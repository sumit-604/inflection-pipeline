# A2 LEDGER: HFCL Q2 FY27 concall (Role 5 addendum)
Caveat: machine transcript (faster-whisper); speakers inferred; turn mapping by fulltext line is coarse at turn boundaries. Values live in the A1 structured file at each ID.

=== A2 COUNT TEST ===
category: numbers (mgmt+analyst)             grep_count: 166   sweep_count: 166   header_declared: 166   match: yes
category: entities (participants+other)      grep_count: 68   sweep_count: 68   header_declared: 68   match: yes
category: forward_phrases                    grep_count: 112   sweep_count: 112   header_declared: 112   match: yes
category: dates                              grep_count: 46   sweep_count: 46   header_declared: 46   match: yes
category: qualifiers (source+gaps+hedges)    grep_count: 78   sweep_count: 78   header_declared: 78   match: yes
category: turns                              grep_count: 145   sweep_count: 145   header_declared: 145   match: yes
category: partition mgmt_numbers+analyst_figures = 126+40 vs NUMBER 166   match: yes
category: partition participants+other_entities = 20+48 vs 68   match: yes
category: partition source+gaps+hedges = 9+3+66 vs 78   match: yes
category: questions   sweep_count: 54  (analyst turns excl. close/thanks; T018 answer has no recorded question)
category: missing_from_structured   grep_count: 14   sweep_count: 14   match: yes (loop 1, audit M1)
gate_a2: pass
=== END COUNT TEST ===
ids_in_structured: 615 (R 470 + T 145) | ids_referenced_in_ledger: 615 | orphan_ids: [] | match: yes

## 1. PARTICIPANTS (entity rows, both sides)
ROW_ID | category | turn / speaker | A2 flags | cross-ref / note
R168 | participant | turn T001 (MODERATOR) | ASR_GARBLE | 
R169 | participant | turn T001 (MODERATOR) | - | 
R170 | participant | turn T002 (HOST) | - | 
R171 | participant | turn T002 (HOST) | ASR_GARBLE | 
R172 | participant | turn T002 (HOST) | - | 
R173 | participant | turn T002 (HOST) | - | 
R184 | participant | turn T005 (MODERATOR) | - | 
R186 | participant | turn T013 (MODERATOR) | - | 
R195 | participant | turn T020 (MODERATOR) | - | 
R201 | participant | turn T030 (MODERATOR) | - | 
R207 | participant | turn T040 (MODERATOR) | ASR_GARBLE | 
R212 | participant | turn T048 (MODERATOR) | ASR_GARBLE | 
R217 | participant | turn T065 (MODERATOR) | ASR_GARBLE | 
R222 | participant | turn T081 (MODERATOR) | - | 
R225 | participant | turn T091 (MODERATOR) | - | 
R226 | participant | turn T101 (MODERATOR) | - | 
R227 | participant | turn T104 (MODERATOR) | ASR_GARBLE | 
R228 | participant | turn T112 (MODERATOR) | - | 
R229 | participant | turn T118 (MODERATOR) | - | 
R230 | participant | turn T137 (MODERATOR) | ASR_GARBLE | 
Note: all management speech is attributed to MD (inferred). CFO V.R. Jain, CS and IR head are introduced (R171-R173) but have no separate turn. MD Mahendra Nahata present; no MGMT_ABSENCE raised. Unnamed analyst at T126 (~01:10).

