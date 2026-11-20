# VERIFIER C: FRAMEWORK ADHERENCE (B12c), VRLLOG, run 2026-11-12

Scope: PHASE 1 only (the Gate 0 and Emerging Moat half). Model: claude-opus-5-5 (.claude/agents/verifier-c-framework.md L5). This is the first Verifier C run in this Phase 1 (manifest.yaml L17: verifier_runs C: 0).

Inputs read:
- Rule sources: prompts/01-gate-0-pipeline.md and prompts/07-emerging-moat-pipeline.md.
- Artifacts: outputs/reports/01-gate0.md, outputs/blocks/B01-gate0.yaml, outputs/reports/07-emoat.md, outputs/blocks/B07-emoat.yaml.

Not read (outside phase-1 scope): the Master Project Prompt, the Section 1B layers, FTTCP, any corpus document, and every other verifier's output.

Method. I re-derived every Gate 0 metric score from the inputs the report states, against the thresholds in 01-gate-0-pipeline.md. I re-derived every Emerging Moat row from its stated likelihood, impact and evidence tier, against 07-emerging-moat-pipeline.md. I do not test whether a number exists at its source anchor. Verifier A owns that question.

Anchor key: "G0 Lnn" = line nn of 01-gate0.md. "EM Lnn" = line nn of 07-emoat.md. "R01 Lnn" = line nn of prompts/01-gate-0-pipeline.md. "R07 Lnn" = line nn of prompts/07-emerging-moat-pipeline.md.

## SUMMARY

- I checked 75 rules: 48 Gate 0 and 27 Emerging Moat. 64 pass and 11 fail. The acceptance rate is 85.3% (64/75). That is above 60%, so it does not trigger REWORK.
- Findings: 0 CRITICAL, 2 MAJOR, 9 MINOR. Both MAJOR findings are in Gate 0. All six Emerging Moat findings are MINOR.
- The arithmetic holds. Every block score re-derives from the stated inputs: core 63, moat 11, grand total 74, EM total 12.8, EM band MODEST. One rounding slip (FY26 ROCE is 18.05%, shown as 18.1%) moves no band.
- The Gate 0 classification depends on how a gap is read. The stage treated the same kind of gap (years missing from a history window) in three ways: a substitute formula (FCF, ROCE), a partial window (E2, M12), and NOT FOUND scored 0 (B4).
- Under one consistent reading the core is 64 (GOOD). Under the other the core is 51 (AVERAGE). E2 scores 0 under both readings, because its 3-year start point (30 Sep 2023) is NOT FOUND. That correction alone puts the delivered core at 60, the floor of the GOOD band.
- One document separates the two readings: the FY17 to FY24 "purchase of PPE and intangibles" lines from the earlier cash-flow statements. With them, B2 and B3 run on the fixed formula and the reading question disappears.
- Emerging Moat holds at MODEST (12.8) under every recompute a rule requires. The lowest is 12.4 (B3 at the inference multiplier). The band floor is 12.

## TABLE 1. GATE 0 (B01) COMPLIANCE, RULE BY RULE

