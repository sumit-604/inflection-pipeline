# VERIFIER C: FRAMEWORK ADHERENCE, PHASE 1 SCOPE. MMP, run date 2026-10-05

Run folder: runs/mmp-2026-10-04. Model: claude-opus-5-5 (effort xhigh, per .claude/agents/verifier-c-framework.md).
Scope: Gate 0 (B01 run 2) and Emerging Moat (B07 run 2) only. The valuation audit is pending phase 3 (Section 7).

Rule sources (the only two): prompts/01-gate-0-pipeline.md (cited "G0 prompt") and prompts/07-emerging-moat-pipeline.md (cited "S7 prompt"). Output shape: prompts/12-verifiers-pipeline.md, Verifier C section.
Artifacts audited: outputs/reports/01-gate0.md, outputs/blocks/B01-gate0.yaml, outputs/reports/07-emoat.md, outputs/blocks/B07-emoat.yaml.
Sources opened to re-derive scores and test basis choices: inputs/screening/screener-Data_Sheet.csv, APARINDS-Data_Sheet.csv, ARFIN-Data_Sheet.csv, MAANALU-Data_Sheet.csv; inputs/annual-report/Annual_Report_2026.txt (consolidated cash flow p.173, energy p.43, borrowings note p.204); inputs/annual-report/Annual_Report_2025.txt (consolidated cash flow p.156, Note 16(d) p.112, shareholding pattern p.67).
Units: Rs Cr unless marked L (Rs Lakh). The AR statements are in Rs Lakh on their face ("in Lakhs", AR26 p.173 heading).
Independence: I read no other verifier output and no earlier B12c.

Verifier A owns source fidelity. This audit judges rule application. I recompute from the inputs the artifacts state. I open a source only to test a basis choice.

---

## 1. RESULT

- Rules checked: 90 (Gate 0: 54, Emerging Moat: 36). Passed: 86. Acceptance rate 95.6%.
- Findings: 0 CRITICAL, 3 MAJOR, 3 MINOR.
- No finding changes a classification. Gate 0 stays AVERAGE. EM stays NONE at 11.6. Combined stays AVERAGE.
- Three emitted fields change if the MAJOR findings stand:
  - B01 blocks.B 14 to 10 and core_score 54 to 50 (F1).
  - B01 moat_score 12 to 10, moats_confirmed 2 to 1, moat_class MODERATE to THIN (F2).
  - B07 capex_embedded_growth_pct 20.4 to 8.7 (F5).
- REWORK gate: not triggered. The acceptance rate is 95.6% on a denominator of 90.

---

## 2. GATE 0 (B01 RUN 2) COMPLIANCE

Every block score was re-derived from the stated inputs with the G0 prompt thresholds. Data_Sheet references are rows of screener-Data_Sheet.csv (r11 Sales, r12 Raw Material Cost, r13 Change in Inventory, r17 Selling and admin, r21 Interest, r22 PBT, r24 Net profit, r39-r40 equity and reserves, r41 Borrowings, r43 Total, r44 Net Block, r51 Cash, r57 CFO).

