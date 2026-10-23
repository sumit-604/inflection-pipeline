# A2 LEDGER: concall GRWRHITECH q2fy27

ids_in_structured: 419 | ids_referenced_in_ledger: 419 | orphan_ids: [] | match: yes

```
=== A2 COUNT TEST ===
category: participants     grep_count: 11  sweep_count: 11  match: yes   (ENTITY rows naming a person+role: R015,R018,R113,R145,R198,R264,R312,R350,R363,R376,R390; R417 restates Joshi)
category: turns            grep_count: 97  sweep_count: 97  match: yes   (T01-T97 sequential, header says 97)
category: questions        grep_count: 39  sweep_count: 39  match: yes   (analyst-side turns incl. clarifications/comments; 9 analysts)
category: mgmt_numbers     grep_count: 222 sweep_count: 222 match: yes   (grep NUMBER rows = header NUMBER 222)
category: forward_phrases  grep_count: 67  sweep_count: 67  match: yes
category: hedge_qualifiers grep_count: 47  sweep_count: 47  match: yes
category: entities         grep_count: 53  sweep_count: 53  match: yes
category: dates            grep_count: 30  sweep_count: 30  match: yes
row_ids_total              grep_count: 419 sweep_count: 419 match: yes   (R001-R419 contiguous, no gaps, no duplicates; 222+53+67+30+47=419)
fulltext_numeric_sweep: 1 unit missing from structured (L520, see MISSING_FROM_STRUCTURED)
gate_a2: pass
=== END COUNT TEST ===
```

NOTE ANCHOR_DRIFT: A1 row line anchors run 1-3 lines off the fulltext 4-digit prefix in places (e.g. 3500 crore at R146 line 221 vs fulltext 0224; cash 933 at R058 line 54 vs 0053). Row-to-turn mapping below is by A1 line; '~' = nearest turn, boundary-adjacent. Not a gate issue; A3/A4 should read the fulltext by value, not by line.

NOTE ASR: all numbers are [ASR, verify against filed transcript]. Turns are best-effort, no diarization; management replies unlabelled.

## 1. PARTICIPANTS
ROW_ID | category | flags | note
R015 | participant |  | line 19; Go India Advisors host
R018 | participant |  | line 26; company speaker
R113 | participant |  | line 103; analyst Q1
R145 | participant |  | line 209; analyst Q2
R198 | participant |  | line 363; analyst Q3
R264 | participant |  | line 549; analyst Q4
R312 | participant |  | line 677; analyst Q5
R350 | participant |  | line 746; analyst Q6
R363 | participant |  | line 764; analyst Q7
R376 | participant |  | line 779; analyst Q8
R390 | participant |  | line 804; analyst Q9
R417 | participant | RESTATED(R018) | line 840; closing comments
R002,R005,R013 | company/host entities | | company ids, host Go India Advisors, ASR name 'Garwale'
MGMT_ABSENCE | only management speaker is Deepak Joshi (Director Sales & Marketing, R018); no promoter/CMD or CFO named on a substantive call. Flag MGMT_ABSENCE. Moderator unnamed (T01). Rows: R015,R018,R417

