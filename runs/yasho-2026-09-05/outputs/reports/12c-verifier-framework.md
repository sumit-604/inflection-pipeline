# VERIFIER C — FRAMEWORK ADHERENCE (PHASE 1 SCOPE)
Company: YASHO | Run date: 2026-09-05 | Model: claude-opus-4-8 | Emits: B12c

Scope: Gate 0 (B01) and Emerging Moat (B07) adherence only. Valuation
adherence (B10/B11) deferred to Phase 3; that section is emitted PENDING.
I audit rule application, not company quality, and not source-fidelity of raw
numbers (Verifier A owns number existence). Where I re-derive a score I do so
from the inputs stated inside the report itself.

Rule sources read: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md.

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### Block A — Return on Capital (re-derived from the report's own inputs)
ROCE series FY22-FY26: 34.16 / 24.63 / 12.87 / 8.98 / 11.34.
ROE series FY22-FY26: 30.21 / 28.52 / 19.66 / 1.46 / 5.69.

| Rule | Stated | Re-derived | Verdict |
|---|---|---|---|
| A1 Median ROCE | 12.87% → band 10-14.9 = 1 | sorted median = 12.87 → 1 | PASS |
| A2 Min single-yr ROCE | 8.98% → band 8-11.9 = 1 | min = 8.98 → 1 | PASS |
| A3 Median ROE | 19.66% → band 15-19.9 = 4 | sorted median = 19.66 → 4 | PASS |
| A4 ROCE trend | 11.34 vs 34.16 = -22.82pp → >5pp = 0 | -22.82pp → 0 | PASS |

Block A = 6/20. CONFIRMED.

### Block B — Cash Generation Quality
Cum CFO FY21-26 = 263.94; cum PAT = 230.95 (both re-summed, exact).

| Rule | Stated | Re-derived | Verdict |
|---|---|---|---|
| B1 Cum CFO/PAT | 1.14x → ≥1.00 = 5 | 263.94/230.95 = 1.143 → 5 | PASS |
| B2 FCF-positive yrs | 1 of 3 (33%) → <50 = 0 | 33% → 0 | PASS |
| B3 Cum FCF/PAT (FY24-26) | -2.50x → negative = 0 | -223.03/89.31 = -2.497 → 0 | PASS |
| B4 WC-days change | +25.6d (FY26 vs FY24) → >15 = 0 | 152.97 - 127.35 = +25.6 → 0 | PASS |

Block B = 5/20. CONFIRMED. FCF and WC-days restricted to FY24-26 for corpus
reasons; the narrower window is disclosed at each line and the "never estimate"
rule is honoured (no synthetic FY21-23 fills). Compliant.

### Block C — Growth (CAGR edge rules checked)
| Rule | Stated | Re-derived | Verdict |
|---|---|---|---|
| C1 Revenue CAGR | 18.22% → 15-19.9 = 4 | (830.03/359.44)^0.2-1 = 18.23% → 4 | PASS |
| C2 PAT CAGR | 3.30% → <5 = 0 | (25.26/21.48)^0.2-1 = 3.30% → 0 | PASS |
| C3 Positive YoY yrs | 4 of 5 (80%) → 75-99 = 3 | FY24 the only decline → 80% → 3 | PASS |
| C4 PAT-Rev CAGR | -14.92pp → <-8pp = 0 | 3.30 - 18.22 = -14.92 → 0 | PASS |

CAGR edge rules: no endpoint is zero/negative, no loss-to-profit swing across
the window (both PAT endpoints positive), so no synthetic CAGR was attempted
and no data_notes swing entry is required. Correctly handled. Block C = 7/20.
CONFIRMED.

### Block D — Balance Sheet Strength (deal-breaker 6 is here)
| Rule | Stated | Re-derived | Verdict |
|---|---|---|---|
| D1 ND/EBITDA | 539.91/144.46 = 3.74x → >3x = 0 | 3.737 → 0 | PASS |
| D2 Interest cover | 89.68/55.72 = 1.61x → 1.5-2.9 = 1 | EBIT 89.68/55.72 = 1.609 → 1 | PASS |
| D3 Debt/Equity | 557.93/443.92 = 1.257 → 1.0-1.5 = 1 | 1.257 → 1 | PASS |
| D4 Current ratio | 49856.59/36396.95 = 1.370 → 1.2-1.49 = 2 | 1.370 → 2 | PASS |

