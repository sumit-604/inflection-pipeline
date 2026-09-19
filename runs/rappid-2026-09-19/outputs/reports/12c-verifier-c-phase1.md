# STAGE 12 VERIFIER C: FRAMEWORK ADHERENCE, PHASE 1 SCOPE
RAPPID (Rappid Valves (India) Ltd) | Run date 2026-09-19 | Model: claude-opus-5

Scope: I audited Gate 0 (B01, round-2 corrected report) and the Emerging Moat scan (B07).
The valuation audit (B10, B11), the Expectation Ledger (rules 13-14), the Business
Understanding Narrative (rule 9), the dossier check (rule 10) and the method plurality
check (rule 7) did NOT run. They are pending phase 3.

Rule sources: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md.
Artifacts: outputs/reports/01-gate0.md, outputs/blocks/B01-gate0.yaml,
outputs/reports/07-emoat.md, outputs/blocks/B07-emoat.yaml.
Re-derivation sources: inputs/screening/screener-Data_Sheet.csv,
inputs/annual-report/Annual_Report_2026.txt (INR Lakhs),
inputs/prospectus/Rappid_Valves_RHP_Sep2024.txt (INR Lakhs).

I audit how the rules were applied. Verifier A owns whether each number exists at
its anchor. Where I quote a source number, I quote it only to test a rule.

---

## PART 1: GATE 0 (B01) COMPLIANCE

### 1.1 Re-derivation of block scores

I re-derived every metric from the screener series. The B01 arithmetic reproduces
exactly: cumulative CFO -25.42 Cr, cumulative PAT 17.40 Cr, cumulative FCF -34.37 Cr,
WC days 150.3 (FY22) to 334.2 (FY26), revenue CAGR 44.7%, PAT CAGR 117.4%, ROE
series -116.0 / 32.1 / 78.6 / 22.9 / 13.4 (median 22.9%), computed ROCE FY26
9.67 / (75.32 - 23.52) = 18.7% (screener-Data_Sheet.csv; AR p.69 Note 36 base value B
current liabilities 2,351.8 Lakh).

One rule application fails: the ROCE series (finding F1 below).

### 1.2 Rule-by-rule table

