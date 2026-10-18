# A2 LEDGER: Cyient DLM (CYIENTDLM) concall Q2 FY27
Source: A1 structured extraction only (fulltext used for count test). Machine transcript; speaker tags INFERRED by A1.

ids_in_structured: 303 | ids_referenced_in_ledger: 303 | orphan_ids: [] | missing_from_structured: 1 (M001) | match: yes

=== A2 COUNT TEST ===
category: participants   grep_count: 14  sweep_count: 14  match: yes   (3 management R162-R164, moderator R165, 10 analyst slots; 'Our first/next/last question' cue lines in fulltext = 10)
category: turns          grep_count: 97  sweep_count: 97  match: yes   (A1 T001-T097 contiguous; independent fulltext sweep of moderator cue lines gives 17 moderator turns = 17 MODERATOR turns in A1 table; non-moderator turns are speaker-change inferences, not independently countable in an unlabelled transcript)
category: question_slots grep_count: 10  sweep_count: 10  match: yes   (fulltext cue lines 191,219,241,268,271,322,364,370,421,448; 8 analysts asked; Meeth Jain no response lines 268-270; Suman Kumar dropped lines 364-369)
category: question_turns grep_count: 26  sweep_count: 26  match: yes   (analyst turns tagged QUESTION in A1 turn table)
category: mgmt_numbers   grep_count: 160  sweep_count: 160  match: yes
category: entities       grep_count: 37  sweep_count: 37  match: yes
category: forward        grep_count: 53  sweep_count: 53  match: yes
category: dates          grep_count: 22  sweep_count: 22  match: yes
category: qualifiers     grep_count: 31  sweep_count: 31  match: yes
category: total_ids      grep_count: 303  sweep_count: 303  match: yes
gate_a2: pass
=== END COUNT TEST ===

## 1. PARTICIPANTS (MGMT_ABSENCE: none; Chairman, CEO and CFO all present)
ROW_ID | category | flags | note
R162 | participant | - | line 27; speaker
R163 | participant | - | line 29; speaker
R164 | participant | - | line 29; speaker
R165 | participant | - | line 28; moderator addressed by chairman
R181 | participant | - | line 191; analyst Q1
R182 | participant | - | line 219; analyst Q2
R183 | participant | - | line 241; analyst Q3
R184 | participant | NO_RESPONSE | line 268; analyst Q4, no response
R185 | participant | - | line 271; analyst Q5
R187 | participant | - | line 322; analyst Q6
R188 | participant | NO_RESPONSE | line 364; analyst Q7, dropped from queue
R189 | participant | - | line 370; analyst Q8
R190 | participant | - | line 399; large customer with signed order, per analyst
R194 | participant | - | line 413; product signed with Honeywell (analyst)
R195 | participant | - | line 421; analyst Q9
R197 | participant | - | line 448; analyst Q10

