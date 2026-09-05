# VERIFIER C: FRAMEWORK ADHERENCE (PHASE 1) — PITTIENG
Run: runs/pittieng-2026-09-05 | Run date 2026-09-05 | Model: opus

## SCOPE

Phase 1 only. Two audits run here.

- Gate 0 (B01) against prompts/01-gate-0-pipeline.md. Rubric rule 2.
- Emerging Moat (B07) against prompts/07-emerging-moat-pipeline.md. Rubric
  rules 3 and 8.

Deferred, not run in this pass:
- Rule 4, 5, 7, 11, 12 (valuation adherence, B10/B11). Phase 3.
- Rule 6 (B09 downstream candidates). B09 is not an input here.
- Rule 9 (stage 13 Business Understanding Narrative). Not written yet.
- Rule 10 (Halt 1 dossier B09b). Not written yet.

No frameworks/ document was loaded. Phase 1 rule sources only.

Boundary respected: I audit rule application. I do not audit company
quality. I do not audit whether a number exists in a source PDF. That is
Verifier A's sole and non-overridable authority. Where a finding below
touches a figure, it concerns the BASIS or the FORMULA the maker applied,
not the existence of the number.

Inputs read:
- /home/user/inflection-pipeline/prompts/01-gate-0-pipeline.md
- /home/user/inflection-pipeline/prompts/07-emerging-moat-pipeline.md
- /home/user/inflection-pipeline/runs/pittieng-2026-09-05/outputs/reports/01-gate0.md
- /home/user/inflection-pipeline/runs/pittieng-2026-09-05/outputs/blocks/B01-gate0.yaml
- /home/user/inflection-pipeline/runs/pittieng-2026-09-05/outputs/reports/07-emoat.md
- /home/user/inflection-pipeline/runs/pittieng-2026-09-05/outputs/blocks/B07-emoat.yaml

Method: every Block A to F score was re-derived from the inputs the report
itself states, against the thresholds in the prompt. Every Emerging Moat
row was re-multiplied from its stated raw score and evidence tier, and the
adjusted total was re-added.

Headline: 137 rules checked, 126 pass, 11 fail. Acceptance 92%. No
CRITICAL. Three MAJOR. The AVERAGE classification and the MODEST emerging
moat classification both survive every recomputation below.

---

## PART 1: GATE 0 (B01) COMPLIANCE TABLE

Rule source: prompts/01-gate-0-pipeline.md.

### 1.1 Operating rules and formula definitions

| # | Rule | Verdict | Recomputed value / note |
|---|---|---|---|
| 1 | OR1: entire scorecard in one response, no stops | PASS | All six blocks plus classification present |
| 2 | OR3: show every number extracted and its score | PASS | Every sub-metric shows inputs and band |
| 3 | OR4: source anchor on every extracted number | PASS | Anchors present throughout, screener/AR convention declared up front |
| 4 | OR5: unavailable data marked N/A and scored 0, no estimates | PASS | E2 and E3 marked "N/A (not in provided data)", scored 0. M5 marked PEER DATA NEEDED, scored 0. No industry-typical fills found |
| 5 | OR6: open with the data-available statement, use available history | PASS | Opens with "Data available:" and states the three overlapping windows and the adaptation |
| 6 | Formula: ROCE = EBIT / (Total Assets − Current Liabilities); use source's own ROCE where given, else compute and state "computed" | **FAIL** | FY21 substitutes an alternative capital-employed basis (Net Worth + Total Borrowings). Formula block is declared "fixed, do not substitute alternatives". See G-01. Recomputed on the AR-basis series alone: A4 = 1, Block A = 11/20 |
| 7 | Formula: ROE = PAT / average net worth; closing for earliest year if opening absent, and say so | PASS | FY21 uses closing net worth, stated |
| 8 | Formula: WC Days = Receivable + Inventory − Payable days; state the basis used | PASS | Revenue basis used for all three legs and stated |
| 9 | Formula: FCF = CFO − capex (PPE + intangibles from the cash flow statement, exclude acquisitions) | **FAIL** | FY22 to FY24 capex is a Δ(Net Block+CWIP)+Depreciation proxy, not the cash flow line. Disclosed. Re-derived strictly on FY25-FY26 only: B2 = 2, B3 = 0, unchanged. See G-03 |
| 10 | Formula: CAGR = (End/Start)^(1/years) − 1 | PASS | C1 re-derived 24.05%, C2 re-derived 37.93%. Six periods over seven data points, exponent correct |
| 11 | CAGR edge: negative or zero endpoint = N/M, score 0 | PASS | No endpoint negative or zero. Rule not engaged, correctly |
| 12 | CAGR edge: loss-to-profit swing noted in data_notes | PASS | data_notes item 8 records the check and its negative result |
| 13 | CAGR edge: C4 = 0 when PAT CAGR is N/M | PASS | Not engaged. PAT CAGR is a real number |

### 1.2 Block A, Return on Capital (max 20)

Series used by the maker: 12.32 / 13.75 / 16.07 / 17.19 / 17.28 / 18.39.