| # | Rule (G0 prompt) | B01 value | Verifier C re-derivation | Result |
|---|---|---|---|---|
| GZ-01 | Rule 6 opening line | "Data available: 10 years (FY2017 to FY2026). Scoring adapted to 10-year history." | Data_Sheet holds 10 annual columns, FY2017 to FY2026 (r10) | PASS |
| GZ-02 | Rule 6: minimum 3 years, maximum whatever exists | A1, A2, A4, B2, B3, B4, M12 on FY24-FY26; the rest on FY17-FY26 | Each window meets the 3-year minimum. Current liabilities, payables and capex lines exist only in AR25/AR26 (FY24-FY26); the Data_Sheet has no such rows | PASS |
| GZ-03 | Rule 4: anchor on every number | Anchored | 25 scored lines spot-checked; each carries (screener-data) or an AR page | PASS |
| GZ-04 | Rule 5: NOT FOUND scores 0 | E2 start point, M7 player count, M8 reach scored 0 | AR25 Note 16(d) p.112 gives 31-Mar-2025 and 31-Mar-2024 only (both 74.48%); no earlier promoter figure in the inputs | PASS |
| GZ-05 | ROCE: use source figure, else compute and say "computed" | Computed, stated | Data_Sheet has no ROCE row | PASS |
| GZ-06 | Formulas fixed, "do not substitute alternatives" | Proxy EBIT/(equity+reserves+borrowings) shown, not scored | Correct | PASS |
| GZ-07 | ROE = PAT / average net worth; FY17 closing stated | 10 values listed | Recomputed all 10 (r24, r39, r40): 31.55, 24.40, 16.44, 10.20, 8.73, 12.97, 8.61, 11.59, 12.70, 9.26%. Match | PASS |
| GZ-08 | WC days formula, basis stated | Revenue basis stated | Correct | PASS |
| GZ-09 | FCF = CFO - Capex; capex = purchase of PPE + intangibles; exclude acquisitions | PPE line only | **FAIL, F1.** Recomputed FCF 0.43, 4.76, -2.50 Cr; B2 2, B3 0, Block B 10, core 50 | **FAIL** |
| GZ-10 | CAGR = (End/Start)^(1/years) - 1 | 9-year windows | Correct | PASS |
| GZ-11 | CAGR edge rules | No negative endpoint; "No loss-to-profit PAT swing" noted; C4 computed | All ten PAT values positive (r24) | PASS |
| GZ-12 | A1 median ROCE | 14.74% = 1 | FY24 46.81/317.61 = 14.74%; FY25 61.30/375.94 = 16.31%; FY26 53.40/413.63 = 12.91%; median 14.74%, band 10-14.9 = 1 | PASS |
| GZ-13 | A2 minimum ROCE | 12.91% = 3 | Band 12-14.9 = 3 | PASS |
| GZ-14 | A3 median ROE | 12.15% = 2 | Median of 10 = (11.59 + 12.70)/2 = 12.15%, band 12-14.9 = 2 | PASS |
| GZ-15 | A4 ROCE trend | -1.83pp = 3 | 12.91 - 14.74 = -1.83pp, band 1-3pp = 3 | PASS |
| GZ-16 | Block A total | 9 | 1 + 3 + 2 + 3 = 9 | PASS |
| GZ-17 | B1 cumulative CFO / PAT | 1.21 = 5 | 297.83 / 246.72 = 1.21 (r57, r24, FY17-FY26) | PASS |
| GZ-18 | B2 FCF-positive years | 3 of 3 = 5 | PASS on the stated capex. Under F1: 2 of 3 = 2 | PASS |
| GZ-19 | B3 cumulative FCF / PAT | 0.33 = 1 | 33.07 / 101.53 = 0.33. PASS on the stated capex. Under F1: 2.69 / 101.53 = 0.03 = 0 | PASS |
| GZ-20 | B4 change in WC days | -2.5 days = 3 | FY24 36.00 + 70.03 - 14.66 = 91.37; FY26 39.36 + 70.03 - 20.47 = 88.92; -2.45, band within 5 days = 3 | PASS |
| GZ-21 | C1 revenue CAGR | 16.8% = 4 | (824.00 / 203.22)^(1/9) - 1 = 16.83% (r11) | PASS |
| GZ-22 | C2 PAT CAGR | 6.8% = 1 | (31.01 / 17.21)^(1/9) - 1 = 6.76% (r24) | PASS |
| GZ-23 | C3 positive revenue years | 7 of 9 = 3 | FY20 and FY21 declined (r11); 77.8%, band 75-99 = 3 | PASS |
| GZ-24 | C4 PAT CAGR minus revenue CAGR | -10.1pp = 0 | -10.07pp, band below -8pp = 0 | PASS |
| GZ-25 | D1 net debt / EBITDA | 2.81x = 1 | 182.51 / 64.94 = 2.81x; on Data_Sheet EBITDA 65.27 it is 2.80x; same band 2-3x = 1 | PASS |
| GZ-26 | D2 EBIT / interest | 4.01x = 2 | 53.40 / 13.33 = 4.01x, band 3-4.9 = 2 | PASS |
| GZ-27 | D3 debt / equity | 0.53 = 3 | 184.52 / 346.51 = 0.53, band 0.5-1.0 = 3 | PASS |
| GZ-28 | D4 current ratio | 1.26 = 2 | 26,543.14 / 21,130.77 L = 1.26, band 1.2-1.49 = 2 | PASS |
| GZ-29 | E1 promoter holding | 74.49% = 5 | Band 60% or more = 5 | PASS |
| GZ-30 | E2 promoter change over 3 years | NOT FOUND = 0 | Rule 5. The evidenced 27 months sit under the rule 6 3-year minimum | PASS |
| GZ-31 | E3 pledge | 0% = 5 | Correct | PASS |
| GZ-32 | E4 contingent liabilities / net worth | 1.29% = 5 | 445.72 / 34,650.78 L = 1.29%. Consolidated basis on both sides. Guarantees for subsidiaries drop out on consolidation; capital commitments are not contingent liabilities | PASS |
| GZ-33 | Core score | 54 | 9 + 14 + 8 + 8 + 15 = 54 | PASS |
| GZ-34 | M1 pricing power | 1 | FY17 EBITDA 20.78 / 203.22 = 10.23% to FY26 7.92% = -2.31pp, CAGR 16.8%: "declined 2-5pp despite growth" = 1 | PASS |
| GZ-35 | M2 cost vs peer median | 1 | Peer EBITDA margins recomputed from each Data_Sheet: Apar 1,921.79 / 22,902.12 = 8.39%, Arfin 46.16 / 617.99 = 7.47%, Maan 20.12 / 808.71 = 2.49%; each reconciles to its PBT. Median 7.47%; MMP +0.45pp = 1 | PASS |
| GZ-36 | M3 capital efficiency | 1 | FAT 824.00 / 250.23 = 3.29x (r44); ROCE 12.91%: "FAT >1x AND ROCE >12%" = 1 | PASS |
| GZ-37 | M4 customer stickiness | 1 | 2 decline years, CAGR positive = 1 | PASS |
| GZ-38 | M5 scale and dominance | 3 | Market cap rank 3 of 4, EBITDA margin rank 2 of 4: "top 3 mcap AND margin top 2" = 3. See O1 | PASS |
| GZ-39 | M6 technology / R&D | 0 | No R&D spend (AR26 p.44) = 0 | PASS |
| GZ-40 | M7 regulatory | 0 | Player count NOT FOUND = 0 | PASS |
| GZ-41 | M8 distribution | 0 | Reach NOT FOUND = 0 | PASS |
| GZ-42 | M9 band on the stated proxy | 3 | MMP 175.33 / 824.00 = 21.28%; Apar 17.92%, Arfin 12.16%, Maan 10.97%; median 12.16%; gap 9.12pp, CAGR 16.8%: "5pp above AND 8%" = 3 | PASS |
| GZ-43 | M9 proxy basis: "(Revenue - Material Cost)" | Raw Material Cost line, change in inventory excluded | **FAIL, F2.** Recomputed gap 3.56pp; M9 1; moats 1 (M5); THIN; moat 10 | **FAIL** |
| GZ-44 | M10 switching costs | 1 | Overall growth, 2 decline years = 1 | PASS |
| GZ-45 | M11 network effects | 1 | Latest 3-yr CAGR 15.25% < prior 30.57%; selling and admin 9.29 / 538.29 = 1.73% (FY23) to 15.96 / 824.00 = 1.94% (FY26), rising; growth above 15% = 1 | PASS |
| GZ-46 | M12 negative WC / float | 0 | 91.4, 104.1, 88.9 days, all above 45 = 0 | PASS |
| GZ-47 | Moat count and class | 12/60, 2 present, MODERATE | PASS on the stated scores. Under F2: 10/60, 1 present (M5), THIN | PASS |
| GZ-48 | Grand total | 66 | 54 + 12 = 66 | PASS |
| GZ-49 | Data confidence tier | 10 years, full, no downgrade | The tier keys to data years (rule 6 opener; YAML data_years). 10 years = "10+ yrs full" | PASS |
| GZ-50 | Classification matrix | AVERAGE | Core 40-59 = AVERAGE; the moat class does not enter this row | PASS |
| GZ-51 | Deal-breakers 1 to 9 | None | Block A 9 (not <8); Block B 14 (not <8); median ROCE 14.74% (not <10%); CFO/PAT 1.21; pledge 0%; ND/EBITDA 2.81x with IC 4.01x; revenue fell in 2 of 9 years; PAT positive FY24-FY26; history 10 years. None trips | PASS |
| GZ-52 | FLAG-GATE0 when classification is AVERAGE or lower with depressors | Raised | Correct | PASS |
| GZ-53 | Dashboard elements | All blocks, anchors, moat bars, classification box, strongest/weakest, decision line | All present | PASS |
| GZ-54 | YAML block shape | Template keys, data_notes (proxy bases, PEER DATA NEEDED), block_b_trend, analyst_note | All keys present; model claude-sonnet-5-5 matches the template; analyst_note about 136 words, under the 200 cap | PASS |

