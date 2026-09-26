# Stage 12 Verifier C: Framework Adherence. QUALITEK, run 2026-09-26

Scope: phase 1 only. Audited B01 (Gate 0) against prompts/01-gate-0-pipeline.md and B07 (Emerging Moat) against prompts/07-emerging-moat-pipeline.md. The valuation audit (B10, B11, rules 4-7, 11-15) is PENDING PHASE 3. Raw-number fidelity belongs to Verifier A. This audit takes the stated inputs as given and re-derives the scores.

Result: 62 rules checked, 56 PASS, 6 FAIL (0 CRITICAL, 6 MAJOR), 7 MINOR notes. Acceptance 90.3%. No fail changes the Gate 0 classification (AVERAGE) or the combined assessment (AVERAGE).

## 1. GATE 0 (B01) compliance table

Sources: 01-gate0.md, B01-gate0.yaml. Thresholds: prompts/01-gate-0-pipeline.md lines 54-159.

| # | Rule | Stated | Re-derived | Verdict |
|---|---|---|---|---|
| 1 | A1 Median ROCE band | 10.02% -> 3 | Sorted 6.38, 7.4, 9.34, 10.7, 13.76, 15.41; median 10.02%. Band 10-14.9 = **1** (prompt line 55) | **FAIL (MAJOR)** |
| 2 | A2 Min ROCE | 6.38% -> 0 | <8 = 0 | PASS |
| 3 | A3 Median ROE | 14.63% -> 2 | (8.9+20.36)/2 = 14.63; band 12-14.9 = 2 | PASS (basis note, MINOR) |
| 4 | A4 ROCE trend | 7.4 vs 6.38 -> 5 | latest >= earliest = 5 | PASS |
| 5 | B1 CFO/PAT | 1.09 -> 5 | 2,410.81 / 2,212.09 = 1.090 | PASS |
| 6 | B2 FCF+ years | 0/6 -> 0 | 0% = 0 | PASS |
| 7 | B3 FCF/PAT | -3.15 -> 0 | -6,961.27 / 2,212.09 = -3.147 | PASS |
| 8 | B4 WC days change | +145.76 -> 0 | -65.49 to 80.27, >15 up = 0 | PASS |
| 9 | C1 Revenue CAGR | 60.47% -> 5 | (6,762.45/635.49)^(1/5)-1 = 60.47% | PASS |
| 10 | C2 PAT CAGR | 76.8% -> 5 | (796.44/46.11)^(1/5)-1 = 76.8% | PASS |
| 11 | C3 Positive YoY | 5/5 -> 5 | 100% = 5 | PASS |
| 12 | C4 PAT minus Rev CAGR | +16.3pp -> 5 | >= +3pp = 5 | PASS |
| 13 | D1 ND/EBITDA | 3.75x -> 0 | 6,285.25 / 1,676.01 = 3.750 | PASS |
| 14 | D2 Interest cover | 4.80x -> 2 | 1,212.57 / 252.84 = 4.796, band 3-4.9 | PASS |
| 15 | D3 D/E | 0.45 -> 4 | 6,499.19 / 14,575.06 = 0.446 | PASS (basis note, MINOR) |
| 16 | D4 Current ratio | 0.92 -> 0 | <1.0 = 0 | PASS |
| 17 | E1 Promoter holding | 56.46% -> 4 | band 50-59.9 = 4; screener source flagged as not a filing | PASS |
| 18 | E2 Promoter change | -16.89pp -> 0 | decreased >3% = 0 | PASS (window label, MINOR) |
| 19 | E3 Pledge | N/A -> 0 | rule 5 N/A = 0, not treated as a trigger | PASS |
| 20 | E4 CL/NW | 14.63% -> 3 | 2,133.00 / 14,575.06 = 14.63%, band 5-15 | PASS |
| 21 | M1 Pricing power | 5 | 16.57% to 24.78%, +8.2pp, CAGR >= 10 | PASS (basis note, MINOR) |
| 22 | M2 Cost advantage | 0 PEER DATA NEEDED | correct handling | PASS |
| 23 | M3 Capital efficiency | 0 | FAT 0.72x, not >1x | PASS |
| 24 | M4 Stickiness | 3 | 0 decline years satisfies "max 1 decline year" tier; receivables not +/-10 so not 5 | PASS |
| 25 | M5 Scale | 0 PEER DATA NEEDED | correct | PASS |
| 26 | M6 R&D | 0 | none disclosed | PASS |
| 27 | M7 Regulatory | 1 | margin range >10pp rules out 3 and 5; 1 not "present" | PASS (no effect on count) |
| 28 | M8 Distribution | 3 | network growing, CAGR >= 15 | PASS |
| 29 | M9 Brand | 0 PEER DATA NEEDED | correct | PASS |
| 30 | M10 Switching | 0 | receivables +37.29 days, no tier fits | PASS |
| 31 | M11 Network | 0 | two-window test impossible on 6 points; fallback also 0 (selling % undisclosed) | PASS (window note, MINOR) |
| 32 | M12 Neg WC | 0 | not negative in majority, last 3 years >45 | PASS |
| 33 | Moat class | 3 present, MODERATE, 12/60 | M1, M4, M8 >= 3; sum 12 | PASS |
| 34 | Data confidence / downgrade | 6 yrs, lower, no downgrade | 5-6 band flags, no tier downgrade | PASS |
| 35 | Classification matrix | Core 48 -> AVERAGE | Core 46 -> 40-59 -> AVERAGE | PASS (outcome unchanged) |
| 36 | Deal-breakers | only #2 fires, non-binding | #1: Block A 8, not <8, does not fire (zero headroom). #3: median 10.02% not <10 (0.02pp headroom). #6 joint condition not met. #2 fires, non-binding | PASS |
| 37 | CAGR edge rules | no N/M | both endpoints positive, no loss swing | PASS |
| 38 | ROCE source-vs-compute rule | source where given, FY24 computed | rule followed; mixed basis disclosed | PASS |
| 39 | N/A and PEER DATA NEEDED handling | no estimates | rule 5 honoured throughout | PASS |
| 40 | YAML schema and FLAG-GATE0 | present | FLAG-GATE0 raised for AVERAGE with named depressor; block_b_trend carries one number | PASS |

