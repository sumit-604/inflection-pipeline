# STAGE 12 — VERIFIER C: FRAMEWORK-ADHERENCE AUDIT (PHASE 3, VALUATION SCOPE)

**Company:** ENTERO (Entero Healthcare Solutions Ltd) | **Run Date:** 2026-07-27
**Model:** claude-opus-4-8 | **Scope:** VALUATION ADHERENCE + ROLE 2 (deferred half)
**Artifacts audited:** B10 (10-valinputs.md / B10-valinputs.yaml), B11 (11-valuation.md / B11-valuation.yaml), B14 Role 2 (14-thesis.md / B14-thesis.yaml)
**Rule sources:** Master v3.6 Role 1 + Role 2; Section 1B v3.3/v3.5.1/v3.6/v3.7/v3.8/v3.9; FTTCP v2.1
**Not re-emitted:** Gate 0 (B01) and Emerging Moat (B07) audits were recorded in phase 1; this pass audits valuation adherence only.

I audit rule application, not raw numbers (Verifier A owns number-in-source fidelity) and not company quality.

---

## 1. SECTION 1B / ROLE 1 COMPLIANCE TABLE

| # | Rule (source) | Applied as written? | Recomputed | Verdict |
|---|---|---|---|---|
| 1 | Exit PE drawn ONLY from Section 1B layer set; honours operator base 18-20x mid 19x (CLAUDE.md NEVER; fttcp carry) | Track1 RRM 18-20x, Track2 additive 18-20x, mid 19x; no outside/round-number PE | 19x | PASS |
| 2 | Continuous Pillar 1 formula 0.5xROCE+7.5, not old bands (v3.6 Amdt 5) | 0.5 x 22.5 + 7.5 = 18.75 -> 19x | 18.75 -> 19 | PASS |
| 3 | FTTCP ROCE verdict sole Pillar 1 authority (RECOVERING; forward-capital 20-25%) | Verdict RECOVERING carried; midpoint 22.5% is the operator forward-capital ruling from FTTCP | — | PASS |
| 4 | Single-credit: ROCE recovery in Pillar 1 XOR Strategic Premium (CLAUDE.md; consumption clause) | Credited in Pillar 1; Strategic Premium +0x BARRED | — | PASS |
| 5 | Pillar 2 matches determination; no offset on structural/INDETERMINATE; INDETERMINATE never clean pass (CLAUDE.md) | INDETERMINATE, <=1.0x, disposition cap only, growth offset 0, no numeric uplift; caps verdict at PROCEED WITH CAVEATS/WATCHLIST | — | PASS |
| 6 | Pillar 3 matches injected EM/catalyst inputs | EM 19 MODEST -> +0x (below 25 gate); premium capped by sector cap regardless | +0x | PASS |
| 7 | UA in Amendment 3 order, all three qualifiers evidenced; correctly withheld if FII+DII > 3% | UA DOES NOT APPLY; FII+DII ~19.8% > 3%; also Gate0 53<60 and EM 19<25 fail. Withheld | not applied | PASS |
| 8 | Sector cap absolute (18-20x operator, overrides manifest Pharma/CDMO) | min(F2=19, cap 20) = 19; cap binds premiums | 19x | PASS |
| 9 | BOTH tracks present and carried through every fair value + verdict card | Track1 (RRM) and Track2 (additive) both on card and in fair_values; divergence 0% | — | PASS |
| 10 | Conservative track governs entry on >15% divergence | Track divergence 0% (rule not triggered); 14.4x/12x conservative sensitivities shown, not overwriting operator | — | PASS |
| 11 | Hurdle Ratio (Amdt 2) Tier A 25% on CMP 1,806; threshold HR>=1.953 | base (1.167)^3 x (19/55.6) = 0.54; bull (1.23)^3 x (19/52.5) = 0.67; STOP | 0.54 / 0.67 | PASS |
| 12 | Credibility-grade gate on Bull (bull usable only at qualifying grade) | Grade B usable; bull row admitted | — | PASS |
| 13 | Amdt 18.0 projection horizon = hold+1 (Year 4 mandatory, all cases) | Section 2C reaches Y4 FY30 bear/base/bull | — | PASS |
| 14 | Amdt 18.1 exit-basis symmetry, forward=forward | Exit = dest PE x Year N+1 (FY30) EPS; both ends forward; stated once | — | PASS |
| 15 | Amdt 19.0 FV path table (today -> end-Y3), governing track, base | Today 617 / Y1 722 / Y2 830 / Y3 929, each = 19x x forward EPS | consistent | PASS |
| 16 | Amdt 19.1 FV CAGR line, one number | (929/617)^(1/3)-1 = 14.6% | 14.6% | PASS |
| 17 | Amdt 19.2 return-source classification, fixed bands | HYBRID (14.6% inside 10-20%) | HYBRID | PASS |
| 18 | Amdt 19.3 decomposition line | Present: growing core, zero static slices, no re-rating lever left, CMP de-rating named | — | PASS |
| 19 | Amdt 19.5 FV CAGR + label on verdict card and Role 2 Section 5 | On B11 card and B14 Section 5 | — | PASS |
| 20 | Amdt 20 Step 1C handled; no fabricated peers (20.1 / Correction 6) | PENDING LIVE PEER TABLE; pillar 19x governs; 30% test deferred to claude.ai; provisional read notes cap binds relative multiple too | — | PASS |
| 21 | Earnings basis forward as operator-approved | pe_basis forward, both ends (Amdt 18.1) | — | PASS |
| 22 | Method plurality: Section 1A matrix + >=2 methods + triangulation weights (rule 7) | Matrix present; P/E 70% primary + EV/EBITDA 30% secondary; triangulation stated | — | PASS |
| 23 | Converter classification correct (v3.7 Amdt 17) | NON-CONVERTER (finished-goods resale, distribution spread); 17.1-17.4 do not bind; no spot ROCE fed to converter math | — | PASS |
| 24 | One-improvement-one-mechanism (no double credit) | ROCE once (Pillar 1), cash once (Pillar 2), complexity once (r); explicit check present | — | PASS |
| 25 | Intrinsic-today vs 3yr-target reconciliation (adjudicated below) | Math consistent at every USE; YAML field label ambiguous | see F1 | PASS-with-note (MINOR) |
| 26 | Hurdle EPS-CAGR basis consistency with forward Current PE | 16.7% (Y0->Y3) used vs 14.6% (Y1->Y4) implied by forward Current PE; verdict-invariant | see F2 | PASS-with-note (MINOR) |

