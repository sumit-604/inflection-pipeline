# VERIFIER C: FRAMEWORK ADHERENCE, PHASE 1 SCOPE. RKFORGE, run 2026-11-12

Model: claude-opus-5-5 (matches .claude/agents/verifier-c-framework.md frontmatter). Emits: B12c.

## Scope

- This run covers phase 1 only: Gate 0 (B01) and Emerging Moat (B07).
- The valuation audit did not run (rubric rules 4, 5, 7, 11 to 15; B10, B11). It is PENDING PHASE 3. The valuation framework docs were not loaded.
- Rule 6 needs B09, rule 9 needs stage 13, rule 10 needs B09b at /finalize. None is in this scope.
- I audit rule application only. Verifier A owns whether each number sits in its source. Where I recompute, I use the inputs the stage itself states.

Inputs read: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md, outputs/reports/01-gate0.md, outputs/blocks/B01-gate0.yaml, outputs/reports/07-emoat.md, outputs/blocks/B07-emoat.yaml.

Anchor key: B01 l.N = outputs/reports/01-gate0.md line N. B01y l.N = outputs/blocks/B01-gate0.yaml line N. B07 l.N = outputs/reports/07-emoat.md line N. B07y l.N = outputs/blocks/B07-emoat.yaml line N. P01 l.N = prompts/01-gate-0-pipeline.md line N. P07 l.N = prompts/07-emerging-moat-pipeline.md line N.

## Result

| Framework | Checks | PASS | FAIL | Critical | Major | Minor |
|---|---|---|---|---|---|---|
| Gate 0 (B01) | 26 | 21 | 5 | 0 | 1 | 4 |
| Emerging Moat (B07) | 22 | 16 | 6 | 0 | 0 | 6 |
| Valuation (B11) | PENDING PHASE 3 | - | - | - | - | - |
| Total | 48 | 37 | 11 | 0 | 1 | 10 |

- Acceptance rate: 37 / 48 = 77.1%. The denominator is 48, so the rate applies. It is above 60%. This verifier sets no REWORK trigger.
- Rubric rule 8 passes: categories 21 and 22 are present in B07 (B07 l.165, l.166). No stage 7 REWORK.
- Gate 0 classification AVOID concurs on the as-written reading. It rests on deal-breaker 6 (DB6) alone (B01 l.88, l.93).
- One MAJOR finding (G07). The maker's EBIT strips other income. On the stated inputs the as-written EBIT lifts A1 from 0 to 1 and removes DB3. AVOID survives because DB6 binds.
- Operator note N1. The word "latest" in Block D has two readings. On the latest-reported-period reading, DB6 likely does not fire and Gate 0 becomes AVERAGE. The separating observation is the Sep-26 consolidated net debt on the B01 basis. The maker's reading is the literal one, so I do not count N1 as a fail.
- Emerging Moat score 9.0, NONE, concurs (B07 l.249, l.251). Every alternative multiplier reading lands between 8.7 and 11.7, below the 12 band edge (P07 l.175 to 176).

---

## 1. Gate 0 compliance (B01)

