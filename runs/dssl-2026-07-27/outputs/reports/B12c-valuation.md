# STAGE 12c — VERIFIER C: FRAMEWORK ADHERENCE (PHASE 3 VALUATION HALF)

**Run:** dssl-2026-07-27 | **Verifier:** B12c framework-adherence | **Model:** claude-opus-4-8
**Scope:** PHASE 3 valuation-adherence audit ONLY, extended to Role 2 (B14) decision rules and position sizing. Gate 0 (B01) and Emerging Moat (B07) checks were completed and recorded in phase 1 (acceptance 99%); they are NOT re-run here.
**Artifacts audited:** B10-valinputs.md, B11-valuation.md, B14-thesis.md
**Authorities:** Master v3.3 (Section 1B, Role 1 RRM, Role 2), Section 1B v3.3 Amendments, Section 1B v3.5.1 Reconciliation (Amendment 9 Route A/B), FTTCP v1.2 (Pillar 1 ROCE table, SOTP rule).
**Domain note:** Source fidelity (does a number exist in the PDF) is Verifier A's non-overridable domain. This report audits rule APPLICATION and judgment only; it re-derives from the anchored inputs as given.

---

## PART 1 — PILLAR 1 (ROCE BASE MULTIPLE)

| # | Rule | Framework anchor | Applied value | Verdict |
|---|---|---|---|---|
| P1.1 | FTTCP ROCE forward verdict is sole Pillar 1 authority; RECOVERING maps to blend of current + FY[Y+2] | FTTCP v1.2 table (RECOVERING 40-60% → 60/40 current/FY[Y+2]) | RECOVERING(+1); FY[Y+2] NOT FOUND → blend not computable → current 30.17% used as sole anchor | PASS |
| P1.2 | NOT FOUND is the only fill; conservative outcome | CLAUDE.md; Amendment 4.5 text ("NOT FOUND is the only fill") | Current 30.17% alone credits no upward recovery = conservative (a RECOVERING FY[Y+2] would blend higher) | PASS |
| P1.3 | Continuous formula 0.5×ROCE+7.5, floor 9x, cap 24x | Amendment 5 | 0.5×30.17+7.5 = 22.585 → **22.6x**; cap 24x not binding | PASS |
| P1.4 | Normalization route declared; Route A gate 20%, Route B needs 📄 dated catalyst | Section 1B v3.5.1 (Amendment 9) | Route NONE. Route A: idle pool ~0.6% CE << 20% gate → fails. Route B: no named/dated 📄 unwind catalyst (RBI go-live undated, capex payoff NOT FOUND) + FY[Y+2] NOT FOUND → fails. Both fail → statutory 30.17% feeds Pillar 1. | PASS |
| P1.5 | Single-credit: recovery via Pillar 1 OR Strategic Premium, never both | Amendment 4 / FTTCP single-credit | Recovery credited via Pillar 1 only; Strategic Premium ROCE route BARRED. (Also correct because Strategic route is permitted only for STAGNANT/FIRING verdicts, not RECOVERING.) | PASS |
| P1.6 | Worksheet yaml route label accuracy | Presentational | B11 yaml `roce_recovery_route: "pillar1-midpoint"` — but NO midpoint was computed (FY[Y+2] NOT FOUND; route NONE; current used as sole anchor). Label is misleading vs the prose/worksheet. | **FAIL (MINOR)** |

**Pillar 1 verdict:** Rule application correct and conservative. Base 22.6x confirmed. One MINOR yaml-label imprecision (P1.6) that does not touch any number.

---

## PART 2 — PILLAR 2 (CASH CONVERSION MULTIPLIER)

| # | Rule | Framework anchor | Applied value | Verdict |
|---|---|---|---|---|
| P2.1 | Cash verdict maps to multiplier; STAGNANT/structural → neutral | FTTCP cash verdict; operator Override 1 | STAGNANT(0) → **1.00x neutral** | PASS |
| P2.2 | No growth offset when WC intensity is STRUCTURAL | Master Pillar 2 structural-vs-growth test; Acuité "operations expected to remain intensive over medium term" | Growth offset = 0 (structural per rating-agency precedence over 17-day net-WC claim) | PASS |
| P2.3 | Ind AS 116 / SOTP carve-out applied, not double-counted | FTTCP SOTP rule (do not penalize BOO/annuity portion) | Lease-annuity portion not cash-penalized; used only to justify holding at 1.00x (no penalty), so no double-count. Multiplier already neutral. | PASS |

