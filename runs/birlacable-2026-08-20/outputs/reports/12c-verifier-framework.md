# STAGE 12C — VERIFIER C: FRAMEWORK ADHERENCE (PHASE 1 SCOPE)
Company: Birla Cable Ltd (BIRLACABLE) | Run date: 2026-08-20 | Model: claude-opus-4-8

Scope: Gate 0 (B01) and Emerging Moat (B07) only. The valuation-adherence audit
(B11, B10) does not run in this phase. B10 and B11 do not exist yet. They are
produced in phase 3. The valuation section of the block below is left blank with
status pending-phase-3.

Rule sources read (the only two loaded, per phase-1 scope):
- prompts/01-gate-0-pipeline.md
- prompts/07-emerging-moat-pipeline.md

Artifacts audited:
- outputs/reports/01-gate0.md + outputs/blocks/B01-gate0.yaml
- outputs/reports/07-emoat.md + outputs/blocks/B07-emoat.yaml

Boundary note: I audit rule application. I do not audit company quality, and I do
not audit whether a number exists in a source PDF. Source fidelity belongs to
Verifier A and its verdicts bind. Where I recompute below, I recompute from the
inputs the maker stated, not from the PDFs.

---

## PART 1 — GATE 0 (B01) COMPLIANCE

### 1.1 Arithmetic re-derivation from stated inputs

Every score was re-derived. The arithmetic is clean throughout. The failures below
are window-selection failures, not calculation failures.

Block A:
- ROCE FY25 = 16.93 / (416.06 − 111.83 = 304.23) = 5.565%. Matches 5.56%.
- ROCE FY26 = 31.18 / (464.45 − 137.59 = 326.86) = 9.539%. Matches 9.54%.
- Median of the two = 7.55%. Band <10% = 0. Correct.
- ROE FY23 32.94/229.42 = 14.36%; FY24 22.14/240.21 = 9.22%; FY25 4.89/252.125 =
  1.94%; FY26 16.90/267.075 = 6.33%. Median of four = (6.33+9.22)/2 = 7.775 →
  7.78%. Band <12% = 0. Correct.
- Block A stated 5. Recomputed as reported 5. See G-10 for the disputed 5 points.

Block B:
- B1: CFO sum −7.84+15.82+112.26−20.71 = 99.53. PAT sum 76.87. Ratio 1.2947.
  Band ≥1.00 = 5. Correct.
- B3: FCF sum 84.66−23.42 = 61.24. PAT FY25+FY26 = 21.79. Ratio 2.810.
  Band ≥0.60 = 5. Arithmetic correct, window wrong. See G-15.
- B4: FY25 rec/inv/pay days 92.24 / 28.24 / 16.28 → 104.20. FY26 96.08 / 37.38 /
  14.55 → 118.91. Change +14.71 days. Band increased 5-15 = 1. Correct.
- Block B stated 13. Recomputed as reported 13.

Block C:
- C1 (771.11/792.20)^(1/3) − 1 = −0.895%. Band <5% = 0. Correct.
- C2 (16.90/32.94)^(1/3) − 1 = −19.95%. Band negative = 0. Correct.
- C3 1 of 3 positive YoY = 33.3%. Band <50% = 0. Correct.
- C4 −19.94 − (−0.89) = −19.05pp. Band <−8pp = 0. Correct.
- CAGR edge rules honoured. Both endpoints are positive in both CAGRs, so N/M does
  not apply, and the report states this. No loss-to-profit swing occurred and the
  report records that in data_notes. C4 N/M fallback not triggered. Correct.
- Block C = 0. Correct.

Block D:
- D1 (132.57 − 3.63 = 128.94) / 46.97 = 2.745x. Band 2-3x = 1. Correct.
- D2 31.18 / 12.34 = 2.527x. Band 1.5-2.9 = 1. Correct.
- D3 132.57 / 280.90 = 0.472. Band 0.1-0.5 = 4. Correct.
- D4 301.53 / 137.59 = 2.191x. Band ≥2.0 = 5. Correct.
- Block D = 11. Correct.

Block E:
- E1 19,905,743 / 30,000,000 = 66.35%. Band ≥60% = 5. Correct.
- E2 3-year change not in provided data → 0. Correct under operating rule 5. The
  maker refused the AR's 1-year "Nil change" line as a substitute. That is the
  right call.
