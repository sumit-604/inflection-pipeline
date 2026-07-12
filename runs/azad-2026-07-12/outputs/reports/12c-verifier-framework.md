# VERIFIER C — FRAMEWORK ADHERENCE (B12c) — Azad Engineering (AZAD)

Run date: 2026-07-12 | Model: claude-opus-4-8 | Stage: B12c
Scope: PHASE 1 ONLY — Gate 0 (B01) and Emerging Moat (B07) rule application.
Valuation adherence (B11/B10) is DEFERRED to phase 3 (stages 10/11 not yet
run); the valuation section of the emitted YAML is left pending as instructed.

Audit basis: I re-derive scores and classifications from the INPUTS AS STATED
in each report against the THRESHOLDS AS WRITTEN in the framework files. I do
not re-verify raw source numbers (Verifier A owns numbers) and I do not judge
company quality. A rule "PASSES" when the stated inputs, run through the
written band, reproduce the reported score/classification.

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) COMPLIANCE
Framework: prompts/01-gate-0-pipeline.md
═══════════════════════════════════════════════════════════════════

### Block A — Return on Capital
| Rule | Stated input | Written band | Expected | Reported | Verdict |
|---|---|---|---|---|---|
| A1 Median ROCE | 11.05% (median of 8.12/8.84/11.03/11.05/14.03/15.44/23.24, 4th of 7) | 10-14.9→1 | 1 | 1 | PASS |
| A2 Min ROCE | 8.12% | 8-11.9→1 | 1 | 1 | PASS |
| A3 Median ROE | 13.80% (median of 5.25/8.59/8.90/13.80/15.08/24.31/26.37) | 12-14.9→2 | 2 | 2 | PASS |
| A4 ROCE trend | FY26 8.84% vs FY20 23.24% = −14.4pp | decline >5pp→0 | 0 | 0 | PASS |
| Block A total | 1+1+2+0 | — | 4 | 4 | PASS |

### Block B — Cash Generation Quality
| Rule | Stated input | Written band | Expected | Reported | Verdict |
|---|---|---|---|---|---|
| B1 Cum CFO/PAT | 13.92/350.39 = 0.04 | <0.50→0 | 0 | 0 | PASS |
| B2 FCF-positive % | 0/2 = 0% (FY25-26 subset; FY20-24 capex N/A) | <50%→0 | 0 | 0 | PASS (data-gap note) |
| B3 Cum FCF/PAT | −906.21/220.69 = −4.11 | negative→0 | 0 | 0 | PASS |
| B4 Δ WC Days | +72.8 (FY26 339.7 vs FY25 266.9; FY20 payables N/A) | increased >15→0 | 0 | 0 | PASS w/ MINOR |
| Block B total | 0+0+0+0 | — | 0 | 0 | PASS |

B4 MINOR: framework specifies "latest vs earliest." True FY26-vs-FY20 is not
computable (FY20 trade payables absent). Report substituted the nearest
fully-computable comparator (FY26 vs FY25) and disclosed it. Score is 0 under
any admissible reading (R+I-only proxy rises 171→340 across the window before
any payables offset), so the deviation is score-neutral and transparently
handled per the NOT-FOUND discipline. Rule outcome unaffected.

### Block C — Growth
| Rule | Stated input | Written band | Expected | Reported | Verdict |
|---|---|---|---|---|---|
| C1 Rev CAGR | 30.04% (FY20→26) | ≥20→5 | 5 | 5 | PASS |
| C2 PAT CAGR | 35.78%; both endpoints positive, no loss-to-profit swing | ≥20→5 | 5 | 5 | PASS |
| C3 Positive YoY | 5/6 = 83.3% | 75-99→3 | 3 | 3 | PASS |
| C4 PAT−Rev CAGR | +5.74pp | ≥+3pp→5 | 5 | 5 | PASS |
| Block C total | 5+5+3+5 | — | 18 | 18 | PASS |

CAGR edge rules honoured: no negative/zero endpoints (C1/C2), no synthetic
CAGR attempted, no loss-to-profit swing (PAT positive every year FY20-26), so
C4 computed normally rather than forced to 0. PASS.

