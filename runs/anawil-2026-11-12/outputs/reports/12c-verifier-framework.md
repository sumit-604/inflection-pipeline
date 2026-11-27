# VERIFIER C: FRAMEWORK ADHERENCE (PHASE 1 SCOPE), ANAWIL, 2026-11-12

Stage B12c. Model claude-opus-5-5 (.claude/agents/verifier-c-framework.md line 5). This is the first Verifier C run for this Phase 1 (manifest.yaml `verifier_runs: {C: 0}` before this run).

## Scope

- Phase 1 scope only. I audited B01 (Gate 0) and B07 (Emerging Moat).
- The valuation audit is deferred to phase 3. B10 and B11 do not exist yet. I read no valuation framework document.
- Rule sources: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md, and the Verifier C section of prompts/12-verifiers-pipeline.md.
- Artifacts: runs/anawil-2026-11-12/outputs/reports/01-gate0.md, outputs/blocks/B01-gate0.yaml, outputs/reports/07-emoat.md, outputs/blocks/B07-emoat.yaml.
- Verifier C rules in phase-1 scope: rule 2 (Gate 0), rule 3 (Emerging Moat), rule 8 (categories 21 and 22). Rules 6, 9 and 10 need B09, stage 13 and B09b, which are not among my inputs. Rules 4, 7 and 11 to 15 are valuation scope.
- I audit how the rules were applied. Verifier A owns whether each input number exists in its source. Every recomputed value below uses the maker's own stated inputs, unchanged. Anchors of the form "B01 l.N" point to lines of 01-gate0.md, and "B07 l.N" to lines of 07-emoat.md.

## Headline

- Findings: 0 CRITICAL, 2 MAJOR, 7 MINOR. No decision changes.
- Gate 0 revenue CAGR is 77.1%, not 177.1% (B01 l.74). C4 scores 5, not 0. Core is 66, not 61.
- M11 scores 1, not 3, under the fewer-than-6-years conservative clause (B01 l.123). Moat class is THIN, not MODERATE.
- Recomputed Gate 0: core 66, moat 5, grand total 71, classification AVERAGE. The classification holds.
- Emerging Moat: 10.8, NO MEANINGFUL EMERGING MOAT. I concur with the score and the class.
- Rules checked: 79. Passed: 70. Acceptance rate 88.6%.
- No REWORK trigger fires. Categories 21 and 22 are present and correctly scored 0 (rule 8).

## PART 1: GATE 0 COMPLIANCE (B01)

