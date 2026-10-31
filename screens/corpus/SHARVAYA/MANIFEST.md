# SHARVAYA corpus manifest

Sharvaya Metals Ltd, BSE SME 544506. Ledger written 2026-10-18 for the shallow card
`screens/cards/SHARVAYA.md`. Page numbers are PDF pages.

## Documents held

| Path | Type | Period | Pages | Use |
|---|---|---|---|---|
| filings/2026-09-02_annual-report-FY26.pdf | Annual report with AGM notice | FY26 | 54 (two printed pages per PDF page) | Read in full: MD letter, highlights, directors' report, secretarial audit, MD&A, auditor's report and CARO, statements, all notes. AGM notice and e-voting pages skimmed |
| screener/Annual_Report_2026.pdf | Annual report | FY26 | 54 | Not used: byte identical to the filings copy (same MD5) |
| screener/Financials.xlsx (+ .txt) | screener.in export | FY22 to FY26 | 6 sheets | Cross-check only. Data Sheet is populated; the formatted sheets are empty in the .txt |
| filings/2025-11-14_results-H1FY26.pdf | Half year results, limited review | H1 FY26 | 5 | Read in full. Pages 2 to 4 read visually |
| filings/2026-05-30_results-FY26.pdf | Audited results with H2 column | FY26, H2 FY26 | 10 | Read in full. Pages 8 to 10 read visually |
| filings/2026-02-24_monitoring-agency-Feb26-b.pdf | Monitoring agency report (Infomerics) | Quarter to 30-Sep-2025 | 15 | Skimmed: no deviation, tax auditor certificate |
| filings/2026-02-24_monitoring-agency-Feb26-a.pdf | Monitoring agency report | Quarter to 31-Dec-2025 | 18 | Read utilisation table; pages 11 to 12 read visually |
| filings/2026-05-19_monitoring-agency-May26.pdf | Monitoring agency report | Quarter to 31-Mar-2026 | 18 | Read utilisation table; pages 12 to 13 read visually |
| filings/2026-08-21_monitoring-agency-Aug26.pdf | Monitoring agency report | Quarter to 30-Jun-2026 | 17 | Read in full; pages 11 to 12 read visually |
| filings/2026-05-30_deviation-statement.pdf | Reg 32 deviation statement | H2 FY26 | 3 | Read in full |
| filings/2026-04-28_reg30-announcement.pdf | Reply to BSE price movement query of 23-Apr-2026 | Apr-2026 | 1 | Read in full |
| filings/2026-06-24_price-movement-clarification.pdf | Reply to BSE price movement query of 22-Jun-2026 | Jun-2026 | 1 | Read in full |
| filings/2026-09-02_meeting-updates.pdf | AGM dispatch letter (AGM 24-Sep-2026) | Sep-2026 | 2 | Skimmed, housekeeping |
| filings/2026-10-06_press-release-revised.pdf | Press release: 10 inch extrusion press commissioned 5-Oct-2026 | Oct-2026 | 3 | Read in full |
| filings/2026-10-14_board-outcome.pdf | Board outcome: warrants, share swap, Success Electronics acquisition, Annexures A, B, B1i, B1ii | 14-Oct-2026 | 14 | Read in full |
| filings/2026-10-14_issue-of-securities.pdf | Same document as board outcome | 14-Oct-2026 | 14 | Not used: byte identical |
| filings/2026-10-14_preferential-issue.pdf | Same document as board outcome | 14-Oct-2026 | 14 | Not used: byte identical |
| filings/2026-10-14_raising-funds.pdf | Same document as board outcome | 14-Oct-2026 | 14 | Not used: byte identical |
| filings/2026-10-14_acquisition.pdf | Scanned copy of the board outcome | 14-Oct-2026 | 14 page images, file damaged | Page 1 image extracted and read; content matches the board outcome |
| filings/2026-10-15_EGM-notice.pdf | EGM notice, 6-Nov-2026, with explanatory statement | Oct-2026 | 58 | Read: resolutions, acquisition rationale, pricing, objects, pre and post shareholding, allottee tables. Voting instructions skimmed |
| credit-ratings/01-CARE.pdf | CARE rationale, reaffirmed B minus INC and withdrawn | 25-Oct-2024 | 5 | Read in full |
| market-data-2026-10-18.md | screener.in service record, not a filed document | 18-Oct-2026 | 1 | Used for market cap, price, range, shareholding trend |

## OCR notes

- results-H1FY26 pages 2 to 4 are [OCR]. Table digits are garbled in the .txt. Every
  number used was read from the PDF image.
- Annual report pages 3, 44 and 45 are [OCR]: cover, design credit and back cover. No
  numbers used.
- Monitoring agency Feb26-a and Feb26-b each carry one [OCR] page. Tables used were read
  visually.
- Monitoring agency Aug26 .txt is not marked OCR but its tables extract out of order.
  Pages 11 to 12 were read visually.

## Documents that exist but are not held

- IPO RHP dated 26-Aug-2025 and the final prospectus. Bull AI indexes the RHP; no file
  was fetched. Needed for customer concentration, utilisation history, promoter group,
  and the FY24 restatement.
- FY25 and earlier annual reports.
- Shareholding pattern filings (pledge is NOT FOUND without them).
- Registered valuer reports for the swap: CA Shwet Bhanushali (Sharvaya) and RV Bhavin R.
  Patel (Success), both dated 14-Oct-2026, on the company website per EGM p.23.
- Success Electronics financial statements.
- Any concall transcript or investor presentation. None appears in the filings list held;
  whether any exists is NOT FOUND.
- H1 FY27 results (half to 30-Sep-2026), not yet due at the screen date.

## Defects found

1. `filings/2026-10-14_acquisition.pdf` is truncated: no xref or trailer, poppler cannot
   open it, and the `.txt` is empty (0 pages). Its 14 page images were extracted raw; the
   last image is cut at 1,509 of 1,650 rows. Content duplicates the board outcome.
2. Three 14-Oct files (issue-of-securities, preferential-issue, raising-funds) are byte
   copies of `2026-10-14_board-outcome.pdf`. The collector saved one BSE attachment under
   four subjects.
3. `screener/Annual_Report_2026.pdf` duplicates `filings/2026-09-02_annual-report-FY26.pdf`.
4. Filing errors inside the documents, not collector errors:
   - MA Dec-2025 report (p.11 to p.12) shows only in-quarter spend in the "at the end"
     column, not the cumulative figure.
   - MA Mar-2026 report (p.13) prints a total of 28.89 for 25.30 plus 3.23. The
     deviation statement (p.2) gives 28.53. MA Jun-2026 (p.12) opens at 27.33.
   - EGM notice p.47 misstates the pre issue holdings of three promoter group warrant
     allottees against board outcome p.14.
   - FY25 PAT differs between AR p.31 (Rs 1,222.98 lakh) and FY26 results p.8 (Rs
     1,250.93 lakh). FY24 PAT differs between AR p.8 (Rs 153.57 lakh) and H1 FY26
     results p.3 (Rs 99.71 lakh).
