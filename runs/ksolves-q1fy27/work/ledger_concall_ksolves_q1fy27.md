# Completeness Ledger — Concall — Ksolves India Limited — Q1FY27

Source: `extract_concall_ksolves_q1fy27.txt` (751 header+body lines, 15 pages, 100% text-layer coverage, no OCR)
Prior-quarter ledger: not supplied — no diff performed, no `DROPPED_SLIDE` / prior-turn-count comparison possible this run.

```
=== A2 COUNT TEST ===
category: turns        grep_count: 74   sweep_count: 74   match: yes
category: questions     grep_count: 17   sweep_count: 17   match: yes
category: mgmt_numbers  grep_count: n/a  sweep_count: 34   match: n/a (no single regex covers all number formats; sweep only, see note below)
gate_a2: pass
=== END COUNT TEST ===
```

**Turn count reconciliation detail.** Grep pattern
`grep -nE "^(Moderator|Ratan Srivastava|Umang Soni|Manish Gurnani|Darpan Audichya|Parth Sodha|Apoorv Bandi|Vaibhav Chechani):"`
over the extract returns 74 matches. Per-speaker sub-grep (`grep -cE "^<name>:"` for
each of the 8 named speakers, summed) also returns 74 (Ratan Srivastava 30, Moderator
16, Apoorv Bandi 9, Umang Soni 5, Manish Gurnani 5, Vaibhav Chechani 5, Parth Sodha 4,
Darpan Audichya 0). Manual line-by-line sweep of the transcript body (lines 109-777),
listing every speaker-attributed line independently of the grep pattern, also produced
74 turns in the same sequence. All three counts reconcile at 74. GATE A2: PASS.

**Question count reconciliation detail.** Manual sweep of all 74 turns identified 17
turns that contain a substantive question (as opposed to acknowledgements, transitions,
thanks, or restatements): 1 from Parth Sodha, 6 from Apoorv Bandi, 2 from Vaibhav
Chechani, and 8 read by the Moderator on behalf of unnamed Q&A-tab submitters. Cross-
check: of the Moderator's 16 turns, 8 contain a "?"-bearing question payload (lines 445,
475, 502, 513, 522, 537, 556, 605); line 611 is a verbatim restatement of the line-605
question (Ratan asked "Can you repeat the question, please?" at line 609) and is not
counted as a second question. This reconciles to 17 by both methods (turn-content sweep
and moderator-payload sub-check). GATE A2: PASS.

**Mgmt-numbers count note.** No single grep pattern reliably captures every numeric
disclosure format used (Rs. X crore, X%, X basis points, X per share, $XK, "6 years",
"2 to 3 quarters" etc.) without heavy false-positive/false-negative noise (page numbers,
dates, DIN-style strings are absent here but percentages inside prose sentences vary in
form). This category is therefore sweep-only per row below; flagged `n/a` in the count
test rather than forced into a false match. No gate-relevant mismatch results because
gate A2 is scoped to the turn count (the anti-miss mechanism this pipeline exists to
protect), which is dual-counted and reconciled above.

---

## 1. Management / Moderator Panel Roster (from title page, lines 88-100)

| # | Name | Designation | Side | Line | Flags |
|---|------|-------------|------|------|-------|
| 1 | Ratan Srivastava | Founder, Chairman and Managing Director | Management | 88, 123, 134 | — |
| 2 | Umang Soni | Chief Financial Officer | Management | 90, 125, 230 | — |
| 3 | Manish Gurnani | Chief Technical Officer | Management | 92, 127, 401 | — |
| 4 | Darpan Audichya | Head, Business Transformation and Consulting | Management | 94-96, 129 | `SILENT_PANELIST` — listed on the panel and in the moderator's roll call (line 129) but has zero speaker turns across the entire 751-line transcript (grep for `^Darpan Audichya:` = 0 matches) |
| 5 | Siddhi Jain | Finportal Investments Private Limited (IR) — Moderator | Sell-side / IR (moderator) | 100 | Acts as Moderator throughout; individually named only on the title page, all in-transcript turns attributed to "Moderator:" |

Panel count: 4 management + 1 moderator = 5 named individuals. CMD (Ratan Srivastava) present and the dominant speaker (30/74 turns, 40.5%) — no `MGMT_ABSENCE` flag applicable.

---

## 2. Q&A Roster — Every Analyst / Firm Who Asked a Question

