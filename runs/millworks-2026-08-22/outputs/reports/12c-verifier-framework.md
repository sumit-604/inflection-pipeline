# B12c — VERIFIER C: FRAMEWORK ADHERENCE (PHASE 1)
Company: MILLWORKS (Millworks Technologies Limited) | Run date: 2026-08-22
Model: claude-opus-4-8 | Scope: PHASE 1 — Gate 0 (B01) + Emerging Moat (B07) ONLY
Valuation adherence (B11/B10 vs Master v3.6 / Section 1B / FTTCP): DEFERRED to phase 3, not run here.

Audit question: was each framework applied AS WRITTEN? Not company quality
(the AVOID is the framework's own output). Not raw source fidelity
(Verifier A owns whether a number exists at its anchor). Rule application only.

---

## PART 1 — GATE 0 (B01) COMPLIANCE

Data window: 3 restated years FY2024-FY2026. Opens with the mandated
"Data available" line. Correct.

### Block-by-block re-derivation (thresholds from prompts/01-gate-0-pipeline.md)

| Rule | Stated input | Threshold band | Report score | Recompute | Verdict |
|---|---|---|---|---|---|
| A1 median ROCE | 38.61 (median 23.02/38.61/56.44) | >=25 = 5 | 5 | 5 | PASS |
| A2 min single-yr ROCE | 23.02 | >=15 = 5 | 5 | 5 | PASS |
| A3 median ROE | 69.94 (median 40.94/69.94/144.46) | >=20 = 5 | 5 | 5 | PASS |
| A4 ROCE trend | 56.44 vs 38.61, latest>=earliest | =5 | 5 | 5 | PASS |
| B1 cumul CFO/PAT | -1302.90/4426.70 = -0.29 | <0.50 = 0 | 0 | 0 | PASS |
| B2 FCF-positive yrs | 0/3 | <50% = 0 | 0 | 0 | PASS |
| B3 cumul FCF/PAT | -3281.64/4426.70 = -0.74 | negative = 0 | 0 | 0 | PASS |
| B4 WC-days change | 136.11 -> 191.15 = +55 | increased >15 = 0 | 0 | 0 | PASS |
| C1 revenue CAGR | (14876.70/938.60)^0.5-1 = 298.1% | >=20 = 5 | 5 | 5 | PASS |
| C2 PAT CAGR | (3706.39/195.41)^0.5-1 = 335.5% | >=20 = 5 | 5 | 5 | PASS |
| C3 positive YoY rev | 2/2 = 100% | 100% = 5 | 5 | 5 | PASS |
| C4 PAT-Rev CAGR | +37.4pp | >=+3pp = 5 | 5 | 5 | PASS |
| D1 ND/EBITDA | 0.278x | 0-1.0x = 4 | 4 | 4 | PASS |
| D2 interest cover | 15.77x | >=10x = 5 | 5 | 5 | PASS |
| D3 debt/equity | 0.21 | 0.1-0.5 = 4 | 4 | 4 | PASS |
| D4 current ratio | 1.434 | 1.2-1.49 = 2 | 2 | 2 | PASS |
| E1 promoter holding | 65.08% | >=60 = 5 | 5 | 5 | PASS |
| E2 promoter change | decrease 10-16pp | decreased >3% = 0 | 0 | 0 | PASS |
| E3 pledge | 0% | 0% = 5 | 5 | 5 | PASS |
| E4 CL/NW | 0.10% | <5% = 5 | 5 | 5 | PASS |
| M1 pricing power | margin +7.16pp AND CAGR>=10% | =5 | 5 | 5 | PASS |
| M2 cost advantage | 36.71% vs peer 42.13% (below) | =0 | 0 | 0 | PASS |
| M3 capital efficiency | FAT 5.93x AND ROCE 56.44% | =5 | 5 | 5 | PASS |
| M4 customer stickiness | 0 decline yrs; recv NOT stable (73->340) | see note | 3 | 0-3 debatable | MINOR |
| M5 scale/dominance | smallest of 3 peers; universe unknown | 0 PEER DATA NEEDED | 0 | 0 | PASS |
| M6 tech/R&D | R&D% not disclosed | 0 N/A | 0 | 0 | PASS |
| M7 regulatory/license | not a licence model | 0 N/A | 0 | 0 | PASS |
| M8 distribution | B2B, no network | 0 | 0 | 0 | PASS |
| M9 brand | peer GM not extracted | 0 PEER DATA NEEDED | 0 | 0 | PASS |
| M10 switching costs | recv +267d; no tier fits | else = 0 | 0 | 0 | PASS |
| M11 network effects | <6yr, selling exp bundled | 0 | 0 | 0 | PASS |
| M12 negative WC | all yrs >45 days | >45 = 0 | 0 | 0 | PASS |

Block totals: A 20, B 0, C 20, D 15, E 15 -> Core 70. Moat 13. Grand 83.
All arithmetic re-derived clean.

### Classification chain

- Matrix: Core 70 (60-79 band) + Moat MODERATE (not STRONG/FORTRESS) ->
  "Core 60-79 + else = GOOD". Correct.
- Moat class: 3 present (M1, M3, M4) -> "2-3 = MODERATE". Correct given the
  stated scores.
- Deal-breakers: DB2 (Block B<8 -> max GOOD) and DB4 (cumul CFO/PAT -0.29
  <0.50 -> max AVERAGE) both fire; DB4 binds. Correct numbering vs the prompt
  list. DB1/3/5/6/7/8/9 correctly not triggered (history is exactly 3, so
  DB9 does not fire).
- Confidence: 3-4 yrs = LIMITED -> downgrade one tier. history_downgrade:true.
- Final chain: GOOD -> DB4 cap AVERAGE -> LIMITED downgrade one tier -> AVOID.

Order check (decision-relevant): the report applies the DB4 cap FIRST
(GOOD->AVERAGE) then the LIMITED one-tier downgrade (AVERAGE->AVOID). The
alternative order (downgrade GOOD->AVERAGE first, then a non-binding
AVERAGE cap) would land at AVERAGE, not AVOID. The report's order matches
the framework's intended sequential reading (cap sets the ceiling to
AVERAGE, the confidence downgrade then reduces one tier). PASS — the two
penalties address independent deficiencies (cash conversion vs data depth)
and stacking is not a double-count. Classification AVOID is correctly derived.

