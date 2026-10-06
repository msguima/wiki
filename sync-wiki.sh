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
PUBLISH=(
  areas
  concepts
  connections
  entities
  papers
  projects
  questions
  overview.md
  ai-authorship.md
  # Course teaching material: lecture notes, syllabi, reference appendices,
  # notation conventions. Skeletons and supervision docs stay private.
  courses/2026-algebraic-qft-course/notes
  courses/2026-algebraic-qft-course/appendices
  courses/2026-algebraic-qft-course/syllabus.md
  courses/2026-algebraic-qft-course/conventions.md
  courses/ads-cft-course/notes
  courses/ads-cft-course/appendices
  # Figures embedded in the holography lectures, prefixed ads-cft-.
  courses/ads-cft-course/assets
  courses/ads-cft-course/syllabus.md
  courses/ads-cft-course/conventions.md
  courses/generalized-symmetries-course/notes
  courses/generalized-symmetries-course/appendices
  # Figures of the generalized-symmetries notes, prefixed gs-, drawn by script
  # in the lecture dossier.
  courses/generalized-symmetries-course/assets
  courses/generalized-symmetries-course/syllabus.md
  courses/generalized-symmetries-course/conventions.md
  # The neural-networks/LLM course prefixes its files nn-llm- and carries
  # reader-facing navigation the older courses lack (start here, week map,
  # glossary, resources), plus the first figures on the site in assets/.
  courses/neural-networks-llms-course/notes
  courses/neural-networks-llms-course/appendices
  courses/neural-networks-llms-course/assets
  courses/neural-networks-llms-course/nn-llm-syllabus.md
  courses/neural-networks-llms-course/nn-llm-conventions.md
  courses/neural-networks-llms-course/nn-llm-start-here.md
  courses/neural-networks-llms-course/nn-llm-week-map.md
  courses/neural-networks-llms-course/nn-llm-glossary.md
  courses/neural-networks-llms-course/nn-llm-resources.md
  # Geometric QCD, a critical course on Migdal's IAS lectures: the guide, the
  # five modules with their 35 lectures, the reference pages and the figures
  # in assets/, prefixed geometric-qcd-. The lecture standard stays in the
  # vault; the instructor guide, with the assessments, stays in the dossier.
  courses/geometric-qcd-course/modules
  courses/geometric-qcd-course/appendices
  courses/geometric-qcd-course/assets
  courses/geometric-qcd-course/geometric-qcd-course-guide.md
  courses/geometric-qcd-course/syllabus.md
  courses/geometric-qcd-course/conventions.md
  courses/geometric-qcd-course/notation.md
  courses/geometric-qcd-course/glossary.md
  courses/geometric-qcd-course/bibliography.md
  courses/geometric-qcd-course/exercises.md
  courses/geometric-qcd-course/claim-status-map.md
  courses/geometric-qcd-course/source-map.md
)

# People notes that stay private (junior researchers; see wiki/entities/),
# plus internal course documents (organizational crosswalk), plus the one
# generalized-symmetries note that follows the group's unpublished manuscript
# in detail, held back until the manuscript is public (decision of 2026-10-04),
# with its five figures.
EXCLUDE=(
  entities/ismael-porfirio.md
  entities/erick-landim.md
  entities/luigi-carvalho-ferreira.md
  courses/ads-cft-course/appendices/adscft-org-crosswalk.md
  courses/generalized-symmetries-course/notes/sem2-week-14-defect-condensation-and-julia-toulouse.md
  courses/generalized-symmetries-course/assets/gs-s2w14-current-clock.svg
  courses/generalized-symmetries-course/assets/gs-s2w14-endpoint-regimes.svg
  courses/generalized-symmetries-course/assets/gs-s2w14-small-sheet.svg
  courses/generalized-symmetries-course/assets/gs-s2w14-splitting.svg
  courses/generalized-symmetries-course/assets/gs-s2w14-wall.svg
)

# Clear the previous copy, keeping the hand-written landing page.
find "$DEST" -mindepth 1 -maxdepth 1 ! -name 'index.md' -exec rm -rf {} +

for item in "${PUBLISH[@]}"; do
  [ -e "$SRC/$item" ] || { echo "error: missing $item in $SRC" >&2; exit 1; }
  # cp -R with a path only keeps the last component; recreate the parent
  # dirs so courses/<course>/notes lands at content/courses/<course>/notes
  mkdir -p "$DEST/$(dirname "$item")"
  cp -R "$SRC/$item" "$DEST/$(dirname "$item")/"
done

for item in "${EXCLUDE[@]}"; do
  rm -f "$DEST/$item"
done

find "$DEST" -name '.DS_Store' -delete

python3 "$CULL" "$SRC" "$DEST"
