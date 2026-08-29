# STAGE 12 — VERIFIER C: FRAMEWORK ADHERENCE (PHASE 1 SCOPE)
Company: ENTERO (Entero Healthcare Solutions Ltd) | Run date: 2026-07-27
Model: claude-opus-4-8 | Scope: PHASE 1 — Gate 0 (B01) + Emerging Moat (B07) only.
Valuation adherence audit (B10/B11) DEFERRED to phase 3, not run here.

Method: re-derive every stated score from the report's own stated inputs
against the rubric thresholds in prompts/01-gate-0-pipeline.md and
prompts/07-emerging-moat-pipeline.md. This is a rule-application audit only.
Number-to-PDF fidelity is Verifier A's job and is not touched here.

═══════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) COMPLIANCE
═══════════════════════════════════════════════════════════

### Block A — Return on Capital (rubric max 20)
Stated ROCE: FY25 9.71%, FY26 11.62% (computable years only).

| Item | Stated input | Rubric band | Rubric score | Report score | Verdict |
|---|---|---|---|---|---|
| A1 Median ROCE | median(9.71, 11.62)=10.67% | 10-14.9 = 1 | 1 | 1 | PASS |
| A2 Min single-year ROCE | 9.71% | 8-11.9 = 1 | 1 | 1 | PASS |
| A3 Median ROE | median(FY24-26)=5.64% | <12 = 0 | 0 | 0 | PASS |
| A4 ROCE trend latest vs earliest usable | 11.62 ≥ 9.71 | latest ≥ earliest = 5 | 5 | 5 | PASS |

Block A = 1+1+0+5 = 7. Report states 7. PASS.
Note on A3: negative-net-worth years FY20-23 dropped as N/M (negative
denominator), median taken over the 3 valid years. The formula does not
legislate the negative-denominator case; N/M is a conservative and defensible
reading, consistent with the CAGR negative-endpoint edge rule. PASS.
Note on A4: "earliest" was read as earliest COMPUTABLE year (FY25), because
ROCE is not derivable before FY25 in the corpus. Forced by data, not a choice
that changes the band. PASS.

### Block B — Cash Generation Quality (rubric max 20)

| Item | Stated input | Rubric band | Rubric score | Report score | Verdict |
|---|---|---|---|---|---|
| B1 Cum CFO/PAT | -203.07/192.89 = -1.05 | <0.50 = 0 | 0 | 0 | PASS |
| B2 FCF-positive years | not computable (N/A) | score 0 | 0 | 0 | PASS |
| B3 Cum FCF/PAT | not computable (N/A) | score 0 | 0 | 0 | PASS |
| B4 Change in WC Days | -5.26 days (decrease) | decreased >5 = 5 | 5 | 5 | PASS |

Block B = 0+0+0+5 = 5. Report states 5. PASS.
B2/B3: FCF not computable (no consolidated per-year capex line). Grounded-
claims rule requires score 0 on absent data, not an estimate. Handled correctly,
STANDALONE capex explicitly NOT substituted onto a consolidated CFO basis. PASS.
B4: -5.26 clears the >5-day decrease band by 0.26 day. Threshold applied
mechanically. The report itself flags the low-confidence 2-year window; the flag
is honest and does not alter the mechanical band. PASS.

### Block C — Growth (rubric max 20)

| Item | Stated input | Rubric band | Rubric score | Report score | Verdict |
|---|---|---|---|---|---|
| C1 Revenue CAGR | 30.27% (FY20-26) | ≥20 = 5 | 5 | 5 | PASS |
| C2 PAT CAGR | loss-to-profit swing in window → N/M | N/M = 0 | 0 | 0 | PASS |
| C3 Positive YoY rev years | 6/6 = 100% | 100% = 5 | 5 | 5 | PASS |
| C4 PAT CAGR − Rev CAGR | PAT CAGR N/M | N/M rule → 0 | 0 | 0 | PASS |

Block C = 5+0+5+0 = 10. Report states 10. PASS.
C2 edge-rule check: window contains net losses FY21-FY23 between profit
endpoints (FY20 +0.94, FY26 +115.04). The maker invoked the loss-to-profit
swing edge rule ("do not attempt a synthetic CAGR") and scored 0. A mechanical
CAGR off a 0.94-cr base would be meaningless; the conservative N/M reading is
within the edge rule's intent. C4 correctly follows the explicit "C4 = 0 when
PAT CAGR is N/M" instruction. PASS.

### Block D — Balance Sheet Strength (rubric max 20)

