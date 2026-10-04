# STAGE 12 VERIFIER C: FRAMEWORK ADHERENCE (PHASE 1 SCOPE)
Company: SYNGENE (Syngene International Ltd) | Run date: 2026-09-15 | Emits: B12c

## SCOPE AND INPUTS

Phase 1 scope only. This audit covers Gate 0 (B01) and the Emerging Moat scan (B07).
The valuation audit (B10, B11), the Expectation Ledger rules (13-14), and the Business
Understanding Narrative rule (9) are out of scope. They are PENDING PHASE 3 / STAGE 13.

Rule sources read:
- prompts/01-gate-0-pipeline.md (Gate 0 thresholds, formulas, CAGR edge rules, matrix, deal-breakers)
- prompts/07-emerging-moat-pipeline.md (22-category scan plus R1, multipliers, recount, Family I)
- prompts/12-verifiers-pipeline.md (Verifier C section)
- CLAUDE.md global NEVER rules where they bind document stages (one improvement one mechanism; company memory is never anchored evidence; never estimate a missing number)

Artifacts audited:
- runs/syngene-2026-09-15/outputs/blocks/B01-gate0.yaml and outputs/reports/01-gate0.md
- runs/syngene-2026-09-15/outputs/blocks/B07-emoat.yaml and outputs/reports/07-emoat.md

Boundary. This audit judges rule application. It does not judge whether a number exists in a
source. Verifier A owns that question, and its verdicts bind. Where a framework finding touches a
number, the number is routed to Verifier A and no fidelity verdict is given here.

---

## PART 1: GATE 0 (B01) COMPLIANCE TABLE

Method: every block score re-derived from the inputs B01 itself states, against the thresholds in
prompts/01. Arithmetic re-run where the inputs are shown.

### 1A. Formula and edge rules

| # | Rule | Result | Recomputed / note |
|---|---|---|---|
| G01 | Opening "Data available: X years" line | PASS | 9 years, FY2018 to FY2026 stated (01-gate0.md l.4) |
| G02 | ROCE = EBIT / (TA - CL); "computed" stated when source ROCE absent | PASS | FY24 668.0/5,007.3 = 13.34%; FY25 713.0/5,399.5 = 13.20%; FY26 459.7/5,502.4 = 8.35%. AR Note 38 own-definition ROCE kept out of scoring, correct |
| G03 | ROE = PAT / average NW; closing-only year stated | PASS | FY18 closing-only disclosed |
| G04 | WC Days formula, and the revenue vs COGS basis stated | FAIL (MINOR) | Basis never stated for inventory or payable days (01-gate0.md l.108). Rule text: "state which basis was used" |
| G05 | FCF = CFO - (PPE + intangibles), ex acquisitions | PASS | FY25 1,167.6 - 770.1 = 397.5; FY26 915.2 - 368.2 = 547.0 |
| G06 | CAGR formula | PASS | Revenue (3,738.7/1,423.1)^(1/8) - 1 = 12.83%; PAT (316.7/305.4)^(1/8) - 1 = 0.46% |
| G07 | CAGR edge rules (negative endpoint N/M, loss-to-profit note, C4 N/M) | PASS | Both endpoints positive. No annual loss-to-profit swing. C4 computable. Q1FY27 loss is a quarter, outside the annual window |

### 1B. Block scores re-derived

