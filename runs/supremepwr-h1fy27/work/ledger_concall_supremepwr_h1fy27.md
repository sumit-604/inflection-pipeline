# A2 LEDGER: SUPREMEPWR concall H1 FY27 (ASR; speaker turns ASR-INFERRED)

ids_in_structured: 344 | ids_referenced_in_ledger: 344 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: participants     grep_count: 16  sweep_count: 16  match: yes   (moderator unnamed, host, CMD, 10 analysts, Arvind self-named, closing host rows)
category: turns            grep_count: 99  sweep_count: 99  match: yes   ({'MGMT': 35, 'ANALYST': 41, 'MOD': 16, 'HOST': 2, 'MIXED': 5})
category: questions        grep_count: 41  sweep_count: 41  match: yes   (analyst-labelled turns; 5 MIXED exchange turns carry further questions; 10 analysts, 9 substantive, Q5 audio failure)
category: mgmt_numbers     grep_count: 95  sweep_count: 95  match: yes   (123 NUMBER - 25 analyst-tagged - R001,R002,R121 non-management)
category: entity_rows      grep_count: 43  sweep_count: 43  match: yes
category: forward_rows     grep_count: 80  sweep_count: 80  match: yes
category: date_rows        grep_count: 25  sweep_count: 25  match: yes
category: qualifier_rows   grep_count: 73  sweep_count: 73  match: yes
category: zero_standing    grep_count: 1   sweep_count: 1   match: yes   (R105)
gate_a2: pass
=== END COUNT TEST ===

Turn numbers for rows derive from A1 turn line ranges (fulltext lines); ASR-inferred.

## 1. PARTICIPANTS
ROW ID | category | flags | note
R122 | participant |  | host, IR firm Kiran Advisors
R123 | participant |  | host speaker
R124 | participant | CMD_PRESENT; no other management designation in structured file (CFO NOT FOUND) | CMD V Rajamon, management
R137 | participant |  | self-named speaker Arvind in Q1
R136 | participant |  | Analyst Q1
R138 | participant |  | Analyst Q2
R139 | participant |  | Analyst Q3
R140 | participant |  | Analyst Q4
R141 | participant |  | Analyst Q5
R142 | participant |  | Analyst Q6
R143 | participant |  | Analyst Q7
R144 | participant |  | Analyst Q8
R145 | participant |  | Analyst Q9
R146 | participant |  | Analyst Q10 individual investor
R162 | participant |  | closing host
R164 | participant |  | host closing address

MGMT_ABSENCE: none for CMD (present).

