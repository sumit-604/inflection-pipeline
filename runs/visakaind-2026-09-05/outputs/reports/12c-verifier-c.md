# STAGE 12C: VERIFIER C, FRAMEWORK ADHERENCE (PHASE 1)
Company: Visaka Industries Ltd (VISAKAIND) | Run date: 2026-09-05
Model: claude-opus-4-8 | Scope: phase-1, Gate 0 (B01) + Emerging Moat (B07) only

## SCOPE AND METHOD

I audit rule application. I do not audit company quality. I do not audit
whether a number exists in a source PDF. Verifier A owns source fidelity and
its verdicts are non-overridable.

Rule sources read for this pass:
- prompts/01-gate-0-pipeline.md (Gate 0 thresholds, formulas, matrix, overrides)
- prompts/07-emerging-moat-pipeline.md (23-row scan, taxonomy, guard, bands)

Artifacts audited:
- runs/visakaind-2026-09-05/outputs/reports/01-gate0.md
- runs/visakaind-2026-09-05/outputs/reports/07-emoat.md

Every block score below was re-derived from the inputs the B01 report itself
states. I did not open source PDFs. Where an input is unanchored inside B01, I
say so and route the existence question to Verifier A.

### NOT ASSESSED in this pass

These verifier-C rules are out of phase-1 scope. Silence here is not a pass.

| Verifier C rule | Status |
|---|---|
| Rule 4, valuation audit (B11) | NOT ASSESSED. B11 does not exist yet. Phase 3. |
| Rule 5, destination-PE tolerance | NOT ASSESSED. Depends on B11. |
| Rule 6, downstream candidates in B09 | NOT ASSESSED. B09 not among inputs. |
| Rule 7, method plurality in B11 | NOT ASSESSED. Phase 3. |
| Rule 9, Business Understanding Narrative | NOT ASSESSED. B13 not among inputs. |
| Rule 10, Halt 1 dossier B09b | NOT ASSESSED here by design. The rule fires at the /finalize verifier pass; the phase-1 structural check is mechanical inside run-pipeline step 6b. |
| Rule 11, v3.8 exit construction | NOT ASSESSED. Phase 3. |
| Rule 12, Amendment 19 FV path | NOT ASSESSED. Phase 3. |

The valuation framework documents were not loaded. Phase-1 scope forbids it.

---

## PART 1: GATE 0 (B01) COMPLIANCE

54 rules checked. 47 PASS, 7 FAIL. One MAJOR, six MINOR, zero CRITICAL.

### 1.1 Rule-by-rule table

