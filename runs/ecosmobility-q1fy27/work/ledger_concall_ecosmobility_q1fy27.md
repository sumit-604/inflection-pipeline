# A2 COMPLETENESS LEDGER — Concall — ECOSMOBILITY — Q1 FY27

Source: extract_concall_ecosmobility_q1fy27.txt (105 source lines, line numbers as in
source, referenced verbatim via `<line>\t<text>` convention). All turn/line numbers below
are SOURCE line numbers (col 1 of the tab-delimited extract), not Read-tool line numbers.

```
=== A2 COUNT TEST ===
category: participants        grep_count: 12   sweep_count: 12   match: yes
category: speaker_turns       grep_count: 65   sweep_count: 65   match: yes
category: qa_questioner_blocks grep_count: 9   sweep_count: 9    match: yes
category: questions (formally marked: primary + "Follow-up:") grep_count: 28  sweep_count: 28  match: yes
category: mgmt_answer_turns ("CMD:" prefixed)  grep_count: 25   sweep_count: 25  match: yes
category: mgmt_numbers        grep_count: 67   sweep_count: 67   match: yes
category: guidance_forward_statements grep_count: 14  sweep_count: 14  match: yes
category: hedge_phrases       grep_count: 10   sweep_count: 10   match: yes
category: zero_standing_nondisclosure grep_count: 6  sweep_count: 6  match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Reconciliation notes:
- `qa_questioner_blocks`: `grep -n -E "^[0-9]+\tQ[0-9]+ —" extract` returns 9 header lines
  (source lines 31,43,51,55,73,79,85,89,94). One false-positive candidate ("Q1 was a healthy
  quarter..." at source line 10, inside CMD opening remarks, referring to the fiscal quarter
  not a questioner) was manually excluded on inspection — grep pattern anchored on the em-dash
  after "Q#" avoids this collision. 9 = 9, match.
- `questions`: grep `^[0-9]+\tQ[0-9]+ —` primary lines (9) is not itself a question line (the
  header is a label; the question text sits on the next content line) — primary question
  content lines are 32,44,52,56,74,80,86,90,95 (9) + `grep -c "^[0-9]+\tFollow-up:"` = 19 →
  28 total. Manual sweep of Q1-Q9 blocks (see QUESTIONS LEDGER below) independently counts
  28 question turns. Match.
  NOTE: source line 95 (Q9 primary) bundles TWO distinct interrogative asks ("what % booked
  online this quarter" and "and last quarter?") into one transcript line, each answered
  inline. Ledger row-count convention here is one row per TRANSCRIPT LINE (per the "every row
  carries a line number" rule), so this is carried as ONE ledger row flagged
  `MULTI_QUESTION_TURN` rather than split into two rows — flagged, not dropped.
- `mgmt_answer_turns`: `grep -c -E "^[0-9]+\tCMD:"` = 25. Independently reconciles against
  25 CMD: turns identified in the Speaker Turn Ledger. Match.
- `mgmt_numbers`: built from three mechanically-verified sub-buckets over management-only
  lines (opening 8/10/12/14/16/18; CFO 21/23/25/27; CMD Q&A answers
  33/35/37/39/41/45/47/49/53/57/59/61/63/65/67/69/71/75/77/81/83/87/91/98/100; inline mgmt
  figures embedded in Q9 lines 95/96; closing 103):
  (a) `%`-glyph count via `grep -o '%'` restricted to those lines = 29
  (b) INR/₹ monetary figures via `grep -oE "(INR [0-9][0-9,.]*|₹[0-9,]+)"` = 14
  (c) whole-number KPI figures (cities, clients, vehicles, trips, countries, tenure-years,
      not %-suffixed or currency-prefixed) via manual line-by-line sweep, cross-checked
      against raw digit-token extraction = 24
  29 + 14 + 24 = 67, and the Quantitative Claims table below has exactly 67 rows
  (manual sweep). Match.
- Exclusions applied consistently to both grep and sweep (documented, not silently dropped):
  "Fortune 500", "BSE 500" (proper-noun client-tier references, not ECOS-reported metrics);
  "Q1/Q4" and "FY26/FY27" quarter/year labels; calendar date "30 June 2026" / "June 30, 2026";
  idiomatic "a million dollar question" (line 63, not a number); vague quantifier "one or
  two" (line 65, not a hard number — captured qualitatively in the Non-Disclosure table
  instead).
```

