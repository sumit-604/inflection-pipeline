# A2 LEDGER: INDIAMART Q2 FY27 concall (ASR machine transcript)

ids_in_structured: 614 | ids_referenced_in_ledger: 614 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: participants   grep_count: 25   sweep_count: 25   match: yes   (13 named people/firm rows analyst side + 12 mgmt/moderator rows, table 1)
category: turns          grep_count: 17   sweep_count: 17   match: yes   (SPEAKER_CHANGE R149-R165 = 17; fulltext sweep of question-intro and handoff lines agrees)
category: questions      grep_count: 9    sweep_count: 9    match: yes   (fulltext regex hit 13 lines: 9 question intros plus 4 non-intro lines (3 'Just one last question' style asides and the moderator closing 'last question for the day' at line 796); 6 live + 3 chat)
category: mgmt_numbers   grep_count: 254  sweep_count: 254  match: yes   (NUMBER rows excl. header line 1 R001-R002; independent fulltext sweep: 107 source lines carry a digit; 106 are rowed as digit NUMBER rows, line 179 is rowed via R044/R111 tokens, and 4 lines (249,385,637,714) are number-word lines A1 rowed as numbers; no line lacks a row)
category: forward        grep_count: 126  sweep_count: 126  match: yes
category: qualifiers     grep_count: 37   sweep_count: 37  match: yes
category: timestamps     grep_count: 806  sweep_count: 806  match: yes (anchors, not content)
gate_a2: pass
=== END COUNT TEST ===

## 1. Participants (ENTITY rows; side inferred from role text, unverified)
MGMT_ABSENCE: not raised. CEO, full-time director, CFO and CSO named (R096-R099); no speaker tags in ASR.

ROW_ID | category | A2 flags | note
R094 | participant-mgmt/moderator | NAME_VARIANT (ASR) | see QUALIFIER R232-R233
R096 | participant-mgmt/moderator | NAME_VARIANT (ASR) | see QUALIFIER R232-R233
R097 | participant-mgmt/moderator | NAME_VARIANT (ASR) | see QUALIFIER R232-R233
R098 | participant-mgmt/moderator | NAME_VARIANT (ASR) | see QUALIFIER R232-R233
R099 | participant-mgmt/moderator | NAME_VARIANT (ASR) | see QUALIFIER R232-R233
R100 | participant-mgmt/moderator | NAME_VARIANT (ASR) | see QUALIFIER R232-R233
R101 | participant-mgmt/moderator | NAME_VARIANT (ASR) | see QUALIFIER R232-R233
R105 | participant-mgmt/moderator | NAME_VARIANT (ASR) | see QUALIFIER R232-R233
R145 | participant-mgmt/moderator | NAME_VARIANT (ASR) | see QUALIFIER R232-R233
R147 | participant-mgmt/moderator | NAME_VARIANT (ASR) | see QUALIFIER R232-R233
R148 | participant-mgmt/moderator | NAME_VARIANT (ASR) | see QUALIFIER R232-R233
R102 | participant-mgmt/moderator | NAME_VARIANT (ASR) | see QUALIFIER R232-R233
R106 | participant-analyst | | questioner or firm
R107 | participant-analyst | | questioner or firm
R114 | participant-analyst | | questioner or firm
R115 | participant-analyst | | questioner or firm
R125 | participant-analyst | | questioner or firm
R126 | participant-analyst | | questioner or firm
R127 | participant-analyst | | questioner or firm
R128 | participant-analyst | | questioner or firm
R132 | participant-analyst | | questioner or firm
R137 | participant-analyst | | questioner or firm
R138 | participant-analyst | | questioner or firm
R139 | participant-analyst | | questioner or firm
R144 | participant-analyst | | questioner or firm

