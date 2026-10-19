=== A2 COUNT TEST ===
category: NUMBER    grep_count: 105   sweep_count: 105   header_count: 105   match: yes
category: ENTITY    grep_count: 43   sweep_count: 43   header_count: 43   match: yes
category: FORWARD   grep_count: 57   sweep_count: 57   header_count: 57   match: yes
category: DATE      grep_count: 37   sweep_count: 37   header_count: 37   match: yes
category: QUALIFIER grep_count: 92   sweep_count: 92   header_count: 92   match: yes
category: turns     grep_count: 65   sweep_count: 65   header_count: 65   match: yes
category: questions question_slots: 9   analyst_question_turns: 22   match: yes
ids_in_structured: 334 | ids_referenced_in_ledger: 334 | orphan_ids: [] | match: yes
missing_from_structured: 2 (M1 fulltext L325-326; M2 fulltext L453-454) | category mgmt_numbers/analyst figures: structured 105 + 2 added = 107 | sweep_count: 107 | match: yes
gate_a2: pass
=== END COUNT TEST ===

CAVEAT: MACHINE TRANSCRIPT (faster-whisper); all speakers SPEAKER_INFERRED; turns T1-T65 follow A1 SPEAKER TURN INDEX order. Filings win on any number conflict.

## 1. PARTICIPANTS
| ROW_ID | role | flags | note |
|---|---|---|---|
| R109 | Mgmt: Sudhir Rai, CMD | MGMT_ABSENCE_QA (speaks T4 opening only; no Q&A answers attributed) | present on call |
| R110 | Mgmt: Sumit Rai, full-time director | NAME_FLAG (R247) | answers trailer, extruded beam, seamless |
| R111 | Mgmt: Kunal Rai, full-time director | - | financials, receivables, debt |
| R112 | IR: Captify Consulting | - |  |
| R107 | Host: Iguira Securities (as spoken) | HOST_NAME_CONFLICT (R246) |  |
| R108 | Host: Ronald Jain, Aquarius Securities | HOST_NAME_CONFLICT (R246) |  |
| R126 | Analyst Q1: Anubhav Mukherjee, Pristine Tapati (as spoken) | - | |
| R127 | Analyst Q2: Pratish Chheda, Lucky Investment Manager (as spoken) | - | |
| R128 | Analyst Q3: Uncle Bodhar (likely Ankur Bohra), Swann Investment Manager (as spoken) | - | |
| R134 | Analyst Q4: Shubham Batra, Ambit Asset Management | - | |
| R136 | Analyst Q5: Vignesh IAF, Sequent Investments (as spoken) | - | |
| R137 | Analyst Q6: Rajat Agarwal, LQD Advisors NSP (as spoken) | - | |
| R140 | Analyst Q7: Dhvanil Shah, iWorld Fund (as spoken) | - | |
| R145 | Analyst Q8: Anubhav Mukherjee (follow-up), Brazil Capital (as spoken) | REPEATED_ANALYST (same as R126) | |
| R146 | Analyst Q9: Shubham Batra (question lost in audio gap), Ambit | REPEATED_ANALYST (same as R134) | |
Totals: management 3 (promoter CMD present, no promoter MGMT_ABSENCE), IR 1, host 1 firm (name conflict), analysts 7 unique / 9 question slots.

## 2. SPEAKER TURNS (65)
| turn | src_lines | speaker (inferred) |
|---|---|---|
| T1 | 5-5 | Moderator |
| T2 | 6-6 | Moderator hand to Ronald Jain |
| T3 | 7-12 | Ronald Jain (host, brokerage name unclear) |
| T4 | 13-73 | Sudhir Rai (CMD) opening remarks |
| T5 | 74-94 | Sumit Rai (as spoken) expansion |
| T6 | 95-113 | Kunal Rai financials |
| T7 | 114-119 | Moderator |
| T8 | 120-124 | Anubhav Mukherjee question |
| T9 | 125-136 | Sumit Rai answer (trailer) |
| T10 | 137-148 | Kunal Rai answer (parts business) |
| T11 | 149-150 | Anubhav Mukherjee follow-up |
| T12 | 151-159 | Sumit Rai answer (extruded beams) |
| T13 | 160-163 | Analyst on receivables, likely Anubhav Mukherjee (start of question cut) |
| T14 | 164-178 | Kunal Rai answer (receivables) |
| T15 | 179-183 | Moderator |
| T16 | 184-188 | Pratish Chheda |
| T17 | 189-198 | Management answer (Sumit/Kunal unclear) |
| T18 | 199-201 | Pratish Chheda |
| T19 | 202-218 | Kunal Rai / management answers volumes |
| T20 | 219-226 | Pratish Chheda and management exchange |
| T21 | 227-229 | Moderator |
| T22 | 230-232 | Moderator introduces Uncle Bodhar |
| T23 | 233-234 | Uncle Bodhar (likely Ankur Bohra) |
| T24 | 235-238 | Management answer (Kunal) |
| T25 | 239-244 | Uncle Bodhar / management |
| T26 | 245-255 | Management answer (Sumit/Kunal) |
| T27 | 256-259 | Uncle Bodhar |
| T28 | 260-270 | Sumit Rai answer (cold drawn tubes) |
| T29 | 271-277 | Exchange Uncle Bodhar / management |
| T30 | 278-279 | Moderator introduces Shubham Batra |
| T31 | 280-282 | Shubham Batra |
| T32 | 283-296 | Management answer (Kunal then Sumit) |
| T33 | 297-298 | Shubham Batra |
| T34 | 299-302 | Management answer |
| T35 | 303-306 | Shubham Batra |
| T36 | 307-319 | Sumit Rai answer (seamless capex) |
| T37 | 320-321 | Moderator introduces Vignesh IAF |
| T38 | 322-323 | Vignesh IAF |
| T39 | 324-338 | Management answer (capex) |
| T40 | 339-342 | Moderator / Rajat Agarwal |
| T41 | 343-349 | Management answer (debt) |
| T42 | 350-353 | Rajat Agarwal |
| T43 | 354-358 | Kunal Rai answer (debt) |
| T44 | 359-360 | Rajat Agarwal |
| T45 | 361-366 | Management answer (exports) |
| T46 | 367-369 | Rajat Agarwal |
| T47 | 370-377 | Kunal Rai answer (mix) |
| T48 | 378-378 | Rajat Agarwal |
| T49 | 379-382 | Moderator / Dhvanil Shah |
| T50 | 383-385 | Dhvanil Shah |
| T51 | 386-395 | Management answer |
| T52 | 396-401 | Dhvanil Shah |
| T53 | 402-413 | Management answer (competition) |
| T54 | 414-415 | Dhvanil Shah |
| T55 | 416-424 | Management answer (seamless) |
| T56 | 425-427 | Dhvanil Shah |
| T57 | 428-430 | Management answer |
| T58 | 431-438 | Dhvanil Shah / management |
| T59 | 439-443 | Moderator / Anubhav Mukherjee |
| T60 | 444-447 | Anubhav Mukherjee |
| T61 | 448-467 | Management answer (margins) |
| T62 | 468-471 | Moderator / Shubham Batra (question cut) |
| T63 | 472-473 | Moderator, no further questions (audio gap) |
| T64 | 474-483 | Management closing |
| T65 | 484-487 | Moderator closing |
Prepared remarks T4-T6 (3 turns); Q&A T7-T65 (59 turns incl. moderator).