---

## SECTION 1 — PARTICIPANTS (12 rows; grep_count 12, sweep_count 12, match)

| # | Name | Firm / Role | Side | First appearance (line) | Flags |
|---|---|---|---|---|---|
| 1 | Hashika Mutreja | Adfactors PR | Moderator/Operator | 5 | — |
| 2 | Rajesh Loomba | Chairman & Managing Director, ECOS | Management | 8 | — |
| 3 | Hem Kumar Upadhyay | Chief Financial Officer, ECOS | Management | 21 | — |
| 4 | Jigar Jani | Nuvama PCG Research | Analyst (Q1) | 31 | — |
| 5 | Pulkit Singh | Dness Capital Management | Analyst (Q2) | 43 | — |
| 6 | Kesha Gag | Counter Cyclical PMS | Analyst (Q3) | 51 | — |
| 7 | [name] Jain | ENS Wealth | Analyst (Q4) | 55 | name-not-fully-transcribed |
| 8 | Sam Sha | Nuvama Wealth Research | Analyst (Q5) | 73 | — |
| 9 | Priya Sha | Sha Family Office | Analyst (Q6) | 79 | — |
| 10 | Salon Sha | Individual investor | Analyst (Q7) | 85 | — |
| 11 | [DRJ] | Sapphire Capital | Analyst (Q8) | 89 | name-not-fully-transcribed |
| 12 | Swatch Chen / [name] | ENS | Analyst (Q9) | 94 | name-ambiguous-in-transcript |

`MGMT_ABSENCE` check: CMD present (opening, Q&A, closing) and CFO present (financial
remarks) — both sides of management on the call. No absence flag.

---

## SECTION 2 — SPEAKER TURN LEDGER (65 turns; grep_count 65, sweep_count 65, match)

Turn numbering is sequential across the whole call. Line = source line number.