| Item | Stated input | Rubric band | Rubric score | Report score | Verdict |
|---|---|---|---|---|---|
| D1 Net Debt/EBITDA | 515.36/277.02 = 1.86x | 1-2x = 3 | 3 | 3 | PASS |
| D2 Interest Coverage | 233.73/54.39 = 4.30x | 3-4.9 = 2 | 2 | 2 | PASS |
| D3 Debt/Equity | 677.15/1688.61 = 0.401 | 0.1-0.5 = 4 | 4 | 4 | PASS |
| D4 Current Ratio | 2508.44/1587.67 = 1.58x | 1.5-1.99 = 4 | 4 | 4 | PASS |

Block D = 3+2+4+4 = 13. Report states 13. PASS.

### Block E — Shareholder Alignment (rubric max 20)
All four items N/A (no shareholding / contingent-liability data in corpus),
each scored 0 per the grounded-claims rule (absent = 0, never a typical-value
fill). Block E = 0. Report states 0. PASS. Data-absence, correctly flagged for
Halt 1, not scored as an evidenced failure.

### Core score
7 + 5 + 10 + 13 + 0 = 35. Report states 35. PASS.

### Block F — Quantitative Moat (rubric max 60)

| Test | Stated input | Rubric band | Rubric score | Report | Verdict |
|---|---|---|---|---|---|
| M1 Pricing Power | margin +2.30pp AND rev CAGR 30.27% | ≥2pp AND ≥10% = 5 | 5 | 5 | PASS |
| M2 Cost Advantage | no peer data | PEER DATA NEEDED = 0 | 0 | 0 | PASS |
| M3 Capital Efficiency | FAT 6.86x, ROCE 11.62% (<12%) | fails lowest band | 0 | 0 | PASS |
| M4 Customer Stickiness | 0 decline years, recv days +4.48 (±10) | =5 | 5 | 5 | PASS |
| M5 Scale & Dominance | no peer data | PEER DATA NEEDED = 0 | 0 | 0 | PASS |
| M6 Technology/R&D | no R&D line | 0 | 0 | 0 | PASS |
| M7 Regulatory/License | no peer count | PEER DATA NEEDED = 0 | 0 | 0 | PASS |
| M8 Distribution | reach not quantified | 0 | 0 | 0 | PASS |
| M9 Brand | no peer median | PEER DATA NEEDED = 0 | 0 | 0 | PASS |
| M10 Switching Costs | grew every year, recv days +4.48 (≤10) | =5 | 5 | 5 | PASS |
| M11 Network Effects | latest 3yr 25.94% ≥20%, selling% stable | ≥20% AND stable = 3 | 3 | 3 | PASS |
| M12 Negative WC/Float | WC days 74-80 (>45) | >45 = 0 | 0 | 0 | PASS |

Moat score = 5+0+0+5+0+0+0+0+0+5+3+0 = 18. Report states 18. PASS.
Moats present (≥3): M1, M4, M10, M11 = 4. Report states 4. PASS.
Moat classification: 4-5 present = STRONG. Report states STRONG. PASS.
M3 correctly denied even the lowest band: ROCE 11.62% is below the >12% floor,
so FAT >3x alone does not clear it. Mechanically correct.
M11 two-window test correctly run on the ≥6-year data (7 years); latest 3yr
CAGR is LOWER than prior, so the top "accelerating" tier was correctly denied
and the ≥20%-plus-stable-selling tier applied. PASS.

### Grand total
35 + 18 = 53. Report states 53. PASS.

### Classification and overrides
Data confidence: 7 years → moderate (7-9), no auto-downgrade. Correct.
Classification matrix: Core 35 <40 → AVOID (unconditional, overrides STRONG
moat). Report states AVOID. PASS. The matrix does not let a STRONG moat rescue
a sub-40 core; the report applies this correctly.

Deal-breaker application:
| # | Rule | Triggered? | Report | Verdict |
|---|---|---|---|---|
| 1 | Block A <8 → max GOOD | A=7 yes | listed | PASS |
| 2 | Block B <8 → max GOOD | B=5 yes | listed | PASS |
| 3 | median ROCE <10% → max AVERAGE | 10.67% ≥10, no | correctly not triggered | PASS |
| 4 | cum CFO/PAT <0.50 → max AVERAGE | -1.05 yes | listed | PASS |
| 5 | pledge >15% | no data, not evaluable | not listed | PASS |
| 6 | ND/EBITDA >3x AND IC <3x → AVOID | 1.86x, no | not triggered | PASS |
| 7 | revenue declined majority → max AVERAGE | no | not triggered | PASS |
| 8 | PAT negative any of last 3 yrs → max AVERAGE | FY24-26 all positive, no | not triggered | PASS |
| 9 | history <3 yrs → AVERAGE | 7 yrs, no | not triggered | PASS |

