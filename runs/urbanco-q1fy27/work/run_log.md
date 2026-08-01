# RUN LOG — /run-quarterly URBANCO Q1 FY27

Orchestrator: quarterly-00-orchestrator.md v1.0
Run date: 2026-07-31
Ticker: URBANCO (NSE) / 544515 (BSE)
Quarter detected: Q1 FY27 (quarter ended June 30, 2026)

## PRECHECKS
- Protocol files: PRESENT (Results v1.2, Concall v1.1, Master v3.3)
- Toolchain: pdftotext / pdfinfo / pdftoppm / tesseract — installed OK
  (poppler-utils + tesseract-ocr via apt after `apt-get update`)
- Company memory companies/URBANCO.md: ABSENT (first quarterly run for this ticker)

## DOCUMENT CLASS DETECTION
- D2 (11 pages) -> RESULTS. Reg 30+33 Board Outcome letter; Limited Review
  Report (consolidated) + Annexure I entity list; Statement of consolidated
  financial results + Notes; Limited Review Report (standalone) + Statement of
  standalone financial results + Notes. Statutory filing = primary evidence.
  inputs/results_URBANCO_q1fy27.pdf
- D1 (5 pages) -> PRESENTATION. Reg 30 media release (press release) with
  operating metrics: NTV, Adjusted EBITDA, segment splits (India Consumer
  Services ex-InstaHelp, International, Native, InstaHelp). No statutory
  statements. Investor summary feeding Role 4/Role 5.
  inputs/presentation_media_release_URBANCO_q1fy27.pdf
- CONCALL: none supplied. Role 5 has no transcript this run; A4 runs Role 4
  plus presentation cross-checks. Concall analysis deferred.

## COMPANY MEMORY / NOTION
- No companies/URBANCO.md. Notion page fetch attempted at orchestrator step 0F.

## PIPELINE OUTCOME (2026-07-31)
- A1 results: PASS (11/11 pages, 582 lines, no OCR). A1 presentation: PASS (5/5 pages).
- A2 results: PASS (16 notes / 88 line items / 9 ZERO_STANDING / 10 entities / 14 auditor paras).
  A2 presentation: PASS (5 slides / 158 numeric tokens / 14 footnotes).
- A3 results: GATE PASS (17/17 checks; 10 FINDINGs). A3 presentation: GATE PASS (17/17; 4 FINDINGs).
- A4: merged review written. Protocol verdict PROCEED WITH CAVEATS (capped by INDETERMINATE cash
  conversion). Decision Status UNCHANGED WATCHLIST/AVOID; no thesis-broken trigger fired. 12 mgmt Qs.
- A5: VERDICT COMPLETE (0 orphan rows / 0 arithmetic mismatches / 0 surviving bear counters). No loop-back.
- NOTION SAVE: done. Full review + A3 forensics tables + A5 verdict inserted at page end; Key Notes
  audit trail prepended (prior entries preserved); Decision Status not changed (no trigger fired).
- Count reconciliation: 16 notes / 0 turns / 5 slides, all reviewed.

## CONCALL ADDENDUM (2026-08-01)
- Concall transcript (pasted text) added. A1 concall PASS (102 lines verbatim). A2 concall PASS
  (51 turns / 16 questions / 103 mgmt numbers). A3 concall PASS (17/17; F6/F7/F14/F16/F17 findings;
  26 findings incl 7-of-12 prior questions NOT ADDRESSED, CFO silent, ATU 9.3m vs 8.2m).
- A4 Role 5 addendum written (review_addendum_concall_URBANCO_q1fy27.md); verdict UNCHANGED
  PROCEED WITH CAVEATS; Decision Status UNCHANGED WATCHLIST/AVOID; 0 thesis-broken triggers fired;
  spine ties EXACT on statutory; Closing Brief included.
- A5 addendum audit: VERDICT COMPLETE (0 orphan / 0 arithmetic mismatch / 0 surviving bear counters).
- NOTION SAVE: full concall addendum inserted at page end; Key Notes prepended with dated concall entry.
- Count reconciliation (cumulative): 16 notes / 51 turns / 5 slides, all reviewed.
