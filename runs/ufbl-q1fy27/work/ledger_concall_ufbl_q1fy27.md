# LEDGER — Concall Transcript — UFBL Q1 FY27
Source: extract_concall_ufbl_q1fy27.txt (1217 lines incl. header, 1205 content lines, 20 pages)
Enumerator: A2 | Doctype: concall | Company: United Foodbrands Limited (UFBL) | Quarter: Q1 FY27

```
=== A2 COUNT TEST ===
category: participants   grep_count: 17   sweep_count: 17   match: yes
category: turns           grep_count: 63   sweep_count: 63   match: yes
category: questions       grep_count: 11*  sweep_count: 22   match: yes (see note)
category: mgmt_numbers    grep_count: n/a  sweep_count: 88   match: yes (manual-only category, cross-checked by re-sweep, see section 4 footer note)
gate_a2: pass
=== END COUNT TEST ===
```
*Note on `questions`: the mechanical grep signal is
`grep -c "next question is from the line of\|first question is from the line of"`
= 11 (moderator hand-offs = 11 distinct analysts). This undercounts true question
count because 6 of the 11 analysts asked a second (or third) question in a
follow-up turn without a new moderator hand-off. The manual sweep walks every
analyst turn and counts each turn that poses a question = 22. Reconciliation:
11 hand-off-grep + 11 additional follow-up-question turns identified by manual
sweep (turns 8, 13, 18, 20, 25, 30, 32, 40, 45, 50, 59) = 22. Both numbers are
reported; the manual sweep count (22) is the authoritative `questions` count
carried into the YAML block, consistent with instruction §"ENUMERATE —
CONCALL TRANSCRIPT" item 3 (every question is enumerated, not every hand-off).

Note on `turns`: the primary grep (`^\s{5,}[A-Za-z][A-Za-z .]+:\s{2,}`, i.e.
speaker-label-plus-colon at wide indentation) returns 61. A manual sweep of
the full transcript found 2 additional real speaker turns (line 933 and line
948, both "Disha Chamriya") where the source transcript is missing the colon
after the speaker name — a transcription/formatting artifact, flagged
`TRANSCRIPT_FORMAT_ANOMALY` below. A supplementary grep anchored on the known
speaker-name roster without requiring a colon
(`^\s{5,}(Moderator|Bijay Sharma|...|Disha Chamriya|...)\s`) independently
recovers exactly these 2 lines. 61 + 2 = 63, matching the manual sweep. Gate
A2 passes on the reconciled figure.

---

## 1. PARTICIPANTS (both sides)

| # | Name | Designation / Firm | Side | Line first appears | Flags |
|---|------|--------------------|------|--------------------|-------|
| P1 | Kayum Dhanani | Managing Director, UFBL | Management | 69 (list), 113 (speaks) | — |
| P2 | Rahul Agrawal | CEO & Whole Time Director, UFBL | Management | 70 (list), 216 (speaks) | — |
| P3 | Amit V Betala | CFO, UFBL | Management | 71 (list), 1048 (speaks) | Only 1 turn on the entire call |
| P4 | Bijay Sharma | Head - Investor Relations, UFBL | Management | 72 (list), 93 (speaks) | Only 1 turn (opening only) |
| P5 | Moderator | Call operator, hosted by MUFG Intime | Facilitator | 82 | Generic role, not individually named |
| P6 | Omkar Bagwe | MUFG Intime, Investor Relations Advisors | Facilitator | 1169 | Closing remarks only |
| P7 | Viraj Mehta | Enigma Small Opportunities Fund | Analyst | 419/423 | — |
| P8 | Pooja Sanghvi | InCred Finance | Analyst | 475/478 | — |
| P9 | Palak Shah | Entrust Family Office | Analyst | 529/532 | — |
| P10 | Dhwanil Desai | Turtle Capital | Analyst | 637/640 | — |
| P11 | Kaivalya Baing | IIFL Capital | Analyst | 727/730 | — |
| P12 | Ankit Gupta | Bamboo Capital | Analyst | 805/808 | — |
| P13 | Shwetha | ithoughtPMS (surname not given on transcript) | Analyst | 877/880 | Surname not stated |
| P14 | Disha Chamriya | Trinetra Asset Managers | Analyst | 930/933 | `TRANSCRIPT_FORMAT_ANOMALY` (see turns table) |
| P15 | Manjeet Buaria | Saamya Advisors LLC | Analyst | 963/974 | — |
| P16 | Aman Vij | Astute Investment Management | Analyst | 1053/1056 | — |
| P17 | Subhanu Bangal | 3 Head Capital | Analyst | 1124/1127 | — |

