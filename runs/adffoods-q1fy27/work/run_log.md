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

## Notion (fetched + saved live, 2026-07-30)
- Company page found: "🍛 ADF Foods Limited" (COMPANIES MASTER db). Live thesis extracted to notion_thesis_inline.md.
- Decision Status verified BEFORE analysis and AFTER save: WATCHLIST / AVOID (unchanged; no pre-committed trigger fired -> flag, not decide). Entry 204/205, MoS 181/182, Promoter CAUTION all unchanged.
- Full merged review + Questions-for-Management + A3 forensic scorecard + A5 audit verdict appended to page body (position end, 5 sequential inserts). Page grew 170k -> 226k chars.
- Key Notes property: new dated Q1 FY27 entry PREPENDED; all prior entries (18-Jul AR, 28-Jun PM, 28-Jun AM) preserved verbatim; verified no escaping corruption. Backup of prior value in _keynotes_current.txt.

## Gate log (all mechanical gates)
- Gate A1: PASS x4 (results 8pp, presentation 50pp/12 OCR, press release 4pp, Ireland letter 2pp; 100% page coverage each).
- Gate A2: PASS x3 (results 8 notes/76 items; presentation 50 slides/285 metrics; press release 57 units). Count tests reconciled.
- Gate A3: PASS x3 (all F1-F17 statused, every FINDING line-cited).
- Gate A5: COMPLETE after 2 loop-backs (loop 0 flat-EBITDA read; loop 1 standalone-clean-read error; loop 2 COMPLETE). Max-2-loop rule respected; no human escalation.

## Count-reconciliation line
8 notes / 0 concall turns / 50 slides / 57 press-release units + 8-row Ireland Annexure — all reviewed.

## Protocol verdict: PROCEED WITH FLAGS | cash conversion INDETERMINATE | Decision Status WATCHLIST / AVOID (unchanged).

RUN CLOSE 2026-07-30: A5 caught a material read error twice (reported +26% EBITDA growth is entirely a Rs 7.29 Cr Note-6 tariff credit; underlying operating EBITDA declined YoY on both bases). Two A4<->A5 loops resolved it. No concall or prior-quarter ledger supplied (documented). Toolchain absent at start (installed poppler-utils + tesseract after removing broken PPAs). Otherwise clean run.
