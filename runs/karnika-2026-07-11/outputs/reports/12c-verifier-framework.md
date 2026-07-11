# STAGE 12C: VERIFIER C — FRAMEWORK ADHERENCE AUDIT
Company: Karnika Industries Ltd (KARNIKA) | Run date: 2026-07-11 | Model: claude-opus-4-8

**Scope note (phase 1):** This run executes ONLY the Gate 0 (B01) and Emerging
Moat (B07) compliance audits. The valuation-adherence audit (B11/B10) is
DEFERRED to phase 3 and is NOT run here; those artifacts do not yet exist. The
valuation section of the YAML block is emitted as `pending-phase-3` with no
findings. No valuation findings are fabricated.

Audit basis: rule application only (not company quality, not raw-number
sourcing — Verifier A owns numbers). Rubrics: prompts/01-gate-0-pipeline.md and
prompts/07-emerging-moat-pipeline.md. Framework docs (Master v3.3, Section 1B
v3.3, FTTCP v1.2) are relevant to the deferred valuation audit; for Gate 0 and
Emoat the stage prompts are the governing rubric.

---

## PART 1 — GATE 0 (B01) COMPLIANCE

Every block score was re-derived from the stated inputs using the rubric
thresholds. Values below are the auditor's independent recompute.

### Block A — Return on Capital (rubric prompts/01 L56-60)

| Rule | Inputs (report) | Recompute | Report | Verdict |
|---|---|---|---|---|
| EBIT FY25 = PBT+Int−OthInc | 2417.11+446.38−373.12 | 2490.37 | 2490.37 | PASS |
| EBIT FY26 | 3659.15+538.16−868.12 | 3329.19 | 3329.19 | PASS |
| ROCE FY25 = EBIT/(TA−CL) | 2490.37/7227.29 | 34.46% | 34.46% | PASS |
| ROCE FY26 | 3329.19/9611.07 | 34.64% | 34.64% | PASS |
| A1 median ROCE ≥25→5 | median(34.46,34.64)=34.55 | 5 | 5 | PASS |
| A2 min ROCE ≥15→5 | 34.46 | 5 | 5 | PASS |
| ROE FY25 (closing NW fallback) | 1803.05/7078.30 | 25.47% | 25.47% | PASS |
| ROE FY26 (avg NW) | 2667.73/8295.93 | 32.16% | 32.16% | PASS |
| A3 median ROE ≥20→5 | median(25.47,32.16)=28.82 | 5 | 5 | PASS |
| A4 ROCE latest≥earliest→5 | 34.64≥34.46 | 5 | 5 | PASS |
| **Block A total** | | **20** | **20** | **PASS** |