| # | Rule (prompts/01) | Result | Stated / recomputed (anchor) |
|---|---|---|---|
| G0-01 | Rule 6 opening data line | PASS | "Data available: 4 years (FY23 to FY26). Scoring adapted to 4-year history." (B01 l.3) |
| G0-02 | ROCE formula; source ROCE first; "computed" stated | PASS | Screener carries none, so ROCE is computed (B01 l.36). Re-derived: FY24 11.0982/67.6958 = 16.39%, FY25 20.8175/79.3028 = 26.25%, FY26 50.4518/188.3299 = 26.79% (B01 l.37-39) |
| G0-03 | ROE on average net worth; closing-only for earliest year, stated | PASS | FY23 closing only, stated. Re-derived 22.2 / 17.2 / 36.3 / 56.5%, median 29.2% (B01 l.49) |
| G0-04 | WC days formula; basis stated | PASS | Revenue basis stated (B01 l.60). Re-derived 68.1 / 132.3 / 109.5 days (B01 l.61-63) |
| G0-05 | FCF = CFO less capex (PPE + intangibles) | PASS, note | Capex line reads "PPE incl CWIP" (B01 l.22). Intangibles are not named. The FY26 intangible block is Rs 0.3 Cr (B07 l.86). An intangibles purchase above Rs 2.1 Cr would be needed to flip FY24 FCF of +2.1013 (B01 l.56). B2 holds |
| G0-06 | CAGR = (End ÷ Start)^(1/years) − 1 | **FAIL** | Revenue: (143.2669/25.78)^(1/3) − 1 = **77.1%**. B01 states 177.1% (B01 l.74). The 177.1 is the growth factor 1.771 printed as a rate. PAT 91.9% is correct (B01 l.75). The 177% repeats at M1 and M11 (B01 l.113, l.123) and in the block data_notes; no tier changes there. See F1 |
| G0-07 | CAGR edge rules | PASS | No zero or negative endpoint. No loss-to-profit swing. The FY23 to FY24 PAT fall is noted (B01 l.79). C4 is not N/M |
| G0-08 | NOT FOUND handling, no estimates (rules 5, 6) | PASS, see F5 | FY23 current liabilities, capex and payables are NOT FOUND, with no fill (B01 l.20, l.22, l.64). ROCE runs on 3 computable years, the rule-6 minimum. FY23 FCF sign follows from CFO −2.81 (B01 l.56). That logic is sound |
| G0-09 | A1 median ROCE | PASS | 26.25% ≥ 25 = 5 |
| G0-10 | A2 minimum ROCE | PASS | 16.39% ≥ 15 = 5 (3-year basis) |
| G0-11 | A3 median ROE | PASS | 29.2% ≥ 20 = 5 |
| G0-12 | A4 ROCE trend | PASS | 26.79% ≥ 16.39% = 5 |
| G0-13 | B1 cum CFO / cum PAT | PASS | 34.1858/58.5059 = 0.584, band 0.50-0.69 = 1. Sensitivity 28.21/58.51 = 0.482 = 0 is also correct (B01 l.55, l.66) |
| G0-14 | B2 FCF-positive years | PASS | 2 of 4 = 50% = 2 (B01 l.56) |
| G0-15 | B3 cum FCF / cum PAT | PASS | −70.00 Cr, negative = 0 (B01 l.57) |
| G0-16 | B4 WC days change | PASS | +41.4 days > 15 = 0 (B01 l.58). Against FY23 the rise is at least 83.9 days. FY23 WC is at most 25.6 days on the stated receivable 0.7 and inventory 24.9 (B01 l.64). The score is 0 either way |
| G0-17 | C1 revenue CAGR | PASS on score | 77.1% ≥ 20 = 5. The stated value is wrong (G0-06) but the band is the same |
| G0-18 | C2 PAT CAGR | PASS | 91.9% = 5 |
| G0-19 | C3 positive YoY years | PASS | 3 of 3 = 5 |
| G0-20 | C4 PAT CAGR minus revenue CAGR | **FAIL** | Stated −85.2pp = 0 (B01 l.77). Recomputed 91.9 − 77.1 = **+14.8pp**, band ≥ +3pp = **5**. Block C is 20, not 15. See F1 |
| G0-21 | D1 net debt / EBITDA | PASS | 126.6505/61.0890 = 2.07x, band 2-3x = 1 (B01 l.85) |
| G0-22 | D2 interest cover | PASS | 8.48x, band 5-9.9 = 4 (B01 l.86) |
| G0-23 | D3 debt / equity | PASS | 1.43, band 1.0-1.5 = 1 (B01 l.87) |
| G0-24 | D4 current ratio | PASS | 1.40, band 1.2-1.49 = 2 (B01 l.88) |
| G0-25 | "latest" applied to one basis across D and E | **FAIL** (MINOR) | Block D uses 31-Mar-2026 (B01 l.81, l.95). E1 and E3 use 30-Sep-2026 XBRL (B01 l.101, l.103). Recomputed on the maker's Sep-26 inputs: D1 0.38x = 4, D2 4.44x = 2, D3 0.15 = 4, D4 2.02 = 5, Block D = 15 (B01 l.91-94). See F3 |
| G0-26 | E1 promoter holding | PASS | 65.26% ≥ 60 = 5 |
| G0-27 | E2 3-year change | PASS, note | Derived and labelled as derived (B01 l.106). The window starts Mar-2024, 2.5 years before Sep-2026, not 3 years. Any pre-IPO start above 68.26% gives a decline above 3pp, so the score of 0 holds |
| G0-28 | E3 pledge | PASS | 0% = 5 |
| G0-29 | E4 contingent liabilities / net worth | PASS | 0% = 5 (B01 l.104) |
| G0-30 | M1 pricing power | PASS | −7.1pp is "else" = 0. Earliest year is the base. FY24 alternative disclosed (B01 l.113) |
| G0-31 | M2 | PASS | PEER DATA NEEDED = 0 |
| G0-32 | M3 capital efficiency | PASS | FAT 1.05x > 1, ROCE 26.79% > 12 = 1 (B01 l.115) |
| G0-33 | M4 customer stickiness | PASS | Zero decline years. Receivable days unstable, so tier 5 fails. Tier "max 1 decline year, fully recovered" carries no receivable condition = 3 (literal reading, B01 l.116) |
| G0-34 | M5 | PASS | PEER DATA NEEDED = 0 |
| G0-35 | M6 | PASS | R&D NOT FOUND = 0 |
| G0-36 | M7 | PASS | No regulated segment = 0 |
| G0-37 | M8 | PASS | No outlet network = 0 |
| G0-38 | M9 | PASS | PEER DATA NEEDED = 0, proxy stated (B01 l.121) |
| G0-39 | M10 switching costs | PASS | Receivables +98.5 days. Tier 3 needs "stable". No 2+ decline years. Else = 0 (B01 l.122) |
| G0-40 | M11 network effects, fewer-than-6-years clause | **FAIL** (MAJOR) | Stated 3 (B01 l.123). The rule says "score conservatively on the overall trend". Selling and admin share rises 1.9% to 2.0% on the stated inputs. Tier "growth >15% but selling % rising" = **1**. See F2 |
| G0-41 | M12 negative WC | PASS | 68 / 132 / 109 days, all > 45 = 0 |
| G0-42 | Moat count to class | PASS on stated scores | 2 present = MODERATE (B01 l.135). Recomputed with F2: 1 present = THIN |
| G0-43 | Block, core and grand-total arithmetic | PASS on stated scores | 20+3+15+8+15 = 61; 61+7 = 68 (B01 l.140-142) |
| G0-44 | Data confidence and one-tier downgrade | PASS | 4 years = LIMITED, downgrade one tier (B01 l.144) |
| G0-45 | Classification matrix | PASS | Core 60-79 + MODERATE = GOOD, then AVERAGE (B01 l.143-146) |
| G0-46 | Deal-breakers 1 to 9 | PASS | DB2 fires (Block B 3 < 8). DB4 conditional, correct (0.584 on restated CFO, 0.482 on filed CFO). DB1, 3, 5, 6, 7, 8, 9 do not fire: Block A 20; median ROCE 26.25%; pledge 0%; ND/EBITDA 2.07x with cover 8.48x; no revenue decline year; PAT positive FY24 to FY26; 4 years of history |
| G0-47 | Years that drive each deal-breaker named | PASS | DB2 tied to FY26 capex, FCF and the FY24 to FY26 WC build (block deal_breakers) |
| G0-48 | FLAG-GATE0 when classification ≤ AVERAGE with depressors | PASS | Present with depressors (block flags) |
| G0-49 | block_b_trend with its number | PASS | 8.8933/4.3918 = 2.03, 9.6631/12.3058 = 0.79, 18.4394/36.6283 = 0.50 (B01 l.151) |
| G0-50 | Dashboard parts | PASS | Moat bars, classification box, strongest and weakest block, decision line (B01 l.126-155) |
| G0-51 | Report ends with exactly the YAML block | **FAIL** (MINOR) | The embedded block shortens data_notes and analyst_note to pointers (B01 l.184, l.186). A line follows the block (B01 l.188). The block file is complete. See F4 |
| G0-52 | analyst_note within 200 words | PASS | About 115 words. Its content error is carried in F1 |

