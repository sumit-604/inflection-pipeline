=== A2 COUNT TEST ===
category: turns          grep_count: 53   sweep_count: 53   match: yes
category: questions      grep_count: 15   sweep_count: 15   match: yes
category: mgmt_numbers   grep_count: n/a  sweep_count: 67   match: n/a (no single regex captures free-text spoken numbers; manual sweep only, see method note)
gate_a2: pass
=== END COUNT TEST ===

Method notes:
- turns: grep pattern `\[TURN [0-9]+:` against
  `work/extract_concall_indgn_q1fy27.txt` returns 53 matches (verified via
  `grep -n -E "\[TURN [0-9]+:"`, see command run). Manual sweep = read the
  full 1001-line extract start to finish, incrementing a counter at every
  `[TURN n: Speaker]` marker, confirming n runs 1..53 with no gap, no repeat,
  no marker missing a sequential number. 53 == 53. GATE A2 PASS for turns.
- questions: manual sweep of the 53 turns for analyst-authored interrogative
  content addressed to management = 15 distinct questions (see ROSTER below).
  Sanity cross-check: `grep -c "?"` on the whole extract returns 27 (multiple
  "?" per compound question, e.g. Turn 7 contains two question marks within
  one question thread) — consistent with, not equal to, the 15-question
  count; question-mark literal count is not a valid proxy for question count
  in this transcript because analysts routinely stack 2+ interrogative
  clauses inside one turn. 15 is the sweep-verified figure and is what feeds
  GATE A2 turns/questions reconciliation stated above.
- mgmt_numbers: no single grep pattern reliably isolates spoken figures
  embedded in prose (currency figures, %, bps, day-counts, multiples, year
  ranges all use different tokens). Enumerated by manual sweep only; count
  stated as sweep_count, match marked n/a per instruction to record both
  methods where feasible and state the limitation where a grep pass is not
  meaningful.

All line numbers below are the A1 EXTRACT's own embedded line numbers
(1..1001, printed in the extract file text itself), not the Read-tool
display offset (which is embedded + 15 due to the 15-line header block).

---

## 1. PARTICIPANTS (both sides)

| # | Name | Designation | Side | Turns appearing | Flags |
|---|------|-------------|------|------------------|-------|
| 1 | Manish Gupta | Chairman and Chief Executive Officer | Management | 3,5,8,14,16,18,20,23,25,30,32,35,37,40,47,49,52 (17 turns) | |
| 2 | Suhas Prabhu | Chief Financial Officer | Management | 4,9,11,15,24,27,31,42,45,50 (10 turns) | |
| 3 | Abhishek Agarwal | Head, Investor Relations | Management | 2 (1 turn, intro only; silent through Q&A) | |
| 4 | Moderator | Call operator (third-party) | Facilitator | 1,6,12,21,28,33,38,43,51,53 (10 turns) | |
| 5 | Sucrit Patil | Analyst | Analyst — Eyesight Fintrade | 7,10 (2 turns) | |
| 6 | Prolin Nandu | Analyst | Analyst — Edelweiss Public Alternatives | 13,17,19 (3 turns) | |
| 7 | Vinay Menon | Analyst | Analyst — Monarch Capital | 22,26 (2 turns) | |
| 8 | Prakash Kapadia | Analyst | Analyst — Kapadia Financial Services | 29 (1 turn) | |
| 9 | Varun Bahl | Analyst | Analyst — Plutus Investment | 34,36 (2 turns) | |
| 10 | Chandan Kumar | Analyst | Analyst — Narnolia Financial Services | 39,41 (2 turns) | |
| 11 | Chirag Kachhadiya | Analyst | Analyst — Motilal Oswal Financial Services | 44,46,48 (3 turns) | |

Turn-count reconciliation: Moderator 10 + Agarwal 1 + Gupta 17 + Prabhu 10 +
analysts (2+3+2+1+2+2+3=15) = 53. Matches total turn count exactly.

CMD/Chairman presence check: Manish Gupta (Chairman and CEO) present and
active in both prepared remarks and Q&A. No `MGMT_ABSENCE` flag.

---

## 2. EVERY SPEAKER TURN (53 of 53)

