# STAGE 12c — VERIFIER C: FRAMEWORK ADHERENCE (AURUM)
Run date: 2026-07-14 | Model: claude-opus-4-8 | FRESH context
Scope: PHASE 1 ONLY — Gate 0 (B01) + Emerging Moat (B07). Valuation
adherence (B11/B10) DEFERRED to phase 3; those artifacts do not exist yet.

Authority documents used:
- Gate 0 scorecard rules: prompts/01-gate-0-pipeline.md (rules are inline in
  the stage prompt; frameworks/ holds only the valuation-stage authorities,
  which are out of phase-1 scope).
- 20-category + R1 scan rules: prompts/07-emerging-moat-pipeline.md.
- CLAUDE.md NEVER rules (Emerging-Moat vs FTTCP separation; no double-credit;
  no estimated fills; low institutional ownership not a risk).

Method: rule application audited against the stated inputs only. Raw-number
correctness is Verifier A's remit and is NOT re-derived here; where a score
depends on a stated input, the band/threshold application to that input is
checked. Company quality is not judged.

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### 1.1 Data window, confidence, history handling

| Rule | As written | Applied | Verdict |
|---|---|---|---|
| Open with data-years statement | "Data available: [X] years... adapted to [X]-year history" | FY22-FY26, 5 usable years, FY17-21 excluded as divested Majesco enterprise; opened correctly | PASS |
| Confidence band | 5-6 yrs = "lower, flag may not have seen full cycle"; 3-4 = LIMITED, downgrade one tier | Placed in 5-6 band, explicitly NOT the 3-4 auto-downgrade band | PASS |
| `history_downgrade` field | Boolean tracks the 3-4-year one-tier classification downgrade | Set **true** for a 5-year history "as a qualitative caveat," self-acknowledged as outside the 3-4 band; no tier downgrade was actually applied | **FAIL (MINOR)** |

FAIL detail — `history_downgrade`: The field is mechanically tied to the 3-4
year LIMITED band, which prescribes a one-tier classification downgrade. AURUM
has 5 usable years, so no mechanical downgrade is due and none was applied
(AVOID stands on Core <40 regardless). Setting the boolean `true` repurposes it
to carry a qualitative "business is only 5 years old" caveat it was not designed
for. Zero decision impact — AVOID is the Core-driven floor and no cap or
downgrade could move it. Recorded as a MINOR field-usage deviation; the correct
mechanical value is `false` with the caveat carried in `data_notes` (where the
maker also, correctly, already narrates it). This is the specific item the task
asked me to check for the ex-Majesco rebuild; it is handled defensibly in prose
but the boolean is set contrary to its written definition.

### 1.2 Block-by-block re-derivation (band application to stated inputs)

BLOCK A (stated ROCE FY22-26: -9.42/-13.25/-10.29/-2.78/+3.32; ROE median -14.68)
- A1 median ROCE -9.42% → <10% → 0 ✓
- A2 min ROCE -13.25% → <8% → 0 ✓
- A3 median ROE -14.68% → <12% → 0 ✓
- A4 latest (+3.32) ≥ earliest (-9.42) → 5 ✓  → **Block A = 5 PASS**

BLOCK B
- B1 cum CFO/PAT -0.29 → <0.50 → 0 ✓
- B2 FCF-positive 2/3 = 66.7% → 50-74 → 2 ✓ (computed on FY24-26 subset per
  "use whatever history available"; gap disclosed) ✓
- B3 cum FCF/PAT 0.33 → 0.20-0.39 → 1 ✓ (literal band; see note)
- B4 WC days +38.77 (FY26 vs FY24) → increased >15 → 0 ✓  → **Block B = 3 PASS**

  B3 note (MINOR observation, scored PASS): the ratio is arithmetically positive
  only because both numerator (-28.86) and denominator (-87.22) are negative; the
  underlying cumulative FCF is negative. A stricter reading of the band's "…or
  negative = 0" clause (reading "negative FCF") would score B3 = 0. The maker
  applied the literal ratio value (0.33 → band 0.20-0.39 → 1) and flagged the
  artefact explicitly. Literal application is defensible. Even at B3 = 0, Block B
  → 2, Core → 35, classification unchanged (still AVOID). No decision impact.

BLOCK C
- C1 rev CAGR 121.6% → ≥20 → 5 ✓ (base-distortion flagged, robustness window shown)
- C2 PAT CAGR negative endpoint → N/M → 0 ✓; loss-to-profit swing noted ✓
- C3 positive YoY 4/4 = 100% → 5 ✓
- C4 PAT CAGR N/M → 0 per explicit rule ✓  → **Block C = 10 PASS**

