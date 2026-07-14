# STAGE 12c — VERIFIER C: FRAMEWORK ADHERENCE
Company: Asian Energy Services Limited (ASIANENE) | Run date: 2026-07-13
Model: claude-opus-4-8 | Emits: B12c

**SCOPE: PHASE 1 ONLY.** Gate 0 (B01) and Emerging Moat (B07) compliance
audited in full. Valuation-adherence (rule 4, B11/B10) is DEFERRED to Phase 3
and NOT run here — B10 and B11 do not yet exist. The valuation section of the
YAML is marked pending; recomputed_destination_pe and recomputed_decision are
left blank.

Audit basis: rule application only, not company quality and not raw-number
accuracy (Verifier A owns numbers). Stated inputs are taken as given; the
question is whether each threshold, band, matrix cell, edge rule, deal-breaker,
and evidence multiplier was applied AS WRITTEN.

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### Block A — Return on Capital (stated 7/20)
| Rule | Stated input | Band applied | Re-derived score | Verdict |
| --- | --- | --- | --- | --- |
| A1 Median ROCE | 14.11% (median of FY25 14.51, FY26 13.71) | 10-14.9 = 1 | 1 | PASS |
| A2 Min single-yr ROCE | 13.71% | 12-14.9 = 3 | 3 | PASS |
| A3 Median ROE | 11.07% (10-value median, avg of 5th/6th = (10.67+11.46)/2) | <12 = 0 | 0 | PASS |
| A4 ROCE trend | FY26 13.71 vs FY25 14.51 = -0.80pp | decline 1-3pp = 3 (edge) | 3 (edge, conservative) | PASS (MINOR note) |

A3 median re-derived from stated ROE series: sorted 5th=10.67, 6th=11.46 →
11.065 → <12 → 0. Correct. A4 note: a 0.80pp decline falls below the enumerated
"decline 1-3pp" floor and above the "latest ≥ earliest = 5" cell (which requires
non-decline). The band is genuinely un-enumerated for a sub-1pp decline; the
maker resolved it conservatively downward to 3 and disclosed it as a banding
edge. Not a misapplication. **Decision impact test:** had A4 = 5, Block A = 9,
Core = 39, still < 40 → AVOID unchanged. Non-material. **Block A = 7 confirmed.**

### Block B — Cash Generation Quality (stated 7/20)
| Rule | Stated input | Band | Re-derived | Verdict |
| --- | --- | --- | --- | --- |
| B1 Cum CFO/Cum PAT | 139.57/166.21 = 0.8397 | 0.70-0.84 = 2 | 2 | PASS |
| B2 FCF-positive yrs | 0 of 2 = 0% | <50 = 0 | 0 | PASS |
| B3 Cum FCF/Cum PAT | -59.75/93.28 = -0.64 | negative = 0 | 0 | PASS |
| B4 Change WC Days | 54.64 - 64.47 = -9.83 | decreased >5 = 5 | 5 | PASS |

Cumulative CFO (139.57) and PAT (166.21) sums re-added from the stated 10-year
series — both tie. B1 ratio 0.8397 sits inside 0.70-0.84 (upper bound 0.84);
score 2 is correct, not 4. B2/B3 correctly scored on the 2 disclosed years only,
with the FY17-FY24 gap marked NOT FOUND and not extrapolated (framework rule 5).
**Block B = 7 confirmed.**

### Block C — Growth (stated 6/20)
| Rule | Stated input | Band | Re-derived | Verdict |
| --- | --- | --- | --- | --- |
| C1 Revenue CAGR | (791.05/124.32)^(1/9)-1 = 22.83% | ≥20 = 5 | 5 | PASS |
| C2 PAT CAGR | FY17 PAT -18.20 (negative endpoint) | N/M = 0 | 0 | PASS |
| C3 Positive YoY yrs | 6 of 9 = 66.7% | 50-74 = 1 | 1 | PASS |
| C4 PAT CAGR - Rev CAGR | PAT CAGR N/M | 0 per rule | 0 | PASS |

