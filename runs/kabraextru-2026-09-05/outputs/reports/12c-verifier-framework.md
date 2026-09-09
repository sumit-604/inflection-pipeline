# STAGE 12C — VERIFIER C: FRAMEWORK ADHERENCE (PHASE 1 SCOPE, RERUN 2)
Company: Kabra Extrusiontechnik Ltd (KABRAEXTRU) | Run date of record: 2026-09-05
Audit date: 2026-09-09 | Model: claude-opus-4-8 | Status: partial-phase1 | Rerun: 2

## SCOPE

Two frameworks audited, both from their own rule source:
- Gate 0 (B01) against `prompts/01-gate-0-pipeline.md`
- Emerging Moat (B07) against `prompts/07-emerging-moat-pipeline.md`

Artifacts read:
- `/home/user/inflection-pipeline/runs/kabraextru-2026-09-05/outputs/reports/01-gate0.md`
- `/home/user/inflection-pipeline/runs/kabraextru-2026-09-05/outputs/blocks/B01-gate0.yaml`
- `/home/user/inflection-pipeline/runs/kabraextru-2026-09-05/outputs/reports/07-emoat.md`
  (audited as amended by the `## REWORK ADDENDUM (2026-09-09)` and its trailing YAML block, which
  is the authoritative B07 block)
- `/home/user/inflection-pipeline/runs/kabraextru-2026-09-05/outputs/blocks/B07-emoat.yaml`

NOT run, by instruction: the valuation-adherence audit (verifier rules 4-7, 11-14). B10 and B11
do not exist. No valuation framework document was loaded. `valuation` stays at zero rules checked,
`recomputed_destination_pe` and `recomputed_decision` stay "pending phase 3", and every
`business_understanding_narrative` field stays at its pending default because the stage-13
synthesis for this rerun has not run. `expectation_ledger` stays at schema defaults for the same
reason. No other pipeline report and no other verifier output was read.

Method: every Gate 0 block score was re-derived from the inputs stated in the B01 report, using
the thresholds in the rule source. I audit rule application. I do not audit company quality, and I
do not audit whether a number exists in a source PDF (Verifier A owns that, and its verdicts bind).
Where a rule fails, the recomputed value sits beside it. Where a number could not be recomputed
from the stated inputs, it is NOT FOUND, never estimated.

---

# PART 1: GATE 0 (B01) COMPLIANCE

## 1.1 Operating rules and formula definitions

| # | Rule (source) | Test | Verdict | Recomputed / note |
|---|---|---|---|---|
| G1 | Operating rule 1: entire scorecard in one response, no stops | All blocks A-F, classification, moat profile, decision line present | PASS | — |
| G2 | Operating rule 2: no qualitative judgments, only numbers and the scoring rules | Decision line recommends a pipeline posture ("the numbers argue for a REWORK / INSUFFICIENT EVIDENCE posture") | **FAIL (MINOR)** | Classification itself is correct (AVOID). The verdict-set recommendation is not this stage's output. No score effect. |
| G3 | Operating rule 3: show every extracted number and each metric score | Per-year ROCE/ROE table, CFO/PAT series, WC-day table, peer table, all 12 moat tests | PASS | — |
| G4 | Operating rule 4: source anchor on every extracted number | Screener Data_Sheet, AR FY26 p.51/82/105-106/110/123-124/148-150/165/167, AR FY25 p.83/89/125/148-151, peer Data_Sheets | PASS | Per-number source fidelity is Verifier A's call, not mine. |
| G5 | Operating rule 5: grounded claims; unavailable data marked N/A and scored 0; never estimate | E3 pledge NOT FOUND scored 0; FY17-FY23 capex NOT FOUND; FY17-FY23 trade payables NOT FOUND. No gap filled with a typical value. | PASS | — |
| G6 | Operating rule 6: use available history, min 3 years, open with the data-availability line | "Data available: 10 years (FY2017 to FY2026)... Scoring adapted to 10-year history." | PASS | — |
| G7 | Formula: ROCE = EBIT ÷ (Total Assets − Current Liabilities); use the source's own figure if provided, else compute and state "computed". Formulas are "fixed, do not substitute alternatives". | Denominator substituted with Net Worth + Borrowings; stated as a proxy and cross-validated to AR Note 43 for FY25-FY26 only | **FAIL (MINOR)** | Literal TA−CL basis is NOT computable from the stated inputs (screener Data_Sheet does not split current vs non-current liabilities), so the alternative median is NOT FOUND, not estimated. Direction of bias is stated in Finding F-2. Max plausible effect: A1 stays 1 unless median ≥15%; M3 could move 0→1. Core score unchanged, classification unchanged. |
| G8 | Formula: ROE = PAT ÷ average Net Worth; earliest year may use closing, state so | "FY17 uses closing net worth only (no FY16 opening data available), stated" | PASS | FY17 20.42/226.33 = 9.02%. All 10 ROE cells re-derived and match. |
| G9 | Formula: WC days = Rec + Inv − Pay, revenue basis unless COGS explicitly available, state basis | Sales named as the divisor input; all three components computed on revenue | PASS | FY26: 64.7 + 231.6 − 52.6 = 243.7. Matches. |
| G10 | Formula: FCF = CFO − capex (PPE + intangibles, exclude acquisitions) | FY24 46.85 / FY25 68.15 / FY26 37.38 Cr capex, from AR consolidated cash flow | PASS | FY26: 8.96 − 37.38 = −28.42. Matches. FY24 intangibles inflow treated at face value and flagged as a data quirk. |
| G11 | Formula: CAGR = (End ÷ Start)^(1/years) − 1 | C1 uses 9 periods across 10 data years | PASS | (451.05/276.08)^(1/9) − 1 = 5.607%. Report 5.61%. Matches. |
| G12 | CAGR edge rule: negative or zero endpoint → "N/M (negative endpoint)", score 0 | C2 with FY26 PAT −5.37 Cr | PASS | C2 = 0. Correct. |
| G13 | CAGR edge rule: swing noted in data_notes, no synthetic CAGR | data_notes carries "profit-to-loss swing, FY25 (PAT +32.20 Cr) to FY26 (PAT −5.37 Cr)" | PASS | The written rule names the loss-to-profit direction. The report logged the mirror case. Extra disclosure, not a breach. |
| G14 | CAGR edge rule: C4 = 0 and note when PAT CAGR is N/M | C4 scored 0 with the rule cited | PASS | — |

