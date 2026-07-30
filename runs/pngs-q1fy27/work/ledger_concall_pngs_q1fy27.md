# LEDGER — A2 ENUMERATOR — PNGSREVA Q1FY27 — Concall

Source: `/home/user/inflection-pipeline/runs/pngs-q1fy27/work/extract_concall_pngs_q1fy27.txt`
(plain-text transcript, 208 source lines / 231 extract lines with A1 structural markers, content_coverage 100%, gate_a1 = pass)

Units: MIXED per A1 header — P&L figures in Rs Cr shorthand ("K"/"cr" both used loosely for Crore),
finance-cost split in Rs Million, AOV in Rs Lakh, inventory turn as a ratio (x). All figures below are
carried in the unit management actually spoke; conversions are NOT applied by A2 (enumeration only,
no interpretation) but are noted inline per A1's conversion_factor_to_cr for downstream A3/A4 use.

```
=== A2 COUNT TEST ===
category: turns          grep_count: 103  sweep_count: 103  match: yes
category: questions      grep_count: 35   sweep_count: 35   match: yes
category: mgmt_numbers   grep_count: 76   sweep_count: 76   match: yes
category: slides         grep_count: 0    sweep_count: 0    match: yes   (n/a — doctype=concall, no deck in this extract)
category: notes          grep_count: 0    sweep_count: 0    match: yes   (n/a — doctype=concall, no numbered notes)
gate_a2: pass
=== END COUNT TEST ===
```

**Reconciliation note (mgmt_numbers):** first grep pass (raw `[0-9]` token extraction across all
management-attributed lines, grouped into claims per line) and first manual topic-sweep both
independently landed on 73. Per operating rule 3 (zero/nil standing items must never be dropped), a
targeted re-sweep for negation/zero language ("not using," "no ... as such," "don't have anyone yet")
in management speech surfaced 3 additional ZERO_STANDING rows the first pass missed (MN34, MN66, MN76
below). Both counting methods were re-run including these 3 rows and both landed on 76. Final
grep_count = sweep_count = 76 → gate passes at 76, not 73.

---

## 0. PARTICIPANT ROSTER

| # | Name | Designation / Firm | Side | Turns |
|---|---|---|---|---|
| 1 | Operator (unnamed) | Conference operator | Non-management | T1, T5, T13, T23, T33, T37, T42, T54, T62, T63, T69, T77, T83, T87, T101, T103 |
| 2 | "Suya Sam Shaman" (name garbled by STT) | Stellar Investor Relations Advisors (IR) | IR | T2 |
| 3 | Amit Modak | Whole-time Director & CEO | Management | T3 only (opening remarks) — **flag MGMT_ABSENCE**: cites fever/throat illness, explicitly hands the entire remainder of the call, including all 12 Q&A turns, to the Non-executive Director (line 46) |
| 4 | Aditya Modak | Non-executive Director | Management | T4 (opening operational/financial highlights), all subsequent [A] answer turns (T7 onward), T41 (deferred finance-cost follow-up), T102 (closing) — de facto sole management voice on this call |
| 5 | Prince Chheda | Pink Wealth | Analyst | Q&A Turn 1 (T6–T12) |
| 6 | Kushi Jain | Share India Securities | Analyst | Q&A Turn 2 (T14–T22) |
| 7 | Harsha | Mas Advisor / Marcellus | Analyst | Q&A Turn 3 (T24–T32), Turn 7 (T55–T61, cut short by operator interrupt T62), Turn 10 (T78–T82) — 3 turns, same questioner, requeued twice |
| 8 | Kesha Bhansali | SBSPL | Analyst | Q&A Turn 4 (T34–T36) |
| 9 | Harshit Pandya | Blue Star Capital | Analyst | Q&A Turn 5 (T38–T40) |
| 10 | Ankit Gupta | Bamboo Capital | Analyst | Q&A Turn 6 (T43–T53) |
| 11 | Pranav | Rare Enterprises | Analyst | Q&A Turn 8 (T64–T68) |
| 12 | Rahul Kumar Pal | Sapphire / Sheffa Family Office | Analyst | Q&A Turn 9 (T70–T76) |
| 13 | Prashant | Individual investor | Analyst | Q&A Turn 11 (T84–T86) |
| 14 | Dhruv Jain | Individual investor | Analyst | Q&A Turn 12 (T88–T100) |

10 unique questioners, 12 Q&A turns (Harsha appears 3x via requeue). Matches A1's
`unique_questioners`/`qa_turn_count_observed` header exactly — no discrepancy with A1.

---

## 1. TURNS LEDGER (103 rows — count-test anchor for this doctype)

Every discrete speaker turn, sequential, with line number, speaker, first ~10 words, flags.