- E3 pledge not disclosed → 0, explicitly not assumed zero. Correct. Assuming 0%
  would have paid 5 points.
- E4 0.2085 / 280.90 = 0.074%. Band <5% = 5. Correct.
- Block E = 10. Correct.

Block F, all twelve moat tests:
- M1: EBITDA margin 7.97% FY23 → 6.09% FY26, a 1.88pp decline, and revenue CAGR
  −0.89%. The 5 and 3 bands need revenue CAGR ≥10%. The 1 band needs a 2-5pp
  decline "despite growth". Neither leg holds. 0 correct.
- M2, M5, M9: PEER DATA NEEDED, scored 0, no peer figure guessed. Correct per the
  Block F instruction. M9's gross-margin proxy was computed (17.7% FY26) and
  correctly not scored without a peer median.
- M3: FAT 771.11/109.99 = 7.01x, ROCE 9.54%. Lowest band needs ROCE >12%. 0 correct.
- M4: two decline years with a negative CAGR falls between the "2 decline years,
  CAGR positive = 1" band and the "3+ decline years = 0" band. The rubric has no
  explicit row for this case. Scoring 0 as closest fit is the conservative reading
  and the maker stated the reasoning. PASS with note, not a fail.
- M6, M7, M8, M10, M12: bands applied as written. 0 correct in each.
- M11: fewer than 6 years, so the two-window test cannot run. The rubric's own
  fallback ("score conservatively on the overall trend and state so") was used and
  stated. Correct.
- moats_confirmed = 0 (none scored ≥3), moat_class NONE (0 present = NONE). Correct.

Classification chain:
- core_score 5+13+0+11+10 = 39. Correct.
- Matrix: Core <40 → AVOID. Correct.
- Data confidence: 4 years falls in the "3-4 LIMITED, downgrade one tier" band.
  history_downgrade = true. Correct. AVOID is the floor, so the downgrade has no
  further effect, and the report says so.

Deal-breaker application, all nine evaluated:
| # | Rule | Trigger state | Verdict |
|---|---|---|---|
| 1 | Block A <8 | Block A = 5, triggered, capped max GOOD | Correct |
| 2 | Block B <8 | Block B = 13, not triggered | Correct |
| 3 | Median ROCE <10% | 7.55%, triggered, capped max AVERAGE | Correct |
| 4 | Cumul CFO/PAT <0.50 | 1.295, not triggered | Correct |
| 5 | Pledge >15% | not assessable, not triggered, not assumed | Correct |
| 6 | ND/EBITDA >3x AND IC <3x | 2.74x fails the first leg; IC 2.53x satisfies the second. AND logic requires both | Correct, not triggered |
| 7 | Revenue declined in majority of years | 2 of 3 YoY transitions, triggered, max AVERAGE | Correct |
| 8 | PAT negative in any of last 3 years | all positive, not triggered | Correct |
| 9 | History <3 years | 4 years, not triggered | Correct |

All three triggered deal-breakers are ceilings (max GOOD, max AVERAGE). The matrix
result AVOID already sits below both ceilings, so the caps are inert. The report
states this correctly and does not misread a ceiling as a floor. The "state WHICH
years drive any deal-breaker" instruction was honoured on all three.

FLAG-GATE0 emission condition (classification ≤ AVERAGE with depressors
identified) is met and the flag is present with named depressors. Correct.

### 1.2 Gate 0 rule-by-rule table