| # | Analyst | Firm | First question turn # | First question line | Total questions asked | Flags |
|---|---------|------|------------------------|----------------------|------------------------|-------|
| 1 | Parth Sodha | NOT FOUND (no firm affiliation stated anywhere in transcript) | 6 | 296 | 1 | `FIRM_NOT_DISCLOSED` |
| 2 | Apoorv Bandi | NOT FOUND (no firm affiliation stated anywhere in transcript) | 14 | 321 | 6 | `FIRM_NOT_DISCLOSED` |
| 3 | Vaibhav Chechani | NOT FOUND (no firm affiliation stated anywhere in transcript) | 57 | 645 | 2 | `FIRM_NOT_DISCLOSED` |
| 4 | Unnamed (Q&A-tab written submissions, read aloud by Moderator) | NOT FOUND — no submitter name attached to any of these 8 questions | 28 | 445 | 8 | `ANALYST_NOT_NAMED` (applies to all 8; see Question Ledger rows Q7-Q13, Q15) |

Named analysts: 3 (Parth Sodha, Apoorv Bandi, Vaibhav Chechani). Firms disclosed for any analyst: 0 — every analyst-firm cell is NOT FOUND. Only firm named on the call at all is the Moderator's own IR-agency affiliation, Finportal Investments Private Limited (line 100), which is not a sell-side/buy-side analyst firm and is not counted in the analyst-firm tally.

**Analyst-firm count for GATE A2 reporting: 3 analysts identified by name; 0 of 3 firms disclosed; 8 additional questions from anonymous Q&A-tab submitters with 0 names and 0 firms disclosed.**

---

## 3. Speaker Turn Ledger (all 74 turns, sequential)