ROE closing-net-worth fallback for the earliest year is applied per rubric L34
("if opening net worth unavailable for the earliest year, use closing and state
so") — stated. PASS.

### Block B — Cash Generation Quality (rubric L63-69)

| Rule | Recompute | Report | Verdict |
|---|---|---|---|
| B1 cumCFO/cumPAT 2445.51/4470.78 = 0.547 → band 0.50-0.69 = 1 | 1 | 1 | PASS |
| B2 FCF+ years: FY25 −18.00, FY26 +2083.38 → 1/2 = 50% → 50-74 = 2 | 2 | 2 | PASS |
| B3 cumFCF/cumPAT 2065.38/4470.78 = 0.462 → 0.40-0.59 = 3 | 3 | 3 | PASS |
| B4 WC days 165.48 vs 219.17 = −53.69 → decreased >5 = 5 | 5 | 5 | PASS |
| **Block B total** | **11** | **11** | **PASS** |

WC-days components re-derived on Revenue basis (rubric L37-39 permits revenue
basis when COGS not disclosed; basis stated): FY25 R157.72 + I105.79 − P44.34 =
219.17; FY26 R109.70 + I82.44 − P26.66 = 165.48. Both reproduce. PASS.

### Block C — Growth (rubric L72-75) + CAGR edge rules (L44-52)

| Rule | Recompute | Report | Verdict |
|---|---|---|---|
| C1 Rev CAGR (22428.14/17254.85)^(1/1)−1 = 29.98% → ≥20 = 5 | 5 | 5 | PASS |
| C2 PAT CAGR (2667.73/1803.05)−1 = 47.96% → ≥20 = 5 | 5 | 5 | PASS |
| C3 positive YoY 1/1 = 100% → 5 | 5 | 5 | PASS |
| C4 47.96−29.98 = +17.98pp → ≥+3 = 5 | 5 | 5 | PASS |
| **Block C total** | **20** | **20** | **PASS** |

CAGR edge rules honoured: no negative/zero endpoint (both bases positive), no
loss-to-profit swing (both years positive) — correctly noted in data_notes; no
synthetic CAGR attempted. Single-period n=1 nature disclosed. PASS.

### Block D — Balance Sheet Strength (rubric L78-87), latest = FY26

| Rule | Recompute | Report | Verdict |
|---|---|---|---|
| D1 NetDebt/EBITDA 7039.64/3492.68 = 2.02x → 2-3x = 1 | 1 | 1 | PASS |
| D2 IC 3329.19/538.16 = 6.19x → 5-9.9 = 4 | 4 | 4 | PASS |
| D3 D/E 7048.77/9513.56 = 0.74 → 0.5-1.0 = 3 | 3 | 3 | PASS |
| D4 CR 15710.76/9290.78 = 1.69 → 1.5-1.99 = 4 | 4 | 4 | PASS |
| **Block D total** | **12** | **12** | **PASS** |

Not a bank/NBFC; standard bands correctly used (not CAR/PCR). PASS.

### Block E — Shareholder Alignment (rubric L90-96)

All four items N/A (no shareholding/pledge/contingent-liability data in inputs)
→ scored 0, per grounded-claims rule L21-23 (mark N/A, score 0, never estimate).
Block E 0/20. PASS (correct handling of a data gap, not an invented zero).

### Core score

A20 + B11 + C20 + D12 + E0 = **63**. Reproduces. PASS.

### Block F — Quantitative Moat (rubric L98-139)

| Test | Recompute vs rubric band | Report | Verdict |
|---|---|---|---|
| M1 Pricing Power: EBITDA margin 15.09%→15.58% (+0.49pp, ±2pp) AND revCAGR 29.98%≥10% → stable+growth = 3 | 3 | 3 | PASS |
| M2 Cost Adv: 15.58% vs peer median 13.40% = +2.18pp → 2-5pp above = 3 | 3 | 3 | PASS (basis caveat, MINOR-1) |
| M3 Cap Eff: FAT 37.23x>3x AND ROCE 34.64%>20% → 5 | 5 | 5 | PASS |
| M4 Stickiness: 0 decline yrs but rec days not ±10 → drops from 5 to "max 1 decline" tier = 3 | 3 | 3 | PASS |
| M5 Scale: PEER DATA NEEDED, full universe absent → 0 | 0 | 0 | PASS (conservative, MINOR-2) |
| M6 R&D: nil R&D → 0 | 0 | 0 | PASS |
| M7 Regulatory: unregulated segment → 0 | 0 | 0 | PASS |
| M8 Distribution: no quantified reach in inputs → 0 | 0 | 0 | PASS |
| M9 Brand: GM proxy 33.72% below peer → at/below = 0 | 0 | 0 | PASS (peer-median labeling, MINOR-1) |
| M10 Switching: rev grew AND rec days rose ≤10 (declined 48d) → 5 | 5 | 5 | PASS (literal test met) |
| M11 Network: <6yr, selling% unverifiable → conservative 0 | 0 | 0 | PASS (conservative, MINOR-2) |
| M12 Neg WC: WC days >45 both yrs → 0 | 0 | 0 | PASS |
| **Moat total** | 3+3+5+3+5 = **19** | **19** | **PASS** |

Moats present (≥3): M1, M2, M3, M4, M10 = 5 → **STRONG** (4-5 band). PASS.

### Grand total, classification, deal-breakers

| Rule | Recompute | Report | Verdict |
|---|---|---|---|
| Grand total 63+19 | 82 | 82 | PASS |
| Matrix Core 60-79 + STRONG → GOOD+ (raw) | GOOD+ | GOOD+ | PASS |
| Data-confidence <3yr → auto AVERAGE (L146) | AVERAGE | AVERAGE | PASS |
| Deal-breaker #9 history <3yr → AVERAGE (L160), years driving it stated (FY25,FY26) | AVERAGE | AVERAGE | PASS |
| Deal-breaker #4 cumCFO/PAT <0.50: 0.547 → NOT triggered, flagged watch | not triggered | not triggered | PASS |
| Deal-breakers #1,#2 (Block A/B <8) not triggered | — | — | PASS |
| Deal-breaker #3 median ROCE <10%: 34.55% not triggered | — | — | PASS |
| Deal-breaker #6 ND/EBITDA>3x AND IC<3x: 2.02x/6.19x not triggered | — | — | PASS |
| Deal-breakers #5,#7,#8 not evaluable / not triggered on available data, stated | — | — | PASS |
| FLAG-GATE0 required (class ≤AVERAGE w/ depressor) → emitted | present | present | PASS |
| Final classification | AVERAGE | AVERAGE | PASS |

**Gate 0 verdict: FULLY COMPLIANT.** Every block score, the moat scan, the
classification matrix, the data-confidence rule, all nine deal-breakers, the
CAGR edge rules, and the FLAG requirement were applied as written. No score,
band, or classification changes on recompute. Three MINOR labeling/conservatism
notes below carry zero score or classification impact.

---

## PART 2 — EMERGING MOAT (B07) COMPLIANCE

### Category coverage (rubric requires all 20 + R1 addressed or NO EVIDENCE)

21 rows present and addressed: A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2,
H1-H3, R1. No category force-fit; NO EVIDENCE FOUND stated explicitly for the 12
inactive categories. **PASS.**

### Scorecard — raw matrix + evidence multiplier re-derivation (rubric L126-132)

Matrix: HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0. Multiplier 📄1.0 /
🎙️0.7 / 🔍0.5.

| Cat | L×I | Raw (check) | Tier | Mult | Adjusted (check) | Report | Verdict |
|---|---|---|---|---|---|---|---|
| A3 | HM | 3 | 🎙️ | 0.7 | 2.1 | 2.1 | PASS |
| C1 | ML | 1 | 🎙️ | 0.7 | 0.7 | 0.7 | PASS |
| C2 | HL | 2 | 📄 | 1.0 | 2.0 | 2.0 | PASS on math; tier queried (MINOR-3) |
| D2 | HL | 2 | 📄 | 1.0 | 2.0 | 2.0 | PASS |
| E1 | MH | 3 | 📄 | 1.0 | 3.0 | 3.0 | PASS |
| F2 | LM | 1 | 📄 | 1.0 | 1.0 | 1.0 | PASS |
| H1 | HM | 3 | 📄 | 1.0 | 3.0 | 3.0 | PASS |
| H2 | HH | 4 | 📄 | 1.0 | 4.0 | 4.0 | PASS |
| R1 | ML | 1 | 🔍 | 0.5 | 0.5 | 0.5 | PASS |
| **Total** | | | | | **18.3** | **18.3** | **PASS** |

Sum reproduces exactly: 2.1+0.7+2.0+2.0+3.0+1.0+3.0+4.0+0.5 = 18.3.
Classification 12-24 → **MODEST MOAT DEVELOPMENT**. PASS.

### Evidence-tier discipline (Verifier rule 3: a 🎙️-only category must not score as 📄)

Checked each active row against its cited evidence:
- **A3** — machinery/margins are 📄 but the *moat mechanism* rests on management
  causal attribution; report deliberately took the LOWER 🎙️ tier ("attribution
  governs"). Correct conservative discipline. PASS.
- **C1** — AR ">90% repeat" downgraded to 🎙️/Weak because undercut by concall
  agent-concentration disclosure. Conservative. PASS.
- **C2** — scored **📄 1.0** for named new orders (Style Bazaar, Bumzy,
  Hopscotch) stated in a concall Q&A with undisclosed amounts, single-period.
  Per the taxonomy (L20-26), a concall statement not backed by a signed contract
  or committed capital is 🎙️. Named-counterparty specificity lends some
  documentary weight, but strictly this is a 🎙️ item. **MINOR-3** (see findings).
- **D2, E1, F2, H1, H2** — launch confirmed / store counts / consolidated
  financials / transcript-of-record promise-delivery / named acquisition
  counterparty: all genuinely 📄. PASS.
- **R1** — inference-only sector tailwind → 🔍 0.5. PASS.
- No 🎙️→📄 upgrade in the completionist recount (guard explicitly satisfied).

### Completionist recount (rubric L30-35, L112-116)

Recount performed and stated: "📄 recount performed: 11 documented items across
7 categories." Active-category count 7 is above the 3-6 base rate but below the
12-category re-examine trigger; the report explicitly re-examines and attributes
the cluster to a single event (Kidcity), not broad moat formation. **PASS.**

### Section 2C capex-embedded growth (rubric L50-52, arithmetic shown)

FAT 17254.85/625.19 = 27.6x; 347.60 × 27.6 = 9593.76L; /17254.85 = 55.6%.
Reproduces; distortion (asset-light job-work) flagged, not suppressed.
capex_embedded_growth_pct 55.6. **PASS.**

### Optionality register + combined assessment

Optionality register present with converting-evidence / first-appearance /
window columns per rubric L134-143; items are 🎙️/🔍/0-scored and watched, never
scored. PASS. Combined 6D: the report discloses the Master v3.3 combined matrix
was NOT among injected inputs and reasons the AVERAGE label transparently rather
than reading it off the framework — acceptable given the input gap (MINOR-5).

**Emerging Moat verdict: SUBSTANTIALLY COMPLIANT.** All 21 categories addressed,
multiplier and raw-matrix math reproduce to 18.3, completionist guard satisfied,
tier discipline sound except one MINOR over-tiering (C2). Recompute with C2 at
🎙️ (2×0.7=1.4) yields em_score 17.7 — still MODEST, no classification change.

---

## FINDINGS (all MINOR; no CRITICAL, no MAJOR)

| # | Sev | Location | Finding | Impact |
|---|---|---|---|---|
| MINOR-1 | MINOR | 01-gate0.md M9 (L207) / M2 (L200) | M9 cites "peer median 55.20% (KITEX)" — a "median" resting on a single peer's computable GM proxy; M2's peer EBITDA-margin comparison does not reconcile that Karnika's margin excludes Other Income while peer screener margins may not. Both are like-for-like basis imprecisions. | None. M9 → 0 regardless (Karnika 21pp below); M2 band buffer +2.18pp is comfortably inside the 2-5pp band. No score change. |
| MINOR-2 | MINOR | 01-gate0.md M5 (L203), M11 (L209) | M5 scored 0 (PEER DATA NEEDED) though Karnika sits in a known 4-company set as smallest mcap; a literal "top 5 = 1" reading was arguably available. M11 scored a conservative 0 with selling-% unverifiable. Both are conservative-zero readings. | None. Neither test reaches the ≥3 "present" bar at 1, so moats-present count (5) and STRONG class are unaffected. |
| MINOR-3 | MINOR | 07-emoat.md C2 (L200) / B07 scorecard | C2 assigned 📄 (1.0) to named new orders stated in a concall Q&A with undisclosed amounts and single-period visibility; taxonomy L20-26 places an un-contracted concall statement at 🎙️ (0.7). | Recompute em_score 18.3 → 17.7. Classification MODEST unchanged. No decision impact. |
| MINOR-4 | MINOR | 07-emoat.md F2 (L110-120) / input_gaps | F2 built directly from the two transcripts because the B05 promise-delivery record was not injected at this stage; rubric L96 expects a cross-reference to B05. Substitution is reasonable and disclosed. | None. Retrospective promise-delivery facts are transcript-of-record; F2 raw 1 / 📄 stands. Process note only. |
| MINOR-5 | MINOR | 07-emoat.md 6D (L260-262) | Combined classification reasoned without the Master v3.3 combined matrix (not among injected inputs); the report discloses this and reasons AVERAGE transparently. | None. Backward AVERAGE + forward MODEST would not clear a HIGH POTENTIAL/transition upgrade under the matrix either. |

---

## RECOMPUTED DESTINATION

- Gate 0 classification: **AVERAGE** — CONCUR (no change).
- Emerging Moat: **MODEST (18.3; 17.7 if C2 re-tiered)** — CONCUR, band unchanged.
- Destination PE / decision: **PENDING PHASE 3** (valuation audit deferred; B10/B11 do not exist). Not assessed, not fabricated.

## COVERAGE

Gate 0: all 5 core blocks (21 line items), all 12 moat tests, core/moat/grand
totals, moat-present count, classification matrix, data-confidence rule, all 9
deal-breakers, CAGR edge rules, FLAG requirement — 48 rule-checks, re-derived
from stated inputs. Emerging Moat: 21-category coverage, 9 active scorecard rows
(raw matrix + multiplier + adjusted), total, classification band, completionist
recount + guard, evidence-tier discipline on all active rows, 2C arithmetic,
optionality register, combined assessment — 46 rule-checks. Valuation: 0 (phase
3). One MINOR soft-fail (C2 tier); all other checks pass with no score,
threshold, or classification change.

---

```yaml
stage: B12c
company: "KARNIKA"
run_date: "2026-07-11"
model: claude-opus-4-8
status: complete
gate0:
  rules_checked: 48
  fails: []
emoat:
  rules_checked: 46
  fails:
    - "C2 assigned 📄(1.0) to un-contracted concall-stated new orders; taxonomy places at 🎙️(0.7); MINOR, em_score 18.3->17.7, class MODEST unchanged"
valuation:
  rules_checked: 0
  fails: []
  status: pending-phase-3
recomputed_destination_pe: ""   # pending phase 3 (valuation deferred)
recomputed_decision: ""         # pending phase 3; Gate0 AVERAGE and Emoat MODEST both CONCUR
findings:
  - {severity: "MINOR", location: "01-gate0.md M9/M2", note: "peer 'median' from single peer (M9) and unreconciled Other-Income basis vs peers (M2); no score change"}
  - {severity: "MINOR", location: "01-gate0.md M5/M11", note: "conservative zeros where a literal top-5=1 (M5) or trend read (M11) was arguable; moats-present count and STRONG class unaffected"}
  - {severity: "MINOR", location: "07-emoat.md C2", note: "evidence over-tiered 📄 vs 🎙️ for un-contracted concall orders; em_score 18.3->17.7, MODEST unchanged"}
  - {severity: "MINOR", location: "07-emoat.md F2", note: "F2 built from transcripts as B05 promise-delivery record not injected; disclosed, reasonable substitution, no score impact"}
  - {severity: "MINOR", location: "07-emoat.md 6D", note: "combined classification reasoned without injected Master v3.3 matrix; disclosed; AVERAGE stands"}
critical_count: 0
major_count: 0
minor_count: 5
acceptance_rate: 99            # 93 clean of 94 checked (C2 tier the sole soft-fail); valuation excluded, phase 3
```
