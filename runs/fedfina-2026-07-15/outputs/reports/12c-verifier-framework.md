# VERIFIER C — FRAMEWORK ADHERENCE AUDIT (PHASE 1 SCOPE)
**Company:** Fedbank Financial Services Ltd (FEDFINA) | **Run date:** 2026-07-15
**Verifier:** C (framework adherence) | **Model:** claude-opus-4-8 | **Emits:** B12c
**Scope this run:** Gate 0 (B01) and Emerging Moat (B07) ONLY. Valuation adherence
(B10/B11) is DEFERRED to phase 3; those reports do not exist yet and were not audited.

I audit rule application, not raw-number provenance (Verifier A owns numbers) and not
company quality. Where I re-derive a score I take the report's stated input values as
given and check only whether the framework's thresholds/multipliers were applied as
written.

Severity scale: CRITICAL (misapplication that changes destination PE >1x, flips the
Hurdle verdict, or flips the decision) | MAJOR (wrong but the headline decision
survives, or a propagated field changes) | MINOR (imprecision, defensible adaptation,
presentational).

---

## PART 1 — GATE 0 (B01) COMPLIANCE

Framework references: prompts/01-gate-0-pipeline.md (scoring blocks, thresholds,
formula definitions, CAGR edge rules, classification matrix, deal-breakers).

### 1.1 Block scores re-derived against thresholds

| Test | Reported input | Reported score | Threshold check | Verdict |
|---|---|---|---|---|
| A1 Median ROCE | N/A | 0 | Rule 5: N/A→0; no NBFC ROCE substitute is written in the framework | PASS |
| A2 Min ROCE | N/A | 0 | same | PASS |
| A3 Median ROE | 11.5% | 0 | <12 = 0 → 0 | PASS |
| A4 ROCE trend | N/A | 0 | Rule 5 | PASS |
| B1 CFO/PAT | −5.04x | 0 | <0.50 = 0 | PASS |
| B2 FCF+ years | 0% | 0 | <50 = 0 | PASS |
| B3 FCF/PAT | −5.14x | 0 | negative = 0 | PASS |
| B4 WC days | N/A | 0 | Rule 5 | PASS |
| C1 Rev CAGR | 26.1% | 5 | ≥20 = 5 | PASS |
| C2 PAT CAGR | 41.0% | 5 | ≥20 = 5 | PASS |
| C3 +YoY years | 100% | 5 | 100% = 5 | PASS |
| C4 PAT−Rev CAGR | +14.9pp | 5 | ≥+3pp = 5 | PASS |
| D1 CRAR | 20.71% | 5 | NBFC CAR ≥18 = 5 (substitute is framework-authorized) | PASS |
| D2 PCR | 38.36% | 0 | NBFC PCR <60 = 0 | PASS |
| D3 Debt/Equity | 4.89x reported | 3 | "Financials: default 3" | PASS |
| D4 Current ratio | N/A | 0 | Rule 5 | PASS |
| E1 Promoter | 60.7% | 5 | ≥60 = 5 | PASS |
| E2 Δ3yr | −12.5pp | 0 | decreased >3% = 0 | PASS |
| E3 Pledge | N/A | 0 | Rule 5 (data gap, not a 0% finding) | PASS |
| E4 CL/NW | 0.33% | 5 | <5% = 5 | PASS |

Core score 0+0+20+8+10 = **38**. Confirmed. A3 median of {8.08, 9.37, 10.41, 12.6,
13.54, 14.36} = (10.41+12.6)/2 = 11.5% correctly placed below the 12% cut. CAGR
windows correctly use 1/5 over FY21→FY26 (five intervals). No negative-endpoint or
loss-to-profit CAGR edge cases mishandled.

### 1.2 Block F (moat tests) re-derived

| Test | Score | Rule check | Verdict |
|---|---|---|---|
| M1 Pricing Power | 5 | EBITDA-margin band, applied via a (1−Cost-to-Income) **proxy** | **FAIL (MAJOR)** — see F-1 |
| M2 Cost advantage | 0 | PEER DATA NEEDED, no guess | PASS |
| M3 Capital efficiency | 0 | N/A (lender), consistent with Block A | PASS |
| M4 Customer stickiness | 0 | N/A (receivable days) | PASS (minor, see F-2) |
| M5 Scale/dominance | 0 | PEER DATA NEEDED | PASS |
| M6 Technology/R&D | 0 | none disclosed → else 0 | PASS |
| M7 Regulatory/license | 0 | player count unverifiable, not guessed | PASS |
| M8 Distribution | 5 | reach quantified+growing; also ≥3 via "network growing AND rev CAGR≥15%" band (rev CAGR 26.1%) so moat-present is robust | PASS |
| M9 Brand | 0 | PEER DATA NEEDED | PASS |
| M10 Switching costs | 0 | N/A (receivable days) | PASS (minor, see F-2) |
| M11 Network effects | 0 | two-window deceleration; selling% not disclosed → 0 | PASS (minor, see F-3) |
| M12 Negative WC/float | 0 | N/A (non-deposit NBFC) | PASS |

