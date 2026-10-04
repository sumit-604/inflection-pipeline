# Verifier C: Framework Adherence, MMP, run 2026-10-05 (PHASE 1 SCOPE)

Model: claude-opus-5-5 (matches .claude/agents/verifier-c-framework.md frontmatter).
Scope: Gate 0 (B01) and Emerging Moat (B07) only. The valuation audit (B10, B11, rules 4, 5 valuation half, 6, 7, 9 to 15) is PENDING PHASE 3. Those blocks do not exist yet.
Rule sources (the only two): prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md. Output shape: prompts/12-verifiers-pipeline.md, VERIFIER C section.
Artifacts audited: outputs/reports/01-gate0.md, outputs/blocks/B01-gate0.yaml, outputs/reports/07-emoat.md, outputs/blocks/B07-emoat.yaml.
Sources read to settle basis and availability: inputs/screening/screener-Data_Sheet.csv; inputs/screening/APARINDS-Data_Sheet.csv, ARFIN-Data_Sheet.csv, MAANALU-Data_Sheet.csv; inputs/annual-report/Annual_Report_2026.txt; inputs/annual-report/Annual_Report_2025.txt; inputs/shareholding/SHP_MMP_2026-06-30.md.
Units: Rs Cr unless marked L. L = Rs Lakh, the unit on the face of both annual reports. 100 L = 1 Cr.
Page anchors: the "[page N]" markers in the annual-report text files. Line numbers refer to the same text files.
Boundary: this verifier audits rule application. Verifier A owns whether each number exists at its anchor. This report cites source lines only to settle the basis of a figure or whether data was available. No other verifier output was read.

---
## 1. RESULT IN NUMBERS

| Item | Value |
| --- | --- |
| Gate 0 rules checked | 50 |
| Gate 0 FAIL lines | 12, from 7 findings: 1 CRITICAL, 4 MAJOR, 2 MINOR |
| Emerging Moat rules checked | 36 |
| Emerging Moat FAIL lines | 2, from 2 findings: 2 MINOR |
| Valuation rules checked | 0 (pending phase 3) |
| Acceptance rate | 72 of 86 = 83.7% (above the 60% REWORK trigger) |
| B01 classification as emitted | AVOID, core 39/100 (01-gate0.md line 78) |
| B01 classification recomputed | AVERAGE, core 40 to 54 across the rule readings in Section 3. AVOID survives under one reading only (core 38). |
| B01 moat profile as emitted | 4/60, 0 present, NONE |
| B01 moat profile recomputed | 11 or 12/60, 2 present (M5, M9), MODERATE |
| B07 em_score and band | 11.6, NONE. Concur. |
| B07 combined_assessment | AVOID. It inherits the B01 error. B07 applied its own rule correctly on the block it received. |

The one CRITICAL is F1. B01 declared a consolidated basis and then scored E4 on the standalone contingent-liabilities note. The consolidated note exists. On it, E4 scores 5, not 1. Core moves 39 to 43. The classification moves AVOID to AVERAGE. This holds under every reading of the rules.

---
## 2. GATE 0 COMPLIANCE TABLE (B01)

Recomputed values sit beside each FAIL. "On stated input" means the band was applied correctly to the value B01 stated; any input problem is a separate line.

