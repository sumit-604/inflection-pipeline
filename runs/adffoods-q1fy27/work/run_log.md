# Quarterly Analysis Pipeline Run Log — ADFFOODS Q1 FY27

Run date: 2026-07-30
Ticker: ADFFOODS (ADF Foods Limited, NSE: ADFFOODS / BSE: 519183)
Quarter detected: Q1 FY27 (quarter ended 30 June 2026)
Operator: Keerti Kaushik

## Toolchain precheck
- pdftotext, pdfinfo, pdftoppm: INSTALLED (poppler-utils 24.02.0)
- tesseract: INSTALLED (5.3.4)
- Note: deadsnakes/ondrej PPAs were blocking apt; removed to install from main archives.

## Document classification (by content, not filename)
| ID | Source file | Pages (pdfinfo=pdftoppm) | Class | Basis |
|----|-------------|-------|-------|-------|
| D1 | results_boardoutcome_q1fy27.pdf | 8 | results | Reg 30 & 33 Board Outcome + Unaudited Standalone & Consolidated Financial Results Q1FY27 + Limited Review Report (MSKA & Associates LLP) |
| D2 | presentation_q1fy27.pdf | 50 | presentation | Investor / Corporate Presentation Q1FY27, slide structure |
| D3 | pressrelease_q1fy27.pdf | 4 | presentation (management narrative) | Press Release of Q1 FY2026-27 Financials; no concall supplied so this is the primary management-commentary source |
| D4 | disclosure_ireland_subsidiary.pdf | 2 | results (corporate action) | Reg 30 intimation: incorporation of wholly owned step-down subsidiary in Ireland (same 29-Jul-2026 board meeting) |

Page-count note: the Read-tool renderer earlier reported 39/94 pages for D1/D2; pdfinfo AND pdftoppm both report 8/50. The pdftext/pdfinfo count is the authoritative evidence spine; the renderer figure is a rendering artifact and is disregarded.

## Chain plan
- Full A1 -> A2 -> A3: D1 (results), D2 (presentation), D3 (press release).
- A1 extract only for D4 (Ireland subsidiary); its content (new step-down entity, board approval, Europe growth commitment) is passed inline to A4 as an F13/F15/F6 corporate-action signal.
- A4 once (merged). A5 once (adversary).

## Company memory / Notion
- companies/ADFFOODS.md: ABSENT (new company to the pipeline).
- Notion page: checked (see below).
