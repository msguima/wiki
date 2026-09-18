#!/bin/bash
# Publishes the public subset of the physics-wiki vault into content/,
# from where Quartz builds the site at msguima.github.io/wiki/.
#
#   ./sync-wiki.sh                 # uses ~/Projects/physics-wiki
#   ./sync-wiki.sh <vault-dir>
#
# The vault is the source of truth and stays private: only the directories
# in PUBLISH below are copied, and raw/, courses/, sources/ and the vault
# index never leave it. scripts/cull-links.py then rewrites wiki links that
# point to non-published notes into plain text and maps last_updated to the
# frontmatter key Quartz reads for dates. content/ is generated — edit the
# vault, rerun this, review the diff, commit and push.
#
# content/index.md is the hand-written landing page of this repository and
# survives every run.
set -euo pipefail

VAULT="${1:-$HOME/Projects/physics-wiki}"
SRC="$VAULT/wiki"
ROOT="$(cd "$(dirname "$0")" && pwd)"
DEST="$ROOT/content"
CULL="$ROOT/scripts/cull-links.py"

[ -d "$SRC/areas" ] || { echo "error: no wiki/ under $VAULT" >&2; exit 1; }

# Everything the public site may contain. Add to this list, never to a copy.
PUBLISH=(areas concepts connections entities papers projects questions overview.md)

# People notes that stay private (junior researchers; see wiki/entities/).
EXCLUDE=(
  entities/ismael-porfirio.md
  entities/erick-landim.md
  entities/luigi-carvalho-ferreira.md
)

# Clear the previous copy, keeping the hand-written landing page.
find "$DEST" -mindepth 1 -maxdepth 1 ! -name 'index.md' -exec rm -rf {} +

for item in "${PUBLISH[@]}"; do
  [ -e "$SRC/$item" ] || { echo "error: missing $item in $SRC" >&2; exit 1; }
  cp -R "$SRC/$item" "$DEST/"
done

for item in "${EXCLUDE[@]}"; do
  rm -f "$DEST/$item"
done

find "$DEST" -name '.DS_Store' -delete

python3 "$CULL" "$SRC" "$DEST"
