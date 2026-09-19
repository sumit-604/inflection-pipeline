# STAGE 12 VERIFIER C: FRAMEWORK ADHERENCE, DPABHUSHAN (PHASE-1 SCOPE)

Run date: 2026-09-19 | Model: claude-opus-5 | Scope: Gate 0 (B01) and Emerging Moat (B07) only.
Valuation audit (B10/B11), Expectation Ledger (rules 13-14), Business Understanding Narrative (rule 9),
B09b dossier (rule 10) and Role 1 exit rules (11-12, 15): NOT RUN, PENDING PHASE 3 / FINALIZE.

Rule sources read: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md.
Artifacts audited: outputs/reports/01-gate0.md + outputs/blocks/B01-gate0.yaml; outputs/reports/07-emoat.md
+ outputs/blocks/B07-emoat.yaml. Re-derivation data: inputs/screening/screener-Data_Sheet.csv,
inputs/screening/{SENCO,PNGJL,KALYANKJIL}-Data_Sheet.csv, inputs/other/MOTISONS-Data_Sheet.csv, run-log.md.

Verifier C audits rule application. Number existence is Verifier A's call. Where I re-derive a value
below, I use only figures B01/B07 already state or the named CSV rows.

---

## 1. GATE 0 (B01) COMPLIANCE TABLE

