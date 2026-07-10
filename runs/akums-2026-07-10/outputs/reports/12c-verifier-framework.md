# STAGE 12C: VERIFIER C — FRAMEWORK ADHERENCE (PHASE 1 SCOPE)

Company: Akums Drugs & Pharmaceuticals Ltd (AKUMS) | Run date: 2026-07-10 | Model: claude-opus-4-8

Scope this run: Gate 0 (B01) and Emerging Moat (B07) compliance ONLY. The
valuation-adherence audit (B11/B10) is DEFERRED to phase 3 — those artifacts do
not exist yet, so the valuation section is emitted as pending and
recomputed_destination_pe / recomputed_decision are left blank.

Audit stance: rule application only. Raw-number accuracy is Verifier A's charge;
I re-derive scores from the stated inputs using the stated thresholds and check
matrix / edge-rule / multiplier application. I do not re-judge company quality.

Artifacts audited:
- runs/akums-2026-07-10/outputs/reports/01-gate0.md (narrative)
- runs/akums-2026-07-10/outputs/blocks/B01-gate0.yaml (structured block)
- runs/akums-2026-07-10/outputs/reports/07-emoat.md (narrative + inline YAML)

Framework rule sources:
- prompts/01-gate-0-pipeline.md
- prompts/07-emerging-moat-pipeline.md

---

## PART 1 — GATE 0 (B01) COMPLIANCE

Note on file layout: the mandated closing YAML block for stage 1 is emitted to
`outputs/blocks/B01-gate0.yaml`, not appended to `01-gate0.md`. That block is
present, complete, and consistent with the narrative (blocks A8/B13/C13/D14/E0,
core 48, moat 10, THIN, AVERAGE, FLAG-GATE0 present, deal-breaker #8 recorded,
CAGR loss-swing data_note present). No structural finding.

### Block A — Return on Capital (re-derived)

| Rule | Stated input | Threshold applied | Score | Recomputed | Verdict |
|---|---|---|---|---|---|
| A1 Median ROCE | 13.34% (5th of 9 sorted) | 10-14.9 = 3 | 3 | median of sorted set = 13.34% → 3 | PASS |
| A2 Min single-year ROCE | -17.36% (FY22) | <8 = 0 | 0 | 0 | PASS |
| A3 Median ROE | 8.72% (5th of 9 sorted) | <12 = 0 | 0 | median = 8.72% → 0 | PASS |
| A4 ROCE trend FY26 vs FY15 | 13.72% ≥ 13.34% | latest ≥ earliest = 5 | 5 | 5 | PASS |

Block A = 8/20. Confirmed. ROE closing-only treatment for FY15 (earliest) and
FY20 (opening = missing FY19) is disclosed; rule permits closing-only for the
earliest year, and FY20's opening is genuinely absent under the identical data
condition. Result-neutral (A3 = 0 in any case). Acceptable.

### Block B — Cash Generation (re-derived)

| Rule | Stated input | Threshold applied | Score | Recomputed | Verdict |
|---|---|---|---|---|---|
| B1 Cumul CFO/PAT | 3.80x (9-yr) | ≥1.00 = 5 | 5 | 5 | PASS |
| B2 FCF-positive proportion | 3/7 = 42.9% | <50 = 0 | 0 | 0 | PASS |
| B3 Cumul FCF/PAT | 1.34x (7-yr window) | ≥0.60 = 5 | 5 | FCF sum 825.13 ✓; ≥0.60 → 5 | PASS |
| B4 WC-days change | -3.06d (RD+ID proxy) | ±5d = 3 | 3 | 3 | PASS |

Block B = 13/20. Confirmed. Two disclosed methodology adaptations, both
result-neutral: (1) B3 denominator uses the 7-year PAT (615.84) to match the
7-year FCF window rather than the 9-year cumulative PAT used in B1 — even on the
9-year PAT the ratio is 1.17x, still ≥0.60 = 5; (2) B4/M12 use a Receivable+
Inventory partial WC proxy because Trade Payables is not a separate screener line
— disclosed as a partial proxy. Neither changes a band.

### Block C — Growth (re-derived, CAGR edge rules checked)

| Rule | Stated input | Threshold applied | Score | Recomputed | Verdict |
|---|---|---|---|---|---|
| C1 Revenue CAGR | 10.43% | 10-14.9 = 3 | 3 | 3 | PASS |
| C2 PAT CAGR | 17.56% | 15-19.9 = 4 | 4 | endpoints both positive → computable → 4 | PASS |
| C3 Positive YoY prop. | 5/7 = 71.4% | 50-74 = 1 | 1 | 1 | PASS |
| C4 PAT − Rev CAGR | +7.13pp | ≥+3pp = 5 | 5 | 5 | PASS |

