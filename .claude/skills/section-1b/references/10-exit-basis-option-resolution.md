# Chunk 10. Exit-basis symmetry and the Option Resolution Calendar (A18)

Loaded by: Role 1 Section 2 projection horizon and Section 4 exit table. Pipeline: stage 11 (overrides 8 and 9); stage 15 (Amendment 18.7 standing question).
Sources in force: Section 1B v3.8 Amendment 18 and its interactions; Master v3.7 §2A projection horizon; v3.6 Amendment 14; v3.7 Amendment 17; v3.9 Amendment 20.

## 18.0 Projection horizon = hold + 1

- Every Section 2 projection table runs to Year 4 at minimum, Year 5 preferred. The Year 3 buyer pays for Years 4 and 5.
- Year 4 revenue, margin, PAT and EPS are explicit committed rows in every case (bear, base, bull), built from the same fade machinery as Years 1-3 (Amendment 14).
- Where the fade needs an industry growth anchor the corpus does not hold, the anchor is a NAMED assumption in the table, not a silent one.
- "NOT PROJECTED" for Year 4 is REWORK.
- A name with no credible Year 4 to Year 5 story (typically Emerging Moat None, or a documented saturation of the runway) takes an exit-multiple haircut: reduce the destination PE mid by one full turn, restate, and flag "no Year 4-5 story: exit haircut applied" on the verdict card.

## 18.1 Exit-basis symmetry: one basis, both ends

The Year N exit price applies the destination PE to the SAME earnings basis the entry used:

- Entry basis one-year-forward → exit = destination PE × Year N+1 EPS.
- Entry basis trailing → exit = destination PE × Year N EPS.

Mixing bases is barred. State the basis once in the Section 1B worksheet; it governs both ends. The Year N buyer is an investor of the same kind as the operator, so a mixed basis hides an unquantified bias in the exit price. Where the operator approved an earnings basis at the FTTCP pillar-approval gate, that basis applies.

## 18.2 Option Resolution Calendar (mandatory per option slice)

Every option slice in a SOTP carries, in a stated table:

- the fructification window (the year or years in which the option resolves), sourced from committed milestones, and citing the DOWNSTREAM SIGNAL TRACKER event row by name where one exists;
- the classification: RESOLVES-WITHIN-HOLD (window at or before Year N) or BEYOND-HOLD (window after Year N);
- the resolution event itself: the observable fact that flips the option (first commercial order, first invoiced revenue, commissioning, licence grant).

A slice with no nameable resolution event is not an option. It is narrative and takes zero value. A run without tracker rows states milestones from committed filings alone; the calendar is still mandatory.

## 18.3 Exit-state pricing for within-hold options

At the Year N exit, RESOLVES-WITHIN-HOLD options appear as resolved states, not discounted probabilities:

- SUCCESS: mature PAT × the slice's OWN destination multiple, entering the exit price as ordinary earnings power, with no probability haircut and no PV discount. A converter-classified slice keeps its converter multiple; no slice inherits the core multiple by resolving.
- FAILURE: zero, plus any stated salvage only if anchored to a filed asset value.
- Scenario weighting uses the operator's slice probability at scenario level. **The BEAR case carries ALL within-hold options at FAILURE.**
- The exit-price table shows each slice's resolved contribution per case.

## 18.4 Exit carry for beyond-hold options

BEYOND-HOLD options remain options at the exit, with two changes: (a) PV is re-dated from Year N, not from today, to the fructification window; (b) the probability is CONDITIONAL on what has resolved by Year N. The conditional probability is an operator input at the gate; it defaults to the unconditional input only where no within-hold dependency exists, and the dependency is named either way.

## 18.5 Today-value machinery

Amendment 18 changes the EXIT construction only. Today's fair value carries option slices as probability-weighted, PV-discounted expected values, because they are unresolved today. Pillar math, destination PE derivation and the entry-zone formula are unchanged by 18.0-18.4.

## 18.6 Transition dual display

For the first five Role 1 runs under Amendment 18, the Section 4 exit table shows both constructions (static-carry exit and resolution-based exit) with the per-share delta. The resolution-based exit governs the verdict from the first run. The dual display retires after five names.

## 18.7 Role 3 standing question

For any SOTP with within-hold options: "Which resolution dates carry the exit, and what does the exit price become if each slips by one year?" On managements with timeline-miss records, slippage is the base case for dates, and the answer shows the one-year-slip exit per slice.

## Interactions

- The Hurdle Ratio formula is unchanged; only the EPS the destination PE multiplies at exit is brought onto the entry basis.
- A failed 18.0 (no Year 4 row) makes Amendment 19's FV path impossible. That is a single REWORK against 18.0, not two.
- A relative exit multiple (Step 1C) multiplies the same Year N+1 EPS on the entry basis (chunk 15).
- Amendment 19 FV-step lines read this calendar and add no new probability inputs (chunk 12).

## Worksheet lines

- "Earnings basis (entry and exit): [forward / trailing] (operator-approved: Y/N)"
- Per slice: "Slice ___ | window FY__ | [RESOLVES-WITHIN-HOLD / BEYOND-HOLD] | resolution event ___ | tracker row ___ | probability ___ (conditional on ___) | SUCCESS PAT ₹___ Cr × own multiple ___x"
