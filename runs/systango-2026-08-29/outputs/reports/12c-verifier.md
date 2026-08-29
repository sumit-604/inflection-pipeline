# B12c — VERIFIER C: FRAMEWORK ADHERENCE (PHASE 1 SCOPE)
Company: Systango Technologies Ltd (SYSTANGO) | Run date: 2026-08-29
Model: claude-opus-4-8 | Scope: PHASE 1 ONLY (Gate 0 B01 + Emerging Moat B07)
Valuation audit (B10/B11) DEFERRED to Phase 3 — not produced yet, section marked pending.

Rule sources read: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md
Artifacts audited: 01-gate0.md (B01), 07-emoat.md (B07)
Out of scope, NOT loaded: Master Prompt v3.6, Section 1B layers, FTTCP v2.1 (Phase 3 only).

I audit rule APPLICATION, not raw source fidelity (Verifier A owns whether a
number exists in the PDF) and not company quality. Every score below is
re-derived from the inputs the report itself states, against the thresholds in
the two rule files.

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### Block A — Return on capital (re-derived)
ROCE FY23-26 = [26.85, 26.88, 28.54, 33.00]; ROE = [22.73, 21.56, 23.17, 27.00].

| Rule | Threshold applied | Re-derived | Report | Verdict |
|---|---|---|---|---|
| A1 median ROCE | ≥25=5 | median (26.88+28.54)/2 = 27.71 → 5 | 5 | PASS |
| A2 min single-yr ROCE | ≥15=5 | 26.85 → 5 | 5 | PASS |
| A3 median ROE | ≥20=5 | median (22.73+23.17)/2 = 22.95 → 5 | 5 | PASS |
| A4 ROCE trend | latest≥earliest=5 | 33.00 ≥ 26.85 → 5 | 5 | PASS |

Block A = 20/20. PASS.

### Block B — Cash generation (re-derived)
| Rule | Threshold | Re-derived | Report | Verdict |
|---|---|---|---|---|
| B1 cum CFO/PAT | 0.70-0.84=2 | 7yr CFO 74.36 / PAT 101.57 = 0.732 → 2 | 2 | PASS |
| B2 FCF-pos years | 100%=5 | 4/4 → 5 | 5 | PASS |
| B3 cum FCF/PAT | ≥0.60=5 | 526/865 = 0.608 → 5 | 5 | PASS |
| B4 ΔWC days | ±5d=3 | 43.59 − 43.95 = −0.36 → 3 | 3 | PASS |

Block B = 15/20. PASS.

B1 window note (compliant, not a fail): B1 is scored on the 7-year window
(0.732 → 2) rather than the 4-year post-listing window (0.693 → 1). The rule
"use whatever history is available: maximum whatever exists" directs this, and
CFO+PAT are the only inputs B1 needs, both present for all 7 years. The choice
is favourable but rule-directed. Deal-breaker #4 (<0.50) does not trigger under
either window, so the selection is decision-neutral.

### Block C — Growth (re-derived)
Revenue CAGR = (90.38/52.34)^(1/3)−1 = 19.97%. PAT CAGR = 31.6%.

| Rule | Threshold | Re-derived | Report | Verdict |
|---|---|---|---|---|
| C1 revenue CAGR | ≥20=5 / 15-19.9=4 | 19.97% (see finding) | 5 | FLAG (MINOR) |
| C2 PAT CAGR | ≥20=5 | 31.6 → 5 | 5 | PASS |
| C3 pos YoY years | 100%=5 | 6/6 → 5 | 5 | PASS |
| C4 PAT−Rev CAGR | ≥+3pp=5 | 11.6pp → 5 | 5 | PASS |

CAGR edge rules honoured: no negative/zero endpoint, no loss-to-profit swing
(PAT positive every year). PASS.

FINDING C1 (MINOR, decision-neutral). Computed revenue CAGR is 19.97%, which is
strictly below the ≥20% band boundary and above the "15-19.9" band top. The
report rounds to the deck's 20% to award 5. The band label "15-19.9" implies
one-decimal precision, at which 19.97 → 20.0 ≥ 20 → 5, so the call is defensible.
But it is internally inconsistent with M11, where the SAME 19.97% is treated as
below 20% to fail the M11 middle band. If C1 were scored strictly (4), Block C =
19 and core = 87 — still ≥80, classification GOOD+ unchanged. Recorded as a
threshold-edge imprecision, not a decision error.