| Turn | Speaker | First ~10 words | Line |
|------|---------|------------------|------|
| 1 | Moderator | Ladies and gentlemen, good day, and welcome to the Indegene | 92 |
| 2 | Abhishek Agarwal | Thank you, moderator. A very good morning to all of | 103 |
| 3 | Manish Gupta | Thank you, Abhishek. Good morning, everyone, and thank you for | 119 |
| 4 | Suhas Prabhu | Thank you, Manish. Once again, a very good morning to | 375 |
| 5 | Manish Gupta | Thank you, Suhas. Let me close with a few words | 467 |
| 6 | Moderator | The first question comes from the line of Sucrit Patil | 498 |
| 7 | Sucrit Patil | I have 2 questions. The first question to Mr. Gupta | 501 |
| 8 | Manish Gupta | Let me take a step back. At a broader level, | 509 |
| 9 | Suhas Prabhu | And Sucrit, you also spoke about the risks. What we | 542 |
| 10 | Sucrit Patil | My second question to Mr. Suhas is, from a financial | 549 |
| 11 | Suhas Prabhu | Coming to the currency volatility, we have in the last | 555 |
| 12 | Moderator | The next question comes from the line of Prolin Nandu | 595 |
| 13 | Prolin Nandu | I have just one question, and I want to start | 598 |
| 14 | Manish Gupta | Let me break this up. And I'll give you a | 617 |
| 15 | Suhas Prabhu | Yes. Maybe just to reiterate, if I was not clear, | 666 |
| 16 | Manish Gupta | The last one, let me come back, is the capitalization | 672 |
| 17 | Prolin Nandu | Just so what I understand, and just to correct me | 682 |
| 18 | Manish Gupta | Six quarters was from October 2025. So, it's no longer | 687 |
| 19 | Prolin Nandu | But this is despite the fact that you have invested | 690 |
| 20 | Manish Gupta | Yes, absolutely. | 694 |
| 21 | Moderator | The next question comes from the line of Vinay Menon | 697 |
| 22 | Vinay Menon | A couple of things, what was the organic growth this | 700 |
| 23 | Manish Gupta | We're not breaking up organic and inorganic growth from a | 704 |
| 24 | Suhas Prabhu | And sequentially, both are in the base... | 720 |
| 25 | Manish Gupta | Yes. Both are in the base from a sequence perspective. | 723 |
| 26 | Vinay Menon | Okay. And what was the constant currency growth for this | 726 |
| 27 | Suhas Prabhu | Vinay, we disclosed U.S. dollar growth, given that about 84%-85% | 730 |
| 28 | Moderator | The next question comes from the line of Prakash Kapadia | 736 |
| 29 | Prakash Kapadia | Two questions from my end. You talked about some outcome-based | 739 |
| 30 | Manish Gupta | Let me talk about the outcome and output things and | 753 |
| 31 | Suhas Prabhu | Sure. And Prakash, as Manish mentioned, most of our engagements | 785 |
| 32 | Manish Gupta | If I just can add in on this part, the | 804 |
| 33 | Moderator | The next question comes from the line of Varun Bahl | 808 |
| 34 | Varun Bahl | My question is regarding your Gen AI strategy. If you | 811 |
| 35 | Manish Gupta | That's a great question, and I'm glad you asked that. | 817 |
| 36 | Varun Bahl | Yes, it's on a slightly broader market question, especially since | 873 |
| 37 | Manish Gupta | Not really. The companies, especially the larger companies, will be | 879 |
| 38 | Moderator | The next question comes from the line of Chandan Kumar | 894 |
| 39 | Chandan Kumar | I just have a question. You have recently highlighted your | 905 |
| 40 | Manish Gupta | Chandan, unfortunately, we can't break this out because unlike other | 910 |
| 41 | Chandan Kumar | I have one more question. You have given the EBITDA | 928 |
| 42 | Suhas Prabhu | Other than the costs that are already incurred, given our | 933 |
| 43 | Moderator | The next question comes from the line of Chirag Kachhadiya | 940 |
| 44 | Chirag Kachhadiya | Just on margin part. So, from 4Q FY27 should we | 944 |
| 45 | Suhas Prabhu | Yes, Chirag. | 948 |
| 46 | Chirag Kachhadiya | Okay. And Manish, few broader questions. The deals which we | 951 |
| 47 | Manish Gupta | Yes, yes. What we call out over here is net | 956 |
| 48 | Chirag Kachhadiya | And what is generally the renewal deals in the organic | 960 |
| 49 | Manish Gupta | Our net retention has been more than 100% for our | 971 |
| 50 | Suhas Prabhu | Yes. And typically, renewal cycles are Jan to December. And | 974 |
| 51 | Moderator | Ladies and gentlemen, we will take that as the last | 980 |
| 52 | Manish Gupta | Thank you once again for your active participation and continued | 984 |
| 53 | Moderator | Thank you, sir. Ladies and gentlemen, on behalf of Indegene | 989 |