## 2. SPEAKER TURNS (T01-T97) with structured rows falling in each turn
TURN | lines | speaker | rows
T01 | L12-19 | Operator/Moderator (UNLABELLED, cue "hand over the conference") | R001..R015 (15)
T02 | L21-29 | Garima Singla, Go India Advisors (stated L21) | R016,R017,R018
T03 | L31-90 | Deepak Joshi, Director Sales & Marketing (stated L26; prepared remarks) | R019..R112 (94)
T04 | L92-105 | Moderator (UNLABELLED, cue "first question is from") | R113
T05 | L106-112 | Mahesh Bendre, LIC Mutual Fund (question) | -
T06 | L113-121 | Management reply (UNLABELLED; Deepak Joshi inferred from L27) | R114,R115,R116,R117,R118,R119
T07 | L123-126 | Mahesh Bendre (question) | R120
T08 | L127-146 | Management reply (UNLABELLED) | R121..R127 (7)
T09 | L148-152 | Mahesh Bendre (question) | R128
T10 | L153-160 | Management reply (UNLABELLED) | R129,R130,R131
T11 | L161-164 | Mahesh Bendre (question) | R132
T12 | L166-180 | Management reply (UNLABELLED) | R133,R134,R135,R136
T13 | L181-186 | Mahesh Bendre (question) | -
T14 | L187-204 | Management reply (UNLABELLED) | R137..R144 (8)
T15 | L205-208 | Mahesh Bendre/management thanks (UNLABELLED) | -
T16 | L209-211 | Moderator (introduces Viraj Parikh) | R145
T17 | L212-220 | Viraj Parikh, Kalanilian AMC (question) | -
T18 | L221-225 | Management reply (UNLABELLED) | R146,R147,R148
T19 | L226-228 | Viraj Parikh (question) | R149,R150,R151
T20 | L229-231 | Management reply (UNLABELLED) | R152
T21 | L232-244 | Viraj Parikh (question; mixed with replies "Yes, yes", UNLABELLED) | R153,R154
T22 | L245-257 | Management reply (UNLABELLED) | R155..R164 (10)
T23 | L258-261 | Viraj Parikh (question, customer concentration) | R165,R166
T24 | L262-291 | Management reply (UNLABELLED) | R167..R178 (12)
T25 | L292-297 | Viraj Parikh (question, inventory) | R179
T26 | L298-359 | Management reply (UNLABELLED) | R180..R197 (18)
T27 | L360-362 | Viraj Parikh (thanks) | -
T28 | L363-364 | Moderator (introduces Archal Pal) | R198
T29 | L365-368 | Archal Pal, Monag Network (ASR) (question) | -
T30 | L369-383 | Management reply (UNLABELLED) | R199..R208 (10)
T31 | L384-386 | Archal Pal (question) | -
T32 | L387-392 | Management reply (UNLABELLED) | R209..R216 (8)
T33 | L393-397 | Archal Pal (question) | -
T34 | L398-457 | Management reply (UNLABELLED) | R217..R241 (25)
T35 | L458-460 | Archal Pal (question) | -
T36 | L461-470 | Management reply (UNLABELLED) | R242..R248 (7)
T37 | L471-475 | Archal Pal (question) | -
T38 | L476-534 | Management reply (UNLABELLED) | R249..R261 (13)
T39 | L535-538 | Archal Pal (question) | -
T40 | L539-545 | Management reply (UNLABELLED) | R262,R263
T41 | L546-548 | Archal Pal/management thanks (UNLABELLED) | -
T42 | L549-551 | Moderator (introduces Rahul Jain) | R264
T43 | L552-573 | Rahul Jain, Credence Wealth (question) | R265,R266
T44 | L574-609 | Management reply (UNLABELLED) | R267..R275 (9)
T45 | L610-622 | Rahul Jain (question) | R276,R277,R278,R279
T46 | L623-624 | Management reply (UNLABELLED) | R280,R281,R282
T47 | L625-635 | Rahul Jain (question) | R283,R284,R285
T48 | L636-646 | Management reply (UNLABELLED) | R286..R296 (11)
T49 | L647-648 | Rahul Jain (question, margin sustainability) | R297,R298
T50 | L648-657 | Management reply (UNLABELLED) | R299,R300,R301
T51 | L658-660 | Rahul Jain (clarification) | -
T52 | L661-668 | Mixed management/analyst exchange (UNLABELLED) | R302,R303,R304,R305,R306,R307
T53 | L669-674 | Rahul Jain (dividend request) | R308,R309,R310
T54 | L675-676 | Management reply (UNLABELLED) | R311
T55 | L677-677 | Moderator (introduces Bhavika Singhvi) | R312
T56 | L678-683 | Bhavika Singhvi, Neveshay (ASR) (question) | -
T57 | L684-695 | Management reply (UNLABELLED) | R313..R323 (11)
T58 | L696-701 | Bhavika Singhvi (question, studios) | R324,R325,R326
T59 | L702-720 | Management reply (UNLABELLED) | R327..R341 (15)
T60 | L721-728 | Bhavika Singhvi (question, B2C margin and product margins; continues L730-731) | R342,R343
T61 | L732-739 | Management reply (UNLABELLED) | R344,R345
T62 | L740-741 | Bhavika Singhvi (question) | -
T63 | L742-745 | Management reply (UNLABELLED) | R346,R347,R348,R349
T64 | L746-747 | Moderator (introduces Dhvaneel Desai) | R350
T65 | L748-750 | Dhvaneel Desai, Total Capital (question) | R351
T66 | L751-760 | Management reply (UNLABELLED) | R352..R361 (10)
T67 | L761-762 | Dhvaneel Desai (comment/thanks) | R362
T68 | L764-764 | Moderator (introduces Vedant Sarada) | R363
T69 | L765-767 | Vedant Sarada, Nirmal Bang Securities (ASR) (question) | R364,R365
T70 | L768-771 | Management reply (UNLABELLED) | R366
T71 | L772-772 | Vedant Sarada (question) | R367
T72 | L773-773 | Management reply (UNLABELLED) | -
T73 | L774-774 | Vedant Sarada (question) | -
T74 | L775-776 | Management reply (UNLABELLED) | R368..R375 (8)
T75 | L777-777 | Vedant Sarada (thanks) | -
T76 | L779-779 | Moderator (introduces Nilesh Chain) | R376
T77 | L780-785 | Nilesh Chain, Astute Investment Management (question) | R377
T78 | L786-795 | Management reply (UNLABELLED) | R378,R379,R380,R381,R382
T79 | L796-797 | Nilesh Chain (question, D2C margins) | R383
T80 | L798-798 | Management reply (UNLABELLED) | R384,R385
T81 | L799-799 | Nilesh Chain (audio drop) | -
T82 | L800-801 | Management reply (UNLABELLED) | R386,R387,R388
T83 | L802-802 | Nilesh Chain (thanks) | R389
T84 | L804-804 | Moderator (introduces Switcher Jain) | R390
T85 | L805-809 | Switcher Jain, NS Wealth (ASR) (question, Lubrizol) | -
T86 | L810-825 | Management reply (UNLABELLED) | R391..R403 (13)
T87 | L826-827 | Switcher Jain (clarification) | -
T88 | L828-829 | Management reply (UNLABELLED) | R404,R405,R406
T89 | L830-830 | Switcher Jain (question) | -
T90 | L831-832 | Management reply (UNLABELLED) | R407,R408
T91 | L833-834 | Switcher Jain (question, volume and geography) | -
T92 | L835-836 | Management reply (UNLABELLED) | R409,R410,R411,R412,R413
T93 | L837-837 | Switcher Jain (question) | -
T94 | L838-839 | Management reply (UNLABELLED) | R414,R415,R416
T95 | L840-840 | Moderator (last question, hand to Deepak Joshi) | R417
T96 | L841-841 | Deepak Joshi (closing comments, stated L840) | R418,R419
T97 | L842-842 | Moderator (close) | -

