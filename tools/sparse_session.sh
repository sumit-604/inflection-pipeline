#!/usr/bin/env bash
# Sparse checkout for one pipeline session (branch audit item 22, operator
# ruling 2026-10-03). Keeps everything outside runs/, every run's
# session-cost.md and manifest.yaml (COST SPIKE checks and company memory
# links need them), and the run folders named on the command line.
#
# Usage:  tools/sparse_session.sh runs/<ticker>-<date> [more run folders...]
#         tools/sparse_session.sh --off      # back to a full checkout
#
# Effect: the working tree drops from about 4.8 GB to tens of MB. The git
# history and every branch stay intact; nothing is deleted from the repo.
# A run folder not listed is absent from disk until you add it:
#         tools/sparse_session.sh runs/<a> runs/<b>
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
if [ "${1:-}" = "--off" ]; then
  git sparse-checkout disable
  echo "full checkout restored"
  exit 0
fi
if [ "$#" -lt 1 ]; then
  sed -n '2,15p' "$0"; exit 2
fi
patterns=('/*' '!/runs/*/*' '/runs/*/session-cost.md' '/runs/*/manifest.yaml')
for r in "$@"; do
  r="${r%/}"; r="${r#./}"
  case "$r" in runs/*) ;; *) echo "not a run folder: $r" >&2; exit 2 ;; esac
  patterns+=("/$r/**")
done
git sparse-checkout set --no-cone "${patterns[@]}"
echo "sparse checkout set:"; printf '  %s\n' "${patterns[@]}"
du -sh --exclude=.git . 2>/dev/null | tail -1