### Block D — Balance sheet (re-derived)
| Rule | Threshold | Re-derived | Report | Verdict |
|---|---|---|---|---|
| D1 ND/EBITDA | net cash=5 | debt 6.26 lakh < cash 1573.43 → net cash → 5 | 5 | PASS |
| D2 interest cover | ≥10x=5 | EBIT 3329.66 / 6 = 555x → 5 | 5 | PASS |
| D3 debt/equity | <0.1=5 | 6.26/13546.65 = 0.0005 → 5 | 5 | PASS |
| D4 current ratio | ≥2.0=5 | 10768.90/1496.90 = 7.19 → 5 | 5 | PASS |

Block D = 20/20. PASS. (EBIT excludes other income — a conservative adjustment;
IC lands 555x either way, no effect.)

### Block E — Shareholder alignment (re-derived)
| Rule | Threshold | Re-derived | Report | Verdict |
|---|---|---|---|---|
| E1 promoter holding | ≥60=5 | 72.07% → 5 | 5 | PASS |
| E2 promoter Δ | ±1%=3 | +0.11pp → 3 | 3 | PASS |
| E3 pledge | not found → 0 (grounding rule) | 0 | 0 | PASS |
| E4 conting.liab/NW | <5%=5 | NIL → 5 | 5 | PASS |

Block E = 13/20. PASS.
- E1: data is 17 months stale (Mar-2025 AR, not "latest quarter"). Rule 5
  (grounding) directs use of best available; 72% is far above the 60% band edge,
  so staleness does not move the score. Correctly flagged as a data gap. PASS.
- E2: rule reads "over 3 years"; only a 2-year window exists. Change is +0.11pp
  under any window and lands in the ±1% band regardless. PASS with note.
- E3: scoring NOT FOUND as 0 correctly follows the grounding rule (rule 5) even
  though it conflates "unknown" with ">15% pledge." Deal-breaker #5 correctly
  NOT triggered (unknown ≠ confirmed breach). Handling is correct.

### Block F — Quantitative moat (re-derived, 12 tests)
| Test | Threshold applied | Re-derived | Report | Verdict |
|---|---|---|---|---|
| M1 pricing power | margin +≥2pp AND rev≥10%=5 | +7.4pp, 19.97% → 5 | 5 | PASS |
| M2 cost advantage | peer data absent → 0 | 0 PEER DATA NEEDED | 0 | PASS |
| M3 capital efficiency | FAT>3x AND ROCE>20%=5 | 18.3x, 33% → 5 | 5 | PASS |
| M4 stickiness | top band needs stable ±10 rec-days | swing 45→84→48 fails top; 0 decline yrs → mid band 3 | 3 | PASS |
| M5 scale | peer data absent → 0 | 0 | 0 | PASS |
| M6 tech/R&D | R&D% undisclosed → 0 | 0 | 0 | PASS |
| M7 regulatory | unregulated → 0 | 0 | 0 | PASS |
| M8 distribution | purely digital → 0 | 0 | 0 | PASS |
| M9 brand | peer median absent → 0 | 0 PEER DATA NEEDED | 0 | PASS |
| M10 switching | grew every yr AND rec-days rose ≤10 net=5 | +2.28d net → 5 | 5 | PASS |
| M11 network | two-window; latest 19.97% < prior 54.2%, selling% blank → 0 | 0 | 0 | PASS |
| M12 negative WC | see finding | 1 (latest-yr basis) | 1 | FLAG (MINOR) |

Block F = 5+0+5+3+0+0+0+0+0+5+0+1 = 19/60. Arithmetic PASS.
Moats present (≥3): M1, M3, M4, M10 = 4 → STRONG (4-5 band). PASS.

M4/M10 consistency check: M4 denies its top band using a receivable-day
STABILITY condition (±10, violated by the swing); M10 awards its top band using
a NET-CHANGE condition (rose ≤10 over period, +2.28 satisfied). The two rules are
worded differently (stable vs rose over period), so applying each literally is
correct — not a contradiction. PASS.

