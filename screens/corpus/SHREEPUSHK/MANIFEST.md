# SHREEPUSHK corpus manifest

Shree Pushkar Chemicals & Fertilisers Ltd. NSE SHREEPUSHK, BSE 539334, CIN L24100MH1993PLC071376.
Mumbai registered office; plants at MIDC Lote Parshuram (Ratnagiri), Deewanganj and Meghnagar (MP),
Hisar (Haryana). Quarterly reporter. Ledger written 2026-10-29. Card: `screens/cards/SHREEPUSHK.md`.

Status key: FULL = read in full; PART = key sections read, rest navigated by keyword; SKIM =
housekeeping, checked for substance; DUP = byte-identical to another held file (md5 checked).
Page numbers are PDF page numbers. In the annual report the printed page number is two lower than
the PDF page (AR26 PDF p.28 = printed p.26). In the transcripts the PDF page is one higher than the
printed "Page n of N" (cover letter is PDF p.1).

## How it was built

- screener/: `tools/collector/screener_collect.py https://www.screener.in/company/SHREEPUSHK/ --output-dir
  screens/corpus/SHREEPUSHK/screener --no-drive` under `py -3.14`, 2026-10-29: annual reports FY26 and
  FY25, four transcripts (Nov-2025, Feb-2026, May-2026, Aug-2026), the latest deck (Aug-2026), Financials.xlsx.
- filings/: BSE announcements API (`AnnSubCategoryGetData/w`, strCat -1), called from a bseindia.com page in
  the in-app browser because scripted calls to NSE and BSE returned Access Denied on 2026-10-29. One window,
  08-Nov-2025 to 01-Oct-2026 (44 announcements listed in `bse-announcements-2026-10-29.json`). Housekeeping
  categories dropped (board-meeting intimations, newspaper publications, trading-window closures, Reg 74(5),
  investor complaints, shareholding patterns, Reg 7(3), Reg 40, record dates, large-corporate forms,
  secretarial compliance). 35 attachments downloaded from `xml-data/corpfiling/AttachLive/`, falling back to
  `AttachHis/`, with `curl -C -` and three retries. Nine ledger rows with the same date and byte size as a held
  file were not downloaded again (the same PDF filed under a second category). File name = filing date +
  BSE attachment name.
- credit-ratings/: `tools/collector/fetch_ratings.py` found no rating link on the screener.in page; the folder
  does not exist.
- market-data-2026-10-29.md: screener.in company page, a service record (prices are the 28-Oct-2026 close).
- Text: PyMuPDF; Tesseract OCR on pages with under 40 characters of native text, tagged `[OCR]`.

## Integrity check (2026-10-29)

