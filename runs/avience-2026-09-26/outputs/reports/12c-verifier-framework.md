# STAGE 12 VERIFIER C: FRAMEWORK ADHERENCE (PHASE 1 SCOPE)
AVIENCE (Avience Biomedicals Ltd) | Run date 2026-09-26 | Model: claude-opus-5-5

Scope: phase 1 only. Gate 0 (B01) and Emerging Moat (B07) compliance.
The valuation audit (B10/B11, rules 4, 5, 7, 11-15) is PENDING PHASE 3.
Rules 6 (B09 downstream block), 9 (stage 13 narrative) and 10 (B09b dossier)
fall outside the inputs of this pass and are not checked here.

Rule sources: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md.
Audited artifacts: outputs/reports/01-gate0.md + outputs/blocks/B01-gate0.yaml;
outputs/reports/07-emoat.md + outputs/blocks/B07-emoat.yaml.
Spot source reads (rule-application checks only, not number audits):
inputs/screening/screener-Data_Sheet.csv; inputs/prospectus/RHP_Avience_Biomedicals_Jun2026.txt
lines 5172-5176 (page 131 region), 7513-7531 ([page 136], p.131 KPI table), 7612-7626 (p.132 ratio table).

Verifier A owns whether numbers exist in the sources. This pass re-derives
scores from the numbers the reports state, and tests rule application.

---

## PART 1: GATE 0 (B01) COMPLIANCE TABLE

Re-derivation uses the inputs B01 states. Recomputed value shown beside any FAIL.