## 2. SPEAKER TURNS
TURN | category | flags | structured IDs by line | note
T01 | turn:MOD |  | R122,R123,R230,R255 | lines 31-39; Moderator: opening and hand-over
T02 | turn:HOST |  | R124 | lines 40-47; Host (Kiran Advisors): introduction
T03 | turn:MGMT |  | R003,R004,R005,R006,R007,R008,R009,R010,R011,R012,R013,R014,R015,R016,R017,R018,R129,R130,R131,R132,R133,R134,R165,R166,R167,R168,R169,R170,R171,R172,R173,R174,R231,R232,R233,R234,R235,R256,R257,R258,R263,R264,R265,R266,R267,R268,R269,R270,R271,R272,R312,R313 | lines 48-113; Management (CMD): opening remarks
T04 | turn:MOD |  | R121 | lines 114-120; Moderator: Q&A instructions
T05 | turn:MOD |  | R136 | lines 121-122; Moderator: introduces Q1 (Carbeth Coel, Serini Alpha)
T06 | turn:ANALYST |  | R137,R236,R237,R262,R273 | lines 123-134; Analyst Q1: questions on H2 orders, year-end order book
T07 | turn:MGMT |  | R019,R159,R175 | lines 135-145; Management: reply
T08 | turn:ANALYST |  | R020,R021,R240,R274,R275 | lines 146-148; Analyst Q1: follow-up on revenue guidance
T09 | turn:MGMT |  | R022,R023,R024,R176,R177,R276,R277 | lines 149-152; Management: reply
T10 | turn:ANALYST |  | R025,R238,R261 | lines 153-164; Analyst Q1: margin question
T11 | turn:MGMT |  | R026,R027,R028,R029,R178,R179,R181 | lines 165-172; Management: reply
T12 | turn:ANALYST |  | - | lines 173-178; Analyst Q1: follow-up on 9 to 12%
T13 | turn:MGMT |  | R030,R180,R239,R310,R311 | lines 179-186; Management: reply
T14 | turn:ANALYST |  | R031 | lines 187-191; Analyst Q1: closing
T15 | turn:MOD |  | R138 | lines 192-195; Moderator: introduces Q2 (Tisha, fire capital)
T16 | turn:ANALYST |  | - | lines 196-202; Analyst Q2: procurement, execution risk
T17 | turn:MGMT |  | R032,R120,R135,R182,R314 | lines 203-214; Management: reply
T18 | turn:ANALYST |  | R147,R148,R278 | lines 215-217; Analyst Q2: Tamil Nadu capacity
T19 | turn:MIXED |  | R033,R034,R035,R036,R037,R184,R185,R279,R280,R281 | lines 218-240; Management/Analyst: clarification exchange
T20 | turn:ANALYST |  | - | lines 241-242; Analyst Q2: final unit timing
T21 | turn:MGMT |  | R183 | lines 243-243; Management: reply
T22 | turn:ANALYST |  | - | lines 244-246; Analyst Q2: power vs distribution margin
T23 | turn:MGMT |  | R038,R160,R186,R323 | lines 247-254; Management: reply
T24 | turn:MOD |  | - | lines 255-255; Moderator: interrupts, requests re-queue
T25 | turn:ANALYST |  | - | lines 256-258; Analyst Q2: follow-up on order mix
T26 | turn:MGMT |  | R039,R040,R041,R042,R043,R044,R045,R046,R047,R048,R049,R161,R282,R283,R284 | lines 259-261; Management: order book product mix
T27 | turn:ANALYST |  | - | lines 262-262; Analyst Q2: pipeline mix
T28 | turn:MGMT |  | R224,R316 | lines 263-263; Management: reply
T29 | turn:ANALYST |  | - | lines 264-265; Analyst Q2: closing
T30 | turn:MOD |  | R139 | lines 266-266; Moderator: introduces Q3 (Mukesh Majwani, WC securities)
T31 | turn:ANALYST |  | R050 | lines 267-269; Analyst Q3: execution timeline question
T32 | turn:MGMT |  | R051,R052,R189,R241,R308 | lines 270-270; Management: reply
T33 | turn:MIXED |  | R053,R054,R055,R056,R187,R188,R242 | lines 271-278; Analyst/Management: H2 execution exchange
T34 | turn:MOD |  | R140 | lines 279-279; Moderator: introduces Q4 (Paras Chedha)
T35 | turn:ANALYST |  | R057,R243,R260,R285 | lines 280-282; Analyst Q4: peak revenue verification
T36 | turn:MGMT |  | R058,R059,R060,R190,R191 | lines 283-284; Management: reply
T37 | turn:ANALYST |  | R061,R062,R063 | lines 285-286; Analyst Q4: customer requirement vs guidance
T38 | turn:MGMT |  | R064,R065,R066,R192,R193,R286,R287,R309 | lines 287-291; Management: reply
T39 | turn:ANALYST |  | R067 | lines 292-297; Analyst Q4: operating leverage
T40 | turn:MGMT | ASR_GAP | R194,R318 | lines 298-300; Management: reply (truncated)
T41 | turn:ANALYST |  | - | lines 301-303; Analyst Q4: working capital
T42 | turn:MGMT |  | R068,R069,R070,R195 | lines 304-310; Management: reply
T43 | turn:ANALYST |  | - | lines 311-312; Analyst Q4: cash flow
T44 | turn:MGMT |  | R196 | lines 313-313; Management: reply
T45 | turn:ANALYST |  | - | lines 314-317; Analyst Q4: demand outlook
T46 | turn:MGMT |  | R071,R197 | lines 318-321; Management: reply
T47 | turn:ANALYST |  | R198 | lines 322-322; Analyst Q4: capacity expansion
T48 | turn:MGMT |  | R199 | lines 323-324; Management: reply
T49 | turn:MOD | ASR_GAP | R141,R319,R320 | lines 325-334; Moderator: introduces Q5 (Mohammed Amir); audio failure
T50 | turn:MOD | ASR_GAP | - | lines 335-342; Moderator: audio failure, asks re-queue
T51 | turn:MOD |  | R142 | lines 344-344; Moderator: introduces Q6 (Walford PMS)
T52 | turn:ANALYST |  | - | lines 345-351; Analyst Q6: ramp-up, utilization
T53 | turn:MGMT |  | R072,R073,R200,R201,R244,R299 | lines 352-353; Management: reply
T54 | turn:ANALYST |  | - | lines 354-355; Analyst Q6: MVA delivered
T55 | turn:MGMT |  | R225,R315 | lines 356-357; Management: reply
T56 | turn:ANALYST |  | - | lines 358-364; Analyst Q6: closing
T57 | turn:MOD |  | R143 | lines 365-366; Moderator: introduces Q7 (Mahesh Atal)
T58 | turn:ANALYST |  | R077 | lines 367-370; Analyst Q7: power vs distribution split
T59 | turn:MGMT |  | R074,R288 | lines 371-372; Management: reply
T60 | turn:ANALYST |  | R075,R289 | lines 373-379; Analyst Q7: margin with power mix
T61 | turn:MGMT |  | R076,R290 | lines 380-384; Management: reply
T62 | turn:ANALYST |  | R078,R291 | lines 385-387; Analyst Q7: government vs private
T63 | turn:MGMT |  | R079,R080,R081,R292 | lines 388-389; Management: reply
T64 | turn:ANALYST |  | - | lines 390-390; Analyst Q7: same for current year
T65 | turn:MGMT |  | R202,R317 | lines 391-392; Management: reply
T66 | turn:ANALYST |  | - | lines 393-393; Analyst Q7: receivable cycle
T67 | turn:MGMT |  | R084,R085,R086,R087,R088 | lines 394-399; Management: reply
T68 | turn:ANALYST |  | - | lines 400-401; Analyst Q7: government strategy
T69 | turn:MGMT |  | R089,R090,R091,R149,R203,R204,R293,R294,R295 | lines 402-409; Management: reply
T70 | turn:MIXED |  | R082,R083,R205 | lines 410-415; Analyst/Management: closing exchange
T71 | turn:MOD |  | R144 | lines 416-416; Moderator: introduces Q8 (Sunil Kateshia)
T72 | turn:ANALYST |  | R092,R093,R094,R095,R096,R206,R245,R246,R296 | lines 417-424; Analyst Q8: capacity, long-term plan
T73 | turn:MIXED |  | R097,R098,R099,R100,R101,R151,R207,R208,R209,R210,R211,R297 | lines 425-449; Management/Analyst: expansion exchange
T74 | turn:MOD | ASR_GAP | R145,R321 | lines 450-460; Moderator: introduces Q9 (Charles Malu); audio check
T75 | turn:ANALYST |  | R247,R259 | lines 461-461; Analyst Q9: utilization
T76 | turn:MGMT |  | R102,R103,R212 | lines 462-463; Management: reply
T77 | turn:ANALYST |  | - | lines 464-464; Analyst Q9: data centers
T78 | turn:MGMT |  | R104,R105,R154,R213,R214,R298 | lines 465-472; Management: reply
T79 | turn:ANALYST |  | - | lines 473-473; Analyst Q9: realization
T80 | turn:MGMT |  | R106,R107,R108,R300 | lines 474-477; Management: reply
T81 | turn:ANALYST |  | - | lines 478-478; Analyst Q9: closing
T82 | turn:MOD |  | R146 | lines 479-480; Moderator: introduces Q10 (Harin and Darasi)
T83 | turn:ANALYST |  | R109,R155 | lines 481-490; Analyst Q10: bushings, China dependency
T84 | turn:MGMT |  | R110,R111,R112,R301 | lines 491-497; Management: reply
T85 | turn:MIXED |  | R113,R114,R156,R222,R223,R302 | lines 498-506; Analyst/Management: bushing exchange
T86 | turn:ANALYST |  | R152 | lines 507-514; Analyst Q10: inventory, PGCIL
T87 | turn:MGMT |  | R153,R215,R216,R217,R305 | lines 515-521; Management: reply
T88 | turn:ANALYST |  | - | lines 522-522; Analyst Q10: PGCIL priority
T89 | turn:MGMT |  | R115,R116,R150,R218,R219,R220,R303,R304,R322 | lines 523-530; Management: reply
T90 | turn:ANALYST |  | - | lines 531-534; Analyst Q10: short circuit calculation approvals
T91 | turn:MGMT |  | R158 | lines 535-540; Management: reply
T92 | turn:ANALYST |  | R117,R157,R248,R249 | lines 541-545; Analyst Q10: LME and margin pressure
T93 | turn:MGMT |  | R118,R250 | lines 546-549; Management: reply
T94 | turn:ANALYST |  | - | lines 550-553; Analyst Q10: margin pressure follow-up
T95 | turn:MGMT |  | R119,R221 | lines 554-554; Management: reply
T96 | turn:ANALYST |  | - | lines 555-556; Analyst Q10: closing
T97 | turn:MOD |  | R162 | lines 557-558; Moderator: last question announced
T98 | turn:HOST |  | R163,R164,R306,R307 | lines 559-562; Host (Kiran Advisors): closing comments
T99 | turn:MOD |  | - | lines 563-567; Moderator: close
preamble rows (lines<31): R001,R002,R125,R126,R127,R128,R226,R227,R228,R229,R251,R252,R253,R254

