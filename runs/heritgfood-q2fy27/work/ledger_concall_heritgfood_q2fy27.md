# A2 LEDGER: Heritage Foods (HERITGFOOD) Q2 FY27 concall (ASR transcript, 16 Oct 2026)
Enumeration source: runs/heritgfood-q2fy27/extracted/heritgfood-concall-q2fy27-structured.md (A1). Row lines are fulltext lines. Turn numbers derive from the A1 turn map (a line shared by two turns resolves to the later turn). No speakers inferred. Page = ten-minute block.

=== A2 COUNT TEST ===
category: rows_total   grep_count: 336   sweep_count: 336   match: yes
category: numbers      grep_count: 162   sweep_count: 162   match: yes
category: entities     grep_count: 52   sweep_count: 52   match: yes
category: forward      grep_count: 60   sweep_count: 60   match: yes
category: dates        grep_count: 20   sweep_count: 20   match: yes
category: qualifiers   grep_count: 42   sweep_count: 42   match: yes
category: turns        grep_count: 81   sweep_count: 81   match: yes   (A1 header states 81)
category: questions    grep_count: 24   sweep_count: 24   match: yes   (A1 header states 24)
category: mgmt_numbers grep_count: 144   sweep_count: 144   match: yes   (NUMBER rows by management turn; 18 analyst-stated split out; 144+18=162)
category: loop1_addendum  missing_from_structured: 10 (M01-M10): NUMBER 7 (M02-M08), DATE 2 (M01, M09), ENTITY 1 (M10). grep (CC-L cross-check of A5 list) 10  sweep 10  match: yes
category: loop2_addendum  missing_from_structured: 51 (M11-M61): M11-M32 = A5 V1-V22 (verified, 22 of 22 real): NUMBER 10, ENTITY 3, FORWARD 2, DATE 2, QUALIFIER 5. M33-M61 = closing sweep, 29: NUMBER 18, FORWARD 3, DATE 5, QUALIFIER 2, ENTITY 1. grep (CC-L cross-check of fulltext lines) 51  sweep 51  match: yes
category: final_totals_with_addenda  numbers 197 | entities 57 | forward 65 | dates 29 | qualifiers 49 | total 397 (336 structured + 61 MISSING_FROM_STRUCTURED) | turns 81 | questions 24 | mgmt_numbers 178 + analyst_stated 19 = 197
category: A1_header     NUMBER 162 | ENTITY 52 | FORWARD 60 | DATE 20 | QUALIFIER 42 | total 336: match: yes
gate_a2: pass
=== END COUNT TEST ===

ids_in_structured: 336 | ids_referenced_in_ledger: 336 | orphan_ids: [] | match: yes
ledger rows total after loop 2 (FINAL, ledger closed): 397 (336 structured IDs + 61 MISSING_FROM_STRUCTURED rows M01-M61); structured IDs 336 all referenced, orphan_ids [] (loop 1 total was 346)

## 1. PARTICIPANTS (management and analysts)
ROW_ID | category | A2 flags | note
R163 | participant |  | Host introducing call (Go India Advisors) (T001)
R164 | participant |  | Investor relations host of the call (T002)
R165 | participant | MGMT ASR_NAME | Executive Director (ASR of Brahmani Nara) (T002)
R166 | participant | MGMT | Whole-Time Director (T002)
R167 | participant | MGMT ASR_NAME | CEO (ASR of Sreedeep Kesavan) (T002)
R168 | participant | MGMT | CFO (T002)
R169 | participant | MGMT | COO (T002)
R170 | participant | MGMT | CEO, Heritage NutriVate Limited (T002)
R171 | participant | MGMT ASR_NAME | Company Secretary and Compliance Officer (ASR of Umakanta Barik) (T002)
R182 | participant | ANALYST | Analyst, question 1 (T004)
R184 | participant | ASR_NAME | ASR variant of Sreedeep Kesavan (T008)
R186 | participant | ANALYST ASR_NAME | Analyst (firm ASR "the matic"), question 2 (T010)
R187 | participant | ANALYST | Analyst (T020)
R194 | participant | SPEAKER_UNMAPPED | Self-identified speaker, not in source-header mapping (T028)
R195 | participant | ANALYST | Analyst (T030)
R196 | participant | ANALYST ASR_NAME | Analyst (ASR firm name) (T036)
R198 | participant | ANALYST | Analyst (T039)
R203 | participant | ANALYST ASR_NAME | Analyst (ASR name) (T047)
R204 | participant | ANALYST ASR_NAME | Analyst (ASR name; also "Mr. Rajat") (T053)
R205 | participant | ANALYST | Analyst (T061)
R208 | participant | ANALYST ASR_NAME | Analyst (ASR name) (T064)
R209 | participant | ANALYST ASR_NAME | Analyst (ASR "Roger in Korea") (T069)
R210 | participant | ANALYST | Analyst (T071)
R211 | participant | ANALYST | Analyst (T074)
MGMT_ABSENCE: none raised. Listed management: Executive Director (R165), Whole-Time Director (R166), CEO (R167), CFO (R168), COO (R169), CEO NutriVate (R170), CS (R171). Self-identified speakers: Dr. Rao (T003,T080), CEO (T008,T022,T032,T076), Dr. Bridge Mohan (T067), Ramani (T028). Executive Director has no self-identified turn (A1 attributes T078 by cue only). Most answers T006-T078 are unattributed.

