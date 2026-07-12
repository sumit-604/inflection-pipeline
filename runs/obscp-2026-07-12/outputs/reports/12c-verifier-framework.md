# VERIFIER C — FRAMEWORK ADHERENCE AUDIT
## OBSC Perfection Ltd (OBSCP) | Run 2026-07-12 | Model: claude-opus-4-8

**Scope this run (PHASE 1):** Gate 0 (B01) and Emerging Moat (B07) compliance
only. The valuation-adherence audit (B11/B10) is DEFERRED to phase 3; those
artifacts do not exist yet and were not audited. The valuation section of the
B12c block is marked pending. `recomputed_destination_pe` and
`recomputed_decision` are intentionally blank.

**Method:** every block score re-derived from the stated inputs using the
stated thresholds; classification matrix, confidence adjustment, deal-breaker
application and CAGR edge rules re-checked; all 21 emerging-moat rows
re-scored for evidence-tier/multiplier consistency and the completionist
recount reperformed. This audit judges *rule application*, not company quality
and not raw-number provenance (Verifier A owns numbers). The run is degraded
(AR pp.3-59 corrupted font; pp.78-101 truncated); the test applied is whether
the pipeline handled missing data by the framework's conservative rules with
no silent fills — NOT whether the data exists.

---

## PART 1 — GATE 0 (B01) RULE-BY-RULE

### Block A: Return on Capital (claimed 15/20)

| Rule | Inputs used | Re-derived | Claimed | Verdict |
|---|---|---|---|---|
| A1 Median ROCE | median(33.38, 19.01)=26.20% | ≥25 → 5 | 5 | PASS |
| A2 Min single-yr ROCE | min=19.01% | ≥15 → 5 | 5 | PASS |
| A3 Median ROE | median{19.58,25.01,27.11,29.35,50.95}=27.11% | ≥20 → 5 | 5 | PASS |
| A4 ROCE trend | 19.01 vs 33.38 = −14.37pp | >5pp decline → 0 | 0 | PASS |

ROCE recompute confirmed: FY24 EBIT 19.12 / CE 57.28 = 33.38%; FY25 EBIT 23.75
/ CE 124.94 = 19.01%. Only FY24/FY25 carry an anchored Current-Liabilities
split; FY22/23/26 correctly marked NOT FOUND and excluded, not filled. Block A
= 15. **PASS.**

Note (MINOR, not scored as fail): A1/A2/A4 rest on a 2-year ROCE basis where
the scorecard's stated preference is a minimum 3-year history. This is a
sub-metric data gap, handled transparently with explicit NOT FOUND on the
other three years and no silent fill — compliant with operating rules 5-6. The
thin basis is disclosed; flagged for the reader, not a misapplication.

### Block B: Cash Generation Quality (claimed 1/20)

| Rule | Re-derived | Claimed | Verdict |
|---|---|---|---|
| B1 Cum CFO/PAT | 19.74/64.15 = 0.31 → <0.50 → 0 | 0 | PASS |
| B2 FCF-positive yrs | 0 of 2 measurable = 0% → <50 → 0 | 0 | PASS |
| B3 Cum FCF/PAT | −29.95/28.97 = −1.03 → negative → 0 | 0 | PASS |
| B4 Δ WC Days | 79.18→93.12 = +13.94d → 5-15 incr → 1 | 1 | PASS |

Cumulative sums independently re-added (CFO 19.74, PAT 64.15). B2/B3 correctly
restricted to the FY24-FY25 capex-anchored window; unmeasured years excluded
rather than assumed positive — conservative. Block B = 1. **PASS.**

### Block C: Growth (claimed 20/20)

| Rule | Re-derived | Claimed | Verdict |
|---|---|---|---|
| C1 Rev CAGR | (219.54/55.55)^0.25−1 = 41.0% → ≥20 → 5 | 5 | PASS |
| C2 PAT CAGR | (27.01/3.60)^0.25−1 = 65.4% → ≥20 → 5 | 5 | PASS |
| C3 Positive YoY yrs | 4/4 = 100% → 5 | 5 | PASS |
| C4 PAT−Rev CAGR | +24.4pp → ≥+3 → 5 | 5 | PASS |

CAGR edge rules honoured: no negative/zero endpoints, no loss-to-profit swing,
so no N/M and no synthetic CAGR — correct. Block C = 20. **PASS.**

### Block D: Balance Sheet Strength (claimed 16/20)