Moats confirmed (≥3): as reported, M1 + M8 = 2 → moat_class MODERATE. **Contingent on
M1; see F-1.** Moat block score 10/60, grand total 48/160 as reported.

### 1.3 Classification, confidence, deal-breakers

- Classification matrix: Core 38 < 40 → **AVOID**. Correct. Moat class does not alter a
  Core<40 outcome. PASS.
- Data confidence: 6 years → "5-6 lower" band + "may not have seen full cycle" flag,
  no history downgrade (downgrade rule is 3-4 years). PASS.
- Deal-breakers: #1 (Block A<8→max GOOD) triggered, #2 (Block B<8→max GOOD) triggered,
  #4 (CFO/PAT<0.50→max AVERAGE) triggered; all correctly logged as non-binding under
  the AVOID floor. #3 (median ROCE<10%) marked not-triggered because ROCE is N/A rather
  than computed-below-10 — defensible and non-binding (MINOR). #5–#9 correctly
  not-triggered. PASS.
- CAGR edge rules honoured (no N/M cases; loss-to-profit correctly noted absent). PASS.

### Gate 0 findings

**F-1 (MAJOR) — M1 Pricing Power scored via an unauthorized EBITDA-margin proxy.**
Framework M1 requires "EBITDA margin expanded ≥2pp AND revenue CAGR ≥10%." The report
substitutes (1 − Cost-to-Income%) as an EBITDA-margin proxy and scores 5. Unlike D1
(CAR) and D2 (PCR), Block F provides **no** written NBFC substitute for M1, and the
report's own consistent treatment of every other lender-inapplicable test (A1/A2/A4,
M3/M4/M6/M10/M12) is N/A→0 per Rule 5. Applied strictly, M1 = N/A→0.
Recompute effect: moats_confirmed 2→1 (M8 only), moat_class MODERATE→**THIN**,
moat_score 10→5, grand_total 48→43. **Does NOT change the classification** (Core 38<40
= AVOID regardless), so not CRITICAL, but it changes propagated fields (moat_class,
moats_confirmed) that downstream stages consume. Location: 01-gate0.md lines 170,
183-184. Defensibility note: the proxy is transparently labeled and EBITDA is genuinely
undefined for a lender; this is a borderline adherence call, flagged because it is
inconsistent with the report's own N/A→0 discipline elsewhere.

**F-2 (MINOR) — M4/M10 marked N/A→0 despite zero revenue-decline years.** The lower
bands of M4/M10 key partly off decline-year counts (which favour FEDFINA: 0 declines),
but the top band requires receivable-days stability, genuinely N/A for a lender.
Scoring N/A→0 per Rule 5 is defensible; immaterial to classification.

**F-3 (MINOR) — M11 two-window CAGR uses overlapping windows** (FY21→FY24 vs
FY23→FY26 share FY23/FY24). Scored 0 regardless of window choice; immaterial.

**Gate 0 net:** classification AVOID is correctly derived and stands. One MAJOR
(M1 proxy → moat_class characterization), two MINOR. All block A-E scores, the
classification matrix, deal-breakers, CAGR edge rules and confidence band are
applied as written.

---

## PART 2 — EMERGING MOAT (B07) COMPLIANCE

Framework references: prompts/07-emerging-moat-pipeline.md (evidence taxonomy,
completionist guard, raw L×I matrix, evidence-quality multipliers, classification
bands).

### 2.1 Completeness and structure

All 21 categories (A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, R1)
are addressed with evidence tables or explicit NO EVIDENCE FOUND / NOT APPLICABLE.
No fabricated categories. Six sections present. PASS.

### 2.2 Raw-score matrix and evidence-multiplier re-derivation

Matrix: HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0. Multiplier: 📄 1.0,
🎙️ 0.7, 🔍 0.5.