## 3. QUESTION LEDGER
| Q | analyst | firm | topic | turns | ROW_ID | flags |
|---|---|---|---|---|---|---|
| Q1 | Anubhav Mukherjee | Pristine Tapati (as spoken) | trailer/component growth vs industry; extruded beam; receivables | T8, T11, T13 | R126 | REPEAT_QUESTION (receivables repeats in Q2) |
| Q2 | Pratish Chheda | Lucky Investment Manager (as spoken) | receivable days; extruded XLB utilisation; axle volumes | T16, T18 | R127 | REPEAT_QUESTION (receivables repeats Q1; axle volumes repeats in Q7) |
| Q3 | Uncle Bodhar (likely Ankur Bohra) | Swann Investment Manager (as spoken) | tipping jacks; agri/TAFE; cold drawn tubes | T23, T27 | R128 | - |
| Q4 | Shubham Batra | Ambit Asset Management | extruded beam share; trailer revenue; seamless capex | T31, T33, T35 | R134 | REPEAT_QUESTION (seamless capex repeats in Q5, Q6) |
| Q5 | Vignesh IAF | Sequent Investments (as spoken) | seamless capex spent / funding | T38 | R136 | REPEAT_QUESTION (seamless spend repeats Q4, Q6; answers conflict R304) |
| Q6 | Rajat Agarwal | LQD Advisors NSP (as spoken) | H2 capex, debt, exports, segment mix | T40, T42, T44, T46, T48 | R137 | REPEAT_QUESTION (capex funding and debt repeat Q4, Q5) |
| Q7 | Dhvanil Shah | iWorld Fund (as spoken) | axle/suspension volumes; competition; seamless benefit and margin | T50, T52, T54, T56 | R140 | REPEAT_QUESTION (axle volumes repeats Q2) |
| Q8 | Anubhav Mukherjee (follow-up) | Brazil Capital (as spoken) | cost recovery, gross margin Q2 vs Q1, guided margin | T60 | R145 | REPEAT_QUESTION (margin recovery; Q9 likely same) |
| Q9 | Shubham Batra (question lost in audio gap) | Ambit | UNKNOWN, lost 00:48:16-00:48:48 (R333) | T62 | R146 | AUDIO_GAP; possible REPEAT (margin) |

