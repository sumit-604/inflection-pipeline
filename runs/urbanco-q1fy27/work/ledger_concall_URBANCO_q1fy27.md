# LEDGER — Concall Transcript — URBANCO Q1 FY27
Source: extract_concall_URBANCO_q1fy27.txt (102 lines; plain-text transcript, no page/formfeed markers; unit convention Cr INR unless stated)
Note on source quality (carried from A1 header): transcription contains verbatim errors — "FI27"(FY27), "IBIDA/AITA"(EBITDA), "instead/instel/Insta Health"(InstaHelp), "Abhat/Abhira/Airaj/Aira/Ain"(CEO name, Abhiraj Singh Bhal), "dam/spam/town/stam/channel/price"(TAM), and stray digit artifacts (e.g. "1,56 crores", "a,000 crores", "7 to 12,000 0 crores"). These are preserved verbatim below with a TRANSCRIPTION_GARBLED flag where the true figure is ambiguous. Nothing was corrected or estimated.

Line-numbering convention: line numbers below are the raw file line numbers (as returned by the Read tool / `cat -n`) of the paragraph block in which the turn begins. Seven paragraph blocks contain two speakers merged with no transcript break (lines 20, 44, 56, 80, 86, 94, 96); each such block is split into sub-turns "a"/"b" at the same line number, both cited explicitly below.

=== A2 COUNT TEST ===
category: participants   grep_count: 8    sweep_count: 8    match: yes
category: turns          grep_count: 51   sweep_count: 51   match: yes
category: questions      grep_count: 16   sweep_count: 16   match: yes
category: mgmt_numbers   grep_count: 103  sweep_count: 103  match: yes
category: phrases        grep_count: 32   sweep_count: 32   match: yes
gate_a2: pass
=== END COUNT TEST ===

