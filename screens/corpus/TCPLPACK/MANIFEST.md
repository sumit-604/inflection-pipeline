# Corpus manifest: TCPLPACK (two collections, merged 2026-11-04)

Two runs collected documents for this company. Both ledgers are kept below. Files from the 2026-10-30 run sit in the top-level category folders; files from the 2026-11-04 run sit under inputs/.

## Collection of 2026-11-04

### Corpus manifest: TCPLPACK

Collected 2026-11-04.

#### Identity
- Company: TCPL Packaging Ltd (screener name field came back empty in collect.log)
- NSE: TCPLPACK; BSE: 523301; ISIN: not recorded (collector does not capture it)
- Screener: https://www.screener.in/company/TCPLPACK/consolidated/
- Q2 FY27 results due 5-Nov-2026; not yet filed.

#### Documents held
Page markers in .txt are `[page n]` (not `===== PAGE n =====`).

| File | Document | Period | Filed | Pages | Text |
|---|---|---|---|---:|---|
| annual-report/Annual_Report_2026.pdf | Annual report | FY26 | - | 309 | OK |
| annual-report/Annual_Report_2025.pdf | Annual report | FY25 | - | 306 | OK |
| results/TCPLPACK-result-Q1FY27-2026-08-11.pdf | Results (BSE) | Q1 FY27 | 2026-08-11 | 7 | OK |
| results/TCPLPACK-result-Q4FY26-2026-05-28.pdf | Results (BSE, AttachHis) | Q4 FY26 | 2026-05-28 | 19 | OK |
| concalls/Concall_Aug_2026_Transcript.pdf | Transcript | Q1 FY27 | Aug 2026 | 18 | OK |
| concalls/Concall_Jun_2026_Transcript.pdf | Transcript | Q4 FY26 | Jun 2026 | 13 | OK |
| concalls/Concall_Feb_2026_Transcript.pdf | Transcript | Q3 FY26 | Feb 2026 | 13 | OK |
| concalls/Concall_Nov_2025_Transcript.pdf | Transcript | Q2 FY26 | Nov 2025 | 13 | OK |
| presentations/Investor_Presentation_1.pdf | Investor presentation (period not checked) | - | - | 18 | OK |
| credit-ratings/01-CRISIL.html/.txt | CRISIL rationale | 21 May 2026 | - | - | text OK (A+/Stable reaffirmed) |
| credit-ratings/02-CRISIL | CRISIL | 11 Sep 2025 | - | - | OK |
| credit-ratings/03-ICRA | ICRA | 27 Aug 2025 | - | - | OK |
| credit-ratings/04-CRISIL | CRISIL | 10 Jul 2025 | - | - | OK |
| credit-ratings/05-CRISIL | CRISIL | 1 Aug 2024 | - | - | OK |
| credit-ratings/06-CRISIL | CRISIL | 9 Jul 2024 | - | - | OK |
| screening/Financials.xlsx | Screener export | - | - | - | n/a |

#### Known gaps
- Shareholding pattern: not collected (screener Financials.xlsx only).
- Q2 FY27 results: not yet filed (due 5-Nov-2026).
- Earlier ICRA rating: only Aug 2025 held; no ICRA 2026 link on screener.
- Defects: collector printed empty Company name; fetch_ratings.py BSE-style header needs Origin+Accept (curl with only Referer got Access Denied from api.bseindia.com, python requests with Origin worked); extractor marker is `[page n]`.

## Collection of 2026-10-30

### TCPLPACK corpus manifest

TCPL Packaging Ltd (formerly Twenty First Century Printers Ltd, renamed 2008).
NSE TCPLPACK, BSE 523301, ISIN INE822C01015 (AR26 p.274). Promoter: Kanoria family, 55.74% at
31-Mar-2026 (AR26 p.273). New wholly owned subsidiary TCPL Energy Materials Ltd, incorporated
24-Sep-2026 for lithium-ion battery separator film.
Ledger written 2026-10-30. Card: `screens/cards/TCPLPACK.md`.