### Block D — Balance Sheet Strength (latest FY26)
| Rule | Stated input | Written band | Expected | Reported | Verdict |
|---|---|---|---|---|---|
| D1 ND/EBITDA | 1.29x | 1-2x→3 | 3 | 3 | PASS |
| D2 Interest cover | 5.65x | 5-9.9→4 | 4 | 4 | PASS |
| D3 Debt/Equity | 0.30x | 0.1-0.5→4 | 4 | 4 | PASS |
| D4 Current ratio | 3.30x | ≥2.0→5 | 5 | 5 | PASS |
| Block D total | 3+4+4+5 | — | 16 | 16 | PASS |

Non-financial issuer, so the bank/NBFC alternate bands (CAR/PCR/default-3)
correctly not invoked. PASS.

### Block E — Shareholder Alignment
| Rule | Stated input | Written rule | Expected | Reported | Verdict |
|---|---|---|---|---|---|
| E1-E4 | N/A (no shareholding-pattern or contingent-liab data in any file) | rule 5: N/A→0 | 0 each | 0 each | PASS |
| Block E total | — | — | 0 | 0 | PASS |

Correct: gaps scored 0, not estimated. No promoter/pledge/contingent figures
were fabricated. PASS.

### Block F — Quantitative Moat (12 tests)
| Test | Stated input | Written band | Expected | Reported | Verdict |
|---|---|---|---|---|---|
| M1 Pricing power | margin +2.99pp AND rev CAGR 30% | ≥2pp exp AND ≥10%→5 | 5 | 5 | PASS |
| M2 Cost adv | +16.19pp vs peer median | ≥5pp above→5 | 5 | 5 | PASS |
| M3 Cap efficiency | FAT 0.78x, ROCE 8.84% | fails all tiers→0 | 0 | 0 | PASS |
| M4 Stickiness | 1 decline yr, fully recovered | max1 recovered→3 | 3 | 3 | PASS |
| M5 Scale | top-3 mcap (3rd/5), margin #1 | top3 AND margin top2→3 | 3 | 3 | PASS |
| M6 Tech/R&D | no data | N/A→0 | 0 | 0 | PASS |
| M7 Reg/License | no player census | N/A→0 | 0 | 0 | PASS |
| M8 Distribution | B2B OEM, none | none→0 | 0 | 0 | PASS |
| M9 Brand | GM proxy +32.67pp, rev CAGR 30% | ≥10pp AND ≥10%→5 | 5 | 5 | PASS |
| M10 Switching | growth all-but-1 yr, recv days +69.4 (not stable) | fails =3 (not stable), <2 declines→else 0 | 0 | 0 | PASS |
| M11 Network | latest 3yr 32.88% > prior 27.24%, selling% declining | both→5 | 5 | 5 | PASS |
| M12 Neg WC | WC days >45 all measurable yrs | >45→0 | 0 | 0 | PASS |

Matrix mapping: M10 correctly cascades to 0 — the =3 tier requires "stable"
receivable days (report shows +69.4), and the =1 tier requires 2+ decline
years (only 1 exists), so "else = 0" is the only admissible landing. PASS.

Block F total = 5+5+0+3+3+0+0+0+5+0+5+0 = 26 (reported 26) PASS.
Moats present (≥3): M1,M2,M4,M5,M9,M11 = 6 → 6+ = FORTRESS (reported) PASS.