Recomputed Gate 0: Block A 8 (1+0+2+5), core **46**, moat 12, grand total **58**, classification **AVERAGE** (unchanged).

Deal-breaker sensitivity. Two deal-breakers sit at their lines. Block A lands exactly on 8. Median ROCE sits 0.02pp above 10%. The median depends on FY24 ROCE (15.41%), the one year computed on a different capital base. Either trigger caps at GOOD or AVERAGE, and the matrix already gives AVERAGE. Neither can change the outcome.

## 2. EMERGING MOAT (B07) compliance table

Sources: 07-emoat.md, B07-emoat.yaml. Rules: prompts/07-emerging-moat-pipeline.md.

| # | Rule | Stated | Re-derived | Verdict |
|---|---|---|---|---|
| 1 | Six sections present | yes | Sections 1-6 plus optionality register | PASS |
| 2 | All 23 categories addressed or NO EVIDENCE | yes | 22 in Section 3, R1 in Section 4 | PASS |
| 3 | Section 3 summary table, 23 rows | yes | 23 rows | PASS |
| 4 | Scorecard, 23 rows | yes | 23 rows | PASS |
| 5 | Raw matrix values legal | LL=1, MM=2, HM/MH=3 | all legal | PASS |
| 6 | Multiplier arithmetic as applied | 15.4 | 2+0.7+3+3+2+0.5+0.5+3+0.7 = 15.4 | PASS |
| 7 | A1 tier consistency | MM x 1.0 = 2.0 | Documented fact is the lab acquisition. The moat attribute, "few domestic labs hold USFDA", has no anchor. Report admits no manufacturer-count or qualification-timeline evidence. Inference tier: 2 x 0.5 = **1.0** | **FAIL (MAJOR)** |
| 8 | E1 tier consistency | MM x 1.0 = 2.0 | "First-mover under PPP" and "first-of-kind among small-cap peers" are not stated in any cited document. Inference tier: **1.0** | **FAIL (MAJOR)** |
| 9 | H2 tier consistency | HM x 1.0 = 3.0 | Only anchor is the Inv. Pres. deck. Report states no contract value or exclusivity is disclosed. Prompt line 30-33: a presentation statement not backed by signed contracts is a management claim. 3 x 0.7 = **2.1** | **FAIL (MAJOR)** |
| 10 | Other scored rows tier | A3 C, B2 D, C1 D, F1 I, H1 I, R1 C | consistent with anchors | PASS |
| 11 | Completionist recount performed | yes | line present in report and YAML | PASS |
| 12 | Recount accuracy | 17 documented items, 5 categories | USFDA lab counted in A1, B2 and E1. Bhubaneswar PPP 2018 (E1) and the MSMED PPP with Utkal Pharma Mfr. Assn. since 2018 (C1) are probably one arrangement [INFERENCE: Utkal is Odisha, Bhubaneswar is its capital; confirm in the deck page 21]. H2's 7 items are claim tier. Distinct documented items: 8 to 10 | **FAIL (MAJOR)** |
| 13 | Completionist guard threshold | 9 categories > 0 | under 12, no forced re-examination | PASS |
| 14 | Classification band | 15.4 -> MODEST | see recompute below | PASS (margin thin) |
| 15 | Category 21 (I1) | 0 | neither leg evidenced; director pay correctly rejected as leg (a) | PASS |
| 16 | Category 22 (I2) | 0 | named competitors can copy without a P&L sacrifice; execution lead, not configuration | PASS |
| 17 | I1/I2 contribution stated separately | 0.0 | stated | PASS |
| 18 | 2C capex-embedded growth | 63 x 1.74 = 88% | Rule (prompt line 60-62): capex UNDER EXECUTION x HISTORICAL FAT. FY27 Rs 63 Cr is ANNOUNCED with funding NOT FOUND. 1.74x is one year of consolidated revenue over net PPE, excluding CWIP and intangibles. B01 FAT on PPE+CWIP+intangibles is 0.72x: 63 x 0.72 = 45.4 Cr, about 36% of Rs 124.5 Cr. That mixes a standalone turnover with a consolidated base, so a clean single-basis figure is NOT DETERMINABLE from the inputs. 88 is overstated | **FAIL (MAJOR)** |
| 19 | Optionality register | 8 rows | all 0-scored or C/I-only, each with converting evidence and window | PASS |
| 20 | Section 6 A-E; 6C uses injected B01 | yes | all present; 6C carries B01 core 48 (recomputed 46, no class effect) | PASS |
| 21 | YAML schema | complete | all fields present | PASS |
| 22 | Source anchors on evidence | yes | line and filing anchors throughout | PASS |

