=== A2 COUNT TEST ===
category: participants   grep_count: 9    sweep_count: 9    match: yes   (5 mgmt R068-R072, host R073, 2 analysts R142/R155, operator Moderator R134)
category: turns          grep_count: 52   sweep_count: 52   match: yes   (grep -c "SPEAKER TURN" in structured = 52; A1 header = 52)
category: questions      grep_count: 15   sweep_count: 15   match: yes   (18 analyst turns: 15 questions, 1 muffled fragment T34, 2 audibility checks T22/T36; see Note Q)
category: mgmt_numbers   grep_count: 53   sweep_count: 53   match: yes   (61 NUMBER rows minus R001 cover scrip code minus 7 analyst-voiced R050,R051,R053,R054,R057,R058,R060)
category: forward_phrases grep_count: 65  sweep_count: 65   match: yes   (R186-R249 plus R327; fulltext re-sweep adds R327)
category: hedge_qualifiers grep_count: 39 sweep_count: 39   match: yes   (R288-R324 plus R325, R326; fulltext re-sweep)
category: dates          grep_count: 38   sweep_count: 38   match: yes   (R250-R287)
category: entities_nonturn grep_count: 72 sweep_count: 72   match: yes   (R062-R133)
category: zero_standing  grep_count: 0    sweep_count: 0    match: yes   (no nil/dash standing items in a transcript)
gate_a2: pass
=== END COUNT TEST ===

ids_in_structured: 324 | ids_referenced_in_ledger: 327 (324 structured + 3 MISSING_FROM_STRUCTURED) | orphan_ids: [] | match: yes
LOOP 1 (A5 correction): fulltext re-sweep for forward and hedge lexicon added R325-R327; no further units found (lines 74 and 327 are operator boilerplate and analyst speech).

Note Q: speaker labels sit in a left column and "?" is inconsistent; questions are identified by function per analyst turn. Analyst turns = 9,11,13,15,17,19,22,24,27,30,32,34,36,38,40,43,45,47 (18). T22 and T36 are audibility checks. T34 is a muffled restart of the question completed in T38 (counted once, in T38). Moderator turns 01,08,21,23,35,37,42,50,52 are procedural.
Note N: line-to-turn mapping uses the nearest preceding turn start line. Cover-letter rows (lines before 69) carry turn 00. A1 turn rows give each turn's FIRST line only.
Note vs Q1 FY27 ledger (ASR transcript, not like-for-like): Q1 had 109 turns, 8 analysts, 37 questions, host ICICI Securities. Q2 has 52 turns, 2 analysts, 15 questions, host Emkay (Aryan Tripathi). Q2 transcript is "edited for clarity" (R323). Peace Wealth (Tushar Khurana; Q1 "Pushkar Kurana") is the only repeat analyst; Niveshaay is new. Sanjay Malik named with zero turns in both quarters. Preetham Uthaiah (COO) listed, zero turns.


=== 1. PARTICIPANTS ===
ROW_ID | category | A2 flags | note
R068 | mgmt participant | TITLE_DISCREPANCY | p2 Chairman and MD vs p3 MD and CEO (R075); promoter-CMD present on call
R069 | mgmt participant | - | CFO; speaks T04,T29,T31
R070 | mgmt participant | - | CTO; speaks T06,T25,T44,T46,T48
R071 | mgmt participant | MGMT_ABSENCE | COO listed, zero speaking turns
R072 | mgmt participant | MGMT_ABSENCE | CSBO listed, zero speaking turns (also zero in Q1 FY27)
R073 | host Emkay (Aryan Tripathi) | - | host changed from ICICI Securities in Q1; cross-ref R074, R135
R134 | call operator Moderator | - | procedural
R142 | analyst Tushar Khurana, Peace Wealth | - | also in Q1 (as Pushkar Kurana, ASR)
R155 | analyst Keyurkumar Vadaliya, Niveshaay | ENTITY_CHANGE (new vs Q1 roster) | -