| # | Metric | Stated input | Band per prompts/01 | Stated score | Recomputed | Result |
|---|---|---|---|---|---|---|
| G08 | A1 Median ROCE | 13.20% | 10-14.9 = **1** | 3 | **1** | **FAIL (MAJOR)** |
| G09 | A2 Min ROCE | 8.35% | 8-11.9 = 1 | 1 | 1 | PASS |
| G10 | A3 Median ROE | 13.43% | 12-14.9 = 2 | 2 | 2 | PASS |
| G11 | A4 ROCE trend | -4.99pp | 3-5pp decline = 1 | 1 | 1 | PASS |
| G12 | B1 CFO/PAT | 1.92 | >=1.00 = 5 | 5 | 5 | PASS |
| G13 | B2 FCF+ years | 2 of 2 | 100% = 5 | 5 | 5 (band only; see G46) | PASS |
| G14 | B3 FCF/PAT | 944.5/812.9 = 1.16 | >=0.60 = 5 | 5 | 5 (band only; see G46) | PASS |
| G15 | B4 WC Days change | -3.52 days | +/-5 = 3 | 3 | 3 (band only; see G46) | PASS |
| G16 | C1 Revenue CAGR | 12.83% | 10-14.9 = 3 | 3 | 3 | PASS |
| G17 | C2 PAT CAGR | 0.46% | <5 = 0 | 0 | 0 | PASS |
| G18 | C3 Positive YoY years | 8 of 8 | 100% = 5 | 5 | 5 | PASS |
| G19 | C4 PAT - Rev CAGR | -12.37pp | <-8pp = 0 | 0 | 0 | PASS |
| G20 | D1 ND/EBITDA | net cash 374.6 | net cash = 5 | 5 | 5 | PASS |
| G21 | D2 Interest cover | 459.7/48.8 = 9.42x | 5-9.9 = 4 | 4 | 4 | PASS |
| G22 | D3 D/E | 458.4/4,839.1 = 0.095 | <0.1 = 5 | 5 | 5 | PASS |
| G23 | D4 Current ratio | 21,428/15,523 = 1.38 | 1.2-1.49 = 2 | 2 | 2 | PASS |
| G24 | E1 Promoter holding | 52.59% | 50-59.9 = 4 | 4 | 4 | PASS |
| G25 | E2 Promoter change | -2.13pp (2 yrs) | decreased 1-3% = 1 | 1 | 1 (band only; see G47) | PASS |
| G26 | E3 Pledge | N/A | N/A scores 0 (rule 5) | 0 | 0 | PASS |
| G27 | E4 Contingent/NW | 531.2/4,703.8 = 11.29% | 5-15 = 3 | 3 | 3 | PASS |
| G28 | M1 Pricing power | margin -8.65pp, CAGR 12.83% | decline >5pp falls to else = 0 | 0 | 0 | PASS |
| G29 | M2 Cost advantage | 4.27pp below median 28.91% | below = 0 | 0 | 0 | PASS |
| G30 | M3 Capital efficiency | FAT 1.25x, ROCE 8.35% | else = 0 | 0 | 0 | PASS (note N1) |
| G31 | M4 Customer stickiness | 0 decline yrs, rec. days -18.75 | +/-10 test fails for 5; "max 1 decline year" = 3 | 3 | 3 | PASS |
| G32 | M5 Scale | rank 4 of 4 supplied names; segment universe absent | PEER DATA NEEDED = 0 | 0 | 0 | PASS |
| G33 | M6 R&D | no rupee figure | N/A = 0 | 0 | 0 | PASS |
| G34 | M7 Regulatory | player count absent | PEER DATA NEEDED = 0 | 0 | 0 | PASS (note N2) |
| G35 | M8 Distribution | none | none = 0 | 0 | 0 | PASS |
| G36 | M9 Brand (GM proxy) | +4.76pp, CAGR 12.83% | 3 tier needs >=5pp; 1 is the nearest tier met | 1 | 1 | PASS (note N3) |
| G37 | M10 Switching costs | grew every year, rec. days fell | = 5 | 5 | 5 | PASS |
| G38 | M11 Network effects | 5.40% latest 3y vs 16.65% prior | all tiers fail = 0 | 0 | 0 | PASS |
| G39 | M12 Negative WC | 33.08 / 29.56 days | 15-45 = 1 | 1 | 1 (band only; see G46) | PASS |

### 1C. Aggregation, classification, overrides, output

| # | Rule | Result | Recomputed / note |
|---|---|---|---|
| G40 | Moats present (>=3) and moat class | PASS | M4, M10 = 2, MODERATE |
| G41 | Block sums, core, moat, grand total arithmetic as stated | PASS | 7+18+8+16+8 = 57; moat 10; grand 67. Arithmetic is correct on the stated line scores. The A1 error in G08 flows through: A = 5, core = 55, grand = 65 |
| G42 | Data confidence tier | PASS | 9 years = moderate, no downgrade. Block A runs on 3 years; the tier rule keys to overall history, so no LIMITED downgrade applies |
| G43 | Classification matrix | PASS | Core 57 stated and 55 recomputed both sit in 40-59 = AVERAGE |
| G44 | Deal-breaker application and "which years drive it" | PASS | #1 triggered (A = 7 stated, 5 recomputed, both < 8), cap max GOOD, non-binding. FY26 named as driver |
| G45 | All nine deal-breakers stated as checked | FAIL (MINOR) | #2 (Block B < 8) and #6 (ND/EBITDA > 3x AND IC < 3x) are absent from the checked list (01-gate0.md l.241-247). Neither triggers on stated inputs |
| G46 | Minimum 3-year history per scored metric; stated input gaps consistent with sources actually used | **FAIL (MAJOR)** | See Finding F-G2 |
| G47 | E2 3-year window rule | FAIL (MINOR) | Scored 1 on a 2-year window (Jun-2024 to Jun-2026). Rule 5 reading: 3-year change not in provided data = N/A, score 0. E = 7 under that reading |
| G48 | FLAG-GATE0 raised for classification <= AVERAGE with depressors | PASS | Raised with named, dated depressors |
| G49 | YAML schema and data_notes content | FAIL (MINOR) | Schema asks data_notes to carry "proxy bases used, PEER DATA NEEDED items". The M9 GM proxy is absent from data_notes. PEER DATA NEEDED (M5, M7) sits only in input_gaps. data_notes also calls M6 "archetype-inapplicable" while the report table scores it "N/A (not in provided data)" |
| G50 | analyst_note <= 200 words | PASS | About 140 words |
| G51 | block_b_trend carries the one number | PASS | CFO -21.6% YoY |
| G52 | Narrative fields consistent with the report body and sibling stage | FAIL (MINOR) | analyst_note says "newly capitalised Stelis/Baltimore biologics licence". The body (l.55-58) names the Stelis licence (Unit 3, Bengaluru) as capitalised. B07 2A states Bayview (Baltimore, Maryland) is NOT capitalised at 31-Mar-2026. The note conflates two assets |

