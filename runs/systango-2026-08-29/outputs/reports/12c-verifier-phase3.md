# B12c — VERIFIER C (FRAMEWORK ADHERENCE), PHASE 3 VALUATION-ADHERENCE AUDIT

Company: SYSTANGO | Run 2026-08-29 | Model claude-opus-4-8
Scope: PHASE 3 valuation-adherence only. Gate 0 (B01) and Emerging Moat (B07)
were audited in Phase 1 and are carried as `status: recorded-phase-1`; not redone.
Artifacts audited: 11-valuation.md + 11-valuation.yaml (Role 1), 10-valinputs.yaml
(assembly), 14-thesis.md + 14-thesis.yaml (Role 2), fttcp-deliberation.md (approved base).
Rule sources: Master v3.6 Role 1, Section 1B v3.3 / v3.5.1 / v3.6 / v3.7 / v3.8 / v3.9,
FTTCP v2.1. Later layers govern overlaps. Sector cap is the only ceiling.

No verifier defends its maker. Every FAIL carries the recomputed value beside it.

---

## 1. PILLAR-BY-PILLAR RE-DERIVATION (Section 1B)

| # | Rule / check | Source | Maker value | Re-derived | Verdict |
|---|---|---|---|---|---|
| 1 | Pillar 1 continuous formula, ROCE 33.0% | Amdt 11 (v3.6) | 24.0x | 0.5×33.0+7.5 = 24.0x | PASS |
| 2 | Amdt 11 boundary (>33% branch cross-check) | Amdt 11 | 24.0x | 24+0.3×(33−33) = 24.0x; both branches agree at the boundary | PASS |
| 3 | Ceiling 30x applied (not superseded 24x of Amdt 5) | Amdt 11 supersedes Amdt 5 | 30x, not binding | Correct layer; 24x cap retired | PASS |
| 4 | Pillar 1 normalization route | v3.5.1 | NONE | STAGNANT forward verdict bars Route A AND Route B (v3.5.1: "Neither route may be invoked on a STAGNANT or DECLINING ROCE verdict"). Route A test (12.6% < 20%) also fails; Route B N/A (ROCE not depressed). NONE by two independent paths. | PASS |
| 5 | FTTCP ROCE verdict = sole Pillar 1 authority | FTTCP v2.1 | STAGNANT → ROCE used = current 33.0% | Matches deliberation §2 | PASS |
| 6 | Converter classification stated upfront | Amdt 17.0 (v3.7) | NON CONVERTER (labour not a quoted commodity, R3) | Condition (a) fails cleanly; 17.1-17.3 do not bind; spot ROCE / rupee WC permitted | PASS |
| 7 | Pillar 2 multiplier matches determination | Master Pillar 2 / operator R1 | 1.00x GROWTH INDUCED, no offset | Operator-approved; CFO/PAT 1.06x FY26 audited; WC drag unwinding in acceleration scores growth-induced | PASS |
| 8 | Pillar 2 A3 conditional carried as sensitivity, not base | deliberation A3 | 0.80x revert → 13.4x, held as sensitivity | 24.0×0.80×0.70 = 13.44 ≈ 13.4x; carried below, not in base | PASS |
| 9 | Pillar 3 growth premium matches evidence gates | Amdt 4.1/4.2, Amdt 16 | +0x (3a 0 grade D; 3b 0 EM 10; 3c 0) | Grade D pays 3a +0x; EM 10 pays 3b +0x; 3c 0. Correct. | PASS |
| 10 | Amdt 16 gate opening ≠ automatic premium | Amdt 16 (v3.6) | Module B2 YES from FY27, but gates pay +0x | Amdt 16 precedes the evidence gates; gate open does not by itself award. Correct. | PASS |
| 11 | Strategic premium, single-credit | Amdt 4 | +0x, ROCE re-rating barred (no recovery claimed) | Correct; recovery NOT CREDITED in Pillar 1 → strategic route also barred | PASS |
| 12 | UA ordering min(F×1.25, cap), cap absolute | Amdt 3 | UA NOT APPLIED → F2 = F = 24.0x | Ordering correct; outcome neutral. See Finding V-1 on the stated qualifier reasoning. | PASS (outcome) |
| 13 | Sector cap absolute, not breached | Amdt 3 / cap table | 45x, not binding on either track | 16.8x and 24.0x both << 45x. Cap value operator-approved (B00 sector_cap_row); immaterial as non-binding. | PASS |