| ID | Rule (source) | Delivered | Re-derived | Result |
|---|---|---|---|---|
| G0-01 | Opening data line (R01 L23-25) | "Data available: 10 years (FY2017 to FY2026). Scoring adapted to 10-year history." (G0 L3) | same | PASS |
| G0-02 | Anchor after every extracted number (R01 L15-18) | screener-data, AR p., results p., presentation p. anchors present | | PASS |
| G0-03 | Show every number extracted (R01 L14) | yearly revenue FY18-FY25, FY23 revenue, yearly net worth not shown | C3, M4, M10, M11 and A3 re-derive only from stated intermediates | FAIL MINOR |
| G0-04 | ROCE = EBIT / (TA - CL), or the source's own figure; state "computed" (R01 L29-31) | proxy (PBT + Int) / (Equity + Reserves + Borrowings), stated "COMPUTED" (G0 L38) | strict FY26 18.9%, FY25 15.8% (G0 L53); bands hold; FY26 proxy 18.05%, not 18.1% | FAIL MINOR |
| G0-05 | ROE on average net worth; closing for earliest year, stated (R01 L32-33) | FY17 closing, stated (G0 L57) | | PASS |
| G0-06 | WC days formula; basis stated (R01 L34-38) | revenue basis stated (G0 L70) | FY26 9.7 + 5.0 - 3.0 = 11.7 days | PASS |
| G0-07 | FCF = CFO - capex (purchase of PPE + intangibles; exclude acquisitions), fixed (R01 L27, L39-40) | FY17-FY24 capex replaced by -CFI (G0 L63) | see Finding G0-07 | FAIL MAJOR |
| G0-08 | CAGR = (End / Start)^(1/years) - 1 (R01 L41) | 9-year windows | C1 6.66%, C2 14.42% | PASS |
| G0-09 | CAGR edge rules: negative endpoint, loss-to-profit swing, C4 (R01 L43-50) | endpoints positive, no swing (G0 L83) | no N/M case arises | PASS |
| G0-10 | A1 median ROCE (R01 L55) | 18.0% -> 3 | (17.90 + 18.05) / 2 = 17.98% -> 3 | PASS |
| G0-11 | A2 minimum ROCE (R01 L56) | 9.9% FY21 -> 1 | 101.14 / 1,018.90 = 9.93% -> 1 | PASS |
| G0-12 | A3 median ROE (R01 L57) | 15.6% -> 4 | (14.8 + 16.3) / 2 = 15.55% -> 4 | PASS |
| G0-13 | A4 ROCE latest vs earliest (R01 L58-59) | 18.1 vs 17.9 -> 5 | 18.05 vs 17.90 -> 5 | PASS |
| G0-14 | B1 cumulative CFO / PAT (R01 L62-63) | 2.49 -> 5 | 3,446.73 / 1,382.04 = 2.49 -> 5 | PASS |
| G0-15 | B2 FCF-positive years (R01 L64) | 9 of 10 -> 4 | 9 of 10 on the stated FCF -> 4 | PASS (input method fails at G0-07) |
| G0-16 | B3 cumulative FCF / PAT (R01 L65-66) | 1.21 -> 5 | 1,668.87 / 1,382.04 = 1.21 -> 5 | PASS (input method fails at G0-07) |
| G0-17 | B4 WC days change; NOT FOUND scores 0 (R01 L67-68, L20-21) | 0, FY17 payables NOT FOUND (G0 L70) | 0 | PASS |
| G0-18 | C1 revenue CAGR (R01 L71) | 6.7% -> 1 | (3,221.11 / 1,803.09)^(1/9) - 1 = 6.66% -> 1 | PASS |
| G0-19 | C2 PAT CAGR (R01 L72) | 14.4% -> 3 | (236.83 / 70.47)^(1/9) - 1 = 14.42% -> 3 | PASS |
| G0-20 | C3 positive YoY years (R01 L73) | 8 of 9 -> 3 | 88.9% -> 3 | PASS |
| G0-21 | C4 PAT CAGR minus revenue CAGR (R01 L74) | +7.8pp -> 5 | 14.42 - 6.66 = +7.76pp -> 5 | PASS |
| G0-22 | D1 net debt / EBITDA (R01 L77-79) | 1.73x -> 3 | 1,138.51 / 658.42 = 1.73x -> 3 | PASS |
| G0-23 | D2 EBIT / interest (R01 L80-82) | 4.29x -> 2 | 414.50 / 96.62 = 4.29x -> 2 | PASS |
| G0-24 | D3 debt / equity (R01 L83-84) | 1.01 -> 1 | 1,154.13 / 1,142.44 = 1.01 -> 1 | PASS |
| G0-25 | D4 current ratio (R01 L85-86) | 0.49 -> 0 | 20,390 / 41,392 = 0.49 -> 0 | PASS |
| G0-26 | E1 promoter holding (R01 L89-90) | 60.24% -> 5 | -> 5 | PASS |
| G0-27 | E2 promoter change over 3 years (R01 L91-92; NOT FOUND rule L20-21) | 0.00pp, 31 Mar 2024 to 30 Sep 2026 -> 3 (G0 L98) | 3-year start point (30 Sep 2023) NOT FOUND -> 0 | FAIL MAJOR |
| G0-28 | E3 pledge (R01 L93) | 0% -> 5 | -> 5 | PASS |
| G0-29 | E4 contingent liabilities / net worth (R01 L94-95) | 4.6% -> 5 | 53.03 / 1,142.44 = 4.64% -> 5 | PASS |
| G0-30 | M1 pricing power (R01 L102-104) | 0 | margin +8.26pp, but revenue CAGR 6.66% < 10% -> 0 | PASS |
| G0-31 | M2, PEER DATA NEEDED scores 0 (R01 L99-100, L105-106) | 0 | 0 | PASS |
| G0-32 | M3 capital efficiency (R01 L107-108) | 1 | FAT 1.40x, ROCE 18.05% -> 1 | PASS |
| G0-33 | M4 customer stickiness (R01 L109-111) | 3 | one decline year (FY21), recovered (FY22 2,163.56 > FY20 2,118.54) -> 3 | PASS |
| G0-34 | M5 scale and dominance (R01 L112-113) | 0 PEER DATA NEEDED | 0 | PASS |
| G0-35 | M6 technology / R&D (R01 L114-116) | 0 | no R&D line -> 0 | PASS |
| G0-36 | M7 regulatory / licence (R01 L117-119) | 0 | no licence evidence -> 0 | PASS |
| G0-37 | M8 distribution (R01 L120-122) | 1 | reach quantified and growing; revenue per outlet NOT FOUND; CAGR < 15% -> 1 | PASS |
| G0-38 | M9 brand (R01 L123-125) | 0 PEER DATA NEEDED | 0 | PASS |
| G0-39 | M10 switching costs (R01 L126-128) | 3 | growth in all but 1 year, receivable days fell -> 3 | PASS |
| G0-40 | M11 network effects, two windows (R01 L129-133) | 0 | 6.7% vs 7.7%, not higher; CAGR < 15% -> 0 | PASS |
| G0-41 | M12 "0-15 days consistently" (R01 L134-135; NOT FOUND rule L20-21) | 3 on FY25 and FY26 only (G0 L124) | 8 of 10 years NOT FOUND -> 0 under reading (b) | FAIL MINOR |
| G0-42 | Moat present at >= 3; moat class (R01 L98-99, L137-138) | 3 present, MODERATE | 3 present (M4, M10, M12) -> MODERATE | PASS |
| G0-43 | Block, core and grand-total sums | 13 + 14 + 12 + 6 + 18 = 63; 63 + 11 = 74 | same | PASS |
| G0-44 | Data confidence and history downgrade (R01 L142-144) | full, no downgrade | 10 years -> full | PASS |
| G0-45 | Classification matrix (R01 L146-149) | core 63 + MODERATE -> GOOD | GOOD on the delivered scores | PASS |
| G0-46 | Deal-breakers 1-9; state the driving years (R01 L151-159) | none fire (G0 L133) | none fire on the delivered scores | PASS |
| G0-47 | FLAG-GATE0 when classification <= AVERAGE (R01 L175-177) | flags: [] | correct for GOOD | PASS |
| G0-48 | YAML schema, data_notes, block_b_trend, analyst_note <= 200 words (R01 L168-198) | every field present; analyst_note about 75 words | | PASS |

