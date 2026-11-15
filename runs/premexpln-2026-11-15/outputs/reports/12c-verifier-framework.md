# Verifier C: Framework Adherence, PREMEXPLN, run 2026-11-15 (PHASE 1)

Model: claude-opus-5-5 | Emits: B12c | Scope: Gate 0 (B01) and Emerging Moat (B07) only.

## Scope and method

- Rule sources: prompts/01-gate-0-pipeline.md (P01) and prompts/07-emerging-moat-pipeline.md (P07). Rubric: prompts/12-verifiers-pipeline.md, VERIFIER C, rules 1-3 and 8.
- Valuation audit (B10, B11; rubric rules 4, 5, 7, 11-15): PENDING PHASE 3. The valuation framework documents were not loaded.
- Rule 6 (B09 downstream candidates) is outside this invocation. Rules 9 and 10 fire at /finalize.
- I audit rule application. Source fidelity and raw numbers belong to Verifier A. I took every input value as the maker stated it and re-derived each score from it.
- Artifacts: runs/premexpln-2026-11-15/outputs/reports/01-gate0.md, outputs/blocks/B01-gate0.yaml, outputs/reports/07-emoat.md, outputs/blocks/B07-emoat.yaml.
- Anchors: (01 l.N) = line N of 01-gate0.md. (B01 l.N) = line N of B01-gate0.yaml. (07 l.N) and (B07 l.N) = the same for stage 7. (P01 l.N) and (P07 l.N) = rule-source lines. "(derived)" marks my arithmetic on stated inputs.

## Summary

- 91 rules checked. 9 fails. 82 passed. Acceptance rate 90.1% (derived, 82 / 91). 0 CRITICAL, 4 MAJOR, 5 MINOR.
- Gate 0 classification AVERAGE (01 l.80) survives every reading. Recomputed core range is 45 to 57 against the reported 53 (01 l.79). Every value sits in the 40-59 AVERAGE band (P01 l.149).
- The Emerging Moat class MODEST (B07 l.19) does not survive the framework reading. Two independent corrections each put em_score below the 12.0 floor (P07 l.175-176): H2 gives 11.4 (or 11.3), B2 gives 10.2, both together give 9.3. Class NONE in each case. The maker's KNIFE-EDGE flag (B07 l.13) names H2 as the only swing row.
- This verifier triggers no REWORK: no CRITICAL, and the rate is above 60% on a denominator of 91. The four MAJOR items are remediation candidates for the orchestrator under the one-cycle cap.

## GATE 0 (B01) COMPLIANCE TABLE