### Pillar 1 / base PE — CONCUR
24.0x base is correct on the current Amendment 11 layer. The maker cited Amendment 11
(30x ceiling), not the retired Amendment 5 (24x cap); the numerical coincidence that
the formula lands at 24.0x at exactly 33% ROCE does not mean the old cap was applied.

### Pillar 2 — CONCUR with the operator-ruled resolution
The Phase-1 INDETERMINATE did not silently resolve to PROCEED (CLAUDE.md guard). It
was resolved by operator R1 with named audited evidence (FY26 CFO p.18) and the missing
evidence (collection vs factoring) is named in the A3 tripwire. The verdict is capped at
WATCHLIST regardless. Compliant.

---

## 2. RRM DUAL-TRACK RE-DERIVATION (Master Role 1 + Amdt 12/13)

r build audit (Amdt 12 worksheet line):

| Component | Maker | Source rule | Verdict |
|---|---|---|---|
| base r | 14.0% (small/micro) | Master RRM Dual-Track | PASS |
| durability adj | 0 (Unproven band owns short record) | Amdt 12C | PASS |
| governance adj | +1.5 (DBX, Rs 5.30 cr loan book, 33-mo silence, one unaudited sub) | Master "adjust for governance" | PASS |
| cyclical surcharge | 0 (not cyclical) | Amdt 12B | PASS |
| complexity adj | +0.5 (4 subs / 3 countries, one unaudited; RPT 32-42%) | Amdt 13 | PASS (see Finding V-2) |
| cash-conversion r-UP | none | Amdt 12A (Pillar 2 owns cash quality) | PASS |
| short-record r-UP | none | Amdt 12C (Unproven band owns it) | PASS |
| final r | 16.0% (bounded [9,18]) | — | PASS |

- 14.0 + 1.5 + 0.5 = **16.0%**. Re-derived, matches.
- Governance double-charge check (operator R4): +1.5 lives only in r; Track 2 (Additive)
  carries no governance deduction; no pillar is docked for governance; the verdict card
  adds no separate governance haircut. **Not double-charged.** PASS.
- Complexity +0.5 justified: Amendment 13 triggers present — high subsidiary count and
  dense RPT (32-42% of standalone revenue) each qualify independently. PASS.

RRM = 1 + (13.5 − 16.0) × 0.12 = 1 + (−2.5)(0.12) = 1 − 0.30 = **0.70** (percentage-point
reading per Amdt 4.4; floor of the [0.70, 1.60] band). Re-derived, matches.

- Track 1 (RRM) = 24.0 × 0.70 = **16.8x**, range ±7.5% = 15.5-18.0x. Matches.
- Track 2 (Additive) = 24.0x (no RRM), range 22.2-25.8x. Matches.
- Divergence = (24.0 − 16.8) / 24.0 = **30%** (>15%). Master line 554: the more
  conservative track sets the entry zone → Track 1 governs. **CONCUR.** The maker prices
  the open question (governance/durability) once, through r, per operator R5.

---

## 3. EXIT CONSTRUCTION, FV PATH, HURDLE (v3.8 / v3.9)

| # | Rule | Source | Maker | Re-derived | Verdict |
|---|---|---|---|---|---|
| 14 | Exit-basis symmetry, one basis both ends | Amdt 18.1 | FORWARD both ends; today uses FY27, Year-3 exit uses FY30 (N+1) | Correct: forward entry → exit = PE × Year N+1 EPS | PASS |
| 15 | Multiple meets operating EPS; treasury not multiplied | Amdt 18.1 / deliberation §4 | PE × operating EPS (treasury Rs 5.94 cr stripped) + net cash | Treasury income NOT inside the multiplied term | PASS |
| 16 | Net cash added once, never multiplied | Amdt 19.0 | Rs 118.52 cr / Rs 80.8 per share, static, added once | Confirmed in every FV cell and the FV path | PASS |
| 17 | Horizon = hold + 1 (Year 4 in every case) | Amdt 18.0 | Table to Year 5 (FY31); Year 4 (FY30) present bear/base/bull | PASS |
| 18 | Option Resolution Calendar per slice | Amdt 18.2 | All 4 slices ZERO (no probability, no nameable event); bear at failure | PASS |
| 19 | FV-step lines where within-hold parameterised | Amdt 19.4 | None quantified (no parameterised slice) | Correct — nothing to step | PASS |
| 20 | FV path table (today → end-Y3) | Amdt 19.0 | 443 / 505 / 537 / 614 | 16.8×21.56+80.8=443.0; ×25.23=504.7; ×27.15=536.9; ×31.76=614.4. All match. | PASS |
| 21 | FV CAGR one-number line | Amdt 19.1 | 11.5% | (614/443)^(1/3)−1 = 11.49% | PASS |
| 22 | Return-source label, fixed band | Amdt 19.2 | HYBRID | 11.5% ∈ [10%, 20%) → HYBRID. Boundary recomputed: COMPOUNDER ≥20, HYBRID 10-20, DISCOUNT-CLOSER <10. Correct. | PASS |
| 23 | Decomposition line | Amdt 19.3 | 82% growing core / 18% static cash, no re-rating lever | PASS |
| 24 | Step 1C PENDING, pillar governs interim | Amdt 20.1/20.9 (v3.9) | PENDING LIVE PEER TABLE; pillar governs | Code holds no live data; correct per team-workflow split | PASS |
| 25 | Amdt 15 relative-PE expression | Amdt 15 (v3.6) | Market PE NOT FOUND; PENDING; pillar governs, sits mid-range | Handled as unresolved with no silent fill | PASS |