## 2. Speaker turns (sequential; turn starts at A1 SPEAKER_CHANGE row; answers sit in the segment to the next turn start)
TURN | START_ROW | start line | segment lines | label | IDs in segment
T01 | R149 | 3 | 3-14 | IR head opens (R149) | n=23 ids: R094,R095,R096,R097,R098,R099,R100,R149,R205,R226,R230,R231,R232,R233,R265,R266,R267,R268,R269,R270,R271,R272,R273
T02 | R150 | 15 | 15-57 | CEO opening (R150) | n=38 ids: R003,R004,R005,R006,R007,R008,R009,R010,R011,R012,R013,R101,R146,R150,R206,R240,R244,R274,R275,R276,R277,R278,R279,R280,R281,R282,R283,R284,R285,R286,R287,R288,R289,R290,R291,R292,R293,R294
T03 | R151 | 58 | 58-81 | Busy segment (R151) | n=21 ids: R014,R015,R016,R017,R018,R019,R020,R021,R022,R102,R103,R104,R151,R167,R168,R234,R295,R296,R297,R298,R299
T04 | R152 | 82 | 82-114 | CFO financials (R152) | n=47 ids: R023,R024,R025,R026,R027,R028,R029,R030,R031,R032,R033,R034,R035,R036,R105,R152,R166,R207,R235,R236,R237,R238,R239,R241,R242,R243,R300,R301,R302,R303,R304,R305,R306,R307,R308,R309,R310,R311,R312,R313,R314,R315,R316,R317,R318,R319,R320
T05 | R153 | 115 | 115-122 | Moderator opens Q&A (R153) | n=8 ids: R153,R321,R322,R323,R324,R325,R326,R327
T06 | R154 | 123 | 123-137 | Q1 Kunal Tanvi / Banyan Tree (R154) + answer | n=12 ids: R106,R107,R108,R109,R154,R328,R329,R330,R331,R332,R333,R334
T07 | R155 | 138 | 138-235 | CEO answer lead-in (R155) | n=76 ids: R037,R038,R039,R040,R041,R042,R043,R044,R045,R093,R110,R111,R112,R113,R155,R169,R170,R171,R172,R208,R209,R262,R335,R336,R337,R338,R339,R340,R341,R342,R343,R344,R345,R346,R347,R348,R349,R350,R351,R352,R353,R354,R355,R356,R357,R358,R359,R360,R361,R362,R363,R364,R365,R366,R367,R368,R369,R370,R371,R372,R373,R374,R375,R376,R377,R378,R379,R380,R381,R382,R383,R384,R385,R386,R387,R388
T08 | R156 | 236 | 236-390 | Q2 Amit Chandra / HDFC Sec (R156) + answer | n=77 ids: R046,R047,R048,R049,R050,R051,R114,R115,R116,R117,R118,R119,R120,R121,R122,R123,R124,R156,R173,R174,R175,R176,R177,R178,R210,R211,R212,R213,R214,R389,R390,R391,R392,R393,R394,R395,R396,R397,R398,R399,R400,R401,R402,R403,R404,R405,R406,R407,R408,R409,R410,R411,R412,R413,R414,R415,R416,R417,R418,R419,R420,R421,R422,R423,R424,R425,R426,R427,R428,R429,R430,R431,R432,R433,R434,R435,R436
T09 | R157 | 391 | 391-435 | Q3 Ritvik Agrawal / 3P Inv Mgrs (R157) + answer | n=80 ids: R052,R053,R054,R055,R056,R057,R058,R059,R060,R061,R062,R125,R126,R157,R179,R180,R181,R182,R183,R215,R216,R217,R218,R245,R246,R247,R248,R249,R437,R438,R439,R440,R441,R442,R443,R444,R445,R446,R447,R448,R449,R450,R451,R452,R453,R454,R455,R456,R457,R458,R459,R460,R461,R462,R463,R464,R465,R466,R467,R468,R469,R470,R471,R472,R473,R474,R475,R476,R477,R478,R479,R480,R481,R482,R483,R484,R485,R486,R487,R488
T10 | R158 | 436 | 436-552 | Q4 Abhishek Benarjee / ICICI Sec (R158) + answer | n=61 ids: R063,R064,R065,R066,R127,R128,R129,R130,R131,R158,R184,R185,R186,R187,R188,R189,R219,R220,R221,R222,R250,R251,R252,R253,R254,R489,R490,R491,R492,R493,R494,R495,R496,R497,R498,R499,R500,R501,R502,R503,R504,R505,R506,R507,R508,R509,R510,R511,R512,R513,R514,R515,R516,R517,R518,R519,R520,R521,R522,R523,R524
T11 | R159 | 553 | 553-578 | Q5 Ravi Purohit chat (R159) + answer | n=13 ids: R092,R132,R133,R134,R135,R136,R159,R190,R191,R525,R526,R527,R528
T12 | R160 | 579 | 579-611 | Q6 Ashwin R chat (R160) + answer | n=20 ids: R067,R068,R069,R137,R147,R160,R192,R193,R529,R530,R531,R532,R533,R534,R535,R536,R537,R538,R539,R540
T13 | R161 | 612 | 612-677 | Q7 Shreya Chatterjee / Ageless (R161) + answer | n=50 ids: R070,R071,R072,R073,R074,R075,R076,R138,R139,R140,R141,R161,R194,R195,R255,R260,R261,R263,R541,R542,R543,R544,R545,R546,R547,R548,R549,R550,R551,R552,R553,R554,R555,R556,R557,R558,R559,R560,R561,R562,R563,R564,R565,R566,R567,R568,R569,R570,R571,R572
T14 | R162 | 678 | 678-705 | Q8 Ashwin R chat (R162) + answer | n=13 ids: R142,R143,R148,R162,R196,R197,R198,R573,R574,R575,R576,R577,R578
T15 | R163 | 706 | 706-795 | Q9 Pranaj / Banyan Tree Advisors (R163) + answer | n=58 ids: R077,R078,R079,R080,R081,R082,R083,R084,R085,R086,R087,R088,R089,R090,R091,R144,R163,R199,R200,R201,R202,R203,R223,R256,R257,R258,R259,R579,R580,R581,R582,R583,R584,R585,R586,R587,R588,R589,R590,R591,R592,R593,R594,R595,R596,R597,R598,R599,R600,R601,R602,R603,R604,R605,R606,R607,R608,R609
T16 | R164 | 796 | 796-807 | Last-question handover to CEO (R164) | n=8 ids: R145,R164,R224,R225,R610,R611,R612,R613
T17 | R165 | 808 | 808-808 | IR closing (R165) | n=3 ids: R165,R227,R614
T00 | header | 1 | 1-2 | transcriber header | R001,R002,R204,R228,R229,R264

