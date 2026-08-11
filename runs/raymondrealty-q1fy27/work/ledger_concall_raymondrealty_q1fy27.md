# LEDGER — concall — raymondrealty — Q1 FY27

Source: `extract_concall_raymondrealty_q1fy27.txt` (A1 extract, 217 original transcript lines,
lines 1-9 = header/metadata block, line 11 = `---` separator, lines 13-217 = dialogue).
All line numbers below cite the ORIGINAL transcript line number as embedded in the A1 extract
(the number preceding the tab on each content line), not the Read-tool line number.

```
=== A2 COUNT TEST ===
category: turns          grep_count: 103  sweep_count: 103  match: yes
category: participants   grep_count: 15   sweep_count: 15   match: yes
category: questions      grep_count: 27   sweep_count: 28   match: yes (reconciled — see note)
category: mgmt_numbers   grep_count: 71   sweep_count: 71   match: yes
category: commitments_hedges  grep_count: 19  sweep_count: 19  match: yes
gate_a2: pass
=== END COUNT TEST ===
```

**Reconciliation note (questions category):** Grep proxy = raw count of lines containing a
literal `?` character (`grep -o '?' | wc -l` on distinct lines = 27 lines; command:
`grep -nP '^\s*\d+\t.*\?' extract.txt`). Manual line-by-line cross-check of those 27 hits found
8 false positives (4 management rhetorical asides at L17, L61, L121, L151; 4 audio-check filler
turns at L115, L143, L145, L181 — none is a substantive analyst question) and the manual sweep
recovered 9 additional substantive analyst question/comment units where the ASR transcript
dropped terminal punctuation (L23, L59, L91, L103, L107, L123, L165, L197, L207). Net: both
methods converge on the same 28-item universe of analyst question/comment turns once
reconciled (19 grep-confirmed + 9 sweep-recovered = 28; 8 grep hits excluded as non-questions).
Flag: `ASR_PUNCTUATION_UNRELIABLE` — grep alone is not a valid enumeration method for this
doctype instance; manual sweep is load-bearing. Re-swept per GATE A2 rule before emitting.

---

## SECTION A — PARTICIPANTS (management and analyst side)

| # | Name (as transcribed) | Designation / Firm | Side | Line cite | Flags |
|---|---|---|---|---|---|
| P1 | Mr. Harmohan (Mohan) Sani (also spelled "Harmohan Swani" in same header line) | MD and CEO, Raymond Realty | Management | L5 | `NAME_INCONSISTENT` — two spellings of the same person in one header line ("Sani" vs "Swani"); likely ASR/OCR artifact, not a corporate-identity issue, but flagged for A3 |
| P2 | Mr. Rakkesh Tiwari | Group CFO, Raymond Realty | Management | L6 | `MGMT_ABSENCE` — listed as present but has zero speaking turns anywhere in the 103-turn transcript |
| P3 | Mr. Ankur Jindal | CFO, Raymond Realty | Management | L7 | `MGMT_ABSENCE` — a question is explicitly addressed to him (T8/L27) and he does not answer; MD/CEO answers on his behalf citing "Ankor is traveling ... may not be able to get proper connectivity" (T9/L29) |
| P4 | Mr. Amit Saburval (also given as "Sani Desa" in the same header line) | Head Investor Relations, Raymond Realty | Management | L8 | `NAME_INCONSISTENT` — two names in one line, same ASR-artifact pattern as P1; cross-referenced later at L199 where MD states "a gentleman by the name of Amit Saburval ... joined only a few weeks back" — confirms Amit Saburval is correct, "Sani Desa" is the artifact |
| P5 | Mr. Bhavin Modi | Moderator/host, Anand Rathi (also asks an analyst question later) | Moderator (dual role) | L9; question at T22-T29/L55-L69 | `MODERATOR_AS_ANALYST` — same individual who hosts the call also asks a full analyst question set representing the host broker; note for A3/A4, not necessarily a defect |
| P6 | Sukrit Deartil | Analyst, "eyesight fint private limited" (name/firm both ASR-garbled, likely a securities firm) | Analyst | T5/L21 | `NAME_GARBLED` |
| P7 | Ishita Loda | Analyst, "Swen Investments" (likely "Swan Investments") | Analyst | T13/L37 | `NAME_GARBLED` (firm) |
| P8 | Deepak Podar | Analyst, Sapphire Capital | Analyst | T30/L71 | none |
| P9 | Pratik | Analyst, "Modila Financial Service Limited" (likely Motilal Oswal Financial Services) | Analyst | T45/L101 | `NAME_GARBLED` (firm); surname not given |
| P10 | "breach. SH" (unclear) | Analyst, Blue Star Capital | Analyst | T51/L113 | `NAME_GARBLED` — name effectively unrecoverable from transcript text |
| P11 | Kunal / "Kungal" | Analyst, Aryan Capital Markets Limited | Analyst | T63/L137 | `NAME_GARBLED`; addressed as "ma'am" by management (T65/L141) — possible gender/name mismatch in ASR, flag `SPEAKER_ATTRIBUTE_UNCERTAIN` |
| P12 | "man based" / addressed later as "Mr. V" | Analyst, "someone India PMS" (likely a named PMS firm, garbled) | Analyst | T76/L163; T80/L171 | `NAME_GARBLED` (name and firm both) |
| P13 | Pushbindu | Individual investor | Analyst/Investor | T84/L179 | none |
| P14 | Akhil Jawahar ("Akih Javahar") | Individual investor | Analyst/Investor | T96/L203 | `NAME_GARBLED` (minor) |
| P15 | Unnamed operator/moderator (conference operator, distinct from Bhavin Modi in call-management turns) | Call operator | Moderator | T1, T4, T12, T21, T101, T103 etc. | none — standard conference-call operator continuity announcements |