=== 2. SPEAKER TURNS (52) ===
Turn | ROW_ID | speaker | A2 flags
01 | R134 | Moderator (operator) | -
02 | R135 | Aryan Tripathi (Emkay Global Financial Services Limited) | -
03 | R136 | Arnob Roy (Tejas) | -
04 | R137 | AVS Prasad (Tejas) | -
05 | R138 | Arnob Roy (Tejas) | -
06 | R139 | Kumar N. Sivarajan (Tejas) | -
07 | R140 | Arnob Roy (Tejas) | -
08 | R141 | Moderator | -
09 | R142 | Tushar Khurana (Peace Wealth) | -
10 | R143 | Arnob Roy (Tejas) | -
11 | R144 | Tushar Khurana (Peace Wealth) | -
12 | R145 | Arnob Roy (Tejas) | -
13 | R146 | Tushar Khurana (Peace Wealth) | -
14 | R147 | Arnob Roy (Tejas) | -
15 | R148 | Tushar Khurana (Peace Wealth) | -
16 | R149 | Arnob Roy (Tejas) | -
17 | R150 | Tushar Khurana (Peace Wealth) | -
18 | R151 | Arnob Roy (Tejas) | -
19 | R152 | Tushar Khurana (Peace Wealth) | -
20 | R153 | Arnob Roy (Tejas) | -
21 | R154 | Moderator | -
22 | R155 | Keyurkumar Vadaliya (Niveshaay) | AUDIBILITY_CHECK
23 | R156 | Moderator | -
24 | R157 | Keyurkumar Vadaliya (Niveshaay) | -
25 | R158 | Kumar N. Sivarajan (Tejas) | -
26 | R159 | Arnob Roy (Tejas) | -
27 | R160 | Keyurkumar Vadaliya (Niveshaay) | -
28 | R161 | Arnob Roy (Tejas) | -
29 | R162 | AVS Prasad (Tejas) | -
30 | R163 | Keyurkumar Vadaliya (Niveshaay) | -
31 | R164 | AVS Prasad (Tejas) | -
32 | R165 | Keyurkumar Vadaliya (Niveshaay) | -
33 | R166 | Arnob Roy (Tejas) | -
34 | R167 | Keyurkumar Vadaliya (Niveshaay) | FRAGMENT_MUFFLED
35 | R168 | Moderator | -
36 | R169 | Keyurkumar Vadaliya (Niveshaay) | AUDIBILITY_CHECK
37 | R170 | Moderator | -
38 | R171 | Keyurkumar Vadaliya (Niveshaay) | -
39 | R172 | Arnob Roy (Tejas) | -
40 | R173 | Keyurkumar Vadaliya (Niveshaay) | -
41 | R174 | Arnob Roy (Tejas) | -
42 | R175 | Moderator | -
43 | R176 | Tushar Khurana (Peace Wealth) | -
44 | R177 | Kumar N. Sivarajan (Tejas) | -
45 | R178 | Tushar Khurana (Peace Wealth) | -
46 | R179 | Kumar N. Sivarajan (Tejas) | -
47 | R180 | Tushar Khurana (Peace Wealth) | -
48 | R181 | Kumar N. Sivarajan (Tejas) | -
49 | R182 | Arnob Roy (Tejas) | -
50 | R183 | Moderator | -
51 | R184 | Arnob Roy (Tejas) | -
52 | R185 | Moderator (Emkay Global) | -

=== 3. QUESTIONS (15) ===
Q# | turn | ROW_ID | analyst | firm | topic | flags
Q01 | T09 | R142 | Tushar Khurana | Peace Wealth | BSNL dues recovered/outstanding and timing | -
Q02 | T11 | R144 | Tushar Khurana | Peace Wealth | Does Rs2,300cr order book include BSNL Rs1,500cr | REPEAT_QUESTION (order book composition, with 13; R050-R054)
Q03 | T13 | R146 | Tushar Khurana | Peace Wealth | Order book split ex-BSNL (Q1 Rs1,500cr vs now) | REPEAT_QUESTION (with 11)
Q04 | T15 | R148 | Tushar Khurana | Peace Wealth | International bids and expos, conversion | -
Q05 | T17 | R150 | Tushar Khurana | Peace Wealth | Vi POC trials, case for expansion order | -
Q06 | T19 | R152 | Tushar Khurana | Peace Wealth | DCI stack, GPU vendor onboarding | -
Q07 | T24 | R157 | Keyurkumar Vadaliya | Niveshaay | AI/6G products, AI DCI order window, railway 700MHz/Kavach (multi-part) | -
Q08 | T27 | R160 | Keyurkumar Vadaliya | Niveshaay | Rs145cr contract-manufacturing loss in COGS | -
Q09 | T30 | R163 | Keyurkumar Vadaliya | Niveshaay | Clarify Rs145cr provisioning timing (Sep 2025) | REPEAT_QUESTION (follow-up of 27)
Q10 | T32 | R165 | Keyurkumar Vadaliya | Niveshaay | Is the loss non-recurring | REPEAT_QUESTION (follow-up of 27/30)
Q11 | T38 | R171 | Keyurkumar Vadaliya | Niveshaay | BSNL PO effect on inventory and debt (quantum) | -
Q12 | T40 | R173 | Keyurkumar Vadaliya | Niveshaay | Gross debt effect | REPEAT_QUESTION (debt, restates 38)
Q13 | T43 | R176 | Tushar Khurana | Peace Wealth | D2M RFP | -
Q14 | T45 | R178 | Tushar Khurana | Peace Wealth | Size/type of international POC telcos | -
Q15 | T47 | R180 | Tushar Khurana | Peace Wealth | NEC: exclusivity, USD500m business, virtual radios | -
Non-question analyst turns: T22 R155 (audibility), T34 R167 (muffled restart of T38 question), T36 R169 (audibility). Moderator procedural: R134,R141,R154,R156,R168,R170,R175,R183,R185.