## 2. SPEAKER TURNS (sequential; speaker per A1, INFERRED)
TURN | speaker (A1) | fulltext lines | flags
T001 | MODERATOR | 24-27 | -
T002 | CHAIRMAN Krishna Bodanapu | 28-58 | -
T003 | CEO Rajendra Velagapudi | 59-123 | -
T004 | CFO R.M. Subramanian | 124-184 | -
T005 | MODERATOR | 185-191 | -
T006 | ANALYST-Q1 Bala Subramanian (Arihant Capital) | 192-196 | -
T007 | CFO R.M. Subramanian | 197-209 | -
T008 | ANALYST-Q1 Bala Subramanian (follow-up) | 210-211 | -
T009 | MANAGEMENT (CEO inferred) | 212-217 | SPEAKER_INFERRED
T010 | ANALYST-Q1 Bala Subramanian | 218-218 | -
T011 | MODERATOR | 219-219 | -
T012 | ANALYST-Q2 Santosh Seshadri (Avendus Park) | 220-224 | -
T013 | MANAGEMENT (CFO inferred) | 225-228 | SPEAKER_INFERRED
T014 | ANALYST-Q2 Santosh Seshadri | 229-229 | -
T015 | MANAGEMENT (CEO inferred) | 230-231 | SPEAKER_INFERRED
T016 | ANALYST-Q2 Santosh Seshadri | 232-235 | -
T017 | MANAGEMENT (CEO inferred) | 236-239 | SPEAKER_INFERRED
T018 | ANALYST-Q2 Santosh Seshadri | 240-240 | -
T019 | MODERATOR | 241-242 | -
T020 | ANALYST-Q3 Shashank Jha (SP Capital) | 243-243 | -
T021 | MANAGEMENT (inferred) | 244-244 | SPEAKER_INFERRED
T022 | ANALYST-Q3 Shashank Jha | 245-247 | -
T023 | MANAGEMENT (CEO inferred) | 248-252 | SPEAKER_INFERRED
T024 | ANALYST-Q3 Shashank Jha | 253-253 | -
T025 | MANAGEMENT (CEO inferred) | 254-256 | SPEAKER_INFERRED
T026 | ANALYST-Q3 Shashank Jha | 257-258 | -
T027 | MANAGEMENT (inferred) | 259-259 | SPEAKER_INFERRED
T028 | ANALYST-Q3 Shashank Jha | 260-260 | -
T029 | MANAGEMENT (CEO inferred) | 261-264 | SPEAKER_INFERRED
T030 | ANALYST-Q3 Shashank Jha | 265-265 | -
T031 | MANAGEMENT (inferred) | 266-266 | SPEAKER_INFERRED
T032 | ANALYST-Q3 Shashank Jha | 267-267 | -
T033 | MODERATOR | 268-270 | -
T034 | MODERATOR | 271-271 | -
T035 | ANALYST-Q5 Umang Gadda (Avener) | 272-272 | -
T036 | MODERATOR | 273-273 | -
T037 | ANALYST-Q5 Umang Gadda (Avener) | 274-278 | -
T038 | MANAGEMENT (CEO inferred) | 279-281 | SPEAKER_INFERRED
T039 | MANAGEMENT (CHAIRMAN inferred) | 282-293 | SPEAKER_INFERRED
T040 | MANAGEMENT (CEO inferred) | 294-299 | SPEAKER_INFERRED
T041 | ANALYST-Q5 Umang Gadda | 300-304 | -
T042 | MANAGEMENT (CEO inferred) | 305-310 | SPEAKER_INFERRED
T043 | ANALYST-Q5 Umang Gadda | 311-312 | -
T044 | MANAGEMENT (inferred) | 313-313 | SPEAKER_INFERRED
T045 | ANALYST-Q5 Umang Gadda | 314-314 | -
T046 | MANAGEMENT (CEO inferred) | 315-317 | SPEAKER_INFERRED
T047 | ANALYST-Q5 Umang Gadda | 318-318 | -
T048 | MANAGEMENT/MODERATOR (unclear) | 319-319 | SPEAKER_INFERRED
T049 | MODERATOR | 320-322 | -
T050 | ANALYST-Q6 Nishita (Sapphire Capital) | 323-326 | -
T051 | MANAGEMENT (CEO inferred) | 327-333 | SPEAKER_INFERRED
T052 | ANALYST-Q6 Nishita (Sapphire Capital) | 334-335 | -
T053 | MANAGEMENT (CHAIRMAN inferred, low confidence) | 336-348 | SPEAKER_INFERRED
T054 | ANALYST-Q6 Nishita (Sapphire Capital) | 349-353 | -
T055 | MANAGEMENT (CEO inferred) | 354-361 | SPEAKER_INFERRED
T056 | ANALYST-Q6 Nishita (Sapphire Capital) | 362-362 | -
T057 | MODERATOR | 363-369 | -
T058 | MODERATOR | 370-371 | -
T059 | ANALYST-Q8 Aditya Pal (MSA Capital Partners) | 372-372 | -
T060 | MODERATOR | 373-373 | -
T061 | ANALYST-Q8 Aditya Pal (MSA Capital Partners) | 374-381 | -
T062 | MANAGEMENT (CFO inferred) | 382-394 | SPEAKER_INFERRED
T063 | ANALYST-Q8 Aditya Pal | 395-403 | -
T064 | MANAGEMENT (CEO inferred) | 404-411 | SPEAKER_INFERRED
T065 | ANALYST-Q8 Aditya Pal | 412-417 | -
T066 | MANAGEMENT (CEO inferred) | 418-420 | SPEAKER_INFERRED
T067 | MODERATOR | 421-421 | -
T068 | ANALYST-Q9 Karan Sanwal (Niveshye) | 422-422 | -
T069 | MODERATOR | 423-423 | -
T070 | ANALYST-Q9 Karan Sanwal (Niveshye) | 424-425 | -
T071 | MANAGEMENT (CEO inferred) | 426-429 | SPEAKER_INFERRED
T072 | ANALYST-Q9 Karan Sanwal | 430-430 | -
T073 | MANAGEMENT (CEO inferred) | 431-431 | SPEAKER_INFERRED
T074 | ANALYST-Q9 Karan Sanwal | 432-433 | -
T075 | MANAGEMENT (inferred) | 434-434 | SPEAKER_INFERRED
T076 | ANALYST-Q9 Karan Sanwal | 435-436 | -
T077 | MANAGEMENT (CEO inferred) | 437-439 | SPEAKER_INFERRED
T078 | ANALYST-Q9 Karan Sanwal | 440-441 | -
T079 | MANAGEMENT (inferred) | 442-442 | SPEAKER_INFERRED
T080 | ANALYST-Q9 Karan Sanwal | 443-443 | -
T081 | MANAGEMENT (CEO inferred) | 444-445 | SPEAKER_INFERRED
T082 | ANALYST-Q9 Karan Sanwal | 446-446 | -
T083 | MANAGEMENT/MODERATOR (unclear) | 447-447 | SPEAKER_INFERRED
T084 | MODERATOR | 448-448 | -
T085 | ANALYST-Q10 Gaurav Shukla (PitVestor) | 449-449 | -
T086 | MODERATOR | 450-450 | -
T087 | ANALYST-Q10 Gaurav Shukla (PitVestor) | 451-451 | -
T088 | MANAGEMENT (CFO inferred) | 452-455 | SPEAKER_INFERRED
T089 | ANALYST-Q10 Gaurav Shukla | 456-457 | -
T090 | MANAGEMENT (CEO inferred) | 458-461 | SPEAKER_INFERRED
T091 | ANALYST-Q10 Gaurav Shukla | 462-463 | -
T092 | MANAGEMENT (CFO inferred) | 464-465 | SPEAKER_INFERRED
T093 | ANALYST-Q10 Gaurav Shukla | 466-466 | -
T094 | MANAGEMENT/MODERATOR (unclear) | 467-469 | SPEAKER_INFERRED
T095 | MODERATOR | 470-470 | -
T096 | CHAIRMAN Krishna Bodanapu | 471-485 | -
T097 | MODERATOR | 486-488 | -

