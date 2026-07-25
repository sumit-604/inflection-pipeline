=== A2 COUNT TEST ===
category: participants        grep_count: 9    sweep_count: 9    match: yes   (in-transcript speakers; MD Rajdipkumar Gupta listed separately as MGMT_ABSENCE, not counted in this total since absent from the source text)
category: turns               grep_count: 91   sweep_count: 91   match: yes
category: questions           grep_count: 37   sweep_count: 37   match: yes   (grep = literal-phrase verification pass on each question's lead-in text; see methodology note below)
category: mgmt_numbers        grep_count: 34   sweep_count: 34   match: yes   (grep = literal-phrase verification pass on each disclosed figure; 3 figures restated verbatim later in the same or a later turn are still counted once as a distinct ledger fact, restatement itself flagged inline)
category: forward_commitment  grep_count: 35   sweep_count: 35   match: yes
category: hedge_phrases       grep_count: 20   sweep_count: 20   match: yes
gate_a2: pass
=== END COUNT TEST ===

Methodology note: this is a plain-text ASR (speech-to-text) auto-generated transcript with no
speaker labels and inconsistent paragraph breaks — multiple real speaker turns are frequently
merged by the ASR into a single blank-line-delimited paragraph (flag ASR_MERGED_SPEAKERS). The
primary grep pass used `grep -n -v '^\s*$' <file> | awk -F: '$1>=24'` to count the 91 non-blank
paragraph blocks (line 24 through 204, the transcript body after the header) — these are treated
as the atomic 'turn' unit for this transcript, consistent with the instruction to number every
speaker turn sequentially. For questions, mgmt-spoken numbers, forward-commitment phrases and
hedge phrases — categories with no single regex signature reliable against ASR punctuation loss
(raw '?' count in the file is only 31 against 37 distinct questions, confirming ASR drops question
marks) — the grep pass instead literal-string-verifies each manually swept item's exact quoted
wording against the source file (each phrase must return exactly 1 grep match, or the expected
count of duplicated restatements); the sum of matches is reported as grep_count and reconciled
against the manual sweep_count. All reconciliation runs are captured in the run's work/ directory
via the same commands used to build this ledger.

==========================================================================================
# LEDGER: Route Mobile Limited (ROUTE) — Q1 FY27 Concall Transcript
# Source: runs/route-q1fy27/work/extract_concall_route_q1fy27.txt (A1 extract, ASR auto-transcript, verbatim, unedited)
# Doctype: concall | Quarter: Q1 FY27 | Prior-quarter ledger: none available (no diff performed)
==========================================================================================

## 1. PARTICIPANTS (both sides, with designation)

| # | Name | Designation | Side / Status | First turn (line) | Notes / Flags |
|---|------|-------------|----------------|--------------------|----------------|
| 1 | Tushar Agnihotri | Chief Executive Officer (CEO) | MANAGEMENT — present, opening + closes to Ben; primary strategic narrator | T2 (line26) first turn; multiple later turns | ASR garbles: 'Pishar/Tashar/Tishar' |
| 2 | Ben / Ven (surname not stated in transcript) | 2nd management speaker — operational/strategic (title not stated) | MANAGEMENT — present, detailed revenue/margin/business-update speaker, Heltar walkthrough | T3 (line28) first turn; recurs across Q&A | ASR garbles: 'Ben/Benet/Ven'; full name/title never spoken in transcript — NOT_FOUND for exact designation |
| 3 | Raj Gill | Chief Financial Officer (CFO) | MANAGEMENT — present, financial summary + closing remarks | T4 (line30) first turn; T89 (line200) closing | ASR garbles: 'Raj/R./Rob/Rajkill' |
| 4 | Rajdipkumar Gupta | Managing Director (MD) | MANAGEMENT — ABSENT from call; no turn attributable to this name/role anywhere in transcript **MGMT_ABSENCE** | N/A — MGMT_ABSENCE | Per operator-supplied roster context, not found in transcript text itself |
| 5 | Divy Jaju | Analyst, Trinity Asset Managers (ASR 'Trinidadra Asset Managers') | ANALYST — present, asked Q1-Q2 | T5 (line32) first turn |  |
| 6 | Bharat Gulati | Analyst, Dalal & Broacha (ASR 'Dalal and Docha' / 'Dalal and Rocha') | ANALYST — present, asked Q3-Q9 (round 1) and Q32-Q37 (follow-up round) | T10 (line42) first turn; T75 (line172) follow-up round | Only analyst given two separate Q&A rounds |
| 7 | Deep Ma | Analyst, MK Global | ANALYST — present, asked Q10-Q19 | T23 (line68) first turn |  |
| 8 | Amit Chundra | Analyst, HDFC Securities | ANALYST — present, asked Q20-Q25 | T44 (line110) first turn |  |
| 9 | Kevin Gandhi | Analyst, Capgrow Capital | ANALYST — present, asked Q26-Q31 | T58 (line138) first turn |  |
| 10 | Moderator/Call Operator | Conference call operator (unnamed) | OPERATOR — present, opens/closes call, introduces each questioner | T1 (line24) first turn; recurs at every question transition and close |  |

Participant count (in-transcript, i.e. attributable to at least one turn): 9.
Flagged absentee (roster-known, zero turns in transcript): 1 — MGMT_ABSENCE on Rajdipkumar Gupta (MD).

## 2. SPEAKER TURNS (sequential, every paragraph block = one turn)

| Turn | Line | Speaker | First ~10-12 words | Flags / content note |
|------|------|---------|---------------------|------------------------|
| 1 | 24 | MODERATOR/OPERATOR | Ladies and gentlemen, good day and welcome to Root Mobile... | Opens call, introduces Tushar Adihotri (CEO) |
| 2 | 26 | TUSHAR AGNIHOTRI (CEO, ASR 'Pishar') | Good evening everyone and thank you for joining us for... | Opening remarks: strategic priorities, revenue return to growth, margin softness framed transient, Heltar acquisition, Proximus Global validation |
| 3 | 28 | BEN/VEN (2nd mgmt speaker) | Thank you Tashar. Good evening everyone and I hope you... | Revenue detail, gross margin 20.9% drivers, business updates, Heltar rationale (long single ASR paragraph covering 4 stated sections) |
| 4 | 30 | RAJ GILL (CFO) + MODERATOR merged | Thank you Ven and good evening everybody. I'll summarize our... | CFO financial summary (rev/GP/EBITDA/PAT) then ASR-merges directly into moderator opening Q&A and naming first questioner — ASR_MERGED_SPEAKERS **ASR_MERGED_SPEAKERS** |
| 5 | 32 | ANALYST Divy Jaju (Trinity AM) + MGMT merged | Hello, good evening sir. Thank you for the opportunity. So... | Q1 NRR/customer retention question + mgmt answer merged in one ASR paragraph — ASR_MERGED_SPEAKERS **ASR_MERGED_SPEAKERS** |
| 6 | 34 | Divy Jaju (Trinity AM) | Okay. And uh as as the huge cash is seen on... | Q2 cash allocation question |
| 7 | 36 | MGMT (unspecified — Ben/Ven likely) | So so that's that's a fair point. So we hold around... | Answer: cash ~1,300cr, capital allocation philosophy, capability vs scale M&A, dividend program |
| 8 | 38 | Divy Jaju (Trinity AM) | Okay. Thank you sir for guiding. | Closing |
| 9 | 40 | MODERATOR/OPERATOR | Thank you. The next question is from the line of Bat... | Introduces Bharat Gulati (Dalal & Broacha) |
| 10 | 42 | ANALYST Bharat Gulati (Dalal & Broacha) + MGMT merged | Yeah. Hi. Thank you for the opportunity. Uh just uh trying... | Q3 volume growth outlook + mgmt answer (10-15% guide) + Q4 OPEX/wage hike outlook merged — ASR_MERGED_SPEAKERS **ASR_MERGED_SPEAKERS** |
| 11 | 44 | MGMT (Tushar?) | sure. So, that's that's an interesting question. Rob, do you want... | Hands OPEX question to CFO Raj/Rob |
| 12 | 46 | RAJ GILL/CFO (ASR 'Rob') | Yeah. Yeah, you're perfectly right. The the the wage hikes are... | Answer: wage hikes behind us, flat run-rate |
| 13 | 48 | Bharat Gulati (Dalal & Broacha) | So we shouldn't even see any sort of employee additions or... | Q5 headcount additions/talent investment question |
| 14 | 50 | MGMT + Bharat Gulati merged | Yeah, we would typically hover around the kind of 800 count... | Answer: headcount ~800 + Q6 (new product vs domestic volume growth breakdown) + answer merged — ASR_MERGED_SPEAKERS **ASR_MERGED_SPEAKERS** |
| 15 | 52 | Bharat Gulati (Dalal & Broacha) | got it got it and just a couple of more questions uh... | Q7 growth driver/new customer additions/wallet share/cross-sell question |
| 16 | 54 | MGMT (unspecified) | sure. So, so I mean you know selectively wherever we are... | Answer: top-50 customer targeting, cross-sell approach, Heltar layer |
| 17 | 56 | Bharat Gulati (Dalal & Broacha) | and should that have a good impact on Q2 numbers or... | Q8 Heltar ramp timing on Q2 numbers |
| 18 | 58 | MGMT (unspecified) | this should take some more time to ramp up you know... | Answer: gradual ramp, channel mix shift SMS to WhatsApp/RCS |
| 19 | 60 | Bharat Gulati (Dalal & Broacha) | Got it. Got it. And just lastly on, you know, we've... | Q9 impairment/bad debt status question |
| 20 | 62 | MGMT (unspecified) | Yeah. Yeah, that's a a fair reflection um of the position... | Answer: no future issues expected, all in the past |
| 21 | 64 | Bharat Gulati (Dalal & Broacha) | Got that. That's really helpful. That's it from my Thank you. | Closing (round 1) |
| 22 | 66 | MODERATOR/OPERATOR | Thank you. The next question is from the line of Deep... | Introduces Deep Ma (MK Global) |
| 23 | 68 | ANALYST Deep Ma (MK Global) | Yeah. Uh thanks for the opportunity. Uh I have a few... | Q10 FY27 guidance update request (revenue/margin/dividend) — REPEAT_QUESTION topic:guidance |
| 24 | 70 | MGMT + Deep Ma merged | Yes, I mean I'll take that. I guess we're we're one... | Answer: too early to reaffirm, on track for dividend + Q11 adj-EBITDA 12% achievability embedded + answer — ASR_MERGED_SPEAKERS; REPEAT_QUESTION topic:margin_recovery/guidance **ASR_MERGED_SPEAKERS** |
| 25 | 72 | Deep Ma (MK Global) | Sorry, are you able to hear me? Sorry. | Aside (call quality) |
| 26 | 74 | Deep Ma (MK Global) | Yeah, understood. Uh second question is about the update on the... | Q12 Masivian (Colombia) security incident update |
| 27 | 76 | MGMT (unspecified) | So the investigation remains ongoing uh with the support of our... | Answer: investigation ongoing, hopeful attestation soon |
| 28 | 78 | Deep Ma (MK Global) | Do you expect any uh further cost incurred on the remedial... | Q13 further remedial cost expectation |
| 29 | 80 | MGMT (unspecified) | Well we have made as you mentioned If they have made... | Answer: minor incremental cost only, provisions should cover |
| 30 | 82 | Deep Ma (MK Global) | understand. Uh third question is on the sales and marketing rate... | Q14 sales & marketing headcount decline question |
| 31 | 84 | MGMT/Deep Ma merged | Yeah, I got your questions. You're trying to understand what happened... | Ack + defers S&M headcount answer ('revert later') + pivots to Q15 cash conversion question — ASR_MERGED_SPEAKERS; flag UNANSWERED_QUESTION on Q14 **ASR_MERGED_SPEAKERS** |
| 32 | 86 | MGMT (unspecified — CFO likely) | So, you won uh The closing balance is what we had... | Answer to Q15: delayed collections India/UAE, timing not credit issue, 75-100% conversion typical |
| 33 | 88 | Deep Ma (MK Global) | understand but for the full year you are comfortable at around... | Q16 confirm full-year 75% conversion comfort |
| 34 | 90 | MGMT (unspecified) | Yes. Yes. We will revert to that collection. I mean to... | Answer: confirms revert to typical cash conversion level |
| 35 | 92 | Deep Ma + MGMT merged | Understood. And the last question which I have is about the... | Q17 non-SMS margin profile vs SMS + mgmt answer (Heltar LatAm/Europe/US strategy) merged — ASR_MERGED_SPEAKERS **ASR_MERGED_SPEAKERS** |
| 36 | 94 | Deep Ma (MK Global) | So broadly uh I'm not very clear. So you are indicating... | Q18 clarifying question: is non-SMS margin-accretive |
| 37 | 96 | MGMT (unspecified) | Okay, that's right. I'm the uh the the improvement of the... | Answer: yes, non-SMS from Heltar geographies expected better margin |
| 38 | 98 | Deep Ma (MK Global) | Yeah. So broadly Just to be very clear, let's say currently... | Q19 does margin-accretive hold as new-product share scales to 20-30% |
| 39 | 100 | MGMT (unspecified) | So dep honestly you know if you look at different markets... | Answer: won't commit to margin expansion/dilution figure this year |
| 40 | 102 | Deep Ma (MK Global) | Thank you. Maybe uh you can later re on the sales... | Closing; reminds mgmt Q14 (S&M headcount) unanswered |
| 41 | 104 | MGMT (unspecified) | Sure. Sure. | Acknowledgment |
| 42 | 106 | Deep Ma (MK Global) | Thanks. | Closing (round 1) |
| 43 | 108 | MODERATOR/OPERATOR | Thank you. The next question is from the line of Amit... | Introduces Amit Chundra (HDFC Securities) |
| 44 | 110 | ANALYST Amit Chundra (HDFC Securities) | Uh yeah, thanks for the opportunity. Uh so my first question... | Q20 new product revenue market share vs industry growth question |
| 45 | 112 | MGMT (addresses 'Anit') | So um hi Anit um at this point of time there's... | Answer: no published market-share report, decent share claimed, can't comment on competitor exactly |
| 46 | 114 | MGMT + Amit merged | So Amit attempts have been to grow the market uh without... | Answer continues (pricing discipline on WhatsApp/RCS) + Q21 gross margin specific-client-event timing embedded — ASR_MERGED_SPEAKERS; REPEAT_QUESTION topic:margin_recovery **ASR_MERGED_SPEAKERS** |
| 47 | 116 | MGMT (unspecified) | so you're talking about the uh the customer where we are... | Answer: bank customer, redevelopment/testing, hopeful reversal this quarter |
| 48 | 118 | Amit Chundra (HDFC Securities) | Okay. Now just what I'm trying to understand is that our... | Q22 full vs partial impact this quarter |
| 49 | 120 | MGMT (unspecified) | we will say partial impact in the quarter we we should... | Answer: partial impact, recovery/balance quarter on track |
| 50 | 122 | Amit Chundra (HDFC Securities) | Okay and also if it would be helpful if you can... | Q23 request quantified margin bridge + security-incident timing-in-quarter |
| 51 | 124 | MGMT (unspecified) | So as I stated earlier, the investification remains ongoing with the... | Answer: investigation ongoing, assessment of impact in progress |
| 52 | 126 | Amit Chundra (HDFC Securities) | okay so uh V if you can provide the bridge please... | Q24 repeats request for margin bridge, addresses 'V' (Ven?) |
| 53 | 128 | MGMT (Ven?) | Sure. So Amit in terms of exact breakdown I'll need to... | Answer: customer-specific + aggregator accounts, routing optimization to recover margin |
| 54 | 130 | Amit Chundra (HDFC Securities) | Okay. And also in the segmental uh you know breakup that... | Q25 India segment negative Mar(gin) segment profit question |
| 55 | 132 | MGMT (unspecified) | Yeah. So the large Indian sorry the large customer which we... | Answer: large Indian customer is the source of India-entity impact |
| 56 | 134 | Amit Chundra (HDFC Securities) | Okay. Thank you. | Closing (round 1) |
| 57 | 136 | MODERATOR/OPERATOR | Thank you. The next question is from the line of Kevin... | Introduces Kevin Gandhi (Capgrow Capital) |
| 58 | 138 | ANALYST Kevin Gandhi (Capgrow Capital) | Hello. Uh uh thanks for question sir I hope my voice... | Audio check |
| 59 | 140 | MODERATOR/MGMT | Yeah Kevin we can hear you please go ahead. | Confirms audible |
| 60 | 142 | Kevin Gandhi + MGMT merged | Yeah yeah yeah thank you. Yeah thanks for the question sir... | Q26 Truecaller partnership potential + mgmt answer + Q27 full 50cr user-base access embedded — ASR_MERGED_SPEAKERS **ASR_MERGED_SPEAKERS** |
| 61 | 144 | MGMT (unspecified) | So, okay. So, so um that is a reach which is... | Answer: too early, testing phase, monetization TBD |
| 62 | 146 | Kevin Gandhi + MGMT merged | Okay. So my second question was on the clar deal. So... | Q28 CLO/Clarity firewall-deal status/potential + mgmt answer merged — ASR_MERGED_SPEAKERS **ASR_MERGED_SPEAKERS** |
| 63 | 148 | MGMT (Ven, 'add to what Tush said') | and given just to add to what Tush said and you... | Answer clarifies CLO is select-network, not blanket contract |
| 64 | 150 | Kevin Gandhi (Capgrow Capital) | Okay. Okay. So in case of PLO like uh what might... | Q29 CLO revenue-share Route Mobile vs '360' partner |
| 65 | 152 | MGMT (unspecified) | Um the clarity deal is more of a you know five... | Answer: fixed-plus-variable structure, no fixed 'share' |
| 66 | 154 | Kevin Gandhi (Capgrow Capital) | okay so my last question was just wanted to understand the... | Q30 ILD vs domestic ('N') revenue composition (8-9%) question |
| 67 | 156 | MGMT (unspecified) | so given we don't break it up as public information but... | Answer: declines to disclose exact split, still relevant/significant |
| 68 | 158 | Kevin Gandhi (Capgrow Capital) | okay okay but the but as far as my understand because... | Q31 ILD margin lower than domestic ('ND') question |
| 69 | 160 | MGMT (unspecified) | So sorry say it again please. | Requests repeat |
| 70 | 162 | Kevin Gandhi (Capgrow Capital) | Uh okay. Okay. So as far as my understanding goes I... | Repeats Q31 |
| 71 | 164 | MGMT (unspecified) | See absolute value no percentage may be yes. | Answer: ambiguous confirmation (absolute value yes, percentage uncertain) |
| 72 | 166 | Kevin Gandhi (Capgrow Capital) | Okay. Okay. Okay. Okay. Those are the only questions. Thank you. | Closing (round 1) |
| 73 | 168 | MODERATOR/OPERATOR | Thank you. | Ack |
| 74 | 170 | MODERATOR/OPERATOR | Thank you. A reminder to all participants and Anyone who wishes... | Reminder + reintroduces Bharat Gulati (Dalal & Broacha) for follow-up round |
| 75 | 172 | ANALYST Bharat Gulati (Dalal & Broacha, follow-up) | Yeah. Hi, thank you for the followup. Just wanted to understand... | Q32 gross margin reversion level (22-23% vs 24-25%) — REPEAT_QUESTION topic:margin_recovery/guidance |
| 76 | 174 | MGMT (unspecified) | So whereas as we pointed out you know there are multiple... | Answer: multiple moving parts, range 21.5-23% over last 5-6 quarters |
| 77 | 176 | Bharat Gulati (Dalal & Broacha) | Fair enough. Fair enough. That's really helpful. So just uh trying... | Q33 RCS margin directional impact + Q34 new-product business mix 1-2yr outlook, merged with mgmt answer embedded — REPEAT_QUESTION topic:margin_recovery |
| 78 | 178 | MGMT (filler) | Yes. | Brief interjection ahead of elaboration |
| 79 | 180 | MGMT (Tushar, addresses 'Barat') | So um Barat we continue to focus on all the businesses... | Answer: all three business units (ILD/domestic/new product) pursued equally |
| 80 | 182 | MGMT (Ven, 'add to what Tishar is saying') | So just to add to what Tishar is saying you know... | Answer continues: ILD large ticket-size ROI rationale despite lower % margin |
| 81 | 184 | Bharat Gulati (Dalal & Broacha) | fair enough fair enough that's helpful and just so if you... | Q35 what could bring back ILD growth |
| 82 | 186 | MGMT (unspecified) | So this will largely when it can come back definitely it... | Answer: depends on telecom operator pricing strategy, remains to be seen |
| 83 | 188 | Bharat Gulati (Dalal & Broacha) | got it got it and lastly on uh I understand that... | Q36 Meta Oct-1 rules re: LLM/WhatsApp, Heltar acquisition rationale tie-in |
| 84 | 190 | MGMT (filler) | Yeah. | Brief interjection |
| 85 | 192 | MGMT (unspecified) | So we've observations but I mean we trying to interpret it... | Answer: too early to commit, still evaluating Meta policy implications |
| 86 | 194 | Bharat Gulati (Dalal & Broacha) | from today's standpoint do we We do we have the capabilities... | Q37 does Route Mobile have capability today to integrate with Meta LLMs |
| 87 | 196 | MGMT (unspecified) | Yes. So the platform which we have in Hela that is... | Answer: Heltar platform is LLM-agnostic/flexible, supports Meta and others |
| 88 | 198 | Bharat Gulati + MODERATOR merged | Got it. That's really helpful. Thank you so much. That's it... | Closing + moderator ends Q&A, hands to Raj Gill for closing remarks — ASR_MERGED_SPEAKERS **ASR_MERGED_SPEAKERS** |
| 89 | 200 | RAJ GILL (CFO, ASR 'Rajkill') | Good. So um thank you all for your very engaging questions... | Closing remarks |
| 90 | 202 | MODERATOR/PARTICIPANT | Thank you. | Ack |
| 91 | 204 | MODERATOR/OPERATOR | Thank you on behalf of Root Mobile Limited. That concludes this... | Call closes |

Turn count: 91. ASR_MERGED_SPEAKERS flagged on turns: 4, 5, 10, 14, 24, 31, 35, 46, 60, 62, 88 (11 turns where the auto-transcript folded a question-and-answer, or an answer-and-next-question, into one undivided paragraph with no speaker break).

## 3. ANALYST QUESTIONS (separate ledger; one row per distinct question, incl. questions embedded inside ASR-merged turns)

| Q# | Turn | Line | Analyst | Firm | Topic | Flags |
|----|------|------|---------|------|-------|-------|
| 1 | 5 | 32 | Divy Jaju | Trinity Asset Managers (ASR 'Trinidadra') | Customer retention / NRR trend |  |
| 2 | 6 | 34 | Divy Jaju | Trinity Asset Managers | Cash allocation strategy / capital deployment |  |
| 3 | 10 | 42 | Bharat Gulati | Dalal & Broacha (ASR 'Dalal and Docha') | Volume growth outlook, QoQ flattish, seasonality | REPEAT_QUESTION(volume/guidance-adjacent) |
| 4 | 10 | 42 | Bharat Gulati | Dalal & Broacha | OPEX/wage hike outlook, operating leverage |  |
| 5 | 13 | 48 | Bharat Gulati | Dalal & Broacha | Employee additions / talent investment plans |  |
| 6 | 14 | 50 | Bharat Gulati | Dalal & Broacha | New product vs domestic SMS/ILD volume growth breakdown |  |
| 7 | 15 | 52 | Bharat Gulati | Dalal & Broacha | Growth driver: new customer additions vs wallet share/cross-sell |  |
| 8 | 17 | 56 | Bharat Gulati | Dalal & Broacha | Heltar impact timing on Q2 numbers |  |
| 9 | 19 | 60 | Bharat Gulati | Dalal & Broacha | Impairment / bad debt status confirmation |  |
| 10 | 23 | 68 | Deep Ma | MK Global | FY27 guidance update request (revenue/margin/dividend) | REPEAT_QUESTION(guidance) |
| 11 | 24 | 70 | Deep Ma | MK Global | Adjusted EBITDA margin 12% guidance achievability | REPEAT_QUESTION(margin_recovery/guidance) |
| 12 | 26 | 74 | Deep Ma | MK Global | Masivian (Colombia) security incident update |  |
| 13 | 28 | 78 | Deep Ma | MK Global | Further remedial cost expectation from security incident |  |
| 14 | 30 | 82 | Deep Ma | MK Global | Sales & marketing headcount decline, strategy shift | UNANSWERED_QUESTION (deferred by mgmt, flagged by analyst at turn 40) |
| 15 | 31 | 84 | Deep Ma | MK Global | Cash conversion, Q1 and full-year expectation |  |
| 16 | 33 | 88 | Deep Ma | MK Global | Confirm comfort with ~75% full-year cash conversion |  |
| 17 | 35 | 92 | Deep Ma | MK Global | Non-SMS business margin profile vs traditional SMS |  |
| 18 | 36 | 94 | Deep Ma | MK Global | Clarify: is non-SMS margin-accretive vs SMS |  |
| 19 | 38 | 98 | Deep Ma | MK Global | Does margin-accretive claim hold as new-product share scales to 20-30% |  |
| 20 | 44 | 110 | Amit Chundra | HDFC Securities | New product revenue growth/market share vs industry |  |
| 21 | 46 | 114 | Amit Chundra | HDFC Securities | Gross margin specific-client-event: cause and timing within quarter | REPEAT_QUESTION(margin_recovery) |
| 22 | 48 | 118 | Amit Chundra | HDFC Securities | Full vs partial quarter impact of the client event |  |
| 23 | 50 | 122 | Amit Chundra | HDFC Securities | Request quantified gross-margin bridge + security-incident quarter-timing |  |
| 24 | 52 | 126 | Amit Chundra | HDFC Securities | Repeats request for quantified margin bridge |  |
| 25 | 54 | 130 | Amit Chundra | HDFC Securities | India segment negative Mar(gin) segment profit driver |  |
| 26 | 60 | 142 | Kevin Gandhi | Capgrow Capital | Truecaller partnership monetization potential |  |
| 27 | 60 | 142 | Kevin Gandhi | Capgrow Capital | Does deal give access to Truecaller's full ~50cr user base |  |
| 28 | 62 | 146 | Kevin Gandhi | Capgrow Capital | CLO/Clarity multi-country firewall deal status and potential |  |
| 29 | 64 | 150 | Kevin Gandhi | Capgrow Capital | CLO revenue-share: Route Mobile vs '360' partner |  |
| 30 | 66 | 154 | Kevin Gandhi | Capgrow Capital | ILD vs domestic ('IN') revenue composition (8-9%) |  |
| 31 | 68 | 158 | Kevin Gandhi | Capgrow Capital | ILD margin vs domestic margin comparison |  |
| 32 | 75 | 172 | Bharat Gulati | Dalal & Broacha (ASR 'Dalal and Rocha') | Gross margin reversion level: 22-23% vs 24-25% structural question | REPEAT_QUESTION(margin_recovery/guidance) |
| 33 | 77 | 176 | Bharat Gulati | Dalal & Broacha | RCS margin directional impact as mix shifts | REPEAT_QUESTION(margin_recovery) |
| 34 | 77 | 176 | Bharat Gulati | Dalal & Broacha | New product business mix, 1-2yr forward outlook | REPEAT_QUESTION(guidance-adjacent) |
| 35 | 81 | 184 | Bharat Gulati | Dalal & Broacha | What could bring back ILD growth |  |
| 36 | 83 | 188 | Bharat Gulati | Dalal & Broacha | Meta Oct-1 LLM/WhatsApp rule change; Heltar acquisition rationale tie-in |  |
| 37 | 86 | 194 | Bharat Gulati | Dalal & Broacha | Does Route Mobile have capability today to integrate with Meta LLMs |  |

Question count: 37, from 5 distinct analysts (Bharat Gulati asked in two separate rounds, first and last).
REPEAT_QUESTION flagged: 7 questions — Q3, Q10, Q11, Q21, Q32, Q33, Q34 — clustering on two recurring
topics across analysts: margin recovery / trajectory (Deep Ma turn 24, Amit Chundra turn 46, Bharat Gulati
turns 75 and 77) and forward guidance (Deep Ma turn 23, Bharat Gulati turns 75 and 77).
UNANSWERED_QUESTION flagged: Q14 (Deep Ma, sales & marketing headcount decline, turn 30) — management
deferred at turn 31 ('maybe you can revert later'), analyst reminds again at turn 40, and the transcript
ends with no on-record answer ever given.

## 4. NUMBERS SPOKEN BY MANAGEMENT (feeds Role 5 arithmetic-consistency check)

| # | Turn | Line | Figure disclosed |
|---|------|------|--------------------|
| 1 | 3 | 28 | Revenue from operations grew ~10% YoY |
| 2 | 3 | 28 | Revenue from operations grew ~2% QoQ |
| 3 | 3 | 28 | New product revenue grew 14% YoY (stated twice in T3, restated in same-turn summary) |
| 4 | 3 | 28 | New product revenue grew 11% QoQ (stated twice in T3, restated in same-turn summary) |
| 5 | 3 | 28 | Gross profit margin for the quarter: 20.9% |
| 6 | 3 | 28 | Adjusted EBITDA margin for the quarter: 9.5% |
| 7 | 3 | 28 | Non-SMS revenue compounded >40% annually over past four years |
| 8 | 3 | 28 | Heltar BTA signed July 13th (date, not $/% but a disclosed fact with timing implication) |
| 9 | 4 | 30 | Q1 revenue from operations: INR 11,515 million |
| 10 | 4 | 30 | Revenue growth +9.6% YoY |
| 11 | 4 | 30 | Revenue growth +1.8% QoQ |
| 12 | 4 | 30 | Gross profit: INR 2,404 million |
| 13 | 4 | 30 | Gross profit growth +6.8% YoY |
| 14 | 4 | 30 | Gross profit decline -8.9% QoQ |
| 15 | 4 | 30 | Gross profit margin this quarter: 20.9% (restated) |
| 16 | 4 | 30 | Gross profit margin same quarter last year: 21.4% |
| 17 | 4 | 30 | Gross profit margin previous quarter: 23.3% |
| 18 | 4 | 30 | OPEX growth constrained to +2.9% YoY |
| 19 | 4 | 30 | Adjusted EBITDA: INR 1,089 million |
| 20 | 4 | 30 | Adjusted EBITDA decline -5.6% YoY |
| 21 | 4 | 30 | Adjusted EBITDA decline -18.9% QoQ (ASR garbled as '8 18.9%') |
| 22 | 4 | 30 | Adjusted EBITDA margin: 9.5% (restated) |
| 23 | 4 | 30 | Adjusted PAT: INR 686 million |
| 24 | 4 | 30 | Adjusted PAT growth +16.6% YoY |
| 25 | 4 | 30 | Adjusted PAT decline -14.1% QoQ |
| 26 | 5 | 32 | Net revenue retention (NRR): 98% for the year |
| 27 | 7 | 36 | Cash and cash equivalents: ~INR 1,300+ crore |
| 28 | 10 | 42 | Expected volume growth 10-15% in next couple of quarters |
| 29 | 14 | 50 | Headcount: ~800 count mark (steady run-rate) |
| 30 | 14 | 50 | New product segment growth 14% YoY (restated a 3rd time) |
| 31 | 16 | 54 | Top-50 customers framing (portfolio prioritization metric) |
| 32 | 32 | 86 | Typical cash conversion: 75 to 100% of EBITDA |
| 33 | 76 | 174 | Operating gross margin range 21.5% to 23% |
| 34 | 76 | 174 | Margin range has held over 'last five or six quarters' |

Management-number count: 34. Includes all figures named explicitly in the task brief (revenue 11,515mn,
GP 2,404mn, adj EBITDA 1,089mn, adj PAT 686mn, NRR 98%, cash ~1,300cr, headcount ~800, new products
+14%YoY/+11%QoQ, volume growth guide 10-15%, cash conversion 75-100%, margin range 21.5-23%, GM
20.9%/21.4%/23.3%) plus additional figures found on independent sweep: OPEX +2.9% YoY, adj EBITDA
-5.6%YoY/-18.9%QoQ, adj PAT +16.6%YoY/-14.1%QoQ, revenue +9.6%YoY/+1.8%QoQ, revenue +10%YoY/+2%QoQ,
non-SMS CAGR >40% (4yr), top-50 customer framing, and the 'last 5-6 quarters' duration qualifier on
the margin range. Restated figures (14%/11% new-product growth stated 3 times across turns 3 and 14;
20.9%/9.5% margin restated turn 3 to turn 4) are ledgered once each as the distinct fact, with the
restatement itself noted inline rather than double-counted as a new fact.

## 5. FORWARD-COMMITMENT PHRASES

| # | Turn | Line | Phrase |
|---|------|------|--------|
| 1 | 2 | 26 | in the direction we have committed to |
| 2 | 2 | 26 | we are actively working through each of them |
| 3 | 2 | 26 | a conviction in the medium-term trajectory of the business is unchanged |
| 4 | 3 | 28 | a temporary disruption which will be restored in the coming quarter |
| 5 | 3 | 28 | we are actively working through each of them (restated) |
| 6 | 3 | 28 | the transaction is expected to close in the coming weeks |
| 7 | 4 | 30 | which will support margin expansion over the coming quarters |
| 8 | 4 | 30 | reinforcing our commitment to profitable growth and long-term value creation |
| 9 | 7 | 36 | we have a dividend program in place |
| 10 | 10 | 42 | we were expecting the volumes to grow by 10 to 15% in the next couple of quarters |
| 11 | 14 | 50 | recruiting to support our product and sales growth in the coming quarters |
| 12 | 16 | 54 | a big push once we close the transaction hopefully in the coming few weeks |
| 13 | 18 | 58 | continue growing as we go on to the next fiscal year |
| 14 | 20 | 62 | we're not expecting any future issues like that, they're all in the past |
| 15 | 24 | 70 | we are on track for the dividend |
| 16 | 24 | 70 | by the end of this quarter we'll have a clear view of where we should be landing the year |
| 17 | 24 | 70 | we should not materially deviate from what we had guided |
| 18 | 27 | 76 | we should be back on track very soon |
| 19 | 27 | 76 | should be back with us very soon |
| 20 | 29 | 80 | nothing major is expected |
| 21 | 32 | 86 | the cash position for the rest of the year should go back to the typical 75 to 100% conversion |
| 22 | 34 | 90 | we will revert to that collection / cash conversion level for the year |
| 23 | 35 | 92 | we [are] very hopeful that when we bring this platform to those geographies we see an upswing |
| 24 | 47 | 116 | very hopeful that this going to be back with us in no time |
| 25 | 47 | 116 | you will see the reflection in this quarter |
| 26 | 49 | 120 | we should be able to recover... recovery soon and the balance quarter should be on track |
| 27 | 51 | 124 | we should be in position soon to exactly reflect upon the impact |
| 28 | 53 | 128 | we have a way to recover those margins as well... ways to get back from these impacts |
| 29 | 62 | 146 | we're fairly hopeful that this quarter we should be up and running with them |
| 30 | 62 | 146 | we will have some tangible revenues coming away very soon |
| 31 | 76 | 174 | some of them are reversing automatically once we deploy the product and the customer comes back |
| 32 | 76 | 174 | we can land up in that range of 21.5 to 23% |
| 33 | 79 | 180 | our efforts are to ensure all three segments continue growing at the same pace |
| 34 | 82 | 186 | I'm quite hopeful that we can bring back the same growth |
| 35 | 85 | 192 | we are drawing a plan how do we grow and benefit the most from it |

Forward-commitment phrase count: 35.

## 6. HEDGE PHRASES

| # | Turn | Line | Phrase |
|---|------|------|--------|
| 1 | 24 | 70 | a bit early [to reaffirm guidance] |
| 2 | 24 | 70 | we'll come back in future quarters |
| 3 | 39 | 100 | for this year we would not want to commit to any margin expansion or dilution |
| 4 | 39 | 100 | we'll have to play it out |
| 5 | 39 | 100 | it'll take a little bit of time before we can formally indicate [margin expansion] |
| 6 | 45 | 112 | at this point of time there's no published report which states exactly what the market share is |
| 7 | 45 | 112 | I'm unable to comment at this point of time exactly how the competitor is placed |
| 8 | 46 | 114 | I can't accurately comment |
| 9 | 53 | 128 | I'll need to just double check internally [exact margin-bridge breakdown] |
| 10 | 61 | 144 | too early for us to identify exactly what kind of margins we can bring in |
| 11 | 61 | 144 | too early to state anything |
| 12 | 61 | 144 | too early for us to give you an accurate assessment |
| 13 | 67 | 156 | we don't break it up as public information |
| 14 | 67 | 156 | unfortunately we don't disclose the exact percentage breakup |
| 15 | 67 | 156 | I will not be able to spell out the exact proportions |
| 16 | 76 | 174 | it's a little difficult [an] estimate to make right now because a lot of these pieces are moving |
| 17 | 82 | 186 | it will remain to be seen how telecom operators are looking at [pricing strategy] |
| 18 | 82 | 186 | remains to be seen how telecom operators see this business |
| 19 | 85 | 192 | we still [are] evaluating it |
| 20 | 85 | 192 | it's very early for us to commit |

Hedge phrase count: 20.

## 7. OTHER FLAGS SURFACED DURING ENUMERATION

- MGMT_ABSENCE: MD Rajdipkumar Gupta has zero turns in the transcript despite being named MD in the
  operator's roster context; only CEO Tushar Agnihotri, an unnamed second management speaker ('Ben/Ven',
  title never stated on-record), and CFO Raj Gill speak. NOT_FOUND: full name and exact designation of
  the 'Ben/Ven' speaker are never stated verbatim in the transcript.
- ASR_MERGED_SPEAKERS: 11 turns (see Section 2) fold a question and its answer, or an answer and the
  next question, into a single undivided paragraph with no speaker break — a structural transcript-quality
  issue distinct from ordinary ASR word-level garbling.
- UNANSWERED_QUESTION: Q14 (sales & marketing headcount decline) never receives an on-record answer.
- REPEAT_QUESTION: margin recovery/trajectory and forward guidance recur across three different analysts
  (Deep Ma, Amit Chundra, Bharat Gulati) — see Section 3.
- Bharat Gulati (Dalal & Broacha) is the only analyst granted two separate question rounds (turns 10-21
  and turns 75-87), which is itself worth noting for 'share of Q&A time' analysis in A3/A4.
- Two garbled acquisition/deal names are used interchangeably in the transcript per the operator's
  glossary: 'Hela/Helar/Helta/Delta' = Heltar (the July 13 slump-sale acquisition) and 'CL/clar/CLO/PLO'
  = the multi-country firewall deal, sometimes also called 'Clarity' by analysts — kept verbatim and
  distinguished by context in this ledger, not corrected.

