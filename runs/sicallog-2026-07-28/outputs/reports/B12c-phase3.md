# STAGE 12 — VERIFIER C: FRAMEWORK ADHERENCE (B12c)
# PHASE 3 — VALUATION & THESIS ADHERENCE (deferred half of B12c)
# Company: Sical Logistics Limited (SICALLOG) | Run date: 2026-07-29
# Model: claude-opus-4-8

> **SCOPE.** This is the PHASE 3 valuation-adherence audit. Gate 0 (B01) and
> Emerging Moat (B07) were audited in Phase 1 (B12c.yaml, 2026-07-28) and are
> carried here **verbatim, unchanged** (0 CRIT / 0 MAJ / 4 MINOR, acceptance 95).
> This pass audits VALUATION (B11) and Role 2 THESIS (B14) framework adherence
> against the operator-approved base in the FTTCP deliberation.
>
> **BOTTOM LINE: CONCUR.** Every Section 1B pillar input, both destination-PE
> tracks, the Hurdle Ratio, the entry/MoS cascade, the tier assignment, and the
> Role 2 decision rules reconcile on re-derivation. Recomputed destination PE =
> RRM 8.6x governing / additive 12.4x (matches). Recomputed decision = AVOID,
> position None, Tier A (matches). No exit PE originates outside Section 1B.
> 0 CRITICAL, 0 MAJOR in the valuation pass; 3 MINOR presentational notes.

---

## PART 1 — GATE 0 (B01) — CARRIED FROM PHASE 1, UNCHANGED

Not re-audited this phase. Phase-1 result stands: 42 rules checked, 2 MINOR fails
(A4 ROCE trend basis-mix; M12 negative-WC/float band), both immaterial to the
Block totals and to Gate0 classification AVOID (14/160). See B12c.yaml lines 6-10.

## PART 2 — EMERGING MOAT (B07) — CARRIED FROM PHASE 1, UNCHANGED

Not re-audited this phase. Phase-1 result stands: 34 rules checked, 2 MINOR fails
(H3 evidence-type multiplier; R1 impact weighting), both immaterial to EM
classification MODEST (17.4/80). See B12c.yaml lines 11-15.

---

## PART 3 — VALUATION (B11) — DEEP AUDIT vs OPERATOR-APPROVED BASE

Authority chain: FTTCP deliberation "OPERATOR-APPROVED VALUATION PILLARS" block
(authoritative for Phase 3) → carried verbatim into B10 → applied in B11. B11 may
NOT silently derive a different exit PE. It did not.

### 3.1 Pillar 1 — ROCE Base (continuous formula + v3.5.1 normalization route)

| Rule (authority) | Required | B11 value | Re-derivation | Verdict |
|---|---|---|---|---|
| Continuous formula (Amdt 5) | 0.5×ROCE + 7.5, floor 9 / cap 24 | 12.9x | 0.5×10.7 + 7.5 = 12.85 → 12.9x | **PASS** |
| ROCE blend (FTTCP v1.2 RECOVERING 40-60%) | 60% current / 40% FY[Y+2] | 10.7% | 0.60×9.9 + 0.40×12.0 = 5.94+4.80 = 10.74 → 10.7% | **PASS** |
| Normalization route (v3.5.1) | Route A test: (CWIP+idle+advances) >20% cap employed | NONE | CWIP 4.20cr = 0.6% of capital employed < 20% → **Route A fails** | **PASS** |
| Normalization route (v3.5.1) | Route B: TEMP-DEPRESSED/RECOVERING + 📄 pre-depression HIGH-ROCE cycle | NONE | Backward verdict STRUCTURALLY LOW (not TEMP-DEPRESSED); FY17-19 ROCE 6.9/6.2/5.3% is a LOW base, no high pre-cycle to normalize toward → **Route B fails**. Neither holds → **NONE correct** | **PASS** |
| Band table NOT used | continuous formula only | continuous used | old bands not applied | **PASS** |

Route selection is exactly right: with neither Route A nor Route B satisfied, the
statutory 60/40 blend feeds the formula directly. NONE is the correct declaration.

### 3.2 Single-Credit Rule (Amendment 4)