## 4. MANAGEMENT NUMBERS
| ROW_ID | turn | category | A2 flags | note |
|---|---|---|---|---|
| R001 | T4 (page 1, line 37) | mgmt_number | RESTATED (R015) | revenue from operations Q2 FY27 |
| R002 | T4 (page 1, line 37) | mgmt_number | RESTATED (R016) | revenue growth Q2 FY27 (basis not stated at this line) |
| R003 | T4 (page 1, line 37) | mgmt_number | NUMBER_CONFLICT (36 cr vs R017 30.6 cr) | IPITA (EBITDA, ASR) Q2 FY27 |
| R004 | T4 (page 1, line 37) | mgmt_number | - | IPITA margin Q2 FY27 |
| R005 | T4 (page 1, line 38) | mgmt_number | NUMBER_CONFLICT (196 million vs R021 19.69 cr) | profit after tax Q2 FY27 (as spoken; unit mismatch with crores) |
| R006 | T4 (page 1, line 39) | mgmt_number | - | PAT year-on-year change Q2 FY27 |
| R007 | T4 (page 1, line 40) | mgmt_number | RESTATED (R024) | revenue from operations H1 FY27 |
| R008 | T4 (page 1, line 41) | mgmt_number | RESTATED (R026) | TIPITA (EBITDA, ASR) H1 FY27 |
| R009 | T4 (page 1, line 41) | mgmt_number | UNIT_UNSTATED; RESTATED (R027) | profit after tax H1 FY27 (unit not stated here) |
| R010 | T4 (page 1, line 50) | mgmt_number | - | preferential issue size |
| R011 | T4 (page 1, line 64) | mgmt_number | - | historical H2 vs H1 uplift |
| R012 | T4 (page 1, line 70) | mgmt_number | RESTATED (R029, R046) | capacity utilization of extruded axle beam, of current output |
| R013 | T4 (page 1, line 82) | mgmt_number | RESTATED (R028) | exports share of component business |
| R014 | T4 (page 1, line 87) | mgmt_number | RESTATED (R160) | export growth this year vs previous year |
| R015 | T6 (page 1, line 115) | mgmt_number | RESTATED (R001) | revenue from operations Q2 FY27 |
| R016 | T6 (page 1, line 116) | mgmt_number | RESTATED (R002) | revenue growth Q2 FY27 |
| R017 | T6 (page 1, line 116) | mgmt_number | NUMBER_CONFLICT (vs R003) | EBITDA Q2 FY27 |
| R018 | T6 (page 1, line 116) | mgmt_number | - | EBITDA margin Q2 FY27 |
| R019 | T6 (page 1, line 117) | mgmt_number | UNIT_UNSTATED | CBT (PBT, ASR) Q2 FY27, unit crores not stated |
| R020 | T6 (page 1, line 117) | mgmt_number | - | CBT growth Q2 FY27 (period basis not stated) |
| R021 | T6 (page 1, line 118) | mgmt_number | NUMBER_CONFLICT (vs R005) | PAT Q2 FY27 |
| R022 | T6 (page 1, line 119) | mgmt_number | RESTATED (R092) | trailer segment share of Q2 revenue |
| R023 | T6 (page 1, line 120) | mgmt_number | RESTATED (R091) | component business share of Q2 revenue |
| R024 | T6 (page 1, line 121) | mgmt_number | RESTATED (R007) | H1 FY27 revenue |
| R025 | T6 (page 1, line 121) | mgmt_number | - | H1 FY26 revenue (last year) |
| R026 | T6 (page 1, line 122) | mgmt_number | RESTATED (R008) | EBITDA H1 FY27 |
| R027 | T6 (page 1, line 122) | mgmt_number | RESTATED (R009) | PAT H1 FY27 |
| R028 | T10 (page 2, line 163) | mgmt_number | RESTATED (R013) | exports share of total component business |
| R029 | T12 (page 2, line 171) | mgmt_number | - | axles rolling out with extrusion single piece beam |
| R030 | T12 (page 2, line 172) | mgmt_number | - | axles made conventionally |
| R031 | T13 (page 2, line 179) | mgmt_number | - | receivable days before FY24 |
| R032 | T13 (page 2, line 181) | mgmt_number | ANALYST_FIGURE | receivable days H1 balance sheet (analyst figure) |
| R033 | T14 (page 2, line 188) | mgmt_number | - | receivable days H1 last year |
| R034 | T14 (page 2, line 190) | mgmt_number | - | receivable days for Q2 |
| R035 | T14 (page 2, line 191) | mgmt_number | - | receivable days overall H1 |
| R036 | T14 (page 2, line 194) | mgmt_number | - | receivable days, export portion |
| R037 | T14 (page 2, line 195) | mgmt_number | - | export portion share of business |
| R038 | T14 (page 2, line 197) | mgmt_number | - | working capital cycle ceiling |
| R039 | T16 (page 2, line 204) | mgmt_number | ANALYST_FIGURE | utilization of extruded XLB (analyst quoting presentation) |
| R040 | T16 (page 2, line 205) | mgmt_number | ANALYST_FIGURE | expanded capacity (analyst figure) |
| R041 | T17 (page 2, line 209) | mgmt_number | RESTATED (R042 4,000 vs 4,200) | current production |
| R042 | T17 (page 2, line 209) | mgmt_number | RESTATED (R041) | current production (restated) |
| R043 | T17 (page 2, line 210) | mgmt_number | - | extruded beam share of axle output |
| R044 | T17 (page 2, line 212) | mgmt_number | ANALYST_FIGURE | original capacity (analyst figure) |
| R045 | T17 (page 2, line 214) | mgmt_number | - | manufacturing/sale base |
| R046 | T17 (page 2, line 215) | mgmt_number | - | extruded share today on 4,500 base |
| R047 | T19 (page 3, line 223) | mgmt_number | RESTATED (R096) | trailer axles Q2 FY27 volume |
| R048 | T19 (page 3, line 225) | mgmt_number | - | H1 axle/suspension volume (metric unclear) |
| R049 | T19 (page 3, line 229) | mgmt_number | ASR_GARBLE | volume growth H1 vs H1 last year |
| R050 | T19 (page 3, line 234) | mgmt_number | - | H1 volume growth |
| R051 | T19 (page 3, line 234) | mgmt_number | ASR_GARBLE | Q2 volume growth on 10,500 |
| R052 | T19 (page 3, line 237) | mgmt_number | ASR_GARBLE | Q2 trailer segment value growth (garbled) |
| R053 | T19 (page 3, line 237) | mgmt_number | - | quarter versus quarter growth |
| R054 | T19 (page 3, line 238) | mgmt_number | ASR_GARBLE | trailer segment Q1 FY27 value |
| R055 | T20 (page 3, line 239) | mgmt_number | ASR_GARBLE; VALUE_DROPPED | trailer Q2 value truncated |
| R056 | T20 (page 3, line 240) | mgmt_number | - | trailer segment Q2 FY26 value (units not stated) |
| R057 | T20 (page 3, line 241) | mgmt_number | ASR_GARBLE | trailer value, as spoken |
| R058 | T20 (page 3, line 242) | mgmt_number | - | trailer segment Q2 FY27 value (units not stated) |
| R059 | T20 (page 3, line 244) | mgmt_number | - | comparison base value |
| R060 | T20 (page 3, line 245) | mgmt_number | - | Q2 and H1 volume growth YoY |
| R061 | T24 (page 3, line 255) | mgmt_number | - | tipping jacks Q2 vs Q1 (no figure) |
| R062 | T24 (page 3, line 258) | mgmt_number | - | tipping jack capacity |
| R063 | T24 (page 3, line 258) | mgmt_number | - | expected capacity utilization by Q4 |
| R064 | T25 (page 3, line 261) | mgmt_number | - | realization per tipping set |
| R065 | T26 (page 3, line 268) | mgmt_number | - | TAFE planned production Oct-Nov |
| R066 | T28 (page 3, line 288) | mgmt_number | AMBIGUOUS_UNIT | capex for cold drawn tube and metal treatment |
| R067 | T31 (page 3, line 301) | mgmt_number | - | trailer axle revenue growth (QoQ, ASR) |
| R068 | T33 (page 4, line 318) | mgmt_number | ANALYST_FIGURE | trailer revenue in quarter (analyst, units dropped, likely crore) |
| R069 | T36 (page 4, line 328) | mgmt_number | - | seamless spent from term borrowing |
| R070 | T36 (page 4, line 333) | mgmt_number | ANALYST_FIGURE | analyst figure: spend in next six months |
| R071 | T36 (page 4, line 335) | mgmt_number | - | total budgeted seamless cost |
| R072 | T36 (page 4, line 336) | mgmt_number | NUMBER_CONFLICT (110 vs 70+60) | term loan funding |
| R073 | T36 (page 4, line 338) | mgmt_number | NUMBER_CONFLICT | own contribution |
| R074 | T36 (page 4, line 339) | mgmt_number | NUMBER_CONFLICT | term loan taken (firm term loan) |
| R075 | T36 (page 4, line 339) | mgmt_number | NUMBER_CONFLICT | spent (ASR "70 plus 50 120") |
| R076 | T36 (page 4, line 340) | mgmt_number | - | cash flow to date |
| R077 | T39 (page 4, line 346) | mgmt_number | - | capital being raised |
| R078 | T39 (page 4, line 351) | mgmt_number | - | balance seamless capex |
| R079 | T39 (page 4, line 353) | mgmt_number | NUMBER_CONFLICT (35 earlier debt vs R080 80, R086 115, R089 80, R090 32) | earlier debt |
| R080 | T39 (page 4, line 353) | mgmt_number | NUMBER_CONFLICT | debt now |
| R081 | T39 (page 4, line 359) | mgmt_number | ANALYST_FIGURE | analyst total capex H2 (50 + 60) |
| R082 | T40 (page 4, line 363) | mgmt_number | ASR_GARBLE; ANALYST_FIGURE | analyst debt guess end FY27 |
| R083 | T41 (page 4, line 365) | mgmt_number | NUMBER_CONFLICT (110.70 vs R072 110, R074 70, R073 60) | seamless funding total (as spoken) |
| R084 | T41 (page 4, line 366) | mgmt_number | - | from internal accruals |
| R085 | T41 (page 4, line 367) | mgmt_number | - | term loan cost |
| R086 | T42 (page 4, line 371) | mgmt_number | NUMBER_CONFLICT; ANALYST_FIGURE | total debt incl working capital (analyst) |
| R087 | T42 (page 4, line 373) | mgmt_number | - | undrawn |
| R088 | T42 (page 4, line 373) | mgmt_number | ANALYST_FIGURE | total debt incl undrawn (analyst) |
| R089 | T43 (page 4, line 375) | mgmt_number | - | total term loan |
| R090 | T43 (page 4, line 376) | mgmt_number | - | working capital and CC limit |
| R091 | T47 (page 4, line 395) | mgmt_number | RESTATED (R023) | component business Q2 share |
| R092 | T47 (page 4, line 396) | mgmt_number | RESTATED (R022) | trailer segment Q2 share |
| R093 | T47 (page 4, line 397) | mgmt_number | - | tractor segment share, all OEMs |
| R094 | T47 (page 4, line 398) | mgmt_number | - | largest customer share of top line |
| R095 | T50 (page 5, line 406) | mgmt_number | RESTATED (R096); ANALYST_FIGURE | axle volume Q2 (analyst recall) |
| R096 | T51 (page 5, line 412) | mgmt_number | RESTATED (R047) | axle volume Q2 |
| R097 | T51 (page 5, line 413) | mgmt_number | ANALYST_FIGURE | Q1 axle volume (analyst recall) |
| R098 | T51 (page 5, line 413) | mgmt_number | ANALYST_FIGURE | growth (analyst) |
| R099 | T55 (page 5, line 444) | mgmt_number | - | seamless cost vs existing buying price |
| R100 | T57 (page 5, line 451) | mgmt_number | - | margin benefit on axles/overall (answer) |
| R101 | T58 (page 5, line 457) | mgmt_number | ANALYST_FIGURE | phase one capacity share (analyst) |
| R102 | T58 (page 5, line 459) | mgmt_number | - | phase one capacity share (answer) |
| R103 | T61 (page 5, line 480) | mgmt_number | ANALYST_FIGURE | guided EBITDA margin (analyst) |
| R104 | T62 (page 5, line 492) | mgmt_number | ASR_GARBLE | CWIP/WC stat, unclear |
| R105 | T62 (page 5, line 493) | mgmt_number | ASR_GARBLE; VALUE_DROPPED | difference figure, truncated |