CAGR EDGE RULES honoured exactly: negative endpoint → "N/M (negative endpoint)"
score 0 (C2); the two loss-to-profit swings (FY17→18, FY23→24) noted, no
synthetic CAGR attempted; C4 forced to 0 because PAT CAGR is N/M (the explicit
C4-when-N/M rule). C3 YoY count re-derived from the revenue series: 6 up
(FY18,20,22,24,25,26), 3 down (FY19,21,23) → 66.7% → 50-74 band → 1. **Block C =
6 confirmed.**

### Block D — Balance Sheet Strength (stated 17/20)
| Rule | Stated input | Band | Re-derived | Verdict |
| --- | --- | --- | --- | --- |
| D1 Net Debt/EBITDA | 11.79/98.35 = 0.12x | 0-1.0x = 4 | 4 | PASS |
| D2 Interest Coverage | 79.49/10.65 = 7.46x | 5-9.9 = 4 | 4 | PASS |
| D3 Debt/Equity | 158.64/494.15 = 0.32x | 0.1-0.5 = 4 | 4 | PASS |
| D4 Current Ratio | 715.10/338.81 = 2.11x | ≥2.0 = 5 | 5 | PASS |

D1 correctly scored 4 (0-1.0x), not 5 (net cash) — net debt is positive 11.79.
**Block D = 17 confirmed.**

### Block E — Shareholder Alignment (stated 0/20)
All four items N/A (no shareholding/pledge/contingent data in any input),
scored 0 per framework rule 5 ("mark N/A and score 0"). Correctly treated as a
data-availability gap, not a company-quality finding. **Block E = 0 confirmed.**

### Block F — Quantitative Moat (stated 10/60)
| Rule | Stated input | Band | Re-derived | Verdict |
| --- | --- | --- | --- | --- |
| M1 Pricing Power | margin +8.56pp (FY26 12.43 vs FY17 3.87), rev CAGR 22.84 | ≥2pp AND ≥10% = 5 | 5 | PASS (literal) |
| M2 Cost Advantage | peer data excluded | PEER DATA NEEDED = 0 | 0 | PASS |
| M3 Capital Efficiency | FAT 6.91x, ROCE 13.71% | FAT>1x AND ROCE>12% = 1 | 1 | PASS |
| M4 Customer Stickiness | 3 decline years | 3+ decline = 0 | 0 | PASS |
| M5 Scale & Dominance | peer data excluded | PEER DATA NEEDED = 0 | 0 | PASS |
| M6 Technology/R&D | no R&D line | 0 | 0 | PASS |
| M7 Regulatory/License | unregulated services | 0 | 0 | PASS |
| M8 Distribution | none (B2B project) | 0 | 0 | PASS |
| M9 Brand | proxy uncomputable + peer excluded | 0 | 0 | PASS |
| M10 Switching Costs | overall growth, 3 decline yrs | 2+ decline = 1 | 1 | PASS |
| M11 Network Effects | latest 3yr 61.0% > prior 3yr -30.68%; selling% declining thru FY25, FY26 NOT FOUND | rev CAGR≥20 AND selling stable/declining = 3 (edge) | 3 (conservative) | PASS (MINOR note) |
| M12 Negative WC/Float | FY25 64.47, FY26 54.64 (both >45) | >45 = 0 | 0 | PASS |

M3 correctly cascades to the third band: FAT 6.91x clears >3x but ROCE 13.71%
fails >20% (no 5) and >15% (no 3), lands at FAT>1x AND ROCE>12% = 1. M1 scored
5 on the literal latest-vs-earliest reading; the maker correctly flagged the
margin path is volatile (peak 26.56% FY22, -18.31% FY23), but the rule as
written is latest-vs-earliest only, so 5 is the compliant score. M11 top band
(=5) needs selling% declining across the full window; FY26 selling figure is
NOT FOUND, so the maker held at the =3 band. **Decision impact test:** had M11 =
5, Block F = 12, grand total = 49, moats_confirmed still 2 (M11 already ≥3 =
present), moat_class MODERATE unchanged, core unaffected → AVOID unchanged.
Non-material. **Block F = 10 confirmed; moats_confirmed 2; moat_class MODERATE
(2-3 present) correct.**