## 3. Questions ledger
Q# | START_ROW | turn | analyst | firm | mode | flags
Q1 | R154 | T06 | Kunal Tanvi | Banyan Tree | live | 
Q2 | R156 | T08 | Amit Chandra | HDFC Securities | live | 
Q3 | R157 | T09 | Ritvik Agrawal | 3P Investment Managers | live | 
Q4 | R158 | T10 | Abhishek Benarjee | ICICI Securities (ASR: ICCI) | live | 
Q5 | R159 | T11 | Ravi Purohit | chat | chat | 
Q6 | R160 | T12 | Ashwin R | chat | chat | 
Q7 | R161 | T13 | Shreya Chatterjee | Ageless Capital | live | 
Q8 | R162 | T14 | Ashwin R | chat | chat | REPEAT_QUESTION candidate (same asker as Q6; topic compare in A3)
Q9 | R163 | T15 | Pranaj | Banyan Tree Advisors | live | REPEAT_QUESTION candidate (Banyan family as Q1; topic compare in A3)

## 4. Management numbers (NUMBER rows; R001-R002 are HEADER). Speaker side unverified inside analyst-question segments.
ROW_ID | category | A2 flags | turn / line
R001 | number | HEADER | T00 line 1
R002 | number | HEADER | T00 line 1
R003 | number | MGMT_PREPARED | T02 line 24
R004 | number | MGMT_PREPARED | T02 line 25
R005 | number | MGMT_PREPARED | T02 line 26
R006 | number | MGMT_PREPARED | T02 line 27
R007 | number | MGMT_PREPARED | T02 line 28
R008 | number | MGMT_PREPARED | T02 line 29
R009 | number | MGMT_PREPARED | T02 line 30
R010 | number | MGMT_PREPARED | T02 line 31
R011 | number | MGMT_PREPARED | T02 line 33
R012 | number | MGMT_PREPARED | T02 line 38
R013 | number | MGMT_PREPARED | T02 line 38
R014 | number | MGMT_PREPARED | T03 line 63
R015 | number | MGMT_PREPARED | T03 line 64
R016 | number | MGMT_PREPARED | T03 line 65
R017 | number | MGMT_PREPARED | T03 line 66
R018 | number | MGMT_PREPARED | T03 line 67
R019 | number | MGMT_PREPARED | T03 line 68
R020 | number | MGMT_PREPARED | T03 line 69
R021 | number | MGMT_PREPARED | T03 line 70
R022 | number | MGMT_PREPARED | T03 line 71
R023 | number | MGMT_PREPARED | T04 line 90
R024 | number | MGMT_PREPARED | T04 line 91
R025 | number | MGMT_PREPARED | T04 line 93
R026 | number | MGMT_PREPARED | T04 line 94
R027 | number | MGMT_PREPARED | T04 line 95
R028 | number | MGMT_PREPARED | T04 line 96
R029 | number | MGMT_PREPARED | T04 line 98
R030 | number | MGMT_PREPARED | T04 line 99
R031 | number | MGMT_PREPARED | T04 line 100
R032 | number | MGMT_PREPARED | T04 line 101
R033 | number | MGMT_PREPARED | T04 line 102
R034 | number | MGMT_PREPARED | T04 line 107
R035 | number | MGMT_PREPARED | T04 line 109
R036 | number | MGMT_PREPARED | T04 line 111
R037 | number | SIDE_UNVERIFIED | T07 line 155
R038 | number | SIDE_UNVERIFIED | T07 line 155
R039 | number | SIDE_UNVERIFIED | T07 line 156
R040 | number | SIDE_UNVERIFIED | T07 line 164
R041 | number | SIDE_UNVERIFIED | T07 line 167
R042 | number | SIDE_UNVERIFIED | T07 line 168
R043 | number | SIDE_UNVERIFIED | T07 line 175
R044 | number | SIDE_UNVERIFIED | T07 line 179
R045 | number | SIDE_UNVERIFIED | T07 line 181
R046 | number | SIDE_UNVERIFIED | T08 line 249
R047 | number | SIDE_UNVERIFIED | T08 line 259
R048 | number | SIDE_UNVERIFIED | T08 line 262
R049 | number | SIDE_UNVERIFIED | T08 line 279
R050 | number | SIDE_UNVERIFIED | T08 line 294
R051 | number | SIDE_UNVERIFIED | T08 line 385
R052 | number | SIDE_UNVERIFIED | T09 line 403
R053 | number | SIDE_UNVERIFIED | T09 line 403
R054 | number | SIDE_UNVERIFIED | T09 line 407
R055 | number | SIDE_UNVERIFIED | T09 line 409
R056 | number | SIDE_UNVERIFIED | T09 line 409
R057 | number | SIDE_UNVERIFIED | T09 line 418
R058 | number | SIDE_UNVERIFIED | T09 line 426
R059 | number | SIDE_UNVERIFIED | T09 line 427
R060 | number | SIDE_UNVERIFIED | T09 line 428
R061 | number | SIDE_UNVERIFIED | T09 line 429
R062 | number | SIDE_UNVERIFIED | T09 line 434
R063 | number | SIDE_UNVERIFIED | T10 line 501
R064 | number | SIDE_UNVERIFIED | T10 line 502
R065 | number | SIDE_UNVERIFIED | T10 line 503
R066 | number | SIDE_UNVERIFIED | T10 line 504
R067 | number | SIDE_UNVERIFIED | T12 line 584
R068 | number | SIDE_UNVERIFIED | T12 line 592
R069 | number | SIDE_UNVERIFIED | T12 line 594
R070 | number | SIDE_UNVERIFIED | T13 line 636
R071 | number | SIDE_UNVERIFIED | T13 line 637
R072 | number | SIDE_UNVERIFIED | T13 line 644
R073 | number | SIDE_UNVERIFIED | T13 line 651
R074 | number | SIDE_UNVERIFIED | T13 line 652
R075 | number | SIDE_UNVERIFIED | T13 line 652
R076 | number | SIDE_UNVERIFIED | T13 line 661
R077 | number | SIDE_UNVERIFIED | T15 line 713
R078 | number | SIDE_UNVERIFIED | T15 line 714
R079 | number | SIDE_UNVERIFIED | T15 line 723
R080 | number | SIDE_UNVERIFIED | T15 line 723
R081 | number | SIDE_UNVERIFIED | T15 line 733
R082 | number | SIDE_UNVERIFIED | T15 line 733
R083 | number | SIDE_UNVERIFIED | T15 line 734
R084 | number | SIDE_UNVERIFIED | T15 line 735
R085 | number | SIDE_UNVERIFIED | T15 line 735
R086 | number | SIDE_UNVERIFIED | T15 line 737
R087 | number | SIDE_UNVERIFIED | T15 line 741
R088 | number | SIDE_UNVERIFIED | T15 line 753
R089 | number | SIDE_UNVERIFIED | T15 line 754
R090 | number | SIDE_UNVERIFIED | T15 line 779
R091 | number | SIDE_UNVERIFIED | T15 line 783
R092 | number | SIDE_UNVERIFIED | T11 line 566
R093 | number | SIDE_UNVERIFIED | T07 line 215
R265 | number | TOKEN_LEVEL | T01 line 4
R266 | number | TOKEN_LEVEL | T01 line 4
R273 | number | TOKEN_LEVEL | T01 line 12
R274 | number | MGMT_PREPARED,TOKEN_LEVEL | T02 line 16
R276 | number | MGMT_PREPARED,TOKEN_LEVEL | T02 line 17
R277 | number | MGMT_PREPARED,TOKEN_LEVEL | T02 line 24
R278 | number | MGMT_PREPARED,TOKEN_LEVEL | T02 line 24
R281 | number | MGMT_PREPARED,TOKEN_LEVEL | T02 line 27
R282 | number | MGMT_PREPARED,TOKEN_LEVEL | T02 line 27
R286 | number | MGMT_PREPARED,TOKEN_LEVEL | T02 line 30
R287 | number | MGMT_PREPARED,TOKEN_LEVEL | T02 line 30
R289 | number | MGMT_PREPARED,TOKEN_LEVEL | T02 line 32
R290 | number | MGMT_PREPARED,TOKEN_LEVEL | T02 line 32
R292 | number | MGMT_PREPARED,TOKEN_LEVEL | T02 line 37
R300 | number | MGMT_PREPARED,TOKEN_LEVEL | T04 line 88
R301 | number | MGMT_PREPARED,TOKEN_LEVEL | T04 line 88
R302 | number | MGMT_PREPARED,TOKEN_LEVEL | T04 line 90
R304 | number | MGMT_PREPARED,TOKEN_LEVEL | T04 line 93
R306 | number | MGMT_PREPARED,TOKEN_LEVEL | T04 line 98
R308 | number | MGMT_PREPARED,TOKEN_LEVEL | T04 line 100
R310 | number | MGMT_PREPARED,TOKEN_LEVEL | T04 line 103
R315 | number | MGMT_PREPARED,TOKEN_LEVEL | T04 line 107
R317 | number | MGMT_PREPARED,TOKEN_LEVEL | T04 line 109
R319 | number | MGMT_PREPARED,TOKEN_LEVEL | T04 line 111
R324 | number | TOKEN_LEVEL | T05 line 120
R328 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T06 line 125
R329 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T06 line 125
R330 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T06 line 127
R334 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T06 line 133
R337 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T07 line 146
R339 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T07 line 147
R340 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T07 line 149
R342 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T07 line 174
R343 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T07 line 174
R349 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T07 line 183
R350 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T07 line 195
R351 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T07 line 198
R353 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T07 line 202
R355 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T07 line 203
R359 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T07 line 207
R361 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T07 line 212
R362 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T07 line 216
R363 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T07 line 216
R364 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T07 line 216
R382 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T07 line 227
R389 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T08 line 248
R391 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T08 line 260
R393 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T08 line 261
R398 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T08 line 272
R400 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T08 line 276
R402 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T08 line 278
R404 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T08 line 292
R405 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T08 line 295
R406 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T08 line 295
R409 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T08 line 326
R411 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T08 line 335
R412 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T08 line 335
R413 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T08 line 335
R417 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T08 line 352
R418 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T08 line 362
R419 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T08 line 362
R421 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T08 line 364
R424 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T08 line 369
R426 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T08 line 383
R427 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T08 line 383
R428 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T08 line 383
R429 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T08 line 383
R432 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T08 line 384
R433 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T08 line 384
R434 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T08 line 386
R435 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T08 line 386
R437 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T09 line 391
R438 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T09 line 395
R439 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T09 line 395
R446 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T09 line 399
R447 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T09 line 399
R448 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T09 line 399
R449 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T09 line 399
R450 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T09 line 401
R452 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T09 line 404
R453 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T09 line 404
R455 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T09 line 405
R456 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T09 line 405
R459 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T09 line 408
R460 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T09 line 408
R464 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T09 line 410
R466 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T09 line 413
R467 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T09 line 413
R468 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T09 line 413
R471 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T09 line 414
R472 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T09 line 414
R474 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T09 line 415
R475 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T09 line 415
R476 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T09 line 415
R477 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T09 line 415
R480 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T09 line 417
R482 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T09 line 420
R483 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T09 line 422
R485 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T09 line 431
R488 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T09 line 434
R489 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T10 line 443
R501 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T10 line 469
R502 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T10 line 476
R503 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T10 line 480
R507 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T10 line 493
R511 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T10 line 497
R512 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T10 line 497
R517 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T10 line 505
R518 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T10 line 510
R520 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T10 line 537
R521 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T10 line 549
R522 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T10 line 549
R525 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T11 line 560
R526 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T11 line 565
R527 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T11 line 568
R529 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T12 line 580
R530 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T12 line 580
R531 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T12 line 581
R533 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T12 line 591
R536 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T12 line 605
R537 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T12 line 607
R541 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T13 line 624
R543 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T13 line 626
R545 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T13 line 627
R546 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T13 line 627
R547 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T13 line 633
R548 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T13 line 635
R549 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T13 line 635
R551 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T13 line 636
R552 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T13 line 637
R553 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T13 line 650
R554 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T13 line 650
R555 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T13 line 650
R563 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T13 line 666
R567 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T13 line 669
R568 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T13 line 669
R571 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T13 line 673
R578 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T14 line 704
R579 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T15 line 710
R581 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T15 line 713
R582 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T15 line 716
R583 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T15 line 717
R584 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T15 line 722
R588 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T15 line 734
R590 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T15 line 736
R591 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T15 line 736
R592 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T15 line 738
R593 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T15 line 742
R594 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T15 line 742
R595 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T15 line 742
R596 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T15 line 745
R597 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T15 line 745
R599 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T15 line 747
R600 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T15 line 748
R601 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T15 line 748
R602 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T15 line 749
R604 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T15 line 767
R605 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T15 line 769
R606 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T15 line 778
R608 | number | SIDE_UNVERIFIED,TOKEN_LEVEL | T15 line 787
R610 | number | TOKEN_LEVEL | T16 line 802
R611 | number | TOKEN_LEVEL | T16 line 802
R612 | number | TOKEN_LEVEL | T16 line 802

