# VERIFIER C — FRAMEWORK ADHERENCE AUDIT (B12c)
Company: UFBL (United Foodbrands Ltd, erstwhile Barbeque Nation Hospitality Ltd)
Run date: 2026-08-05 | Model: claude-opus-4-8 | Stage: B12c
Scope: PHASE 1 ONLY — Gate 0 (B01) and Emerging Moat (B07) framework compliance.
Valuation adherence (B11/B10) is DEFERRED TO PHASE 3 (those reports do not yet
exist); the valuation section of the YAML block is left pending.

## SOURCES OF THE "FRAMEWORK AS WRITTEN"

The task pointed me to frameworks/Master_Project_Prompt_v3.3.md for the Gate 0
scorecard tables and the 20-category moat scan. That file contains only Roles 1-3
(valuation, thesis, devil's advocate) plus the Section 1B valuation machinery; it
does NOT contain the Gate 0 block point-allocations, the deal-breaker table, the
data-length/history-downgrade rule, the 12-test moat block, or the 20-category
emerging-moat scan rules. Per CLAUDE.md ("prompts/ stage instructions, single
source of truth"), the authoritative, as-written scoring rules for these two
stages live in:
- prompts/01-gate-0-pipeline.md (Blocks A-F point allocations, CAGR edge rules,
  classification matrix, 9 deal-breakers, data-confidence/history-downgrade rule)
- prompts/07-emerging-moat-pipeline.md (evidence taxonomy, completionist guard,
  20-category + R1 scan, Section 5 scoring method and classification bands, 6D
  combined-assessment taxonomy)

I audited B01 and B07 against those authoritative rule texts. The Section 1B
Amendments and the v3.5.1 Reconciliation are valuation-only (Pillar 1 routes,
UA ordering, Hurdle Ratio) and are Phase-3 material; they contain nothing that
governs Gate 0 or the emerging-moat scan, so they are not scored here.

Framework-availability note (MINOR, process, not scored against B01/B07): the
{{FRAMEWORK_DOCS}} pointer for this run misattributes the Gate 0 and 20-category
tables to Master v3.3. The tables were located in the stage prompts. No adherence
finding turns on this; recorded for the orchestrator.

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) COMPLIANCE
═══════════════════════════════════════════════════════════════════

Re-derivation uses B01's own stated inputs (Verifier A owns whether those inputs
match the source PDFs; I audit only rule application on the inputs as stated).

### Block A — Return on Capital (rule 01-gate0 lines 56-60)

| Line | Stated input | Rule band | Correct score | B01 score | Verdict |
|---|---|---|---|---|---|
| A1 Median ROCE | 3.25% (median 4.85/1.64) | <10 = 0 | 0 | 0 | PASS |
| A2 Min single-yr ROCE | 1.64% | <8 = 0 | 0 | 0 | PASS |
| A3 Median ROE | -7.75% (5th/6th of 10 sorted) | <12 = 0 | 0 | 0 | PASS |
| A4 ROCE trend | 4.85→1.64, -3.21pp | decline 3-5pp = 1 | 1 | 1 | PASS |

A3 sort re-verified: {-72.42,-47.09,-27.76,-17.57,-8.13,-7.36,-3.97,-3.38,4.33,
6.14}; mean of 5th/6th = (-8.13-7.36)/2 = -7.745%. Correct.
A4 uses FY25 as the "earliest" leg because ROCE is computable only for FY25/FY26
(documented data constraint). Acceptable adaptation of "latest vs earliest" given
the data; transparently flagged. **Block A = 1/20. PASS.**

### Block B — Cash Generation (rule 01-gate0 lines 63-69)

| Line | Stated input | Rule band | Correct | B01 | Verdict |
|---|---|---|---|---|---|
| B1 Cum CFO/PAT | negative (1477.20/-266.92) | <0.50 = 0 | 0 | 0 | PASS |
| B2 FCF-positive proportion | 2/2 = 100% | 100% = 5 | 5 | 5 | PASS (see note) |
| B3 Cum FCF/PAT | negative (204.33/-86.92) | <0.20 or neg = 0 | 0 | 0 | PASS |
| B4 Change WC Days | +2.06→-25.19, -27.25d | decreased >5d = 5 | 5 | 5 | PASS |