Gate 0 tally: 52 rules checked, 7 FAIL (2 MAJOR, 5 MINOR), 45 PASS.

### 1D. Gate 0 findings in detail

**F-G1 (MAJOR). A1 misbanded.** Median ROCE 13.20% falls in the 10-14.9% band, which scores 1
under prompts/01 l.56. B01 scored 3, the 15-19.9% value. Block A = 5, not 7. Core = 55, not 57.
Grand total = 65, not 67. Classification stays AVERAGE. Deal-breaker #1 stays triggered and
non-binding. B07 6C carries the stale core of 57, so the correction propagates there.

**F-G2 (MAJOR). Two-year windows below the 3-year minimum, with a stated gap the maker's own sources contradict.**
B2, B3, B4 and M12 score on FY25-FY26 only. The stated reason is that Trade Payables and capex
exist only for FY25-FY26. But Block A takes FY24 Total Current Liabilities from the "AR2025
consol BS" (01-gate0.md l.80).

[INFERENCE] An Ind AS Schedule III consolidated balance sheet shows Trade Payables as its own line
inside current liabilities. It also carries a prior-year column. The AR2025 cash flow statement
carries "Purchase of property, plant and equipment" for FY25 and FY24. So the FY24 inputs for B2,
B3, B4 and M12 were most likely in the corpus the maker already opened. The FY-2 year would have
given a 3-year window.

Two readings:
- (a) Maker reading. "Minimum 3 years" binds the whole scorecard, not each metric, so a 2-year
  sub-window with a flag is valid. Scores stand: B = 18.
- (b) Strict reading. Rule 6 sets a 3-year floor and rule 5 scores unavailable data 0. B2, B3, B4
  and M12 become N/A, and E2 follows (G47). Then B = 5, E = 7, moat = 9. With F-G1, core = 5 + 5
  + 8 + 16 + 7 = 41. That is still AVERAGE, one point above the AVOID band (<40). Deal-breaker #2
  triggers (B < 8, cap max GOOD) and does not bind.

The separating observation: open the AR2025 consolidated balance sheet and cash flow statement.
If FY24 Trade Payables and FY24 PPE purchases appear there, reading (b)'s N/A is not needed. The
correct fix is to recompute B2, B3, B4 and M12 on FY24-FY26. Classification survives under every
reading. The margin above AVOID under reading (b) is 1 point, so the operator should see it.

Numbers route to Verifier A. This audit does not say whether the FY24 lines exist.

### 1E. Gate 0 notes (not counted as fails)

- N1 (M3). The rubric does not say whether ROCE means the spot year or the median. B01 used FY26
  spot (8.35%). The median (13.20%) with FAT 1.25x gives 1. No moat-present change either way.
- N2 (M7). Contract manufacturing under USFDA/cGMP is regulated (B07 4A). Margin fell 8.65pp, so
  the 3 and 5 tiers fail whatever the player count. The best possible score is 1. B01's 0 follows
  the PEER DATA NEEDED rule as written.
- N3 (M9). The rubric has a gap. It defines no tier for "above peers by <5pp with growth above
  8%". B01's 1 is the defensible nearest tier. A score of 3 would give 3 moats present, still
  MODERATE.