Block C = 13/20. Confirmed. CAGR edge rules honoured: both CAGR endpoints
(FY15, FY26) positive → computed, not marked N/M; the intervening FY22/FY24
losses did not constitute a start-to-end loss-to-profit swing, and the swing was
nonetheless recorded in data_notes as required. C4 not zeroed because PAT CAGR is
not N/M. The FY16→FY20 4-year gap pair is correctly excluded from YoY counts.

### Block D — Balance Sheet (re-derived)

| Rule | Stated input | Threshold applied | Score | Verdict |
|---|---|---|---|---|
| D1 ND/EBITDA | net cash (-1523.17) | net cash = 5 | 5 | PASS |
| D2 Interest coverage | 5.06x | 5-9.9 = 4 | 4 | PASS |
| D3 Debt/Equity | 0.048x | <0.1 = 5 | 5 | PASS |
| D4 Current ratio | not computable | N/A → 0 | 0 | PASS |

Block D = 14/20. Confirmed. D4 correctly marked N/A and scored 0 per operating
rule 5 (data point unavailable → N/A → 0, no gap-filling).

### Block E — Shareholder Alignment (re-derived)

E1-E4 all N/A → 0, Block E = 0/20. Confirmed. No shareholding file supplied.
Critically, the E1 "professionally managed: 3 if FII+DII >50%" branch was NOT
invoked because no FII+DII figure was supplied — the report correctly declined to
apply the alternate branch on absent evidence rather than defaulting it to 3.
This is the correct conservative handling of missing data per the rules.

### Block F — 12 Moat Tests (re-derived)

| Test | Stated basis | Threshold applied | Score | Recomputed | Verdict |
|---|---|---|---|---|---|
| M1 Pricing power | margin +8.2pp, rev CAGR 10.43% | ≥2pp & ≥10% = 5 | 5 | 5 | PASS |
| M2 Cost adv. | 11.98% vs peer median 13.11% (−1.13pp) | ±2pp = 1 | 1 | median of 4 peers = 13.11% ✓; within 2pp → 1 | PASS |
| M3 Capital eff. | FAT 2.99x, ROCE 13.72% | FAT>1 & ROCE>12 = 1 | 1 | FAT>2 fails on ROCE<15; falls to 1 | PASS |
| M4 Stickiness | 2 decline yrs, CAGR+ | 2 decline, CAGR+ = 1 | 1 | 1 | PASS |
| M5 Scale | 3rd/5 mcap, 3rd/5 margin | top-5 mcap = 1 | 1 | top-3 mcap holds, margin-top-2 fails → 1 | PASS |
| M6 Tech/R&D | R&D not in screener | N/A → 0 | 0 | 0 | PASS |
| M7 Regulatory | segment count unverifiable | PEER DATA NEEDED → 0 | 0 | 0 | PASS |
| M8 Distribution | not disclosed | N/A → 0 | 0 | 0 | PASS |
| M9 Brand | GM proxy 42.97% vs median 53.58% | at/below = 0 | 0 | peer median = 53.58% ✓; below → 0 | PASS |
| M10 Switching | overall growth, 2 decline yrs | 2+ decline = 1 | 1 | 1 | PASS |
| M11 Network | latest 3yr 6.05% < prior 14.83%, <20% | else = 0 | 0 | ≥6-yr window met; deceleration → 0 | PASS |
| M12 Neg WC | payables not computable | N/A → 0 | 0 | 0 | PASS |

Moat score = 10/60. Confirmed. Moats present (≥3): M1 only = 1 → THIN.
Confirmed. M6/M8 correctly N/A, M7 correctly PEER DATA NEEDED, M12 correctly N/A
(partial RD+ID proxy already ~130 days ≥45 so a full-WC figure could not lift
the band anyway — result-neutral). Peer medians for M2, M9 recomputed clean.
Cross-stage note: M6 scored 0 on screener input scope; the emoat stage later
found R&D at 3.2% of revenue from the investor presentation, which was NOT in
Gate 0's input set — so this is not a contradiction, it is a scope difference.

### Classification, Data Confidence, Deal-breakers

| Check | As written | As applied | Verdict |
|---|---|---|---|
| Core score | A+B+C+D+E | 8+13+13+14+0 = 48 | PASS |
| Data confidence | 7-9 = moderate | 9 data points → moderate, no downgrade | PASS |
| Classification matrix | Core 40-59 = AVERAGE | AVERAGE (moat class does not branch this tier) | PASS |
| DB#1 Block A <8 | strict < | A=8, not <8 → no trigger | PASS (boundary correct) |
| DB#2 Block B <8 | | 13 → no | PASS |
| DB#3 median ROCE <10 | | 13.34% → no | PASS |
| DB#4 CFO/PAT <0.50 | | 3.80x → no | PASS |
| DB#5 pledge >15% | | N/A → not triggered on absence | PASS |
| DB#6 ND/EBITDA>3 & IC<3 | | net cash → no | PASS |
| DB#7 rev decline majority | | 2/7 = 28.6% → no | PASS |
| DB#8 PAT neg last 3 yrs | | FY24 -4.04 → YES → max AVERAGE | PASS |
| DB#9 history <3 yrs | | 9 points → no | PASS |