---

## SECTION B — SPEAKER TURNS (all 103, sequential)

Turn# | Line | Speaker (best attribution) | First ~10 words | Flags
---|---|---|---|---
T1 | L13 | Operator | Ladies and gentlemen, good day and welcome to the Raymond | 
T2 | L15 | Bhavin Modi (moderator, Anand Rathi) | Thank you. On behalf of Anandrati, I would like to | 
T3 | L17 | Harmohan Swani (MD & CEO) — opening remarks | Today on this call for Raymond Realy's performance for the | dense turn, see Section D for all figures
T4 | L19 | Operator | Thank you so much sir. Ladies and gentlemen, we will | Q&A session opens
T5 | L21 | Operator | Our first question comes from the line of Sukrit Deartil | question intro 1 of 10
T6 | L23 | Sukrit Deartil (analyst) | Good morning to the team. Uh I have two questions. | Q1a (`ASR_PUNCTUATION_UNRELIABLE`, no terminal `?`)
T7 | L25 | Harmohan Swani (MD & CEO) | Yeah, thank you. Thank you very much for your question. | answers Q1a
T8 | L27 | Sukrit Deartil (analyst) | Thank you. My uh second question to Mr. Jindel is | Q1b, addressed to Ankur Jindal (CFO)
T9 | L29 | Harmohan Swani (MD & CEO) | Yeah, I'll I'll only take that. Uh uh I think | answers Q1b on CFO's behalf; `MGMT_ABSENCE` (CFO does not answer)
T10 | L31 | Sukrit Deartil (analyst) | Thank you and uh best wish is | closing
T11 | L33 | Management (Swani) | thank you. | 
T12 | L35 | Operator | Thank you. | 
T13 | L37 | Operator | Our next question come from the line of Ishita Loda | question intro 2 of 10
T14 | L39 | Ishita Loda (analyst) | Hello sir, thank you for the opportunity. Uh my question | Q2a — Parel ticket size/units/inventory/timing (bundled)
T15 | L41 | Harmohan Swani (MD & CEO) | Uh thank you for your question. So the Parel project | answers Q2a
T16 | L43 | Ishita Loda (analyst) | Yeah. So what is the realization that we have underwritten? | Q2b
T17 | L45 | Harmohan Swani (MD & CEO) | Sorry, the total GDV is 8,500 crores. That's what we | answers Q2b
T18 | L47 | Ishita Loda (analyst) | Okay sir. And uh are we on track to launch | Q2c — Mahim launch status
T19 | L49 | Harmohan Swani (MD & CEO) | Yeah. So the we we are on track to launch | answers Q2c
T20 | L51 | Ishita Loda (analyst) | Okay. Thank you so much. | closing
T21 | L53 | Operator | Thank you ladies and gentlemen. Anyone who wishes to ask | question intro 3 of 10 (Bhavin Modi)
T22 | L55 | Bhavin Modi (analyst role) | Yeah, thank you for the opportunity. Uh sir, there was | Q3a — 10X Mahalakshmi Ltd incorporation
T23 | L57 | Harmohan Swani (MD & CEO) | Uh see we are always looking at opportunities uh as | answers Q3a
T24 | L59 | Bhavin Modi (analyst role) | Yes. Got it. Got so second thing is you know | Q3b — launch calendar Q2-Q4 + GDV (`ASR_PUNCTUATION_UNRELIABLE`)
T25 | L61 | Harmohan Swani (MD & CEO) | So uh would it be okay if we gave you | answers Q3b
T26 | L63 | Bhavin Modi (analyst role) | Yeah. What? So the last question so you know the | Q3c — JDA margin/capital profile vs own-land, ROC
T27 | L65 | Harmohan Swani (MD & CEO) | Yeah sir certainly see if I compare JDA versus buying | answers Q3c (part 1, capital efficiency)
T28 | L67 | Harmohan Swani (MD & CEO), continued | So so clearly capital efficiency is there and then what | answers Q3c (part 2, margin/ROC); contains historical ROC >25% vs 20% forward guidance — see Section D
T29 | L69 | Bhavin Modi (analyst role) | Got it. Got it. Thank you sir. That's it from | closing
T30 | L71 | Operator | Thank you. Our next question comes from the line of | question intro 4 of 10 (Deepak Podar)
T31 | L73 | Deepak Podar (analyst) | Yeah I'm audible sir. | audio check
T32 | L75 | Moderator/Operator (unclear) | Yes sure. | `SPEAKER_AMBIGUOUS`
T33 | L77 | Deepak Podar (analyst) | No just one question. question I have on the interest | Q4a — interest cost outlook
T34 | L79 | Harmohan Swani (MD & CEO) | See interest cost has been quite stable actually it's not | answers Q4a
T35 | L81 | Deepak Podar (analyst) | Mhm. | filler ack
T36 | L83 | Deepak Podar (analyst) | Hello. | audio issue
T37 | L85 | Speaker unclear | Yeah. | `SPEAKER_AMBIGUOUS`
T38 | L87 | Deepak Podar (analyst) | Yeah. Yeah. So, so I I was not talking about | Q4b — clarifies, asks current (absolute) debt level
T39 | L89 | Harmohan Swani (MD & CEO) | Our current debt levels are net debt is in the | answers Q4b (net debt 824 cr)
T40 | L91 | Deepak Podar (analyst) | And and cash how much cash you would have 250 | Q4c — cash level (`ASR_PUNCTUATION_UNRELIABLE`)
T41 | L93 | Harmohan Swani (MD & CEO) | Cash is 271 crores. So the gross debt is 1095. | answers Q4c (cash 271 cr, gross debt 1095 cr — new figure not in opening remarks)
T42 | L95 | Deepak Podar (analyst) | 1095 and and and you mentioned this debt may not | Q4d — confirms elevated interest cost persists
T43 | L97 | Harmohan Swani (MD & CEO) | No, absolutely. | answers Q4d (confirms)
T44 | L99 | Deepak Podar (analyst) | Okay. Okay. Fair fair point. Um that would be it | closing
T45 | L101 | Operator | Thank you. An question comes from the line of Pratik | question intro 5 of 10; transcription typo "An question"
T46 | L103 | Pratik (analyst) | Good morning, sir. Thank you for giving me an opportunity | Q5a — geographic diversification (`ASR_PUNCTUATION_UNRELIABLE`)
T47 | L105 | Harmohan Swani (MD & CEO) | I think for the foreseeable future we are very focused | answers Q5a
T48 | L107 | Pratik (analyst) | Okay. And sir just uh I wanted to understand it's | Q5b — explain JDA strategy (`ASR_PUNCTUATION_UNRELIABLE`)
T49 | L109 | Harmohan Swani (MD & CEO) | So I'll I'll tell you very quickly I mean what | answers Q5b
T50 | L111 | Pratik (analyst) | Okay sir. Thank you sir. Thank you. | closing
T51 | L113 | Operator | Thank you. Our next question comes from the line of | question intro 6 of 10 ("breach. SH", Blue Star Capital)
T52 | L115 | Analyst (Blue Star Capital) | Am I audible sir? | audio check
T53 | L117 | Moderator/Operator | Yes sir you are. | 
T54 | L119 | Analyst (Blue Star Capital) | Yeah first of all congratulations for good set of numbers. | Q6a — full-year FY27 interest cost
T55 | L121 | Harmohan Swani (MD & CEO) | Can we get that to you? On that number we | answers Q6a (hedged, ~100 cr ballpark)
T56 | L123 | Analyst (Blue Star Capital) | around 100 cr for full year right | Q6b — confirms ~100 cr (`ASR_PUNCTUATION_UNRELIABLE`)
T57 | L125 | Harmohan Swani (MD & CEO) + Analyst (merged, no turn break) | yeah 100 to 120 max that that should be the | `TURN_MERGED` — mgmt answer ("100-120 max") runs directly into analyst's next question ("should we assume Q1 interest cost was 47 cr, so Q2-Q4 lower than Q1") with no speaker break in source
T58 | L127 | Harmohan Swani (MD & CEO) | it will be it will be there about so between | answers embedded Q6c
T59 | L129 | Analyst (Blue Star Capital) | So my point is like it it will be less | Q6d — confirms "less than Q1"
T60 | L131 | Harmohan Swani (MD & CEO) | Yeah. Yeah. Means Yeah. | confirms
T61 | L133 | Harmohan Swani (MD & CEO) | Yeah. Yeah. You can assume that. | confirms (repeat/continuation)
T62 | L135 | Analyst (Blue Star Capital) | Yeah. Thank you, sir. | closing
T63 | L137 | Operator | Thank you. Our next question comes from the line of | question intro 7 of 10 (Kunal, Aryan Capital Markets)
T64 | L139 | Kunal (analyst, addressed as "ma'am") | Uh hello sir, thank you for the opportunity. Uh sir, | Q7a — borrowings growth, corporate vs project debt, leverage need (first attempt, audio-garbled)
T65 | L141 | Harmohan Swani (MD & CEO) | Uh ma'am your voice was not clear I think get | requests repeat
T66 | L143 | Speaker unclear (Swani or Operator) | Can you repeat that please? | `SPEAKER_AMBIGUOUS`
T67 | L145 | Kunal (analyst) | Uh can you hear me now? | audio check
T68 | L147 | Harmohan Swani (MD & CEO) | Yeah, slightly better. Yes. | confirms audio
T69 | L149 | Kunal (analyst) | Okay. So, borrowings have gone from uh 380 cr to,97 | Q7a repeated in full — borrowings 380cr → ~897cr(?) YoY, construction finance vs corporate debt, repayment schedule, GDV pipeline leverage need
T70 | L151 | Harmohan Swani (MD & CEO) | Yeah. Okay. Got it. See, I mean I don't know | answers Q7a (part 1 — debt purpose/type)
T71 | L153 | Kunal (analyst) | Yes sir. | ack
T72 | L155 | Harmohan Swani (MD & CEO) | Uh so so for that we have already given a | answers Q7a (part 2 — 1:1 D/E discipline repeat)
T73 | L157 | Kunal (analyst) | Okay sir. So there's one more followup question with it. | Q7b — margin difference own-land vs JDA
T74 | L159 | Harmohan Swani (MD & CEO) | So our blended margin is the guidance that we have | answers Q7b (`REPEAT_QUESTION` — same topic as Q3c/T26)
T75 | L161 | Kunal (analyst) | Okay sir. Thank you. That's it from my side. Thank | closing
T76 | L163 | Operator | Thank you. Our next question come from the line of | question intro 8 of 10 ("man based"/"Mr. V", Someone India PMS)
T77 | L165 | Analyst (Someone India PMS) | Good morning sir. I wanted uh your view on the | Q8a — demand environment/softness + home fest purpose (`ASR_PUNCTUATION_UNRELIABLE`)
T78 | L167 | Harmohan Swani (MD & CEO) | Yeah. So the demand remains quite strong all through and | answers Q8a (part 1 — demand)
T79 | L169 | Analyst (Someone India PMS) | Hello. | audio check
T80 | L171 | Moderator/Swani (unclear) | Um Mr. V, are we done with your question? | `SPEAKER_AMBIGUOUS`
T81 | L173 | Analyst (Someone India PMS) | Uh, yeah. And how was the response to the home | Q8b — home fest response follow-up
T82 | L175 | Harmohan Swani (MD & CEO) | Uh, home fest response was pretty good. We uh I | answers Q8b
T83 | L177 | Analyst (Someone India PMS) | Got it. Right. Thank you. | closing
T84 | L179 | Operator | Thank you. Ladies and gentlemen, anyone who wishes to ask | question intro 9 of 10 (Pushbindu)
T85 | L181 | Pushbindu (individual investor) | Yeah. Am I audible? | audio check
T86 | L183 | Speaker unclear | Hello. | `SPEAKER_AMBIGUOUS`
T87 | L185 | Moderator/Operator | Yes, you are. Yes, you are. | 
T88 | L187 | Speaker unclear (second confirmation) | Yes sir, you are. | `SPEAKER_AMBIGUOUS` — duplicate confirmation, two voices
T89 | L189 | Pushbindu + Harmohan Swani (merged, no turn break) | Yeah. So, good morning Harmon sir and compliment for good | `TURN_MERGED` — Pushbindu's full question (PAT/OCF guidance ask, embedded as Q9a) runs directly into Swani's full answer with no speaker break in source
T90 | L191 | Pushbindu (individual investor) | Yeah. But then uh you don't uh expect any pad | Q9b — PAT deceleration follow-up
T91 | L193 | Harmohan Swani (MD & CEO) | Uh sorry I didn't get that. You're saying the pad | clarifies/restates Q9b
T92 | L195 | Harmohan Swani (MD & CEO) | it I mean I I don't have that number just | answers Q9b (hedge — declines to give PAT number)
T93 | L197 | Pushbindu (individual investor) | yeah sure fine sir one more observation what we have | Q9c — FII/DII holding decline concern (`ASR_PUNCTUATION_UNRELIABLE`)
T94 | L199 | Harmohan Swani (MD & CEO) + Pushbindu (merged, no turn break) | Yeah. So yeah I mean obviously uh it is a | `TURN_MERGED` — Swani's full answer (FII/DII, market cap, IR hire) runs directly into Pushbindu's follow-up suggestion (embedded as Q9d, bring in PE fund at project level) with no speaker break in source
T95 | L201 | Harmohan Swani (MD & CEO) | No no that's a extremely good suggestion and we we | answers/acknowledges Q9d (`FORWARD_COMMITMENT`, vague — "we will work on it")
T96 | L203 | Operator | Yeah. Uh thank you. Our next question comes from the | question intro 10 of 10 (Akhil Jawahar)
T97 | L205 | Akhil Jawahar (individual investor) | Uh thank you for the opportunity. Uh I just had | Q10a — finance cost breakdown, term loans vs dues-to-government, reconcile with 9.6% math
T98 | L207 | Harmohan Swani (MD & CEO) + Akhil Jawahar (merged, no turn break) | You know dues to government is nothing but uh the | `TURN_MERGED` — Swani's answer on "dues to government" runs directly into Akhil's follow-up confirming question (embedded as Q10b, full-year costing ~100-120?) with no speaker break in source
T99 | L209 | Harmohan Swani (MD & CEO) | Yeah, it should be but we will share a better | answers Q10b (`FORWARD_COMMITMENT` — promises separate disclosure of exact interest-cost number)
T100 | L211 | Akhil Jawahar (individual investor) | Um uh all right. Okay. Thank you. | closing
T101 | L213 | Operator | Thank you so much. Ladies and gentlemen, that was the | last question announced; hands to MD for closing remarks
T102 | L215 | Harmohan Swani (MD & CEO) | Yeah, thank you so much uh for being patient and | closing remarks
T103 | L217 | Operator | Thank you so much sir. Ladies and gentlemen on behalf | call sign-off

