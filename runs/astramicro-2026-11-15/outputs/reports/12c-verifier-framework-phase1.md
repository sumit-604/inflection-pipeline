# VERIFIER C: FRAMEWORK ADHERENCE, PHASE 1 (ASTRAMICRO, run 2026-11-15)

Stage: B12c, phase-1 half. Model: claude-opus-5-5. Audit date: 2026-11-16.

Scope. This audit covers Gate 0 (B01) and the Emerging Moat scan (B07) only. The valuation audit (B10, B11; rules 4-7 and 11-15) runs in phase 3. Rule 9 (stage 13 narrative) and rule 10 (B09b dossier) are outside this scope. I did not load the Master prompt, the Section 1B layers or FTTCP.

Rule sources read: prompts/12-verifiers-pipeline.md (Verifier C section, l.213-390), prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md.

Artifacts audited: outputs/reports/01-gate0.md, outputs/blocks/B01-gate0.yaml, outputs/reports/07-emoat.md (its ERRATA at l.603-607 govern over the text above them), outputs/blocks/B07-emoat.yaml.

What this audit judges: rule application. Whether a number is in its source is Verifier A's question (P12 l.22-33). I re-derive each score from the inputs the stage states.

Anchor key:
- "P01 l.N" = prompts/01-gate-0-pipeline.md, line N.
- "P07 l.N" = prompts/07-emerging-moat-pipeline.md, line N.
- "P12 l.N" = prompts/12-verifiers-pipeline.md, line N.
- "B01 l.N" = outputs/reports/01-gate0.md, line N. "B01y l.N" = outputs/blocks/B01-gate0.yaml, line N.
- "B07 l.N" = outputs/reports/07-emoat.md, line N. "B07y l.N" = outputs/blocks/B07-emoat.yaml, line N.
- "calc" = my arithmetic on the cited inputs.
- Evidence classes: [DOC] documented, [CLAIM] management claim, [INFER] analyst inference (the stage's mapping, B07 l.8).

## RESULT

| Framework | Rules checked | PASS | FAIL | CRITICAL | MAJOR | MINOR |
| --- | --- | --- | --- | --- | --- | --- |
| Gate 0 (B01) | 21 | 20 | 1 | 0 | 0 | 1 |
| Emerging Moat (B07) | 25 | 20 | 5 | 0 | 1 | 4 |
| Valuation (B11) | pending phase 3 | - | - | - | - | - |
| Total | 46 | 40 | 6 | 0 | 1 | 5 |

Acceptance rate: 40 / 46 = 87.0% (calc). The denominator is 4 or more, so the rate applies. It is above 60%. This report gives no REWORK trigger.

- Gate 0. Every block score reproduces from the stated inputs: A 16, B 0, C 12, D 17, E 8, core 53, moat 15, grand total 68 (B01y l.20-23). Classification AVERAGE concurs. One MINOR finding: the stage applied a 3-year floor per metric to Block B but not to M6.
- Emerging Moat. The arithmetic on the stated scores reproduces 16.5 (B07 l.438). The MAJOR finding: three categories scored 0 although each tables evidence that matches an indicator its rubric lists. The matrix floor for any evidence is 1. Recomputed score: 19.2. The band stays MODEST MOAT DEVELOPMENT. The four MINOR findings cover labels, register carry, I2 reasoning and a 2C basis note.
- Decision concurrence. Gate 0 AVERAGE, EM MODEST, combined AVERAGE. No change.

## PART 1: GATE 0 (B01)

### 1A. Compliance table

| ID | Rule (source) | B01 application (anchor) | Re-derived | Result |
| --- | --- | --- | --- | --- |
| G01 | Opening data line (P01 l.23-25) | "Data available: 10 years (FY17 to FY26). Scoring adapted to 10-year history." (B01 l.3) | present | PASS |
| G02 | Anchor after every extracted number (P01 l.15-18) | sd, Q4, Q2, AR, SH anchors on inputs (key at B01 l.8) | anchors present; fidelity is Verifier A's | PASS |
| G03 | NOT FOUND scores 0, no estimates (P01 l.19-22) | B2, B3, B4 (B01 l.54-56), E2 (B01 l.96), M7 (B01 l.112) scored 0 as NOT FOUND | no gap filled | PASS |
| G04 | Formula definitions (P01 l.29-41) | ROCE: source figure (AR p.11) used, computed cross-check labelled "computed" (B01 l.29-35). ROE: average net worth, FY17 closing stated (B01 l.41, l.44). WC days: revenue basis stated (B01 l.62). FCF capex = PPE + intangibles (B01 l.59). CAGR formula (B01 l.72-73) | all as defined | PASS |
| G05 | CAGR edge rules (P01 l.45-50) | No negative endpoint, no loss year, "No loss-to-profit swing in window" (B01 l.77; B01y l.43) | none triggered, correctly | PASS |
| G06 | Block A (P01 l.55-58) | 4 / 5 / 2 / 5 = 16 (B01 l.39-42) | A1 median (19.34 + 22.78) / 2 = 21.06% -> 4. A2 18.52% -> 5. A3 median of ten ROE values 12.085% -> 2. A4 +4.42pp -> 5. Total 16 | PASS |
| G07 | Block B (P01 l.62-68) | 0 / 0 / 0 / 0 = 0 (B01 l.53-56) | B1 367.07 / 776.57 = 0.473 -> 0. B2-B4 NOT FOUND -> 0 | PASS |
| G08 | Block C (P01 l.71-74) | 3 / 3 / 3 / 3 = 12 (B01 l.72-75) | C1 (1,162.80 / 389.79)^(1/9) - 1 = 12.91% -> 3. C2 (192.97 / 57.58)^(1/9) - 1 = 14.38% -> 3. C3 7 of 9 = 77.8% -> 3. C4 +1.47pp -> 3 | PASS |
| G09 | Block D (P01 l.77-86) | 4 / 4 / 4 / 5 = 17 (B01 l.83-86) | D1 34.81 / 334.17 = 0.104x -> 4. D2 316.73 / 55.97 = 5.66x -> 4. D3 287.66 / 1,314.57 = 0.219 -> 4. D4 162,051.47 / 51,828.93 = 3.13 -> 5. Sep-26 cross-check gives the same bands: 0.77x, 6.69x, 0.36, 2.55 (B01 l.88) | PASS |
| G10 | Block E (P01 l.89-95) | 0 / 0 / 5 / 3 = 8 (B01 l.95-98) | E1 6.54% (<30) -> 0. FII + DII 27.00% is not above 50%, so the professionally-managed 3 does not apply. E2 NOT FOUND -> 0. E3 0% -> 5. E4 8,184.86 / 131,457.12 = 6.23% -> 3 | PASS |
| G11 | Block F tests on stated inputs (P01 l.98-135) | 15 (B01 l.106-117) | M1 +2.20pp with 12.9% CAGR -> 5. M3 4.35x with 22.94% -> 5. M4 two decline years -> 1. M6 tier 2 -> 3. M10 -> 1. M11 latest 3-yr 12.55% below prior 20.40%, selling % rising -> 0. M12 above 45 days -> 0. M2, M5, M7, M8, M9 -> 0. Total 15 | PASS |
| G12 | PEER DATA NEEDED (P01 l.99-100) | M2, M5, M9 scored 0 and marked (B01 l.107, l.110, l.114; B01y l.39) | as written | PASS |
| G13 | Moat class (P01 l.137-138) | M1, M3, M6 present -> MODERATE (B01 l.119) | 3 present -> MODERATE | PASS |
| G14 | One window treatment across metrics (P01 l.19-25; P12 l.237-238) | B2-B4 refused on a 2-year window as "window under 3 years" (B01 l.58). M6 scored 3 on a 2-year window, FY25-FY26 (B01 l.111; B01y l.40) | see finding C-P1-06 | FAIL (MINOR) |
| G15 | Data confidence (P01 l.142-144) | 10 years = full, no downgrade (B01 l.127; B01y l.30) | 10 -> full | PASS |
| G16 | Classification matrix (P01 l.147-149) | Core 53 -> AVERAGE (B01 l.126) | 40-59 -> AVERAGE | PASS |
| G17 | Deal-breakers 1-9 (P01 l.155-159) | DB2 and DB4 fire; DB1, DB3, DB5-DB9 do not (B01 l.130-132) | DB2: Block B 0 is below 8. DB4: 0.47 is below 0.50. DB6: 0.10x is not above 3x. DB7: 2 of 9 decline years. DB8: FY24-FY26 PAT positive. Cap = AVERAGE | PASS |
| G18 | Name the years that drive a deal-breaker (P01 l.151-154) | DB4: FY23 -25.47, FY24 -181.52, FY25 -90.15 Cr CFO (B01 l.131). DB2: B1 plus NOT FOUND FY17-FY24 capex and payables (B01y l.28) | named | PASS |
| G19 | FLAG-GATE0 when AVERAGE or below with depressors (P01 l.175-177) | raised (B01y l.16) | required and present | PASS |
| G20 | Block arithmetic matches report | core 16 + 0 + 12 + 17 + 8 = 53; grand total 53 + 15 = 68; moats_confirmed 3 (B01y l.20-26) | matches B01 l.124-125 | PASS |
| G21 | Block schema; analyst_note at most 200 words (P01 l.168-198) | all template fields present; note about 100 words (B01y l.45) | within cap | PASS |

### 1B. Re-derivation notes

- ROE. The ten values are 1.95, 5.25, 6.62, 8.47, 11.37, 12.80, 12.85, 14.87, 15.05, 15.99% (B01 l.44). I re-checked each average net worth denominator from B01 l.14-23. All ten match. Median (11.37 + 12.80) / 2 = 12.085% (calc). Band 12-14.9 -> 2.
- Cumulative CFO. The ten values at B01 l.48 sum to 367.07 (calc). Cumulative PAT at B01 l.14-23 sums to 776.57 (calc).
- M11. Latest 3-year CAGR (1,162.80 / 815.52)^(1/3) - 1 = 12.55%. Prior 3-year (815.52 / 467.22)^(1/3) - 1 = 20.40% (calc). Latest is lower, so tier 1 fails. Tiers 2 and 3 fail because growth is below 15%. Score 0.
- M6. Tier 1 also fails on revenue CAGR (12.9%, below 15%). B01 l.111 cites only the R&D leg. The score does not change.
- ROCE cross-check. FY26: 316.73 / (1,987.96 - 518.29) = 21.55%. FY25: 261.22 / (1,851.22 - 644.49) = 21.65% (calc, inputs at B01 l.32-33). Both sit in the same A1 band as the source figures.

### 1C. Observations (no fail)

1. ROCE window. A1, A2, A4 and DB3 run on FY23-FY26 only (B01 l.29; B01y l.33). FY17-FY22 ROCE is NOT FOUND. That gap includes FY19-FY22, when ROE ran 1.95% to 8.47% (B01 l.44). The rules allow "whatever history is available" (P01 l.23). Four years meets the stage's own 3-year floor. B01 discloses it (B01 l.127). Read A2 = 5 as a statement about FY23-FY26, not about the 10-year record. A DB3 trigger would cap at AVERAGE, which is already the classification.
2. M1 margin. The endpoint change of +2.20pp clears the 2pp line by 0.20pp (B01 l.106). The path is not monotone: 31.36% in FY18, 10.43% in FY19 (B01 l.15-16). P01 l.102 names no window. Endpoints match the "latest vs earliest" convention of A4 and B4. B01y l.41 discloses it.
3. Robustness line. B01 l.134 does not say that DB2 stops firing when Block B reaches 8. DB4 still binds, so the AVERAGE claim holds.

## PART 2: EMERGING MOAT (B07)

### 2A. Compliance table

| ID | Rule (source) | B07 application (anchor) | Re-derived | Result |
| --- | --- | --- | --- | --- |
| E01 | Six sections plus optionality register (P07 l.28, l.48-210) | Sections 1-6 and the register present (B07 l.56-537) | present | PASS |
| E02 | 22 categories, each with an evidence table or NO EVIDENCE FOUND (P07 l.65-67; P12 l.241-242) | A1 to I2 all addressed (B07 l.148-340) | 22 of 22 | PASS |
| E03 | R1 (P07 l.161-168) | 4A, 4B, 4C present (B07 l.377-405) | present | PASS |
| E04 | Evidence class and anchor on every item (P07 l.29-36) | [DOC] / [CLAIM] / [INFER] mapped to the three classes (B07 l.8); every Section 3 item anchored | present | PASS |
| E05 | Section 3 summary, 22 rows, Strong/Moderate count (P07 l.155-157) | B07 l.344-369 | 22 rows; count stated | PASS |
| E06 | Section 5 table, 23 rows, adjusted total (P07 l.171-174) | B07 l.413-438 | 23 rows | PASS |
| E07 | Matrix values (P07 l.171-172) | HH 4; HM/MH 3; HL/MM/LH 2; ML/LM/LL 1; none 0 (B07 l.411) | as written | PASS |
| E08 | Zero only where no evidence exists; any evidence scores at least LL = 1 (P07 l.171-172) | A3, A4, G2 scored 0 with evidence tabled (B07 l.171-187, l.288-297) | see finding C-P1-01 | FAIL (MAJOR) |
| E09 | Multiplier arithmetic (P07 l.172-173) | ten non-zero rows (B07 l.415-437) | 1.4 + 0.5 + 1.5 + 3.0 + 2.0 + 1.0 + 1.0 + 1.0 + 3.0 + 2.1 = 16.5 (calc) | PASS |
| E10 | No claim-only category scored as documented (P12 l.243-244) | DOC rows B2, C1, F1, F2, G1, H2 each rest on a [DOC] item; A1 and R1 at 0.7; A2 and B1 at 0.5 (B07 l.415-437) | no inflation found | PASS |
| E11 | Documented-item recount line and count (P07 l.157-159; P12 l.242-243) | "recount performed: 27 documented items across 15 categories" (B07 l.371) | 27 [DOC] items in 15 categories reproduce from the Section 3 tables (calc) | PASS |
| E12 | Guard check at 12 (P07 l.41-46) | 10 non-zero categories, below 12 (B07 l.369, l.371) | holds on the stage's scores; see the C-P1-01 knock-on | PASS |
| E13 | Band from the total (P07 l.175-176) | 16.5 -> MODEST (B07 l.441; B07y l.22-23) | 12-24 -> MODEST | PASS |
| E14 | I1/I2 contribution stated (P07 l.180-181) | "of which I1 + I2: 0.0" (B07 l.439) | stated | PASS |
| E15 | Category 21 present; above 0 only with both legs and a [DOC] source on leg (b) (P07 l.122-138; P12 l.292-295) | leg (a) only (I1-1 [DOC]); leg (b) NO EVIDENCE FOUND -> 0 (B07 l.326-332) | 0 | PASS |
| E16 | Category 22 present; above 0 only with a specific named sacrifice (P07 l.139-153; P12 l.295-297) | none named -> 0 (B07 l.334-340) | 0 | PASS |
| E17 | I2 answered per moat, both directions tested (P07 l.140-148) | one collective answer; relationships called "execution leads" (B07 l.340) | see finding C-P1-02 | FAIL (MINOR) |
| E18 | "NO EVIDENCE FOUND" used only when none exists (P07 l.39-40) | D1, E2, H1 carry that heading and also table items (B07 l.239, l.245-250, l.301) | see finding C-P1-03 | FAIL (MINOR) |
| E19 | One improvement, one mechanism (CLAUDE.md NEVER list; stage rule at B07 l.52) | Uttam in B2 only; gross margin in B1 only; ARC in H2; policy in R1 (B07 l.52, l.177, l.228, l.301) | no point counted twice; see observation 3 | PASS |
| E20 | 2C formula with arithmetic shown (P07 l.60-62) | Rs 51 Cr x 4.51 = Rs 230 Cr = 19.9% of Rs 1,155.67 Cr (B07 l.131-132) | 51 x 4.51 = 230.0; 230.0 / 1,155.67 = 19.9% (calc) | PASS |
| E21 | Block field carries a basis the report supports | capex_embedded_growth_pct 19.9 (B07y l.40), while B07 l.132 calls Rs 27 Cr of it "not capacity" | see finding C-P1-04 | FAIL (MINOR) |
| E22 | Register lists every advantage that scored 0 or rests only on claim or inference evidence, and the block carries it (P07 l.183-196) | 13 rows in the report (B07 l.458-470), 10 in the block (B07y l.42-51); no R1 or B1 row | see finding C-P1-05 | FAIL (MINOR) |
| E23 | 6C uses the injected B01 block (P07 l.202-203) | core 53, moat 15 MODERATE, AVERAGE, DB2 and DB4 (B07 l.499-503) | matches B01y l.20-29 | PASS |
| E24 | 6D label from the set, with full reasoning on HIGH POTENTIAL and TURNAROUND (P07 l.203-208) | AVERAGE; both rows reasoned out (B07 l.507-514) | label in the set; mapping not re-derivable, see gap 3 | PASS |
| E25 | Block schema; analyst_note at most 200 words (P07 l.216-243) | all template fields present; note about 150 words (B07y l.60) | within cap | PASS |

### 2B. Re-score for finding C-P1-01

| Category | Tabled evidence that matches a listed indicator | Indicator in the rubric | B07 score | Floor as written |
| --- | --- | --- | --- | --- |
| A3 Process innovation | A3-1 [DOC]: laser welding, automatic wire bonding and test chambers added (B07 l.175) | "automation" (P07 l.73) | 0 (B07 l.417) | LL = 1 x 1.0 = 1.0 |
| A4 Platform / modular architecture | A4-2 [CLAIM]: counter-UAV structure "modular" (B07 l.184); A4-1 [CLAIM]: radar family in final stages (B07 l.183) | "shared architecture language" (P07 l.75) | 0 (B07 l.418) | LL = 1 x 0.7 = 0.7 |
| G2 WC improvement trajectory | G2-1 [DOC]: cash conversion cycle 459 to 374 days, debtor days 273 to 216, FY25 to FY26 (B07 l.292) | "WC days declining" (P07 l.111) | 0 (B07 l.431) | LL = 1 x 1.0 = 1.0 |
| Adjusted total | | | 16.5 (B07 l.438) | 19.2 (calc) |

The reversal evidence (G2-2, B07 l.293) and the lack of yield data (B07 l.177) belong on the likelihood axis. They lower L. They do not turn evidence into no evidence. The stage scores comparable weak evidence at the floor elsewhere. F1 scores ML = 1.0 (B07 l.428) although the stage calls the postgraduate share "not unusual" (B07 l.264). G1 scores ML = 1.0 (B07 l.430) although "the net cash while investing test fails" (B07 l.278).

Knock-ons at 19.2:
- Band: MODEST, unchanged (12-24, P07 l.175-176). active_categories do not change. A3 1.0, A4 0.7 and G2 1.0 are all Weak on the stage's own bands (B07 l.11).
- Downside case. "B2 and H2 both fail" gives 13.2, not 10.5 (calc; stage figure at B07 l.447). The claim that the band is "fragile on the downside" (B07y l.60) no longer holds. The gap to STRENGTHENING is 5.8 points, not 8.5 (calc).
- Guard. Non-zero categories become 13. The stage reads "active" as non-zero (B07 l.369), so 13 sits at or above the guard line of 12. The guard then asks for the documented-item recount. The recount at B07 l.371 already counts A3-1 and G2-1, so no new item appears. On the block's reading (active = Strong/Moderate, P07 l.227), the count stays 4.
- Range. The stage tiers A2 and B1 by their weakest link, [INFER] (B07 l.166, l.198). If A3 is tiered the same way, the total is 18.7 (calc). If D1 and E2 were also scored at LL x 0.7, the total would be 20.6 (calc). I do not support that second step (see C-P1-03). Every point in the range is MODEST.

### 2C. Observations (no fail)

1. Strength bands. The cut-offs are the stage's own (B07 l.11; ERRATA 3 at B07 l.607). P07 l.157 names Strong, Moderate, Weak and None but sets no cut-offs. The stage discloses this. The cut-offs decide active_categories, which later stages consume. See gap 2.
2. Evidence mix. The stage labels "24 claims" as "across all Section 3 tables" (B07 l.371). The Section 3 tables hold 21 claim items. The other 3 are R1-1 to R1-3 in Section 4 (B07 l.404). The count is right for the whole scan. The label is loose. The 27 documented and 5 inference counts reproduce (calc).
3. Uttam and ARC also appear in F2-1 as delivered promises (B07 l.270), in addition to B2 and H2. F2 credits guidance credibility from the injected promise record, and P07 l.106-107 requires that cross-reference. F2 scores ML = 1.0 on a record of 5 delivered, 3 partial and 3 missed. Those two items do not drive the score. No point is counted twice. The stage's double-credit line (B07 l.52) names A1, C1 and C2, not F2.
4. Tiering of A2 and B1. Both are tiered [INFER] although each holds [DOC] items (A2-1, A2-2, B1-1). The documented items show spend and a cost-ratio fall. The moat link (IP; integration as the cause) is inferred. That is a conservative reading of filed evidence, which the document protocols allow. See gap 5.

## FINDINGS

### C-P1-01. MAJOR. Emerging Moat, E08 matrix floor.
- Rule: "HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, no evidence=0" (P07 l.171-172). A score of 0 is for no evidence only.
- Claimed: A3 0, A4 0, G2 0; em_score 16.5 (B07 l.417, l.418, l.431, l.438; B07y l.22).
- Recomputed: A3 1.0, A4 0.7, G2 1.0; em_score 19.2 (range 18.7 to 19.2). Table 2B shows the evidence and the indicators.
- Cause: each of the three categories tables an item that matches an indicator in its own rubric. The stage used headings the rubric does not provide for: "no moat-grade effect" (B07 l.171), "no SKU or launch cadence" (B07 l.179), "no current improving trend" (B07 l.288).
- Decision impact: band MODEST unchanged. The "EM >= 25" UA qualifier fails at either score. active_categories unchanged. The downside-fragility statement in the analyst_note fails (13.2, not 10.5).
- Fix: stage 7 restates A3, A4 and G2 at the floor. The other route is an operator ruling that lets a category score 0 with evidence present, with the test named.

### C-P1-02. MINOR. Emerging Moat, E17 I2 reasoning.
- Rule: "For each moat claimed anywhere in this scan, answer" (P07 l.140-141). "Two directions both count: private players protected by PSU internal rigidities; incumbents protected by decades-old institutional customer relationships no capex can shortcut" (P07 l.144-148).
- Claimed: one answer covers every moat. "Qualification time and relationships, which are execution leads" (B07 l.340).
- Recomputed: I2 = 0, unchanged. Rule 8 needs a specific named sacrifice for a score above 0 (P12 l.295-297), and the stage names none. The BEL L2 bid (I2-1, B07 l.338) is evidence against the first direction.
- Gap: the rubric counts institutional relationships as a direction. The report calls them execution leads. It does not test the second direction for each moat (B2, C1, H2) against the government customer tier framework that P07 l.147-148 cites.

### C-P1-03. MINOR. Emerging Moat, E18 labels.
- Claimed: D1 is headed "NO EVIDENCE FOUND" but tables D1-1 [CLAIM] (B07 l.239). E2 is headed the same but tables E2-1 [CLAIM] and E2-2 [DOC] (B07 l.245-250). H1 is headed the same but tables H1-1 [CLAIM] (B07 l.301).
- Recomputed: 0 for each, unchanged. No tabled item matches a listed indicator. D1 needs an accumulated data asset (P07 l.93-94); D1-1 is a concept that leaves with the demerger. E2 needs wins, certifications, export capex or supply-chain-shift language (P07 l.99-101); E2-1 gives leads only, and E2-2 is adverse. H1-1 is credited once, in R1.
- Fix: head each one "evidence reviewed; no item matches the category indicators", or "credited in R1".

### C-P1-04. MINOR. Emerging Moat, E21 capex basis in the block.
- Claimed: capex_embedded_growth_pct 19.9 (B07y l.40). The input is CWIP Rs 24 Cr plus intangible assets under development Rs 27 Cr, times 4.51x (B07 l.131-132).
- Recomputed: 19.9% follows the literal "total capex under execution" (P07 l.60-61), so E20 passes. But 4.51x is revenue over net PPE (B07 l.120-128), and B07 l.132 says the Rs 27 Cr is "development spend, not capacity". The plant-only figure is 9.4% (24 x 4.51 = Rs 108 Cr; calc).
- Fix: the block carries both figures, 9.4% plant-only and 19.9% literal, with the basis. A later stage reading this field as capacity-embedded growth needs the caveat. No EM score impact.

### C-P1-05. MINOR. Emerging Moat, E22 optionality register.
- Rule: the register holds forward advantages that "scored 0 or rest only on" claim or inference evidence (P07 l.184-185). It is "Carried in the B07 block as optionality_register[]" (P07 l.194).
- Claimed: 13 rows in the report (B07 l.458-470); 10 rows in the block (B07y l.42-51).
- Recomputed: the block drops "GaN next-generation radar" (B07 l.467) and "Platform / modular product cadence (A4)" (B07 l.468), and merges the A2 and I1 rows into one. R1 scores 2.1 on claims only (B07 l.437) and B1 scores 1.5 at the inference multiplier (B07 l.419). Neither has a register row in the report or the block. Converting evidence: for R1, the final DAP 2026 notification (draft only, B07 l.393; date NOT FOUND); for B1, a disclosed in-house share of active devices or a material-cost breakdown.
- Impact: synthesis merges the block register into the monitoring checklist (P07 l.194-195), so two report rows would not reach it. No score impact; register items are watched, never scored.

### C-P1-06. MINOR. Gate 0, G14 window treatment.
- Claimed: B2, B3 and B4 scored 0 as NOT FOUND on a 2-year FY25-FY26 window, "window under 3 years" (B01 l.58). M6 scored 3 on a 2-year FY25-FY26 R&D window (B01 l.111; B01y l.40). M12 uses the same 2-year WC-days window (B01 l.117).
- Rule: P01 sets the 3-year minimum for the data set as a whole (l.23-25). It zeroes only data points that are absent (l.20-22). It sets no per-metric window. The stage applied an unwritten per-metric floor to Block B but not to M6.
- Recomputed, reading 1 (3-year floor per metric, applied to all): M6 = 0; moat_score 12; moats_confirmed 2; grand_total 65; moat_class MODERATE; classification AVERAGE.
- Recomputed, reading 2 (no per-metric floor): B2 2, B3 1, B4 5 (B01 l.64); Block B 8; core 61; DB2 stops firing; DB4 caps at AVERAGE. E2 stays NOT FOUND because its window is 3 years by definition.
- Decision impact: none. AVERAGE and MODERATE hold under both readings. Severity is MINOR because the written rule does not settle which reading is right, and B01 discloses both 2-year bases. If a later stage uses moat_score or moats_confirmed as a number, it should use one reading throughout, never the current mix.

## FRAMEWORK GAPS FOR OPERATOR RULING (not stage failures)

1. Per-metric window. P01 does not say whether the 3-year minimum (l.23) applies to each metric. See C-P1-06.
2. Strength bands. P07 names Strong, Moderate, Weak and None (l.157) but sets no cut-offs. The stage used its own (B07 l.11). active_categories depend on them.
3. Combined matrix. P07 names the combined labels (l.204-205) but not the mapping from Gate 0 class and EM band to a label. A grep for "HIGH POTENTIAL" in prompts/ finds only P07. I did not check the Master, which is outside phase-1 scope. 6D cannot be re-derived from the phase-1 rule sources.
4. "Active" in the completionist guard (P07 l.42-43) is undefined. It could mean non-zero, or Strong/Moderate as in the block template (P07 l.227).
5. Mixed evidence. P07 sets no rule for the multiplier when a category holds items of more than one class (weakest link or strongest item).
6. 2C basis. P07 l.60-62 does not say whether "historical fixed asset turnover" is the latest year or a mean. The stage used FY26 4.51x, the lowest of the five years (B07 l.124-128). The five-year mean of 4.84x gives 21.4% (calc). The rule also does not say whether intangibles under development count as capex under execution. See C-P1-04.

## OUT OF SCOPE THIS PHASE

Rules 4-7 and 11-15 run in phase 3: B09 downstream candidates, B11 valuation, the expectation ledger and chunk fidelity. B09 is not among the phase-1 inputs, so rule 6 is not checked here. Rule 9 (stage 13 narrative) and rule 10 (B09b dossier) run at the /finalize verifier pass. The valuation, expectation-ledger and narrative fields in the block are pending, not passed.

## YAML BLOCK

```yaml
stage: B12c
company: "ASTRAMICRO"
run_date: "2026-11-15"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete
scope: "phase 1: Gate 0 (B01) and Emerging Moat (B07) only; valuation audit (B10, B11) pending phase 3"
gate0: {rules_checked: 21, fails: ["G14 window treatment inconsistent: B2-B4 refused on a 2-year window, M6 scored 3 on a 2-year window (MINOR; AVERAGE and MODERATE unchanged)"]}
emoat: {rules_checked: 25, fails: ["E08 A3, A4, G2 scored 0 with evidence matching a listed indicator; matrix floor LL=1 (MAJOR; em_score 19.2 not 16.5, MODEST unchanged)", "E17 I2 answered collectively; institutional-relationship direction not tested per moat (MINOR; I2 0 unchanged)", "E18 D1, E2, H1 headed NO EVIDENCE FOUND while tabling items (MINOR; scores unchanged)", "E21 capex_embedded_growth_pct 19.9 carries Rs 27 Cr the report calls not capacity; plant-only 9.4 (MINOR)", "E22 register: block drops 2 report rows and merges 2; R1 and B1 have no row (MINOR)"]}
valuation: {status: "pending phase 3", rules_checked: 0, fails: []}
expectation_ledger: {status: "pending phase 3", present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: []}  # rules 13-14; any fail = REWORK stage 11
business_narrative: {status: "pending stage 13 (finalize verifier pass)", fails: []}  # rule 9; any fail = REWORK stage 13
recomputed_destination_pe: ""  # phase 3
recomputed_decision: ""        # concur: Gate 0 AVERAGE, EM MODEST, combined AVERAGE
findings:
  - {id: "C-P1-01", framework: "emoat", rule: "E08 matrix floor: no evidence = 0, LL = 1 (prompts/07 l.171-172)", severity: "MAJOR", stage: "07", claimed: "A3 0, A4 0, G2 0; em_score 16.5 (07-emoat.md l.417, l.418, l.431, l.438)", recomputed: "A3 1.0 (A3-1 DOC automation), A4 0.7 (A4-2 CLAIM modular), G2 1.0 (G2-1 DOC WC days 459 to 374); em_score 19.2, range 18.7-19.2", decision_impact: "band MODEST unchanged; active_categories unchanged; B2+H2 downside case 13.2 not 10.5, so the analyst_note fragility statement fails; gap to STRENGTHENING 5.8 not 8.5"}
  - {id: "C-P1-02", framework: "emoat", rule: "E17 I2 answered per moat with both directions tested (prompts/07 l.140-148)", severity: "MINOR", stage: "07", claimed: "one collective answer; relationships called execution leads (07-emoat.md l.340)", recomputed: "I2 0 unchanged; no specific sacrifice named (prompts/12 rule 8)", decision_impact: "none; reasoning gap on the institutional-relationship direction"}
  - {id: "C-P1-03", framework: "emoat", rule: "E18 NO EVIDENCE FOUND only when none exists (prompts/07 l.39-40)", severity: "MINOR", stage: "07", claimed: "D1, E2, H1 headed NO EVIDENCE FOUND while tabling D1-1, E2-1, E2-2, H1-1 (07-emoat.md l.239, l.245-250, l.301)", recomputed: "0 each unchanged; no tabled item matches a listed indicator; H1-1 credited in R1", decision_impact: "none; label only"}
  - {id: "C-P1-04", framework: "emoat", rule: "E21 block field carries a basis the report supports (prompts/07 l.60-62)", severity: "MINOR", stage: "07", claimed: "capex_embedded_growth_pct 19.9 (B07-emoat.yaml l.40)", recomputed: "19.9 on the literal total-capex reading; 9.4 plant-only (24 x 4.51 = 108 Cr), the report's own capacity figure (07-emoat.md l.132)", decision_impact: "none on the EM score; block should carry both figures with the basis"}
  - {id: "C-P1-05", framework: "emoat", rule: "E22 optionality register complete and carried to the block (prompts/07 l.184-185, l.194)", severity: "MINOR", stage: "07", claimed: "13 report rows (07-emoat.md l.458-470); 10 block rows (B07-emoat.yaml l.42-51)", recomputed: "block missing GaN next-generation radar and A4 platform cadence; A2 and I1 merged; R1 (2.1, claim-only) and B1 (1.5, inference multiplier) have no row", decision_impact: "none on scores; two report rows would not reach the synthesis monitoring checklist"}
  - {id: "C-P1-06", framework: "gate0", rule: "G14 one window treatment across metrics (prompts/01 l.19-25)", severity: "MINOR", stage: "01", claimed: "B2-B4 NOT FOUND on a 2-year window (01-gate0.md l.58); M6 3 on a 2-year window (01-gate0.md l.111)", recomputed: "reading 1, per-metric 3-year floor: M6 0, moat_score 12, moats_confirmed 2, grand_total 65; reading 2, no floor: Block B 8, core 61, DB2 off", decision_impact: "none; AVERAGE and MODERATE under both readings"}
framework_gaps:
  - "prompts/01: per-metric minimum window undefined (C-P1-06)"
  - "prompts/07: Strong/Moderate/Weak/None cut-offs undefined; stage used its own (07-emoat.md l.11)"
  - "prompts/07: combined-matrix mapping absent (labels only, l.204-205); 6D not re-derivable in phase-1 scope"
  - "prompts/07: 'active' in the completionist guard undefined (non-zero vs Strong/Moderate)"
  - "prompts/07: multiplier rule for mixed-class evidence undefined"
  - "prompts/07 2C: 'historical' FAT (latest vs mean) and treatment of intangibles under development undefined"
critical_count: 0
major_count: 1
minor_count: 5
acceptance_rate: 87.0             # rules passed / rules checked = 40 / 46, %
rework_trigger: false             # no Verifier A item here; rate above 60% on a denominator of 46
```