rows mapped to turns: 419 of 419

## 3. QUESTIONS LEDGER
TURN | analyst/firm | topic | flags | rows
T05 | Mahesh Bendre, LIC Mutual Fund (question) | L106-112 |  | 
T07 | Mahesh Bendre (question) | L123-126 |  | R120
T09 | Mahesh Bendre (question) | L148-152 |  | R128
T11 | Mahesh Bendre (question) | L161-164 |  | R132
T13 | Mahesh Bendre (question) | L181-186 |  | 
T17 | Viraj Parikh, Kalanilian AMC (question) | L212-220 |  | 
T19 | Viraj Parikh (question) | L226-228 |  | R149,R150,R151
T21 | Viraj Parikh (question; mixed with replies "Yes, yes", UNLABELLED) | L232-244 |  | R153,R154
T23 | Viraj Parikh (question, customer concentration) | L258-261 |  | R165,R166
T25 | Viraj Parikh (question, inventory) | L292-297 |  | R179
T29 | Archal Pal, Monag Network (ASR) (question) | L365-368 |  | 
T31 | Archal Pal (question) | L384-386 |  | 
T33 | Archal Pal (question) | L393-397 |  | 
T35 | Archal Pal (question) | L458-460 |  | 
T37 | Archal Pal (question) | L471-475 |  | 
T39 | Archal Pal (question) | L535-538 |  | 
T43 | Rahul Jain, Credence Wealth (question) | L552-573 |  | R265,R266
T45 | Rahul Jain (question) | L610-622 |  | R276,R277,R278,R279
T47 | Rahul Jain (question) | L625-635 |  | R283,R284,R285
T49 | Rahul Jain (question, margin sustainability) | L647-648 | MARGIN_THEME(T47,T49,T60,T79) | R297,R298
T51 | Rahul Jain (clarification) | L658-660 |  | 
T53 | Rahul Jain (dividend request) | L669-674 |  | R308,R309,R310
T56 | Bhavika Singhvi, Neveshay (ASR) (question) | L678-683 |  | 
T58 | Bhavika Singhvi (question, studios) | L696-701 | REPEAT_QUESTION(D2C/B2C T58,T60,T79) | R324,R325,R326
T60 | Bhavika Singhvi (question, B2C margin and product margins; continues L730-731) | L721-728 | REPEAT_QUESTION(D2C/B2C T58,T60,T79) MARGIN_THEME(T47,T49,T60,T79) | R342,R343
T62 | Bhavika Singhvi (question) | L740-741 |  | 
T65 | Dhvaneel Desai, Total Capital (question) | L748-750 |  | R351
T67 | Dhvaneel Desai (comment/thanks) | L761-762 |  | R362
T69 | Vedant Sarada, Nirmal Bang Securities (ASR) (question) | L765-767 |  | R364,R365
T71 | Vedant Sarada (question) | L772-772 |  | R367
T73 | Vedant Sarada (question) | L774-774 |  | 
T77 | Nilesh Chain, Astute Investment Management (question) | L780-785 |  | R377
T79 | Nilesh Chain (question, D2C margins) | L796-797 | REPEAT_QUESTION(D2C/B2C T58,T60,T79) MARGIN_THEME(T47,T49,T60,T79) | R383
T81 | Nilesh Chain (audio drop) | L799-799 |  | 
T85 | Switcher Jain, NS Wealth (ASR) (question, Lubrizol) | L805-809 |  | 
T87 | Switcher Jain (clarification) | L826-827 |  | 
T89 | Switcher Jain (question) | L830-830 |  | 
T91 | Switcher Jain (question, volume and geography) | L833-834 |  | 
T93 | Switcher Jain (question) | L837-837 |  | 
REPEAT_QUESTION notes: D2C/B2C margin raised by Bhavika Singhvi (T60) and Nilesh Chain (T79); medium-term 27%+ margin raised by Rahul Jain (T47,T49,T51); capacity/3500 crore raised T17, T62 area (R146,R162,R322); TPU 25% external sale restated T85-T88 (R266,R270). Same analyst multi-turn follow-ups (Mahesh Bendre x5) are not counted as repeats.

