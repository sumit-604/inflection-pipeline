# STAGE 12c — VERIFIER C: FRAMEWORK ADHERENCE (RATHIST)
Run date: 2026-07-20 | Model: claude-opus-4-8 | Emits: B12c
Scope: PHASE 1 — Gate 0 (B01) + Emerging Moat (B07) only. Valuation audit
(B11/B10) DEFERRED to phase 3; those blocks do not yet exist.

I audit rule application, not company quality and not raw source fidelity
(Verifier A owns whether a number appears in the source PDF). Where the
rules permit, I re-derived every block score from the inputs the stage
itself stated, then compared to the reported score.

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) COMPLIANCE
═══════════════════════════════════════════════════════════════════

Re-derivation uses the inputs as stated in 01-gate0.md; band edges from
prompts/01-gate-0-pipeline.md. "PASS" = reported score equals my
re-derived score under the stated band.

### BLOCK A — Return on Capital (reported 5/20)
| Metric | Stated input | Band applied | Re-derived | Reported | Verdict |
|---|---|---|---|---|---|
| A1 Median ROCE | median{13.49, 10.80}=12.15% | 10-14.9→1 | 1 | 1 | PASS |
| A2 Min single-yr ROCE | 10.80% (FY26) | 8-11.9→1 | 1 | 1 | PASS |
| A3 Median ROE | median{11.59, 9.25}=10.42% | <12→0 | 0 | 0 | PASS |
| A4 ROCE trend | 10.80 vs 13.49 = −2.69pp | decline 1-3pp→3 | 3 | 3 | PASS |

Block A = 5. PASS. ROCE formula applied per definition (EBIT ÷ (TA − CL));
EBIT taken as PBT+Interest, "computed" flag stated as required since no
source ROCE series exists. Restriction to FY25/FY26 (only years with a
current/non-current split) is a data-availability constraint, not a rule
breach — the stage marked FY17-FY24 NOT FOUND rather than estimating,
which the "never fill gaps" rule requires. A3 correctly excluded the
negative-net-worth years (FY17-FY23) and the FY24 recap artifact (108% ROE
on near-zero average net worth) as N/M rather than scoring them.

### BLOCK B — Cash Generation Quality (reported 5/20)
| Metric | Stated input | Band | Re-derived | Reported | Verdict |
|---|---|---|---|---|---|
| B1 Cum CFO/PAT | 309.36 / 202.27 = 1.53x | ≥1.00→5 | 5 | 5 | PASS |
| B2 FCF-pos years | 0 of 2 = 0% | <50→0 | 0 | 0 | PASS |
| B3 Cum FCF/PAT | −58.63 / 26.81 = −2.19 | negative→0 | 0 | 0 | PASS |
| B4 ΔWC Days | −5.49→+10.77 = +16.26d | increase >15→0 | 0 | 0 | PASS |

Block B = 5. PASS. Cumulative sums re-added independently: ΣCFO=309.36,
ΣPAT=202.27, ratio 1.529 → band ≥1.00. WC-days arithmetic re-checked on
Revenue basis (COGS not itemized, basis stated as required): FY25 −5.49,
FY26 +10.77. FY18/FY19 correctly excluded from B1 as NOT FOUND rather than
zero-filled. block_b_trend "improving (still negative)" is a permitted
narrative, not a scoring input.

### BLOCK C — Growth (reported 2/20)
| Metric | Stated input | Band | Re-derived | Reported | Verdict |
|---|---|---|---|---|---|
| C1 Rev CAGR | (716.05/381.75)^(1/9)−1 = 7.24% | 5-9.9→1 | 1 | 1 | PASS |
| C2 PAT CAGR | FY17 = −63.31 (neg endpoint) | N/M→0 | 0 | 0 | PASS |
| C3 Pos YoY yrs | 6 of 9 = 66.7% | 50-74→1 | 1 | 1 | PASS |
| C4 PAT−Rev CAGR | PAT CAGR N/M | N/M→C4=0 | 0 | 0 | PASS |

Block C = 2. PASS. CAGR edge rules honoured exactly: C2 negative-endpoint
→ N/M and scored 0 with the loss-to-profit swing recorded in data_notes,
no synthetic CAGR attempted; C4 forced to 0 per the explicit "when PAT
CAGR is N/M, score C4=0" rule. C3 decline count (FY18, FY20, FY24 = 3)
correctly places it in 50-74, and deal-breaker #7 (majority decline) was
correctly NOT triggered (3 of 9 is a minority).

