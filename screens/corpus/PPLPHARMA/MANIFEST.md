# PPLPHARMA corpus manifest

Piramal Pharma Ltd. NSE PPLPHARMA, BSE 543635. Demerged from Piramal Enterprises and listed in 2022 (AR26 p.105).
Ledger written 2026-10-29. Card: `screens/cards/PPLPHARMA.md`.

Status key: FULL = read in full; PART = key sections read, rest navigated by keyword; SKIM =
housekeeping, checked for substance; DUP = byte-identical to another held file (md5 checked).
Page numbers are PDF page numbers. In the annual reports two printed pages share one PDF page
(AR26 PDF p.37 = printed pp.68-69).

## How it was built

- screener/: `screener_collect.py https://www.screener.in/company/PPLPHARMA/ --output-dir ... --no-drive`
  under `py -3.14`, 2026-10-29. Two annual reports, one transcript (Jul-2026), the latest deck
  (Q2 FY27, a duplicate of the BSE filing), Financials.xlsx (never cited).
- filings/: BSE announcements API (`AnnSubCategoryGetData/w`, strCat -1), called from a
  bseindia.com page in the in-app browser because scripted calls to NSE and BSE returned Access
  Denied on 2026-10-29. One window, 29-Oct-2025 to 28-Oct-2026; the ledger's first dated item is
  05-Nov-2025 and the last 27-Oct-2026. Housekeeping categories dropped (board-meeting
  intimations, newspaper publications, trading-window closures, Reg 74(5), investor complaints,
  shareholding patterns, Reg 7(3), Reg 40, ESOP allotments, record dates, large-corporate forms,
  secretarial compliance). 77 attachments downloaded from `xml-data/corpfiling/AttachLive/`,
  falling back to `AttachHis/`, with `curl -C -` and three retries. File name = filing date +
  BSE attachment name. Where two announcements shared one attachment (board outcome plus
  results, press release plus deck) both names were kept; they are DUP pairs.
- credit-ratings/: `fetch_ratings.py` over the agency links on the screener.in page: four CARE
  PDFs (Jul-2024, Mar-2025, Jul-2025, Jul-2026) and two ICRA HTML captures (Oct-2024, Oct-2025).
- market-data-2026-10-29.md: screener.in company page, a service record, cited as MD only for
  market cap, price and the shareholding cross-check.
- Text: PyMuPDF; Tesseract OCR on pages with under 40 characters of native text, tagged `[OCR]`.

## Integrity check (2026-10-29, run by the orchestrator)

All 85 PDFs (4 screener, 4 credit-ratings, 77 filings) opened with PyMuPDF; every page's text
extracted; page markers in each `.txt` match the PDF page count; every file ends with `%%EOF` in
its last 2 KB; 41 filing pages and 4 screener pages carry `[OCR]`. 13 md5 duplicate sets, listed in
`dup-sets-2026-10-29.json`. **No broken file.**

## Substantive files, read