| # | Rule | Stated input (anchor) | Threshold applied | B01 score | Recomputed | Result |
|---|---|---|---|---|---|---|
| A1 | Median ROCE | 38.91% (B01 Block A table) | >=25% = 5 | 5 | 5 | PASS |
| A2 | Min single-year ROCE | 37.36% FY24 (B01 Block A) | >=15% = 5 | 5 | 5 | PASS |
| A3 | Median ROE | 35.07% (B01 Block A) | >=20% = 5 | 5 | 5 | PASS |
| A4 | ROCE trend | 45.86% vs 37.36% (B01 Block A) | latest >= earliest = 5 | 5 | 5 | PASS |
| B1 | Cum CFO / Cum PAT | -24.59 / 541.14 = -4.5% (screener-Data_Sheet.csv rows 24, 57) | <0.50 = 0 | 0 | 0 | PASS |
| B2 | FCF-positive years | 0 of 3 (B01 Block B) | <50% = 0 | 0 | 0 | PASS |
| B3 | Cum FCF / Cum PAT | -152.66 / 386.40 = -39.5% (B01 Block B) | negative = 0 | 0 | 0 | PASS |
| B4 | WC days change | 59.72 -> 80.08, +20.4 days (B01 Block F WC table) | increased >15 = 0 | 0 | 0 | PASS |
| C1 | Revenue CAGR | (4,065.13/451.02)^(1/9)-1 = 27.67% (screener-Data_Sheet.csv row 11) | >=20% = 5 | 5 | 5 | PASS |
| C2 | PAT CAGR | (211.84/4.90)^(1/9)-1 = 51.99% (screener-Data_Sheet.csv row 24) | >=20% = 5 | 5 | 5 | PASS |
| C3 | Positive YoY revenue years | 8/9 = 88.9%; only FY20 807.17 < FY19 811.88 (row 11) | 75-99% = 3 | 3 | 3 | PASS |
| C4 | PAT CAGR minus Rev CAGR | +24.3pp (B01 Block C) | >=+3pp = 5 | 5 | 5 | PASS |
| D1 | ND / EBITDA | 261.63 / 309.67 = 0.85x (B01 Block D) | 0-1.0x = 4 | 4 | 4 | PASS |
| D2 | Interest cover | 298.92 / 16.22 = 18.43x (B01 Block D) | >=10x = 5 | 5 | 5 | PASS |
| D3 | D/E | 287.38 / 632.61 = 0.454 (B01 Block D) | 0.1-0.5 = 4 | 4 | 4 | PASS |
| D4 | Current ratio | 1,05,124.21 / 49,078.82 Lakh = 2.14x (B01 Block D) | >=2.0 = 5 | 5 | 5 | PASS |
| E1 | Promoter holding | 73.59% (B01 Block E, AR FY26 p.81) | >=60% = 5 | 5 | 5 | PASS |
| E2 | Promoter change, 3 years | 1-year filed -0.23pp (B01 Block E); 3-year screener text -0.11pp (B01 Block E context) | +-1% = 3 | 3 | 3 | PASS (window note, finding F-G5) |
| E3 | Pledge | N/A, not in provided data (B01 Block E) | N/A scores 0 (stage-1 rule 5) | 0 | 0 | PASS |
| E4 | Contingent liab / NW | 12.57 Lakh / 63,261 Lakh = 0.02% (B01 Block E) | <5% = 5 | 5 | 5 | PASS |
| Core | Block sums | 20+0+18+18+13 | sum | 69 | 69 | PASS |
| M1 | Pricing power | EBITDA margin 4.54% FY17 -> 7.62% FY26, +3.08pp; rev CAGR 27.67% (B01 Block F) | >=2pp AND >=10% = 5 | 5 | 5 | PASS |
| M2 | Cost advantage vs peer median | B01: 7.62% vs median 12.62% (SENCO, PNGJL, MOTISONS) | below = 0 | 0 | 1 on the run's current peer set | FAIL (stale peer set, F-G3) |
| M3 | Capital efficiency | FAT 54.5x, ROCE 45.86% (B01 Block F) | FAT >3x AND ROCE >20% = 5 | 5 | 5 | PASS |
| M4 | Customer stickiness | 1 decline year, recovered; receivable days 0.09-0.24 (B01 Block F) | max 1 decline, recovered = 3 | 3 | 3 | PASS |
| M5 | Scale and dominance | B01: 3rd of 4 by mcap, 3rd on margin | top 5 mcap = 1 | 1 | 1 (4th of 4 on current set, same band) | PASS |
| M6 | Technology/R&D | no R&D disclosed | else 0 | 0 | 0 | PASS |
| M7 | Regulatory/licence | unregulated segment | unregulated = 0 | 0 | 0 | PASS |
| M8 | Distribution | 12 showrooms, growing; rev CAGR 27.67%; per-store trend N/A (B01 Block F) | growing AND >=15% = 3 | 3 | 3 | PASS |
| M9 | Brand (GM proxy) | B01 marked PEER DATA NEEDED | at/below peer median = 0 | 0 | 0, but on computed peer data | FAIL (process, F-G2) |
| M10 | Switching costs | growth 8/9 years; receivable days stable | all but 1 year AND stable = 3 | 3 | 3 | PASS |
| M11 | Network effects | selling % FY23 0.94, FY24 0.88, FY25 1.06, FY26 blank (B01 Block F) | rising = 1; N/A = 0 | 3 | 1 (or 0 strict N/A) | FAIL (F-G1) |
| M12 | Negative WC | 59.72 / 60.38 / 80.08 days (B01 Block F) | >45 = 0 | 0 | 0 | PASS |
| Moat | Moat score, count, class | 23/60, 6 present, FORTRESS | 6+ = FORTRESS; 4-5 = STRONG | FORTRESS | 21-22/60, 5 present, STRONG | FAIL (consequential of F-G1) |
| Conf | Data confidence / history downgrade | 10 years P&L/CF; BS detail FY24-FY26 only | 10+ full | full, no downgrade | no change to final class | PASS (note F-G4) |
| Matrix | Classification matrix | Core 69 + FORTRESS -> GOOD+ | 60-79 + STRONG/FORTRESS = GOOD+ | GOOD+ pre-cap | GOOD+ pre-cap (STRONG maps the same) | PASS |
| DB | Deal-breaker application | #2 Block B 0 <8; #4 cum CFO/PAT -4.5% <0.50 | #4 -> max AVERAGE | AVERAGE, #4 binding, driving years named FY25-FY26 | AVERAGE | PASS |
| Edge | CAGR edge rules | all endpoints positive; no loss-to-profit swing (B01 data_notes) | N/M only on non-positive endpoint | honoured | honoured | PASS |
| Form | Formula definitions (ROCE, ROE, WC days, FCF, CAGR) | ROCE computed and stated as computed; revenue basis for days stated; capex excludes acquisitions | fixed formulas | applied | applied | PASS |
| N/A | N/A-scores-0 and anchor rules | E3, M9 marked; anchors present | rule 4-5 | applied | applied (M9 mislabelled, see F-G2) | PASS |

Gate 0 rules checked: 40. FAIL: 4 (M2, M9, M11, moat class). Final classification AVERAGE survives every recomputation.

### Gate 0 findings