| Rule | Required | B11 | Verdict |
|---|---|---|---|
| ROCE recovery credited in ONE place | Pillar 1 midpoint OR Strategic Premium, never both | Credited via **Pillar 1**; Strategic Premium ROCE re-rating **BARRED** | **PASS** |
| Route stated | worksheet declares the route | "ROCE recovery credited via: Pillar 1" stated | **PASS** |
| Shared-catalyst flagged (not a double-credit) | if same catalyst drives Pillar 1 and a Pillar 3 premium, permitted but must be flagged | SHARED CATALYST flag = YES (SECL + Chennai drive Pillar 1 ROCE AND Pillar 3a/3c); Role 3 must stress-test | **PASS** — permitted (Amdt 4: earnings-visibility vs capital-efficiency are different measures), correctly flagged not double-credited |

### 3.3 Pillar 2 — Cash Conversion Multiplier

| Rule | Required | B11 | Verdict |
|---|---|---|---|
| Structural band | Structurally-negative → 0.65x | 0.65x | **PASS** |
| Structural test | "if growth stopped, WC days stay high?" = YES → structural | YES → structural | **PASS** |
| No growth offset on structural | offset table: Structural = 0 | 0.65 + 0 offset | **PASS** |
| Quality-adjusted base | ROCE base × multiplier | 12.9 × 0.65 = 8.385 → 8.4x | **PASS** |
| INDETERMINATE cap (CLAUDE.md) | caps at PROCEED WITH CAVEATS, missing evidence named | capped, FLAG-CASH carried (CARO +45.6%, ECL freeze, no live rating) | **PASS** |

Note: the 0.65x band's literal descriptor is "rating agency confirms persistent
WC," and the ICRA rating is withdrawn (no live rating). The Master's governing
structural test ("if growth stopped tomorrow, would WC days still be high?") is
independently answered YES, which is what assigns 0.65x. Not a fail; the
withdrawn rating is the reason the disposition is capped INDETERMINATE, which
B11 honors.

### 3.4 Pillar 3 — Growth Visibility (decoupled, Amendments 4.1 / 4.2)

| Component | Required | B11 | Re-derivation | Verdict |
|---|---|---|---|---|
| 3a Growth Visibility | +2x if any two 📄 qualifiers; grade C caps at +2x | +2x | order book 11.9x rev (≥1.0x) ✓ + SOM-implied CAGR >20% ✓ = two qualify → +2x; grade C caps at +2x (also bars the +3x route) | **PASS** |
| 3b Moat Formation | EM-gated; EM 17.4 < 25 | +0x | below 25 threshold → +0x | **PASS** |
| 3c Duration | +2x when visibility ≥4yr (📄 LoA) | +2x | order-book visibility ~11.9yr ≥ 4yr, SECL LoA with stated value → +2x | **PASS** |
| Pillar 3 total | combined 3a+3b+3c hard cap +6x | +4x | 2+0+2 = 4 ≤ 6 | **PASS** |

### 3.5 Strategic Premium

+0x. Institutional backing (GIP/BlackRock ~57%) sits at the PARENT (Pristine),
not at Sical; ROCE re-rating optionality barred by single-credit (already in
Pillar 1). **PASS.**

### 3.6 Undiscovered Alpha (Amendment 3) — ordering + qualifiers

| Rule | Required | B11 | Verdict |
|---|---|---|---|
| Three qualifiers all met to apply | listed ≥12mo AND (Gate0≥60 OR EM≥25) AND FII+DII <3% | listed ✓; Gate0 14 & EM 17.4 → quality gate **fails**; FII+DII 3.19% > 3% **fails** → not all met | **PASS** |
| UA applied? | only if all three | **NOT APPLIED** (F2 = F) | **PASS** |
| Ordering min(F×1.25, cap) | UA on RAW PE before sector cap | not applied → no ordering breach possible | **PASS (correctly not applied)** |

### 3.7 Additive & RRM Destination PE (both tracks, Amendment 4.4)

| Rule | Required | B11 | Re-derivation | Verdict |
|---|---|---|---|---|
| Additive Raw PE | (ROCE base × cash) + growth + strategic | 12.4x | 8.4 + 4 + 0 = 12.4x | **PASS** |
| Sector cap | min(Raw, cap), absolute | 12.4x (cap 20x not binding) | min(12.4, 20) = 12.4 | **PASS** (note MINOR-V3) |
| RRM formula | 1 + (13.5−r)×0.12, pct-points, bound ×0.70–×1.60 | 0.64 → floored 0.70 | 1 + (13.5−16.5)×0.12 = 1 − 0.36 = 0.64 → floor 0.70 | **PASS** |
| RRM destination PE | Base PE × RRM | 8.6x | 12.4 × 0.70 = 8.68 → 8.6x | **PASS** |
| Both tracks carried | through all fair values + verdict card | present in §3.2, §4A, verdict card | both tracks throughout | **PASS** |
| Divergence >15% → conservative governs | RRM (more conservative) sets entry | RRM governs (divergence 30.6%) | (12.4−8.6)/12.4 = 30.6% > 15% → RRM | **PASS** |
| r bound | r ∈ [9%, 18%] | 16.5% | micro-cap base 14% + structural cash + pledge + grade-C + NCI → 16.5% ∈ [9,18] | **PASS** |

