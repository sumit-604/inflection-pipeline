# B12c — VERIFIER C: FRAMEWORK ADHERENCE (PHASE-1 SCOPE)
Company: CMS Info Systems Ltd (CMSINFO) | Run date: 2026-08-29 | Model: claude-opus-4-8

Scope: PHASE 1 only. Gate 0 (B01) adherence and Emerging Moat (B07)
adherence. Valuation adherence (B10/B11) is deferred to phase 3 and is
marked PENDING below. Valuation framework docs were not loaded (dead
context in phase 1).

Rule sources audited against:
- Gate 0: prompts/01-gate-0-pipeline.md
- Emerging Moat: prompts/07-emerging-moat-pipeline.md

Reports audited:
- outputs/reports/01-gate0.md
- outputs/reports/07-emoat.md

I audit rule application, not company quality and not source-number
existence (Verifier A owns numbers). Every block below is re-derived from
the report's own stated inputs against the rule file's thresholds.

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### BLOCK A — Return on Capital (Max 20) — PASS

| Item | Stated input | Rule band | Score | Re-derived | Verdict |
|---|---|---|---|---|---|
| A1 Median ROCE | median(16.6, 25.2, 25.4)=25.2% | ≥25%=5 | 5 | 5 | PASS |
| A2 Min single-yr ROCE | 16.6% (FY26) | ≥15%=5 | 5 | 5 | PASS |
| A3 Median ROE | 5th-of-9 sorted=17.68% | 15-19.9%=4 | 4 | 4 | PASS |
| A4 ROCE trend | 16.6% vs 25.4%, -8.8pp | decline >5pp=0 | 0 | 0 | PASS |

Re-sort of the 9 ROE values (11.89, 12.91, 13.54, 16.88, **17.68**, 18.37,
19.79, 19.996, 21.09) confirms median 17.68%. A4 correctly uses the
"earliest anchored" (FY24) endpoint; the ROCE window is only 3 clean years,
disclosed. Block A = 14. Concur.

### BLOCK B — Cash Generation Quality (Max 20) — PASS

| Item | Stated input | Rule band | Score | Verdict |
|---|---|---|---|---|
| B1 Cumul CFO/PAT | 1.298x | ≥1.00=5 | 5 | PASS |
| B2 FCF-positive years | 1 of 2 = 50% | 50-74%=2 | 2 | PASS |
| B3 Cumul FCF/PAT | 0.4565 | 0.40-0.59=3 | 3 | PASS |
| B4 WC-days change | +13.38 days | increased 5-15=1 | 1 | PASS |

Windows for B2/B3/B4 are 2 years (FY25-26) with NOT FOUND correctly
recorded for FY18-24 (no capex split, no payables line). Rule 5 (never fill
gaps) honored. Block B = 11. Concur.

### BLOCK C — Growth (Max 20) — PASS

| Item | Stated input | Rule band | Score | Verdict |
|---|---|---|---|---|
| C1 Revenue CAGR | 12.38% (8yr) | 10-14.9%=3 | 3 | PASS |
| C2 PAT CAGR | 18.11% (8yr) | 15-19.9%=4 | 4 | PASS |
| C3 Positive YoY | 7 of 8 = 87.5% | 75-99%=3 | 3 | PASS |
| C4 PAT−Rev CAGR | +5.73pp | ≥+3pp=5 | 5 | PASS |

CAGR edge rules: no negative/zero endpoints, no loss-to-profit swing (PAT
positive every year), so no N/M treatment required. C4 computed normally
(PAT CAGR not N/M). Block C = 15. Concur.

### BLOCK D — Balance Sheet Strength (Max 20) — PASS