B2 note (MINOR): the 100%→5 mapping is literally the rule, but the sample is 2 of
10 years (FCF computable only FY25/FY26). Rule 6 sets a 3-year minimum for the
scorecard as a whole; B2/B3/B4/A4 rest on a 2-year window. This is a data
constraint, transparently disclosed, and applied as written — not a scoring
misapplication. Recorded as a note. **Block B = 10/20. PASS.**

### Block C — Growth (rule 01-gate0 lines 72-75)

| Line | Stated input | Rule band | Correct | B01 | Verdict |
|---|---|---|---|---|---|
| C1 Revenue CAGR | 11.47% | 10-14.9 = 3 | 3 | 3 | PASS |
| C2 PAT CAGR | N/M (neg endpoint) | neg/N/M = 0 | 0 | 0 | PASS |
| C3 Positive YoY prop | 7/9 = 77.8% | 75-99 = 3 | 3 | 3 | PASS |
| C4 PAT−Rev CAGR | N/M | C4=0 per edge rule | 0 | 0 | PASS |

C4 correctly applies the CAGR edge rule (01-gate0 line 52: "For C4 when PAT CAGR
is N/M, score C4 = 0"). **Block C = 6/20. PASS.**

### Block D — Balance Sheet (rule 01-gate0 lines 78-87)

| Line | Stated input | Rule band | Correct | B01 | Verdict |
|---|---|---|---|---|---|
| D1 ND/EBITDA | 4.13x | >3x = 0 | 0 | 0 | PASS |
| D2 Interest Coverage | 0.21x | <1.5 = 0 | 0 | 0 | PASS |
| D3 Debt/Equity | 2.85x | >1.5 = 0 | 0 | 0 | PASS |
| D4 Current Ratio | 0.42x | <1.0 = 0 | 0 | 0 | PASS |

**Block D = 0/20. PASS.**

### Block E — Shareholder Alignment (rule 01-gate0 lines 90-96)

| Line | Stated input | Rule band | Correct | B01 | Verdict |
|---|---|---|---|---|---|
| E1 Promoter holding | 32.7% | 30-39.9 = 1 | 1 | 1 | PASS |
| E2 Promoter Δ 3yr | N/A | no data → 0 | 0 | 0 | PASS |
| E3 Promoter pledge | N/A | no data → 0 | 0 | 0 | PASS |
| **E4 Cont. liab/NW** | **26.17%** | **15-30 = 1** | **1** | **3** | **FAIL** |

**FINDING F-G1 (MAJOR).** E4 = contingent liabilities Rs 97.02cr ÷ net worth
Rs 370.86cr = 26.17%. Rule E4 bands (01-gate0 line 95-96): `<5%=5 | 5-15=3 |
15-30=1 | >30=0`. 26.17% is in the 15-30 band → **score 1**. B01 wrote "15-30%
band → Score 3" (report line 131) — it named the correct band but assigned the
neighbouring band's score (3 belongs to 5-15). Correct E4 = 1, not 3.
- Block E recomputes: 1+0+0+1 = **2/20** (B01 stated 4/20).
- Core Score recomputes: 1+10+6+0+2 = **19/100** (B01 stated 21/100).
- Classification impact: NONE. 19 is still <40 → AVOID; deal-breaker #6 also
  independently forces AVOID. Decision survives, so MAJOR not CRITICAL.

### Block F — Quantitative Moat, 12 tests (rule 01-gate0 lines 103-136)

| Test | Stated input | Rule outcome | Correct | B01 | Verdict |
|---|---|---|---|---|---|
| M1 Pricing power | mgn -6.25pp, CAGR 7.93% | outside all bands = 0 | 0 | 0 | PASS |
| M2 Cost adv | no peer data | PEER DATA NEEDED = 0 | 0 | 0 | PASS |
| M3 Capital eff | FAT 1.15x, ROCE 1.64% | ROCE<12 → 0 | 0 | 0 | PASS |
| M4 Stickiness | 2 decline yrs, CAGR+ | 2 decline, CAGR+ = 1 | 1 | 1 | PASS |
| M5 Scale | no peer rank | PEER DATA NEEDED = 0 | 0 | 0 | PASS |
| M6 Tech/R&D | none | 0 | 0 | 0 | PASS |
| M7 Regulatory | unregulated | unregulated = 0 | 0 | 0 | PASS |
| M8 Distribution | 236 outlets, 1 snapshot | mentioned unquant. = 1 | 1 | 1 | PASS |
| M9 Brand | no peer data | PEER DATA NEEDED = 0 | 0 | 0 | PASS |
| M10 Switching | growth+, 2 decline yrs | overall growth, 2+ = 1 | 1 | 1 | PASS |
| M11 Network | insufficient/distorted | conservative 0 | 0 | 0 | PASS |
| M12 Neg WC/Float | FY25 +2.06, FY26 -25.19 | ambiguous (see note) | 1-3 | 3 | PASS-w/note |

**M12 note (MINOR).** Rule M12: `negative in majority of years = 5 | 0-15 days
consistently = 3 | 15-45 = 1 | >45 = 0`. On the 2-year sample the two readings
straddle bands: +2.06 (0-15 magnitude) and -25.19 (15-45 magnitude); "negative in
majority" is not met (1 of 2). B01 scored 3 on the average magnitude (-11.57,
inside 0-15). A stricter reading ("not consistently 0-15") gives 1. The rule does
not specify the 2-year case; B01 chose transparently and conservatively relative
to the 5 it declined to claim. If M12 were 1, it would fall below the ≥3 "present"
threshold → moats_confirmed 0 and moat_class NONE (not THIN). This does not affect
the AVOID classification (Core<40 and deal-breaker #6 govern). Flagged MINOR, not
overturned. **Moat score 6/60, moats_confirmed 1, moat_class THIN — arithmetic
correct; M12 borderline noted.**

### Classification, data-confidence, deal-breakers

- **Data length / history_downgrade (task-flagged check): PASS.** 10 years of P&L/
  CFO history → "10+ yrs full" tier; history_downgrade=false is correct. B01
  correctly keeps the metric-level computability gaps (ROCE/WC/FCF only FY25-26)
  OUT of history_downgrade and routes them to a data-note + FLAG-GATE0 instead.
  The downgrade tier is reserved for the 3-4yr LIMITED data-length case; it is NOT
  conflated with the COVID trough / recovery / Ind-AS-116 depressors. This is
  exactly the rule as written (01-gate0 lines 144-160). Clean.
- **Classification matrix: PASS.** Core 21 (or corrected 19) <40 → AVOID.
- **Deal-breakers: PASS.** Triggered #1 (Block A 1<8→GOOD cap), #3 (median ROCE
  3.25%<10%→AVERAGE cap), #4 (cum CFO/PAT neg<0.50→AVERAGE cap), #6 (ND/EBITDA
  4.13x>3x AND IC 0.21x<3x→AVOID), #8 (PAT neg in last 3 yrs→AVERAGE cap). Not
  triggered #2/#5/#7/#9 correctly justified. Most-restrictive = #6 AVOID.
  Every trigger states the driving years as the rule requires (01-gate0 line 155).

