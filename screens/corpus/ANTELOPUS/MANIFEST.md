# ANTELOPUS corpus manifest

Antelopus Selan Energy Ltd (formerly Selan Exploration Technology Ltd). NSE ANTELOPUS (was SELAN; NSE file names still carry the SELAN prefix), BSE 530075.
Ledger written 2026-10-26 for the sixth screen run. Card: `screens/cards/ANTELOPUS.md`.

Status key: FULL = read in full; PART = key sections read, rest navigated by keyword; SKIM = housekeeping, checked for substance; DUP = byte-identical to another held file (md5 checked).

## How it was built

- screener/: `screener_collect.py` output (FY25 and FY26 annual reports, latest deck, Financials.xlsx). Collected earlier on 2026-10-26 by an interrupted session of this same task and reused after the integrity check below.
- filings/: NSE corporate-announcements API (cookie from the home page first), 1-Apr-2025 to 26-Oct-2026, results, decks, rating letters, Reg 30 and SAST disclosures.
- market-data-2026-10-26.md: screener.in company page, a service record.

## Integrity check (2026-10-26)

All 55 PDFs opened with PyMuPDF, every page's text extracted, page markers in each `.txt` match the PDF page count, and every PDF ends with `%%EOF` in its last 2 KB. **No broken file.** No NSE file name in this set carries a byte count to check against.

## screener/

| Path | Type | Period | Pages | Status | Notes |
|---|---|---|---|---|---|
| screener/Annual_Report_2026.pdf | Annual report | FY26 | 178 | PART | Read: p.15 (history, strategy), p.16 (field, licence validity, in-place and 2P table), p.46 (board, KMP, auditor), p.72 (shareholding categories), pp.106-107 (auditor's report, emphasis of matters, KAM), p.119 (cash flow), p.121 (equity), pp.145-146 (promoter holding, merger shares), pp.158-159 (related parties, KMP pay). The NSE copy filings/SELAN_05092026182952_Annual_Report has 179 pages (one extra cover page) and differs in bytes. |
| screener/Annual_Report_2025.pdf | Annual report | FY25 | 158 | SKIM | Pre-merger Selan. Not used for numbers; FY25 restated figures come from the FY26 filings. |
| screener/Investor_Presentation_1.pdf | Earnings deck | Q2 FY27 | 11 | DUP | Byte-identical to filings/SELAN_26102026164942_Investor_Presentation. |
| screener/Financials.xlsx | screener.in export | n/a | n/a | not used | Service export. |

## filings/ (52 PDFs)

Substantive, read:
- SELAN_26102026163129_outcome_of_bm (7 pp): Q2 FY27 results with limited review, balance sheet, H1 cash flow, notes 4-9. FULL.
- SELAN_26102026164942_Investor_Presentation (11 pp): Q2 FY27 deck, FY29 production roadmap, field sales, P&L, balance sheet. FULL.
- SELAN_27072026205722_Investor_presentation (11 pp): Q1 FY27 deck. PART (pp.3-7).
- SELAN_27072026175920_outcome_of_BM (5 pp): Q1 FY27 results. Superseded by the Q2 filing's comparative column; SKIM.
- SELAN_04052026182056_Outcome_040526_sd (10 pp): Q4 and FY26 audited results, merger and Cambay notes. PART (pp.5, 8).
- SELAN_04052026193734_FY_26_Annual_Presentation_sd (10 pp): FY26 deck. FULL.
- SELAN_09062026214349_Intimation_of_Credit_Rating (8 pp): India Ratings press release of 09-Jun-2026 enclosed, IND A/Stable/IND A1. pp.2-8 [OCR]. FULL.
- SELAN_09022026211500_Reg30_Clarification (2 pp): Synergia Cambay transaction clarification. FULL.
- SELAN_01092026163546_Regulation_30 (1 p): DSF Round IV award. FULL.
- SELAN_27072026130057_Reclassification_request (3 pp) and SELAN_31072026161942_Intimation (1 p): Payal Upadhyay promoter-group reclassification. FULL.
- team_sandeshc_11062026122746_42 and team_sandeshc_10062026131836_40, team_sandeshc_19052026130215_34, team_sandeshc_07052025133118_8 (1 p each, [OCR]): Reg 31(4) no-encumbrance declarations. SKIM.
- SELAN_20062026123635_Intimation (1 p): one-to-one investor meetings 24-25 Jun 2026. SKIM.
- SELAN_22102026182842_Intimation_of_schedule_of_Earning_call (2 pp): Q2 FY27 earnings call schedule. SKIM.

Older decks and results held and not needed beyond the cited quarters: Q1 FY26 (12-Aug-2025, two DUP copies of the outcome), Q2 FY26 (11-Nov-2025, two DUP copies of the outcome, two deck copies), Q3 FY26 (22-Jan-2026 outcome and deck), Q4 FY25 (09-May-2025), May-2025 and May-2026 corporate presentation notices. Housekeeping filings (AGM proceedings and voting results 2025 and 2026, Reg 29 and Reg 10(6) SAST filings of Aug-2025, trading-window and misc Reg 30 notices) SKIM.

DUP pairs (md5): SELAN_12082025174758 = SELAN_12082025175652; SELAN_11112025181850 = SELAN_11112025182712; SELAN_26102026164942 = screener/Investor_Presentation_1.

## Gaps (NOT FOUND, with where it was looked for)

- **Concall transcripts: none exist in the corpus.** NSE announcements 1-Apr-2025 to 26-Oct-2026 list no transcript. screener.in lists one call recording (mp3, not held) and no transcript. The company site www.antelopusenergy.com serves no investor page to a plain fetch (/investors/ returns 404). The Q2 FY27 call was scheduled after the 26-Oct-2026 results (SELAN_22102026182842); its transcript is not yet filed. Weakens steps 3, 7 and 8.
- **Name of the private-equity backer behind Blackbuck Energy Investments Ltd.** The FY26 AR says only "backed by private equity" (AR26 p.15). Weakens step 4.
- **Independent reserve report.** Referenced in the Q2 FY27 results note 4 ("reserve studies corroborated by Independent Expert"); not filed. Weakens steps 6 and 9.
- **Merger valuation report and swap ratio document** for the Antelopus Energy amalgamation. Not in the NSE set read. Weakens step 4.