| ID | Rule (source) | Stated input (anchor) | Re-derived | Result |
|---|---|---|---|---|
| G01 | Opening data line, history adaptation (P01 l.23-25) | "Data available: 10 years (FY17 to FY26)" (01 l.3) | Present, correct form | PASS |
| G02 | Data confidence tier (P01 l.142-144) | 10 years (B01 l.16) | 10+ = full; no downgrade; history_downgrade false (B01 l.28) | PASS |
| G03 | ROCE formula fixed; NOT FOUND scores 0 (P01 l.27-31, l.19-22) | Proxy capital employed = equity + reserves + borrowings (01 l.12; B01 l.30) | See C-G03. A4 0, Block A 0, core 48 | FAIL MAJOR |
| G04 | ROE on average net worth; earliest year on closing, stated (P01 l.32-33) | 01 l.16-25; B01 l.31 | All 10 ROE values re-derived to 0.1pp. Average net worth chain runs back to FY17 closing 125.13 (derived) vs 125.03 stated: rounding only | PASS |
| G05 | WC days formula; basis stated (P01 l.34-38) | Revenue basis memo (01 l.38) | 33.3 + 134.2 - 101.9 = 65.6; 50.2 + 96.8 - 39.0 = 108.0 (derived) | PASS |
| G06 | FCF formula: capex = PPE + intangibles purchase (P01 l.39-40) | Investing cash flow as capex proxy FY17-FY23 (01 l.36; B01 l.32) | See C-G06. Block B 5 or 12 by reading | FAIL MAJOR |
| G07 | CAGR formula (P01 l.41) | 388.34 / 237.78 and 45.81 / 15.73 over 9 years (01 l.41-42) | 5.6% and 12.6% (derived) | PASS |
| G08 | CAGR edge rules (P01 l.43-50) | Both endpoints positive; FY20-FY21 losses noted mid-window (01 l.45) | No N/M; no endpoint swing to record; C4 N/M rule not engaged | PASS |
| G09 | A1 median ROCE (P01 l.55) | 8.2% (01 l.28) | Sorted 10 values, (7.4 + 9.0) / 2 = 8.2 (derived); below 10 = 0 | PASS |
| G10 | A2 minimum ROCE (P01 l.56) | -3.6% FY20 (01 l.29) | Below 8 = 0 | PASS |
| G11 | A3 median ROE (P01 l.57) | 5.3% (01 l.30) | (5.0 + 5.6) / 2 = 5.3 (derived); below 12 = 0 | PASS |
| G12 | A4 ROCE trend (P01 l.58-59) | 19.9% vs 16.8% (01 l.31) | 5 on the stated input. 0 under C-G03 (consequence, not counted twice) | PASS (threshold) |
| G13 | B1 CFO / PAT (P01 l.62-63) | 238.24 / 129.47 (01 l.35) | PAT sum re-derived 129.47; 1.84 = 5 | PASS |
| G14 | B2 FCF-positive years (P01 l.64) | 5 of 10 (01 l.36) | 50% = 2 on the stated input. Input construction under C-G06 | PASS (threshold) |
| G15 | B3 FCF / PAT (P01 l.65-66) | 47.51 / 129.47 (01 l.37) | FCF sum re-derived 47.51; 0.37 = 1 on the stated input. Input construction under C-G06 | PASS (threshold) |
| G16 | B4 WC days change (P01 l.67-68) | Earliest-year payables NOT FOUND (01 l.38) | 0. Memo change +42.4 days (derived) also scores 0 | PASS |
| G17 | C1 revenue CAGR (P01 l.71) | 5.6% | 5-9.9 = 1 | PASS |
| G18 | C2 PAT CAGR (P01 l.72) | 12.6% | 10-14.9 = 3 | PASS |
| G19 | C3 positive YoY years (P01 l.73) | 5 of 9 (01 l.43) | 55.6% = 1 | PASS |
| G20 | C4 PAT minus revenue CAGR (P01 l.74) | +7.0pp (01 l.44) | 12.61 - 5.60 = 7.01pp (derived); 5 | PASS |
| G21 | D1 net debt / EBITDA (P01 l.77-79) | Borrowings 32.34, cash 60.07 (01 l.48) | Net cash = 5 | PASS |
| G22 | D2 interest cover (P01 l.80-82) | 63.87 / 3.38 (01 l.49) | 18.9x = 5 | PASS |
| G23 | D3 debt / equity (P01 l.83-84) | 32.34 / 289.07 (01 l.50) | 0.112 = 4 | PASS |
| G24 | D4 current ratio (P01 l.85-86) | 25,832.44 / 15,673.70 lakhs (01 l.51) | 1.65 = 4 | PASS |
| G25 | E1 promoter holding (P01 l.89-90) | 41.33% (01 l.54) | 40-49.9 = 3 | PASS |
| G26 | E2 3-year change (P01 l.91-92) | 41.33% to 41.33% (01 l.55) | Change 0 = 3. Window note O2 | PASS |
| G27 | E3 pledge (P01 l.93) | 0% (01 l.56) | 5 | PASS |
| G28 | E4 contingent liabilities / NW (P01 l.94-95) | 83.54 / 289.07 (01 l.57) | 28.9% = 1 | PASS |
| G29 | M1 pricing power (P01 l.102-104) | Margin -2.3pp; revenue CAGR 5.6% (01 l.62) | 0 on the contextual reading. Plain-text reading gives 1. See O1 | PASS |
| G30 | M2 cost advantage (P01 l.98-100, l.105-106) | PEER DATA NEEDED (01 l.63) | 0 | PASS |
| G31 | M3 capital efficiency (P01 l.107-108) | FAT 2.07x, ROCE 19.9% (01 l.64) | Over 2x and over 15% = 3 on the stated input. ROCE input is open under C-G03 | PASS |
| G32 | M4 stickiness (P01 l.109-111) | 4 decline years (01 l.65) | 3+ = 0 | PASS |
| G33 | M5 scale (P01 l.112-113) | PEER DATA NEEDED (01 l.66) | 0 | PASS |
| G34 | M6 R&D (P01 l.114-116) | 0.13% of revenue (01 l.67) | Below 1% = 0 | PASS |
| G35 | M7 regulatory (P01 l.117-119) | Player count PEER DATA NEEDED (01 l.68) | 0 | PASS |
| G36 | M8 distribution (P01 l.120-122) | "not quantified in inputs" (01 l.69) | See C-G36. 0 or 1 | FAIL MINOR |
| G37 | M9 brand (P01 l.123-125) | PEER DATA NEEDED (01 l.70) | 0 | PASS |
| G38 | M10 switching (P01 l.126-128) | Overall growth, 4 decline years (01 l.71) | 1 | PASS |
| G39 | M11 network (P01 l.129-133) | 24.3% vs 7.1%; selling and admin 8.40% to 5.69%, no years (01 l.72) | See C-G39 | FAIL MINOR |
| G40 | M12 negative WC (P01 l.134-135) | 2 of 10 years known, both over 45 days (01 l.73) | 0 | PASS |
| G41 | Moat present at 3 or more (P01 l.98-99) | M3, M11 (01 l.75) | 2 | PASS |
| G42 | Moat classification (P01 l.137-138) | 2 present | MODERATE | PASS |
| G43 | Block, core, moat, grand arithmetic | A5 B8 C10 D18 E12 (B01 l.18) | Core 53; moat 0+0+3+0+0+0+0+0+0+1+5+0 = 9; grand 62 (derived) | PASS |
| G44 | Classification matrix (P01 l.146-149) | Core 53 | 40-59 = AVERAGE | PASS |
| G45 | DB1 Block A below 8 (P01 l.155) | 5 | Fires; max GOOD; not binding | PASS |
| G46 | DB2 Block B below 8 (P01 l.155) | 8 | Does not fire (exactly at 8) | PASS |
| G47 | DB3 median ROCE below 10% (P01 l.155-156) | 8.2% | Fires; max AVERAGE | PASS |
| G48 | DB4 CFO / PAT below 0.50 (P01 l.156) | 1.84 | Does not fire | PASS |
| G49 | DB5 pledge over 15% (P01 l.156-157) | 0% | Does not fire | PASS |
| G50 | DB6 ND/EBITDA over 3x and IC below 3x (P01 l.157) | Net cash; 18.9x | Does not fire | PASS |
| G51 | DB7 revenue declined in majority (P01 l.157-158) | 4 of 9 | Does not fire | PASS |
| G52 | DB8 PAT negative in last 3 years (P01 l.158-159) | FY24-FY26 positive (01 l.23-25) | Does not fire | PASS |
| G53 | DB9 history below 3 years (P01 l.159) | 10 years | Does not fire | PASS |
| G54 | Deal-breaker driving years stated (P01 l.151-154) | "FY17-FY23" (B01 l.26; 01 l.81) | See C-G54. FY18-FY23 | FAIL MINOR |
| G55 | FLAG-GATE0 at AVERAGE or below with depressors (P01 l.175-177) | Raised (B01 l.14) | Required and present | PASS |
| G56 | PEER DATA NEEDED marked, scored 0 (P01 l.99-100) | M2, M5, M7, M9 (B01 l.35) | Marked and 0 | PASS |
| G57 | data_notes carry proxies, peer items, swings (P01 l.189-190) | B01 l.29-39 | Proxies and peer items present; no endpoint swing exists | PASS |
| G58 | block_b_trend with one number (P01 l.191-192) | B01 l.40 | Present | PASS |
| G59 | analyst_note cap 200 words (P01 l.193-197) | B01 l.41 | About 100 words. Wording point folded into C-G54 | PASS |
| G60 | YAML schema (P01 l.168-198) | B01 l.1-41 | All keys present; model claude-sonnet-5-5 | PASS |
| G61 | Dashboard elements (P01 l.163-165) | Bars 01 l.76; box 01 l.78-81; strongest/weakest 01 l.83; decision line 01 l.86 | Present | PASS |
| G62 | Anchors present on extracted numbers (P01 l.15-18) | Throughout | Present. Fidelity is Verifier A's | PASS |

