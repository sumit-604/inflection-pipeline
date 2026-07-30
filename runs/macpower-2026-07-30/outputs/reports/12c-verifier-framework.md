# STAGE 12c — VERIFIER C: FRAMEWORK ADHERENCE (MACPOWER)
Run date: 2026-07-30 | Model: claude-opus-4-8 | Phase 1 scope

Scope note: PHASE 1 runs Gate 0 (B01) and Emerging Moat (B07) compliance ONLY.
The valuation-adherence audit (B11/B10) is DEFERRED to phase 3; those artifacts
do not yet exist. The valuation section of the B12c block is marked
`status: pending phase 3` and left unpopulated. `framework_adherence` below is
the Gate0+EM portion only.

I audit rule application against the framework AS WRITTEN. I do not re-audit raw
source numbers (Verifier A owns number-in-source fidelity); I re-derive scores
from the inputs the report itself states, using the framework's own thresholds.

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### Block A — Return on Capital (re-derived from stated inputs)

| Rule | Stated input | Threshold applied | Recompute | Report | Verdict |
|---|---|---|---|---|---|
| A1 Median ROCE | {26.70, 23.75, 26.24}, median 26.24% | ≥25% = 5 | 5 | 5 | PASS |
| A2 Min single-yr ROCE | min 23.75% | ≥15% = 5 | 5 | 5 | PASS |
| A3 Median ROE | {22.34, 19.42, 21.30}, median 21.30% | ≥20% = 5 | 5 | 5 | PASS |
| A4 ROCE trend | 26.24% (FY26) vs 26.70% (FY24), −0.46pp | see note | edge | 3 | PASS (edge, flagged) |

A4 edge: framework bands are `latest ≥ earliest = 5 | decline 1-3pp = 3 | ...`.
A −0.46pp move satisfies neither the ≥ band (26.24 < 26.70, fails by 0.46pp) nor
the 1-3pp band (below its floor). The framework defines NO sub-1pp-decline band,
so there is no as-written answer. Maker took the conservative lower band (3) and
flagged it. Immaterial: Block A is 18 (with 3) or 20 (with 5); Core is 67 or 69,
neither crossing the 60-79/≥80 boundary; final classification is locked elsewhere.
Severity MINOR.

Block A = 18/20. PASS.

### Block B — Cash Generation Quality

| Rule | Input | Threshold | Recompute | Report | Verdict |
|---|---|---|---|---|---|
| B1 Cum CFO/PAT | 3785.21/8341.03 = 0.4538 | <0.50 = 0 | 0 | 0 | PASS |
| B2 FCF-positive yrs | 2/3 = 66.7% | 50-74 = 2 | 2 | 2 | PASS |
| B3 Cum FCF/PAT | 35.79/8341.03 = 0.0043 | <0.20 = 0 | 0 | 0 | PASS |
| B4 ΔWC days | +27.19 | increased >15 = 0 | 0 | 0 | PASS |

Block B = 2/20. PASS.

### Block C — Growth

| Rule | Input | Threshold | Recompute | Report | Verdict |
|---|---|---|---|---|---|
| C1 Rev CAGR | (33317.59/24116.53)^½−1 = 17.54% | 15-19.9 = 4 | 4 | 4 | PASS |
| C2 PAT CAGR | (3387.08/2409.78)^½−1 = 18.56% | 15-19.9 = 4 | 4 | 4 | PASS |
| C3 Positive YoY | 2/2 = 100% | 100% = 5 | 5 | 5 | PASS |
| C4 PAT−Rev CAGR | +1.02pp | ±3pp = 3 | 3 | 3 | PASS |

CAGR edge rules honoured: no negative/zero endpoints (no N/M), no loss-to-profit
swing. 2-year CAGR on 3 data points is within "minimum 3 years" rule. PASS.
Block C = 16/20. PASS.

### Block D — Balance Sheet Strength

| Rule | Input | Threshold | Report | Verdict |
|---|---|---|---|---|
| D1 Net Debt/EBITDA | net cash (−526.68) | net cash = 5 | 5 | PASS |
| D2 Interest Coverage | 29.91x | ≥10x = 5 | 5 | PASS |
| D3 Debt/Equity | 0.0039 | <0.1 = 5 | 5 | PASS |
| D4 Current Ratio | 2.339x | ≥2.0 = 5 | 5 | PASS |

Block D = 20/20. PASS.

### Block E — Shareholder Alignment

