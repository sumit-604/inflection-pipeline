# A2 ENUMERATOR LEDGER — SOUTHWEST Q1 FY27 — concall

Source: `extract_concall_southwest_q1fy27.txt` (verbatim ASR transcript, not corrected; 168 source
lines / 187 extract lines, 100% line-for-line coverage per A1 header). Prior-quarter ledger: none
available (first concall run for this ticker) — no cross-quarter diff (`DROPPED_SLIDE` /
`ENTITY_CHANGE` style checks) is possible; noted per row where relevant instead of computed.

DOCTYPE NOTE: this is a poor-quality ASR transcript with almost no reliable speaker tagging.
Turns are recoverable only via blank-line paragraph breaks in the source file; many paragraph
blocks visibly splice two or three real speaker turns together (operator handoff + analyst
question, or management answer + analyst interjection) because the ASR/diarization dropped the
speaker-change marker. Every such spliced block is enumerated as ONE turn (the paragraph is the
only mechanically reproducible unit) and flagged `ASR_MERGED_TURN`, with the sub-speakers named
in the notes column so A3/A4 do not lose the internal structure.

---

## === A2 COUNT TEST ===
```
category: turns              grep_count: 83   sweep_count: 83   match: yes
category: questions          grep_count: 35   sweep_count: 35   match: yes
category: mgmt_numbers       grep_count: 155  sweep_count: 155  match: yes
category: participants       grep_count: 11   sweep_count: 11   match: yes   (analyst "from the line of" announcements; 9 distinct analysts + 1 no-response + 2 repeat rounds = 11)
category: hedge_fwd_phrases  grep_count: 122  sweep_count: 122  match: yes   (supplementary, NOT gated — see methodology note; lexicon is A3's authority, this is a best-effort proxy pass)
gate_a2: pass
```
=== END COUNT TEST ===

Grep methods used (reproducible):
- **turns**: `awk 'NR>=23 && NR<=187 && NF>0{c++}'` on the extract (23-187 is the transcript body,
  after the header/title and before the A1 YAML footer) → counts every blank-line-delimited
  paragraph block → 83. Manual sweep independently walked the same 83 blocks and assigned
  speaker + first words to each → 83. Match.
- **questions**: `awk` counting `?` characters in lines 23-187 → 35 (spread across 24 distinct
  lines, verified by per-line `gsub` count). Manual sweep read every `?`-terminated clause in
  context and attributed it to a speaker/topic → 35 individual rows. Match. NOTE: this transcript's
  ASR frequently drops terminal punctuation, so a number of real analyst asks have NO trailing
  `?` (e.g. line 81, line 99, line 137, line 151, line 165, line 175 lead-in) — these are enumerated
  separately below as **Implied Questions (IQ1-IQ7)**, flagged `NO_TERMINAL_QMARK`, and are NOT
  counted toward the gated `questions: 35` figure because they are not mechanically reproducible
  via the `?`-count grep. Nothing is dropped; the count boundary is just made explicit.
- **mgmt_numbers**: Python regex `\$?\d[\d,]*(?:\.\d+)?%?` over lines 23-187 → 155 raw numeric
  tokens across 47 source lines. Manual sweep re-derived the same 47 lines token-by-token from the
  verbatim text and attributed every token to a claim/context → 155. Match. (This count
  intentionally includes ASR noise tokens, date/quarter labels, and non-business digits like "L1"
  bidder classification — each is flagged accordingly rather than silently excluded, per the
  "enumerate everything, interpret nothing" mandate; a supplementary "substantive company KPI"
  reading is noted per-row in Table 4.)
- **participants**: `grep -n -i "from the line"` → 11 hits (10 x "next question from the line of...",
  1 x "first question from the line. of..."); one hit (line 155) contains two announcements
  (Sahir Hyderabad Duala, no response + Rahul, round 2) spliced together. Manual sweep of the same
  11 announcements → 11. Match.
- **hedge_fwd_phrases**: Python regex proxy lexicon (`expect|guidance|hope|confident|should|plan|
  going to|aim|target|commit|cautious|conservative|will|we intend|hopefully|strateg`) over lines
  23-187 → 122 hits across 48 lines. This is a raw lexicon count, not a curated list; most hits are
  the generic modal "will"/"should". A curated substantive subset (Table 6) is presented for A3/A4
  with turn numbers; rule 5's lexicon itself is A3's authority, not A2's, so this category is
  enumerated in good faith but excluded from the pass/fail gate.

---

## 0. Participants

| # | Role | Name (verbatim / ASR variant) | Firm | Notes |
|---|------|-------------------------------|------|-------|
| P1 | Moderator/Operator | (unnamed, generic conference-call operator) | conference-call service | opens/closes call, manages Q&A queue |
| P2 | Investor Relations | Ms. Purvangi Chan (ASR: "Purwangi Chan", "Purvangi Jen") | Advisory firm — name garbled across mentions: "Baloram Advisers" (line 23), "Baller Advisors" (line 25), "Valorum Advisor" (line 185) | `ASR_AMBIGUOUS` firm name — treated as one firm, three ASR renderings |
| P3 | Management — CMD | Mr. Vikas Jain (ASR: "Vikas Jen", later "Vicaran") | Managing Director & Chairman | delivers financial performance section, turn 3 |
| P4 | Management — JMD | Mr. "Pus Chen" / "P Chen" (ASR-garbled given name, surname uncertain) | Joint Managing Director | delivers business-overview section, turn 3 |
| P5 | Management — Finance/other | Referenced only as "Mr. Dhagal" (ASR-uncertain spelling) | designation not stated on the call | answers debt/D-E question (turn 36) after CMD defers ("Mr. Dhagal would be able to answer"); also implicitly the one asked to answer the JV cash/profit question at turns 42-44 | `NAME_UNCERTAIN` |
| P6 | Analyst | Raman KV | Sequent Investments | 2 rounds (turns 5-13, turns 50-53) |
| P7 | Analyst | Smit Gala (ASR: "Smith Gala") | RS PN Ventures (ASR-uncertain full name) | 1 round (turns 14-24) |
| P8 | Analyst | Sakshi Kapoor (ASR: "Sakit Kapoor") | Kapoor and Company | 1 long round (turns 25-45) |
| P9 | Analyst | Sajil Raj | Zenflow Finance Private Limited | 1 round (turns 46-49) |
| P10 | Analyst | Rahul | "Ne Money" / "leave money" (ASR variants of same firm name) | 2 rounds (turns 54-62, turns 67-68) |
| P11 | Analyst | Rishab Modi | AJ Agarwal Family Office (ASR: "AJ Agarval Family Office") | 1 round (turns 63-66) |
| P12 | Analyst (announced, no response) | Sahir Hyderabad Duala | Grow Bis Fund | announced at turn 67 (line 155), did not respond, operator moved on | `NO_RESPONSE` |
| P13 | Analyst | "Sep" (name truncated/ASR-garbled) | individual investor | 1 long round (turns 69-79) |
| P14 | Analyst | Akshay Jawar (ASR: "Akshai Jawar") | individual investor | 1 round (turns 80-81) |