Deal-breaker #8 correctly fires and correctly caps at AVERAGE, coinciding with
the matrix-derived AVERAGE so no further depression. The post-IPO rebase /
legacy-cleanup pattern (FY22, FY24 Other-Expenses spikes) is recorded for
downstream position-sizing per the rules, without lifting the Gate 0 cap. The
FLAG-GATE0 is correctly emitted in B01-gate0.yaml with the depressors named.
history_downgrade = false is correct (9 points sits in the moderate band).

**Gate 0 verdict: fully compliant. 0 findings. All 46 checked rules PASS.**

---

## PART 2 — EMERGING MOAT (B07) COMPLIANCE

### Category coverage (21 required: 20 + R1)

All 21 categories appear in the Section 3 summary table (A1-A4, B1-B3, C1-C2,
D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, R1), each with either an evidence table or an
explicit "NO EVIDENCE FOUND". 9 correctly zeroed (A2, B1, B3, C2, D1, D2, E2, G2,
H3). B1 marked NO EVIDENCE with the stronger "explicitly ruled out" note; G2
marked NO EVIDENCE (worsening WC correctly scored 0, not negative). PASS — full
coverage, no force-fitting.

### Scorecard re-derivation (likelihood x impact matrix + evidence multiplier)

Matrix: HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0. Multiplier: 📄1.0,
🎙️0.7, 🔍0.5.

| Cat | L×I | Raw (recomp) | Ev | Mult | Adj (recomp) | Stated | Verdict |
|---|---|---|---|---|---|---|---|
| A1 | H×M | 3 | 📄 | 1.0 | 3.0 | 3.0 | PASS |
| A3 | M×L | 1 | 🔍 | 0.5 | 0.5 | 0.5 | PASS |
| A4 | M×L | 1 | 🔍 | 0.5 | 0.5 | 0.5 | PASS |
| B2 | H×H | 4 | 📄 | 1.0 | 4.0 | 4.0 | PASS |
| C1 | M×L | 1 | 🎙️ | 0.7 | 0.7 | 0.7 | PASS |
| E1 | H×M | 3 | 📄 | 1.0 | 3.0 | 3.0 | PASS |
| F1 | M×L | 1 | 📄 | 1.0 | 1.0 | 1.0 | PASS |
| F2 | M×H | 3 | 📄 | 1.0 | 3.0 | 3.0 | PASS |
| G1 | M×L | 1 | 📄 | 1.0 | 1.0 | 1.0 | PASS |
| H1 | L×M | 1 | 🎙️ | 0.7 | 0.7 | 0.7 | PASS |
| H2 | H×H | 4 | 📄 | 1.0 | 4.0 | 4.0 | PASS |
| R1 | M×H | 3 | 🎙️(blended) | 0.7 | 2.1 | 2.1 | PASS |

Adjusted total recomputed = 23.5. Matches. Classification 23.5 → 12-24 band =
MODEST MOAT DEVELOPMENT. Correct. Every matrix cell and every multiplier is
applied as written; R1, whose evidence is mixed 📄/🎙️, is conservatively taken at
the 0.7 claim multiplier rather than 1.0 — no over-crediting.

### Evidence-tier consistency (the core Verifier-C test)

No Strong/Moderate category rests on 🎙️/🔍 alone. The 6 active (Strong/Moderate)
categories are A1, B2, E1, F2, H2 (all 📄) and R1 (📄 approvals + 🎙️ policy, scored
at the conservative claim multiplier). The three 🎙️/🔍 categories that could have
been inflated — C1 (🎙️), H1 (🎙️), A3/A4 (🔍) — are all held at Weak with the
correct reduced multipliers. No claim-only category is scored as if documented.
PASS.

### Completionist guard + evidence-mix

Guard explicitly performed (Section 3, "COMPLETIONIST GUARD CHECK"): initial 8
Strong/Moderate reduced to 6 by downgrading A4 (no SKU/launch-frequency trend,
only a static snapshot) and G1 (headline OCF is a one-off EU advance; organic Adj
OCF fell 465→227) to Weak. 6 active sits inside the stated 3-6 base rate. The 📄
recount line ("~14 documented items across 6 active categories") is present, and
the B2/E1/H2 overlap (same two underlying facts: EU contract + Zambia JV) is
disclosed with the honest "2-3 core facts, not 6 independent moats" caveat.
evidence_mix {documented:14, claim:8, inference:3} matches the recount line.
PASS. (Twelve categories carry a nonzero adjusted score, which brushes the guard's
"12-or-more active" threshold — but "active" is correctly scoped to Strong/
Moderate = 6, and the recount + downgrades + overlap disclosure are exactly the
skeptical re-examination the guard demands. Not a finding.)