**Observation (not scored):** A full SOTP blend (InvIT-style 10-14x on the BOO leg, blended sector cap) was NOT performed; the deliberation instead approved a single four-pillar treatment with the Data-centres 30x cap. This is a documented operator ruling (Override 3), within the framework's optionality, and it is the conservative-neutral treatment here. Noted, not a fail.

---

## PART 3 — PILLAR 3 (GROWTH VISIBILITY PREMIUM)

| # | Rule | Framework anchor | Applied value | Verdict |
|---|---|---|---|---|
| P3.1 | 3a award: +3x if ≥3 qualifiers AND grade A/B; +2x if any two; grade C caps at +2x | Amendment 4.1 | Qualifiers holding: order book 2.08x (≥1.0x) ✓; SOM-implied CAGR 33.9% (≥20%) with capacity cross-check passing ✓; delivery grade B ✓. (capex-embedded growth = 0x, fails.) Three of four qualify AND grade B → **+3x** | PASS |
| P3.2 | 3b Moat Formation: EM-gated | Amendment 4.1 / Master EM table (EM <25 → +0x) | EM 22.7 < 25 → **+0x** | PASS |
| P3.3 | 3c Duration: +1x at ≥2.5yr visibility | Amendment 4.2 | Visibility 2.08yr < 2.5 → **+0x** | PASS |
| P3.4 | Combined 3a+3b+3c ≤ +6x hard cap | Amendment 4.1/4.2 | +3x total, under cap | PASS |

**3a interpretive note (informational, not scored a fail):** The +3x turns on counting "management delivery grade A/B" as one of the four listed qualifying-evidence items (which the amendment text does). Under a stricter reading where grade is only the gate and not a counted qualifier, only two non-grade items qualify (order book + SOM; capex-embedded fails) → +2x. Impact test: +2x would leave the ADDITIVE destination unchanged (24.6×1.25 = 30.75, still cap-bound at 30.0x) and move RRM by only ~0.6x (24.6×0.76×1.25 ≈ 23.4x) — within tolerance, decision unchanged. The literal amendment text supports +3x; flagged for transparency only.

---

## PART 4 — PILLAR 4 / STRATEGIC PREMIUM & UNDISCOVERED ALPHA

| # | Rule | Framework anchor | Applied value | Verdict |
|---|---|---|---|---|
| P4.1 | Strategic Premium: no licence/monopoly, ROCE route barred | Master Strategic table; Amendment 4 single-credit | +0x (weak pricing power, no scarcity; ROCE route barred) | PASS |
| UA.1 | All three qualifiers evidenced | Master UA / Amendment 3 | Listed ≥12m (inc. 1995) ✓; Gate 0 core 60 ≥60 ✓; FII+DII 1.36% <3% ✓ | PASS |
| UA.2 | Ordering: Final = min(Raw F ×1.25, Sector Cap); UA before cap on additive Row F | Amendment 3 | F=25.6 → F2 = 25.6×1.25 = 32.0 → min(32.0, 30.0) = **30.0x** | PASS |
| UA.3 | Sector cap absolute; cap binds | Master Sector Reality Cap | Data centres/cloud infra (capital-heavy) = 30x; F2 32.0 truncated to 30.0. Cap absolute, honoured | PASS |
| UA.4 | Quality uplift on cap only if durability ≥ Moderate-Strong | Master (25% uplift rule) | No uplift applied (durability Medium, EM MODEST) — correct; uplift would need Moderate-Strong | PASS |
| UA.5 | UA multiplier applied INSIDE the RRM (governing/conservative) track | Master RRM: "Destination PE = Fundamental Base PE × RRM, capped at sector cap" — no UA term | B11 computes RRM = 25.6 × 0.76 × **1.25 UA** = 24.3 → carried 24.0x. Master RRM formula contains no UA factor. | **FAIL (MAJOR)** |