BLOCK D
- D1 ND/EBITDA 1.12x → 1-2x → 3 ✓
- D2 IC 0.90x → <1.5 → 0 ✓
- D3 D/E 0.44 → 0.1-0.5 → 4 ✓
- D4 current ratio 1.39 → 1.2-1.49 → 2 ✓  → **Block D = 9 PASS**

BLOCK E
- E1 promoter 47.41% → 40-49.9 → 3 ✓
- E2 change -2.93pp → decreased 1-3% → 1 ✓
- E3 pledge N/A → scored 0 per rule 5 (absent data → 0), NOT treated as >15%
  breach ✓ (also correctly kept out of deal-breaker #5)
- E4 contingent/NW 1.42% → <5% → 5 ✓  → **Block E = 9 PASS**

CORE = 5+3+10+9+9 = 36 ✓

### 1.3 Moat block (F) tier consistency and sum

M1=5, M2=0 (PEER DATA NEEDED, not guessed ✓), M3=0, M4=3, M5=0 (peer ✓), M6=0,
M7=0, M8=1, M9=0 (peer ✓), M10=5, M11=3 (conservative <6yr per instruction ✓),
M12=5 (majority-negative WC, 3-yr sample flagged ✓). Sum = **22 ✓**. Moats
present ≥3: M1/M4/M10/M11/M12 = 5 → band 4-5 → **STRONG ✓**. PEER-DATA-NEEDED
tests correctly scored 0 rather than estimated (NEVER-rule compliant).

- M4 = 3: 0 decline years but receivables not stable ±10 fails the 5-tier's
  second condition; scored at the 3-tier ("≤1 decline year"). Bands do not
  cleanly fit a "0 decline / unstable receivables" case; the conservative 3 is
  defensible. PASS.
- M8 = 1: quantified reach but primary metric (houses) shrinking, so "network
  growing" unmet; conservative 1. Defensible. PASS.

### 1.4 Classification, deal-breakers, flag

- Matrix: Core 36 <40 → **AVOID** ✓ (correctly noted as binding before any cap).
- Deal-breakers 1,2,3,4,8 triggered; 5,6,7,9 not triggered — all nine checked
  and correctly evaluated against stated inputs ✓. #6 (ND/EBITDA>3x AND IC<3x →
  AVOID) correctly NOT triggered (1.12x not >3x); the maker correctly identifies
  IC, not leverage, as the live risk. Caps are all ≥ AVOID so moot vs the floor,
  correctly stated.
- Grand total 36 + 22 = **58 ✓**.
- FLAG-GATE0: rule fires when classification ≤ AVERAGE with historical
  depressors identified. AVOID ≤ AVERAGE, depressors (FY22-25 loss years)
  identified → flag correctly raised ✓. This matches the task's stated
  expectation (mechanically AVOID with FLAG-GATE0, losses predate FY26 inflection).

**GATE 0 VERDICT: framework-correct. 1 MINOR field-usage fail (history_downgrade
boolean); no score, no classification, no decision affected. The AVOID + FLAG-
GATE0 outcome is correctly derived.**

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### 2.1 Coverage and structure

- All 21 rows (20 categories A1-H3 + R1) addressed or explicitly NO EVIDENCE
  FOUND in Section 3 + scorecard ✓. Count verified: A(4)+B(3)+C(2)+D(2)+E(2)+
  F(2)+G(2)+H(3)+R1 = 21.
- B3 explicitly folded into D2 to avoid double-crediting one mechanism, scored 0
  — directly honours CLAUDE.md "Never credit one quality improvement through two
  mechanisms" ✓.
