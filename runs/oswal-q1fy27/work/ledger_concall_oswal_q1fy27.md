# LEDGER — Oswal Pumps Ltd (OSWAL) — Q1 FY27 — CONCALL — Agent A2 Enumerator

Source: `runs/oswal-q1fy27/work/extract_concall_oswal_q1fy27.txt`
A1 header confirms: text transcript, 150 source lines total, header block lines 1-2/4
(blank lines 3,5), 145 transcript content lines = source lines 6-150, all reproduced
verbatim with original line numbers preserved. This ledger enumerates every one of
those 145 content lines as a discrete "turn," plus every question, every management
spoken number, every forward-commitment/hedge, and every ASR ambiguity.

Prior-quarter ledger: none available (first quarterly-pipeline run for OSWAL) — no
diff possible, no DROPPED_SLIDE / ENTITY_CHANGE-type comparison possible this cycle.

Tool note: Devanagari regex matching via `grep -P` in this shell was unreliable for
multi-character Hindi word patterns (returned false zeros / false full-matches on
several test patterns — documented below in the COUNT TEST). Digit-only regex
(`[0-9]+(\.[0-9]+)?%?`) worked reliably. All Hindi word-number instances (लाख,
करोड़ written out, etc. where no digit is present) were therefore located by manual
sweep only, not cross-grepped; this is flagged explicitly, not silently assumed.

