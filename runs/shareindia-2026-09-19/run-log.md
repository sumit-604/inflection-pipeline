# RUN LOG — SHAREINDIA 2026-09-19

- step1: shared tools/collector/companies.txt was overwritten by concurrent sessions; the first collector run read another session's list (RAPPID). Killed; re-ran from a private copy with its own companies.txt.
- step1: private collector run came back logged out of screener ("Company: Get a free account"); zero files. Corpus built by hand from the BSE announcements API (60-day windows; the collector's 12-month single query returned zero rows), public screener tables, Infomerics (built-in browser to find the rationale link), SEBI and cmsapi.choiceindia.com.
- step1: main working tree is shared by live sessions and switched branch mid-run; the run lives in worktree .claude/worktrees/shareindia (sparse checkout) on run/shareindia-2026-09-19.
- stage 0: done inline by orchestrator. Empty-folder pause suppressed (Step-1 autonomy contract).
- stages 1, 2.1: block files carried markdown code fences; stripped by orchestrator (content unchanged), now parse.
- stage 2 pass 3: B02-notes.input_gaps emitted empty; B00.input_gaps remain authoritative and are passed to every later stage.
- stage 8 found a SEBI AO order (NSE co-location, ~30-May-2022) cited in the Aug-2026 NCLT scheme filing; order text not in corpus; sebi.gov.in search blocked the automated request. B00 amended: freshness pair 3 FAIL, freshness_verdict CORPUS GAPPED-FRESHNESS. Gate caps at PROCEED WITH CAVEATS.