## 5. FORWARD COMMITMENTS
| ROW_ID | turn | category | A2 flags | note |
|---|---|---|---|---|
| R149 | T4 (page 1, line 42) | forward_commitment | - | capacity expansion |
| R150 | T4 (page 1, line 45) | forward_commitment | - | utilization outlook |
| R151 | T4 (page 1, line 47) | forward_commitment | - | capex posture |
| R152 | T4 (page 1, line 56) | forward_commitment | - | pricing benefit |
| R153 | T4 (page 1, line 57) | forward_commitment | - | management intent |
| R154 | T4 (page 1, line 63) | forward_commitment | - | volume outlook |
| R155 | T4 (page 1, line 64) | forward_commitment | HEDGE | seasonality, reads as forward |
| R156 | T4 (page 1, line 71) | forward_commitment | - | extruded beam benefit |
| R157 | T4 (page 1, line 73) | forward_commitment | RESTATED (R177) | 100% switch |
| R158 | T4 (page 1, line 77) | forward_commitment | - | agri outlook |
| R159 | T4 (page 1, line 84) | forward_commitment | - | export intent |
| R160 | T4 (page 1, line 87) | forward_commitment | RESTATED (R014) | export growth guidance |
| R161 | T5 (page 1, line 100) | forward_commitment | TIMELINE_WATCH (trials Feb/Mar 27 vs end Q4; equipment Nov/Dec) | seamless tube trials |
| R162 | T5 (page 1, line 101) | forward_commitment | - | seamless benefit |
| R163 | T5 (page 1, line 103) | forward_commitment | - | planned expansion |
| R164 | T5 (page 1, line 104) | forward_commitment | - | planned expansion |
| R165 | T5 (page 1, line 105) | forward_commitment | - | planned capex |
| R166 | T5 (page 1, line 106) | forward_commitment | - | funding plan |
| R167 | T5 (page 1, line 109) | forward_commitment | - | industry outlook |
| R168 | T5 (page 1, line 111) | forward_commitment | - | new products |
| R169 | T6 (page 2, line 125) | forward_commitment | - | utilization outlook |
| R170 | T6 (page 2, line 126) | forward_commitment | - | margin outlook |
| R171 | T6 (page 2, line 131) | forward_commitment | - | intent |
| R172 | T9 (page 2, line 150) | forward_commitment | HEDGE | trailer outlook |
| R173 | T10 (page 2, line 158) | forward_commitment | - | CV outlook |
| R174 | T14 (page 2, line 183) | forward_commitment | - | working capital outlook |
| R175 | T14 (page 2, line 196) | forward_commitment | - | receivable outlook |
| R176 | T14 (page 2, line 197) | forward_commitment | - | WC cycle outlook |
| R177 | T17 (page 2, line 211) | forward_commitment | RESTATED (R157) | extruded beam switch |
| R178 | T21 (page 3, line 248) | forward_commitment | PROCESS_NOT_FORWARD | process |
| R179 | T24 (page 3, line 257) | forward_commitment | - | tipping jack volume |
| R180 | T26 (page 3, line 274) | forward_commitment | - | agri Q3 outlook |
| R181 | T27 (page 3, line 277) | forward_commitment | - | presentation claim |
| R182 | T28 (page 3, line 281) | forward_commitment | - | plan |
| R183 | T32 (page 3, line 307) | forward_commitment | - | extruded beam |
| R184 | T33 (page 4, line 319) | forward_commitment | - | trailer revenue outlook |
| R185 | T34 (page 4, line 323) | forward_commitment | HEDGE | sustainability (sentence truncated) |
| R186 | T36 (page 4, line 332) | forward_commitment | TIMELINE_WATCH (trials Feb/Mar 27 vs end Q4; equipment Nov/Dec) | equipment timing |
| R187 | T36 (page 4, line 332) | forward_commitment | TIMELINE_WATCH (trials Feb/Mar 27 vs end Q4; equipment Nov/Dec) | trials timing |
| R188 | T39 (page 4, line 347) | forward_commitment | - | capex plan |
| R189 | T39 (page 4, line 348) | forward_commitment | - | capex purpose |
| R190 | T39 (page 4, line 351) | forward_commitment | - | remaining capex |
| R191 | T39 (page 4, line 355) | forward_commitment | - | H2 plan |
| R192 | T39 (page 4, line 357) | forward_commitment | - | timing |
| R193 | T41 (page 4, line 368) | forward_commitment | - | debt outlook |
| R194 | T41 (page 4, line 370) | forward_commitment | - | debt outlook |
| R195 | T51 (page 5, line 408) | forward_commitment | PROCESS_NOT_FORWARD | follow-up |
| R196 | T51 (page 5, line 417) | forward_commitment | PROCESS_NOT_FORWARD | follow-up |
| R197 | T54 (page 5, line 437) | forward_commitment | - | timing |
| R198 | T55 (page 5, line 438) | forward_commitment | - | seamless phase 1 |
| R199 | T55 (page 5, line 440) | forward_commitment | TIMELINE_WATCH (trials Feb/Mar 27 vs end Q4; equipment Nov/Dec) | timing |
| R200 | T55 (page 5, line 441) | forward_commitment | - | ramp |
| R201 | T55 (page 5, line 441) | forward_commitment | - | backward integration target |
| R202 | T57 (page 5, line 451) | forward_commitment | - | margin outlook |
| R203 | T61 (page 5, line 476) | forward_commitment | - | timing |
| R204 | T61 (page 5, line 485) | forward_commitment | RECOVERY_CLAIM | recovery claim |
| R205 | T61 (page 5, line 488) | forward_commitment | RECOVERY_CLAIM | recovery claim |

