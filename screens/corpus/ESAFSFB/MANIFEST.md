# ESAFSFB corpus manifest

ESAF Small Finance Bank Ltd. NSE ESAFSFB, BSE 544020. Thrissur, Kerala. Small finance bank; listed on BSE and NSE on 10-Nov-2023 (Q1 deck p.29).
Ledger written 2026-10-29. Card: `screens/cards/ESAFSFB.md`.

Status key: FULL = read in full; PART = key sections read, rest navigated by keyword; SKIM =
housekeeping, checked for substance; DUP = byte-identical to another held file (md5 checked).
Page numbers are PDF page numbers. Deck PDF page = slide number plus one. Transcript PDF page =
printed page plus one. AR26 printed page numbers do not map evenly to PDF pages; the card cites PDF
pages only.

## How it was built

- screener/: `tools/collector/screener_collect.py https://www.screener.in/company/ESAFSFB/ --output-dir screens/corpus/ESAFSFB/screener --no-drive`
  under `py -3.14`, 2026-10-29: the FY25 and FY26 annual reports, four transcripts (Nov-2025, Feb-2026,
  May-2026, Aug-2026), the Q1 FY27 investor presentation, Financials.xlsx (service export, never cited).
- filings/: BSE announcements API (`AnnSubCategoryGetData/w`, strCat -1), called from a bseindia.com
  page in the in-app browser because scripted calls to NSE and BSE returned Access Denied on
  2026-10-29. One window of 12 months, 29-Oct-2025 to 28-Oct-2026: 93 announcements listed from
  03-Nov-2025 to 26-Oct-2026, 89 attachments held (four ledger rows share a file with a same-day
  twin). Housekeeping categories dropped (board-meeting intimations, newspaper publications,
  trading-window closures, Reg 74(5), investor complaints, shareholding patterns, Reg 7(3), Reg 40,
  record dates, large-corporate forms, secretarial compliance). ESOP allotments and Reg 57 interest
  certificates came through and are held as SKIM. Attachments downloaded from
  `xml-data/corpfiling/AttachLive/`, falling back to `AttachHis/`, with `curl -C -` and three
  retries. File name = filing date + BSE attachment name.
- credit-ratings/: `tools/collector/fetch_ratings.py` over the six agency links on the screener.in
  page: CARE PDFs of 17-Mar-2025, 28-Mar-2025, 02-Sep-2025 and 01-Sep-2026; Brickwork PDFs of
  04-Oct-2024 and 19-Aug-2025. The Brickwork action of 17-Aug-2026 is held only as the bank's BSE
  intimation (filings/20260818_60227bd6), which encloses the rationale.
- market-data-2026-10-29.md: screener.in company page, a service record (28-Oct-2026 close).
- Text: PyMuPDF; Tesseract OCR on pages with under 40 characters of native text, tagged `[OCR]`.

## Integrity check (2026-10-29)

All 102 PDFs (7 screener, 6 credit-ratings, 89 filings) opened with PyMuPDF. Every page's text was
extracted, page markers in each `.txt` match the PDF page count, and every file ends with `%%EOF`.
33 filing pages and 14 screener pages carry `[OCR]`. 6 md5 duplicate sets, listed in
`dup-sets-2026-10-29.json`. **No broken file.**

## Substantive files, read