| Turn# | Line | Speaker | First ~10 words | Flags |
|---|---|---|---|---|
| T1 | 40 | Operator | "Ladies and gentlemen, good day and welcome to the..." | |
| T2 | 43 | IR (Stellar) | "Thank you. Good afternoon everyone and thank you for..." | |
| T3 | 46 | CEO Amit Modak | "It's almost 4:30 so I will say good afternoon..." | MGMT_ABSENCE (cites illness, hands off entire call) |
| T4 | 49 | Director Aditya Modak | "Uh thank you sir. So uh good afternoon everyone..." | carries MN1–MN24 |
| T5 | 52 | Operator | "Thank you. Thank you very much sir. We will now..." | Q&A session begin + Turn1 intro combined |
| T6 | 55 | Q — Prince Chheda, Pink Wealth | "Yeah. Hi sir. Uh congratulations on the good sides..." | Turn1 Q1 |
| T7 | 57 | A — Management | "Yeah. Thanks. Uh first of all like you have..." | MN25 |
| T8 | 59 | Q — Prince Chheda (follow-up) | "uh so but uh for the folure how do you..." | Turn1 Q1-followup |
| T9 | 61 | A — Management | "so uh aida margins so the current margins that..." | MN26–MN30 |
| T10 | 63 | Q — Prince Chheda | "understood and second question how do you see the..." | Turn1 Q2 |
| T11 | 65 | A — Management | "so uh I think uh through if you see uh..." | MN31 |
| T12 | 67 | Q — Prince Chheda (closing) | "Okay sir, understood. Thank you for answer the question." | |
| T13 | 70 | Operator | "Thank you. We have our next question from the..." | Turn2 intro |
| T14 | 72 | Q — Kushi Jain, Share India Securities | "Yeah. Hello. Uh thank you for taking my question..." | Turn2 Q1 |
| T15 | 74 | A — Management | "Yeah. Hi Kushi. So I have the volume growth..." | MN32 |
| T16 | 76 | Q — Kushi Jain | "Okay. Um also thank you for the answer. Uh..." | Turn2 Q2 |
| T17 | 78 | A — Management | "Yeah. So uh I think uh so basically we do..." | MN76 ZERO_STANDING |
| T18 | 80 | Q — Kushi Jain | "Okay perfect. Uh last question from my side uh..." | Turn2 Q3 |
| T19 | 82 | A — Management | "Sorry, can you repeat?" | |
| T20 | 84 | Q — Kushi Jain (clarify/repeat) | "I want same sales growth on the cocoa model..." | CLARIFICATION_REPEAT of T18, not a new question |
| T21 | 86 | A — Management | "So all the triple SG that has happened is..." | MN33, MN34 ZERO_STANDING |
| T22 | 88 | Q — Kushi Jain (closing) | "Okay. Okay. Uh thank you and yeah," | |
| T23 | 91 | Operator | "Thank you. We have our next question from the..." | Turn3 intro |
| T24 | 93 | Q — Harsha, Mas Advisor/Marcellus | "Yeah. Hi sir. Hi Amit sir. Uh hi Arita..." | Turn3 Q1; REPEAT_QUESTION (vs Turn2 SSG topic) |
| T25 | 95 | A — Management | "yes sir" | MN35 |
| T26 | 97 | Q — Harsha | "okay okay and one more thing um actually just..." | Turn3 Q2 |
| T27 | 99 | A — Management | "So all the IPO proceeds which are parked in..." | MN36; ANALYST_STATED_MGMT_CONFIRMED, CROSS_CHECK |
| T28 | 101 | Q — Harsha | "Okay. Okay. And uh we keep it in." | |
| T29 | 103 | A — Management | "Okay. That is entirely the interest income treasury..." | |
| T30 | 105 | Q — Harsha | "Okay. And sir uh can you give bifurcation on..." | Turn3 Q3 |
| T31 | 107 | A — Management (deferred) | "uh just give me one minute I'm just accepting..." | DEFERRED_ANSWER → answered at T41 |
| T32 | 109 | Q — Harsha | "Sure. No wor I'll join back with you." | |
| T33 | 112 | Operator | "Thank you. A reminder to all participants... next..." | Turn4 intro |
| T34 | 114 | Q — Kesha Bhansali, SBSPL | "Hi sir. Congratulations on great set of numbers..." | Turn4 Q1 |
| T35 | 116 | A — Management | "So this is because our sales has gone up..." | MN37; ANALYST_STATED_MGMT_CONFIRMED, CROSS_CHECK |
| T36 | 118 | Q — Kesha Bhansali (closing) | "Yeah. Yeah. Your it was there but this number..." | |
| T37 | 121 | Operator | "Thank you. A reminder to all participants... next..." | Turn5 intro |
| T38 | 123 | Q — Harshit Pandya, Blue Star Capital | "Hello. Am I audible? Yeah. First of all,..." | Turn5 Q1 |
| T39 | 125 | A — Management | "So uh we we we honestly I think Mur..." | GUIDANCE reaffirmed, no new number |
| T40 | 127 | Q — Harshit Pandya (closing) | "Okay. Thank you and all the best sir." | |
| T41 | 130 | Management follow-up | "Thank you. And uh uh I would like to..." | MN38–MN40; ARITHMETIC_INCONSISTENCY, CROSS_CHECK, UNIT_MILLION |
| T42 | 133 | Operator | "A reminder to all participants... next question from..." | Turn6 intro |
| T43 | 135 | Q — Ankit Gupta, Bamboo Capital | "for the opportunity and congratulations for a good..." | Turn6 Q1 |
| T44 | 137 | A — Management | "Yeah. Hi. Uh that's a yeah very much a..." | MN41; CONTRADICTORY_STATEMENT (states "no investment buying" then "there is investment buying but lower") |
| T45 | 139 | Q — Ankit Gupta (follow-up) | "so because I'm actually if you look at the..." | ANALYST_STATED figures (PJS Gadgil 11%, PNGS Reva ~120%) — not mgmt numbers |
| T46 | 141 | A — Management (defers) | "Of course so obviously we would be answering that..." | DEFERRED_TO_OTHER_ENTITY_CALL |
| T47 | 143 | Q — Ankit Gupta | "No and sir just you know uh next year..." | Turn6 Q2 |
| T48 | 145 | A — Management | "yeah so uh I think what we are expecting..." | MN42–MN47 |
| T49 | 147 | Q — Ankit Gupta | "impact levels but obviously the contribution topline..." | Turn6 Q2-followup |
| T50 | 149 | A — Management | "so 75 is where it break even and one..." | MN48–MN49; TRANSCRIPTION_AMBIGUITY |
| T51 | 151 | Q — Ankit Gupta | "Okay. So so if.5 inventory comes we start..." | Turn6 Q2-followup2 |
| T52 | 153 | A — Management (correction) | "sorry correct 75 is break even" | MN50 |
| T53 | 155 | Q — Ankit Gupta (closing) | "oh 75 okay okay thank you so much I..." | |
| T54 | 158 | Operator | "Thank you. We have our next question from line..." | Turn7 intro (Harsha 2nd requeue) |
| T55 | 160 | Q — Harsha | "Yeah. Uh hi sir. Um so I just noted..." | Turn7 Q1; REPEAT_QUESTION (topic-adjacent to Turn6) |
| T56 | 162 | A — Management | "So the competition from lab grown is not that..." | MN51–MN53 |
| T57 | 164 | Q — Harsha | "Okay. How can you repeat the diamond category..." | clarify |
| T58 | 166 | A — Management | "So it it say so basically smaller diamonds the..." | |
| T59 | 168 | Q — Harsha | "Star mele or minus2 diamonds. Okay. And uh..." | Turn7 Q2; REPEAT_QUESTION (overlaps Turn6 inventory-turn topic) |
| T60 | 170 | A — Management | "So currently we are having 1.29 and I think..." | MN54–MN56 |
| T61 | 172 | Q — Harsha | "Okay and if I can squeeze one more" | INTERRUPTED_QUESTION — never completed |
| T62 | 174 | Operator (interrupt) | "sorry to interrupt you hush may we please..." | forces Harsha to requeue |
| T63 | 177 | Operator | "Thank you. We have our next question from the..." | Turn8 intro |
| T64 | 179 | Q — Pranav, Rare Enterprises | "Uh hi sir. Uh thanks a lot for the..." | Turn8 Q1+Q2 (two-part) |
| T65 | 181 | A — Management | "Uh can you repeat the second question sorry" | |
| T66 | 183 | Q — Pranav (repeats Q2) | "uh can you give the store opening guidance..." | CLARIFICATION_REPEAT of T64 part b |
| T67 | 185 | A — Management | "okay so to answer your first question uh the..." | MN57–MN58 |
| T68 | 187 | Q — Pranav (closing) | "thanks a lot sir" | |
| T69 | 190 | Operator | "Thank you. We have our next question from the..." | Turn9 intro |
| T70 | 192 | Q — Rahul Kumar Pal, Sapphire/Sheffa Family Office | "Thanks for the opportunity. Thank you um and..." | Turn9 Q1 |
| T71 | 194 | A — Management | "Hi sir. Uh thank you. So basically like I..." | MN59–MN60 |
| T72 | 196 | Q — Rahul Kumar Pal | "Got it. Got it. Similarly with the 27th CR..." | Turn9 Q2; ANALYST_STATED FY PAT assumption Rs80–100cr, UNCONFIRMED_BY_MGMT; also states trade payable 30→20cr |
| T73 | 198 | A — Management | "So uh I think it it so it is not..." | no new number; ANALYST_STATED_MGMT_CONFIRMED re trade payable |
| T74 | 200 | Q — Rahul Kumar Pal | "Got it. Got it. Got it. And my final..." | Turn9 Q3a+Q3b (two-part) |
| T75 | 202 | A — Management | "so like so basically to answer your first..." | MN61–MN62 |
| T76 | 204 | Q — Rahul Kumar Pal (closing) | "Got it. Next. All the best to you on..." | |
| T77 | 207 | Operator | "Thank you. We have a follow-up question from the..." | Turn10 intro (Harsha 3rd requeue) |
| T78 | 209 | Q — Harsha | "Yeah. Hi sir. Uh so I wanted to ask..." | Turn10 Q1; AOV_FIGURE_DISCREPANCY raised |
| T79 | 211 | A — Management | "So generally so if you see there is a..." | MN63–MN65; AOV_FIGURE_DISCREPANCY not resolved |
| T80 | 213 | Q — Harsha | "Okay. Okay. Understood sir. And uh one more..." | Turn10 Q2 |
| T81 | 215 | A — Management | "So of course we are uh in hunt uh..." | MN66 ZERO_STANDING; HEDGE |
| T82 | 217 | Q — Harsha (closing) | "Okay. Oops. Thank you." | |
| T83 | 220 | Operator | "Thank you. We have our next question from the..." | Turn11 intro |
| T84 | 222 | Q — Prashant, individual investor | "Yeah. Hello. Uh thank you. Uh I think all..." | Turn11 Q1 |
| T85 | 224 | A — Management | "Uh so for EBO within Maharasha, it will be..." | MN67–MN70; STORE_COUNT_DISCREPANCY |
| T86 | 226 | Q — Prashant (closing) | "Okay. Okay, thank you." | |
| T87 | 229 | Operator | "Thank you. We have our next question from the..." | Turn12 intro |
| T88 | 231 | Q — Dhruv Jain, individual investor | "Hello sir. Am I audible? Yes. Yeah...." | Turn12 Q1 |
| T89 | 233 | A — Management | "No. So basically I was mentioning about the..." | MN71–MN73; CROSS_CHECK (200-300bps) |
| T90 | 235 | Q — Dhruv Jain | "right. So uh so if my understanding is..." | Turn12 Q1-followup |
| T91 | 237 | A — Management | "Correct." | |
| T92 | 239 | Q — Dhruv Jain | "Right. And uh secondly, sir, my uh just a..." | Turn12 Q2 |
| T93 | 241 | A — Management | "So it was WCDL taken at the start of..." | MN74–MN75; CROSS_CHECK |
| T94 | 243 | Q — Dhruv Jain | "right so uh so do we plan to uh..." | Turn12 Q2-followup |
| T95 | 245 | A — Management | "it won't be cleared entirely but as and as..." | |
| T96 | 247 | Q — Dhruv Jain | "right so so by going by this our..." | Turn12 Q2-followup2 |
| T97 | 249 | A — Management | "yeah yeah correct" | |
| T98 | 251 | Q — Dhruv Jain | "okay and uh sir if I can squeeze in..." | Turn12 Q3 |
| T99 | 253 | A — Management | "So primarily it will be through internal acrals..." | |
| T100 | 255 | Q — Dhruv Jain (closing) | "Okay sir thank you thank you so much and..." | |
| T101 | 258 | Operator | "Thank you ladies and gentlemen. That was the last..." | Q&A session ends |
| T102 | 261 | Closing — Aditya Modak | "Yes. So, thank you all for joining us today..." | |
| T103 | 264 | Operator (sign-off) | "Thank you members of the management. On behalf of..." | |