Turn count: 53. Matches header `speaker_turn_count: 53` and GATE A2 count
test above.

---

## 3. Q&A ROSTER — every question, every answer, firm by firm

Prepared remarks (Turns 1-5) are not Q&A; management commitments within them
are captured in Section 5.

| Q# | Question turn | Analyst | Firm | Topic | Answer turn(s) | Flags |
|----|----|---------|------|-------|-----------------|-------|
| Q1 | 7 | Sucrit Patil | Eyesight Fintrade | Top 2-3 execution priorities for coming quarters; biggest client-adoption risk (regulatory / compliance / competitive) and mitigation | 8 (Manish - priorities), 9 (Suhas - regulatory risk) | |
| Q2 | 10 | Sucrit Patil | Eyesight Fintrade | Financial risks/challenges ahead: margin, cash flow, balance sheet strength, receivables, currency volatility | 11 (Suhas) | |
| Q3 | 13 | Prolin Nandu | Edelweiss Public Alternatives | Apparent inconsistency: H2 margin normalization vs. Q4-specific normalization stated in opening remarks; is there a delay?; nature of the margin-compressing expenses (true investment vs. recurring opex); would management capitalize instead of expense? | 14 (Manish - trajectory/no delay), 15 (Suhas - reiterate 6-quarter confidence), 16 (Manish - capitalization answer) | |
| Q3a | 17 | Prolin Nandu | Edelweiss Public Alternatives | Follow-up: confirm summary — margin target reached in 6 quarters despite large new deal investments | 18 (Manish) | Same thread as Q3 |
| Q3b | 19 | Prolin Nandu | Edelweiss Public Alternatives | Follow-up: confirm this 6-quarter target holds despite investments possibly not factored into original guidance | 20 (Manish - "Yes, absolutely") | Same thread as Q3 |
| Q4 | 22 | Vinay Menon | Monarch Capital | Organic growth this quarter; BioPharm contribution breakup | 23 (Manish - declines breakup), 24 (Suhas), 25 (Manish) | DEFLECTED — organic/BioPharm % explicitly not disclosed ("We're not breaking up organic and inorganic growth from a BioPharm perspective, anymore", turn 23, line 704) |
| Q5 | 26 | Vinay Menon | Monarch Capital | Constant-currency growth for the quarter (not in the presentation) | 27 (Suhas - gives approximation 2.6%-2.7%) | PARTIAL — approximation given, not a precise disclosed figure (turn 27, line 730) |
| Q6 | 29 | Prakash Kapadia | Kapadia Financial Services | (a) % of business that is outcome-based / is this the industry norm going forward; (b) order-book and execution-cycle mechanics for how revenue/margin initiatives flow to the P&L | 30 (Manish - (a)), 31 (Suhas - (b)), 32 (Manish - add-on) | |
| Q7 | 34 | Varun Bahl | Plutus Investment | Gen AI strategy detail: proprietary model build for vertical oncology; integration with frontier models vs. open-source Chinese AI models; IP protection narrative and frontier-model cost pressure | 35 (Manish) | |
| Q7a | 36 | Varun Bahl | Plutus Investment | Follow-up: client concerns on data ownership / data protection when integrating frontier models | 37 (Manish) | Same thread as Q7 |
| Q8 | 39 | Chandan Kumar | Narnolia Financial Services | % of revenue currently generated through AI-led platform engagements; expected mix evolution over next 2-3 years | 40 (Manish - declines to quantify) | DEFLECTED — explicit refusal to quantify ("Chandan, unfortunately, we can't break this out...", turn 40, line 910) |
| Q9 | 41 | Chandan Kumar | Narnolia Financial Services | Key margin driver(s) other than costs already incurred, supporting the FY27-end return to historical EBITDA range | 42 (Suhas) | |
| Q10 | 44 | Chirag Kachhadiya | Motilal Oswal Financial Services | Confirm Q4 FY27 margin range will be ~19%-20% | 45 (Suhas - "Yes, Chirag") | REPEAT_QUESTION — restates the margin-normalization confirmation already covered in Q3/Q3a/Q3b (turns 13-20) and in Turn 4 (line 375 onward) |
| Q11 | 46 | Chirag Kachhadiya | Motilal Oswal Financial Services | Are the deals targeted over the past year incremental to the existing revenue base, or replacing it? | 47 (Manish - "net new business", no renewal counted) | |
| Q12 | 48 | Chirag Kachhadiya | Motilal Oswal Financial Services | What is the typical annual renewal rate within the organic business? | 49 (Manish - net retention >100%), 50 (Suhas - renewal-cycle mechanics, 2-3% variance) | |