No `MGMT_ABSENCE` flag — both CMD and JMD are present and speak (turn 3); a third management
voice (P5) is deferred to but does answer.

---

## 1. Speaker turns (83 rows — every blank-line-delimited paragraph block, lines 23-187)

| Turn | Line | Speaker(s) | First ~10 words | Flags |
|------|------|-----------|------------------|-------|
| 1 | 23 | Operator | "Ladies and gentlemen, good day and welcome to the..." | — |
| 2 | 25 | IR (Purvangi Chan) | "Thank you. Good evening everyone and a very warm..." | — |
| 3 | 27 | Management — JMD then CMD | "Uh thank you Pwangi and good evening to everyone..." | `ASR_MERGED_TURN` (JMD business overview + CMD financial performance, handoff mid-paragraph, no speaker tag) |
| 4 | 29 | Operator | "Thank you. Ladies and gentlemen, we will now begin..." | — |
| 5 | 31 | Analyst — Raman KV (Sequent Investments) | "Hello sir, can you hear me? Yeah sir. Uh..." | — |
| 6 | 33 | Management | "Yeah, I'll ask you to answer this question. So..." | — |
| 7 | 35 | Analyst + Management | "I just want to understand in terms of like..." | `ASR_MERGED_TURN` |
| 8 | 37 | Analyst + Management + Analyst | "Understood. And uh with respect to the execution time..." | `ASR_MERGED_TURN` |
| 9 | 39 | Management | "So see uh so you know we have some longer..." | — |
| 10 | 41 | Analyst — Raman KV | "And uh on the Oman on the Oman JV front..." | — |
| 11 | 43 | Management | "See Oman um we have two joint ventures. The..." | — |
| 12 | 45 | Analyst | "because you have like I think 35% stake it..." | — |
| 13 | 47 | Management | "no it yeah it is just added uh uh in..." | — |
| 14 | 49 | Operator + Analyst — Smit Gala (RS PN Ventures) | "Thank you. We take the next question from the..." | `ASR_MERGED_TURN` |
| 15 | 51 | Management | "Yeah, as as uh we have been saying that..." | — |
| 16 | 53 | Analyst | "So can you give me a well split of..." | — |
| 17 | 55 | Management | "yeah as I said it is going to be..." | — |
| 18 | 57 | Analyst | "Um okay. uh and uh once the production starts..." | — |
| 19 | 59 | Management | "Yeah, actually this in this block we have a..." | — |
| 20 | 61 | Analyst | "Okay. Uh and how is the pipeline looking apart..." | — |
| 21 | 63 | Management | "Yeah, it is looking great. In fact, all the..." | — |
| 22 | 65 | Analyst + Management | "Uh any number which we have that our exit..." | `ASR_MERGED_TURN` |
| 23 | 67 | Analyst | "Um okay and we have delivered delivered a strong..." | — |
| 24 | 69 | Management | "See we should we should experience significant growth in..." | — |
| 25 | 71 | Operator + Analyst — Sakshi Kapoor (Kapoor and Company) | "Thank you. We take the next question from the..." | `ASR_MERGED_TURN` |
| 26 | 73 | Management | "So basically Reliance is now being continued like for..." | — |
| 27 | 75 | Analyst | "So just to simplify it sir so for on..." | — |
| 28 | 77 | Management + Analyst interjection | "See we cannot divulge uh this detail you know..." | `ASR_MERGED_TURN` |
| 29 | 79 | Management | "so we can't we can't diverge this figures because..." | — |
| 30 | 81 | Analyst | "Correct sir. And uh sir when you were talking..." | — |
| 31 | 83 | Management + Analyst | "Oman Oman is uh you know it is um..." | `ASR_MERGED_TURN` |
| 32 | 85 | Management | "See, in the first phase, we invested about uh..." | — |
| 33 | 87 | Analyst | "Okay sir and lastly on this all part is..." | — |
| 34 | 89 | Management | "that's a listed entity in Australia where I'm also..." | — |
| 35 | 91 | Analyst | "Okay, sir. And can you give us uh the..." | — |
| 36 | 93 | Management | "Credit rating we have already uh announced in the..." | — |
| 37 | 95 | Analyst | "Okay. And Lastly sir just to classify us as..." | — |
| 38 | 97 | Management | "no no we are we are basically exploration services..." | — |
| 39 | 99 | Analyst | "Okay sir. Right sir I I'll join the queue..." | — |
| 40 | 101 | Analyst (continuing) | "Exactly. And the for the cash approvals which we..." | — |
| 41 | 103 | Analyst (continuing) | "from from the various JB sir whatever we are..." | — |
| 42 | 105 | Management | "Yeah, that that amount we we always mention in..." | — |
| 43 | 107 | Management/Analyst (ambiguous) | "Hello yes can you please answer this? How much..." | `ASR_MERGED_TURN`, `AMBIGUOUS_SPEAKER` |
| 44 | 109 | Management | "Uh it was it was somewhere uh uh it..." | — |
| 45 | 111 | Management + Analyst + Management | "Yeah, this is what we are putting the share..." | `ASR_MERGED_TURN` — heaviest splice in the transcript (cash-vs-consolidation exchange + garbled "78 versus 62" figure + monsoon seasonality + closing pleasantries all run together) |
| 46 | 113 | Operator + Analyst — Sajil Raj (Zenflow Finance Pvt Ltd) | "Thank you. We take the next question from the..." | `ASR_MERGED_TURN` |
| 47 | 115 | Management | "Already think we have already completed the exploration phase..." | — |
| 48 | 117 | Analyst | "Uh yes uh sir uh uh second question uh..." | — |
| 49 | 119 | Management | "So basically you know these uh blocks for underground..." | — |
| 50 | 121 | Operator + Analyst — Raman KV (round 2) | "Thank you. We take The next question from the..." | `ASR_MERGED_TURN` |
| 51 | 123 | Management | "Raman G this is as we have been telling..." | — |
| 52 | 125 | Analyst | "Understood. Understood. Uh can you can you just give..." | — |
| 53 | 127 | Management | "Wasn't 100%. The reason is that uh we have..." | `ASR_AMBIGUOUS` ("Wasn't" likely mis-transcribed "It was") |
| 54 | 129 | Operator + Analyst — Rahul (Ne Money) | "We take the next question from the line of..." | `ASR_MERGED_TURN` |
| 55 | 131 | Management | "Oh no no no this is from the this..." | — |
| 56 | 133 | Analyst | "Uh no sir I am asking for the amount..." | — |
| 57 | 135 | Management | "No no it is it is in addition to..." | — |
| 58 | 137 | Analyst | "Okay. And uh sir there was also an oil..." | — |
| 59 | 139 | Management + Analyst (multiple exchanges) | "Currently it is currently under uh execution right now..." | `ASR_MERGED_TURN` |
| 60 | 141 | Management | "Yeah. Uh we have we have completed uh almost..." | — |
| 61 | 143 | Analyst | "Okay. Thank you so much sir. So last question..." | — |
| 62 | 145 | Management | "Let's hope for the best means uh let's we..." | — |
| 63 | 147 | Operator + Analyst — Rishab Modi (AJ Agarwal Family Office) | "We take the next question from the line of..." | `ASR_MERGED_TURN` |
| 64 | 149 | Management | "we have been? Yeah. So we have been working..." | — |
| 65 | 151 | Analyst | "Okay. So was this a highly competitive bid uh..." | — |
| 66 | 153 | Management | "private clients generally have a different mindset. So uh..." | — |
| 67 | 155 | Operator (x2, incl. no-response) + Analyst — Rahul (round 2) | "Thank you. We take the next question from the..." | `ASR_MERGED_TURN`; `NO_RESPONSE` for Sahir Hyderabad Duala (Grow Bis Fund) |
| 68 | 157 | Management | "Yeah, it's it should be on the same line..." | `ASR_AMBIGUOUS` ("plus - 5%" likely "+/- 5%") |
| 69 | 159 | Operator + Analyst — "Sep" (individual investor) | "Thank you. We take the next question from the..." | `ASR_MERGED_TURN` |
| 70 | 161 | Management | "see uh obviously uh it's a competitive market uh..." | — |
| 71 | 163 | Management (continuing) | "So our business is 70% private as I believe..." | — |
| 72 | 165 | Analyst | "That's good. And that is negotiated contract. There is..." | — |
| 73 | 167 | Management | "These they are like uh like any any other..." | — |
| 74 | 169 | Analyst | "Perfectly all right. So You mean to say the..." | — |
| 75 | 171 | Management | "Yeah. Yeah. Definitely. And coming back to international business..." | — |
| 76 | 173 | Analyst + Management | "Understood. Understood. And coming back to international business..." | `ASR_MERGED_TURN`, `ASR_AMBIGUOUS` (10-yr vs 11-yr contract conflict) |
| 77 | 175 | Analyst | "Now coming back to the last question is about..." | — |
| 78 | 177 | Management + Analyst | "See primarily our focus would be to uh fund..." | `ASR_MERGED_TURN` |
| 79 | 179 | Management + Analyst + Management | "Jan Cole on the expecting revenue in financial year..." | `ASR_MERGED_TURN` |
| 80 | 181 | Operator + Analyst + Management + Analyst + Management + Analyst | "thank you we take the next question from the..." | `ASR_MERGED_TURN`, `ASR_AMBIGUOUS` (FY27-28 vs FY28-29 conflict — see Table 4 row 47) |
| 81 | 183 | Management | "The promoters have currently acquired uh uh you know..." | — |
| 82 | 185 | Operator + Management | "And thank you ladies and gentlemen. As there are..." | `ASR_MERGED_TURN` |
| 83 | 187 | Operator | "Thank you. On behalf of Southwest Panacle Exploration Limited..." | — |

