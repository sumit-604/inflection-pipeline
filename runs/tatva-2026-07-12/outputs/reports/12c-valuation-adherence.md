# STAGE 12 VERIFIER C: FRAMEWORK ADHERENCE — PHASE 3 (VALUATION HALF)
## Tatva Chintan Pharma Chem Ltd (TATVA) | Run 2026-07-12
**Model:** claude-opus-4-8 | **Scope:** RULE 4 valuation audit of B11 + extended B14 decision/position-sizing rules.
Gate 0 (B01) and Emerging Moat (B07) were audited in Phase 1 and are NOT re-checked here.

Frameworks governing: Master v3.3 (Role 1 four-pillar, RRM dual-track, Hurdle Ratio; Role 2 L806-818) / Section 1B v3.3+v3.4 (continuous Pillar 1, Amendment 3 UA ordering, Pillar 3 decoupled 3a/3b/3c, two-tier hurdle, Amendment 6 range) / FTTCP v1.2 (Pillar 1 ROCE-from-forward-verdict table, single-credit rule).

I audit rule application only. Numbers-in-sources is Verifier A's domain; I re-derived only where a framework formula had to be re-run to test compliance.

---

## A. PILLAR-BY-PILLAR COMPLIANCE (B11)

| # | Rule (as written) | Applied in B11 | Re-derivation | Verdict |
|---|---|---|---|---|
| 1 | Pillar 1 uses the **continuous formula** 0.5×ROCE+7.5 (floor 9, cap 24), not the superseded bands (Amdt 5) | Base 0.5(7.36)+7.5 = 11.2x; bear 10.7x; bull 11.6x | 0.5×7.36+7.5 = 11.18 → 11.2x; all above 9x floor | PASS |
| 2 | **FTTCP ROCE forward verdict is sole Pillar 1 authority**; RECOVERING 40-60% → 60/40 weighted avg of current and FY[Y+2] (FTTCP table L329) | RECOVERING 40-60% → 60/40 of FY26 6.6% and FY28 est | Y0=FY26, Y+2=FY28 correct; weighting direction correct (60% on known current) | PASS |
| 3 | Pillar 1 blend arithmetic | Bear 6.48% / Base 7.36% / Bull 8.20% | 0.6(6.6)+0.4(8.5)=7.36; 0.6(6.6)+0.4(6.3)=6.48; 0.6(6.6)+0.4(10.6)=8.20 | PASS |
| 4 | **Single-credit route stated in writing**; RECOVERING routes to Pillar 1, Strategic route barred (FTTCP L337, Amdt 4) | "ROCE recovery credited via: Pillar 1 (midpoint blend). Strategic Premium withheld." | Strategic route only permitted for STAGNANT/FIRING; verdict is RECOVERING → Pillar 1 mandatory. Correct | PASS |
| 5 | **Pillar 2 multiplier matches determination**: INDETERMINATE leaning structural → 0.80x | 0.80x band applied | Matches injected determination; not pushed to 0.65x (no rating confirmation), not lifted | PASS |
| 6 | **No growth offset** on the unconfirmed/structural portion | Offset = +0; effective 0.80x | Leaning-structural → offset withheld per Pillar 2 CRITICAL DISTINCTION; correct | PASS |
| 7 | Quality-Adjusted Base = ROCE Base × Cash Mult | Bear 8.56 / Base 8.96 / Bull 9.28 | 11.2×0.80=8.96; 10.7×0.80=8.56; 11.6×0.80=9.28 | PASS |
| 8 | **Pillar 3a** (📄 documented tier): +2x needs any two of four qualifiers; +0x otherwise (Amdt 4.1) | 1 of 4 met (grade B only); capex-embedded, order book, SOM≥20% all NOT MET → +0x | SOM 14.3% < 20; no order book; no clean committed-capex 📄 → only grade B qualifies. 1 qualifier → +0x | PASS |
| 9 | **Pillar 3b** EM-gated; EM 19.2 < 25 threshold → +0x | +0x | Matches injected EM 19.2 (B07) | PASS |
| 10 | **Pillar 3c** duration premium, 📄 forward visibility ≥2.5yr | No order book/contracted tenor → +0x | Correct; no documented visibility | PASS |
| 11 | **Shared-catalyst flag** where a catalyst feeds both Pillar 1 and Pillar 3 (FTTCP L341) | Dahej flagged SHARED CATALYST; 3a=0 so no premium actually credited through it | Flag present; no double-count because 3a resolves +0x on documented grounds | PASS |
| 12 | **Strategic Premium**: single-credit (ROCE re-rating withheld) + scarcity gate | +0x; re-rating withheld; moats MODERATE, pricing power moderate → no scarcity | Asset-heavy recovering to only ~8-10% ROCE would not earn the +1x re-rating even if routed; single-credit already forbids it | PASS |
| 13 | Raw Destination PE = Quality Base + Growth + Strategic | F = 8.96 + 0 + 0 = 8.96x | Correct | PASS |
| 14 | **UA in Amendment 3 order**: F2 = F×1.25 only if all three qualifiers hold; B10 all_met=false → F2=F, F2 row shown as F | F2 = 8.96x, "UA applied N", F2 row = F | B10 all_met false (1 of 3); UA correctly NOT applied | PASS |
| 15 | **Sector cap absolute**: min(F2, G), G=35x specialty chemicals | H = min(8.96, 35) = 8.96x; cap not binding, no quality uplift to cap | 35x corrects manifest 38x per B10; absolute, not breached | PASS |
| 16 | **Amendment 6** proportional range = value ±7.5%, round to nearest 0.5x, both tracks | T2: 8.96 ±7.5% = 8.29-9.63 → 8.5-9.5x (mid 9.0); T1: 6.80-7.90 → 7.0-8.0x (mid 7.3) | Rounding correct both tracks | PASS |