| # | Rule (prompts/01) | B01 applied | Verdict | Recomputed value |
|---|---|---|---|---|
| G01 | Opening line "Data available: X years" (pipeline rule 6) | "5 years (FY22 to FY26)" | PASS | |
| G02 | Source anchor after every number (rule 4) | Anchors present on spot-checked lines | PASS | |
| G03 | ROCE: use source's own ROCE where provided, else compute, one basis per series | Mixed: FY22-24 computed EBIT/(TA-CL), FY25-26 AR Note 36 disclosed; RHP disclosed ROCE rejected for "different denominator" | **FAIL (MAJOR, F1)** | Uniform source reading: 18.38 / 15.85 / 29.88 / 17 / 14. A1 median 17% = 3 (B01: 5). A2 min 14% = 3 (same). A4 14 vs 18.38 = -4.38pp = 1 (B01: 0) |
| G04 | Block A total | 13 | **FAIL (MAJOR, F1)** | 12 (uniform source) or 15 (uniform computed). Never 13 on one basis |
| G05 | A3 ROE, PAT / average NW, closing NW for earliest year | FY22 on closing NW, included, median 22.9% = 5 | PASS | |
| G06 | B1 cumulative CFO / PAT | -1.46 = 0 | PASS | |
| G07 | B2 FCF = CFO - capex, positive-year share | 1 of 5 = 0 | PASS | |
| G08 | B3 cumulative FCF / PAT | -1.98 = 0 | PASS | |
| G09 | B4 WC days, revenue basis stated when COGS absent | +183.9 days = 0; basis stated | PASS | |
| G10 | C1-C4 bands | 5/5/5/5 | PASS | |
| G11 | CAGR edge rules (negative endpoint, loss-to-profit note, C4) | No negative endpoint; "no loss-to-profit swing" noted in data_notes | PASS | |
| G12 | D1 Net debt / EBITDA | 1.49x = 3 | PASS | Netting investments 4.76 Cr gives 1.03x, same band |
| G13 | D2 interest coverage = EBIT / Interest | Used AR p.27 disclosed 7.52x; formula figure 7.27x shown as cross-check | **FAIL (MINOR, F2)** | 7.27x = 4, score unchanged |
| G14 | D3, D4 | 0.35x = 4; 2.55x = 5 | PASS | |
| G15 | E1 promoter holding latest | 51.58% = 4 | PASS | |
| G16 | E2 promoter holding change over 3 years | 69.46% (pre-issue, Sep-2024) to 51.58% (Mar-2026) = 0; window called "approximating 3 years" | **FAIL (MINOR, F3)** | Window is about 18 months. Score 0 stands |
| G17 | E3, E4 | 0% = 5; 0.28% = 5 | PASS | |
| G18 | M1 pricing power, use all available history | FY23-FY26 window from AR snapshot, +6.3pp = 5 | **FAIL (MINOR, F4)** | FY22-FY26 on screener: 16.0% to 19.4% = +3.4pp, CAGR 44.7% = 5, unchanged |
| G19 | M2, M5, M9 peer tests without peer data = 0, PEER DATA NEEDED | Applied | PASS | |
| G20 | M3 capital efficiency | FAT 5.18x, ROCE 14% = 1 | PASS | Holds under the uniform source reading. Under the computed reading it is 3 (see F1) |
| G21 | M4 customer stickiness | 0 decline years satisfies "max 1 decline year" = 3 | PASS | |
| G22 | M6, M7, M8 | 0 / 0 / 1 | PASS | |
| G23 | M10 switching costs | 0, reasoning corrected in round 2 | PASS | |
| G24 | M11 with fewer than 6 years, conservative | 3 on overall trend, stated | PASS | |
| G25 | M12 | 0 | PASS | |
| G26 | Moat count (score >= 3) and class | 3 = MODERATE | PASS | |
| G27 | Data confidence: 5-6 yrs lower, flag carried, no downgrade | Flag in data_notes, history_downgrade false | PASS | |
| G28 | Classification matrix, raw | Core 63 + MODERATE = GOOD | PASS | Core 62 + MODERATE = GOOD, same cell |
| G29 | Deal-breakers applied, driving years stated, FLAG-GATE0 emitted | #2 and #4 triggered; FY23-FY26 named; final AVERAGE | PASS | |

Gate 0: 29 rules checked, 5 fail, 24 pass.

### 1.3 Gate 0 findings

**F1 (MAJOR). ROCE series mixes two formula bases, and the stated reason for the mix
is contradicted by the source.**
- Rule (prompts/01, FORMULA DEFINITIONS): "ROCE = EBIT ÷ (Total Assets − Current
  Liabilities), per year. If the data source provides its own ROCE (screener.in does),
  use the source's figure and anchor it; compute only when absent, and state 'computed'."
- B01 took the AR Note 36 disclosed ROCE for FY25-FY26 (17%, 14%). It kept its own
  computed figures for FY22-FY24 (85.4%, 39.5%, 47.7%). It rejected the RHP's
  disclosed ROCE for FY22-FY24 because RHP uses "a different denominator (Net worth +
  Total Debt)". It also states that "The AR's formula denominator ('average of K') is
  not shown in the extracted text".
- Source truth: the AR defines K on the same page. Base value K "Capital Employed = H + I
  + Deferred Tax Liabilities" (Equity + Debt + DTL), 6,955.7 / 5,366.2 Lakh (AR p.69,
  Note 36 base-value table). The RHP KPI note defines ROCE as "Profit before tax +
  Finance Costs – Other Income (EBIT) divided by (Tangible Net Worth + Total Debt +
  Deferred Tax Liabilities)" (RHP p.151, KPI note (6)). The AR and RHP denominators are
  the same family. The ground B01 gives for rejecting the RHP figures applies equally to
  the AR figures it accepted.