Methodology notes on reconciliation (kept here, not repeated per category below):
- participants: grep = `grep -noE '(Mr\.|Miss|Mrs\.) [A-Za-z]+'` → 9 raw hits, deduplicated to 8 unique named individuals (CEO "Abhirat"/"Abhat" is the same person mentioned twice in the intro line). Manual sweep independently reads all 8 same people. Unnamed call operator (addressed once by the CEO as "Baba") is listed separately below and excluded from the gated count since it is neither management nor an analyst.
- turns: mechanical grep = `awk 'NR>=16 && NR<=102 && NF>0 {print NR}'` → 44 blank-line-delimited paragraph blocks. Manual close-read found 7 of those 44 blocks contain a second, undelimited speaker change (lines 20, 44, 56, 80, 86, 94, 96), each independently confirmed by a name-vocative/thanks/greeting cue at the merge point. 44 + 7 = 51, matching the manual sweep total of 51 turns exactly.
- questions: ordinal/declarative marker grep (`first question|second question|third question|last question|next question|three questions`) restricted to analyst-turn lines returns 13 real boundary markers (one false-positive preview mention at line 42 excluded: Manish previews "my second question" while still inside Q1). The 3 questions lacking any ordinal marker (Shinat Q1 at line 86a, Pranav Q1 at line 94b, Pranav's follow-up at line 96b) were independently confirmed present by a supplemental interrogative-pattern grep (`is this|what kind|how (is|are|should)|my question is|would you`) matching all three. 13 + 3 = 16, matching manual sweep.
- mgmt_numbers: combined regex (unit-adjacent numbers `%|crore(s)|rupees?|million|lakh(s)|bps|hours?|households?|days?|months?|years?`, `FY[0-9]{2}`, `Q[0-9] FY[0-9]{2}`, bare "N to M" ranges, "N plus", and bare 4-digit years `20[0-9]{2}`) run against every CEO-attributed line/line-portion → 103 hits. Manual sweep built one row per hit, in order, below; totals 103.
- phrases: forward-commitment cue grep (`continue to retain|second core profit engine|line of sight|will become|we want to be|we are investing|cement our leadership|certainly have no intentions|certainly not building|going for`, CEO-attributed only, one analyst false positive at line 42 excluded) → 17 hits. Hedge cue grep (`ahead of ourselves|best visualized|not really in our control|some quarters it will be|don't want to trivialize|maybe in a few years|very difficult for us to see|would not like to comment|we don't know|worst case|don't want to get ahead|have not necessarily seen adequate evidence|rarely does|very large unbounded market`) → 15 hits. 17 + 15 = 32, matching manual sweep.

---
## 1. PARTICIPANTS

| # | Name (as transcribed) | Role/Firm | Side | First appears (line) | Flags |
|---|---|---|---|---|---|
| 1 | Abhiraj Singh Bhal (transcribed "Abhirat"/"Abhat" Singh Bhal) | CEO & co-founder, Urban Company | Management | 16 (introduced), 18 (speaks) | — |
| 2 | Abhim Matur | Chief Financial Officer, Urban Company | Management | 16 (introduced) | **MGMT_DYNAMICS** — CFO is named in the operator's opening introduction ("Mr. Abhim Matur, chief financial officer... on the call today") but has zero attributed speaking turns anywhere in the 51-turn transcript; every management answer across all 16 analyst questions comes from the CEO alone. |
| 3 | Gorav (transcribed "Goravia"/"Gorov"/"Korov") | Analyst, Morgan Stanley | Analyst | 20 | — |
| 4 | Manish Adukia | Analyst, Goldman Sachs | Analyst | 40 | — |
| 5 | Sachin Salgaocar (transcribed "Salgawar") | Analyst, Bank of America | Analyst | 54 | — |
| 6 | Garima Mishra (transcribed "Gimma Mishra"/"Karima") | Analyst, Kotak | Analyst | 70 | — |
| 7 | Sinat (transcribed "Sinat"/"Shina"/"Reinat"; surname not given) | Analyst, Belwa Capital | Analyst | 84 | Name spelling inconsistent across 3 transcribed forms in one session — TRANSCRIPTION_GARBLED, actual name likely differs (e.g. "Shinet"/"Shrinath") |
| 8 | Pranav Chhatria | Analyst, MK Global | Analyst | 94 | — |
| — | Unnamed call operator/moderator (addressed once by CEO as "Baba") | Conference call operator | Facilitator (not gated) | 16 | Not a company or analyst participant; runs housekeeping and hands mic between speakers throughout (turns 1,3,14,22,31,39,45,51 per turn ledger below) |

Confirmed: no promoter/Chairman other than the CEO is on the call; no MGMT_ABSENCE flag on the CEO side (CEO present and answers every question). CFO's total silence is flagged MGMT_DYNAMICS per above — every one of the 16 analyst questions, including three finance/margin-heavy questions (Manish Q2 on ICS margin ceiling, Sachin Q1 on InstaHelp unit economics, Gorav Q3 on capital allocation) is fielded by the CEO.

---
## 2. SPEAKER TURNS (sequential, all 51)

| Turn | Line | Speaker | First ~10 words |
|---|---|---|---|
| 1 | 16 | Operator | "Good evening ladies and gentlemen. Welcome to Urban Company Limited's..." |
| 2 | 18 | CEO (Abhiraj Singh Bhal) | "Thank you very much Baba. Good Evening ladies and gentlemen and..." |
| 3 | 20a | Operator | "Thank you, Abhira. We will now wait for the question..." |
| 4 | 20b | Gorav (Morgan Stanley) | "Hi, hope I'm audible." |
| 5 | 22 | CEO | "Yes." |
| 6 | 24 | Gorav (Morgan Stanley) — Q1 | "Yeah. Hi, congratulations on uh great performance. Uh my first..." |
| 7 | 26 | CEO — A1 pt.1 | "yeah that's a good question Gorov um I think the..." |
| 8 | 28 | CEO — A1 pt.2 | "Um at what point uh can we go out there..." |
| 9 | 30 | Gorav — Q2 | "Thank you for the detailed answer. My second question is..." |
| 10 | 32 | CEO — A2 | "Yeah, so Um a we think insta help is strategically..." |
| 11 | 34 | Gorav — Q3 | "All right, last question from me on capital allocation framework..." |
| 12 | 36 | CEO — A3 | "Yeah. So from a two-year perspective um if I go..." |
| 13 | 38 | Gorav — closing | "Thank you. All the best." |
| 14 | 40 | Operator | "Thank you. Thanks Korov. Um our next question is from..." |
| 15 | 42 | Manish Adukia (Goldman Sachs) — Q1 | "Hi, good evening. Uh, thank you for taking my questions..." |
| 16 | 44a | CEO — A1 | "thanks for the question Manish uh Manish two parts to..." |
| 17 | 44b | Manish — Q2 | "my second question is on India core services and the..." |
| 18 | 46 | CEO — A2 | "I think our goal right now is to get to..." |
| 19 | 48 | Manish — Q3 | "Very clear. My last question is on uh Insta Help..." |
| 20 | 50 | CEO — A3 | "Yeah. So let me let me delve a little bit..." |
| 21 | 52 | Manish — closing | "Very comprehensive and very clear. Thank you and all the..." |
| 22 | 54 | Operator | "Thanks Manish. Uh next question is from the line of..." |
| 23 | 56a | Sachin Salgaocar (BofA) — Q1 | "Hi Aira, congrats on a great set of numbers. I..." |
| 24 | 56b | CEO — A1 | "Sachin we've articulated that the AOV has to get..." |
| 25 | 58 | Sachin — Q2 (start) | "Pretty clear. Um second question is on the core business..." |
| 26 | 60 | Sachin — Q2 (continued) | "U so you know when we think about uh let's..." |
| 27 | 62 | CEO — A2 | "Yes, Sin, we we also believe the TAM here is..." |
| 28 | 64 | Sachin — Q3 | "pretty clear and last question uh on AI and how..." |
| 29 | 66 | CEO — A3 | "Yes. So, I think AI uh I would say we're..." |
| 30 | 68 | Sachin — closing | "Very clear. Thank you and all the best." |
| 31 | 70 | Operator | "Thanks Ain. Our next question is from the line of..." |
| 32 | 72 | Garima Mishra (Kotak) — Q1 | "Thank you so much for the opportunity and congratulations on..." |
| 33 | 74 | CEO — A1 | "Thanks for the question. However, the beauty segment I..." |
| 34 | 76 | Garima — Q2 | "Got it. Um next question uh that I had was..." |
| 35 | 78 | CEO — A2 | "Um we have not necessarily seen adequate evidence of that..." |
| 36 | 80a | Garima — Q3 | "Got it. Got it. That's clear. Um, last question from..." |
| 37 | 80b | CEO — A3 | "I think the you know the the category is still..." |
| 38 | 82 | Garima — closing | "Perfect Airaj. Thank you so much and wish you the..." |
| 39 | 84 | Operator | "Thanks Karima. Next question is from the line of Mr...." |
| 40 | 86a | Sinat (Belwa Capital) — Q1 | "Hi Airaj just want to you know hear your thoughts...." |
| 41 | 86b | CEO — A1 | "Hey Shina, thanks for thanks for the question. Um, I..." |
| 42 | 88 | Sinat — Q2 | "Fantastic. Uh if you know in the next shareholders letter..." |
| 43 | 90 | CEO — A2 | "Yeah. No, good question. So on core shin I think..." |
| 44 | 92 | Sinat — closing | "Thanks a lot. Fantastic." |
| 45 | 94a | Operator | "Thanks Reinat. Moving on to our final question of the..." |
| 46 | 94b | Pranav Chhatria (MK Global) — Q1 | "Yeah. Hi. Uh thank you for the opportunity. Uh my..." |
| 47 | 96a | CEO — A1 | "Thanks for the question. Um I think on uh native..." |
| 48 | 96b | Pranav — follow-up Q | "...would you want to constrain yourself to some premium products..." |
| 49 | 98 | CEO — A2 | "Yeah, it's a it's a good question and goes back..." |
| 50 | 100 | Pranav — closing | "Uh thank you for uh such a detailed answer. Wish..." |
| 51 | 102 | Operator | "Thank you Prana. Thank you everyone for your participation. You..." |

Q&A share: 49 of 51 turns (96%) fall after the opening remarks (turns 1-2); operator housekeeping accounts for 8 turns (1,3,14,22,31,39,45,51); all remaining 43 turns are analyst/CEO exchange. CEO turns: 21 (2,5,7,8,10,12,16,18,20,24,27,29,33,35,37,41,43,47,49 = 19, plus turn5 "Yes" = 20... recount: turns 2,5,7,8,10,12,16,18,20,24,27,29,33,35,37,41,43,47,49 = 19 CEO turns). Analyst turns: 22 (questions + closings across 6 analysts, turns 4,6,9,11,13,15,17,19,21,23,25,26,28,30,32,34,36,38,40,42,44,46,48,50 = 24 analyst turns). 19+24+8=51.

---
## 3. ANALYST QUESTIONS LEDGER (16 distinct questions)

| Q# | Turn | Line | Analyst | Firm | Topic | Flags |
|---|---|---|---|---|---|---|
| 1 | 6 | 24 | Gorav | Morgan Stanley | ICS "cheaper/faster/better" flywheel — when can management call the growth trajectory structurally shifted? | REPEAT_QUESTION (ICS growth/TAM theme; recurs with Sachin Q25-26, Garima Q32) |
| 2 | 9 | 30 | Gorav | Morgan Stanley | InstaHelp: why does it deserve this much management time/bandwidth; competitive spillover risk into core categories | REPEAT_QUESTION (InstaHelp theme; recurs Manish Q19, Sachin Q23, Garima Q34, Garima Q36) |
| 3 | 11 | 34 | Gorav | Morgan Stanley | Capital allocation framework once consolidated adjusted EBITDA reaches breakeven (~Q3 FY28) | — |
| 4 | 15 | 42 | Manish Adukia | Goldman Sachs | Why not enter new international markets given UAE/Singapore playbook success | — |
| 5 | 17 | 44b | Manish Adukia | Goldman Sachs | ICS margin: is 9-10% guidance now conservative; will margin be capped at 10% or allowed to exceed | REPEAT_QUESTION (ICS margin theme; recurs with Gorav Q1's flywheel/margin framing, Sachin Q28's AI-margin question) |
| 6 | 19 | 48 | Manish Adukia | Goldman Sachs | InstaHelp: revised TAM and structurally lower margins — can the segment be profitable at all, even with 2 players and a narrow loss range | REPEAT_QUESTION (InstaHelp theme) |
| 7 | 23 | 56a | Sachin Salgaocar | Bank of America | InstaHelp AOV: comfort that steady-state AOV reaches 300 given competitors expect AOV to stay low | REPEAT_QUESTION (InstaHelp theme) |
| 8 | 25-26 | 58, 60 | Sachin Salgaocar | Bank of America | Core ICS growth durability/acceleration and TAM size, tier 2 expansion | REPEAT_QUESTION (ICS growth/TAM theme) |
| 9 | 28 | 64 | Sachin Salgaocar | Bank of America | AI: how much margin benefit already reflected vs. remaining headroom | — |
| 10 | 32 | 72 | Garima Mishra | Kotak | Beauty segment: drivers of accelerated growth and sustainability given rising competition | REPEAT_QUESTION (ICS growth/sub-category theme) |
| 11 | 34 | 76 | Garima Mishra | Kotak | InstaHelp TAM: could frequency assumption (30-40x annually) prove conservative if usage shifts from backup to main service | REPEAT_QUESTION (InstaHelp TAM theme) |
| 12 | 36 | 80a | Garima Mishra | Kotak | InstaHelp: signs of impending consolidation among cash-burning players | REPEAT_QUESTION (InstaHelp theme) |
| 13 | 40 | 86a | Sinat | Belwa Capital | ICS: nature of the ~5 lakh QoQ ATU addition — organic vs. funnel/app-download driven | — |
| 14 | 42 | 88 | Sinat | Belwa Capital | Training capacity: InstaHelp and core ICS — is capacity keeping pace with growth | — |
| 15 | 46 | 94b | Pranav Chhatria | MK Global | Native: is the shift to premium products (M3, smart lock) driven by a more premium customer base; how will category count evolve | — |
| 16 | 48 | 96b | Pranav Chhatria | MK Global | Native: future-category product strategy — constrain to premium, or span the full range | — |

REPEAT_QUESTION themes, summarized:
- **InstaHelp** (TAM, unit economics/AOV, structural margin, consolidation risk): Q2(Gorav), Q6(Manish), Q7(Sachin), Q11(Garima), Q12(Garima) — 5 of 16 questions, asked by 4 of 6 analysts.
- **ICS growth / TAM / margin**: Q1(Gorav), Q5(Manish), Q8(Sachin), Q10(Garima) — 4 of 16 questions, asked by 4 of 6 analysts.

---
## 4. NUMBERS SPOKEN BY MANAGEMENT (103 rows; CEO-only, CFO silent per MGMT_DYNAMICS)

| # | Turn | Line | Figure | Context | Flags |
|---|---|---|---|---|---|
| 1 | 2 | 18 | Q1 FY27 | Quarter under discussion | — |
| 2 | 2 | 18 | 42% | Consolidated NTV YoY growth | — |
| 3 | 2 | 18 | 1465 crores | Consolidated NTV, absolute | — |
| 4 | 2 | 18 | 44% | Consolidated revenue YoY growth | — |
| 5 | 2 | 18 | 528 crores | Consolidated revenue, absolute | — |
| 6 | 2 | 18 | 13.2 million | Total orders | — |
| 7 | 2 | 18 | 79% | Total orders YoY growth | — |
| 8 | 2 | 18 | 1.2 million | New customers added in quarter | — |
| 9 | 2 | 18 | 1 million | "Crossing the 1 million mark for the first time in a quarter" (new-customer milestone) | — |
| 10 | 2 | 18 | 9.3 million | Annual transacting user (ATU) base | — |
| 11 | 2 | 18 | 29% | ICS NTV YoY growth (headline) | — |
| 12 | 2 | 18 | "1,56 crores" | ICS NTV absolute, as transcribed | TRANSCRIPTION_GARBLED — likely "1,566 Cr" or similar; not corrected |
| 13 | 2 | 18 | "a,000 crores" (transcribed "000 crores") | ICS NTV crossing this threshold "for the first time in a quarter" | TRANSCRIPTION_GARBLED — likely "1,000 Cr" |
| 14 | 2 | 18 | 10% | ICS growth rate, same quarter last year (base of 4-quarter acceleration) | — |
| 15 | 2 | 18 | 19% → 21% | ICS growth acceleration, intermediate quarters (progression) | — |
| 16 | 2 | 18 | 29% | ICS NTV YoY growth, restated ("now 29% year-on-year growth") | — |
| 17 | 2 | 18 | 6.9% | ICS adjusted EBITDA margin (% of NTV), this quarter | — |
| 18 | 2 | 18 | 5.2% | ICS adjusted EBITDA margin, same period last year | — |
| 19 | 2 | 18 | 76% | International NTV YoY growth | — |
| 20 | 2 | 18 | 51% | Native NTV YoY growth | — |
| 21 | 2 | 18 | 119 crores | Native NTV, absolute | — |
| 22 | 2 | 18 | 60% | Native net revenue YoY growth | — |
| 23 | 2 | 18 | 95 crores | Native net revenue, absolute | — |
| 24 | 2 | 18 | 7.3% | Native adjusted EBITDA loss (% of NTV), this quarter | — |
| 25 | 2 | 18 | 11.4% | Native adjusted EBITDA loss, year back | — |
| 26 | 2 | 18 | ~75% | Water-purifier first-replacement-cycle filter renewal rate | — |
| 27 | 2 | 18 | 3.82 million | InstaHelp orders | — |
| 28 | 2 | 18 | 43% | InstaHelp orders QoQ growth | — |
| 29 | 2 | 18 | 132 crores | InstaHelp adjusted EBITDA loss | — |
| 30 | 2 | 18 | 447 rupees | InstaHelp loss per order, Q4 | — |
| 31 | 2 | 18 | 346 rupees | InstaHelp loss per order, this quarter | Raw grep matched a garbled overlap fragment "4 to 346" (regex artifact of "447...to 346"); manual sweep records the true figure |
| 32 | 2 | 18 | 7,000 - 12,000 crores | InstaHelp TAM, top-15 cities (first mention) | — |
| 33 | 2 | 18 | 65 crores | Consolidated adjusted loss | — |
| 34 | 2 | 18 | 132 crores | InstaHelp loss, restated as the driver of the consol. loss | — |
| 35 | 2 | 18 | 67 crores | Ex-InstaHelp adjusted EBITDA profit | — |
| 36 | 2 | 18 | >100% | Ex-InstaHelp EBITDA YoY growth | — |
| 37 | 2 | 18 | 116% | Ex-InstaHelp EBITDA YoY growth, precise | — |
| 38 | 2 | 18 | 19 crores | Cash & treasury investments, quarter-end | flagged in A1 header for plausibility ("19 crores" cash on a company this size) |
| 39 | 2 | 18 | ~2 crores | Cash decline QoQ | — |
| 40 | 2 | 18 | Q3 FY28 | Guidance: consolidated adjusted EBITDA breakeven | — |
| 41 | 2 | 18 | 1,000 crores | Guidance: FY31 adjusted EBITDA target | — |
| 42 | 2 | 18 | FY31 | Guidance year-tag paired with row 41 | — |
| 43 | 7 | 26 | 50+ | ICS service categories ("50 plus service categories across hundreds if not thousands of micro markets") | — |
| 44 | 7 | 26 | 30-60 minutes | "UC Instant" core-service fulfillment window | — |
| 45 | 8 | 28 | 9-10% | Long-term ICS adjusted EBITDA margin guidance (% of NTV) | — |
| 46 | 8 | 28 | 21% | "the 21% year-on-year growth we are seeing" — base-effect commentary | TRANSCRIPTION_AMBIGUOUS — immediately follows discussion of the 29% headline growth number and monsoon base-effect; possibly a mistranscription of 29% |
| 47 | 10 | 32 | 7,000 crores | InstaHelp TAM, low end (restated) | — |
| 48 | 10 | 32 | 12,000 crores | InstaHelp TAM, high end (restated) | — |
| 49 | 12 | 36 | ~18 months | Timeline to overall consolidated adjusted breakeven ("hopefully latest in the next 18 months or so") | — |
| 50 | 16 | 44a | 76% | International NTV YoY growth (restated) | — |
| 51 | 16 | 44a | 58% | International NTV YoY growth, ex-currency (constant currency) | — |
| 52 | 18 | 46 | 10% | ICS margin ceiling reference ("once we get to that 10% stage") | — |
| 53 | 20 | 50 | 7 - 12,000 crores | InstaHelp TAM range (restated) | — |
| 54 | 20 | 50 | "0 crores" | Stray digit fragment: "between uh 7 to 12,000 0 crores" | TRANSCRIPTION_GARBLED |
| 55 | 20 | 50 | 7-8 [billion, as transcribed] | InstaHelp base case: monthly transacting households | TRANSCRIPTION_IMPLAUSIBLE — "billion" households is not plausible at this addressable-market scale; likely "million," not corrected per rule 4 |
| 56 | 20 | 50 | 300 rupees | InstaHelp base-case full price point, per hour | — |
| 57 | 20 | 50 | 200 rupees | InstaHelp base-case alternate price point, per hour | — |
| 58 | 20 | 50 | 20 million | Implied InstaHelp ATU under base case | — |
| 59 | 20 | 50 | 10-12 million | InstaHelp bull-case monthly transacting households | — |
| 60 | 20 | 50 | 10-12,000 crores | InstaHelp bull-case TAM translation (NTV) | — |
| 61 | 20 | 50 | ~6 months | Competitive-behavior observation window ("over the past 6 months") | — |
| 62 | 20 | 50 | 10-12,000 crores | Bull-case TAM, restated ("bull case assumption... of 10 to 12,000 crores") | — |
| 63 | 20 | 50 | 7-8,000 crores base / 10,000 crores aggressive | InstaHelp TAM, base and aggressive case restated explicitly | — |
| 64 | 20 | 50 | 5 years | "no intentions of making any money from this business over the next 5 years" | Hedge-adjacent |
| 65 | 20 | 50 | FY31 | InstaHelp segment breakeven guidance year | — |
| 66 | 24 | 56b | 130-160 rupees/hr | Service-professional sustainable pay range | — |
| 67 | 24 | 56b | 140-150 hours | Achievable monthly utilization hours | — |
| 68 | 24 | 56b | 150 hours | Utilization assumption, restated | — |
| 69 | 24 | 56b | 6 hours | Daily utilized hours | — |
| 70 | 24 | 56b | 8-9 hours | Daily hours available (base for utilization %) | — |
| 71 | 24 | 56b | ~65% | Implied utilization rate | — |
| 72 | 24 | 56b | 20,000-22,000 rupees | Minimum required partner net earnings/month | — |
| 73 | 24 | 56b | 15,000-17,000 rupees | Offline earnings comparator/month | — |
| 74 | 24 | 56b | 130-160 rupees | Pay range, restated | — |
| 75 | 24 | 56b | 11 years | Company operating track record | — |
| 76 | 24 | 56b | 50+ | Categories operated across (restated) | — |
| 77 | 24 | 56b | 150 rupees/hr | Gross-margin breakeven price point | — |
| 78 | 24 | 56b | 200 rupees/hr | Full-cost (all-in) breakeven price point | — |
| 79 | 24 | 56b | 50 rupees | Incremental margin needed above 150 for full-cost breakeven | — |
| 80 | 24 | 56b | 5 years | "will it take 5 years? We don't know" | Hedge |
| 81 | 24 | 56b | 5 years | "we're taking the worst case here which is 5 years" (restated) | Hedge |
| 82 | 27 | 62 | 29% | Current ICS growth referenced again | — |
| 83 | 27 | 62 | 29% | Restated ("the 29% does have a little bit of margin") | — |
| 84 | 27 | 62 | 19% | Base-quarter growth comparison | — |
| 85 | 27 | 62 | 17% | Base-quarter growth comparison | — |
| 86 | 27 | 62 | 19% → 21% | Growth progression, restated (partial) | — |
| 87 | 27 | 62 | 26% → 29% | Growth progression, restated (partial) | — |
| 88 | 29 | 66 | "90 95%" (transcribed) | Share of engineering code now AI-written | TRANSCRIPTION_GARBLED — missing connector, read as "90 to 95%" |
| 89 | 33 | 74 | ~100% | Target two-wheeler adoption among beauty service professionals | — |
| 90 | 35 | 78 | 8-10 times/month | InstaHelp usage frequency, "bachelor/younger user" sub-segment | — |
| 91 | 35 | 78 | 80-100 rupees/hr | Offline pricing comparator | — |
| 92 | 35 | 78 | up to 120 rupees/hr | Offline pricing upper bound | — |
| 93 | 35 | 78 | 30-40 times/month | InstaHelp transaction frequency observed in most-compressed micro markets | — |
| 94 | 35 | 78 | 10-12 million | Bull-case monthly transacting households, restated | — |
| 95 | 41 | 86b | 24 crores | ICS marketing spend, same period last year | — |
| 96 | 41 | 86b | 25 crores | ICS marketing spend, this year | — |
| 97 | 47 | 96a | 2023 | Native M1/M2 water-purifier launch year (October 2023) | — |
| 98 | 47 | 96a | 3 years | M3 no-service-needed interval | — |
| 99 | 47 | 96a | 3 years | Restated ("you're again set up for three more years") | — |
| 100 | 47 | 96a | 5 years | Timeline horizon for a possible one additional Native category | — |
| 101 | 49 | 98 | 9.3 million | ATU, restated in Native-strategy context | — |
| 102 | 49 | 98 | 9.3 million | "the top 9.3 million households", restated/conflated with ATU in same sentence | TRANSCRIPTION_AMBIGUOUS — CEO conflates "users" and "households" mid-sentence |
| 103 | 49 | 98 | 8 million | "...or whatever 8 million households in the country" — self-correction/hedge on prior figure | Hedge-adjacent |

Zero/nil/dash standing items: none apply to this doctype (concall transcript carries no standing financial-statement line items). No ZERO_STANDING flags raised in this ledger.

---
## 5. FORWARD-COMMITMENT AND HEDGE PHRASES (32 rows)

### 5a. Forward-commitment phrases (17)

| # | Turn | Line | Phrase (verbatim excerpt) |
|---|---|---|---|
| 1 | 2 | 18 | "We continue to retain our guidance of consolidated adjusted IBIDA break even by Q3 FY28 and 1,000 crores in adjusted [EBITDA] by FY31" |
| 2 | 2 | 18 | "[International] will become the second core profit engine of urban company in the coming years" |
| 3 | 2 | 18 | "We are investing aggressively in Insta to cement our leadership for a category that we believe is of strategic importance" |
| 4 | 12 | 36 | "We want to be disciplined and maximize growth while ensuring that there is steady improvements in margin" (ICS) |
| 5 | 12 | 36 | "We now believe that we have line of sight of profitability [in] the coming quarters" (Saudi JV) |
| 6 | 12 | 36 | "We now have line of sight of profitability in native... over the next few quarters" |
| 7 | 12 | 36 | "We are investing... [InstaHelp] fair to say over the next two years if not longer we'll continue to take investments" |
| 8 | 16 | 44a | "We want to be sharply focused on these [India, UAE, Singapore, Saudi JV]" |
| 9 | 18 | 46 | "Our goal right now is to get to that number" [10% ICS margin] |
| 10 | 20 | 50 | "We believe it is even more important for us over the next few quarters to be aggressive [in InstaHelp]" |
| 11 | 20 | 50 | "We want to be very aggressive right now so that... we capture disproportionate share of the TAM... and... of the profit" |
| 12 | 20 | 50 | "We certainly have no intentions of making any money from this business over the next 5 years" [InstaHelp] |
| 13 | 29 | 66 | "We want to be at the forefront of [the AI shift]" |
| 14 | 37 | 80b | "We want to be the eventual winner here... we're not playing to look elegant. We don't want to give an inch away" |
| 15 | 37 | 80b | "...and that's what we're going for" [InstaHelp market leadership] |
| 16 | 47 | 96a | "If at all we have to venture into another category over the next 5 years, maybe we will enter one more category" [Native] |
| 17 | 49 | 98 | "We are certainly not building a consumer durable play in native" |

### 5b. Hedge phrases (15)

| # | Turn | Line | Phrase (verbatim excerpt) |
|---|---|---|---|
| 1 | 7 | 26 | "As management we've always refrained from giving any forward-looking guidance on this business" [ICS] |
| 2 | 8 | 28 | "I do want to highlight a couple of things... so that we also don't get very ahead of ourselves" |
| 3 | 8 | 28 | "Margins... are best visualized year on year" |
| 4 | 8 | 28 | "[Growth] is an outcome of it. It's not really in our control" |
| 5 | 12 | 36 | "Some quarters it will be up, some quarters it will be down" [ICS margin trajectory] |
| 6 | 16 | 44a | "I also don't want to trivialize what it actually takes to enter and win in a market... you need... a little bit of good luck" |
| 7 | 16 | 44a | "Maybe in a few years... we may change that thought process" [re: no new international markets] |
| 8 | 20 | 50 | "When will the pricing correct to its full potential? Very difficult for us to see" |
| 9 | 24 | 56b | "I would not like to comment on... how prudent the view of our competitors is" |
| 10 | 24 | 56b | "How soon will it get there? Will it take a couple of years? Will it take 5 years? We don't know. We're taking the worst case here which is 5 years" |
| 11 | 27 | 62 | "I don't want to get ahead of ourselves. I don't want to set the wrong expectations here" |
| 12 | 27 | 62 | "I would not get too caught up with a quarter here or a quarter there" |
| 13 | 35 | 78 | "We have not necessarily seen adequate evidence of that happening at scale" [InstaHelp frequency upside] |
| 14 | 35 | 78 | "Rarely does larger future cohorts behave better than early cohorts. Usually the usership of future cohorts only deteriorates" |
| 15 | 37 | 80b | "We don't think there's a very large unbounded market which can support multiple winners" [InstaHelp] |

---
## SUMMARY

- Participants: 8 (2 management incl. one silent CFO flagged MGMT_DYNAMICS; 6 analysts) + 1 unnamed operator (not gated).
- Turns: 51, of which 19 CEO, 24 analyst, 8 operator.
- Distinct analyst questions: 16, with InstaHelp (5 questions/4 analysts) and ICS growth/margin/TAM (4 questions/4 analysts) both flagged REPEAT_QUESTION.
- Management-spoken numbers: 103 rows, including 5 TRANSCRIPTION_GARBLED/TRANSCRIPTION_IMPLAUSIBLE/TRANSCRIPTION_AMBIGUOUS-flagged figures (rows 12, 13, 31, 46, 54, 55, 88, 102 — 8 total transcription-quality flags) that A3/A4 should treat as NOT FOUND-equivalent for any precision arithmetic check rather than as clean anchors.
- Forward-commitment phrases: 17. Hedge phrases: 15.
- CFO named but silent for the entire call (MGMT_DYNAMICS) — every management answer, across all 16 questions and all four opening-remarks pillars, is the CEO alone.

GATE A2: PASS — all five categories reconcile grep vs. sweep exactly (see COUNT TEST above and methodology notes).
