# VERIFIER C — FRAMEWORK ADHERENCE AUDIT (PHASE 3: VALUATION + THESIS)
## Shyam Metalics & Energy Ltd (SHYAMMETL) | Run 2026-07-19 | Model: claude-opus-4-8

**Scope this pass:** B11 (Role 1 valuation) and B14 (Role 2 thesis) against Master v3.3 Role 1/Role 2, Section 1B v3.3 Amendments, Section 1B v3.5.1 Reconciliation, and FTTCP v1.2. Gate 0 (B01) and Emerging Moat (B07) were audited in Phase 1 (acceptance 96%) and are NOT re-adjudicated here. Numbers-in-source is Verifier A's hard gate and is not re-litigated; this pass audits rule application and re-derivation logic only.

**Bottom line:** The valuation is framework-adherent on every load-bearing mechanic. The AVOID decision is robust and correctly derived. One MAJOR re-derivation discrepancy (Pillar 3b under-credited vs the EM-gated table) and three MINOR presentational/YAML-labeling gaps. Nothing changes the applied destination PE (operator-fixed 20x flat), the Hurdle verdict (STOP), or the decision (AVOID). **recomputed decision: concur (AVOID). recomputed applied destination PE: concur (20x).**

---

## A. B11 VALUATION — RULE-BY-RULE COMPLIANCE

### A1. Pillar 1 — ROCE Base Multiple (continuous formula + normalization route)

| Rule | Requirement | Applied | Verdict |
|---|---|---|---|
| Continuous Pillar 1 formula | 0.5 × ROCE + 7.5, floor 9x, cap 24x (Amendment 5) | 0.5 × 15.926 + 7.5 = 15.46 → 15.5x | PASS |
| Blended ROCE arithmetic | 60/40 current/anchor for RECOVERING 40-60% | 0.60×13.21 + 0.40×20 = 15.93% | PASS |
| Route selection (v3.5.1 Amdt 9) | Route A only if (CWIP+idle+advances) >20% of CE | CWIP 106.47 / CE 12,527.88 = 0.85% << 20% → Route A FAILS | PASS |
| Route B condition set | Denominator clean AND FTTCP TEMP DEPRESSED/RECOVERING with 📄 pre-depression history | Backward TEMP DEPRESSED, forward RECOVERING 40-60%; FY18 23.4% anchored | PASS |
| Route B anchor cap | Anchor ≤ evidenced pre-depression print, never extrapolated | Anchor 20% < evidenced 23.4% (capped below the print) | PASS |
| Route B named/dated 📄 catalyst | Specific dated unwind mechanism | Aluminium FRP Sep-26, Wagon Sep-26, DRI Mar-27 (📄 B07) | PASS |
| Route B self-withdrawal | Anchor withdrawn if recovery not printed by catalyst date +1q | Stated: next refresh after Mar-27 +1q grace | PASS |
| FTTCP ROCE sole Pillar 1 authority | Verdict as injected, no standalone re-derivation | RECOVERING 40-60% carried from deliberation/B10 | PASS |

Route selection is exactly right: CWIP ~0.85% of capital employed defeats Route A's 20% denominator test; Route B (numerator fix) is the correct route, and only one route is used (no double-normalization). Anchor conservatism (20% < the single evidenced 23.4% print) is correctly applied.

Note the retired Amendment 4.5 blend for RECOVERING 40-60% was a THREE-anchor form (40% normalized / 30% FY[Y+2] / 30% current); v3.5.1 Route B supersedes it with a 60/40 current/anchor blend, which is what B11 used. Correct — the maker applied the live v3.5.1 rule, not the retired text.

### A2. Single-credit rule

| Rule | Applied | Verdict |
|---|---|---|
| ROCE recovery credited in Pillar 1 OR Strategic Premium, never both; route stated | Credited via Pillar 1 (Route B blend); Strategic ROCE re-rating explicitly BARRED; worksheet states the route | PASS |
| No structural offset double-count | Growth offset 0; single 1.0x delivered directly | PASS |

### A3. Pillar 2 — Cash Conversion Multiplier