**F-G1 (MAJOR). M11 scored 3 on a selling-expense series that rises and lacks its latest year.**
The 3-band needs "rev CAGR >=20% AND selling % stable/declining". Selling and admin as % of sales:
FY23 18.51/1,971.11 = 0.94%, FY24 20.57/2,336.82 = 0.88%, FY25 35.09/3,306.97 = 1.06%
(screener-Data_Sheet.csv rows 11, 17). FY26 is blank in that row. In FY26, screener folds Power, Other
Mfr. Exp and Selling and admin into "Other Expenses" 73.26 (rows 14-18). The combined line reads
FY24 34.74/2,336.82 = 1.49%, FY25 56.51/3,306.97 = 1.71%, FY26 73.26/4,065.13 = 1.80% (rows 14-18).
Both readings show a rising ratio. The 1-band ("growth >15% but selling % rising") applies: M11 = 1.
Under stage-1 rule 5, a missing latest-year point would score 0. Either value is below 3.
Consequence: moat score 23 -> 21 (22 with F-G3), moats present 6 -> 5, moat class FORTRESS -> STRONG.
The classification matrix maps Core 60-79 + STRONG to GOOD+, the same as FORTRESS. Deal-breaker #4 still
caps at AVERAGE. Decision unchanged. The FORTRESS label is carried into B07 Section 6C and 6E and into
downstream prose. It must read STRONG (5 present).

**F-G2 (MINOR). M9 marked PEER DATA NEEDED when the peer proxy was computable.**
The rule's proxy is (Revenue - Material Cost) / Revenue. B01 computed DPABHUSHAN's own gross margin as
10.28% by netting Change in Inventory (row 12 3,789.76 minus row 13 142.37 = 3,647.39; 417.74/4,065.13).
The same netting works for peers. SENCO: 8,662.18 - 1,900.13 = 6,762.05; GM 19.79% (SENCO-Data_Sheet.csv
rows 11-13). PNGJL: 9,367.58, Change in Inventory blank; GM 11.96% (PNGJL rows 11-13). KALYANKJIL:
35,614.8 - 4,576.27 = 31,038.53; GM 13.16% (KALYANKJIL rows 11-13). MOTISONS: 430.98 - 50.67 = 380.31;
GM 22.31% (inputs/other/MOTISONS-Data_Sheet.csv rows 11-13). SENCO's "Raw Material Cost > Sales" is
purchases before the inventory change, not an artefact. Peer median is 19.79% on B01's set and 13.16%
on the current set. DPABHUSHAN at 10.28% is below either. M9 = 0 stands. The label is wrong, the score is not.

**F-G3 (MINOR). B01 peer set is stale against the run's governing peer set.**
B01 used MOTISONS for M2, M5 and M9. Stage 6 run 1 found the MOTISONS transcripts were RBZ Jewellers and
replaced the peer with KALYANKJIL (run-log.md line 7). MOTISONS-Data_Sheet.csv now sits in inputs/other/.
On SENCO, PNGJL, KALYANKJIL: KALYANKJIL EBITDA (1,801.99 + 499.48 + 422.86) / 35,742.86 = 7.62%
(KALYANKJIL rows 11, 20-22). Peer median of 12.62% / 6.46% / 7.62% = 7.62%. DPABHUSHAN 7.62% sits
within +-2pp: M2 = 1 (was 0). M5: KALYANKJIL mcap 60,090.62 (KALYANKJIL row 8) ranks first; DPABHUSHAN
3,306.17 (screener-Data_Sheet.csv row 8) falls to 4th of 4; band stays 1. Neither change creates a
moat present. Moat score +1. Stage 1 applied its rules to the peer set it received; the defect is
that B01 was not refreshed after the peer swap.

**F-G4 (MINOR, observation, no FAIL). Data-confidence tier rests on a mixed window.**
B01 declares "10+ yrs full" (B01 opening, data_years 10). Block A, D, B2-B4 and the WC-based moat tests
run on FY24-FY26 only (B01 data_notes line 2). The rule keys confidence to years of data, and 10 years of
P&L and cash flow exist, so the tier is defensible. If the 3-4-year LIMITED tier were applied to the
ratio blocks, the pre-cap class would drop GOOD+ -> GOOD. Deal-breaker #4 still binds at AVERAGE. No
decision change. B01 disclosed the window per metric, which the rule's intent needs.

**F-G5 (MINOR, observation, no FAIL). E2 scored on a 1-year filed window.**
The rule asks for a 3-year change. The filed comparison covers 1 year, -0.23pp (AR FY25 p.67 vs AR FY26
p.81, per B01). The 3-year screener aggregation shows -0.11pp (B01 Block E context). Both sit in the
+-1% band, so E2 = 3 on either window. Disclosed by B01.

