# VERIFIER C — FRAMEWORK ADHERENCE AUDIT (PHASE 3, VALUATION HALF)
## UFBL | Run 2026-08-05 | Model claude-opus-4-8

**Scope.** Phase 3 valuation-adherence only. B01 (Gate 0) and B07 (Emerging Moat) were
audited in phase 1 and are NOT re-run here. This audit covers B11 (Role 1 valuation) and
B10 (assembly) against Section 1B v3.5.1 / Amendments / FTTCP v1.2, EXTENDED to B14 (Role 2)
decision rules and position sizing against Master Prompt v3.3.

**Authoritative base.** Per `outputs/final/fttcp-deliberation.md` Section 5, the operator
approved a 25% pre-Ind AS ROCE, an additive-track governing exit PE of 25.0x on a one-year-
forward pre-Ind AS basis (an explicit operator override of the RRM-governs default, recorded
in Override 2), and Tier A 25% hurdle. I audit rule application ON that approved base and
re-derive every step from the stated inputs.

---

## PART 1 — SECTION 1B PILLAR ARITHMETIC (B11 §1B, B10 approved-pillars)

| # | Rule | Stated value | My re-derivation | Verdict |
|---|---|---|---|---|
| V1 | Pillar 1 base PE = 0.5×ROCE + 7.5 (Amdt 5) | 20.0x | 0.5×25 + 7.5 = 12.5+7.5 = **20.0x** | PASS |
| V2 | Floor 9x / cap 24x applied | not binding | 20.0 in [9,24] → not binding | PASS |
| V3 | Continuous formula used, not old bands | continuous | Amdt 5 continuous form applied; no band table | PASS |
| V4 | Pillar 2 quality-adjusted base = base × mult | 23.0x | 20.0 × 1.15 = **23.0x** | PASS |
| V5 | Cash multiplier matches determination (growth-induced, no offset on structural) | 1.15x growth-induced | Determination GROWTH-INDUCED (not structural); 1.15x within growth band; no structural offset misapplied | PASS |
| V6 | Pillar 3 decoupled 3a/3b/3c (Amdt 4.1/4.2) | 3a +2.0 / 3b 0 / 3c 0 | 3b=0 correct (EM 9.1 < 25 threshold); 3a=+2.0 independent of 3b; 3c=0 (no order book) | PASS |
| V7 | Pillar 3 combined ≤ +6x cap | +2.0x | 2.0+0+0 = 2.0 ≤ 6 | PASS |
| V8 | Additive raw destination PE = quality base + 3a+3b+3c + strategic | 25.0x | 23.0 + 2.0 + 0 + 0 + 0 = **25.0x** | PASS |
| V9 | Strategic premium gate + single-credit (Amdt 4) | +0.0x, ROCE via Pillar 1, re-rating BARRED | Pricing-power gate fails → 0; recovery credited via Pillar 1 midpoint; Strategic ROCE re-rating barred; route stated explicitly | PASS |
| V10 | UA in Amdt 3 order min(F×1.25, cap); all 3 qualifiers | NOT applied | Institutions ~27.8% >> 3% qualifier fails → UA not qualified; F2 = F = 25.0x; ordering not triggered | PASS |
| V11 | Sector cap absolute; H = min(F2, G) | 30x Hotels, not binding | min(25.0, 30.0) = **25.0x** not binding | PASS |
| V12 | Destination PE range = value ±7.5%, rounded to nearest 0.5x (Amdt 5) | 23.1x–26.9x | 25×0.925=23.125, 25×1.075=26.875. Nearest 0.5x = **23.0x–27.0x**. Report/delib carried unrounded 23.1–26.9 | MINOR (rounding convention; mid 25.0 unaffected) |

**Destination PE (additive, governing): re-derived 25.0x. CONCUR.**

---

## PART 2 — RRM TRACK, DIVERGENCE, TRACK SELECTION (B11 §1B RRM / track divergence)