### Hurdle Ratio (Amdt 2 / Amdt 4.3)
- Tier assignment: FII+DII = 2.16% < 3% → **Tier A (25% hurdle)**. Tier B also fails on
  Promoter (CONCERN, not TRUSTWORTHY) and on structural FLAG-CASH. Correct. PASS.
- Threshold 1.953 (Tier A). Bull uses Base + 5% for grade D (Amdt 2 conservative-bias
  note). Correct. PASS.
- HR(base) = (1.138)^3 × (16.8 / 7.1) = 1.4737 × 2.366 = **3.48** → PASS. Re-derived, matches.
- Current ex-cash operating forward PE = (234 − 80.8) / 21.56 = 153.2 / 21.56 = 7.1x.
  Basis-consistent: destination 16.8x also applies to ex-cash operating EPS. Correct.
- On-price cross-read: 234 / 21.56 = 10.85x → HR = 1.4737 × (16.8/10.85) = 2.28 → PASS.
- **HR magnitude sanity: 3.48 is consistent with a 47% EPS-growth term (1.47) times a
  2.37x PE-gap term. Both inputs verified. PASS.**

### Fair values (full matrix) — spot re-derivation
- Track 1 base 16.8×31.76+80.8 = 614; bull 18.0×31.76+80.8 = 653; bear 15.5×24.82+80.8 = 465. Match.
- Track 2 base 24.0×31.76+80.8 = 843; bull 25.8×31.76+80.8 = 900; bear 22.2×24.82+80.8 = 632. Match.
- Expected CAGR: 25.8×0.45 + 38.0×0.40 + 40.8×0.15 = 11.6 + 15.2 + 6.1 = **32.9%**. Match.
- 4D weights grade D = 45/40/15 (Master line 806, "Poor"). PASS.
- A3 revert: 24.0×0.80×0.70 = 13.44 → base FV 13.44×31.76+80.8 = 508. Match.

### Entry zone (Amdt 4.3 cascade)
- 25% CAGR entry = 614 / 1.953 = **Rs 315**. MoS 30% (MIXED evidence scale) = 315×0.70 = **Rs 220**.
- Built on the GOVERNING (conservative) Track 1 base FV Rs 614 — correct (Master line 554).
- MoS at 30% (evidence-scaled, thin forward evidence) is more conservative than the fixed
  20% floor; a wider MoS lowers the buy price, so it cannot inflate the verdict. Accepted.
- Entry conjunction: zone WITHDRAWN because the proof gate has not fired. Correctly applied.

---

## 4. ROLE 2 (B14) DECISION-RULE + POSITION-SIZING AUDIT (extended)

