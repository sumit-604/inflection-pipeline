# SUDARCOLOR corpus manifest

Sudarshan Colorants India Ltd (formerly Heubach Colorants India Ltd, formerly Clariant Chemicals (India) Ltd).
NSE SUDARCOLOR, BSE 506390, ISIN INE492A01029. Promoter: Sudarshan Chemical Industries Ltd group, 70.25%
since the open offer closed on 03-Oct-2025 (AR26 p.21).
Ledger written 2026-10-29. Card: `screens/cards/SUDARCOLOR.md`.

Status key: FULL = read in full; PART = key sections read, rest navigated by keyword; SKIM =
housekeeping, checked for substance; DUP = byte-identical to another held file (md5 checked).
Page numbers are PDF page numbers. In AR26 the PDF page carries two printed pages (PDF p.21 =
printed pp.34-35).

## How it was built

- screener/: `tools/collector/screener_collect.py https://www.screener.in/company/SUDARCOLOR/ --output-dir
  screens/corpus/SUDARCOLOR/screener --no-drive` under `py -3.14`, 2026-10-29. Two annual reports
  (FY25, FY26) and Financials.xlsx. No transcripts or decks exist on screener.in.
- filings/: BSE announcements API (`AnnSubCategoryGetData/w`, strCat -1), called from a bseindia.com
  page in the in-app browser (scripted calls to NSE and BSE returned Access Denied on 2026-10-29).
  Windows of 12 months or less covering 14-Nov-2024 to 28-Oct-2026, 104 announcements listed
  (an orchestrator pagination error first dropped 08-Oct-2025 to 23-Mar-2026; 18 rows and their
  attachments were added on 2026-10-29). Housekeeping categories dropped (board-meeting
  intimations, newspaper publications, trading-window closures, Reg 74(5), investor complaints,
  shareholding patterns, Reg 7(3), Reg 40, record dates, large-corporate forms, secretarial
  compliance). 89 attachments downloaded from `xml-data/corpfiling/AttachLive/`, falling back to
  `AttachHis/`, with `curl -C -` and three retries. File name = filing date + BSE attachment name. Where several announcements of
  one date carried the same byte size, one attachment was downloaded and the ledger marks the others
  "held as" that file.
- credit-ratings/: `tools/collector/fetch_ratings.py` over the four CARE links on the screener.in page.
  All four are Clariant-era releases (2017 to 2019).
- market-data-2026-10-29.md: screener.in company page, a service record.
- Text: PyMuPDF; Tesseract OCR on pages with under 40 characters of native text, tagged `[OCR]`.

## Integrity check (2026-10-29)

All 77 PDFs of the first pass (2 screener, 4 credit-ratings, 71 filings) opened with PyMuPDF;
every page's text extracted; page markers match page counts; every file ends with `%%EOF`; 1
screener page carries `[OCR]`, plus the filing pages marked below. 4 md5 duplicate sets, listed in
`dup-sets-2026-10-29.json`. The 18 filings added in the second pass carry `.txt` beside each with
page markers matching and `%%EOF` present (orchestrator check). 95 PDFs in all.