## 4. MANAGEMENT NUMBERS (all NUMBER rows; each tagged ASR)
ROW_ID | turn | flags
R003 | T01~ | 
R007 | T01~ | 
R008 | T01~ | 
R021 | T03 | 
R022 | T03 | 
R023 | T03 | 
R024 | T03 | 
R025 | T03 | 
R026 | T03 | 
R027 | T03 | 
R028 | T03 | 
R029 | T03 | 
R033 | T03 | 
R035 | T03 | 
R037 | T03 | 
R038 | T03 | 
R040 | T03 | 
R041 | T03 | 
R042 | T03 | 
R043 | T03 | 
R044 | T03 | 
R045 | T03 | 
R046 | T03 | 
R047 | T03 | 
R048 | T03 | 
R049 | T03 | 
R050 | T03 | 
R051 | T03 | 
R052 | T03 | 
R053 | T03 | 
R054 | T03 | 
R058 | T03 | 
R060 | T03 | 
R061 | T03 | 
R075 | T03 | 
R079 | T03 | 
R081 | T03 | 
R082 | T03 | 
R083 | T03 | 
R085 | T03 | 
R087 | T03 | 
R088 | T03 | 
R089 | T03 | 
R093 | T03 | 
R096 | T03 | 
R098 | T03 | 
R099 | T03 | 
R100 | T03 | 
R101 | T03 | 
R102 | T03 | 
R106 | T03 | 
R107 | T03 | 
R109 | T03 | 
R114 | T06 | 
R115 | T06 | 
R116 | T06 | 
R117 | T06 | 
R118 | T06 | 
R125 | T08 | 
R126 | T08 | 
R129 | T10 | 
R130 | T10 | 
R131 | T10 | 
R133 | T12 | 
R134 | T12 | 
R135 | T12 | 
R137 | T14 | 
R138 | T14 | 
R143 | T14 | 
R146 | T18 | 
R149 | T19 | 
R150 | T19 | 
R151 | T19 | 
R153 | T21 | 
R154 | T21 | 
R155 | T22 | 
R156 | T22 | 
R162 | T22 | 
R165 | T23 | 
R168 | T24 | 
R169 | T24 | 
R173 | T24 | 
R177 | T24 | 
R178 | T24 | 
R179 | T25 | 
R181 | T26 | 
R182 | T26 | 
R183 | T26 | 
R184 | T26 | 
R185 | T26 | 
R187 | T26 | 
R188 | T26 | 
R189 | T26 | 
R190 | T26 | 
R191 | T26 | 
R193 | T26 | 
R194 | T26 | 
R195 | T26 | 
R196 | T26 | 
R199 | T30 | 
R200 | T30 | 
R202 | T30 | 
R203 | T30 | 
R209 | T32 | 
R210 | T32 | 
R211 | T32 | 
R212 | T32 | 
R215 | T32 | 
R216 | T32 | 
R218 | T34 | 
R219 | T34 | 
R220 | T34 | 
R221 | T34 | 
R228 | T34 | 
R229 | T34 | 
R231 | T34 | 
R234 | T34 | 
R235 | T34 | 
R237 | T34 | 
R238 | T34 | 
R239 | T34 | 
R240 | T34 | 
R241 | T34 | 
R242 | T36 | 
R243 | T36 | 
R244 | T36 | 
R245 | T36 | 
R248 | T36 | 
R249 | T38 | 
R250 | T38 | 
R251 | T38 | 
R252 | T38 | 
R254 | T38 | 
R255 | T38 | 
R257 | T38 | 
R258 | T38 | 
R259 | T38 | 
R260 | T38 | 
R261 | T38 | 
R265 | T43 | 
R266 | T43 | 
R267 | T44 | 
R270 | T44 | 
R271 | T44 | 
R273 | T44 | 
R276 | T45 | 
R277 | T45 | 
R278 | T45 | 
R279 | T45 | 
R280 | T46 | 
R283 | T47 | 
R284 | T47 | 
R285 | T47 | 
R287 | T48 | 
R289 | T48 | 
R291 | T48 | 
R293 | T48 | 
R294 | T48 | 
R296 | T48 | 
R297 | T49 | 
R302 | T52 | 
R303 | T52 | 
R304 | T52 | 
R305 | T52 | 
R307 | T52 | 
R313 | T57 | 
R314 | T57 | 
R315 | T57 | 
R320 | T57 | 
R321 | T57 | 
R322 | T57 | 
R325 | T58 | 
R327 | T59 | 
R329 | T59 | 
R330 | T59 | 
R332 | T59 | 
R334 | T59 | 
R335 | T59 | 
R336 | T59 | 
R339 | T59 | 
R346 | T63 | 
R348 | T63 | 
R349 | T63 | 
R351 | T65 | 
R352 | T66 | 
R353 | T66 | 
R354 | T66 | 
R355 | T66 | 
R356 | T66 | 
R359 | T66 | 
R360 | T66 | 
R364 | T69 | 
R367 | T71 | 
R368 | T74 | 
R369 | T74 | 
R370 | T74 | 
R371 | T74 | 
R372 | T74 | 
R374 | T74 | 
R375 | T74 | 
R377 | T77 | 
R381 | T78 | 
R382 | T78 | 
R383 | T79 | 
R384 | T80 | 
R385 | T80 | 
R386 | T82 | 
R387 | T82 | 
R389 | T83 | 
R393 | T86 | 
R394 | T86 | 
R395 | T86 | 
R397 | T86 | 
R404 | T88 | 
R405 | T88 | 
R407 | T90 | 
R410 | T92 | 
R411 | T92 | 
R412 | T92 | 
R413 | T92 | 
R414 | T94 | 
R415 | T94 | 

