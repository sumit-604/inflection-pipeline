# STAGE 12c — VERIFIER C: FRAMEWORK ADHERENCE (PHASE 1 SCOPE)
## Shyam Metalics & Energy Ltd (SHYAMMETL) — Run date 2026-07-19
Model: claude-opus-4-8 | Emits: B12c

**Scope this run:** Gate 0 (B01) compliance + Emerging Moat (B07) compliance ONLY.
The valuation-adherence audit (B11/B10) is DEFERRED to phase 3 — those artifacts
do not exist yet — and is marked `pending phase 3` in the YAML. I audit rule
application, not company quality and not raw source-fidelity of numbers (Verifier
A owns whether a number exists in the source PDF at its anchor).

---

## PART 1 — GATE 0 (B01) COMPLIANCE

Framework authority: `prompts/01-gate-0-pipeline.md`. Every block score re-derived
from the stated inputs against the stated thresholds.

### Block A — Return on Capital (re-derived)

| Rule | Framework threshold | Report input | Re-derived band | Report score | Verdict |
|---|---|---|---|---|---|
| A1 Median ROCE | 10-14.9=1 | sorted median 13.38% | 1 | 1 | PASS |
| A2 Min single-yr ROCE | 8-11.9=1 | 9.67% (FY20) | 1 | 1 | PASS |
| A3 Median ROE | 12-14.9=2 | sorted median 13.01% | 2 | 2 | PASS |
| A4 ROCE trend | decline >5pp=0 | 13.21% vs 23.38% = -10.17pp | 0 | 0 | PASS |

Median ROCE check: sorted [9.67, 10.48, 12.21, 13.21, 13.38, 23.38, 25.22, 25.74,
37.44] → 5th value = 13.38%. Median ROE sorted [8.99, 9.70, 12.23, 12.80, 13.01,
22.89, 26.11, 27.82, 36.43] → 13.01%. **Block A = 4. PASS.**

Methodology note (see Finding GA-1): ROCE was computed from a proxy Capital Employed
(Equity + Reserves + Borrowings) rather than the framework formula's TA−CL or the
source's own ROCE, because the current/non-current liability split is absent for
FY18-24 in the provided Data_Sheet. Documented and cross-checked (proxy CE within
1.9-3.1% of audited TA−CL for FY25/FY26). Deviation from formula-as-written but data-
justified; no band change.

### Block B — Cash Generation (re-derived)

| Rule | Framework | Report | Re-derived | Score | Verdict |
|---|---|---|---|---|---|
| B1 Cum CFO/PAT | ≥1.00=5 | 10,530.30/7,802.43 | 1.35 → 5 | 5 | PASS |
| B2 FCF-pos years | <50%=0 | 0/2 assessable | 0 | 0 | PASS |
| B3 Cum FCF/PAT | negative=0 | -0.53 (partial) | 0 | 0 | PASS |
| B4 WC-days change | missing→0 | Trade Payables NOT FOUND FY18 | 0 | 0 | PASS |

