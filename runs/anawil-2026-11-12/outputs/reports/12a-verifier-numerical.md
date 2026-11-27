# VERIFIER A: NUMERICAL AUDIT. ANAWIL, run 2026-11-12

Model claude-sonnet-5-5. Inputs: stage reports 01 to 09 (final stage 2 report 02-notes.md) and the page-marked source text under runs/anawil-2026-11-12/inputs/. The H1 results page 4 was also read as a PDF image because its text layer is OCR and one finding rests on it. Prospectus anchors below use the [page N] marker (printed folio is N minus 3).

## Result in one paragraph

Three MAJOR findings, five MINOR, no CRITICAL. The Gate 0 revenue CAGR is printed as 177.1% where the report's own inputs give 77.1%. That one error flips the C4 score from 0 to 5 and moves Core 61 to 66 and Grand 68 to 73, but the AVERAGE classification holds. Stage 4 prints a FY26 material cost per tower of 21.6 lakh that does not match the cited H1 results page (19.85). Everything else I checked traced to the source. The stage reports are otherwise accurate and anchor well.

## Findings table

| # | Severity | Report location | Claimed (anchor) | Source truth (location) | Note | source_fidelity |
|---|---|---|---|---|---|---|
| 1 | MAJOR | 01-gate0.md C1 (line 74); also M1 (line 113) and M11 (line 123) | Revenue CAGR FY23-FY26 = 177.1% | 77.1%. SC Data_Sheet FY23 sales 25.78; Prospectus p.173 FY26 revenue 14,326.69 lakh = 143.2669 Cr. 143.2669 / 25.78 = 5.557; cube root 1.771; CAGR 77.1% | Inputs right, result wrong by 100pp. 03-ardeep.md derives FY24-FY26 revenue CAGR 62.8% correctly. Score C1 stays 5 | true |
| 2 | MAJOR | 01-gate0.md C4 (line 77); Core 61, Grand 68 (lines 140-142, YAML) | C4 = 91.9 - 177.1 = -85.2pp, score 0; Block C 15; Core 61; Grand 68 | C4 = 91.9 - 77.1 = +14.8pp; prompts/01-gate-0-pipeline.md line 74 gives >= +3pp = 5. Block C 20; Core 66; Grand 73 | Consequence of #1. Matrix: Core 60-79 + MODERATE = GOOD, then LIMITED-history downgrade = AVERAGE, unchanged. 07-emoat.md section 6C carries 61 and 68 | true |
| 3 | MAJOR | 04-bizmodel.md 3D table, FY26 "Material cost, Rs lakh" = 21.6 (H1 Res. p.4) | 21.6 per tower | 19.85. H1 Res. p.4 FY26 audited column: materials 4,372.06 less inventory change (203.30) = 4,168.76 / 210. Page image read; AFS p.17 prints the same two values | 21.6 = restated 4,528.28 / 210 (Pros p.173). Other FY26 cells in that column are audited basis, so the column does not foot (69.9 vs revenue 68.2). On audited basis it foots (68.2). Unlabelled basis mix | true |
| 4 | MINOR | 01-gate0.md E1 (line 101) "PR p.66 post-IPO 65.26%" | page 66 shows 65.26% | 65.26% (1,63,14,162 shares) is on [page 68] (lines 4747, 4751). [page 66] shows the build-up; post-offer 70.46% ends [page 67] | Value correct and confirmed by XBRL 2026-09-30 (0.6526, 16,314,162), the primary anchor. Secondary page cite off by two | true |
| 5 | MINOR | 07-emoat.md 6C | "61 of 140 core points" | 01-gate0.md: Core 61 / 100; Grand 68 / 160 | Wrong denominator, report-to-report | false |
| 6 | MINOR | 05-concall.md 1C order book row (line 69) | Rs 359.81 Cr | 35,981.72 lakh (Pros p.114) = 359.8172 Cr, rounds to 359.82 | Same report prints 359.82 at lines 90 and 175 | false |
| 7 | MINOR | 02-notes.md P2 (line 52) | "funded by debt 7,313.88" (audited paragraph, AFS p.15) | AFS p.15 gross 5,973.82 + 1,367.30 = 7,341.12. 7,313.88 is the restated figure (Pros p.174: 9,029.27 - 2,030.05 + 314.66) | Unlabelled basis. 03-ardeep.md line 128 already flagged. FCF (8,053.92) unaffected | false |
| 8 | MINOR | 01-gate0.md header and YAML input_gaps | AFS "blank on all 103 pages" | AFS .txt has OCR text on all 103 pages (02-notes.md line 227 agrees). AFS p.15 prints CFO 1,246.69, tax 851.19, capex 9,300.61, matching the H1 Res. p.8 audited column Gate 0 used | Stale statement of input state. Gate 0 figures used are correct and labelled. No number is wrong because of it | false |