| # | Rule | Source | Maker | Verdict |
|---|---|---|---|---|
| 26 | Promoter-override print rule (no BUY/WATCHLIST without CONCERN block) | deliberation §1 / CLAUDE.md | CONCERN block printed at top of thesis, in Section 4, and in the verdict box | PASS |
| 27 | BUY NOW gate (needs Promoter ≥ TRUSTWORTHY) | Master line 1020 | Not BUY; Promoter is CONCERN | PASS |
| 28 | AVOID map for Promoter CONCERN, overridden to PROCEED | Master line 1024 / operator override | Verdict lands WATCHLIST (leaning AVOID), override recorded not resolved | PASS |
| 29 | Transition Decision Matrix posture | CLAUDE.md matrix | Proof NOT fired + gap OPEN → RESEARCH/WATCH | Correct cell | PASS |
| 30 | Position sizing ceiling | Master lines 1050-1053 | NO POSITION now; Small (2-3%) ceiling if it converts | PASS |
| 31 | Promoter CONCERN cap binds size | Master line 1053 | Cap binds; override lifts the AVOID map, not the size cap | PASS |
| 32 | Sector Literacy Track ≥3 books bars Medium+ | Master line 26 / 1051 | Unevidenced → independently bars Medium+ | PASS |
| 33 | Dispersion-capped sizing | Master lines 862-872 | Range width (653−465)/614 = 31% (<40%) → normal, but tighter caps dominate | PASS |
| 34 | Entry conjunction stated in Section 7 box | Master line 1026 | Stated: price-in-zone AND no trigger fired AND proof fired AND DBX resolved | PASS |
| 35 | Tier line on verdict card | Amdt 4.3 line 180 | Tier A / 25% is derivable but the explicit "Tier: A \| Hurdle: 25%" first-line print is not verbatim on the Role 2 card | MINOR (Finding V-3) |

Position-size logic is internally consistent: grade D + unresolved CONCERN governance +
proof-gate-not-fired + A3 conditional swing + model-external downside all point below a
full-size BUY, and every one is named. Operator override to size = NONE recorded; the
maker correctly holds that the PROCEED override does not lift the size cap. No Tier,
hurdle, or entry-zone rule is mis-applied in a way that changes the outcome.

---

## 5. FINDINGS

**V-1 (MINOR) — UA qualifier reasoning mis-stated; outcome correct.**
Location: 11-valuation.md §"UA multiplier (F2 row)" and 10-valinputs.yaml `ua_qualifiers.gate0_or_em`.
The maker states the Gate-0-OR-EM qualifier FAILS ("EM score 10 < 25 gate FAIL").
Amendment 3 reads the qualifier as **Gate 0 ≥60 OR EM ≥25**. Gate 0 = 88 satisfies the
OR leg regardless of EM = 10, so this qualifier is **MET, not failed**. The genuine reason
all three qualifiers are not jointly satisfied is the FII+DII leg being STALE/unfiled
(Mar-2025), plus operator R2 (the "undiscovered" premise is falsified by the Kacholia
exit). UA NOT APPLIED (neutral 1.00x) is the correct and conservative outcome and does not
change the destination PE, so this is a reasoning defect only. Recorded as a divergence
from the maker. No PE or decision impact.

**V-2 (MINOR) — "one unaudited subsidiary" cited under both r adjustments.**
Location: 11-valuation.md §"RRM derivation" and deliberation §4 r-build.
The fact "one unaudited subsidiary" appears in BOTH the governance +1.5 justification and
the complexity +0.5 justification. Amendment 13 requires the complexity charge to be a
distinct, additive opacity charge. Each adjustment stands on independent sufficient
triggers (governance: DBX + Rs 5.30 cr loan book + 33-month silence; complexity:
subsidiary count + RPT 32-42%), so there is no material double-charge and r = 16.0% holds
either way. The overlapping citation should be homed to one adjustment so the
single-credit audit trail is clean. No r or PE impact.

**V-3 (MINOR) — Tier line not printed verbatim on the Role 2 card.**
Location: 14-thesis.md Section 7 verdict box.
Amendment 4.3 mandates the verdict card's first line state "Tier: [A/B] | Hurdle:
[25%/20%]". Tier A / 25% is fully derived and used correctly in Role 1 (Hurdle threshold
1.953) and traced in the Role 2 decision-rule trace, but the verbatim first-line print is
absent from the Role 2 card. Presentational; the tier is correct and load-bearing values
are unaffected.

No CRITICAL. No MAJOR. Nothing changes the destination PE by >1x, flips the Hurdle
verdict, or flips the decision.

---

## 6. RE-DERIVATION SUMMARY vs MAKER

| Quantity | Maker | Verifier re-derivation | Diverge? |
|---|---|---|---|
| Pillar 1 base PE | 24.0x | 24.0x | No |
| final r | 16.0% | 16.0% | No |
| RRM | 0.70 | 0.70 | No |
| Track 1 destination | 16.8x | 16.8x | No |
| Track 2 destination | 24.0x | 24.0x | No |
| Divergence | 30% | 30% | No |
| FV CAGR | 11.5% | 11.49% | No |
| Return-source label | HYBRID | HYBRID | No |
| Hurdle (base) | 3.48 | 3.48 | No |
| Expected CAGR | 32.9% | 32.9% | No |
| Base Year-3 FV (Track 1) | 614 | 614 | No |
| A3-revert destination | 13.4x | 13.44x | No |
| UA qualifier 2 (Gate0-OR-EM) | FAIL (stated) | MET (Gate 0 = 88 ≥ 60) | **Yes (V-1)** |