| ID | Rule (source: prompts/01-gate-0-pipeline.md) | Verdict | Recomputed / note |
|---|---|---|---|
| G-01 | Opening "Data available: X years" line | PASS | present, 4 years FY23-FY26 |
| G-02 | Rule 5, gaps marked N/A, no estimates | PASS | all six gaps marked, none filled |
| G-03 | Rule 4, source anchor on every number | PASS | anchors present throughout |
| G-04 | ROCE = EBIT ÷ (TA − CL) | PASS | re-derived, exact |
| G-05 | Use the source's own ROCE if provided; compute only when absent | **FAIL (MINOR)** | report computes and labels "computed" but never states whether screener-Data_Sheet.csv carried a ROCE row that was checked first |
| G-06 | A1 median ROCE band | PASS | 7.55% → 0 |
| G-07 | A2 minimum ROCE band | PASS | 5.56% → 0 |
| G-08 | ROE formula + earliest-year closing-NW disclosure | PASS | FY23 closing-only basis stated |
| G-09 | A3 median ROE band | PASS | 7.78% → 0 |
| G-10 | A4 ROCE trend, latest vs earliest | **FAIL (MAJOR)** | earliest (FY23) is N/A; a 1-year FY25→FY26 window scored 5. Recomputed under rule 5: **A4 = 0** |
| G-11 | Block A sum | PASS | 5 as stated (0 after G-10) |
| G-12 | FCF = CFO − (PPE + intangibles), acquisitions excluded | PASS | re-derived FY25 84.66, FY26 −23.42 |
| G-13 | B1 cumulative CFO/PAT band | PASS | 1.295 → 5 |
| G-14 | B2 FCF-positive-years proportion | **FAIL (MAJOR)** | denominator is 2 assessable years, not the 4-year history. Recomputed: 1 of 4 = 25% → **B2 = 0** |
| G-15 | B3 cumulative FCF/PAT window | **FAIL (MAJOR)** | 2-year numerator and denominator while B1 used 4 years. Recomputed under rule 5: **B3 = 0** |
| G-16 | WC-days formula and basis statement | PASS | revenue basis stated, no COGS line available |
| G-17 | B4 change band | PASS | +14.71 days → 1 |
| G-18 | Block B sum | PASS | 13 as stated (6 after G-14, G-15) |
| G-19 | CAGR formula | PASS | re-derived to 2dp |
| G-20 | CAGR edge rules (negative endpoint, loss-to-profit, C4 fallback) | PASS | all three correctly not triggered and stated |
| G-21 | C1 band | PASS | −0.89% → 0 |
| G-22 | C2 band | PASS | −19.94% → 0 |
| G-23 | C3 band | PASS | 33.3% → 0 |
| G-24 | C4 band | PASS | −19.05pp → 0 |
| G-25 | Block C sum | PASS | 0 |
| G-26 | D1 band | PASS | 2.74x → 1 |
| G-27 | D2 band | PASS | 2.53x → 1 |
| G-28 | D3 band | PASS | 0.47 → 4 |
| G-29 | D4 band | PASS | 2.19x → 5 |
| G-30 | Block D sum | PASS | 11 |
| G-31 | E1 band | PASS | 66.35% → 5 |
| G-32 | E2 unavailable → 0 | PASS | 1-year AR figure correctly refused |
| G-33 | E3 pledge never assumed zero | PASS | scored 0, not 5 |
| G-34 | E4 band | PASS | 0.07% → 5 |
| G-35 | Block E sum | PASS | 10 |
| G-36 | M1-M12 applied 0-5 each as specified | PASS | all twelve re-derived; M4 band gap handled conservatively |
| G-37 | PEER DATA NEEDED rule, score 0, never guess | PASS | M2, M5, M9 |
| G-38 | M11 <6-year fallback stated | PASS | stated explicitly |
| G-39 | Moat classification thresholds | PASS | 0 present → NONE |
| G-40 | core_score and grand_total arithmetic | PASS | 39 / 39 |
| G-41 | Classification matrix | PASS | Core <40 → AVOID |
| G-42 | Data-confidence tier, history_downgrade | PASS | 4 years → LIMITED, true |
| G-43 | Deal-breakers 1-9 evaluated, correct trigger set | PASS | 3 triggered, 6 correctly not |
| G-44 | "State WHICH years drive any deal-breaker" | PASS | years named on all three |
| G-45 | Deal-breaker caps vs matrix floor | PASS | caps correctly inert at AVOID |
| G-46 | FLAG-GATE0 emission condition | PASS | present with depressors |
| G-47 | Dashboard output elements (moat bars, strongest/weakest, decision line) | PASS | all present |
| G-48 | YAML fields complete and consistent with report | PASS | every field cross-checked, no drift |
| G-49 | analyst_note ≤200 words | PASS | ~135 words |
| G-50 | data_notes carries proxy bases and PEER DATA NEEDED items | PASS | 8 notes, all required items present |

**Gate 0: 50 rules checked, 46 PASS, 4 FAIL (3 MAJOR, 1 MINOR). Adherence 92%.**

### 1.3 The window-selection failure, stated once

G-10, G-14 and G-15 share one root cause. Where a metric was computable in only
two of the four years, the maker scored the metric on the 2-year subset instead of
scoring the missing years against the metric. Operating rule 5 is explicit: "If a
data point is not available, mark it N/A ... and score it 0." Rule 6 sets the
history floor at three years. A 2-year subset sits below that floor.

