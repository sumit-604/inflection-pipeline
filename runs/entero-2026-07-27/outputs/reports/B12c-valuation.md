# B12c — VERIFIER C (FRAMEWORK ADHERENCE) — PHASE 3 VALUATION-ADHERENCE SCOPE
## ENTERO HEALTHCARE SOLUTIONS LTD (ENTERO)
**Run:** 2026-07-27 | **Report date:** 2026-07-28 | **Model:** claude-opus-4-8
**Scope this pass:** DEFERRED valuation-adherence audit ONLY (B11 vs Section 1B v3.5.1 + Role 2 decision rules). Gate 0 (B01) and Emerging Moat (B07) were audited in Phase 1 and are NOT re-opened here.
**Authorities:** Master v3.3 (Section 1B + Role 2), Section_1B_v3.3_Amendments, Section_1B_v3_5_1_Reconciliation, FTTCP v1.2.

> Boundary: I audit framework application and arithmetic re-derivation only. Whether a source number is TRUE at its cited anchor is Verifier A's non-overridable gate; I do not adjudicate it. The destination PE 15.0x (both tracks) and the FORWARD owners'-EPS basis are OPERATOR OVERRIDES recorded in fttcp-deliberation; per the task they are authoritative inputs, audited for CONSISTENT USE, not re-derived as violations.

---

## 1. OPERATOR-OVERRIDE CONSISTENCY (authoritative inputs — check use, not derivation)

| # | Rule | Framework anchor | Re-derivation / check | PASS/FAIL |
|---|---|---|---|---|
| V1 | Destination PE 15.0x applied on BOTH tracks | fttcp-deliberation Override 1 | B11 §1, §3, §5 all use 15.0x; Track1=Track2=15.0x, divergence 0% | PASS |
| V2 | Earnings basis = ONE YEAR FORWARD owners' EPS | Override 2 | Exit FV = 15.0x × FY30 owners' EPS (one year forward from FY29 exit); B11 §3 | PASS |
| V3 | Owners' PAT post-minority; NCI ~26% FY27+ | Override 2; B10 | EPS ladder on 4.35 Cr shares, NCI 26% base; FY26 owners' EPS Rs26.45 | PASS |
| V4 | Sector cap (VAD 25x) NOT breached | Amendment 3 (cap absolute) | 15.0x < 25x; no breach. Also < the pharma/CDMO 38x that VAD replaced | PASS |
| V5 | 15.0x above pillar-derived (13.4x additive / 10.2x RRM), reported not used | fttcp-deliberation | B11 §1 reports pillar tracks, applies flat 15.0x per override | PASS |

**Override use is internally consistent.** No independent exit-PE was substituted; both tracks carry 15.0x through every fair value and the verdict card.

---

## 2. PILLAR DETAIL — INTERNAL CONSISTENCY (informational tracks, for the record)