---

## 2. ADJUDICATION — THE Rs 617 vs Rs 929 "INTERNAL TENSION"

B11 flags an internal tension for this verifier: the decision line cites fair value ~Rs 617 while `fair_values.base` in the YAML is Rs 929. B11-valuation.yaml line 22 asks me to reconcile which is intrinsic-today and which is the 3-year target.

**Ruling: there is no valuation error. Both numbers are framework-correct at their own point on the Amendment 19 FV path. The apparent tension is a YAML field-label ambiguity only.**

The earnings basis is ONE-YEAR-FORWARD (operator-approved, Amdt 18.1). Under that basis:

- **Fair value TODAY = destination PE x next-year forward EPS = 19x x FY27 EPS (32.5) = Rs 617.** This is the Amendment 19.0 "today" row and the framework-correct intrinsic value TODAY. It is the figure against which CMP is measured (1,806 / 617 = 2.9x; downside to FV today = -66%).
- **End-Year-3 EXIT fair value (the 3-year target) = 19x x FY30 (Year 4) forward EPS (48.9) = Rs 929.** This is the Amendment 18.1 exit price and the Amendment 19.0 end-Year-3 row. It is NOT today's intrinsic value.

The stored `fair_values: {bear: 694, base: 929, bull: 1157}` are the **end-Year-3 exit/target prices**, not today's fair value. Every USE of these numbers in B11 is correct:

- Entry zone = exit / 1.25^3 = 929 / 1.953 = Rs 476 (uses exit price — correct).
- FV CAGR = (929 / 617)^(1/3) - 1 = 14.6% (today -> exit — correct).
- CMP multiple and downside use Rs 617 (today FV — correct).

The report body removes any ambiguity: Section 4 states "Today's fair value ... Rs 617" and "End-Year-3 (exit) ... Rs 929"; the verdict card carries "Fair value today (base) Rs 617"; B14 Section 5 labels both rows explicitly ("Base Fair Value today Rs 617" and "Base Fair Value end-Year-3 exit Rs 929"). The prose is unambiguous.

The single defect: the B11 YAML field is named `fair_values` with no time qualifier, while it holds Year-3 exit prices, and the sibling `decision` string cites today's Rs 617. A machine reader consuming `fair_values.base` as "today's intrinsic value" would be misled by ~1.5x. This is presentational, changes no decision and no destination PE. Recorded as **F1, MINOR**. Recommended fix: rename to `fair_values_exit_y3` (or add a `fair_value_today: 617` field).

---

## 3. HURDLE-RATIO BASIS NOTE (F2, MINOR)

The Master Hurdle formula is HR = (1 + EPS CAGR)^3 x (Dest PE mid / Current PE). B11 uses the Y0->Y3 EPS CAGR (base 16.7%, bull 23.0%) while the Current PE denominator is on Year-1 forward EPS (55.6x = 1,806/32.5). On a strict forward basis the g consistent with a Year-1 Current PE is the Y1->Y4 CAGR (14.6%), which is exactly the FV CAGR B11 already computed. Using 16.7% slightly overstates HR (0.54 vs a strict-forward 0.51). The offset is one year of fade and is **verdict-invariant**: both readings sit far below the 1.953 pass threshold, so the STOP holds by a wide margin. Recorded as **F2, MINOR**; no recompute of the decision.

---

## 4. ROLE 2 (B14) DECISION-RULE AND POSITION-SIZE COMPLIANCE

| # | Role 2 rule (Master v3.6) | Applied? | Verdict |
|---|---|---|---|
| R1 | AVOID triggers: Gate 0 AVERAGE/AVOID OR Promoter CONCERN OR U/D < 2x OR Hurdle STOP | Fires on all four independently (Gate0 53 AVOID; Promoter CONCERN; U/D 0; HR STOP) | PASS |
| R2 | Entry conjunction (anti-value-trap) stated in Section 7 verdict box | Present verbatim (price-in-zone AND no thesis-broken trigger) | PASS |
| R3 | Promoter Concern cap binds over everything above Small | Small ceiling; Promoter CONCERN cap named as binding | PASS |
| R4 | INDETERMINATE cash caps disposition at WATCHLIST/PROCEED WITH CAVEATS, no BUY NOW | Applied; ceiling WATCHLIST, zero position at CMP | PASS |
| R5 | Dispersion cap (Section 4H-pre): 40-80% width caps Medium, >80% caps Small | (1,218-657)/929 = 60% -> Medium; tighter Promoter cap binds first -> Small | PASS |
| R6 | Sector Literacy gating: Medium/Large need >=3 books; Small not gated | Small not gated; Medium/Large correctly withheld (no books evidenced) | PASS |
| R7 | Position-size derivation documented; no undocumented operator size override | Four binding reasons listed; operator override recorded as Halt-1/ROCE only, not size | PASS |
| R8 | Thesis-broken trigger specific and measurable | M&A > ~Rs 200 Cr rolling 12m; margin < 4.5%; H1 FY27 FCF negative | PASS |
| R9 | FV CAGR + return-source label carried into Role 2 Section 5 (Amdt 19.5) | 14.6% HYBRID present in B14 Section 5 and one-line thesis | PASS |

Position size: verdict AVOID -> operative position at CMP zero; recorded forward ceiling Small (2-3%). Every cap that could lift it is either not met (Sector Literacy) or binds downward (Promoter CONCERN, INDETERMINATE cash, dispersion). The derivation is internally consistent and matches the Master rules.