| Rule | Input | Threshold | Report | Verdict |
|---|---|---|---|---|
| E1 Promoter holding | 73.22% | ≥60% = 5 | 5 | PASS |
| E2 Promoter Δ (~3yr) | +0.06pp | ±1% = 3 | 3 | PASS |
| E3 Pledge | NOT FOUND | N/A → 0 (rule 5, no gap-fill) | 0 | PASS |
| E4 Contingent/NW | 1075/14282.42 = 7.53% | 5-15 = 3 | 3 | PASS |

E3 handled correctly: absent disclosure scored 0 under operating rule 5 (never
fill gaps), NOT force-scored to 5. Deal-breaker #5 (pledge >15%) correctly NOT
applied for absence-of-data. E2 window is ~2.75yr not full 36m (maker flagged);
does not change the band. Block E = 11/20. PASS.

### Core Score
18+2+16+20+11 = **67**. Report 67. PASS.

### Block F — 12 Moat Tests

| Test | Basis (as stated) | Band applied | Report | Verdict |
|---|---|---|---|---|
| M1 Pricing Power | margin +1.47pp (±2pp stable) AND rev CAGR 17.54% ≥10% | stable+≥10% = 3 | 3 | PASS |
| M2 Cost Adv | no peer data | 0 PEER DATA NEEDED | 0 | PASS |
| M3 Capital Eff | FAT 5.68x >3x AND ROCE 26.24% >20% | 5 | 5 | PASS |
| M4 Cust Stickiness | 0 decline yrs BUT recv days +17.72 (>±10) | edge | 3 | PASS (edge, flagged) |
| M5 Scale/Dominance | no peer data | 0 PEER DATA NEEDED | 0 | PASS |
| M6 Tech/R&D | R&D not quantified | 0 | 0 | PASS |
| M7 Regulatory | unregulated segment | unregulated = 0 | 0 | PASS |
| M8 Distribution | no anchored network figures | 0 | 0 | PASS |
| M9 Brand | no peer GM data | 0 PEER DATA NEEDED | 0 | PASS |
| M10 Switching | grew every yr BUT recv days +17.72 (>10) | edge | 3 | PASS (edge, flagged) |
| M11 Network | <6yr; rev CAGR 17.54%, selling% rising | see note | 0 | PASS (conservative clause) |
| M12 Neg WC/Float | WC days 104-132 (>45) | 0 | 0 | PASS |

M4/M10 edge: both top bands require BOTH unbroken growth AND receivable-days
stability; growth leg met, stability leg fails (+17.72d). The intermediate band
is keyed to decline-years (a different scenario), so no band cleanly fits a
0-decline-but-unstable-receivables profile. Maker applied nearest band (3) and
flagged. MINOR.

