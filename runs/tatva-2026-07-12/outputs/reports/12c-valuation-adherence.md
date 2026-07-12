# STAGE 12c: VERIFIER C — FRAMEWORK ADHERENCE (VALUATION), AMENDMENT 4.5 REFRESH
## Tatva Chintan Pharma Chem Ltd (TATVA) | Run 2026-07-12
**Model:** claude-opus-4-8 | **Scope:** RULE 4 valuation audit of the REFRESHED B11 under Section 1B Amendment 4.5 (v3.5) plus the standard valuation-adherence checks.
Gate 0 (B01) and Emerging Moat (B07) were audited in Phase 1 and are NOT re-checked here.

> This supersedes the pre-4.5 valuation-adherence audit previously held at this path. The refresh changed exactly one input — the Pillar 1 ROCE anchor — moving from the 60/40 blend (7.36% → 11.18x, dest PE 9.0x/7.3x, entry 121, MoS 97) to the Amendment 4.5 three-anchor blend (13.51% → 14.26x, dest PE 11.4x/9.4x, entry 118-147, MoS 118). Decision unchanged: AVOID (Hurdle STOP).

**Authority:** Master v3.3 (Role 1 four-pillar, RRM dual-track, Hurdle) / Section 1B v3.3 + v3.4 + **Amendment 4.5 (v3.5)** / FTTCP v1.2. I audit rule application only; numbers-in-source belong to Verifier A. I re-derived formulas where compliance required it.

---

## PART 1 — AMENDMENT 4.5 (v3.5) SPECIFIC AUDIT

### 1.1 Applicability gate — does 4.5 fire at all?

| Rule (4.5) | Requirement | B11 state | Check | Verdict |
|---|---|---|---|---|
| Trigger conjunction | Applies ONLY when backward verdict TEMPORARILY DEPRESSED **and** forward RECOVERING | Backward TEMPORARILY DEPRESSED (FY24 10.91 → FY25 1.20 → FY26 6.6, capital-cycle trough; "if growth stopped would ROCE recover" passes); forward RECOVERING 40-60% | Both present, both cited (B11 FTTCP handoff; B10 "RECOVERING, probability 40-60%"). Conjunction correct — 4.5 legitimately fires | PASS |
| Not structural decay | Must be trough, not structural erosion | Trough attributed to Dahej capex + post-IPO cash bloat | Correctly scoped; structural decay would bar 4.5 | PASS |

### 1.2 Normalized ROCE anchor — 📄-gated, capped, named catalyst

| Rule (4.5) | Requirement | B11 / B10 | Re-derivation | Verdict |
|---|---|---|---|---|
| Median of last complete pre-depression cycle | Median ROCE FY18-FY21 from Gate0/AR history | FY18 18.8 / FY19 20.0 / FY20 24.9 / FY21 25.4 | Sorted [18.8, 20.0, 24.9, 25.4]; median of 4 = (20.0+24.9)/2 = **22.45%** ✓ | PASS |
| Gate A: historical ROCE series 📄 | Documented pre-depression series | Screener Data_Sheet FY18-21, EBIT/(NetWorth+Borrowings), B01 basis | Documented tier; method matches B01. Present | PASS |
| Gate B: specific mechanical unwind catalyst 📄 | Named capex/cash/WC unwind | Dahej block operational Jan 2026, confirmed Q4 FY26; utilisation 64.11%/30.54% headroom to 75-80% (B05/B04) | Named, mechanical, documented. Present | PASS |
| Cap at evidenced median | May never exceed evidenced median | Uses 22.45% (= the median exactly) | Not exceeded; no invention | PASS |
| NOT FOUND discipline | If either gate NOT FOUND, 4.5 does not apply | Both gates PASS; B11 states counterfactual ("had either been NOT FOUND, standard 60/40 blend stands") | Correctly conditioned | PASS |

### 1.3 The 40-60% RECOVERING blend and continuous formula

| Rule (4.5 / Amd 5) | Requirement | B11 | Re-derivation | Verdict |
|---|---|---|---|---|
| Blend weights, 40-60% band | 40% Normalized + 30% FY[Y+2] + 30% current | 0.40×22.45 + 0.30×8.5 + 0.30×6.6 | 8.98 + 2.55 + 1.98 = **13.51%** ✓ | PASS |
| FY[Y+2] identity | Two years forward of FY26 base = FY28 | FY28 base 8.5% used as FY[Y+2] | Consistent with Year0=FY26; B10 FY28 base 8.5% | PASS |
| Feed continuous formula (Amd 5) | 0.5×ROCE + 7.5, floor 9 cap 24 | 0.5×13.51 + 7.5 = 14.255 → 14.26x | 14.255 ✓; within [9,24] | PASS (see MINOR-1) |
| Explicit three-anchor display + cite evidence | Worksheet + verdict card show blend | Pillar 1 block and verdict card show 0.40×22.45 + 0.30×8.5 + 0.30×6.6 with sources | Present | PASS |

