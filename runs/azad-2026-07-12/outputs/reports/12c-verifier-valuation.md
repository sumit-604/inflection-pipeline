# B12c — VERIFIER C: FRAMEWORK ADHERENCE (PHASE 3, VALUATION HALF)

**Company:** AZAD (Azad Engineering Ltd) | **Run date:** 2026-07-12 | **Model:** claude-opus-4-8
**Scope:** Valuation (B11) + Role 2 decision rules and position sizing (B14), audited against Master v3.3 / Section 1B v3.3 (+v3.4 4.1-4.4) / FTTCP v1.2 AS WRITTEN.
**Not in scope this pass:** Gate 0 (B01) and Emerging Moat (B07) — cleared in phase 1 (47+36 rules, 0 fails, 100%). Not re-audited.
**Inputs audited:** `10-valinputs.md` (B10), `11-valuation.md` (B11), `14-thesis.md` (B14).
**Rule authority:** `Master_Project_Prompt_v3.3.md`, `Section_1B_v3.3_Amendments.md`, `FTTCP_v1.2_Consolidated.md`.

Verifier C audits rule APPLICATION, not raw source numbers (Verifier A owns numbers) and not company quality. Operator/FTTCP deliberation overrides carried in B10 (operational ROCE basis, +3x strategic, 25x cap, cash 0.90x, RECOVERING verdict) are treated as authoritative injected inputs; I audit only that B11 applied them per the framework's mechanics.

---

## PART 1 — SECTION 1B FOUR-PILLAR (B11) RULE-BY-RULE

### Pillar 1 — ROCE Base (continuous formula)

| # | Rule (source) | Applied in B11 | Verdict |
|---|---|---|---|
| V1 | Continuous formula 0.5×ROCE+7.5, floor 9x, cap 24x (Amd 5; Master L211) | 0.5×13.6+7.5 = 14.3x, within band | PASS |
| V2 | FTTCP ROCE verdict is SOLE Pillar-1 authority (Master L218) | RECOVERING (40-60%) taken from B10/FTTCP; no ad hoc trajectory judgment | PASS |
| V3 | RECOVERING (40-60%) → 60/40 wtd avg of current + FY[Y+2] (Master L224) | 0.6×12.0 + 0.4×16.0 = 13.6% | PASS |
| V4 | ROCE basis = operational per override (B10 override 1), not statutory 8.84 / mgmt 20.7 | Operational 12.0% current; 16.0% FY[Y+2]; both conflicting values recorded, not used | PASS |
| V5 | Base PE arithmetic and one-decimal rounding (Amd 5) | 14.3x | PASS |

Note (MINOR, not a fail): FY[Y+2] operational ROCE 16.0% is back-solved from B10's "blended forward ~13.6%" and the 60/40 weight (0.4X = 13.6 − 7.2 → X = 16.0). B11 labels it "implied … not independently disclosed" in `unresolved_inputs_used`. Transparent, no silent fill. Rule application correct.

### Pillar 1 / Strategic — Single-credit rule

| # | Rule (source) | Applied in B11 | Verdict |
|---|---|---|---|
| V6 | ROCE recovery credited Pillar 1 OR Strategic, never both; default Pillar 1 (Amd 4; Master L228) | "ROCE recovery credited via: Pillar 1" stated explicitly | PASS |
| V7 | Strategic Premium must NOT re-credit ROCE re-rating (Amd 4) | +3x explicitly credits franchise/pricing power, not ROCE; stated | PASS |
| V8 | Shared-catalyst permitted but must be flagged (Amd 4; Master L307) | SHARED CATALYST flagged (serial-production ramp drives Pillar 1 ROCE + Pillar 3); handed to Role 3 | PASS |
| V9 | One-improvement-one-mechanism; cash risk not double-policed in r (Master L78) | Cash risk kept in Pillar 2 only, explicitly NOT added to RRM r | PASS |

### Pillar 2 — Cash Conversion Multiplier