## 3. QUESTIONS
TURN | analyst | topic | flags
T06 | Analyst Q1 | questions on H2 orders, year-end order book | 
T08 | Analyst Q1 | follow-up on revenue guidance | REPEAT_QUESTION revenue guidance
T10 | Analyst Q1 | margin question | REPEAT_QUESTION margin
T12 | Analyst Q1 | follow-up on 9 to 12% | REPEAT_QUESTION margin 9-12%
T14 | Analyst Q1 | closing | 
T16 | Analyst Q2 | procurement, execution risk | 
T18 | Analyst Q2 | Tamil Nadu capacity | 
T20 | Analyst Q2 | final unit timing | 
T22 | Analyst Q2 | power vs distribution margin | 
T25 | Analyst Q2 | follow-up on order mix | REPEAT_QUESTION order mix
T27 | Analyst Q2 | pipeline mix | REPEAT_QUESTION pipeline mix
T29 | Analyst Q2 | closing | 
T31 | Analyst Q3 | execution timeline question | REPEAT_QUESTION execution H2
T35 | Analyst Q4 | peak revenue verification | REPEAT_QUESTION revenue
T37 | Analyst Q4 | customer requirement vs guidance | REPEAT_QUESTION revenue guidance
T39 | Analyst Q4 | operating leverage | REPEAT_QUESTION margin/operating leverage
T41 | Analyst Q4 | working capital | 
T43 | Analyst Q4 | cash flow | 
T45 | Analyst Q4 | demand outlook | 
T47 | Analyst Q4 | capacity expansion | 
T52 | Analyst Q6 | ramp-up, utilization | REPEAT_QUESTION utilization
T54 | Analyst Q6 | MVA delivered | 
T56 | Analyst Q6 | closing | 
T58 | Analyst Q7 | power vs distribution split | REPEAT_QUESTION order mix
T60 | Analyst Q7 | margin with power mix | REPEAT_QUESTION margin
T62 | Analyst Q7 | government vs private | 
T64 | Analyst Q7 | same for current year | 
T66 | Analyst Q7 | receivable cycle | 
T68 | Analyst Q7 | government strategy | 
T72 | Analyst Q8 | capacity, long-term plan | 
T75 | Analyst Q9 | utilization | REPEAT_QUESTION utilization
T77 | Analyst Q9 | data centers | 
T79 | Analyst Q9 | realization | 
T81 | Analyst Q9 | closing | 
T83 | Analyst Q10 | bushings, China dependency | 
T86 | Analyst Q10 | inventory, PGCIL | REPEAT_QUESTION PGCIL
T88 | Analyst Q10 | PGCIL priority | REPEAT_QUESTION PGCIL
T90 | Analyst Q10 | short circuit calculation approvals | 
T92 | Analyst Q10 | LME and margin pressure | REPEAT_QUESTION margin
T94 | Analyst Q10 | margin pressure follow-up | REPEAT_QUESTION margin
T96 | Analyst Q10 | closing | 
T19 | MIXED exchange | Management/Analyst: clarification exchange | questions inside mixed turn
T33 | MIXED exchange | Analyst/Management: H2 execution exchange | questions inside mixed turn
T70 | MIXED exchange | Analyst/Management: closing exchange | questions inside mixed turn
T73 | MIXED exchange | Management/Analyst: expansion exchange | questions inside mixed turn
T85 | MIXED exchange | Analyst/Management: bushing exchange | questions inside mixed turn
T49/T50 | Analyst Q5 | audio failure, no question captured | ASR_GAP (R319,R320)

