# STAGE 12C (PHASE 3): VERIFIER C — VALUATION FRAMEWORK ADHERENCE
## Fedbank Financial Services Ltd (FEDFINA)
**Run Date:** 2026-07-15 | **Report Date:** 2026-07-16
**Model:** claude-opus-4-8 | **Scope (phase 3):** B11 valuation + B10 assembly against Section 1B v3.3 Four-Pillar Framework (lender carve-outs), EXTENDED to B14 Role 2 decision rules and position sizing against Master v3.3 Role 2.
**Fresh context.** Phase-1 Gate 0 + Emerging Moat findings already recorded and NOT redone here.

Framework authorities read at audit time: Master_Project_Prompt_v3.3.md (Role 1 Pillar tables, RRM Dual-Track, Role 2 decision + sizing rules), Section_1B_v3.3_Amendments.md (Amendments 1-8, 4.1-4.5), Section_1B_v3_5_1_Reconciliation.md (consolidated Amendment 9), FTTCP_v1.2_Consolidated.md (Pillar 1 forward-verdict table, single-credit).

Method: I re-derived every pillar, the RRM track, the Hurdle Ratio, projections, triangulation, entry/MoS, and the Role 2 decision/sizing logic from the stated inputs and thresholds. I audit rule application, not raw source numbers (Verifier A owns numbers) and not company quality.

---

## A. PILLAR-BY-PILLAR COMPLIANCE (B11, Section 1B lender carve-out)

### Pillar 1 — ROE Base Multiple (Amendment 7 lender substitution)

| # | Rule | Recompute | PASS/FAIL |
|---|---|---|---|
| P1.1 | ROE used, not ROCE (Amendment 7 lender carve-out) | ROE basis throughout; ROCE marked NOT FOUND / non-computable | PASS |
| P1.2 | FTTCP forward verdict is sole Pillar 1 authority | RECOVERING 40-60% taken from fttcp-deliberation; no standalone trajectory rule | PASS |
| P1.3 | RECOVERING 40-60% → 60/40 weighted avg of current & FY[Y+2] (FTTCP v1.2 Pillar 1 table) | 0.60×12.6 + 0.40×15.0 = 7.56 + 6.00 = 13.56% | PASS |
| P1.4 | Continuous formula 0.5×ROE + 7.5, floor 9x cap 24x (Amendment 5) | 0.5×13.56 + 7.5 = 14.28 → 14.3x; inside [9,24] | PASS |
| P1.5 | Amendment 9 Route B (pre-cycle normalized ROE) gate | FY-wise pre-depression ROE series NOT FOUND → 📄 gate fails → route NONE; standard blend stands | PASS |
| P1.6 | Amendment 9 Route A (operational ROCE) applicability | N/A (lender; CWIP/idle-capital denominator test inapplicable) — correctly NONE | PASS |
| P1.7 | Single-credit: recovery credited via Pillar 1, Strategic re-rating barred | Worksheet states "credited via Pillar 1"; Strategic ROE re-rating route barred | PASS |

Pillar 1 base multiple arithmetic and the 60/40 RECOVERING blend of current 12.6% and the stage-set FY[Y+2] 15.0% are correct exactly as the task specifies.

### Pillar 2L — Asset-Quality Multiplier (Amendment 7)

| # | Rule | Recompute | PASS/FAIL |
|---|---|---|---|
| P2.1 | Asset-Quality Multiplier used, NOT the cash-conversion multiplier | Pillar 2L applied; cash multiplier explicitly replaced | PASS |
| P2.2 | Mechanical band read stated before override | GNPA 1.87% (<2%) but PCR 32-38% (<60%) → draft mechanical 0.80x (Stressed) correctly identified | PASS |
| P2.3 | 1.00x carried as operator override (not re-litigated at stage 11) | 1.00x from fttcp-deliberation override 2 / B10 authoritative overlay, applied as given | PASS |
| P2.4 | Self-withdraw condition carried | Reverts to 0.80x if Q4 FY26 credit cost >1.1% or PCR thins; FLAG-ASSET-QUALITY-OVERRIDE + FLAG-Q4-FY26-DATA-GAP | PASS |
| P2.5 | NO growth offset (lenders get none, Amendment 7) | growth_offset = 0; "loan growth cannot offset underwriting" | PASS |
| P2.6 | FLAG-CASH structural (Ind AS 7), no cash-multiplier penalty | Carried, zero penalty; Pillar 2L governs | PASS |
| P2.7 | Quality-Adjusted Base = Base × multiplier | 14.3x × 1.00x = 14.3x | PASS |

### Pillar 3 — Growth Visibility (decoupled, Amendments 4.1/4.2, +6x cap)

