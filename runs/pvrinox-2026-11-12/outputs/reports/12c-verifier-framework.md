# Stage 12 Verifier C: Framework Adherence, PVRINOX, run 2026-11-12 (PHASE 1 SCOPE)

## Scope and inputs

- Scope: Gate 0 (B01) and Emerging Moat (B07) compliance only. The valuation audit (B10, B11) is PENDING PHASE 3.
- Rule sources read: prompts/12-verifiers-pipeline.md (Verifier C section, l.213-390), prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md. Where a CLAUDE.md law applies, it is cited by name (spear-gate load-bearing facts, one improvement one mechanism, Rule J symmetric bar, the "flag" definition).
- Artifacts audited: runs/pvrinox-2026-11-12/outputs/reports/01-gate0.md, runs/pvrinox-2026-11-12/outputs/blocks/B01-gate0.yaml, runs/pvrinox-2026-11-12/outputs/reports/07-emoat.md, runs/pvrinox-2026-11-12/outputs/blocks/B07-emoat.yaml.
- Not read: the valuation framework documents (Master Role 1, Section 1B layers, FTTCP), per phase-1 scope. Corpus documents were not read either. Verifier A owns the question of whether a number exists in the source. Every re-derivation below uses the inputs that B01 or B07 state, with the line anchor.
- Verifier C rules in phase-1 scope: 1, 2, 3, 8. Deferred: 4, 5, 7, 11 to 15 (B11 scope). Rule 6 is deferred because it needs B09 and the stage 11 catalysts, and B09 is not a phase-1 input. Rule 9 waits for stage 13. Rule 10 fires at /finalize.
- Anchor key: "G l.N" = 01-gate0.md line N. "GB l.N" = B01-gate0.yaml line N. "E l.N" = 07-emoat.md line N. "EB l.N" = B07-emoat.yaml line N. "P01 l.N" and "P07 l.N" = rule source lines in prompts/01 and prompts/07. All money in Rs Cr unless the cited line says Rs Mn.

## Summary

| Framework | Rules checked | Passed | Failed | Acceptance |
|---|---|---|---|---|
| Gate 0 (B01) | 52 | 46 | 6 | 88.5% |
| Emerging Moat (B07) | 34 | 29 | 5 | 85.3% |
| Total | 86 | 75 | 11 | 87.2% |

Findings: 12 (11 rule fails plus 1 observation). CRITICAL 0, MAJOR 1, MINOR 11.

Decision effect: none.
- The Gate 0 classification AVOID (GB l.25) holds under every rule-literal reading. The highest rule-literal core is 38 (G0-03 mixed-basis A4), still under 40 (P01 l.149).
- EM 9.4, NONE (EB l.22-23) holds. With the E-20 double-credit correction, the range is 8.4 to 9.4. Both ends are under 12 (P07 l.176).
- The one MAJOR (G0-51) is a one-sided sensitivity. B01 headlines an "AVERAGE ex-lease" reading at core 44. That reading needs two things at once: the lease re-basing and the one-time Zea Maize gain. Remove the gain and the ex-lease core is 35, AVOID. B07 6D repeats the AVERAGE reading.

## Part 1: Gate 0 (B01) compliance