| Short name | Path | Period / date | Pages | Status | Pages read |
|---|---|---|---|---|---|
| Q1 deck | screener/Investor_Presentation_1.pdf | Q1 FY27, filed 31-Jul-2026 | 45 | FULL | 1-45. Pages 5, 8, 17, 20, 25, 35 are OCR section dividers with no text. DUP = filings/20260731_677cea2b |
| Q1 res | filings/20260731_0146fdf8-... | Q1 FY27 results, 31-Jul-2026 | 10 | FULL | 1-10 (review report, P&L, segments, notes incl. SRs and Tier II, Reg 52(4)) |
| Q4 res | filings/20260430_4ac45599-... | FY26 audited results, 30-Apr-2026 | 18 | FULL | 1-18 (audit report, P&L, balance sheet, cash flow, ARC sale table, notes, Reg 52(4)). Same-day twin under "Outcome of Board Meeting" |
| Q2 res | filings/20251111_1c74d1ac-... | Q2 FY26 results, 11-Nov-2025 | 14 | PART | 5 (P&L columns for provisions and PAT) |
| Q3 res | filings/20260130_9af399dd-... | Q3 FY26 results, 30-Jan-2026 | 11 | SKIM | Q3 figures taken from Q4 res p.8 comparatives |
| Q2 KBU | filings/20261001_31d31d4a-... | Q2 FY27 key business update, 01-Oct-2026 | 2 | FULL | 1-2 (deposits, advances, Rs 625 crore technical write-off) |
| KBU Q1, Q4, Q3 | filings/20260702_43186521, 20260404_dd70b152, 20260105_0df168a8 | quarterly business updates | 2 each | SKIM | 1 (deposit and advance tables) |
| AR26 | screener/Annual_Report_2026.pdf | FY26, AGM 14-Aug-2026 | 199 | PART | 32-35 (MARG, financial capital KPIs), 50-51 (MD&A NII, provisions, ratio table), 68 (director pay ratios), 112-113 (top shareholders, category table), 114 (penalties), 120-121 (key audit matters), 129 (opex schedule, BC expenses), 150 (RBI penalty), 154-155 (related parties), 159 (contingent liabilities, ESMACO). DUP = filings/20260720_c99656e6 |
| AR25 | screener/Annual_Report_2025.pdf | FY25 | 180 | SKIM | Not read beyond page 1; FY25 figures taken from Q4 res, Q1 deck p.40 and CARE-25 |
| AGM | filings/20260720_c99fe6cb-... | 10th AGM notice, 20-Jul-2026 | 199 | PART | 31 (MD pay revision), 34 (ED pay revision), 39 (Articles amendment, promoter nomination rights); item list via keyword |
| Aug-26 call | screener/Concall_Aug_2026_Transcript.pdf | Q1 FY27 call, 03-Aug-2026 | 12 | FULL | 1-12. DUP = filings/20260807_27801c0c |
| May-26 call | screener/Concall_May_2026_Transcript.pdf | Q4 FY26 call, 04-May-2026 | 8 | FULL | 1-8. DUP = filings/20260508_38293954 |
| Feb-26 call | screener/Concall_Feb_2026_Transcript.pdf | Q3 FY26 call, 02-Feb-2026 | 10 | FULL | 1-10. DUP = filings/20260207_66d0b24b |
| Nov-25 call | screener/Concall_Nov_2025_Transcript.pdf | Q2 FY26 call, 12-Nov-2025 | 15 | FULL | 1-15. DUP = filings/20251118_032eeb00 |
| Q1 press, Q4 press | filings/20260731_dd707a2a; 20260430_0437e21e | Q1 FY27 and Q4 FY26 press releases | 3 / 4 | FULL | 1-3 / 1-4 |
| Q4 deck, Q3 deck, Q2 deck | filings/20260501_4592ce22; 20260131_6a95ab08; 20251111_31983e7b | FY26 quarterly decks | 44 / 43 / 42 | SKIM | Credit-cost definition page only; the Q1 deck carries the five-quarter series |
| CARE | credit-ratings/01-CARE.pdf | 01-Sep-2026, A-/Stable from Negative | 8 | FULL | 1-8 |
| CARE-25 | credit-ratings/02-CARE.pdf | 02-Sep-2025, downgrade to A-/Negative | 8 | PART | 1-2 |
| CARE Mar-25 | credit-ratings/04-CARE.pdf, 05-CARE.pdf | 28-Mar-2025, 17-Mar-2025 | 7 / 7 | SKIM | Rating history taken from CARE p.6-7 |
| BWR | filings/20260818_60227bd6-... | Brickwork upgrade to A-/Stable, 17-Aug-2026 | 10 | FULL | 1-10 (cover letter p.1, rationale pp.2-7) |
| BWR-25 | credit-ratings/03-Brickwork.pdf | 19-Aug-2025, downgrade to BBB+ | 8 | PART | 1 |
| BWR-24 | credit-ratings/06-Brickwork.pdf | 04-Oct-2024 | 8 | SKIM | Rating history taken from BWR p.6 |
| CARE intimation | filings/20260902_10c2ded1-... | bank's intimation of CARE action | 11 | SKIM | 1-2 (summary table); rationale read from credit-ratings/01-CARE |
| ARC | filings/20251229_cd3b1e84-... | ARC sale of Rs 1,693.65 crore for Rs 183.18 crore | 1 | FULL | 1 |
| Scheme | filings/20251124_959a0ed0-... | EFHL revised scheme of arrangement | 27 | PART | 1-4 (cover, EFHL letter: 52.87% to 45.58%, Dia Vikas below 5%) |
| RBI-S | filings/20251219_6f615325-... | RBI takes revised scheme on record | 2 | FULL | 1-2 |
| Bd-Dec | filings/20251212_7c48e96f-... | board outcome 12-Dec-2025: ARC pool up to Rs 1,700 crore, four retirements | 7 | PART | 1-2. Twin: 20251212_9a04ad4b (director retirements) |
| Bd-Jun | filings/20260604_8599f9eb-... | board outcome 04-Jun-2026: new ID, NED, CRO, Head IA | 10 | PART | 1-3. Twins: 20260604_c12eb70b, 20260604_60dee9fa |
| Bd-Sep | filings/20260923_9e6d82c7-... | Tier II NCDs up to Rs 500 crore approved | 3 | FULL | 1-3 |
| Bd-Nov | filings/20251103_c2f81f30-... | Tier II NCDs up to Rs 150 crore approved | 4 | PART | 1-2 |
| CBS | filings/20261026_a07e6fb8; 20261016_67dff301 | core banking migration complete; migration window | 2 / 2 | FULL | 1-2 each |
| Call-int | filings/20261022_a217ee2c-... | Q2 FY27 call intimation, 29-Oct-2026 4 PM | 2 | FULL | 1-2 |
| Directors | filings/20260814_ab1868a1; 20260814_dd4e68ad; 20260430_bc37a407; 20260430_27437992; 20260331_e93a9458; 20260227_4518870b; 20251111_2a198dc4 | AGM approvals, auditor appointment, KMP reclassification, retirements | 2-5 each | PART | 1-2 each |
| Volume query | filings/20260617_2839e487; 20260617_b4b054c5 | NSE and BSE volume clarifications | 1 each | FULL | 1 |
| Milestone | filings/20260612_d209a25d-... | total business crosses Rs 50,000 crore | 1 | FULL | 1 |
| MD | market-data-2026-10-29.md | screener.in service record | n/a | FULL | market cap, price, book value, shareholding, quarterly cross-check only |

