# VERIFIER C — FRAMEWORK ADHERENCE (VALUATION SCOPE, PHASE 3): AYE FINANCE LIMITED

**Run date:** 2026-07-23 | **Model:** claude-opus-4-8 | **Scope:** deferred VALUATION-ADHERENCE audit only
**Artifacts audited:** B10-valinputs (10-valinputs.md), B11-valuation (11-valuation.md), B14-thesis (14-thesis.md)
**Authorities:** Master v3.3 (Role 1 + Role 2), Section 1B v3.3 Amendments (5/6/7/8, 3, 4, 4.1-4.4), Section 1B v3.5.1 Reconciliation (Route A/B), FTTCP v1.2, run deliberation record (fttcp-deliberation.md, operator-approved pillars).

> Gate 0 (B01) and Emerging Moat (B07) adherence were audited in Phase 1 and are NOT re-opened here. This report covers the valuation half only.

Governing principle applied per task: a disclosed lender-substitution or the operator-approved exit PE is NOT a deviation. NOT FOUND is valid. I audited rule application, not company quality and not raw source numbers (Verifier A owns numbers).

---

## 1. PILLAR 1 — ROE NORMALIZATION (LENDER, Amendment 7 + Amendment 5 + v3.5.1)

| Rule | Expected | Found (B11 s3a / B10) | Verdict |
|---|---|---|---|
| Uses ROE not ROCE | ROE form for leveraged financial (Amendment 7) | ROE anchor 11.7-13%, ROCE explicitly rejected as not meaningful for a lender | PASS |
| Continuous formula 0.5×ROE+7.5 | floor 9x, cap 24x (Amendment 5) | 11.7%→13.4x, 13.0%→14.0x, 12.35%→13.7x | PASS (recomputed: 13.35/14.0/13.675 — matches to 1 dp) |
| Floor/cap binding? | 9x / 24x | 13.4-14.0x, neither binds | PASS |
| Route selection A vs B (v3.5.1) | Route A where post-IPO idle-capital denominator distortion >20% CE; if both hold, A governs, B "suppressed per single-credit" noted | Route A governs (post-IPO excess capital stripped, net proceeds ~Rs 672 Cr vs NW ~Rs 2,533 Cr ≈ 26.5%); Route B condition present but suppressed; declared on worksheet line | PASS |
| Recovery credited via Pillar 1 only | Strategic Premium barred (Amendment 4 single-credit) | Strategic = +0x; recovery in Pillar 1 midpoint; declared | PASS |
| No double-credit within Pillar 1 | anchor not lifted to operational 15% while also crediting recovery | Anchor capped at 11.7-13% (deliberation line 50 explicitly bars the double-count) | PASS |

**Pillar 1 verdict: fully compliant.** The lender substitution (ROE for ROCE) is the Amendment 7 carve-out, disclosed. Route A/B handled exactly per the v3.5.1 route-selection rule, with the single-credit suppression of Route B stated. The recovery is credited once.

---

## 2. PILLAR 2 — LENDER ASSET-QUALITY MULTIPLIER (Amendment 7)

| Rule | Expected | Found | Verdict |
|---|---|---|---|
| Multiplier applied | per band table | 1.00x (Sound) | see note |
| Band assignment vs evidence | 1.00x Sound requires **GNPA 2-4% and stable**, PCR 60-70%, credit costs within guided band | GNPA **4.49% (>4%)**, PCR 63.8% (in band), ECL 3.4x floor, GNPA falling 4 qtrs | **MINOR** (band stretch, operator override) |
| No growth offset | loan growth cannot offset underwriting | Stated explicitly: "No growth offset (Amendment 7)" | PASS |

**Note (F-1, MINOR).** GNPA 4.49% is above 4%, which by the strict Amendment 7 band table lands in the **0.80x Stressed** row ("GNPA rising OR >4%"), not the 1.00x Sound row (GNPA 2-4%). The draft correctly carried 0.80x. The 1.00x is an **operator override** ratified through the approved 15x destination (deliberation lines 26, 29, 51: "The operator's 15x therefore rules the asset-quality multiplier up to 1.00x"), disclosed in B10 (Pillar 2 table) and B11 (s3a, FTTCP gate). Per the audit rule that an operator-approved input is not a deviation, this is NOT a framework breach; it is logged as MINOR for transparency because the band, read strictly, is a marginal miss (4.49% vs 4.00% ceiling) resting on an override rather than a clean band fit. The "no growth offset" rule is correctly honoured.

