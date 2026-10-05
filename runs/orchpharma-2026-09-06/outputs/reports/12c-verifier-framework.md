# STAGE 12C — VERIFIER C: FRAMEWORK ADHERENCE AUDIT
Company: Orchid Pharma Ltd (ORCHPHARMA) | Run date: 2026-09-06 | Model: claude-opus-4-8
Scope: PHASE 1 ONLY — Gate 0 (B01) and Emerging Moat (B07). Valuation audit (B10/B11)
deferred to phase 3; those artifacts do not exist and the valuation framework documents
were not loaded.

Rule sources read: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md.
Artifacts audited: outputs/reports/01-gate0.md + outputs/blocks/01-gate0.yaml;
outputs/reports/07-emoat.md + outputs/blocks/07-emoat.yaml.
Data re-derived independently from inputs/screening/screener-Data_Sheet.csv.

I audited rule application, not company quality and not source fidelity. Verifier A owns
the existence-of-a-number question. Where I recomputed, I recomputed from the numbers the
stage itself stated, plus the screener CSV the orchestrator named as the Gate 0 data source.

## CONVENTION USED IN THIS REPORT

- FAIL = the framework was not applied as written. Counted against acceptance_rate.
- PASS-with-note = the stage complied with the literal rule, but made a choice a
  downstream stage could misread. Surfaced in findings, NOT counted as a fail.
- Every FAIL carries the recomputed value beside it.

---

# PART 1: GATE 0 (B01) COMPLIANCE

## 1.1 Inputs re-derived from the screener CSV

I rebuilt the Block A and Block D inputs from screener-Data_Sheet.csv before checking any
score. EBIT = PBT + Interest, per the stage's stated method:

| FY | PBT (csv) | Interest (csv) | EBIT | Cap. Employed (ESC+Res+Borr) | ROCE % | Stage said |
|---|---|---|---|---|---|---|
| 17 | -543.77 | 346.77 | -197.00 | 2,639.41 | -7.46 | -7.46 ✓ |
| 18 | -398.96 | 310.26 | -88.70 | 2,410.19 | -3.68 | -3.68 ✓ |
| 19 | 69.41 | 6.69 | 76.10 | 2,525.92 | 3.01 | 3.01 ✓ |
| 20 | -131.07 | 6.23 | -124.84 | 1,332.38 | -9.37 | -9.37 ✓ |
| 21 | -116.53 | 52.21 | -64.32 | 1,105.65 | -5.82 | -5.82 ✓ |
| 22 | 1.58 | 33.46 | 35.04 | 915.34 | 3.83 | 3.83 ✓ |
| 23 | 48.47 | 32.90 | 81.37 | 1,019.99 | 7.98 | 7.98 ✓ |
| 24 | 91.94 | 16.74 | 108.68 | 1,304.65 | 8.33 | 8.33 ✓ |
| 25 | 95.56 | 14.93 | 110.49 | 1,441.90 | 7.66 | 7.66 ✓ |
| 26 | 10.43 | 8.98 | 19.41 | 1,650.38 | 1.18 | 1.18 ✓ |

The capital-employed proxy reconciles to the framework formula exactly: Total Assets minus
Other Liabilities equals ESC + Reserves + Borrowings on every row (FY17: 3,255.59 − 616.18 =
2,639.41). The Data_Sheet publishes no ROCE column, so the "compute only when absent, and
state computed" branch is the correct one and the stage used it and said so. PASS.

## 1.2 Block-by-block rule audit

### BLOCK A — RETURN ON CAPITAL

| Rule | Stated input | Threshold applied | Re-derived | Verdict |
|---|---|---|---|---|
| A1 Median ROCE | 2.10% | <10 = 0 | Sorted 10-year series middle pair = 1.18 and 3.01, median 2.095 → 2.10 ✓ | PASS |
| A2 Min single-year ROCE | -9.37% (FY20) | <8 = 0 | Series minimum is -9.37 ✓ | PASS |
| A3 Median ROE | 3.86% | <12 = 0 | See below | FAIL x2 (MINOR) |
| A4 ROCE trend | FY26 1.18 vs FY17 -7.46 | latest ≥ earliest = 5 | Correct as written | PASS |
| Block A subtotal | 0+0+0+5 = 5 | — | 5 ✓ | PASS |

A3, re-derived. ROE = PAT ÷ average net worth, net worth = ESC + Reserves:

| FY | PAT | Avg NW | ROE % |
|---|---|---|---|
| 21 | -116.53 | 709.45 | -16.43 |
| 22 | -1.95 | 650.15 | -0.30 |
| 23 | 46.32 | 668.02 | 6.93 |
| 24 | 92.17 | 929.06 | **9.92** |
| 25 | 99.66 | 1,218.38 | 8.18 |
| 26 | 9.96 | 1,277.54 | 0.78 |

Two defects, both MINOR:

1. **A3 lists five values for a six-year median.** The report prints "-16.43, -0.30, 0.78,
   6.93, 8.18" and omits FY2024 = 9.92%. The stated median of 3.86% is nonetheless
   ARITHMETICALLY CORRECT: with FY24 included the sorted six are -16.43, -0.30, 0.78, 6.93,
   8.18, 9.92, middle pair 0.78 and 6.93, median 3.855. Score 0 stands. Presentation defect,
   not a scoring error.
2. **A3 drops FY2017-FY2020 as "N/M".** The framework's ROE definition gives one adaptation
   only: use closing net worth where opening is unavailable. It gives no authority to exclude
   years from a median. The negative-endpoint escape is a CAGR edge rule and A3 is not a
   CAGR. Recomputed on all available years the median falls further below 12%, so the score
   is 0 either way. The stage disclosed the exclusion and its reason, which is why this is
   MINOR and not MAJOR.

### BLOCK B — CASH GENERATION QUALITY