Gate 0: 52 rules checked, 5 FAIL, 47 PASS (90.4%). G0-06 and G0-20 share one root cause, the revenue CAGR slip. Both rows count, but they make one finding (F1).

### Recomputed Gate 0 scorecard (maker's stated inputs, FY26 Block D basis kept)

| Field | B01 stated (block) | Recomputed | Driver |
|---|---|---|---|
| Block A | 20 | 20 | concur |
| Block B | 3 | 3 | concur |
| Block C | 15 | **20** | F1 (C4 0 to 5) |
| Block D | 8 | 8 | concur on FY26 basis; 15 on Sep-26 basis (F3) |
| Block E | 15 | 15 | concur |
| Core score | 61 | **66** | F1 |
| Moat score | 7 | **5** | F2 (M11 3 to 1) |
| Grand total | 68 | **71** | F1 + F2 |
| Moats confirmed | 2 | **1** | F2 |
| Moat class | MODERATE | **THIN** | F2 |
| Matrix | Core 60-79 + MODERATE = GOOD | Core 60-79 + THIN = GOOD | concur on tier |
| Classification | AVERAGE | AVERAGE | concur |

Sensitivities re-run on the recomputed core of 66:
- Filed FY26 CFO Rs 12.467 Cr (B01 l.66): B1 falls to 0, core 65, DB4 caps at AVERAGE. Result AVERAGE.
- Sep-26 Block D of 15 (B01 l.94): core 73. Result AVERAGE.
- FY23 ROCE floor (F5): Block A floor 15, core 61. With the filed CFO it is 60, exactly on the line. Result AVERAGE.
- The recomputed core sits 6 points above the 60 line. The maker's core of 61 sat 1 point above it.