FOOTNOTE_UNRESOLVED (ASR conflicts, per A1 note, grep-confirmed rows): 
  [studios] R082 line 70 NUMBER | two [ASR]
  [studios] R083 line 70 NUMBER | 14 [ASR]
  [studios] R084 line 70 DATE | Q2
  [studios] R087 line 74 NUMBER | 9 [ASR]
  [studios] R088 line 75 NUMBER | 14 [ASR]
  [studios] R089 line 75 NUMBER | 12 [ASR]
  [studios] R090 line 75 FORWARD | plan to add another 12 studios in Q3 incl Delhi NCR and Mumbai
  [studios] R094 line 76 FORWARD | longer term target 50 studios by December 2027
  [studios] R327 line 705 NUMBER | 40 [ASR]
  [studios] R329 line 709 NUMBER | 14 [ASR]
  [studios] R330 line 709 NUMBER | 50 [ASR]
  [studios] R331 line 709 FORWARD | target 50 studios in next 9 to 12 months, not in next six months
  [studios] R332 line 709 NUMBER | 9 to 12 months [ASR]
  [114] R179 line 297 NUMBER | 114 [ASR]
  [beta] R346 line 743 NUMBER | 40-45% [ASR]
  [beta] R347 line 743 QUALIFIER | margin referred to as "beta margin" (ASR; basis undefined)

