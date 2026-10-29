#!/usr/bin/env python3
"""Deferred-work check (CLAUDE.md, FERRY AND COMMIT HYGIENE).

A commit message or PR description that contains a deferred-work phrase needs
a matching LESSONS line. A commit matches when it changes LESSONS.md or
LESSONS_ARCHIVE.md itself, or when either file names its 8-character hash.
A PR matches when either file names it as "#N".

Usage: lessons-phrase-check.py <repo root> [--prs-json -]
With --prs-json -, the PR list (gh pr list --json number,title,body) is read
from stdin. The hook runs gh in bash, where gh's sign-in is visible, and pipes
the JSON in. Without it, PR descriptions are reported as not checked.

Called by .claude/hooks/session-start.sh. Read-only. Prints nothing when every
item matches and PRs were checked. Never blocks a session: exit code is 0.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

SINCE_DATE = "2026-09-15"                  # rule adoption date
GIT_SINCE = SINCE_DATE + "T00:00:00"       # a bare date means "that day, at the current time" to git
PHRASES = ("open action", "left for later", "recorded as")
LESSON_FILES = ("LESSONS.md", "LESSONS_ARCHIVE.md")


def run(args, timeout=20):
    result = subprocess.run(args, capture_output=True, text=True,
                            encoding="utf-8", errors="replace", timeout=timeout)
    return result.returncode, result.stdout


def first_phrase(text):
    low = text.lower()
    return next((p for p in PHRASES if p in low), None)


def main(argv):
    root = Path(argv[1]) if len(argv) > 1 and not argv[1].startswith("--") else Path.cwd()
    prs_from_stdin = "--prs-json" in argv
    git = ["git", "-C", str(root)]
    lessons = "\n".join(
        (root / name).read_text(encoding="utf-8", errors="replace")
        for name in LESSON_FILES if (root / name).exists()
    ).lower()

    problems, notes = [], []

    refs = ["HEAD"]
    if run(git + ["rev-parse", "--verify", "-q", "origin/main"])[0] == 0:
        refs.append("origin/main")
    code, out = run(git + ["log", *refs, f"--since={GIT_SINCE}",
                           "--format=%H%x1f%s%x1f%B%x1e"])
    if code != 0:
        notes.append("git log failed, so commit messages were not checked")
    else:
        for record in out.split("\x1e"):
            record = record.strip()
            if not record:
                continue
            sha, subject, body = (record.split("\x1f") + ["", ""])[:3]
            phrase = first_phrase(body)
            if not phrase:
                continue
            short = sha[:8].lower()
            _, touched = run(git + ["show", "--name-only", "--format=", sha])
            if any(name in touched.split() for name in LESSON_FILES) or short in lessons:
                continue
            problems.append(f'commit {short} "{subject[:70]}" (phrase: "{phrase}")')

    raw = sys.stdin.read() if prs_from_stdin else ""
    if not raw.strip():
        notes.append("PR descriptions were not checked (gh unavailable or not signed in)")
    else:
        try:
            for pr in json.loads(raw):
                phrase = first_phrase(pr.get("body") or "")
                if phrase and not re.search(rf"#{pr['number']}\b", lessons):
                    problems.append(f'PR #{pr["number"]} "{(pr.get("title") or "")[:70]}" (phrase: "{phrase}")')
        except (ValueError, KeyError, TypeError) as exc:
            notes.append(f"PR list could not be read ({type(exc).__name__}), so PRs were not checked")

    if problems:
        lines = [f"LESSONS CHECK (CLAUDE.md deferred-work rule): {len(problems)} item(s) "
                 f"since {SINCE_DATE} use a deferred-work phrase but have no matching "
                 "LESSONS.md or LESSONS_ARCHIVE.md line:"]
        lines += [f"- {p}" for p in problems]
        lines += [f"Note: {n}." for n in notes]
        print("\n".join(lines))
    elif notes:
        print("LESSONS CHECK: no unmatched deferred-work phrases found. Note: "
              + "; ".join(notes) + ".")


if __name__ == "__main__":
    try:
        main(sys.argv)
    except Exception as exc:
        print(f"LESSONS CHECK: skipped ({type(exc).__name__}: {exc})")
    sys.exit(0)