Cumulative CFO sum verified = 10,530.30; cumulative PAT = 7,802.43; ratio 1.3496.
B2/B3/B4 all scored 0 on genuine data gaps (Capex NOT FOUND FY18-24; Trade Payables
NOT FOUND FY18-24), consistent with operating rule 5 ("mark N/A and score 0; never
estimate"). Source conflict on FY25 CFO (Data_Sheet 1,964.15 vs audited 1,713.43) was
flagged; substituting the audited figure yields cumulative ratio 1.32, still ≥1.00 → 5,
no score change. **Block B = 5. PASS.**

### Block C — Growth (re-derived)

| Rule | Framework | Report | Re-derived | Score | Verdict |
|---|---|---|---|---|---|
| C1 Rev CAGR | ≥20%=5 | (18,552.21/3,747.16)^(1/8)-1 | 22.14% → 5 | 5 | PASS |
| C2 PAT CAGR | 10-14.9=3 | (1,070.24/424.37)^(1/8)-1 | 12.26% → 3 | 3 | PASS |
| C3 Pos YoY years | 75-99=3 | 7/8 = 87.5% | 3 | 3 | PASS |
| C4 PAT−Rev CAGR | <−8pp=0 | 12.26−22.12 = −9.86pp | 0 | 0 | PASS |

Both CAGR endpoints positive → CAGR edge rules (N/M, loss-to-profit swing) correctly
NOT triggered. **Block C = 11. PASS.**

### Block D — Balance Sheet (latest FY26, re-derived)

| Rule | Framework | Report | Re-derived | Score | Verdict |
|---|---|---|---|---|---|
| D1 Net Debt/EBITDA | net cash=5 | −20.39cr net cash | 5 | 5 | PASS |
| D2 Interest Coverage | 5-9.9x=4 | 1,654.60/192.23 = 8.61x | 4 | 4 | PASS |
| D3 Debt/Equity | <0.1=5 | 981.32/11,522.81 = 0.085x | 5 | 5 | PASS |
| D4 Current Ratio | <1.0=0 | 7,255.90/7,279.63 = 0.997x | 0 | 0 | PASS |

**Block D = 14. PASS.**

### Block E — Shareholder Alignment

All four line items NOT FOUND (shareholding + contingent-liability data absent, carried
from B00). Scored 0 each per operating rule 5. The "professionally managed: 3 if
FII+DII>50%" alternative on E1 correctly NOT invoked (FII/DII data also absent).
**Block E = 0. PASS** (mechanically correct; data-gap caveat properly flagged, not
treated as a quality signal — consistent with CLAUDE.md).

### Block F — Quantitative Moat (12 tests re-derived)

| Test | Framework path taken | Report score | Verdict |
|---|---|---|---|
| M1 Pricing Power | margin −7.18pp > 5pp → "else" | 0 | PASS |
| M2 Cost Advantage | PEER DATA NEEDED → 0 | 0 | PASS |
| M3 Capital Efficiency | FAT 2.33x>2 but ROCE 13.21%<15 → "FAT>1x AND ROCE>12%" | 1 | PASS |
| M4 Customer Stickiness | 1 decline yr, recovered → tier 3 | 3 | PASS |
| M5 Scale & Dominance | PEER DATA NEEDED → 0 | 0 | PASS |
| M6 Technology/R&D | R&D NOT FOUND → 0 | 0 | PASS |
| M7 Regulatory/License | unregulated → 0 | 0 | PASS |
| M8 Distribution | NOT FOUND → 0 | 0 | PASS |
| M9 Brand | PEER DATA NEEDED → 0 | 0 | PASS |
| M10 Switching Costs | growth all but 1 yr AND stable receivables → 3 | 3 | PASS |
| M11 Network Effects | latest 3yr CAGR 13.60% < prior 42.49%, <20% → 0 | 0 | PASS |
| M12 Negative WC | Payables NOT FOUND 7/9 yrs, "consistently" unprovable → 0 | 0 | PASS |

Moat matrix bands applied correctly throughout. M11 two-window test (needs ≥6 yrs)
correctly used the full 9-yr history. M3 correctly landed on the 1-point tier (ROCE
13.21% clears >12 but not >15). Moat sum = 7/60; moats present (≥3) = M4, M10 = 2;
2-3 present = MODERATE. **Block F PASS.**

Advisory (Finding GA-2, Verifier A domain): M10/M12 use FY26 Trade Receivables =
904.59, numerically identical to the FY26 "Cash & cash equivalents" figure (904.59)
cited in D1. Possible transcription collision. This is an existence-of-a-number
question owned by Verifier A, not a framework fail — the M10 scoring *logic* (growth
all-but-one-year AND declining receivable days) holds either way. Routed to Verifier A
for source confirmation.

### Classification, deal-breakers, confidence

- Core Score = 4+5+11+14+0 = **34**. Grand Total = 34+7 = 41. Re-derived, matches.
- Data confidence: 9 yrs → "7-9 moderate" band; downgrade triggers only at 3-4 yrs →
  `history_downgrade = false`. **PASS.**
- Deal-breakers: #1 (Block A<8) and #2 (Block B<8) correctly triggered → cap at GOOD.
  #5 (pledge>15%) correctly marked "cannot evaluate" (data absent), NOT asserted as a
  trigger. #3,4,6,7,8,9 correctly evaluated as not-triggered. **PASS.**
- Classification matrix: Core 34 → Core <40 = **AVOID**. Deal-breaker GOOD cap is
  correctly superseded by the lower matrix outcome. **PASS.**

**GATE 0 VERDICT: fully compliant. Classification AVOID re-derived independently and
confirmed. One MINOR methodology deviation (ROCE proxy, GA-1), one advisory routed to
Verifier A (GA-2). No score, band, deal-breaker, or classification error.**

---

## PART 2 — EMERGING MOAT (B07) COMPLIANCE

Framework authority: `prompts/07-emerging-moat-pipeline.md`.

### Category coverage (21 = 20 + R1)

All 21 categories addressed. A2, B2, B3, D2 = NO EVIDENCE FOUND; C2 = NOT FOUND — all
explicit, none force-fit. Scorecard table carries all 21 rows. **PASS.**

### Evidence taxonomy & completionist guard

- 📄/🎙️/🔍 taxonomy applied per item with source anchors. **PASS.**
- Completionist recount performed and stated in the required format: "📄 recount
  performed: 19 documented items across 7 categories." 8-9 active categories, below the
  12-category red-flag; recount honestly executed with F2/H1 deliberately held at
  Moderate to avoid over-crediting. **PASS.**

### Scorecard re-computation (likelihood×impact × evidence multiplier)

Raw matrix (HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0) verified row-by-row: all
21 raw scores correct. Weighted sum re-added:

1.4+3.0+0.5+4.0+0.5+0.5+0.7+2.1+0.5+1.4+4.0+3.0+1.7+4.0+0.7+1.7 = **29.7 → 30**.
Classification 25-39 = **MOAT STRENGTHENING**. Re-derived, matches. **PASS.**

### Findings against evidence-tier consistency (framework rule 3 / §5 multipliers)

The framework specifies exactly three evidence multipliers: 📄 1.0x, 🎙️ 0.7x, 🔍 0.5x.

- **EM-1 (MINOR):** A blended 0.85x multiplier — not in the framework taxonomy — is
  applied to H1 and R1 ("roughly half-and-half"). Reasonable interpretation for mixed
  rows but unsanctioned. Effect is small and non-directional; STRENGTHENING (30, mid-
  band) unaffected.
- **EM-2 (MINOR):** Multiplier/evidence-type inconsistency. The §3 summary table
  classifies A4, C1, and F1 evidence as 📄 (brand extension AR p.54; SEL Tiger
  distribution AR p.26; GPTW cert + hiring ratio AR p.44), yet the scorecard applies
  🔍 0.5x to each. Direction is conservative (understates), so it does not inflate the
  score and does not breach the completionist guard, but the tier is internally
  inconsistent. No classification change.
- **EM-3 (MINOR):** Active-category count stated inconsistently. §3 headline says "8 of
  21 rows," the reconciliation math says "5 Strong + 4 Moderate = 9," while the Moderate
  name list (A1, E2, F2, H1, R1) is 5 and the YAML `active_categories` correctly lists
  10 (5 Strong + 5 Moderate). The YAML figure (10) is the correct one; the prose count
  is muddled. Presentational; em_score 30 and the STRENGTHENING/TURNAROUND outputs are
  unaffected.

### Sections 2C, optionality, combined assessment

- §2C capex-embedded-growth arithmetic shown: 10,617 × 2.62 ≈ 27,817cr = 150% of FY26
  revenue, with an analyst-inference skepticism flag and a management-guidance sanity
  check. **PASS.**
- Optionality register present with all four required columns, 5 rows, each a 0/🎙️/🔍
  item. **PASS.**
- §6C uses the injected Gate 0 block; §6D returns TURNAROUND with full reasoning per the
  framework's instruction to fully reason HIGH POTENTIAL / TURNAROUND rows. The
  GOOD/AVERAGE-backward + EXPANSION-forward transition-hunt logic is correctly invoked
  and correctly qualified as "one notch below the clean pattern." **PASS.**

**EMERGING MOAT VERDICT: compliant. em_score 30 and MOAT STRENGTHENING re-derived and
confirmed; combined TURNAROUND properly reasoned. Three MINOR findings, all conservative
or presentational, none altering em_score or classification.**

---

## PART 3 — VALUATION (B11/B10)

**PENDING PHASE 3.** B11/B10 artifacts do not exist this run. The continuous-Pillar-1,
FTTCP-ROCE, single-credit, Pillar-2 offset, Pillar-3, Amendment-3 UA, dual-track,
Hurdle-Ratio, 4D-weight, SOM cross-check, and one-improvement-one-mechanism audit is
DEFERRED and NOT run now.

---

## SUMMARY

| Framework | Rules checked | Fails | Severity |
|---|---|---|---|
| Gate 0 (B01) | 46 | 1 | MINOR (GA-1); GA-2 advisory → Verifier A |
| Emerging Moat (B07) | 44 | 3 | MINOR (EM-1, EM-2, EM-3) |
| Valuation (B11/B10) | — | — | PENDING PHASE 3 |

No CRITICAL, no MAJOR. Gate 0 AVOID and Emerging Moat STRENGTHENING / combined
TURNAROUND all independently re-derived and confirmed. I concur with both destinations;
no recomputed classification differs.

```yaml
stage: B12c
company: "SHYAMMETL"
run_date: "2026-07-19"
model: claude-opus-4-8
status: complete
phase: 1
gate0:
  rules_checked: 46
  fails:
    - {id: "GA-1", severity: "MINOR", location: "B01 Formula Notes / Block A", description: "ROCE computed from proxy Capital Employed (Equity+Reserves+Borrowings) instead of framework formula TA-CL or source ROCE, for FY18-24 where CL split is absent. Documented, cross-checked within 1.9-3.1% of audited; no band or score change."}
emoat:
  rules_checked: 44
  fails:
    - {id: "EM-1", severity: "MINOR", location: "B07 Section 5 scorecard (H1, R1)", description: "Blended 0.85x evidence multiplier applied; framework taxonomy specifies only 1.0/0.7/0.5. Non-directional, immaterial; STRENGTHENING unaffected."}
    - {id: "EM-2", severity: "MINOR", location: "B07 Section 3 summary vs Section 5 (A4, C1, F1)", description: "Summary table classifies evidence as documented but scorecard applies 0.5x inference multiplier. Conservative (understates), does not inflate score or breach completionist guard; no classification change."}
    - {id: "EM-3", severity: "MINOR", location: "B07 Section 3 count statement", description: "Active-category count stated inconsistently (headline '8 of 21', reconciliation '5+4=9', YAML lists 10). Correct count is 5 Strong + 5 Moderate = 10 per YAML; prose is muddled. Presentational; em_score 30 unaffected."}
valuation: {status: "pending phase 3", rules_checked: 0, fails: []}
recomputed_destination_pe: ""   # pending phase 3 (valuation not audited this run)
recomputed_decision: ""          # concur: Gate 0 AVOID and EM STRENGTHENING / combined TURNAROUND re-derived and confirmed
findings:
  - {severity: "MINOR", location: "B01 Block A / Formula Notes", description: "ROCE proxy CE deviation from formula-as-written; data-justified, no score change (GA-1)"}
  - {severity: "MINOR", location: "B01 Block F M10/M12", description: "FY26 Trade Receivables 904.59 identical to FY26 cash figure 904.59; possible transcription collision, routed to Verifier A (number-existence domain); M10 scoring logic holds regardless (GA-2 advisory)"}
  - {severity: "MINOR", location: "B07 Section 5 (H1, R1)", description: "Unsanctioned 0.85x blended multiplier (EM-1)"}
  - {severity: "MINOR", location: "B07 Section 3 vs 5 (A4, C1, F1)", description: "Evidence-type vs multiplier inconsistency, conservative direction (EM-2)"}
  - {severity: "MINOR", location: "B07 Section 3 count", description: "Active-category count stated inconsistently; correct count 10 per YAML (EM-3)"}
critical_count: 0
major_count: 0
minor_count: 5
acceptance_rate: 96             # (90 rules checked - 4 rule fails) / 90, Gate 0 + EM scope; GA-2 is a Verifier-A-domain advisory, not a framework-rule fail
scope_note: "Phase 1 scope: Gate 0 (B01) + Emerging Moat (B07) only. Valuation (B11/B10) audit deferred to phase 3; those artifacts do not exist this run."
```