The maker flagged each instance in the report text, and on B3 wrote that the ratio
"likely overstates true 4-year cash conversion". Self-disclosure mitigates. It does
not cure, because the flagged score still propagates into core_score.

Recomputed Gate 0 under the strict rule-5 reading:
- Block A = 0 (A4 5 → 0)
- Block B = 6 (B2 2 → 0, B3 5 → 0)
- Core = 0 + 6 + 0 + 11 + 10 = **27**, versus 39 as reported. A 12-point gap.
- Classification: Core <40 → **AVOID**. Unchanged.
- Additional consequence: Block B = 6 would newly trigger deal-breaker 2 (Block B
  <8, max GOOD), which is still inert at AVOID.

Because the classification does not move, these are MAJOR, not CRITICAL. They
matter downstream for one reason: core_score 39 versus 27 is a materially
different input if any later stage reads the number rather than the label.

---

## PART 2 — EMERGING MOAT (B07) COMPLIANCE

### 2.1 Twenty-category scan completeness

All 21 categories are addressed. Count verified against the rubric: Family A 4
(A1-A4), B 3 (B1-B3), C 2, D 2, E 2, F 2, G 2, H 3 (H1-H3) = 20, plus R1 = 21.
Every row carries either an evidence table entry or an explicit NO EVIDENCE FOUND.
No category is silently skipped. No category is force-fit.

Section 3 summary states 6 rows with evidence and 15 NO EVIDENCE FOUND. 6 + 15 =
21. Internally consistent.

Four NO EVIDENCE rows (C2, E2, G1, G2) are marked as running in the opposite
direction from the category. That is above the rubric's requirement and is good
practice, not a deviation.

### 2.2 Completionist guard

The guard triggers at 12 or more active categories. Six active is inside the
stated 3-6 base rate. The required recount line is present in the rubric's exact
form: "📄 recount performed: 6 documented items across 6 categories (A3, B2, F2,
H2, H3, R1)."

The guard was applied in the right direction on C1. The MD&A's "customer service
excellence ... widely appreciated by leading clients" line is a 🎙️ assertion with
no named customer, no cross-sell count and no wallet-share figure. The maker
excluded it rather than crediting it. That is the guard working as designed.

### 2.3 Evidence typing and multipliers

Every scored row is 📄 and carries the 1.0x multiplier. Re-derivation of each:

| Cat | Stated L×I | Raw per matrix | Multiplier | Adjusted | Verdict |
|---|---|---|---|---|---|
| A3 | LM | 1 | 📄 1.0x | 1.0 | correct |
| B2 | LL | 1 | 📄 1.0x | 1.0 | correct |
| F2 | MM | 2 | 📄 1.0x | 2.0 | correct |
| H2 | HH | 4 | 📄 1.0x | 4.0 | see E-17 |
| H3 | LL | 1 | 📄 1.0x | 1.0 | correct |
| R1 | LM | 1 | 📄 1.0x | 1.0 | correct |
| Total | | | | **10.0** | matches stated 10.0 |

Matrix values check out against the rubric (HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1,
LL=1, no evidence=0). The multiplier ladder is applied without error. No 🎙️-only
or 🔍-only category is scored anywhere, which is the specific abuse rule 3 of my
rubric names, and it is absent here.

Classification: 10.0 < 12 → NO MEANINGFUL EMERGING MOAT. Correct threshold read.
Block field em_classification "NONE" matches the block's own enum.

Underlying evidence tier per scored row, checked one by one:
- A3: AR Annexure V, completed equipment upgrades. Actions taken, not promised. 📄 holds.
- B2: certifications held with validity dates and accreditation scope. 📄 holds.
- F2: Note 47 CWIP ageing at zero, no cost or schedule overrun. 📄 holds.
- H3: equity investment tied to a PPA, accounting policy note. Thin but disclosed. 📄 holds.
- R1: incentive amounts received and adjusted, ₹416.28 lakh FY26. 📄 holds.
- H2: the board approval, exchange ratio and filings are 📄. The impact rating is not. See below.

### 2.4 The H2 finding

H2 contributes 4.0 of the 10.0 total, 40% of the score. Two problems.