| # | Rule (prompt 01) | B01 value | Verdict | Recomputed / note (anchor) |
| --- | --- | --- | --- | --- |
| G01 | Rule 6 opening line | "Data available: 10 years (FY2017 to FY2026)" | PASS | 10 annual columns (screener-Data_Sheet lines 10-11) |
| G02 | Rule 4, anchor after every extracted number | C1-C4, M3, M11 lines carry no inline anchor | FAIL MINOR (F6) | Add (screener-data) per line |
| G03 | ROCE formula fixed: EBIT / (Total Assets minus Current Liabilities); no substitutes | EBIT / (equity + reserves + borrowings), all 10 years | FAIL MAJOR (F3) | Fixed formula computable FY24-FY26: 14.74%, 16.31%, 12.91% (AR25 [page 154]-[page 155]; AR26 p.171 per B01 cross-check) |
| G04 | ROE = PAT / average net worth; FY17 closing disclosed | 10 values, median 12.15% | PASS | Recomputed all 10 from screener lines 24, 39-40; match to 0.1pp |
| G05 | WC days formula, basis stated | revenue basis stated | PASS | |
| G06 | FCF = CFO minus PPE and intangibles capex; no CFI proxy in the score | CFO+CFI proxy shown as info only | PASS | |
| G07 | CAGR formula | revenue 16.8%, PAT 6.8% | PASS | 16.83%, 6.76% (screener lines 11, 24) |
| G08 | CAGR edge rules | no negative endpoint; no annual swing; noted in data_notes | PASS | |
| G09 | A1 median ROCE band | 12.85% → 1 | PASS on stated input | 12.835% |
| G10 | A2 minimum ROCE band | 10.06% → 1 | PASS on stated input | |
| G11 | A3 median ROE band | 12.15% → 2 | PASS | |
| G12 | A4 ROCE trend band | −15.2pp → 0 | PASS on stated input | |
| G13 | B1 cumulative CFO / PAT | 1.21 → 5 | PASS | 297.83 / 246.72 = 1.207 (screener lines 24, 57) |
| G14 | B2 FCF-positive years | NOT FOUND → 0 | FAIL MAJOR (F2) | FY24-FY26 in corpus: 5 (PPE line) or 2 (PPE + CWIP + capital advances) |
| G15 | B3 cumulative FCF / PAT | NOT FOUND → 0 | FAIL MAJOR (F2) | 1 (0.33) or 0 (0.03) |
| G16 | B4 WC days change | NOT FOUND → 0 | FAIL MAJOR (F2) | FY24 91.4 to FY26 88.9 days, −2.4 → 3 |
| G17 | C1 revenue CAGR | 16.8% → 4 | PASS | |
| G18 | C2 PAT CAGR | 6.8% → 1 | PASS | |
| G19 | C3 positive YoY years | 7 of 9 → 3 | PASS | FY20, FY21 declined (screener line 11) |
| G20 | C4 PAT CAGR minus revenue CAGR | −10.1pp → 0 | PASS | |
| G21 | D1 net debt / EBITDA | 2.81x → 1 | PASS | |
| G22 | D2 EBIT / interest | 4.01x → 2 | PASS | |
| G23 | D3 debt / equity | 0.53 → 3 | PASS | |
| G24 | D4 current ratio | 1.26 → 2 | PASS | |
| G25 | E1 promoter holding | 74.49% → 5 | PASS | |
| G26 | E2 promoter change over 3 years | "window NOT evidenced", scored 3 | FAIL MAJOR (F4) | 0 under rule 5 |
| G27 | E3 pledge | 0% → 5 | PASS | |
| G28 | E4 contingent liabilities / net worth, declared consolidated basis | 7,133.72 L standalone / 34,650.78 L consolidated = 20.6% → 1 | FAIL CRITICAL (F1) | Consolidated Note 51: 445.72 L / 34,650.78 L = 1.29% → 5 (AR26 [page 241]) |
| G29 | M1 pricing power | −2.3pp margin, CAGR 16.8% → 1 | PASS | 10.23% FY17 to 7.92% FY26 (screener) |
| G30 | M2 cost advantage vs peer median | PEER DATA NEEDED → 0 | FAIL MAJOR (F5) | MMP 7.92% vs peer median 7.47% = +0.45pp → 1 |
| G31 | M3 capital efficiency | proxy ROCE 10.06% → 0 | FAIL MINOR (consequence of F3) | FAT 3.29x, fixed-formula FY26 ROCE 12.91% > 12% → 1 |
| G32 | M4 stickiness | 2 decline years → 1 | PASS | |
| G33 | M5 scale and dominance | PEER DATA NEEDED → 0 | FAIL MAJOR (F5) | Market cap rank 3 of 4, margin rank 2 → 3 |
| G34 | M6 R&D | 0 | PASS | No separate R&D (B07 cites AR26 p.44); 0 either way |
| G35 | M7 regulatory | listed-player count NOT FOUND → 0 | PASS | |
| G36 | M8 distribution | 0 | PASS | AR26 names no company dealer or distributor network; "distribution networks" at lines 2550, 2604, 2650 are power grids |
| G37 | M9 brand, GM proxy (Rev − RM) / Rev | PEER DATA NEEDED → 0 | FAIL MAJOR (F5) | 21.28% vs peer median 12.16% = +9.12pp, CAGR 16.8% → 3 |
| G38 | M10 switching costs | → 1 | PASS | |
| G39 | M11 network effects | → 1 | PASS | Latest 3y 15.25% < prior 3y 30.57%; selling 1.73% (FY23) to 1.94% (FY26), rising |
| G40 | M12 float | → 0 | PASS | WC days above 45 in all known years |
| G41 | Moat class from present count | 0 present → NONE | PASS on stated scores | |
| G42 | Classification matrix | core 39 < 40 → AVOID | PASS on stated core | |
| G43 | Data-confidence tier | 10 years, full, no downgrade | PASS | |
| G44 | Deal-breakers 1-9 tested, driving years stated | 1 and 2 recorded with years; 3-9 not triggered | PASS | |
| G45 | FLAG-GATE0 when ≤ AVERAGE with depressors | raised, years named | PASS | |
| G46 | B01 YAML block file carries all schema keys | 21 of 21 keys present | PASS | |
| G47 | Report ends with exactly the fenced YAML block | report ends with a 6-key stub and a pointer to the block file | FAIL MINOR (F7) | |
| G48 | Dashboard elements | all blocks, line items, moat table, classification box, strongest/weakest, decision line | PASS | Moat profile is a score table, not bars; same content |
| G49 | analyst_note ≤ 200 words | about 95 words | PASS | |
| G50 | data_notes carry swing, proxy bases, PEER DATA NEEDED | present | PASS | |

Gate 0: 50 checked, 38 PASS, 12 FAIL (76.0%).