### BLOCK D — Balance Sheet Strength (reported 9/20)
| Metric | Stated input | Band | Re-derived | Reported | Verdict |
|---|---|---|---|---|---|
| D1 ND/EBITDA | 42.54 / 28.46 = 1.50x | 1-2x→3 | 3 | 3 | PASS |
| D2 Int Coverage | 19.85 / 7.42 = 2.68x | 1.5-2.9→1 | 1 | 1 | PASS |
| D3 Debt/Equity | 44.80 / 149.89 = 0.30x | 0.1-0.5→4 | 4 | 4 | PASS |
| D4 Current Ratio | 144.61 / 139.33 = 1.04x | 1.0-1.19→1 | 1 | 1 | PASS |

Block D = 9. PASS. Not a bank/NBFC, so the standard (non-CAR/PCR) bands
apply — correctly used. The redeemable preference share Rs8.89cr note is
correctly flagged for downstream review rather than silently forced into
D3 (which would be a numbers question for Verifier A / a valuation input).

### BLOCK E — Shareholder Alignment (reported 3/20)
| Metric | Stated input | Band | Re-derived | Reported | Verdict |
|---|---|---|---|---|---|
| E1 Promoter holding | 41.30% (Mar-26) | 40-49.9→3 | 3 | 3 | PASS |
| E2 3yr change | 41.30 − 51.47 = −10.17pp | dec >3%→0 | 0 | 0 | PASS |
| E3 Pledge | NOT FOUND | N/A→0 | 0 | 0 | PASS |
| E4 ContLiab/NW | NOT FOUND | N/A→0 | 0 | 0 | PASS |

Block E = 3. PASS. E1/E2 rest on the operator-provided screener snapshot,
explicitly labelled NON-ANCHORED — that labelling is the correct handling,
not a rule breach. E3/E4 NOT FOUND → 0 per the "mark N/A and score 0"
rule; deal-breaker #5 (pledge >15%) correctly not applied since it cannot
be confirmed either way. NOTE for downstream: E1/E2 anchoring quality is
Verifier A's domain, not mine.

### CORE SCORE
5+5+2+9+3 = 24. PASS (matches reported 24/100).

### BLOCK F — Quantitative Moat (reported 5/60)
| Test | Stated input | Band | Reported | Verdict |
|---|---|---|---|---|
| M1 Pricing power | rev CAGR 7.25% (<10%), margin not declined | else→0 | 0 | PASS |
| M2 Cost advantage | 3.97% vs peer median 5.86% (below) | below→0 | 0 | PASS |
| M3 Capital eff. | FAT 7.28x, ROCE 10.80% (<12%) | else→0 | 0 | PASS |
| M4 Cust. stickiness | 3 decline years | 3+→0 | 0 | PASS |
| M5 Scale | Rathi 3rd of 4 in 3-peer set; full segment unknown | see below | 1 | MINOR FAIL |
| M6 Tech/R&D | N/A not in data | →0 | 0 | PASS |
| M7 Regulatory | unregulated segment | →0 | 0 | PASS |
| M8 Distribution | N/A not in data | →0 | 0 | PASS |
| M9 Brand | GM proxy 16.77% vs peer median 22.58% (below) | at/below→0 | 0 | PASS |
| M10 Switching | overall growth, 2+ decline yrs | →1 | 1 | PASS |
| M11 Network | FY20 base anomaly corrupts 2-window test | conservative→0 | 0 | PASS |
| M12 Neg WC/Float | FY25 −5.49d, FY26 +10.77d (2-yr sample) | see below | 3 | PASS (borderline) |

Moat total reported 5; moats present (≥3) = 1 (M12) → THIN.

**M5 — MINOR FAIL.** The stage marked M5 "PEER DATA NEEDED" (only 3 of an
admittedly larger listed segment were provided) yet scored it 1 on the
"top 5 mcap" rung. Block F's own rule is explicit: "If a test needs peer
data that is not provided, score 0 and mark PEER DATA NEEDED (never guess
peer figures)." Marking PEER DATA NEEDED and simultaneously scoring 1 is
internally inconsistent with that rule; the compliant score is 0. Impact:
moat total 5→4, grand total 29→28. Immaterial — M5=1 is not "present"
(needs ≥3), so the moat count (1, THIN) and the classification (AVOID) are
unchanged. Severity MINOR.

