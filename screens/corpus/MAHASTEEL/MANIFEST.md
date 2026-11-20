# MAHASTEEL corpus manifest

Company: Mahamaya Steel Industries Ltd
NSE: MAHASTEEL | BSE: 513554 | ISIN: INE451L01014
Screened: 2026-10-18. Card: `screens/cards/MAHASTEEL.md`.
Page counts from pdfinfo. "Read" means read in full; "skimmed" means navigated by grep and the relevant pages read.

## Documents held

| Path | Type | Period / date | Pages | Use |
|---|---|---|---|---|
| screener/Annual_Report_2026.pdf | Annual report | FY26, notice dated 31-Aug-2026 | 144 | Read: MD speech p.6-7, notice and explanatory statement p.8-26, Directors' Report p.28-36, AOC-1/AOC-2 p.39-40, remuneration p.41-43, energy p.50, MD&A p.51-54, shareholding p.71-73, auditor report, KAM, CARO, IFC p.79-89, notes p.90-110. Consolidated statements skimmed. |
| screener/Annual_Report_2025.pdf | Annual report | FY25 | 156 | Skimmed: MD letter p.6-7, MD&A p.51-53, KAM p.79 and p.120, ratings p.74, penalties p.36 and p.47 |
| screener/Investor_Presentation_1.pdf | Investor deck | September 2016 (cover letter 03-Oct-2016) | 35 | Read. Pages 1, 2, 29, 31, 33, 35 are [OCR] cover and image pages; no numbers taken from them |
| screener/Financials.xlsx and .txt | screener.in export | FY17 to FY26, quarters to Jun-2026 | n/a | Data Sheet used for price history and cross-check only. Service record, not a filed document. Formula sheets are empty shells |
| market-data-2026-10-18.md | screener.in page | 18-Oct-2026 | n/a | Market cap, price, PE, book. Service record |
| results/q-2026-09.pdf | MISLABELLED: Reg 74(5) depository certificate | Quarter to 30-Sep-2026, filed 10-Oct-2026 | 2 | Read. Holds no results |
| filings/..._13082026124818_..QUICKRESULTS30062026.pdf | Q1 FY27 results, standalone and consolidated, limited review | 13-Aug-2026 | 7 | Read. Tables on p.4 and p.7 read visually (OCR garbled digits) |
| filings/..._26052026143335_..OBM_26052026.pdf | FY26 audited results, BS, cash flow, audit reports, Reg 33(3)(d) declaration, qualified borrowings | 26-May-2026 | 17 | Read. p.3 read visually |
| filings/..._13022026151110_..OBM130202026.pdf | Q3 FY26 results (Dec-2025 quarter) | 13-Feb-2026 | unreadable | DEFECT: truncated download (18.1 MB held, 29.3 MB declared in the linearisation header); pdfinfo fails; .txt empty. Q3 numbers taken from FY26 results p.3 comparatives |
| filings/..._12122025170905_..OBM12112025.pdf | Q2 FY26 results re-submission (original 13-Nov-2025) | Filed 12-Dec-2025 | 10 | Read. p.1 and p.8 read visually. No NSE query or reply letter inside |
| filings/..._13112025172125_..NOBM07112025.pdf | Board meeting intimation | 07-Nov-2025 | 1 | Skimmed |
| filings/..._13082026125521_..DISC30SOLAR13082026.pdf | Reg 30: 350 acres for solar, Rs 70 crore | 13-Aug-2026 | 2 | Read |
| filings/..._22082026114023_..OBM22082026.pdf | Board outcome: AGM date, scrutiniser | 22-Aug-2026 | 1 | Read. No capex, fundraise or preferential issue |
| filings/..._31082026115819_..OBM310826.pdf | Board outcome: auditor change, borrowing Rs 900 crore, s.186 Rs 900 crore, s.185 Rs 300 crore, material RPTs, promoter loans | 31-Aug-2026 | 3 | Read |
| filings/..._31082026115949_..OBM310826.pdf | Duplicate of above | 31-Aug-2026 | 3 | DEFECT: byte-identical (md5 3d52869b...) |
| filings/..._31082026120101_..OBM310826.pdf | Duplicate of above | 31-Aug-2026 | 3 | DEFECT: byte-identical |
| filings/..._26062026141154_..OBM_26062026.pdf | Board outcome: independent director re-appointment | 26-Jun-2026 | 2 | Read |
| filings/..._26092026142441_..VOTRESSCRREP25092026.pdf | AGM voting results and scrutiniser report | 25-Sep-2026 | 15 | Skimmed: all 12 resolutions passed; RPT resolutions 11 and 12 carried by 2,51,508 public votes (1.53% of shares) |
| filings/..._07022026144656_..INTOFCREDITRATING07022026.pdf | Infomerics IVR BBB Stable reaffirmed | 07-Feb-2026 | 1 | Read |
| filings/..._23062026112502_..CREDT_RATING_INT_23062026.pdf | Brickwork BBB+/A2 assigned, Rs 51.47 crore | 22-Jun-2026 | 5 | Read |
| filings/team_bbodade_15042026180537_MAHASTEEL1.pdf | Reg 31(4) encumbrance disclosure, promoter list | 02/03-Apr-2026 | 3 | Read visually (image pages, .txt holds only signature blocks) |
| filings/team_sandeshc_13042026115814_MAHASTEEL.pdf | Reg 31(4) encumbrance disclosure | 02-Apr-2026 | 2 | Read visually; same content as above |
| filings/team_sandeshc_13042026115624_Annual12.pdf | Reg 31(4) promoter declaration | 02-Apr-2026 | 1 | Read visually; duplicate of p.3 above. .txt empty |
| credit-ratings/01-ICRA.pdf (.txt) | ICRA rationale, Issuer Not Cooperating | 27-Aug-2026 | 6 | Read |
| credit-ratings/manifest.json | Collector log | n/a | n/a | Records a failed Brickwork rationale fetch (6-Aug update, connection reset) |