---
## 3. GATE 0 RECOMPUTATION

### 3a. Corrections that hold under every reading
| Line | B01 | Recomputed | Basis |
| --- | --- | --- | --- |
| E4 | 1 | 5 | Declared consolidated basis; consolidated Note 51 = 445.72 L (AR26 [page 241]) |
| E2 | 3 | 0 | Rule 5; 3-year start point NOT FOUND |
| Core | 39 | 40 | AVERAGE, on the band floor |

### 3b. The rule 6 window question
Rule 6 reads: "Use whatever history is available: minimum 3 years, maximum whatever exists." It has two readings.
- Reading 1, per-metric window. Each metric uses the years its inputs exist, if 3 or more.
- Reading 2, full window. A metric whose inputs do not span the scorecard window is NOT FOUND and scores 0.

| Line | B01 as emitted | Reading 1 | Reading 2 |
| --- | --- | --- | --- |
| Block A | 4 (proxy ROCE) | 9 on the fixed formula FY24-FY26; 4 if the proxy is accepted | 2 (fixed formula NOT FOUND FY17-FY23); 4 if the proxy is accepted |
| Block B | 5 | 10 (capex incl. CWIP and capital advances) or 14 (PPE line only) | 5 |
| Block C | 8 | 8 | 8 |
| Block D | 8 | 8 | 8 |
| Block E | 14 | 15 | 15 |
| Core | 39 | 45 to 54 | 38 (proxy rejected) or 40 (proxy accepted) |
| Classification | AVOID | AVERAGE | AVOID or AVERAGE |
| Deal-breakers | 1, 2 | none with A = 9; only 1 with A = 4 (max GOOD, not binding at AVERAGE) | 1, 2 |
| Moat | 4/60, 0 present, NONE | 11-12/60, 2 present, MODERATE | 11-12/60, 2 present, MODERATE |

The text supports Reading 1, for three reasons.
1. Rule 6 sets a floor of 3 years and a ceiling of "whatever exists". It does not require every metric to span the same years.
2. The confidence tiers score a company with 3-4 years and downgrade it one tier. A rule that scores a 3-year company but zeroes a 10-year company with the same 3 years of capex data contradicts that design.
3. B01 rejected Reading 2 itself, twice. It used a proxy to get a 10-year ROCE series (G03). It scored E2 on 21 months (G26).

Residual point for the operator. Under Reading 1 the confidence tier stays "10 years, full". Rule 6 keys the tier to "Data available: [X] years", the scorecard history. If the operator keys the tier to the shortest scored window instead (3 years, LIMITED), AVERAGE downgrades one tier to AVOID.

What separates the readings: an operator ruling on the scope of rule 6 (per metric or full window) and on whether a disclosed ROCE proxy is admissible when the fixed formula's inputs are absent. F1 does not depend on that ruling.

Economic caveat, not a scoring input. Under Reading 1 the Block B lift rests on reported CFO. Reported CFO carries short-term borrowing inflows of 26.78 Cr in FY24 (AR25 [page 156], line 8721), 44.26 Cr in FY25 (same line) and 17.23 Cr in FY26 (AR26 [page 173], line 9448). If those lines moved to financing, FY24-FY26 FCF on the PPE line would be −14.81, −37.22 and −3.17 Cr, and B2 and B3 would return to 0. Prompt 01 rule 2 bars that reclassification inside the scorecard. B01's FLAG-CASH already carries it.

---
## 4. EMERGING MOAT COMPLIANCE TABLE (B07)

