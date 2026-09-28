# HOLMARC corpus manifest

Company: Holmarc Opto-Mechatronics Ltd
NSE: HOLMARC (NSE EMERGE, SME platform) | ISIN: INE0LXA01019
CIN L33125KL1993PLC006984. BSE code: none in the Bull AI record.
Reports half-yearly. Latest financial period ends 31-Mar-2026.
Screened: 2026-09-28

## Corpus rule deviation (operator ruling 2026-09-08 applies)

No egress this session. The corpus is the Bull AI chunk reader over the same
filed PDFs. Page numbers are the source PDF's own. Nobody holds the original.

## Documents read

| Document | Bull AI doc id | Pages read | Period |
|---|---|---|---|
| Annual Report FY2024-25 (Reg. 34) | 3cac43b8-1c2d-4446-a7cb-a72e0e2e2771 | 3 to 24; 27, 46, 47, 59, 89, 97, 99, 107 as search snippets | FY2025 (Bull AI label FY2025 Q4, upload date shown as 2025-03-31, which cannot be right for a report on that year) |
| Intimation, purchase of industrial unit at Edayar, 19-Jun-2026 | bf261e20-5f52-418a-8ab7-33b7d61b2b67 | 1, 2 | FY2027 Q1 |
| Intimation, DIC sanction for land transfer, 11-Sep-2026 | d914f5c5-4337-46c8-af60-7d9db0f72d9e | 1 to 5 | FY2027 Q2 |
| Record date and board outcome, 05-Aug-2026 | 168c0d30-6d3a-455b-8341-91bcb4ae8466 | 1, 2 (search snippets) | FY2027 Q2 |
| Dividend TDS communication, FY26 final dividend | 7527b159-2283-4221-9c11-f47bf86ec506 | 1, 2 (search snippets) | FY2027 Q2 |
| Board outcome, whole-time director re-appointment | 73a4a20e-d1f2-493b-bd64-30d3023fd0b9 | 3 (search snippet) | FY2026 Q4 |
| Corporate governance non-applicability letter, 13-Jul-2026 | 75e71bdb-adbc-4781-9b53-aa2e8e7c5fba | 1 (search snippet) | FY2027 Q2 |
| Management guidance records (get_company_guidance) | n/a | returned **zero records** | all |

## Known gaps

- **FY26 financial results NOT FOUND.** The board outcome of 28-May-2026 that
  carries the FY26 results is indexed as document
  5fdf428a-f114-4d33-b265-1706bb558543 (Bull AI label FY2026 Q2, a fiscal-label
  error: an upload of 2026-05-28 is FY2026 Q4 business). The chunk reader
  returns **empty** for it.
- **FY26 annual report NOT FOUND.** Indexed as document
  15f27991-646e-4c25-96e3-f548e6c80624 (upload 2026-08-08). The chunk reader
  returns empty in both the annual_reports and pdf_content collections, and a
  filtered search returns nothing.
- The "Result" category holds only H1 FY25, FY24 and H1 FY24 filings.
- No investor presentation, no concall transcript, no guidance record exists.
- **Credit rating NOT FOUND.** No rating filing in the availability map.
- Promoter holding and pledge NOT FOUND. Searched twice.

## Reader defects found

- FY25 Directors' Report financial summary (AR page 46) is garbled: tax,
  deferred tax, profit after tax and EPS rows are shifted by one line, so
  "Deferred Tax" reads 373.51 and "Profit after Tax" reads 3.72. Figures are
  taken from the profit and loss statement (AR page 89) and MD&A (page 21).
- FY25 trade receivables ageing (AR page 107): the column headers for the two
  years are swapped against the table body. Only the totals are used.
- Two FY26 documents indexed but unreadable (above).

## Price basis

Not a corpus document. Bull AI company record, market capitalisation
Rs 123.01 crore, read 2026-09-28.

## Bull AI calls

12 billable: 1 guidance, 5 searches, 6 chunk reads (three returned empty).
Free: 2 availability maps.