**UA.5 detail (the material finding).** The RRM track is the conservative counterweight that GOVERNS the entry zone. The Master RRM derivation is "Fundamental Base PE × RRM," with no UA multiplier; UA ordering is codified (Amendment 3) only for the additive Row F → F2. B11 inserts ×1.25 UA into the RRM computation, lifting the governing track from a literal **25.6 × 0.76 = 19.5x** to **24.0x** — a >4x, >1x swing, in the LESS-conservative direction for the track whose purpose is conservatism.
Recomputed consequences if UA is excluded from RRM (literal reading):
- RRM destination ≈ **19.5x** (vs reported 24.0x).
- Pure-P/E base FV ≈ Rs2,078 (vs Rs2,558); entry = 2,078/1.953 ≈ **Rs1,064** (vs Rs1,310); MoS ≈ **Rs851** (vs Rs1,048).
- RRM base Hurdle = 1.600 × (19.5/18.5) = **1.69 → CONDITIONAL** (fails 1.953 on base; bull 2.35 passes), vs reported PASS 2.08.
- CMP Rs1,232 would sit ABOVE the entry band (Rs1,064), not inside it — the "price already inside the band, hurdle PASSES" framing collapses.
**Decision impact: NONE** — WATCHLIST holds either way (CMP above entry, or DEEP WATCH pending confirmation), so this is MAJOR, not CRITICAL. It is material to the entry zone, MoS, and the governing-track hurdle characterization. Framework text is genuinely silent on UA-in-RRM, so a consistent-application defence exists; surfaced for the operator rather than overturned.

---

## PART 5 — RRM TRACK & GOVERNING-TRACK CHOICE

| # | Rule | Framework anchor | Applied value | Verdict |
|---|---|---|---|---|
| R.1 | RRM = 1+(13.5−r)×0.12, percentage-point reading | Amendment 4.4 | 1+(13.5−15.5)×0.12 = 1−0.24 = **0.76** ✓; percentage-point reading (r=15.5 → −2.0, not −0.02) | PASS |
| R.2 | Base r + durability/governance load, bounded [9%,18%] | Master RRM | small/micro 14% + 1.5% (promoter CAUTION, Cybercons, acct 5/10) = 15.5%, within bounds; RRM 0.76 within [0.70,1.60] | PASS |
| R.3 | BOTH tracks carried through all fair values and the verdict card | Master Role 1 dual-track | Additive and RRM present in worksheet, matrix, fair-value table, and verdict card | PASS |
| R.4 | On >15% divergence, more conservative track sets entry zone | Master Role 1 | Divergence ~23% (>15%); RRM (lower) GOVERNS entry zone | PASS (choice correct; magnitude affected by UA.5) |

---

## PART 6 — HURDLE RATIO

| # | Rule | Framework anchor | Applied value | Verdict |
|---|---|---|---|---|
| H.1 | HR = (1+EPS CAGR)³ × (Dest PE mid ÷ Current PE); threshold 1.953 (Tier A) | Amendment 2 / 4.3 | Base EPS CAGR 16.96% → 1.1696³ = 1.600; RRM 1.600×(24.0/18.5)=**2.08 PASS**; additive 1.600×(30/18.5)=**2.60 PASS** | PASS (subject to UA.5) |
| H.2 | EPS-basis consistency: numerator AND denominator trailing (SFL lesson) | Master / SFL lesson | Numerator trailing FY26→FY29; denominator current PE = CMP/trailing FY26 EPS = 18.5x. Both trailing. Consistent. | PASS |
| H.3 | Bull row usable only if credibility grade A/B | Amendment 2 | Grade B → bull permitted; both bull rows pass | PASS |

Arithmetic re-derived clean. The reported PASS at 2.08 holds ON THE REPORTED RRM 24x. If UA.5 is corrected (RRM 19.5x), the RRM base row becomes CONDITIONAL (1.69), which still permits WATCHLIST/BUY-ON-DIPS. Additive PASS is robust regardless.

---

## PART 7 — TIER & ENTRY ZONE

| # | Rule | Framework anchor | Applied value | Verdict |
|---|---|---|---|---|
| E.1 | Tier A assignment | Amendment 4.3 | FII+DII 1.36% <3% → Tier A (hurdle 25%, divisor 1.953). Correct. | PASS |
| E.2 | Entry = base FV ÷ 1.953 (Tier A) | Amendment 4.3 | RRM 2,558/1.953 = Rs1,310 ✓; additive 3,197/1.953 = Rs1,637 ✓ | PASS |
| E.3 | MoS = 20% below entry | Amendment 4.3 | 1,310×0.8 = Rs1,048 ✓ | PASS |