| Item | Stated input | Rule band | Score | Verdict |
|---|---|---|---|---|
| D1 Net Debt/EBITDA | net cash ~Rs 307 Cr | net cash=5 | 5 | PASS |
| D2 Interest Coverage | 21.81x | ≥10x=5 | 5 | PASS |
| D3 Debt/Equity | 0.091 (lease basis) | <0.1=5 | 5 | PASS |
| D4 Current Ratio | 2.56x | ≥2.0=5 | 5 | PASS |

CMS is not a bank/NBFC, so the standard (not CAR/PCR) bands correctly
apply. Block D = 20. Concur.

### BLOCK E — Shareholder Alignment (Max 20) — FAIL (one item)

| Item | Stated input | Rule band | Score | Framework-correct | Verdict |
|---|---|---|---|---|---|
| E1 Promoter holding | 0.00%; FII+DII 58.70% | prof-managed alt-path: 3 if FII+DII>50% | 3 | 3 | PASS |
| E2 Promoter chg 3yr | 26.69% -> 0.00%, -26.69pp | decreased >3% = **0** | **3** | **0** | **FAIL** |
| E3 Promoter pledge | 0% (no promoter) | 0%=5 | 5 | 5 | PASS (literal) |
| E4 Cont. liab/NW | 2.28% | <5%=5 | 5 | 5 | PASS |

**E1** — the alt-path "Professionally managed: 3 if FII+DII >50%" is an
explicit rule provision. 22.70 + 36.00 = 58.70% > 50%. Score 3 is
legitimate. PASS.

**E2 — DEVIATION.** The report itself states the literal formula reads 0
("decline of 26.69pp... decreased >3% = 0"), then scores **3 "(neutral)"**
on a qualitative rationale (orderly PE-sponsor exit, not insider distress,
no promoter register to test). The rule set provides an alt-path only for
E1, none for E2. Gate 0 operating rule 2 is explicit: "No qualitative
judgments. Only numbers and the scoring rules provided." Rule 5 scores a
truly-absent data point as 0 (not 3); here the data is present and defined
(a real 26.69% -> 0% decline of a formerly-classified promoter), so the
formula output is 0. Framework-correct E2 = 0. The maker was transparent
about the override (data_notes item 8), but transparency does not make the
score compliant. **Impact: +3 inflation.**

**E3** — 0% pledge is literally true (0%=5). No promoter exists to pledge,
so the item is vacuous, but the recorded value is factually 0% and the
formula maps 0% -> 5. Within the letter of the rule; noted as MINOR context
(the same no-promoter structure that zeroes E2 is being scored top-band at
E3), not a fail.

Block E as scored = 16. Framework-correct = 13.

### MOAT BLOCK F — Quantitative Moat (Max 60) — PASS

Re-derivation of each test against its rule:
- M1 5: margin +8.9pp (≥2pp) AND rev CAGR 12.38% (≥10%) = 5. Correct. (Ind
  AS 116 caveat noted; rule does not adjust, so 5 stands as written.)
- M2 0: PEER DATA NEEDED, scored 0 per rule (never guess peer figures). Correct.
- M3 3: FAT 2.15x (>2x) AND ROCE 16.6% (>15%) = 3. Correct (top band needs >3x AND >20%).
- M4 3: 1 decline year fully recovered = 3. Correct (top band needs 0 decline + stable DSO).
- M5 0: PEER DATA NEEDED. Correct.
- M6 0: no R&D disclosure; correctly scored 0 as absence, not PEER DATA NEEDED. Correct.
- M7 0: PEER DATA NEEDED (player count). Correct.
- M8 1: reach quantified but growth unverifiable and rev CAGR 12.38% < 15%
  fails the "network growing AND ≥15%" band; conservative 1. Acceptable —
  no band exists for "quantified-but-growth-unverified"; 1 vs 0 is a defensible read.
- M9 0: PEER DATA NEEDED. Correct.
- M10 0: 1 decline year AND DSO +58pp (>10) -> else = 0. Correct.
- M11 0: ≥6yr available; latest 3yr CAGR 9.12% < prior 11.46% (not accelerating), neither ≥20 nor >15 -> 0. Correct.
- M12 0: WC days 81.9/95.3 (>45) -> 0. Correct.