| Turn | Line | Speaker | Role/Side | First ~10 words | Flags |
|------|------|---------|-----------|------------------|-------|
| 1 | 109 | Moderator | IR (Finportal) | "Good afternoon, everyone, and welcome to the Q1FY27..." | Opening |
| 2 | 134 | Ratan Srivastava | CMD | "Thank you. Welcome, and thank you, everyone, for joining..." | Opening remarks begin |
| 3 | 230 | Umang Soni | CFO | "Thank you, Ratan. Good day, everyone, and a very warm welcome." | Financials walkthrough begins |
| 4 | 286 | Moderator | IR | "Thank you to the management team for sharing their insights..." | Q&A session opens |
| 5 | 292 | Parth Sodha | Analyst | "Am I audible?" | Audio check, not a question |
| 6 | 294 | Umang Soni | CFO | "Yes, yes." | — |
| 7 | 296 | Parth Sodha | Analyst | "Good evening, and thank you for the opportunity. My first question..." | Q1 |
| 8 | 300 | Umang Soni | CFO | "For this quarter, certain large engagements were ramped down..." | A1 (partial) |
| 9 | 303 | Ratan Srivastava | CMD | "One second. Out of the 10, most of them are stable." | A1 continued |
| 10 | 311 | Parth Sodha | Analyst | "Got it. Thank you so much." | Acknowledgement |
| 11 | 313 | Ratan Srivastava | CMD | "Thank you. But one second, one thing I would like to add." | Unprompted addition |
| 12 | 317 | Parth Sodha | Analyst | "Got it. Thank you so much." | Acknowledgement, closes Q1 |
| 13 | 319 | Moderator | IR | "Thank you, sir. We will move on to the next question from Mr. Apoorv." | Transition |
| 14 | 321 | Apoorv Bandi | Analyst | "Thank you, sir, for the opportunity. My question is on the two clients..." | Q2 |
| 15 | 334 | Ratan Srivastava | CMD | "No, no. This is not the reason. In fact, we were working..." | A2 |
| 16 | 343 | Apoorv Bandi | Analyst | "Okay. Do we see any other challenges? As you mentioned..." | Q3 (follow-up) |
| 17 | 347 | Ratan Srivastava | CMD | "Okay, sure, definitely. See, Apoorv, this year we have completed six years..." | A3 |
| 18 | 365 | Apoorv Bandi | Analyst | "Okay. Sir, so do you see the current year to be the same as FY26?" | Q4 |
| 19 | 367 | Ratan Srivastava | CMD | "In terms of revenue?" | Clarifying question back |
| 20 | 369 | Apoorv Bandi | Analyst | "Right, yes." | Confirms, not a new question |
| 21 | 371 | Ratan Srivastava | CMD | "Yes, in terms of revenue, maybe. But as I said..." | A4 |
| 22 | 376 | Apoorv Bandi | Analyst | "Got it. So what I understood from your last statement was..." | Q5 |
| 23 | 388 | Ratan Srivastava | CMD | "Margins will not be impacted. The reason is that we are not hiring." | A5 |
| 24 | 394 | Apoorv Bandi | Analyst | "I remember from the con calls of the last couple of quarters..." | Q6 |
| 25 | 398 | Ratan Srivastava | CMD | "See, I can give you the answer, but I have my friend and CTO..." | Hands off to Manish |
| 26 | 401 | Manish Gurnani | CTO | "Sure. So first, how are we leveraging AI?..." | A6 |
| 27 | 433 | Apoorv Bandi | Analyst | "Got it. Thank you, sir. That's it from my end..." | Closes Apoorv's first round |
| 28 | 445 | Moderator | IR | "Thank you, sir. We have a few questions in the Q&A tab..." | Q7 (Q&A-tab, unnamed) |
| 29 | 449 | Ratan Srivastava | CMD | "So, we started with a very small amount of work..." | A7 (partial) |
| 30 | 455 | Manish Gurnani | CTO | "Alright. Think of it as one of the most leading banks in that region." | A7 continued |
| 31 | 469 | Ratan Srivastava | CMD | "Year-long. And the important thing is that this is..." | A7 continued |
| 32 | 475 | Moderator | IR | "Thank you, sir. Now we will move on to the next question: Your product business..." | Q8 (Q&A-tab, unnamed) |
| 33 | 480 | Ratan Srivastava | CMD | "So, in the last concall, I explicitly mentioned that we are now focusing..." | A8 |
| 34 | 502 | Moderator | IR | "Okay, thank you, sir. The next question is: North America contributes more than 60%..." | Q9 (Q&A-tab, unnamed) |
| 35 | 505 | Ratan Srivastava | CMD | "For the Middle East, I am not confident..." | A9 |
| 36 | 513 | Moderator | IR | "Okay, sir. The next question is related to the employee count..." | Q10 (Q&A-tab, unnamed) |
| 37 | 516 | Ratan Srivastava | CMD | "It is a very direct question. The answer is that when people are leaving..." | A10 |
| 38 | 522 | Moderator | IR | "Okay. The next question is: What is the average time it takes..." | Q11 (Q&A-tab, unnamed) |
| 39 | 526 | Ratan Srivastava | CMD | "Almost every customer is asking for AI in new proposals..." | A11 |
| 40 | 537 | Moderator | IR | "Sir, one more question: What percentage of revenue is recurring in nature..." | Q12 (Q&A-tab, unnamed) |
| 41 | 540 | Ratan Srivastava | CMD | "Umang, over to you." | Hands off to CFO |
| 42 | 551 | Umang Soni | CFO | "So, almost, I would say, more than 80% of our revenue..." | A12 |
| 43 | 556 | Moderator | IR | "Okay, sir. The next question is: Many companies are still experimenting with AI..." | Q13 (Q&A-tab, unnamed) |
| 44 | 559 | Ratan Srivastava | CMD | "Manish?" | Hands off to CTO |
| 45 | 561 | Manish Gurnani | CTO | "I do not know about others, but for us, it is already being implemented." | A13 |
| 46 | 571 | Moderator | IR | "Sir, we will take the next question from Mr. Apoorv. He has some follow-up questions." | Transition |
| 47 | 573 | Apoorv Bandi | Analyst | "Thank you, sir, for the follow-up. Sir, I was reading somewhere..." | Q14 |
| 48 | 579 | Ratan Srivastava | CMD | "No. I will answer your first question first. Token costs are not higher..." | A14 |
| 49 | 591 | Apoorv Bandi | Analyst | "Thank you." | Closes Apoorv's second round |
| 50 | 605 | Moderator | IR | "Thank you, sir. The next question is: In the services space, do we not feel threatened..." | Q15 (Q&A-tab, unnamed) |
| 51 | 609 | Ratan Srivastava | CMD | "Can you repeat the question, please?" | Requests repeat |
| 52 | 611 | Moderator | IR | "In the services space, do we feel threatened by the larger players..." | Q15 restated (not a new question) |
| 53 | 615 | Ratan Srivastava | CMD | "Manish, would you like to answer this?" | Hands off to CTO |
| 54 | 617 | Manish Gurnani | CTO | "Yes, let me take that. See, just yesterday, Ratan and I were discussing this." | A15 |
| 55 | 634 | Ratan Srivastava | CMD | "Yes. Adding here, even if they use AI, and we are already using AI..." | A15 continued |
| 56 | 642 | Moderator | IR | "Sir, I think we have a follow-up question from Mr. Vaibhav..." | Transition |
| 57 | 645 | Vaibhav Chechani | Analyst | "Hi, team. Thank you for the opportunity, and a solid set of numbers." | Q16 |
| 58 | 663 | Ratan Srivastava | CMD | "For the next five years, it is a very tough question for me to say..." | A16 (partial) |
| 59 | 670 | Vaibhav Chechani | Analyst | "One part has already been addressed." | Clarifies scope, not new question |
| 60 | 672 | Ratan Srivastava | CMD | "I got that. So, on new verticals, we are planning to start..." | A16 continued |
| 61 | 680 | Manish Gurnani | CTO | "Just to add to what Ratan said earlier, on your question about five years." | A16 continued |
| 62 | 694 | Ratan Srivastava | CMD | "One thing, since we are talking about the numbers. As I said in the last con call..." | A16 continued / unprompted numbers |
| 63 | 712 | Vaibhav Chechani | Analyst | "Thank you so much for the answer. I totally understand..." | Acknowledgement |
| 64 | 715 | Ratan Srivastava | CMD | "This year, unfortunately, my plan was that this year, again, I would give 18% to 20%." | Unprompted addition |
| 65 | 720 | Vaibhav Chechani | Analyst | "Thank you, sir. One last thing, any color on the deal pipeline..." | Q17 |
| 66 | 724 | Ratan Srivastava | CMD | "Sure. I can share that I have one deal in the pipeline..." | A17 |
| 67 | 732 | Vaibhav Chechani | Analyst | "Thank you, and all the best." | Closing acknowledgement |
| 68 | 734 | Ratan Srivastava | CMD | "Thank you." | — |
| 69 | 738 | Moderator | IR | "Thank you, sir. Thank you, everyone, for joining us today. On behalf of Finportal..." | Closing remarks begin |
| 70 | 743 | Ratan Srivastava | CMD | "Let me conclude. The first thing is that, for this year, we will maintain..." | Closing summary |
| 71 | 750 | Umang Soni | CFO | "No, that is fine. I think everything is well covered. For the guidance related to FY'28..." | `GUIDANCE_DEFERRED` — FY28 guidance explicitly deferred to March 2027 |
| 72 | 753 | Ratan Srivastava | CMD | "Thank you." | — |
| 73 | 767 | Moderator | IR | "Thank you so much, sir. I would also like to thank the participants..." | Closing |
| 74 | 777 | Ratan Srivastava | CMD | "Thank you." | Final line of transcript |