### Recomputed em_score

| Row | Stated | Recomputed |
|---|---|---|
| A1 | 2.0 | 1.0 |
| A3 | 0.7 | 0.7 |
| B2 | 3.0 | 3.0 |
| C1 | 3.0 | 3.0 |
| E1 | 2.0 | 1.0 |
| F1 | 0.5 | 0.5 |
| H1 | 0.5 | 0.5 |
| H2 | 3.0 | 2.1 |
| R1 | 0.7 | 0.7 |
| Total | 15.4 | **12.5** |

12.5 stays MODEST (12-24), 0.5 above the NO MEANINGFUL line. De-duplication decides the band. If E1 is struck as a restatement of C1 (PPP) and B2 (USFDA), the total is 11.5 and the class falls to NO MEANINGFUL EMERGING MOAT. The two readings: (a) A1, B2 and E1 score different attributes of one fact, so multi-category credit stands; (b) one fact earns one credit (CLAUDE.md, one improvement through one mechanism). The separating observation: a document that shows the USFDA lab's scarcity or first-mover position apart from its accreditation. The corpus has none. The combined assessment stays AVERAGE under both readings. The EM >= 25 UA qualifier fails under both.

## 3. Findings

| Severity | Location | Finding |
|---|---|---|
| MAJOR | 01-gate0.md A1 | 10.02% scored 3; band gives 1. Block A 8, core 46, grand 58. AVERAGE unchanged. Deal-breaker 1 at zero headroom. |
| MAJOR | 07-emoat.md A1 | Inference-grade scarcity claim scored at the documented multiplier. 2.0 to 1.0. |
| MAJOR | 07-emoat.md E1 | Inference-grade first-mover claim scored at the documented multiplier. 2.0 to 1.0. |
| MAJOR | 07-emoat.md H2 | Deck-only partner list, no contracts, scored as documented. 3.0 to 2.1. |
| MAJOR | 07-emoat.md recount; B07 evidence_mix | USFDA lab counted three times; PPP 2018 probably twice; H2 items are claims. "17 documented" overstates. Band sensitive to de-duplication. |
| MAJOR | 07-emoat.md 2C; B07 capex_embedded_growth_pct | 88% uses announced capex and a single-year, narrow-base turnover. Downstream must not use 88 as an input. |
| MINOR | 01-gate0.md E2 | "~3 years" is 2 years (Mar-2024 to Mar-2026). Score unaffected. |
| MINOR | 01-gate0.md M11 | Prior window is 2 years. Fallback also scores 0. Score unaffected. |
| MINOR | 01-gate0.md FY24 CFO | Line 59 says "WC-adjusted"; data_note says "before WC changes". If pre-WC, the figure is not CFO. B1 holds unless true FY24 CFO is below Rs 354.79 lakh. Referred to Verifier A. |
| MINOR | 01-gate0.md A3 | ROE rule has no use-source exception; FY21-23 DRHP ROE taken as printed, FY24 computed. Mixed basis on a 2-point item. |
| MINOR | 01-gate0.md M1 | FY26 EBITDA built from PBT (includes other income); FY21 from the DRHP line. M1 holds unless the basis gap exceeds about 6pp. |
| MINOR | 01-gate0.md D3 and analyst_note | Standalone D/E 0.45 is read as low leverage. B07 cites consolidated D/E 1.25. On 1.25, D3 scores 1 and core falls to 43, still AVERAGE. Do not carry 0.45 forward as group leverage. |
| MINOR | 07-emoat.md line 80 | Stray non-English token in B2 prose. "Renewable" contract claim is inference, not in the cited Reg 30 terms. |

