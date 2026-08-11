# A2 COMPLETENESS LEDGER — GOLDIAM Q1 FY27 Concall Transcript

Source: `runs/goldium-q1fy27/work/extract_concall_goldiam_q1fy27.txt`
Doctype: concall (transcript, no explicit speaker labels/timestamps in source; turns
inferred from paragraph/blank-line boundaries and moderator hand-off phrases).
Enumeration unit: SPEAKER TURN, keyed to the embedded transcript line numbers
already present in the A1 extract (1-201; content lines are odd-numbered from
line 5 through line 201, blank separator lines are even-numbered; lines 1-3 are
transcript title/header metadata, not a spoken turn).

Methodology note on merged turns: this transcript is a garbled machine
transcription with several paragraphs that splice two speakers' material
together with no blank-line break (e.g. an analyst's brief interjection glued
to the middle of management's answer, or an analyst's follow-up question glued
onto the tail of management's prior answer with no break before the next
answer). These are flagged `TRANSCRIPT_ARTIFACT` / `MERGED_TURN` in place; the
enumeration unit (one row per blank-line-delimited paragraph) is preserved
exactly as the source presents it so no material is silently split or dropped.

```
=== A2 COUNT TEST ===
category: turns              grep_count: 99   sweep_count: 99   match: yes
category: participants       grep_count: 10   sweep_count: 10   match: yes
  (grep = case-insensitive count of "question is (on|from) the line of" moderator
  hand-off phrases = 10 Q&A rounds; sweep = independent manual walk of all 10
  hand-offs, normalizing name-transcription variants, resolves to 7 unique
  analysts with 3 taking a second round: Doshi, Ganani, Saurabh/Kumar)
category: questions           sweep_pass1: 32   sweep_pass2: 32   match: yes
  (literal "?" grep on the transcript body returns only 15 hits — this
  undercounts because the machine transcription frequently drops the question
  mark on interrogative sentences; literal-punctuation grep is therefore not a
  reliable cross-check on this source and is reported for transparency only,
  not used as the count-test denominator. The reconciling two ways used were
  two independent manual passes over all 99 turns, both landing on 32 question
  rows: 29 substantive + 3 procedural ("can you hear me" / "am I audible").)
category: mgmt_numbers        sweep_pass1: 27   sweep_pass2: 27   match: yes
category: forward_hedge       sweep_pass1: 19   sweep_pass2: 19   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

---

## 1. PARTICIPANTS

| # | Name (as transcribed) | Designation | Side | Turns | Flags |
|---|---|---|---|---|---|
| 1 | Unnamed conference operator ("Palak"? — name only surfaces once, embedded in host's thanks at line 7, spelling uncertain) | Call operator | Non-participant (call mechanics) | L5, L11, L145, L161, L169, L183(?), L199 (opening, Q&A open, hand-offs, close) | `PARTICIPANT_NAME_UNCLEAR` |
| 2 | Rahul Dhani | Host, Monarch Network Capital Limited (call arranger) | Non-participant (call mechanics) | L7 | — |
| 3 | Rash Bansali (transcribed; likely "Rashesh Bansali" or similar) | Executive Chairman | Management | Introduced L7; speaks in-turn additions at L19 (embedded), L79, L121 (embedded), L153, L189(?) | — |
| 4 | Anmul / Anmol Bansali | Managing Director | Management | Introduced L7; primary answering voice, self-identifies "Anmali here" at L19; answers nearly all Q&A turns | — |
| 5 | Dixit / Zikit Doshi (name transcribed two ways) | Analyst, Whitestone PMS (transcribed "Whit Stone PMS" / "Whitstone PMS") | Analyst | Round 1: L11(intro)-L35; Round 2: L161(intro)-L167 | asked twice — see REPEAT_QUESTION note below |
| 6 | Amit B. Rathi (transcribed "Aam B. Rali") | Analyst, Dalal & Broacha Stock Broking Private Limited | Analyst | L37(intro)-L45 | `NAME_GARBLED` |
| 7 | Anubhav Mukharji | Analyst, Prescient Capital (transcribed "Precient Capital") | Analyst | L47(intro)-L85 | — |
| 8 | Bharat Ganani | Analyst, Money Control Research (transcribed "Bat Ganani" round 1) | Analyst | Round 1: L87(intro)-L105; Round 2: L169(intro)-L181 | asked twice |
| 9 | Ankush Agarwal | Analyst, Search Capital | Analyst | L107(intro)-L127 | — |
| 10 | Kumar Saurabh / Sarup Kumar (same person, name transcribed two ways) | Analyst, Scientific Investing | Analyst | Round 1: L129(intro)-L141; Round 2: L183(intro)-L193 | asked twice; second round fulfils a question explicitly deferred in round 1 (L135) |
| 11 | Vivek Gautam (transcribed "Vive Gotham") | Analyst, GS Investment | Analyst | L145(intro)-L157 | `NAME_GARBLED` |

`MGMT_ABSENCE`: not triggered — both the Executive Chairman and the Managing
Director are present and both are heard answering substantive questions
throughout the call (Chairman adds color at L19, L79, L121, L153, and possibly
L189; MD/Anmol Bansali is the primary respondent).

---

## 2. FULL TURN LEDGER (99 turns, sequential)

| Turn | Line | Speaker | First ~10 words | Flags |
|---|---|---|---|---|
| 1 | 5 | Operator | "Ladies and gentlemen, good day and welcome to Kulam International..." | — |
| 2 | 7 | Rahul Dhani (Monarch, host) | "Yeah, good afternoon everyone. Thank you Palak. On behalf..." | `PARTICIPANT_NAME_UNCLEAR` (Palak) |
| 3 | 9 | Management (opening remarks, unattributed by name) | "Thank you Rahul. Good afternoon everyone and welcome to..." | dense with mgmt numbers, see Sec.4 |
| 4 | 11 | Operator | "Thank you very much. We will now begin the question..." | intro's Doshi (round 1) |
| 5 | 13 | Analyst — Doshi | "Uh can you hear me?" | procedural question |
| 6 | 15 | Management | "Yes sir." | — |
| 7 | 17 | Analyst — Doshi | "Yeah thanks for the opportunity and congrats for the excellent..." | QUESTION 1 (order book YoY, Q2/Q3 demand, bracelet/necklace) |
| 8 | 19 | Management (Anmol Bansali + Chairman addition) | "Hi Mr. Jooshi Anmali here um I will take that..." | answer; Chairman's 40% growth driver comment embedded |
| 9 | 21 | Analyst — Doshi | "And uh you mentioned about Middle East and Israel. So..." | QUESTION 2 (follow-up: ME/Israel B2B number) |
| 10 | 23 | Management | "So close to outside US B2 B2B business is still..." | answer |
| 11 | 25 | Analyst — Doshi | "Okay. Uh now my second question is regarding uh you..." | QUESTION 3 (margin / other-income / IBIDA definition) |
| 12 | 27 | Management | "Sure. Um thanks for the question Mr. Dshi. So we..." | answer; mgmt numbers (24% steady-state margin, ~22cr tariff refund) |
| 13 | 29 | Analyst — Doshi | "Yeah, just one question on the origin and then short..." | QUESTION 4 (Origam new stores, franchise remodel, brand ambassador) |
| 14 | 31 | Management | "Sure. Thank you Mr. Doshi. So we have um signed..." | answer (7 new stores signed) |
| 15 | 33 | Analyst — Doshi | "All right. Thank you." | close |
| 16 | 35 | Management | "Thank you." | — |
| 17 | 37 | Operator | "Thank you sir. The next question is from the line..." | intro's Rathi |
| 18 | 39 | Analyst — Rathi | "Uh yeah, hi sir. Thanks for the opportunity. First of..." | QUESTION 5 (tariff refund: received in cash or accrual?) |
| 19 | 41 | Management | "Yes, Mr. Bali. The refund fully been received in cash..." | answer |
| 20 | 43 | Analyst — Rathi | "Okay. Okay. And one more question. So as more players..." | QUESTION 6 (LGD competitive intensity, Origam differentiation) |
| 21 | 45 | Management | "Uh yes. So uh you know great question. I think this..." | long answer |
| 22 | 47 | Operator | "Thank you sir. The next question is from the line..." | intro's Mukharji |
| 23 | 49 | Analyst — Mukharji | "Hello. Am I audible?" | procedural question |
| 24 | 51 | Management | "Yes sir." | — |
| 25 | 53 | Analyst — Mukharji | "Yeah. Uh uh so my first question is in the..." | QUESTION 7 (B2B realization/ASP increase driver) |
| 26 | 55 | Management | "Um thank you Mr. Mukhari. I it's a little hazy but..." | answer cuts off mid-sentence | `TRANSCRIPT_ARTIFACT` |
| 27 | 57 | Analyst ack + Management (continuation, no break) | "perfect perfect. So so that is defined by um..." | `MERGED_TURN` / `TRANSCRIPT_ARTIFACT` — analyst's "perfect perfect" spliced directly into mgmt's continued answer |
| 28 | 59 | Analyst — Mukharji | "Get that. Uh and sir uh like uh how are..." | QUESTION 8 (wholesale/retail LGD price trend) |
| 29 | 61 | Management | "Sure. Um so you know as mentioned mentioned even in..." | answer |
| 30 | 63 | Analyst — Mukharji | "Uh get that. Thanks for that uh perspective. Uh I'm..." | QUESTION 9 (Chinese CVD supply competition impact) |
| 31 | 65 | Management | "Sure. Sure. Mr. Mukhar G. So um it's a great..." | answer |
| 32 | 67 | Analyst question + Management answer, no break | "Uh good. But just a small followup uh uh the..." | `MERGED_TURN` / `TRANSCRIPT_ARTIFACT` — QUESTION 10 (does supply increase pressure wholesale pricing) spliced directly into mgmt's answer within same paragraph |
| 33 | 69 | Analyst — Mukharji | "Get that. And so my last question is on the..." | QUESTION 11 (2-3yr demand outlook, B2B & B2C) |
| 34 | 71 | Management | "Sure absolutely. So let's um just dividing that question into..." | long answer; mgmt number (FY26 exit ~1,000cr revenue); hands to Chairman |
| 35 | 73 | Management/Chairman | "Hello." | line check |
| 36 | 75 | Unclear (operator/analyst confirming) | "Yes sir." | — |
| 37 | 77 | Management (MD) | "Yes. Just requesting our chairman to add if any further..." | — |
| 38 | 79 | Management (Chairman) | "Longerterm growth trajectory. I believe that we are uh in..." | brief comment |
| 39 | 81 | Analyst — Mukharji | "Uh just a a small uh followup uh like will..." | QUESTION 12 (US vs non-US export share split) |
| 40 | 83 | Management | "Um sure of course. Uh as on FI 26 um on..." | answer; mgmt number (90-95% US share FY26); defers exact split to email |
| 41 | 85 | Analyst | "thank you." | close |
| 42 | 87 | Operator | "Thank you sir. The next question is on the line..." | intro's Ganani (round 1) |
| 43 | 89 | Analyst — Ganani | "Uh yes sir. Uh congratulations for a great set of..." | QUESTION 13 (LGD share of overall US jewelry market + industry growth rate) |
| 44 | 91 | Management | "Sure. Thank you Mr. Bat. Um we don't have industry..." | answer (LGD share 40-60% range, no industry reports) |
| 45 | 93 | Analyst — Ganani | "Okay. And what is the growth rate that the uh..." | QUESTION 14 (follow-up: clarifies industry growth, not company's) |
| 46 | 95 | Management | "Yes. Yes. So in the finished jewelry segment um labroom..." | answer (healthy double-digit industry growth) |
| 47 | 97 | Analyst — Ganani | "Okay. Okay. Okay. Uh and uh secondh what would be..." | QUESTION 15 (Goldium's own market share in US LGD market) |
| 48 | 99 | Management answer + Analyst clarifying question, no break | "Um yes Mr. Bat still very very small. Um you..." | `MERGED_TURN` / `TRANSCRIPT_ARTIFACT` — mgmt numbers (largest customer $6bn retail sales, $2-2.5bn wholesale addressable, Goldium ~$30-40mn = <2% share) followed immediately by QUESTION 16 (clarify: is the 40-60% LGD-penetration figure for the whole market or a segment?) spliced in |
| 49 | 101 | Management | "Uh yes Mr. Bat that's with the major retailers corporate..." | answer (clarifies: major/corporate retailers, upper-mid/premium price segment, excludes luxury) |
| 50 | 103 | Analyst | "Okay. Okay. Okay sir. Great. Thanks and all the best..." | close |
| 51 | 105 | Management | "Thank you Mr. Bat." | — |
| 52 | 107 | Operator | "Thank you sir. The next question is from the line..." | intro's Agarwal |
| 53 | 109 | Analyst — Agarwal | "Yeah I'm audible." | — |
| 54 | 111 | Management | "Yes sir." | — |
| 55 | 113 | Analyst — Agarwal | "Yeah. Uh can you share the or loss for origin..." | QUESTION 17 (Origam P&L / operating loss for the quarter) |
| 56 | 115 | Management answer + Analyst 2nd question, no break | "Um hi Mr. Agraal we'll be able to get back..." | `MERGED_TURN` / `TRANSCRIPT_ARTIFACT` — mgmt number (5-6cr Origam operating loss ballpark) followed by QUESTION 18 (pushback: low single-digit share with largest US retailers vs their 30-40% LGD growth — why isn't overall B2B growth faster) spliced in |
| 57 | 117 | Management | "Um sure sure Ankush so uh yes I think you know..." | long answer (bridal-first strategy; tennis bracelet/necklace fashion expansion rationale) |
| 58 | 119 | Analyst — Agarwal | "Correct. So I uh one of the comments few quarters..." | QUESTION 19 (bridal 85% / fashion 15% mix — pace of shift) |
| 59 | 121 | Management + Chairman addition | "Uh it it will always so the model that we..." | answer (1-yr testing cycle); Chairman adds context (last-year base 235cr, tariff-driven early shipment, 50% YoY growth) |
| 60 | 123 | Analyst — Agarwal | "Yeah, not complaining about the growth. The growth has been..." | QUESTION 20 (implicit/rhetorical: why isn't growth faster given execution & opportunity size) |
| 61 | 125 | Management | "yeah so we we don't want to put any forwardlooking..." | explicit hedge: "we don't want to put any forward-looking numbers straight away" |
| 62 | 127 | Analyst | "thank you sir" | close |
| 63 | 129 | Operator | "the next question is from the line of Kumar Sor..." | intro's Saurabh/Kumar (round 1) |
| 64 | 131 | Analyst — Saurabh | "uh hi thanks for for a great set of result..." | `MERGED_TURN` — QUESTION 21 (fashion segment: new clients or same end clients) + QUESTION 22 (Europe/UK/Germany B2B expansion plans) both asked in one continuous paragraph |
| 65 | 133 | Management (Europe answer) + Analyst (transition + Origam biz-model question) + Management (Origam answer), all no break | "Hi Mr. Sor. Uh yes so we have already new..." | `MERGED_TURN` / `TRANSCRIPT_ARTIFACT` (severe) — contains: answer to Q21 (same existing clients, different buyers); full answer to Q22 (Europe: medium-term goal, margin/product-profile constraints, nearer-term priority Australia/Canada/Israel/ME); analyst's "two questions on origin" transition plus QUESTION 23 (physical vs. digital vs. omnichannel model for Origam); and management's answer to Q23 — four distinct disclosure units compressed into one paragraph with zero blank-line breaks |
| 66 | 135 | Analyst — Saurabh | "Got it. Got it. And my last question is on..." | QUESTION 24 (2nd Origam question) explicitly deferred, asks to be re-queued — fulfilled later at Turn 91 (L185) |
| 67 | 137 | Management | "Sure." | ack |
| 68 | 139 | Analyst | "Thank you." | — |
| 69 | 141 | Management | "Thank you, sir." | — |
| 70 | 143 | Management/Operator (ambiguous) | "Thank you, sir." | — |
| 71 | 145 | Operator | "Ladies and gentlemen, in order to ensure that management is..." | reminds "one question per participant"; intro's Gautam |
| 72 | 147 | Analyst — Gautam | "Yeah. Am I audible? Yeah." | procedural question |
| 73 | 149 | Management ack + Analyst question, no break | "Yes sir. Now kudos on the date number sir. Uh..." | `MERGED_TURN` / `TRANSCRIPT_ARTIFACT` — QUESTION 25 (gross margin at 30%, lowest in 10 quarters; any new customer addition like Costco; Origam quarterly exit rate) spliced onto mgmt's "Yes sir" |
| 74 | 151 | Management | "Uh thank you Mr. Goautam. So I uh will have..." | answer; hedge — "will have to review... let me double check on those numbers and get back to you" re: own gross margin figure |
| 75 | 153 | Management (Chairman) | "Also, I would like to add that Costco doesn't do..." | addendum (Costco does not currently carry lab-grown diamonds) |
| 76 | 155 | Management | "Yes. So, as our chairman has mentioned, uh you know..." | continues Costco answer |
| 77 | 157 | Analyst — Gautam | "Okay. And the quarterly sales rate of the origins." | QUESTION 26 (Origam quarterly sales run-rate) — `REPEAT_QUESTION` (same metric essentially already disclosed at Turn 3/L9 as Rs 81.56mn Q1FY27 Origam revenue) |
| 78 | 159 | Management | "Uh so in the quarter we did about 8.1 8.2..." | answer: 8.1-8.2 cr (consistent with L9's 81.56mn figure) |
| 79 | 161 | Operator | "Thank you sir. The next question is on the line..." | intro's Doshi (round 2) |
| 80 | 163 | Analyst — Doshi | "Uh yeah, thanks for the opportunity again. So uh my..." | QUESTION 27 (Middle East/Israel/Australia model: wholesale vs retail, consignment vs order-book) |
| 81 | 165 | Management | "Um sure thank you. So it's It's uh it's a..." | answer |
| 82 | 167 | Analyst | "okay thank you." | close |
| 83 | 169 | Operator | "Thank you sir. The next question is on the line..." | intro's Ganani (round 2) |
| 84 | 171 | Analyst — Ganani | "Yes sir. Uh thanks for the followup. Uh just wanted..." | QUESTION 28 (US wholesale vs retail sales mix; online sales attributed to wholesalers or retailers) |
| 85 | 173 | Management | "So Mr. Bat So about um it varies quarter on..." | answer: 85-90% direct retail |
| 86 | 175 | Analyst — Ganani | "Okay. So 85 to 90% of the sales the retailers..." | QUESTION 29 (confirmation of figure) |
| 87 | 177 | Management | "Yes. Yes. Two of the US cities. Yes. Okay. Okay." | garbled confirmation |
| 88 | 179 | Analyst | "Okay. Uh fine, fine. Okay. Thanks a lot, sir. Thank..." | close |
| 89 | 181 | Management | "Thank you. Thank you, Mr." | cuts off |
| 90 | 183 | Operator | "Thank you, sir. The next question is from the line..." | intro's Saurabh/Kumar (round 2, "Sarup Kumar") |
| 91 | 185 | Analyst — Saurabh | "Yeah, I have uh one more pending question. I think..." | QUESTION 30 — fulfils the deferred Q24 (mature-store monthly run-rate vs peer benchmark of 10-11cr/store) |
| 92 | 187 | Management | "sure Mr. Sorab so great question we have um um..." | answer (store-level performance range, "25 to 30, 85 lakh"/month, unclear figure) |
| 93 | 189 | Management (Chairman?) | "One of the best stores has always crosses 40 45..." | addendum: best store 40-45 lakh/month |
| 94 | 191 | Analyst | "Okay, got it sir. Got it. Wish you all the..." | close |
| 95 | 193 | Management | "Thank you." | — |
| 96 | 195 | Unclear | "Thank you sir." | — |
| 97 | 197 | Unclear | "Thank you sir." | duplicate ack |
| 98 | 199 | Operator | "Ladies and gentlemen, In the interest of time, that was..." | last question closed; hands to management for closing comments |
| 99 | 201 | Management (closing) + Operator (sign-off), no break | "I I want to thank all the participants for joining..." | `MERGED_TURN` — management's closing thanks spliced directly into the operator's call-conclusion sign-off, no break |

---

## 3. QUESTIONS LEDGER (32 rows: 29 substantive + 3 procedural)

| Q# | Turn | Analyst | Firm | Topic | Flags |
|---|---|---|---|---|---|
| P1 | 5 | Doshi | Whitestone PMS | procedural — audio check | `PROCEDURAL` |
| 1 | 7 | Doshi | Whitestone PMS | order book YoY comparison, Q2/Q3 demand outlook, bracelet/necklace launch update | — |
| 2 | 9 | Doshi | Whitestone PMS | Middle East / Israel B2B revenue number (follow-up) | — |
| 3 | 11 | Doshi | Whitestone PMS | margin / other-income treatment / IBIDA definition, tariff-refund breakdown | — |
| 4 | 13 | Doshi | Whitestone PMS | Origam new store additions, franchise remodel, brand ambassador plans | — |
| 5 | 18 | Rathi | Dalal & Broacha Stock Broking | tariff refund: cash received or still to be realized | — |
| 6 | 20 | Rathi | Dalal & Broacha Stock Broking | LGD competitive intensity, how Origam differentiates | — |
| P2 | 23 | Mukharji | Prescient Capital | procedural — audio check | `PROCEDURAL` |
| 7 | 25 | Mukharji | Prescient Capital | B2B export realization/ASP increase driver | — |
| 8 | 28 | Mukharji | Prescient Capital | wholesale/retail LGD price trend in key markets | — |
| 9 | 30 | Mukharji | Prescient Capital | Chinese CVD-manufactured LGD supply competition impact | — |
| 10 | 32 | Mukharji | Prescient Capital | does increased LGD supply pressure wholesale jewelry pricing | `MERGED_TURN` source |
| 11 | 33 | Mukharji | Prescient Capital | 2-3 year demand outlook, B2B and B2C | — |
| 12 | 39 | Mukharji | Prescient Capital | US vs non-US export revenue share split | — |
| 13 | 43 | Ganani | Money Control Research | LGD share of overall US jewelry market + industry growth rate | — |
| 14 | 45 | Ganani | Money Control Research | clarifies: industry growth rate, not company's own growth | — |
| 15 | 47 | Ganani | Money Control Research | Goldium's own market share within the US LGD jewelry market | — |
| 16 | 48 | Ganani | Money Control Research | clarifies whether 40-60% LGD-penetration figure is market-wide or segment-specific | `MERGED_TURN` source |
| 17 | 55 | Agarwal | Search Capital | Origam profit/loss for the quarter | — |
| 18 | 56 | Agarwal | Search Capital | pushback: low single-digit share with largest US retailers vs their 30-40% LGD growth — why isn't overall B2B growth faster | `MERGED_TURN` source |
| 19 | 58 | Agarwal | Search Capital | bridal (85%) / fashion (15%) mix — pace of shift, medium-term | — |
| 20 | 60 | Agarwal | Search Capital | rhetorical/implicit: why isn't growth faster given execution and opportunity size | — |
| 21 | 64 | Saurabh/Kumar | Scientific Investing | fashion-segment expansion: same end clients or new client set | `MERGED_TURN` source (with Q22) |
| 22 | 64 | Saurabh/Kumar | Scientific Investing | plans to expand B2B into Europe (UK, Germany) | `MERGED_TURN` source (with Q21) |
| 23 | 65 | Saurabh/Kumar | Scientific Investing | Origam business model: physical, digital, or omnichannel | `MERGED_TURN`/`TRANSCRIPT_ARTIFACT` (severe) |
| 24 | 66 | Saurabh/Kumar | Scientific Investing | 2nd Origam question, explicitly deferred to a later turn | deferred; fulfilled at Turn 91 |
| P3 | 72 | Gautam | GS Investment | procedural — audio check | `PROCEDURAL` |
| 25 | 73 | Gautam | GS Investment | gross margin at 30% (lowest in 10 quarters); new customer additions incl. Costco; Origam quarterly exit rate | `MERGED_TURN` source |
| 26 | 77 | Gautam | GS Investment | Origam quarterly sales run-rate | `REPEAT_QUESTION` (already disclosed L9 as Rs 81.56mn) |
| 27 | 80 | Doshi | Whitestone PMS | Middle East/Israel/Australia go-to-market model: wholesale/retail, consignment vs order-book | — |
| 28 | 84 | Ganani | Money Control Research | US wholesale vs retail sales mix; online sales channel attribution | — |
| 29 | 86 | Ganani | Money Control Research | confirms 85-90% retail-direct figure | — |
| 30 | 91 | Saurabh/Kumar | Scientific Investing | mature-store monthly revenue run-rate vs peer benchmark (10-11 cr/store) | fulfils Q24 deferral |

`REPEAT_QUESTION` also applies loosely across the call to the "US vs non-US
export share" theme (asked at Q12/Turn 39 and revisited via Q27/Turn 80 and
Q28/Turn 84 from different angles) and to the Costco/new-customer theme
(Q25/Turn 73, answered and re-confirmed at Turns 74-76) — noted here rather
than as separate flagged rows since each instance targets a distinct sub-metric.

---

## 4. MANAGEMENT NUMBERS SPOKEN (27 rows, with turn number)

| # | Turn | Line | Number / metric |
|---|---|---|---|
| 1 | 3 | 9 | Total revenue Q1 FY27: Rs 3,637 million |
| 2 | 3 | 9 | EBITDA ("Zita") Q1 FY27: grew 120% YoY to Rs 1,039 million |
| 3 | 3 | 9 | Steady-state EBITDA margin post tariff-refund calibration: +400bps to 24% |
| 4 | 3 | 9 | PAT Q1 FY27: more than doubled to Rs 740 million |
| 5 | 3 | 9 | LGD jewelry export mix: 90.7% of export sales (vs 87.8% Q1 FY26) |
| 6 | 3 | 9 | Online revenue: 19.3% of Q1 FY27 revenue |
| 7 | 3 | 9 | ~64% of finished-jewelry inventory (as of 30 June 2026) is held with customers |
| 8 | 3 | 9 | Order book as of 30 June 2026: ~Rs 2,250 million |
| 9 | 3 | 9 | Cash & cash equivalents incl. investments: Rs 4,566.7 million |
| 10 | 3 | 9 | Bonus issue: 3,76,39,281 equity shares of Rs 2 each, 1:3 ratio, utilizing ~Rs 7.53 cr (transcribed "7 cr 527 562") |
| 11 | 3 | 9 | Origam: 26 operational stores as of date |
| 12 | 3 | 9 | Origam Q1 FY27 revenue: Rs 81.56 million |
| 13 | 12 | 27 | Tariff/duty refund within other income: ~Rs 22 crore |
| 14 | 12 | 27 | Steady-state IBIDA margin restated: 24% (repeat of #3) |
| 15 | 14 | 31 | 7 new Origam stores signed, targeted to open before Diwali |
| 16 | 34 | 71 | FY26 exit revenue: ~Rs 1,000 crore (B2B, record year) |
| 17 | 34 | 71 | Origam long-term store target: ~100 stores |
| 18 | 40 | 83 | FY26 US export share: 90-95%, balance non-US |
| 19 | 44 | 91 | LGD penetration among addressable major US retailers: 40-60% range |
| 20 | 48 | 99 | Largest US customer: ~$6 billion total retail sales |
| 21 | 48 | 99 | Same customer's addressable wholesale purchase value (LGD segment): ~$2-2.5 billion |
| 22 | 48 | 99 | Goldium's annual sales to that customer: ~$30-40 million (<2% share) |
| 23 | 56 | 115 | Origam operating loss for the quarter: ballpark Rs 5-6 crore |
| 24 | 59 | 121 | Prior-year comparable-quarter revenue base: Rs 235 crore; this year's growth over that base: 50% |
| 25 | 78 | 159 | Origam Q1 FY27 quarterly sales: Rs 8.1-8.2 crore (consistent with #12) |
| 26 | 85 | 173 | US sales mix: 85-90% direct retail, balance wholesale |
| 27 | 93 | 189 | Best-performing Origam store: 40-45 lakh/month sales |

Note: turn 92 (line 187) contains a further store-performance figure
transcribed as "25 to 30, 85 lakh" per store per month — kept out of the
numbered table above because the OCR/transcription garble leaves the exact
value ambiguous (could be "25 to 30 lakh" and a separate "85 lakh" reference,
or a single garbled figure); flagged `NUMBER_AMBIGUOUS` for A3/A4 to resolve
against the audio source if available, not silently dropped.

Analyst-spoken numbers used as question context (not management disclosures,
kept out of the management table but noted for the Role 5 arithmetic-consistency
check): order book cited by Doshi at Turn 7 as "225K this June-end vs 140K a
year ago" (units unstated, presumably Rs lakh or a shorthand for crore — cross-
check against management's Rs 2,250 million order-book figure at Turn 3);
gross margin cited by Gautam at Turn 73 as "30% this quarter, lowest in 10
quarters" (management disputes this at Turn 74 without giving its own number,
promising to follow up — `INDETERMINATE`, not resolved on this call).

---

## 5. FORWARD-COMMITMENT AND HEDGE PHRASES (19 rows, with turn number)

| # | Turn | Type | Phrase (paraphrase/fragment) |
|---|---|---|---|
| 1 | 8 | forward-commitment | "we are looking forward to a robust Q2 Q3... we hope to continue the growth" |
| 2 | 8 | forward-commitment | "it will be our endeavor to provide further stronger presence for Goldium... in US and globally" |
| 3 | 10 | forward-commitment | "we hope to increase that number... we'll have double digit growth in non-American areas as well" |
| 4 | 12 | forward-commitment | "we hope to maintain and continue this margin profile as FY27..." |
| 5 | 12 | hedge | "even if you keep consistent over the quarters you will see..." (qualifying the ex-tariff-refund margin claim) |
| 6 | 14 | forward-commitment | "target is to get them open before [Diwali]" (7 new stores) |
| 7 | 21 | forward-commitment | "will play out in the longer term... we believe we would be in a great position" |
| 8 | 26 | hedge | "it's a little hazy but I believe your question is..." (management uncertain of what was asked) |
| 9 | 34 | forward-commitment | "we hope to continue on this path... over the next two to three years drive a business... amongst the largest jewelry exporters" |
| 10 | 40 | hedge/deferral | "I'll be able to provide the exact number on email" (US/non-US split) |
| 11 | 56 | hedge/deferral | "we'll be able to get back to you on that... ballpark figure" (Origam P&L) |
| 12 | 57 | forward-commitment | "we hope over Q2 certainly over Q3 that we will be able to introduce this category" (tennis bracelet/necklace fashion line) |
| 13 | 61 | hedge (explicit) | "we don't want to put any forward-looking numbers straight away but we are positive for the growth" |
| 14 | 65 | forward-commitment | "over the medium term we would love to add on certain revenue coming from these geographies [Europe]" |
| 15 | 65 | forward-commitment | "this fiscal year we hope to see... deepening of presence in Australia... Canada... Israel and Middle East" |
| 16 | 66 | forward-commitment | "I do believe... over the coming fiscal year... we will slowly increase a digital spend" (Origam) |
| 17 | 74 | hedge | "I will have to review to the best of my knowledge... let me again double check on those numbers and get back to you" (own gross margin figure) |
| 18 | 74 | hedge | "significantly higher than previous quarters but let me again double check" |
| 19 | 92 | hedge | "mixed... it's been about a year plus, little bit over a year" (store maturity, imprecise timeframe) |

---

## 6. FLAGS SUMMARY

- `TRANSCRIPT_ARTIFACT` / `MERGED_TURN`: Turns 27, 32, 48, 56, 64-65 (compound),
  73, 99 — paragraphs that splice two or more speakers' material with no
  blank-line break. Turn 65 (line 133) is the most severe: it compresses a
  full management answer, an analyst's two-question transition, and a second
  management answer into one paragraph.
- `PARTICIPANT_NAME_UNCLEAR`: operator possibly named "Palak" (single mention,
  line 7), spelling and role not independently confirmable from the text.
- `NAME_GARBLED`: analyst names transcribed inconsistently across their two
  appearances (Doshi: "Zikit Dshi"/"Dshit Doshi"; Ganani: "Bat Ganani"/"of
  Bharat Ganani"; Saurabh: "Kumar Sor"/"Sarup Kumar"; Rathi: "Aam B. Rali";
  Gautam: "Vive Gotham").
- `REPEAT_QUESTION`: Origam quarterly revenue/run-rate asked and answered
  twice (opening remarks L9 = Rs 81.56mn; Q26/Turn 77 = Rs 8.1-8.2cr, same
  figure restated).
- `NUMBER_AMBIGUOUS`: Turn 92 (line 187) store-performance figure "25 to 30,
  85 lakh" — exact value not resolvable from the text alone.
- `INDETERMINATE`: gross margin figure disputed at Turn 73/74 (analyst cites
  30%, lowest in 10 quarters; management disputes without giving its own
  number, defers to follow-up) — not resolved within this transcript.
- `MGMT_ABSENCE`: not triggered — Chairman and MD both present and both heard.