Turn distribution: Ratan Srivastava 30/74 (40.5%), Moderator 16/74 (21.6%), Apoorv Bandi 9/74 (12.2%), Umang Soni 5/74 (6.8%), Manish Gurnani 5/74 (6.8%), Vaibhav Chechani 5/74 (6.8%), Parth Sodha 4/74 (5.4%), Darpan Audichya 0/74 (0%).

Q&A-session turn share (turns 4-74, i.e. line 286 onward, 71 of 74 turns) vs opening-remarks turn share (turns 1-3, 3 of 74 turns): Q&A = 71/74 = 96% of turns by count (not by word count — this is a turn-count proxy only, word-count-weighted "% effort on Q&A" is an A4 interpretive computation, out of scope for A2).

---

## 4. Question Ledger (17 questions, separate from turn ledger per instruction #3)

| Q# | Turn | Line | Analyst / Source | Firm | Topic | Flags |
|----|------|------|-------------------|------|-------|-------|
| Q1 | 7 | 296 | Parth Sodha | NOT FOUND | Top-10 client concentration — is slowdown concentrated in a few large customers or spread across the base | — |
| Q2 | 14 | 321 | Apoorv Bandi | NOT FOUND | Are the two clients reducing headcount because they want to bring AI in-house | — |
| Q3 | 16 | 343 | Apoorv Bandi | NOT FOUND | Are the next few quarters soft only because of these two clients, or is overall demand weak | — |
| Q4 | 18 | 365 | Apoorv Bandi | NOT FOUND | Will FY27 revenue be the same as FY26 | — |
| Q5 | 22 | 376 | Apoorv Bandi | NOT FOUND | Confirm: even after losing two customers, margins will not be impacted | — |
| Q6 | 24 | 394 | Apoorv Bandi | NOT FOUND | Has AI-driven efficiency improvement been measured / is there a metric | — |
| Q7 | 28 | 445 | Moderator, on behalf of unnamed Q&A-tab submitter | NOT FOUND | Size of the international-bank AI-hosted-platform deal; one-time project or recurring platform income | `ANALYST_NOT_NAMED` |
| Q8 | 32 | 475 | Moderator, on behalf of unnamed Q&A-tab submitter | NOT FOUND | Strategy to grow product-business contribution over next 2-3 years; which product has the biggest growth potential | `ANALYST_NOT_NAMED` |
| Q9 | 34 | 502 | Moderator, on behalf of unnamed Q&A-tab submitter | NOT FOUND | Plans to diversify beyond North America into Europe, Middle East, or India | `ANALYST_NOT_NAMED` |
| Q10 | 36 | 513 | Moderator, on behalf of unnamed Q&A-tab submitter | NOT FOUND | Have there been layoffs due to AI-driven efficiency | `ANALYST_NOT_NAMED` |
| Q11 | 38 | 522 | Moderator, on behalf of unnamed Q&A-tab submitter | NOT FOUND | Average time for a new client to become a repeat customer; % of new proposals where clients ask for AI | `ANALYST_NOT_NAMED` |
| Q12 | 40 | 537 | Moderator, on behalf of unnamed Q&A-tab submitter | NOT FOUND | % of revenue that is recurring; nature of the recurring revenue | `ANALYST_NOT_NAMED` |
| Q13 | 43 | 556 | Moderator, on behalf of unnamed Q&A-tab submitter | NOT FOUND | When will AI spending move from pilot projects to large-scale deployment | `ANALYST_NOT_NAMED` |
| Q14 | 47 | 573 | Apoorv Bandi | NOT FOUND | Is AI token cost now exceeding employee cost, and is that factored into margin guidance | — |
| Q15 | 50 / 52 (restated) | 605 / 611 | Moderator, on behalf of unnamed Q&A-tab submitter | NOT FOUND | Threat from larger players chasing smaller deals amid revenue deflation and wider service breadth | `ANALYST_NOT_NAMED`; restated verbatim at line 611 after management requested a repeat (line 609) — one question, not counted twice |
| Q16 | 57 | 645 | Vaibhav Chechani | NOT FOUND | 5-year vision / long-term strategy given diversification into 6-7 verticals and 100% services focus | — |
| Q17 | 65 | 720 | Vaibhav Chechani | NOT FOUND | Any color or ballpark number on the deal pipeline | — |

