# VERIFIER C: FRAMEWORK ADHERENCE, ACCORD, run 2026-10-06 (PHASE 1 SCOPE)

Model: claude-opus-5-5 (.claude/agents/verifier-c-framework.md frontmatter, effort xhigh).
Scope: Gate 0 (B01) and Emerging Moat (B07) compliance only. The valuation audit (B10, B11) is PENDING PHASE 3. I read no valuation framework document.

Inputs read:
- Rule sources: prompts/12-verifiers-pipeline.md (Verifier C section), prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md
- Artifacts: runs/accord-2026-10-06/outputs/reports/01-gate0.md, outputs/blocks/B01-gate0.yaml, outputs/reports/07-emoat.md, outputs/blocks/B07-emoat.yaml

Anchor key:
- "B01 L57" = line 57 of 01-gate0.md. "B01y L19" = line 19 of B01-gate0.yaml.
- "B07 L276" = line 276 of 07-emoat.md. "B07y L36" = line 36 of B07-emoat.yaml.
- "G0 L99" = line 99 of prompts/01-gate-0-pipeline.md. "EM L184" = line 184 of prompts/07-emerging-moat-pipeline.md.

Method:
- I re-derived every Gate 0 line score from the inputs the stage states, with the stated thresholds. I did not check any input against a source document. Verifier A owns that question.
- A rule FAILs when the score, the classification or a required element does not follow the rule as written. The recomputed value sits beside each FAIL.
- A finding can attach to a PASS rule. That happens when the score is right but a shown figure or a required declaration is wrong. Those findings are MINOR.
- Grading follows the stage-12 scale. Where the rule text is ambiguous and the stage disclosed its reading, I grade MINOR and show the strict recompute.
- Evidence tiers are written in words here (documented, claim, inference) for the three taxonomy marks.

## 1. GATE 0 (B01) COMPLIANCE TABLE

