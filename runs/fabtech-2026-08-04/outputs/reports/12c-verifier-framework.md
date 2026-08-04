# STAGE 12c — VERIFIER C: FRAMEWORK ADHERENCE AUDIT (PHASE 1 SCOPE)
Company: FABTECH (Fabtech Technologies Ltd) | Run date: 2026-08-04 | Model: claude-opus-4-8

## SCOPE AND METHOD

Phase-1 scope only. This audit runs TWO of the three framework-adherence checks:

1. **Gate 0 (B01)** — full re-derivation of every block score, moat test, deal-breaker,
   history downgrade, and classification against the stated thresholds in
   `prompts/01-gate-0-pipeline.md`.
2. **Emerging Moat (B07)** — all-21-category coverage, evidence-multiplier arithmetic,
   completionist recount, evidence-tier consistency, scorecard total, classification band,
   and combined assessment against `prompts/07-emerging-moat-pipeline.md`.

The **valuation-adherence audit (B10/B11)** is **DEFERRED TO PHASE 3** — those stages do not
exist yet. No exit PE, Hurdle Ratio, RRM, or fair value is re-derived here.

I audit RULE APPLICATION, not raw-number source fidelity (Verifier A owns whether a number
exists at its cited anchor) and not company quality. Where a score depends on an input, I take
the stage's stated input as given and check only that the threshold/formula was applied as
written.

---

## PART 1 — GATE 0 (B01) COMPLIANCE

### Block A — Return on Capital (stated ROCE: FY23 29.32, FY24 27.01, FY25 22.06, FY26 11.25; ROE: FY23 24.43, FY24 24.65, FY25 30.46, FY26 12.94)

| Rule | Stated basis | Re-derived | Band applied | Verdict |
|---|---|---|---|---|
| A1 Median ROCE | median{11.25,22.06,27.01,29.32} = 24.535% | 24.535% | 20-24.9 = **4** | PASS |
| A2 Min single-yr ROCE | 11.25% | 11.25% | 8-11.9 = **1** | PASS |
| A3 Median ROE | median{12.94,24.43,24.65,30.46} = 24.54% | 24.54% | ≥20 = **5** | PASS |
| A4 ROCE trend latest vs earliest | 11.25 − 29.32 = −18.07pp | decline >5pp | **0** | PASS |

Block A = 4+1+5+0 = **10**. PASS. (screener ROCE was blank → computed, per "compute only when absent".)

### Block B — Cash Generation Quality

| Rule | Re-derived | Band | Verdict |
|---|---|---|---|
| B1 Cum CFO/PAT | 1,087.26 / 13,376.23 = 8.13% | <0.50 = **0** | PASS |
| B2 FCF-positive years | 1 of 4 (only FY24 +5,920.98) = 25% | <50 = **0** | PASS |
| B3 Cum FCF/PAT | −2,016.04 / 13,376.23 = −15.08% | negative = **0** | PASS |
| B4 WC-days change | FY23 118.0 → FY26 106.9 = −11.1 days | decreased >5 = **5** | PASS |

Block B = 0+0+0+5 = **5**. PASS. WC-day arithmetic re-checked on revenue-basis days (stated basis) and reconciles.

### Block C — Growth (3-yr CAGR FY23→FY26)

| Rule | Re-derived | Band | Verdict |
|---|---|---|---|
| C1 Revenue CAGR | (41,077.18/19,379.75)^(1/3)−1 = 28.46% | ≥20 = **5** | PASS |
| C2 PAT CAGR | (3,835.80/2,173.37)^(1/3)−1 = 20.86% | ≥20 = **5** | PASS |
| C3 Positive YoY yrs | 3 of 3 (FY24/25/26 all +) = 100% | 100 = **5** | PASS |
| C4 PAT−Rev CAGR | 20.86 − 28.46 = −7.60pp | −3 to −8pp = **1** | PASS |

Block C = 5+5+5+1 = **16**. PASS. CAGR edge rules N/A (both endpoints positive, no loss-to-profit swing).

### Block D — Balance Sheet Strength (latest = FY26)