All 42 PDFs (7 screener, 35 filings) opened with PyMuPDF. Every page's text was extracted, page markers in
each `.txt` match the PDF page count, and every file ends with `%%EOF`. 6 md5 duplicate sets, listed in
`dup-sets-2026-10-29.json`. **No broken file.** One page carries `[OCR]` (filings/20260812_74df4b98, p.4,
the director's resignation letter). The results statements of 08-Nov-2025, 11-Feb-2026, 18-May-2026 and
12-Aug-2026 are scanned images with native text of uneven quality; the consolidated P&L, balance sheet and
cash flow pages used on the card were read from the PDF page image as well as the `.txt`.

## Substantive files, read

| Short name | Path | Period / date | Pages | Status | Pages read |
|---|---|---|---|---|---|
| AR26 | screener/Annual_Report_2026.pdf | FY26, AGM 28-Sep-2026 | 267 | PART | 6-8 (CMD letter, profiles), 27-29 (Board's report: results, verticals, exports, dividend, warrants), 32-33 (RPT, subsidiaries), 54 (pay ratio), 70-71 (MD&A: industry, NBS, verticals, outlook, risks), 75 (related directors), 88-89 (shareholding, credit rating, RPT), 91 (warrant use), 98 (exports 8.28%), 133-134 (KAM), 136, 140 (CARO), 164 (CWIP, charge), 188-189 (contingent, guarantees, segment), 194 (RPT detail), 198-199 (standalone ratios), 253-254 (consolidated contingent, segment), 258, 262 (subsidiary shares), 264 (consolidated ratios). DUP = filings/20260904_1a61cea4 |
| AR25 | screener/Annual_Report_2025.pdf | FY25 | 276 | SKIM | 1 (identity). FY25 figures taken from FY26 comparatives |
| Q1 res | filings/20260812_f176e61b-... | Q1 FY27, board outcome of 12-Aug-2026 | 17 | FULL | 1-17 (outcome, director change, auditor change, review reports, consolidated and standalone results, annexures). p.6 read from the page image |
| Aug-26 PR | filings/20260812_6ce3fa7a-... | Q1 FY27 press release | 5 | FULL | 2-5 |
| Aug-26 deck | filings/20260812_97fb4e8b-... | Q1 FY27 presentation | 26 | FULL | 2-17 read; 18-26 (ESG, safe harbour) skimmed. DUP = screener/Investor_Presentation_1.pdf |
| Aug-26 call | screener/Concall_Aug_2026_Transcript.pdf | Call of 13-Aug-2026 | 14 | FULL | 2-14. DUP = filings/20260818_be92392e |
| May-26 call | screener/Concall_May_2026_Transcript.pdf | Call of 19-May-2026 | 13 | FULL | 2-13. DUP = filings/20260525_7f090ce6 |
| Feb-26 call | screener/Concall_Feb_2026_Transcript.pdf | Call of 12-Feb-2026 | 17 | PART | 5-7, 10-17 (margins, Unit 5/6, China, guidance, utilisation, capex, FY29). DUP = filings/20260217_2a12a024 |
| Nov-25 call | screener/Concall_Nov_2025_Transcript.pdf | Call of 10-Nov-2025 | 17 | PART | 5-8, 10-13, 15-16 (delays, guidance, Unit 8, utilisation, promoter, Dyecol). DUP = filings/20251114_a50e9cbb |
| FY26 res | filings/20260518_94e67120-... | Q4 and FY26 audited, 18-May-2026 | 16 | FULL | 1-16; pp.7-9 (consolidated P&L, balance sheet, cash flow) read from the page image |
| May-26 deck | filings/20260518_ad75ba93-... | Q4 and FY26 presentation | 31 | PART | 2-18 (highlights, segments, debt, balance sheet, cash flow, capex table) |
| May-26 PR | filings/20260518_c7795c8a-... | Q4 and FY26 press release | 5 | FULL | 2-3 |
| Feb-26 PR | filings/20260211_b19d982c-... | Q3 FY26 press release | 5 | FULL | 2-3 |
| Q3 res | filings/20260211_b460fc9d-... | Q3 and 9M FY26, 11-Feb-2026 | 6 | SKIM | 1 (period check); figures taken from Feb-26 PR and FY26 res comparatives |
| Q3 deck | filings/20260211_4ecb4508-... | Q3 FY26 presentation | 28 | SKIM | 1 (identity) |
| Nov-25 PR | filings/20251108_7917aa0b-... | Q2 and H1 FY26 press release | 5 | FULL | 2-3 |
| Q2 res | filings/20251108_5ca6919e-... | Q2 and H1 FY26 with warrant approval, 08-Nov-2025 | 13 | SKIM | 1 (period check); figures taken from Nov-25 PR |
| Q2 deck | filings/20251108_8e0eb58a-... | Q2 FY26 presentation | 26 | SKIM | 1 (identity) |
| EGM | filings/20251115_6b0cd9a8-... | EGM notice, warrants to promoter | 23 | PART | 16-17 (objects, utilisation), 20, 22-23 (pre/post holding, allottee) |
| EGM result | filings/20251211_cae1f5ae-... | Voting results, 10-Dec-2025 | 12 | SKIM | 1 |
| Warrants | filings/20251227_93d9a1ee-... | Allotment of 7,36,196 warrants | 2 | FULL | 1-2 |
| CS cert | filings/20251219_de428ce0-... | Certificate on use of proceeds | 1 | FULL | 1 |
| Bangladesh | filings/20251124_80f4d7c7-... | Dyecol Bangladesh incorporation | 3 | FULL | 1-2 |
| Reg 32 | filings/20260211_b161fa71, 20260518_de1bd16e, 20260812_5a615136 | Deviation statements, three quarters | 4 each | PART | Aug-2026 copy pp.2-3 |
| Rating | filings/20260727_89095fe6-... | ICRA A+/Stable, A1 reaffirmed | 1 | FULL | 1 |
| Solar | filings/20260817_d805addf-... | 10 MW Nanded commissioned | 1 | FULL | 1 |
| U5 | filings/20260910_273e32bf-... | Unit 5 dyes commercial production | 1 | FULL | 1 |
| NCLT | filings/20261001_2e28d306-... | Scheme withdrawal order | 2 | FULL | 1-2 |
| Director | filings/20260812_74df4b98-... | Nayak resignation (p.4 [OCR]) | 6 | SKIM | 1, 4 |
| Auditor | filings/20260812_b5b08f0f-... | JASS & Co appointment | 6 | SKIM | 1 |
| Int. auditor | filings/20260518_cc260968-... | Internal auditor re-appointment | 2 | FULL | 1-2 |
| AGM letter | filings/20260904_90c4e907-... | Letter to members, AGM web link | 3 | FULL | 1-3 |
| BRSR | filings/20260904_73080768-... | BRSR FY26 | 37 | SKIM | 1 |
| Audio | filings/20260813_9f868809-... | Audio recording intimation | 1 | SKIM | 1 |
| MD | market-data-2026-10-29.md | screener.in service record | | FULL | market cap, price, shareholding, PE basis |

Held, SKIM or not opened beyond page 1: the Q2 and Q3 FY26 results statements and decks (figures taken
from the press releases and the FY26 audited comparatives), the BRSR, the voting-result filing, the
audio-recording intimation, Financials.xlsx (never cited).

DUP sets (md5): 6 pairs, all screener-to-filings copies of the same document (four transcripts, the
Aug-2026 deck, the FY26 annual report). Listed in `dup-sets-2026-10-29.json`.

## Gaps (NOT FOUND, with where it was looked for)

- **Q2 FY27 result (quarter to 30-Sep-2026).** Not in the BSE ledger to 01-Oct-2026; the last result filed is
  Q1 FY27 on 12-Aug-2026. Due by 14-Nov-2026. Steps 5, 8 and 13 run on Q1 FY27.
- **Unit 6 commercial-production intimation.** No Reg 30 filing in the ledger after the Unit 5 filing of
  10-Sep-2026. Looked in all 35 filings and the ledger headlines.
- **Credit-rating rationale.** credit-ratings/ absent; screener.in lists no rating link (MD); the 27-Jul-2026
  filing is a one-page intimation; AR26 p.89 repeats the grades only. Step 10 carries the grade, not the view.
- **Segment profit.** AR26 Note 45 (p.254) and every results statement report one segment. Revenue and
  volume by segment come from the press releases; profit by entity from AR26 pp.33, 262 and FY26 res p.13.
- **Promoter pledge.** No encumbrance line in the AR26 shareholding table (p.88); no SAST or pledge filing in
  the ledger.
- **Chemicals revenue split** between acids, intermediates and Dyecol dyes. AR26 p.28 gives one chemicals
  line; no deck or call gives the split.
- **Q1 FY27 balance sheet.** Quarterly results carry no balance sheet; leverage and working capital are at
  31-Mar-2026.
- **Third-party evidence on China's VAT-refund removal** and Indian H-acid exports. Management claim only
  (Feb-26 call, pp.7, 17).