Gate 0: 62 rules checked, 5 fails, 57 passed.

### Recomputed Gate 0 grid (all rows derived from stated inputs)

| Reading | A | B | C | D | E | Core | Moat | Grand | Class | Deal-breakers that fire |
|---|---|---|---|---|---|---|---|---|---|---|
| Maker (B01 l.18-24) | 5 | 8 | 10 | 18 | 12 | 53 | 9 | 62 | AVERAGE | DB1, DB3 |
| C-G03 strict, C-G06 as stated | 0 | 8 | 10 | 18 | 12 | 48 | 9 | 57 | AVERAGE | DB1; DB3 not testable |
| C-G03 strict, C-G06 strict | 0 | 5 | 10 | 18 | 12 | 45 | 9 | 54 | AVERAGE | DB1, DB2; DB3 not testable |
| C-G03 strict, C-G06 filed-years window | 0 | 12 | 10 | 18 | 12 | 52 | 9 | 61 | AVERAGE | DB1; DB3 not testable |
| C-G03 proxy ruled acceptable, C-G06 filed-years window | 5 | 12 | 10 | 18 | 12 | 57 | 9 | 66 | AVERAGE | DB1, DB3 |

Moat 9 holds in every row, subject to the M3 open check under C-G03 and the M11 check under C-G39. If either fell below 3, moats present = 1 = THIN. Classification stays AVERAGE because the core band governs (P01 l.149).

### Gate 0 findings

