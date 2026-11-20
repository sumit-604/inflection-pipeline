# POOJAAPREC corpus manifest

Poojaa Precision Engg. Ltd (formerly Pooja Castings Pvt. Ltd). BSE SME 544844, symbol PPEL, ISIN INE288301026.
No NSE listing. Listed on the SME Platform of BSE on 04-Aug-2026 after a Rs 159.83 crore fresh-issue IPO at
Rs 301 (BSE notice 20260803-8; AR26 p.36). Half-yearly reporter under Indian GAAP (AS 25), exempt from Ind AS
as an SME listing (H1 res p.8). The filed H1 FY27 results carry H2 FY26 and H1 FY26 as comparatives.
Ledger written 2026-10-29. Card: `screens/cards/POOJAAPREC.md`.

Status key: FULL = read in full; PART = key sections read, rest navigated by keyword; SKIM =
housekeeping, checked for substance; DUP = byte-identical to another held file (md5 checked).
Page numbers are PDF page numbers. AR26 holds two printed pages per PDF page. In the RHP the printed
page is the PDF page minus 3. In the call transcript the printed page is the PDF page minus 1.

## How it was built

- screener/: `tools/collector/screener_collect.py https://www.screener.in/company/544844/ --output-dir
  screens/corpus/POOJAAPREC/screener --no-drive` under `py -3.14`, 2026-10-29: one annual report (FY26, the
  only one that exists for a company listed in Aug-2026), one transcript (Oct-2026), the H1 FY27 deck,
  Financials.xlsx. Financials.xlsx is a service export and is never cited.
- filings/: BSE announcements API (`AnnSubCategoryGetData/w`, strCat -1), called from a bseindia.com page in
  the in-app browser because scripted calls to NSE and BSE returned Access Denied on 2026-10-29. One window,
  04-Aug-2026 (the "New Listing" row, no attachment) to 27-Oct-2026: 15 announcements listed, 14 with
  attachments, 10 distinct PDFs downloaded (four pairs are the same PDF filed under two categories; see DUP
  sets). Housekeeping categories dropped (board-meeting intimations, newspaper publications, trading-window
  closures, Reg 74(5), investor complaints, shareholding patterns, Reg 7(3), Reg 40, record dates, large-corporate
  forms, secretarial compliance). Attachments from `xml-data/corpfiling/AttachLive/`, falling back to `AttachHis/`,
  `curl -C -` with three retries. File name = filing date + BSE attachment name.
- prospectus/: added by the orchestrator on 2026-10-29. The Red Herring Prospectus dated 22-Jul-2026 from the
  lead manager's site (hemsecurities.com, offer file 3097), found through a web search by the orchestrator, and
  BSE notice 20260803-8 from bseindia.com/downloads/UploadDocs/Notices. The post-pricing final Prospectus is
  not held; the issue price comes from AR26 p.36 and the BSE notice.
- credit-ratings/: `tools/collector/fetch_ratings.py` over the two CRISIL links on the screener.in page. Both are
  HTML with extracted text beside each; no page markers, cited by file.
- market-data-2026-10-29.md: screener.in company page, a service record (28-Oct-2026 close), cited as "MD" for
  market cap, price and the shareholding cross-check only.
- Text: PyMuPDF; Tesseract OCR on pages with under 40 characters of native text, tagged `[OCR]`.

## Integrity check (2026-10-29)

All 19 PDFs (3 screener, 14 filings, 2 prospectus) opened with PyMuPDF. Every page's text was extracted, page
markers in each `.txt` match the PDF page count, and every file carries `%%EOF` in its last 2 KB. 31 filing
pages and 5 screener pages carry `[OCR]`; the RHP and the BSE notice have 0 OCR pages. The two prospectus
files were re-checked for `%%EOF` by the analyst. 6 md5 duplicate sets, listed in
`dup-sets-2026-10-29.json`. **No broken file.**

## Substantive files, read