## 2. SPEAKER TURNS (145)
TURN_ID | speaker | page | A2 flags | note
T001 | MODERATOR | page 1 | - | opening, disclaimer, hands to host
T002 | HOST (Achal Lohade, Nuwama) | page 1 | - | introduces management
T003 | MD (Mahendra Nahata) | page 1 | - | opening remarks
T004 | UNATTRIBUTED (IR or moderator) | page 2 | - | thanks, Q&A begins
T005 | MODERATOR | page 2 | - | Q&A instructions, introduces Pranav Kshatriya
T006 | ANALYST Pranav Kshatriya | page 2 | - | Q1 hyperscaler share of order book
T007 | MD | page 2 | - | answer
T008 | ANALYST Pranav Kshatriya | page 2 | - | Q2 guidance conservative
T009 | MD | page 2 | - | answer
T010 | ANALYST Pranav Kshatriya | page 2 | - | preform supply follow-up
T011 | MD | page 2 | - | answer
T012 | ANALYST Pranav Kshatriya | page 2 | - | close
T013 | MODERATOR | page 2 | - | introduces Ashutosh Kumar Jha
T014 | ANALYST Ashutosh Kumar Jha | page 2 | - | Q1 margin trajectory
T015 | MD | page 2 | - | answer
T016 | ANALYST Ashutosh Kumar Jha | page 2 | - | Q2 demand and US rates
T017 | MD | page 2 | - | answer
T018 | MD | page 3 | TIMESTAMP_GAP,QUESTION_MISSING | answer to a defence question; question not in transcript (timestamp gap 00:20:00 to 00:20:32)
T019 | ANALYST (unattributed, likely Ashutosh Kumar Jha) | page 3 | - | thanks
T020 | MODERATOR | page 3 | - | introduces Chilmay Sapre
T021 | ANALYST Chilmay Sapre | page 3 | - | Q1 telecom revenue split
T022 | MD | page 3 | - | asks to repeat
T023 | ANALYST Chilmay Sapre | page 3 | - | repeats question
T024 | MD | page 3 | - | split answer and capacity utilisation
T025 | ANALYST Chilmay Sapre | page 3 | - | Q2 preform cost reset
T026 | MD | page 3 | - | answer
T027 | ANALYST Chilmay Sapre | page 3 | - | margin follow-up
T028 | MD | page 3 | - | answer
T029 | ANALYST Chilmay Sapre | page 3 | - | close
T030 | MODERATOR | page 3 | - | introduces Rikin
T031 | ANALYST Rikin | page 3 | - | Q1 OFC three-year view and margin drivers
T032 | MD | page 3 | - | answer
T033 | ANALYST Rikin | page 4 | - | Q2 defence ramp
T034 | MD | page 4 | - | answer
T035 | ANALYST Rikin | page 4 | - | Q3 EPC loss
T036 | MD | page 4 | - | answer
T037 | ANALYST Rikin | page 4 | - | profit timing
T038 | MD | page 4 | - | answer
T039 | ANALYST Rikin | page 4 | - | close
T040 | MODERATOR | page 4 | - | introduces Maarek
T041 | ANALYST Maarek | page 4 | - | Q1 India data centre opportunity
T042 | MD | page 4 | - | answer
T043 | ANALYST Maarek | page 4 | TIMESTAMP_GAP | FY28 guidance question (begins mid-question, gap 00:38:30 to 00:38:51)
T044 | MD | page 4 | - | answer
T045 | ANALYST Maarek | page 5 | - | utilisation
T046 | MD | page 5 | - | answer
T047 | ANALYST Maarek | page 5 | - | close
T048 | MODERATOR | page 5 | - | introduces Kush Tandar
T049 | ANALYST Kush Tandar | page 5 | - | Q1 revenue from 1.1 billion dollar order
T050 | MD | page 5 | - | answer
T051 | ANALYST Kush Tandar | page 5 | - | follow-up
T052 | MD | page 5 | - | answer
T053 | ANALYST Kush Tandar | page 5 | - | Q2 O&M margin
T054 | MD | page 5 | - | answer
T055 | ANALYST Kush Tandar | page 5 | - | Q3 EPC restructuring
T056 | MD | page 5 | - | answer
T057 | ANALYST Kush Tandar | page 5 | - | Q4 capex and debt
T058 | MD | page 5 | - | answer
T059 | ANALYST Kush Tandar | page 5 | - | debt follow-up
T060 | MD | page 5 | - | answer
T061 | ANALYST Kush Tandar | page 5 | - | Q5 any one-time event
T062 | MD | page 5 | - | answer
T063 | ANALYST Kush Tandar | page 5 | - | close
T064 | UNATTRIBUTED | page 5 | - | thanks
T065 | MODERATOR | page 5 | - | introduces Kushi Soni
T066 | ANALYST Kushi Soni | page 5 | - | Q1 preform expansion
T067 | MD | page 5 | - | answer
T068 | ANALYST Kushi Soni | page 5 | - | germanium supply
T069 | MD | page 5 | - | answer
T070 | ANALYST Kushi Soni | page 5 | - | follow-up and MD addition
T071 | ANALYST Kushi Soni | page 5 | - | Q2 volume and pricing trends
T072 | MD | page 5 | - | answer
T073 | MD | page 5 | - | data centre vs telco mix answer
T074 | ANALYST Kushi Soni | page 5 | - | revenue or volume
T075 | MD | page 6 | - | answer
T076 | ANALYST Kushi Soni | page 6 | - | Q2 growth mix
T077 | MD | page 6 | - | answer on fibre types and price
T078 | ANALYST Kushi Soni | page 6 | - | blended price trend
T079 | MD | page 6 | - | answer
T080 | ANALYST Kushi Soni | page 6 | - | close
T081 | MODERATOR | page 6 | - | introduces Debashish Mazumdar
T082 | ANALYST Debashish Mazumdar | page 6 | - | Q1 telecom margin vs peers
T083 | MD | page 6 | TIMESTAMP_GAP | answer (declines to comment on peers; gap 00:54:13 to 00:54:43)
T084 | ANALYST Debashish Mazumdar | page 6 | - | Q2 order book delivery time
T085 | MD | page 6 | - | answer
T086 | ANALYST Debashish Mazumdar | page 6 | - | average 2 years challenge
T087 | MD | page 6 | - | answer
T088 | ANALYST Debashish Mazumdar | page 6 | - | Q3 preform sufficiency
T089 | MD | page 6 | - | answer
T090 | ANALYST Debashish Mazumdar | page 6 | - | close
T091 | MODERATOR | page 6 | - | introduces Sagar Parikh
T092 | ANALYST Sagar Parikh | page 6 | - | Q1 OFC scale next 2-3 years
T093 | MD | page 6 | - | answer
T094 | ANALYST Sagar Parikh | page 7 | - | Q2 visibility vs order book
T095 | MD | page 7 | - | answer
T096 | ANALYST Sagar Parikh | page 7 | - | follow-up
T097 | MD | page 7 | - | answer
T098 | ANALYST Sagar Parikh | page 7 | - | visibility next 2 years
T099 | MD | page 7 | - | answer
T100 | ANALYST Sagar Parikh | page 7 | - | close
T101 | MODERATOR | page 7 | - | introduces Rishabh Vasa
T102 | ANALYST Rishabh Vasa | page 7 | TIMESTAMP_GAP,QUESTION_CUT_OFF | defence gap question (cut off)
T103 | MODERATOR | page 7 | - | participant dropped, next
T104 | MODERATOR | page 7 | - | introduces Akshat Mehta
T105 | ANALYST Akshat Mehta | page 7 | - | Q1 data centre capex
T106 | MD | page 7 | - | answer
T107 | ANALYST Akshat Mehta | page 7 | - | clarifies
T108 | MD | page 7 | - | answer
T109 | ANALYST Akshat Mehta | page 7 | - | Q2 connectivity revenue
T110 | MD | page 7 | - | answer
T111 | ANALYST Akshat Mehta | page 7 | - | close
T112 | MODERATOR | page 7 | - | introduces Smith Gara
T113 | ANALYST Smith Gara | page 7 | - | interconnect revenue question
T114 | MD | page 7 | - | answer
T115 | ANALYST Smith Gara | page 7 | - | quarter 1
T116 | MD | page 7 | - | answer
T117 | ANALYST Smith Gara | page 7 | - | close
T118 | MODERATOR | page 7 | - | introduces Dhruv Sitlani
T119 | ANALYST Dhruv Sitlani | page 7 | - | Q1 volume vs price
T120 | MD | page 7 | - | answer
T121 | ANALYST Dhruv Sitlani | page 7 | - | asks ballpark
T122 | MD | page 7 | - | answer
T123 | ANALYST Dhruv Sitlani | page 7 | - | Q2 connectivity revenue
T124 | MD | page 7 | - | answer
T125 | ANALYST Dhruv Sitlani | page 7 | - | close, moderator introduces next
T126 | ANALYST unnamed participant (~01:10) | page 8 | - | Q1 price pass-through
T127 | MD | page 8 | - | answer
T128 | ANALYST unnamed participant | page 8 | - | preform midterm solution
T129 | MD | page 8 | - | answer
T130 | ANALYST unnamed participant | page 8 | - | follow-up
T131 | MD | page 8 | - | answer
T132 | ANALYST unnamed participant | page 8 | - | connectivity certification
T133 | MD | page 8 | - | answer
T134 | ANALYST unnamed participant | page 8 | - | supply additions and margins
T135 | MD | page 8 | - | answer
T136 | ANALYST unnamed participant | page 8 | - | close
T137 | MODERATOR | page 8 | - | introduces Saket Kapoor
T138 | ANALYST Saket Kapoor | page 8 | - | Q1 key risks, preform and OFC pricing
T139 | MD | page 8 | - | answer germanium
T140 | ANALYST Saket Kapoor | page 8 | - | margin sustainability, US cost of finance
T141 | MD | page 8 | - | answer
T142 | MODERATOR | page 9 | - | last question, contact Amit Agarwal
T143 | MD | page 9 | - | no further questions, email Amit Agarwal
T144 | MODERATOR | page 9 | - | closes call
T145 | MD | page 9 | - | closing thanks and outlook

