# STAGE 12c: VERIFIER C — FRAMEWORK ADHERENCE AUDIT (PHASE 1 SCOPE)

Company: Apex Ecotech Ltd (APEXECO) | Run date: 2026-07-10 | Model: claude-opus-4-8

SCOPE: Phase 1 only. Gate 0 (B01) compliance + Emerging Moat (B07) compliance.
Valuation audit (B11, B10) is DEFERRED to phase 3 and NOT run here (those artifacts
do not exist yet). This audit checks RULE APPLICATION only. Raw-number verification
is Verifier A's domain; company quality is out of scope.

Rule sources:
- Gate 0: prompts/01-gate-0-pipeline.md
- Emerging Moat: prompts/07-emerging-moat-pipeline.md

Artifacts audited:
- B01: runs/apexeco-2026-07-10/outputs/reports/01-gate0.md
- B07: runs/apexeco-2026-07-10/outputs/reports/07-emoat.md

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) COMPLIANCE
═══════════════════════════════════════════════════════════════════

Each block score re-derived from the stated inputs against the thresholds in
prompts/01-gate-0-pipeline.md. I re-check band selection, sums, classification
matrix, data-confidence rule, deal-breaker application, and CAGR edge rules.
I do NOT re-source the underlying numbers (Verifier A owns that).

### Block A — Return on Capital (stated 20/20)

| Rule | Stated input | Threshold | Stated score | Re-derived | Verdict |
|---|---|---|---|---|---|
| A1 Median ROCE | 29.91% (median of FY25 24.70, FY26 35.12) | ≥25=5 | 5 | ≥25 → 5 | PASS |
| A2 Min single-yr ROCE | 24.70% | ≥15=5 | 5 | ≥15 → 5 | PASS |
| A3 Median ROE | 28.08% (median of 9 yrs) | ≥20=5 | 5 | sorted median = 28.08 → 5 | PASS |
| A4 ROCE trend | FY26 35.12 vs earliest-avail FY25 24.70 | latest≥earliest=5 | 5 | latest≥earliest → 5 | PASS |

Block A sum: 5+5+5+5 = 20. PASS. Low-confidence flag (n=2 for ROCE) correctly
raised; A4 uses FY25 as "earliest" because FY18–FY24 ROCE is genuinely
uncomputable (no CL split) — this is a data limit correctly handled under the
"never estimate" rule, not a rule misapplication. Correctly flagged.

### Block B — Cash Generation Quality (stated 7/20)

| Rule | Stated input | Threshold | Stated score | Re-derived | Verdict |
|---|---|---|---|---|---|
| B1 Cumul CFO/PAT | 14.84/36.09 = 0.41 | <0.50=0 | 0 | 0.411 → <0.50 → 0 | PASS |
| B2 FCF-positive prop | 1 of 2 = 50% | 50-74=2 | 2 | 50% → 50-74 band → 2 | PASS |
| B3 Cumul FCF/PAT | −0.53/25.58 = −0.02 | neg=0 | 0 | negative → 0 | PASS |
| B4 ΔWC Days | 35.65 − 107.85 = −72.2 | dec>5=5 | 5 | decreased >5 → 5 | PASS |

Block B sum: 0+2+0+5 = 7. PASS. WC-days formula (Rec+Inv−Pay) applied correctly
on both years. Note (MINOR, not a fail): B2/B3 are computed over a 2-year window
while B1 spans 7 years, forced by capex being itemised only in the two PDF years;
correctly flagged, and does not change the classification because deal-breaker #4
already governs.

### Block C — Growth (stated 18/20)

| Rule | Stated input | Threshold | Stated score | Re-derived | Verdict |
|---|---|---|---|---|---|
| C1 Rev CAGR | 30.75% (FY18→26, both endpoints +) | ≥20=5 | 5 | ≥20 → 5 | PASS |
| C2 PAT CAGR | 58.86% (both endpoints +) | ≥20=5 | 5 | endpoints +ve, valid → 5 | PASS |
| C3 Positive YoY rev | 7 of 8 = 87.5% | 75-99=3 | 3 | 87.5 → 75-99 → 3 | PASS |
| C4 PAT−Rev CAGR | +28.11pp | ≥+3pp=5 | 5 | ≥+3 → 5 | PASS |

Block C sum: 18. PASS. CAGR EDGE RULES honoured: both endpoints of C1/C2 are
positive so no N/M; the FY21/FY22 mid-window PAT dips are correctly NOT treated as
a loss-to-profit swing (endpoints already positive) and are recorded in data_notes
for context, exactly as the edge rule requires.