Q&A share by turn number: prepared remarks T002-T004; Q&A T005-T097 (93 of 97 turns, 95.9%); chairman close T096.

## 3. QUESTIONS (by analyst slot)
SLOT | analyst, firm | question turns | topics | flags
Q1 | Bala Subramanian, Arihant Capital | T006,T008 | T006 margin, product development spend; T008  | -
Q2 | Santosh Seshadri, Avendus Park | T012,T014,T016 | T012 margin quantification, revenue mix, recurrence; T014 on FY27 margin guidance; T016 order book timeline, semiconductor programs | -
Q3 | Shashank Jha, SP Capital | T020,T022,T024,T026,T030 | T020 FY27 margin; T022 order book vs revenue pace; T024 bid pipeline conversion; T026 win from 1 billion bid pipeline; T030 FY28 margin | -
Q4 | Meeth Jain, Systematics | none | no question asked | NO_RESPONSE (no reply, moderator T033)
Q5 | Umang Gadda, Avener | T037,T041 | T037 margin squeeze, product development, mix; T041 $1 billion order book interview | -
Q6 | Nishita, Sapphire Capital | T050,T052,T054 | T050 pipeline timeline, B2S in pipeline; T052 timing of 400 to 500 million; T054 Q1 vs Q2 growth, FY27 30-35% | -
Q7 | Suman Kumar, Modila Loswal | none | no question asked | NO_RESPONSE (dropped from queue, moderator T057)
Q8 | Aditya Pal, MSA Capital Partners | T061,T063,T065 | T061 B2S contribution, margin vs investment; T063 EBITOL customer, Honeywell/Indigo; T065 Honeywell micro VCS, liquid loops | -
Q9 | Karan Sanwal, Niveshye | T070,T072,T074,T076,T078 | T070 B2S projects and clients; T072 years covered by billion dollar; T074 export market, US defence; T076 Altec division; T078 revenue mix geography | -
Q10 | Gaurav Shukla, PitVestor | T087,T089,T091 | T087 order book executed FY27 vs FY28; T089 AI/data center, semicap, robotics engagement; T091 other income 23 crore | -

REPEAT_QUESTION: margin / product development spend asked by Q1 (T006), Q2 (T012), Q3 (T020, T030), Q5 (T037), Q8 (T061). Answers held in R285, R286, R295-R298.
REPEAT_QUESTION: $1 billion order book / pipeline conversion asked by Q2 (T016), Q3 (T022-T026), Q5 (T041), Q6 (T050-T052), Q9 (T072), Q10 (T087). Rows R002, R287-R292.
REPEAT_QUESTION: B2S / build-to-specification asked by Q6 (T050), Q8 (T061), Q9 (T070).
REPEAT_QUESTION: FY27 margin guidance asked by Q2 (T014) and Q3 (T020); FY28 margin T030.