## 3. QUESTIONS (analyst turns)
Q# | turn | analyst | firm (per entity row) | page | A2 flags | topic
Q01 | T006 | Pranav Kshatriya | MK | page 2 | - | Q1 hyperscaler share of order book
Q02 | T008 | Pranav Kshatriya | MK | page 2 | REPEAT_QUESTION (growth guidance conservative, cf T043) | Q2 guidance conservative
Q03 | T010 | Pranav Kshatriya | MK | page 2 | - | preform supply follow-up
Q04 | T014 | Ashutosh Kumar Jha | Baliyani Asset Management | page 2 | - | Q1 margin trajectory
Q05 | T016 | Ashutosh Kumar Jha | Baliyani Asset Management | page 2 | - | Q2 demand and US rates
Q06 | T021 | Chilmay Sapre | Schonfeld | page 3 | - | Q1 telecom revenue split
Q07 | T023 | Chilmay Sapre | Schonfeld | page 3 | REPEAT_QUESTION (same analyst re-asked T021 at MD request) | repeats question
Q08 | T025 | Chilmay Sapre | Schonfeld | page 3 | - | Q2 preform cost reset
Q09 | T027 | Chilmay Sapre | Schonfeld | page 3 | - | margin follow-up
Q10 | T031 | Rikin | Kapri family office | page 3 | - | Q1 OFC three-year view and margin drivers
Q11 | T033 | Rikin | Kapri family office | page 4 | REPEAT_QUESTION (defence ramp, cf T018,T102) | Q2 defence ramp
Q12 | T035 | Rikin | Kapri family office | page 4 | REPEAT_QUESTION (EPC loss, cf T055) | Q3 EPC loss
Q13 | T037 | Rikin | Kapri family office | page 4 | - | profit timing
Q14 | T041 | Maarek | as spoken | page 4 | - | Q1 India data centre opportunity
Q15 | T043 | Maarek | as spoken | page 4 | REPEAT_QUESTION (FY28 guidance, cf T008) | FY28 guidance question (begins mid-question, gap 00:38:30 to 00:38:51)
Q16 | T045 | Maarek | as spoken | page 5 | - | utilisation
Q17 | T049 | Kush Tandar | May another capital | page 5 | REPEAT_QUESTION (order revenue, cf T094) | Q1 revenue from 1.1 billion dollar order
Q18 | T051 | Kush Tandar | May another capital | page 5 | - | follow-up
Q19 | T053 | Kush Tandar | May another capital | page 5 | - | Q2 O&M margin
Q20 | T055 | Kush Tandar | May another capital | page 5 | REPEAT_QUESTION (EPC restructuring, cf T035) | Q3 EPC restructuring
Q21 | T057 | Kush Tandar | May another capital | page 5 | - | Q4 capex and debt
Q22 | T059 | Kush Tandar | May another capital | page 5 | - | debt follow-up
Q23 | T061 | Kush Tandar | May another capital | page 5 | - | Q5 any one-time event
Q24 | T066 | Kushi Soni | Novama Institutional Equities | page 5 | - | Q1 preform expansion
Q25 | T068 | Kushi Soni | Novama Institutional Equities | page 5 | REPEAT_QUESTION (germanium, cf T138) | germanium supply
Q26 | T070 | Kushi Soni | Novama Institutional Equities | page 5 | - | follow-up and MD addition
Q27 | T071 | Kushi Soni | Novama Institutional Equities | page 5 | - | Q2 volume and pricing trends
Q28 | T074 | Kushi Soni | Novama Institutional Equities | page 5 | - | revenue or volume
Q29 | T076 | Kushi Soni | Novama Institutional Equities | page 6 | - | Q2 growth mix
Q30 | T078 | Kushi Soni | Novama Institutional Equities | page 6 | - | blended price trend
Q31 | T082 | Debashish Mazumdar | shagun capital | page 6 | - | Q1 telecom margin vs peers
Q32 | T084 | Debashish Mazumdar | shagun capital | page 6 | - | Q2 order book delivery time
Q33 | T086 | Debashish Mazumdar | shagun capital | page 6 | REPEAT_QUESTION (order book delivery period, cf T084) | average 2 years challenge
Q34 | T088 | Debashish Mazumdar | shagun capital | page 6 | REPEAT_QUESTION (preform sufficiency, cf T010,T066) | Q3 preform sufficiency
Q35 | T092 | Sagar Parikh | Renaissance asset managers | page 6 | - | Q1 OFC scale next 2-3 years
Q36 | T094 | Sagar Parikh | Renaissance asset managers | page 7 | - | Q2 visibility vs order book
Q37 | T096 | Sagar Parikh | Renaissance asset managers | page 7 | - | follow-up
Q38 | T098 | Sagar Parikh | Renaissance asset managers | page 7 | REPEAT_QUESTION (visibility, cf T094, T084) | visibility next 2 years
Q39 | T102 | Rishabh Vasa | IntSec Securities and Finance Limited | page 7 | REPEAT_QUESTION (defence gap; cut off, cf T033) | defence gap question (cut off)
Q40 | T105 | Akshat Mehta | seven reverse holding | page 7 | - | Q1 data centre capex
Q41 | T107 | Akshat Mehta | seven reverse holding | page 7 | - | clarifies
Q42 | T109 | Akshat Mehta | seven reverse holding | page 7 | - | Q2 connectivity revenue
Q43 | T113 | Smith Gara | RSP and Ventures | page 7 | - | interconnect revenue question
Q44 | T115 | Smith Gara | RSP and Ventures | page 7 | REPEAT_QUESTION (connectivity/interconnect Q1, cf T109) | quarter 1
Q45 | T119 | Dhruv Sitlani | Vyomara Capital | page 7 | REPEAT_QUESTION (volume vs price, cf T071,T078) | Q1 volume vs price
Q46 | T121 | Dhruv Sitlani | Vyomara Capital | page 7 | REPEAT_QUESTION (price/volume ballpark, cf T071,T119) | asks ballpark
Q47 | T123 | Dhruv Sitlani | Vyomara Capital | page 7 | REPEAT_QUESTION (Q2 connectivity revenue, cf T109) | Q2 connectivity revenue
Q48 | T126 | unnamed participant | NOT FOUND | page 8 | REPEAT_QUESTION (price pass-through, cf T025,T071,T078) | Q1 price pass-through
Q49 | T128 | unnamed participant | NOT FOUND | page 8 | REPEAT_QUESTION (preform solution, cf T010,T088) | preform midterm solution
Q50 | T130 | unnamed participant | NOT FOUND | page 8 | - | follow-up
Q51 | T132 | unnamed participant | NOT FOUND | page 8 | - | connectivity certification
Q52 | T134 | unnamed participant | NOT FOUND | page 8 | REPEAT_QUESTION (margins, cf T140) | supply additions and margins
Q53 | T138 | Saket Kapoor | Kapoor company | page 8 | REPEAT_QUESTION (germanium/preform risk, cf T068) | Q1 key risks, preform and OFC pricing
Q54 | T140 | Saket Kapoor | Kapoor company | page 8 | REPEAT_QUESTION (margin sustainability, cf T014,T027) | margin sustainability, US cost of finance