| # | Rule (source) | Result | Evidence / recomputed value |
|---|---|---|---|
| G01 | Opening data line, history rule (P01 l.23 to 25) | PASS | "Data available: 10 years (FY17 to FY26). Scoring adapted to 10-year history" (B01 l.3) |
| G02 | Data confidence tier and downgrade (P01 l.142 to 144) | PASS | 10 years = full; history_downgrade false (B01 l.91; B01y l.29) |
| G03 | Source anchor on every number (P01 l.15 to 18) | FAIL MINOR | FY24 trade payables 1,016.63 Cr anchored "(AR2025 consolidated financial instruments note)" with no page (B01 l.38). It is the B4 earliest endpoint (5 points). See F3 |
| G04 | NOT FOUND scores 0, no estimates (P01 l.19 to 22) | PASS | B2 FY17 to FY23 (B01 l.36), E2 (l.61), M2/M5/M9 (l.71, l.74, l.78) all 0, none estimated |
| G05 | Source ROCE first; "computed" stated (P01 l.29 to 31) | PASS | Screener sheet has no ROCE row (B01y l.7); "Computed" (B01 l.25) |
| G06 | ROCE = EBIT / (Total Assets less Current Liabilities), fixed (P01 l.27 to 31) | FAIL MINOR | Proxy Equity + Reserves + Borrowings for all 10 years (B01 l.11). Formula inputs for FY25 to FY26 were read for D1/D4 (B01 l.54, l.57). Recomputed: NOT DETERMINABLE from B01. See F2 |
| G07 | EBIT, no substitute, no qualitative judgment (P01 l.13, l.27 to 31) | FAIL MAJOR | EBIT = PBT + Interest less Other income, "strips ... one-off" (B01 l.11). As written: FY24 14.4%, FY25 7.7%, median at least 10.2%; A1 0 to 1; Block A 5 to 6; DB3 does not fire. Classification AVOID unchanged. See F1 |
| G08 | ROE on average net worth; closing for first year stated (P01 l.32 to 33) | PASS | B01 l.29 |
| G09 | WC days formula; basis stated (P01 l.34 to 38) | PASS | Revenue basis stated (B01 l.38) |
| G10 | FCF = CFO less (PPE + intangibles), excl. acquisitions (P01 l.39 to 40) | PASS | B01 l.34 to 35 |
| G11 | CAGR formula and edge rules (P01 l.41, l.43 to 50) | PASS | Endpoints positive (revenue 920.73, 4,238.08; PAT 11.22, 71.80; B01 l.46 to 47). No loss-to-profit swing in annual PAT. C4 not N/M |
| G12 | Block A thresholds (P01 l.54 to 58) | PASS | 0 + 0 + 2 + 3 = 5 on the maker's ROCE series (table 1A). Score depends on G07 |
| G13 | Block B thresholds (P01 l.61 to 68) | PASS | 5 + 0 + 0 + 5 = 10 (table 1A) |
| G14 | Block C thresholds (P01 l.70 to 74) | PASS | 4 + 5 + 3 + 5 = 17 (table 1A) |
| G15 | Block D thresholds (P01 l.76 to 86) | PASS | 0 + 0 + 3 + 1 = 4 on FY26 (table 1A). D2 depends on G07. "Latest" reading: note N1 |
| G16 | Block E thresholds (P01 l.88 to 95) | PASS | 3 + 0 + 0 + 1 = 4 (table 1A). Pledge basis: note N2 |
| G17 | Block F M1 to M12 bands (P01 l.102 to 135) | FAIL MINOR | M11 1-band not tested (B01 l.80). M11 = 0 or 1; moat count and class unchanged. See F4 |
| G18 | PEER DATA NEEDED rule (P01 l.99 to 100) | PASS | M2, M5, M9 scored 0 and marked (B01 l.71, l.74, l.78) |
| G19 | Moat present at 3 or more; class bands (P01 l.98 to 99, l.137 to 138) | PASS | M4 3, M10 3: 2 present, MODERATE (B01 l.84) |
| G20 | Core, moat, grand total arithmetic | PASS | Core 5 + 10 + 17 + 4 + 4 = 40; moat 1 + 3 + 3 = 7; grand total 47 (B01y l.17 to 20) |
| G21 | Classification matrix (P01 l.146 to 149) | PASS | Core 40 sits in 40 to 59: AVERAGE before overrides (B01 l.87) |
| G22 | Deal-breakers 1 to 9 (P01 l.151 to 159) | PASS | Fired: DB1 (Block A 5 < 8), DB3 (9.5% < 10%), DB5 (16.2% > 15%), DB6 (3.65x > 3x AND 1.38x < 3x). Correctly not fired: DB2 (B 10), DB4 (2.17), DB7 (1 of 9 decline years), DB8 (PAT 291.21, 415.03, 71.80), DB9 (10 years). Result AVOID (B01 l.88 to 93). DB3 depends on G07 |
| G23 | State which years drive each deal-breaker (P01 l.153 to 154) | FAIL MINOR | DB1 carries no years (B01 l.88; B01y l.25). See F5 |
| G24 | FLAG-GATE0 when classification is AVERAGE or lower with depressors (P01 l.175 to 177) | PASS | Present with depressors named (B01y l.13) |
| G25 | YAML schema, analyst_note cap, block_b_trend label (P01 l.168 to 197) | PASS | All keys present; analyst_note about 116 words (cap 200); block_b_trend opens "improving" with numbers (B01y l.42) |
| G26 | Dashboard elements (P01 l.163 to 165) | PASS | Moat bars (B01 l.83), classification box and strongest/weakest block (l.93), decision line (l.94) |

### 1A. Block re-derivation (stated inputs, stated thresholds)

| Metric | Stated input (anchor) | Band (P01) | Maker | Verifier |
|---|---|---|---|---|
| A1 median ROCE | Sorted 10-year series, 5th and 6th values 6.17% (FY17) and 12.74% (FY18): 9.45% (B01 l.15 to 24, l.27) | < 10 = 0 (l.55) | 0 | 0 (on maker EBIT; 1 under F1) |
| A2 min ROCE | 4.72% FY20 (B01 l.18, l.28) | < 8 = 0 (l.56) | 0 | 0 |
| A3 median ROE | Sorted 1.1, 2.3, 2.4, 2.4, 14.6, 14.7, 14.7, 15.5, 20.2, 20.7: 14.65% (B01 l.29) | 12 to 14.9 = 2 (l.57) | 2 | 2 |
| A4 ROCE trend | FY26 5.12% vs FY17 6.17%: down 1.05pp (B01 l.30) | 1 to 3pp = 3 (l.58) | 3 | 3 |
| B1 CFO/PAT | 3,213.53 / 1,480.81 = 2.17 (B01 l.33) | >= 1.00 = 5 (l.62) | 5 | 5 |
| B2 FCF+ years | 1 of 3 scoreable = 33% (B01 l.36) | < 50 = 0 (l.64) | 0 | 0 |
| B3 FCF/PAT | (32.33 less 944.32 less 85.34) = -997.33 / 778.04 = -1.28 (B01 l.35, l.37) | negative = 0 (l.65 to 66) | 0 | 0 |
| B4 WC days | 87.5 (FY24) to 77.4 (FY26): -10.1 days (B01 l.39 to 42) | decreased > 5 = 5 (l.67) | 5 | 5 (note N3) |
| C1 revenue CAGR | (4,238.08 / 920.73)^(1/9) less 1 = 18.5% (B01 l.46) | 15 to 19.9 = 4 (l.71) | 4 | 4 |
| C2 PAT CAGR | (71.80 / 11.22)^(1/9) less 1 = 22.9% (B01 l.47) | >= 20 = 5 (l.72) | 5 | 5 |
| C3 positive YoY | 8 of 9 = 88.9% (B01 l.48) | 75 to 99 = 3 (l.73) | 3 | 3 |
| C4 PAT less revenue CAGR | +4.4pp (B01 l.49) | >= +3pp = 5 (l.74) | 5 | 5 |
| D1 ND/EBITDA | 2,285.87 / 627.00 = 3.65x (B01 l.52 to 54) | > 3x = 0 (l.77 to 78) | 0 | 0 |
| D2 interest cover | 294.11 / 212.50 = 1.38x (B01 l.55) | < 1.5 = 0 (l.80 to 81) | 0 | 0 (on maker EBIT; see F1) |
| D3 D/E | 2,448.77 / 3,290.40 = 0.74 (B01 l.56) | 0.5 to 1.0 = 3 (l.83) | 3 | 3 |
| D4 current ratio | 244,775.39 / 213,167.59 lakh = 1.15 (B01 l.57) | 1.0 to 1.19 = 1 (l.85 to 86) | 1 | 1 |
| E1 promoter | 40.93% (B01 l.60) | 40 to 49.9 = 3 (l.89) | 3 | 3 |
| E2 3-year change | NOT FOUND (B01 l.61) | rule 5: 0 (l.20 to 22) | 0 | 0 |
| E3 pledge | 16.2% of promoter shares (B01 l.62) | > 15 = 0 (l.93) | 0 | 0 (note N2) |
| E4 contingent / NW | 581.61 / 3,290.40 = 17.7% (B01 l.63) | 15 to 30 = 1 (l.94 to 95) | 1 | 1 |
| M1 | EBITDA margin -2.9pp, revenue CAGR 18.5% (B01 l.70) | declined 2 to 5pp despite growth = 1 (l.102 to 104) | 1 | 1 |
| M3 | FAT 1.13x, ROCE 5.1% (B01 l.72) | FAT > 1x AND ROCE > 12% needed for 1 (l.107 to 108) | 0 | 0 |
| M4 | 1 decline year (FY20), recovered (B01 l.73) | max 1 decline, recovered = 3 (l.109 to 111) | 3 | 3 |
| M6 | R&D 0.2% of revenue (B01 l.75) | < 1% fails every band (l.114 to 116) | 0 | 0 (note N7) |
| M7, M8 | Unregulated; B2B, no outlets (B01 l.76 to 77) | 0 (l.117 to 122) | 0, 0 | 0, 0 |
| M10 | Growth 8 of 9 years; receivable days fell (B01 l.79) | all but 1 year AND stable = 3 (l.126 to 128) | 3 | 3 (note N4) |
| M11 | Latest 3-yr 9.9% vs prior 37.9%; full-window 18.5% (B01 l.80, l.46) | 1-band: growth > 15% but selling % rising (l.132) | 0 | 0 or 1, NOT DETERMINABLE (F4) |
| M12 | WC days 77 to 104 (B01 l.81) | > 45 = 0 (l.134 to 135) | 0 | 0 |
| Totals | | | Core 40, moat 7, 2 present, MODERATE | Same on maker inputs |

