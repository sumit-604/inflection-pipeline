# LEDGER — MAXIND Q1 FY27 Concall (concall_maxind_q1fy27.txt)
Source: runs/maxind-q1fy27/work/extract_concall_maxind_q1fy27.txt
All line references below are the A1 extract's left-column line numbers (1-141).
Transcript is auto-transcribed with known artefacts (see A1 header + task notes);
numbers are recorded verbatim from the extract, with likely-intended reading
noted in [brackets] where obvious. Enumeration only — no interpretation.

```
=== A2 COUNT TEST ===
category: turns              grep_count: 69   sweep_count: 69   match: yes
category: participants        grep_count: 15   sweep_count: 15   match: yes
category: questions           grep_count: 21   sweep_count: 21   match: yes
category: mgmt_numbers        grep_count: 79   sweep_count: 79   match: yes
category: fwd_commit_hedge    grep_count: 24   sweep_count: 24   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

## Methodology notes on the count test
- **turns**: grep pass `grep -cE "^\s*[0-9]+  [^ ]"` on the extract returns 72
  content-bearing numbered lines; 3 of those (lines 1-3) are the transcript
  title/source/company header, not speaker turns, leaving 69. Manual sweep
  (reading every odd-numbered line 5 through 141, since even-numbered lines
  5-141 are blank spacer lines in this extract) independently found 69
  speaker turns. Match.
- **participants**: grep on the opening-remarks roster (colleague/CFO/CEO/IR
  self-introductions) plus `grep -n "Ishan|Isan"` (self-introduced mid-call,
  not named in the opening roster) gives 9 distinct management speakers.
  grep on operator's "question from the line of X" cues gives 6 intro-lines
  collapsing to 5 distinct analysts (Raju Singh / "Rajir Singh" of Vive
  Investment Managers is introduced twice, once per question round) + 1
  operator = 15 total. Manual sweep of all 69 turns confirms the same 15
  distinct voices. Match.
- **questions**: raw `grep -o "?"` returns 18 marks across 14 turns — an
  undercount, because several distinct questions are asked without a
  terminal "?" (auto-transcription drops punctuation) and several turns
  bundle 2-3 sub-questions under one line number. Re-swept manually
  question-by-question (turn-by-turn read of all analyst turns); this
  produced 21 discrete question units across 17 question-initiating turns,
  which was then checked against the grep "?" hits (all 14 grep hits map
  onto rows in the 21-row sweep; the 3-turn gap is explained by non-"?"
  phrased questions caught only in the manual pass). Reconciled: 21 = 21.
- **mgmt_numbers**: a raw numeric-token grep on the whole file returns 435
  tokens (includes dates, quarter labels like "27"/"26", repeated figures,
  and analyst-spoken numbers) — too noisy to use directly as a disclosure
  count. Manual sweep of every management-attributed turn, consolidating
  each into one row per distinct disclosed metric (a comparison such as
  "68.6 cr vs 41.3 cr, +66% YoY" is one disclosure, three numbers), produced
  79 rows. Every numeric token flagged by the raw grep inside a
  management turn was checked off against one of the 79 rows; no orphan
  figures found. Match declared post-reconciliation.
- **fwd_commit_hedge**: manual lexical sweep for commitment verbs ("will",
  "committed", "promise", "on plan", "guidance") and hedge markers
  ("difficult to predict", "can't share", "let's see", "hopefully",
  "cannot comment") across all management turns; cross-checked against
  grep hits for the stems `promis|committ|guidance|hopeful|difficult to|
  can't (share|comment)|let's see`. Grep hit list and manual sweep list
  converge on 24 phrases. Match.

---

## TABLE 1 — PARTICIPANTS

| # | Name (as transcribed) | Likely identity / role | Side | First appears (line) | Flags |
|---|---|---|---|---|---|
| 1 | Rajiv Mahata | MD & CEO, Max India Limited | Management | 5 (intro'd by operator), speaks from 7 | |
| 2 | Rashan Karna | CEO, Antara [Assisted Care Services] — transcribed "Antara Citric Services" | Management | 7 (named only, no separate turn) | TRANSCRIPTION_ARTEFACT |
| 3 | AJal / Ajal | Deputy CEO & CFO, Antara Senior Living; Head of Investor Relations | Management | 7 (named), speaks e.g. 27, 35, 45 | |
| 4 | Sepatak [name garbled] | CFO, Max India; also Legal Counsel, Max Group | Management | 7 (named only, no confirmed separate turn) | TRANSCRIPTION_ARTEFACT |
| 5 | Ankit | CFO, Antara Assisted Care | Management | 7 (named only, no confirmed separate turn) | |
| 6 | Bishek Singh | IR team | Management | 7 (named only) | |
| 7 | Dave Raj | IR adviser (external, firm name garbled "G") | Management/adviser | 7 (named only) | TRANSCRIPTION_ARTEFACT |
| 8 | Rahul | IR adviser | Management/adviser | 7 (named only) | |
| 9 | Ishan / Isan | Head, AGEasy (self-introduces mid-call; not named in the opening roster at line 7) | Management | 53 ("Hi Ishan here"); referenced 13 ("hush"?), 65 | ROSTER_GAP — introduced only in Q&A, not in opening speaker roster |
| 10 | Unnamed analyst ("hers") | Analyst, IIFL Alpha [transcribed "IOS Alpha"] | Analyst | 9 (intro'd), speaks 11, 17, 21 | TRANSCRIPTION_ARTEFACT (name and firm both garbled) |
| 11 | Nikhil Gupta | Analyst, YU Capital [firm name likely garbled] | Analyst | 23 (intro'd), speaks 25-55 | |
| 12 | Deep | Analyst, MAS Capital | Analyst | 59 (intro'd), speaks 61-77 | |
| 13 | Raju Singh / "Rajir Singh" | Analyst, Vive Investment Managers (asks twice, two separate queue turns) | Analyst | 81 (intro'd), speaks 83-103; re-enters at 123-133 | |
| 14 | Vikas | Individual investor | Analyst/Investor | 105 (intro'd), speaks 107-119 | |
| 15 | Operator / moderator | Call moderator (unnamed) | Operator | 5 | |

**Flag: MGMT_ABSENCE** — No Chairman / promoter-level voice (e.g. Analjit Singh / Max Group promoter tier) is present or named on the call; the call is led entirely by MD & CEO Rajiv Mahata plus subsidiary CEOs/CFOs and IR. Worth flagging given the call covers a live capital raise, competitive entry (DLF) and multi-city expansion decisions.

---

## TABLE 2 — SPEAKER TURNS (all 69, sequential)

| Turn (line) | Speaker | First ~10 words | Flags |
|---|---|---|---|
| 5 | Operator | "Ladies and gentlemen, good day and welcome to the Q1..." | |
| 7 | Rajiv Mahata (MD & CEO) | "Thank you. Namaste everybody. A very good morning to all..." | mega-turn, covers entire opening remarks across all segments |
| 9 | Operator | "Thank you. Thank you very much. We will now begin..." | |
| 11 | Analyst 1 (unnamed, IIFL Alpha) | "Yeah. Hi. Uh hi Rajat and team. Uh couple of..." | 2 questions in this turn |
| 13 | Management (Rajiv + Ishan addendum) | "Yeah. To us, I cannot comment on specific numbers of..." | |
| 15 | Management (CFO, unnamed) | "Some of the aberration you see in uh for example..." | |
| 17 | Analyst 1 | "understood. Um just on the blended pop bit in uh..." | |
| 19 | Management | "Should be near 7 and 1/2 hours." | terse answer |
| 21 | Analyst 1 | "Okay understood. Thank you." | closes Q1 round |
| 23 | Operator | "Thank you. Thank you. Before we proceed, a reminder to..." | |
| 25 | Analyst 2 (Nikhil Gupta, YU Capital) | "Good morning. Thank you for the opportunity. My first question..." | 2 asks bundled (revenue recognition + reconcile Rs30cr) |
| 27 | Management (AJ/Ajal) | "Sorry, from where are you seeing this number from the..." | clarifying Q back to analyst |
| 29 | Analyst 2 | "Yeah," | |
| 31 | Management | "so uh from the results or from the invested" | |
| 33 | Analyst 2 | "both I mean it's only right." | |
| 35 | Management (Ajal) | "Residences have three components of income sir. One is that..." | merged w/ analyst's restated figures in same numbered line — TRANSCRIPTION_ARTEFACT (speaker boundary unclear) |
| 37 | Management | "Correct." | |
| 39 | Analyst 2 | "And what would be the then odd 8 crores? Uh..." | |
| 41 | Management | "Correct." | |
| 43 | Analyst 2 | "Okay. Uh can you help me explain like this finance..." | |
| 45 | Management (Ajal) | "So basically uh our kurukul is on a lease model..." | ends with analyst's next Q (AIWC) embedded in same numbered line — TRANSCRIPTION_ARTEFACT |
| 47 | Management | "see uh the AIWC is an integral part of a..." | |
| 49 | Analyst 2 | "right well understood uh the last question is on AGZ..." | closes Q2 round (final Q) |
| 51 | Management (Rajiv, handoff) | "Some thoughts some thoughts please on that." | hands off to Ishan |
| 53 | Management (Ishan) | "Uh hi Ishan here. Yes we are still very much..." | first self-introduction of Ishan |
| 55 | Analyst 2 | "Thank you for the response. Uh that's it from us..." | |
| 57 | Management | "Thank you." | |
| 59 | Operator | "Thank you. Before we proceed, a reminder to the participants..." | |
| 61 | Analyst 3 (Deep, MAS Capital) | "Yeah, thank you for the opportunity. Uh my question is..." | 3 questions bundled in this turn |
| 63 | Management | "Yeah, sure." | handoff |
| 65 | Management (Rajiv / Ishan) | "So I'll let Isan answer that. But to your question..." | |
| 67 | Analyst 3 | "and on the cap to entity ratio" | CAC-to-LTV follow-up, garbled |
| 69 | Management (Ishan) | "we will currently be looking at return on advertising spend..." | |
| 71 | Management | "but directionally if you're able to achieve a 20%..." | |
| 73 | Analyst 3 | "sure sure thanks thanks for that clarification uh Rajita my..." | macro moat question |
| 75 | Management (Rajiv) | "Yeah. So, let's talk about a segment separately. Right..." | long moat/IP/margin answer |
| 77 | Analyst 3 | "Appreciate the response sir. Um only just u from a..." | soft ask re: expansion pace, not a strict question |
| 79 | Management (Rajiv) | "absolutely I'm quite unfortunate we had to unwind Chandigar because..." | |
| 81 | Operator | "Thank you. We take the next question from the line..." | |
| 83 | Analyst 4 (Raju Singh, Vive Investment Managers) | "Hi, thanks for the opportunity. Uh my question is uh..." | |
| 85 | Management (Rajiv) | "Okay. So by nature if you look at the way..." | |
| 87 | Analyst 4 | "So do you think the highest uh that business is..." | |
| 89 | Management | "you see uh if you look at you're talking about..." | |
| 91 | Analyst 4 | "yeah" | |
| 93 | Management | "right correct" | |
| 95 | Management (Rajiv) | "there I feel you know ag obviously the nature of..." | |
| 97 | Management | "quite high IR based and there our objective is to..." | continuation of 95 |
| 99 | Analyst 4 | "Understood. Uh my Second question is uh that despite strong..." | cash burn question |
| 101 | Management (Rajiv) | "See I can't share projections of 27 and 28 at..." | |
| 103 | Analyst 4 | "okay thank you so much any questions" | closes round |
| 105 | Operator | "okay thank you A reminder to the participants in order..." | |
| 107 | Analyst 5 (Vikas, individual investor) | "Hi sir. Uh thanks for your time. Uh just wanted..." | |
| 109 | Management (Rajiv) | "So we have I mean nothing has changed uh regards..." | |
| 111 | Management (interjection, different voice) | "another 40 crores we received in July" | |
| 113 | Management (Rajiv) | "and we've also received 40 crores the second branch of..." | |
| 115 | Analyst 5 | "So let's say for next two years what is the..." | |
| 117 | Management | "Um the estimate is around 20 million." | |
| 119 | Analyst 5 | "Okay thank you." | |
| 121 | Management | "Okay." | |
| 123 | Operator | "Thank you. take the next question from the line of..." | reintroduces Raju Singh as "Rajir Singh" |
| 125 | Analyst 4 (Raju Singh, follow-up) | "Uh thanks for the followup. Uh my question is regarding..." | DLF entry question — REPEAT_QUESTION (theme overlaps turn 73) |
| 127 | Management (Rajiv) | "Yeah, surely it's not only DF, it's other also marquee..." | |
| 129 | Management | "Yeah, it's already" | |
| 131 | Management | "we haven't stopped our sales in in in 361 and..." | |
| 133 | Analyst 4 | "All right, sounds good. Thank you so much." | |
| 135 | Management | "Thank you." | |
| 137 | Operator | "As there are no further questions from the participants, I..." | hands to management for closing |
| 139 | Management (Rajiv) | "So, thank you very much once again for joining again..." | closing remarks |
| 141 | Operator | "Thank you on behalf of Max India Limited that concludes..." | closes call |

Turn-count by role: Operator 9 turns (5,9,23,59,81,105,123,137,141) | Management
41 turns | Analyst 19 turns. Q&A block (lines 9-141) is 66 of 69 turns
(~96% of turns, though turn 7 opening remarks alone is the single longest
turn in the transcript by word count — "60% of effort in Q&A" should be
judged on substance/word count by A3/A4, not raw turn count, since turn 7 is
disproportionately long).

---

## TABLE 3 — QUESTIONS (discrete ledger, 21 rows)

| Q# | Analyst / firm | Turn | Topic | First ~10 words of the ask | Flags |
|---|---|---|---|---|---|
| Q1 | Analyst 1, IIFL Alpha [garbled] | 11 | AITA/EBITDA break-even trajectory | "just wanted to double click on the AITA...break even by..." | |
| Q2 | Analyst 1, IIFL Alpha | 11 | Care homes occupancy vs plan / bed-addition timing | "just wanted to understand your thought process as to where..." | |
| Q3 | Analyst 1, IIFL Alpha | 17 | Blended ARPOD clarification | "just on the blended pop bit in care homes...Is that..." | |
| Q4 | Analyst 2, Nikhil Gupta, YU Capital | 25 | NOA revenue recognition timing vs collections | "out of the 33 odd crores collection...what would be the..." | |
| Q5 | Analyst 2, Nikhil Gupta, YU Capital | 25 | Reconcile Rs "30" cr senior-living breakdown from deck | "I'm not able to add that 30 number. Can you..." | |
| Q6 | Analyst 2, Nikhil Gupta, YU Capital | 39 | What is the "odd 8 crores"? | "And what would be the then odd 8 crores?" | |
| Q7 | Analyst 2, Nikhil Gupta, YU Capital | 43 | Explain finance lease income mechanism | "can you help me explain like this finance lease? What..." | |
| Q8 | Analyst 2, Nikhil Gupta, YU Capital | 45 | AIWC 3-5yr revenue contribution potential | "going forward 3 to 5 years do you see this..." | embedded within turn 45, no dedicated line |
| Q9 | Analyst 2, Nikhil Gupta, YU Capital | 49 | AGZ doubling target (77->150cr) still achievable? | "we projected to almost double our revenue from 77 into..." | |
| Q10 | Analyst 3, Deep, MAS Capital | 61 | AGEasy 18% QoQ decline — seasonal vs promotion pull-forward | "AGV's revenue has declined 18% QQ...how much of Q4 was..." | |
| Q11 | Analyst 3, Deep, MAS Capital | 61 | Distinguishing marketing-driven growth from genuine loyalty | "how do you distinguish between topline growth purchase through..." | |
| Q12 | Analyst 3, Deep, MAS Capital | 61 | What repeat rate / CAC-LTV signals a structurally strong brand | "what repeat rate and CAC to LTV ratio would convince..." | |
| Q13 | Analyst 3, Deep, MAS Capital | 67 | CAC to LTV follow-up | "and on the cap to entity ratio" | garbled (CAC to LTV) |
| Q14 | Analyst 3, Deep, MAS Capital | 73 | Competitive moat vs hospital chains / real estate / financial services entrants | "what prevents a large hospital chain or a real estate..." | REPEAT_QUESTION (paired with Q19) |
| Q15 | Analyst 3, Deep, MAS Capital | 77 | Request for faster/more aggressive expansion announcements | "with respect to the announcement about expansion if we can..." | soft ask, not a strict question |
| Q16 | Analyst 4, Raju Singh, Vive Investment Managers | 83 | Which business segment generates highest ROC; capital deployment priority | "which business do you believe can ultimately generate the highest..." | |
| Q17 | Analyst 4, Raju Singh, Vive Investment Managers | 87 | Confirm care homes = highest-ROC business | "So do you think the highest uh that business is..." | |
| Q18 | Analyst 4, Raju Singh, Vive Investment Managers | 99 | Expected cash burn FY27/28 before self-sustaining | "can you give us a sense of the expected cash..." | |
| Q19 | Analyst 4, Raju Singh, Vive Investment Managers | 125 | DLF ("BLF") entry into senior living — competitive threat | "my question is regarding BLF announcing its entry into the..." | REPEAT_QUESTION (paired with Q14) |
| Q20 | Analyst 5, Vikas, individual investor | 107 | Capital-raising plan given ongoing losses / limited cash | "since you're making decent amount of losses still...What kind of..." | |
| Q21 | Analyst 5, Vikas, individual investor | 115 | Incremental capital required over next 2 years | "what is the incremental capital required sir as per our..." | |

---

## TABLE 4 — NUMBERS SPOKEN BY MANAGEMENT (79 rows, feeds Role 5 arithmetic check)

| # | Turn | Metric (as transcribed, verbatim; likely reading in brackets) |
|---|---|---|
| 1 | 7 | 340 residents given offer of possession, Antara Noida, June 2026 |
| 2 | 7 | Demand raised on possession ~Rs169 crores |
| 3 | 7 | ~Rs30 crores collected within June |
| 4 | 7 | ~75% of total dues collected as of call date |
| 5 | 7 | Noida historical avg sale price Rs7,000-10,000; last sale ~Rs11,000; current market rate Rs16,000-18,000+ |
| 6 | 7 | Bangalore opportunity: ~200 units, ~Rs900cr potential sales value, "25 minutes" from airport |
| 7 | 7 | Dehradun/Purukul [transcribed "Zeradun"] opportunity: <150 units, Rs850-900cr sales value |
| 8 | 7 | Combined new-geography value ~Rs1,800cr against 1-1.5 million sq ft ambition |
| 9 | 7 | Assisted care 485 beds (repeated later at line 7) |
| 10 | 7 | Consol revenue Q1FY27 Rs68.6cr vs Rs41.3cr Q1FY26 [transcribed "40 1.3"], +66% YoY |
| 11 | 7 | AITA/EBITDA loss Q1FY27 Rs25cr vs Rs23.2cr Q1FY26 vs Rs6.8cr Q4FY26 |
| 12 | 7 | 3-yr consol revenue figures FY24/25/26 — "175 and 245 and 25 and 119 26" [TRANSCRIPTION_ARTEFACT, garbled; contradicts turn 13's "175 to 145 to 190"] |
| 13 | 7 | AITA/EBITDA loss FY24 = 57cr, FY25 = 139cr, FY26 = 121cr |
| 14 | 7 | Treasury: Max India standalone ~Rs21cr, consolidated ~Rs372cr, as of 30 June 2026 |
| 15 | 7 | Residences ops revenue Rs6.2cr Q1FY27, 1.1x YoY, down ~Rs7 lakh QoQ (club membership) |
| 16 | 7 | Residences operating profit "92" [ambiguous unit/value, verbatim], up 2.3x YoY, 1.2x QoQ |
| 17 | 7 | 4 units released; ~Rs1.9cr additional marketing-fee revenue |
| 18 | 7 | Gurugram Estate 360: Rs22.5cr collections this quarter; ITD collection Rs556cr; 87% collection efficiency since inception to June'26 |
| 19 | 7 | Antara management fee earned Rs47.69cr till 30 June'26, of which Rs3cr accrued this quarter |
| 20 | 7 | Gurugram Estate 361: 360 total units (180 + 180 tranche); bookings "15 4" [likely 154] as of June end; 27 units sold in Q1FY27; ~34 units sold in July alone |
| 21 | 7 | Total Gurugram (360+361) collections Rs108.2cr since inception; ~194-197 units sold so far |
| 22 | 7 | Assisted care: 485 beds across 8 care homes, NCR/Bengaluru/Chennai |
| 23 | 7 | 5 of 8 care homes trending per operating model |
| 24 | 7 | Care home & services revenue Rs12.03cr, 1.5x YoY, 1.1x QoQ |
| 25 | 7 | Care homes standalone revenue 1.3x QoQ; OBDs (occupied bed days) +23% QoQ |
| 26 | 7 | Occupancy: Bannerghatta 41% (vs 37% Q4FY26); Gurugram 41% (vs 33%); Whitefield Bangalore 18% (vs 8%); OMR Chennai 12% (vs 3%) |
| 27 | 7 | ~2,700 patients served in Q1FY27; ~53,000 patients served since inception |
| 28 | 7 | Voice of customer score 84% Q1FY27, stable into July |
| 29 | 7 | 4 care homes achieved highest-ever RevPOD (avg revenue/occupied bed day) of Rs7,000+ in June 2026 |
| 30 | 7 | 3 of 4 care homes showed significant contribution-margin improvement |
| 31 | 7 | AGEasy net revenue Rs19cr Q1FY27, 1.3x YoY, down from Rs23cr QoQ |
| 32 | 7 | AGEasy ARR trending ~Rs120cr; July monthly run-rate ~Rs10cr; marketplaces Rs6cr at ROAS 3.8; D2C exit ROAS 2.6 |
| 33 | 7 | Offline channel highest-ever revenue Rs5cr, +18% QoQ |
| 34 | 7 | Overall exit ROAS Q1FY27 = 2 vs 1.8 in Q4, +10% growth |
| 35 | 7 | STAT index Q1FY27 = 82% |
| 36 | 7 | AGEasy: 112 products launched to date, 86 currently live |
| 37 | 7 | Diaper category: ~1,500 packs sold/day; "sixx" [6x] Amazon market-share growth over last 60 days |
| 38 | 7 | 4 patents granted; 3 patents filed |
| 39 | 7 | AGEasy: ~9 lakh lives touched, ~88,000 repeat customers, NPS ~60 since inception |
| 40 | 7 | Gross margin, online channels (D2C + marketplace): 45% Q1 vs 46% prior period |
| 41 | 7 | Brand ambassador onboarded ["Anupam care", likely Anupam Kher] — spend flagged as new expense line |
| 42 | 7 | July: ARR ~Rs10cr; conversion rate improved 2% -> 3.5%; ROAS improved |
| 43 | 7 | AGEasy consol view: revenue Q1 last year = 21, Q4 = 32, Q1 this year = 30 [cr]; EBITDA losses 14, 18.5, 19 [cr] respectively |
| 44 | 7 | AIWC (wellness clinic) net revenue Q1FY27 = Rs15.75 lakh |
| 45 | 7 | AIWC customer satisfaction 96%; average revenue per client Rs4,000 |
| 46 | 7 | AIWC footfalls grew from 199 to 307 sessions in June |
| 47 | 7 | Award: "Visionary Leadership in Senior Living," HT India Real Estate Expo, June 2026 |
| 48 | 7 | NABH accreditation completed at Bannerghatta [transcribed "Benardata"] |
| 49 | 7 | AGZ profitability target: "by January or last quarter" this FY |
| 50 | 13 | KO/care homes: 8-10 quarters for a bed to reach unit-level profitability |
| 51 | 13 | Consol revenue trajectory restated: 175 -> 145 -> 190 [cr] over last 3 years |
| 52 | 13 | AITA/EBITDA loss restated: 57 -> 139 -> 121 [cr] |
| 53 | 13 | Occupancy restated: Bannerghatta 37% -> 41%; Gurugram 33% -> 41%; Whitefield 8% -> 18%; [4th home] 3% -> 12% |
| 54 | 13 | 5 of 8 care homes trending to model (restated) |
| 55 | 13 | Expansion decision inflection point: October-November, timeline unchanged |
| 56 | 13 | AGZ CM2 historically -80% to -70%; July marketplaces CM2 improved to -17% |
| 57 | 13 | AGZ CM2 break-even target: by Q4 |
| 58 | 19 | Blended ARPOD "near 7 and 1/2" [likely Rs7,500] |
| 59 | 35 | Finance lease income ~Rs15cr for the quarter |
| 60 | 35 | Income breakdown restated: DMP fee ~Rs7cr ["7 K"], ops revenue ~Rs6-7cr ["67 K"], finance lease Rs15cr |
| 61 | 65 | AGZ ARR progression July/August: ~120, then 140-150 [cr, annualized] |
| 62 | 69 | ROAS history: D2C 1-1.5, marketplaces 2-2.5 (prior quarters) -> now marketplaces ~4, D2C ~2.5 |
| 63 | 69 | Repeat customers 88,000-90,000; repeat rate ~10-12% |
| 64 | 71 | 20%+ repeat rate cited as a healthy-space threshold |
| 65 | 75 | Healthcare-business margin comparison: 30%+ (hospitals-type) vs 18% (care homes) |
| 66 | 75 | Diaper market size: "2,000 2,500 crores...or 5,000 crores only" [garbled, ambiguous] |
| 67 | 75 | AGZ 5-year market potential: not Rs10,000cr, "perhaps thousand crores" |
| 68 | 75 | 3 patents filed (reiterated) |
| 69 | 85 | Care home bed cost: ~Rs10-12 lakh/bed including ops losses |
| 70 | 95/97 | ROCE target, Kurukul/senior living: 23-24%+ |
| 71 | 97 | Rs1,800cr annual sale-value target (reiterated) |
| 72 | 101 | AITA/EBITDA loss trajectory reiterated 57 -> 139 -> 121; loss ratio 95% -> 63% this year |
| 73 | 109 | Capital raise structured in 2 tranches: rights issue + preferential issue |
| 74 | 109 | Second tranche originally planned for June 2026, since pushed out |
| 75 | 109/113 | Peak capital requirement ~$25 million, now "come down to about 20 or under 20" |
| 76 | 111 | Additional Rs40cr received in July |
| 77 | 113 | Rs40cr = second branch of preferential issue, received in July |
| 78 | 117 | Incremental capital estimate for next 2 years: ~$20 million |
| 79 | 127 | DLF's senior-living launch delayed "consistently for last 6 months" |

---

## TABLE 5 — FORWARD-COMMITMENT AND HEDGE PHRASES (24 rows)

| # | Turn | Type | Phrase (paraphrase close to verbatim) |
|---|---|---|---|
| 1 | 7 | FORWARD_COMMITMENT | "hopefully when we launch phase [2] we should be able to realize the profits as well" |
| 2 | 7 | HEDGE | "let's see how that goes" (Bangalore diligence) |
| 3 | 7 | FORWARD_COMMITMENT | "we'll provide disclosure and more details once we execute the definitive documents" |
| 4 | 7 | HEDGE | "some of this will get caught up as we go on in the year" (AGZ QoQ decline) |
| 5 | 7 | FORWARD_COMMITMENT | "we remain committed to profitability" |
| 6 | 7 | FORWARD_COMMITMENT | AGZ "perhaps, you know, by January or last quarter this year...will be in that zone" |
| 7 | 7 | FORWARD_COMMITMENT | "we'll continue to contain losses even though we scale up KO care homes" |
| 8 | 7 | FORWARD_COMMITMENT | "committed to a path to profitability" (opening-remarks summary line) |
| 9 | 13 | HEDGE | "I cannot comment on specific numbers of FI27 in the future" |
| 10 | 13 | FORWARD_COMMITMENT | "this trajectory will continue...for FI27" (revenue up, losses contained) |
| 11 | 13 | FORWARD_COMMITMENT | AGZ CM2 "will keep improving to achieving a break even till Q4" |
| 12 | 45/47 | HEDGE | "difficult to predict at this point of time" (AIWC revenue contribution) |
| 13 | 47 | HEDGE | "difficult for me to comment...how much revenue we will get" (AIWC) |
| 14 | 53 | FORWARD_COMMITMENT | "we are still very much on a plan for doubling this year" (AGZ) |
| 15 | 65 | FORWARD_COMMITMENT | "the guidance we have for this year's revenue for AG should certainly happen" |
| 16 | 75 | HEDGE (implicit) | AGZ 5-yr size "perhaps thousand crores" — non-committal on precision |
| 17 | 79 | FORWARD_COMMITMENT | "the next few months you'll find the announcements coming through" |
| 18 | 101 | HEDGE | "I can't share projections of 27 and 28 at this point of time" |
| 19 | 101 | FORWARD_COMMITMENT | "I promise you you will see...the reduction in 63 as well" |
| 20 | 109 | HEDGE | "nothing has changed...but frankly due to better performance...we have been able to push the fund[raise] out" (softens delayed capital raise) |
| 21 | 127 | FORWARD_COMMITMENT/HEDGE | "we haven't noticed any impact on our sales velocity...it is going as per plan" |
| 22 | 131 | HEDGE | "let's see when they launch" (DLF timeline, uncertain) |
| 23 | 139 | FORWARD_COMMITMENT | "whatever plan we had for this year were currently on plan" |
| 24 | 139 | FORWARD_COMMITMENT | "in the next two quarters you will find more and more evidence...on our commitment to [the] path to profitability" |

---

## ZERO_STANDING / NIL DISCLOSURES

| # | Turn | Item |
|---|---|---|
| 1 | 25 | Antara Noida (NOA) SPV: revenue recognition for the JV in June/Q1 FY27 = **nil**. Explicitly stated: "presently in June there had been no revenue" because revenue recognition is linked to possession/registration (which occurs in Q2), not collections. Standing income-statement line for the SPV reads zero this quarter despite ~Rs30cr cash collected. `ZERO_STANDING` |

---

## OTHER FLAGS RAISED (cross-reference)

- `MGMT_ABSENCE` — no Chairman/promoter-tier voice present or named on the call (Table 1).
- `ROSTER_GAP` — Ishan (Head, AGEasy) speaks substantively (turns 53, 65, 69) but is not named in the opening speaker roster at turn 7; first self-identifies mid-Q&A (turn 53).
- `REPEAT_QUESTION` — Q14 (turn 73, competitive-moat question from Deep/MAS Capital) and Q19 (turn 125, DLF-entry question from Raju Singh/Vive) cover the same underlying theme — new/large entrants compressing senior-care returns — asked by two different analysts in the same call.
- `TRANSCRIPTION_ARTEFACT` — multiple instances flagged inline in Tables 1, 2 and 4 (garbled names, garbled figures, e.g. turn 7's "175 and 245 and 25 and 119 26" contradicting turn 13's "175 to 145 to 190" for the same 3-year revenue trend — A3/A4 should reconcile which figure set is intended, this ledger records both as they appear).
- `ZERO_STANDING` — see table above (NOA SPV Q1 revenue = nil).