### 1.4 Single-credit and self-withdrawal guard

| Rule (4.5 / Amd 4) | Requirement | B11 | Verdict |
|---|---|---|---|
| Single-credit route stated | Recovery via Pillar 1; Strategic ROCE re-rating barred | "ROCE recovery credited via: Pillar 1"; Strategic route BARRED | PASS |
| Self-withdrawal (DECLINING backstop) stated | Withdrawn next quarter if recovery does not print / prob slips below band / catalyst dies | Dedicated guard-note section reproduces all three withdrawal triggers | PASS |
| Re-open keyed to evidence | DEEP WATCH re-open keys off ROCE reverting + cash turning, not a fixed trough price line | Stated in guard note and verdict card | PASS |
| Not the rejected premium-scaling | Corrects ROCE input; does not scale a premium or relax a cap | Cap 35x untouched; premiums +0x; Pillar 2 still 0.80x | PASS |

---

## PART 2 — STANDARD VALUATION-ADHERENCE AUDIT

| # | Rule (as written) | B11 | Re-derivation | Verdict |
|---|---|---|---|---|
| 1 | Pillar 2 multiplier matches determination: INDETERMINATE leaning structural → 0.80x | 0.80x, no offset | B10 cash INDETERMINATE leaning structural; 0.65x band needs rating confirmation (NOT FOUND) → not used | PASS |
| 2 | No growth offset on structural/unconfirmed drag | Offset 0 | Debtor days 48→86 through flat-revenue years → not growth-explained; offset correctly barred | PASS |
| 3 | Quality-Adjusted Base = A × B | 14.26 × 0.80 = 11.41x | 11.408 → 11.41x ✓ | PASS |
| 4 | Pillar 3a: +2x needs any two of four 📄 qualifiers | +0x | Only grade B qualifies (1 of 4): capex-embed NO, order book NO, SOM 14.3%<20% NO → +0x ✓ | PASS |
| 5 | Pillar 3b: EM-gated ≥25 | +0x | EM 19.2 < 25 → +0x ✓ | PASS |
| 6 | Pillar 3c: 📄 forward visibility ≥2.5yr | +0x | No documented order book/contracted tenor → +0x ✓ | PASS |
| 7 | Pillar 3 combined cap ≤ +6x | +0x | Within cap | PASS |
| 8 | Strategic Premium: single-credit route stated; scarcity gate | +0x; ROCE re-rating barred | No rare licence/monopoly of +4-6x class; moats MODERATE. Barred correctly | PASS |
| 9 | UA qualifiers: all three required | all_met false (1 of 3) | Listed≥12m YES; Gate0 48<60 & EM 19.2<25 NO; FII+DII≥3% NO → false ✓ | PASS |
| 10 | UA ordering (Amd 3): F2 = F×1.25 if qualified else F; H = min(F2, cap) | F2 = F = 11.41x; H = min(11.41, 35) = 11.4x | UA not applied; F2=F ✓ | PASS |
| 11 | Sector cap absolute | 35x, non-binding (11.41 << 35) | UA cannot breach; cap not reached | PASS |
| 12 | Both tracks carried through every FV and the verdict card | Track1 RRM + Track2 additive throughout | Pillar summary, Section 3, 4A-4E, verdict card all carry both ✓ | PASS |
| 13 | RRM = 1+(13.5−r)×0.12 percentage-point reading (Amd 4.4); r bound [9,18] | r=15, RRM=0.82 | 1+(−1.5)(0.12)=0.82 ✓; r within bound | PASS |
| 14 | Track 1 Destination PE = Base × RRM | 11.408 × 0.82 = 9.355 → 9.4x | 9.355x ✓ | PASS |
| 15 | Divergence >15% → conservative track governs entry | 22% → Track 1 (lower FV) governs | (11.408−9.355)/9.355 = 21.9% >15% ✓; Track 1 lower → governs ✓ | PASS |
| 16 | Amendment 6 range = value ±7.5%, nearest 0.5x, both tracks | T2 10.5-12.5; T1 8.5-10.0 | 11.408×[.925,1.075]=10.55-12.26→10.5-12.5 ✓; 9.355→8.65-10.06→8.5-10.0 ✓ | PASS |
| 17 | Two-tier hurdle (Amd 4.3): Tier B needs ALL gates; else Tier A 25% | Tier A, divisor 1.953 | Gate0 48/EM 19.2/promoter CAUTION/structural FLAG-CASH each fail Tier B → Tier A ✓ | PASS |
| 18 | Current PE = CMP / diluted EPS | 73.75x | 1326/17.98 = 73.75 ✓ | PASS |
| 19 | Credibility-grade gate on Bull (Amd 2 note): bull EPS usable only if grade A/B | Grade B → bull 34.5% used | B=Good → full bull permitted (not Base+5% cap) ✓ | PASS |
| 20 | Hurdle = (1+EPS CAGR)³ × (Dest PE mid ÷ Current PE) | Bull T1 0.309 / T2 0.376 | 2.4327×(9.355/73.75)=0.309 ✓; ×(11.408/73.75)=0.376 ✓; base 0.216/0.264 ✓ | PASS |
| 21 | HR verdict: HR(Bull)<1.953 → STOP; STOP does not halt run | STOP | 0.31/0.38 << 1.953 → STOP ✓ | PASS |
| 22 | 4D weights match grade: B → 25/50/25 | 25/50/25 | Applied ✓ | PASS |
| 23 | Prob-weighted expected CAGR | −39.8% (T1) | 0.25(−46.7)+0.50(−40.0)+0.25(−32.4) = −39.775 → −39.8 ✓ | PASS |
| 24 | Entry: Tier A divisor 1.953; MoS 20% below entry | Entry 147, MoS 118 | 287/1.953 = 146.9 → 147 ✓; 147×0.80 = 117.6 → 118 ✓ | PASS |
| 25 | SOM cross-check performed | base 14.3% = SOM 14.3% consistent; bull 25% flagged | Executed ✓ | PASS |
| 26 | Unresolved inputs handled by stated conservative rule, no silent fills | rating_wc_quote NOT FOUND → 0.80x no offset; peer medians NOT COMPUTED → not weighted | Both surfaced in input_gaps; no estimated fill ✓ | PASS |
| 27 | One-improvement-one-mechanism (no double-credit) | Dahej fed Pillar 1 via 4.5; Pillar 3a +0x; SHARED-CATALYST flagged for Role 3 | Because 3a=+0x, catalyst credited once (Pillar 1). No double-credit ✓ | PASS |

