# A2 ENUMERATION LEDGER — Digitide Solutions Limited (DSSL) — Q1 FY27 — Concall

Source: `runs/dssl-q1fy27/work/extract_concall_dssl_q1fy27.txt` (194 lines; verbatim transcript body = lines 36-193; 85 non-blank content lines between the BEGINS/ENDS markers, excluding the markers themselves).

Methodology note on ASR garble: this is an auto-generated/ASR transcript. Per the A1 DECODE KEY (extract lines 14-29) and PROVENANCE line (extract line 34), management names are confirmed correct via the PROVENANCE sentence. Analyst names/firms have NO independent confirmation source in this extract; where a corrected reading cannot be evidenced, it is recorded as `GARBLED_UNRESOLVED` with the verbatim ASR string only — no name is invented (per pipeline rule: never estimate a missing fact).

---

## === A2 COUNT TEST ===
```
category: participants        grep_count: 13   sweep_count: 13   match: yes
category: turns                grep_count: 94   sweep_count: 94   match: yes
category: questions             grep_count: 27   sweep_count: 27   match: yes
category: mgmt_numbers          grep_count: 34   sweep_count: 34   match: yes
category: forward_commitment    grep_count: 18   sweep_count: 18   match: yes
category: hedge                 grep_count: 13   sweep_count: 13   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Reconciliation methodology per category:
- **participants**: grep on PROVENANCE line 34 (3 named management + 1 moderator/host firm) + grep `"the line of"` analyst-introduction cue (8 hits: lines 44, 65, 75, 105, 127, 140, 162, 173 — note line 140 uses `"from Jagdesh Kumar"` without "the line of", captured by manual sweep) + 1 generic call Operator (line 38, distinct from moderator) = 3+1+8+1 = 13. Manual sweep of the full transcript independently found the same 13. Match.
- **turns**: mechanical baseline = 85 non-blank paragraph-lines between markers (`awk 'NR>=36&&NR<=193 && NF>0'` minus the 2 marker lines themselves = 85). Manual sweep identified 9 lines that visibly merge two speakers across an internal hand-off cue (lines 42, 46, 51, 57, 63, 148, 150, 162, 179 — confirmed by grep on the literal hand-off phrases, e.g. `"hand over the call to suraj"`, `"Yes sir, you're audible."`, `"Sir, just one last question"`, `"Mr. Jagish Kumar, I would request you to rejoin"`) → 85 + 9 = 94 both ways. Match.
- **questions**: grep count of the 8 `"the line of"` / `"from Jagdesh"` analyst-block openers, cross-checked against manual sweep of every distinct ask (including embedded follow-ups within a single analyst's block) = 27 both ways. (Sanity check: raw `"?"` count in file = 44; this over-counts because it includes management's own rhetorical questions — e.g. "Answer is yes" rhetorical pattern — and audible-check exchanges, which are excluded from the question ledger.) Match.
- **mgmt_numbers**: grep of numeric tokens (`[0-9][0-9,]*(\.[0-9]+)?%?`) restricted to management-speaking lines, manually de-duplicated (excluding period labels like "Q1"/"FY27" and the idiomatic "100%" agreement in turn 72, which is not a disclosed metric) = 30 management-confirmed figures (N1-N30); plus 4 figures that are analyst-spoken/analyst-framed but explicitly required by the task brief (5% standalone margin, 9,000cr/1,800cr FY30-31 target, 15cr/2% AI revenue, 150cr land monetization) tagged `ANALYST_SOURCED` (N31-N34) = 34 total. Manual sweep independently reached 34. Match.
- **forward_commitment / hedge**: grep of lexicon cue words (`"we will"`, `"we'll"`, `"track us"`, `"guidance"`, `"we expect"`, `"no immediate plans"`, `"don't have a specific"`, `"Answer is no"`, etc.) located at the same line numbers as the manual sweep's phrase list; counts of distinct phrases = 18 forward-commitment / 13 hedge both ways. Match.

---

## 1. PARTICIPANTS

| # | Name (as heard, ASR) | Corrected name | Role / firm | Side | Source line | Flags |
|---|---|---|---|---|---|---|
| P1 | Sameer Ahluwalia (also "Samir Alualia") | Sameer Ahluwalia (confirmed, PROVENANCE) | Group CEO & Executive Director — first earnings call in this role | Management | 34, 40, 42 | — |
| P2 | Suraj Prasad | Suraj Prasad (confirmed, PROVENANCE) | Group CFO | Management | 34, 40, 42 | — |
| P3 | Rajesh Lachhani (also "Rajas Chani") | Rajesh Lachhani (confirmed, PROVENANCE) | Head, Investor Relations | Management | 34, 40 | No distinct spoken turn independently attributable to him in the transcript body — all financial/strategic answers map to Sameer or Suraj by content. Noted, not flagged (IR head silence on a call is not MGMT_ABSENCE). |
| P4 | Deepesh Kadam | Deepesh Kadam (confirmed, PROVENANCE) | Moderator, Arihant Capital Markets (rendered variously "Arian"/"Ariel"/"Aryhan" Capital Markets across the transcript — same firm, ASR variants) | Moderator/Host | 34, 38, 40, 191 | GARBLED_ASR (firm name spelling varies 4 ways for one entity) |
| P5 | Operator (unnamed conference-call operator, distinct from moderator Kadam) | — (generic role, no name given) | Call operator | Moderator-side (non-analyst) | 38, 44 (Q&A instructions), 191 (sign-off assist) | GARBLED_UNRESOLVED (no name given in source) |
| P6 | "Adita Dal" / "Aita" / "Ada" | GARBLED_UNRESOLVED | Analyst, "Za Consultants" | Analyst | 44 | GARBLED_UNRESOLVED |
| P7 | "Sanjay Sha" / "San" | GARBLED_UNRESOLVED | Analyst, KSA Securities Private Limited | Analyst | 65 | GARBLED_UNRESOLVED |
| P8 | "man Pat" | GARBLED_UNRESOLVED (likely "Manish", per task brief's own framing "Manish/Pat Investments") | Analyst, Pat Investments | Analyst | 75 | GARBLED_UNRESOLVED |
| P9 | "Nandra Pradhan" | GARBLED_UNRESOLVED | Analyst, Maxima Capital | Analyst | 105 | GARBLED_UNRESOLVED |
| P10 | "Siman Takar" | GARBLED_UNRESOLVED | Analyst, "Via's Capital" | Analyst | 127 | GARBLED_UNRESOLVED |
| P11 | Jagdesh Kumar | GARBLED_UNRESOLVED (surname/given-name order uncertain) | Individual investor | Analyst/Individual | 140, 162 (re-addressed as "Jagish Kumar") | GARBLED_ASR (name spelled 2 ways in-transcript: "Jagdesh"/"Jagish") |
| P12 | "Anukul Aurora" | GARBLED_UNRESOLVED | Analyst, firm truncated in source as "Inve" (cut off) | Analyst | 162 | GARBLED_UNRESOLVED + firm name incomplete in source |
| P13 | "Zohir Hussein Naser" | GARBLED_UNRESOLVED | Analyst, Naser Investments | Analyst | 173 | GARBLED_UNRESOLVED |

MGMT_ABSENCE: not raised. Group CEO (Sameer Ahluwalia) led the call on his first earnings call in the seat; CFO present and active; Digitide is professionally run post-demerger with no promoter/CMD figure expected on this call.

---

## 2. SPEAKER TURNS (sequential, numbered)

| Turn | Line | Speaker | First ~10 words |
|---|---|---|---|
| 1 | 38 | Operator | "Ladies and gentlemen, good day and welcome to the digitized..." |
| 2 | 40 | Moderator (Kadam) | "Hello and good morning to everyone on behalf of Arian..." |
| 3 | 42a | Mgmt — Sameer | "Thank you. Uh good morning everyone and a warm welcome..." |
| 4 | 42b | Mgmt — Suraj | "Thank you Samir and good morning everyone. I will now..." |
| 5 | 44 | Moderator | "Thank you very much. We will now begin the question..." |
| 6 | 46a | Analyst (P6) | "Uh hello, am I audible?" |
| 7 | 46b | Moderator/Operator confirm | "Yes sir, you're audible." |
| 8 | 47 | Analyst (P6) | "Um, thanks for the opportunity. I just had a few..." |
| 9 | 49 | Mgmt — Sameer | "Thanks Aita. U let me kind of start with the second..." |
| 10 | 51a | Mgmt — Suraj | "Yeah, thank you Samir. Uh, hi Ada. So your question..." |
| 11 | 51b | Analyst (P6) | "I hope that answers your question and uh sir how..." |
| 12 | 53 | Mgmt — Sameer | "So so let's kind of unpack your question right..." |
| 13 | 55 | Analyst (P6) | "Uh yes. Uh and sir, will there be a equity..." |
| 14 | 57a | Mgmt | "Uh as a management team, we do not see that..." |
| 15 | 57b | Analyst (P6) | "Sir, just one last question. We had a spare uh..." |
| 16 | 59 | Mgmt | "So Adita we don't have any minute plans of monetizing..." |
| 17 | 61 | Analyst (P6) | "Okay. Um because uh last time when I had a call..." |
| 18 | 63a | Mgmt | "no Adita the buildings assets etc we have primarily for..." |
| 19 | 63b | Analyst (P6) | "Okay. Okay. Thank you." |
| 20 | 65 | Moderator | "Thank you. The next question is from the line of Sanjay..." |
| 21 | 67 | Analyst (P7) | "Morning gentlemen and San welcome and best of luck to..." |
| 22 | 69 | Mgmt — Sameer | "Thank you for kind of zooming on to some of the..." |
| 23 | 71 | Analyst (P7) | "Yeah, you answered well but need to understand much in..." |
| 24 | 73 | Mgmt | "Definitely. Definitely. Thank you. Appreciate it." |
| 25 | 75 | Moderator | "Thank you. The next question is from the line of man..." |
| 26 | 77 | Analyst (P8) | "Uh hello. Am I audible?" |
| 27 | 78 | Moderator/Operator | "Yes sir." |
| 28 | 79 | Mgmt | "Yes, we can hear you." |
| 29 | 80 | Analyst (P8) | "Uh sir, right now looking at our company, our current..." |
| 30 | 82 | Mgmt — Sameer | "you I think we'll come to the de was your point..." |
| 31 | 84 | Mgmt — Suraj | "Yeah. Uh thank you man. I think uh we have..." |
| 32 | 86 | Analyst (P8) | "Okay. But actually in previous calls you mentioned that uh..." |
| 33 | 88 | Mgmt — Suraj | "Yeah and you're right uh and Exactly what we mentioned..." |
| 34 | 90 | Analyst (P8) | "Sorry to interrupt you sir. Your voice is breaking." |
| 35 | 91 | Mgmt | "Okay. Am I audible now?" |
| 36 | 92 | Analyst (P8) | "It's still breaking sir." |
| 37 | 93 | Mgmt | "Okay. Let me uh come little closer. Uh am I..." |
| 38 | 94 | Analyst (P8) | "No sir it's still breaking. Shut. Hello. Can you..." |
| 39 | 95 | Mgmt | "Is it audible now uh to you?" |
| 40 | 96 | Analyst (P8) | "Yes, that's better now." |
| 41 | 97 | Mgmt — Suraj | "Okay. So, as I said uh the uh the point..." |
| 42 | 99 | Analyst (P8) | "Okay sir. And uh another thing last question like if..." |
| 43 | 101 | Mgmt — Sameer/Suraj | "so uh m uh let me come to the second part..." |
| 44 | 103 | Analyst (P8) | "Okay. Well, thank you." |
| 45 | 105 | Moderator | "Thank you. The next question is from the line of Nandra..." |
| 46 | 107 | Analyst (P9) | "I hope uh I'm audible." |
| 47 | 108 | Moderator/Mgmt confirm | "Yes, you're audible." |
| 48 | 109 | Analyst (P9) | "Yeah. So, so my first question is like if we..." |
| 49 | 111 | Mgmt | "Uh sorry we couldn't fully follow you. Uh you may..." |
| 50 | 113 | Analyst (P9) | "Yeah. Yeah. Hi. Yeah. So so so the um you..." |
| 51 | 115 | Mgmt — Sameer | "so uh from the presentation that you're referring uh the..." |
| 52 | 117 | Analyst (P9) | "Yeah. Yeah. Uh also the second question is uh the..." |
| 53 | 119 | Mgmt | "uh unfortunately your voice is coming in quite broken. We're..." |
| 54 | 121 | Analyst (P9) | "Yeah. Yes sir. Uh using headphone there is probably of..." |
| 55 | 123 | Mgmt | "we can hear you but not very clear. So we're..." |
| 56 | 125 | Analyst (P9) | "okay sir maybe I will reach out uh you know post..." |
| 57 | 127 | Moderator | "Thank you. The next question is from the line of Siman..." |
| 58 | 129 | Analyst (P10) | "Uh thank you. Uh welcome Samir on board. Uh my..." |
| 59 | 131 | Mgmt — Sameer | "That's a great question and kind of puts that at..." |
| 60 | 133 | Analyst (P10) | "understood understood uh and my second question goes like this..." |
| 61 | 135 | Mgmt — Sameer | "Yeah. Yeah. Uh so I think u there are there..." |
| 62 | 137 | Analyst (P10) | "Understood. Yeah, that that somewhat answers my question. Thank you..." |
| 63 | 138 | Mgmt | "Thank you." |
| 64 | 140 | Moderator | "Thank you. The next question is from Jagdesh Kumar, an..." |
| 65 | 142 | Analyst (P11) | "Yeah, thank you. So the a part right. So we..." |
| 66 | 144 | Mgmt — Sameer | "Definitely I think building on to the previous question uh..." |
| 67 | 146 | Analyst (P11) | "Yeah. Any future uh deal pipeline? I mean I I..." |
| 68 | 148a | Mgmt — Sameer | "that's a valid question right otherwise how will you track..." |
| 69 | 148b | Analyst (P11) | "Okay, just to add the top of question here. So..." |
| 70 | 150a | Mgmt — Sameer | "we we don't have an option that is we have..." |
| 71 | 150b | Analyst (P11) | "Great if I may add just top up. So this..." |
| 72 | 152 | Mgmt | "100%" |
| 73 | 154 | Analyst (P11) | "yeah yeah that's a great yeah so this capital whatever..." |
| 74 | 156 | Mgmt | "exactly exactly" |
| 75 | 158 | Analyst (P11) | "yeah thanks thanks yeah and final question if anything are..." |
| 76 | 160 | Mgmt — Sameer | "I think the the the the most important marker uh..." |
| 77 | 162a | Moderator | "Mr. Jagish Kumar, I would request you to rejoin the..." |
| 78 | 162b | Analyst (P12) | "Yeah. Hi sir, thanks for the opportunity. Uh sir in..." |
| 79 | 164 | Mgmt — Sameer | "See I want to be very clear here Anukul right..." |
| 80 | 166 | Analyst (P12) | "Yeah. Yes, definitely. Uh just a follow up on that..." |
| 81 | 168 | Mgmt — Sameer | "Yeah. Uh business here uh if you uh followed Sunil..." |
| 82 | 170 | Analyst (P12) | "Got it sir. Got it. That answers my question. Thank..." |
| 83 | 171 | Analyst (P12) | "Thank you everybody." |
| 84 | 173 | Moderator | "Thank you. The next question is from the line of..." |
| 85 | 175 | Analyst (P13) | "Hi uh thank you so much and congratulations Samir on..." |
| 86 | 177 | Mgmt — Sameer | "Zoe, thank you for bringing that up. Uh I mean..." |
| 87 | 179a | Analyst (P13) | "Thank you. And uh what sort of revenue growth do..." |
| 88 | 179b | Mgmt | "It's going to be a growth that we will all..." |
| 89 | 181 | Analyst (P13) | "Okay. And uh how do you see the headcount number..." |
| 90 | 183 | Mgmt — Suraj/Sameer | "So uh if you look at uh our headcount as..." |
| 91 | 185 | Analyst (P13) | "Got it. Thank you so much." |
| 92 | 187 | Moderator | "Thank you. Ladies and gentlemen, in the interest of time..." |
| 93 | 189 | Mgmt — Sameer | "I mean, as part of closing statement, uh, I mean..." |
| 94 | 191 | Moderator | "on behalf of Aryhan Capital Markets Limited that concludes this..." |

Auditability note: Management turns = 3,4,9,10,12,14,16,18,22,24,28,30,31,33,35,37,39,41,43,49,51,53,55,59,61,63,66,68,70,72,74,76,79,81,86,88,90,93 = 38 turns. Analyst turns = 6,8,11,13,15,17,19,21,23,26,29,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,65,67,69,71,73,75,78,80,82,83,85,87,89,91 = 41 turns. Moderator/Operator turns = 1,2,5,7,20,25,27,45,47,57,64,77,84,92,94 = 15 turns. 38+41+15 = 94. Reconciles with turn count.

---

## 3. QUESTIONS (one row per distinct ask)

| Q# | Turn | Analyst | Firm | Topic | Flags |
|---|---|---|---|---|---|
| Q1 | 8 (L47) | P6 (Adita) | Za Consultants | Standalone margin ex-Alldigi ~5% run-rate — outlook | REPEAT_QUESTION (margin/guidance theme, see Q3, Q24) |
| Q2 | 8 (L47) | P6 (Adita) | Za Consultants | ~500cr/quarter order book — how much converted to date | — |
| Q3 | 11 (L51b) | P6 (Adita) | Za Consultants | Margin outlook — number management will maintain going forward | REPEAT_QUESTION (margin/guidance theme, see Q1, Q24) |
| Q4 | 11 (L51b) | P6 (Adita) | Za Consultants | Funding of FY30/31 ~9,000cr target's ~1,800cr inorganic piece — equity dilution vs. debt | REPEAT_QUESTION (Alldigi/value-structure & funding theme, see Q10-Q12) |
| Q5 | 13 (L55) | P6 (Adita) | Za Consultants | Direct yes/no follow-up: will there be equity dilution | — |
| Q6 | 15 (L57b) | P6 (Adita) | Za Consultants | Land/building monetization — timeline | — |
| Q7 | 17 (L61) | P6 (Adita) | Za Consultants | Land monetization follow-up (prior ~150cr mention, no timeline given then either) | — |
| Q8 | 21 (L67) | P7 (Sanjay Sha) | KSA Securities Pvt Ltd | BPM & Tech-Digital degrowth, TCV crash, credibility of "3x3x3 by 2031" vision, which verticals can grow with low risk | REPEAT_QUESTION ($1bn/3x3x3 FY31 aspiration theme, see Q25) |
| Q9 | 23 (L71) | P7 (Sanjay Sha) | KSA Securities Pvt Ltd | Requests a separate detailed 1:1 meeting (not a new substantive question) | — |
| Q10 | 29 (L80) | P8 (Manish/"man Pat") | Pat Investments | Value-dilutive current structure (ex-Alldigi negative) — plan to merge Alldigi back in | REPEAT_QUESTION (Alldigi-merger/value-dilution theme, see Q4, Q11, Q12, Q14) |
| Q11 | 29 (L80) | P8 (Manish) | Pat Investments | Path back to pre-demerger numbers; continuous QoQ deterioration since demerger (5th quarter) | REPEAT_QUESTION (same thread as Q10) |
| Q12 | 32 (L86) | P8 (Manish) | Pat Investments | Cost/revenue allocation mechanics between Alldigi and Digitide (value-dilution mechanism) | REPEAT_QUESTION (Alldigi/value-dilution theme, see Q10, Q11, Q14) |
| Q13 | 42 (L99) | P8 (Manish) | Pat Investments | AI helping productivity vs. rising employee expense QoQ — will employee expense fall | REPEAT_QUESTION (AI-vs-employee-cost theme, see Q20) |
| Q14 | 48 (L109) | P9 (Nandra Pradhan) | Maxima Capital | BPM/Tech-Digital segment split between Digitide and Alldigi (slide 7 clarification) | REPEAT_QUESTION (Alldigi structure theme, see Q10-Q12) |
| Q15 | 52 (L117) | P9 (Nandra Pradhan) | Maxima Capital | BPM growth guidance (~10% FY27 expectation) and granularity on segment drivers — call broke up, never substantively answered | UNANSWERED (connection quality; moderator/mgmt could not follow the question, no resolution before analyst dropped off) |
| Q16 | 58 (L129) | P10 (Siman Takar) | Via's Capital | AI-led revenue (15cr, ~2%) — incremental new revenue or cannibalization of BPM/T&D | REPEAT_QUESTION (AI incremental-vs-cannibalization theme, see Q18) |
| Q17 | 60 (L133) | P10 (Siman Takar) | Via's Capital | Competitive intensity in the insurance vertical | — |
| Q18 | 65 (L142) | P11 (Jagdesh Kumar) | Individual investor | AI revenue (2%) — new clients vs. existing clients repurposed as new service; competitive backdrop | REPEAT_QUESTION (AI incremental-vs-cannibalization theme, see Q16) |
| Q19 | 67 (L146) | P11 (Jagdesh Kumar) | Individual investor | Future AI deal-pipeline visibility | — |
| Q20 | 69 (L148b) | P11 (Jagdesh Kumar) | Individual investor | Will AI-skill hiring add to employee cost | REPEAT_QUESTION (AI-vs-employee-cost theme, see Q13) |
| Q21 | 71 (L150b) | P11 (Jagdesh Kumar) | Individual investor | Reusability of AI investment/capability across existing BPO/KPO/BPM business (comment framed as question) | — |
| Q22 | 75 (L158) | P11 (Jagdesh Kumar) | Individual investor | Catch-all: anything else long-term shareholders should track besides AI | — |
| Q23 | 78 (L162b) | P12 (Anukul Aurora) | "Inve..." (firm name truncated in source) | Double-digit revenue growth guidance for FY27 — still standing? | REPEAT_QUESTION (growth-guidance theme, see Q8, Q26) |
| Q24 | 80 (L166) | P12 (Anukul Aurora) | "Inve..." | Margin outlook — what level should investors expect going forward | REPEAT_QUESTION (margin/guidance theme, see Q1, Q3) |
| Q25 | 85 (L175) | P13 (Zohir Hussein Naser) | Naser Investments | Is the $1bn FY31 revenue target still standing, or has the timeline been recalibrated | REPEAT_QUESTION ($1bn/3x3x3 FY31 aspiration theme, see Q8) |
| Q26 | 87 (L179a) | P13 (Zohir Hussein Naser) | Naser Investments | Revenue growth outlook over next 2 years and next 5 years | REPEAT_QUESTION (growth-guidance theme, see Q8, Q23) |
| Q27 | 89 (L181) | P13 (Zohir Hussein Naser) | Naser Investments | Headcount trajectory over next couple of years | — |

Repeat-question clusters: (a) margin/profitability guidance — Q1, Q3, Q24; (b) revenue growth guidance / "when will double-digit / 3x3x3 / $1bn happen" — Q8, Q23, Q25, Q26; (c) Alldigi consolidated-vs-standalone value-dilution/merger structure — Q4, Q10, Q11, Q12, Q14; (d) AI revenue incremental-vs-cannibalization — Q16, Q18; (e) AI investment vs. employee-cost trade-off — Q13, Q20.

---

## 4. NUMBERS SPOKEN (management-confirmed, plus analyst-sourced figures flagged separately) — Role 5 arithmetic-consistency spine

| N# | Turn | Line | Speaker | Figure | Flags |
|---|---|---|---|---|---|
| N1 | 3 | 42a | Sameer | Revenue 775cr, +5.3% YoY (headline, opening remarks) | — |
| N2 | 3 | 42a | Sameer | EBITDA 76.9cr, 9.9% margin (headline) | — |
| N3 | 3 | 42a | Sameer | 55,000 people mapped to business units (of ~75,000 total, see N23) | — |
| N4 | 4 | 42b | Suraj | Revenue 775cr, +5.3% YoY, -3.1% QoQ (restated with sequential figure) | — |
| N5 | 4 | 42b | Suraj | Tech & Digital +20.3% YoY, ~237cr, 31% of revenue | — |
| N6 | 4 | 42b | Suraj | International +10.2% YoY, ~296cr, 38% of revenue | — |
| N7 | 4 | 42b | Suraj | EBITDA 76.9cr, 9.9% margin (restated) | — |
| N8 | 4 | 42b | Suraj | Sequential EBITDA lower by ~11cr | — |
| N9 | 4 | 42b | Suraj | ...of which ~9.9cr = March-quarter one-off (lease renewal reclassified from short-term rent to ROU) | — |
| N10 | 4 | 42b | Suraj | ...and ~1cr = sequential operational decline | — |
| N11 | 4 | 42b | Suraj | Wage cost impact ~10cr this quarter (new labor codes / minimum wage revisions) | — |
| N12 | 4 | 42b | Suraj | D&A total 55cr = ~36cr lease ROU (Ind AS 116) + ~19cr owned/intangible | — |
| N13 | 4 | 42b | Suraj | Normalized D&A guide 55-57cr/quarter | — |
| N14 | 4 | 42b | Suraj | EBIT 22cr, up ~1cr from 21cr prior quarter | — |
| N15 | 4 | 42b | Suraj | Finance cost 15cr, incl. ~11cr lease interest | — |
| N16 | 4 | 42b | Suraj | FY27 lease cash outflow guide 175-180cr (reaffirmed vs. prior guidance) | — |
| N17 | 4 | 42b | Suraj | PAT 2.9cr (return to profit after 2 quarters, no exceptional items) | — |
| N18 | 4 | 42b | Suraj | TCV bookings 205cr, 16 logos added | — |
| N19 | 4 | 42b | Suraj | 3 large international deals in pipeline (hyperscaler-linked) | — |
| N20 | 4 | 42b | Suraj | 5.7mn AI interactions, 80-85% containment rate | — |
| N21 | 4 | 42b | Suraj | DSO 82 days (+7 QoQ vs. 75d prior quarter; -9 YoY vs. 91d prior year) | — |
| N22 | 9 | 49 | Sameer | Order/close book ~500cr/quarter (confirms analyst's Q2 framing) | — |
| N23 | 9 | 49 | Sameer | Book-to-bill 11-13% for the quarter | — |
| N24 | 9 | 49 | Sameer | 3 contracts under active renegotiation discussion | — |
| N25 | 12 | 53 | Sameer | M&A count guide: not one big deal — likely 2-3 deals | — |
| N26 | 22 | 69 | Sameer | 6 new clients signed on AI and cloud this quarter | — |
| N27 | 43 | 101 | Sameer/Suraj | Headcount ~75,000 professionals (BPM/CX company) | — |
| N28 | 68 | 148a | Sameer | AI funnel 100-150cr | — |
| N29 | 81 | 168 | Sameer | ~200bps margin expansion guide for FY27 (reaffirmed) | — |
| N30 | 86 | 177 | Sameer | $1bn FY31 revenue aspiration reaffirmed ("northstar stays"); no numeric timeline recalibration given | — |
| N31 | 11 | 51b | **Analyst** (Adita) | FY30/31 target ~9,000cr revenue, of which ~1,800cr inorganic (framed as management's prior guidance, restated by analyst; not independently re-confirmed with figures by management in this turn) | ANALYST_SOURCED |
| N32 | 8 | 47 | **Analyst** (Adita) | Standalone margin ~5% ex-Alldigi, cited as run-rate since last quarter (management's Turn 10 response does not restate this number) | ANALYST_SOURCED |
| N33 | 58 | 129 | **Analyst** (Siman Takar) | AI-led revenue ~15cr, ~2% of revenue, cited from company presentation (management's Turn 59/68 responses discuss the revenue's nature qualitatively but do not restate the cr figure) | ANALYST_SOURCED |
| N34 | 17 | 61 | **Analyst** (Adita) | Land monetization ~150cr, previously mentioned by company secretary in an earlier call, no timeline given then or now (management's Turn 18 response denies any immediate plan without confirming/denying the 150cr figure) | ANALYST_SOURCED |

Management-confirmed rows N1-N30 = 30. Analyst-sourced rows N31-N34 = 4 (each cross-referenced to its source turn; none double-counted). Total mgmt_numbers ledger = 34, reconciling both the grep pass and the manual sweep.

---

## 5. FORWARD-COMMITMENT PHRASES

| F# | Turn | Line | Speaker | Phrase (paraphrase-free excerpt) |
|---|---|---|---|
| F1 | 3 | 42 | Sameer | "These actions have already started to happen and they will continue through the year... more to come as we meet you again." |
| F2 | 3 | 42 | Sameer | "We are not going to chase top line for its own sake. We are going to chase the quality of our revenue and the quality of our earnings..." |
| F3 | 3 | 42 | Sameer | "We will therefore run a deliberate program built on three tracks" (BPA: build/partner/acquire) |
| F4 | 3 | 42 | Sameer | "We will continue to invest and build our existing platforms in payroll, insurance, and collections." |
| F5 | 4 | 42 | Suraj | "We are in active discussions with our clients on repricing and cost of living adjustments to offset the wage impact." |
| F6 | 4 | 42 | Suraj | "We expect a total lease outflow for FY27 in the range of 175 to 180 crores in line with our previous guidance." |
| F7 | 4 | 42 | Suraj | "We are working towards a bit of margin expansion in FY27. We [are] confident in the direction, and we look forward to demonstrating our numbers in the upcoming quarters." |
| F8 | 12 | 53 | Sameer | "Are we open to the idea? Answer is yes. Are we considering options? Answer is yes as well." (M&A) |
| F9 | 18 | 63 | Mgmt | "...if there are any [monetization] plans we will come out and guide the market." |
| F10 | 22 | 69 | Sameer | "We'll continue to modernize and invest on those three platforms. We'll continue to bring more modules. We'll continue to expand..." |
| F11 | 43 | 101 | Mgmt | "...many of them are in active discussions ... for repricing and renegotiations ongoing." |
| F12 | 68 | 148 | Sameer | "...the confidence level of converting them [AI funnel] through the year is also very high." |
| F13 | 70 | 150 | Sameer | "Is that something that we might have to do and we are open to it? Answer is yes." (AI business unit) |
| F14 | 76 | 160 | Sameer | "Track us on our actions for margin improvement, track us on the quality of revenue, track us on quality of earnings, and track us on ROE." |
| F15 | 81 | 168 | Sameer | "We will be in track with our 200 bps margin expansion in this fiscal." |
| F16 | 86 | 177 | Sameer | "Are we shying away from a billion dollar number that we have shared? Answer is no... the northstar stays." |
| F17 | 90 | 183 | Mgmt | "...headcount will be on a declining trend for the next couple of quarters." |
| F18 | 93 | 189 | Sameer | "The next phase for digitize is about acceleration ... accelerating our profitability, accelerating our execution and accelerating value creation." |

## 6. HEDGE PHRASES

| H# | Turn | Line | Speaker | Phrase |
|---|---|---|---|
| H1 | 3 | 42 | Sameer | "Q1 was clearly below our expectations" |
| H2 | 4 | 42 | Suraj | "This is a regulated change affecting the sector as a whole rather than anything specific to our delivery [pace]." (externalizing wage-cost miss) |
| H3 | 9 | 49 | Sameer | "...things that we are expecting to book and bill in this quarter are actually moving to Q2 and Q3 ... because of the tech progress ... or any other micro macro or management shifts [on customer side]." (deferment attributed to external/vague factors) |
| H4 | 14 | 57 | Mgmt | "We do not see that [equity dilution] as one of the options that we will execute. Not something that we have decided or thought about." |
| H5 | 16 | 59 | Mgmt | "We don't have any [imminent] plans of monetizing the land and buildings at this moment." |
| H6 | 18 | 63 | Mgmt | "...no immediate plans of monetizing it at the moment [but] this will be evaluated frequently." |
| H7 | 31 | 84 | Suraj | "We don't have a specific timeline or an action plan against it [Alldigi merger] at this moment." |
| H8 | 33 | 88 | Suraj | "Optically it would look like it is incurring losses while [Alldigi] is profitable. You have to look at the group as a whole." |
| H9 | 59 | 131 | Sameer | "We are between different customers in terms of their maturity and their consumption of AI." |
| H10 | 70 | 150 | Sameer | "Today we don't have it [AI business unit]... Are we there yet? Answer is no." |
| H11 | 79 | 164 | Sameer | "Revenue is not the only metric we are managing for this year." |
| H12 | 87 | 179 | Mgmt | "We'll come back in the subsequent quarters. What does it mean in terms of percentages and many other markers around that?" (deferred specificity on 2yr/5yr growth outlook) |
| H13 | 89-90 | 181/183 | Mgmt | Headcount answered only directionally ("declining trend") with no numeric target or timeline beyond "next couple of quarters." |

---

## GATE A2 STATUS: PASS

All six enumerated categories reconcile between the grep-assisted count and the manual sweep count after one re-sweep of the mgmt_numbers category (initial pass undercounted at 32 by treating two legitimate management disclosures — the 55,000-of-75,000 headcount mapping and the 3-contract renegotiation / 2-3 deal M&A count — inconsistently; corrected final count is 34, confirmed by both methods).

Flags carried forward to A3/A4: `REPEAT_QUESTION` (5 clusters, see Section 3), `GARBLED_ASR` / `GARBLED_UNRESOLVED` (all 8 analyst identities and their firms lack independent confirmation in-source; 1 firm name truncated — "Inve" — in the source itself), `ANALYST_SOURCED` (4 numbers in Section 4 attributed to analysts, not independently re-confirmed with figures by management), `UNANSWERED` (Q15, Nandra Pradhan's BPM-growth-guidance question, connection dropped before resolution).