| Rule | Stated input | Threshold | Re-derived | Verdict |
|---|---|---|---|---|
| B1 Cum CFO ÷ Cum PAT | 883.76 ÷ -780.23 = -1.13 | <0.50 = 0 | CFO sum 883.76 ✓, PAT sum -780.23 ✓ | PASS |
| B2 FCF-positive proportion | 1 of 3 = 33% | <50 = 0 | 33.3% ✓ | PASS |
| B3 Cum FCF ÷ Cum PAT | -36.64 ÷ 238.15 = -0.15 | negative = 0 | FCF sum -71.16+75.58-41.06 = -36.64 ✓; PAT 46.32+92.17+99.66 = 238.15 ✓ | PASS |
| B4 Change in WC days | 157.44 vs 172.58 = -15.14 | decrease >5 = 5 | FY23: 117.97+125.36-70.75 = 172.58 ✓; FY25: 95.75+129.20-67.51 = 157.44 ✓ | PASS |
| Block B subtotal | 0+0+0+5 = 5 | — | 5 ✓ | PASS |

B1 applies the ratio literally against a negative denominator and scores 0. That is the rule
as written; the framework gives no negative-PAT branch. PASS. The stage stated the FY22-26
subset ratio (1.45) as unscored context, which is permitted and useful.

WC days basis: revenue basis used throughout, with the reason stated (raw material cost alone
is not full COGS). The formula explicitly requires the basis to be stated. PASS.

**FAIL (MINOR) — Block B mixes two CFO bases inside one block.** B1 uses Data_Sheet CFO
(FY23 18.34, FY24 125.99, FY25 19.22). B2 and B3 use AR cash-flow CFO for the same three
years (13.39, 130.73, 27.48). The gap is unreconciled and unexplained, almost certainly a
standalone-versus-consolidated difference. Recomputed on the Data_Sheet basis throughout:
FY23 FCF = 18.34 − 84.55 = -66.21; FY24 = 125.99 − 55.15 = +70.84; FY25 = 19.22 − 68.54 =
-49.32; cumulative -44.69, still negative, still 1-of-3 positive. B2 = 0 and B3 = 0 on either
basis, so no score moves. The defect is that one block reports two different CFO numbers for
the same year without saying which is authoritative.

### BLOCK C — GROWTH

| Rule | Stated input | Threshold | Re-derived | Verdict |
|---|---|---|---|---|
| C1 Revenue CAGR | 4.97% over 9 years | <5 = 0 | (1232.78/796.51)^(1/9)−1 = 4.974% ✓ | PASS |
| C2 PAT CAGR | N/M, negative endpoint | N/M = 0 | FY17 PAT -495.43, endpoint negative ✓ | PASS |
| C3 Positive YoY years | 5 of 9 = 55.6% | 50-74 = 1 | Declines FY18/19/20/21, increases FY22-26 ✓ | PASS |
| C4 PAT − Revenue CAGR | PAT CAGR N/M | C4 = 0 per edge rule | Correct branch ✓ | PASS |
| Block C subtotal | 0+0+1+0 = 1 | — | 1 ✓ | PASS |

CAGR edge rules audited specifically, as my rule 2 requires. All three fire correctly: the
negative endpoint marks C2 as N/M rather than producing a synthetic number; the loss-to-profit
swing is recorded in data_notes with the years named; C4 takes the mandated 0. The C1 span is
9 years for 10 data points, which is the correct exponent. PASS on the edge-rule check.

### BLOCK D — BALANCE SHEET STRENGTH

| Rule | Stated input | Threshold | Re-derived | Verdict |
|---|---|---|---|---|
| D1 Net Debt ÷ EBITDA | 279.38 ÷ 62.66 = 4.46x | >3x = 0 | 362.59−83.21 = 279.38 ✓; 19.41+43.25 = 62.66 ✓; 4.459x ✓ | PASS |
| D2 Interest coverage | 19.41 ÷ 8.98 = 2.16x | 1.5-2.9 = 1 | 2.161x ✓ | PASS |
| D3 Debt ÷ Equity | 362.59 ÷ 1,287.79 = 0.28 | 0.1-0.5 = 4 | 0.2816 ✓ | PASS |
| D4 Current ratio | NOT FOUND for FY26 | not available = 0 | See note | PASS-with-note |
| Block D subtotal | 0+1+4+0 = 5 | — | 5 ✓ | PASS |

D4 PASS-with-note (MINOR). The stage scored 0 because FY2026 has no current/non-current
split, while FY2025 audited current ratio of 3.31x sits in the corpus and would score 5.
Operating rule 5 is explicit: a data point not available is marked N/A and scored 0. The
metric is defined "(latest)", and D1, D2 and D3 all take FY2026 as latest, so the choice is
internally consistent and literally compliant. I do not fail it. Operator visibility matters
though: had the stage read "latest" as "latest available", Block D would be 10 and core would
be 34, still under 40, still AVOID. No decision moves either way.

### BLOCK E — SHAREHOLDER ALIGNMENT

| Rule | Stated input | Threshold | Re-derived | Verdict |
|---|---|---|---|---|
| E1 Promoter holding | 69.84% | ≥60 = 5 | 3,54,19,957 ÷ 5,07,19,105 = 69.84% ✓ | PASS |
| E2 Holding change over 3 years | 0.00% on a 1-year proxy | ±1% = 3 | See below | **FAIL (MAJOR)** |
| E3 Pledge | NOT FOUND | not available = 0 | Correct branch ✓ | PASS |
| E4 Contingent liab ÷ NW | 14.10 ÷ 1,267.29 = 1.11% | <5 = 5 | 1,409.64 lakh = 14.10cr ✓; 1.112% ✓ | PASS-with-note |
| Block E subtotal | 5+3+0+5 = 13 | — | 13 ✓ | PASS |

**FAIL (MAJOR) — E2 scores 3 on a metric that could not be computed.** The rule is "Promoter
holding change over 3 years". The corpus holds two annual data points, 31-Mar-2024 and
31-Mar-2025. The stage itself writes "a 1-year proxy, NOT a true 3-year trend" and then scores
it anyway. Operating rule 5 governs: confirm the figure exists, and where it does not, mark
N/A and score 0. A one-year proxy for a three-year metric is a gap fill. The stage applied
rule 5 correctly at E3 (pledge, NOT FOUND, 0) and D4 (current ratio, NOT FOUND, 0) and then
did not apply it at E2. That internal inconsistency is what makes this a fail rather than a
judgment call.

Recomputed: **E2 = 0, Block E = 10/20, core score = 26/100.** Classification is unchanged
(26 < 40 → AVOID). Deal breakers 1 and 2 are unaffected. No decision moves.

