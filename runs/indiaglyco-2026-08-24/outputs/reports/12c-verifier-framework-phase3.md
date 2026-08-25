# VERIFIER C — FRAMEWORK ADHERENCE, PHASE 3 (VALUATION-ADHERENCE AUDIT)
**INDIA GLYCOLS LTD (INDIAGLYCO)** | Run: runs/indiaglyco-2026-08-24 | Model: claude-opus-4-8
Scope: B11 (Role 1 valuation) + B10 (assembly) against the Section 1B layer set, EXTENDED to B14 (Role 2) decision rules and position sizing against Master v3.6.
Gate 0 (B01) and Emerging Moat (B07) were audited in phase 1 and are NOT re-audited here.

Rule sources read: Master_Project_Prompt_v3_6.md (Role 1 + Role 2); Section_1B_v3.3_Amendments.md; Section_1B_v3_5_1_Reconciliation.md; Section_1B_v3_6_Amendments.md; Section_1B_v3_7_Amendments.md; Section_1B_v3_8_Amendments.md; FTTCP_v2_1_Consolidated.md.
Artifacts audited: B10-valinputs.yaml + 10-assembly.md; B11-valuation.yaml + 11-valuation.md; B14-thesis.yaml + 14-thesis.md.
I audit rule application only. Number existence in source PDFs is Verifier A's gate; I do not clear or override it. Internal computation consistency (a value rolled against its own stated basis) is framework application and is in scope.

---

## 1. PILLAR 1 (continuous formula, converter smoothing, single-credit)

| Check | Rule | Result |
|---|---|---|
| Entity A base PE = 0.5×13+7.5 = 14.0x | Amdt 5 / Amdt 11 | PASS (arith correct) |
| Entity B base PE = 0.5×24+7.5 = 19.5x | Amdt 5 | PASS |
| Entity C base PE = 0.5×9.4+7.5 = 12.2x | Amdt 5 | PASS |
| Ceiling 30x (v3.6 Amdt 11), not old 24x | Amdt 11 | PASS (no old 24x cap applied) |
| Converter through-cycle ROCE used, spot never the input; both numbers shown | 17.1 / CLAUDE.md NEVER | PARTIAL — disclosure PASS; input VALUE flagged (F5) |
| Single-credit: recovery via Pillar 1 midpoint, Strategic +0, route stated | Amdt 4 / v3.5.1 | PASS (route: "17.1 through-cycle governs; no v3.5.1 Route A/B") |
| No rupee-denominated WC / spot ROCE fed to 1B/FTTCP for the converter | 17.1 / 17.2 / CLAUDE.md | PASS |

**F5 (MAJOR).** Entity A through-cycle ROCE **13%** exceeds the evidenced 2-year ROCE range (B01: ~9% FY25, ~10-12% FY26) and is not reconciled to 17.1's prescribed method. 17.1 requires the 5-7 year average, or the midpoint of current and cycle-trough where listed history is shorter; with the flagged 2-year balance-sheet window the midpoint of current (~12%) and Q1 trough (~4.3%) is ~8%, not 13%. Using 13% inflates the quality base above any figure the company has printed. Decision impact limited: the destination is operator-approved at 14.5x additive verbatim and governs by override, so the ROCE-to-base derivation is largely cosmetic to the final number, but the 17.1 method is not satisfied. Location: 11-valuation.md Entity A Pillar 1; B10 entity_a.roce_through_cycle_pct.

---

## 2. PILLAR 2 (cash multiplier, input-price fork)

| Check | Rule | Result |
|---|---|---|
| Entity A INPUT-PRICE-DRIVEN neutral 1.00x, justified by the volume test | 17.2 | PASS (WC-per-tonne stable while WC-in-rupees swings on MEG price; no offset, no penalty) |
| Cash-quality trend denominated on volumes, not spread | 17.2 | PASS |
| Entity B 1.00x applied conservatively (1.05-1.15x deferred to filed cash flow) | Pillar 2 | PASS (conservative; no offset misuse) |
| No offset on a structural determination | Master Pillar 2 | PASS (not structural; input-price-driven) |