Question count: 12 primary questions + 3 same-thread follow-ups (Q3a, Q3b,
Q7a) = 15 question turns total (turns 7,10,13,17,19,22,26,29,34,36,39,41,
44,46,48). Matches sweep_count in COUNT TEST.

Analyst firm roster (7 distinct firms, all questions answered in some form;
none left wholly unanswered; 2 flagged DEFLECTED where quantification was
explicitly declined; 1 flagged REPEAT_QUESTION; 1 flagged PARTIAL):
Eyesight Fintrade, Edelweiss Public Alternatives, Monarch Capital, Kapadia
Financial Services, Plutus Investment, Narnolia Financial Services, Motilal
Oswal Financial Services.

---

## 4. EVERY NUMBER SPOKEN BY MANAGEMENT (with turn + line)

| # | Turn | Line | Speaker | Metric | Value |
|---|------|------|---------|--------|-------|
| 1 | 3 | 129 | Manish Gupta | Global pharma industry growth, H1 2026 YoY | mid to high single digits |
| 2 | 3 | 132 | Manish Gupta | Top 20 global pharma cumulative revenue growth, Q1 calendar YoY | ~10%-12% |
| 3 | 3 | 140 | Manish Gupta | Biopharma (top 25) posting double-digit revenue growth in Q1 | 8 of 25 |
| 4 | 3 | 143 | Manish Gupta | Big pharma spend on biopharma M&A, H1 (pace for largest since 2019) | >$100 billion |
| 5 | 3 | 162 | Manish Gupta | Omnichannel marketing deal size (won/announced Q3, referenced) | $10 million-plus |
| 6 | 3 | 173 | Manish Gupta | Q1 FY27 revenue | INR10,631 million |
| 7 | 3 | 174 | Manish Gupta | Q1 FY27 revenue growth YoY | 39.7% |
| 8 | 3 | 174 | Manish Gupta | Q1 FY27 revenue growth QoQ | 6% |
| 9 | 3 | 180 | Manish Gupta | Active client base | crossed 100, reached 105 |
| 10 | 3 | 181 | Manish Gupta | Revenue from accounts beyond top 20 as share of total | more than a third |
| 11 | 3 | 181 | Manish Gupta | New customers added to $10-25 million bucket this quarter | 2 (cohort now 9) |
| 12 | 3 | 183 | Manish Gupta | Revenue per employee, TTM | ~$77,000 |
| 13 | 3 | 206 | Manish Gupta | Enterprise Commercial deal signed, $3-5 million range | 1 deal |
| 14 | 3 | 207 | Manish Gupta | Deals signed, $1-3 million annual-contract range | 4 deals (3 commercial, 1 medical) |
| 15 | 3 | 349 | Manish Gupta | Total revenue growth since Q1 FY25 (listing quarter) | up 57% |
| 16 | 3 | 350 | Manish Gupta | Active client base growth since listing | 65 to 105 |
| 17 | 3 | 350 | Manish Gupta | Million-dollar-plus clients growth since listing | 36 to 54 |
| 18 | 3 | 351 | Manish Gupta | Revenue from accounts beyond top 20 growth since listing | more than 2.5x |
| 19 | 3 | 356 | Manish Gupta | Revenue per employee growth over last 2 years | 25%, to over $77,000 |
| 20 | 3 | 357 | Manish Gupta | Delivery talent with healthcare background, then vs. now | risen to 29% from 22% |
| 21 | 3 | 358 | Manish Gupta | Cash position strengthening over same 2-year period | over 30% |
| 22 | 4 | 380 | Suhas Prabhu | Q1 FY27 revenue (USD) | USD 112.5 million |
| 23 | 4 | 380 | Suhas Prabhu | Q1 FY27 revenue growth YoY (USD terms) | 26.5% |
| 24 | 4 | 381 | Suhas Prabhu | Q1 FY27 revenue growth QoQ (USD terms) | 2.5% |
| 25 | 4 | 384 | Suhas Prabhu | Q1 FY27 EBITDA | INR1,795 million |
| 26 | 4 | 384 | Suhas Prabhu | Q1 FY27 EBITDA margin | 16.9% |
| 27 | 4 | 385 | Suhas Prabhu | EBITDA margin change QoQ, reported basis | +50 bps |
| 28 | 4 | 386-387 | Suhas Prabhu | Prior-quarter adverse MTM impact (undesignated forward contracts, pre hedge-accounting) | ~240 bps |
| 29 | 4 | 409 | Suhas Prabhu | PBT | INR1,527 million |
| 30 | 4 | 409 | Suhas Prabhu | PBT growth sequential | +45.3% |
| 31 | 4 | 410 | Suhas Prabhu | Effective tax rate, quarter | 23.9% |
| 32 | 4 | 410-411 | Suhas Prabhu | PAT | INR1,162 million |
| 33 | 4 | 410-411 | Suhas Prabhu | PAT growth sequential | +45.9% |
| 34 | 4 | 411 | Suhas Prabhu | PAT margin (% of revenue) | 10.9% |
| 35 | 4 | 411 | Suhas Prabhu | PAT margin change sequential | up ~300 bps |
| 36 | 4 | 415 | Suhas Prabhu | Enterprise Commercial share of revenue | 70.6% |
| 37 | 4 | 415-416 | Suhas Prabhu | North America share of revenue | 75.1% |
| 38 | 4 | 416-417 | Suhas Prabhu | Revenue from accounts beyond top 20, YoY change (rupee terms) | almost doubled |
| 39 | 4 | 417 | Suhas Prabhu | Revenue from accounts beyond top 20, share of total | 33.4% |
| 40 | 4 | 422-423 | Suhas Prabhu | Active customer count, sequential change | +14, to 105 |
| 41 | 4 | 424 | Suhas Prabhu | DSO (net of unearned/unbilled) | 67 days |
| 42 | 4 | 424-425 | Suhas Prabhu | DSO change QoQ | +4 days |
| 43 | 4 | 425-426 | Suhas Prabhu | Cash & cash equivalents + investments | INR14,602 million |
| 44 | 4 | 431-432 | Suhas Prabhu | Prior guidance (Aug 2025 call): margin impact starting Q3 FY26 | 150 bps, 6-8 quarter normalization |
| 45 | 4 | 433-434 | Suhas Prabhu | Updated margin normalization timeline | 6 quarters, i.e. by Q4 FY27 |
| 46 | 4 | 458-459 | Suhas Prabhu | H2 FY27 EBITDA margin target range | 19%-20% |
| 47 | 8 | 511 | Manish Gupta | Customer-pyramid priority thresholds referenced | first $50 million accounts; moving more to $25 million |
| 48 | 11 | 568 | Suhas Prabhu | Share of revenue from top-20 + mid-tier pharma (strong balance sheets) | more than 90% |
| 49 | 11 | 575 | Suhas Prabhu | Historical look-back for minimal bad-debt/provisions claim | 27 years |
| 50 | 14 | 618-619 | Manish Gupta | First margin-hit guidance given | October 2025 (Q2 FY25-26 call) |
| 51 | 14 | 634-635 | Manish Gupta | Original normalization guidance range | 6 to 8 quarters |
| 52 | 14 | 640-641 | Manish Gupta | Updated normalization commitment | 6 quarters (not 6-8); back to 19%-20% by March end |
| 53 | 15 | 667-669 | Suhas Prabhu | Confirms updated normalization commitment | 6 quarters (from 6-8), by Q4 |
| 54 | 16 | 656-657 | Manish Gupta | Value of pharma-company brand portfolio managed under a strategic deal | more than $1 billion worth of products |
| 55 | 18 | 687 | Manish Gupta | Remaining quarters to margin-normalization target, restated from October 2025 baseline | 3 quarters (from current call date) |
| 56 | 27 | 730-733 | Suhas Prabhu | Revenue in U.S. dollar terms, share of total | 84%-85% |
| 57 | 27 | 732-733 | Suhas Prabhu | Constant-currency growth approximation (vs. 2.5% USD growth) | ~2.6%-2.7% |
| 58 | 30 | 754 | Manish Gupta | Share of business under output + outcome-based contracts | ~60% |
| 59 | 31 | 788-789 | Suhas Prabhu | Typical ramp-up period for $1-3M (up to ~$4M) hybrid deals | 3 to 4 quarters |
| 60 | 31 | 793 | Suhas Prabhu | Size of large outcome-based omnichannel deal announced Q3 FY26 | north of $10 million ACV |
| 61 | 31 | 795-797 | Suhas Prabhu | Revenue-recognition deferral on that deal | ~3 quarters (from go-live) |
| 62 | 32 | 804-805 | Manish Gupta | Duration client has been sharing revenue-uptick data on that engagement | 5 months |
| 63 | 40 | 919 | Manish Gupta | Content-volume growth enabled by automation methods | 5-7x |
| 64 | 44 | 944-945 | Chirag Kachhadiya (analyst, restated and confirmed by mgmt in 45) | Q4 FY27 margin range confirmed | 19%-20% |
| 65 | 49 | 971 | Manish Gupta | Net customer retention | more than 100% |
| 66 | 50 | 976-977 | Suhas Prabhu | Renewal-cycle length across customer base | 3-4 years, some 5 years |
| 67 | 50 | 976-977 | Suhas Prabhu | Renewal rate variance in absolute terms | 2%-3% plus/minus of the >100% base |