| ID | Rule (source) | B01 states | Re-derived from stated inputs | Result |
|---|---|---|---|---|
| G0-01 | Opening data line; 3-year minimum history (P01 l.23-25) | "Data available: 10 years (FY17 to FY26)"; B2, B3, B4, M12 on FY24-FY26 (G l.3) | 10 years. The 3-year windows meet the 3-year minimum. | PASS |
| G0-02 | Data confidence tier (P01 l.142-144) | 10 years full; history_downgrade false (G l.106; GB l.32) | 10+ years = full. No downgrade. | PASS |
| G0-03 | ROCE = EBIT / (TA - CL), fixed, no substitution (P01 l.27-31) | Proxy capital employed (equity + reserves + borrowings incl. leases) for all 10 years. Exact TA - CL shown for FY25 3.2% and FY26 8.4% only (G l.18, l.30-31) | This is a substitution. On the fixed formula, only FY25-FY26 exist: 2 years, under the 3-year minimum. A1, A2 and A4 are then NOT FOUND and score 0 (P01 l.19-22). Block A = 0, the same as B01. | FAIL, MINOR |
| G0-04 | ROE on average NW; closing-only earliest year stated (P01 l.32-33) | FY17 "closing only 964.99" (G l.22) | 95.79 / 964.99 = 9.9% | PASS |
| G0-05 | WC days formula; basis stated (P01 l.34-38) | Revenue basis (G l.49) | FY26: (267.2 + 73.2 - 594.8) / 6,646.2 x 365 = -14.0 days (G l.49) | PASS |
| G0-06 | FCF = CFO - capex (P01 l.39-40) | G l.47 | 1,979.0 - 627.9 = 1,351.1; 1,967.5 - 330.7 = 1,636.8; 2,160.3 - 258.7 = 1,901.6 (G l.47) | PASS |
| G0-07 | CAGR formula (P01 l.41) | 13.5% revenue, 14.9% PAT (G l.54-55) | (6,646.2 / 2,119.43)^(1/9) - 1 = 13.54%; (334.1 / 95.79)^(1/9) - 1 = 14.89% (G l.54-55) | PASS |
| G0-08 | CAGR edge rules (P01 l.43-50) | Both endpoints positive; interior losses noted; no synthetic CAGR (GB l.38) | The negative-endpoint rule does not trigger. The swing note is in data_notes. C4 is not N/M. | PASS |
| G0-09 | A1 median ROCE (P01 l.55) | 6.3%, score 0 (G l.35) | Sorted: -6.5, -2.8, 2.4, 2.9, 4.8, 7.9, 13.1, 14.6, 15.4, 20.6 (G l.22-31). Median (4.78 + 7.89) / 2 = 6.33%. Under 10 = 0. | PASS |
| G0-10 | A2 minimum ROCE (P01 l.56) | -6.5% FY21, score 0 (G l.36) | -441.00 / 6,836.47 = -6.45% (G l.26). Under 8 = 0. | PASS |
| G0-11 | A3 median ROE (P01 l.57) | 0.7%, score 0 (G l.37) | Median (-0.44 + 1.83) / 2 = 0.70% (G l.25, l.29). Under 12 = 0. | PASS |
| G0-12 | A4 ROCE trend (P01 l.58-59) | -5.2pp, score 0 (G l.38) | 7.885 - 13.080 = -5.20pp (G l.22, l.31). Decline over 5pp = 0. | PASS |
| G0-13 | B1 cumulative CFO / PAT (P01 l.62-63) | N/M, score 0 (G l.46) | Sum of PAT G l.22-31 = -1,111.0. 9,107.4 / -1,111.0 = -8.20. Under 0.50 = 0. | PASS |
| G0-14 | B2 FCF-positive years (P01 l.64) | 3 of 3, score 5 (G l.47) | 100% = 5 | PASS |
| G0-15 | B3 cumulative FCF / PAT (P01 l.65-66) | 217x, literal 5, flagged (G l.48) | 4,889.5 / 22.5 = 217.3. At or above 0.60 = 5. The literal score follows the rule. | PASS |
| G0-16 | B4 WC days change (P01 l.67-68) | +6.6 days, score 1 (G l.49) | -14.0 - (-20.6) = +6.6. Increase of 5-15 = 1. | PASS |
| G0-17 | C1 revenue CAGR (P01 l.71) | 13.5%, score 3 | 13.54%. Band 10-14.9 = 3. | PASS |
| G0-18 | C2 PAT CAGR (P01 l.72) | 14.9%, score 3 | 14.89%. Band 10-14.9 = 3. | PASS |
| G0-19 | C3 positive revenue years (P01 l.73) | 7 of 9, score 3 (G l.56) | 77.8%. Band 75-99 = 3. | PASS |
| G0-20 | C4 PAT CAGR minus revenue CAGR (P01 l.74) | +1.4pp, score 3 (G l.57) | 14.89 - 13.54 = +1.35pp. Within 3pp = 3. | PASS |
| G0-21 | D1 ND / EBITDA (P01 l.77-78) | 2.95x, score 1 (G l.63) | (6,779.1 - 591.6) / 2,095.2 = 2.95x. Band 2-3x = 1. | PASS |
| G0-22 | D2 EBIT / interest (P01 l.80-81) | 1.52x, score 1 (G l.64) | 1,116.4 / 732.8 = 1.52x. Band 1.5-2.9 = 1. | PASS |
| G0-23 | D3 debt / equity (P01 l.83-84) | 0.92, score 3 (G l.65) | 6,779.1 / 7,378.7 = 0.92. Band 0.5-1.0 = 3. | PASS |
| G0-24 | D4 current ratio (P01 l.85-86) | 0.47, score 0 (G l.66) | 11,122 / 23,520 = 0.47. Under 1.0 = 0. | PASS |
| G0-25 | E1 promoter holding (P01 l.89-90) | 27.02%, score 0; professionally-managed exception not applied (G l.75) | Under 30 = 0. A promoter group exists, so the exception does not apply. | PASS |
| G0-26 | E2 promoter change, 3 years (P01 l.91-92) | -0.82pp, score 3 (G l.76) | 27.02 - 27.84 = -0.82pp. Within 1 = 3. | PASS |
| G0-27 | E3 pledge (P01 l.93) | 11.10% of promoter holding, score 1 (G l.77) | Band 5-15 = 1. DB5 (over 15%) does not trigger. | PASS |
| G0-28 | E4 contingent liabilities / NW (P01 l.94-95) | 3.5%, score 5 (G l.78) | 255.5 / 7,378.7 = 3.46%. Under 5 = 5. | PASS |
| G0-29 | M1 pricing power (P01 l.102-104); no qualitative judgments (P01 l.13) | 3, on company pre-Ind AS 116 margin FY26 14.4% vs screener FY17 15.1% (G l.84) | Rule-literal on the screener series: 15.1% to 31.5% = +16.4pp, revenue CAGR 13.5% = 5 (G l.84) | FAIL, MINOR |
| G0-30 | M2, M5, M9 peer tests (P01 l.99-100) | 0, PEER DATA NEEDED (G l.85, l.88, l.92) | 0 | PASS |
| G0-31 | M3 capital efficiency (P01 l.107-108) | 0 (G l.86) | FAT 6,646.2 / 13,373.0 = 0.50x; ROCE 7.9%. Fails the FAT over 1x and ROCE over 12% floor = 0. | PASS |
| G0-32 | M4 customer stickiness (P01 l.109-111) | 1 (G l.87) | 2 decline years, CAGR positive = 1 | PASS |
| G0-33 | M6 technology (P01 l.114-116) | 0 (G l.89) | R&D not reported. Every band needs R&D of 1% or more = 0. | PASS |
| G0-34 | M7 regulatory (P01 l.117-119) | 0, PEER DATA NEEDED (G l.90) | Listed-player count not provided = 0 | PASS |
| G0-35 | M8 distribution (P01 l.120-122) | 5 (G l.91) | 1,798 screens, net +75 (93 - 18). Revenue per screen 6,646.2 / 1,798 = 3.70 vs 5,699.9 / 1,723 = 3.31 (G l.91, l.56). = 5 | PASS |
| G0-36 | M10 switching costs (P01 l.126-128) | 1 (G l.93) | Overall growth, 2 decline years = 1 | PASS |
| G0-37 | M11 network effects (P01 l.129-133) | 5, literal (G l.94) | 10 years is 6 or more, so the two-window test runs. 21.0% over 3.2%, selling % 6.65 to 5.51 = 5. | PASS |
| G0-38 | M12 negative WC (P01 l.134-135) | 5 (G l.95) | 3 of 3 years negative = majority = 5 | PASS |
| G0-39 | Moat count and class (P01 l.98-99, l.137-138) | 4 present, STRONG (G l.97) | M1 3, M8 5, M11 5, M12 5 = 4 present = STRONG | PASS |
| G0-40 | Block, core and grand totals | A 0, B 11, C 12, D 5, E 9; core 37; moat 20; grand 57 (GB l.19-22) | B 0+5+5+1 = 11. C 3+3+3+3 = 12. D 1+1+3+0 = 5. E 0+3+1+5 = 9. Core 37. Moat 3+0+0+1+0+0+0+5+0+1+5+5 = 20. Grand 57. | PASS |
| G0-41 | Classification matrix (P01 l.146-149) | AVOID (G l.105) | Core 37 under 40 = AVOID | PASS |
| G0-42 | Deal-breaker application (P01 l.151-159) | 1, 3, 4, 8 triggered; 6 not (GB l.26-31) | DB1: Block A 0 under 8. DB2 not (B 11). DB3: 6.3% under 10. DB4: -8.20 under 0.50. DB5 not (11.1%). DB6 not (2.95x is not over 3x). DB7 not (2 of 9). DB8: FY24 and FY25 negative. DB9 not. Every cap sits above AVOID, so AVOID stands. | PASS |
| G0-43 | State WHICH years drive each deal-breaker (P01 l.151-154) | Years given for DB1, DB4, DB8. DB3 reads "median ROCE 6.3%" only (G l.111; GB l.28) | DB3 driving years: FY21-FY26, six of ten years under 10% (G l.26-31) | FAIL, MINOR |
| G0-44 | FLAG-GATE0 at AVERAGE or below with depressors (P01 l.175-177) | Raised (GB l.14-16) | Required and present | PASS |
| G0-45 | Source anchor on every extracted number (P01 l.15-18) | Block F rows M3, M11, M12 carry no anchor (G l.86, l.94, l.95) | Unanchored: net block 13,373.0; CAGRs 21.0% and 3.2%; selling % 6.65 and 5.51; FY25 WC -18.1 days (no components shown anywhere in B01) | FAIL, MINOR |
| G0-46 | NOT FOUND, never estimated (P01 l.19-22) | Capex FY17-FY23, payables FY17-FY23, CL FY17-FY24 NOT FOUND (GB l.8-10) | No filled gap found | PASS |
| G0-47 | End with exactly the template block (P01 l.165-198); report copy equals block file (agent non-negotiable) | Report data_notes is a one-line string pointer (G l.155). Block file data_notes is an 18-item list (GB l.33-51). | The template types data_notes as a list (P01 l.189). The two copies differ. | FAIL, MINOR |
| G0-48 | block_b_trend with the number (P01 l.191-192) | "improving: CFO 2,160.3 Cr FY26 vs 1,967.5 Cr FY25" (GB l.52) | Present | PASS |
| G0-49 | analyst_note at most 200 words (P01 l.193-197) | About 90 words (GB l.53) | Under the cap | PASS |
| G0-50 | Spear load-bearing facts first (CLAUDE.md SPEAR GATE) | 4 facts checked before scoring (G l.7-14) | Present | PASS |
| G0-51 | Symmetric bar on sensitivities (CLAUDE.md Rule J; "flag" = surfaced prominently in the verdict) | Flag, analyst note and decision line carry "ex-lease core 44 = AVERAGE" and "AVOID only on the lease-inclusive reported basis" (GB l.16, l.53; G l.113) | The ex-lease reading re-bases Block D only and keeps the one-time gain. On B01's own ex-gain inputs: ex-gain core 27; ex-lease plus ex-gain core 35, AVOID. Detail below. | FAIL, MAJOR |
| G0-52 | Dashboard elements (P01 l.163-165) | Blocks, anchors, moat bars, classification box, strongest and weakest block, decision line (G l.97-113) | Present | PASS |

