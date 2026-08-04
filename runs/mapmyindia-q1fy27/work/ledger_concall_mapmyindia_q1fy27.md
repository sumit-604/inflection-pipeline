# A2 ENUMERATOR LEDGER — MAPMYINDIA (C.E. Info Systems Limited) Q1 FY27 Concall

Source: /home/user/inflection-pipeline/runs/mapmyindia-q1fy27/work/extract_concall_mapmyindia_q1fy27.txt
All line numbers below are the SOURCE transcript line numbers embedded in the
extract (the "N:" prefix on each extract line, preserved 1:1 with the
original transcript per the A1 header). Turn numbers are assigned
sequentially by this ledger, first turn = 1.

```
=== A2 COUNT TEST ===
category: turns         grep_count: 86   sweep_count: 86   match: yes
category: questions     grep_count: 42   sweep_count: 42   match: yes
  (grep_count = candidate analyst-attributed turns in Q&A: 35 bracket-tagged
  [Anmol/Amar/Analyst/Gautam/Abhishek/Pranay] + 7 unbracketed turns opening
  each of the 7 numbered questions. sweep_count = manual classification of
  those same 42 turns into 33 QUESTION rows + 9 NON_QUESTION
  closing/acknowledgment rows (33+9=42); both methods land on the identical
  42-turn set, so the classification reconciles.)
category: mgmt_numbers  grep_count: 46   sweep_count: 46   match: yes
  (grep_count = digit-sequences with units, in Rakesh Verma / Rohan Verma /
  unbracketed management-opening / "[Management]"-tagged lines, after
  discarding false positives that are quarter/FY labels embedded in prose
  — e.g. the "4" in "Q4", the "26" in "FY26" — not stated figures.
  sweep_count = independent manual walk of every management turn, atomic
  figure by atomic figure. Both methods produce the same 46-item set.)
gate_a2: pass
=== END COUNT TEST ===
```

---

## 1. PARTICIPANTS (management and analyst side)

| # | Name | Firm / Role | Side | Line cite | Flags |
|---|------|-------------|------|-----------|-------|
| 1 | (unnamed) Operator | Telephone conferencing operator | Host-side | L7 | — |
| 2 | Ms. Natasha Singh | Arhant Capital Markets Limited (moderator/host) | Host-side | L2, L9 | — |
| 3 | Mr. Rakesh Verma | Group Chairman & MD | Management | L3 | — |
| 4 | Mr. Rohan Verma | Joint MD | Management | L3 | — |
| 5 | Mr. Anuj Jain | CFO | Management | L3 | `SILENT_PARTICIPANT` — named present, zero individually-attributed speaking turns anywhere in transcript; all financial/reconciliation answers tagged to Rakesh Verma, Rohan Verma, or generic "[Management]" |
| 6 | Mr. Saurabh Somani | Company Secretary | Management | L3 | `SILENT_PARTICIPANT` — same as above |
| 7 | Anmol G | DA Capital | Analyst (Q1) | L19 | — |
| 8 | Amar Maurya | Lucky Investment | Analyst (Q2) | L42 | — |
| 9 | Ahmed Chandra? (Aejas/Ahmed) | HDFC Securities | Analyst (Q3) | L57 | `NAME_UNCERTAIN` — source transcript itself marks the name with "?" and an alternate spelling in parentheses |
| 10 | Gautam Rathi | CWC | Analyst (Q4) | L84 | — |
| 11 | Abhishek Jain | Chris PMS | Analyst (Q5) | L127 | — |
| 12 | Pranay Jain | Banyan Tree Advisors Private Limited | Analyst (Q6) | L154 | — |
| 13 | (Jamoshi/Jayesh) | Chris PMS | Analyst (Q7) | L169 | `NAME_UNCERTAIN` — source transcript gives two alternate spellings in parentheses, no firm-confirmed first name |