| # | Rule | Anchor | Re-derivation | PASS/FAIL |
|---|---|---|---|---|
| V6 | Continuous Pillar 1 formula (not old bands) | Amendment 5 | 0.5 × 11.05 + 7.5 = **13.03x** (floor 9 / cap 24; not bound) — matches | PASS |
| V7 | Pillar 2 multiplier 0.80x, offset WITHHELD (INDETERMINATE takes no clean offset) | Amdt 9 / FTTCP; deliberation | 13.03 × 0.80 = **10.42x**; growth offset 0. Matches; no offset on INDETERMINATE — correct | PASS |
| V8 | Pillar 3 = +3x (3a +2, 3b +1, 3c +0) | Amendment 4.1/4.2; deliberation | Raw additive 13.03 + 0 + 0.42? → stated 13.42x = 10.42 + 3.0. Matches | PASS |
| V9 | Strategic premium +0x; single-credit ROCE via Pillar 1, Strategic barred | Amendment 4 | +0x strategic; 3c ROCE = +0 (not double-credited); route stated "Pillar 1" | PASS |
| V10 | RRM percentage-point reading | Amendment 4.4 | 1 + (13.5 − 15.3) × 0.12 = 1 − 0.216 = **0.78x** (within 0.70–1.60) — matches | PASS |
| V11 | RRM base r build | Master Role 1 (small/micro 14%, adj governance/durability, bound [9,18]) | 14% + FLAG-PROMOTER CONCERN + FLAG-CASH → 15.3%, in bounds | PASS |
| V12 | RRM destination PE | Master Role 1 | 13.03 × 0.78 = **10.16 ≈ 10.2x** — matches | PASS |
| V13 | Pillar divergence + conservative-governs rule | Master Role 1 (>15% → conservative governs) | (13.4−10.2)/13.4 = 23.9% ≈ 24%; RRM would govern PRE-override; override collapses both to 15.0x (divergence 0). Handled and disclosed | PASS |
| V14 | UA NOT applied | Amendment 3 (requires FII+DII <3%) | FII+DII ~19.8% fails the <3% qualifier → UA correctly not applied; F2 row n/a | PASS |
| V15 | SHARED CATALYST flag present | Amendment 4 | M&A pause drives Pillar 1 ROCE recovery AND part of Pillar 3; flagged in B11 §5 and B14 | PASS |
| V16 | Amendment 6 ±7.5% band | Amendment 6 | 15.0x ±7.5% → 14.0–16.0x, reported as informational | PASS |

---

## 3. HURDLE RATIO — RE-DERIVATION (Amendment 2, Tier A)

