# VERIFIER C: FRAMEWORK ADHERENCE, CNL (Creative Newtech Ltd), run 2026-11-11

Scope: PHASE 1 ONLY. Gate 0 (B01) and Emerging Moat (B07) compliance. The valuation audit (rule 4, rules 5 and 7, rules 11-15) is deferred to phase 3 because B10 and B11 do not exist yet. Rules 6 (B09 downstream candidates), 9 (stage 13 narrative) and 10 (B09b dossier) are not in this invocation's scope (task message: "Run ONLY the Gate 0 (B01) and Emerging Moat (B07) compliance checks").

Rule sources: prompts/01-gate-0-pipeline.md ("01" below) and prompts/07-emerging-moat-pipeline.md ("07" below). The only other inputs were the artifacts: outputs/reports/01-gate0.md + outputs/blocks/B01-gate0.yaml ("B01 rpt"), and outputs/reports/07-emoat.md + outputs/blocks/B07-emoat.yaml ("B07 rpt"). Anchors are file line numbers (L).

Boundary: I check how the rules were applied, not raw numbers. Recomputations below are arithmetic on the inputs each report states. Whether those inputs match the source PDFs is Verifier A's call, and A's verdict binds.

Headline: 43 rules checked, 37 passed (86.0%). Findings: 0 CRITICAL, 2 MAJOR, 4 MINOR. Both stage classifications survive:
- B01 stays AVERAGE in every reading. DB4 (cumulative CFO/PAT -1.52) pins it there.
- B07 stays MODEST, but the corrected em_score is 12.5, only 0.5 above the 12.0 floor.

---

## PART 1: GATE 0 (B01) COMPLIANCE

### 1A Rule-by-rule table

