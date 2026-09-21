# Chunk 12. Amendments 16 and 19

Loaded by: Role 1 Section 1B Pillar 3 eligibility gate (A16); Role 1 Section 4 fair-value path and verdict card (A19). Pipeline: stage 11 (override 10); stage 14 (A19 lines in Role 2 Section 5 and the one-line thesis); stage 13 synthesis (verdict card lines).
Sources in force: Section 1B v3.6 Amendment 16; v3.8 Amendment 19 and its interactions; v3.9 Amendment 20.8; FTTCP v2.3 Module B2.

## Amendment 16: growth premium eligibility gate

Growth below the cost of capital destroys value as it compounds, so it is not paid for.

- **No Pillar 3 growth premium (3a growth visibility, 3b moat formation, 3c duration) is awarded for any year before projected ROCE crosses the minimum ROCE requirement.**
- The crossover is a binary gate read directly from FTTCP Module B2: "growth premium eligible: YES from FY__ / NO".
- B2 reads NO (ROCE does not cross within the projection) → Pillar 3 pays +0x regardless of order book, moat score or duration.
- B2 reads YES from a future fiscal year → the premium is eligible only from that year forward, and the projection shows the pre-crossover years earning no premium.
- The gate sits on top of the existing Pillar 3 evidence gates and precedes them. It does not replace them.

### FTTCP Module B2 inputs Role 1 reads (never recomputes)

- Minimum ROCE requirement = the required return r the valuation uses. Where the RRM-derived r is not yet available at the FTTCP stage, the standing default is **13.5% for micro and small caps** (operator Gate E, 13-Aug-2026). B2 states which was used.
- Forward ROCE path, Year 1 / Year 2 / Year 3, built from the Part A evidence.
- The crossover year.

## Amendment 19: fair-value path and FV-CAGR classification

Display and diagnosis. It alters no pillar math, destination PE, entry-zone formula, margin of safety, or today-value machinery. It depends on Amendment 18's Year 4 projection.

### 19.0 The FV path table (mandatory in every Role 1)

In Section 4, beside the entry-zone derivation, on the GOVERNING track, base case: fair value at each year-end of the hold, using the same machinery as today's value.

- The entry-consistent earnings basis rolls forward one year at each step (Amendment 18.1).
- Option slices follow their resolution treatment: static today (18.5); resolved or re-dated at each future point per 18.3 / 18.4 as the calendar dictates.
- Net debt is held at the anchored figure unless a committed projection moves it.
- Minimum rows: today, end-Year-1, end-Year-2, end-Year-3 (the exit point). The Year 4 EPS the end-Year-3 row needs exists by 18.0.

### 19.1 The FV CAGR line (one number, mandatory)

"FV CAGR over the hold: X.X% (today Rs A to end-Year-3 Rs B, governing track, base case)." Computed as (B/A)^(1/3) − 1. Bear and bull FV CAGRs may be shown; the base-case number is the classification input.

### 19.2 Return-source classification (mechanical, from 19.1)

| Label | FV CAGR | Meaning |
|---|---|---|
| COMPOUNDER | ≥ 20% | Fair value itself delivers most of the required return; entry near fair value is defensible; the entry zone is a bonus, not the engine |
| HYBRID | 10-20% | Return comes partly from FV growth, partly from the discount closing; the entry zone matters proportionally |
| DISCOUNT-CLOSER | < 10% | The required return must come almost entirely from the entry discount; zone reachability (market-unlikely vs plausible) becomes the decision-relevant fact; an event-driven FV step is the realistic path to entry, not price drift alone |

- The 20% and 10% thresholds are fixed constants.
- The label diagnoses WHERE the return comes from. It is not a quality grade. A DISCOUNT-CLOSER can be a fine business at the wrong price; a COMPOUNDER can be a bad buy above fair value.
- COMPOUNDER does not override the transition-alpha mandate or any FTTCP verdict.

### 19.3 The decomposition line (mandatory)

One or two sentences naming the drivers: the growing fraction of FV (core) against the static fraction (unresolved option slices), the fade schedule's drag, and whether any re-rating lever remains (multiple already at destination = no lever). SOTP names state the static share explicitly: "X% of fair value is non-compounding option value."

### 19.4 FV-step events (SOTP names with resolution calendars)

One line per within-hold resolution event in the 18.2 calendar: the approximate per-share FV step if it resolves SUCCESS (the slice's resolved value minus its static carry). No new probability inputs; the step uses the already-approved slice parameters.

### 19.5 Surfacing

- The verdict card carries: "FV CAGR: X.X% [COMPOUNDER / HYBRID / DISCOUNT-CLOSER]" and, for discount-closers, the zone-reachability class beside it.
- Role 2 Section 5 carries the same two lines.
- A DISCOUNT-CLOSER one-line thesis states where the return comes from: "the return is the discount closing from Rs A to Rs B, not the business compounding."
- No entry zone is presented without the FV CAGR and the return-source label.

### Recompute when the relative multiple governs (Amendment 20.8)

When Step 1C hands governance to the relative multiple, recompute the FV path, the FV CAGR, the label and its decomposition line on that governing multiple (capped). The pillar-based lines stay as the labelled cross-check.