## 4. MANAGEMENT NUMBERS (NUMBER rows in non-analyst turns)
ROW_ID | category | turn / speaker | A2 flags | cross-ref / note
R001 | mgmt_number | turn T003 (MD) | ASR_GARBLE | 
R002 | mgmt_number | turn T003 (MD) | - | 
R003 | mgmt_number | turn T003 (MD) | - | 
R004 | mgmt_number | turn T003 (MD) | - | 
R005 | mgmt_number | turn T003 (MD) | - | 
R006 | mgmt_number | turn T003 (MD) | - | 
R007 | mgmt_number | turn T003 (MD) | - | 
R008 | mgmt_number | turn T003 (MD) | - | 
R009 | mgmt_number | turn T003 (MD) | - | 
R010 | mgmt_number | turn T003 (MD) | ASR_GARBLE | 
R011 | mgmt_number | turn T003 (MD) | - | 
R012 | mgmt_number | turn T003 (MD) | - | 
R013 | mgmt_number | turn T003 (MD) | ASR_GARBLE | 
R014 | mgmt_number | turn T003 (MD) | - | 
R015 | mgmt_number | turn T003 (MD) | - | 
R016 | mgmt_number | turn T003 (MD) | - | 
R017 | mgmt_number | turn T003 (MD) | - | 
R018 | mgmt_number | turn T003 (MD) | - | 
R019 | mgmt_number | turn T003 (MD) | - | 
R020 | mgmt_number | turn T003 (MD) | - | 
R021 | mgmt_number | turn T003 (MD) | - | 
R022 | mgmt_number | turn T003 (MD) | - | 
R023 | mgmt_number | turn T003 (MD) | - | 
R024 | mgmt_number | turn T003 (MD) | - | 
R025 | mgmt_number | turn T003 (MD) | ASR_GARBLE | 
R026 | mgmt_number | turn T003 (MD) | - | 
R027 | mgmt_number | turn T003 (MD) | - | 
R028 | mgmt_number | turn T003 (MD) | - | 
R029 | mgmt_number | turn T003 (MD) | NUMBER_CONFLICT | order book stated 28,900/29,000/28,000/30,000 across speakers; R029/R129 28,900 is MD anchor [R029,R129,R130,R135,R136,R108,R125,R146]
R030 | mgmt_number | turn T003 (MD) | - | 
R031 | mgmt_number | turn T003 (MD) | - | 
R032 | mgmt_number | turn T003 (MD) | - | 
R033 | mgmt_number | turn T003 (MD) | ASR_GARBLE | 
R034 | mgmt_number | turn T003 (MD) | - | 
R035 | mgmt_number | turn T003 (MD) | RESTATED | 1800 crore capex / pending restated [R035,R244,R148]
R036 | mgmt_number | turn T003 (MD) | NUMBER_CONFLICT | aerospace order book 1600 vs 1800 crore [R036,R048,R072]
R037 | mgmt_number | turn T003 (MD) | RESTATED | defence FY27 500 (500-600) aspiration restated [R037,R045,R073,R145,R070]
R038 | mgmt_number | turn T003 (MD) | - | 
R039 | mgmt_number | turn T003 (MD) | - | 
R041 | mgmt_number | turn T007 (MD) | RESTATED | OFC and DCI order book 18,500 crore [R041,R040,R042]
R042 | mgmt_number | turn T007 (MD) | RESTATED | OFC and DCI order book 18,500 crore [R041,R040,R042]
R045 | mgmt_number | turn T018 (MD) | RESTATED | defence FY27 500 (500-600) aspiration restated [R037,R045,R073,R145,R070]
R046 | mgmt_number | turn T018 (MD) | RESTATED | defence 2000 crore next-year restated [R046,R049,R141]
R047 | mgmt_number | turn T018 (MD) | NUMBER_CONFLICT | defence 5000 crore horizon: three years (R047) vs next two years (R142,R143) [R047,R142,R143]
R048 | mgmt_number | turn T018 (MD) | NUMBER_CONFLICT | aerospace order book 1600 vs 1800 crore [R036,R048,R072]
R049 | mgmt_number | turn T018 (MD) | RESTATED | defence 2000 crore next-year restated [R046,R049,R141]
R050 | mgmt_number | turn T018 (MD) | - | 
R051 | mgmt_number | turn T018 (MD) | - | 
R052 | mgmt_number | turn T018 (MD) | - | 
R055 | mgmt_number | turn T024 (MD) | - | 
R056 | mgmt_number | turn T024 (MD) | - | 
R057 | mgmt_number | turn T024 (MD) | - | 
R058 | mgmt_number | turn T024 (MD) | - | 
R059 | mgmt_number | turn T024 (MD) | - | 
R060 | mgmt_number | turn T026 (MD) | - | 
R061 | mgmt_number | turn T026 (MD) | - | 
R062 | mgmt_number | turn T032 (MD) | - | 
R063 | mgmt_number | turn T032 (MD) | ASR_GARBLE,NUMBER_CONFLICT | capacity step target 63m vs 43m vs 53m fibre km [R063,R064,R118,R140]
R064 | mgmt_number | turn T032 (MD) | NUMBER_CONFLICT | capacity step target 63m vs 43m vs 53m fibre km [R063,R064,R118,R140]
R065 | mgmt_number | turn T032 (MD) | RESTATED | connectivity FY27 800 crore restated [R065,R067,R154,R157]
R066 | mgmt_number | turn T032 (MD) | - | 
R067 | mgmt_number | turn T032 (MD) | RESTATED | connectivity FY27 800 crore restated [R065,R067,R154,R157]
R068 | mgmt_number | turn T032 (MD) | - | 
R072 | mgmt_number | turn T034 (MD) | ASR_GARBLE,NUMBER_CONFLICT | aerospace order book 1600 vs 1800 crore [R036,R048,R072]
R073 | mgmt_number | turn T034 (MD) | RESTATED | defence FY27 500 (500-600) aspiration restated [R037,R045,R073,R145,R070]
R074 | mgmt_number | turn T036 (MD) | ASR_GARBLE,NUMBER_CONFLICT | EPC loss 121 (as spoken) and 7500 ceiling (as spoken) implausible; verify
R075 | mgmt_number | turn T036 (MD) | ASR_GARBLE,NUMBER_CONFLICT | 
R076 | mgmt_number | turn T042 (MD) | - | 
R077 | mgmt_number | turn T042 (MD) | - | 
R078 | mgmt_number | turn T042 (MD) | - | 
R079 | mgmt_number | turn T042 (MD) | - | 
R080 | mgmt_number | turn T042 (MD) | - | 
R081 | mgmt_number | turn T042 (MD) | - | 
R082 | mgmt_number | turn T044 (MD) | - | 
R083 | mgmt_number | turn T046 (MD) | - | 
R084 | mgmt_number | turn T046 (MD) | - | 
R089 | mgmt_number | turn T054 (MD) | - | 
R094 | mgmt_number | turn T067 (MD) | - | 
R095 | mgmt_number | turn T067 (MD) | ASR_GARBLE | 
R096 | mgmt_number | turn T073 (MD) | - | 
R097 | mgmt_number | turn T073 (MD) | - | 
R099 | mgmt_number | turn T077 (MD) | - | 
R100 | mgmt_number | turn T077 (MD) | - | 
R101 | mgmt_number | turn T077 (MD) | ASR_GARBLE | 
R102 | mgmt_number | turn T077 (MD) | ASR_GARBLE | 
R103 | mgmt_number | turn T079 (MD) | - | 
R109 | mgmt_number | turn T085 (MD) | - | 
R110 | mgmt_number | turn T085 (MD) | - | 
R111 | mgmt_number | turn T085 (MD) | - | 
R112 | mgmt_number | turn T087 (MD) | - | 
R116 | mgmt_number | turn T089 (MD) | - | 
R117 | mgmt_number | turn T093 (MD) | - | 
R118 | mgmt_number | turn T093 (MD) | NUMBER_CONFLICT | capacity step target 63m vs 43m vs 53m fibre km [R063,R064,R118,R140]
R119 | mgmt_number | turn T093 (MD) | ASR_GARBLE,NUMBER_CONFLICT | OFC illustrative revenue arithmetic garbled (89000/9000/1670/500 vs 10,000 total); verify against audio [R119,R120,R121,R122]
R120 | mgmt_number | turn T093 (MD) | ASR_GARBLE,NUMBER_CONFLICT | OFC illustrative revenue arithmetic garbled (89000/9000/1670/500 vs 10,000 total); verify against audio [R119,R120,R121,R122]
R121 | mgmt_number | turn T093 (MD) | ASR_GARBLE,NUMBER_CONFLICT | OFC illustrative revenue arithmetic garbled (89000/9000/1670/500 vs 10,000 total); verify against audio [R119,R120,R121,R122]
R122 | mgmt_number | turn T093 (MD) | ASR_GARBLE,NUMBER_CONFLICT | OFC illustrative revenue arithmetic garbled (89000/9000/1670/500 vs 10,000 total); verify against audio [R119,R120,R121,R122]
R123 | mgmt_number | turn T093 (MD) | ASR_GARBLE | 
R124 | mgmt_number | turn T093 (MD) | - | 
R128 | mgmt_number | turn T095 (MD) | - | 
R129 | mgmt_number | turn T095 (MD) | NUMBER_CONFLICT | order book stated 28,900/29,000/28,000/30,000 across speakers; R029/R129 28,900 is MD anchor [R029,R129,R130,R135,R136,R108,R125,R146]
R130 | mgmt_number | turn T095 (MD) | NUMBER_CONFLICT | order book stated 28,900/29,000/28,000/30,000 across speakers; R029/R129 28,900 is MD anchor [R029,R129,R130,R135,R136,R108,R125,R146]
R131 | mgmt_number | turn T095 (MD) | NUMBER_CONFLICT | quarter orders: 3000 added (R132) vs 5500 received (R133,R139); 2500 delivered; 26000 to 28900 needs 5500 [R131,R132,R133,R139,R137,R138]
R132 | mgmt_number | turn T095 (MD) | ASR_GARBLE,NUMBER_CONFLICT | quarter orders: 3000 added (R132) vs 5500 received (R133,R139); 2500 delivered; 26000 to 28900 needs 5500 [R131,R132,R133,R139,R137,R138]
R133 | mgmt_number | turn T095 (MD) | NUMBER_CONFLICT | quarter orders: 3000 added (R132) vs 5500 received (R133,R139); 2500 delivered; 26000 to 28900 needs 5500 [R131,R132,R133,R139,R137,R138]
R135 | mgmt_number | turn T097 (MD) | NUMBER_CONFLICT | order book stated 28,900/29,000/28,000/30,000 across speakers; R029/R129 28,900 is MD anchor [R029,R129,R130,R135,R136,R108,R125,R146]
R136 | mgmt_number | turn T097 (MD) | NUMBER_CONFLICT | order book stated 28,900/29,000/28,000/30,000 across speakers; R029/R129 28,900 is MD anchor [R029,R129,R130,R135,R136,R108,R125,R146]
R137 | mgmt_number | turn T097 (MD) | NUMBER_CONFLICT | quarter orders: 3000 added (R132) vs 5500 received (R133,R139); 2500 delivered; 26000 to 28900 needs 5500 [R131,R132,R133,R139,R137,R138]
R138 | mgmt_number | turn T097 (MD) | ASR_GARBLE,NUMBER_CONFLICT | quarter orders: 3000 added (R132) vs 5500 received (R133,R139); 2500 delivered; 26000 to 28900 needs 5500 [R131,R132,R133,R139,R137,R138]
R139 | mgmt_number | turn T097 (MD) | NUMBER_CONFLICT | quarter orders: 3000 added (R132) vs 5500 received (R133,R139); 2500 delivered; 26000 to 28900 needs 5500 [R131,R132,R133,R139,R137,R138]
R141 | mgmt_number | turn T099 (MD) | RESTATED | defence 2000 crore next-year restated [R046,R049,R141]
R142 | mgmt_number | turn T099 (MD) | NUMBER_CONFLICT | defence 5000 crore horizon: three years (R047) vs next two years (R142,R143) [R047,R142,R143]
R143 | mgmt_number | turn T099 (MD) | ASR_GARBLE,NUMBER_CONFLICT | defence 5000 crore horizon: three years (R047) vs next two years (R142,R143) [R047,R142,R143]
R148 | mgmt_number | turn T106 (MD) | RESTATED | 1800 crore capex / pending restated [R035,R244,R148]
R149 | mgmt_number | turn T108 (MD) | HEDGED_NUMBER | 
R151 | mgmt_number | turn T110 (MD) | ASR_GARBLE,NUMBER_CONFLICT | Q2 connectivity revenue: 200-300 / 300+ vs 300 crore [R151,R152,R153]
R152 | mgmt_number | turn T110 (MD) | ASR_GARBLE,NUMBER_CONFLICT | Q2 connectivity revenue: 200-300 / 300+ vs 300 crore [R151,R152,R153]
R153 | mgmt_number | turn T114 (MD) | NUMBER_CONFLICT | Q2 connectivity revenue: 200-300 / 300+ vs 300 crore [R151,R152,R153]
R154 | mgmt_number | turn T114 (MD) | RESTATED | connectivity FY27 800 crore restated [R065,R067,R154,R157]
R155 | mgmt_number | turn T116 (MD) | ZERO_STANDING | Q1 FY27 connectivity revenue nil; template signal
R157 | mgmt_number | turn T124 (MD) | RESTATED | connectivity FY27 800 crore restated [R065,R067,R154,R157]
R158 | mgmt_number | turn T124 (MD) | - | 
R160 | mgmt_number | turn T127 (MD) | - | 
R164 | mgmt_number | turn T135 (MD) | - | 
R165 | mgmt_number | turn T135 (MD) | ASR_GARBLE | 
R166 | mgmt_number | turn T135 (MD) | - | 