| # | Rule | Recompute | PASS/FAIL |
|---|---|---|---|
| P3.1 | 3a qualifiers 📄-gated; award +2x only if any two qualify | Clean qualifiers = 1 (mgmt grade B). SOM 23.6% ≥20% but capacity cross-check is inference, not clean 📄 → not counted; capex-embedded 12.6% <15% fails; order book N/A → 3a = +0x | PASS |
| P3.2 | 3b Moat Formation EM-gated table, EM 25-29 any timeline → +1x | EM 25.3 → +1x (Master Pillar 3 table line: "EM 25-29 any timeline → +1x") | PASS |
| P3.3 | 3c Duration premium 📄-gated | N/A lender (no documented order book / contracted tenor) → +0x | PASS |
| P3.4 | Combined 3a+3b+3c ≤ +6x cap | +0 +1 +0 = +1x ≤ 6x | PASS |

### Strategic Premium + UA + Sector Cap

| # | Rule | Recompute | PASS/FAIL |
|---|---|---|---|
| SP.1 | Strategic base +0x; single-credit (ROE re-rating barred, credited in Pillar 1) | +0x base; re-rating route barred, correct | PASS |
| SP.2 | Optional +1x Federal Bank backing is a DISTINCT premium type (Master: "Turnaround with institutional backing +1 to +2x"), not the barred ROE re-rating | Distinct category confirmed; held at +0x in governing case (no double-credit) | PASS |
| UA.1 | UA NOT applied (Amendment 3 qualifiers) | FII 0.66% + DII 18.82% = ~19.5% >> 3% test → all_met NO → no 1.25x | PASS |
| UA.2 | UA ordering min(F×1.25, Cap), F2 row present | UA not qualified → F2 = F = 15.3x | PASS |
| SC.1 | Sector cap 18x Banks/NBFCs/MFIs applied as ABSOLUTE ceiling | H = min(15.3, 18) = 15.3x; both tracks below 18x | PASS |
| SC.2 | No exit PE from outside Section 1B | Every multiple earned via the worksheet; no round-number default | PASS |

### Four-Pillar Summary & ranges

| # | Rule | Recompute | PASS/FAIL |
|---|---|---|---|
| FP.1 | Raw PE F = Quality-Adjusted Base + Growth + Strategic | 14.3 + 1 + 0 = 15.3x | PASS |
| FP.2 | Track 2 range ±7.5%, rounded to nearest 0.5x (Amendment 6) | 15.3×0.925 = 14.15 → 14.0x; 15.3×1.075 = 16.45 → 16.5x | PASS |

---

## B. RRM DUAL-TRACK, HURDLE RATIO, TWO-TIER (B11)

### RRM Track 1 (Master v3.3 RRM Dual-Track Derivation)

| # | Rule | Recompute | PASS/FAIL |
|---|---|---|---|
| R.1 | Track 1 = Fundamental (Quality-Adjusted) Base PE × RRM, capped at sector cap | 14.3x × RRM | PASS |
| R.2 | RRM = 1 + (13.5 − r) × 0.12, percentage-point reading (Amendment 4.4), bounds 0.70-1.60 | r = 13.5 → 1 + 0 × 0.12 = 1.00; within bounds | PASS |
| R.3 | r = CoE 13.5% (one required-return, one mechanism) | r aligned to CoE; no second required-return introduced | PASS |
| R.4 | Track 1 value & range | 14.3 × 1.00 = 14.3x; ±7.5% → 13.0x / 15.5x | PASS |
| R.5 | BOTH tracks present and carried through every fair value and the verdict card | Track 1 and Track 2 shown in worksheet, Section 3-4 tables, and verdict card | PASS |
| R.6 | Divergence test; more conservative track governs entry | (15.3−14.3)/14.3 = 7.0% (<15%); governing = Track 1 (more conservative) | PASS |

### Hurdle Ratio (Amendment 2 / two-tier Amendment 4.3)

| # | Rule | Recompute | PASS/FAIL |
|---|---|---|---|
| H.1 | HR = (1+EPS CAGR)³ × (Dest PE mid ÷ Current PE), governing track mid | Uses Track 1 mid 14.3x, Current PE 17.98x | PASS |
| H.2 | Current PE internally consistent | 164 / 9.12 = 17.98x (consistent with EPS base; more conservative than 16.0x screener) | PASS |
| H.3 | HR base arithmetic | 1.15³ × (14.3/17.98) = 1.5209 × 0.7953 = 1.21 | PASS |
| H.4 | Bull row permitted (Role 5 grade A or B) | Grade B = Good → Bull EPS CAGR usable | PASS |
| H.5 | HR bull arithmetic | 1.20³ × 0.7953 = 1.728 × 0.7953 = 1.37 | PASS |
| H.6 | HR(Bull) < 1.953 → STOP | 1.37 < 1.953 → STOP; robustness rows (Track 2, 16.0x, +1x strategic) all still STOP | PASS |
| T.1 | Tier assignment (Amendment 4.3): Tier A when combined = TURNAROUND/HIGH POTENTIAL OR FII+DII <3% | Combined TURNAROUND → Tier A (25% hurdle, divisor 1.953) correctly applied | PASS |
| T.2 | Verdict card MUST state on first line "Tier: [A/B] \| Hurdle: [25%/20%]" | ABSENT from B11 verdict card (4H) and B14 verdict box | **FAIL (MINOR)** |

