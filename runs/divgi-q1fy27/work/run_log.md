# RUN LOG — DIVGI q1fy27 quarterly review

Orchestrator: /run-quarterly DIVGI
Run date: 2026-08-11
Ticker: divgi (DIVGIITTS / BSE 543812)
Company: Divgi TorqTransfer Systems Limited

## Documents (class detected from content, not filename)
- DOC1 -> results  : 6 pages. Reg 30+33 Board Outcome + Unaudited Financial Results (standalone) + Auditor Limited Review Report. Q1 FY27 (quarter ended 30 Jun 2026). Ref DTTS/Sec/26-27/29.
- DOC2 -> presentation : 41 pages. Reg 30 Investor Presentation "performance for quarter ended June 30, 2026". Ref DTTS/Sec/26-27/33.
- No concall transcript supplied this run.

## Toolchain
- pdftotext/pdfinfo/pdftoppm/tesseract: installed this session via apt-get (poppler-utils, tesseract-ocr). apt index refresh required first (stale 404).

## Company memory / Notion (fetched live at Step 0F)
- companies/DIVGI.md: DOES NOT EXIST.
- Notion workspace search for Divgi TorqTransfer company/monitoring page: NO PAGE FOUND.
- Conclusion: DIVGI is a FRESH company to the pipeline. No prior Decision Status, entry zone, active tripwires, or monitoring checklist to pass to A3/A4. Recorded as run-log fact; not a halt condition.

## Gates
- GATE A1 results: PASS (6/6 pages, units Millions x0.1, no OCR).
- GATE A1 presentation: PASS (41/41 pages, units Crores x1, OCR on divider slides 15/22/32 confirmed no missed text).
- GATE A2 results: pending
- GATE A2 presentation: pending

## Gate updates (post A2/A3)
- GATE A2 results: PASS (8/8 count categories reconcile).
- GATE A2 presentation: PASS (41/41 slides reconcile; grep==manual==pdfinfo).
- GATE A3 results: PASS (17/17 checks statused; 8 PASS / 4 FINDING / 5 N.A.).
  - LEDGER CORRECTION by A3: FY26 "changes in inventories" confirmed (80.76), not A2's (807.60). Footing to total expenses 3,124.22 proves it. Affects FY26 comparative only, not any Q1 FY27 figure. A4 must use corrected value.
  - Findings feeding mandatory A4 mgmt questions: FORWARD-SIGNAL {A3-F2 new foreign entity, A3-F6a, A3-F13b AGM/AR incoming, A3-F15}; AMBIGUOUS {A3-F6b IPO capex 60.7% deployed, A3-F13a statutory auditor change independence}.
- GATE A3 presentation: pending.