## 4. MANAGEMENT NUMBERS (NUMBER rows; units as spoken)
ROW_ID | category | turn | flags | note
R001 | number | T002 | - | line 33, page 1; order backlog
R002 | number | T002 | - | line 33, page 1; sales pipeline
R003 | number | T002 | - | line 35, page 1; sustained positive order book momentum
R004 | number | T002 | - | line 36, page 1; Q2 book-to-bill ratio
R005 | number | T002 | - | line 40, page 1; Q2 revenue growth YoY
R006 | number | T002 | - | line 54, page 1; H1 FY27 revenue growth
R007 | number | T003 | - | line 62, page 1; global EMS market today
R008 | number | T003 | - | line 62, page 1; global EMS market over next few years
R009 | number | T003 | - | line 63, page 1; high-reliability EMS opportunity
R010 | number | T003 | - | line 69, page 1; addressable EMS opportunity AI and data center
R011 | number | T003 | - | line 78, page 1; margin framework, Strengthen phase
R012 | number | T003 | - | line 83, page 2; portfolio expansion count
R013 | number | T003 | - | line 86, page 2; margin framework, Expand phase
R014 | number | T003 | - | line 96, page 2; margin framework, Transform phase
R015 | number | T003 | - | line 106, page 2; Q2 book-to-bill, order book all-time high
R016 | number | T003 | - | line 108, page 2; Q2 revenue growth YoY
R017 | number | T003 | - | line 109, page 2; H1 revenue growth YoY
R018 | number | T003 | - | line 111, page 2; Box-build revenue growth YoY, Q2
R019 | number | T003 | - | line 113, page 2; new logos added in quarter
R020 | number | T004 | - | line 126, page 2; Q2 FY27 revenue
R021 | number | T004 | - | line 126, page 2; Q2 revenue growth YoY
R022 | number | T004 | - | line 127, page 2; order book, all-time high
R023 | number | T004 | - | line 127, page 2; sequential order book increase
R024 | number | T004 | - | line 129, page 2; Q2 FY27 EBITDA
R025 | number | T004 | - | line 129, page 2; Q2 EBITDA growth YoY
R026 | number | T004 | - | line 129, page 2; Q2 EBITDA margin
R027 | number | T004 | - | line 130, page 2; Q2 EBITDA margin decline YoY
R028 | number | T004 | - | line 131, page 2; normalized PAT growth YoY, Q2
R029 | number | T004 | - | line 131, page 2; normalized PAT, Q2
R030 | number | T004 | - | line 131, page 2; normalized PAT margin, Q2
R031 | number | T004 | - | line 132, page 2; reported PAT, Q2
R032 | number | T004 | - | line 133, page 2; one-time reversal of provisions, Q2
R033 | number | T004 | - | line 137, page 2; revenue Q2 FY27
R034 | number | T004 | - | line 137, page 2; revenue Q2 FY26
R035 | number | T004 | - | line 137, page 2; revenue growth YoY Q2
R036 | number | T004 | - | line 138, page 2; EBITDA Q2
R037 | number | T004 | - | line 138, page 2; EBITDA margin Q2
R038 | number | T004 | - | line 141, page 2; normalized PAT Q2
R039 | number | T004 | - | line 141, page 2; normalized PAT growth YoY Q2
R040 | number | T004 | - | line 142, page 2; reported PAT Q2
R041 | number | T004 | - | line 142, page 2; one-time benefit in reported PAT Q2
R042 | number | T004 | - | line 143, page 2; normalized PAT Q2 excluding one-off
R043 | number | T004 | - | line 148, page 3; order book end Q2 FY27
R044 | number | T004 | - | line 148, page 3; order book end Q1 FY27
R045 | number | T004 | - | line 148, page 3; net working capital days Q2
R046 | number | T004 | - | line 148, page 3; net working capital days Q1
R047 | number | T004 | - | line 148, page 3; inventory days, stable
R048 | number | T004 | - | line 148, page 3; DSO Q1
R049 | number | T004 | - | line 148, page 3; DSO Q2
R050 | number | T004 | - | line 149, page 3; customer advances Q2
R051 | number | T004 | - | line 149, page 3; customer advances Q1
R052 | number | T004 | - | line 149, page 3; operating free cash flow Q2
R053 | number | T004 | - | line 151, page 3; aerospace share of Q2 revenue
R054 | number | T004 | - | line 151, page 3; industrial share of Q2 revenue
R055 | number | T004 | - | line 151, page 3; aerospace YoY growth
R056 | number | T004 | - | line 151, page 3; industrial YoY growth
R057 | number | T004 | - | line 152, page 3; defence share of revenue
R058 | number | T004 | - | line 152, page 3; defence YoY growth
R059 | number | T004 | - | line 152, page 3; Mettech share of revenue
R060 | number | T004 | - | line 152, page 3; Mettech YoY growth
R061 | number | T004 | - | line 153, page 3; PCBA share of revenue
R062 | number | T004 | - | line 153, page 3; PCBA YoY growth
R063 | number | T004 | - | line 153, page 3; BoxBill share of revenue
R064 | number | T004 | - | line 153, page 3; BoxBill YoY growth
R065 | number | T004 | - | line 154, page 3; rest of world share of revenue
R066 | number | T004 | - | line 154, page 3; India share of revenue
R067 | number | T004 | - | line 156, page 3; revenue growth YoY Q2
R068 | number | T004 | - | line 156, page 3; revenue Q2
R069 | number | T004 | - | line 157, page 3; EBITDA Q2
R070 | number | T004 | - | line 157, page 3; EBITDA growth YoY Q2
R071 | number | T004 | - | line 157, page 3; EBITDA margin Q2
R072 | number | T004 | - | line 157, page 3; EBITDA margin Q2 FY26
R073 | number | T004 | - | line 160, page 3; finance cost decline YoY Q2
R074 | number | T004 | - | line 160, page 3; finance costs Q2
R075 | number | T004 | - | line 161, page 3; reported PBT Q2
R076 | number | T004 | - | line 161, page 3; reported PAT Q2
R077 | number | T004 | - | line 163, page 3; one-time reversal in other income Q2
R078 | number | T004 | - | line 164, page 3; normalized PAT Q2
R079 | number | T004 | - | line 164, page 3; normalized PAT growth YoY Q2
R080 | number | T004 | - | line 164, page 3; normalized PAT margin Q2
R081 | number | T004 | - | line 168, page 3; H1 FY27 revenue
R082 | number | T004 | - | line 168, page 3; H1 revenue growth YoY
R083 | number | T004 | - | line 169, page 3; H1 FY27 EBITDA
R084 | number | T004 | - | line 169, page 3; H1 EBITDA growth YoY
R085 | number | T004 | - | line 170, page 3; H1 EBITDA margin
R086 | number | T004 | - | line 171, page 3; H1 normalized PAT growth YoY
R087 | number | T004 | - | line 171, page 3; H1 normalized PAT
R088 | number | T004 | - | line 171, page 3; H1 normalized PAT margin improvement
R089 | number | T004 | - | line 171, page 3; H1 normalized PAT margin
R090 | number | T004 | - | line 172, page 3; H1 reported PAT
R091 | number | T004 | - | line 172, page 3; H1 reported PAT growth YoY
R092 | number | T004 | - | line 173, page 3; one-time reversal recorded in Q2 (H1 context)
R093 | number | T004 | - | line 174, page 3; order book all-time high
R094 | number | T004 | - | line 174, page 3; order book increase vs same period last year
R095 | number | T004 | - | line 175, page 3; H1 revenue and EBITDA growth
R096 | number | T004 | - | line 177, page 3; H1 EBITDA margin
R097 | number | T004 | - | line 179, page 3; H1 finance cost decline YoY
R098 | number | T004 | - | line 180, page 3; H1 normalized PAT growth YoY
R099 | number | T004 | - | line 180, page 3; H1 normalized PAT margin improvement
R100 | number | T004 | - | line 180, page 3; H1 normalized PAT margin
R101 | number | T007 | - | line 199, page 3; margin impact of investment, Q2
R102 | number | T015 | - | line 230, page 4; FY27 EBITDA margin guidance
R103 | number | T017 | - | line 236, page 4; order book execution range
R104 | number | T017 | - | line 237, page 4; few orders beyond
R105 | number | T020 | - | line 243, page 4; analyst restates FY27 margin
R106 | number | T021 | - | line 244, page 4; FY27 margin guidance range
R107 | number | T025 | - | line 255, page 4; book-to-bill
R108 | number | T025 | - | line 256, page 4; order inflow, last quarter and this quarter
R109 | number | T029 | - | line 262, page 4; bid pipeline win ratio
R110 | number | T029 | - | line 264, page 4; win ratio
R111 | number | T031 | - | line 266, page 4; FY28 margin
R112 | number | T031 | - | line 266, page 4; FY27 margin
R113 | number | T037 | - | line 275, page 4; FY27 vs FY26 margin squeeze (analyst)
R114 | number | T039 | - | line 287, page 4; drop in margins from sales and marketing costs
R115 | number | T039 | - | line 288, page 4; threshold for adding sales and marketing cost (quarterly)
R116 | number | T039 | - | line 290, page 4; absorption cost vs last year
R117 | number | T040 | - | line 294, page 5; margin expansion
R118 | number | T041 | - | line 301, page 5; design-led order book (per newspaper interview, analyst)
R119 | number | T041 | - | line 302, page 5; executable period of design-led order book (analyst)
R120 | number | T042 | - | line 306, page 5; major build-to-spec programs
R121 | number | T042 | - | line 309, page 5; four programs, not in order book
R122 | number | T050 | - | line 323, page 5; order book pipeline (analyst)
R123 | number | T050 | - | line 324, page 5; win ratio (analyst)
R124 | number | T050 | - | line 324, page 5; implied orders (analyst computation)
R125 | number | T050 | - | line 326, page 5; B2S (analyst)
R126 | number | T051 | - | line 331, page 5; earlier pipeline
R127 | number | T051 | - | line 331, page 5; current pipeline
R128 | number | T051 | - | line 332, page 5; order intake from pipeline
R129 | number | T051 | - | line 333, page 5; order intake from existing pipeline
R130 | number | T052 | - | line 335, page 5; restated by analyst
R131 | number | T053 | - | line 338, page 5; unweighted pipeline
R132 | number | T053 | - | line 338, page 5; previous unweighted pipeline (billion dollars)
R133 | number | T053 | - | line 340, page 5; assumed next quarter closures
R134 | number | T053 | - | line 341, page 5; assumed pipeline additions
R135 | number | T054 | - | line 351, page 5; Q1 revenue growth (analyst)
R136 | number | T054 | - | line 351, page 5; Q2 revenue growth (analyst)
R137 | number | T055 | - | line 354, page 5; FY27 growth expectation
R138 | number | T055 | - | line 360, page 5; H1 revenue growth
R139 | number | T055 | - | line 361, page 5; H2 growth
R140 | number | T061 | - | line 376, page 5; B2S contribution in FY27 (analyst recalling guidance)
R141 | number | T061 | - | line 379, page 5; investment drag (analyst)
R142 | number | T063 | - | line 399, page 6; customer product launch years (analyst)
R143 | number | T063 | - | line 400, page 6; contract length (analyst)
R144 | number | T063 | - | line 402, page 6; airbuses, Indigo avionics contract (analyst)
R145 | number | T064 | - | line 411, page 6; production and revenue start
R146 | number | T071 | - | line 427, page 6; four B2S programs
R147 | number | T071 | - | line 428, page 6; production may start
R148 | number | T071 | - | line 429, page 6; full production and ramp up
R149 | number | T073 | - | line 431, page 6; program duration
R150 | number | T073 | - | line 431, page 6; years, some programs
R151 | number | T073 | - | line 431, page 6; years, some programs
R152 | number | T087 | - | line 451, page 6; order book (analyst)
R153 | number | T088 | - | line 452, page 6; average execution period
R154 | number | T088 | - | line 453, page 6; months, some order durations
R155 | number | T088 | - | line 453, page 6; months, some order durations
R156 | number | T088 | - | line 453, page 6; some order durations
R157 | number | T088 | - | line 455, page 6; average execution period
R158 | number | T091 | - | line 462, page 6; other income Q2 last year (analyst)
R159 | number | T091 | - | line 462, page 6; other income Q2 this year (analyst)
R160 | number | T096 | - | line 476, page 7; FY28 margins from backlog execution