Deal-breakers 1, 2, 4 correctly recorded; 3 correctly withheld (median ROCE
10.67% narrowly clears 10%). All caps are non-binding beneath the Core<40 AVOID
floor, which the report states. PASS.

history_downgrade: false. 7-year history sits in the moderate band; the LIMITED
(3-4 year) downgrade rule does not fire. Report states false. PASS. Per-metric
thinness (2-year ROCE/WC window) is flagged individually, not folded into the
global downgrade flag — which matches the rule's design (downgrade keys off
top-line years-count, not per-metric coverage).

### Gate 0 verdict
Full adherence. Every block score re-derives to the reported value against the
stated thresholds. Classification matrix, deal-breaker set, moat-test rules,
CAGR edge rules, and history_downgrade logic all applied as written. No fails.

═══════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) COMPLIANCE
═══════════════════════════════════════════════════════════

### Category coverage (23-row method)
All 23 rows addressed: A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2,
H1-H3, I1, I2, R1. Each carries an evidence table or an explicit NO EVIDENCE
FOUND / NOT APPLICABLE. No category silently omitted, none force-fit. PASS.
Categories 21 (I1 TALENT ASYMMETRY) and 22 (I2 CANNIBALIZATION BARRIER) both
present. PASS (Verifier C rule 8).

### Scoring-table multiplier audit
Multiplier scheme: 📄 1.0x, 🎙️ 0.7x, 🔍 0.5x. Raw = L×I matrix.

| Row | L×I | Raw | Evidence label | Mult applied | Adjusted | Strict-rule mult | Verdict |
|---|---|---|---|---|---|---|---|
| B1 | MM | 2 | 🎙️/📄 mixed | 0.7 | 1.4 | mixed → 0.7 defensible | PASS |
| B2 | MM | 2 | 🎙️ | 0.7 | 1.4 | 0.7 | PASS |
| B3 | HM | 3 | 📄 (trend contested) | 0.7 | 2.1 | 📄 → 1.0 | DEVIATION (MINOR) |
| C1 | MM | 2 | 🎙️ | 0.7 | 1.4 | 0.7 | PASS |
| D1 | LM | 1 | 📄/🔍 | 0.7 | 0.7 | mixed 📄/🔍 → 0.5-1.0 | DEVIATION (MINOR) |
| D2 | MM | 2 | 📄 (no metrics) | 0.7 | 1.4 | 📄 → 1.0 | DEVIATION (MINOR) |
| F2 | HM | 3 | 📄 | 1.0 | 3.0 | 1.0 | PASS |
| G2 | MM | 2 | 📄 | 1.0 | 2.0 | 1.0 | PASS |
| H1 | HH | 4 | 📄 | 1.0 | 4.0 | 1.0 | PASS |
| H2 | MM | 2 | 🎙️/📄 mixed | 0.7 | 1.4 | mixed → 0.7 defensible | PASS |

Sum of adjusted = 18.8 → rounds to 19. Matches em_score 19 exactly. Internal
arithmetic is consistent with the maker's own multiplier choices.

FINDING (MINOR): rows B3, D2, and D1 are labelled 📄 (or 📄-lead) yet were
multiplied by 0.7, not the fixed 1.0 for the 📄 tier. The maker did this to
penalise a contested trend (B3) or absent adoption metrics (D2/D1). The strict
rubric multiplier keys off evidence TYPE, not evidence strength, so applying
0.7 to a 📄 row deviates from the mechanical rule. Direction of the deviation is
CONSERVATIVE (it lowers the score). Materiality: strict application would lift
B3 to 3.0, D2 to 2.0, D1 to 1.0 (or 0.5 on the 🔍 read), raising the total from
18.8 to ~20.7 at most. That stays inside the 12-24 MODEST band and stays below
the EM≥25 UA qualifier. No classification change, no threshold crossing, no
downstream decision impact. Severity: MINOR (presentational/within-tolerance).

Reverse failure-mode check (Verifier C rule 3 — a 🎙️-only category scored as if
📄): none present. No 🎙️-only row received a 1.0 multiplier. The only deviations
run the safe direction (📄 penalised toward 🎙️), so no score inflation exists.

### Classification and thresholds
em_score 19 → 12-24 band → MODEST MOAT DEVELOPMENT. Bands applied as written
(≥40 EXPANSION | 25-39 STRENGTHENING | 12-24 MODEST | <12 NONE). PASS.
UA qualifier: EM≥25 required; 19 < 25 → does NOT qualify. Report states this.
PASS. Threshold used absolute (no rescale), per the 20-Aug-2026 operator ruling.