RESTATED: collections 443cr (R005,R023); revenue 429cr (R003,R029); revenue growth 10% (R004,R030); deferred revenue 2029cr (R007,R027); collection growth 9% (R006,R024); deferred growth 16% (R008,R028).

## 5. Forward-commitment / hedge phrases (FORWARD rows)
ROW_ID | category | A2 flags | turn / line
R166 | forward |  | T04 line 105
R167 | forward |  | T03 line 73
R168 | forward |  | T03 line 79
R169 | forward |  | T07 line 173
R170 | forward |  | T07 line 224
R171 | forward |  | T07 line 229
R172 | forward |  | T07 line 235
R173 | forward |  | T08 line 335
R174 | forward |  | T08 line 342
R175 | forward |  | T08 line 376
R176 | forward |  | T08 line 383
R177 | forward |  | T08 line 385
R178 | forward |  | T08 line 389
R179 | forward |  | T09 line 402
R180 | forward |  | T09 line 406
R181 | forward |  | T09 line 417
R182 | forward |  | T09 line 427
R183 | forward |  | T09 line 433
R184 | forward |  | T10 line 457
R185 | forward |  | T10 line 459
R186 | forward |  | T10 line 486
R187 | forward |  | T10 line 487
R188 | forward |  | T10 line 496
R189 | forward |  | T10 line 547
R190 | forward |  | T11 line 571
R191 | forward |  | T11 line 572
R192 | forward |  | T12 line 596
R193 | forward |  | T12 line 606
R194 | forward |  | T13 line 662
R195 | forward |  | T13 line 667
R196 | forward |  | T14 line 696
R197 | forward |  | T14 line 699
R198 | forward |  | T14 line 702
R199 | forward |  | T15 line 711
R200 | forward |  | T15 line 724
R201 | forward |  | T15 line 755
R202 | forward |  | T15 line 783
R203 | forward |  | T15 line 793
R267 | forward | TOKEN_LEVEL | T01 line 5
R268 | forward | TOKEN_LEVEL | T01 line 6
R271 | forward | TOKEN_LEVEL | T01 line 11
R272 | forward | TOKEN_LEVEL | T01 line 11
R293 | forward | TOKEN_LEVEL | T02 line 39
R295 | forward | TOKEN_LEVEL | T03 line 58
R298 | forward | TOKEN_LEVEL | T03 line 75
R299 | forward | TOKEN_LEVEL | T03 line 80
R312 | forward | TOKEN_LEVEL | T04 line 106
R313 | forward | TOKEN_LEVEL | T04 line 106
R321 | forward | TOKEN_LEVEL | T05 line 115
R322 | forward | TOKEN_LEVEL | T05 line 119
R323 | forward | TOKEN_LEVEL | T05 line 119
R325 | forward | TOKEN_LEVEL | T05 line 120
R326 | forward | TOKEN_LEVEL | T05 line 120
R327 | forward | TOKEN_LEVEL | T05 line 122
R331 | forward | TOKEN_LEVEL | T06 line 127
R332 | forward | TOKEN_LEVEL | T06 line 128
R333 | forward | TOKEN_LEVEL | T06 line 128
R335 | forward | TOKEN_LEVEL | T07 line 140
R336 | forward | TOKEN_LEVEL | T07 line 141
R341 | forward | TOKEN_LEVEL | T07 line 161
R346 | forward | TOKEN_LEVEL | T07 line 176
R347 | forward | TOKEN_LEVEL | T07 line 177
R352 | forward | TOKEN_LEVEL | T07 line 200
R354 | forward | TOKEN_LEVEL | T07 line 202
R356 | forward | TOKEN_LEVEL | T07 line 203
R358 | forward | TOKEN_LEVEL | T07 line 204
R360 | forward | TOKEN_LEVEL | T07 line 207
R368 | forward | TOKEN_LEVEL | T07 line 219
R369 | forward | TOKEN_LEVEL | T07 line 219
R372 | forward | TOKEN_LEVEL | T07 line 221
R373 | forward | TOKEN_LEVEL | T07 line 222
R374 | forward | TOKEN_LEVEL | T07 line 223
R375 | forward | TOKEN_LEVEL | T07 line 223
R381 | forward | TOKEN_LEVEL | T07 line 226
R383 | forward | TOKEN_LEVEL | T07 line 227
R384 | forward | TOKEN_LEVEL | T07 line 228
R385 | forward | TOKEN_LEVEL | T07 line 232
R386 | forward | TOKEN_LEVEL | T07 line 233
R387 | forward | TOKEN_LEVEL | T07 line 234
R388 | forward | TOKEN_LEVEL | T07 line 234
R390 | forward | TOKEN_LEVEL | T08 line 248
R396 | forward | TOKEN_LEVEL | T08 line 270
R397 | forward | TOKEN_LEVEL | T08 line 271
R403 | forward | TOKEN_LEVEL | T08 line 286
R408 | forward | TOKEN_LEVEL | T08 line 322
R416 | forward | TOKEN_LEVEL | T08 line 340
R423 | forward | TOKEN_LEVEL | T08 line 365
R440 | forward | TOKEN_LEVEL | T09 line 395
R442 | forward | TOKEN_LEVEL | T09 line 396
R443 | forward | TOKEN_LEVEL | T09 line 396
R444 | forward | TOKEN_LEVEL | T09 line 396
R445 | forward | TOKEN_LEVEL | T09 line 397
R451 | forward | TOKEN_LEVEL | T09 line 401
R457 | forward | TOKEN_LEVEL | T09 line 405
R481 | forward | TOKEN_LEVEL | T09 line 418
R484 | forward | TOKEN_LEVEL | T09 line 422
R490 | forward | TOKEN_LEVEL | T10 line 443
R494 | forward | TOKEN_LEVEL | T10 line 448
R495 | forward | TOKEN_LEVEL | T10 line 450
R499 | forward | TOKEN_LEVEL | T10 line 458
R506 | forward | TOKEN_LEVEL | T10 line 488
R519 | forward | TOKEN_LEVEL | T10 line 529
R528 | forward | TOKEN_LEVEL | T11 line 570
R532 | forward | TOKEN_LEVEL | T12 line 582
R534 | forward | TOKEN_LEVEL | T12 line 598
R535 | forward | TOKEN_LEVEL | T12 line 602
R539 | forward | TOKEN_LEVEL | T12 line 609
R540 | forward | TOKEN_LEVEL | T12 line 611
R559 | forward | TOKEN_LEVEL | T13 line 655
R560 | forward | TOKEN_LEVEL | T13 line 657
R561 | forward | TOKEN_LEVEL | T13 line 664
R564 | forward | TOKEN_LEVEL | T13 line 666
R566 | forward | TOKEN_LEVEL | T13 line 668
R573 | forward | TOKEN_LEVEL | T14 line 679
R574 | forward | TOKEN_LEVEL | T14 line 682
R575 | forward | TOKEN_LEVEL | T14 line 685
R576 | forward | TOKEN_LEVEL | T14 line 692
R577 | forward | TOKEN_LEVEL | T14 line 698
R585 | forward | TOKEN_LEVEL | T15 line 725
R586 | forward | TOKEN_LEVEL | T15 line 731
R587 | forward | TOKEN_LEVEL | T15 line 732
R598 | forward | TOKEN_LEVEL | T15 line 746
R603 | forward | TOKEN_LEVEL | T15 line 765
R607 | forward | TOKEN_LEVEL | T15 line 781
R609 | forward | TOKEN_LEVEL | T15 line 792
R614 | forward | TOKEN_LEVEL | T17 line 808