| Turn | Line | Speaker | First ~10 words | Segment | Flags |
|---|---|---|---|---|---|
| 1 | 5 | Operator (Hashika Mutreja) | "Ladies and gentlemen, good day and welcome to ECOS..." | Intro | — |
| 2 | 8 | CMD | "Good morning and a very warm welcome. ECOS is India's..." | Opening | — |
| 3 | 10 | CMD | "Q1 was a healthy quarter with operating growth. Revenue grew..." | Opening | — |
| 4 | 12 | CMD | "We ended Q1 with presence across 151 cities in India..." | Opening | — |
| 5 | 14 | CMD | "We onboarded 61 new clients compared to 53 in Q1..." | Opening | — |
| 6 | 16 | CMD | "In Q4 we launched our direct web booking portal, and..." | Opening | — |
| 7 | 18 | CMD | "As we look at the rest of FY27, our priorities remain..." | Opening | — |
| 8 | 21 | CFO | "Revenue from operations for the quarter stood at INR 2,113.72..." | CFO remarks | NUMBER_DISCREPANCY (see Sec.4 row 30) |
| 9 | 23 | CFO | "EBITDA margin for the quarter was below the 11% to..." | CFO remarks | — |
| 10 | 25 | CFO | "Employee benefit expenses for the quarter stood at INR 237.63..." | CFO remarks | — |
| 11 | 27 | CFO | "From a balance sheet perspective we continue to remain in..." | CFO remarks | — |
| 12 | 32 | Jigar Jani (Q1 primary) | "Let's address the elephant in the room, the margins...." | Q&A | REPEAT_QUESTION (margin trajectory) |
| 13 | 33 | CMD | "Great question. Last quarter we were already seeing these signs..." | Q&A answer | — |
| 14 | 34 | Jigar Jani (follow-up) | "What is that margin level below which you wouldn't do..." | Q&A | — |
| 15 | 35 | CMD | "That depends market to market and client to client; these..." | Q&A answer | — |
| 16 | 36 | Jigar Jani (follow-up) | "On the event management line in your press release —..." | Q&A | — |
| 17 | 37 | CMD | "This is not very material. We have been getting requirements..." | Q&A answer | ZERO_STANDING |
| 18 | 38 | Jigar Jani (follow-up) | "Any update on inorganic acquisition — we are close to..." | Q&A | — |
| 19 | 39 | CMD | "We will be looking at certain opportunities. Only last month..." | Q&A answer | — |
| 20 | 40 | Jigar Jani (follow-up) | "Employee expense growth number?" | Q&A | REPEAT_QUESTION (employee cost) |
| 21 | 41 | CMD | "Growth around 20%." | Q&A answer | — |
| 22 | 44 | Pulkit Singh (Q2 primary) | "A suggestion first: in the previous call you came in..." | Q&A | — |
| 23 | 45 | CMD | "In CCR this quarter we rolled out new technology that..." | Q&A answer | — |
| 24 | 46 | Pulkit Singh (follow-up) | "Elaborate on the automation and cost savings — which line..." | Q&A | — |
| 25 | 47 | CMD | "It would come across almost all departments in CCR —..." | Q&A answer | — |
| 26 | 48 | Pulkit Singh (follow-up) | "At 10% margins, given investments already made, what revenue..." | Q&A | — |
| 27 | 49 | CMD | "Our guidance remains between 15 to 18%." | Q&A answer | — |
| 28 | 52 | Kesha Gag (Q3 primary) | "In this industry with no entry barriers, where cost of..." | Q&A | — |
| 29 | 53 | CMD | "While there are no entry barriers and anybody can buy..." | Q&A answer | — |
| 30 | 56 | [name] Jain (Q4 primary) | "On gross margins — they have also declined. Why?" | Q&A | REPEAT_QUESTION (margin trajectory) |
| 31 | 57 | CMD | "In a very high competitive environment, if we have to..." | Q&A answer | — |
| 32 | 58 | Jain (follow-up) | "Is it because of competition pressure that you reduced prices?" | Q&A | — |
| 33 | 59 | CMD | "Yes, you can say that." | Q&A answer | — |
| 34 | 60 | Jain (follow-up) | "Has gross margin declined in both ETS and CCR?" | Q&A | — |
| 35 | 61 | CMD | "More evident in ETS because it is bulk / mass..." | Q&A answer | — |
| 36 | 62 | Jain (follow-up) | "As competition intensifies with big names entering, how much lower..." | Q&A | — |
| 37 | 63 | CMD | "That's a million dollar question. Internally we have set..." | Q&A answer | hedge |
| 38 | 64 | Jain (follow-up) | "Did we lose any clients this quarter to competition?" | Q&A | — |
| 39 | 65 | CMD | "Not majorly. Maybe one or two renewals that didn't happen..." | Q&A answer | ZERO_STANDING |
| 40 | 66 | Jain (follow-up) | "Were added clients more on ETS or CCR side?" | Q&A | — |
| 41 | 67 | CMD | "By numbers more on CCR side; by revenues more on..." | Q&A answer | — |
| 42 | 68 | Jain (follow-up) | "Can you give EBITDA margin separately for ETS and CCR..." | Q&A | — |
| 43 | 69 | CMD | "No, we do not declare that; costs are common to..." | Q&A answer | ZERO_STANDING (canonical non-disclosure: segment margin split declined) |
| 44 | 70 | Jain (follow-up) | "On the SIXT tie-up — what is it and how..." | Q&A | — |
| 45 | 71 | CMD | "We are the exclusive GSA (general selling agent) in India..." | Q&A answer | — |
| 46 | 74 | Sam Sha (Q5 primary) | "On margins — when and by how much could margins..." | Q&A | REPEAT_QUESTION (margin trajectory) |
| 47 | 75 | CMD | "Our guidance is that we would be maintaining this, because..." | Q&A answer | hedge |
| 48 | 76 | Sam Sha (follow-up) | "A data point — previous quarter's presentation said over 1,750..." | Q&A | REPEAT_QUESTION (active-client count reconciliation) |
| 49 | 77 | CMD | "We have a large number of clients, perhaps more than..." | Q&A answer | — |
| 50 | 80 | Priya Sha (Q6 primary) | "Fleet capacity has expanded significantly ahead of revenue growth...." | Q&A | — |
| 51 | 81 | CMD | "The fleet capacity is the vehicles on our network. Out..." | Q&A answer | — |
| 52 | 82 | Priya Sha (follow-up) | "On the macro environment / competitiveness — how has the..." | Q&A | — |
| 53 | 83 | CMD | "It's very hard to predict competitors' actions, so I would..." | Q&A answer | hedge; ZERO_STANDING (declines to comment on moderation) |
| 54 | 86 | Salon Sha (Q7 primary) | "Employee costs are expected to go up — elaborate on..." | Q&A | REPEAT_QUESTION (employee cost) |
| 55 | 87 | CMD | "Employee cost this year is expected up ~20% (as the..." | Q&A answer | — |
| 56 | 90 | [DRJ] (Q8 primary) | "The B2C app launching this quarter — what expectations do..." | Q&A | — |
| 57 | 91 | CMD | "We are addressing the growing premium market for car rentals..." | Q&A answer | hedge (no target given this year) |
| 58 | 92 | [DRJ] (follow-up) | "With the increase in oil prices, has the vendor been..." | Q&A | DROPPED_QUESTION (line incomplete, no management response recorded) |
| 59 | 95 | Swatch Chen/[name] (Q9 primary) | "Two more follow-ups. What percentage of bookings came online..." | Q&A + inline answer | MULTI_QUESTION_TURN (2 questions bundled); mgmt answers inline unlabeled |
| 60 | 96 | Swatch Chen/[name] (follow-up) | "Current active client base this quarter? — Around 1,400." | Q&A + inline answer | REPEAT_QUESTION (active-client count); mgmt answer inline unlabeled |
| 61 | 97 | Swatch Chen/[name] (follow-up) | "How do we categorize an active client?" | Q&A | — |
| 62 | 98 | CMD | "Any organization we have a signed contract with, who gives..." | Q&A answer | — |
| 63 | 99 | Swatch Chen/[name] (follow-up) | "On the clients added — you said more revenue on..." | Q&A | — |
| 64 | 100 | CMD | "We added 15 clients on the ETS side — one of..." | Q&A answer | — |
| 65 | 103 | CMD | "Thank you for the opportunity. We are hopeful of keeping..." | Closing | hedge |

