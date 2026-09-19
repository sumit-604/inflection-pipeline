# STAGE 12, VERIFIER C: FRAMEWORK ADHERENCE, PHASE 1 SCOPE
Company: Rappid Valves (India) Ltd (RAPPID) | Run date: 2026-09-19 | Model: claude-opus-5

Scope: Gate 0 (B01) and Emerging Moat (B07) only. Rule sources:
prompts/01-gate-0-pipeline.md and prompts/07-emerging-moat-pipeline.md.
The valuation audit (B10, B11, rules 4-7 and 9-15) does NOT run in phase 1.
It is pending phase 3. Valuation framework documents were not loaded.

This verifier audits rule application. Verifier A owns source fidelity. No
number below is a source-fidelity ruling. Where a re-derivation needed a
number, it comes from screener-Data_Sheet.csv (Rs Cr) or
Annual_Report_2026.txt (Rs Lakh, page markers), anchored.

Severity scale: CRITICAL (would change a decision) | MAJOR (wrong, decision
survives) | MINOR (imprecision, presentational).

---

## PART 1: GATE 0 (B01) COMPLIANCE TABLE

Re-derivation inputs: screener-Data_Sheet.csv rows Sales, PBT, Interest,
Other Income, Depreciation, Net profit, Receivables, Inventory, Cash & Bank,
Borrowings, Equity, Reserves, CFO. Current liabilities, payables and capex
for FY22-FY24 cite the RHP, which is not in this verifier's input set; those
values were taken as stated (NOT RE-DERIVABLE here; Verifier A owns them).