## 6. Dates / period markers (DATE rows)
ROW_ID | category | A2 flags | turn / line
R204 | date |  | T00 line 1
R205 | date |  | T01 line 4
R206 | date |  | T02 line 17
R207 | date |  | T04 line 88
R208 | date |  | T07 line 181
R209 | date |  | T07 line 179
R210 | date |  | T08 line 273
R211 | date |  | T08 line 279
R212 | date |  | T08 line 294
R213 | date |  | T08 line 363
R214 | date |  | T08 line 369
R215 | date |  | T09 line 399
R216 | date |  | T09 line 409
R217 | date |  | T09 line 417
R218 | date |  | T09 line 434
R219 | date |  | T10 line 501
R220 | date |  | T10 line 502
R221 | date |  | T10 line 503
R222 | date |  | T10 line 493
R223 | date |  | T15 line 793
R224 | date |  | T16 line 802
R225 | date |  | T16 line 806
R226 | date |  | T01 line 3
R227 | date |  | T17 line 808
R269 | date | TOKEN_LEVEL | T01 line 7
R270 | date | TOKEN_LEVEL | T01 line 10
R275 | date | TOKEN_LEVEL | T02 line 16
R279 | date | TOKEN_LEVEL | T02 line 24
R280 | date | TOKEN_LEVEL | T02 line 25
R283 | date | TOKEN_LEVEL | T02 line 27
R284 | date | TOKEN_LEVEL | T02 line 27
R285 | date | TOKEN_LEVEL | T02 line 29
R288 | date | TOKEN_LEVEL | T02 line 30
R291 | date | TOKEN_LEVEL | T02 line 32
R294 | date | TOKEN_LEVEL | T02 line 57
R296 | date | TOKEN_LEVEL | T03 line 66
R297 | date | TOKEN_LEVEL | T03 line 68
R303 | date | TOKEN_LEVEL | T04 line 90
R305 | date | TOKEN_LEVEL | T04 line 93
R307 | date | TOKEN_LEVEL | T04 line 98
R309 | date | TOKEN_LEVEL | T04 line 100
R311 | date | TOKEN_LEVEL | T04 line 103
R314 | date | TOKEN_LEVEL | T04 line 106
R316 | date | TOKEN_LEVEL | T04 line 107
R318 | date | TOKEN_LEVEL | T04 line 109
R320 | date | TOKEN_LEVEL | T04 line 111
R338 | date | TOKEN_LEVEL | T07 line 146
R344 | date | TOKEN_LEVEL | T07 line 174
R345 | date | TOKEN_LEVEL | T07 line 174
R348 | date | TOKEN_LEVEL | T07 line 180
R357 | date | TOKEN_LEVEL | T07 line 203
R365 | date | TOKEN_LEVEL | T07 line 216
R366 | date | TOKEN_LEVEL | T07 line 216
R367 | date | TOKEN_LEVEL | T07 line 216
R370 | date | TOKEN_LEVEL | T07 line 220
R371 | date | TOKEN_LEVEL | T07 line 220
R376 | date | TOKEN_LEVEL | T07 line 223
R377 | date | TOKEN_LEVEL | T07 line 223
R378 | date | TOKEN_LEVEL | T07 line 224
R379 | date | TOKEN_LEVEL | T07 line 224
R380 | date | TOKEN_LEVEL | T07 line 224
R392 | date | TOKEN_LEVEL | T08 line 260
R394 | date | TOKEN_LEVEL | T08 line 261
R395 | date | TOKEN_LEVEL | T08 line 265
R399 | date | TOKEN_LEVEL | T08 line 272
R401 | date | TOKEN_LEVEL | T08 line 276
R407 | date | TOKEN_LEVEL | T08 line 295
R410 | date | TOKEN_LEVEL | T08 line 326
R414 | date | TOKEN_LEVEL | T08 line 335
R415 | date | TOKEN_LEVEL | T08 line 335
R420 | date | TOKEN_LEVEL | T08 line 362
R422 | date | TOKEN_LEVEL | T08 line 364
R425 | date | TOKEN_LEVEL | T08 line 381
R430 | date | TOKEN_LEVEL | T08 line 383
R431 | date | TOKEN_LEVEL | T08 line 383
R436 | date | TOKEN_LEVEL | T08 line 386
R441 | date | TOKEN_LEVEL | T09 line 395
R454 | date | TOKEN_LEVEL | T09 line 404
R458 | date | TOKEN_LEVEL | T09 line 405
R461 | date | TOKEN_LEVEL | T09 line 408
R462 | date | TOKEN_LEVEL | T09 line 408
R463 | date | TOKEN_LEVEL | T09 line 409
R465 | date | TOKEN_LEVEL | T09 line 410
R469 | date | TOKEN_LEVEL | T09 line 413
R470 | date | TOKEN_LEVEL | T09 line 413
R473 | date | TOKEN_LEVEL | T09 line 414
R478 | date | TOKEN_LEVEL | T09 line 415
R479 | date | TOKEN_LEVEL | T09 line 415
R486 | date | TOKEN_LEVEL | T09 line 431
R487 | date | TOKEN_LEVEL | T09 line 431
R491 | date | TOKEN_LEVEL | T10 line 443
R492 | date | TOKEN_LEVEL | T10 line 444
R493 | date | TOKEN_LEVEL | T10 line 445
R496 | date | TOKEN_LEVEL | T10 line 450
R497 | date | TOKEN_LEVEL | T10 line 454
R498 | date | TOKEN_LEVEL | T10 line 455
R500 | date | TOKEN_LEVEL | T10 line 464
R504 | date | TOKEN_LEVEL | T10 line 480
R505 | date | TOKEN_LEVEL | T10 line 482
R508 | date | TOKEN_LEVEL | T10 line 494
R509 | date | TOKEN_LEVEL | T10 line 495
R510 | date | TOKEN_LEVEL | T10 line 496
R513 | date | TOKEN_LEVEL | T10 line 497
R514 | date | TOKEN_LEVEL | T10 line 497
R515 | date | TOKEN_LEVEL | T10 line 497
R516 | date | TOKEN_LEVEL | T10 line 499
R523 | date | TOKEN_LEVEL | T10 line 549
R524 | date | TOKEN_LEVEL | T10 line 549
R538 | date | TOKEN_LEVEL | T12 line 607
R542 | date | TOKEN_LEVEL | T13 line 624
R544 | date | TOKEN_LEVEL | T13 line 626
R550 | date | TOKEN_LEVEL | T13 line 635
R556 | date | TOKEN_LEVEL | T13 line 650
R557 | date | TOKEN_LEVEL | T13 line 650
R558 | date | TOKEN_LEVEL | T13 line 651
R562 | date | TOKEN_LEVEL | T13 line 664
R565 | date | TOKEN_LEVEL | T13 line 666
R569 | date | TOKEN_LEVEL | T13 line 669
R570 | date | TOKEN_LEVEL | T13 line 669
R572 | date | TOKEN_LEVEL | T13 line 673
R580 | date | TOKEN_LEVEL | T15 line 712
R589 | date | TOKEN_LEVEL | T15 line 734
R613 | date | TOKEN_LEVEL | T16 line 806

