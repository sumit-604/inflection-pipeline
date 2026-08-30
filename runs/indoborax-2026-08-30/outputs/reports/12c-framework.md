# STAGE 12c — VERIFIER C: FRAMEWORK ADHERENCE (PHASE 1 SCOPE)
Company: Indo Borax & Chemicals Ltd (INDOBORAX) | Run date: 2026-08-30
Model: claude-opus-4-8 | Emits: B12c

SCOPE: Phase 1 only. Gate 0 (B01) and Emerging Moat (B07) adherence.
Valuation audit (B10/B11) deferred to phase 3; valuation section pending.
Rule sources in scope: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md.
Master Prompt / Section 1B / FTTCP NOT loaded (out of scope this phase).

Method: I re-derived every stated score from the stated inputs using the
stated thresholds. I do not re-verify that the raw numbers exist in the
source PDFs. That is Verifier A's non-overridable domain. I audit rule
application only.

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### Block A — Return on Capital (rule: prompts/01 lines 55-73)

| Rule | Stated inputs | Threshold applied | Score | Re-derived | Verdict |
|---|---|---|---|---|---|
| A1 Median ROCE | 10 values, median (17.81+19.62)/2 = 18.72% | 15-19.9% = 3 | 3 | median 18.72%, band 15-19.9 → 3 | PASS |
| A2 Min single-yr ROCE | 12.25% (FY17) | 12-14.9% = 3 | 3 | 12.25 → band 12-14.9 → 3 | PASS |
| A3 Median ROE | 10 values, median (13.93+14.22)/2 = 14.08% | 12-14.9% = 2 | 2 | median 14.08 → band 12-14.9 → 2 | PASS |
| A4 ROCE trend | FY26 17.13 ≥ FY17 12.25 | latest ≥ earliest = 5 | 5 | 17.13 ≥ 12.25 → 5 | PASS |

Block A total 13/20 confirmed. A3 correctly rejected the AR Note 45
"Return on Equity Ratio" (15.50/13.05) as a copy-paste artifact of the EPS
figures and used independently computed ROE. This is the correct
application of the "confirm it exists / never fill with a suspect figure"
grounding rule (lines 20-23).

NOTE (MINOR, see finding F-01): the formula rule (lines 29-31) states "If
the data source provides its own ROCE (screener.in does), use the source's
figure ... compute only when absent." FY17-FY24 ROCE was computed via the
Net Worth + Borrowings convention rather than taken from a screener ROCE
row. The report justifies this by the missing current/non-current
liability split. Whether a screener ROCE row was in the provided extract is
a source-existence question (Verifier A domain), so this stands as a MINOR
adherence note, not a fail. Band impact untested but A1/A2 sit mid-band
(18.72, 12.25), so a small revision is unlikely to move either score.

### Block B — Cash Generation Quality (rule: lines 62-69)

| Rule | Re-derived | Score | Verdict |
|---|---|---|---|
| B1 Cum CFO/PAT | 189.36/308.96 = 0.613 → 0.50-0.69 | 1 | PASS (both cumulative sums recomputed and tie) |
| B2 FCF-positive proportion | 1/2 = 50% → 50-74 | 2 | PASS (rule applied as written; n=2 flagged) |
| B3 Cum FCF/PAT | -24.34/92.78 = -0.262 → negative | 0 | PASS |
| B4 Change WC days | 66.27 - 119.61 = -53.34 → >5 day decrease | 5 | PASS |

Block B total 8/20 confirmed. CFO sum (189.36) and PAT sum (308.96)
independently re-added and match. B2 and B4 rest on a 2-year window
(capex/payables absent pre-FY25); the report applies the mechanical band
and flags the thin window. Rule permits "use whatever history is
available" (lines 25-26), so this is compliant.

### Block C — Growth (rule: lines 71-75)

