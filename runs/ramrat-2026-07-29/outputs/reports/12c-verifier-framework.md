# B12c — VERIFIER C: FRAMEWORK ADHERENCE (RAMRAT, 2026-07-29)

Scope: PHASE 1 ONLY. Gate 0 (B01) + Emerging Moat (B07) rule-application audit.
Valuation adherence (B11/B10) DEFERRED to Phase 3 — those artifacts do not yet
exist and were not audited. This verifier owns rule application, not raw-number
source fidelity (Verifier A owns numbers). Re-derivations below take each
stage's stated per-line inputs as given and re-apply the framework thresholds,
matrices, and edge rules exactly as written in prompts/01 and prompts/07.

Artifacts audited:
- runs/ramrat-2026-07-29/outputs/reports/01-gate0.md
- runs/ramrat-2026-07-29/outputs/reports/07-emoat.md

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) COMPLIANCE TABLE
═══════════════════════════════════════════════════════════════════

### Block A — Return on Capital (stated inputs re-banded)
| Rule | Stated input | Threshold applied | Score | Recompute | Verdict |
|---|---|---|---:|---|---|
| A1 Median ROCE | 16.65% (median of 10 yrs) | 15-19.9→3 | 3 | sorted median = (16.36+16.93)/2 = 16.65% → band 3 | PASS |
| A2 Min single-yr ROCE | 8.38% (FY21) | 8-11.9→1 | 1 | min = 8.38 → band 1 | PASS |
| A3 Median ROE | 15.42% | 15-19.9→4 | 4 | median = (15.40+15.43)/2 = 15.42% → band 4 | PASS |
| A4 ROCE trend FY26 vs FY17 | 19.01 vs 16.36 (+2.65pp) | latest≥earliest→5 | 5 | latest ≥ earliest → 5 | PASS |
| Block A total | | | 13/20 | 3+1+4+5=13 | PASS |

### Block B — Cash Generation
| Rule | Stated input | Threshold | Score | Recompute | Verdict |
|---|---|---|---:|---|---|
| B1 ΣCFO/ΣPAT | 541.87 / 424.57 = 1.28x | ≥1.00→5 | 5 | Σ re-added: CFO 541.87, PAT 424.57, ratio 1.276 → 5 | PASS |
| B2 FCF-pos years | N/A (no capex breakdown) | missing→0 | 0 | grounded NOT-FOUND → 0, not estimated | PASS |
| B3 ΣFCF/ΣPAT | N/A (no capex breakdown) | missing→0 | 0 | grounded NOT-FOUND → 0 | PASS |
| B4 ΔWC Days | N/A (trade payables not disclosed) | missing→0 | 0 | payables component absent → cannot compute → 0 | PASS |
| Block B total | | | 5/20 | 5+0+0+0=5 | PASS |

### Block C — Growth
| Rule | Stated input | Threshold | Score | Recompute | Verdict |
|---|---|---|---:|---|---|
| C1 Rev CAGR (9y) | 23.04% | ≥20→5 | 5 | (5176.65/800.83)^(1/9)-1 = 23.05% → 5 | PASS |
| C2 PAT CAGR (9y) | 19.19% | 15-19.9→4 | 4 | (107.05/22.05)^(1/9)-1 = 19.19% → 4 | PASS |
| C3 Positive YoY yrs | 9/9 = 100% | 100→5 | 5 | 5 | PASS |
| C4 PAT−Rev CAGR | -3.85pp | -3 to -8→1 | 1 | 19.19-23.04 = -3.85 → band 1 | PASS |
| Block C total | | | 15/20 | 5+4+5+1=15 | PASS |
| CAGR edge rules | endpoints all +ve, no loss-to-profit swing | no synthetic CAGR needed | — | correctly not invoked | PASS |

### Block D — Balance Sheet
| Rule | Stated input | Threshold | Score | Recompute | Verdict |
|---|---|---|---:|---|---|
| D1 ND/EBITDA | 661.37/261.43 = 2.53x | 2-3x→1 | 1 | 2.53 → band 1 | PASS |
| D2 Int Cov | 238.49/85.52 = 2.79x | 1.5-2.9→1 | 1 | 2.79 → band 1 | PASS |
| D3 D/E | 675.23/579.48 = 1.17x | 1.0-1.5→1 | 1 | 1.165 → band 1 | PASS |
| D4 Current Ratio | 1304.61/738.80 = 1.77x | 1.5-1.99→4 | 4 | 1.766 → band 4 | PASS |
| Block D total | | | 7/20 | 1+1+1+4=7 | PASS |

### Block E — Shareholder Alignment
| Rule | Stated input | Threshold | Score | Verdict |
|---|---|---|---:|---|
| E1-E4 | all NOT FOUND (no SHP/pledge/contingent filing) | missing→0 | 0 each | PASS (grounded 0, flagged as data gap not adverse finding — matches "NOT FOUND only fill" rule) |
| Block E total | | | 0/20 | PASS |

