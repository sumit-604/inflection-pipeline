# DCMSRIND corpus manifest

DCM Shriram Industries Ltd. NSE DCMSRIND, BSE 523369, ISIN INE843D01027 (AR26 p.69).
Post-scheme entity: Daurala Sugar Works only (sugar, distillery, co-generation, Meerut UP). Chemical
undertaking demerged to DCM Shriram Fine Chemicals Ltd and Rayon undertaking (with Engineering Projects)
to DCM Shriram International Ltd; Lily Commercial Pvt Ltd (promoter holding company, 50.11%) amalgamated
in. NCLT order 21-Nov-2025, effective 17-Dec-2025, appointed date 01-Apr-2023, record date 26-Dec-2025.
Promoter group 50.11% held directly by family members and Akshay Foundation (AR26 p.121).
Ledger written 2026-10-30. Card: `screens/cards/DCMSRIND.md`.

Status key: FULL = read in full; PART = key sections read, rest navigated by keyword; SKIM =
housekeeping, checked for substance; DUP = same content as another held file.
Page numbers are PDF page numbers. In AR26 the printed page number is the PDF page minus 3.

## How it was built

- screener/: the two annual reports are BSE attachments, not screener.in downloads. The ledger shows
  `screener/Annual_Report_2026.pdf` from `bseindia.com/xml-data/corpfiling/AttachHis/b48b8d20-...pdf`
  (the 18-Jun-2026 Reg 34(1) filing) and `screener/Annual_Report_2025.pdf` from
  `AttachHis/b49187ed-...pdf`, both fetched 2026-10-30 09:39. No transcripts or decks are held.
- results/: three screener.in public-page quarter links (`screener.in/company/source/quarter/774/<m>/<y>/`),
  each redirected to a BSE `AttachHis/` PDF: Q4 FY25 (16 pp), Q1 FY26 (10 pp), Q2 FY26 (12 pp,
  the 05-Nov-2025 filing). Periods checked on page 1. All three are pre-scheme (sugar, chemicals and
  rayon combined) and are superseded by the restated comparatives in later filings.
- filings/: BSE announcements listed through the bseindia.com corporate-announcements form in the
  in-app browser (windows 30-Oct-2025 to 30-Oct-2026: 82 rows, then 30-Oct-2025 to 23-Mar-2026: 35 rows;
  list in `work/bse/DCMSRIND.txt`). Housekeeping dropped, plus 15 SAST Reg 10(5), 10(6) and 29(2)
  promoter disclosures (post-scheme inter se) and IEPF items. 22 attachments downloaded from
  `xml-data/corpfiling/AttachHis/`, fetched 2026-10-30 09:52-09:53. File name = filing date + first 8
  characters of the BSE attachment name. The 18-Jun-2026 AR and 05-Nov-2025 Q2 FY26 rows are held
  under screener/ and results/ respectively.
- credit-ratings/: `tools/collector/fetch_ratings.py` over four CARE links on the screener.in page
  (careratings.com PDFs, 23-Aug-2023 to 09-Apr-2026). No ICRA file, so the ShowRationalReportFilePdfViewer
  path was not used.
- prospectus/: none (not a recent IPO).
- market-data-2026-10-30.md: screener.in public company page (consolidated view), fetched 2026-10-30
  about 09:00 IST, a service record.
- Financials.xlsx: absent (screener collector browser could not start this run).
- Text: PyMuPDF; Tesseract OCR on low-text pages, tagged `[OCR]`.

## Integrity check (2026-10-30, from the fetch ledger)

All 27 PDFs in the ledger carry status OK; every byte size matches the declared size where one is
declared (20251209_067d1fa8 has no declared size). Pages: AR26 148, AR25 230, results 16/10/12,
filings 1 to 37. OCR pages: AR26 1 (p.148), AR25 1, filings/20251223_26c93560 1 (p.4). The four
CARE PDFs are not in the fetch ledger; they are recorded in `credit-ratings/manifest.json` with HTTP 200
and byte sizes. `dup-sets-2026-10-30.json` is empty (no md5 duplicates).

Defects found by the analyst:
- **Garbled native text layers with no `[OCR]` tag** on every results table: FY26 res pp.5-11, Q3-26
  p.4, Q1 res pp.4 and 7, and most of the NCLT order (37 pp, scanned with a poor text layer). The card's
  result figures were read from the page images (FY26 res pp.7, 10, 11; Q3-26 pp.4-5; Q1 res p.4;
  AR26 p.121 promoter table, rendered at 220 dpi).