Gate 0: 54 rules checked, 52 PASS, 2 FAIL (GZ-09, GZ-43).

### 2a. Verifier C reading of the five B01 open rulings

B01 lists five open rulings and the score under each other reading. The open-ruling table is honest and complete for those five. Here is how the G0 prompt text reads on each. The operator still decides.

| Open ruling | B01 primary | What the G0 prompt text says | Verifier C reading |
|---|---|---|---|
| Rule 6 scope | Per metric | "Use whatever history is available: minimum 3 years, maximum whatever exists." Each per-metric window meets the 3-year minimum. | Primary is as written. The full-window reading zeroes metrics that meet the minimum. The text does not require that. The core 38 AVOID path has no textual support. |
| ROCE proxy | Not admitted | "FORMULA DEFINITIONS (fixed, do not substitute alternatives)." | Not a live reading. |
| Confidence tier key | 10-year history | The tier keys to data years: rule 6 opener "Data available: [X] years", YAML data_years. No per-metric tier exists in the text. | Primary is as written. The LIMITED/AVOID path has no textual support. The text did not foresee mixed windows, so the operator may still rule. A "may not have seen full cycle" note on the FY24-FY26 metrics fits the spirit of the 5-6 year tier, without a downgrade. |
| Capex definition | PPE line | "Purchase of PPE + intangibles ... exclude acquisitions." | The text supports PPE + CWIP + capital advances. See F1. |
| E2 window | NOT FOUND = 0 | Rule 5: a missing data point scores 0. Rule 6 minimum is 3 years. | Primary is as written. 27 months is under the minimum. |

Under the text, neither AVOID path holds. The as-written Gate 0 result is AVERAGE, core 50 (F1), moat 10/60 THIN (F2).

---

## 3. EMERGING MOAT (B07 RUN 2) COMPLIANCE