| # | Rule (01 anchor) | What B01 did (B01 rpt anchor) | Verdict | Recomputed value beside FAIL |
|---|---|---|---|---|
| G01 | Op rule 6: opening data line, min 3 yrs (01 L23-25) | "Data available: 8 years (FY19 to FY26). Scoring adapted to 8-year history" (L3) | PASS | |
| G02 | Data confidence tier, history downgrade (01 L142-144) | 8 yrs = 7-9 moderate, no downgrade; history_downgrade false (L3, YAML L140) | PASS | |
| G03 | Op rule 3: show every number and the score for each metric (01 L14) | B3 gives no ratio, and its bound is garbled ("at most -328.71 + 19.04 + ... bounded", L45). DB2 line reads "Block B 8 < 8" for B = 0 (L106) | FAIL (MINOR) | Cum FCF <= cum CFO -328.71 less known capex 6.12 = -334.83, so B3 ratio <= -1.55. Score 0 unchanged |
| G04 | Op rule 4: anchor on every number. YAML data_notes must carry proxy bases (01 L15-18, L189-190) | M11 inputs (3-yr CAGRs 24.7% / 44.9%; S&A % 2.67% FY23 / 2.71% FY26) have no anchor or "computed" label. S&A stands in for "selling exp" (01 L131) but data_notes does not list this proxy (L90; YAML L141-151) | FAIL (MINOR) | M11 = 3 unchanged |
| G05 | Op rule 5: NOT FOUND = 0, no gap fills (01 L19-22) | B4, E2, E3, M6, M12 are NOT FOUND and scored 0. FY19-FY24 FCF is bounded negative by CFO < 0 with capex >= 0 (L40-41). That is a logical bound, not an estimate | PASS | |
| G06 | ROCE formula: EBIT / (TA - CL), fixed, "do not substitute alternatives"; compute only when source ROCE absent (01 L27-31). Op rule 2: no qualitative judgments (01 L13) | Substituted capital employed = Equity + Reserves + Borrowings for all 8 years, picked as the "conservative proxy". The written formula was computed only as a cross-check: FY25 22.9%, FY26 26.3% (L16, L30) | FAIL (MAJOR) | See 1C. Written formula: A = 18 (2 computable yrs) or A = 4 (strict NOT FOUND); core 56 or 42; FY26 ROCE 26.3% lifts M3 1 -> 5 (moats 4, STRONG). Maker: A 11, core 49, MODERATE. Classification AVERAGE in all readings |
| G07 | ROE = PAT / avg NW; state if closing used (01 L32-33) | Series given; FY19 closing-only stated (L34) | PASS | |
| G08 | WC days formula; state basis (01 L34-38) | Sales basis stated (L46-48) | PASS | |
| G09 | FCF = CFO - capex, excluding acquisitions (01 L39-40) | FY25 +19.04, FY26 -275.18; rest bounded (L41) | PASS | |
| G10 | CAGR = (End / Start)^(1/yrs) - 1 (01 L41) | 7 intervals. Revenue (2,704.04 / 367.62)^(1/7) - 1 = 33.0%. PAT (61.87 / 5.85)^(1/7) - 1 = 40.1% (L52-55) | PASS | Re-derived 33.0% and 40.1% |
| G11 | CAGR edge rules: negative endpoint N/M; loss-to-profit note; C4 = 0 if PAT N/M (01 L43-50) | All endpoints positive, PAT positive every year (L109). No N/M, no swing, so nothing to note. Correctly not triggered | PASS | |
| G12 | Block A thresholds (01 L54-59) | A1 median 19.3 -> 3; A2 min 14.9 -> 3; A3 median ROE 18.5 -> 4; A4 decline 3.6pp -> 1; A = 11 (L32-35) | PASS on stated inputs (input definition fails at G06) | Median of the proxy series = (19.0 + 19.6) / 2 = 19.3. ROE median (18.3 + 18.8) / 2 = 18.55 |
| G13 | Block B thresholds (01 L61-68) | B1 -1.52 -> 0; B2 1/8 -> 0; B3 negative -> 0; B4 NOT FOUND -> 0; B = 0 (L43-46) | PASS | CFO sum re-derived -328.71 |
| G14 | Block C thresholds (01 L70-74) | 5/5/5/5 = 20 (L53-56); C4 +7.1pp >= +3 | PASS | |
| G15 | Block D thresholds, non-financial bands (01 L76-86) | D1 3.32x -> 0; D2 4.96x -> 2; D3 0.89 -> 3; D4 1.68 -> 4; D = 9 (L61-64) | PASS (see O2, O3) | 302.09 / 91.05 = 3.32; 102.42 / 20.66 = 4.96; 324.27 / 363.63 = 0.89; 921.66 / 548.38 = 1.68 |
| G16 | Block E thresholds (01 L88-95) | E1 56.62% -> 4; E2 NOT FOUND -> 0; E3 NOT FOUND -> 0; E4 4.6% -> 5; E = 9 (L71-74) | PASS (see O5) | 16.58 / 363.63 = 4.56% |
| G17 | Block F: 12 tests as specified; PEER DATA NEEDED = 0 (01 L97-135) | Per-test re-derivation in 1B. Moat score 11 (L78-93) | PASS on stated inputs (M3 input fails at G06; basis note O1) | 3+0+1+3+0+0+0+1+0+0+3+0 = 11 |
| G18 | Moat class: present at >= 3; 2-3 = MODERATE (01 L99, L137-138) | M1, M4, M11 = 3 -> MODERATE (L93) | PASS on stated inputs | |
| G19 | Classification matrix (01 L146-149) | Core 49 in 40-59 -> AVERAGE (L98-101) | PASS | |
| G20 | Deal-breakers 1-9, with the driving years stated (01 L151-159) | DB2 (B 0 < 8, max GOOD) and DB4 (-1.52 < 0.50, max AVERAGE) triggered, years FY19-FY24 and FY26 stated. DB6 not triggered (3.32x > 3 but IC 4.96x >= 3). DB5 not assessable (pledge NOT FOUND). Others correctly not triggered (L105-109) | PASS | |
| G21 | FLAG-GATE0 if <= AVERAGE with depressors (01 L175-177) | Present with reason (YAML L11-12) | PASS | |
| G22 | Output: dashboard, bars, classification box, strongest/weakest, decision line; all YAML fields; model; analyst_note <= 200 words (01 L161-198) | All present. model claude-sonnet-5-5 matches .claude/agents/stage-01-gate0.md. analyst_note about 104 words | PASS | |

Gate 0: 22 checked, 19 passed, 3 failed (86.4%).

### 1B Block F per-test re-derivation (stated inputs, B01 rpt L78-91)