| # | Rule | B01 value | Re-derived | Result |
|---|---|---|---|---|
| G1 | Opening "Data available" line | 3 years FY24-FY26 | screener sheet holds FY24-FY26 only (screener-Data_Sheet.csv rows 10, 38, 56) | PASS |
| G2 | A1 median ROCE band | 31.5% -> 5 | median(18.6, 34.1, 31.5) = 31.5 -> 5 | PASS |
| G3 | A2 min ROCE band | 18.6% -> 5 | 18.6 >= 15 -> 5 | PASS |
| G4 | A3 median ROE band, closing-NW rule for earliest year stated | 34.7% -> 5 | median(34.7, 49.2, 32.4) = 34.7 -> 5; closing NW use declared | PASS |
| G5 | A4 ROCE trend | 31.5 vs 18.6 -> 5 | latest >= earliest -> 5 | PASS |
| G6 | ROCE source rule: use a source's own ROCE when provided, compute only when absent | computed all 3 years; FY24 approximated | screener has no ROCE row (CSV rows 9-60), so compute is valid for FY25-FY26. For FY24 the RHP, a provided source, prints consolidated ROCE 17.97% (RHP p.131, txt line 7526) / 17.96% (RHP p.132, line 7626). B01 built an estimate instead (see F-G1) | FAIL (MINOR) |
| G7 | Grounded claims: no estimates, N/A where missing (Gate 0 rule 5) | FY24 ROCE approximated via identity plus an assumption that short-term debt was near zero | Assumption not evidenced; implied LT debt 15.18 Cr exceeds total borrowings 15.13 Cr, which shows the inputs are on mixed net-worth bases | FAIL (MINOR), same root as G6, logged once as F-G1 |
| G8 | B1 cumulative CFO/PAT band | 0.573 -> 1 | 10.32 / 18.01 = 0.573 -> 0.50-0.69 -> 1 | PASS |
| G9 | FCF formula: capex = PPE + intangibles purchase, exclude acquisitions; N/A where missing | FY24 capex proxied by total CFI -3.90 Cr | Proxy is an estimate, not the defined line (see F-G2). The DR Meditech acquisition was paid in shares (RHP txt lines 5172-5176), so the proxy does not carry a cash acquisition outflow. Scores do not move | FAIL (MINOR) |
| G10 | B2 FCF-positive proportion | 0% -> 0 | 0 of 3 -> 0. Holds even at FY24 capex = 0 (FCF +1.02): 1 of 3 = 33% -> 0 | PASS |
| G11 | B3 cumulative FCF/PAT | -0.906 -> 0 | negative -> 0. Holds at any FY24 capex >= 0 | PASS |
| G12 | B4 WC days change, Revenue basis stated | +13.0 days FY25->FY26 -> 1 | 199.8 - 186.8 = +13.0 -> 1. FY25 used as earliest available year, disclosed. Reading two (FY24 N/A, score 0) gives Block B 1, same classification | PASS (observation) |
| G13 | Block B total | 2 | 1+0+0+1 = 2 | PASS |
| G14 | C1 revenue CAGR | 48.4% -> 5 | (52.46/23.83)^(1/2) - 1 = 48.4% -> 5 | PASS |
| G15 | C2 PAT CAGR | 101.3% -> 5 | (8.75/2.16)^(1/2) - 1 = 101.3% -> 5 | PASS |
| G16 | C3 positive YoY years | 2/2 -> 5 | 100% -> 5 | PASS |
| G17 | C4 PAT minus revenue CAGR | +52.9pp -> 5 | >= +3pp -> 5 | PASS |
| G18 | CAGR edge rules (negative endpoint, loss-to-profit note) | none triggered; stated in data_notes | all endpoints positive; no swing | PASS |
| G19 | D1 ND/EBITDA | 1.69x -> 3 | 26.00 / 15.39 = 1.69 -> 1-2x -> 3 | PASS |
| G20 | D2 interest cover | 8.34x -> 4 | 14.17 / 1.70 = 8.34 -> 4 | PASS |
| G21 | D3 D/E | 0.921 -> 3 | 28.93 / 31.41 = 0.921 -> 3 | PASS |
| G22 | D4 current ratio | 1.459 -> 2 | 4,316.35 / 2,958.09 = 1.459 -> 1.2-1.49 -> 2 | PASS |
| G23 | E1 promoter holding | 64.59% -> 5 | >= 60 -> 5 | PASS |
| G24 | E2 3-year change | -23.3pp -> 0 | decrease > 3% -> 0; IPO dilution disclosed, not reinterpreted | PASS |
| G25 | E3 pledge | 0% -> 5 | 0 -> 5 | PASS |
| G26 | E4 contingent liab / NW, basis consistent | 1.18% -> 5 | 37.16 / 3,141.30 = 1.18% -> 5; intra-group guarantee excluded on consolidated basis, correct | PASS |
| G27 | Core score sum | 69 | 20+2+20+12+15 = 69 | PASS |
| G28 | M1 pricing power | 5 | +10.1pp margin, CAGR 48.4% -> 5 | PASS |
| G29 | M2 cost advantage vs peer median | 1 | 29.3 vs median(30.1, 19.5, 33.4) = 30.1 -> -0.8pp -> 1 | PASS |
| G30 | M3 capital efficiency | 5 | FAT 3.27x > 3, ROCE 31.5 > 20 -> 5 | PASS |
| G31 | M4 customer stickiness | 3 | 0 decline years, receivable days +22.3 (not +/-10) -> 3 band | PASS |
| G32 | M5 scale | 0 PEER DATA NEEDED | per rule | PASS |
| G33 | M6 R&D | 0 | no R&D/revenue figure -> 0 | PASS |
| G34 | M7 regulatory | 0 PEER DATA NEEDED | listed-player count not in corpus -> per rule | PASS |
| G35 | M8 distribution | 1 | mentioned, unquantified -> 1 | PASS |
| G36 | M9 brand, GM proxy stated | 0 | 37.9 vs 62.7 -> below -> 0 | PASS |
| G37 | M10 switching costs | 0 | receivable days +22.3 > 10; "stable" leg fails for the 3 band -> 0; consistent with M4 reading | PASS |
| G38 | M11 network effects, <6 years handled | 3, partial-history stated | CAGR >= 20, selling % 8.2 -> 6.75 -> 6.39 (CSV rows 11, 17) -> 3 | PASS |
| G39 | M12 negative WC | 0 | 186.8 / 199.8 > 45 -> 0 | PASS |
| G40 | Moat total and class | 18; 4 present; STRONG | M1, M3, M4, M11 >= 3 -> 4 -> STRONG | PASS |
| G41 | Data confidence, classification matrix, deal-breakers | 3 yrs LIMITED; GOOD+ -> GOOD; DB2 triggered; GOOD | Core 69 + STRONG -> GOOD+; LIMITED downgrade -> GOOD; DB2 (Block B 2 < 8) -> max GOOD; DB1, 3-9 not triggered, drivers named | PASS |
| G42 | YAML schema, FLAG-GATE0 condition, analyst_note cap | flags [] ; note ~95 words | classification GOOD > AVERAGE, so FLAG-GATE0 not required | PASS |