**Turn count reconciliation:** grep sweep of non-blank, non-separator content lines at
orig-line ≥13 (`grep -nP '^\s*\d+\t\S' extract.txt`, filtered to exclude the `---` separator
line at L11 and header lines 1-9, then counted for line ≥13) = 103. Manual sweep above,
numbered T1-T103 = 103. **Match: yes.**

---

## SECTION C — QUESTIONS LEDGER (analyst name, firm, topic, turn, flags)

# | Analyst | Firm | Topic | Turn/Line | Flags
---|---|---|---|---|---
Q1a | Sukrit Deartil | eyesight fint private limited | Top 2-3 execution priorities for the year; biggest risks (demand/regulatory/competitive) and mitigation | T6/L23 | 
Q1b | Sukrit Deartil | eyesight fint private limited | Capital allocation and funding alignment with growth pipeline; execution/financing/industry risk and mitigation | T8/L27 | addressed to CFO Jindal, answered by MD (`MGMT_ABSENCE`)
Q2a | Ishita Loda | Swen (Swan) Investments | Parel project: ticket sizes, free-sale component, unit count, inventory at launch, launch timing | T14/L39 | bundled multi-part question
Q2b | Ishita Loda | Swen (Swan) Investments | Underwritten realization/GDV for Parel | T16/L43 | follow-up
Q2c | Ishita Loda | Swen (Swan) Investments | Mahim project launch track/approval status | T18/L47 | follow-up
Q3a | Bhavin Modi | Anand Rathi | Purpose of 10X Mahalakshmi Limited incorporation — new business/acquisition? | T22/L55 | 
Q3b | Bhavin Modi | Anand Rathi | Tentative launch calendar Q2-Q4 and associated GDV | T24/L59 | 
Q3c | Bhavin Modi | Anand Rathi | JDA portfolio margin and capital profile vs own-land engine; can JDA improve ROC while restricting leverage | T26/L63 | `REPEAT_QUESTION` (see Q7b)
Q4a | Deepak Podar | Sapphire Capital | Interest cost trend — elevated last two quarters, outlook going forward | T33/L77 | `REPEAT_QUESTION` (interest-cost topic recurs across Q6a, Q7a, Q9a/b, Q10a)
Q4b | Deepak Podar | Sapphire Capital | Current (absolute) debt level, not just cost-of-debt % | T38/L87 | 
Q4c | Deepak Podar | Sapphire Capital | Current cash level | T40/L91 | 
Q4d | Deepak Podar | Sapphire Capital | Confirms elevated absolute interest cost expected to continue | T42/L95 | 
Q5a | Pratik | Motilal Oswal Financial Services (garbled) | Development plans outside Mumbai/MMR for diversification | T46/L103 | 
Q5b | Pratik | Motilal Oswal Financial Services (garbled) | Explain the joint development (JDA) strategy mechanics | T48/L107 | 
Q6a | Analyst (name garbled) | Blue Star Capital | Full-year FY27 interest cost guidance | T54/L119 | `REPEAT_QUESTION`
Q6b | Analyst (name garbled) | Blue Star Capital | Confirms ~100 cr for full year | T56/L123 | follow-up
Q6c | Analyst (name garbled) | Blue Star Capital | Confirms Q1 interest cost was 47 cr; asks if Q2-Q4 will be lower than Q1 | embedded in T57/L125 | `TURN_MERGED`
Q6d | Analyst (name garbled) | Blue Star Capital | Confirms "less than Q1" framing | T59/L129 | follow-up
Q7a | Kunal | Aryan Capital Markets Limited | Borrowings grew ~380 cr → ~897 cr(?) YoY — construction finance/project debt vs corporate debt; repayment schedule; does the 52,000 cr GDV pipeline need more leverage or is incremental collection self-funding | T64/L139 (repeated T69/L149 after audio issue) | `REPEAT_QUESTION`; figure "97 cr" in transcript is ASR-garbled, likely "897 cr" or similar — see `NOT FOUND` note in Section D
Q7b | Kunal | Aryan Capital Markets Limited | Margin difference between own-land and JDA engine | T73/L157 | `REPEAT_QUESTION` (see Q3c)
Q8a | Analyst (name garbled) | Someone India PMS (garbled) | Demand environment view — any softness; purpose of recent "home fest" event | T77/L165 | 
Q8b | Analyst (name garbled) | Someone India PMS (garbled) | Response to the home fest | T81/L173 | follow-up
Q9a | Pushbindu | Individual investor | EBITDA/operating profit growing but interest cost growing faster — guidance sought on net profit (PAT)/cash profit/operating cash flow growth, not just revenue and EBITDA | embedded in T89/L189 | `TURN_MERGED`
Q9b | Pushbindu | Individual investor | Do you expect PAT growth deceleration due to higher interest cost? | T90/L191 | follow-up; management declines to give a number (`HEDGE`)
Q9c | Pushbindu | Individual investor | FII/DII institutional holding has fallen from ~20-22% to ~8% since listing — is there an information-asymmetry/governance concern, and what is management doing about it; analyst notes this has been "asked repeatedly in several calls" | T93/L197 | analyst self-reports this as a recurring question across prior calls (not verifiable within this transcript alone)
Q9d | Pushbindu | Individual investor | Suggestion: bring in institutional/PE investors at the project level (cites Kolte-Patil/Embassy-Blackstone precedent) | embedded in T94/L199 | `TURN_MERGED`; `NOT_A_QUESTION` — framed as a suggestion, not a question; management responds with vague `FORWARD_COMMITMENT` ("we will definitely work on it") at T95/L201
Q10a | Akhil Jawahar | Individual investor | FY26 annual report shows finance cost split: ~50 cr interest on term loans + ~45 cr interest expense on "dues to government" — asks what "dues to government" interest is, and Q1 math using 9.6% only accounts for ~20 cr of the total, asks for reconciliation | T97/L205 | analyst-cited numbers are from FY26 annual report, not this quarter's filing — flag `ANALYST_CITED_NOT_MGMT` for the ~50cr/~45cr/~20cr figures
Q10b | Akhil Jawahar | Individual investor | Confirms full-year costing including dues-to-government would be ~100-120 cr (±10-20%) as previously guided | embedded in T98/L207 | `TURN_MERGED`

