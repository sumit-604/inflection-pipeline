# ZENITHHE corpus manifest

Zenith Health Care Ltd. BSE 530665, scrip ID ZENITHHE, ISIN INE812B01026. No NSE listing. Face value Re 1.
Ledger written 2026-10-29. Card: `screens/cards/ZENITHHE.md`.

Status key: FULL = read in full; PART = key sections read, rest navigated by keyword; SKIM =
housekeeping, checked for substance; DUP = byte-identical to another held file (md5 checked).
Page numbers are PDF page numbers. In AR26 the printed page number is one lower than the PDF page
(AR26 PDF p.53 = printed p.52). AR26 is a scan; every page after the cover letter is `[OCR]`, so
every figure used on the card was checked against the page image.

## How it was built

- screener/: `tools/collector/screener_collect.py https://www.screener.in/company/530665/ --output-dir
  screens/corpus/ZENITHHE/screener --no-drive` under `py -3.14`, 2026-10-29. Two annual reports
  (FY26, FY25) and Financials.xlsx. No transcripts or decks exist on screener.in.
- filings/: BSE announcements API (`AnnSubCategoryGetData/w`, strCat -1), called from a bseindia.com
  page in the in-app browser because scripted calls to NSE and BSE returned Access Denied on
  2026-10-29. Two windows of 12 months or less, covering 11-Feb-2025 to 28-Oct-2026: 42 announcements
  listed after housekeeping categories were dropped (board-meeting intimations, newspaper
  publications, trading-window closures, Reg 74(5), investor complaints, shareholding patterns,
  Reg 7(3), Reg 40, record dates, large-corporate forms, secretarial compliance). 42 attachments
  held; 13 of them are the same PDF filed twice or three times under different categories, downloaded
  once and recorded in the ledger as "same date and byte size". Attachments came from
  `xml-data/corpfiling/AttachLive/`, falling back to `AttachHis/`, with `curl -C -` and three
  retries. File name = filing date + BSE attachment name.
- credit-ratings/: none. No rating link on the screener.in page; `fetch_ratings.py` had nothing to fetch.
- market-data-2026-10-29.md: screener.in company page, a service record (28-Oct-2026 close).
- Text: PyMuPDF; Tesseract OCR on pages with under 40 characters of native text, tagged `[OCR]`.

## Integrity check (2026-10-29, run by the orchestrator)

All 44 PDFs (2 screener, 42 filings) opened with PyMuPDF. Every page's text was extracted, page
markers in each `.txt` match the PDF page count, and every file ends with `%%EOF`. 146 filing pages
and 78 screener pages carry `[OCR]`. 13 md5 duplicate sets, listed in `dup-sets-2026-10-29.json`.
**No broken file.**

## Substantive files, read