- Effect: A1, A2 and A4 compare figures from two formulas. A4 is the worst case. It sets
  a computed FY22 figure (85.4%, capital employed Rs 2.04 Cr) against a disclosed FY26
  figure (14%) on a different denominator.
- Two readings, one separating observation:
  - Reading 1, uniform source-disclosed (the rule text as written; RHP and AR are both
    provided data sources): FY22 18.38%, FY23 15.85%, FY24 29.88% (RHP p.151), FY25 17%,
    FY26 14% (AR p.69). A1 = 3, A2 = 3, A3 = 5, A4 = 1. **Block A = 12. Core 62. Moat 13
    (M3 = 1). Grand total 75.** Raw GOOD.
  - Reading 2, uniform computed (the fixed formula for all five years): 85.4 / 39.5 /
    47.7 / 20.2 / 18.7. A1 = 5, A2 = 5, A3 = 5, A4 = 0. Block A = 15. M3 = 3, so 4 moats,
    STRONG. Core 65, moat 15, grand total 80. Raw GOOD+.
  - Separating observation: does "the data source" in the ROCE clause mean only the
    screener dataset, or any provided filing that discloses ROCE? This needs an operator
    ruling. The rule text favours Reading 1.
- The B01 mixed series (Block A 13, core 63) matches neither reading.
- Decision impact: none. Deal-breaker 4 (cumulative CFO/PAT -1.46) caps both readings at
  AVERAGE. The moat class (MODERATE vs STRONG) depends on the reading, and B07 section 6C
  reads that class.
- Fix: stage 1 applies one basis across all five years, states which one, and corrects the
  "denominator not shown" sentence.

**F2 (MINOR). D2 uses a disclosed ratio where the rule fixes a formula.** The rule says
"Interest Coverage EBIT ÷ Interest (latest)". Only ROCE has a source-precedence clause.
Formula value: 9.67 / 1.33 = 7.27x (screener-Data_Sheet.csv). Band 5-9.9x, score 4
either way. The report shows 7.27x as a cross-check, so no information is lost.

**F3 (MINOR). E2 window mislabelled.** The rule tests "change over 3 years". B01 measures
from the pre-issue holding 69.46% (RHP p.95, dated to the Sep-2024 RHP) to 51.58%
(AR p.60, Mar-2026). That window is about 18 months, not "approximating 3 years". The
Mar-2023 holding (the 3-year start) is NOT FOUND in the report. The score of 0 is robust:
any Mar-2023 holding at or above 52.58% gives a fall above 3pp. The label should say
"18-month window, 3-year start point NOT FOUND".

**F4 (MINOR). M1 uses a shorter window than the data allows.** Pipeline rule 6 says "use
whatever history is available". M1 uses the AR FY23-FY26 snapshot, while C1 uses
FY22-FY26. On the screener series, EBITDA (PBT + interest + depreciation - other income)
runs from 1.94 Cr (16.0%) in FY22 to 10.31 Cr (19.4%) in FY26. That is +3.4pp. M1 = 5
either way.

### 1.4 Gate 0 items that pass on re-check (round-2 corrections)
- G22 fix (E2 = 0 with no dilution exception): correct application of rule 2.
- G6 fix (FY22 ROE included on closing NW): correct.
- G30 fix (M10 reasoning): the corrected reasoning is literal and right.
- G34 fix (confidence flag in YAML data_notes): present.
- G37 fix (matched CFO/PAT windows in FLAG-GATE0): present and correct.

---

## PART 2: EMERGING MOAT (B07) COMPLIANCE

### 2.1 Scorecard re-derivation