| Rule | Re-derived | Band | Verdict |
|---|---|---|---|
| D1 Net Debt/EBITDA | 4,273.26 − 8,688.16 − 12,168.98 = −16,583.88 (net cash) | net cash = **5** | PASS |
| D2 Interest coverage | 5,025.41 / 415.90 = 12.08x | ≥10 = **5** | PASS |
| D3 Debt/Equity | 4,273.26 / 41,976.93 = 0.102x | 0.1-0.5 = **4** | PASS |
| D4 Current ratio | 51,641.88 / 20,684.70 = 2.50x | ≥2.0 = **5** | PASS |

Block D = 5+5+4+5 = **19**. PASS. D3 borderline (0.102 > 0.10, so band 4 not 5) — applied correctly.

### Block E — Shareholder Alignment

| Rule | Stated basis | Band | Verdict |
|---|---|---|---|
| E1 Promoter holding | N/A (input gap) | score 0 | PASS (N/A→0 per grounded-claims rule) |
| E2 Promoter Δ 3yr | N/A | score 0 | PASS |
| E3 Pledge | N/A | score 0 | PASS |
| E4 Contingent liab / NW | FY25 3,256.20 / 17,311.36 = 18.81% | 15-30 = **1** | PASS |

Block E = 0+0+0+1 = **1**. PASS. E4 uses FY25 (FY26 contingent-liability note absent from results extracts); the maker matched FY25 numerator to FY25 net-worth denominator (consistent-period), a defensible handling of the data gap and explicitly flagged. Not a deviation.

**CORE SCORE = 10+5+16+19+1 = 51.** PASS.

### Block F — Quantitative Moat (Max 60)

| Test | Stated inputs | Band applied | Score | Verdict |
|---|---|---|---|---|
| M1 Pricing power | margin −1.3pp (±2pp) AND rev CAGR 28.46% | stable ±2pp AND ≥10% = 3 | **3** | PASS |
| M2 Cost advantage | peer data absent | PEER DATA NEEDED = 0 | **0** | PASS |
| M3 Capital efficiency | FAT 14.2x, ROCE 11.25% (<12 floor) | no band met = 0 | **0** | PASS |
| M4 Customer stickiness | 0 decline yrs; recv days 156-187 (not ±10) | top fails; "0 decline, recovered" = 3 | **3** | PASS |
| M5 Scale/dominance | peer data absent | 0 | **0** | PASS |
| M6 Technology/R&D | no R&D line | else 0 | **0** | PASS |
| M7 Regulatory/license | peer count absent | 0 | **0** | PASS |
| M8 Distribution | not a distribution model | none = 0 | **0** | PASS |
| M9 Brand | GM proxy 40.95%, no peer median | PEER DATA NEEDED = 0 | **0** | PASS |
| M10 Switching costs | rev grew every yr AND recv days −5.7 (≤10 rise) | =5 | **5** | PASS |
| M11 Network effects | <6yr; rev CAGR ≥20 but selling% unconfirmed | conservative 1 | **1** | PASS |
| M12 Negative WC/float | WC days all yrs >45 (98-124) | >45 = 0 | **0** | PASS |

Block F = 3+0+0+3+0+0+0+0+0+5+1+0 = **12**. PASS.
Moats present (≥3): M1, M4, M10 = **3** → **MODERATE** (2-3 present). PASS.

### Moat classification, history, deal-breakers, final class

| Check | Re-derived | Verdict |
|---|---|---|
| Moat class | 3 present → MODERATE | PASS |
| Grand total | 51 + 12 = 63 / 160 | PASS |
| Data confidence | 4 yrs → "3-4 LIMITED, downgrade one tier" | PASS (applied) |
| DB1 Block A<8→max GOOD | A=10, not triggered | PASS |
| DB2 Block B<8→max GOOD | B=5, **TRIGGERED** | PASS |
| DB3 median ROCE<10%→max AVG | 24.5%, not triggered | PASS |
| DB4 cum CFO/PAT<0.50→max AVG | 0.0813, **TRIGGERED** | PASS |
| DB5 pledge>15%→max AVG | no data, not evaluable | PASS |
| DB6 ND/EBITDA>3 AND IC<3→AVOID | net cash, not triggered | PASS |
| DB7 rev decline majority→max AVG | 0 decline yrs, not triggered | PASS |
| DB8 PAT neg in last 3→max AVG | all positive, not triggered | PASS |
| DB9 history<3yr→AVERAGE | 4 yrs, not triggered | PASS |
| Most-restrictive cap | max AVERAGE (DB4); DB2 = max GOOD | PASS |
| Classification matrix | Core 51 → 40-59 = AVERAGE | PASS |
| Deal-breaker cap | max AVERAGE (already AVERAGE) | PASS |
| History downgrade | AVERAGE − 1 tier → **AVOID** | PASS |
| FLAG-GATE0 rule | class ≤ AVERAGE + named depressors → flag emitted | PASS |