| # | Rule (prompt 07) | B07 value | Verdict | Note (anchor) |
| --- | --- | --- | --- | --- |
| E01 | Six sections in one response | Sections 1-6 plus register present | PASS | |
| E02 | 1A: status from the set, evidence type, date, revenue potential, difference | 11 rows | PASS | Statuses LAUNCHED-recent, IN TRIALS, ANNOUNCED, UNDER DEVELOPMENT, CONCEPT, LAUNCHED |
| E03 | 1B direction with evidence and timeline | 5 rows | PASS | |
| E04 | 1C mix table | 3-year % stated NOT FOUND, not filled | PASS | |
| E05 | 2A capex table | 8 rows | PASS | |
| E06 | 2B utilisation | 5 facilities | PASS | |
| E07 | 2C capex under execution x historical FAT, % of revenue, arithmetic shown | 52.5 x 3.196 = 167.8 Cr = 20.4% of 824.0 Cr | PASS | Recomputed FAT mean 3.196x and 20.36%. See observation O2. |
| E08 | 2D new geographies | present | PASS | |
| E09 | 22 categories, each with evidence table or NO EVIDENCE FOUND | 22 of 22 | PASS | |
| E10 | Taxonomy tag on every evidence item | tagged | PASS | |
| E11 | Source anchor (AR p., call, slide) on every evidence item | several items anchor to upstream blocks; one unanchored | FAIL MINOR (F8) | |
| E12 | Never force-fit | sparse scan, 9 rows scored | PASS | See observation O1 on G2 |
| E13 | One improvement, one mechanism | ADD in R1 only; FRP in B1 only; AVL in H2 only | PASS | |
| E14 | Section 3 summary: 22 rows, evidence, type, strength, time | present | PASS | |
| E15 | Strong/Moderate count stated | 3 Moderate, 0 Strong | PASS | |
| E16 | Recount line in the mandated form, arithmetic correct | "11 documented items across 7 categories" | PASS | 2+1+3+1+2+1+1 = 11 across B1, B2, E2, F2, H2, H3, R1 |
| E17 | Completionist guard at 12 or more active | 9 active | PASS | |
| E18 | 4A approvals pipeline | present | PASS | |
| E19 | 4B policy tailwinds, shared or not | present | PASS | |
| E20 | 4C regulatory moat assessment | present, score stated | PASS | |
| E21 | Section 5: all 23 rows | 23 rows | PASS | |
| E22 | Likelihood x impact matrix values | 9 scored rows checked | PASS | MM 2, ML 1, LL 1, HL 2 |
| E23 | Evidence multipliers 1.0 / 0.7 / 0.5 | applied | PASS | B2 mixed evidence scored at 0.7, the lower tier |
| E24 | No claim-only or inference-only row scored at documented weight | none found | PASS | E1 0.7 (claim), G2 0.5 (inference) |
| E25 | Adjusted total | 11.6 | PASS | 2.0+1.4+0.7+2.0+1.0+0.5+2.0+1.0+1.0 = 11.6 |
| E26 | Band | below 12 → NONE | PASS | |
| E27 | I1/I2 contribution stated separately | 0.0 | PASS | |
| E28 | Category 21 (I1) present; above 0 only with both legs and a documented (b) leg | present, 0 | PASS | |
| E29 | Category 22 (I2) present; above 0 only with a specific named sacrifice | present, 0 | PASS | |
| E30 | I2 test run "for each moat claimed anywhere in this scan" | 4 moats tested; E2 and H2 not tested | FAIL MINOR (F9) | Score 0 survives |
| E31 | Optionality register: table and YAML; rows scored 0 or claim/inference only; never scored | 8 rows | PASS | |
| E32 | 6A-6E present; 6C uses the injected Gate 0 block | core 39, moat 4/60, 0 confirmed, NONE, AVOID | PASS | Inputs carry the B01 errors (Section 5) |
| E33 | 6D: HIGH POTENTIAL and TURNAROUND reasoning in full | both tested, both fail with reasons | PASS | |
| E34 | B07 YAML schema | all keys present; one extra key (no_concall_mode) | PASS | |
| E35 | active_categories only Strong/Moderate; capex_embedded_growth_pct equals 2C headline | B1, E2, H2; 20.4 | PASS | |
| E36 | analyst_note ≤ 200 words; scan kept separate from FTTCP | about 162 words; "It is not FTTCP" | PASS | |

Emerging Moat: 36 checked, 34 PASS, 2 FAIL (94.4%).

Observations (no fail):
- O1. G2 (WC trajectory) scores 0.5 on one year of data. AR25 adds FY24. WC days run 91.4 (FY24), 104.1 (FY25), 88.9 (FY26). That is a round trip, not a trajectory. Without G2 the total is 11.1, still NONE. B07 flagged the row itself in FLAG-BORDERLINE-BAND.
- O2. 2C case A counts the 7 MW solar park (Rs 30 Cr) as "committed and in execution". Its 2A status is a claim: "land acquired; no contract disclosed". AR26 consolidated Note 52 ([page 241], lines 13319-13327) shows capital commitments of 5,642.27 L, which fits Rs 50-55 Cr committed but names no project. Without solar, case A is wire rod 20-25 Cr x 3.196 = 63.9-79.9 Cr, 7.8-9.7% of 824.0 Cr. B07 labels 20.4% an upper bound and states the quality adjustment. Disclosed, so no fail.
- O3. B2 shows "Weak" in the Section 3 summary but takes raw MM = 2 in Section 5, the same raw score as the Moderate rows. The 0.7 multiplier brings it to 1.4. No rule maps strength to raw score. Noted for consistency only.

---
## 5. INHERITED EFFECTS ON B07 (not B07 misapplications)

B07 applied prompt 07 correctly to the Gate 0 block it received. Three B07 outputs rest on the B01 errors.
- 6C reads core 39, moat 4/60, 0 moats confirmed, NONE, AVOID. Recomputed B01: core 40 to 54, AVERAGE, 2 moats present (M5, M9), MODERATE.
- 6D combined_assessment "AVOID" and combined_reasoning ("Gate 0 core 39 (AVOID...") no longer follow. Stage 7 must re-derive 6D on the corrected block. The forward score (11.6, NONE) does not change. The TURNAROUND and HIGH POTENTIAL tests rest on forward evidence and stand as written.
- 6E "Existing (Gate 0)" shows "none" in every family. M5 (scale) and M9 (gross-margin proxy) would show as existing, with the four-name peer-set caveat in F5.

---
## 6. FINDINGS