Held, SKIM or not opened beyond page 1: twelve ESOP allotment intimations; six Reg 57 interest-payment
certificates; two half-yearly NCD reports (Oct-2026, Apr-2026); three Tier II allotment intimations
(Nov-2025, Jan-2026, Jun-2026); four earlier call intimations and four call outcomes; two ESG rating
intimations; two committee reconstitutions; postal ballot results (12-Dec-2025); AGM date intimation;
annual report dispatch letter; BRSR FY26 (filings/20260720_f39c33a2, 28 pages); ESOP grant intimation.

DUP sets (md5): 6 sets, all screener-to-filings twins: the four transcripts, the Q1 FY27 deck and the
FY26 annual report. Four ledger rows ("Financial Results" for Q1 FY27 and FY26, "Outcome of Board
Meeting" 27-Feb-2026, "Outcome" 30-Jan-2026) share a same-day file and are not separate attachments.

## Gaps (NOT FOUND, with where it was looked for)

- **Q2 FY27 results, deck and press release.** Not filed by 28-Oct-2026; only the call intimation of
  22-Oct-2026 is held. The ledger's last row is 26-Oct-2026. Steps 5, 8 and 13 use Q4 FY26 and Q1 FY27.
- **Explanation of the Rs 625 crore technical write-off** in Q2 FY27. The business update (Q2 KBU p.2)
  states the amount only. Provision effect, segment and vintage not disclosed.
- **Promoter pledge or encumbrance.** No line in AR26 pp.112-113 (shareholding tables), the Q1 deck
  p.27, or MD. The shareholding-pattern filings are a dropped housekeeping category.
- **AGM voting results** of 14-Aug-2026 on items 7, 8 (MD and ED pay) and 10 (Articles amendment).
  Only the director and auditor approvals (items 2 to 6) were filed under Reg 30; the scrutiniser
  report is a dropped category.
- **Emerging Household vintage slippage.** Segment GNPA and SMA stock are in the Q1 deck pp.13-14;
  vintage-wise behaviour was given once for microfinance (Nov-25 call p.11) and never for EH.
- **Q2 FY26 and Q3 FY26 credit cost in rupees by segment.** Only the blended quarterly percentage
  (Q1 deck p.16) and total provisions are disclosed.
- **Brickwork 17-Aug-2026 rationale as an agency PDF.** screener.in links only the 2024 and 2025
  Brickwork PDFs; the 2026 rationale is held through the bank's intimation, which encloses it in full.