| ID | Raw (stated) | Matrix-correct raw | Mult | Weighted (stated) | Weighted (correct) | Verdict |
|---|---|---|---|---|---|---|
| A3 | MM=2 | 2 | 0.7 | 1.4 | 1.4 | PASS |
| C1 | LM=1 | 1 | 0.5 | 0.5 | 0.5 | PASS |
| C2 | HM=3 | 3 | 1.0 | 3.0 | 3.0 | PASS |
| D1 | MM=2 | 2 | 0.7 | 1.4 | 1.4 | PASS |
| D2 | HM=3 | 3 | 1.0 | 3.0 | 3.0 | PASS |
| E1 | LM=1 | 1 | 0.5 | **1.0** | **0.5** | **FAIL (MAJOR)** — E-1 |
| F2 | HH=4 | 4 | 1.0 | 4.0 | 4.0 (grade contested) | **FLAG (MAJOR)** — E-2 |
| G1 | HM=3 | 3 | 1.0 | 3.0 | 3.0 | PASS |
| H1 | MM=2 | 2 | 0.5 | 1.0 | 1.0 | PASS |
| H2 | HM=3 | 3 | 1.0 | 3.0 | 3.0 | PASS |
| H3 | LL=1 | 1 | 1.0 | 1.0 | 1.0 | PASS |
| R1 | HM=3 | 3 | 1.0 | 3.0 | 3.0 | PASS |