| # | Rule (source) | Stage value (anchor) | Re-derived from stated inputs | Result |
| --- | --- | --- | --- | --- |
| G01 | Opening "Data available" line (G0 L23-25) | "6 years (FY21 to FY26). Scoring adapted to 6-year history." (B01 L3) | present, and 4-year coverage of CFO, ROCE, WC days stated | PASS |
| G02 | ROCE: source figure if given, else compute and say so (G0 L29-31) | computed, "Screener export has no ROCE row" (B01 L31); AR 0.13 and 0.35 shown as cross-check (B01 L42) | FY23 1.54/4.66 = 33.0%; FY24 2.62/6.58 = 39.8%; FY25 8.57/22.65 = 37.8%; FY26 6.61/49.86 = 13.3% (inputs B01 L37-40) | PASS |
| G03 | ROE on average net worth; closing for earliest year, stated (G0 L32-33) | B01 L48-53 | 24.6, 13.3, 21.6, 30.8, 43.1, 12.8% | PASS |
| G04 | WC days formula; revenue basis unless COGS is explicit; basis stated (G0 L34-38) | revenue basis, "no COGS line in the filings" (B01 L76) | FY23 24.5, FY24 69.8, FY25 145.4, FY26 108.3 (inputs B01 L80-83) | PASS |
| G05 | FCF = CFO minus capex from cash flow statement (G0 L39-40) | B01 L68-72 | 1.61, -7.16, -11.31, 7.24; cumulative -9.62 | PASS |
| G06 | CAGR formula (G0 L41) | B01 L101-102 | revenue 30.7%, PAT 42.0% | PASS |
| G07 | CAGR edge rules (G0 L43-50) | endpoints positive; "No loss-to-profit swing" (B01y L32) | no N/M case arises | PASS |
| G08 | A1 median ROCE (G0 L55) | 35.4% = 5 (B01 L57) | (33.0 + 37.8)/2 = 35.4% -> 5 | PASS |
| G09 | A2 minimum ROCE (G0 L56) | 13.3% = 3 (B01 L58) | 12-14.9 band -> 3 | PASS |
| G10 | A3 median ROE (G0 L57) | 23.1% = 5 (B01 L59) | (21.6 + 24.6)/2 = 23.1% -> 5 | PASS |
| G11 | A4 ROCE latest vs earliest (G0 L58-59) | -19.7pp = 0 (B01 L60) | 13.3 vs 33.0, decline above 5pp -> 0 | PASS |
| G12 | B1 cumulative CFO / PAT (G0 L62-63) | -0.18 = 0 (B01 L89) | -2.29/12.92 = -0.18 -> 0 | PASS |
| G13 | B2 FCF-positive years (G0 L64) | 50% = 2 (B01 L90) | 2 of 4, 50-74 band -> 2 | PASS |
| G14 | B3 cumulative FCF / PAT (G0 L65-66) | -0.74 = 0 (B01 L91) | -9.62/12.92 = -0.74 -> 0 | PASS |
| G15 | B4 WC days change (G0 L67-68) | +83.8 days = 0 (B01 L92) | 108.3 - 24.5 = +83.8 -> 0 | PASS |
| G16 | C1 revenue CAGR (G0 L71) | 30.7% = 5 (B01 L101) | (70.05/18.38)^(1/5) - 1 = 30.7% -> 5 | PASS |
| G17 | C2 PAT CAGR (G0 L72) | 42.0% = 5 (B01 L102) | (4.50/0.78)^(1/5) - 1 = 42.0% -> 5 | PASS |
| G18 | C3 positive YoY revenue years (G0 L73) | 80% = 3 (B01 L103) | 4 of 5, 75-99 band -> 3 | PASS |
| G19 | C4 PAT CAGR minus revenue CAGR (G0 L74) | +11.3pp = 5 (B01 L104) | 42.0 - 30.7 = +11.3pp -> 5 | PASS |
| G20 | D1 net debt / EBITDA (G0 L77-79) | net cash 13.49 = 5 (B01 L113) | 8.83 - 22.33 < 0 -> 5; still net cash on CFS cash 13.43 (B01 L119) | PASS |
| G21 | D2 interest cover (G0 L80-82) | 12.0x = 5 (B01 L114) | 6.61/0.55 = 12.0x -> 5 | PASS |
| G22 | D3 debt / equity (G0 L83-84) | 0.18 = 4 (B01 L115) | 8.83/48.87 = 0.18 -> 4 | PASS |
| G23 | D4 current ratio (G0 L85-86) | 2.23 = 5 (B01 L116) | 75.29/33.80 = 2.23 -> 5 | PASS |
| G24 | E1 promoter holding, latest quarter (G0 L89-90) | 61.97% = 5, AR Note 3(c) at 31-Mar-2026 (B01 L125) | 61.97% >= 60 -> 5 | PASS (see O6) |
| G25 | E2 promoter change over 3 years (G0 L91-92) | about -38pp = 0 (B01 L126) | any filed start point (100.00% or 84.94%) to 61.97% is a fall above 3pp -> 0; a NOT FOUND start also scores 0 | PASS |
| G26 | E3 promoter pledge, latest (G0 L93) | 0% = 5, anchor prospectus 2026-02-26; "Post-listing pattern NOT FOUND" (B01 L127) | the stage itself marks the latest (post-listing) pledge NOT FOUND; G0 rule 5 (G0 L19-22) scores NOT FOUND as 0. E3 0, Block E 8, core 60, grand total 75. Band 60-79, matrix GOOD, DB4 cap AVERAGE: classification unchanged | FAIL (MINOR, F1) |
| G27 | E4 contingent liabilities / net worth (G0 L94-95) | 10.9% = 3 (B01 L128) | 5.32/48.87 = 10.9%, 5-15 band -> 3 | PASS |
| G28 | M1 pricing power (G0 L102-104) | 5 (B01 L143) | margin 7.0% to 10.0% = +3.0pp, revenue CAGR 30.7% -> 5 | PASS |
| G29 | M2 cost advantage (G0 L105-106) | PEER DATA NEEDED = 0 (B01 L144) | peer data not provided -> 0 (G0 L99-100) | PASS (see O3) |
| G30 | M3 capital efficiency (G0 L107-108) | FAT median 13.5x, median ROCE 35.4% = 5 (B01 L145) | median of 8.8, 11.2, 15.3, 15.7 is 13.25x, not 13.5x. Still above 3x with ROCE above 20% -> 5 | PASS (MINOR finding F3; see O2) |
| G31 | M4 customer stickiness (G0 L109-111) | "No row fits; scored 1" (B01 L146) | 1 unrecovered decline year has no rubric row; 1 keeps the ladder monotone; below 3 either way, not a moat | PASS (see O2) |
| G32 | M5 scale (G0 L112-113) | PEER DATA NEEDED = 0 (B01 L147) | -> 0 | PASS |
| G33 | M6 technology (G0 L114-116) | R&D NIL = 0 (B01 L148) | -> 0 | PASS |
| G34 | M7 regulatory (G0 L117-119) | unregulated = 0 (B01 L149) | no licence or regulated price in stated inputs -> 0 | PASS |
| G35 | M8 distribution (G0 L120-122) | none disclosed = 0 (B01 L150) | -> 0 | PASS |
| G36 | M9 brand (G0 L123-125) | PEER DATA NEEDED = 0; GM proxy shown and named (B01 L151) | -> 0 | PASS |
| G37 | M10 switching costs (G0 L126-128) | growth all but 1 year, receivable days fell 21.5 = 3 (B01 L152) | row 2 "stable" read on row 1's metric (rose <= 10 days); a fall qualifies -> 3 | PASS (see O2) |
| G38 | M11 network effects (G0 L129-133) | 1 (B01 L153) | latest 3-yr revenue CAGR FY23-26 19.8% is below every prior window (FY21-24 38.2%, FY21-23 49.0%), so the 5 row fails; the 3 row fails on a rising ratio; growth above 15% with a rising ratio -> 1 | PASS (MINOR finding F4) |
| G39 | M12 negative WC (G0 L134-135) | 0 (B01 L154) | 3 of 4 years above 45 days, none negative -> 0 | PASS |
| G40 | Score arithmetic | A 13, B 2, C 18, D 19, E 13, core 65; moat 15; grand total 80 (B01 L135, L155, L166) | 13+2+18+19+13 = 65; 5+0+5+1+0+0+0+0+0+3+1+0 = 15; 65+15 = 80 | PASS |
| G41 | Moats present and moat class (G0 L99, L137-138) | 3 (M1, M3, M10), MODERATE (B01 L157) | 3, in the 2-3 band -> MODERATE | PASS |
| G42 | Data confidence tier (G0 L142-144) | 6 years, lower tier, flag raised, no downgrade (B01 L165; B01y L29, L31) | as written, the tier keys to "Data available: 6 years" -> 5-6 band, no downgrade | PASS (see O1) |
| G43 | Classification matrix (G0 L146-149) | core 65 + MODERATE = GOOD (B01 L161) | core 60-79 and not STRONG or FORTRESS -> GOOD | PASS |
| G44 | Deal-breakers 1-9 (G0 L155-159) | DB4 binds, DB2 non-binding, rest not triggered (B01 L162-164) | DB4: -0.18 < 0.50 -> max AVERAGE. DB2: 2 < 8 -> max GOOD. DB1 13; DB3 35.4%; DB5 0%; DB6 net cash; DB7 1 of 5; DB8 PAT positive; DB9 6 years: none trigger. Result AVERAGE | PASS |
| G45 | Years driving each deal-breaker stated (G0 L151-154) | DB4: FY24 CFO -4.82, FY25 CFO -8.18 (B01 L162; B01y L27) | binding deal-breaker years stated; DB2 drivers sit in the Block B table (B01 L68-71) | PASS |
| G46 | FLAG-GATE0 when AVERAGE or lower with depressors (G0 L175-177) | raised (B01y L13) | condition met | PASS |
| G47 | NOT FOUND and PEER DATA NEEDED discipline (G0 L19-22, L99-100) | FY21-22 CFO, current liabilities, payables NOT FOUND; M2, M5, M9 marked (B01y L9-10, L43) | no estimated fill found | PASS (E3 handled at G26) |
| G48 | Dashboard elements (G0 L163-165) | blocks, anchored line items, classification box, strongest/weakest block, decision line present (B01 L29-177); moat profile bars absent, moat shown as a table only (B01 L141-155) | one required element missing | FAIL (MINOR, F2) |
| G49 | B01 YAML schema (G0 L168-198) | every template key present; block_b_trend opens "improving" with numbers (B01y L46) | complete | PASS (see O8) |
| G50 | analyst_note at or under 200 words (G0 L193) | about 133 words (B01y L47) | within cap | PASS |

