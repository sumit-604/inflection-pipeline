# VERIFIER C — FRAMEWORK ADHERENCE AUDIT (B12c)
Company: GNG Electronics Ltd (EBGNG) | Run date: 2026-07-12 | Model: claude-opus-4-8
Scope: PHASE 1 — Gate 0 (B01) re-derivation + Emerging Moat (B07) compliance ONLY.
Valuation adherence (B11/B10) DEFERRED to phase 3; those artifacts do not exist yet.
Status: PARTIAL.

I audit rule application, not company quality and not raw numbers (Verifier A owns numbers).
Where a re-derivation depends on an input figure, I re-ran the framework arithmetic on the
figures AS STATED in the report; I did not re-source the raw inputs.

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) COMPLIANCE
═══════════════════════════════════════════════════════════════════

Data window: 7 years (FY2020-FY2026), moderate confidence band (7-9). No history downgrade.
Correctly declared. CAGR windows use FY20 endpoints (6-year), both endpoints positive.

### BLOCK A — Return on Capital (re-derived)
| Rule | Stated inputs | Re-derived | Report | PASS/FAIL |
|---|---|---|---|---|
| ROCE FY25 | 116.69 / 305.59 | 38.19% | 38.19% | PASS |
| ROCE FY26 | 190.15 / 790.40 | 24.06% | 24.06% | PASS |
| A1 median ROCE | (38.19+24.06)/2 = 31.13% → ≥25 | 5 | 5 | PASS |
| A2 min ROCE | 24.06% → ≥15 | 5 | 5 | PASS |
| A3 median ROE | sorted 7 vals, median 31.30% → ≥20 | 5 | 5 | PASS |
| A4 ROCE trend | 24.06 vs 38.19 = -14.13pp → >5pp decline | 0 | 0 | PASS |
Block A = 15/20. PASS. A4=0 is mechanically correct on the 2 computable years; the
IPO-denominator caveat is flagged but correctly NOT allowed to alter the mechanical score.

### BLOCK B — Cash Generation (re-derived)
| Rule | Re-derived | Report | PASS/FAIL |
|---|---|---|---|
| ΣCFO (7yr) | -34.69-12.42-17.21+1.47+97.46-113.84-215.30 = -294.53 | -294.53 | PASS |
| ΣPAT (7yr) | 1.64+7.49+20.23+32.75+52.14+68.83+132.02 = 315.10 | 315.10 | PASS |
| B1 CFO/PAT | -294.53/315.10 = -0.93 → <0.50 → 0 | 0 | PASS |
| B2 FCF-pos | 0/2 = 0% → 0 | 0 | PASS |
| B3 FCF/PAT | -361.98/200.85 = -1.80 → neg → 0 | 0 | PASS |
| B4 WC-days chg | 178.14-136.44 = +41.7d → >15 → 0 | 0 | PASS |
Block B = 0/20. PASS. Note (MINOR, non-material): B1 uses the full 7-year cumulative PAT
denominator while B3 uses only the 2-year (FY25+FY26) PAT denominator. The mismatch is
driven by FCF being computable for only 2 years; both metrics score 0 regardless, so the
inconsistency changes nothing. Disclosed in the report body. No score impact.

### BLOCK C — Growth (re-derived)
Rev CAGR (1891.08/244.70)^(1/6)-1 = 40.6% → 5 (PASS). PAT CAGR (132.02/1.64)^(1/6)-1 =
107.8% → 5 (PASS). C3 6/6 positive = 5 (PASS). C4 +67.2pp ≥+3 → 5 (PASS). Block C = 20/20.
CAGR edge rules honoured: both endpoints positive, no loss-to-profit swing, PAT positive
every year — correctly stated, no synthetic CAGR attempted. PASS.