| Rule | Re-derived | Score | Verdict |
|---|---|---|---|
| C1 Revenue CAGR | (215.38/66.59)^(1/9)-1 = 13.93% → 10-14.9 | 3 | PASS |
| C2 PAT CAGR | (50.27/7.99)^(1/9)-1 = 22.68% → ≥20 | 5 | PASS |
| C3 Positive YoY proportion | 6/9 = 66.7% → 50-74 | 1 | PASS |
| C4 PAT-Rev CAGR | 22.67-13.93 = +8.74pp → ≥+3 | 5 | PASS |

Block C total 14/20 confirmed. CAGR edge rules (lines 44-51) honoured: no
CAGR endpoint is negative or zero (revenue 66.59→215.38, PAT 7.99→50.27),
so no N/M mark is required and none was forced. No loss-to-profit swing
across the window (FY17 PAT positive), so the data_notes swing rule
correctly did not fire. Deal-breaker 7 (revenue decline majority) correctly
not triggered (3/9 = 33%).

### Block D — Balance Sheet Strength (rule: lines 77-87)

| Rule | Re-derived | Score | Verdict |
|---|---|---|---|
| D1 Net Debt/EBITDA | net cash | 5 | PASS |
| D2 Interest coverage | 6587.57/6.61 = 997x → ≥10x | 5 | PASS |
| D3 Debt/Equity | 142.99/38455.18 = 0.0037 → <0.1 | 5 | PASS |
| D4 Current ratio | 31202.60/1556.13 = 20.05x → ≥2.0 | 5 | PASS |

Block D total 20/20 confirmed.

### Block E — Shareholder Alignment (rule: lines 89-96)

| Rule | Re-derived | Score | Verdict |
|---|---|---|---|
| E1 Promoter holding | 38.41% → 30-39.9 | 1 | PASS |
| E2 3-yr change | 38.41 - 52.07 = -13.66pp → decreased >3% | 0 | PASS (Sep-2023 used as best-available proxy per "use available history"; score band-invariant) |
| E3 Pledge | 100% → >15% | 0 | PASS |
| E4 Contingent liab/NW | 0.0165/384.55 = 0.0043% → <5% | 5 | PASS |

Block E total 6/20 confirmed. E1 did not apply the "professionally managed
3 if FII+DII>50%" alternative; promoter is identifiable (Zenrock 38.41%),
so the base band is correct, not the professional-managed path.

### Block F — Quantitative Moat (rule: lines 98-139)

| Test | Re-derived | Score | Verdict |
|---|---|---|---|
| M1 Pricing power | margin -1.1pp, rev CAGR 6.11% <10% → else | 0 | PASS |
| M2 Cost advantage | no peer → PEER DATA NEEDED | 0 | PASS |
| M3 Capital efficiency | FAT 4.52x, ROCE 17.13% → FAT>2 & ROCE>15 | 3 | PASS |
| M4 Customer stickiness | 3 decline years → 3+ | 0 | PASS |
| M5 Scale/dominance | no peer mcap/margin → PDN | 0 | PASS |
| M6 Technology/R&D | no R&D dept, R&D/Rev 0% | 0 | PASS |
| M7 Regulatory/licence | player count not quantified → PDN | 0 | PASS (see F-02) |
| M8 Distribution | none quantified | 0 | PASS |
| M9 Brand | no peer GM median → PDN | 0 | PASS |
| M10 Switching costs | overall growth, 2+ decline yrs | 1 | PASS |
| M11 Network effects | latest 3yr -1.45% < prior 25.02% | 0 | PASS |
| M12 Negative WC | WC days >45 both years | 0 | PASS |

Block F total 4/60 confirmed. Moats present (≥3): M3 only → moats_confirmed
1 → THIN (rule line 138: "1 = THIN"). Correct.