| # | Rule (source) | Applied in B11 | Verdict |
|---|---|---|---|
| V10 | Band "CFO/PAT <30% or CFO negative" → 0.80x base (Master L247) | CFO/PAT −0.93 / cum 0.04, FCF neg → 0.80x | PASS |
| V11 | Structural vs growth-induced test; structural → 0.65x, NO offset (Master L250-266) | GROWTH-INDUCED per B10/FTTCP ruling 7 (WC build QIP-funded; CARE normalization statement); NOT 0.65x structural | PASS |
| V12 | Growth offset by PAT/Rev CAGR band; 25-40% → +0.10 (Master L261) | PAT CAGR 35.78% → +0.10 | PASS |
| V13 | Effective multiplier and Quality-Adjusted Base (Master L275-276) | 0.80+0.10 = 0.90x; 14.3×0.90 = 12.87x | PASS |
| V14 | No offset applied to a structural determination (Amd 7; Appendix A) | Offset applied only because determination is growth-induced; 0.80x floor carried until Q1 FY27 print | PASS |

### Pillar 3 — Decoupled 3a/3b/3c (v3.4 4.1-4.2)

| # | Rule (source) | Applied in B11 | Verdict |
|---|---|---|---|
| V15 | 3a: +3x if ≥3 qualify AND grade A/B; 📄 only (Amd 4.1) | Order book ~11x, SOM 31% w/ capacity check, grade B → 3 qualify + grade B → +3x | PASS |
| V16 | 3b: EM-gated table, EM 25-29 any timeline → +1x (Master L304; Amd 4.1) | EM 26 → +1x | PASS |
| V17 | 3c: ≥4yr documented visibility → +2x; 📄 only (Amd 4.2) | Order book ~11x rev, CARE 5-6yr visibility (LTAs 4-8yr) → +2x | PASS |
| V18 | Combined 3a+3b+3c hard cap +6x (Amd 4.1/4.2) | 3+1+2 = +6x, at cap | PASS |

Note (MINOR, not a fail): 3a did not explicitly evaluate the "capex-embedded growth ≥15%" qualifier. Immaterial: order book + SOM + grade already reach the ≥3 threshold, and capex-embedded growth (570.71 Cr capex on 590.38 Cr revenue) would almost certainly qualify too, so +3x is robust under either reading of whether the grade line counts inside the qualifier tally. B11 also stress-notes that even +4x total Pillar 3 leaves the Hurdle verdict unchanged.

### Strategic Premium / UA / Sector Cap

| # | Rule (source) | Applied in B11 | Verdict |
|---|---|---|---|
| V19 | Strategic tier "strong franchise/limited comp/pricing power" = +2 to +4x (Master L320) | +3x, mid-tier; explicitly NOT the +4-6x rare-licence tier (justified) | PASS |
| V20 | UA all-three qualifiers; here FII+DII ~22% >3% → all_met false → no UA (Amd 3; Master L332) | UA not applied; F2 = F (×1.0) | PASS |
| V21 | UA ordering min(F×1.25, Cap); cap absolute (Amd 3; Master L205/334) | Ordering shown; UA n/a so H = min(F, G) | PASS |
| V22 | Sector cap absolute, precision-eng/industrial = 25x (Amd 8; Master L355) | 25x applied; min(21.87, 25) = 21.87x; cap not binding | PASS |
| V23 | Raw Destination PE = (ROCE Base × Cash Mult) + Growth + Strategic (Master L203) | 12.87 + 6.0 + 3.0 = 21.87x | PASS |

### RRM dual-track / range / divergence

