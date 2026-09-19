#!/usr/bin/env python3
"""Post-process the published copy of the physics-wiki vault.

Run by sync-wiki.sh after the allowlisted files are copied into content/.
Passes over each markdown file:

  1. frontmatter: last_updated: -> modified:, the key Quartz reads for the
     "last modified" date shown on every page.
  2. ambiguous wikilinks: the three courses ship files with the same stem
     (syllabus, conventions, bibliography-and-paper-map). A bare
     [[syllabus]] inside a course's files means that course's file, so it is
     rewritten to the folder-qualified target Quartz resolves by path;
     the same bare link from outside courses/ cannot be attributed and
     becomes plain text.
  3. wikilinks: [[target]] or [[target|alias]] pointing at a vault note that
     is not part of the published subset is replaced by plain text (the alias
     when one is given). Links to targets that exist nowhere in the vault are
     left alone: disableBrokenWikilinks in quartz.config.ts renders them as
     dimmed anchors, marking them as notes yet to be written.

Usage: cull-links.py <vault-wiki-dir> <content-dir>
"""

import re
import sys
from collections import Counter
from pathlib import Path

WIKILINK = re.compile(r"!?\[\[([^\[\]]+?)\]\]")


def split_target(raw: str) -> tuple[str, str]:
    """Split 'target\\|alias' or 'target|alias' into (target, display)."""
    parts = re.split(r"\\\||\|", raw, maxsplit=1)
    target = parts[0].strip()
    display = parts[1] if len(parts) > 1 else None
    if display is None:
        display = target.split("#", 1)[0]
    return target, display.replace("\\|", "|")


def inventory(root: Path) -> dict[str, set[Path]]:
    stems: dict[str, set[Path]] = {}
    for path in root.rglob("*.md"):
        stems.setdefault(path.stem, set()).add(path)
    return stems


def main() -> int:
    vault = Path(sys.argv[1])
    content = Path(sys.argv[2])

    vault_stems = inventory(vault)

    published_files = sorted(content.rglob("*.md"))
    pub_stems = {p.stem for p in published_files}
    # stems carried by more than one published file are ambiguous as bare links
    stem_count: Counter[str] = Counter(p.stem for p in published_files)
    ambiguous = {s for s, n in stem_count.items() if n > 1}

    culled: Counter[str] = Counter()
    dead: Counter[str] = Counter()
    disambiguated: Counter[str] = Counter()
    files_touched = 0

    for path in published_files:
        text = path.read_text(encoding="utf-8")
        original = text
        rel = path.relative_to(content)

        # Pass 1: frontmatter date key.
        if text.startswith("---\n"):
            end = text.find("\n---\n", 3)
            if end != -1:
                head = text[: end + 5]
                body = text[end + 5 :]
                head = re.sub(r"(?m)^last_updated:", "modified:", head)
                text = head + body

        # Pass 2/3: wikilinks.
        def cull(match: re.Match) -> str:
            embed = "!" if match.group(0).startswith("!") else ""
            target, display = split_target(match.group(1))
            anchor = ""
            if "#" in target:
                target, anchor = target.split("#", 1)
                anchor = "#" + anchor
            stem = target.strip().rstrip("/")
            if not stem or stem.startswith("#"):
                return match.group(0)  # same-page section link

            if stem in ambiguous:
                # inside a course, a bare ambiguous stem means that course's file
                parts = rel.parts
                if len(parts) >= 3 and parts[0] == "courses":
                    qualified = f"{parts[0]}/{parts[1]}/{stem}"
                    if (content / f"{qualified}.md").is_file():
                        disambiguated[stem] += 1
                        had_alias = "|" in match.group(1)
                        if had_alias:
                            return f"{embed}[[{qualified}{anchor}|{display}]]"
                        return f"{embed}[[{qualified}{anchor}]]"
                culled[stem] += 1
                return display
            if stem in pub_stems:
                return match.group(0)
            if stem in vault_stems:
                culled[stem] += 1
                return display
            dead[stem] += 1
            return match.group(0)

        text = WIKILINK.sub(cull, text)

        if text != original:
            path.write_text(text, encoding="utf-8")
            files_touched += 1

    print(f"cull-links: rewrote {files_touched} files")
    if disambiguated:
        print(f"  ambiguous stems -> folder-qualified ({sum(disambiguated.values())} links):")
        for stem, n in sorted(disambiguated.items(), key=lambda kv: -kv[1]):
            print(f"    {stem} x{n}")
    if culled:
        print(f"  private targets -> plain text ({sum(culled.values())} links):")
        for stem, n in sorted(culled.items(), key=lambda kv: -kv[1]):
            print(f"    {stem} x{n}")
    if dead:
        print(f"  targets missing from the vault ({sum(dead.values())} links, left as dimmed anchors)")
        print(f"    {', '.join(sorted(dead))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