---

## 2. Emerging Moat compliance (B07)

| # | Rule (source) | Result | Evidence / recomputed value |
|---|---|---|---|
| E01 | All six sections plus register, one response (P07 l.28) | PASS | Sections 1 to 6 and the register present (B07 l.11 to 324) |
| E02 | Section 1: 1A, 1B, 1C content (P07 l.49 to 55) | PASS | 1A (B07 l.14 to 23), 1B five axes (l.26 to 32), 1C current %, 3-year %, margin direction, impact (l.35 to 43). Status "DROPPED": note N5 |
| E03 | Section 2: 2A to 2D; 2C arithmetic shown (P07 l.57 to 63) | PASS | 2C: 550 x 1.22 = Rs 672 Cr = 15.9% of Rs 4,238 Cr, with the FY24 1.82x sensitivity (B07 l.74 to 79); block 15.9 (B07y l.31) |
| E04 | Taxonomy on every evidence item; anchors (P07 l.29 to 36) | FAIL MINOR | Untagged descriptive items; uneven tagging of deck-reported history. No score change. See F6 |
| E05 | 22 categories plus R1 addressed or NO EVIDENCE FOUND (P07 l.39 to 40, l.65 to 67) | PASS | A1 to I2 (B07 l.101 to 166); R1 (l.197 to 217). H2 says "scored 0 here" with the reason (l.161); it is addressed |
| E06 | Section 3 summary: 22 rows, four columns (P07 l.155 to 157) | PASS | B07 l.169 to 192 |
| E07 | Strong/Moderate count and the recount line (P07 l.44 to 46, l.157 to 159) | FAIL MINOR | "1 of 22" should read 0 of 22 plus R1 Moderate; recount mixes units. See F8 |
| E08 | Completionist trigger at 12 or more active (P07 l.41 to 46) | PASS | 7 active, below 12 (B07 l.194) |
| E09 | Raw score from likelihood x impact matrix (P07 l.171 to 172) | PASS | 7 of 7 scored rows correct (table 2A) |
| E10 | Evidence multipliers 1.0 / 0.7 / 0.5 (P07 l.172 to 173) | FAIL MINOR | No mixed-tier rule stated; H3 treated apart from B2, C2, E2, R1. Range 8.7 to 11.7, NONE throughout. See F7 |
| E11 | No claim-only category scored as documented (rubric rule 3) | PASS | C1 is the only claim-only scored row; 0.7 applied (B07 l.232) |
| E12 | Adjusted total arithmetic | PASS | 1.4 + 0.7 + 1.4 + 1.4 + 1.0 + 1.0 + 2.1 = 9.0 (B07 l.230 to 249) |
| E13 | Classification band (P07 l.175 to 176) | PASS | 9.0 < 12: NO MEANINGFUL EMERGING MOAT, block "NONE" (B07 l.251; B07y l.19) |
| E14 | I1/I2 contribution stated separately (P07 l.177 to 181) | PASS | 0.0 line (B07 l.248); no threshold crossed via I1/I2 (l.251) |
| E15 | Category 21 I1: both legs, (b) leg documented, else 0 (P07 l.122 to 138; rubric rule 8) | PASS | Both legs absent; 0 (B07 l.165) |
| E16 | Category 22 I2: named sacrifice, else 0 (P07 l.139 to 153; rubric rule 8) | PASS | "nothing must be destroyed": 0 (B07 l.166) |
| E17 | One improvement, one mechanism (CLAUDE.md NEVER list; B07 own rule l.98) | FAIL MINOR | Railway share rise evidences both B2 and C2. Worst case 7.6, NONE unchanged. See F9 |
| E18 | Register definition and table (P07 l.183 to 196) | PASS | Four columns; rows score 0 or rest on claim/inference evidence (B07 l.256 to 267) |
| E19 | Register carried in the block (P07 l.194 to 196) | FAIL MINOR | 9 of 10 rows carried; one row lost. See F10 |
| E20 | Section 6: 6A to 6E; 6C uses injected B01; HIGH POTENTIAL and TURNAROUND reasoned (P07 l.198 to 210) | PASS | 6A (B07 l.273 to 278); 6B (l.281 to 288); 6C core 40, 2 moats, MODERATE, AVOID, 47 (l.291 to 301) matches B01y l.17 to 23; 6D (l.304 to 307); 6E (l.310 to 324). Matrix source: note N6 |
| E21 | YAML schema, vocabulary, active_categories Strong/Moderate only, analyst_note cap (P07 l.216 to 243) | PASS | All keys; em_classification "NONE"; active_categories holds R1 only (B07y l.20 to 21); analyst_note about 143 words |
| E22 | Report YAML and block file are one copy (P07 l.214) | FAIL MINOR | Block carries an anchor-errata line the report lacks. See F11 |