Gate 0 rules checked: 42. Fails: 3 rule rows, 2 distinct findings (G6 and G7 are one root, F-G1).
Decision impact: none. Every alternative reading re-derived above leaves Core 67-69,
moat STRONG, classification GOOD.

Sensitivity worked for F-G1: if FY24 ROCE were N/A, A4 compares FY26 31.5 with
FY25 34.1, a 2.6pp decline, score 3. Block A 18, Core 67, still GOOD. If the
RHP's own FY24 ROCE 17.96% is used (the rule-compliant route), A1-A4 stay 5,
Block A 20, Core 69. The compliant route and B01's estimate give the same
score, so the defect is procedural only.

---

## PART 2: EMERGING MOAT (B07) COMPLIANCE TABLE

| # | Rule | B07 value | Re-derived | Result |
|---|---|---|---|---|
| E1 | All 23 rows addressed (A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, I1-I2, R1) | 23 rows | 4+3+2+2+2+2+2+3+2+1 = 23 | PASS |
| E2 | NO EVIDENCE FOUND stated where empty, no force-fit | 15 zero rows each stated | yes | PASS |
| E3 | Likelihood x impact mapping | M/M=2, H/H=4, L/M=1, L/L=1, H/M=3 | matches HH=4, HM=3, MM=2, LM=1, LL=1 | PASS |
| E4 | Evidence multipliers | 1.0 / 0.7 applied | each row checked | PASS |
| E5 | Adjusted total arithmetic | 11.4 | 1.4+2.0+2.8+1.4+0.7+1.0+2.1 = 11.4 | PASS |
| E6 | Band applied | <12 -> NONE | 11.4 < 12 -> NO MEANINGFUL EMERGING MOAT | PASS |
| E7 | Completionist guard applied, recount line present | 7 active, guard not triggered, recount present | 7 < 12 | PASS |
| E8 | Recount accuracy | "5 documented items across 4 categories" | F2 carries a documented item (43 licences on schedule, RHP pdf p.106, labelled 📄 in B07 Section 3) that the recount omits. Recount should read at least 6 items across 5 categories (F-E3) | FAIL (MINOR) |
| E9 | No 🎙️-only category scored at 📄 tier | none | H3 and B1 at 1.0x rest on 📄 items; claim-tier rows at 0.7x | PASS |
| E10 | Score consistent with stated strength; one improvement, one mechanism | B2 H/H = 4 x 0.7 = 2.8 | B07 labels the emerging B2 piece Weak and says the existing mechanic sits in Gate 0 moat_score. H/H is the top cell. Recomputed B2: 0.7 (Weak, L/M) to 1.4 (Moderate, M/M). em_score 9.3 to 10.0, not 11.4 (F-E2) | FAIL (MAJOR) |
| E11 | I1 (Cat 21) both legs, (b) leg 📄 for >0 | 0, both legs absent | correct | PASS |
| E12 | I2 (Cat 22) named sacrifice for >0 | 0, each claimed moat tested | correct | PASS |
| E13 | I1/I2 contribution stated separately | 0 | present | PASS |
| E14 | Section 1 (1A, 1B, 1C) | present | complete | PASS |
| E15 | Section 2C arithmetic: capex x historical FAT = implied INCREMENTAL revenue, as % above current revenue | 30.18 x 3.30 = 99.6; "(99.6/52.51) - 1 = +90%"; capex_embedded_growth_pct 90 | 99.6 is already the increment. % above current = 99.6 / 52.51 = 189.7%. Subtracting 1 treats the increment as total revenue. Recomputed capex_embedded_growth_pct = 190 (F-E1) | FAIL (MAJOR) |
| E16 | Section 4 (4A, 4B, 4C) | present | complete; PLI non-enrolment and shared park incentives stated | PASS |
| E17 | Optionality register present and carried to YAML optionality_register[] | report 8 rows; YAML 7 rows | YAML omits "Manufacturing:trading revenue-mix shift (27:72 toward 50:50)" (F-E4) | FAIL (MINOR) |
| E18 | Section 6C uses injected Gate 0 block | 69 / 18 / 4 / STRONG / GOOD | matches B01-gate0.yaml | PASS |
| E19 | 6D combined classification with reasoning | GOOD | backward GOOD + forward NONE -> GOOD; not HIGH POTENTIAL / TURNAROUND, reasoning given | PASS |
| E20 | Source anchors on evidence items | present throughout | anchor existence is Verifier A's remit | PASS |
| E21 | YAML schema: active_categories holds only Strong/Moderate rows | 7 rows, 4 Weak (A4, F2, H2, H3) | should hold 3 rows (B1, B2, R1) (F-E5) | FAIL (MINOR) |
| E22 | C1 withheld to avoid double credit with B2 | C1 = 0 | correct application | PASS |
| E23 | Taxonomy: EM scan kept separate from FTTCP | stated | correct | PASS |

