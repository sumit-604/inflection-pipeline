# VERIFIER A: NUMERICAL ACCURACY, CREDENT (run 2026-11-12)

Model sonnet-5-5 (high). Fresh context. Inputs: stage reports 01 to 09 and the source PDFs and page-marked text files in the run folder. Units follow each source face: AR, RHP, H1 FY27 results and listing deck in Rs Lakhs; H1 FY27 deck in Rs Mn; call and press release in Rs Cr.

Page convention used for the check: the "[page N]" marker in the .txt (content follows its marker). The RHP printed folio is marker minus 4. Where a stage cited the printed folio without saying so, the finding says so.

Images read to settle OCR doubts: H1 FY27 results PDF pages 4 (balance sheet), 6 (cash flow) and 19 (IPO utilisation, Annexure A).

## Result in one line

No CRITICAL. 3 MAJOR, 6 MINOR. Gate 0 mandatory inputs: 56 of 56 checked. Every Gate 0 base figure, every recomputed ratio and every score input matches the RHP, the XBRL files, the screener sheet and the decks. The Gate 0 verdict is not touched by any finding below.

## Findings table

| # | Severity | Report location | Claimed (value and anchor) | Source truth (location) | Note | Source fidelity |
|---|---|---|---|---|---|---|
| 1 | MAJOR | 01-gate0.md, Block E, E2 (mandatory input) | "100% at 7 Aug 2024 (Ashok Kumar Sharma 50%, Karan Sharma 50%, RHP p.76)". Report header says all RHP pages are .txt page markers | RHP marker p.76 holds no such table. The table "Two Years prior ... 10,00,000 50.00% ... 20,00,000 100.00%" with the 7 Aug 2024 footnote is on marker p.80 (txt lines 5531-5540). Printed folio of that page is 76 | The number is right and the score is not affected (a 36.25pp fall scores 0 on any size). The cited page is wrong under the report's own stated convention. ANCHOR NOT FOUND stands until the anchor is corrected to p.80 | true |
| 2 | MAJOR | 03-ardeep.md Phase 3A, bullet "The FY27 half confirms direction" | "purchase of fixed assets and FD placement 636.67" (H1 cash flow, OCR-read) | H1 FY27 results PDF p.6 image: Purchase of Fixed Assets incl CWIP (443.12); Investment in FD / Redeem (656.67). Net investing (1,091.67) = 7.37 + 0.75 - 443.12 - 656.67 | The OCR text reads "(63667)". The image shows 656.67. 636.67 is neither line and not their sum | true |
| 3 | MAJOR | 03-ardeep.md LB4 bullet 3 ("H1 consolidated balance sheet ... Cash 6,919.72"), Phase 3A "Cash pile", Phase 8 strength 3 ("post-IPO cash 6,919.72 (H1 BS)"); carried into 04-bizmodel.md 4A ("IPO cash 6,919.72 at Sep-26 (B03)") | Balance-sheet cash 6,919.72 at 30 Sep 2026 | H1 FY27 results PDF p.4 image: Cash and Bank Balances 7,419.72 (txt "741972"). 6,919.72 is "Cash and Cash equivalents at end of the year" on the cash flow, p.6. The 500.00 gap is fixed deposits. H1 deck p.22 (Rs Mn) also shows cash and bank 742 | The 6,919.72 exists in the source, but on the cash flow, not on the balance sheet where the report places it. The basis is not labelled at the three uses. Net cash after IPO is understated by 500.00 on the balance-sheet reading. Stage 5 and 7 use 74.20 Cr correctly | true |
| 4 | MINOR | 02-notes-pass1.md sections 0, 2.1 and 3 ("AR Note 1, p.79 and p.106"; going concern "Note 1, p.79") | Standalone Note 1 basis of preparation and going concern text on p.79 | AR marker p.78 (txt lines 2929-2937). Marker p.79 begins at line 2985 with the next policies. Consolidated p.106 is correct (line 4651). Stage 3 D1 already records the slip | Page off by one. B02 text was not corrected | true |
| 5 | MINOR | 05-concall.md LB2 first bullet; 2B | "p.14 (Prashant Sharma): '45% CAGR ... excluding the inorganic growth rate, right?' Tarun: 'Yes. You are right on this.'" | Transcript marker p.15 (txt lines 640-646). Marker p.14 ends at line 606 with Abhi Jain's reply. Printed page "14 of 18" is the foot of marker p.15 | The quote is exact. The page is the printed folio, while the report says it uses PDF pages. Same slip: "wrong question (p.15)" is on p.16 (line 678); "beautiful question (p.12 ...)" first instance is on p.13 (line 534) | true |
| 6 | MINOR | 04-bizmodel.md 1B, "RHP p.27: no credit period is punched in the system and ageing is built from the accounting date (RHP line 13510, Note 15 per B02)" | Statement sits on RHP p.27 | RHP p.27 (lines 1702-1765) holds "working capital intensive" (line 1722) and the terminable-contract text (lines 1711-1714). The "no credit period punched in system" text is at line 13510, far from p.27, and in the AR at Note 15 note 4 (marker p.84) | The line anchor in brackets is correct. The page label is not | true |
| 7 | MINOR | 08-promoter.md Load-bearing 4 context, 3E, 6A row 7, 6C (auditor resignation "RHP p.68, lines 4741-4775") | Auditor change table on RHP p.68 | Marker p.72 (txt lines 4741-4775). Printed folio of p.72 is 68 | Dates and wording match: Aakash Kumar & Co, 8 Sep 2025, "On request of Management"; R K Jagetiya & Co, 30 Sep 2025. The report mixes printed folios (p.68, p.156-157, p.149-150) with markers (p.31-32, p.37) and does not say so. Line numbers resolve every call | true |
| 8 | MINOR | 09-tam.md 5E | "current valuation of 30.8x P/E (screener, 2026-11-12; step1 brief)" | screener-Data_Sheet.csv carries Current Price 432.3 and Market Capitalization 787.78 Cr. It has no P/E field. 787.78 / (H1 FY27 PAT 14.65 + H2 FY26 PAT 10.84 = 25.49) = 30.9x | The figure is close to a derivable one but not printed in the file. The step1 brief is memory, not a source in front of me. Not a verdict-card input | true |
| 9 | MINOR | 07-emoat.md G2 | "receivable days 81.55 FY25 to 98.58 FY26 (B01)" | B01 shows receivable days 83.85 (FY25) and 100.26 (FY26). 81.55 and 98.58 are working-capital days (receivable days less payable days) in B01 | Basis mislabel: net WC days called receivable days. Direction (worse) is unchanged. Unlabelled basis difference, reported as UNANCHORED, not material | false |