- N4 (rubric design, operator item). M4 and M10 score the same two inputs: revenue-decline years
  and receivable days. Together they give the only 2 confirmed moats. B01 applied the rubric as
  written. The rubric double-credits one observation, and only an operator ruling can change that.
- N5 (EBITDA definition). M1 and M2 build EBITDA from PBT, and FY26 PBT includes the Rs 46.2 cr
  net exceptional charge. LBF1 uses screener Sales minus Expenses. Adding the charge back (about
  1.24pp) leaves M1 at 0 and M2 at 0. No score change. B01 should declare one definition.

---

## PART 2: EMERGING MOAT (B07) COMPLIANCE TABLE

### 2A. Structure, taxonomy, anchors

| # | Rule | Result | Note |
|---|---|---|---|
| E01 | Six sections plus optionality register present | PASS | Sections 1-6 and register present |
| E02 | Not-FTTCP separation stated | PASS | Header l.3 |
| E03 | Evidence taxonomy applied to each evidence item | PASS | DOC / CLAIM / INFER on every table row |
| E04 | Anchors are source documents; company memory is never anchored evidence | **FAIL (MAJOR)** | See Finding F-E1 |
| E05 | 1A status/evidence/timing; 1B directions; 1C mix table with honest NOT FOUND | PASS | Mix target marked NOT FOUND, not estimated |
| E06 | 2A-2D present; 2C arithmetic shown | PASS | 1,040 x 1.24 = 1,290; /3,739 = 34.5%. Ceiling caveat stated |
| E07 | NO EVIDENCE stated where none; no force-fit | PASS | A2, A4, B1, B3, D2, H1, I1, I2 |
| E08 | Never estimate a missing number | FAIL (MINOR) | 2A converts "$36.5mn (~Rs 300cr at FY25 rates)" with no stated rate or source. Not load-bearing for any score |

### 2B. Scan coverage and scoring

| # | Rule | Result | Recomputed / note |
|---|---|---|---|
| E09 | All 23 rows (22 + R1) addressed in the summary table and the scorecard | PASS | 23 rows in both |
| E10 | Strong/Moderate count stated | PASS | 6 (A1, B2, C1, F1, H2, H3) |
| E11 | Completionist guard threshold (>=12 active triggers re-exam) | PASS | 6 active, guard not triggered |
| E12 | Recount line present and reconciles to Section 3 | FAIL (MINOR) | Line says "across 9 categories" but lists 10 (A1, B2, C1, C2, E1, F1, G1, G2, H2, H3). Stated 14 DOC items. A plain count of DOC rows in the Section 3 tables gives about 22-23 (A1 4, B2 2, C1 2, C2 2, E1 1, F1 2, G1 2, G2 1, H2 3, H3 4). evidence_mix.documented = 14 inherits the same count. Guard outcome unaffected |
| E13 | L x I to raw mapping per rubric (HH 4, HM/MH 3, HL/MM/LH 2, ML/LM 1, LL 1) | PASS | All 23 rows map correctly (E1 L/M = 1, H3 H/L = 2, H2 M/H = 3) |
| E14 | No CLAIM-only or INFER-only category scored at the DOC multiplier | PASS | B2 excludes Amgen/Baxter CLAIM; H2 scores on the DOC deal signing; no inflation found |
| E15 | Tier labels consistent across Section 3 table, summary table and scorecard | FAIL (MINOR) | See Finding F-E3 (A1) |
| E16 | Raw score consistent with the category's own stated strength and reading | FAIL (MINOR) | C2: Section 3 grades it Weak and names mechanical Zoetis fall-out as "the more evidenced explanation", with a flat ~400 customer count. Scored M/M = 2.0, the same raw as Moderate F1. Every other Weak row scores L/L = 1. Recomputed C2 = 1.0 |
| E17 | Adjusted total arithmetic and band | PASS | Sum of 13 non-zero rows = 23.2; 12-24 = MODEST |
| E18 | One improvement, one mechanism; emerging vs existing standard applied evenly | **FAIL (MAJOR)** | See Finding F-E2 |
| E19 | I1/I2 contribution stated separately | PASS | 0 of 23.2 |
| E20 | Category 21 (I1) present; >0 only with both legs and a DOC (b) leg | PASS | Present, 0. (a) not evidenced; (b) addressed |
| E21 | Category 22 (I2) present; >0 only with a named specific sacrifice | PASS | Present, 0. "Nothing must be destroyed" = execution lead |
| E22 | I2 test applied "for each moat claimed anywhere in this scan" | FAIL (MINOR) | Test run only on BMS (C1/B2). A1 (Unit 3 / Bayview), F1, H2 and H3 not tested. Likely score-neutral |
| E23 | F2 cross-references injected B05 promise-delivery record | PASS | Grade C, 2/2/4 cited |
| E24 | Section 4 R1: 4A approvals with competitor column; 4B schemes with enrolment and sharing; 4C assessment | PASS | Present |