### Classification, confidence, deal-breakers
| Check | Stated | Re-derived | Verdict |
| --- | --- | --- | --- |
| Core score | 37 | 7+7+6+17+0 = 37 | PASS |
| Grand total | 47 | 37+10 = 47 | PASS |
| Classification matrix | Core <40 → AVOID | 37 < 40 → AVOID | PASS |
| Data confidence tier | 10+ yrs full | 10 fiscal years → full (by letter) | PASS |
| History downgrade | not applied | correct (history length satisfied) | PASS |
| Deal-breaker 1 (A<8) | caps GOOD, no effect | 7<8, base already below GOOD | PASS |
| Deal-breaker 2 (B<8) | caps GOOD, no effect | 7<8, no effect | PASS |
| Deal-breaker 3 (med ROCE<10) | not triggered | 14.11% ≥10 | PASS |
| Deal-breaker 4 (CFO/PAT<0.50) | not triggered | 0.84 | PASS |
| Deal-breaker 5 (pledge>15) | unknown → not triggered | NOT FOUND, defensible | PASS |
| Deal-breaker 6 (ND/EBITDA>3 & IC<3) | not triggered | 0.12x | PASS |
| Deal-breaker 7 (rev decline majority) | not triggered | 3 of 9 not majority | PASS |
| Deal-breaker 8 (PAT neg last 3) | not triggered | FY24-26 all positive | PASS |
| Deal-breaker 9 (history<3) | not triggered | 10 yrs | PASS |

Classification matrix applied correctly: Core 37 is below the 40 floor, so AVOID
is reached directly (deal-breakers can only cap downward, never raise; AVOID is
already the floor). The maker's transparency on the FY23 collapse and the
FY24-26 recovery is narrative context, correctly NOT allowed to override the
mechanical AVOID at this stage. **Final classification AVOID confirmed.**

### Gate 0 structural gap
The written B01 artifact (01-gate0.md) ends at the `---` on line 351 and does
**not** contain the mandatory closing ```yaml stage: B01-gate0``` block that the
Stage 1 spec requires ("end with exactly this fenced YAML block"). B07 clearly
consumed B01's YAML values (it cites core 37/100, moat_score 10, moats_confirmed
2, AVOID), so the block was almost certainly emitted at runtime and is missing
only from the saved report file — but as the artifact stands it is absent, and
with it the required FLAG-GATE0 (classification ≤ AVERAGE with historical
depressors identified) cannot be confirmed present. **MINOR** (structural /
presentational; downstream consumption evidently succeeded).

**Gate 0 verdict: fully compliant on every score, band, matrix cell, CAGR edge
rule, and deal-breaker. One MINOR structural gap (missing YAML block in the
saved file). Two conservative banding edge cases (A4, M11), both disclosed,
neither material to the classification. Concur with AVOID.**

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### All 21 categories addressed
A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3 (Section 3, 20 rows) plus
R1 (Section 4) = 21. Every category is either scored with evidence or explicitly
marked NO EVIDENCE FOUND. Section 5 scorecard lists all 21 rows. **PASS.**

### Raw L×I and evidence-multiplier check (scored rows)
| # | Stated L×I / Raw | Multiplier | Stated adj | Re-derived | Verdict |
| --- | --- | --- | --- | --- | --- |
| B1 | HH / 4 | 📄 1.0 | 4.0 | 4.0 | PASS |
| B2 | HH / 4 | 📄 1.0 | 4.0 | 4.0 | PASS |
| C1 | HM / 3 | 📄 1.0 | 3.0 | 3.0 | PASS |
| C2 | HM / 3 | 📄 1.0 | 3.0 | 3.0 | PASS |
| E1 | HH / 4 | 📄 1.0 | 4.0 | 4.0 | PASS |
| F1 | LL / 1 | 🎙️ 0.7 | 0.7 | 0.7 (see note) | PASS w/ MINOR |
| F2 | LM / 1 | 🎙️ 0.7 | 0.7 | 0.7 | PASS |
| G1 | HM / 3 | 📄 1.0 | 3.0 | 3.0 | PASS |
| G2 | MM / 2 | 🎙️ 0.7 | 1.4 | 1.4 | PASS |
| H1 | ML / 1 | 🎙️ 0.7 | 0.7 | 0.7 | PASS |
| H2 | HM / 3 | 📄 1.0 | 3.0 | 3.0 | PASS |
| R1 | LM / 1 | 🔍 0.5 | 0.5 | 0.5 | PASS |

