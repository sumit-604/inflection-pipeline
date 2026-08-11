# Run Log — SPAPPAREL Q1 FY27 Quarterly Review

- Invocation: `/run-quarterly SPAPPAREL --docs <uploaded results PDF>`
- Run date: 2026-08-11
- Ticker: SPAPPAREL (BSE 540048 / NSE SPAL) — SP Apparels Limited
- Quarter: Q1 FY27 (quarter ended 30.06.2026)

## Prechecks
- Toolchain: pdftotext/pdfinfo/pdftoppm/tesseract MISSING at start → installed
  via apt (poppler-utils, tesseract-ocr) after `apt-get update`. All OK.
- Protocol files present: Quarterly_Results_Review_Protocol_v1_2.md,
  Quarterly_Concall_Analysis_Protocol_v1_1.md, Master_Project_Prompt_v3.3.md. PASS.

## Document class detection
- Doc 1: 12 pages. Markers: "Outcome of the Board Meeting", Reg 30/33, "Standalone
  and Consolidated un-audited Financial Results", Limited Review Report. → CLASS: results

## Company memory / Notion
- No companies/SPAPPAREL.md (or SPAL) file exists — new/uncovered name.
- GitHub/Notion MCP disconnected this session; no live Notion thesis fetch possible.
- Thesis context passed to A3/A4 = NONE AVAILABLE (uncovered name; no Decision Status,
  no entry zone, no tripwires, no monitoring checklist). Flagged, not halted.

## Board Outcome items noted at detection (to be enumerated fully by A2/A3)
1. Standalone + Consolidated unaudited results Q1 FY27
2. Final dividend Rs.3.00/sh (30%) for FY ended 31.03.2026; record date 04.09.2026
3. Sub-division/split 1 share (FV Rs.10) → 5 shares (FV Rs.2); AGM approval pending
4. Alteration of SPAL ESOP 2024 Scheme A & B due to split