| Row | Raw (L×I) | Multiplier used | Stated evidence tier in Section 3 | Adjusted | Verdict |
|---|---|---|---|---|---|
| A1 | HH 4 | 1.0 | D | 4.0 | PASS (observation O1) |
| A3 | ML 1 | 0.5 | D (AR p.15; call p.1), table "D/I" | 0.5 | FAIL, tier vs multiplier (F6) |
| B2 | HH 4 | 1.0 | D | 4.0 | PASS |
| C1 | HM 3 | 0.7 | M dominant | 2.1 | PASS |
| C2 | LM 1 | 0.7 | M | 0.7 | PASS |
| E2 | MM 2 | 1.0 | D | 2.0 | PASS |
| F2 | LL 1 | "mixed, 0.5" | D/D | 0.5 | FAIL, 0.5 is the 🔍 multiplier; no "mixed" multiplier exists (F6) |
| H1 | MM 2 | 0.7 | M | 1.4 | FAIL, raw inconsistent with "Weak" label (F7) |
| H2 | LM 1 | 1.0 | D | 1.0 | PASS |
| R1 | HM 3 | 1.0 | D | 3.0 | PASS |
| 13 others | 0 | n/a | NO EVIDENCE FOUND | 0.0 | PASS |

Arithmetic: 4 + 0.5 + 4 + 2.1 + 0.7 + 2 + 0.5 + 1.4 + 1 + 3 = 19.2. Correct.
Recomputed range after F6, F7 and O1: 18.2 to 19.7. Band 12-24 in every case.
**MODEST MOAT DEVELOPMENT stands.**

### 2.2 Rule-by-rule table

| # | Rule (prompts/07 and verifier rules 3, 8) | B07 applied | Verdict |
|---|---|---|---|
| E01 | All six sections, one response | Present | PASS |
| E02 | Evidence taxonomy: concall or presentation statements are 🎙️ | "90+ clients" (call p.1) and repeat rate 60% (Inv. Pres. p.7) labelled [D] | **FAIL (MINOR, F5)** |
| E03 | Source anchors on every evidence item | Present. Observation O2: two items lean on "company memory" | PASS |
| E04 | All 23 rows addressed or NO EVIDENCE FOUND | 22 categories + R1, all addressed | PASS |
| E05 | Section 3 summary table, all rows, Strong/Moderate count stated | 23 rows, count 5 | PASS |
| E06 | Raw scores are legal L×I values | All legal | PASS |
| E07 | Multiplier matches stated evidence tier | A3, F2 mismatched | **FAIL (MINOR, F6)** |
| E08 | Scores consistent across rows with the same strength label | H1 "Weak" at MM = 2; every other Weak row at 1 | **FAIL (MINOR, F7)** |
| E09 | 🎙️-only category not scored as 📄 (rule 3) | C1, C2, H1 at 0.7 | PASS |
| E10 | Adjusted total and classification band | 19.2, MODEST | PASS |
| E11 | I1/I2 contribution stated separately | "0.0 of 19.2" | PASS |
| E12 | Completionist recount line, exact count of 📄 items | "approximately 9 ... across 4 categories" | **FAIL (MINOR, F8)** |
| E13 | Guard threshold: fewer than 12 active categories | 10 non-zero rows, 5 Strong/Moderate | PASS |
| E14 | Category 21 (I1) present, 0 unless both legs evidenced, (b) leg 📄 (rule 8) | Present, 0, leg (a) absent | PASS |
| E15 | Category 22 (I2) present, 0 unless sacrifice named and specific (rule 8) | Present, 0, "nothing must be destroyed" | PASS |
| E16 | I2 test run "for each moat claimed anywhere in this scan" | Run for B2 only | **FAIL (MINOR, F9)** |
| E17 | F2 cross-references the injected promise-delivery record | B05 record cited (1/1/3, grade C) | PASS |
| E18 | Section 2C arithmetic shown | 1.25 × 5.18 = 6.47 Cr = 12.2%, capex tagged [M] | PASS |
| E19 | Section 4 (4A, 4B, 4C) for R1 | Present; shared-not-exclusive stated | PASS |
| E20 | Optionality register: columns, scope, YAML matches report | Report has 7 rows, YAML has 6 (A3 row missing); H1 rests on 🎙️ only and is not registered | **FAIL (MINOR, F10)** |
| E21 | 6C uses the INJECTED Gate 0 block | Shows Core 68, Moat 15, GT 83, 4 moats STRONG. Current B01: Core 63, Moat 13, GT 76, 3 moats MODERATE | **FAIL (MAJOR, F11)** |
| E22 | 6D combined classification | AVERAGE; survives the corrected Gate 0 inputs | PASS |
| E23 | 6A, 6B, 6E present | Present (6E also stale, see F11) | PASS |
| E24 | YAML block fields valid (catalysts_12m is a 12-month list) | Two rows carry "24-36m" and "long" windows | **FAIL (MINOR, F12)** |
| E25 | Not conflated with FTTCP | Stated at the top and kept apart | PASS |