| # | Metric | Threshold applied | Verdict | Recomputation |
|---|---|---|---|---|
| 14 | A1 median ROCE 16.63% | 15-19.9 = 3 | PASS | Median of six = (16.07+17.19)/2 = 16.63. Score 3 confirmed |
| 15 | A2 minimum single-year ROCE 12.32% | 12-14.9 = 3 | PASS | Score 3 confirmed. Also 3 if FY21 is dropped (min becomes 13.75) |
| 16 | A3 median ROE 18.44% | 15-19.9 = 4 | PASS | Median of six = (17.83+19.04)/2 = 18.435. Score 4 confirmed |
| 17 | A4 ROCE latest vs earliest | latest >= earliest = 5 | PASS (band applied correctly to the stated series) | 13.75 >= 12.32, so 5 is right FOR THAT SERIES. The series itself fails rule 6. See G-01 |
| 18 | Block A total | sum | PASS | 3+3+4+5 = 15 confirmed |

### 1.3 Block B, Cash Generation Quality (max 20)

| # | Metric | Threshold applied | Verdict | Recomputation |
|---|---|---|---|---|
| 19 | B1 cumulative CFO/PAT 1.95 | >=1.00 = 5 | PASS | CFO sum 915.25, PAT sum 469.26, ratio 1.950. Score 5 confirmed. Also 5 on the FY22-26 window (2.006) |
| 20 | B2 FCF-positive years 3 of 5 = 60% | 50-74 = 2 | PASS | Score 2 confirmed |
| 21 | B3 cumulative FCF/PAT −0.096 | negative = 0 | PASS | FCF sum −42.40, PAT sum 440.50. Score 0 confirmed |
| 22 | B4 WC days +13.46 | increased 5-15 = 1 | PASS | 54.85 to 68.31 re-derived from the stated day counts. Score 1 confirmed. Two-year window is a corpus limit, disclosed |
| 23 | Block B total | sum | PASS | 5+2+0+1 = 8 confirmed. Deal-breaker 2 edge handled correctly (8 is not < 8) |

### 1.4 Block C, Growth (max 20)

| # | Metric | Threshold applied | Verdict | Recomputation |
|---|---|---|---|---|
| 24 | C1 revenue CAGR 24.06% | >=20 = 5 | PASS | Re-derived 24.05%. Score 5 confirmed |
| 25 | C2 PAT CAGR 37.95% | >=20 = 5 | PASS | Re-derived 37.93%. Score 5 confirmed |
| 26 | C3 positive YoY years 5 of 6 = 83.3% | 75-99 = 3 | PASS | Score 3 confirmed |
| 27 | C4 PAT CAGR minus revenue CAGR +13.89pp | >=+3pp = 5 | PASS | Score 5 confirmed |
| 28 | Block C total | sum | PASS | 5+5+3+5 = 18 confirmed |

### 1.5 Block D, Balance Sheet Strength (max 20)

| # | Metric | Threshold applied | Verdict | Recomputation |
|---|---|---|---|---|
| 29 | D1 net debt/EBITDA 1.75x | 1-2x = 3 | PASS | Score 3 confirmed on the stated primary basis. The basis choice itself is a discretionary call the framework does not define. See G-05 |
| 30 | D2 interest coverage 3.01x | 3-4.9 = 2 | **FAIL** | EBIT here includes other income (250.99) while D1's EBITDA excludes it (315.75). On the consistent exclude-other-income basis, EBIT = 211.09 and IC = 2.53x, band 1.5-2.9 = **1**, Block D = **9/20**. See G-02 |
| 31 | D3 debt/equity 0.708x (0.821x alt) | 0.5-1.0 = 3 | PASS | Both bases in the same band. Score 3 confirmed |
| 32 | D4 current ratio 1.403x | 1.2-1.49 = 2 | PASS | 90,531.52 / 64,542.36 = 1.4027. Score 2 confirmed |
| 33 | Block D total | sum | PASS (arithmetic) | 3+2+3+2 = 10 as stated. 9 under the D2 recomputation |

### 1.6 Block E, Shareholder Alignment (max 20)

| # | Metric | Threshold applied | Verdict | Recomputation |
|---|---|---|---|---|
| 34 | E1 promoter holding 54.18% | 50-59.9 = 4 | PASS | Score 4 confirmed |
| 35 | E2 promoter holding 3-year change | N/A = 0 per OR5 | PASS | Correct refusal. A one-year flat reading exists but the metric requires three years. The maker did not score the shortcut |
| 36 | E3 promoter pledge | N/A = 0 per OR5 | PASS | Correct refusal. Search evidence stated. CARO pledge mention correctly rejected as a different disclosure |
| 37 | E4 contingent liabilities / net worth 7.60% | 5-15 = 3 | PASS | 74.99/986.90 = 7.598%. Score 3 confirmed |
| 38 | Block E total | sum | PASS | 4+0+0+3 = 7 confirmed |

### 1.7 Block F, Quantitative Moat Scoring (max 60)

