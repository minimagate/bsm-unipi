#!/usr/bin/env sh
# Local preview: regenerate content/ from an Obsidian vault, then serve the site.
# Usage: scripts/dev.sh <vault_root>   (or set BSM_VAULT)
set -eu
VAULT="${1:-${BSM_VAULT:-}}"
if [ -z "$VAULT" ]; then
  echo "usage: scripts/dev.sh <vault_root>  (or set BSM_VAULT)" >&2
  exit 2
fi
cd "$(dirname "$0")/.."
python3 scripts/build_content.py "$VAULT"
exec zola serve
