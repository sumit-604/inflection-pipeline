# RUN LOG — UNIABEX Q1 FY27

## Setup (orchestrator)
- Invoked as: /run-quarterly UNIPART --docs .../7c075ba1-Concall_Intelligence_20260624_evening.pdf
- IDENTITY DISCREPANCY: user said "UNIPART"; the document is **Uni Abex Alloy Products Limited**
  (uniabex.com, CIN L27100MH1972PLC015950, Neterwala Group). Ticker set to UNIABEX. Flagged to user.
- Protocol files: all present (Results v1.2, Concall v1.1, Master v3.3).
- Toolchain: pdftotext/pdfinfo/pdftoppm/tesseract installed (were missing; apt-get poppler-utils + tesseract-ocr).
- Company memory: none (companies/UNIABEX.md absent) — new coverage.

## Document classification
- File: uniabex_q1fy27_results.pdf (7 pages)
  - CLASS: results. Reg 33 markers, "Unaudited Financial Results", Limited Review Report, Board Outcome.
  - Filename ("Concall_Intelligence") is misleading; content is a results filing. No concall/presentation supplied.
  - Text layer is OCR-derived (iLovePDF) with corruption on numeric tables -> OCR fallback expected at A1.
- Quarter detected: Q1 FY2026-27 (quarter ended 30 June 2026) -> q1fy27.

## Operator ruling (2026-08-06)
- User confirmed: ANALYZE UNI ABEX (the uploaded PDF). Treat as NEW coverage.
  Do NOT touch the Uniparts India Ltd Notion page. No prior thesis to seed A4.
- Notion save: no existing UNIABEX page; user did not opt to create one -> hold Notion save, present in chat.
