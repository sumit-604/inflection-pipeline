# B12c — VERIFIER C: FRAMEWORK ADHERENCE (PHASE 1 SCOPE)
Company: ZAGGLE (Zaggle Prepaid Ocean Services Ltd) | Run date: 2026-07-27 | Model: claude-opus-4.8

**Scope note (Phase 1 only):** This pass audits framework adherence for the Gate 0
re-derivation (B01) and the Emerging Moat scan (B07) ONLY. The valuation-adherence
audit (B11 valuation + B10 assembly) is DEFERRED to Phase 3 — those artifacts do not
yet exist. The `valuation` block in the YAML is explicitly marked `pending phase 3`.
I do not own numbers (Verifier A is the sole source-fidelity authority); I re-derive
scores from the inputs the reports themselves state, and I audit whether each
framework rule was applied AS WRITTEN.

Rule sources: `prompts/01-gate-0-pipeline.md` (Gate 0 thresholds, classification
matrix, deal-breaker overrides, CAGR edge rules), `prompts/07-emerging-moat-pipeline.md`
(21-category scan, evidence multipliers, completionist guard, combined matrix),
`frameworks/Master_Project_Prompt_v3.3.md`, `frameworks/FTTCP_v1.2_Consolidated.md`
(non-conflation boundary).

---

## PART 1 — GATE 0 (B01) RE-DERIVATION

Inputs are taken exactly as stated in B01. I re-applied the thresholds in
`prompts/01-gate-0-pipeline.md` lines 55-160.

### Block A — Return on Capital (thresholds L56-60)

| Rule | Stated input | Threshold applied | Re-derived score | B01 score | Verdict |
|---|---|---|---|---|---|
| A1 Median ROCE | ROCE [22.06, 9.41, 7.83, 10.15]; median=(9.41+10.15)/2=**9.78%** | <10 = 0 | 0 | 0 | PASS |
| A2 Min single-yr ROCE | 7.83% (FY25) | <8 = 0 | 0 | 0 | PASS |
| A3 Median ROE | ROE [46.97, 14.11, 9.65, 10.41]; median=(10.41+14.11)/2=**12.26%** | 12-14.9 = 2 | 2 | 2 | PASS |
| A4 ROCE trend | FY26 10.15% vs FY23 22.06% = -11.91pp | decline >5pp = 0 | 0 | 0 | PASS |
| **Block A total** | | | **2** | **2** | **PASS** |

### Block B — Cash Generation Quality (thresholds L63-69)

| Rule | Stated input | Threshold | Re-derived | B01 | Verdict |
|---|---|---|---|---|---|
| B1 Cum CFO/Cum PAT | -130.14 / 292.92 = **-0.444** | <0.50 = 0 | 0 | 0 | PASS |
| B2 FCF-positive-yr % | 0 of computable years | <50 = 0 | 0 | 0 | PASS |
| B3 Cum FCF/Cum PAT | -335.06 / 270.02 = negative | <0.20 or negative = 0 | 0 | 0 | PASS |
| B4 ΔWC Days | FY26 65.28 vs FY24 81.42 = -16.14 | decreased >5 = 5 | 5 | 5 | PASS (note 1) |
| **Block B total** | | | **5** | **5** | **PASS** |