| # | Test | Threshold applied | Verdict | Recomputation |
|---|---|---|---|---|
| 39 | M1 margin +1.71pp, rev CAGR 24.06% | stable +/-2pp AND CAGR >=10% = 3 | PASS | +1.71 is inside +/-2pp. Score 3 confirmed. The 5-band needs >=2pp expansion, correctly denied |
| 40 | M2 16.51% vs peer median 16.43% | +/-2pp = 1 | PASS | Peer median of two = 16.43. Delta +0.08pp. Score 1 confirmed |
| 41 | M3 FAT 1.66x, ROCE 13.75% | FAT>1x AND ROCE>12% = 1 | PASS | Score 1 confirmed. The 3-band needs FAT>2x AND ROCE>15%, both fail |
| 42 | M4 one decline year, recovered | max 1 decline year, fully recovered = 3 | PASS | Score 3 confirmed. Rationale text misstates which leg of the 5-band fails. See G-07 |
| 43 | M5 peer set incomplete | PEER DATA NEEDED = 0 | PASS | Exactly the rule's instruction. No peer figure guessed |
| 44 | M6 R&D Nil | else = 0 | PASS | Score 0 confirmed |
| 45 | M7 unregulated segment | unregulated = 0 | PASS | Score 0 confirmed |
| 46 | M8 distributor sales Nil | none = 0 | PASS | Score 0 confirmed |
| 47 | M9 GM proxy 37.10% vs peer median 54.26% | at/below = 0 | PASS | Proxy formula and its use stated as the rule requires. Score 0 confirmed |
| 48 | M10 growth all but one year, receivable days −82 | else = 0 | PASS (literal read defensible) | The 3-band needs "stable". A −82 day move is not stable on the literal text. An alternative read (no deterioration = stable) gives 3. Sensitivity in G-06 |
| 49 | M11 latest 3yr CAGR 20.26%, selling % 5.18 to 5.11 | CAGR>=20% AND selling % stable/declining = 3 | PASS | Two-window test needs >=6 years, seven available. Deceleration correctly denies the 5-band. Score 3 confirmed |
| 50 | M12 WC days 54.85 and 68.31 | >45 days = 0 | PASS | Score 0 confirmed |
| 51 | Moat present at score >=3, count | count | PASS | M1, M4, M11 = 3 present. Confirmed |
| 52 | Moat classification bands | 2-3 = MODERATE | PASS | 3 present maps to MODERATE. Confirmed |
| 53 | Never guess peer figures | rule | PASS | VILAS excluded, not estimated. Median-of-two disclosed |
| 54 | Block F total | sum | PASS | 3+1+1+3+0+0+0+0+0+0+3+0 = 11 confirmed |

### 1.8 Classification, confidence, deal-breakers, output

| # | Rule | Verdict | Recomputation |
|---|---|---|---|
| 55 | Core = A+B+C+D+E | PASS | 15+8+18+10+7 = 58 confirmed |
| 56 | Grand total = Core + F | PASS | 58+11 = 69 confirmed |
| 57 | Data confidence bands, 5-6 years = lower, flag "may not have seen full cycle" | PASS | Report applies the 5-6 band to the binding balance-sheet window and flags it. Correct |
| 58 | History downgrade only at 3-4 years | PASS | history_downgrade: false is right at six or seven years |
| 59 | Classification matrix | PASS | Core 40-59 = AVERAGE, moat class irrelevant in that band. Confirmed. Holds at Core 54 and 57 under both recomputations below |
| 60 | Deal-breaker 1, Block A < 8 | PASS | A = 15. Not fired. Still not fired at the recomputed 11 |
| 61 | Deal-breaker 2, Block B < 8 | PASS | B = 8 exactly. Correctly not fired. Near-miss flagged |
| 62 | Deal-breaker 3, median ROCE < 10% | PASS | 16.63%. Not fired |
| 63 | Deal-breaker 4, cumulative CFO/PAT < 0.50 | PASS | 1.95. Not fired |
| 64 | Deal-breaker 5, pledge > 15% | PASS | Data absent. Correctly recorded as an open item, not as a fired breach and not as a clearance |
| 65 | Deal-breaker 6, ND/EBITDA > 3x AND IC < 3x | PASS | Max ND/EBITDA 2.10x on either basis, so the AND fails even at the recomputed IC of 2.53x. Not fired |
| 66 | Deal-breaker 7, revenue declined in majority of years | PASS | 1 of 6. Not fired |
| 67 | Deal-breaker 8, PAT negative in last 3 years | PASS | All positive. Not fired |
| 68 | Deal-breaker 9, history < 3 years | PASS | Not fired |
| 69 | YAML block: all template fields present | PASS | Every field in the stage-1 template is present |
| 70 | YAML values consistent with the report body | **FAIL** | data_years: 7 while the report's own confidence band uses the binding six-year window. The "may not have seen full cycle" flag sits in the report and not in the block. See G-04 |
| 71 | analyst_note <= 200 words | PASS | About 146 words |
| 72 | flags: FLAG-GATE0 when classification <= AVERAGE with depressors named | PASS | Present, depressors named (Block B, Block E) |
| 73 | block_b_trend carries the one number that shows the trend | PASS | "deteriorating", +13.46 days, with the FCF series |
| 74 | Dashboard output elements: moat bars, strongest/weakest block, classification, decision line | PASS | All present |

**Gate 0: 74 rules checked, 70 pass, 4 fail.**

---

## PART 2: EMERGING MOAT (B07) COMPLIANCE TABLE

Rule source: prompts/07-emerging-moat-pipeline.md.

### 2.1 Operating rules and Sections 1 and 2