## Rows struck by the rule 5b self-check (7)

1. Gate 0 "presentation FY25 revenue 81.8 Cr and PAT 5.5 Cr conflicts with RHP, gap unexplained". Faithful transcription of an odd source difference. Stage 4 later explains it (the deck repeats the unrestated AR figures 8,182.32 and 553.23). Not a finding.
2. 05-concall "IPO annexure prints 21.65 and 21.13 in two total columns". The source prints both (results PDF p.19 image). Faithful transcription.
3. 02-notes-pass1 Section 2.6 "statutory dues 393.28". Superseded by the stage's own ERRATA (393.69 gross; 259.28 net). The corrected figure matches the Note 9 rows.
4. 02-notes-pass1 "benefit paid 13.48??", "IALM 2012-14", "43% of opening obligation". Superseded by ERRATA.
5. 02-notes-pass1 LB2 "100,000 x Rs 11,440 = 1,144.00". Superseded by pass 2 C2 (11,440.00).
6. 02-notes-pass1 deferred tax "movement column does not reproduce". Withdrawn in pass 2 C1; I re-added 40.02 + 21.36 = 61.38 against AR p.82 and it ties.
7. 03-ardeep "H1 CFO printed total garbled, derived (152.94) + (239.49) = (392.43)". The value matches the image (results PDF p.6 prints (392.43)). A matched figure is not a finding.

## What checked clean (no finding), by stage

Gate 0 (mandatory): all 16 base rows across FY24, FY25 and FY26 against RHP markers p.56 (balance sheet), p.57 (P&L), p.58 (cash flow); contingent liability 62.11 (p.60); promoter 63.75% and pledge false (XBRL, both dates); FII 2.13% and DII 5.71%; net block 1,457.08 (p.56); M8 reach figures 6,000+, 19,000+, 2,500+ (H1 deck p.13); concentration 15.76%, 22.43%, 18.70% and top 10 81.76%, 83.31%, 87.92% (RHP marker p.25 line 1638 and p.26); screener FY26 sales 214.16, PAT 18.45, receivables 58.83, CFO -6.62. All derived ROCE, ROE, WC days, FCF, CAGR, EBITDA, D1 to D4 and E4 values were recomputed and match to the stated decimals.