### Gate 0 fail detail

**G0-51 (MAJOR). The ex-lease AVERAGE reading is one-sided.**

B01 reports three ex-gain inputs, but never totals them:
- C2 ex-gain 7.0%, score 1 (G l.55).
- D2 ex-gain 1.38x, score 0 (G l.69).
- B3 depends on the gain. Without B3, Block B is 6 (G l.48, l.50).

Recomputed on B01's own ex-gain basis (continuing PAT 176.1 Cr, G l.12):
- B3: cumulative PAT FY24-FY26 = -32.0 - 279.6 + 176.1 = -135.5. Negative = 0. Block B = 6, and DB2 triggers (Block B under 8, max GOOD) (P01 l.155).
- C2 = 1 (7.00%). C4: 7.00 - 13.54 = -6.54pp, band -3 to -8 = 1. Block C = 8.
- D2 = 0 (1.38x). Block D = 4.
- Block A is unchanged at 0. FY26 ex-gain ROCE is 1,008.0 / 14,157.8 = 7.12%, the median is 5.95% and A4 is -5.96pp, so all score 0. Block E is unchanged at 9.
- **Ex-gain core = 0 + 6 + 8 + 4 + 9 = 27, AVOID.**
- Ex-lease plus ex-gain: D1 167.0 / 2,095.2 = 0.08x = 4; D2 1,008.0 / 145.6 = 6.92x = 4; D3 0.10 = 4; D4 0.70 = 0. Block D = 12 (G l.63-66, l.69). **Core = 0 + 6 + 8 + 12 + 9 = 35, AVOID.**