Self-check (rule 5b) on rows 1 to 3: each claimed value differs from its source truth (177.1 vs 77.1; -85.2 vs +14.8; 21.6 vs 19.85), none is a matched figure, a faithfully copied anomaly or a labelled basis difference, and none is a verdict-card or Section 1B pillar input, so MAJOR not CRITICAL. Three drafted rows were struck:
1. Gate 0 computed ROCE 26.79 / 26.25 / 16.39 against the Prospectus printed 23.05 / 21.84 / 13.68 (Pros lines 6212, 13638). Gate 0 states its basis (EBIT = PBT + finance cost; capital employed = total assets less current liabilities). Class 5a.
2. "PRES p.27" for the 12.5 CFO print. The deck prints slide number 27; the text sits on file page 28. The value and slide are right.
3. Prospectus Annexure N not-due 3,841.82 against AFS Note 16 3,841.81. Each report copy matches its own source.

## Mandatory tier (OR-32): 183 of 183 checked

Rule: every discrete figure in 01-gate0.md that feeds a block score line, a deal-breaker or the classification. Stages 02 to 09 mark no verdict-card or Section 1B pillar input, so the tier is Gate 0 only. My count by section:

| Section | Figures | Result |
|---|---|---|
| Base data table (FY23 SC, FY24-26 Pros pp.171-174 and p.213) incl. margins | 46 | all match |
| Cross-checks (screener PAT/CFO, audited PAT 3.34/13.98/35.95 Pros p.187) | 8 | all match |
| FY26 cash flow, two prints, advances (Pros p.172, 174, 206; H1 Res. p.8; Pres) | 15 | all match |
| Block A (EBIT, capital employed, ROCE, ROE, medians) | 18 | all match |
| Block B (CFO/PAT, FCF, WC-day components, sensitivity, H1 context, trend) | 32 | all match |
| Block C (CAGRs, C3, C4) | 4 | C1 and C4 WRONG |
| Block D (FY26 and Sep-26 sensitivity, H1 Res. pp.4, 6-7) | 22 | all match |
| Block E (65.26%, 16,314,162, pledge, contingent liabilities, E2 derivation) | 12 | all match (page cite off, finding 4) |
| Block F moat inputs | 23 | M1 and M11 carry the wrong 177% |
| Classification totals 61 / 7 / 68 | 3 | 61 and 68 consequential |
| Total | 183 | 6 wrong, 177 clean |

Principal confirmations: revenue, PBT, finance cost, depreciation, PAT, net worth, total assets, current liabilities, CFO and capex FY24-FY26 all match Pros pp.171-174. EBITDA 22.2228 / 29.9757 / 61.0890 match Pros p.213 Annexure ZD (2,222.28 / 2,997.57 / 6,108.90 lakh). FY26 CFO 1,843.94 restated (Pros p.174), 1,246.70 filed (H1 Res. p.8), 1,246.69 audited (AFS p.15). Sep-26 inputs match H1 Res. pp.4, 6-8 (borrowings 2,701.83 + 658.96; cash 19.61; equity 22,634.51; current assets 12,850.91; current liabilities 6,348.47; H1 EBITDA 3,608.24; H1 FY26 EBITDA 1,014.13). Promoter 65.26% and no pledge match the 2026-09-30 XBRL. Contingent liability 226.93 lakh FY24 and FY25, nil FY26, matches Pros pp.209-210. FY23 values match screener Data_Sheet.

## Sample tier

Material universe: about 600 numbers in reports 02 to 09. I counted a number as material if it feeds a stated flag, a top-findings row, a guidance or margin arithmetic chain, a ratio, or a scorecard row. I checked about 235. Method: arithmetic re-derivation for every derived chain I could close from filed numbers, plus source look-ups for the figures that carry the thesis.