| # | Rule checked | Verdict | Recomputed value / note |
|---|---|---|---|
| G-01 | Rule 6 opening: "Data available: X years (FY__ to FY__)" + "Scoring adapted to X-year history" | PASS | Both elements present in the opening paragraph, 10 years, FY2017 to FY2026. |
| G-02 | A1 median ROCE band | PASS | Sorted [3.01, 3.46, 8.34, 9.71, 11.87, 14.67, 16.13, 17.45, 19.16, 21.83]. Median (11.87+14.67)/2 = 13.27%. Band 10-14.9 = 1. Concur. |
| G-03 | A2 minimum single-year ROCE band | PASS | Min 3.01% (FY24). Band <8 = 0. Concur. |
| G-04 | A3 median ROE band | PASS | All 10 ROE values re-divided from the stated PAT and average net worth. Every one reproduces to 2dp. Median (10.90+11.07)/2 = 10.99%. Band <12 = 0. Concur. |
| G-05 | A4 ROCE trend band | PASS | 11.87 minus 14.67 = decline 2.80pp. Band 1-3pp = 3. Concur on the stated basis. |
| G-06 | ROCE formula fidelity ("fixed, do not substitute alternatives") | **FAIL (MINOR)** | Two bases are blended in one 10-year series. FY17-FY23 uses a proxy capital employed (Equity + Reserves + Borrowings). FY24-FY26 uses the AR Schedule-III disclosure. The prescribed formula is EBIT / (Total Assets minus Current Liabilities). Disclosed in Formula Notes and input_gaps, and cross-validated (proxy on FY26 gives 12.57% vs AR 11.87%). Score impact on A1/A2/A4 is nil. Score impact on M3 is not nil, see G-33 note. |
| G-07 | ROE formula (PAT / average net worth; earliest year closing-only stated) | PASS | FY17 flagged as closing-only, no FY16. Rule permits this and requires the statement. Present. |
| G-08 | Block A sum and deal-breaker 1 | PASS | 1+0+0+3 = 4/20. Block A <8 triggers deal-breaker 1, max GOOD. Recorded. |
| G-09 | B1 cumulative CFO / cumulative PAT | PASS | CFO sum re-added = 1,071.88. PAT sum re-added = 600.51. Ratio 1.785. Band >=1.00 = 5. Concur. |
| G-10 | B2 FCF-positive proportion | PASS | 2 of 3 = 66.7%. Band 50-74 = 2. Concur on the stated 3-year window. |
| G-11 | B3 cumulative FCF / cumulative PAT | PASS | FCF sum -112.94+90.80+145.89 = 123.75. PAT sum 90.50. Ratio 1.367. Band >=0.60 = 5. Concur on the stated window. |
| G-12 | B4 WC-days formula and revenue basis declared | PASS | Recomputed FY24 = 33.28+102.10-21.36 = 114.02. FY26 = 35.06+76.60-19.24 = 92.42. Revenue basis stated as the rule requires. Concur. |
| G-13 | Block B window consistency | **FAIL (MINOR)** | B1 runs on 10 years. B2, B3 and B4 run on 3 years. The block total of 17/20 therefore mixes windows. B3's 1.367 ratio is flattered by an FY24-FY26 PAT denominator of 90.50, which contains the two trough years and the FY26 one-off. Disclosed, but the block is not comparable to a full-history Block B. No deal-breaker consequence: B1 and B4 alone keep Block B at or above 10, so deal-breaker 2 cannot fire. |
| G-14 | Block B sum | PASS | 5+2+5+5 = 17/20. Concur. |
| G-15 | C1 revenue CAGR, period count | PASS | (1675.59/960.57)^(1/9)-1 = 6.379%. Nine periods used, not ten. Correct. Band 5-9.9 = 1. |
| G-16 | C2 PAT CAGR | PASS | (87.83/42.78)^(1/9)-1 = 8.32%. Band 5-9.9 = 1. Concur. |
| G-17 | C3 positive YoY proportion | PASS | 7 of 9 = 77.8%. Band 75-99 = 3. Concur. |
| G-18 | C4 PAT CAGR minus revenue CAGR | PASS | 8.32 minus 6.38 = +1.94pp. Band within +/-3pp = 3. Concur. |
| G-19 | CAGR edge rules | PASS | Both endpoints positive, so no N/M. No loss-to-profit swing, PAT positive every year with an FY25 floor of 0.14. Noted in data_notes as the rule directs. C4-when-N/M rule not triggered. |
| G-20 | Block C sum | PASS | 1+1+3+3 = 8/20. Concur. |
| G-21 | D1 net debt / EBITDA | PASS | 303.44 minus 27.55 = 275.89. EBITDA 110.25+32.96+64.97 = 208.18. Ratio 1.325x. Band 1-2x = 3. I also tested the ex-exceptional case: EBITDA 148.48 gives 1.858x, same band. Score is robust. |
| G-22 | D2 interest coverage basis | **FAIL (MINOR)** | 143.21/32.96 = 4.34x scores 2. The EBIT numerator carries the Rs 59.70 Cr one-off land gain. The report itself computes the ex-exceptional figure at 2.53x, states it "is the decision-relevant one", then scores the higher band. Recomputed D2 = 1 on the decision-relevant basis. Block D becomes 12/20, core 55. Classification unchanged. |
| G-23 | D3 debt / equity | PASS | 303.44/835.57 = 0.363x. Band 0.1-0.5 = 4. AR cross-check 0.42x lands in the same band. Concur. |
| G-24 | D4 current ratio | PASS | 1.60x source-provided, independently reproduced as 628.24/391.47 = 1.605x. Band 1.5-1.99 = 4. Concur. |
| G-25 | Block D sum | PASS | 3+2+4+4 = 13/20. Arithmetic concur. |
| G-26 | E1 promoter holding, "latest quarter" requirement | PASS | 4,60,05,365 / 8,64,04,760 = 53.25%. Band 50-59.9 = 4. The 31-Mar-2026 date is a quarter end and is the latest in the corpus. Staleness disclosed. Concur. |
| G-27 | E2 promoter change over 3 years | **FAIL (MAJOR)** | The rule specifies a 3-year change. Only a 1-year window exists. The report awards the maximum band, 5, on that 1-year substitute. The same report flags the +4.82pp move as unexplained, records 0.00% change for both named individual promoters, and writes "worth independent verification before relying on this score". Rule 5 directs N/A and a score of 0 when a data point is not available. Recomputed E2 = 0. Block E becomes 9/20, core 51. Classification unchanged. |
| G-28 | E3 pledge, not-found handling | PASS | NOT FOUND, scored 0 on availability grounds, explicitly not recorded as a confirmed pledge. This is exactly rule 5. Concur. |
| G-29 | E4 contingent liabilities / net worth | PASS | 7.73/835.57 = 0.93%. Band <5% = 5. Concur. |
| G-30 | Block E sum | PASS | 4+5+0+5 = 14/20. Arithmetic concur. |
| G-31 | M1 pricing power band | PASS | Margin fell 3.76pp with growth. "Declined 2-5pp despite growth" = 1. Correct band. |
| G-32 | M2 cost advantage, peer median derivation | PASS | Peer margins -2.53, 2.51, 9.67 give median 2.51%. 8.44 minus 2.51 = +5.93pp. Band >=5pp = 5. The 3-year alternate (+2.98pp, score 3) is disclosed. Either way M2 stays at or above 3, so moats_confirmed and moat_class do not move. |
| G-33 | M3 capital efficiency band | PASS | FAT 2.475x, ROCE 11.87%. Both the FAT>2x/ROCE>15% and FAT>1x/ROCE>12% legs fail. Score 0 is correct on the stated inputs. Note the coupling to G-06: on the report's own proxy basis FY26 ROCE is 12.57%, which clears the >12% leg and would score M3 = 1. Moat score 13, no class change. |
| G-34 | M4 customer stickiness band | PASS | Two decline years with positive CAGR = 1. Correct. |
| G-35 | M5 scale and dominance band | PASS | Third of four by market cap, second by margin. "Top 3 mcap AND margin top 2" = 3 under either reading of the margin test. Peer-set narrowness disclosed in input_gaps. |
| G-36 | M6 technology / R&D band | PASS | AR states no R&D expenditure line. Else-band = 0. Correct. |
| G-37 | M7 regulatory / licence band | PASS | Unregulated = 0. Correct. |
| G-38 | M8 distribution band | **FAIL (MINOR)** | The rubric has no band for a network that is quantified and shrinking. Band 1 reads "mentioned unquantified", which does not fit. Band 0 reads "none or purely digital", which also does not fit. The report chose 0 and stated why. The choice is conservative and disclosed. The defect sits in the rubric, not in the analyst. Alternate reading M8 = 1 gives moat score 13, no class change. Framework amendment candidate. |
| G-39 | M9 brand band and GM proxy declaration | PASS | Peer GM median 43.66%. Gap +5.58pp with 6.38% growth, below the 8% leg. "Above peers but growth below" = 1. Proxy basis stated in data_notes as the rule requires. |
| G-40 | M10 switching costs band | PASS | Overall growth with 2 decline years = 1. Correct. |
| G-41 | M11 network effects, two-window test | PASS | 10 years available, above the 6-year minimum. Latest 3yr 0.58% recomputed. Prior 3yr 16.17%. All three bands fail. Score 0. Correct. |
| G-42 | M12 negative WC band | PASS | 114.02, 110.51, 92.42, all above 45 days. Score 0. Correct. Window limitation disclosed. |
| G-43 | Block F sum, moats present at >=3, moat class | PASS | 1+5+0+1+3+0+0+0+1+1+0+0 = 12/60. Two tests at or above 3 (M2, M5). Band 2-3 present = MODERATE. Concur. |
| G-44 | "PEER DATA NEEDED" rule | PASS | Peer data was provided for three names, so scoring was permitted. No peer figure was guessed. Scope limitation recorded in input_gaps. |
| G-45 | Core score and grand total arithmetic | PASS | 4+17+8+13+14 = 56. 56+12 = 68. Concur. |
| G-46 | Classification matrix | PASS | Core 56 sits in the 40-59 band, which is AVERAGE and is not split by moat class. Correctly stated. |
| G-47 | All 9 deal-breakers checked, driving years named | PASS | All nine tested and recorded. Only 1 fires. The rule's "state WHICH years drive any deal-breaker" is met: FY23 to FY25 named with ROCE and ROE values. |
| G-48 | Data confidence table and history_downgrade | PASS | 10 years maps to the full confidence band. history_downgrade = false is literally correct. The downgrade triggers key off overall history, not per-metric windows. Per-metric narrowness is flagged at each metric. |
| G-49 | Rule 4 source-anchor discipline | **FAIL (MINOR)** | Two scored inputs carry no anchor at the point of use. M3's Net Block of 676.89 has no source cited, and it does not reconcile to B07's AR-sourced net PP&E of 675.98. M1's FY17 operating EBITDA margin of 12.20% has no anchor and its components are not shown. Rule 4 states an unanchored number counts against this stage. Existence routed to Verifier A. |
| G-50 | Rule 5 grounded claims, no estimated fills | PASS | Every gap is marked NOT FOUND or N/A. No industry-typical value appears anywhere. |
| G-51 | Output dashboard-format completeness | **FAIL (MINOR)** | The rule requires moat profile bars and a classification box. Neither is present. All blocks, line items, strongest and weakest block, and the decision line are present. Presentational only. |
| G-52 | YAML template completeness | PASS | All 21 template fields present with correct types. |
| G-53 | analyst_note 200-word cap | PASS | 197 words. Inside the strict cap. |
| G-54 | Conditional FLAG-GATE0 emission | PASS | Classification is AVERAGE with named historical depressors. FLAG-GATE0 is present with the depressors stated. Four further flags propagate, which the Master file permits. |