Emerging Moat: 24 rules checked, 8 fail, 16 pass.

### 2.3 Emerging Moat findings

**F5 (MINOR). Evidence tiers mislabelled on concall and presentation items.** Stage 7
rule 2 classes a statement "in concall or presentation" as 🎙️. B07 tags "90+ clients,
65 most active" (Jun-2026 call p.1) and the 60% repeat rate (Inv. Pres. p.7) as [D].
C1 is scored at 0.7, so the score does not move. The labels feed evidence_mix
{documented: 9}, which overstates the 📄 count.

**F6 (MINOR). Multiplier does not follow the stated tier on A3 and F2.**
- A3: the only evidence row is tagged [D] (AR p.15; call p.1), but the row is scored at
  🔍 0.5. Per the stated tier: 1 × 1.0 = 1.0 (+0.5).
- F2: scored at "🎙️/📄 mixed, 0.5". The rubric has three multipliers only (1.0, 0.7,
  0.5), and 0.5 belongs to 🔍. The listed evidence is [D]/[D]. Per the stated tier:
  1.0 (+0.5). At 🎙️ the lowest defensible value is 0.7 (+0.2).
- Both errors understate the score. Neither crosses a band.

**F7 (MINOR). H1 raw score is out of line with its own label.** H1 is labelled "Weak" on
one uncorroborated CMD claim (Jun-2026 call p.28), with no named competitor exit. It is
scored MM = 2. Every other Weak row (A3, C2, F2, H2) is scored at 1. Recomputed:
ML 1 × 0.7 = 0.7 (-0.7).

**F8 (MINOR). The completionist recount is approximate and does not match the scorecard.**
- The rule wants "📄 recount performed: [n] documented items across [m] categories".
  B07 writes "approximately 9".
- The UL approval (Reg 30, 16-Oct-2025) counts twice, once in A1 and once in E2. The
  distinct count is 8, not 9.
- The recount covers 4 categories. Five rows are scored at the 📄 1.0 multiplier (A1, B2,
  E2, H2, R1). H2 is left out.
- Section 6D then says "5 categories score Strong/Moderate on 📄-grade evidence (A1, B2,
  C1, E2, R1)". That contradicts the recount's own statement that C1's strongest evidence
  is 🎙️.
- The guard outcome is unchanged: 10 non-zero rows, below 12.

**F9 (MINOR). I2 test not run for every claimed moat.** Stage 7 says "For each moat
claimed anywhere in this scan, answer: what SPECIFIC thing would the best-resourced
competitor have to destroy". B07 runs it for B2 only. The analyst_note claims it holds
"for every moat claimed here", but the report shows no work for A1, C1, E2 or R1. The
score of 0 is likely to survive, because nothing in the corpus names a competitor
sacrifice. The procedure is still incomplete.

**F10 (MINOR). Optionality register incomplete, and report and block disagree.** The
report register has 7 rows. B07-emoat.yaml optionality_register has 6 rows, and the A3
process-innovation row is missing. The rule scope is "scored 0 or rest only on 🎙️/🔍
evidence". H1 rests on one 🎙️ claim only and is not registered.