## 5. FORWARD COMMITMENTS AND HEDGES
ROW_ID | category | turn | flags | note
R198 | forward | T002 | FORWARD_COMMIT | line 44, page 1; strategy
R199 | forward | T002 | FORWARD_COMMIT | line 46, page 1; margin impact
R200 | forward | T002 | FORWARD_COMMIT | line 51, page 1; stated focus
R201 | forward | T002 | FORWARD_COMMIT | line 56, page 1; growth sustain
R202 | forward | T003 | FORWARD_COMMIT | line 73, page 1; strategy phases
R203 | forward | T003 | FORWARD_COMMIT | line 78, page 1; margin framework
R204 | forward | T003 | FORWARD_COMMIT | line 82, page 2; Expand phase
R205 | forward | T003 | FORWARD_COMMIT | line 83, page 2; portfolio expansion
R206 | forward | T003 | FORWARD_COMMIT | line 86, page 2; margin framework
R207 | forward | T003 | FORWARD_COMMIT | line 88, page 2; Transform phase
R208 | forward | T003 | FORWARD_COMMIT | line 94, page 2; electronic products
R209 | forward | T003 | FORWARD_COMMIT | line 95, page 2; investment priority
R210 | forward | T003 | FORWARD_COMMIT | line 96, page 2; margin framework
R211 | forward | T003 | FORWARD_COMMIT | line 103, page 2; FY27 margin guidance
R212 | forward | T003 | FORWARD_COMMIT | line 117, page 2; growth engines
R213 | forward | T004 | FORWARD_COMMIT | line 150, page 3; working capital
R214 | forward | T004 | FORWARD_COMMIT | line 182, page 3; H2 priorities
R215 | forward | T009 | FORWARD_COMMIT | line 217, page 3; disclosure timing
R216 | forward | T013 | FORWARD_COMMIT | line 226, page 4; margin recovery
R217 | forward | T013 | FORWARD_COMMIT | line 228, page 4; margin recovery
R218 | forward | T015 | FORWARD_COMMIT | line 230, page 4; FY27 guidance
R219 | forward | T015 | FORWARD_COMMIT | line 231, page 4; margin guidance (period as spoken)
R220 | forward | T017 | FORWARD_COMMIT | line 239, page 4; semicap revenue
R221 | forward | T021 | FORWARD_COMMIT | line 244, page 4; FY27 guidance
R222 | forward | T023 | FORWARD_COMMIT | line 251, page 4; order conversion
R223 | forward | T025 | FORWARD_COMMIT | line 256, page 4; order inflow
R224 | forward | T029 | FORWARD_COMMIT | line 264, page 4; win ratio
R225 | forward | T031 | FORWARD_COMMIT | line 266, page 4; FY28 guidance
R226 | forward | T039 | FORWARD_COMMIT | line 288, page 4; cost commitment
R227 | forward | T040 | FORWARD_COMMIT | line 295, page 5; cost intensity
R228 | forward | T040 | FORWARD_COMMIT | line 297, page 5; cost commitment
R229 | forward | T040 | FORWARD_COMMIT | line 299, page 5; operating leverage
R230 | forward | T042 | FORWARD_COMMIT | line 308, page 5; B2S timeline
R231 | forward | T042 | FORWARD_COMMIT | line 309, page 5; B2S pipeline
R232 | forward | T042 | FORWARD_COMMIT | line 310, page 5; B2S to order book
R233 | forward | T046 | FORWARD_COMMIT | line 317, page 5; B2S timeline
R234 | forward | T051 | FORWARD_COMMIT | line 332, page 5; pipeline conversion
R235 | forward | T055 | FORWARD_COMMIT | line 354, page 5; FY27 growth
R236 | forward | T055 | FORWARD_COMMIT | line 361, page 5; H2 growth
R237 | forward | T062 | FORWARD_COMMIT | line 385, page 5; lag in returns
R238 | forward | T062 | FORWARD_COMMIT | line 394, page 5; product investment
R239 | forward | T064 | FORWARD_COMMIT | line 411, page 6; EBITOL program
R240 | forward | T064 | FORWARD_COMMIT | line 410, page 6; order book entry condition
R241 | forward | T071 | FORWARD_COMMIT | line 429, page 6; B2S timeline
R242 | forward | T077 | FORWARD_COMMIT | line 439, page 6; US business
R243 | forward | T081 | FORWARD_COMMIT | line 445, page 6; geography mix
R244 | forward | T090 | FORWARD_COMMIT | line 459, page 6; semicap
R245 | forward | T090 | FORWARD_COMMIT | line 460, page 6; AI/robotics
R246 | forward | T090 | FORWARD_COMMIT | line 461, page 6; disclosure timing
R247 | forward | T096 | FORWARD_COMMIT | line 472, page 6; closing
R248 | forward | T096 | FORWARD_COMMIT | line 476, page 7; FY28 margin
R249 | forward | T096 | FORWARD_COMMIT | line 478, page 7; order conversion
R250 | forward | T096 | FORWARD_COMMIT | line 482, page 7; closing