| # | Rule | Stage value | Recomputed / check | Result |
|---|---|---|---|---|
| G1 | Opening "Data available" line | 5 yrs FY22-FY26 | Present | PASS |
| G2 | Anchor on every extracted number | Anchored | Spot-checked AR p.27 (Interest Coverage 7.52x, D/E 0.35x, CR 2.55x), p.68 (CL 14.6 Lakh), p.69 (CL 2,351.8 Lakh, Equity 5,171.4 Lakh) | PASS |
| G3 | ROCE: use source's own ROCE where the source provides it; compute only when absent | Computed all 5 years; cross-checked RHP ROCE only | AR p.69, Note 36 ratio table, discloses "Return on capital employed" FY26 14%, FY25 17%. B01 cites the same table for CR (AR p.69) and RoNW, but omits the ROCE row. Not disclosed, not reconciled. Sensitivity under source figures for FY25-26: A2 min ROCE 14% -> 3 (not 5); M3 ROCE 14% -> 1 (not 3) | FAIL, MAJOR |
| G4 | A1 median ROCE | 39.5% -> 5 | EBIT FY22-26 = 1.74, 2.03, 6.84, 9.15, 9.67 (PBT + Interest - OI, screener). Sorted 18.7/20.2/39.5/47.7/85.4, median 39.5% -> 5. Same median under G3 source reading | PASS |
| G5 | A2 min ROCE | 18.7% -> 5 | Correct on computed basis; 3 under G3 reading | PASS (see G3) |
| G6 | A3 median ROE; "if opening NW unavailable, use closing and state so" | FY22 excluded; median 27.5% -> 5 | Rule says use closing NW; it gives no exclusion clause. FY22 = 0.29 / -0.25 = -116% included -> median of 5 = 22.9% -> 5. Score unchanged; exclusion is an unwritten step | FAIL, MINOR |
| G7 | A4 ROCE trend latest vs earliest | -66.7pp -> 0 | 18.7 vs 85.4 -> >5pp decline -> 0 | PASS |
| G8 | B1 cum CFO / cum PAT | -1.46 -> 0 | -25.42 / 17.40 = -1.46 (screener) -> 0 | PASS |
| G9 | B2 FCF-positive years | 1 of 5 -> 0 | Only FY22 positive -> 20% -> 0 | PASS |
| G10 | B3 cum FCF / cum PAT | negative -> 0 | Negative under any capex figure (CFO alone negative) -> 0 | PASS |
| G11 | B4 WC days change; revenue basis unless COGS explicit, basis stated | +183.9d -> 0 | FY22 79.1+138.3-67.1 = 150.3; FY26 170.3+183.0-19.0 = 334.2 -> +183.9 -> 0. No explicit COGS line in screener; revenue basis stated | PASS |
| G12 | C1 revenue CAGR | 44.7% -> 5 | (53.23/12.14)^0.25 - 1 = 44.7% | PASS |
| G13 | C2 PAT CAGR | 117.4% -> 5 | (6.48/0.29)^0.25 - 1 = 117.4%; both endpoints positive | PASS |
| G14 | C3 positive YoY years | 4/4 -> 5 | All four YoY positive | PASS |
| G15 | C4 PAT CAGR minus rev CAGR | +72.7pp -> 5 | Correct | PASS |
| G16 | CAGR edge rules (N/M endpoints, swing note, C4) | No swing noted | No negative endpoint; PAT positive all 5 years; data_note present | PASS |
| G17 | D1 ND/EBITDA | 1.49x -> 3 | EBITDA check: 8.66+1.33+0.64-0.32 = 10.31 (screener) = AR 1,030.9 Lakh. (17.85-2.51)/10.31 = 1.49 -> 3. If Investments 4.76 Cr are treated as cash: 1.03x, same band | PASS |
| G18 | D2 EBIT / Interest | 7.52x disclosed -> 4 | Rule formula EBIT/Interest = 9.67/1.33 = 7.27x. Stage scored the disclosed ratio (AR p.27) and showed the formula value; same band | PASS |
| G19 | D3 D/E | 0.35 -> 4 | 17.85/51.71 = 0.345 -> 4 | PASS |
| G20 | D4 current ratio | 2.55 -> 5 | AR p.69: 6,008.4 / 2,351.8 = 2.55 -> 5 | PASS |
| G21 | E1 promoter holding latest | 51.58% -> 4 | 50-59.9 band -> 4; Mar-2026 latest available, gap stated | PASS |
| G22 | E2 promoter holding change over 3 years | +0.45pp over ~2 yrs -> 3 | Rule measures holding change over 3 years. It does not distinguish dilution from selling (Rule 2: no qualitative judgment). The stage replaced the window with the 18-month listed window. The only same-window comparator the stage itself cites is 69.46% pre-issue (RHP p.95) against 51.58% Mar-2026 (AR p.60): a 17.88pp decrease -> >3% -> 0 | FAIL, MAJOR |
| G23 | E3 pledge | 0% -> 5 | Correct | PASS |
| G24 | E4 contingent liabilities / NW | 0.28% -> 5 | 14.6 / 5,171.4 = 0.28% -> 5. Observation: AR p.69 Note 37(iii) states "no capital commitments and contingent liabilities as on March 31, 2026", which conflicts with Note 34 (AR p.68). Both readings score 5 | PASS |
| G25 | M1 pricing power | +6.3pp FY23-26 -> 5 | Stage used a 3-year window (FY23-26) while every other block uses FY22-26. Full-window check: EBITDA FY22 = 0.29+1.46+0.20-0.01 = 1.94 -> 16.0%; FY26 19.4%; +3.4pp, rev CAGR 44.7% -> 5. Score unchanged | PASS |
| G26 | M2, M5, M9 peer tests | 0, PEER DATA NEEDED | Rule-compliant | PASS |
| G27 | M3 capital efficiency | FAT 5.18x, ROCE 18.7% -> 3 | 53.23/10.28 = 5.18x. Correct on computed ROCE; 1 under G3 reading | PASS (see G3) |
| G28 | M4 customer stickiness | 3 | Top tier blocked by receivable days +91. Tier "max 1 decline year, fully recovered" literally includes 0 decline years -> 3 | PASS |
| G29 | M6, M7, M8 | 0, 0, 1 | Rule-compliant | PASS |
| G30 | M10 switching costs | 0 | Score 0 is correct: tier 1 needs "2+ decline years" and there are 0; tier 3 needs stable receivables. But the stated reason ("≤10-day threshold required even at the loosest scoring tier") misstates the rule: the loosest tier has no receivable condition | FAIL, MINOR (reasoning only) |
| G31 | M11 network effects, <6 yrs rule | 3 | 5 yrs, overall-trend basis stated; S&A % 5.35% FY22 -> 3.87% FY26 (screener); rev CAGR ≥20% -> 3 | PASS |
| G32 | M12 negative WC | 0 | WC days 150-334 -> >45 -> 0 | PASS |
| G33 | Moat count and class | 4, STRONG | M1, M3, M4, M11 ≥3 -> 4 -> STRONG on the stage's basis. Under G3 reading M3 drops -> 3 moats -> MODERATE | PASS (see G3) |
| G34 | Data confidence: 5-6 yrs -> flag "may not have seen full cycle" | Stated in report | The flag is absent from the B01 YAML flags and data_notes. Downstream stages read the block, not the report | FAIL, MINOR |
| G35 | Classification matrix | Core 68 + STRONG -> GOOD+ | Correct on stage basis | PASS |
| G36 | Deal-breakers applied, driving years stated | #2 and #4, AVERAGE | Both triggered; #4 governs; years FY23-FY26 CFO named | PASS |
| G37 | FLAG-GATE0 emitted with coherent reason | Present | Flag reason sets FY23-26 cumulative CFO (-26.56) against FY22-26 cumulative PAT (17.40). Window mismatch. The block_b_trend field uses the matched FY23-26 PAT (17.11) | FAIL, MINOR |