**Pillar sub-total: 16/16 PASS. Destination PE stands unchanged (Track 2 mid 9.0x, Track 1 mid 7.3x).**

---

## B. RRM DUAL-TRACK, HURDLE, TRIANGULATION (B11)

| # | Rule (as written) | Applied in B11 | Re-derivation | Verdict |
|---|---|---|---|---|
| 17 | RRM base r by cap band, adjusted for governance/durability, bound [9%,18%] | r = 15% (small-cap 14% + FLAG-PROMOTER governance) | Within [9,18]; governance amber cluster documented (GPCB, pay-vs-PAT, 2× CRISIL) | PASS |
| 18 | **RRM = 1+(13.5−r)×0.12**, percentage-point reading (Amdt 4.4), bound ×0.70–×1.60 | 1+(13.5−15)×0.12 = 0.82 | 1+(−1.5)(0.12)=0.82; within bounds; percentage-point reading correct | PASS |
| 19 | Track 1 Destination PE = Fundamental Base PE × RRM | 8.96 × 0.82 = 7.35 → 7.3x (C=F here, premiums zero) | Correct; scenario bear 7.0x, bull 7.6x check out | PASS |
| 20 | **BOTH tracks carried** through every fair value AND the verdict card | Both tracks in Pillar summary, Section 3, 4A, 4C-F, verdict card | Present throughout | PASS |
| 21 | **>15% divergence → conservative track governs entry** | Divergence 18.9% (dest PE) / 16.0% (FV) → Track 1 governs | (9.0−7.3)/9.0 = 18.9%; Track 1 is the more conservative; sets entry zone | PASS |
| 22 | **Two-tier hurdle** (Amdt 4.3): Tier B needs ALL four gates; else Tier A 25% | Tier A: Gate0 48, EM 19.2, promoter CAUTION, FLAG-CASH all fail Tier B → Tier A, divisor 1.953 | Tier B quality gates fail → stays 25% regardless of discovery. Correct | PASS |
| 23 | Hurdle Ratio = (1+EPS CAGR)³ × (Dest PE mid ÷ Current PE); current PE = 1326/17.98 | Current PE 73.75x | 1326/17.98 = 73.75x | PASS |
| 24 | **Credibility-grade gate on Bull**: Bull EPS CAGR usable only if grade A/B (Amdt 2, Master L406) | Grade B → bull 34.5% used | Grade B permits bull row | PASS |
| 25 | HR values → verdict | Base 0.169, Bull 0.241; both << 1.953 → STOP | 1.7047×(7.3/73.75)=0.169; 2.4327×(7.3/73.75)=0.241; T2 0.208/0.297; HR(Bull)<1.953 → STOP | PASS |
| 26 | **4D weights match grade** (grade B Good = 25/50/25, Master L629) | 25/50/25 applied | Correct mapping | PASS |
| 27 | Prob-weighted expected CAGR | −44.1% (Track 1) | 0.25(−52.9)+0.50(−43.7)+0.25(−36.0) = −44.08 → −44.1% | PASS |
| 28 | **SOM cross-check performed** | Base 3yr rev 749.4 vs SOM 754; 14.0% ≤ 14.3% → CONSISTENT | Cross-check executed; base does not exceed SOM ceiling | PASS |
| 29 | Entry price: Tier A divisor 1.953; MoS = 20% below entry (Amdt 4.3) | Entry 237/1.953 = 121; MoS 97 | 237/1.953 = 121.3 → 121; 121×0.80 = 96.8 → 97 | PASS |
| 30 | **Unresolved inputs handled by stated conservative rule, no silent fills** | rating_wc_quote NOT FOUND → held 0.80x no offset; peer medians NOT COMPUTED → no peer-relative; Y3 net debt ~150 disclosed | All three surfaced in input_gaps/unresolved_inputs_used; no estimated fill passed off as fact | PASS |
| 31 | **One-improvement-one-mechanism** (no double-credit) | ROCE recovery only in Pillar 1; shared catalyst flagged, 3a=0 | No quality improvement credited twice | PASS |