Gate 0 result: 50 rules checked, 48 PASS, 2 FAIL (both MINOR). Classification AVERAGE confirmed. The strict recompute of every Gate 0 finding (F1 and F4 together) gives core 60, moat 14, grand total 74, moat class MODERATE, matrix GOOD, DB4 cap AVERAGE. The classification does not move.

## 2. EMERGING MOAT (B07) COMPLIANCE TABLE

| # | Rule (source) | Stage value (anchor) | Re-derived or checked | Result |
| --- | --- | --- | --- | --- |
| E01 | Emerging Moat scan, not FTTCP (EM L3-6) | stated (B07 L3) | separate | PASS |
| E02 | Section 1: 1A fields, 1B axes, 1C mix table (EM L48-55) | 8 pipeline rows with status, evidence, launch, revenue, difference; 1C expected % NOT FOUND where no target is filed (B07 L20-51) | present | PASS (see O7) |
| E03 | Section 2: 2A, 2B, 2C, 2D (EM L57-63) | B07 L55-97 | present | PASS |
| E04 | 2C: capex under execution x historical FAT, % above current revenue, arithmetic shown (EM L59-62) | 13.03 x 9.10 = 118.6, 169% above 70.07 (B07 L82, L87, L90; B07y L36) | 13.03 x 9.10 = 118.57; 118.57/70.07 = 169%. The x 11.20 cell (208%) and both all-in cells (308%, 379%) also re-derive | PASS (see O4) |
| E05 | All 22 categories addressed (EM L65-67) | A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, I1-I2 (B07 L103-211) | 22 of 22 | PASS |
| E06 | Scan each category on its own list; never force-fit (EM L39-40, L66-67) | C1 scored M x L = 1.0 on repeat orders from Sunsure and Good Earth (B07 L134, L278) | C1's list is 3+ product cross-sell, wallet share, ERP or workflow integration, co-development, AMC revenue, designed-around components (EM L86-89). The stage finds each of these absent or NOT FOUND (B07 L134). Strict reading: C1 0; em_score 7.0; NONE unchanged | FAIL (MINOR, F5) |
| E07 | Evidence taxonomy and anchors on each item (EM L29-36) | tier and anchor on the Section 3 items | present | PASS |
| E08 | No claim-only or inference-only category scored as documented (verifier rule 3) | all 5 scored rows carry documented items: B2 4, C1 2, C2 2 or 3, G1 2, H2 4 (B07 L119-127, L134, L138-144, L176, L186-192) | consistent | PASS |
| E09 | L x I matrix values (EM L171-172) | H x L = 2, M x L = 1 (B07 L276-290) | HL = 2, ML = 1 per rubric | PASS (see O5) |
| E10 | Evidence multipliers (EM L172-173) | documented 1.0 on all scored rows (B07 L276-290) | correct | PASS |
| E11 | Adjusted total | 8.0 (B07 L294; B07y L20) | 2.0 + 1.0 + 1.0 + 2.0 + 2.0 = 8.0 | PASS |
| E12 | Scoring table, all 23 rows with R1 (EM L171-174) | 23 rows (B07 L271-293) | complete | PASS |
| E13 | Classification band (EM L175-176) | 8.0 = NO MEANINGFUL EMERGING MOAT, "NONE" (B07 L297; B07y L21) | below 12 -> NONE | PASS |
| E14 | I1 and I2 contribution stated separately (EM L180-181) | 0.0 (B07 L296) | present | PASS |
| E15 | Category 21 (I1) present; above 0 only with both legs and a documented (b) leg (EM L122-138; verifier rule 8) | 0; leg (a) fails, (b) not reached (B07 L200) | correct | PASS |
| E16 | Category 22 (I2) present; above 0 only with a named, specific sacrifice (EM L139-153; verifier rule 8) | 0; "nothing must be destroyed" (B07 L211) | correct | PASS |
| E17 | I2 answered for each moat claimed in the scan (EM L140-142) | table tests B2, low overhead, BESS stance, H2 (B07 L204-209) | scored C1, C2 and G1 are not tested. I2 stays 0: B07 names no sacrifice for any of them, and a score above 0 needs one (EM L149-153) | FAIL (MINOR, F6) |
| E18 | Section 3 summary table and Strong/Moderate count (EM L155-157) | 22 rows; 0 Strong or Moderate, 5 Weak (B07 L215-240) | present | PASS |
| E19 | Completionist guard and recount line in the required form (EM L41-46, L157-159) | "14 documented items across 5 categories" (B07 L242; B07y L24) | form met; 5 active categories, below the 12 trigger | PASS (see O7) |
| E20 | Section 4: 4A, 4B, 4C for R1 (EM L161-168) | B07 L246-263 | present; R1 0 with approvals credited once in B2 | PASS |
| E21 | Optionality register: table, eligibility, YAML carry (EM L183-196) | 12 rows (B07 L311-322; B07y L37-49). Row "Customer concentration improvement (C2)" (B07 L319) | C2 scored 1.0 on documented evidence (B07 L279). Register eligibility is "scored 0 or rest only on claim or inference evidence" (EM L184-185), so this row is ineligible. No score effect, since registered items are never scored | FAIL (MINOR, F7) |
| E22 | F2 cross-references the injected B05 promise record (EM L106-107) | "2 delivered, 5 partial, 2 missed; grade C" (B07 L164) | present | PASS |
| E23 | Section 6: 6A to 6E (EM L198-210) | B07 L328-380 | present | PASS |
| E24 | 6C uses the injected Gate 0 block | core 65, moat 15 with 3 confirmed, MODERATE, AVERAGE (B07 L351-354) | matches B01y L19-25 | PASS |
| E25 | 6D combined classification; HIGH POTENTIAL and TURNAROUND reasoned (EM L203-208) | AVERAGE; both rows reasoned (B07 L360) | consistent with the stated guidance. The full combined matrix is not in the phase-1 rule sources, so I checked consistency only | PASS |
| E26 | B07 YAML schema; em_classification in the enum; active_categories holds only Strong or Moderate rows (EM L216-243) | all keys present; "NONE"; active_categories [] (B07y) | complete | PASS (see O8) |
| E27 | analyst_note at or under 200 words (EM L239) | about 136 words (B07y L58) | within cap | PASS |