## 6. HEDGES (flagged HEDGE in tables): R155 R172 R185 R287 R307 R321 R322 R332

## 7. DATES
| ROW_ID | turn | category | A2 flags | note |
|---|---|---|---|---|
| R206 | T0 (page 1, line 18) | date | - | recording publication date |
| R207 | T0 (page 1, line 18) | date | - | call quarter |
| R208 | T1 (page 1, line 23) | date | - | call quarter |
| R209 | T3 (page 1, line 27) | date | - | post results call |
| R210 | T4 (page 1, line 32) | date | - | reporting period |
| R211 | T4 (page 1, line 32) | date | - | period end |
| R212 | T4 (page 1, line 36) | date | - | prior quarter (ASR FI=FY) |
| R213 | T4 (page 1, line 36) | date | - | current quarter |
| R214 | T4 (page 1, line 40) | date | - | half year |
| R215 | T4 (page 1, line 56) | date | - | forward periods |
| R216 | T4 (page 1, line 63) | date | - | periods |
| R217 | T4 (page 1, line 67) | date | - | prior record quarter |
| R218 | T4 (page 1, line 73) | date | - | switch timing |
| R219 | T4 (page 1, line 77) | date | - | period |
| R220 | T5 (page 1, line 100) | date | - | trial timing |
| R221 | T6 (page 1, line 114) | date | - | periods |
| R222 | T6 (page 1, line 115) | date | - | quarter end |
| R223 | T6 (page 2, line 125) | date | - | forward period |
| R224 | T9 (page 2, line 148) | date | - | monsoon timing |
| R225 | T9 (page 2, line 149) | date | - | demand timing |
| R226 | T9 (page 2, line 150) | date | - | periods |
| R227 | T10 (page 2, line 157) | date | - | GST timing |
| R228 | T13 (page 2, line 179) | date | - | period |
| R229 | T13 (page 2, line 180) | date | - | receivable stage |
| R230 | T14 (page 2, line 184) | date | - | slow CV period |
| R231 | T24 (page 3, line 257) | date | - | period |
| R232 | T26 (page 3, line 268) | date | - | production months |
| R233 | T34 (page 4, line 323) | date | - | period |
| R234 | T36 (page 4, line 332) | date | - | timing |
| R235 | T36 (page 4, line 333) | date | - | timing |
| R236 | T39 (page 4, line 347) | date | - | timing |
| R237 | T41 (page 4, line 368) | date | - | period |
| R238 | T42 (page 4, line 371) | date | DATE_CONFLICT (3rd Sept vs 30 Sept) | debt date, likely 30 September |
| R239 | T54 (page 5, line 437) | date | - | plant start per analyst |
| R240 | T55 (page 5, line 440) | date | - | timing |
| R241 | T55 (page 5, line 442) | date | - | timing |
| R242 | T61 (page 5, line 476) | date | - | periods |