| Test | Stated input | Band applied (01) | B01 | Re-derived |
|---|---|---|---|---|
| M1 | EBITDA margin +0.58pp (2.79% -> 3.37%); rev CAGR 33.0% | stable +/-2pp and CAGR >= 10% = 3 (L102-104) | 3 | 3 |
| M2 | peer data absent | PEER DATA NEEDED = 0 (L100) | 0 | 0 |
| M3 | FAT 220x; ROCE 14.9% (FY26 proxy) | FAT > 1x and ROCE > 12% = 1 (L107-108) | 1 | 1 on proxy. 5 on the written formula (26.3%) (G06) |
| M4 | 0 decline years; receivable days +32.5 | not "stable +/-10"; "max 1 decline year" = 3 (L109-111) | 3 | 3 |
| M5 | peer data absent | 0 | 0 | 0 |
| M6 | R&D NOT FOUND | 0 | 0 | 0 |
| M7 | no licence-limited segment | unregulated = 0 | 0 | 0 |
| M8 | reach quantified (31+ branches, 10,000+ partners); growth not shown | no band for "quantified, growth unknown". Floor of the ladder = 1 (L120-122) | 1 | 1 (conservative ladder reading) |
| M9 | peer data absent | 0 | 0 | 0 |
| M10 | grew every year; receivable days +32.5 (> 10) | fails 5 and 3 (not stable); fails 1 (no decline years); else 0 (L126-128) | 0 | 0 (mechanical, as written) |
| M11 | 8 yrs; latest 3y 24.7% < prior 44.9%; S&A % stable | CAGR >= 20% and selling % stable = 3 (L129-133) | 3 | 3 (anchor and proxy gap at G04) |
| M12 | FY26 74.7, FY25 42.6; earlier NOT FOUND | NOT FOUND = 0 | 0 | 0 |

### 1C Recomputation for G06 (ROCE formula substitution)

01 L27-31 fixes ROCE = EBIT / (Total Assets - Current Liabilities) and forbids alternatives. B01 says CL by year exists only for FY25 and FY26 (B01 rpt L16). It then swapped in Equity + Reserves + Borrowings for all 8 years, on the grounds that the written formula "flatters FY26" (L30). That is a judgment call, and 01 Op rule 2 (L13) excludes judgment calls. The written formula has two as-written readings:

| Reading | A1 | A2 | A3 | A4 | Block A | Core | M3 | Moats present / class | Moat score | Grand | Classification |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B01 as filed (proxy CE, 8 yrs) | 3 (19.3%) | 3 (14.9%) | 4 | 1 (-3.6pp) | 11 | 49 | 1 | 3 / MODERATE | 11 | 60 | AVERAGE |
| R1: written formula, computable years FY25-FY26 (22.9%, 26.3%) | 4 (median 24.6%) | 5 (min 22.9%) | 4 | 5 (26.3 >= 22.9) | 18 | 56 | 5 (FAT 220x, ROCE 26.3% > 20%) | 4 / STRONG | 15 | 71 | AVERAGE |
| R2: written formula, FY19-FY24 NOT FOUND (Op rule 5), series metrics scored 0 | 0 | 0 | 4 | 0 | 4 (DB1 triggers, max GOOD, non-binding) | 42 | 5 on latest FY26, or 0 if a median basis is used | 4 STRONG or 3 MODERATE | 15 or 10 | 57 or 52 | AVERAGE |

R1 rests on 2 years, which is below Op rule 6's 3-year minimum (01 L23). R2 is the strict reading. B01's proxy lands between the two, so the "conservative" label is wrong: the proxy is more generous than R2 on Block A (11 vs 4).

Decision effect: none. Core stays in 40-59 under R1 and R2, and DB4 caps the result at AVERAGE whatever the core is. moat_class can read STRONG instead of MODERATE. B07 6C quotes "3 confirmed, class MODERATE" (B07 rpt L268), so that figure is soft.

### 1D Gate 0 observations (not scored as FAILs)