### Block D — Balance Sheet Strength (stated 20/20)

| Rule | Stated input | Threshold | Stated score | Re-derived | Verdict |
|---|---|---|---|---|---|
| D1 Net Debt/EBITDA | −33.75 Cr (net cash) | net cash=5 | 5 | net cash → 5 | PASS |
| D2 Interest coverage | 253.9x | ≥10x=5 | 5 | ≥10 → 5 | PASS |
| D3 Debt/Equity | 0.021 | <0.1=5 | 5 | <0.1 → 5 | PASS |
| D4 Current ratio | 3.56x | ≥2.0=5 | 5 | ≥2.0 → 5 | PASS |

Block D sum: 20. PASS. (Non-financial issuer; standard bands correctly used, not
the bank/NBFC variants.)

### Block E — Shareholder Alignment (stated 0/20)

| Rule | Stated input | Threshold | Stated score | Re-derived | Verdict |
|---|---|---|---|---|---|
| E1 Promoter holding | N/A (not provided) | — | 0 | N/A → 0 | PASS |
| E2 Promoter Δ 3yr | N/A | — | 0 | N/A → 0 | PASS |
| E3 Promoter pledge | N/A | — | 0 | N/A → 0 | PASS |
| E4 Contingent liab/NW | N/A | — | 0 | N/A → 0 | PASS |

