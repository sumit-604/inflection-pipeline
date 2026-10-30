# OPTIEMUS corpus manifest

Optiemus Infracom Ltd. NSE OPTIEMUS, BSE 530135, ISIN INE350C01017 (AR26 p.127).
Promoter: Ashok Gupta family, 72.17% at 31-Mar-2026 (AR26 p.126); 71.10% at Sep-2026 (market data, service record).
Ledger written 2026-10-30. Card: `screens/cards/OPTIEMUS.md`.

Status key: FULL = read in full; PART = key sections read, rest navigated by keyword; SKIM =
housekeeping, checked for substance; DUP = byte-identical to another held file (md5 from the ledger).
Page numbers are PDF page numbers. In AR26 the printed page number is the PDF page less 2.

## How it was built

- screener/: the screener.in public page (https://www.screener.in/company/OPTIEMUS/consolidated/)
  links the annual reports and decks; the ledger shows each file downloaded from BSE
  `xml-data/corpfiling/AttachHis/` (decks via `stockinfo/AnnPdfOpen.aspx`), 2026-10-30. Two annual
  reports (FY25, FY26) and two decks (May-2026, Aug-2026). No transcript is listed on screener.in.
  Financials.xlsx is absent this run (the screener collector's browser could not start).
- results/: screener.in quarter links (`/company/source/quarter/2342/<m>/<y>/`), each resolving to a
  BSE AttachHis PDF. Periods confirmed on page 1: q-2025-06 = Q1 FY26, q-2025-09 = Q2 FY26,
  q-2025-12 = Q3 FY26, q-2026-03 = Q4 and FY26 audited, q-2026-06 = Q1 FY27. No wrong period.
- filings/: BSE announcements listed through the bseindia.com corporates/ann form in the in-app
  browser, 2026-10-30, in three windows (30-Oct-2025 to 28-Feb-2026, 36 rows; 01-Mar-2026 to
  29-May-2026, 13 rows; 01-May-2026 to 30-Oct-2026, page 1 of 2 read to 30-May-2026, the overlap
  covered by the second window). Housekeeping and physical-share re-lodgement rows dropped. 54 rows
  kept. Attachments from `AttachHis/`. 47 are in filings/; the other 7 are held in screener/ or
  results/ (AR26, two decks, four results). File name = filing date + first 8 characters of the BSE
  attachment. List: `work/bse/OPTIEMUS.txt`.
- credit-ratings/: `tools/collector/fetch_ratings.py` over the four rating links on the screener.in
  page. ICRA rationales via ICRA's `ShowRationalReportFilePdfViewer/143896` and `/133833` paths
  (01-ICRA-rationale.pdf, 03-ICRA-rationale.pdf); 01-ICRA.txt and 03-ICRA.txt are 5.6 KB site shells
  with no content. CRISIL as HTML text (02-CRISIL). CARE PDF (04-CARE).
- prospectus/: not applicable (listed since 2011 per ICRA-26 p.4).
- market-data-2026-10-30.md: screener.in company page, fetched 2026-10-30, a service record.
- Text: PyMuPDF; Tesseract OCR on pages with under 40 characters of native text, tagged `[OCR]`.

## Integrity check (from the ledger, 2026-10-30)

58 ledger rows (9 screener and results, 47 filings, 2 ICRA rationales), all status OK, every byte
size equal to the exchange's declared size. 04-CARE.pdf comes from the ratings manifest (status
200). 59 PDFs in all. OCR pages: 8 (AR26 pp.2, 331; AR25 pp.2, 306; filings/20260905_a2cfccc3
pp.2, 331; Deck-Nov p.17; Deck-Feb p.20), all covers or closing slides.

Defects found by the analyst:
- **Garbled native text, no OCR tag.** results/q-2026-06 pp.2, 5-6 and results/q-2026-03 pp.9-12
  misread digits (Q1 FY27 revenue reads "8820933" and "8,299.33"; the image reads 88,299.33). Every
  figure from these pages and from results/q-2025-09 p.7 was read from the page image.
- **Mislabelled attachment.** filings/20251114_3bd664d5 ("Amendments to MoA and AoA") is
  byte-identical to results/q-2025-09 (Q2 FY26 results, md5 44b9e3f5...). The MoA amendment text
  itself is held only through the postal ballot notice (filings/20251118_ca6a0c4e).
- No truncated or zero-page file.

## Substantive files, read

| Short name | Path | Period / date | Pages | Status | Pages read |
|---|---|---|---|---|---|
| AR26 | screener/Annual_Report_2026.pdf | FY26, AGM 28-Sep-2026 | 331 [2 OCR] | PART | 5-6 (chairman), 9-12 (directors' report: financials, subsidiaries, warrants, use of proceeds, objects change), 33 (pay), 52-61 (MD&A, standalone ratios), 126-127 (shareholding, ISIN), 178-180 (Teleecare FVTPL), 218-222 (consolidated audit report, other matters), 264 (other current assets), 273 (other income, materials), 278-284 (related parties, borrowings), 300 (contingent). Keyword search for pledge, KAM, Teleecare, BlackBerry, customer. DUP = filings/20260905_a2cfccc3 |
| AR25 | screener/Annual_Report_2025.pdf | FY25 | 306 [2 OCR] | SKIM | 10 (FY24 and FY25 financial summary) |
| Q1-27 | results/q-2026-06.pdf | Q1 FY27, filed 04-Aug-2026 | 10 | FULL | 1-10; pp.5-6 from page image |
| FY26 res | results/q-2026-03.pdf | Q4 and FY26 audited, filed 30-May-2026 | 18 | PART | 9-12 from page image (P&L, segments, balance sheet, cash flow), 13-17 (notes, audit report, other matters) |
| Q3-26 | results/q-2025-12.pdf | Q3 and 9M FY26, filed 13-Feb-2026 | 10 | PART | 7-8 (notes: BIGTech and OUS losses, Rs 53.01 crore incentive claims) |
| Q2-26 | results/q-2025-09.pdf | Q2 and H1 FY26, filed 14-Nov-2025 | 13 | PART | 7 from page image (consolidated P&L), 11 (notes) |
| Q1-26 | results/q-2025-06.pdf | Q1 FY26 | 9 | SKIM | 1 (period); figures taken from Q1-27 comparatives |
| Deck-Aug | screener/Investor_Presentation_Aug_2026.pdf | Q1 FY27 | 19 | FULL | 1-19 |
| Deck-May | screener/Investor_Presentation_May_2026.pdf | Q4 FY26 | 15 | FULL | 1-15 |
| Deck-Nov | filings/20251114_a2105069 | Q2 FY26 deck | 17 [1 OCR] | FULL | 1-17 (Nothing JV, Ordinary Theory, ECMS applications) |
| Deck-Feb | filings/20260213_a8d1f0ba | Q3 FY26 deck | 20 [1 OCR] | FULL | 1-20 (seven partnership wins; charts have no labels in text) |
| MA-Q1 | filings/20260804_f252cdce | ICRA monitoring report, Q1 FY27 | 13 | FULL | 1-13 (issue size, objects change, utilisation Rs 216.857 crore, GCP use) |
| MA earlier | filings/20251114_b4e2140e; 20260213_2c78aaf7; 20260514_4623ef33 | Q2 FY26, Q3 FY26, Q4 FY26 | 13 each | SKIM | Proceeds credited (192.699, 201.389, 216.857 crore), deviation line, GCP table |
| Warrants | filings/20251216_b1a3155d; 20260102_76303ca0; 20260116_65406831; 20260721_b5f1cd26; 20260804_c6b4e76d; 20260811_421c5df1 | Six warrant conversions at Rs 672.25 | 1-2 each | FULL | All; Renu Gupta 3,75,000 (Jul-2026); shares 9,01,66,450 after 11-Aug-2026 |
| Rights / Rights-off | filings/20260309_6b008275; 20260402_fca006d1 | OEL Rs 156 crore and GDN Rs 40 crore rights, OEL dropped | 6 / 1 | FULL | All |
| BIG-GDN | filings/20260630_4499da18 (DUP 20260630_6e4bd66a) | BIGTech Rs 10.80 crore rights; GDN Rs 100 crore loan | 5 | FULL | 1-5 |
| GDN-Oct | filings/20261027_dc26abdb | GDN further Rs 50 crore loan; Rs 100 crore outstanding | 3 | FULL | 1-3 |
| OUS | filings/20260827_c6beb6b1 (DUPs 7c20ea8b, 4172f8e3, 5596bdee) | Board 27-Aug-2026: ID re-appointments, OUS Rs 5.60 crore | 6 | FULL | 1-6 |
| CMF | filings/20260922_0c180eae (DUPs 3b5ac4d2, a1bcd7c4) | Binding term sheet with Nothing, 51.1% of CMF JV | 7 | FULL | 1-7 |
| Ai+ | filings/20260312_0a31c3c7 | OEL and Ai+ manufacturing agreement | 4 | FULL | 1-4 |
| Quectel | filings/20260629_accb8538 | OEL and Quectel press release | 3 | FULL | 1-3 |
| Guarantees | filings/20251128_ab90134a; 20251227_f89d9a1b; 20260430_5bce66d7; 20260610_c2a32195; 20260923_4f98d08c; 20261012_41cee2b5 | OEL guarantees and customs surety | 1-2 each | FULL | All |
| OEL-MD | filings/20260701_e36a3beb | OEL MD resignation, Neetesh Gupta appointed | 1 | FULL | 1 |
| Shelat | filings/20260731_cc7af842 | President, New Projects resigned | 3 | FULL | 1-3 |
| SMP-Dec | filings/20251231_7bd3eda1 (DUP 20251231_fc1da673) | AVP retirement | 2 | FULL | 1-2 |
| Surv | filings/20260624_39f624b2; 20261007_aed5c74e | Volume surveillance replies | 1 each | FULL | 1 |
| Rating-int | filings/20260421_7f3ffb53 | CRISIL rating; mandate moved from ICRA | 1 | FULL | 1 |
| Factory | filings/20251219_279187fa | The Factory Pvt Ltd (Nothing JV) incorporated | 1 | FULL | 1 |
| PB | filings/20251118_ca6a0c4e; 20251222_d3a26cb3 | Postal ballot on objects clause; passed 99.9994% | 13 / 8 | PART | 1-5 / vote line |
| AGM | filings/20260928_c7bc606e | AGM proceedings 28-Sep-2026 | 4 | FULL | 1-4 (voting results not attached) |
| CRISIL-26 | credit-ratings/02-CRISIL.txt | BBB/Stable, A3+, 20-Apr-2026 | HTML | FULL | All sections |
| ICRA-26 | credit-ratings/01-ICRA-rationale.pdf | Upgrade to BBB (Stable)/A3+, 29-Jun-2026 | 9 | PART | 1-5 |
| ICRA-25 | credit-ratings/03-ICRA-rationale.pdf | BBB- reaffirmed, 24-Mar-2025 | 7 | SKIM | 1 |
| CARE-22 | credit-ratings/04-CARE.pdf | Withdrawn, 30-Aug-2022 | 4 | SKIM | 1 |
| MD | market-data-2026-10-30.md | screener.in, fetched 30-Oct-2026 | - | FULL | Market cap Rs 7,276 crore, price Rs 807, PE 100, ROCE, shareholding |

Housekeeping, SKIM: filings/20251114_3bd664d5 (DUP of Q2-26, see defects); 20260228_b7989c00
(physical share transfers); 20260905_7c09f19e (AR web-link letter); 20260905_a2cfccc3 (AGM notice,
DUP of AR26).

DUP sets (same md5 in the ledger): AR26 and filings/20260905_a2cfccc3; results/q-2025-09 and
filings/20251114_3bd664d5; the four 27-Aug-2026 files; the three 22-Sep-2026 files; the two
30-Jun-2026 files; the two 31-Dec-2025 files.

## Gaps (NOT FOUND, with where it was looked for)

- **Earnings call transcripts.** None on screener.in; none in the 54 BSE rows (30-Oct-2025 to
  30-Oct-2026). Management's words are limited to decks, the AR26 chairman's letter and MD&A.
  Would come from the company website or the exchange if a call is ever held.
- **Q2 FY27 results.** Not filed by 27-Oct-2026, the last BSE row. Due on BSE by mid-November 2026.
- **Q1 FY27 balance sheet and cash flow.** Not required for a first quarter; only segment assets
  and liabilities are filed (Q1-27 p.6).
- **Promoter pledge.** AR26 keyword search finds none; no SAST disclosure in the BSE windows.
- **Promoter holding change Jun to Sep 2026.** No SAST or PIT filing in the corpus explains the
  0.30 pp gap between the expected 71.40% and the reported 71.10%. Would come from the BSE
  shareholding pattern and insider-trading disclosures (dropped as housekeeping).
- **Status of 99,341 unconverted warrants** of 30,12,800. Not in AR26 pp.11-12 or the BSE list.
- **AGM 2026 voting results.** Filing 20260928_c7bc606e says they follow "in due course"; not in the list.
- **BIGTech audited accounts.** Not made available to the group auditor (AR26 p.220); not filed.
- **Customer concentration, capacity utilisation, product revenue split.** Not in AR26 (pp.52-61,
  264, 278-284) or the decks, beyond "~₹500+ cr" from Ai+ in Q1 FY27 (Deck-Aug p.7).
- **Financials.xlsx.** Absent this run.