- O1. 01 L107 does not say which ROCE M3 uses (latest or median). B01 used the latest-year proxy (14.9%) and did not say why. On the median proxy (19.3%), M3 = 3 (FAT > 2x and ROCE > 15%), giving 4 moats and STRONG. Classification unchanged. The operator should state the M3 ROCE basis in 01.
- O2. EBITDA basis: D1 and M1 exclude other income (EBITDA 91.05, L60), while EBIT for Block A and D2 includes it (PBT + interest, L16). On the EBIT-consistent basis (91.05 + 12.89 = 103.94), ND/EBITDA = 302.09 / 103.94 = 2.91x, so D1 = 1, D = 10, core 50, still AVERAGE. 01 does not define EBITDA, so this is not a rule FAIL.
- O3. D2 4.96x falls in the gap between bands "3-4.9" and "5-9.9" (01 L80-81). Treated as < 5, it scores 2, which is what B01 did. Rounded to one decimal (5.0), it scores 4 and core rises by 2. Still AVERAGE.
- O4. Stacking every favourable reading (R1 Block A 18, D1 1, D2 4): core = 18 + 0 + 20 + 12 + 9 = 59. Using B01's own Sep-26 Block D estimate of about 15 (L66): core about 62, which the matrix would grade GOOD. DB4 (cumulative CFO/PAT -1.52 < 0.50, 01 L156) still caps at AVERAGE. AVERAGE is robust to every input-definition question raised here.
- O5. E1 uses the 31-Mar-26 holding of 56.62% (AR, the latest available) instead of the latest quarter (01 L89). This is disclosed (YAML L148). The score of 4 holds unless the holding has moved below 50%.

---

## PART 2: EMERGING MOAT (B07) COMPLIANCE

Evidence tiers are written in words here: DOC = documented (1.0x), CLAIM = management claim (0.7x), INFER = analyst inference (0.5x) (07 L29-34, L173).

### 2A Rule-by-rule table

| # | Rule (07 anchor) | What B07 did (B07 rpt anchor) | Verdict | Recomputed value beside FAIL |
|---|---|---|---|---|
| E01 | Op rule 1: all six sections plus the Optionality Register (07 L28, L183-196) | Sections 1-6 and the register present (L10-288) | PASS | |
| E02 | Op rule 2: tier on every scored evidence item (07 L29-34) | Every scored row's evidence table carries a tier (L83-152, L195-204) | PASS | |
| E03 | Op rule 3: source anchor on every evidence item (07 L35-36) | Several items anchor to upstream stage outputs, not source documents: G2 row 2 (DOC) "B05 flags" (L133); G1 "(B01)" (L128); F2 B05 record (L125); H2 "59% of FY26 segment result (B05)" (L152); 1C "B05" (L35, L38) | FAIL (MINOR) | No score change. The G2 row 2 source is results Q2 FY27 p.13 (per B01 rpt L10) |
| E04 | Op rule 5 / Section 3: each of the 22 categories has an evidence table or NO EVIDENCE FOUND (07 L39-40, L65-67) | All 22 addressed: A1-A3, B1-B3, D1-D2, E1-E2, F2, G1, H3, I1, I2 NO EVIDENCE FOUND; A4, C1, C2, F1, G2, H1, H2 tabled (L78-157) | PASS | |
| E05 | R1 via Section 4 (4A/4B/4C) (07 L161-168) | 4A, 4B, 4C present; R1 scored 2 x 0.7 = 1.4 (L190-207) | PASS | |
| E06 | Section 3 summary table: all 22 rows; Strong/Moderate count stated (07 L155-158) | 22 rows (L161-184); "Count with Strong/Moderate evidence: 3 (C2, H1, H2); Strong: 0" (L186) | PASS | |
| E07 | Op rule 6 completionist guard; recount line in the set form (07 L41-46, L157-159) | "recount performed: 10 documented items across 8 categories"; 8 active, below the 12 trigger; items listed (L186; YAML L24) | PASS | |
| E08 | L x I matrix: HH 4, HM/MH 3, HL/MM/LH 2, ML/LM 1, LL 1 (07 L171-172) | A4 MM 2; C1 ML 1; C2 HM 3; F1 ML 1; G2 LM 1; H1 MM 2; H2 MM 2; R1 MM 2 (L217-224) | PASS | All 8 mappings re-derived |
| E09 | Evidence multiplier matches the stated tier; a CLAIM-only category scored as DOC is a finding (07 L172-173; verifier rule 3) | C1 scored 1.0x DOC. B07's own table tags the category's substance (recurring/embedded benefit) CLAIM and says "no recurring revenue disclosed" (L99-101). The only DOC item is the Zicom acquisition action, which H1 already credits (L141). The register lists "Zicom SaaS recurring monitoring revenue" as a watched option (L238; YAML L39) | FAIL (MAJOR) | C1 = 1 x 0.7 = 0.7; em_score 12.8 -> 12.5; class MODEST (unchanged); margin above the 12.0 floor falls from 0.8 to 0.5 |
| E10 | Adjusted total arithmetic (07 L174) | 1.4 + 1.0 + 3.0 + 1.0 + 1.0 + 2.0 + 2.0 + 1.4 = 12.8 (L226) | PASS (on rows as scored) | 12.8 |
| E11 | Full scoring table, all 23 rows (07 L171-174) | 8 rows listed; the rest collapsed as "all other 14 + I1, I2" (L225). 8 + 14 + 2 = 24, not 23 | FAIL (MINOR) | Residual is 13 + I1, I2 = 15 zero rows: A1, A2, A3, B1, B2, B3, D1, D2, E1, E2, F2, G1, H3, I1, I2. Total unchanged |
| E12 | Bands absolute, no rescale (07 L175-181) | 12.8 in 12-24 -> MODEST (L229) | PASS | 12.5 corrected -> still MODEST |
| E13 | I1/I2 contribution stated separately (07 L180-181) | "I1/I2 contribution: 0.0" (L228) | PASS | |
| E14 | Verifier rule 8 / 07 L122-138: Category 21 (I1) present; > 0 only if both legs are evidenced and leg (b) has >= 1 DOC | Present; neither leg evidenced; 0 (L156) | PASS | |
| E15 | Verifier rule 8 / 07 L139-153: Category 22 (I2) present; > 0 only with a specific named sacrifice | Present; "nothing must be destroyed" for Honeywell, WOZOYO, STQC, Zicom; 0 (L157) | PASS (coverage note O8) | |
| E16 | Section 1: 1A status/evidence/launch/potential/difference; 1B directions; 1C mix table (07 L48-55) | Present (L12-38). The 1C "profitability impact" content sits in the margin-direction cell | PASS | |
| E17 | Section 2 incl. 2C arithmetic; never estimate (07 L57-63; non-negotiable) | 2A/2B/2D present. 2C: owned capex under execution NOT FOUND, so capex_embedded_growth_pct = "NOT FOUND", with a non-capex cross-check kept separate (L44-71) | PASS | |
| E18 | Optionality Register: four columns; carried in the block; watched, never scored (07 L183-196) | 8 rows, four columns, in the block (L231-242; YAML L35-43). The Zicom-recurring overlap with C1 is graded at E09 | PASS | |
| E19 | 6C uses the injected B01 block (07 L202-203) | Core 49, grand 60, AVERAGE, 3 moats MODERATE, all matching B01 YAML (L263-269) | PASS | |
| E20 | 6D combined class; transition-setup rule; HIGH POTENTIAL and TURNAROUND reasoning (07 L203-208) | AVERAGE. MODEST is not EXPANSION, so not a transition setup. HP/TURNAROUND considered and rejected (L271-272). 07 does not reproduce the "standard matrix", so this check covers internal consistency only | PASS | |
| E21 | Output YAML fields; em_classification enum; model; analyst_note <= 200 words (07 L212-243) | All fields present; "MODEST" in enum; model claude-sonnet-5-5 matches .claude/agents/stage-07-emoat.md; analyst_note about 115 words | PASS | |