The ex-lease D2 also mixes two bases. It divides the Ind AS 116 EBIT (rent out, ROU depreciation in) by interest on borrowings only, 145.6 Cr (G l.64). B01 does not give the same-basis figure: NOT FOUND. Bound: with the gain kept and D2 at 0, the ex-lease core is 40, still AVERAGE. So the basis mix weakens the presentation but does not move the 44 reading across a band.

Effect: the classification of record stays AVOID. The analyst-note sentence "Core 37 is AVOID only on the lease-inclusive reported basis" (GB l.53) is not true as a general statement. AVERAGE needs both the lease re-basing and the one-time disposal gain of 195.2 Cr reported (G l.12). The reading carries through to B07 6D and to combined_assessment (E l.320; EB l.47).

Fix: put four readings side by side in the FLAG-GATE0 reason and the analyst_note:
- reported: core 37, AVOID;
- ex-lease, Block D only, gain kept: core 44, AVERAGE;
- ex-lease and ex-gain: core 35, AVOID;
- ex-gain: core 27, AVOID, with DB2 triggered.

The observation that separates the two readings is whether FY27 continuing PAT, with no disposal gain, makes cumulative FY25-FY27 PAT positive.

**G0-03 (MINOR). ROCE formula substitution.** P01 l.27-31 fixes the formula and forbids alternatives. B01 used screener-convention capital employed for all ten years. It did so even for FY25-FY26, where TA - CL exists (G l.30-31). It disclosed the change (G l.18). On a strict reading, the fixed formula covers 2 years, under the 3-year minimum (P01 l.23). A1, A2 and A4 are NOT FOUND and score 0, so Block A = 0, as B01 has it. The A4 sensitivity in B01 (G l.38: exact FY26 8.4% against proxy FY17 13.1%, -4.7pp, score 1) mixes the two bases. It is not the fixed formula either. Even if that sensitivity were scored, core would be 38, AVOID. No score change.

**G0-29 (MINOR). M1 scored off the literal rule.** The scorecard rule bars qualitative judgments (P01 l.13). The screener series gives +16.4pp margin expansion with a 13.5% revenue CAGR, so M1 = 5 (G l.84). B01 swapped in the company's pre-Ind AS 116 FY26 margin and scored 3. Recomputed: M1 5, moat_score 22, grand_total 59. moats_confirmed stays 4 and the class stays STRONG. The basis choices across B01 are not uniform:
- M1 removes the Ind AS 116 effect, which lowers the score by 2.
- Block D keeps the Ind AS 116 effect, as the rule requires.
- M11 keeps the INOX merger break at the literal score of 5 (G l.94).

A rule-literal scorecard uses the screener series throughout: M1 5, M11 5, Block D 5. A like-for-like scorecard needs an operator ruling that covers every structural break, not one test.

**G0-43 (MINOR).** P01 l.153-154 asks for the years that drive each deal-breaker. DB3 has none (GB l.28). The driving years are FY21-FY26: six of ten years have proxy ROCE under 10% (G l.26-31).

**G0-45 (MINOR).** These Block F numbers carry no anchor, against P01 l.15-18:
- M3 net block 13,373.0 (G l.86);
- M11 CAGRs 21.0% and 3.2%, and selling % 6.65 and 5.51 (G l.94);
- M12 FY25 WC -18.1 days (G l.95). Its receivables, inventory and payables are shown nowhere in B01.

Verifier A owns whether these numbers exist in the source. This finding covers only the missing anchors.