| Short name | Path | Period / date | Pages | Status | Pages read |
|---|---|---|---|---|---|
| H1 res | filings/20261022_e83a62c2-b9eb-42f0-99ea-3a733ee7eccd.pdf | H1 FY27 results, filed 22-Oct-2026 | 59 | FULL (pp.1-10) | 1-2 (outcome, monitoring-agency note), 3-4 (review report [OCR]), 5 (P&L [OCR], checked on the page image), 6 (balance sheet [OCR], checked), 7 (cash flow [OCR], checked), 8 (notes: AS 25, SME, IPO), 9-10 (Reg 32 statement [OCR]). pp.11-59 are the deck, read under Deck. DUP = 20261022_97c4e0a4 |
| Deck | screener/Investor_Presentation_1.pdf | H1 FY27 investor presentation, 22-Oct-2026 | 49 | FULL | 4-6 (snapshot, MD and CFO letters), 7 (leadership), 8 (IPO subscription), 11-12 (mix), 23 (milestones), 24 (geography), 28-32 (customers, awards, plants, utilisation, order book), 34 (strategy), 38-42 (P&L, verticals, IPO deployment), 44-48 (annual P&L, balance sheet, cash flow, shareholding). 5 pages [OCR] are section dividers. DUP = filings/20261022_bf29cc9c |
| Call | screener/Concall_Oct_2026_Transcript.pdf | H1 FY27 call of 23-Oct-2026, filed 27-Oct-2026 | 19 | FULL | 1-19. DUP = filings/20261027_832e6b63 |
| AR26 | screener/Annual_Report_2026.pdf | FY26, AGM notice for 29-Sep-2026 | 70 | PART | 4 (board, KMP), 9-12 (highlights, IPO, chairman, CFO), 28-29, 33-34 (AGM material RPT resolutions, Rs 50 crore each), 36-37 (listing, IPO price, objects, RPT), 42 (AOC-2), 49 (MD&A ratios), 50 (audit opinion), 53 (CARO), 56 (P&L), 57 (share capital), 59 (borrowings), 61 (payables), 64 (other expenses), 65-66 (contingent liabilities, capital commitments, MSME), 67 (related parties). DUP = filings/20260907_9589980c and 20260907_cf51f0f7 |
| RHP | prospectus/Prospectus-Hem-Securities-3097.pdf | Red Herring Prospectus, 22-Jul-2026 | 374 | PART | 2 (cover, promoters, issue structure), 25-26 (top ten customers), 29-30 (auditor, disqualifications, missing records), 42 (litigation summary), 47 (cost of acquisition risk), 61-63 (related-party schedule, three years), 79-80 (bonus, private placement allottees), 89-90 (promoter cost, pre and post-issue holding), 95-97 (objects, schedule, capacity), 113-115 (basis for price, peers), 118 (pre-IPO price), 143 (capacity utilisation), 190-193 (promoters), 276-278 (promoter tax matters) |
| Notice | prospectus/BSE-listing-notice-20260803-8.pdf | BSE notice, 03-Aug-2026, segment SME | 2 | FULL | 1-2 |
| U3 | filings/20260902_2f9d77d0-7ea0-45da-b220-e556b96fbcda.pdf | Unit III partial commencement, dated 30-Aug-2026 | 2 | FULL | 1-2 |
| PriceClar | filings/20260902_f31d10ca-c9e8-42c8-886d-271cd6562809.pdf | Reply to BSE price-movement query, 01-Sep-2026 | 1 | FULL | 1 |
| Solar | filings/20260916_e857ff9d-b4ac-4e94-ac8c-9fce0b8af673.pdf | Solar project commencement, 16-Sep-2026 | 2 | FULL | 1-2 |
| AGM-out | filings/20260929_01227a17-c577-4b43-bac9-f0d83b6f4cc6.pdf | AGM outcome: statutory and secretarial auditors appointed | 5 | FULL | 1-5. DUP = 20260929_a337457a |
| BM-Aug | filings/20260817_01487b67-4dd3-419e-b511-785a12108f96.pdf | Board outcome 17-Aug-2026: AGM date, secretarial auditor | 2 | FULL | 1-2. DUP = 20260817_4a4e083f |
| Audio | filings/20261023_53bad11f-028e-4989-90d9-b485ab1f1617.pdf | Audio recording intimation, 23-Oct-2026 | 1 | FULL | 1 |
| CRISIL-Jul | credit-ratings/02-CRISIL.html (.txt) | Rating rationale, BBB+/Stable/A2 assigned, 27-Jul-2026 | n/a | FULL | whole text |
| CRISIL-Aug | credit-ratings/01-CRISIL.html (.txt) | Credit bulletin on listing, 10-Aug-2026 | n/a | FULL | whole text |

Held, SKIM or not opened beyond page 1: none. Every held file was read.

DUP sets (md5), from `dup-sets-2026-10-29.json`: (1) 20260817_01487b67 = 20260817_4a4e083f (board outcome
filed twice); (2) 20260907_9589980c = 20260907_cf51f0f7 = screener/Annual_Report_2026.pdf (AR filed as AGM
notice and as Reg 34 report); (3) 20260929_01227a17 = 20260929_a337457a (auditor appointment filed twice);
(4) 20261022_97c4e0a4 = 20261022_e83a62c2 (results filed as outcome and as results); (5) 20261022_bf29cc9c =
screener/Investor_Presentation_1.pdf; (6) 20261027_832e6b63 = screener/Concall_Oct_2026_Transcript.pdf.
The results PDF (59 pages) also embeds the deck as pp.11-59.

## Gaps (NOT FOUND, with where it was looked for)

- **Final Prospectus (post-pricing).** Not held; the RHP leaves the issue price, P/E and general-corporate
  amount blank (RHP pp.95, 113-115). Issue price Rs 301 and the object amounts are taken from AR26 pp.36-37 and
  Deck p.42.
- **Monitoring agency report** for the quarter ended 30-Sep-2026. The board had not received it on 22-Oct-2026
  (H1 res p.2). Not in the BSE ledger to 27-Oct-2026.
- **Customer names.** Withheld under NDA on the call (Call p.10); the RHP gives shares of revenue only
  (RHP pp.25-26). Step 2 and 3 use shares and the award names on Deck p.29.
- **Pledge disclosure.** No pledge line in the H1 res, no SAST or pledge filing in the BSE ledger, no pledge
  figure in the MD. Step 4 marks it NOT FOUND.
- **Segment margins by vertical.** One 60:40 margin split stated on the call (Call p.9); nothing filed. The
  company reports one segment (H1 res p.8).
- **Pre-listing results, earlier calls or decks.** None exist; the company listed on 04-Aug-2026. FY24 and FY25
  come from the RHP restated statements, AR26 p.56 and Deck p.45.
- **Shareholding pattern filing for 30-Sep-2026.** Dropped as housekeeping; the Deck p.48 figure (63.8%) and
  the MD figure (60.63%) disagree, and the RHP post-issue table (60.63%, p.90) is used.
- **Lock-in schedule for pre-IPO holders.** The RHP states a 20% promoter lock-in (RHP p.92 area); the dates of
  expiry for the Oct-2025 private-placement holders were not extracted. Weakens the step 12 "what would change"
  line on selling.