FINDING M12 (MINOR, decision-neutral). WC days = [43.95, 68.35, 82.13, 43.59].
The report scores 1 on the latest year (43.59, in the 15-45 band). Two of four
years are >45 (band 0); the good band ("0-15 consistently") uses a consistency
frame, which suggests a majority/consistency read for the others too. Under a
majority read (2 of 4 years >45, mean 59.5) M12 = 0. The rule does not state the
basis for the 15-45 vs >45 bands, so latest-year is defensible. Effect: moat
score 19 vs 18; M12 is not a "present" moat (≥3) either way, moat_class STRONG
unaffected, grand total 107 vs 106, classification unchanged.

### Classification, downgrade, deal-breakers (re-derived)
- Core = A+B+C+D+E = 20+15+20+20+13 = 88. PASS (87 under strict-C1; both ≥80).
- Moat = 19; Grand = 107. PASS.
- Matrix: Core ≥80 + STRONG → EXCELLENT. PASS.
- History: 4-year primary window → LIMITED band (3-4 yrs) → one-tier downgrade →
  GOOD+. history_downgrade = true. PASS.
- Deal-breakers, 9 checks: A≥8, B≥8, medROCE 27.71≥10, cumCFO/PAT 0.732≥0.50,
  pledge unknown (not confirmed >15%), net cash (not ND>3x&IC<3x), never declined,
  PAT never negative, history 4yr (not <3). All clear. deal_breakers: []. PASS.

### Gate 0 verdict
Every block score re-derives to the reported value under a defensible reading of
the thresholds. The two flags (C1, M12) are threshold-edge imprecisions, both
decision-neutral. Classification GOOD+ stands. No CRITICAL, no MAJOR.

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### 23-category completeness (rule 3)
All 23 scored rows (A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3,
I1-I2, R1) are addressed with evidence or an explicit NO EVIDENCE FOUND / NOT
APPLICABLE. Section 3 summary table lists all 23. PASS.

### Family I present and correctly scored (verifier rule 8)
- I1 (talent asymmetry, Cat 21): scored 0. Report confirms part (a) absent (no
  patents → no named inventors; only ordinary KMP pay) and part (b) not attempted.
  Rule requires BOTH legs with (b) carrying ≥1 documented source to score above 0;
  correctly 0. PASS.
- I2 (cannibalization barrier, Cat 22): scored 0. Report applies the "what must a
  competitor destroy" test to every candidate moat and answers "nothing" → 0.
  Rule requires a specific named sacrifice to score above 0; correctly 0. PASS.
- I1/I2 contribution stated separately (0 of 0). PASS.

### Evidence-tier discounting (rules 2-3)
Raw = likelihood×impact, ×multiplier (📄 1.0, 🎙️ 0.7, 🔍 0.5). Re-derived:

| Cat | L×I (report) | Raw | Tier | Mult | Adj (re-derived) | Report |
|---|---|---|---|---|---|---|
| A2 | M×M | 2 | CLAIM | 0.7 | 1.4 | 1.4 |
| A4 | M×M | 2 | CLAIM | 0.7 | 1.4 | 1.4 |
| B2 | M×L | 1 | DOCUMENTED | 1.0 | 1.0 | 1.0 |
| C1 | L×L | 1 | CLAIM | 0.7 | 0.7 | 0.7 |
| D2 | M×M | 2 | CLAIM | 0.7 | 1.4 | 1.4 |
| G1 | M×M | 2 | DOCUMENTED | 1.0 | 2.0 | 2.0 |
| H2 | M×H | 3 | CLAIM | 0.7 | 2.1 | 2.1 |
| Sum | | | | | 10.0 | 10.0 |

All matrix values and multipliers correct. No 🎙️-only category is scored as if
📄: the mixed 📄+🎙️ rows (A2, A4, D2) are conservatively discounted at 0.7
(claim tier), which is the correct direction (no upward mis-crediting). The two
DOCUMENTED rows (B2, G1) carry 1.0 and rest on genuinely documented facts (ISO/
GOV.UK badges; cash/debt-free/FCF). G1 impact held at Medium (not High) with the
non-deployment caveat — a justified conservative cap. PASS.

### 12-point floor (rules 3, floor)
em_score 10 < 12 → NO MEANINGFUL EMERGING MOAT (NONE). Bands applied as absolute
per the 20-Aug-2026 operator ruling (no rescale). Reported as computed, not
rounded up. PASS.