**C-G03 (MAJOR). ROCE built on a substituted capital base.**
- Rule: "FORMULA DEFINITIONS (fixed, do not substitute alternatives)" (P01 l.27). ROCE = EBIT / (Total Assets - Current Liabilities). Use the source's figure first, else compute (P01 l.29-31). A missing data point is NOT FOUND and scores 0 (P01 l.19-22).
- What B01 did: current liabilities NOT FOUND FY17-FY24. B01 then computes ROCE on equity + reserves + borrowings (01 l.12; B01 l.30). That is a different denominator, not the formula.
- Internal inconsistency: the same report treats missing payables strictly. B4 is 0 because earliest-year WC days are not computable (01 l.38).
- Recomputed: under the fixed formula, FY17-FY24 ROCE is NOT FOUND. FY25 and FY26 balance sheets sit in the results filing B01 cites (01 l.38, l.51), but two years is below the 3-year minimum (P01 l.23-25). A1 0 and A2 0 stand (already 0). A4 5 becomes 0. Block A 5 becomes 0. Core 53 becomes 48. Grand 62 becomes 57. DB1 still fires. DB3 cannot be tested on a NOT FOUND median.
- Open check: M3 (01 l.64) uses the proxy FY26 ROCE 19.9%. The FY26 formula ROCE needs FY26 total assets from the same filing. B01 does not state it. If M3 fell below 3, moats present = 1 = THIN.
- Alternative reading: the operator rules that the equity + reserves + borrowings convention stands in for "the source's figure" (P01 l.30-31). Then A4 = 5 stands. That is an operator ruling, not a stage-1 choice.
- Decision effect: none. AVERAGE in every reading.

**C-G06 (MAJOR). FCF built on investing cash flow instead of capex.**
- Rule: FCF = CFO - Capex, capex = purchase of PPE + intangibles, acquisitions excluded (P01 l.39-40). Missing data is NOT FOUND (P01 l.19-22).
- What B01 did: capex NOT FOUND FY17-FY23, so net cash from investing stands in (01 l.36; B01 l.32). Investing cash flow carries flows the formula excludes: investment and deposit movements, acquisitions, interest and dividends received.
- Recomputed, reading (i), strict NOT FOUND: B2 0, B3 0, Block B 5. DB2 fires (max GOOD, not binding at AVERAGE).
- Recomputed, reading (ii), the three filed years FY24-FY26 (3-year minimum met, P01 l.23-25): FCF 55.57, 105.06, -29.10 (01 l.36). Positive 2 of 3 = 66.7% = B2 2. Cumulative FCF 131.53 / PAT 102.87 (28.36 + 28.70 + 45.81, 01 l.23-25) = 1.28 = B3 5 (derived). Block B 12.
- The maker's 8 sits between the two readings. The proxy is not a one-way shade: against reading (ii) it understates B3 by 4 points.
- Decision effect: none. Core 45 to 57 across readings, all AVERAGE.

**C-G36 (MINOR). M8 band cannot be re-derived.**
- Rule: "mentioned unquantified = 1 | none or purely digital = 0" (P01 l.121-122).
- B01 evidence: "not quantified in inputs" (01 l.69). It does not say whether distribution is mentioned at all.
- Recomputed: 0 (none) or 1 (mentioned, unquantified). Effect at most 1 point. Below the moat threshold of 3 either way.

**C-G39 (MINOR). M11 selling leg carries no years and a substituted basis.**
- Rule: latest 3-year revenue CAGR above the prior 3-year AND selling expense % declining = 5 (P01 l.129-133).
- B01 states the revenue leg (24.3% vs 7.1%) but gives the selling leg as "8.40 to 5.69" with no years, on selling and admin (01 l.72; B01 l.36).
- Recomputed: 5 holds only if the selling leg falls across the test windows. That cannot be tied to the windows from the stated input. If the leg fails, M11 drops to 1 or 0, moats present = 1, THIN. Classification unchanged (core band).
- Fix: state the two years and the expense basis.

**C-G54 (MINOR). Deal-breaker driving years mislabelled.**
- Rule: "state WHICH years drive any deal-breaker" (P01 l.151-154).
- B01 labels the DB1 and DB3 years "FY17-FY23" (B01 l.26; 01 l.81). FY17 ROCE was 16.8% (01 l.16), not a depressor. The values B01 lists are FY18-FY23.
- B01's own FLAG-GATE0 reason is correct: "Depressors are FY18-FY23" (B01 l.14). The analyst note repeats the wider label: "FY17-FY23 produced median ROCE 8.2%" (B01 l.41). The 8.2% is the FY17-FY26 ten-year median (01 l.28).
- Recomputed: FY18-FY23.
- Why it matters: the downstream post-IPO rebase / legacy cleanup override keys on these years (P01 l.151-154).

## EMERGING MOAT (B07) COMPLIANCE TABLE