`ASR_MERGED_TURN` count: 22 of 83 turns (turns 3,7,8,14,22,25,28,31,43,45,46,50,54,59,63,67,69,76,78,79,80,82) — 26.5% of all turns carry a speaker splice, a direct consequence of ASR diarization loss, not of the underlying call.

---

## 2. Analyst questions — strict (`?`-terminated, 35 rows, GATE-matched)

| Q# | Turn | Line | Analyst | Firm | Topic | Verbatim clause | Flags |
|----|------|------|---------|------|-------|------------------|-------|
| 1 | 5 | 31 | Raman KV | Sequent Investments | Audio check | "can you hear me?" | `AUDIO_CHECK` |
| 2 | 5 | 31 | Raman KV | Sequent Investments | Order book split, oil&gas vs metals | "Can you give the split between oil and gas orders versus metals...percentage wise?" | — |
| 3 | 8 | 37 | Raman KV | Sequent Investments | Execution time period of order book | "what's the execution time period you're talking about?" | `ASR_MERGED_TURN` |
| 4 | 8 | 37 | Management | — | Clarifying which contract analyst means | "Which which one?" | `MGMT_CLARIFYING_Q` |
| 5 | 10 | 41 | Raman KV | Sequent Investments | Oman JV2 revenue contribution timeline | "what will be the revenue contribution this year and how will revenue...start improving?" | — |
| 6 | 18 | 57 | Smit Gala | RS PN Ventures | Revenue-sharing agreement with government post-production | "do we have any revenue sharing agreement with the government or how will the revenue work post the production?" | — |
| 7 | 20 | 61 | Smit Gala | RS PN Ventures | Pipeline outlook | "How is the pipeline looking uh for our business?" | — |
| 8 | 27 | 75 | Sakshi Kapoor | Kapoor and Company | Reliance/HZL revenue contribution split | "what was the contribution from Reliance...and from Hindustan[Zinc]...on a quarterly basis?" | — |
| 9 | 31 | 83 | Sakshi Kapoor | Kapoor and Company | Alara rights-issue investment amount (INR) | "what is the total amount in rupee term?" | `ASR_MERGED_TURN` |
| 10 | 31 | 83 | Sakshi Kapoor | Kapoor and Company | Alara rights-issue investment amount (continuation) | "How much are we investing?" | `ASR_MERGED_TURN` |
| 11 | 35 | 91 | Sakshi Kapoor | Kapoor and Company | Net debt as of 30 June | "can you give us the net debt number...as on the 30th June?" | — |
| 12 | 35 | 91 | Sakshi Kapoor | Kapoor and Company | Credit-rating due date | "What is our debt and when is our uh credit rating due sir?" | — |
| 13 | 40 | 101 | Sakshi Kapoor | Kapoor and Company | JV/equity-participation cash accrual, last year | "how much have we accrued through the JVs and the equity participation?" | — |
| 14 | 42 | 105 | Management | — | Handoff — asking colleague to answer | "can you please explain...can you please answer this?" | `MGMT_CLARIFYING_Q` (handoff) |
| 15 | 43 | 107 | Ambiguous (analyst prompt or moderator relay) | — | Re-prompting for JV profit answer | "Hello yes can you please answer this?" | `ASR_MERGED_TURN`, `AMBIGUOUS_SPEAKER` |
| 16 | 46 | 113 | Sajil Raj | Zenflow Finance Pvt Ltd | Coal block allocation outlook, 3-4 yrs | "could you share your broader outlook on coal block allocations and exploration activities over the next three to four years?" | `ASR_MERGED_TURN` |
| 17 | 46 | 113 | Sajil Raj | Zenflow Finance Pvt Ltd | Opportunity-pipeline evolution/quantification | "how do you see the opportunity pipeline evolve for uh SWPD?" | `ASR_MERGED_TURN` |
| 18 | 48 | 117 | Sajil Raj | Zenflow Finance Pvt Ltd | UCG discussion status update | "could you share where these discussion uh stand today?" | — |
| 19 | 48 | 117 | Sajil Raj | Zenflow Finance Pvt Ltd | UCG FY27 revenue-contribution expectation | "should investors expect any uh meaningful contribution from UCG in the financial year 27?" | — |
| 20 | 50 | 121 | Raman KV | Sequent Investments (round 2) | Audio check | "can you hear me?" | `AUDIO_CHECK` |
| 21 | 52 | 125 | Raman KV | Sequent Investments | Resource-utilization ballpark | "can you can you just give a ballpark figure with respect to the routine[utilization]?" | — |
| 22 | 52 | 125 | Raman KV | Sequent Investments | Resource utilization (continuation) | "What was the utilization for the company?" | — |
| 23 | 59 | 139 | Rahul | Ne Money | Oil India contract revenue timing | "So can we expect the revenue in the next quarter?" | `ASR_MERGED_TURN` |
| 24 | 59 | 139 | Rahul | Ne Money | Aquifer-mapping tender progress | "has there been any progress in those contracts or tenders?" | `ASR_MERGED_TURN` |
| 25 | 61 | 143 | Rahul | Ne Money | Growth guidance for the year | "can you give a guidance for the growth for this year?" | `REPEAT_QUESTION` (cf. Q for Smit Gala at turn 23) |
| 26 | 61 | 143 | Rahul | Ne Money | Beat 20% guidance? | "Are you expecting to beat your 20% guidance that you gave in the last poll?" | `REPEAT_QUESTION` |
| 27 | 63 | 147 | Rishab Modi | AJ Agarwal Family Office | Reason HZL chose SOUTHWEST | "what do you think was the key reason Hindustan[Zinc] chose South Pinnacle for such a large contract?" | `ASR_MERGED_TURN` |
| 28 | 64 | 149 | Management | — | Verbal echo, non-substantive | "we have been?" | `NON_SUBSTANTIVE`, `ASR_ARTIFACT` |
| 29 | 67 | 155 | Rahul | Ne Money (round 2) | Reliance 35-40% FY27 revenue guidance, still valid? | "is it still in the same line or has the percentage changed?" | `ASR_MERGED_TURN` |
| 30 | 74 | 169 | "Sep" | individual investor | Confirming margins maintainable / competition manageable | "Is that right to understand?" | — |
| 31 | 76 | 173 | "Sep" | individual investor | Alara 11-yr/$125M contract revenue/cash contribution | "how much is the contribution of revenue and you know net cash that we expect in next 11 years?" | `ASR_MERGED_TURN`, `ASR_AMBIGUOUS` (10-yr vs 11-yr, see Table 4 row 44) |
| 32 | 76 | 173 | "Sep" | individual investor | Confirming contract duration/value | "11 years 125 million contract is that right?" | `ASR_AMBIGUOUS` |
| 33 | 76 | 173 | "Sep" | individual investor | Confirming garbled margin figures | "Is that right?" [re: "78% margin of which 37% is RCS"] | `ASR_AMBIGUOUS` (undefined "RCS", meaning unresolved) |
| 34 | 79 | 177/179 | "Sep" | individual investor | Revenue timing, AML & Jharkhand coal | "when are you expecting revenue from all these these two HML and Jan Cole?" | `ASR_MERGED_TURN` |
| 35 | 80 | 181 | Akshay Jawar | individual investor | Promoter dilution plans | "is there anything planned like is there any promoter dilution...that you all are planning on doing?" | `ASR_MERGED_TURN` |

