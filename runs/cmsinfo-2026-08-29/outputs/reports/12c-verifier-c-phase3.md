# VERIFIER C — FRAMEWORK ADHERENCE AUDIT (PHASE 3, VALUATION SCOPE)

Company: CMSINFO. Run: runs/cmsinfo-2026-08-29. Model: Opus 4.8. Date: 2026-08-31.
Scope: Role 1 valuation (B10, B11) and Role 2 thesis (B14) rule-compliance only.
Authorities read: Master v3.6 (Role 1, Role 2), Section 1B v3.3 + v3.5.1(ref) + v3.6(ref) + v3.7 + v3.8 + v3.9, FTTCP v2.1.
I audit rule application, not company quality and not raw-number source fidelity (Verifier A owns numbers).

---

## A. PILLAR BUILD — SECTION 1B (rule 4)

| Step | Reported | Re-derived from stated rule | PASS/FAIL |
|---|---|---|---|
| Pillar 1 ROCE input | 16.6% spot (NON-CONVERTER, no smoothing) | Spot ROCE valid for NON-CONVERTER (v3.7 17.1 applies to converters only) | PASS |
| Pillar 1 base PE | 16.0x (band table) | Amendment 5 formula 0.5x16.6+7.5 = 15.8x. Band table is "superseded, quick-reference only." 0.2x gap | MINOR (F1) |
| Pillar 2 cash multiplier | 1.15x (operator Override 1) | INDETERMINATE (industry-event-induced); 1.15x one notch below top band, FY26 FCF negative breaks 1.30x. Operator-approved | PASS |
| Quality-adjusted base | 18.4x | 16.0 x 1.15 = 18.40 | PASS |
| Pillar 3 growth/moat | +0x | 3b EM-gated: EM 23 < 25 = +0. 3a/3c numbers also support +0 but not walked explicitly | PASS (F2 note) |
| Strategic premium | +0x | No licence/scarcity, L1 lowest-bidder | PASS |
| Raw destination PE | 18.4x | 18.4 + 0 + 0 | PASS |
| UA F2 | 18.4x (no uplift) | Not qualified; ordering min(Raw x1.25, cap) correctly gated OFF | PASS (F3 note on B10) |
| Sector cap | 25x, min(18.4, 25) = 18.4x | Absolute ceiling applied, non-binding | PASS |
| Amendment 20 result | trim to 17.0x | Operator Override 2, conservative; direction-of-test citation is loose | MINOR (F4) |
| FINAL destination (exit) PE | 17.0x (band 15.7-18.3x) | Operator-approved, binds (v3.9 Amdt 20.9). Within Section 1B layer set, no round-number default | PASS |

**UA ordering (rule: min(Raw x1.25, Cap), applied only if qualified).** Correctly understood and gated. Three qualifiers: listed >=12m YES; Gate0>=60 OR EM>=25; FII+DII <3%. The DECISIVE qualifier fails: FII+DII 58.70% >> 3%, so UA does not apply. B11 states this reason correctly. B10 (assembly) mis-reasons the second qualifier ("gate0_or_em: NO ... EM fails"): the OR only needs one leg and Gate0 core 76 >= 60 satisfies it, so that qualifier is actually YES. Outcome unchanged (FII+DII fails regardless). F3, MINOR, located in B10-assembly.yaml lines 156-160.

**Amendment 20 (F4).** v3.8/v3.9 Amendment 20.5 is one-directional: the "30% test" hands governance to the RELATIVE multiple only when the pillar destination sits MORE THAN 30% BELOW the adjusted peer base (pillar < 0.70x peer base). Here the pillar (18.4x) sits 43% ABOVE the peer median (~12.9x). Under the amendment as written, the "otherwise" branch applies: the PILLAR governs (18.4x) and the peer table is the cross-check. There is no Amendment-20 mechanism that trims a pillar DOWN toward peers. 11-valuation Sec 1B row I and B10 label the 17.0x cut "Amendment 20 relative trim / 30% test FAILED." The 17.0x is nonetheless fully compliant because it is an explicit OPERATOR ruling (Override 2, 30-Aug-2026), and Amendment 20.9 states the operator-approved base binds and step 1C is a cross-check against it, never an override of it. The trim is conservative (lower exit multiple, harder Hurdle), so it cannot inflate the case. Finding: the number adheres; the framework citation misreads the amendment's direction. MINOR.

## B. SINGLE-CREDIT (rule 4, CLAUDE.md)