## 1.2 Re-derived block scores

Block A, from the report's own ROCE/ROE series:

| # | Rule threshold | Report input | Report score | Recomputed | Verdict |
|---|---|---|---|---|---|
| G15 | A1 median ROCE: 10-14.9 = 1 | sorted 5th/6th = 10.07, 10.55 | 1 | median 10.31% → 1 | PASS |
| G16 | A2 min single-year ROCE: <8 = 0 | FY26 0.62% | 0 | 0.62% → 0 | PASS |
| G17 | A3 median ROE: <12 = 0 | sorted 5th/6th = 8.70, 9.02 | 0 | median 8.86% → 0 | PASS |
| G18 | A4 ROCE trend: decline >5pp = 0 | 0.62% vs 10.55% | 0 | −9.93pp → 0 | PASS |
| G19 | Block A total | — | 1 / 20 | 1 + 0 + 0 + 0 = 1 | PASS |

Block B:

| # | Rule threshold | Report input | Report score | Recomputed | Verdict |
|---|---|---|---|---|---|
| G20 | B1 cum CFO ÷ cum PAT: 0.50-0.69 = 1 | 122.26 / 225.18 | 1 | series re-added: CFO 122.26, PAT 225.18, ratio 0.5430 → 1 | PASS |
| G21 | B2 FCF-positive year proportion: <50% = 0 | 0 of 3 computable years | 0 | 0% → 0 | PASS (3-year window forced by corpus, disclosed in data_notes; rule 6 permits the available history) |
| G22 | B3 cum FCF ÷ cum PAT: negative = 0 | −67.13 / 60.65 | 0 | −1.107 → 0 | PASS |
| G23 | B4 change in WC days: increase >15 = 0 | 243.7 vs 154.1 | 0 | +89.6 days → 0 | PASS (latest-vs-earliest-available stated as FY26 vs FY24, with the reason) |
| G24 | Block B total | — | 1 / 20 | 1 + 0 + 0 + 0 = 1 | PASS |

Block C:

| # | Rule threshold | Report input | Report score | Recomputed | Verdict |
|---|---|---|---|---|---|
| G25 | C1 revenue CAGR: 5-9.9 = 1 | FY17 276.08 → FY26 451.05 | 1 | 5.607% → 1 | PASS |
| G26 | C2 PAT CAGR: N/M = 0 | FY26 PAT negative | 0 | N/M → 0 | PASS |
| G27 | C3 positive YoY revenue years: <50% = 0 | 3 of 9 | 0 | up in FY21/22/23 only = 33.3% → 0 | PASS |
| G28 | C4 PAT CAGR − revenue CAGR: 0 when N/M | — | 0 | 0 | PASS |
| G29 | Block C total | — | 1 / 20 | 1 + 0 + 0 + 0 = 1 | PASS |

Block D (latest = FY26):