| # | Rule (S7 prompt, and Verifier C rules 3 and 8) | B07 value | Verifier C check | Result |
|---|---|---|---|---|
| EM-01 | Six sections plus register, one response | 1 to 6 plus Optionality Register | All present, in order | PASS |
| EM-02 | Rule 2: evidence tag on every evidence item | Tags on items | Correct | PASS |
| EM-03 | Rule 3: source anchor on every evidence item | Most anchored to source pages | **FAIL, F6.** Five items anchor to upstream records or to unpaged notes | **FAIL** |
| EM-04 | Rules 4-5: NO EVIDENCE FOUND, no force-fit | 13 of 22 categories marked NO EVIDENCE FOUND | Correct | PASS |
| EM-05 | Rule 6: completionist guard | 9 active categories (under 12); recount performed | Correct | PASS |
| EM-06 | 1A status vocabulary | LAUNCHED-recent, IN TRIALS, ANNOUNCED, UNDER DEVELOPMENT, CONCEPT | Correct | PASS |
| EM-07 | 1B diversification direction | 5 directions with evidence and timeline | Correct | PASS |
| EM-08 | 1C mix table | FY26 and Q1 FY27 mix; 3-year mix NOT FOUND stated | Correct | PASS |
| EM-09 | 2A capex table | Project, Rs Cr, funding, status, date, capacity, % over current | Correct | PASS |
| EM-10 | 2B utilisation | Per facility, unknowns NOT FOUND | Correct | PASS |
| EM-11 | 2C arithmetic shown | 3.196x mean FAT; 50-55 x 3.196 = 159.8-175.8; 20.4% | FAT FY22-FY26: 3.0455, 3.3665, 3.1681, 3.1083, 3.2934; mean 3.1964. 52.5 x 3.196 = 167.8; 167.8 / 824.0 = 20.36% | PASS |
| EM-12 | 2C input: "total capex under execution", consistent with stated evidence tier | Wire rod 20-25 + solar 30 = 50-55 Cr | **FAIL, F5.** Solar is claim-only in B07's own tags. Recomputed 8.7% (7.8-9.7%) | **FAIL** |
| EM-13 | 2D new geography | Nepal, Venezuela, US, Latin America, exports | Correct | PASS |
| EM-14 | 22 categories each addressed | A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, I1-I2 | 22 counted | PASS |
| EM-15 | Section 3 summary table | 22 rows; Strong or Moderate count 3 (B1, E2, H2), 0 Strong | Correct | PASS |
| EM-16 | Recount line, exact form | "📄 recount performed: 11 documented items across 7 categories" | Items listed: B1 2, B2 1, E2 3, F2 1, H2 2, H3 1, R1 1 = 11 across 7 | PASS |
| EM-17 | Category 21 (I1): above 0 only with both legs, (b) leg documented | 0; leg (a) and leg (b) both absent | Correct | PASS |
| EM-18 | Category 22 (I2): above 0 only with a specific named sacrifice | 0; tested for B1, E2, H2, insulators, powders, foils | Correct | PASS |
| EM-19 | Categories 21 and 22 present in B07 (Verifier C rule 8) | Present in Sections 3 and 5 | Correct | PASS |
| EM-20 | 4A approvals | 5 rows: body, status, timeline, unlock, competitors | Correct | PASS |
| EM-21 | 4B policy tailwinds | ADD, RDSS, MSEDCL incentive, PLI NOT FOUND; shared column | Correct | PASS |
| EM-22 | 4C regulatory moat assessment | Emerging, weak, shared | Correct | PASS |
| EM-23 | Section 5: all 23 rows | 22 categories plus R1 | 23 counted | PASS |
| EM-24 | Likelihood x impact matrix | B1 MM 2, B2 MM 2, E1 ML 1, E2 MM 2, F2 ML 1, G2 LL 1, H2 HL 2, H3 ML 1, R1 ML 1 | Each raw value matches the matrix | PASS |
| EM-25 | Evidence multipliers 1.0 / 0.7 / 0.5 | As listed | Correct | PASS |
| EM-26 | Score consistent with stated evidence tier (no claim scored as documented) | E1 claim 0.7; G2 inference 0.5; B2 blend 0.7; every 1.0 row carries documented evidence | Correct. See O3 on B2 | PASS |
| EM-27 | Adjusted total | 11.6 | 2.0 + 1.4 + 0.7 + 2.0 + 1.0 + 0.5 + 2.0 + 1.0 + 1.0 = 11.6 | PASS |
| EM-28 | Band | NONE | 11.6 < 12 = NO MEANINGFUL EMERGING MOAT | PASS |
| EM-29 | I1/I2 contribution stated separately | 0.0 | Correct | PASS |
| EM-30 | "EM >=25" UA qualifier stated | Not met | Correct | PASS |
| EM-31 | Optionality register | 8 rows, four columns, watched never scored | Matches report table and YAML | PASS |
| EM-32 | One improvement, one mechanism | FRP in B1 only; ADD in R1 only; AVL in H2 only; M9 not re-credited | No double credit found | PASS |
| EM-33 | 6A timeline and 6B risks | Four windows; six risks with early warnings | Correct | PASS |
| EM-34 | 6C uses the injected Gate 0 block | Core 54, moat 12/60, 2 moats (M5, M9), AVERAGE, MODERATE | Matches B01-gate0.yaml | PASS |
| EM-35 | 6D combined classification with TURNAROUND and HIGH POTENTIAL reasoning | AVERAGE; both tests reasoned and failed | Correct | PASS |
| EM-36 | 6E output card and YAML shape | Map, 12-month catalysts, biggest risk; YAML keys present; analyst_note about 177 words | Correct. See O4 on two extra keys | PASS |