E4 PASS-with-note (MINOR). Contingent liabilities come from the CONSOLIDATED note 45; net
worth comes from the Data_Sheet standalone series. The stage flagged the mismatch and named
the reason (no standalone note 45 located, subsidiaries described as dormant). The framework
does not specify a basis for E4. The band is not close: at 14.10cr the ratio would have to
rise past 63cr to leave the <5% band. No score effect.

### BLOCK F — QUANTITATIVE MOAT SCORING

| Test | Stage score | Re-derived | Verdict |
|---|---|---|---|
| M1 Pricing power | 3 | See below | **FAIL (MAJOR)** |
| M2 Cost advantage | 0 | 12.79% vs peer median 21.15%, 8.36pp below → "below = 0" ✓ | PASS |
| M3 Capital efficiency | 0 | FAT 921.93/632.71 = 1.457x >1x, but ROCE 7.66% <12% → bottom band fails → 0 ✓ | PASS |
| M4 Customer stickiness | 0 | 4 decline years → "3+ decline years = 0" ✓ | PASS |
| M5 Scale and dominance | 1 | See below | FAIL (MINOR) |
| M6 Technology / R&D | 0 | R&D/Rev 0.91% < 1% floor, margin below peer median → 0 ✓ | PASS |
| M7 Regulatory / license | 0 | Peer player count absent → "score 0 and mark PEER DATA NEEDED" ✓ | PASS |
| M8 Distribution | 1 | Reach quantified but no growth baseline → "mentioned = 1" ✓ | PASS |
| M9 Brand | 0 | GM proxy 36.21% vs 60.83% median → "at/below = 0" ✓; proxy basis stated as the rule requires ✓ | PASS |
| M10 Switching costs | 1 | Overall growth with 4 decline years → "2+ decline years = 1" ✓ | PASS |
| M11 Network effects | 5 | (1232.78/665.90)^(1/3)−1 = 22.79% > (665.90/483.80)^(1/3)−1 = 11.24%, selling% 13.17 → 5.03 declining → 5 ✓; ≥6 years available so the two-window test is legitimate ✓ | PASS |
| M12 Negative WC / float | 0 | WC days 157-173, all >45 → 0 ✓ | PASS |
| Moat subtotal | 11 | 3+0+0+0+1+0+0+1+0+1+5+0 = 11 ✓ | PASS |
| Moat classification | MODERATE | 2 present (M1, M11); band 2-3 = MODERATE ✓ given the scores as stated | PASS |

I re-derived the EBITDA margins M1 rests on, from the CSV, subtracting change in inventory
from raw material cost as the stage described: FY23 84.45cr on 665.90 = 12.68%; FY24 111.25
on 819.37 = 13.58%; FY25 117.89 on 921.93 = 12.79%. All three match the stage exactly, and
the ±2pp stability leg is satisfied.

**FAIL (MAJOR) — M1 uses an undeclared revenue-CAGR window that the scorecard contradicts
elsewhere.** M1's band requires "margin stable ±2pp AND revenue CAGR ≥10%". The test does not
name a window. The stage used FY23→FY25 (17.67%, which I confirm: (921.93/665.90)^0.5 − 1 =
17.66%). The same scorecard's own revenue-CAGR line, C1, is 4.97%. A single scorecard cannot
carry two authoritative revenue CAGRs without declaring which governs which test, and the
stage declared nothing.

Recomputed on C1's basis: revenue CAGR 4.97% < 10%, margin stable rather than declined, so no
band is met and **M1 = 0**. Consequences: moats present falls from 2 to 1 → **moat_class
MODERATE becomes THIN**; **moat_score 11 becomes 8**; **grand_total 40 becomes 37**.
Classification is unchanged: the matrix keys on core score for the AVOID branch (Core <40 →
AVOID), and core is untouched at 29 (or 26 after the E2 fail). No decision moves.

This is rated MAJOR and not MINOR because moat_class is a field a downstream stage consumes
directly. B07 Section 6C reprints "2 confirmed, moat_class MODERATE" verbatim. I am not
asserting the stage's reading is wrong; the framework is genuinely silent. I am asserting
that a silent framework obliges the stage to declare the window it chose, and that the
alternative reading flips a downstream field.

**FAIL (MINOR) — M5 scores 1 where the block's own peer rule directs 0.** Block F's preamble:
"If a test needs peer data that is not provided, score 0 and mark PEER DATA NEEDED (never
guess peer figures)." The stage marked M5 "PARTIAL / PEER DATA NEEDED" because only three
peers were supplied and the true segment ranking is unknown, then scored 1 on the partial set
anyway. The stage applied the rule correctly at M7 (scored 0, marked PEER DATA NEEDED), which
again makes this an internal inconsistency. Recomputed: M5 = 0, moat_score 11 → 10 (or 7 in
combination with the M1 recompute). Moats present is unaffected (1 < 3), so moat_class does
not move on this fail alone.

## 1.3 Classification, confidence and deal-breaker audit

| Check | Stage | Re-derived | Verdict |
|---|---|---|---|
| Core score | 29 | 5+5+1+5+13 = 29 ✓ | PASS |
| Grand total | 40 | 29+11 = 40 ✓ | PASS |
| Classification matrix | Core 29 <40 → AVOID | Matrix branch correct ✓ | PASS |
| Data confidence tier | "10 years → full tier, no downgrade" in the report | 10+ yrs = full ✓ | PASS in body |
| `history_downgrade` field | **true** | Should be **false** | **FAIL (MAJOR)** |
| Deal breaker 1 (Block A <8) | fired | A = 5 ✓ | PASS |
| Deal breaker 2 (Block B <8) | fired | B = 5 ✓ | PASS |
| Deal breaker 3 (median ROCE <10%) | fired | 2.10% ✓ | PASS |
| Deal breaker 4 (cum CFO/PAT <0.50) | fired | -1.13 ✓ | PASS |
| Deal breaker 5 (pledge >15%) | not fired | No pledge evidence either way ✓ | PASS |
| Deal breaker 6 (ND/EBITDA >3x AND IC <3x) | fired → AVOID | 4.46x and 2.16x ✓ | PASS |
| Deal breaker 7 (revenue declined in majority) | not fired | 4 of 9 declines, not a majority ✓ | PASS |
| Deal breaker 8 (PAT negative in last 3 years) | not fired | FY24 92.17, FY25 99.66, FY26 9.96 ✓ | PASS |
| Deal breaker 9 (history <3 years) | not fired | 10 years ✓ | PASS |
| Cap application | Caps 1-4 sit above AVOID; DB6 sets AVOID; final AVOID | Caps are ceilings, not floors; AVOID is correct ✓ | PASS |
| `deal_breakers: [1,2,3,4,6]` | — | Matches the fired set exactly ✓ | PASS |