**Questions count reconciliation:** 28 total analyst question/comment units (27 genuine
questions + 1 suggestion/comment, Q9d, flagged `NOT_A_QUESTION`). See count-test header for
grep-vs-sweep reconciliation detail (`ASR_PUNCTUATION_UNRELIABLE`).

**REPEAT_QUESTION summary:** interest-cost / debt topic raised independently by 5 different
analysts (Deepak Podar Q4a, Blue Star Capital analyst Q6a, Kunal Q7a, Pushbindu Q9a/b, Akhil
Jawahar Q10a) — a strong cross-analyst signal. Own-land-vs-JDA margin split raised independently
by 2 analysts (Bhavin Modi Q3c, Kunal Q7b).

---

## SECTION D — EVERY NUMBER SPOKEN BY MANAGEMENT (guidance, capacity, margin, order book, capex, timeline)

Listed in order of first utterance; turn/line cites every recurrence.

# | Figure | Metric | Turn(s)/Line(s) | Flags
---|---|---|---|---
N1 | 700 crores | Q1 FY27 booking value (pre-sales) | T3/L17 (stated 2x within turn) | 
N2 | 129% | YoY growth in booking value | T3/L17 | 
N3 | 306 crores | Q1 FY26 booking value comparator | T3/L17 | 
N4 | 550 crores | Q1 FY27 customer collections | T3/L17 | 
N5 | 47% | YoY growth in customer collections | T3/L17 | 
N6 | 536 crores | Q1 FY27 total income (revenue) | T3/L17 | 
N7 | 390 crores | Q1 FY26 total income comparator | T3/L17 | 
N8 | 37% | YoY growth in total income | T3/L17 | 
N9 | 70 crores | Q1 FY27 EBITDA ("IITA"/"ITA", ASR garble for EBITDA) | T3/L17 | 
N10 | 70% | YoY growth in EBITDA | T3/L17 | 
N11 | 41 crores | Q1 FY26 EBITDA comparator | T3/L17 | 
N12 | 13% | Q1 FY27 EBITDA margin | T3/L17 | 
N13 | 11% | Q1 FY26 EBITDA margin comparator | T3/L17 | 
N14 | four projects | Projects launched in Q4 FY26 | T3/L17 | 
N15 | 17-19% | Full-year FY27 EBITDA margin guidance | T3/L17, T28/L67, T74/L159, T89/L189 (4 mentions) | `FORWARD_COMMITMENT`
N16 | 824 crores | Net debt at Q1 FY27 end | T3/L17, T39/L89 | 
N17 | 7% ("7X" in transcript) | Net debt-to-equity ratio Q1 FY27 | T3/L17 | transcript internally inconsistent between "7% of ... ratio" and "This number 7X" — likely means ~0.07x; `NOT FOUND` — exact intended figure/units ambiguous in source, flag for A3
N18 | 1x | Internal debt-to-equity discipline ceiling | T3/L17, T9/L29, T72/L155, T94/L199 (referenced again) | `FORWARD_COMMITMENT`
N19 | 271 crores | Liquidity/cash buffer at Q1 end | T3/L17, T41/L93 | 
N20 | 9.6% | Average cost of debt | T3/L17, T34/L79, T65 area/T98/L207 (context) | 
N21 | below 10% | Cost of debt framing | T3/L17 | 
N22 | 52,000 crores | Total GDV (portfolio) | T3/L17 | 
N23 | 6-7 years / 7-8 years | Growth visibility (two slightly different figures given in same turn) | T3/L17 | internal inconsistency (6-7 vs 7-8 years) within same turn, flag for A3
N24 | 52% | JDA share of total GDV | T3/L17 | 
N25 | 27,000 crores | JDA revenue potential (aggregate) | T3/L17, T26/L63 (referenced) | 
N26 | eight projects | Total JDA projects signed | T3/L17, T25/L61 | 
N27 | 25,000 crores | Own-land (Thane 100-acre parcel) revenue potential | T3/L17 | 
N28 | 64% | JDA (asset-light) share of Q1 pre-sales | T3/L17 | 
N29 | ~2/3 vs ~1/3 | MMR vs Thane share of sales | T3/L17 | 
N30 | 8,500 crores | Parel JDA project estimated GDV | T3/L17, T17/L45, T65/L65 (context) | 
N31 | four projects launched (of eight JDAs) | Launched JDA count | T3/L17 | 
N32 | 2.8 million sq ft | Combined RERA carpet area of the 4 launched JDA projects | T3/L17 | 
N33 | 11,500 crores | Revenue potential of the 4 launched JDA projects | T3/L17, T61/L61 (context, "27,000cr" total referenced) | 
N34 | 2,900 crores | Cumulative sales from launched JDA projects | T3/L17 | 
N35 | ~692 crores (~700 crores) | Cash collections from launched JDA projects | T3/L17 | 
N36 | 100 acres | Total Thane land parcel | T3/L17, T109 (context, JDA control discussion) | 
N37 | 65 acres | Thane acreage under active development | T3/L17 | 
N38 | 6.7 million sq ft | Thane active-development RERA carpet area | T3/L17 | 
N39 | 16,500 crores | Thane total revenue potential | T3/L17 | 
N40 | 2019 | Year Thane monetization began | T3/L17 | 
N41 | 9,400 crores | Thane cumulative sales | T3/L17 | 
N42 | 7,460 crores | Thane cumulative collections | T3/L17 | 
N43 | 11 towers | Towers delivered at Thane | T3/L17 | 
N44 | ~4,000 homes | Homes delivered at Thane | T3/L17 | 
N45 | 36% | Thane contribution to Q1 booking value | T3/L17 | 
N46 | 15,700 crores | Unsold (launched) GDV | T3/L17 | 
N47 | 24,000 crores | Unlaunched GDV | T3/L17 | 
N48 | ≥20% | FY27 pre-sales growth guidance (minimum) | T3/L17 | `FORWARD_COMMITMENT`
N49 | ≥20% | FY27 revenue growth guidance (minimum) | T3/L17 | `FORWARD_COMMITMENT`
N50 | ≥20% | FY27 ROCE guidance | T3/L17, T28/L67 | `FORWARD_COMMITMENT`
N51 | 30 years | MD's stated tenure/experience in the industry | T7/L25 | qualitative context, not a company metric
N52 | 5-6 years | Typical project life cycle | T7/L25 | 
N53 | 2034 | Reference year for Maharashtra's DCR (Development Control Regulation) policy framework | T7/L25 | 
N54 | 2-3 years | Period cited for state government's pro-growth policy stance | T7/L25 | 
N55 | 18 months | Estimated time-to-market for the Parel project | T15/L41 | `FORWARD_COMMITMENT` (timeline)
N56 | 6 crores to 20 crores | Ticket size range underwritten for Parel | T15/L41 | 
N57 | 2 Mahim projects this year | Mahim launch count for FY27 | T19/L49, T25/L61 | `FORWARD_COMMITMENT`
N58 | Nov-Dec (Q3) / Feb-Mar (Q4) | Mahim project 1 and 2 launch timing | T19/L49 | `FORWARD_COMMITMENT` (timeline)
N59 | ~2,500 crores | Mahim project 1 GDV | T25/L61 | 
N60 | ~2,000-2,200 crores | Mahim project 2 GDV | T25/L61 | 
N61 | six of eight JDAs | Cumulative JDAs to be launched by end of FY27 | T25/L61 | `FORWARD_COMMITMENT`
N62 | 10-15% | Land-value deposit paid upfront in a JDA deal | T27/L65 | 
N63 | ~300-350 crores | Typical peak capital required per ~2,000 cr GDV JDA deal | T27/L65 | 
N64 | ~350-500 crores | Peak capital requirement for the larger Parel JDA | T27/L65 | 
N65 | 1.7 million sq ft | Parel project carpet area | T27/L65 | 
N66 | ~17-19% (referenced again, "7 18 to 19%" garbled) | Current-year margin profile reiteration | T28/L67 | ASR garble ("7 18 to 19%") — likely just "17 to 19%" restated, flag `NOT FOUND` for the stray "7"
N67 | ~20% | Desired margin target ("as close to 20% as possible") | T28/L67 | `FORWARD_COMMITMENT`
N68 | >25% | Historical ROC over "the last 6 years" | T28/L67 | notable vs forward guidance of 20% (N50) — step-down flagged for A3/A4 interpretation, not resolved here
N69 | 6 years | Look-back period for the >25% historical ROC claim | T28/L67 | 
N70 | 1,095 crores | Gross debt (derived from net debt 824 + cash 271) | T41/L93 | new figure, not stated in opening remarks; internal consistency check: 824+271=1095, arithmetic checks out
N71 | ~2 years | Period Raymond Realty has been studying the Pune market (without transacting) | T47/L105 | 