First, category fit. H2's what-to-look-for list is "JV with global leader,
exclusivity, inbound tech licensing, co-development, strategic equity investor".
An amalgamation in which BCL is the Transferor Company and "shall stand dissolved"
is not a partnership. The report itself says so twice: 6D calls it "a corporate
structure event that dissolves BCL, not a competitive advantage building
catalyst", and 6E calls it "not a moat at all for the BIRLACABLE ticker". The
scorecard credits 4 points to an item the narrative argues is not a moat.

Second, the impact leg. High × High rests on the Scheme's stated rationale:
balance sheet strength, R&D pooling, cross-selling, procurement synergies. Section
6B classifies exactly this material as "🎙️/aspirational language in a Scheme
document, common to most amalgamation filings". So a 📄 1.0x multiplier is applied
to a raw score whose impact half is sourced from 🎙️ material. The documented fact
is that a board approved a scheme. The High impact is a claim.

Recomputed both ways:
- Impact downgraded to Medium (HM = 3): em_score = **9.0**.
- H2 treated as out of category and scored 0: em_score = **6.0**.
- Reported: 10.0.
- Classification under all three: <12 → **NO MEANINGFUL EMERGING MOAT**. Unchanged.

MAJOR, not CRITICAL. The classification survives, and downstream consumers get the
right label. But active_categories carries H2 as the single Strong row, so a stage
reading that field inherits the overstatement.

### 2.5 Catalyst evidence anchoring

All three catalysts_12m entries carry an anchor and a window. Anchors are AR page
references (p.26-27, p.63-64, p.20-21). None is bare.

Catalyst 1 (NCLT sanction) and catalyst 2 (CARE rating watch resolution) are
company-specific documented events. Both correctly typed.

Catalyst 3 is typed "documented (industry data cited in AR)". The underlying
signal is third-party market intelligence about global Q1 FY27 demand, quoted
inside the AR. The same report rejects exactly this reasoning twice: section 1A
excludes HCF/MCF industry commentary because "no BCL capex, trial, or launch is
tied to any of these terms", and E2 excludes China+1 commentary as "industry
narrative, not a company specific capex or order win disclosure". Typing the same
class of material as documented in the catalyst list is inconsistent with the
report's own standard. The parenthetical disclosure limits the damage. MINOR, with
a carry-forward instruction: stage 11 must not treat catalyst 3 as a
company-specific 📄 catalyst when computing Pillar 3 catalyst proximity.

### 2.6 Optionality register

Four required columns present, five rows. Registered items are correctly excluded
from the scorecard as a set.

One overlap. Three of the five rows (post-merger balance sheet strength, pooled
R&D, cross-selling) are the same Scheme synergies that supply H2's High impact
leg. The rubric says registered options are "watched, never scored". These are
registered and, through H2's impact rating, partly scored. MINOR, and it is the
same root cause as E-17.

### 2.7 No-conflation rule

PASS, and handled well. The report opens with an explicit taxonomy line: "this is
the Emerging Competitive Advantages scan (20 categories + R1), NOT FTTCP. FTTCP
runs later, inside the valuation stage." No FTTCP terminology, no FTTCP ROCE
verdict, and no FTTCP scoring appears anywhere in the six sections or the block.
The two analyses are kept separate by name and by content.

### 2.8 Section 2C arithmetic

Re-derived. Average net block (12,821.42 + 10,989.12)/2 = 11,905.27 lakh = ₹119.05cr.
FAT = 771.11 / 119.05 = 6.477x, matches 6.48x. Implied incremental revenue =
0.0395 × 6.48 = ₹0.256cr, matches ₹0.26cr. As % of revenue = 0.256/771.11 =
0.033%, matches 0.03%. Block field capex_embedded_growth_pct 0.03 is consistent.
The arithmetic is shown, as the rubric demands.

Using outstanding capital commitment as "capex under execution" is defensible
here, because Note 47 shows zero CWIP carried forward, so nothing is mid-flight.

### 2.9 Emerging Moat rule-by-rule table