Gate 0: 48 checked, 43 pass, 5 fail (2 MAJOR, 3 MINOR).

### Gate 0 findings

**G0-07 (MAJOR). FCF formula substitution for FY17 to FY24.**
- Rule: "FCF = CFO − Capex (capex = purchase of PPE + intangibles from cash flow statement; exclude acquisitions)", under "FORMULA DEFINITIONS (fixed, do not substitute alternatives)" (R01 L27, L39-40). Rule 5: "If a data point is not available, mark it "NOT FOUND" and score it 0" (R01 L20-21).
- Delivered: FCF for FY17 to FY24 = CFO + CFI, labelled "Stated proxy; not an estimate" (G0 L63). Actual capex is used for FY25 (448.79 Cr) and FY26 (298.62 Cr) only (G0 L63, L66).
- Why it fails: the rule names the capex line and carves out acquisitions. CFI is the broader line the rule narrows away from. It nets disposal proceeds, investment purchases and acquisitions. The stated inputs do not show which way the proxy error runs.
- Recompute under the two readings the rule text admits:
  - (a) Score on the fixed-formula years that exist. The stage gave M12 this treatment. FY25 FCF 106.00 Cr and FY26 FCF 355.75 Cr are both positive, so B2 = 5. B3 = (106.00 + 355.75) / (182.92 + 236.83) = 461.75 / 419.75 = 1.10, so B3 = 5 (G0 L65-66).
  - (b) Treat the metric over the declared 10-year history (G0 L3) as NOT FOUND. The stage gave B4 this treatment. B2 = 0 and B3 = 0. Block B = 5. Deal-breaker 2 fires (Block B < 8, max GOOD). It does not bind, because the core is already in the AVERAGE band.
- Effect: Block B is 14 as delivered, 18 under (a) (B4 also scores 3 under (a)), and 5 under (b). The sensitivity table below gives the classification.
- Separating observation: the FY17 to FY24 "purchase of PPE and intangibles" from the earlier annual reports' cash-flow statements. These are outside this corpus (G0 L144).
- Severity: MAJOR. GOOD survives under the delivered proxy and under (a). Under (b) the classification is AVERAGE. The run continues under all three, because Gate 0 has no halt. The label and FLAG-GATE0 differ.

**G0-27 (MAJOR). E2 scored on a 2.5-year window.**
- Rule: "E2 Promoter holding change over 3 years" (R01 L91-92). Rule 5 scores a missing data point at 0 (R01 L20-21).
- Delivered: 3, on a flat 60.24% from 31 Mar 2024 to 30 Sep 2026. The report says: "The 3-year window starts Sep 2023; quarters before Mar 2024 are NOT FOUND in this corpus" (G0 L98).
- Why it fails: the window is fixed at 3 years, and its start point (30 Sep 2023) is NOT FOUND. The stage scored the same kind of gap at 0 in B4 (G0 L70). The report also records a 5.4% promoter stake sale whose date is NOT FOUND in the corpus (G0 L26). The holding is flat from 31 Mar 2024, so any such sale came before that date. If the sale came after 30 Sep 2023, the evidenced band is "decreased >3% = 0" (R01 L92). The partial window cannot show which case applies.
- Recompute: E2 = 0. Block E = 15. With only this change, the core is 60, the floor of the 60-79 band. GOOD holds by 0 points.
- Separating observation: the 30 Sep 2023 shareholding pattern, or the dated disclosure of the 5.4% sale.
- Severity: MAJOR. The score is wrong as written. The label survives, but only at the band edge.