### 2A. Scorecard re-derivation

Matrix: HH 4, HM/MH 3, HL/MM/LH 2, ML/LM 1, LL 1 (P07 l.172). Multipliers: documented 1.0, claim 0.7, inference 0.5 (P07 l.173).

| Row | L x I (B07) | Raw | Tiers present in the row | Multiplier used | Adjusted | Verifier |
|---|---|---|---|---|---|---|
| B2 | M x M | 2 | 3 documented, 2 claim (l.111 to 115) | 0.7 | 1.4 | Arithmetic PASS; tier choice F7 |
| C1 | L x M | 1 | claim only (l.120) | 0.7 | 0.7 | PASS |
| C2 | M x M | 2 | 3 documented, 1 inference, 1 claim (l.124 to 128) | 0.7 | 1.4 | Arithmetic PASS; tier choice F7; overlap F9 |
| E2 | M x M | 2 | 3 documented, 1 claim (l.139 to 142) | 0.7 | 1.4 | Arithmetic PASS; tier choice F7 |
| F2 | L x M | 1 | documented only (l.150 to 152) | 1.0 | 1.0 | PASS |
| H3 | L x L | 1 | 1 documented, claim items (l.162) | 1.0 | 1.0 | Arithmetic PASS; tier choice F7 |
| R1 | M x H | 3 | documented JV capital, claim offtake (l.217) | 0.7 | 2.1 | Arithmetic PASS; tier choice F7 |
| Total | | | | | 9.0 | PASS, NONE |

Multiplier sensitivity (F7): all mixed rows at 0.7 = 8.7. All mixed rows at 1.0 = 2.0 + 2.0 + 2.0 + 3.0 + 1.0 + 1.0 + 0.7 = 11.7. Maker = 9.0. All three sit below 12, so the class is NONE in every reading. The maker's own all-upgrade case (C1 upgraded too) is 12.0 (B07 l.251). C1 has no documented item, so that case is a ceiling, not a reading.

---

## 3. Findings (FAIL detail)

### F1 (G07). MAJOR. EBIT definition strips other income.
- Rule. "FORMULA DEFINITIONS (fixed, do not substitute alternatives)" (P01 l.27). The source ROCE is first choice, and the rule names screener (P01 l.29 to 31). Operating rule 2: "No qualitative judgments" (P01 l.13).
- B01 says. "EBIT = PBT + Interest - Other income (operating; strips FY24 other income 36.41 and FY25 109.33 which includes a one-off)" (B01 l.11; B01y l.31).
- Two readings. (a) EBIT = PBT + finance cost. This is the convention behind the screener ROCE that the rule names first. (b) Operating EBIT, the maker's choice. Reading (a) is the as-written one. The formula block bars substitutes, and removing a one-off is a qualitative judgment. Reading (b) also mismatches the ratio: the denominator keeps the capital that earns the other income.
- Recomputed on stated inputs. FY24 (516.42 + 36.41) / 3,840.41 = 14.4%. FY25 (289.31 + 109.33) / 5,163.87 = 7.7%. I hold the other eight years at the maker's values. The sorted 5th and 6th values become 7.72% and 12.74%, so the median is 10.2%. Non-negative other income can only raise it. B01 does not itemise other income for those eight years (NOT FOUND in verifier inputs); the screener rows settle it.
- Effect. A1 moves from 0 to 1 (band 10 to 14.9, P01 l.55). Block A moves from 5 to 6. DB3 (median ROCE < 10%) does not fire. A2 and A4: NOT DETERMINABLE. A2 stays 0 unless FY20 other income is at least 61.33 Cr (8% x 1,868.99 less 88.19). D2 moves from 0 to 1 if FY26 other income is at least 24.64 Cr (1.5 x 212.50 less 294.11). The DB6 cover leg (< 3x) holds unless FY26 other income is at least 343.39 Cr (3 x 212.50 less 294.11). Core becomes 41 (42 if D2 lifts). Grand total becomes 48 (49).
- Decision. Classification AVOID is unchanged. DB6 binds, and DB1 still fires at Block A 6 (< 8). B07 6C lists "also DB1, DB3, DB5" (B07 l.296). DB3 would drop from that line.
- Fix. Stage 1 re-scores A1, A2, A4, M3 and D2 on PBT + finance cost from the screener rows. Or the operator defines EBIT in prompt 01, and reading (b) becomes the rule.