## 7. Other entities (incl. speaker-change rows)
ROW_ID | category | A2 flags | turn / line
R095 | entity |  | T01 line 4
R103 | entity |  | T03 line 63
R104 | entity |  | T03 line 72
R108 | entity |  | T06 line 131
R109 | entity |  | T06 line 134
R110 | entity |  | T07 line 154
R111 | entity |  | T07 line 179
R112 | entity | CLOSED_BUSINESS | T07 line 180
R113 | entity | NEW_INITIATIVE | T07 line 182
R116 | entity |  | T08 line 316
R117 | entity |  | T08 line 316
R118 | entity |  | T08 line 316
R119 | entity |  | T08 line 316
R120 | entity |  | T08 line 317
R121 | entity |  | T08 line 317
R122 | entity |  | T08 line 263
R123 | entity |  | T08 line 278
R124 | entity |  | T08 line 363
R129 | entity | SUBSIDIARY_AS_HEARD | T10 line 472
R130 | entity | SUBSIDIARY_AS_HEARD | T10 line 473
R131 | entity | SUBSIDIARY_AS_HEARD | T10 line 524
R133 | entity | EXAMPLE_ENTITY | T11 line 554
R134 | entity | EXAMPLE_ENTITY | T11 line 564
R135 | entity | EXAMPLE_ENTITY | T11 line 564
R136 | entity | EXAMPLE_ENTITY | T11 line 565
R140 | entity |  | T13 line 643
R141 | entity | EXAMPLE_ENTITY | T13 line 658
R142 | entity |  | T14 line 679
R143 | entity |  | T14 line 683
R146 | entity |  | T02 line 35
R149 | entity |  | speaker-change row, see turn table
R150 | entity |  | speaker-change row, see turn table
R151 | entity |  | speaker-change row, see turn table
R152 | entity |  | speaker-change row, see turn table
R153 | entity |  | speaker-change row, see turn table
R154 | entity |  | speaker-change row, see turn table
R155 | entity |  | speaker-change row, see turn table
R156 | entity |  | speaker-change row, see turn table
R157 | entity |  | speaker-change row, see turn table
R158 | entity |  | speaker-change row, see turn table
R159 | entity |  | speaker-change row, see turn table
R160 | entity |  | speaker-change row, see turn table
R161 | entity |  | speaker-change row, see turn table
R162 | entity |  | speaker-change row, see turn table
R163 | entity |  | speaker-change row, see turn table
R164 | entity |  | speaker-change row, see turn table
R165 | entity |  | speaker-change row, see turn table

