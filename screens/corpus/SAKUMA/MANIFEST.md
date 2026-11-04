# SAKUMA corpus manifest

Sakuma Exports Ltd. NSE SAKUMA, BSE 532713, ISIN INE190H01024 (AGM-26 p.1).
Promoter: Saurabh Malhotra and family, 46.29% (AR26 p.89); 32.72% after the proposed preferential
issue (EGM p.15).
Ledger written 2026-10-30. Card: `screens/cards/SAKUMA.md`.

Status key: FULL = read in full; PART = key sections read, rest navigated by keyword; SKIM =
housekeeping, checked for substance; DUP = byte-identical to another held file (cmp checked).
Page numbers are PDF page numbers. In AR26 the PDF page number runs three ahead of the printed
page (PDF p.16 = printed p.13).

## How it was built

- screener/: annual reports linked from the public screener.in page
  (https://www.screener.in/company/SAKUMA/consolidated/). Both ARs were fetched from BSE
  `AttachHis/` (FY26: 30284b6c-...; FY25: 16908bda-...), per the fetch ledger. No transcripts or
  presentations exist on screener.in for this name.
- results/: screener.in quarter links (`/company/source/quarter/2848/<m>/<yyyy>/`), each resolving
  to a BSE `AttachHis/` PDF. Periods checked on page 1: q-2025-06 = Q1 FY26, q-2025-09 = Q2 and H1
  FY26, q-2025-12 = Q3 and 9M FY26, q-2026-03 = Q4 and FY26 audited, q-2026-06 = Q1 FY27. All correct.
- filings/: BSE announcements listed through the bseindia.com announcements form in the in-app
  browser, 2026-10-30, in two windows (30-Oct-2025 to 30-Oct-2026, 45 rows; 30-Oct-2024 to
  29-Oct-2025, 47 rows). Housekeeping dropped (newspaper, trading window, Reg 74(5), board-meeting
  intimations, book closure, large corporate). 41 rows kept in `work/bse/SAKUMA.txt`; 34
  attachments downloaded from `AttachHis/`. The other 7 rows are held elsewhere: the two Reg 34
  annual reports as screener/ ARs, and five results attachments as results/ files. File name =
  filing date + first 8 characters of the BSE attachment name.
- credit-ratings/: `tools/collector/fetch_ratings.py` over the four rating links on the screener.in
  page (Infomerics PDF 07-Sep-2026; ICRA 18-Jun-2025 and 31-Jan-2023; Acuite 05-Nov-2021). The ICRA
  `NN-ICRA.html/.txt` files are 5.6 KB site shells; the rationales came through ICRA's
  ShowRationalReportFilePdfViewer path as `NN-ICRA-rationale.pdf`.
- prospectus/: none; not a recent IPO.
- market-data-2026-10-30.md: screener.in consolidated company page, about 09:00 IST 30-Oct-2026,
  a service record (market cap Rs 298 crore, price Rs 1.90, P/E 27.9, book value Rs 4.78).
- Financials.xlsx: absent this run (the screener collector's browser could not start). The
  financial trajectory was built from filed results, the ARs and the rating rationales.
- Text: PyMuPDF; Tesseract OCR on pages with under 40 characters of native text, tagged `[OCR]`.

## Integrity check (from fetch-ledger-2026-10-30.jsonl)

42 ledger rows, all status OK. Byte size matches the exchange-declared size on 40 rows; 2 rows
carry no declared size (filings/20250826_f74156d1, filings/20250722_d449c1f9). Pages: AR26 173,
AR25 178, results 6 to 15, filings 1 to 23. OCR pages: AR26 2, AR25 3, results/q-2025-09 10,
results/q-2025-06 5, filings/20251114_700564c8 10, filings/20261027_efb2d14f 1. The Infomerics and
Acuite PDFs are recorded in credit-ratings/manifest.json, not the ledger (HTTP 200, 331,181 and
144,680 bytes). DUPs by cmp: results/q-2026-06 = filings/20260813_ac138f77; results/q-2026-03 =
filings/20260530_980ae19a.

Defects found by the analyst:
- **Garbled native text, no `[OCR]` tag.** filings/20260813_ac138f77 p.8 (consolidated Q1 FY27)
  reads the Q4 FY26 inventory change as "(42,237.88)"; the page image reads (12,237.88), as does
  filings/20260530_980ae19a p.3. Every Q1 FY27 figure in the card was read from the page image.
- **OCR page with no text.** filings/20261027_efb2d14f p.13 is tagged `[OCR]` and empty; the image
  is a blank page. Nothing is lost.
- **Scanned results pages.** filings/20251114_700564c8 pp.2-11 are OCR text; Q2 FY26 consolidated
  figures were read from the p.5 image.
- **Issuer errors, not corpus errors.** The 23-Oct-2026 board outcome says the board met "today
  i.e. 19th October 2026" in both the original and the revision. The original outcome showed
  post-issue holdings of 4.82% where the revision shows 4.87%. The original EGM notice set a book
  closure for 18-20 Nov-2026 that the revision drops.

## Substantive files, read

| Short name | Path | Period / date | Pages | Status | Pages read |
|---|---|---|---|---|---|
| Board | filings/20261024_b5e93f63 | Revised outcome, board meeting 23-Oct-2026 | 4 | FULL | 1-4 |
| Board-orig | filings/20261023_e7ef5412 | Original outcome, 23-Oct-2026 | 4 | FULL | 1-4; diffed against the revision |
| EGM | filings/20261027_efb2d14f | Revised EGM notice for 21-Nov-2026 | 18 [1 OCR] | FULL | 1-18 (p.13 blank image) |
| EGM-orig | filings/20261027_5cb118cc | Original EGM notice | 18 | FULL | Diffed against the revision; differences listed above |
| Q1 res | filings/20260813_ac138f77 | Q1 FY27, filed 13-Aug-2026 | 8 | FULL | 1-8; p.8 read from image |
| FY26 res | filings/20260530_980ae19a | Q4 and FY26 audited, filed 30-May-2026 | 15 | FULL | 1-15; p.3 read from image |
| Q3-26 | filings/20260214_8ac18e5c | Q3 and 9M FY26, filed 14-Feb-2026 | 8 | PART | Results pages and notes; Q3 figures taken from FY26 res p.3 comparatives |
| Q2-26 | filings/20251114_700564c8 | Q2 and H1 FY26, filed 14-Nov-2025 | 11 [10 OCR] | PART | 1, 2, 5 (image), 6 |
| AR26 | screener/Annual_Report_2026.pdf | FY26, AGM 29-Sep-2026 | 173 [2 OCR] | PART | 3 (board, bankers), 4, 7 (Grover profile), 14-24 (board report, AOC-1 p.19, forex p.20), 25-28 (MD&A), 29 (pay ratios), 32-33 (secretarial audit), 36 (board composition), 47 (director pay), 62 (KAMs), 87 (mutual funds), 89 (promoters), 100 (receivable ageing), 103 (contingent liabilities), 107-109 (related parties), 138 (consolidated PPE) |
| AR25 | screener/Annual_Report_2025.pdf | FY25 | 178 [3 OCR] | SKIM | 22-23 (FY24 and FY25 highlights), 98-99 (rights issue, bonus) |
| Rights-MA | filings/20241114_af8e4038 | Reg 32 statement and ICRA monitoring report, rights issue | 14 | PART | 1-14 |
| Cancel | filings/20260925_4dd06432 | Board meeting of 30-Sep-2026 cancelled | 1 | FULL | 1 |
| PriceQ | filings/20260407_79652348 | Reply to BSE price-movement query | 1 | FULL | 1 |
| SAST | filings/20250404_08555561 | Reg 31(4), no encumbrance in FY25 | 2 | FULL | 1-2 |
| PSP | filings/20251001_61a5b6d2 | SEL Performance Share Plan 2025 approved | 2 | FULL | 1-2 |
| Appts | filings/20251001_4b96fe23 | Auditors appointed, Amist re-appointed | 2 | FULL | 1-2 |
| BM-25 | filings/20250826_f74156d1 | Board outcome 26-Aug-2025, PSP adopted | 2 | FULL | 1-2 |
| BM-26 | filings/20260829_9581f330 | Board outcome 29-Aug-2026 | 2 | FULL | 1-2 |
| AGM-26 | filings/20260930_d90b329c | AGM 2026 voting results | 6 | PART | 1-4 |
| AGM-out | filings/20260929_383edaab | AGM 2026 proceedings | 1 | FULL | 1 |
| Reg24A | filings/20260527_81e9ed71 | Annual secretarial compliance report FY26 | 6 | SKIM | Deviation table: none |
| INF-26 | credit-ratings/01-Infomerics.pdf | IVR BBB/Stable assigned, 07-Sep-2026 | 9 | FULL | 1-9 |
| ICRA-25 | credit-ratings/02-ICRA-rationale.pdf | BBB (Stable)/A3+ reaffirmed, 18-Jun-2025 | 8 | PART | 1-4 |
| ICRA-23 | credit-ratings/03-ICRA-rationale.pdf | BBB (Stable)/A3+ reaffirmed, 31-Jan-2023 | 8 | SKIM | 1 |
| ACU-21 | credit-ratings/04-Acuite.pdf | BB+ downgraded and withdrawn, 05-Nov-2021 | 3 | SKIM | 1 |
| MD | market-data-2026-10-30.md | screener.in, 30-Oct-2026 | - | FULL | Ratios, shareholding |
| Q1-26 | results/q-2025-06.pdf | Q1 FY26 | 6 [5 OCR] | SKIM | Period and headline lines; figures taken from Q1 res comparatives |
| Q2-26r | results/q-2025-09.pdf | Q2 and H1 FY26 results attachment | 11 [10 OCR] | SKIM | Period check |
| Q3-26r | results/q-2025-12.pdf | Q3 FY26 results attachment | 8 | SKIM | Period check, revenue lines |

Held, SKIM or not opened beyond page 1: Q2 FY25 results (20241114_40bb0457), Q3 FY25 results
(20250214_6a3d6ce4), FY25 results (20250530_5f5240c7), CS resignations and appointments
(20241114_f4a4dfb2, 20250206_5c875d04, 20250722_0e49620d, 20250722_d449c1f9), board outcome
22-Jul-2025 (20250722_5886236a), secretarial auditor appointment (20250530_908785f6), AGM 2025
notice (20250903_fbfc0f1c), AGM 2025 scrutinizer reports (20251001_9723df0d, 20251001_15cff10d),
board-meeting time change (20260529_abc8d5a4), AGM 2026 notice (20260903_8f392341), ICRA HTML
shells (02-ICRA, 03-ICRA).

## Gaps (NOT FOUND, with where it was looked for)

- **Q2 FY27 results.** Not filed by 30-Oct-2026; the last BSE row is 27-Oct-2026. Will come from
  BSE by 14-Nov-2026.
- **Concall transcripts and investor presentations.** None on screener.in; none in the 92 BSE
  announcements listed.
- **Product, volume and geography split.** Not in AR26 (pp.14-16, 25-28) or any results note
  (single segment).
- **Reg 23(9) related-party disclosures, shareholding-pattern filings, FY26 Reg 31(4)
  declaration.** Not in the kept BSE list (dropped as housekeeping or not listed). Would come from
  BSE corporate filings.
- **The PCS certificate under ICDR for the preferential issue.** Referenced at
  sakumaexportsltd.com (EGM p.18); not fetched under the no-new-fetch rule.
- **Identity and business links of the nine allottees.** The EGM notice names the owners of the two
  entities only (EGM p.16). Would need a live-web promoter dig, outside shallow scope.
- **What and where the Rs 106 crore "Warehouse" asset is.** AR26 p.138 gives the class only; the
  board report and AOC-1 (AR26 pp.15-19) are silent.
- **ICRA's 2026 rating status.** Latest held is 18-Jun-2025; Infomerics (07-Sep-2026) reports no
  non-cooperation with a previous agency. Would come from icra.in.
- **Infomerics lender annexure.** Linked at an Infomerics blob URL (INF-26 p.7); not fetched.
- **FY28 forward basis.** No guidance in any held document.