### 2C. Register, Section 6, output

| # | Rule | Result | Note |
|---|---|---|---|
| E25 | Optionality register: qualifying rows, four columns, carried to YAML | PASS | 7 rows, table matches YAML. Bayview dual presence handled under E15 |
| E26 | 6A-6E present; 6C uses the injected B01 values | PASS | 57 / 2 / MODERATE / AVERAGE match the B01 block. F-G1 later corrects core to 55 |
| E27 | catalysts_12m inside the 12-month window | FAIL (MINOR) | Run date 15-Sep-2026, so the window ends Sep-2027. Rows 2 and 4 carry "FY27-FY28". Row 2 keys to "double-digit growth starting FY28", which 6A files under 12-24m |
| E28 | Output: report ends with the exact fenced YAML; block matches schema | FAIL (MINOR) | 07-emoat.md ends at INPUT GAPS with no fenced YAML. B07-emoat.yaml adds a non-schema key `one_line_note_placeholder: ""` (l.35). Cosmetic: 6A says "mid-25s margin", YAML says "mid-20s" |
| E29 | em_classification enum and band | PASS | MODEST, 23 |
| E30 | analyst_note <= 200 words | PASS | About 130 words |

6D combined classification (AVERAGE): NOT VERIFIABLE and not counted. prompts/07 names the
standard matrix labels but does not define the cells, so this audit cannot re-derive the call.
Rule-source gap for operator attention.

Emerging Moat tally: 30 rules checked, 9 FAIL (2 MAJOR, 7 MINOR), 21 PASS.

### 2D. Emerging Moat findings in detail

**F-E1 (MAJOR). Company memory used as an evidence anchor, including under a load-bearing flag.**
CLAUDE.md MEMORY: company memory "is memory to weigh, never anchored evidence". prompts/07 rule 3
requires source anchors of the form (AR p.__), (Q_ FY__ call), (Inv. Pres. slide __). B07
anchors these items to "company memory":
- 1C and FLAG-EMOAT-SEGMENT-MISMATCH: Research Services "78% Q1FY27"
- 2C: CDMO share "59% (Q4FY26) to 22% (Q1FY27)"
- 1A / 4A / catalysts_12m[0]: Bayview "operationalization in FY27" ("company memory Board's Report p.69")
- 2A / 2D: Bayview acquisition $36.5mn ("company memory, external SEC source")
- H2: Zoetis "nearly $50 million" and the 15-Jul-2022 press release ("external, company memory")
- A1 INFER row: "no listed Indian pure-play biologics CDMO exists"
- B2: Amgen and Baxter dedicated centres

The segment-mismatch flag and the 6D "single most decision-relevant finding" both rest on the 78%
and 22% split. The rule failure is the anchor type. It is not a claim that the figures are wrong.
Fix: re-anchor to the Q1FY27 results segment note, the Q1FY27 investor presentation, or the
Jul-2026 concall page, or mark NOT FOUND. Figures route to Verifier A.

**F-E2 (MAJOR). One relationship event credited through three categories, and the existing-moat exclusion applied unevenly.**
The BMS extension to 2035 (Reg 30, 19-Jan-2026) is the anchoring DOC item in B2 (4.0), C1 (4.0)
and H2 (3.0). Those three rows carry 11.0 of 23.2 points, 47%. B07's own flag concedes that "the
two Strong-scoring categories (B2, C1) both anchor to BMS".

Two further inconsistencies:
- 6E lists "switching costs (dedicated R&D centres, BMS to 2035)" as an EXISTING Gate 0 moat.
- 4C excludes approvals already in place from emerging credit because they are "already reflected
  in the Gate 0 moats_confirmed count". B07 does not apply that standard to the B2 certifications
  ("all current") or to the BMS centre, which has run since 1998.

Two readings:
- (a) B2, C1 and H2 measure different facets (lock-in, ecosystem, partnership), so one
  relationship can evidence all three.
- (b) CLAUDE.md "never credit one quality improvement through two mechanisms" binds, and 4C's
  existing-moat standard applies to every row.