**Gate 0 verdict: one MAJOR (E4 mis-band), two MINOR notes (B2 2-yr sample, M12
borderline). Classification AVOID is correct and robust. Corrected Core = 19/100
(cosmetic; no decision change).**

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) COMPLIANCE
═══════════════════════════════════════════════════════════════════

Audited against prompts/07-emerging-moat-pipeline.md (evidence taxonomy line 18-22;
completionist guard line 31-36; Section 5 scoring line 126-132; 6D taxonomy).

### Coverage of the 21 categories — PASS

All 20 categories (A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3) plus
R1 are addressed with evidence tables or explicit NO EVIDENCE FOUND, and all 21
rows appear in the Section 5 scorecard. C1/D1 are explicitly folded into D2 with a
no-double-credit rationale (correct application of the taxonomy). No forced fits.

### Completionist base-rate check (task-flagged) — PASS

Base rate is 3-6 categories (07 line 31). B07 finds 3 active (A4, D2, E1) and
runs the required "📄 recount performed: 10 documented items across 3 active
categories" line. 3 active is inside the base rate — this is the guard working
correctly (the guard catches OVER-counting; a disciplined 3-active read is not
inflated). Category count is honest. **No category-count inflation.**

### Evidence-tier consistency — PASS

No 🎙️-only category is scored as if 📄. Active categories A4/D2/E1 are all mixed
📄+🎙️. D2's "90% captive channel / structural moat" 🎙️ framing is explicitly
separated from the 📄 KPI series and the score is held to Moderate — correct
tier discipline. F2 (execution, 📄 from B05) is risk-flagged, not credited as a
positive moat. Correct.