---

## 3. PILLAR 3 (growth/moat), STRATEGIC PREMIUM, UA

| Check | Rule | Result |
|---|---|---|
| Entity A Pillar 3 +0.5x (3b moat; 3a +0) | Amdt 4.1 / Amdt 16 | FAIL (F4) |
| Strategic premium +0 (single-credit) | Amdt 4 | PASS |
| UA correctly NOT applied (FII+DII ≥3%, one qualifier fails) | Amdt 3 | PASS |
| UA ordering min(Raw×1.25, Cap), all-three-qualifier | Amdt 3 | PASS (not triggered; F2=F, no ×1.25) |

**F4 (MAJOR).** Amendment 16 gates the ENTIRE Pillar 3 (3a growth visibility, 3b moat formation, 3c duration) on projected ROCE crossing the minimum ROCE requirement, read from the FTTCP Module B2 binary flag ("growth premium eligible: YES from FY__ / NO"). The report applies the gate to zero 3a but awards **3b +0.5x** without citing the B2 flag, while Entity A ROCE (~13%) sits below the required return used in its own RRM build (r=15.25%). Where B2 reads NO the gate zeros 3b too, which drops the additive raw from 14.5x to 14.0x. Within the 1x tolerance (MAJOR, not CRITICAL) and the destination is operator-approved, but the gate is applied inconsistently across the two Pillar 3 legs. Location: 11-valuation.md Entity A Pillar 3.

---

## 4. RRM DUAL-TRACK (formula, bounds, complexity in r)

| Check | Rule | Result |
|---|---|---|
| RRM produced for all three entities | Master RRM dual-track | PASS |
| Formula 1+(13.5−r)×0.12, percentage-point reading, bounded 0.70-1.60 | Amdt 4.4 | PASS (A 0.79, B 0.82, C 0.82) |
| Entity A r build: 14 + 0.75 (12B cyclical cap) + 0.5 (Amdt 13 complexity) = 15.25% | Amdt 12/13 | PASS |
| Amdt 12A (no cash-conversion r-UP), 12C (no short-record r-UP) honoured | Amdt 12 | PASS |
| Complexity lives in r only (+0.5, dense RPT trigger, B08) | Amdt 13 | PASS |
| Entity B RRM mid 16.6x consistent with stated r | Amdt 4.4 + conservative-track rule | FAIL (F2) |
| Entity A RRM carried 11.5x vs formula 11.06x at r=15.25% | Amdt 4.4 | MINOR (F9) |

**F2 (MAJOR).** Entity B stated r-build = base 14% + durability 0.5 + complexity 0.5 = **15.0%**, which gives RRM 0.82 and destination 19.5×0.82 = **16.0x**. The report carries **16.6x** ("at r 14.75%") as the GOVERNING (entry) track for Entity B. On a >15% track divergence the framework default is that the MORE conservative track governs; 16.0x is more conservative than 16.6x, so the governing value should be 16.0x. Using 16.6x lifts the B base FV from ~530 to 549.8 and the SOTP with it. Verdict (STOP) and AVOID unchanged. Location: 11-valuation.md Entity B Track 1; B11 entity_b.destination_pe_track1_rrm.mid.

**F9 (MINOR).** Entity A RRM mid carried at 11.5x while the stated r=15.25% yields 11.06x. Presentational; the RRM track is not governing for A (additive governs by override).

---

## 5. AMENDMENT 19 — FV PATH, FV CAGR, RETURN-SOURCE CLASSIFICATION (the load-bearing finding)

**F1 (CRITICAL).** The Section 4 FV path over-rolls the end-Year-3 row by one full year, overstating the FV CAGR and flipping the mandatory Amendment 19.2 return-source label.