Emerging Moat rules checked: 23. Fails: 5.
Decision impact: none. Every recomputed em_score (9.3 to 10.0) stays below 12,
so classification NONE and combined GOOD stand. The operator-facing
"borderline, one point below MODEST" framing (B07 Section 5, analyst_note) is
overstated. Corrected, the score sits 2.0 to 2.7 points below the band, and B2
is not a swing item: it already carries more credit than its stated strength.

---

## FINDINGS

| ID | Severity | Location | Finding | Recomputed / fix |
|---|---|---|---|---|
| F-E1 | MAJOR | 07-emoat.md Section 2C; B07 capex_embedded_growth_pct | 2C formula misapplied. B07 subtracts 1 from incremental revenue / current revenue. The rule defines the product as implied incremental revenue, so the ratio is the % above current with no subtraction. The Section 2C and 6A comparison against management's +376-405% peak claim inherits the error. | capex_embedded_growth_pct = 190 (99.6 / 52.51 = 189.7%). This field feeds stage 11 (Pillar 3 catalyst proximity and any CAPACITY revenue basis). Correct it before phase 3. Escalates to CRITICAL if stage 11 consumes 90 as a base-case input. |
| F-E2 | MAJOR | 07-emoat.md Section 5 row B2; Section 3 B2; analyst_note | B2 scored H/H (4) while B07 labels the emerging piece Weak and places the existing reagent-rental mechanic inside Gate 0 moat_score. The score credits the existing moat a second time, against B07's own double-count guard. | B2 adjusted 0.7 to 1.4. em_score 9.3 to 10.0. Classification NONE unchanged. Remove the "borderline / B2 swing item" framing. |
| F-G1 | MINOR | 01-gate0.md Block A, FY24 ROCE; data_note 2 | FY24 ROCE (18.6%) built from an identity plus an unevidenced near-zero short-term-debt assumption. Gate 0 rule 5 bars estimates. The provided RHP prints its own FY24 consolidated ROCE 17.96% (RHP p.132, txt line 7626; 17.97% at p.131, line 7526). Under the formula rule, that anchored figure is the compliant input. | Use 17.96% (RHP p.132) labelled as the RHP's own definition, or mark N/A. A1-A4 unchanged at 5 on the RHP figure. N/A reading gives A4 = 3, Core 67, still GOOD. |
| F-G2 | MINOR | 01-gate0.md Block B, FY24 capex; data_note 3 | FY24 capex proxied by total CFI (-3.90 Cr). Rule 5 requires N/A when the defined line is absent. The proxy does not carry a cash acquisition outflow (DR Meditech was paid in shares, RHP txt lines 5172-5176). | Mark FY24 capex and FCF N/A. B2 and B3 stay 0 under every FY24 value >= 0. No score change. |
| F-E3 | MINOR | 07-emoat.md Section 3 recount line; B07 completionist_recount | Recount omits F2's documented item (43 licences obtained on schedule, RHP pdf p.106, labelled 📄 in B07 itself). | Recount reads at least 6 documented items across 5 categories. Guard outcome unchanged. |
| F-E4 | MINOR | B07-emoat.yaml optionality_register | YAML carries 7 of the report's 8 register rows. Missing: manufacturing:trading mix shift (27:72 toward 50:50), H1 FY27 segment-mix disclosure, near window. | Add the row. Synthesis merges the register into the monitoring checklist, so the omission would drop a watch item. |
| F-E5 | MINOR | B07-emoat.yaml active_categories | Schema says Strong/Moderate rows only. Block carries 4 Weak rows (A4, F2, H2, H3). Downstream counts of "active categories" read 7, not 3. | Keep B1, B2, R1 only, or relabel the field. |

