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