The intermediate rows roll one EPS step per year (consistent with 18.1 exit-basis symmetry):
- Entity A (10%): today 178.5, end-Y1 196.4 (×1.10), end-Y2 216.0 (×1.10²). End-Y3 should be 178.5×1.10³ = **237.6**. Reported: **261.6** (= 178.5×1.10⁴, four steps).
- Entity B (8%): today 549.8, end-Y1 593.8, end-Y2 641.3 (×1.08²). End-Y3 should be 549.8×1.08³ = **692.6**. Reported: **747.8** (= ×1.08⁴).
- Entity C (10%, ×1/3): today 13.9, end-Y2 16.8 (×1.10²). End-Y3 should be 13.9×1.10³ = **18.5**. Reported: **20.3** (= ×1.10⁴).

Today's FV uses the one-year-forward (Year-1/FY27) EPS; the exit at end-Year-3 uses one-year-forward-from-Year-3 = Year-4/FY30 EPS, which is **three** growth steps from today, not four. The end-Year-3 row applied a fourth step.

Corrected SOTP end-Year-3 ≈ 237.6 + 692.6 + 18.5 = **948.7** (report: 1,029.7).
Corrected FV CAGR = (948.7 / 742.2)^(1/3) − 1 = **≈ 8.5%** (report: 11.5%).
Corrected Amendment 19.2 label: FV CAGR < 10% → **DISCOUNT-CLOSER** (report: HYBRID).

Consequences: the 19.2 thresholds are fixed constants; ~8.5% is below the 10% HYBRID floor. A DISCOUNT-CLOSER also requires the zone-reachability class ON the verdict card (19.5) and a one-line thesis stating the return is the discount closing — the card carries the HYBRID label, so the required zone-reachability line is absent. The 4D targets (base ~1,030) and expected CAGR (−4.9%) inherit the over-roll; corrected base target ~948.7 gives base CAGR ≈ −6.9% and a slightly more negative expected CAGR. The AVOID / no-buy decision survives (it fails the hurdle either way), but a mandatory, mechanical, verdict-card classification is materially wrong. This triggers a stage-11 REWORK of the Amendment 19 path and label (rubric rule 12). Location: 11-valuation.md Section 4 (Amdt 19 table), Section 4D; B11 sotp.fv_path_governing_base / fv_cagr_pct / return_source_class.

| Other Amdt 19 checks | Rule | Result |
|---|---|---|
| FV path table present (today → end-Y3) | 19.0 | PASS (structure) |
| FV CAGR one-line present | 19.1 | PASS (line present; value wrong per F1) |
| Decomposition line + SOTP static-slice share (≈0%) | 19.3 | PASS |
| FV-step event line for the within-hold Clariant slice | 19.4 | PASS |
| FV CAGR + label on verdict card and Role 2 Section 5 | 19.5 | PARTIAL (label present but wrong; discount-closer reachability line missing per F1) |

---

## 6. AMENDMENT 18 — EXIT-BASIS SYMMETRY AND OPTION RESOLUTION

| Check | Rule | Result |
|---|---|---|
| Exit basis matches entry basis (one-year-forward both ends), stated once | 18.1 | PASS |
| Option Resolution Calendar per slice: window + class + named event | 18.2 | PASS (Clariant 24% stake, Bio-MEG, NSU, guar-gum) |
| Clariant 24% stake classified RESOLVES-WITHIN-HOLD; no-event slices take zero | 18.2 | PASS |
| Within-hold options exit as resolved states; bear carries all at FAILURE | 18.3 | PASS (bear Rs 571, JV floor + sale at zero) |
| Converter-multiple bar at resolution preserved | 18.3 / v3.8 interaction | PASS (n/a; JV not a converter slice) |
| Transition dual-display (first five names), resolution track governs | 18.6 | PASS (static Rs 1,030 vs resolution Rs 1,030, delta Rs 0) |
| Role 3 one-year-slip standing question | 18.7 | PASS |
| Projection horizon = hold+1, explicit Year-4 rows with the fade step-down | 18.0 + Amdt 14 | FAIL (F7) |