Emerging Moat result: 27 rules checked, 24 PASS, 3 FAIL (all MINOR). em_score 8.0 and class NONE confirmed. The strict recompute gives 7.0, still NONE. Verifier rule 8 REWORK condition (categories 21 or 22 missing) is not met: both are present and correctly scored 0.

## 3. FINDINGS (graded)

| ID | Stage | Rule | Severity | Claimed | Recomputed | Decision effect |
| --- | --- | --- | --- | --- | --- | --- |
| F1 | B01 | G26 E3 pledge (latest) | MINOR | E3 5 on 0% pledge at prospectus 2026-02-26 (B01 L127) | E3 0; Block E 8; core 60; grand total 75 | none: band 60-79, DB4 cap AVERAGE holds |
| F2 | B01 | G48 dashboard elements | MINOR | moat profile bars absent (B01 L141-155) | add bars | none, presentational |
| F3 | B01 | G30 M3 shown figure | MINOR | FAT median 13.5x (B01 L145) | 13.25x from the four stated values | none: score 5 stands |
| F4 | B01 | G38 M11 proxy and window reasoning | MINOR | selling ratio measured on "selling and admin" (B01 L153), not declared as a proxy in data_notes; "needs FY20 for the two-window test" | proxy to be declared (G0 L189-190); the rule threshold is 6 years and 6 were available (G0 L129-130). Score 1 stands on every two-window split. Strict NOT FOUND reading of selling expense alone gives 0: moat 14, grand total 79 | none: moats confirmed 3, MODERATE |
| F5 | B07 | E06 force-fit (C1) | MINOR | C1 1.0 (B07 L278) | C1 0; em_score 7.0 | none: NONE either way |
| F6 | B07 | E17 I2 coverage | MINOR | I2 table omits C1, C2, G1 (B07 L204-209) | I2 0 | none |
| F7 | B07 | E21 register eligibility | MINOR | C2 scored 1.0 and registered (B07 L279, L319) | drop the row, or reword it to the unfiled FY26 and H1 FY27 tables only | none: register is never scored |