**RRM/Hurdle/Triangulation sub-total: 15/15 PASS. Hurdle verdict STOP stands; decision AVOID-on-valuation stands.**

---

## C. B14 DECISION RULES + POSITION SIZING (extended audit)

| # | Rule (as written) | Applied in B14 | Assessment | Verdict |
|---|---|---|---|---|
| 32 | AVOID decision consistent with valuation (Master L809: Gate0 AVERAGE/AVOID OR Promoter CONCERN/AVOID OR U/D<2x OR Hurdle STOP) | Verdict AVOID; cites four independent grounds — Hurdle STOP (decisive), Gate 0 AVERAGE, Promoter CAUTION, U/D 0.82x<2x | AVOID is over-determined: Gate 0 AVERAGE, Hurdle STOP, and U/D 0.82x each independently trigger it and are correctly established. Consistent with B11 AVOID-on-valuation and FTTCP DEEP WATCH. See MINOR note below on the promoter-verdict wording | PASS |
| 33 | Position-size logic per Master L813-818 | None now; if zone reached with thesis intact, cap Small (2-3%); Medium fails (needs Gate0 GOOD+ & Promoter TRUSTWORTHY), Large fails; Promoter cap binds | Medium gate fails directly on Gate 0 AVERAGE and Promoter below TRUSTWORTHY; Small ceiling correct; no operator override recorded. Conditional framing consistent with Entry Conjunction (L811) | PASS |
| 34 | Entry-conjunction / anti-value-trap stated (Master L811) | Section 7 box + narrative: BUY executes only if price in zone AND no thesis-broken trigger fired; zone withdrawn if the drop is the cash flag confirming structural | Correctly reproduced; zone treated as conditional | PASS |

**B14 sub-total: 3/3 rules PASS (1 MINOR imprecision, no decision impact).**

---

## FINDINGS