FLAG-GATE0 emitted (classification <= AVERAGE with historical depressors
named). Deal-breaker driving years stated (FY2026 CFO/receivables). CAGR
edge rules honoured (no negative-endpoint, no loss-to-profit swing; noted).

### Gate 0 finding

- **MINOR / M4 customer stickiness (B01 Block F):** scored 3. The top tier
  (5) requires zero decline years AND receivable days stable +/-10; the
  stability leg fails hard (73->340 days). Tier 3 text ("max 1 decline year,
  fully recovered") presupposes a decline that recovered, which did not
  occur, so a strict reading supports 0 or 1. The analyst's choice of 3 is
  transparently reasoned but sits in a genuine rubric gap. Recompute impact:
  moat_score 13 -> 10 and moats_confirmed 3 -> 2 if M4 were 0; moat_class
  stays MODERATE (2-3 present) either way, Core is untouched, and the AVOID
  is driven by DB4 + LIMITED, not by the moat count. No decision impact.

Gate 0 verdict: compliant. 37 rule applications checked, 1 MINOR.

---

## PART 2 — EMERGING MOAT (B07) COMPLIANCE

### Category coverage
All 22 scan categories (A1-I2) plus R1 addressed, each scored or marked NO
EVIDENCE FOUND. Family I present: I1 and I2 both scored, both 0. PASS.

### I1/I2 gate discipline (verifier rule 8)
- I1 (Category 21, talent asymmetry): scored 0. Both legs (a) and (b) absent;
  no named inventors, no ex-DRDO/HAL concentration, no above-norm remuneration.
  The rule bars a score above 0 without both legs and a 📄 (b) leg. Correct.
- I2 (Category 22, cannibalization barrier): scored 0. Honest answer for the
  two strongest rows (A4, H2) is "nothing must be destroyed" -> execution lead,
  explicitly excluded. Correct.
- I1/I2 contribution stated separately (0 of 21). No threshold crossing via
  I1/I2. Matches the operator's 20-Aug-2026 review-checkpoint requirement.

### Evidence-multiplier / raw-matrix re-check
Matrix labels (HH=4, MH/HM=3, MM/HL/LH=2, LM/ML=1, LL=1, none=0) all
internally consistent with the stated raw scores. Multipliers (📄 1.0x,
🎙️ 0.7x, 🔍 0.5x) re-derived. Adjusted total re-summed = 20.5 -> 21.
No inflation: no 🎙️-only or 🔍-only row was credited at 📄 1.0x — the
error direction the completionist guard targets does not appear.

Two rows carry an off-taxonomy multiplier, both in the conservative
(score-lowering) direction:
- B2 qualification lock-in: 📄/🔍 mixed, multiplied 0.7x (the 🎙️ value).
  Taxonomy offers 1.0x or 0.5x, not 0.7x for this mix.
- F2 execution moat: rests on 📄 documented capacity/revenue proxy, yet
  multiplied 0.7x rather than 1.0x.
Corrected to their 📄 legs both would rise (1.4->2.0 each), lifting the
total to ~21.7-22.2 -> still MODEST (12-24), still below EM>=25. No impact
on band or UA qualifier.

### Completionist guard
"📄 recount performed: 19 documented items across 12 categories" present.
Active (Strong/Moderate) rows = 7, below the guard's 12-active re-examine
trigger; the recount reconciles the 12 📄-carrying categories against the 7
active. Discipline honoured, no force-fitting. PASS.

### Classification and combined assessment
- em_score 21 -> "12-24 = MODEST MOAT DEVELOPMENT". Correct band.
- EM >= 25 UA qualifier: not met (21 < 25). Correctly stated as absolute per
  the 20-Aug-2026 ruling; no rescale attempted.
- Combined 6D: AVOID (Gate 0 AVOID + MODEST forward not clearing the
  qualifier). Correctly reasoned; the two top rows (C1, H2) flagged as the
  same Quick Pay related-party fact pattern, not double-credited. Matches the
  transition-setup matrix logic (this is NOT the GOOD/AVERAGE-backward +
  EXPANSION-forward pattern the operation hunts).

### Emerging Moat findings

- **MINOR / Section 2C (capex-embedded growth):** the prescribed method
  (capex-under-execution x historical fixed-asset turnover) was declared an
  INPUT GAP on the stated basis that "Gate 0/B01 does not carry this line."
  B01 in fact carries FY26 Net Block (2,508.48 lakhs) and FAT 5.93x inside
  M3. The prescribed method was therefore attemptable from an injected input
  (capex 6,103.25 lakhs x ~5.93x). The capacity-hours substitute (+75.3%) is
  transparently flagged, and 2C does not feed em_score, so no score/decision
  impact — but the INPUT GAP claim is inaccurate.
- **MINOR / B2, F2 multiplier (Section 5 scorecard):** 0.7x applied to 📄- or
  📄/🔍-anchored rows where taxonomy offers 1.0x/0.5x. Conservative
  direction, no band or qualifier impact (see re-check above).

Emerging Moat verdict: compliant. 30 rule applications checked, 2 MINOR.

---

## SUMMARY

- Gate 0: classification AVOID correctly derived (matrix GOOD -> DB4 cap
  AVERAGE -> LIMITED one-tier downgrade -> AVOID). Every block score, the
  deal-breaker set, and the CAGR edge rules re-derive clean. One MINOR
  (M4 tier choice, no decision impact).
- Emerging Moat: em_score 21 MODEST, EM<25 (no UA qualifier), combined AVOID.
  All 23 rows addressed, I1/I2 gate honoured, completionist recount present,
  no evidence-tier inflation. Two MINORs, both conservative, no band impact.
- Zero CRITICAL, zero MAJOR. Both stage decisions stand. Recomputed decision
  concurs: AVOID.
- Valuation (B11/B10) adherence: NOT RUN — deferred to phase 3.

```yaml
stage: B12c
company: "MILLWORKS"
run_date: "2026-08-22"
model: claude-opus-4-8
status: complete
gate0:
  rules_checked: 37
  fails:
    - {rule: "M4 customer stickiness (Block F)", severity: "MINOR", recompute: "scored 3; strict reading 0-1 (top-tier stability leg fails, tier-3 'fully recovered' presupposes a decline that did not occur). moat_score 13->10, moats_confirmed 3->2 if 0; moat_class MODERATE unchanged; no decision impact"}
emoat:
  rules_checked: 30
  fails:
    - {rule: "Section 2C capex-embedded growth", severity: "MINOR", recompute: "declared INPUT GAP citing B01 lacking FAT, but B01 M3 carries FY26 Net Block 2,508.48 and FAT 5.93x; prescribed method was attemptable. No em_score impact (2C does not feed score)"}
    - {rule: "Section 5 multiplier B2/F2", severity: "MINOR", recompute: "0.7x on 📄/📄-mixed rows vs taxonomy 1.0x/0.5x; corrected total ~21.7-22.2, still MODEST, still <25. Conservative direction, no band/qualifier impact"}
valuation: {rules_checked: 0, fails: []}   # PHASE 3, not run
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: ["N/A phase-1: stage 13 not in inputs, not audited"]}
recomputed_destination_pe: ""   # valuation deferred to phase 3
recomputed_decision: ""         # concur: AVOID (both stages)
findings:
  - {severity: "MINOR", location: "B01 Block F, M4 customer stickiness", description: "Scored 3 in a rubric gap (zero decline years but receivable days 73->340 fail the top-tier stability leg; tier-3 text presupposes a recovered decline). Defensible but strict reading is 0-1. moat_class MODERATE and the AVOID (DB4+LIMITED) both hold regardless."}
  - {severity: "MINOR", location: "B07 Section 2C, capex-embedded growth", description: "Prescribed capex x FAT method declared INPUT GAP on the claim B01 lacks the FAT line; B01 M3 in fact carries FY26 Net Block 2,508.48 and FAT 5.93x, so the method was attemptable from an injected input. Capacity-hours proxy transparently flagged; no em_score/decision impact."}
  - {severity: "MINOR", location: "B07 Section 5 scorecard, B2 and F2 multipliers", description: "0.7x (the 🎙️ value) applied to 📄- and 📄/🔍-anchored rows where taxonomy offers 1.0x or 0.5x. Conservative (score-lowering); corrected total stays MODEST and below EM>=25. No inflation, no band impact."}
critical_count: 0
major_count: 0
minor_count: 3
acceptance_rate: 96             # rules passed / rules checked, Gate0+EM (64/67)
framework_adherence: 96         # Gate 0 + Emerging Moat portion; 0 CRITICAL, 0 MAJOR, decision concurs AVOID
```