| # | Rule | Stated | My re-derivation | Verdict |
|---|---|---|---|---|
| V13 | RRM = 1 + (13.5 − r)×0.12, percentage-point reading (Amdt 4.4) | 0.70 | 1 + (13.5−16)×0.12 = 1 + (−2.5)(0.12) = 1 − 0.30 = **0.70**; floored at 0.70 bound | PASS |
| V14 | r bound [9%,18%] respected | r=16% | 16% within [9,18]; base 14% + 2% governance/durability | PASS |
| V15 | RRM track destination PE = base × RRM | 17.5x | 25.0 × 0.70 = **17.5x** | PASS |
| V16 | RRM range ±7.5% | 16.2–18.8x | 17.5×0.925=16.19, ×1.075=18.81; nearest 0.5x = 16.0–19.0x (carried 16.2–18.8, same convention as V12) | MINOR (same rounding note) |
| V17 | BOTH tracks carried through every FV and the verdict card | yes | Track 1 and Track 2 fair values and verdict card both present in §4A/4C/4H | PASS |
| V18 | Divergence computed; >15% trigger noted | 30.0% | (25.0−17.5)/25.0 = **30.0%** > 15% | PASS |
| V19 | Conservative track sets entry on >15% divergence — UNLESS legitimate operator override | additive governs (override) | Framework default = RRM (more conservative). Operator OVERRODE to additive 25.0x (delib Override 2, legitimate). Report flags divergence, states RRM is more conservative, records both, and applies operator-selected additive as governing. Override is recorded and legitimate | PASS |

**Note on V19 (observation, not a finding).** The operator's additive selection is the more
GENEROUS track. Had the framework default (RRM) governed, base FV would be Rs 445 and the entry
ceiling Rs 228 — i.e. the decision would be even MORE decisively AVOID. The report records both,
so the AVOID is robust to track choice.

---

## PART 3 — EARNINGS BASIS & HURDLE RATIO (B11 §2, §4) — the SFL trap check

| # | Rule | Stated | My re-derivation | Verdict |
|---|---|---|---|---|
| V20 | Consistent basis both sides of HR; no post-Ind AS EPS mixed with pre-Ind AS ROCE/EV (SFL trap) | all pre-Ind AS | ROCE base, EV/EBITDA, and the EPS the 25.0x is applied to are ALL pre-Ind AS. Financial net debt Rs 102 cr in EV bridge; Rs 750.84 cr lease liability excluded from pre-Ind AS bridge. No mixed-basis error | PASS |
| V21 | HR = (1+EPS CAGR)³ × (Dest PE mid ÷ Current PE) | simplified to target/CMP | Algebra: with Current PE = CMP/FY27 EPS and (1+CAGR)³ = FY30/FY27 EPS, the FY27 base CANCELS → HR = (FY30 EPS × 25.0)/CMP = Year-3 target/CMP. Simplification is **valid and basis-consistent**; it also removes the thin-base CAGR artifact | PASS |
| V22 | HR base value | 0.82 | 635 ÷ 772 = **0.822 ≈ 0.82** | PASS |
| V23 | HR bull value | 1.40 | 1,084 ÷ 772 = **1.404 ≈ 1.40** | PASS |
| V24 | HR bear value | 0.30 | 229 ÷ 772 = **0.297 ≈ 0.30** | PASS |
| V25 | HR verdict: HR(Bull) < 1.953 → STOP (Amdt 1 band) | STOP | Bull 1.40 < 1.953 → **STOP**; correct band (bull fails ⇒ STOP, not CONDITIONAL) | PASS |
| V26 | Bull admissibility gate (credibility grade on Bull) | grade B → bull usable | Grade B admits bull; bull still fails → STOP is conservative and correct | PASS |

**Cross-check of the FY30 EPS × 25.0 targets:** Bear 9.16×25=229 ✓ / Base 25.41×25=635 ✓ /
Bull 43.35×25=1,084 ✓. Targets tie to the verdict card.

---

## PART 4 — ENTRY, MoS, RETURN MATH, VALIDATION (B11 §4C–4G)