=== 4. MGMT NUMBERS (53) ===
ROW_ID | turn | line | flags / note
R002 | T03 | 92 | RESTATED R015,R026
R003 | T03 | 92 | RESTATED R016
R004 | T03 | 93 | RESTATED R024
R005 | T03 | 94 | RESTATED R023
R006 | T03 | 95 | MISMATCH vs analyst Rs2,300cr R050/R054
R007 | T03 | 95 | cross-ref analyst R053 (Rs1,500cr)
R008 | T03 | 96 | -
R009 | T03 | 96 | -
R010 | T03 | 96 | -
R011 | T03 | 97 | -
R012 | T03 | 98 | cross-ref R034
R013 | T03 | 105 | -
R014 | T03 | 105 | RESTATED R037
R015 | T04 | 109 | RESTATED R002,R026
R016 | T04 | 110 | RESTATED R003
R017 | T04 | 110 | -
R018 | T04 | 111 | -
R019 | T04 | 112 | -
R020 | T04 | 112 | -
R021 | T04 | 115 | -
R022 | T04 | 116 | RESTATED R028
R023 | T04 | 116 | RESTATED R005
R024 | T04 | 117 | RESTATED R004
R025 | T04 | 124 | -
R026 | T04 | 125 | RESTATED R002,R015
R027 | T04 | 125 | -
R028 | T04 | 126 | RESTATED R022
R029 | T04 | 129 | -
R030 | T04 | 134 | -
R031 | T04 | 134 | -
R032 | T04 | 139 | LABEL net debt, see R292
R033 | T04 | 140 | LABEL net debt (R032) vs debt (R033), see R292/R299
R034 | T05 | 145 | cross-ref R012 (18,000-plus vs 18,685)
R035 | T05 | 158 | -
R036 | T05 | 166 | -
R037 | T05 | 182 | RESTATED R014
R038 | T05 | 182 | -
R039 | T05 | 199 | -
R040 | T05 | 205 | -
R041 | T05 | 209 | -
R042 | T05 | 209 | -
R043 | T06 | 233 | -
R044 | T06 | 235 | -
R045 | T06 | 238 | -
R046 | T06 | 239 | -
R047 | T06 | 252 | -
R048 | T06 | 258 | -
R049 | T06 | 259 | -
R052 | T12 | 349 | cross-ref R051/R053 (analyst-voiced); mgmt says LOI total Rs1,500cr
R055 | T16 | 404 | NO_FIGURE claim
R056 | T25 | 462 | -
R059 | T33 | 498 | cross-ref R057 (analyst Rs145cr)
R061 | T46 | 562 | -
Analyst-voiced numbers (accounted, not mgmt): R050 T11, R051 T11, R053 T13, R054 T13, R057 T27, R058 T24, R060 T47. Cover item: R001 BSE scrip code (turn 00).