Block D = 4/20. CONFIRMED.

**Deal-breaker 6 application — the load-bearing check.**
Rule: ND/EBITDA >3x AND Interest Coverage <3x → AVOID. Stated inputs:
3.74x > 3x TRUE, 1.61x < 3x TRUE. Both legs true → AVOID triggered. The
report applies it as binding and hard (not a cap). Applied exactly per rule.
Both legs rest on the FY2026 audited figures; the Q1FY27 presentation
(1.86x) is explicitly kept out of the deal-breaker test per the "never
substitute unaudited later-period into a deal-breaker" discipline. This is
the correct mechanical application. PASS.

### Block E — Shareholder Alignment
| Rule | Stated | Re-derived | Verdict |
|---|---|---|---|
| E1 Promoter holding | 67.91% → ≥60 = 5 | 5 | PASS |
| E2 3-yr change | data unavailable → 0 | no FY23 baseline in corpus | PASS (see note) |
| E3 Pledge | 0% (absence inference) → 5 | absence-of-disclosure, flagged | PASS |
| E4 Contingent liab/NW | 58.50/443.92 = 13.18% → 5-15 = 3 | 13.18% → 3 | PASS |

Block E = 13/20. CONFIRMED. E2 scored 0 because only a 1-year window exists
(no FY23 baseline). Gate 0 rule 5 mandates "not available → N/A, score 0", so
0 is the compliant score, not the conservative one. E3 0% pledge is correctly
labelled an absence-of-disclosure inference. Compliant.

### Block F — Quantitative Moat (M1-M12)
| Test | Stated | Re-check | Verdict |
|---|---|---|---|
| M1 Pricing power | 3 (margin +0.96pp stable, rev CAGR ≥10) | tier "stable ±2pp AND ≥10%" = 3 | PASS |
| M2 Cost advantage | 0 PEER DATA NEEDED | no peer set → 0 (not guessed) | PASS |
| M3 Capital efficiency | 0 (FAT 1.29x, ROCE 11.34% <12%) | see advisory below | PASS (advisory) |
| M4 Customer stickiness | 3 (1 decline yr, recovered) | tier "max 1 decline, recovered" = 3 | PASS |
| M5 Scale/dominance | 0 PEER DATA NEEDED | no peer mcap → 0 | PASS |
| M6 Technology/R&D | 0 (R&D/Rev 0.69% <1%) | below 1% floor → 0 | PASS |
| M7 Regulatory/licence | 0 (unregulated) | 0 | PASS |
| M8 Distribution | 1 (mentioned, unquantified) | 1 | PASS |
| M9 Brand | 0 PEER DATA NEEDED | proxy GM 40.13%, no peer → 0 | PASS |
| M10 Switching costs | 3 (grew all but 1 yr, recv +7.06d ≤10) | tier 3 | PASS |
| M11 Network effects | 0 (boundary case, scored conservatively) | conservative per instruction | PASS |
| M12 Negative WC/float | 0 (WC 127-180d >45) | 0 | PASS |

Moats present (≥3): M1, M4, M10 = 3 → 2-3 = MODERATE. CONFIRMED.
Moat score = 3+0+0+3+0+0+0+1+0+3+0+0 = 10/60. CONFIRMED. PEER DATA NEEDED
correctly used in place of guessed peer figures on M2/M5/M9.

### Classification, confidence, deal-breaker roll-up
- Core = 6+5+7+4+13 = 35. Grand total = 35+10 = 45. CONFIRMED.
- Classification matrix: Core 35 < 40 → AVOID, independent of moat tier.
  Applied correctly (MODERATE moat does not lift it). PASS.
- Data confidence: 6 years falls in the "5-6 lower confidence" band. The
  history-downgrade tier fires only at 3-4 years, so no one-tier downgrade
  applies and history_downgrade=false is correct. PASS.