| Short name | Path | Period / date | Pages | Status | Pages read |
|---|---|---|---|---|---|
| Q2 res | filings/20261027_a6725b04-... | Q2 and H1 FY27 results, filed 27-Oct-2026 | 15 | FULL | 1-15: standalone and consolidated P&L, balance sheets, cash flows, notes (Yapan, exceptional items, one segment), review reports with Other Matters (11 and 10 subsidiaries), entity annexure. DUP = 20261027_8e54447f (board outcome) |
| Q2 deck | filings/20261027_7a320fcd-... | Q2 FY27 press release and deck, 27-Oct-2026 | 24 | FULL | 2-5 press release (segment table, P&L, balance sheet, FY27 outlook, call date); 9-22 deck (outlook, CDMO metrics, CHG, PCH, Bayer exit, AbbVie JV, balance sheet). DUP = 20261027_da812bf2 and screener/Investor_Presentation_1.pdf |
| Q1 deck | filings/20260729_5efe2042-... | Q1 FY27 press release and deck, 29-Jul-2026 | 20 | FULL | 2-5 press release (P&L, segments); 9-16 deck. DUP = 20260729_b3b6433d |
| Q1 res | filings/20260729_8dfa758e-... | Q1 FY27 results | 10 | SKIM | Q1 figures taken from Q2 res comparatives. DUP = 20260729_ff51bd4d |
| FY26 deck | filings/20260428_a2cef5d4-... | Q4 and FY26 press release and deck, 28-Apr-2026 | 39 | FULL | 2-5 press release; 8-37 deck (segment history FY23-FY26, geography, destocking, CDMO pipeline and customer mix, ADC, US expansion, CHG product mix, PCH, quarterly table p.36, balance sheet p.37). DUP = 20260428_6af1c917 |
| FY26 res | filings/20260428_21f4e662-... | FY26 audited results plus board outcome, CS and director changes | 27 | PART | Impairment and Labour Code notes (lines on the exceptional items); audit report wording checked for qualifications (none). DUP = six other 20260428 names |
| Jul-26 call | screener/Concall_Jul_2026_Transcript.pdf | Q1 FY27 call, 30-Jul-2026 (title page misprints "Q1 FY '26") | 19 | FULL | 1-19 |
| AR26 | screener/Annual_Report_2026.pdf | FY26, AGM notice dated 05-Jun-2026 | 182 | PART | 10-15 (board, highlights, leadership letter), 30 (CDMO MD&A), 36-38 (PCH, financial review, quality), 44-47 (governance, board changes), 51 (shareholding pattern), 55-57 (remuneration, auditors, CSR), 128-130 (consolidated audit report, KAM, Other Matters, CARO para), 149 (revenue, contract liabilities, contingent liabilities), 151-152 (exceptional items, associates), 157-158 (RPT, KMP pay, security, EPS, debt, capital management), 161 (tax, hedging, geography, customer over 10%), 168 (MSME, note 65, Kenalog subsequent event), 172 and 178-179 (AGM notice items 9-10, CA Alchemy 17.95%, Schedule V). DUP = 20260703_8a3aabd8 and 20260703_b63fb394 |
| AR25 | screener/Annual_Report_2025.pdf | FY25 | 166 | PART | 5, 13-14 (FY25 highlights, FY30 vision), 29, 33, 37 (segment FY30 aspirations), 38 (financial review FY25 vs FY24) |
| CARE | credit-ratings/01-CARE.pdf | Rating reaffirmed 17-Jul-2026 | 12 | FULL | 1-8 (rationale, sensitivities, strengths, weaknesses, liquidity, financials, instruments) |
| CARE 03, 04, 06 | credit-ratings/03-CARE, 04-CARE, 06-CARE | Jul-2025, Mar-2025, Jul-2024 | 10, 9, 9 | SKIM | Rating history only; the Jul-2026 rationale supersedes them |
| ICRA 02, 05 | credit-ratings/02-ICRA.txt, 05-ICRA.txt | Oct-2025, Oct-2024 | n/a | DEFECT | The captures hold the ICRA site shell (menus, unrelated headlines), not the rationale. NOT FOUND |
| Kenalog | filings/20260128_854dbadb; 20260401_0f8c46f9 | Acquisition agreement; completion | 1; 1 | FULL | |
| Yapan | filings/20260810_4a0a2aaf; 20260818_b7efdf15 | Call option exercised; 40.67% bought for about Rs 76 crore | 1; 1 | FULL | |
| DB pledge | filings/20260818_9DE6D096; 20260826_D47DDDB2 | Deutsche Bank Reg 29(2): 7.39% released for a "Permitted Sale Transaction", then re-pledged | 7; 6 | PART | 1-2 of each |
| HDFC | filings/20260717_32839F19 | HDFC MF Reg 29(2): stake down 2.005% to 7.015% | 3 | FULL | |
| Dahej | filings/20260204_9550ce25; 20260211_22c039ab; 20260214_38ae7f76; 20260603_f3d966be | GPCB closure, Rs 1 crore damages, interim revocation, permanent revocation | 1 each | FULL | |
| FDA | filings/20251211_68cc8f85; 20260214_afad5484; 20260413_246a7841; 20260510_be61f1a9; 20260518_25582fcf; 20260709_eff448fa; 20260914_06e6114c | Form 483s at Lexington, Digwal, Sellersville, Morpeth; EIR closures | 1 each | FULL | |
| AGM | filings/20260730_cdec2b2e | 6th AGM proceedings and scrutinizer report, 30-Jul-2026 | 29 | PART | 16 (item 10 vote, 96.18% in favour). DUP = 20260730_eac921f4 |
| Mgmt | filings/20260128_ec28cbac; 20260205_333758ba; 20260930_402d4ad6; 20260930_bd1e5cd3; 20251208_6a33af86 | CS resignation and SMP designations; Ramadorai term end; PCC COO succession; CTO; Amit Soni appointment | 6; 1; 2; 2; 2 | FULL | |
| Bayer | filings/20261001_3bfd08d6 | Distribution arrangement expires 31-Dec-2026 | 1 | FULL | |
| GST | filings/20260929_6a60cd5c | Order Rs 4.06 crore plus penalty, under appeal | 1 | FULL | |
| Q3 FY26 set | filings/20260129_2871069a (results), 20260129_94be2676 (deck), 20260128_fd285e0c (outcome) | Q3 FY26, 28/29-Jan-2026 | 10; 28; 10 | SKIM | Q3 figures taken from the FY26 deck's QoQ column. DUPs: 00c6eb45, 843bcc3f, b28a9de9, ec28cbac |
| Q2 FY26 set | filings/20251105_32a65634 (results), 20251105_f67db704 (deck) | Q2 FY26, 05-Nov-2025 | 16; 25 | SKIM | Q2 FY26 figures taken from Q2 FY27 comparatives. DUPs: 61f84b58, 72621249 |