| Rule | Applied | Verdict |
|---|---|---|
| Multiplier matches stated determination | GROWTH-INDUCED, 1.0x provisional (operator/B10) applied as given | PASS |
| No offset stacked on a directly-delivered multiplier | Growth offset 0 (single-credit discipline noted) | PASS |
| No offset on structural | N/A — determination is growth-induced, not structural | PASS |

### A4. Pillar 3 — Growth Visibility Premium (decoupled 3a/3b/3c, +6x cap)

| Component | Framework requirement | Applied | Verdict |
|---|---|---|---|
| 3a Growth Visibility | +2x if any two 📄 qualifiers (Amdt 4.1); grade B ok | Capex-embedded growth 150% + delivery grade B = 2 qualifiers → +2x | PASS |
| **3b Moat Formation** | **EM-gated table (Amdt 4.1 "unchanged"): EM 30-39 + catalyst 0-12m + mixed evidence = +3x (Master v3.3 line 302); +4x if mostly 📄** | **+1x credited** | **FAIL (MAJOR)** |
| 3c Duration | +1x only if ≥2.5yr documented revenue tenor | +0x (no 📄 order book ≥2.5yr) | PASS |
| Combined cap | ≤ +6x | +3x total, within cap | PASS |
| Shared-catalyst flag | Flag if same capex drives Pillar 1 + Pillar 3a | Flagged SHARED CATALYST for Role 3 | PASS |

**MAJOR — Pillar 3b under-credited (line 74, worksheet).** With EM 30 (STRENGTHENING), catalyst 0-12m, and evidence stated as mixed (19 documented / 10 claim / 6 inference), the EM-gated 3b table returns **+3x** (line 302; +4x if the 54% documented share is read as "mostly documented"). B11 credited **+1x**, which is the EM 25-29 row (line 304) applied to an EM-30 company. The +1x originates in the FTTCP deliberation's provisional 3b figure and B11 faithfully carried the injected +3x Pillar 3 total, so this is not a B11 arithmetic error — but it is a framework-adherence gap on the pillar build that must surface. Correct 3b (+3x) would lift Pillar 3 to +5x, raising the self-derived additive Raw PE from 18.5x to **20.5x (capped at the 20x sector cap)** and the RRM track to ~17.4x.

**Why the decision survives:** the operator elected a 20x FLAT destination that SUPERSEDES the entire pillar build. The applied destination (20x), the fair values (867/913/1,006), the Hurdle Ratio (STOP), and the decision (AVOID) are all unchanged. The under-credit only understates the "for the record" self-derived additive track, and even corrected that track caps at 20x. Direction of the error is conservative (biases toward AVOID). Hence MAJOR, not CRITICAL: the number is wrong but the decision is robust.

### A5. Strategic Premium

| Rule | Applied | Verdict |
|---|---|---|
| ROCE re-rating route barred once credited in Pillar 1 | +0x, barred (single credit) | PASS |
| No rare licence/monopoly claimed without evidence | +0x (safeguard duty provisional, PLI lapsed) | PASS |

### A6. Undiscovered Alpha (Amendment 3 ordering)

| Rule | Applied | Verdict |
|---|---|---|
| Order: F2 = Raw × 1.25, then H = min(F2, cap) | Row F2 present; UA not qualified so F unchanged | PASS |
| All three qualifiers required | listed ≥12m ✓; Gate0≥60 OR EM≥25 (EM 30 ✓); FII+DII <3% ✗ (~16.7%) → all_met false | PASS |
| UA never breaches sector cap | Not applied | PASS |

UA correctly NOT applied: FII+DII ~16.7% > 3% ceiling defeats the institutional-absence qualifier. This is the required outcome per the task's own read.

### A7. Sector cap

| Rule | Applied | Verdict |
|---|---|---|
| Sector cap is absolute ceiling | 20x (commodity-cyclical integrated steel); H = min(18.5, 20)=18.5x | PASS |
| Manifest 38x (Pharma/CDMO) not used | Overridden; 20x used; 38x never touched | PASS |

### A8. RRM dual-track derivation (Amendment 4.4 units)