---

## 2. QUESTIONS LEDGER (35 rows)

Every distinct analyst question including follow-ups and multi-part questions counted per part.

| Q# | Turn ref | Line | Analyst / Firm | Topic | Flags |
|---|---|---|---|---|---|
| Q1 | T6 (QA-Turn1) | 55 | Prince Chheda, Pink Wealth | EBITDA/PAT margin sustainability + drivers (scale vs product mix) | |
| Q2 | T8 | 59 | Prince Chheda | Follow-up: sustainable EBITDA margin going forward | |
| Q3 | T10 | 63 | Prince Chheda | Demand for natural diamonds outside Pune | |
| Q4 | T14 (QA-Turn2) | 72 | Kushi Jain, Share India Securities | Volume growth June and mid-July | |
| Q5 | T16 | 76 | Kushi Jain | Inventory hedging practice — gold vs MCX/GML | |
| Q6 | T18/T20 | 80/84 | Kushi Jain | SSG split: Coco (EBO) vs shop-in-shop (SIS) | line84 is a mis-heard repeat of the same ask, not a new question |
| Q7 | T24 (QA-Turn3) | 93 | Harsha, Mas Advisor/Marcellus | Confirm SSG 50% is on YoY basis | REPEAT_QUESTION (re-confirms Q6's SSG topic) |
| Q8 | T26 | 97 | Harsha | Reason for other income jump to Rs5.6cr | CROSS_CHECK |
| Q9 | T30 | 105 | Harsha | Finance-cost bifurcation: lease interest vs loan interest | DEFERRED — answered at T41 (Management follow-up) |
| Q10 | T34 (QA-Turn4) | 114 | Kesha Bhansali, SBSPL | Change in inventory of finished goods Rs30cr — how determined | CROSS_CHECK |
| Q11 | T38 (QA-Turn5) | 123 | Harshit Pandya, Blue Star Capital | Upward revision to guidance given strong results | |
| Q12 | T43 (QA-Turn6) | 135 | Ankit Gupta, Bamboo Capital | Impact of PM Modi's gold-buying remarks on sales sentiment | |
| Q13 | T45 | 139 | Ankit Gupta | Follow-up: comparison with sister co PJS Gadgil's slowdown to 11% | management defers to that entity's own call |
| Q14 | T47 | 143 | Ankit Gupta | FY28/29 sales split SIS vs EBO and margin/return impact | |
| Q15 | T49 | 147 | Ankit Gupta | Clarify: is 1.25x–1.5x inventory turn the profit/breakeven threshold | |
| Q16 | T51 | 151 | Ankit Gupta | Further clarify 0.75x vs 1.2x breakeven confusion | |
| Q17 | T55 (QA-Turn7) | 160 | Harsha (2nd turn) | Lab-grown diamond competitive intensity | REPEAT_QUESTION (topic-adjacent to Q14–16 margin/EBO thread) |
| Q18 | T57 | 164 | Harsha | Clarify: repeat the diamond category name | |
| Q19 | T59 | 168 | Harsha | Inventory turn guidance FY27/28/29 | REPEAT_QUESTION (overlaps Q15/Q16) |
| Q20 | T61 | 172 | Harsha | [unstated — cut off by operator] | INTERRUPTED_QUESTION, never completed or answered |
| Q21 | T64a (QA-Turn8) | 179 | Pranav, Rare Enterprises | Volume growth number (missed due to sound quality) — repeat ask | |
| Q22 | T64b/T66 | 179/183 | Pranav | Store opening guidance split — EBO vs franchise | |
| Q23 | T70 (QA-Turn9) | 192 | Rahul Kumar Pal, Sapphire/Sheffa Family Office | Will next 2 quarters be better on festive seasonality | |
| Q24 | T72 | 196 | Rahul Kumar Pal | Trade payable fell Rs30cr → Rs20cr — reason | CROSS_CHECK |
| Q25 | T74a | 200 | Rahul Kumar Pal | Can margin/inventory-turn dent from EBOs be offset via scale/efficiency/AOV | |
| Q26 | T74b | 200 | Rahul Kumar Pal | EBO geography plan and DRHP 24-month timeline — any aggression on target | |
| Q27 | T78 (QA-Turn10) | 209 | Harsha (3rd turn) | AOV difference vs last quarter/year — seasonality driven? | AOV_FIGURE_DISCREPANCY (analyst cites Rs1,29,000 "for March 26"; mgmt answers with Rs1,12,000 "last quarter" — different figures, unreconciled) |
| Q28 | T80 | 213 | Harsha | Brand ambassador / marketing activity plans for H2 | |
| Q29 | T84 (QA-Turn11) | 222 | Prashant, individual investor | EBO average break-even period | |
| Q30 | T88 (QA-Turn12) | 231 | Dhruv Jain, individual investor | Does 200–300bps margin guidance include EBITDA losses from 9 new EBOs | |
| Q31 | T90 | 235 | Dhruv Jain | Confirm: margin impact driven more by marketing cost than EBO fixed cost | |
| Q32 | T92 | 239 | Dhruv Jain | Short-term debt Rs166cr at FY26-end — what is it for | CROSS_CHECK |
| Q33 | T94 | 243 | Dhruv Jain | Plan to clear this debt by year-end? | |
| Q34 | T96 | 247 | Dhruv Jain | Confirm: quarterly interest cost to decline sequentially | |
| Q35 | T98 | 251 | Dhruv Jain | EBO expansion funding — debt or internal accruals | |

---

## 3. MANAGEMENT QUANTIFIED CLAIMS / GUIDANCE LEDGER (76 rows)

Every number and forward-looking statement spoken by management, opening remarks + Q&A + the
deferred management follow-up. REPORTED_ACTUAL = stated as already-occurred fact. GUIDANCE =
forward-looking target/expectation. CONTEXT/OPINION = qualitative/benchmark, not a hard company
number. RESTATED = same underlying figure repeated at a later line (kept as its own row per operating
rule 2 — every row carries its own line number — since restatements are the raw material for the
Role 5 arithmetic-consistency check).

| MN# | Line | Claim | Value | Type | Flags |
|---|---|---|---|---|---|
| MN1 | 49 | Inventory turn, Q1FY27 | 1.29x | REPORTED_ACTUAL | |
| MN2 | 49 | Industry-accepted inventory-turn range for diamond | "0.75x"–1.5x (verbatim "75x to 1.5x") | CONTEXT | TRANSCRIPTION_AMBIGUITY |
| MN3 | 49 | AOV, Q1FY27 | ~Rs1,00,000 (1 lakh) | REPORTED_ACTUAL | |
| MN4 | 49 | Revenue from operations | Rs118 Cr | REPORTED_ACTUAL | |
| MN5 | 49 | Revenue growth YoY | 119.5% | REPORTED_ACTUAL | |
| MN6 | 49 | Gross profit | Rs41.83 Cr | REPORTED_ACTUAL | |
| MN7 | 49 | Gross profit growth YoY | 147.25% | REPORTED_ACTUAL | |
| MN8 | 49 | Gross margin | 35.46% | REPORTED_ACTUAL | |
| MN9 | 49 | EBITDA | Rs33.92 Cr | REPORTED_ACTUAL | |
| MN10 | 49 | EBITDA growth YoY | 192.88% | REPORTED_ACTUAL | |
| MN11 | 49 | EBITDA margin | 28.76% | REPORTED_ACTUAL | CROSS_CHECK vs MN29 (29% restated in Q&A) |
| MN12 | 49 | PAT | Rs27.21 Cr | REPORTED_ACTUAL | |
| MN13 | 49 | PAT growth YoY | 265% | REPORTED_ACTUAL | |
| MN14 | 49 | PAT margin | 23.06% | REPORTED_ACTUAL | |
| MN15 | 49 | Akshaya Tritiya revenue, Q1FY27 | Rs12.7 Cr | REPORTED_ACTUAL | |
| MN16 | 49 | Akshaya Tritiya revenue, comparative (Q1FY26) | Rs3.5 Cr | REPORTED_ACTUAL | |
| MN17 | 49 | Akshaya Tritiya growth YoY | 268% | REPORTED_ACTUAL | |
| MN18 | 49 | New Coco store opened | Amanora, Pune, 7-Jul-2026 | REPORTED_ACTUAL | |
| MN19 | 49 | Total store network | 37 stores | REPORTED_ACTUAL | |
| MN20 | 49 | Network mix | 3 Coco + 34 shop-in-shop (PNGS) | REPORTED_ACTUAL | |
| MN21 | 49 | Coco store expansion plan | 15 new stores via IPO proceeds | GUIDANCE | |
| MN22 | 49 | Stores already operational (of the 15) | 2 | REPORTED_ACTUAL | CROSS_CHECK vs MN67 ("3 EBOs opened" at line 224) |
| MN23 | 49 | Store-opening plan, year 1 post-IPO | 9 stores | GUIDANCE | |
| MN24 | 49 | E-commerce website launch | end-August 2026 | GUIDANCE | |
| MN25 | 57 | Margin dent expected from Q2–Q4 marketing ramp | 1–2% | GUIDANCE | |
| MN26 | 61 | EBITDA margin guidance, annual | 25–27% | GUIDANCE | |
| MN27 | 61 | PAT margin guidance | 20–23% | GUIDANCE | |
| MN28 | 61 | Dent reiterated | "2–3%" | GUIDANCE | |
| MN29 | 61 | Current EBITDA margin (restated) | 29% | REPORTED_ACTUAL (restated) | CROSS_CHECK vs MN11 (28.76%) |
| MN30 | 61 | Current PAT margin (restated) | ~23% | REPORTED_ACTUAL (restated) | |
| MN31 | 65 | Cities with company presence | 21 | REPORTED_ACTUAL | |
| MN32 | 74 | Volume growth (diamond carats), Q1 | >50% YoY | REPORTED_ACTUAL | |
| MN33 | 86 | SIS (shop-in-shop) SSG | ~50% | REPORTED_ACTUAL | |
| MN34 | 86 | EBO/Coco SSG (like-for-like) | 0 / not applicable — no EBO store older than 1 year | ZERO_STANDING | never dropped per operating rule 3 |
| MN35 | 95 | Confirms SSG 50% figure basis | year-on-year | REPORTED_ACTUAL (confirmation) | |
| MN36 | 99 | Other income driver (figure Rs5.6cr sourced from analyst Q, line 97) | IPO-proceeds treasury/interest income | REPORTED_ACTUAL / CONFIRMED | ANALYST_STATED_MGMT_CONFIRMED, CROSS_CHECK |
| MN37 | 116 | Change in inventory of finished goods (figure Rs30cr sourced from analyst Q, line 114) | confirmed as routine, consistent with prior quarters | REPORTED_ACTUAL / CONFIRMED | ANALYST_STATED_MGMT_CONFIRMED, CROSS_CHECK |
| MN38 | 130 | Total finance cost | Rs27 million (~Rs2.7 Cr) | REPORTED_ACTUAL | ARITHMETIC_INCONSISTENCY, CROSS_CHECK, UNIT_MILLION |
| MN39 | 130 | Pure finance cost | Rs26.53 million (~Rs2.653 Cr) | REPORTED_ACTUAL | ARITHMETIC_INCONSISTENCY, CROSS_CHECK, UNIT_MILLION |
| MN40 | 130 | Lease-liability interest | Rs95 million (~Rs9.5 Cr — exceeds stated total of Rs27 million) | REPORTED_ACTUAL | ARITHMETIC_INCONSISTENCY, CROSS_CHECK, UNIT_MILLION, LIKELY_TRANSCRIPTION_ERROR (95 vs 9.5/0.95) |
| MN41 | 137 | Gold component of product mix | ~40% gold, rest diamond + making | REPORTED_ACTUAL | |
| MN42 | 145 | EBO breakeven, within Maharashtra | ~1st year (~12 months) | GUIDANCE | |
| MN43 | 145 | EBO breakeven, outside Maharashtra | 15–18 months | GUIDANCE | |
| MN44 | 145 | Store-opening plan clarified | 9 stores yr1 / 7 stores yr2 | GUIDANCE | RESOLVES_AMBIGUITY (vs MN23's unquantified "remaining") |
| MN45 | 145 | Dependency on parent PNGS | ~95% currently | REPORTED_ACTUAL | |
| MN46 | 145 | Dependency on PNGS, forward | expected to fall to 20–25% "in years to come" | GUIDANCE | |
| MN47 | 145 | EBO stock-turn target for significant PAT contribution | 1.25x–1.5x | GUIDANCE | |
| MN48 | 149 | Inventory-turn breakeven point | 0.75x (verbatim "75") | GUIDANCE | TRANSCRIPTION_AMBIGUITY |
| MN49 | 149 | Profit thresholds | reasonable profit at 1.25x; "super normal" beyond 1.3x | GUIDANCE | |
| MN50 | 153 | Reaffirms breakeven point (correction) | 0.75x | GUIDANCE (confirmation) | |
| MN51 | 162 | Lab-grown vs natural diamond price differential | 10–15% | OPINION / REPORTED | |
| MN52 | 162 | Share of Indian diamond-jewelry market that is <2 carat | ~95% | CONTEXT / OPINION | |
| MN53 | 162 | Share of PNGS Reva's own business in smaller diamonds | ~97% | REPORTED_ACTUAL | |
| MN54 | 170 | Inventory turn, current (restated) | 1.29x | REPORTED_ACTUAL (restated) | |
| MN55 | 170 | Inventory-turn guidance, FY27/28/29 | 1.1x–1.4x | GUIDANCE | |
| MN56 | 170 | Historical Q1 share of annual turnover | ~15% | REPORTED_ACTUAL / context | |
| MN57 | 185 | Volume growth (restated) | >50% | REPORTED_ACTUAL (restated) | |
| MN58 | 185 | Store plan restated | 9 stores yr1 (2 already opened) / 7 stores yr2 | GUIDANCE (restated) | |
| MN59 | 194 | Q1 share of annual turnover (restated) | ~15% | REPORTED_ACTUAL (restated) | |
| MN60 | 194 | H1/H2 seasonality split | ~35% H1 / ~65% H2 | GUIDANCE | |
| MN61 | 202 | EBO topline contribution target (restated) | 20–25% in 2–3 years | GUIDANCE (restated) | |
| MN62 | 202 | Stock-turn threshold to avoid PAT/EBITDA dent (restated) | >1.1x or 1.25x | GUIDANCE (restated) | |
| MN63 | 211 | AOV, last quarter (Q4FY26, per management) | Rs1,12,000 | REPORTED_ACTUAL (comparative) | AOV_FIGURE_DISCREPANCY — analyst's question (line 209) cited Rs1,29,000 "for March 26"; unreconciled |
| MN64 | 211 | AOV, this quarter (restated) | ~Rs1,00,000 | REPORTED_ACTUAL (restated) | |
| MN65 | 211 | AOV sequential dent | ~7–8% | REPORTED_ACTUAL (derived) | |
| MN66 | 215 | Brand ambassador signings as of call date | 0 — none signed, negotiations ongoing/unformalized | ZERO_STANDING | HEDGE |
| MN67 | 224 | EBOs opened so far | 3, of which 1 is >6 months old | REPORTED_ACTUAL | STORE_COUNT_DISCREPANCY vs MN22 ("2 operational" in opening remarks) |
| MN68 | 224 | EBO breakeven, Maharashtra (restated) | ~1 year | GUIDANCE (restated) | |
| MN69 | 224 | Outside-Maharashtra EBOs to open | in 2–3 months | GUIDANCE | |
| MN70 | 224 | EBO breakeven, outside Maharashtra (restated) | 15–18 months | GUIDANCE (restated) | |
| MN71 | 233 | Current PAT margin (restated) | 23–24% | REPORTED_ACTUAL (restated) | |
| MN72 | 233 | Full-year margin impact guidance | 200–300 bps | GUIDANCE | CROSS_CHECK — relationship to earlier 1–2%/2–3% dent language (MN25/MN28) not reconciled by management |
| MN73 | 233 | EBO operating period this fiscal year | most start April, average 4–5 months | REPORTED_ACTUAL / context | |
| MN74 | 241 | Short-term debt at FY26-end (WCDL for BTA settlement) | Rs166 Cr | REPORTED_ACTUAL | CROSS_CHECK |
| MN75 | 241 | Short-term debt outstanding currently | ~Rs120 Cr (implies ~Rs46 Cr repaid) | REPORTED_ACTUAL | CROSS_CHECK |
| MN76 | 78 | Gold loan facility utilization / MCX hedging | facility available but undrawn; no MCX/gold hedging undertaken (deliberate policy) | ZERO_STANDING | |

---

## 4. CROSS-CHECK PRIORITY LIST (for A3/A4/A5 against filing + investor deck)

1. **Inventory turn 1.29x** (MN1, MN54) — tie to FY26 closing turn and the 0.75x/1.25x/1.3x
   breakeven/profit bands (MN2, MN48–MN50) for the SOTP/stock-turn thesis.
2. **AOV discrepancy** — three figures in play: Rs1,00,000 (this quarter, MN3/MN64), Rs1,12,000
   ("last quarter" per management, MN63), Rs1,29,000 ("for March 26" per analyst, unconfirmed by
   management, Q27/MN63 flag AOV_FIGURE_DISCREPANCY). Needs reconciliation against the investor
   presentation before any AOV trend is asserted.
3. **Other income Rs5.6 Cr** (MN36) — prior-period comparator garbled in transcript ("30 tax");
   NOT_FOUND for the prior-period other income figure; cross-check against P&L.
4. **Finished-goods inventory change Rs30 Cr** (MN37) — bookkeeping line item flagged by two
   separate analysts as unusually large; management calls it "routine" without a comparative number.
5. **Finance-cost bifurcation arithmetic inconsistency** (MN38–MN40) — Rs27mn total does not equal
   Rs26.53mn + Rs95mn; Rs95mn alone exceeds the stated Rs27mn total. Carried forward from A1's
   header flag, confirmed present in the transcript verbatim; likely mis-transcribed decimal/unit
   (e.g., intended Rs9.5mn or Rs0.95mn lease interest). Do not resolve — flag to A3/A5 for the filing
   tie-out.
6. **Trade payable Rs30 Cr → Rs20 Cr** (Q24) — management's qualitative explanation (payment-cycle
   timing) has no independent numeric confirmation; needs balance-sheet cross-check.
7. **Short-term debt Rs166 Cr → ~Rs120 Cr** (MN74–MN75) — WCDL for BTA settlement; cross-check
   against balance sheet / borrowings note.
8. **EBITDA margin 28.76% vs 29%** (MN11 vs MN29) — same quarter, two slightly different
   restatements by the same speaker minutes apart.
9. **Store count discrepancy** — opening remarks state 2 of the 15 planned Coco stores are already
   operational (MN22); Turn 11 answer states 3 EBOs have been opened, one >6 months old (MN67). Not
   necessarily contradictory (different counting basis — "IPO-funded new stores" vs "all EBOs
   including pre-IPO") but unreconciled in the transcript; flag for filing cross-check.

---

## 5. OTHER FLAGS

- **MGMT_ABSENCE**: CEO Amit Modak is present and speaks in the opening remarks only (line 46),
  explicitly citing illness (fever, throat) and handing the entire Q&A session (all 12 turns) to the
  Non-executive Director. On a quarter with 100%+ YoY growth being discussed, the CMD/CEO fields zero
  analyst questions.
- **DEFERRED_ANSWER**: the finance-cost bifurcation question (Q9, Turn3, line105) is deliberately
  deferred mid－turn ("can we just move to next question... my team is extracting that") and answered
  three turns later via an out-of-band "management follow-up" (T41, line 130) rather than when the
  next question would naturally resume with Harsha.
- **REPEAT_QUESTION**: Q7 (Harsha, SSG confirmation) repeats ground already covered by Q6 (Kushi
  Jain, SSG split); Q17/Q19 (Harsha, Turn7) re-tread the inventory-turn/EBO-margin ground opened by
  Q14–Q16 (Ankit Gupta, Turn6).
- **INTERRUPTED_QUESTION**: Q20 (Harsha, Turn7, line172) is cut off by an operator interrupt for
  queue management before the question is even stated; Harsha is requeued and returns in Turn10.
- **ZERO_STANDING** (3 instances, never dropped): EBO/Coco same-store-growth = nil this quarter
  (MN34); brand ambassador signings = 0 as of call date (MN66); gold loan facility undrawn / no MCX
  hedging (MN76).
- **CONTRADICTORY_STATEMENT**: line 137 states "there is no ... investment buying which happens in
  our case" immediately followed by "obviously there is a investment buying but the component is
  lower" — internally contradictory as transcribed; flag for A3 lexicon review, do not resolve.

---

## 6. NOT APPLICABLE FOR THIS DOCTYPE

- Numbered notes: n/a (concall transcript, no notes section).
- Investor-presentation slides: n/a (this extract is the transcript only; no deck was supplied
  alongside it for this run — see PRIOR_LEDGER_PATH note below).
- Results-filing categories (line items, agenda items, auditor paragraphs, entity list): n/a for
  doctype=concall.

Prior-quarter ledger path: not supplied for this run — no prior-quarter turn/question/mgmt-number
diff performed. `DROPPED_SLIDE`/`ENTITY_CHANGE`-style comparisons deferred to when a prior ledger is
available.

```yaml
stage: A2-enumerator
company: "PNGSREVA"
quarter: "Q1FY27"
doctype: "concall"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/pngs-q1fy27/work/ledger_concall_pngs_q1fy27.md"
counts:
  notes: 0
  line_items: 0
  zero_standing: 3
  agenda_items: 0
  auditor_paras: 0
  entities: 0
  turns: 103
  questions: 35
  mgmt_numbers: 76
  slides: 0
  slide_numbers: 0
flags_raised: [MGMT_ABSENCE, DEFERRED_ANSWER, REPEAT_QUESTION, INTERRUPTED_QUESTION, ZERO_STANDING, ARITHMETIC_INCONSISTENCY, CROSS_CHECK, AOV_FIGURE_DISCREPANCY, STORE_COUNT_DISCREPANCY, ANALYST_STATED_MGMT_CONFIRMED, TRANSCRIPTION_AMBIGUITY, HEDGE, CONTRADICTORY_STATEMENT, RESOLVES_AMBIGUITY]
gate_a2: pass
mismatch_note: ""
```