Status key: FULL = read in full; PART = key sections read, rest navigated by keyword; SKIM =
housekeeping or duplicate content, checked for substance; DUP = md5-identical to another held
file. Page numbers are PDF page numbers. Transcript PDF page = printed "Page N of M" plus one.

#### How it was built

Sources exactly as `fetch-ledger-2026-10-30.jsonl` records them:

- screener/: links listed on the public screener.in page for TCPLPACK, fetched 2026-10-30
  09:41-09:42. They resolve to bseindia.com `xml-data/corpfiling/AttachHis/` (annual reports FY25
  and FY26) and `stockinfo/AnnPdfOpen.aspx` redirecting to `AttachHis/` (four transcripts, the
  Q4 FY26 deck). The Q1 FY27 deck came from tcpl.in
  (`wp-content/uploads/2026/08/Earning-Presentation-Q1-FY-2026-27.pdf`).
- results/: screener.in quarter links (`screener.in/company/source/quarter/3384/<m>/<yyyy>/`),
  each redirecting to a BSE `AttachHis/` results PDF. Periods checked on page 1 of each: Q1 FY26,
  Q2 FY26, Q3 FY26, Q4 FY26, Q1 FY27. All five are the stated period.
- filings/: BSE announcements listed through the bseindia.com announcements form in the in-app
  browser on 2026-10-30, windows 30-Oct-2025 to 30-Apr-2026 (29 rows) and 01-May-2026 to
  30-Oct-2026 (49 rows); housekeeping, ESOP allotments and SAST 29(1)/29(2) forms dropped; 31 rows
  kept in `work/bse/TCPLPACK.txt`. 21 attachments downloaded from `AttachHis/`, 10:01-10:04. The
  other 10 rows are held under screener/ or results/ (same BSE attachment).
- credit-ratings/: `tools/collector/fetch_ratings.py` over the four rating links on the
  screener.in page (three CRISIL HTML, one ICRA HTML). The ICRA HTML is a site shell; the
  rationale PDF came from ICRA's `Rating/ShowRationalReportFilePdfViewer/137263` path.
- market-data-2026-10-30.md: screener.in consolidated company page, about 09:00 IST 2026-10-30.
  A service record, not a filed document.
- Financials.xlsx: absent. The screener collector's browser could not start this run. The
  trajectory was built from filed results and the annual reports.
- Text: PyMuPDF; Tesseract OCR on low-text pages, tagged `[OCR]`.

#### Integrity (from the ledger)