**G0-04 (MINOR). ROCE denominator proxy, plus one rounding slip.**
- Rule: "ROCE = EBIT ÷ (Total Assets − Current Liabilities), per year. If the data source provides its own ROCE (screener.in does), use the source's figure and anchor it; compute only when absent, and state "computed"" (R01 L29-31).
- Delivered: computed on (Equity + Reserves + Borrowings) in all 10 years, and stated (G0 L38). The strict formula is shown for FY26 (18.9%) and FY25 (15.8%), with "Bands unchanged" (G0 L53).
- Why MINOR and not MAJOR: the rule accepts a source-supplied ROCE and does not fix that source's denominator. The stage disclosed the proxy and tested it on both years where the strict formula can be computed. A1 and A2 hold their bands on those years.
- Rounding: FY26 414.50 / 2,296.57 = 18.05%, shown as 18.1% (G0 L51). The A1 median becomes 17.98% (band 3). A4 becomes 18.05 vs 17.90 (band 5). No score changes.
- Open: A4 under the strict formula needs FY17 current liabilities, which are NOT FOUND (G0 L38).

**G0-41 (MINOR). M12 "consistently" scored on 2 of 10 years.**
- Rule: "0-15 days consistently = 3" (R01 L134-135), plus rule 5.
- Delivered: 3, with the note "only those two years are evidenced" (G0 L124; B01 data_notes).
- Recompute under reading (b): M12 = 0. Moat score 8. Moats present 2 (M4, M10). Class MODERATE, unchanged. Grand total 71 on the delivered core. Under reading (a), the 3 stands.
- Severity: MINOR. The class does not change.

**G0-03 (MINOR). Not every extracted number is shown.**
- Rule: "Show every number you extract and the score for each metric" (R01 L14).
- Missing: yearly revenue FY18 to FY25 (C3 count, M4, M10), FY23 revenue (both M11 windows), yearly net worth (A3), and yearly receivable days between FY17 and FY26 (M4, M10). I re-derived these scores from the intermediate values the report states. I could not re-derive them from the inputs.
- Severity: MINOR. No score is shown to be wrong.

### Gate 0 classification sensitivity

Every component comes from the G0 lines cited in the findings above.

| Reading | A | B | C | D | E | Core | Moat (class) | Grand total | Classification |
|---|---|---|---|---|---|---|---|---|---|
| Delivered (proxy FCF, partial E2, M12 on 2 years, B4 at 0) | 13 | 14 | 12 | 6 | 18 | 63 | 11 (MODERATE) | 74 | GOOD |
| Delivered, E2 corrected only | 13 | 14 | 12 | 6 | 15 | 60 | 11 (MODERATE) | 71 | GOOD (band floor) |
| (a) fixed-formula years that exist; E2 on its fixed window | 13 | 18 | 12 | 6 | 15 | 64 | 11 (MODERATE) | 75 | GOOD |
| (b) NOT FOUND scores 0 throughout | 13 | 5 | 12 | 6 | 15 | 51 | 8 (MODERATE) | 59 | AVERAGE; deal-breaker 2 fires; FLAG-GATE0 due |

- Under (a): B2 5, B3 5, B4 3 (FY25 12.1 to FY26 11.7 days, -0.4, inside +/-5; G0 L70), M12 3.
- Under (b): B2 0, B3 0, B4 0, M12 0.
- Both readings keep Block A at 13, because I accept the ROCE proxy (G0-04). If the ROCE proxy were also refused, A1, A2 and A4 would rest on two strict-formula years. I do not apply that reading.

The two readings:
- (a) A metric runs on the fixed-formula years that exist.
- (b) A metric over the declared history is NOT FOUND when most of its years are missing.

The rule text supports both. Reading (b) is the more literal reading of rule 5, given the declared "10-year history" (G0 L3). Reading (a) matches rule 6 ("Use whatever history is available", R01 L23) and the stage's own M12 treatment. The FY17 to FY24 capex lines would settle the question, because they let B2 and B3 run on the fixed formula. An operator ruling on how to treat missing years would settle it for later runs as well. The underlying defect is that the stage treated one kind of gap in three different ways.

## TABLE 2. EMERGING MOAT (B07) COMPLIANCE, RULE BY RULE

