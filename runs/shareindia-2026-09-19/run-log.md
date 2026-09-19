# RUN LOG — SHAREINDIA 2026-09-19

- step1: shared tools/collector/companies.txt was overwritten by concurrent sessions; the first collector run read another session's list (RAPPID). Killed; re-ran from a private copy with its own companies.txt.
- step1: private collector run came back logged out of screener ("Company: Get a free account"); zero files. Corpus built by hand from the BSE announcements API (60-day windows; the collector's 12-month single query returned zero rows), public screener tables, Infomerics (built-in browser to find the rationale link), SEBI and cmsapi.choiceindia.com.
- step1: main working tree is shared by live sessions and switched branch mid-run; the run lives in worktree .claude/worktrees/shareindia (sparse checkout) on run/shareindia-2026-09-19.
- stage 0: done inline by orchestrator. Empty-folder pause suppressed (Step-1 autonomy contract).