| ID | Rule (source: prompts/07-emerging-moat-pipeline.md) | Verdict | Recomputed / note |
|---|---|---|---|
| E-01 | All six sections executed in one response | PASS | 1-6 all present |
| E-02 | Section 1A/1B/1C complete | PASS | 1C table with NOT FOUND fills |
| E-03 | 2A capex programme table | PASS | both years, all columns |
| E-04 | 2B utilisation trajectory | PASS | NOT FOUND stated, not estimated |
| E-05 | 2C arithmetic shown | PASS | re-derived 6.48x / ₹0.26cr / 0.03% |
| E-06 | 2D new geography or market entries | PASS | |
| E-07 | All 21 categories addressed or NO EVIDENCE FOUND | PASS | 6 + 15 = 21 verified |
| E-08 | Evidence taxonomy applied to every item | PASS | |
| E-09 | Source anchor on every evidence item | PASS | AR page refs throughout |
| E-10 | Rule 5, never force-fit | PASS | C1 excluded, not credited |
| E-11 | Completionist guard, base rate check and recount line | PASS | exact required wording |
| E-12 | Section 3 summary table columns incl. time to materialise | **FAIL (MINOR)** | column absent from all family tables; appears only for H2 in the block |
| E-13 | 4A regulatory approvals in pipeline | PASS | |
| E-14 | 4B policy tailwinds with amounts, duration, enrolment | PASS | duration NOT FOUND, correctly marked |
| E-15 | 4C regulatory moat assessment | PASS | active vs emerging stated |
| E-16 | Section 5 scores all 21 rows | PASS | 21 rows present |
| E-17 | Likelihood × impact matrix correct per row | **FAIL (MAJOR)** | H2 HH impact leg rests on 🎙️ synergy language the report itself labels aspirational; category fit is a stretch. Recomputed **9.0** (HM) or **6.0** (out of category) vs 10.0 |
| E-18 | Evidence multipliers 📄1.0 / 🎙️0.7 / 🔍0.5 | PASS | all scored rows 📄 1.0x |
| E-19 | Adjusted total arithmetic | PASS | 10.0 re-derived |
| E-20 | Classification thresholds | PASS | <12 → NONE |
| E-21 | No 🎙️-only category scored as 📄 | PASS | none found |
| E-22 | Register rows are unscored / 🎙️ / 🔍 only, never scored | **FAIL (MINOR)** | 3 merger-synergy rows overlap H2's credited impact leg |
| E-23 | 6A four timeline windows | PASS | 12m / 12-24 / 24-36 / 3-5yr |
| E-24 | 6B risks with early warning signs | PASS | 4 risks, warning sign each |
| E-25 | 6C uses the injected Gate 0 block | PASS | core 39, moat 0, AVOID, NONE all match B01 |
| E-26 | 6D combined classification from the stated matrix | PASS | AVOID, valid enum member, reasoning given |
| E-27 | 6E final card elements | PASS | map, catalysts, biggest risk |
| E-28 | No conflation with FTTCP | PASS | explicit taxonomy line, no FTTCP content |
| E-29 | catalysts_12m each anchored | PASS | 3 of 3 anchored |
| E-30 | Catalyst evidence typing consistent with the taxonomy | **FAIL (MINOR)** | catalyst 3 typed documented on third-party industry data, contradicting the report's own 1A and E2 exclusions |
| E-31 | evidence_mix reports item counts | **FAIL (MINOR)** | reports scored-category counts (6/0/0); 🎙️ and 🔍 items do appear in 1A, 1C, C1 and 6B |
| E-32 | active_categories limited to Strong/Moderate rows | PASS | H2 only, consistent with the summary |
| E-33 | capex_embedded_growth_pct matches 2C | PASS | 0.03 |
| E-34 | em_score / em_classification block-report consistency | PASS | 10 / NONE |
| E-35 | F2 cross-references the concall promise-delivery record | PASS | NO-CONCALL mode; AR substitution disclosed with its single-data-point limit |
| E-36 | input_gaps and flags completeness | PASS | 6 gaps, 4 flags, all material |
| E-37 | analyst_note ≤200 words | PASS | ~150 words |

**Emerging Moat: 37 rules checked, 32 PASS, 5 FAIL (1 MAJOR, 4 MINOR). Adherence 86%.**

---

## PART 3 — CONSOLIDATED FINDINGS

