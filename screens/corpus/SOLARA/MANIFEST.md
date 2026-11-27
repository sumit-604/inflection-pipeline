# SOLARA corpus manifest

Solara Active Pharma Sciences Ltd. NSE SOLARA and SOLARAPP1 (partly paid), BSE 541540 and 890202.
Ledger written 2026-10-18 for the fifth screen run. Card: `screens/cards/SOLARA.md`.

Status key: FULL = read in full; PART = key sections read in full, rest navigated by grep; SKIM = housekeeping, checked for substance; DUP = byte-identical to another held file (md5 checked), read once.

## screener/

| Path | Type | Period | Pages | Status | Notes |
|---|---|---|---|---|---|
| screener/Annual_Report_2026.pdf | Annual report | FY26 | 257 | PART | Read: pp.4-35 (highlights, base vs Ibuprofen split, MD and CEO letter, KPIs, board, leadership), MD&A pp.35-41, Board's report pp.42-47, shareholding p.77, auditor's report and CARO pp.114-125, tax note p.148, share capital and promoter notes pp.151-152, CWIP p.143, related parties pp.167-168, segment note p.170, fire note p.178, AGM notice RPT resolution pp.243, 251-253. |
| screener/Annual_Report_2025.pdf | Annual report | FY25 | 249 | PART | Navigated by grep: TPG sell-down p.58, Vizag USFDA zero-483 inspection p.57 (secretarial audit), >5% holders p.148. p.30 is [OCR]; not used. |
| screener/Concall_Nov_2025_Transcript.pdf | Transcript | Q2 FY26, call 05-Nov-2025 | 15 | FULL, DUP | Identical to filings/SOLARA_11112025150734. |
| screener/Concall_Feb_2026_Transcript.pdf | Transcript | Q3 FY26, call 06-Feb-2026 | 11 | FULL, DUP | Identical to filings/SOLARA_10022026175146. |
| screener/Concall_May_2026_Transcript.pdf | Transcript | Q4 FY26, call 15-May-2026 | 16 | FULL, DUP | Identical to filings/SOLARA_21052026122119. |
| screener/Concall_Jul_2026_Transcript.pdf | Transcript | Q1 FY27, call 23-Jul-2026 | 17 | FULL, DUP | Identical to filings/SOLARA_29072026113417. |
| screener/Investor_Presentation_1.pdf | Earnings deck | Q1 FY27 | 11 | FULL, DUP | Mislabelled. Byte-identical to filings/SOLARA_23072026133057 (Q1 FY27 press release and earnings update). No standalone investor presentation is held. p.11 [OCR], contact page. |
| screener/Financials.xlsx (+ .txt) | screener.in export | FY18-FY26, Q1 FY25-Q2 FY27 | n/a | FULL | Service export, not a filed document. Data Sheet populated; formula sheets blank in the text export. Used only as a cross-check. |

## credit-ratings/ (CRISIL rationales, HTML plus text)

| Path | Date | Action | Status |
|---|---|---|---|
| 01-CRISIL | 22-Jun-2026 | Upgraded to BBB+/Stable/A2 from BBB/Stable/A3+ | FULL |
| 02-CRISIL | 30-Apr-2026 | Reaffirmed BBB/Stable/A3+; Rs 692.8 crore proposed facility withdrawn | FULL |
| 03-CRISIL | 16-Apr-2025 | Outlook Negative to Stable, BBB reaffirmed | FULL |
| 04-CRISIL | 07-Jun-2024 | BBB/Negative/A3+ reaffirmed | FULL |
| 05-CRISIL | 03-May-2024 | BBB/Negative/A3+ reaffirmed | FULL |
| 06-CRISIL | 22-Feb-2024 | Downgraded to BBB/Negative/A3+ from BBB+ (Watch Negative after Puducherry fire) | FULL |
| manifest.json | | Source URLs | read |

## filings/ (59 exchange filings)