The separating observation: does each scored row rest on a DOC item that no other row already
credits? C1 keeps the BMS extension (4.0). B2 is left with existing certifications: 0 under the
4C standard, or 2.0 (M/M) if treated as still forming. H2 is left with the BioHub Maryland
founding-partner DOC item: 1.0 (L/L). Recomputed total under (b) = 17.2 to 19.2, before F-E3 and
E16. Classification stays MODEST.

**F-E3 (MINOR). A1 tier label mismatch, and Bayview both scored and registered.**
The Section 3 A1 table lists four DOC items and one INFER item. It lists zero CLAIM items. The
summary labels A1 "DOC+CLAIM". The scorecard applies CLAIM 0.7 because "Bayview dominant,
unresolved". Two readings:
- (a) The DOC items drive A1: the Unit 3 USFDA VAI, and the Bayview pre-check application (the
  taxonomy counts a submitted regulatory application as DOC). Score 3 x 1.0 = 3.0.
- (b) The forming increment is Bayview full approval and fill, which is unproven. But that item
  already sits in the optionality register, and registered options "are watched, never scored".

The separating observation: which item the MH likelihood keys to. Recomputed A1 = 2.1 or 3.0.

### 2E. EM score sensitivity across all readings

| Reading | em_score | Class | EM >= 25 UA qualifier |
|---|---|---|---|
| As stated | 23.2 | MODEST | not met |
| A1 at DOC (F-E3 a) only | 24.1 | MODEST | not met |
| Single-credit BMS (F-E2 b) + C2 at L/L (E16), A1 as stated | 16.2 to 18.2 | MODEST | not met |
| Single-credit BMS + C2 at L/L + A1 at DOC | 17.1 to 19.1 | MODEST | not met |

Range 16.2 to 24.1. MODEST under every reading. The EM >= 25 UA qualifier (prompts/07 l.12-13)
is not met under any reading. The highest reading (24.1) is 0.9 below it. Phase 3 should treat
the qualifier as not met, not borderline.

---

## PART 3: VALUATION AUDIT

PENDING PHASE 3. B10 and B11 do not exist in phase 1. Rules 4, 5 (valuation severity), 6, 7,
11, 12, 13 and 14 are not run. The valuation framework documents were not loaded, per scope.
Rule 9 (Business Understanding Narrative) is pending stage 13. Rule 10 (B09b dossier) fires at
/finalize.

---

## CONSOLIDATED FINDINGS

| # | Severity | Location | Rule | Stated | Recomputed | Note |
|---|---|---|---|---|---|---|
| F-G1 | MAJOR | 01-gate0.md l.84; B01 blocks.A, core_score, grand_total | A1 band | A1 = 3; A = 7; core 57; grand 67 | A1 = 1; A = 5; core 55; grand 65 | AVERAGE unchanged; propagates to B07 6C |
| F-G2 | MAJOR | 01-gate0.md l.106-108, l.190; B01 input_gaps[1-2] | 3-year minimum; gaps consistent with sources used | B2 5, B3 5, B4 3, M12 1 on FY25-26 | Recompute on FY24-26 from AR2025 comparatives; strict floor B = 5, core 41 | AVERAGE under all readings; 1 pt above AVOID at the floor |
| F-G3 | MINOR | 01-gate0.md l.108 | WC basis stated | not stated | state revenue or COGS basis | |
| F-G4 | MINOR | 01-gate0.md l.241-247 | all deal-breakers checked | #2, #6 omitted | neither triggers | |
| F-G5 | MINOR | 01-gate0.md l.155-159 | E2 3-year window | 1 on 2 years | 0 under rule 5 N/A | E = 7 |
| F-G6 | MINOR | B01 data_notes | schema content | GM proxy and PEER DATA NEEDED not in data_notes; M6 label conflict | add | |
| F-G7 | MINOR | B01 analyst_note | narrative consistency | "Stelis/Baltimore" capitalised | Stelis (Unit 3) capitalised; Bayview not (B07 2A) | |
| F-E1 | MAJOR | 07-emoat.md 1A, 1C, 2A, 2C, A1, B2, H2, 4A; B07 flags[0], catalysts_12m[0] | company memory never anchored evidence | memory-anchored figures under load-bearing flag | re-anchor to filed source or NOT FOUND | figures to Verifier A |
| F-E2 | MAJOR | 07-emoat.md B2, C1, H2, 4C, 6E | one improvement one mechanism; existing vs emerging | B2 4.0 + C1 4.0 + H2 3.0 on one event | C1 4.0, B2 0-2.0, H2 1.0; total 17.2-19.2 | MODEST unchanged |
| F-E3 | MINOR | 07-emoat.md l.83-90, l.198, l.261 | tier label consistency; register never scored | A1 CLAIM 2.1 | 2.1 or 3.0 | |
| F-E4 | MINOR | 07-emoat.md l.121-126, l.269 | strength vs raw consistency | C2 M/M 2.0 | L/L 1.0 | |
| F-E5 | MINOR | 07-emoat.md l.224; B07 completionist_recount, evidence_mix | recount reconciles | 14 items / 9 categories | ~22-23 items / 10 categories | guard unaffected |
| F-E6 | MINOR | 07-emoat.md l.192 | I2 applied to each moat | BMS only | test A1, F1, H2, H3 | likely score-neutral |
| F-E7 | MINOR | B07 catalysts_12m[1], [3] | 12-month window | FY27-FY28 | move to 6A 12-24m | |
| F-E8 | MINOR | 07-emoat.md end; B07-emoat.yaml l.35 | output format | no fenced YAML in report; non-schema key | append block; drop key | |
| F-E9 | MINOR | 07-emoat.md l.49 | never estimate | ~Rs 300cr at unstated rate | state rate and source or NOT FOUND | not scored |