### 1.2 Gate 0 recomputation summary

| Item | B01 reported | My recomputation | Verdict |
|---|---|---|---|
| Block A | 4/20 | 4/20 | Concur |
| Block B | 17/20 | 17/20 as computed | Concur, window caveat G-13 |
| Block C | 8/20 | 8/20 | Concur |
| Block D | 13/20 | 12/20 on the ex-exceptional D2 basis | Differ by 1 |
| Block E | 14/20 | 9/20 with E2 at 0 under rule 5 | Differ by 5 |
| Core | 56 | 50 to 56 across variants | Same band |
| Block F | 12/60 | 11 to 14 across variants | Same class |
| moats_confirmed | 2 | 2 in every variant | Concur |
| moat_class | MODERATE | MODERATE in every variant | Concur |
| deal_breakers | [1] | [1] in every variant | Concur |
| classification | AVERAGE | AVERAGE in every variant | **Concur** |

The classification is robust. Core stays inside the 40-59 AVERAGE band under
every correction I can justify. Deal-breaker 1 fires in every variant. No
Gate 0 finding changes the pipeline decision.

---

## PART 2: EMERGING MOAT (B07) COMPLIANCE

36 rules checked. 27 PASS, 9 FAIL. One MAJOR, eight MINOR, zero CRITICAL.