No `REPEAT_QUESTION` flag applicable — no two distinct analysts asked the same question; Q15's restatement is a single question repeated verbatim by the same moderator at management's own request, not a repeat by a second analyst.

---

## 5. Quantitative Disclosures Ledger — Every Number Spoken by Management (34 items, sequential by first mention)

| # | Turn | Line | Speaker | Disclosure | Flags |
|---|------|------|---------|------------|-------|
| 1 | 2 | 136 | Ratan Srivastava | Six years as a listed company; NSE debut 6 July 2020 | — |
| 2 | 2 | 154-155 | Ratan Srivastava | Consolidated revenue Q1FY27 = Rs. 41.4 crore; +10% YoY; -3.7% QoQ | — |
| 3 | 2 | 168-169 | Ratan Srivastava | Full impact of engagement ramp-downs expected over "next two to three quarters" | Forward-looking / hedge |
| 4 | 2 | 175-176 | Ratan Srivastava | EBITDA Q1FY27 = Rs. 12.56 crore; +26.2% YoY; broadly flat QoQ; EBITDA margin +389 bps YoY | — |
| 5 | 2 | 177-179 | Ratan Srivastava | PAT Q1FY27 = Rs. 9.21 crore; +43.3% YoY; -5% QoQ; PAT margin 22.2% vs 17.1% Q1FY26; EPS Rs. 3.88 vs Rs. 2.71, +43% YoY | — |
| 6 | 2 | 181-183 | Ratan Srivastava | Company declines to reaffirm FY27 revenue guidance at this stage | `GUIDANCE_WITHDRAWN` |
| 7 | 2 | 192 | Ratan Srivastava | EBITDA margin target reiterated at 25%-30% range, full year and QoQ basis | — |
| 8 | 3 | 234 | Umang Soni | Revenue Rs. 41.4 crore, +10% YoY, -3.7% QoQ (repeats item 2) | Duplicate of #2 — corroborating restatement |
| 9 | 3 | 239-240 | Umang Soni | EBITDA Rs. 12.56 crore, +26.2% YoY, flat QoQ; EBITDA margin 30.3% vs 29.3% prior quarter vs 26.4% Q1FY26 | — |
| 10 | 3 | 248-250 | Umang Soni | PAT Rs. 9.21 crore, +43.3% YoY, PAT margin 22.2% vs 17.1%, -5% QoQ (repeats item 5) | Duplicate of #5 |
| 11 | 3 | 253-254 | Umang Soni | IT services = 98.3% of revenue; overseas revenue = 82% of total | — |
| 12 | 3 | 257-259 | Umang Soni | Geography mix: North America 63%, India 18%, Europe 6%, Australia 3%, RoW 10% | — |
| 13 | 3 | 262-263 | Umang Soni | Cash and bank balance Rs. 17 crore as of 30 June 2026; company debt-free | — |
| 14 | 3 | 265-266 | Umang Soni | Interim dividend of Rs. 4 per share declared for FY27 | — |
| 15 | 9 | 303-309 | Ratan Srivastava | Top-10 clients: 2 of 10 have suddenly reduced business; relationship duration approximately 3 years | — |
| 16 | 17 | 347-349 | Ratan Srivastava | ~24 calls attended in six years listed; historically "5 large customers, 10 large customers" contributed 40%-50% of revenue | — |
| 17 | 26 | 408-410 | Manish Gurnani | Developer efficiency gain approximately 25% (work of 4 people now done by ~2); for senior developers, up to 3x (1 person doing >2 people's work) | — |
| 18 | 30 | 462-463 | Manish Gurnani | Bank AI platform: "more than 50 use cases" identified | — |
| 19 | 29/31 | 449-467 | Ratan Srivastava / Manish Gurnani | Bank deal size explicitly not disclosed ("Till now, I cannot disclose the number") | `NOT_DISCLOSED` |
| 20 | 31 | 469 | Ratan Srivastava | Bank AI project framed as "a year-long project" | — |
| 21 | 42 | 551-553 | Umang Soni | ">80%" of revenue from repeat/existing customers | — |
| 22 | 45 | 563-564 | Manish Gurnani | Fortune 500 telecom-giant relationship duration: "almost two and a half years" | — |
| 23 | 54 | 621-622 | Manish Gurnani | Ksolves-scale deals deploy ~4 resources; large competitors deploy "50 to 60 people per project, minimum" | — |
| 24 | 61 | 694-698 | Ratan Srivastava | Historical target: 18%-20% YoY revenue growth; this year (FY27) growth expected soft, not this target; target resumes at "20% minimum" from FY28; margin target 30% reiterated | — |
| 25 | 64 | 715-717 | Ratan Srivastava | Restates 18%-20% growth plan for the year was not achieved due to two client losses | Duplicate of #24, restated |
| 26 | 66 | 724-726 | Ratan Srivastava | Deal pipeline: one deal sized $300K, another sized $250K; total pipeline "approximately 1 million US dollars" | USD figure per extraction header note (not converted to INR); non-standard reporting unit |
| 27 | 66 | 727-728 | Ratan Srivastava | Even if all pipeline deals close, completion will take "at least two quarters" | Forward-looking |
| 28 | 70 | 744-745 | Ratan Srivastava | If conditions improve, FY27 revenue could rise "4% to 5% year on year, maximum" | Forward-looking / hedge ("if things go well") |
| 29 | 70 | 746-747 | Ratan Srivastava | Margin band reiterated 25%-30%, with potential upside above 30% | Duplicate of #7/#24, restated |
| 30 | 71 | 750-751 | Umang Soni | FY28 guidance explicitly deferred: "we will revisit it again in March 2027" | `GUIDANCE_DEFERRED` |
| 31 | 62 | 408 (context) / 401-403 | Manish Gurnani | AI-certification initiative underway "for more than a year" prior to this quarter | — |
| 32 | 2 | 254-259 (context) | Umang Soni | (see #11-12; separately flagged that 98.3% + non-IT-services residual ≈ 1.7% of revenue is implied but not itself named — a template/derived-not-stated figure) | Derived, not directly spoken — flagged for A3/A4 review, not itself a disclosure |
| 33 | 17 | 348 | Ratan Srivastava | Historically cited customer concentration: "40%, 50% of the revenue" from top 5/10 customers (restated context of #16) | Duplicate of #16 |
| 34 | 3 (Umang) | 234-235 | Umang Soni | Cross-reference to "earnings presentation and the press release" as containing further detail not verbally repeated on the call | `EXTERNAL_DOC_REFERENCED` — content of presentation/press release out of scope for this transcript-only extract; A3/A4 should reconcile against those documents separately if in the same run |

Note on item #32: this is a derived arithmetic implication (100% - 98.3% = 1.7% non-IT-services revenue), not a number spoken verbatim by management. Flagged here for completeness-ledger transparency per "enumerate everything, interpret nothing," but it is NOT counted toward the sweep total of spoken numbers in the strict sense — retained as a review flag only, not a management disclosure. Sweep count of 34 above includes it as a listed row; treat items #8, #10, #25, #29, #33 as duplicate/restated rows of an earlier primary disclosure (5 duplicates), so the count of distinct (non-duplicate) quantitative disclosures is 34 - 5 = 29 distinct figures across 34 total spoken/derived instances logged.

---

## 6. Forward-Commitment and Hedge Phrase Ledger (turn-cited, no A3 lexicon available this run — logged verbatim for A3 to classify)

| # | Turn | Line | Speaker | Phrase (verbatim or near-verbatim) | Type |
|---|------|------|---------|-------------------------------------|------|
| 1 | 2 | 181-183 | Ratan Srivastava | "it would not be prudent for us to reaffirm the revenue guidance for the current financial year at this stage" | Hedge / guidance withdrawal |
| 2 | 2 | 192 | Ratan Srivastava | "We continue to target EBITDA margin... in the 25% to 30% range" | Forward commitment |
| 3 | 17 | 355-359 | Ratan Srivastava | "I would like to be conservative. I do not want to give any false hope." | Hedge |
| 4 | 17 | 371-374 | Ratan Srivastava | "Margins, however, will definitely improve. They will always be between 25% to 30%" | Forward commitment |
| 5 | 30 | 466-467 | Manish Gurnani | "This is still in discussion, but the goal is that this will be almost a year-long project." | Hedge + forward commitment (paired) |
| 6 | 58/63 | 663-668 | Ratan Srivastava | "it is a very tough question for me to say what we will be after the next five years... Right now, we do not have any plan" | Hedge |
| 7 | 62 | 694-699 | Ratan Srivastava | "we would again like to maintain 20% minimum growth, with a 30% margin... let us see how it goes" | Forward commitment + hedge (paired) |
| 8 | 66 | 726 | Ratan Srivastava | "if all those things get confirmed, I can say that I have enough amount of work" | Hedge |
| 9 | 70 | 744-745 | Ratan Srivastava | "if things go well, we may increase revenue by 4% to 5% year on year, maximum" | Hedge |
| 10 | 71 | 750-751 | Umang Soni | "For the guidance related to FY'28, we will revisit it again in March 2027" | Guidance deferral (forward commitment to a future decision date) |

---

## Flags Summary (all flags raised across this ledger)

- `SILENT_PANELIST` — Darpan Audichya listed on management panel, zero speaker turns (1 instance)
- `FIRM_NOT_DISCLOSED` — all 3 named analysts, no firm affiliation stated (3 instances)
- `ANALYST_NOT_NAMED` — 8 questions read from Q&A tab with no submitter name (Q7-Q13, Q15; 8 instances, one question so counted once at Q15 despite the line-611 restatement)
- `NOT_DISCLOSED` — bank AI deal size explicitly declined (1 instance)
- `GUIDANCE_WITHDRAWN` — FY27 revenue guidance not reaffirmed (1 instance)
- `GUIDANCE_DEFERRED` — FY28 guidance deferred to March 2027 (1 instance)
- `EXTERNAL_DOC_REFERENCED` — earnings presentation / press release referenced but not reconciled within this transcript-only extract (1 instance)

No `ENTITY_CHANGE`, `ZERO_STANDING` (no financial-table line items in a concall transcript — that flag family applies to the results-filing doctype, not applicable here), `MGMT_ABSENCE`, or `REPEAT_QUESTION` (in the cross-analyst sense) found in this document.
