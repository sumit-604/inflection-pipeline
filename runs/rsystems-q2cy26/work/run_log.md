# Run Log — RSYSTEMS Q2 CY2026

- Ticker: RSYSTEMS (NSE: RSYSTEMS, BSE: 532735 / 977286)
- Company: R Systems International Limited
- Period: Quarter and six months ended June 30, 2026 (calendar-year reporter → Q2 CY2026)
- Invoked: /run-quarterly RSYSTEMS --docs <results> <press release>

## Setup / Prechecks
- Protocol files present: Quarterly_Results_Review_Protocol_v1_2.md, Quarterly_Concall_Analysis_Protocol_v1_1.md, Master_Project_Prompt_v3.3.md — OK
- Toolchain: pdftotext/pdfinfo/pdftoppm/tesseract initially MISSING → installed poppler-utils + tesseract-ocr via apt-get — OK
- Company memory companies/RSYSTEMS.md: ABSENT (new coverage)

## Document-class detection
- inputs/results_rsystems_q2cy26.pdf (21pp): Reg 30/33/52 Board Outcome + audited standalone & unaudited consolidated financial results → doctype = results
- inputs/presentation_rsystems_q2cy26.pdf (11pp): Earnings Press Release, management commentary + highlights + key deal wins (not Reg 33 statement, not a concall transcript) → doctype = presentation
- No concall transcript supplied this run.

## GATE A1 — PASS (both documents)
- results: 21/21 pages, formfeed 21, 1357 lines, unit=Millions (x0.1→Cr), no OCR. extract_results_rsystems_q2cy26.txt
- presentation: 11/11 pages, formfeed 11, 579 lines, unit=Millions (x0.1→Cr, parallel US$mn), no OCR. extract_presentation_rsystems_q2cy26.txt

## A2 — enumerators launched (results ledger + presentation ledger)