Emerging Moat: 36 rules checked, 34 PASS, 2 FAIL (EM-03, EM-12).

---

## 4. FINDINGS

| ID | Severity | Artifact and location | Rule | Claimed | Recomputed / required | Note |
|---|---|---|---|---|---|---|
| F1 | MAJOR | B01 Block B (B2, B3); data_notes capex line; block_b_trend; open-ruling row "Capex definition"; YAML blocks.B, core_score | G0 FORMULA DEFINITIONS: "FCF = CFO - Capex (capex = purchase of PPE + intangibles from cash flow statement; exclude acquisitions)" | Capex = "Investment in Property, Plants and Equipment (Net of Disposal)" only: FY24 3,078.11 L, FY25 4,974.53 L, FY26 3,923.03 L. FCF 11.97, 7.04, 14.06 Cr. B2 5, B3 1, Block B 14, core 54 | Capex = PPE line + increase in CWIP + capital advances. FY24 3,078.11 + 1,285.85 - 131.62 = 4,232.34 L (AR25 p.156); FY25 4,974.53 + 92.28 + 135.59 = 5,202.40 L; FY26 3,923.03 + 991.83 + 663.86 = 5,578.72 L (AR26 p.173). CFO 4,275.02 / 5,678.74 / 5,328.97 L (AR25 p.156, AR26 p.173). FCF 0.43, 4.76, -2.50 Cr. B2 2 (2 of 3), B3 0 (2.69 / 101.53 = 0.03). Block B 10. Core 50. AVERAGE unchanged. Netting "Liabilities towards Capital Expenditures" (10.15, 24.38, 18.22 L) gives 0.53, 5.01, -2.32 Cr and the same scores | The rule excludes only acquisitions. Cash spent on plant under construction (CWIP) and advances paid for plant are purchases of PPE. MMP reports them on separate cash-flow lines. A company with the same cash flows on one combined line would score B 10. Under B01's reading the score depends on line layout. Support outside the two rule sources: Ind AS 7 para 16(a) counts payments for self-constructed PPE as cash paid to acquire PPE. B01 already shows this reading in its open-ruling table, so the fix is to make it primary |
| F2 | MAJOR | B01 Block F M9 row; data_notes M9 line; YAML moat_score, moats_confirmed, moat_class, grand_total | G0 M9: "GM proxy if needed: (Revenue - Material Cost) / Revenue, state proxy used" | Raw Material Cost line, change in inventory excluded. MMP 21.28%, peer median 12.16%, gap 9.12pp, M9 3. Moats 2 (M5, M9), MODERATE, moat 12, grand total 66 | Material cost for the year's sales = Raw Material Cost net of Change in Inventory. This is the basis B01 itself uses for EBITDA in M1, M2 and M5 (data_notes: "Sales - RM + change in inventory - ..."). FY26: MMP (824.00 - 648.67 + 5.97) / 824.00 = 22.00% (r11-r13); Apar (22,902.12 - 18,797.67 + 706.82) / 22,902.12 = 21.01%; Arfin (617.99 - 542.87 + 38.85) / 617.99 = 18.44%; Maan (808.71 - 719.98 + 10.30) / 808.71 = 12.25% (each Data_Sheet r11-r13). Peer median 18.44%. Gap 3.56pp, under the 5pp tier. M9 1 (above peers, below the 5pp tier; the rubric has no band for that case, and 0 applies only at or below peers). Moats 1 (M5), THIN, moat 10, grand total 64. AVERAGE unchanged | B01 states its proxy, as the rule asks. The fault is that one scorecard treats change in inventory as a cost in three margin tests and ignores it in the fourth. Arfin drives the swing: change in inventory +38.85 Cr, 6.3% of its FY26 sales, moves its proxy from 12.16% to 18.44% and makes it the median. The open-ruling table does not show this reading |
| F3 | MINOR | B01 LBF3, Block A, FLAG-GATE0 reason | Presentation: a disclosed sensitivity shown in one direction only (no G0 scoring rule broken) | FY26 EBIT 53.40 Cr includes the associates share and the exceptional fire loss 973.69 L (AR26 p.172, Note 37). Only the ex-associates sensitivity is shown (ROCE about 10.9%). FLAG-GATE0 names "FY26 ROCE 12.91% ... down from 16.31% FY25" as a depressor | Show the ex-exceptional line beside the ex-associates line: EBIT 53.40 + 9.74 = 63.14 Cr; ROCE 63.14 / 413.63 = 15.26%. The one-off loss is 2.35pp of the 3.40pp fall from FY25. Score effect if read that way: A1 3, A2 3, A4 5, Block A 13; M3 3 (FAT 3.29x and ROCE above 15%); core 58; AVERAGE | The scored figure follows the formula as written (EBIT = PBT + interest). Do not rescore. Add the missing line and a clause in the FLAG-GATE0 reason |
| F4 | MINOR | B01 LBF4, Block B caveat, open-ruling table | Presentation: score effect of a named caveat not shown | Filed CFO includes increases in short-term borrowings inside operating activities: FY24 26.78, FY25 44.26, FY26 17.23 Cr (AR25 p.156; AR26 p.173 shows 1,723.34 L). CFO ex short-term borrowing 15.97, 12.53, 36.06 Cr is shown. Its score effect is not | Add a row to the open-ruling table. CFO ex short-term borrowing: B1 (297.83 - 88.27) / 246.72 = 0.85 = 4 (0.849 unrounded; 2 if read strictly); FCF 15.97 - 30.78, 12.53 - 49.75, 36.06 - 39.23, all negative, so B2 0 and B3 0; B4 3. Block B 7. Deal-breaker 2 (Block B <8, max GOOD) trips but does not bind at AVERAGE. Core 47. AVERAGE | Filed CFO is the correct scored input under "No qualitative judgments". The table shows the capex alternative but omits this one. This is the only reading that trips a deal-breaker |
| F5 | MAJOR | B07 2C case A and headline; YAML capex_embedded_growth_pct; FLAG-CAPEX-FUNDING; 6E stage 9 hand-off line | S7 2C: "total capex under execution x historical fixed asset turnover"; S7 rule 4 (hard evidence over promises); Verifier C rule 3 (consistent with stated evidence tiers) | Case A "committed and in execution" = wire rod 20-25 + solar 30 = 50-55 Cr; 52.5 x 3.196 = 167.8 Cr = 20.4% of 824.0 Cr | B07 tags the 7 MW solar park as a claim: 2A "land acquired (deck p.14); no contract disclosed"; catalysts_12m "claim (land acquired per deck)". AR26 documents only the existing 1.5 MW (p.43). Its Citi solar loan funds the existing Bhandara plant, repaid from March 2025 (AR26 p.204, consolidated borrowings note (e)). Documented capex under execution = wire rod only (machinery ordered, civil works, AR26 p.30; Kotak loan per B07, AR26 p.205). 20-25 x 3.196 = 63.9-79.9 Cr = 7.8-9.7% of 824.0 Cr; midpoint 22.5 x 3.196 = 71.9 Cr = 8.7% | em_score and combined class do not change. The YAML field is the stage 9 hand-off and a CAPACITY-basis input at stage 11. B07's own quality note says consolidated revenue from this capex is near zero, so the 20.4 headline contradicts the report's own reading. Emit 8.7 as the headline. Keep 20.4 as the upper bound that includes the claim-only solar project |
| F6 | MINOR | B07 2A solar row; F2 table solar row; G1 net debt line and "Figure changes"; 2A MEPL funding cell; C1 | S7 rule 3: "SOURCE ANCHORS on every evidence item: (AR p.__), (Q_ FY__ call), (Inv. Pres. slide __)" | (a) Solar date revisions anchored to "run 1 reading of the PR and deck series" (2A, F2 table). (b) "guidance cut from 20-25% to 15-18% (stage 5 record)" (6D). (c) EBITDA 6,626.71 L "on the stage 2 basis" (G1, Figure changes). (d) "7.00% preference share (standalone related-party notes)" (2A). (e) "related-party structures (AR26 related-party notes)" (C1) | Give the source page for each, or mark NOT FOUND | No score rests on these five items. The run 2 anchor remediation left them open |