- 02-notes.md (about 45 checked): AFS p.15 cash flow, Note 18 (3,003.57 / 602.44 / 59.63 / 55.28 / 1,878.59 / 827.37), Note 15 (3,930.40 / 269.92 / 1,039.64 / 81.47 / 90.29 / 8.45), capital creditors 1,036.39 / 203.51, bank-return table (2,146.40 / 3,524.13 / 4,820.04 / 248.74; 1,134.23 / 3,043.06 / 3,592.03 / 302.51), Note 38 printed ratios (1.10, 3.94, 117.56), Darpan FY24 flows in INR thousand (1,74,863.72; 39,901.15; 58,847.38; 13,291.36), FY24 audited bridge (revenue 5,40,664.72; PAT 33,355.21; CFO 68,163.36; tax paid 2,402.17), the P2 reconstruction (2,814.94, 3,114.75, 10,868.86, 8,053.92, 78.3%, 85.0%), the 7 tie-outs on H2 FY26 margin (5,108.87; 50.1%; 93.3%), and the 115BAB demand (Pros pp.240-241). All match except finding 7.
- 03-ardeep.md (about 60): ratio table (net debt 12,665.05, EBITDA/finance cost 10.58 and 5.11, current ratio 1.40 / 1.53, quick 0.91, ROE 55.2%, D/E 1.35), P&L walk, cash-flow table (FCF, CFO/EBITDA, capex/depreciation), cumulative 5,053.24 / 6,432.35 / 15,355.09, RPT map, Pros p.23-24 concentration and seasonality (70.50 / 80.23 / 71.12%), RF37 516.76 / 4.03%, CRISIL 292 / 226 / 99 days, shareholding XBRL items (AIF 25,02,000 10.01%; locked 5,96,000; DII 10.23%), OFS and private placement arithmetic. All match.
- 04-bizmodel.md (about 30): order-book mix tie (202.9 / 395.58 = 51.29%), conversion fee 58.73 and 58.74 lakh, Model 3 EBITDA share, unit-economics table (one error, finding 3), incremental margins, net trade working capital 92.9 / 100.7, Prospectus ROCE 23.05% and EBITDA margin 42.64% (Pros pp.113, 229).
- 05-concall.md (about 20): growth rates 272.2 / 255.8 / 539.3%, press-release items (395.58, 450-500, 55-60, 64.3 / 21.2 / 10.8 / 3.7, 32.82, 104.7%, 14.8%), implied bases 16.03 and 28.59, guidance arithmetic. One rounding slip (finding 6).
- 06-peers.md (10 spot checks of transcript quotes, all located in the files): Inox 70% / 70-75% / 25%; Suzlon 35-40 vs 60-65 and 1.5-1.65x, "crossed 59 gigawatts", "record 6.34", "8 gigawatt in '27"; KP Green 40/60 and 37/63, 2% royalty, 4,00,500 tpa, 30-34% utilisation. All match.
- 07-emoat.md (about 30): scorecard sum 10.8, Section 5 multipliers, blend margins 23.4% / 27.7%, order-book roll-forward (379 - 107 + 38 + 10 = 320; 153.7 vs 153.97), BoB sanctions 13.85 + 21.69 + 48.50 = 84.04, Kutch land areas, attrition 56.79 / 29.03 / 8.28%, 99.75% indigenous, 25.04% to 20.03% manufacturing cost, capacity 93,600 / 1,47,000, CRISIL 84% limit use. Finding 5.
- 08-promoter.md (about 20): RPT table (Pros pp.50-51: 338.15, 498.71, 1,389.52 / 1,574.57, 1,018.67 / 551.00, 108.50 / 576.17, 97.60, 127.67, 32.22, 87.27, CMD 1,442.24 / 1,039.58 and balances 311.29 / 12.09 / 414.75), pay table, KMP dates, promoter holdings 88.38 / 64.50 / 89.35 / 65.26, OFS 13,00,800 x Rs 270 = Rs 35.12 Cr, 7,20,000 x Rs 101 = Rs 7.27 Cr. All match.
- 09-tam.md (about 20): Prospectus-sourced items (25,406 MW p.100; RPO 3.36 / 6.94% pp.102-103; 18 GW p.104; 48.17% p.111) and the arithmetic chain (CAGR 49.3% and 35.1%, SAM 35.8%, price per MW 1.068 / 1.111, PAT margin 12.1%, earnings CAGR 17.0%). All match.

Not checked: the web-sourced stage 9 figures (IWTMA, MNRE, JMK, SolarQuarter and similar are not in my inputs), stage 8 aggregator and media items, the other peer transcript quotes, and the remaining 02 and 03 AFS note cells not named above.

## Observations that are not findings

