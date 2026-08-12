# Run Log — KRN Q1 FY27 Quarterly Review

- Ticker: KRN (KRN Heat Exchanger and Refrigeration Limited, NSE: KRN, BSE: 544263, ISIN INE0Q3J01015)
- Quarter: Q1 FY27 (quarter ended 30 June 2026)
- Invoked: /run-quarterly KRN --docs <results.pdf>
- Run date: 2026-08-12

## Documents supplied
- Three PDFs uploaded; all byte-identical (md5 8f9fef7aa7211cdecb512dc7d03468ea), 13 pages each.
- De-duplicated to ONE unique document.
- No concall transcript supplied. No investor presentation supplied.

## Document-class detection
- results_krn_q1fy27.pdf -> class = RESULTS
  Markers: "Unaudited Financial Results for the quarter ended on 30th June, 2026",
  Reg 30/33 SEBI LODR Board Meeting Outcome, Limited Review Reports.

## Prechecks
- Protocol files: all present (Results v1.2, Concall v1.1, Master v3.3).
- Toolchain: pdftotext, pdfinfo, pdftoppm, tesseract all OK (poppler-utils + tesseract-ocr installed this session).
- Company memory companies/KRN.md: ABSENT (new company, no prior coverage).

## Notes
- Single results document -> A1/A2/A3 run once (no parallel chains).
- No concall -> Role 5 not applicable this run; A4 runs Role 4 only.