Segment sub-totals (independently reconciled): Intro 1, CMD opening 6, CFO remarks 4,
Q&A 53 (Q1:10, Q2:6, Q3:2, Q4:16, Q5:4, Q6:4, Q7:2, Q8:3, Q9:6), Closing 1. Total = 65.

---

## SECTION 3 — QUESTIONS LEDGER (28 formally-marked question turns; grep 28, sweep 28, match)

| # | Turn (line) | Analyst | Firm | Topic | Flags |
|---|---|---|---|---|---|
| 1 | 32 | Jigar Jani | Nuvama PCG Research | Margin decline drivers / FY27 guidance now ~10% vs prior 11-13% / pricing threshold | REPEAT_QUESTION |
| 2 | 34 | Jigar Jani | Nuvama PCG Research | Specific margin threshold below which business is declined | — |
| 3 | 36 | Jigar Jani | Nuvama PCG Research | Event-management revenue line: materiality, investment, scalability | — |
| 4 | 38 | Jigar Jani | Nuvama PCG Research | M&A / inorganic use of ~₹150 cr cash, or buyback/dividend | — |
| 5 | 40 | Jigar Jani | Nuvama PCG Research | Employee expense growth number | REPEAT_QUESTION |
| 6 | 44 | Pulkit Singh | Dness Capital Management | Guidance-credibility pushback; cost-cutting / productivity measures | — |
| 7 | 46 | Pulkit Singh | Dness Capital Management | Which cost line does automation savings hit (employee vs other) | — |
| 8 | 48 | Pulkit Singh | Dness Capital Management | Revenue growth assumption consistent with 10% margin | — |
| 9 | 52 | Kesha Gag | Counter Cyclical PMS | No entry barriers; competitive edge / cost-of-capital challenge | — |
| 10 | 56 | [name] Jain | ENS Wealth | Gross margin decline — why | REPEAT_QUESTION |
| 11 | 58 | [name] Jain | ENS Wealth | Is decline competition-driven | — |
| 12 | 60 | [name] Jain | ENS Wealth | ETS vs CCR — where is gross margin decline more evident | — |
| 13 | 62 | [name] Jain | ENS Wealth | How much lower can margins go; comfort level | — |
| 14 | 64 | [name] Jain | ENS Wealth | Client losses to competition this quarter | — |
| 15 | 66 | [name] Jain | ENS Wealth | Added clients — ETS or CCR skew | — |
| 16 | 68 | [name] Jain | ENS Wealth | Segment (ETS vs CCR) EBITDA margin split — requested | ZERO_STANDING (declined) |
| 17 | 70 | [name] Jain | ENS Wealth | SIXT tie-up structure and commission mechanics | — |
| 18 | 74 | Sam Sha | Nuvama Wealth Research | Margin trajectory / timing and magnitude of improvement | REPEAT_QUESTION |
| 19 | 76 | Sam Sha | Nuvama Wealth Research | Active client count reconciliation: prior deck >1,750 vs this qtr 1,400 | REPEAT_QUESTION |
| 20 | 80 | Priya Sha | Sha Family Office | Fleet utilization and headroom before adding more fleet | — |
| 21 | 82 | Priya Sha | Sha Family Office | ETS competitive intensity trend vs FY26; pricing moderation signs | — |
| 22 | 86 | Salon Sha | Individual investor | Employee cost investment areas; customer acquisition cost trajectory | REPEAT_QUESTION |
| 23 | 90 | [DRJ] | Sapphire Capital | B2C app launch — expectations this quarter | — |
| 24 | 92 | [DRJ] | Sapphire Capital | Oil-price impact on vendors (incomplete — line dropped) | DROPPED_QUESTION |
| 25 | 95 | Swatch Chen/[name] | ENS | Online booking % this quarter and prior quarter (2 asks bundled) | MULTI_QUESTION_TURN |
| 26 | 96 | Swatch Chen/[name] | ENS | Current active client base | REPEAT_QUESTION |
| 27 | 97 | Swatch Chen/[name] | ENS | Definition of "active client" | — |
| 28 | 99 | Swatch Chen/[name] | ENS | ETS client additions this quarter (of the 61 total) | — |