## PART 2: EMERGING MOAT COMPLIANCE (B07)

| # | Rule (prompts/07, and rule 8 of prompts/12) | Result | Stated / recomputed (anchor) |
|---|---|---|---|
| EM-01 | Six sections in one response | PASS | Sections 1 to 6 plus the register (B07 l.18-293) |
| EM-02 | Evidence taxonomy on every item | **FAIL** (MINOR) | The Meet Outcome note of 2026-10-05 is tagged [DOC] (B07 l.104, l.179). It is a management statement at an investor meet, which prompt 07 rule 2 grades as a claim. See F7 |
| EM-03 | Anchors on evidence items | PASS | One aside about Inox Wind and Suzlon is labelled "not anchored" (B07 l.129). It sits in a row that scores 0. Anchor existence belongs to Verifier A |
| EM-04 | "NO EVIDENCE FOUND" where none; no force-fit | PASS | A1-A4, B3, D1, D2, E2, F1, G2, H1-H3, I1 and I2 |
| EM-05 | Section 1: 1A, 1B, 1C with listed statuses | PASS | B07 l.20-51 |
| EM-06 | Section 2: 2A to 2D; 2C arithmetic shown | PASS | Re-derived 30.69 × 1.05 = 32.2 to 32.3 Cr; ÷ 143.27 = 22.5% (B07 l.85-87). Matches capex_embedded_growth_pct 22.5 |
| EM-07 | All 22 categories addressed | PASS | B07 l.96-129 |
| EM-08 | Summary table, 22 rows, Strong/Moderate count | PASS | 2 (F2, G1) (B07 l.148-173) |
| EM-09 | Completionist guard: under 12 active; recount line in the required form | PASS | 8 of 23 rows scored. "recount performed: 13 documented items across 7 categories" (B07 l.175) |
| EM-10 | Recount itemisation accurate | **FAIL** (MINOR) | See F8 |
| EM-11 | I1 (Category 21): both legs, leg (b) needs one documented source for top band | PASS | Both legs fail; 0 (B07 l.128) |
| EM-12 | I2 (Category 22): specific named sacrifice or 0 | PASS | Honest answer is "nothing"; 0 (B07 l.129) |
| EM-13 | Section 4: 4A, 4B, 4C | PASS | B07 l.177-188 |
| EM-14 | Likelihood x impact mapping | PASS | B1 MM 2, B2 LM 1, C1 MM 2, C2 LM 1, E1 ML 1, F2 MM 2, G1 HM 3, R1 LL 1 (B07 l.200-218) |
| EM-15 | Evidence multipliers | PASS | 1.4, 1.0, 1.0, 1.0, 0.7, 2.0, 3.0, 0.7 |
| EM-16 | Score tier matches evidence tier | PASS | No claim-only row scores as documented. B1 scores at CLAIM although it holds documented items. C1 scores at INFER. Both sit at or below their best tier |
| EM-17 | Adjusted total | PASS | 1.4+1.0+1.0+1.0+0.7+2.0+3.0+0.7 = 10.8 (B07 l.219) |
| EM-18 | Classification band | PASS | 10.8 < 12 = NO MEANINGFUL EMERGING MOAT, "NONE" |
| EM-19 | I1/I2 contribution stated separately | PASS | 0.0 (B07 l.221) |
| EM-20 | Section 5 has all 23 rows | PASS | B07 l.196-218 |
| EM-21 | Optionality register covers 0-scored and claim/inference-only items | **FAIL** (MINOR) | R1 rests on claim-only evidence and has no register row. See F6 |
| EM-22 | F2 cross-references the promise-delivery record, or a disclosed substitute | PASS | No concall exists. The dated-statement test is disclosed, and guidance delivery is NOT TESTABLE (B07 l.131-144) |
| EM-23 | 6A and 6B present | PASS | B07 l.238-255 |
| EM-24 | 6C uses the injected Gate 0 block correctly | **FAIL** (MINOR) | "61 of 140 core points" (B07 l.261). Core maximum is 100 (B01 l.140). See F9 |
| EM-25 | 6D combined class; HIGH POTENTIAL and TURNAROUND reasoned | PASS | Prompt 07 names the matrix labels but not the cell rules, so I cannot re-derive the cell. AVERAGE is consistent with Gate 0 AVERAGE and EM NONE. Both rows are reasoned (B07 l.269) |
| EM-26 | 6E card: map per family, 12-month catalysts, biggest risk | PASS | B07 l.276-291 |
| EM-27 | YAML: fields, enumerations, active_categories only Strong/Moderate, analyst_note within 200 words | PASS | Report block and block file match. analyst_note is about 140 words |