| # | Severity | Section | Rule | Finding | Recomputed |
|---|---|---|---|---|---|
| 1 | MAJOR | Gate 0 | G-10 (A4) | ROCE trend scored on a 1-year FY25→FY26 window because FY23/FY24 ROCE is N/A. Rule 5 scores an unavailable data point 0; rule 6 sets a 3-year floor | A4 5 → 0 |
| 2 | MAJOR | Gate 0 | G-14 (B2) | FCF-positive-years proportion uses 2 assessable years as the denominator, not the 4-year history | 50% → 25%, B2 2 → 0 |
| 3 | MAJOR | Gate 0 | G-15 (B3) | Cumulative FCF/PAT computed on FY25-FY26 while B1 used all four years. The two weak/negative CFO years are excluded from the numerator's window | B3 5 → 0; core 39 → 27, classification AVOID unchanged |
| 4 | MAJOR | E-Moat | E-17 (H2) | Amalgamation into the parent scored HH=4 under "strategic partnerships". Category fit is a stretch, and the High impact leg rests on Scheme synergy language the report itself calls 🎙️/aspirational in 6B | em 10.0 → 9.0 (HM) or 6.0 (out of category); classification NONE unchanged |
| 5 | MINOR | Gate 0 | G-05 | Report does not state whether the source's own ROCE figure was checked before computing, as the formula rule requires | none |
| 6 | MINOR | E-Moat | E-12 | Section 3 summary tables omit the required "time to materialise" column | none |
| 7 | MINOR | E-Moat | E-22 | Three optionality-register rows are the same synergies that supply H2's scored impact leg. Registered options are meant to be watched, never scored | none |
| 8 | MINOR | E-Moat | E-30 | Catalyst 3 typed "documented" on third-party industry data, inconsistent with the report's own exclusions in 1A and E2. Stage 11 must not read it as a company-specific 📄 catalyst | none |
| 9 | MINOR | E-Moat | E-31 | evidence_mix reports scored-category counts, not item counts. 🎙️ and 🔍 items exist in the narrative but are recorded as 0 | none |

Totals: 0 CRITICAL, 4 MAJOR, 5 MINOR. 87 rules checked, 78 PASS. Acceptance 90%.

No CRITICAL. No misapplication flips a classification. Gate 0 stays AVOID under
the strict recomputation (core 27, still below the 40 floor). Emerging Moat stays
NO MEANINGFUL EMERGING MOAT under both H2 recomputations (9.0 or 6.0, both below
12). Acceptance sits well above the 60% REWORK trigger. No REWORK from this
verifier.

## PART 4 — WHAT THE MAKERS GOT RIGHT

Worth recording, because these are the places where a weaker run loses points:
- Pledge not assumed zero at E3. Assuming 0% pays 5 points and is the common error.
- Deal-breaker 6's AND logic read correctly. ND/EBITDA 2.74x fails the first leg
  even though IC 2.53x satisfies the second.
- Deal-breaker ceilings correctly treated as inert at AVOID, not misread as floors.
- C1's 🎙️ MD&A assertion excluded rather than credited. The completionist guard
  worked in the direction it is designed to work.
- Every peer-dependent moat test scored 0 and marked PEER DATA NEEDED. No peer
  figure invented.
- The FTTCP no-conflation rule handled explicitly at the top of the B07 report.
- NO-CONCALL mode substitution at F2 disclosed with its limitation named, not
  passed off as a multi-year record.

## PART 5 — CARRY-FORWARD FOR PHASE 3

Not findings. Inputs the valuation audit will need:
1. core_score 39 as published, 27 under strict rule-5 recomputation. Any stage
   reading the number rather than the AVOID label should know the spread.
2. em_score 10 as published, 6.0 to 9.0 under the H2 recomputation. Pillar 3 reads
   this input.
3. catalysts_12m item 3 is industry data, not a company-specific documented
   catalyst. It must carry the MODERATE cap or a candidate cite in stage 11.
4. Downstream signal candidates (my rubric rule 6): B09 was not among my phase-1
   inputs, so the downstream_candidates check is NOT RUN and defers to phase 3.
5. The pending BCL-into-VTL amalgamation is flagged in both B01 and B07. It is a
   framework-relevant fact for stage 11's horizon, not a framework finding here.

---