---

## C. PROJECTIONS, TRIANGULATION, ENTRY, VERDICT (B11)

| # | Rule / arithmetic | Recompute | PASS/FAIL |
|---|---|---|---|
| E.1 | EPS Y3 (9.12 base) | bear 9.12×1.10³=12.14; base ×1.15³=13.87; bull ×1.20³=15.76 | PASS |
| E.2 | BVPS Y3 (78.2 base) | bear ~105.4; base ~112.2; bull ~118.0 (book CAGR on ROE×retention) | PASS |
| E.3 | P/B fair value = justified exit P/B × BVPS Y3 | 105.4×0.85=89.6; 112.2×1.05=117.8; 118.0×1.25=147.5 | PASS |
| E.4 | P/E fair value diagonal (Track 1 13.0/14.3/15.5) | 12.14×13.0=157.8; 13.87×14.3=198.3; 15.76×15.5=244.3 | PASS |
| E.5 | Justified P/B primary = ROE/CoE; P/B primary 60% / P/E secondary 40% (Amendment 7) | 13.56/13.5 ≈ 1.00x; weights honour P/B-primary carve-out | PASS |
| E.6 | Triangulation both tracks | T1 base 70.7+79.3=150.0; T2 base 70.7+84.9=155.6 (all cells recompute clean) | PASS |
| E.7 | SOM cross-check performed | Base EPS/revenue ~15-17% below B09 SOM-implied 23.6% → consistent, no cut | PASS |
| E.8 | 4D weights match grade (Master 4D: Good = 25/50/25) | 25/50/25 applied; no re-weighting trigger evidenced | PASS |
| E.9 | Expected prob-weighted CAGR | −10.7×.25 + −2.9×.50 + 4.3×.25 = −3.05 ≈ −3.1% | PASS |
| E.10 | Entry = base FV ÷ 1.953 (Tier A); 30% = ÷2.197; MoS 20% below 25% entry | 150/1.953=76.8; 150/2.197=68.3; 76.8×0.8=61.4 → range Rs 68-77, MoS Rs 61 | PASS |
| E.11 | Upside/downside ratio | 13.5 / 28.7 = 0.47x (fails ≥2x) | PASS |
| E.12 | Every unresolved input set by stated conservative rule, no silent fills | FY[Y+2] ROE 15.0% and CoE 13.5% set with reasoning + anchors under "UNRESOLVED INPUTS"; gaps propagated | PASS |
| E.13 | One-improvement-one-mechanism (no double-credit) | ROE recovery in Pillar 1 only; Strategic barred; shared credit-cost catalyst FLAGGED for Role 3 (pillars measure different dimensions — permitted per Amendment 4 / FTTCP shared-catalyst rule) | PASS |
| E.14 | Decision AVOID follows framework | HR STOP + U/D 0.47<2x + Gate 0 AVOID all force AVOID | PASS |

---

## D. B10 ASSEMBLY HANDOFF

| # | Rule | Recompute | PASS/FAIL |
|---|---|---|---|
| A.1 | Deliberation overlay carried as authoritative into B11 (Pillar 1 ROE basis, P/B primary, Pillar 2L 1.00x + self-withdraw, 18x cap, single-credit) | All overlay fields present in B11 verbatim | PASS |
| A.2 | Input gaps propagated, not silently filled | FY-wise ROE, Q4 FY26 breakout, FY[Y+2] ROE, CoE, FII/DII all surfaced as gaps | PASS |
| A.3 | UA qualifiers resolved with evidence | FII 0.66% + DII 18.82% from shareholding-pattern-screener.txt → all_met NO | PASS |

---

## E. B14 ROLE 2 EXTENSION (Master v3.3 Role 2 decision + sizing)