## 5. ANALYST FIGURES (NUMBER rows in analyst turns or analyst-labelled)
ROW_ID | category | turn / speaker | A2 flags | cross-ref / note
R040 | analyst_figure | turn T006 (ANALYST Pranav Kshatriya) | ANALYST_FIGURE,RESTATED | OFC and DCI order book 18,500 crore [R041,R040,R042]
R043 | analyst_figure | turn T008 (ANALYST Pranav Kshatriya) | ANALYST_FIGURE | 
R044 | analyst_figure | turn T014 (ANALYST Ashutosh Kumar Jha) | ANALYST_FIGURE | 
R053 | analyst_figure | turn T023 (ANALYST Chilmay Sapre) | ANALYST_FIGURE,ASR_GARBLE | 
R054 | analyst_figure | turn T023 (ANALYST Chilmay Sapre) | ANALYST_FIGURE | 
R069 | analyst_figure | turn T033 (ANALYST Rikin) | ANALYST_FIGURE | 
R070 | analyst_figure | turn T033 (ANALYST Rikin) | ANALYST_FIGURE,RESTATED | defence FY27 500 (500-600) aspiration restated [R037,R045,R073,R145,R070]
R071 | analyst_figure | turn T033 (ANALYST Rikin) | ANALYST_FIGURE | 
R085 | analyst_figure | turn T047 (ANALYST Maarek) | ANALYST_FIGURE | 
R086 | analyst_figure | turn T049 (ANALYST Kush Tandar) | ANALYST_FIGURE | 
R087 | analyst_figure | turn T049 (ANALYST Kush Tandar) | ANALYST_FIGURE | 
R088 | analyst_figure | turn T053 (ANALYST Kush Tandar) | ANALYST_FIGURE | 
R090 | analyst_figure | turn T057 (ANALYST Kush Tandar) | ANALYST_FIGURE | 
R091 | analyst_figure | turn T066 (ANALYST Kushi Soni) | ANALYST_FIGURE | 
R092 | analyst_figure | turn T066 (ANALYST Kushi Soni) | ANALYST_FIGURE | 
R093 | analyst_figure | turn T066 (ANALYST Kushi Soni) | ANALYST_FIGURE | 
R098 | analyst_figure | turn T076 (ANALYST Kushi Soni) | ANALYST_FIGURE | 
R104 | analyst_figure | turn T082 (ANALYST Debashish Mazumdar) | ANALYST_FIGURE | 
R105 | analyst_figure | turn T082 (ANALYST Debashish Mazumdar) | ANALYST_FIGURE | 
R106 | analyst_figure | turn T082 (ANALYST Debashish Mazumdar) | ANALYST_FIGURE | 
R107 | analyst_figure | turn T082 (ANALYST Debashish Mazumdar) | ANALYST_FIGURE | 
R108 | analyst_figure | turn T084 (ANALYST Debashish Mazumdar) | ANALYST_FIGURE,ASR_GARBLE,NUMBER_CONFLICT | order book stated 28,900/29,000/28,000/30,000 across speakers; R029/R129 28,900 is MD anchor [R029,R129,R130,R135,R136,R108,R125,R146]
R113 | analyst_figure | turn T088 (ANALYST Debashish Mazumdar) | ANALYST_FIGURE | 
R114 | analyst_figure | turn T088 (ANALYST Debashish Mazumdar) | ANALYST_FIGURE | 
R115 | analyst_figure | turn T088 (ANALYST Debashish Mazumdar) | ANALYST_FIGURE | 
R125 | analyst_figure | turn T094 (ANALYST Sagar Parikh) | ANALYST_FIGURE,NUMBER_CONFLICT | order book stated 28,900/29,000/28,000/30,000 across speakers; R029/R129 28,900 is MD anchor [R029,R129,R130,R135,R136,R108,R125,R146]
R126 | analyst_figure | turn T094 (ANALYST Sagar Parikh) | ANALYST_FIGURE | 
R127 | analyst_figure | turn T094 (ANALYST Sagar Parikh) | ANALYST_FIGURE | 
R134 | analyst_figure | turn T096 (ANALYST Sagar Parikh) | ANALYST_FIGURE,ASR_GARBLE | 
R140 | analyst_figure | turn T098 (ANALYST Sagar Parikh) | ANALYST_FIGURE,ASR_GARBLE,NUMBER_CONFLICT | capacity step target 63m vs 43m vs 53m fibre km [R063,R064,R118,R140]
R144 | analyst_figure | turn T102 (ANALYST Rishabh Vasa) | ANALYST_FIGURE | 
R145 | analyst_figure | turn T102 (ANALYST Rishabh Vasa) | ANALYST_FIGURE,RESTATED | defence FY27 500 (500-600) aspiration restated [R037,R045,R073,R145,R070]
R146 | analyst_figure | turn T105 (ANALYST Akshat Mehta) | ANALYST_FIGURE,NUMBER_CONFLICT | order book stated 28,900/29,000/28,000/30,000 across speakers; R029/R129 28,900 is MD anchor [R029,R129,R130,R135,R136,R108,R125,R146]
R147 | analyst_figure | turn T105 (ANALYST Akshat Mehta) | ANALYST_FIGURE | 
R150 | analyst_figure | turn T109 (ANALYST Akshat Mehta) | ANALYST_FIGURE | 
R156 | analyst_figure | turn T119 (ANALYST Dhruv Sitlani) | ANALYST_FIGURE | 
R159 | analyst_figure | turn T126 (ANALYST unnamed participant) | ANALYST_FIGURE | 
R161 | analyst_figure | turn T134 (ANALYST unnamed participant) | ANALYST_FIGURE | 
R162 | analyst_figure | turn T134 (ANALYST unnamed participant) | ANALYST_FIGURE | 
R163 | analyst_figure | turn T134 (ANALYST unnamed participant) | ANALYST_FIGURE | 