| ID | Rule (source) | Delivered | Re-derived | Result |
|---|---|---|---|---|
| EM-01 | All six sections plus the register, one response (R07 L28) | Sections 1-6 and the register present | | PASS |
| EM-02 | Not conflated with FTTCP (R07 L3-6) | stated (EM L3) | | PASS |
| EM-03 | Evidence tag on every item (R07 L29-34) | tags present | | PASS |
| EM-04 | Source anchor on every evidence item (R07 L35-36) | "May call p.?" (EM L189); "FY25 AR" with no page (EM L98) | 2 anchors incomplete | FAIL MINOR |
| EM-05 | NO EVIDENCE FOUND; never force-fit (R07 L39-40) | 13 categories marked NO EVIDENCE | | PASS |
| EM-06 | Section 1: 1A statuses, 1B, 1C table (R07 L48-55) | present; two labels outside the status list ("ANNOUNCED then silent", "LAUNCHED (old)") | | PASS |
| EM-07 | Section 2A, 2B, 2D (R07 L57-63) | present; 2B utilisation NOT FOUND, stated | | PASS |
| EM-08 | 2C: capex under execution x historical FAT, arithmetic shown (R07 L59-62) | H2 FY27 guided capex 150-160 Cr (a plan) x 1.887 -> 9.1% (EM L67) | commitments 79.84 Cr x 1.887 = 150.66 Cr = 4.7%; full FY27 programme 313 Cr x 1.887 = 590.6 Cr = 18.3% | FAIL MINOR |
| EM-09 | 22 categories plus R1 addressed (R07 L65-67, L161) | 23 of 23 | | PASS |
| EM-10 | Section 3 summary table and Strong/Moderate count (R07 L155-157) | 23 rows; 0 Strong, 4 Moderate (EM L183) | | PASS |
| EM-11 | Completionist guard and documented-item recount line (R07 L41-46, L157-159) | "📄 recount performed: 11 documented items across 7 categories" (EM L184) | 3 + 3 + 1 + 1 + 1 + 1 + 1 = 11 across 7 | PASS |
| EM-12 | Likelihood x impact raw matrix (R07 L171-172) | HH=4 through LL=1 applied | every scored row maps correctly | PASS |
| EM-13 | Evidence multiplier by tier (R07 L173) | B3 at 0.7 (claim), while the same row tags its moat conclusion as inference (EM L200, L184) | at 0.5: 1.0, total 12.4; at 1.0: 2.0, total 13.4; MODEST in every case | FAIL MINOR |
| EM-14 | No claim-only row scored as documented (verifier rule 3) | D1 and H3 at 0.7; H1 at 0.5 | | PASS |
| EM-15 | Full scoring table, all 23 rows (R07 L173-174) | A1-A4 share one row, B1-B2 share one row: 19 rows (EM L198-199) | grouped rows all score 0; total unaffected | FAIL MINOR |
| EM-16 | Adjusted total | 12.8 (EM L217) | 1.4 + 1.0 + 0.7 + 2.0 + 1.0 + 2.0 + 2.0 + 1.0 + 1.0 + 0.7 = 12.8 | PASS |
| EM-17 | Classification band (R07 L175-176) | MODEST | 12-24 -> MODEST | PASS |
| EM-18 | I1/I2 contribution stated separately (R07 L180-181) | 0.0 of 12.8 (EM L219) | | PASS |
| EM-19 | Category 21 (I1) present; above 0 only with both legs, (b) with a documented source (R07 L122-138; verifier rule 8) | present, scored 0 | | PASS |
| EM-20 | Category 22 (I2) present; above 0 only with a named, specific sacrifice (R07 L139-153; verifier rule 8) | present, scored 0 | | PASS |
| EM-21 | I2 answered "for each moat claimed anywhere in this scan" (R07 L140-141) | answers network, owned fleet and hubs, price pass-through; F2 and G1 (both Moderate) not named (EM L153) | I2 score 0 unaffected | FAIL MINOR |
| EM-22 | Section 4, R1 (4A, 4B, 4C) (R07 L161-168) | present; R1 = 0 | | PASS |
| EM-23 | Register: four-column table and optionality_register[] in YAML (R07 L183-196) | 8 rows in both places | | PASS |
| EM-24 | Register covers advantages scored 0 or resting only on claim or inference (R07 L184) | "Customised supply chain solutions with storage" (claim, Pres. p.19; EM L28) absent | 1 item missing | FAIL MINOR |
| EM-25 | Section 6A-6E; 6C uses the injected B01 values (R07 L198-210) | 63, 11/60, 3 moats, GOOD (EM L258-260) match the B01 block | | PASS |
| EM-26 | 6D label from the standard set; full reasoning for HIGH POTENTIAL or TURNAROUND (R07 L203-208) | GOOD, with reasoning | the cell mapping is NOT VERIFIABLE: the rule source names the labels, not the matrix cells | PASS |
| EM-27 | YAML schema (R07 L216-243) | every field present; em_classification MODEST; active_categories has only Strong/Moderate rows; evidence_mix 11/5/4 matches EM L184; analyst_note about 100 words | | PASS |