=== 5. FORWARD COMMITMENT PHRASES (64) ===
ROW_ID | turn | line | flags
R186 | T03 | 99 | -
R187 | T03 | 102 | -
R188 | T03 | 104 | -
R189 | T04 | 135 | UNQUANTIFIED_INVENTORY_DEBT_PATH
R190 | T04 | 141 | -
R191 | T05 | 157 | -
R192 | T05 | 151 | -
R193 | T05 | 203 | -
R194 | T05 | 205 | -
R195 | T05 | 208 | EXTERNAL_FORECAST (not mgmt)
R196 | T05 | 210 | -
R197 | T05 | 211 | -
R198 | T05 | 214 | -
R199 | T05 | 220 | -
R200 | T06 | 233 | -
R201 | T06 | 237 | -
R202 | T06 | 241 | -
R203 | T06 | 253 | -
R204 | T06 | 258 | -
R205 | T06 | 260 | -
R206 | T06 | 262 | -
R207 | T07 | 271 | -
R208 | T07 | 274 | -
R209 | T07 | 281 | -
R210 | T07 | 286 | -
R211 | T07 | 291 | -
R212 | T07 | 295 | UNQUANTIFIED_INVENTORY_DEBT_PATH
R213 | T07 | 296 | -
R214 | T07 | 298 | -
R215 | T07 | 300 | -
R216 | T07 | 302 | -
R217 | T07 | 305 | -
R218 | T07 | 306 | -
R219 | T07 | 315 | UNQUANTIFIED_INVENTORY_DEBT_PATH
R220 | T07 | 317 | -
R221 | T10 | 338 | TIME_BOUND (this quarter)
R222 | T10 | 341 | -
R223 | T12 | 349 | TIME_BOUND (this quarter)
R224 | T16 | 368 | -
R225 | T16 | 378 | -
R226 | T18 | 414 | -
R227 | T18 | 417 | -
R228 | T16 | 396 | -
R229 | T20 | 431 | -
R230 | T25 | 466 | -
R231 | T25 | 464 | -
R232 | T26 | 476 | -
R233 | T31 | 494 | NEGATIVE_COMMITMENT
R234 | T33 | 498 | NEGATIVE_COMMITMENT
R235 | T39 | 516 | UNQUANTIFIED_INVENTORY_DEBT_PATH
R236 | T41 | 528 | UNQUANTIFIED_INVENTORY_DEBT_PATH
R237 | T41 | 529 | UNQUANTIFIED_INVENTORY_DEBT_PATH
R238 | T44 | 539 | -
R239 | T44 | 546 | -
R240 | T44 | 549 | -
R241 | T46 | 564 | -
R242 | T46 | 573 | -
R243 | T48 | 586 | -
R244 | T48 | 589 | -
R245 | T49 | 598 | -
R246 | T49 | 599 | -
R247 | T51 | 611 | -
R248 | T51 | 612 | -
R249 | T51 | 615 | -

=== 6. HEDGE / QUALIFIER PHRASES (37) ===
ROW_ID | turn | line | flags
R288 | T00 | 40 | -
R289 | T04 | 111 | -
R290 | T04 | 109 | -
R291 | T04 | 128 | -
R292 | T04 | 139 | -
R293 | T04 | 130 | -
R294 | T04 | 141 | -
R295 | T05 | 182 | -
R296 | T05 | 209 | -
R297 | T06 | 233 | -
R298 | T06 | 249 | -
R299 | T07 | 316 | -
R300 | T07 | 292 | -
R301 | T10 | 340 | NON_DISCLOSURE
R302 | T12 | 347 | -
R303 | T14 | 356 | -
R304 | T14 | 355 | NON_DISCLOSURE
R305 | T11 | 344 | -
R306 | T16 | 372 | -
R307 | T18 | 412 | -
R308 | T16 | 398 | -
R309 | T16 | 404 | -
R310 | T25 | 464 | -
R311 | T25 | 465 | -
R312 | T24 | 458 | -
R313 | T29 | 485 | -
R314 | T31 | 494 | -
R315 | T39 | 514 | NON_DISCLOSURE
R316 | T33 | 498 | -
R317 | T41 | 529 | -
R318 | T44 | 551 | -
R319 | T44 | 549 | -
R320 | T48 | 584 | NON_DISCLOSURE
R321 | T47 | 576 | -
R322 | T46 | 557 | -
R323 | T52 | 622 | -
R324 | T51 | 615 | -

=== 7. DATES / TIMELINES (38) ===
ROW_ID | turn | line | flags
R250 | T00 | 18 | -
R251 | T00 | 29 | -
R252 | T00 | 32 | -
R253 | T00 | 42 | -
R254 | T00 | 53 | -
R255 | T00 | 51 | -
R256 | T03 | 92 | -
R257 | T03 | 93 | -
R258 | T03 | 95 | -
R259 | T04 | 111 | -
R260 | T04 | 112 | -
R261 | T04 | 124 | -
R262 | T04 | 128 | -
R263 | T04 | 137 | -
R264 | T04 | 136 | VAGUE_TIMELINE
R265 | T05 | 177 | -
R266 | T05 | 205 | -
R267 | T05 | 209 | -
R268 | T06 | 246 | -
R269 | T06 | 251 | -
R270 | T06 | 252 | -
R271 | T07 | 283 | -
R272 | T07 | 298 | -
R273 | T07 | 301 | VAGUE_TIMELINE
R274 | T07 | 318 | VAGUE_TIMELINE
R275 | T09 | 334 | -
R276 | T10 | 338 | VAGUE_TIMELINE
R277 | T12 | 350 | VAGUE_TIMELINE
R278 | T16 | 368 | -
R279 | T24 | 458 | -
R280 | T25 | 465 | -
R281 | T31 | 494 | -
R282 | T38 | 512 | VAGUE_TIMELINE
R283 | T39 | 516 | VAGUE_TIMELINE
R284 | T46 | 557 | -
R285 | T51 | 606 | -
R286 | T51 | 616 | VAGUE_TIMELINE
R287 | T51 | 611 | VAGUE_TIMELINE