### F2 (G06). MINOR. ROCE denominator is a proxy for all ten years.
- Rule. ROCE = EBIT / (Total Assets less Current Liabilities) (P01 l.29).
- B01 says. Capital employed = Equity + Reserves + Borrowings, "Total assets less Other Liabilities proxy" (B01 l.11; B01y l.7, l.31).
- Gap. The proxy counts short-term borrowings as capital. The formula removes them as current liabilities. The proxy also leaves out non-current liabilities other than debt, which the formula keeps. For FY25 and FY26 the formula inputs were in the corpus. B01 read current liabilities 213,167.59 lakh and the borrowings split 161,556.58 + 71,946.77 lakh from AR2026 p.164 (B01 l.54, l.57).
- Recomputed. NOT DETERMINABLE from B01. Total assets and the current share of borrowings are not stated.
- Effect. The proxy is disclosed and uniform across years. A1 and DB3 sit near the 10% line (F1), so the basis matters there. The classification does not move (DB6).
- Fix. State the FY25 and FY26 formula ROCE beside the proxy.

### F3 (G03). MINOR. Weak anchor on a scored endpoint.
- Rule. Anchors take the form "(AR p.187, Note 27)" (P01 l.15 to 18).
- B01 says. FY24 trade payables 1,016.63 Cr "(AR2025 consolidated financial instruments note)" with no page (B01 l.38). It is the earliest endpoint of B4, worth 5 points. Company-reported net debt 1,638.78 Cr "(standalone MD&A ...; AR2026)" also has no page (B01 l.54), but it is not scored.
- Fix. Add the AR2025 page. Verifier A owns whether the number is on that page.

### F4 (G17). MINOR. M11 1-band not tested.
- Rule. M11: "growth >15% but selling % rising = 1" (P01 l.132).
- B01 says. "Latest 3-yr revenue CAGR 9.9% vs prior 37.9%; below 20%" (B01 l.80). This tests the 5-band and the 3-band only.
- Recomputed. Full-window revenue CAGR is 18.5% (B01 l.46). FY26 selling and admin share = 248.98 / 4,238.08 = 5.9% (computed from B01 l.52). FY17 share: NOT FOUND in B01. M11 = 1 if the share rose and the band reads on the full-window CAGR. Otherwise M11 = 0.
- Effect. Moat score 7 becomes 8 at most. M11 at 1 is not a present moat (3 or more), so the count stays 2 and the class stays MODERATE.
- Fix. State the selling-expense share for FY17 and FY26 and score the 1-band.

### F5 (G23). MINOR. DB1 driving years not stated.
- Rule. "state WHICH years drive any deal-breaker" (P01 l.153 to 154).
- B01 says. Years are named for DB3 (FY17, FY20, FY21, FY25, FY26), DB5 (30 Sep 2026) and DB6 (FY26) (B01 l.88 to 89; B01y l.26 to 28). The DB1 string carries none (B01y l.25).
- Recomputed. DB1 rests on A1 (the same five sub-7% years) and A2 (FY20, 4.72%).
- Fix. Add the years to the DB1 string.

### F6 (E04). MINOR. Taxonomy not applied to every item.
- Rule. The taxonomy applies "to every single piece of evidence" (P07 l.29 to 30).
- B07 says. These items carry no tag: 2B utilisation rows (B07 l.66 to 70), 1C shares (l.37 to 43), 2D Europe 41% and Asia Rs 1.88 Cr (l.91, l.93), and the H3 net-zero 2040 and ZLD 2030 targets (l.162).
- Uneven tagging. Deck-reported history is tagged documented in B2 (slide 11, l.111) and E2 (slides 9 and 12, l.139). It is tagged claim in H3 (slides 22 to 23, l.162).
- Effect. No scored row changes, because the multiplier is set per category (F7).
- Fix. Tag every item. State one rule for deck-reported history.

### F7 (E10). MINOR. No rule for rows that mix evidence tiers.
- Rule. One multiplier per tier (P07 l.172 to 173). P07 gives no rule for a category that holds more than one tier, and B07 states none.
- B07 says. B2, C2, E2 and R1 are mixed and take 0.7 (B07 l.230, l.233, l.237, l.247). H3 is mixed and takes 1.0 (l.244).
- Two readings. (a) The multiplier keys to the tier behind the forward claim being scored. This fits all five rows if the H3 L x L rests on the commissioned 10.24 MW solar alone (l.162). (b) The multiplier keys to the strongest item in the row, which puts all five at 1.0.
- Recomputed. 8.7 (all mixed rows at 0.7) to 11.7 (all at 1.0). Both are below 12, so NONE holds.
- Separating observation. An operator line on mixed-tier rows in P07 Section 5.
- Fix. B07 states the mixed-tier rule it applies in Section 5.

### F8 (E07). MINOR. Count line and recount mix units.
- Count line. B07 says "Categories with Strong or Moderate evidence: 1 of 22 (R1 only, see Section 4/5)" (B07 l.194). R1 is the 23rd row. Of the 22 categories, 0 are Strong or Moderate.
- Recount. B07 counts "14 documented items across 6 categories (R1 1, B2 3, C2 2, E2 3, F2 4, H3 1)" (B07 l.194; B07y l.23). The tables differ. C2 holds 3 documented rows: TML share, non-auto FY25 to FY26, and two customers above 10% from Note 34 (l.124, l.125, l.128). F2 holds 3 documented rows: four lines in one row, casting promise met, and margin up four quarters (l.150 to 152). The F2 count of 4 counts the four lines as items but drops two documented rows. The C2 count drops the Note 34 row.
- Recomputed. 14 on a row basis (R1 1, B2 3, C2 3, E2 3, F2 3, H3 1). 17 on an item basis (F2 6). The claim count of 10 leaves out the Ind-Ra preferred-supplier row, which is tagged claim (l.115). The correct claim count is 11. evidence_mix {14, 10, 3} carries the same counts (B07y l.22).
- Effect. No score changes. The guard result stands (7 active, below 12).
- Fix. Recount on one unit and correct evidence_mix.