NOTE (MINOR, F-02): M7. The company is the sole India manufacturer of
IP-grade boric acid with FDA/BIS licence (a documented fact, not a guess).
The M7 top band asks for "≤5 listed players in the regulated segment AND
margin stable ±3pp." "Sole manufacturer" plus margin within ±3pp could
arguably support a non-zero score. The report scored 0 PEER DATA NEEDED and
self-flagged it as likely under-scored, invoking "never guess peer figures"
(line 101). The conservative reading is rule-defensible. Materiality is
low: even M7=5 lifts moats_confirmed to 2 → MODERATE, which with Core 61
still yields matrix GOOD, still capped to AVERAGE by deal-breaker 5.
Classification is unchanged. MINOR.

### Classification and overrides (rule: lines 141-160)

- Data confidence: 10 years → "10+ yrs full", no history downgrade. Correct
  (line 143). history_downgrade=false confirmed.
- Core score 13+8+14+20+6 = 61 confirmed. Grand total 61+4 = 65 confirmed.
- Matrix (line 149): Core 61 (60-79) + THIN → "Core 60-79 + else = GOOD".
  Pre-override GOOD confirmed.
- Deal-breaker sweep (all 9 checked in the report):
  1 Block A<8 → A=13, not triggered. Correct.
  2 Block B<8 → B=8, exactly at threshold, NOT below → not triggered.
    Correct (the report explicitly notes "not below it").
  3 Median ROCE<10% → 18.72%, not triggered. Correct.
  4 Cum CFO/PAT<0.50 → 0.613, not triggered. Correct.
  5 Pledge>15% → 100%, TRIGGERED → max AVERAGE. Correct application.
  6 ND/EBITDA>3x AND IC<3x → net cash, IC 997x, not triggered. Correct.
  7 Revenue decline majority → 3/9, not triggered. Correct.
  8 PAT negative last 3 yrs → all positive, not triggered. Correct.
  9 History<3 yrs → 10 yrs, not triggered. Correct.
- Final classification AVERAGE (matrix GOOD capped by deal-breaker 5).
  Correct. FLAG-GATE0 raised carrying the pre-cap GOOD and the pledge
  context, per the flags rule (lines 176-178). Compliant.

GATE 0 VERDICT: fully compliant. Every block score, the classification
matrix, the deal-breaker sweep, and the CAGR edge rules re-derive to the
reported values. Two MINOR adherence notes (F-01 ROCE source-figure rule,
F-02 M7 conservative zero); neither changes any score band or the AVERAGE
classification.

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### Category completeness (rule: prompts/07 lines 65-181, Section 5 line 174)

All 22 categories plus R1 = 23 scored rows present in the Section 5 table:
A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, I1-I2, R1. Every
non-scoring category carries "NO EVIDENCE FOUND" (or a documented negative
finding for F1/F2). No category omitted, none force-fit. PASS (rubric 3;
stage-7 rule 8 — I1 and I2 both present).

### Evidence multipliers and score total (rule: lines 170-174)

| Cat | Raw (L×I) | Type | Multiplier | Adjusted | Re-check |
|---|---|---|---|---|---|
| B1 | 2 (M/M) | 🎙️ | 0.7 | 1.4 | 2×0.7=1.4 ✓ |
| C1 | 1 (L/M) | 🎙️ | 0.7 | 0.7 | 1×0.7=0.7 ✓ |
| G1 | 3 (H/M) | 📄 | 1.0 | 3.0 | 3×1.0=3.0 ✓ |
| all others | 0 | — | — | 0 | ✓ |

Total 1.4+0.7+3.0 = 5.1 confirmed. Likelihood×impact matrix values
(MM=2, LM=1, HM=3) match the stated matrix (line 172). em_score 5.1 →
band <12 → NO MEANINGFUL EMERGING MOAT / YAML "NONE" (line 175). Correct.
The <12 band and the "EM ≥25" UA qualifier are applied without rescale, per
the 20-Aug-2026 absolute-thresholds ruling (lines 11-18, 179-181). PASS.

### Evidence-tier discipline (rubric 3)

- B1 (🎙️) and C1 (🎙️) both take the 0.7 multiplier. Neither 🎙️-only
  category is scored as if 📄. PASS.