(Magnitudes inherit the UA.5 caveat; the divisor/tier mechanics are correct.)

---

## PART 8 — ROLE 2 (B14) DECISION RULES & POSITION SIZING

| # | Rule | Framework anchor | Applied value | Verdict |
|---|---|---|---|---|
| D.1 | BUY NOW gate: CMP≤MoS AND Gate0≥GOOD AND Promoter≥TRUSTWORTHY AND HR=PASS | Master Role 2 decision rules | Correctly FAILED: CMP 1,232 > MoS 1,048; Promoter CAUTION < TRUSTWORTHY → no BUY NOW | PASS |
| D.2 | Verdict WATCHLIST consistent with unconfirmed transition (DEEP WATCH) | Master Role 2; Transition-Alpha Filter (good business w/o clear inflection → WATCH-FOR-INFLECTION); FTTCP +3 DEEP WATCH | WATCHLIST pending Q1 FY27 confirmation — consistent with DEEP WATCH and the inflection filter | PASS |
| D.3 | ENTRY CONJUNCTION stated and correctly applied | Master Role 2 (anti-value-trap) | Invoked to hold at WATCHLIST, but reasons from "transition unconfirmed / open trigger" — no thesis-broken trigger has actually FIRED (Q4 9.02% is not <9% for two quarters; RBI not cancelled). The conjunction (price-in-zone AND no fired trigger) is technically satisfied; WATCHLIST is carried on the DEEP WATCH / inflection-filter basis, not on a fired trigger. Conclusion correct; the conjunction invocation is imprecise. | **FAIL (MINOR)** |
| D.4 | Position size Small; promoter cap binds | Master Role 2 position rules | Medium needs Promoter TRUSTWORTHY; Large needs Gate0 EXCELLENT + EM EXPANSION. DSSL CAUTION/GOOD/MODEST → both fail; promoter CAUTION cap → **Small (2-3%)**. Correct. | PASS |
| D.5 | Tier interaction with sizing | Amendment 4.3 | Tier A (no Tier-B Medium cap); promoter cap is the binding ceiling → Small. Correct. | PASS |
| D.6 | Thesis-broken conditions present, specific and measurable | Master Role 2 verdict box | Three explicit falsifiers (margin <9% two quarters; debtor days >160 with widening tail on frozen ECL; RBI order cancelled). Specific and measurable. | PASS |

**Role 2 verdict:** Decision (WATCHLIST) and sizing (Small) are correctly derived and correctly gated by the promoter CAUTION cap. One MINOR: the ENTRY CONJUNCTION is invoked with "unconfirmed transition / open trigger" language, conflating a pending-confirmation state with a fired thesis-broken trigger; the WATCHLIST conclusion is nonetheless correct via the DEEP WATCH / inflection route.

---

## SUMMARY

Rules checked: **34**. Passed: **31**. Failed: **3** (1 MAJOR, 2 MINOR). No CRITICAL.

- **MAJOR (UA.5):** UA ×1.25 applied inside the RRM governing track, unsupported by the Master RRM formula; lifts the conservative track from ~19.5x to 24.0x, changes entry (Rs1,310 vs ~Rs1,064) / MoS (Rs1,048 vs ~Rs851) and flips the RRM base Hurdle (PASS 2.08 → CONDITIONAL 1.69). Decision WATCHLIST survives.
- **MINOR (P1.6):** B11 yaml `roce_recovery_route: "pillar1-midpoint"` mislabels a no-midpoint, route-NONE, current-ROCE-sole-anchor derivation.
- **MINOR (D.3):** ENTRY CONJUNCTION invoked on "unconfirmed transition" rather than a fired trigger; conclusion (WATCHLIST) correct via DEEP WATCH.

**Recomputed destination PE:** Additive **30.0x — CONCUR** (cap binds under either +3x/+2x Pillar 3 and either UA reading). RRM governing: reported **24.0x**; on the literal Master formula (Fundamental Base × RRM, no UA) **≈19.5x**. Both are carried below for the operator.

