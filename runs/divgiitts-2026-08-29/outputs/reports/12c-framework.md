# VERIFIER C: FRAMEWORK ADHERENCE — DIVGIITTS (PHASE 1 SCOPE)
Run date: 2026-08-29 | Model: claude-opus-4-8 | Emits: B12c

Scope: PHASE 1 only. Gate 0 (B01) and Emerging Moat (B07) compliance.
The valuation-adherence audit (B10/B11) is deferred to phase 3; those
stages do not exist yet. The valuation framework docs were NOT loaded.

Method: I re-derived every stated score from the stated inputs using the
thresholds in prompts/01-gate-0-pipeline.md and prompts/07-emerging-moat-pipeline.md.
I audit rule application only. Raw-number fidelity (does a figure appear
in the source PDF) belongs to Verifier A and is not second-guessed here.

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### Block A — Return on Capital (stated 7/20)

| Item | Stated input | Threshold | Stated score | Re-derived | Verdict |
|---|---|---|---|---|---|
| A1 Median ROCE | 7.68% (mean of FY25 5.53, FY26 9.82; n=2) | <10 = 0 | 0 | 0 | PASS |
| A2 Min single-year ROCE | 5.53% | <8 = 0 | 0 | 0 | PASS |
| A3 Median ROE | 12.70% (5th of 9 sorted) | 12-14.9 = 2 | 2 | 2 | PASS |
| A4 ROCE trend | FY26 9.82 >= FY25 5.53 | latest>=earliest = 5 | 5 | 5 | PASS |

Sorted ROE set: 4.15, 7.02, 7.62, 11.48, 12.70, 14.51, 15.05, 24.54,
26.23. Median = 12.70%. Band 12-14.9 -> 2. Correct.
Block A = 0+0+2+5 = 7. PASS.

### Block B — Cash Generation Quality (stated 11/20)

| Item | Stated input | Threshold | Stated score | Re-derived | Verdict |
|---|---|---|---|---|---|
| B1 Cum CFO/PAT | 96.90% | 0.85-0.99 = 4 | 4 | 4 | PASS |
| B2 FCF-positive yrs | 1/2 = 50% | 50-74 = 2 | 2 | 2 | PASS |
| B3 Cum FCF/PAT | 7.67% | <0.20 = 0 | 0 | 0 | PASS |
| B4 Change WC days | -14.37d (decrease) | >5d decrease = 5 | 5 | 5 | PASS |

Block B = 4+2+0+5 = 11. PASS.

### Block C — Growth (stated 8/20)

| Item | Stated input | Threshold | Stated score | Re-derived | Verdict |
|---|---|---|---|---|---|
| C1 Revenue CAGR | 10.44% | 10-14.9 = 3 | 3 | 3 | PASS |
| C2 PAT CAGR | 8.04% | 5-9.9 = 1 | 1 | 1 | PASS |
| C3 Positive YoY yrs | 5/8 = 62.5% | 50-74 = 1 | 1 | 1 | PASS |
| C4 PAT-Rev CAGR | -2.40pp | +/-3pp = 3 | 3 | 3 | PASS |

Block C = 3+1+1+3 = 8. PASS.

### Block D — Balance Sheet Strength (stated 20/20)

| Item | Stated input | Threshold | Stated score | Re-derived | Verdict |
|---|---|---|---|---|---|
| D1 ND/EBITDA | net cash | net cash = 5 | 5 | 5 | PASS |
| D2 Interest cover | 203.4x | >=10 = 5 | 5 | 5 | PASS |
| D3 Debt/Equity | 0.003 | <0.1 = 5 | 5 | 5 | PASS |
| D4 Current ratio | 5.04 | >=2.0 = 5 | 5 | 5 | PASS |

Block D = 20. PASS.

### Block E — Shareholder Alignment (stated 0/20)

All four items N/A (shareholding, pledge, contingent liabilities absent
from provided data). Rule 5: not-available -> mark N/A, score 0. Applied
correctly. E = 0. PASS. This is a data-availability zero, not a governance
finding; the report labels it so and flags it forward. Compliant.