Coverage: 40 Gate 0 rules (20 metric scores, 12 moat tests, 8 structural rules) and 22 Emerging Moat rules. Every Gate 0 metric was re-derived from its stated inputs. Every B07 scored row was checked for tier consistency.

```yaml
stage: B12c
company: "QUALITEK"
run_date: "2026-09-26"
model: "claude-opus-5-5"
status: complete
scope: "phase-1 (Gate 0 B01 + Emerging Moat B07 only); valuation audit pending phase 3"
gate0:
  rules_checked: 40
  fails:
    - {rule: "A1 Median ROCE band", stated: "median 10.02% scored 3", recomputed: "10.02% sits in 10-14.9 band = 1", consequence: "Block A 10 -> 8; core 48 -> 46; grand_total 60 -> 58; classification AVERAGE unchanged; deal-breaker 1 (Block A <8) not fired at 8, zero headroom", severity: MAJOR, anchor: "01-gate0.md Block A line 35-36; prompts/01-gate-0-pipeline.md line 55"}
emoat:
  rules_checked: 22
  fails:
    - {rule: "A1 evidence tier", stated: "MM x D 1.0 = 2.0", recomputed: "scarcity claim ('few domestic labs hold USFDA') is unanchored inference; documented fact is only the acquisition -> I 0.5 = 1.0", severity: MAJOR, anchor: "07-emoat.md line 72, 174"}
    - {rule: "E1 evidence tier", stated: "MM x D 1.0 = 2.0", recomputed: "'first-mover' / 'first-of-kind' attribute is inference, not in any cited document -> I 0.5 = 1.0", severity: MAJOR, anchor: "07-emoat.md line 95, 185"}
    - {rule: "H2 evidence tier", stated: "HM x D 1.0 = 3.0", recomputed: "sole anchor is Inv. Pres. deck; no contract, value or exclusivity disclosed; prompt taxonomy puts presentation statements without signed contracts at 0.7 -> 2.1", severity: MAJOR, anchor: "07-emoat.md line 111, 192; prompts/07-emerging-moat-pipeline.md line 30-33"}
    - {rule: "Completionist recount accuracy", stated: "17 documented items across 5 categories", recomputed: "USFDA lab counted 3x (A1, B2, E1); Bhubaneswar PPP 2018 (E1) and MSMED/Utkal PPP 2018 (C1) probably one arrangement [INFERENCE]; H2 7 items are claim tier -> at most 8-10 distinct documented items", severity: MAJOR, anchor: "07-emoat.md line 149; B07 completionist_recount"}
    - {rule: "2C capex-embedded growth", stated: "Rs 63 Cr FY27 plan x 1.74x = 88%", recomputed: "rule requires capex UNDER EXECUTION x HISTORICAL FAT; FY27 plan is ANNOUNCED, funding NOT FOUND; 1.74x is single-year consolidated net-PPE turnover excluding CWIP/intangibles; B01 FAT on PPE+CWIP+intangibles is 0.72x (standalone) -> ~36% on that turnover; a single-basis value is NOT DETERMINABLE from the inputs", severity: MAJOR, anchor: "07-emoat.md line 54-60; B07 capex_embedded_growth_pct; 01-gate0.md M3 line 151-152"}
recomputed_em_score: "12.5 after tier corrections (still MODEST, 0.5 above the 12 line); 11.5 (NONE) if E1 is treated as fully duplicative of C1 and B2"
recomputed_gate0: "Block A 8, core 46, grand_total 58, classification AVERAGE (unchanged)"
valuation: {rules_checked: null, fails: [], note: "PENDING PHASE 3: B10/B11 not in scope"}
expectation_ledger: {present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: [], note: "PENDING PHASE 3"}
business_understanding_narrative: {present: null, five_questions_answered: null, prose_only: null, section6_candidates_named: null, valuation_vocab_leak: null, fails: [], note: "PENDING stage 13"}
recomputed_destination_pe: ""  # not in phase-1 scope
recomputed_decision: ""        # concur: Gate 0 AVERAGE and combined AVERAGE survive every recompute
findings:
  - {severity: MAJOR, location: "01-gate0.md Block A, A1", finding: "Median ROCE 10.02% scored 3; the 10-14.9 band scores 1. Block A 8, core 46, grand 58. Classification unchanged. Deal-breaker 1 sits exactly at its line (8, fires at <8)."}
  - {severity: MAJOR, location: "07-emoat.md A1", finding: "Moat attribute (scarcity) is inference scored at documented multiplier; 2.0 -> 1.0."}
  - {severity: MAJOR, location: "07-emoat.md E1", finding: "First-mover attribute is inference scored at documented multiplier; 2.0 -> 1.0."}
  - {severity: MAJOR, location: "07-emoat.md H2", finding: "Deck-only partner list with no contracts scored as documented; taxonomy says claim 0.7; 3.0 -> 2.1."}
  - {severity: MAJOR, location: "07-emoat.md Section 3 recount; B07 evidence_mix", finding: "Recount double and triple counts one fact (USFDA lab x3; PPP 2018 probably x2). Classification MODEST survives tier fixes at 12.5 but falls to NONE (11.5) if E1 is struck as duplicative. CLAUDE.md one-improvement-one-mechanism."}
  - {severity: MAJOR, location: "07-emoat.md 2C; B07 capex_embedded_growth_pct 88", finding: "Uses announced (not under-execution) capex and a single-year consolidated net-PPE turnover. B01's 0.72x FAT gives ~36%. Downstream should not consume 88 as a stated input."}
  - {severity: MINOR, location: "01-gate0.md E2", finding: "Window labelled '~3 years' is Mar-2024 to Mar-2026, 2 years (listing Jan-2024). Score 0 unaffected (-16.89pp)."}
  - {severity: MINOR, location: "01-gate0.md M11", finding: "Prior window is FY21-FY23 (2 years), not 3. Rule's fallback (overall trend) also scores 0 because selling % is not disclosed. Score unaffected."}
  - {severity: MINOR, location: "01-gate0.md FY24 CFO", finding: "Report line 59 calls the base row 'WC-adjusted operating profit'; data_note calls it 'before WC changes'. If pre-WC, it is not CFO. B1 holds at 5 unless true FY24 CFO < Rs 354.79 lakh. Referred to Verifier A for the source read."}
  - {severity: MINOR, location: "01-gate0.md A3", finding: "ROE formula has no use-source exception (only ROCE does); FY21-23 DRHP ROE (-105.39%, 181.61%) taken as source, FY24 computed. Mixed basis; A3 2 points at stake."}
  - {severity: MINOR, location: "01-gate0.md M1", finding: "FY26 EBITDA computed from PBT (includes other income); FY21 from DRHP line. Basis may differ; M1 5 survives unless the gap exceeds ~6pp."}
  - {severity: MINOR, location: "01-gate0.md Block D / analyst_note vs 07-emoat.md G1", finding: "B01 scores standalone D/E 0.45 and the analyst_note reads it as low leverage; B07 cites consolidated D/E 1.25. On 1.25, D3 scores 1 (core 43, still AVERAGE). Carry the basis gap forward; do not read 0.45 as group leverage."}
  - {severity: MINOR, location: "07-emoat.md line 80 (B2)", finding: "Stray non-English token in prose ('contracting典型'); 'renewable' contract claim is inference, not in the cited Reg 30 terms."}
critical_count: 0
major_count: 6
minor_count: 7
acceptance_rate: 90.3   # 56 passed / 62 checked (gate0 39/40, emoat 17/22)
```