### Block F — 12 Moat Tests
| Test | Stated basis | Threshold applied | Score | Verdict |
|---|---|---|---:|---|
| M1 Pricing Power | OPM -1.35pp (stable ±2pp) + rev CAGR 23% | stable+≥10%→3 | 3 | PASS |
| M2 Cost Advantage | 5.05% vs peer med 4.56% (+0.49pp) | ±2pp→1 | 1 | PASS |
| M3 Capital Efficiency | FAT 8.10x + ROCE 19.01% (≤20%) | FAT>2x & ROCE>15%→3 | 3 | PASS (top tier correctly denied: ROCE not >20%) |
| M4 Customer Stickiness | 0 decline yrs; rec days NOT stable ±10 | tier1 fails, tier2 max-1-decline→3 | 3 | PASS (lenient but literal waterfall read; immaterial — see note) |
| M5 Scale & Dominance | 2nd mcap of 4, top OPM of 3 | top-3 mcap & margin top-2→3 | 3 | PASS |
| M6 Technology/R&D | no R&D line | missing→0 (PEER DATA NEEDED) | 0 | PASS |
| M7 Regulatory/License | unregulated segment | unregulated→0 | 0 | PASS |
| M8 Distribution | no network figures | missing→0 | 0 | PASS |
| M9 Brand | GM proxy 6.71% vs peer med 7.36% | at/below→0 | 0 | PASS |
| M10 Switching Costs | rev +9/9; rec days -22.12 (a fall) | grew all yrs & rec days rose ≤10→5 | 5 | PASS (fall satisfies "rose ≤10") |
| M11 Network Effects | L3y 25.03% > P3y 22.36%; selling% declining | →5 | 5 | PASS (10y ≥ 6y two-window requirement met) |
| M12 Negative WC/Float | N/A (payables absent) | missing→0 | 0 | PASS |
| Moat score | | | 23/60 | sum re-added = 23 | PASS |
| Moats present (≥3) | M1,M3,M4,M5,M10,M11 | count = 6 | 6 | PASS |
| Moat classification | 6 present | 6+→FORTRESS | FORTRESS | PASS (count-based rule; label decoupled from 23/60 by design — as written) |

### Aggregation, confidence, matrix, deal-breakers
| Rule | Value | Verdict |
|---|---|---|
| Core = A+B+C+D | 13+5+15+7 = 40 | PASS |
| Grand total = Core+E+F | 40+0+23 = 63 | PASS |
| Data-confidence adjustment | 10 yrs → "10+ full", no downgrade, history_downgrade=false | PASS |
| Classification matrix | Core 40 ∈ 40-59 → AVERAGE (moat tier does not lift below Core 60) | PASS |
| Deal-breaker 1 (A<8) | A=13, not triggered | PASS |
| Deal-breaker 2 (B<8→max GOOD) | B=5, triggered, correctly noted non-binding under AVERAGE | PASS |
| Deal-breaker 3 (median ROCE<10) | 16.65%, no | PASS |
| Deal-breaker 4 (ΣCFO/PAT<0.50) | 1.28x, no | PASS |
| Deal-breaker 5 (pledge>15%) | NOT FOUND → cannot evaluate, treated as data gap not clean pass | PASS |
| Deal-breaker 6 (ND/EBITDA>3x AND IC<3x→AVOID) | ND/EBITDA 2.53x not >3x → AND fails → not triggered | PASS |
| Deal-breaker 7 (rev decline majority) | 0 declines, no | PASS |
| Deal-breaker 8 (PAT neg in last 3y) | FY24/25/26 all +ve, no | PASS |
| Deal-breaker 9 (history<3y) | 10y, no | PASS |
| Final classification | AVERAGE | PASS |

**Gate 0 FAIL:** none on rule application. One MINOR artifact-format gap:

| Location | Issue | Severity | Note |
|---|---|---|---|
| 01-gate0.md (ends L377) | Stage 1 mandates a closing fenced `stage: B01-gate0` YAML block; the report file has none. | MINOR | Every scored value is present and correct in prose and demonstrably propagated (B07 consumed the B01 YAML — core_score 40, moats_confirmed 6, moat_class FORTRESS all appear in 07-emoat). No decision impact; presentational/completeness only. |

Gate 0 verdict: rule application fully compliant. AVERAGE classification concurred.

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) COMPLIANCE TABLE
═══════════════════════════════════════════════════════════════════

### Category coverage (21 required)
All 20 scan categories (A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2,
H1-H3) plus R1 are individually addressed with an evidence treatment or an
explicit NO EVIDENCE FOUND. **21/21 addressed — PASS.**