- FTTCP separation: report carries an explicit scope note ("distinct from and
  never to be conflated with FTTCP") — NEVER-rule compliant ✓.
- capex_embedded_growth_pct = 0: no capex programme (asset-light, actively
  DIVESTING the one owned building). Reported 0 with an explicit "not computable,
  not estimated" caveat rather than a force-fit — rule-5 compliant ✓.

### 2.2 Evidence multipliers and scorecard arithmetic

Multipliers 📄 1.0 / 🎙️ 0.7 / 🔍 0.5 applied per row; re-added independently:
1.4+0.5+0.7+2.1+1.4+3.0+0.7+1.0+3.0+0.7+3.0+0.7+3.0+4.0 = **25.2 ✓** (matches
em_score). Band 25-39 → **STRENGTHENING ✓**.

One tier-vs-multiplier inconsistency:

| Row | Summary-table tier | Scorecard multiplier | Verdict |
|---|---|---|---|
| B2 Qualification lock-in | 📄 (thin) | 🎙️ 0.7 | **FAIL (MINOR)** |

FAIL detail — B2: Section 3 narrative and the summary table label B2's evidence
📄 (5-7yr landlord leases, 27% multi-product billing), but the scorecard applies
the 🎙️ 0.7 multiplier. The inconsistency runs in the CONSERVATIVE direction
(📄 1.0 would give 1.0, i.e. +0.3), so it understates rather than inflates — the
opposite of the "🎙️-only scoring as 📄" failure mode the rubric targets. No
inflation risk; recorded MINOR. E1 and F1 carry minor label/multiplier
mismatches of the same small magnitude (E1 labelled 📄-launch/🔍-stall, scored
🎙️ 0.7; F1 labelled 📄/🎙️ mixed, scored 📄 1.0) — these roughly offset and are
within presentational tolerance.

### 2.3 Completionist guard and honest evidence grading

- Guard base rate 3-6 active categories: **6 Moderate+/Strong (C1, D2, F2, G2,
  H2, R1)** — within band ✓.
- Mandated 📄 recount performed and stated verbatim: "14 documented items across
  9 categories" ✓. Spot-checked — each of the 9 (A3, C1, D2, F1, F2, G1, G2, H2,
  R1) carries a genuine disclosed/filed/audited 📄 item; the recount is honest.
- Guard threshold nuance (MINOR observation): 14 categories carry a NON-ZERO
  score, which under a strict reading of the guard's "12 or more categories as
  active" would trip the re-examine trigger. The maker's own definition of
  "active" = Moderate+/Strong (6) is the one carried into the block, and the
  mandated recount was performed precisely because the scan is broad — so the
  guard was procedurally honoured, not evaded. Noted for transparency; not a fail.
- Honest grading: the scan is notably skeptical and self-disciplined — A2
  correctly demoted (registered TRADEMARK, not a patent → NO EVIDENCE for patent
  moat); D1 "data is the biggest moat" narrative held to 🎙️ 1.4 not credited as
  documented; E1 Dubai flagged stalled; G1 deliberately DOWNGRADED Moderate→Weak
  when the supporting Reg 30 filing was found uncollected. FLAG-NARRATIVE-VS-
  EVIDENCE explicitly surfaces the AI-story-vs-proof gap. evidence_mix
  {14 doc / 11 claim / 3 inf} is consistent with the recount. This is the honest
  documented-vs-claim-vs-inference grading the rubric demands ✓.

### 2.4 Combined assessment with B01

- 6C table pulls the INJECTED B01 correctly: core 36 / moat 22 / grand 58 / AVOID
  / 5-of-12 STRONG — all match B01-gate0.yaml exactly ✓.
- 6D combined = **TURNAROUND** with full reasoning ✓. The stage prompt names the
  label set (…GOOD / TURNAROUND / AVERAGE / AVOID) and directs full reasoning for
  transition rows, but does NOT reproduce a cell-by-cell backward×forward matrix.
  Judged on the label descriptions + the operator's stated transition-alpha
  intent: AVOID-backward (worse than AVERAGE) paired with STRENGTHENING-forward
  (real, documented, not-yet-EXPANSION) maps cleanly to TURNAROUND — the lowest
  transition label, correctly not AVERAGE (backward is worse) and not HIGH
  POTENTIAL (backward too weak). Framework-consistent ✓. Matches the task's
  stated expectation.

### 2.5 Boundary-sensitivity finding (MINOR, surfaced prominently)

em_score 25.2 sits **0.2 above the 25.0 STRENGTHENING/MODEST boundary**. The
single largest lever is **R1 scored raw HH = 4** (× 1.0 = 4.0, the top score in
the scan). R1's likelihood×impact = HH rests on a GRANTED SM-REIT registration
(high likelihood — documented) but an IMPACT the report's own text repeatedly
undercuts: SM-REIT in "wait and watch" for three consecutive quarters with no
scheme filed, Capital segment ~2% of revenue and loss-making, and the second R1
component (Supreme Court GST ruling) explicitly "confers no competitive
separation" (sector-shared). Had R1 impact been graded HM/MH (raw 3), em_score
= 24.2 → **MODEST MOAT DEVELOPMENT**, flipping the em_classification band.