### 2a. Implied questions — no terminal `?` (ASR punctuation loss; supplementary, NOT gate-counted)

| IQ# | Turn | Line | Analyst | Firm | Topic | Flags |
|-----|------|------|---------|------|-------|-------|
| IQ1 | 30 | 81 | Sakshi Kapoor | Kapoor and Company | Alara rights-issue rationale + Oman geopolitical impact | `NO_TERMINAL_QMARK` |
| IQ2 | 39 | 99 | Sakshi Kapoor | Kapoor and Company | M&A opportunity in drilling segment (suggestion framed as question) | `NO_TERMINAL_QMARK` |
| IQ3 | 58 | 137 | Rahul | Ne Money | Oil India (2024) contract status update request | `NO_TERMINAL_QMARK` |
| IQ4 | 65 | 151 | Rishab Modi | AJ Agarwal Family Office | Number of serious bidders / competitive bid (sentence truncated mid-clause) | `NO_TERMINAL_QMARK` |
| IQ5 | 72 | 165 | "Sep" | individual investor | Negotiated contract vs reverse auction confirmation | `NO_TERMINAL_QMARK` |
| IQ6 | 25 | 71 | Sakshi Kapoor | Kapoor and Company | Whether HZL (307cr) + Reliance (160/166cr) orders are reflected in this quarter's revenue | `NO_TERMINAL_QMARK` |
| IQ7 | 77 | 175 | "Sep" | individual investor | Funding-plan / capital-raise approach for AML + Jharkhand coal | `NO_TERMINAL_QMARK` |