**Recomputed destination PE = RRM 8.6x governing / additive 12.4x → MATCHES the
operator-approved base. CONCUR.**

### 3.8 Earnings Basis

One-year-forward P/E (operator-approved). B11 applies the exit multiple to FY30
(one year past the FY29 exit year). **PASS.**

### 3.9 Hurdle Ratio (Amendment 2) + credibility-grade gate on Bull

| Rule | Required | B11 | Re-derivation | Verdict |
|---|---|---|---|---|
| HR formula | (1+g)³ × (Dest PE mid ÷ Current PE) | 0.27 RRM / 0.39 additive | (1.50)³ × (8.6/107) = 3.375×0.0804 = 0.271; (1.50)³×(12.4/107) = 0.391 | **PASS** |
| Threshold Tier A | ≥ 1.953 | STOP | both far below 1.953 | **PASS** |
| Bull EPS CAGR cap (grade C) | Mixed/Poor grade → Bull row uses Base+5% max | bull 55% (= 50%+5%) | grade C → cap 55%; HR = (1.55)³×0.0804 = 0.299 < 1.953 | **PASS** |
| Verdict | STOP if HR(bull) < 1.953 | STOP | 0.30 on capped bull < 1.953 → STOP | **PASS** |

Basis note (MINOR-V2): B11 correctly could not anchor HR on a current clean PE
because clean pre-exceptional owners' EPS is negative (NM). It ran HR on an
explicit one-year-forward owners'-clean construct (current forward PE ~107x on
FY27 EPS ~Rs 1.00), holding numerator and denominator on the same basis (the
"SFL lesson"). Disclosed, internally consistent, verdict robust (to reach 1.953
against a 8.6/107 ratio would need EPS CAGR ≈ 190%). Logged as a MINOR
presentational/basis substitution, not a fail of substance.

### 3.10 Entry / MoS Cascade + Tier (Amendment 4.3)

| Rule | Required | B11 | Re-derivation | Verdict |
|---|---|---|---|---|
| Tier assignment | Tier A default; Tier B needs ALL 4 gates | Tier A, Tier B barred | Tier B fails 3 of 4: Gate0 not GOOD+/EM<25, promoter not TRUSTWORTHY (CONCERN), structural FLAG-CASH present → stays Tier A | **PASS** |
| Tier A divisor | 1.953 | 1.953 | 1.25³ = 1.953 | **PASS** |
| Entry = base ÷ divisor | RRM governing base Year-3 | Rs 14.9 | 29.1 ÷ 1.953 = 14.90 | **PASS** |
| MoS = entry × 0.80 | 20% below entry | Rs 11.9 | 14.9 × 0.80 = 11.92 → 11.9 | **PASS** |
| Entry range | ± around entry | Rs 12–15 | consistent | **PASS** |

### 3.11 Method discipline, SOM, unresolved inputs

| Rule | Required | B11 | Verdict |
|---|---|---|---|
| SOM cross-check performed | base CAGR vs SOM-implied ceiling | base 20% < SOM 38.5% ceiling & < 2yr hist 32.1% → CONSISTENT | **PASS** |
| No silent fills; unresolved handled conservatively | NOT FOUND, not estimated | land value NF (book only + bull uplift), slice debt assumed conservatively, segment EBITDA derived + flagged, forward EPS ILLUSTRATIVE | **PASS** |
| Exit PE only from Section 1B | no outside PE | exit PE = RRM 8.6x / additive 12.4x only; SOTP slice multiples are EV/EBITDA (method inputs), not exit PE | **PASS — no outside exit PE** |
| Peer data provenance | consistency across stages | B10 marked peer medians NOT FOUND; B11 extracted them from screener Data_Sheets for the tertiary SOTP anchor | **MINOR-V1** — cross-stage inconsistency, transparently flagged, immaterial to exit PE (peers only anchor the 10% tertiary SOTP slice multiples, flagged stale) |

---

## PART 4 — ROLE 2 THESIS (B14) — DECISION RULES & POSITION SIZING

