#!/usr/bin/env sh
# Local preview: regenerate content/ from notes/, then serve the site.
# Extra arguments go to scripts/build_content.py (e.g. --strict).
set -eu
cd "$(dirname "$0")/.."
python3 scripts/build_content.py "$@"
exec zola serve