ROCE-recovery credit route = "not-credited": NEITHER Pillar 1 midpoint (spot 16.6%, no forward uplift) NOR Strategic Premium (+0x), because the FY28 ROCE>22% proof gate has not fired. No double-credit is possible when neither leg is credited. SHARED CATALYST flag = YES, correctly raised per Amendment 4 (FY28 ROCE recovery and any future growth premium ride the same capex-fill event). PASS.

## C. AMENDMENT 18 — EXIT-BASIS SYMMETRY AND HORIZON (rules, CLAUDE.md)

- Basis symmetry: entry = CMP / FY27E EPS (forward); exit = 17.0x x FY30E EPS (forward). One basis, both ends. PASS.
- Horizon = hold + 1: hold FY27/FY28/FY29, exit priced on FY30E (Year N+1), projection table runs FY27-FY31 (Year 4/5 explicit rows in all three cases). Meets 18.0 minimum. PASS.
- Option Resolution Calendar: single operating entity, no SOTP option slices; N/A stated. The FY28 proof gate is a resolution event for the thesis, not a value-bearing slice. PASS.
- Transition dual-display (18.6): moot (no static-carry-vs-resolution difference without slices). PASS.

## D. AMENDMENT 19 — FV PATH / FV CAGR / RETURN SOURCE (rules)

- FV path table present (Sec 4.4): Today 364, EoY1 413, EoY2 471, EoY3(exit) 535 (17.0x x forward EPS 21.4/24.3/27.7/31.5). Arithmetic verified. PASS.
- FV CAGR line: (535/364)^(1/3)-1 = 13.7-13.8%. Reported 13.8%. PASS.
- Return-source label: HYBRID (10-20% band). 13.8% is in-band. Present on verdict card and Role 2 Sec 5. PASS.
- Decomposition line (19.3): present — FV path compounds on earnings alone (multiple held at 17.0x, no re-rating lever in the path); re-rating lever lives in the CMP-to-destination gap. PASS.
- FV-step events (19.4): N/A (no within-hold slices). PASS.

## E. CONVERTER CLASSIFICATION (rule, CLAUDE.md Amendment 17)

NON-CONVERTER stated upfront (Override 7). Cash-logistics operator, no traded-commodity raw input, no cost-plus/spread-on-commodity. Amendment 17 machinery correctly NOT applied: Pillar 1 uses spot FY26 ROCE with no through-cycle smoothing, which is correct for a NON-CONVERTER. CLAUDE.md bar ("never feed spot-year ROCE into Section 1B for a CONVERTER") not breached. PASS.

## F. HURDLE RATIO AND TIER (rule 4)

- Tier assignment: Tier A (25%, divisor 1.953). Tier B barred because FLAG-CASH is INDETERMINATE, failing Tier B's "no structural FLAG-CASH" gate (Amendment 4.3). Using the harder Tier A on an unresolved cash flag is the conservative and correct reading. PASS.
- HR arithmetic: EPS CAGR FY27->FY30 = (31.5/21.4)^(1/3)-1 = 13.75% ~ 13.8%; (1.138)^3 = 1.472. Entry (current) forward PE = 243/21.4 = 11.355x. HR = 1.472 x (17.0/11.355) = 1.472 x 1.497 = 2.204 ~ 2.20. Closed form 535.5/243 = 2.204. HR 2.20 >= 1.953 -> PASS. Verified.
- Bull not used (base passes); credibility grade B- Bull cap (Base+5%) correctly noted, not invoked. PASS.

## G. ROLE 2 DECISION RULES AND POSITION SIZING (rule 4, Master Role 2)

- Price bands: CMP 243 sits between MoS 227 and Entry 284. Master decision rule = BUY-ON-DIPS on price alone (CMP not <= MoS, so not BUY NOW; not above Entry, so not the Master literal WATCHLIST). The report says exactly this and then holds the actionable verdict at WATCHLIST via the disposition cap.
- Verdict label (F5): the emitted verdict is WATCHLIST. Master's WATCHLIST is defined as "CMP above Entry Price," which does NOT hold here (243 < 284). The situation — no position pending two named data events (FY28 ROCE proof gate; next receivables ageing print) — maps more literally to Master's INSUFFICIENT CONVICTION verdict (a specific unresolved gap with named resolving events and a review posture), not WATCHLIST. The report defers to the operator's authoritative WATCHLIST call (fttcp-deliberation Sec 3), which binds. The actionable output is identical under either label (no buy today, monitor, convert on proof + price + entry conjunction). MINOR, label tension only; decision unaffected.
- Five-verdict disposition: INDETERMINATE cash caps disposition at PROCEED WITH CAVEATS (CLAUDE.md). Reported disposition = PROCEED WITH CAVEATS. PASS.
- Entry conjunction: stated explicitly in the Section 7 verdict box (convert only when proof fires AND price in Rs 227-284 AND no thesis-broken trigger). Master line 1026 satisfied. PASS.
- Dispersion-capped sizing: (Bull 661 - Bear 368)/Base 555 = 52.8%, in the 40-80% band -> caps at Medium. Verified. Report then pulls to Small (Gate0 GOOD not EXCELLENT bars Large; EM MODEST; management B-; cash INDETERMINATE; thin ROCE-CoE spread). Small is below the Medium cap and is conservative; Sector Literacy Track is non-gating for Small. Master sizing gates (Large/Medium) not met for a larger size in any case. PASS. Position is conditional ("Small on conversion only; no position at WATCHLIST").