Emerging Moat: 27 rules checked, 4 FAIL, 23 PASS (85.2%). Recomputed EM score 10.8, class NONE. I concur.

G1 is the largest row at 3.0 of 10.8 (B07 l.211). Its tier (DOC) is correct. Its likelihood grade (H) is a judgment I do not overturn. It rests on IPO-funded deleveraging, with cash of Rs 0.2 Cr and bank limits 84% used (B07 l.122). F3 names the double-credit coupling between G1 and Gate 0 Block D.

## FINDINGS

| ID | Sev | Rule | Location | Stated | Recomputed | Effect |
|---|---|---|---|---|---|---|
| F1 | MAJOR | G0-06, G0-20 | B01 l.74, l.77; block blocks.C, core_score, grand_total, data_notes, analyst_note | Revenue CAGR 177.1%; C4 −85.2pp = 0; Block C 15; core 61; grand total 68 | (143.2669/25.78)^(1/3) − 1 = 77.1%; C4 +14.8pp = 5; Block C 20; core 66; grand total 73 (71 with F2) | Classification stays AVERAGE. The block analyst_note says the FY23 ramp-year base "wrecks C4, M1 and B4". That is wrong on two of three. For C4, the FY23 base gives PAT growth of 7.07x (36.6283/5.18) against revenue growth of 5.56x (143.2669/25.78), so operating leverage is positive. For B4, the test runs FY24 to FY26 (B01 l.58) and FY23 is not used. Only M1 is driven by FY23 |
| F2 | MAJOR | G0-40 | B01 l.123, l.135; block moat_score, moats_confirmed, moat_class, data_notes | M11 = 3; moats 2; MODERATE; moat score 7 | M11 = 1; moats 1; THIN; moat score 5 | Classification stays AVERAGE (Core 60-79 + THIN = GOOD, one tier down = AVERAGE). There are two readings. Reading the 0.1pp rise as "stable", by analogy to M1's ±2pp, gives 3. The clause for fewer than 6 years says "score conservatively", which gives 1. The clause governs, because the two-window test cannot run. The maker's own words, "a growth artefact, not a network effect" (B01 l.123), match a score of 1. B07 6C carries the stale MODERATE and 2 moats |
| F3 | MINOR | G0-25 | B01 l.81, l.95, l.101, l.103 | Block D 8 on 31-Mar-2026; E1 and E3 on 30-Sep-2026 | Block D 15 on the 30-Sep-2026 balance sheet (D1 4, D2 2, D3 4, D4 5); core 73 with F1 | Classification stays AVERAGE. The maker disclosed the basis and ran the sensitivity. Coupling: B07 G1 (3.0 points) says there is no double credit because Gate 0 did not score the Sep-26 balance sheet (B07 l.122). If "latest" is ruled to mean Sep-26, Block D and G1 credit the same IPO deleveraging. Stage 11 must then take it through one mechanism only. Operator ruling requested (note N2) |
| F4 | MINOR | G0-51 | B01 l.157-188; B01 l.106 | Embedded YAML differs from the block file; a line follows the block; truncated phrase "pre-IPO placement (1.38 crore... see note)" with no note | B01-gate0.yaml is the copy of record | Presentational only |
| F5 | MINOR (observation) | G0-08 | B01 l.40, l.148 | "No sensitivity moves it off AVERAGE" | FY23 ROCE is NOT FOUND. On the stated FY23 EBIT of 9.61 Cr (6.28 + 3.33, B01 l.12-13) and total assets of 80.90 Cr (B01 l.19), FY23 ROCE is at least 11.88% for any current-liabilities value. In a 4-year window, A1 can fall to 4, A2 to 3 or 1, or A4 to 3, 1 or 0. Block A floor is 15 | On the maker's core of 61, the floor is 56. That gives matrix AVERAGE, and the one-tier downgrade would then give AVOID, if the downgrade can run below AVERAGE (note N5). On the recomputed core of 66, the floor is 61, or 60 with the filed CFO, so AVERAGE holds. The maker's robustness claim is true only after F1. The observation that closes the gap is FY23 current liabilities (screener Balance Sheet sheet, absent per B01 input_gaps) |
| F6 | MINOR | EM-21 | B07 l.188, l.218, l.225-234 | R1 = 0.7 on claim-only evidence; no register row; 4C says "NOT an active or emerging moat ... Score kept at the floor" | Add an R1 register row. The 0.7 itself is consistent with the matrix (LL = 1 is the floor for any evidence) | EM class stays NONE. The analyst_note says E1 moving from 0.7 to 2.0 "reaches 12.1" (MODEST). That sum includes R1's 0.7. Without it, the same move reaches 11.4. The "band is close" reading depends on a sector-wide row graded as a claim |
| F7 | MINOR | EM-02 | B07 l.104, l.179 | Meet Outcome 2026-10-05 tagged [DOC] | Management statement at an investor meet = claim (prompt 07 rule 2) | B2 keeps its documented tier through Prospectus p.119-120. That is the B2 item the recount counts (B07 l.175). No score change |
| F8 | MINOR | EM-10 | B07 l.175; block completionist_recount | "Management claims 6 across 5 categories (A1, B1, E1, R1, C1 ..., F2 ...)"; B1 documented item = "CWIP rise" | Six categories are named, not five. The CWIP project is unnamed (B07 l.63, l.67), so its link to B1 is inference. The B1 documented item that can be attributed is the Rs 0.89 Cr GCP machinery (CARE p.8, cited at B07 l.24, l.103) | After the swap the recount stays at 13 items across 7 categories. No score change |
| F9 | MINOR | EM-24 | B07 l.261-263; block combined_reasoning | "61 of 140 core points"; core 61, grand total 68, MODERATE | Core maximum is 100 (B01 l.140). With F1 and F2: core 66, moat 5, grand total 71, 1 moat, THIN | Combined assessment stays AVERAGE |