- **market-data-2026-10-30.md is stale on P/E (9.03) and book value (Rs 105).** These do not reconcile
  with the filed sugar-only entity (net worth Rs 364.78 crore over 8.70 crore shares = Rs 41.9 a share;
  trailing four-quarter PAT Rs 32.47 crore gives about 16.9x). Market cap Rs 550 crore and price
  Rs 63.3 reconcile with the share count. Only those two fields are used.
- **AR25 is the full pre-scheme report** (standalone and consolidated, all three segments). It is used
  only for the FY25 segment split (p.118).

## Substantive files, read

| Short name | Path | Period / date | Pages | Status | Pages read |
|---|---|---|---|---|---|
| AR26 | screener/Annual_Report_2026.pdf | FY26, post-scheme, board report 20-May-2026 | 148 [1 OCR] | PART | 28 (managerial pay terms), 29-31 (scheme, financial summary, dividend, sugar operations, subsidiaries), 32-34 (board changes, MD pay), 36 (RPT power and steam to DSFCL), 52-53 (pay ratios), 55-56 (board), 68-70 (shareholding, ratings), 76-80 (MD&A, SWOT, ratios, employees), 81-82 (auditor, KAM), 121 (share capital, promoter table, image), 132 (contingent liabilities), 137 (RPT note 42), 144 (note 49 GST), 147 (note 54 Lily) |
| AR25 | screener/Annual_Report_2025.pdf | FY25, pre-scheme | 230 [1 OCR] | SKIM | 1 (cover letter), 118 (segment revenue and results FY24-FY25) |
| FY26 res | filings/20260520_080532f7-... | Q4 and FY26 audited, filed 20-May-2026, Rs lakh | 13 | FULL | 1-13; tables pp.7, 10, 11 from the page image; EoM p.2; restatement p.9; segment and notes p.8 |
| Board-26 | filings/20260520_292f3c26-... | Board outcome 20-May-2026: results, dividend Re 0.40, Rastogi as Director and COO, CFO reappointed | 17 | SKIM | 1-5; pp.6-17 repeat FY26 res |
| Q1 res | filings/20260813_cfb62e99-... | Q1 FY27, filed 13-Aug-2026, Rs lakh | 7 | FULL | 1-7; table p.4 from image; notes p.5 (pre-scheme Q1 FY26 PAT Rs 17.79 crore, modified tax returns) |
| Q3-26 | filings/20260214_0cc46a6b-... | Q3 and 9M FY26, filed 14-Feb-2026, first post-scheme result | 9 | PART | 2-5 (review report, table p.4 and restatement p.5 from image), 6 (notes) |
| NCLT | filings/20251205_c1002190-... | Certified NCLT order 21-Nov-2025, received 05-Dec-2025 | 37 | PART | 1-8 (parties, scheme rationale), 12-14 (meeting results: 99.9999% of shares voting in favour; creditors 100%), 16-22 (RD and OL observations, replies), 33-35 (order terms) |
| Sanction | filings/20251121_266b2bc7-... | NCLT order pronounced 21-Nov-2025 | 1 | FULL | 1 |
| Rec | filings/20251210_41ee2be9-... | Shareholder letter, record date | 3 | FULL | 1-3 (states record date 19-Dec-2025 and "demerger of the Sugar business undertaking"; both contradicted later) |
| Eff | filings/20260116_57c2fb4c-... | Effective date 17-Dec-2025, allotment and credit of DSFCL and DSIL shares | 1 | FULL | 1 |
| CoA | filings/20260203_a9cf20a7-... | Cost-of-acquisition split 42.66 / 25.22 / 32.12 | 3 | FULL | 1-3 |
| Board-23 | filings/20251223_8eaadfc3-... | Alok Shriram and Urvashi Tilakdhar resign; Uday and Rohan Shriram inducted; MD redesignated MD and CEO | 8 | PART | 1-4 |
| ID-res | filings/20251223_26c93560-... | Behara and Khaitan resign as IDs | 5 [1 OCR] | PART | 1-4 |
| ID-app | filings/20251209_067d1fa8-... | Surana and Prasad appointed IDs from 10-Dec-2025 | 5 | FULL | 1-5 |
| PB | filings/20260121_aeb655b3-...; 20260121_6f4b0e6f-... | Postal ballot notice (two versions, one with cover letter) | 22 / 20 | SKIM | Resolution list: two IDs, Uday and Rohan Shriram appointments |
| Rate | filings/20260402_fc3c5d12-...; 20260407_7c0081d3-... | CARE downgrade to A- / A2+ (01-Apr-2026); re-filed with CARE letters after BSE discrepancy notice | 1 / 9 | FULL / SKIM | 1 / 1 |
| ITR | filings/20260720_b3112f99-... | Income tax refund Rs 16.59 crore incl. interest, FY2018 | 1 | FULL | 1 |
| AGM-26 | filings/20260715_c8f6a565-... | AGM outcome 15-Jul-2026 | 4 | SKIM | 3 (business list) |
| RO | filings/20260922_a5424b42-... | Registered office move within New Delhi from 01-Oct-2026 | 1 | FULL | 1 |
| Surv-1 | filings/20261006_b319db67-... | Reply to exchange volume query | 1 | FULL | 1 |
| Surv-2 | filings/20261023_6d532e2d-... | Reply to exchange price query | 1 | FULL | 1 |
| CARE-26 | credit-ratings/01-CARE.pdf | 09-Apr-2026, post-scheme | 7 | FULL | 1-4 (pp.5-7 annexures skimmed) |
| CARE-25 | credit-ratings/02-CARE.pdf | 06-Oct-2025, rating watch negative, pre-scheme | 7 | PART | 1 |
| Q2-26 pre | results/q-2025-09.pdf | Q2 and H1 FY26 pre-scheme, filed 05-Nov-2025 | 12 | SKIM | 1 (period). Superseded by restated Q2 FY26 in Q3-26 p.4 |
| MD | market-data-2026-10-30.md | screener.in, fetched 30-Oct-2026 | - | FULL | Market cap, price, 52-week range, shareholding |