### Classification, confidence, deal-breakers
| Check | Derivation | Reported | Verdict |
|---|---|---|---|
| Core total | 4+0+18+16+0 = 38 | 38 | PASS |
| Grand total | 38+26 = 64 | 64 | PASS |
| Data confidence | 7 yrs → 7-9 "moderate" | moderate | PASS |
| History downgrade | LIMITED only at 3-4 yrs; 7 yrs → none | none | PASS |
| Classification matrix | Core <40 → AVOID (moat class does not enter matrix below Core 60) | AVOID | PASS |
| DB1 Block A<8 | 4<8 → max GOOD (triggered, recorded, years named) | recorded | PASS |
| DB2 Block B<8 | 0<8 → max GOOD (triggered, recorded, years named) | recorded | PASS |
| DB3 median ROCE<10% | 11.05%≥10% → not triggered | not triggered | PASS |
| DB4 cum CFO/PAT<0.50 | 0.04<0.50 → max AVERAGE (triggered, years named) | recorded | PASS |
| DB5 pledge>15% | data absent → not assessed | not triggered | PASS |
| DB6 ND/EBITDA>3x AND IC<3x | 1.29x / 5.65x → not triggered | not triggered | PASS |
| DB7 rev decline majority | 1/6 → not triggered | not triggered | PASS |
| DB8 PAT neg last 3 yrs | all positive → not triggered | not triggered | PASS |
| DB9 history<3 yrs | 7 yrs → not triggered | not triggered | PASS |
| Cap application | base AVOID already ≤ every cap (GOOD/AVERAGE) → caps non-binding | non-binding | PASS |

Deal-breaker discipline is correctly applied: triggered caps are recorded with
their driving years (per the framework's "state WHICH years drive any
deal-breaker" instruction), and because the base classification (AVOID) already
sits below every cap, the caps do not alter the final verdict. Final
classification AVOID is correctly derived. The FLAG-GATE0 condition
(classification ≤ AVERAGE with historical depressors) is satisfied and the
report flags forward with the QIP/capex rebase named. PASS.

### Gate 0 verdict
All 47 rule checks reproduce the reported scores and classification. One MINOR
(B4 comparator substitution) — disclosed, score-neutral, no classification
impact. No score, no block total, no deal-breaker, and no classification is
misapplied.

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) COMPLIANCE
Framework: prompts/07-emerging-moat-pipeline.md
═══════════════════════════════════════════════════════════════════

### Coverage — all 21 categories addressed or explicitly NO EVIDENCE
A1,A2,A3,A4 (4) + B1,B2,B3 (3) + C1,C2 (2) + D1,D2 (2) + E1,E2 (2) +
F1,F2 (2) + G1,G2 (2) + H1,H2,H3 (3) + R1 (1) = 21. Every row appears in the
Section 3 summary table and the Section 5 scorecard. Zero-evidence categories
(A2,A4,B3,D1,D2,H3) are stated "NO EVIDENCE FOUND"; contrary-evidence
categories (C2,G1,G2) are stated "No (contrary evidence)" with the contradiction
named. PASS — no category skipped or force-fit.

### Evidence multiplier + likelihood×impact mapping (Section 5)
Matrix: HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0.
Multipliers: 📄1.0, 🎙️0.7, 🔍0.5.

| ID | L×I → raw | Type → mult | Expected adj | Reported | Verdict |
|---|---|---|---|---|---|
| A1 | HH→4 | 📄→1.0 | 4.0 | 4.0 | PASS |
| A3 | HM→3 | 📄→1.0 | 3.0 | 3.0 | PASS |
| B1 | MM→2 | 📄→1.0 | 2.0 | 2.0 | PASS (note) |
| B2 | HH→4 | 📄→1.0 | 4.0 | 4.0 | PASS |
| C1 | HM→3 | 🎙️→0.7 | 2.1 | 2.1 | PASS |
| E1 | LM→1 | 🎙️→0.7 | 0.7 | 0.7 | PASS |
| E2 | LL→1 | 🎙️→0.7 | 0.7 | 0.7 | PASS |
| F1 | ML→1 | 🎙️→0.7 | 0.7 | 0.7 | PASS |
| F2 | MM→2 | 📄→1.0 | 2.0 | 2.0 | PASS |
| H1 | ML→1 | 🎙️→0.7 | 0.7 | 0.7 | PASS |
| H2 | HH→4 | 📄→1.0 | 4.0 | 4.0 | PASS |
| R1 | MM→2 | 📄→1.0 | 2.0 | 2.0 | PASS |
| zeros | none→0 | — | 0 | 0 | PASS |

Adjusted total = 4.0+3.0+2.0+4.0+2.1+0.7+0.7+0.7+2.0+0.7+4.0+2.0 = 25.9 ≈ 26
(reported 25.9≈26) PASS. Band 25-39 → MOAT STRENGTHENING (reported) PASS.