### Block F — Quantitative Moat (stated 1/60)

| Test | Stated basis | Threshold | Score | Re-derived | Verdict |
|---|---|---|---|---|---|
| M1 Pricing power | OPM -7.91pp, rev CAGR 10.4% | decline >5pp -> else = 0 | 0 | 0 | PASS |
| M2 Cost advantage | PEER DATA NEEDED | 0 | 0 | 0 | PASS |
| M3 Capital efficiency | FAT 1.36x, ROCE 9.82% | ROCE<12 fails lowest band = 0 | 0 | 0 | PASS |
| M4 Customer stickiness | 3 decline years | 3+ = 0 | 0 | 0 | PASS |
| M5 Scale/dominance | PEER DATA NEEDED | 0 | 0 | 0 | PASS |
| M6 Tech/R&D | R&D not disclosed | 0 | 0 | 0 | PASS |
| M7 Regulatory | unregulated | 0 | 0 | 0 | PASS |
| M8 Distribution | B2B OEM, no metric | 0 | 0 | 0 | PASS |
| M9 Brand | PEER DATA NEEDED | 0 | 0 | 0 | PASS |
| M10 Switching costs | growth w/ 2+ decline yrs | 2+ decline = 1 | 1 | 1 | PASS |
| M11 Network effects | latest 3yr CAGR 9.19 < prior 19.44 | fails all = 0 | 0 | 0 | PASS |
| M12 Negative WC | WC days >45 both yrs | >45 = 0 | 0 | 0 | PASS |

Moat = 1. Moats present (>=3) = 0 -> NONE. PASS. PEER DATA NEEDED handling
on M2/M5/M9 (and partial M7) is per rule 98-101: score 0, never guess.
Compliant.

### Classification, deal-breakers, edge rules

- Core = 7+11+8+20+0 = 46. Grand total 46+1 = 47. Arithmetic PASS.
- Matrix: Core 46 in 40-59 -> AVERAGE, moat tier not consulted at this
  band. Correct. PASS.
- Deal-breaker #1 (Block A 7 < 8 -> max GOOD): FIRES, correctly recorded.
- Deal-breaker #3 (median ROCE 7.68% < 10% -> max AVERAGE): FIRES, is the
  binding cap. Correct.
- #2, #4, #6, #7, #8, #9 correctly evaluated as not-triggered.
- #5 (pledge >15%): pledge N/A. Report does not fire on unverified data.
  Correct treatment (NEVER estimate; NOT FOUND cannot assert >15%). Non-
  decision-changing (already AVERAGE). PASS.
- CAGR edge rules: no negative/zero endpoints; PAT positive all 9 years so
  no loss-to-profit swing; C4 handled normally (PAT CAGR not N/M). Report
  states "no loss-to-profit swing." Correct. PASS.
- Data confidence: 9 years -> 7-9 -> moderate; no history downgrade;
  history_downgrade: false. Correct. PASS.

### Gate 0 verdict
All 44 checked rule-applications PASS. No CRITICAL, no MAJOR. Classification
AVERAGE re-derived independently and confirmed.

MINOR observation (not a rule failure, no score/decision impact): A1, A2
and A4 rest on ROCE computable for only 2 years (FY25-FY26) because the
screener export lacks the current/non-current liability split for
FY18-FY24. The maker discloses this per metric. The A4 "trend" therefore
spans FY25->FY26, not the full window, and scores 5 on a 2-point rise. The
constraint is data-driven and transparent, not a threshold misapplication;
the outcome is unchanged because deal-breaker #3 caps at AVERAGE regardless
and both computable ROCE years sit below every higher band.

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### Coverage: all 23 categories addressed

A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, I1-I2 (22) + R1
(23). Every category carries an evidence table or an explicit NO EVIDENCE
FOUND / None. B1, B3, D1, H1 explicitly NO EVIDENCE FOUND. PASS.

### Scorecard: raw x multiplier re-derivation