### F9 (E17). MINOR. One railway improvement backs two categories.
- Rule. CLAUDE.md NEVER list: "Never credit one quality improvement through two mechanisms." B07's own single-credit rule covers the wheel JV and the capacity lines (B07 l.98), not railway assemblies.
- B07 says. Railway share rose from 4.6% (FY25) to 7.5% (FY26) of standalone revenue (B07 l.18). That rise is B2 evidence (l.111). It is also most of the C2 evidence "Non-auto share 22% FY25 to 26% FY26" (l.125): about 2.9 of the 4 points. This is approximate, because the standalone deck basis is set against the Ind-Ra figure.
- Two readings. (a) Two different claims (qualification lock-in and customer spread) may cite one fact. (b) One improvement is credited twice.
- Separating observation. Whether C2 holds M x M on the TML share fall (documented, l.124) and the order mix (claim, l.127) alone.
- Recomputed. If the overlapping row is dropped, C2 likely stays 1.4. If C2 is dropped entirely, the total is 7.6. NONE holds either way.
- Fix. State which row owns the railway ramp.

### F10 (E19). MINOR. Register row lost from the block.
- Rule. The register is "Carried in the B07 block as optionality_register[]. Synthesis merges register items into the monitoring checklist." (P07 l.194 to 195).
- B07 says. The report table holds 10 rows (B07 l.258 to 267). The block holds 9 (B07y l.32 to 41; report YAML l.365 to 374).
- Missing row. "Cold forging and casting approvals as lock-in | Customer approval letters; utilisation above 75% sustained | Concalls; utilisation table | 12 months" (B07 l.265). Synthesis would lose this watch item.
- Fix. Add the row to optionality_register in B07y.

### F11 (E22). MINOR. Two versions of the B07 block exist.
- Rule. "Full six-section report, then end with exactly this fenced YAML block" (P07 l.214). The block file is the copy of that block.
- B07 says. The block file adds a sixth input_gaps line with anchor errata (B07y l.12). The report YAML lacks it (B07 l.340 to 345). The report body still prints the anchors the errata correct: ESOP AR p.10 (l.146), AR p.36 (l.160), AR p.18 (l.19), Inv. Pres. slide 8 (l.253), and Jan call "MD/NJ p.5" (l.114).
- Fix. Keep one copy. Correct the body anchors or mark the errata in the body. Verifier A owns which anchor is true.

---

## 4. Operator notes (not counted as fails)