| # | Rule | Stated | My re-derivation | Verdict |
|---|---|---|---|---|
| V27 | Entry @25% = base FV ÷ 1.953 (Tier A, Amdt 4.3) | Rs 325 | 635 ÷ 1.953 = **Rs 325.1** | PASS |
| V28 | Entry @30% = base FV ÷ 2.197 | Rs 289 | 635 ÷ 2.197 = **Rs 289.0** | PASS |
| V29 | MoS = 20% below the 25% entry | Rs 260 | 325 × 0.80 = **Rs 260** | PASS |
| V30 | Prob-weighted CAGR uses grade-B weights 25/50/25 (4D) | −8.5% | 0.25(−33.3)+0.50(−6.3)+0.25(+12.0) = −8.325−3.15+3.0 = **−8.48 ≈ −8.5%** | PASS |
| V31 | Scenario CAGRs from targets/CMP | Bear −33.3/Base −6.3/Bull +12.0 | (229/772)^⅓−1=−33.4; (635/772)^⅓−1=−6.3; (1084/772)^⅓−1=+12.0 | PASS |
| V32 | Upside/Downside ≥2x check (4F) | 0.57 (fails) | Report used BULL upside +40.4% ÷ bear downside −70.3% = **0.57**. Master 4F template specifies BASE upside ÷ bear downside; base target Rs 635 is BELOW CMP ⇒ base upside negative ⇒ ratio fails harder. Report discloses "base offers negative return; asymmetry fails" | MINOR (numerator basis differs from template; verdict unchanged and disclosed) |
| V33 | 4G pillar validation performed (ROCE/cash/catalyst/single-credit/UA/sector) | all rows present | §4G table complete; ROCE row flagged CAVEAT (operator anchor), single-credit PASS, UA PASS, sector-cap PASS | PASS |
| V34 | SOM cross-check performed (Amdt/2D) | consistent | Base revenue CAGR 15% < SOM-implied 20.6% (B09) → conservative | PASS |
| V35 | Unresolved inputs handled by conservative rule, no silent fills | yes | Owned-depreciation ex-ROU (higher-dep conservative bias), peer EV/EBITDA UNRESOLVED (flagged, not fabricated), tax at full 25.17% with loss carryforward NOT credited — all conservative, all disclosed; STOP shown robust to depreciation sensitivity | PASS |
| V36 | One-improvement-one-mechanism (no double-credit) | honoured | ROCE recovery credited only via Pillar 1; not re-credited in Strategic or 3a | PASS |

---

## PART 5 — ROLE 2 DECISION RULES & POSITION SIZING (B14 vs Master v3.3)

| # | Rule | Stated | Check | Verdict |
|---|---|---|---|---|
| V37 | AVOID triggers (Master "Decision rules": Gate0 AVERAGE/AVOID OR Promoter CONCERN/AVOID OR U/D<2x OR HR=STOP) | AVOID | Over-determined: HR=STOP ✓, U/D 0.57<2x ✓, Gate0 AVOID ✓, Promoter CAUTION ✓ — any one sufficient | PASS |
| V38 | Binding reason identified (price) | price / Hurdle STOP | Report names price as dispositive; quality flags reinforce but do not set verdict | PASS |
| V39 | Entry conjunction (anti-value-trap) stated in Section 7 verdict box | present | §7 states both-gates rule: price in Rs 289–325 AND no thesis-broken trigger fired; withdrawn-zone logic explicit | PASS |
| V40 | Position size caps bind (Promoter cap always binds; never Large unless Gate0 EXCELLENT + Promoter TRUSTWORTHY+) | Small cap, no capital now | Gate0 AVOID + Promoter CAUTION each bar Medium/Large; verdict AVOID ⇒ no capital deployed; Small documented as hypothetical ceiling only; no override recorded in deliberation, none applied | PASS |
| V41 | Entry zone = base FV ÷ 1.953 carried consistently into thesis | Rs 289–325 | B14 §5/§7 match B11 (289–325, MoS 260); target 635 base/1,084 bull | PASS |
| V42 | 5yr target discipline (no fabrication) | NOT FOUND | Role 1 built 3yr/FY30 only; B14 correctly reports 5yr target NOT FOUND rather than inventing | PASS |