Why F1 is MINOR and not MAJOR. A filed pledge figure exists (0% at 2026-02-26). The defect is a stale, pre-listing anchor standing in for "latest". The stage disclosed the E3 = 0 sensitivity itself (B01 L131; B01y L42). The observation that separates the two readings is the pledge column of the first post-listing shareholding pattern.

Why F5 is MINOR and not MAJOR. The EM prompt does not say the what-to-look-for list is closed. Repeat orders carry some weight on "embedded relationships". The stage used the lowest non-zero band. The strict reading still moves the score by 1.0 only.

Combined strict recompute of all seven findings: Gate 0 core 60, moat 14, grand total 74, MODERATE, AVERAGE; Emerging Moat 7.0, NONE; combined assessment AVERAGE. No finding changes a classification or the combined assessment.

## 4. OBSERVATIONS (not graded, not counted)

O1. Data confidence tier. The stage keyed the tier to 6 years of P&L data (B01 L3). CFO, ROCE and WC days cover 4 years, FY23 to FY26 (B01 L3, B01y L31). The written rule keys the tier to "Data available: X years" (G0 L23-25, L142-144), so the stage complied. If the operator keys the tier to the shortest scored series, 4 years falls in LIMITED: the matrix GOOD drops to AVERAGE and DB4 holds AVERAGE. Only a cap-first, downgrade-second order would give AVOID, and the rule does not set the order. Operator ruling suggested on both points.