Counts: CRITICAL 0, MAJOR 2, MINOR 7.

Severity basis: rule 5 of the Verifier C section. A misapplication that flips the classification or the decision would be CRITICAL. A wrong score or class where the decision survives is MAJOR. A presentational gap is MINOR. No finding flips the Gate 0 classification, the EM class, or the combined assessment.

## PART 3: VALUATION: PENDING PHASE 3

B10 and B11 are not yet produced. The valuation audit is not run: growth symmetry, pillar mechanics, method plurality, v3.8 exit construction, Amendment 19 FV path, expectation ledger and skill-to-source fidelity. The valuation, expectation_ledger and business_understanding_narrative fields in the block are placeholders. Their nulls mean "not assessed", not "failed".

## NOTES FOR THE OPERATOR (not scored)

- N1. Template defect. prompts/12-verifiers-pipeline.md line 379 holds the text `(same line, comment "# rule 9; any fail = REWORK stage 13")` in place of a field. October audit item VER-08 meant to change only the comment on the `business_understanding_narrative` line (audits/PROMPT_AUDIT_2026-10.md l.1960-1965). The patch replaced the whole line. I emitted the intended field. The fix needs a prompt PR on a framework branch.
- N2. Gate 0 "latest" (D1 to D4, E4) has no definition. It can mean the latest audited year-end or the latest filed balance sheet. Every post-IPO name hits this. A ruling is needed (F3).
- N3. Gate 0 rule 5 ("mark it NOT FOUND and score it 0") and rule 6 ("use whatever history is available: minimum 3 years") pull apart when one year of a multi-year metric is missing. Under a strict rule-5 reading, FY23 ROCE scores as 0: A1 4, A2 0, A4 5, Block A 14. The recomputed core is then 60, or 59 with the filed CFO, which falls in Core 40-59. I applied rule 6, as the maker did.
- N4. A4 has no band for a decline between 0 and 1pp.
- N5. The LIMITED one-tier downgrade does not say whether it can take AVERAGE to AVOID.
- N6. F1 and F2 change B01 block fields that stage 7 and later stages read: blocks.C, core_score, moat_score, grand_total, moats_confirmed, moat_class. This verifier fires no REWORK trigger (88.6% on a denominator of 79). The correction belongs to the one permitted remediation cycle, or goes to Halt 1 as an open item (operator ruling 2026-10-11). I did not edit any upstream artifact.