**F11 (MAJOR). Section 6C and 6E carry stale Gate 0 values.**
- Stage 7 section 6C must use "the INJECTED Gate 0 block".
- B07 shows Core 68, Moat 15, Grand Total 83, "4 confirmed, class STRONG". 6E repeats
  "4 confirmed moats, STRONG".
- The current B01 block (round 2) reads core_score 63, moat_score 13, grand_total 76,
  moats_confirmed 3, moat_class MODERATE (B01-gate0.yaml). The B01 analyst_note tells B07
  to read 3 / MODERATE.
- B07 was not refreshed after the B01 round-2 correction. The 6D outcome (AVERAGE)
  survives, because the corrected backward read is further from GOOD+. A downstream stage
  that reads 6C gets a moat class that no current block supports.
- Fix: stage 7 refreshes 6C and 6E from the current B01 block. If F1 is ruled toward
  Reading 2, the moat class goes back to STRONG, so 6C must follow the final B01 after
  F1 is resolved.

**F12 (MINOR). catalysts_12m holds items outside 12 months.** The "EBITDA/PAT margin
recovery" row carries window "medium, 24-36m". The US bulk contract row carries "long".
The field feeds Pillar 3 catalyst proximity. These rows belong in 6A or in the register,
not in the 12-month list.

### 2.4 Observations (not counted as rule failures)
- **O1.** A1 is scored HH (4.0) as a "rare" capability. B07's own 6B risk row concedes that
  "multiple Indian peers (KSB, Atam, Quest Flow) hold overlapping certifications". An
  impact of M (HM = 3, -1.0) matches the report's own text better. The row is also close
  to B2: one certification and qualification base supports both rows. Two readings: the
  certification set is peer-scarce (HH holds), or it is table stakes among qualified
  suppliers (HM). Separating observation: a peer holder count for ClassNK valve type
  approval, which is not in this corpus. This is a judgment on company quality, outside
  this verifier's remit, so I record it and do not fail it.
- **O2.** E1 cites "company memory's peer set" as support. H2 cites "company memory" next
  to Inv. Pres. p.6. Per CLAUDE.md, company memory is weighed, never anchored evidence.
  Neither item changes a score. The Inv. Pres. anchor carries H2.
- **O3.** 6D says the mix shift is "a genuine, evidenced climb of the Section 3G
  qualification ladder". Section 3G is the Role 2 Entrepreneur Ledger, and the quality
  ladder is a Mental Model construct. Stage 7 should not claim a rung placement. The
  wording is loose and changes no score.

---

## PART 3: VALUATION (B10, B11)

NOT RUN. Pending phase 3. Rules 4-7 and 9-15 do not apply in phase-1 scope.

---

## SUMMARY

| Framework | Rules checked | Pass | Fail | CRITICAL | MAJOR | MINOR |
|---|---|---|---|---|---|---|
| Gate 0 (B01) | 29 | 24 | 5 | 0 | 2 rows (1 finding, F1) | 3 |
| Emerging Moat (B07) | 24 | 16 | 8 | 0 | 1 | 7 |
| Valuation (B11) | NOT RUN, phase 3 | | | | | |
| **Total** | **53** | **40** | **13** | **0** | **2 findings** | **10 findings** |

Acceptance rate: 40 / 53 = 75.5%. The denominator is 4 or more, so the rate applies. It
is above 60%, so it does not trigger REWORK.

Decision impact: none. Gate 0 final classification AVERAGE stands on both F1 readings.
Emerging Moat MODEST stands across the recomputed range 18.2 to 19.7. The combined
classification AVERAGE stands.