### Section 5 scoring method — TWO FINDINGS

**FINDING F-E1 (CRITICAL) — non-framework "corroboration adjustment" inflates the
score across a classification boundary.**

The framework scoring method (07 line 127-130) is exactly: `raw = likelihood×impact
(HH=4, HM/MH=3, HL/MM/LH=2, ML/LM/LL=1, none=0), adjusted = raw × evidence
multiplier (📄 1.0, 🎙️ 0.7, 🔍 0.5)`. There is NO further adjustment permitted.

B07's own row-by-row adjusted total is stated correctly as **≈ 9.1**
(A3 0.7 + A4 2.55 + D2 2.55 + E1 1.7 + F2 1.0 + H1 0.6). B07 then adds a
fabricated step (report lines 391-396): "a modest continuity/corroboration
adjustment is applied per category (+1.5 each ...), bringing the adjusted total to
~14.7, rounded to 15." That +1.5 × 3 = +4.5 has no basis anywhere in the framework.

Consequence — it crosses a classification band:
- Framework bands (07 line 131-132): `≥40 EXPANSION | 25-39 STRENGTHENING |
  12-24 MODEST | <12 NO MEANINGFUL EMERGING MOAT`.
- Correct em_score = **9.1 → <12 → NO MEANINGFUL EMERGING MOAT (NONE)**.
- B07 reported em_score 15 → MODEST.

Robustness: even at the most generous strict-multiplier reading (treating every
mixed category as full 📄 1.0: A3 1.0 + A4 3.0 + D2 3.0 + E1 2.0 + F2 1.0 +
H1 1.0 = 11.0) the score is still <12 → NONE. Only the invented +4.5 lifts it
into MODEST. The classification flip is therefore entirely an artefact of a
non-framework step. **Recomputed em_score 9.1; em_classification NONE.**

Severity: CRITICAL. It is a fabricated scoring mechanism that flips a headline
pipeline classification band (NONE→MODEST) and feeds the 6D combined assessment
below. Note for the orchestrator: the Phase-3 valuation destination-PE impact is
NIL — both 9.1 and 15 are <25, so Pillar 3 (Growth Visibility) pays +0x either
way (Master v3.3 Pillar 3 table). The CRITICAL rests on the classification-band
flip and the combined-assessment routing, not on destination PE. (This is a
framework-judgment finding, not a source-fidelity/number-existence finding — the
9.1 vs 15 arithmetic itself is Verifier A's domain; my finding is that the
+1.5/category rule does not exist.)

**FINDING F-E2 (MINOR) — evidence multipliers outside the defined set.**

A4, D2, E1 use 0.85 and H1 uses 0.6. The framework multiplier set is the three
discrete values {📄 1.0, 🎙️ 0.7, 🔍 0.5}; 0.85 and 0.6 are interpolations the
framework does not define for mixed evidence. Mixed-evidence handling is a genuine
gap in the rule text, so this is imprecision rather than manipulation, and (per
the robustness check above) it does not change the <12 outcome. MINOR.

### 6D Combined assessment / taxonomy (task-flagged) — FINDING

**FINDING F-E3 (MAJOR) — combined assessment does not follow the taxonomy.**

B07 grades **combined_assessment: TURNAROUND**. Its own 6D text (report lines
472-477) states the matrix result first: "an AVOID backward paired with a MODEST
(not EXPANSION/STRENGTHENING) forward score does not meet the bar for TURNAROUND
— TURNAROUND requires a materially stronger emerging-moat signal than this scan
honestly supports." It then overrides that with qualitative narrative (SSSG
recovery, Q1 FY27 PAT) to grade TURNAROUND anyway. That is the report
contradicting the taxonomy it just applied.

With the corrected forward score (NONE, <12, per F-E1), the case is stronger still:
AVOID backward + NONE forward does not support TURNAROUND under any reading of the
6D matrix (07 line 155-159). Correct combined_assessment = **AVOID / not a
transition setup on the evidence** (a watch-for-inflection note is defensible in
narrative, but the taxonomy label should not read TURNAROUND). MAJOR: it changes
the headline routing label the synthesis consumes, though the ultimate human
decision is anchored by Gate 0 AVOID regardless.