---

## 2. EMERGING MOAT (B07) COMPLIANCE TABLE

| # | Rule | B07 evidence | Result |
|---|---|---|---|
| 1 | All 22 categories plus R1 addressed (23 rows) | Section 3 and Section 5 tables list A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, I1-I2, R1 = 23 rows | PASS |
| 2 | NO EVIDENCE FOUND stated where none | stated on each zero row with a reason | PASS |
| 3 | Raw likelihood x impact values | C1 MM=2, D2 LM=1, E1 MM=2, H1 HL=2, R1 HM=3 (B07 Section 5) | PASS |
| 4 | Evidence multipliers per row | C1, E1, H1, R1 at 1.0x (DOC); D2 at 0.7x (CLAIM) | PASS |
| 5 | Adjusted total arithmetic | B07 total 10; 2.0+0.7+2.0+2.0+3.0 = 9.7 | FAIL (F-E3) |
| 6 | Completionist recount performed and reconciled | recount line present; counts do not reconcile | FAIL (F-E4) |
| 7 | Scores consistent with evidence tiers (no CLAIM scored as DOC) | D2 scored at CLAIM tier; A3 contradicted claim zeroed; no CLAIM-only row scored at 1.0x | PASS |
| 8 | Classification band | <12 -> NO MEANINGFUL EMERGING MOAT | PASS (9.7 or lower, same band) |
| 9 | Category 21 (I1) present, gated on both legs | present, 0, no (a) or (b) leg evidenced | PASS |
| 10 | Category 22 (I2) present, gated on named sacrifice | present, 0, "nothing must be destroyed" reasoning stated | PASS |
| 11 | I1/I2 contribution stated separately | "I1/I2 contribution: 0" | PASS |
| 12 | One improvement, one mechanism (CLAUDE.md NEVER) | hallmarking formalisation credited in H1 (2.0) and R1 (3.0) | FAIL (F-E1) |
| 13 | Section 2C: capex under execution x historical FAT, arithmetic shown, no estimated inputs | Jodhpur capex and guided-store capex estimated by analogy | FAIL (F-E2) |
| 14 | F2 cross-references the B05 promise-delivery record | cited: grade C, 2 delivered / 5 partial / 4 missed | PASS |
| 15 | Optionality register: columns and membership | 6 rows, 4 columns, all 0-scored or CLAIM-only | PASS (note F-E6) |
| 16 | Section 6C uses the injected Gate 0 block | core 69, 6 moats, both classes present | PASS (note F-E5) |
| 17 | Section 6D combined classification per the matrix | AVERAGE backward + NONE forward -> AVERAGE | PASS |
| 18 | active_categories holds only Strong/Moderate rows | E1, R1 only | PASS |
| 19 | All six sections plus register present | Sections 1-6 and register present | PASS |
| 20 | Taxonomy note: EM scan is not FTTCP | stated in header | PASS |

Emerging Moat rules checked: 20. FAIL: 4 (rows 5, 6, 12, 13). Classification NONE survives every recomputation.

### Emerging Moat findings

**F-E1 (MAJOR). Hallmarking formalisation credited twice, H1 and R1.**
H1 scores 2.0 on "mandatory hallmarking coverage expanded from 343 to 361 to 385 districts... favouring
organised retailers" (B07 Section 3, H1). R1 scores 3.0 on the same hallmarking expansion (B07 Section
4B row 1, Section 4C). B07 itself treats them as one item ("H1/R1", Section 6B and 6E). CLAUDE.md: "Never
credit one quality improvement through two mechanisms." Recomputed: keep R1 3.0, drop H1 -> 9.7 - 2.0 =
7.7. Classification stays NONE (<12). Decision unchanged. Stage 11 must not draw two Pillar 3 or catalyst
credits from this one tailwind.

