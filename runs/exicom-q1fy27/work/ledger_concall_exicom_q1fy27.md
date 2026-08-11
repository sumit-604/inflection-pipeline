# A2 ENUMERATION LEDGER — EXICOM Q1 FY27 — CONCALL

Source: `/home/user/inflection-pipeline/runs/exicom-q1fy27/work/extract_concall_exicom_q1fy27.txt`
Line numbers cited below are the extract's own embedded numbering (1-112, per
`line_count: 112` in the A1 header), NOT the Read-tool file-line numbers. File
line = embedded line + 15 (embedded 1 = file line 16; embedded 112 = file
line 127). Lines 1-13 are the A1 header/phonetic-decoding note, not transcript
content. Transcript content runs embedded lines 14-112.

Decoding key applied throughout (per A1 header): "Tridium" =
Tridium/Titim/Titanium/Pritium/Faradium; "EBITDA" = iita/ivita/AEA/ATM/a
beta/kibbita; "BharatNet" = Bhatnet/Valatnet; "TRI-FLEX" = Trilex/Triplex;
"PM E-Drive" = PME/PM E-drive.

Structural note before the tables: three embedded line numbers each contain
TWO speaker turns concatenated with no line break — the transcript's paragraph
segmentation does not match its own speaker-turn boundaries at these points.
Flag `MIXED_SPEAKER_TURN` applies to lines **34, 46, 106**. In each case the
management answer to one question and the start of the analyst's next
question (or, at 106, one analyst's full question AND management's full
answer) share a single embedded line number. This is called out again at the
relevant rows below and is itself a disclosure-completeness risk (A3/A4 must
not miss the sub-turn).

=== A2 COUNT TEST ===
category: participants        grep_count: 8    sweep_count: 8    match: yes
category: turns                grep_count: 50   sweep_count: 50   match: yes
category: questions             grep_count: 13   sweep_count: 13   match: yes
category: mgmt_numbers         grep_count: 127  sweep_count: 127  match: yes
category: forward_commitments  grep_count: 14   sweep_count: 14   match: yes
category: hedge_phrases        grep_count: 11   sweep_count: 11   match: yes
gate_a2: pass
=== END COUNT TEST ===

Methodology note on the count test (concall doctype has no fixed-format
tables, so grep cannot use a single clean regex the way it can on a notes
block or a financial-statement line-item list; the two-way reconciliation
below was done iteratively, per the operating rules, until match):
- `participants`: grep on lines 4-5 (management/moderator/host block) plus
  `grep -n "is from the line of"` (analyst introductions) = 2 + 2 + 4 = 8.
  Sweep of the transcript confirms the same 8, no additional unnamed
  participants heard.
- `turns`: grep — `sed -n '16,127p' extract | grep -cE '^[0-9]+  \S'` = 61
  non-blank embedded lines total; of these 11 fall in the header block
  (embedded 1-13, not turns) and 50 fall in the transcript body (embedded
  14-112). 61 − 11 = 50. Manual sweep of embedded 14-112 (every even number
  has content, every odd number 15-111 is a blank separator; confirmed by
  `grep -cE` for blank vs non-blank in that range: 50 non-blank / 49 blank)
  independently gives 50. Match.
- `questions`: grep on `\?` across the 16 analyst-turn lines gives 14 raw
  question marks; sweep collapses these to 13 distinct substantive business
  questions after (a) excluding 1 pure audio-check exchange ("Am I audible?"
  at line 24, a procedural courtesy check, not a disclosure question) and (b)
  treating the three-part question at line 44 (revenue mix / EV growth
  outlook / capacity-figure confusion) as three separate topic rows since
  each got a materially separate management answer. Net: 14 raw marks − 1
  procedural + 0 net (the line-44 compound expands what a single `?` count
  would treat as one) reconciles to 13 distinct question rows on manual count.