**FAIL (MAJOR) — the block contradicts its own report on the confidence adjustment.** The
report body states "Data confidence: 10 years available → full tier, no data-confidence
downgrade." The YAML emits `history_downgrade: true`. The framework's confidence ladder gives
"10+ yrs full", and the one-tier downgrade belongs to the 3-4 year branch. The correct field
value is **false**. Any downstream stage reading the block rather than the report is told the
classification was already downgraded once, which it was not.

Severity MAJOR, not CRITICAL, for one reason only: AVOID is the bottom of the classification
set, so a spurious downgrade flag cannot move it lower. Had the core score landed anywhere
above 40, this field would have changed a classification and would be CRITICAL. This is the
single most mechanical defect in B01 and the cheapest to fix.

## 1.4 Operating-rule and format audit

| Rule | Verdict | Note |
|---|---|---|
| Rule 1, entire scorecard in one response, no stops | PASS | Complete, no confirmation requests |
| Rule 3, every extracted number shown with its score | PASS | Full series tables for ROCE, WC days, margins |
| Rule 4, source anchors mandatory | PASS | (screener-data), (Annual_Report_2025.pdf, p.__), note references throughout |
| Rule 5, grounded claims, no estimated fills | PASS | NOT FOUND used at D4, E3, FY26 cost split, FY17-22 capex |
| Rule 6, opening data-availability line, exact form | PASS | "Data available: 10 years (FY2017 to FY2026). Scoring adapted to 10-year history." |
| Formula: ROCE | PASS | Proxy reconciles to Total Assets − Other Liabilities; "computed" stated |
| Formula: ROE | FAIL (MINOR) | Year exclusion not authorised, see 1.2 A3 |
| Formula: WC days | PASS | Revenue basis used and stated, as the rule requires |
| Formula: FCF (CFO − capex, acquisitions excluded) | FAIL (MINOR) | Two CFO bases inside one block, see 1.2 Block B |
| Formula: CAGR | PASS | Correct exponent, edge rules honoured |
| Output format: dashboard, moat bars, classification box, strongest/weakest, decision line | PASS | All five present |
| YAML field completeness and report agreement | FAIL (MAJOR) | `history_downgrade`, see 1.3 |
| `flags` includes FLAG-GATE0 where classification ≤ AVERAGE with depressors | PASS | Present, plus three additive flags (permitted) |

The stage's handling of the FY2026 evidence problem deserves a positive note, since a
verifier that only reports defects gives the operator a distorted picture. FY2026 has no
primary filing; the stage tagged every FY2026 number "unverified, screener-sourced", scored
the deal breaker it triggers, and then stated plainly that AVOID stands on the audited years
alone without it. It also surfaced the 7.95cr quarterly-versus-annual PBT gap rather than
smoothing it. That is the "flags propagate, only mechanical failures halt" discipline applied
correctly.

## 1.5 Gate 0 tally

Rules checked: 56. Fails: 7 (3 MAJOR, 4 MINOR). Acceptance: 49/56 = **87.5%**.

Recomputed values carried forward, none of which change the verdict:
- E2 = 0 → Block E 10 → **core score 26** (stage: 29)
- M1 = 0 → moats present 1 → **moat_class THIN** (stage: MODERATE)
- M5 = 0 → **moat_score 7-8** (stage: 11) → **grand_total 33-34** (stage: 40)
- `history_downgrade` = **false** (stage: true)
- **Classification AVOID: I concur.** It survives every recompute above.

---

# PART 2: EMERGING MOAT (B07) COMPLIANCE

## 2.1 Category completeness — all 23 rows

Verifier rule 3 requires all categories addressed or explicitly NO EVIDENCE. I counted the
scan: A1-A4 (4), B1-B3 (3), C1-C2 (2), D1-D2 (2), E1-E2 (2), F1-F2 (2), G1-G2 (2), H1-H3 (3),
I1-I2 (2), R1 (1) = **23 rows, all present** in Section 3, in the Section 3 summary table, and
in the Section 5 scoring table. PASS.

Every zero-scored category carries an explicit statement rather than silence: B3, D1, D2, E2,
F1, I1, I2 say NO EVIDENCE FOUND or equivalent; C2 says NOT FOUND and labels it a data gap
rather than an evidenced negative; A3, F2 and G1 record NEGATIVE findings, which is a stronger
form of compliance than a blank. PASS on the no-force-fit rule.

E2 (China+1) deserves specific credit: the stage scored it 0 and named the reason as
avoidance of double-counting with B1, since the 7-ACA import-substitution evidence was already
credited there. That is the CLAUDE.md one-improvement-one-mechanism rule applied without being
asked. PASS.

## 2.2 Scorecard arithmetic, re-derived

Raw = likelihood x impact (HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0); adjusted = raw x
quality (📄 1.0, 🎙️ 0.7, 🔍 0.5). I re-derived every non-zero row:

| ID | Raw | Matrix label valid? | Quality | Adjusted | Check |
|---|---|---|---|---|---|
| A1 | 3 | HM = 3 ✓ | 📄 1.0 | 3.0 | ✓ |
| A2 | 3 | MH = 3 ✓ | 📄 1.0 | 3.0 | ✓ |
| A4 | 2 | MM = 2 ✓ | 🎙️ 0.7 | 1.4 | ✓ |
| B1 | 3 | MH = 3 ✓ | 📄 1.0 | 3.0 | ✓ |
| B2 | 2 | MM = 2 ✓ | 🔍 0.5 | 1.0 | ✓ |
| C1 | 2 | MM = 2 ✓ | 🎙️ 0.7 | 1.4 | ✓ |
| E1 | 1 | LM = 1 ✓ | 🎙️ 0.7 | 0.7 | ✓ |
| G2 | 1 | LM = 1 ✓ | 📄 1.0 | 1.0 | ✓ |
| H1 | 1 | LM = 1 ✓ | 🔍 0.5 | 0.5 | ✓ |
| H2 | 3 | HM = 3 ✓ | 📄 1.0 | 3.0 | ✓ |
| H3 | 1 | LM = 1 ✓ | 📄 1.0 | 1.0 | ✓ |
| R1 | 4 | HH = 4 ✓ | 📄 1.0 | 4.0 | ✓ |

