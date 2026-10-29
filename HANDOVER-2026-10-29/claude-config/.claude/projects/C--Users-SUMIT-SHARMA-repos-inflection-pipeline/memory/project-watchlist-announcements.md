---
name: project-watchlist-announcements
description: Daily 05:00 Screener watchlist announcement download + full-read digest against Notion theses; replaced the 4-hourly feed on 2026-10-03
metadata:
  node_type: memory
  type: project
  originSessionId: 342c6778-4b97-4372-891b-051ba4be1756
  modified: 2026-10-03T15:27:13.937Z
---

Lives in `C:\ConcallPipeline\Daily Concall Intelligence\` (not a git repo).
- `fetch_announcements.py` / `.bat`, Task Scheduler "Watchlist Announcements 0500": downloads every Screener feed item since `announcements\last_run.txt` into `announcements\<since>_to_<now>\` with INDEX.md (Key documents block first: annual reports, transcripts, presentations, meet notices).
- Feed pages: GET `/dash/85202/?timestamp=<data-last-timestamp>` needs header `X-Requested-With: XMLHttpRequest`, else page 1 repeats. Scrolling loads nothing.
- Old 4-hourly feed stopped 2026-10-03: its two .bat files were replaced with `exit /b 0` (tasks need admin to disable; backups `.bak-2026-10-03`).
- Digest run 2026-10-03 over 1-3 Oct (141 items, 126 PDFs, 1,230 pages): text in `text/`, batches in `work/`, per-batch cards in `cards/`, Notion COMPANIES MASTER data source 345bb2b9-d3ab-8032-9b46-000ba16ab827 (read-only).

- Deep review (operator rejected the shallow digest 2026-10-03): `prep_review.py` -> Opus analysts per T-group / Sonnet per N-group (`review_spec\COMPANY_ANALYST.md`, bar = `STYLE_SAMPLE.md`, the operator's own review) -> Opus assembler writes frame only (`ASSEMBLER.md`) -> `stitch_review.py` pastes sections verbatim into REVIEW.md. Claude scheduled task `daily-watchlist-deep-review` cron 20 5 (fires ~05:32 with jitter). First full run: ~6.8M tokens, ~40 min, 2.5-day window.

**Why:** operator spent 1h+ each morning downloading and feeding PDFs by hand.
**How to apply:** see [[feedback-read-every-announcement]] for how the digest must be written.