## 4. MANAGEMENT NUMBERS
ROW ID | category | flags | turn | note
R003 | mgmt_number |  | T03 | total income, H1 FY27
R004 | mgmt_number |  | T03 | total income YoY growth, H1 FY27
R005 | mgmt_number |  | T03 | EBITDA, H1 FY27
R006 | mgmt_number |  | T03 | EBITDA YoY growth, H1 FY27
R007 | mgmt_number |  | T03 | EBITDA margin, H1 FY27
R008 | mgmt_number |  | T03 | PAT YoY growth, H1 FY27
R009 | mgmt_number |  | T03 | profit after tax, H1 FY27
R010 | mgmt_number | ASR_RAW | T03 | margin as transcribed, H1 FY27
R011 | mgmt_number | ASR_RAW | T03 | EPS as transcribed, unit anomaly
R012 | mgmt_number |  | T03 | years of transformer experience
R013 | mgmt_number |  | T03 | orders secured, H1 FY27
R014 | mgmt_number |  | T03 | value of 11 orders, H1 FY27
R015 | mgmt_number |  | T03 | order execution timeline, lower bound
R016 | mgmt_number |  | T03 | order execution timeline, upper bound
R017 | mgmt_number | RESTATED(order book 565: R017,R027,R041,R079) | T03 | current order book
R018 | mgmt_number | ASR_RAW | T03 | order book under price variation clause
R019 | mgmt_number | ASR_RAW | T07 | year-end order book expected
R022 | mgmt_number |  | T09 | FY27 revenue expected
R023 | mgmt_number | RESTATED(H1 revenue 135/134: R003,R023,R056,R066,R106) | T09 | H1 revenue done, as spoken
R024 | mgmt_number | ASR_RAW | T09 | balance revenue to achieve
R026 | mgmt_number |  | T11 | order book covered with PVC
R027 | mgmt_number | RESTATED(order book 565: R017,R027,R041,R079) | T11 | order book
R028 | mgmt_number | ASR_RAW | T11 | order book expected to execute this year
R029 | mgmt_number | RESTATED(margin 9-12%: R029,R030,R119) | T11 | margin maintainable, as spoken "pack margin"
R030 | mgmt_number | RESTATED(margin 9-12%: R029,R030,R119) | T13 | margin guideline range
R032 | mgmt_number |  | T17 | order book covered by PVC
R035 | mgmt_number | ASR_RAW | T19 | unit one peak revenue
R036 | mgmt_number | ASR_RAW | T19 | new plant revenue expected
R037 | mgmt_number | ASR_RAW | T19 | both plants combined peak revenue
R038 | mgmt_number |  | T23 | power transformer margin uplift absorbed
R039 | mgmt_number |  | T26 | distribution share of order book
R040 | mgmt_number |  | T26 | distribution share of order book
R041 | mgmt_number | RESTATED(order book 565: R017,R027,R041,R079) | T26 | order book base for mix
R042 | mgmt_number | ASR_RAW | T26 | order book as spoken before correction
R043 | mgmt_number |  | T26 | distribution order book, crores
R044 | mgmt_number |  | T26 | distribution order book
R045 | mgmt_number |  | T26 | power transformer order book
R046 | mgmt_number |  | T26 | power transformer share of order book
R047 | mgmt_number | ASR_RAW | T26 | power transformer share of order book
R048 | mgmt_number |  | T26 | inverter duty transformer order book
R049 | mgmt_number |  | T26 | inverter duty share of order book
R051 | mgmt_number | ASR_RAW | T32 | order book execution before March 2027
R052 | mgmt_number | ASR_RAW | T32 | order book execution after March 2027
R053 | mgmt_number |  | T33 | H2 execution guideline
R055 | mgmt_number |  | T33 | H2 execution aim
R056 | mgmt_number | RESTATED(H1 revenue 135/134: R003,R023,R056,R066,R106) | T33 | H1 revenue done, as spoken
R058 | mgmt_number |  | T36 | time to reach 600 crores
R059 | mgmt_number |  | T36 | peak revenue reach
R060 | mgmt_number |  | T36 | next year revenue
R064 | mgmt_number | ASR_RAW | T38 | customer requirement this year
R065 | mgmt_number | ASR_RAW | T38 | further execution
R066 | mgmt_number | RESTATED(H1 revenue 135/134: R003,R023,R056,R066,R106) | T38 | H1 revenue, as spoken
R068 | mgmt_number |  | T42 | FY27 top line expected
R069 | mgmt_number |  | T42 | inventory holding needed
R070 | mgmt_number | ASR_RAW | T42 | inventory to be maintained
R071 | mgmt_number |  | T46 | power sector demand horizon
R072 | mgmt_number | ASR_RAW | T53 | new facility utilization this year
R073 | mgmt_number |  | T53 | new facility utilization next year
R074 | mgmt_number |  | T59 | H1 revenue share power transformers
R076 | mgmt_number | ASR_RAW | T61 | margin increase absorbed by overheads
R079 | mgmt_number | RESTATED(order book 565: R017,R027,R041,R079) | T63 | order book base for govt share
R080 | mgmt_number | ASR_RAW | T63 | government share of order book
R081 | mgmt_number |  | T63 | non-government share of order book
R082 | mgmt_number |  | T70 | government share to maintain
R083 | mgmt_number | ASR_RAW | T70 | government share to maintain
R084 | mgmt_number |  | T67 | advance from private customers
R085 | mgmt_number |  | T67 | payment before dispatch
R086 | mgmt_number |  | T67 | payment after commissioning
R087 | mgmt_number |  | T67 | credit to repeat private customers
R088 | mgmt_number |  | T67 | government payment cycle
R089 | mgmt_number | ASR_RAW | T69 | tender, as transcribed
R090 | mgmt_number |  | T69 | Tanger Co order
R091 | mgmt_number | ASR_RAW | T69 | posted tender
R097 | mgmt_number | ASR_RAW | T73 | spent on capacity at Kanpur (raw)
R100 | mgmt_number |  | T73 | mgmt reply on growth horizon
R101 | mgmt_number |  | T73 | mgmt reply on expansion horizon
R102 | mgmt_number |  | T76 | current utilization as of H1
R103 | mgmt_number |  | T76 | utilization expected this year
R104 | mgmt_number | ASR_RAW | T78 | data centre transformer size
R105 | mgmt_number | ZERO_STANDING | T78 | data centre orders to date
R106 | mgmt_number | RESTATED(H1 revenue 135/134: R003,R023,R056,R066,R106) | T80 | H1 revenue, as spoken
R107 | mgmt_number |  | T80 | distribution transformer realization
R108 | mgmt_number |  | T80 | power transformer realization
R110 | mgmt_number | ASR_RAW | T84 | bushing demand voltage class
R111 | mgmt_number |  | T84 | bushing supply voltage class
R112 | mgmt_number |  | T84 | order book voltage class
R113 | mgmt_number | ASR_RAW | T85 | orders with bushings booked
R114 | mgmt_number |  | T85 | orders at higher voltage
R115 | mgmt_number | ASR_RAW | T89 | type test certificates
R116 | mgmt_number | ASR_RAW | T89 | type test for Tanjiko
R118 | mgmt_number |  | T93 | PVC calculation lag
R119 | mgmt_number | RESTATED(margin 9-12%: R029,R030,R119) | T95 | margin maintained
R120 | mgmt_number |  | T17 | in business