| # | Rule (source) | Applied in B11 | Verdict |
|---|---|---|---|
| V24 | Both tracks (RRM + additive) produced (Master L390) | Track 2 additive 21.87x; Track 1 RRM 20.56x | PASS |
| V25 | RRM base r: mid 13% (16,013 Cr mcap) + durability/governance adj, bound [9,18] (Master L392) | 13% base +0.75 gov +0.25 dur = 14.0% | PASS |
| V26 | RRM = 1+(13.5−r)×0.12, percentage-point units, bounds 0.70-1.60 (Amd 4.4) | 1+(13.5−14.0)×0.12 = 0.94 | PASS |
| V27 | Track 1 destination = Fundamental Base × RRM, capped (Master L392) | 21.87×0.94 = 20.56x, <25x cap | PASS |
| V28 | Destination PE range = ±7.5%, nearest 0.5x (Amd 6) | T2 20.0-23.5x; T1 19.0-22.0x | PASS |
| V29 | Divergence stated; conservative track sets entry zone (Master L394/599) | 6.0% (<15%); Track 1 (conservative) governs entry | PASS |
| V30 | Both tracks carried through fair values and verdict card (Master L390/599) | 4A shows both; verdict card shows both; entry from Track 1 | PASS |

### Hurdle Ratio / two-tier / 4D

| # | Rule (source) | Applied in B11 | Verdict |
|---|---|---|---|
| V31 | HR = (1+EPS CAGR)³ × (Dest PE mid ÷ Current PE) (Master L398; Amd 2) | 1.876 × (20.6/121.21) = 0.32 base; 2.259 × 0.16995 = 0.38 bull | PASS |
| V32 | Tier assignment: Tier A via TURNAROUND (Amd 4.3) | Tier A, threshold 1.953; verdict card line 1 "Tier: A | Hurdle: 25%" | PASS |
| V33 | Bull row usable only if credibility grade A/B (Master L406; Amd 2) | Grade B → bull row used | PASS |
| V34 | HR(Bull) < 1.953 → STOP (Master L404; Amd 2) | 0.38 << 1.953 → STOP | PASS |
| V35 | 4D probability weights match grade: Good = 25/50/25 (Master L629) | 25/50/25 applied; Expected CAGR −34.3% | PASS |
| V36 | "Would I pay this destination PE?" validation asked (Master L408) | Yes at ~21x; problem is 121x entry — stated | PASS |

### Unresolved-input discipline / SOM

| # | Rule (source) | Applied in B11 | Verdict |
|---|---|---|---|
| V37 | Every B10.unresolved handled by a stated conservative rule; no silent fill (CLAUDE.md; Master input discipline) | Peer multiples NOT fabricated; Y3 net debt conservative ~500/550/450; diluted shares 6.46 approximated; FY[Y+2] 16% flagged implied | PASS |
| V38 | SOM cross-check performed (Master 2D / Amd 4.1 capacity cross-check) | Base 26% vs SOM 31% → below SOM, consistent; capacity +126 Cr spare 3yr | PASS |
| V39 | Entry price = Base FV ÷ 1.953 (Tier A); MoS 20% below (Amd 4.3) | 719.50/1.953 = 368.4; ×0.8 = 294.7 → zone ~295-368 | PASS |
| V40 | 4G four-pillar validation table completed incl UA ordering + single-credit re-check (Master L656) | All six 4G checks present and consistent | PASS |

---

## PART 2 — ROLE 2 DECISION RULES & POSITION SIZING (B14)