M11 note: strict band read of `growth >15% but selling % rising = 1` would give
**1** (rev CAGR 17.54% > 15%, selling% rose 1.47%→1.90%), not 0. Maker scored 0
citing the framework's explicit `<6yr → score conservatively on the overall
trend and state so` latitude. This is authorised by the rule, so PASS; but a
strict reader lands on 1. Immaterial: M11 at 1 is still <3 (not "present"),
moats-present count unchanged (4), Moat Score would be 15 not 14, grand total 82
not 81 — no threshold crossed. MINOR.

**Moat Score** = 3+0+5+3+0+0+0+0+0+3+0+0 = **14/60**. Report 14. PASS.

### Moat count & classification
Present (≥3): M1, M3, M4, M10 = **4 present**. Bands: 6+ FORTRESS | 4-5 STRONG |
2-3 MODERATE. 4 → **STRONG**. Report STRONG. PASS. (Note: two of the four
"present" tests, M4 and M10, are the edge-case 3s; had either scored lower the
count would drop to MODERATE, but as scored the count is correct.)

### Classification matrix & overrides

| Step | Rule | Recompute | Report | Verdict |
|---|---|---|---|---|
| Base matrix | Core 60-79 (67) + STRONG = GOOD+ | GOOD+ | GOOD+ | PASS |
| DB1 Block A<8 | 18, not triggered | not triggered | not triggered | PASS |
| DB2 Block B<8 | 2<8 → max GOOD | triggered | triggered | PASS |
| DB3 median ROCE<10% | 26.24%, no | not triggered | not triggered | PASS |
| DB4 cum CFO/PAT<0.50 | 0.4538 → max AVERAGE | triggered (governs) | triggered | PASS |
| DB5 pledge>15% | NOT FOUND, not applied | not applied | not applied | PASS |
| DB6 ND/EBITDA>3x & IC<3x | net cash, IC 29.91x, no | not triggered | not triggered | PASS |
| DB7 rev decline majority | 0/2, no | not triggered | not triggered | PASS |
| DB8 PAT neg last 3 | no | not triggered | not triggered | PASS |
| DB9 history<3 | =3, no | not triggered | not triggered | PASS |
| Post-DB | most restrictive = AVERAGE | AVERAGE | AVERAGE | PASS |
| Confidence | 3yr = LIMITED (3-4) → downgrade 1 tier | AVERAGE→AVOID | AVOID | PASS |

Two-penalty stacking (DB cap to AVERAGE, then LIMITED-history one-tier downgrade
to AVOID) is as-written: deal-breakers cap; data-confidence downgrades one tier
for 3-4yr. These are distinct mechanisms and both apply. The "one-improvement-
one-mechanism" rule governs crediting improvements, not stacking penalties, so no
double-credit violation. history_downgrade flag = true. PASS.

**Final classification AVOID — re-derived, concurs.** The AVOID is mechanically
locked by DB4 + LIMITED-history downgrade regardless of the A4/M4/M10/M11 edge
cases, so none of the flagged minors can flip it.

**Gate 0 verdict: fully compliant. 0 rule FAILs. 4 MINOR edge/latitude notes,
all flagged by the maker, none material to classification.**

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) COMPLIANCE
═══════════════════════════════════════════════════════════════════

### 21-category completeness
Section 3 addresses all 20 (A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2,
H1-H3) plus R1 in Section 4; the summary table carries all 21 rows with
evidence?/type/strength/time. Every category either scored or explicitly NO
EVIDENCE FOUND. No force-fit. PASS.

### Raw score matrix (likelihood×impact: HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0)

| Cat | L×I | Recompute raw | Report raw | Verdict |
|---|---|---|---|---|
| A1 | M×M | 2 | 2 | PASS |
| A4 | H×M | 3 | 3 | PASS |
| B1 | M×M | 2 | 2 | PASS |
| C1 | M×L | 1 | 1 | PASS |
| E2 | M×L | 1 | 1 | PASS |
| F1 | L×M | 1 | 1 | PASS |
| F2 | M×H | 3 | 3 | PASS |
| G1 | H×M | 3 | 3 | PASS |
| H2 | L×H | 2 | 2 | PASS |
| R1 | M×H | 3 | 3 | PASS |
| all NO-EVIDENCE | — | 0 | 0 | PASS |

All raw scores correct. PASS.

### Evidence multipliers (📄 1.0x, 🎙️ 0.7x, 🔍 0.5x)

| Cat | raw × mult | Recompute | Report | Verdict |
|---|---|---|---|---|
| A1 | 2×0.7 | 1.4 | 1.4 | PASS |
| A4 | 3×0.7 | 2.1 | 2.1 | PASS |
| B1 | 2×0.7 | 1.4 | 1.4 | PASS |
| C1 | 1×0.7 | 0.7 | 0.7 | PASS |
| E2 | 1×1.0 | 1.0 | 1.0 | PASS |
| F1 | 1×0.7 | 0.7 | 0.7 | PASS |
| F2 | 3×0.7 | 2.1 | 2.1 | PASS |
| G1 | 3×0.7 | 2.1 | 2.1 | PASS |
| H2 | 2×0.7 | 1.4 | 1.4 | PASS |
| R1 | 3×0.7 | 2.1 | 2.1 | PASS |

Adjusted total = 1.4+2.1+1.4+0.7+1.0+0.7+2.1+2.1+1.4+2.1 = **15.0**. Report 15.0.
PASS.

### Evidence-tier consistency (no 🎙️-only category scoring as 📄)
Only E2 carries the 1.0x 📄 multiplier, and E2 rests on the audited AR Segment
Note export-revenue figure — genuinely documented. Every 🎙️-based active
category (A1, A4, B1, C1, F1, F2, G1, H2, R1) took 0.7x. F2 and G1 have partial
📄 anchors yet were scored at the conservative 🎙️ 0.7x, not inflated to 1.0x. No
tier inflation detected. PASS.

### Classification threshold
15.0 → band 12-24 = MODEST MOAT DEVELOPMENT. Report MODEST. PASS.

### Completionist recount
Framework requires the explicit line `📄 recount performed: [n] documented items
across [m] categories`. Report: "📄 recount performed: 4 documented items across
3 categories," plus explicit statement that active/nonzero categories = 10 which
is below the 12-category red-flag threshold. Guard performed as written. PASS.

Note: YAML `evidence_mix.documented: 6` vs the recount's "4 documented items."
These count different things — the recount tallies 📄 items that back SCORED moat
categories (E2/G1/F2), while evidence_mix appears to tally all 📄-tagged evidence
threads across the report (which includes non-scored 📄 items such as import
outgo and bank-guarantee disclosures). Not a scoring error; a presentational
count-basis mismatch. MINOR.

### Structural completeness
Six sections present (1: 1A/1B/1C; 2: 2A-2D; 3: 20-cat + summary; 4: R1 4A-4C;
5: scorecard; 6: 6A-6E). Optionality register present (8 rows, each with
converting 📄 evidence / where-first-appears / window). active_categories lists
only Strong/Moderate rows (0 Strong, 4 Moderate: A4/F2/G1/R1). PASS.

### 2C capex-embedded growth
₹46cr (midpoint of ₹40-52cr) × 5.05x FAT = ₹232.3cr ≈ 70% above ₹333.18cr FY26
revenue. capex_embedded_growth_pct = 70. Maker reported the mechanical figure per
instruction and flagged it as an overstatement vs the 40-60% unit-capacity
grounding. As written. PASS.

### 6D combined classification
Gate 0 = AVOID, EM = MODEST → combined AVOID. The transition setup the operation
hunts (GOOD/AVERAGE backward + EXPANSION 40+ forward) is not present: backward
classification is AVOID (not GOOD/AVERAGE-tier) and forward is MODEST 15.0 (not
EXPANSION). Maker gave the required reasoning for why HIGH POTENTIAL / TURNAROUND
do not apply (neither precondition met). PASS.

**Emerging Moat verdict: fully compliant. 0 rule FAILs. 1 MINOR count-basis
note.**

═══════════════════════════════════════════════════════════════════
## PART 3 — VALUATION (B11/B10)
═══════════════════════════════════════════════════════════════════
DEFERRED to phase 3. B10 and B11 artifacts do not exist yet. Not audited here.
Status: pending phase 3.

═══════════════════════════════════════════════════════════════════
## SUMMARY
═══════════════════════════════════════════════════════════════════
- Gate 0: 47 rule checks, 0 FAIL, 4 MINOR (A4 sub-1pp band gap; M4/M10 dual-leg
  band gap; M11 conservative-clause vs strict-band). None change Core, Moat
  count, or the AVOID classification.
- Emerging Moat: 30 rule checks, 0 FAIL, 1 MINOR (evidence_mix vs recount count
  basis). Scorecard arithmetic, multipliers, tiering, thresholds, completionist
  guard and combined classification all as-written.
- Gate0+EM framework adherence: 77/77 hard rules applied as written = 100%.
- No recomputed value differs enough to change any destination or decision.
- Valuation adherence: pending phase 3.

```yaml
stage: B12c
company: "MACPOWER"
run_date: "2026-07-30"
model: claude-opus-4-8
status: complete
scope: "phase 1 — gate0 + emerging moat only; valuation deferred to phase 3"
gate0: {rules_checked: 47, fails: []}
emoat: {rules_checked: 30, fails: []}
valuation: {status: "pending phase 3", rules_checked: 0, fails: []}
framework_adherence: 100   # Gate0+EM portion: 77/77 hard rules applied as written
recomputed_destination_pe: ""   # n/a in phase 1; valuation deferred
recomputed_decision: ""         # concur — Gate 0 AVOID and EM MODEST re-derive cleanly
findings:
  - {severity: MINOR, framework: gate0, location: "Block A / A4", note: "ROCE trend −0.46pp falls in an undefined sub-1pp-decline gap; maker took conservative band 3 (vs strict-read 5) and flagged. Block A 18 vs 20 immaterial; classification locked by DB4+history."}
  - {severity: MINOR, framework: gate0, location: "Block F / M4 & M10", note: "Both top bands need growth AND receivable-days stability; growth met, stability fails (+17.72d), and the intermediate band is decline-year-keyed. Maker applied nearest band 3 and flagged. As-scored moat count (4=STRONG) holds."}
  - {severity: MINOR, framework: gate0, location: "Block F / M11", note: "Strict band 'growth >15% but selling% rising = 1' yields 1, not 0 (rev CAGR 17.54%). Maker scored 0 under the framework's explicit <6yr conservative-scoring latitude — authorised. Immaterial: still <3, moat count and grand-total band unchanged."}
  - {severity: MINOR, framework: emoat, location: "YAML evidence_mix vs completionist recount", note: "evidence_mix.documented:6 vs recount '4 documented items across 3 categories' count different bases (all 📄 threads vs 📄 items backing scored categories). Not a scoring error; presentational."}
critical_count: 0
major_count: 0
minor_count: 4
acceptance_rate: 100            # 77/77 Gate0+EM rules passed as written
```