One defect, found by the analyst and repaired by the orchestrator after the card was written:
`filings/20250716_47755654-fcb9-43cf-8328-9978d1295dba.pdf` ("Resignation of Chairman and
Non-executive Director") first arrived with a 0-page tree, the product of a download that was
interrupted and then resumed with `curl -C -` against a path that re-served the file from the start.
Re-fetched whole from `AttachHis/` on 2026-10-29 without resume: 12,021,738 bytes (matches the
exchange ledger), 25 pages, md5 identical to `filings/20250716_4bb6edb8` (DUP set 1), `.txt`
regenerated. No broken file remains. Lesson for the next run: never resume a BSE download; delete
and refetch. The `.txt` of `filings/20261028_2acad37c`
p.3 misreads three cells (Q1 FY27 PAT "20.38", total tax "8.88", H1 PAT "^449"); the page image
reads 20.36, 6.88 and 44.49, and the card uses the image.

## Substantive files, read

| Short name | Path | Period / date | Pages | Status | Pages read |
|---|---|---|---|---|---|
| AR26 | screener/Annual_Report_2026.pdf | FY26, AGM 18-Aug-2026 | 106 | PART | 9-10 (chairman, MD letters), 15-16 (board, officers), 17-20 (MD&A), 21-22, 24 (directors' report, acquisition, board changes, RPT policy), 29 (pay), 30-31 (secretarial audit), 39 (BRSR RPT share), 52, 60-61 (governance), 65-67 (shareholding, no rating), 68-71 (auditor, KAM, CARO), 76 (cash flow), 86-87 (shares held, payables, revenue note), 90 (contingent), 92-94 (RPT note 40, segment note 41), 96 (ratios), 97 (notes 48-54). DUP = filings/20260727_eb94ae02 and _a34e7e7b |
| AR25 | screener/Annual_Report_2025.pdf | FY25 | 106 | SKIM | 16 (FY24 and FY25 highlights, ratios), 56 (no rating). DUP = filings/20250905_b6f1019c, _ada6c512, _6cb5290d |
| Q2 res | filings/20261028_2acad37c-... | Q2 and H1 FY27, filed 28-Oct-2026 | 6 | FULL | 1-6 (outcome, review report, P&L, balance sheet, cash flow, notes incl. 15.89% inter se transfer). Period on p.1 and p.3 confirmed |
| Q1 res | filings/20260805_4507b81d-... | Q1 FY27, filed 05-Aug-2026 | 5 | FULL | 1-5 (P&L with Q4 FY26 and Q1 FY26 comparatives, notes, review report) |
| FY26 res | filings/20260511_ac39e071-... | Q4 and FY26 audited, filed 11-May-2026 | 13 [1 OCR] | PART | 1-4 (outcome, interim CFO, P&L with Q3 FY26 column, balance sheet) |
| Q3-26 | filings/20260203_ce326101-... | Q3 and 9M FY26, filed 03-Feb-2026, Rs lakh | 9 [1 OCR] | PART | 5 (P&L: revenue 17,567, exceptional (1,280), PAT (200)), 6-7 (notes: CIPL asset recovery, Handa, Mukhopadhyay, labour codes). Period on p.1 and p.5 confirmed |
| Q2-26 | filings/20251031_e933e238-... | Q2 and H1 FY26, filed 31-Oct-2025, Rs lakh | 11 [1 OCR] | PART | 3 (P&L: revenue 18,314, PAT 1,628, Q1 FY26 comparative), 4-5 (notes: fire exceptional Rs 49.87 lakh, MD re-appointment), 7 (cash flow headings). Period on p.1 and p.3 confirmed |
| Oct-25 | filings/20251031_1e77829d-...; _9dc33a77; _6b690d53; _addcb039 | Board outcome 31-Oct-2025: name change proposed, MD re-appointed to Nov-2030, Mukhopadhyay as NED, PwC internal auditor | 3 / 3 / 3 / 11 | FULL (first three) | 1-2 |
| Feb-26 | filings/20260203_084b852e-...; _dba83f43 | Board outcome 03-Feb-2026: Navandar appointed ID, Sahu CFO resignation noted | 9 / 9 | PART | 1-2 |
| Handa | filings/20251029_52c753af-...; _d8bf761f | Handa ID resignation 28-Oct-2025 "due to preoccupation", filed twice (different md5) | 4 / 3 | FULL | 1-4 |
| CFO | filings/20260310_7bb6238c-...; _0caf2e0a (identical md5); _49e27edc | Sahu CFO resignation effective 09-Mar-2026 after notice, filed three times | 3 / 3 / 2 | FULL | 1-2 |
| GST-22 | filings/20260203_497eb81b-... | Appeal against Rs 3.87 crore GST order of 29-Oct-2025 for FY22 | 2 | FULL | 1-2 |
| Delay | filings/20260210_e2c07643-... | Reason for late disclosure of the 29-Oct-2025 order, on BSE query | 1 | FULL | 1 |
| Name | filings/20251212_43b32f66-...; 20251208_32c9e858-... | Name change effective 12-Dec-2025 (ROC certificate); postal ballot results 06-Dec-2025, three resolutions passed | 2 / 13 | FULL / SKIM | 1-2 / resolution list |
| LoF | filings/20250902_a93e2bc8-... | Letter of Offer, 01-Sep-2025 | 94 | PART | 1, 21, 23-25 (offer terms, intentions: no delisting two years, restructuring and merger rights reserved). Manager's copy 20250902_92B543AF held, SKIM |
| Acq | filings/20250303_09fe17f9-... | Acquisition completed 03-Mar-2025 | 5 | FULL | 1-5 (consideration EUR 127.5 million plus EUR 29.44 million) |
| Jul-25 | filings/20250716_4bb6edb8-... | Board outcome 16-Jul-2025 | 25 | PART | 2-3 (items incl. chairman change), 24-25 (Kapoor resignation). DUPs: 454f9aa8, 72eb9d58, c592c4e1, 47755654 (repaired 2026-10-29, now byte-identical) |
| GST-S | filings/20260826_f0ea0d17-...; 20260901_49e046d8-... | GST search 25-Aug to 31-Aug-2026 | 2 / 2 | FULL | 1-2 each |
| GST-A | filings/20260912_4fa1bdd8-... | Appeal order, Rs 5.11 crore demand upheld | 2 | FULL | 1-2 |
| GST orders | filings/20260323_b0e7f3f1-...; 20260624_b205b5ff-... | DRC-07 orders Rs 0.62 crore and Rs 0.04 crore | 2 / 2 | FULL | 1-2 each |
| Vel | filings/20260901_067ca73a-... | Velankar resignation 01-Sep-2026 | 3 [1 OCR] | FULL | 1-3. DUP = 20260901_d7ab61c7 (held as) |
| SAST-10 | filings/20261005_7382F095-...; 20261021_C1DC7FB5-...; 20260818_C0699C58-... | Reg 10(5), 10(6), 10(7) inter se transfer of 15.89% | 4 / 36 / 16 [OCR] | PART | 1-2 of each |
| SAST-29 | filings/20251006_A284B883-...; 20251004_ABD66FAF-...; 20261005_6D1F3240, _A16C6814 | Reg 29(2) disclosures | 2-3 each | SKIM | Encumbrance line (blank) |
| Fine | filings/20250628_23785a30-... | Exchange fines for late FY25 results | 3 | FULL | 1-3 |
| Mgmt-24 | filings/20241114_b72244cd-...; 20241114_2ef87890-... | Q2 FY25 media release; MD appointment | 2 / 7 | SKIM | 1-2 |
| Prom-name | filings/20250620_8e685bac-... | Promoter entity renaming | 1 | FULL | 1 |
| Aud-LLP | filings/20260115_d4bb8d21-... | Statutory auditor firm converted to LLP, 13-Jan-2026 | 1 | FULL | 1 |
| Acq-upd | filings/20250220_218d5010-... | Anti-trust approvals received | 1 | FULL | 1 |
| IDC | filings/20250909_bb9a0730-... | IDC recommendation on the offer (newspaper scan) | 4 | SKIM | 1; pp.2-4 unreadable glyph text, not OCR-tagged |
| AGM-26 | filings/20260819_3dcd0bee-... | 69th AGM voting results | 13 [6 OCR] | SKIM | Resolution list: three ordinary items, all passed |
| AGM-25 | filings/20251001_b700ae77-... | 68th AGM voting results | 18 | SKIM | Resolution list: five ordinary items |
| PB-26 | filings/20260410_4da572f2-... | Postal ballot, Navandar appointment | 10 | SKIM | 1 |
| CARE-19 | credit-ratings/01-CARE.pdf | Withdrawal of AA+/Stable, 25-Jan-2019 | 4 | PART | 1 |
| CARE-17 | credit-ratings/04-CARE.pdf | AAA/Stable reaffirmed, 27-Jan-2017 | 4 | PART | 1 |
| MD | market-data-2026-10-29.md | screener.in, 28-Oct-2026 close | - | FULL | Market cap, price, shareholding, quarterly cross-check |

Held, SKIM or not opened beyond page 1: Q2 FY25 and Q3 FY25 results (Nov-2024, Jan-2025) and the
Jan-2025 media release; the DPS and draft letter of offer (Mar-2025, two copies, 85-86 pages); the
Apr and May 2025 Reg 30 director disclosures; the May-2025 board-meeting cancellation and delay
intimations; the Jun-2025 Reg 29(2); the Aug-2025 Q1 FY26 bundle (15 pages, five copies, held
as DUP set 2; Q1 FY26 figures taken from Q1 res comparatives); the Sep and Oct 2025 pre-offer and
post-offer advertisements and the Oct-2025 Reg 7(2) PIT disclosure; the Sep-2025 senior
management change; the Nov-2024 and Dec-2024 lost-certificate and RTA items; the Jan-2025 RTA
name change; the 2026 BRSR copy of AR26.

DUP sets (md5, `dup-sets-2026-10-29.json`): (1) four 16-Jul-2025 board-outcome copies; (2) five
11-Aug-2025 Q1 FY26 copies; (3) three 05-Sep-2025 copies and AR25; (4) two 27-Jul-2026 copies
and AR26. Among the second-pass files, 20260310_7bb6238c and _0caf2e0a are identical (md5
9f6f2a70...); the two 29-Oct-2025 Handa filings differ in bytes but not in substance.

## Gaps (NOT FOUND, with where it was looked for)

- **Concall transcripts and investor presentations.** None on screener.in; none in the 104 BSE
  announcements. Management's words are limited to the AR26 letters (pp.9-10) and MD&A.
- **Half-yearly related-party disclosures (Reg 23(9))** for H2 FY26 and H1 FY27. Not in the BSE list
  (likely dropped with housekeeping categories). The related-party share of H1 FY27 is NOT FOUND.
- **Installed capacity, production volumes, product-wise revenue.** Not in AR26 (looked: pp.9, 17-20,
  26, 67, BRSR pp.36-49) or any results filing. Segment note gives only pigments vs services.
- **Customer concentration.** Not in AR26 (CARO p.71 silent; BRSR p.39 gives dealer shares only).
- **Current credit rating.** None: AR26 p.67 and AR25 p.56 state no rating was sought. The four CARE
  files are Clariant-era (2017 to 2019) and stale.
- **Promoter pledge statement.** No explicit "nil pledge" line in AR26; the Reg 29(2) encumbrance
  field (SAST-29) is blank.
- **AZO product-transfer volumes and HP Azo localisation numbers.** Named in AR26 pp.9-10 without
  figures.
- **Any merger, delisting or product-transfer proposal.** None filed to 28-Oct-2026; the LoF (pp.24-25)
  carries the reserved rights only.
- **IDC recommendation text** on the open offer: the filed newspaper scan (filings/20250909_bb9a0730
  pp.2-4) extracted as glyph noise and was not OCR-tagged.