Sum: 3.0+3.0+1.4+3.0+1.0+1.4+0.7+1.0+0.5+3.0+1.0+4.0 = **23.0**. The stage states 23.0.
Arithmetic PASS.

Classification: 23 sits in the 12-24 band = MODEST MOAT DEVELOPMENT. The stage states MODEST
and `em_classification: "MODEST"` matches the permitted value set. The stage also states that
23 falls below the EM ≥ 25 UA-multiplier qualifier, which is the operator ruling of
20-Aug-2026 applied as written (bands ABSOLUTE, no rescale, ceiling 92). PASS.

I1/I2 contribution stated separately, as the same operator ruling requires: "I1/I2
contribution: 0.0 points (0 of 23 rows)", with the explicit note that this name reaches no
threshold via I1/I2 and belongs on the review-checkpoint EXCLUSION list. That is exactly what
the checkpoint was built to collect. PASS.

## 2.3 Evidence-tier discipline

Verifier rule 3's named finding trigger is a 🎙️-only category scoring as if 📄. I checked
every 1.0-multiplier row for at least one genuine 📄 item under the stage's own taxonomy
(capex committed, patent filed, contract signed, plant under construction, product launched,
regulatory application submitted):

| Row at 1.0x | Documented item(s) found | Verdict |
|---|---|---|
| A1 | 48 US DMFs, 15 EU COS, 8 JDMFs, 6 ANDAs (filed/approved); oral API capacity commissioned | ✓ genuine 📄 |
| A2 | 24 patents (22 granted); Enmetazobactam USFDA/EMA/DCGI approvals; signed Russia contract | ✓ genuine 📄 |
| B1 | Rs 750cr capex committed; PLI approval letter with reference number; 19.79 acres purchased | ✓ genuine 📄 |
| G2 | FY24/FY25 audited WC and payable-days figures | ✓ genuine 📄 |
| H2 | Cipla partnership live; GARDP/Shionogi sub-license; Advanz operating; Russia contract signed | ✓ genuine 📄 |
| H3 | ZLD plant operating, technology described | ✓ 📄 (plant built), thin but within taxonomy |
| R1 | IFCI PLI approval letter ref. IFCI/CASD/DoP/PLI220715016; USFDA EIR/VAI status | ✓ genuine 📄 |

**No category scores 🎙️ evidence at the 📄 multiplier.** The trigger does not fire. PASS.

The discipline runs in the other direction too, which is the harder direction. A1's single
most attractive line, "one of only three USFDA approved facilities in the world", was demoted
to 🎙️ COMPANY-STATED and excluded from the documented tier because no third-party source in
the corpus corroborates it, then registered as an optionality item requiring live-web
verification. A3 records that the 7-ACA process technology is licensed from a partner who
also supplies the Chinese competitors, and scores the category 0 against the narrative rather
than crediting the largest capex in the company's history as a process moat. F2 reads the
injected B05 promise-delivery record (3 delivered, 6 partial, 3 missed, grade B) and scores
the execution-moat category 0, calling it evidence the opposite way. These are the "be
skeptical, most management plans never materialise" and "never be a cheerleader" rules working
as designed.

**FAIL (MINOR) — mixed-evidence rows are not treated by a consistent multiplier policy.**
Three rows whose summary type is 📄/🎙️ (A1, A2, B1) take the 📄 1.0 multiplier. Two rows whose
summary type also contains 📄 take the lower multiplier: E1 (🎙️/📄, contains an APPROVED
Italian ASMF and a FILED Brazilian CADIFA, both squarely 📄 under the taxonomy) takes 🎙️ 0.7,
and B2 (🔍/📄, contains a documented USFDA EIR/VAI) takes 🔍 0.5. The stage never states its
rule for mixed rows. Recomputed at the upper bound, with every mixed row taking 1.0: E1 0.7 →
1.0 (+0.3) and B2 1.0 → 2.0 (+1.0), giving **em_score 24.3**. Still MODEST (12-24 band), still
below the EM ≥ 25 UA qualifier. No band crosses, no downstream gate changes. The direction of
the inconsistency is conservative, which is why this is MINOR.

**FAIL (MINOR) — three evidence items carry no page anchor.** Stage 7 operating rule 3
requires "(AR p.__)" on every evidence item. F1's remuneration figure, G2's accounts-payable
days, and H3's ZLD plant are anchored to "AR BRSR section" and "AR narrative, environment
section" with no page. Two of the three feed scored rows (G2 = 1.0, H3 = 1.0). Verifier A owns
whether the numbers are real; my finding is that the anchor as written cannot be located by
page, which is the form the rule mandates.

## 2.4 Completionist guard

| Check | Stage | Verdict |
|---|---|---|
| Strong/Moderate count stated | "Count with Strong/Moderate evidence: 5" (R1, A1, A2, B1, H2) | PASS |
| Inside the 3-6 realistic base rate | 5, stated explicitly against the base rate | PASS |
| 12-or-more trigger examined | Not tripped on the active definition the block itself uses (active_categories = Strong/Moderate rows only) | PASS |
| Recount performed and stated in the mandated form | "📄 recount performed: 16 documented items across 7 categories (A1, A2, B1, G2, H2, H3, R1)" | PASS |
| Recount enumerated, not asserted | All 16 items listed by name | PASS |
| `evidence_mix.documented` agrees with the recount | 16 = 16 | PASS |
| active_categories[] agrees with the summary table | 5 rows, same IDs, same strengths | PASS |