### Scorecard: multiplier + matrix re-application (non-zero rows)
| ID | Text/summary evidence tier | Raw (matrix) | Multiplier applied | Correct multiplier | Adjusted | Verdict |
|---|---|---:|---|---|---:|---|
| A3 | 📄 | 1 (LL) | 1.0 | 1.0 | 1.0 | PASS |
| A4 | 🎙️/📄 (scored as 🎙️) | 1 (LM) | 0.7 | 0.7 (conservative) | 0.7 | PASS |
| B2 | 📄 | 3 (HM) | 1.0 | 1.0 | 3.0 | PASS |
| C1 | 🎙️ (summary) / scored 🎙️🔍 | 1 (LL) | 0.5 | ≤0.7 (used weakest, conservative) | 0.5 | PASS |
| E1 | 🎙️ | 1 (LM) | 0.7 | 0.7 | 0.7 | PASS |
| F1 | 📄 | 1 (LL) | 1.0 | 1.0 | 1.0 | PASS |
| F2 | 📄 | 4 (HH) | 1.0 | 1.0 | 4.0 | PASS |
| **H1** | **🎙️ (summary table row H1)** | 1 (LM) | **1.0 (📄)** | **0.7 (🎙️)** | 1.0 → should be 0.7 | **FAIL** |
| H2 | 📄 | 3 (HM) | 1.0 | 1.0 | 3.0 | PASS |
| H3 | 📄 | 3 (HM) | 1.0 | 1.0 | 3.0 | PASS |
| R1 | 📄 | 3 (HM) | 1.0 | 1.0 | 3.0 | PASS |

Raw likelihood×impact matrix mappings (HH=4, HM/MH=3, ML/LM/LL=1) all applied
correctly across every scored row.

**H1 FINDING (MINOR):** the maker's own Section 3 summary table classifies H1
"Industry consolidation beneficiary" as 🎙️ (the load-bearing evidence — India's
~70% copper-tube import dependency — is sourced to third-party research, and the
only 📄 item, the Rs 200 Lakh Tefabo bolt-on, is expressly discounted as "not a
competitor acquisition"). The Section 5 scorecard nonetheless applies the 📄
1.0x multiplier. This is exactly the "🎙️-only category scoring as if 📄"
pattern the rubric flags.
- Recomputed: raw 1 × 🎙️ 0.7 = **0.7 adjusted** (maker used 1.0).
- em_score effect: 20.9 → **20.6**, rounds to 21 either way.
- Classification band (12-24 = MODEST): **unchanged**. Severity MINOR (H1 is a
  Weak/inactive row, so the error does not touch the 5 active categories, all of
  which are genuinely 📄).

### Adjusted total, classification, completionist guard
| Rule | Value | Recompute | Verdict |
|---|---|---|---|
| Adjusted total (em_score) | 20.9 ≈ 21 | sum of adjusted column = 20.9 (20.6 if H1 corrected) | PASS |
| Classification band | MODEST (12-24) | 21 ∈ 12-24 → MODEST | PASS |
| Active-category count | 5 (B2,F2,H2,H3,R1) | matches Strong/Moderate rows; all genuinely 📄 | PASS |
| Completionist guard | 5 active < 12 trigger; recount stated | "📄 recount performed: ~16 documented items across 5 categories" — performed and explicit | PASS |
| capex_embedded_growth_pct (2C) | 14 | 80.8×8.82/5076.1 = 14.0% | PASS |
| Combined 6D | AVERAGE (Gate0 AVERAGE + MODEST forward, below EXPANSION lift threshold) | consistent | PASS |

**Emerging Moat FAIL:** 1 (H1 multiplier, MINOR). All 21 categories addressed;
completionist recount performed; the 5 active categories each carry genuine 📄
evidence (no active category is inflated from 🎙️). em_score 21 / MODEST concurred.

═══════════════════════════════════════════════════════════════════
## PART 3 — VALUATION (B11 / B10)
═══════════════════════════════════════════════════════════════════

DEFERRED to Phase 3. B10 and B11 do not exist yet; not audited. valuation
rules_checked = 0. recomputed_destination_pe and recomputed_decision left blank.

═══════════════════════════════════════════════════════════════════
## SUMMARY
═══════════════════════════════════════════════════════════════════
- Gate 0: 46 rules checked, rule application fully compliant; 1 MINOR
  artifact-format gap (missing closing YAML block, no decision impact).
  AVERAGE classification concurred.
- Emerging Moat: 34 rules checked, 1 MINOR fail (H1 multiplier 📄→should be 🎙️;
  em_score 20.9→20.6, MODEST unchanged). em_score 21 / MODEST concurred.
- Valuation: deferred to Phase 3, 0 rules checked.
- No CRITICAL or MAJOR findings. No recomputed value flips a band or the decision.
- Acceptance rate: 78/80 = 98%.
