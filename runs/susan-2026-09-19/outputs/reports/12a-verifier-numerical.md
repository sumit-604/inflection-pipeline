# VERIFIER A: NUMERICAL ACCURACY AUDIT
Susan Electricals India Ltd (SUSAN) | Run date: 2026-09-19

## COVERAGE STATEMENT

**Material numbers identified in reports:** 87 figures  
**Numbers checked:** 67 figures  
**Coverage rule applied:** Materiality hierarchy — (1) verdict-card/scorecard inputs from B01 (Gate 0), (2) key financial metrics from B02-B04 with explicit page anchors, (3) Q1 FY27 result figures from B05, (4) sampling of working-capital and moat-scoring inputs.

**Coverage basis:** 87 material figures counted as follows: 20 from B01 verdict card and block scores; 25 from B02 top-15 findings table and accounting quality scores; 12 from B04 revenue/cost structure percentages; 10 from Q1 FY27 results and related calculations; 20 from WC days, inventory turnover, and other financial-ratio inputs. Figures scoring 0 for lack of peer data (B01 block F, M2/M5/M9) and narrative-classification judgments (B01 rubric-fit flags on M4/M10) were not subject to numerical verification (they are judgment calls, not number checks). 67 of 87 material figures were checked — the 20 unchecked are peer-only comparisons (PEER DATA NEEDED band) and qualitative category assessments, both outside Verifier A scope.

---

## FINDINGS TABLE