Excluded as non-figures (flagged, not counted): Turn 35 (line 819-820)
Manish Gupta's rhetorical contrast "we train 5,000 people, 10,000 people,
whatever it is" is an explicitly hypothetical framing device ("we will not
get into the trap of saying...") describing what the company does NOT
claim, not a disclosed actual figure — excluded from the mgmt_numbers count
above but flagged here as `RHETORICAL_NUMBER` so A3/A4 do not mistake it
for guidance. Similarly Turn 35 line 829 "200 reports" and "clinical study
reports, various protocol offering" is an illustrative capability list, not
a quantified metric — flagged `RHETORICAL_NUMBER`, excluded from the count.

Total distinct spoken quantified metrics enumerated: 67 rows above. This
figure is the final, reconciled sweep count and matches the sweep_count
stated in the COUNT TEST header at the top of this file.

---

## 5. FORWARD-COMMITMENT AND HEDGE PHRASES (candidate list for A3 lexicon classification)

| # | Turn | Line | Speaker | Phrase (paraphrase/quote) | Candidate type |
|---|------|------|---------|---------------------------|-----------------|
| 1 | 3 | 262 | Manish Gupta | "gives us the confidence to say that FY27 will be a stronger year than FY26" | FORWARD_COMMITMENT |
| 2 | 3 | 365-366 | Manish Gupta | "we are confident we will convert it into revenue soon" (re: top-account pipeline) | FORWARD_COMMITMENT |
| 3 | 4 | 405-406 | Suhas Prabhu | "thereby keeping our margins stable unlike the declining Q2 EBITDA margin that we have historically trended" | FORWARD_COMMITMENT |
| 4 | 4 | 433-434 | Suhas Prabhu | "the margin normalization is expected in 6 quarters, that is by Q4 of FY27" | FORWARD_COMMITMENT |
| 5 | 4 | 441 | Suhas Prabhu | "most of that revenue will flow straight to the bottom line" | FORWARD_COMMITMENT |
| 6 | 4 | 458-461 | Suhas Prabhu | "the EBITDA in H2 FY27 will be back in the range...19% to 20%. Nothing we have seen in this quarter changes that expectation...our conviction...has increased" | FORWARD_COMMITMENT |
| 7 | 5 | 469-470 | Manish Gupta | "we expect our organic growth in FY27 to be better than FY26, and we anticipate an acceleration in the second half" | FORWARD_COMMITMENT |
| 8 | 5 | 486 | Manish Gupta | "we expect the margin recovery to become clearly visible to you" | FORWARD_COMMITMENT |
| 9 | 9 | 545-546 | Suhas Prabhu | "currently, the policy outlook is stable...that's one thing that we are constantly on the lookout for" | HEDGE |
| 10 | 11 | 563-564 | Suhas Prabhu | "we believe that the currency volatility will not impact us at an operating margin level going forward" | FORWARD_COMMITMENT / HEDGE (qualified by "believe") |
| 11 | 11 | 592 | Suhas Prabhu | "I would say that the cash flow and receivable risk is not a significant one" | HEDGE |
| 12 | 14 | 638-641 | Manish Gupta | "there is no delay...it's going to be 6. By March end, we get back to that 19% to 20% range" | FORWARD_COMMITMENT |
| 13 | 15 | 667-669 | Suhas Prabhu | "we have strong confidence that we would be able to get there in 6 quarters" | FORWARD_COMMITMENT |
| 14 | 18 | 687 | Manish Gupta | "it's no longer 6 quarters from here, 3 quarters" | FORWARD_COMMITMENT |
| 15 | 20 | 694 | Manish Gupta | "Yes, absolutely" (confirming target holds despite added investment) | FORWARD_COMMITMENT (affirmation) |
| 16 | 23 | 704-706 | Manish Gupta | "We're not breaking up organic and inorganic growth from a BioPharm perspective, anymore" | HEDGE (disclosure withheld) |
| 17 | 31 | 799-801 | Suhas Prabhu | "the revenue recognition would start from Q3, as we anticipate, the revenue will start flowing directly to the bottom line" | FORWARD_COMMITMENT |
| 18 | 37 | 886-887 | Manish Gupta | "we believe the direction the market will go into is that larger pharma companies will want to have their own open weight models" | HEDGE (belief-qualified forward view) |
| 19 | 40 | 910 | Manish Gupta | "unfortunately, we can't break this out" | HEDGE (explicit non-disclosure) |
| 20 | 42 | 933-937 | Suhas Prabhu | "...are the other drivers that would get the margins back into this range because those are costs that are not going to increase in line with the increased revenue" | FORWARD_COMMITMENT |
| 21 | 47 | 956-957 | Manish Gupta | "What we call out over here is net new business. We don't talk about renewals in our earnings calls" | HEDGE (disclosure scope limited) |