**F7 (MAJOR).** Section 2 shows a single forward P&L column per entity (one "Operating PBIT" line, bear/base/bull), not the explicit Year-1 through Year-4 committed rows that 18.0 mandates ("Year-4 revenue, margin, PAT and EPS are explicit committed rows in every case"). The FV path rolls EPS at a FLAT CAGR (A 10%, B 8%, C 10%), which Amendment 14 explicitly replaces ("Flat CAGR lines … replacing flat CAGR lines"; the STRENGTHENING classification requires a fade-by-Year-4 step-down shown "year by year"). No year-by-year fade table is present. The report asserts the horizon is "carried to Year 4," but the committed rows and the fade step-down are absent. Location: 11-valuation.md Section 2 P&L tables + Section 4 FV path.

---

## 7. HURDLE RATIO AND VERDICT LOGIC

| Entity | Recompute HR(base) | Report | Result |
|---|---|---|---|
| A | 1.10³ × (14.5/25.5) = 1.331×0.5686 = 0.757 | 0.757 | PASS |
| A bull | 1.15³ × 0.5686 = 0.865 | 0.865 | PASS |
| B | 1.08³ × (19.5/25.5) = 1.2597×0.7647 = 0.964 | 0.964 | PASS |
| B bull | 1.13³ × 0.7647 = 1.104 | 1.104 | PASS |
| C | 1.10³ × (12/25.5) = 0.627 | 0.627 | PASS |
| Pass threshold 1.953 (Tier A) | Amdt 2 / 4.3 | PASS |
| STOP where HR(bull) < 1.953 | Amdt 2 | PASS (A, B STOP; C provisional) |

**F8 (MINOR).** Entity B Hurdle Ratio uses the additive 19.5x mid, while the governing (entry) track is RRM 16.6x. The hurdle should test the destination the entry rests on; the additive value is less conservative (easier to pass). Verdict (STOP) is unchanged even at 16.6x (HR base ≈ 0.82, bull ≈ 0.94), so decision impact is nil. Location: 11-valuation.md Section 4B.

Current PE basis 25.5x = 1,191 / 46.6 forward EPS/share: PASS (single pre-demerger blended multiple, flagged [ESTIMATE, X1]).

---

## 8. TIER ASSIGNMENT, ENTRY ZONE, MoS

| Check | Rule | Result |
|---|---|---|
| Tier A (25% hurdle) applies | Amdt 4.3 | PASS (outcome) — via HIGH POTENTIAL limb; Tier B barred (Gate 0 AVERAGE) |
| Tier A justification stated | Amdt 4.3 | FAIL (F3) |
| Entry = base FV ÷ 1.953 (Tier A divisor) | Amdt 4.3 | PASS (742.2/1.953 = 380.0; 838.2/1.953 = 429.2) |
| MoS = entry × (1 − MoS%) | Master | PASS (380×0.60 = 228) |
| Role 1 ↔ Role 2 entry (380-429) and MoS (228) consistent | cross-artifact | PASS |

**F3 (MAJOR).** The entry-zone derivation (Section 4D/4E) justifies Tier A with "FII+DII <3% keeps this in the transition sleeve." This contradicts B10 ua_qualifiers (fii_dii_lt3: **false**, i.e., FII+DII ≥3%) AND the report's own UA section, which withholds UA precisely because the FII+DII <3% test is NOT met. Both statements cannot hold. Tier A is in fact correct via the OTHER limb of Amdt 4.3 — the combined Gate0+EM assessment is HIGH POTENTIAL (B07) — and Tier B is barred because Gate 0 is AVERAGE. The divisor (1.953) and entry zone are unaffected, but the stated rule basis is wrong and internally contradictory. Location: 11-valuation.md Section 4D, 4E.

---

## 9. ROLE 2 (B14) DECISION RULES AND POSITION SIZING vs MASTER v3.6

| Check | Rule | Result |
|---|---|---|
| Verdict WATCHLIST | Master Role 2 decision rules | FAIL (F6) |
| Entity C INSUFFICIENT CONVICTION, no BUY, resolving event + review date | Master INSUFFICIENT CONVICTION | PASS (guar-free quarter + Prompt H; review post-Q2 FY27) |
| Dispersion sizing: width (999−534)/742 = 63% → Medium cap | Master 4H-pre / Section 7 | PASS (recompute 62.7%; capped further to Small on [ESTIMATE, X1] + DEEP WATCH — tighter cap, allowed) |
| Sector Literacy not gating for Small | Master | PASS |
| Position override recorded | Master | PASS (none; stated) |
| Entry zone / MoS consistent with Role 1 | cross-artifact | PASS |
| ENTRY CONJUNCTION stated in verdict box | Master | PASS |