## 8. QUALIFIERS
| ROW_ID | turn | category | A2 flags | note |
|---|---|---|---|---|
| R243 | T0 (page 1, line 19) | qualifier | - | transcript status |
| R244 | T0 (page 1, line 19) | qualifier | - | model switch, lower accuracy after 20:00 |
| R245 | T0 (page 1, line 20) | qualifier | - | proper-noun corrections applied to transcript |
| R246 | T2 (page 1, line 24) | qualifier | HOST_NAME_CONFLICT | host name inconsistent in machine text |
| R247 | T3 (page 1, line 29) | qualifier | NAME_FLAG (Sumit vs Sumeet) | name flag |
| R248 | T3 (page 1, line 30) | qualifier | SPEAKER_INCONSISTENCY | speaker inconsistency |
| R249 | T4 (page 1, line 37) | qualifier | - | ASR garble |
| R250 | T4 (page 1, line 38) | qualifier | NUMBER_CONFLICT | number conflict internal |
| R251 | T4 (page 1, line 51) | qualifier | - | volume qualifier, no figure |
| R252 | T4 (page 1, line 55) | qualifier | - | cost pressure statement |
| R253 | T4 (page 1, line 61) | qualifier | - | demand statement |
| R254 | T4 (page 1, line 67) | qualifier | - | record statement, no figure |
| R255 | T4 (page 1, line 76) | qualifier | - | statement |
| R256 | T5 (page 1, line 92) | qualifier | - | turn marker |
| R257 | T5 (page 1, line 98) | qualifier | - | schedule statement |
| R258 | T5 (page 1, line 110) | qualifier | - | demand statement |
| R259 | T6 (page 1, line 116) | qualifier | NUMBER_CONFLICT | number conflict internal |
| R260 | T6 (page 2, line 124) | qualifier | - | statement |
| R261 | T6 (page 2, line 127) | qualifier | - | capex use, no figure |
| R262 | T6 (page 2, line 129) | qualifier | - | statement |
| R263 | T7 (page 2, line 133) | qualifier | - | section marker |
| R264 | T8 (page 2, line 140) | qualifier | - | analyst premise |
| R265 | T9 (page 2, line 144) | qualifier | - | speaker handoff |
| R266 | T9 (page 2, line 146) | qualifier | - | trailer demand statement |
| R267 | T9 (page 2, line 152) | qualifier | - | demand reason |
| R268 | T9 (page 2, line 154) | qualifier | - | share gain statement |
| R269 | T10 (page 2, line 158) | qualifier | - | demand statement |
| R270 | T10 (page 2, line 160) | qualifier | - | statement |
| R271 | T10 (page 2, line 162) | qualifier | - | history |
| R272 | T10 (page 2, line 165) | qualifier | - | statement |
| R273 | T12 (page 2, line 174) | qualifier | DATE_DROPPED | date gap in ASR |
| R274 | T12 (page 2, line 175) | qualifier | - | customer feedback |
| R275 | T12 (page 2, line 177) | qualifier | - | statement |
| R276 | T14 (page 2, line 185) | qualifier | - | statement |
| R277 | T14 (page 2, line 186) | qualifier | - | statement |
| R278 | T14 (page 2, line 193) | qualifier | - | statement |
| R279 | T15 (page 2, line 199) | qualifier | - | turn marker |
| R280 | T19 (page 3, line 224) | qualifier | - | volume not stated |
| R281 | T19 (page 3, line 229) | qualifier | - | ASR ambiguity |
| R282 | T25 (page 3, line 264) | qualifier | - | analyst premise |
| R283 | T26 (page 3, line 266) | qualifier | - | statement |
| R284 | T26 (page 3, line 267) | qualifier | - | agri Q3 |
| R285 | T26 (page 3, line 269) | qualifier | - | statement |
| R286 | T26 (page 3, line 272) | qualifier | - | statement |
| R287 | T26 (page 3, line 273) | qualifier | HEDGE | hedge |
| R288 | T28 (page 3, line 282) | qualifier | - | process statement |
| R289 | T28 (page 3, line 286) | qualifier | - | statement |
| R290 | T28 (page 3, line 290) | qualifier | - | statement |
| R291 | T29 (page 3, line 292) | qualifier | - | answer to captive question |
| R292 | T29 (page 3, line 296) | qualifier | - | statement |
| R293 | T32 (page 3, line 303) | qualifier | - | share gain statement |
| R294 | T32 (page 3, line 304) | qualifier | - | statement |
| R295 | T32 (page 3, line 306) | qualifier | - | date statement |
| R296 | T32 (page 4, line 315) | qualifier | - | statement |
| R297 | T32 (page 4, line 317) | qualifier | - | statement |
| R298 | T34 (page 4, line 320) | qualifier | - | confirmation |
| R299 | T35 (page 4, line 325) | qualifier | - | question |
| R300 | T36 (page 4, line 330) | qualifier | - | status |
| R301 | T36 (page 4, line 332) | qualifier | - | status |
| R302 | T36 (page 4, line 335) | qualifier | - | correction |
| R303 | T36 (page 4, line 337) | qualifier | - | funding |
| R304 | T37 (page 4, line 341) | qualifier | NUMBER_CONFLICT | number conflict |
| R305 | T38 (page 4, line 344) | qualifier | - | question |
| R306 | T39 (page 4, line 352) | qualifier | - | statement |
| R307 | T39 (page 4, line 358) | qualifier | HEDGE | conditional hedge |
| R308 | T41 (page 4, line 364) | qualifier | - | statement |
| R309 | T42 (page 4, line 371) | qualifier | DATE_CONFLICT | ASR flag |
| R310 | T43 (page 4, line 377) | qualifier | - | statement |
| R311 | T45 (page 4, line 382) | qualifier | - | statement |
| R312 | T45 (page 4, line 385) | qualifier | - | status |
| R313 | T46 (page 4, line 388) | qualifier | - | question |
| R314 | T47 (page 4, line 393) | qualifier | - | non answer |
| R315 | T47 (page 4, line 398) | qualifier | - | statement |
| R316 | T50 (page 5, line 405) | qualifier | - | question |
| R317 | T51 (page 5, line 415) | qualifier | - | statement |
| R318 | T51 (page 5, line 416) | qualifier | - | statement |
| R319 | T53 (page 5, line 430) | qualifier | - | statement |
| R320 | T53 (page 5, line 432) | qualifier | - | statement |
| R321 | T53 (page 5, line 433) | qualifier | HEDGE | hedge |
| R322 | T55 (page 5, line 446) | qualifier | HEDGE | hedge |
| R323 | T58 (page 5, line 453) | qualifier | - | capacity, unclear |
| R324 | T58 (page 5, line 459) | qualifier | - | correction |
| R325 | T60 (page 5, line 466) | qualifier | - | analyst premise |
| R326 | T60 (page 5, line 468) | qualifier | - | analyst premise |
| R327 | T61 (page 5, line 471) | qualifier | - | statement |
| R328 | T61 (page 5, line 471) | qualifier | - | statement |
| R329 | T61 (page 5, line 473) | qualifier | - | statement |
| R330 | T61 (page 5, line 475) | qualifier | - | statement |
| R331 | T61 (page 5, line 479) | qualifier | - | statement |
| R332 | T61 (page 5, line 482) | qualifier | HEDGE | hedge |
| R333 | T63 (page 5, line 494) | qualifier | AUDIO_GAP (00:48:16-00:48:48) | coverage gap in source |
| R334 | T64 (page 5, line 496) | qualifier | - | section marker |