## 6. OTHER ENTITIES (non-participant)
ROW_ID | category | turn / speaker | A2 flags | cross-ref / note
R167 | entity | turn T001 (MODERATOR) | - | 
R174 | entity | turn T003 (MD) | - | 
R175 | entity | turn T003 (MD) | - | 
R176 | entity | turn T003 (MD) | - | 
R177 | entity | turn T003 (MD) | - | 
R178 | entity | turn T003 (MD) | - | 
R179 | entity | turn T003 (MD) | - | 
R180 | entity | turn T003 (MD) | - | 
R181 | entity | turn T003 (MD) | - | 
R182 | entity | turn T003 (MD) | - | 
R183 | entity | turn T003 (MD) | - | 
R185 | entity | turn T006 (ANALYST Pranav Kshatriya) | ASR_GARBLE | 
R187 | entity | turn T017 (MD) | - | 
R188 | entity | turn T017 (MD) | - | 
R189 | entity | turn T017 (MD) | - | 
R190 | entity | turn T017 (MD) | - | 
R191 | entity | turn T018 (MD) | - | 
R192 | entity | turn T018 (MD) | ASR_GARBLE | 
R193 | entity | turn T018 (MD) | ASR_GARBLE | 
R194 | entity | turn T018 (MD) | - | 
R196 | entity | turn T024 (MD) | - | 
R197 | entity | turn T024 (MD) | - | 
R198 | entity | turn T024 (MD) | - | 
R199 | entity | turn T024 (MD) | ASR_GARBLE | 
R200 | entity | turn T024 (MD) | - | 
R202 | entity | turn T036 (MD) | - | 
R203 | entity | turn T036 (MD) | - | 
R204 | entity | turn T036 (MD) | - | 
R205 | entity | turn T036 (MD) | ASR_GARBLE | 
R206 | entity | turn T036 (MD) | - | 
R208 | entity | turn T042 (MD) | - | 
R209 | entity | turn T042 (MD) | ASR_GARBLE | 
R210 | entity | turn T042 (MD) | ASR_GARBLE | 
R211 | entity | turn T042 (MD) | ASR_GARBLE | 
R213 | entity | turn T053 (ANALYST Kush Tandar) | - | 
R214 | entity | turn T055 (ANALYST Kush Tandar) | - | 
R215 | entity | turn T056 (MD) | - | 
R216 | entity | turn T056 (MD) | - | 
R218 | entity | turn T068 (ANALYST Kushi Soni) | - | 
R219 | entity | turn T069 (MD) | - | 
R220 | entity | turn T077 (MD) | ASR_GARBLE | 
R221 | entity | turn T077 (MD) | ASR_GARBLE | 
R223 | entity | turn T082 (ANALYST Debashish Mazumdar) | - | 
R224 | entity | turn T082 (ANALYST Debashish Mazumdar) | ASR_GARBLE | 
R231 | entity | turn T141 (MD) | - | 
R232 | entity | turn T141 (MD) | - | 
R233 | entity | turn T141 (MD) | - | 
R234 | entity | turn T142 (MODERATOR) | - | 

