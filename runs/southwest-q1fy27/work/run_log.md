# Run Log — SOUTHWEST Q1 FY27 Quarterly Review

Date: 2026-07-21
Ticker: SOUTHWEST (South West Pinnacle Exploration Ltd, BSE 543986 / NSE SOUTHWEST)
Quarter: Q1 FY27 (Apr-Jun 2026)

## Toolchain
pdftotext / pdfinfo / pdftoppm / tesseract — installed OK (poppler-utils fetched after apt-get update; tesseract 5.3.4).

## Protocol files — present
- frameworks/Quarterly_Results_Review_Protocol_v1_2.md
- frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md
- frameworks/Master_Project_Prompt_v3.3.md

## Documents supplied & class detection (from content)
- Doc A (pressrelease_southwest_q1fy27.pdf, 4 pp): cover letter + "Investor Release" narrative;
  consolidated-only headline table + Q1 highlights + CMD commentary. CLASS = results
  (results press release). NOTE: NOT a Reg 33 Statement of Unaudited Financial Results —
  no standalone numbers, no notes, no auditor limited-review report, no Board Outcome.
- Doc B (presentation_southwest_q1fy27.pdf, 40 pp): investor presentation slides incl.
  financial-statement slides (pg33 qtrly consol income stmt, pg35 hist income stmt,
  pg36 consol balance sheet, pg37 consol perf, pg38 capital market). CLASS = presentation.

## MATERIAL INPUT GAP (flagged, non-halting per orchestrator)
The formal Reg 33 "Statement of Unaudited Financial Results" (standalone+consolidated,
notes, auditor's limited review, Board Outcome) was NOT provided. Role 4 forensic checks
that require it (standalone/consolidated PAT gap, auditor-para diff, Board Outcome items,
notes incl. exceptional/other-income lines) will return N.A. for want of source. This is
the exact artifact the pipeline's origin-miss lived in; user instructed to proceed anyway.

## Company memory
No companies/SOUTHWEST.md exists. No prior per-company memory. First quarterly run.