Analyst-stated NUMBER rows (not management): R020, R021, R025, R031, R033, R034, R050, R054, R057, R061, R062, R063, R067, R075, R077, R078, R092, R093, R094, R095, R096, R098, R099, R109, R117
Non-management NUMBER rows: R001,R002 (ASR meta), R121 (moderator question limit)

## 5. FORWARD COMMITMENTS
ROW ID | category | flags | turn | note
R165 | forward |  | T03 | order book
R166 | forward |  | T03 | growth
R167 | forward |  | T03 | H2 FY27
R168 | forward |  | T03 | priority 1
R169 | forward |  | T03 | priority 2
R170 | forward |  | T03 | priority 3
R171 | forward |  | T03 | priority 4
R172 | forward |  | T03 | priority 5
R173 | forward |  | T03 | demand
R174 | forward |  | T03 | outlook
R175 | forward |  | T07 | order book
R176 | forward |  | T09 | revenue guidance
R177 | forward |  | T09 | H2 revenue
R178 | forward |  | T11 | margin guidance
R179 | forward |  | T11 | margin
R180 | forward |  | T13 | margin
R181 | forward |  | T11 | execution
R182 | forward |  | T17 | input cost
R183 | forward |  | T21 | capacity
R184 | forward |  | T19 | capacity
R185 | forward |  | T19 | capacity
R186 | forward |  | T23 | power margin
R187 | forward |  | T33 | H2
R188 | forward |  | T33 | H2
R189 | forward |  | T32 | execution
R190 | forward |  | T36 | revenue
R191 | forward |  | T36 | revenue
R192 | forward |  | T38 | guidance
R193 | forward |  | T38 | execution
R194 | forward |  | T40 | margin
R195 | forward |  | T42 | working capital
R196 | forward |  | T44 | cash flow
R197 | forward |  | T46 | demand
R198 | forward |  | T47 | demand
R199 | forward |  | T48 | capex
R200 | forward |  | T53 | utilization
R201 | forward |  | T53 | utilization
R202 | forward |  | T65 | mix
R203 | forward |  | T69 | strategy
R204 | forward |  | T69 | strategy
R205 | forward |  | T70 | mix
R206 | forward | ANALYST_VOICE | T72 | utilization
R207 | forward |  | T73 | capex
R208 | forward |  | T73 | capex
R209 | forward |  | T73 | capex
R210 | forward |  | T73 | growth
R211 | forward |  | T73 | cash flow
R212 | forward |  | T76 | utilization
R213 | forward |  | T78 | data centers
R214 | forward |  | T78 | data centers
R215 | forward |  | T87 | approval
R216 | forward |  | T87 | approval
R217 | forward |  | T87 | approval
R218 | forward |  | T89 | approval
R219 | forward |  | T89 | approval
R220 | forward |  | T89 | approval
R221 | forward |  | T95 | margin
R222 | forward |  | T85 | supply
R223 | forward |  | T85 | supply
R224 | forward |  | T28 | pipeline
R225 | forward |  | T55 | disclosure