## 7. FORWARD-COMMITMENT PHRASES
ROW_ID | category | turn / speaker | A2 flags | cross-ref / note
R235 | forward_phrase | turn T003 (MD) | - | 
R236 | forward_phrase | turn T003 (MD) | - | 
R237 | forward_phrase | turn T003 (MD) | - | 
R238 | forward_phrase | turn T003 (MD) | - | 
R239 | forward_phrase | turn T003 (MD) | - | 
R240 | forward_phrase | turn T003 (MD) | - | 
R241 | forward_phrase | turn T003 (MD) | - | 
R242 | forward_phrase | turn T003 (MD) | - | 
R243 | forward_phrase | turn T003 (MD) | - | 
R244 | forward_phrase | turn T003 (MD) | RESTATED | 1800 crore capex / pending restated [R035,R244,R148]
R245 | forward_phrase | turn T003 (MD) | - | 
R246 | forward_phrase | turn T003 (MD) | - | 
R247 | forward_phrase | turn T003 (MD) | - | 
R248 | forward_phrase | turn T003 (MD) | - | 
R249 | forward_phrase | turn T003 (MD) | - | 
R250 | forward_phrase | turn T009 (MD) | - | 
R251 | forward_phrase | turn T011 (MD) | - | 
R252 | forward_phrase | turn T015 (MD) | - | 
R253 | forward_phrase | turn T015 (MD) | - | 
R254 | forward_phrase | turn T017 (MD) | - | 
R255 | forward_phrase | turn T017 (MD) | - | 
R256 | forward_phrase | turn T017 (MD) | - | 
R257 | forward_phrase | turn T017 (MD) | - | 
R258 | forward_phrase | turn T017 (MD) | - | 
R259 | forward_phrase | turn T017 (MD) | - | 
R260 | forward_phrase | turn T017 (MD) | - | 
R261 | forward_phrase | turn T018 (MD) | - | 
R262 | forward_phrase | turn T018 (MD) | - | 
R263 | forward_phrase | turn T018 (MD) | - | 
R264 | forward_phrase | turn T018 (MD) | - | 
R265 | forward_phrase | turn T018 (MD) | - | 
R266 | forward_phrase | turn T018 (MD) | - | 
R267 | forward_phrase | turn T018 (MD) | - | 
R268 | forward_phrase | turn T018 (MD) | - | 
R269 | forward_phrase | turn T018 (MD) | - | 
R270 | forward_phrase | turn T018 (MD) | - | 
R271 | forward_phrase | turn T018 (MD) | - | 
R272 | forward_phrase | turn T018 (MD) | - | 
R273 | forward_phrase | turn T026 (MD) | - | 
R274 | forward_phrase | turn T026 (MD) | ASR_GARBLE | 
R275 | forward_phrase | turn T028 (MD) | - | 
R276 | forward_phrase | turn T032 (MD) | - | 
R277 | forward_phrase | turn T032 (MD) | - | 
R278 | forward_phrase | turn T032 (MD) | - | 
R279 | forward_phrase | turn T032 (MD) | - | 
R280 | forward_phrase | turn T032 (MD) | - | 
R281 | forward_phrase | turn T032 (MD) | - | 
R282 | forward_phrase | turn T032 (MD) | - | 
R283 | forward_phrase | turn T032 (MD) | - | 
R284 | forward_phrase | turn T032 (MD) | - | 
R285 | forward_phrase | turn T032 (MD) | - | 
R286 | forward_phrase | turn T032 (MD) | - | 
R287 | forward_phrase | turn T034 (MD) | - | 
R288 | forward_phrase | turn T034 (MD) | - | 
R289 | forward_phrase | turn T034 (MD) | - | 
R290 | forward_phrase | turn T034 (MD) | - | 
R291 | forward_phrase | turn T034 (MD) | - | 
R292 | forward_phrase | turn T036 (MD) | - | 
R293 | forward_phrase | turn T036 (MD) | - | 
R294 | forward_phrase | turn T036 (MD) | - | 
R295 | forward_phrase | turn T036 (MD) | - | 
R296 | forward_phrase | turn T036 (MD) | ASR_GARBLE | 
R297 | forward_phrase | turn T038 (MD) | - | 
R298 | forward_phrase | turn T042 (MD) | - | 
R299 | forward_phrase | turn T042 (MD) | - | 
R300 | forward_phrase | turn T042 (MD) | - | 
R301 | forward_phrase | turn T042 (MD) | - | 
R302 | forward_phrase | turn T044 (MD) | - | 
R303 | forward_phrase | turn T044 (MD) | - | 
R304 | forward_phrase | turn T044 (MD) | - | 
R305 | forward_phrase | turn T044 (MD) | - | 
R306 | forward_phrase | turn T044 (MD) | - | 
R307 | forward_phrase | turn T056 (MD) | - | 
R308 | forward_phrase | turn T056 (MD) | - | 
R309 | forward_phrase | turn T058 (MD) | - | 
R310 | forward_phrase | turn T060 (MD) | - | 
R311 | forward_phrase | turn T062 (MD) | - | 
R312 | forward_phrase | turn T067 (MD) | - | 
R313 | forward_phrase | turn T067 (MD) | - | 
R314 | forward_phrase | turn T067 (MD) | - | 
R315 | forward_phrase | turn T069 (MD) | - | 
R316 | forward_phrase | turn T070 (ANALYST Kushi Soni) | - | 
R317 | forward_phrase | turn T072 (MD) | - | 
R318 | forward_phrase | turn T072 (MD) | - | 
R319 | forward_phrase | turn T072 (MD) | - | 
R320 | forward_phrase | turn T079 (MD) | - | 
R321 | forward_phrase | turn T085 (MD) | - | 
R322 | forward_phrase | turn T087 (MD) | - | 
R323 | forward_phrase | turn T089 (MD) | - | 
R324 | forward_phrase | turn T093 (MD) | - | 
R325 | forward_phrase | turn T093 (MD) | - | 
R326 | forward_phrase | turn T095 (MD) | - | 
R327 | forward_phrase | turn T097 (MD) | - | 
R328 | forward_phrase | turn T099 (MD) | - | 
R329 | forward_phrase | turn T099 (MD) | - | 
R330 | forward_phrase | turn T099 (MD) | - | 
R331 | forward_phrase | turn T120 (MD) | - | 
R332 | forward_phrase | turn T120 (MD) | - | 
R333 | forward_phrase | turn T124 (MD) | - | 
R334 | forward_phrase | turn T127 (MD) | - | 
R335 | forward_phrase | turn T131 (MD) | - | 
R336 | forward_phrase | turn T135 (MD) | - | 
R337 | forward_phrase | turn T135 (MD) | - | 
R338 | forward_phrase | turn T135 (MD) | - | 
R339 | forward_phrase | turn T135 (MD) | - | 
R340 | forward_phrase | turn T139 (MD) | - | 
R341 | forward_phrase | turn T141 (MD) | - | 
R342 | forward_phrase | turn T141 (MD) | - | 
R343 | forward_phrase | turn T141 (MD) | - | 
R344 | forward_phrase | turn T143 (MD) | - | 
R345 | forward_phrase | turn T145 (MD) | - | 
R346 | forward_phrase | turn T145 (MD) | - | 

## 8. HEDGE PHRASES (qualifiers excl. source status and gaps)
ROW_ID | category | turn / speaker | A2 flags | cross-ref / note
R402 | hedge | turn T003 (MD) | - | 
R403 | hedge | turn T003 (MD) | - | 
R404 | hedge | turn T003 (MD) | - | 
R405 | hedge | turn T003 (MD) | ASR_GARBLE | 
R406 | hedge | turn T003 (MD) | - | 
R407 | hedge | turn T003 (MD) | - | 
R408 | hedge | turn T003 (MD) | - | 
R409 | hedge | turn T003 (MD) | - | 
R410 | hedge | turn T003 (MD) | - | 
R411 | hedge | turn T003 (MD) | - | 
R412 | hedge | turn T003 (MD) | ASR_GARBLE | 
R413 | hedge | turn T007 (MD) | - | 
R414 | hedge | turn T007 (MD) | - | 
R415 | hedge | turn T007 (MD) | - | 
R416 | hedge | turn T008 (ANALYST Pranav Kshatriya) | - | 
R417 | hedge | turn T015 (MD) | - | 
R418 | hedge | turn T017 (MD) | - | 
R419 | hedge | turn T017 (MD) | - | 
R421 | hedge | turn T024 (MD) | - | 
R422 | hedge | turn T024 (MD) | - | 
R423 | hedge | turn T024 (MD) | - | 
R424 | hedge | turn T024 (MD) | - | 
R425 | hedge | turn T032 (MD) | - | 
R426 | hedge | turn T033 (ANALYST Rikin) | - | 
R427 | hedge | turn T034 (MD) | ASR_GARBLE | 
R428 | hedge | turn T036 (MD) | ASR_GARBLE | 
R429 | hedge | turn T042 (MD) | - | 
R430 | hedge | turn T042 (MD) | - | 
R432 | hedge | turn T044 (MD) | - | 
R433 | hedge | turn T044 (MD) | - | 
R434 | hedge | turn T044 (MD) | - | 
R435 | hedge | turn T050 (MD) | - | 
R436 | hedge | turn T054 (MD) | - | 
R437 | hedge | turn T054 (MD) | - | 
R438 | hedge | turn T056 (MD) | - | 
R439 | hedge | turn T067 (MD) | - | 
R440 | hedge | turn T067 (MD) | ASR_GARBLE | 
R441 | hedge | turn T070 (ANALYST Kushi Soni) | - | 
R442 | hedge | turn T072 (MD) | - | 
R443 | hedge | turn T073 (MD) | - | 
R444 | hedge | turn T076 (ANALYST Kushi Soni) | - | 
R445 | hedge | turn T079 (MD) | - | 
R447 | hedge | turn T083 (MD) | - | 
R448 | hedge | turn T085 (MD) | - | 
R449 | hedge | turn T086 (ANALYST Debashish Mazumdar) | - | 
R450 | hedge | turn T093 (MD) | - | 
R451 | hedge | turn T093 (MD) | - | 
R452 | hedge | turn T093 (MD) | - | 
R453 | hedge | turn T093 (MD) | ASR_GARBLE | 
R454 | hedge | turn T097 (MD) | - | 
R455 | hedge | turn T108 (MD) | HEDGED_NUMBER | 
R456 | hedge | turn T108 (MD) | - | 
R457 | hedge | turn T110 (MD) | - | 
R458 | hedge | turn T110 (MD) | - | 
R459 | hedge | turn T116 (MD) | - | 
R460 | hedge | turn T122 (MD) | - | 
R461 | hedge | turn T126 (ANALYST unnamed participant) | - | 
R462 | hedge | turn T127 (MD) | - | 
R463 | hedge | turn T127 (MD) | - | 
R464 | hedge | turn T129 (MD) | - | 
R465 | hedge | turn T133 (MD) | - | 
R466 | hedge | turn T135 (MD) | ASR_GARBLE | 
R467 | hedge | turn T135 (MD) | - | 
R468 | hedge | turn T135 (MD) | ASR_GARBLE | 
R469 | hedge | turn T139 (MD) | - | 
R470 | hedge | turn T141 (MD) | - | 