| # | Raw (L×I) | Ev. type | Mult | Stated adj | Re-derived | Verdict |
|---|---|---|---|---|---|---|
| A1 | ML=1 | 🎙️ | 0.7 | 0.7 | 0.7 | PASS |
| A2 | 0 | — | — | 0 | 0 | PASS |
| A3 | MM=2 | 📄 | 1.0 | 2.0 | 2.0 | PASS |
| A4 | LL=1 | 📄 | 1.0 | 1.0 | 1.0 | PASS |
| B1 | 0 | — | — | 0 | 0 | PASS |
| B2 | HH=4 | 📄 | 1.0 | 4.0 | 4.0 | PASS |
| B3 | 0 | — | — | 0 | 0 | PASS |
| C1 | MH=3 | 📄 | 1.0 | 3.0 | 3.0 | PASS* |
| C2 | 0 | — | — | 0 | 0 | PASS |
| D1 | 0 | — | — | 0 | 0 | PASS |
| D2 | 0 | — | — | 0 | 0 | PASS |
| E1 | MH=3 | 🎙️ | 0.7 | 2.1 | 2.1 | PASS |
| E2 | HH=4 | 📄 | 1.0 | 4.0 | 4.0 | PASS |
| F1 | MM=2 | 📄 | 1.0 | 2.0 | 2.0 | PASS |
| F2 | LL=1 | 📄 | 1.0 | 1.0 | 1.0 | PASS |
| G1 | HM=3 | 📄 | 1.0 | 3.0 | 3.0 | PASS |
| G2 | MM=2 | 📄 | 1.0 | 2.0 | 2.0 | PASS |
| H1 | 0 | — | — | 0 | 0 | PASS |
| H2 | MH=3 | 📄 | 1.0 | 3.0 | 3.0 | PASS |
| H3 | LL=1 | 📄 | 1.0 | 1.0 | 1.0 | PASS |
| I1 | 0 | — | — | 0 | 0 | PASS |
| I2 | 0 | — | — | 0 | 0 | PASS |
| R1 | ML=1 | 📄 | 1.0 | 1.0 | 1.0 | PASS |

Sum re-derived = 29.8, matches the stated 29.8 ≈ 30. PASS.
Classification 25-39 -> MOAT STRENGTHENING. Correct, absolute bands per the
20-Aug-2026 operator ruling. PASS.

### Evidence-tier discipline (rule 3)

Strongest test of this audit: is any 🎙️-only category scored as if 📄?
No. The two management-claim categories (A1, E1) are the ONLY rows carrying
the 0.7 multiplier, and both are correctly discounted. Every 1.0 row rests
on documented evidence (filed AR/investor-presentation facts, certificate
dates, audited tables). The four Strong rows (B2, E2, G1, G2) are all 📄.
Discipline is sound. PASS.

### Completionist guard (stage-7 rule 6)

Active (Strong/Moderate) categories = 9 (B2, E2, G1, G2, A3, C1, E1, F1,
H2), below the 12-category alarm threshold. The recount line is present:
"📄 recount performed: 21 documented items across 9 categories." 13 of 22
categories score None. Honest and sparse, as the guard intends. PASS.

### I1/I2 gate (verifier rule 8)

- I1 (Category 21, Talent asymmetry): scored 0. Report shows part (b)
  absent (no arithmetic competitor-economics leg, no 📄 source) and part
  (a) only a hiring/pipeline story. Rule requires >0 ONLY if both legs
  evidenced with (b) carrying >=1 📄. Correctly held at 0. PASS.
- I2 (Category 22, Cannibalisation barrier): scored 0. No specific, named,
  implausible sacrifice with a 📄 source; every advantage classed as
  execution lead or external tailwind. Correctly held at 0. PASS.
- I1/I2 contribution stated separately ("0 points, zero threshold impact"),
  as the operator ruling requires for the review checkpoint. PASS.

### 2C capex-embedded growth