REPEAT_QUESTION topic clusters: (a) margin trajectory/threshold — Q1(#1), Q4(#10), Q5(#18);
(b) employee cost — Q1(#5), Q7(#22); (c) active client count reconciliation — Q5(#19),
Q9(#26). All three clusters reflect analysts pressing management on the same unresolved
point across independent questioner blocks — a signal of unresolved disclosure quality,
carried forward as data, not interpreted here.

---

## SECTION 4 — QUANTITATIVE CLAIMS SPOKEN BY MANAGEMENT (67 rows; grep 67, sweep 67, match)

Grouped by bucket per the Count Test reconciliation note. Turn = source line number.

### 4a. Percentage figures (29 rows)

| # | Line | Speaker | Metric | Value | Comparator given | Flags |
|---|---|---|---|---|---|---|
| 1 | 10 | CMD | Revenue growth YoY | 16.7% | — | — |
| 2 | 10 | CMD | Volume growth YoY | 27% | — | — |
| 3 | 12 | CMD | Trip growth YoY | 27% | (repeat of #2) | — |
| 4 | 12 | CMD | Trip growth QoQ | ~7% | — | — |
| 5 | 12 | CMD | ETS share of revenue | 59% | prior quarter lower | — |
| 6 | 12 | CMD | CCR share of revenue | 41% | — | — |
| 7 | 14 | CMD | Active client base YoY growth | ~18% | — | — |
| 8 | 14 | CMD | Revenue share from 5+ year customers | 51% | — | — |
| 9 | 21 | CFO | Revenue growth YoY | 16.7% | (repeat of #1) | — |
| 10 | 21 | CFO | Revenue growth QoQ | ~2.2% | — | — |
| 11 | 21 | CFO | EBITDA margin, quarter (as transcribed) | 9.3% | vs 12.0% Q1FY26, 11.7% Q4FY26 | NUMBER_DISCREPANCY — reconciles to reported 10.34% (bracketed in extract) |
| 12 | 21 | CFO | EBITDA margin, Q1 FY26 | 12.0% | — | — |
| 13 | 21 | CFO | EBITDA margin, Q4 FY26 | 11.7% | — | — |
| 14 | 23 | CFO | FY27 EBITDA margin guidance, prior (floor) | 11% | superseded this call | — |
| 15 | 23 | CFO | FY27 EBITDA margin guidance, prior (ceiling) | 13% | superseded this call | — |
| 16 | 23 | CFO | FY27 EBITDA margin guidance, revised | ~10% | GUIDANCE | — |
| 17 | 25 | CFO | Employee benefit expense growth YoY (actual) | ~20% | — | — |
| 18 | 25 | CFO | Employee cost growth guidance FY27 | ~20% | GUIDANCE (restates #17 as forward) | — |
| 19 | 25 | CFO | Cost of service growth YoY | 20.7% | — | — |
| 20 | 41 | CMD | Employee expense growth (Q&A restate) | ~20% | repeat of #17/#18 | — |
| 21 | 49 | CMD | FY27 revenue growth guidance | 15 to 18% | GUIDANCE (range, 1 row per spoken range) | — |
| 22 | 53 | CMD | Industry organized share, floor | 15% | (range spoken as "15-20%") | — |
| 23 | 53 | CMD | Industry organized share, ceiling | 20% | (same range as #22) | — |
| 24 | 53 | CMD | Unorganized/future opportunity share | 80% | — | — |
| 25 | 65 | CMD | Revenue growth restated | 17-18% | repeat of #1/#9 range | — |
| 26 | 81 | CMD | Trip growth restated | ~27% | repeat of #2/#3 | — |
| 27 | 81 | CMD | Revenue growth restated (vs trip growth, price-reduction context) | ~17% | repeat, contrasted with trip growth | — |
| 28 | 87 | CMD | Employee cost growth restated | ~20% | repeat of #17/#18/#20 | — |
| 29 | 95 | CMD (inline, unlabeled) | Online booking % of total bookings, this quarter | 14% | "prior quarter around the same" (qualitative, not a hard number) | — |

### 4b. Currency figures — INR / ₹ (14 rows)

| # | Line | Speaker | Metric | Value | Comparator given | Flags |
|---|---|---|---|---|---|---|
| 30 | 21 | CFO | Revenue from operations, quarter | INR 2,113.72 mn | — | — |
| 31 | 21 | CFO | EBITDA, quarter | INR 218.47 mn | vs INR 219.18 mn Q1FY26, INR 241.53 mn Q4FY26 | — |
| 32 | 21 | CFO | EBITDA, Q1 FY26 | INR 219.18 mn | — | — |
| 33 | 21 | CFO | EBITDA, Q4 FY26 | INR 241.53 mn | — | — |
| 34 | 25 | CFO | Employee benefit expense, quarter | INR 237.63 mn | — | — |
| 35 | 25 | CFO | Other expenses, quarter | INR 70.32 mn | vs INR 81.54 mn Q1FY26 | — |
| 36 | 25 | CFO | Other expenses, Q1 FY26 | INR 81.54 mn | — | — |
| 37 | 25 | CFO | Profit before tax, quarter | INR 191.64 mn | vs INR 186.68 mn Q1FY26 | — |
| 38 | 25 | CFO | Profit before tax, Q1 FY26 | INR 186.68 mn | — | — |
| 39 | 25 | CFO | Profit after tax, quarter | INR 145.50 mn | vs INR 132.87 mn Q1FY26 | — |
| 40 | 25 | CFO | Profit after tax, Q1 FY26 | INR 132.87 mn | — | — |
| 41 | 27 | CFO | Cash and investments, as of 30 June 2026 | INR 1,558 mn | — | — |
| 42 | 27 | CFO | Final dividend recommended, FY26 | INR 2.38 per share | subject to AGM approval | forward/contingent |
| 43 | 75 | CMD | Revenue threshold for operating-leverage inflection | over ₹1,000 crores | GUIDANCE | — |

### 4c. Whole-number operational KPIs, non-%/non-currency (24 rows)

| # | Line | Speaker | Metric | Value | Comparator given | Flags |
|---|---|---|---|---|---|---|
| 44 | 10 | CMD | New clients added, quarter | 61 | — | — |
| 45 | 12 | CMD | Cities of presence, end of quarter | 151 | — | — |
| 46 | 12 | CMD | New cities added, quarter | 20 | — | — |
| 47 | 12 | CMD | Cities, end of FY26 (baseline) | 130-plus | — | — |
| 48 | 12 | CMD | Countries covered (international network) | more than 100 | — | — |
| 49 | 12 | CMD | Trips completed, quarter | ~1.48 million | — | — |
| 50 | 14 | CMD | New clients added, quarter (restated) | 61 | repeat of #44 | — |
| 51 | 14 | CMD | New clients added, Q1 FY26 | 53 | — | — |
| 52 | 14 | CMD | Active client base, quarter | 1,400 enterprise organizations | — | — |
| 53 | 14 | CMD | Customer tenure threshold cited | more than 5 years | — | — |
| 54 | 14 | CMD | Fleet, owned + vendor-operated, as of 30 June 2026 | ~19,500 vehicles | — | — |
| 55 | 14 | CMD | EV fleet, end of quarter | 460 vehicles | vs 390 end of Q4FY26 | — |
| 56 | 14 | CMD | EV fleet, end of Q4 FY26 | 390 vehicles | — | — |
| 57 | 45 | CMD | Automation platform development time (CCR) | almost 2 years | — | — |
| 58 | 53 | CMD | Trips delivered per year (scale claim) | more than 5 million | — | — |
| 59 | 63 | CMD | Company operating history cited | over 30 years | — | — |
| 60 | 77 | CMD | Total client base (broader than "active") | perhaps more than 1,700 | reconciling analyst's cited 1,750 | — |
| 61 | 77 | CMD | Active clients, quarter (restated) | 1,400 | repeat of #52 | — |
| 62 | 81 | CMD | Fleet, restated (rounded) | ~19,000 | repeat of #54 | — |
| 63 | 81 | CMD | Daily vehicle utilization, floor | 10,000 vehicles/day | — | — |
| 64 | 81 | CMD | Daily vehicle utilization, ceiling | 11,000 vehicles/day | — | — |
| 65 | 96 | CMD (inline, unlabeled) | Active client base, quarter (restated) | Around 1,400 | repeat of #52/#61 | — |
| 66 | 100 | CMD | New ETS clients added, quarter | 15 | "one of the highest ... in any quarter" | — |
| 67 | 100 | CMD | New CCR clients added, quarter | 46 | sums with #66 to the 61 total (#44/#50) | arithmetic cross-check: 15+46=61, consistent |

---

## SECTION 5 — GUIDANCE / FORWARD-LOOKING STATEMENTS (14 rows; grep 14, sweep 14, match)

| # | Line | Speaker | Statement | Flags |
|---|---|---|---|---|
| 1 | 16 | CMD | B2C app expected to launch this quarter (Q2 FY27), addressing premium CCR B2C demand | — |
| 2 | 16 | CMD | SIXT partnership "progressing as planned," continued distribution build-out | — |
| 3 | 18 | CMD | FY27 priorities: high-quality enterprise adds, wallet-share growth, selective geo expansion, leadership bandwidth, tech-led efficiency | — |
| 4 | 23 | CFO | FY27 EBITDA margin guidance revised to ~10% (down from prior 11-13%) | supersedes prior guidance |
| 5 | 25 | CFO | FY27 employee cost expected to grow ~20% | — |
| 6 | 27 | CFO | Coming quarters' focus: operating efficiency and better operating leverage | — |
| 7 | 27 | CFO | Final dividend of INR 2.38/share for FY26 recommended, subject to AGM shareholder approval | contingent/pending |
| 8 | 33 | CMD | Internal threshold set below which new business will not be taken | — |
| 9 | 39 | CMD | M&A: "will be looking at certain opportunities... in coming quarters we will give a better picture" | deferred/vague |
| 10 | 45 | CMD | CCR automation to be settled within this quarter, then deliver productivity results | — |
| 11 | 49 | CMD | FY27 revenue growth guidance reaffirmed at 15-18% | — |
| 12 | 75 | CMD | Operating leverage expected to inflect at revenue over ₹1,000 crores | key structural guidance number |
| 13 | 87 | CMD | Continued leadership-bandwidth hiring investment through the year, tempered by productivity/automation/AI | — |
| 14 | 91 | CMD | B2C app: no high target this year; "from next year we will schedule a guidance" | guidance explicitly deferred |

---

## SECTION 6 — HEDGE PHRASES (10 rows; grep 10, sweep 10, match)

| # | Line | Speaker | Phrase | Context |
|---|---|---|---|---|
| 1 | 33 | CMD | "We are hopeful of maintaining these margins going ahead this year" | Margin guidance |
| 2 | 39 | CMD | "in coming quarters we will give a better picture" | M&A |
| 3 | 45 | CMD | "Those are the two basic strategies I can publicly reveal" | Cost-cutting detail withheld |
| 4 | 63 | CMD | "That's a million dollar question" | Margin floor under competition |
| 5 | 65 | CMD | "Not majorly. Maybe one or two..." | Client losses |
| 6 | 75 | CMD | "we are not sure of the longevity of this intensity of competition" | Margin trajectory |
| 7 | 83 | CMD | "It's very hard to predict competitors' actions, so I would not comment on moderation" | Pricing-pressure trend |
| 8 | 91 | CMD | "we don't have a high target this year, but from next year we will schedule a guidance" | B2C app |
| 9 | 98 | CMD | "some may not give business for a few months and then restart" | Active-client definition, softening the metric |
| 10 | 103 | CMD | "We are hopeful of keeping the momentum going" | Closing |

---

## SECTION 7 — NON-DISCLOSURE / ZERO-STANDING ANSWERS (6 rows; grep 6, sweep 6, match)

Per task instruction: zero/nil and "we do not disclose" answers are data, not gaps to drop.

| # | Line | Speaker | Item declined / nil | Flags |
|---|---|---|---|---|
| 1 | 37 | CMD | Event-management revenue line described as "not very material" — no size given | ZERO_STANDING |
| 2 | 65 | CMD | Client losses to competition — "not majorly," 1-2 non-renewals, no count given | ZERO_STANDING |
| 3 | 69 | CMD | ETS vs CCR segment EBITDA margin split — explicitly declined ("No, we do not declare that") | ZERO_STANDING (canonical example per task instruction) |
| 4 | 83 | CMD | View on whether ETS pricing-pressure is moderating vs FY26 — explicitly declined to comment | ZERO_STANDING |
| 5 | 91 | CMD | B2C app FY27 revenue/user target — none given, deferred to FY28 guidance cycle | ZERO_STANDING |
| 6 | 92 | [DRJ] / CMD | Oil-price impact on vendor economics — question itself incomplete, transcript records no management answer at all | DROPPED_QUESTION (distinct from ZERO_STANDING: here the gap is a missing transcript/response, not a management decline) |

---

## SUMMARY OF ALL FLAGS RAISED

- NUMBER_DISCREPANCY: 1 (line 21 — transcribed EBITDA margin 9.3% vs bracketed reported/audited
  10.34%; carry both forward, do not silently pick one)
- ZERO_STANDING: 5 (lines 37, 65, 69, 83, 91)
- DROPPED_QUESTION: 1 (line 92 — incomplete follow-up, no recorded management answer)
- MULTI_QUESTION_TURN: 1 (line 95 — two distinct asks bundled in one transcript line)
- REPEAT_QUESTION: 3 topic clusters spanning 7 individual question turns (margin trajectory:
  lines 32/56/74; employee cost: lines 40/86; active-client count: lines 76/96)
- name-not-fully-transcribed / name-ambiguous-in-transcript: 3 analysts (Q4, Q8, Q9 — surnames
  or full names garbled/bracketed in source transcript)

Cross-checks noted (not flags, informational): 15 ETS + 46 CCR new clients (line 100) sums to
61 total, consistent with the 61 new clients cited at lines 10 and 14 — internally consistent.
Fleet figures 19,500 (line 14) and ~19,000 (line 81, rounded restatement) are consistent.
Active client base 1,400 (lines 14, 77, 96) is restated consistently across three separate
turns; the ">1,700 total clients" vs "1,400 active clients" distinction (line 77) is
management's own reconciliation of an analyst-flagged apparent inconsistency (line 76,
REPEAT_QUESTION) — carried as data, not resolved/interpreted here per A2 scope.