RESTATED cross-refs: 3500 crore = R146,R162,R322 (also R147,R163,R323); cash 933 = R058; 80-85% price vs global = R251,R252,R258; 27%+ margin family around R285,R286 and T49-T52; TPU 35% = R270,R271; D2C 10-15% = R388,R389,R387.

## 5. FORWARD COMMITMENTS (FORWARD rows)
ROW_ID | turn | flags
R016 | T02 | forward-commitment
R036 | T03 | forward-commitment
R063 | T03 | forward-commitment
R064 | T03 | forward-commitment
R071 | T03 | forward-commitment
R074 | T03 | forward-commitment
R076 | T03 | forward-commitment
R077 | T03 | forward-commitment
R090 | T03 | forward-commitment
R094 | T03 | forward-commitment
R097 | T03 | forward-commitment
R104 | T03 | forward-commitment
R105 | T03 | forward-commitment
R108 | T03 | forward-commitment
R111 | T03 | forward-commitment
R121 | T08 | forward-commitment
R127 | T08 | forward-commitment
R132 | T11~ | forward-commitment
R136 | T12 | forward-commitment
R140 | T14 | forward-commitment
R141 | T14 | forward-commitment
R144 | T14 | forward-commitment
R147 | T18 | forward-commitment
R157 | T22 | forward-commitment
R158 | T22 | forward-commitment
R159 | T22 | forward-commitment
R161 | T22 | forward-commitment
R164 | T22 | forward-commitment
R167 | T24 | forward-commitment
R192 | T26 | forward-commitment
R197 | T26 | forward-commitment
R201 | T30 | forward-commitment
R204 | T30 | forward-commitment
R205 | T30 | forward-commitment
R207 | T30 | forward-commitment
R208 | T30 | forward-commitment
R213 | T32 | forward-commitment
R227 | T34 | forward-commitment
R230 | T34 | forward-commitment
R233 | T34 | forward-commitment
R246 | T36 | forward-commitment
R247 | T36 | forward-commitment
R268 | T44 | forward-commitment
R275 | T44 | forward-commitment
R281 | T46 | forward-commitment
R288 | T48 | forward-commitment
R295 | T48 | forward-commitment
R300 | T50 | forward-commitment
R306 | T52 | forward-commitment
R310 | T53 | forward-commitment
R311 | T54 | forward-commitment
R316 | T57 | forward-commitment
R319 | T57 | forward-commitment
R323 | T57 | forward-commitment
R331 | T59 | forward-commitment
R338 | T59 | forward-commitment
R344 | T61 | forward-commitment
R345 | T61 | forward-commitment
R361 | T66 | forward-commitment
R362 | T67 | forward-commitment
R388 | T82 | forward-commitment
R396 | T86 | forward-commitment
R398 | T86 | forward-commitment
R406 | T88 | forward-commitment
R408 | T90 | forward-commitment
R416 | T94 | forward-commitment
R419 | T96 | forward-commitment

