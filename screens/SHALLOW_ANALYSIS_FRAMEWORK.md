# Shallow Analysis Framework v1.0

The specification for the shallow read of a screener candidate. It sits between
the screener hit and the heavy pipeline. Its job is understanding, a posture,
and a go or no-go into `/step1`. It is not the deep pipeline.

Operator: Keerti Kaushik. Strategy: transition alpha, quality-ladder climb.

## What shallow means

- Grounded only in the corpus held under `screens/corpus/<TICKER>/`. Every
  number points at a file and a page. "NOT FOUND" means not in the corpus, and
  the analysis says where it was looked for.
- No forensics: no Notes triple-pass, no 17-check, no arithmetic audit.
- No live-web promoter dig, no peer verification, no verifier agents.
- No Role 1 valuation and no price target. Shallow stops before the spear and
  before `/step1`. **Step 13 is the one exception** (operator ruling
  2026-09-21): a forward bottom-line estimate and a forward PE, built only from
  disclosed guidance or delivered run-rates, are screening metrics and are
  required on every card.
- One independent check stands in for the cut machinery: the credit-rating
  rationale, written by an agency that holds management's numbers.

## What it keeps, cuts, substitutes against full Phase 1

| Full Phase 1 | Shallow |
|---|---|
| Stage 4 business decode | KEEP, compressed |
| Stage 3 AR deep dive (8 phases) | COMPRESS to MD&A, MD letter, segments, highlights |
| Stage 5 concall | KEEP where a transcript exists |
| Stage 7 emerging moat (22 cat) | COMPRESS to the competitive-advantage step |
| Stage 8 promoter web check | REPLACE with the corpus promoter step plus the credit report |
| Stage 1 Gate 0 (160 pt) | REPLACE with the financial-trajectory read |
| Stage 2 notes forensic | CUT |
| Stage 6 peers | CUT |
| Stage 9 TAM/SAM/SOM | CUT, opportunity noted in one line |
| Verifiers A to D | REPLACE with document-surfaced flags plus the credit rating |
| 09b dossier, 13 synthesis | KEEP as the narrative plus the verdict card |
| Role 1 valuation | REPLACE with the step 13 forward view: next-year bottom line and forward PE |

## The output, per company

One markdown file at `screens/cards/<TICKER>.md`. The Business Understanding
Narrative first, then the twelve steps as sections, then the verdict. Roughly
1,400 to 1,900 words. Operator voice: one idea per sentence, numbers first,
active voice, no em-dashes, plain words.

## Business Understanding Narrative (read first, prose)

Five questions, answered in prose before any step or verdict.
1. What does it do, and how does it make money?
2. What is changing, the transition?
3. Why now?
4. What must be true for the thesis to work?
5. What breaks it?

## The twelve steps

The four themes the operator named each get a dedicated step: business model
(2), transition (6), competitive advantages (3), promoters (4).

1. **Corpus ledger.** What is held, what is missing, which later step each gap
   weakens. No new fetching.
2. **Business model and archetype.** What it makes and sells, segments,
   revenue mix, where the margin comes from, the one economic engine. Assign an
   archetype from the library.
3. **Competitive advantages.** Pricing power, switching costs, cost advantage,
   scale, scarcity. Is a moat present, forming, or absent. One paragraph, not
   the 22-category scan.
4. **The promoters.** Holding and pledge, who they are, group backing,
   related-party dependence, skin in the game. From the AR board and
   shareholding pages and the credit report. No web.
5. **Financial trajectory.** The multi-year highlights plus the last two
   quarters: revenue, EBITDA margin, PAT, ROCE, leverage, cash-conversion
   direction. Classify the inflection: earnings-led, margin-led, one-off, or an
   asset event.
6. **The transition and the quality ladder.** The rung the business leaves and
   the rung it claims, R0 to R5, with the mechanism. Management's claim quoted
   once.
7. **Growth-trigger register.** Each trigger as a line: what, date, source, and
   status marked stated, underway, or delivered.
8. **Proof check.** Do the last two quarters move the way the triggers claim.
   Name the proof point, or name its absence. Not the forensic gate.
9. **Flags from the documents.** Related-party, auditor emphasis, dilution,
   concentration, litigation, governance. Surfaced, not investigated.
10. **Independent check: the credit rating.** The agency's conclusion on
    sustainability, leverage, and the transition.
11. **Posture: the Transition Decision Matrix.** Proof gate fired or not;
    ugliness artifact-of-climb or structural; recognition gap open or closed.
    Yields the posture label.
12. **Verdict card.** PROCEED to `/step1`, WATCH, or PASS. Load-bearing facts
    to verify first. What would change the view. No price.
13. **Forward view.** Added by operator ruling, 2026-09-21. Next year's
    expected bottom line, the growth rate against the last reported year, and
    the forward price-to-earnings ratio. The operator screens on growth against
    forward multiple, so a card without this step cannot be ranked and is
    incomplete. Rules in the section below.

## Step 13: the forward view

Operator ruling, 2026-09-21. The purpose is ranking, not valuation: find the
companies whose bottom line grows fast and whose forward multiple has not yet
paid for it.

Each card states four things and the basis tier for the estimate.

- **FY+1 bottom line.** Profit after tax. Where only profit before tax is
  disclosed, apply tax and say the rate is an assumption.
- **Growth** against the last reported full year.
- **Forward PE** = market capitalisation divided by the FY+1 bottom line.
  Market capitalisation comes from the Bull AI company record and is labelled
  as a service record, not a filed document, with its date.
- **Basis tier**, which is the honest part:
  - **A — Guided.** Management gave a rupee number, a growth band or a margin
    target, with a date. Cite it.
  - **B — Run-rate.** A delivered quarter or half-year, annualised. Say so,
    and respect any seasonality warning the company itself filed.
  - **C — Trend.** A delivered multi-year growth rate with a mechanism behind
    it. Weakest usable tier.
  - **D — NOT FOUND.** No forward basis exists. Leave the forward PE blank.
    Do not fill it.

Three prohibitions carry over unchanged. Do not set a target price. Do not
issue a buy or sell. Do not compute a forward PE for a loss-making company;
write NOT APPLICABLE and name the gate to profitability instead.

One warning the ruling exists to serve. A cheap forward multiple on fast
growth is a screen result, not a conclusion. Earnings that carry no tax, a
quarter that will not repeat, and a run-rate built on falling revenue all
screen well and all mislead. The card's own steps 5, 8, 9 and 11 are what stop
that, so the forward view is read with them, never instead of them.

## Rules that must not break

- Every number traces to a corpus file and page.
- No target price and no buy or sell instruction. The step 13 forward PE is a
  screening metric and is not a valuation.
- A missing document marks the steps it weakens; it does not stop the analysis.
- The credit rating is one view, not the verdict. Today's filings win over an
  older rating.
- The verdict decides only whether the name is worth a full `/step1`. It is not
  a position.