| # | Rule | Recompute | PASS/FAIL |
|---|---|---|---|
| R2.1 | Verdict AVOID per Master decision rules ("AVOID: Gate 0 AVERAGE/AVOID OR U/D <2x OR HR STOP") | Gate 0 AVOID + U/D 0.47 + HR STOP → AVOID; hardest verdict wins | PASS |
| R2.2 | Entry range / MoS carried from Role 1, not re-derived | Rs 68-77, MoS Rs 61 sourced to 11-valuation.md 4E | PASS |
| R2.3 | Large gate fails (Gate 0 EXCELLENT + Promoter EXEMPLARY/TRUSTWORTHY + EM EXPANSION + CMP<MoS) | Fails on Gate 0 AVOID, Promoter CAUTION, EM STRENGTHENING | PASS |
| R2.4 | Medium gate fails (Gate 0 GOOD+ + Promoter TRUSTWORTHY + CMP≤Entry) | Fails on Gate 0 AVOID, Promoter CAUTION | PASS |
| R2.5 | Promoter verdict cap always binds (Master: caps override upward) | Promoter CAUTION caps at Small; no upward override | PASS |
| R2.6 | Gate 0 AVOID cap on eligibility | Applied; classification stands despite structural NBFC zeros | PASS |
| R2.7 | Position size = Small (ceiling only, not active; verdict AVOID) | Correctly framed as ceiling; no live position | PASS |
| R2.8 | No operator override to position size unless documented | position_size_override empty; two recorded overrides are valuation inputs, not size instructions | PASS |
| R2.9 | Entry conjunction (anti-value-trap) stated in Section 7 verdict box (Master line 811) | Present verbatim ("price inside zone AND no thesis-broken trigger fired") | PASS |
| R2.10 | Decision-rule trace present and internally consistent | Section 7 trace maps every rule to AVOID | PASS |

Note on R2.5/R2.6: FEDFINA's Promoter verdict is CAUTION (below TRUSTWORTHY), so it fails the Medium/Large quality gates on its own; combined with Gate 0 AVOID, Small is the only reachable tier even if the stock ever entered the zone. The B14 tiering logic reaches this correctly and does not manufacture an override.

---

## FINDINGS (consolidated)

| Severity | Location | Rule | Finding | Impact |
|---|---|---|---|---|
| MINOR | B11 verdict card (11-valuation.md §4H); B14 verdict box (14-thesis.md §7) | Amendment 4.3 tier-line mandate | The mandated first-line declaration "Tier: A \| Hurdle: 25%" is absent from both verdict cards. Tier A is correctly applied numerically (25% hurdle, 1.953 divisor, entry Rs 68-77), so this is presentational only. | None on destination PE, Hurdle verdict, or decision |

No CRITICAL or MAJOR findings. No misapplication changes the destination PE by >1x, flips the Hurdle verdict, or changes the decision.

## RECOMPUTATION VERDICT

- Destination PE: CONCUR. Track 1 14.3x mid (13.0-15.5x), Track 2 15.3x mid (14.0-16.5x) reproduce exactly. No restatement.
- Decision: CONCUR. AVOID (on valuation); Hurdle Ratio STOP; probability-weighted CAGR −3.1%; entry Rs 68-77 / MoS Rs 61; position size Small (ceiling only) all reproduce.

## COVERAGE

56 rules checked across Pillars 1-3, Strategic/UA/Sector cap, RRM dual-track, Hurdle Ratio, two-tier assignment, projections, triangulation, entry/MoS, B10 handoff, and B14 Role 2 decision/sizing. 55 PASS, 1 FAIL (MINOR). Acceptance rate 98.2%. Not re-audited: raw source-number provenance (Verifier A scope) and phase-1 Gate 0 / Emerging Moat (already recorded).

---

```yaml
stage: B12c-valuation
company: "FEDFINA"
run_date: "2026-07-15"
model: claude-opus-4-8
status: complete
phase: 3
scope: "B11 valuation + B10 assembly (Section 1B v3.3 Four-Pillar, lender carve-outs) + B14 Role 2 decision/sizing (Master v3.3 Role 2)"
valuation:
  rules_checked: 56
  fails:
    - severity: "MINOR"
      location: "11-valuation.md §4H verdict card; 14-thesis.md §7 verdict box"
      rule: "Amendment 4.3 — verdict card MUST state on first line 'Tier: [A/B] | Hurdle: [25%/20%]'"
      note: "Tier A correctly applied in the math (25% hurdle, 1.953 divisor); only the mandated first-line label is missing. Presentational; decision unaffected."
recomputed_destination_pe: ""   # concur — Track 1 14.3x mid, Track 2 15.3x mid reproduce exactly
recomputed_decision: ""         # concur — AVOID (on valuation), Hurdle STOP
findings:
  - {severity: "MINOR", location: "11-valuation.md §4H / 14-thesis.md §7", note: "Amendment 4.3 Tier/Hurdle first-line declaration absent from verdict cards; Tier A applied correctly in arithmetic"}
critical_count: 0
major_count: 0
minor_count: 1
acceptance_rate: 98    # 55 rules passed / 56 checked
```