Stage 2 and 3 (AR): standalone and consolidated balance sheet, P&L and cash flow (p.75-77, p.103-105); ageing tables (p.85) and consolidated ageing (874.55 unbilled); Note 7.2 bank gap 3,730.10 / 4,063.31 / 333.21; Notes 2, 3, 4, 6, 7, 9, 13, 15, 19 to 26; share capital and bonus; Annexure 4A and 4B (total 1,586.95; third-party 865.64; EMI sum 42.12 recomputed); AOC-1 p.58-59 (Alltrak 1.00 / 23.99 / 415.92 / 199.64; Healthcare 583.87; Team (5.51)); auditor's Other Matter 238.32 and 172.40 (p.98); Note 29 goodwill 80.74 + 5.48 + 148.40 = 234.62; MD&A p.13-14 (state split 29.40% and 26.83%; EBITDA 2,846.36; ROE 61.81%; ROCE 40.00%; concentration); workforce 6,338, 4,052, 2,286, 2,589, 4,156, 3,851 (p.18); ESOP pool 5,64,000; IPO 49,68,000 shares and 9,389.52. Note 9 rows sum to 320.23 against 659.33 (gap 339.10), re-added and correct. Note 22 row sum 3,913.90 correct. DuPont, interest cover, net debt to EBITDA, growth splits recomputed.

Stage 2 and 3 (RHP): restatement Annexure V p.193 (553.23 to 224.67; 388.05 unbilled); KPI p.103; Alltrak RPT p.216 (130.33 / 869.38 / 1,416.34; 374.17 / 348.69 / 574.03); SPA text p.153 (Healthcare 11,45,20,000; Rs 11,440; Team 6,00,000; Alltrak 1,00,000 at Rs 10); objects of the issue (2,680.00; 3,700.00; 1,250.00; 231.90; 73.08); debtor days table (3,667.16; 5,052.02; 7,126.56).

Stage 4 (decks): listing deck slide 6 mix, slides 21 to 25 statements; H1 deck slides 18, 20, 21, 22, 23. All percentages recomputed (34.17%, 39.51%, 12.87%, 23.12%, 11.5%, 72.1%).

Stage 5 (call): quotes and numbers at call markers p.5, p.7, p.8, p.9, p.10, p.11, p.12, p.13, p.14, p.16, p.17, p.18 against the .txt (OCR). Press release p.2 to p.4 values (138.09; 90.03; 124.13; 80.60%; 81.76%; 84.20%; 6,789; 320 plus; 28.00; 8.75%; 74.20; 21.62) match. IPO Annexure A table (63.80, 5.31, 6.00, 8.92, 12.17, 10.34, 3.00, 93.90, 21.65, 72.25) matches the page image. Derived H2 need 181.91 and growth 46.5% and 31.7% re-derived.

Stage 6 (peers): sampled quotes and pages in KRYSTAL Nov 2026 (118 days p.7; 46.25%; 6.25 to 7.5% p.9; margin dip p.7), TCIEXP Nov 2026 (59 / 32 days p.5; 12.7% p.3; 15-16% p.13), THYROCARE Feb 2026 (market 10-11% p.16; in-house fleet p.8; Vimta credit p.9; 60 to 90 days p.17), THYROCARE Nov 2026 (PharmEasy 11% p.11; 2,100 phlebotomists), KRYSTAL May 2025 (management fee on CTC; negative operating cash flow). All found at the cited pages.

Stage 7: scorecard sum 10.5 re-added; inputs match B01, B03, B04, B05 and the H1 deck pages cited.

Stage 8: voting result 12,913,500 / 11,616,300 / 499,800 / 797,400 / 1,176 holders; both XBRL dates (63.75%, no pledge); AIF 5.41%; Kartavya terms (Rs 4,50,00,000; nil to 25 Nov 2026; 12% from 26 Nov; up to 26%); CFO change 18 Sep 2026; CEO designation in the H1 results filing; education and ages in RHP; restatement cuts 59.4% and 21.8% re-derived.