O2. Rubric gaps in Block F. M3 does not say median or latest; the stage used the period median and showed the FY26 reading (1, B01 L145; B01y L44). M4 has no row for one unrecovered decline year; the stage scored 1 and said so (B01 L146). M10 row 2 says "stable" without a metric; the stage used row 1's "rose 10 days or less" (B01 L152). The intra-period receivable-days range is 32.4 to 131.7 days (B01 L80-83), so a range-based reading of "stable" would fail M10. If both M3 (FY26 reading) and M10 fell, moats would be 1 (THIN), the matrix would give GOOD, and DB4 would still cap at AVERAGE.

O3. Peer data. M2, M5 and M9 scored 0 PEER DATA NEEDED because peer data sheets were not injected, though they exist in inputs/screening (B01y L10). The stage applied the rule as written. This is an orchestration input gap. If two of the three reached 3, moats would be 5 (STRONG), the matrix GOOD+, and DB4 would still cap at AVERAGE.

O4. Fixed asset turnover basis differs across stages. B01 uses 8.8x for FY26 on screener net block (B01 L145). B07 uses 9.10x on AR net PPE Rs 7.70 Cr (B07 L82). At 8.8x the 2C value is 13.03 x 8.8 / 70.07 = 163.6%, not 169% (B07y L36). This is an input-basis question for Verifier A. No rule effect.

O5. Likelihood ratings. B07 rates likelihood H on B2, G1 and H2. Its own text calls B2 "an entry ticket that every qualified peer holds" (B07 L128), G1 "a capital-structure strength and not a competitive one" (B07 L176), and the H2 documents "channel or discussion level, with end dates inside 15 months" (B07 L194). The rubric does not define the likelihood axis, so this is not a FAIL. An L x L reading on all five scored rows gives 5.0. The score range is 5.0 to 8.0, NONE in every case.

O6. E1 anchor. The 31-Mar-2026 holding (B01 L125) is a post-listing quarter-end figure, one quarter older than the latest filed quarter (shareholding pattern ABSENT, B01y L7). The AR Note 3(c) total row prints 84.94% against the 61.97% share-count result (B01 L131). That conflict is a number question for Verifier A.