Emerging Moat: 21 checked, 18 passed, 3 failed (85.7%).

### 2B Recomputed scorecard (E09 applied; all other rows as scored)

| ID | L x I | Raw | B07 tier / mult | Corrected tier / mult | B07 adj | Corrected adj |
|---|---|---|---|---|---|---|
| A4 | MM | 2 | CLAIM 0.7 | CLAIM 0.7 | 1.4 | 1.4 |
| C1 | ML | 1 | DOC 1.0 | CLAIM 0.7 | 1.0 | 0.7 |
| C2 | HM | 3 | DOC 1.0 | DOC 1.0 | 3.0 | 3.0 |
| F1 | ML | 1 | DOC 1.0 | DOC 1.0 | 1.0 | 1.0 |
| G2 | LM | 1 | DOC 1.0 | DOC 1.0 | 1.0 | 1.0 |
| H1 | MM | 2 | DOC 1.0 | DOC 1.0 | 2.0 | 2.0 |
| H2 | MM | 2 | DOC 1.0 | DOC 1.0 | 2.0 | 2.0 |
| R1 | MM | 2 | CLAIM 0.7 | CLAIM 0.7 | 1.4 | 1.4 |
| 15 others | none | 0 | | | 0.0 | 0.0 |
| Total | | | | | 12.8 | 12.5 (MODEST) |