The recount is the part of this framework most often faked, so I checked it item by item: PLI
letter and terms, EIR/VAI, 48 DMFs, 15 COS, 8 JDMFs, 6 ANDAs, 24 patents, three Enmetazobactam
approvals, Russia contract, 7-ACA capex, land acquisition, oral API capacity, Cipla, GARDP
sub-license, ZLD plant, FY25 WC/payables figures = 16 distinct items across exactly the 7
categories named. The count is real. PASS.

Note (MINOR, not a fail): the `completionist_recount` YAML field drops the 📄 glyph that
opens the mandated sentence. The report body carries it correctly, and the body is where the
rule applies.

## 2.5 Section completeness and the 2C arithmetic

| Section | Requirement | Verdict |
|---|---|---|
| 1A | Pipeline table with status, evidence type, launch, revenue potential, differentiation | PASS, 6 rows, all six columns |
| 1B | Diversification direction with evidence and timeline | PASS, 5 directions |
| 1C | Mix table: current %, expected % in 3 years, margin direction, profitability impact | PASS; forward column is NOT FOUND on most rows with the reason stated, which is compliance, not a gap |
| 2A | Capex table, 7 columns | PASS, 5 projects; flags the Rs 600cr → Rs 750cr overrun as unreconciled |
| 2B | Utilisation trajectory per facility | PASS, 3 facilities, one NOT FOUND |
| 2C | Capex x FAT = implied incremental revenue, arithmetic SHOWN | PASS-with-note |
| 2D | New geography/market entries | PASS, 6 geographies with evidence tier each |
| 4A/4B/4C | Approvals, policy tailwinds, moat assessment | PASS, all three present with amounts, duration, enrolment status |
| 5 | 23-row table, adjusted total, classification, I1/I2 stated separately | PASS |
| Optionality register | 4 columns, items scoring 0 or resting on 🎙️/🔍 only | PASS, 8 rows, correct population |
| 6A-6E | Timeline, risks, combined table, combined classification with full reasoning, output card | PASS, all five; 6D gives the full reasoning the framework demands rather than a one-line dismissal |

2C arithmetic re-derived: 750 + 150 + 90 = 990cr; FAT 921.93 ÷ 612.9 = 1.504x; 990 x 1.50 =
1,485cr; 1,485 ÷ 921.93 = 161.1%. Matches. The adjusted figure also checks: 390 x 1.50 = 585;
585 ÷ 921.93 = 63.5%. Both labelled 🔍 ANALYST INFERENCE. PASS on the "show the arithmetic"
requirement.

Two MINOR notes on 2C, neither a fail:
1. `capex_embedded_growth_pct: 161` carries the naive figure while the report body says the
   63% figure "should be preferred by any downstream stage that reads this number". The field
   spec says "from 2C" and the instruction says show the mechanical formula, so carrying 161
   is literal compliance. The risk is real anyway: a downstream stage reading the block and
   not the report gets 161, and the stage's own view is that 161 overstates by roughly 2.5x.
   Worth the operator's attention at Halt 1.
2. The 2C fixed-asset denominator (612.9cr, AR p.23) differs from the denominator Gate 0 used
   for M3 (Net Block 632.71cr, screener FY25). Recomputed on the Gate 0 figure: FAT 1.457x,
   naive implied revenue 1,442cr, 156% rather than 161%. No conclusion moves. A cross-stage
   inconsistency, both anchored.

## 2.6 Categories 21 and 22 (verifier rule 8)

| Check | Finding | Verdict |
|---|---|---|
| Category 21 (I1 TALENT ASYMMETRY) present | Yes, Family I, scored row in Section 5 | PASS |
| I1 above 0 only if BOTH legs evidenced, (b) leg carrying ≥1 📄 | Scored **0**. Leg (a) unevidenced (no traced inventor pedigree, no ex-DRDO/global-major concentration); leg (b) "entirely absent". The one remuneration data point (median non-KMP pay Rs 85,039) is explicitly rejected as not supporting an above-sector-norm claim | PASS |
| Category 22 (I2 CANNIBALIZATION BARRIER) present | Yes, scored row in Section 5 | PASS |
| I2 above 0 only if the named sacrifice is specific | Scored **0**. The stage answers the category's own question directly ("nothing, it would have to spend money and wait"), works through 7-ACA (capital and a PLI window, not a configuration) and Enmetazobactam (patent law, already captured under A2), and cites the category's own scoring rule for the zero | PASS |

Both categories were applied as written, including the trap each was built to catch. I1 was
not converted into a "strong team" score, and I2 was not converted into an execution-lead
score. Neither zero was reached by omission; both were reasoned to.

## 2.7 Emerging Moat tally

Rules checked: 37. Fails: 2 (both MINOR). Acceptance: 35/37 = **94.6%**.

Recomputed value: em_score upper bound **24.3** under a uniform mixed-row multiplier policy
(stage: 23.0). Classification MODEST holds on both. EM < 25 holds on both, so the UA-qualifier
gate is unaffected. **em_classification MODEST and combined assessment AVOID: I concur.**

---

# PART 3: VALUATION (B11) — NOT AUDITED

Deferred to phase 3 by the invocation scope. Stages 10 and 11 have not run; B10 and B11 do
not exist. The valuation framework documents (Master v3.7 Role 1, the Section 1B layer set
v3.3 through v3.10, FTTCP v2.3) were deliberately NOT loaded, per my instruction file's rule
that carrying them in phase-1 scope is dead context.

Verifier-C rules 4, 6, 7, 9, 10, 11, 12, 13 and 14 are therefore unexercised. The
`valuation`, `expectation_ledger` and `business_understanding_narrative` YAML sections are
marked pending, not passed. Nothing in this report should be read as clearance for any of
them. Specifically NOT checked and still owed at phase 3: growth-symmetry (Amendment 26.1-26.4),
the margin bridge, both tracks, the Hurdle Ratio, the Amendment 19 FV path, the Expectation
Ledger gates, the residual starter cap, the Section 1A matrix, and the stage-13 Business
Understanding Narrative.

---

# PART 4: CONSOLIDATED FINDINGS