**Gate 0 final classification AVOID: re-derives exactly. No deviation found.**

### Gate 0 verdict
**46 rules checked, 46 PASS, 0 FAIL.** Every block score, moat test, deal-breaker, the history
downgrade, and the final AVOID reconstruct exactly from the stated inputs and thresholds. This is
a clean, rule-faithful application. The concern with FABTECH is company quality (out of my scope,
correctly flagged, not a halt), not framework misapplication.

---

## PART 2 — EMERGING MOAT (B07) COMPLIANCE

### Category coverage
All **21** categories present (A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, R1) in
both the Section 3 summary table and the Section 5 scorecard; each carries evidence or an explicit
NO EVIDENCE FOUND. **PASS.**

### Evidence-multiplier arithmetic (📄 1.0 / 🎙️ 0.7 / 🔍 0.5)

Every scored row re-derived (raw L×I × multiplier):
A1 2×0.7=1.4 · A3 1×0.7=0.7 · B1 1×1.0=1.0 · C1 1×0.7=0.7 · C2 2×1.0=2.0 · E1 4×1.0=4.0 ·
F2 1×0.7=0.7 · G1 3×1.0=3.0 · H2 2×1.0=2.0 · H3 1×0.7=0.7 · R1 3×1.0=3.0; all zero rows = 0.
**Sum = 19.2 → em_score 19.** Matches the block. **PASS** on all 21 multiplier applications.

### Completionist guard / recount
Active (Strong/Moderate) categories = 5 (C2, E1, G1, H2, R1); positive-scored categories = 11.
Both below the 12-category re-examination trigger. The 📄 recount was nonetheless performed
("20 documented items across 5 scored categories"). **PASS.**

### Evidence-tier consistency (the key rule: no 🎙️-only category scored as 📄)
The five Moderate categories all rest on genuine 📄 evidence:
- C2 — geographic revenue segment table (AR p.43) 📄
- E1 — SACE incorporated, Rs 24 Cr approved, first civil order won 📄
- G1 — cash/debt metrics, AR p.46 Annexure C 📄
- H2 — SACE + KP Group collaboration, AR p.11 📄
- R1 — SACE entity/first order 📄 backbone (labelled "📄/🎙️ mixed")

No Strong/Moderate score rests on management claim or inference alone. **PASS.**

### Classification and combined assessment
- em_score 19 → band 12-24 = **MODEST MOAT DEVELOPMENT**. Correct band. PASS.
- 2C capex-embedded-growth: Rs 24 Cr × 14.2x FAT = 340.8 / 410.77 = **83%**; arithmetic shown,
  and correctly flagged low-confidence. PASS.
- 6D combined: backward AVOID + forward MODEST cannot reach HIGH POTENTIAL / TURNAROUND (which
  require GOOD/AVERAGE backward + EXPANSION forward). Combined = **AVOID**. Rule applied correctly. PASS.
- All six sections + optionality register present. PASS.

### Emerging Moat verdict
**26 rules checked, 26 PASS, 0 hard FAIL.** Two MINOR observations (below) — both defensible,
neither a rule violation, neither classification-changing.

---

## MINOR OBSERVATIONS (Emerging Moat — non-blocking, decision unchanged)

**MINOR-1 — E1 and R1 share one underlying development.** E1 (Geographic first-mover, 4.0) and
R1 (Regulatory/policy tailwind, 3.0) are both scored primarily off the same SACE incorporation /
Vision 2030 localisation event, together contributing 7.0 of the 19.2 total (~36%). The 20-category
scan permits a single development to surface across families, and the report is fully transparent
about the E1/R1 linkage (Section 4C explicitly ties them), so this is NOT a rule violation. Noted so
a reader understands the forward score is more concentrated than "5 Moderate categories" implies.
Location: B07 Section 5 scorecard + Section 4C. Severity MINOR. Removing the overlap still leaves MODEST.