Total participants enumerated: 13. `MGMT_ABSENCE` not applicable — Chairman & MD (Rakesh Verma) present and extensively speaking; no substantive-call absence of promoter/CMD.

---

## 2. SPEAKER TURNS (sequential, 86 total)

Format: Turn# | Line | Speaker | First ~10 words | Flags

| Turn | Line | Speaker | First ~10 words | Flags |
|------|------|---------|------------------|-------|
| 1 | L7 | Operator (unnamed) | "Ladies and gentlemen, good day and welcome to the..." | — |
| 2 | L9 | Natasha Singh (Arhant) | "Thank you so much. Hello and good evening to..." | — |
| 3 | L12 | Rakesh Verma (opening) | "Uh thank you Natasha, this is Rakesh Verma. I'll..." | — |
| 4 | L15 | Rohan Verma (opening) | "Uh thank you Mr. Verma and good evening to..." | — |
| 5 | L20 | Anmol (Q1a) | "Yeah hi, thanks for the opportunity. I have few..." | QUESTION |
| 6 | L22 | Rohan Verma (A) | "Sure. See there are lot of opportunities ahead for..." | — |
| 7 | L24 | Anmol (Q1b) | "Sure, thanks that's helpful. Second is, last year we..." | QUESTION |
| 8 | L26 | Rakesh Verma (A) | "Anmol it was not and it is not a..." | — |
| 9 | L28 | Anmol (Q1c) | "Right sir, just wanted to understand when did it..." | QUESTION |
| 10 | L30 | Rohan Verma (A) | "It got time shifted as Mr. Verma explained, this..." | — |
| 11 | L32 | Anmol (Q1d) | "Understood. And one last thing, in this quarter we..." | QUESTION, `REPEAT_QUESTION` (write-off topic; see also Turns 28, 36) |
| 12 | L34 | Rakesh Verma (A) | "Okay. First let me tell you it is a..." | — |
| 13 | L36 | Anmol (Q1e) | "Right. So from that perspective sir, can we expect..." | QUESTION |
| 14 | L38 | Rakesh Verma (A) | "Because we have always been saying that we have..." | — |
| 15 | L40 | Anmol (closing) | "Sure. Thank you for answering my questions and I'll..." | NON_QUESTION |
| 16 | L43 | Amar Maurya (Q2a) | "Yeah hi sir. Thanks a lot for the opportunity...." | QUESTION |
| 17 | L45 | Rohan Verma (A) | "I mean, just — you have to look at..." | — |
| 18 | L47 | Amar Maurya (Q2b) | "Okay okay. And secondly sir, now in terms of..." | QUESTION |
| 19 | L49 | Rohan Verma (A) | "Amar, what we had disclosed at end of Q4..." | — |
| 20 | L51 | Amar Maurya (Q2c) | "So basically you're saying on a full year basis..." | QUESTION |
| 21 | L53 | Rakesh Verma (A) | "I would suggest that if you understand the overall..." | — |
| 22 | L55 | Amar Maurya (closing) | "Sure sir. Thank you. Thanks a lot." | NON_QUESTION |
| 23 | L58 | Analyst / Ahmed (Q3a) | "Yes sir, thanks for the opportunity. So my question..." | QUESTION, multi-part |
| 24 | L60 | Rohan Verma (A / aside) | "Will tell you more, but I'm sure you are..." | — |
| 25 | L62 | Analyst | "Yeah." | NON_QUESTION (acknowledgment to management's aside) |
| 26 | L64 | "[Rohan Verma]" (A) | "MapmyIndia is powering it. And you can see our..." | `SPEAKER_LABEL_ARTIFACT` — turn is labeled [Rohan Verma] but closes "But Rohan — you can add something," referring to Rohan in the third person; content suggests the actual speaker is Rakesh Verma, mislabeled in source |
| 27 | L66 | Rohan Verma (A) | "Yeah. So we disclose currently amid the order book..." | — |
| 28 | L68 | Analyst (Q3b) | "Okay. And my second question is on the write-off..." | QUESTION, multi-part, `REPEAT_QUESTION` (write-off topic; see also Turns 11, 36) |
| 29 | L70 | Rohan Verma (A) | "Yeah. And also sorry, just to complete the answer..." | — |
| 30 | L72 | Analyst (Q3c) | "Okay. And in terms of the overall receivables that..." | QUESTION |
| 31 | L74 | Rohan Verma (A) | "Yeah, this receivables we must have shared in the..." | hedge — "I don't have it... I don't remember" |
| 32 | L76 | Analyst (Q3d) | "There in Q1?" | QUESTION |
| 33 | L78 | Rohan Verma (A) | "Q1 we've not given the balance sheet, but just..." | hedge — "I'm trying to remember" |
| 34 | L80 | Management (A) | "176 crores was the total at the end of..." | — |
| 35 | L82 | Analyst (closing) | "Okay okay. Thank you and all the best." | NON_QUESTION |
| 36 | L85 | Gautam Rathi (Q4a) | "Yeah hi, thanks for taking my question and congrats..." | QUESTION, `REPEAT_QUESTION` (write-off topic; see also Turns 11, 28) |
| 37 | L87 | Rakesh Verma (A) | "Okay let me make you understand in a simple..." | — |
| 38 | L89 | Gautam Rathi (Q4b) | "Net 80 lakhs." | QUESTION (implicit confirm-seek) |
| 39 | L91 | Rakesh Verma (A) | "Is net 80 lakhs." | — |
| 40 | L93 | Gautam Rathi (Q4c) | "Okay, so in your P&L the charge off is..." | QUESTION |
| 41 | L95 | Management (A) | "But margin impacted more, 4%. That's what he's trying..." | — |
| 42 | L97 | Gautam Rathi (Q4d) | "Understood. So your net impact is 80 lakhs, but..." | QUESTION (confirm) |
| 43 | L99 | Management (A) | "Right, you got it." | — |
| 44 | L101 | Gautam Rathi (Q4e) | "That's why. Okay. Understood, very clear. Second — two..." | QUESTION, multi-part (international + IoT seasonality) |
| 45 | L103 | Rohan Verma (A) | "Sure. Let me answer the second one first, it's..." | — |
| 46 | L105 | Gautam Rathi (Q4f) | "No sorry, my question was—" | QUESTION (interrupted/restated) |
| 47 | L107 | Rohan Verma (A) | "No no let me explain. Increase will lead to..." | — |
| 48 | L109 | Gautam Rathi (Q4g) | "You understand the quarterly seasonality — I just want..." | QUESTION (restated) |
| 49 | L111 | Rohan Verma (A) | "It's not a quarterly seasonality, Gautam. Our services revenue..." | — |
| 50 | L113 | Gautam Rathi (Q4h) | "Maybe let me put my question better. First of..." | QUESTION (restated w/ figures) |
| 51 | L115 | Rohan Verma (A) | "Okay, see, Q1 to Q1 is 16.3 to 18...." | — |
| 52 | L117 | Gautam Rathi (Q4i) | "Okay fine, I'll take it offline. The last one..." | QUESTION (new sub-topic: international business) |
| 53 | L119 | Rohan Verma (A) | "International business — things are going fine. I don't..." | hedge — "I don't know... I'm guessing" |
| 54 | L121 | Gautam Rathi (Q4j) | "So in the current revenue there might not be..." | QUESTION (confirm) |
| 55 | L123 | Rohan Verma (A) | "Profit — it's not material." | — |
| 56 | L125 | Gautam Rathi (closing) | "Okay understood, thanks a lot, all the best." | NON_QUESTION |
| 57 | L128 | Abhishek Jain (Q5a) | "Thanks for the opportunity sir. In automotive, just wanted..." | QUESTION |
| 58 | L130 | Rohan Verma (A) | "I mean it's all shown in the automotive, we..." | — |
| 59 | L132 | Abhishek Jain (Q5b) | "I think your revenue more than 75% will come..." | QUESTION |
| 60 | L134 | Rohan Verma (A) | "We don't break out subvertical level, Abhishek." | — |
| 61 | L136 | Abhishek Jain (Q5c) | "So how is the revenue per vehicle in terms..." | QUESTION |
| 62 | L138 | Rohan Verma (A) | "This is all bespoke — price is a function..." | hedge — "it's all competitive information" |
| 63 | L140 | Abhishek Jain (Q5d) | "Got it sir. And how is the share of..." | QUESTION |
| 64 | L142 | Rohan Verma (A) | "Yeah we are the provider there, we are the..." | — |
| 65 | L144 | Abhishek Jain (Q5e) | "And how much is our share of business in..." | QUESTION |
| 66 | L146 | Rohan Verma (A) | "We are the suppliers there. We have all the..." | — |
| 67 | L148 | Abhishek Jain (Q5f) | "Okay got it. So sir just wanted to understand..." | QUESTION |
| 68 | L150 | Rohan Verma (A) | "I mean it's looking good. Target — I'm not..." | hedge — "not going to talk about quantitative target" |
| 69 | L152 | Abhishek Jain (closing) | "Thank you sir." | NON_QUESTION |
| 70 | L155 | Pranay Jain (Q6a) | "Hello sir, can you hear me? Thank you for..." | QUESTION |
| 71 | L157 | Rohan Verma (A) | "Yeah. In the slides in the investor presentation we've..." | — |
| 72 | L159 | Pranay Jain (Q6b) | "Yeah I have gone through that. I also wanted..." | QUESTION |
| 73 | L161 | Rohan Verma (A) | "There's no typical, it varies. For some customer it..." | — |
| 74 | L163 | Pranay Jain (Q6c) | "Right, understood. And second question is on wallet share..." | QUESTION |
| 75 | L165 | Rohan Verma (A) | "Yeah, that is what we explained — that for..." | — |
| 76 | L167 | Pranay Jain (closing) | "Understood, got it, thank you." | NON_QUESTION |
| 77 | L170 | Analyst / Jamoshi-Jayesh (Q7a) | "Yeah sir, just wanted to confirm — the reason..." | QUESTION |
| 78 | L172 | Management (A) | "You're talking about lower gross margin — we have..." | — |
| 79 | L174 | Analyst | "Correct." | NON_QUESTION (acknowledgment) |
| 80 | L176 | Management (A) | "Oh yeah, you are right. The mix for this..." | — |
| 81 | L178 | Analyst (Q7b) | "Understood. And sir, how are we evaluating the digital..." | QUESTION |
| 82 | L180 | Rohan Verma (A) | "Yeah, we are pretty well positioned in digital twin..." | — |
| 83 | L182 | Analyst (closing) | "Understood, thanks a lot, that's it from me." | NON_QUESTION |
| 84 | L185 | Operator (unnamed) | "As there are no further questions, I now hand..." | — |
| 85 | L186 | Management (closing) | "We just thank everybody for joining and we look..." | — |
| 86 | L187 | Operator/Moderator | "On behalf of Arhant Capital Markets Limited that concludes..." | — |

Turn count: 86.

---

## 3. QUESTIONS (33 distinct question rows; every analyst turn classified NON_QUESTION excluded)

| Q# | Analyst | Firm | Topic | Turn | Line | Flags |
|----|---------|------|-------|------|------|-------|
| 1 | Anmol G | DA Capital | JMD focus area / priority vertical for first couple of years | 5 | L20 | — |
| 2 | Anmol G | DA Capital | Auto OEM contract reduction — timing, base effect for Q2 FY27 | 7 | L24 | — |
| 3 | Anmol G | DA Capital | When did the OEM technology reduction start last year | 9 | L28 | — |
| 4 | Anmol G | DA Capital | Write-off in a client this quarter — detail and recoverability | 11 | L32 | `REPEAT_QUESTION` |
| 5 | Anmol G | DA Capital | Can EBITDA margin run at 43-44% over next few quarters | 13 | L36 | — |
| 6 | Amar Maurya | Lucky Investment | Standalone map-led growth only 6%; why core business not growing | 16 | L43 | — |
| 7 | Amar Maurya | Lucky Investment | How to view forward growth given government-side order backlog | 18 | L47 | — |
| 8 | Amar Maurya | Lucky Investment | Challenge: is open-order growth expected to convert to visible revenue/core growth | 20 | L51 | — |
| 9 | Ahmed (Analyst) | HDFC Securities | Order book mix by AEG segment + enterprise focus vertical + e-commerce deal traction | 23 | L58 | multi-part |
| 10 | Analyst | HDFC Securities | Write-off follow-up: government receivables mix, further write-off/collection-delay risk, government strategy | 28 | L68 | multi-part, `REPEAT_QUESTION` |
| 11 | Analyst | HDFC Securities | What part of total receivables is from government contracts, as of this quarter | 30 | L72 | — |
| 12 | Analyst | HDFC Securities | Clarifying: "There in Q1?" (is that receivables figure as of Q1) | 32 | L76 | — |
| 13 | Gautam Rathi | CWC | Reconcile 80 lakh net P&L impact vs stated 4% EBITDA margin impact | 36 | L85 | `REPEAT_QUESTION` |
| 14 | Gautam Rathi | CWC | "Net 80 lakhs." — confirmation-seek restatement | 38 | L89 | implicit question |
| 15 | Gautam Rathi | CWC | Points out margin impact should be ~1.5%, not 4%, per his math | 40 | L93 | — |
| 16 | Gautam Rathi | CWC | Confirms understanding: EBITDA impacted 4% because write-off nets against other income below EBITDA | 42 | L97 | implicit question |
| 17 | Gautam Rathi | CWC | International regions update AND IoT services revenue seasonality | 44 | L101 | multi-part |
| 18 | Gautam Rathi | CWC | "No sorry, my question was—" (interrupted restatement) | 46 | L105 | — |
| 19 | Gautam Rathi | CWC | Re-asks: wants the quarterly seasonality point specifically | 48 | L109 | — |
| 20 | Gautam Rathi | CWC | Restates with own figures: IoT services revenue build-up quarter to quarter (37/27/24/18 cr sequence, analyst-sourced) | 50 | L113 | — |
| 21 | Gautam Rathi | CWC | New sub-topic: international business update | 52 | L117 | — |
| 22 | Gautam Rathi | CWC | Confirms: no material P&L revenue contribution currently from international | 54 | L121 | implicit question |
| 23 | Abhishek Jain | Chris PMS | Automotive revenue mix — 2W / PV / CV split | 57 | L128 | — |
| 24 | Abhishek Jain | Chris PMS | Confirms PV segment >75% of automotive revenue | 59 | L132 | — |
| 25 | Abhishek Jain | Chris PMS | Revenue per vehicle by sub-segment + growth expectation | 61 | L136 | — |
| 26 | Abhishek Jain | Chris PMS | Share of business with large PV OEMs (Maruti, Hyundai, Mahindra) | 63 | L140 | — |
| 27 | Abhishek Jain | Chris PMS | How much is our share of business in those OEMs (follow-up) | 65 | L144 | — |
| 28 | Abhishek Jain | Chris PMS | Automotive segment growth target for FY27 | 67 | L148 | — |
| 29 | Pranay Jain | Banyan Tree Advisors | Typical contract structure — tenure, pricing, escalation/scope-expansion provisions | 70 | L155 | — |
| 30 | Pranay Jain | Banyan Tree Advisors | Follow-up specifically on typical contract tenure | 72 | L159 | — |
| 31 | Pranay Jain | Banyan Tree Advisors | Wallet-share expansion within existing customers | 74 | L163 | — |
| 32 | Analyst (Jamoshi/Jayesh) | Chris PMS | Reason for lower gross margin — product mix / IoT hardware share | 77 | L170 | — |
| 33 | Analyst (Jamoshi/Jayesh) | Chris PMS | Digital twin cities opportunity + government Naksha scheme role | 81 | L178 | multi-part |

Question count: 33.

`REPEAT_QUESTION` cross-reference: the one-time government-client write-off is independently raised by three different analysts — Anmol G/DA Capital (Q4, Turn 11), the HDFC Securities analyst (Q10, Turn 28), and Gautam Rathi/CWC (Q13, Turn 36).

---

## 4. MANAGEMENT-STATED NUMBERS (46 atomic figures; guidance, capacity, margin, order book, receivables, timeline)

| # | Turn | Line | Speaker | Figure | Context | Flags |
|---|------|------|---------|--------|---------|-------|
| 1 | 3 | L12 | Rakesh Verma | 14.9% YoY | Q1 FY27 revenue growth | — |
| 2 | 3 | L12 | Rakesh Verma | Rs 139.7 crores | Q1 FY27 revenue | — |
| 3 | 3 | L12 | Rakesh Verma | Rs 56.1 cr | Q1 FY27 EBITDA | — |
| 4 | 3 | L12 | Rakesh Verma | 40.2% | Q1 FY27 EBITDA margin | — |
| 5 | 3 | L12 | Rakesh Verma | 8.6% | Q1 FY27 PAT growth YoY | — |
| 6 | 3 | L12 | Rakesh Verma | Rs 49.7 cr | Q1 FY27 PAT | — |
| 7 | 3 | L12 | Rakesh Verma | 31.2% | Q1 FY27 PAT margin | — |
| 8 | 3 | L12 | Rakesh Verma | "last 5 years" | Duration the old A&M/C&E segment framework was used | — |
| 9 | 3 | L12 | Rakesh Verma | "30th of June" | Date Rohan Verma's JMD appointment was announced | — |
| 10 | 4 | L15 | Rohan Verma | "five plus years, maybe 6 7 8 years" | Duration company has used AI to update/enhance maps | vague range, as spoken |
| 11 | 4 | L15 | Rohan Verma | "30 years" | Company's operating history / continuous innovation duration | — |
| 12 | 10 | L30 | Rohan Verma | 26 crores | Automotive segment revenue, Q1 FY25 | — |
| 13 | 10 | L30 | Rohan Verma | 46 crores | Automotive segment revenue, Q1 FY26 | — |
| 14 | 10 | L30 | Rohan Verma | 59 crores | Automotive segment revenue, Q1 FY27 | — |
| 15 | 10 | L30 | Rohan Verma | 182 (crores) | Automotive segment revenue, full year FY25 | — |
| 16 | 10 | L30 | Rohan Verma | 190 (crores) | Automotive segment revenue, full year FY26 | — |
| 17 | 10 | L30 | Rohan Verma | "nine quarters" | Length of history shown on the AEG segmental-revenue slide | — |
| 18 | 12 | L34 | Rakesh Verma | ~4 crores | Gross impact of one-time government-client write-off | — |
| 19 | 12 | L34 | Rakesh Verma | 80 lakhs | Net P&L effect of the write-off | recurs — see #34, #35 |
| 20 | 12 | L34 | Rakesh Verma | 40.2 | EBITDA margin, restated in context of write-off | — |
| 21 | 12 | L34 | Rakesh Verma | "43 plus"% | Hypothetical EBITDA margin ex-write-off | — |
| 22 | 14 | L38 | Rakesh Verma | "35% plus" | EBITDA margin target for full FY27 | forward-commitment |
| 23 | 17 | L45 | Rohan Verma | 98.2 cr | Map-led revenue, prior period | — |
| 24 | 17 | L45 | Rohan Verma | 98.7 (cr) | Map-led revenue, current period | — |
| 25 | 17 | L45 | Rohan Verma | 23.4 (cr) | IoT-led revenue, prior period | — |
| 26 | 17 | L45 | Rohan Verma | 41 (cr) | IoT-led revenue, current period | recurs — see #37 |
| 27 | 17 | L45 | Rohan Verma | 45.7 (cr) | Automotive revenue, prior period | — |
| 28 | 17 | L45 | Rohan Verma | 58.98 cr | Automotive revenue, current period | — |
| 29 | 17 | L45 | Rohan Verma | 29% | Automotive revenue jump | — |
| 30 | 17 | L45 | Rohan Verma | 60.6 (to) 64 crores | Enterprise revenue, prior->current | `NUMBER_ARTIFACT` — operator-flagged transcription anomaly (possible "16.6"-type mis-speak); recorded exactly as stated, not corrected |
| 31 | 17 | L45 | Rohan Verma | 6% | Enterprise revenue jump | — |
| 32 | 19 | L49 | Rohan Verma | 1,750 crores | Open order book, disclosed at end of Q4 FY26 | — |
| 33 | 19 | L49 | Rohan Verma | 1,500 crores | Open order book, previous year end | — |
| 34 | 19 | L49 | Rohan Verma | "about 1,350 cr" | Open order book, year before that | hedge — "about" |
| 35 | 33 | L78 | Rohan Verma | "120-130 crores" | Uncertain recollection of a receivables total | hedge — "I'm trying to remember" |
| 36 | 34 | L80 | Management | 176 crores | Total receivables at end of FY26 | — |
| 37 | 37 | L87 | Rakesh Verma | ~4 crores | Write-off receivable, restated | recurs — see #18 |
| 38 | 37 | L87 | Rakesh Verma | 3.2 cr | Payment avoided (offset against the write-off) | — |
| 39 | 37 | L87 | Rakesh Verma | 80 lakhs | Net accounting effect, restated | recurs — see #19, #35 (ledger #41 below) |
| 40 | 39 | L91 | Rakesh Verma | 80 lakhs | Net effect re-confirmed | recurs — 3rd mgmt mention this call |
| 41 | 41 | L95 | Management | 4% | EBITDA margin impact, restated (booked via other expense / other income) | recurs — see #4-context |
| 42 | 45 | L103 | Rohan Verma | 23 (to) 41 cr | IoT-led revenue growth, restated rounded | recurs — see #25/#26 |
| 43 | 45 | L103 | Rohan Verma | 7 crores (to) 23 cr | IoT hardware revenue, prior->current | — |
| 44 | 51 | L115 | Rohan Verma | 16.3 (to) 18 | IoT services revenue, Q1 FY26 to Q1 FY27 | — |
| 45 | 73 | L161 | Rohan Verma | "5 years" | Example contract tenure, long end | illustrative, not a specific customer disclosure |
| 46 | 73 | L161 | Rohan Verma | "one year" | Example contract tenure, short end | illustrative, not a specific customer disclosure |

Management-number count: 46.

Note: analyst-restated figures citing management's own numbers back to them (e.g., Gautam's "Net 80 lakhs" at Turn 38, or his cited services-revenue series "37/27/24/18 cr" at Turn 50, which management neither confirms nor originates in the same form) are NOT counted here — those are captured in the Questions table (Q14, Q20) since they are analyst speech, not management speech. Where management independently repeats a figure (e.g., 80 lakhs at Turns 12, 37, 39), each management-turn mention is retained as its own row per the enumerator mandate to record every number as spoken, with cross-references noted.