## 9. SOURCE STATUS AND DISCLAIMER QUALIFIERS
ROW_ID | category | turn / speaker | A2 flags | cross-ref / note
R393 | source_status | turn PRE (PREAMBLE) | - | 
R394 | source_status | turn PRE (PREAMBLE) | - | 
R395 | source_status | turn PRE (PREAMBLE) | - | 
R396 | source_status | turn PRE (PREAMBLE) | - | 
R397 | source_status | turn PRE (PREAMBLE) | - | 
R398 | source_status | turn T001 (MODERATOR) | - | 
R399 | source_status | turn T001 (MODERATOR) | - | 
R400 | source_status | turn T001 (MODERATOR) | - | 
R401 | source_status | turn T003 (MD) | ASR_GARBLE,DATE_ANOMALY | half-year end spoken as September 13 vs Sept 30 convention

## 10. TIMESTAMP GAPS
ROW_ID | category | turn / speaker | A2 flags | cross-ref / note
R420 | timestamp_gap | turn T018 (MD) | MISSING_QUESTION,TIMESTAMP_GAP | defence question absent; answer T018
R431 | timestamp_gap | turn T043 (ANALYST Maarek) | TIMESTAMP_GAP | FY28 guidance question starts mid-sentence (T043)
R446 | timestamp_gap | turn T083 (MD) | TIMESTAMP_GAP | peer margin answer (T083)

## 11. DATES
ROW_ID | category | turn / speaker | A2 flags | cross-ref / note
R347 | date | turn PRE (PREAMBLE) | - | 
R348 | date | turn T001 (MODERATOR) | - | 
R349 | date | turn T003 (MD) | ASR_GARBLE | 
R350 | date | turn T003 (MD) | - | 
R351 | date | turn T003 (MD) | - | 
R352 | date | turn T003 (MD) | - | 
R353 | date | turn T003 (MD) | - | 
R354 | date | turn T003 (MD) | - | 
R355 | date | turn T003 (MD) | - | 
R356 | date | turn T003 (MD) | - | 
R357 | date | turn T003 (MD) | - | 
R358 | date | turn T003 (MD) | - | 
R359 | date | turn T003 (MD) | ASR_GARBLE | 
R360 | date | turn T003 (MD) | - | 
R361 | date | turn T018 (MD) | - | 
R362 | date | turn T018 (MD) | - | 
R363 | date | turn T018 (MD) | - | 
R364 | date | turn T018 (MD) | - | 
R365 | date | turn T018 (MD) | - | 
R366 | date | turn T018 (MD) | - | 
R367 | date | turn T018 (MD) | - | 
R368 | date | turn T018 (MD) | - | 
R369 | date | turn T032 (MD) | - | 
R370 | date | turn T032 (MD) | - | 
R371 | date | turn T032 (MD) | - | 
R372 | date | turn T034 (MD) | - | 
R373 | date | turn T036 (MD) | - | 
R374 | date | turn T036 (MD) | - | 
R375 | date | turn T038 (MD) | - | 
R376 | date | turn T042 (MD) | - | 
R377 | date | turn T042 (MD) | - | 
R378 | date | turn T044 (MD) | ASR_GARBLE | 
R379 | date | turn T044 (MD) | ASR_GARBLE | 
R380 | date | turn T056 (MD) | - | 
R381 | date | turn T056 (MD) | - | 
R382 | date | turn T058 (MD) | - | 
R383 | date | turn T059 (ANALYST Kush Tandar) | - | 
R384 | date | turn T067 (MD) | - | 
R385 | date | turn T067 (MD) | ASR_GARBLE | 
R386 | date | turn T067 (MD) | - | 
R387 | date | turn T070 (ANALYST Kushi Soni) | - | 
R388 | date | turn T072 (MD) | - | 
R389 | date | turn T072 (MD) | - | 
R390 | date | turn T113 (ANALYST Smith Gara) | - | 
R391 | date | turn T113 (ANALYST Smith Gara) | ASR_GARBLE | 
R392 | date | turn T139 (MD) | - | 

## 12. MISSING_FROM_STRUCTURED
ROW_ID | fulltext line | turn / speaker | A2 flags | claim text (verbatim from fulltext)
M01 | C-L238 | T017 (MD) | NUMBER_PERIOD; MISSING_FROM_STRUCTURED | "since last two years": telcos have not been buying much (period)
M02 | C-L275 | T018 (MD) | FORWARD; MISSING_FROM_STRUCTURED | "that revenue also will get consolidated after acquisition being completed", dated by C-L274 "in this quarter itself"; C-L273 pending order of 1800 crores
M03 | C-L432-433 | T036 (MD) | NUMBER; MISSING_FROM_STRUCTURED | "25 different steps"; "25th steps ... goes back to step 0 and then comes back to step 25" (BharatNet bill verification; ASR line break)
M04 | C-L676 | T083 (MD) | FORWARD; MISSING_FROM_STRUCTURED | "talking to international telcos also where we think we'll get some orders"
M05 | C-L700 | T086 (ANALYST Debashish Mazumdar) | NUMBER; ANALYST_FIGURE; ASR_GARBLE; MISSING_FROM_STRUCTURED | "2 years time frame", "10,000 column number" (garbled; analyst challenge on average delivery; line is in T086 text per fulltext 699-701)
M06 | C-L745-746 | T094 (ANALYST Sagar Parikh) | NUMBER; ANALYST_FIGURE; MISSING_FROM_STRUCTURED | "3 year 2 years", "6 7000 crores" (visibility beyond run rate)
M07 | C-L755-756 | T095 (MD) | FORWARD; MISSING_FROM_STRUCTURED | "we will keep on receiving more orders ... orders would be more than the supply we do"; C-L755 "5500 crores or more orders"
M08 | C-L852 | T121 (ANALYST) | NUMBER; ANALYST_FIGURE; MISSING_FROM_STRUCTURED | "50, 50, 60, 40 or 70, 30" ratio ballpark asked; C-L853 MD declines to give a ballpark
M09 | C-L878 | T127 (MD) | NUMBER; MISSING_FROM_STRUCTURED | "short term contract note 4 to 6 points there is no reset clause" (4 to 6 months; R463 holds the qualifier only)
M10 | C-L880-881 | T127 (MD) | NUMBER; MISSING_FROM_STRUCTURED | "four to six months" price always higher; "five year" (contract tenors; ASR garbled)
M11 | C-L980 | T140 (ANALYST) | NUMBER_PERIOD; ANALYST_FIGURE; MISSING_FROM_STRUCTURED | "four to five years" planned data center story
M12 | C-L391 | T033 (ANALYST) | DATE_PERIOD; ANALYST_FIGURE; MISSING_FROM_STRUCTURED | "into 3 or Q4" (period reference); C-L389-392 defence "200 crore quarter", "hundred for the defense business"
M13 | C-L767 | T098 (ANALYST Sagar Parikh) | DATE_PERIOD; ANALYST_FIGURE; MISSING_FROM_STRUCTURED | "next 2 years" visibility; C-L765-766 "25000 crores supply" (likely 2500), "orders of 5500 crores"
M14 | C-L835 | T119 (ANALYST) | DATE_PERIOD; ANALYST_FIGURE; MISSING_FROM_STRUCTURED | "Q3 and Q4" realization vs volume question
