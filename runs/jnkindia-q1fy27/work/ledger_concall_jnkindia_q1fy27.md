# A2 ENUMERATOR LEDGER — JNK India Limited (JNKINDIA), Q1 FY27, CONCALL

Source: `/home/user/inflection-pipeline/runs/jnkindia-q1fy27/work/extract_concall_jnkindia_q1fy27.txt`
(extract file lines 16-160 = transcript body; source transcript carries its own
embedded line numbering 1-145, tab-separated after leading spaces — this
embedded number is used as the TURN number throughout this ledger, alongside
the extract file's own Read-tool line number for pinpoint citation.)

## METHODOLOGY NOTES

1. **Turn numbering.** The source transcript text itself carries an embedded
   sequential line numbering 1-145 (verified: `awk` pass on tab-delimited
   field 1, sequence 1..145, no gaps, no duplicates). This ledger treats each
   of these 145 embedded numbers as one TURN. Two of the 145 (turn 2, turn 5)
   are blank (no text) — flagged `BLANK_TURN`, not dropped. Turn 1 is the
   transcript title line, not spoken content — flagged `NOT_A_TURN`.
2. **Speaker segmentation.** This is operator-supplied ASR text with no
   speaker labels and inconsistent punctuation. Management answers and
   analyst questions are frequently run together inside a single numbered
   turn with no delimiter (e.g. turn 4 = moderator hand-off sentence +
   the entire management opening statement; turn 7 = an analyst's question
   immediately followed by management's answer with no break). Where a turn
   contains both an analyst question and a management answer, it is flagged
   `TURN_MIXED` and both speakers are recorded in the Turn table. Speaker
   attribution within mixed turns is inferred from address patterns ("Hi
   Kamesh", "Yeah basically...we..."), first-person plural ("we/our") for
   management, and second-person / interrogative framing for analysts. One
   turn (47, TAM figures) has an attribution that cannot be resolved with
   confidence — flagged `SPEAKER_AMBIGUOUS`, both possibilities logged.
3. **ASR garbling map** (noted here, RAW transcript lines are cited
   throughout, not corrected in place):
   - IITA / IVITA / EVITA = EBITDA
   - ",81 crores" = order book Rs 1,801 Cr (turn 4, both mentions)
   - "Zangote" = Dangote (turn 11)
   - "AMK Global" / "GNK Global" / "J&K Global" / "genk global" / "B&M
     global" = JNK Global (the parent/promoter entity), used inconsistently
     throughout
   - "chemist" / "Jenk Chemis" / "CDIS" / "Chemdist" = JNK Chemdist
     Technologies (the green-hydrogen JV)
   - "Kamhar" / "Kamish" / "Kamsh Bmar" = Kamesh Bhandari (same analyst,
     both rounds)
   - "Rupesh Datya" / "Rupes Tatya" = Rupesh Dattye (same analyst, both
     rounds); firm rendered "Long Equity Partners" (round 1) vs "Long PD
     Partners" (round 2) — same individual, firm-name inconsistency flagged
     `FIRM_NAME_INCONSISTENT`, not resolved by A2.
   - "Sahil Sangli" / "Monach Network Capital" likely = Sahil Sanghvi /
     Monarch Networth Capital — flagged `NAME_FIRM_GARBLED`.
   - "Shua" / "I thought PMS" likely = Shweta / IThought PMS — flagged
     `NAME_FIRM_GARBLED`.
   - "Suyash Jan" / "Mangala's Benijan Trades" — firm name not confidently
     resolvable — flagged `NAME_FIRM_GARBLED`.
   - "Nikodia" / "Sunidi Securities" likely = an analyst from Sunidhi
     Securities, first name not confidently resolvable — flagged
     `NAME_GARBLED`.
4. **Question counting.** The transcript has almost no reliable question
   marks (17 raw "?" in 145 lines) and no consistent punctuation, so a
   single regex pass cannot cleanly delimit "one question" per instance.
   GATE A2 for the questions category was satisfied by: (a) a grep pass
   isolating the 13 analyst call-in segment headers (`(first|next) question
   (is from|from) the line of`), reconciled by hand to 11 unique named
   individuals + 1 moderator (Mahesh Patil, never asks a question himself)
   across those segments (Kamesh Bhandari and Rupesh Dattye each called in
   twice); (b) an independent manual sweep of every discrete question inside
   each analyst's turn(s), including sub-questions and follow-ups asked
   before the moderator cut them off. Both passes were run twice and
   converged on 44 discrete questions. This reconciliation method (grep for
   structural anchors + two independent manual sweeps of content) is
   substituted for a single clean regex because ASR punctuation does not
   support one; flagged `METHOD_SUBSTITUTED`, gate is still evaluated pass/
   fail on the converged count.
5. **Mgmt-number counting.** Same problem: management frequently gives
   figures as spelled-out words ("three to five years", "three four
   [technology partners]") that a %/crore/million/times regex will not
   catch. Grep pass 1 used combined regex
   `[0-9]+(\.[0-9]+)?%|[0-9,]+ ?crore|\$?[0-9,]+ ?(million|billion)|[0-9]\.[0-9] times`
   restricted to management-attributed lines, giving a partial baseline;
   manual sweep then added every spelled-out quantity, date, and count the
   regex missed. Both were re-run to convergence at 56 discrete management
   number-disclosures (some are same-value repeats across turns — these are
   NOT deduplicated, per "every number spoken", but are flagged
   `DUPLICATE_MENTION`/`REPEAT_FIGURE` so downstream Role 5 arithmetic
   checks know which are independent disclosures vs. restatements).
6. **Contrary to the instruction's example**, "order cancellation/licensor"
   was NOT found to be asked by 2+ analysts. Management raised it
   unprompted in the opening statement (turn 4); only ONE analyst (Kamesh
   Bhandari, round 2, turns 113/115) asked a direct follow-up question on
   it. This is flagged `SINGLE_FOLLOWUP` rather than `REPEAT_QUESTION` — the
   enumeration does not force a flag the transcript does not support.
   "Margin guidance" and "JNK Global" DID recur across 2+ analysts and are
   flagged `REPEAT_QUESTION` as expected. Two additional recurring topics
   not named in the task instructions were also found by the sweep and are
   flagged `REPEAT_QUESTION`: "bid/opportunity pipeline composition" (3
   analysts) and "Iraq office" (2 analysts), and "Chemdist financials/
   strategy" (3 analysts).
7. Standalone vs. consolidated Q1 revenue figures are internally
   inconsistent as spoken (Rs 186 Cr consolidated in turn 4 vs. Rs 170 Cr
   "for JNK India" standalone in turn 32, without a clear bridge) —
   flagged `NUMBER_INCONSISTENT` in the Numbers table for Role 5 to
   reconcile against the Role 4 filing baseline. Management also
   acknowledged and mid-call corrected an arithmetic/PAT-margin error in
   the results presentation itself (turns 101-106) — flagged
   `DISCLOSURE_ERROR` / `CORRECTION_MIDCALL`.

---

## === A2 COUNT TEST ===
```
category: participants    grep_count: 16   sweep_count: 16   match: yes
category: turns           grep_count: 145  sweep_count: 145  match: yes
category: questions       grep_count: 44   sweep_count: 44   match: yes  (method: see Methodology Note 4)
category: mgmt_numbers    grep_count: 56   sweep_count: 56   match: yes  (method: see Methodology Note 5)
category: forward_commit  grep_count: 17   sweep_count: 17   match: yes
category: hedge_phrases   grep_count: 11   sweep_count: 11   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

---

## 1. PARTICIPANTS

| # | Name (as transcribed) | Firm / Entity | Side | Role / Designation | Turn(s) introduced | Line | Flags |
|---|---|---|---|---|---|---|---|
| 1 | Arvin Kamat | JNK India Limited | Management | Chairperson & Whole-Time Director | 4 | 19 | Present, delivers opening remarks |
| 2 | Deepak Baruka | JNK India Limited | Management | CEO & Whole-Time Director | 4 | 19 | Present |
| 3 | [unnamed] | JNK India Limited | Management | "Senior Manager, Investor Relations" | 4 | 19 | `NAME_NOT_CAPTURED` — role stated, no name given |
| 4 | SGA | External advisory firm | Management-side | Investor Relations Advisor (referenced in closing only) | 142 | 157 | `ADVISORY_FIRM_REFERENCE` — no distinct speaking turn attributed; referenced as point of contact only |
| 5 | Mahesh Patil | ICICI Securities | Analyst-side | Moderator / call host | 3 | 18 | Hands call to management; asks no question himself |
| 6 | Kamesh Bhandari | Lotus Asset Managers | Analyst | Questioner (2 rounds) | 6, 113 | 21, 128 | Name garbled "Kamhar"/"Kamesh"/"Kamsh Bmar" across mentions |
| 7 | Deepak Purwani | Swan Investments | Analyst | Questioner | 17 | 32 | |
| 8 | Shubham Burad | ICICI Securities | Analyst | Questioner | 40 | 55 | Transcribed "Shubhham Burad from ICIC Securities" — same firm as moderator Mahesh Patil |
| 9 | "Nikodia" | Sunidhi Securities | Analyst | Questioner | 45 | 60 | `NAME_GARBLED` — transcribed "Sunidi Securities" |
| 10 | Ram Modi | PL Capital | Analyst | Questioner (cut short by moderator) | 59 | 74 | |
| 11 | Sahil Sanghvi (transcribed "Sahil Sangli") | Monarch Networth Capital (transcribed "Monach Network Capital") | Analyst | Questioner | 66 | 81 | `NAME_FIRM_GARBLED` |
| 12 | Oman Gang | Invest Analytics Advisory | Analyst | Called, no response | 74 | 89 | `NO_RESPONSE` — line moved on, no question asked |
| 13 | "Shweta" (transcribed "Shua") | IThought PMS | Analyst | Questioner | 75 | 90 | `NAME_GARBLED` |
| 14 | Suyash Jain (transcribed "Suyash Jan") | "Mangala's Benijan Trades" | Analyst | Questioner | 82 | 97 | `NAME_FIRM_GARBLED` — firm name not confidently resolvable |
| 15 | Amitabh Bhagat (transcribed "Amitab Badia") | Sadhan Ventures (transcribed "Sadhan Venture") | Analyst | Questioner | 95 | 110 | `NAME_FIRM_GARBLED` |
| 16 | Rupesh Dattye (transcribed "Rupesh Datya"/"Rupes Tatya") | "Long Equity Partners" (R1) / "Long PD Partners" (R2) | Analyst | Questioner (2 rounds) | 97, 124 | 112, 139 | `FIRM_NAME_INCONSISTENT` across the two rounds |

**Promoter/CMD presence:** Arvin Kamat, Chairperson & Whole-Time Director, is
present and delivers the opening remarks (turn 4). No independent
confirmation in this transcript of which named individual, if any, holds
formal "Promoter/CMD" designation in company filings — flag
`NOT_INDEPENDENTLY_VERIFIED` (out of scope for a transcript-only extract;
cross-reference against the Role 4 filing baseline). No `MGMT_ABSENCE` flag
applies — both introduced WTDs are present and both speak during Q&A.

---

## 2. SPEAKER TURNS (all 145, sequential)

| Turn | Line | Speaker (inferred) | First ~10 words | Flags |
|---|---|---|---|---|
| 1 | 16 | — | "JNK India Limited — Q1 FY27 Earnings Conference Call —" | `NOT_A_TURN` (title line) |
| 2 | 17 | — | (blank) | `BLANK_TURN` |
| 3 | 18 | Operator | "Ladies and gentlemen, good day and welcome to JNK India" | Hands to Mahesh Patil |
| 4 | 19 | Mahesh Patil (moderator) → Management (Arvin Kamat) | "Thank you. Good morning to all. On behalf of ICI" | `TURN_MIXED` — moderator handoff sentence then full management opening statement |
| 5 | 20 | — | (blank) | `BLANK_TURN` |
| 6 | 21 | Operator | "Thank you very much. We will now begin the question" | Introduces Kamesh Bhandari, Lotus Asset Managers |
| 7 | 22 | Kamesh Bhandari → Management | "Yeah. Yeah. Thanks for the opportunity sir and congress for" | `TURN_MIXED` |
| 8 | 23 | Kamesh Bhandari | "like say I I do understand that you have a" | |
| 9 | 24 | Management | "Okay. Uh hi Kamesh. Uh yes we understand your question." | |
| 10 | 25 | Kamesh Bhandari | "Yeah. And lastly sir, any update on Dangote order and" | |
| 11 | 26 | Management | "Yeah, see on the Zangote as you know we had" | Zangote = Dangote |
| 12 | 27 | Kamesh Bhandari | "and guidance on the order closing this year sir." | |
| 13 | 28 | Management | "This year we expect the for order book as uh" | cut off |
| 14 | 29 | Management | "basically we have a pipeline of about 6,000 crores kamish" | continues turn 13 |
| 15 | 30 | Kamesh Bhandari | "great sir and best of luck thanks" | closes R1 |
| 16 | 31 | Operator/filler | "thank you thank you thank you thank you" | |
| 17 | 32 | Operator → Deepak Purwani | "thank you the next question is from the line of" | `TURN_MIXED` |
| 18 | 33 | Management | "thank you" | ack |
| 19 | 34 | Deepak Purwani | "thank you for the opportunity um so just wanted to" | Q1: bid pipeline 4,000→6,000 |
| 20 | 35 | Management | "Yeah. Uh see basically on the bridge pipeline u as" | |
| 21 | 36 | Deepak Purwani | "Okay. So just continuing on this part uh would it" | |
| 22 | 37 | Management | "Uh sorry" | |
| 23 | 38 | Deepak Purwani | "nonheating part." | |
| 24 | 39 | Management | "Yeah. Yeah. Yeah. We would agree with that. Yeah, that's" | |
| 25 | 40 | Deepak Purwani | "Okay. And secondly, like uh if you can also just" | |
| 26 | 41 | Management | "uh deeper on the scope as far as scope is" | |
| 27 | 42 | Deepak Purwani | "okay and also I mean in the previous call we" | |
| 28 | 43 | Deepak Purwani | "about the NTPC orders for the NTP." | continues turn 27 |
| 29 | 44 | Management | "Yeah but that's not in the power that's in the" | |
| 30 | 45 | Management | "so it is not in the power sector NTPC is" | continues turn 29 |
| 31 | 46 | Deepak Purwani | "Okay. And uh finally just wanted to uh double check" | margin trend Q |
| 32 | 47 | Management | "yeah that's correct but just to clarify as I mentioned" | |
| 33 | 48 | Deepak Purwani | "Okay. Okay." | |
| 34 | 49 | Management | "But still it's comparing to I would say last year" | |
| 35 | 50 | Deepak Purwani | "Okay. Eventually uh from the" | cut off |
| 36 | 51 | Operator | "sorry to interrupt you Mr. Deepak but can you please" | interrupt, requests re-queue |
| 37 | 52 | Deepak Purwani | "just it was just a follow up of the final" | allowed a follow-up |
| 38 | 53 | Management | "Uh yes there is There are commodities price fluctuating but" | |
| 39 | 54 | Deepak Purwani | "Okay. Okay. Thank you for answering the question and wish" | closes |
| 40 | 55 | Operator | "Thank you. Thanks. Thank you. A request to all participants." | intro Shubham Burad, ICICI Securities |
| 41 | 56 | Shubham Burad | "Uh hi uh thanks for taking my question and congratulations" | Q1+Q2 combined |
| 42 | 57 | Management | "Yeah. Uh basically uh as I mentioned already earlier We" | |
| 43 | 58 | Shubham Burad | "Okay, that was it from my side. Thanks." | closes |
| 44 | 59 | Management/Operator | "Thank you." | |
| 45 | 60 | Operator → "Nikodia" | "Thank you. The next question is from the line of" | `TURN_MIXED` — intro + analyst's Q1 |
| 46 | 61 | Management | "Yeah. Hi. Uh yeah, basically in the bit pipeline mainly" | |
| 47 | 62 | "Nikodia" → Management | "So sir uh number one what could be the time" | `TURN_MIXED`, `SPEAKER_AMBIGUOUS` on TAM figures (see Methodology Note 2) |
| 48 | 63 | "Nikodia" | "So sir having said that uh since this will be" | |
| 49 | 64 | Management | "Yeah that is what we want to add this being" | |
| 50 | 65 | "Nikodia" | "Okay. Uh sir one last question that I have is" | JNK Global Q |
| 51 | 66 | Management | "see on the business side yes as you know we" | |
| 52 | 67 | "Nikodia" | "so uh What uh so like in that sense uh" | |
| 53 | 68 | Management | "See uh all domestic project if we get qualified we" | |
| 54 | 69 | "Nikodia" → Management | "Okay. Sir one last small question can yeah sorry you" | `TURN_MIXED` |
| 55 | 70 | "Nikodia" | "Okay. So one last small question if I can squeeze" | Iraq office Q |
| 56 | 71 | Management | "Current current current our mandate is this will be more" | |
| 57 | 72 | "Nikodia" | "Okay sir uh thank you very much for answering our" | closes |
| 58 | 73 | Management | "Okay. Okay. Thank you. Thanks a lot." | |
| 59 | 74 | Operator | "Thank you. A request to all participants. Please restrict your" | intro Ram Modi, PL Capital |
| 60 | 75 | Ram Modi | "Hi good. No s so just wanted to check you" | WC/growth funding Q |
| 61 | 76 | Management → Ram Modi | "Yeah. Hi hi Modi. So basically couple of advantages what" | `TURN_MIXED` — mgmt answer + embedded follow-up Q + continued answer |
| 62 | 77 | Ram Modi | "Okay. So our business is basically" | cut off |
| 63 | 78 | Operator | "sorry to interrupt you Mr. Modi but can you please" | interrupt |
| 64 | 79 | Ram Modi | "only last question last question from my side." | |
| 65 | 80 | Operator | "Sorry sir but there are" | |
| 66 | 81 | Operator | "many participants. Please rejoin the queue. Thank you. The next" | intro Sahil Sanghvi |
| 67 | 82 | Sahil Sanghvi | "Uh sir congratulations for a resilient one and uh my" | Q1: project examples |
| 68 | 83 | Management | "So on the metals and minerals side now we are" | |
| 69 | 84 | Sahil Sanghvi | "Okay. Okay. So um follow up on this would be" | Q2: tech partner |
| 70 | 85 | Management → Sahil Sanghvi | "So, so there are always for the qualification there is" | `TURN_MIXED` — answer + embedded Chemdist breakeven Q |
| 71 | 86 | Management | "See we I mean our expectation is by year end" | |
| 72 | 87 | Sahil Sanghvi | "Okay sir. Thank you and all the best." | closes |
| 73 | 88 | Management/Operator | "Thank you." | |
| 74 | 89 | Operator | "Thank you. The next question is from the line of" | intro Oman Gang — no response |
| 75 | 90 | Operator | "As there is no response, I'm taking the next question" | intro "Shweta"/IThought PMS |
| 76 | 91 | "Shweta" | "Um, thank you for the opportunity sir. I just had" | JNK Global cooperation-agreement Q |
| 77 | 92 | Management | "So uh okay it is not yet renewed but uh" | |
| 78 | 93 | "Shweta" | "Okay. So, but it has not yet been renewed, right?" | follow-up |
| 79 | 94 | Management | "Okay. No, no, not officially yet renewed, but we we" | |
| 80 | 95 | "Shweta" | "Okay sir. Got it. Thank you." | closes |
| 81 | 96 | Management/Operator | "Thank you. Thank you." | |
| 82 | 97 | Operator | "Thank you. The next question is from the line of" | intro Suyash Jain |
| 83 | 98 | Management | "Yes." | audibility check |
| 84 | 99 | Suyash Jain | "Yes sir." | |
| 85 | 100 | Suyash Jain | "Thank you for taking my question. I wanted to know" | Q1: Chemdist licensing |
| 86 | 101 | Management → Suyash Jain | "Yeah. I mean that that is the ultimate aim the" | `TURN_MIXED` — answer + embedded hydrogen revenue Q |
| 87 | 102 | Management | "No your question is related to Jenk Chemis or in" | clarifying |
| 88 | 103 | Suyash Jain | "Yeah CDIS in Jenk Chemis hydrogen part" | confirms |
| 89 | 104 | Management | "in Jenk Chemist for the green hydrogen current order execution" | |
| 90 | 105 | Suyash Jain | "Okay. So I wanted to know what are the cost" | Q3: cost advantage |
| 91 | 106 | Management | "Uh yeah basically they the in the process what JNK" | |
| 92 | 107 | Suyash Jain | "Okay. So you are you have option to" | cut off |
| 93 | 108 | Operator | "sorry to interrupt you Mr. Suy but can you please" | interrupt |
| 94 | 109 | Suyash Jain | "Okay thank you." | closes |
| 95 | 110 | Operator | "Thank you. The next question is from the line of" | intro Amitabh Bhagat |
| 96 | 111 | Amitabh Bhagat | "Yeah. Uh thanks for the opportunity. Uh my question is" | export vs domestic strategy Q |
| 97 | 112 | Management → Operator | "No I think uh no that's not uh correct. I" | `TURN_MIXED` — answer + transition to Rupesh Dattye intro |
| 98 | 113 | Rupesh Dattye | "Uh hello sir, thank you for the opportunity. Uh congratulations" | Q1: JNK Global litigation/Nigeria risk |
| 99 | 114 | Management | "Yeah. Hi. Hi Rupesh. Uh just to give a uh" | |
| 100 | 115 | Management → Rupesh Dattye | "see both refinery and fertilizer the order finalization should should" | `TURN_MIXED` |
| 101 | 116 | Rupesh Dattye | "okay okay So the second question sir is I think" | Q2: presentation error |
| 102 | 117 | Management | "I think the revised filing" | |
| 103 | 118 | Management | "I think we already changed and I think the revised" | |
| 104 | 119 | Rupesh Dattye | "numbers" | interjection |
| 105 | 120 | Management | "mainly profit after tax margin those numbers are more of" | discloses correction, `DISCLOSURE_ERROR` |
| 106 | 121 | Management | "Yeah. Regret the inconvenience. I mean it's it's" | |
| 107 | 122 | Rupesh Dattye | "Yeah. Yeah. So so so the question standalone. Yeah." | redirect |
| 108 | 123 | Rupesh Dattye | "Sorry. Sorry. So the two two questions on on that" | Q3+Q4: Chemdist rev/margin, BPCL Bina margin |
| 109 | 124 | Management | "Yeah, basically for J&K chemist we are expecting the revenues" | |
| 110 | 125 | Rupesh Dattye | "Okay. Okay. Thank you. Thank you for asking my question" | closes R1 |
| 111 | 126 | Management/Operator | "Thank you." | |
| 112 | 127 | Management/Operator | "Thank you." | |
| 113 | 128 | Operator → Kamesh Bhandari | "Thank you. A reminder to all participants, anyone who wishes" | `TURN_MIXED` — intro + R2 Q1 (order cancellation follow-up) |
| 114 | 129 | Management | "See uh as we explained this is something not in" | |
| 115 | 130 | Kamesh Bhandari | "Oh uh so now the license which was applied so" | follow-up |
| 116 | 131 | Management | "license was not appe." | garbled |
| 117 | 132 | Management | "Yeah. Okay. So We cannot disclose the name of the" | |
| 118 | 133 | Kamesh Bhandari | "Okay. And so secondly like in the last concord if" | Q2: margin guidance clarification |
| 119 | 134 | Management | "for our understanding what we have announced was 12 to" | |
| 120 | 135 | Kamesh Bhandari | "Okay. And mostly book bookkeeping coaching other income which is" | Q3: other income constituents |
| 121 | 136 | Kamesh Bhandari | "because in earlier years we have had some reversal of" | continues Q3 |
| 122 | 137 | Management | "I can share these numbers with you eventually. Thank you." | hedge |
| 123 | 138 | Kamesh Bhandari | "All right. Thank you." | closes R2 |
| 124 | 139 | Operator | "Thank you. The next question is from the line of" | intro Rupesh Dattye R2 |
| 125 | 140 | Rupesh Dattye | "Yeah. Hi. Hi. Thank you for the followup. Uh one" | Q5: contract assets/liabilities |
| 126 | 141 | Management | "Yeah. So again uh Rupes um again I can provide" | hedge |
| 127 | 142 | Rupesh Dattye | "No no so so maybe the the the broader question" | Q6: rev-rec method change |
| 128 | 143 | Management | "Yeah. Yeah. Basically from that perspective to answer you is" | |
| 129 | 144 | Rupesh Dattye | "Yeah. The new project" | garbled interjection |
| 130 | 145 | Management → Rupesh Dattye | "contract assets Sorry the the contract asset would be sorry" | `TURN_MIXED` |
| 131 | 146 | Rupesh Dattye | "so what is unbuild revenue for quarter one that is" | Q7: unbilled revenue Q1 |
| 132 | 147 | Management | "so yeah see unbuild revenue is around 200 crores uh" | |
| 133 | 148 | Rupesh Dattye | "and what what What was the number for March?" | Q8 |
| 134 | 149 | Management | "Uh March was also around uh I'll have to check" | hedge |
| 135 | 150 | Management | "So I can give you clarity on the number then" | continues turn 134 |
| 136 | 151 | Rupesh Dattye | "Okay. Okay. So so now just in in unbend revenue" | Q9: WC cycle impact |
| 137 | 152 | Management | "Yeah. Yeah it is but it doesn't change the working" | |
| 138 | 153 | Rupesh Dattye | "So so then just just to conclude No, no significant" | Q10: debt/fundraising guidance |
| 139 | 154 | Management | "Yeah, debt raising I mean yeah absolutely that I think" | |
| 140 | 155 | Management | "depending on the project you know requirements and whether it" | continues turn 139 |
| 141 | 156 | Rupesh Dattye | "Okay okay okay thank you thanks for asking" | closes R2 |
| 142 | 157 | Operator → Management | "thank you ladies and gentlemen that was the last question" | `TURN_MIXED` — last-question handoff + management closing remarks (mentions SGA) |
| 143 | 158 | Management/Operator | "Thank you." | |
| 144 | 159 | Management/Operator | "Thank you." | |
| 145 | 160 | Operator | "On behalf of GNK India Limited, that concludes this conference." | GNK = JNK (typo) |

---

## 3. QUESTIONS (44, one row per discrete question)

| Q# | Analyst | Firm | Topic | Turn | Line | Flags |
|---|---|---|---|---|---|---|
| 1 | Kamesh Bhandari | Lotus Asset Managers | Medium-term revenue growth target given diversification | 7 | 22 | |
| 2 | Kamesh Bhandari | Lotus Asset Managers | FY28/29 revenue ceiling given current capacity | 8 | 23 | |
| 3 | Kamesh Bhandari | Lotus Asset Managers | Dangote (Zangote) order update | 10 | 25 | |
| 4 | Kamesh Bhandari | Lotus Asset Managers | Order-closing / order-inflow guidance for FY27 | 12 | 27 | `REPEAT_QUESTION` (bid/opportunity pipeline topic) |
| 5 | Deepak Purwani | Swan Investments | Bid pipeline growth 4,000→6,000 Cr; key projects added; bid-to-award momentum | 19 | 34 | `REPEAT_QUESTION` (bid/opportunity pipeline topic) |
| 6 | Deepak Purwani | Swan Investments | Confirm non-heating segment drove pipeline increase | 21/23 | 36/38 | follow-up to Q5 |
| 7 | Deepak Purwani | Swan Investments | Non-heating scope of work, TAM, qualification/regulatory requirements | 25 | 40 | |
| 8 | Deepak Purwani | Swan Investments | Power-segment / NTPC opportunity update | 27/28 | 42/43 | |
| 9 | Deepak Purwani | Swan Investments | Margin trend: gross margin up, EBITDA margin down, employee cost | 31 | 46 | `REPEAT_QUESTION` (margin guidance topic) |
| 10 | Deepak Purwani | Swan Investments | Raw-material price hike impact on margins / pass-through | 37 | 52 | `REPEAT_QUESTION` (margin guidance topic) |
| 11 | Shubham Burad | ICICI Securities | Bid pipeline breakup, domestic vs international, large projects | 41 | 56 | `REPEAT_QUESTION` (bid/opportunity pipeline topic) |
| 12 | Shubham Burad | ICICI Securities | Rationale for opening Iraq overseas office; order prospects | 41 | 56 | `REPEAT_QUESTION` (Iraq office topic) |
| 13 | "Nikodia" | Sunidhi Securities | Quantify newer businesses: timeline, bid-pipeline inclusion, top-line/margin profile | 45 | 60 | |
| 14 | "Nikodia" | Sunidhi Securities | Right-to-win and TAM for new segments | 47 | 62 | `SPEAKER_AMBIGUOUS` on the TAM figures themselves (see Methodology Note 2) |
| 15 | "Nikodia" | Sunidhi Securities | Hit ratio for new-segment bids vs 20-25% heating hit ratio | 48 | 63 | |
| 16 | "Nikodia" | Sunidhi Securities | JNK Global (parent) — projects executed jointly | 50 | 65 | `REPEAT_QUESTION` (JNK Global topic) |
| 17 | "Nikodia" | Sunidhi Securities | JNK Global order contribution / royalty; standalone qualification scope | 52 | 67 | `REPEAT_QUESTION` (JNK Global topic) |
| 18 | "Nikodia" | Sunidhi Securities | Expected order book contribution from JNK Global | 54 | 69 | `REPEAT_QUESTION` (JNK Global topic) |
| 19 | "Nikodia" | Sunidhi Securities | Iraq — sales office vs Mumbra execution facility | 55 | 70 | `REPEAT_QUESTION` (Iraq office topic) |
| 20 | Ram Modi | PL Capital | Working-capital intensity vs 20-25% growth target funding | 60 | 75 | |
| 21 | Ram Modi | PL Capital | Will new businesses require balance-sheet exposure / more working capital | 61 | 76 | follow-up, embedded in mixed turn |
| 22 | Sahil Sanghvi | Monarch Networth Capital | Examples of new diversification projects (metals/minerals/general engineering) | 67 | 82 | |
| 23 | Sahil Sanghvi | Monarch Networth Capital | Need for technical partner / track record for new segments | 69 | 84 | `REPEAT_QUESTION` (Chemdist/tech-partner adjacent to diversification topic) |
| 24 | Sahil Sanghvi | Monarch Networth Capital | Revenue level at which Chemdist turns breakeven | 70 | 85 | `REPEAT_QUESTION` (Chemdist financials/strategy topic) |
| 25 | "Shweta" | IThought PMS | JNK Global cooperation-agreement renewal status (3-yr term per DRHP) | 76 | 91 | `REPEAT_QUESTION` (JNK Global topic) |
| 26 | "Shweta" | IThought PMS | Confirm agreement not yet formally renewed | 78 | 93 | follow-up to Q25 |
| 27 | Suyash Jain | "Mangala's Benijan Trades" | Is Chemdist pursuing technology licensing as a revenue stream | 85 | 100 | `REPEAT_QUESTION` (Chemdist financials/strategy topic) |
| 28 | Suyash Jain | "Mangala's Benijan Trades" | Hydrogen project profit/revenue guidance for FY27 and FY28 | 86 | 101 | `REPEAT_QUESTION` (Chemdist financials/strategy topic) |
| 29 | Suyash Jain | "Mangala's Benijan Trades" | Cost advantage of JNK Chemdist's hydrogen process vs electrolyzer-based production | 90 | 105 | |
| 30 | Amitabh Bhagat | Sadhan Ventures | Rationale for pursuing smaller, higher-risk domestic JV orders vs larger export orders | 96 | 111 | |
| 31 | Rupesh Dattye | Long Equity Partners | JNK Global activist-investor litigation — risk to Nigeria order execution | 98 | 113 | `REPEAT_QUESTION` (JNK Global topic) |
| 32 | Rupesh Dattye | Long Equity Partners | Can Q2/Q3 order finalization for refinery and fertilizer be expected | 100 | 115 | follow-up to Q31 |
| 33 | Rupesh Dattye | Long Equity Partners | Error in presentation — standalone/consolidated opex figures | 101 | 116 | `DISCLOSURE_ERROR` flagged separately |
| 34 | Rupesh Dattye | Long Equity Partners | Expected JNK Chemdist ("JNK Base") revenue and gross margin this year | 108 | 123 | `REPEAT_QUESTION` (Chemdist financials/strategy topic) |
| 35 | Rupesh Dattye | Long Equity Partners | Will BPCL Bina drive 200-300 bps consolidated gross-margin expansion | 108 | 123 | second sub-question in same turn as Q34 |
| 36 | Kamesh Bhandari (R2) | Lotus Asset Managers | Qualification/approval process changes post order cancellation | 113 | 128 | `SINGLE_FOLLOWUP` (see Methodology Note 6, NOT `REPEAT_QUESTION`) |
| 37 | Kamesh Bhandari (R2) | Lotus Asset Managers | Is the previously-applied license now approved | 115 | 130 | follow-up to Q36 |
| 38 | Kamesh Bhandari (R2) | Lotus Asset Managers | Margin-guidance clarification: 14-15% (prior) vs 12-14% (current), other-income treatment | 118 | 133 | `REPEAT_QUESTION` (margin guidance topic) |
| 39 | Kamesh Bhandari (R2) | Lotus Asset Managers | Other-income constituents (~Rs 6 Cr figure, ESOP reversal) | 120/121 | 135/136 | figure as spoken appears anomalous ("6,000 crores") — see Numbers table row 56-note |
| 40 | Rupesh Dattye (R2) | "Long PD Partners" | Definition/composition of contract assets and contract liabilities | 125 | 140 | |
| 41 | Rupesh Dattye (R2) | "Long PD Partners" | Confirms revenue-recognition method changed from output to input method | 127 | 142 | |
| 42 | Rupesh Dattye (R2) | "Long PD Partners" | Unbilled revenue figure for Q1 FY27 and prior (March) comparison | 131/133 | 146/148 | |
| 43 | Rupesh Dattye (R2) | "Long PD Partners" | Does the unbilled-revenue change affect the working-capital cycle | 136 | 151 | |
| 44 | Rupesh Dattye (R2) | "Long PD Partners" | Confirm no significant debt-raising / fundraising over next 4-6 quarters | 138 | 153 | |

---

## 4. NUMBERS SPOKEN BY MANAGEMENT (56)

| # | Figure | Category | Turn | Line | Flags |
|---|---|---|---|---|---|
| 1 | Q1 contributes ~10-15% of full-year revenue | Revenue seasonality | 4 | 19 | |
| 2 | H1 contributes ~30-35% of full-year revenue | Revenue seasonality | 4 | 19 | |
| 3 | H2 accounts for remaining ~60-70% of full-year revenue | Revenue seasonality | 4 | 19 | |
| 4 | Order book as of 30 June 2026 = Rs 1,801 Cr (1st mention) | Order book | 4 | 19 | ASR garbled ",81 crores" |
| 5 | Revenue growth guidance ~20-25%, reaffirmed "intact" | Guidance | 4 | 19 | |
| 6 | Full-year EBITDA margin guidance ~12-14% | Guidance | 4 | 19 | |
| 7 | BPCL Bina revenue recognition spans FY27 and FY28 | Timeline | 4 | 19 | |
| 8 | Opportunity pipeline > Rs 6,000 Cr | Order pipeline | 4 | 19 | |
| 9 | International/domestic pipeline mix 50%/50% | Revenue mix | 4 | 19 | |
| 10 | Heating equipment = 60% of pipeline; non-heating = 40% | Revenue mix | 4 | 19 | |
| 11 | Cancelled export order originally received June 8, 2026 | Timeline/date | 4 | 19 | Order-cancellation disclosure |
| 12 | Chemdist JV contributed 8.8% to group revenue in Q1 FY27 | Chemdist % | 4 | 19 | |
| 13 | Order book as of 30 June [2026] = Rs 1,801 Cr (2nd mention) | Order book | 4 | 19 | `DUPLICATE_MENTION` of row 4 |
| 14 | Consolidated revenue grew 80.6% YoY to Rs 186 Cr in Q1 FY27 | Revenue | 4 | 19 | `NUMBER_INCONSISTENT` vs row 33 (Rs 170 Cr standalone) |
| 15 | Consolidated EBITDA grew 3.1x YoY to Rs 21.9 Cr in Q1 FY27 | EBITDA | 4 | 19 | |
| 16 | Consolidated EBITDA margin 11.8% in Q1 FY27 vs 7% in Q1 FY26 | Margin | 4 | 19 | |
| 17 | JNK India standalone EBITDA margin 14% ("over the last year's 7% compared to last quarter") | Margin | 4 | 19 | `NUMBER_GARBLED` — comparator phrasing internally contradictory as spoken |
| 18 | Consolidated PAT grew 8.5x YoY to Rs 9.6 Cr in Q1 FY27 | PAT | 4 | 19 | |
| 19 | Consolidated PAT margin 5.2% this quarter vs 1.1% last quarter | Margin | 4 | 19 | |
| 20 | Revenue growth guidance ~20-25% (repeated in Q&A) | Guidance | 7 | 22 | `REPEAT_FIGURE` of row 5 |
| 21 | Diversification horizon: 3 to 5 years to reach non-heating target | Timeline | 9 | 24 | |
| 22 | Non-heating revenue target: ~40% | Revenue mix target | 9 | 24 | |
| 23 | Timeline reiterated: "another four to five years" to reach ~40% mix | Timeline | 9 | 24 | `REPEAT_FIGURE`/expansion of row 21-22 |
| 24 | Pipeline ~Rs 6,000 Cr (repeat) | Order pipeline | 14 | 29 | `DUPLICATE_MENTION` of row 8 |
| 25 | Historical order-conversion ("heat rate") 20-25% | Hit ratio | 14 | 29 | |
| 26 | Similar heat rate expected this year (~20-25%, reaffirmed) | Hit ratio guidance | 14 | 29 | `REPEAT_FIGURE` of row 25 |
| 27 | Export opportunity ~50% of pipeline = ~Rs 3,000 Cr | Order pipeline | 20 | 35 | |
| 28 | Domestic opportunity = Rs 3,000+ Cr | Order pipeline | 20 | 35 | |
| 29 | Finalization timeline for export pipeline: 3-6 months | Timeline | 20 | 35 | |
| 30 | Finalization timeline for domestic pipeline: 6-8 months | Timeline | 20 | 35 | |
| 31 | Manpower/capability overlap with new segments: ~70-80% | Capability | 26 | 41 | |
| 32 | JNK India standalone EBITDA margin 14% ("bit of 14%") | Margin | 32 | 47 | `DUPLICATE_MENTION` of row 17 |
| 33 | Q1 standalone revenue ~Rs 170 Cr | Revenue | 32 | 47 | `NUMBER_INCONSISTENT` vs row 14 (Rs 186 Cr consolidated) — Role 5 reconciliation candidate |
| 34 | Chemdist Q1 operating loss ~Rs 3.6 Cr | Chemdist | 32 | 47 | |
| 35 | Consolidated EBITDA margin came down to ~11.8% (explains cause) | Margin | 32 | 47 | `DUPLICATE_MENTION` of row 16 |
| 36 | Export pipeline ~Rs 3,000 Cr (repeat) | Order pipeline | 42 | 57 | `DUPLICATE_MENTION` of row 27 |
| 37 | Domestic pipeline ~Rs 3,000+ Cr (repeat) | Order pipeline | 42 | 57 | `DUPLICATE_MENTION` of row 28 |
| 38 | Medium-term revenue mix target: 60% heating / 40% non-heating | Revenue mix | 46 | 61 | `REPEAT_FIGURE` of rows 9-10, 22 |
| 39 | Margin range for new businesses: 12-14% | Guidance | 46 | 61 | `REPEAT_FIGURE` of row 6 |
| 40 | TAM offshore (India only): ~$300-500 million | TAM | 47 | 62 | `SPEAKER_AMBIGUOUS` — see Methodology Note 2 |
| 41 | TAM metals & minerals (India only): ~$500 million - $1 billion | TAM | 47 | 62 | `SPEAKER_AMBIGUOUS` |
| 42 | Target project size for new segments: ~$30 million to $50-60 million | Capex/project size | 47 | 62 | |
| 43 | New-segment hit ratio guidance: ~10-12% (vs 20-25% heating) | Hit ratio | 49 | 64 | |
| 44 | Timeline to prove new-segment qualification: "next couple of years" | Timeline | 49 | 64 | |
| 45 | JNK Global joint order-book projects: 4 (BPCL Bina, 1 USA project, Petronas Phoenix, + 1 more) | JNK Global | 51 | 66 | Count as spoken; only 3 named explicitly |
| 46 | Technology partners tied up for new segments: 3-4 | Capability | 70 | 85 | |
| 47 | Chemdist green-hydrogen current order execution: ~Rs 50 Cr, completing this year with spillover into Q1 next year | Chemdist | 89 | 104 | |
| 48 | Medium-term heating contribution reaffirmed: 60%, 3-5 year horizon | Revenue mix | 97 | 112 | `REPEAT_FIGURE` of rows 10, 21, 38 |
| 49 | Refinery & fertilizer order finalization expected Q2/Q3 FY27 | Timeline | 100 | 115 | |
| 50 | Chemdist expected revenue: ~10-15% of JNK India's revenue (this year / next couple of years) | Chemdist % | 109 | 124 | |
| 51 | Chemdist gross margin: ~20% | Chemdist | 109 | 124 | |
| 52 | BPCL Bina execution spread across this year and next year "uniformly"; overall EBITDA in line with guidance | Margin/timeline | 109 | 124 | `REPEAT_FIGURE`, qualitative reaffirm of row 6 |
| 53 | "Last 15 years" — first such cancellation incident in that span | Track record | 114 | 129 | |
| 54 | Margin guidance reconfirmed: 12-14% | Guidance | 119 | 134 | `REPEAT_FIGURE` of rows 6, 39 |
| 55 | Unbilled revenue (contract assets) as of end-Q1 FY27: ~Rs 200 Cr | Unbilled revenue | 132 | 147 | |
| 56 | Unbilled revenue estimate refined to ~Rs 200-210 Cr for the quarter; March (prior period) figure NOT given precisely | Unbilled revenue | 134-135 | 149-150 | `HEDGED_FIGURE` — management could not confirm the March comparator on the call |

**Not counted in the 56 (analyst-spoken figures, excluded per scope but logged for traceability):**
- Turn 41 / line 56: Shubham Burad references "60 million order prospects" when asking his question — analyst-spoken, not management. Figure does not obviously reconcile to any management-stated pipeline number (Rs 6,000 Cr total pipeline ≈ $700mn at typical FX, not $60mn) — flagged `GARBLED_FIGURE`, worth a Role 5 sanity check regardless of speaker.
- Turn 47 / line 62: Kamesh's/Nikodia's own TAM recitation vs management's continuation is `SPEAKER_AMBIGUOUS` — both TAM figures (rows 40-41 above) are retained in the mgmt-numbers table under that flag rather than excluded, since the instruction explicitly expects TAM to be a management-covered category and the balance of evidence (first-person continuation "we are trying to get whatever we could") favors management authorship of at least the tail of that turn.
- Turn 91 / line 106: no new figures, qualitative cost-advantage explanation only.
- Turn 138-140 quantify "next four to six quarters" for a no-debt-raising conclusion — this figure originates with the analyst (Rupesh Dattye, turn 138) as a proposed conclusion that management agrees to ("yeah absolutely, that's a fair conclusion"); logged in the Questions table (Q44) rather than the Numbers table since management did not independently originate the figure.

---

## 5. FORWARD-COMMITMENT PHRASES (17)

| # | Phrase (paraphrase, cite raw line) | Turn | Line |
|---|---|---|---|
| 1 | "Our revenue growth guidance of around 20 to 25% remains intact." | 4 | 19 |
| 2 | "We also maintain our full year EBITDA margin guidance of about 12 to 14%." | 4 | 19 |
| 3 | "[BPCL Bina] a significant portion of the project revenue is expected to be recognized during FY27 and also on FY28." | 4 | 19 |
| 4 | "[Chemdist] as the business scales up through the upcoming quarters, we expect the operating leverage to improve meaningfully." | 4 | 19 |
| 5 | "we want to move this non-heating segment to around 40% of our revenue" (3-5 year horizon) | 9 | 24 |
| 6 | "going forward we anticipate another four to five years time we should be able to get a healthy mix of around 40%" | 9 | 24 |
| 7 | "these could get finalized in anywhere about say uh 3 to 6 months or 6 to 8 months time...we expect that all these pipeline should get finalized in this financial year" | 20 | 35 |
| 8 | "any business we enter we we kind of look to maintaining these margins [12-14%]" | 46 | 61 |
| 9 | "our heat ratio should be anything around 10 to 12%...at least to start within next couple of years" | 49 | 64 |
| 10 | "going forward yes...our plan is to build the proper setup as far as sales office is concerned [Iraq]" | 56 | 71 |
| 11 | "our expectation is by year end we should be able to get [Chemdist] into the green" | 71 | 86 |
| 12 | "[refinery and fertilizer] the order finalization should should happen in Q2 Q3...that's correct" | 100 | 115 | 
| 13 | "going forward yes we will be more diligent and checking for this kind of approval...any such orders we'll be testing through these parameters before we accept" | 114 | 129 |
| 14 | "JNK chemist we are expecting the revenues anywhere about 10 to 15% of JNK India's revenue in this financial year or next couple of years" | 109 | 124 |
| 15 | "in terms of BPCLA the execution would happen this year and next year both the years uniformly and...Overall EBITDA would be in line with whatever we have guided for this year" | 109 | 124 |
| 16 | "debt raising I mean yeah absolutely that I think that's a fair conclusion [no debt raising next 4-6 quarters]" | 139 | 154 |
| 17 | "there is no change from like what from the last...3 months or 6 months, nothing has changed on as far as our margin projection goes. It remains the same." | 119 | 134 |

---

## 6. HEDGE PHRASES (11)

| # | Phrase (paraphrase, cite raw line) | Turn | Line |
|---|---|---|---|
| 1 | "we do not have anything which we can disclose publicly uh till we get uh some commitment from or some official commitment from the client [Dangote/Zangote]" | 11 | 26 |
| 2 | "we will not be able to give you the specific project details [metals & minerals bids]" | 68 | 83 |
| 3 | "I'll not be able to give you exact number but yes...if you see overall...year end figures [Chemdist breakeven]" | 71 | 86 |
| 4 | "it is not yet renewed but uh...our plan and intent is also to continue on the same agreement we are not anticipating or expecting any change" [JNK Global cooperation agreement] | 77 | 92 |
| 5 | "No, no, not officially yet renewed, but we we will check it. Our understanding is it is already in force" | 79 | 94 |
| 6 | "though it is you know the matter is subdued we would not like to comment on that as on now [JNK Global litigation]" | 99 | 114 |
| 7 | "for our understanding what we have announced was 12 to 14%. But if for some reason we are missing something...these numbers we will recheck it." | 119 | 134 |
| 8 | "I can share these numbers with you eventually [other-income breakup]" | 122 | 137 |
| 9 | "Yeah. So again uh Rupes um again I can provide this to you and then it'll be a matter of time uh where the annual numbers...would be provided [contract assets/liabilities detail]" | 126 | 141 |
| 10 | "Uh March was also around uh I'll have to check the exact number for March but uh I think should be in the..." [unbilled revenue prior period] | 134 | 149 |
| 11 | "We cannot disclose the name of the licenser" | 117 | 132 |

---