| # | Rule | Verdict | Recomputed value / note |
|---|---|---|---|
| 1 | OR1: all six sections in one response | PASS | Sections 1 to 6 plus the optionality register all present |
| 2 | OR2: evidence taxonomy on every item | PASS | Every scored category carries a tier |
| 3 | OR3: source anchors on every evidence item | PASS | AR page, call page, slide number throughout |
| 4 | OR4: skepticism, hard evidence over promises | PASS | Marketing claim vs statutory Nil-R&D contradiction raised and flagged. Unapproved Rs 400 Cr item excluded from 2C |
| 5 | OR5: state NO EVIDENCE FOUND, never force-fit | PASS | A2, B3, D1, D2, E1, G1, G2 all state it. I1 and I2 state score 0 with the rule reasoning |
| 6 | OR6: completionist guard, stop and recheck at 12+ active categories | PASS | Six active. Trigger check performed and stated |
| 7 | Recount line "n documented items across m categories", internally consistent | **FAIL** | Stated "9 documented items across 11 categories". Its own list holds 11 items across 9 categories, and omits F2, which Section 3 tags 📄. Correct: at least 11 items across 10 categories. See EM-02 |
| 8 | 1A table: status, evidence type, launch, revenue potential, differentiation | PASS | All columns present. Status labels drawn from the prescribed vocabulary with qualifiers |
| 9 | 1B: product, customer, geographic, channel, vertical integration | PASS | All five addressed. Channel returns NO EVIDENCE FOUND |
| 10 | 1C: mix table with current %, expected % in 3 years, margin direction, impact | PASS | The three-year forward column has no source. Gap named, one-year proxy caveated, nothing invented. OR5 governs |
| 11 | 2A: project, Rs Cr, funding, status, commissioning, capacity, % over current | PASS | All seven columns present for all three projects |
| 12 | 2B: utilisation trajectory per facility | PASS | Three businesses, three periods |
| 13 | 2C: total capex under execution x **historical fixed asset turnover** = implied incremental revenue, arithmetic shown | **FAIL** | The company-guided capex-specific turn (1.0-1.2x) was substituted for the historical fixed asset turnover. Framework method: Rs 440 Cr x 2.0x = Rs 880 Cr = **45.1%** of FY26 revenue, against the reported 25%. See EM-01 |
| 14 | 2C denominator basis consistent with the injected Gate 0 revenue | **FAIL** | Uses Rs 1,952.91 Cr where B01 scores on Rs 1,912.81 Cr. On the B01 base: 23.0% to 27.6%, midpoint 25.3%. No material change. See EM-05 |
| 15 | 2D: new geography or market entries | PASS | NOT FOUND stated, with the reason |

### 2.2 The 23 scored rows: addressed or explicitly NO EVIDENCE (rubric rule 3)

| # | Category | Addressed | Tier stated | Multiplier applied | Verdict |
|---|---|---|---|---|---|
| 16 | A1 rare manufacturing capability | Yes | 🎙️/🔍 | 0.7 | PASS |
| 17 | A2 patent and IP pipeline | NO EVIDENCE FOUND | — | 0 | PASS |
| 18 | A3 process innovation | Yes | 📄/🎙️ | 0.7 (conservative) | PASS |
| 19 | A4 product platform | Yes | 🔍/🎙️ | 0.6 | PASS on coverage, see row 44 |
| 20 | B1 backward integration | Yes | 📄/🎙️ | 0.7 (conservative) | PASS |
| 21 | B2 qualification lock-in | Yes | 🎙️ | 0.7 | PASS |
| 22 | B3 supply chain network effect | NO EVIDENCE FOUND | — | 0 | PASS |
| 23 | C1 customer ecosystem | Yes | 📄/🎙️ | 0.7 (conservative) | PASS |
| 24 | C2 concentration improving | Yes | 📄 | 1.0 | PASS, the load-bearing item is the Note 25.6 ratio |
| 25 | D1 proprietary data asset | NO EVIDENCE FOUND | — | 0 | PASS |
| 26 | D2 digital platform | NO EVIDENCE FOUND | — | 0 | PASS, SAP correctly rejected as failing the bar |
| 27 | E1 geographic first-mover | NO EVIDENCE FOUND | — | 0 | PASS |
| 28 | E2 China+1 beneficiary | Yes | 📄 | 1.0 | PASS, export trend and tariff fact are documented |
| 29 | F1 talent density | Yes | 📄 | 1.0 | PASS, ESOP and turnover tables are documented |
| 30 | F2 execution moat, cross-referenced to B05 | Yes | 📄/🎙️ | 0.7 (conservative) | PASS, promise-delivery record cross-referenced as the rule requires |
| 31 | G1 war chest | NO EVIDENCE FOUND (adverse) | — | 0 | PASS |
| 32 | G2 WC improvement | NO EVIDENCE FOUND (adverse) | — | 0 | PASS |
| 33 | H1 consolidation beneficiary | Yes | 🔍/📄 | 0.5 (conservative) | PASS |
| 34 | H2 strategic partnerships | Yes | 🎙️ | 0.7 | PASS |
| 35 | H3 ESG moat | Yes | 📄 | 1.0 | PASS |
| 36 | I1 talent asymmetry (Category 21) | Yes | — | 0 | PASS, see rows 48 and 51 |
| 37 | I2 cannibalization barrier (Category 22) | Yes | — | 0 | PASS on presence, see rows 49 and 50 |
| 38 | R1 regulatory and policy tailwinds | Yes | 🎙️ | 0.7 (conservative) | PASS |

All 23 scored rows are addressed. No category is missing. No REWORK
trigger for stage 7 on coverage.

### 2.3 Sections 3 to 6, scorecard and block