Sum = 5+0+3+3+0+0+0+1+0+0+0+0 = 12. Moats present (≥3): M1, M3, M4 = 3.
Moat classification: 2-3 present -> MODERATE. Correct. Block F = 12/60. Concur.

### CORE, GRAND TOTAL, CLASSIFICATION

- Core as scored: A14 + B11 + C15 + D20 + E16 = **76**. Arithmetic correct.
- Grand total: 76 + 12 = **88 / 160**. Internally consistent with blocks
  A..E and moat 12/60 **as scored**. The 88 is arithmetically sound.
- Framework-correct (E2 = 0): core = **73**, grand total = **85**.
- Classification matrix: core 76 (60-79) + MODERATE = "Core 60-79 + else =
  GOOD" -> **GOOD**. Correct.
- With the corrected core 73 (still 60-79) + MODERATE -> **GOOD** unchanged.
  The E2 deviation does NOT flip the classification. Decision survives.

### DEAL-BREAKERS — PASS

All 9 assessed and correctly negative:
1 Block A<8 (14) no | 2 Block B<8 (11) no | 3 median ROCE<10% (25.2%) no |
4 cumul CFO/PAT<0.50 (1.298) no | 5 pledge>15% (0%) no | 6 ND/EBITDA>3x AND
IC<3x (net cash, 21.81x) no | 7 revenue declined majority (1 of 8) no |
8 PAT negative last 3yr (positive) no | 9 history<3yr (9) no.
No deal-breaker triggered. The "state which years drive any deal-breaker"
instruction is moot (none triggered). Correct.

### DATA CONFIDENCE — PASS
9 years -> 7-9 "moderate", no downgrade (downgrade reserved for 3-4 yrs).
Per-metric short windows flagged but do not trigger the history-based
tier downgrade, which governs total years. Correct application.

### GATE 0 VERDICT
One MAJOR framework deviation (E2 qualitative override, +3 inflation,
classification unchanged). All other blocks, the moat block, the
classification matrix, all deal-breakers, CAGR edge rules and data-
confidence logic applied as written. 12 of 13 rule-checks pass.

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### COMPLETENESS — PASS
All 23 rows present (A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2,
H1-H3, I1-I2, R1). Every zero-score row carries "NO EVIDENCE FOUND",
"N/A", or a stated double-count/negative-evidence reason. No forced fits.
Categories 21 (I1) and 22 (I2) present per Verifier C rule 8.

### RAW SCORE (L×I MATRIX) — PASS
Matrix HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0. Re-checked each
active row: A3 HM=3, A4 LL=1, B1 MM=2, C1 HH=4, C2 MM=2, D1 HH=4, D2 HM=3,
F1 LL=1, H1 MM=2, R1 MM=2. All consistent with the matrix.

### EVIDENCE MULTIPLIERS — PASS
D=1.0, C=0.7, I=0.5. Row adjusted values recomputed:
A3 3.0 | A4 0.7 | B1 2.0 | C1 4.0 | C2 2.0 | D1 4.0 | D2 3.0 | F1 1.0 |
H1 2.0 | R1 1.4. Sum = **23.1**. Matches report (23.1 ≈ 23). Concur.

### STRENGTHENING THRESHOLD (23 vs 25) — PASS
Bands are ABSOLUTE (operator ruling 20-Aug-2026): ≥40 EXPANSION | 25-39
STRENGTHENING | 12-24 MODEST | <12 NONE. Adjusted total 23.1 falls in
12-24 -> **MODEST MOAT DEVELOPMENT**. Correct. The report did NOT round
23.1 up to cross 25, and did NOT claim the "EM ≥25" UA qualifier. It
explicitly names that a more generous read of C2/H1 would cross 25 and
declines it on evidence-discipline grounds. That is legitimate analyst
discretion inside the raw-score step, not threshold misuse. No rescale
applied (correct — bands are absolute).