Observation, not a finding: R1 is scored H/M (3 x 0.7 = 2.1) while B07 Section 4C
says the regulatory position "does not differentiate Avience" from licensed peers
and the park incentives are shared. The H/M cell is defensible for the emerging
new-plant approvals piece (likely to be obtained, moderate impact). No score change proposed.

Observation, not a finding: Gate 0 B4 uses FY25 as the earliest year because FY24
payables are missing. B01 discloses this. The alternative reading (B4 N/A, score 0)
gives Block B 1 and the same GOOD classification.

---

## PENDING (NOT IN PHASE 1 SCOPE)

- Valuation audit (rules 4, 5, 7, 11, 12, 15): PENDING PHASE 3. B10/B11 do not exist yet.
- Expectation ledger (rules 13-14): PENDING PHASE 3.
- Business Understanding Narrative (rule 9): PENDING stage 13.
- B09 downstream-candidates block (rule 6) and B09b dossier (rule 10): not among this pass's inputs.
- Carry to phase 3: F-E1 must be corrected before stage 11 reads capex_embedded_growth_pct.

## TOTALS

Rules checked: 65 (Gate 0: 42, Emerging Moat: 23). Rule rows failed: 8. Distinct findings: 7.
Rules passed: 57 of 65 = 87.7%.
Critical 0, Major 2, Minor 5.
No finding changes the Gate 0 classification (GOOD), the EM classification (NONE),
or the combined assessment (GOOD).