| Rule | Applied | Verdict |
|---|---|---|
| r build: mid-cap 13% base + adjustments, bound [9,18] | 13 + gov 1.25 + durability 0.5 = 14.75% (in bounds) | PASS |
| RRM percentage-point reading | 1 + (13.5 − 14.75) × 0.12 = 1 − 0.15 = 0.85 (pp, not decimal) | PASS |
| RRM bounds ×0.70–×1.60 | 0.85 in bounds | PASS |
| Track 1 destination | 18.5 × 0.85 = 15.7x | PASS |
| Both tracks carried through fair values + verdict card | Additive 18.5x and RRM 15.7x both present in card and YAML | PASS |
| >15% divergence handling | (18.5−15.7)/18.5 = 15.1% > 15%; RRM named more conservative | PASS (see note) |

**Note (not scored a fail):** on a self-derived basis the >15% divergence rule nominates the more conservative RRM track (15.7x) to set the entry zone. B11 instead computes entry from the operator-approved 20x FLAT (base FV 913 → entry 468). This is the correct precedence — the operator override is authoritative and explicitly supersedes both tracks (deliberation Override 1) — but it produces a HIGHER (less conservative) entry than the conservative-track rule alone would. Immaterial to AVOID (CMP 1,022 is ~2.2x the top of any entry range). The maker flagged the tension transparently.

### A9. Hurdle Ratio (Amendment 2 / Amendment 4.3 Tier A)

| Rule | Applied | Verdict |
|---|---|---|
| HR = (1+EPS CAGR)³ × (Dest PE mid ÷ Current PE) | 1.18³ × (20/26.41) = 1.643 × 0.757 = 1.24 base; 1.30³ × 0.757 = 1.66 bull | PASS |
| Tier A threshold 1.953 | Both < 1.953 → STOP | PASS |
| Current PE basis (trailing) | 1,022 / 38.70 trailing FY26 diluted = 26.41x | PASS |
| Bull-row credibility gate | Bull permitted only if grade A/B; grade B → bull used | PASS |
| STOP definition (bull < 1.953) | HR(bull) 1.66 < 1.953 → STOP correctly declared | PASS |

HR correctly computed on the applied 20x, and additionally shown STOPping on both self-derived tracks (18.5x bull 1.54; 15.7x bull 1.31) — STOP is robust to the destination choice.

### A10. Operator-approved inputs (deliberation honored)

| Operator ruling | Requirement | Applied | Verdict |
|---|---|---|---|
| Exit PE 20x FLAT | Applied as single flat destination to fair values | 20x on FY27E EPS → 867/913/1,006 | PASS |
| FORWARD earnings basis | 20x on one-year-forward FY27E EPS | FY27E derived 38.70 × growth; base 45.67 | PASS (see MINOR-2) |
| Tier A, 25% (divisor 1.953) | Tier B barred (promoter CONCERN fails Tier B quality gate) | Tier A applied; Tier B correctly barred | PASS |
| Cash 1.0x growth-induced | Applied 1.0x | PASS |
| Pillar 3 ~+3x | Applied +3x total | PASS (component 3b under-table — see MAJOR) |
| UA not applied | all_met false | PASS |
| Sector cap 20x, 38x overridden | 20x used | PASS |

### A11. Section 2/4 mechanics

| Rule | Applied | Verdict |
|---|---|---|
| Entry = base fair value ÷ 1.953 (Tier A) | 913 / 1.953 = 468 | PASS |
| MoS = 20% below entry | 468 × 0.80 = 374 | PASS |
| 4D probability weights = grade B (25/50/25) | 25/50/25 applied | PASS |
| Expected CAGR arithmetic | 0.25(−5.3)+0.50(−3.7)+0.25(−0.5) = −3.3% | PASS |
| SOM cross-check performed | Section 2D: ~16-18% rev vs SOM 14.8%, flagged justified | PASS |
| 4G exit-multiple validation performed | All six checks run | PASS |

---

## B. B14 THESIS — DECISION-RULE & POSITION-SIZE COMPLIANCE