=== 8. ENTITIES non-turn (72) ===
ROW_ID | turn | line | flags
R062 | T00 | 18 | -
R063 | T00 | 20 | -
R064 | T00 | 25 | -
R065 | T00 | 38 | -
R066 | T00 | 46 | -
R067 | T00 | 20 | -
R068 | T00 | 55 | -
R069 | T00 | 57 | -
R070 | T00 | 59 | -
R071 | T00 | 61 | -
R072 | T00 | 63 | -
R073 | T00 | 66 | -
R074 | T01 | 79 | -
R075 | T02 | 83 | -
R076 | T03 | 98 | -
R077 | T03 | 101 | -
R078 | T03 | 101 | -
R079 | T03 | 103 | -
R080 | T04 | 132 | -
R081 | T04 | 136 | -
R082 | T05 | 145 | -
R083 | T05 | 146 | -
R084 | T05 | 147 | -
R085 | T05 | 152 | -
R086 | T05 | 157 | -
R087 | T05 | 158 | -
R088 | T05 | 159 | -
R089 | T05 | 163 | -
R090 | T05 | 166 | -
R091 | T05 | 176 | -
R092 | T05 | 177 | -
R093 | T05 | 181 | -
R094 | T05 | 185 | -
R095 | T05 | 187 | -
R096 | T05 | 191 | -
R097 | T05 | 194 | -
R098 | T05 | 195 | -
R099 | T05 | 199 | -
R100 | T05 | 200 | -
R101 | T05 | 178 | -
R102 | T06 | 241 | -
R103 | T06 | 246 | -
R104 | T06 | 251 | -
R105 | T06 | 252 | -
R106 | T06 | 263 | -
R107 | T07 | 270 | -
R108 | T08 | 323 | ANALYST_FIRM
R109 | T07 | 286 | -
R110 | T07 | 290 | -
R111 | T11 | 344 | ANALYST_ATTRIBUTION (TCS)
R112 | T10 | 337 | -
R113 | T16 | 372 | -
R114 | T16 | 395 | PARTNER_LICENSOR
R115 | T16 | 395 | PARTNER_LICENSOR
R116 | T17 | 407 | -
R117 | T20 | 431 | ANALYST_ATTRIBUTION (TCS)
R118 | T16 | 391 | -
R119 | T19 | 423 | -
R120 | T21 | 447 | ANALYST_FIRM
R121 | T25 | 462 | -
R122 | T25 | 464 | -
R123 | T26 | 469 | -
R124 | T27 | 478 | -
R125 | T33 | 498 | -
R126 | T43 | 534 | -
R127 | T44 | 538 | -
R128 | T44 | 538 | -
R129 | T46 | 557 | -
R130 | T46 | 568 | -
R131 | T47 | 576 | PARTNER_LICENSOR
R132 | T48 | 585 | PARTNER_LICENSOR
R133 | T51 | 609 | -

=== 9. ZERO_STANDING ===
None. MISSING_FROM_STRUCTURED: none found.

=== ID ACCOUNTABILITY ===
R001-R061 (section 4 plus analyst-voiced list plus cover), R062-R185 (sections 1,2,8), R186-R249 (5), R250-R287 (7), R288-R324 (6). ids_in_structured: 324 | ids_referenced_in_ledger: 324 | orphan_ids: [] | match: yes

=== 10. MISSING_FROM_STRUCTURED (loop 1, fulltext line numbers; claim text held here only) ===
ROW_ID | category | fulltext line | turn | flags | text
R325 | hedge qualifier | 516-517 | T39 Arnob Roy | MISSING_FROM_STRUCTURED, HEDGE | "we certainly should see a significant reduction of this inventory. That's all I can say, right?" (hedge plus limit on disclosure; adjacent R235, R315)
R326 | hedge qualifier | 590-591 | T48 Kumar N. Sivarajan | MISSING_FROM_STRUCTURED, NON_DISCLOSURE | "That's about all I can say. I cannot comment on the revenue numbers." (NEC supply; adjacent R243, R244, R320)
R327 | forward phrase | 524-526 | T41 Arnob Roy | MISSING_FROM_STRUCTURED, FORWARD | "with the collection of the past from the initial order ... milestones ... are due ... significant amount is going to come in" (collections inflow, unquantified, no date; adjacent R236, R237)