### 2C Emerging Moat observations (not scored as FAILs)

- O6. H1 impact "M" has no stated reason. Zicom alone is FY26 revenue 20.09 Cr, 0.74% of revenue (B07 rpt L99). If the M impact draws on Infinova (CLAIM, register row 2), H1 reads 1.0 (ML x 1.0 on Zicom only) or 1.4 (MM x 0.7). With E09, em_score would be 11.5-11.9, which is NONE. 07 gives no numeric L/I bands, so this is a judgment call, not a FAIL.
- O7. H2 credits the Honeywell licence, in force since 2016 (L148). 07 frames the scan as "moats currently FORMING that do not fully show in historical financials yet" (07 L21-24), and B07's own analyst_note calls the brand story "largely the existing Honeywell moat" (YAML L52). With H2 at 0, em_score is 10.5 after E09, which is NONE. 07's H2 checklist does list "exclusivity" without requiring it to be new, so this is not a FAIL. It is the biggest unexamined lever on the class.
- O8. I2's "for each moat claimed" (07 L140) is answered for Honeywell, WOZOYO, STQC and Zicom, but not for C2, F1, G2, CyberPowerPC or Super Micro. The 0 score holds because no named sacrifice appears anywhere.
- O9. C2 tier: a CRISIL rationale is neither "concall or presentation" (CLAIM, 07 L32-33) nor analyst inference (INFER, 07 L33-34), so DOC is the only tier the taxonomy allows. B07's own knife-edge flag (C2 as CLAIM gives 11.9, NONE; YAML L13) still stands. After E09 the same re-grade gives 11.6.
- O10. Mixed-evidence rows: 07 does not say which multiplier applies when a row has both DOC and CLAIM items. B07 used CLAIM for A4 and R1 (each has a DOC item) and DOC for G2, H1 and H2. That matches a "multiplier follows the evidence carrying the category's substance" principle, which is the principle E09 applies to C1. Under the alternative "any DOC item = 1.0x" principle: A4 2.0, R1 2.0, C1 1.0, em_score 14.0. MODEST under both principles. The operator should write a mixed-evidence rule into 07 Section 5.
- O11. Numbers for Verifier A, not graded here:
  - The 2C/4B denominator "FY26 revenue 2,717.51" (L63, L203) equals revenue from operations 2,704.62 plus other income 12.89 (B01 rpt L5, L60). That is total income, not revenue.
  - The orchestrator's appended corrections (1C CAGR 84.7% instead of 85.5%; F1 anchors AR p.41 and p.26; L346-350) are taken as read. They have no framework effect.

---

## PART 3: FINDINGS SUMMARY

| ID | Framework | Severity | Rule | Finding | Recomputed | Decision effect |
|---|---|---|---|---|---|---|
| C-G1 | Gate 0 | MAJOR | 01 L27-31 (fixed ROCE formula), L13 | Proxy capital employed substituted for TA - CL on a "conservative" judgment | A 18 / core 56 / M3 5 / STRONG (R1), or A 4 / core 42 (R2); B01 A 11 / core 49 / MODERATE | None: AVERAGE in all readings (core 40-59; DB4 cap). moat_class may be STRONG |
| C-G2 | Gate 0 | MINOR | 01 L14 | B3 ratio not stated, bound garbled; "Block B 8 < 8" typo | B3 <= -1.55, score 0 | None |
| C-G3 | Gate 0 | MINOR | 01 L15-18, L189-190 | M11 inputs unanchored; S&A-for-selling proxy missing from data_notes | M11 3 unchanged | None |
| C-E1 | Emerging Moat | MAJOR | 07 L172-173; verifier rule 3 | C1 scored DOC 1.0x on CLAIM-only substance; the DOC item is H1's Zicom action; the register calls it a watched option | C1 0.7; em_score 12.5 | None on class (MODEST); knife-edge narrows to 0.5 |
| C-E2 | Emerging Moat | MINOR | 07 L171-174 | 23-row table collapsed; "other 14" should be 13 | 15 zero rows; total unchanged | None |
| C-E3 | Emerging Moat | MINOR | 07 L35-36 | Evidence items anchored to B01/B05 instead of source documents | n/a | None |

Counts: CRITICAL 0, MAJOR 2, MINOR 4. Acceptance rate 37 / 43 = 86.0%. The denominator is at least 4, so the rate applies; it is above 60%, so no REWORK trigger from Verifier C. Rule 8 passes: categories 21 and 22 are present and correctly gated, so stage 7 needs no REWORK.