Note on dispersion input: B14 computes width from the 18x-bear / 20x-bull corner cells (60%). Using same-multiple (mid-19x) bull/bear fair values gives (1,157-694)/929 = 50%. Both land in the 40-80% Medium band; result unchanged. Not a finding.

---

## 5. FINDINGS

| ID | Severity | Location | Finding | Effect |
|---|---|---|---|---|
| F1 | MINOR | B11-valuation.yaml `fair_values` | Field holds end-Year-3 exit/target prices (base 929) but is named without a time qualifier while `decision` cites today's FV Rs 617. Both numbers framework-correct at their FV-path point; prose is unambiguous. Machine reader could misread the field. | No decision change; no destination-PE change. Rename to `fair_values_exit_y3` / add `fair_value_today`. |
| F2 | MINOR | B11 Section "THE HURDLE RATIO" | Hurdle uses Y0->Y3 EPS CAGR (16.7%/23.0%) against a Year-1 forward Current PE; strict forward consistency wants the Y1->Y4 CAGR (14.6%). Overstates HR by ~0.03. | Verdict-invariant; STOP holds far below 1.953 threshold. |

No CRITICAL findings. No MAJOR findings. No misapplication changes the destination PE by >1x, flips the Hurdle verdict, or flips the decision.

**Concurrence:** destination PE 19x (both tracks) — concur. Decision AVOID (on valuation) — concur. Exit PE sourced only from the Section 1B layer set, honouring the operator base and absolute sector cap — confirmed. Single-credit, UA withholding, Amendment 18 symmetry, Amendment 19 path/CAGR/label, and Amendment 20 Step-1C deferral all applied as written.

---

## 6. TALLY

- Rules checked: 26 (Section 1B/Role 1) + 9 (Role 2) = 35; consolidated below as 26 valuation-adherence rules with Role 2 folded into the count table.
- Fails: 2 (both MINOR).
- Critical: 0 | Major: 0 | Minor: 2.
- Acceptance rate: 33 clean / 35 checked = 94%.

---

```yaml
stage: B12c
company: "ENTERO"
run_date: "2026-07-27"
model: claude-opus-4-8
status: complete
gate0: {rules_checked: 0, fails: []}   # recorded in phase 1, not re-audited
emoat: {rules_checked: 0, fails: []}   # recorded in phase 1, not re-audited
valuation:
  rules_checked: 35
  fails:
    - {id: "F1", severity: "MINOR", rule: "Amdt 19 / YAML labelling", detail: "fair_values field holds end-Year-3 exit prices (base 929) but is unqualified while decision cites today's FV Rs 617; both correct at their FV-path point, prose unambiguous; machine reader could misread. Rename to fair_values_exit_y3 or add fair_value_today: 617"}
    - {id: "F2", severity: "MINOR", rule: "Hurdle Ratio (Amdt 2) basis consistency", detail: "Hurdle uses Y0->Y3 EPS CAGR (16.7%/23.0%) against a Year-1 forward Current PE; strict-forward g is the Y1->Y4 CAGR (14.6%); overstates HR ~0.03; verdict-invariant, STOP holds"}
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: ["Not in valuation scope; stage-13 synthesis not audited this pass"]}
recomputed_destination_pe: ""   # concur, 19x both tracks
recomputed_decision: ""         # concur, AVOID (on valuation)
findings:
  - {severity: "MINOR", location: "B11-valuation.yaml fair_values", note: "Field holds Year-3 exit/target prices; name lacks time qualifier vs decision citing today's Rs 617. Framework-math correct at every use; entry=929/1.953=476, FV CAGR 617->929=14.6%, CMP=1806/617=2.9x. Presentational; no decision/PE change."}
  - {severity: "MINOR", location: "B11 Hurdle Ratio section", note: "Y0->Y3 EPS CAGR used with Year-1 forward Current PE; strict-forward consistency wants Y1->Y4 (14.6%). HR overstated ~0.03; STOP verdict unchanged."}
critical_count: 0
major_count: 0
minor_count: 2
acceptance_rate: 94
```