Critical 0 | Major 4 | Minor 12. Rules checked 82 (Gate 0 52, EM 30). Passed 66. Acceptance 80%.

No finding changes a classification. Gate 0 stays AVERAGE. EM stays MODEST. The combined
assessment stays AVERAGE, though that cell cannot be re-derived from the rule source. The two
operator-visible items: Gate 0 core drops to 41 at the strict floor (F-G2), and the EM >= 25 UA
qualifier is not met under any reading (Part 2E).

```yaml
stage: B12c
company: "SYNGENE"
run_date: "2026-09-15"
model: claude-opus-5
status: complete
gate0: {rules_checked: 52, fails: ["G08 A1 misband: 13.20% scores 1 not 3; A 7->5, core 57->55, grand 67->65 (MAJOR)", "G46 B2/B3/B4/M12 on 2-year window below 3-year minimum; stated payables/capex gap contradicted by maker's own AR2025 consol BS use for FY24; strict floor core 41, still AVERAGE (MAJOR)", "G04 WC days basis not stated (MINOR)", "G45 deal-breakers #2 and #6 not stated as checked (MINOR)", "G47 E2 scored 1 on 2-year window; rule 5 N/A reading = 0 (MINOR)", "G49 data_notes omits M9 GM proxy and PEER DATA NEEDED; M6 label conflict (MINOR)", "G52 analyst_note conflates Stelis Unit 3 and Bayview capitalisation (MINOR)"]}
emoat: {rules_checked: 30, fails: ["E04 company memory used as evidence anchor incl. 78%/22% segment split under FLAG-EMOAT-SEGMENT-MISMATCH and 6D (MAJOR)", "E18 BMS 2035 extension credited in B2, C1, H2 (11.0 of 23.2 pts); 4C existing-moat exclusion not applied to B2/C1; recomputed 17.2-19.2, MODEST (MAJOR)", "E08 USD to INR conversion at unstated rate (MINOR)", "E12 recount says 9 categories lists 10; 14 DOC items vs ~22-23 in Section 3 tables (MINOR)", "E15 A1 tier: Section 3 has zero CLAIM items but scored CLAIM 0.7; Bayview both scored and registered; 2.1 vs 3.0 (MINOR)", "E16 C2 graded Weak and read as mechanical but scored M/M 2.0; recomputed 1.0 (MINOR)", "E22 I2 test applied to BMS only, not each claimed moat (MINOR)", "E27 catalysts_12m rows 2 and 4 extend past Sep-2027 (MINOR)", "E28 report lacks fenced YAML; block carries non-schema key one_line_note_placeholder (MINOR)"]}
valuation: {rules_checked: 0, fails: []}   # PENDING PHASE 3: B10/B11 not in phase-1 scope
expectation_ledger: {present: false, downside_row: false, all_rows_confirm_by: false, all_rows_metric_threshold: false, prob_in_range: false, decay_status_valid: false, off_ledger_credit: false, residual_pct_cmp: 0, residual_starter_cap_ok: true, fails: []}  # NOT RUN: pending phase 3 (rules 13-14); defaults are placeholders, not findings
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: []}  # NOT RUN: pending stage 13; defaults are placeholders, not findings
recomputed_destination_pe: ""  # pending phase 3
recomputed_decision: ""        # concur: Gate 0 AVERAGE (core 55 recomputed; strict-window floor 41), EM MODEST (range 16.2-24.1), combined AVERAGE
findings:
  - {severity: "MAJOR", location: "01-gate0.md l.84; B01 blocks.A/core_score/grand_total", rule: "A1 band", stated: "A1=3, A=7, core 57, grand 67", recomputed: "A1=1, A=5, core 55, grand 65", note: "classification AVERAGE unchanged; B07 6C carries stale 57"}
  - {severity: "MAJOR", location: "01-gate0.md l.106-108, l.190; B01 input_gaps", rule: "3-year minimum; stated gaps consistent with sources used", stated: "B2 5, B3 5, B4 3, M12 1 on FY25-FY26", recomputed: "recompute on FY24-FY26 from AR2025 comparatives; strict N/A floor B=5, E=7, core 41", note: "AVERAGE under every reading; floor 1 pt above AVOID; FY24 line existence routed to Verifier A"}
  - {severity: "MINOR", location: "01-gate0.md l.108", rule: "WC days basis stated", stated: "not stated", recomputed: "n/a", note: ""}
  - {severity: "MINOR", location: "01-gate0.md l.241-247", rule: "all deal-breakers checked", stated: "#2 and #6 omitted", recomputed: "neither triggers on stated inputs", note: ""}
  - {severity: "MINOR", location: "01-gate0.md l.155-159", rule: "E2 3-year window / rule 5 N/A", stated: "E2=1 on 2 years", recomputed: "E2=0, E=7", note: ""}
  - {severity: "MINOR", location: "B01 data_notes", rule: "schema content", stated: "GM proxy and PEER DATA NEEDED absent; M6 label conflict", recomputed: "n/a", note: ""}
  - {severity: "MINOR", location: "B01 analyst_note", rule: "narrative consistency", stated: "Stelis/Baltimore licence capitalised", recomputed: "Stelis Unit 3 capitalised; Bayview not capitalised per B07 2A", note: ""}
  - {severity: "MAJOR", location: "07-emoat.md 1A,1C,2A,2C,A1,B2,H2,4A; B07 flags[0], catalysts_12m[0]", rule: "company memory is never anchored evidence; prompts/07 rule 3", stated: "memory-anchored figures under load-bearing segment-mismatch flag", recomputed: "re-anchor to filed source or NOT FOUND", note: "anchor-type failure only; figures routed to Verifier A"}
  - {severity: "MAJOR", location: "07-emoat.md B2, C1, H2, 4C, 6E", rule: "one improvement one mechanism; existing vs emerging standard", stated: "B2 4.0 + C1 4.0 + H2 3.0 on BMS 2035 extension; em_score 23.2", recomputed: "C1 4.0, B2 0-2.0, H2 1.0; em_score 17.2-19.2", note: "MODEST unchanged; EM>=25 UA qualifier not met under any reading (max 24.1)"}
  - {severity: "MINOR", location: "07-emoat.md l.83-90, l.198, l.261", rule: "tier label consistency; register never scored", stated: "A1 CLAIM 0.7 = 2.1", recomputed: "2.1 or 3.0", note: ""}
  - {severity: "MINOR", location: "07-emoat.md l.121-126, l.269", rule: "raw score consistent with stated strength", stated: "C2 M/M 2.0", recomputed: "L/L 1.0", note: ""}
  - {severity: "MINOR", location: "07-emoat.md l.224; B07 completionist_recount, evidence_mix", rule: "recount reconciles", stated: "14 items / 9 categories", recomputed: "about 22-23 items / 10 categories", note: "guard not triggered either way"}
  - {severity: "MINOR", location: "07-emoat.md l.192", rule: "I2 test for each claimed moat", stated: "BMS only", recomputed: "test A1, F1, H2, H3", note: "likely score-neutral"}
  - {severity: "MINOR", location: "B07 catalysts_12m[1], [3]", rule: "12-month window", stated: "FY27-FY28", recomputed: "file under 12-24m", note: ""}
  - {severity: "MINOR", location: "07-emoat.md end; B07-emoat.yaml l.35", rule: "exact fenced YAML output", stated: "no YAML in report; non-schema key", recomputed: "n/a", note: "cosmetic: 6A mid-25s vs YAML mid-20s"}
  - {severity: "MINOR", location: "07-emoat.md l.49", rule: "never estimate a missing number", stated: "~Rs 300cr at FY25 rates", recomputed: "state rate and source or NOT FOUND", note: "not used in scoring"}
critical_count: 0
major_count: 4
minor_count: 12
acceptance_rate: 80             # 66 passed / 82 checked (gate0 52 + emoat 30); 6D combined cell not verifiable from rule source, not counted
```
