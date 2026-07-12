# STAGE 12C: VERIFIER C — FRAMEWORK ADHERENCE (TATVA)
Run date: 2026-07-12 | Model: claude-opus-4-8 | Fresh context
Scope this run: PHASE 1 ONLY — Gate 0 (B01) and Emerging Moat (B07) compliance.
Valuation adherence (B10/B11) is DEFERRED to phase 3 and is NOT audited here.

I audit rule application only (not company quality, not raw number sourcing —
Verifier A owns numbers). Every block score below is independently re-derived
from the inputs stated in the report, using the thresholds as written in the
framework files.

═══════════════════════════════════════════════════════════════════
## FRAMEWORK 1 — GATE 0 (B01) vs prompts/01-gate-0-pipeline.md
═══════════════════════════════════════════════════════════════════

Sourcing caveat honoured per task instruction: Block E was sourced from the
FY24-25 AR (report explains why). I audit whether the thresholds were applied
to the values used, not whether the source was ideal.

### BLOCK A — Return on Capital (thresholds re-applied)

| Rule | Input used | Threshold band | Re-derived score | Report | Verdict |
|---|---|---|---|---|---|
| A1 Median ROCE | 18.42% (5th of 9 sorted) | 15-19.9 → 3 | 3 | 3 | PASS |
| A2 Min single-yr ROCE | 1.17% (FY25) | <8 → 0 | 0 | 0 | PASS |
| A3 Median ROE | 20.79% (5th of 9) | ≥20 → 5 | 5 | 5 | PASS |
| A4 ROCE trend latest v earliest | 6.64% vs 18.80% = -12.16pp | decline >5pp → 0 | 0 | 0 | PASS |
| Block A total | | | 8 | 8 | PASS |