Emerging Moat: 27 checked, 21 pass, 6 fail (all MINOR).

### Emerging Moat findings

**EM-04 (MINOR). Two anchors are incomplete.**
- Rule: "SOURCE ANCHORS on every evidence item: (AR p.__), (Q_ FY__ call), (Inv. Pres. slide __)" (R07 L35-36).
- Defects: EM L189 cites "May call p.?" for "impact of DFC will not be much". EM L98 cites "FY25 AR" with no page. The stage flagged the first one itself (B07 flags).
- Effect: no score changes. 4B feeds R1, which scores 0. C2 also rests on AR p.79 and Note 20(h) p.210.

**EM-08 (MINOR). The 2C basis is a guided plan, not capex under execution.**
- Rule: "total capex under execution × historical fixed asset turnover = implied incremental revenue, expressed as % above current revenue; show the arithmetic" (R07 L59-62).
- Delivered: the H2 FY27 guide of 150-160 Cr, a management claim (call p.6), x 1.887 = 292.5 Cr = 9.1% (EM L67). The vehicle-only floor is 6.3% (EM L68). The arithmetic is shown and correct.
- Why it fails: the filed figure for capex under execution is the capital commitment of 79.84 Cr gross at 31 Mar 2026 (AR Note 30 p.215, per EM L57).
- Recompute on that basis: 79.84 x 1.887 = 150.66 Cr = 4.7% of 3,221.11 Cr.
- Another basis is the full FY27 programme: H1 158 + H2 midpoint 155 = 313 Cr. That gives 313 x 1.887 = 590.6 Cr = 18.3%. The delivered 9.1% sits between the two.
- Effect: no phase-1 classification uses capex_embedded_growth_pct. Stage 11 should see all three bases.

**EM-13 (MINOR). The B3 evidence tier is tagged two ways.**
- Rule: multiply by evidence quality, 1.0x documented, 0.7x claim, 0.5x inference (R07 L173).
- Delivered: 0.7 (claim) (EM L200). The same row calls the moat conclusion "inferred". The recount lists "B3 moat conclusion" as an inference item (EM L184). EM L94 calls it "a claim".
- Recompute: at 0.5 the row gives 1.0 and the total is 12.4. At 1.0, keyed to the documented counts, the row gives 2.0 and the total is 13.4. All three totals are MODEST. The stage should state which evidence item the multiplier keys to.

**EM-15 (MINOR). Scorecard rows are grouped.**
- Rule: "Full scoring table, all 23 rows, adjusted total" (R07 L173-174).
- Delivered: 19 rows. "A1, A2, A3, A4" share one row and "B1, B2" share another (EM L198-199). Every grouped row scores 0, so the total is unaffected.

**EM-21 (MINOR). I2 is not answered for every claimed moat.**
- Rule: "For each moat claimed anywhere in this scan, answer: what SPECIFIC thing would the best-resourced competitor have to destroy in its own P&L or org to copy this?" (R07 L140-141).
- Delivered: answers for (1) network density, (2) owned fleet and hubs, and (3) fuel and price pass-through, then "Honest answer for most claims: execution lead" (EM L153). F2 (execution) and G1 (war chest) are both Moderate rows, and neither gets a named answer.
- Effect: I2 stays at 0 under any answer. The top band needs a documented competitor source, and the corpus holds none (EM L153).

**EM-24 (MINOR). One item is missing from the optionality register.**
- Rule: the register lists "forward advantages that scored 0 or rest only on 🎙️/🔍 evidence" (R07 L184).
- Missing: "Customised supply chain solutions with storage" is an ANNOUNCED claim item with no warehouse capex and no revenue (EM L28). It is not in the register (EM L226-235, B07 block).
- Converting evidence would be committed warehouse capex or a disclosed contract-logistics revenue line.

### Emerging Moat sensitivity

- The lowest recompute any rule requires is 12.4 (EM-13). MODEST holds.
- The stage's own sensitivity is correct: one raw point off E1 or G1 gives 11.8, which is NONE (EM L221).
- Observation (not a finding): the stage describes C2 as "not an improving trend, it is a standing feature" (EM L98) and G2 as "a flat structural strength, not a forming one" (EM L144). Each still scores 1.0. Each row does carry one qualifying item from its category list: new customer additions, 10 lakh plus vs about 9 lakh (EM L98), and WC days 12.1 to 11.7 with receivable days 10.7 to 9.7 (EM L144). So both scores are within the rule.
- If both rows were read as standing features and scored 0, the total would be 10.8, which is NONE. The observation that separates the two readings is a trend in top-10 share or customer count across more than two years (C2), and a third year of WC days (G2).

## OBSERVATIONS (not counted, no PASS/FAIL)