Reported total 25.3 → 25. With E1 corrected (1.0→0.5): **24.8 → 25** (round-to-nearest,
the report's own convention). em_classification STRENGTHENING (25-39) survives.

### 2.3 Completionist guard, tiers, register

- Completionist recount performed explicitly (line 174 / YAML line 325): "8 categories
  carry at least one hard 📄 item; only 6 clear the Strong/Moderate bar, inside the 3-6
  base rate." 6 active < the 12-category trigger. PASS.
- Evidence-tier consistency: no clean "🎙️-only category scored as 📄" violation found,
  except the F2 judgment (E-2). A3 and D1 (claim-stage payoffs) correctly carry the
  🎙️ 0.7x haircut. PASS with E-2 caveat.
- Optionality register present and populated. PASS.
- Classification band (25-39 STRENGTHENING) correctly applied to em_score 25. PASS.

### Emerging Moat findings

**E-1 (MAJOR) — E1 evidence-multiplier arithmetic error.** Geographic first-mover is
graded raw LM=1 with 🔍 evidence (0.5x); 1 × 0.5 = 0.5, but the report records **1.0**
in the narrative (line 113), the Section-3 summary table (line 161), and the Section-5
scorecard (line 211). The weighted score is overstated by 0.5, inflating em_score from
a correct 24.8 to 25.3. em_classification STRENGTHENING survives on rounding (24.8→25),
so not CRITICAL, but the total then sits exactly on the 24/25 band boundary and the
error direction is inflationary. Location: lines 113, 161, 211.

**E-2 (MAJOR) — F2 Execution moat carries full HH/📄 credit (4.0) on a self-derived,
unreconciled promise-delivery record.** Framework F2 says to "cross-reference the
injected concall promise-delivery record" — i.e., B05. B05 was **not available** this
run (stated input_gap); the record was self-derived from the three FY26 concalls. F2 is
the single largest contributor (4.0 of 25.3) and the swing category. The delivered
actuals (credit-cost prints, branch counts, ECB amounts) are disclosed, so a 📄 grade
on the delivery leg is defensible, but full HH=4 × 📄 1.0 on an unreconciled,
self-derived record is aggressive: a 🎙️ haircut (4 × 0.7 = 2.8) would drop em_score to
~23.6 (or ~23.1 net of E-1), flipping em_classification to MODEST (12-24). The maker
transparently flagged the provisionality (input_gaps, FLAG-EMOAT-UNTESTED-FY27,
combined_reasoning "provisional pending stage 5 reconciliation"), which mitigates but
does not remove the swing risk. Location: lines 121-130, 214, 281. Framework-permissible
but surfaced as MAJOR because it and E-1 together determine whether the STRENGTHENING
classification holds.

**E-3 (MINOR) — capex_embedded_growth_pct (Section 2C) computed on an AUM base as
incremental AUM.** Framework 2C specifies implied incremental **revenue** as % of
current **revenue**. The report uses 150 branches × ₹17.7 Cr AUM/branch ÷ ₹21,136 Cr
AUM = 12.6%. NBFC-adapted and clearly labeled; feeds phase-3 valuation, not phase-1.

**E-4 (MINOR) — evidence_mix {documented:19, claim:12, inference:7} is self-reported**
and not independently item-recounted here (item-level counting is Verifier A territory).

**Emerging Moat net:** 21/21 categories addressed, completionist recount performed,
raw-matrix mapping correct on all rows; one clear arithmetic FAIL (E-1) and one
aggressive but framework-permissible grade (E-2) that together sit on the STRENGTHENING/
MODEST boundary. em_classification STRENGTHENING survives on rounding but is fragile.

---

## PART 3 — VALUATION (B10/B11)

**DEFERRED to phase 3.** B10 and B11 do not exist at this run date and were not
provided. No valuation-adherence audit performed. Continuous Pillar 1 formula, FTTCP
ROCE authority, single-credit rule, Pillar 2/3, UA Amendment-3 order, sector cap,
dual-track carry-through, Hurdle Ratio, 4D weights, SOM cross-check — all UNCHECKED.

---

## SUMMARY

| Framework | Rules checked | CRITICAL | MAJOR | MINOR | Net |
|---|---|---|---|---|---|
| Gate 0 (B01) | 45 | 0 | 1 (M1 proxy) | 2 | AVOID stands; moat_class fragile |
| Emerging Moat (B07) | 25 | 0 | 2 (E1 math, F2 grade) | 2 | STRENGTHENING survives on rounding, fragile |
| Valuation (B10/B11) | — | — | — | — | pending-phase-3 |

- **No CRITICAL findings.** Neither the Gate 0 classification (AVOID) nor the em
  classification (STRENGTHENING) flips under my recomputes.
- **Recomputed moat characterization (informational, not a decision flip):** under
  strict M1 handling, moat_class MODERATE→THIN and moats_confirmed 2→1; under E-1 +
  E-2 conservative handling, em_score falls toward the STRENGTHENING/MODEST boundary.
- acceptance_rate = rules passed ÷ checked = 67/70 = 96%. Above the 60% REWORK
  threshold. No Verifier-C REWORK trigger.

```yaml
stage: B12c
company: "FEDFINA"
run_date: "2026-07-15"
model: claude-opus-4-8
status: complete
gate0:
  rules_checked: 45
  fails:
    - {rule: "M1 Pricing Power", severity: MAJOR, issue: "scored 5 via unauthorized (1-Cost/Income) EBITDA-margin proxy; no NBFC substitute is written for M1 and report's own N/A->0 discipline (A1/A2/A4,M3/M4/M6/M10/M12) implies M1=N/A->0. Recompute: moats_confirmed 2->1, moat_class MODERATE->THIN, moat_score 10->5, grand_total 48->43. Classification AVOID unchanged (Core 38<40).", location: "01-gate0.md L170,183-184"}
emoat:
  rules_checked: 25
  fails:
    - {rule: "E1 evidence multiplier", severity: MAJOR, issue: "raw LM=1 x 0.5 (paper-search) = 0.5 but recorded as 1.0; em_score overstated 24.8->25.3. STRENGTHENING survives on rounding but total sits on 24/25 boundary.", location: "07-emoat.md L113,161,211"}
    - {rule: "F2 Execution moat grade", severity: MAJOR, issue: "full HH=4 x documented 1.0 = 4.0 (largest contributor) on a self-derived promise-delivery record; required B05 feed was absent. A 0.7x haircut (2.8) would flip em_classification to MODEST. Framework-permissible but swing-critical; maker flagged provisionality.", location: "07-emoat.md L121-130,214,281"}
valuation: pending-phase-3
recomputed_destination_pe: ""   # valuation deferred to phase 3; not computed
recomputed_decision: ""          # Gate 0 AVOID and em STRENGTHENING both survive; no flip
findings:
  - {severity: MAJOR, framework: gate0, item: "M1 EBITDA-margin proxy unauthorized; strict apply -> moat_class MODERATE->THIN, moats_confirmed 2->1", location: "01-gate0.md L170,183-184"}
  - {severity: MAJOR, framework: emoat, item: "E1 weighted score arithmetic 1x0.5 recorded as 1.0 not 0.5; inflates em_score to boundary", location: "07-emoat.md L113,161,211"}
  - {severity: MAJOR, framework: emoat, item: "F2 graded HH/documented 4.0 on self-derived record with B05 absent; conservative haircut would flip band to MODEST", location: "07-emoat.md L121-130,214"}
  - {severity: MINOR, framework: gate0, item: "M4/M10 N/A->0 despite zero revenue-decline years; defensible under Rule 5, immaterial", location: "01-gate0.md L173,179"}
  - {severity: MINOR, framework: gate0, item: "M11 two-window CAGR uses overlapping windows; scored 0 regardless", location: "01-gate0.md L180"}
  - {severity: MINOR, framework: emoat, item: "capex_embedded_growth_pct computed on AUM base as incremental AUM, framework 2C specifies revenue; NBFC-adapted, labeled, feeds phase-3", location: "07-emoat.md L66-72,332"}
  - {severity: MINOR, framework: emoat, item: "evidence_mix counts self-reported, not independently item-recounted (Verifier A scope)", location: "07-emoat.md L324"}
critical_count: 0
major_count: 3
minor_count: 4
acceptance_rate: 96             # 67 of 70 checked rules passed clean
```