### F1. CRITICAL. E4 scored on a standalone note against a consolidated net worth
- Rule: prompt 01 Block E, E4 "Contingent liabilities ÷ Net Worth (latest)"; rule 5 "confirm it exists in the provided data".
- B01 declares "Basis: consolidated" (01-gate0.md line 4). E4 uses standalone Note 47: 7,133.72 L (AR26 [page 157], Annual_Report_2026.txt lines 8459-8472). That total includes corporate guarantees for two wholly owned subsidiaries, MMP Electricals 3,400.00 L and MMP Cables 3,288.00 L. B01 divides it by consolidated net worth 34,650.78 L and states "no separate consolidated note found" (B01-gate0.yaml data_notes).
- Source: the consolidated statements carry Note 51 Contingent Liabilities (AR26 [page 241], lines 13308-13318). Bank guarantees 445.72 L. Total 445.72 L at 31-Mar-2026.
- Recomputed: 445.72 / 34,650.78 = 1.29%. Band below 5% = 5.
- Why the basis matters: the subsidiary loans the guarantees cover already sit in consolidated borrowings, which D1 and D3 score. The standalone figure counts the same debt twice.
- Effect: Block E 14 to 18. Core 39 to 43. Classification AVOID to AVERAGE. This holds under both readings in Section 3b. B07 combined_assessment inherits the change.
- Fix: stage 1 re-scores E4 on Note 51.

### F2. MAJOR. B2, B3, B4 marked NOT FOUND while three years of inputs sit in the corpus
- Rule: prompt 01 rule 5 (confirm in the provided data) and rule 6 (use whatever history is available, minimum 3 years).
- B01 input_gaps: "no 10-year capex line and no trade payables before FY25 in corpus". The corpus holds inputs/annual-report/Annual_Report_2025.txt.
- Source: AR25 consolidated cash flow ([page 156], lines 8693-8739): FY24 CFO 4,275.02 L; investment in PPE 3,078.11 L; CWIP increase 1,285.85 L; capital advances +131.62 L. AR25 consolidated balance sheet ([page 154], lines 8518-8573): FY24 trade payables 700.31 + 1,624.13 = 2,324.44 L; receivables 5,706.17 L; inventories 11,099.96 L. AR25 P&L ([page 155]): FY24 revenue 57,854.35 L. FY25 from AR25 [page 156]. FY26 from AR26 [page 173], lines 9455-9461 (CFO 5,328.97 L; PPE 3,923.03 L; CWIP 991.83 L; capital advances 663.86 L).
- Recomputed (Rs Cr; cumulative PAT FY24-FY26 = 31.64 + 38.88 + 31.01 = 101.53, screener line 24):

| Capex reading | FY24 FCF | FY25 FCF | FY26 FCF | B2 | Cum FCF / PAT | B3 |
| --- | --- | --- | --- | --- | --- | --- |
| PPE line only (the line B01 itself used) | 11.97 | 7.04 | 14.06 | 3 of 3 → 5 | 33.07 / 101.53 = 0.33 → 1 | 1 |
| PPE + CWIP + capital advances | 0.43 | 4.76 | −2.50 | 2 of 3 → 2 | 2.69 / 101.53 = 0.03 → 0 | 0 |

  B4: FY24 receivable 36.0 + inventory 70.0 − payable 14.7 = 91.4 days (revenue basis). FY26 88.9 days (B01). Change −2.4 days, within ±5 → 3.
- Effect: Block B 5 to 14 or 10. Under Reading 1, this finding alone gives core 48 or 44, AVERAGE. Under Reading 2 the zeros stand. Graded MAJOR because the score effect depends on the rule 6 reading. The input_gaps statement is wrong under both readings.
- Cause not visible here: stage 1 may not have received AR25 as an input. B07 (stage 7) cites "AR25 p.18", so AR25 was in the corpus by stage 7. The fix is the same either way.
- Fix: re-run stage 1 with AR25 injected.

### F3. MAJOR. ROCE computed on a substituted formula
- Rule: prompt 01 FORMULA DEFINITIONS, "fixed, do not substitute alternatives". ROCE = EBIT / (Total Assets − Current Liabilities).
- B01 used EBIT / (equity + reserves + borrowings) for all 10 years and disclosed it as a proxy. The proxy keeps short-term borrowings inside capital employed; the fixed formula removes them with the other current liabilities.
- Fixed formula where inputs exist: FY24 46.81 / (435.00 − 117.39) = 14.74% (EBIT screener lines 21-22; total assets 43,500.03 L and current liabilities 11,738.68 L, AR25 [page 154]). FY25 16.31% and FY26 12.91% (B01 cross-check, AR26 p.171).
- Reading 1: A1 median 14.74% → 1; A2 minimum 12.91% → 3; A3 → 2; A4 decline 1.83pp → 3. Block A 4 to 9. M3: FAT 3.29x and FY26 ROCE 12.91% above 12% → 1 (G31).
- Reading 2: the fixed formula is NOT FOUND for FY17-FY23. A1, A2, A4 score 0. Block A 4 to 2.
- Effect: from −2 to +5 on core, depending on the reading. The breach holds under both readings.
- Fix: operator ruling on proxy admissibility; then stage 1 applies it.

