# SECTION 1B v3.8 AMENDMENTS — EXIT-BASIS SYMMETRY AND OPTION RESOLUTION

*Version 3.8 | 23 August 2026 | Exit-basis symmetry and option resolution, operator directive 23-Aug-2026. Layers on top of Section 1B v3.3 + v3.3 Amendments + v3.5.1 + v3.6 + v3.7. It does not modify any prior file in place. Where they overlap on items named here, v3.8 governs. Stage 11 reads this alongside the earlier Section 1B files. Amendments number continuing from v3.7 (whose last amendment is 17).*

---

## AMENDMENT 18 — EXIT-BASIS SYMMETRY AND OPTION RESOLUTION

`[v3.8: projection horizon = hold + 1, exit-basis symmetry, Option Resolution Calendar, exit-state pricing for within-hold options, re-dated carry for beyond-hold options, transition dual-display, and a Role 3 standing question — operator directive 23-Aug-2026, arising from the PERMAGNET v3 valuation walkthrough]`

**18.0 Projection horizon = hold + 1 (mandatory).** Every Role 1 Section 2 projection table runs to Year 4 at minimum (Year 5 preferred, consistent with Master v3.6's existing runway language: the Year-3 buyer pays for Years 4 and 5). Year-4 revenue, margin, PAT and EPS are explicit committed rows in every case (bear/base/bull), built from the same fade machinery as Years 1-3 (Amendment 14 fade-to-industry applies; where the fade rule requires an industry growth anchor that the corpus does not hold, the anchor is a NAMED assumption in the table, not a silent one). "NOT PROJECTED" for Year 4 is no longer an acceptable gap in a completed Role 1; it is REWORK.

**18.1 Exit-basis symmetry (one basis, both ends).** The exit price at Year N applies the destination PE to the SAME earnings basis the entry used:
- Entry basis one-year-forward → exit = destination PE × Year N+1 EPS.
- Entry basis trailing → exit = destination PE × Year N EPS.

Mixing bases (forward entry, trailing exit, or the reverse) is barred. The chosen basis is stated once in the Section 1B worksheet and governs both ends. Rationale, recorded here: the Year-N buyer is an investor of the same kind as the operator; assuming they price on a more conservative basis than the operator's own entry embeds hidden, unquantified conservatism (or, reversed, hidden optimism) into every exit price.

**18.2 Option Resolution Calendar (mandatory per option slice).** Every option slice in a SOTP carries, in a stated table:
- fructification window (the year(s) in which the option resolves), sourced from committed milestones and, where a DOWNSTREAM SIGNAL TRACKER event row exists for the milestone, citing that row by name;
- classification: RESOLVES-WITHIN-HOLD (window at or before Year N) or BEYOND-HOLD (window after Year N);
- the resolution event itself (the observable fact that flips the option: first commercial order, first invoiced revenue, commissioning, licence grant).

A slice with no nameable resolution event is not an option; it is narrative, and takes zero value (consistent with the FTTCP survivorship guard).

**18.3 Exit-state pricing for within-hold options.** At the Year-N exit, options classified RESOLVES-WITHIN-HOLD do not appear as discounted probabilities. They appear as resolved states:
- SUCCESS state: mature PAT × the slice's OWN destination multiple (a converter-classified slice keeps its converter multiple per Amendment 17; no slice inherits the core multiple by resolution) — entering the exit price as ordinary earnings power, no probability haircut, no PV discount (both have resolved away for the winner).
- FAILURE state: zero (plus any stated salvage only if anchored to a filed asset value).
- Scenario weighting: the success/failure states are weighted at scenario level using the operator's slice probability; the BEAR case carries ALL within-hold options at FAILURE (hard rule).
- The exit-price table shows the per-slice resolved contribution explicitly, per case.

**18.4 Exit carry for beyond-hold options.** Options classified BEYOND-HOLD remain options at the exit, with two changes from the today-value treatment: (a) PV re-dated from Year N (not from today) to the fructification window; (b) probability stated as CONDITIONAL on what has resolved by Year N (e.g., a full-plan option conditional on the modest phases having delivered) — the conditional probability is an operator input at the gate, defaulting to the unconditional input only where no within-hold dependency exists, with the dependency named either way.

**18.5 Today-value machinery unchanged.** Amendment 18 changes the EXIT construction only. Today's fair value continues to carry option slices as probability-weighted, PV-discounted expected values (they are genuinely unresolved today). Nothing in 18.0-18.4 alters Section 1B pillar math, destination PE derivation, or the entry-zone formula (entry = exit-consistent fair value ÷ 1.25^N, MoS per evidence scale).

**18.6 Transition display (sunset after 5 names).** For the first five Role 1 runs under this amendment, the Section 4 exit table displays BOTH constructions — static-carry exit (old) and resolution-based exit (new) — with the per-share delta, so the operator sees the systematic effect before the old display retires. The resolution-based exit GOVERNS the verdict from the first run.

**18.7 Devil's standing question.** Role 3 gains one mandatory question for any SOTP with within-hold options: "Which resolution dates carry the exit, and what does the exit price become if each slips by one year?" (On managements with timeline-miss records, slippage is the base case for dates; the answer must show the one-year-slip exit per slice.)

---

## AMENDMENT 19 — FAIR-VALUE PATH AND FV-CAGR CLASSIFICATION

`[v3.8: mandatory fair-value path table, the one-number FV CAGR, and the COMPOUNDER / HYBRID / DISCOUNT-CLOSER return-source classification — operator directive 23-Aug-2026, arising from the PERMAGNET entry-zone interrogation. Display and diagnosis; alters no pillar math. Mechanically dependent on Amendment 18's Year-4 projection.]`

**19.0 The FV path table (mandatory in every Role 1).** Every completed Role 1 contains, in Section 4 alongside the entry-zone derivation, a fair-value path table on the GOVERNING track, base case: fair value computed at each year-end of the hold, using the same machinery as the today-value — the entry-consistent earnings basis rolled forward one year at each step (18.1 symmetry), option slices carried per their resolution treatment (static today per 18.5; resolved or re-dated at each future point per 18.3/18.4 as the calendar dictates), net debt held at the anchored figure unless a committed projection moves it. Minimum rows: today, end-Year-1, end-Year-2, end-Year-3 (the exit point). The Year-4 EPS required by the end-Year-3 row exists by 18.0.

**19.1 The FV CAGR line (one number, mandatory).** Below the table, one line: "FV CAGR over the hold: X.X% (today Rs A to end-Year-3 Rs B, governing track, base case)." Computed as (B/A)^(1/3) − 1. Bear and bull FV CAGRs may be shown but the base-case number is the classification input.

**19.2 Return-source classification (mechanical, from 19.1).** One of three labels, printed on the verdict card:
- **COMPOUNDER — FV CAGR ≥ 20%:** fair value itself delivers most of the required return; entry near fair value is defensible; the entry zone is a bonus, not the engine. (Cross-reference: this is the quality-at-fair-price case the framework's transition-alpha mandate normally deprioritizes — the label makes the exception visible rather than accidental.)
- **HYBRID — FV CAGR 10-20%:** return comes partly from FV growth, partly from discount closing; the entry zone matters proportionally.
- **DISCOUNT-CLOSER — FV CAGR < 10%:** the required return must come almost entirely from the entry discount; the entry zone does ALL the work; zone reachability (market-unlikely vs plausible) becomes the decision-relevant fact, and an event-driven FV STEP (a resolution date moving the whole path) is the realistic path to entry, not price drift alone.

The label is a diagnosis of WHERE the return comes from, not a quality grade — a DISCOUNT-CLOSER can be a fine business at the wrong price (the PERMAGNET case), and a COMPOUNDER can be a bad buy above fair value. The three-band thresholds (20% / 10%) are fixed constants, not fuzzy language.

**19.3 The decomposition line (why the FV CAGR is what it is).** One or two sentences, mandatory, naming the drivers: the growing fraction of FV (core) vs the static fraction (unresolved option slices), the fade schedule's drag, and whether any re-rating lever remains (multiple already at destination = no lever). For SOTP names, state the static-slice share of FV explicitly ("X% of fair value is non-compounding option value").

**19.4 FV-step events (SOTP names with resolution calendars).** Where 18.2's calendar contains within-hold resolution events, add one line per event: the approximate FV step if it resolves SUCCESS (the slice's resolved value minus its static carry, per share). This is the bridge between the tracker's event rows and the valuation: it quantifies what a fired signal is worth to the path. No new probability inputs — the step uses the already-approved slice parameters.

**19.5 Verdict-card and thesis surfacing.** The verdict card gains two lines: "FV CAGR: X.X% — [COMPOUNDER / HYBRID / DISCOUNT-CLOSER]" and, for discount-closers, the zone-reachability class alongside it. Role 2 Section 5's valuation summary carries the same two lines. The one-line thesis for a DISCOUNT-CLOSER must state where the return comes from ("the return is the discount closing from Rs A to Rs B, not the business compounding").

---

## INTERACTION WITH THE REST OF THE FRAMEWORK

- **18.3 preserves Amendment 17's converter-multiple bar at resolution.** A converter slice resolving successfully still exits on its converter PE; no slice inherits the core multiple by resolving. This is load-bearing: it is what stops a converter option (e.g. an NdFeB line) from inheriting the core quality multiple the moment it prints revenue.
- **18.1 does not alter the FTTCP Hurdle Ratio formula's inputs** beyond making the destination-PE-times-EPS term basis-consistent. The (1 + EPS CAGR)^3 × (Destination PE ÷ Current PE) form is unchanged; only the EPS the destination PE multiplies at exit is brought onto the entry basis.
- **18.2's tracker citations are references, not dependencies.** A run without tracker rows (pre-Role-5.5) states milestones from committed filings alone; the Resolution Calendar is still mandatory.
- **Amendment 14's fade governs the Year-4 build in 18.0.** Where 14's fade-to-industry step is numerically unpinned, the named-assumption rule in 18.0 applies rather than a silent -1pp continuation.
- **Single-credit and the sector cap are untouched.** 18.3's resolved-state earnings power is priced on the slice's own already-derived multiple; it creates no new premium and raises no cap.
- **19.0 consumes 18.0's Year-4 projection and 18.1's basis symmetry.** A run failing 18.0 (no Year-4 row) cannot produce 19.0; that is a SINGLE REWORK against 18.0, not two.
- **19.4 reads 18.2's Resolution Calendar** and introduces no new resolution machinery or probability inputs; it only quantifies the per-share FV step of an already-parameterized slice.
- **19.2's COMPOUNDER label does not override the transition-alpha mandate or any FTTCP verdict.** It is display and diagnosis. Nothing in Amendment 19 alters pillar math, destination PE, the entry-zone formula, MoS, or today-value machinery.

## VERSION HISTORY

| Version | Date | Changes |
|---|---|---|
| 3.6 | 13-Aug-2026 | (prior) Amendments 11-16, Damodaran integration. See `Section_1B_v3_6_Amendments.md`. |
| 3.7 | 20-Aug-2026 | (prior) Amendment 17, commodity converter cycle integration. See `Section_1B_v3_7_Amendments.md`. |
| 3.8 | 23-Aug-2026 | Amendment 18, exit-basis symmetry and option resolution, operator directive 23-Aug-2026, arising from the PERMAGNET v3 valuation walkthrough. 18.0 projection horizon = hold + 1 (Year 4 minimum in every case, Year-4 gap is REWORK). 18.1 exit-basis symmetry (exit EPS basis matches entry basis; mixing barred; stated once, governs both ends). 18.2 Option Resolution Calendar mandatory per slice (window, RESOLVES-WITHIN-HOLD vs BEYOND-HOLD, named resolution event; no event = narrative = zero). 18.3 within-hold options exit as resolved states (SUCCESS = mature PAT × the slice's own multiple, no probability/PV haircut; FAILURE = zero; bear carries all within-hold options at failure; converter-multiple bar preserved). 18.4 beyond-hold options re-dated from Year N and conditionally-probabilized. 18.5 today-value machinery unchanged (exit-only amendment). 18.6 transition dual-display for the first five names, resolution-based exit governs. 18.7 Role 3 standing one-year-slip question for within-hold options. |
| 3.8 | 23-Aug-2026 | Amendment 19, fair-value path and FV-CAGR classification, operator directive 23-Aug-2026, arising from the PERMAGNET entry-zone interrogation. 19.0 mandatory FV path table in Section 4 (governing track, base case; today through end-Year-3, consuming 18.0's Year-4 EPS and 18.1's basis). 19.1 the one-number FV CAGR line = (end-Year-3 ÷ today)^(1/3) − 1. 19.2 mechanical return-source label COMPOUNDER (≥20%) / HYBRID (10-20%) / DISCOUNT-CLOSER (<10%), fixed thresholds; a diagnosis of where the return comes from, not a quality grade. 19.3 mandatory decomposition line (growing core vs static option share, fade drag, re-rating lever; SOTP names state the static-slice share of FV). 19.4 per-event FV-step lines for within-hold resolution events (bridge from tracker to valuation; no new probability inputs). 19.5 FV CAGR + label surface on the verdict card and in Role 2 Section 5; a DISCOUNT-CLOSER one-line thesis states the return is the discount closing, not compounding. Display and diagnosis only; alters no pillar math, destination PE, entry-zone formula, MoS, or today-value machinery. |