- G1 takes 📄 1.0. See F-03 (MINOR): the documented leg is the static
  balance-sheet cash (zero debt, ~Rs 130 cr investment rise); the emerging
  moat value (deployment into value-creating capex) is 🎙️ forward intent,
  which the report itself flags as unproven. Treating the war-chest
  existence as 📄 is defensible; the forward-moat leg is not documented.
  Low materiality (does not cross any band). MINOR.

### I1 / I2 discipline (stage-7 rule 8; lines 122-153)

- I1 Talent asymmetry: scored 0. Report correctly rejects a single senior
  hire as "a class of person of unusual capability" (leg a fails) and finds
  no competitor-economics arithmetic (leg b fails). Framework scores this
  "strong team" narrative 0 by design (line 137). Correct — 0 is compliant;
  the rule only gates scores ABOVE 0.
- I2 Cannibalization barrier: scored 0. Report finds no named, specific
  sacrifice; stickiness is classified as execution lead, which the
  framework explicitly scores 0 (lines 148-150). Correct.
- I1/I2 contribution stated separately: "I1/I2 contribution: 0 of 5.1"
  (line 297-299), feeding the operator review checkpoint (line 181). PASS.

### Completionist guard (rule: lines 42-46, 158)

"📄 recount performed: 4 documented items across 2 categories" line present
(report line 221; YAML completionist_recount). 3 active categories, 4 📄
items — inside the 3-6 base rate, no inflation, no guard correction needed.
PASS.

### Combined assessment with B01 (rule: Section 6C/6D, lines 198-210; rubric 3)

6C table pulls the injected Gate 0 block correctly: Core 61, moats_confirmed
1, moat_score 4/60, classification AVERAGE. 6D combined = AVERAGE. The
report correctly identifies this as NOT a HIGH POTENTIAL / TURNAROUND
transition setup (backward AVERAGE + forward NONE, not paired with a
STRENGTHENING/EXPANSION forward score). combined_reasoning consistent.
capex_embedded_growth_pct = 0 correctly derived (2C: zero capex under
execution × any FAT = 0). PASS.

NOTE (MINOR, F-04): active_categories in the YAML lists G1 as strength
"Moderate", but the Section 3 summary band table records "Moderate = 0" and
places all three surfaced rows (B1, C1, G1) in "Weak-Moderate = 3". The
framework says active_categories carries "only Strong/Moderate rows"
(line 227). Strictly, no row is Strong or Moderate, so either the label on
G1 or the band table is imprecise. Surfacing the top-3 Weak-Moderate rows
as the active set is useful and honest; the label mismatch is
presentational. MINOR.

EMERGING MOAT VERDICT: compliant. All 23 categories addressed, multipliers
and the 5.1 total re-derive exactly, I1/I2 correctly zero with the
contribution stated, the completionist recount is present and honest, and
the combined-with-B01 assessment uses the injected Gate 0 block correctly.
Two MINOR notes (F-03 G1 tier, F-04 active_categories label); neither moves
em_score, the band, or the combined AVERAGE.

═══════════════════════════════════════════════════════════════════
## PART 3 — VALUATION (B11)
═══════════════════════════════════════════════════════════════════

PENDING — PHASE 3. B10/B11 do not exist this phase; not audited. The
valuation framework docs (Master v3.6 Role 1, Section 1B layer set, FTTCP
v2.1) were deliberately not loaded, per phase-1 scope.

═══════════════════════════════════════════════════════════════════
## SUMMARY
═══════════════════════════════════════════════════════════════════

No CRITICAL, no MAJOR. Four MINOR adherence notes, all low-materiality;
none changes a score band, the Gate 0 AVERAGE classification, the em_score,
or the combined assessment. Both stages applied their frameworks as
written. Recomputed destination PE and decision: not in scope this phase
(valuation deferred); Gate 0 classification AVERAGE and Emerging Moat NONE
both concur with the makers' outputs.