### Completionist recount (rule 3)
Recount WAS performed — rule satisfied. FINDING (MINOR): the recount line states
"13 documented items across 7 categories" but then enumerates 8 categories (A2,
A4, B2, C2, F1, F2, G1, G2), and the enumerated sub-items total ~10, not 13. The
guard's purpose (detect an inflated scan) is met — the conclusion (sparse scan,
sub-floor score, negative-finding rows separated from scored rows) is sound and
the score is not over-credited. The defect is a cosmetic internal miscount in the
stated tallies, not a scoring error.

### Emerging Moat verdict
Scan applied the 23-category rubric, tier discounting, completionist recount, and
the 12-point floor correctly to reach em_score 10 / NONE. combined_assessment
GOOD+ is consistent (no forward EXPANSION found; not a transition setup). One
MINOR cosmetic miscount in the recount tally. No CRITICAL, no MAJOR.

═══════════════════════════════════════════════════════════════════
## PART 3 — VALUATION (B11) — DEFERRED
═══════════════════════════════════════════════════════════════════

Out of Phase 1 scope. B10/B11 are not produced yet (Phase 3). The valuation
framework docs (Master v3.6, Section 1B layers, FTTCP v2.1) were deliberately NOT
loaded — dead context in Phase 1. Section marked pending-phase-3.
recomputed_destination_pe: blank. recomputed_decision: blank (concur; GOOD+ and
em NONE stand as computed).

Business Understanding Narrative (verifier rule 9) is a stage-13 artifact, not an
input in Phase 1 — check N/A this pass.

═══════════════════════════════════════════════════════════════════
## SUMMARY
═══════════════════════════════════════════════════════════════════
- Gate 0: every block re-derives to reported value; classification GOOD+ correct;
  history downgrade correct; deal-breaker logic correct. 2 MINOR threshold-edge
  flags (C1, M12), both decision-neutral.
- Emerging Moat: rubric, discounting, floor, Family I all correct; em_score 10 /
  NONE re-derives exactly. 1 MINOR cosmetic recount miscount.
- No CRITICAL, no MAJOR. No decision changes. acceptance_rate well above the 60%
  REWORK floor.

```yaml
stage: B12c
company: "SYSTANGO"
run_date: "2026-08-29"
model: claude-opus-4-8
status: complete
gate0:
  rules_checked: 20
  fails:
    - {rule: "C1 revenue CAGR band", severity: "MINOR", detail: "19.97% scored 5 (≥20 band) via rounding to deck 20%; strict read = 15-19.9 band = 4. Defensible at one-decimal precision but internally inconsistent with M11 (treats 19.97% as <20%). Strict recompute: Block C 19, core 87, classification GOOD+ unchanged.", decision_impact: "none"}
    - {rule: "M12 negative-WC band basis", severity: "MINOR", detail: "Scored 1 on latest-year WC days (43.59, band 15-45); 2 of 4 years >45, a consistency/majority read gives 0. Rule does not fix the basis; latest-year defensible. Moat score 19 vs 18, moat_class STRONG unaffected, classification unchanged.", decision_impact: "none"}
emoat:
  rules_checked: 8
  fails:
    - {rule: "completionist recount tally", severity: "MINOR", detail: "Recount performed (rule satisfied) but states '13 documented items across 7 categories' while enumerating 8 categories (A2,A4,B2,C2,F1,F2,G1,G2) and ~10 sub-items. Cosmetic internal miscount; guard purpose met, score not over-credited.", decision_impact: "none"}
valuation:
  rules_checked: 0
  fails: []
  status: "pending-phase-3"
  note: "B10/B11 not produced in phase 1; valuation framework docs deliberately not loaded (dead context). Deferred to phase-3 valuation-scope pass."
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: [], note: "N/A phase-1 scope: stage-13 synthesis not an input this pass; not a REWORK trigger."}
recomputed_destination_pe: ""
recomputed_decision: ""
findings:
  - {severity: "MINOR", location: "B01 Block C / C1", note: "19.97% CAGR at the ≥20% band edge; scored 5 by rounding, decision-neutral, inconsistent with M11 treatment of same number."}
  - {severity: "MINOR", location: "B01 Block F / M12", note: "Latest-year basis for negative-WC band; majority read gives 0; decision-neutral."}
  - {severity: "MINOR", location: "B07 Section 3 recount", note: "Stated recount tally (7 categories / 13 items) inconsistent with 8 categories enumerated; cosmetic, score not over-credited."}
critical_count: 0
major_count: 0
minor_count: 3
acceptance_rate: 89
```