This is a discretionary likelihood×impact judgment, not a violation of a written
rule (no rule prescribes "pre-launch = Medium impact"), and the large SM-REIT TAM
provides a defensible "high impact if converted" reading — so it is NOT scored as
a rule fail. But because the classification band is decision-relevant downstream
and turns on this one 0.2-margin call, it is surfaced as a MINOR finding for the
operator: the STRENGTHENING label is real but marginal, and its robustness rests
principally on the R1 impact assignment. (B2's conservative -0.3 partially
offsets in the other direction; the score is genuinely near the line.)

**EMERGING MOAT VERDICT: framework-correct. 1 MINOR multiplier-vs-tier fail (B2,
conservative direction); STRENGTHENING classification and TURNAROUND combined
assessment are correctly derived, with a flagged boundary sensitivity at R1.**

═══════════════════════════════════════════════════════════════════
## PART 3 — VALUATION (B11 / B10)
═══════════════════════════════════════════════════════════════════

**DEFERRED TO PHASE 3.** B10 and B11 do not exist in this run. No continuous
Pillar 1 formula, FTTCP ROCE authority, single-credit route, Pillar 2/3, UA
Amendment-3 order, dual-track, Hurdle Ratio, 4D weights, or SOM cross-check was
audited. Not attempted; not scored. To be run when the valuation artifacts exist.

═══════════════════════════════════════════════════════════════════
## SUMMARY
═══════════════════════════════════════════════════════════════════

Phase-1 rules checked: 30 (Gate 0) + 19 (Emerging Moat) = 49. Passed: 47.
Fails: 2, both MINOR, neither changing any score, classification, or decision.
- Gate 0: AVOID (Core 36) + FLAG-GATE0 — framework-correct.
- Emerging Moat: em_score 25.2 STRENGTHENING + combined TURNAROUND —
  framework-correct, band marginal (0.2 above MODEST boundary, R1-impact
  sensitive).
No CRITICAL, no MAJOR. Verifier C concurs with both phase-1 destinations.
Framework adherence (phase-1 scope): ~96%.

```yaml
stage: B12c
company: "AURUM"
run_date: "2026-07-14"
model: claude-opus-4-8
status: complete
scope: phase-1-only   # Gate 0 + Emerging Moat; valuation deferred to phase 3
gate0:
  rules_checked: 30
  fails:
    - {rule: "history_downgrade field usage", severity: MINOR, detail: "Set true for a 5-year history though the field is tied to the 3-4-year LIMITED band; no tier downgrade was applied and AVOID is the Core<40 floor, so zero decision impact. Correct mechanical value is false with the caveat in data_notes (already narrated)."}
emoat:
  rules_checked: 19
  fails:
    - {rule: "B2 evidence-tier vs multiplier consistency", severity: MINOR, detail: "Summary table labels B2 evidence 📄 but scorecard applies the 🎙️ 0.7 multiplier; runs in the conservative (understating) direction, no inflation. Would add +0.3 if corrected; band unchanged."}
valuation: pending-phase-3
framework_adherence_pct: 96   # phase-1 scope only (Gate 0 + Emerging Moat)
recomputed_destination_pe: ""   # N/A in phase 1 (valuation deferred)
recomputed_decision: ""         # concur: Gate 0 AVOID+FLAG-GATE0 and combined TURNAROUND are framework-correct
findings:
  - {severity: MINOR, area: gate0, location: "B01 YAML history_downgrade / report Data-window section", issue: "history_downgrade=true outside the 3-4yr band; field repurposed as a qualitative caveat", decision_impact: "none, AVOID unchanged"}
  - {severity: MINOR, area: gate0, location: "B01 Block B, B3", issue: "cum FCF/PAT 0.33 scored 1 on a ratio that is positive only because both FCF and PAT are negative; literal band application, flagged by maker", decision_impact: "none; B3=0 would give Core 35, still AVOID"}
  - {severity: MINOR, area: emoat, location: "B07 scorecard row 6 (B2) vs Section 3 summary", issue: "📄 tier in summary vs 🎙️ 0.7 multiplier in scorecard; conservative direction", decision_impact: "none; band unchanged"}
  - {severity: MINOR, area: emoat, location: "B07 scorecard row 21 (R1) / classification", issue: "em_score 25.2 sits 0.2 above the 25.0 STRENGTHENING/MODEST boundary; R1 raw HH=4 impact is generous vs the report's own 'wait-and-watch, ~2% loss-making segment, sector-shared GST' narrative; R1 at HM(3) -> 24.2 -> MODEST. Discretionary judgment, not a rule breach, but decision-relevant.", decision_impact: "potential em_classification band flip; surfaced, not rescored"}
critical_count: 0
major_count: 0
minor_count: 4
acceptance_rate: 96            # rules passed (47) / rules checked (49), phase-1 scope
```