## 6. HEDGE / QUALIFIER PHRASES (QUALIFIER rows)
ROW_ID | turn | flags
R001 | T01~ | hedge/qualifier
R009 | T01~ | hedge/qualifier
R011 | T01~ | hedge/qualifier
R012 | T01~ | hedge/qualifier
R017 | T02 | hedge/qualifier
R030 | T03 | hedge/qualifier
R031 | T03 | hedge/qualifier
R032 | T03 | hedge/qualifier
R034 | T03 | hedge/qualifier
R057 | T03 | hedge/qualifier
R080 | T03 | hedge/qualifier
R103 | T03 | hedge/qualifier
R119 | T06 | hedge/qualifier
R139 | T14 | hedge/qualifier
R142 | T14 | hedge/qualifier
R148 | T18 | hedge/qualifier
R152 | T20 | hedge/qualifier
R163 | T22 | hedge/qualifier
R166 | T23 | hedge/qualifier
R174 | T24 | hedge/qualifier
R180 | T26 | hedge/qualifier
R186 | T26 | hedge/qualifier
R226 | T34 | hedge/qualifier
R232 | T34 | hedge/qualifier
R253 | T38 | hedge/qualifier
R256 | T38 | hedge/qualifier
R262 | T40 | hedge/qualifier
R263 | T40 | hedge/qualifier
R269 | T44 | hedge/qualifier
R272 | T44 | hedge/qualifier
R282 | T46 | hedge/qualifier
R286 | T48 | hedge/qualifier
R290 | T48 | hedge/qualifier
R292 | T48 | hedge/qualifier
R299 | T50 | hedge/qualifier
R324 | T58 | hedge/qualifier
R328 | T59 | hedge/qualifier
R333 | T59 | hedge/qualifier
R337 | T59 | hedge/qualifier
R340 | T59 | hedge/qualifier
R343 | T60 | hedge/qualifier
R347 | T63 | hedge/qualifier
R357 | T66 | hedge/qualifier
R366 | T70 | hedge/qualifier
R380 | T78 | hedge/qualifier
R401 | T86 | hedge/qualifier
R409 | T92 | hedge/qualifier

## 7. ENTITIES
ROW_ID | turn | flags
R002 | T01~ | 
R005 | T01~ | 
R013 | T01 | 
R015 | T01 | 
R018 | T02 | 
R019 | T03 | 
R055 | T03 | 
R056 | T03 | 
R065 | T03 | 
R066 | T03 | 
R067 | T03 | 
R068 | T03 | 
R069 | T03 | 
R070 | T03 | 
R073 | T03 | 
R086 | T03 | 
R092 | T03 | 
R113 | T04 | 
R120 | T07 | 
R122 | T08 | 
R123 | T08 | 
R124 | T08 | 
R128 | T09 | 
R145 | T16 | 
R170 | T24 | 
R171 | T24 | 
R172 | T24 | 
R175 | T24 | 
R176 | T24 | 
R198 | T28 | 
R222 | T34 | 
R223 | T34 | 
R224 | T34 | 
R225 | T34 | 
R264 | T42 | 
R308 | T53 | 
R312 | T55 | 
R341 | T59 | 
R342 | T60 | 
R350 | T64 | 
R363 | T68 | 
R365 | T69 | 
R376 | T76 | 
R378 | T78 | 
R390 | T84 | 
R391 | T86 | 
R392 | T86 | 
R399 | T86 | 
R400 | T86 | 
R402 | T86 | 
R403 | T86 | 
R417 | T95 | 
R418 | T96 | 

## 8. DATES
ROW_ID | turn | flags
R004 | T01~ | 
R006 | T01~ | 
R010 | T01~ | 
R014 | T01 | 
R020 | T03 | 
R039 | T03 | 
R059 | T03 | 
R062 | T03 | 
R072 | T03 | 
R078 | T03 | 
R084 | T03 | 
R091 | T03 | 
R095 | T03 | 
R110 | T03 | 
R112 | T03 | 
R160 | T22 | 
R206 | T30 | 
R214 | T32 | 
R217 | T34 | 
R236 | T34 | 
R274 | T44 | 
R298 | T49 | 
R301 | T50 | 
R309 | T53 | 
R317 | T57 | 
R318 | T57 | 
R326 | T58 | 
R358 | T66 | 
R373 | T74 | 
R379 | T78 | 

## 9. MISSING_FROM_STRUCTURED
MFS01 | fulltext L520 (prefix 0520) | NUMBER | management example '...one product, we can simply say this is 85%' (price vs global player, single-product example; R258 covers 85-120% range, not this statement). ASR, verify.

ZERO_STANDING: none (concall; A1 observed none).