### F4. MAJOR. E2 scored 3 on a window B01 itself calls not evidenced
- Rule: prompt 01 E2 "change over 3 years"; rule 5 "NOT FOUND ... score it 0".
- B01: "Three-year window NOT evidenced", scored ±1% = 3 on 30-Sep-2024 to 30-Jun-2026 (21 months, SHP_MMP_2026-06-30.md lines 8-15) plus an unchanged share count.
- Source: AR25 Note 16(d) ([page 112], Annual_Report_2025.txt lines 6070-6093) adds 31-Mar-2024: 1,89,20,779 promoter shares, 74.48%. The window grows to 27 months. The start point (mid-2023) stays NOT FOUND.
- Recomputed: 0.
- Consistency: B01 applied NOT FOUND → 0 to B2-B4 and not to E2.
- Effect: Block E −3. Alone: core 36, AVOID stands. With F1: core 40, AVERAGE.

### F5. MAJOR. Peer tests scored PEER DATA NEEDED while three peer Data_Sheets sit in the corpus
- Rule: prompt 01 Block F, "If a test needs peer data that is not provided, score 0".
- B01 input_gaps: "no peer data (M2, M5, M6, M9 PEER DATA NEEDED)". inputs/screening/ holds APARINDS-, ARFIN- and MAANALU-Data_Sheet.csv beside the MMP sheet.
- FY26 values (each sheet: market cap line 8; sales line 11; raw material line 12; other income, depreciation, interest, PBT lines 19-22):

| Company | Market cap Cr | EBITDA margin | GM proxy (Rev − RM) / Rev |
| --- | --- | --- | --- |
| MMP | 1,142.1 | 7.92% | 21.28% |
| APAR Industries | 73,896.3 | 8.39% | 17.92% |
| Arfin India | 1,472.1 | 7.47% | 12.16% |
| Maan Aluminium | 595.89 | 2.49% | 10.97% |
| Peer median (3) | | 7.47% | 12.16% |

- Recomputed: M2 +0.45pp, within ±2pp → 1. M5 market cap rank 3 of 4 (top 3) and margin rank 2 → 3. M9 +9.12pp (≥5pp) with revenue CAGR 16.8% (≥8%) → 3. M6 stays 0 (no R&D).
- Effect: moat score 4 to 11 (proxy ROCE) or 12 (fixed-formula ROCE, F3). Moats present 0 to 2. Class NONE to MODERATE. The classification does not change: below core 60 the matrix ignores the moat class.
- Caveat on M5: the set has four names. A top-3 market cap rank needs only that MMP is not the smallest. APAR's market cap is 65x MMP's. M5 = 3 is mechanical and rests on the peer list the pipeline chose.
- Cause not visible here: the sheets may not have been injected into stage 1. The fix is the same.
- Fix: re-run stage 1 with the peer sheets injected.

### F6. MINOR. Inline anchors missing on some Gate 0 lines
- Rule: prompt 01 rule 4.
- C1-C4 lines (01-gate0.md lines 42-45), the M3 FAT figure and the M11 CAGRs carry no inline anchor. The block header names screener-data, so the source is traceable.
- No score effect.

### F7. MINOR. The Gate 0 report does not end with the full YAML block
- Rule: prompt 01 OUTPUT, "end with exactly this fenced YAML block".
- 01-gate0.md lines 86-96 hold a 6-key stub that points to outputs/blocks/B01-gate0.yaml. The block file is complete (G46).
- No score effect.

### F8. MINOR. Some B07 evidence anchors cite upstream blocks, not source pages
- Rule: prompt 07 rule 3, "SOURCE ANCHORS on every evidence item: (AR p.__), (Q_ FY__ call), (Inv. Pres. slide __)".
- Examples: G1 "CFO net of borrowing and payables Rs 16.96 Cr (B03)"; G2 "Payable days rose 17.8 to 24.8 (B03)" and "WC days 104.1 to 88.9 (B01)"; B2 "PGCIL approval pending, slipped three times (B05)"; 1A AL59 "conductor revenue 171 Mn, -42% YoY (B05)". E1 "central-India location" has no anchor. F2 cites B05 by design (prompt 07 F2 text), so F2 is exempt.
- No score effect.

### F9. MINOR. I2 test skips two of the three Moderate moats
- Rule: prompt 07 I2, "For each moat claimed anywhere in this scan, answer: what SPECIFIC thing would the best-resourced competitor have to destroy".
- The I2 table tests polymer insulators, powders, foils and wire rod. It omits E2 (exports) and H2 (AVL, Toyal). H2's four-decade AVL tie is the "decades-old relationship" case the second I2 direction names, so the test was owed.
- Score 0 survives: no specific sacrifice is named, and no documented competitor evidence exists for the top band.

---
## 7. VALUATION AUDIT: PENDING PHASE 3