**F-E2 (MAJOR). Section 2C capex_embedded_growth_pct = 23 rests on estimated capex.**
B07 builds "capex under execution" of Rs 13.75 Cr as Dahod + Jodhpur at the Rs 2.5-3 Cr format bracket
(~Rs 5.5 Cr) plus ~Rs 8.25 Cr for 2-3 guided, unsited FY27 stores (B07 Section 2C). B07's own input_gaps
say Jodhpur capex "was estimated ... by analogy to Dahod, not anchored directly". The guided stores are
CLAIM-grade, not capex under execution. CLAUDE.md: "Never estimate a missing number. NOT FOUND is the only
valid fill." Recomputed: anchored capex under execution is NOT FOUND at site level. If the format bracket
is accepted as Dahod's figure, Rs 2.5-3 Cr x 67.7 = Rs 169-203 Cr = 4.2-5.0% of Rs 4,070.33 Cr (B07
Section 2C inputs). The YAML field should read NOT FOUND, or 4-5% with the bracket basis stated, not 23.
Separately, the FAT basis (67.7x on PP&E Rs 60.14 Cr, B07 2C) differs from B01's 54.5x on Net Block Rs
74.66 Cr (B01 M3). B07 caveats 2C heavily, which limits the damage. The field still feeds a numeric
slot that Stage 11 may read under the 26.1 CAPACITY basis.

**F-E3 (MINOR). Adjusted total rounds D2 up.**
D2 = 1 x 0.7 = 0.7 (B07 Section 5). B07 shows "0.7 (rounded to 1)" and totals 10. The rule has no rounding
step. Correct total 9.7 (7.7 after F-E1). em_score should carry 9.7 or 7.7. Band unchanged.

**F-E4 (MINOR). Completionist recount does not reconcile.**
Section 3 states "7 DOC items across 5 categories" and then lists items that include the F2/G1/G2/H3
zeroing evidence. The YAML recount says 7 across 5 non-zero categories plus 3 more. evidence_mix says
documented 10, claim 6, inference 2. D2 is counted as a DOC category in the recount but scored at the CLAIM
tier. The recount was performed and the non-zero count (5) sits in the 3-6 base rate, so the guard's
purpose is met. The three counts must agree.

**F-E5 (MINOR, observation). Section 6C presentation.**
Core score printed as "69/?" (B07 6C). The denominator is 100 (stage-1 Block A-E max). Section 6C, 6E and
the H1/4C text also carry the FORTRESS label (see F-G1) and name MOTISONS as a listed peer (see F-G3).

**F-E6 (MINOR, observation). Digital revenue sits in the register and drives a score.**
The digital 3-5%-of-topline claim is an optionality register row. The same claim is the "moat-relevant"
basis for D2's 0.7 (B07 Section 5, D2 row). The prompt says registered options are "watched, never
scored". The prompt also admits CLAIM-only items to the register. The two instructions collide here. No
FAIL is charged. Operator note: decide whether D2's 0.7 stands or the claim lives only in the register
(the D2 score would then be 0 and the total 7.0 after F-E1).

---

## 3. RULES NOT IN PHASE-1 SCOPE

- Rule 4, 5, 7, 11, 12, 15 (valuation, B11): PENDING PHASE 3.
- Rules 13-14 (Expectation Ledger, gates): PENDING PHASE 3.
- Rule 6 (B09 downstream candidates): not in this invocation's input list. Not checked.
- Rule 9 (Business Understanding Narrative, stage 13): PENDING.
- Rule 10 (B09b dossier): fires at /finalize.

## 4. SUMMARY