| # | Rule | Verdict | Recomputed value / note |
|---|---|---|---|
| 39 | Section 3 summary table, all rows, four columns, Strong/Moderate count | PASS | 23 rows, four columns, count of six stated |
| 40 | 4A approvals table: body, status, timeline, unlock, competitors | PASS | Two rows, all columns |
| 41 | 4B policy table: amount, duration, enrolment, shared | PASS | Four rows, all columns. PLI correctly denied as unevidenced |
| 42 | 4C active vs emerging, time to kick in, sustainability | PASS | All three addressed, shared-with-peers cap stated |
| 43 | Raw score matrix HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0 | PASS | All 14 non-zero rows re-derived, every raw score matches its stated likelihood x impact pair |
| 44 | Evidence multipliers exactly 📄 1.0, 🎙️ 0.7, 🔍 0.5 | **FAIL** | A4 uses 0.6, which is not one of the three defined values. A1 carries the same mixed 🎙️/🔍 tier and was scored 0.7. Recomputed: A4 = 0.7 gives total 18.6, A4 = 0.5 gives 18.4. Band unchanged. See EM-04 |
| 45 | Adjusted total arithmetic and rounding | PASS | Re-added all 23 rows: 18.5 exactly. Rounds to 19. Band unchanged either way |
| 46 | Bands absolute, no rescale: >=40 / 25-39 / 12-24 / <12 | PASS | 19 maps to MODEST. No rescale attempted. Ceiling stated as ~92 |
| 47 | I1/I2 contribution stated separately (operator ruling 20-Aug-2026) | PASS | "I1/I2 contribution: 0.0" stated, with the review-checkpoint note |
| 48 | I1 two-leg rule, (a) capability class AND (b) competitor economics, (b) needs >=1 📄 for the top band | PASS | Both legs tested and both fail. Leg (a) rejected against the named evidence hierarchy. Leg (b) declared untested. Score 0. The "management quality / strong team" exclusion is cited by name |
| 49 | I2 named-sacrifice rule, score 0 when the answer is "nothing must be destroyed" | PASS | Answer is "nothing", classified as execution lead, scored 0. Both directions (PSU rigidity, institutional relationships) checked |
| 50 | I2 applied "for each moat claimed anywhere in this scan" | **FAIL** | Only B2 and C1 tested by name, out of six active categories. E2, C2, F2 and R1 are not individually run through the test. See EM-06 |
| 51 | Scores consistent with stated evidence tiers, no 🎙️-only row scored as 📄 | PASS | Every 1.0x row (C2, E2, F1, H3) carries a real 📄 item. Five rows with 📄 evidence were scored down to 0.7 or 0.5, which is conservative and allowed |
| 52 | Optionality register: four columns, only 0-scored or 🎙️/🔍-only rows | PASS | Ten rows, four columns, all eligible |
| 53 | Register carried into the block | **FAIL** | Block carries 8 of the report's 10 rows. Marine propulsion and the Caterpillar data-centre platform are dropped. The latter survives in catalysts_12m, the former is lost to synthesis. See EM-07 |
| 54 | 6A four windows with a milestone in each | PASS | 12m, 12-24m, 24-36m, 3-5yr all present |
| 55 | 6B risk plus early warning per top-scoring moat | PASS | Six rows, matching the six active categories |
| 56 | 6C combined table from the INJECTED Gate 0 block | PASS | Core 58/100, moat 11/60 and 3/12, both classifications. Matches B01 exactly |
| 57 | 6D combined classification, full reasoning for HIGH POTENTIAL and TURNAROUND | PASS | AVERAGE declared, both special rows argued in full and rejected on evidence |
| 58 | 6E final card: evolution map, catalysts, biggest risk | PASS | Map per family present. Catalysts cross-referenced to the block. Biggest risk named |
| 59 | YAML: all template fields present | PASS | Every field present |
| 60 | YAML evidence_mix consistent with the report's own tags | **FAIL** | documented: 9 against 10 categories tagged 📄 in Section 3. F2 omitted, same root cause as row 7. claim: 10 and inference: 3 both re-derived clean. See EM-03 |
| 61 | YAML em_score, em_classification, active_categories consistent with the report | PASS | 19, MODEST, six Strong/Moderate rows. All match |
| 62 | analyst_note <= 200 words | PASS | About 120 words |
| 63 | Emerging Moat not conflated with FTTCP | PASS | Separation declared in the scope note. Scope line "22 categories + I1/I2 + R1" double-counts I1 and I2, cosmetic only |

**Emerging Moat: 63 rules checked, 56 pass, 7 fail.**

---

## PART 3: FINDINGS

### MAJOR

**G-01. ROCE formula substituted for FY21, creating a cross-basis A4
comparison.** Location: 01-gate0.md Block A, FY21 row and A4.
The prompt declares its formula block "fixed, do not substitute
alternatives", and defines ROCE as EBIT / (Total Assets − Current
Liabilities). FY21 has no current-liability split in the corpus, so the
maker computed capital employed as Net Worth + Total Borrowings instead.
The substitution is disclosed twice. It is still a substitution, and it is
load-bearing: FY21 is the earliest endpoint that A4 compares against.
A4 also compares a maker-computed FY21 figure against an AR-computed FY26
figure, so the two endpoints do not share a basis.
Recomputed on the AR-basis series alone (FY22 17.28 to FY26 13.75):
decline 3.53pp, band "decline 3-5pp", **A4 = 1, Block A = 11/20, Core =
54**. Classification stays AVERAGE (40-59). Deal-breaker 1 (Block A < 8)
stays unfired. Rule 3 (median ROCE < 10%) stays unfired at a five-year
median of 17.19%.