## 6. HEDGES / QUALIFIERS
ROW ID | category | flags | turn | note
R251 | qualifier |  | preamble | source status
R252 | qualifier |  | preamble | source caveat
R253 | qualifier |  | preamble | source caveat
R254 | qualifier |  | preamble | source caveat
R255 | qualifier | ASR_QUALITY | T01 | likely FY27 period label
R256 | qualifier | ASR_QUALITY | T03 | period label
R257 | qualifier | ASR_QUALITY | T03 | period label
R258 | qualifier | ASR_QUALITY | T03 | period label
R259 | qualifier | ASR_QUALITY | T75 | period label
R260 | qualifier | ASR_QUALITY | T35 | period label
R261 | qualifier | ASR_QUALITY | T10 | period label
R262 | qualifier | ASR_QUALITY | T06 | period label
R263 | qualifier | ASR_QUALITY | T03 | metric label
R264 | qualifier | ASR_QUALITY | T03 | EPS with percent sign
R265 | qualifier | ASR_QUALITY | T03 | geography name
R266 | qualifier | ASR_QUALITY | T03 | phrase
R267 | qualifier | ASR_QUALITY | T03 | PVC coverage
R268 | qualifier |  | T03 | term as transcribed
R269 | qualifier | ASR_QUALITY | T03 | inputs
R270 | qualifier | ASR_QUALITY | T03 | facility name
R271 | qualifier | ASR_QUALITY | T03 | facility name
R272 | qualifier | ASR_QUALITY | T03 | priority 1
R273 | qualifier |  | T06 | analyst Q1
R274 | qualifier | ASR_QUALITY | T08 | prior guidance
R275 | qualifier | ASR_QUALITY | T08 | analyst range
R276 | qualifier | ASR_QUALITY | T09 | unit/basis unclear
R277 | qualifier | ASR_QUALITY | T09 | balance revenue
R278 | qualifier | ASR_QUALITY | T18 | plant name
R279 | qualifier | ASR_QUALITY | T19 | unit
R280 | qualifier | ASR_QUALITY | T19 | unit
R281 | qualifier | ASR_QUALITY | T19 | unit
R282 | qualifier | ASR_QUALITY | T26 | order book
R283 | qualifier | ASR_QUALITY | T26 | share
R284 | qualifier | ASR_QUALITY | T26 | product
R285 | qualifier | ASR_QUALITY | T35 | analyst
R286 | qualifier | ASR_QUALITY | T38 | customer requirement
R287 | qualifier | ASR_QUALITY | T38 | execution
R288 | qualifier |  | T59 | product
R289 | qualifier | ASR_QUALITY | T60 | analyst
R290 | qualifier | ASR_QUALITY | T61 | margin uplift
R291 | qualifier | ASR_QUALITY | T62 | unit
R292 | qualifier | ASR_QUALITY | T63 | share
R293 | qualifier | ASR_QUALITY | T69 | tender
R294 | qualifier | ASR_QUALITY | T69 | tender
R295 | qualifier | ASR_QUALITY | T69 | customer
R296 | qualifier | ASR_QUALITY | T72 | analyst
R297 | qualifier | ASR_QUALITY | T73 | capex unit
R298 | qualifier | ASR_QUALITY | T78 | MVA size
R299 | qualifier | ASR_QUALITY | T53 | utilization
R300 | qualifier |  | T80 | realization
R301 | qualifier |  | T84 | voltage class
R302 | qualifier | ASR_QUALITY | T85 | voltage class
R303 | qualifier | ASR_QUALITY | T89 | type test
R304 | qualifier | ASR_QUALITY | T89 | customer
R305 | qualifier |  | T87 | body
R306 | qualifier | ASR_QUALITY | T98 | contact
R307 | qualifier | ASR_QUALITY | T98 | address
R308 | qualifier |  | T32 | execution basis
R309 | qualifier |  | T38 | guidance basis
R310 | qualifier |  | T13 | margin
R311 | qualifier |  | T13 | margin
R312 | qualifier |  | T03 | margin
R313 | qualifier |  | T03 | PVC
R314 | qualifier |  | T17 | PVC
R315 | qualifier | NOT_DISCLOSED | T55 | NOT DISCLOSED
R316 | qualifier |  | T28 | pipeline
R317 | qualifier |  | T65 | mix
R318 | qualifier | ASR_GAP | T40 | ASR gap
R319 | qualifier |  | T49 | lines 300-312
R320 | qualifier | ASR_GAP | T49 | audio
R321 | qualifier | ASR_GAP | T74 | audio
R322 | qualifier | ASR_QUALITY | T89 | ASR
R323 | qualifier | ASR_QUALITY | T23 | ASR