Stage 9: AR p.8 and RHP p.116-118 market sizes (USD 11.07, 16.50, 18.50, 31.50 Bn; 20.48 Bn MarkNtel); deck p.16 (11.8 Bn; 20.1 Bn; 399.3 Mn to 1.09 Bn; 13.4%); call p.13 quote; arithmetic re-run (13.8% forward CAGR, 304 and 404 Cr SOM, 15.0% CAGR).

## Coverage statement

Mandatory tier (rule 2, OR-32): there is no verdict card, no Section 1B pillar input and no stage 13 output among the reports in front of me, so the tier is the Gate 0 scorecard inputs. Counting rule: every input value that a Gate 0 score reads, as stated in 01-gate0.md. That is 48 base-table values (16 rows by 3 years; the "Inventory none" row is a nil and not counted), 4 Block E inputs (E1 63.75%, E2 100%, E3 pledge false, E4 62.11), 1 net-block input (1,457.08 for M3) and 3 M8 reach figures. mandatory_total 56. mandatory_checked 56. Unchecked: none. One of the 56 (E2) is a MAJOR anchor finding with the number itself correct.

Sample tier: I counted 420 material numbers in the sample tier. A number counted as material if it feeds a flag, a score, a stated ratio, a guidance row, a promise-delivery row, a table cell used for a judgment, or a load-bearing fact. I checked about 244 of the 420 (58%), about 300 figures in all with the mandatory tier. Work order was: load-bearing facts and flags first, then tables that feed judgments, then other table cells. The count is approximate because many table rows share one source cell.

Not checked, with reason:
- Web-sourced numbers in 08-promoter.md and 09-tam.md (Qorpiq, EMIS, Tofler, TheCompanyCheck, People Matters, Business Today, 5paisa; anchor investors Rs 26.5 crore; listing gain and subscription 142 to 153 times; Dr Lal 2,763 Cr and cost ratio 14.5%; Metropolis, Vijaya, Krsnaa revenue; CareEdge 17% organised share; FX 95.2492; Credence USD 900 Mn). The source is the open web, not among my inputs. Stage 8 and 9 mark them UNVERIFIED or web. This is a coverage shortfall, not a clean pass.
- Peer Data_Sheet CSVs (THYROCARE, TCIEXP, KRYSTAL): no report cites a figure from them.
- Most peer transcript content beyond the quotes listed above. Stage 6 has about 120 quoted numbers. I sampled 24 and all matched.
- CREDENT_08112026013152_Intimation_for_Investor_Call.pdf (image-only): no report cites a figure from it.
- Auditor appointment filing, AGM filing, 5 Sep board outcome and 4 Nov board outcome: only the facts quoted in stages 3, 5 and 8 were checked (voting, CFO change, Kartavya).
- Stage 2 pass 1 to 3 detail below the Top 15 (for example CARO clause wording, Annexure A line items) was checked where it feeds a flag, not line by line.
- RHP page anchors in stage 5 that use the printed folio (for example "RHP p.88-89 printed") are labelled printed by the report; I did not re-map each one.

acceptance_rate: about 9 flawed numbers or anchors among about 300 checked figures, 97% clean. The REWORK trigger needs a CONFIRMED CRITICAL or a rate below 60% on 4 or more. Neither applies.

Source-fidelity gate note: findings 1 to 8 are marked source_fidelity true. They stand until the source PDF at a correct anchor shows the number exists there. For findings 1, 4, 5, 6, 7 the number does exist in the source at a different page, so the fix is a corrected anchor, and the clearance would be logged as a disagreement.