Note 1: FY23 payables are NOT FOUND, so B01 anchors B4's "earliest" year to FY24.
This is the honest no-estimate reading (fabricating an FY23 payable would violate the
no-estimate rule) but it is the score-maximising choice: had an incomplete FY23 WC of
~67.8 days been used, ΔWC would be ~-2.5 days → the ±5-day band = 3 rather than 5. The
choice is defensible and correctly disclosed in B01 data_notes #3. MINOR observation
only — no decision impact (Block B is 5 either way, still <8, deal-breaker #2 still trips).

### Block C — Growth (thresholds L72-75)

| Rule | Stated input | Threshold | Re-derived | B01 | Verdict |
|---|---|---|---|---|---|
| C1 Revenue CAGR | (1907.65/553.46)^(1/3)-1 = **51.08%** | ≥20 = 5 | 5 | 5 | PASS |
| C2 PAT CAGR | (138.08/22.90)^(1/3)-1 = **82.02%** | ≥20 = 5 | 5 | 5 | PASS |
| C3 Positive YoY rev yrs | 3 of 3 = 100% | 100% = 5 | 5 | 5 | PASS |
| C4 PAT-Rev CAGR gap | 82.03-51.08 = +30.95pp | ≥+3pp = 5 | 5 | 5 | PASS |
| **Block C total** | | | **20** | **20** | **PASS** |

CAGR edge rules (L44-51): no negative/zero endpoints, no loss-to-profit swing (PAT
positive and growing every year). Edge rules correctly not triggered, and the
no-swing note is carried in data_notes. PASS.

### Block D — Balance Sheet Strength (thresholds L78-87)

| Rule | Stated input | Threshold | Re-derived | B01 | Verdict |
|---|---|---|---|---|---|
| D1 Net Debt/EBITDA | 54.64 - 545.77 = net cash -491.13 | net cash = 5 | 5 | 5 | PASS |
| D2 Interest Coverage | 148.07 / 5.33 = **27.78x** | ≥10 = 5 | 5 | 5 | PASS |
| D3 Debt/Equity | 54.64 / 1404.22 = **0.039x** | <0.1 = 5 | 5 | 5 | PASS |
| D4 Current Ratio | 12068.65 / 1384.23 = **8.72x** | ≥2.0 = 5 | 5 | 5 | PASS |
| **Block D total** | | | **20** | **20** | **PASS** |

Non-financial company — the bank/NBFC alternative bands (CAR/PCR/default-3) correctly
NOT applied. PASS.

### Block E — Shareholder Alignment (thresholds L90-96)

| Rule | Stated input | Threshold | Re-derived | B01 | Verdict |
|---|---|---|---|---|---|
| E1 Promoter holding | 44.21% (Mar-2025) | 40-49.9 = 3 | 3 | 3 | PASS |
| E2 Promoter Δ | FY24 43.92% → FY25 44.21% = +0.29pp | ±1% = 3 | 3 | 3 | PASS (note 2) |
| E3 Promoter pledge | NOT FOUND | scored 0 per no-estimate | 0 | 0 | PASS |
| E4 Cont.Liab/NW | 74.44 / 12476.12 = **0.60%** | <5% = 5 | 5 | 5 | PASS |
| **Block E total** | | | **11** | **11** | **PASS** |

Note 2: The E2 rule text specifies a 3-year window; only a 1-year window (FY24→FY25)
exists in the provided data. B01 applied the ±1% band on the available 1-year change and
disclosed the limitation in the data-note and in E2 itself. Consistent with the
"use whatever history exists" operating rule (L24-26). MINOR observation, no decision impact.

Note on E3: the no-estimate rule (L20-23) forces pledge=0 when NOT FOUND rather than
crediting the 0%→5 band. Correctly applied and flagged as "not confirmed nil". PASS.

### Block F — Quantitative Moat (12 tests, thresholds L103-136)

| Test | Stated basis | Threshold met | Re-derived | B01 | Verdict |
|---|---|---|---|---|---|
| M1 Pricing Power | OPM +1.0pp (stable ±2pp) AND rev CAGR 51%≥10 | stable±2pp+CAGR≥10 = 3 | 3 | 3 | PASS |
| M2 Cost Advantage | PEER DATA NEEDED | peer data absent = 0 | 0 | 0 | PASS |
| M3 Capital Efficiency | FAT 6.68x>3x BUT ROCE 10.15%<12% | fails lowest tier = 0 | 0 | 0 | PASS |
| M4 Customer Stickiness | 0 decline yrs; recv days range 60-82 (not ±10) | drops to 3-tier | 3 | 3 | PASS (note 3) |
| M5 Scale & Dominance | PEER DATA NEEDED | 0 | 0 | 0 | PASS |
| M6 Technology/R&D | R&D not separately disclosed | 0 | 0 | 0 | PASS |
| M7 Regulatory/License | PEER DATA NEEDED (player count) | 0 | 0 | 0 | PASS |
| M8 Distribution | purely digital B2B2C | none/purely digital = 0 | 0 | 0 | PASS |
| M9 Brand | PEER DATA NEEDED | 0 | 0 | 0 | PASS |
| M10 Switching Costs | rev grew every yr AND recv days +1.4 (≤10) | =5 | 5 | 5 | PASS |
| M11 Network Effects | <6 yrs; rev CAGR 51%≥20 AND selling% stable/decl | =3 | 3 | 3 | PASS |
| M12 Negative WC/Float | WC days 59-82, all >45 | >45 = 0 | 0 | 0 | PASS |
| **Moat total** | | | **14** | **14** | **PASS** |

Note 3: M4 top tier (=5) requires BOTH zero decline years AND receivable days stable
±10. Receivable days span 60.2-82.2 (range 22), so the =5 tier correctly fails; 0 decline
years satisfies the "max 1 decline year" =3 tier. Defensible reading of the rubric. PASS.

Moats present (score ≥3): M1, M4, M10, M11 = **4** → 4-5 band = **STRONG** (L138). PASS.

### Classification, Deal-breakers, History Downgrade (L141-160)

| Rule | Re-derivation | B01 output | Verdict |
|---|---|---|---|
| Core score arithmetic | 2+5+20+20+11 = **58** | 58 | PASS |
| Grand total | 58 + 14 = **72** | 72 | PASS |
| Data-confidence tier | 4 yrs → 3-4 band = LIMITED, downgrade one tier | LIMITED, downgrade true | PASS |
| Base matrix | Core 58 → 40-59 band = **AVERAGE** | AVERAGE | PASS |
| DB #1 | Block A 2 <8 → max GOOD | recorded | PASS |
| DB #2 | Block B 5 <8 → max GOOD | recorded | PASS |
| DB #3 | median ROCE 9.78% <10% → max AVERAGE | recorded | PASS |
| DB #4 | cum CFO/PAT -0.44 <0.50 → max AVERAGE | recorded | PASS |
| DB #5-9 | pledge>15% / ND-IC / rev decline / PAT-neg / hist<3yr — none apply | not triggered | PASS |
| Most-restrictive cap | AVERAGE (from #3,#4) | AVERAGE | PASS |
| History downgrade | AVERAGE − one tier = **AVOID** | AVOID | PASS |
| **Final classification** | **AVOID** | **AVOID** | **PASS** |

Deal-breaker set is complete and correctly applied: #3 and #4 are the binding
AVERAGE caps; #1/#2 cap only at the looser GOOD tier and are correctly noted as
non-binding; #9 (history <3 yrs) correctly does NOT fire (4 years ≥ 3), while the
separate 3-4-year LIMITED confidence downgrade (L144) correctly does. The one-tier
downgrade sequencing (deal-breaker cap → then history downgrade → AVOID) is the
correct order. FLAG-GATE0 correctly raised (classification ≤ AVERAGE with the
depressors named as post-IPO/QIP capital dilution + cash-conversion strain).

**GATE 0 VERDICT: fully reconstructed, every score and the final AVOID classification
re-derive to the reported value. Zero FAILs. Two MINOR observations (B4 earliest-year
selection, E2 1-year window), both correctly disclosed and neither decision-relevant.**

---

## PART 2 — EMERGING MOAT (B07) COMPLIANCE

Rules from `prompts/07-emerging-moat-pipeline.md` (evidence taxonomy L18-23,
completionist guard L30-35, 21-category scan L54-132, multiplier L128-132,
combined matrix L149-161) and the CLAUDE.md non-conflation NEVER.

| Rule | Requirement | Finding | Verdict |
|---|---|---|---|
| 21 categories addressed | all of A1-R1 scored or NO EVIDENCE, no force-fit | All 21 rows present in the Section 5 scorecard; 6 (A1,A2,B1,E1,E2,H3) marked NO EVIDENCE/N-A; none force-fitted | PASS |
| Raw score matrix | HH=4, HM/MH=3, MM/HL/LH=2, ML/LM=1, LL=1, none=0 | All 12 scored rows match matrix (A4/D2 HH=4; B2/C1/G1/H2 HM/MH=3; A3/B3/D1/R1 MM=2; C2 LL=1; H1 LM=1) | PASS |
| Evidence multipliers | 📄1.0 / 🎙️0.7 / 🔍0.5 applied per row | Every row's multiplier matches its evidence type (see recompute below) | PASS |
| Adjusted total | sum of adjusted scores | Re-summed = **26.4 ≈ 26** (matches) | PASS |
| Classification band | 25-39 = STRENGTHENING | 26 → STRENGTHENING | PASS |
| Evidence-tier honesty | no 🎙️-only category scored as if 📄 | B3 (network claim 🎙️ though partner count 📄) took the conservative 0.7x, not 1.0x; A4 (📄 capitalised spend + 🎙️ cross-sell) rests HH on the documented spend; no inflation found | PASS |
| Completionist guard | recount performed + stated; <12 active | "📄 recount performed: 19 documented items across 6 categories"; 9 rows Strong/Moderate < 12 threshold; F2/G2 explicitly scored None on NEGATIVE evidence rather than credited | PASS |
| Optionality register | scored-0 / 🎙️-🔍-only items listed, watched not scored | 7 register rows, all genuinely 0/claim-only, none double-counted into the score | PASS |
| Capex-embedded growth (2C) | show arithmetic | Arithmetic shown (₹107cr × 32.8x ≈ ₹3,510cr ≈ 190%) then set to 0/NOT MEANINGFUL for asset-light model; handoff flag explicit | PASS (note 4) |
| EM-vs-FTTCP non-conflation | keep stage-7 taxonomy separate from FTTCP | Header + L3 explicitly state "NOT FTTCP (runs separately inside Stage 11)"; no FTTCP scoring performed here; 6C/6D reference only Gate 0 backward vs EM forward | PASS |
| Combined assessment (6D) | matrix label + full reasoning for TURNAROUND | AVOID (backward) + STRENGTHENING (forward) → TURNAROUND with full reasoning; correctly WITHHOLDS a cleaner upgrade because F2 execution + G2 WC fail on the same mechanisms that capped Gate 0 | PASS |
| active_categories = Strong/Moderate only | YAML list matches the prose count | YAML lists 7 (A4,D2,B2,G1,H2,C1,A3); Section-3 prose says "9 of 21 Strong/Moderate" (adds the two borderline Weak-Moderate rows B3,R1). Internal count mismatch | **FAIL (MINOR, note 5)** |

### Multiplier re-computation (spot audit)
A3 2×0.7=1.4 · A4 4×1.0=4.0 · B2 3×1.0=3.0 · B3 2×0.7=1.4 · C1 3×0.7=2.1 ·
C2 1×1.0=1.0 · D1 2×0.7=1.4 · D2 4×1.0=4.0 · G1 3×1.0=3.0 · H1 1×0.7=0.7 ·
H2 3×1.0=3.0 · R1 2×0.7=1.4 → **Σ = 26.4**. Matches B07 exactly.

Note 4: 2C requires the arithmetic to be shown; it is. Setting the handoff field to
0/NOT MEANINGFUL (rather than the mechanical 190%) is defensible for an asset-light
platform where PP&E is a rounding error and "capex" is capitalised software; the
no-estimate/no-mislead framing is sound. PASS with note.

Note 5 (the one EM FAIL): the Section-3 prose count ("9 of 21 rows Strong/Moderate")
and completionist_recount YAML ("9 of 21") include the two borderline **Weak-Moderate**
rows B3 and R1, whereas `active_categories` (defined as "only Strong/Moderate rows")
lists 7 and excludes them. The two counts should reconcile: either B3/R1 are
Moderate (then active_categories should list 9) or they are Weak (then the prose count
should be 7). Purely presentational — em_score (26), classification (STRENGTHENING),
and combined_assessment (TURNAROUND) are all unaffected. Severity MINOR.

**EMERGING MOAT VERDICT: scan is framework-compliant, correctly skeptical (two
negative-evidence categories held at None rather than credited), multipliers and total
re-derive exactly, non-conflation honoured. One MINOR internal count inconsistency
(active_categories 7 vs prose 9), no score or decision impact.**

---

## PART 3 — VALUATION (B11) + ASSEMBLY (B10) ADHERENCE

**STATUS: PENDING PHASE 3.** B11 (valuation) and B10 (assembly) are not produced until
Phase 3 of the pipeline and do not exist in this run's outputs at audit time. Per the
Phase-1 scope instruction, the deepest audit (continuous Pillar 1 formula, FTTCP ROCE
verdict as sole Pillar 1 authority, single-credit rule, Pillar 2 multiplier/offset
rules, Pillar 3 injected inputs, UA Amendment-3 ordering, sector-cap absolute, dual-track
carry-through, Hurdle Ratio + credibility gate, 4D weights, SOM cross-check,
one-improvement-one-mechanism) is DEFERRED and not scored here. No B10/B11 artifact was
read. This section will be completed by the Phase-3 valuation-adherence pass.

---

## SUMMARY

- Gate 0 (B01): 40 rule checks, 40 pass. Full re-derivation reproduces every block
  score (A2 B5 C20 D20 E11 = Core 58; Moat 14; Grand 72; 4 moats STRONG) and the final
  **AVOID** classification. Two MINOR disclosed-edge observations, no FAILs.
- Emerging Moat (B07): 12 rule checks, 11 pass, 1 MINOR fail (active_categories/prose
  count mismatch). Adjusted total 26 → STRENGTHENING and combined **TURNAROUND** both
  re-derive and are logically sound.
- Valuation (B11/B10): pending Phase 3, not scored.
- No CRITICAL or MAJOR findings. Recomputed classification CONCURS with B01 (AVOID) and
  B07 (STRENGTHENING / TURNAROUND); no destination-PE or decision recompute in scope.

Rules checked (Phase 1): 52 | passed: 51 | acceptance_rate = 98%.

---

```yaml
stage: B12c
company: "ZAGGLE"
run_date: "2026-07-27"
model: claude-opus-4-8
status: complete_phase1
phase: "1 (Gate 0 + Emerging Moat only; valuation deferred to Phase 3)"
gate0:
  rules_checked: 40
  fails: []
emoat:
  rules_checked: 12
  fails:
    - {severity: "MINOR", rule: "active_categories = Strong/Moderate only", issue: "YAML active_categories lists 7 (A4,D2,B2,G1,H2,C1,A3) but Section-3 prose + completionist_recount say 9 Strong/Moderate (adds borderline Weak-Moderate B3,R1); counts do not reconcile", impact: "none — em_score 26, STRENGTHENING, TURNAROUND all unaffected"}
valuation:
  status: "pending phase 3"
  rules_checked: 0
  fails: []
  note: "B11 (valuation) and B10 (assembly) not produced until Phase 3; not read, not scored in this pass"
recomputed_destination_pe: ""   # N/A in Phase 1 (valuation deferred); concur otherwise
recomputed_decision: ""         # blank — concur with B01 AVOID and B07 STRENGTHENING/TURNAROUND
findings:
  - {severity: "MINOR", location: "B01 Block B / B4", note: "Earliest WC-Days year anchored to FY24 (FY23 payables NOT FOUND); honest no-estimate reading but score-maximising (5 vs a possible 3). Correctly disclosed. No decision impact."}
  - {severity: "MINOR", location: "B01 Block E / E2", note: "E2 rule specifies a 3-year window; only a 1-year change (FY24->FY25 +0.29pp) available. ±1% band applied on available history per operating rule; disclosed. No decision impact."}
  - {severity: "MINOR", location: "B07 Section 3 / active_categories", note: "active_categories (7) vs prose/completionist count (9 Strong/Moderate) do not reconcile; two borderline Weak-Moderate rows (B3,R1) counted in prose but excluded from YAML. Presentational only."}
  - {severity: "MINOR", location: "B07 Section 2C", note: "capex_embedded_growth set to 0/NOT MEANINGFUL after showing the 190% mechanical arithmetic; defensible for asset-light model, flagged in handoff."}
critical_count: 0
major_count: 0
minor_count: 4
acceptance_rate: 98    # 51 of 52 Phase-1 rules passed (Gate 0 + Emerging Moat only)
```
