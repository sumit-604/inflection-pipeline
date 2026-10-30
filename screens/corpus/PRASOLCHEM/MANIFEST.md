# PRASOLCHEM corpus manifest

Prasol Chemicals Ltd (formerly Prachi Poly Products Ltd, renamed 2007; Prosp p.3).
NSE PRASOLCHEM, BSE 544912, CIN L99999MH1992PLC065026 (filings/20261005_0690f0a6 p.2). ISIN NOT FOUND
in the corpus. Listed 16-Sep-2026 after a Rs 500 crore book-built IPO at Rs 676 (Rs 80 crore fresh,
Rs 420 crore offer for sale; Prosp p.3). Promoters: ten individuals of the Shah, Parikh, Dharia and Gupta
families, 33.84% as first holders post-offer (Prosp p.182); promoter and group 75.25% at Sep-2026
(market-data-2026-10-30.md).
Ledger written 2026-10-30. Card: `screens/cards/PRASOLCHEM.md`.

Status key: FULL = read in full; PART = key sections read, rest navigated by keyword; SKIM =
housekeeping, checked for substance; DUP = byte-identical to another held file (md5 checked).
Page numbers are PDF page numbers. In the prospectus the printed page is the PDF page minus 5
(printed p.22 = PDF p.27).

## How it was built