### I1 / I2 rules
I1 scored 0: neither leg evidenced (no named inventors, no ex-major staff
concentration, no remuneration-annexure specialist-class signal for leg (a); no
competitor-economics arithmetic for leg (b)). Rubric requires both legs with a
📄 (b) leg for any score above 0; 0 is correct. PASS.
I2 scored 0: honest answer is "nothing structural must be destroyed" — a
well-capitalised rival can run the same acquire-and-integrate playbook. Rubric
requires a specific, named sacrifice for any score above 0; 0 is correct. PASS.
I1/I2 contribution stated separately as 0, flagged for the operator review
checkpoint as a name that did NOT cross a threshold via I1/I2. Matches the
ruling's disclosure requirement. PASS.

### Completionist recount
"📄 recount performed: 15 documented items across 8 of 23 rows." Present, in the
required format. 4 rows clear Moderate/Strong (B3, F2, G2, H1), well inside the
3-6 base rate; the 12+-active guard does not fire. No inflation of 🎙️ claims into
📄. PASS.

### evidence_mix honesty
evidence_mix {documented: 15, claim: 10, inference: 5}. Documented count ties to
the recount line (15). The mix is not skewed to over-claim documentation; the
scan is sparse and self-critical (network-reach contraction surfaced against the
company's own core pitch). Honest. PASS.

### active_categories / combined_assessment derivation
active_categories lists only the Strong/Moderate rows (B3, F2, G2, H1) — matches
the rule "only Strong/Moderate rows." PASS.
combined_assessment AVOID: backward Gate 0 already AVOID, forward EM 19 (MODEST,
below EM≥25). No GOOD/AVERAGE-backward + EXPANSION-forward setup exists, so no
transition upgrade. AVOID correctly derived from 6D. PASS.
capex_embedded_growth_pct = 0, carried as NOT FOUND / NOT COMPUTABLE with a
stated reason (no forward capex commitment in corpus), not estimated. Honours
the never-estimate rule. PASS.

### Emerging Moat verdict
Adherent, with one MINOR mechanical deviation on the evidence-quality multiplier
(B3/D2/D1 taxed to 0.7 despite a 📄 label). The deviation is conservative and
does not move the MODEST classification or the UA qualifier outcome. All other
rules — 23-category coverage, band thresholds, I1/I2 gating, completionist
recount, evidence_mix honesty, combined_assessment derivation — applied as
written.

═══════════════════════════════════════════════════════════
## PART 3 — VALUATION (B11) — DEFERRED
═══════════════════════════════════════════════════════════
Out of phase-1 scope. B10/B11 not in inputs; valuation framework docs
deliberately not loaded (dead context in phase 1). This audit runs in phase 3.
Valuation section marked pending.

═══════════════════════════════════════════════════════════
## SUMMARY
═══════════════════════════════════════════════════════════
- Gate 0 (B01): full adherence, 0 fails. Every block, moat test, deal-breaker,
  and the classification matrix re-derives to the reported values.
- Emerging Moat (B07): adherent, 1 MINOR finding (conservative multiplier
  deviation on 3 📄-labelled rows; no classification or UA impact).
- No CRITICAL, no MAJOR. No REWORK trigger from this verifier.
- recomputed_destination_pe: n/a (phase 1, no valuation audited).
- recomputed_decision: concur (AVOID backward, MODEST forward, combined AVOID).

```yaml
stage: B12c
company: "ENTERO"
run_date: "2026-07-27"
model: claude-opus-4-8
status: complete
gate0:
  rules_checked: 38
  fails: []
emoat:
  rules_checked: 25
  fails:
    - {rule: "evidence-quality multiplier keyed to evidence TYPE (📄 1.0x)", severity: MINOR, detail: "Rows B3, D2, D1 labelled 📄 (or 📄-lead) but multiplied 0.7 not 1.0. Conservative (lowers score); strict application raises total 18.8->~20.7, still MODEST (12-24), still below EM>=25 UA qualifier. No classification or decision impact."}
valuation:
  rules_checked: 0
  fails: []
  status: pending_phase_3
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: ["out of phase-1 scope; stage 13 not audited here"]}
recomputed_destination_pe: ""
recomputed_decision: ""
findings:
  - {severity: MINOR, location: "B07 Section 5 scoring table, rows B3/D2/D1", issue: "📄-labelled rows multiplied by 0.7 rather than the fixed 1.0 for the documented tier; conservative deviation, no classification or UA-qualifier impact (total 18.8 vs strict <=20.7, both MODEST)."}
critical_count: 0
major_count: 0
minor_count: 1
acceptance_rate: 98
```