## 6. ENTITIES (all; participants repeated for accountability)
ROW_ID | category | turn | flags | note
R161 | entity | PRE-CALL HEADER (no turn; line 19) | - | line 19, page 1; company
R162 | entity | T001 | SEE_SEC1 | line 27, page 1; speaker
R163 | entity | T002 | SEE_SEC1 | line 29, page 1; speaker
R164 | entity | T002 | SEE_SEC1 | line 29, page 1; speaker
R165 | entity | T002 | SEE_SEC1 | line 28, page 1; moderator addressed by chairman
R166 | entity | T002 | - | line 39, page 1; supply chain pressure source
R167 | entity | T002 | - | line 41, page 1; segment
R168 | entity | T002 | - | line 41, page 1; segment
R169 | entity | T002 | - | line 41, page 1; segment
R170 | entity | T002 | - | line 41, page 1; segment
R171 | entity | T003 | - | line 76, page 1; core industry
R172 | entity | T003 | - | line 83, page 2; new growth area
R173 | entity | T003 | - | line 83, page 2; new growth area
R174 | entity | T003 | - | line 84, page 2; focus area
R175 | entity | T003 | - | line 91, page 2; offering
R176 | entity | T003 | - | line 114, page 2; acquired business
R177 | entity | T003 | MACHINE_TEXT_RENAME | line 114, page 2; renamed Altec Electronics
R178 | entity | T004 | - | line 152, page 3; segment
R179 | entity | T004 | - | line 153, page 3; product category
R180 | entity | T004 | - | line 153, page 3; product category
R181 | entity | T005 | SEE_SEC1 | line 191, page 3; analyst Q1
R182 | entity | T011 | SEE_SEC1 | line 219, page 3; analyst Q2
R183 | entity | T019 | SEE_SEC1 | line 241, page 4; analyst Q3
R184 | entity | T033 | SEE_SEC1 | line 268, page 4; analyst Q4, no response
R185 | entity | T034 | SEE_SEC1 | line 271, page 4; analyst Q5
R186 | entity | T039 | ENTITY_NEW_HIRE | line 289, page 4; new hire
R187 | entity | T049 | SEE_SEC1 | line 322, page 5; analyst Q6
R188 | entity | T057 | SEE_SEC1 | line 364, page 5; analyst Q7, dropped from queue
R189 | entity | T058 | SEE_SEC1 | line 370, page 5; analyst Q8
R190 | entity | T063 | SEE_SEC1 | line 399, page 6; large customer with signed order, per analyst
R191 | entity | T063 | - | line 402, page 6; customer, avionics suite
R192 | entity | T063 | - | line 402, page 6; airline, avionics contract
R193 | entity | T063 | - | line 402, page 6; aircraft in Indigo contract
R194 | entity | T065 | SEE_SEC1 | line 413, page 6; product signed with Honeywell (analyst)
R195 | entity | T067 | SEE_SEC1 | line 421, page 6; analyst Q9
R196 | entity | T077 | MACHINE_TEXT_RENAME | line 437, page 6; renamed Altec business
R197 | entity | T084 | SEE_SEC1 | line 448, page 6; analyst Q10