---

## 3. PILLAR 3 — GROWTH & DURATION ADDITIVE (Amendment 4.1/4.2)

| Rule | Expected | Found | Verdict |
|---|---|---|---|
| 3a growth visibility | +2x if ≥2 qualifiers; grade C caps 3a at +2x | +2x on documented ~26% AUM machinery, "capped at +2x by delivery grade C" | **MINOR** (thin qualifier count) |
| 3b moat formation | EM-gated; EM<25 → +0x | +0x (EM 19.6 MODEST) | PASS |
| 3c duration | 📄 contracted revenue ≥2.5yr → +1x | +0x (no contracted revenue; lender has no order book) | PASS |
| Combined ≤ +6x cap | hard cap | +2x total | PASS |

**Note (F-2, MINOR).** Under a strict Amendment 4.1 read, of the four 3a qualifiers only capex-embedded growth ≥15% (B07: 84%) cleanly qualifies. The SOM-implied 3-yr AUM CAGR is 18.3% (B09), which fails the ≥20% qualifier; management delivery grade is C, which fails the A/B qualifier. Two clean qualifiers are needed for +2x. The +2x therefore rests on the lender-substitution of the documented ~26% AUM growth machinery as the "growth visibility" evidence, and is operator-ratified (deliberation line 52). Disclosed. It is **immaterial to the destination PE actually used**, which is the operator-fixed 15x, not the additive output — but it is what lets B11 characterise the additive as 15.4-16.0x and the approved 15x as "sitting at the additive floor / conservative." Had 3a been read strictly at +0x, the additive would be 13.4-14.0x and the approved 15x would sit *above* the additive track. This does not change the governing 15x, the hurdle, or the decision.

---

## 4. STRATEGIC PREMIUM, UNDISCOVERED ALPHA, SECTOR CAP

| Rule | Expected | Found | Verdict |
|---|---|---|---|
| Strategic premium | +0x, barred by single-credit | +0x (barred) | PASS |
| UA three-qualifier test | listed≥12m AND (Gate0≥60 OR EM≥25) AND FII+DII<3% | listed ~5.5m (fail), Gate0 59 & EM 19.6 (fail), FII+DII 35.45% (fail) → NOT applied | PASS |
| UA ordering | min(F×1.25, Cap), shown as F2 row before cap | F2 row present, ×1.25 not applied (not qualified) | PASS |
| Sector cap absolute | 18x Banks/NBFCs/MFIs (Amendment 8) | 18x; min(F2,G) not binding; 15x approved well within | PASS |

UA correctly not applied on the FII+DII 35.45% test (fails <3%); the CLAUDE.md Amendment-3 protection (never treat low institutional ownership as a risk) is not engaged because ownership is high, not low. Sector cap not breached on any track.

---

## 5. DESTINATION PE, DUAL TRACK, DIVERGENCE

| Rule | Expected | Found | Verdict |
|---|---|---|---|
| Operator-approved 15x authoritative | forward basis, FY29; not re-derived to a different exit PE | 15x used for all fair values, entry, hurdle | PASS |
| Applied within sector cap | ≤18x | 15x ≤ 18x | PASS |
| RRM percentage-point formula (Amendment 4.4) | 1+(13.5−r)×0.12, bounds 0.70-1.60 | r15.5%→0.76; 13.7×0.76=10.4x; r15/16 give 11.2x/9.6x | PASS (recomputed, matches) |
| Divergence SHOWN not silently reconciled | conservative track shown; operator override disclosed | s3c/s3d + FLAG-RRM-DIVERGENCE: additive 15.7x vs RRM 10.4x, ~31-34% divergence, RRM AVOID-on-valuation flagged | PASS |
| Both tracks carried through | fair values + verdict card | Track 1 (188/225/260) and Track 2 (272/324/375) in s5, triangulation, verdict card | PASS |
| Conservative-track-on->15%-divergence default | governed by disclosed operator override at the valuation approval gate | Operator approved 15x; deliberation line 56 explicit it does not override; B11 obeys and flags | PASS |