## 2. SPEAKER TURNS (T001-T081)
TURN | speaker (A1 map) | question | A2 flags | structured rows anchored in turn (count; first-last)
T001 | moderator (operator; cue: hand-off to Ms. Deya Kaswa L00:00:28) | - |  | 1; R163-R163
T002 | Deya Kaswa, host (self-identified L00:00:37; Go India Advisors) | - |  | 11; R164-R297
T003 | Dr. Rao, opening remarks (cue: moderator-host hand-off L00:01:22 "I now invite Dr. Rao") | - |  | 91; R001-R306
T004 | moderator (cue: "We will now begin the question and answer session"; turn starts mid-line) | - |  | 1; R182-R182
T005 | Samir Gupta, IIFL Capital (cue L00:13:19) | Q01 |  | 0; none
T006 | management (unattributed in-turn; cue L00:21:29 says the whole-time director answered Sami | - | SPEAKER_UNATTRIBUTED | 7; R060-R282
T007 | Samir Gupta, IIFL Capital (continuing, same caller) | Q02 |  | 0; none
T008 | Sreedeep Kesavan, CEO (ASR "Srivithya", self-identified L00:17:09) | - | ASR_NAME | 2; R184-R185
T009 | Samir Gupta, IIFL Capital (closing remark) | - |  | 0; none
T010 | moderator (cue: "The next question comes from the line of") | - |  | 1; R186-R186
T011 | Jay Dangir, "which is the matic" (ASR firm name; cue L00:19:08) | Q03 | ASR_NAME | 0; none
T012 | management (unattributed; asks to repeat question) | - | SPEAKER_UNATTRIBUTED | 0; none
T013 | analyst (Jay Dangir, repeats second question) | - |  | 0; none
T014 | management (unattributed; "Good morning." L00:20:00 unclear who speaks, answer follows) | - | SPEAKER_UNATTRIBUTED | 20; R062-R310
T015 | analyst (unattributed; follows Jay Dangir turn, QoQ price movement) | Q04 | SPEAKER_UNATTRIBUTED | 2; R072-R311
T016 | management (unattributed) | - | SPEAKER_UNATTRIBUTED | 5; R073-R231
T017 | analyst (unattributed; "Yeah, yes sir") | - | SPEAKER_UNATTRIBUTED | 0; none
T018 | management (unattributed) | - | SPEAKER_UNATTRIBUTED | 0; none
T019 | moderator or management (unattributed; audio-quality remark L00:23:29), moderator cue at L | - | SPEAKER_UNATTRIBUTED | 1; R312-R312
T020 | moderator (cue: next question) | - |  | 1; R187-R187
T021 | Nirmal, Unique PMS (cue L00:23:55) | Q05 |  | 0; none
T022 | Sreedeep Kesavan, CEO (ASR "Sridhi Kagan", self-identified L00:24:23) | - | ASR_NAME | 15; R076-R285
T023 | analyst (Nirmal, follow-up Q3 prices) | Q06 |  | 1; R235-R235
T024 | management (unattributed; "Yes, that's what we are hoping") | - | SPEAKER_UNATTRIBUTED | 1; R236-R236
T025 | analyst (Nirmal, second question: cycle turns, pass-through) | Q07 |  | 0; none
T026 | management (unattributed; answer on consumer pricing and mix) | - | SPEAKER_UNATTRIBUTED | 9; R081-R240
T027 | analyst (Nirmal, last question: milk availability, flush season) | Q08 |  | 0; none
T028 | Ramani (self-identified "This is Ramani here" L00:28:46; ASR; not in source-header name ma | - | ASR_NAME | 3; R086-R241
T029 | analyst (Nirmal, thanks) | - |  | 0; none
T030 | moderator (limit two questions per participant; next question) | - |  | 1; R195-R195
T031 | Yash, Oregon Capital Advisors (ASR; cue L00:30:24) | Q09 | ASR_NAME | 0; none
T032 | Sreedeep Kesavan, CEO (ASR "Srivithi", self-identified L00:30:41) | - | ASR_NAME | 14; R087-R315
T033 | Yash, Oregon Capital Advisors (follow-up: cooperatives) | Q10 |  | 0; none
T034 | management (unattributed; declines to comment on cooperatives) | - | SPEAKER_UNATTRIBUTED | 1; R316-R316
T035 | analyst/moderator (thanks, unattributed) | - | SPEAKER_UNATTRIBUTED | 0; none
T036 | moderator (cue: next question) | - |  | 1; R196-R196
T037 | Ishani, Enri Alpha (ASR; cue L00:33:31) | Q11 | ASR_NAME | 3; R091-R317
T038 | management (unattributed; "Volume.") | - | SPEAKER_UNATTRIBUTED | 1; R318-R318
T039 | moderator (cue: next question) | - |  | 1; R198-R198
T040 | Siddharth Share, YES Securities (ASR; cue L00:34:05) | Q12 | ASR_NAME | 0; none
T041 | management (unattributed) | - | SPEAKER_UNATTRIBUTED | 8; R092-R320
T042 | Siddharth Share, YES Securities (follow-up: consumer packs share of ghee) | Q13 |  | 0; none
T043 | management (unattributed) | - | SPEAKER_UNATTRIBUTED | 1; R095-R095
T044 | Siddharth Share, YES Securities (follow-up: new large-conglomerate competition) | Q14 |  | 1; R200-R200
T045 | management (unattributed; industry and strategy answer) | - | SPEAKER_UNATTRIBUTED | 20; R096-R322
T046 | analyst (thanks, unattributed) | - | SPEAKER_UNATTRIBUTED | 0; none
T047 | moderator (cue: next question) | - |  | 1; R203-R203
T048 | Tetsumana Chaudhry, Bowhead Investments (ASR; cue L00:41:04) | Q15 | ASR_NAME | 3; R110-R323
T049 | management (unattributed) | - | SPEAKER_UNATTRIBUTED | 8; R112-R325
T050 | analyst (Tetsumana Chaudhry, follow-up: procurement cost trajectory) | Q16 |  | 3; R116-R118
T051 | management (unattributed) | - | SPEAKER_UNATTRIBUTED | 8; R119-R326
T052 | analyst (thanks) then moderator (cue: limit one question per participant) | - |  | 1; R327-R327
T053 | Prachat, ITAR PMS (ASR; cue L00:45:07) | Q17 | ASR_NAME | 4; R122-R204
T054 | management (unattributed) | - | SPEAKER_UNATTRIBUTED | 7; R125-R330
T055 | analyst (Prachat, follow-up: absolute vs margin; Q3 price hike) | Q18 |  | 0; none
T056 | management (unattributed) | - | SPEAKER_UNATTRIBUTED | 1; R256-R256
T057 | analyst (Prachat, third: months and percentage of price hikes) | Q19 |  | 0; none
T058 | moderator (interrupts Mr. Rajat; asks to rejoin queue) | - |  | 0; none
T059 | management (unattributed) | - | SPEAKER_UNATTRIBUTED | 3; R129-R290
T060 | analyst (thanks) and moderator (cue: next question) | - |  | 0; none
T061 | moderator (cue: next question) | - |  | 1; R205-R205
T062 | Resha Mehta, Green-Edged Wealth (ASR; cue L00:47:52) | Q20 | ASR_NAME | 2; R130-R131
T063 | management (unattributed; cow milk vs buffalo milk answer) | - | SPEAKER_UNATTRIBUTED | 5; R132-R207
T064 | analyst (thanks) and moderator (cue: next question) | - |  | 1; R208-R208
T065 | Madhu Rahati, Counter Cyclical Investments (ASR; cue L00:50:58) | Q21 | ASR_NAME | 0; none
T066 | moderator or management (unattributed; "Even request Mr. Bridge.") | - | SPEAKER_UNATTRIBUTED | 0; none
T067 | Dr. Bridge Mohan, Heritage NutriVate (self-identified L00:51:36) | - |  | 5; R257-R331
T068 | analyst/moderator (thanks) and moderator (cue: next question) | - |  | 0; none
T069 | Roger, Chris PMS (ASR "Roger in Korea"; cue L00:52:55) | Q22 | ASR_NAME | 1; R209-R209
T070 | management (unattributed) | - | SPEAKER_UNATTRIBUTED | 6; R135-R333
T071 | analyst (thanks) and moderator (cue: next question) | - |  | 1; R210-R210
T072 | Sunil Desai, Total Capital (cue L00:54:22) | Q23 |  | 3; R139-R259
T073 | management (unattributed) | - | SPEAKER_UNATTRIBUTED | 9; R141-R264
T074 | moderator (cue: next question) | - |  | 1; R211-R211
T075 | Siddharth, CWC (cue L00:56:36) | Q24 |  | 4; R145-R148
T076 | management (unattributed; then Sreedeep Kesavan self-identifies L00:59:22 "this is Shree D | - | SPEAKER_UNATTRIBUTED | 26; R149-R336
T077 | management (unattributed; hand-off "I'll pass on to Edie" L01:03:01; ASR) | - | SPEAKER_UNATTRIBUTED ASR_NAME | 0; none
T078 | management (unattributed; speaks after handoff, "Thanks, Anshit", ASR; executive-director  | - | SPEAKER_UNATTRIBUTED ASR_NAME | 5; R161-R273
T079 | moderator (cue: last question; hand to Dr Rao) | - |  | 0; none
T080 | Dr. Rao, closing remarks (cue L01:05:58) | - |  | 1; R274-R274
T081 | moderator (cue: "On behalf of Heritage Foods Limited ... concludes this conference") | - |  | 0; none

## 3. QUESTIONS (24)
Q | analyst | firm | topic | turn | A2 flags | anchor row
Q01 | Samir Gupta | IIFL Capital | moderation of procurement prices into buffalo flush | T005 |  | R182
Q02 | Samir Gupta | IIFL Capital | VAP 32% growth, weather support | T007 |  | R182
Q03 | Jay Dangir | firm ASR "the matic" | Q2 price hikes, Q3 plans; procurement inflation (second part repeated at T013) | T011 |  | R186
Q04 | unattributed analyst | - | QoQ price movement 2.4-2.5% vs Q3 | T015 | REPEAT_QUESTION (price movement; see Q03) | R072
Q05 | Nirmal | Unique PMS | cooperator (Nandini) price hike; October trend | T021 |  | R187
Q06 | Nirmal | Unique PMS | Q3 continuation of price levels | T023 | REPEAT_QUESTION (Q3 price stance; see Q03,Q04) | R187
Q07 | Nirmal | Unique PMS | cycle turn: segments, pass-through | T025 |  | R187
Q08 | Nirmal | Unique PMS | milk availability in flush season, drought | T027 |  | R187
Q09 | Yash | Oregon Capital Advisors | is the procurement-cycle worst behind us | T031 | REPEAT_QUESTION partial (cycle direction, see Q01,Q16); MGMT_DECLINE speculative (R313) | R195
Q10 | Yash | Oregon Capital Advisors | cooperatives behaviour | T033 | MGMT_DECLINE (R316) | R195
Q11 | Ishani | Enri Alpha (ASR) | 80% of procurement: price or volume | T037 |  | R196
Q12 | Siddharth Share | YES Securities | lassi and buttermilk growth at near zero price rise | T040 |  | R198
Q13 | Siddharth Share | YES Securities | consumer packs vs bulk share of ghee | T042 |  | R198
Q14 | Siddharth Share | YES Securities | new large-conglomerate competition | T044 |  | R198
Q15 | Tetsumana Chaudhry | Bowhead Investments (ASR) | Q3 11% procurement rise implies +3 rupees | T048 | REPEAT_QUESTION (Q3 11% procurement; answered R230) | R203
Q16 | Tetsumana Chaudhry | Bowhead Investments (ASR) | procurement cost trajectory 47.7 to 50+ | T050 | REPEAT_QUESTION (procurement trajectory; see Q01,Q15) | R203
Q17 | Prachat | ITAR PMS (ASR) | 0.5 rupee cut to 0.7% bottom line: absolute or margin | T053 | REPEAT_QUESTION partial (R081-R082 illustration) | R204
Q18 | Prachat | ITAR PMS (ASR) | Q3 price hike plan | T055 | REPEAT_QUESTION (Q3 price hike plan; see Q03,Q06) | R204
Q19 | Prachat | ITAR PMS (ASR) | months and percentage of Q2 hikes | T057 | REPEAT_QUESTION (Q2 hike months and percent; see Q03,R069,R129) | R204
Q20 | Resha Mehta | Green-Edged Wealth | cow vs buffalo milk inflation slide | T062 |  | R205
Q21 | Madhu Rahati | Counter Cyclical Investments (ASR) | feed segment pass-through | T065 |  | R208
Q22 | Roger | Chris PMS (ASR) | curd, paneer, ice cream revenue contribution | T069 |  | R209
Q23 | Sunil Desai | Total Capital | margin trajectory after price hike at 5.6% | T072 |  | R210
Q24 | Siddharth | CWC | 6% procurement CAGR adequacy; ice cream, exports | T075 |  | R211
Q&A share: T005-T079 = 75 of 81 turns; T001-T004 and T080-T081 outside Q&A; opening remarks T003 span fulltext lines 150-265.

## 4. NUMBERS (162): MGMT_NUMBER vs ANALYST_STATED, with turn
ROW_ID | category | A2 flags | turn | cross-ref / note
R001 | number | MGMT_NUMBER | T003 page 1 | 
R002 | number | MGMT_NUMBER | T003 page 1 | ASR_UNIT dollar sign (R298)
R003 | number | MGMT_NUMBER | T003 page 1 | 
R004 | number | MGMT_NUMBER | T003 page 1 | 
R005 | number | MGMT_NUMBER | T003 page 1 | 
R006 | number | MGMT_NUMBER | T003 page 1 | 
R007 | number | MGMT_NUMBER | T003 page 1 | 
R008 | number | MGMT_NUMBER | T003 page 1 | RESTATED: 98bps margin step
R009 | number | MGMT_NUMBER | T003 page 1 | RESTATED: 7% procurement volume
R010 | number | MGMT_NUMBER | T003 page 1 | 
R011 | number | MGMT_NUMBER | T003 page 1 | 
R012 | number | MGMT_NUMBER | T003 page 1 | 
R013 | number | MGMT_NUMBER | T003 page 1 | RESTATED: 11% procurement cost
R014 | number | MGMT_NUMBER | T003 page 1 | RESTATED: 47.7 rupee procurement cost
R015 | number | MGMT_NUMBER | T003 page 1 | 
R016 | number | MGMT_NUMBER | T003 page 1 | 
R017 | number | MGMT_NUMBER | T003 page 1 | 
R018 | number | MGMT_NUMBER | T003 page 1 | 
R019 | number | MGMT_NUMBER | T003 page 1 | 
R020 | number | MGMT_NUMBER | T003 page 1 | 
R021 | number | MGMT_NUMBER | T003 page 1 | 
R022 | number | MGMT_NUMBER | T003 page 1 | 
R023 | number | MGMT_NUMBER | T003 page 1 | 
R024 | number | MGMT_NUMBER | T003 page 1 | 
R025 | number | MGMT_NUMBER | T003 page 1 | 
R026 | number | MGMT_NUMBER | T003 page 1 | 
R027 | number | MGMT_NUMBER | T003 page 1 | 
R028 | number | MGMT_NUMBER | T003 page 1 | 
R029 | number | MGMT_NUMBER | T003 page 1 | 
R030 | number | MGMT_NUMBER | T003 page 1 | 
R031 | number | MGMT_NUMBER | T003 page 1 | 
R032 | number | MGMT_NUMBER | T003 page 1 | 
R033 | number | MGMT_NUMBER | T003 page 1 | RESTATED: Ice cream growth
R034 | number | MGMT_NUMBER | T003 page 1 | 
R035 | number | MGMT_NUMBER | T003 page 1 | 
R036 | number | MGMT_NUMBER | T003 page 1 | 
R037 | number | MGMT_NUMBER | T003 page 1 | 
R038 | number | MGMT_NUMBER | T003 page 1 | 
R039 | number | MGMT_NUMBER | T003 page 1 | 
R040 | number | MGMT_NUMBER | T003 page 1 | 
R041 | number | MGMT_NUMBER | T003 page 1 | 
R042 | number | MGMT_NUMBER | T003 page 1 | 
R043 | number | MGMT_NUMBER | T003 page 1 | 
R044 | number | MGMT_NUMBER | T003 page 1 | 
R045 | number | MGMT_NUMBER | T003 page 1 | 
R046 | number | MGMT_NUMBER | T003 page 1 | 
R047 | number | MGMT_NUMBER | T003 page 1 | 
R048 | number | MGMT_NUMBER | T003 page 1 | 
R049 | number | MGMT_NUMBER | T003 page 1 | 
R050 | number | MGMT_NUMBER | T003 page 1 | ASR "71 percent" (R176)
R051 | number | MGMT_NUMBER | T003 page 1 | 
R052 | number | MGMT_NUMBER | T003 page 1 | 
R053 | number | MGMT_NUMBER | T003 page 2 | 
R054 | number | MGMT_NUMBER | T003 page 2 | 
R055 | number | MGMT_NUMBER | T003 page 2 | 
R056 | number | MGMT_NUMBER | T003 page 2 | 
R057 | number | MGMT_NUMBER | T003 page 2 | 
R058 | number | MGMT_NUMBER | T003 page 2 | 
R059 | number | MGMT_NUMBER | T003 page 2 | 
R060 | number | MGMT_NUMBER | T006 page 2 | 
R061 | number | MGMT_NUMBER | T006 page 2 | RESTATED: 7% procurement volume
R062 | number | MGMT_NUMBER | T014 page 3 | RESTATED: 8% weighted price rise
R063 | number | MGMT_NUMBER | T014 page 3 | RESTATED: Milk NR 6%
R064 | number | MGMT_NUMBER | T014 page 3 | 
R065 | number | MGMT_NUMBER | T014 page 3 | RESTATED: 8% weighted price rise
R066 | number | MGMT_NUMBER | T014 page 3 | RESTATED: 11% procurement cost
R067 | number | MGMT_NUMBER | T014 page 3 | RESTATED: 8% weighted price rise
R068 | number | MGMT_NUMBER | T014 page 3 | RESTATED: Milk NR 6%
R069 | number | MGMT_NUMBER | T014 page 3 | RESTATED: Jul-Sep hikes
R070 | number | MGMT_NUMBER | T014 page 3 | UNQUANTIFIED
R071 | number | MGMT_NUMBER | T014 page 3 | UNQUANTIFIED
R072 | number | ANALYST_STATED | T015 page 3 | 
R073 | number | MGMT_NUMBER | T016 page 3 | RESTATED: 11% procurement cost
R074 | number | MGMT_NUMBER | T016 page 3 | RESTATED: 8% weighted price rise
R075 | number | MGMT_NUMBER | T016 page 3 | RESTATED: 11% procurement cost
R076 | number | MGMT_NUMBER | T022 page 3 | RESTATED: Aavin farm price
R077 | number | MGMT_NUMBER | T022 page 3 | RESTATED: Aavin farm price
R078 | number | MGMT_NUMBER | T022 page 3 | RESTATED: Aavin farm price
R079 | number | MGMT_NUMBER | T022 page 3 | RESTATED: Karnataka 8 rupee hike
R080 | number | MGMT_NUMBER | T022 page 3 | RESTATED: Karnataka 8 rupee hike
R081 | number | MGMT_NUMBER | T026 page 3 | RESTATED: 0.5 rupee 0.7% illustration
R082 | number | MGMT_NUMBER | T026 page 3 | RESTATED: 0.5 rupee 0.7% illustration
R083 | number | MGMT_NUMBER | T026 page 3 | 
R084 | number | MGMT_NUMBER | T026 page 3 | 
R085 | number | MGMT_NUMBER | T026 page 3 | 
R086 | number | MGMT_NUMBER | T028 page 3 | RESTATED: 7% procurement volume
R087 | number | MGMT_NUMBER | T032 page 4 | ASR_GARBLED (R314)
R088 | number | MGMT_NUMBER | T032 page 4 | ASR_GARBLED (R314)
R089 | number | MGMT_NUMBER | T032 page 4 | AMBIGUOUS_PERIOD (R315,R090)
R090 | number | MGMT_NUMBER | T032 page 4 | AMBIGUOUS_PERIOD (R315,R089)
R091 | number | ANALYST_STATED | T037 page 4 | 
R092 | number | MGMT_NUMBER | T041 page 4 | 
R093 | number | MGMT_NUMBER | T041 page 4 | IN_CALL_CONFLICT 90% vs 95% (R320)
R094 | number | MGMT_NUMBER | T041 page 4 | 
R095 | number | MGMT_NUMBER | T043 page 4 | 
R096 | number | MGMT_NUMBER | T045 page 4 | RESTATED: Industry size
R097 | number | MGMT_NUMBER | T045 page 4 | RESTATED: Industry size
R098 | number | MGMT_NUMBER | T045 page 4 | RESTATED: Industry size
R099 | number | MGMT_NUMBER | T045 page 4 | RESTATED: Amul 75-80k cr
R100 | number | MGMT_NUMBER | T045 page 4 | 
R101 | number | MGMT_NUMBER | T045 page 4 | 
R102 | number | MGMT_NUMBER | T045 page 4 | 
R103 | number | MGMT_NUMBER | T045 page 4 | 
R104 | number | MGMT_NUMBER | T045 page 4 | 
R105 | number | MGMT_NUMBER | T045 page 4 | 
R106 | number | MGMT_NUMBER | T045 page 4 | RESTATED: Industry size
R107 | number | MGMT_NUMBER | T045 page 4 | ASR_SUSPECT 405% (R322)
R108 | number | MGMT_NUMBER | T045 page 5 | RESTATED: Amul 75-80k cr
R109 | number | MGMT_NUMBER | T045 page 5 | 
R110 | number | ANALYST_STATED | T048 page 5 | RESTATED: 11% procurement cost
R111 | number | ANALYST_STATED | T048 page 5 | 
R112 | number | MGMT_NUMBER | T049 page 5 | RESTATED: 98bps margin step
R113 | number | MGMT_NUMBER | T049 page 5 | ASR_GARBLED label (R324)
R114 | number | MGMT_NUMBER | T049 page 5 | RESTATED: 11% procurement cost
R115 | number | MGMT_NUMBER | T049 page 5 | RESTATED: 98bps margin step
R116 | number | ANALYST_STATED | T050 page 5 | RESTATED: 47.7 rupee procurement cost
R117 | number | ANALYST_STATED | T050 page 5 | 
R118 | number | ANALYST_STATED | T050 page 5 | 
R119 | number | MGMT_NUMBER | T051 page 5 | 
R120 | number | MGMT_NUMBER | T051 page 5 | 
R121 | number | MGMT_NUMBER | T051 page 5 | 
R122 | number | ANALYST_STATED | T053 page 5 | RESTATED: 0.5 rupee 0.7% illustration
R123 | number | ANALYST_STATED | T053 page 5 | RESTATED: 0.5 rupee 0.7% illustration
R124 | number | ANALYST_STATED | T053 page 5 | RESTATED: 0.5 rupee 0.7% illustration
R125 | number | MGMT_NUMBER | T054 page 5 | IN_CALL_CONFLICT vs R010 (R328)
R126 | number | MGMT_NUMBER | T054 page 5 | ASR_GARBLED (R330)
R127 | number | MGMT_NUMBER | T054 page 5 | RESTATED: 0.5 rupee 0.7% illustration
R128 | number | MGMT_NUMBER | T054 page 5 | RESTATED: 0.5 rupee 0.7% illustration
R129 | number | MGMT_NUMBER | T059 page 5 | RESTATED: Jul-Sep hikes
R130 | number | ANALYST_STATED | T062 page 5 | 
R131 | number | ANALYST_STATED | T062 page 5 | 
R132 | number | MGMT_NUMBER | T063 page 5 | 
R133 | number | MGMT_NUMBER | T063 page 6 | RESTATED: Aavin farm price
R134 | number | MGMT_NUMBER | T063 page 6 | RESTATED: Aavin farm price
R135 | number | MGMT_NUMBER | T070 page 6 | 
R136 | number | MGMT_NUMBER | T070 page 6 | IN_CALL_CONFLICT/ASR (R333)
R137 | number | MGMT_NUMBER | T070 page 6 | IN_CALL_CONFLICT/ASR (R333)
R138 | number | MGMT_NUMBER | T070 page 6 | 
R139 | number | ANALYST_STATED | T072 page 6 | 
R140 | number | ANALYST_STATED | T072 page 6 | ASR_SUSPECT 70% as printed
R141 | number | MGMT_NUMBER | T073 page 6 | RESTATED: 98bps margin step
R142 | number | MGMT_NUMBER | T073 page 6 | 
R143 | number | MGMT_NUMBER | T073 page 6 | 
R144 | number | MGMT_NUMBER | T073 page 6 | 
R145 | number | ANALYST_STATED | T075 page 6 | 
R146 | number | ANALYST_STATED | T075 page 6 | ASR_GARBLED axis
R147 | number | ANALYST_STATED | T075 page 6 | ASR_GARBLED axis
R148 | number | ANALYST_STATED | T075 page 6 | RESTATED: Ice cream growth
R149 | number | MGMT_NUMBER | T076 page 6 | RESTATED: Ice cream 500 cr vision
R150 | number | MGMT_NUMBER | T076 page 6 | IN_CALL_CONFLICT horizon vs R154 (R334); RESTATED: Ice cream 500 cr vision
R151 | number | MGMT_NUMBER | T076 page 6 | 
R152 | number | MGMT_NUMBER | T076 page 6 | IN_CALL_CONFLICT with R153 (R335)
R153 | number | MGMT_NUMBER | T076 page 6 | IN_CALL_CONFLICT with R152 (R335)
R154 | number | MGMT_NUMBER | T076 page 7 | IN_CALL_CONFLICT horizon vs R150 (R334); RESTATED: Ice cream 500 cr vision
R155 | number | MGMT_NUMBER | T076 page 7 | 
R156 | number | MGMT_NUMBER | T076 page 7 | 
R157 | number | MGMT_NUMBER | T076 page 7 | RESTATED: 11% procurement cost
R158 | number | MGMT_NUMBER | T076 page 7 | 
R159 | number | MGMT_NUMBER | T076 page 7 | 
R160 | number | MGMT_NUMBER | T076 page 7 | RESTATED: 8% weighted price rise
R161 | number | MGMT_NUMBER | T078 page 7 | UNQUANTIFIED
R162 | number | MGMT_NUMBER | T078 page 7 | 

## 5. FORWARD COMMITMENTS AND HEDGES (60 FORWARD rows)
ROW_ID | category | A2 flags | turn | note
R215 | forward | FORWARD_MGMT | T003 | 
R216 | forward | FORWARD_MGMT | T003 | 
R217 | forward | FORWARD_MGMT | T003 | 
R218 | forward | FORWARD_MGMT | T003 | 
R219 | forward | FORWARD_MGMT | T003 | 
R220 | forward | FORWARD_MGMT | T003 | 
R221 | forward | FORWARD_MGMT | T003 | 
R222 | forward | FORWARD_MGMT | T003 | 
R223 | forward | FORWARD_MGMT | T006 | 
R224 | forward | FORWARD_MGMT HEDGE | T006 | 
R225 | forward | FORWARD_MGMT | T006 | 
R226 | forward | FORWARD_MGMT COMMITMENT_STRONG | T014 | 
R227 | forward | FORWARD_MGMT | T014 | 
R228 | forward | FORWARD_MGMT HEDGE | T014 | 
R229 | forward | FORWARD_MGMT HEDGE | T014 | 
R230 | forward | FORWARD_MGMT | T016 | RESTATED: 11% procurement cost
R231 | forward | FORWARD_MGMT HEDGE | T016 | 
R232 | forward | FORWARD_MGMT | T022 | RESTATED: Karnataka 8 rupee hike
R233 | forward | FORWARD_MGMT COMMITMENT_STRONG | T022 | RESTATED: Karnataka 8 rupee hike
R234 | forward | FORWARD_MGMT | T022 | 
R235 | forward | FORWARD_ANALYST_VOICE | T023 | 
R236 | forward | FORWARD_MGMT HEDGE | T024 | LOOP1 RE-FLAG: A1 turn map gives CC-L408 to T024 (management); prior FORWARD_ANALYST_VOICE at T025 was a shared-line slip (A5 hygiene note)
R237 | forward | FORWARD_MGMT COMMITMENT_STRONG | T026 | 
R238 | forward | FORWARD_MGMT COMMITMENT_STRONG | T026 | 
R239 | forward | FORWARD_MGMT | T026 | 
R240 | forward | FORWARD_MGMT | T026 | 
R241 | forward | FORWARD_MGMT HEDGE | T028 | 
R242 | forward | FORWARD_MGMT | T032 | 
R243 | forward | FORWARD_MGMT COMMITMENT_STRONG | T032 | 
R244 | forward | FORWARD_MGMT | T032 | 
R245 | forward | FORWARD_MGMT | T032 | RESTATED: Operating leverage Q3
R246 | forward | FORWARD_MGMT COMMITMENT_STRONG DUPLICATE_OF_R247 | T032 | RESTATED: Operating leverage Q3
R247 | forward | FORWARD_MGMT COMMITMENT_STRONG DUPLICATE_OF_R246 | T032 | RESTATED: Operating leverage Q3
R248 | forward | FORWARD_MGMT COMMITMENT_STRONG | T041 | 
R249 | forward | FORWARD_MGMT | T045 | 
R250 | forward | FORWARD_MGMT | T045 | RESTATED: Amul 75-80k cr
R251 | forward | FORWARD_MGMT COMMITMENT_STRONG | T049 | 
R252 | forward | FORWARD_MGMT HEDGE | T049 | 
R253 | forward | FORWARD_MGMT | T051 | 
R254 | forward | FORWARD_MGMT HEDGE | T051 | 
R255 | forward | FORWARD_MGMT HEDGE | T051 | 
R256 | forward | FORWARD_MGMT | T056 | 
R257 | forward | FORWARD_MGMT | T067 | 
R258 | forward | FORWARD_MGMT | T067 | 
R259 | forward | FORWARD_ANALYST_VOICE | T072 | 
R260 | forward | FORWARD_MGMT | T073 | 
R261 | forward | FORWARD_MGMT | T073 | 
R262 | forward | FORWARD_MGMT | T073 | RESTATED: Operating leverage Q3
R263 | forward | FORWARD_MGMT | T073 | 
R264 | forward | FORWARD_MGMT | T073 | 
R265 | forward | FORWARD_MGMT | T076 | RESTATED: Ice cream 500 cr vision
R266 | forward | FORWARD_MGMT | T076 | RESTATED: Ice cream 500 cr vision
R267 | forward | FORWARD_MGMT | T076 | 
R268 | forward | FORWARD_MGMT | T076 | RESTATED: Ice cream 500 cr vision
R269 | forward | FORWARD_MGMT | T076 | 
R270 | forward | FORWARD_MGMT | T076 | 
R271 | forward | FORWARD_MGMT | T076 | 
R272 | forward | FORWARD_MGMT | T078 | 
R273 | forward | FORWARD_MGMT | T078 | 
R274 | forward | FORWARD_MGMT | T080 | 

## 6. ENTITIES (52)
ROW_ID | category | A2 flags | turn
R163 | entity |  | T001
R164 | entity |  | T002
R165 | entity | ASR_NAME | T002
R166 | entity |  | T002
R167 | entity | ASR_NAME | T002
R168 | entity |  | T002
R169 | entity |  | T002
R170 | entity |  | T002
R171 | entity | ASR_NAME | T002
R172 | entity |  | T003
R173 | entity |  | T003
R174 | entity |  | T003
R175 | entity | ASR_NAME | T003
R176 | entity |  | T003
R177 | entity |  | T003
R178 | entity |  | T003
R179 | entity | ASR_NAME | T003
R180 | entity |  | T003
R181 | entity |  | T003
R182 | entity |  | T004
R183 | entity | ASR_NAME | T006
R184 | entity | ASR_NAME | T008
R185 | entity |  | T008
R186 | entity | ASR_NAME | T010
R187 | entity |  | T020
R188 | entity | ASR_NAME | T022
R189 | entity |  | T022
R190 | entity | ASR_NAME | T022
R191 | entity |  | T022
R192 | entity | ASR_NAME | T022
R193 | entity |  | T022
R194 | entity | SPEAKER_UNMAPPED | T028
R195 | entity |  | T030
R196 | entity | ASR_NAME | T036
R197 | entity | ASR_NAME ENTITY_UNRESOLVED | T037
R198 | entity |  | T039
R199 | entity |  | T041
R200 | entity | COMPETITOR_UNNAMED | T044
R201 | entity |  | T045
R202 | entity |  | T045
R203 | entity | ASR_NAME | T047
R204 | entity | ASR_NAME | T053
R205 | entity |  | T061
R206 | entity |  | T063
R207 | entity |  | T063
R208 | entity | ASR_NAME | T064
R209 | entity | ASR_NAME | T069
R210 | entity |  | T071
R211 | entity |  | T074
R212 | entity | ASR_NAME | T076
R213 | entity |  | T076
R214 | entity | ASR_NAME | T078
ENTITY_CHANGE: not assessable, no prior ledger (ND).

## 7. DATES (20)
ROW_ID | category | A2 flags | turn | note
R275 | date |  | hdr | 
R276 | date |  | T002 | 
R277 | date |  | T003 | 
R278 | date |  | T003 | 
R279 | date |  | T003 | 
R280 | date |  | T003 | 
R281 | date | ASR_DATE | T003 | 
R282 | date |  | T006 | 
R283 | date |  | T014 | RESTATED: Jul-Sep hikes
R284 | date |  | T014 | 
R285 | date |  | T022 | RESTATED: Karnataka 8 rupee hike
R286 | date |  | T032 | 
R287 | date |  | T041 | 
R288 | date |  | T051 | 
R289 | date |  | T059 | RESTATED: Jul-Sep hikes
R290 | date | ASR_DATE | T059 | 
R291 | date |  | T067 | 
R292 | date |  | T067 | 
R293 | date |  | T076 | 
R294 | date |  | T076 | 

## 8. QUALIFIERS (42)
ROW_ID | category | A2 flags | turn
R295 | qualifier | ASR_GARBLE; SOURCE_TIER_MGMT_ASR | hdr
R296 | qualifier | SAFE_HARBOR | T002
R297 | qualifier | SAFE_HARBOR | T002
R298 | qualifier | ASR_GARBLE | T003
R299 | qualifier |  | T003
R300 | qualifier |  | T003
R301 | qualifier |  | T003
R302 | qualifier |  | T003
R303 | qualifier |  | T003
R304 | qualifier |  | T003
R305 | qualifier | ASR_GARBLE | T003
R306 | qualifier |  | T003
R307 | qualifier |  | T014
R308 | qualifier |  | T014
R309 | qualifier |  | T014
R310 | qualifier |  | T014
R311 | qualifier |  | T015
R312 | qualifier |  | T019
R313 | qualifier | MGMT_DECLINE | T032
R314 | qualifier | ASR_GARBLE | T032
R315 | qualifier |  | T032
R316 | qualifier | MGMT_DECLINE | T034
R317 | qualifier | ASR_GARBLE | T037
R318 | qualifier |  | T038
R319 | qualifier |  | T041
R320 | qualifier | IN_CALL_CONFLICT 90% vs 95%; ASR_GARBLE | T041
R321 | qualifier |  | T045
R322 | qualifier | ASR_GARBLE | T045
R323 | qualifier | ASR_GARBLE | T048
R324 | qualifier | ASR_GARBLE | T049
R325 | qualifier | MGMT_DECLINE | T049
R326 | qualifier |  | T051
R327 | qualifier | ASR_GARBLE | T052
R328 | qualifier | IN_CALL_CONFLICT 1.8m L/day (R125, management T054) vs R010 | T054
R329 | qualifier |  | T054
R330 | qualifier | ASR_GARBLE | T054
R331 | qualifier | ASR_GARBLE | T067
R332 | qualifier |  | T070
R333 | qualifier | IN_CALL_CONFLICT paneer 1200 vs 200+230 cr; ASR_GARBLE | T070
R334 | qualifier | IN_CALL_CONFLICT ice cream horizon | T076
R335 | qualifier | IN_CALL_CONFLICT ice cream FY27 revenue | T076
R336 | qualifier |  | T076

## 9. IN-CALL CONFLICT LEDGER
C1: ice cream FY27 revenue, ~200 cr (R153) vs 170-180 cr (R152); R335; T076
C2: ice cream 500 cr horizon 6-7 yrs (R150, R266) vs 5-6 yrs (R154, R268); R334; T076/T077
C3: TWO READINGS of CC-L715-718 (R136 "1200 kind of thing", R137 "200 crores plus 200 230 crores"; R333; T070). Reading A: "1200" is an ASR artefact for paneer. Reading B: "annualized about 1200" is curd's annual figure (about 320 x 4) and the paneer figure is the separate "annualized ... 200 crores plus 200 230 crores". Not a settled in-call contradiction; A4 states both (A5 F1). Separating observation: quarterly curd revenue.
C4: ghee/paneer/curd share 90% vs 95% (R093); R320; T041
C5: 1.8m L/day (R125, management turn T054, "illustration" per A1) vs reported 17.28 lakh L/day (R010, T003); R328; T054 (LOOP1: prior label "analyst, T055" was a turn slip)
C6: VAP contribution 4.1% "in Q3" with "15 days into the quarter" (R089,R090); R315; T032 (LOOP1: prior cite T045 was a turn slip; CC-L477 sits in T032)
C7: EBITDA 4.6 to 5.6 (R141) vs 98 bps (R008): about 100 bps, consistent within rounding
C8: Q2 revenue prints "$13,196 million" (R002,R298): ASR dollar sign; Rs by context

## 10. MISSING_FROM_STRUCTURED (LOOP 1 ADDENDUM, 2026-10-19; source: A5 Role 5 finding M1)
Each unit was checked against the fulltext (CC-L = fulltext line) and against structured rows at the same lines. No structured row holds any of the ten claims. Rows at neighbouring lines (R155/R156 at L779-780; R206 at L682; R140 at L725; R089/R090 at L477; R133/R134 at L681) carry different claims, so none is duplicated. New row IDs are M-prefixed; they are NOT structured IDs.
ROW | CC-L | time | type | turn | verbatim unit | A2 flags | note
M01 | CC-L479-481 | 00:31:44-00:31:57 | DATE | T032 (management, CEO) | "in the beginning of the year, we had capitalized some large projects and those depreciation is also impacting the P and L" | MISSING_FROM_STRUCTURED | A4 uses in K10, Q43
M02 | CC-L481-482 | 00:31:57-00:32:01 | NUMBER (unquantified comparative) | T032 | "the EBITDA improvement sequential is far better than PVT or VAT. The reason is depreciation is much higher" | MISSING_FROM_STRUCTURED | A4 uses in FC-1, Q49; ASR "PVT or VAT" as printed
M03 | CC-L667-669 | 00:49:12-00:49:25 | NUMBER (unquantified comparative) | T063 (management) | "what is really affected is the buffalo milk supply ... cow milk supply is reasonably growing" | MISSING_FROM_STRUCTURED | Q20 answer substance
M04 | CC-L672 | 00:49:46 | NUMBER (unquantified comparative) | T063 | "cow milk on a solid basis is cheaper than buffalo milk" | MISSING_FROM_STRUCTURED | Carries working reading B (slide 9 note)
M05 | CC-L677 | 00:50:01 | NUMBER (unquantified comparative) | T063 | "cow [milk] is becoming dearer now" | MISSING_FROM_STRUCTURED, ASR_GARBLE | ASR prints "cow meat"; bracket restores milk from context of L667-686
M06 | CC-L686 | 00:50:40 | NUMBER (unquantified comparative) | T063 | "the significant inflationary trend we have seen also is in the hardcore cow milk" | MISSING_FROM_STRUCTURED | Carries working reading B; sits with R133/R134 (L681)
M07 | CC-L699-701 | 00:51:40-00:51:47 | NUMBER (unquantified comparative) | T067 (Dr. Bridge Mohan, Heritage NutriVate) | "we have a strong quarter two ... we had a difficult quarter one due to the very, very high cost of the ingredients" | MISSING_FROM_STRUCTURED | A4 uses in FC-5, Q9
M08 | CC-L798-799 | 01:02:46-01:02:49 | NUMBER (unquantified comparative) | T076 (management) | "our bottom line is suffering whenever there is a raw milk price increase" | MISSING_FROM_STRUCTURED | A4 uses in 6A, 6D, 8D
M09 | CC-L725-726 | 00:54:55-00:55:06 | DATE (analyst horizon) | T072 (analyst, Q23 Sunil Desai) | "over let's say next 2-3-4 quarters" | MISSING_FROM_STRUCTURED, ANALYST_STATED | Same sentence as R140 (70%, L725); horizon is analyst's, not management's
M10 | CC-L779-780 | 01:00:54-01:01:02 | ENTITY (export regions) | T076 | "Middle East and West Asia as well as Southeast Asia and Far East Asia" | MISSING_FROM_STRUCTURED | Same sentence as R155 (12 countries) and R156 (0.5%)
Mapping: M01-M10 equal A5 units U1-U10 in order. Turn for L725-726 resolves to T072 (lines 721-726, Q23 analyst); L798-799 sits in T076 (lines 764-802).
Loop 1 fixes also applied: R236 re-flagged FORWARD_MGMT at T024 (turn table T024/T025 anchors swapped); conflict C3 relabelled as two readings; C5 and C6 turn slips corrected (T054, T032).

## 10B. MISSING_FROM_STRUCTURED (LOOP 2 ADDENDUM, 2026-10-20; source: A5 Role 5 loop 1 finding M-A)
Part 1 (M11-M32): all 22 A5 units V1-V22 were checked against the fulltext line by line. All 22 are real, and no structured row or M01-M10 row holds any of them. Neighbouring rows are named in each note. No unit was a duplicate. Turn numbers follow the audit and the A1 turn map; two speaker notes are marked (M19, M29).
ROW | CC-L | time | type | turn | verbatim unit | A2 flags | note
M11 | CC-L275-276 | 00:13:42-00:13:47 | NUMBER (analyst-stated duration) | T005 (analyst Q01) | normally it doesn't happen that for two consecutive years we have persistent inflation | MISSING_FROM_STRUCTURED, ANALYST_STATED | = A5 V1. minor. R118 (8 quarters, L611) is a different duration
M12 | CC-L319-322 | 00:17:09-00:17:32 | DATE (comparison base) | T008 | weather helped in Q1 ... compared to let's say previous year Q1 | MISSING_FROM_STRUCTURED | = A5 V2. minor; CQ02. R278 is L168, not this unit
M13 | CC-L335-337 | 00:18:30-00:18:43 | NUMBER (unquantified comparative) | T008 | temperature sensitive products ... it is sustained at the same levels as Q1 | MISSING_FROM_STRUCTURED | = A5 V3. minor; CQ02
M14 | CC-L346-349 | 00:19:20-00:19:35 | DATE (analyst horizon) | T011 (analyst Q03) | are we planning further price hikes in 3Q and beyond ... over the next few months | MISSING_FROM_STRUCTURED, ANALYST_STATED | = A5 V4. minor; same class as M09
M15 | CC-L369-371 | 00:21:18-00:21:29 | NUMBER (unquantified comparative) | T014 | village level, farm level procurement prices also increasing | MISSING_FROM_STRUCTURED | = A5 V5. minor; R228/R229 sit at L372-373 and hold the flush hope, not this
M16 | CC-L400-402 | 00:25:12-00:25:34 | NUMBER (unquantified comparative) | T022 (CEO) | our procurement footprint in Karnataka is not significant ... we have some sales volume in Bangalore city now it is significant enough for us | MISSING_FROM_STRUCTURED | = A5 V6. MATERIAL: basis of the R5-M4 fork (Q45, M17, 8A-W). R285 holds only the 1st November date at L400
M17 | CC-L426 | 00:28:12 | NUMBER (unquantified comparative) | T026 | Our yoghurt's contribution share is going up, ice cream's share is going up | MISSING_FROM_STRUCTURED | = A5 V7. minor; R083/R084 hold the premium paneer and ice cream numbers
M18 | CC-L444-451 | 00:29:28-00:29:53 | NUMBER (unquantified comparative) | T028 (Ramani) | farmer metrics very encouraging and very positive: the number of farmers they are adding, the number they are activating, the volume per farmer, the capacity utilization per milk collection center | MISSING_FROM_STRUCTURED, ASR_NAME | = A5 V8. MATERIAL: CQ08; M5 status 'answered'. R086 holds only 7%
M19 | CC-L486-487 | 00:32:27-00:32:34 | QUALIFIER (decline) | T032 (management; L487 is shared with analyst T033, the speaker of this clause is management) | normal crisis is speculative and I do not wish to make any comment | MISSING_FROM_STRUCTURED, MGMT_DECLINE, ASR_GARBLE | = A5 V9. MATERIAL: 6C #2, CQ09, Step 2. R313 (L469) is the earlier decline in the same answer, a separate unit. ASR 'normal crisis' as printed
M20 | CC-L490-491 | 00:32:50-00:32:53 | ENTITY (cooperatives) | T033 (analyst Q10; A1 map puts L491 in T034) | the cooperators in the Southern region, Arvind, Pichaya, and Nandari | MISSING_FROM_STRUCTURED, ASR_NAME, ENTITY_UNRESOLVED | = A5 V10. minor; CQ10. 'Pichaya' unresolved; R188 (Aavin) and R192 (nandini) may be the referents of two names, not asserted
M21 | CC-L510-511 | 00:34:45-00:34:51 | QUALIFIER (data caveat) | T041 | For example, I'm just making it up | MISSING_FROM_STRUCTURED | = A5 V11. MATERIAL: Q21 status, 5B. R319 (L508) holds the 'weighted averages' caveat; this is the next sentence's disclaimer
M22 | CC-L522-524 | 00:36:02-00:36:16 | NUMBER (unquantified; about 0% volume growth) | T041 | except in the case of ghee, we were able to sustain the volume growth in all other both curd and paneer. As far as ghee is concerned you will see that the volume growth has been flat | MISSING_FROM_STRUCTURED | = A5 V12. MATERIAL: CQ12, Q17, 5A row 13, 7A, Q46, brief. R248 (L525) holds only the Q3 bumper forecast
M23 | CC-L527-528 | 00:36:33-00:36:41 | QUALIFIER (data caveat) | T041 | please don't use that graph to calibrate and calculate to that granularity | MISSING_FROM_STRUCTURED | = A5 V13. MATERIAL: 6C #5, CQ12, 4B. R319 and R332 are different caveats (L508, L715)
M24 | CC-L606 | 00:42:45 | FORWARD (conditional) | T049 | If it comes down, well and good actually it is going to be tremendous | MISSING_FROM_STRUCTURED | = A5 V14. minor. R252 (L605) holds the 'not willing to speculate' lead-in
M25 | CC-L612-615 | 00:43:43-00:43:57 | QUALIFIER (decline) | T051 | you are answering questions yourself ... Will it go to 100 rupees per litre ... I don't know | MISSING_FROM_STRUCTURED, MGMT_DECLINE | = A5 V15. MATERIAL: 6C #7, CQ16, 4B. R119 holds the 100 rupees number only
M26 | CC-L616-617 | 00:43:58-00:44:04 | FORWARD (management expectation) | T051 | we also expect that, you know, with such high prices, the farmers should produce more milk and prices should come down | MISSING_FROM_STRUCTURED | = A5 V16. MATERIAL: 6C #16-18; third management statement on the load-bearing Q3 cost row. R253 (L618) is the next sentence
M27 | CC-L623-624 | 00:44:38-00:44:43 | NUMBER (unquantified comparative) | T051 | our consumer prices are at much higher level than it was earlier | MISSING_FROM_STRUCTURED | = A5 V17. minor. R227 is the October statement at L367
M28 | CC-L624 | 00:44:43 | QUALIFIER (decline) | T051 | That's all I can say | MISSING_FROM_STRUCTURED, MGMT_DECLINE | = A5 V18. MATERIAL: 6C #8. R255 (L624) holds the 'prices will come down' clause on the same line
M29 | CC-L696 | 00:51:33 | ENTITY (person name) | T066 per A1 map (the speaker of L696 is Dr. Bridge Mohan, whose T067 starts at L697) | Ramnigaru | MISSING_FROM_STRUCTURED, ASR_NAME | = A5 V19. minor; 0B Unmapped inference. R194 (Ramani) is a different mention at L432
M30 | CC-L703-704 | 00:51:55-00:52:02 | ENTITY (sales channels) | T067 (Dr. Bridge Mohan) | in all the verticals including our integration as well as the outside general trade market | MISSING_FROM_STRUCTURED | = A5 V20. MATERIAL: Q6, Q47, 5A row 17. R291 holds only 'September' at L703
M31 | CC-L705-706 | 00:52:08-00:52:15 | NUMBER (unquantified comparative) | T067 | we have seen that in our PBT ... we have grown significantly during quarter two | MISSING_FROM_STRUCTURED | = A5 V21. minor; CQ21. M07 holds the separate 'strong quarter two' claim (L699-701)
M32 | CC-L784-786 | 01:01:28-01:01:39 | NUMBER (stated number) | T076 | if milk procurement prices go by 11% you can't take up all products by 11% ... I can't increase consumer milk prices by 11 percentage ... milk ... cannot go up by 11% | MISSING_FROM_STRUCTURED | = A5 V22. MATERIAL: 6A, 6D, 8D, brief. R157 (L782) is only the analyst-frame reference

Part 2 (M33-M61): ONE FINAL SWEEP of CC-L130-853 under the A5 class rule (NUMBER = stated number, or stated direction or level of a named metric; FORWARD = expectation, intent or conditional; ENTITY = person, firm, place, channel, pack type; DATE = named period or horizon incl. analyst horizons; QUALIFIER = decline, refusal or data caveat). Every fulltext line was read against R001-R336 and M01-M32. 29 further units found. Clause-level restatements already inside a structured row were not re-added (L706-710 Q3, Q4 and H2 sit in R257/R258; L548 sits with R249; L790 with R063/R158; greeting, programme and narrative lines carry no class unit). MATERIAL only where A4 is seen citing the line (M33, M35, M53) or the unit companions a material one (M39, M47). The A4 citation test does not discriminate on wide cited ranges, so minor is the default.
THIS SWEEP CLOSES THE LEDGER. No further A2 loop is opened for this concall. The ledger is final at 397 rows (336 structured + 61 MISSING_FROM_STRUCTURED, M01-M61).
ROW | CC-L | time | type | turn | verbatim unit | A2 flags | note
M33 | CC-L229-230 | 00:09:16-00:09:23 | NUMBER (unquantified comparative) | T003 | Getaway, in which we now hold 71 percent stake, delivered robust revenue growth during the quarter | MISSING_FROM_STRUCTURED | Closing sweep. MATERIAL: A4 5B row 22 cites CC-L229-230. R050 holds the 71 only
M34 | CC-L296 | 00:15:43 | NUMBER (unquantified comparative) | T006 | As of now in certain areas milk availability has improved | MISSING_FROM_STRUCTURED | Closing sweep. minor. R223 holds only 'may improve after Diwali' on the same line
M35 | CC-L411-412 | 00:26:34-00:26:43 | NUMBER (unquantified direction) | T026 | usually the consumer prices once it goes up at least we have not seen it coming down | MISSING_FROM_STRUCTURED | Closing sweep. MATERIAL: A4 cites CC-L411-418 (one-way price ratchet, 5B, 6A). R237 holds only 'We won't have to'
M36 | CC-L414-415 | 00:26:56-00:27:01 | NUMBER (unquantified comparative) | T026 | we are now cycling all this high levels that are much higher procurement volume level as well as much higher consumer franchise level | MISSING_FROM_STRUCTURED | Closing sweep. minor; premise of the R081/R082 0.7 percent sensitivity
M37 | CC-L419-420 | 00:27:31-00:27:37 | QUALIFIER (data caveat) | T026 | the net revenue reported by the company is a weighted average of the products that we sell and the regions where we sell in | MISSING_FROM_STRUCTURED | Closing sweep. minor; same class as R308/R319 but a different metric statement
M38 | CC-L517-518 | 00:35:29-00:35:35 | QUALIFIER (data caveat) | T041 | there is also timing issue in terms of timing on when we might have taken up the prices | MISSING_FROM_STRUCTURED | Closing sweep. minor; caveat on the near-zero price reading in Q12; R309 is a different caveat (L366)
M39 | CC-L519-522 | 00:35:40-00:36:02 | NUMBER (unquantified direction) | T041 | because the raw milk prices were going up, we took significant price increases in ghee and paneer and curd | MISSING_FROM_STRUCTURED | Closing sweep. MATERIAL: companion of M22 (ghee growth was price-led, 5A row 13 cites CC-L522-531). R320 holds only the 90/95 percent share (L521)
M40 | CC-L528 | 00:36:41 | NUMBER (unquantified direction) | T041 | The general idea is that everything is growing | MISSING_FROM_STRUCTURED | Closing sweep. minor
M41 | CC-L554 | 00:38:40 | FORWARD (management expectation) | T045 | There is humongous headroom for everyone to grow | MISSING_FROM_STRUCTURED | Closing sweep. minor; R249 (L549) holds the neighbouring 'helps drive market penetration'
M42 | CC-L557-558 | 00:38:56-00:39:04 | FORWARD (intent) | T045 | We are sharply focused on a significant leadership position in ... fresh categories, which is buttermilk | MISSING_FROM_STRUCTURED, ASR_GARBLE | Closing sweep. minor; ASR 'in third' precedes 'a significant leadership position' as printed
M43 | CC-L562-563 | 00:39:23-00:39:30 | FORWARD (management expectation) | T045 | we see tremendous potential in fresh category dairy value added products, whether it is curd, bottom milk, paneer | MISSING_FROM_STRUCTURED, ASR_GARBLE | Closing sweep. minor; ASR 'bottom milk' printed for buttermilk
M44 | CC-L574-575 | 00:40:23-00:40:27 | NUMBER (unquantified level; footprint unchanged) | T045 | without expanding geographic footprint which means actually we are going deeper rather than going wider unlike many of our competitors | MISSING_FROM_STRUCTURED | Closing sweep. minor; R109 holds the 14 or 15 percent CAGR at L573; R269 is the later L777 statement
M45 | CC-L578-580 | 00:40:40-00:40:47 | NUMBER (unquantified direction) | T045 | Our existing consumers are buying more and more of our products and our household penetration is improving in the markets where we are operating | MISSING_FROM_STRUCTURED | Closing sweep. minor
M46 | CC-L602 | 00:42:24 | NUMBER (unquantified level) | T049 | we are exiting Q2 in a much stronger position | MISSING_FROM_STRUCTURED | Closing sweep. minor; R251 (L603) holds the 'EBITDA not going to come down' promise
M47 | CC-L662-666 | 00:48:45-00:49:09 | NUMBER (unquantified direction) | T063 | there is a widening supply demand gap ... demand is going strong, the supply is not unfortunately ... the supply is not really growing | MISSING_FROM_STRUCTURED | Closing sweep. MATERIAL: CQ20 '18-month supply gap'. R132 holds only 'last 18 months' at L664
M48 | CC-L670-671 | 00:49:32-00:49:43 | NUMBER (unquantified direction) | T063 | both farmers and producers as well as companies, brands switching more and more towards cow milk | MISSING_FROM_STRUCTURED | Closing sweep. minor; carries working reading B with M04
M49 | CC-L674-676 | 00:49:55-00:50:00 | NUMBER (unquantified direction) | T063 | people are switching to a cheaper cow milk alternative, both production side as well as buying side | MISSING_FROM_STRUCTURED, RESTATED | Closing sweep. minor; restates M48. A page marker sits at L675
M50 | CC-L677 | 00:50:01 | NUMBER (unquantified direction) | T063 | even though production volumes of cow milk is going up | MISSING_FROM_STRUCTURED | Closing sweep. minor; M05 holds the second clause 'cow [milk] is becoming dearer' on the same line
M51 | CC-L678-679 | 00:50:06-00:50:10 | NUMBER (unquantified comparative) | T063 | the total solids level price is almost getting closer to buffalo | MISSING_FROM_STRUCTURED, ASR_GARBLE | Closing sweep. minor; ASR prints 'How milk actually' and 'bubble away'; read as cow milk and buffalo from the L667-686 passage. Reading B support
M52 | CC-L687-688 | 00:50:46-00:50:51 | NUMBER (unquantified direction) | T063 | driven both availability of cow milk also upwards but prices also upwards | MISSING_FROM_STRUCTURED | Closing sweep. minor; M06 sits at L686
M53 | CC-L732-733 | 00:55:52-00:55:58 | NUMBER (unquantified direction) | T073 | the only expense which is going up is the raw material as a percentage [of] revenue | MISSING_FROM_STRUCTURED | Closing sweep. MATERIAL: A4 cites CC-L727-733. R144 holds only the 0.1 percent freight number on L732
M54 | CC-L820-822 | 01:03:48-01:03:58 | NUMBER (unquantified direction) | T078 | we've seen a significant increase in higher protein sort of concentrated feed and the outcome of which we're seeing in terms of the volumes that we procure from individual farmers | MISSING_FROM_STRUCTURED | Closing sweep. minor
M55 | CC-L828-829 | 01:04:37-01:04:44 | NUMBER (unquantified comparative) | T078 | our artificial insemination program is more successful than an average program | MISSING_FROM_STRUCTURED | Closing sweep. minor
M56 | CC-L388 | 00:23:43 | ENTITY (person name, moderator address) | T019 | Mr. Vijay, I would just request you to please come back in the queue | MISSING_FROM_STRUCTURED, ASR_NAME | Closing sweep. minor; the turn table notes the name at T019 but no structured ENTITY row holds it (Mr. Rajat is held in the R204 note)
M57 | CC-L429-430 | 00:28:30-00:28:38 | DATE (analyst period) | T027 (analyst Q08) | last flash season we saw that milk availability itself was a challenge | MISSING_FROM_STRUCTURED, ANALYST_STATED, ASR_GARBLE | Closing sweep. minor; ASR 'flash' printed for flush
M58 | CC-L274-275 | 00:13:37-00:13:42 | DATE (analyst period) | T005 (analyst Q01) | last year also the prices had gone up during the flush season | MISSING_FROM_STRUCTURED, ANALYST_STATED | Closing sweep. minor; pairs with M11
M59 | CC-L280-281 | 00:14:15-00:14:23 | DATE (comparison base) | T006 | the situation is repeating like last year, the prices have gone up in quarter two | MISSING_FROM_STRUCTURED | Closing sweep. minor; R013 holds the 11 percent
M60 | CC-L750-751 | 00:58:13-00:58:16 | DATE (analyst horizon) | T075 (analyst Q24) | do you believe that next quarter, most of it should be to the right | MISSING_FROM_STRUCTURED, ANALYST_STATED | Closing sweep. minor; same class as M09
M61 | CC-L636-637 | 00:46:16-00:46:21 | DATE (analyst horizon) | T055 (analyst Q18) | do you plan to take any price hike in Q3 or you will take a call later on | MISSING_FROM_STRUCTURED, ANALYST_STATED | Closing sweep. minor; R256 (L639) holds the management answer

Loop 2 totals: M11-M32 = 22 (NUMBER 10, ENTITY 3, FORWARD 2, DATE 2, QUALIFIER 5). M33-M61 = 29 (NUMBER 18, FORWARD 3, DATE 5, QUALIFIER 2, ENTITY 1). Addendum total M01-M61 = 61.