**REPEAT_QUESTION summary**: (a) 20% CAGR / "beat guidance" question asked independently by Smit
Gala (turn 23) and Rahul (turn 61); (b) debt/D-E ratio metric revisited by Sakshi Kapoor (turn 35,
net debt) and Akshay Jawar (turn 80, target D-E ceiling) — related but not verbatim-identical asks,
flagged for A3/A4 topic-clustering.

---

## 3. Every forward-commitment / hedge phrase — curated substantive subset (supplementary, not gated)

Raw lexicon proxy pass found 122 hits across 48 lines (mostly the generic modal "will"/"should" —
see COUNT TEST methodology note). Curated substantive subset for A3/A4:

| # | Turn | Line | Speaker | Phrase | Type |
|---|------|------|---------|--------|------|
| H1 | 3 | 27 | Management | "we remain confident in our growth outlook" | `FORWARD_COMMITMENT` |
| H2 | 3 | 27 | Management | "we intend to start this block in financial year 2829" [FY28-29] | `FORWARD_COMMITMENT` |
| H3 | 3 | 27 | Management | "we expect this trend to continue as in future as well" (H2-over-H1 seasonality) | `FORWARD_COMMITMENT` |
| H4 | 3 | 27 | Management | "reaffirming our long-term commitment to our international mining business" (re: Alara rights issue) | `FORWARD_COMMITMENT` |
| H5 | 21 | 63 | Management | "it should go on for the next uh 3 to 5 years" (pipeline visibility) | `FORWARD_COMMITMENT` |
| H6 | 24 | 69 | Management | "we should be able to achieve significant growth...for the financial year 27" | `FORWARD_COMMITMENT`/`HEDGE` (cyclicality caveat attached) |
| H7 | 26 | 73 | Management | "for the next three and a half four years it'll keep on giving us...revenue...consistently" | `FORWARD_COMMITMENT` |
| H8 | 28 | 77 | Management | "we cannot divulge...this detail...this is the confidential detail" | `HEDGE` (non-disclosure) |
| H9 | 62 | 145 | Management | "Let's hope for the best...we have been conservative...whatever we have told we've achieved more" | `HEDGE` (guidance conservatism) |
| H10 | 62 | 145 | Management | "our business is quite dynamic and quite cyclical" | `HEDGE` |
| H11 | 68 | 157 | Management | "it should be on the same line plus - 5%" (Reliance revenue-share guidance) | `FORWARD_COMMITMENT` w/ `ASR_AMBIGUOUS` |
| H12 | 75 | 171 | Management | "the margin should be maintained because the entry barriers are quite high" | `FORWARD_COMMITMENT` |
| H13 | 78 | 177 | Management | "primarily our focus would be to fund these projects from our internals...the debt...and also the...offtake contracts" | `FORWARD_COMMITMENT` |
| H14 | 79 | 179 | Management | "we are hopeful of achieving that goal" (AML/Jharkhand coal internal evaluation) | `HEDGE` |
| H15 | 79 | 179 | Management | "it all depends on the results which we derive from the exploration" (200cr AML+coal investment) | `HEDGE` (contingency) |
| H16 | 80 | 181 | Management | "we are getting towards being a debt-free company" | `FORWARD_COMMITMENT` |
| H17 | 80 | 181 | Management | "the idea is to prepare ourselves to take a plunge into...coal block execution" | `FORWARD_COMMITMENT` |
| H18 | 51 | 123 | Management | "this figure should go up" (private-client mix, 70-75%) | `FORWARD_COMMITMENT` |

---

## 4. Management / quantitative-claim numbers (47 rows covering all 155 raw numeric tokens)