## H. EVIDENCE-SCALED MARGIN OF SAFETY (rule 4, Master v3.5 Sec 4H-pre / 4H card)

MoS applied at 20% (Rs 227 = 284 x 0.80). Master mandates stating WHICH evidence-scaled row applies and why (lines 852, 860) and carrying it on the verdict card (line 890: "evidence-scaled row applied (20%/30%/40%) with the evidence and catalyst basis"). Neither B11 Sec 4.2 nor the Sec 4.5 verdict card states the row or its basis; both just apply 20%. The 20% row requires "mostly documented evidence AND catalyst inside 12 months." Evidence is mostly documented (19/6/3), which supports the near leg. But the GOVERNING catalyst — the FY28 ROCE>22% proof gate — carries an 18-24 month window (B10 catalyst_12m_primary text), which is "catalyst beyond 18 months," the 40% row trigger. A 40% MoS would set the floor at Rs 170, not Rs 227. The decision survives (verdict is WATCHLIST regardless; CMP is above MoS under either 227 or 170), and the operator referenced Rs 227 (role1-handover Sec 9). But the mandated row-statement is absent and a defensible reading of the governing catalyst timing points to a wider MoS. MAJOR (F6): missing mandatory evidence-scaled MoS row + possible under-selection; number could be materially wrong (Rs 227 vs Rs 170); decision unaffected.

## I. EXIT PE PROVENANCE (rule 8, CLAUDE.md NEVER)

The exit PE 17.0x derives entirely from the Section 1B pillar build (16.0 x 1.15 = 18.4x) reduced by the operator/relative cross-check. It is not a round-number default and enters from no source outside the Section 1B layer set. PASS.

## J. METHOD PLURALITY (rule 7)

Section 1A Method Suitability Matrix present with four applied methods (P/E 50% primary, EV/EBIT 20%, EV/EBITDA 15%, DCF 15%) plus rejected methods and a triangulation table (Sec 3.5). Section 1B destination governs the exit multiple, does not replace method selection. PASS.

---

## OVERALL ASSESSMENT

The core valuation machinery adheres. The destination PE (16.0 x 1.15 = 18.4x raw, trimmed by operator ruling to 17.0x within the sector cap), single-credit (neither leg credited, proof gate unfired), exit-basis symmetry (forward both ends), the Amendment 19 FV path / 13.8% FV CAGR / HYBRID label, the NON-CONVERTER treatment, and the Hurdle Ratio (2.20 >= 1.953, Tier A) all re-derive correctly. The five-verdict disposition cap (INDETERMINATE cash -> PROCEED WITH CAVEATS), the entry conjunction, the dispersion cap, and conservative Small sizing all comply. No CRITICAL finding. No exit PE enters from outside Section 1B.

One MAJOR: the mandatory evidence-scaled MoS row and its basis are not stated, and the governing FY28 proof-gate catalyst (18-24 month window) plausibly selects the 40% row (MoS ~Rs 170) rather than the applied 20% (Rs 227). The decision is unaffected. Four MINOR: Pillar 1 band-table 16.0x vs the superseding Amendment 5 formula 15.8x (operator-approved, 0.2x, disclosed); Amendment 20 cited in the wrong direction for a downward operator trim (number binds via 20.9); B10 UA OR-logic mis-reasoned on the Gate0-or-EM qualifier (outcome correct via the decisive FII+DII leg); WATCHLIST label vs Master's literal WATCHLIST/INSUFFICIENT definitions (operator-approved, decision identical).

Recomputed destination PE: concur, 17.0x. Recomputed decision: concur, WATCHLIST / PROCEED WITH CAVEATS. The valuation+thesis half is framework-adherent; the findings are one material presentational/number gap on MoS and four immaterial or operator-resolved items.