| Rule (Master §7) | Required | B14 | Verdict |
|---|---|---|---|
| AVOID trigger | Gate0 AVERAGE/AVOID OR Promoter CONCERN/AVOID OR U/D <2x OR HR STOP | all four fire (Gate0 AVOID, Promoter CONCERN, U/D ≈0, HR STOP) | **PASS — AVOID correct** |
| Decision-rule trace | state the triggers | explicit trace naming all four | **PASS** |
| Position size | Promoter Concern cap overrides everything; no BUY to size | **NONE** | **PASS** |
| Position size override | only if operator-documented | none recorded → blank | **PASS** |
| Tier | Tier A, 25%, divisor 1.953; Tier B barred | Tier A stated; Tier B explicitly barred | **PASS** |
| Entry conjunction (anti-value-trap) | BUY only if price in zone AND no thesis-broken trigger | stated in Section 7 box | **PASS** |
| Fair values / entry carried from B11 | consistent | Rs 12–15 entry, MoS 11.9, base Rs 29 (RRM)/42 (additive), SOTP Rs 22 | **PASS** |
| Symmetric bull/bear | both carried honestly | Section 3 bull + Section 3-BEAR symmetric | **PASS** |

Role 2 reproduces the B11 valuation faithfully and applies the decision rules as
written. AVOID is over-determined (four independent triggers), position None is
forced by the absolute Promoter Concern cap, and Tier B is correctly barred.

---

## PART 5 — RECOMPUTATION & CONCURRENCE

- **Recomputed destination PE:** additive 0.5×10.7+7.5 = 12.85→12.9 ROCE base ×0.65
  = 8.385→8.4 quality base +4 +0 = **12.4x**; RRM 12.4×0.70 = 8.68→**8.6x**.
  Identical to the audited values. **No divergence >1x. CONCUR.**
- **Recomputed decision:** AVOID (on valuation), position None, Tier A 25% hurdle.
  Identical to B11/B14. **CONCUR.**
- **Exit-PE provenance:** clean. Only the Section 1B approved base (RRM 8.6x /
  additive 12.4x) is used as the exit multiple. No round-number default, no
  outside-1B multiple. **PASS.**

### Valuation-pass findings (all MINOR, all immaterial to destination PE and decision)

- **MINOR-V1** (peer provenance): B11 used peer EV/EBITDA multiples that B10
  marked NOT FOUND, sourced from screener Data_Sheets, to anchor the 10% tertiary
  SOTP slice multiples. Transparently flagged as stale/illustrative; does not
  touch the exit PE or any Section 1B pillar.
- **MINOR-V2** (HR basis): Hurdle Ratio run on a one-year-forward owners'-clean
  construct rather than a current trailing PE, because clean current EPS is
  negative (NM). Disclosed, internally consistent, STOP verdict robust.
- **MINOR-V3** (sector-cap row): the "Logistics (WC-heavy / project cargo) 20x"
  cap row is operator-assigned in the FTTCP deliberation; Amendment 8's table has
  no explicit "Logistics" row (nearest is Mining 20x). Non-binding here (both
  tracks 8.6x/12.4x sit far below 20x), so zero valuation impact.

No CRITICAL, no MAJOR. Every verdict-card figure and every Section 1B pillar input
reconciles.

---

## COMPLIANCE SUMMARY

| Framework | Rules checked | CRIT | MAJ | MINOR | Result |
|---|---|---|---|---|---|
| Gate 0 (B01) — Phase 1, carried | 42 | 0 | 0 | 2 | classification AVOID robust |
| Emerging Moat (B07) — Phase 1, carried | 34 | 0 | 0 | 2 | classification MODEST robust |
| Valuation (B11) — Phase 3 | 34 | 0 | 0 | 3 | CONCUR, destination PE + decision reconcile |
| Role 2 thesis (B14) — Phase 3 | (folded into valuation) | 0 | 0 | 0 | decision rules + sizing correct |
| **TOTAL** | **110** | **0** | **0** | **7** | **CONCUR — AVOID stands** |

