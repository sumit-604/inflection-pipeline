#!/usr/bin/env bash
# Daily canary wrapper for cron. Loud on drift, quiet on clean.
# Cron example (07:30 daily), assuming the key lives in ~/.inflection.env:
#   30 7 * * * /home/user/inflection-pipeline/canary/run-daily.sh >> /home/user/inflection-pipeline/canary/canary.log 2>&1
set -u

REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO" || exit 2

# Load ANTHROPIC_API_KEY from a private env file if present (keep it out of git).
[ -f "$HOME/.inflection.env" ] && . "$HOME/.inflection.env"

echo "===== canary $(date -u +%FT%TZ) ====="
python3 canary/verifier.py
code=$?
if [ "$code" -ne 0 ]; then
  echo "CANARY DRIFT DETECTED — pipeline blocked. See canary/DRIFT.flag and canary/state.json."
  # Add your own notification here if desired (mail, ntfy, etc.).
fi
exit "$code"