O7. Small presentational points in B07. Two 1A statuses sit outside the enumerated list: "LAUNCHED" and "NOT PURSUED" (B07 L26-27, L31; EM L49-50). C1 and G1 give prose evidence, not an evidence table (B07 L134, L176; EM L66-67). G2 is labelled "NO EVIDENCE FOUND (INDETERMINATE)" while documented WC data exist (B07 L178); the 0 is right because the FY23 to FY26 path is 24.5 to 108.3 days (B01 L80-83), which shows no improvement trajectory. E1 gives "credited once, as capex in 2A" as its reason (B07 L156), but 2A is not a scoring row; the 0 stands because no first-mover evidence exists. The C2 table carries three documented rows (B07 L140, L141, L144) and the recount counts 2 (B07 L242); counting the adverse UGVCL row gives 15 documented items. None of these moves a score.

O8. Copy drift. The B07 block file differs from the report's YAML in two strings: the FLAG-RD-CONTRADICTION anchor ("Pros. p.117-118" in B07y L13 against "Pros. p.118" in B07 L410) and the analyst_note wording ("documented" in B07y L58 against the taxonomy mark in B07 L455). No value differs. The B01 report does not end with the fenced YAML (B01 L177); the block file B01-gate0.yaml is complete, and the agent wrapper requires the block file and the reply. Not counted as a FAIL.

O9. Prompt defect for operator fix. prompts/12-verifiers-pipeline.md line 379, inside the B12c template, reads (same line, comment "# rule 9; any fail = REWORK stage 13") and carries no key. This block supplies the key business_understanding_narrative, pending phase 3.

## 5. CARRY-FORWARD TO PHASE 3 (named here, not audited here)

- UA qualifier. em_score 8.0 sits below the "EM >=25" UA qualifier (EM L12-13, L177-178) under every recompute in this report (5.0 to 8.0).
- Single credit. Post-IPO net cash is credited in Gate 0 D1 (5, B01 L113) and in Emerging Moat G1 (2.0, B07 L286). The phase-3 audit must confirm the pillar mechanics credit it once.
- Catalyst tiers. catalysts_12m tags "documented" on events whose outcome is not filed: machinery purchase orders (none placed, B07 L61) and H1 FY27 results (not filed, B07 L14) (B07y L26, L28). The tag reflects a documented schedule. Pillar 3 catalyst proximity should read it that way.
- Verifier C rules not run in phase 1, by task scope: 4 and 5 (B11 valuation), 6 (B09 downstream candidates and stage 11 catalysts), 7 (B11 method plurality), 9 (stage 13 narrative), 10 (B09b dossier at /finalize), 11 and 12 (Role 1 exit and FV path), 13 and 14 (expectation ledger and gates), 15 (section-1b skill fidelity).

## 6. VALUATION (B11)

PENDING PHASE 3. Not run. No valuation framework document read. recomputed_destination_pe and the expectation_ledger fields stay blank.

## 7. COUNTS

- Rules checked: 77 (Gate 0 50, Emerging Moat 27). Passed: 72. Acceptance rate: 72/77 = 93.5%. The denominator is 4 or more, so the rate is applicable.
- Findings: 7, all MINOR. CRITICAL 0, MAJOR 0.
- REWORK triggers from this verifier: none. Acceptance is above 60%. Categories 21 and 22 are present in B07.

