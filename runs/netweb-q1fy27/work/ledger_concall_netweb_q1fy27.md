# LEDGER — Netweb Technologies (NETWEB), Q1 FY27, Concall Transcript
Source: /home/user/inflection-pipeline/runs/netweb-q1fy27/work/extract_concall_netweb_q1fy27.txt
(A1 extract; transcript body = extract lines 30-304, verbatim, 137 blank lines marking turn boundaries)

```
=== A2 COUNT TEST ===
category: turns                  grep_count: 138  sweep_count: 138  match: yes
  method — grep: `awk 'NR>=30 && NR<=304 && NF>0'` on extract (non-blank lines
  between transcript-body-begins and transcript-body-ends markers, each
  bounded by the 137 blank-line separators the header attests to).
  method — sweep: manual walk of every paragraph line 30,32,34,...,304
  (step 2), assigning speaker to each. Counts agree.

category: questions (Q&A exchange markers)   grep_count: 12  sweep_count: 13  match: no (FIRST PASS)
  method — grep pass 1: `grep -niE "next question is from the line|first
  question is from the line"` -> 12 hits (lines 40,60,80,92,118,142,172,
  204,258,266,280,292).
  method — sweep pass 1: manual read of full transcript found a 13th
  question-introduction turn at line 186 ("Thank you. The next question
  is from the of Mani Mir Singh Sati from Sati Capitals ... Singhi please
  go ahead.") — the marker is malformed (missing the word "line"), so the
  strict grep pattern silently missed it. GATE A2 MISMATCH -> RESWEEP.

category: questions (Q&A exchange markers)   grep_count: 13  sweep_count: 13  match: yes (RESWEEP, FINAL)
  method — grep pass 2 (broadened): `grep -niE "next question is from
  the|first question is from the line"` -> 13 hits (adds line 186).
  method — sweep pass 2: confirms 13 distinct question-introduction turns,
  12 distinct analysts (Jatin Kalra of Bank of America is re-introduced
  as a follow-up questioner at line 258). Counts agree. Flag:
  MALFORMED_MARKER (line 186) — logged as the reason pass 1 undercounted.

category: participants            grep_count: 19  sweep_count: 19  match: yes
  method — grep: distinct name+firm pairs at the 13 question markers,
  deduped for the repeat questioner (Jatin Kalra) = 12 analysts; plus
  distinct named/titled roles in the intro turn (line 32) and IR/operator
  turns = 7 management/host-side participants (CMD, full-time director,
  CFO, CSSO, IR adviser, ICICI Securities moderator, conference operator).
  method — sweep: independent manual list of every named or titled
  individual across all 138 turns = 19. Counts agree.

category: mgmt_numbers (canonical, from task's named-figure list)  grep_count: 23  sweep_count: 23  match: yes
  method — grep: pattern search for each of the 23 named figures/ratios
  in the injected input list (8,197 / 853 / 48.2 / 44.6 / 43.9 / 96 days /
  86->78 / 86->110 / 1,999 / 25,069.35 (or "25,69.35" as garbled) /
  8,480.47 / ~104,100 (or garbled variants) / 5,105.70 (or "5,15.70") /
  62% / 484% / 1,252.94 / 1,353.46 / 1,600 cr & 430 cr / 1,200 cr / 125
  people / 8-12->16-20 weeks / 60% & 18-24 months / 38% CAGR / 4-5%
  exports) = all 23 found spoken on the call.
  method — sweep: manual read confirms the same 23, each anchored to a
  turn number below (Table 4). Counts agree. A broader sweep-only
  supplementary count of every additional number/repeat mention (not
  independently grep-verifiable as one line item each) = 26 more rows,
  disclosed in Table 4 but not part of this GATE A2 canonical count.

gate_a2: pass
=== END COUNT TEST ===
```

---

## TABLE 1 — PARTICIPANTS (19)

| # | Name (as transcribed) | Role / Firm | First appears (line) | Flags |
|---|---|---|---|---|
| 1 | Unnamed conference operator | Call operator, ICICI Securities-hosted line | 30 | |
| 2 | Ms. Siman Nay ("Shima"/"Sema"/"Simma") | ICICI Securities Limited — call host/moderator | 30 | NAME_GARBLED |
| 3 | Mr. Sanji / "Sanjie" (Sanjay Sanji?) | IR Adviser, "Yotus Advisers" (name as transcribed) | 32 | NAME_GARBLED |
| 4 | Mr. Sanjay Lodha | CMD | 32 | |
| 5 | Mr. Navin Lodha | Full-time Director | 32 | MGMT_ABSENCE — introduced, never individually attributable to a turn in this transcript |
| 6 | Mr. Ankit Kumar Singh | CFO | 32 | |
| 7 | Mr. Sidar Vikram (Siddharth Vikram?) | Chief Sales and Strategy Officer | 32 | MGMT_ABSENCE — introduced, never individually attributable to a turn |
| 8 | Reu Bet (name as transcribed) | Analyst, IIFL Capital | 40 | NAME_GARBLED |
| 9 | DH Meta (Dhaval Mehta?) | Analyst, Invesco India Mutual Fund | 60 | NAME_GARBLED |
| 10 | Jatin Kalra | Analyst, Bank of America | 80, 258 | asks a first round and a follow-up round |
| 11 | Sepa (name as transcribed) | Analyst, Equirus Securities | 92 | NAME_GARBLED |
| 12 | Vine (name as transcribed) | Analyst, Mun Capital | 118 | NAME_GARBLED |
| 13 | Rohit | Analyst, CLSA | 142 | |
| 14 | Akshai | Analyst, AK Investments | 172 | |
| 15 | Mani Mir Singh Sati / "Singhi" | Analyst, Sati Capitals | 186 | NAME_GARBLED, MALFORMED_MARKER |
| 16 | Omar | Analyst, Shri Investments | 204 | |
| 17 | Ja Lakshmi Gupta | Analyst, The Wealth Company | 266 | NAME_GARBLED |
| 18 | Anoj Kashab (Anuj Kashyap?) | Analyst, A3 Capital | 280 | NAME_GARBLED |
| 19 | Sarab Sadhuani / "Sorup Sahadwani" | Analyst, Sahasra Capital (transcribed "Sahasur") | 292 | NAME_GARBLED — two different renderings of one name in the same line |

---

## TABLE 2 — SPEAKER TURNS (138, sequential, line = extract line number)

| Turn | Line | Speaker (attribution) | First ~10 words | Flags |
|---|---|---|---|---|
| 1 | 30 | Operator | Ladies and gentlemen, good day and welcome to Net Web | |
| 2 | 32 | ICICI Securities moderator ("Shima") | Thank you. Good afternoon everyone. On behalf of ICIC Security, | introduces all 4 named mgmt + IR adviser |
| 3 | 34 | IR Adviser ("Sanji") | Thank you Shima. Good afternoon to all the participants. Before | safe harbor statement |
| 4 | 36 | CMD Sanjay Lodha | Thank you Sema and Sanjie. Good afternoon and a very | opening remarks; see Table 4 rows 1-13 |
| 5 | 38 | CFO Ankit Kumar Singh | Thank you, Mr. Loa. Good afternoon, ladies and gentlemen, and | financial overview; see Table 4 rows 14-28 |
| 6 | 40 | Operator | Thank you very much. We will now begin the question | Q&A opens; introduces analyst #8 (Reu Bet, IIFL Capital) |
| 7 | 42 | Analyst Reu Bet (IIFL Capital) | Yeah. Hi uh good afternoon team. Uh so my first | Q1 of exchange 1 |
| 8 | 44 | Mgmt (Sanjay Lodha) | So basically thank you for your question actually you you | A1 |
| 9 | 46 | Analyst Reu Bet | and sir to support this kind of growth uh do | Q2 (capex/capacity) |
| 10 | 48 | Mgmt (Sanjay Lodha) | Reu you know that basically we are a primarily not | A2 |
| 11 | 50 | Analyst Reu Bet | sure uh so secondly if you look on the working | Q3 (working capital) |
| 12 | 52 | Mgmt (CFO, self-ID as "Sanjit"/attribution uncertain) | so so reu thanks for this I'll take that this | A3; ATTRIBUTION_AMBIGUOUS |
| 13 | 54 | Analyst Reu Bet | Sure. Um thank you sir. I have one more question | Q4 (competitive landscape) |
| 14 | 56 | Mgmt (Sanjay Lodha) | So basically on the competition numbers speak actually really speaking | A4 |
| 15 | 58 | Analyst Reu Bet | Thank you. | closes exchange 1 |
| 16 | 60 | Operator | Thank you. The next question is from the line of | introduces analyst #9 (DH Meta, Invesco India MF) |
| 17 | 62 | Analyst DH Meta | Uh thanks for taking my question. Uh so can you | Q1 |
| 18 | 64 | Mgmt | Okay we'll wait for your second question and then answer | deferral |
| 19 | 66 | Analyst DH Meta | Okay. And uh so if I'm not wrong, this quarter | Q2 (margins) |
| 20 | 68 | Mgmt (attribution uncertain — CFO likely) | I will take the first one first. Uh so if | A1; ATTRIBUTION_AMBIGUOUS |
| 21 | 70 | Mgmt (Sanjay Lodha) | yes question basically on the margin front basically I will | A2; contains ARITHMETIC_FLAG figure ("growing at 90%") |
| 22 | 72 | Analyst DH Meta | okay Fred uh so ju just uh I think in | follow-up (like-to-like comparison) |
| 23 | 74 | Mgmt | I think it's probably not last year last quarter | short; ATTRIBUTION_AMBIGUOUS |
| 24 | 76 | Mgmt | last quarters he have not he not given the pipeline | answer (prior pipeline ex-strategic) |
| 25 | 78 | Analyst DH Meta | Okay. Thank you. | closes exchange 2 |
| 26 | 80 | Operator | Thank you. The next question is from the line of | introduces analyst #10 (Jatin Kalra, BofA) |
| 27 | 82 | Analyst Jatin Kalra | Uh hi. Uh uh thank you for taking my question. | Q1 + preview of Q2 |
| 28 | 84 | Mgmt (Sanjay Lodha) + Analyst Jatin Kalra | yes so basically I'd like to tell you one thing | MERGED_TURN — A1 and analyst's Q2 run together with no transcript break |
| 29 | 86 | Mgmt (Sanjay Lodha) | So basically on specific deals I will not like to | A2 |
| 30 | 88 | Analyst Jatin Kalra | Understood. Uh that's really helpful. Uh thank you so much | closes round 1 of exchange 3 |
| 31 | 90 | Operator/transition | Thank you. | |
| 32 | 92 | Operator | Thank you. The next question is from the line of | introduces analyst #11 (Sepa, Equirus Securities) |
| 33 | 94 | Analyst Sepa | Yeah, thanks. Thanks for the opportunity and congratulations to the | Q1 (conversion timeline w/ strategic orders) |
| 34 | 96 | Mgmt (Sanjay Lodha) | Thank you SP G. Basically your question is very relevant. | A1 |
| 35 | 98 | Analyst Sepa | Okay. And uh sir, even in this year with robust | Q2 (1H contribution) |
| 36 | 100 | Mgmt (Sanjay Lodha, deferring) | I think yeah you answer it. | short deferral to CFO |
| 37 | 102 | Mgmt (Ankit Singh, CFO) | So Sanjep slightly difficult to say because you know we | A2 |
| 38 | 104 | Analyst Sepa | Okay. Okay. And looking at the raw material prices and | Q3 (inventory days) |
| 39 | 106 | Mgmt (Ankit Singh) | So u uh Sep uh on the inventory days the | A3 |
| 40 | 108 | Analyst Sepa | okay fair enough And just the last question uh globally | Q4 (Chinese open-source models) |
| 41 | 110 | Mgmt (attribution uncertain) | thanks for the question. So basically I tell you that | A4; ATTRIBUTION_AMBIGUOUS |
| 42 | 112 | Analyst Sepa | Okay. Okay. And the last question if I can squeeze | Q5 (AI demand, two legs CSP+govt) |
| 43 | 114 | Mgmt | I think as of now we can only say that | A5 |
| 44 | 116 | Analyst Sepa | Okay. Thanks and all the best. | closes exchange 4 |
| 45 | 118 | Operator | Thank you. The next question is from the line of | introduces analyst #12 (Vine, Mun Capital) |
| 46 | 120 | Analyst Vine | Hi. Thank you for the opportunity and congratulations on a | Q1 (execution cycle weeks) |
| 47 | 122 | Mgmt (Sanjay Lodha) | So basically 8 to 12 weeks was earlier now we | A1 |
| 48 | 124 | Analyst Vine | Okay. Okay. That that is very helpful and this R&D | Q2 (physical AI/quantum R&D spend %) |
| 49 | 126 | Mgmt (Sanjay Lodha, short) | These are not guiding on revenue at all or these | short |
| 50 | 128 | Mgmt | So basically your primary question was this only that when | A2 |
| 51 | 130 | Analyst Vine | Okay. Okay. My question is more about what kind of | follow-up (R&D cost) |
| 52 | 132 | Mgmt | so basically we are not quantifying it actually V the | A (125-person R&D team) |
| 53 | 134 | Analyst Vine | Okay. And one last thing is are you working with | Q3 (Indian LLM companies) |
| 54 | 136 | Mgmt (Sanjay Lodha) | So the good part is that some of the largest | A3 |
| 55 | 138 | Analyst Vine | okay thank you so much thank you | closes exchange 5 |
| 56 | 140 | Mgmt/Operator (short) | thank you thank you for all | |
| 57 | 142 | Operator | Thank you. Next question is from the line of Rohit | introduces analyst #13 (Rohit, CLSA) |
| 58 | 144 | Analyst Rohit | Uh hi, thank you sir. Uh I actually had a | Q1 (component inflation/margins/WC) |
| 59 | 146 | Mgmt (Sanjay Lodha) | So basically as regards I cannot say that that these | A1 |
| 60 | 148 | Mgmt (continuation, likely Ankit Singh) | and along with this there is also a shortage shocks | A1 cont'd (inventory rationale); ATTRIBUTION_AMBIGUOUS |
| 61 | 150 | Analyst Rohit | Right. So quick clarification uh with respect to given how | follow-up (price pass-through) |
| 62 | 152 | Mgmt (Ankit Singh) | Um yeah Rohit I think we've answered this a couple | A2 |
| 63 | 154 | Mgmt (short) | I hope this clarifies | |
| 64 | 156 | Mgmt (Sanjay Lodha) | and plus basically you might have seen our margins are | A2 cont'd |
| 65 | 158 | Analyst Rohit | So that's actually very commendable because it actually shows it's | reaction/comment |
| 66 | 160 | Mgmt (Sanjay Lodha) | Yeah but basically I would like to again clarify that | clarifies no overcharging |
| 67 | 162 | Mgmt (continuation) | Yeah. Yeah. Because every every order every quarter margin cannot | continued |
| 68 | 164 | Analyst Rohit | Right. And maybe um uh another question in terms of | Q2 (component availability risk) |
| 69 | 166 | Mgmt (Sanjay Lodha) | Actually people have got used to this scarcity actually really | A2 |
| 70 | 168 | Analyst Rohit | Uh got it. Uh thanks a lot. Uh that's all | closes exchange 6 |
| 71 | 170 | Operator/Mgmt (short) | Thank you sir. | |
| 72 | 172 | Operator | Thank you. The next question is from the line of | introduces analyst #14 (Akshai, AK Investments) |
| 73 | 174 | Analyst Akshai | Uh hi s first of all congratulations on the great | Q1 (1,200 cr QIP rationale) |
| 74 | 176 | Mgmt (Sanjay Lodha/CMD) | No, I I don't know where you got this news | A1 (denies QIP; enabling resolution, 12-month validity) |
| 75 | 178 | Analyst Akshai | Okay, understood. Fair enough. And sir, my second question is | Q2 (physical AI/quantum timeline) |
| 76 | 180 | Mgmt | So see uh thanks for the question first. So as | A2 |
| 77 | 182 | Analyst Akshai | Okay. Fair enough and all the best. | closes exchange 7 |
| 78 | 184 | Operator | Thank you. | |
| 79 | 186 | Operator | Thank you. The next question is from the of Mani | introduces analyst #15 (Mani Mir Singh Sati/"Singhi", Sati Capitals); MALFORMED_MARKER |
| 80 | 188 | Analyst | Hello. | |
| 81 | 190 | Operator/Mgmt | Yeah. Hi man. | |
| 82 | 192 | Analyst | Yeah man. | |
| 83 | 194 | Analyst | Hello sir. So uh in last in May call there | Q1 (1,600 cr strategic order consumption) |
| 84 | 196 | Mgmt | So, so out of that 1,600 cr strategy order close | A1 (430 cr executed) |
| 85 | 198 | Analyst | Okay. And my second question is resp uh with regard | Q2 (1,200 cr fundraising, more to come?) |
| 86 | 200 | Mgmt | uh I no no no so first of all we | A2 (no raise yet; ZERO_STANDING) |
| 87 | 202 | Analyst | Okay. Okay. Thank you sir. That's all from my | closes exchange 8 |
| 88 | 204 | Operator | Thank you. The next question is from the line of | introduces analyst #16 (Omar, Shri Investments) |
| 89 | 206 | Analyst Omar | So just one one clarification first question. Uh you said | Q1 (why enabling resolution) |
| 90 | 208 | Mgmt | Yeah. So I told that I gave that answer. Uh | A1 |
| 91 | 210 | Analyst Omar | Yes. Please go ahead. Yeah, that's it. | interjection |
| 92 | 212 | Analyst Omar | Yeah. But uh is it for additional capacity expansions because | follow-up |
| 93 | 214 | Mgmt (short, interrupted) | Yeah. It is for | |
| 94 | 216 | Mgmt | Yeah. So this is for growth capital for we will | A (working capital for growth) |
| 95 | 218 | Analyst Omar | So this is for working capital right? If If you | clarifying |
| 96 | 220 | Mgmt | if you raise anything before working capital, you're right. | |
| 97 | 222 | Analyst Omar | And not for any uh M&A or something like that. | |
| 98 | 224 | Mgmt | No, no, no, not at all. Not at all. Absolutely | denies M&A use |
| 99 | 226 | Analyst Omar | So, so this is only for working capital if and | |
| 100 | 228 | Mgmt | Yeah. We will argue for working capital. No, M&A. Absolutely. | |
| 101 | 230 | Analyst Omar | Okay. And like uh for the next uh I I | Q (strategic order fading, growth trajectory) |
| 102 | 232 | Mgmt | I don't think we have guided any strategic order separately | A ("strategic is the new normal") |
| 103 | 234 | Analyst Omar | and like for how much period do you think that | follow-up |
| 104 | 236 | Mgmt | That's a very different question. I mean we can tell | A (pipeline/order book serves 2 years) |
| 105 | 238 | Mgmt (continuation) | So this strategic orders you are saying They are the | reasserts new-normal framing |
| 106 | 240 | Analyst Omar | No, I'm asking just that. | |
| 107 | 242 | Mgmt | You're asking. | |
| 108 | 244 | Analyst Omar | So these are the new orders, right? | |
| 109 | 246 | Mgmt | You're asking what you already answered. | |
| 110 | 248 | Analyst Omar | Okay. And given the government's also focus on this, how | Q (sector growth outlook) |
| 111 | 250 | Mgmt | I think we have put up that's why we specifically | A (38% CAGR, 3-4 yrs, national level) |
| 112 | 252 | Analyst Omar | This 38% CH for next four years you are saying | clarifying (entire category or AI only?) |
| 113 | 254 | Mgmt | it's for the AI for product line only for the | A (AI product line only) |
| 114 | 256 | Analyst Omar | Uh just finally if you can answer like currently everything | cut off, interrupted by operator |
| 115 | 258 | Operator | Sorry to interrupt Mr. Mr. Sorry to interrupt. Uh, may | cuts off Omar; re-introduces analyst #10 (Jatin Kalra) for follow-up |
| 116 | 260 | Analyst Jatin Kalra (follow-up round) | Uh, hi. Uh, thanks for the followup. Uh, this one | Q (R&D expensing vs. capitalizing) |
| 117 | 262 | Mgmt (Ankit Singh, CFO) | Yeah so Jatin uh as you know that we have | A |
| 118 | 264 | Analyst Jatin Kalra | Uh perfect. That is really clear. Uh thank you so | closes exchange 3 round 2 |
| 119 | 266 | Operator | Thank you. The next question is from the line of | introduces analyst #17 (Ja Lakshmi Gupta, The Wealth Company) |
| 120 | 268 | Analyst Ja Lakshmi Gupta | Uh hi sir. Thank you for taking my question and | Q1+Q2 (restatement + pipeline conversion timeline) |
| 121 | 270 | Mgmt (Ankit Singh) | On the first question regarding the balance, yeah, regarding the | A1 (inventory FIFO -> weighted average restatement); ACCOUNTING_POLICY_CHANGE |
| 122 | 272 | Mgmt (Sanjay Lodha) | your second part is basically uh the I already answered | A2 (60% / 18-24 months, repeat) |
| 123 | 274 | Analyst + Mgmt | Uh so and lastly can you give a broad break | MERGED_TURN — follow-up Q (funnel breakup by AI/HPC/cloud) and mgmt's declining-to-disclose answer run together with no break |
| 124 | 276 | Analyst | thank you thank you so much | closes exchange 9 |
| 125 | 278 | Mgmt/Operator | thank you | |
| 126 | 280 | Operator | Thank you. The next question is from the line of | introduces analyst #18 (Anoj Kashab, A3 Capital) |
| 127 | 282 | Analyst Anoj Kashab | good afternoon sir uh thank you for the opportunity uh | Q (data sovereignty/SLMs, forward-looking) |
| 128 | 284 | Mgmt | so whatever you are saying is music to our ears | A (declines further comment) |
| 129 | 286 | Analyst Anoj Kashab | and s last time sir uh you tell He told | follow-up (exports 4-5%) |
| 130 | 288 | Mgmt (Sanjay Lodha) | the domestic demand is phenomenal actually okay and so first | A (not focusing on exports) |
| 131 | 290 | Analyst Anoj Kashab | Thank you sir. Best of luck for the future. Thank | closes exchange 10 |
| 132 | 292 | Operator | Thank you. The next question is from the line of | introduces analyst #19 (Sarab Sadhuani, Sahasra Capital) |
| 133 | 294 | Analyst Sarab Sadhuani | Hello I'm sorry I was speaking on mute. Good afternoon | Q (Ethernet switch portfolio, bandwidth, Nvidia spectrum) |
| 134 | 296 | Mgmt (Sanjay Lodha) | so basically as uh we as as you know the | A (not selling boxes; DB300/B300) |
| 135 | 298 | Analyst Sarab Sadhuani | Okay sir. Uh thank you. Thank you so much | closes exchange 11 (last question) |
| 136 | 300 | Operator | ladies and gentlemen. We will take that as the last | closes Q&A, hands to IR adviser |
| 137 | 302 | IR Adviser ("Sanji") | Um thanks uh thanks a lot uh everybody for taking | closing remarks |
| 138 | 304 | Operator (ICICI Securities) | On behalf of ICIC Securities Limited that concludes this conference. | final sign-off |

---

## TABLE 3 — Q&A EXCHANGES (13 question-introduction markers, 12 distinct analysts)

| Exch. | Marker line | Analyst | Firm | Turns spanned (lines) | Sub-questions in exchange | Flags |
|---|---|---|---|---|---|---|
| 1 | 40 | Reu Bet | IIFL Capital | 42-58 | Q1 order book/AI mix/ticket size; Q2 capex/capacity; Q3 working-capital funding; Q4 competitive landscape | |
| 2 | 60 | DH Meta | Invesco India Mutual Fund | 62-78 | Q1 strategic order like-to-like comparison; Q2 margin resilience | |
| 3a | 80 | Jatin Kalra | Bank of America | 82-88 | Q1 pipeline breakup govt/private/cloud + conversion 55-60%/18-24mo; Q2 OEM route vs box sellers | MERGED_TURN at 84 |
| 4 | 92 | Sepa | Equirus Securities | 94-116 | Q1 conversion timeline w/ strategic orders; Q2 1H revenue contribution; Q3 inventory days outlook; Q4 Chinese open-source model risk; Q5 AI demand two legs (CSP+govt) | REPEAT_QUESTION (conversion 60%/18-24mo, also asked in exch. 3a, 9) |
| 5 | 118 | Vine | Mun Capital | 120-138 | Q1 execution-cycle weeks; Q2 physical AI/quantum R&D spend; Q3 Indian LLM partnerships | |
| 6 | 142 | Rohit | CLSA | 144-168 | Q1 component inflation/margin/WC impact + price pass-through; Q2 component-availability execution risk | |
| 7 | 172 | Akshai | AK Investments | 174-182 | Q1 1,200cr QIP rationale; Q2 physical AI/quantum timeline | REPEAT_QUESTION (1,200cr capital raise, also asked in exch. 8, 8b) |
| 8 | 186 | Mani Mir Singh Sati / "Singhi" | Sati Capitals | 188-202 | Q1 1,600cr strategic order consumption; Q2 1,200cr fundraising follow-on | MALFORMED_MARKER, REPEAT_QUESTION |
| 9 | 204 | Omar | Shri Investments | 206-256 | Q1 rationale for enabling resolution (extended back-and-forth); Q2 strategic-order fade/growth trajectory; Q3 sector CAGR outlook; Q4 (cut off) | REPEAT_QUESTION (enabling-resolution purpose, also exch. 7,8) |
| 3b | 258 | Jatin Kalra (follow-up) | Bank of America | 260-264 | Q (R&D expense vs. capitalize) | follow-up round, re-introduced explicitly by operator |
| 10 | 266 | Ja Lakshmi Gupta | The Wealth Company | 268-278 | Q1 balance-sheet restatement (inventory policy); Q2 pipeline conversion by FY27/FY28; Q3 funnel breakup AI/HPC/cloud | MERGED_TURN at 274; REPEAT_QUESTION (conversion 60%/18-24mo) |
| 11 | 280 | Anoj Kashab | A3 Capital | 282-290 | Q1 data sovereignty/SLM outlook; Q2 exports 4-5% outlook | |
| 12 | 292 | Sarab Sadhuani / "Sorup Sahadwani" | Sahasra Capital | 294-298 | Q (Ethernet switch portfolio, bandwidth, Nvidia spectrum) | last question of the call |

---

## TABLE 4 — QUANTIFIED FIGURES (turn-anchored; management figures = canonical 23 + 26 supplementary/repeat; analyst-cited figures flagged separately)

| # | Turn(line) | Speaker | Figure | Value as spoken | Flags |
|---|---|---|---|---|---|
| 1 | 4(36) | CMD | Revenue from operations, Q1FY27 | Rs 8,197 Mn | |
| 2 | 4(36) | CMD | Revenue YoY growth | 172.1% | |
| 3 | 4(36) | CMD | PAT | Rs 853 Mn | |
| 4 | 4(36) | CMD | PAT YoY growth | 179.9% | |
| 5 | 4(36) | CMD | PAT margin | 10.3% | |
| 6 | 4(36) | CMD | AI segment revenue | Rs 5,105.70 Mn (transcribed "5,15.70") | TRANSCRIPTION_GARBLED |
| 7 | 4(36) | CMD | AI % of revenue | 62% | |
| 8 | 4(36) | CMD | AI YoY growth | 484% | |
| 9 | 4(36) | CMD | HPC segment revenue | Rs 1,252.94 Mn | |
| 10 | 4(36) | CMD | Private cloud segment revenue | Rs 1,353.46 Mn | |
| 11 | 4(36) | CMD | Order book (as on 30-Jun-2026) | Rs 25,069.35 Mn (transcribed "25,69.35") | TRANSCRIPTION_GARBLED |
| 12 | 4(36) | CMD | L1 position | Rs 8,480.47 Mn | |
| 13 | 4(36) | CMD | Pipeline | ~Rs 104,100 Mn | TRANSCRIPTION_GARBLED — spoken 3 different garbled ways in the same turn ("10,400 10,41 million", "1 lakh 4,000 u 100 million") |
| 14 | 5(38) | CFO | Revenue from operations (repeat) | Rs 8,197 Mn | REPEAT of #1 |
| 15 | 5(38) | CFO | Revenue YoY growth (repeat) | 172.1% | REPEAT of #2 |
| 16 | 5(38) | CFO | Operating EBITDA | garbled "rupees 1,25 million" | TRANSCRIPTION_GARBLED — value not cleanly resolvable from transcript text alone |
| 17 | 5(38) | CFO | EBITDA YoY growth | 169% | |
| 18 | 5(38) | CFO | EBITDA margin | 14.7% | |
| 19 | 5(38) | CFO | PAT (repeat) | Rs 853 Mn | REPEAT of #3 |
| 20 | 5(38) | CFO | PAT YoY growth (repeat) | 179.9% | REPEAT of #4 |
| 21 | 5(38) | CFO | PAT margin (repeat) | 10.3% | REPEAT of #5 |
| 22 | 5(38) | CFO | ROCE | 48.2% | |
| 23 | 5(38) | CFO | ROE | 44.6% | |
| 24 | 5(38) | CFO | GFA turnover ratio | 43.9x | |
| 25 | 5(38) | CFO | Cash conversion cycle | 96 days | |
| 26 | 5(38) | CFO | Receivable days, Mar26 -> Jun26 | 86 -> 78 days | |
| 27 | 5(38) | CFO | Inventory days, Mar26 -> Jun26 | 86 -> 110 days | transcribed "1 to 10 days" |
| 28 | 5(38) | CFO | Net debt (as on 30-Jun-2026) | Rs 1,999 Mn | |
| 29 | 7(42) | Analyst Reu Bet | Order book cited | "35 billion" | ANALYST_FIGURE, TRANSCRIPTION_GARBLED, possible restatement of combined order book+L1 |
| 30 | 8(44) | Mgmt (Sanjay Lodha) | Order book (won, in hand) | ~Rs 2,500 Cr | |
| 31 | 8(44) | Mgmt | L1 (won, not yet received) | ~Rs 800 Cr | |
| 32 | 8(44) | Mgmt | Order book + L1 combined | ~Rs 3,400 Cr | |
| 33 | 8(44) | Mgmt | AI share of order book mix | 40-45% | |
| 34 | 9(46) | Analyst Reu Bet | Growth ask | "50-60% CAGR" | ANALYST_FIGURE |
| 35 | 10(48) | Mgmt (Sanjay Lodha) | Built-up turnover capacity | "3,000-plus Cr" | |
| 36 | 11(50) | Analyst Reu Bet | Revenue target cited | "Rs 4,000 Cr" | ANALYST_FIGURE |
| 37 | 20(68) | Mgmt | Current-year pipeline released | "upwards of Rs 10,000 Cr" | |
| 38 | 21(70) | Mgmt (Sanjay Lodha) | Margin guidance range | 13-14% | |
| 39 | 21(70) | Mgmt | Turnover growth cited | "growing at 90%" | ARITHMETIC_FLAG — inconsistent with 172.1% YoY revenue growth stated at turns 4(36)/5(38); flagged for Role 5 arithmetic-consistency check |
| 40 | 24(76) | Mgmt | Prior-quarter pipeline, ex-strategic order | ~Rs 4,400 Cr | |
| 41 | 27(82) | Analyst Jatin Kalra | Conversion guidance cited | "55-60% over 18-24 months" | ANALYST_FIGURE |
| 42 | 28(84) | Mgmt (Sanjay Lodha) | Conversion ratio reaffirmed | 60% | MERGED_TURN |
| 43 | 33(94) | Analyst Sepa | Conversion cited | "closer to 60%" | ANALYST_FIGURE |
| 44 | 34(96) | Mgmt (Sanjay Lodha) | Conversion tenure updated | 18-24 months (was "18 months") | |
| 45 | 35(98) | Analyst Sepa | 1H revenue-contribution ask | "35-40%" | ANALYST_FIGURE |
| 46 | 38(104) | Analyst Sepa | Inventory-days projection ask | "100-110 days" | ANALYST_FIGURE |
| 47 | 46(120) | Analyst Vine | L1+order book cited | "~3,400 Cr" | ANALYST_FIGURE, REPEAT of #32 |
| 48 | 46(120) | Analyst Vine | Execution cycle cited (prior guidance) | "8-12 weeks" | ANALYST_FIGURE |
| 49 | 47(122) | Mgmt (Sanjay Lodha) | Execution cycle updated | "16-20 weeks" (from 8-12 weeks) | |
| 50 | 52(132) | Mgmt | R&D team size | ~125 people | |
| 51 | 73(174) | Analyst Akshai | QIP figure cited | "Rs 1,200 Cr" | ANALYST_FIGURE |
| 52 | 74(176) | Mgmt (Sanjay Lodha/CMD) | Enabling-resolution validity | 12 months | |
| 53 | 83(194) | Analyst | Strategic order cited (from May call PPT) | "Rs 1,600 Cr" | ANALYST_FIGURE |
| 54 | 84(196) | Mgmt | Strategic order executed in Q1 | Rs 430 Cr (of Rs 1,600 Cr) | |
| 55 | 85(198) | Analyst | Fundraising cited | "Rs 1,200 Cr" | ANALYST_FIGURE, REPEAT of #51 |
| 56 | 86(200) | Mgmt | Capital raised to date | "we haven't raised" = Rs 0 | ZERO_STANDING |
| 57 | 104(236) | Mgmt | Pipeline/order-book runway | "2 years" | |
| 58 | 111(250) | Mgmt | Sector CAGR (AI product line, national level) | 38% over next 3-4 years | |
| 59 | 117(262) | Mgmt (Ankit Singh) | R&D team size (repeat) | ~125 people | REPEAT of #50 |
| 60 | 120(268) | Analyst Ja Lakshmi Gupta | Pipeline cited | "104 billion" (garbled) | ANALYST_FIGURE, TRANSCRIPTION_GARBLED — restating ~Rs 104,100 Mn / Rs 10,410 Cr pipeline |
| 61 | 121(270) | Mgmt (Ankit Singh) | Inventory valuation method change | FIFO -> Moving Weighted Average | ACCOUNTING_POLICY_CHANGE — no magnitude quantified |
| 62 | 122(272) | Mgmt (Sanjay Lodha) | Conversion rate & timeline (repeat) | 60% / 18-24 months | REPEAT of #42, #44 |
| 63 | 129(286) | Analyst Anoj Kashab | Exports share cited | "4-5%" | ANALYST_FIGURE |
| 64 | 133(294) | Analyst Sarab Sadhuani | Port bandwidth cited | "100 GB" | ANALYST_FIGURE |

Canonical management-only count (rows without ANALYST_FIGURE flag) = 49.
Canonical 23-figure count per injected task list (deduped to one row per
named figure/ratio, i.e. rows 1-13, 17-18, 22-27, 30-32(as one order-book
figure), 44, 49, 50, 52, 54, 58, 63 collapse to the 23 named items) = 23
(GATE A2 verified above).

---

## TABLE 5 — FORWARD-COMMITMENT AND HEDGE PHRASES (representative sweep, turn-anchored; full lexicon-matched pass is A3's job per operating rules)

| Turn(line) | Speaker | Phrase (as spoken) | Type |
|---|---|---|---|
| 8(44) | Mgmt | "that will give you an indication...what kind of numbers we can expect" | forward-commitment (soft) |
| 10(48) | Mgmt | "I'm not guiding on any for any new capex as such" | hedge |
| 12(52) | Mgmt | "we will invest in the working capital for growth" | forward-commitment |
| 12(52) | Mgmt | "we've not found out uh what what trajectory will go" | hedge |
| 20(68) | Mgmt | "this is how we're going to report as we go forward" | forward-commitment (disclosure practice) |
| 21(70) | Mgmt | "our margins will remain between 13 to 14%" | forward-commitment (guidance) |
| 28(84) | Mgmt | "we will not like to disclose too much" | hedge (confidentiality) |
| 34(96) | Mgmt | "it will remain 18 to 24 months but not beyond that" | forward-commitment |
| 37(102) | Mgmt | "slightly difficult to say...very difficult" | hedge |
| 47(122) | Mgmt | "now we are measuring basically 16 to 20 weeks...can stretch a little bit" | hedge + forward-commitment |
| 49(126) | Mgmt | "not guiding on revenue at all" | hedge |
| 52(132) | Mgmt | "investments we cannot quantify at this point of time" | hedge |
| 74(176) | Mgmt | "if at some stage we think we'll need to raise capital we'll look at it" | hedge / conditional forward-commitment |
| 86(200) | Mgmt | "if and when we need to raise capital we'll raise capital" | conditional forward-commitment |
| 102(232) | Mgmt | "the strategic is the new normal" | reframing/hedge on prior disclosure practice |
| 104(236) | Mgmt | "difficult beyond that sitting today to address" | hedge |
| 111(250) | Mgmt | "at a very conservative level...38% CAGGR" | forward-commitment (guidance) |
| 113(254) | Mgmt | "it's for the AI for product line only" | scope-limiting qualifier |
| 121(270) | Mgmt | "shifted our inventory valuation from FIFO to the moving weighted average method" | disclosed accounting policy change |
| 123(274) | Mgmt | "it's very difficult at this point of time to give segment wise funnel" | hedge |
| 128(284) | Mgmt | "I would not like to comment anything more" | hedge |
| 130(288) | Mgmt | "we are not focusing on exports actually" | forward-statement (strategic priority) |
| 134(296) | Mgmt | "we are not disclosing it as a separate...product skew" | hedge (disclosure limitation) |
| 111(250) | Mgmt | "we'll have to strategize to capture it as much as we can" | forward-commitment (soft) |

---

## SUMMARY FLAGS RAISED
MALFORMED_MARKER (line 186 — caught only on resweep, GATE A2 mismatch
resolved), NAME_GARBLED (multiple analyst/management names, transcript
quality issue throughout), MGMT_ABSENCE (Navin Lodha, full-time director;
Sidar Vikram, CSSO — both introduced, neither individually attributable
to any turn), ATTRIBUTION_AMBIGUOUS (several turns cannot be cleanly
assigned between CMD and CFO due to poor diarization — turns 12, 20, 23,
41, 60), MERGED_TURN (turns 28/84 and 123/274 — management answer and
analyst's next question run together with no transcript break),
TRANSCRIPTION_GARBLED (figures at turns 4/36, 5/38, 29/42, 60/268),
ARITHMETIC_FLAG (turn 21/70 "growing at 90%" vs. 172.1% YoY revenue
growth stated twice elsewhere — feeds Role 5 arithmetic-consistency
check), REPEAT_QUESTION (pipeline-conversion 60%/18-24-month question
asked by 3 different analysts — exchanges 3a, 4, 10; enabling-resolution
purpose asked by 3 different analysts — exchanges 7, 8, 9),
ACCOUNTING_POLICY_CHANGE (inventory valuation FIFO -> moving weighted
average, disclosed at turn 121/270, no magnitude quantified on the
call), ZERO_STANDING (capital raised to date against the Rs 1,200 Cr
enabling resolution = Rs 0, confirmed explicitly at turns 86/200 and
74/176).
