# LESSONS — Inflection Alpha Pipeline

Operational memory. Every session reads this file at start. Every
/run-pipeline, /fttcp, and /finalize session appends one dated entry at
close: what broke or dragged this run, in one line each; write "clean run"
if nothing. Entries are never deleted. When a lesson is promoted into a
prompt file so it cannot recur, note it under PROMOTED TO LAW.

Dated entries, newest first within each section. Date format YYYY-MM-DD.
/compost reads this file to find patterns appearing 2+ times and proposes
the prompt-file edits that would make each recur-proof.

## RECURRING PATTERNS
_Patterns seen across more than one run. This is the section /compost mines
for 2+ occurrences._

- Operator pastes of text as chat attachments arrive empty; screenshots and direct chat-box text always work; .md/.txt file uploads work. (Observed 6+ times.)

## WHAT BROKE AND THE FIX
_A mechanical failure or wrong output this run, and what resolved it._

- [2026-07-11] FTTCP rewrite drafted in chat but never landed in repo; old interactive behavior recurred across three companies. Law: every repo task ends with an explicit merge reminder, and no dependent session starts until the merge is confirmed on main.
- [2026-07-11] Identical final filenames across run folders caused a wrong-company upload (Apex payload grabbed for an Akums save). Candidate law: finals get ticker-prefixed names (AKUMS-notion-payload.md), or the payload's first line must state ticker plus run date in bold.
- [2026-07-11] Repo tasks are not done at 'pushed' — they are done at 'merged.' Unmerged branches are invisible to every new session. After any repo task: push, then immediately merge, then proceed.
- [2026-07-10] Changelog entries must be written by the session that made the change, never pre-supplied by the operator or planner — a pre-supplied changelog claimed the RRM clarification existed when the task had been skipped. Caught by session cross-check; fixed as Amendment 4.4.
- [2026-07-10] Documents added to a local run folder after the initial push do not exist for cloud sessions until --push-again runs. Cost: half a phase-1 re-run on AKUMS (AR, results, rating all local-only). Promoted to law: stage-0 empty-folder pause.
- [2026-07-10] Sessions started before a command-file merge run the OLD rules for their whole life. Fix: after merging any .claude/commands change, kill or finish pre-merge sessions before relying on the new behavior.
- [2026-07-09] Background launch-and-wait stalls silently (2 hours on APEXECO stage 1-2). Promoted to law: foreground execution discipline in run-pipeline.
- [2026-07-09] Interactive section-by-section deliberation frustrates the operator; jargon-dense drafts get rejected. Promoted to law: fttcp autonomous plain-language draft with year-wise tables.
- [2026-07-09] openpyxl read_only leaves Windows file handles open, making staging undeletable and polluting git. Fixed in collect_to_repo v3.1 (wb.close + gitignore _download).
- [2026-07-09] Notion text properties reject < and → characters; EM Classification select lacks NONE, Promoter Verdict select lacks CAUTION. Workaround: clean characters, verdicts to text fields; consider adding select options.

## SLOW SPOTS
_Stages or steps that dragged: where wall-clock or attention went._

(none yet)

## PROMOTED TO LAW
_Lessons written into a prompt file so they cannot recur. Each entry names
the file and the change._

(none yet)