```yaml
stage: B12c
company: "CMSINFO"
run_date: "2026-08-29"
model: claude-opus-4-8
status: complete
scope: "phase-3 valuation (B10, B11, B14 only; Gate0/Emoat audited in phase-1)"
gate0: {rules_checked: 0, fails: []}
emoat: {rules_checked: 0, fails: []}
valuation:
  rules_checked: 24
  fails:
    - {id: F6, severity: MAJOR, location: "11-valuation.md Sec 4.2 and Sec 4.5 verdict card; B11-valuation.yaml mos_price 227", rule: "Master v3.6 Sec 4H-pre / 4H card — evidence-scaled MoS row (20/30/40) must be stated with evidence+catalyst basis", issue: "20% MoS applied without stating the row or basis; governing FY28 proof-gate catalyst window is 18-24 months (the 40% row trigger), which would set MoS ~Rs 170 not Rs 227", decision_impact: "none (verdict WATCHLIST regardless; CMP above MoS under either reading; operator referenced Rs 227)"}
    - {id: F1, severity: MINOR, location: "11-valuation.md Sec 1B row 'Pillar 1 base PE'; B10 valuation_pillars.pillar_1_base_pe", rule: "Section 1B v3.3 Amendment 5 — continuous formula replaces band table", issue: "band-table 16.0x used; formula 0.5x16.6+7.5 = 15.8x; 0.2x gap, operator Override 4, disclosed and logged", decision_impact: "none"}
    - {id: F4, severity: MINOR, location: "11-valuation.md Sec 1B row I; B10 amendment_20_relative_trim", rule: "Section 1B v3.9 Amendment 20.5/20.9 — 30% test is one-directional (pillar >30% BELOW peer base); operator base binds", issue: "17.0x cut labelled 'Amendment 20 relative trim / 30% test FAILED' but pillar 18.4x sits ABOVE peers; the cut is an operator conservative override (Override 2), not the amendment's mechanism", decision_impact: "none (17.0x binds via 20.9; conservative)"}
    - {id: F3, severity: MINOR, location: "B10-assembly.yaml ua_qualifiers lines 156-160", rule: "Section 1B v3.3 Amendment 3 — UA qualifier 'Gate0>=60 OR EM>=25'", issue: "gate0_or_em marked NO citing EM<25; the OR is satisfied by Gate0 core 76>=60, so qualifier is YES; UA still does not apply because FII+DII 58.70% fails the <3% leg (B11 reasons this correctly)", decision_impact: "none"}
    - {id: F5, severity: MINOR, location: "14-thesis.md Sec 7 verdict box; B14-thesis.yaml verdict WATCHLIST", rule: "Master v3.6 Role 2 decision rules (lines 1022-1023, 1028-1043)", issue: "WATCHLIST emitted, but Master WATCHLIST = 'CMP above Entry' (here CMP 243 < Entry 284); the unresolved-gap-pending-named-events pattern maps more literally to INSUFFICIENT CONVICTION; operator authoritative WATCHLIST call binds", decision_impact: "none (identical action: no buy, monitor, convert on conjunction)"}
business_understanding_narrative: {present: null, five_questions_answered: null, prose_only: null, section6_candidates_named: 0, valuation_vocab_leak: null, fails: []}  # stage-13 artifact; not in phase-3 valuation inputs
recomputed_destination_pe: ""   # concur, 17.0x
recomputed_decision: ""         # concur, WATCHLIST / PROCEED WITH CAVEATS
findings:
  - {severity: MAJOR, id: F6, location: "11-valuation Sec 4.2/4.5", note: "evidence-scaled MoS row not stated; 20% vs possible 40% (Rs 227 vs Rs 170); decision unaffected"}
  - {severity: MINOR, id: F1, location: "11-valuation Sec 1B", note: "band 16.0x vs formula 15.8x; operator-approved, 0.2x"}
  - {severity: MINOR, id: F4, location: "11-valuation Sec 1B row I", note: "Amendment 20 cited wrong direction for a downward operator trim; number binds via 20.9"}
  - {severity: MINOR, id: F3, location: "B10 ua_qualifiers", note: "UA OR-logic mis-reasoned; outcome correct via FII+DII leg"}
  - {severity: MINOR, id: F5, location: "14-thesis Sec 7", note: "WATCHLIST vs Master INSUFFICIENT-CONVICTION mapping; operator-approved; action identical"}
critical_count: 0
major_count: 1
minor_count: 4
framework_adherence: 88
acceptance_rate: 79    # 19 of 24 rule-checks clean
overall_verdict: "ADHERES — no CRITICAL, decision fully survives; one MAJOR (MoS evidence-scale row) and four MINOR, all decision-neutral or operator-resolved"
```