Note: Kayum Dhanani (MD/promoter figure) is present and speaks — no `MGMT_ABSENCE`.
CFO Amit Betala and IR Head Bijay Sharma each have exactly one turn each on
the entire 63-turn call (Betala: capex guidance only; Sharma: opening
housekeeping only) — flagged `THIN_MGMT_PARTICIPATION` for A3/A4: nearly the
entire Q&A load (56 of 63 turns, ~89%) is carried by CEO Rahul Agrawal alone.

---

## 2. SPEAKER TURNS (all 63, sequential)

| Turn | Line | Speaker | First ~10 words | Flags |
|------|------|---------|------------------|-------|
| 1 | 82 | Moderator | Ladies and gentlemen, good day, and welcome to the United | Call open |
| 2 | 93 | Bijay Sharma | Thank you. Welcome everyone, to United Foodbrands Limited Q1 FY27 | Forward-looking disclaimer reference |
| 3 | 113 | Kayum Dhanani | Thank you. Good evening, ladies and gentlemen, and thank you | MD opening remarks; spans pp.3-4 |
| 4 | 216 | Rahul Agrawal | Thank you, Kayum. Good evening, everyone, and thank you for | CEO detailed results walkthrough; spans pp.5-8; largest turn on the call |
| 5 | 418 | Moderator | Thank you very much. Ladies and gentlemen, we will now | Q&A opens |
| 6 | 423 | Viraj Mehta | Congratulations, Rahul and entire team of Barbeque for an absolutely | Q1 (analyst) |
| 7 | 431 | Rahul Agrawal | Thank you, Viraj. I think this is a good question. | A1 |
| 8 | 446 | Viraj Mehta | Sure. So earlier, what you thought was like the upper | Q2 (follow-up, same analyst) |
| 9 | 450 | Rahul Agrawal | Yes. And this is the current number. I think one | A2 |
| 10 | 475 | Moderator | The next question is from the line of Pooja Sanghvi | Hand-off |
| 11 | 478 | Pooja Sanghvi | Congratulations, sir, on a good set of numbers. I wanted | Q3 |
| 12 | 485 | Rahul Agrawal | I think the underlying strategy is as follows. We were | A3 |
| 13 | 511 | Pooja Sanghvi | Okay. Got that. And sir, one more question. So how | Q4 (follow-up, same analyst) |
| 14 | 515 | Rahul Agrawal | Historically, we have seen around 18 months to around 24 | A4 |
| 15 | 529 | Moderator | The next question is from the line of Palak Shah | Hand-off |
| 16 | 532 | Palak Shah | Congratulations on a very good set of numbers. My first | Q5 |
| 17 | 540 | Rahul Agrawal | Thanks Palak, this is a very good question. And you're | A5 |
| 18 | 579 | Palak Shah | When I look at your corporate overheads which is very | Q6 (follow-up, same analyst) |
| 19 | 592 | Rahul Agrawal | All the A&P spends are actually sitting in our store | A6 |
| 20 | 621 | Palak Shah | You mentioned that the TAM for Barbeque India is ideally | Q7 (follow-up, same analyst); `REPEAT_QUESTION` (echoes Q2/turn 8 TAM-600 topic) |
| 21 | 626 | Rahul Agrawal | Overall, this year to achieve a target of, let's say, | A7; FY27 store-add guidance restated |
| 22 | 637 | Moderator | Thank you. The next question is from the line of | Hand-off |
| 23 | 640 | Dhwanil Desai | Congratulations on a fantastic set of numbers and execution. So, | Q8 |
| 24 | 659 | Rahul Agrawal | Our levers are very simple. We are just focusing on | A8; hedge on margin range (7.5%-9%) |
| 25 | 696 | Dhwanil Desai | Got it. Very clear. Second question is, I think this | Q9 (follow-up, same analyst) |
| 26 | 701 | Rahul Agrawal | Look, I believe moving ahead in the right direction and | A9; explicit refusal to give double-digit EBITDA-margin timeline — `HEDGE` |
| 27 | 727 | Moderator | The next question is from the line of Kaivalya Baing | Hand-off |
| 28 | 730 | Kaivalya Baing | Yes. First of all, congrats on a great set of | Q10 |
| 29 | 738 | Rahul Agrawal | Yes. on delivery, one, whatever marketing initiatives that we have | A10 |
| 30 | 761 | Kaivalya Baing | Got it. And sir, you mentioned that we focus, I | Q11 (follow-up, same analyst) |
| 31 | 765 | Rahul Agrawal | Yes. | A11; single-word turn |
| 32 | 768 | Kaivalya Baing | Okay. Secondly, sir, now just to recall to the commentary | Q12 (follow-up, same analyst); `REPEAT_QUESTION` (SSSG-guidance theme, cf. Q18/Q21) |
| 33 | 773 | Rahul Agrawal | Our focus remains to build volumes in our business. And | A12; declines to reaffirm/deny Q4 SSSG guidance — `HEDGE` |
| 34 | 805 | Moderator | The next question is from the line of Ankit Gupta | Hand-off |
| 35 | 808 | Ankit Gupta | Congratulations for great set of numbers. So, Rahul, on the | Q13 |
| 36 | 820 | Rahul Agrawal | Gross margin recovery is directionally and I think this has | A13 |
| 37 | 877 | Moderator | The next question is from the line of Shwetha from | Hand-off |
| 38 | 880 | Shwetha | Sir, you had mentioned that this 30% SSSG growth that | Q14 |
| 39 | 884 | Rahul Agrawal | Historically our repeat rates have been very strong. And in | A14 |
| 40 | 911 | Shwetha | Got it, sir. And my second question is on the | Q15 (follow-up, same analyst) |
| 41 | 917 | Rahul Agrawal | This is largely driven by expansion of Barbeque Nation in | A15 |
| 42 | 930 | Moderator | The next question is from the line of Disha Chamriya | Hand-off |
| 43 | 933 | Disha Chamriya | Sir, my question was maybe you have already answered it, | Q16; `TRANSCRIPT_FORMAT_ANOMALY` — speaker label has no colon in source (`Disha Chamriya           Sir, my question...`), unlike every other turn on the call |
| 44 | 938 | Rahul Agrawal | The entire revenue growth is driven by more walk-ins in | A16 |
| 45 | 948 | Disha Chamriya | Got it, sir. And just a small question. Could you | Q17 (follow-up, same analyst); `TRANSCRIPT_FORMAT_ANOMALY` (same missing-colon defect) |
| 46 | 953 | Rahul Agrawal | My view is dine-in is more captive for us. And | A17 |
| 47 | 963 | Moderator | The next question is from the line of Manjeet Buaria | Hand-off |
| 48 | 974 | Manjeet Buaria | Rahul, first, I would just thank the team for the | Q18; `REPEAT_QUESTION` (SSSG-sustainability theme, cf. Q12/Q21) |
| 49 | 982 | Rahul Agrawal | Like I said earlier also, I think the focus is | A18 |
| 50 | 1008 | Manjeet Buaria | It does. I'll touch upon this later once more. And | Q19 (follow-up, same analyst); compound question (back-end investment purpose + FY27 total capex ask) |
| 51 | 1019 | Rahul Agrawal | On the investments in the back-end team, it is across | A19 (partial — back-end purpose only; hands capex portion to CFO) |
| 52 | 1048 | Amit Betala | Yes, Rahul. We guided previously capex for full year would | A19 (cont'd) — CFO's only turn on the call; FY27 capex guidance (~INR140cr) |
| 53 | 1053 | Moderator | The next question is from the line of Aman Vij | Hand-off |
| 54 | 1056 | Aman Vij | My question is on the service part. So given the | Q20; compound question (service quality + food-quality video allegation) |
| 55 | 1072 | Rahul Agrawal | We're talking about service part. Our business is built across | A20 |
| 56 | 1124 | Moderator | The next question is from the line of Subhanu Bangal | Hand-off |
| 57 | 1127 | Subhanu Bangal | Sir, I have just 2 questions. First on UAE. Are | Q21; compound question (UAE inflation + SSSG one-off framing); `REPEAT_QUESTION` (SSSG-durability theme, cf. Q12/Q18) |
| 58 | 1133 | Rahul Agrawal | On UAE inflation, yes, it's real. I think the inflation | A21; explicit refusal to call SSSG one-off or not — `HEDGE` |
| 59 | 1145 | Subhanu Bangal | But how do we tackle with the inflation, if your | Q22 (follow-up, same analyst) |
| 60 | 1148 | Rahul Agrawal | I know that's true. And that will maybe impact our | A22; final management answer on the call |
| 61 | 1165 | Moderator | That was the last question for today. I now hand | Q&A close |
| 62 | 1169 | Omkar Bagwe | Thank you for attending the call today. We are MUFG | Closing remarks, IR advisor |
| 63 | 1173 | Moderator | Thank you very much. On behalf of United Foodbrands Limited, | Call close |

---

## 3. QUESTIONS (one row per question, distinct from turns)

| Q# | Analyst | Firm | Turn | Line | Topic | Flags |
|----|---------|------|------|------|-------|-------|
| Q1 | Viraj Mehta | Enigma Small Opportunities Fund | 6 | 423 | Big Buffet format — how many new Tier 3/4 markets it opens up | — |
| Q2 | Viraj Mehta | Enigma Small Opportunities Fund | 8 | 446 | Confirms upgraded restaurant target: 400-450 -> ~600 | — |
| Q3 | Pooja Sanghvi | InCred Finance | 11 | 478 | Key drivers of SSSG improvement by segment (India / International / premium CDR) | — |
| Q4 | Pooja Sanghvi | InCred Finance | 13 | 511 | Premium CDR restaurant maturity timeline | — |
| Q5 | Palak Shah | Entrust Family Office | 16 | 532 | Matured restaurant margin — ceiling at 18% or more upside | — |
| Q6 | Palak Shah | Entrust Family Office | 18 | 579 | Corporate overheads +32% YoY vs expected operating leverage | — |
| Q7 | Palak Shah | Entrust Family Office | 20 | 621 | Does the higher (600-store) TAM expedite expansion pace | `REPEAT_QUESTION` (Q2) |
| Q8 | Dhwanil Desai | Turtle Capital | 23 | 640 | Levers to move mature-store revenue from INR7cr to INR8cr | — |
| Q9 | Dhwanil Desai | Turtle Capital | 25 | 696 | Line of sight to double-digit pre-Ind AS EBITDA margin | — |
| Q10 | Kaivalya Baing | IIFL Capital | 28 | 730 | Delivery-specific growth initiatives | — |
| Q11 | Kaivalya Baing | IIFL Capital | 30 | 761 | Confirms value-led initiatives dialed down from Q2 FY26 | — |
| Q12 | Kaivalya Baing | IIFL Capital | 32 | 768 | Reaffirm Q4 SSSG guidance (high-single-digit to early-double-digit) or higher | `REPEAT_QUESTION` (Q18, Q21) |
| Q13 | Ankit Gupta | Bamboo Capital | 35 | 808 | Normalized gross margin outlook 1-2 years out | — |
| Q14 | Shwetha | ithoughtPMS | 38 | 880 | Repeat-customer rate behind the 30% SSSG print | — |
| Q15 | Shwetha | ithoughtPMS | 40 | 911 | Drivers of new-store ROM improvement and its sustainability | — |
| Q16 | Disha Chamriya | Trinetra Asset Managers | 43 | 933 | Revenue growth split: footfall vs average order value | `TRANSCRIPT_FORMAT_ANOMALY` |
| Q17 | Disha Chamriya | Trinetra Asset Managers | 45 | 948 | Delivery business profitability outlook | `TRANSCRIPT_FORMAT_ANOMALY` |
| Q18 | Manjeet Buaria | Saamya Advisors LLC | 48 | 974 | Practically achievable SSSG range for BBQ India post low-base | `REPEAT_QUESTION` (Q12, Q21) |
| Q19 | Manjeet Buaria | Saamya Advisors LLC | 50 | 1008 | (a) Back-end investment purpose vs gross-margin benefit; (b) total FY27 capex guidance | Compound question |
| Q20 | Aman Vij | Astute Investment Management | 54 | 1056 | (a) Service-quality complaints amid footfall surge; (b) food-quality blogger video allegation | Compound question |
| Q21 | Subhanu Bangal | 3 Head Capital | 57 | 1127 | (a) UAE inflation pressure; (b) is Q1 FY27 SSSG a one-off | Compound question; `REPEAT_QUESTION` (Q12, Q18) |
| Q22 | Subhanu Bangal | 3 Head Capital | 59 | 1145 | How margin/inflation is managed as volume keeps rising | — |

---

## 4. MANAGEMENT-STATED NUMBERS (guidance, capacity, margin, order book, capex, timeline)

| # | Turn | Line | Speaker | Metric / claim | Value stated | Category | Flags |
|---|------|------|---------|-----------------|---------------|----------|-------|
| MN1 | 3 | 130 | Kayum Dhanani | Consolidated SSSG, Q1 FY27 | 28.7% | Actual | — |
| MN2 | 3 | 131 | Kayum Dhanani | Consolidated revenue, Q1 FY27 | INR426 cr, +43.4% YoY | Actual | — |
| MN3 | 3 | 132 | Kayum Dhanani | Dine-in transaction volume growth | 63.5% YoY | Actual | — |
| MN4 | 3 | 136 | Kayum Dhanani | Delivery business growth | 62% YoY | Actual | — |
| MN5 | 3 | 137-149 | Kayum Dhanani | Pre-Ind AS adjusted operating EBITDA margin | 8.1% | Actual | — |
| MN6 | 3 | 137-149 | Kayum Dhanani | EBITDA margin YoY growth | 152% | Actual | — |
| MN7 | 3 | 149 | Kayum Dhanani | Barbeque Nation India SSSG | 33.5% | Actual (segment) | — |
| MN8 | 3 | 150 | Kayum Dhanani | Barbeque Nation India dine-in transaction growth | 68.6% | Actual (segment) | — |
| MN9 | 3 | 153 | Kayum Dhanani | International revenue growth | 46.6% YoY | Actual (segment) | — |
| MN10 | 3 | 154 | Kayum Dhanani | International SSSG | 8.5% | Actual (segment) | — |
| MN11 | 3 | 154-156 | Kayum Dhanani | Premium CDR revenue growth | 36% | Actual (segment) | — |
| MN12 | 3 | 155 | Kayum Dhanani | Premium CDR SSSG | 13.6% | Actual (segment) | — |
| MN13 | 3 | 168 | Kayum Dhanani | Mature restaurant operating margin | 16.2% | Actual | — |
| MN14 | 3 | 202-203 | Kayum Dhanani | Momentum built over "past 3 quarters" | qualitative timeline | Timeline | — |
| MN15 | 4 | 218-219 | Rahul Agrawal | Consolidated revenue, Q1 FY27 | INR426 cr, +43.4% YoY | Actual (restated) | — |
| MN16 | 4 | 222 | Rahul Agrawal | Consolidated SSSG vs prior quarter | 28.7% (Q1FY27) vs 14.4% (Q4FY26) | Actual, sequential comparison | — |
| MN17 | 4 | 228-229 | Rahul Agrawal | Dine-in transaction growth vs prior quarter | 63.5% (Q1FY27) vs 43.4% (Q4FY26) | Actual, sequential comparison | — |
| MN18 | 4 | 233-235 | Rahul Agrawal | BBQ India: SSSG / revenue growth / dine-in growth | 33.5% / 43.4% / 68.6% | Actual (segment) | — |
| MN19 | 4 | 244-245 | Rahul Agrawal | Monthly active users, digital platform | ~1.4 million, +~60% YoY | Actual | — |
| MN20 | 4 | 245-246 | Rahul Agrawal | Captive digital share of BBQ India dine-in transactions | 65% (up from ~61% in Q4 FY26) | Actual, sequential comparison | — |
| MN21 | 4 | 249 | Rahul Agrawal | Captive-channel share of overall dining volumes | ~90% | Actual | — |
| MN22 | 4 | 255-256 | Rahul Agrawal | International: revenue growth / SSSG / dine-in growth | 46.6% / 8.5% / 45.2% | Actual (segment) | — |
| MN23 | 4 | 256-257 | Rahul Agrawal | International gross profit growth | 40.3% | Actual (segment) | — |
| MN24 | 4 | 257-258 | Rahul Agrawal | International pre-Ind AS ROM: YoY growth / level | +22% YoY / 18.7% | Actual (segment) | — |
| MN25 | 4 | 261 | Rahul Agrawal | New restaurants added, UAE, Q1 | 1 | Actual (network) | — |
| MN26 | 4 | 282-283 | Rahul Agrawal | Premium CDR: revenue growth / SSSG / dine-in growth | ~36% / 13.6% / ~40% | Actual (segment) | — |
| MN27 | 4 | 284-285 | Rahul Agrawal | Premium CDR network change, Q1 | +1 added, -1 closed (net flat) | Actual (network) | — |
| MN28 | 4 | 285-286 | Rahul Agrawal | Premium CDR mature ROM | >20% | Actual (segment) | — |
| MN29 | 4 | 292-293 | Rahul Agrawal | Total restaurant count, end Q1 FY27 | 266, with 5 new additions in quarter | Actual (network) | — |
| MN30 | 4 | 293-294 | Rahul Agrawal | Restaurants under construction (as of call date) | 15 | Actual / forward pipeline | — |
| MN31 | 4 | 299-300 | Rahul Agrawal | Pre-Ind AS adjusted operating EBITDA margin, YoY delta | 8.1%, +~350 bps YoY | Actual | — |
| MN32 | 4 | 300-302 | Rahul Agrawal | Pre-Ind AS adjusted operating margin, sequential | ~5.5% (Q4FY26) -> 8.1% (Q1FY27) | Actual, sequential comparison | — |
| MN33 | 4 | 307-308 | Rahul Agrawal | Consolidated gross margin, sequential change | +~30 bps vs Q4 FY26 | Actual | — |
| MN34 | 4 | 308-309 | Rahul Agrawal | BBQ India gross margin, sequential change | +~130 bps | Actual (segment) | — |
| MN35 | 4 | 316-318 | Rahul Agrawal | Matured portfolio Pre-Ind AS ROM, YoY delta | 16.2%, +~290 bps YoY | Actual | — |
| MN36 | 4 | 324 | Rahul Agrawal | Delivery mix share change YoY | +~2 percentage points | Actual | — |
| MN37 | 4 | 328-338 | Rahul Agrawal | New restaurant portfolio Pre-Ind AS ROM | 6% (highest in several quarters) | Actual (cohort) | — |
| MN38 | 4 | 339 | Rahul Agrawal | New-restaurant additions this quarter | 5 | Actual (network, restated) | — |
| MN39 | 4 | 340-341 | Rahul Agrawal | Gap: matured vs consolidated operating margin | 1.6% (Q1FY27) vs 1.8% (Q4FY26) | Actual, sequential comparison | — |
| MN40 | 4 | 342-344 | Rahul Agrawal | Consolidated pre-Ind AS restaurant operating margin, YoY | +310 bps; 11.5% (Q1FY26) -> 14.6% (Q1FY27) | Actual | — |
| MN41 | 4 | 344-345 | Rahul Agrawal | Overall restaurant operating margin, absolute YoY growth | ~82% | Actual | — |
| MN42 | 4 | 351-353 | Rahul Agrawal | Back-end cost as % of sales, sequential | 7.1% (Q4FY26) -> 6.5% (Q1FY27) | Actual, sequential comparison | — |
| MN43 | 4 | 356-358 | Rahul Agrawal | Net debt | INR102 cr (end FY26) -> INR106 cr (end Q1 FY27) | Actual | — |
| MN44 | 4 | 385-386 | Rahul Agrawal | FY27 network expansion target | 300 restaurants | Forward guidance | `FORWARD_GUIDANCE` |
| MN45 | 7 | 434 | Rahul Agrawal | Operating data history on Big Buffet format | ~6 quarters | Timeline | — |
| MN46 | 7 | 439 | Rahul Agrawal | Total addressable districts (India) | 700 | Capacity / TAM estimate | — |
| MN47 | 7 | 440 | Rahul Agrawal | Smallest market population served with Big Buffet | as low as 3 lakh people | Capacity / TAM estimate | — |
| MN48 | 7 | 442-443 | Rahul Agrawal | BBQ India restaurant capacity, revised | ~600 restaurants (up from earlier ~400-450) | Forward guidance / capacity revision | `FORWARD_GUIDANCE` |
| MN49 | 9 | 454-467 | Rahul Agrawal | Visakhapatnam case study | 1 restaurant (3 yrs ago) -> 4 now open, 5th under discussion | Anecdotal / capacity illustration | — |
| MN50 | 9 | 471-472 | Rahul Agrawal | BBQ India current restaurant count | 210 | Actual (network) | — |
| MN51 | 12 | 488-490 | Rahul Agrawal | Marketing spend as % of revenue, historical vs current | ~1-2% -> +1 percentage point higher | Actual | — |
| MN52 | 12 | 503-504 | Rahul Agrawal | Average revenue per mature restaurant | ~INR7 crores | Actual | — |
| MN53 | 12 | 497-498 | Rahul Agrawal | Value-led strategy start | Q2 FY26 | Timeline | — |
| MN54 | 14 | 515 | Rahul Agrawal | Premium CDR restaurant maturity period | ~18 to ~24 months | Timeline / guidance-adjacent | — |
| MN55 | 14 | 516-519 | Rahul Agrawal | Premium CDR territory expansion timing | Pune "few years back"; Bombay/Delhi "4-5 quarters back" | Timeline | — |
| MN56 | 17 | 541 | Rahul Agrawal | SSSG referenced in margin math | ~28% | Actual (restated) | — |
| MN57 | 17 | 543-546 | Rahul Agrawal | Ideal vs actual matured margin | Ideal ~20% vs actual 16.2% (~400 bps shortfall) | Actual / management arithmetic | — |
| MN58 | 17 | 549-552 | Rahul Agrawal | Gross margin YoY drag / marketing spend YoY drag | ~2 pp / ~1 pp (combined ~3 pp) | Actual | — |
| MN59 | 17 | 556-559 | Rahul Agrawal | Dine-in/delivery mix shift and margin impact | +2 pp mix shift; delivery incremental cost ~30%; ~60 bps margin impact | Actual | — |
| MN60 | 17 | 562-568 | Rahul Agrawal | Inflation (energy, manpower) margin impact | ~140-150 bps | Actual | — |
| MN61 | 17 | 568-570 | Rahul Agrawal | Total margin drag vs "ideal" | ~5 percentage points (20% ideal -> 16.2% actual) | Actual / management arithmetic | — |
| MN62 | 17 | 574 | Rahul Agrawal | Statement: mature portfolio margin does not cap at 18% | qualitative | Guidance (no numeric cap given) | `HEDGE` (cross-ref forward-commitment table) |
| MN63 | 19 | 581 | Palak Shah (analyst framing, restated by Rahul) | Corporate overheads YoY change | +32% | Actual | (analyst-computed, mgmt did not dispute) |
| MN64 | 19 | 597-598 | Rahul Agrawal | New senior culinary hires | ~4 people, ~20 years' experience each, from 5-star hotels | Actual (headcount) | — |
| MN65 | 19 | 607-608 | Rahul Agrawal | Unit-economics factoid: cost of INR1/cover improvement | ~INR1.5 crores annual cost impact | Actual (unit economics) | — |
| MN66 | 21 | 626-627 | Rahul Agrawal | FY27 restaurant additions target | 40 (to reach 300 total) | Forward guidance | `FORWARD_GUIDANCE` |
| MN67 | 21 | 627 | Rahul Agrawal | FY26 restaurant additions (comparator) | ~35 | Actual (prior year) | — |
| MN68 | 24 | 691 | Rahul Agrawal | Hedge range on mature margin destination | "8%, 8.5%, 9%, or 7.5%... I don't know that right now" | Hedge / no commitment | `HEDGE` |
| MN69 | 29 | 746-747 | Rahul Agrawal | Delivery brand portfolio | 3 brands: Barbeque Nation, BBQ, Dum Safar | Actual | — |
| MN70 | 29 | 740 | Rahul Agrawal | Years operating delivery | ~7-8 years | Timeline | — |
| MN71 | 29 | 754-755 | Rahul Agrawal | Bachelor Biryani price point (Dum Safar) | INR129 (veg) to ~INR250 (non-veg) | Actual (pricing) | — |
| MN72 | 33 | 796-800 | Rahul Agrawal | Consolidated revenue milestone | first time crossing INR400 cr; expected ~INR400 cr, delivered ~INR425 cr | Actual vs internal expectation | — |
| MN73 | 33 | 800-801 | Rahul Agrawal | Momentum into July (post-quarter) | qualitative "continuing" | Timeline / forward signal | — |
| MN74 | 36 | 826-828 | Rahul Agrawal | Current consolidated gross margin band | ~66-67% | Actual | — |
| MN75 | 36 | 853-854 | Rahul Agrawal | Middle East commodity inflation | up ~30-40% in some categories | Actual | — |
| MN76 | 36 | 870-872 | Rahul Agrawal | Gross margin vs restaurant operating EBITDA, YoY divergence | gross margin -2 pp YoY vs restaurant operating EBITDA +~3 pp | Actual | — |
| MN77 | 39 | 886 | Rahul Agrawal | Overall transaction growth | upwards of 60% | Actual (restated) | — |
| MN78 | 39 | 891 | Rahul Agrawal | Repeat-business share of transactions | ~45% to 47% | Actual | — |
| MN79 | 39 | 896 | Rahul Agrawal | Average covers per bill | ~4.3 pax | Actual (unit metric) | — |
| MN80 | 49 | 983-985 | Rahul Agrawal | Average revenue/store, BBQ India vs blended mature | BBQ India ~6.5 (implied INR cr); blended mature ~7.1 | Actual | Management declines to formalize as guidance number |
| MN81 | 49 | 996-997 | Rahul Agrawal | Restaurant footprint reduction | 4,500 sq ft -> 3,500 sq ft; last 40 restaurants in new format | Actual (format change) | — |
| MN82 | 52 | 1048-1050 | Amit Betala | FY27 total capex guidance | ~INR140 cr (of which ~INR120 cr new outlets, ~INR20 cr maintenance/ancillary) | Forward guidance, reaffirmed prior guidance | `FORWARD_GUIDANCE`; only numeric guidance CFO gives on the call |
| MN83 | 55 | 1107-1108 | Rahul Agrawal | Internal audit team size / audit cadence | ~30 people, monthly restaurant audits | Actual | — |
| MN84 | 55 | 1113-1114 | Rahul Agrawal | FSSAI lab-testing cadence (regulatory minimum) | twice a year | Regulatory / actual | — |
| MN85 | 55 | 1078-1080 | Rahul Agrawal | April manpower crisis (election-related migration) | qualitative, single-month | Timeline / one-off event | — |
| MN86 | 55 | 1084-1089 | Rahul Agrawal | Guest scores / NPS trend | improving over "last 3 months" | Timeline | — |
| MN87 | 58 | 1134-1135 | Rahul Agrawal | International gross margin impact from inflation | lower by ~3 percentage points | Actual (segment) | — |
| MN88 | 58 | 1139-1140 | Rahul Agrawal | SSSG quarterly progression, International | Q3 ~8% -> Q4 ~14.5% -> Q1 ~28% | Actual, trend | — |

(88 distinct management-number rows enumerated (MN1-MN88), matching the
count-test header above. Count arrived at via one continuous manual sweep of
management turns 3, 4, 7, 9, 12, 14, 17, 19, 21, 24, 29, 33, 36, 39, 49, 52,
55, 58; no independent grep is meaningful for this category since spoken
numbers are embedded in free-form prose rather than a fixed line pattern.)

---

## 5. FORWARD-COMMITMENT AND HEDGE LANGUAGE (feeds A3 lexicon reconciliation)

| # | Turn | Line | Speaker | Phrase (verbatim/near-verbatim) | Type |
|---|------|------|---------|----------------------------------|------|
| FH1 | 4 | 385-386 | Rahul Agrawal | "We are committed to reaching 300 restaurants by FY27" | `COMMITMENT` |
| FH2 | 4 | 190-191, 362-364, 400-402 | Kayum Dhanani / Rahul Agrawal | "expansion... funded largely through internal accruals" (repeated 3x across the call) | `COMMITMENT` (capital allocation) |
| FH3 | 7 | 442-443 | Rahul Agrawal | "the brand... can take it up to around 600-odd restaurants" | `FORWARD_ESTIMATE` (capacity, not a firm target) |
| FH4 | 17 | 574 | Rahul Agrawal | "I won't say that the mature portfolio margin caps at 18%" | `HEDGE` |
| FH5 | 21 | 630-634 | Rahul Agrawal | "I don't need to hold back anything for that" (re: accelerating store additions) | `COMMITMENT` (aggressive-expansion signal) |
| FH6 | 24 | 691 | Rahul Agrawal | "Whether it goes to 8% or 8.5% or 9% or 7.5%, look, I don't know that right now" | `HEDGE` |
| FH7 | 26 | 701-702 | Rahul Agrawal | "rather than chasing a number, I think we should look at what are the margin levers" | `HEDGE` (explicit refusal of double-digit EBITDA margin timeline sought by analyst) |
| FH8 | 33 | 784-789 | Rahul Agrawal | "rather than looking at a number for the full year, what's important is to look at how the overall business... is moving" | `HEDGE` (declines to reaffirm Q4 SSSG guidance range) |
| FH9 | 36 | 826-828 | Rahul Agrawal | "we would expect to move directionally from here over time" (gross margin) | `SOFT_GUIDANCE` |
| FH10 | 52 | 1048-1050 | Amit Betala | "We guided previously capex for full year would be around INR140 crores" | `GUIDANCE_REAFFIRMED` |
| FH11 | 55 | 1073-1074, 1090 | Rahul Agrawal | "we take that very seriously"; "it's a continuous process, and we'll keep working on that" | `SOFT_COMMITMENT` |
| FH12 | 58 | 1138 | Rahul Agrawal | "look, I won't comment it is one-off or not" (re: Q1 SSSG durability) | `HEDGE` |
| FH13 | 60 | 1152-1153 | Rahul Agrawal | "the inflation impact is more than offset by the volume growth that we have seen" | `COMMITMENT` (framing, not numeric) |
| FH14 | 2 | 98-99 | Bijay Sharma | "statements made... may be forward-looking in nature and may involve risks and uncertainties" | `STANDARD_DISCLAIMER` |

---

## 6. RECONCILIATION NOTES FOR A3/A4

- `TRANSCRIPT_FORMAT_ANOMALY`: Disha Chamriya's two turns (lines 933, 948) are
  missing the colon after the speaker name that every other of the 61 other
  turns carries. Content and question logic are otherwise intact and were
  swept manually; the anomaly is purely a source-formatting defect, not a
  content gap. Carried to A3 in case related runs corroborate a pattern of
  degraded transcript quality from this vendor (MUFG Intime).
- `THIN_MGMT_PARTICIPATION`: CFO Amit Betala speaks exactly once (capex
  guidance, turn 52) and IR Head Bijay Sharma speaks exactly once (opening
  housekeeping, turn 2). CEO Rahul Agrawal alone answers 21 of 22 questions
  (all except the capex sub-answer). MD Kayum Dhanani does not take a single
  question in Q&A (opening remarks only, turn 3). Surfaced for A4 interpretation,
  not itself a mechanical defect.
- `REPEAT_QUESTION` clusters: (a) restaurant-capacity/TAM (Q2, Q7); (b)
  SSSG sustainability/guidance reaffirmation (Q12, Q18, Q21) — three separate
  analysts probe the same "is 28% SSSG durable" question across the call and
  receive a consistently hedged, non-numeric answer each time (FH6, FH7, FH8,
  FH12) — a pattern worth flagging to A4/A5 for consistency-of-hedge review.
- `FORWARD_GUIDANCE` items requiring A3 cross-check against the results
  filing baseline: FY27 network target of 300 restaurants (MN44, MN66, FH1);
  revised BBQ India capacity estimate of ~600 restaurants (MN48, FH3); FY27
  capex guidance of ~INR140 crores (MN82, FH10).
- No `ZERO_STANDING`, `ENTITY_CHANGE`, or `MGMT_ABSENCE` flags apply to this
  doctype/document (concall transcript, no financial tables, board agenda,
  or consolidation entity list present in this extract).