Rework routing (for the orchestrator):
- Stage 1: F1. Pick one ROCE basis for all five years (operator ruling on "the data
  source"), recompute Block A, and correct the "denominator not shown" sentence.
- Stage 7: F11. Refresh 6C and 6E from the final B01 block, after F1 is resolved. The
  MINOR items F5-F10 and F12 can be fixed in the same pass.

```yaml
stage: B12c
company: "RAPPID"
run_date: "2026-09-19"
model: "claude-opus-5"
status: complete
scope: "phase 1 only (B01 Gate 0, B07 Emerging Moat). valuation, expectation_ledger, business_understanding_narrative NOT RUN, pending phase 3; their fields below are schema placeholders, not results."
gate0:
  rules_checked: 29
  fails:
    - {rule: "G03 ROCE source precedence / single basis", severity: MAJOR, claimed: "mixed series 85.4/39.5/47.7 computed + 17/14 AR-disclosed; RHP ROCE rejected for different denominator; AR denominator 'not shown'", recomputed: "AR K = H + I + DTL (AR p.69 Note 36) is the same family as RHP (Tangible NW + Total Debt + DTL, RHP p.151 note 6). Uniform source: 18.38/15.85/29.88/17/14 -> A1 3, A2 3, A4 1"}
    - {rule: "G04 Block A total", severity: MAJOR, claimed: "13 (core 63, GT 76)", recomputed: "12 (core 62, GT 75) uniform source; 15 (core 65, moat 15, 4 moats STRONG, GT 80) uniform computed; final AVERAGE either way"}
    - {rule: "G13 D2 formula EBIT/Interest", severity: MINOR, claimed: "7.52x AR-disclosed", recomputed: "7.27x (9.67/1.33); score 4 unchanged"}
    - {rule: "G16 E2 3-year window", severity: MINOR, claimed: "69.46% pre-issue to 51.58%, 'approximating 3 years'", recomputed: "window is ~18 months (Sep-2024 to Mar-2026); Mar-2023 start NOT FOUND; score 0 unchanged"}
    - {rule: "G18 M1 window, use all history", severity: MINOR, claimed: "FY23-FY26 +6.3pp", recomputed: "FY22-FY26 16.0% to 19.4% = +3.4pp; score 5 unchanged"}
emoat:
  rules_checked: 24
  fails:
    - {rule: "E02 evidence taxonomy", severity: MINOR, detail: "concall/presentation items (90+ clients call p.1; 60% repeat rate Inv. Pres. p.7) tagged [D]; inflates evidence_mix documented"}
    - {rule: "E07 multiplier vs stated tier", severity: MINOR, detail: "A3 [D] scored at 0.5 (should be 1.0, +0.5); F2 'mixed 0.5' is not a defined multiplier (0.7-1.0, +0.2 to +0.5)"}
    - {rule: "E08 raw score consistency", severity: MINOR, detail: "H1 'Weak' on one CMD claim scored MM=2; other Weak rows at 1; recomputed 0.7 (-0.7)"}
    - {rule: "E12 completionist recount", severity: MINOR, detail: "'approximately 9'; UL approval double-counted (distinct 8); H2 scored at 1.0x omitted; 6D claims C1 is documented-grade, contradicting recount"}
    - {rule: "E16 I2 test for each claimed moat", severity: MINOR, detail: "run for B2 only; A1, C1, E2, R1 not shown; score 0 likely survives"}
    - {rule: "E20 optionality register", severity: MINOR, detail: "report 7 rows, YAML 6 (A3 row missing); H1 claim-only not registered"}
    - {rule: "E21 6C uses injected Gate 0 block", severity: MAJOR, detail: "6C/6E show Core 68, Moat 15, GT 83, 4 moats STRONG; current B01 is Core 63, Moat 13, GT 76, 3 moats MODERATE; 6D AVERAGE survives"}
    - {rule: "E24 catalysts_12m window", severity: MINOR, detail: "margin-recovery row '24-36m' and US contract row 'long' sit in a 12-month list"}
valuation: {rules_checked: 0, fails: []}  # NOT RUN, pending phase 3
expectation_ledger: {present: false, downside_row: false, all_rows_confirm_by: false, all_rows_metric_threshold: false, prob_in_range: false, decay_status_valid: false, off_ledger_credit: false, residual_pct_cmp: 0, residual_starter_cap_ok: true, fails: []}  # NOT RUN, pending phase 3; placeholder values, not findings
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: []}  # NOT RUN, pending phase 3 (stage 13); placeholder values, not findings
recomputed_destination_pe: ""  # not in phase-1 scope
recomputed_decision: ""        # concur: Gate 0 AVERAGE, EM MODEST (18.2-19.7 recomputed range), combined AVERAGE
findings:
  - {id: F1, stage: B01, severity: MAJOR, rule: "ROCE formula / source precedence (prompts/01 FORMULA DEFINITIONS)", finding: "5-year ROCE series mixes computed (FY22-24) and AR-disclosed (FY25-26) bases; RHP disclosed ROCE rejected for a denominator that AR p.69 Note 36 K (H + I + DTL) shares; report wrongly says AR denominator not shown", recomputed: "Reading 1 uniform source: A 12, core 62, moat 13 MODERATE, GT 75, raw GOOD. Reading 2 uniform computed: A 15, core 65, moat 15 STRONG, GT 80, raw GOOD+. Final AVERAGE both (deal-breaker 4)", separating_observation: "operator ruling on whether 'the data source' includes AR/RHP disclosures", decision_impact: none, rework: "stage 1"}
  - {id: F2, stage: B01, severity: MINOR, rule: "D2 EBIT/Interest", finding: "disclosed 7.52x used over formula", recomputed: "7.27x, score 4 unchanged"}
  - {id: F3, stage: B01, severity: MINOR, rule: "E2 change over 3 years", finding: "18-month window labelled as approximating 3 years", recomputed: "score 0 unchanged; Mar-2023 holding NOT FOUND"}
  - {id: F4, stage: B01, severity: MINOR, rule: "pipeline rule 6 / M1", finding: "M1 on FY23-26 while FY22-26 available", recomputed: "+3.4pp FY22-26, score 5 unchanged"}
  - {id: F5, stage: B07, severity: MINOR, rule: "stage 7 rule 2 taxonomy", finding: "concall/presentation statements tagged documented", recomputed: "no score change; evidence_mix documented overstated"}
  - {id: F6, stage: B07, severity: MINOR, rule: "Section 5 multipliers", finding: "A3 and F2 multipliers do not match stated tiers", recomputed: "A3 1.0 (+0.5); F2 0.7-1.0 (+0.2 to +0.5)"}
  - {id: F7, stage: B07, severity: MINOR, rule: "Section 5 L x I consistency", finding: "H1 Weak scored MM", recomputed: "0.7 (-0.7)"}
  - {id: F8, stage: B07, severity: MINOR, rule: "completionist guard recount", finding: "approximate count, UL double-counted, H2 omitted, 6D contradicts recount on C1", recomputed: "8 distinct documented items across 5 categories scored at 1.0x; guard still passes (10 non-zero rows)"}
  - {id: F9, stage: B07, severity: MINOR, rule: "I2 for each claimed moat", finding: "test applied to B2 only", recomputed: "score 0 likely unchanged"}
  - {id: F10, stage: B07, severity: MINOR, rule: "optionality register", finding: "YAML omits A3 row; H1 claim-only not registered", recomputed: "n/a"}
  - {id: F11, stage: B07, severity: MAJOR, rule: "6C uses injected Gate 0 block", finding: "stale round-1 Gate 0 values (68/15/83, 4 STRONG) in 6C and 6E", recomputed: "63/13/76, 3 MODERATE per current B01 (subject to F1 resolution); 6D AVERAGE unchanged", decision_impact: none, rework: "stage 7 sections 6C, 6E"}
  - {id: F12, stage: B07, severity: MINOR, rule: "catalysts_12m", finding: "24-36m and 'long' windows inside the 12-month list", recomputed: "move to 6A / register"}
critical_count: 0
major_count: 2
minor_count: 10
acceptance_rate: 75.5             # 40 passed / 53 checked (gate0 24/29, emoat 16/24)
```