| # | Rule (source) | Applied in B14 | Verdict |
|---|---|---|---|
| V41 | AVOID if Gate0 AVERAGE/AVOID OR Promoter CONCERN/AVOID OR U/D <2x OR Hurdle STOP (Master L809) | Three AVOID triggers fire: Gate 0 AVOID, U/D 0x, Hurdle STOP → AVOID | PASS |
| V42 | Hardest verdict wins on unresolved contradiction (Master L760) | AVOID chosen over strong forward case | PASS |
| V43 | Entry conjunction (anti-value-trap) stated in Section 7 box (Master L811) | Explicit: price in zone AND checklist clean; zone withdrawn if triggered by the falsifier print | PASS |
| V44 | Large needs Gate0 EXCELLENT + Promoter EXEMPLARY/TRUSTWORTHY + EM EXPANSION + CMP<MoS (Master L815) | Fails (Gate0 AVOID, Promoter CAUTION, EM STRENGTHENING) → not Large | PASS |
| V45 | Medium needs Gate0 GOOD+ or Promoter TRUSTWORTHY + CMP≤Entry (Master L816) | Fails (Gate0 AVOID, Promoter CAUTION) → not Medium | PASS |
| V46 | Small = everything else that qualifies as BUY (Master L817) | Small (2-3%) selected, in-zone starter only | PASS |
| V47 | Promoter verdict cap binds downward (Master L818) | CAUTION cap binds to Small; stated | PASS |
| V48 | Position-size override only if operator documents it (Amd 4.3; Master L818) | No override recorded; the two recorded overrides (ROCE basis, Strategic) noted; not misused as sizing override | PASS |
| V49 | Tier A sizing consistent (no Tier-B Medium ceiling misapplied) (Amd 4.3) | Tier A; Small ceiling from quality gates, not Tier-B rule | PASS |
| V50 | Verdict card / thesis first-line Tier+Hurdle carried into thesis (Amd 4.3) | Snapshot and valuation summary carry Tier A / Hurdle STOP consistently | PASS |

---

## RECONCILIATION OF DESTINATION PE AND DECISION

- Recomputed Raw Destination PE (Track 2): 12.87 + 6.0 + 3.0 = **21.87x** — matches B11.
- Recomputed Track 1 (RRM): 21.87 × 0.94 = **20.56x → 20.6x mid** — matches B11.
- Recomputed Hurdle: HR(Bull) 0.38 << 1.953 → **STOP** — matches B11.
- Recomputed decision: Gate 0 AVOID + U/D 0x + Hurdle STOP → **AVOID** — matches B14.
- Position size: quality gates fail Large and Medium; CAUTION cap binds → **Small (Tier A)** — matches B14.

I concur on destination PE (both tracks), the Hurdle verdict, the decision, and the position size. No misapplication changes destination PE by >1x, flips the Hurdle verdict, or flips the decision. Sensitivity noted: even a −2x haircut to Pillar 3 (to +4x) leaves destination ~19.9x and the STOP/AVOID intact (B11 states this), so no rule interpretation in play is decision-material.

**No CRITICAL. No MAJOR. Two MINOR observations** (both non-fails; rule application correct):
1. 3a omitted an explicit read on the "capex-embedded growth ≥15%" qualifier (immaterial to the +3x, which is over-satisfied).
2. FY[Y+2] operational ROCE 16.0% is back-solved from B10's blended 13.6%; transparently flagged as implied, not silently filled.

**Rules checked: 50. Passed: 50. Acceptance rate: 100%.**

---

```yaml
stage: B12c
company: "AZAD"
run_date: "2026-07-12"
model: claude-opus-4-8
status: complete
gate0: {rules_checked: 0, fails: []}   # phase 1, not re-audited (passed 47/47)
emoat: {rules_checked: 0, fails: []}   # phase 1, not re-audited (passed 36/36)
valuation:
  rules_checked: 50
  fails: []
recomputed_destination_pe: ""   # concur: Track2 21.87x / Track1 20.6x
recomputed_decision: ""          # concur: AVOID (on valuation), Small, Tier A
findings:
  - {severity: MINOR, location: "B11 Pillar 3 / 3a", note: "capex-embedded growth >=15% qualifier not explicitly evaluated; immaterial, +3x already over-satisfied by order book + SOM + grade B; rule application correct"}
  - {severity: MINOR, location: "B11 Pillar 1 / unresolved_inputs_used", note: "FY[Y+2] operational ROCE 16.0% back-solved from B10 blended 13.6% via 60/40 weight; flagged as implied, not silently filled; conservative-rule discipline honored"}
critical_count: 0
major_count: 0
minor_count: 2
acceptance_rate: 100
```