```yaml
stage: B12c
company: "ACCORD"
run_date: "2026-10-06"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete  # phase-1 scope (gate0 + emoat) complete; valuation half pending phase 3
scope: "phase 1: Gate 0 (B01) and Emerging Moat (B07) only; valuation (B10, B11) pending phase 3"
gate0:
  rules_checked: 50
  rules_passed: 48
  fails:
    - {rule: "G26 E3 promoter pledge (latest)", severity: MINOR, stage_value: "5 on 0% pledge at prospectus 2026-02-26; post-listing pattern NOT FOUND (B01 L127)", recomputed: "E3 0 under G0 rule 5; Block E 8; core 60; grand total 75; band 60-79, matrix GOOD, DB4 cap AVERAGE; classification unchanged"}
    - {rule: "G48 dashboard output elements", severity: MINOR, stage_value: "moat profile bars absent; moat shown as table only (B01 L141-155)", recomputed: "no score effect"}
emoat:
  rules_checked: 27
  rules_passed: 24
  fails:
    - {rule: "E06 scan each category on its own list, never force-fit (C1)", severity: MINOR, stage_value: "C1 M x L = 1.0 on repeat orders; every listed C1 signal absent or NOT FOUND (B07 L134, L278)", recomputed: "C1 0; em_score 7.0; NONE unchanged"}
    - {rule: "E17 I2 answered for each moat claimed in the scan", severity: MINOR, stage_value: "I2 table omits scored C1, C2, G1 (B07 L204-209)", recomputed: "I2 stays 0; no sacrifice named for C1, C2 or G1"}
    - {rule: "E21 optionality register eligibility", severity: MINOR, stage_value: "C2 scored 1.0 on documented evidence (B07 L279) and also registered (B07 L319)", recomputed: "drop the row or limit it to the unfiled FY26 and H1 FY27 tables; no score effect"}
valuation: {status: "pending phase 3", rules_checked: 0, fails: []}
expectation_ledger: {status: "pending phase 3", present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: []}  # rules 13-14; any fail = REWORK stage 11
business_understanding_narrative: {status: "pending phase 3"}  # rule 9; any fail = REWORK stage 13 (template line 379 carries no key; key supplied here)
recomputed_destination_pe: ""  # valuation pending phase 3
recomputed_decision: ""        # concur on phase-1 scope: Gate 0 AVERAGE, EM NONE, combined AVERAGE
findings:
  - {id: F1, stage: B01, rule: "G26 E3 pledge (latest)", severity: MINOR, claimed: "E3 5; Block E 13; core 65 (B01 L127, L129, L135)", recomputed: "E3 0; Block E 8; core 60; grand total 75", decision_effect: "none; AVERAGE via DB4 holds", note: "stale pre-listing anchor; stage disclosed the E3 = 0 sensitivity (B01 L131)"}
  - {id: F2, stage: B01, rule: "G48 dashboard elements", severity: MINOR, claimed: "moat table without profile bars (B01 L141-155)", recomputed: "add moat profile bars", decision_effect: "none; presentational"}
  - {id: F3, stage: B01, rule: "G30 M3 shown figure", severity: MINOR, claimed: "FAT median 13.5x (B01 L145)", recomputed: "13.25x from 8.8, 11.2, 15.3, 15.7", decision_effect: "none; M3 5 stands"}
  - {id: F4, stage: B01, rule: "G38 M11 proxy and two-window reasoning", severity: MINOR, claimed: "M11 1 on selling and admin ratio; 'needs FY20' (B01 L153)", recomputed: "proxy must be declared in data_notes; 6 years meet the rule threshold; score 1 stands on every split (FY23-26 19.8% vs FY21-24 38.2%); strict NOT FOUND reading gives 0, moat 14, grand total 79", decision_effect: "none; moats confirmed 3, MODERATE"}
  - {id: F5, stage: B07, rule: "E06 no force-fit (C1)", severity: MINOR, claimed: "C1 1.0 (B07 L278)", recomputed: "C1 0; em_score 7.0", decision_effect: "none; NONE either way"}
  - {id: F6, stage: B07, rule: "E17 I2 coverage", severity: MINOR, claimed: "I2 tested on B2, overhead claim, BESS stance, H2 only (B07 L204-209)", recomputed: "I2 0", decision_effect: "none"}
  - {id: F7, stage: B07, rule: "E21 register eligibility", severity: MINOR, claimed: "C2 scored and registered (B07 L279, L319)", recomputed: "row ineligible as worded", decision_effect: "none; register never scored"}
critical_count: 0
major_count: 0
minor_count: 7
acceptance_rate: 93.5  # 72 of 77 rules passed (gate0 48/50, emoat 24/27); denominator >= 4, applicable
```