Severity rule applied (prompts/12, Verifier C rule 5): no finding moves a classification or decision, so none is CRITICAL. F1, F2 and F5 change an emitted value, so they are MAJOR. F3, F4 and F6 are presentation gaps, so they are MINOR.

Direction of the basis choices, stated for the symmetric bar (Master Rule J): both Gate 0 FAILs resolved a basis choice toward the higher score. The E2 choice went the other way (0 rather than 3). F3 is an upward reading left unshown. F4 is a downward reading left unshown.

---

## 5. EFFECT ON EMITTED FIELDS

### 5a. Gate 0 under the findings

| Reading | A | B | C | D | E | Core | Moat /60 | Moats present | Class | Classification | Deal-breaker |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B01 as emitted | 9 | 14 | 8 | 8 | 15 | 54 | 12 | 2 (M5, M9) | MODERATE | AVERAGE | none |
| F1 + F2 (as-written, Verifier C) | 9 | 10 | 8 | 8 | 15 | 50 | 10 | 1 (M5) | THIN | AVERAGE | none |
| F1 + F2 + F3 sensitivity (ex-exceptional) | 13 | 10 | 8 | 8 | 15 | 54 | 12 | 2 (M3, M5) | MODERATE | AVERAGE | none |
| F1 + F2 + F4 sensitivity (CFO ex short-term borrowing) | 9 | 7 | 8 | 8 | 15 | 47 | 10 | 1 (M5) | THIN | AVERAGE | 2 trips, not binding |