---

## PART 3 — ONE-IMPROVEMENT-ONE-MECHANISM DEEP CHECK (as requested)

The Dahej commissioning is (a) the mechanical unwind catalyst that lets 4.5 credit the normalized 22.45% into Pillar 1, and (b) the notional driver of a Pillar 3a growth-visibility premium. Double-credit risk: normalized ROCE lift **and** a +2x 3a premium off the same event.

- Pillar 3a scored **+0x** — only 1 of 4 qualifiers met (grade B); capex-embedded growth, order book, and SOM≥20% all failed on documented grounds. No premium paid on the catalyst.
- Strategic Premium ROCE re-rating route **barred** by single-credit (recovery is in Pillar 1).
- SHARED-CATALYST flag = TRUE, carried to Role 3 for single-point-of-failure stress.

The catalyst is credited exactly once (Pillar 1 via 4.5). **No double-credit. PASS.**

---

## PART 4 — FINDINGS

| Severity | Location | Issue | Effect |
|---|---|---|---|
| MINOR-1 | B11 Pillar 1 (14.26x) | Amendment 5 says "round the resulting base to one decimal"; the base 14.255 is carried as 14.26x rather than 14.3x. B11 explicitly acknowledges this in-text. | Using 14.3x: 14.3×0.80 = 11.44x vs 11.41x → +0.03x on raw destination PE; no change to range (10.5-12.5), Hurdle, entry, or decision. Presentational. |
| MINOR-2 | B10 normalized_roce block | B10 still displays the legacy pre-4.5 `pillar_1_roce_blend_pct: 7.36` (60/40) as "Pillar 1 ROCE Calculation." B11 correctly overrode it with the 4.5 three-anchor 13.51% and explicitly warned against the 7.36% figure. | Zero effect on the governing output. Stale legacy line in the input-assembly artifact only. |

No CRITICAL, no MAJOR. Neither finding moves the destination PE by ≥1x, flips the Hurdle verdict, or changes the decision.

---