### Gate 0 recomputed position

| Item | Stage | E2 fix only | E2 fix + G3 source-ROCE reading |
|---|---|---|---|
| Block A | 15 | 15 | 13 |
| Block E | 17 | 14 | 14 |
| Core | 68 | 65 | 63 |
| Moat score | 15 | 15 | 13 |
| Moats confirmed / class | 4 / STRONG | 4 / STRONG | 3 / MODERATE |
| Grand total | 83 | 80 | 76 |
| Raw classification | GOOD+ | GOOD+ | GOOD |
| Final classification | AVERAGE | AVERAGE | AVERAGE |

The final classification survives every reading. Deal-breaker #4 (cumulative
CFO/PAT -1.46) caps it. Both MAJOR findings change inputs that feed the B07
6C combined table and downstream moat framing. Neither changes the decision.

Gate 0: 37 rules checked, 6 fails (2 MAJOR, 4 MINOR).

---

## PART 2: EMERGING MOAT (B07) COMPLIANCE TABLE

| # | Rule | Stage value | Recomputed / check | Result |
|---|---|---|---|---|
| M-1 | All 23 rows (22 categories + R1) addressed or NO EVIDENCE FOUND | 23 rows | All present in Section 3, summary table, and Section 5 | PASS |
| M-2 | Evidence taxonomy plus source anchor on every item | [D]/[M]/[I] declared | H2's 📄 item anchors to "Inv. Pres. p.6 (Milestones); company memory". Company memory is memory to weigh, never evidence (CLAUDE.md). The deck anchor alone carries it | FAIL, MINOR |
| M-3 | Raw L×I values drawn from the matrix | All values legal | HH=4, HM=3, MM=2, LM/ML/LL=1, none=0 | PASS |
| M-4 | Evidence multiplier matches stated tier (📄 1.0, 🎙️ 0.7, 🔍 0.5) | F2: "🎙️/📄 mixed, 0.5" | 0.5 is the 🔍 multiplier. F2's evidence table lists [D] items only (capex delivery, B05 record). No "mixed" multiplier exists. At 📄 F2 = 1.0; at 🎙️ F2 = 0.7. Total 19.2 -> 19.7 or 19.4. Band unchanged (MODEST). A3 scored at 🔍 0.5 while its only listed item is [D] (AR p.15): the lower multiplier is defensible because the impact leg is inference, and it is not counted as a fail | FAIL, MINOR |
| M-5 | No 🎙️-only category scored or described as 📄 | Scores correct | C1 is scored at 🎙️ 0.7 (correct). But 6D states "5 categories score Strong/Moderate on 📄-grade evidence (A1, B2, C1, E2, R1)". C1 is 🎙️-grade by the stage's own scoring and recount. Narrative misstates the tier | FAIL, MINOR |
| M-6 | Adjusted total arithmetic | 19.2 | 4.0+0.5+4.0+2.1+0.7+2.0+0.5+1.4+1.0+3.0 = 19.2 | PASS |
| M-7 | Classification band | MODEST (12-24) | 19.2 -> MODEST. All sensitivities below stay in 12-24 | PASS |
| M-8 | Section 3 summary table: evidence, type, strength, time; Strong/Moderate count stated | 5 | Present | PASS |
| M-9 | Completionist recount line "📄 recount performed: [n] documented items across [m] categories" | "approximately 9 ... across 4 categories" | The rule asks for a count, not an estimate. The UL approval is counted twice (A1 and E2), so distinct items = 8. H2 is scored at the 📄 1.0 multiplier but is absent from the 📄 recount, so the recount and the scorecard disagree on which categories hold 📄 evidence (5, not 4) | FAIL, MINOR |
| M-10 | Completionist guard (stop at ≥12 active) | 5 active | Below threshold; inside 3-6 base rate | PASS |
| M-11 | Category 21 (I1) present; >0 only if both legs evidenced, (b) leg with ≥1 📄 | 0 | Present, 0, reason given | PASS |
| M-12 | Category 22 (I2) present; test answered "for each moat claimed anywhere in this scan" | 0 | Score 0 is compliant. The Section 3 test is worked for B2 only. The analyst_note asserts "nothing must be destroyed" for every moat without showing A1, C1, E2, R1 | FAIL, MINOR |
| M-13 | I1/I2 contribution stated separately | 0.0 of 19.2 | Present | PASS |
| M-14 | Optionality register: items scored 0 or resting only on 🎙️/🔍; carried in YAML | 7 rows report, 6 rows YAML | The A3 process-innovation row in the report is missing from the YAML optionality_register. H1 (🎙️ only, single CMD claim) and C2 (🎙️ only) meet the register test and are absent. Synthesis merges from the block, so dropped rows never reach the monitoring checklist | FAIL, MINOR |
| M-15 | Section 1 (1A, 1B, 1C) complete | Present | NOT FOUND used where no numeric target exists | PASS |
| M-16 | Section 2C arithmetic shown | 12.2% | 1.25 × 5.18 = 6.475; 6.475 / 53.23 = 12.2%. The 1.25 Cr input is 🎙️ (Jun-2026 call p.14); stated | PASS |
| M-17 | Section 4 (4A, 4B, 4C) complete | Present | Shared-not-exclusive stated | PASS |
| M-18 | 6C uses the injected B01 block | Core 68, 4 moats, AVERAGE | Matches B01 as emitted (see Part 1 for B01's own fails) | PASS |
| M-19 | 6D combined classification with reasoning | AVERAGE | The standard matrix labels are listed in prompts/07 but its cell mapping is not written there. Checked for internal consistency: AVERAGE backward + MODEST forward does not meet any HIGH POTENTIAL or TURNAROUND condition the stage states | PASS |
| M-20 | Emerging Moat not conflated with FTTCP | Stated at head | No FTTCP naming or reuse | PASS |
| M-21 | B07 YAML schema fields present | All present | em_score rounded 19.2 -> 19; stated | PASS |

### Emerging Moat observations (judgment, not scored as fails)

- A1 scores HH=4 as "rare manufacturing capability". The rarity leg rests on
  the company phrase "select group of Indian manufacturers" (a claim). The
  stage's own 6B says KSB, Atam and Quest Flow hold overlapping
  certifications.
- B2 scores HH=4 as "qualification lock-in". The stage's own I2 test calls
  the same barrier an execution lead that closes. Its 6B says PSU tenders
  stay open reverse-auction, not sole-source.
- H1 is labelled Weak in Section 3 but scored MM=2, the same raw as E2
  (Moderate).
- Sensitivity: A1 and B2 at HM=3 each and H1 at LM=1 give a total of 16.5.
  F2 at 📄 adds 0.5 to give 17.0. Every combination stays in the MODEST band
  (12-24). No classification change.

Emerging Moat: 21 rules checked, 6 fails (all MINOR).

---

## PART 3: VALUATION (B11)

NOT RUN. Phase 1 scope. Pending phase 3 (rules 4-7 and 9-15, expectation
ledger, business understanding narrative, method plurality, skill-to-source
fidelity).

---

## SUMMARY

| Framework | Rules checked | Fails | CRITICAL | MAJOR | MINOR |
|---|---|---|---|---|---|
| Gate 0 (B01) | 37 | 6 | 0 | 2 | 4 |
| Emerging Moat (B07) | 21 | 6 | 0 | 0 | 6 |
| Valuation (B11) | 0 | pending phase 3 | - | - | - |
| Total | 58 | 12 | 0 | 2 | 10 |

Acceptance rate: 46 / 58 = 79.3%. The denominator is 4 or more, so the rate
applies. It sits above the 60% REWORK trigger.

The Gate 0 final classification (AVERAGE) and the Emerging Moat
classification (MODEST) both survive every recomputation. The two MAJOR
findings are rework candidates for stage 1 at operator discretion: E2 window
substitution and the omitted AR ROCE disclosure. The raw classification can
fall from GOOD+ to GOOD, and the moat class from STRONG to MODERATE. The B07
6C table and any downstream text that quotes "4 moats, STRONG" inherit that.

```yaml
stage: B12c
company: "RAPPID"
run_date: "2026-09-19"
model: "claude-opus-5"
status: complete
scope: "phase1 (gate0 + emoat only; valuation pending phase 3)"
gate0: {rules_checked: 37, fails: ["G3 ROCE source-precedence: AR p.69 Note 36 ROCE FY26 14% / FY25 17% omitted and unreconciled (MAJOR)", "G22 E2 window substituted; 3-yr rule gives 69.46% -> 51.58% = -17.88pp -> 0 not 3 (MAJOR)", "G6 A3 FY22 ROE excluded, rule has no exclusion; score unchanged (MINOR)", "G30 M10 stated reason misstates loosest tier; score 0 correct (MINOR)", "G34 'may not have seen full cycle' flag absent from B01 YAML (MINOR)", "G37 FLAG-GATE0 reason mixes FY23-26 CFO with FY22-26 PAT window (MINOR)"]}
emoat: {rules_checked: 21, fails: ["M-2 H2 documented item anchored partly to company memory (MINOR)", "M-4 F2 multiplier 0.5 applied to D-tier evidence; total 19.2 -> 19.4/19.7, band unchanged (MINOR)", "M-5 6D narrative calls C1 documented-grade; scored as claim (MINOR)", "M-9 recount 'approximately 9', UL double-counted (8 distinct), H2 scored 1.0 but omitted from recount (MINOR)", "M-12 I2 test worked for B2 only, not each claimed moat; score 0 unaffected (MINOR)", "M-14 optionality register: A3 row dropped from YAML; H1 and C2 claim-only rows absent (MINOR)"]}
valuation: {rules_checked: 0, fails: [], note: "NOT RUN - pending phase 3"}
expectation_ledger: {not_run: true, note: "pending phase 3", present: false, downside_row: false, all_rows_confirm_by: false, all_rows_metric_threshold: false, prob_in_range: false, decay_status_valid: false, off_ledger_credit: false, residual_pct_cmp: 0, residual_starter_cap_ok: true, fails: []}
business_understanding_narrative: {not_run: true, note: "pending phase 3 (stage 13)", present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: []}
recomputed_destination_pe: ""
recomputed_decision: ""
recomputed_gate0: "Final AVERAGE unchanged. E2 fix: core 65, grand 80, raw GOOD+. E2 fix + source-ROCE reading: A 13, E 14, core 63, moat 13, 3 moats MODERATE, grand 76, raw GOOD."
recomputed_emoat: "em_score 19.2 -> 19.4-19.7 on F2 multiplier fix; MODEST unchanged under all sensitivities (floor 16.5)."
findings:
  - {id: G3, stage: B01, severity: MAJOR, rule: "ROCE: use source's own ROCE where provided", claimed: "computed ROCE FY26 18.7%, FY25 20.2%; A2=5, M3=3, 4 moats STRONG", recomputed: "AR p.69 Note 36 ROCE FY26 14%, FY25 17% -> A2=3, M3=1, 3 moats MODERATE, raw GOOD", decision_impact: "none; final AVERAGE held by deal-breaker 4"}
  - {id: G22, stage: B01, severity: MAJOR, rule: "E2 promoter holding change over 3 years", claimed: "+0.45pp over Sep-2024 to Mar-2026 -> 3", recomputed: "69.46% pre-issue (RHP p.95) to 51.58% (AR p.60) = -17.88pp -> 0; Block E 14, core 65", decision_impact: "none; final AVERAGE unchanged"}
  - {id: G6, stage: B01, severity: MINOR, rule: "A3 ROE closing-NW fallback", claimed: "FY22 excluded, median 27.5%", recomputed: "FY22 included, median 22.9% -> 5 unchanged", decision_impact: "none"}
  - {id: G30, stage: B01, severity: MINOR, rule: "M10 tiers", claimed: "loosest tier needs receivable days <=10", recomputed: "loosest tier needs 2+ decline years, no receivable test; score 0 correct", decision_impact: "none"}
  - {id: G34, stage: B01, severity: MINOR, rule: "5-6 yr data confidence flag", claimed: "flag in report only", recomputed: "flag missing from YAML flags/data_notes", decision_impact: "none"}
  - {id: G37, stage: B01, severity: MINOR, rule: "FLAG-GATE0 reason coherence", claimed: "FY23-26 CFO -26.56 vs PAT 17.40", recomputed: "matched window PAT FY23-26 = 17.11 (screener)", decision_impact: "none"}
  - {id: M-2, stage: B07, severity: MINOR, rule: "anchor every evidence item to a filed source", claimed: "H2 anchored to Inv. Pres. p.6 + company memory", recomputed: "drop memory anchor; deck anchor stands", decision_impact: "none"}
  - {id: M-4, stage: B07, severity: MINOR, rule: "evidence multiplier per tier", claimed: "F2 LL x 0.5 = 0.5", recomputed: "F2 LL x 1.0 = 1.0 (D) or x 0.7 = 0.7 (M); total 19.4-19.7", decision_impact: "none; MODEST"}
  - {id: M-5, stage: B07, severity: MINOR, rule: "claim-only category not treated as documented", claimed: "6D: C1 on documented-grade evidence", recomputed: "C1 scored and recounted as management claim", decision_impact: "none"}
  - {id: M-9, stage: B07, severity: MINOR, rule: "completionist recount line", claimed: "approximately 9 items, 4 categories", recomputed: "8 distinct items (UL counted twice); 5 categories incl. H2 scored at 1.0", decision_impact: "none"}
  - {id: M-12, stage: B07, severity: MINOR, rule: "I2 answered for each moat claimed", claimed: "worked for B2 only", recomputed: "A1, C1, E2, R1 not shown; score 0 unaffected", decision_impact: "none"}
  - {id: M-14, stage: B07, severity: MINOR, rule: "optionality register carries 0-scored and claim/inference-only items in YAML", claimed: "6 YAML rows", recomputed: "add A3 (in report), H1 and C2 (claim-only)", decision_impact: "none; monitoring checklist incomplete"}
critical_count: 0
major_count: 2
minor_count: 10
acceptance_rate: 79             # 46 / 58 = 79.3%
```