## 7. DATES AND TIMELINES
ROW_ID | category | turn | flags | note
R251 | date | PRE-CALL HEADER (no turn; line 19) | - | line 19, page 1; call date
R252 | date | T001 | - | line 24, page 1; results quarter
R253 | date | T002 | - | line 54, page 1; period
R254 | date | T002 | - | line 55, page 1; H2 FY27
R255 | date | T003 | - | line 82, page 2; Expand phase
R256 | date | T003 | - | line 88, page 2; Transform phase
R257 | date | T003 | - | line 94, page 2; growth onset
R258 | date | T004 | - | line 137, page 2; comparison period
R259 | date | T004 | - | line 148, page 3; sequential comparison
R260 | date | T009 | - | line 217, page 3; disclosure timing
R261 | date | T015 | - | line 231, page 4; double-digit margin (as spoken)
R262 | date | T025 | - | line 256, page 4; order inflow expectation
R263 | date | T037 | - | line 275, page 4; FY26 comparison (machine text)
R264 | date | T038 | - | line 280, page 4; FY26 vs FY27
R265 | date | T040 | - | line 295, page 5; investment intensity lower
R266 | date | T046 | - | line 317, page 5; B2S production
R267 | date | T055 | - | line 361, page 5; H2 FY27
R268 | date | T063 | - | line 399, page 6; customer product launch
R269 | date | T064 | - | line 411, page 6; production and revenue start
R270 | date | T071 | - | line 428, page 6; production may start
R271 | date | T071 | - | line 429, page 6; full production
R272 | date | T096 | - | line 476, page 7; margin 10 plus percent