1. D1 and D3 use lease-inclusive debt (G0 L87-91). The rule fixes no debt definition, and the report gives its reason (EBITDA is before lease rent). D3 at 1.01 sits 0.01 above the 1.0 band edge. Ex-lease, D3 would be 0.40 and score 4 (G0 L91), and D1 would be 0.67x and score 4 (G0 L89). The delivered core would then be 65. The choice is consistent across D1 and D3.
2. The FAT definition differs between stages. B01 M3 uses 1.40x on net block of 2,304.55 Cr (G0 L109). B07 2C uses 1.887x on net PPE of 1,706.79 Cr, excluding ROU assets (EM L66). Neither rule fixes the denominator, and neither score changes.
3. [INFERENCE] The ROCE proxy denominator jumps from 786.61 Cr (FY19) to 1,071.30 Cr (FY20) (G0 L44-45). If lease liabilities enter borrowings only from FY20, A4 compares a lease-free FY17 with a lease-inclusive FY26. The report does not say. The separating observation is the FY17 to FY19 lease line.
4. B07 6D (GOOD) rests on the injected B01 GOOD. If Gate 0 reading (b) is ruled to bind, the injected classification becomes AVERAGE and 6D needs a re-check.
5. The G1 recount counts the ICRA "A+ (positive)" outlook as documented, sourced to Pres. p.16. The ICRA rationale on file is dated 2025-11-19 (EM L139). G1 keeps its documented net debt and CFO items either way, so no score changes.
6. The B01 M8 anchor reads "AR 2026 .txt p.77 (line 3823); anchor pinned by orchestrator per the stage hand-back" (G0 L120). Verifier A should confirm this anchor. I note the orchestrator edit for provenance.
7. B01 M12 and B07 G2 rest on the same WC days (11.7 and 12.1). The 07 rule does not bar this, and B07 scores G2 as Weak. I note it so that no later stage counts the same evidence a third time.

## OUT OF SCOPE THIS PHASE

- Verifier rules 4, 5 (valuation severity), 7, 11, 12, 13, 14 and 15 need B10/B11. They are pending phase 3.
- Rule 6 (B09 downstream candidates), rule 9 (stage 13 narrative) and rule 10 (09b dossier) fall outside the B01/B07 scope named in the task message. I did not check them.

## COUNT

75 rules checked. 64 pass. 11 fail: 0 CRITICAL, 2 MAJOR, 9 MINOR. Acceptance rate 85.3%.

