LEDGER — QPOWER Q1 FY27 CONCALL (Quality Power Electrical Equipments Ltd)
A2 ENUMERATOR OUTPUT
Source: runs/qpower-q1fy27/work/extract_concall_qpower_q1fy27.txt (318 lines, verbatim ASR transcript)

=== A2 COUNT TEST ===
category: turns          grep_count: 143  sweep_count: 143  match: yes
category: questions (questioner slots)   grep_count: 15   sweep_count: 15   match: yes
category: mgmt_numbers (turns with >=1 numeral)   grep_count: 38   sweep_count: 38   match: yes
category: notes          grep_count: N/A (doctype has no numbered notes section)   sweep_count: N/A   match: n/a
category: line_items     grep_count: N/A (doctype has no financial table)         sweep_count: N/A   match: n/a
category: zero_standing  grep_count: N/A   sweep_count: N/A   match: n/a
category: agenda_items   grep_count: N/A (no Board Outcome letter in this doctype) sweep_count: N/A   match: n/a
category: auditor_paras  grep_count: N/A   sweep_count: N/A   match: n/a
category: entities       grep_count: N/A   sweep_count: N/A   match: n/a
category: slides         grep_count: N/A (concall transcript, not investor presentation) sweep_count: N/A match: n/a
gate_a2: pass
=== END COUNT TEST ===

## Methodology note on the "questions" count test