- Rules checked: 60 (Gate 0 40, Emerging Moat 20). Passed: 52. Acceptance rate 86.7%.
- CRITICAL 0. MAJOR 3 (F-G1, F-E1, F-E2). MINOR 8 (F-G2, F-G3, F-G4, F-G5, F-E3, F-E4, F-E5, F-E6).
- Gate 0 recomputed: core 69 (unchanged); moat score 22/60 on the current peer set (21 on B01's set);
  5 moats present; moat class STRONG (B01: FORTRESS); classification AVERAGE (unchanged, deal-breaker #4).
- Emerging Moat recomputed: 7.7 (B07: 10); class NONE (unchanged); capex_embedded_growth_pct NOT FOUND,
  or 4-5% on the bracket basis (B07: 23).
- No finding changes a decision. No REWORK trigger from this verifier.

```yaml
stage: B12c
company: "DPABHUSHAN"
run_date: "2026-09-19"
model: "claude-opus-5"
status: complete
scope: "PHASE 1 - Gate 0 (B01) and Emerging Moat (B07) only; valuation audit pending phase 3"
gate0: {rules_checked: 40, fails: ["M11 scored 3 on rising selling % with FY26 missing; recomputed 1 (or 0 strict N/A)", "Moat class FORTRESS -> STRONG (5 present) consequential of M11", "M9 PEER DATA NEEDED misapplied; peer GM proxy computable, score 0 unchanged", "M2 on stale peer set (MOTISONS); current set SENCO/PNGJL/KALYANKJIL gives M2 = 1"]}
emoat: {rules_checked: 20, fails: ["H1 and R1 both credit hallmarking formalisation (double credit); recomputed total 7.7", "Section 2C capex estimated by analogy and from guided unsited stores; capex_embedded_growth_pct NOT FOUND (or 4-5% on bracket basis), not 23", "Adjusted total rounds D2 0.7 up to 1; correct sum 9.7", "Completionist recount does not reconcile with evidence_mix (7 vs 10 DOC)"]}
valuation: {rules_checked: 0, fails: [], status: "PENDING PHASE 3"}
expectation_ledger: {status: "PENDING PHASE 3", present: false, downside_row: false, all_rows_confirm_by: false, all_rows_metric_threshold: false, prob_in_range: false, decay_status_valid: false, off_ledger_credit: false, residual_pct_cmp: 0, residual_starter_cap_ok: true, fails: []}
business_understanding_narrative: {status: "PENDING STAGE 13", present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: []}
recomputed_destination_pe: ""
recomputed_decision: ""
recomputed_gate0: {core_score: 69, moat_score: "22 (current peer set) / 21 (B01 peer set)", moats_confirmed: 5, moat_class: "STRONG", classification: "AVERAGE"}
recomputed_emoat: {em_score: 7.7, em_classification: "NONE", capex_embedded_growth_pct: "NOT FOUND (4-5 on Dahod bracket basis)"}
findings:
  - {id: "F-G1", stage: "B01", rule: "M11 network effects", severity: "MAJOR", claimed: "M11 = 3; 6 present; FORTRESS", recomputed: "M11 = 1 (selling % 0.88 FY24 -> 1.06 FY25, combined opex 1.49 -> 1.80 FY24-FY26); 5 present; STRONG", decision_change: false}
  - {id: "F-G2", stage: "B01", rule: "M9 brand, PEER DATA NEEDED", severity: "MINOR", claimed: "PEER DATA NEEDED, 0", recomputed: "peer GM median 19.79 (B01 set) / 13.16 (current set) vs DPABHUSHAN 10.28; score 0", decision_change: false}
  - {id: "F-G3", stage: "B01", rule: "M2/M5 peer set", severity: "MINOR", claimed: "peer median EBITDA 12.62 incl MOTISONS; M2 = 0", recomputed: "median 7.62 with KALYANKJIL; M2 = 1; M5 = 1 unchanged", decision_change: false}
  - {id: "F-G4", stage: "B01", rule: "data confidence tier", severity: "MINOR", claimed: "10+ yrs full", recomputed: "defensible; ratio blocks on FY24-FY26 only; LIMITED tier would not change final AVERAGE", decision_change: false}
  - {id: "F-G5", stage: "B01", rule: "E2 3-year window", severity: "MINOR", claimed: "1-year filed -0.23pp, 3", recomputed: "3-year screener -0.11pp, 3", decision_change: false}
  - {id: "F-E1", stage: "B07", rule: "one improvement one mechanism", severity: "MAJOR", claimed: "H1 2.0 + R1 3.0 on hallmarking", recomputed: "one credit only; total 7.7", decision_change: false}
  - {id: "F-E2", stage: "B07", rule: "Section 2C no estimated inputs", severity: "MAJOR", claimed: "capex 13.75 Cr, growth 23%", recomputed: "NOT FOUND at site level; 4.2-5.0% on Dahod bracket basis", decision_change: false}
  - {id: "F-E3", stage: "B07", rule: "adjusted total arithmetic", severity: "MINOR", claimed: "10", recomputed: "9.7", decision_change: false}
  - {id: "F-E4", stage: "B07", rule: "completionist recount", severity: "MINOR", claimed: "7 DOC items", recomputed: "evidence_mix documented 10; counts must reconcile", decision_change: false}
  - {id: "F-E5", stage: "B07", rule: "Section 6C presentation", severity: "MINOR", claimed: "Core 69/?; FORTRESS; MOTISONS named", recomputed: "Core 69/100; STRONG; peer set SENCO/PNGJL/KALYANKJIL", decision_change: false}
  - {id: "F-E6", stage: "B07", rule: "register items never scored", severity: "MINOR", claimed: "D2 0.7 on digital revenue claim also in register", recomputed: "operator ruling needed; if register-only, D2 0 and total 7.0", decision_change: false}
critical_count: 0
major_count: 3
minor_count: 8
acceptance_rate: 86.7
```