## 8. Qualifiers
ROW_ID | category | A2 flags | turn / line
R228 | qualifier | ASR_CAVEAT | T00 line 1
R229 | qualifier | ASR_CAVEAT | T00 line 1
R230 | qualifier | ASR_CAVEAT | T01 line 10
R231 | qualifier | ASR_CAVEAT | T01 line 12
R232 | qualifier | ASR_CAVEAT | T01 line 7
R233 | qualifier | ASR_CAVEAT | T01 line 8
R234 | qualifier | ASR_CAVEAT | T03 line 64
R235 | qualifier | ASR_CAVEAT | T04 line 91
R236 | qualifier | ASR_CAVEAT | T04 line 94
R237 | qualifier | ASR_CAVEAT | T04 line 95
R238 | qualifier | ASR_CAVEAT | T04 line 96
R239 | qualifier | ASR_CAVEAT | T04 line 99
R240 | qualifier | ASR_CAVEAT | T02 line 36
R241 | qualifier | ASR_CAVEAT | T04 line 93
R242 | qualifier | ASR_CAVEAT | T04 line 103
R243 | qualifier | ASR_CAVEAT | T04 line 105
R244 | qualifier | ASR_CAVEAT | T02 line 34
R245 | qualifier | ASR_CAVEAT | T09 line 407
R246 | qualifier | ASR_CAVEAT | T09 line 411
R247 | qualifier | ASR_CAVEAT | T09 line 429
R248 | qualifier | ASR_CAVEAT | T09 line 431
R249 | qualifier | ASR_CAVEAT | T09 line 431
R250 | qualifier | ASR_CAVEAT | T10 line 469
R251 | qualifier | ASR_CAVEAT | T10 line 475
R252 | qualifier | ASR_CAVEAT | T10 line 479
R253 | qualifier | ASR_CAVEAT | T10 line 480
R254 | qualifier | ASR_CAVEAT | T10 line 484
R255 | qualifier | ASR_CAVEAT | T13 line 635
R256 | qualifier | ASR_CAVEAT | T15 line 721
R257 | qualifier | ASR_CAVEAT | T15 line 735
R258 | qualifier | ASR_CAVEAT | T15 line 737
R259 | qualifier | ASR_CAVEAT | T15 line 734
R260 | qualifier | ASR_CAVEAT | T13 line 644
R261 | qualifier | ASR_CAVEAT | T13 line 666
R262 | qualifier | ASR_CAVEAT | T07 line 156
R263 | qualifier | ASR_CAVEAT | T13 line 661
R264 | qualifier | ASR_CAVEAT | T00 line 1