The >15% divergence would normally hand the entry zone to the conservative RRM track. The operator-approved 15x supersedes at the valuation approval gate (deliberation lines 30, 56), is disclosed, and both tracks are carried through with the RRM AVOID-on-valuation counterpoint flagged for synthesis. This is compliant, not a deviation.

---

## 6. HURDLE RATIO (SFL consistent-basis lesson)

| Rule | Expected | Found | Verdict |
|---|---|---|---|
| Formula | (1+EPS CAGR)³ × (Dest PE ÷ Current PE) | applied | PASS |
| Consistent EPS basis num/denom | forward/forward (SFL lesson) | Current PE = CMP/FY27E fwd EPS = 15.4x; Dest PE 15x forward — both forward | PASS |
| Base/Bull math | pass threshold 1.953 (Tier A) | base 1.77 FAIL, bull 2.00 PASS | PASS (recomputed 1.771 / 1.997) |
| Bull grade-C cap | base+5% max when grade C/D | bull capped at 27% (=22+5); true 28% used only for target | PASS |
| Verdict mapping | HR(base)<1.953 & HR(bull)≥1.953 → CONDITIONAL, cap WATCHLIST/BUY-ON-DIPS, no BUY NOW | CONDITIONAL, flagged "growth-dependent with de-rating headwind" | PASS |
| Proportional ±7.5% range (Amendment 6) | value ±7.5% | 15.7±7.5% = 14.5-16.9x | PASS (immaterial rounding at top end) |
| Tier A divisor 1.953 | entry = base FV / 1.953; MoS 20% below | 324/1.953 = 166; MoS 133 | PASS |
| 4D weights match grade C | 35/45/20 | 35/45/20; prob-weighted CAGR 19.7% | PASS (recomputed 19.74%) |

The Hurdle keeps a forward EPS basis on both numerator and denominator — the exact SFL failure mode is avoided. All hurdle math verified.

---

## 7. SOM CROSS-CHECK (Master Role 1)

**Finding F-3 (MAJOR).** The SOM cross-check was performed (B11 s4) but against the wrong benchmark. B11 checks base EPS CAGR 22% (base-case driver AUM ~25%) against "the documented AUM-growth machinery (25-28%)" and concludes "Assumption does not exceed the SOM-implied growth → consistent (no cut required)." However, the framework-disciplined **SOM-implied 3-yr AUM CAGR is 18.3%** (B09, carried in B14 s3E), not 25-28%. The base-case AUM growth assumption (~25%) **exceeds** the SOM-implied capacity figure. Under the Master Role 1 SOM discipline the cross-check should have flagged the exceedance and either cut the growth assumption or explicitly justified using the historical-delivery rate over the SOM-capacity ceiling. The sentence "does not exceed the SOM-implied growth" is inaccurate with respect to the 18.3% figure; B11 substituted the delivered/guided machinery range (25-28%) for the SOM-implied capacity number and never engaged the 18.3%.

Materiality: this does NOT change the operator-fixed destination PE (15x). If the 18.3% SOM ceiling governed and propagated to EPS, the base EPS CAGR would fall, the base target/entry would compress, and the Hurdle could tighten from CONDITIONAL toward STOP (bull-capped HR would drop below 1.953). The propagation is not clean because a material part of the forward EPS recovery is RoA/credit-cost driven and partly independent of AUM growth, so I do not affirmatively re-derive a STOP. The actionable outcome (not a buy at CMP; WATCHLIST) survives either reading. Classified MAJOR because a required cross-check reached "consistent" on the wrong benchmark, with a plausible path to flipping the Hurdle verdict.

---

## 8. ROLE 2 (B14) — DECISION RULES AND POSITION SIZING (Master Role 2)

| Rule | Expected | Found (B14 s7) | Verdict |
|---|---|---|---|
| Hurdle CONDITIONAL cap | WATCHLIST/BUY-ON-DIPS, no BUY NOW | Applied; BUY NOW failed on 3 counts | PASS |
| Gate 0 <60 default | WATCHLIST regardless of narrative (Master line 915) | Applied (59/160 → WATCHLIST) | PASS |
| "Both paths converge on WATCHLIST" claim | — | Master line 809 lists "Gate 0 AVERAGE/AVOID" as an AVOID trigger | **MINOR** (see F-4) |
| Position size — Large | Gate 0 EXCELLENT required | Blocked (AVOID) | PASS |
| Position size — Medium | Gate 0 GOOD+ and CMP≤entry | Blocked (both fail) | PASS |
| Position size — Small | ceiling for else that qualifies, applied in-zone only | Small (2-3%), starter tranche, in-zone only | PASS |
| Tier A (not Tier B) | no Tier-B Medium ceiling logic mis-imported | Tier A, divisor 1.953 | PASS |
| Promoter cap | TRUSTWORTHY imposes no cap | Correctly no cap | PASS |
| Entry conjunction (anti-value-trap) | stated in verdict box | Stated (price zone AND no thesis-broken trigger) | PASS |
| Operator sizing override | honour if recorded | NONE recorded; framework rule unmodified | PASS |