Grep pass: `grep -n -E "^\[MODERATOR\].*(line of|question is from)"` on the extract
returns 15 hits (the moderator's questioner-introduction lines, including the
"first question is from the line of..." opener and 14 subsequent "next question is
from the line of..." handoffs). Manual sweep: walking the Q&A section and marking
every new `[ANALYST — Name, Firm]` label that immediately follows a moderator
handoff also yields 15 distinct questioner slots. The two reconcile exactly: 15
questioner slots, 14 unique analysts (Rahul Maheshwari / Ambit Investment Advisor
appears twice — slot 2, line 60, and slot 15, line 300, the latter introduced by
the moderator at line 298 as "one last question... due to paucity of time").
GATE A2 for this category: pass.

A second, finer-grained sweep (Section 4 below) further breaks each of the 15
slots into individual distinct questions (49 total) for A3/A4 traceability. That
finer count is informational and not part of the GATE A2 reconciliation, which is
anchored on the mechanically verifiable 15-slot figure per task instruction.

## Methodology note on the "mgmt_numbers" count test

Grep pass (Python, equivalent to `grep -n` restricted to `[MANAGEMENT` tagged lines,
testing the body text after the speaker tag for any digit character `\d`): 38 of the
58 total MANAGEMENT-tagged turns contain at least one numeral. Manual sweep across
the same 58 turns, read in full, independently marks the identical 38 turns as
numerically bearing (the other 20 use only spelled-out quantities — "two HVDCs",
"half a dozen statcom projects", "hundred million dollar bids", "60 audits" restated
without digits, "four GW facility", "40 acres" restated, etc. — or carry no
quantified content at all). Match: yes. GATE A2 for this category: pass.

Section 5 below itemizes every individual number found inside those 38 turns
(and, separately, the spelled-out quantities inside the other 20 non-gated turns)
as discrete rows for the Role 5 arithmetic-consistency check — this itemized count
runs well above 38 and is informational, not part of the gate.

---

## SECTION 1 — PARTICIPANTS (both sides)

| # | Name | Role / Firm | First appearance (line) | Flags |
|---|------|-------------|--------------------------|-------|
| 1 | Mr. Gandharan Parab ("Pandu") | Joint Managing Director, QPOWER | line 22 (roster), speaks line 34 | — |
| 2 | Mr. Sanju Madre | CEO, QPOWER | line 23 (roster), speaks line 36 | — |
| 3 | Mr. Rajes Jayaraman | CFO, QPOWER | line 24 (roster), speaks line 38 | — |
| 4 | Mrs. Jadu | Senior Vice President, Finance, QPOWER | line 25 (roster) | SPEAKER_NO_ATTRIBUTED_TURN — named on roster but never individually attributed a turn; all 55 non-opening management responses are ASR-collapsed into a generic `[MANAGEMENT]` tag (see header note, line 13) |
| 5 | Siddharth VHR | Moderator / Host, Asset (C) Meta Investments Intermediates | line 26 (roster), speaks line 32 | — |
| 6 | [MODERATOR] (operator, unnamed) | Call operator | line 30 | distinct from Host Siddharth; used for call-opening and Q&A handoffs |
| 7 | Bikar | Analyst, Unifi | line 42 (intro), 44 (turn) | — |
| 8 | Rahul Maheshwari | Analyst, Ambit Investment Advisor | line 58 (intro), 60 (turn); returns line 298 (intro), 300 (turn) | appears twice — 2 questioner slots, 1 unique analyst |
| 9 | Nimish Sundar | Analyst, "Capital" | line 74 (intro), 76 (turn) | FIRM_NAME_INCOMPLETE — firm rendered only as "Capital" throughout transcript, likely truncated by ASR |
| 10 | Dil Zaviri | Analyst, Crown Capital | line 102 (intro), 104 (turn) | — |
| 11 | Naman Parmar | Analyst, NE Investments | line 118 (intro), 120 (turn) | — |
| 12 | Ankit J | Analyst, Anand Rathi | line 150 (intro), 152 (turn) | — |
| 13 | Lowish | Analyst, Berwin Capital Management | line 170 (intro), 172 (turn) | — |
| 14 | [name garbled: "church"] | Analyst, Genuity Capital | line 198 (intro), 200 (turn) | NAME_UNCLEAR / ASR_ARTIFACT — transcript renders name as "[church]" in brackets, evidently an ASR mis-transcription |
| 15 | Nakul Gupta | Analyst, Shikari Advisers | line 212 (intro), 214 (turn) | — |
| 16 | Rohit Taparia | Analyst, individual investor | line 224 (intro), 226 (turn) | — |
| 17 | Bhavya Shah | Analyst, 3A Capital Services | line 252 (intro), 254 (turn) | — |
| 18 | Vir | Analyst, Money Guru | line 260 (intro), 262 (turn) | — |
| 19 | Rajat G | Analyst, Fortune | line 276 (intro), 278 (turn) | — |
| 20 | Akhilesh Gupta | Analyst, individual investor | line 282 (intro), 284 (turn) | — |

Management side headcount: 4 named (JMD, CEO, CFO, SVP Finance) + moderator/host support staff (2, non-management).
Analyst side headcount: 14 unique individuals across 15 questioner slots.

MGMT_ABSENCE check: no separate Chairman / full-time Managing Director role is
identified in the roster distinct from JMD Parab; Parab (co-founder/promoter,
per his own remarks on Turkey site visits and acquisition strategy) is present
and speaks first. No prior-quarter participant list was supplied to this run
(prior-quarter ledger path not provided), so a comparison for a dropped attendee
cannot be made. Not flagging MGMT_ABSENCE for lack of a baseline; downstream
agents should treat this as INDETERMINATE if promoter-attendance continuity
matters to the thesis.

---

## SECTION 2 — SPEAKER TURN LEDGER (all 143 turns, sequential)

Turn# | Line | Speaker tag | First 10 words
---|---|---|---
1 | 30 | MODERATOR | Ladies and gentlemen, good day and welcome to Quality Power
2 | 32 | HOST — Siddharth | Thank you. Good afternoon everyone. It gives us great pleasure
3 | 34 | MANAGEMENT — JMD Parab, opening remarks | Thank you and good afternoon. Welcome to the meeting. This
4 | 36 | MANAGEMENT — CEO Madre, opening remarks | Thank you Mr. Pandu and good afternoon to everyone on
5 | 38 | MANAGEMENT — CFO Jayaraman, opening remarks | Thank you Sanju and good afternoon to everyone on the
6 | 42 | MODERATOR | Thank you very much. We will now begin the question
7 | 44 | ANALYST — Bikar, Unifi | Gentlemen, hi. Good morning and congrats on strong quarter. A
8 | 46 | MANAGEMENT | Sir I may not have the year-on-year of individual company
9 | 48 | ANALYST — Bikar, Unifi | Yeah I was just trying to appreciate the CFO's comments
10 | 50 | MANAGEMENT | So the margin profile for the reactor or the coil
11 | 52 | ANALYST — Bikar, Unifi | Okay. No that helps Mr. Pandu, and one last question
12 | 54 | MANAGEMENT | So we are targeting two HVDCs — one which has
13 | 56 | ANALYST — Bikar, Unifi | Yeah thanks for that. I'll come back. Thank you.
14 | 58 | MODERATOR | Thank you. The next question is from the line of
15 | 60 | ANALYST — Rahul Maheshwari, Ambit | Good afternoon Mr. Pandu. Excellent set of results. My two
16 | 62 | MANAGEMENT | So the machinery installation is already on. I believe we
17 | 64 | ANALYST — Rahul Maheshwari, Ambit | Sure. My second question is how should we look at
18 | 66 | MANAGEMENT | Rahul this order book is slated to completion in the
19 | 68 | ANALYST — Rahul Maheshwari, Ambit | Sure. And we can expect the book to bill ratio
20 | 70 | MANAGEMENT | I think I wouldn't commit on that. But we would
21 | 72 | ANALYST — Rahul Maheshwari, Ambit | Sure. Best wishes to you and your entire team. Thank
22 | 74 | MODERATOR | Thank you. The next question is from the line of
23 | 76 | ANALYST — Nimish Sundar, Capital | Yeah hi. So a very good afternoon and congratulations on
24 | 78 | MANAGEMENT | My current guess is that we have about 60 million
25 | 80 | ANALYST — Nimish Sundar, Capital | Okay. And so the execution cycle of BESS would be
26 | 82 | MANAGEMENT | No. BESS are very fast. I think they would be
27 | 84 | ANALYST — Nimish Sundar, Capital | Oh okay. So even the working capital cycle also around
28 | 86 | MANAGEMENT | Correct. It's a fast moving product.
29 | 88 | ANALYST — Nimish Sundar, Capital | Okay sir. And just my second question on Winwin insulators.
30 | 90 | MANAGEMENT | So Nimish we are quite conservative in the way we
31 | 92 | ANALYST — Nimish Sundar, Capital | And margins would be similar to MEU as it was
32 | 94 | MANAGEMENT | Yes, I think the margin profile would stabilize in about
33 | 96 | ANALYST — Nimish Sundar, Capital | Okay. And any tentative date that you look for finalizing
34 | 98 | MANAGEMENT | I think consolidation will happen out of Q4 not before
35 | 100 | ANALYST — Nimish Sundar, Capital | Okay. Fine. Thanks a lot sir. Thank you. I'll get
36 | 102 | MODERATOR | Thank you. The next question is from the line of
37 | 104 | ANALYST — Dil Zaviri, Crown Capital | Hello. Good evening. Thank you so much for taking my
38 | 106 | MANAGEMENT | Dash I think we have guided to 20% at this
39 | 108 | ANALYST — Dil Zaviri, Crown Capital | Okay fair enough. And the overall margin guidance, what would
40 | 110 | MANAGEMENT | Please model us at 20%. High teens a bit, we
41 | 112 | ANALYST — Dil Zaviri, Crown Capital | Oh okay, that's sticking to the 50% growth in FY28
42 | 114 | MANAGEMENT | Yeah I think you can start looking at our order
43 | 116 | ANALYST — Dil Zaviri, Crown Capital | Okay. Fair enough. That's it from me. Thank you.
44 | 118 | MODERATOR | Thank you. The next question is from the line of
45 | 120 | ANALYST — Naman Parmar, NE Investments | Yeah good afternoon sir and congratulations on great set of
46 | 122 | MANAGEMENT | So the plant is being installed as we speak. I
47 | 124 | ANALYST — Naman Parmar, NE Investments | Okay got it. Secondly, on the bookkeeping side, how much
48 | 126 | MANAGEMENT | I think we had a loss of 8 crores or
49 | 128 | ANALYST — Naman Parmar, NE Investments | No, that's the hyperinflation accounting entry right, non-monetary — but
50 | 130 | MANAGEMENT | I am asking about forex currency — no, no loss,
51 | 132 | ANALYST — Naman Parmar, NE Investments | And lastly, on the margin side if you can help
52 | 134 | MANAGEMENT | MEU this quarter delivered about 18%. Our target was to
53 | 136 | ANALYST — Naman Parmar, NE Investments | Okay. And for Endoc?
54 | 138 | MANAGEMENT | Around 18% going forward for MEU. For Endoc you will
55 | 140 | ANALYST — Naman Parmar, NE Investments | Okay got it. And lastly, like you mentioned you are
56 | 142 | MANAGEMENT | I don't think we have much of debt. One second.
57 | 144 | ANALYST — Naman Parmar, NE Investments | Yeah so total raise will be how much?
58 | 146 | MANAGEMENT | We have not put numbers to it but less than
59 | 148 | ANALYST — Naman Parmar, NE Investments | Okay got it. Thank you so much for answering all
60 | 150 | MODERATOR | Thank you. The next question is from the line of
61 | 152 | ANALYST — Ankit J, Anand Rathi | Good evening sir. Congratulations for delivering very solid set of
62 | 154 | MANAGEMENT | So for MEU we have got a lot of orders
63 | 156 | ANALYST — Ankit J, Anand Rathi | Understood sir. Second would be in order to cater to
64 | 158 | MANAGEMENT | Most of the markets are inward looking by the way
65 | 160 | ANALYST — Ankit J, Anand Rathi | Understood.
66 | 162 | MANAGEMENT | Europe we are already supplying inside the Denmark grid from
67 | 164 | ANALYST — Ankit J, Anand Rathi | Got it. And if I can squeeze in a quick
68 | 166 | MANAGEMENT | So as the scale increases we are seeing the reason
69 | 168 | ANALYST — Ankit J, Anand Rathi | Understood. So glad to hear that you're moving towards that
70 | 170 | MODERATOR | Thank you. The next question is from the line of
71 | 172 | ANALYST — Lowish, Berwin Capital | Hi sir, thank you for the opportunity. My question is
72 | 174 | MANAGEMENT | Technically the commercial production can start the day we get
73 | 176 | ANALYST — Lowish, Berwin Capital | Got it. And what is the timeline for getting these
74 | 178 | MANAGEMENT | We have guided about 6 months because we have at
75 | 180 | ANALYST — Lowish, Berwin Capital | And would we need all of these audits in one
76 | 182 | MANAGEMENT | So our first focus is the orders which we are
77 | 184 | ANALYST — Lowish, Berwin Capital | Understood. And on the Winwin acquisition, I wanted to understand
78 | 186 | MANAGEMENT | Good question Lowish. This facility will take some time of
79 | 188 | ANALYST — Lowish, Berwin Capital | Good. And just one last question. If you look at
80 | 190 | MANAGEMENT | So as I said, we have been traditionally doing about
81 | 192 | ANALYST — Lowish, Berwin Capital | But just one small follow-on the standalone. Can we expect
82 | 194 | MANAGEMENT | Yeah standalone we should be good enough for that.
83 | 196 | ANALYST — Lowish, Berwin Capital | Understood. Great. Thank you sir.
84 | 198 | MODERATOR | Thank you. The next question is from the line of
85 | 200 | ANALYST — Genuity Capital | Hi sir, thanks a lot for the opportunity and congrats
86 | 202 | MANAGEMENT | I think we may attempt raising them this month before
87 | 204 | ANALYST — Genuity Capital | And on the Sangli ramp up, by when are we
88 | 206 | MANAGEMENT | So commencement is subject to the approvals from the bureaucrats.
89 | 208 | ANALYST — Genuity Capital | Okay. And how much we targeting from this?
90 | 210 | MANAGEMENT | At this moment our first focus is to get the
91 | 212 | MODERATOR | Thank you. The next question is from the line of
92 | 214 | ANALYST — Nakul Gupta, Shikari Advisers | Good afternoon. Congratulations on the set of numbers. I just
93 | 216 | MANAGEMENT | We are not able to understand your question sir, can
94 | 218 | ANALYST — Nakul Gupta, Shikari Advisers | Like if we are deducting the expense and adding it
95 | 220 | MANAGEMENT | Yes sir. You'll have to give us some time on
96 | 222 | ANALYST — Nakul Gupta, Shikari Advisers | Sir I'll do that. That's from me. Thank you.
97 | 224 | MODERATOR | Thank you. The next question is from the line of
98 | 226 | ANALYST — Rohit Taparia, individual | Good afternoon. Sir I had a couple of questions. First
99 | 228 | MANAGEMENT | So at a high technology product we really don't invest
100 | 230 | ANALYST — Rohit Taparia, individual | Okay that is for FY28?
101 | 232 | MANAGEMENT | No, you asked me the peak revenue. I gave you
102 | 234 | ANALYST — Rohit Taparia, individual | Okay. And contribution cost the same if you can provide
103 | 236 | MANAGEMENT | Give us some time. As I said the factory is
104 | 238 | ANALYST — Rohit Taparia, individual | Okay sir. And second is on Winwin specialty — when
105 | 240 | MANAGEMENT | We will start most probably consolidation Q4 this year. Without
106 | 242 | ANALYST — Rohit Taparia, individual | Okay. So and the Sangli plant, the peak revenue potential
107 | 244 | MANAGEMENT | Hello. Hello sir, for plant what would be the peak
108 | 246 | ANALYST — Rohit Taparia, individual | Yes, I can hear you. What would be the peak
109 | 248 | MANAGEMENT | As I said about 1,500 crores given day. That is
110 | 250 | ANALYST — Rohit Taparia, individual | 15%. Okay sir. Thank you.
111 | 252 | MODERATOR | Thank you. Ladies and gentlemen, in order to ensure that
112 | 254 | ANALYST — Bhavya Shah, 3A Capital | Congratulations sir for the great set of numbers. So my
113 | 256 | MANAGEMENT | Good afternoon. I'm not aware of the news that four
114 | 258 | ANALYST — Bhavya Shah, 3A Capital | Okay. Thank you so much.
115 | 260 | MODERATOR | Thank you. The next question is from the line of
116 | 262 | ANALYST — Vir, Money Guru | Hi, congratulations on the fantastic results and kudos to you
117 | 264 | MANAGEMENT | Thank you Vir. So WS stands for Westinghouse. This is
118 | 266 | ANALYST — Vir, Money Guru | Fantastic. And does the technical team stay on with WS
119 | 268 | MANAGEMENT | There are currently about 120 people in the plant. This
120 | 270 | ANALYST — Vir, Money Guru | Excellent. And you are already running the Vizag plant or
121 | 272 | MANAGEMENT | No, the Chennai is closed down. This Vizag is rebranded
122 | 274 | ANALYST — Vir, Money Guru | Excellent. All the best. Thank you.
123 | 276 | MODERATOR | Thank you. The next question is from the line of
124 | 278 | ANALYST — Rajat G, Fortune | Yeah good afternoon sir. So my question is very long-term.
125 | 280 | MANAGEMENT | I have expressed it Rajat. We would like to be
126 | 282 | MODERATOR | Thank you. The next question is from the line of
127 | 284 | ANALYST — Akhilesh Gupta, individual | Hi. Thank you so much for the opportunity and congratulations
128 | 286 | MANAGEMENT | We do not own — a couple of directors of
129 | 288 | ANALYST — Akhilesh Gupta, individual | Okay. So do we plan to get into that segment
130 | 290 | MANAGEMENT | It is a very high entry barrier segment but the
131 | 292 | ANALYST — Akhilesh Gupta, individual | Yeah. On those lines, any partnership with Hosang on the
132 | 294 | MANAGEMENT | So we are making instrument transformers, we are also getting
133 | 296 | ANALYST — Akhilesh Gupta, individual | Thank you so much sir. That's all.
134 | 298 | MODERATOR | Thank you. Due to paucity of time we take one
135 | 300 | ANALYST — Rahul Maheshwari, Ambit | Thank you once again for giving me the opportunity. Just
136 | 302 | MANAGEMENT | I think the highest growth will come from power electronic
137 | 304 | ANALYST — Rahul Maheshwari, Ambit | Yeah but power products growth will be lower than the
138 | 306 | MANAGEMENT | It is not only the scope, it is also the
139 | 308 | ANALYST — Rahul Maheshwari, Ambit | And just last question from my end. You being the
140 | 310 | MANAGEMENT | We are not one product, we are making about 12
141 | 312 | ANALYST — Rahul Maheshwari, Ambit | Thank you once again and best wishes to the entire
142 | 314 | MANAGEMENT | Thank you.
143 | 316 | MODERATOR | Thank you. Thank you everyone for joining this conference call

Tally: MODERATOR 17, HOST 1, MANAGEMENT 58 (3 opening remarks individually
attributed to JMD/CEO/CFO + 55 generic Q&A responses), ANALYST 67. 17+1+58+67 = 143.
Management/Q&A ratio by turn count: 58 of 143 turns (40.6%) are management
speech; of those, 55 of 58 (94.8%) occur inside the Q&A section (turns 8-142),
i.e. the overwhelming majority of management airtime by turn-count is Q&A
response, consistent with the "60% of effort on Q&A" house convention this
ledger exists to make auditable — exact word-count/time-based verification is
out of scope for A2 (turn-count proxy only; flag for A4 if a stricter test is
needed).

ATTRIBUTION_AMBIGUOUS: of the 58 MANAGEMENT turns, only 3 (turns 3, 4, 5 —
opening remarks) are individually attributed to JMD Parab / CEO Madre / CFO
Jayaraman by name. All 55 Q&A-section MANAGEMENT turns (turns 8, 10, 12, ... 140)
carry only the generic `[MANAGEMENT]` tag per the extract header's stated
convention (line 13). Any downstream claim of "the CFO said X in Q&A" cannot be
verified against this transcript at the individual-turn level; it can only be
verified for the three opening-remarks turns.

---

## SECTION 3 — Q&A QUESTIONER SLOT LEDGER (15 slots, 14 unique analysts)

Slot | Analyst | Firm | First turn# / line | Moderator handoff line | Topics (summary) | Flags
---|---|---|---|---|---|---
1 | Bikar | Unifi | turn 7 / line 44 | line 42 | YoY growth split (QP/MEU/Endoc); margin-pressure rehash for Q3; order-book reflecting enlarged capacity timing | REPEAT_QUESTION (margin guidance; order-book execution timing)
2 | Rahul Maheshwari | Ambit Investment Advisor | turn 15 / line 60 | line 58 | Sangli oil facility & HVDC magnet wire commissioning + peak asset turns; order-book execution staging; book-to-bill sustainability | REPEAT_QUESTION (Sangli timeline; order-book execution)
3 | Nimish Sundar | Capital | turn 23 / line 76 | line 74 | BESS/PCS current capacity & Endoc facility scalability; BESS execution cycle; BESS working-capital cycle; Winwin revenue/margin/use; margin trajectory; acquisition consolidation date | FIRM_NAME_INCOMPLETE; REPEAT_QUESTION (Winwin/WS insulators)
4 | Dil Zaviri | Crown Capital | turn 37 / line 104 | line 102 | FY27 revenue guidance (1,400 cr ask); overall margin guidance; FY28 50% growth confirmation | REPEAT_QUESTION (margin guidance)
5 | Naman Parmar | NE Investments | turn 45 / line 120 | line 118 | GIS / grading capacitor product update; forex gain in other income (confused with hyperinflation entry); MEU margin; Endoc margin; capital raise purpose & current debt; total raise quantum | REPEAT_QUESTION (margin guidance; capital raise); CONFUSED_RESPONSE (turns 48-50 / lines 126-130)
6 | Ankit J | Anand Rathi | turn 61 / line 152 | line 150 | Global product reception (Europe/US) & India capacity implication; European localization/manufacturing need; procurement consolidation margin accretion | —
7 | Lowish | Berwin Capital Management | turn 71 / line 172 | line 170 | Sangli delay reasons & commercial-production timeline; approvals timeline; audit sequencing (all-at-once vs incremental); Winwin acquisition rationale & turnaround; standalone gross-margin sustainability; standalone EBITDA margin confirmation | REPEAT_QUESTION (Sangli timeline; Winwin/WS insulators; margin guidance)
8 | [name unclear — "church"] | Genuity Capital | turn 85 / line 200 | line 198 | Fund-raise (~500 cr) timeline; Sangli ramp-up timing; Sangli revenue target | NAME_UNCLEAR / ASR_ARTIFACT; REPEAT_QUESTION (capital raise; Sangli timeline)
9 | Nakul Gupta | Shikari Advisers | turn 92 / line 214 | line 212 | Ind AS 29 hyperinflation adjustment — pre-adjustment Turkey asset base (management could not answer live, took the question offline) | UNANSWERED_LIVE (management deferred to written follow-up, line 220)
10 | Rohit Taparia | individual investor | turn 98 / line 226 | line 224 | Endoc facility peak revenue potential & FY28 contribution; contribution-cost guidance; Winwin timing & peak contribution with/without capex; Sangli plant peak revenue potential | REPEAT_QUESTION (Sangli peak revenue; Winwin/WS insulators)
11 | Bhavya Shah | 3A Capital Services | turn 112 / line 254 | line 252 | Impact of 4 Chinese companies newly allowed to bid on HVDC contracts | —
12 | Vir | Money Guru | turn 116 / line 262 | line 260 | WS Insulators company history/rationale for acquisition; technical team retention; Vizag vs Chennai plant status | REPEAT_QUESTION (Winwin/WS insulators)
13 | Rajat G | Fortune | turn 124 / line 278 | line 276 | Long-term (2030/2035) vision, 10,000 cr revenue runway framing | —
14 | Akhilesh Gupta | individual investor | turn 127 / line 284 | line 282 | Invitas (Endoc-group software co.) licensing question; QPOWER's own software-segment entry plans; Hosang/GIS instrument-transformer partnership | —
15 | Rahul Maheshwari (2nd appearance) | Ambit Investment Advisor | turn 135 / line 300 | line 298 (explicitly flagged by moderator as "last question... due to paucity of time") | Growth trajectory by segment (power products / power electronics / ancillaries) & mix shift; relative growth power products vs power electronics; biggest component shortage in supply chain | REPEAT_QUESTION (analyst re-asking within own slot set; also topically close to slot-1 growth-split question)

Slot count: 15. Unique analysts: 14 (Rahul Maheshwari counted once, occupies
slots 2 and 15). This matches the task's stated expectation exactly.

---

## SECTION 4 — INDIVIDUAL QUESTION SWEEP (informational; 49 distinct questions inside the 15 slots)

This finer sweep is not part of GATE A2 (which is anchored to the 15-slot
count per task instruction) but is provided so A3/A4 can cite a specific
question rather than an entire multi-question slot.

Q# | Slot | Turn# / line | Analyst | Question topic | Flags
---|---|---|---|---|---
1 | 1 | 7 / 44 | Bikar | YoY revenue growth split QP vs MEU vs Endoc | —
2 | 1 | 7,9 / 44,48 | Bikar | Rehash of CFO's Q3 margin-pressure caution, exact line items | REPEAT_QUESTION
3 | 1 | 11 / 52 | Bikar | When will order book reflect enlarged capacity (given 4-6 month execution cycle) | REPEAT_QUESTION
4 | 2 | 15 / 60 | Rahul Maheshwari | Sangli oil facility & HVDC magnet-wire commissioning timing + peak asset turns | REPEAT_QUESTION
5 | 2 | 17 / 64 | Rahul Maheshwari | Staged order-book execution timeline | REPEAT_QUESTION
6 | 2 | 19 / 68 | Rahul Maheshwari | Book-to-bill ratio sustainability next 1-2 years | —
7 | 3 | 23 / 76 | Nimish Sundar | BESS current capacity (volume/revenue) + Endoc new facility scalability | —
8 | 3 | 25 / 80 | Nimish Sundar | BESS execution cycle length (vs 12-15 month assumption) | —
9 | 3 | 27 / 84 | Nimish Sundar | BESS working-capital cycle | —
10 | 3 | 29 / 88 | Nimish Sundar | Winwin insulators revenue/margin, internal vs external use | REPEAT_QUESTION
11 | 3 | 31 / 92 | Nimish Sundar | Winwin margin trajectory (similar to MEU initially?) | REPEAT_QUESTION
12 | 3 | 33 / 96 | Nimish Sundar | Tentative acquisition-finalization/consolidation date | REPEAT_QUESTION
13 | 4 | 37 / 104 | Dil Zaviri | FY27 revenue guidance; can QPOWER reach 1,400 cr | —
14 | 4 | 39 / 108 | Dil Zaviri | Overall margin guidance | REPEAT_QUESTION
15 | 4 | 41 / 112 | Dil Zaviri | Confirm 50% growth framing holds for FY28 | —
16 | 5 | 45 / 120 | Naman Parmar | GIS and grading-capacitor product status update | —
17 | 5 | 47,49 / 124,128 | Naman Parmar | Forex currency gain/loss in other income (clarifying vs hyperinflation entry) | CONFUSED_RESPONSE
18 | 5 | 51 / 132 | Naman Parmar | MEU margin this quarter | REPEAT_QUESTION
19 | 5 | 53 / 136 | Naman Parmar | Endoc margin | REPEAT_QUESTION
20 | 5 | 55 / 140 | Naman Parmar | Capital raise purpose and current debt structure | REPEAT_QUESTION
21 | 5 | 57 / 144 | Naman Parmar | Total quantum of capital raise | REPEAT_QUESTION
22 | 6 | 61 / 152 | Ankit J | Global product reception (Europe vs US) and India capacity implication | —
23 | 6 | 63 / 156 | Ankit J | European localization / local manufacturing requirement | —
24 | 6 | 67 / 164 | Ankit J | Group procurement consolidation — margin accretion potential | —
25 | 7 | 71 / 172 | Lowish | Reason for Sangli delay; commercial-production start timing | REPEAT_QUESTION
26 | 7 | 73 / 176 | Lowish | Timeline for regulatory approvals | REPEAT_QUESTION
27 | 7 | 75 / 180 | Lowish | Whether all audits needed together or can ramp incrementally | —
28 | 7 | 77 / 184 | Lowish | Winwin acquisition rationale and turnaround plan | REPEAT_QUESTION
29 | 7 | 79 / 188 | Lowish | Standalone gross-margin increase — sustainable? | REPEAT_QUESTION
30 | 7 | 81 / 192 | Lowish | Confirm ~20% standalone EBITDA margin expectation | REPEAT_QUESTION
31 | 8 | 85 / 200 | [Genuity analyst] | Fund-raise (~500 cr) timeline | REPEAT_QUESTION
32 | 8 | 87 / 204 | [Genuity analyst] | Sangli ramp-up commencement timing | REPEAT_QUESTION
33 | 8 | 89 / 208 | [Genuity analyst] | Sangli revenue target | —
34 | 9 | 92,94 / 214,218 | Nakul Gupta | Ind AS 29 — pre-adjustment Turkey asset base figure | UNANSWERED_LIVE
35 | 10 | 98,100 / 226,230 | Rohit Taparia | Endoc facility peak revenue potential and FY28 contribution | —
36 | 10 | 102 / 234 | Rohit Taparia | Endoc contribution-cost guidance for FY28 | —
37 | 10 | 104 / 238 | Rohit Taparia | Winwin — when contributing, peak contribution with/without capex | REPEAT_QUESTION
38 | 10 | 106,108 / 242,246 | Rohit Taparia | Sangli plant peak revenue potential | REPEAT_QUESTION
39 | 11 | 112 / 254 | Bhavya Shah | Impact of 4 Chinese companies allowed to bid on HVDC contracts | —
40 | 12 | 116 / 262 | Vir | WS Insulators company history and acquisition rationale | REPEAT_QUESTION
41 | 12 | 118 / 266 | Vir | Does WS technical/R&D team stay on | —
42 | 12 | 120 / 270 | Vir | Vizag vs Chennai plant operating status | —
43 | 13 | 124 / 278 | Rajat G | 2030/2035 vision, 10,000 cr revenue runway | —
44 | 14 | 127 / 284 | Akhilesh Gupta | Invitas (Endoc-group software co.) licensing arrangement | —
45 | 14 | 129 / 288 | Akhilesh Gupta | QPOWER's own plans to enter software segment | —
46 | 14 | 131 / 292 | Akhilesh Gupta | Hosang / GIS instrument-transformer partnership expansion | —
47 | 15 | 135 / 300 | Rahul Maheshwari | Segment growth trajectory (power products / power electronics / ancillaries) and mix shift | —
48 | 15 | 137 / 304 | Rahul Maheshwari | Will power products growth lag power electronics | —
49 | 15 | 139 / 308 | Rahul Maheshwari | Single biggest component shortage driving supply-chain extension | —

---

## SECTION 5 — QUANTIFIED CLAIMS LEDGER (every number/metric spoken, management + analyst-asserted)

All rows carry (turn#, line#). Speaker column distinguishes MANAGEMENT (gated,
feeds GATE A2 mgmt_numbers test) from ANALYST (asserted in the question, not
management-confirmed — retained for the Role 5 arithmetic-consistency check).

### 5A. Opening remarks — CFO Jayaraman's structured results (turn 5, line 38) — richest single turn

# | Metric | Value | Speaker | Turn/Line | Flags
---|---|---|---|---|---
1 | Revenue, the quarter | Rs 256.4 cr | CFO Jayaraman | 5/38 | —
2 | Gross profit | Rs 121 cr | CFO Jayaraman | 5/38 | —
3 | Gross margin, current quarter | 47.2% | CFO Jayaraman | 5/38 | —
4 | Gross margin, prior-year quarter (implied YoY comp) | 44.6% | CFO Jayaraman | 5/38 | —
5 | Reported EBITDA | Rs 64.7 cr | CFO Jayaraman | 5/38 | —
6 | Reported EBITDA margin | 25.2% | CFO Jayaraman | 5/38 | —
7 | Profit before tax (PBT), reported | Rs 59.4 cr | CFO Jayaraman | 5/38 | —
8 | Profit after tax (PAT), reported | Rs 46.7 cr | CFO Jayaraman | 5/38 | —
9 | EPS, current quarter | Rs 4.66 | CFO Jayaraman | 5/38 | —
10 | EPS, prior-year comp | Rs 3.12 | CFO Jayaraman | 5/38 | —
11 | Net monetary loss, hyperinflation accounting (Turkey, Ind AS 29), included in other expenses | Rs 7.82 cr | CFO Jayaraman | 5/38 | non-cash per CFO
12 | EBITDA, ex-hyperinflation adjustment | Rs 72.5 cr | CFO Jayaraman | 5/38 | —
13 | EBITDA margin, ex-hyperinflation adjustment | 28.3% | CFO Jayaraman | 5/38 | —
14 | PBT, ex-hyperinflation adjustment | Rs 67.2 cr | CFO Jayaraman | 5/38 | —
15 | PAT, ex-hyperinflation adjustment | Rs 54.5 cr | CFO Jayaraman | 5/38 | —
16 | Volume-discount benefit from group-level procurement, this quarter | ~Rs 3 cr | CFO Jayaraman | 5/38 | approximate ("Approximately")
17 | Consolidated order book, quarter-end (30 Jun) | Rs 1,945 cr | CFO Jayaraman | 5/38 | restated by JMD Parab at turn 3/line 34 also — consistent
18 | Order book vs last year's revenue | ~1.9x | CFO Jayaraman | 5/38 | consistent with JMD's statement, turn 3/line 34
19 | Order book — Endoc | Rs 801 cr | CFO Jayaraman | 5/38 | see ARITH_DELTA note below
20 | Order book — MEU | Rs 585 cr | CFO Jayaraman | 5/38 | see ARITH_DELTA note below
21 | Order book — Quality Power standalone | Rs 553 cr | CFO Jayaraman | 5/38 | see ARITH_DELTA note below
22 | Finance costs | Rs 1.4 cr | CFO Jayaraman | 5/38 | —
23 | Depreciation, current quarter | Rs 3.9 cr | CFO Jayaraman | 5/38 | —
24 | Interim dividend declared | Rs 0.25 / share | CFO Jayaraman | 5/38 | —
25 | Winwin Specialty Insulators — enterprise value (EV) of the transaction | ~Rs 315 cr | CFO Jayaraman | 5/38 | the sole EV figure disclosed for the WS/Winwin deal

**ARITH_DELTA flag (rows 19-21 vs row 17):** Endoc (801) + MEU (585) + QPOWER
standalone (553) = Rs 1,939 cr, against the stated consolidated total of Rs
1,945 cr (row 17) — a Rs 6 cr (0.3%) gap. Immaterial in magnitude but flagged
for Role 5 to check against the filing baseline (could be a residual/holdco
adjustment, WS/other-entity order book not separately broken out, or a
rounding artifact in the spoken figures).

### 5B. Q&A — management-spoken figures (with turn/line), grouped by topic

# | Metric | Value | Turn/Line | Flags
---|---|---|---|---
26 | Quality Power standalone revenue, YoY comparison | from Rs 37 cr to Rs 69 cr | 8/46 | ESTIMATE_CAVEAT — management stated "I may not have the exact year-on-year... roughly the estimates"
27 | MEU revenue, YoY comparison | from ~Rs 60 cr to ~Rs 83 cr | 8/46 | ESTIMATE_CAVEAT (same caveat)
28 | Endoc revenue contribution, this quarter | ~Rs 107 cr | 8/46 | ESTIMATE_CAVEAT ("I don't remember exactly")
29 | Sum check: 69+83+107 = 259 cr vs reported total revenue Rs 256.4 cr (row 1) | delta ~Rs 2.6 cr | 8/46 vs 5/38 | ARITH_DELTA (minor; management explicitly caveated the segment figures as rough)
30 | MEU raw-material pass-through cycle time | ~8 weeks | 10/50 | —
31 | Quality Power aluminium input lag to production | ~4-5 months (CFO said "6 months later" in general, MANAGEMENT specifies "four or five months") | 10/50 | internal wording inconsistency: "about 6 months later" vs "four or five months later" in the same turn — flag INTERNAL_INCONSISTENCY
32 | Coil products business — stable margin guidance | ~20% | 10/50 | —
33 | Coil products — orders booked, margin level | in excess of 25% | 10/50 | —
34 | HVDC projects being pursued | two (one already awarded, timing Q3/Q4; one near tender completion) | 12/54 | —
35 | Statcom projects in discussion, across US/Europe/Australia | about half a dozen | 12/54 | spelled-out quantity (non-gated numeral turn, still itemized)
36 | Statcoms already secured, US | a couple | 12/54 | spelled-out/approximate
37 | Data-center opportunity bid sizes | ~$100 million (bids) | 12/54 | USD figure
38 | Data-center delivery period | ~12 months | 12/54 | —
39 | Timeline to stabilize new facility before taking more orders | ~3 months | 12/54 | —
40 | Sangli facility physical scale | ~600 m corner-to-corner (walking) | 12/54 | qualitative-scale figure
41 | Existing factories' order-book cover | "more than two years... close to two years" of order book at current capacity | 12/54 | —
42 | Initial ISO/OSHAS audit completion timeline (Sangli) | ~1 month | 16/62 | —
43 | Global customer audits expected at Sangli before full volume | ~60 audits | 16/62 | restated later at 74/178 as "about 60 audits" — consistent
44 | Timeline from facility opening to global-audit completion | ~6 months | 16/62 | restated at 74/178 — consistent
45 | Sangli facility peak asset turnover | Rs 1,500-1,800 cr | 16/62 | narrowed later to "about 1,500 crores" at 109/248 — flag GUIDANCE_NARROWING
46 | HVDC magnet-wire facility — trial-run duration | ~3 months | 16/62 | —
47 | HVDC magnet-wire facility — stabilization period | 3 to 5 months | 16/62 | —
48 | HVDC magnet-wire facility — full production target | Q4 (FY27) | 16/62 | —
49 | Order-book execution timeline (aggregate) | ~15 months | 18/66 | —
50 | Turkey (Endoc) facility capacity | 4 GW | 20/70 | spelled-out numeral ("4 GW") captured via digit
51 | Order secured against that capacity | ~1 GW | 20/70 | —
52 | BESS/PCS pipeline, current | ~$60 million | 24/78 | USD figure
53 | BESS/PCS pipeline, additional expected next 12 months | ~$40 million | 24/78 | USD figure
54 | BESS/PCS — prior guidance reference | at least $50 million of business | 24/78 | USD figure; internally consistent with rows 52+53 summing above $50mn baseline
55 | BESS execution cycle | 6 to 9 months | 26/82 | —
56 | Winwin/WS internal (captive) insulator demand | ~Rs 40-45 cr/year | 30/90 | —
57 | Winwin/WS insulator order target, next 9 months | ~Rs 200 cr | 30/90 | —
58 | Winwin/WS type-test completion | up to 220 KV completed; 765 KV expected in next few months | 30/90 | —
59 | Winwin/WS factory initial revenue potential | Rs 300-400 cr/year | 30/90 | —
60 | Winwin/WS composite insulator type test reference | KEMA Netherlands, 400 KV | 30/90 | —
61 | Winwin/WS margin stabilization timeline | ~4 quarters from acquisition date | 32/94 | —
62 | Winwin/WS current margin range | 15%-25% | 32/94 | wide/uncertain range, management flagged the gap itself
63 | Winwin/WS consolidation timing | Q4 (FY27) | 34/98 | restated at 105/240 — consistent
64 | FY27 revenue growth guidance | 20% | 38/106 | reiterated multiple times through the call (rows 65, 90 below)
65 | FY27 margin guidance | ~20% ("high teens a bit") | 40/110 | —
66 | GIS component roadmap | 220 KV first, then 400/765 KV | 46/122 | timeline: "next say one year's time"
67 | Forex or hyperinflation loss, other income (ambiguous) | Rs 8 cr or Rs 7.5 cr, then "no loss, nothing" | 48/126, 50/130 | CONFUSED_RESPONSE — contradicts the CFO's precise Rs 7.82 cr hyperinflation-loss figure at 5/38; unclear if this is the same item restated imprecisely or a genuinely separate (and then denied) forex line
68 | MEU margin, this quarter | ~18% | 52/134 | —
69 | MEU margin, internal target | 22-23% | 52/134 | missed vs actual ~18% (row 68)
70 | MEU margin, revised forward guidance | ~18% (up from "above 15%" prior guidance) | 52/134 | GUIDANCE_REVISION — guidance raised intra-call
71 | Endoc current product-line margins (satcoms/SVCs/automation) | ~25% | 54/138 | —
72 | Total group debt, prior quarter-end | ~Rs 23 cr | 56/142 | —
73 | Proposed capex at Winwin/WS location | Rs 50 cr | 56/142 | CAPEX figure
74 | Land available at Winwin/WS campus | ~40 acres | 56/142 | —
75 | Total capital raise contemplated | less than Rs 500 cr | 58/146 | —
76 | MEU market share language | "one in two" high-voltage instrument transformers in India | 62/154 | qualitative ~50% share framing
77 | Decision timeline for Turkey vs Vizag export facility | 6-7 months | 62/154 | —
78 | Group procurement scale example — MEU aluminium castings spend | Rs 15-20 cr | 68/166 | —
79 | Group procurement scale example — WS (at ~Rs 250 cr revenue) casting spend | ~Rs 50 cr | 68/166 | —
80 | Group procurement scale example — Sukrut casting spend | ~Rs 10 cr | 68/166 | —
81 | Timeline to find procurement "equilibrium" | next 2 years | 68/166 | —
82 | Amount paid for WS/Winwin business (distinct from EV, row 25) | ~Rs 50-60 cr | 78/186 | flag EV_VS_PRICE_GAP — CFO's Rs 315 cr "enterprise value" (row 25) vs management's later "amount of money I paid for the business per se is about 50-60 crores" (this row); management explains the gap as land/asset value vs cash paid, but the two figures need explicit reconciliation by A3/A4
83 | Global insulator supplier count | India: ~4-5 players; globally: ~8-9 more | 78/186 | —
84 | WS/Winwin facility land use | 8 acres of the campus is the operating facility (vs ~40 acres total, row 74) | 78/186 | —
85 | Payback timeline management expects on WS/Winwin | ~2 years | 78/186 | —
86 | Standalone gross margin, historical run-rate | ~25%, last six quarters | 80/190 | —
87 | Standalone EBITDA margin, near-term expectation | ~20% | 82/194 | confirms analyst's proposed figure at 81/192
88 | Fundraise roadshow start date | 20th of this month (August 2026, per header extraction date) | 86/202 | —
89 | Sangli revenue-trickle timeline | Q3 initial, Q4 more visible | 88/206 | restates JMD's Q3 commissioning language (turn 3/34) and CFO's Q3 margin-moderation caution (turn 5/38)
90 | Sangli/FY27 target reiteration | "stick to the 20" (% growth guidance) | 90/210 | consistent with row 64
91 | Endoc PCS facility capex, current | ~$2 million | 99/228 | USD figure, CAPEX
92 | Endoc PCS facility, incremental spend flagged | ~$1 million | 99/228 | USD figure, CAPEX
93 | Endoc PCS facility peak revenue potential | ~$70-80 million | 99/228 | USD figure
94 | Winwin/WS peak contribution, without further capex | Rs 250-300 cr | 105/240 | —
95 | Winwin/WS peak contribution, with capex | Rs 450-500 cr | 105/240 | —
96 | Sangli plant peak revenue potential (restated) | ~Rs 1,500 cr | 109/248 | narrower than the Rs 1,500-1,800 cr range given at 16/62 — GUIDANCE_NARROWING (see row 45)
97 | FY28 guidance figure appended to Sangli answer | 15% | 109/248 | ambiguous whether this refers to FY28 revenue growth or margin — needs A3/A4 disambiguation; distinct from the 20% FY27 growth guidance (row 64) and could be read against the analyst's "50% growth FY28" framing at Q&A row 15 (turn 41/112, never explicitly confirmed by management)
98 | Local-sourcing-content requirement cited for newly permitted Chinese HVDC bidders | 60-70% domestic content | 113/256 | —
99 | Duration Chinese-approved factories have been largely dormant | ~7 years | 113/256 | —
100 | WS/Westinghouse origin | started 1960s, Chennai | 117/264 | historical, non-financial
101 | WS historical product reach | up to 800 KV | 117/264 | —
102 | Cyclone write-off at original WS Chennai-to-Vizag shift | ~Rs 240 cr | 117/264 | —
103 | Plant idle period before new investors | ~6-7 years | 117/264 | —
104 | New investor renovation spend, pre-QPOWER | ~Rs 150 cr | 117/264 | —
105 | Prior owner's daily cash burn (gas crisis) | ~Rs 2 cr/day | 117/264 | —
106 | WS/Winwin current headcount | ~120 people | 119/268 | —
107 | WS/Winwin approvals footprint | approved in over 15 countries | 119/268 | —
108 | CTC/aluminium-wire ancillary business target | at least Rs 500 cr (aluminium wire) | 136/302 | distinct from the "less than Rs 500 cr" total capital raise figure at row 75 — same round number, different context, flag NUMBER_REUSE for reader clarity (not an inconsistency, just worth distinguishing)
109 | CTC ancillary business — copper-wire equivalent framing | Rs 1,500-1,800 cr (in copper-wire terms) | 136/302 | same figure set as Sangli asset-turnover potential (rows 45/96) — coincidental reuse, flag NUMBER_REUSE
110 | Number of distinct product lines across the group | 12-13 products | 140/310 | scope statement, non-financial

### 5C. Analyst-asserted figures (not management-confirmed; retained for Role 5 cross-check)

# | Metric | Value asserted | Speaker | Turn/Line | Flags
---|---|---|---|---|---
111 | FY27 revenue target proposed by analyst | ~Rs 1,400 cr | Dil Zaviri | 37/104 | management did not confirm or deny this figure directly (response at 38/106 reiterates "20%" growth guidance only) — UNCONFIRMED_ANALYST_FIGURE
112 | FY28 growth framing proposed by analyst | 50% growth | Dil Zaviri | 41/112 | management response (42/114) is non-committal ("you can start looking at our order book... start mixing the data") — UNCONFIRMED_ANALYST_FIGURE
113 | Long-term revenue runway framing proposed by analyst | 10,000 cr revenue (2030/2035 horizon) | Rajat G | 124/278 | management's answer (125/280) addresses strategic positioning (Hitachi analogue) without confirming/denying the number — UNCONFIRMED_ANALYST_FIGURE
114 | Execution-cycle assumption proposed by analyst | 4 to 6 months (typical order-to-execution) | Bikar | 7/44 | used as the premise for a follow-up question; not independently confirmed by management in that exchange
115 | BESS execution-cycle assumption proposed by analyst | 12 to 15 months | Nimish Sundar | 25/80 | management corrected this to 6-9 months (row 55) — good example of a management correction of an analyst's premise, worth noting for A4 rather than flagging as inconsistency

Total quantified-claims rows in Section 5: 115 (25 in 5A + 85 in 5B + 5 in 5C).
This is the informational, granular figure referenced in the count-test
methodology note; the GATE A2 mgmt_numbers gate itself rests on the coarser,
mechanically reconciled 38-turn figure above.

---

## SECTION 6 — FORWARD-COMMITMENT AND HEDGE PHRASES (best-effort sweep; A3 owns the full lexicon)

Type | Phrase (paraphrase kept close to verbatim) | Turn/Line | Note
---|---|---|---
Commitment | "We closed this quarter with an order book of 1945 crores" | 3/34 | factual/backward-looking, not forward, included for context
Commitment | "Every executable order currently in our order book has been booked above the margin guidance communicated to the market" | 5/38 | strong forward-looking pricing-discipline claim
Hedge | "We therefore expect some temporary moderation in standalone margins particularly in Q3" | 5/38 | explicit guidance walk-back embedded in opening remarks
Hedge | "This is more of a cautionary word rather than a real world scenario at this point" | 10/50 | explicit hedge on the Q3 margin caution
Hedge | "I think I wouldn't commit on that. But we would try our best." | 20/70 | book-to-bill sustainability question, explicit non-commitment
Commitment | "Getting orders is not a worry at this moment for us... we could get in more if you're able to deliver more" | 12/54 | strong demand-confidence claim
Hedge | "I don't want to commit things I cannot honor. I would rather err in caution than be aggressive on this." | 38/106 | explicit hedge on FY27 revenue guidance
Commitment | "Please model us at 20%. ... we will always try to deliver better." | 40/110 | guidance reiteration with upside framing
Hedge | "I wouldn't bet too much on ancillary at this moment" | 136/302 | hedge on ancillary-segment contribution
Hedge | "Please don't build your castle based on these numbers. Please build your castle based on the numbers we've guided." | 80/190 | explicit hedge against extrapolating one quarter's gross margin
Hedge | "At this moment I will be shooting in the dark when I give you a number" | 103/236 | explicit refusal to guide on Endoc contribution cost
Hedge | "We have not put numbers to it but less than 500 crores" | 58/146 | soft/unquantified capital-raise commitment
Commitment | "I think in the next two years I should be able to collect my cheque back" | 78/186 | payback-period forward claim on WS/Winwin
Commitment | "We believe we will start opening up... to get in more orders once we are comfortable" | 16/62 | forward capacity-ramp commitment
Hedge | "We are not able to understand your question sir" / deferred to written follow-up | 93/216, 95/220 | non-answer, procedural hedge (Ind AS 29 question)
Hedge | "Give us some time. ... I will be shooting in the dark" | 103/236 | duplicate-topic hedge, Endoc contribution cost
Commitment | "I believe we should be increasing the guidance of MEU above 15%... revised guidance for MEU would be around 18%" | 52/134 | live guidance revision, upward
Hedge | "The gap is very large because we still don't have things under our control. Once we have in control, we will narrow down the margin percentage." | 32/94 | hedge on Winwin/WS margin range (15-25%)

This sweep is representative, not exhaustive; A3's forensic lexicon pass should
be treated as authoritative for completeness on this dimension.

---

## SECTION 7 — CATEGORIES NOT APPLICABLE TO THIS DOCTYPE

The following A2 enumeration categories from the agent prompt's "RESULTS FILING"
checklist do not apply to a concall transcript and are recorded as N/A rather
than silently omitted, per the "never drop a nil row" principle applied at the
category level: numbered notes, financial-table line items (incl. zero/nil/dash
standing items), Board Outcome letter agenda items, annexures/director profiles,
auditor report paragraphs, consolidation-entity list, digital signature blocks.
None of these disclosure types exist in a transcript; this is stated explicitly
so a downstream reviewer does not mistake the absence for a missed sweep.

---

## FLAGS SUMMARY (all flags raised in this ledger)

- REPEAT_QUESTION — margin guidance (5 analysts), Sangli facility timeline/peak
  revenue (4 analysts), Winwin/WS insulators (4 analysts), capital raise
  purpose/timeline (2 analysts), order-book execution timing (2 analysts)
- FIRM_NAME_INCOMPLETE — Nimish Sundar's firm rendered only as "Capital"
- NAME_UNCLEAR / ASR_ARTIFACT — Genuity Capital questioner's name rendered as "[church]"
- SPEAKER_NO_ATTRIBUTED_TURN — Mrs. Jadu (SVP Finance) on roster, never individually attributed a turn
- ATTRIBUTION_AMBIGUOUS — 55 of 58 MANAGEMENT turns (all of Q&A) not attributed to a named individual
- CONFUSED_RESPONSE — forex vs hyperinflation loss exchange, turns 48-50 / lines 126-130
- UNANSWERED_LIVE — Ind AS 29 Turkey asset-base question, turn 92/94, deferred to written follow-up
- INTERNAL_INCONSISTENCY — aluminium input-lag stated as "6 months" then "four or five months" within the same turn, 10/50
- ARITH_DELTA — order-book components (801+585+553=1,939) vs stated total (1,945), Rs 6 cr gap; also YoY segment revenue sum (259) vs reported total revenue (256.4), Rs 2.6 cr gap (management-caveated as rough estimates)
- ESTIMATE_CAVEAT — YoY segment revenue figures, turn 8/46, explicitly flagged by management as rough/approximate
- GUIDANCE_NARROWING — Sangli peak asset turnover narrated as Rs 1,500-1,800 cr (16/62) then narrowed to ~Rs 1,500 cr (109/248)
- GUIDANCE_REVISION — MEU margin guidance raised intra-call from "above 15%" to "~18%", 52/134
- EV_VS_PRICE_GAP — Winwin/WS "enterprise value" of ~Rs 315 cr (CFO, 5/38) vs "amount paid for the business" of ~Rs 50-60 cr (management, 78/186); needs explicit reconciliation
- NUMBER_REUSE — "Rs 500 cr" used for both total capital raise (58/146) and CTC/aluminium-wire ancillary target (136/302); "Rs 1,500-1,800 cr" used for both Sangli asset turnover (16/62, 96/248) and CTC copper-wire equivalent framing (136/302) — coincidental, flagged for clarity only
- UNCONFIRMED_ANALYST_FIGURE — Rs 1,400 cr FY27 revenue ask (37/104), 50% FY28 growth framing (41/112), 10,000 cr long-term revenue runway (124/278) — none explicitly confirmed by management

---
Output ledger path: runs/qpower-q1fy27/work/ledger_concall_qpower_q1fy27.md