| Rule (Master v3.3 Role 2) | Requirement | Applied | Verdict |
|---|---|---|---|
| AVOID triggers | Gate0 AVERAGE/AVOID OR Promoter CONCERN OR U/D<2x OR HR STOP | All four present; verdict AVOID | PASS |
| Decision-rule trace | State which rule(s) force the verdict | Three independent rules traced + U/D 0.7x noted | PASS |
| Entry = FV / hurdle divisor | 913 / 1.953 = 468; range 416-468 | Matches Role 1 | PASS |
| MoS 20% below entry | 374 | Matches Role 1 | PASS |
| Position size vs verdict | AVOID → zero deployed; Promoter CONCERN cap binds | "Small" recorded as ceiling under the cap, ZERO deployed today; override field empty | PASS |
| Entry conjunction (anti-value-trap) | Must be stated in Section 7 box | Stated (price-in-zone AND no trigger fired) | PASS |
| Upside/Downside disclosed | 0.7x < 2x flagged | PASS |
| Return matrix summary | cells ≥25% and ≥15% | 0/9 and 0/9 | PASS |
| Thesis-broken triggers measurable | Specific/measurable | ROCE, FG-inventory, ED-PMLA triggers all measurable | PASS |
| 5yr target | Do not estimate if not produced | Marked NOT COMPUTED (Role 1 built 3yr) | PASS |