---

## 5. FORWARD-COMMITMENT AND HEDGE PHRASES (supplementary; not separately gated per task scope)

| Turn | Line | Speaker | Phrase (paraphrase) | Type |
|------|------|---------|----------------------|------|
| 14 | L38 | Rakesh Verma | "we have kept the target for us to do a 35% plus for the whole year" | forward-commitment |
| 19 | L49 | Rohan Verma | "that gives us strong visibility into future... we are confident about what we're going to do in the time to come" | forward-commitment (soft, non-quantitative) |
| 19 | L49 | Rohan Verma | "I'm not — we can't obviously comment quarter on quarter what is going to happen" | hedge |
| 27 | L66 | Rohan Verma | "for competitive reasons, at least so far, we are not disclosing that" (order book fixed/volume split) | hedge / non-disclosure |
| 31 | L74 | Rohan Verma | "I don't have it just off the top of my hand, so I don't remember" | hedge |
| 33 | L78 | Rohan Verma | "I'm trying to remember — it was 120-130 crores" | hedge |
| 53 | L119 | Rohan Verma | "I don't know, in our P&L, if we've shown the share of loss of JV... I'm guessing" | hedge |
| 62 | L138 | Rohan Verma | "it's all negotiated bespoke, so I can't speak to individual prices, it's all competitive information" | hedge / non-disclosure |
| 68 | L150 | Rohan Verma | "Target — I'm not going to talk about quantitative target" | hedge / non-disclosure |
| 68 | L150 | Rohan Verma | "the objective is to keep winning more orders and to execute on the orders...as that increases the revenue will also increase there" | forward-commitment (qualitative) |
| 82 | L180 | Rohan Verma | "we are looking at that space quite aggressively... but we'll be calibrated in our approach" (digital twin / Naksha) | forward-commitment + hedge combined |