## OCR notes

- Only Investor_Presentation_1.txt carries [OCR] page markers (6 pages, all cover or image slides).
- The results filings are scanned PDFs with a text layer that garbles table digits. Every results number in the card was read from the page image: Q1 FY27 p.4 and p.7; FY26 p.3; Q2 FY26 p.8. Example of the garble: OCR read consolidated Q2 FY26 diluted EPS as 1.35; the page shows 1.15.

## Documents that exist but are not held

- Results for the Sep-2026 quarter: not yet due. The company calendar sets 14-Nov-2026 (Annual_Report_2026, p.71).
- A readable Q3 FY26 (Dec-2025) results filing.
- The Brickwork rating rationale of 22-Jun-2026 and the Brickwork update of 6-Aug-2026 (fetch failed).
- CARE rationale of 27-Nov-2025 (Issuer Not Cooperating), and the ICRA rationale before non-cooperation.
- Any earnings call transcript. None appears to exist.
- Any investor presentation after September 2016.
- The NSE notice behind the 12-Dec-2025 re-filing. The FY26 annual report records a Rs 1,30,000 plus GST NSE fine for late filing of the H1 FY26 results PDF (p.36, p.47), which fits a re-submission.
- Financial statements of Devi Iron & Power and Abhishek Steel Industries.

## Defects found

1. `results/q-2026-09.pdf` is mislabelled. It is a Regulation 74(5) certificate, not quarterly results.
2. `filings/..._13022026151110_..OBM130202026.pdf` is truncated and cannot be opened.
3. Three byte-identical copies of the 31-Aug-2026 board outcome.
4. `screener/Investor_Presentation_1.pdf` is a 2016 deck. Treat it as history, not as the current presentation.
5. `screener/Financials.xlsx` formula sheets are empty; only the Data Sheet carries numbers.
6. Three Reg 31(4) filings are image-only; their .txt files hold signature metadata only.