**G0-47 (MINOR).** The YAML at the end of the report (G l.155) has data_notes as a string that points to the block file. The block file has the list (GB l.33-51). The template types the field as a list (P01 l.189). The agent non-negotiable requires the same block in both places. The block file is the correct copy. The report copy should match it.

## Part 2: Emerging Moat (B07) compliance

| ID | Rule (source) | B07 states | Re-derived / checked | Result |
|---|---|---|---|---|
| E-01 | All six sections plus register, one response (P07 l.28) | Sections 1-6 and the register (E l.18-342) | Present | PASS |
| E-02 | Emerging Moat is not FTTCP (P07 l.3-6; CLAUDE.md) | E l.3 | Stated | PASS |
| E-03 | Spear load-bearing facts first (CLAUDE.md SPEAR GATE) | E l.9-16 | Present | PASS |
| E-04 | Evidence tag on every evidence item (P07 l.29-34) | Type column on every Section 3 evidence row (E l.114-191) | Present | PASS |
| E-05 | Source anchors in primary form (P07 l.35-36) | Several rows anchor to B03, B04 or B08, or to "AR MD&A" with no page | B03, B04 and B08 are not named stage-7 inputs (P07 l.7, l.246-264). B05 is (P07 l.254-255). | FAIL, MINOR |
| E-06 | NO EVIDENCE FOUND stated; no force-fit (P07 l.39-40) | 15 categories plus R1 marked (E l.98-197, l.233-237) | Present | PASS |
| E-07 | All 23 rows addressed (Verifier C rule 3; P07 l.171-174) | 22 plus R1 in Section 3 (E l.98-237), the summary table (E l.201-225) and the scorecard (E l.245-267) | 23 rows in each | PASS |
| E-08 | Summary table plus Strong/Moderate count (P07 l.155-157) | "Strong or Moderate rows: 2 (D2, G1). Strong: 0." (E l.227) | Matches the rows | PASS |
| E-09 | Likelihood x impact matrix (P07 l.171-172) | C1 ML 1, D2 MM 2, E1 ML 1, F2 LM 1, G1 HM 3, H2 ML 1, H3 LL 1 (E l.252-264) | Each raw score matches the matrix | PASS |
| E-10 | Evidence multipliers (P07 l.172-173) | C1 0.7, D2 1.0, E1 0.7, F2 1.0, G1 1.0, H2 1.0, H3 1.0 (E l.252-264) | Every value is a legal multiplier. B07 calls the E1 weight 0.7 "blended" (E l.142, l.256). The rule has no blend: 0.7 is the claim multiplier. It fits here because the first-mover scale rests on claims. At 1.0 the total would be 9.7, still NONE. | PASS |
| E-11 | Scores consistent with evidence tiers; no claim-only row scored as documented (Verifier C rule 3) | C1 is claim-only and carries 0.7. Every 1.0 row rests on documented items (E l.133, l.157, l.167, l.182, l.193). | Consistent | PASS |
| E-12 | Adjusted total | 9.4 (E l.268) | 0.7 + 2.0 + 0.7 + 1.0 + 3.0 + 1.0 + 1.0 = 9.4 | PASS |
| E-13 | Classification band (P07 l.175-176) | NONE (E l.272) | 9.4 under 12 = NO MEANINGFUL EMERGING MOAT | PASS |
| E-14 | I1/I2 contribution stated separately (P07 l.180-181) | 0.0 of 9.4 (E l.270) | Present | PASS |
| E-15 | Completionist guard; recount line in the required form (P07 l.41-46, l.157-159) | "📄 recount performed: 9 documented items across 6 categories" (E l.229); 7 categories with any evidence | Line present. 7 is under 12, so the guard does not trip. | PASS |
| E-16 | Recount and evidence_mix match the tagged evidence (Verifier C rule 3) | documented 9, claim 6, inference 0 (EB l.27-28) | Section 3 tagged rows: documented 15, claim 7, inference 0 | FAIL, MINOR |
| E-17 | Category 21, I1 (Verifier C rule 8; P07 l.122-138) | Present, scored 0, "Neither leg" (E l.195) | 0. Neither leg is evidenced. The rule is met. | PASS |
| E-18 | Category 22, I2 above 0 only with a specific sacrifice (Verifier C rule 8; P07 l.139-153) | Present, scored 0 (E l.197) | 0 | PASS |
| E-19 | I2 answers the question for each moat claimed in the scan (P07 l.140-142) | Answered for scale, premium formats, online fees (D2), SMART (E1) and capital-light (H2) (E l.197) | Not answered for C1, F2, G1, H3 | FAIL, MINOR |
| E-20 | One improvement, one mechanism (CLAUDE.md NEVER list) | The G1/H2 split is stated (E l.182) | The balance-sheet repair is credited in F2 (E l.153) and G1 (E l.163-164). The capital-light share is credited in F2 (E l.153) and H2 (E l.177). | FAIL, MINOR |
| E-21 | 2C arithmetic shown (P07 l.60-62) | 3,100 x 2.27 = 7,037; 7,037 / 64,843 = 10.9% (E l.81-86) | 64,843 / 28,538 = 2.27x; 3,100 x 2.27 = 7,037; 7,037 / 64,843 = 10.85% | PASS (see O-1) |
| E-22 | 1C left NOT FOUND, not estimated (P07 l.39-40) | Expected % NOT FOUND (E l.56) | Correct | PASS |
| E-23 | Section 4, 4A-4C, R1 (P07 l.161-168) | E l.231-237; R1 = 0 | Present | PASS |
| E-24 | Optionality register: format, contents, carried in block (P07 l.183-196) | 8 rows, 4 columns (E l.278-287; EB l.38-46) | Every row scored 0 or rests on claim-only evidence | PASS |
| E-25 | 6C uses the injected Gate 0 block (P07 l.201-203) | Core 37, 4 moats, AVOID and STRONG (E l.311-316) | Matches GB l.20-25 | PASS |
| E-26 | Full reasoning for HIGH POTENTIAL and TURNAROUND (P07 l.207-208) | E l.320 | Present | PASS |
| E-27 | One combined classification (P07 l.203-204) | Two values: AVOID, and AVERAGE on the ex-lease basis (E l.320; EB l.47) | One value. The Gate 0 classification of record is AVOID (GB l.25). | FAIL, MINOR |
| E-28 | 6A, 6B, 6E present (P07 l.199-210) | E l.291-342 | Present | PASS |
| E-29 | active_categories holds only Strong/Moderate rows (P07 l.227) | G1, D2 (EB l.24-26) | Matches | PASS |
| E-30 | catalysts_12m with evidence type and anchor (P07 l.231-232) | 7 rows (EB l.29-36) | Present | PASS |
| E-31 | capex_embedded_growth_pct comes from 2C (P07 l.233) | 10.9 (EB l.37) | Matches E l.88 | PASS |
| E-32 | Exact template block; report copy equals block file | E l.344-399 vs EB l.1-54 | Identical | PASS |
| E-33 | analyst_note at most 200 words (P07 l.239-242) | About 100 words (EB l.54) | Under the cap | PASS |
| E-34 | Absolute bands, no rescale (P07 l.11-18, l.177-181) | Bands applied as written (E l.272) | Correct | PASS |