| ID | Rule (source) | Evidence in B07 (anchor) | Re-derived | Result |
|---|---|---|---|---|
| E01 | All sections in one response (P07 l.28) | Sections 1-6 plus register (07 l.16-259) | Present | PASS |
| E02 | Section 1: 1A, 1B, 1C (P07 l.48-55) | 07 l.17-43 | Present | PASS |
| E03 | Section 2: 2A-2D (P07 l.57-63) | 07 l.46-64 | Present | PASS |
| E04 | 2C arithmetic shown (P07 l.60-62) | 60 x 2.17 = 130.2; 130.2 / 388.34 (07 l.59) | 33.5% (derived); block 33.5 (B07 l.33) | PASS |
| E05 | Taxonomy on every evidence item (P07 l.29-34) | DOC / CLAIM / INF tags, mapped at 07 l.4 | Present | PASS |
| E06 | Source anchors on evidence items (P07 l.35-36) | Every evidence table | Present. Fidelity is Verifier A's | PASS |
| E07 | All 23 categories addressed or NO EVIDENCE FOUND (P07 l.39-40, l.65-67; rubric rule 3) | 22 categories 07 l.69-147; R1 07 l.178-192 | 23 of 23 | PASS |
| E08 | Summary table, 22 rows, Strong/Moderate count (P07 l.155-157) | 07 l.150-175: 0 Strong, 4 Moderate | Present | PASS |
| E09 | Recount line, exact form, arithmetic (P07 l.157-159) | 07 l.176; B07 l.26 | 4 + 2 + 2 + 3 + 1 = 12 items across 5 categories (derived) | PASS |
| E10 | Completionist guard (P07 l.41-46) | 6 of 23 rows carry points (07 l.175) | Below 12 | PASS |
| E11 | Likelihood x impact matrix values (P07 l.171-172) | A1 MH, B1 ML, B2 HM, E2 MH, H2 HM, R1 MM (07 l.197-202) | 3, 1, 3, 3, 3, 2: all match | PASS |
| E12 | Multipliers consistent with stated evidence tiers (P07 l.172-173; rule 4 P07 l.37-38; rubric rule 3) | H2 factor 1.0 (07 l.201) | See C-E12. H2 2.1, em_score 11.4 | FAIL MAJOR |
| E13 | Scored rows are moats currently forming (P07 l.21-24) | B2 "existing, not new", "already present" (07 l.102) | See C-E13. B2 0, em_score 10.2 | FAIL MAJOR |
| E14 | Scorecard arithmetic (P07 l.173-174) | 07 l.204 | 2.1 + 0.7 + 2.1 + 3.0 + 3.0 + 1.4 = 12.3 (derived) | PASS |
| E15 | Scoring table lists all 23 rows (P07 l.173-174) | 6 rows plus one line for 17 rows (07 l.203) | See C-E15 | FAIL MINOR |
| E16 | Classification band on the stated total (P07 l.175-176) | 12.3 = MODEST (07 l.206) | Correct on the stated total. Consequence of E12/E13 not counted twice | PASS |
| E17 | I1/I2 contribution stated separately (P07 l.180-181) | 0.0 of 12.3 (07 l.205) | Present | PASS |
| E18 | Rubric rule 8: I1 present; above 0 only with both legs, (b) leg DOC (P07 l.122-138) | 0; neither leg evidenced (07 l.146) | 0 correct | PASS |
| E19 | Rubric rule 8: I2 present; above 0 only with a specific named sacrifice (P07 l.139-153) | 0; "nothing identified" (07 l.147) | 0 correct | PASS |
| E20 | Section 4 R1: 4A, 4B, 4C, scored (P07 l.161-168) | 07 l.178-192 | MM 2 x 0.7 = 1.4 (derived) | PASS |
| E21 | Optionality register: columns, scope, carried in block (P07 l.183-196) | 8 rows (07 l.209-218; B07 l.34-42) | Present, matched | PASS |
| E22 | 6A timeline and 6B risks (P07 l.199-201) | 07 l.221-236 | Present | PASS |
| E23 | 6C uses the injected Gate 0 block (P07 l.201-203) | Core 53, 2 moats, 9, MODERATE, AVERAGE (07 l.241-244) | Matches B01 l.18-24 | PASS |
| E24 | 6D combined class; HIGH POTENTIAL and TURNAROUND reasoned (P07 l.203-208) | 07 l.246-247 | Present. Matrix cells are not defined in the rule source, so I checked consistency only | PASS |
| E25 | 6E existing-to-emerging map, attribution (P07 l.208-210) | "Existing (Gate 0)" column (07 l.250-257) | See C-E25 | FAIL MINOR |
| E26 | F2 cross-references the injected promise-delivery record (P07 l.105-107) | B05 grade D (07 l.126) | Present | PASS |
| E27 | YAML schema; active_categories Strong/Moderate only; capex % from 2C (P07 l.216-243) | B07 l.1-51 | All keys present; 4 Moderate rows; 33.5 | PASS |
| E28 | analyst_note cap 200 words (P07 l.239-242) | B07 l.51 | About 100 words | PASS |
| E29 | Not conflated with FTTCP (P07 l.3-6) | 07 l.2 | Stated | PASS |

Emerging Moat: 29 rules checked, 4 fails, 25 passed.

### Recomputed scorecard (derived from the stated row scores)