Rules 4 (valuation half), 5 (valuation half), 6, 7, 9 to 15 of the Verifier C section are not run. B10 and B11 do not exist. The valuation framework documents were not loaded, as the phase-1 scope requires. The valuation, expectation_ledger and business-narrative fields in B12c are marked "pending phase 3".

---
## 8. NOTES FOR THE ORCHESTRATOR

- Acceptance 83.7% on a denominator of 86. The REWORK rate trigger does not fire. A Verifier C CRITICAL does not by itself trigger REWORK under the stage 12 header.
- Fix path: re-run stage 1 on the full corpus (AR25 and the three peer Data_Sheets injected), with E4 on consolidated Note 51 and E2 at NOT FOUND = 0. Then re-derive B07 6C to 6E on the new block. B07 Sections 1 to 5 and the register stand.
- Operator rulings needed before the stage 1 re-run settles the core: (a) rule 6 scope, per metric or full window; (b) admissibility of the disclosed ROCE proxy; (c) whether the confidence tier keys to scorecard history or to the shortest scored window. Under the reading this verifier judges the text supports (Reading 1, tier on scorecard history), the class is AVERAGE with core 45 to 54.
- Verifier A owns the existence of AR26 Note 51 (445.72 L), the AR25 FY24 lines and the peer-sheet values used here. This report used them only for basis and availability.