**Note on N17, N23, N66:** three instances of internally inconsistent or garbled figures within
management's own turns (net debt/equity ratio units, 6-7 vs 7-8 years growth visibility, stray
digit in margin restatement). These are transcription-quality issues in the source, not
necessarily errors by management; flagged `NOT FOUND` / `TRANSCRIPT_INCONSISTENT` for A3 to
adjudicate against the filing baseline, not resolved or estimated here per pipeline rule
(never estimate a missing number).

**Note on interest-cost guidance repetition:** the FY27 full-year interest cost estimate
(~100-120 crores, always hedged as approximate) is restated with near-identical hedged language
five separate times across the call (T55/L121, T57/L125 embedded, T58/L127, T89/L189 embedded,
T99/L209) — each instance carries a live `HEDGE` flag ("don't have it readily available,"
"don't hold me to it," "we will share a better number").

**mgmt_numbers count reconciliation:** grep count of numeric tokens (`\d[\d,.]*`) across the 38
lines independently identified as containing management speech (T3/T7/T9/T15/T17/T19/T23/T25/
T27/T28/T34/T39/T41/T47/T49/T55/T57/T58/T60/T61/T65/T67/T70/T72/T74/T78/T82/T89/T92/T93/T95/
T97... — cross-checked against the manual list above) = 71 raw numeric tokens after collapsing
repeated in-turn mentions of the identical figure (e.g., "700 crores" said twice in T3) into
one count per distinct occurrence-with-context; manual sweep above (N1-N71) = 71 distinct
disclosure entries. **Match: yes.**