## BLOCK

```yaml
stage: B12c
company: "ANAWIL"
run_date: "2026-11-12"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete
scope: "phase-1: Gate 0 (B01) and Emerging Moat (B07) only; valuation audit PENDING PHASE 3; no valuation framework doc read"
gate0: {rules_checked: 52, fails: ["G0-06 CAGR formula: revenue CAGR stated 177.1%, recomputed 77.1% from 25.78 and 143.2669 (B01 l.74)", "G0-20 C4: stated 0 on -85.2pp, recomputed 5 on +14.8pp; Block C 15 to 20, core 61 to 66", "G0-25 'latest' read as 31-Mar-2026 for Block D and 30-Sep-2026 for E1/E3; Block D 15 on the Sep-26 basis", "G0-40 M11: stated 3, recomputed 1 under the fewer-than-6-years conservative clause; moats 2 to 1, MODERATE to THIN", "G0-51 report-embedded YAML differs from the block file and a line follows it"]}
emoat: {rules_checked: 27, fails: ["EM-02 Meet Outcome 2026-10-05 tagged DOC; it is a management claim; no score change", "EM-10 recount text names 6 claim categories as 5; B1 documented item is the unattributed CWIP rise; count unchanged", "EM-21 R1 scored 0.7 on claim-only evidence but has no optionality register row", "EM-24 6C states core as 61 of 140; core maximum is 100; carries uncorrected Gate 0 values"]}
valuation: {rules_checked: 0, fails: []}  # PENDING PHASE 3: B10/B11 not yet produced
expectation_ledger: {present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: []}  # rules 13-14; any fail = REWORK stage 11; PENDING PHASE 3, null = not assessed
business_understanding_narrative: {present: null, five_questions_answered: null, prose_only: null, section6_candidates_named: null, valuation_vocab_leak: null, fails: []}  # rule 9; any fail = REWORK stage 13; not in phase-1 scope, null = not assessed
recomputed_destination_pe: ""  # PENDING PHASE 3
recomputed_decision: ""        # concur: Gate 0 AVERAGE, EM NONE, combined AVERAGE
recomputed_gate0: {blocks: {A: 20, B: 3, C: 20, D: 8, E: 15}, core_score: 66, moat_score: 5, grand_total: 71, moats_confirmed: 1, moat_class: "THIN", classification: "AVERAGE"}  # F1 + F2 on maker's stated inputs; FY26 Block D basis kept (15 on Sep-26 basis, core 73)
recomputed_emoat: {em_score: 10.8, em_classification: "NONE"}  # concur
findings:
  - {id: F1, severity: MAJOR, framework: gate0, rule: "G0-06, G0-20", location: "01-gate0.md l.74, l.77; B01 blocks.C, core_score, grand_total, data_notes, analyst_note", stated: "revenue CAGR 177.1%; C4 -85.2pp = 0; Block C 15; core 61; grand total 68", recomputed: "revenue CAGR 77.1%; C4 +14.8pp = 5; Block C 20; core 66; grand total 73 (71 with F2)", effect: "classification unchanged AVERAGE; analyst_note 'ramp-year base wrecks C4, M1 and B4' is wrong on C4 and B4"}
  - {id: F2, severity: MAJOR, framework: gate0, rule: "G0-40", location: "01-gate0.md l.123, l.135; B01 moat_score, moats_confirmed, moat_class", stated: "M11 3; moats 2; MODERATE; moat score 7", recomputed: "M11 1 (selling share 1.9% to 2.0% rising; fewer-than-6-years clause says score conservatively); moats 1; THIN; moat score 5", effect: "classification unchanged AVERAGE; B07 6C carries the stale MODERATE"}
  - {id: F3, severity: MINOR, framework: gate0, rule: "G0-25", location: "01-gate0.md l.81, l.95, l.101, l.103", stated: "Block D 8 on 31-Mar-2026; E1/E3 on 30-Sep-2026", recomputed: "Block D 15 on 30-Sep-2026 (D1 4, D2 2, D3 4, D4 5); core 73 with F1", effect: "classification unchanged; if latest = Sep-26, Block D and B07 G1 credit the same IPO deleveraging; operator ruling requested"}
  - {id: F4, severity: MINOR, framework: gate0, rule: "G0-51", location: "01-gate0.md l.106, l.157-188", stated: "embedded YAML abbreviated; text after block; truncated '1.38 crore... see note'", recomputed: "B01-gate0.yaml is the copy of record", effect: "presentational"}
  - {id: F5, severity: MINOR, framework: gate0, rule: "G0-08 (observation)", location: "01-gate0.md l.40, l.148", stated: "No sensitivity moves it off AVERAGE", recomputed: "FY23 ROCE NOT FOUND; floor 11.88% from EBIT 9.61 / TA 80.90; Block A floor 15; recomputed core floor 61 (60 with filed CFO)", effect: "AVERAGE holds only after F1; on the maker's core 61 the floor is 56 (matrix AVERAGE, then AVOID if the downgrade runs below AVERAGE)"}
  - {id: F6, severity: MINOR, framework: emoat, rule: "EM-21", location: "07-emoat.md l.188, l.218, l.225-234", stated: "R1 0.7 on claim-only evidence, no register row", recomputed: "add R1 register row; 0.7 is matrix-consistent", effect: "EM NONE unchanged; analyst_note path E1 to 2.0 reaches 11.4, not 12.1, without R1"}
  - {id: F7, severity: MINOR, framework: emoat, rule: "EM-02", location: "07-emoat.md l.104, l.179", stated: "Meet Outcome 2026-10-05 tagged DOC", recomputed: "management claim", effect: "no score change; B2 DOC tier rests on Prospectus p.119-120"}
  - {id: F8, severity: MINOR, framework: emoat, rule: "EM-10", location: "07-emoat.md l.175; B07 completionist_recount", stated: "claims 6 across 5 categories (six named); B1 documented item = CWIP rise", recomputed: "6 categories; attributable B1 documented item = Rs 0.89 Cr GCP machinery (CARE p.8)", effect: "recount stays 13 items across 7 categories; no score change"}
  - {id: F9, severity: MINOR, framework: emoat, rule: "EM-24", location: "07-emoat.md l.261-263; B07 combined_reasoning", stated: "61 of 140 core points; grand total 68; MODERATE", recomputed: "core maximum 100; with F1 and F2 core 66, grand total 71, THIN", effect: "combined AVERAGE unchanged"}
critical_count: 0
major_count: 2
minor_count: 7
acceptance_rate: 88.6             # 70 of 79 rules passed (gate0 47/52, emoat 23/27)
```