Not verifiable in phase-1 scope: the 6D mapping to the "standard matrix" (P07 l.203-205). prompts/07 names the matrix but does not define it. A search of prompts/ for HIGH POTENTIAL, TURNAROUND and EXCELLENT+ finds only P07 l.204-208. B07 states its own entry test for HIGH POTENTIAL and TURNAROUND (E l.320). That test is consistent with the P07 l.205-207 hint. It is not counted as a check.

### Emerging Moat fail detail

**E-05 (MINOR). Secondary anchors.** P07 l.35-36 asks for primary anchors (AR page, call, presentation slide). Rows that anchor to blocks that are not stage-7 inputs:
- H3 "FY26 plan was solar in 47 cinemas; 3 commissioned", documented, anchored "B03 guidance_table" (E l.190);
- F2 "FY26 screens 93 vs AR range 100-110", documented, anchored "B03" (E l.155);
- 1A Devyani "AR promised 7-9, delivered 3 (B03)" (E l.29);
- 1C rows anchored to B04 (E l.48-54);
- I1 pay figure "(B08)" (E l.195);
- 6E existing-moat column "(B04)" (E l.328).

A3 has "(B03, AR MD&A)" with no page (E l.102). These rows do not set any positive raw score, so the effect on the score is nil. The run-pipeline dependency line is "7 after 1" (run-pipeline.md l.283-284). This verifier cannot see whether the orchestrator passed B03, B04 or B08 to stage 7.

**E-16 (MINOR). The recount does not match the tags.** Tagged evidence rows in Section 3, by category (documented / claim):
- C1 0 / 2 (E l.116-117);
- D2 2 / 1 (E l.129-131);
- E1 1 / 1 (E l.139-140);
- F2 4 / 0 (E l.152-155);
- G1 3 / 0 (E l.163-165);
- H2 2 / 2 (E l.177-180);
- H3 3 / 1 (E l.188-191).

Total: documented 15, claim 7, inference 0. B07 reports 9, 6, 0 (EB l.27). The recount leaves out these documented rows:
- F2: delivered list, missed list, and FY26 screens 93 vs 100-110;
- H2: Devyani 3 of 7-9;
- H3: FY26 solar plan 47 vs 3 commissioned, and utilities +7.0%.

Most of these count against the moat. The recount also leaves out the C1 CRM claim. Sections 1-2 hold inference items (E l.40, l.77), so "inference 0" is true only for Section 3. The guard outcome does not change: 7 categories, under 12. Recomputed evidence_mix on Section 3 rows: {documented: 15, claim: 7, inference: 0}. Phase 3 note: if stage 11 reads evidence_mix into a Pillar 3 evidence input, it should use the recomputed counts or the stated counting unit.

**E-19 (MINOR). I2 coverage.** P07 l.140-142 says "For each moat claimed anywhere in this scan, answer". B07 answers for five items (E l.197). It does not answer for C1 loyalty, F2 execution, G1 war chest or H3 ESG. The score of 0 stands. B07 must still state the answer for those four. The answer may well be "nothing must be destroyed".