**G-02. Block D uses two different other-income bases inside one block.**
Location: 01-gate0.md D1 and D2.
D1's EBITDA is stated as PBT + Dep + Interest − Other Income = 315.75,
which excludes other income. D2's EBIT is stated as PBT + Interest =
250.99, which includes it. The same block cannot run on two bases. The
gap is the full Rs 39.90 Cr of other income, which B07 reports is about
77% fed by a state subsidy receivable.
The result sits on a band boundary. IC of 3.01x clears the 3.0x line by
0.01x. Harmonised downward (exclude other income from both), EBIT =
211.09 and **IC = 2.53x, band 1.5-2.9, D2 = 1, Block D = 9/20, Core =
57**. Harmonised upward (include other income in both), EBITDA = 355.65,
ND/EBITDA = 1.55x, which stays in the 1-2x band and leaves the score at
10. So the score impact is 0 or minus 1 depending on the direction of the
fix, and the maker took the more favourable reading in each of the two
tests. Classification stays AVERAGE either way. Deal-breaker 6 stays
unfired because the ND/EBITDA leg never exceeds 2.10x.

**EM-01. Section 2C substituted the company-guided asset turn for the
framework's historical fixed asset turnover.** Location: 07-emoat.md
Section 2C and block field capex_embedded_growth_pct.
The framework states the method in one line: "total capex under execution
x historical fixed asset turnover = implied incremental revenue". The
report computes both, then rejects the historical figure (2.0x, Inv. Pres.
slide 29) in favour of management's capex-specific 1.0-1.2x guide, and
gives a defensible reason: a mature fleet ratio overstates day-one
greenfield capacity.
The reasoning is sound and the arithmetic is shown both ways, which is
why this is MAJOR and not CRITICAL. The problem is the block. It carries
a single number, capex_embedded_growth_pct: 25, and downstream stages read
the block, not the argument.
Framework value: Rs 440 Cr x 2.0x = Rs 880 Cr, **45.1%** of FY26 revenue,
against the reported 25%. Remedy: carry both, or carry the framework value
with the maker's caveat attached, so stage 11 sees the deviation.

### MINOR

**G-03. Capex definition proxied for FY22 to FY24.** Location: 01-gate0.md
Block B capex table. The framework defines capex as the cash flow
statement's PPE plus intangibles line. FY22 to FY24 use a Δ(Net Block +
CWIP) + Depreciation proxy. Disclosed clearly, and the acquisition-year
exclusion rule was honoured correctly for FY25. Re-derived on the strict
definition (FY25 and FY26 only): B2 = 2 (1 of 2 positive = 50%), B3 = 0
(ratio 0.043). Both scores unchanged. No score impact.

**G-04. Block field data_years disagrees with the confidence window used
in the report.** Location: B01-gate0.yaml, data_years: 7. The report
applies the "5-6, lower, flag" confidence band to the binding six-year
balance-sheet window, and states the "may not have seen full cycle" flag.
The block reports seven years, which maps to the "7-9 moderate" band with
no flag, and the flag text does not appear anywhere in the block. A
downstream stage reading only the block loses the flag.
history_downgrade: false is correct at either window, since the downgrade
needs 3-4 years.

**G-05. D1 debt basis is a discretionary choice the framework does not
define.** Location: 01-gate0.md D1. The framework says "Net Debt / EBITDA"
and never rules on lease liabilities. Excluding leases scores 3, including
them scores 1, a 2-point swing in Block D. The maker chose the excluding
basis, anchored it to the AR's own Note 25.21 convention, showed both, and
stated that the classification band does not move. Compliant, and worth
naming because the chosen basis is the higher-scoring one and the
framework gives no rule to appeal to.

**G-06. M10 tier reading is defensible but sits on an ambiguity with a
moat-class consequence.** Location: 01-gate0.md M10. The 3-band reads
"growth all but 1 year AND stable". Receivable days moved minus 82 days.
The maker read that as failing "stable" and scored 0 by elimination. On
the literal text that read is right, because the neighbouring 5-band
defines the same concept as a movement of 10 days or less. An alternative
read, that an improvement cannot be instability, gives **M10 = 3, Block F
= 14/60, moats present 4, moat_class STRONG** rather than MODERATE.
Classification stays AVERAGE, because Core 40-59 governs that band with no
moat qualifier. Flagged because moat_class is a field downstream stages
consume. The maker's read stands; the operator should know it is a
one-word call.

**G-07. M4 rationale misstates which leg fails.** Location: 01-gate0.md
M4 basis text. It says the top band "fails on stability, not decline
count". The 5-band needs zero revenue-decline years, and FY21 declined, so
the decline-count leg fails as well. Score 3 is correct either way.
Presentational only.