Findings:
- F-01 (MINOR, B01 Block A): FY17-FY24 ROCE computed, not taken from a
  screener ROCE row, where the formula note says screener provides one.
  Transparently justified; source-existence is Verifier A's domain.
- F-02 (MINOR, B01 M7): licence test scored 0 PEER DATA NEEDED though "sole
  India manufacturer" is a documented fact; conservative, self-flagged,
  classification-invariant.
- F-03 (MINOR, B07 G1): 📄 1.0 multiplier on a war chest whose forward-moat
  (deployment) leg is 🎙️; documented leg is static cash only.
- F-04 (MINOR, B07 active_categories): G1 labelled "Moderate" in YAML vs
  "Weak-Moderate / Moderate=0" in the Section 3 band table.

```yaml
stage: B12c
company: "INDOBORAX"
run_date: "2026-08-30"
model: claude-opus-4-8
status: complete
gate0:
  rules_checked: 39
  fails:
    - {severity: MINOR, rule: "Block A ROCE source-figure rule (prompts/01 lines 29-31)", note: "FY17-FY24 ROCE computed via Net Worth+Borrowings rather than screener's own ROCE; transparently justified by missing CE split; band-invariant; source existence is Verifier A domain"}
    - {severity: MINOR, rule: "M7 regulatory/licence (prompts/01 lines 118-120)", note: "scored 0 PEER DATA NEEDED though 'sole India manufacturer' documented; conservative per 'never guess'; classification-invariant (deal-breaker 5 caps to AVERAGE regardless)"}
emoat:
  rules_checked: 33
  fails:
    - {severity: MINOR, rule: "Evidence-tier discipline G1 (prompts/07 lines 170-174, rubric 3)", note: "G1 uses 1.0x documented multiplier; the emerging/forward-moat leg (capex deployment) is management-claim only; documented leg is static cash; low materiality, no band change"}
    - {severity: MINOR, rule: "active_categories composition (prompts/07 line 227)", note: "G1 labelled 'Moderate' in YAML vs Section 3 band table 'Moderate=0 / Weak-Moderate=3'; presentational inconsistency; rule expects Strong/Moderate rows only"}
valuation: pending-phase-3
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: []}  # not in phase-1 scope; stage 13 not audited this phase
recomputed_destination_pe: ""   # not in scope this phase (no valuation)
recomputed_decision: ""         # concur: Gate 0 AVERAGE, Emerging Moat NONE
findings:
  - {severity: MINOR, location: "B01 Block A (01-gate0.md lines 30-73)", description: "FY17-FY24 ROCE computed via Net Worth+Borrowings convention rather than a screener-supplied ROCE figure; formula note says screener provides ROCE. Transparently justified; band-invariant; source existence is Verifier A's domain."}
  - {severity: MINOR, location: "B01 M7 (01-gate0.md lines 282-287)", description: "Regulatory/licence test scored 0 PEER DATA NEEDED though the sole-India-manufacturer FDA/BIS position is documented. Conservative and rule-defensible; self-flagged as likely under-scored; classification unchanged (deal-breaker 5 caps to AVERAGE)."}
  - {severity: MINOR, location: "B07 G1 scorecard (07-emoat.md lines 287, 423)", description: "War chest scored with 1.0x documented multiplier; documented leg is static balance-sheet cash, while the emerging-moat value (deployment into value-creating capex) rests on management claim. Defensible; does not cross any band."}
  - {severity: MINOR, location: "B07 active_categories (B07-emoat.yaml lines 14-17)", description: "G1 labelled strength 'Moderate' in YAML while the Section 3 summary band table records Moderate=0 and places B1/C1/G1 in Weak-Moderate=3. Framework expects Strong/Moderate rows only. Presentational inconsistency."}
critical_count: 0
major_count: 0
minor_count: 4
acceptance_rate: 94    # (72 checked - 4 minor soft-fails) / 72 across gate0+emoat
```