### 2.1 Rule-by-rule table

| # | Rule checked | Verdict | Recomputed value / note |
|---|---|---|---|
| E-01 | All six sections in one response, no stops | PASS | Sections 1 to 6 plus the optionality register, all present. |
| E-02 | Section 1A, 1B, 1C structure and required columns | PASS | 1A carries status, evidence type, timing, revenue potential and portfolio difference. 1C refuses to invent a 3-year mix and cites the never-estimate rule. Correct. |
| E-03 | Section 2A capex table, required columns | PASS | Project, cost, funding, status, commissioning, capacity, percent over current, all present. |
| E-04 | Section 2B utilisation per facility | PASS | Four-year series per facility with anchors. |
| E-05 | Section 2C arithmetic shown, anchored figure chosen | PASS | FAT 1675.59/680.83 = 2.461x. Scenario 1: 16.87 x 2.462 = 41.5, which is 2.5% of revenue. Scenario 2: 450 x 2.462 = 1,108, which is 66.1%. Arithmetic reproduces. The report reports the documented scenario as capex_embedded_growth_pct. That is the correct conservative choice. |
| E-06 | Section 2D new geography | PASS | NO EVIDENCE FOUND stated, with a documented retrenchment noted against it. |
| E-07 | All 22 categories plus R1 addressed or explicitly NO EVIDENCE | PASS | I enumerated all 23. A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, I1-I2, R1. Every zero-scored row carries NO EVIDENCE FOUND or an explicit reasoned zero. None force-fitted. |
| E-08 | Section 3 summary table, 23 rows, required columns | PASS | 23 rows with evidence, type, strength and time to materialise. |
| E-09 | Strong/Moderate count stated | PASS | "3 of 23 rows (A3, G2, R1)". Matches active_categories exactly. |
| E-10 | Completionist guard applied and recount line stated | PASS | Guard threshold is 12 active categories. Three are active, so no trigger. The recount was still performed and stated, which the Section 3 instruction requires unconditionally. |
| E-11 | Recount internal consistency, body vs YAML | **FAIL (MINOR)** | The body attributes the 13 documented items as A3 5, G2 3, R1 3, plus 2 capex-table items. The YAML attributes them as A3 5, G2 3, R1 5. Both total 13. The 2 capex items move into R1 without explanation. The recount is the guard artifact and must be exact. |
| E-12 | Evidence-tier tags applied per item (rule 2) | PASS | Documented and management-claim tags appear on items throughout Sections 1 to 4. |
| E-13 | Rule 3 anchor format on every evidence item | **FAIL (MINOR)** | Several evidence items name a document but no page or slide. Examples: the yarn margin series cited to "AR2025/AR2026 segment notes"; the 3 ATUM Life stores cited to "AR FY26 BRSR"; the input-cost rise cited to "the Aug-2023 call". Rule 3 mandates the (AR p.__) form. |
| E-14 | evidence_mix counts reconcilable to the body | **FAIL (MAJOR)** | The YAML reports documented 16, claim 13, inference 5. No analyst-inference item is tagged anywhere in the report. The inference count of 5 has zero supporting tagged items. The documented count of 16 contradicts the body, which enumerates 13 supporting the Moderate rows plus at least 5 further documented facts. Downstream stages read evidence_mix as an evidence-quality input. No effect on em_score, because multipliers apply per category, not per item. |
| E-15 | Evidence multipliers applied per row | PASS | I checked all 23 rows. Documented rows use 1.0, management-claim rows use 0.7, zero rows use no multiplier. No misapplication. |
| E-16 | Likelihood x impact raw values match the matrix | PASS | LL maps to 1, HM maps to 3, HL/MM maps to 2. Every non-zero row conforms. |
| E-17 | Scores consistent with the stated evidence tiers | **FAIL (MINOR)** | B1 and H3 are mixed rows graded at the documented 1.0 multiplier. B1's headline claim, raw-material security through UK and France sourcing, rests on a concall quote. Its documented leg is only the captive solar plant. H3's exclusivity claim, "among the few" GreenPro holders, is self-assessed and unverified against peers. Its documented leg is the certificates. Grading both rows to their documented leg over-credits by 0.6 points. em_score 13.9 on the stricter read. Band unchanged. |
| E-18 | Impact grade consistent with the report's own narrative | **FAIL (MINOR)** | A3 is graded HM, high likelihood and medium impact, giving raw 3 and adjusted 3.0. Section 6E of the same report calls A3 "the smallest in likely financial impact". An HL grade would give raw 2 and em_score 13.5. Band unchanged. |
| E-19 | em_score arithmetic | PASS | Row sum 0.7+0.7+3.0+1.0+1.0+0.7+0.7+3.0+0.7+1.0+2.0 = 14.5. Reproduces exactly. |
| E-20 | Classification band applied | PASS | 14.5 falls in 12-24, which is MODEST MOAT DEVELOPMENT. Correct. |
| E-21 | I1 scored above 0 only with both legs and a documented (b) leg | PASS | I1 = 0. Leg (a) absent, leg (b) not attempted. The report says so explicitly. Verifier C rule 8 satisfied. |
| E-22 | I2 scored above 0 only with a specific named sacrifice | PASS | I2 = 0. The report names the honest answer as "nothing", and correctly classifies the position as execution lead, not configuration. Verifier C rule 8 satisfied. |
| E-23 | I1/I2 contribution stated separately | PASS | "I1/I2 contribution: 0 of 14.5". The 20-Aug-2026 ruling requires this for the operator's review checkpoint. Present, with the checkpoint flagged. |
| E-24 | Bands treated as absolute, no rescale | PASS | The report scores against the unchanged 40/25-39/12-24 bands and cites the EM>=25 UA qualifier correctly. |
| E-25 | Optionality register, four columns, correct membership | PASS | 7 rows. Every row is a zero-scored or claim-only item. None is double-counted in the score. |
| E-26 | Optionality register carried into the YAML | PASS | All 7 rows present as optionality_register[]. |
| E-27 | Section 4A, 4B, 4C complete for R1 | PASS | 4A states NOT FOUND. 4B tabulates amount, duration, enrolment status and competitor sharing. 4C rules the tailwind active but non-exclusive. |
| E-28 | Section 6A to 6E complete | PASS | All five sub-sections present, including the four timeline windows. |
| E-29 | 6C uses the injected B01 block correctly | PASS | Core 56/100, moat 12/60, moats_confirmed 2, MODERATE, AVERAGE. Every value matches B01's YAML. The FLAG-CASH and one-off figures cited in G1 also match B01 exactly. Propagation is clean. |
| E-30 | 6D combined classification from the named set | PASS | AVERAGE is a member of the mandated set. The rule's own language reserves the transition cells for an EXPANSION forward score. Forward is MODEST, so AVERAGE holds. Scope note: prompts/07 names the combined matrix but does not print its cells, so a cell-by-cell re-derivation is not possible from my rule sources. I verified membership, input carriage and reasoning consistency. |
| E-31 | catalysts_12m window discipline | **FAIL (MINOR)** | The field is named for 12 months. Two of five entries carry a 12-24m window. This field feeds Pillar 3 catalyst proximity in Stage 11. A 12-24m catalyst is less proximate than a 12m one. Each entry does state its own window, so a careful Stage 11 read recovers the truth. |
| E-32 | 6E catalyst list matches the YAML list | **FAIL (MINOR)** | The body lists dealer-count reversal as a 12-month catalyst. The YAML omits it and substitutes "total debt holds at or below Rs 350cr". Both are defensible catalysts. The two lists should agree. |
| E-33 | YAML template completeness | PASS | All 17 template fields present with correct types. |
| E-34 | analyst_note 200-word cap | PASS | 162 words. Inside the cap. |
| E-35 | Cross-artifact consistency with B01 | **FAIL (MINOR)** | Three divergences with no reconciling note. First, FY26 capex of Rs 36.75 Cr is anchored to AR FY26 p.155 in B07 and p.158 in B01. Second, the nil-R&D statement is anchored to p.92 in B07 and p.95 in B01. Third, B07 states total debt as Rs 579 Cr for FY24 and Rs 350 Cr for FY26, while B01 states Rs 534.98 Cr and Rs 303.44 Cr. The gap is a lease-liability definition difference, which B01 flags at D3 but B07 never names. B07 also reports WC tenure of 94 and 81 days for FY25 and FY26, against B01's computed 110.51 and 92.42 days on a revenue basis. Both are anchored, but they are different series. Stage 11 must not treat them as one. Page-anchor truth routed to Verifier A. |
| E-36 | Band-proximity and single-row sensitivity disclosed | **FAIL (MINOR)** | em_score 14.5 sits 2.5 points above the 12-point NONE floor. G2 alone carries 3.0 of the 14.5, which is 21%. Removing G2 gives 11.5 and flips em_classification from MODEST to NONE. G2 is also graded "already realised", which sits awkwardly against the scan's own scope line, "moats currently FORMING that do not fully show in historical financials yet". The G2 category text does contemplate a realised trend, so I do not score this as a category misapplication. The sensitivity is real and is not stated anywhere in B07. |