- screener/: the screener.in public page (https://www.screener.in/company/PRASOLCHEM/) links its
  concall transcript and deck to BSE. Both were downloaded from `bseindia.com/xml-data/corpfiling/AttachHis/`
  on 2026-10-30 09:43: the Q1 FY27 transcript (attachment 6da52da3, 23 pages) and the Q1 FY27 investor
  presentation (attachment bd23db2f, 31 pages). No annual report exists on screener.in for a company listed
  in September 2026.
- results/: the one screener quarter link (`/company/source/quarter/1286151/6/2025/`, labelled Jun-2025)
  redirected to the BSE announcements HTML page and returned no PDF (ledger: `FAIL NOT-PDF`, 16,901 bytes).
  The folder is empty. Q1 FY26 figures are taken from the Q1 FY27 result's comparative column.
- filings/: BSE announcements for scrip 544912, listed through the bseindia.com corporate-announcements
  form in the in-app browser on 2026-10-30, window 01-Aug-2026 to 30-Oct-2026: 20 announcements, housekeeping
  dropped, 9 rows kept in `work/bse/PRASOLCHEM.txt`. Eight attachments downloaded from `AttachHis/`; the
  ninth row (Earnings Call Transcript, 05-Oct-2026) is the screener/ transcript. The 28-Sep-2026 deck
  attachment (bd23db2f) is not among the 9 kept rows but was fetched through the screener link.
  File name = filing date + first 8 characters of the BSE attachment name.
- credit-ratings/: `tools/collector/fetch_ratings.py` over the one rating link on the screener.in page,
  CRISIL, 10-Jun-2015 (HTML plus extracted text). No ICRA file exists, so the ICRA
  `ShowRationalReportFilePdfViewer` path was not used.
- prospectus/: https://www.prasolchem.com/wp-content/uploads/2026/09/Prasol-Chemicals-Limited-Prospectus.pdf,
  fetched 2026-10-30 10:06 (Prospectus dated 10-Sep-2026, 590 pages).
- market-data-2026-10-30.md: https://www.screener.in/company/PRASOLCHEM/consolidated/, fetched 2026-10-30
  about 09:00 IST, a service record. Its P/E of 110 and ROE of 12.6% match FY25, not FY26, figures
  (market cap Rs 4,806 crore over FY25 PAT Rs 43.57 crore = 110.3x), so its ratios are a year stale.
- Financials.xlsx: absent (the screener collector's browser could not start in this environment).
- Text: PyMuPDF; Tesseract OCR on pages with under 40 characters of native text, tagged `[OCR]`.

## Integrity check (fetch-ledger-2026-10-30.jsonl)

11 ledger rows: 10 OK, 1 FAIL (the screener quarter link above). Every OK file's byte size equals the
declared size. Page counts: prospectus 590 (1 OCR page, p.362, an organisation chart), transcript 23
(0 OCR), deck 31 (3 OCR, all section-title slides: pp.4, 11, 24), filings 1, 1, 1, 2, 3, 8, 8, 2
(OCR: 1 page in each of the two 8-page result copies, p.8; 1 page in 20261005_0690f0a6, p.2). Prospectus
`.txt` carries 590 page markers.

Defects found:
- **Garbled native text, not OCR-tagged:** `filings/20260928_70fa067f` p.6, the Q1 FY27 results table.
  The text layer reads "Siles 432090" and "Toulincome". Every number the card uses from that page was read
  from the page image (rendered at 220 dpi), and the company's own deck (p.10) agrees with each total.
- **Duplicate:** `filings/20260928_84df9793` is byte-identical to `20260928_70fa067f` (md5 6f9b1f2e...),
  filed under two BSE titles (results; board outcome).

## Substantive files, read

| Short name | Path | Period / date | Pages | Status | Pages read |
|---|---|---|---|---|---|
| Prosp | prospectus/PROSPECTUS_PRASOLCHEM_Prospectus_202609.pdf | Prospectus, 10-Sep-2026 | 590 [1 OCR] | PART | 2-5 (cover, offer, selling shareholders), 17-26 (definitions, KPI definitions, forward-looking summary), 27-90 (risk factors: 27-44, 49-50, 53-58, 62-63, 69-77 read; others by heading), 140, 181-183 (pledge, WACA, pre/post shareholding), 192-195 (objects of the offer, loans to repay), 208 (KPIs), 302-304 (business overview, product and geography split), 366-378 (promoters, promoter group, dividend), 384 (restated P&L), 437-439 (note 45-46, lapsed 2022 IPO, related parties, director pay), 448-449 (financial indebtedness at 15-Jul-2026), 467 (no seasonality), 471-479 (outstanding litigation), 485-487 (group companies, selling shareholders). Not read: industry overview 223-301, regulations, restated notes other than 45-46, MD&A 452-470 beyond keyword search |
| Q1 res | filings/20260928_70fa067f | Q1 FY27 results and board outcome, filed 28-Sep-2026 | 8 [1 OCR] | FULL | 1-8 (outcome, VP R&D retirement, limited review with EoM on IPO costs, P&L with Q4 FY26, Q1 FY26 and FY26 columns, notes incl. IPO and unreviewed Q4). Period on p.6 confirmed. DUP = 20260928_84df9793 |
| Call | screener/Concall_Oct_2026_Transcript.pdf | Q1 FY27 call 29-Sep-2026, filed 05-Oct-2026 | 23 | FULL | 1-23 |
| Deck | screener/Investor_Presentation_Oct_2026.pdf | Q1 FY27 deck, filed 28-Sep-2026 | 31 [3 OCR] | FULL | 1-31 (guidance p.6, Q1 bridge p.8, P&L pp.10, 26, balance sheet p.27, cash flow p.28, IPO use p.29, Phase 1 and 2 p.22) |
| PIT | filings/20260924_20fffebb | PIT code violation report, 24-Sep-2026 | 3 | FULL | 1-3 (CFO's relative bought 300 shares in the closed window, 18-Sep-2026; warning letter) |
| KMP | filings/20260916_f8150ffb | Reg 30(5) KMP list, 16-Sep-2026 | 2 | FULL | 1-2 |
| CIN | filings/20261005_0690f0a6 | CIN change to listed, 05-Oct-2026 | 2 [1 OCR] | FULL | 1-2 (MCA master data: paid-up Rs 11.84 crore, last AGM 16-Jul-2026) |
| CRISIL-15 | credit-ratings/01-CRISIL.html / .txt | Rating suspended, 10-Jun-2015 | - | FULL | Whole text: BBB-/Stable suspended for non-cooperation |
| MD | market-data-2026-10-30.md | screener.in, 30-Oct-2026 | - | FULL | Market cap, price, shareholding; stale P/E and ROE noted |

Housekeeping, checked for substance: filings/20260916_1ea98176 (Reg 6(1) compliance officer, 1 p.),
20260916_95c5c1b9 (Reg 7(1) registrar, 1 p.), 20260916_841fd8f2 (PIT Reg 8(2) fair-disclosure code cover
letter, 1 p.; the code itself is not attached).

## Gaps (NOT FOUND, with where it was looked for)

- **Listed-company annual report.** None exists yet; FY26 is held only as restated financials (Prosp
  pp.379-446). The FY26 statutory annual report (AGM 16-Jul-2026 per CIN p.2) would come from the company
  website; it is not on screener.in or in the BSE window.
- **Q2 FY27 result.** Due 2-Nov-2026 per the orchestrator brief; the board-meeting intimation was dropped as
  housekeeping and is not held.
- **Q2 and Q3 FY26 quarterly figures.** Not in Q1 res (only Q1 and Q4 FY26 columns) or Prosp. Would come
  from the RHP's interim data, if any, or not at all for a pre-listing company.
- **Current credit rationale.** Acuite A+/Stable and A1+, reaffirmed 6-Jan-2026, is cited in Prosp pp.70,
  194; the rationale is not held. Would come from acuite.in; screener.in links only the 2015 CRISIL page.
- **ISIN.** Not in Prosp (cover, definitions, p.511) or any filing.
- **CARE industry report** (28-Jul-2026), cited for market-share and largest-importer claims (Prosp p.302).
  Not held; it was on the company website until the offer closed (Prosp p.23).
- **Product volumes and per-product margins.** Prosp p.303 states the split is confidential; only
  tonnage capacity and production by plant are given (Prosp p.31).
- **Mahad EBITDA for Q1 FY27.** The chairman promised to "revert back" (Call p.17); nothing filed.
- **Phase 1 split between Khopoli and Mahad, and whether it uses MIDC plot FS 26.** Deferred by management
  to "the second half" (Call p.23); MIDC status after the 16-Apr-2026 reply NOT FOUND (Prosp p.31).
- **Financials.xlsx.** Absent this run.