## 9. ENTITIES
| ROW_ID | turn | category | A2 flags | note |
|---|---|---|---|---|
| R106 | T1 (page 1, line 23) | entity/participant | - | company |
| R107 | T1 (page 1, line 23) | entity/participant | - | call host as spoken (ASR) |
| R108 | T2 (page 1, line 24) | entity/participant | - | host/moderator handover |
| R109 | T3 (page 1, line 28) | entity/participant | - | management |
| R110 | T3 (page 1, line 29) | entity/participant | - | management, as spoken |
| R111 | T3 (page 1, line 29) | entity/participant | - | management |
| R112 | T4 (page 1, line 35) | entity/participant | - | investor relation advisor |
| R113 | T4 (page 1, line 49) | entity/participant | - | funding instrument |
| R114 | T4 (page 1, line 56) | entity/participant | - | price revision counterparties |
| R115 | T4 (page 1, line 56) | entity/participant | - | price revision counterparty (corrected from Taiwan/TAFEA) |
| R116 | T4 (page 1, line 60) | entity/participant | - | segment heading (ASR) |
| R117 | T4 (page 1, line 65) | entity/participant | - | segment |
| R118 | T4 (page 1, line 68) | entity/participant | - | product |
| R119 | T4 (page 1, line 69) | entity/participant | - | product, commercial production commenced |
| R120 | T4 (page 1, line 75) | entity/participant | - | segment |
| R121 | T4 (page 1, line 80) | entity/participant | - | segment |
| R122 | T4 (page 1, line 90) | entity/participant | - | handover to expansion |
| R123 | T5 (page 1, line 98) | entity/participant | - | capex project |
| R124 | T5 (page 1, line 99) | entity/participant | - | equipment, received and installed |
| R125 | T5 (page 1, line 112) | entity/participant | - | handover to financials |
| R126 | T7 (page 2, line 138) | entity/participant | - | analyst Q1 |
| R127 | T15 (page 2, line 201) | entity/participant | - | analyst Q2 |
| R128 | T22 (page 3, line 250) | entity/participant | - | analyst Q3 |
| R129 | T23 (page 3, line 253) | entity/participant | - | product |
| R130 | T26 (page 3, line 268) | entity/participant | - | tractor customer |
| R131 | T28 (page 3, line 284) | entity/participant | - | internal use |
| R132 | T29 (page 3, line 293) | entity/participant | - | plant location |
| R133 | T29 (page 3, line 295) | entity/participant | - | cold drawing facilities elsewhere |
| R134 | T30 (page 3, line 299) | entity/participant | - | analyst Q4 |
| R135 | T32 (page 4, line 313) | entity/participant | - | region, good demand after long time |
| R136 | T37 (page 4, line 342) | entity/participant | - | analyst Q5 |
| R137 | T40 (page 4, line 360) | entity/participant | - | analyst Q6 |
| R138 | T45 (page 4, line 383) | entity/participant | - | customers |
| R139 | T45 (page 4, line 384) | entity/participant | - | customer |
| R140 | T49 (page 5, line 401) | entity/participant | - | analyst Q7 |
| R141 | T53 (page 5, line 424) | entity/participant | - | trailer competitor, market leader |
| R142 | T53 (page 5, line 426) | entity/participant | - | competitor (as spoken) |
| R143 | T53 (page 5, line 427) | entity/participant | - | competitor (as spoken) |
| R144 | T53 (page 5, line 427) | entity/participant | - | competitor |
| R145 | T59 (page 5, line 462) | entity/participant | - | analyst Q8 follow-up |
| R146 | T62 (page 5, line 490) | entity/participant | - | analyst Q9 |
| R147 | T64 (page 5, line 503) | entity/participant | - | IR contact |
| R148 | T65 (page 5, line 506) | entity/participant | - | host closing |