**MINOR-2 — negative-signal categories carry positive floor scores.** B1 (backward integration,
+1.0) and F2 (execution moat, +0.7) are described in the narrative as *negative* signals (rising
related-party procurement dependence ~26%; promise-delivery grade C, 3/2/5). Each is scored at the
LL=1 floor rather than 0, so both contribute a small positive amount (1.7 combined) to a forward
score whose narrative treats them as risks. Multiplier application is internally correct (B1 📄 ×1.0,
F2 🎙️ ×0.7); the quibble is only whether a moat's likelihood×impact should be the floor or zero when
the evidence points against a moat. Conservative-direction only. Stripping both leaves 17.5 — still
MODEST (12-24). Location: B07 Section 5. Severity MINOR.

---

## PART 3 — VALUATION (B10/B11) COMPLIANCE

**PENDING PHASE 3.** Stages 10 and 11 do not exist in this run yet; the continuous-Pillar-1
formula, FTTCP ROCE authority, single-credit rule, Pillar-2 multiplier/offset rules, Pillar-3
EM/catalyst inputs, UA Amendment-3 ordering, sector cap, dual-track carry-through, Hurdle Ratio,
4D weights, and SOM cross-check are all deferred and NOT audited here. No exit PE, Hurdle Ratio,
RRM, or fair value has been re-derived.

---

## SUMMARY

| Framework | Rules checked | Pass | Fail (hard) | Minor | Verdict |
|---|---|---|---|---|---|
| Gate 0 (B01) | 46 | 46 | 0 | 0 | Fully compliant; AVOID re-derives exactly |
| Emerging Moat (B07) | 26 | 26 | 0 | 2 | Compliant; 2 non-blocking observations; MODEST + combined AVOID correct |
| Valuation (B10/B11) | — | — | — | — | PENDING PHASE 3 |

No CRITICAL, no MAJOR. Nothing changes the Gate 0 AVOID classification or the combined-assessment
AVOID. Destination PE / decision recompute: not applicable in Phase 1 (valuation deferred);
concur with both stages' framework application on the two audited stages.

```yaml
stage: B12c
company: "FABTECH"
run_date: "2026-08-04"
model: claude-opus-4-8
status: complete
phase: 1
scope_note: "Phase-1 scope: Gate 0 (B01) and Emerging Moat (B07) framework audits only. Valuation (B10/B11) deferred to Phase 3 - stages do not exist yet."
gate0: {rules_checked: 46, fails: []}
emoat:
  rules_checked: 26
  fails:
    - {severity: "MINOR", rule: "Evidence concentration (E1/R1)", note: "E1 (4.0) and R1 (3.0) both scored off the same SACE/Vision 2030 development, ~36% of the 19.2 total; permitted by the 20-category scan and transparently disclosed, not a rule violation, MODEST unchanged."}
    - {severity: "MINOR", rule: "Negative-signal floor score (B1/F2)", note: "B1 (+1.0) and F2 (+0.7) are narrated as risk/negative signals yet carry the LL=1 floor rather than 0; multipliers correct, conservative-direction only, MODEST unchanged if removed."}
valuation: {status: "PENDING PHASE 3", rules_checked: 0, fails: []}
recomputed_destination_pe: ""
recomputed_decision: ""
findings:
  - {severity: "MINOR", location: "B07 Section 5 scorecard + Section 4C", note: "E1 and R1 share one underlying development (SACE / Vision 2030 localisation), together 7.0 of 19.2 (~36%); allowed and disclosed, forward score more concentrated than 5 Moderate categories suggests."}
  - {severity: "MINOR", location: "B07 Section 5 scorecard", note: "B1 and F2 are negative-signal categories carrying LL=1 floor scores (+1.7 combined); conservative-direction, classification stays MODEST if zeroed."}
critical_count: 0
major_count: 0
minor_count: 2
acceptance_rate: 97
```