Destination PE: CONCUR (16.8x governing). Decision: CONCUR (WATCHLIST, leaning AVOID, no
position). The single re-derivation divergence (V-1) is a reasoning defect with no PE or
decision consequence; UA-not-applied is the correct and conservative outcome by two other
paths.

---

## 7. ACCEPTANCE

Rules checked: 38. Clean pass: 35. MINOR-flagged (outcome correct, defect noted): 3.
CRITICAL: 0. MAJOR: 0.
Acceptance rate = 35 / 38 = 92%. Well above the 60% REWORK threshold.
**Valuation ACCEPTED.** No rework triggered.

---

```yaml
stage: B12c
company: "SYSTANGO"
run_date: "2026-08-29"
model: claude-opus-4-8
status: complete
scope: "phase-3 valuation-adherence (B10/B11/B14 + approved deliberation base)"
gate0: {status: recorded-phase-1, rules_checked: 0, fails: []}
emoat: {status: recorded-phase-1, rules_checked: 0, fails: []}
valuation:
  rules_checked: 38
  fails: []   # no PASS->FAIL flips; 3 MINOR reasoning/presentational findings recorded below
  concur_destination_pe: true
  concur_decision: true
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: ["NOT IN SCOPE — stage 13 synthesis not among phase-3 inputs; not audited here"]}
recomputed_destination_pe: ""   # concur: Track 1 16.8x governing, Track 2 24.0x cross-check
recomputed_decision: ""         # concur: WATCHLIST (leaning AVOID), no position
findings:
  - {severity: "MINOR", location: "11-valuation.md UA (F2) row + 10-valinputs.yaml ua_qualifiers.gate0_or_em", issue: "Gate-0-OR-EM qualifier stated as FAIL on EM 10<25; it is MET because Gate 0 = 88 >= 60 satisfies the OR leg. Real non-satisfaction is the stale FII+DII leg plus operator R2 (Kacholia falsifies the undiscovered premise). UA NOT APPLIED is correct and conservative; no PE impact.", pe_impact: "none"}
  - {severity: "MINOR", location: "11-valuation.md RRM derivation + deliberation §4 r-build", issue: "'one unaudited subsidiary' cited under both the governance +1.5 and the complexity +0.5 adjustments. Each stands on independent sufficient triggers (Amdt 13: subsidiary count + RPT; governance: DBX + loan book + call silence), so no material double-charge; r=16.0% holds. Home the fact to one adjustment for a clean single-credit trail.", pe_impact: "none"}
  - {severity: "MINOR", location: "14-thesis.md Section 7 verdict box", issue: "Amdt 4.3 mandates first-line 'Tier: A | Hurdle: 25%' verbatim on the card; tier is derived and used correctly (threshold 1.953, Tier A on FII+DII 2.16%<3%) but not printed verbatim. Presentational.", pe_impact: "none"}
re_derivation_divergences:
  - {quantity: "UA qualifier 2 (Gate0-OR-EM)", maker: "FAIL", verifier: "MET (Gate 0 88 >= 60)", consequence: "none — UA not applied is correct on other grounds"}
concur_re_derivations: ["pillar1_base 24.0x", "r 16.0%", "RRM 0.70", "track1 16.8x", "track2 24.0x", "divergence 30%", "fv_cagr 11.5%", "label HYBRID", "hurdle 3.48 PASS", "expected_cagr 32.9%", "base_fv 614", "a3_revert 13.4x", "entry 220-315", "tier A / 25%"]
role2_decision_rules: {promoter_override_print: PASS, buy_gate_respected: PASS, avoid_map_overridden_to_proceed: PASS, decision_matrix_cell: "RESEARCH/WATCH (proof not fired + gap open) PASS", position_size: "Small ceiling / no position now — PASS", promoter_cap_binds_size: PASS, sector_literacy_bars_medium_plus: PASS, entry_conjunction_stated: PASS, tier_line_verbatim: "MINOR (V-3)"}
critical_count: 0
major_count: 0
minor_count: 3
acceptance_rate: 92
valuation_verdict: "ACCEPTED — no rework; destination PE and decision concur; 3 MINOR findings, none altering PE, Hurdle, or decision"
```