## 10. Other flags: ZERO_STANDING none (transcript). ENTITY_CHANGE and DROPPED_SLIDE n/a (no prior ledger). MISSING_FROM_STRUCTURED none.

## 11. MISSING_FROM_STRUCTURED (added in Role 5 loop 1, A5 finding M1)
| ROW_ID | turn | category | A2 flags | claim text |
|---|---|---|---|---|
| M1 | T35 (fulltext L325-326, 00:31:19-00:31:24; context: Shubham Batra seamless spend question, Q4 slot) | analyst_figure | MISSING_FROM_STRUCTURED; ANALYST_FIGURE; ASR_GARBLE | verbatim: "what is the amount that we are spent in now and what is the we are going to spend maybe 1 / 6 3 7 or 4 routes." Total budget figure garbled; plausibly 170 crores (cf. R071 approx 170 crores total seamless budget; analyst reading unconfirmed, not estimated). |
| M2 | T58 (fulltext L453-454, 00:44:50-00:44:53; context: Dhvanil Shah follow-up on seamless phase 1 capacity, Q7 slot; cf. R101, R102, R324) | analyst_figure | MISSING_FROM_STRUCTURED; ANALYST_FIGURE; ASR_GARBLE | verbatim: "And check this index tube is overall 1 leg capacity right. So phase 1 would be 2 percent of that." Percent figure (2) garbled; management then corrects to 30 percent (R102, R324). |

```yaml
stage: A2-enumerator
company: "KROSS"
quarter: "Q2 FY27"
doctype: "concall"
model: claude-sonnet-5-5
status: complete
ledger_path: "runs/kross-q2fy27/work/ledger_concall_kross_q2fy27.md"
counts:
  notes: 0
  line_items: 0
  zero_standing: 0
  agenda_items: 0
  auditor_paras: 0
  entities: 43
  turns: 65
  questions: 9
  mgmt_numbers: 107
  slides: 0
  slide_numbers: 0
flags_raised: [MISSING_FROM_STRUCTURED, REPEAT_QUESTION, MGMT_ABSENCE_QA, NUMBER_CONFLICT, DATE_CONFLICT, RESTATED, AUDIO_GAP, ASR_GARBLE, HEDGE, ANALYST_FIGURE, HOST_NAME_CONFLICT, NAME_FLAG, TIMELINE_WATCH]
ids_in_structured: 334
ids_referenced: 334
orphan_ids: []
missing_from_structured: ["M1: analyst figure 1 6 3 7 or 4 routes (fulltext L325-326, ASR garble of seamless budget; see R071)", "M2: analyst figure phase 1 would be 2 percent of that (fulltext L454, ASR garble; see R101, R102)"]
gate_a2: pass
mismatch_note: ""
analyst_note: "Counts reconcile (grep, sweep, A1 header). questions: 9 analyst slots across 22 analyst turns; 7 unique analysts. Seamless-tube funding was asked three times (Batra, Vignesh, Rajat) and the answers conflict (110 vs 70+60, 110.70, debt 35/80/115/165-170); A3 should treat R072-R090 as one cluster. Receivables and axle volumes also repeat. Sudhir Rai (CMD) speaks only in opening remarks; no Q&A answer is attributed to him, so MGMT_ABSENCE_QA is raised, not a promoter absence. Audio gap 00:48:16-00:48:48 (R333) lost a Batra question and answer, probably on margin. Seamless trial timing varies: Feb or Mar 2027, end Q4, equipment Nov or Dec. 15 NUMBER rows are analyst-spoken, so 90 are management numbers."
```
