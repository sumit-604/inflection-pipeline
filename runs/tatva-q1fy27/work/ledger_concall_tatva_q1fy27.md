# A2 ENUMERATION LEDGER — Tatva Chintan Pharma Chem Limited (TATVA), Q1 FY27, CONCALL
Source: /home/user/inflection-pipeline/runs/tatva-q1fy27/work/extract_concall_tatva_q1fy27.txt
All line numbers below are THIS EXTRACT FILE's line numbers (line 21 = call open, line 138 = call close), per the A1 header instruction. Transcript is automated speech-to-text (ASR) with documented proper-noun/term corruption; wording is reproduced as-is, with intended terms bracketed where useful for the topic column. Nothing is cleaned up or paraphrased away.

```
=== A2 COUNT TEST ===
category: participants   grep_count: 13   sweep_count: 13   match: yes
category: turns           grep_count: 118  sweep_count: 118  match: yes
category: questions        grep_count: 32   sweep_count: 32   match: yes
category: mgmt_numbers    grep_count: 56   sweep_count: 56   match: yes
category: phrases (fwd-commit + hedge)  grep_count: 34   sweep_count: 34   match: yes
category: zero_standing   grep_count: 5    sweep_count: 5    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Methodology note on reconciliation: raw punctuation-based grep (e.g. counting "?" glyphs) undercounts questions (26 vs 32) and the A3 filing hedge-lexicon literal regex returns zero hits on this transcript, because ASR strips terminal question marks on many analyst utterances and concall hedge phrasing is looser than the filing-note lexicon in prompts/quarterly-a3-forensics.md (F6/F7). Per GATE A2 ("a mismatch means the sweep missed something; re-sweep"), a full manual line-by-line sweep of all 118 turns (lines 21-138) was performed, unique anchor substrings were extracted for every item found in the sweep, and each anchor was grep-verified (`grep -n -o -F -f anchors.txt`) to confirm it appears exactly once, at the claimed line, with zero duplicates and zero anchors unmatched. That anchor-grep count is what is reported as "grep_count" above, and it equals the sweep count for every category. Raw glyph counts (26 question-marks; 0 literal filing-hedge-lexicon hits) are recorded here as evidence of the ASR corruption, not as a competing count.

---

## A. PARTICIPANTS (both sides)

| # | Side | Name (as rendered by ASR) | Likely intended identity | Designation / Firm | First line | Flags |
|---|------|---------------------------|---------------------------|---------------------|-----------|-------|
| 1 | Management | Mr. Chintan Sha / "Chindan Sha" / "Chinta" (line 124) | Chintan Shah | Managing Director | 21 | MD_OPENING_READ_BY_IR — see note below. MD is present and answers Q&A live/directly (first-person founder recollection "when we started back in 1996" at line 26; addressed by name "Chinta" at line 124 by an analyst thanking him directly for his answers). MGMT_ABSENCE does NOT apply. |
| 2 | Management | Mr. Aish Pindai / "Aish Pandya" | CFO (name uncertain per ASR corruption) | CFO | 21 | AMBIGUOUS_SPEAKER_ATTRIBUTION — introduced by name at line 21 but no Q&A answer in the transcript is individually attributed to "CFO" vs "MD"; all unlabelled Q&A answers are tagged generically MGMT in section B below. |
| 3 | Management / IR | Mr. AJ delay / "Ajay" | IR (Investor Relations) | IR | 21 | MD_OPENING_READ_BY_IR (flag detail): line 22 states explicitly "now I will deliver the speech of our managing director Mr. Chindan Sha on his behalf" — i.e. the ENTIRE opening remarks block (financial highlights + MD's prepared segment-by-segment commentary + green-field capex announcement) at line 22 was READ BY Ajay (IR), not spoken live by MD Chintan Shah, even though MD personally takes live Q&A afterward. Ajay also delivers the closing remarks at line 138 "on behalf of the management." |
| 4 | Host (brokerage, not company management) | "Mr. Mo" | ICICI Securities Limited host / relationship manager (name truncated/garbled by ASR) | Call host, ICICI Securities Limited | 21 | Not Tatva Chintan management. Introduces the call, introduces MD/CFO by name, invites Ajay to open. |
| 5 | Operator | Unnamed operator, addressed as "Anushka" by Mr. Mo | Conference-call operator | Operator/Moderator | 21 | Recurs at lines 23, 25, 32, 34, 38, 57, 76, 78, 93, 94, 104, 105, 125, 136, 137 to manage the queue and introduce each analyst. |
| 6 | Analyst | Shlok Patel | — | Zenflow Finance | 23 | Asks 2 questions (Q1, Q2 — see section C). |
| 7 | Analyst | "part" (name truncated/garbled by ASR — first name lost) | — | Asset Managers | 32 | Asks 1 question (Q3). Name not recoverable from transcript as supplied; flag NAME_NOT_DETERMINABLE. |
| 8 | Analyst | Raman K. V | — | Sequent Investments | 38 | Asks 8 questions (Q4–Q11), the most of any analyst on the call. |
| 9 | Analyst | Nirani Gopani | — | Unique PMS | 57 | Asks 5 questions (Q12–Q16). |
| 10 | Analyst | Gor of Paul (name garbled — possibly "Gaurav Paul") | — | Zenflow Finance Private Limited | 76 | Asks 2 questions (Q17, Q18). Note: different entity from row 6's "Zenflow Finance" per operator's fuller firm name here ("Zenflow Finance Private Limited") — flag POSSIBLE_FIRM_NAME_OVERLAP for A3/A4 to check if these are the same brokerage. |
| 11 | Analyst | Sam Bay Desai (name garbled — possibly "Sambhav Desai") | — | "Tamura" (firm name as rendered; likely garbled) | 94 | Asks 2 questions (Q19, Q20). |
| 12 | Analyst | Rohit | — | Progressive Shares | 105 | Asks 8 questions (Q21–Q28), most granular technical questions on the call (continuous-flow chemistry, ROIC). |
| 13 | Analyst | Ketan Chedda | — | Individual investor (explicitly stated by operator, not a firm) | 125 | Asks 4 questions (Q29–Q32). |

Participant grep verification: `grep -n -o -E "Chintan Sha|Chindan Sha|Aish Pindai|AJ delay|Mr\. Mo|Anushka" extract...txt` restricted to transcript body (lines 21+, excluding header lines 15/19 which are the A1 corruption glossary, not transcript) returns 5 distinct management/host/operator name-anchors at line 21 (+1 at line 22 for "Chindan Sha"); `grep -c "from the line of\|is from the line"` returns 8 (one per analyst introduction). 5 + 8 = 13 = sweep count of 13 participant rows.

---

## B. SPEAKER TURNS — every line 21–138, numbered sequentially by extract line number

Speaker code key: OPERATOR = call operator ("Anushka"); HOST = "Mr. Mo" (ICICI Securities); IR = Ajay; MGMT = unattributed management answer (MD and/or CFO, transcript does not disambiguate); ANALYST(name) = named analyst. MULTI_SPEAKER_LINE = the ASR merged two or more speaker turns into one file line with no line break (documented A1 behavior); AMBIGUOUS_SPEAKER = brief interjection whose speaker cannot be determined from text alone.

| Turn (line) | Speaker | First ~10 words | Flags |
|---|---|---|---|
| 21 | OPERATOR then HOST (Mr. Mo) | "Ladies and gentlemen, good day and welcome to the" | MULTI_SPEAKER_LINE |
| 22 | IR (Ajay) | "Thank you. Good evening. On behalf of the management" | MD_OPENING_READ_BY_IR; contains full financial-highlights block and MD's prepared segment commentary + Rs 200cr green-field capex announcement (see sections D/E) |
| 23 | OPERATOR | "Thank you very much. We will now begin the" | introduces Shlok Patel, Zenflow Finance |
| 24 | ANALYST (Shlok Patel) | "Hi Am I audible?" | audio-check, non-substantive |
| 25 | OPERATOR | "Yes, you are audible." | |
| 26 | ANALYST (Shlok Patel) then MGMT | "Yeah, congratulations on the great results. Uh my" | MULTI_SPEAKER_LINE; carries Q1 |
| 27 | ANALYST (Shlok Patel) then MGMT (start) | "Okay, great. Uh my second question is on PAC." | MULTI_SPEAKER_LINE; carries Q2 (start) |
| 28 | MGMT | "we don't sell for lithium batteries. We are into" | continuation of Q2 answer |
| 29 | ANALYST (Shlok Patel) | "Okay. So uh in people written that uh we" | clarification within Q2 |
| 30 | MGMT | "which yeah you are correct. So basically monoglime is" | Q2 answer continued (monoglime detail) |
| 31 | ANALYST (Shlok Patel) | "Okay. Thanks. I'll join back the queue." | |
| 32 | OPERATOR | "Thank you. We take the next question from the" | introduces "part," Asset Managers |
| 33 | ANALYST ("part") | "Yes. Am I audible?" | audio-check |
| 34 | OPERATOR | "Yes, you're audible." | |
| 35 | ANALYST ("part") | "Yes." | filler |
| 36 | ANALYST ("part") then MGMT | "Thank you for the opportunity. And my question is" | MULTI_SPEAKER_LINE; carries Q3 |
| 37 | ANALYST ("part") | "Okay, thank you so much for the opportunity." | |
| 38 | OPERATOR | "Thank you. We take the next question from the" | introduces Raman K V, Sequent Investments |
| 39 | ANALYST (Raman K V) | "Uh hello sir can you hear me?" | audio-check |
| 40 | (confirmation, speaker ambiguous) then ANALYST (Raman K V) | "Yes sir firstly congratulation on good side of uh" | MULTI_SPEAKER_LINE; AMBIGUOUS_SPEAKER for "Yes sir" fragment; carries Q4 |
| 41 | MGMT | "Uh it should contribute around 70 to 80 crores" | Q4 answer (number) |
| 42 | ANALYST (Raman K V) | "Uh and how much can we expect from like" | carries Q5 |
| 43 | MGMT | "200 in the range of 200." | Q5 answer (number) |
| 44 | ANALYST (Raman K V) | "Okay. And uh my second question is uh on" | carries Q6 |
| 45 | MGMT | "Basically the application of this product what we have" | Q6 answer (numbers + hedge) |
| 46 | ANALYST (Raman K V) then MGMT | "Uh and just a follow up on this uh" | MULTI_SPEAKER_LINE; carries Q7 |
| 47 | ANALYST (Raman K V) then MGMT | "So can I ask you who is the end" | MULTI_SPEAKER_LINE; carries Q8 |
| 48 | ANALYST (Raman K V) then MGMT then ANALYST (follow-up) | "Understood. Sir also you mentioned in the call" | MULTI_SPEAKER_LINE; carries Q9 + embedded follow-up; numbers (1.2-1.5x, ~300cr) |
| 49 | MGMT | "No it's a multi-purpose multi-product facility that we" | Q9 follow-up answer |
| 50 | ANALYST (Raman K V) | "understood and so finally uh so you guided for" | carries Q10; contains ANALYST-CITED numbers (10%, 6cr, ~50-60cr) |
| 51 | MGMT | "yeah between 40 to 50 cr is what we" | Q10 answer (number, 40-50cr) |
| 52 | MGMT | "now everything is in place customer demands are very" | continuation |
| 53 | MGMT | "unfortunately we lost a couple of months due to" | continuation — raw-material delay disclosure |
| 54 | ANALYST (Raman K V) | "Uh do we have any specific order book for" | carries Q11 |
| 55 | MGMT | "It is not never an order book in hand." | Q11 answer; ZERO_STANDING (no order book) |
| 56 | ANALYST (Raman K V) | "Okay. Understood. Thank you sir. Thank you so much." | |
| 57 | OPERATOR | "Thank you. We take the next question from the" | introduces Nirani Gopani, Unique PMS |
| 58 | ANALYST (Nirani Gopani) | "Yeah. Hi, thank you for the opportunity and congratulations" | carries Q12 |
| 59 | MGMT | "marginally. So that's not a major impact coming from" | Q12 answer start |
| 60 | MGMT | "because actually honestly speaking we have not been thorough" | continuation; hedge |
| 61 | MGMT | "Now we are looking for price increase." | continuation; forward-commitment |
| 62 | MGMT | "So now we are translating that we are so" | continuation |
| 63 | ANALYST (Nirani Gopani) | "Okay. Okay. Uh perfect. And uh and second is" | carries Q13; ANALYST-CITED number (900cr) |
| 64 | MGMT | "There we we are doing some debottlashing stuff. We" | Q13 answer (numbers: 800-850cr, 21/18-month timeline) |
| 65 | ANALYST (Nirani Gopani) | "right so post this 850 crores we'll have some" | follow-up confirmation, not a new question |
| 66 | MGMT | "we are nearly saturated we have consumed all the" | continuation |
| 67 | ANALYST (Nirani Gopani) | "Okay. Okay. And semiconductors will be over and above" | carries Q14 |
| 68 | MGMT | "Not at the moment because we don't honestly speaking" | Q14 answer; ZERO_STANDING (no semiconductor capex at present); hedge; number (not before Q4 2028) |
| 69 | ANALYST (Nirani Gopani) | "right and lastly uh so for this FI27 do" | carries Q15 |
| 70 | MGMT | "okay You see so 25 30% growth is what" | Q15 answer (number, 25-30%) |
| 71 | ANALYST (Nirani Gopani) | "right and for the full year what kind of" | carries Q16 |
| 72 | MGMT | "as I always say so unfortunately we have lost" | Q16 answer (number, 20-22%) |
| 73 | ANALYST (Nirani Gopani) | "Okay." | |
| 74 | ANALYST (Nirani Gopani) | "Okay. Uh no, perfect. Uh that's it. Thank you" | |
| 75 | (brief, speaker ambiguous) | "Thank you." | AMBIGUOUS_SPEAKER |
| 76 | OPERATOR | "Thank you. We take the next question from the" | introduces Gor of Paul, Zenflow Finance Private Limited |
| 77 | ANALYST (Gor of Paul) | "Hello. Am I audible?" | audio-check |
| 78 | OPERATOR | "Yes, you are audible." | |
| 79 | ANALYST (Gor of Paul) | "Yeah. Hi, sir. Thank you for uh the great" | carries Q17 |
| 80 | MGMT | "Yeah. I mean the prices in China is" | Q17 answer start, cut off |
| 81 | (interruption, speaker ambiguous) | "pardon can come back." | AMBIGUOUS_SPEAKER; connection issue |
| 82 | MGMT | "So I" | cut off |
| 83 | ANALYST (Gor of Paul) | "what is happening in China?" | re-ask of Q17 |
| 84 | MGMT | "The price I mean the government is taking away" | Q17 answer continued |
| 85 | MGMT | "so this is this is still news but it's" | Q17 answer continued; hedges (see section F) |
| 86 | ANALYST (Gor of Paul) | "Got it sir. The second question is regarding the" | carries Q18 |
| 87 | MGMT | "but electrolyte of different types of batteries not in" | Q18 answer |
| 88 | ANALYST (Gor of Paul) | "okay so do we have any any uh solutions" | Q18 follow-up |
| 89 | MGMT | "we don't no" | Q18 follow-up answer; ZERO_STANDING (no lithium-battery solutions) |
| 90 | ANALYST (Gor of Paul) | "okay yeah that's all from" | |
| 91 | MGMT | "so basically we we have solution in the uh" | |
| 92 | ANALYST (Gor of Paul) | "Okay. Okay. Understood. Thank you." | |
| 93 | OPERATOR | "Thank you." | |
| 94 | OPERATOR | "We take the next question from the line of" | introduces Sam Bay Desai, Tamura |
| 95 | ANALYST (Sam Bay Desai) | "Uh no audible." | connection issue |
| 96 | ANALYST (Sam Bay Desai) | "Hello. Yes. Hello. Am I audible? Yes. Yes. Yes." | audio-check + carries Q19 |
| 97 | MGMT | "Euro7 is right now is only being implemented across" | Q19 answer (number, 3-4-5 years) |
| 98 | ANALYST (Sam Bay Desai) | "Okay. Okay. Uh and uh my next question was" | carries Q20 |
| 99 | MGMT | "hybrid vehicle batteries customer is into the process of" | Q20 answer (number, Oct/Nov 2026) |
| 100 | ANALYST (Sam Bay Desai) | "Okay. Okay. But but but like the ramp up" | Q20 follow-up |
| 101 | MGMT | "in the revenue" | fragment/continuation |
| 102 | MGMT | "and then that actual commercialization so full scale commercialization" | Q20 answer continued (number, late 2027) |
| 103 | ANALYST (Sam Bay Desai) | "Okay. Okay. Uh thank you so much. That's it" | |
| 104 | OPERATOR | "Thank you." | |
| 105 | OPERATOR then ANALYST (Rohit) | "Thank you. We take the next question from the" | MULTI_SPEAKER_LINE; introduces Rohit, Progressive Shares; carries Q21 |
| 106 | MGMT | "Two products" | Q21 answer (number) |
| 107 | ANALYST (Rohit) | "and in in the next uh 3 years or" | carries Q22 |
| 108 | MGMT | "Now majority of the development what we are doing" | Q22 answer (number, 7-8 products) |
| 109 | ANALYST (Rohit) then MGMT | "When when these uh products probably move from bash" | MULTI_SPEAKER_LINE; carries Q23 |
| 110 | ANALYST (Rohit) | "Mhm." | filler |
| 111 | ANALYST (Rohit) | "Uh if if this continuous flow is our core" | lead-in to Q24 |
| 112 | ANALYST (Rohit) then MGMT | "if if this uh chemistry has got uh such" | MULTI_SPEAKER_LINE; carries Q24 |
| 113 | MGMT | "if we can do I'm sure with given dedication" | Q24 answer continued; hedge |
| 114 | (speaker ambiguous) | "Okay. Okay. Is always faster and easy. So," | AMBIGUOUS_SPEAKER |
| 115 | ANALYST (Rohit) | "Yeah, makes sense. Uh on these uh new uh" | carries Q25 |
| 116 | MGMT then ANALYST (embedded follow-up) | "as I said among the eight products what I" | MULTI_SPEAKER_LINE; Q25 answer + embedded continuation |
| 117 | MGMT | "as far as see we have lot of things" | Q25 answer continued; ZERO_STANDING (no contract manufacturing) |
| 118 | ANALYST (Rohit) | "but for this uh new capacity uh uh do" | carries Q26 |
| 119 | MGMT | "of course of course we do but there may" | Q26 answer; hedge + forward-commitment |
| 120 | ANALYST (Rohit) | "and in the next 3 years uh what sort" | carries Q27 |
| 121 | MGMT | "So over next next 3 to four year it" | Q27 answer (number, 20-25% CAGR) |
| 122 | ANALYST (Rohit) then MGMT | "and anything on the uh minimum acceptable uh post" | MULTI_SPEAKER_LINE; carries Q28 |
| 123 | MGMT | "Now when we talk we say okay asset turn" | Q28 answer continued (numbers: 1.5x, 1:3, 20-22% ROC) |
| 124 | ANALYST (Rohit) | "Okay Chinta thank you for answering my question thanks" | confirms MD ("Chinta") personally answered Q&A |
| 125 | OPERATOR | "So from the next question is from the line" | introduces Ketan Chedda, individual investor |
| 126 | ANALYST (Ketan Chedda) then MGMT | "Yeah hi uh thank you for the opportunity and" | MULTI_SPEAKER_LINE; carries Q29 + Q30 (both embedded in one line); numbers (2,000 tons, $4.6-4.8 to $2.1, 30 days, $3-3.5) |
| 127 | MGMT | "No, it still continues to remain in situation. Basically" | Q30 answer |
| 128 | ANALYST (Ketan Chedda) | "Okay. All right." | |
| 129 | MGMT then ANALYST | "So we are not getting into commercialization. of those" | MULTI_SPEAKER_LINE; ZERO_STANDING (flame retardant, no near-term commercialization) |
| 130 | ANALYST (Ketan Chedda) | "Sure. Right. Um the other question I have is" | carries Q31 |
| 131 | MGMT then ANALYST (embedded follow-up) | "Currently we have five products on pipeline. So one" | MULTI_SPEAKER_LINE; Q31 answer (number, 5) + embedded Q32 |
| 132 | MGMT | "in mature pipeline we have about nine different products" | Q32 answer (number, 9) |
| 133 | MGMT | "uh and semiconductor. So semiconductor products I'm not including" | continuation (number, 8-9, before 2028) |
| 134 | ANALYST (Ketan Chedda) | "Okay. Okay. Um yeah, those are my questions. Uh" | |
| 135 | (brief, speaker ambiguous) | "Thanks." | AMBIGUOUS_SPEAKER |
| 136 | OPERATOR | "Thank you." | |
| 137 | OPERATOR | "Thank you very much... due to time constraints, we" | hands to management for closing |
| 138 | IR (Ajay) then OPERATOR | "Thank you. On behalf of the management of Tazuchin," | MULTI_SPEAKER_LINE; closing remarks delivered by Ajay "on behalf of the management," then operator sign-off |

Turn count check: lines 21 through 138 inclusive = 118 lines; blank-line check (`grep -n -E "^\s*$"`) confirms zero blank lines in that range (blanks occur only at lines 14, 16, 20, all before transcript start). 118 = 118, match.

---

## C. QUESTIONS — one row per distinct analyst question/topic

| Q# | Analyst | Firm | Topic (intended term bracketed where ASR-garbled) | Line | Flags |
|----|---------|------|----------------------------------------------------|------|-------|
| Q1 | Shlok Patel | Zenflow Finance | PTC segment growth drivers and sustainability of growth rate | 26 | |
| Q2 | Shlok Patel | Zenflow Finance | PAC segment — "gimes" [monoglime] sold for lithium-ion batteries; other molecules in segment | 27 (cont. 28-30) | REPEAT_QUESTION — monoglime/lithium-battery topic also asked by Gor of Paul (Q18) and Ketan Chedda (Q29) |
| Q3 | "part" | Asset Managers | Biggest execution risk to FY27 guidance (customer demand vs raw-material volatility vs new-product commercialization) | 36 | |
| Q4 | Raman K V | Sequent Investments | Incremental FY27 revenue from the 3 new pharma molecules flagged in the Q4 FY26 call | 40 | |
| Q5 | Raman K V | Sequent Investments | Revenue from the 3 pharma molecules at full utilization | 42 | |
| Q6 | Raman K V | Sequent Investments | Semiconductor chemical — product/application/total addressable market | 44 | REPEAT_QUESTION — semiconductor topic also asked by Ketan Chedda (Q31) |
| Q7 | Raman K V | Sequent Investments | Semiconductor — customer qualification confirmation (follow-up) | 46 | |
| Q8 | Raman K V | Sequent Investments | Semiconductor — identity of end client (direct semiconductor maker vs intermediary) | 47 | |
| Q9 | Raman K V | Sequent Investments | Green-field capex (~Rs 200cr) — product mix, expected revenue, timeline | 48 | REPEAT_QUESTION — green-field capex/capacity topic also asked by Nirani Gopani (Q13) |
| Q10 | Raman K V | Sequent Investments | ESS/electrolyte segment FY27 guidance (10% revenue contribution) and ramp path | 50 | REPEAT_QUESTION — ESS segment outlook also asked by Sam Bay Desai (Q20) |
| Q11 | Raman K V | Sequent Investments | ESS — existence of a specific order book | 54 | |
| Q12 | Nirani Gopani | Unique PMS | Revenue growth drivers this quarter — pricing improvement vs volume growth | 58 | |
| Q13 | Nirani Gopani | Unique PMS | Current capacity (peak revenue ~Rs900cr) and additional debottlenecking capacity available before green-field comes online | 63 | REPEAT_QUESTION — see Q9 |
| Q14 | Nirani Gopani | Unique PMS | Whether semiconductor business requires capex over and above the green-field/existing base | 67 | REPEAT_QUESTION — see Q6 |
| Q15 | Nirani Gopani | Unique PMS | Whether Q1 FY27 quarterly run-rate (growth) is sustainable for the rest of FY27 | 69 | |
| Q16 | Nirani Gopani | Unique PMS | Full-year FY27 EBITDA margin guidance | 71 | |
| Q17 | Gor of Paul | Zenflow Finance Private Limited | China "anti-involution" / geopolitical — subsidy withdrawal impact on speciality chemicals pricing | 79 (re-asked 83) | |
| Q18 | Gor of Paul | Zenflow Finance Private Limited | DMI/electrolyte salts — solutions for lithium batteries specifically | 86 (follow-up 88) | REPEAT_QUESTION — see Q2 |
| Q19 | Sam Bay Desai | Tamura | SDA vertical — Euro7 rollout geography, China EV/hybrid substitution effect on diesel-truck demand | 96 | |
| Q20 | Sam Bay Desai | Tamura | ESS vertical — hybrid-vehicle-battery customer order/ramp-up timeline | 98 (follow-up 100) | REPEAT_QUESTION — see Q10 |
| Q21 | Rohit | Progressive Shares | Number of current commercial molecules using continuous-flow chemistry | 105 | |
| Q22 | Rohit | Progressive Shares | Expected additions to continuous-flow product count over next 3 years | 107 | |
| Q23 | Rohit | Progressive Shares | Batch-to-continuous transition — impact on yield, manufacturing time, or ROC | 109 | |
| Q24 | Rohit | Progressive Shares | Risk of competitors replicating the continuous-flow-chemistry advantage | 112 | |
| Q25 | Rohit | Progressive Shares | New reactor capacity — which product category will consume it; appetite for contract manufacturing | 115 (cont. 116) | |
| Q26 | Rohit | Progressive Shares | Whether customer commitments exist ahead of new-capacity commissioning | 118 | |
| Q27 | Rohit | Progressive Shares | 3-year forward revenue-growth CAGR outlook | 120 | |
| Q28 | Rohit | Progressive Shares | Minimum acceptable post-tax ROIC / asset-turnover-ratio target | 122 | |
| Q29 | Ketan Chedda | Individual investor | Monoglime — status of the previously-planned ~2,000-ton capacity | 126 | REPEAT_QUESTION — see Q2 |
| Q30 | Ketan Chedda | Individual investor | Flame-retardant product — commercialization status update | 126 (embedded) | |
| Q31 | Ketan Chedda | Individual investor | Semiconductor — other products in the pipeline for this sector | 130 | REPEAT_QUESTION — see Q6 |
| Q32 | Ketan Chedda | Individual investor | Total product count across the pipeline (lab/pilot scale, all segments) | 131 (embedded) | |

Questions grep verification: 32 unique anchor substrings (one per question, drawn from the exact wording of each question) were grep-matched with `grep -n -o -F -f anchors.txt` against the extract file; all 32 matched, each exactly once, at the line cited above (no duplicates, no misses). 32 = 32, match. REPEAT_QUESTION flags raised: 4 topic clusters — (1) monoglime/glimes-for-lithium-batteries: Shlok Patel Q2, Gor of Paul Q18, Ketan Chedda Q29 (3 analysts); (2) semiconductor pipeline/TAM: Raman K V Q6, Nirani Gopani Q14, Ketan Chedda Q31 (3 analysts); (3) green-field capex/capacity: Raman K V Q9, Nirani Gopani Q13 (2 analysts); (4) ESS segment outlook: Raman K V Q10, Sam Bay Desai Q20 (2 analysts).

---

## D. NUMBERS SPOKEN BY MANAGEMENT (and analyst-cited figures recapping guidance, flagged separately)

Attribution key: MGMT/IR = spoken in a management or IR turn; ANALYST_CITED = the figure appears inside an analyst's own question (recapping earlier guidance), not newly disclosed by management at that point in the call — retained here because Role 5 needs it for arithmetic-consistency cross-checking even though it is not a fresh management disclosure.

| N# | Line | Attribution | Figure |
|----|------|-------------|--------|
| N1 | 22 | MGMT/IR | Operating revenue Q1 FY27: Rs 1,671 million |
| N2 | 22 | MGMT/IR | Revenue growth YoY: 43% |
| N3 | 22 | MGMT/IR | Revenue growth QoQ (sequential): 25% |
| N4 | 22 | MGMT/IR | EBITDA ("Evita"): Rs 323 million |
| N5 | 22 | MGMT/IR | EBITDA growth YoY: 86% |
| N6 | 22 | MGMT/IR | EBITDA growth QoQ: 15% |
| N7 | 22 | MGMT/IR | PTC ["case transfer catalyst" = phase transfer catalyst] segment revenue: Rs 428 million |
| N8 | 22 | MGMT/IR | PTC growth QoQ: 38% |
| N9 | 22 | MGMT/IR | PTC growth YoY: 47% |
| N10 | 22 | MGMT/IR | ESS ["electrolyte stalls" = electrolyte salts] segment revenue: Rs 63 million |
| N11 | 22 | MGMT/IR | ESS QoQ: down 52% |
| N12 | 22 | MGMT/IR | ESS growth YoY: 676% |
| N13 | 22 | MGMT/IR | PAC [pharma, agro and specialty chemicals] segment revenue: Rs 584 million |
| N14 | 22 | MGMT/IR | PAC growth QoQ: 63% |
| N15 | 22 | MGMT/IR | PAC growth YoY: 25% |
| N16 | 22 | MGMT/IR | SDA [structure directing agents] segment revenue: Rs 578 million |
| N17 | 22 | MGMT/IR | SDA growth QoQ: 10% |
| N18 | 22 | MGMT/IR | SDA growth YoY: 47% |
| N19 | 22 | MGMT/IR | Green-field manufacturing facility capex: approximately Rs 200 crores |
| N20 | 22 | MGMT/IR | Groundbreaking ceremony date: 20 July 2026 |
| N21 | 22 | MGMT/IR | Company anniversary: "30 years" |
| N22 | 41 | MGMT | Pharma molecules — expected FY27 incremental revenue: Rs 70-80 crores |
| N23 | 43 | MGMT | Pharma molecules — revenue at full utilization: "in the range of 200" (crores) |
| N24 | 45 | MGMT | Semiconductor — plant-scale customer-qualification trials expected: 3-4, "over the course of next two years" |
| N25 | 48 | MGMT | Green-field facility — target asset-turnover ratio: 1.2-1.5x |
| N26 | 48 | MGMT | Green-field facility — peak-utilization revenue: ~Rs 300 crores |
| N27 | 50 | ANALYST_CITED | ESS FY27 guidance recap: "10% revenue contribution" |
| N28 | 50 | ANALYST_CITED | ESS current-quarter revenue recap: "six crores" |
| N29 | 50 | ANALYST_CITED | ESS target recap: "roughly 60 crores... almost 50" |
| N30 | 51 | MGMT | ESS guidance (management-confirmed): Rs 40-50 crores |
| N31 | 63 | ANALYST_CITED | Current capacity — "peak revenue of 900 crores" |
| N32 | 64 | MGMT | Capacity ceiling before new capacity required: "800 850" crores |
| N33 | 64 | MGMT | Green-field timeline (theoretical/stated target): 21 months |
| N34 | 64 | MGMT | Green-field timeline (internal stretch target): 18 months |
| N35 | 68 | MGMT | Semiconductor large-volume commercialization: "not before Q4 of 2028" |
| N36 | 70 | MGMT | FY27 growth forecast (reaffirmed): 25-30% |
| N37 | 72 | MGMT | FY27 EBITDA margin guidance (reaffirmed): 20-22% |
| N38 | 97 | MGMT | Euro7 global geographic rollout: "next 3 4 5 years" |
| N39 | 99 | MGMT | Hybrid-vehicle-battery customer commercialization start: "October or November of this year calendar year 26" |
| N40 | 102 | MGMT | Hybrid-vehicle full-scale commercialization: "somewhere in... late 2027" |
| N41 | 106 | MGMT | Products currently on continuous-flow chemistry: "Two products" |
| N42 | 108 | MGMT | Products expected into commercial/piloting phase near-term: "seven or eight" |
| N43 | 49 | MGMT | Timeframe for recent new-product introductions: "last 2 three years" |
| N44 | 121 | MGMT | 3-4 year forward revenue-growth CAGR: "at least 20 to 25% compounded" |
| N45 | 123 | MGMT | Current asset-turnover ratio: "1.5" |
| N46 | 123 | MGMT | Historical (legacy 3-product) asset-turnover ratio: "one is to three" (1:3) |
| N47 | 123 | MGMT | ROC target: "about 20 22%" |
| N48 | 126 | MGMT | Monoglime — originally planned capacity: "about 2,000 tons" |
| N49 | 126 | MGMT | Monoglime — China price before crash: "$4.6 4.7 $4.8" |
| N50 | 126 | MGMT | Monoglime — China price after crash: "$2.1" |
| N51 | 126 | MGMT | Monoglime — price-crash timeframe: "within 30 days" |
| N52 | 126 | MGMT | Monoglime — current recovered price: "$3 3.5" |
| N53 | 126 | MGMT | Monoglime — current production scale: "few hundred tons" |
| N54 | 131 | MGMT | Semiconductor — pipeline products: "five products" |
| N55 | 132 | MGMT | Mature pipeline products (ex-semiconductor, aggregate): "about nine different products" |
| N56 | 133 | MGMT | Mature pipeline products (restated) / semiconductor commercialization cutoff: "eight or nine different products," "before 2020. 28" [2028] |

Numbers grep verification: 55 of 56 anchor substrings matched on first pass (`grep -n -o -F -f anchors.txt`); the one non-match (N39, line 99) was a transcription-fidelity error in the anchor itself (the source line contains an extra "uh" — "calendar year uh 26" — not present in my anchor string), confirmed present at line 99 on re-check. All 56 rows verified present at their cited lines with zero duplicates. 56 = 56, match. Attribution split: 52 MGMT/IR rows + 4 ANALYST_CITED rows (N27, N28, N29, N31) = 56.

---

## E. FORWARD-COMMITMENT PHRASES (A3 lexicon + concall equivalents)

| FC# | Line | Phrase (as spoken) | Note |
|-----|------|---------------------|------|
| FC1 | 22 | "will continue to create opportunities for sustainable organic growth" | PTC segment |
| FC2 | 22 | "we are confident that this business will position to witness a strong demand" | SDA/Euro7 |
| FC3 | 22 | "commence during the very first quarter itself" | pharma intermediate — "commenc" lexicon hit; status-change (initiated) |
| FC4 | 22 | "expected to move towards commercialization in the later half of the year" | additional pharma molecules |
| FC5 | 22 | "development activities for others are already underway" | R&D pipeline — "underway" lexicon hit |
| FC6 | 22 | "board of directors has today approved the establishment of a new green field manufacturing facility" | ~Rs200cr capex — "board has approved" lexicon hit; the single most concrete dated commitment on the call |
| FC7 | 22 | "We have scheduled the groundbreaking ceremony for this on 20th July 2026" | dated commitment |
| FC8 | 45 | "at least three or four such plant scale trials will happen over the course of next two years" | semiconductor |
| FC9 | 46 | "there will be multiple stages scaleups would happen" | semiconductor scale-up path |
| FC10 | 61 | "Now we are looking for price increase." | pricing pass-through |
| FC11 | 62 | "since last... 40 50 days now that price pass on has started" | status-change: initiated |
| FC12 | 64 | "pushing to get it through within 18 months" (vs 21-month theoretical) | green-field timeline |
| FC13 | 70 | "25 30% growth is what we forecasted and that's what we stick to" | FY27 growth reaffirmation |
| FC14 | 72 | "I would still stick to 20 22% margins" | FY27 margin reaffirmation |
| FC15 | 85 | "if at all happens is expected to be in place from January of next year" | China subsidy change (dated, but conditional — also see hedge H7 same line) |
| FC16 | 97 | "it will happen over the next 3 4 5 years time frame" | Euro7 global rollout |
| FC17 | 99 | "this should happen from October or November of this year calendar year" | hybrid battery |
| FC18 | 102 | "expected to happen somewhere in... late 2027" | hybrid battery full-scale |
| FC19 | 108 | "about seven or eight products in near future getting into commercial phase" | pipeline |
| FC20 | 119 | "there is of course some uh commitment from a customer" | new-capacity customer commitment (informal — also see hedge H10 same line) |
| FC21 | 121 | "at least 20 to 25% compounded growth" | 3-4 year CAGR |
| FC22 | 122 | "we are targeting to cross" [ROIC/asset-turn threshold] | ROIC target framing |
| FC23 | 133 | "what we will commercialize before 2028, we are looking into eight or nine different products" | pipeline / semiconductor cutoff |

## F. HEDGE PHRASES

| H# | Line | Phrase (as spoken) | Note |
|----|------|---------------------|------|
| H1 | 36 | "we don't foresee any uh obstacles to achieve our uh this year's guidance" | reassurance-framed hedge (negation) |
| H2 | 45 | "it is too early right now to wait [predict]" | semiconductor TAM — explicit non-quantification |
| H3 | 45 | "any change in semiconductor is extremely difficult... probably it's not an easy take" | semiconductor qualification-cycle risk |
| H4 | 60 | "honestly speaking we have not been thorough in terms of passing on the increase in cost" | candid admission of margin/pricing lag |
| H5 | 64 | "otherwise we'll start kind of getting stagnated" | risk-framed hedge on capacity timing |
| H6 | 68 | "we don't honestly speaking we don't foresee a major commercialization happening until... Q4 of 2028" | double-hedge on semiconductor timeline |
| H7 | 85 | "it is too early to predict and you never know what the China is going to do. So let us wait and watch and not speculate on that." | explicit refusal to predict — China subsidy scenario |
| H8 | 112 | "if we say we are a very small company... potentially we are the smallest player" | self-deprecating hedge, bears on moat-durability claim |
| H9 | 113 | "I'm sure with given dedication or a given vision any one of them can crack this" | explicit acknowledgment that continuous-flow-chemistry edge is replicable |
| H10 | 119 | "there may not be a contract official contract in place" | informal-only customer commitment, no binding contract |
| H11 | 127 | "it still continues to remain in situation... not much reversal in the situation" | flame retardant — stalled, no forward path given |

Phrases grep verification: 34 anchor substrings (23 FC + 11 H) grep-matched with zero misses and zero duplicates, each at its cited line. 34 = 34, match. Cross-check against literal A3 lexicon regex: forward-commitment lexicon (`expected to be|expected by|will be|...|board has approved|intends to`) hits 12 lines directly; literal filing hedge lexicon (`may sometimes|could have an effect|no assurance|subject to|evaluating|exploring|in discussions|endeavour`) hits 0 lines on this transcript — the manual sweep supplements this with concall-register hedge equivalents (H1-H11), which is the expected and necessary divergence given spoken vs written registers (documented in the reconciliation note at the top of this file).

---

## G. ZERO/NIL-STANDING DISCLOSURES (concall analogue of ZERO_STANDING — flagged per general operating rule 3, never dropped)

| Z# | Line(s) | Item | Flag |
|----|---------|------|------|
| Z1 | 54-55 | ESS order book: none in hand ("It is not never an order book in hand") | ZERO_STANDING |
| Z2 | 88-89 | Lithium-battery electrolyte solutions: none offered ("we don't no") | ZERO_STANDING |
| Z3 | 67-68 | Semiconductor-specific capex: none at present ("Not at the moment") | ZERO_STANDING |
| Z4 | 126-127, 129 | Flame-retardant product: no near-term commercialization ("still continues to remain in situation," "not getting into commercialization... in very near future") | ZERO_STANDING |
| Z5 | 116-117 | Contract manufacturing: none pursued ("I don't see that we... want to go and do contract manufacturing") | ZERO_STANDING |

Zero-standing grep verification: 5 anchor substrings matched with zero misses, each at cited line. 5 = 5, match.

---

## SUMMARY OF FLAGS RAISED

MD_OPENING_READ_BY_IR (line 21-22: opening remarks/MD's prepared speech read by IR Ajay "on his behalf"; MD Chintan Shah personally present and answering Q&A live — not MGMT_ABSENCE), AMBIGUOUS_SPEAKER_ATTRIBUTION (CFO never individually attributed a Q&A turn), MULTI_SPEAKER_LINE (13 lines: 21, 26, 27, 36, 40, 46, 47, 48, 105, 109, 112, 116, 122, 126, 129, 131, 138 — ASR merged consecutive speaker turns with no line break), AMBIGUOUS_SPEAKER (4 brief interjections: lines 40, 75, 81, 114, 135), NAME_NOT_DETERMINABLE (analyst "part," Asset Managers, line 32), POSSIBLE_FIRM_NAME_OVERLAP (Shlok Patel's "Zenflow Finance" vs Gor of Paul's "Zenflow Finance Private Limited" — flagged for A3/A4 to confirm same or different entity), REPEAT_QUESTION (4 topic clusters: monoglime/lithium-battery — Q2/Q18/Q29; semiconductor — Q6/Q14/Q31; green-field capex/capacity — Q9/Q13; ESS segment outlook — Q10/Q20), ZERO_STANDING (5 items, section G), ANALYST_CITED (4 numeric rows, N27/N28/N29/N31, recapping guidance inside an analyst's own question rather than a fresh management disclosure).