Notes for synthesis:
- Carry em_score as 12.5, not 12.8.
- Treat MODEST as one evidence re-grade away from NONE (O6, O7, O9).
- Treat the Gate 0 moat_class as MODERATE-or-STRONG pending an operator ruling on the ROCE formula and the M3 basis (C-G1, O1).
- AVERAGE is pinned by DB4.

Valuation half: PENDING. It runs in phase 3, after B10/B11 exist (rules 4, 5, 7, 11-15 and the expectation-ledger gates).

```yaml
stage: B12c
company: "CNL"
run_date: "2026-11-11"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete
scope: "phase-1 (gate0 + emoat only); valuation half pending phase 3"
gate0: {rules_checked: 22, rules_passed: 19, fails: ["C-G1 MAJOR ROCE formula substituted (proxy CE = Eq+Res+Borr) vs fixed EBIT/(TA-CL); recomputed A 18/core 56/M3 5/STRONG (2-yr reading) or A 4/core 42 (strict NOT FOUND); classification AVERAGE unchanged", "C-G2 MINOR B3 ratio not shown, bound garbled (correct <= -1.55); DB2 typo 'Block B 8 < 8'", "C-G3 MINOR M11 inputs unanchored; S&A-as-selling proxy absent from data_notes"]}
emoat: {rules_checked: 21, rules_passed: 18, fails: ["C-E1 MAJOR C1 scored documented 1.0x on claim-only substance (Zicom recurring benefit; documented item is H1's acquisition action); recomputed C1 0.7, em_score 12.5, MODEST unchanged", "C-E2 MINOR Section 5 table collapses 15 zero rows and miscounts them as 'other 14 + I1, I2' (should be 13 + I1, I2)", "C-E3 MINOR evidence items anchored to upstream stages (B01/B05) not source documents (G2 row 2, G1, F2, H2, 1C)"]}
valuation: {status: pending, rules_checked: 0, fails: []}  # phase 3, after B10/B11
expectation_ledger: {status: pending, present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: []}  # rules 13-14; any fail = REWORK stage 11; not run in phase 1
business_understanding_narrative: {status: pending, fails: []}  # rule 9; any fail = REWORK stage 13; not run in phase 1
recomputed_destination_pe: ""  # valuation pending phase 3
recomputed_decision: ""        # concur: B01 AVERAGE (pinned by DB4), B07 combined AVERAGE
findings:
  - {id: C-G1, framework: gate0, severity: MAJOR, rule: "01 L27-31 fixed ROCE formula; L13 no judgments", recomputed: "A 18 core 56 M3 5 moats 4 STRONG grand 71 (FY25-26 reading) | A 4 core 42 DB1 non-binding (strict) | filed A 11 core 49 MODERATE", decision_effect: "none; AVERAGE in all readings (core 40-59, DB4 cap); moat_class may read STRONG"}
  - {id: C-G2, framework: gate0, severity: MINOR, rule: "01 L14 show every number", recomputed: "cum FCF <= -334.83, B3 <= -1.55, score 0", decision_effect: "none"}
  - {id: C-G3, framework: gate0, severity: MINOR, rule: "01 L15-18 anchors; L189-190 proxy in data_notes", recomputed: "M11 3 unchanged", decision_effect: "none"}
  - {id: C-E1, framework: emoat, severity: MAJOR, rule: "07 L172-173 multiplier by tier; verifier rule 3", recomputed: "C1 1 x 0.7 = 0.7; em_score 12.5; MODEST", decision_effect: "none on class; margin to 12.0 floor 0.5; C2 re-grade then gives 11.6 NONE"}
  - {id: C-E2, framework: emoat, severity: MINOR, rule: "07 L171-174 all 23 rows", recomputed: "15 zero rows (A1 A2 A3 B1 B2 B3 D1 D2 E1 E2 F2 G1 H3 I1 I2); total unchanged", decision_effect: "none"}
  - {id: C-E3, framework: emoat, severity: MINOR, rule: "07 L35-36 source anchors", recomputed: "n/a", decision_effect: "none"}
critical_count: 0
major_count: 2
minor_count: 4
acceptance_rate: 86.0             # rules passed / rules checked, % (37 / 43, phase-1 scope)
```