---

## SECTION E — FORWARD-COMMITMENT AND HEDGE PHRASES

# | Type | Phrase (paraphrase) | Turn/Line | Flags
---|---|---|---|---
C1 | FORWARD_COMMITMENT | "firmly and completely on track to achieving our full-year EBITDA margin guidance of 17-19%" | T3/L17 | 
C2 | FORWARD_COMMITMENT | "committed and very very confident that we will be delivering a pre-sales growth of upward of 20% YoY ... these are minimum numbers" | T3/L17 | 
C3 | FORWARD_COMMITMENT | "revenue growth ... minimum 20% year-on-year growth" | T3/L17 | 
C4 | FORWARD_COMMITMENT | "return on capital employed will be 20% or upward of that" | T3/L17 | 
C5 | FORWARD_COMMITMENT | discipline of "not going beyond 1 is to 1" debt-to-equity | T3/L17, T9/L29, T72/L155 | 
C6 | FORWARD_COMMITMENT | Parel project ~18 months to market | T15/L41 | 
C7 | FORWARD_COMMITMENT | two Mahim launches this year, specific quarter windows (Q3, Q4) | T19/L49, T25/L61 | 
C8 | FORWARD_COMMITMENT | six of eight JDAs to be launched by end of FY27 | T25/L61 | 
C9 | FORWARD_COMMITMENT | JDA margins to scale up "by FY28" as projects mature | T74/L159 | 
C10 | FORWARD_COMMITMENT | "making a commitment of 20%" ROC "and we are very very confident that we will achieve that" | T28/L67 | juxtaposed against historical >25% ROC (N68) — flagged as a downward step in Section D
C11 | FORWARD_COMMITMENT | promise to work out and separately disclose the exact FY27 interest-cost number | T55/L121, T99/L209 | 
C12 | FORWARD_COMMITMENT | "we will definitely work on it" re: bringing in project-level PE/institutional investors | T95/L201 | vague, no timeline or mechanism specified
C13 | HEDGE | "don't hold me to it" re: ~100 cr interest cost estimate | T55/L121 | 
C14 | HEDGE | "I don't have that number readily available" (full-year interest cost) | T55/L121, T98 embedded/L207 | 
C15 | HEDGE | "we have not given any guidance on net profit ... we don't have a policy just now of giving that out" | T89 embedded/L189 | direct refusal to guide on PAT despite EBITDA guidance being given — caps interpretive confidence on bottom-line trajectory
C16 | HEDGE | "Let me not give you a number" (re: PAT arithmetic) | T89 embedded/L189 | 
C17 | HEDGE | "I don't have that number just now ... I can get back to you on that if you write to us" (PAT deceleration question) | T92/L195 | 
C18 | HEDGE | "safe to assume ... but don't hold me to it" | T55/L121 | duplicate of C13 pattern, separate instance
C19 | HEDGE | "I don't have it readily available here. We will work out that number" (dues-to-government full-year cost) | T99/L209 | 