### I1 / I2 (CATEGORIES 21/22) — PASS
- I1 scored 0: part (a) is a hiring-composition claim, part (b) has zero
  evidence. Rule requires both legs with (b) carrying ≥1 documented source
  for any positive band; correctly 0.
- I2 scored 0: no specific named sacrifice; honest answer is "execution
  lead, not configuration." Correctly 0.
- I1/I2 contribution stated separately as 0.0 (feeds the review
  checkpoint), as the rule requires. The 23.1 threshold read is driven
  entirely by the pre-existing 21 categories + R1, not by the I-family.

### COMPLETIONIST RECOUNT — PASS
"📄 recount performed: 19 documented items across 7 Strong/Moderate
categories." Active (Strong/Moderate) count = 7, below the 12-category
guard trigger. Recount performed explicitly and the above-base-rate count
(7 vs 3-6) is addressed with per-category sourcing. Rule satisfied.

### DOUBLE-COUNT AVOIDANCE — PASS
G1 (war chest) held to 0 to avoid re-crediting Gate-0 Block D quality; B3
(supply-chain network effect) routed to D2 to avoid crediting the same
ALGO fact twice. Both consistent with the operating rules. Correct.

### EVIDENCE-TIER CONSISTENCY — PASS with one MINOR
No 🎙️/C-only category is scored as if 📄/D. Spot check: R1 is a pending
IBA claim, correctly tagged C (0.7x). A4 a "seamless modular" claim,
correctly C (0.7x). D1 correctly separates the (D) underlying data facts
from the (C) "no competitor can replicate" line and scores only the D fact.
- MINOR: the "70% AI/ML" figure is tagged **(D)** at F1 but **(C)** at I1.
  Same figure, two tiers. Immaterial: F1 raw is LL=1 either way; a C
  re-tag would move F1 from 1.0 to 0.7, a 0.3 swing that leaves the total
  at ~22.8, still MODEST. Does not approach the 25 threshold.

### COMBINED ASSESSMENT (6C / 6D) — PASS (judgment)
6C carries the injected Gate-0 block (core 76, grand_total 88,
moats_confirmed 3, moat_score 12/60, GOOD) against em_score ≈23 MODEST.
Note: the Gate-0 figures 6C inherits embed the E2 +3 inflation (Part 1);
the emoat stage inherited them and is not at fault, but the propagation is
recorded. 6D classifies **GOOD+**: GOOD backward base plus broader-than-
average forward evidence, below the STRENGTHENING/HIGH-POTENTIAL bar. The
stage-7 matrix names the classification set but gives no deterministic
threshold table for each backward×forward pair, so GOOD+ is a defensible
half-tier judgment, not a mechanical rule violation. HIGH POTENTIAL was
correctly withheld (forward is MODEST, not EXPANSION/STRENGTHENING).

### EMERGING MOAT VERDICT
All scoring mechanics (23-row completeness, L×I matrix, D/C/I multipliers,
23.1 total, the 25-point band, I1/I2 zero-scoring, the completionist
recount, double-count avoidance) applied as written. One MINOR evidence-
tier tagging inconsistency (F1 vs I1), immaterial to the band. No
threshold misuse.