**E-20 (MINOR). Double credit.** CLAUDE.md: "Never credit one quality improvement through two mechanisms."
- F2's documented "Delivered" row (E l.153) lists gross debt Rs 760 Cr to Rs 501 Cr, net debt zero a quarter early, and capital-light share 77%.
- G1 scores the same balance-sheet repair (E l.163-164).
- H2 scores the same capital-light openings (E l.177).

B07 guards the G1/H2 overlap (E l.182) but not F2. B07 itself says F2 is "proven on the balance sheet and cost line" (E l.157). Bound: F2 adds 1.0 (E l.259). With the balance-sheet leg removed, F2 rests on the cost line and the missed expansion chain, so it scores 0 to 1.0. EM range 8.4 to 9.4, NONE either way.

**E-27 (MINOR). Two combined classifications.** 6D and combined_assessment carry "AVOID (reported ...); AVERAGE on the ex-lease basis (core 44)" (E l.320; EB l.47). P07 l.203-204 asks for one combined classification. The Gate 0 classification of record is AVOID. The ex-lease AVERAGE reading falls to core 35, AVOID, once the one-time gain is removed (G0-51). Recommended: combined_assessment "AVOID", with the sensitivity set from G0-51 as a note.

### Observation

**O-1 (MINOR, not a rule fail). The 2C FAT basis differs from B01.**
- B07 2C uses FAT 2.27x: standalone PPE only, one year, over a derived revenue proxy, Rs 432 x 150.1 Mn admissions (E l.81-83).
- B01 M3 uses FAT 0.50x on the screener net block (G l.86).
- On B01's FAT: 3,100 Mn x 0.497 = 1,541 Mn. Over FY26 revenue of 66,462 Mn (E l.44), that is 2.3%. B07 reports 10.9% (E l.88).

B07 calls 10.9% a ceiling (E l.88). Its own limits sentence says the 2.27x understates the leased screens, so the error runs both ways. The 2C arithmetic is shown and the limits are stated, so the 2C rule passes. Phase 3 note: stage 11 should not use capex_embedded_growth_pct 10.9 as a CAPACITY revenue basis without both FAT readings beside it.

## Part 3: Notes for the operator (not findings)

- N-1. Line 379 of the prompts/12 Verifier C template reads "(same line, comment "# rule 9; any fail = REWORK stage 13")". It is not a YAML key. This block emits `business_narrative:` as the rule 9 placeholder. Please name the key in the template.
- N-2. prompts/07 6D refers to a "standard matrix" (P07 l.203-205) that is not defined in prompts/. Until it is, nobody can verify 6D mappings against a rule source.
- N-3. run-pipeline.md l.283-284 gives the dependency "7 after 1". But prompts/07 l.254-255 injects B05 for F2. This run committed stage 5 (360ec479) before stage 7 (13137e83), so this run is not affected. A future run could dispatch stage 7 before B05 exists.
- N-4. B3 = 5 is the rule-literal score. It rests on a 22.5 Cr cumulative PAT that contains the one-time gain (G l.48). B01 flagged it. It is the swing input in G0-51.
- N-5. Verifier C rule 6 (B09 downstream candidates) is deferred. B09 is not among the phase-1 inputs.

## Part 4: Deliverable block