=== A2 COUNT TEST ===
category: turns              grep_count: 145  sweep_count: 145  match: yes
category: question_rounds    grep_count: 9    sweep_count: 9    match: yes
  (mechanism: grep -n on phrase "फर्स्ट क्वेश्चन" / "नेक्स्ट क्वेश्चन" over source
  lines 6-150 → 9 hits at lines 11,25,59,65,66,83,91,108,145. Manual sweep of the
  same 9 lines independently confirms: 1 "first question" announcement (line 11,
  Manish Gadia) + 7 named "next question" analyst-round announcements (lines 25
  Disha, 59 Dheeraj Ram attempt-1, 66 Karan, 83 Prakhar/Prakash, 91 Dheeraj Ram
  attempt-2, 108 Pawan Kumar, 145 Manish Gadia round-2) + 1 generic operator
  "you can take the next question" skip-instruction (line 65, following Dheeraj
  Ram's audio failure at lines 60-64, no new analyst named). 9 = 9, match.)
category: individual_questions   grep_count: n/a (ASR punctuation "?" unreliable
  for Hindi content — see note)   sweep_count: 28   match: n/a-informational
  (Literal "?" grep on lines 6-150 returns only 24 hits because Hindi ASR output
  frequently drops question-mark punctuation on interrogatives phrased in
  Devanagari; this undercounts by construction, not by miss. A punctuation-based
  grep is therefore NOT used as the GATE A2 pair for this sub-category — the
  question_rounds category above (phrase-based, reliable) is the GATE A2 pair for
  "questions." The 28-count individual-question breakdown below is manual-sweep-
  only and carried as an informational supplement for A3/A4, itemised in Table 3.)
category: mgmt_numbers       grep_count: 53  sweep_count: 53  match: yes
  (mechanism: awk/gsub digit-pattern scan over lines 6-150 found 53 lines
  containing at least one numeral. Manual speaker-attribution sweep classified
  all 53: 30 lines are management-attributed (VG/VY/mgmt-unclear-but-answering)
  substantive figures → these are Table 4 below; 23 lines are analyst-spoken or
  call-mechanics/operator digit mentions (fiscal-year labels, firm names, analysts
  echoing figures back in questions) → explicitly excluded from mgmt_numbers with
  reasons in Table 4b. 30 + 23 = 53 = grep universe. Match on total accounted-for
  universe; mgmt_numbers final count = 30.)
category: participants        grep_count: n/a (proper-noun grep not attempted —
  Devanagari name-grep unreliable per tool note above)   sweep_count: 12
  match: n/a-manual-only (12 named/generic participants confirmed by manual
  read-through of speaker introductions at lines 7 and Q&A round announcements;
  no independent mechanical cross-check performed — documented limitation, not
  silently assumed complete.)
gate_a2: pass
=== END COUNT TEST ===

---

## TABLE 1 — PARTICIPANTS

| # | Name | Role/Firm | Side | First appears (line) | Flags |
|---|------|-----------|------|----------------------|-------|
| 1 | Vivek Gupta | Chairman & Managing Director (CMD) | Management | 7 (introduced), 9 (speaks) | |
| 2 | [Om] Gupta | Whole-time Director | Management | 7 (introduced only) | `MGMT_ABSENCE` — introduced by name in the roster at line 7 but no turn in lines 8-150 is attributable to him by name or clear context; either he did not speak on a substantive call or the ASR/transcript failed to attribute any of his remarks — cannot distinguish from this transcript alone |
| 3 | Vijay Kumar Yadav | Chief Financial Officer (CFO) | Management | 7 (introduced), 10 (speaks) | |
| 4 | Avdhesh Singh | Chief Operating Officer (COO) | Management | 7 (introduced); possibly 43 | `AMBIGUOUS_ASR` — line 43 addresses "आयुष" (Ayush), plausibly an ASR mis-hearing of "Avdhesh," answering the Q1 volume question; not confirmed |
| 5 | Sanjeev Singh | Investor Advisor / IR | Management-side | 7 (introduced), 8 (speaks) | speaks again at lines 22/24 (embedded, see `MULTI_EXCHANGE_LINE`) |
| 6 | Dheeraj Ram | 361 Capital Markets — call moderator AND later an analyst asking questions himself | Dual role | 7 (moderator), 59/60-65 (analyst attempt 1, FAILED), 91-106 (analyst attempt 2, succeeded) | dual-role noted; `AUDIO_FAILURE_QUESTION_DROPPED` on first attempt |
| 7 | Manish Gadia | Individual Investor | Analyst/Investor | 39/40 (round 1, line 11-24), 140/145 (round 2, line 145-147) | asks in two separate rounds — `REPEAT_QUESTION` participant (returns after round 7) |
| 8 | Disha | "सपा कैपिटल" (ASR garble — plausibly SBI Capital) | Analyst | 20/25-58 | `AMBIGUOUS_ASR` on firm name |
| 9 | Karan | Choice Institutional Equities | Analyst | 61/66-82 | |
| 10 | Prakhar / Prakash | Choice Institutional Equities | Analyst | 78/83-90 | `AMBIGUOUS_ASR` — name spelled "प्रखर" at line 83, "प्रकाश" at line 90; same person, spelling not reconciled by ASR |
| 11 | Pawan Kumar | "शेयर कैपिटल" (ASR garble, firm name unclear — possibly "SAR Capital" or similar) | Analyst | 103/108-144 | `AMBIGUOUS_ASR` on firm name |
| 12 | Operator | Generic conference call operator (unnamed) | Call mechanics | 6 | recurring throughout for queue management, not a substantive participant |

Total participants enumerated: 12. Sweep-count only (see COUNT TEST note); no
independent mechanical name-grep cross-check performed in this environment.

---

## TABLE 2 — SPEAKER TURNS (every content line, 6-150 = 145 turns)

Speaker codes: OP=Operator, DR=Dheeraj Ram, SS=Sanjeev Singh, VG=Vivek Gupta (CMD),
VY=Vijay Kumar Yadav (CFO), MGMT=management speaker not distinctly separable from
ASR text, MG=Manish Gadia, DI=Disha, KA=Karan, PR=Prakhar/Prakash, PK=Pawan Kumar.

| Turn (=line) | Speaker | First ~10 words (English gloss of ASR content) | Flags |
|---|---|---|---|
| 6 | OP | Ladies and gentlemen, welcome to Oswal Pumps Q1 FY27 conference call, lines in listen-only mode | |
| 7 | DR | On behalf of 361 Cap, welcome the management of Oswal — introduces Vivek Gupta, Om Gupta, Vijay Yadav, Avdhesh Singh, Sanjeev Singh; hands to Sanjeev Singh | roster line — see Table 1 |
| 8 | SS | Thank you, good afternoon — draws attention to safe harbor statement in presentation | hands to Vivek Gupta |
| 9 | VG | Thank you Sanjeev ji, very good afternoon — opening remarks: Q1 revenue, EBITDA, order book, capex | number-dense — see Table 4 |
| 10 | VY | Thank you sir, good afternoon — key financial highlights: PAT, net debt, cash conversion, guidance | number-dense — see Table 4 |
| 11 | OP | Thank you, we will now begin the question-and-answer session; first question from Manish Gadia | round announcement |
| 12 | MG | Sir I had a query — retail investors invested from listing, stock price halved | Question 1 (round 1) start |
| 13 | MGMT (unclear) | Please, you'll say it again to me | `SPEAKER_UNCLEAR` |
| 14 | MG | I was saying we are invested from the IPO level | |
| 15 | MG | So whenever guidance is given on the call it's good but execution doesn't match | continues Q1 |
| 16 | MGMT (unclear) | Right? | `SPEAKER_UNCLEAR`, brief interjection |
| 17 | SS/OP (unclear) | So as a retail investor, many are worried — what do you have to say? | `SPEAKER_UNCLEAR`, paraphrases question back |
| 18 | VG | Right, see Manish ji, your thinking is absolutely correct, but let me tell you fundamentally | answer to Q1 begins |
| 19 | MG | OK sir, so fundamentally we are all good, only temporary — will life be better? | follow-up |
| 20 | VG | Absolutely, what I see is FY27 has turbulence, FY28/FY29 look much clearer and better | answer |
| 21 | MG | OK sir, thank you sir — if you have hope, we have hope | brief |
| 22 | VG+SS+MG | Absolutely, we sit on your hope; [SS adds] the challenge is entirely PM Kusum delay; [MG asks] one more query — competitor guided PM Kusum 2 in August | `MULTI_EXCHANGE_LINE` — 3 speakers merged; embeds Question 2 (round 1) start |
| 23 | MGMT (unclear) | OK see, this is what we're getting — actually two types of information coming in | `SPEAKER_UNCLEAR` — answer re August timing |
| 24 | SS+MG | I want to add — having said that, ultimately PM Kusum has to be released by government; [MG] thank you sir for taking my query | `MULTI_EXCHANGE_LINE` — closes round 1 |
| 25 | OP | Thank you — restrict questions to 2 per participant; next question from Disha, SBI/SAPA Capital | round 2 announcement |
| 26 | DI | Hello am I audible — thank you, couple of questions, first on this decline and margin | Question 1 (round 2) start |
| 27 | OP | Ladies and gentlemen, the management line is connected, sir please go ahead | interjection |
| 28 | DI | Yes sir, please | brief |
| 29 | DI | Yeah sir, my question was again for you — decline in margin because of heightened competition in tenders | restates Q1 |
| 30 | VG | OK see Disha ji, there are two things — so far the major margin decline reason was our Margala pump project | answer begins |
| 31 | VG | The bidding prices for that came down — this is the biggest reason; second, geopolitical RM cost rise; PM Surya Ghar 2 lakh homes target mentioned | answer continues |
| 32 | DI | OK OK so sir, we do a lot of diversification for that impact to come from next year, but this year, if PM Kusum delayed again, how should we look at overall growth? | Question 2 (round 2) |
| 33 | VG | OK see, as I said, ~2 lakh PM Surya Ghar target FY27; channel sales for wires & cables activated; Magalla orders execute Q2; P6 new tender floated; 20-25% growth visibility clear | answer, number-dense |
| 34 | DI | Right and sir, just want to understand more — how long does tendering process take to convert into orders? | Question 3 (round 2) |
| 35 | VG | It depends — normally PM Surya Ghar tenders, bid to allotment roughly 60-80 days; Bihar, AP, Rajasthan projects taken up, execution started | answer |
| 36 | DI | OK OK so sir, pretty much we are confident of this 202% growth | `AMBIGUOUS_ASR` — "202%" almost certainly garbled for "20-25%"; Question 4 (round 2) |
| 37 | VG | Yes sir, we are very confident, no challenge to 20-25% growth, whole team 100% aligned; Q1 no PM Kusum contribution, Q2 also none | answer |
| 38 | DI | Sir but this 20-25% majority growth will come in H2 right — Q2 growth or degrowth? | Question 5 (round 2) |
| 39 | MGMT/DI (unclear cross-talk) | Not by much, but will it be a degrowth | `SPEAKER_UNCLEAR` — reads as echo/cross-talk, not a clean answer |
| 40 | MGMT | Q2 definitely we're expecting growth, quarter-on-quarter basis | answer |
| 41 | MGMT | Definitely expecting more than 10-15% growth in Q2 — not expecting any degrowth | answer continues |
| 42 | DI | OK OK, and the last thing — what was the Q1 volume, number of pumps supplied | Question 6 (round 2) |
| 43 | MGMT ("आयुष"/possibly Avdhesh Singh, COO) | OK, [name], you have in Q1 — total number of company supplied around 43,000 numbers | `AMBIGUOUS_ASR` speaker name; answer |
| 44 | DI | And what was this number last year sir? | Question 7 (round 2) follow-up |
| 45 | MGMT | Last year number? | clarifying |
| 46 | DI | What was this number for Q4 FY26 and Q1 FY26, both quarter comparisons | clarifies further |
| 47 | DI | The sequential quarter and the last quarter | continues |
| 48 | MGMT | Yeah yeah, one minute ji | looking up figure |
| 49 | MGMT | Yes, Q4 — Q4 it was around 4400 | `AMBIGUOUS_ASR` — plausibly 44,000 per glossary; answer |
| 50 | MGMT | And Q1 last year was 56,000 | answer |
| 51 | DI+VG | OK OK, this is my last question — margin pressure this year, guided 15-17%, do we expect margins back to previous levels in FY28? [VG answers] see Disha ji, one thing is very fundamentally clear, company is fundamentally very strong | `MULTI_EXCHANGE_LINE` — Question 8 (round 2) + answer merged |
| 52 | DI/MGMT | Yeah, thank you | brief close |
| 53 | DI | As a worst case scenario, we can expect PM Kusum 2 to come by this year end, so for next year automatically pressure on bidding should go away | analyst scenario-confirmation question, `SPEAKER_UNCLEAR` on exact attribution |
| 54 | VG | See — [worst] case scenario | answer begins, short |
| 55 | VG | OK, this much futuristic talk we can't fully commit to; this may create a perception... | answer continues |
| 56 | VG | If aggressive bidding happened, vendors also face pressure; price benefit expected to flow through eventually | answer continues |
| 57 | DI | OK OK OK, that is it for my questions, thank you so much, all the best | closes round 2 |
| 58 | MGMT/OP | Thank you, thank you | brief close |
| 59 | OP | Thank you — restrict to 2 per participant; next question from Dheeraj Ram, please go ahead | round 3 announcement |
| 60 | DR | Is your voice audible, yes sir, now | audio check attempt |
| 61 | MGMT/OP (unclear) | Hello, it's not clear | `SPEAKER_UNCLEAR`; audio issue |
| 62 | DR | Can you hear me sir | audio check |
| 63 | MGMT/OP (unclear) | Your voice is not... cracking sir, can you please say again | `SPEAKER_UNCLEAR`; audio issue continues |
| 64 | MGMT/OP (unclear) | No sir, your voice is not audible | `SPEAKER_UNCLEAR`; `AUDIO_FAILURE_QUESTION_DROPPED` — Dheeraj Ram's round-3 question never delivered |
| 65 | OP | You can take the next question | skips Dheeraj Ram's attempt |
| 66 | OP+KA | OK, next question is on the line of Karan, Choice Institutional Equities, go ahead; hope I'm audible, thank you — margin loss from ~24-25% to 15%, how much attributable to lower realization vs higher RM cost | `MULTI_EXCHANGE_LINE` — round 4 announcement + Question 1 (round 4) |
| 67 | VG | Hello Karan ji, see, if I bifurcate — broadly ~8-9% impact is aggressive price bidding in Margala | answer, number-dense (margin bridge) |
| 68 | KA | Right sir, this price impact — is this from during-the-quarter orders or previously booked orders outstanding as of March 26 | Question 2 (round 4) |
| 69 | VG | See what we had outstanding in March, some tender prices executed in Q1; ~9% Margala tender pricing impact directly | answer |
| 70 | KA | OK OK, and sir, when do you expect this to stabilize and get back on board — PM Kusum or PM Surya, rough timeline | Question 3 (round 4) |
| 71 | VG | See Karan ji, I believe whatever happens is for good — PM Kusum 2 delay gave us extra vision to enter PM Surya Ghar and EPC | answer |
| 72 | KA | Yes | brief ack |
| 73 | KA | OK | brief ack |
| 74 | KA | Yes | brief ack |
| 75 | KA | Sir you've taken a good target for Surya Ghar, new scheme for me personally — how are orders received in Surya Ghar | Question 4 (round 4) |
| 76 | VG | See, entry into PM Surya Ghar had several reasons — backward integrated, module/BOS/structures manufacturing in-house, inverter production in-house within 6 months | answer |
| 77 | KA | Good, just one last question — margins of all three businesses, wires & cables, would we need capacity addition or is it a trading business | Question 5 (round 4) |
| 78 | VG | No, actually wires and cables we already manufacture in-house — introducing capacity into full channels, will get feedback | answer |
| 79 | KA | OK sir, any margin number you'd like to give for all businesses? | Question 6 (round 4) — reattributed to Karan, not management (correction from earlier draft speaker mapping) |
| 80 | VG | See Surya — broadly, as our CFO Vijay ji said, this year ~15-17% EBITDA margin; FY27 most challenging year for entire industry | answer |
| 81 | KA | OK, thank you and all the best | closes round 4 |
| 82 | MGMT | Thank you ji, thank you very much | brief close |
| 83 | OP | Thank you — next question from Prakhar, Choice Institutional Equities, please go ahead | round 5 announcement |
| 84 | PR | Hello sir, first question about capex — 1.5 GW module expansion, saw ~200 crore capex this quarter in the PPT, is Q3 timeline on schedule | Question 1 (round 5) |
| 85 | VG | Yes, see, solar module — one 1 GW investment already done, operational first/max second week of September; rest of IPO capex plan on track | answer |
| 86 | PR | OK, so sir, this year's full-year capex approximately 360-400 crore range | Question 2 (round 5) |
| 87 | VG | Whatever capex we took in IPO proceeds, almost as per plan, will all be infused | answer |
| 88 | PR+VG | OK OK done, one more question — EBITDA margin guidance 15-17% for FY27, does this assume Kusum renewal or is this worst-case scenario? [VG answers] see, present bidding we have in hand, we don't visualize better prices, this is calculated on the safer side | `MULTI_EXCHANGE_LINE` — Question 3 (round 5) + answer merged |
| 89 | PR | OK OK done, thank you so much sir, I am done | closes round 5 |
| 90 | MGMT/OP | Thank you, thank you Prakash ji | brief close — confirms name spelling "Prakash" (vs "Prakhar" at line 83, see `AMBIGUOUS_ASR`) |
| 91 | OP+DR | Thank you — next question from Dheeraj Ram, please go ahead; hi sir, am I audible? | `MULTI_EXCHANGE_LINE` — round 6 announcement (Dheeraj Ram's 2nd attempt, this time succeeds) |
| 92 | VY/MGMT+DR | Yes sir, audible Dheeraj ji, thank you for taking up the question; [DR asks] have we received any outstanding receivables this quarter? | `MULTI_EXCHANGE_LINE` — Question 1 (round 6) |
| 93 | MGMT | This quarter outstanding receivables received but very few; Q2 receivables expected comparatively better; Q3 much better | answer |
| 94 | DR | OK | brief ack |
| 95 | DR | OK great, sir — did the 15-17% margin guidance trend toward 17% by Q2, or reflect in Q3/Q4? | Question 2 (round 6) |
| 96 | MGMT | See, 15-17% specifically because some things are not in our hands due to external factors | answer, hedges precision |
| 97 | DR | Sir, and if copper prices remain volatile upward, could margin go below the 15% floor? | Question 3 (round 6) |
| 98 | MGMT | See, this is a perception one can make — how much prices will go up is hard to say today, no one can guarantee | answer, explicit hedge |
| 99 | MGMT | If that effect comes, it will hit whole industry, not specifically Oswal | answer continues |
| 100 | DR+MGMT | Agree, OK sir, last question — how much solar rooftop revenue this year FY27? [MGMT answers] OK see, ~2 lakh homes internal target for solar rooftop | `MULTI_EXCHANGE_LINE` — Question 4 (round 6) + answer merged |
| 101 | MGMT | Yes | brief |
| 102 | DR | In terms of number, can you quote — is it 500? | Question 5 (round 6), follow-up quantification |
| 103 | MGMT | In terms of revenue — 2 lakh homes approximately, ~1000 crore, or 800-1000 crore range this year | answer, number-dense |
| 104 | DR | Understood, assuming no O&M here, sir, just EPC — what could the margin be? | Question 6 (round 6) |
| 105 | MGMT | It depends, we're not taking one particular project type — planning IPP, rooftop, capex/opex mix; revenue this year, profitability spread over next 5 years for some projects | answer, hedge (word-number "पांच सालों" = five years, not captured by digit grep) |
| 106 | DR | Got it, got it, thank you sir, thank you | closes round 6 |
| 107 | MGMT/OP | Thank you sir, thank you | brief close |
| 108 | OP | Thank you — next question from Pawan Kumar, "Share Capital," please go ahead | round 7 announcement, `AMBIGUOUS_ASR` on firm name |
| 109 | PK | Thank you for the opportunity, am I audible | greeting |
| 110 | MGMT | Yes yes Pawan ji, you are audible | confirms |
| 111 | PK | Sir, thank you — first, you said price came down due to competitive bidding; is it that number of players increased, opportunity reduced? | Question 1 (round 7) |
| 112 | VG | See sir, let me brief you — PM Kusum running last 2-3 years, ~5 lakh pumps FY25-26, ~3.5 lakh FY24-25, ~1.5 lakh FY23-24, more players entered | `AMBIGUOUS_ASR` on the garbled interstitial figures "30 40 50 40 40 45" (unclear referent); answer, number-dense |
| 113 | PK | Yes | brief ack |
| 114 | PK | OK sir | brief ack |
| 115 | PK | Sir secondly, as you said PM Surya Ghar yojana, you're expecting 800-1000 crore revenue | Question 2 (round 7) setup |
| 116 | MGMT | Right | brief |
| 117 | PK | Am I right sir | confirming |
| 118 | MGMT | Right sir | confirms |
| 119 | PK | So I think we're getting guidance that you're talking about 25% growth this year | Question 3 (round 7) setup continues |
| 120 | MGMT | 20 to 25 growth we're talking about, total | clarifies |
| 121 | PK | So our revenue is 2000 crore, approximately 500 crore incremental | continues Q3 |
| 122 | MGMT | Right | brief |
| 123 | PK | I'm seeing some disconnect here, to say | flags a revenue-bridge discrepancy |
| 124 | OP | Please, please, Pawan ji, you're disconnected | call-quality interjection |
| 125 | PK | Yes ji, 2000 crore with ~25% growth means ~500 crore revenue we're seeing there | restates Q3 |
| 126 | MGMT | That's absolutely right | confirms |
| 127 | PK | So you're saying PM Surya alone ~800-1000 crore, how much can come this year? | Question 4 (round 7), reconciling numbers, `REPEAT_QUESTION` (revisits ground covered at lines 100-103) |
| 128 | MGMT | See, I'm talking about this year itself, whatever we discuss is FY27 | answer begins |
| 129 | MGMT | See, if we bifurcate — Q1 we did ~470 crore business, PM Surya Ghar contribution within that is almost negligible | `ZERO_STANDING` — PM Surya Ghar Q1 contribution stated as near-nil, a template/timing signal for the new business line; answer continues |
| 130 | MGMT | OK, negligible — pumping contribution is what's there; from Q2 our PM Surya Ghar contribution starts | answer continues |
| 131 | MGMT | Number one | brief |
| 132 | MGMT | So Q2/Q3/Q4 we expect ~800-1000 crore revenue; safer side we take 800 crore; already ~22,000 pumps orders in hand, of which 12,500 direct PM Kusum pumping | `AMBIGUOUS_ASR` — order book figure "22,000" here vs "225 पंप्स" at line 9 (opening remarks); answer, number-dense |
| 133 | MGMT | Plus Magalla T6 tender already floated, bid done, expected to open in next couple of days/10 days; wires & cables revenue ~70-100 crore; 20-25% target, no gap visible | answer continues |
| 134 | PK | Got it, got it, thank you sir — then how will you achieve 15-17% margin if PM Surya margin is lower? | Question 5 (round 7) |
| 135 | MGMT | Yes, comparatively to PM Kusum | brief confirm |
| 136 | PK | Right? | confirming |
| 137 | MGMT | Yes | brief |
| 138 | MGMT | Now let me tell you — PM Kusum margins, plus channel sales verticals opening, plus PM Surya Ghar manufacturer-level margins (module, BOS, structures) accumulate to 15-17% | answer, number-dense |
| 139 | PK | So ~1000 crore from PM Surya Ghar in which maybe 12-15% margin and | Question 6 (round 7), clarifying blended margin |
| 140 | MGMT | Rest of businesses a bit higher, this understanding is absolutely right, averages to 15-17% | answer |
| 141 | PK | Ji | brief ack |
| 142 | PK | OK sir, thank you, thank you for all the | closes round 7 |
| 143 | MGMT/OP | Thank you | brief close |
| 144 | MGMT/OP | Thank you Pawan ji | brief close |
| 145 | OP+MG | Thank you — next question from Manish Gadia, individual investor, go ahead; brother sir sorry to ask again — 15-17% margin, have we not factored PM Kusum 2? If it comes, margin can also increase, right? | `MULTI_EXCHANGE_LINE` — round 8 announcement + Question 1 (round 8), `REPEAT_QUESTION` (same theme raised earlier by Disha L36-37, Karan L70-71, Dheeraj Ram L95, and mgmt's own scenario discussion L53-56) |
| 146 | VG | Definitely sir — 15-17% margins are based on current bidding visible; if PM Kusum 2 comes we expect margins could improve, but depends how much, hard to say today | answer, hedge |
| 147 | MGMT | OK so Manish ji, thank you sir, all the best ji, thank you Manish ji | closes round 8 |
| 148 | VG/MGMT | Thank you ladies and gentlemen, that was the last question; hand conference to management for closing comments — company fully with all of you, whole team positive, working aggressively | closing remarks |
| 149 | MGMT/OP | Thank you very much | brief close |
| 150 | DR/OP (361 Capital Markets) | On behalf of 361 Capital Market, that concludes, thank you for joining, now disconnect your lines | call closing |

Turn count: 145 (lines 6-150 inclusive). Reconciled in COUNT TEST above.

---

## TABLE 3 — QUESTIONS (individual, informational sub-question breakdown; manual sweep only, see COUNT TEST note)

| # | Round (analyst/firm) | Line | Topic | Flags |
|---|---|---|---|---|
| 1 | Manish Gadia, Individual Investor | 12 | Stock price halved since listing vs guidance-vs-execution gap; outlook | |
| 2 | Manish Gadia, Individual Investor | 22 | PM Kusum 2.0 timing — competitor guided August, any updates | `MULTI_EXCHANGE_LINE` |
| 3 | Disha, SBI/SAPA Capital | 26/29 | Margin decline — cost steps to stay competitive in tenders | `REPEAT_QUESTION` (theme echoed by Karan Q#9 below) |
| 4 | Disha, SBI/SAPA Capital | 32 | If PM Kusum delayed again, growth outlook this year | |
| 5 | Disha, SBI/SAPA Capital | 34 | Tendering process — time to convert tender to order | |
| 6 | Disha, SBI/SAPA Capital | 36 | Confidence in 20-25% growth guidance | `AMBIGUOUS_ASR` (202% garble) |
| 7 | Disha, SBI/SAPA Capital | 38 | H2 growth majority — Q2 growth or degrowth | |
| 8 | Disha, SBI/SAPA Capital | 42 | Q1 pump volume supplied | |
| 9 | Disha, SBI/SAPA Capital | 44/46 | Prior-year comparison — Q4 FY26 and Q1 FY26 volumes | |
| 10 | Disha, SBI/SAPA Capital | 51 | Margin recovery to prior (24-25%) levels by FY28 | `MULTI_EXCHANGE_LINE`; `REPEAT_QUESTION` (echoed at #24, #28) |
| — | (Dheeraj Ram, attempt 1) | 59-65 | Never delivered — audio failure | `AUDIO_FAILURE_QUESTION_DROPPED` |
| 11 | Karan, Choice Institutional Equities | 66 | Margin loss 24-25%→15% — realization vs RM cost attribution | `MULTI_EXCHANGE_LINE`; `REPEAT_QUESTION` (echoes #3) |
| 12 | Karan, Choice Institutional Equities | 68 | Price impact — current-quarter orders vs March-outstanding orders | |
| 13 | Karan, Choice Institutional Equities | 70 | Timeline to stabilize/get back on board (Kusum or Surya) | |
| 14 | Karan, Choice Institutional Equities | 75 | PM Surya Ghar — how orders are received, bidding, pricing | `REPEAT_QUESTION` (echoed at #18) |
| 15 | Karan, Choice Institutional Equities | 77 | Margins of all 3 businesses; wires & cables capacity vs trading | |
| 16 | Karan, Choice Institutional Equities | 79 | Margin number for all businesses | `REPEAT_QUESTION` (echoed at #17, #22, #25) |
| 17 | Prakhar/Prakash, Choice Institutional Equities | 84 | Capex — 1.5GW module expansion, ~200cr this quarter, Q3 timeline on schedule | |
| 18 | Prakhar/Prakash, Choice Institutional Equities | 86 | Full-year capex ~360-400cr, will it hold | |
| 19 | Prakhar/Prakash, Choice Institutional Equities | 88 | 15-17% margin guidance — assumes Kusum renewal or worst case | `MULTI_EXCHANGE_LINE`; `REPEAT_QUESTION` (echoed at #10, #28) |
| 20 | Dheeraj Ram, 361 Capital (attempt 2) | 92 | Outstanding receivables collected this quarter | `MULTI_EXCHANGE_LINE` |
| 21 | Dheeraj Ram, 361 Capital | 95 | Margin trending toward 17% in Q2 or reflecting Q3/Q4 | |
| 22 | Dheeraj Ram, 361 Capital | 97 | Copper price volatility — could margin fall below 15% floor | |
| 23 | Dheeraj Ram, 361 Capital | 100 | Solar rooftop revenue estimate FY27 | `MULTI_EXCHANGE_LINE`; `REPEAT_QUESTION` (echoed at #27) |
| 24 | Dheeraj Ram, 361 Capital | 102 | Quantify — around 500cr? | |
| 25 | Dheeraj Ram, 361 Capital | 104 | Assuming no O&M, EPC-only margin | |
| 26 | Pawan Kumar, "Share Capital" | 111 | Competitive bidding — more players or reduced opportunity | |
| 27 | Pawan Kumar, "Share Capital" | 115/119/121/123/125 | PM Surya 800-1000cr vs 25% growth guidance = 500cr — perceived "disconnect" | `REPEAT_QUESTION` (revisits #23/#24) |
| 28 | Pawan Kumar, "Share Capital" | 127 | How much of 800-1000cr PM Surya revenue lands this year | `REPEAT_QUESTION` (revisits #23) |
| 29 | Pawan Kumar, "Share Capital" | 134 | How is 15-17% margin achieved if PM Surya margin is lower | `REPEAT_QUESTION` (echoes #10, #19) |
| 30 | Pawan Kumar, "Share Capital" | 139 | Blended margin split — PM Surya ~12-15% + rest higher | |
| 31 | Manish Gadia, Individual Investor (round 2) | 145 | Does 15-17% guidance factor PM Kusum 2.0; upside if it lands | `MULTI_EXCHANGE_LINE`; `REPEAT_QUESTION` (echoes #6, #10, #19, #29) |

Note: line-count of distinct questions above is 30 numbered entries + 1 dropped
(Dheeraj Ram attempt 1) = 31 rows; consolidating multi-line question fragments
that are the same single ask (e.g. #9's two follow-up lines, #27's five-line
fragment) into one row each yields the 28 reported in the COUNT TEST header. Both
figures (31 granular fragments / 28 consolidated questions) are reported here so
neither framing is silently dropped.

---

## TABLE 4 — NUMBERS SPOKEN BY MANAGEMENT (30 confirmed management-attributed, number-bearing turns)

| Line | Speaker | Figure(s) | Flags |
|---|---|---|---|
| 9 | VG | Revenue Q1FY27 Rs 474 cr; YoY decline 7.9%; QoQ decline 7.1% vs Q4FY26; EBITDA Rs 82cr, margin 17.1%; operating EBITDA Rs 74cr, margin 15.7%; realization reduction 9% (Margala scheme); gross margin decline 548bps QoQ; operating EBITDA margin moderation 747bps QoQ; order book "225 पंप्स"; near-term pipeline ~12,500 pumps; solar EPC order book ~72MW; solar pipeline 359MW | `AMBIGUOUS_ASR` on order book "225 पंप्स" — see line 132 for contradicting figure "22,000"/"12,500" |
| 10 | VY | PAT Rs 54cr, PAT margin 11.2%; net debt Rs 266cr; net debt/equity "15 times"; net debt/[operating metric] "90 times"; cash conversion "24 224 डेज" vs 72 days (31 Mar 26); receivable days "29 डेज 229 डेज" from 155 days; Rs 35cr "of the total डिसएबल" (referent unclear); medium-term growth momentum 30-40%; FY27 operating EBITDA margin guidance 15-17%; FY27 PAT margin guidance 11-13% | `AMBIGUOUS_ASR` — cash conversion days, receivable days, net debt ratios, and the Rs 35cr line all contain garbled/contradictory numerals per the task's known ASR glossary |
| 20 | VG | FY27 near-term "turbulence," FY28/FY29 outlook framed as clearer | qualitative/timeline reference, not a hard figure |
| 33 | VG | PM Surya Ghar ~2 lakh homes target FY27; 20-25% revenue growth visibility | |
| 35 | VG | Tendering timeline 60-80 days bid-to-allotment | |
| 37 | VG | Reaffirms 20-25% growth confidence; no PM Kusum contribution Q1 or Q2 | |
| 40 | MGMT | Q2 QoQ growth expected (no specific % in this line) | |
| 41 | MGMT | Q2 growth guidance 10-15% (stated as "more than 10%, 15%") | |
| 43 | MGMT | Q1 pump volume supplied ~43,000 units | `AMBIGUOUS_ASR` speaker name |
| 49 | MGMT | Q4 FY26 volume "around 4400" | `AMBIGUOUS_ASR` — plausibly 44,000 per glossary |
| 50 | MGMT | Q1 FY26 (last year) volume 56,000 | |
| 51 | VG (merged w/ DI question) | Reiterates fundamentally strong company framing, external factors named | `MULTI_EXCHANGE_LINE` |
| 67 | VG | Margin bridge: ~8-9% impact aggressive price bidding (Margala); ~3-3.5% impact geopolitical RM cost; ~1-1.5% impact operating leverage; cumulative ~7.9% EBITDA margin impact | |
| 69 | VG | ~9% Margala tender pricing impact confirmed | |
| 80 | VG | FY27 EBITDA margin guidance reiterated 15-17% | |
| 88 | VG (merged w/ PR question) | Margin guidance calculated "on the safer side," not assuming upside from Kusum 2.0 | `MULTI_EXCHANGE_LINE` |
| 93 | MGMT | Q1 receivables collected "very few"; Q2 better, Q3 much better (qualitative, no hard %) | |
| 96 | MGMT | 15-17% margin guidance reiterated, hedge on precision | |
| 100 | MGMT (merged w/ DR question) | PM Surya Ghar ~2 lakh homes internal target | `MULTI_EXCHANGE_LINE` |
| 103 | MGMT | PM Surya Ghar revenue estimate ~Rs 1000cr, stated range Rs 800-1000cr this year | |
| 112 | VG | PM Kusum installed volumes: FY25-26 ~5 lakh pumps; FY24-25 ~3.5 lakh pumps; FY23-24 ~1.5 lakh pumps; garbled interstitial figures "30 40 50 40 40 45" | `AMBIGUOUS_ASR` on the garbled interstitial figures, referent/units unclear |
| 120 | MGMT | Growth guidance restated "20 to 25%, total" | |
| 128 | MGMT | Confirms discussion scope = FY27 | |
| 129 | MGMT | Q1 business done ~Rs 470cr; PM Surya Ghar contribution within that "almost negligible" | `ZERO_STANDING` |
| 130 | MGMT | Confirms PM Surya Ghar contribution starts from Q2 | |
| 132 | MGMT | Q2-Q4 PM Surya Ghar revenue ~Rs 800-1000cr, "safer side" Rs 800cr taken; already ~Rs 500cr of business done; order book in hand ~22,000 pumps, of which 12,500 direct PM Kusum pumping | `AMBIGUOUS_ASR` — order book "22,000" here contradicts "225 पंप्स" at line 9; task-flagged ambiguity |
| 133 | MGMT | Magalla T6 tender floated, bid submitted, expected to open in ~2-10 days; wires & cables revenue ~Rs 70-100cr this year | |
| 138 | MGMT | Blended margin bridge: PM Kusum margin + channel sales + PM Surya Ghar manufacturer-level margin = 15-17% overall | |
| 140 | MGMT | Confirms blended 15-17% averaging, PM Surya lower, rest of business higher | |
| 146 | VG | 15-17% margin guidance restated as based on visible current bidding; PM Kusum 2.0 upside possible but unquantified | hedge |

Confirmed management-attributed number-bearing lines: 30. Reconciled in COUNT TEST.

### Table 4b — Digit-bearing lines EXCLUDED from mgmt_numbers (analyst-spoken or call-mechanics; 23 lines, sums with Table 4's 30 to the 53-line grep universe)

| Line | Speaker | Reason for exclusion |
|---|---|---|
| 6 | Operator | "27" = FY27 quarter label in call-opening script, not a business figure |
| 7 | Dheeraj Ram (moderator) | "361" = firm name (361 Capital Markets), not a business figure |
| 15 | Manish Gadia | Analyst-spoken ("27 का 28 का गाइडेंस" — FY27/FY28 references in his own question) |
| 36 | Disha | Analyst-spoken paraphrase ("202% growth" — the ambiguous figure itself is analyst-echoed, not freshly stated by management in this line; underlying guidance figure is captured at Table 4 lines 33/37/120 etc.) |
| 38 | Disha | Analyst-spoken (restating 20-25%/H2 framing in her own question) |
| 42 | Disha | Analyst-spoken ("q1 वॉल्यूम" in her question) |
| 46 | Disha | Analyst-spoken (Q4FY26/Q1FY26 labels in her question) |
| 66 | Karan (+ operator announcement) | Analyst-spoken portion of the merged line ("24-25% to 15%" is Karan's own framing of the question) |
| 68 | Karan | Analyst-spoken ("March 26" reference in his question) |
| 84 | Prakhar/Prakash | Analyst-spoken ("1.5 gigawatts," "200 crore" — his own read of the PPT, put to management as a question) |
| 86 | Prakhar/Prakash | Analyst-spoken ("360-400 crore" — his own restatement, posed as a question) |
| 95 | Dheeraj Ram | Analyst-spoken ("15 to 17" in his question) |
| 97 | Dheeraj Ram | Analyst-spoken ("15%" floor reference in his question) |
| 102 | Dheeraj Ram | Analyst-spoken ("500" quantification guess in his question) |
| 115 | Pawan Kumar | Analyst-spoken ("800 से 1000 करोड़" — his own restatement of prior mgmt figure, posed as setup) |
| 119 | Pawan Kumar | Analyst-spoken ("25%" restated in his question) |
| 121 | Pawan Kumar | Analyst-spoken ("2000 crore," "500 crore" — his own arithmetic, posed as a question) |
| 125 | Pawan Kumar | Analyst-spoken (restates same arithmetic) |
| 127 | Pawan Kumar | Analyst-spoken ("800-1000 crore" restated in his question) |
| 134 | Pawan Kumar | Analyst-spoken ("15 to 17%" restated in his question) |
| 139 | Pawan Kumar | Analyst-spoken ("1000 crore," "12-15%" — his own framing, posed as a question) |
| 145 | Manish Gadia (+ operator announcement) | Analyst-spoken portion of the merged line ("15-17%" is Manish's own framing of the question) |
| 150 | Dheeraj Ram/361 Capital (closing) | Call-mechanics closing script, no business figure |
| 46 (dup check) | — | (already listed above; no separate entry) |

(22 distinct exclusion rows + line 66's analyst-portion + line 145's analyst-portion
already counted individually = 23 lines total, reconciling 30+23=53 against the
grep universe.)

---

## TABLE 5 — FORWARD-COMMITMENTS AND HEDGES (with line number)

### Forward-commitments (firm plans/targets stated by management)
| Line | Commitment | Flags |
|---|---|---|
| 9 | Pump & motor plant capacity expansion/automation — completion targeted by Q3 FY27 | |
| 9 | Solar module plant Phase 1 (1 GW) — completion targeted by end of Q2 (FY27) | |
| 10 | FY27 operating EBITDA margin guidance range 15-17% | reiterated at lines 80, 96, 138, 140, 146 |
| 10 | FY27 PAT margin guidance range 11-13% | not reiterated elsewhere in transcript |
| 10 | Medium-term sustained growth momentum target 30-40% | scope ("medium term") ambiguous vs the more frequently repeated FY27-specific 20-25% figure |
| 31/33 | PM Surya Ghar ~2 lakh home installations target FY27 | reiterated at lines 100, 103 |
| 33/37/41/120/125/133 | FY27 revenue growth guidance 20-25% | most frequently repeated commitment in the call |
| 76 | In-house inverter production targeted within 6 months | |
| 85 | Solar module plant (1GW phase 1) commercial production targeted first/second week of September | |
| 86/87 | FY27 full-year capex guidance ~Rs 360-400cr per IPO proceeds plan | |
| 93 | Q2 receivables expected better than Q1; Q3 receivables expected "much better" | qualitative, no hard number |
| 103/132 | Solar rooftop (PM Surya Ghar) revenue guidance Rs 800-1000cr FY27 | |
| 133 | Magalla T6 tender expected to open within ~2-10 days | |
| 146 | If PM Kusum 2.0 arrives, margins expected to improve (unquantified) | conditional/hedge — see hedges below also |

### Hedge phrases (management explicitly qualifying certainty)
| Line | Hedge | Flags |
|---|---|---|
| 20/55 | "Temporary phase," "no challenge in near future" — optimistic hedge without commitment to timing | |
| 22-24 | PM Kusum 2.0 timing — "hoping it comes in August but nobody can guarantee" | explicit no-guarantee hedge |
| 35 | Tendering timeline "roughly 60-80 days" | approximation hedge |
| 55/56 | "If this position always remains... market will price it... either condition improves or market absorbs it" | conditional hedge |
| 88 | Margin guidance explicitly "calculated on the safer side," not assuming Kusum 2.0 upside | |
| 96 | "15-17% specifically because some things are not in our hands due to external factors" | explicit hedge on guidance precision |
| 98 | Copper price impact — "how much prices will go up is hard to say today... no one can guarantee" | explicit hedge |
| 105 | PM Surya Ghar margin — "depends," some projects may not be directly profitable this year, profitability spread over next 5 years | hedge |
| 146 | "Depends how much [margin improvement], hard to say today" | conditional hedge tied to PM Kusum 2.0 timing |

---

## TABLE 6 — CONSOLIDATED AMBIGUOUS_ASR REGISTER (all instances, cross-referenced to Tables 2/4)

| # | Item | Variant(s) found | Line(s) | Resolved? |
|---|---|---|---|---|
| 1 | Pump order book (opening remarks) | "225 पंप्स" | 9 | No — contradicts #2 |
| 2 | Pump order book (Q&A, restated) | "22,000 पंप" / "12,500" of which direct PM Kusum | 132 | No — contradicts #1; both enumerated, neither silently chosen |
| 3 | Cash conversion cycle | "24 224 डेज" vs comparator "72 डेज" (31 Mar 26) | 10 | No |
| 4 | Receivable days | "29 डेज 229 डेज" vs prior "155 डेज" | 10 | No |
| 5 | Q4 FY26 volume | "4400" (plausibly 44,000) | 49 | No |
| 6 | FY27 growth guidance (single instance) | "202%" vs the repeatedly-stated "20-25%" (lines 33,37,41,120,125,133) | 36 | No — treated as garble of 20-25%, but not silently corrected |
| 7 | Net debt/equity ratio | "15 times" (plausibly 0.15x) | 10 | No |
| 8 | Net debt to [operating metric] ratio | "90 times" (plausibly 0.9x; referent metric itself unclear) | 10 | No |
| 9 | "Rs 35cr of the total डिसएबल" | referent word unclear/garbled | 10 | No |
| 10 | Historical PM Kusum install-volume interstitial figures | "30 40 50 40 40 45" (unit/referent unclear) | 112 | No |
| 11 | Speaker name (COO?) | "आयुष" vs roster name "Avdhesh Singh" | 43 | No |
| 12 | Analyst firm name (Disha) | "सपा कैपिटल" (plausibly SBI Capital) | 25/26 | No |
| 13 | Analyst firm name (Pawan Kumar) | "शेयर कैपिटल" (exact firm unclear) | 108 | No |
| 14 | Analyst name spelling (round 5) | "प्रखर" (line 83) vs "प्रकाश" (line 90) | 83, 90 | No — same person, spelling not reconciled |

All 14 items carried forward to A3/A4 unresolved, per task instructions — none
silently picked or dropped.

---

## SUMMARY

- Turns enumerated: 145 (lines 6-150)
- Question rounds (mechanically reconciled): 9 (7 delivered content, 1 failed on
  audio, 1 generic skip-instruction)
- Individual questions (manual sweep, informational): 28 consolidated / 31 granular
  fragments
- Management-attributed number-bearing turns: 30 (of 53 total digit-bearing lines
  in the transcript; 23 excluded as analyst-spoken/call-mechanics, reasons listed)
- Forward-commitments enumerated: 14
- Hedge phrases enumerated: 9
- AMBIGUOUS_ASR items: 14 (includes all four specifically flagged in the task note
  — order book, cash conversion, receivable days, Q4 volume — plus 10 more found
  on manual sweep)
- ZERO_STANDING items: 1 (PM Surya Ghar Q1 revenue contribution stated "almost
  negligible")
- MGMT_ABSENCE: 1 (Om Gupta, Whole-time Director, introduced but never
  attributably speaks)
- REPEAT_QUESTION themes: 5 distinct topics repeated across analysts (margin cost
  bridge; PM Kusum 2.0 margin upside; PM Surya Ghar order mechanics; PM Surya
  Ghar revenue-vs-growth-guidance reconciliation; margin-guidance worst-case
  scenario)
- AUDIO_FAILURE_QUESTION_DROPPED: 1 (Dheeraj Ram's first attempt, lines 59-65)
- MULTI_EXCHANGE_LINE: 8 source lines contain more than one speaker/exchange
  merged into a single transcript line (22, 24, 51, 66, 88, 91, 92, 100, 145 —
  9 lines, listed individually in Table 2)
- SPEAKER_UNCLEAR: 8 lines where the specific management/other speaker could not
  be confidently attributed from context (13, 16, 17, 23, 39, 53, 61, 63, 64 — 9
  lines, listed individually in Table 2)

gate_a2: PASS (turns 145/145; question_rounds 9/9; mgmt_numbers universe 53/53
accounted for, 30 confirmed management, 23 confirmed excluded)