| # | Rule threshold | Report input | Report score | Recomputed | Verdict |
|---|---|---|---|---|---|
| G30 | D1 ND/EBITDA: >3x = 0 | (145.06 − 3.08) / (3.61 + 30.25) | 0 | 141.98 / 33.86 = 4.193x → 0 | PASS |
| G31 | D2 interest coverage: <1.5x = 0 | 3.61 / 11.39 | 0 | 0.3169x → 0 | PASS |
| G32 | D3 debt/equity: 0.1-0.5 = 4 | 145.06 / 441.49 | 4 | 0.3286x → 4 | PASS (AR Note 43 cross-check 0.32x) |
| G33 | D4 current ratio: 1.5-1.99 = 4 | 1.55x, AR Note 43 | 4 | 1.55x → 4 | PASS (source's own figure used, correct preference) |
| G34 | Block D total | — | 8 / 20 | 0 + 0 + 4 + 4 = 8 | PASS |

Block E (latest = FY26):

| # | Rule threshold | Report input | Report score | Recomputed | Verdict |
|---|---|---|---|---|---|
| G35 | E1 promoter holding: ≥60% = 5 | 60.49%, AR FY26 Note 14.4 | 5 | 60.49% → 5 | PASS |
| G36 | E2 3-year change: ±1% = 3 | FY26 60.49% vs FY23 ~60.23% | 3 | +0.26pp → 3. Insensitive: FY24 60.24% as the base gives +0.25pp → 3 | PASS |
| G37 | E3 pledge: NOT FOUND → 0 per grounding rule | no shareholding filing in corpus | 0 | 0 | PASS (correctly not read as 0% pledge) |
| G38 | E4 contingent liabilities ÷ net worth: 5-15% = 3 | 25.05 / 441.49 | 3 | components sum 2,505.13 lakh; 5.674% → 3 | PASS |
| G39 | Block E total | — | 11 / 20 | 5 + 3 + 0 + 3 = 11 | PASS |

Block F, the 12 quantitative moat tests:

| # | Test | Report input | Report score | Recomputed | Verdict |
|---|---|---|---|---|---|
| G40 | M1 pricing power | margin −8.51pp, rev CAGR 5.61% | 0 | outside every scoring band → 0 | PASS |
| G41 | M2 cost advantage | 2.31% vs peer median 18.40% | 0 | −16.09pp, "below" → 0 | PASS |
| G42 | M3 capital efficiency | FAT 1.83x, ROCE 10.31%/0.62% | 0 | 1-point tier needs ROCE >12% → 0 | PASS |
| G43 | M4 customer stickiness | 6 decline years | 0 | 3+ decline years → 0 | PASS |
| G44 | M5 scale and dominance | 3rd of 4 mcap, lowest margin | 1 | top-5 mcap tier → 1 | PASS |
| G45 | M6 technology / R&D | R&D/rev 1.22%, margin below peer median | 0 | 1-point tier needs both legs → 0 | PASS |
| G46 | M7 regulatory / licence | unregulated | 0 | 0 | PASS |
| G47 | M8 distribution | quantified reach, no growth trend | 1 | see Observation O-1 (band gap) | PASS |
| G48 | M9 brand | GM proxy 35.72% vs peer median 37.02% | 0 | −1.30pp, "at/below" → 0 | PASS (proxy basis stated as the rule requires) |
| G49 | M10 switching costs | overall growth, 6 decline years | 1 | "2+ decline years" tier → 1 | PASS |
| G50 | M11 network effects | latest 3yr −12.4%, prior 3yr +44.9% | 0 | −12.36% vs +44.91%, latest < prior → 0 | PASS (two-window test used; 10 years available) |
| G51 | M12 negative WC / float | 154-244 days | 0 | >45 days → 0 | PASS |
| G52 | Moat classification band | 0 tests ≥3 | NONE | 0 present → NONE | PASS |
| G53 | moats_confirmed count | — | 0 | 0 | PASS |
| G54 | "PEER DATA NEEDED" rule (score 0, never guess peer figures) | 3 peer Data_Sheets supplied; comparability limits logged in data_notes | — | no peer figure invented | PASS |

Block F total re-derived: 0+0+0+0+1+0+0+1+0+1+0+0 = **3 / 60**. Matches.

## 1.3 Classification, data confidence, deal-breakers

| # | Rule | Report | Recomputed | Verdict |
|---|---|---|---|---|
| G55 | Core score = A+B+C+D+E | 22 | 1+1+1+8+11 = 22 | PASS |
| G56 | Grand total = core + moat | 25 | 22 + 3 = 25 | PASS |
| G57 | Data confidence: 10+ yrs = full, no downgrade | history_downgrade false | 10 years → full tier, no downgrade | PASS |
| G58 | Classification matrix: core <40 = AVOID | AVOID | 22 < 40 → AVOID | PASS |
| G59 | All nine deal-breakers evaluated, triggered ones recorded | 1, 2, 6, 7, 8 triggered; 3, 4, 5, 9 tested and not triggered | 1 (A=1<8) yes; 2 (B=1<8) yes; 3 (10.31% not <10%) no; 4 (0.543 not <0.50) no; 5 NOT FOUND, not counted; 6 (4.19x and 0.317x) yes → AVOID; 7 (6 of 9) yes; 8 (FY26 PAT −5.37) yes; 9 (10 years) no | PASS |
| G60 | Cap application produces the final classification | AVOID | Binding cap is #6 (AVOID); matrix independently gives AVOID | PASS |
| G61 | State WHICH years drive any deal-breaker | #6 FY26; #7 FY18,19,20,24,25,26; #8 FY26 | Year-specific breakers all carry their years | PASS |

## 1.4 Output and block-schema rules

| # | Rule | Verdict | Note |
|---|---|---|---|
| G62 | Full dashboard format: all blocks, line items with anchors, moat profile bars, classification box, strongest/weakest block, decision line | PASS | All present. |
| G63 | Ends with exactly the specified fenced YAML block, all fields | PASS | 21 fields present, no field missing, none added. Block file is byte-consistent with the report block. |
| G64 | FLAG-GATE0 required when classification ≤ AVERAGE with historical depressors identified | PASS | Flag present, depressor named and segment-identified. |
| G65 | block_b_trend = improving / stable / deteriorating with the one number | PASS | "deteriorating - working capital days rose from ~154 (FY24) to ~244 (FY26)". |
| G66 | analyst_note ≤200 words, strict cap | PASS | ~159 words. |

**Gate 0: 66 rules checked, 64 PASS, 2 FAIL (both MINOR).**

---

# PART 2: EMERGING MOAT (B07) COMPLIANCE

Audited as amended by the 2026-09-09 rework addendum. The last fenced YAML block in the file is
treated as authoritative and matches `outputs/blocks/B07-emoat.yaml` exactly.

## 2.1 Operating rules and evidence taxonomy

| # | Rule | Test | Verdict | Note |
|---|---|---|---|---|
| E1 | Rule 1: all six sections in one response | Sections 1-6 plus the optionality register present | PASS | — |
| E2 | Rule 2: exactly three evidence tiers (📄 / 🎙️ / 🔍) | A fourth tier, "📰 MEDIA-REPORTED", is declared in the report's own "Evidence taxonomy used throughout" framing paragraph and used at Section 3 H2 and Section 6A | **FAIL (MINOR)** | The addendum closes this at block level only. See Finding F-3. No scoring weight anywhere; em_score unaffected at 9. |
| E3 | Rule 2: tier applied to every evidence item | Tier symbol carried on evidence lines throughout Sections 1-4 | PASS | "STALE" and "(neg)" are qualifiers on an in-taxonomy tier, not new tiers. |
| E4 | Rule 3: source anchor on every evidence item | AR26 p.4-5/17/22-23/28-30/32-38/51/82-83/87-88/105-106/110/127/148-149; AR25 p.30/37/83; Inv. Pres. slides 14/16/17/18/19/22/23 | PASS | — |
| E5 | Rule 4: skepticism, hard evidence over promises | B2 scored 0 despite the Dec-2023 ARAI/IATF claims; H2 scored 0 on decades-old tie-ups; the dropped-claims pattern flagged | PASS | — |
| E6 | Rule 5: "NO EVIDENCE FOUND" stated, never force-fit | 19 of 22 categories explicitly NO EVIDENCE FOUND | PASS | — |
| E7 | Rule 6: completionist guard threshold logic (≥12 active → re-examine) | 4 categories carry a non-zero score, 2 are Moderate | PASS | Well under the trigger; the guard was still run. |
| E8 | Rule 6: recount stated in the required form | "📄 recount performed: 9 documented items across 4 categories" | PASS | Matches the block's completionist_recount field. |

## 2.2 Section coverage

| # | Rule | Verdict | Note |
|---|---|---|---|
| E9 | Section 1A: pipeline products with status, evidence type, launch, revenue potential, differentiation | PASS | 4 rows; unavailable fields marked NOT FOUND, not estimated. |
| E10 | Section 1B: diversification direction with evidence and timeline | PASS | Includes two explicit negative-evidence directions. |
| E11 | Section 1C: revenue mix table, current %, 3-year %, margin direction, profitability impact | PASS | 3-year % marked NOT FOUND with the reason. |
| E12 | Section 2A: capex table with the seven required columns | PASS | Unavailable cells marked NOT FOUND. |
| E13 | Section 2B: utilisation per facility | PASS | NOT FOUND stated; the <10% read is labelled 🔍 inference, not a disclosed figure. |
| E14 | Section 2C: arithmetic shown | PASS | 31.77 + 9.12 = 40.89; 40.89 × 1.83 = 74.83. |
| E15 | Section 2C: expressed as % above current revenue, carried to the block | PASS | 74.83 / 451.05 = 16.59% → 16.6%; capex_embedded_growth_pct 16.6. |
| E16 | Section 2D: new geography or market entries | PASS | NO EVIDENCE FOUND, with the export decline as counter-evidence. |
| E17 | Section 3: all 22 categories addressed or explicitly NO EVIDENCE | PASS | A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, I1-I2 = 22 present. |
| E18 | R1 addressed (Section 4) | PASS | 4A, 4B, 4C all present. |
| E19 | Section 3 summary table: all rows with evidence?, type, strength, time to materialise | PASS | 23 rows (22 + R1), 4 required columns. |
| E20 | Strong/Moderate count stated | PASS | "Count with Strong/Moderate evidence: 2 of 22 (A4, C2)." |
| E21 | Category 21 (I1) two-leg rule; score >0 only if both legs evidenced, (b) leg carrying ≥1 📄 | PASS | Scored 0; leg (a) absent (no patents, no named cohort, remuneration annexure covers KMP only). Rule cited by name. |
| E22 | Category 22 (I2) named-sacrifice rule; score >0 only if the sacrifice is specific | PASS | Scored 0; honest answer recorded as "nothing must be destroyed" per the rule's own instruction. |
| E23 | Section 4A regulatory approvals in pipeline | PASS | NOT FOUND stated. |
| E24 | Section 4B policy tailwinds with amounts, duration, enrolment status, competitor sharing | PASS | Five schemes with outlays, end dates, and an explicit "no enrolment disclosed" for PLI ACC and PM E-DRIVE. |
| E25 | Section 4C regulatory moat assessment: active vs emerging, time to kick in, sustainability | PASS | All three answered; scored low on the differentiation test, which is the correct test. |

## 2.3 Scorecard re-derivation

Matrix: HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0. Multipliers: 📄 1.0, 🎙️ 0.7, 🔍 0.5.

| Row | Stated L/I | Stated raw | Stated tier | Stated adjusted | Recomputed | Verdict |
|---|---|---|---|---|---|---|
| A4 | HM | 3 | 📄 | 3.0 | 3 × 1.0 = 3.0 | PASS |
| C2 | HM | 3 | 📄 | 3.0 | 3 × 1.0 = 3.0 | PASS |
| F2 | LM | 1 | 📄 | 1.0 | 1 × 1.0 = 1.0 | PASS |
| R1 | HL | 2 | 📄 | 2.0 | 2 × 1.0 = 2.0 | PASS |
| 19 others | none | 0 | — | 0 | 0 | PASS |

| # | Rule | Verdict | Recomputed |
|---|---|---|---|
| E26 | Section 5 table carries all 23 rows | PASS | 23 rows counted. |
| E27 | Raw score matches the likelihood × impact matrix on every scored row | PASS | HM→3, LM→1, HL→2. All correct. |
| E28 | Evidence multiplier applied correctly on every scored row | PASS | All four scored rows are 📄 at 1.0x; no 🎙️ or 🔍 row carries a non-zero score. |
| E29 | Adjusted total arithmetic | PASS | 3.0 + 3.0 + 1.0 + 2.0 = 9.0. em_score 9. |
| E30 | Bands absolute, no rescale (operator ruling 20-Aug-2026) | PASS | ≥40 / 25-39 / 12-24 / <12 used unchanged. |
| E31 | em_classification matches the band | PASS | 9 < 12 → NO MEANINGFUL EMERGING MOAT; block field "NONE". |
| E32 | Score stated against the 92 ceiling | PASS | "em_score = 9 / 92." |
| E33 | I1/I2 contribution stated separately in the scoring table | PASS | "I1/I2 contribution: 0", with the operator-ruling reference. |
| E34 | Scores consistent with the stated evidence tiers (a 🎙️-only category scoring as if 📄 is a finding) | PASS | A4 rests on a launched product and a described completed development in statutory Annexure-4; C2 on a Note 38 numerical disclosure; F2 on the Note 2B CWIP schedule; R1 on published scheme outlays. A3 (🎙️), C1 (🎙️), F1 (🔍) all correctly score 0. See Observation O-3 for the closest call. |
| E35 | Optionality register: table with the four required columns | PASS | 6 rows, all four columns populated. |
| E36 | Register carries only 0-scored or 🎙️/🔍-only items; registered options are watched, never scored | PASS | None of the six feeds a Section 5 score. |
| E37 | Section 6A: four windows with a milestone in each | PASS | 12m / 12-24m / 24-36m / 3-5yr. |
| E38 | Section 6B: risks to each top-scoring moat with early warning signs | PASS | A4 and C2, both with early warnings. |
| E39 | Section 6C: combined table built on the INJECTED Gate 0 block | PASS | Core 22/100, moat 3/60, moats_confirmed 0, both classifications carried correctly. |
| E40 | Section 6D: classification from the standard set, HIGH POTENTIAL and TURNAROUND rows given full reasoning | PASS | AVOID selected; a full TURNAROUND/HIGH POTENTIAL counterfactual is written out as the prompt demands. |
| E41 | Section 6E: final card with the moat evolution map per family, 12m catalysts, biggest risk | PASS | All nine families mapped; four catalysts; one biggest risk. |

## 2.4 Rework addendum closure audit (items E-35, E-33, E-32, E-13)

| # | Item | Required fix | Verdict | Note |
|---|---|---|---|---|
| E42 | E-35: A4 time_to_materialise carried an unanchored 12-24m date | Restate to NOT FOUND | PASS | Block now reads "ongoing (RESS live now; HV e-bus packs NOT FOUND)". The addendum explicitly supersedes both the Section 3 summary row and the YAML field, and re-cites AR26 p.28 to confirm no date exists. See Observation O-2 on the un-edited body row. |
| E43 | E-33: catalysts_12m entry 4 carried a 12-24m window inside a 12-month field | Restate to a genuine 0-12m observable, or move it | PASS | Restated to the Note 2B CWIP-appearance proxy at "0-12m (FY27 AR due ~May-2027)"; the commissioning test stays in Section 6A's 12-24m bucket. Roughly 8 months from the 2026-09-05 date of record, so the window fits. |
| E44 | E-32: evidence_mix {25, 10, 6} was not auditable | Replace with an auditable count | PASS | Now {documented: 9, claim: 0, inference: 0}, scoped to items feeding a non-zero Section 5 score, enumerated with category id and page anchor. I traced all nine to the report body: A4-1 (1A row 1, AR26 p.5/p.29), A4-2 (1A row 2, AR26 p.28-29), C2-1 and C2-2 (Section 3 C2, AR26 p.106), F2-1 (Section 3 F2, AR25/AR26 p.83), F2-2 (Section 2A row 2, AR26 p.110), R1-1/2/3 (Section 4B, AR26 p.32-35). All nine exist. See Observation O-4. |
| E45 | evidence_mix consistent with completionist_recount | Both fields on the same basis | PASS | Both now use the identical 9-item / 4-category basis. |
| E46 | catalysts_12m windows fit the field | All entries inside 12 months | PASS | "0-12m (FY27)", "0-12m", "0-12m (FY27 AR due ~May-2027)". |
| E47 | E-13: a fourth "media-reported" tier is outside the three-tier taxonomy | Remove the fourth tier | See E2 | Block level closed: the item is out of catalysts_12m and labelled "NON-CORPUS, unscored... no evidence tier assigned" in the register. Report body not aligned. Counted once, at E2. |

## 2.5 Block schema rules

| # | Rule | Verdict | Note |
|---|---|---|---|
| E48 | Block carries every schema field | PASS | All 19 schema fields present. One extra field, `rework_addendum: "2026-09-09"`, added and documented by the addendum. Observation O-5. |
| E49 | active_categories carries Strong/Moderate rows only | PASS | A4 and C2 only. F2 (Weak) and R1 (Weak/Low) correctly excluded despite non-zero scores. |
| E50 | analyst_note ≤200 words | PASS | ~138 words. |
| E51 | Block file matches the authoritative report YAML | PASS | `outputs/blocks/B07-emoat.yaml` is the addendum-amended block, not the superseded original. |

Rules E42 through E47 count as six checks (E47 folded into E2), so the emoat total is **49 rules
checked, 48 PASS, 1 FAIL (MINOR)**.

---

# PART 3: FINDINGS

## F-1 — MINOR — Gate 0 decision line issues a pipeline verdict the stage does not own

Location: `outputs/reports/01-gate0.md`, DECISION LINE, final sentence.
Rule: `prompts/01-gate-0-pipeline.md` operating rule 2, "No qualitative judgments. Only numbers
and the scoring rules provided."

The report writes that "the numbers argue for a REWORK / INSUFFICIENT EVIDENCE posture pending
resolution of the promoter-pledge gap, the CRISIL rationale gap, and clarity on whether the
Battery division loss is a temporary scale-up cost or a structural drag." REWORK and INSUFFICIENT
EVIDENCE are two of the five run-level verdicts. Gate 0 produces a classification, a flag, and a
decision line. It does not set the run verdict.

Recomputed: no effect. The stage's own output, classification AVOID, is correct and unchanged.
The report does state that it does not halt the pipeline, so the CLAUDE.md rule against halting on
company quality is respected. The defect is scope, not substance.

Fix: delete the verdict-set sentence, or restate it as a flag for the orchestrator.

## F-2 — MINOR — ROCE denominator substituted against a "fixed, do not substitute" formula

Location: `outputs/reports/01-gate0.md`, FORMULA NOTES, "Capital Employed" bullet; propagates to
A1, A2, A4, M3 and to deal-breaker 3.
Rule: `prompts/01-gate-0-pipeline.md`, FORMULA DEFINITIONS header ("fixed, do not substitute
alternatives") and the ROCE bullet ("EBIT ÷ (Total Assets − Current Liabilities)").

The report computes capital employed as Net Worth + Borrowings, not Total Assets − Current
Liabilities. It states the substitution openly, marks the figures "computed", and cross-validates
FY25 and FY26 against the company's own AR Note 43 ROCE (computed 8.63% vs disclosed 8.67%;
computed 0.62% vs disclosed 0.61%). The other eight years carry no cross-check.

Recomputed: the literal TA − CL basis is NOT COMPUTABLE from the inputs the report states, because
the screener Data_Sheet does not split current from non-current liabilities. The alternative median
is NOT FOUND. It is not estimated here.

Direction of bias, stated for the operator: TA − CL excludes current borrowings, while the proxy
denominator includes them. FY26 borrowings are almost entirely short-term (Rs 141.09 Cr of
Rs 145.06 Cr, per the report's own Note 17 read). The proxy therefore uses the larger denominator
and, on the stated evidence, understates ROCE rather than flattering it.

Score sensitivity, bounded:
- A1 stays 1 unless the true median reaches 15%; the band 10-14.9 is 5pp wide and the proxy median
  is 10.31%.
- M3's 1-point tier needs ROCE >12%; a higher true median could move M3 from 0 to 1, lifting
  moat_score 3 → 4. Moat class stays NONE (still zero tests at ≥3).
- Deal-breaker 3 (median ROCE <10%) is 0.31pp away on the proxy basis, and an understating proxy
  moves it further from firing, not closer.
- Core score 22 and classification AVOID are unchanged under every case above.

Fix: state whether the source supplies its own ROCE column; if it does not, keep the proxy but
label the metric as basis-limited wherever it approaches a deal-breaker line.

## F-3 — MINOR — A fourth evidence tier survives in the B07 report body after the rework

Location: `outputs/reports/07-emoat.md` header framing paragraph (lines 13-15), Section 3 H2, and
Section 6A first bullet.
Rule: `prompts/07-emerging-moat-pipeline.md` operating rule 2, which defines exactly three tiers.

The 2026-09-09 addendum closes E-13 at block level. The preferential-issue item is out of
catalysts_12m, and the optionality register row now reads "NON-CORPUS, unscored... no evidence tier
assigned". The block is clean.

The report body is not. The framing paragraph still defines the taxonomy "used throughout" as four
tiers, ending "and — for one item only... 📰 MEDIA-REPORTED". Section 3 H2 still says the item is
"carried here as 📰 MEDIA-REPORTED, unscored, in the optionality register", which is now false in
two ways: the register no longer carries that tier, and the tier does not exist. Section 6A still
prefixes the item "(📰, unconfirmed in this corpus...)". The addendum names all three of these
locations in its own analysis of the defect, then corrects only the two block-level artifacts and
declares everything above its heading unchanged.

Recomputed: em_score 9, unchanged. The item carried no scoring weight before or after. No category
strength, no classification, no downstream Pillar 3 input moves.

Why it still counts: this is the CLAUDE.md dependency-alignment rule. An edit that changes a
ruling in one section must align every dependent section in the same commit. The addendum
identified the dependent sections and left them. A reader who stops before the addendum reads a
four-tier taxonomy as the report's operating standard.

Fix: strike the 📰 tier from the framing paragraph, H2, and 6A, replacing it with the addendum's
"NON-CORPUS, unscored, no tier assigned" wording. One edit, three locations.

---

# PART 4: OBSERVATIONS (not fails, no rule breached)

**O-1. M8 sits in a gap between bands.** The 5-point band needs quantified reach that is growing;
the 1-point band reads "mentioned unquantified"; the 0 band reads "none or purely digital". Kabra's
reach is quantified (100+ countries, 15,000+ installations) but static and repeated verbatim across
two ARs, which fits none of the three literally. The report chose 1, stated the reasoning, and took
the conservative side of the only other candidate (3, which fails on the ≥15% CAGR leg). One point
on a 60-point moat score, no effect on moat class.

**O-2. The E-35 fix supersedes rather than edits.** Section 3's summary row for A4 still reads
"12-24m". The addendum explicitly supersedes it, names the field, and re-cites the source. That is
a documented supersession and is compliant, but it leaves the table row contradicting the block for
any reader who stops at Section 3. The same one-edit fix that closes F-3 should sweep this row.

**O-3. A4's 1.0x multiplier is the closest tier call in the scan.** The two 📄 items are a launched
product (RESS, AR26 p.5/p.29) and a completed development described in statutory Annexure-4
(HV liquid-cooled packs, AR26 p.28-29). Both sit inside the 📄 definition. The platform-architecture
reading around them is closer to 🔍. If A4 were graded 🎙️ at 0.7x, em_score would be 8.1 and the
classification would still be NONE. No decision rests on it.

**O-4. The R1 sub-count inside evidence_mix is a selection, not a rule output.** Section 4B lists at
least five documented policy items (JJM 2.0, PM E-DRIVE, PLI ACC, the 5% GST rate, and the Union
Budget package). The enumeration credits three. Because all of them feed the single R1 score, the
stated scope rule ("items feeding a non-zero raw score") does not by itself fix the count at three.
Each listed item is individually traceable with an anchor, which is what the fix asked for, so the
field is auditable. The count is reproducible only from the addendum's list, not from the rule.

**O-5. Two schema deviations, both benign.** The B07 block adds `rework_addendum: "2026-09-09"`,
which the prompt's "exactly this fenced YAML block" instruction does not provide for. It buys
provenance and is documented. Separately, two catalysts_12m rows carry compound evidence_type
labels ("documented (base commitment); inference (...)"). Both components are inside the taxonomy;
the schema does not enumerate a single-value set for that field.

---

# PART 5: SUMMARY

| Framework | Rules checked | Passed | Failed | Critical | Major | Minor |
|---|---|---|---|---|---|---|
| Gate 0 (B01) | 66 | 64 | 2 | 0 | 0 | 2 |
| Emerging Moat (B07) | 49 | 48 | 1 | 0 | 0 | 1 |
| Valuation (B11) | 0 | — | — | — | — | — |
| **Total** | **115** | **112** | **3** | **0** | **0** | **3** |

Acceptance rate: 112 / 115 = **97%**. Well clear of the 60% REWORK trigger.

Concurrence on the two headline outputs. Gate 0 core score 22/100, moat score 3/60, moat class
NONE, classification AVOID: every block re-derived to the same number, and deal-breaker 6 fires
independently of the matrix, exactly as the report states. Emerging Moat em_score 9/92 with
classification NONE: the scoring table re-adds to 9.0, and all four scored rows use the correct raw
band and the correct 1.0x multiplier.

The three defects are all presentational or basis-declaration issues. None changes a score, a
classification, or a downstream input. No finding rises to MAJOR.

The four rework items are closed on the numbers. Three are closed cleanly (E-35, E-33, E-32). E-13
is closed in the block and left open in the report body, which is Finding F-3. It needs one edit
across three locations, and the same edit should sweep the stale A4 row from Observation O-2.

Two items are carried forward for the phase-3 audit, not resolved here:
- The ROCE basis question (F-2). Section 1B and FTTCP consume ROCE. If phase 3 uses the same
  proxy basis, it should say so in the same words, and the FTTCP ROCE verdict remains the sole
  Pillar 1 authority regardless.
- The Gate 0 input gaps that the block already carries: promoter pledge NOT FOUND, no CRISIL
  rationale, no shareholding filing, and the sector-cap row flagged for phase-3 confirmation.

---

```yaml
stage: B12c
company: "KABRAEXTRU"
run_date: "2026-09-05"
model: claude-opus-4-8
status: partial-phase1
rerun: 2
gate0:
  rules_checked: 66
  fails:
    - "G2 operating rule 2: decision line recommends a run-level REWORK / INSUFFICIENT EVIDENCE posture; Gate 0 owns a classification and a flag, not the verdict set. No score effect."
    - "G7 ROCE formula: capital employed computed as Net Worth + Borrowings against a 'fixed, do not substitute' definition of Total Assets - Current Liabilities. Disclosed and cross-validated to AR Note 43 for FY25-FY26 only; literal basis NOT COMPUTABLE from the stated inputs."
emoat:
  rules_checked: 49
  fails:
    - "E2 operating rule 2: fourth evidence tier 'media-reported' still declared in the report body framing paragraph and used at Section 3 H2 and Section 6A. Rework item E-13 closed at block level only. em_score unaffected at 9."
valuation: {rules_checked: 0, fails: []}
expectation_ledger: {present: false, downside_row: false, all_rows_confirm_by: false, all_rows_metric_threshold: false, prob_in_range: false, decay_status_valid: false, off_ledger_credit: false, residual_pct_cmp: 0, residual_starter_cap_ok: true, fails: []}
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: []}
recomputed_destination_pe: "pending phase 3"
recomputed_decision: "pending phase 3"
findings:
  - {severity: "MINOR", location: "01-gate0.md, DECISION LINE, final sentence", rule: "prompts/01-gate-0-pipeline.md operating rule 2", issue: "Recommends a run-level REWORK / INSUFFICIENT EVIDENCE posture, which is orchestrator vocabulary, not a Gate 0 output.", recomputed: "No change. Classification AVOID stands; core 22/100 re-derived identical."}
  - {severity: "MINOR", location: "01-gate0.md, FORMULA NOTES 'Capital Employed'; propagates to A1, A2, A4, M3, deal-breaker 3", rule: "prompts/01-gate-0-pipeline.md FORMULA DEFINITIONS, ROCE", issue: "Net Worth + Borrowings substituted for Total Assets - Current Liabilities under a 'do not substitute' instruction; cross-validated for FY25-FY26 only, eight years unchecked.", recomputed: "Literal-basis median ROCE NOT FOUND (not computable from stated inputs, not estimated). Proxy median 10.31% -> A1 = 1. Proxy includes current borrowings so it understates ROCE. Bounded effect: M3 could move 0 -> 1, moat_score 3 -> 4, moat class stays NONE; core 22 and AVOID unchanged; deal-breaker 3 stays unfired."}
  - {severity: "MINOR", location: "07-emoat.md lines 13-15 (taxonomy framing paragraph), Section 3 H2, Section 6A bullet 1", rule: "prompts/07-emerging-moat-pipeline.md operating rule 2 (three-tier taxonomy); CLAUDE.md dependency alignment", issue: "Fourth tier 'media-reported' survives in the report body after the 2026-09-09 addendum closed E-13 in the block only. The addendum named these three locations and did not align them.", recomputed: "em_score 9 unchanged; the item carries no scoring weight. Block-level catalysts_12m and optionality_register are correct."}
critical_count: 0
major_count: 0
minor_count: 3
acceptance_rate: 97
```