```yaml
stage: B12c
company: "PVRINOX"
run_date: "2026-11-12"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete
gate0: {rules_checked: 52, fails: ["G0-03 ROCE fixed formula substituted by proxy capital employed (MINOR)", "G0-29 M1 scored 3 off-literal; rule-literal 5 (MINOR)", "G0-43 DB3 driving years not stated (MINOR)", "G0-45 unanchored Block F numbers M3, M11, M12 (MINOR)", "G0-47 report YAML data_notes is a string; block file and template are a list (MINOR)", "G0-51 one-sided sensitivity: ex-lease AVERAGE needs the one-time gain; ex-lease ex-gain core 35 AVOID; ex-gain core 27 (MAJOR)"]}
emoat: {rules_checked: 34, fails: ["E-05 evidence anchored to B03/B04/B08 or AR MD&A without page (MINOR)", "E-16 recount and evidence_mix 9/6/0 vs tagged Section 3 rows 15/7/0 (MINOR)", "E-19 I2 not answered for C1, F2, G1, H3 (MINOR)", "E-20 balance-sheet repair credited in F2 and G1; capital-light share in F2 and H2 (MINOR)", "E-27 two combined classifications; one required, AVOID of record (MINOR)"]}
valuation: {rules_checked: 0, fails: [], status: "PENDING PHASE 3: B10/B11 not in phase-1 inputs"}
expectation_ledger: {present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: [], status: "PENDING PHASE 3"}  # rules 13-14; any fail = REWORK stage 11
business_narrative: {status: "PENDING: stage 13 not run; rule 9 fires at /finalize", fails: []}  # rule 9; any fail = REWORK stage 13
recomputed_destination_pe: ""  # phase 1: not applicable
recomputed_decision: ""        # concur: Gate 0 AVOID (GB l.25), EM NONE 9.4 (EB l.22-23)
findings:
  - {id: "G0-51", block: "B01", rule: "symmetric bar on sensitivities (CLAUDE.md Rule J; flag definition)", severity: "MAJOR", claimed: "ex-lease core 44 AVERAGE; 'AVOID only on the lease-inclusive reported basis' (GB l.16, l.53)", recomputed: "ex-gain core 27 AVOID with DB2 (B3 0, C2 1, C4 1, D2 0); ex-lease plus ex-gain core 35 AVOID; AVERAGE needs lease re-basing AND the 195.2 Cr one-time gain (G l.12, l.48, l.55, l.69)", decision_effect: "none; AVOID of record stands; flag and analyst_note should carry all four readings"}
  - {id: "G0-03", block: "B01", rule: "ROCE fixed formula EBIT/(TA-CL), no substitution (P01 l.27-31)", severity: "MINOR", claimed: "proxy capital employed all 10 years (G l.18)", recomputed: "fixed formula covers FY25-FY26 only (G l.30-31), under the 3-year minimum; A1, A2, A4 NOT FOUND = 0; Block A 0, same as B01", decision_effect: "none"}
  - {id: "G0-29", block: "B01", rule: "M1 pricing power; no qualitative judgments (P01 l.13, l.102-104)", severity: "MINOR", claimed: "M1 3 on like-for-like 14.4% vs 15.1% (G l.84)", recomputed: "M1 5 on screener series 15.1% to 31.5%, +16.4pp, revenue CAGR 13.5%; moat_score 22, grand_total 59; moats_confirmed 4, STRONG unchanged", decision_effect: "none"}
  - {id: "G0-43", block: "B01", rule: "state which years drive each deal-breaker (P01 l.151-154)", severity: "MINOR", claimed: "DB3 'median ROCE 6.3%' with no years (GB l.28)", recomputed: "DB3 driven by FY21-FY26, six of ten years under 10% (G l.26-31)", decision_effect: "none"}
  - {id: "G0-45", block: "B01", rule: "anchor on every extracted number (P01 l.15-18)", severity: "MINOR", claimed: "M3 net block 13,373.0; M11 21.0%/3.2% and selling % 6.65/5.51; M12 FY25 -18.1 days unanchored (G l.86, l.94, l.95)", recomputed: "anchors required; FY25 WC components NOT FOUND in B01", decision_effect: "none"}
  - {id: "G0-47", block: "B01", rule: "exact template block; report copy equals block file (P01 l.165-198)", severity: "MINOR", claimed: "report data_notes is a string pointer (G l.155)", recomputed: "list of 18 items as in block file (GB l.33-51); report copy to match", decision_effect: "none"}
  - {id: "E-05", block: "B07", rule: "primary source anchors (P07 l.35-36)", severity: "MINOR", claimed: "rows anchored to B03/B04/B08 and 'AR MD&A' without page (E l.29, l.48-54, l.102, l.155, l.190, l.195, l.328)", recomputed: "primary page anchors required; no positive raw score depends on these rows", decision_effect: "none"}
  - {id: "E-16", block: "B07", rule: "recount consistent with evidence tiers (Verifier C rule 3; P07 l.41-46, l.157-159)", severity: "MINOR", claimed: "evidence_mix documented 9, claim 6, inference 0 (EB l.27)", recomputed: "Section 3 tagged rows documented 15, claim 7, inference 0; guard result unchanged (7 categories under 12)", decision_effect: "none in phase 1; phase 3 re-checks any Pillar 3 use of evidence_mix"}
  - {id: "E-19", block: "B07", rule: "I2 answered for each moat claimed in the scan (P07 l.140-142)", severity: "MINOR", claimed: "answered for scale, premium, D2, E1, H2 (E l.197)", recomputed: "C1, F2, G1, H3 not answered; I2 score 0 stands", decision_effect: "none"}
  - {id: "E-20", block: "B07", rule: "one improvement, one mechanism (CLAUDE.md)", severity: "MINOR", claimed: "F2 1.0 includes debt reduction and capital-light share (E l.153, l.259)", recomputed: "same facts scored in G1 (E l.163-164) and H2 (E l.177); F2 range 0 to 1.0; EM 8.4 to 9.4, NONE either way", decision_effect: "none"}
  - {id: "E-27", block: "B07", rule: "one combined classification (P07 l.203-204)", severity: "MINOR", claimed: "AVOID and AVERAGE ex-lease (E l.320; EB l.47)", recomputed: "combined_assessment AVOID; ex-lease reading is a sensitivity that falls to core 35 AVOID ex-gain (G0-51)", decision_effect: "none"}
  - {id: "O-1", block: "B07", rule: "observation: 2C FAT basis vs B01 M3 (P07 l.60-62)", severity: "MINOR", claimed: "capex_embedded_growth_pct 10.9 on PPE-only standalone FAT 2.27x (E l.81-88)", recomputed: "on B01 FAT 0.50x (G l.86): 3,100 Mn x 0.497 = 1,541 Mn / 66,462 Mn = 2.3%; 2C arithmetic itself correct", decision_effect: "none in phase 1; stage 11 should show both readings before any CAPACITY basis use"}
critical_count: 0
major_count: 1
minor_count: 11
acceptance_rate: 87.2             # rules passed / rules checked, % (75 of 86; gate0 46/52 = 88.5, emoat 29/34 = 85.3)
```