```yaml
stage: B12c
company: "VRLLOG"
run_date: "2026-11-12"
model: "claude-opus-5-5"
status: complete
scope: "phase 1: Gate 0 (B01) and Emerging Moat (B07) only; valuation half pending phase 3"
gate0:
  rules_checked: 48
  rules_passed: 43
  fails:
    - {id: "G0-07", rule: "FCF fixed formula: capex = purchase of PPE + intangibles, exclude acquisitions (01-gate-0-pipeline.md L39-40)", severity: "MAJOR", delivered: "FY17-FY24 capex replaced by -CFI; B2 4, B3 5, Block B 14", recomputed: "reading (a) fixed-formula years FY25-FY26: B2 5, B3 461.75/419.75 = 1.10 -> 5, Block B 18 with B4 3; reading (b) NOT FOUND: B2 0, B3 0, Block B 5, deal-breaker 2 fires", effect: "classification GOOD under delivered and (a); AVERAGE under (b)"}
    - {id: "G0-27", rule: "E2 promoter change over 3 years; NOT FOUND scores 0 (L91-92, L20-21)", severity: "MAJOR", delivered: "3 on 31 Mar 2024 to 30 Sep 2026 window", recomputed: "0; 30 Sep 2023 start point NOT FOUND; 5.4% promoter sale undated in corpus; Block E 15; core 60", effect: "GOOD holds at the band floor"}
    - {id: "G0-04", rule: "ROCE = EBIT / (TA - CL) or source figure (L29-31)", severity: "MINOR", delivered: "proxy (PBT+Int)/(Equity+Reserves+Borrowings); FY26 18.1%", recomputed: "FY26 proxy 414.50/2,296.57 = 18.05%; strict FY26 18.9%, FY25 15.8%; A1 3, A2 1, A4 5 unchanged", effect: "none"}
    - {id: "G0-41", rule: "M12 0-15 days consistently (L134-135)", severity: "MINOR", delivered: "3 on FY25 and FY26 only", recomputed: "0 under reading (b); moat 8, 2 present, MODERATE", effect: "class unchanged"}
    - {id: "G0-03", rule: "show every number extracted (L14)", severity: "MINOR", delivered: "yearly revenue FY18-FY25, FY23 revenue, yearly net worth not shown", recomputed: "C3, M4, M10, M11, A3 re-derived from stated intermediates only", effect: "none shown"}
  classification_delivered: "GOOD (core 63, moat 11 MODERATE, grand total 74)"
  classification_recomputed: "GOOD at core 60 with E2 corrected; GOOD at core 64 under reading (a); AVERAGE at core 51 under reading (b)"
  separating_observation: "FY17-FY24 purchase of PPE and intangibles from earlier AR cash-flow statements; 30 Sep 2023 shareholding pattern"
emoat:
  rules_checked: 27
  rules_passed: 21
  fails:
    - {id: "EM-04", rule: "source anchor on every evidence item (07-emerging-moat-pipeline.md L35-36)", severity: "MINOR", delivered: "May call p.? (4B); FY25 AR with no page (C2)", recomputed: "no score effect", effect: "none"}
    - {id: "EM-08", rule: "2C capex under execution x historical FAT (L59-62)", severity: "MINOR", delivered: "H2 FY27 guided capex 150-160 Cr x 1.887 = 9.1%", recomputed: "commitments 79.84 Cr x 1.887 = 150.66 Cr = 4.7%; full FY27 programme 313 Cr x 1.887 = 590.6 Cr = 18.3%", effect: "capex_embedded_growth_pct basis-dependent; no phase-1 class effect"}
    - {id: "EM-13", rule: "evidence multiplier by tier (L173)", severity: "MINOR", delivered: "B3 at 0.7 while its moat conclusion is tagged inference", recomputed: "0.5 -> total 12.4; 1.0 -> total 13.4", effect: "MODEST unchanged"}
    - {id: "EM-15", rule: "full scoring table, all 23 rows (L173-174)", severity: "MINOR", delivered: "19 rows; A1-A4 and B1-B2 grouped", recomputed: "grouped rows all 0; total 12.8", effect: "none"}
    - {id: "EM-21", rule: "I2 answered for each moat claimed (L140-141)", severity: "MINOR", delivered: "F2 and G1 not named", recomputed: "I2 stays 0", effect: "none"}
    - {id: "EM-24", rule: "optionality register covers 0-scored or claim/inference-only advantages (L184)", severity: "MINOR", delivered: "customised supply chain solutions with storage (Pres. p.19) absent", recomputed: "1 item to add", effect: "none"}
  em_score_delivered: 12.8
  em_score_recomputed: "12.4 to 13.4 by B3 multiplier; MODEST in every case"
valuation: {rules_checked: 0, fails: [], status: "pending phase 3"}
expectation_ledger: {present: "pending phase 3", downside_row: "pending phase 3", all_rows_confirm_by: "pending phase 3", all_rows_metric_threshold: "pending phase 3", prob_in_range: "pending phase 3", decay_status_valid: "pending phase 3", off_ledger_credit: "pending phase 3", residual_pct_cmp: "pending phase 3", residual_starter_cap_ok: "pending phase 3", fails: []}  # rules 13-14; any fail = REWORK stage 11
business_narrative: {present: "pending phase 3", fails: []}  # rule 9; any fail = REWORK stage 13
recomputed_destination_pe: "pending phase 3"
recomputed_decision: "pending phase 3"
findings:
  - {id: "G0-07", severity: "MAJOR", summary: "FCF FY17-FY24 built on -CFI, not the fixed capex line; Gate 0 is GOOD (core 64) under one admissible reading and AVERAGE (core 51) under the other; FY17-FY24 capex lines separate them"}
  - {id: "G0-27", severity: "MAJOR", summary: "E2 scored 3 on a 2.5-year window; 30 Sep 2023 start point NOT FOUND and a 5.4% promoter sale is undated; E2 0, core 60, GOOD at band floor"}
  - {id: "G0-04", severity: "MINOR", summary: "ROCE proxy denominator, disclosed and tested on FY25-FY26; FY26 18.05% shown as 18.1%; no band change"}
  - {id: "G0-41", severity: "MINOR", summary: "M12 consistently scored on 2 of 10 years; 0 under reading (b); class MODERATE unchanged"}
  - {id: "G0-03", severity: "MINOR", summary: "yearly revenue, FY23 revenue and yearly net worth not shown; scores re-derivable only from intermediates"}
  - {id: "EM-04", severity: "MINOR", summary: "two incomplete anchors (May call p.?, FY25 AR page)"}
  - {id: "EM-08", severity: "MINOR", summary: "2C uses a guided H2 plan, not capex under execution; 4.7% on commitments, 18.3% on the full FY27 programme, 9.1% delivered"}
  - {id: "EM-13", severity: "MINOR", summary: "B3 tier tagged both claim and inference; total 12.4 to 13.4, MODEST holds"}
  - {id: "EM-15", severity: "MINOR", summary: "scorecard shows 19 rows, not 23; grouped rows are all 0"}
  - {id: "EM-21", severity: "MINOR", summary: "I2 sacrifice question not answered for F2 and G1; score 0 unaffected"}
  - {id: "EM-24", severity: "MINOR", summary: "customised supply chain solutions item missing from the optionality register"}
critical_count: 0
major_count: 2
minor_count: 9
acceptance_rate: 85.3
```