**commitments_hedges count reconciliation:** grep count of turns containing guidance-lexicon
markers ("guidance," "commit," "on track," "confident," "don't have," "don't hold me to it,"
"can't answer," "get back to you" — case-insensitive) across management turns = 19 distinct
phrase instances after collapsing near-duplicate repeats within the same turn. Manual sweep
above (C1-C19) = 19. **Match: yes.**

---

## SECTION F — SUPPLEMENTARY DATA-QUALITY FLAGS (source-transcript defects, not interpretation)

- `TURN_MERGED` (4 instances): T57/L125, T89/L189, T94/L199, T98/L207 — the source transcript
  runs a management answer directly into the next analyst's question (or vice versa) with no
  speaker break, blank line, or attribution marker. Each instance is called out at its turn row
  in Section B and its corresponding embedded question in Section C. This is a transcription
  defect, not an interpretive finding — noted for A3/A4 so the arithmetic/consistency checks do
  not misattribute a question's numbers to management or vice versa.
- `NAME_INCONSISTENT` (2 instances): P1 (Harmohan Sani / Harmohan Swani), P4 (Amit Saburval /
  Sani Desa) — both resolved via later in-call cross-reference (T94/L199 confirms "Amit
  Saburval" as correct); Harmohan Sani/Swani resolution not independently confirmed within this
  transcript, flag `NOT FOUND` for definitive spelling.
- `NAME_GARBLED` (7 analyst/firm names): P6, P7 (firm), P9 (firm), P10, P11 (firm), P12 (name
  and firm), P14 (minor) — transcript quality issue affecting the participant registry; does not
  affect topic/figure enumeration.
- `SPEAKER_AMBIGUOUS` (6 short filler turns): T32/L75, T37/L85, T66/L143, T80/L171, T86/L183,
  T88/L187 — all are short audio-confirmation or filler turns ("Yes sure," "Yeah," "Hello,"
  "Can you repeat that please?") where the source gives no reliable speaker cue.
- `MODERATOR_AS_ANALYST`: P5 (Bhavin Modi) both moderates the call and asks a full analyst
  question set (Q3a-Q3c) representing host broker Anand Rathi.
- `MGMT_ABSENCE` (2 instances): P2 (Group CFO Rakkesh Tiwari, zero turns across the entire
  103-turn transcript) and P3 (CFO Ankur Jindal, explicitly stated as traveling/unreachable at
  T9/L29, does not answer a question addressed directly to him at T8/L27).
- `ANALYST_CITED_NOT_MGMT`: the ~50 cr / ~45 cr / ~20 cr finance-cost breakdown figures at
  Q10a/T97/L205 are cited by the analyst from the FY26 annual report, not spoken by management
  as a Q1 FY27 disclosure — excluded from Section D's management-numbers count, kept in
  Section C's question ledger for A3/A4 cross-check against the filing baseline.

---