| # | Line | Turn | Speaker | Tokens (verbatim) | Claim(s) | Flags |
|---|------|------|---------|--------------------|----------|-------|
| 1 | 23 | 1 | Operator | 1, 27 | "Q1 FI27 earnings conference call" — quarter/year label | `CONTEXT_DATE` |
| 2 | 25 | 2 | IR | 2027 | "financial year 2027" — full-year label | `CONTEXT_DATE` |
| 3 | 27 | 3 | Management (JMD+CMD) | 2,3,19,165,43,3.3,20,761,7,60,166,7,77%,2,3,2027,1,27,62,54,54%,15,157%,24.15%,9.3,2.5,1,26,289%,2829,20,75% (32 tokens) | 2D/3D seismic service labels (x2, not KPIs); 19-yr track record; 165+ projects completed; 43 drilling rigs; 3.3mn meters drilled; 20 ongoing projects (mentioned twice in this turn); order book **761 Cr**; HZL order stated as **"7 crores"**; Reliance CBM extension stated as **"over 166 crores"** (with a garbled noise fragment "60" in "I 60 166"); private-client mix stated as **"7 77%"**; FY2027/Q1 date labels (x3 pairs); operating revenue **62 Cr**; revenue growth **54%** (stuttered as bare "54" then "54%"); EBITDA **15 Cr**; EBITDA growth **157%** YoY; EBITDA margin **24.15%**; PAT **9.3 Cr** vs comparator **2.5 Cr** (Q1 FY26); PAT growth **289%** YoY; coal production start **"2829"**; warrant conversion: balance **75%** consideration received | `ASR_AMBIGUOUS` (HZL order "7 crores" — resolved to 307cr at row 21; Reliance value; private mix %; "2829"=FY28-29); `ASR_STUTTER` (54/54%); `NOT_A_NUMBER` (2D/3D tokens x2); `CONTEXT_DATE` |
| 4 | 31 | 5 | Analyst (Raman KV) | 761 | restates order book **761 Cr** | cross-ref row 3 |
| 5 | 35 | 7 | Management (merged) | 25%,15,45,30%,15,25% | oil&gas **~25%** of order book; vertical-mix range garbled "15 to 45 to 30%"; restated range "15 to 25%" | `ASR_AMBIGUOUS`; `ASR_MERGED_TURN` |
| 6 | 37 | 8 | Analyst (merged) | 760 | rounds order book to **"760"** | `ROUNDING_VARIANT`; `ASR_MERGED_TURN` |
| 7 | 39 | 9 | Management | 6 | contract-duration tier: **6-month** contracts (4-yr and 1-2-yr tiers word-spelled, not digit-captured) | — |
| 8 | 41 | 10 | Analyst (Raman KV) | $125 | Oman JV2 (copper mining) contract value **$125M** | cross-ref rows 11, 44 |
| 9 | 43 | 11 | Management | 35% | Oman JV1 stake **35%** | cross-ref |
| 10 | 45 | 12 | Analyst | 35% | restates Oman JV1 stake **35%** | cross-ref |
| 11 | 47 | 13 | Management | 35%,$125,10,3,4,35%,2,3,1400 | Oman JV1 stake **35%** (x2); **$125M / 10-year** contract | **conflicts with "11-year" claim at row 44 (line 173)**; JV1 profit last quarter **"3 to 4" Cr** at 35% share; Oman drilling-services backlog **2-3 years**; Oman JV2 exploration block area **1,400 sq km** | `ASR_AMBIGUOUS`/`INCONSISTENT` (10yr vs 11yr) |
| 12 | 49 | 14 | Analyst (merged) | 200,278,29 | Jharkhand capex phase-1 **~200 Cr**; funding-timing garbled **"FY278 and 29"** | `ASR_AMBIGUOUS`; `ASR_MERGED_TURN` |
| 13 | 51 | 15 | Management | 200 | confirms Jharkhand capex phase-1 **~200 Cr** | cross-ref |
| 14 | 53 | 16 | Analyst | 200,26 | restates **200 Cr**; references **FY26** cash flow (no figure given) | `CONTEXT_DATE` |
| 15 | 55 | 17 | Management | 200 | restates **200 Cr**, including non-fund-based exposure | cross-ref |
| 16 | 59 | 19 | Management | 24.25%,2829 | Jharkhand revenue-share with government **24.25%**; production start **"2829"** | `ASR_AMBIGUOUS` (FY28-29) |
| 17 | 63 | 21 | Management | 3,5 | pipeline visibility **3-5 years** | — |
| 18 | 65 | 22 | Analyst+Mgmt (merged) | 27,761,3,5 | FY27 exit-order-book query; order book **761** restated (rendered "761 K" — unit garble); visibility **3-5 years** restated | `ASR_AMBIGUOUS`; `ASR_MERGED_TURN` |
| 19 | 67 | 23 | Analyst | 1,50%,20%,27,24% | Q1 growth **">50%"** (analyst approximation of actual 54%); guidance **"~20%"** CAGR; FY27 label; margin **"24%"** (vs actual 24.15%) | `ROUNDING_VARIANT` |
| 20 | 69 | 24 | Management | 1,27,2,1,27 | Q1/FY27 labels (x2 each); H2/H1 seasonality references | `CONTEXT_DATE`; `CONTEXT_PERIOD_REF`; `NOT_A_NUMBER` |
| 21 | 71 | 25 | Analyst (Sakshi Kapoor, merged) | 307,160 | HZL order value **CONFIRMED 307 Cr** (resolves row 3's ASR ambiguity); Reliance value cited **"160 Cr"** | **conflicts with row 3's ~166cr and row 35's 166cr** | `ASR_AMBIGUOUS`/`INCONSISTENT`; `ASR_MERGED_TURN` |
| 22 | 73 | 26 | Management | 2,3 | Reliance relationship **~2(.5) years**; HZL ramp-up **~3 months** | — |
| 23 | 75 | 27 | Analyst | 61.78 | revenue base cited **"61.78 Cr"** vs mgmt's clean **"62 Cr"** (row 3) | `ASR_AMBIGUOUS`/`ROUNDING_VARIANT` |
| 24 | 79 | 29 | Management | 60%,60% | HZL+Reliance = **60%** of order book; = **60%** of revenue | — |
| 25 | 85 | 32 | Management | 500000,2.8,2.8,1 | Alara rights-issue phase-1: **500,000 AUD = 2.8 Cr** (stated twice); phase-2 cap **up to 1 million AUD** | `ASR_STUTTER` |
| 26 | 89 | 34 | Management | 1.25% | Alara direct stake **~1.25%** | — |
| 27 | 91 | 35 | Analyst | 30 | net-debt as-of date: **30th June** | `CONTEXT_DATE` |
| 28 | 93 | 36 | Management | 15,39 | debt **~15 Cr**; D/E **"less than 39"** | `ASR_AMBIGUOUS` (missing decimal, = 0.39) |
| 29 | 109 | 44 | Management | 1.5,1.32 | JV profit last year **~1.5 Cr**; JV profit this quarter **1.32 Cr** (framed by mgmt as "much higher" though 1.32 < 1.5) | `INTERNAL_INCONSISTENCY` |
| 30 | 111 | 45 | Mgmt/Analyst (merged) | 78,62,1,4,2 | garbled figures **"78 versus 62"** (meaning unresolved); Q1/Q4/Q2 seasonality references | `ASR_AMBIGUOUS` (unresolved); `ASR_MERGED_TURN`; `CONTEXT_PERIOD_REF` |
| 31 | 115 | 47 | Management | 200,500,1,1,200,200,2030,30,40% | industry stats (not company-specific): **~200** coal blocks under auction; **~500** mining blocks (critical minerals/base metals); India coal production **"touched/crossed 1 billion"** tons (x2); production increase **~200mn tons** over 2-3 years (x2, stutter); by **2030** growth of **30-40%** | `INDUSTRY_STAT`; `ASR_STUTTER` |
| 32 | 117 | 48 | Analyst | 27 | FY27 label (UCG contribution question) | `CONTEXT_DATE` |
| 33 | 123 | 51 | Management | 70,75%,25,30% | private-client mix **70-75%**; government-sector mix **25-30%** | cross-ref row 3 (77%), row 43 (70%) |
| 34 | 127 | 53 | Management | 100%,100% | resource utilization **"wasn't 100%"** / **"more than 100%"** — contradictory phrasing | `ASR_AMBIGUOUS` (likely mis-negation) |
| 35 | 129 | 54 | Analyst (Rahul, merged) | 2222,166,55 | CBM order-book figure **"2222 million"**; Reliance extension **166 Cr** (3rd citation); unexecuted phase-1 balance **~55 Cr** (analyst-introduced, not confirmed by mgmt's reply) | `ASR_AMBIGUOUS` (2222 million); `UNCONFIRMED_BY_MGMT` (55cr); `ASR_MERGED_TURN` |
| 36 | 137 | 58 | Analyst | 2024,60,20 | Oil India contract awarded **2024**, value **60 Cr**, **~20 Cr** execution remaining (unit implied) | `UNIT_IMPLIED` |
| 37 | 141 | 60 | Management | 65%,35% | aquifer-mapping project **65%** complete / **35%** remaining | — |
| 38 | 143 | 61 | Analyst | 20% | restates **20% CAGR** guidance | cross-ref row 19; `REPEAT_QUESTION` |
| 39 | 155 | 67 | Analyst (Rahul rd2, merged) | 27,35,40% | FY27 label; Reliance revenue-contribution guidance restated **35-40%** | `ASR_MERGED_TURN` |
| 40 | 157 | 68 | Management | 5% | Reliance guidance variance band **"+/- 5%"** | `ASR_AMBIGUOUS` ("plus - 5%") |
| 41 | 159 | 69 | Analyst | 1 | "L1" bid-classification term (not a business metric) | `NOT_A_NUMBER` |
| 42 | 161 | 70 | Management | 1 | "L1" bid-classification term (repeated) | `NOT_A_NUMBER` |
| 43 | 163 | 71 | Management | 70% | private-client mix **70%** (3rd mention) | cross-ref |
| 44 | 173 | 76 | Analyst+Mgmt (merged) | 11,125,11,35%,11,125,5,7%,78%,37% | Alara/JV1 contract **"11-year, $125M"** (analyst) | **conflicts with row 11's "10-year" mgmt claim**; restated 3x/2x (stutter); JV1 stake **35%** restated; Oman services net margin **"5 to 7%"**; garbled **"78% margin of which 37% is RCS"** (undefined term "RCS", meaning unresolved) | `ASR_AMBIGUOUS`/`INCONSISTENT` (10yr vs 11yr); `ASR_STUTTER`; `ASR_AMBIGUOUS` (78%/37% RCS unresolved); `ASR_MERGED_TURN` |
| 45 | 175 | 77 | Analyst | 17,17 | AML stake **"17 and a half%" = 17.5%**, stated twice | — |
| 46 | 179 | 79 | Mgmt+Analyst (merged) | 2829,2030,2030,200 | Jharkhand coal revenue **FY28-29** (restated); AML/Oman project revenue timing garbled **"around 2030 to 2030"** (duplicate); combined AML+Jharkhand total planned investment **~200 Cr** (possible overlap with the Jharkhand-only 200cr capex at rows 12-15) | `ASR_AMBIGUOUS`; `CLARIFICATION_NEEDED` (is this incremental or a restatement?); `ASR_MERGED_TURN` |
| 47 | 181 | 80 | Analyst+Mgmt (merged) | 2728,2829,39,2 | analyst notes investor presentation states coal production **"2728" = FY27-28** — **conflicts with the concall's repeated "FY28-29" claims** (rows 3, 16, 46); mgmt reconfirms **"2829" = FY28-29**; D/E **"It's 39"** (=0.39, 2nd mention); debt-free timeline **"next 2 [to] 3 years"** | `ASR_AMBIGUOUS`/`INCONSISTENT` — **material IP-vs-concall discrepancy, flag prominently for A3/A4**; `ASR_MERGED_TURN` |

Token-sum check: 2+1+32+1+6+1+1+1+1+1+9+3+1+2+1+2+2+4+5+5+2+2+1+2+4+1+1+2+2+5+9+1+4+2+3+3+2+1+3+1+1+1+1+10+2+4+4 = **155**. Matches grep count.

### 4a. Named-example cross-check (per task injection)
- revenue 62 Cr → row 3 ✓ (analyst variant 61.78cr → row 23, flagged)
- EBITDA 15 Cr / margin 24.15% → row 3 ✓
- PAT 9.3 Cr → row 3 ✓
- order book 761 Cr → rows 3,4,6,18 ✓
- HZL order 307 Cr / spoken "7 crores" → rows 3 (ASR-ambiguous origin) and 21 (resolved) ✓
- RIL 166 Cr → rows 3, 21 (160cr variant, flagged inconsistent), 35, 46 ✓
- private-client mix 77% and separately 70-75% → rows 3, 33, 43 ✓
- oil&gas ~25% → row 5 ✓
- JV profit last year ~1.5 Cr / this quarter 1.32 Cr → row 29 ✓
- JV stake 35% → rows 9,10,11,44 ✓
- Alara Australia direct stake ~1.25% → row 26 ✓
- AML stake 17.5% → row 45 ✓
- Alara rights 500,000 AUD / 2.8 Cr, up to 1 million AUD → row 25 ✓
- coal capex phase-1 ~200 Cr → rows 12,13,14,15 ✓
- revenue-share 24.25% → row 16 ✓
- debt "around 15 crores" / D/E <0.39 → rows 28, 47 ✓
- coal production FY28-29 ("2829") → rows 3,16,46,47 (with the 47-row FY27-28-vs-FY28-29 conflict) ✓
- resource utilisation >100% → row 34 ✓
- Oman JV net margin 5-7% → row 44 ✓
- Oman services $125M 10-year → rows 11, 44 (10yr-vs-11yr conflict) ✓
- guidance ~20% medium-term → rows 19, 38 ✓
- Reliance 35-40% of FY27 revenue +/- 5% → rows 39, 40 ✓
- CBM order "2222 million" → row 35 ✓
- old Oil India 2024 contract 60 Cr with ~20 left → row 36 ✓

All named examples located and enumerated.

---

## 5. Cross-cutting flags summary

| Flag | Instances | Where |
|------|-----------|-------|
| `ASR_MERGED_TURN` | 22 turns | see Table 1 |
| `ASR_AMBIGUOUS` | ~18 distinct figures | Table 4 rows 1,2,3,5,11,12,14,16,18,19,21,23,28,30,31(ind. stats not co. specific but still flagged),34,35,40,44,46,47 |
| `ASR_STUTTER` | 4 | Table 4 rows 3(54%),25(2.8cr),31(1bn/200mt),44(11yr/125M) |
| `ROUNDING_VARIANT` | 3 | Table 4 rows 6(760),19(>50%/24%),23(61.78) |
| `INTERNAL_INCONSISTENCY` | 1 | Table 4 row 29 (JV profit "much higher" but 1.32<1.5) |
| `INDUSTRY_STAT` (not company KPI) | 1 row (9 tokens) | Table 4 row 31 |
| `UNCONFIRMED_BY_MGMT` | 1 | Table 4 row 35 (55cr unexecuted balance) |
| `UNIT_IMPLIED` | 1 | Table 4 row 36 |
| `CLARIFICATION_NEEDED` | 1 | Table 4 row 46 (200cr combined vs 200cr Jharkhand-only, possible double count) |
| `NOT_A_NUMBER` | 4 rows | Table 4 rows 3(x2),20,41,42 |
| `CONTEXT_DATE` / `CONTEXT_PERIOD_REF` | 8 rows | Table 4 rows 1,2,14,18(part),20,27,30,32 |
| `NO_RESPONSE` | 1 analyst | Sahir Hyderabad Duala, Grow Bis Fund (turn 67/line 155) |
| `REPEAT_QUESTION` | 2 topic clusters | 20% guidance (Q25/Q26 vs turn 23); D-E ratio (turn 35 vs turn 80) |
| `MGMT_CLARIFYING_Q` | 2 | Q4 (turn 8), Q14 (turn 42) |
| `AMBIGUOUS_SPEAKER` | 1 | Q15 (turn 43) |
| `NON_SUBSTANTIVE`/`ASR_ARTIFACT` | 1 | Q28 (turn 64) |
| `NAME_UNCERTAIN` | 1 | P5, "Mr. Dhagal" |
| `NO_TERMINAL_QMARK` | 7 | Implied Questions IQ1-IQ7 |
| **Most material for A3/A4**: the FY27-28 (investor presentation, per analyst at turn 80) vs FY28-29 (concall, repeated at turns 3, 19, 79, 80) coal-production-start discrepancy, and the Oman/Alara JV1 contract "10-year" (turn 13/line 47) vs "11-year" (turn 76/line 173) conflict. Both are internal to the call/IP set, not resolved by management, and should be checked against the investor presentation ledger for reconciliation. |

---

```yaml
stage: A2-enumerator
company: "SOUTHWEST"
quarter: "Q1 FY27"
doctype: "concall"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/southwest-q1fy27/work/ledger_concall_southwest_q1fy27.md"
counts:
  notes: 0
  line_items: 0
  zero_standing: 0
  agenda_items: 0
  auditor_paras: 0
  entities: 0
  turns: 83
  questions: 35
  mgmt_numbers: 155
  slides: 0
  slide_numbers: 0
flags_raised: [ASR_MERGED_TURN, ASR_AMBIGUOUS, ASR_STUTTER, ROUNDING_VARIANT, INTERNAL_INCONSISTENCY, INDUSTRY_STAT, UNCONFIRMED_BY_MGMT, UNIT_IMPLIED, CLARIFICATION_NEEDED, NOT_A_NUMBER, CONTEXT_DATE, NO_RESPONSE, REPEAT_QUESTION, MGMT_CLARIFYING_Q, AMBIGUOUS_SPEAKER, NON_SUBSTANTIVE, NAME_UNCERTAIN, NO_TERMINAL_QMARK]
gate_a2: pass
mismatch_note: ""
```