- Three versions of FY26 total assets exist and each report names its basis: 29,162.45 restated (Pros p.172), 29,159.89 audited (AFS p.16), 29,145.43 in the H1 results March column (H1 Res. p.7, deferred tax asset shown as a liability). Gate 0 uses the restated figure and says so.
- The Prospectus itself prints two post-offer promoter figures, 70.46% (build-up table, [page 67]) and 65.26% (section 17, [page 68]); 65.26% agrees with the XBRL. Karnataka FY25 appears as 99.55% (line 1667) and 99.95% (line 7669). The reports copy these faithfully.
- The 2026-08-07 shareholding XBRL is dated 2026-08-10 inside the file; Gate 0 cites the 2026-09-30 file for 30-Sep-2026, and that file shows 0.6526.

```yaml
stage: B12a
company: "ANAWIL"
run_date: "2026-11-12"
model: claude-sonnet-5-5
status: complete
numbers_checked: 418
mandatory_checked: 183
mandatory_total: 183
findings:
  - {severity: "MAJOR", location: "01-gate0.md Block C line C1 (line 74); repeated in M1 (line 113) and M11 (line 123)", claimed: "Revenue CAGR FY23-FY26 = 177.1% (formula (143.2669/25.78)^(1/3)-1)", source_truth: "77.1%. Inputs are correct (SC Data_Sheet FY23 sales 25.78; Prospectus p.173 FY26 revenue 14326.69 lakh = 143.2669 Cr); 143.2669/25.78 = 5.557, cube root = 1.771, so CAGR = 77.1%. Stage 3 cross-read of FY24-FY26 CAGR (62.8%) confirms the scale.", note: "Gate 0 mandatory input. Score line C1 stays 5 (>=20%) but the printed value is wrong by 100pp.", source_fidelity: true}
  - {severity: "MAJOR", location: "01-gate0.md Block C line C4 (line 77); flows to Core score 61, Block C 15, Grand total 68 (lines 140-142 and YAML)", claimed: "C4 = 91.9 - 177.1 = -85.2pp, score 0; Block C = 15; Core 61; Grand 68", source_truth: "C4 = 91.9 - 77.1 = +14.8pp, which is >= +3pp under prompts/01-gate-0-pipeline.md line 74, score 5. Block C = 20; Core = 66; Grand = 73. Classification matrix result unchanged (Core 60-79 + MODERATE = GOOD, LIMITED history one tier down = AVERAGE).", note: "Consequence of the C1 error. Value and score are wrong on the report's own stated inputs. 07-emoat.md section 6C repeats Core 61 and Grand 68.", source_fidelity: true}
  - {severity: "MAJOR", location: "04-bizmodel.md section 3D unit-economics table, FY26 column, 'Material cost, Rs lakh' = 21.6 (anchor: H1 Res. p.4)", claimed: "21.6 lakh per tower (FY26)", source_truth: "19.85 lakh per tower on the cited source: H1 Res. p.4 FY26 audited column cost of materials 4,372.06 less inventory change (203.30) = 4,168.76 lakh / 210 towers (page image read; AFS p.17 prints the same 4,372.06 and -203.30). 21.6 equals the Prospectus RESTATED basis 4,528.28 / 210 (Pros p.173).", note: "Mixed basis inside one column, unlabelled: other FY26 cells (other expense 17.2, employee 2.0, EBITDA 29.1) are audited basis. Column does not foot to revenue 68.2 (21.6+17.2+2.0+29.1 = 69.9); on audited basis 19.85+17.26+1.96+29.16 = 68.2.", source_fidelity: true}
  - {severity: "MINOR", location: "01-gate0.md Block E line E1 (line 101): 'PR p.66 post-IPO 65.26%'", claimed: "Prospectus page 66 shows post-IPO promoter holding 65.26%", source_truth: "[page 66] holds the capital build-up; the Grand Total row printing post-offer 70.46% sits at the end of [page 67] (line 4697). 65.26% (1,63,14,162 shares) is printed on [page 68] (section 17 pre/post IPO table, lines 4747 and 4751). The value 65.26% is correct and is also confirmed by the 2026-09-30 XBRL file, which is the primary anchor.", note: "Secondary page citation is wrong by two pages. Number exists in the source.", source_fidelity: true}
  - {severity: "MINOR", location: "07-emoat.md section 6C 'Gate 0 core score = 61 of 140 core points'", claimed: "61 of 140", source_truth: "01-gate0.md prints 'Core score: 61 / 100' (blocks A-E, 5 x 20) and 'Grand total 68 / 160' (100 + 60 moat points).", note: "Wrong denominator in a report-to-report carry. Not a PDF number.", source_fidelity: false}
  - {severity: "MINOR", location: "05-concall.md section 1C table, Order book row (line 69): 'Rs 359.81 Cr, 379 towers'", claimed: "Rs 359.81 Cr", source_truth: "Pros p.114 (printed 35,981.72 lakh) = Rs 359.8172 Cr, rounds to 359.82. The same report prints 359.82 in section 2A (line 90) and section 3D (line 175).", note: "Rounding slip, internal inconsistency only.", source_fidelity: false}
  - {severity: "MINOR", location: "02-notes.md section P2 (line 52): 'funded by debt 7,313.88 and equity 1,280.75' in a paragraph on the audited basis (anchor AFS p.15)", claimed: "7,313.88 lakh debt", source_truth: "AFS p.15 shows 5,973.82 + 1,367.30 = 7,341.12. 7,313.88 is the RESTATED figure (Pros p.174: 9,029.27 - 2,030.05 + 314.66; also balance-sheet debt movement 12,824.76 less 5,510.88).", note: "Unlabelled basis difference. Stage 3 (03-ardeep.md line 128) already flagged the 27.24 gap. FCF (8,053.92) is unaffected.", source_fidelity: false}
  - {severity: "MINOR", location: "01-gate0.md header (line 5) and YAML input_gaps: 'FY2025-26 audited statements file is blank on all 103 pages'", claimed: "AFS text blank on all 103 pages", source_truth: "Audited_Financial_Statements_FY2025-26.txt carries OCR text on all 103 pages (stage 2 final, 02-notes.md line 227, confirms). AFS p.15 prints FY26 CFO 1,246.69, tax paid 851.19, capex 9,300.61, which agree with the H1 Res. p.8 audited column Gate 0 used (1,246.70, 851.19, 9,300.61).", note: "Stale statement of input state; the Gate 0 numbers drawn from Prospectus restated and H1 Res. are all correct and labelled. Not a number finding.", source_fidelity: false}
critical_count: 0
major_count: 3
minor_count: 5
false_positives_struck: 3
material_universe: 600
acceptance_rate: 97
coverage_note: "MANDATORY TIER: 183 of 183 checked (my count; rule: every discrete figure in 01-gate0.md that feeds a block score line, deal-breaker or the classification, including all base-data table cells, FY26 cash-flow prints, ROCE/ROE, WC-day components, Block D FY26 and Sep-26 sensitivity inputs, Block E holding/pledge/derivation inputs, moat-test inputs, and the 61/7/68 totals). Evidence-stage reports 02-09 mark no verdict-card or Section 1B pillar input, so the tier is Gate 0 only. Six mandatory figures are wrong (C1 177.1%, C4 -85.2pp, M1 177%, M11 177%, Core 61, Grand 68, all one root cause); 177 clean. Source pages used: Prospectus text layer pp.64-68, 171-174, 187, 205-206, 209-210, 213; H1 results (OCR, page 4 confirmed against the PDF image); AFS pp.15-17, 22-27, 35, 37 and FY24 thousand-unit pages; screener Data_Sheet; XBRL 2026-09-30 and 2026-08-07; CRISIL; H1 deck; press release. SAMPLE TIER: about 600 material numbers counted in reports 02-09 (material = a figure that feeds a stated flag, finding rank, guidance or margin arithmetic, ratio, or a table cell in a top-findings row); about 235 checked, concentrated on 02 (45), 03 (60), 04 (30), 05 (20), 06 peer quotes (10), 07 (30), 08 (20), 09 prospectus-sourced and arithmetic figures (20). numbers_checked 418 = 183 + about 235 (approximate for the sample tier). NOT CHECKED: stage 09 web-sourced figures (IWTMA, MNRE, JMK, Devdiscourse and similar; not among my inputs), stage 08 web and aggregator items (qorpiq.com, Chittorgarh, AmbitionBox), most peer-transcript quotes beyond ten spot checks (all ten matched), and the remaining 02 and 03 AFS note cells not named above. Anchor convention note: stages 3/4/5/7 mix [page N] marker anchors with printed slide numbers (Pres p.N); the tower-count and CFO chart pages resolved correctly under either reading. Struck before emit (3): Gate 0 ROCE computed 26.79/26.25/16.39 versus Prospectus printed 23.05/21.84/13.68 (basis labelled in Gate 0, class 5a); 'PRES p.27' (the deck prints slide number 27 = file page 28); Pros Annexure N not-due 3,841.82 versus AFS 3,841.81 (both faithfully transcribed). Gate 0 score effect of the C4 correction (Core 61 to 66, Grand 68 to 73) does not change the AVERAGE classification; Verifier C owns rule application."
```