**EM-02. Completionist recount line contradicts its own list.** Location:
07-emoat.md Section 3 recount line, and block field completionist_recount.
Stated: "9 documented items across 11 categories". The enumeration that
follows holds 11 items across 9 categories, so the two counts are
transposed. Separately, F2 is tagged 📄 in Section 3 ("capacity/volume
delivery facts") and does not appear in the enumeration. Corrected count:
at least 11 documented items across 10 categories (A3, B1, C1, C2, E2, F1,
F2, H1, H3, R1). The guard itself was performed properly, the 12-category
trigger was checked, and the honest-sparse-scan instruction was followed.
The count line is the only defect.

**EM-03. evidence_mix documented count omits F2.** Location:
B07-emoat.yaml, evidence_mix. documented: 9 against 10 categories carrying
a 📄 tag in Section 3. Same root cause as EM-02. claim: 10 and inference:
3 both re-derived clean (claim: A1, A3, A4, B1, B2, C1, C2, F2, H2, R1;
inference: A1, A4, H1).

**EM-04. A4 uses a multiplier that does not exist in the framework.**
Location: 07-emoat.md Section 5, A4 row. The framework defines three
multipliers: 1.0, 0.7, 0.5. A4 is scored at 0.6. A1 carries the identical
mixed 🎙️/🔍 tier and is scored at 0.7, so the treatment is also internally
inconsistent. Recomputed at 0.7: total 18.6, em_score 19. At 0.5: total
18.4, em_score 18. MODEST in every case.

**EM-05. 2C revenue denominator differs from the Gate 0 revenue base.**
Location: 07-emoat.md Section 2C. Uses Rs 1,952.91 Cr where B01 scores
every growth metric on Rs 1,912.81 Cr. On the B01 base the range becomes
23.0% to 27.6%, midpoint 25.3%, against the reported 25%. Immaterial to
the field. Named because two stages of one run should state which revenue
basis they use. Which figure is correct in the source is Verifier A's
call, not mine.

**EM-06. I2 enumeration is incomplete.** Location: 07-emoat.md I2. The
rule says "For each moat claimed anywhere in this scan, answer: what
SPECIFIC thing would the best-resourced competitor have to destroy". The
report answers for B2 and C1 by name, then generalises. E2, C2, F2 and R1
are not run through the test individually. The score would very likely
stay 0, since E2 and R1 are described elsewhere in the same report as
sector-wide and shared with competitors, which is the definition of no
sacrifice required. The enumeration is still short of the rule as written.

**EM-07. Optionality register loses two rows on the way into the block.**
Location: 07-emoat.md register table against B07-emoat.yaml
optionality_register. Report table has 10 rows, the block carries 8.
Dropped: marine propulsion components, and the Caterpillar data-centre
platform. The framework states that synthesis merges register items into
the monitoring checklist, and synthesis reads the block. The Caterpillar
item survives through catalysts_12m. The marine propulsion item does not
survive at all.

---

## PART 4: VERDICT AND TRIGGERS

Recomputed classification, Gate 0: **AVERAGE**, unchanged. The two MAJOR
Gate 0 findings move Core to 54 (G-01) or 57 (G-02), or to 53 if both are
applied. All three values sit inside the 40-59 AVERAGE band. No
deal-breaker changes state under any recomputation.

Recomputed classification, Emerging Moat: **MODEST**, unchanged. Every
multiplier recomputation lands between 18.4 and 18.6, inside the 12-24
band.

One downstream-consumed field is sensitive: moat_class could read STRONG
instead of MODERATE under the alternative M10 reading (G-06). One is
disputed: capex_embedded_growth_pct is 25 as reported and 45.1 on the
framework method (EM-01).

REWORK triggers in my scope, none fire:
- Rubric rule 8, categories 21 and 22 present in B07: both present, both
  scored, both scored per their own rules. No REWORK for stage 7.
- Verifier acceptance rate below 60%: acceptance is 92%.
- CRITICAL findings: none. CRITICAL authority on numbers rests with
  Verifier A in any case.

Deferred to phase 3: rules 4, 5, 7, 11, 12 (B10 and B11), rule 6 (B09),
rule 9 (stage 13 narrative), rule 10 (B09b dossier at /finalize).

---

```yaml
stage: B12c
company: "PITTIENG"
run_date: "2026-09-05"
model: claude-opus-4-8
status: complete
gate0:
  rules_checked: 74
  fails:
    - "Formula rule: ROCE basis substituted for FY21 (Net Worth + Total Borrowings), creating a cross-basis A4 endpoint comparison [G-01, MAJOR]"
    - "Formula rule: FCF capex definition proxied for FY22-FY24 (delta Net Block+CWIP + Depreciation) instead of the cash flow statement line [G-03, MINOR]"
    - "D2: EBIT includes other income while D1 EBITDA excludes it; two bases inside one block, on a band boundary [G-02, MAJOR]"
    - "B01 block: data_years 7 contradicts the six-year binding window used for the data-confidence band; 'may not have seen full cycle' flag not carried into the block [G-04, MINOR]"
emoat:
  rules_checked: 63
  fails:
    - "Completionist recount line counts transposed (9 items across 11 categories vs its own list of 11 items across 9) and omits F2 [EM-02, MINOR]"
    - "Section 2C used the company-guided capex-specific asset turn (1.0-1.2x) in place of the framework's historical fixed asset turnover (2.0x) [EM-01, MAJOR]"
    - "Section 2C revenue denominator Rs 1,952.91 Cr differs from the B01 revenue base Rs 1,912.81 Cr [EM-05, MINOR]"
    - "A4 scored at a 0.6 multiplier, which is not one of the three defined values (1.0/0.7/0.5); A1 has the same mixed tier at 0.7 [EM-04, MINOR]"
    - "I2 applied by name to only 2 of the 6 active moats, against 'for each moat claimed anywhere in this scan' [EM-06, MINOR]"
    - "Optionality register: block carries 8 of the report's 10 rows; marine propulsion and Caterpillar data-centre dropped [EM-07, MINOR]"
    - "evidence_mix documented count 9 against 10 categories tagged with a documented item [EM-03, MINOR]"
valuation: {rules_checked: 0, fails: [], note: "pending phase 3"}
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: [], note: "pending phase 3"}
recomputed_destination_pe: ""
recomputed_decision: ""
findings:
  - {severity: "MAJOR", location: "B01 Block A, FY21 ROCE row and A4", rule: "Formula definitions are fixed, do not substitute alternatives", recomputed: "A4 = 1 (FY22 17.28 to FY26 13.75, decline 3.53pp), Block A = 11/20, Core = 54, classification AVERAGE unchanged", note: "FY21 capital employed computed as Net Worth + Total Borrowings, not Total Assets minus Current Liabilities. Disclosed twice, still a substitution, and it is the earliest endpoint A4 rests on. A4 also compares a maker-computed FY21 against an AR-computed FY26."}
  - {severity: "MAJOR", location: "B01 Block D, D1 and D2", rule: "One basis per block; D1 EBITDA and D2 EBIT must share an other-income treatment", recomputed: "Exclude other income from both: EBIT 211.09, IC 2.53x, D2 = 1, Block D = 9/20, Core = 57. Include in both: ND/EBITDA 1.55x, D1 stays 3, no change", note: "IC of 3.01x clears the 3.0x band line by 0.01x. The maker took the higher-scoring basis in each of the two tests. Deal-breaker 6 stays unfired at 2.53x because the ND/EBITDA leg never exceeds 2.10x."}
  - {severity: "MAJOR", location: "B07 Section 2C and block capex_embedded_growth_pct", rule: "Total capex under execution x historical fixed asset turnover", recomputed: "Rs 440 Cr x 2.0x = Rs 880 Cr = 45.1% of FY26 revenue, against the reported 25%", note: "Substitution is disclosed and reasoned, and both figures appear in the report. The block carries only 25, and downstream stages read the block. Carry both or carry the framework value with the caveat."}
  - {severity: "MINOR", location: "B01 Block B capex table, FY22-FY24", rule: "FCF = CFO minus capex from the cash flow statement, exclude acquisitions", recomputed: "Strict basis, FY25-FY26 only: B2 = 2, B3 = 0, both unchanged", note: "Proxy disclosed. Acquisition-year exclusion handled correctly for FY25. No score impact."}
  - {severity: "MINOR", location: "B01-gate0.yaml data_years", rule: "Data confidence bands and their flag", recomputed: "Binding window is 6 years, band 5-6 lower, flag 'may not have seen full cycle'", note: "Block says 7, which maps to the moderate band with no flag. The flag text is in the report only. history_downgrade false is correct at either window."}
  - {severity: "MINOR", location: "B01 D1", rule: "Net Debt / EBITDA, basis for lease liabilities undefined by the framework", recomputed: "Excl. lease 1.75x scores 3; incl. lease 2.10x scores 1; Block D 10 vs 8", note: "Discretionary choice, disclosed on both bases, anchored to the AR's own Note 25.21 convention. Classification band unchanged either way."}
  - {severity: "MINOR", location: "B01 M10", rule: "Switching costs, 3-band 'growth all but 1 year AND stable'", recomputed: "Alternative read gives M10 = 3, Block F = 14/60, moats present 4, moat_class STRONG instead of MODERATE; classification stays AVERAGE", note: "Maker's literal read (a minus 82 day move is not stable) is defensible and disclosed. Flagged because moat_class is consumed downstream."}
  - {severity: "MINOR", location: "B01 M4 basis text", rule: "M4 5-band needs zero decline years AND receivable days stable", recomputed: "Score 3 correct either way", note: "Rationale says the top band fails on stability, not decline count. The decline-count leg fails too, since FY21 declined. Presentational."}
  - {severity: "MINOR", location: "B07 Section 3 recount line and block completionist_recount", rule: "State the recount as n documented items across m categories", recomputed: "At least 11 documented items across 10 categories (A3, B1, C1, C2, E2, F1, F2, H1, H3, R1)", note: "Stated counts are transposed against the report's own enumeration, and F2 is omitted although Section 3 tags it as documented. The guard itself was performed and the 12-category trigger was checked."}
  - {severity: "MINOR", location: "B07-emoat.yaml evidence_mix", rule: "evidence_mix item counts must match the report's tags", recomputed: "documented 10 categories, not 9; claim 10 and inference 3 both confirmed", note: "Same root cause as the recount finding: F2 omitted."}
  - {severity: "MINOR", location: "B07 Section 5, A4 row", rule: "Evidence multipliers are 1.0, 0.7, 0.5", recomputed: "A4 at 0.7 gives 18.6 (em_score 19); at 0.5 gives 18.4 (em_score 18); MODEST in both cases", note: "0.6 is not a defined multiplier. A1 carries the identical mixed tier at 0.7, so the treatment is also internally inconsistent."}
  - {severity: "MINOR", location: "B07 Section 2C denominator", rule: "Cross-stage basis consistency with the injected Gate 0 revenue", recomputed: "On B01's Rs 1,912.81 Cr: 23.0% to 27.6%, midpoint 25.3%", note: "Immaterial to the reported 25. Which revenue figure is correct in the source is Verifier A's call."}
  - {severity: "MINOR", location: "B07 I2", rule: "Apply the cannibalization test to each moat claimed anywhere in the scan", recomputed: "2 of 6 active moats tested by name (B2, C1); E2, C2, F2, R1 not individually tested", note: "Score 0 would very likely stand, since the report elsewhere calls E2 and R1 sector-wide and shared. Enumeration is still short of the rule."}
  - {severity: "MINOR", location: "B07-emoat.yaml optionality_register", rule: "Register carried in the block, synthesis merges it into the monitoring checklist", recomputed: "8 of 10 rows carried", note: "Marine propulsion and Caterpillar data-centre platform dropped. Caterpillar survives via catalysts_12m; marine propulsion is lost."}
critical_count: 0
major_count: 3
minor_count: 11
acceptance_rate: 92
```