**M12 — borderline, accepted.** Scored 3 under "0-15 days consistently"
though FY25 (−5.49) sits below 0. One negative of two years does not meet
the "negative in majority" rung (=5), and negative WC is more favourable
than the 0-15 band, so 3 is a conservative, defensible read on a 2-year
sample (flagged as such). Not a fail. Immaterial to classification either
way (M12 is the sole "present" moat regardless).

### CLASSIFICATION, CONFIDENCE, DEAL-BREAKERS
| Rule | Applied | Verdict |
|---|---|---|
| Data confidence tier | 10yr P&L → "10+ full", no downgrade | PASS |
| history_downgrade | false (10yr ≥ 3) | PASS |
| Classification matrix | Core 24 <40 → AVOID | PASS |
| Moat classification | 1 present → THIN | PASS |
| DB#1 Block A <8 | 5<8 → cap GOOD [superseded by AVOID] | PASS |
| DB#2 Block B <8 | 5<8 → cap GOOD [superseded] | PASS |
| DB#3 Median ROCE <10% | 12.15% → not triggered | PASS |
| DB#4 Cum CFO/PAT <0.50 | 1.53 → not triggered | PASS |
| DB#5 Pledge >15% | unknown → not applied | PASS |
| DB#6 ND/EBITDA>3x AND IC<3x | ND/EBITDA 1.50 → not triggered | PASS |
| DB#7 Rev decline majority | 3 of 9 → not triggered | PASS |
| DB#8 PAT neg last 3yr | FY24-26 all positive → not triggered | PASS |
| DB#9 History <3yr | 10yr → not triggered | PASS |
| FLAG-GATE0 | classification ≤ AVERAGE + depressors → raised | PASS |