B1 note (MINOR, no impact): summary table types B1 as "📄/🎙️" and the scorecard
applies the 📄 1.0 multiplier. This is defensible — the backward-integration
claim rests on a genuine documented anchor (NADCAP heat-treatment approval,
📄 May 2026 call p.14) plus the documented consumption-ratio decline, with the
remaining special-processes language correctly held as 🎙️. Not a case of a
🎙️-only category being scored as 📄. Where evidence is mixed elsewhere (C1,
E2), the report chose the MORE conservative 🎙️ 0.7 multiplier, which is the
correct direction under the skeptical-evidence rule. No inflation detected.

### Tier-consistency guard (the "🎙️-only scored as 📄" trap)
Every category carrying a 1.0 multiplier has a real documented anchor: A1 (MHI
8-yr LTCPA + certs), A3 (restated-P&L consumption decline), B1 (NADCAP), B2
(certs/factories/contracts), F2 (delivered financial results), H2 (PW/RR/
Arabelle/BHEL signed agreements), R1 (BHEL PO + GTRE contract). No 🎙️-only or
🔍-only category received a 📄 multiplier. PASS.

### Completionist guard
Base rate 3-6; hard-stop re-examine at ≥12 active. Report scores 8 active
(A1,A3,B1,B2,C1,F2,H2,R1) — above the base rate, below the hard stop. The
explicit recount was nonetheless performed: "📄 recount performed: ... 17
documented items across 7 of the 8 active categories," with E2 correctly
excluded from the documented driver count as 🎙️-dominant, and the four
commentary-only categories (E1,E2,F1,H1) downgraded to Weak/Optionality rather
than scored active. This is exactly the discipline the guard demands. PASS.

### Combined assessment (6C/6D)
Injected Gate 0 block reused correctly (core 38 / moat 26 / grand 64, 6/12
FORTRESS). em_score 26 STRENGTHENING carried into the combined table.
combined_assessment = TURNAROUND, with full reasoning supplied as the matrix
requires for TURNAROUND rows: AVOID backward + STRENGTHENING (not EXPANSION)
forward does not clear the HIGH POTENTIAL bar (which needs a GOOD/AVERAGE
backward score or an EXPANSION forward score), landing correctly at TURNAROUND.
PASS.

MINOR (presentational): Section 5 narrative writes "six categories scoring
zero (A2,A4,B3,C2,D1,D2,G1,G2,H3 — nine, in fact)" — the "six" is a self-
corrected slip; the enumerated list and the "nine" are right. No scoring
impact.

### Emerging Moat verdict
All 36 rule checks reproduce the reported adjusted scores, the em_score, the
classification band, and the combined assessment. Multipliers and the
likelihood×impact matrix are applied exactly as written; the completionist
recount is performed; no evidence-tier inflation. Two MINORs (B1 mixed-type
label; one self-corrected count typo), neither of which moves a score.

═══════════════════════════════════════════════════════════════════
## PART 3 — VALUATION (B11/B10) — DEFERRED
═══════════════════════════════════════════════════════════════════
Out of scope for Phase 1. Stages 10 and 11 have not run. No Pillar 1/2/3,
UA/Amendment-3, dual-track, Hurdle Ratio, or SOM audit attempted. Valuation
section of the YAML is left pending per task instruction.

═══════════════════════════════════════════════════════════════════
## SUMMARY
═══════════════════════════════════════════════════════════════════
- Gate 0: 47 rules checked, 47 pass, 0 fail. 1 MINOR (B4 comparator).
- Emerging Moat: 36 rules checked, 36 pass, 0 fail. 2 MINOR.
- No misapplication changes any block score, deal-breaker, moat class,
  em_score, or classification. No CRITICAL, no MAJOR.
- acceptance_rate = 83/83 = 100% over the gate0 + emoat rules checked.
- recomputed_destination_pe: n/a (valuation deferred).
- recomputed_decision: concur with framework outcomes on both audited stages
  (Gate 0 AVOID / FORTRESS; Emerging Moat STRENGTHENING / TURNAROUND).