| # | Sev | Stage | Location | Rule | Finding | Recomputed |
|---|---|---|---|---|---|---|
| 1 | MAJOR | B01 | block `history_downgrade` | Confidence ladder: 10+ yrs = full | Field says true; the report body says no downgrade, and 10 years is the full tier | false |
| 2 | MAJOR | B01 | E2 | Op. rule 5 + "change over 3 years" | 3 scored on a 1-year proxy the stage itself calls not a true 3-year trend; rule 5 was applied at E3/D4 but not here | E2 = 0, Block E = 10, core = 26 |
| 3 | MAJOR | B01 | M1 | Block F, "revenue CAGR ≥10%" | Undeclared FY23-25 window (17.67%) contradicts the scorecard's own C1 CAGR (4.97%); no window rule stated | M1 = 0, moats 1, moat_class THIN, moat 8, grand 37 |
| 4 | MINOR | B01 | A3 | ROE formula definition | FY17-FY20 excluded from the median with no authorising rule (the N/M escape is a CAGR edge rule) | Median still <12%, score 0 unchanged |
| 5 | MINOR | B01 | A3 | Rule 3, show every number | Five of six ROE values listed; FY24 = 9.92% omitted | Stated median 3.86% is correct |
| 6 | MINOR | B01 | Block B | FCF formula definition | B1 uses Data_Sheet CFO, B2/B3 use AR CFO for the same three years, unreconciled | Cum FCF -44.69 on one basis; B2/B3 = 0 either way |
| 7 | MINOR | B01 | M5 | Block F peer rule | Scored 1 on a partial 3-peer set while marking PEER DATA NEEDED; M7 applied the same rule correctly at 0 | M5 = 0, moat_score −1 |
| 8 | MINOR | B01 | D4 | Op. rule 5, "latest" | PASS-with-note. Scored 0 on absent FY26 data; FY25 audited 3.31x would score 5. Literally compliant and consistent with D1-D3 | Block D would be 10, core 34, still AVOID |
| 9 | MINOR | B01 | E4 | Basis consistency | PASS-with-note. Consolidated contingent liabilities over standalone net worth; flagged by the stage; framework silent on basis | Band unaffected, 1.11% vs 5% |
| 10 | MINOR | B07 | Section 5, E1 and B2 | Evidence multipliers | Mixed-evidence rows treated inconsistently; A1/A2/B1 at 1.0, E1 at 0.7 and B2 at 0.5 despite 📄 items; policy never stated | em_score upper bound 24.3, still MODEST, still <25 |
| 11 | MINOR | B07 | F1, G2, H3 | Op. rule 3, source anchors | Three evidence items anchored to "AR BRSR section" / "AR narrative" with no page number; two feed scored rows | No score effect |
| 12 | MINOR | B07 | 2C / block field | Field carriage | PASS-with-note. `capex_embedded_growth_pct: 161` is the naive figure; the stage's own preferred figure is 63 | 63% adjusted, 156% on the Gate 0 FAT denominator |
| 13 | MINOR | B07 | 2C | Cross-stage consistency | PASS-with-note. FAT denominator 612.9 (AR p.23) vs Gate 0's Net Block 632.71 (screener FY25) | 161% becomes 156% |
| 14 | MINOR | B07 | block `completionist_recount` | Mandated recount wording | PASS-with-note. YAML field drops the leading 📄; the report body carries it correctly | — |

No CRITICAL findings. Nothing I recomputed changes a classification, a combined assessment,
or a gate.

## What holds, and what the operator should carry to Halt 1

Both stages reach the right answer by the right route. Gate 0's AVOID survives every
recompute I ran, including the harsher ones: with E2 zeroed the core score falls to 26, and
the base matrix branch (Core <40 → AVOID) never depended on deal breaker 6 or on the
unverified FY2026 figures. B07's MODEST holds at both 23.0 and the 24.3 upper bound, and the
EM ≥ 25 UA qualifier fails on both. The combined AVOID is sound.

Three items to fix before this run goes further:
1. `history_downgrade: false` in the B01 block. Mechanical, and the block currently
   contradicts its own report.
2. Declare the M1 revenue-CAGR window, or accept THIN. The moat_class field is consumed
   verbatim by B07 Section 6C, so whichever reading wins should win explicitly.
3. Decide whether E2 scores 0 (rule 5, no 3-year data) or 3 (1-year proxy). The stage cannot
   apply rule 5 at E3 and D4 and waive it at E2 without saying why.

One item to watch rather than fix: `capex_embedded_growth_pct: 161` will be read by a later
stage that may never open the report where the stage explains that 63 is the defensible
number.

---