**Finding F-4 (MINOR).** B14 s7 states "Both paths converge on WATCHLIST (BUY-ON-DIPS)." Master line 809's decision table lists "AVOID: Gate 0 AVERAGE/AVOID OR ..." — AYE's Gate 0 classification is AVOID (an AVERAGE core one-tier downgraded on listing recency). A strict reading of line 809 would push the verdict to AVOID, not WATCHLIST, so the two rules do NOT cleanly "converge." The WATCHLIST(BUY-ON-DIPS) verdict is nonetheless independently and correctly supported by (a) the CONDITIONAL-hurdle cap (Amendment 2, which yields WATCHLIST/BUY-ON-DIPS as the ceiling and forecloses BUY NOW) and (b) Master line 915 (sub-60 defaults to WATCHLIST "regardless of narrative quality"), consistent with the transition-alpha strategy's treatment of listing-recency Gate 0 downgrades (FLAG-GATE0). The verdict stands; only the "converge" wording overclaims by glossing the line-809 AVOID trigger, which was not reconciled on the page. Presentational.

Position-sizing logic is fully correct: Gate 0 AVOID mechanically blocks Large (needs EXCELLENT) and Medium (needs GOOD+), leaving Small as the ceiling, applied only inside the entry zone. Promoter TRUSTWORTHY imposes no cap. No operator sizing override exists and none was invented.

---

## 9. FTTCP GATE, DOUBLE-CREDIT, FORWARD-EPS DISCIPLINE

| Rule | Expected | Found | Verdict |
|---|---|---|---|
| INDETERMINATE cash → cap at PROCEED WITH CAVEATS, evidence named (CLAUDE.md) | never silently PROCEED | s7: PROCEED WITH CAVEATS; missing evidence named (normalized PAT ex-derecognition, FY27 audited PAT) | PASS |
| One improvement / one mechanism | no double-credit | Recovery via Pillar 1 only; Strategic barred; Pillar 2 neutral 1.00x; Pillar 3a on AUM volume (distinct); shared-catalyst flagged | PASS |
| Forward EPS unresolved handled by conservative rule | labelled projection, never an anchor, no silent fill | FY27E EPS ~Rs 11.90 built as labelled projection off anchored base, stress-noted Rs 270-290 Cr downside; flagged in input_gaps | PASS |

---

## 10. RECOMPUTED VALUES

I do not re-derive the destination PE: the operator-approved **15x forward** is authoritative from the deliberation and was applied within the 18x cap; the additive (recomputed 15.4-16.0x) and RRM (recomputed 9.6-11.2x) tracks reproduce the reported values. **Recomputed destination PE: concur (15x).**

I do not re-derive the decision: **WATCHLIST (BUY-ON-DIPS)** stands, supported by the CONDITIONAL hurdle cap and Master line 915. Caveat carried, not a recompute: the SOM benchmark finding (F-3), if the 18.3% ceiling governed and fully propagated, could tighten the Hurdle toward STOP and the fair value/entry downward; the at-CMP action (do not buy) is unchanged under either reading. **Recomputed decision: concur (WATCHLIST / BUY-ON-DIPS).**

---

## 11. SUMMARY

Valuation-scope rules checked: 40. Fails: 4 (1 MAJOR, 3 MINOR). Acceptance rate 90%.