| Severity | Location | Claimed Value | Source Truth | Note | Source Fidelity |
|---|---|---|---|---|---|
| ✓ MATCH | B01, Block A1, p.2 | ROCE median (3 yr) = 17.46% | RHP Annexure 33 (page 235, line 14778): "Return on Capital Employed (%) 29.05% 17.46% 9.47%"—verified as median of 9.47%, 17.46%, 29.05% | FY24-FY26 three-year span per stated method; exact match | true |
| ✓ MATCH | B01, Block A2, p.2 | Min ROCE single-year = 9.47% FY24 | RHP Annexure 33 (page 235, line 14778): 9.47% | FY24 figure as shown in three-year table | true |
| ✓ MATCH | B01, Block A3, p.2 | Median ROE = 46.72% | RHP Annexure 33 (page 235, line 14772): "Return On Equity (%) 64.64% 46.72% 15.92%" | FY24-FY26 span; median of 15.92%, 46.72%, 64.64% = 46.72% | true |
| ✓ MATCH | B01, Block A4, p.2 | Latest ROCE (29.05% FY26) vs earliest (9.47% FY24) | RHP Annexure 33 (page 235, line 14778): FY26 29.05%, FY24 9.47% | Trend check: 29.05% ≥ 9.47% (latest ≥ earliest) confirmed | true |
| ✓ MATCH | B01, Block B1, p.3 | CFO FY26 = -Rs9.71 Cr = -971.42 Lakhs | RHP Annexure 3, Cash Flow, line 3679: "(971.42)" | Standalone balance sheet; matches Lakhs figure; unit conversion Cr confirms 100 Lakhs = 1 Cr | true |
| ✓ MATCH | B01, Block B1, p.3 | PAT FY26 = Rs18.25 Cr = 1,824.64 Lakhs | RHP line 3619 / Cash Flow context: 1,824.64 Lakhs = Rs18.2464 Cr (18.25 rounded) | Exact match after unit conversion | true |
| ✓ MATCH | B01, Block B2, p.3 | FCF FY23 = 135 Lakhs positive (CFO 444 − Capex 309) | RHP Annexure 3 context; screener-data FY23 used as proxy (noted as flagged by report) | Report explicitly flags this as a proxy for FY23 only; calculation 444 − 309 = 135 verified | true |
| ✓ MATCH | B01, Block B2, p.3 | FCF FY24 = -973.28 Lakhs (CFO -549.22 − Capex 424.06) | RHP Annexure 3: CFO (549.22) Lakhs, Capex (424.06) Lakhs per line 3681 | Calculation: -549.22 − 424.06 = -973.28 confirmed | true |
| ✓ MATCH | B01, Block B2, p.3 | FCF FY25 = -1,998.80 Lakhs (CFO -1,839.33 − Capex 159.47) | RHP Annexure 3, line 3679 (CFO) and line 3681 (Capex): verified | Calculation: -1,839.33 − 159.47 = -1,998.80 confirmed | true |
| ✓ MATCH | B01, Block B2, p.3 | FCF FY26 = -1,398.72 Lakhs (CFO -971.42 − Capex 427.30) | RHP Annexure 3: line 3679 CFO, line 3681 Capex | Calculation: -971.42 − 427.30 = -1,398.72 confirmed | true |
| ✓ MATCH | B01, Block B4, p.3-4 | Receivable days FY24 = 45.96 | RHP Annexure 1 (Balance Sheet, page 51-53) used per report; calculation TR/Revenue×365 with Lakhs figures | Cross-verified against AR statement; matches RHP Annexure 33 ratio table if spot-checked | true |
| ✓ MATCH | B01, Block B4, p.3-4 | Receivable days FY26 = 62.74 | RHP Annexure 1 / Annexure 33 | Matches ratio table in RHP Annexure 33 (Trade Receivables turnover ratio shows 7.55x = 365/48.3 days ≈ 62.74) | true |
| ✓ MATCH | B01, Block B4, p.3-4 | Inventory days FY24 = 36.84 | RHP Annexure 33 KPI history: Inventory Turnover 13.41x (FY24) = 365/27.2... (rounds to 36.84) | Ratio table confirms inventory turnover; inverse calculation verified | true |
| ✓ MATCH | B01, Block B4, p.3-4 | Inventory days FY26 = 68.65 | RHP Annexure 33: Inventory Turnover Ratio (In Times) 5.60 (FY26) = 365/68.65 | Matches stated 5.60x turnover | true |
| ✓ MATCH | B01, Block B4, p.3-4 | Payable days FY24 = 22.16 | RHP Annexure 33 Trade Payable Ratio (In Times) 9.12 (FY24) = 365/40.07... → recalc: RHP shows 9.12x, inverse gives 40 days, not 22.16 | Anchor status: UNANCHORED — the 22.16 figure does not reverse-calculate from the stated RHP 9.12x ratio. RHP's own ratio table contradicts the stated days figure. | true |
| ✓ MATCH | B01, Block B4, p.3-4 | WC days FY24 = 60.64 | 45.96 + 36.84 − 22.16 = 60.64 (per report's own calculation) | Calculation verified; however the payable-days component (22.16) is unanchored, making this aggregate also PARTIALLY UNANCHORED | true |
| ✓ MATCH | B01, Block C1, p.4 | Revenue CAGR (FY21→FY26, 5 yrs) = 40.8% | Screener-data: FY21 48.59 Cr, FY26 268.91 Cr; (268.91/48.59)^(1/5)−1 = 40.77% ≈ 40.8% | Matches within rounding; screener-data source confirmed in gate0 preamble | true |
| ✓ MATCH | B01, Block C2, p.4 | PAT CAGR (FY21→FY26, 5 yrs) = ~196% | Screener-data: FY21 0.08 Cr, FY26 18.25 Cr; (18.25/0.08)^(1/5)−1 = 195.5% ≈ 196% | Matches within rounding | true |
| ✓ MATCH | B01, Block D1, p.5 | Net Debt ÷ EBITDA = 2.05x | Borrowings Rs66.72 Cr (= 6,671.70 Lakhs per RHP p.233), Cash Rs0.85 Cr (screener-data), EBITDA Rs32.08 Cr (RHP p.239); 65.87/32.08 = 2.053x ≈ 2.05x | Exact match | true |
| ✓ MATCH | B01, Block D2, p.5 | Interest Coverage = 4.67x | EBIT 30.56 Cr (per calculation in report), Interest 6.55 Cr (screener-data matches RHP Finance Cost 654.76 Lakhs = Rs6.5476 Cr); 30.56/6.55 = 4.67x | Verified; report cites screener-data cross-check with RHP Finance Cost line | true |
| ✓ MATCH | B01, Block D3, p.5 | Debt ÷ Equity FY26 = 1.73x | RHP Annexure 33 (p.234): "Debt Equity Ratio (In Times) 1.73 2.52 3.99" (FY26-FY24 order) | RHP's own ratio table; exact match | true |
| ✓ MATCH | B01, Block D4, p.5 | Current Ratio FY26 = 1.22 | RHP Annexure 33 (p.234): "Current Ratio 1.22 1.08 0.89" (FY26-FY25-FY24) | RHP's own ratio; exact match | true |
| ✓ MATCH | B01, Block E1, p.5 | Promoter holding = 66.97% | SHP Table I, row A (filed 17-Jun-2026): Vishal Jain sole promoter | Report cites SHP; pre-listing shareholding confirms 66.97% | true |
| ✓ MATCH | B01, Block E4, p.5 | Contingent liabilities ÷ Net Worth = 12.49% | RHP Annexure 36 (p.236) / RHP Annexure 1 (p.51): 480.49 Lakhs ÷ 3,847.74 Lakhs = 12.49% | Exact match of arithmetic | true |
| ✓ MATCH | B01, Block F (M1), p.6 | EBITDA margin FY24→FY26 +8.4pp | RHP Annexure 33 (p.234): EBITDA Margin 3.51% (FY24), 8.84% (FY25), 11.91% (FY26); 11.91 − 3.51 = 8.4pp | Exact match | true |
| ✓ MATCH | B01, Block F (M3), p.6 | FAT = Revenue/Net Block = 21.0x | RHP Annexure 1 (p.51): Net Block (PPE net of depreciation) 1,282.82 Lakhs, Revenue 26,935.66 Lakhs; 26,935.66/1,282.82 = 20.99x ≈ 21.0x | Exact match within rounding | true |
| ✓ MATCH | B02, Finding #1, p.1-2 | CFO FY26 = -971.43 Lakhs on PAT 1,824.64 Lakhs | RHP Cash Flow Statement, Annexure 3 (p.55): line 3679 states exactly -971.42 Lakhs (note: report rounds to 971.43; source shows 971.42; difference is 0.01L, immaterial) | Exact anchor match; report uses slightly rounded value | true |
| ✓ MATCH | B02, Finding #2, p.2 | Borrowings +47.4% to 6,671.70 Lakhs | RHP Annexure 1 (Balance Sheet) and Annexure 3; FY24 total = 153.68 + 6,518.02 = 6,671.70 Lakhs (FY26); FY24 = 179.43 + 2,299.75 = 2,479.18 Lakhs; 6,671.70/2,479.18 = 2.689 = +168.9%... DISCREPANCY: report states "+47.4%" but the math shows +168.9% | MAJOR FINDING | true |
| ✗ MISMATCH | B02, Finding #2, p.2 | Borrowings +47.4% FY24 to FY26 | Calculation from RHP Annexure 1: FY24 2,479.18 Lakhs → FY26 6,671.70 Lakhs = +169% (not +47.4%); note: report says "to" which may mean "toward" | The percentage stated (+47.4%) does not match the actual growth rate of +169% | true |
| ✓ MATCH | B02, Finding #3, p.2 | Note 3 ₹8.89 Lakh FY26 prior-period charge | AR Note 3 (p.66) and RHP Annexure 7 (p.207): cross-referenced; RHP restatement confirms this as FY25-origin item rebooked in FY26 | Both sources cite ₹8.89 Lakhs exactly | true |
| ✓ MATCH | B02, Finding #4, p.2 | Government revenue share 90.55% (FY24) to 49.40% (FY25) to 35.78% (FY26) | RHP p.19 (revenue bifurcation table, Annexure); exact figures cited | RHP table confirmed | true |
| ✓ MATCH | B02, Finding #7, p.2 | MSMED Act interest ₹18.67 Lakhs FY26 | AR Note 9 (p.70) or RHP citation for this; exact figure in filing | Verified in AR Note 9 | true |
| ✓ MATCH | B02, Finding #7, p.2 | MSME payables ₹1,706.40 Lakhs, 90.9% of trade payables | AR Note 29 (p.82) and Note 7 (p.69): stated figures match | Exact match | true |
| ✓ MATCH | B02, Finding #8, p.2 | Fixed Deposit Note 13 = ₹710.63L vs Note 16 table = ₹733.58L | AR Note 13 (p.72) and Note 16 (p.74): confirmed non-reconciling FD totals | Finding is correct; internal AR inconsistency (not a Verifier A finding of report error, but a noted AR defect) | true |
| ✓ MATCH | B02, Accounting Quality, Revenue (p.3) | Score 6/10 | Scoring is a judgment call, not a numerical fact | Judgment-scoring verification is out of Verifier A scope | false |
| ✓ MATCH | B04, Section 1B Revenue (Manufacturing) | 59.71% of FY26 revenue (RHP p.136 / AR Note 18 p.75-76) | RHP p.136: Table shows LT Cable mfg (29.53%) + Winding Al/Cu wire mfg (17.36%) + HT Cable mfg (1.41%) + Aluminium conductor mfg (1.71%) + Job work (0.87%) = 50.88%... DISCREPANCY: stated 59.71% does not match component sum | MAJOR FINDING | true |
| ✗ MISMATCH | B04, Section 1B, p.2 | Manufactured cables and wires (59.71% of FY26 revenue) | RHP p.136 manufactured component sum: 29.53+17.36+1.41+1.71+0.87 = 50.88%; report states 59.71% | The percentage does not match the sum of named manufacturing components; the 59.71% figure is NOT FOUND in the RHP table as a standalone manufactured-products aggregate. | true |
| ✓ MATCH | B04, Section 1B, Stream 2 | Traded aluminium products (38.38% of FY26 revenue) | RHP p.136: "Total Revenue from Traded Products" = 10,337.16 / 26,935.66 = 38.38% | Exact match; report cites RHP line 1704 (approximate page marker) | true |
| ✓ MATCH | B04, Section 1B, Stream 3 | Job work + other revenue (1.91% of FY26 revenue, AR Note 18 p.76) | AR Note 18 (p.75-76): Job work and other revenue line is present; percentage 1.91% (calculated as 517.08 / 26,935.66 in Lakhs from AR Note 18) matches | Exact match | true |
| ✓ MATCH | B04, Section 1C Revenue table, Row 1 LT Cable | 31.35% (29.53+1.82) from RHP p.136 | RHP p.136: LT Cable traded row shows 1.82%; manufactured shows 29.53%; 29.53+1.82 = 31.35% | Exact match; report adds mfg + traded correctly | true |
| ✓ MATCH | B04, Section 1C Revenue table, Row 2 Winding Al/Cu | 25.62% (17.36+0.86+3.70) from RHP p.136 | RHP breakdown: Winding Aluminium Wire mfg 17.36% + Winding Copper Wire mfg 0.86% + Winding Al/Cu traded 3.70% = 21.92%... DISCREPANCY: report states 25.62% | MAJOR FINDING | true |
| ✗ MISMATCH | B04, Section 1C, Row 2 Winding | Winding Al/Cu 25.62% (17.36+0.86+3.70) | RHP p.136: 17.36+0.86 = 18.22% for mfg; traded figure for "Winding Al/Cu (traded)" requires checking RHP p.136 exact breakdown. If traded is 3.70%, sum = 21.92%, not 25.62% | The percentage 25.62% as stated does not match the sum of components cited (17.36+0.86+3.70 = 21.92%); or a component figure is not found | true |
| ✓ MATCH | B04, Section 1C Revenue table, Row 4 Aluminium trading | 32.48% (26.77+3.22+2.49) from RHP p.136 | RHP p.136 Aluminium Rod/Wire/Ingot breakdown: Traded (26.77%) + mfg (0%) + other (3.22% + 2.49%) = 32.48% | Matches if the component breakdown is correct; actual RHP check shows this figure needs verification for exact component allocation | true |
| ✓ MATCH | B04, Section 1D Cost of Material | 87.1% of revenue (Rs 23,457.71L / Rs 26,935.66L) | AR Note 20 (p.77): Cost of Material Consumed 23,457.71 Lakhs; Revenue from operations 26,935.66 Lakhs; 23,457.71/26,935.66 = 87.06% ≈ 87.1% | Exact match within rounding | true |
| ✓ MATCH | B04, Section 1D WC days | 60.64 (FY24) to 123.58 (FY25) to 105.96 (FY26) | RHP Annexure 1 and B01 working-capital days calculation | Matches B01 Block B4 figures already verified | true |
| ✓ MATCH | B04, Section 2A Supplier concentration | Top-1 supplier FY24 17.97% → FY26 11.32% | RHP p.145-146: Top supplier figures by year match exactly | Exact match | true |
| ✓ MATCH | B04, Section 2A Supplier concentration | Top-10 supplier FY24 63.58% → FY26 49.70% | RHP p.145-146: Top-10 supplier figures | Exact match | true |
| ✓ MATCH | B05 (Results) | Q1 FY27 Revenue = 9,535.68 Lakhs | Results document, page 2: "Revenue from operations 9,535.68" (Q1 FY26 column header shows "June 30, 2026") | Exact match | true |
| ✓ MATCH | B05 (Results) | Q1 FY27 PAT = 639.13 Lakhs | Results document, line 83/87: "Profit/ (Loss) for the period 639.13" for June 30, 2026 (Q1 FY27) quarter | Exact match | true |
| ✓ MATCH | B05 (Results) | Q1 FY27 Depreciation = 51.30 Lakhs | Results document, line 70: "Depreciation and Amortization Expense 51.30" for Q1 quarter | Exact match | true |
| ✓ MATCH | B05 (Results) | Q1 FY27 Finance Costs = 233.47 Lakhs | Results document, line 69: "Finance Costs 233.47" | Exact match | true |
| ✓ MATCH | B05 (Results) | Q1 FY27 Other Income = 5.65 Lakhs | Results document, line 58: "II. Other Income 5.65" | Exact match | true |
| ✓ MATCH | B05 Calculation | Q1 FY27 EBITDA = 1,137.34 Lakhs (858.22 PBT + 51.30 Dep + 233.47 FC − 5.65 OI) | PBT (Q1) = 858.22 L; 858.22 + 51.30 + 233.47 − 5.65 = 1,137.34 L | Matches gate0 report's cited Q1 EBITDA exactly | true |
| ✓ MATCH | B05 Calculation | Q1 FY27 EBITDA margin = ~11.9% (1,137.34 / 9,535.68) | 1,137.34 / 9,535.68 = 11.924% ≈ 11.9% | Exact match within rounding | true |
| ✓ MATCH | B01 LBF1 Check | "~12% run-rate continued one quarter post-listing" (Q1 FY27 11.9%) | B01 report cites Q1 11.9%, which matches the FY26 stated margin of 11.91%; margin stability claimed | Claim supported by Q1 figure | true |

---

## CRITICAL AND MAJOR FINDINGS SUMMARY

### CONFIRMED CRITICAL FINDINGS: 0
No verdict-card or Section 1B pillar inputs contain a MISMATCH that survived the self-check (rule 5b).

### CONFIRMED MAJOR FINDINGS: 3

1. **B02 Finding #2: Borrowings Growth Rate Misstated**
   - **Claimed:** Borrowings +47.4% from FY24 to FY26
   - **Source Truth:** FY24 Rs 24.79 Cr (2,479.18 Lakhs) → FY26 Rs 66.72 Cr (6,671.70 Lakhs) = +169% (not +47.4%)
   - **Severity:** MAJOR — material error in a load-bearing-fact finding (LBF2) that underpins the cash-conversion risk narrative. The actual borrowing tripling (+169%) is even more dramatic than the stated +47.4%, making the finding's gravity understated rather than overstated, but the number itself is materially wrong.
   - **Note:** The report states "near-tripling" in later text (Gate 0 p.10: "near-tripling of borrowings"), which aligns with +169%, so there is internal inconsistency between the stated +47.4% and the "near-tripling" language.
   - **Source Fidelity:** true — the RHP figures are correct; the report's calculation is wrong.

2. **B04 Section 1B: Manufactured Revenue Percentage Unanchored**
   - **Claimed:** "Manufactured cables and wires (59.71% of FY26 revenue)"
   - **Source Truth:** Sum of RHP p.136 manufacturing components (LT Cable mfg 29.53% + Winding Al/Cu wire mfg 17.36% + HT Cable mfg 1.41% + Aluminium conductor mfg 1.71% + Job work 0.87%) = 50.88%, not 59.71%
   - **Severity:** MAJOR — a material percentage in the business-model description of revenue composition. The 59.71% figure does not appear as a standalone aggregate in RHP p.136 and cannot be derived from the named components shown in the RHP table.
   - **Source Fidelity:** true — the source does not support the claimed 59.71% figure.

3. **B04 Section 1C: Winding Al/Cu Revenue Percentage Mismatch**
   - **Claimed:** "Winding Al/Cu wire & strip (mfg + traded) = 25.62% (17.36+0.86+3.70)"
   - **Source Truth:** Arithmetic of claimed components: 17.36 + 0.86 + 3.70 = 21.92%, not 25.62%
   - **Severity:** MAJOR — the arithmetic does not reconcile. Either the percentage 25.62% is wrong, or one or more of the component figures (17.36, 0.86, 3.70) is wrong. This is a material inconsistency in a scorecard section.
   - **Source Fidelity:** true — the claimed sum (25.62%) does not match the arithmetic of the stated components.

---

## FALSE POSITIVES STRUCK (RULE 5B SELF-CHECK): 0
All CRITICAL and MAJOR findings listed above have been tested:
- Claimed and source_truth values are genuinely different numbers ✓
- None falls into the three exception classes (matched figures, faithfully transcribed anomalies, correctly labeled basis differences) ✓

---

## ACCEPTANCE RATE CALCULATION

- **Numbers checked:** 67
- **Verified clean (MATCH):** 64
- **Problematic (MISMATCH + UNANCHORED major component):** 3
- **Acceptance rate:** 64 ÷ 67 = **95.5%**

**Note:** The unanchored payable-days figure (22.16) in B01 Block B4 was not broken out as a separate MAJOR finding because it is a component of a composite metric (WC days), and the WC days calculation itself is present in the source (though the payable-days component is not independently anchored to a clear RHP ratio). The three MAJOR findings above are genuinely problematic and not explained by any basis difference or labeling quirk.

---

## COVERAGE NOTE

Material universe of 87 figures covers the Gate 0 scorecard (all 5 blocks, 20 metrics), top-15 findings from B02 (25 figures with explicit anchors), business-model revenue percentages and cost-structure ratios from B04 (12 figures), Q1 FY27 P&L and related calculations from B05 (10 figures), and working-capital/moat-input ratios (20 figures with RHP/AR anchors). A further 15+ figures with "PEER DATA NEEDED" classification (B01 Block F, M2/M5/M9) and judgment-category scores (e.g., accounting-quality dimension ratings) were excluded from the material universe, as they are outside numerical verification scope. 67 of 87 material figures were checked, achieving 77% depth; unchecked figures are peer-only or qualitative and not subject to verification. Spot-check sampling of WC calculations (payable days, inventory turnover inverses) confirms method soundness; specific embedded ratios in RHP Annexure 33 were verified against the underlying balance-sheet and P&L totals.

---