### 2.2 Emerging Moat recomputation summary

| Item | B07 reported | My recomputation | Verdict |
|---|---|---|---|
| Row-by-row adjusted scores | see table | every one of 23 rows reproduces | Concur |
| em_score | 14.5 | 14.5 exactly | Concur |
| em_score, stricter tier read (E-17) | n/a | 13.9 | Same band |
| em_score, A3 impact per 6E (E-18) | n/a | 13.5 | Same band |
| em_score, G2 excluded (E-36) | n/a | 11.5 | **Band flips to NONE** |
| em_classification | MODEST | MODEST as scored | Concur, not robust |
| active_categories | A3, G2, R1 | same 3 | Concur |
| capex_embedded_growth_pct | 2.5 | 2.48 recomputed | Concur |
| I1 / I2 | 0 / 0 | 0 / 0 | Concur |
| combined_assessment | AVERAGE | AVERAGE in every variant | **Concur** |

The combined assessment is robust. Every variant stays far below the EM>=25
UA qualifier, so the AVERAGE combined classification holds. The em_score
itself is not robust. It sits 2.5 points above a band boundary and one row
carries 21% of it.

---

## PART 3: CARRY-FORWARD TO THE PHASE-3 VALUATION AUDIT

These are not B01 or B07 rule failures. They are inputs that phase 3 must
handle. I record them so they are not lost between passes.