```yaml
stage: B12c
company: "ORCHPHARMA"
run_date: "2026-09-06"
model: claude-opus-4-8
status: complete
scope: "phase-1 (Gate 0 + Emerging Moat only); valuation audit deferred to phase 3"
gate0:
  rules_checked: 56
  fails:
    - "history_downgrade: true contradicts the 10-year full-confidence tier and the report body; correct value false"
    - "E2 scored 3 on a 1-year proxy for a 3-year metric; operating rule 5 directs N/A and 0 (applied at E3/D4, waived here)"
    - "M1 revenue CAGR uses an undeclared FY23-25 window (17.67%) contradicting the scorecard's own C1 CAGR (4.97%)"
    - "A3 median ROE excludes FY17-FY20 with no authorising rule; the N/M escape is a CAGR edge rule, not an ROE rule"
    - "A3 lists five of six ROE values; FY2024 = 9.92% omitted (stated median 3.86% is nonetheless correct)"
    - "Block B mixes CFO bases: B1 on Data_Sheet CFO, B2/B3 on AR CFO for the same FY23-FY25 years, unreconciled"
    - "M5 scored 1 on a partial 3-peer set while marked PEER DATA NEEDED; Block F rule directs 0 (applied correctly at M7)"
emoat:
  rules_checked: 37
  fails:
    - "Evidence multipliers inconsistent on mixed-evidence rows: A1/A2/B1 at 1.0x, E1 at 0.7x and B2 at 0.5x despite documented items in both; policy never stated"
    - "Three evidence items carry no page anchor (F1 remuneration, G2 payable days, H3 ZLD plant), against the mandatory (AR p.__) anchor rule; two feed scored rows"
valuation:
  rules_checked: 0
  fails: []
  status: "PENDING PHASE 3 - B10/B11 do not exist; valuation framework documents deliberately not loaded; verifier-C rules 4, 6, 7, 11, 12 unexercised"
expectation_ledger: {present: false, downside_row: false, all_rows_confirm_by: false, all_rows_metric_threshold: false, prob_in_range: false, decay_status_valid: false, off_ledger_credit: false, residual_pct_cmp: 0, residual_starter_cap_ok: true, fails: [], status: "PENDING PHASE 3 - not audited, not cleared"}
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: [], status: "PENDING PHASE 3 - stage 13 has not run"}
recomputed_destination_pe: ""
recomputed_decision: ""
recomputed_gate0_core_score: "29 stated / 26 if E2 rescored to 0"
recomputed_moat_class: "MODERATE stated / THIN if M1 is scored on the scorecard's own C1 revenue CAGR"
recomputed_em_score: "23.0 stated / 24.3 upper bound under a uniform mixed-row multiplier; MODEST and EM<25 hold on both"
findings:
  - {severity: "MAJOR", stage: "B01", location: "block field history_downgrade", claimed: "true", rule: "Data confidence: 10+ yrs = full, no downgrade", recomputed: "false", note: "YAML contradicts the report body; cannot lower AVOID, would be CRITICAL at any higher core score"}
  - {severity: "MAJOR", stage: "B01", location: "E2 promoter holding change", claimed: "score 3", rule: "operating rule 5, mark N/A and score 0 where the data point is not available", recomputed: "E2 = 0, Block E = 10, core = 26", note: "Stage itself labels it a 1-year proxy, NOT a true 3-year trend; rule 5 was applied at E3 and D4"}
  - {severity: "MAJOR", stage: "B01", location: "M1 pricing power", claimed: "score 3 on FY23-25 CAGR 17.67%", rule: "Block F M1, revenue CAGR >=10%, window unspecified", recomputed: "M1 = 0 on C1's 4.97%; moats 2 -> 1; moat_class MODERATE -> THIN; moat_score 11 -> 8; grand_total 40 -> 37", note: "Framework silent on window; silence obliges the stage to declare its choice, and the alternative flips a field B07 6C reprints"}
  - {severity: "MINOR", stage: "B01", location: "A3 median ROE", claimed: "FY17-FY20 excluded as N/M", rule: "ROE formula definition", recomputed: "median still <12%, score 0 unchanged", note: "Negative-endpoint N/M is a CAGR edge rule; no rule authorises dropping years from a median. Exclusion was disclosed"}
  - {severity: "MINOR", stage: "B01", location: "A3 value listing", claimed: "five values listed for a six-year median", rule: "operating rule 3, show every number extracted", recomputed: "FY2024 ROE = 9.92% omitted; stated median 3.86% verified correct", note: "Presentation defect only"}
  - {severity: "MINOR", stage: "B01", location: "Block B, B1 vs B2/B3", claimed: "CFO 18.34/125.99/19.22 at B1, 13.39/130.73/27.48 at B2/B3", rule: "FCF = CFO - capex, one basis", recomputed: "cumulative FCF -44.69 on the Data_Sheet basis; B2 and B3 score 0 on either", note: "Two CFO values for the same years in one block, unreconciled; likely standalone vs consolidated"}
  - {severity: "MINOR", stage: "B01", location: "M5 scale and dominance", claimed: "score 1 plus PEER DATA NEEDED", rule: "Block F preamble: missing peer data scores 0 and is marked PEER DATA NEEDED", recomputed: "M5 = 0, moat_score -1", note: "M7 applied the identical rule correctly at 0; internal inconsistency"}
  - {severity: "MINOR", stage: "B01", location: "D4 current ratio", claimed: "score 0, FY2026 NOT FOUND", rule: "operating rule 5", recomputed: "Block D would be 10 and core 34 on FY2025's audited 3.31x; still AVOID", note: "PASS-with-note, not a fail. Literally compliant and consistent with D1-D3 taking FY2026 as latest"}
  - {severity: "MINOR", stage: "B01", location: "E4 contingent liabilities", claimed: "1.11%", rule: "basis consistency", recomputed: "band unaffected", note: "PASS-with-note, not a fail. Consolidated note 45 over standalone net worth; flagged by the stage; framework silent on basis"}
  - {severity: "MINOR", stage: "B07", location: "Section 5, rows E1 and B2", claimed: "E1 at 0.7x, B2 at 0.5x while A1/A2/B1 mixed rows take 1.0x", rule: "evidence multipliers 📄 1.0 / 🎙️ 0.7 / 🔍 0.5", recomputed: "em_score upper bound 24.3", note: "No stated policy for mixed-evidence rows; error direction is conservative; MODEST and EM<25 hold on both readings"}
  - {severity: "MINOR", stage: "B07", location: "F1, G2, H3 evidence items", claimed: "anchored to 'AR BRSR section' / 'AR narrative, environment section'", rule: "operating rule 3, source anchors (AR p.__) on every evidence item", recomputed: "no score effect", note: "Anchor cannot be located by page; two of the three feed scored rows"}
  - {severity: "MINOR", stage: "B07", location: "block field capex_embedded_growth_pct", claimed: "161", rule: "Section 2C, field carries the instructed-formula figure", recomputed: "63% adjusted; 156% on the Gate 0 fixed-asset denominator", note: "PASS-with-note, not a fail. Literal compliance, but the stage's own preferred figure is 63 and a block-only reader never sees that"}
  - {severity: "MINOR", stage: "B07", location: "Section 2C fixed-asset turnover", claimed: "Net Fixed Assets 612.9 (AR p.23)", rule: "cross-stage consistency", recomputed: "Gate 0 M3 used Net Block 632.71 (screener FY25); FAT 1.50x vs 1.457x", note: "PASS-with-note, not a fail. Both anchored, no conclusion moves"}
  - {severity: "MINOR", stage: "B07", location: "block field completionist_recount", claimed: "recount line without the leading 📄", rule: "mandated wording '📄 recount performed: [n] documented items across [m] categories'", recomputed: "n/a", note: "PASS-with-note, not a fail. Report body carries the mandated form correctly"}
critical_count: 0
major_count: 3
minor_count: 11
acceptance_rate: 90
acceptance_detail: "gate0 49/56 = 87.5%; emoat 35/37 = 94.6%; combined 84/93 = 90.3%"
concur_gate0_classification: true
concur_em_classification: true
concur_combined_assessment: true
rework_triggered: false
```