### BLOCK D — Balance Sheet (re-derived)
| Rule | Re-derived | Report | PASS/FAIL |
|---|---|---|---|
| EBITDA FY26 | 147.74+42.41+10.35-4.33 = 196.17 | 196.17 | PASS |
| D1 ND/EBITDA | 287.51/196.17 = 1.47x → 1-2x → 3 | 3 | PASS |
| D2 Int cover | 190.15/42.41 = 4.48x → 3-4.9x → 2 | 2 | PASS |
| D3 D/E | 405.75/759.33 = 0.53x → 0.5-1.0x → 3 | 3 | PASS |
| D4 Current | 1162.38/463.59 = 2.51x → ≥2.0 → 5 | 5 | PASS |
Block D = 13/20. PASS. (Note: D3 equity denominator 759.33 vs data-note-9 net worth 757.79
is a raw-figure discrepancy — Verifier A's domain — and does not cross a band boundary.)
Deal-breaker #6 (ND/EBITDA>3x AND IC<3x): 1.47x / 4.48x → not triggered. Correct.

### BLOCK E — Shareholder Alignment
E1-E4 all N/A (no shareholding pattern / Notes-to-Accounts provided) → scored 0 each.
Correct application of operating rule 5 (data absent → score 0, never estimate). Correctly
framed as a data-availability gap, not an evidenced weakness. Block E = 0/20. PASS.

### BLOCK F — Quantitative Moat (12 tests re-checked)
| Test | Re-derived verdict | Report | PASS/FAIL |
|---|---|---|---|
| M1 Pricing | margin +8pp ≥2pp AND rev CAGR 40.6% ≥10 → 5 | 5 | PASS |
| M2 Cost adv | PEER DATA NEEDED → 0 | 0 | PASS |
| M3 Cap eff | FAT 25.7x >3x AND ROCE 24.06% >20 → 5 | 5 | PASS |
| M4 Stickiness | 0 decline yrs; recv +22.4d fails ±10 tier-5; scored tier-3 | 3 | PASS* |
| M5 Scale | PEER DATA NEEDED → 0 | 0 | PASS |
| M6 Tech/R&D | no R&D disclosed → 0 | 0 | PASS |
| M7 Reg/Licence | unregulated → 0 | 0 | PASS |
| M8 Distribution | quantified but growth unconfirmed → 1 | 1 | PASS* |
| M9 Brand | PEER DATA NEEDED (proxy shown, no benchmark) → 0 | 0 | PASS |
| M10 Switching | grew every yr but recv +22.4d >10 → 1 | 1 | PASS* |
| M11 Network | latest3yr>prior3yr but selling% rising → tier "1" | 1 | PASS |
| M12 Neg WC | WC days 136/178 both >45 → 0 | 0 | PASS |
Sum = 5+0+5+3+0+0+0+1+0+1+1+0 = 16/60. Moats present (≥3): M1, M3, M4 = 3 → MODERATE
(2-3 band). Re-derivation confirms.

*MINOR observations (defensible, non-material, no fail): M4/M8/M10 sit in tiers whose text
does not map cleanly to a "0 decline years but unstable receivable-days" profile. The maker
took the closest / more-conservative tier in each case and flagged the reasoning. Sensitivity:
even if M4 were scored below 3, moats-present would fall from 3 to 2 — still MODERATE — so no
classification effect. M8/M10 at 1 are below the ≥3 "present" line either way. All conservative,
none inflated.

### CLASSIFICATION, MATRIX, DEAL-BREAKERS (re-checked)
Core = 15+0+20+13+0 = 48. Grand = 48+16 = 64. Re-derived, matches.
Matrix: Core 48 ∈ 40-59 → AVERAGE (MODERATE moat does not move the band). Correct.
Deal-breakers: Block B <8 (=0) → cap GOOD [triggered]; Cumul CFO/PAT <0.50 (=-0.93) → cap
AVERAGE [triggered]; median ROCE 31.13% ≥10 [not]; pledge N/A [not assessable]; DB#6 [not];
rev decline majority [not, 0 declines]; PAT neg last 3yr [not]; history <3yr [not, 7yr].
Most restrictive cap = AVERAGE, equal to matrix tier. FINAL: AVERAGE. Re-derivation confirms.
The report correctly did NOT apply any post-IPO position-sizing override at this stage (that
is explicitly a downstream discretion), and correctly kept AVERAGE with depressors flagged.

**GATE 0 VERDICT: fully compliant. 38 rules checked, 0 fails. Classification AVERAGE confirmed.**

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### Coverage — all 21 categories addressed?
A1,A2,A3,A4,B1,B2,B3,C1,C2,D1,D2,E1,E2,F1,F2,G1,G2,H1,H2,H3,R1 — all 21 present in the
Section 3 summary table (+ Section 4 for R1), each either scored with evidence or explicitly
NO EVIDENCE FOUND. G1/G2 correctly recorded as NEGATIVE (net debt / deteriorating WC), not
force-fit. PASS.

### Matrix raw-score mapping (likelihood×impact → HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1)
A1 LM=1, B2 HH=4, B3 LM=1, C1 MM=2, C2 HM=3, E1 LM=1, F1 LL=1, F2 HM=3, H1 HM=3, H2 HL=2,
H3 HM=3, R1 HM=3 — all 12 mappings correct. PASS.

### Evidence-quality multipliers (📄 1.0, 🎙️ 0.7, 🔍 0.5) — re-checked per scored row
| Cat | Stated quality | Raw | Multiplier used | Correct mult | Adj used | Adj correct |
|---|---|---|---|---|---|---|
| A1 | 🔍 | 1 | 0.5 | 0.5 | 0.5 | ✓ |
| B2 | 📄 | 4 | 1.0 | 1.0 | 4.0 | ✓ |
| B3 | 📄 | 1 | 1.0 | 1.0 | 1.0 | ✓ |
| C1 | 🎙️ | 2 | 0.7 | 0.7 | 1.4 | ✓ |
| C2 | 📄 | 3 | 1.0 | 1.0 | 3.0 | ✓ |
| E1 | 📄 | 1 | 1.0 | 1.0 | 1.0 | ✓ |
| F1 | 🔍 | 1 | 0.5 | 0.5 | 0.5 | ✓ |
| F2 | 🎙️/📄 | 3 | 0.7 | 0.7 (🎙️ governs weaker leg) | 2.1 | ✓ |
| **H1** | **🔍** (Sec5 label; Sec3 "📄/🔍") | 3 | **0.7** | **0.5** (🔍 governs) | **2.1** | **✗ FAIL** |
| H2 | 🎙️ | 2 | 0.7 | 0.7 | 1.4 | ✓ |
| H3 | 📄 | 3 | 1.0 | 1.0 | 3.0 | ✓ |
| R1 | 📄 | 3 | 1.0 | 1.0 | 3.0 | ✓ |

**FINDING F-1 (MAJOR): H1 evidence multiplier misapplied.** The Section 5 scorecard labels
H1 quality "🔍" (and Section 3 describes it as "📄/🔍" — the E-Waste Rules fact is 📄 but the
"consolidation-beneficiary" conclusion is explicitly analyst inference). The multiplier table
defines 🔍 = 0.5. The maker applied 0.7 — which is the 🎙️ rate, and H1 has no management-claim
component. This appears copied from the F2 blended-🎙️/📄 logic without a 🎙️ leg to justify it.
Corrected: raw 3 × 0.5 = 1.5 (vs 2.1 stated).
Adjusted total: 23.0 → **22.4**. Classification band unchanged (12-24 MODEST MOAT
DEVELOPMENT). No downstream decision effect → MAJOR, not CRITICAL. (Even the most generous
📄/🔍 blend of 0.75 → 2.25 → total 23.15, still MODEST.)

### Adjusted-total arithmetic
As-stated rows sum to 23.0 (0.5+4.0+1.0+1.4+3.0+1.0+0.5+2.1+2.1+1.4+3.0+3.0). Internally
consistent — the arithmetic is right given the (erroneous) 0.7 input. PASS on arithmetic;
the error is upstream in the multiplier, captured in F-1.

### Completionist recount
"📄 recount performed: 6 documented items across [m] categories" — present and explicit,
listing B2, C2, H3, R1, B3, E1. Active (Strong/Moderate) count = 6, sits at the upper edge of
the stated 3-6 base rate; guard applied and honoured. C1 and H2 (🎙️ "minuscule" claims) were
correctly EXCLUDED from the active list and routed to the optionality register rather than
credited as documented. PASS.

### Evidence-tier consistency (a 🎙️/🔍-only category scoring as if 📄 = a finding)
No category resting on claim/inference is credited at a 📄 multiplier: C1/H2 (🎙️) at 0.7,
A1/F1 (🔍) at 0.5, F2 blended at 0.7. The ONLY tier inconsistency is H1 (captured in F-1),
where a 🔍-labelled row received a 0.7 rather than 0.5 — i.e. an inference credited slightly
above its tier. That is exactly the class of error rubric item 4 targets, hence F-1's MAJOR
grade despite immaterial score impact. All other rows PASS.

### Classification, combined assessment, capex-2C, optionality register
- em_classification 23.0 → 12-24 MODEST: correct on the stated total (and on the corrected
  22.4). PASS.
- 6D combined: injected Gate 0 core 48 / AVERAGE + MODERATE existing moat, paired with a
  MODEST (not STRENGTHENING/EXPANSION) forward score → no upward revision → AVERAGE. Matrix
  logic correctly applied; correctly NOT called TURNAROUND (profitable, growing) nor HIGH
  POTENTIAL (forward score too low). PASS.
- 2C capex-embedded-growth: instructed method (capex × FAT) deliberately not applied;
  capex_embedded_growth_pct = 0 / NOT APPLICABLE. This is a deviation from the written method,
  but justified with evidence (asset-light model, IPO proceeds fund debt not capacity, and
  mechanically applying it would double-count the FY24 leasing-asset line already captured in
  the leasing revenue stream). Deviation is disclosed, reasoned, and conservative. PASS (MINOR
  note: a documented, defensible method-deviation, not a silent skip).
- Optionality register populated with 7 rows, each with converting-📄 evidence, first-appears
  location, and window; 🎙️/🔍-only items correctly parked here, watched not scored. PASS.

**EMERGING MOAT VERDICT: substantially compliant. 24 rules checked, 1 fail (H1 multiplier,
MAJOR, non-classification-changing). Classification MODEST confirmed; combined AVERAGE
confirmed.**

═══════════════════════════════════════════════════════════════════
## SUMMARY
═══════════════════════════════════════════════════════════════════
- Gate 0: 38 rules re-derived, all pass. Classification AVERAGE independently reproduced,
  including both triggered deal-breakers (Block B cap GOOD; cumulative CFO/PAT cap AVERAGE).
- Emerging Moat: 24 rules checked, 1 MAJOR fail (F-1, H1 multiplier 0.7→should be 0.5;
  adjusted total 23.0→22.4; classification MODEST unchanged). Coverage, recount, tier
  discipline, combined-assessment logic otherwise clean.
- Valuation (B11/B10) adherence: NOT RUN — deferred to phase 3 per task scope.
- No CRITICAL findings. acceptance_rate 61/62 = 98%. Well above the 60% REWORK threshold.

Recomputed destination PE: n/a this phase (valuation deferred).
Recomputed decision: no change — Gate 0 AVERAGE and combined-assessment AVERAGE both hold
even after correcting F-1.

```yaml
stage: B12c
company: "EBGNG"
run_date: "2026-07-12"
model: claude-opus-4-8
status: partial   # valuation (B11/B10) adherence deferred to phase 3; not run
gate0:
  rules_checked: 38
  fails: []
emoat:
  rules_checked: 24
  fails:
    - {id: "F-1", severity: "MAJOR", rule: "evidence multiplier (🔍=0.5)", location: "B07 Section 5, row H1", detail: "H1 labelled 🔍 but multiplier 0.7 applied (🎙️ rate); should be 0.5. Adj 2.1→1.5, total 23.0→22.4, classification MODEST unchanged"}
valuation:
  rules_checked: 0
  fails: []          # DEFERRED to phase 3 — B11/B10 artifacts do not exist yet
recomputed_destination_pe: ""   # pending phase 3 (valuation deferred)
recomputed_decision: ""         # concur: Gate 0 AVERAGE and combined AVERAGE unchanged by F-1
findings:
  - {severity: "MAJOR", location: "B07 Sec 5 row H1", claimed: "🔍 × 0.7 = 2.1", correct: "🔍 × 0.5 = 1.5", note: "adjusted total 23.0→22.4; classification MODEST and combined AVERAGE both unchanged, hence not CRITICAL"}
  - {severity: "MINOR", location: "B07 Sec 2C", claimed: "capex_embedded_growth_pct=0 (method not applied)", correct: "documented, evidence-based deviation (asset-light; avoids double-counting leasing-asset line)", note: "disclosed and conservative, not a silent skip"}
  - {severity: "MINOR", location: "B01 Block F M4/M8/M10", claimed: "tier scores 3/1/1", correct: "defensible closest-tier mapping where rubric text is ambiguous for a 0-decline-year, unstable-receivables profile", note: "conservative; moats-present stays MODERATE under any variant, no classification effect"}
  - {severity: "MINOR", location: "B01 Block B B1 vs B3", claimed: "B1 denom = 7yr ΣPAT, B3 denom = 2yr ΣPAT", correct: "basis mismatch driven by FCF availability", note: "both score 0, non-material; disclosed"}
critical_count: 0
major_count: 1
minor_count: 3
acceptance_rate: 98    # 61 of 62 rules passed (gate0 38/38 + emoat 23/24)
```
