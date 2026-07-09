# Inflection Alpha Pipeline

Sonnet 5 primary research pipeline with Claude verification layer.
Runs on Claude Code (web, desktop, or CLI). Built July 2026.

## One-time setup (works entirely from a Chromebook browser)

1. Create a PRIVATE repo on github.com (e.g. inflection-pipeline).
2. Upload this bundle: on the repo page, "uploading an existing file",
   drag the extracted folder contents in, commit. (Drag the CONTENTS of
   the folder, not the folder itself, so CLAUDE.md sits at repo root.
   GitHub's web upload preserves subfolders when you drag folders in.)
3. Copy your three framework files into frameworks/ (see the README
   there). Upload via the same web UI.
4. Go to claude.ai/code, connect your GitHub account, grant access to
   this repo. Requires Pro or Max; Max recommended for full runs.

## Per run

1. On github.com, create runs/<ticker>-<date>/ by copying _template:
   easiest is "Add file > Create new file" for manifest.yaml (path
   runs/TICKER-2026-07-15/manifest.yaml), then upload the PDFs into
   runs/TICKER-2026-07-15/inputs/ via drag and drop.
2. At claude.ai/code, start a session on this repo:
   /run-pipeline runs/TICKER-2026-07-15
3. The session runs all stages, commits outputs, and reports the
   verdict. Close the browser; it keeps running. Monitor from the
   Claude mobile app.
4. Results land in runs/<folder>/outputs/final/ on a claude/ branch or
   PR; review and merge.

## Repo map

CLAUDE.md               constitution: non-negotiables, dispatch, style
prompts/                14 stage instruction files (source of truth)
frameworks/             valuation authority docs (you maintain)
.claude/agents/         16 subagents with per-stage model routing
.claude/commands/       /run-pipeline orchestration command
runs/                   one folder per company run

## Costs

Runs draw subscription usage (not API billing). A full run is heavy:
~15 documents read, 19 subagent invocations. Expect roughly one full
run per day within Max 5x limits; Pro will likely cap out mid-run.
First run: use a company you know well and compare against your
existing thesis before trusting output.