All raw scores match the stated matrix (HH=4, HM/MH=3, MM/HL/LH=2, ML/LM=1,
LL=1). All multipliers arithmetically correct. **em_score re-summed = 4.0+4.0+
3.0+3.0+4.0+0.7+0.7+3.0+1.4+0.7+3.0+0.5 = 28.0.** Matches. Classification band:
28.0 ∈ 25-39 → MOAT STRENGTHENING. Correct.

**F1 evidence-tier inconsistency (MINOR):** the F1 narrative ("📄 (ESOP pool
exists) but thin") and the Section 3 summary table (Type = 📄) label F1 as
DOCUMENTED, but the scorecard applies the 🎙️ 0.7x multiplier rather than 📄
1.0x. The direction is conservative (0.7 < 1.0). Had it been scored 📄 1.0x, F1
= 1.0 and em_score = 28.3 — still inside 25-39 STRENGTHENING. No classification
impact. This is an evidence-tier labelling inconsistency, not a score-inflation
error; the more common failure mode (a 🎙️-only category scored as if 📄) does
NOT occur here — every 📄 1.0x row (B1, B2, C1, C2, E1, G1, H2) rests on a closed
acquisition, a SEBI approval, signed contracts, disclosed order-book splits, a
rating action, or committed BOOT capex.

### Completionist recount
Performed and stated explicitly: "📄 recount performed: 17 documented items
across 7 categories." Only 7 of 20 categories are active (Strong/Moderate),
below the 12-category guard trigger, yet the recount was still executed — good
discipline. **PASS**, with one MINOR bookkeeping note: the enumerated 17 items
actually span 8 categories (B1=3, B2=3, C1=1, C2=3, E1=1, G1=3, H2=2, **F1=1**),
because the F1 ESOP item is counted in the 17 but F1 is not one of the 7 active
categories. "17 items across 7 categories" is therefore off by one category
label. Cosmetic; the guard's purpose (verifying documented items are not
inflated 🎙️ claims) is served. evidence_mix {documented 17, claim 9, inference
4} reconciles to the recount's documented count.

### Other framework rules
- **Double-credit rule honoured:** H2 explicitly states "Kuiper is scored once,
  under E1, to avoid double-crediting the same event across two categories."
  Oilmax scored once under B1, Kuiper once under E1 — no event credited twice.
  **PASS.**
