# SAMPARK corpus manifest

Sampark India Logistics Ltd (formerly Sampark India Logistics Private Limited, converted 02-Sep-2024).
BSE SME 544810, scrip ID SILL, no NSE listing, ISIN INE147701010, CIN L63090DL2012PLC245542 (AR26 p.22).
Listed 07-Jul-2026; IPO of 32,40,000 fresh shares at Rs 84 (AR26 pp.4, 23). Half-yearly reporter.
Promoters: Sanjay Kumar Rathi and Renu Rathi, 97.77% pre-issue (RHP p.22), 71.94% at Sep-2026 (market data).
Ledger written 2026-10-30. Card: `screens/cards/SAMPARK.md`.

Status key: FULL = read in full; PART = key sections read, rest navigated by keyword; SKIM =
housekeeping, checked for substance; DUP = byte-identical to another held file (md5 checked).
Page numbers are PDF page numbers. In the RHP the printed page number is the PDF page minus 2
(PDF p.27 = printed p.25).

## How it was built

- screener/: two files linked from the public screener.in page for SAMPARK, both served from BSE.
  `Annual_Report_2026.pdf` from `https://www.bseindia.com/xml-data/corpfiling/AttachHis/86a01fad-5115-43e9-b63b-b1f052b93693.pdf`
  (the Reg 34(1) FY26 annual report filing); `Investor_Presentation_Jul_2026.pdf` from
  `https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname=f6284bd4-78d0-491a-a044-bfce58dfc762.pdf`,
  final URL `AttachHis/f6284bd4-...`. Fetched 2026-10-30 09:37. No transcripts or other decks exist.
  Financials.xlsx is absent this run (the screener collector's browser could not start); the
  financial trajectory was built from the filed results, the annual report and the RHP.
- filings/: BSE announcements listed through the bseindia.com corporate-announcements form in the
  in-app browser, window 01-Jun-2026 to 30-Oct-2026, 20 announcements, housekeeping dropped, 11 rows
  kept (`work/bse/SAMPARK.txt`). Attachments downloaded from `xml-data/corpfiling/AttachHis/`
  on 2026-10-30 10:01. File name = filing date + first 8 characters of the BSE attachment name.
  Two rows of the kept list are held under screener/ instead (86a01fad annual report; f6284bd4 deck).
- credit-ratings/: none. No rating link on the screener.in page, and the company states it has no
  rating (AR26 p.24). `tools/collector/fetch_ratings.py` had nothing to fetch.
- prospectus/: red herring prospectus of 22-Jun-2026 from the issuer's site,
  `https://silpl.rathigroup.info/assets/images/ipo/rhp_sampark_bse_22062026_final.pdf`, fetched
  2026-10-30 10:06.
- market-data-2026-10-30.md: screener.in company page, a service record (price, market cap,
  shareholding at Sep-2026).
- Text: PyMuPDF; Tesseract OCR on pages with under 40 characters of native text, tagged `[OCR]`.

## Integrity check (2026-10-30, from `fetch-ledger-2026-10-30.jsonl`)

All 12 ledger rows status OK; every file's byte size equals the declared size. Page counts: AR26 92
(1 OCR), Deck 17 (0), RHP 378 (0), FY26 res 10 (1 OCR) twice, CFO 3 (1 OCR), Sep-B 11, AGM 4,
AGM-Q 3, Price-Q 1, KMP 2, filings copy of AR26 92 (1 OCR). 14 PDFs on disk counting the duplicates.
Two md5 duplicate sets: (1) `filings/20260716_1d96187d` = `filings/20260716_920e99f4`
(md5 6e7951d6..., BSE filed the results PDF under two categories); (2) `screener/Annual_Report_2026`
= `filings/20260907_6c122cae` (md5 404ef5b9..., Reg 34 copy and AGM-notice copy).

Defects found by the analyst:
- AR26 p.91 is tagged `[OCR]` with empty text. The page image is blank. Nothing lost.
- `filings/20260716_56c3003b` (KMP contacts) has a garbled native text layer with no `[OCR]` tag
  ("Ritik~ Bachhawat", "Phiroze Jeeje~bhoy"). Its p.2 also carries a stray "Enclosed: Auditor's
  report, Balance Sheet, Profit & loss" line with no such enclosure. Nothing in the card depends on it.
- FY26 res p.8 (cash flow) native text scrambles the column order. Operating cash flow Rs 181.29 lakh
  and receivables change Rs (1,717.25) lakh were read from the page image. FY26 res p.6 was also
  checked against the image; it matches the text layer.
- AR26 p.90 dates a 2024 shareholder approval "18th May 2026". A source error, not a corpus defect.

## Substantive files, read

| Short name | Path | Period / date | Pages | Status | Pages read |
|---|---|---|---|---|---|
| RHP | prospectus/PROSPECTUS_SAMPARK_RHP_20260622.pdf | Red herring prospectus, 22-Jun-2026; restated FY23, FY24, FY25, 9M FY26 | 378 | PART | 3-4 (contents), 21-26 (summary, restated summary, litigation and RPT summaries, promoter cost), 27-44 (risk factors 1-43 in full: cash flow, concentration, unsecured loans, untraceable KMP certificates, conflicts, ROC and statutory delays), 58-64 (risk factor headings 44-69), 84-92 (capital history, 2024 sale to Kamlesh Poddar HUF at Rs 72, lock-in), 96-99 (objects, working-capital table and holding days), 141-152 (business, financial highlights, branches, fleet, unbilled freight, customer and supplier concentration, competition, employees), 176-193 (history, management, IDDB validity), 194-202 (promoters, promoter group, disassociations, group companies), 206-207 and 230 (auditor's restatement report, fixed assets, OSPT note), 244-245 (related-party annexure, Fretex and OSPT sale), 261-269 (MD&A, air mix, "not seasonal"), 270-288 (litigation, MD tax demand, creditors). Not read: industry overview 115-140, regulations 163-175, restated notes 208-243 beyond those named, indebtedness 250-256, approvals and issue procedure 288-378 |
| AR26 | screener/Annual_Report_2026.pdf | FY26, AGM 29-Sep-2026, filed 07-Sep-2026 | 92 [1 OCR] | PART | 1-2 (cover letter), 4-22 (overview, mix, umbrella, MD letter, management, board), 23-34 (directors' report: IPO, capital, rating, board, CFO change, RPT policy, internal auditor, CSR), 35-41 (MD&A, ratios, risks, pay), 42-49 (auditor, KAM, CARO, IFC), 50-52 (statements), 59-77 (notes 3-53: shares, borrowings, payables, fixed assets, receivables, revenue, other income, opex, other expenses, tax, contingent, drawing power, FX, RPT, ratios), 79 (subsequent events), 80-92 (AGM notice, MD and Renu Rathi annexures). DUP = filings/20260907_6c122cae |
| FY26 res | filings/20260716_1d96187d | H2 FY26 and FY26 audited, filed 16-Jul-2026, Rs lakh | 10 [1 OCR] | FULL | 1-10 (outcome, Reg 33 audit report incl. "other matters" on H1 FY26, P&L with H2 FY26, H1 FY26, H2 FY25 columns, balance sheet, cash flow, notes). P.6 and p.8 read from the page image. Period on p.1 and p.6 confirmed. DUP = filings/20260716_920e99f4 |
| Deck | screener/Investor_Presentation_Jul_2026.pdf | FY26 investor presentation, filed 16-Jul-2026 | 17 | FULL | 1-17 (highlights and seasonality claim p.6, mix p.7, history p.8, levers p.9, umbrella and US client p.11, management p.15) |
| CFO | filings/20260803_2ce7fb2a | CFO Sudarshan Jain resignation, effective 03-Aug-2026 | 3 [1 OCR] | FULL | 1-3 (company letter "personal reasons", annexure, his letter "other commitments") |
| Sep-B | filings/20260905_5029fb2e | Board outcome 05-Sep-2026 | 11 | FULL | 1-11 (Renu Rathi to non-executive, secretarial auditor, MD re-appointment, Periwal CFO, CS change, internal auditor A O Mittal) |
| AGM | filings/20261001_fd805629 | 14th AGM outcome, 29-Sep-2026 | 4 | FULL | 1-4 (three resolutions) |
| AGM-Q | filings/20261008_1ebedfe1 | Reply to BSE query on late AGM proceedings | 3 | FULL | 1-3 |
| Price-Q | filings/20261009_6e7a375f | Reply to BSE price-movement query | 1 | FULL | 1 |
| MD | market-data-2026-10-30.md | screener.in, 30-Oct-2026 | - | FULL | Market cap Rs 161 crore, price Rs 132, range Rs 153 / 74, PE 15.3, Sep-2026 shareholding |

Housekeeping, one line: `filings/20260716_56c3003b` (Reg 30(5) KMP contact details, 2 pages, SKIM;
text layer garbled), `filings/20260716_920e99f4` (DUP of FY26 res), `filings/20260907_6c122cae`
(DUP of AR26), `fetch-ledger-2026-10-30.jsonl`.

## Gaps (NOT FOUND, with where it was looked for)

- **H1 FY27 results** (half year to 30-Sep-2026). Not yet filed; due by 14-Nov-2026 on BSE.
- **H1 FY26 limited-review results.** Cited by the auditor (FY26 res p.5); outside the BSE window
  and pre-listing. H1 FY26 taken from the FY26 res comparative column.
- **Credit rating.** None exists (AR26 p.24); no link on screener.in.
- **Concall transcripts.** None on screener.in or in the BSE list.
- **Final prospectus, basis of allotment, listing notice, subscription data.** Not held; would come
  from the BSE IPO pages or the lead manager. Issue price and size taken from AR26.
- **Reg 32 statement of deviation / IPO fund utilisation.** Not in the BSE list; due with H1 FY27.
- **Reg 23(9) related-party disclosure.** Not in the BSE list.
- **Reg 44 AGM voting results.** The AGM outcome says they were filed separately (AGM p.1); not in
  the kept list (possibly dropped as housekeeping).
- **Shareholding-pattern filings.** Dropped as housekeeping; the screener.in record is used.
- **Mode-wise revenue in rupees and margin by mode.** Only percentages (Deck p.7, AR26 p.10).
- **Customer names, including the US umbrella client.** Not in the RHP (pp.148-150), AR26 or Deck.
- **Buyers of the Fretex and OSPT shares (March 2024), repayment of the Rs 6.43 crore OSPT advance,
  and any trade since FY25 with Fretex, OSPT, First Flight Air Freight or Sampark Couriers.** RHP
  pp.25, 197, 244 and AR26 pp.75-76 are silent.
- **Renewal of both independent directors' IICA databank registrations** (valid to 21 and
  22-Oct-2026, RHP p.182). No filing held.
- **Promoter pledge after listing.** No Reg 31 filing held; RHP pp.89-90 show none pre-issue.