## 7. ENTITIES
ROW ID | category | flags | note
R122 | entity |  | conference host, IR firm
R123 | entity | ASR_RAW | host speaker
R124 | entity |  | Chairman and Managing Director
R125 | entity |  | company
R126 | entity |  | listing venue
R127 | entity |  | NSE filing reference
R128 | entity |  | ASR engine
R129 | entity |  | traditional market
R130 | entity | ASR_RAW | new geography
R131 | entity | ASR_RAW | ramp-up facility
R132 | entity | ASR_RAW | facility utilization
R133 | entity | ASR_RAW | input material
R134 | entity | ASR_RAW | input material
R135 | entity |  | input material
R136 | entity | ASR_RAW | analyst Q1
R137 | entity |  | self-named speaker, Q1
R138 | entity |  | analyst Q2
R139 | entity |  | analyst Q3
R140 | entity |  | analyst Q4
R141 | entity |  | analyst Q5
R142 | entity |  | analyst Q6
R143 | entity |  | analyst Q7
R144 | entity |  | analyst Q8
R145 | entity |  | analyst Q9
R146 | entity |  | analyst Q10
R147 | entity |  | plant location
R148 | entity | ASR_RAW | plant name
R149 | entity | ASR_RAW | government customer
R150 | entity | ASR_RAW | government customer
R151 | entity | ASR_RAW | capacity location
R152 | entity |  | approval body
R153 | entity |  | approval body, raw
R154 | entity |  | prospective customer segment
R155 | entity |  | key component
R156 | entity |  | bushing source country
R157 | entity |  | metal price benchmark
R158 | entity |  | tender term
R159 | entity |  | demand drivers
R160 | entity |  | product
R161 | entity | ASR_RAW | product
R162 | entity | ASR_RAW | closing host
R163 | entity | ASR_RAW | IR contact
R164 | entity | ASR_RAW | host closing address