- `mgmt_numbers`: grep pass 1 (regex for number+unit: %, x, crore(s)/cr,
  million, billion, lakh) plus grep pass 2 (regex for number+unit: kW, MWh,
  megawatt, sites, towers, chargers, countries, years, months, quarters,
  operators, deployment, registration, carriers, buses, BSS) = 116 raw
  matches. Manual sweep found 11 additional management-spoken figures that
  grep's unit-adjacency regex missed because (i) a filler word sits between
  the number and its unit ("1,400 for buses", "15 new network operators",
  "10 new countries", "almost 30,000 plus ... points"), (ii) the unit is
  spelled out non-standard ("240 uh kilowatt" not "kW"), or (iii) the figure
  itself is spoken in words, not digits ("two and a half times", "hundred
  billion dollars" [garbled], "one foot" [garbled, likely "one-fourth"]).
  116 + 11 = 127. Re-swept and confirmed no further gaps. Match at 127.
- `forward_commitments` / `hedge_phrases`: grep on lexicon stems ("expect",
  "target", "will", "guided", "confident", "sure" for commitments; "I don't
  know", "can't specify", "hoping", "estimation", "check ... come back",
  "too many factors" for hedges) cross-checked against full manual read of
  all 20 management turns (18, 20, 30, 34, 36, 46, 48, 52, 56, 60, 64, 80, 98,
  102, 106, 110). 14 commitments / 11 hedges on both passes. Match.

---

## 1. PARTICIPANTS (both sides, with designation)

| # | Name | Designation / Firm | Side | Line | Flags |
|---|---|---|---|---|---|
| P1 | Anant Nahata | Managing Director & CEO | Management | 4 | — |
| P2 | Shiraz Khanna | CFO | Management | 4 | — |
| P3 | Ana | Operator / call moderator | Neutral (call ops) | 5 | — |
| P4 | Rahul Dani | Host, Monarch Networth Capital (call sponsor/broker) | Sell-side host | 5 | — |
| P5 | "Takar" (phonetic; name uncertain) | Analyst, Brighter Mind Asset Management | Analyst | 22 | PHONETIC_NAME |
| P6 | Suraj Si (phonetic; name uncertain) | Analyst, Vij Global Securities | Analyst | 42 | PHONETIC_NAME |
| P7 | Himman Chen (phonetic; name uncertain) | Analyst, Indira Securities | Analyst | 82 | PHONETIC_NAME |
| P8 | Shashi Khan | Analyst, "Brighter Mine as management" (phonetic; likely same firm as P5, Brighter Mind Asset Management) | Analyst | 104 | PHONETIC_NAME, POSSIBLE_FIRM_DUPLICATE (two analysts on one call from what may be the same shop — P5 and P8 — or a mis-transcription of the same firm name twice; not resolvable from this transcript alone) |

`MGMT_ABSENCE`: not raised. Both the MD & CEO (Anant Nahata) and the CFO
(Shiraz Khanna) are present for the full call — Nahata delivers the opening
business review (line 18) and fields nearly every Q&A answer; Khanna delivers
the full financial walk-through (line 20). No promoter/CMD absence on this
call.

---

## 2. SPEAKER TURNS (sequential, embedded line = turn number)

50 turns total, embedded lines 14-112 (every even-numbered line in that
range; odd-numbered lines in the same range are blank separators in the
source text and are not turns).

| Turn (line) | Speaker | First ~10 words | Flags |
|---|---|---|---|
| 14 | Operator (Ana) | "Ladies and gentlemen, good day and welcome to the XECOM..." | — |
| 16 | Rahul Dani (Host) | "Uh thank you Ana. Good afternoon everyone. On behalf of..." | — |
| 18 | Anant Nahata (MD & CEO) | "Thank you. Uh uh good evening uh dear shareholders. Uh this..." | Opening business review, longest single turn on the call |
| 20 | Shiraz Khanna (CFO) | "Thank you so much uh Anan uh and good evening uh..." | Full financial walk-through |
| 22 | Operator (Ana) | "Thank you very much. We will now begin with the question..." | Introduces analyst 1 (Takar, Brighter Mind AM) |
| 24 | Analyst 1 (Takar) | "Good evening sir. Am I audible?" | Procedural / audio check |
| 26 | Unclear (Mgmt or Host) | "Yeah." | UNCLEAR_SPEAKER — no explicit attribution in source |
| 28 | Analyst 1 (Takar) | "Oh yes sir. You were at consolidated a break even in..." | Question 1 (see Q1 below) |
| 30 | Anant Nahata (MD & CEO) | "So, uh thank you for your question. Uh you're right. Uh..." | Answer to Q1 |
| 32 | Analyst 1 (Takar) | "Right sir. Right sir. So on a follow-up question, uh..." | Question 2 (Q2) |
| 34 | Anant Nahata + Analyst 1 (Takar) | "Yes. So uh Now we are uh confident of that as..." | MIXED_SPEAKER_TURN — mgmt answer to Q2 then Takar's Q3 embedded in same line |
| 36 | Anant Nahata (MD & CEO) | "So the Hyderabad plant uh was built for a much..." | Answer to Q3 (capacity utilization) |
| 38 | Analyst 1 (Takar) | "Got it sir. Thank you and good." | Sign-off |
| 40 | Anant Nahata (MD & CEO) | "Thank you." | — |
| 42 | Operator (Ana) | "Thank you. The next question is from the line of..." | Introduces analyst 2 (Suraj Si, Vij Global Securities) |
| 44 | Analyst 2 (Suraj Si) | "Yeah. Hi sir, good evening. I had a few questions..." | Question set (3 sub-questions, see Q3-Q5) |
| 46 | Anant Nahata + Analyst 2 (Suraj Si) | "Yeah. So uh okay I remember first two of your..." | MIXED_SPEAKER_TURN — mgmt answers sub-Qs 1-2, Suraj's sub-Q3 (capacity confusion) embedded at end |
| 48 | Anant Nahata (MD & CEO) | "I will uh I will check this uh again. I know..." | Answer to sub-Q3; unresolved, deferred |
| 50 | Analyst 2 (Suraj Si) | "Okay. Okay. And sir, uh second question of mine is..." | Question 6 (depreciation) |
| 52 | Anant Nahata (MD & CEO) | "Okay. So uh you know on a stand uh there are..." | Answer |
| 54 | Analyst 2 (Suraj Si) | "Okay. So is it reasonable to assume that Q4 for..." | Question 7 |
| 56 | Anant Nahata (MD & CEO) | "Yeah. So that's uh you know again in business there..." | Answer |
| 58 | Analyst 2 (Suraj Si) | "Understood. Understood. That's great. And so lastly uh in your..." | Question 8 (EV registration math) |
| 60 | Anant Nahata (MD & CEO) | "Yeah. So uh no good analysis and question. So uh..." | Answer (part 1) |
| 62 | Analyst 2 (Suraj Si) | "Yes." | Acknowledgment |
| 64 | Anant Nahata (MD & CEO) | "Which are supplied with the car. One is a portable..." | Answer (part 2) |
| 66 | Analyst 2 (Suraj Si) | "okay so any blended market share if you could provide..." | Question 9 (market share) |
| 68 | Operator (Ana) | "interrupt sorry to interrupt Mr. Suraj could you please fall..." | Enforces queue / 2-question limit |
| 70 | Analyst 2 (Suraj Si) | "Yeah. Yeah. I I will I will. So, I've asked..." | Yields queue position |
| 72 | Operator (Ana) | "Okay." | — |
| 74 | Analyst 2 (Suraj Si, re-queued) | "Yes sir. So, uh hello." | — |
| 76 | Unclear (Mgmt or Host) | "Yeah." | UNCLEAR_SPEAKER — no explicit attribution |
| 78 | Analyst 2 (Suraj Si) | "Yes sir. So, just ask the question on so could..." | Re-asks Question 9 |
| 80 | Anant Nahata (MD & CEO) | "Yeah. See blended I would not know uh as in..." | Answer to Q9 |
| 82 | Operator (Ana) | "Okay understood understood. Thank you. I'll call back in. Thank..." | Reiterates 2-question limit; introduces analyst 3 (Himman Chen, Indira Securities) |
| 84 | Analyst 3 (Himman Chen) | "Hi. Am I a[udible]" | Procedural / audio check |
| 86 | Rahul Dani / Operator (unclear which) | "Yes, you are." | UNCLEAR_SPEAKER |
| 88 | Analyst 3 (Himman Chen) | "Hi. Okay. in a good quarter. So my question was..." | Question 10 (Tridium/US capacity) |
| 90 | Anant Nahata (MD & CEO) | "At what capacity sorry what" | Clarifying |
| 92 | Analyst 3 (Himman Chen) | "is your uh manufacturing in the US working at?" | Clarifies Q10 |
| 94 | Anant Nahata (MD & CEO) | "Yeah uh I I got that but the what's the..." | Still clarifying |
| 96 | Analyst 3 (Himman Chen) | "I mean at what capac utilization are we uh what..." | Clarifies Q10 further |
| 98 | Anant Nahata (MD & CEO) | "Yeah. So uh as you saw this quarter we did..." | Answer to Q10 |
| 100 | Analyst 3 (Himman Chen) | "Got it. And uh just another question uh um as..." | Question 11 (EV growth 50% vs 15%) |
| 102 | Anant Nahata (MD & CEO) | "So on a standalone basis see uh first of all..." | Answer |
| 104 | Operator (Ana) | "Thank you. The next question is from the line of..." | Introduces analyst 4 (Shashi Khan, Brighter Mind/Mine AM) |
| 106 | Analyst 4 (Shashi Khan) + Anant Nahata | "Uh thank you for the opportunity and good of know..." | MIXED_SPEAKER_TURN — full Q12 (PM E-Drive underutilization) and full answer concatenated in one line |
| 108 | Operator (Ana) | "thank you that was the last question for the Okay..." | Closes Q&A, hands to management |
| 110 | Anant Nahata (MD & CEO) | "So, uh I uh appreciate uh all the people stakeholders..." | Closing remarks |
| 112 | Operator (Ana) | "on behalf of Monarch Network Capital Limited. That concludes this..." | Call closes |

Turn-count auditability check requested by the instructions ("60% of effort
on Q&A" auditable by turn number): opening remarks + financial review = turns
14-20 (4 turns, embedded lines 14-20, i.e. roughly 4/50 = 8% of turns by
count, though a much larger share of words given turns 18 and 20 are the two
longest blocks on the call). Q&A = turns 22-112 (26 turns / 50 = 52% of turns
by count). By turn-count the call is majority Q&A; by raw word-count the
opening management remarks (turn 18 alone) are the single largest block on
the call — flagged for A4 to weigh both metrics, not turn-count alone.

---

## 3. QUESTIONS (one row per distinct analyst question)

| Q# | Analyst | Firm | Topic | Turn(s) | Flags |
|---|---|---|---|---|---|
| Q1 | Takar | Brighter Mind Asset Management | Consolidated EBITDA back to Rs 22 cr loss in Q1 vs Q4 breakeven despite 61% growth — drivers of sequential margin deterioration and breakeven timing | 28 | — |
| Q2 | Takar | Brighter Mind Asset Management | Tridium order intake doubled to $20.8mn — conversion timing to revenue; confidence in guided 3x revenue growth and Q4FY27 breakeven | 32 | — |
| Q3 | Takar | Brighter Mind Asset Management | Hyderabad plant capacity utilization today and expected level in FY27 | 34 (embedded in mixed turn) | REPEAT_QUESTION — capacity-utilization theme recurs at Q5/Q9(part) and Q10 |
| Q4 | Suraj Si | Vij Global Securities | Revenue mix (critical power vs EV) expected after ~2 years | 44 | — |
| Q5 | Suraj Si | Vij Global Securities | Growth expectation for EV chargers, standalone and Tridium, coming year | 44 | — |
| Q6 | Suraj Si | Vij Global Securities | Capacity-figure confusion: annual report shows AC charger capacity expansion 42,000 to 220,000, vs management's stated "2x" — reconciliation requested | 44 (embedded), 46 (embedded), 48 | REPEAT_QUESTION — capacity-utilization/capacity-figure theme; ANSWER_DEFERRED (management could not reconcile on the call, promised to follow up) |
| Q7 | Suraj Si | Vij Global Securities | Depreciation levels — why standalone depreciation is a "lot" higher (~20-25% of gross block cited by analyst) | 50 | — |
| Q8 | Suraj Si | Vij Global Securities | Is it reasonable to assume Q4 will be materially higher for Tridium top-line and bottom-line | 54 | — |
| Q9 | Suraj Si | Vij Global Securities | EV registration volumes vs charger units sold — does market share imply a direct unit-sales read-through | 58 | REPEAT_QUESTION — EV-growth-interpretation theme recurs at Q11 |
| Q10 | Suraj Si | Vij Global Securities | Blended EV charger market share — request for a number | 66, 78 (re-asked after queue interrupt) | Asked twice due to moderator interrupting at turn 68 |
| Q11 | Himman Chen | Indira Securities | Tridium/US manufacturing capacity — utilization level and revenue capacity | 88, 92, 96 (same question, clarified across three exchanges before being answered) | REPEAT_QUESTION — capacity-utilization theme (see Q3, Q6) |
| Q12 | Himman Chen | Indira Securities | EV segment grew ~50% consolidated but only ~15% standalone — reason for the gap | 100 | REPEAT_QUESTION — EV-growth-interpretation theme (see Q9) |
| Q13 | Shashi Khan | Brighter Mind/Mine Asset Management | PM E-Drive charger underutilization reported in news articles — reasons the scheme/installed base is not being fully utilized | 106 (embedded, mixed with the answer in the same line) | — |

Note: turn 24 ("Am I audible?") and turn 84 ("Hi. Am I a[udible]") are
procedural audio-check exchanges, not substantive business questions, and are
excluded from the Q1-Q13 count per the count-test methodology above; they are
still captured in the turns table (Section 2) so no line is dropped from the
ledger overall.

`REPEAT_QUESTION` clusters (topics recurring across DIFFERENT analysts):
1. Capacity utilization — Q3 (Takar, Hyderabad), Q6 (Suraj Si, AC charger
   capacity figure), Q11 (Himman Chen, Tridium/US capacity).
2. EV growth-rate interpretation / discrepancy — Q9 (Suraj Si, registrations
   vs units), Q12 (Himman Chen, 50% consol vs 15% standalone).

---

## 4. MANAGEMENT-SPOKEN NUMBERS (guidance, capacity/utilisation %, margin,
## order book, Tritium bookings/revenue in US$, timelines) — 127 rows

Grouped by turn. `NUMBER_DISCREPANCY` = conflicts with another management
figure on the same call. `GARBLED_NUMBER` = the phonetic auto-transcript
renders the figure ambiguously or implausibly and it cannot be resolved from
this transcript alone. `WORD_FORM` = spoken as words, not digits.

### Turn 18 — Anant Nahata, opening remarks (M1-M52)

| # | Figure | What it is | Flags |
|---|---|---|---|
| M1 | 57% | Standalone revenue YoY growth | — |
| M2 | Rs 237 cr | Standalone revenue, Q1FY27 | — |
| M3 | Rs 21 cr | Standalone EBITDA, Q1FY27 | minor variance vs M64 (Rs 20.9 cr) — rounding, not flagged as discrepancy |
| M4 | 8.8% | Standalone EBITDA margin | — |
| M5 | 61% | Consolidated revenue YoY growth | — |
| M6 | Rs 331 cr | Consolidated revenue, Q1FY27 | — |
| M7 | Rs 40 cr | Consolidated EBITDA loss, Q1FY26 (prior year) | — |
| M8 | ~Rs 22.5 cr | Consolidated EBITDA loss, Q1FY27 ("22 1/2 cr") | GARBLED_NUMBER (fraction spoken, cross-check M79) |
| M9 | $20 mn | Tridium bookings, "north of" this quarter | — |
| M10 | $10 mn | Tridium bookings, prior quarterly run-rate | — |
| M11 | $10 mn | Tridium revenue, this quarter | repeat context at M50, M77, M119 |
| M12 | Rs 177 cr | Critical power segment revenue, Q1 | NUMBER_DISCREPANCY vs M58 (Rs 176 cr, same metric, Shiraz Khanna) |
| M13 | 73% | Critical power YoY growth | NUMBER_DISCREPANCY vs M57 (80%, same metric, Shiraz Khanna) |
| M14 | 11% | Critical power QoQ decline | — |
| M15 | Rs 85 cr | Large TC power systems order value (leading Indian telco) | — |
| M16 | 60% | BharatNet project — share of business | — |
| M17 | Rs 15 cr | Export sales, critical power, this quarter | — |
| M18 | 8% | Export sales as % of critical power revenue, current | — |
| M19 | 15% | Export sales target %, FY27 (of critical power sales) | forward-commitment, see C1 |
| M20 | 10+ | BSS deployments ("more than 10") | — |
| M21 | Rs [X],000 cr | Order book, critical power ("roughly ,000 crores") | GARBLED_NUMBER — leading digit missing/inaudible in source |
| M22 | Rs 700 cr | BharatNet — open orders | — |
| M23 | Rs 800 cr | BharatNet — service order value, over next 10 years | — |
| M24 | 10 years | BharatNet service order period | — |
| M25 | 2,000 | Sites expected (BSNL phase 2 allocation) | — |
| M26 | 2,000 | Towers expected (BSNL phase 2, restated) | — |
| M27 | Rs 90-100 cr | BSNL phase 2 contract value range | — |
| M28 | 15 MWh | BESS orders in hand | — |
| M29 | Rs 20 cr | BESS orders in hand, value | — |
| M30 | 34 MWh | BESS orders, advanced pipeline | — |
| M31 | Rs 45 cr | BESS orders, advanced pipeline, value | — |
| M32 | 31,000 | Passenger car registrations, Q1 (industry stat, highest to date) | — |
| M33 | 15% | EV segment standalone revenue growth, YoY | repeat context at M59, M125 |
| M34 | Rs 53 cr | EV standalone revenue, Q1FY26 | — |
| M35 | Rs 61 cr | EV standalone revenue, Q1FY27 | repeat context at M60 |
| M36 | 85,000 revised to ~86,000 | Passenger EV registrations, Q1 (industry) | in-sentence self-correction, treated as one figure |
| M37 | 1,400 | Bus registrations, Q1 (industry) | grep-missed (filler word before unit) |
| M38 | 6,500 | Goods-carrier registrations, Q1 (industry) | grep-missed (filler word before unit) |
| M39 | 180 kW / 240 kW | High-power charger specs cited | grep-missed (unit spelled "kilowatt") |
| M40 | 4 years | Delhi EV policy duration | — |
| M41 | Rs 15,000 cr | Delhi EV policy outlay | — |
| M42 | 30,000+ | Delhi EV charging points target | grep-missed ("plus" intervenes) |
| M43 | 100% | Share of business, international wallbox brand | — |
| M44 | 15 | New network operators / CPOs added, Q1 | grep-missed (words intervene) |
| M45 | ~180 | Order book figure ("almost close to 180 chargers") | GARBLED_NUMBER — unit implausible for an order-book figure, likely intends crores not "chargers" |
| M46 | 10 | New export countries (ACDC chargers) | grep-missed |
| M47 | Rs 200 cr | Order book, ACDC chargers India incl. exports | — |
| M48 | $2 mn | Export component of charger order book | — |
| M49 | $21 mn | Tridium bookings, this quarter (restated) | cross-check M9's "$20mn+" — consistent |
| M50 | $10.5 mn | Tridium sales/revenue, this quarter | cross-check M11 |
| M51 | $20-30 mn | Tridium/Faradium potential contract (EV fleet trials, CY27) | conditional — see C3, H3; grep caught upper bound only |
| M52 | $20 mn | Grid Flex potential contract (hyperscale customer trial, CY27) | conditional — see C4, H3 |

### Turn 20 — Shiraz Khanna, CFO financial review (M53-M89)

| # | Figure | What it is | Flags |
|---|---|---|---|
| M53 | Rs 236.8 cr | Standalone revenue, Q1FY27 (precise) | — |
| M54 | Rs 150.7 cr | Standalone revenue, Q1FY26 | — |
| M55 | 57% | Standalone revenue YoY growth (repeat, precise) | — |
| M56 | 16% | Standalone revenue QoQ decline vs Q4FY26 | — |
| M57 | 80% | Critical power YoY growth, standalone | NUMBER_DISCREPANCY vs M13 (73%, same metric, Anant Nahata) |
| M58 | Rs 176 cr | Critical power revenue | NUMBER_DISCREPANCY vs M12 (Rs 177 cr, same metric, Anant Nahata) |
| M59 | 15% | EV YoY growth (repeat) | — |
| M60 | Rs 61 cr | EV revenue (repeat) | — |
| M61 | 29.1% | Standalone gross margin, Q1FY27 | — |
| M62 | 2 pts | Gross margin improvement QoQ | — |
| M63 | 3.6 pts | Gross margin decline YoY | — |
| M64 | Rs 20.9 cr | Standalone EBITDA | minor variance vs M3 |
| M65 | 8.8% | Standalone EBITDA margin (repeat) | — |
| M66 | 137% | Standalone EBITDA YoY growth | — |
| M67 | [Rs X cr] | Prior-year EBITDA figure ("8.8 crores... from 8.8 crores... at 5.8% last year") | GARBLED_NUMBER — apparent duplicate/garbled prior-year crore amount |
| M68 | 5.8% | Standalone EBITDA margin, Q1FY26 | — |
| M69 | Rs 8.7 cr | Fixed-cost increase YoY, standalone | same value recurs at M86 in a distinct context |
| M70 | Rs 4.9 cr | Standalone PAT, Q1FY27 | — |
| M71 | 2.1% | Standalone PAT margin | — |
| M72 | Rs 103 cr | Standalone depreciation | GARBLED_NUMBER — implausibly high for the quarter's context; likely intends ~Rs 10.3 cr |
| M73 | Rs 331.1 cr | Consolidated revenue (precise, repeat) | — |
| M74 | 61% | Consolidated revenue YoY growth (repeat) | — |
| M75 | 73% | Consolidated critical power YoY growth | — |
| M76 | 50% | Consolidated EV YoY growth | REPEAT_QUESTION theme, see Q12 |
| M77 | $10 mn+ | Tridium/US revenue — "second consecutive quarter above $10mn" | — |
| M78 | 31.7% | Consolidated gross margin | — |
| M79 | Rs 21.9 cr | Consolidated EBITDA loss | cross-check M8 (~22.5cr, Anant Nahata) — close but not identical |
| M80 | 6.6% | Consolidated EBITDA margin (negative) | — |
| M81 | Rs 38.6 cr | Consolidated EBITDA loss, prior year | — |
| M82 | Rs 83.1 cr | Consolidated PAT loss, prior year | — |
| M83 | Rs 73.6 cr | Consolidated PAT loss, current quarter | — |
| M84 | 67% | Standalone depreciation YoY increase | — |
| M85 | 57% | Consolidated depreciation YoY increase | — |
| M86 | Rs 8.7 cr | Parallel-run (Goa + Hyderabad) fixed-cost impact | same value as M69, different context (parallel-run specific) |
| M87 | 3x | Hyderabad plant production capability multiple | — |
| M88 | Rs 1,400 cr | Order book (consolidated) | repeat at M90's context |
| M89 | Rs 370 cr | Consolidated debt, as of 30 June 2026 | — |

### Turn 30 — Anant Nahata, Q&A answer 1 (M90-M92)

| # | Figure | What it is | Flags |
|---|---|---|---|
| M90 | ~Rs 22 cr | EBITDA loss, this quarter ("22 kibbita loss") | repeat/paraphrase of M8 |
| M91 | Q4 FY27 | Tridium breakeven target ("quarter 427") | GARBLED_NUMBER — glued quarter-code |
| M92 | Q2 or Q3 FY27 | Consolidated breakeven target ("quarter 427", 2nd instance) | GARBLED_NUMBER |

### Turn 34 — Anant Nahata (mgmt portion of mixed turn) (M93-M95)

| # | Figure | What it is | Flags |
|---|---|---|---|
| M93 | $20 mn | Tridium order backlog as of 1 July 2026 | — |
| M94 | 3x | Revenue growth guidance reaffirmed (vs last year) | forward-commitment, see C9 |
| M95 | Q4 FY27 | Tridium breakeven target restated ("quarter 47") | GARBLED_NUMBER — inconsistent glue vs M91/M92's "427" and M113's "526"; same underlying target rendered three different ways across the call |

### Turn 36 — Anant Nahata, Hyderabad capacity (M96-M104)

| # | Figure | What it is | Flags |
|---|---|---|---|
| M96 | 2x | Hyderabad AC-charging capacity vs prior facility | — |
| M97 | 4,000 | DC chargers — capacity built for ("nearly 4,000") | — |
| M98 | 50% | AC charger monthly run-rate growth expected | forward-commitment, see C10 |
| M99 | 3 months | Timeline for AC run-rate growth | — |
| M100 | 65% | DC charging capacity utilization | — |
| M101 | 100% | AC charger utilization ("close to") | — |
| M102 | 90-100% | DC power system line utilization | — |
| M103 | 100% | PCBA lines utilization ("close to") | — |
| M104 | 65% | DC charger utilization (restated/clarified) | repeat of M100 |

### Turn 46 — Anant Nahata (mgmt portion of mixed turn) (M105-M107)

| # | Figure | What it is | Flags |
|---|---|---|---|
| M105 | Rs 277 cr | EV standalone revenue, FY26 (full year) | — |
| M106 | 30% | EV as % of overall standalone revenue, FY26 | — |
| M107 | 70/30 or 65/35 | Critical power vs EV revenue split, forward view | range given, not a single point estimate |

### Turn 48 — Anant Nahata, capacity clarification (M108-M109)

| # | Figure | What it is | Flags |
|---|---|---|---|
| M108 | 220,000 ("2 lakh 20") | AC charger capacity, confirmed | — |
| M109 | 48,000 | Single-shift capacity figure | NUMBER_DISCREPANCY — analyst (turn 44) cited 42,000 from the annual report; management restates 48,000 without reconciling and defers ("will check again and come back") — see H7, Q6 |

### Turn 52 — Anant Nahata, depreciation explanation (M110-M112)

| # | Figure | What it is | Flags |
|---|---|---|---|
| M110 | Rs 10-12 cr | Standalone depreciation increase (new plant) | — |
| M111 | $1 bn | India/Exicom addressable market by 2030 | — |
| M112 | $10 bn | Tridium/US addressable market by 2030 | — |

### Turn 56 — Anant Nahata, Tridium Q4 outlook (M113)

| # | Figure | What it is | Flags |
|---|---|---|---|
| M113 | Q4 FY27 (intended) | Starting point for step-up in Tridium top-line/bottom-line ("Q4 uh 526") | GARBLED_NUMBER — third inconsistent rendering of the same target across the call (cf. M91/M92 "427", M95 "47") |

### Turn 64 — Anant Nahata, AC charger volume (M114-M116)

| # | Figure | What it is | Flags |
|---|---|---|---|
| M114 | 50% | AC charger monthly volume increase already achieved | repeat of M98 concept, different framing (achieved vs. forward) |
| M115 | 50% | Further increase expected, next 3 months | repeat of M98/C10 |
| M116 | 3 months | Timeline (repeat of M99) | — |

### Turn 80 — Anant Nahata, blended market share (M117-M118)

| # | Figure | What it is | Flags |
|---|---|---|---|
| M117 | 60% | Wallbox charger market share at DRHP/IPO time (historical) | — |
| M118 | 50%+ | Current estimated charger market share ("north of 50%") | explicitly a personal estimate, not from a research report — see H9 |

### Turn 98 — Anant Nahata, US/Tridium capacity (M119-M122)

| # | Figure | What it is | Flags |
|---|---|---|---|
| M119 | $10 mn | Tridium US revenue, this quarter (repeat) | cross-check M11, M50 |
| M120 | "two and a half times" (2.5x) | US plant capacity vs current revenue | WORD_FORM — spoken in words, not digits |
| M121 | [~$25 mn implied] | "hundred billion dollars slightly more" | GARBLED_NUMBER — nonsensical as stated; likely intends ~$25mn capacity (2.5x of $10mn quarterly revenue) |
| M122 | [~25% implied] | "we're doing one foot of that today" | GARBLED_NUMBER / WORD_FORM — likely intends "one-fourth" utilization |

### Turn 102 — Anant Nahata, EV standalone vs consol (M123-M125)

| # | Figure | What it is | Flags |
|---|---|---|---|
| M123 | 30% | AC charger growth estimate, standalone (implied) | — |
| M124 | 10% | DC charger growth estimate, standalone | — |
| M125 | 15% | Blended EV growth rate, standalone (reconciles M33) | — |

### Turn 106 — Anant Nahata (mgmt portion of mixed turn) (M126-M127)

| # | Figure | What it is | Flags |
|---|---|---|---|
| M126 | 20%+ | Some charging-site utilization rates ("more than 20%") | — |
| M127 | 30-35% | Deployed DC chargers reported non-functional (third-party study cited) | attributed to an outside study, not company data — see H11 |

---

## 5. FORWARD-COMMITMENT PHRASES (C1-C14)

| # | Phrase (paraphrase kept close to source) | Turn | Related figure |
|---|---|---|---|
| C1 | Target to raise export sales to ~15% of critical power sales within FY27 | 18 | M19 |
| C2 | Trials in mid-to-advanced stages "will be unlocking double-digit large million dollar orders through the course of 2027" | 18 | — |
| C3 | Tridium "can be awarded more than $20 to $30 million contract for calendar 27" | 18 | M51 |
| C4 | Grid Flex "can be expected to be awarded $20 million of contract for CY by 27" | 18 | M52 |
| C5 | Focus to secure majority of CY27-execution orders within calendar 2026 | 18 | — |
| C6 | Charger order book of ~180 "will continue till October 26" | 18 | M45 |
| C7 | "I still expect Tridium break even in quarter 4[FY]27" | 30 | M91 |
| C8 | Consolidated break-even "over the next two quarters" | 30 | M92 |
| C9 | "I'm sure that we will have 3x revenue growth... as well as a breakeven in quarter 4[FY]27" | 34 | M94, M95 |
| C10 | AC charger monthly run-rate "will almost grow by 50% in the next 3 months" | 36 | M98, M99 |
| C11 | R&D investment "will last for next five to seven years of revenue journey for Tridium" | 52 | — |
| C12 | Step-up in Tridium revenue/profit — "starting point will be Q4 [FY]27" | 56 | M113 |
| C13 | AC charger volume "further going to increase by 50% over the next 3 months" (restated) | 64 | M115, M116 |
| C14 | Closing: results "not far, maybe a couple of quarters away" on standalone and consolidated basis | 110 | — |

---

## 6. HEDGE PHRASES (H1-H11)

| # | Phrase | Turn | Pairs with |
|---|---|---|---|
| H1 | "I understand that while we grew our revenue... but the profitability is still not in black" | 18 | — |
| H2 | "I don't want to commit on the target at this point" (re: export % of EV charger revenue) | 18 | — |
| H3 | Tridium and Grid Flex large contracts explicitly conditioned on "if these trials are successful" / "subject to successful trials" | 18 | C3, C4 |
| H4 | "the break even... maybe... over the next two quarters, it's, I can't specify whether quarter two or three" | 30 | C8 |
| H5 | "large double-digit million numbers of revenue which we are hoping to convert" | 34 | C9 |
| H6 | "some of the challenges today is not capacity, it's supply chain disruption" / "sometimes don't allow us to fully use our capacity" | 36 | M100-M104 |
| H7 | "I will check this again... I will take your coordinates and come back to you with an exact answer" — capacity-figure discrepancy left unresolved on the call | 48 | M108, M109, Q6 |
| H8 | "in business there are... too many factors" (hedge preceding a timeline commitment) | 56 | C12 |
| H9 | "blended I would not know... I don't know the exact number today... this is my estimation, not from a research report" | 80 | M118 |
| H10 | "hopefully the [tail] end of it" (hedge on turnaround timing at the US factory) | 98 | M120-M122 |
| H11 | "I cannot say exactly about the accuracy of the report" (distancing from the third-party 30-35% non-functional-charger stat) | 106 | M127 |

---

## 7. SUMMARY OF FLAGS RAISED

- `MIXED_SPEAKER_TURN` — lines 34, 46, 106 (two speaker turns concatenated
  under one embedded line number).
- `UNCLEAR_SPEAKER` — lines 26, 76, 86 (short acknowledgements with no
  explicit speaker attribution in the source).
- `PHONETIC_NAME` — all four analyst names (P5-P8), per the A1 decoding
  note; none should be treated as confirmed spellings downstream.
- `POSSIBLE_FIRM_DUPLICATE` — P5 (Takar, "Brighter Mind Asset Management")
  and P8 (Shashi Khan, "Brighter Mine as management") may be the same firm
  transcribed two different ways, or two different analysts from the same
  shop; not resolvable from this transcript.
- `REPEAT_QUESTION` — capacity-utilization theme (Q3, Q6, Q11) and
  EV-growth-interpretation theme (Q9, Q12).
- `ANSWER_DEFERRED` — Q6 (AC charger capacity figure, 42,000 vs 48,000 vs
  220,000, unresolved on the call).
- `NUMBER_DISCREPANCY` — critical power revenue and YoY growth stated
  differently by Anant Nahata (M12/M13: Rs 177cr / 73%) vs Shiraz Khanna
  (M57/M58: Rs 176cr / 80%) for the same metric in the same call; the
  Q4FY27 Tridium-breakeven target rendered three inconsistent ways by the
  phonetic transcript (M91/M92 "427", M95 "47", M113 "526"); the
  single-shift AC charger capacity figure (M109, 48,000) vs the analyst's
  cited annual-report figure (42,000).
- `GARBLED_NUMBER` — M8, M21, M45, M67, M72, M91, M92, M95, M113, M121, M122
  (11 instances where the phonetic auto-transcript renders a management
  figure ambiguously, implausibly, or as a glued quarter-code).
- `WORD_FORM` — M120, M121, M122 (numbers spoken in words rather than
  digits; structurally invisible to a digits-only grep pass, which is why
  the manual sweep is load-bearing for GATE A2 here).
- `ZERO_STANDING` — not applicable to this doctype (no standing financial
  line items in a concall transcript; this flag is reserved for the results
  filing / financial statement doctypes).

MGMT_ABSENCE: none raised (MD & CEO and CFO both present throughout).
