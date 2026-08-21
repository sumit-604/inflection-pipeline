#!/bin/bash
# Inflection Alpha pipeline: mandatory session-start sync.
# Before any framework or prompt is read, pull origin/main so the
# session never runs stale rules. Conflicts under frameworks/, prompts/,
# and .claude/ resolve by keeping origin/main. Then surface the
# frameworks/ SHAs into session context so the model can see them.
#
# Runs only in Claude Code on the web (fresh clones). It is skipped
# locally, where the operator may hold uncommitted framework edits that
# an auto-merge would clobber.
#
# No -e: a git or network failure must not block the session. Instead the
# failure is reported loudly through additionalContext, because a silent
# skip is the exact failure this hook exists to prevent.
set -uo pipefail

# stdout carries ONLY the final JSON. All logs go to stderr.
log() { echo "$@" >&2; }

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-.}" 2>/dev/null || exit 0

# A merge commit needs an identity. Set a fallback only if none exists.
if ! git config --get user.email >/dev/null 2>&1; then
  git config user.email "session-hook@inflection.local"
fi
if ! git config --get user.name >/dev/null 2>&1; then
  git config user.name "inflection session hook"
fi

WARN=""
ALLOW='^(frameworks/|prompts/|\.claude/)'

if git fetch origin main >&2 2>&1; then
  if git merge --no-edit origin/main >&2 2>&1; then
    log "merge clean"
  else
    CONFLICTS="$(git diff --name-only --diff-filter=U)"
    OUTSIDE="$(printf '%s\n' "$CONFLICTS" | grep -vE "$ALLOW" || true)"
    if [ -n "$OUTSIDE" ]; then
      git merge --abort >&2 2>&1 || true
      WARN="MERGE ABORTED. Conflicts outside frameworks/, prompts/, .claude/ need manual resolution against origin/main before rules are trusted. Conflicted paths: $(printf '%s ' $CONFLICTS)"
    else
      # Keep origin/main (theirs) for every conflicted allowed path.
      while IFS= read -r f; do
        [ -n "$f" ] || continue
        git checkout --theirs -- "$f" >&2 2>&1 || true
        git add -- "$f" >&2 2>&1 || true
      done <<< "$CONFLICTS"
      git commit --no-edit >&2 2>&1 || true
      log "merge conflicts resolved keeping origin/main"
    fi
  fi
else
  WARN="git fetch origin main FAILED (network?). Framework and prompt rules may be STALE this session."
fi

SHAS="$(git ls-tree -r HEAD -- frameworks/ 2>/dev/null | awk '{print $3"  "$4}')"

CTX="inflection-pipeline session-start sync ran (origin/main pulled before any framework read)."
if [ -n "$WARN" ]; then
  CTX="$CTX

WARNING: $WARN"
fi
CTX="$CTX

frameworks/ SHAs (git blob, HEAD after sync):
$SHAS"

python3 - "$CTX" <<'PY'
import json, sys
print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": sys.argv[1],
    }
}))
PY
