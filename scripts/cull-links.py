#!/usr/bin/env python3
"""Post-process the published copy of the physics-wiki vault.

Run by sync-wiki.sh after the allowlisted files are copied into content/.
Two passes over each markdown file:

  1. frontmatter: last_updated: -> modified:, the key Quartz reads for the
     "last modified" date shown on every page.
  2. wikilinks: [[target]] or [[target|alias]] pointing at a vault note that
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
    published = {p.stem for p in content.rglob("*.md")}

    culled: Counter[str] = Counter()
    dead: Counter[str] = Counter()
    files_touched = 0

    for path in sorted(content.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        original = text

        # Pass 1: frontmatter date key.
        if text.startswith("---\n"):
            end = text.find("\n---\n", 3)
            if end != -1:
                head = text[: end + 5]
                body = text[end + 5 :]
                head = re.sub(r"(?m)^last_updated:", "modified:", head)
                text = head + body

        # Pass 2: cull wikilinks into the private half of the vault.
        def cull(match: re.Match) -> str:
            target, display = split_target(match.group(1))
            stem = target.split("#", 1)[0].strip()
            if not stem or stem.startswith("#"):
                return match.group(0)  # same-page section link
            if stem in published:
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