Substantive, read in full:
- SOLARA_16102026133129_SE_Outcome_Signed (12 pp): Q2 FY27 results, review report, balance sheet, cash flow, notes. Text layer garbles digits with no [OCR] tag; pp.4-7 checked visually against the PDF.
- SOLARA_16102026134610_Press_Release_SE (13 pp): Q2 FY27 earnings update, base vs Ibuprofen split, net debt bridge, strategic review status.
- SOLARA_24072026141102_SE_MRL_outcome_July242026 (9 pp): Q1 FY27 results, machine-readable copy. Used in place of the OCR outcome below.
- SOLARA_23072026131622_SE_FIling_Outcome (8 pp): Q1 FY27 results, pp.2-8 [OCR]. Not used for numbers; superseded by the MRL copy.
- SOLARA_23072026133057_SE_Press_Release_Signed (11 pp): Q1 FY27 earnings update. p.11 [OCR] contact page.
- SOLARA_15052026131424_SE_Outcome_Signed (19 pp): FY26 audited results, unmodified opinion, going-concern note p.11.
- SOLARA_15052026132136_Press_Release_SE (10 pp): Q4 FY26 update. States the base vs Ibuprofen split is "management estimated proforma" and restated. p.10 [OCR] contact page.
- SOLARA_06022026140941_SE_Press_Release_Solara (10 pp): Q3 FY26 update, first disclosure of the Ibuprofen split. p.10 [OCR].
- SOLARA_06022026133924_SE_Outcome_Solara_Dec25 (8 pp): Q3 FY26 results. Navigated.
- SOLARA_05112025144017_SE__Press_release_Solara (9 pp), SOLARA_25072025151837 (10 pp): Q2 and Q1 FY26 updates. Skimmed for the quarterly series. Last page [OCR] in each.
- SOLARA_05112025141608_SELetter_FinancialsSep25 (12 pp): Q2 FY26 results. SOLARA_06112025110125 is byte-identical (DUP, refiled).
- SOLARA_25072025132342_SE_Outcome_Solara_Final (17 pp): Q1 FY26 results. Navigated; p.17 [OCR].
- SOLARA_29072025162637_SE_Solara_Transcipt (15 pp): Q1 FY26 call, 25-Jul-2025. FULL. Not one of the four screener transcripts; it carries the Rs 400-500 crore CRAMS ambition.
- SOLARA_19112025102630_Disclosure-_US_FDAMangalore (2 pp): Mangalore EIR, VAI, two 483s.
- SOLARA_28042026165601_SE_Intimation_PressReleaseUSFDA (2 pp): Puducherry EIR, VAI, four 483s, unannounced inspection.
- SOLARA_18032026190217 (2 pp) and SOLARA_28082026144034 (2 pp): Rs 161.92 crore AY2019-20 tax demand and its rectification to nil.
- SOLARA_23062026182838_SE_filings_final (4 pp): CRISIL upgrade letter.
- SOLARA_01072025172336 (3 pp): CRISIL letter, outlook to Stable. pp.2-3 [OCR]; no numbers used.
- SOLARA_05122025182039 (3 pp): WTD and COO Mohan Muthunarayanan moves to Synthix to build CRAMS and convert Vizag to CDMO.
- SOLARA_17122025105153 (3 pp), SOLARA_04022026224954 (16 pp), SOLARA_10032026130035 (6 pp): Mohanraj S appointed WTD; postal ballot; result (promoters 1,81,56,624 shares on record).
- SOLARA_13082025155258_SE_MA_Report (12 pp): CRISIL monitoring agency report, rights issue, Q1 FY26. Names promoters.
- SOLARA_18082026135536_SE_Filing_signed (5 pp): ESOP allotment; shows 2,82,470 shares at Rs 7 paid and 1,65,807 at Rs 3.5 paid still outstanding.
- team_bbodade_28042026163005_SOLARA and team_bbodade_14052026164303_SOLARA (2 pp each): byte-identical (DUP). Pronomz Reg 31(4) declaration dated 06-Apr-2026. Both pages [OCR]; annexure garbled. No numbers taken from them.
- SOLARA_10102026182311 and SOLARA_17102025111650: CRISIL ESG 63 (FY26) and 56 (FY25).

Housekeeping, skimmed:
- NSE surveillance replies on volume: 26-Sep-2025, 04-Dec-2025, 10-Jun-2026.
- ESOP allotments: 14-Oct-2025, 05-Nov-2025, 17-Dec-2025, 15-May-2026, 16-Jun-2026 (x2), 23-Jul-2026, 16-Oct-2026.
- Call intimations and audio-recording notices: 05-Nov-2025, 06-Feb-2026, 15-May-2026, 23-Jul-2026, 16-Oct-2026.
- Newspaper publications: 26-Jul-2025, 06-Nov-2025, 05-Feb-2026, 07-Feb-2026, 16-May-2026 (pp.2-3 [OCR]), 24-Jul-2026, 17-Oct-2026.
- Policy revision 06-Feb-2026.

## market-data-2026-10-18.md
screener.in service record dated 2026-10-18, not a filed document. Market cap Rs 3,381 crore, price Rs 697, quarterly shareholding to Jun-2026.

## Held nowhere: documents that exist but are not in the corpus
- Q2 FY27 earnings call transcript (call held 16-Oct-2026; only the call-outcome filing is held). Weakens steps 6-8 on the strategic review.
- Rights issue Letter of Offer, 09-May-2024 (the call schedule is reconstructed from AR26 p.43 and Q2 FY27 outcome p.7). No offer/ folder.
- No results/ folder: quarterly results sit in filings/ only.
- Ibuprofen strategic review documents and the Synthix demerger scheme.
- USFDA outcome for Cuddalore and a dated EIR for Ambernath.
- Monitoring agency reports after Q1 FY26.
- Promoter pledge or encumbrance quantum (the Reg 31(4) declaration refers to encumbrances "already disclosed"; those disclosures are not held).
- Q4 FY25 (May 2025) transcript.

## Defects found
1. screener/Investor_Presentation_1.pdf is the Q1 FY27 press release, not an investor presentation (md5 match).
2. Five byte-identical duplicates: four transcripts (screener vs filings), the Q2 FY26 financials filed twice, and the two team_bbodade files.
3. Q2 FY27 outcome text layer garbles digits (for example "14 501" for (4.50), "392.IJJ" for 392.60) without an [OCR] tag. Verified visually.
4. CRISIL 22-Jun-2026 rationale says gearing was "1.9 times as on March 31, 2026". AR26 p.24 gives net debt to equity of 0.5 and the 30-Apr-2026 rationale gives gearing below 1 at 31-Dec-2025. Treated as a source text error (the 1.89 figure belongs to March 2024).
5. The base vs Ibuprofen split is unaudited management proforma and was restated between decks: Q3 FY26 base EBITDA Rs 608 Mn in the Feb-2026 deck, Rs 520 Mn in the May-2026 deck; Ibuprofen Rs (234) Mn became Rs (146) Mn.
6. Partly paid reconciliation gap: Q2 FY27 outcome p.7 shows Rs 1.43 crore first-call and Rs 1.90 crore final-call money unpaid; the 18-Aug-2026 filing shows 4,48,277 partly paid shares outstanding, which implies more unpaid money than that at the stated call amounts. Not resolved in the corpus.
7. AR26 states rights money received to 31-Mar-2026 as Rs 309.79 crore in the Board's report (p.44) and Rs 312.79 crore in note 50 (p.178). Internal inconsistency of Rs 3 crore.