- **capex_embedded_growth (2C):** formula applied as written — Rs286.43L capex ×
  4.132 FAT = Rs1,183.5L implied revenue ÷ Rs46,503.81L FY25 revenue = 2.54% →
  2.5%. Arithmetic sound (input accuracy is Verifier A's domain). **PASS.**
- **6D combined assessment:** AVOID backward + STRENGTHENING forward → TURNAROUND,
  with full reasoning as the stage requires for TURNAROUND rows. Defensible under
  the transition-setup guidance (weak/AVOID backward meeting a real forward
  strengthening signal, capped below EXPANSION by the Grade-C execution record).
  **PASS.**
- **Optionality register:** present, 6 rows, all items scored 0 or resting on
  🎙️/🔍 evidence, correctly "watched, never scored." **PASS.**
- **All six sections present**, evidence taxonomy applied per item with source
  anchors. **PASS.**

**Emerging Moat verdict: fully compliant on the 21-category coverage, the L×I
matrix, every evidence multiplier, the completionist recount, the double-credit
rule, and the em_score/classification. Two MINOR items (F1 evidence-tier
label vs multiplier; recount category-count off by one), neither changes
em_score band or the combined assessment. Concur with em_score 28.0 /
STRENGTHENING / TURNAROUND.**

═══════════════════════════════════════════════════════════════════
## PART 3 — VALUATION (B11/B10)
═══════════════════════════════════════════════════════════════════
DEFERRED TO PHASE 3. B10 and B11 do not exist. No rules run. Section pending.

═══════════════════════════════════════════════════════════════════
## SUMMARY
═══════════════════════════════════════════════════════════════════
- Gate 0: 47 rule applications re-derived; all block scores, the classification
  matrix, data-confidence tier, and 9 deal-breakers confirmed. 1 MINOR
  (missing YAML block in saved artifact). Concur: AVOID, core 37, grand total 47.
- Emerging Moat: 40 rule applications checked; 21-category coverage, all
  multipliers, recount, double-credit, and em_score confirmed. 2 MINOR (F1
  evidence-tier label vs 🎙️ multiplier; recount 7-vs-8 category count). Concur:
  em_score 28.0, STRENGTHENING, TURNAROUND.
- Valuation: pending Phase 3.
- No CRITICAL, no MAJOR. Three MINOR, all conservative or presentational, none
  altering a score band or the decision. Neither the Gate 0 classification nor
  the Emerging Moat classification/combined assessment changes on recomputation.

```yaml
stage: B12c
company: "ASIANENE"
run_date: "2026-07-13"
model: claude-opus-4-8
status: complete
gate0:
  rules_checked: 47
  fails:
    - {severity: "MINOR", rule: "Stage 1 output spec (closing YAML block)", detail: "Saved 01-gate0.md ends at line 351 with no mandatory ```yaml stage: B01-gate0``` block; required FLAG-GATE0 (classification <= AVERAGE with historical depressors) not confirmable in artifact. B07 consumed B01 YAML values, so block was likely emitted at runtime but is absent from the saved file."}
emoat:
  rules_checked: 40
  fails:
    - {severity: "MINOR", rule: "Section 5 evidence-tier consistency (F1)", detail: "F1 labelled 📄 in narrative and Section 3 summary table but scored with 🎙️ 0.7x in the scorecard. Conservative direction; F1 at 📄 1.0x would move em_score 28.0 -> 28.3, band unchanged (STRENGTHENING)."}
    - {severity: "MINOR", rule: "Completionist recount category count", detail: "Recount states '17 documented items across 7 categories' but the enumerated items span 8 categories (F1 ESOP item included though F1 is not among the 7 active categories). Cosmetic; guard purpose served, evidence_mix reconciles."}
valuation: {rules_checked: 0, fails: [], status: "pending phase 3"}
recomputed_destination_pe: ""
recomputed_decision: ""
findings:
  - {severity: "MINOR", location: "B01 Block A4", note: "0.80pp ROCE decline falls in an un-enumerated band gap between 'latest>=earliest=5' and 'decline 1-3pp=3'; resolved conservatively to 3 and disclosed. Had it been 5, core=39, still AVOID. Non-material."}
  - {severity: "MINOR", location: "B01 Block F M11", note: "Held at =3 band rather than =5 because FY26 selling-expense figure NOT FOUND; conservative and disclosed. Had it been 5, moats_confirmed and moat_class unchanged, core unchanged, AVOID unchanged. Non-material."}
  - {severity: "MINOR", location: "B01 saved artifact", note: "Mandatory closing YAML block absent from 01-gate0.md; FLAG-GATE0 not confirmable in the file."}
  - {severity: "MINOR", location: "B07 Section 5 F1", note: "F1 evidence tier 📄 (narrative/summary) vs 🎙️ 0.7x (scorecard); conservative, no band change."}
  - {severity: "MINOR", location: "B07 completionist recount", note: "17 documented items span 8 categories, stated as 7; cosmetic count mismatch."}
critical_count: 0
major_count: 0
minor_count: 5
acceptance_rate: 97   # 84 of 87 checked rule applications clean (gate0+emoat); valuation pending
```