```yaml
stage: B12c
company: "SICALLOG"
run_date: "2026-07-29"
model: claude-opus-4-8
status: complete
gate0:
  rules_checked: 42
  fails:
    - {rule: "A4 ROCE trend basis-mix", severity: "MINOR", detail: "FY26 precise ROCE (17.42%) compared to FY17 proxy ROCE (6.95%); not like-for-like. Score 5 holds under either basis. No block-total impact.", recomputed: "5 (unchanged)"}
    - {rule: "M12 Negative WC/Float band", severity: "MINOR", detail: "Two computable years (WC days 43.4, 30.0) both fall in literal '15-45 -> 1' band; B01 scored 0 on data-insufficiency (2 of 10 years). A score of 1 does not reach the >=3 moat-present bar, so moats_confirmed 0 and moat_class NONE unchanged.", recomputed: "0 or 1; moat_class NONE either way"}
emoat:
  rules_checked: 34
  fails:
    - {rule: "H3 evidence-type multiplier", severity: "MINOR", detail: "Summary types H3 as documented/claim but scorecard applies 1.0x. At 0.7x total 17.1 -> still MODEST.", recomputed: "1.0 or 0.7; em_class MODEST either way"}
    - {rule: "R1 impact weighting", severity: "MINOR", detail: "R1 assigned impact Moderate (adj 3.0) while Section 4C concludes the tailwind is fully shared/non-exclusive; a Low-impact read (2.0) is equally defensible. At 2.0 total 16.4 -> still MODEST.", recomputed: "3.0 or 2.0; em_class MODEST either way"}
valuation:
  rules_checked: 34
  fails:
    - {rule: "Peer data provenance (tertiary SOTP anchor)", severity: "MINOR", detail: "B11 extracted peer EV/EBITDA from screener Data_Sheets that B10 marked NOT FOUND, to anchor the 10% tertiary SOTP slice multiples. Transparently flagged stale/illustrative; does not touch exit PE or any Section 1B pillar.", recomputed: "no impact on destination PE (8.6x/12.4x) or decision"}
    - {rule: "Hurdle Ratio input basis (Amdt 2)", severity: "MINOR", detail: "HR run on one-year-forward owners'-clean construct (current fwd PE ~107x) rather than current trailing PE, because clean current EPS is negative/NM. Disclosed, internally consistent; STOP robust (would need ~190% EPS CAGR to clear 1.953).", recomputed: "HR 0.27 RRM / 0.39 additive / 0.30 capped-bull -> STOP unchanged"}
    - {rule: "Sector cap row authority (Amdt 8)", severity: "MINOR", detail: "'Logistics (WC-heavy/project cargo) 20x' cap is operator-assigned in the FTTCP deliberation; Amendment 8 has no explicit Logistics row (nearest Mining 20x). Non-binding (both tracks far below 20x).", recomputed: "min(12.4,20)=12.4x; min(8.6,20)=8.6x; zero impact"}
recomputed_destination_pe: ""   # CONCUR: RRM 8.6x governing / additive 12.4x reproduce exactly (12.85->12.9 x0.65=8.4 +4+0=12.4; 12.4x0.70=8.6)
recomputed_decision: ""         # CONCUR: AVOID (on valuation), position None, Tier A; four independent AVOID triggers (Gate0 AVOID, Promoter CONCERN, U/D<2x, Hurdle STOP)
findings:
  - {severity: "MINOR", framework: "gate0", location: "B01 Block A / A4", note: "ROCE trend compares precise FY26 vs proxy FY17; immaterial, score 5 robust"}
  - {severity: "MINOR", framework: "gate0", location: "B01 Block F / M12", note: "WC-float band literally 15-45->1 vs scored 0 on data-insufficiency; immaterial to moat_class NONE"}
  - {severity: "MINOR", framework: "emoat", location: "B07 scorecard / H3", note: "H3 multiplier 1.0x on a doc/claim-mixed row; immaterial, MODEST holds"}
  - {severity: "MINOR", framework: "emoat", location: "B07 scorecard / R1", note: "R1 impact Moderate vs its own 'no differential advantage' conclusion; immaterial, MODEST holds"}
  - {severity: "MINOR", framework: "valuation", location: "B11 §3.3 tertiary peer cross-check", note: "peer EV/EBITDA extracted despite B10 NOT FOUND; anchors only the 10% tertiary SOTP, immaterial to exit PE"}
  - {severity: "MINOR", framework: "valuation", location: "B11 Hurdle Ratio §1B/§4H", note: "HR on forward-owners' construct (current clean PE negative/NM); disclosed, STOP robust"}
  - {severity: "MINOR", framework: "valuation", location: "B11 §0 / §1B sector cap", note: "Logistics 20x cap operator-assigned, not an explicit Amdt 8 row; non-binding, zero impact"}
critical_count: 0
major_count: 0
minor_count: 7
acceptance_rate: 94   # rules passed (103) / checked (110); gate0 40/42, emoat 32/34, valuation 31/34
```