HR = (1 + owners'-EPS CAGR)³ × (Destination PE mid ÷ Current PE).

**Basis-consistency check (the SFL lesson):** current PE 48.1x is TRAILING on owners' EPS Rs26.45; growth term is owners' reported EPS CAGR; destination 15.0x. Owners'-EPS, trailing, on BOTH sides of the ratio. No forward-EPS current PE mixed with trailing growth. **CONSISTENT.**

| Case | EPS CAGR re-derivation | HR re-derivation | Report | Match |
|---|---|---|---|---|
| Base (FY26→FY29) | (62.39/26.45)^(1/3) − 1 = 2.3588^0.333 − 1 = **33.1%** | (1.331)³ × (15.0/48.1) = 2.358 × 0.3119 = **0.735 ≈ 0.74** | 0.74 | ✓ |
| Bull (FY26→FY29) | (76.74/26.45)^(1/3) − 1 = **42.6%** | (1.426)³ × 0.3119 = 2.900 × 0.3119 = **0.90** | 0.90 | ✓ |

- Threshold Tier A = 1.25³ = **1.953** — confirmed.
- Bull permitted: Amendment 2 conservative-bias note allows Bull EPS CAGR only if delivery grade Good/Excellent; grade is **B (Good)** → bull row permitted. Compliant.
- HR(Bull) 0.90 < 1.953 → **STOP** (Amendment 2: HR(Bull) < 1.953 = overvalued, 25% infeasible even on bull earnings). Verdict correct.

**Observation (MINOR, no verdict impact):** the HR uses FY29 exit-year EPS while the operator FORWARD-EPS valuation applies 15.0x to FY30 EPS. The HR's implied 3-yr price CAGR (FY29 EPS × 15 = Rs936 → −9.7%) therefore does not equal the reported base return CAGR (FY30 EPS × 15 = Rs1,112 → −4.4%). The direction is CONSERVATIVE (HR understated), the STOP verdict is robust under either basis, and the HR formula is applied exactly as Amendment 2 (and the task) specify. Recorded as an internal-consistency note only.

---

## 4. ENTRY ZONE, MoS, DECISION (Amendment 4.3, Role 2)

| # | Rule | Anchor | Re-derivation | Report | PASS/FAIL |
|---|---|---|---|---|---|
| V17 | Tier A threshold / entry divisor 1.953 | Amendment 4.3 | 1.25³ = 1.953 | 1.953 | PASS |
| V18 | Entry (25%) = base FV ÷ 1.953 | Amendment 4.3 | 1,112 / 1.953 = **569.4 ≈ 569** | 569 | PASS |
| V19 | Extra-safety (30%) = base FV ÷ 2.197 | derived (1.30³) | 1,112 / 2.197 = **506.1 ≈ 506** | 506 | PASS |
| V20 | MoS = 20% below the 25% entry | Amendment 4.3 | 569 × 0.80 = **455.2 ≈ 455** | 455 | PASS |
| V21 | Entry zone on the governing (single, converged) fair value | Master Role 1 | Override collapses tracks; base FV 1,112 governs | 506–569 | PASS |
| V22 | AVOID follows the rules | Amendment 2 + Role 2 | HR STOP → AVOID; over-determined (Gate0 AVERAGE, Promoter CONCERN, U/D 0.36x <2x) | AVOID (on valuation) | PASS |

---

## 5. ROLE 2 — TIER, UA, SINGLE-CREDIT, SIZING, SHARED CATALYST

| # | Rule | Anchor | Check | PASS/FAIL |
|---|---|---|---|---|
| V23 | Tier A assigned; Tier B barred | Amendment 4.3 | Tier B requires ALL: FII+DII≥3% ✓, Gate0 GOOD+/EM≥25 ✓, **promoter TRUSTWORTHY+ ✗ (CONCERN)**, no structural FLAG-CASH ✗. Fails → stays Tier A 25%. Correct | PASS |
| V24 | UA not applied | Amendment 3 | FII+DII ~19.8% fails <3% qualifier; all-three-qualifiers = NO | PASS |
| V25 | Single-credit ROCE (Pillar 1, Strategic barred) | Amendment 4 | Credited Pillar 1 midpoint; Strategic +0x; 3c +0x; route stated. No double-credit | PASS |
| V26 | SHARED CATALYST flagged | Amendment 4 | Present (single point of failure noted for Role 3) | PASS |
| V27 | Position sizing consistent | Master Role 2 (lines 815–817) | Large needs Gate0 EXCELLENT + Promoter TRUSTWORTHY+; Medium needs Gate0 GOOD+ + Promoter TRUSTWORTHY; Gate0 AVERAGE + Promoter CONCERN → **Small (2–3%) ceiling at most**, and only if BUY. Decision is AVOID → **None**. B14 sizing reasoning matches framework. No operator sizing override recorded | PASS |

---

## 6. OWNERS' EPS LADDER — ARITHMETIC vs GUIDED INPUTS

Guided inputs: revenue +23% FY27, core EBITDA margin 5.0% base, NCI ~26%, tax 22–23%.

**FY27 base worked re-derivation:**
- Revenue: 6,591.21 × 1.23 = **8,107.19** ✓
- EBITDA: 8,107.19 × 5.0% = **405.36** ✓
- PBT: 405.36 − 52.0 (dep) − 62.0 (int) + 20.0 (OI) = **311.36** ✓
- Tax 22.5%: 70.06 → pre-min PAT **241.30** ✓
- NCI 26%: 62.74 → owners **178.56**; EPS = 178.56 / 4.35 = **41.05** ✓

**FY30 base worked re-derivation (forward-EPS year):**
- EBITDA 12,653 × 5.5% = 695.9; PBT 695.9 − 76 − 80 + 26 = 565.9; tax 23% = 130.2; pre-min 435.7; NCI 26% = 113.3; owners 322.4; EPS = 322.4 / 4.35 = **74.12** ✓

**Fair values:** 15.0 × {57.15, 74.12, 94.79} = **857 / 1,112 / 1,422** ✓
**Prob-weighted CAGR (grade B 25/50/25):** 0.25(−12.3) + 0.50(−4.4) + 0.25(+3.8) = **−4.3%** ✓
**U/D ratio:** 11.7 / 32.7 = **0.36x** ✓
**SOM cross-check:** base revenue CAGR FY26→FY29 = (11,003/6,591)^(1/3) − 1 = **18.6%**, below SOM-implied 33.8% and below guided 23% → conservative, no cut required ✓

| # | Rule | Check | PASS/FAIL |
|---|---|---|---|
| V28 | FY27 ladder consistent with guided rev +23% / margin 5.0% / NCI 26% / tax 22.5% | Re-derived to EPS 41.05 | PASS |
| V29 | FY30 forward-EPS worked example internally consistent | Re-derived to EPS 74.12 | PASS |
| V30 | Fair values = 15.0x × FY30 owners' EPS | 857/1,112/1,422 | PASS |
| V31 | Return, prob-weight, U/D, SOM cross-check arithmetic | All re-derived clean | PASS |

---

## 7. FINDINGS (valuation scope)

| Severity | Location | Finding |
|---|---|---|
| MINOR | B11 §4.2 / §4.3 | HR uses FY29 exit-year EPS while the forward-EPS valuation applies 15.0x to FY30 EPS; HR-implied price CAGR (−9.7%) ≠ reported base return CAGR (−4.4%). Conservative direction, STOP robust, formula applied exactly per Amendment 2. Internal-consistency note only. |
| MINOR | B11 §0 / B10 (carried from fttcp-deliberation) | Sector-cap row labelled "Cybersecurity / VAD 25x" for a pharma/MedTech distributor is facially wrong; it is operator-accepted upstream and NON-BINDING (15.0x sits below both the VAD 25x and the pharma/CDMO 38x it replaced). No valuation effect; not a stage-11 derivation fault. |

No CRITICAL, no MAJOR. No misapplication changes the destination PE by >1x, flips the Hurdle verdict, or changes the decision.

---

## 8. VERDICT

- **recomputed_destination_pe:** CONCUR — 15.0x (operator-set, applied consistently on both tracks; sector cap not breached).
- **recomputed_decision:** CONCUR — AVOID (on valuation); HR STOP (base 0.74 / bull 0.90 < 1.953), over-determined by Gate0 AVERAGE + Promoter CONCERN + U/D 0.36x.
- Rules checked (valuation scope): 31. Clean passes: 31; two MINOR presentational/consistency observations recorded, neither a rule fail with decision impact.

---

```yaml
stage: B12c
company: "ENTERO"
run_date: "2026-07-27"
model: claude-opus-4-8
status: complete
scope: "phase3-valuation-adherence-only (gate0/emoat audited in phase 1, not re-opened)"
gate0: {rules_checked: 0, fails: []}   # audited in Phase 1; out of scope this pass
emoat: {rules_checked: 0, fails: []}   # audited in Phase 1; out of scope this pass
valuation:
  rules_checked: 31
  fails: []
findings:
  - {severity: "MINOR", location: "B11 §4.2/§4.3 Hurdle Ratio", note: "HR uses FY29 exit-year EPS while forward-EPS valuation applies 15.0x to FY30; HR-implied CAGR -9.7% vs reported base -4.4%; conservative direction, STOP robust, formula per Amendment 2 — internal-consistency note only"}
  - {severity: "MINOR", location: "B11 §0 / B10 sector-cap row (carried from fttcp-deliberation)", note: "Sector cap labelled Cybersecurity/VAD 25x for a pharma/MedTech distributor is facially wrong but operator-accepted upstream and non-binding (15.0x < 25x < 38x pharma); no valuation effect"}
recomputed_destination_pe: "CONCUR (15.0x, operator-set, applied consistently both tracks, within 25x cap)"
recomputed_decision: "CONCUR (AVOID on valuation; HR base 0.74 / bull 0.90 STOP < 1.953)"
critical_count: 0
major_count: 0
minor_count: 2
acceptance_rate: 100   # 31/31 valuation rules applied as written; 2 MINOR presentational notes, no rule fail with decision impact
```