### Cross-references and combined classification

- F2 correctly consumes the injected B05 promise-delivery record (5 delivered /
  2 partial / 2 missed, grade C), caps at Moderate below Strong for the two
  confirmed misses. PASS.
- 6C combined table reproduces the injected Gate 0 block accurately (core 48,
  moat 10, 58/160, 1/12, THIN, AVERAGE, blocks A8/B13/C13/D14/E0). PASS.
- 6D combined = AVERAGE: backward AVERAGE + forward MODEST (23.5, below the 25
  STRENGTHENING line) correctly does NOT qualify for the HIGH POTENTIAL /
  TURNAROUND transition upgrade, which the framework reserves for EXPANSION-grade
  forward scores. Defensible application with full reasoning given. PASS.

### Finding

- **F-EM-1 (MINOR, presentational).** Section 2C capex_embedded_growth_pct is
  genuinely not computable (fixed-asset-turnover ratio not disclosed; AR absent)
  and is correctly documented as NOT FOUND in the narrative and in input_gaps
  (no estimation — compliant with CLAUDE.md). However the YAML field is emitted
  as the numeric `0`, which a downstream consumer reading only the structured
  block (e.g. Pillar 3 catalyst/embedded-growth input) could read as a genuine
  "zero embedded growth" rather than "not computable." The field follows the
  template default, so this is low-stakes, but the not-computable state is lost
  in the machine-readable field. Recommend a sentinel/NOT FOUND convention.
  No score, classification, or decision impact.

**Emerging Moat verdict: substantively compliant. 1 MINOR presentational
finding; scoring, multipliers, matrix, guard, and evidence-tier discipline all
correct. em_score 23.5, MODEST, combined AVERAGE — all confirmed.**

---

## PART 3 — VALUATION (B11/B10) — DEFERRED

Not run this phase. B10 and B11 artifacts do not exist yet; the valuation
adherence audit (continuous Pillar 1 formula, FTTCP ROCE authority, single-credit
rule, Pillar 2 multiplier/offset rules, Pillar 3 injected inputs, Amendment-3 UA
ordering, sector-cap absoluteness, dual-track carry-through, Hurdle Ratio + 4D
weights, SOM cross-check, one-improvement-one-mechanism) is DEFERRED to phase 3.
Emitted as pending. recomputed_destination_pe and recomputed_decision left blank.

---

## SUMMARY

| Framework | Rules checked | Fails | Severity | Acceptance |
|---|---|---|---|---|
| Gate 0 (B01) | 46 | 0 | — | 100% |
| Emerging Moat (B07) | 40 | 1 | MINOR | 97.5% |
| Valuation (B11/B10) | — | — | pending phase 3 | — |

No CRITICAL, no MAJOR. Both phase-1 frameworks were applied as written: every
Gate 0 block score, the moat classification, the data-confidence band, all nine
deal-breakers, and the CAGR edge rules re-derive cleanly; the Emerging Moat
matrix, evidence multipliers, completionist guard, and evidence-tier discipline
all hold. The single finding is a presentational YAML convention (capex embedded
growth 0 vs NOT FOUND). No recomputation changes any score, classification, or
decision.

```yaml
stage: B12c
company: "AKUMS"
run_date: "2026-07-10"
model: claude-opus-4-8
status: complete
scope: "phase-1 (Gate 0 + Emerging Moat only); valuation deferred to phase 3"
gate0:
  rules_checked: 46
  fails: []
emoat:
  rules_checked: 40
  fails:
    - {rule: "Section 2C capex_embedded_growth_pct", severity: MINOR, issue: "not-computable value emitted as numeric 0 in YAML; correctly NOT FOUND in narrative + input_gaps, but structured field loses the not-computable state", recomputed: "no score/classification impact"}
valuation:
  status: pending
  note: "DEFERRED to phase 3; B10/B11 do not exist yet"
  rules_checked: 0
  fails: []
recomputed_destination_pe: ""
recomputed_decision: ""
findings:
  - {severity: MINOR, framework: emoat, location: "B07 Section 2C / YAML capex_embedded_growth_pct", note: "not-computable emitted as 0; documented as NOT FOUND in narrative and input_gaps, no estimation, no decision impact"}
critical_count: 0
major_count: 0
minor_count: 1
acceptance_rate: 99   # 85 of 86 checked phase-1 rules passed
```