Gate 0 classification is AVERAGE in every row. FLAG-GATE0 stands in every row.
Under F1 the block_b_trend text changes: FCF positive 2 of 3 (0.43, 4.76, -2.50 Cr), FY26 negative.

### 5b. B07 fields that depend on B01

If F1 and F2 stand, these B07 items must be re-aligned in the same commit. em_score 11.6, NONE and combined AVERAGE do not change.
- 6C row 1 (core 54) and row 2 (12/60, MODERATE, M5 and M9).
- 6D backward-evidence sentence ("but moats M5 and M9 present").
- 6E map, Family A row (M9 Brand).
- Section 5 "Run 2 note on double credit" (M9). It becomes moot.
- combined_reasoning and FLAG-B01-OPEN-RULINGS (core 54, M5 and M9).
If F5 stands: capex_embedded_growth_pct 8.7, FLAG-CAPEX-FUNDING ("Committed capex in execution Rs 50-55 Cr (wire rod, solar)"), the 6E stage 9 hand-off line, and the analyst_note sentence on 20.4.

recomputed_decision: blank. Verifier C concurs with AVERAGE (Gate 0), NONE (EM) and AVERAGE (combined).

---

## 6. OBSERVATIONS (NOT FINDINGS)

- O1. M5 peer set. With four names, "top 3 mcap" passes for any name except the smallest. The three peers (Apar, Arfin, Maan) overlap MMP's conductor line, 12.1% of FY26 segment sales (B07 1C, AR26 p.226). They do not make aluminium powder, which is 61.2%. The rule says to use the peer data provided, and B01 did. B01's caveat names the three-peer set. Peer-set adequacy for M2, M5 and M9 is an operator question, not a rule breach.
- O2. G2 base year. B07 measures the WC gain from FY25 (104.1 days), which is the three-year peak. B01's FY24 to FY26 window gives -2.5 days, inside the 5-day "stable" band. B07 scores G2 at the floor (LL, inference, 0.5) and names it in FLAG-BORDERLINE-BAND. This is judgment inside the rubric. At 0, em_score is 11.1, still NONE.
- O3. B2 multiplier. B2 holds one documented item (AL59 BIS, AR26 p.26) but is scored at 0.7 "on the blend". This is the lower multiplier, so it does not inflate the score.
- O4. B07 YAML carries two keys outside the S7 template (no_concall_mode, run). They do no harm if the orchestrator expects them.
- O5. I2 coverage. The I2 table tests the three Moderate categories and three product lines, not each Weak-scored row. It cannot change the result. No competitor filing in the corpus shows a sacrifice, and I2 needs one for any score.

---

## 7. VALUATION ADHERENCE (B11): PENDING PHASE 3

Pending phase 3. Not run in this invocation.
Not in phase-1 scope per the task message: Verifier C rules 4, 5 (valuation part), 6, 7, 9, 10, 11, 12, 13, 14 and 15. The expectation_ledger and business_narrative lines in the block below are placeholders marked pending, not results.

---