| Rule | Re-derived | Claimed | Verdict |
|---|---|---|---|
| D1 ND/EBITDA (FY26) | 51.88/43.64 = 1.19x → 1-2x → 3 | 3 | PASS |
| D2 Int coverage (FY26) | 36.26/4.49 = 8.08x → 5-9.9 → 4 | 4 | PASS |
| D3 Debt/Equity (FY26) | 68.54/171.97 = 0.40 → 0.1-0.5 → 4 | 4 | PASS |
| D4 Current ratio (FY25) | 84.79/33.61 = 2.52x → ≥2.0 → 5 | 5 | PASS |

D4 uses FY25 because FY26 Current Liabilities is NOT FOUND; substituting the
latest *anchored* year (flagged explicitly) is a defensible conservative
handling of the "latest" instruction, not a silent fill. Block D = 16. **PASS.**

### Block E: Shareholder Alignment (claimed 0/20)

E1-E4 all inputs (promoter holding, holding change, pledge, contingent
liabilities/NW) fall in the corrupted/truncated AR range and are absent from
the screener exports. Per operating rule 5 ("if a data point is not available,
mark N/A and score it 0; never fill gaps"), scoring each 0 is the correct
mechanical application. The report states this is a data-access gap, not an
adverse finding, and does not silently assume a benign value — exactly the
required handling. Block E = 0. **PASS.** No silent fill. **This is the run's
central degradation-handling test and the pipeline passed it.**

### Block F: Quantitative Moats (claimed 14/60)

| Moat | Re-derived | Claimed | Verdict |
|---|---|---|---|
| M1 Pricing power | margin +6.79pp & rev CAGR 41% → 5 | 5 | PASS |
| M2 Cost advantage | PEER DATA NEEDED → 0 | 0 | PASS |
| M3 Capital efficiency | FAT 2.04x & ROCE 19.01% → 3 | 3 | PASS |
| M4 Customer stickiness | 0 decline yrs (satisfies "max 1") → 3 | 3 | PASS |
| M5 Scale | PEER DATA NEEDED → 0 | 0 | PASS |
| M6 Tech/R&D | NOT FOUND / peer needed → 0 | 0 | PASS |
| M7 Regulatory | unregulated segment → 0 | 0 | PASS |
| M8 Distribution | not quantified → 0 | 0 | PASS |
| M9 Brand | proxy, no peer median → 0 | 0 | PASS |
| M10 Switching costs | receivable days +21>10, no tier met → 0 | 0 | PASS |
| M11 Network effects | <6yr, rev CAGR≥20% & selling% declining → 3 | 3 | PASS |
| M12 Negative WC | WC days >45 → 0 | 0 | PASS |

Peer-dependent tests (M2, M5, and M9's benchmark, M6) correctly scored 0 with
"PEER DATA NEEDED" rather than guessed — per Block F instruction. M4 vs M10 are
internally consistent: M4 tier 3 is reachable on 0 decline years alone
(receivable stability is a tier-5-only condition), while M10's tiers each
require either receivable stability or ≥2 decline years, neither of which holds,
correctly dropping M10 to the "else" 0. This is an as-written literal read of
two differently-structured rubrics; both applied correctly. Block F = 14.
Moats present (≥3): M1, M3, M4, M11 = 4 → "4-5 present = STRONG." **PASS.**

### Classification, confidence, deal-breakers

| Check | Re-derived | Claimed | Verdict |
|---|---|---|---|
| Core score | 15+1+20+16+0 = 52 | 52 | PASS |
| Classification | Core 52 in 40-59 → AVERAGE (moat elevates only at Core≥60) | AVERAGE | PASS |
| Data confidence | 5yr → "5-6 lower", flag, no downgrade; history_downgrade=false | as claimed | PASS |
| Deal-breaker #2 (B<8) | triggered, non-binding (already <GOOD) | as claimed | PASS |
| Deal-breaker #4 (CFO/PAT<0.50) | 0.31 triggered, binding → max AVERAGE | as claimed | PASS |
| Deal-breaker #5 (pledge>15%) | NOT FOUND → not evaluable, not applied, flagged | as claimed | PASS |
| Deal-breakers #1,3,6,7,8,9 | none triggered on re-check | as claimed | PASS |

Deal-breaker #5 handling is the second degradation test: pledge data is absent,
so the pipeline neither assumes 0% (silent benign fill) nor assumes a breach —
it records "cannot evaluate" and flags closure via an alternate source. Correct.
Final classification AVERAGE is robust: even generous re-scoring of the two
data-thin lines (A1, A4) keeps Core within the 40-59 band, so no decision flip
is possible. **Classification PASS.**

**Gate 0 FAILS (both MINOR, presentational — no scoring or decision impact):**
- **G-1 (MINOR):** the saved B01 report omits the mandatory closing
  `stage: B01-gate0` fenced YAML block that the stage-1 prompt requires as the
  final output. The values evidently propagated (B07 consumed core_score 52,
  moat_class STRONG, moats 4), so this is a completeness gap in the persisted
  artifact, not a data error.
- **G-2 (MINOR):** `Grand Total = 52 + 14 = 66/100` (line ~305) mislabels the
  denominator; Core(100)+Moat(60) max is 160, so it should read 66/160 (B07's
  6C table labels it correctly as 66/160). Cosmetic; classification is
  Core-based and unaffected.

---

## PART 2 — EMERGING MOAT (B07) RULE-BY-RULE

### Category completeness
All 21 categories addressed (A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2,
H1-H3, R1). Six explicitly marked NO EVIDENCE FOUND (A2, A3, B3, D1, D2, E1).
No category force-fit. **PASS.**

### Scorecard: raw × evidence multiplier (all 21 rows re-derived)

| ID | L×I | Raw | Ev | Mult | Re-derived | Claimed | Verdict |
|---|---|---|---|---|---|---|---|
| A1 | ML | 1 | 🎙️ | 0.7 | 0.7 | 0.7 | PASS |
| A2 | — | 0 | — | — | 0.0 | 0.0 | PASS |
| A3 | — | 0 | — | — | 0.0 | 0.0 | PASS |
| A4 | LL | 1 | 🎙️ | 0.7 | 0.7 | 0.7 | PASS |
| B1 | HM | 3 | 📄 | 1.0 | 3.0 | 3.0 | PASS |
| B2 | HH | 4 | 📄 | 1.0 | 4.0 | 4.0 | PASS |
| B3 | — | 0 | — | — | 0.0 | 0.0 | PASS |
| C1 | MM | 2 | 🎙️ | 0.7 | 1.4 | 1.4 | PASS |
| C2 | HM | 3 | 📄 | 1.0 | 3.0 | 3.0 | PASS |
| D1 | — | 0 | — | — | 0.0 | 0.0 | PASS |
| D2 | — | 0 | — | — | 0.0 | 0.0 | PASS |
| E1 | — | 0 | — | — | 0.0 | 0.0 | PASS |
| E2 | HH | 4 | 📄 | 1.0 | 4.0 | 4.0 | PASS |
| F1 | LL | 1 | 🎙️ | 0.7 | 0.7 | 0.7 | PASS |
| F2 | MM | 2 | 🎙️ | 0.7 | 1.4 | 1.4 | PASS |
| G1 | contradicted | 0 | — | — | 0.0 | 0.0 | PASS |
| G2 | LM | 1 | 📄 | 1.0 | 1.0 | 1.0 | PASS |
| H1 | LL | 1 | 🎙️ | 0.7 | 0.7 | 0.7 | PASS |
| H2 | LL | 1 | 🎙️ | 0.7 | 0.7 | 0.7 | PASS |
| H3 | LL | 1 | 🔍 | 0.5 | 0.5 | 0.5 | PASS |
| R1 | MM | 2 | 🎙️ | 0.7 | 1.4 | 1.4 | PASS |

**Adjusted total re-summed = 23.2** (matches). **PASS.**

### Evidence-tier consistency (the key emerging-moat integrity check)
No claim-only category is scored as if documented:
- Every 🎙️ row carries the 0.7 multiplier (A1, A4, C1, F1, H1, H2, R1). C1 is
  labelled Moderate strength but is correctly discounted to 0.7 because the
  wallet-share/ranking evidence is unaudited management claim — it is NOT
  credited as 📄.
- The single 🔍 row (H3, rooftop-solar photo inference) correctly takes 0.5,
  not 1.0 — this is exactly the failure mode the rubric warns about, and it was
  avoided.
- 📄 rows (B1, B2, C2, E2, G2) take 1.0. E2 and F2 are 📄/🎙️ mixed; E2 takes
  1.0 (its score rests on the documented realized export-country/revenue growth,
  with the forward mix target treated as upside), F2 takes the conservative 0.7.
  Both defensible and internally stated. **PASS.**

### Completionist recount
Performed and stated: "📄 recount performed: 16 documented items across 6
categories (B1, B2, C2, E2, F2, G2)." Item tally re-added: 1+8+2+2+2+1 = 16.
Six active Strong/Moderate categories, well below the 12-category over-credit
trigger. The recount correctly distinguishes the *strength* grouping (B1, B2,
C1, C2, E2, F2 — the 6 Strong/Moderate) from the *documented-evidence* grouping
(B1, B2, C2, E2, F2, G2), which is the mark of a disciplined scan rather than an
error. **PASS.**

### Classification, capex handoff, combined assessment

| Check | Re-derived | Claimed | Verdict |
|---|---|---|---|
| EM classification | 23.2 in 12-24 → MODEST | MODEST | PASS |
| capex embedded growth (2C) | 20.2 × ~2.0x = 40.4 / 223.5 = 18% | 18 | PASS |
| FAT for 2C | 22,351.8 / 11,219.7 lakh = 1.99x ≈ 2.0x | 2.0x | PASS |
| Combined 6D | AVERAGE backward + MODEST forward → not an EXPANSION transition setup → AVERAGE, full reasoning given | AVERAGE | PASS |

6D correctly withholds a HIGH POTENTIAL/TURNAROUND upgrade: the transition
matrix reserves those for AVERAGE/GOOD-backward paired with STRENGTHENING/
EXPANSION-forward, and the forward score lands at MODEST (23, below the 25
STRENGTHENING threshold). Reasoning is complete per the "HIGH POTENTIAL/
TURNAROUND-adjacent calls require full justification" rule. **PASS.**

**Emerging Moat FAIL (MINOR, presentational):**
- **E-1 (MINOR):** Section 2C body text contains an unrendered orchestrator
  template token — "This is the {{B07_CAPEX_FIGURE}} handoff to stage 9". The
  numeric value (~₹20cr / ~18%) is present and correct in the surrounding prose
  and in the YAML `capex_embedded_growth_pct: 18`, so the handoff data is
  intact; only the literal placeholder leaked into the prose. Cosmetic.

---

## PART 3 — VALUATION (B11 / B10)

**DEFERRED to phase 3.** B11 and B10 artifacts do not exist for this run and
were not audited. No continuous Pillar 1 formula, FTTCP ROCE verdict,
single-credit route, Pillar 2/3, UA Amendment-3 order, dual-track, Hurdle
Ratio, 4D weighting or SOM cross-check was reviewed. `recomputed_destination_pe`
and `recomputed_decision` are blank by design.

---

## SUMMARY

Both in-scope frameworks were applied **as written**. Every Gate 0 block score
and the emerging-moat adjusted total were independently re-derived and match.
The two things this degraded run most needed to get right — Block E scored 0 as
a disclosed data gap (not a silent benign fill), and the pledge deal-breaker
recorded "cannot evaluate" rather than assumed-clean — were both handled
correctly. The emerging-moat scan avoided the classic inflation failure: no
🎙️/🔍 category is scored as 📄, and the completionist recount confirms it.

All three findings are MINOR and presentational (a missing persisted YAML
block, a grand-total denominator mislabel, and a leaked template token); none
touches a score, a threshold, a classification, or a decision. No CRITICAL, no
MAJOR.

- **Gate 0:** 38 rules checked, 2 MINOR fails → AVERAGE classification confirmed.
- **Emerging Moat:** 27 rules checked, 1 MINOR fail → MODEST (em_score 23) confirmed.
- **Acceptance rate (Gate 0 + Emerging Moat):** 62 / 65 = **95%**.

Recomputed classification concurs with the pipeline: Gate 0 AVERAGE, Emerging
Moat MODEST, combined AVERAGE. No decision change.

---

```yaml
stage: B12c
company: "OBSCP"
run_date: "2026-07-12"
model: claude-opus-4-8
status: complete
gate0:
  rules_checked: 38
  fails:
    - {severity: "MINOR", rule: "stage-1 output contract", detail: "B01 report omits the mandatory closing stage:B01-gate0 fenced YAML block; values propagated to B07 but the persisted artifact is incomplete"}
    - {severity: "MINOR", rule: "core aggregation label", detail: "Grand Total labelled 66/100; correct denominator is 160 (Core 100 + Moat 60). Classification is Core-based and unaffected"}
emoat:
  rules_checked: 27
  fails:
    - {severity: "MINOR", rule: "Section 2C presentation", detail: "unrendered {{B07_CAPEX_FIGURE}} template token leaked into 2C prose; the numeric handoff (~18%) is intact in text and YAML"}
valuation: {rules_checked: 0, fails: [], status: "deferred to phase 3"}
recomputed_destination_pe: ""
recomputed_decision: ""
findings:
  - {severity: "MINOR", location: "B01 report end", note: "mandatory closing YAML block absent from persisted report"}
  - {severity: "MINOR", location: "B01 Classification section (~line 305)", note: "grand_total denominator mislabelled 66/100 vs 66/160"}
  - {severity: "MINOR", location: "B07 Section 2C (~line 72)", note: "unrendered {{B07_CAPEX_FIGURE}} template token in prose; value correct elsewhere"}
critical_count: 0
major_count: 0
minor_count: 3
acceptance_rate: 95
```