## PART 5 — RECOMPUTED VALUE / DECISION

I concur with B11 on every load-bearing figure:
- Normalized 22.45%; 4.5 blend **13.51%**; Pillar 1 base **14.26x** (one-decimal 14.3x); quality-adjusted **11.41x**; Pillar 3 **+0x**; Strategic **+0x**; F = F2 = 11.41x; H = min(11.41, 35) = **11.4x additive / 9.4x RRM**.
- Divergence 22% → Track 1 governs; entry **Rs 118-147**; MoS **Rs 118**.
- Hurdle **STOP** (bull 0.31/0.38 << 1.953); expected 3yr CAGR **−39.8%**; decision **AVOID (on valuation)**.

Recomputed destination PE: **concur (no change).** Recomputed decision: **concur (AVOID).**

Amendment 4.5 was applied exactly as written: 📄-gated on both required evidences, capped at the evidenced pre-depression median, named unwind catalyst, correct 40/30/30 blend for the 40-60% RECOVERING band, single-credit routed to Pillar 1 with the Strategic ROCE route barred, and the self-withdrawal guard stated. The amendment lifts the destination PE and entry zone as designed without relaxing the cap, the cash multiplier, the premiums, or the Hurdle — CMP sits ~4.6x above even the lifted fair value, so the STOP and AVOID are undisturbed.

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
  rules_checked: 27
  fails: []
  minor:
    - "B11 base PE 14.255 carried as 14.26x instead of one-decimal 14.3x (Amd 5 rounding); acknowledged, +0.03x downstream, no decision impact"
    - "B10 still shows legacy pre-4.5 60/40 blend 7.36% as 'Pillar 1 ROCE Calculation'; B11 correctly overrode with 4.5 three-anchor 13.51%"
  confirmed:
    amd45_applies_only_temp_depressed_recovering: true
    normalized_roce_median_fy18_21: 22.45
    normalized_gated_both_evidences: "historical ROCE series 📄 + Dahej unwind catalyst 📄"
    normalized_capped_at_evidenced_median: true
    blend_40_30_30: "0.40x22.45 + 0.30x8.5 + 0.30x6.6 = 13.51%"
    continuous_formula: "0.5x13.51 + 7.5 = 14.26x (floor 9 / cap 24)"
    single_credit_route: "Pillar 1; Strategic ROCE re-rating barred"
    self_withdrawal_guard_stated: true
    pillar2_multiplier: "0.80x, no growth offset (INDETERMINATE leaning structural)"
    quality_adjusted_base: 11.41
    pillar3: "3a +0x (1 of 4) / 3b +0x (EM 19.2<25) / 3c +0x (no doc order book)"
    shared_catalyst_flagged_not_double_credited: true
    ua_applied: false
    ua_order_correct: "F2 = F (all_met false); H = min(F2, 35)"
    sector_cap_absolute: 35
    both_tracks_carried: true
    divergence_governing: "22% >15% -> Track 1 (conservative) governs entry"
    rrm: {r: 15, value: 0.82, reading: "percentage-point (Amd 4.4)"}
    destination_pe: {track2_additive_mid: 11.4, track1_rrm_mid: 9.4}
    hurdle_ratio: {tier: "A", threshold: 1.953, base_t1: 0.216, bull_t1: 0.309, base_t2: 0.264, bull_t2: 0.376, verdict: "STOP", bull_gate_grade_B: true}
    weights_4d: "25/50/25 (grade B)"
    som_crosscheck: "performed; base 14.3% = SOM 14.3% consistent"
    entry_math: "287/1.953=147; MoS 147x0.80=118"
    expected_cagr: -39.8
    no_silent_fills: true
    one_improvement_one_mechanism: true
recomputed_destination_pe: ""   # concur: 11.4x additive / 9.4x RRM
recomputed_decision: ""         # concur: AVOID (on valuation)
findings:
  - {severity: "MINOR", location: "B11 Pillar 1 base PE", claimed: "14.255 carried as 14.26x not one-decimal 14.3x (Amd 5)", note: "+0.03x downstream, no range/Hurdle/decision change; acknowledged in-text"}
  - {severity: "MINOR", location: "B10 normalized_roce.pillar_1_roce_blend_pct", claimed: "legacy pre-4.5 60/40 blend 7.36% still labelled 'Pillar 1 ROCE Calculation'", note: "B11 correctly overrode with 4.5 three-anchor 13.51%; no effect on governing output"}
critical_count: 0
major_count: 0
minor_count: 2
acceptance_rate: 100
```