```yaml
stage: B12c
company: "MMP"
run_date: "2026-10-05"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete
scope: "phase 1: Gate 0 (B01 run 2) + Emerging Moat (B07 run 2); valuation audit pending phase 3"
gate0:
  rules_checked: 54
  fails:
    - {id: "F1", rule: "G0 FORMULA DEFINITIONS: FCF = CFO - Capex; capex = purchase of PPE + intangibles from cash flow statement; exclude acquisitions", scored: "PPE line only; FCF FY24 11.97, FY25 7.04, FY26 14.06 Cr; B2 5, B3 1, Block B 14, core 54", recomputed: "PPE + increase in CWIP + capital advances (AR25 p.156; AR26 p.173); FCF 0.43, 4.76, -2.50 Cr; B2 2, B3 0, Block B 10, core 50; AVERAGE unchanged"}
    - {id: "F2", rule: "G0 M9 GM proxy (Revenue - Material Cost) / Revenue", scored: "Raw Material Cost line, change in inventory excluded; MMP 21.28% vs peer median 12.16%, gap 9.12pp; M9 3; moats 2 (M5, M9) MODERATE; moat 12", recomputed: "material cost net of change in inventory, the basis B01 uses for EBITDA in M1/M2/M5; MMP 22.00%, peer median 18.44% (Arfin), gap 3.56pp; M9 1; moats 1 (M5) THIN; moat 10; grand total 64; AVERAGE unchanged"}
emoat:
  rules_checked: 36
  fails:
    - {id: "F5", rule: "S7 2C total capex under execution x historical FAT; S7 rule 4; consistency with stated evidence tiers", scored: "wire rod 20-25 + solar 30 = 50-55 Cr x 3.196x = 20.4% of 824.0 Cr", recomputed: "solar is claim-only in B07 2A and catalysts_12m (AR26 p.43 shows 1.5 MW existing only); documented capex under execution = wire rod 20-25 Cr x 3.196x = 63.9-79.9 Cr = 7.8-9.7% of 824.0 Cr, midpoint 8.7%"}
    - {id: "F6", rule: "S7 rule 3 source anchor on every evidence item", scored: "five evidence items anchored to upstream records (run 1 reading, stage 5 record, stage 2 EBITDA basis) or unpaged notes (related-party notes)", recomputed: "n/a; give source page or mark NOT FOUND; no score effect"}
valuation: {rules_checked: 0, fails: [], status: "pending phase 3"}
expectation_ledger: {status: "pending phase 3", present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: []}  # rules 13-14; any fail = REWORK stage 11
business_narrative: {status: "pending phase 3", fails: []}  # rule 9; any fail = REWORK stage 13
recomputed_destination_pe: ""  # phase 3
recomputed_decision: ""        # concur: Gate 0 AVERAGE, EM NONE 11.6, combined AVERAGE hold under every recomputation
findings:
  - {id: "F1", severity: "MAJOR", artifact: "B01", location: "Block B (B2, B3); data_notes capex line; block_b_trend; blocks.B; core_score", claimed: "capex = PPE line only (3,078.11 / 4,974.53 / 3,923.03 L); FCF 11.97 / 7.04 / 14.06 Cr; B 14; core 54", recomputed: "capex = PPE + CWIP increase + capital advances (AR25 p.156; AR26 p.173); FCF 0.43 / 4.76 / -2.50 Cr; B2 2; B3 0; B 10; core 50; AVERAGE", note: "Rule excludes only acquisitions; CWIP spend and capital advances are purchases of PPE; B01 score otherwise depends on cash-flow line layout. B01 already shows this reading as an open ruling; make it primary."}
  - {id: "F2", severity: "MAJOR", artifact: "B01", location: "Block F M9; data_notes M9 line; moat_score; moats_confirmed; moat_class; grand_total", claimed: "GM proxy on Raw Material Cost line; gap 9.12pp; M9 3; 2 moats; MODERATE; moat 12", recomputed: "GM proxy net of change in inventory (same basis as B01 EBITDA); MMP 22.00%, Apar 21.01%, Arfin 18.44%, Maan 12.25%; median 18.44%; gap 3.56pp; M9 1; 1 moat (M5); THIN; moat 10; AVERAGE", note: "Same scorecard treats change in inventory as cost in M1/M2/M5 and ignores it in M9. Arfin change in inventory +38.85 Cr (6.3% of FY26 sales) drives the swing. Reading absent from the open-ruling table."}
  - {id: "F3", severity: "MINOR", artifact: "B01", location: "LBF3; Block A; FLAG-GATE0 reason", claimed: "ex-associates sensitivity shown (FY26 ROCE about 10.9%); exceptional fire loss 973.69 L (AR26 p.172) included in EBIT, its effect not shown", recomputed: "ex-exceptional FY26 EBIT 63.14 Cr, ROCE 15.26%; 2.35pp of the 3.40pp fall is the one-off loss; sensitivity A 13, M3 3, core 58, AVERAGE", note: "Scored figure follows the formula; add the missing sensitivity line, do not rescore."}
  - {id: "F4", severity: "MINOR", artifact: "B01", location: "LBF4; Block B caveat; open-ruling table", claimed: "CFO includes short-term borrowing increases 26.78 / 44.26 / 17.23 Cr (AR25 p.156; AR26 p.173); score effect not shown", recomputed: "ex short-term borrowing: B1 0.85 = 4, B2 0, B3 0, B4 3; Block B 7; deal-breaker 2 trips (max GOOD, not binding); core 47; AVERAGE", note: "Filed CFO is the correct scored input; add the row to the open-ruling table, the only reading that trips a deal-breaker."}
  - {id: "F5", severity: "MAJOR", artifact: "B07", location: "2C case A and headline; capex_embedded_growth_pct; FLAG-CAPEX-FUNDING; 6E stage 9 hand-off", claimed: "50-55 Cr under execution (wire rod 20-25, solar 30); 20.4%", recomputed: "solar claim-only per B07's own tags; documented capex under execution wire rod 20-25 Cr; 7.8-9.7%, midpoint 8.7%", note: "em_score and combined class unchanged; field feeds stage 9 and the stage 11 CAPACITY basis; B07's own quality note puts consolidated revenue from this capex near zero. Emit 8.7; keep 20.4 as upper bound."}
  - {id: "F6", severity: "MINOR", artifact: "B07", location: "2A solar row; F2 table solar row; 6D; G1 and Figure changes; 2A MEPL funding; C1", claimed: "anchors 'run 1 reading of the PR and deck series', 'stage 5 record', 'EBITDA on the stage 2 basis', 'standalone related-party notes', 'AR26 related-party notes'", recomputed: "source page or NOT FOUND for each", note: "No score effect; residual of the run 2 anchor remediation."}
critical_count: 0
major_count: 3
minor_count: 3
acceptance_rate: 95.6             # rules passed / rules checked, % (86 of 90)
```