**Recomputed decision:** CONCUR — **WATCHLIST, Small (2-3%)**. Robust to every finding: even on RRM 19.5x, CMP sits above the entry band and the transition is unconfirmed (DEEP WATCH), so WATCHLIST holds and Small binds on the promoter CAUTION cap.

**Coverage:** Full valuation half (Pillars 1-4, UA, both tracks, Hurdle, Tier/entry) plus Role 2 decision + sizing. Gate 0 and Emerging Moat adherence were audited and recorded in phase 1 (not re-run). Source-fidelity of individual numbers is Verifier A's binding domain and is not adjudicated here.

---

```yaml
stage: B12c-valuation
company: "DSSL"
run_date: "2026-07-27"
model: claude-opus-4-8
status: complete
scope: "phase-3 valuation-adherence half + Role 2 (B14) decision/sizing; Gate0 + EmergingMoat done in phase 1 (acceptance 99%, not re-run)"
valuation:
  rules_checked: 34
  fails:
    - {rule: "UA.5 — UA x1.25 applied inside RRM governing track (Master RRM = Fundamental Base x RRM, no UA term)", severity: MAJOR}
    - {rule: "P1.6 — yaml roce_recovery_route 'pillar1-midpoint' mislabels a route-NONE, current-sole-anchor derivation", severity: MINOR}
    - {rule: "D.3 — ENTRY CONJUNCTION invoked on 'unconfirmed transition' not a fired thesis-broken trigger", severity: MINOR}
findings:
  - {severity: MAJOR, location: "B11 Section 1B RRM track / verdict card; B10 destination-PE table", rule: "Master v3.3 Role 1 RRM derivation (no UA factor); Amendment 3 codifies UA for additive Row F only", issue: "UA x1.25 inserted into RRM (governing) track lifts it from literal ~19.5x to 24.0x — less-conservative direction for the conservative track; changes entry Rs1,310 vs ~Rs1,064, MoS Rs1,048 vs ~Rs851, and flips RRM base Hurdle PASS 2.08 -> CONDITIONAL 1.69", recomputed: "RRM ~19.5x if UA excluded; additive 30.0x unchanged (cap binds)", decision_impact: "none — WATCHLIST survives either reading"}
  - {severity: MINOR, location: "B11 yaml pillar_detail.roce_recovery_route", rule: "worksheet/label fidelity", issue: "label 'pillar1-midpoint' but no midpoint computed (FY[Y+2] NOT FOUND; route NONE; current 30.17% used as sole anchor)", recomputed: "n/a", decision_impact: none}
  - {severity: MINOR, location: "B14 Section 7 verdict box / Verdict reasoning point 3", rule: "Master v3.3 Role 2 ENTRY CONJUNCTION (anti-value-trap)", issue: "conjunction invoked citing 'transition unconfirmed / open trigger' although no thesis-broken trigger has fired; WATCHLIST is correct but on DEEP WATCH / inflection-filter grounds, not a withdrawn zone", recomputed: "n/a", decision_impact: none}
concurrences:
  pillar1_base: "22.6x concur (0.5x30.17+7.5; cap24 not binding); normalization route NONE correct; single-credit respected (Strategic barred)"
  pillar2: "1.00x neutral, no growth offset (structural), SOTP carve-out not double-counted — concur"
  pillar3: "+3x concur (3a +3 order book 2.08x + SOM 33.9% + grade B; 3b/3c +0); under +6x cap"
  ua_ordering_additive: "min(25.6x1.25=32.0, cap 30.0)=30.0x concur; cap absolute; no quality uplift (durability Medium) correct"
  rrm_arithmetic: "0.76 at r=15.5% concur; percentage-point reading (Amdt 4.4) correct"
  hurdle: "formula + trailing/trailing basis consistency (SFL) correct; PASS on reported tracks (RRM 2.08 subject to UA.5)"
  tier_entry: "Tier A (FII+DII 1.36%<3%) correct; entry = FV/1.953; MoS 20% below entry — concur"
  role2: "WATCHLIST + Small correct; promoter CAUTION cap binds; BUY NOW gate correctly failed; thesis-broken conditions present"
recomputed_destination_pe: "Additive 30.0x CONCUR (cap-bound). RRM governing: reported 24.0x; literal Master formula (no UA in RRM) ~19.5x"
recomputed_decision: ""
critical_count: 0
major_count: 1
minor_count: 2
acceptance_rate: 91
```