| Severity | Location | Issue | Impact |
|---|---|---|---|
| MINOR | B14 line 132 / verdict box | Cites Master L809 "Promoter CONCERN/AVOID" as an AVOID trigger while the promoter verdict here is CAUTION, which is a milder band than CONCERN in the promoter vocabulary. The literal L809 trigger is CONCERN/AVOID, not CAUTION | None. AVOID is independently and correctly triggered by Gate 0 AVERAGE, Hurdle STOP, and Upside/Downside 0.82x<2x. Position sizing does not rely on it (Medium fails on Gate 0 and on Promoter-below-TRUSTWORTHY directly). Cosmetic over-citation only |

No CRITICAL, no MAJOR. No misapplication moves the destination PE by ≥1x, flips the Hurdle verdict, or changes the decision.

## CONCLUSION

The valuation half is framework-compliant. Continuous Pillar 1 formula applied with the FTTCP RECOVERING 40-60% verdict as sole authority (60/40 blend); single-credit routed to Pillar 1 in writing; Pillar 2 at 0.80x with no structural offset; Pillar 3 fully +0x with the shared catalyst flagged but not double-credited; UA correctly withheld (all_met false, F2=F); sector cap absolute and non-binding; both tracks carried throughout with Track 1 governing on 18.9% divergence; Hurdle Ratio correctly computed to STOP with the grade-B bull gate honoured; 4D weights 25/50/25; SOM cross-check performed; unresolved inputs handled conservatively with no silent fills. B14 decision and position sizing apply the Master rules correctly. Recomputed destination PE and decision concur with B11 — no change.

---

```yaml
stage: B12c
company: "TATVA"
run_date: "2026-07-12"
model: claude-opus-4-8
status: complete
gate0: {rules_checked: 0, fails: [], note: "already audited phase 1"}
emoat: {rules_checked: 0, fails: [], note: "already audited phase 1"}
valuation:
  rules_checked: 34
  fails: []
  minor:
    - "B14 cites Master L809 'Promoter CONCERN/AVOID' as an AVOID trigger for a CAUTION-band promoter; AVOID is over-determined by Gate 0 AVERAGE + Hurdle STOP + U/D 0.82x, so no decision impact (MINOR)"
  confirmed:
    pillar1_continuous_formula: true
    fttcp_verdict_sole_authority: "RECOVERING 40-60% -> 60/40 blend (7.36% base -> 11.2x)"
    single_credit_route: "Pillar 1, stated in writing; Strategic Premium withheld"
    pillar2_multiplier: "0.80x, no growth offset (INDETERMINATE leaning structural)"
    pillar3: "3a +0x (1 of 4 qualifiers) / 3b +0x (EM 19.2<25) / 3c +0x (no doc visibility)"
    shared_catalyst_flagged_not_double_credited: true
    ua_applied: false
    ua_order_correct: "F2 = F (all_met false); min(F2, 35)"
    sector_cap_absolute: 35
    both_tracks_carried: true
    divergence_governing: "18.9% >15% -> Track 1 (conservative) governs entry"
    hurdle_ratio: {tier: "A", threshold: 1.953, base: 0.169, bull: 0.241, verdict: "STOP", bull_gate_grade_B: true}
    weights_4d: "25/50/25 (grade B)"
    som_crosscheck: "performed; 14.0% <= 14.3% consistent"
    entry_math: "237/1.953=121; MoS 97"
    no_silent_fills: true
    one_improvement_one_mechanism: true
    b14_decision_consistent: true
    b14_position_sizing: "Small cap correct; Medium/Large fail on Gate 0 AVERAGE + Promoter<TRUSTWORTHY"
recomputed_destination_pe: ""
recomputed_decision: ""
findings:
  - {severity: "MINOR", location: "B14 L132 / verdict box", claimed: "Promoter CAUTION cited as L809 AVOID trigger (rule says CONCERN/AVOID)", note: "No decision impact; AVOID over-determined by Gate 0 AVERAGE, Hurdle STOP, U/D 0.82x"}
critical_count: 0
major_count: 0
minor_count: 1
acceptance_rate: 100
```
