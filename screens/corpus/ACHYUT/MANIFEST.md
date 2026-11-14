# ACHYUT corpus manifest

Achyut Healthcare Ltd. BSE 543499, scrip ID ACHYUT, ISIN INE0K1401020. No NSE listing.
Listed on BSE SME on 30-Mar-2022; trading on the BSE Main Board from 02-Jan-2026 (AR26 p.21).
Ledger written 2026-10-27. Card: `screens/cards/ACHYUT.md`.

Status key: FULL = read in full; PART = key sections read, rest navigated by keyword; SKIM =
housekeeping, checked for substance; DUP = byte-identical to another held file (md5 checked).
Page numbers are PDF page numbers. In the annual reports the printed page number is one lower
than the PDF page (AR26 PDF p.21 = printed p.20).

## How it was built

- screener/: `screener_collect.py https://www.screener.in/company/543499/ --output-dir ... --no-drive`
  under `py -3.14`. Two annual reports and Financials.xlsx. No transcripts or decks exist on screener.in.
- filings/: BSE announcements API (`AnnSubCategoryGetData/w`, strCat -1), called from a
  bseindia.com page in the in-app browser (scripted calls return Access Denied), five windows of
  12 months or less from 01-Mar-2022 to 27-Oct-2026: 313 announcements listed. Housekeeping
  categories dropped (Reg 74(5), trading window, newspaper ads, shareholding patterns, investor
  complaints, Reg 7(3), Reg 40(10), board-meeting intimations, large-corporate forms). 221
  attachments downloaded from `xml-data/corpfiling/AttachLive/`, falling back to `AttachHis/`.
  File name = filing date + BSE attachment name.
- filings/zenith-530665/: the transferee's own scheme filing (Zenith Healthcare Ltd, BSE 530665),
  from Zenith's BSE announcement list (Jun to Oct 2026).
- prospectus/: SME IPO prospectus dated 14-Mar-2022, from the BSE link on screener.in.
- market-data-2026-10-27.md: screener.in company page, a service record.
- Text: PyMuPDF, Tesseract OCR on near-empty pages, tagged `[OCR]`.

## Integrity check (2026-10-27)

All 225 PDFs (2 screener, 221 filings, 1 Zenith, 1 prospectus) opened with PyMuPDF. Every page's
text was extracted, page markers in each `.txt` match the PDF page count, and every file carries
`%%EOF` in its last 2 KB. Downloads used `curl -C -` with three retries. **No broken file.** No
file name carries a byte count to check against.

## Substantive files, read

| Short name | Path | Period / date | Pages | Status | Pages read |
|---|---|---|---|---|---|
| AR26 | screener/Annual_Report_2026.pdf | FY26, AGM notice dated 05-Sep-2026 | 111 | PART | 20-25 (Board's report, scheme, board), 31, 46-47 (ratings, penalty, governance), 56-60 (scheme annexure, fund use, AOC-2), 68 (MD&A), 69-73 (auditor, CARO), 94 (CWIP), 98-99 (shareholders), 101-103 (P&L notes, RPT), 108, 110 (ratios). DUP = filings/20260905_37645931 |
| AR25 | screener/Annual_Report_2025.pdf | FY25 | 66 | SKIM | 18-19 (Board's report, plant date). DUP = filings/20250903_55e09964 |
| AR24 | filings/20240902_c189960d-... | FY24 | 60 | SKIM | 15 (plant date, preferential issue) |
| AR23 | filings/20230829_51ede0d8-... | FY23 | 54 | SKIM | 15, 42, 49 (results, export split) |
| Q2 res | filings/20261026_aa0adb1a-... | Q2 and H1 FY27, filed 26-Oct-2026 | 7 | FULL | 1-7 (P&L, balance sheet, cash flow, review report [OCR], Reg 32 statement). DUP = 20261026_493410cc |
| Q1 res | filings/20260813_b0ccfbf5-... | Q1 FY27 | 3 | SKIM | Q1 figures taken from Q2 res comparatives. DUP = 20260813_53fe2596 |
| FY26 res | filings/20260527_8bc2e2a8-... and _683a8aaf-... | FY26 audited | 10 / 9 | SKIM | FY26 figures taken from AR26 |
| Q3 res | filings/20260121_318098e9-... | Q3 FY26 + preferential issue + office change | 10 | SKIM | Combined filing; four DUP copies under other 20260121 names |
| EGM | filings/20260205_f33fcf7d-... | EGM notice for preferential issue, 21-Jan-2026 | 40 | PART | 5-6 (allottee table), 25-26 (pricing, VWAP) |
| Scheme | filings/20260715_2090ee9d-... | Revised outcome, scheme of amalgamation into Zenith | 7 | FULL | 1-6. Original 20260714_09402a77 (DUPs 9625aca6, 9e6124c2) |
| Zenith scheme | filings/zenith-530665/20260714_ZENITH_d9ce30bf-... | Zenith's own filing | 7 | SKIM | Same disclosure; no valuation report enclosed |
| SAST | filings/20260324_E8081FFC_... and 47 other Reg 29(2) files | Jun-2025 to Mar-2026 | 3-6 each [OCR] | SKIM | Filer, mode (gift, open market, preferential) and encumbrance line |
| Mgmt | filings/20260930_33bae4a2, _bde50900, _86f47236; 20260905_01b978d3 | MD and two IDs re-appointed | 2-3 each | FULL | |
| Listing | filings/20260507_d215ae4e-...; 20260101_8ce5bfb9-... | Pref listing approval; main-board migration approval | 2-3 | FULL / SKIM | |
| CS | filings/20250417_1b51c826-... | CS resignation, migration approval | 3 | FULL | |
| Prosp | prospectus/Prospectus_2022-03-14.pdf | SME IPO, Rs 360 lakh at Rs 20 | 276 | PART | 1-2, 9, 19 (business summary), 68 (objects). 14 pages [OCR] |

Held, SKIM or not opened beyond page 1: results and board outcomes FY22 to FY25, Reg 32
deviation statements (each period), AGM and EGM notices, outcomes and scrutiniser reports,
bonus and split corporate actions (Oct to Dec 2024), Nov-2023 preferential issue and RPT
filings, internal and secretarial auditor appointments, Reg 23(9) RPT disclosures.

DUP sets (md5): 37 duplicate pairs across filings; the ones that matter are noted in the table
above. Board outcomes are routinely filed two or three times under different attachment names.

## Gaps (NOT FOUND, with where it was looked for)

- **Credit rating.** None exists. AR26 p.46 states credit ratings "Not Applicable"; screener.in
  shows no ratings block; no rating filing in 313 BSE announcements. Step 10 is NOT FOUND.
- **Concall transcripts and investor presentations.** None on screener.in or in the BSE list.
- **Share-exchange valuation report and fairness opinion** for the Zenith scheme (both dated
  14-Jul-2026). Not enclosed in Achyut's or Zenith's BSE filings. Not held.
- **Zenith Healthcare's own financials and annual report.** Out of scope for this screen; only the
  summary figures in the scheme filing are held.
- **BSE observation letter / NCLT status** for the scheme. Not in the BSE list to 27-Oct-2026.
- **Plant commissioning evidence.** No filing reports commercial production at Bhat.
- **Customer concentration and the counterparty for FY26 commission expense.** Not disclosed in AR26.