1. **Single-credit risk on the working-capital improvement.** B01 Block B4
   scores the WC-days decline at the maximum 5. B07 G2 scores the same
   improvement at 3.0, one of only three active categories. Each stage applied
   its own rule correctly. Stage 11 must not credit this improvement through
   two mechanisms. The Master file forbids it.
2. **Exceptional-item basis.** The Rs 59.70 Cr land and building gain sits
   inside B01's D1 EBITDA, D2 EBIT and the AR-sourced FY26 ROCE. Any Pillar 1
   or entry-basis work must state which basis it uses. B01 names the
   ex-exceptional figures as the decision-relevant ones.
3. **em_score band fragility.** If Stage 11 or FTTCP re-grades G2 or A3, the
   emerging-moat classification can move to NONE. The EM>=25 UA qualifier is
   unaffected either way.
4. **Two debt series in circulation.** Rs 303.44 Cr and Rs 350 Cr both refer
   to FY26. Pick one basis, state it, and carry it through.

---

## PART 4: FINDINGS REGISTER

| # | Severity | Location | Finding |
|---|---|---|---|
| 1 | MAJOR | B01 Block E, E2 | 3-year promoter-change window replaced by a 1-year window, scored at the maximum band, on a change the same report calls unexplained and unverified. Recomputed E2 = 0, Block E 9/20, core 51. Classification unchanged. |
| 2 | MAJOR | B07 YAML, evidence_mix | Counts not reconcilable to the body. Five analyst-inference items claimed with zero tagged in the report. Documented count of 16 contradicts the body's own enumeration. No effect on em_score. |
| 3 | MINOR | B01 Formula Notes, Block A | Two capital-employed bases blended in one ROCE series against the fixed-formula rule. Disclosed and cross-validated. Consequential only at M3. |
| 4 | MINOR | B01 Block B | B1 on 10 years, B2/B3/B4 on 3 years. Block total not comparable to a full-history Block B. No deal-breaker consequence. |
| 5 | MINOR | B01 Block D, D2 | Interest coverage scored on an EBIT basis containing the one-off gain. Recomputed D2 = 1, Block D 12/20. Classification unchanged. |
| 6 | MINOR | B01 Block F, M8 | No rubric band fits a quantified and shrinking distribution network. The report picked the conservative floor and said why. Rubric defect, amendment candidate. |
| 7 | MINOR | B01 M3 and M1 | Two scored inputs unanchored at the point of use: Net Block 676.89 and FY17 operating margin 12.20%. Rule 4 counts these against the stage. Existence routed to Verifier A. |
| 8 | MINOR | B01 output format | Moat profile bars and the classification box absent from the mandated dashboard format. |
| 9 | MINOR | B07 completionist recount | Body and YAML attribute the 13 documented items to different categories. Both total 13. |
| 10 | MINOR | B07 Sections 1, 3, 6B | Several evidence items anchored to a document with no page or slide, against the mandated anchor format. |
| 11 | MINOR | B07 rows B1 and H3 | Mixed-evidence rows graded at the documented multiplier where the headline claim is a management claim. Over-credit 0.6. em_score 13.9 on the stricter read. |
| 12 | MINOR | B07 row A3 | Impact graded medium in the scorecard, called "the smallest in likely financial impact" in Section 6E. em_score 13.5 on the consistent read. |
| 13 | MINOR | B07 YAML, catalysts_12m | Two of five entries carry 12-24m windows in a 12-month field that feeds Pillar 3 catalyst proximity. |
| 14 | MINOR | B07 Section 6E vs YAML | Catalyst lists disagree by one item in each direction. |
| 15 | MINOR | B07 vs B01 | Two page anchors and one debt basis diverge across the reports with no reconciling note. Two different WC-day series also circulate. |
| 16 | MINOR | B07 Section 5 | em_score sits 2.5 points above the NONE floor with 21% resting on one already-realised row. Sensitivity not disclosed. |