═══════════════════════════════════════════════════════════════════
## PART 3 — STRUCTURAL NOTE (both reports)
═══════════════════════════════════════════════════════════════════
Both artifacts as provided end without the required closing fenced YAML
block (01-gate0.md ends at data-note 9; 07-emoat.md ends at "Input gaps
carried forward"). Each stage prompt mandates a terminal YAML block.
Recorded as NOT FOUND in the provided artifacts, severity MINOR: the
emoat 6C table cites the B01 YAML fields verbatim (core_score 76,
grand_total 88, moats_confirmed 3, moat_score 12/60), so the B01 YAML
existed at runtime; the absence here is most likely a capture/excerpt
artifact rather than a missing output. Machine-readable field consistency
could not be verified against the narrative; the narrative arithmetic was
verified instead (see Parts 1-2) and is internally consistent.

═══════════════════════════════════════════════════════════════════
## PART 4 — VALUATION (B10/B11) — PENDING PHASE 3
═══════════════════════════════════════════════════════════════════
Not audited. B10/B11 do not exist in this run yet; the valuation framework
docs were deliberately not loaded (dead context in phase 1). Deferred to
the phase-3 valuation-scope invocation.

═══════════════════════════════════════════════════════════════════
## SUMMARY
═══════════════════════════════════════════════════════════════════
- CRITICAL: 0
- MAJOR: 1 (Gate 0 E2 qualitative override; +3 core inflation;
  classification GOOD unchanged)
- MINOR: 3 (Gate 0 YAML absent in artifact; Emoat YAML absent in artifact;
  Emoat F1 evidence-tier tag inconsistency)
- Recomputed core: 73 (vs 76 as scored). Recomputed grand total: 85 (vs
  88). Recomputed classification: GOOD (unchanged). No decision flips.
- Phase-1 framework adherence: 24 of 25 rule-checks pass (96%).

```yaml
stage: B12c
company: "CMSINFO"
run_date: "2026-08-29"
model: claude-opus-4-8
status: complete
scope: phase-1  # Gate 0 + Emerging Moat only; valuation deferred to phase 3
gate0:
  rules_checked: 13
  fails:
    - {severity: "MAJOR", item: "E2 promoter-holding-change", rule: "Block E / operating-rule-2 (no qualitative judgments)", location: "01-gate0.md Block E, E2", scored: 3, framework_correct: 0, impact: "+3 core inflation (76->73, grand total 88->85); classification GOOD unchanged"}
emoat:
  rules_checked: 12
  fails: []
valuation:
  status: pending-phase-3
  rules_checked: 0
  fails: []
  note: "B10/B11 not present this run; valuation framework docs not loaded in phase-1 scope"
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: ["NOT IN PHASE-1 SCOPE (stage 13 artifact not audited)"]}
recomputed_destination_pe: ""   # not in phase-1 scope
recomputed_decision: "GATE 0: GOOD (unchanged); corrected core 73 vs scored 76, corrected grand total 85 vs scored 88 — band and classification do not move"
findings:
  - {severity: "MAJOR", location: "01-gate0.md / Block E / E2", description: "E2 scored 3 (neutral) after the report states the literal formula yields 0 (26.69% -> 0.00%, decreased >3% = 0). No E2 alt-path exists in the rules (only E1 has one); operating rule 2 forbids qualitative judgments. Framework-correct E2 = 0. Core 76->73, grand total 88->85, classification GOOD unchanged."}
  - {severity: "MINOR", location: "01-gate0.md / end-of-file", description: "Required closing fenced YAML block not present in the provided artifact; likely a capture artifact (B01 YAML fields are cited verbatim in 07-emoat 6C, so it existed at runtime). Narrative arithmetic verified instead and is internally consistent."}
  - {severity: "MINOR", location: "07-emoat.md / end-of-file", description: "Required closing fenced YAML block not present in the provided artifact. Narrative scorecard (23 rows, adjusted total 23.1) verified instead."}
  - {severity: "MINOR", location: "07-emoat.md / F1 vs I1", description: "The '70% AI/ML' figure is tagged (D) at F1 but (C) at I1. Immaterial: a C re-tag moves F1 1.0->0.7, total ~22.8, still MODEST (12-24). Does not approach the 25-point STRENGTHENING threshold."}
critical_count: 0
major_count: 1
minor_count: 3
acceptance_rate: 96   # phase-1 rule-checks passed / checked (24/25)
framework_adherence_phase1_pct: 96
```