- Deal-breakers: #1 (A 6<8, non-binding), #2 (B 5<8, non-binding), #6
  (binding AVOID) triggered; #3/#4/#5/#7/#8/#9 correctly NOT triggered.
  #8 checked on annual PAT (all of FY24/25/26 positive); the two negative
  intra-FY25 quarters do not trigger it, correct reading of the rule. PASS.

**Gate 0 verdict: fully compliant. The AVOID is correctly mechanical and
deal-breaker 6 is applied exactly per rule. No fails.**

Advisory (does not change any decision):
- M3 uses FY26 latest ROCE (11.34%). If median ROCE (12.87%) were paired
  with the FAT tier instead, M3 = 1 and grand_total 45 → 46. No effect on
  moats-present (still 3, MODERATE) and none on classification (AVOID from
  Core<40 and deal-breaker 6). Pairing latest ROCE with the FY26-computed FAT
  is internally consistent and defensible; logged as advisory only.
- The "may not have seen full cycle" confidence note appears in the dashboard
  prose but is not surfaced in the YAML flags[] array. Cosmetic; the flags[]
  slot is scoped to FLAG-GATE0 for ≤AVERAGE cases, which is present.

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### Completeness — all 23 rows addressed
A1,A2,A3,A4,B1,B2,B3,C1,C2,D1,D2,E1,E2,F1,F2,G1,G2,H1,H2,H3,I1,I2,R1 = 23
rows present, each with an evidence table or an explicit NO EVIDENCE FOUND.
PASS. Categories 21 (I1) and 22 (I2) both present. PASS (rule 8).

### Scorecard re-derivation (raw matrix × evidence multiplier)
Matrix HH=4, MH/HM=3, LH/HL/MM=2, LM/ML=1; multipliers DOC 1.0 / CLAIM 0.7 /
INF 0.5.

| Cat | Stated raw × mult | Re-derived | Verdict |
|---|---|---|---|
| A3 | 1 × 0.7 = 0.7 | L×M=1, CLAIM 0.7 → 0.7 | PASS |
| B2 | 4 × 1.0 = 4.0 | H×H=4, DOC 1.0 → 4.0 | PASS |
| C1 | 3 × 0.7 = 2.1 | M×H=3, CLAIM 0.7 → 2.1 | PASS |
| C2 | 1 × 0.7 = 0.7 | L×M=1, CLAIM 0.7 → 0.7 | PASS |
| E1 | 1 × 1.0 = 1.0 | L×M=1, DOC 1.0 → 1.0 | PASS |
| E2 | 1 × 0.7 = 0.7 | L×M=1, CLAIM 0.7 → 0.7 | PASS |
| F1 | 2 × 1.0 = 2.0 | M×M=2, DOC 1.0 → 2.0 | PASS |
| F2 | 2 × 0.7 = 1.4 | M×M=2, mixed 0.7 → 1.4 | PASS |
| G2 | 3 × 1.0 = 3.0 | M×H=3, DOC 1.0 → 3.0 | PASS |
| H3 | 1 × 1.0 = 1.0 | L×M=1, DOC 1.0 → 1.0 | PASS |
| all None/0 rows | 0 | 0 | PASS |

Sum = 0.7+4.0+2.1+0.7+1.0+0.7+2.0+1.4+3.0+1.0 = 16.6 → rounds to 17.
em_score = 17 CONFIRMED. Band 12-24 = MODEST MOAT DEVELOPMENT CONFIRMED.

### Evidence-tier discipline (Verifier C rule 3)
Checked every scored row for a 🎙️-only category scoring as if 📄. None found.
The three top pillars taking the full 1.0 DOC multiplier (B2, F1, G2) each
rest on genuinely documented items: B2 on the signed 15-yr agreement +
customer advances received/paid + the certification set; F1 on the AR R&D
opex line and headcount; G2 on audited AR key ratios plus the Inv-Pres WC
figure. C1 and A3, which lean on management claims, are correctly discounted
to 0.7. No tier inflation. PASS.

### Single-pillar handling
The scan is honest that one documented pillar (B2, the MNC LTSA) carries the
score, with four moderate pillars behind it and a long NO-EVIDENCE tail. The
concentration risk running counter to the "diversification" narrative is
flagged, not scored as a positive. This is the correct sparse-scan posture.
PASS.