### Sections 1-2, 4, optionality register — PASS

- 2C capex-embedded-growth method applied as written (committed capex 140 ×
  historical FAT 3.14 ÷ FY26 revenue 1339 = 32.8% → capex_embedded_growth_pct 33).
  Method-compliant; the underlying figures are Verifier A's domain.
- R1 (Section 4) correctly scored 0: GST tailwind is industry-wide and netted
  against GST-ITC/licensing headwinds — not a company-specific moat. Correct.
- Optionality register: 8 items, all watched-never-scored per line 146. Compliant.

**Emerging Moat verdict: one CRITICAL (invented +4.5 corroboration bump flips
NONE→MODEST), one MAJOR (6D TURNAROUND contradicts taxonomy), one MINOR
(multiplier interpolation). Recomputed em_score 9.1 → NONE; recomputed combined
assessment AVOID.**

═══════════════════════════════════════════════════════════════════
## PART 3 — VALUATION (B11/B10) — DEFERRED TO PHASE 3
═══════════════════════════════════════════════════════════════════

Not run. B10 and B11 do not exist for this run. The continuous-Pillar-1, FTTCP-
ROCE, single-credit, Pillar 2 offset, Pillar 3, UA/Amendment-3, dual-track,
Hurdle-Ratio, and SOM checks (Verifier C rule 4) are all pending Phase 3. The
valuation section of the YAML block is emitted empty with status
pending_phase_3.

═══════════════════════════════════════════════════════════════════
## SUMMARY
═══════════════════════════════════════════════════════════════════

| ID | Sev | Where | Finding | Recompute |
|---|---|---|---|---|
| F-E1 | CRITICAL | B07 §5, lines 391-396 | Non-framework "+1.5/category" bump lifts 9.1→15, flipping NONE→MODEST | em_score 9.1; class NONE |
| F-G1 | MAJOR | B01 Block E, line 131 | E4 26.17% is 15-30 band = score 1, scored 3 | Block E 2/20; Core 19 (still AVOID) |
| F-E3 | MAJOR | B07 §6D, lines 472-479 | Combined TURNAROUND contradicts taxonomy (and corrected NONE forward) | combined AVOID |
| F-E2 | MINOR | B07 §5 scorecard | Multipliers 0.85/0.6 not in defined {1.0,0.7,0.5} set | no outcome change |
| — | MINOR | B01 M12 | 2-yr sample band ambiguous; scored 3, could be 1 | no class change |
| — | MINOR | B01 B2 | 100%→5 on 2-of-10-yr sample (as written, flagged) | no change |

Clean, correctly-applied rules affirmed: Gate 0 Blocks A-D, deal-breaker set,
classification matrix, and — specifically per task — the history_downgrade=false
call (data-length rule honoured, not conflated with trough/recovery depressors);
Emerging Moat 21-category coverage, completionist base-rate (no category
inflation), evidence-tier discipline, and optionality register.