Held, SKIM or not opened beyond page 1: the four BSE "transcript" and "audio recording" cover
letters (20251106, 20251107, 20260129_14e571e6, 20260130, 20260429_1f612bec, 20260430,
20260731), the BRSR (20260703_6b8e5c94, 47 pp.) and Sustainability Report (20260824, 91 pp.),
ESG-rating intimations (20260320, 20260406, 20260903, 20260918), KMP contact updates
(20260224, 20260429_7e0c26d8), the postal-ballot result (20260116), the Blue-Zone press release
(20260205_bc0a4c0f), the Ahmedabad flood suspension and resumption (20260724, 20260803), the
NDTV and Hindu BusinessLine clarifications (20260623, 20261001_7593ce38), the Ontario grant
clarification.

DUP sets (md5): 13 sets per `dup-sets-2026-10-29.json`. The pattern: every board outcome is
filed again under the results, CS, director and office-change categories (seven names for the
28-Apr-2026 PDF), and every press release is filed again as the deck.

## Gaps (NOT FOUND, with where it was looked for)

- **Call transcripts for Nov-2025, Jan-2026 and Apr-2026.** The BSE filings under "Earnings Call
  Transcript" and "Analyst / Investor Meet" are one-page letters pointing to piramalpharma.com;
  screener.in served only the Jul-2026 transcript. The original FY27 guidance (29-Apr-2026 call)
  is therefore NOT FOUND; the card holds the Jul-2026 reaffirmation and the Oct-2026 upgrade only.
- **Q2 FY27 call transcript** (call 28-Oct-2026). Not filed by 29-Oct-2026.
- **ICRA rationales.** Site shell captured, report not. Step 10 uses CARE alone.
- **Segment EBITDA or PBIT.** The company reports one operating segment (Q2 res p.12; AR26
  p.161 geography only). Searched the results notes, both annual reports and all four decks.
- **ROCE.** No ROCE line in AR26's financial review or ratios; the MD service figure (11.8%) is
  shown as a cross-check only.
- **Promoter pledge.** AR26 p.51 shareholding text carries no pledge column; no promoter
  encumbrance filing in the 77 announcements. The only pledge on record is CA Alchemy's.
- **FY30 strategy deck** referenced on the Jul-2026 call (p.16). Targets taken from AR25.
- **Name of the Rs 175.82 crore impaired intangible** (AR26 p.151; FY26 res) and the
  **Kenalog Q2 FY27 revenue** (Q2 deck p.16 says "contributed", no number).
- **Carlyle's "Permitted Sale Transaction"** counterparty and outcome beyond the re-pledge of
  26-Aug-2026.

## Reader and file defects noted

- Jul-26 call title page reads "Q1 FY '26 Earnings Conference Call" for the 30-Jul-2026 (Q1 FY27)
  call; the body is correct.
- Q2 deck p.4 (press release P&L) labels the Q1 FY27 column "Q1FY26"; the figures are Q1 FY27.
- AR26 p.51 shareholding table extracts out of order; the promoter row (46,33,24,672 shares,
  34.86%) and the CA Alchemy row (23,86,63,700, 17.95%) were read from the text and cross-checked
  against p.179 and CARE p.2.
- Several standalone balance-sheet and cash-flow pages in the results filings extract labels and
  values in separate blocks; values were matched by order and cross-checked against the deck.