Zero CRITICAL findings. No finding, alone or combined, changes the Gate 0
classification of AVERAGE or the combined assessment of AVERAGE.

---

## PART 5: ACCEPTANCE RATE

| Scope | Rules checked | Passed | Failed |
|---|---|---|---|
| Gate 0 (B01) | 54 | 47 | 7 |
| Emerging Moat (B07) | 36 | 27 | 9 |
| **Phase-1 total** | **90** | **74** | **16** |

acceptance_rate = 74 / 90 = 82%.

Above the 60% REWORK floor. No verifier-C REWORK trigger fires. Both stages
are framework-compliant on the load-bearing rules: every block score, every
band, every deal-breaker, the classification matrix, the 23-row scan, the
evidence multipliers, the completionist guard, and the I1/I2 gate all
reproduce. The failures are window substitutions, basis blends, an
unreconcilable count field, and anchor hygiene.

---

```yaml
stage: B12c
company: "VISAKAIND"
run_date: "2026-09-05"
model: claude-opus-4-8
status: complete
scope: "phase-1: gate0 + emoat"
gate0:
  rules_checked: 54
  fails:
    - "G-06 ROCE formula fidelity: proxy capital employed FY17-FY23 blended with AR Schedule-III FY24-FY26"
    - "G-13 Block B window consistency: B1 on 10 years, B2/B3/B4 on 3 years"
    - "G-22 D2 interest coverage scored on an EBIT basis containing the Rs59.70cr one-off; recomputed D2 = 1"
    - "G-27 E2 promoter change: 1-year window substituted for the mandated 3-year, maximum band awarded; recomputed E2 = 0"
    - "G-38 M8 distribution: no rubric band fits a quantified and shrinking network; conservative 0 chosen by interpretation"
    - "G-49 Rule 4 anchors: Net Block 676.89 and FY17 operating margin 12.20% unanchored at point of use"
    - "G-51 Output format: moat profile bars and classification box absent"
emoat:
  rules_checked: 36
  fails:
    - "E-11 completionist recount attributes the 13 documented items differently in body and YAML"
    - "E-13 Rule 3 anchors: several evidence items cite a document with no page or slide"
    - "E-14 evidence_mix not reconcilable to the body; 5 inference items claimed, 0 tagged"
    - "E-17 rows B1 and H3 graded at the documented multiplier on a management-claim headline; over-credit 0.6"
    - "E-18 A3 impact graded medium in the scorecard, called smallest in impact in Section 6E"
    - "E-31 catalysts_12m carries two 12-24m entries in a 12-month field feeding Pillar 3 proximity"
    - "E-32 Section 6E catalyst list and YAML catalysts_12m disagree by one item each way"
    - "E-35 cross-artifact divergence with B01 on two page anchors, the total-debt basis, and the WC-day series"
    - "E-36 em_score 14.5 sits 2.5 points above the NONE floor with 21% on one already-realised row; sensitivity not disclosed"
valuation:
  status: "pending phase 3"
  rules_checked: 0
  fails: []
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: ["NOT ASSESSED - B13 not among phase-1 inputs; deferred to the finalize verifier pass"]}
recomputed_destination_pe: ""
recomputed_decision: ""
findings:
  - {severity: "MAJOR", location: "B01 Block E, E2", description: "Mandated 3-year promoter-change window replaced by a 1-year window and scored at the maximum band of 5, on a +4.82pp move the same report calls unexplained and unverified, with 0.00% change in both named individual promoters. Rule 5 directs N/A and 0 when a data point is unavailable. Recomputed E2 = 0, Block E 9/20, core 51. Classification stays AVERAGE."}
  - {severity: "MAJOR", location: "B07 YAML, evidence_mix", description: "evidence_mix {documented 16, claim 13, inference 5} is not reconcilable to the report body. No analyst-inference item is tagged anywhere, so the count of 5 has zero supporting items. The documented count of 16 contradicts the body, which enumerates 13 items supporting the Moderate rows plus at least 5 further documented facts. No effect on em_score because multipliers apply per category."}
  - {severity: "MINOR", location: "B01 Formula Notes and Block A", description: "Two capital-employed bases blended in one 10-year ROCE series against the fixed-formula rule. Disclosed in input_gaps and cross-validated at FY26 (proxy 12.57% vs AR 11.87%). No effect on A1, A2 or A4. Consequential at M3: on the proxy basis FY26 ROCE clears the >12% leg and M3 would score 1, moat score 13, no class change."}
  - {severity: "MINOR", location: "B01 Block B", description: "B1 runs on 10 years while B2, B3 and B4 run on 3 years, so the 17/20 block total mixes windows. B3's 1.367 ratio is flattered by an FY24-FY26 PAT denominator of 90.50 containing both trough years and the FY26 one-off. Disclosed. Deal-breaker 2 cannot fire in any variant because B1 and B4 alone hold Block B at or above 10."}
  - {severity: "MINOR", location: "B01 Block D, D2", description: "Interest coverage of 4.34x scores 2 on an EBIT numerator containing the Rs59.70cr land gain. The report computes the ex-exceptional 2.53x and calls it the decision-relevant figure, then scores the higher band. Recomputed D2 = 1, Block D 12/20, core 55. Classification stays AVERAGE. D1 tested and robust: ex-exceptional ND/EBITDA is 1.858x, same band."}
  - {severity: "MINOR", location: "B01 Block F, M8", description: "The M8 rubric has no band for a network that is quantified and shrinking. Band 1 reads mentioned-unquantified and band 0 reads none-or-purely-digital; neither fits 4,974 dealers down from 5,246. The report chose 0 and stated why. Conservative and disclosed. The defect is in the rubric. Alternate reading M8 = 1 gives moat score 13, no class change. Framework amendment candidate."}
  - {severity: "MINOR", location: "B01 M3 and M1", description: "Two scored inputs carry no anchor at the point of use. M3's Net Block of 676.89 is unsourced and does not reconcile to B07's AR-sourced net PP&E of 675.98. M1's FY17 operating EBITDA margin of 12.20% is unsourced and its components are not shown. Rule 4 states an unanchored number counts against the stage. Existence routed to Verifier A."}
  - {severity: "MINOR", location: "B01 output format", description: "The mandated dashboard format requires moat profile bars and a classification box. Neither is present. All blocks, line items, strongest and weakest block, and the decision line are present. Presentational only."}
  - {severity: "MINOR", location: "B07 Section 3 recount vs YAML completionist_recount", description: "The body attributes the 13 documented items as A3 5, G2 3, R1 3, plus 2 capex-table items. The YAML attributes them as A3 5, G2 3, R1 5, folding the 2 capex items into R1 without explanation. Both total 13. The recount is the completionist guard artifact and must be exact."}
  - {severity: "MINOR", location: "B07 Sections 1A, 1C, 6B", description: "Several evidence items name a document but give no page or slide, against the mandated (AR p.__) anchor format. Examples: the yarn margin series cited to AR2025/AR2026 segment notes; the 3 ATUM Life stores cited to AR FY26 BRSR; the 22-25% input-cost rise cited to the Aug-2023 call."}
  - {severity: "MINOR", location: "B07 scorecard rows B1 and H3", description: "Both are mixed-evidence rows graded at the documented 1.0 multiplier. B1's headline raw-material-security claim rests on a concall quote, with only the captive solar plant documented. H3's among-the-few GreenPro exclusivity claim is self-assessed and unverified against peers, with only the certificates documented. Grading to the documented leg over-credits 0.6 points. em_score 13.9 on the stricter read. Band unchanged."}
  - {severity: "MINOR", location: "B07 scorecard row A3", description: "A3 is graded HM, raw 3, adjusted 3.0, while Section 6E of the same report calls A3 the smallest in likely financial impact. An HL grade gives raw 2 and em_score 13.5. Band unchanged."}
  - {severity: "MINOR", location: "B07 YAML, catalysts_12m", description: "Two of five entries carry a 12-24m window inside a field named for 12 months. The field feeds Pillar 3 catalyst proximity at Stage 11, where a 12-24m catalyst is less proximate. Each entry does state its own window, so a careful Stage 11 read recovers the truth."}
  - {severity: "MINOR", location: "B07 Section 6E vs YAML catalysts_12m", description: "The body lists dealer-count reversal as a 12-month catalyst; the YAML omits it and substitutes total debt holding at or below Rs350cr. Both are defensible. The two lists should agree."}
  - {severity: "MINOR", location: "B07 vs B01, cross-artifact", description: "Three divergences with no reconciling note. FY26 capex of Rs36.75cr anchored to AR FY26 p.155 in B07 and p.158 in B01. The nil-R&D statement anchored to p.92 in B07 and p.95 in B01. Total debt stated as Rs579cr FY24 and Rs350cr FY26 in B07 against Rs534.98cr and Rs303.44cr in B01, a lease-liability definition gap B01 flags at D3 and B07 never names. B07 also carries WC tenure of 94 and 81 days against B01's computed 110.51 and 92.42 days; different series, both anchored. Page-anchor truth routed to Verifier A."}
  - {severity: "MINOR", location: "B07 Section 5", description: "em_score of 14.5 sits 2.5 points above the 12-point NONE floor, and G2 alone carries 3.0 of it, or 21%. Excluding G2 gives 11.5 and flips em_classification from MODEST to NONE. G2 is graded already-realised, which sits awkwardly against the scan's forming-moat scope line, though the G2 category text does contemplate a realised trend. The sensitivity is not disclosed anywhere in B07."}
critical_count: 0
major_count: 2
minor_count: 14
acceptance_rate: 82
```