Deal-breaker logic is correct throughout: the two triggered caps (#1, #2)
cap at GOOD, but the matrix result (AVOID) is more restrictive, so they
are correctly noted as superseded rather than incorrectly relaxing the
verdict. Grand total 24+5=29 matches.

### GATE 0 VERDICT
Full re-derivation reproduces every block score. Classification AVOID is
correctly derived and I concur. One MINOR rule deviation (M5 scored 1
where the stated PEER-DATA-NEEDED rule requires 0); immaterial to the
classification. rules_checked = 46, fails = 1 (MINOR).

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### Coverage: all 21 categories addressed
A1,A2,A3,A4 | B1,B2,B3 | C1,C2 | D1,D2 | E1,E2 | F1,F2 | G1,G2 |
H1,H2,H3 | R1 = 21 rows present in both the Section 3 summary and the
Section 5 scorecard, each with evidence or an explicit "NO EVIDENCE
FOUND." PASS.

### Scorecard re-computation (raw × evidence-quality multiplier)
Matrix: HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0.
Multipliers: 📄 1.0, 🎙️ 0.7, 🔍 0.5.

| ID | L×I | Raw | Ev | × | Re-derived | Reported | Verdict |
|---|---|---|---|---|---|---|---|
| A3 | High×Low | 2 | 📄 | 1.0 | 2.0 | 2.0 | PASS |
| A4 | High×Low | 2 | 📄 | 1.0 | 2.0 | 2.0 | PASS |
| C1 | Med×Med | 2 | 🎙️ | 0.7 | 1.4 | 1.4 | PASS |
| E1 | Low×Low | 1 | 🔍 | 0.5 | 0.5 | 0.5 | PASS |
| H3 | High×Low | 2 | 📄 | 1.0 | 2.0 | 2.0 | PASS |
| R1 | Med×Med | 2 | 📄 | 1.0 | 2.0 | 2.0 | PASS |
| (all others) | no evidence | 0 | — | — | 0 | 0 | PASS |

Adjusted total = 2.0+2.0+1.4+0.5+2.0+2.0 = **9.9**. Matches reported 9.9.

### Classification floor
9.9 < 12 → NO MEANINGFUL EMERGING MOAT (block: "NONE"). PASS. The
12-24 MODEST / 25-39 STRENGTHENING / ≥40 EXPANSION thresholds are cited
correctly; the score does not clear even the MODEST floor.

### Evidence-tier consistency (the 🎙️-scored-as-📄 check)
No 🎙️-only category is scored at the 📄 1.0 multiplier. C1 (management
claim on repeat-customer share) is correctly held to 0.7x and excluded
from the active list as a single-source claim; E1 (location inference) to
0.5x. The four 1.0x categories each rest on a genuine 📄 anchor: A3 on the
completed/commissioned SS hot-charging capex (AR Annexure 1) not the
slipped TMT claim; A4 on issued BIS accreditations; H3 on issued GreenPro
certificates + the AR green-power figure; R1 on the gazetted safeguard
duty + BIS. PASS. F2 correctly scored 0 as *negative* execution evidence
(B05 credibility-C), not as neutral absence — a defensible reading, not a
scoring error.

### Completionist recount
Present and explicit: "📄 recount performed: 6 documented items across 4
categories." 4 active categories sit inside the stated 3-6 base rate; the
guard's inflation trap (12+ active) is nowhere near. PASS.

### FTTCP distinctness
The report opens with an explicit scope note that this is the Emerging
Moat scan (A1-R1, ~0-80 scale) and "is NOT FTTCP," and performs no FTTCP
ROCE verdict or FTTCP scoring. The two analyses are kept separate as the
CLAUDE.md non-negotiable and the prompt taxonomy note require. PASS.

### Combined assessment (6D) using injected Gate 0
Uses B01 as injected (core 24, AVOID, THIN, 1 moat). Backward AVOID +
forward NONE → combined AVOID, with the correct observation that a
transition setup requires a GOOD/AVERAGE backward score paired with
EXPANSION-grade forward evidence, which this name clears on neither axis.
PASS.

### Section 2C — capex-embedded growth: MINOR observation
capex_embedded_growth_pct set to 0 on a strict "contractually committed
per AR Note 1 = NIL" reading. The framework text is "total capex under
execution × historical fixed asset turnover." Capital Work-in-Progress of
Rs6.27cr (AR Note 15) is, on a literal reading, capex under execution; run
through the stated 6.03x FAT it implies ~Rs37.8cr (~7.5% of FY25 revenue),
versus the 0% reported. The stage disclosed the trailing-capex alternative
transparently and its strict basis is defensible, but the choice of NIL
over CWIP is a methodology judgment worth flagging. Impact: does NOT
change the EM score (9.9, driven by the 21-category scoring, not 2C) or
the classification; it feeds Pillar 3 in the valuation stage, so it is
carried as a MINOR note for phase-3 attention. Severity MINOR.

### EMERGING MOAT VERDICT
Scorecard fully reproduces (9.9). All 21 categories addressed, multipliers
correct, tiers consistent, recount performed, FTTCP kept distinct,
combined assessment correctly derived. One MINOR methodology observation
(2C NIL-vs-CWIP basis), immaterial to the EM classification.
rules_checked = 30, fails = 1 (MINOR).

═══════════════════════════════════════════════════════════════════
## PART 3 — VALUATION (B11/B10): DEFERRED
═══════════════════════════════════════════════════════════════════
Out of PHASE 1 scope. B10 and B11 do not yet exist. The continuous
Pillar 1 formula, FTTCP ROCE authority, single-credit rule, Pillar 2/3
mechanics, UA Amendment-3 order, dual-track carry, Hurdle Ratio, 4D
weights, and SOM cross-check are all PENDING PHASE 3 and were not audited
in this run.

═══════════════════════════════════════════════════════════════════
## CONSOLIDATED
═══════════════════════════════════════════════════════════════════
- Gate 0: 46 rules checked, 45 pass, 1 MINOR fail (M5). Classification
  AVOID re-derived and concurred.
- Emerging Moat: 30 rules checked, 29 pass, 1 MINOR fail (2C basis). Score
  9.9 / NONE re-derived and concurred.
- Valuation: pending phase 3.
- No CRITICAL, no MAJOR. recomputed_decision blank (concur with AVOID /
  NO MEANINGFUL EMERGING MOAT). recomputed_destination_pe blank
  (valuation deferred).
- Acceptance rate (rules passed ÷ checked, phase-1 sections) = 74/76 =
  97.4%.

Findings:
1. MINOR — Gate 0 M5 (Scale & Dominance): scored 1 while marked "PEER DATA
   NEEDED"; Block F rule requires 0 in that case. Moat total 5→4, grand
   total 29→28; classification unchanged (AVOID).
2. MINOR — Emerging Moat 2C: capex_embedded_growth_pct=0 uses the
   NIL-committed basis and excludes Rs6.27cr CWIP that is arguably "under
   execution" (~7.5% on the alternative reading). Immaterial to EM class;
   flagged for Pillar 3 in phase 3.