- The four-pillar mechanics, the Hurdle Ratio (consistent forward basis, SFL lesson honoured), the RRM percentage-point formula, the dual-track divergence disclosure, the UA test, the sector cap, the single-credit/one-mechanism discipline, the FTTCP-gate cap, and the Role 2 decision-rule and position-sizing logic are all applied correctly.
- The one MAJOR is the SOM cross-check benchmarked against 25-28% instead of the framework-disciplined 18.3% SOM-implied AUM CAGR.
- The three MINORs (Pillar 2 band stretch via operator override, thin Pillar 3a qualifier count, and the Role 2 "convergence" overclaim) are all disclosed, operator-ratified or textually supported, and none changes the operator-fixed 15x destination PE or the WATCHLIST decision.

No CRITICAL findings. No fabricated inputs. The operator-approved exit PE and the disclosed lender substitutions are not treated as deviations.

---

```yaml
stage: B12c
scope: valuation-adherence-phase3
company: "AYE"
run_date: "2026-07-23"
model: claude-opus-4-8
status: complete
valuation:
  rules_checked: 40
  fails:
    - "F-3 SOM cross-check (B11 s4): benchmarked base AUM ~25% / EPS CAGR 22% against 'documented machinery 25-28%' and declared 'does not exceed SOM-implied'; framework-disciplined SOM-implied 3yr AUM CAGR is 18.3% (B09/B14 s3E). Base assumption exceeds SOM ceiling; cross-check should have flagged/cut."
    - "F-1 Pillar 2 band (B11 s3a): GNPA 4.49% (>4%) strictly maps to 0.80x Stressed, not 1.00x Sound (GNPA 2-4%); 1.00x is disclosed operator override reconciling approved 15x."
    - "F-2 Pillar 3a (B11 s3b): +2x rests on lender-substitution of ~26% AUM machinery; under strict Amendment 4.1 only capex-embedded >=15% cleanly qualifies (SOM-implied 18.3% fails >=20%; grade C fails A/B). Immaterial to operator-fixed 15x."
    - "F-4 Role 2 decision rule (B14 s7): 'both paths converge on WATCHLIST' overclaims; Master line 809 lists Gate 0 AVERAGE/AVOID as an AVOID trigger not reconciled. Verdict stands via CONDITIONAL-hurdle cap + Master line 915."
findings:
  - {severity: "MAJOR", location: "B11 s4 (SOM cross-check)", description: "SOM cross-check reached 'consistent' against a 25-28% documented-machinery benchmark instead of the framework-disciplined 18.3% SOM-implied 3yr AUM CAGR (B09); base AUM ~25% exceeds the SOM ceiling and should have triggered a cut or explicit justification. Does not change operator-fixed 15x; could tighten Hurdle toward STOP if propagated; at-CMP 'no buy' action survives."}
  - {severity: "MINOR", location: "B11 s3a / B10 Pillar 2", description: "Asset-Quality Multiplier 1.00x (Sound) applied where GNPA 4.49% (>4%) strictly falls in the 0.80x Stressed band; the 1.00x is a disclosed, operator-ratified override reconciling the approved 15x (deliberation lines 29, 51). Not a deviation per audit rules; logged for transparency. No growth offset applied (correct)."}
  - {severity: "MINOR", location: "B11 s3b / deliberation line 52 (Pillar 3a)", description: "3a growth visibility +2x rests on the lender-substitution of documented ~26% AUM growth; under strict Amendment 4.1 only capex-embedded >=15% cleanly qualifies (SOM-implied 18.3% fails >=20%; grade C fails A/B). Operator-ratified and disclosed; immaterial to the operator-fixed 15x, but it is what lets the additive read as 15.4-16.0x supporting the 15x as 'conservative'."}
  - {severity: "MINOR", location: "B14 s7 (Role 2 decision-rule trace)", description: "'Both paths converge on WATCHLIST' overclaims: Master line 809 lists Gate 0 AVERAGE/AVOID as an AVOID trigger that a strict reading would push to AVOID and that was not reconciled. Verdict WATCHLIST(BUY-ON-DIPS) is independently correct via the CONDITIONAL-hurdle cap (Amendment 2) and Master line 915 (sub-60 default). Presentational."}
recomputed_destination_pe: ""   # concur: operator-approved 15x forward, applied within 18x cap; additive 15.4-16.0x and RRM 9.6-11.2x reproduced
recomputed_decision: ""         # concur: WATCHLIST (BUY-ON-DIPS); supported by CONDITIONAL-hurdle cap + Master line 915
critical_count: 0
major_count: 1
minor_count: 3
acceptance_rate: 90             # 36 of 40 valuation-scope rules passed
```