Held, SKIM or not opened beyond page 1: results/q-2025-03.pdf (Q4 FY25 pre-scheme, standalone and
consolidated) and results/q-2025-06.pdf (Q1 FY26 pre-scheme); credit-ratings/03-CARE (07-Aug-2024) and
04-CARE (23-Aug-2023), pre-scheme.

## Gaps (NOT FOUND, with where it was looked for)

- **Concall transcripts and investor presentations.** None on screener.in; none in the BSE list for the
  12 months. Management's words are limited to the AR26 directors' report and MD&A (pp.29-36, 76-80).
- **Q2 FY27 results.** Not filed by 30-Oct-2026 (BSE list ends 23-Oct-2026). Would come from BSE
  announcements, due by 14-Nov-2026.
- **Promoter pledge status after the scheme.** Not in AR26 (pp.69, 121) or results. The 15 SAST
  Reg 10(5), 10(6) and 29(2) filings were dropped at listing as housekeeping; they are on BSE.
- **Postal ballot result (Jan-2026)** for the ID and Uday and Rohan Shriram appointments. Not in the
  downloaded set; AR26 p.33 states approval. Would come from BSE announcements, Feb-2026.
- **The scheme document** (Annexure 1 to the NCLT petition). Only quoted in NCLT pp.6-7, 18-19. Would come
  from the BSE scheme filings of Nov-2023 to 2024 or the company website.
- **Identity of the GST indemnifier** behind the Rs 371.11 crore provision and reimbursement asset.
  AR26 p.144 and KAM pp.81-82 say "a party" or "such customer" only.
- **Product-line revenue after the scheme** (sugar, distillery, power). Single segment reported (FY26 res
  p.8); only CARE's FY25 split (CARE-26 p.2) exists.
- **Cause of the Q1 FY27 margin drop and the source of Rs 6.17 crore other income.** No note in Q1 res.
- **Restated quarterly FY25 figures** beyond the comparatives in Q3-26 and FY26 res. Would come from
  the company's restated filings, if any.
- **Size of the retrospective UPPCL tariff gain in FY26** (CARE-26 p.2 names it without a number).
- **Reg 23(9) related-party disclosures** for H2 FY26 and H1 FY27. Not in the BSE list (likely dropped
  with housekeeping).