```yaml
stage: B12c
company: "MMP"
run_date: "2026-10-05"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete
scope: "phase 1: gate0 (B01) + emoat (B07) only; valuation half pending phase 3"
gate0:
  rules_checked: 50
  fails:
    - "G28 E4 CRITICAL (F1): standalone note 47 7,133.72 L over consolidated NW 34,650.78 L = 20.6% -> 1; consolidated Note 51 = 445.72 L (AR26 [page 241]) -> 1.29% -> 5; core 39 -> 43; AVOID -> AVERAGE under every reading"
    - "G14 B2, G15 B3, G16 B4 MAJOR (F2): FY24 capex and payables in AR25 [page 154], [page 156]; FY24-FY26 meets the rule 6 3-year minimum; B2 5 or 2, B3 1 or 0, B4 3; Block B 5 -> 14 or 10"
    - "G03 ROCE formula MAJOR (F3): equity+reserves+borrowings proxy replaces fixed EBIT/(TA-CL); fixed formula FY24-FY26 = 14.74 / 16.31 / 12.91%; Block A 4 -> 9 (per-metric window) or 2 (full window)"
    - "G31 M3 MINOR (consequence of F3): FY26 fixed-formula ROCE 12.91% > 12%, FAT 3.29x -> 1"
    - "G26 E2 MAJOR (F4): 3-year start point NOT FOUND (21 months SHP; 27 months with AR25 note 16(d) [page 112]); rule 5 -> 0, not 3"
    - "G30 M2, G33 M5, G37 M9 MAJOR (F5): three peer Data_Sheets in inputs/screening; M2 1, M5 3, M9 3; moats present 0 -> 2; NONE -> MODERATE; moat score 4 -> 11 or 12"
    - "G02 MINOR (F6): C1-C4, M3, M11 lines lack inline anchors"
    - "G47 MINOR (F7): 01-gate0.md ends with a 6-key stub, not the full block"
  recomputed_core: "40 to 54 (AVERAGE); 38 (AVOID) only under the full-window reading with the ROCE proxy also rejected"
  recomputed_classification: "AVERAGE"
  recomputed_moat: "11 or 12/60, 2 present (M5, M9), MODERATE"
  operator_rulings_needed: "rule 6 scope (per metric vs full window); ROCE proxy admissibility; confidence tier keyed to scorecard history vs shortest scored window"
emoat:
  rules_checked: 36
  fails:
    - "E11 MINOR (F8): evidence anchored to upstream blocks B01/B03/B05 in G1, G2, B2, 1A; E1 central-India location unanchored"
    - "E30 MINOR (F9): I2 test omits E2 and H2 (2 of 3 Moderate moats); I2 = 0 survives"
  em_score_concur: true  # 11.6, NONE
  inherited_from_b01: "6C/6D/6E rest on B01 AVOID and 0 moats; combined_assessment AVOID must be re-derived after the stage 1 re-run; not a B07 misapplication"
valuation: {rules_checked: 0, fails: [], status: "pending phase 3"}
expectation_ledger: {status: "pending phase 3", present: false, downside_row: false, all_rows_confirm_by: false, all_rows_metric_threshold: false, prob_in_range: false, decay_status_valid: false, off_ledger_credit: false, residual_pct_cmp: 0, residual_starter_cap_ok: true, fails: []}  # rules 13-14; any fail = REWORK stage 11
business_understanding_narrative: {status: "pending phase 3", present: false, five_questions: false, prose_only: false, downstream_refs_ok: false, no_valuation_vocab: false, fails: []}  # rule 9; any fail = REWORK stage 13
recomputed_destination_pe: ""  # pending phase 3
recomputed_decision: ""        # pending phase 3; Gate 0 class recomputation is in gate0.recomputed_classification
findings:
  - id: F1
    framework: gate0
    rule: "E4 on the declared consolidated basis (prompt 01 Block E; rule 5)"
    severity: CRITICAL
    claimed: "7,133.72 L standalone Note 47 (AR26 [page 157]) / 34,650.78 L = 20.6% -> 1; 'no separate consolidated note found'"
    recomputed: "445.72 L consolidated Note 51 (AR26 [page 241], lines 13308-13318) / 34,650.78 L = 1.29% -> 5"
    effect: "Block E 14 -> 18; core 39 -> 43; AVOID -> AVERAGE under every reading; B07 combined_assessment inherits"
    fix: "stage 1 re-scores E4 on Note 51"
  - id: F2
    framework: gate0
    rule: "B2/B3/B4 NOT FOUND vs available history (prompt 01 rules 5, 6)"
    severity: MAJOR
    claimed: "capex and payables before FY25 not in corpus; B2 0, B3 0, B4 0"
    recomputed: "AR25 [page 154]-[page 156] gives FY24; FCF FY24/FY25/FY26 = 11.97/7.04/14.06 Cr (PPE line) or 0.43/4.76/-2.50 Cr (PPE+CWIP+capital advances); B2 5 or 2; B3 1 (0.33) or 0 (0.03); B4 FY24 91.4 -> FY26 88.9 days = 3"
    effect: "Block B 5 -> 14 or 10; alone core 48 or 44 (AVERAGE) under the per-metric reading; nil under the full-window reading"
    fix: "re-run stage 1 with AR25 injected"
  - id: F3
    framework: gate0
    rule: "ROCE fixed formula, no substitutes (prompt 01 FORMULA DEFINITIONS)"
    severity: MAJOR
    claimed: "EBIT/(equity+reserves+borrowings), 10 years; A1 1, A2 1, A4 0; M3 0"
    recomputed: "fixed formula FY24 14.74% (AR25 [page 154]), FY25 16.31%, FY26 12.91%; per-metric reading A1 1, A2 3, A4 3 = Block A 9, M3 1; full-window reading A1/A2/A4 NOT FOUND = Block A 2"
    effect: "core -2 to +5 depending on the rule 6 reading"
    fix: "operator ruling on proxy admissibility, then stage 1"
  - id: F4
    framework: gate0
    rule: "E2 3-year change; NOT FOUND scores 0 (prompt 01 rule 5)"
    severity: MAJOR
    claimed: "window NOT evidenced, scored 3"
    recomputed: "0; holdings known 31-Mar-2024 (AR25 note 16(d) [page 112]) to 30-Jun-2026 (SHP), 27 months"
    effect: "Block E -3; alone core 36 (AVOID); with F1 core 40 (AVERAGE)"
    fix: "stage 1 scores E2 NOT FOUND = 0"
  - id: F5
    framework: gate0
    rule: "peer tests scored 0 only when peer data is not provided (prompt 01 Block F)"
    severity: MAJOR
    claimed: "M2, M5, M9 PEER DATA NEEDED = 0; moats present 0; NONE"
    recomputed: "peer sheets APARINDS/ARFIN/MAANALU: EBITDA median 7.47% vs MMP 7.92% -> M2 1; mcap rank 3 of 4, margin rank 2 -> M5 3; GM proxy 21.28% vs median 12.16% -> M9 3"
    effect: "moat 4 -> 11 or 12/60; present 0 -> 2; NONE -> MODERATE; classification unchanged (core below 60); M5 rests on a four-name peer set"
    fix: "re-run stage 1 with peer sheets injected"
  - id: F6
    framework: gate0
    rule: "anchor after every extracted number (prompt 01 rule 4)"
    severity: MINOR
    claimed: "C1-C4, M3, M11 without inline anchors"
    recomputed: "no score change"
    effect: "none"
    fix: "add (screener-data) per line"
  - id: F7
    framework: gate0
    rule: "report ends with exactly the fenced YAML block (prompt 01 OUTPUT)"
    severity: MINOR
    claimed: "6-key stub plus pointer"
    recomputed: "block file complete, 21 of 21 keys"
    effect: "none"
    fix: "paste the full block at the end of 01-gate0.md"
  - id: F8
    framework: emoat
    rule: "source anchor on every evidence item (prompt 07 rule 3)"
    severity: MINOR
    claimed: "G1, G2, B2, 1A items anchored to B01/B03/B05; E1 location unanchored"
    recomputed: "no score change"
    effect: "none"
    fix: "replace block anchors with source pages"
  - id: F9
    framework: emoat
    rule: "I2 test for each moat claimed (prompt 07 I2)"
    severity: MINOR
    claimed: "I2 table tests insulators, powders, foils, wire rod"
    recomputed: "E2 and H2 untested; I2 stays 0 (no specific sacrifice, no documented competitor evidence)"
    effect: "none"
    fix: "add E2 and H2 rows to the I2 table"
critical_count: 1
major_count: 4
minor_count: 4
acceptance_rate: 83.7             # rules passed / rules checked, %: (38 + 34) / (50 + 36)
```
