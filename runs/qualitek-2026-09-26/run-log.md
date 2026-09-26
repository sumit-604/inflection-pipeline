# RUN LOG — QUALITEK 2026-09-26

- step1: identity resolved to BSE SME 544091 (/company/QUALITEK/ is 404). Run built in worktree .claude/worktrees/qualitek on branch run/qualitek-2026-09-26 off origin/main (a7765099), because the main checkout carries the operator's uncommitted framework edits.
- collector: run from a scratchpad copy with REPO_ROOT pointed at the worktree (the script hardcodes the main checkout path). Live tools/collector/companies.txt overwritten per Step E; the prior RAPPID content saved as companies.txt.rappid-bak (main checkout, untracked).
- corpus repair: results, decks, MD&A, DRHP and 30 Reg 30 filings pulled from BSE; 15 byte duplicates removed; text extracted with pymupdf (pdftoppm absent).
- LESSONS PRE-READ: open actions printed in chat (Amendment 14 fade guard; canary API key; cross-family grader deferred; fetch_bse_announcements untested -> TESTED this run: it returned 12 filings for scrip 544091, all real, but only the last ~12 months and capped at 25; the month-window query found 135 since listing; pending-for-next-prompt-branch items 1-3). No lessons tagged [sector: Consulting / Engineering services]; no archetype declared yet.
- stage 0: B00 written inline, corpus commit 93ec0142.