| Row | Maker (07 l.197-202) | C-E12 only | C-E13 only | Both |
|---|---|---|---|---|
| A1 | 2.1 | 2.1 | 2.1 | 2.1 |
| B1 | 0.7 | 0.7 | 0.7 | 0.7 |
| B2 | 2.1 | 2.1 | 0 | 0 |
| E2 | 3.0 | 3.0 | 3.0 | 3.0 |
| H2 | 3.0 | 2.1 | 3.0 | 2.1 |
| R1 | 1.4 | 1.4 | 1.4 | 1.4 |
| Total | 12.3 | 11.4 | 10.2 | 9.3 |
| Class (P07 l.175-176) | MODEST | NONE | NONE | NONE |

Symmetric bar. One reading raises the score. If the factor rates the documented look-for item instead of the load-bearing claim, H2 keeps 1.0. The same rule then lifts A1 and B2 to 1.0 (3.0 each), and the total is 14.1, MODEST (derived). The maker declared the load-bearing-claim method (07 l.67), not this one. Stage 7 rule 4 (P07 l.37-38) and the completionist guard (P07 l.41-46) favour the load-bearing reading. I grade against the declared method.

### Emerging Moat findings

**C-E12 (MAJOR). H2 scored as documented while its forming advantage is claim only.**
- Rule: multiply the raw score by evidence quality (P07 l.172-173). Be skeptical; hard evidence over promises (P07 l.37-38). Rubric rule 3: a CLAIM-only finding scoring as if DOC is a finding.
- Declared method: evidence quality "of the load-bearing claim" (07 l.67). B07 applies it to A1: DOC capex and orders are present, but the factor is 0.7 on the "only qualified" CLAIM (07 l.78). It applies it to B2: DOC certificates are present, but the factor is 0.7 on the sole-source CLAIM (07 l.102). For H2 it uses 1.0 (07 l.142, l.201).
- What is documented in H2: the investor event, meaning the SPA and paid open offer (07 l.137). Also a JV not yet operating with Rs 4.9 L invested (07 l.138), and existing licensed-in ToT (07 l.139).
- What is forming: the effect of the partnership. That means orders, technology flow and capital. It is CLAIM only (07 l.141, Q1 FY27 call p.6). B07 says so itself: "the investor event is documented; its effect on position is not" (07 l.142), and "H2 documents the investor, not an operating link" (B07 l.16).
- Double use: the same signed event also carries likelihood H: "the investor event is signed and cash is paid ... so H2 stays at H" (07 l.206). One document is credited in the factor and again in the likelihood.
- The "most evidenced path" wording is the A26.3 projection rule. CLAUDE.md scopes A26.3 to Role 1 projections. Conservative reading of filed evidence stays in force for document-reading stages. Stage 7 rule 4 governs here.
- Recomputed: factor 0.7 gives H2 2.1 and em_score 11.4. Likelihood M (the maker's own sensitivity, 07 l.206) gives H2 2.0 and em_score 11.3. Both are NONE.
- Separating observation (B07's own, 07 l.142): a named Apollo-linked order, or a filed related-party term after close.
- Decision effect: em_classification goes from MODEST to NONE. Combined assessment AVERAGE (07 l.246) is unchanged. The UA qualifier EM 25 or more fails in both readings. Pillar 3 consumes the EM score in phase 3, so it must be re-checked there.

**C-E13 (MAJOR). B2 is scored as emerging while B07 describes it as existing.**
- Rule: the scan identifies moats "currently FORMING that do not fully show in historical financials yet" (P07 l.21-24).
- B07 on B2: "the row is existing, not new"; time to materialise "already present" (07 l.102; B07 l.51).
- Every B2 evidence item is long-standing: AS9100D and other certificates (07 l.97), DSIR/NABL labs (07 l.98), programme spec-in on MRSAM, LRSAM, Astra and Agni (07 l.99-100). B07 cites no new qualification, design-in or multi-year agreement inside the scan window. Those are the B2 look-for items (P07 l.80-82).
- B07 keeps the row "because the scorecard asks what is forming into margin" (07 l.102). Margin is not a B2 look-for item. The margin claim is itself CLAIM: FY26 EBITDA 10.0% against a 15-20% guide (07 l.41).
- Recomputed: B2 0, em_score 10.2, NONE. With C-E12: 9.3, NONE.
- Alternative reading: B2 counts as forming because Gate 0 did not confirm a switching-cost moat (M10 = 1, 01 l.71), so the lock-in does not show in historical financials. Under that reading 2.1 stands.
- Separating observation: a B2 item dated inside the scan window (new qualification, design-in or multi-year agreement), or EBITDA margin at the 15% floor of the guide, which would show the lock-in carrying price.
- Presentation: the KNIFE-EDGE flag (B07 l.13) names H2 as the only swing row. B2 is a second one.
- Decision effect: same as C-E12.

**C-E15 (MINOR). Scoring table does not list all 23 rows.**
- Rule: "Full scoring table, all 23 rows, adjusted total" (P07 l.173-174).
- B07 rolls 17 zero rows into one line (07 l.203). The summary table (07 l.150-173) names all 22 categories, so the zero rows can be identified. Total unchanged.

**C-E25 (MINOR). 6E "Existing (Gate 0)" column does not match the injected Gate 0 block.**
- Rule: 6C and 6E combine with the INJECTED Gate 0 block (P07 l.201-203, l.208-210).
- The 6E column labelled "Existing (Gate 0)" (07 l.250) lists technology qualification (07 l.252), switching costs (07 l.253) and licence/regulatory (07 l.255).
- B01 confirms only M3 capital efficiency and M11 (scored mechanically) as present (01 l.75). M6 = 0, M7 = 0 PEER DATA NEEDED and M10 = 1 (01 l.67, l.68, l.71). The 6E entries come from B04 (07 l.102), not Gate 0.
- Fix: relabel the column to its B04 source, or carry the B01 moats. No score effect.

## OBSERVATIONS (not counted as fails)

- O1. M1 band wording (P01 l.102-104). "margin declined 2-5pp despite growth = 1" has no growth threshold. The plain reading gives M1 = 1 (margin -2.3pp, revenue CAGR +5.6%, 01 l.62). The contextual reading (growth = the 10% of the bands above) gives 0. The plain reading creates a perverse order: a stable margin at 5.6% growth scores 0, and a falling margin at 5.6% growth scores 1. I accept the maker's 0. Prompt fix for the operator: add the threshold. If 1: moat 10, grand 63, count and class unchanged.
- O2. E2 window. B01 uses Mar 2023 to Sep 2026, which is 42 months (01 l.55). The 3-year window (Sep 2023 to Sep 2026) sits inside it, and the holding is flat at 41.33%. E2 = 3 stands.
- O3. B01 report carries an orchestrator erratum (01 l.88-89) that corrects a garbled fragment. It is labelled, and the block is unaffected.
- O4. The export rocket motor orders (Rs 17.68 Cr and Rs 33.69 Cr) appear as A1 evidence (07 l.74) and inside E2's four orders (07 l.118). A1 is scored at 0.7 on the CLAIM, and the recount counts the orders once, under E2 (07 l.176). No score effect.
- O5. E2 tags a government sector statistic (defence exports Rs 38,424 Cr) as DOC (07 l.120). The P07 DOC list is company-specific (P07 l.30-32). The item is not in the E2 recount. No score effect.
- O6. Prompt defect. prompts/12-verifiers-pipeline.md l.379 holds the audit's instruction text "(same line, comment ...)" in place of the YAML key. I reconstructed the key from audits/PROMPT_AUDIT_2026-10.md l.1962 (business_understanding_narrative) with the rule 9 comment from l.1964. Operator fix needed.
- O7. Number and basis items for Verifier A or the orchestrator. I give no verdict on these. B01 M3 uses fixed assets Rs 187.33 Cr (01 l.64), and B07 2C uses net block Rs 179.07 Cr (07 l.58). B07 G1 uses standalone CFO Rs -1.44 Cr and net cash Rs 23.15 Cr (07 l.129). B01 is consolidated: CFO Rs -1.27 Cr (01 l.6), and cash 60.07 less borrowings 32.34 = 27.73 Cr (01 l.48, derived).

## PHASE 3 CARRY-FORWARD

- Pillar 3 and any EM-dependent input in B11 must cite the em_score reading that survives remediation or an operator ruling: 12.3 MODEST (maker) against 9.3-11.4 NONE (C-E12, C-E13).
- Any B11 use of the Gate 0 ROCE history or core score carries the C-G03 and C-G06 outcome.
- The Verifier C phase 3 run audits B10 and B11 (rubric rules 4, 5, 7, 11-15) against the valuation framework documents.

## VALUATION (B11): PENDING PHASE 3

Not run. B10 and B11 do not exist yet. The expectation_ledger and business_understanding_narrative entries in the block are template defaults. They are not evaluated and are not findings.

```yaml
stage: B12c
company: "PREMEXPLN"
run_date: "2026-11-15"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete
gate0: {rules_checked: 62, fails: ["C-G03", "C-G06", "C-G36", "C-G39", "C-G54"]}
emoat: {rules_checked: 29, fails: ["C-E12", "C-E13", "C-E15", "C-E25"]}
valuation: {rules_checked: 0, fails: []}  # PENDING PHASE 3: B10/B11 not yet produced; audit deferred
expectation_ledger: {present: false, downside_row: false, all_rows_confirm_by: false, all_rows_metric_threshold: false, prob_in_range: false, decay_status_valid: false, off_ledger_credit: false, residual_pct_cmp: 0, residual_starter_cap_ok: true, fails: []}  # rules 13-14; any fail = REWORK stage 11. NOT EVALUATED in phase 1: template defaults, not findings
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: []}  # rule 9; any fail = REWORK stage 13. NOT EVALUATED: stage 13 not yet run; template defaults, not findings
recomputed_destination_pe: ""  # phase 1: no B11
recomputed_decision: ""        # phase 1: no decision to recompute
findings:
  - {id: "C-G03", stage: "B01", rule: "P01 l.27-31 fixed ROCE formula; P01 l.19-22 NOT FOUND scores 0", severity: "MAJOR", claimed: "ROCE on proxy capital employed (equity + reserves + borrowings); A4 5, Block A 5, core 53 (01 l.12, l.31)", recomputed: "Current liabilities NOT FOUND FY17-FY24, so ROCE NOT FOUND: A4 0, Block A 0, core 48, grand 57; DB1 fires, DB3 not testable; M3 ROCE input open. Operator may rule the proxy acceptable, then A4 5 stands", decision_effect: "none; AVERAGE in every reading"}
  - {id: "C-G06", stage: "B01", rule: "P01 l.39-40 FCF = CFO - capex (PPE + intangibles); P01 l.19-22", severity: "MAJOR", claimed: "Investing cash flow as capex proxy FY17-FY23; B2 2, B3 1, Block B 8 (01 l.36-37)", recomputed: "Strict NOT FOUND: B2 0, B3 0, Block B 5, DB2 fires (not binding). Filed years FY24-FY26: B2 2 (2 of 3), B3 5 (131.53 / 102.87 = 1.28), Block B 12", decision_effect: "none; core 45-57 across readings, all AVERAGE"}
  - {id: "C-G36", stage: "B01", rule: "P01 l.120-122 M8 bands", severity: "MINOR", claimed: "M8 0, evidence 'not quantified in inputs' (01 l.69)", recomputed: "0 (none) or 1 (mentioned, unquantified); stated input does not separate the bands", decision_effect: "none; below moat threshold either way"}
  - {id: "C-G39", stage: "B01", rule: "P01 l.129-133 M11 selling leg", severity: "MINOR", claimed: "M11 5; selling and admin 8.40% to 5.69%, no years (01 l.72)", recomputed: "5 holds only if the selling leg falls across the test windows; years and basis not stated. If it fails, M11 1 or 0, moats present 1, THIN", decision_effect: "none; core band governs classification"}
  - {id: "C-G54", stage: "B01", rule: "P01 l.151-154 state which years drive a deal-breaker", severity: "MINOR", claimed: "DB1/DB3 driving years FY17-FY23 (B01 l.26; 01 l.81; B01 l.41)", recomputed: "FY18-FY23; FY17 ROCE 16.8% (01 l.16) is not a depressor; B01 l.14 already says FY18-FY23", decision_effect: "none; the years feed the post-IPO rebase / legacy cleanup override"}
  - {id: "C-E12", stage: "B07", rule: "P07 l.172-173 evidence multiplier; P07 l.37-38 rule 4; rubric rule 3", severity: "MAJOR", claimed: "H2 H x M = 3 x 1.0 = 3.0; em_score 12.3 MODEST (07 l.142, l.201, l.204)", recomputed: "Forming advantage (orders, technology, capital) is CLAIM only (07 l.141-142): factor 0.7 gives H2 2.1, em_score 11.4; likelihood M gives 2.0, em_score 11.3. Class NONE", decision_effect: "em_classification MODEST to NONE; combined AVERAGE unchanged; Pillar 3 re-check in phase 3"}
  - {id: "C-E13", stage: "B07", rule: "P07 l.21-24 moats currently forming", severity: "MAJOR", claimed: "B2 scored 2.1 while described as existing, not new, already present (07 l.102; B07 l.51)", recomputed: "B2 0, em_score 10.2 NONE; with C-E12, 9.3 NONE. Alternative reading (lock-in not in historical financials, M10 = 1) keeps 2.1", decision_effect: "em_classification MODEST to NONE; combined AVERAGE unchanged; KNIFE-EDGE flag (B07 l.13) omits B2 as a swing row"}
  - {id: "C-E15", stage: "B07", rule: "P07 l.173-174 full scoring table, all 23 rows", severity: "MINOR", claimed: "Scorecard lists 6 rows plus one line for 17 zero rows (07 l.203)", recomputed: "List all 23 rows; total unchanged", decision_effect: "none"}
  - {id: "C-E25", stage: "B07", rule: "P07 l.201-203, l.208-210 combine with the injected Gate 0 block", severity: "MINOR", claimed: "6E column 'Existing (Gate 0)' lists technology qualification, switching costs, licence/regulatory (07 l.250-255)", recomputed: "B01 confirms M3 and M11 only (01 l.75); M6 0, M7 0, M10 1. Relabel to the B04 source or carry the B01 moats", decision_effect: "none"}
critical_count: 0
major_count: 4
minor_count: 5
acceptance_rate: 90.1             # rules passed / rules checked, % (82 / 91)
```