Block E sum: 0. PASS. Correctly scored 0 as a data gap under rule 5 ("never
estimate"), correctly labelled NOT a governance finding, and pledge absence
correctly prevents deal-breaker #5 from firing (cannot trigger on missing data).

### Block F — Quantitative Moat (stated 21/60)

| Rule | Stated input | Threshold hit | Stated | Re-derived | Verdict |
|---|---|---|---|---|---|
| M1 Pricing power | +5.45pp margin, CAGR 30.75 | exp≥2pp & CAGR≥10=5 | 5 | 5 | PASS |
| M2 Cost adv | 7.01pp below peer median | below=0 | 0 | 0 | PASS |
| M3 Capital eff | FAT 75.8x, ROCE 35.12 | >3x & >20%=5 | 5 | 5 | PASS |
| M4 Cust stickiness | 1 decline yr, recovered; rec days not stable | max1 recovered=3 | 3 | 3 | PASS |
| M5 Scale | 4th of 5 by mcap | top5=1 | 1 | 1 | PASS |
| M6 Tech/R&D | no data | N/A=0 | 0 | 0 | PASS |
| M7 Regulatory | no player count | PEER DATA NEEDED=0 | 0 | 0 | PASS |
| M8 Distribution | none | none=0 | 0 | 0 | PASS |
| M9 Brand | GM 24.43 below peer 45.86 | at/below=0 | 0 | 0 | PASS |
| M10 Switching | growth all but 1 yr, rec days fell | all-but-1 & stable=3 | 3 | 3 | PASS* |
| M11 Network | 3yr CAGR 62.65>−8.05; sell% partial | CAGR≥20 & sell stable=3 | 3 | 3 | PASS |
| M12 Neg WC/float | FY26 35.65 (2-yr sample) | 15-45=1 | 1 | 1 | PASS* |

Block F sum: 5+0+5+3+1+0+0+0+0+3+3+1 = 21. PASS.
Moats present (≥3): M1, M3, M4, M10, M11 = 5. Classification 4-5 present → STRONG. PASS.

*M10: crediting the 3-band required reading "stable" receivable days as satisfied by
a large DECREASE (101.75→41.15 days). Defensible and conservative (5-band correctly
withheld because growth was not every-year); the alternative reading would only lower
the score. Not a fail. *M12: scored on latest year (35.65, 15-45 band) with only a
2-year sample, correctly flagged; FY25 alone (107.85) would score 0. Conservative
single-year read is acceptable given the data limit. Not a fail.

### Classification, confidence, deal-breakers

| Check | Rule | Stated | Re-derived | Verdict |
|---|---|---|---|---|
| Core score | A+B+C+D+E | 65 | 20+7+18+20+0 = 65 | PASS |
| Grand total | Core+Moat | 86 | 65+21 = 86 | PASS |
| Data confidence | 9 yrs = "7-9 moderate" | moderate, no downgrade | 7-9 → moderate, downgrade only at 3-4 | PASS |
| history_downgrade | false | false | correct | PASS |
| Pre-override matrix | Core 60-79 + STRONG = GOOD+ | GOOD+ | matches matrix | PASS |
| Deal-breaker #1 | Block A<8 → max GOOD | not fired (A=20) | correct | PASS |
| Deal-breaker #2 | Block B<8 → max GOOD | fired (B=7) | 7<8 → correct | PASS |
| Deal-breaker #3 | median ROCE<10 → max AVG | not fired (29.91) | correct | PASS |
| Deal-breaker #4 | cumul CFO/PAT<0.50 → max AVG | fired (0.41) | 0.41<0.50 → correct | PASS |
| Deal-breaker #5 | pledge>15 → max AVG | not fired (no data) | cannot fire on N/A → correct | PASS |
| Deal-breaker #6 | ND/EBITDA>3x & IC<3x → AVOID | not fired (net cash) | correct | PASS |
| Deal-breaker #7 | rev decline majority → max AVG | not fired (1 of 8) | correct | PASS |
| Deal-breaker #8 | PAT neg in last 3 yrs → max AVG | not fired | FY24/25/26 all +ve → correct | PASS |
| Deal-breaker #9 | history<3 → AVERAGE | not fired (9 yrs) | correct | PASS |
| Most-restrictive cap | AVERAGE (from #4) | AVERAGE | GOOD+ capped by #4 to AVERAGE | PASS |
| Final classification | AVERAGE | AVERAGE | correct | PASS |

Deal-breaker #8 was not stated explicitly in B01 but is correctly not triggered
(FY24 6.63, FY25 8.56, FY26 17.02 all positive). The FY21/FY22 negatives fall
outside the last-3-years window. No silent miss.

GATE 0 RESULT: 39 rule checks, 39 PASS, 0 FAIL. Every block score, the
classification matrix, the data-confidence rule, all nine deal-breakers, and the
CAGR edge rules were applied as written. The AVERAGE verdict is correctly derived
and the twice-over cap (deal-breakers #2 and #4) is correctly reduced to the single
most-restrictive AVERAGE.

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) COMPLIANCE
═══════════════════════════════════════════════════════════════════

Checks: all 21 categories addressed or NO EVIDENCE; raw-score matrix
(HH=4/HM,MH=3/HL,MM,LH=2/ML,LM=1/LL=1/none=0); evidence multipliers
(📄1.0 / 🎙️0.7 / 🔍0.5); no 🎙️-only category scored as 📄; completionist
recount performed; classification threshold.

### 21-category coverage

All 21 rows present in the Section 3/5 tables: A1-A4, B1-B3, C1-C2, D1-D2,
E1-E2, F1-F2, G1-G2, H1-H3, R1 (= 21). Every non-scored category carries an
explicit "NO EVIDENCE FOUND" (or "opposite / flagged"). PASS.

### Scorecard rule-by-rule (scored rows only; all others raw 0 → adj 0)

| Cat | Raw (matrix) | Evidence | Mult | Stated adj | Re-derived adj | Verdict |
|---|---|---|---|---|---|---|
| B2 Qualification lock-in | 1 (LL) | 🎙️ | 0.7 | 0.7 | 1×0.7 = 0.7 | PASS |
| C1 Customer ecosystem | 2 (MM) | 🎙️ | 0.7 | 1.4 | 2×0.7 = 1.4 | PASS |
| E1 Geo/tech first-mover | 2 (MM) | 🎙️ | 0.7 | 1.4 | 2×0.7 = 1.4 | PASS |
| F2 Execution moat | 2 (MM) | 🎙️/📄 mixed | 0.7 | 1.4 | 2×0.7 = 1.4 | PASS |
| G1 War chest | 4 (HH) | 📄 | 1.0 | 4.0 | 4×1.0 = 4.0 | PASS |
| H1 Consolidation | 1 (LL) | 🎙️ | 0.7 | 0.7 | 1×0.7 = 0.7 | PASS |
| R1 Regulatory tailwind | 1 (LL) | 🎙️ | 0.7 | 0.7 | 1×0.7 = 0.7 | PASS |

Every raw score matches the likelihood×impact matrix and every multiplier matches
the stated evidence tier.

### Evidence-tier discipline (no 🎙️ scored as 📄)

PASS — and notably conservative. The three mixed-evidence categories that have a
genuine 📄 component (C1: two documented Reliance orders; F2: audited FY26 revenue;
B2: documented ISO 9001 cert) were all assigned the 🎙️ 0.7x multiplier, i.e.
DOWN-weighted, not inflated. Only G1, which rests on audited/filed balance-sheet
figures, received the 1.0x 📄 multiplier. No category was over-credited. The Veolia
"strategic alliance" (H2), marketed in written materials but denied by management on
the call, was correctly reset to NO EVIDENCE (0) with the contradiction flagged, not
scored as a documented partnership.

### Completionist recount

PASS. Line present: "📄 recount performed: 3 documented items across 2 categories
(G1, F2)." Only 4 categories are active (C1, E1, F2, G1), inside the 3-6 base rate,
so the guard's inflation trigger (12+ active) does not apply. The recount is
conservative (it does not even claim the C1/1B documented items), so there is no
over-crediting risk.

### Adjusted total — FAIL (MINOR)

Stated ADJUSTED TOTAL = 10.1 and YAML em_score = 10.1.
Re-summing the seven non-zero adjusted values:
0.7 + 1.4 + 1.4 + 1.4 + 4.0 + 0.7 + 0.7 = **10.3**, not 10.1.
Discrepancy = 0.2. This is an internal arithmetic error in the scorecard total.
NOT decision-changing: both 10.1 and 10.3 fall in the <12 band → NO MEANINGFUL
EMERGING MOAT, and the recomputed total does not cross any classification
threshold. Severity MINOR. (The precise arithmetic is also within Verifier A's
remit; flagged here because it is an internal scorecard-consistency issue.)

### Classification threshold

Stated: <12 → NO MEANINGFUL EMERGING MOAT ("NONE" in YAML). With the corrected
10.3 the band is unchanged. Threshold applied correctly. PASS.

### Sections 1/2/4 and combined assessment

- 2C capex-embedded growth arithmetic shown and correctly ruled "not meaningful"
  for an asset-light integrator; capex_embedded_growth_pct = 0. PASS.
- active_categories (G1, F2, C1, E1) match the Section 3 count of 4 Strong/Moderate
  rows. PASS.
- 6D combined = AVERAGE, correctly derived from injected Gate 0 (Core 65 AVERAGE +
  emerging NONE) against the transition-setup matrix. PASS.

EMERGING MOAT RESULT: 14 rule checks, 13 PASS, 1 FAIL (MINOR, adjusted-total
arithmetic 10.1 vs 10.3, non-decision-changing).

═══════════════════════════════════════════════════════════════════
## PART 3 — VALUATION (B11 / B10)
═══════════════════════════════════════════════════════════════════

DEFERRED to phase 3. B10 and B11 do not exist yet. Not audited. Status: pending.

═══════════════════════════════════════════════════════════════════
## SUMMARY
═══════════════════════════════════════════════════════════════════

- Gate 0: 39/39 rules pass. Classification AVERAGE correctly derived; deal-breakers
  #2 and #4 correctly applied and reduced to the most-restrictive AVERAGE; CAGR edge
  rules and data-confidence rule honoured; no deal-breaker silently missed.
- Emerging Moat: 13/14 rules pass. One MINOR arithmetic slip in the adjusted total
  (10.1 stated vs 10.3 recomputed), no classification impact. Evidence-tier
  discipline and multipliers are correct and consistently conservative; completionist
  recount performed; all 21 categories addressed.
- No CRITICAL or MAJOR framework findings in phase-1 scope.
- Overall acceptance rate (Gate 0 + EM): 52/53 = 98%.

```yaml
stage: B12c
company: "APEXECO"
run_date: "2026-07-10"
model: claude-opus-4-8
status: complete
gate0:
  rules_checked: 39
  fails: []
emoat:
  rules_checked: 14
  fails:
    - {severity: MINOR, rule: "adjusted total sum", detail: "em_score stated 10.1; re-sum of the 7 non-zero adjusted values (0.7+1.4+1.4+1.4+4.0+0.7+0.7) = 10.3. Off by 0.2, non-decision-changing (both <12 -> NONE)."}
valuation: {rules_checked: 0, fails: [], status: "pending phase 3"}
recomputed_destination_pe: ""
recomputed_decision: ""
findings:
  - {severity: MINOR, location: "B07 Section 5 scorecard / YAML em_score", claimed: "adjusted total = 10.1", framework_truth: "sum of stated per-row adjusted values = 10.3", note: "Arithmetic slip only; classification NONE unchanged. Individual multipliers and raw scores all correct."}
critical_count: 0
major_count: 0
minor_count: 1
acceptance_rate: 98
```