```yaml
stage: B12a
company: "CREDENT"
run_date: "2026-11-12"
model: claude-sonnet-5-5
status: complete
numbers_checked: 300
mandatory_checked: 56
mandatory_total: 56
findings:
  - {severity: "MAJOR", location: "01-gate0.md Block E E2 (mandatory input)", claimed: "100% promoter holding at 7 Aug 2024, Ashok Kumar Sharma 50% and Karan Sharma 50%, anchored RHP p.76 (report states .txt page markers)", source_truth: "RHP marker p.76 does not hold the table. It is on marker p.80 (txt lines 5531-5540): 10,00,000 each, 50.00%, total 20,00,000 100.00%, footnote 7 Aug 2024. Printed folio of that page is 76", note: "Number correct; anchor wrong under the report's own stated convention. Score unaffected", source_fidelity: true}
  - {severity: "MAJOR", location: "03-ardeep.md Phase 3A bullet on H1 FY27 half", claimed: "purchase of fixed assets and FD placement 636.67 (H1 cash flow, OCR-read)", source_truth: "H1 results PDF p.6 image: Purchase of Fixed Assets incl CWIP (443.12); Investment in FD / Redeem (656.67); net investing (1,091.67)", note: "OCR read 63667; image shows 656.67. 636.67 matches neither line", source_fidelity: true}
  - {severity: "MAJOR", location: "03-ardeep.md LB4 bullet 3, Phase 3A cash pile, Phase 8 strength 3; carried to 04-bizmodel.md 4A", claimed: "H1 balance sheet cash 6,919.72 at 30 Sep 2026", source_truth: "H1 results PDF p.4 image: Cash and Bank Balances 7,419.72. 6,919.72 is cash and cash equivalents at end of period on the cash flow (p.6); gap 500.00 is fixed deposits. H1 deck p.22 cash and bank 742 Mn", note: "Number exists on the cash flow, not the balance sheet where placed; basis unlabelled at three uses; net cash understated by 500.00", source_fidelity: true}
  - {severity: "MINOR", location: "02-notes-pass1.md sections 0, 2.1, 3 (Note 1 p.79)", claimed: "standalone Note 1 basis and going concern text on AR p.79", source_truth: "AR marker p.78 (txt lines 2929-2937); consolidated p.106 correct. Stage 3 D1 already notes the slip", note: "Page off by one", source_fidelity: true}
  - {severity: "MINOR", location: "05-concall.md LB2 first bullet; 2B", claimed: "Prashant Sharma exchange on call p.14; 'wrong question' p.15; 'beautiful question' p.12", source_truth: "Marker p.15 (lines 640-646); marker p.16 (line 678); marker p.13 (line 534)", note: "Quotes exact; pages are printed folios while the report says PDF pages", source_fidelity: true}
  - {severity: "MINOR", location: "04-bizmodel.md 1B", claimed: "RHP p.27: no credit period is punched in the system (RHP line 13510)", source_truth: "RHP p.27 holds 'working capital intensive' and terminable-contract text. 'No credit period punched' is at txt line 13510 and AR Note 15 note 4 (marker p.84)", note: "Line anchor right, page label wrong", source_fidelity: true}
  - {severity: "MINOR", location: "08-promoter.md 3E, 6A row 7, 6C", claimed: "auditor change table on RHP p.68 (lines 4741-4775)", source_truth: "Marker p.72 (lines 4741-4775); printed folio 68. Dates and wording match", note: "Report mixes printed folios and markers without saying so; line numbers resolve", source_fidelity: true}
  - {severity: "MINOR", location: "09-tam.md 5E", claimed: "30.8x P/E (screener, 2026-11-12; step1 brief)", source_truth: "screener-Data_Sheet.csv has price 432.3 and market cap 787.78 Cr, no P/E field. 787.78 / 25.49 TTM PAT = 30.9x", note: "Close but not printed in the file; step1 brief is memory", source_fidelity: true}
  - {severity: "MINOR", location: "07-emoat.md G2", claimed: "receivable days 81.55 FY25 to 98.58 FY26 (B01)", source_truth: "B01 receivable days 83.85 and 100.26; 81.55 and 98.58 are working-capital days net of payables", note: "Unlabelled basis difference, not material; direction unchanged", source_fidelity: false}
critical_count: 0
major_count: 3
minor_count: 6
false_positives_struck: 7
material_universe: 476
acceptance_rate: 97
coverage_note: "Mandatory tier = Gate 0 scorecard inputs (no verdict card or Section 1B pillar exists in the reports): 56 of 56 checked (48 base-table values, E1 to E4, net block 1,457.08, three M8 reach figures); none unchecked. Sample tier: 420 material numbers counted (those feeding a flag, score, ratio, guidance or promise row, or a load-bearing fact), about 244 checked. material_universe 476 = 56 + 420. Not checked: web-sourced numbers in stages 8 and 9 (open web, not in my inputs), peer Data_Sheet CSVs (no report cites them), most peer transcript content beyond 24 sampled quotes, the image-only investor-call intimation, and stage 2 line items below the Top 15 that feed no flag. H1 FY27 results pages 4, 6 and 19 were read from the page image."
```