---

## 6. FLAGS RAISED (roll-up)

- `DEFLECTED` x2 — Turn 23 (organic/BioPharm growth breakup declined) and
  Turn 40 (AI-led platform revenue % declined) — both explicit refusals to
  quantify a number an analyst directly requested.
- `REPEAT_QUESTION` x1 — Turn 44 (Chirag Kachhadiya, Motilal Oswal) restates
  the Q4 FY27 19%-20% margin confirmation already established across Turns
  13-20 (Prolin Nandu thread) and first stated by management unprompted in
  Turn 4.
- `RHETORICAL_NUMBER` x2 — Turn 35, lines 819-820 ("5,000 people, 10,000
  people") and line 829 ("200 reports") — illustrative, not disclosed
  actuals; excluded from the mgmt_numbers count, flagged so A3/A4 do not
  treat as guidance.
- No `MGMT_ABSENCE`: CEO and CFO both present and active throughout;
  IR head present for prepared remarks only, which is normal call structure,
  not a flag.
- No question left entirely unanswered. Two questions deflected (see
  DEFLECTED above); all others received a direct or partial answer.

---

## 7. NOT APPLICABLE TO THIS DOCTYPE

This document is a concall transcript (doctype: concall). The following A2
enumeration categories from the ENUMERATOR instructions do not apply and are
recorded here for completeness of the audit trail, not omitted silently:
numbered notes, financial-table line items / ZERO_STANDING, Board Outcome
agenda items, annexures/director profiles, auditor-report paragraphs,
consolidation entity list, digital signature blocks (results filings), and
slides/slide numbers (investor presentation). The SEBI Regulation 30
transmittal letter (lines 1-91, pages 1-2) preceding the transcript body is
a cover letter, not part of the 53 speaker turns; its content (signatory
Srishti Ramesh Kaushik, Company Secretary and Compliance Officer, digitally
signed 2026.08.06 10:37:59 +05'30', addressed to BSE and NSE) is noted here
for completeness but carries no turn number and is excluded from the turn
count per the A1 header (`speaker_turn_count: 53` begins at Turn 1, line 92).