35 ledger rows, all status OK, every byte count equal to the declared size. 1,262 pages in all,
42 OCR pages. Page markers in each `.txt` match the ledger page count. Four md5 duplicate sets:
(1) screener/Annual_Report_2026 = filings/20260717_c6ceddb0 ("AGM notice"); (2) results/q-2026-03
= filings/20260528_ccdd5154 (BSE title "Change in Management"; the results bundle carries the
re-appointments); (3) results/q-2025-12 = filings/20260209_468fdfb9 (BSE title "Change in
Management"; the results bundle carries the chairman change); (4)
screener/Investor_Presentation_Aug_2026 = filings/20260811_85f207dd.

Defects found by the analyst:
- results/q-2026-06 pp.3-7: text layer is noisy with no `[OCR]` tag ("Other expenses n.40",
  "10.05)" for (0.05)). Consolidated p.7 was read from the page image: other expenses 77.40,
  revenue 492.97, PAT 40.01, finance cost 12.28. The card uses the image.
- screener/Annual_Report_2026 p.14: chart labels extract out of order (PAT series reads 46.87,
  110.44, 99.39, 97.80, 143.01). The page image gives FY22-FY26 as 46.87, 110.44, 99.39, 143.01,
  97.80. The card uses the image.
- screener/Annual_Report_2026 p.13 labels Rs 1,835.59 crore "Revenue from Operations"; FY26 res
  p.16 shows that figure is total income. Document defect, not a fetch defect.
- results/q-2025-12 p.9 and filings/20260811_ac8050af pp.5-26 are OCR scans; the AGM vote counts
  used in the card come from the native-text scrutinizer report (pp.31-39).

#### Substantive files, read

| Short name | Path | Period / date | Pages | Status | Pages read |
|---|---|---|---|---|---|
| AR26 | screener/Annual_Report_2026.pdf | FY26, AGM 11-Aug-2026 | 309 [1 OCR] | PART | 13-16 (highlights, 10-year table, ROCE), 51 (capital efficiency), 92-95 (MD&A, directors' report), 108 (pay ratios), 184-186 (geography split, contingent, related parties), 189 (forex exposure), 199 (consolidated KAM), 273-274 (shareholding, ISIN). Keyword search for pledge: no hit |
| AR25 | screener/Annual_Report_2025.pdf | FY25 | 306 [2 OCR] | PART | 87 (FY24 and FY25 consolidated summary) |
| Q1 res | results/q-2026-06.pdf | Q1 FY27, filed 11-Aug-2026 | 7 | FULL | 1-7; p.7 read from image |
| FY26 res | results/q-2026-03.pdf | Q4 and FY26 audited, filed 28-May-2026, Rs lakh | 19 | PART | 1-4 (outcome, dividend, re-appointments), 10-11 (standalone cash flow, notes), 12-15 (auditor), 16-18 (consolidated P&L, balance sheet, cash flow) |
| Q3 res | results/q-2025-12.pdf | Q3 FY26, filed 09-Feb-2026 | 11 [1 OCR] | PART | 1-3, 8-10 (chairman change, resignation letter, press release); Q3 figures taken from FY26 res p.16 |
| Q2-26 | results/q-2025-09.pdf | Q2 and H1 FY26, Rs lakh | 12 | PART | 9 (consolidated P&L with H1 FY25 and FY25 columns) |
| Q1-26 | results/q-2025-06.pdf | Q1 FY26 | 6 | SKIM | 2, 4 (Accura acquisition note); figures taken from Q1 res comparatives |
| NLB | filings/20260811_b0a908fe.pdf | Press release, new line of business, 11-Aug-2026 | 4 | FULL | 1-4 |
| NLB deck | filings/20260811_6816e2ba.pdf | Presentation, new line of business | 13 | FULL | 1-13 |
| TEML | filings/20260924_93bd0c57.pdf | TCPL Energy Materials Ltd incorporated 24-Sep-2026 | 3 | FULL | 1-3 |
| Call Aug-26 | screener/Concall_Aug_2026_Transcript.pdf | Q1 FY27 call, 12-Aug-2026 | 18 | FULL | 1-18 |
| Call Jun-26 | screener/Concall_Jun_2026_Transcript.pdf | Q4 FY26 call | 13 | PART | 3, 6-12 (MTM, deferred tax, Chennai, flexible share, no guidance, capex) |
| Call Feb-26 | screener/Concall_Feb_2026_Transcript.pdf | Q3 FY26 call | 13 | PART | 3-9, 11-12 by keyword (volume, utilisation, exports, capex) |
| Call Nov-25 | screener/Concall_Nov_2025_Transcript.pdf | Q2 FY26 call | 13 | PART | 4-6, 10-11 by keyword (aspiration, borrowing rate, utilisation, MTM) |
| Deck Q1 | filings/20260811_85f207dd.pdf | Q1 FY27 deck | 18 [3 OCR] | FULL | 1-18. DUP = screener/Investor_Presentation_Aug_2026 |
| Deck Q4 | screener/Investor_Presentation_Jun_2026.pdf | Q4 FY26 deck | 23 [2 OCR] | PART | 5-11 |
| AGM | filings/20260811_ac8050af.pdf | 38th AGM outcome and scrutinizer report | 40 [22 OCR] | PART | 1-4 (proceedings, nine items), 27-39 (scrutinizer counts, item 6: 10.70% against) |
| Accura | filings/20260209_2e0d1854.pdf | Gravure cylinder plant start, 09-Feb-2026 | 1 | FULL | 1 |
| Clean Max | filings/20260309_13473b8c.pdf | 26% of captive solar SPV, Rs 1.09 crore | 2 | FULL | 1-2 |
| Sub-RI | filings/20251215_0276defe.pdf; 20260324_243f526f.pdf | Rights issues in COPPL (Rs 1.00 and 2.29 crore) and ATPL (Rs 2.49 crore) | 5 / 3 | FULL | 1-5 / 1-3 |
| Letter | filings/20260718_0f203e51.pdf | AR web-link letter | 2 | FULL | 1-2 |
| Q3 PR | filings/20260209_4a42f5be.pdf | Q3 FY26 press release | 5 | PART | 2 |
| CRISIL-26 | credit-ratings/01-CRISIL.txt | A+/Stable, A1 reaffirmed, 21-May-2026 | HTML | FULL | whole rationale |
| CRISIL-25 | credit-ratings/02-CRISIL.txt | Upgrade to A+/Stable, 11-Sep-2025 | HTML | PART | rating action and rationale opening |
| CRISIL-B | credit-ratings/04-CRISIL.txt | Bank-facility bulletin, 10-Jul-2025 | HTML | SKIM | lender table |
| ICRA-25 | credit-ratings/03-ICRA-rationale.pdf | [ICRA]A (Stable) reaffirmed, 27-Aug-2025 | 7 | PART | 1-4 |
| MD | market-data-2026-10-30.md | screener.in, 30-Oct-2026 | - | FULL | Market cap, PE, shareholding |

Held, SKIM or not opened beyond page 1: Q2 FY26 press releases (filings/20251114_ec5b78bb,
_568f4651) and deck (_f3314196); Q3 FY26 deck (filings/20260209_ba9b0079); Q4 FY26 press release
(filings/20260528_b2900062); Q1 FY27 press release (filings/20260811_9c18a058); physical-share
re-lodgement advertisement (filings/20260305_fe1a08a4, 2 OCR pages); the four DUP copies;
credit-ratings/03-ICRA.html and .txt (site shell); credit-ratings/manifest.json; fetch ledger.

#### Gaps (NOT FOUND, with where it would come from)

- **Q2 FY27 results, deck and call transcript.** Not filed; results due 5-Nov-2026 (BSE
  announcements, results category).
- **Rating action after the separator announcement.** CRISIL-26 (21-May-2026) and ICRA-25
  (27-Aug-2025) both predate 11-Aug-2026. Would come from CRISIL or ICRA rating lists.
- **Separator technology source, land site, capital subscribed and debt share.** TEML p.2 files
  only Rs 10 crore authorised capital. Would come from a TEML capital-infusion Reg 30 filing, the
  H1 FY27 results notes, or the Q2 FY27 call.
- **Euro ECB hedge status and repayment schedule.** AR26 p.189 gives the exposure only. Would come
  from AR26 borrowings note (not read) or the Q2 FY27 call.
- **Promoter pledge.** Not in AR26 (keyword search), CRISIL-26 or ICRA-25. Shareholding-pattern
  and SAST filings were dropped as housekeeping. Would come from BSE Reg 31 shareholding filings.
- **Reg 23(9) half-yearly related-party disclosures.** Not in the 31 kept rows. Would come from BSE
  related-party category.
- **Product or segment revenue split.** One reported segment; only the verbal "flexible is about
  20%" (Call Jun-26 p.10). Export split by region not disclosed (Call Aug-26 p.8).
- **Plant-wise capacity and utilisation.** Only verbal: folding carton "70-plus percent", Chennai
  "more than 50%" (Call Aug-26 p.5; Call Jun-26 p.7).
- **Financials.xlsx.** Absent this run (collector browser did not start).