Median re-check: sorted ROCE {1.17, 6.64, 6.69, 7.79, **18.42**, 18.80, 19.98,
24.89, 25.43} → median 18.42. ROE {0.77, 4.85, 5.53, 9.21, **20.79**, 29.59,
30.00, 36.84, 38.29} → median 20.79. Both correct. A3 closing-net-worth-only
basis for FY18 is permitted by the formula ("if opening net worth unavailable,
use closing and state so") and was stated. PASS.

### BLOCK B — Cash Generation Quality

| Rule | Input used | Threshold band | Re-derived | Report | Verdict |
|---|---|---|---|---|---|
| B1 Cumul CFO/PAT | ΣCFO 267.31 / ΣPAT 342.35 = 0.781 | 0.70-0.84 → 2 | 2 | 2 | PASS |
| B2 FCF-positive yrs | 0/8 = 0% | <50 → 0 | 0 | 0 | PASS |
| B3 Cumul FCF/PAT | −436.02/330.06 = −1.32 | <0.20/neg → 0 | 0 | 0 | PASS |
| B4 Δ WC Days latest v earliest | not computable (no FY18 payables) | N/A → 0 | 0 | 0 | PASS |
| Block B total | | | 2 | 2 | PASS |

Cumulative sums independently re-added: ΣCFO = 267.31, ΣPAT = 342.35, ratio
0.7808 → band 0.70-0.84 confirmed. B4 scored 0 under the operating rule "if a
data point is not available, mark N/A and score 0" — correct application, not
an estimate. PASS.

### BLOCK C — Growth (incl. CAGR edge rules)

| Rule | Input used | Threshold band | Re-derived | Report | Verdict |
|---|---|---|---|---|---|
| C1 Revenue CAGR | (505.86/135.81)^(1/8)−1 = 17.86% | 15-19.9 → 4 | 4 | 4 | PASS |
| C2 PAT CAGR | (42.05/12.29)^(1/8)−1 = 16.62% | 15-19.9 → 4 | 4 | 4 | PASS |
| C3 Positive YoY yrs | 5/8 = 62.5% | 50-74 → 1 | 1 | 1 | PASS |
| C4 PAT − Rev CAGR | 16.62 − 17.87 = −1.25pp | ±3pp → 3 | 3 | 3 | PASS |
| Block C total | | | 12 | 12 | PASS |

CAGR edge rules: no negative/zero endpoints, no loss-to-profit swing (PAT
positive every year — correctly noted). No synthetic CAGR attempted. C4 uses
real PAT CAGR (not N/M path). All edge rules honoured. PASS.

### BLOCK D — Balance Sheet Strength (latest = FY26)

| Rule | Input used | Threshold band | Re-derived | Report | Verdict |
|---|---|---|---|---|---|
| D1 Net Debt/EBITDA | 111.58/93.16 = 1.20x | 1-2x → 3 | 3 | 3 | PASS |
| D2 Interest Coverage | 59.86/2.85 = 21.0x | ≥10x → 5 | 5 | 5 | PASS |
| D3 Debt/Equity | 120.37/781.76 = 0.154 | 0.1-0.5 → 4 | 4 | 4 | PASS |
| D4 Current Ratio | 3495.12/2131.35 = 1.640 | 1.5-1.99 → 4 | 4 | 4 | PASS |
| Block D total | | | 16 | 16 | PASS |

Bank/NBFC override branch correctly NOT used (Tatva is not a financial). The
auto-picked "Pharma/CDMO" sector row is flagged in input_gaps but does not
affect D1/D2 since the override branch is only for banks/NBFC/insurance.
Correct. PASS.

### BLOCK E — Shareholder Alignment (AR-sourced this run)

| Rule | Input used | Threshold band | Re-derived | Report | Verdict |
|---|---|---|---|---|---|
| E1 Promoter holding | 72.02% (16,846,958/23,392,055) | ≥60 → 5 | 5 | 5 | PASS |
| E2 Promoter Δ 3yr | N/A (not in AR) | N/A → 0 | 0 | 0 | PASS |
| E3 Pledge | N/A (not in AR) | N/A → 0 | 0 | 0 | PASS |
| E4 Contingent liab/NW | 52.35/7388.24 = 0.71% | <5 → 5 | 5 | 5 | PASS |
| Block E total | | | 10 | 10 | PASS |

E1 holding fraction independently recomputed = 0.7202 → 72.02% ✓. E4 = 0.708%
→ band <5% ✓. E2/E3 scored 0 under "never estimate a missing number; N/A is the
only valid fill" — this is the correct rule, not a threshold misapplication.
PASS.

### BLOCK F — Quantitative Moat (M1-M12)

| Rule | Basis | Re-derived | Report | Verdict |
|---|---|---|---|---|
| M1 Pricing Power | OPM +1.36pp (stable ±2pp) AND rev CAGR 17.87% ≥10 → 3 | 3 | 3 | PASS |
| M2 Cost Advantage | 18.42% vs peer median 25.90% → below → 0 | 0 | 0 | PASS |
| M3 Capital Efficiency | FAT 0.83x <1x → 0 | 0 | 0 | PASS |
| M4 Customer Stickiness | 3 decline yrs → 0 | 0 | 0 | PASS |
| M5 Scale & Dominance | 4th of 5 mcap, top-5 → 1 | 1 | 1 | PASS |
| M6 Technology/R&D | R&D N/A → 0 | 0 | 0 | PASS |
| M7 Regulatory/License | unregulated → 0 | 0 | 0 | PASS |
| M8 Distribution | N/A → 0 | 0 | 0 | PASS |
| M9 Brand | GM proxy 46.78% vs median 51.34% → at/below → 0 | 0 | 0 | PASS |
| M10 Switching Costs | growth, 2+ decline yrs → 1 | 1 | 1 | PASS |
| M11 Network Effects | latest 3yr 6.10% < prior 17.19%, <20% → 0 | 0 | 0 | PASS |
| M12 Negative WC/Float | WC days >45 → 0 | 0 | 0 | PASS |
| Block F total | | 5 | 5 | PASS |

Peer OPM median re-check: {6.20, 15.93, 35.87, 37.12} → (15.93+35.87)/2 = 25.90 ✓.
Peer GM proxy median: {25.98, 47.09, 55.58, 62.40} → (47.09+55.58)/2 = 51.34 ✓.
Moats present (≥3): M1 only → 1 → classification "1 = THIN" ✓. "PEER DATA NEEDED"
correctly not invoked (peer exports were sufficient; M6 gap is Tatva's own
missing R&D line, correctly distinguished). PASS.

### CLASSIFICATION / CONFIDENCE / DEAL-BREAKERS

| Rule | Basis | Re-derived | Report | Verdict |
|---|---|---|---|---|
| Core score | 8+2+12+16+10 | 48 | 48 | PASS |
| Grand total | 48 + 5 | 53 | 53 | PASS |
| Data confidence | 9 yrs → 7-9 "moderate" | moderate | moderate | PASS |
| History downgrade | 9 yrs, not 3-4 LIMITED | false | false | PASS |
| Classification matrix | Core 40-59 → AVERAGE | AVERAGE | AVERAGE | PASS |
| DB1 Block A<8 | A=8, boundary, not <8 | not triggered | not triggered | PASS |
| DB2 Block B<8 | B=2<8 → max GOOD (non-binding vs AVERAGE) | triggered/non-binding | same | PASS |
| DB3 Median ROCE<10% | 18.42% | no | no | PASS |
| DB4 Cumul CFO/PAT<0.50 | 0.781 | no | no | PASS |
| DB5 Pledge>15% | not assessable (absent) | cannot trigger | NOT ASSESSABLE | PASS |
| DB6 ND/EBITDA>3x AND IC<3x | 1.20x / 21.0x | no | no | PASS |
| DB7 Rev decline majority | 3/8 = 37.5% | no | no | PASS |
| DB8 PAT neg last 3yr | FY24/25/26 positive | no | no | PASS |
| DB9 History<3yr | 9 yrs | no | no | PASS |
| FLAG-GATE0 emitted | class ≤AVERAGE + historical depressors | required, present | present | PASS |

DB1 boundary reading is correct as written ("Block A <8", 8 is not <8). DB2 cap
(max GOOD) is correctly noted non-binding since the matrix already yields the
lower AVERAGE. DB5 correctly left unresolved rather than defaulted — consistent
with the never-estimate rule. Classification AVERAGE is the governing result.
FLAG-GATE0 correctly emitted per the YAML trigger (classification ≤ AVERAGE with
identified historical depressors). PASS.

**GATE 0 RESULT: 46 rules checked, 46 PASS, 0 FAIL. Fully compliant as written.**

═══════════════════════════════════════════════════════════════════
## FRAMEWORK 2 — EMERGING MOAT (B07) vs prompts/07-emerging-moat-pipeline.md
═══════════════════════════════════════════════════════════════════

### Coverage — all 21 categories addressed

Section 3 summary table + Section 4 (R1) list all 21 rows: A1-A4, B1-B3, C1-C2,
D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, R1. Every row carries either an evidence
entry or explicit "NO EVIDENCE FOUND" / negative finding. No category skipped,
no force-fit. PASS.

### Scorecard — raw matrix and evidence multiplier per scored row

Matrix as written: HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0.
Multipliers: 📄 1.0, 🎙️ 0.7, 🔍 0.5.

| ID | Likelihood×Impact | Raw (re-derived) | Evid tier | Mult | Adjusted (re-derived) | Report | Verdict |
|---|---|---|---|---|---|---|---|
| A1 | M×H = MH | 3 | 🎙️ dominant | 0.7 | 2.10 | 2.1 | PASS |
| A3 | H×M = HM | 3 | 📄 | 1.0 | 3.00 | 3.0 | PASS |
| A4 | H×L = HL | 2 | 📄 | 1.0 | 2.00 | 2.0 | PASS |
| B2 | M×M = MM | 2 | 🎙️ | 0.7 | 1.40 | 1.4 | PASS |
| C1 | L×M = LM | 1 | 🎙️ | 0.7 | 0.70 | 0.7 | PASS |
| E1 | M×M = MM | 2 | 🎙️ | 0.7 | 1.40 | 1.4 | PASS |
| E2 | M×H = MH | 3 | 🎙️ | 0.7 | 2.10 | 2.1 | PASS |
| H1 | M×L = ML | 1 | 🎙️ | 0.7 | 0.70 | 0.7 | PASS |
| H3 | H×M = HM | 3 | 📄 | 1.0 | 3.00 | 3.0 | PASS |
| R1 | H×H = HH | 4 | 🎙️ | 0.7 | 2.80 | 2.8 | PASS |
| Zero rows (A2,B1,B3,C2,D1,D2,F1,F2,G1,G2,H2) | none | 0 | — | — | 0 | 0 | PASS |
| **TOTAL** | | | | | **19.20** | 19.2 | PASS |

Every raw score matches the likelihood×impact matrix; every multiplier matches
the stated evidence tier; adjusted total re-sums to 19.2. Classification band
12-24 → MODEST MOAT DEVELOPMENT — correct. PASS.

### 🎙️-only-scored-as-📄 test

Checked each 1.0x row (A3, A4, H3): all three rest on genuinely documented
evidence (A3 — AR Annexure F process transcription + R&D spend; A4 — 12 new
products + facility flexibility, AR/IP; H3 — ZLD, EcoVadis, TfS, ISO, quantified
metrics). No 🎙️-only category received a 1.0x multiplier. Mixed 🎙️/📄
categories (A1, E1, E2, R1) were all scored at the conservative 0.7x — the
skeptical read the framework demands. No inflation. PASS.

### Completionist guard / recount

Only 6 categories rated Strong/Moderate (well under the 12-active trigger), so
the guard did not force a downgrade — but the explicit "📄 recount performed"
line is present as required. PASS on performing the recount.

MINOR inconsistency: the recount narrative states "**22** distinct 📄-documented
evidence items" (Section 3 + YAML completionist_recount), while the YAML
`evidence_mix.documented` = **24**. Both purport to count documented items; they
differ by 2. Does not change any score, the multiplier assignment, or the MODEST
classification. Flagged MINOR (presentational count reconciliation).

### Category rules

| Rule | Verdict |
|---|---|
| All 21 categories addressed / NO EVIDENCE | PASS |
| Evidence taxonomy applied to each item (📄/🎙️/🔍) | PASS |
| Raw score = likelihood×impact matrix | PASS |
| Multiplier = stated evidence tier | PASS |
| Adjusted total re-sums | PASS |
| Classification band applied (12-24 MODEST) | PASS |
| Completionist recount performed | PASS |
| No 🎙️-only category scored as 📄 | PASS |
| active_categories = Strong/Moderate rows only (6) | PASS |
| completionist_recount count vs evidence_mix.documented | FAIL (MINOR) |

**EMERGING MOAT RESULT: 26 rules checked, 25 PASS, 1 FAIL (MINOR). Substantively
compliant; the single fail is a non-material count-reconciliation gap.**

═══════════════════════════════════════════════════════════════════
## VALUATION (B10/B11) — PENDING PHASE 3
═══════════════════════════════════════════════════════════════════

Out of scope this run. B10/B11 do not yet exist. RULE 4 not applied. No
destination-PE or decision recompute performed. Section left pending.

═══════════════════════════════════════════════════════════════════
## SUMMARY
═══════════════════════════════════════════════════════════════════

- Gate 0: every block score independently re-derived to the reported value; the
  classification matrix, data-confidence adjustment, all nine deal-breakers, and
  the CAGR edge rules were applied exactly as written. 0 fails.
- Emerging Moat: 21/21 categories covered, all multipliers and raw matrix
  values correct, no evidence-tier inflation, recount performed. One MINOR
  internal count inconsistency (22 vs 24 documented items).
- No CRITICAL, no MAJOR. Neither framework misapplication changes any score,
  band, or classification. No REWORK trigger from this verifier.

```yaml
stage: B12c
company: "TATVA"
run_date: "2026-07-12"
model: claude-opus-4-8
status: complete
gate0:
  rules_checked: 46
  fails: []
emoat:
  rules_checked: 26
  fails:
    - {severity: "MINOR", rule: "completionist recount vs evidence_mix", detail: "completionist_recount states 22 documented items; YAML evidence_mix.documented=24. Off by 2; no score/classification impact."}
valuation: {rules_checked: 0, fails: [], status: "PENDING PHASE 3"}
recomputed_destination_pe: ""
recomputed_decision: ""
findings:
  - {severity: "MINOR", location: "B07 Section 3 recount line / YAML evidence_mix.documented", claimed: "22 documented items (recount) vs 24 (evidence_mix)", note: "Internal count inconsistency, off by 2; MODEST classification and all row scores unaffected."}
critical_count: 0
major_count: 0
minor_count: 1
acceptance_rate: 99   # 71 of 72 audited rules passed (gate0 46/46 + emoat 25/26)
```