---

## 6. FLAGS SUMMARY

- `REPEAT_QUESTION` — write-off topic asked independently by 3 analysts (Turns 11, 28, 36)
- `NUMBER_ARTIFACT` — enterprise revenue base figure stated as "60.6" (Turn 17 / L45); preserved verbatim per operator instruction, not corrected
- `SPEAKER_LABEL_ARTIFACT` — Turn 26 (L64) labeled [Rohan Verma] but content ("But Rohan — you can add something") implies a different speaker, likely Rakesh Verma, referring to Rohan in the third person
- `NAME_UNCERTAIN` — Q3 analyst ("Ahmed Chandra?" / Aejas-Ahmed, HDFC Securities) and Q7 analyst ("Jamoshi/Jayesh", Chris PMS); both name-uncertain in the source transcript itself
- `SILENT_PARTICIPANT` — CFO Anuj Jain and Company Secretary Saurabh Somani listed as present (L3) but have zero individually-attributed speaking turns; all financial reconciliation answers are attributed to Rakesh Verma, Rohan Verma, or a generic "[Management]" tag

No `ZERO_STANDING`, `ENTITY_CHANGE`, `DROPPED_SLIDE`, or `MGMT_ABSENCE` conditions found in this document (not applicable to concall transcript content / no such instances present).

---

## 7. CATEGORY COUNTS (for YAML)

- turns: 86
- questions: 33
- mgmt_numbers: 46
- participants (supplementary, ungated): 13
- forward_hedge_phrases (supplementary, ungated): 11

```yaml
stage: A2-enumerator
company: "C.E. Info Systems Limited / MapMyIndia (MAPMYINDIA)"
quarter: "Q1 FY27"
doctype: "concall"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/mapmyindia-q1fy27/work/ledger_concall_mapmyindia_q1fy27.md"
counts:
  turns: 86
  questions: 33
  mgmt_numbers: 46
flags_raised: [REPEAT_QUESTION, NUMBER_ARTIFACT, SPEAKER_LABEL_ARTIFACT, NAME_UNCERTAIN, SILENT_PARTICIPANT]
gate_a2: pass
mismatch_note: ""
```