### N1. "Latest" in Block D sets the AVOID label.
- The question. D1 to D4 say "(latest)" (P01 l.77 to 86). E1 says "(latest quarter)" (P01 l.89). The rule does not define "latest".
- Reading (a), the maker's. The latest fiscal year of the scored history, FY26 (B01 l.51, l.55). The E1 wording supports this reading, so it is the literal one and not a FAIL.
- Reading (b). The latest reported period: the TTM to Sep 2026 and the Sep-26 balance sheet.
- Numbers under (b). TTM EBITDA = 162.21 + 203.00 + 217.86 + 255.55 = 838.62 Cr (B01 l.97). TTM cover is 2.04x, so D2 = 1 (B01 l.55). D1 stays above 3x only if Sep-26 net debt on the B01 basis exceeds 3 x 838.62 = 2,515.86 Cr. FY26 net debt was 2,285.87 Cr (B01 l.53). Sep-26 net debt on that basis is NOT FOUND in verifier inputs. B07 reports an H1 debt cut of Rs 126 Cr on the company basis (B07 l.306).
- Classification under (b). If DB6 does not fire, the caps are DB1 (max GOOD), DB3 (max AVERAGE, on the maker's EBIT) and DB5 (max AVERAGE). The matrix gives AVERAGE (core 40 to 59). The AVOID label therefore turns on this one word.
- Disclosure. B01 shows the D2 TTM sensitivity and says "the Sep-26 balance sheet was not scored" (B01y l.43). It does not show the D1 sensitivity.
- Separating observation. An operator ruling on "latest" in the prompt 01 D-block. Then the Sep-26 consolidated borrowings less cash.

### N2. Pledge basis.
- P01 l.93 does not name the base. B01 uses % of promoter shares (16.2%) and also shows % of total equity (6.7%) (B01 l.62). The standard disclosure basis supports the maker.
- On the total-equity basis, E3 = 1 and DB5 does not fire. The classification is unchanged (DB6).

### N3. B4 is fragile.
- B4 = 5 on reported trade receivables (B01 l.42). Non-recourse discounted bills of 399.78 Cr sit outside that line. "Trade Receivables" (P01 l.35) is the reported line, so the rule was applied as written.
- With the add-back, WC days rise 24 days and B4 would be 0 (B01 l.42). This is already flagged (B01y l.35; FLAG-CASH, B01y l.14).

### N4. M10 reading.
- The 3-band reads "growth all but 1 year AND stable" (P01 l.127). Receivable days fell from 175.9 to 68.5 (B01 l.79). The 5-band test is one-sided ("rose ≤10 days", P01 l.126 to 127), so a fall meets the receivable leg.
- The 102.9-day add-back figure (B01 l.79) is also a fall. M10 = 3 stands either way.

### N5. B07 status outside the list.
- B07 1A row 8 has status "DROPPED" (B07 l.23). This is outside the six-status list (P07 l.50 to 51). It is informative and has no score effect.

### N6. Combined matrix not in the rule source.
- B07 6D applies "the standard matrix" (P07 l.203 to 204), but P07 does not state that matrix. I checked 6D for internal consistency only.
- Gate 0 AVOID plus EM NONE gives AVOID, and HIGH POTENTIAL and TURNAROUND are reasoned (B07 l.304 to 307). Under N1 reading (b), Gate 0 AVERAGE plus EM NONE would need the matrix to place it.

### N7. M6 label is moot.
- B01 marks M6 "margin vs peers PEER DATA NEEDED" (B01 l.75). R&D at 0.2% already fails every M6 band (P01 l.114 to 116), so the label is cosmetic.

### N8. Instruction-file defect in prompt 12.
- prompts/12-verifiers-pipeline.md l.379 reads `(same line, comment "# rule 9; any fail = REWORK stage 13")`. The audit item VER-08 said to keep the business_understanding_narrative line and fix only its comment (audits/PROMPT_AUDIT_2026-10.md l.1960 to 1965). The patch replaced the whole line with the instruction text instead.
- The B12c block below carries the intended key, marked pending. The operator should restore the line in prompt 12.

---

## 5. Not checked in this scope

- B11 valuation: rubric rules 4, 5, 7, 11, 12, 13, 14, 15. PENDING PHASE 3.
- Rule 6 (B09 downstream candidates): B09 is not a phase-1 input to this verifier.
- Rule 9 (Business Understanding Narrative, stage 13): not run yet.
- Rule 10 (B09b dossier): fires at the /finalize verifier pass. The phase-1 structural check sits in run-pipeline step 6b.
- Source fidelity of any number: Verifier A.

```yaml
stage: B12c
company: "RKFORGE"
run_date: "2026-11-12"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete  # phase-1 scope: Gate 0 (B01) + Emerging Moat (B07); valuation half PENDING PHASE 3
gate0:
  rules_checked: 26
  fails:
    - "G07 MAJOR: EBIT strips other income (B01 l.11). As written EBIT = PBT + finance cost: FY24 ROCE 14.4%, FY25 7.7%, median >= 10.2% if unitemised other income is non-negative; A1 0 -> 1, Block A 5 -> 6, core 40 -> 41, grand total 47 -> 48, DB3 not fired; D2 0 -> 1 if FY26 other income >= 24.64 Cr. Classification AVOID unchanged (DB6, DB1)"
    - "G06 MINOR: ROCE denominator proxy Equity + Reserves + Borrowings for all 10 years, not Total Assets less Current Liabilities, though FY25-FY26 formula inputs were read (AR2026 p.164, B01 l.54, l.57). Recomputed NOT DETERMINABLE from B01"
    - "G03 MINOR: FY24 trade payables 1,016.63 Cr, the B4 earliest endpoint, anchored without a page (B01 l.38)"
    - "G17 MINOR: M11 1-band (growth >15% but selling % rising) not tested (B01 l.80); FY17 selling share NOT FOUND; M11 0 or 1; moat count 2 and MODERATE unchanged"
    - "G23 MINOR: DB1 driving years not stated (B01y l.25); drivers FY20 (A2 4.72%) and FY17, FY20, FY21, FY25, FY26 (A1)"
emoat:
  rules_checked: 22
  fails:
    - "E04 MINOR: taxonomy tag missing on descriptive items (2B utilisation l.66-70, 1C shares l.37-43, 2D l.91 and l.93, H3 targets l.162); deck history tagged documented in B2/E2 but claim in H3; no score change"
    - "E07 MINOR: count line '1 of 22' should read 0 of 22 plus R1 Moderate (B07 l.194); recount 14 mixes units (C2 3 documented rows not 2; F2 3 rows or 6 items, not 4); row basis 14, item basis 17; claim count 11 not 10; evidence_mix wrong (B07y l.22); guard result unchanged"
    - "E10 MINOR: no mixed-tier multiplier rule stated; B2, C2, E2, R1 at 0.7, H3 at 1.0; recomputed range 8.7 to 11.7, NONE in every reading"
    - "E17 MINOR: railway share 4.6% to 7.5% (FY25 to FY26, B07 l.18) backs both B2 (l.111) and the C2 non-auto rise (l.125, about 2.9 of 4 points); worst case total 7.6, NONE unchanged"
    - "E19 MINOR: register row 'Cold forging and casting approvals as lock-in' (B07 l.265) missing from optionality_register (B07y l.32-41; 9 of 10 rows)"
    - "E22 MINOR: report YAML (B07 l.340-345) and block file (B07y l.12) differ; block carries anchor errata the report body does not correct"
valuation: {rules_checked: 0, fails: []}  # PENDING PHASE 3: B10/B11 not in phase-1 inputs, not audited
expectation_ledger: {present: false, downside_row: false, all_rows_confirm_by: false, all_rows_metric_threshold: false, prob_in_range: false, decay_status_valid: false, off_ledger_credit: false, residual_pct_cmp: 0, residual_starter_cap_ok: true, fails: []}  # rules 13-14; any fail = REWORK stage 11; PENDING PHASE 3: template defaults, not findings
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: []}  # rule 9; any fail = REWORK stage 13; PENDING (stage 13 not run): template defaults, not findings
recomputed_destination_pe: ""  # blank: valuation not in phase-1 scope
recomputed_decision: ""        # blank: Gate 0 AVOID and EM NONE concur on the as-written reading; see finding N1
findings:
  - {id: G07, framework: gate0, severity: MAJOR, rule: "P01 l.27-31 fixed ROCE formula; P01 l.13 no qualitative judgments", claimed: "EBIT = PBT + Interest - Other income; median ROCE 9.5%; A1 0; DB3 fired (B01 l.11, l.27, l.88)", recomputed: "EBIT = PBT + finance cost: FY24 14.4%, FY25 7.7%, median >= 10.2% (other eight years at maker values; their other income NOT FOUND in verifier inputs); A1 1; Block A 6; core 41 (42 if FY26 other income >= 24.64 Cr lifts D2); DB3 not fired", effect: "classification AVOID unchanged (DB6 binds; DB1 fires at Block A 6); B07 6C DB list drops DB3", fix: "stage 1 re-scores A1, A2, A4, M3, D2 on PBT + finance cost, or operator defines EBIT in prompt 01"}
  - {id: G06, framework: gate0, severity: MINOR, rule: "P01 l.29 ROCE = EBIT / (TA - CL)", claimed: "capital employed = Equity + Reserves + Borrowings, all years (B01 l.11)", recomputed: "NOT DETERMINABLE from B01 (total assets and current borrowings not stated)", effect: "none on classification (DB6)", fix: "show FY25-FY26 formula ROCE beside the proxy"}
  - {id: G03, framework: gate0, severity: MINOR, rule: "P01 l.15-18 anchor form", claimed: "FY24 trade payables 1,016.63 Cr (AR2025 consolidated financial instruments note) (B01 l.38)", recomputed: "page missing; existence is Verifier A's", effect: "B4 endpoint weakly anchored", fix: "add the AR2025 page"}
  - {id: G17, framework: gate0, severity: MINOR, rule: "P01 l.132 M11 1-band", claimed: "M11 0 on 5-band and 3-band only (B01 l.80)", recomputed: "M11 1 if selling share rose FY17 to FY26 on the 18.5% full-window CAGR, else 0; FY26 share 5.9% (248.98 / 4,238.08, B01 l.52); FY17 share NOT FOUND", effect: "moat score 7 or 8; count 2, MODERATE unchanged", fix: "state the selling share FY17 and FY26 and score the band"}
  - {id: G23, framework: gate0, severity: MINOR, rule: "P01 l.153-154 years driving each deal-breaker", claimed: "DB1 string without years (B01y l.25)", recomputed: "FY20 (A2 4.72%); FY17, FY20, FY21, FY25, FY26 (A1)", effect: "presentational", fix: "add the years to DB1"}
  - {id: E04, framework: emoat, severity: MINOR, rule: "P07 l.29-30 taxonomy on every item", claimed: "untagged 2B, 1C, 2D items and H3 targets; deck history documented in B2/E2, claim in H3", recomputed: "no score change", effect: "presentational", fix: "tag every item; one rule for deck-reported history"}
  - {id: E07, framework: emoat, severity: MINOR, rule: "P07 l.44-46, l.157-159 recount", claimed: "1 of 22 Strong/Moderate; 14 documented (R1 1, B2 3, C2 2, E2 3, F2 4, H3 1); claims 10 (B07 l.194; B07y l.22)", recomputed: "0 of 22 plus R1 Moderate; 14 rows (C2 3, F2 3) or 17 items (F2 6); claims 11", effect: "no score change; guard result stands", fix: "recount on one unit; correct evidence_mix"}
  - {id: E10, framework: emoat, severity: MINOR, rule: "P07 l.172-173 multipliers", claimed: "B2, C2, E2, R1 mixed at 0.7; H3 mixed at 1.0; total 9.0 (B07 l.230-249)", recomputed: "8.7 (all mixed 0.7) to 11.7 (all mixed 1.0)", effect: "NONE in every reading", fix: "state the mixed-tier rule in B07 Section 5; operator line in P07 Section 5"}
  - {id: E17, framework: emoat, severity: MINOR, rule: "CLAUDE.md one improvement one mechanism; B07 l.98 own convention", claimed: "railway share rise backs B2 (l.111) and C2 non-auto rise (l.125)", recomputed: "C2 likely 1.4 on TML share and order mix alone; worst case total 7.6", effect: "NONE unchanged", fix: "name the row that owns the railway ramp"}
  - {id: E19, framework: emoat, severity: MINOR, rule: "P07 l.194-195 register carried in block", claimed: "optionality_register 9 rows (B07y l.32-41)", recomputed: "10 rows; add 'Cold forging and casting approvals as lock-in' (B07 l.265)", effect: "watch item lost to synthesis", fix: "add the row to B07y"}
  - {id: E22, framework: emoat, severity: MINOR, rule: "P07 l.214 one fenced block, block file is its copy", claimed: "B07y l.12 anchor-errata gap absent from report YAML (B07 l.340-345)", recomputed: "one copy needed; body anchors at B07 l.19, l.114, l.146, l.160, l.253 uncorrected", effect: "two B07 versions in the run", fix: "single copy; mark or correct the body anchors"}
  - {id: N1, framework: gate0, severity: NOTE, counted: false, rule: "P01 l.77-86 'latest' undefined (E1 says latest quarter, P01 l.89)", claimed: "D1-D4 on FY26; AVOID by DB6 (B01 l.51-55, l.93)", recomputed: "latest-reported-period reading: TTM EBITDA 838.62 Cr (B01 l.97), D2 2.04x = 1; D1 > 3x only if Sep-26 net debt > 2,515.86 Cr vs 2,285.87 Cr FY26 (B01 l.53); Sep-26 net debt NOT FOUND in verifier inputs; if DB6 off, classification AVERAGE", effect: "AVOID label turns on this reading; maker reading is the literal one", fix: "operator ruling on 'latest' in prompt 01 D-block; then Sep-26 consolidated borrowings less cash"}
critical_count: 0
major_count: 1
minor_count: 10
acceptance_rate: 77.1             # rules passed / rules checked = 37 / 48, %
```