---

## PART 6 — B10 ASSEMBLY FIDELITY (approved-pillar carry-through)

B10 `fttcp_approved_valuation_pillars_authoritative` carries the deliberation Section 5 values
verbatim: Pillar 1 ROCE 25.0 / base PE 20.0 / cash 1.15 / quality base 23.0 / 3a +2.0 /
3b 0 / 3c 0 / strategic 0 / additive 25.0 / RRM 17.5 / sector cap 30 / exit PE 25.0 /
earnings basis one-year-forward pre-Ind AS / Tier A. Every value matches the deliberation and
is carried unchanged into B11. The two recorded conflicts (mechanical 5.38% ROCE vs 25% override;
RRM 17.5x vs additive 25.0x) are logged with `used` = the operator-approved value. No silent
substitution. PASS.

---

## SUMMARY

- **Rules checked:** 42 (V1–V42). **Material fails: 0.** **MINOR: 2** (V12/V16 range-rounding
  convention; V32 upside/downside numerator basis — both cosmetic, decision unaffected, disclosed).
- **CRITICAL: 0 | MAJOR: 0 | MINOR: 2.**
- **Recomputed destination PE:** 25.0x additive (governing) / 17.5x RRM — **CONCUR** with B11/B10.
- **Recomputed decision:** **AVOID** — CONCUR. My independent HR recomputation reproduces base
  0.82 / bull 1.40, both < 1.953 ⇒ STOP; base target Rs 635 sits below CMP Rs 772; U/D 0.57 < 2x.
  Even on the operator's own generous additive base, 25% CAGR is infeasible at Rs 772.
- **SFL mixed-basis trap:** NOT present. Both sides of the Hurdle Ratio are pre-Ind AS; the FY27
  base cancels analytically. The consistency guard was honoured.
- **Operator overrides (Pillar 1 25% ROCE; additive-track governing exit multiple):** both
  recorded in deliberation Section 2, legitimate, and correctly applied on the approved base with
  the mechanical divergence flagged (independent-divergence note) rather than silently adopted.

**Acceptance rate: 40/42 = 95%** (well above the 60% REWORK floor).

```yaml
stage: B12c
company: "UFBL"
run_date: "2026-08-05"
model: claude-opus-4-8
status: complete
gate0: {rules_checked: 0, fails: []}      # audited in phase 1; not re-run per scope
emoat: {rules_checked: 0, fails: []}      # audited in phase 1; not re-run per scope
valuation:
  rules_checked: 42
  fails:
    - {rule: "V12/V16 destination-PE range rounding to nearest 0.5x (Amdt 5)", severity: "MINOR", note: "Carried 23.1-26.9x / 16.2-18.8x (unrounded +/-7.5%) vs convention 23.0-27.0x / 16.0-19.0x; mid 25.0x/17.5x unaffected, no decision impact"}
    - {rule: "V32 upside/downside numerator basis (Master 4F)", severity: "MINOR", note: "Ratio 0.57 computed on BULL upside; template specifies BASE upside/bear downside. Base target 635 < CMP => base ratio fails harder. Disclosed; verdict unchanged"}
recomputed_destination_pe: ""   # concur: 25.0x additive governing / 17.5x RRM
recomputed_decision: ""         # concur: AVOID
findings:
  - {severity: "MINOR", location: "B11 §1B range / deliberation S5", claimed: "23.1x-26.9x (and RRM 16.2-18.8x)", recomputed: "23.0x-27.0x (16.0-19.0x) per nearest-0.5x rounding", note: "Cosmetic; mid unaffected"}
  - {severity: "MINOR", location: "B11 §4F", claimed: "U/D 0.57 on bull upside", recomputed: "Base upside negative (target 635 < CMP 772); ratio fails regardless", note: "Numerator basis differs from Master 4F template; disclosed; verdict unchanged"}
critical_count: 0
major_count: 0
minor_count: 2
acceptance_rate: 95
```