```yaml
stage: B12c
company: "AVIENCE"
run_date: "2026-09-26"
model: "claude-opus-5-5"
status: complete
scope: "phase-1 (Gate 0 + Emerging Moat only); valuation audit PENDING PHASE 3"
gate0: {rules_checked: 42, fails: ["G6/G7 FY24 ROCE estimated via identity + unevidenced assumption; RHP p.132 own FY24 consolidated ROCE 17.96% available (MINOR, F-G1)", "G9 FY24 capex proxied by total CFI -3.90 Cr instead of N/A (MINOR, F-G2)"]}
emoat: {rules_checked: 23, fails: ["E15 Section 2C: (99.6/52.51)-1 = 90% applied to an incremental figure; correct 99.6/52.51 = 189.7% -> capex_embedded_growth_pct 190 (MAJOR, F-E1)", "E10 B2 scored H/H=4 x0.7=2.8 while stated emerging strength is Weak and existing mechanic sits in Gate 0; recomputed B2 0.7-1.4, em_score 9.3-10.0, class NONE unchanged (MAJOR, F-E2)", "E8 recount omits F2 documented item; >=6 items across 5 categories (MINOR, F-E3)", "E17 YAML optionality_register omits mix-shift row carried in report (MINOR, F-E4)", "E21 active_categories carries 4 Weak rows against Strong/Moderate-only schema (MINOR, F-E5)"]}
valuation: {rules_checked: 0, fails: [], status: "PENDING PHASE 3 (B10/B11 not yet produced)"}
expectation_ledger: {status: "PENDING PHASE 3", present: false, downside_row: false, all_rows_confirm_by: false, all_rows_metric_threshold: false, prob_in_range: false, decay_status_valid: false, off_ledger_credit: false, residual_pct_cmp: 0, residual_starter_cap_ok: true, fails: []}
business_understanding_narrative: {status: "PENDING STAGE 13", present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: []}
recomputed_destination_pe: ""
recomputed_decision: ""
recomputed_phase1:
  gate0_classification: "GOOD (concur)"
  em_score: "9.3-10.0 (B07 stated 11.4); em_classification NONE (concur)"
  capex_embedded_growth_pct: "190 (B07 stated 90)"
  combined_assessment: "GOOD (concur)"
findings:
  - {id: "F-E1", severity: "MAJOR", location: "07-emoat.md Section 2C; B07 capex_embedded_growth_pct", finding: "2C formula misapplied: -1 subtracted from an incremental-revenue ratio", recomputed: "190 (99.6/52.51 = 189.7%)", note: "feeds stage 11; correct before phase 3; escalates to CRITICAL if stage 11 consumes 90 as a base input"}
  - {id: "F-E2", severity: "MAJOR", location: "07-emoat.md Section 5 row B2; analyst_note", finding: "B2 scored H/H against stated Weak emerging strength; double-credits existing Gate 0 moat", recomputed: "B2 0.7-1.4; em_score 9.3-10.0; NONE unchanged; drop 'borderline / swing item' framing", note: "classification survives"}
  - {id: "F-G1", severity: "MINOR", location: "01-gate0.md Block A FY24 ROCE; data_note 2", finding: "FY24 ROCE estimated; anchored RHP own figure 17.96% (RHP p.132) available", recomputed: "A1-A4 unchanged on RHP figure; N/A reading gives A4=3, Core 67, GOOD", note: "procedural only"}
  - {id: "F-G2", severity: "MINOR", location: "01-gate0.md Block B FY24 capex; data_note 3", finding: "FY24 capex proxied by total CFI instead of N/A", recomputed: "B2=0, B3=0 unchanged for any FY24 capex >= 0", note: "DR Meditech acquisition paid in shares (RHP p.131 region, txt lines 5172-5176)"}
  - {id: "F-E3", severity: "MINOR", location: "07-emoat.md Section 3 recount; B07 completionist_recount", finding: "recount omits F2 documented item (RHP pdf p.106)", recomputed: ">=6 documented items across 5 categories", note: "guard outcome unchanged"}
  - {id: "F-E4", severity: "MINOR", location: "B07-emoat.yaml optionality_register", finding: "7 of 8 report rows carried; mix-shift row missing", recomputed: "add row", note: "synthesis would drop a watch item"}
  - {id: "F-E5", severity: "MINOR", location: "B07-emoat.yaml active_categories", finding: "4 Weak rows in a Strong/Moderate-only field", recomputed: "B1, B2, R1 only", note: "downstream active-category count reads 7 not 3"}
critical_count: 0
major_count: 2
minor_count: 5
acceptance_rate: 87.7             # 57 rule rows passed / 65 checked (phase-1 scope)
```