## 8. QUALIFIERS, DISCLAIMERS, NON-DISCLOSURES
ROW_ID | category | turn | flags | note
R273 | qualifier | PRE-CALL HEADER (no turn; line 20) | SOURCE_CAVEAT | line 20, page 1; source caveat
R274 | qualifier | PRE-CALL HEADER (no turn; line 21) | SOURCE_CAVEAT | line 21, page 1; name corrections applied by supplier
R275 | qualifier | T002 | SOURCE_CAVEAT | line 30, page 1; forward-looking disclaimer
R276 | qualifier | T002 | SOURCE_CAVEAT | line 31, page 1; disclaimer pointer
R277 | qualifier | T003 | - | line 63, page 1; market size is an estimate
R278 | qualifier | T003 | - | line 69, page 1; market size is an estimate
R279 | qualifier | T004 | - | line 131, page 2; metric definition
R280 | qualifier | T004 | - | line 133, page 2; normalization basis
R281 | qualifier | T004 | - | line 142, page 2; reported vs normalized
R282 | qualifier | T004 | - | line 143, page 2; normalized basis
R283 | qualifier | T004 | - | line 163, page 3; other income composition
R284 | qualifier | T004 | - | line 173, page 3; H1 normalization basis (183 vs 182 elsewhere, verbatim)
R285 | qualifier | T007 | - | line 199, page 3; product development expensed
R286 | qualifier | T039 | - | line 286, page 4; expensed
R287 | qualifier | T053 | - | line 338, page 5; pipeline definition
R288 | qualifier | T053 | - | line 336, page 5; order backlog definition
R289 | qualifier | T042 | - | line 309, page 5; exclusion from order book
R290 | qualifier | T051 | - | line 327, page 5; pipeline composition
R291 | qualifier | T044 | - | line 313, page 5; order book exclusion
R292 | qualifier | T064 | - | line 409, page 6; order book exclusion
R293 | qualifier | T029 | - | line 262, page 4; basis of win ratio
R294 | qualifier | T086 | NOT_DISCLOSED | line 450, page 6; order book split not disclosed
R295 | qualifier | T007 | NOT_DISCLOSED | line 205, page 3; spend not disclosed
R296 | qualifier | T007 | NOT_DISCLOSED | line 208, page 3; spend not disclosed
R297 | qualifier | T062 | - | line 390, page 5; accounting policy
R298 | qualifier | T096 | - | line 473, page 6; accounting policy
R299 | qualifier | T039 | - | line 290, page 4; margin comparison basis
R300 | qualifier | T039 | - | line 282, page 4; margin quality statement
R301 | qualifier | T092 | - | line 464, page 6; other income composition
R302 | qualifier | T066 | - | line 420, page 6; program classification
R303 | qualifier | T066 | - | line 419, page 6; program scope

## ID ACCOUNTABILITY
All R001-R303 appear in sections 4-8. Orphans: none.

MISSING_FROM_STRUCTURED: 1 found (loop 1, A5 finding R5-M4).
M001 | forward | T017 | MISSING_FROM_STRUCTURED | line 238, page 4; "In the last two quarters, we have the revenues on that" (semicap revenue already booked in last two quarters, not quantified). Material: sits beside R220 (line 239, ramp-up); it is the only filed statement that semicap revenue has started, and the structured file holds the ramp but not the start.
No other missing rows. Audio gap 00:40:00-00:40:30 is covered by A1 turns T039-T040 (low confidence).