```yaml
stage: B12c
company: "BIRLACABLE"
run_date: "2026-08-20"
model: claude-opus-4-8
status: complete
scope: phase-1
gate0:
  rules_checked: 50
  rules_passed: 46
  adherence_pct: 92
  fails:
    - {id: "G-10", severity: "MAJOR", rule: "A4 ROCE trend, latest vs earliest", detail: "scored 5 on a 1-year FY25-FY26 window; FY23 earliest ROCE is N/A, rule 5 scores it 0 and rule 6 sets a 3-year floor", recomputed: "A4 = 0"}
    - {id: "G-14", severity: "MAJOR", rule: "B2 FCF-positive years as proportion", detail: "denominator is the 2 assessable years, not the 4-year history", recomputed: "1 of 4 = 25% -> B2 = 0"}
    - {id: "G-15", severity: "MAJOR", rule: "B3 cumulative FCF / cumulative PAT", detail: "computed on FY25-FY26 subset while B1 used the full 4 years; excludes the two weak CFO years", recomputed: "B3 = 0; core_score 39 -> 27, classification AVOID unchanged"}
    - {id: "G-05", severity: "MINOR", rule: "use the source's own ROCE if provided", detail: "report computes ROCE and labels it computed, but never states whether the screener source carried a ROCE row that was checked first", recomputed: ""}
emoat:
  rules_checked: 37
  rules_passed: 32
  adherence_pct: 86
  fails:
    - {id: "E-17", severity: "MAJOR", rule: "likelihood x impact matrix correct per row", detail: "H2 scored HH=4 for an amalgamation in which BCL is dissolved; category fit is a stretch and the High impact leg rests on Scheme synergy language the report itself labels 🎙️/aspirational in 6B, while a 📄 1.0x multiplier is applied", recomputed: "em_score 10.0 -> 9.0 (HM) or 6.0 (out of category); classification NONE unchanged in both"}
    - {id: "E-12", severity: "MINOR", rule: "Section 3 summary table columns", detail: "required 'time to materialise' column absent from all family tables; present only for H2 in the block", recomputed: ""}
    - {id: "E-22", severity: "MINOR", rule: "registered options are watched, never scored", detail: "three optionality-register rows are the same merger synergies that supply H2's scored impact leg", recomputed: ""}
    - {id: "E-30", severity: "MINOR", rule: "catalyst evidence typing", detail: "catalyst 3 typed documented on third-party industry data, inconsistent with the report's own exclusions at 1A and E2; stage 11 must not read it as a company-specific documented catalyst", recomputed: ""}
    - {id: "E-31", severity: "MINOR", rule: "evidence_mix reports item counts", detail: "reports scored-category counts (6/0/0); 🎙️ and 🔍 items appear in 1A, 1C, C1 and 6B but are recorded as zero", recomputed: ""}
valuation: {status: pending-phase-3}
recomputed_destination_pe: ""
recomputed_decision: ""
recomputed_gate0_core_score: "39 as published; 27 under strict rule-5 recomputation; classification AVOID unchanged"
recomputed_em_score: "10.0 as published; 9.0 or 6.0 under the H2 recomputation; classification NONE unchanged"
no_conflation_check: "PASS - B07 states explicitly it is the Emerging Competitive Advantages scan and not FTTCP; no FTTCP content appears"
downstream_candidates_check: "NOT RUN - B09 is not a phase-1 input; deferred to phase 3"
findings:
  - {severity: "MAJOR", location: "B01 Block A, A4", issue: "1-year ROCE trend window scored 5 where the earliest endpoint is N/A", recomputed: "A4 = 0"}
  - {severity: "MAJOR", location: "B01 Block B, B2", issue: "FCF-positive proportion on a 2-year denominator", recomputed: "B2 = 0"}
  - {severity: "MAJOR", location: "B01 Block B, B3", issue: "cumulative FCF/PAT window inconsistent with B1", recomputed: "B3 = 0, core 27"}
  - {severity: "MAJOR", location: "B07 Section 5, H2", issue: "dissolution event scored HH=4 under strategic partnerships; impact leg rests on 🎙️ synergy language", recomputed: "em 6.0 to 9.0"}
  - {severity: "MINOR", location: "B01 formula note", issue: "source-ROCE precedence rule not documented", recomputed: ""}
  - {severity: "MINOR", location: "B07 Section 3 tables", issue: "time-to-materialise column omitted", recomputed: ""}
  - {severity: "MINOR", location: "B07 optionality register", issue: "three rows overlap H2's scored impact leg", recomputed: ""}
  - {severity: "MINOR", location: "B07 catalysts_12m item 3", issue: "industry data typed as documented", recomputed: ""}
  - {severity: "MINOR", location: "B07 evidence_mix", issue: "category counts reported as item counts", recomputed: ""}
critical_count: 0
major_count: 4
minor_count: 5
rules_checked_total: 87
rules_passed_total: 78
acceptance_rate: 90
acceptance_note: "covers the two audited sections only (Gate 0 50 rules, Emerging Moat 37 rules); the valuation audit is deferred to phase 3 and is excluded from this rate"
rework_trigger: false
```