### Completionist recount (Section 3 guard)
"📄 recount performed: 11 documented items across 5 categories." Active
categories (any evidence, Weak included) = 10 of 22, below the 12-category
red-flag threshold, so no forced re-examination is triggered. The recount is
performed explicitly and the arithmetic is internally consistent. PASS.

### I1 / I2 two-leg tests (Verifier C rule 8)
- I1 Talent asymmetry scored 0. Part (a) present only as a hiring story
  ("senior scientists joined", 50+ R&D headcount); part (b) structural-
  economics leg has no evidence and no 📄 source. Rule requires both legs
  with a 📄 (b)-leg source for any score above 0 → correct 0. PASS.
- I2 Cannibalization barrier scored 0. No specific, named competitor
  sacrifice; the corpus supports only an execution lead, which the rule
  explicitly excludes → correct 0. PASS.
- I1/I2 contribution stated separately as 0 points, per the 20-Aug-2026
  operator ruling (feeds the review checkpoint). PASS.

### Combined assessment (6D)
AVOID backward + EM 17 (MODEST) forward → combined AVOID, correctly reasoned:
EM 17 is below the ≥25 STRENGTHENING threshold needed to argue a TURNAROUND,
and HIGH POTENTIAL is ruled out because the backward AVOID is a mechanical
deal-breaker, not a GOOD/AVERAGE score. Consistent with the framework. PASS.

**Emerging Moat verdict: fully compliant. em_score 17 → MODEST is correct,
single-pillar posture handled honestly, evidence-tier discipline held, I1/I2
correctly zeroed, completionist recount performed. No fails.**

═══════════════════════════════════════════════════════════════════
## PART 3 — VALUATION (B10/B11) — PENDING
═══════════════════════════════════════════════════════════════════
Out of Phase-1 scope. B10/B11 not among inputs; the valuation framework docs
were deliberately not loaded (dead context this phase). Deferred to the
Phase-3 valuation-scope invocation. Emitted as rules_checked: 0, PENDING.

═══════════════════════════════════════════════════════════════════
## SUMMARY
═══════════════════════════════════════════════════════════════════
- Gate 0 (B01): every block score, the classification matrix, the confidence
  tier, and all nine deal-breakers re-derived and confirmed. Deal-breaker 6
  correctly triggered and applied as binding AVOID on FY2026 audited figures.
- Emerging Moat (B07): 23 rows addressed, scorecard re-summed to 17 → MODEST,
  multipliers and evidence tiers correct, I1/I2 correctly zeroed, completionist
  recount performed.
- No CRITICAL or MAJOR findings. Two MINOR advisories, neither changes any
  score materially or any decision.
- Valuation adherence deferred to Phase 3.

```yaml
stage: B12c
company: "YASHO"
run_date: "2026-09-05"
model: claude-opus-4-8
status: complete
gate0: {rules_checked: 36, fails: []}
emoat: {rules_checked: 29, fails: []}
valuation: {rules_checked: 0, fails: []}   # PENDING — deferred to Phase 3 (B10/B11 not in scope)
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: []}  # not in phase-1 scope (stage 13 not audited)
recomputed_destination_pe: ""   # concur / not in phase-1 scope
recomputed_decision: ""         # concur — Gate 0 AVOID re-derived and confirmed
findings:
  - {severity: "MINOR", location: "B01 Block F / M3", note: "M3 uses FY26 latest ROCE (11.34%); pairing median ROCE (12.87%) with the FAT tier would give M3=1 and grand_total 45->46. No effect on moats-present (3, MODERATE) or classification (AVOID via Core<40 + deal-breaker 6). Latest-ROCE pairing is internally consistent with the FY26 FAT and defensible; advisory only."}
  - {severity: "MINOR", location: "B01 confidence / YAML flags[]", note: "The '5-6 yrs lower confidence, may not have seen full cycle' note is in the dashboard prose but not surfaced in the YAML flags[] array. Cosmetic; flags[] slot is scoped to FLAG-GATE0 for <=AVERAGE, which is present."}
critical_count: 0
major_count: 0
minor_count: 2
acceptance_rate: 100    # rules passed / rules checked (gate0 + emoat); no rule misapplied
```