Rs 50.52 cr contracted capex x FAT 0.92 = Rs 46.5 cr = ~13% of Rs 352.9 cr
revenue. Arithmetic consistent; flagged 🔍 inference, not guidance. Method
compliant. PASS. (Number fidelity is Verifier A's call.)

### Combined assessment (6D)

AVERAGE backward + STRENGTHENING forward -> TURNAROUND, with full reasoning
given as the matrix requires for TURNAROUND rows. Judgment mapping, applied
reasonably. PASS.

### Emerging Moat verdict
All 30 checked rule-applications PASS. No CRITICAL, no MAJOR. em_score 29.8
and classification STRENGTHENING re-derived and confirmed.

MINOR observations (no score/classification impact):
1. C1 (*) is labelled 📄/🎙️ mixed but multiplied at 1.0. The load-bearing
   evidence (Mahindra five-line and Tata three-line cross-sell, Inv. Pres.
   slide 27) is a filed presentation = documented, so 1.0 is defensible.
   A strict reading might apply 0.7; the delta would be 0.9 points, moving
   the total to 28.9, still inside the 25-39 STRENGTHENING band. No
   classification change.
2. The recount narrative lists E1 among the "documented-item" categories,
   though E1 is 🎙️-evidenced and correctly scored at 0.7. Cosmetic
   labelling only; the active-category count (9) and the 12-alarm threshold
   are applied correctly.

═══════════════════════════════════════════════════════════════════
## PART 3 — VALUATION (B11) COMPLIANCE
═══════════════════════════════════════════════════════════════════

PENDING PHASE 3. Stages 10/11 do not exist yet and were not provided. The
valuation framework docs were not loaded (out of phase-1 scope). No audit
performed; no destination-PE re-derivation; no decision re-derivation.

Business Understanding Narrative (stage 13) is likewise out of phase-1
scope and not audited.

═══════════════════════════════════════════════════════════════════
## SUMMARY

- Gate 0 (B01): 44 rule-applications checked, 0 fails. Classification
  AVERAGE confirmed independently. 1 MINOR data-constraint observation.
- Emerging Moat (B07): 30 rule-applications checked, 0 fails. em_score
  29.8 / STRENGTHENING confirmed. 2 MINOR cosmetic observations.
- Valuation (B11): pending phase 3.
- No CRITICAL. No MAJOR. Both in-scope frameworks were applied as written.
- Recomputed destination PE: n/a (phase 1). Recomputed decision: concur.

```yaml
stage: B12c
company: "DIVGIITTS"
run_date: "2026-08-29"
model: claude-opus-4-8
status: complete
gate0: {rules_checked: 44, fails: []}
emoat: {rules_checked: 30, fails: []}
valuation: {rules_checked: 0, fails: []}   # PENDING PHASE 3 - B10/B11 not yet produced; valuation framework docs not loaded in phase-1 scope
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: []}  # OUT OF PHASE-1 SCOPE (stage 13 not produced); not audited, not a REWORK trigger here
recomputed_destination_pe: ""   # concur / n/a phase 1
recomputed_decision: ""         # concur
findings:
  - {severity: "MINOR", location: "B01 Block A (A1/A2/A4)", note: "ROCE computable only FY25-FY26 due to screener data gap; A4 trend scores 5 on a 2-year window. Data-constrained, transparently disclosed, not a threshold misapplication; classification already capped AVERAGE by deal-breaker #3, so no score or decision impact."}
  - {severity: "MINOR", location: "B07 scorecard C1", note: "C1 labelled 📄/🎙️ mixed but multiplied at 1.0. Load-bearing evidence is a filed investor presentation (documented), so 1.0 is defensible; a strict 0.7 read moves total 29.8 -> 28.9, still within the 25-39 STRENGTHENING band. No classification change."}
  - {severity: "MINOR", location: "B07 completionist recount", note: "Recount narrative bundles E1 into 'documented-item' categories though E1 is 🎙️-evidenced and correctly scored at 0.7. Cosmetic labelling only; active-category count (9) and the 12-alarm threshold applied correctly."}
critical_count: 0
major_count: 0
minor_count: 3
acceptance_rate: 100            # 74 rule-applications passed / 74 checked (gate0 44 + emoat 30); valuation deferred to phase 3
```