**F6 (MAJOR).** Master Role 2 decision rules: "AVOID: Gate 0 AVERAGE/AVOID OR … OR Hurdle Ratio = STOP." Both triggers fire here (Gate 0 AVERAGE 46; Hurdle STOP on all three entities). The mechanical verdict is AVOID. The report emits **WATCHLIST**, substituting the operator's FTTCP DEEP WATCH disposition ("a good business I would own at the right price"). WATCHLIST is defined as "CMP above Entry Price but thesis is strong — wait for correction," which does not by itself override the AVOID triggers. The actionable output (do not buy at CMP; entry zone far below) is identical under either label, and the DEEP WATCH disposition is documented in the deliberation, so decision impact is limited — but the verdict label does not follow the written rule and the deviation is operator-disposition-driven, not rule-driven. Surface for human ruling. Location: 14-thesis.md Section 7.

---

## 10. METHOD PLURALITY, SOM, DOWNSTREAM (structural gates)

| Check | Rule | Result |
|---|---|---|
| Section 1A Method Suitability Matrix + ≥2 methods + triangulation weights | rubric 7 | PASS (SOTP frame + Four-Pillar PE 70% + EV/EBITDA 30%) |
| SOM cross-check performed | rubric 4 | PASS (Entity A EPS CAGR vs SOM revenue CAGR, "justified excess") |
| B09/B10 downstream candidates ≥3; demand_externally_verifiable = YES | rubric 6 | PASS (7 candidates; demand verifiable) |
| Catalysts cite candidates or carry MODERATE cap | rubric 6 | PASS |
| Converter classification gate stated upfront (17.0) | 17.0 | PASS (A CONVERTER, B/C NON-CONVERTER, one sentence each) |

---

## 11. OBSERVATION (not a rule failure)

**F10 (MINOR, observational).** Entity A governing track is set to the LESS conservative additive (14.5x) over RRM (11.5x) on a 26.1% divergence, via operator override 1. Operator override is a legitimate authority and the divergence is flagged, but the >15% "conservative-track-governs" default is set aside; note it so the human sees the mixed convention (A on override/additive, B on framework-default/RRM).

---

## RECOMPUTATION SUMMARY

- **Destination PE:** Entity B governing RRM should read 16.0x at the stated r=15.0% (report 16.6x). Entity A additive raw would read 14.0x if the Amdt 16 gate zeros 3b (report 14.5x; operator-approved). Neither shifts the destination by >1x.
- **FV CAGR / return-source:** corrected SOTP end-Year-3 ≈ Rs 948.7, FV CAGR ≈ 8.5% → **DISCOUNT-CLOSER**, not the reported 11.5% HYBRID.
- **Decision:** AVOID / no-buy at CMP survives (fails the 25% hurdle either way). Entity C INSUFFICIENT CONVICTION correct. The Role 2 WATCHLIST label deviates from the mechanical AVOID rule (F6).

## REWORK POSTURE
Stage 11 REWORK recommended: fix the Amendment 19 FV path over-roll (F1), re-derive FV CAGR and the return-source label, add the discount-closer zone-reachability line if the label lands DISCOUNT-CLOSER, add the explicit Year-1-4 committed rows with the Amendment 14 fade step-down (F7), and reconcile Entity B's governing RRM (F2) and the Tier A / UA FII+DII statements (F3). One CRITICAL present; acceptance rate above the 60% REWORK floor.

---

## END OF PHASE-3 VALUATION-ADHERENCE AUDIT
Gate 0 (B01) and Emerging Moat (B07) audited in phase 1, not repeated. Business Understanding Narrative (stage 13) not provided to this phase-3 audit; not evaluated.