Decision robustness: Gate 0 classification AVOID is unaffected by F-G1 (Core
19 still <40; deal-breaker #6 independently AVOID). The two emerging-moat findings
do not move the Phase-3 destination PE (EM <25 → +0x Pillar 3 either way) but they
do flip the emerging-moat classification (NONE not MODEST) and the combined
routing label (AVOID not TURNAROUND) that synthesis consumes.

acceptance_rate = 42/46 rules passed = 91.3%. Above the 60% REWORK floor. One
CRITICAL is present (F-E1); per Stage 12 rules a Verifier C CRITICAL is flagged
for the orchestrator/synthesis but is not itself an automatic REWORK trigger
(only a Verifier A CRITICAL or sub-60% acceptance forces REWORK).

```yaml
stage: B12c
company: "UFBL"
run_date: "2026-08-05"
model: claude-opus-4-8
status: complete
gate0:
  rules_checked: 36
  fails:
    - {rule: "Block E / E4 contingent-liab-to-net-worth band", severity: "MAJOR", location: "B01 Block E, report line 131", stated: "26.17% -> Score 3", correct: "15-30 band -> Score 1", effect: "Block E 4->2, Core 21->19; classification AVOID unchanged"}
    - {rule: "Block F / M12 negative-WC band on 2-year sample", severity: "MINOR", location: "B01 Block F M12, report line 179", stated: "Score 3", correct: "1 or 3 (rule silent on 2-yr straddle); borderline", effect: "if 1, moat_class NONE not THIN; AVOID unchanged"}
    - {rule: "Block B / B2 sample sufficiency", severity: "MINOR", location: "B01 Block B B2, report line 77", stated: "100% of 2 computable yrs -> 5", correct: "applied as written; 2-of-10-yr sample, disclosed", effect: "none; note only"}
recomputed_core_score: 19          # was 21; classification AVOID unchanged
recomputed_gate0_classification: "AVOID"   # unchanged; robust to F-G1
history_downgrade_check: "PASS - history_downgrade=false correct; data-length rule honoured, not conflated with trough/recovery/Ind-AS-116 depressors"
emoat:
  rules_checked: 10
  fails:
    - {rule: "Section 5 scoring method (raw x evidence-multiplier only)", severity: "CRITICAL", location: "B07 Section 5, report lines 391-396", stated: "adjusted 9.1 + non-framework +1.5/category = 15 -> MODEST", correct: "9.1 (<12) -> NO MEANINGFUL EMERGING MOAT (NONE); no corroboration bump exists in framework; strict-max reading 11.0 still <12", effect: "em_score 15->9.1; em_classification MODEST->NONE"}
    - {rule: "6D combined-assessment taxonomy", severity: "MAJOR", location: "B07 Section 6D, report lines 472-479", stated: "TURNAROUND", correct: "AVOID/not-a-transition-setup; AVOID backward + NONE(corrected) forward fails TURNAROUND bar, and B07's own 6D text says MODEST also fails it", effect: "combined_assessment TURNAROUND->AVOID"}
    - {rule: "Evidence multiplier set {1.0,0.7,0.5}", severity: "MINOR", location: "B07 Section 5 scorecard, rows A4/D2/E1/H1", stated: "0.85 and 0.6 used", correct: "not in defined discrete set; mixed-evidence interpolation undefined by framework", effect: "none; outcome <12 under any strict reading"}
recomputed_em_score: 9.1           # was 15
recomputed_em_classification: "NONE"        # NO MEANINGFUL EMERGING MOAT (<12); was MODEST
recomputed_combined_assessment: "AVOID"     # was TURNAROUND
valuation: {rules_checked: 0, fails: [], status: "pending_phase_3"}   # B10/B11 do not exist yet; deferred
recomputed_destination_pe: ""      # pending Phase 3; note: EM<25 either way -> Pillar 3 +0x, so no destination-PE impact from emoat findings
recomputed_decision: "Gate 0 AVOID unchanged; emerging-moat classification recomputes NONE (not MODEST) and combined assessment AVOID (not TURNAROUND)"
findings:
  - {severity: "CRITICAL", location: "B07 Section 5", note: "Non-framework +1.5/category corroboration adjustment inflates em_score 9.1->15, flipping classification NONE->MODEST. Fabricated scoring step. Destination-PE impact nil (EM<25 -> +0x Pillar 3); flip affects classification band and 6D routing."}
  - {severity: "MAJOR", location: "B01 Block E / E4", note: "Contingent-liab/net-worth 26.17% is in the 15-30 band (score 1); B01 assigned 3. Block E 2/20 not 4/20; Core 19 not 21. AVOID unchanged."}
  - {severity: "MAJOR", location: "B07 Section 6D", note: "combined_assessment TURNAROUND contradicts the 6D taxonomy and B07's own stated logic; with corrected NONE forward score the label should be AVOID."}
  - {severity: "MINOR", location: "B07 Section 5 scorecard", note: "Evidence multipliers 0.85/0.6 lie outside the framework's discrete {1.0,0.7,0.5} set; does not change the <12 outcome."}
  - {severity: "MINOR", location: "B01 Block F / M12", note: "Negative-WC band on a 2-year straddling sample scored 3; a stricter reading gives 1 (which would flip moat_class THIN->NONE). AVOID unchanged."}
  - {severity: "MINOR", location: "B01 Block B / B2", note: "FCF-positive proportion scored 100%->5 on a 2-of-10-year computable sample; applied as written and disclosed. Note only."}
critical_count: 1
major_count: 2
minor_count: 3
acceptance_rate: 91   # 42 of 46 checked rules passed (gate0 35/36 + emoat 7/10)
```