## 8. DATES
ROW ID | category | flags | note
R226 | date |  | call date and time
R227 | date |  | audio link filing date
R228 | date |  | transcription date
R229 | date |  | call period, preamble
R230 | date | ASR_RAW | period, opening
R231 | date | ASR_RAW | period, CMD opening
R232 | date | ASR_RAW | period, performance
R233 | date | ASR_RAW | period, orders
R234 | date |  | period
R235 | date |  | priorities period
R236 | date | ASR_RAW | analyst question period
R237 | date | ASR_RAW | analyst question period
R238 | date | ASR_RAW | analyst period
R239 | date |  | orders with PVC began
R240 | date |  | prior guidance reference
R241 | date |  | execution cut-off
R242 | date | ASR_RAW | guideline period
R243 | date | ASR_RAW | analyst reference year
R244 | date |  | utilization target date
R245 | date |  | analyst utilization year
R246 | date |  | long-term horizon
R247 | date | ASR_RAW | utilization as-of date
R248 | date |  | quote LME month
R249 | date |  | quote month
R250 | date |  | PVC reference month

## 9. ZERO_STANDING
R105 | zero data-centre orders to date | ZERO_STANDING | turn T78

## MISSING_FROM_STRUCTURED
none
## CORRECTION LOOP 1 ADDITIONS (A1 rows R324-R326)
ROW ID | category | flags | turn | note
R324 | mgmt_number | ASR_RAW | T38 (l.287) | order lead time one year before; mgmt's only stated reason for 353 Cr customer requirement vs 200-250 Cr H2 guide gap (cf R189, R187, R188, R308)
R325 | mgmt_number | ASR_RAW | T38 (l.287) | order lead time eight/nine months before; same reason (cf R324)
R326 | forward | RESTATED(repeat of R186 margin-sustain, l.224/252 area) | T61 (l.383) | power-mix margin to sustain; second instance

## CORRECTION LOOP 2 ADDITIONS (A1 FORWARD rows R327-R344)
ROW ID | category | flags | turn | note
R327 | forward | RESTATED(R182,R178,R221 PVC cover of price rise) | T17 (l.206-207) | price escalation covered by PVC; margin not much affected (A5 M7)
R328 | forward | | T17 (l.208-210) | procurement not difficult; long vendor relationships
R329 | forward | RESTATED(R173,R197) | T07 (l.137-138) | demand very high; union and state governments expanding transmission
R330 | forward | RESTATED(R165) | T07 (l.142-143) | pipeline huge; selective on quality and terms
R331 | forward | RESTATED(R178,R179,R180) | T11 (l.165-167) | margin expectation tied to ~80% PVC cover
R332 | forward | RESTATED(R313,R331) | T11 (l.170-171) | major portion of order book PVC covered
R333 | forward | RESTATED(R239) | T13 (l.180-181) | PVC orders taken since January; no price rise expected
R334 | forward | RESTATED(R186,R038) | T23 (l.248-250) | power margin uplift absorbed by overheads
R335 | forward | RESTATED(R194) | T40 (l.298-299) | order selection on margin
R336 | forward | RESTATED(R195) | T42 (l.308-309) | inventory held; revenue to rise
R337 | forward | RESTATED(R334,R326,R076) | T61 (l.380-382) | power-mix margin absorbed by overheads
R338 | forward | RESTATED(R203,R204) | T69 (l.407-408) | government business for credentials
R339 | forward | RESTATED(R213) | T78 (l.466-467) | data centre demand large; 160-200 MVA class
R340 | forward | RESTATED(R112,R301) | T84 (l.493-494) | bushing issue only above 230 kV (raw); order book mostly 110 kV and below
R341 | forward | RESTATED(R222) | T84 (l.497) | no problem getting bushings
R342 | forward | RESTATED(R215-R219) | T89 (l.523-524) | PGCIL approval path; documentation and type tests needed
R343 | forward | RESTATED(R158) | T91 (l.538-540) | govt tenders on BQR; type test mandatory
R344 | forward | RESTATED(R221) | T93 (l.548-549) | PVC calculation takes care of price