Position-size logic is consistent and correctly reasoned: the framework assigns sizes only to BUY verdicts, so an AVOID deploys zero; recording "Small" as the maximum ceiling that would ever apply (matching the operator's cautious disposition and the Promoter CONCERN cap) with zero deployed today is internally consistent and correctly leaves position_size_override empty (no override is being taken). No inconsistency between the AVOID verdict, the flags, and the sizing.

---

## C. FINDINGS

| # | Severity | Location | Description |
|---|---|---|---|
| 1 | MAJOR | B11 Pillar 3b (line 74; verdict card line 303; YAML growth_premium) | Pillar 3b credited +1x; EM-gated 3b table (EM 30-39 + catalyst 0-12m + mixed evidence, Master v3.3 line 302) returns +3x (+4x if "mostly documented"). Under-credit originates in the deliberation's provisional 3b and was honored by B11. Correct 3b lifts self-derived additive Raw PE 18.5x → 20.5x (cap 20x), RRM ~17.4x. NO change to applied destination (operator 20x flat supersedes the build), Hurdle (STOP), or decision (AVOID). Conservative-direction error; decision robust. |
| 2 | MINOR | B11 YAML `pillar_detail.roce_recovery_route: "pillar1-midpoint"` | Mislabels the Route B 60/40 current/anchor blend as "midpoint." "Midpoint" is the FTTCP >60%-Strong case; this is the 40-60% weighted case. Narrative (Section 1B) is correct; only the YAML tag is imprecise. |
| 3 | MINOR | B11 YAML `fair_values.track1` and `track2` | Both keys carry {867/913/1,006}, which are the operator-applied 20x fair values, not the track-specific values. Report body correctly states Track 1 (RRM 15.7x) = 680/717/790 and Track 2 (Additive 18.5x) = 802/845/931. A downstream YAML consumer reading fair_values.track1 would get the wrong RRM-track number. Governing (applied) values and the body are correct; decision unaffected. |
| 4 | MINOR | B11 Section 4C / verdict card; B14 Section 5 | Horizon labeling: 20x is applied to FY27E (one-year-forward) EPS, producing a ~1-year-forward fair value, but 4C and the thesis treat 913 as a "Year 3 target" and compute a 3-year CAGR, and entry divides that 1-yr-forward FV by the 3-yr divisor 1.953. This is operator-directed (forward-basis election) and the deliberation framed it identically ("20x forward implies fair value ~960-1,000... 25% hurdle entry lands well below CMP"); it is conservative and does not change AVOID. Flagged for horizon-consistency transparency. |

**No CRITICAL findings.** No finding flips the Hurdle verdict (STOP holds on all three destination bases) or the decision (AVOID is forced independently by Gate 0 AVOID, Promoter CONCERN, HR STOP, and U/D 0.7x).

---

## D. RE-DERIVATION SUMMARY

- **Applied destination PE:** concur — 20x flat (operator override, correctly applied and supersedes the pillar build).
- **Self-derived pillar build (for the record only):** additive 18.5x is understated; correct EM-gated 3b (+3x) gives 20.5x → capped at 20x. RRM 15.7x → ~17.4x. Neither flows to fair values or the decision.
- **Hurdle Ratio:** concur — base 1.24 / bull 1.66, STOP; robust across 20x / 18.5x / 15.7x.
- **Decision:** concur — AVOID, redundantly forced.
- **Entry / MoS:** concur — 468 / 374 arithmetically correct given the operator-approved 20x base.

```yaml
stage: B12c-valuation
company: "SHYAMMETL"
run_date: "2026-07-19"
model: claude-opus-4-8
status: complete
scope: "phase-3 valuation-adherence (B11 Role 1 + B14 Role 2); Gate 0 (B01) and Emerging Moat (B07) done in phase 1, not re-audited"
gate0: {rules_checked: 0, fails: []}   # out of scope this pass (phase 1)
emoat: {rules_checked: 0, fails: []}   # out of scope this pass (phase 1)
valuation:
  rules_checked: 43
  fails:
    - {rule: "Pillar 3b EM-gated table", severity: "MAJOR", expected: "+3x (EM 30-39/0-12m/mixed; +4x if mostly documented)", applied: "+1x", decision_impact: "none — operator 20x flat supersedes pillar build; HR STOP and AVOID unchanged"}
    - {rule: "YAML roce_recovery_route label", severity: "MINOR", note: "labels Route B 60/40 blend as 'pillar1-midpoint'; narrative correct"}
    - {rule: "YAML fair_values track labeling", severity: "MINOR", note: "track1/track2 both show applied-20x values 867/913/1006, not track-specific (RRM 680/717/790; additive 802/845/931); body correct"}
    - {rule: "forward-basis horizon labeling", severity: "MINOR", note: "20x on FY27E (1yr-fwd) EPS treated as Year-3 target in 4C/thesis; operator-directed, conservative, decision unaffected"}
recomputed_destination_pe: "applied 20x — concur (unchanged). Self-derived additive 18.5x understated → 20.5x (cap 20x) if 3b credited at EM-gated +3x; does not flow to applied destination or decision."
recomputed_decision: ""   # concur — AVOID
findings:
  - {severity: "MAJOR", location: "B11 Pillar 3b / worksheet line 74 / card line 303", description: "3b credited +1x vs EM-gated +3x (EM 30-39/catalyst 0-12m/mixed evidence); conservative under-credit carried from deliberation; corrects additive to 20.5x cap 20x; no change to applied 20x destination, HR STOP, or AVOID"}
  - {severity: "MINOR", location: "B11 YAML pillar_detail.roce_recovery_route", description: "'pillar1-midpoint' mislabels the Route B 40-60% 60/40 current/anchor blend; narrative correct"}
  - {severity: "MINOR", location: "B11 YAML fair_values.track1/track2", description: "both keys hold the applied-20x values, not the track-specific RRM/additive fair values shown correctly in the report body; downstream YAML consumers would be misled; decision unaffected"}
  - {severity: "MINOR", location: "B11 Section 4C / B14 Section 5", description: "20x applied to FY27E (one-year-forward) EPS but used as a 3-year target and divided by the 3-year hurdle divisor; operator-directed forward basis, conservative, does not change AVOID"}
critical_count: 0
major_count: 1
minor_count: 3
acceptance_rate: 91   # 39 of 43 valuation+thesis rules passed clean
coverage_note: "Audited B11 Pillars 1-3 + Strategic + UA + sector cap + RRM dual-track + Hurdle Ratio + entry/MoS/4D + operator-override application, and B14 decision rules + position sizing + entry conjunction. Gate 0 and Emerging Moat out of scope (phase 1). Source-number existence is Verifier A's gate, not re-adjudicated. Decision AVOID and applied destination 20x confirmed; the single MAJOR is a superseded-pillar-build under-credit with zero decision impact."
```