| Short name | Path | Period / date | Pages | Status | Pages read |
|---|---|---|---|---|---|
| AR26 | screener/Annual_Report_2026.pdf | FY26, AGM notice dated 04-Aug-2026 | 79 (78 OCR) | PART | 3-5 (board, notice, CMD pay, RPT resolution), 15-24 (explanatory statement, Schedule V, board's report, scheme), 29-33 (scheme annexure, post-merger holding), 36 (AOC-2), 40-41 (secretarial audit), 44 (MD&A), 46, 49 (auditor), 52-53 (BS, P&L; images), 59, 63-79 (policies, notes 5-48, ratios; images of 67, 70-72, 77, 79). DUP = filings/20260804_13891469 |
| AR25 | screener/Annual_Report_2025.pdf | FY25 | 73 | PART | 14-21 (notice, RPT item, board's report), 24, 26, 28 (pay), 37 (MD&A), 45-46 (BS, P&L), 50, 60-63, 66-67, 72-73 (notes, RPT, ratios). DUP = filings/20250902_202cd5e3 |
| Q2 res | filings/20261028_afebbb84-... | Q2 and H1 FY27, filed 28-Oct-2026 | 5 | FULL | 1-5 (P&L, BS, cash flow, review report), images of 2-4. DUP = 20261028_30a3e556 |
| Q1 res | filings/20260814_a5602f8f-... | Q1 FY27 | 3 (2 OCR) | FULL | 1-3; Q1 figures taken from Q2 res comparatives. DUP = 20260814_77fa5ba8 |
| FY26 res | filings/20260529_478d7468-... | FY26 audited, Q4 FY26, JMD appointment, half-year RPT form | 17 | FULL | 1-17; image of p.7 (results table is OCR-garbled in text). DUP = 20260529_e1849950 |
| Q3 res | filings/20260212_a124b8dc-... | Q3 and 9M FY26 | 3 | FULL | 1-3. DUP = 20260212_6fdc3563 |
| H1-26 res | filings/20251111_f504d9bf-... | Q2 and H1 FY26, with BS and cash flow | 5 | FULL | 1-5; image of p.2. DUP = 20251111_06a33ae5 |
| Scheme | filings/20260714_d9ce30bf-... | Amalgamation of Achyut into Zenith, board outcome 14-Jul-2026 | 7 | FULL | 1-7. DUPs 20260714_96fd4410, 20260714_a7bf3ba7 |
| AGM25 | filings/20250901_7c9827f8-... | 31st AGM notice, Rs 100 crore RPT with Achyut | 15 | PART | 1-3, 12-14 |
| Vote26 | filings/20260831_e199f812-... | 32nd AGM voting results and scrutiniser report | 21 (9 OCR) | PART | 1-8; image of p.7 (RPT vote) |
| MD-reapp | filings/20260804_79b316ef-...; _5a135bc8-... | CMD re-appointment, board outcome 04-Aug-2026 | 4 each | FULL | 1-4 (two near-identical filings, not md5 DUPs) |
| JMD | filings/20260529_4e84c9c5-...; 20260831_d5231a09-... | Joint MD appointment and regularisation | 3 / 2 | FULL | |
| Mgmt | filings/20260831_9fc565e7-...; 20260831_0cd8d320-... | CMD re-appointed; Neela Raycha re-appointed | 3 / 2 | FULL | |
| AGM proc | filings/20250930_152f0043-...; 20260828_9971dd7e-... | 31st and 32nd AGM proceedings | 4 each | FULL | |

Held, SKIM or not opened beyond page 1: the 32nd AGM notice as a standalone filing
(20260804_d3a37eb9, same notice as AR26 pp.4-20; and 20260804_103636c1, the notice plus board
outcome, DUP 20260804_6441da47); Q3 FY25 results and integrated filing (20250211_4baacb1a,
_16da5ea6; DUP _bf3e080e); FY25 results and board outcome (20250527_8eff22ad; DUPs _24568ef1,
_5aec8ee8); Q1 FY26 results (20250812_913bbacf; DUP _0c172c69), figures taken from H1-26 res
comparatives; board outcome and AGM notice of 01-Sep-2025 (20250901_67fe2387); 31st AGM voting
result (20251001_cee6cb11, pp.1-4 read); secretarial and internal auditor appointments
(20250528_bd1f4b00, 20251001_81d22c38, 20260529_623aaf59; DUP _6126f390).

DUP sets (md5): 13 sets, 29 files, listed in `dup-sets-2026-10-29.json`. Results and board
outcomes are routinely filed two or three times under different categories; both annual reports
are also held as Reg 34 filings. The two CMD re-appointment filings of 04-Aug-2026 differ by a
few characters (board date "04th" against "03rd" August) and are not md5 duplicates.

## Gaps (NOT FOUND, with where it was looked for)

- **Credit rating.** None exists. No borrowings (AR26 p.79); no rating link on screener.in; no
  rating filing among the 42 announcements. Step 10 is NOT FOUND.
- **Concall transcripts and investor presentations.** None on screener.in or in the BSE list.
- **Share exchange report (Den Valuation and Vanshika Vijayvargiy) and fairness opinion
  (Aftertrade Broking)**, both dated 14-Jul-2026. Named in Scheme pp.3-4; not enclosed in any
  Zenith filing. The ratio cannot be tested from this corpus.
- **Achyut Healthcare's own accounts and profit.** Only total assets, turnover and net worth at
  31-Mar-2026 are given (Scheme p.3). Achyut's PAT is not in this corpus; the ACHYUT card holds
  it as memory only.
- **Borrower of the Rs 1.63 crore "Loans to others"** (AR26 p.67). The board's report refers to
  "Note 4 and 5" for section 186 particulars; those notes do not cover loans. No name anywhere in
  AR25, AR26, the half-year RPT forms or the results.
- **Source of the Rs 2.09 crore customer advances** (Q2 res p.3; AR26 pp.71, 77). No customer
  named.
- **Promoter pledge.** No SAST filing in the window; the secretarial auditor records that the
  promoters did not file their annual SAST holding disclosure (AR26 p.41).
- **BSE observation letter, shareholder meeting and NCLT status for the scheme.** Nothing filed
  after 14-Jul-2026 beyond the note in Q2 res p.2.
- **Product, therapy, country and customer revenue split** beyond export/domestic and the one
  customer above 10% (AR26 p.77).
- **Capacity and utilisation** of the Changodar plant. Not disclosed in either annual report.
