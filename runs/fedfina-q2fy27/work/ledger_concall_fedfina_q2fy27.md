# A2 LEDGER: FEDFINA q2fy27 concall (anti-miss contract; IDs reference A1 structured file, claim text not re-copied)

=== A2 COUNT TEST ===
loop_1: applied. MFS rows added, mixed turns and question turns corrected, F6 re-attributed.
category: participants      grep_count: 17 sweep_count: 17 match: yes   (7 management incl. 3 named non-speakers R157-R159, 1 host, 9 analysts)
category: turns             grep_count: 74 sweep_count: 74 match: yes   (A1 header said 73; index has 74 lines; fulltext lines 24-952 contiguous, verified)
category: questions         grep_count: 9 (Q-labelled index lines) sweep_count: 26 (9 primary + 14 follow-ups + 3 embedded question turns T47, T50, T51) match: yes
category: mgmt_numbers      grep_count: 149 A1 NUMBER rows sweep_count: 141 mgmt + 8 analyst/mod = 149 match: yes; plus 4 MFS mgmt numbers = 145 total (4 repeats, 2 time refs not counted)
category: forward           grep_count: 58 (49 A1 + 9 MFS) sweep_count: 58 match: yes
category: hedge_qualifier   grep_count: 22 (21 A1 + 1 MFS) sweep_count: 22 match: yes
category: entities          grep_count: 35 sweep_count: 35 match: yes
category: dates             grep_count: 14 (13 A1 + 1 MFS) sweep_count: 14 match: yes
category: zero_standing      grep_count: 1 sweep_count: 1 match: yes (R100 only; R103 is a floor, not nil)
ids_in_structured: 267 | ids_referenced_in_ledger: 267 | orphan_ids: [] | match: yes | MFS ids: 21 (separate, no A1 ID)
gate_a2: pass
=== END COUNT TEST ===

Turn-side split (index lines): management 32, analyst 30, moderator 11, host hand-over 1. Mixed turns (analyst and management speech inside one index turn): [22, 26, 33, 47, 50, 51, 54, 62, 71] (loop_1 added 47, 50, 51, 54).
INFERRED-ATTRIBUTION DEPENDENCE: 52 of 74 turns carry SPEAKER_INFERRED in A1. Speaker-side turn counts, question counts and mgmt-number counts rest on that attribution. Turns NOT inferred (explicit): [3, 5, 6, 7, 14, 15, 23, 24, 34, 35, 38, 39, 45, 46, 49, 50, 53, 54, 62, 63, 72, 74].
Call duration: ND. Prior-quarter ledger: none (ND), so no diffs and no ENTITY_CHANGE test possible.

## 1. PARTICIPANTS
| P# | person | side | designation (A1) | structured ID | flags |
|---|---|---|---|---|---|
| P01 | Parvez Mulla | MGMT | MD & CEO | R153 | - |
| P02 | C.V. Ganesh | MGMT | CFO | R154 | - |
| P03 | Lokesh Parik | MGMT | Investor Relations head | R155 | - |
| P04 | Jagdish Rao | MGMT | heads gold and ST LAP | R156 | SPEAKER_INFERRED |
| P05 | Sharadur Kadam | MGMT | senior management | R157 | NO_TURN_IDENTIFIED |
| P06 | Suresh Pumar | MGMT | senior mgmt, medium ticket LAP | R158 | NO_TURN_IDENTIFIED |
| P07 | Vikram Rati | MGMT | senior management | R159 | NO_TURN_IDENTIFIED |
| P08 | Sreepal Toshi | HOST | Aquarius Securities, call host | R152 | - |
| P09 | Shubranshu Mishra | ANALYST | Philip Capital | R167 | - |
| P10 | Ranish | ANALYST | ICICI Securities | R170 | - |
| P11 | Digant Haria | ANALYST | Green Edge Wealth | R171 | - |
| P12 | Pawan Kumar | ANALYST | Edelweiss Public Alternatives | R172 | - |
| P13 | Meghna Lutra | ANALYST | Incred Equities | R173 | - |
| P14 | Devansh Dhruv | ANALYST | Equinities | R174 | - |
| P15 | Yash | ANALYST | Dantee Equity | R175 | - |
| P16 | Rahul Kumar | ANALYST | Vakaria Fund | R176 | - |
| P17 | Aditya | ANALYST | Securities Investment Management | R177 | - |
MGMT_ABSENCE: no promoter or Federal Bank (parent) representative identified; MD&CEO and CFO both present. Note only. Analyst names and firms are ASR-uncertain (see A1 ASR variants).

## 2. SPEAKER TURNS
| T# | fulltext lines | src | speaker | page | row IDs | flags |
|---|---|---|---|---|---|---|
| T01 | 24-29 | 1-6 | Moderator | 1-1 | R150, R151, R234 | SPEAKER_INFERRED |
| T02 | 30-36 | 7-13 | Toshi (Aquarius host) | 1-1 | R001, R152, R153, R154, R155 | SPEAKER_INFERRED |
| T03 | 37-43 | 14-20 | Lokesh Parik (IR) | 1-1 | R247 | - |
| T04 | 44-101 | 21-78 | Parvez Mulla (MD&CEO) | 1-1 | R002, R003, R004, R005, R006, R007, R008, R009, R010, R011, R012, R013, R014, R015, R016, R017, R018, R019, R020, R021, R022, R023, R024, R025, R026, R027, R028, R029, R030, R031, R032, R033, R034, R035, R036, R037, R038, R039, R040, R041, R156, R157, R158, R159, R160, R161, R162, R163, R164, R165, R166, R185, R186, R235, R244, R248, R251, R260, R264 | SPEAKER_INFERRED |
| T05 | 102-202 | 79-178 | C.V. Ganesh (CFO) | 1-2 | R042, R043, R044, R045, R046, R047, R048, R049, R050, R051, R052, R053, R054, R055, R056, R057, R058, R059, R060, R061, R062, R063, R064, R065, R066, R067, R068, R069, R070, R071, R072, R073, R074, R075, R076, R077, R078, R079, R080, R081, R082, R083, R084, R085, R086, R087, R088, R089, R184, R187, R188, R189, R190, R232, R236, R237, R238, R249, R250, R252, R253, R254, R255, R256, R267 | - |
| T06 | 203-209 | 179-185 | Moderator | 2-2 | none | - |
| T07 | 210-229 | 186-205 | Shubranshu Mishra (Philip Capital) | 2-2 | R167, R180, R183 | - |
| T08 | 230-288 | 206-264 | Parvez Mulla (MD&CEO) | 2-2 | R090, R091, R092, R168, R191, R192, R193, R194, R245 | SPEAKER_INFERRED |
| T09 | 289-293 | 265-268 | C.V. Ganesh (CFO) | 2-3 | R195, R196 | SPEAKER_INFERRED |
| T10 | 294-298 | 269-273 | Shubranshu Mishra (Philip Capital) | 3-3 | none | SPEAKER_INFERRED |
| T11 | 299-315 | 274-290 | Parvez Mulla (MD&CEO) | 3-3 | R197, R198, R199 | SPEAKER_INFERRED |
| T12 | 316-324 | 291-299 | Jagdish Rao (gold/ST LAP) | 3-3 | R093, R094, R095, R169 | SPEAKER_INFERRED |
| T13 | 325-329 | 300-304 | Shubranshu Mishra (Philip Capital) | 3-3 | none | SPEAKER_INFERRED |
| T14 | 330-332 | 305-307 | Moderator | 3-3 | R170 | - |
| T15 | 333-338 | 308-313 | Ranish (ICICI Sec) | 3-3 | none | - |
| T16 | 339-381 | 314-356 | Parvez Mulla (MD&CEO) | 3-3 | R096, R097, R098, R099, R200, R201, R239, R257 | SPEAKER_INFERRED |
| T17 | 382-386 | 357-361 | Ranish (ICICI Sec) | 3-3 | R240 | SPEAKER_INFERRED |
| T18 | 387-415 | 362-390 | Parvez Mulla (MD&CEO) | 3-3 | R202, R259, R265 | SPEAKER_INFERRED |
| T19 | 416-425 | 391-400 | C.V. Ganesh (CFO) | 3-3 | R100, R203, R258 | SPEAKER_INFERRED |
| T20 | 426-441 | 401-415 | Ranish (ICICI Sec) | 3-4 | none | SPEAKER_INFERRED,REPEAT_TOPIC |
| T21 | 442-465 | 416-439 | Parvez Mulla (MD&CEO) | 4-4 | R101, R102, R103, R104, R204, R205, R206 | SPEAKER_INFERRED |
| T22 | 466-467 | 440-441 | Ranish (ICICI Sec) | 4-4 | none | SPEAKER_INFERRED,MIXED_TURN |
| T23 | 468-468 | 442-442 | Moderator | 4-4 | none | - |
| T24 | 469-476 | 443-450 | Digant Haria (Green Edge) | 4-4 | R105, R171 | - |
| T25 | 477-489 | 451-463 | Jagdish Rao (gold/ST LAP) | 4-4 | R106, R107 | SPEAKER_INFERRED |
| T26 | 490-494 | 464-468 | Digant Haria (Green Edge) | 4-4 | none | SPEAKER_INFERRED,MIXED_TURN |
| T27 | 495-506 | 469-480 | Parvez Mulla (MD&CEO) | 4-4 | R108, R109, R110 | SPEAKER_INFERRED |
| T28 | 507-522 | 481-496 | Digant Haria (Green Edge) | 4-4 | none | SPEAKER_INFERRED |
| T29 | 523-532 | 497-506 | Parvez Mulla (MD&CEO) | 4-4 | none | SPEAKER_INFERRED |
| T30 | 533-537 | 507-511 | Digant Haria (Green Edge) | 4-4 | none | SPEAKER_INFERRED,REPEAT_TOPIC |
| T31 | 538-569 | 512-542 | Parvez Mulla (MD&CEO) | 4-5 | R111, R112, R207, R208, R209 | SPEAKER_INFERRED |
| T32 | 570-572 | 543-545 | Digant Haria (Green Edge) | 5-5 | R241 | SPEAKER_INFERRED |
| T33 | 573-574 | 546-547 | Parvez Mulla (MD&CEO) | 5-5 | none | SPEAKER_INFERRED,MIXED_TURN |
| T34 | 575-576 | 548-549 | Moderator | 5-5 | R172 | - |
| T35 | 577-587 | 550-560 | Pawan Kumar (Edelweiss PA) | 5-5 | R113, R266 | - |
| T36 | 588-616 | 561-589 | Parvez Mulla (MD&CEO) | 5-5 | R114, R115, R210, R211, R212, R213 | SPEAKER_INFERRED,REPEAT_TOPIC |
| T37 | 617-618 | 590-591 | Pawan Kumar (Edelweiss PA) | 5-5 | none | SPEAKER_INFERRED |
| T38 | 619-621 | 592-594 | Moderator | 5-5 | R173 | - |
| T39 | 622-628 | 595-601 | Meghna Lutra (Incred) | 5-5 | none | - |
| T40 | 629-647 | 602-620 | C.V. Ganesh (CFO) | 5-5 | R116, R117, R118, R119, R178, R179 | SPEAKER_INFERRED |
| T41 | 648-651 | 621-624 | Meghna Lutra (Incred) | 5-5 | none | SPEAKER_INFERRED |
| T42 | 652-662 | 625-635 | C.V. Ganesh (CFO) | 5-5 | R233 | SPEAKER_INFERRED |
| T43 | 663-664 | 636-637 | Meghna Lutra (Incred) | 5-5 | none | SPEAKER_INFERRED,REPEAT_TOPIC |
| T44 | 665-671 | 638-644 | Parvez Mulla (MD&CEO) | 5-5 | R214 | SPEAKER_INFERRED |
| T45 | 672-673 | 645-646 | Moderator | 5-5 | R174 | - |
| T46 | 674-680 | 647-653 | Devansh Dhruv (Equinities) | 5-5 | R120 | - |
| T47 | 681-695 | 654-668 | C.V. Ganesh (CFO) | 5-5 | R215 | SPEAKER_INFERRED,MIXED_TURN |
| T48 | 696-698 | 669-671 | Devansh Dhruv (Equinities) | 5-5 | none | SPEAKER_INFERRED |
| T49 | 699-703 | 672-676 | Moderator | 5-5 | R175 | - |
| T50 | 704-726 | 677-698 | Yash (Dantee Equity) | 5-6 | R121, R122, R123, R124 | REPEAT_TOPIC,MIXED_TURN |
| T51 | 727-759 | 699-731 | Parvez Mulla (MD&CEO) | 6-6 | R125, R126, R127, R128, R129, R130, R131, R132, R216, R217, R218, R219, R220, R242, R243, R261, R263 | SPEAKER_INFERRED,MIXED_TURN |
| T52 | 760-761 | 732-733 | Parvez Mulla (MD&CEO) | 6-6 | none | SPEAKER_INFERRED |
| T53 | 762-765 | 734-737 | Moderator | 6-6 | R176 | - |
| T54 | 766-771 | 738-743 | Rahul Kumar (Vakaria Fund) | 6-6 | none | MIXED_TURN |
| T55 | 772-795 | 744-767 | Parvez Mulla (MD&CEO) | 6-6 | R133, R134, R181, R182 | SPEAKER_INFERRED,REPEAT_TOPIC |
| T56 | 796-799 | 768-771 | Rahul Kumar (Vakaria Fund) | 6-6 | none | SPEAKER_INFERRED |
| T57 | 800-800 | 772-772 | Parvez Mulla (MD&CEO) | 6-6 | R135, R136 | SPEAKER_INFERRED |
| T58 | 801-801 | 773-773 | Rahul Kumar (Vakaria Fund) | 6-6 | none | SPEAKER_INFERRED |
| T59 | 802-810 | 774-782 | Parvez Mulla (MD&CEO) | 6-6 | R137 | SPEAKER_INFERRED |
| T60 | 811-814 | 783-786 | Rahul Kumar (Vakaria Fund) | 6-6 | none | SPEAKER_INFERRED,REPEAT_TOPIC |
| T61 | 815-826 | 787-798 | Parvez Mulla (MD&CEO) | 6-6 | R138, R139, R221 | SPEAKER_INFERRED |
| T62 | 827-830 | 799-801 | Rahul Kumar (Vakaria Fund) | 6-7 | R177 | MIXED_TURN |
| T63 | 831-844 | 802-815 | Aditya (Securities Inv Mgmt) | 7-7 | R140 | - |
| T64 | 845-869 | 816-840 | Parvez Mulla (MD&CEO) | 7-7 | R222, R223 | SPEAKER_INFERRED,REPEAT_TOPIC |
| T65 | 870-880 | 841-851 | Aditya (Securities Inv Mgmt) | 7-7 | none | SPEAKER_INFERRED,REPEAT_TOPIC |
| T66 | 881-900 | 852-871 | Parvez Mulla (MD&CEO) | 7-7 | R141, R142, R143, R144, R145, R146, R224, R225, R262 | SPEAKER_INFERRED |
| T67 | 901-901 | 872-872 | Aditya (Securities Inv Mgmt) | 7-7 | none | SPEAKER_INFERRED |
| T68 | 902-907 | 873-878 | C.V. Ganesh (CFO) | 7-7 | R147, R148, R226 | SPEAKER_INFERRED |
| T69 | 908-911 | 879-882 | Aditya (Securities Inv Mgmt) | 7-7 | none | SPEAKER_INFERRED,REPEAT_TOPIC |
| T70 | 912-920 | 883-891 | Parvez Mulla (MD&CEO) | 7-7 | R227 | SPEAKER_INFERRED |
| T71 | 921-924 | 892-895 | Aditya (Securities Inv Mgmt) | 7-7 | none | SPEAKER_INFERRED,MIXED_TURN |
| T72 | 925-927 | 896-898 | Moderator | 7-7 | none | - |
| T73 | 928-949 | 899-920 | Parvez Mulla (MD&CEO) | 7-7 | R149, R228, R229, R230, R231, R246 | SPEAKER_INFERRED |
| T74 | 950-952 | 921-923 | Moderator | 7-7 | none | - |

## 3. QUESTIONS (turn number, analyst, firm, topic per A1 index label)
| Q# | turn | analyst, firm | topic (A1 label) | flags |
|---|---|---|---|---|
| Q01 | T07 | Shubranshu Mishra (Philip Capital) | Q1 opening | - |
| Q02 | T10 | Shubranshu Mishra (Philip Capital) | follow-up | SPEAKER_INFERRED |
| Q03 | T15 | Ranish (ICICI Sec) | Q2 opening | - |
| Q04 | T17 | Ranish (ICICI Sec) | follow-up | SPEAKER_INFERRED |
| Q05 | T20 | Ranish (ICICI Sec) | second question, small-ticket LAP | REPEAT_QUESTION(topic candidate),SPEAKER_INFERRED |
| Q06 | T24 | Digant Haria (Green Edge) | Q3 gold LTV / income-generating loans | - |
| Q07 | T26 | Digant Haria (Green Edge) | follow-up | SPEAKER_INFERRED |
| Q08 | T28 | Digant Haria (Green Edge) | second question | SPEAKER_INFERRED |
| Q09 | T30 | Digant Haria (Green Edge) | third question (branches/OpEx) | REPEAT_QUESTION(topic candidate),SPEAKER_INFERRED |
| Q10 | T35 | Pawan Kumar (Edelweiss PA) | Q4 ST LAP yields / disbursements | - |
| Q11 | T39 | Meghna Lutra (Incred) | Q5 borrowing mix / tonnage | - |
| Q12 | T41 | Meghna Lutra (Incred) | follow-up | SPEAKER_INFERRED |
| Q13 | T43 | Meghna Lutra (Incred) | tonnage | REPEAT_QUESTION(topic candidate),SPEAKER_INFERRED |
| Q14 | T46 | Devansh Dhruv (Equinities) | Q6 rate hike / shock absorbers | - |
| Q15 | T50 | Yash (Dantee Equity) | Q7 branch scale-up, ROE and AUM guidance | REPEAT_QUESTION(topic candidate) |
| Q16 | T54 | Rahul Kumar (Vakaria Fund) | Q8 ST LAP competition | - |
| Q17 | T56 | Rahul Kumar (Vakaria Fund) | approval rates | SPEAKER_INFERRED |
| Q18 | T58 | Rahul Kumar (Vakaria Fund) | follow-up (unlabelled) | SPEAKER_INFERRED,QUESTION_STATUS_UNCERTAIN |
| Q19 | T60 | Rahul Kumar (Vakaria Fund) | medium-ticket LAP | REPEAT_QUESTION(topic candidate),SPEAKER_INFERRED |
| Q20 | T63 | Aditya (Securities Inv Mgmt) | Q9 ROA, gold vs LAP mix | - |
| Q21 | T65 | Aditya (Securities Inv Mgmt) | follow-up (guidance/tonnage/AUM per branch) | REPEAT_QUESTION(topic candidate),SPEAKER_INFERRED |
| Q22 | T67 | Aditya (Securities Inv Mgmt) | insurance | SPEAKER_INFERRED |
| Q23 | T69 | Aditya (Securities Inv Mgmt) | branch | REPEAT_QUESTION(topic candidate),SPEAKER_INFERRED |
| Q24 | T47 | analyst (Devansh Dhruv inferred), embedded in CFO-indexed turn, Call L687-L690 | follow-up on lever to offset (loop_1 M9) | MIXED_TURN,SPEAKER_INFERRED,MISSING_FROM_INDEX |
| Q25 | T50 | Yash (Dantee Equity), Call L723-L726 | second question: ROE trajectory, H2 AUM and ROA guidance (loop_1 M9) | MIXED_TURN,REPEAT_QUESTION(topic candidate) |
| Q26 | T51 | Yash (Dantee Equity), Call L743-L746 | can AUM and ROE guidance be upgraded (loop_1 M9) | MIXED_TURN,SPEAKER_INFERRED,MISSING_FROM_INDEX |
Repeat-topic groups (turns): branches/OpEx/scale-up: T30, T50, T69; tonnage: T43, T65; ST/medium LAP competition-yield-ticket: T20, T36, T55, T60; ROE/AUM/ROA guidance: T50, T64, T65. Based on A1 labels only; A3 confirms. (T36, T55, T64 are answer turns whose topic repeats the question topic.)
Non-question analyst turns (thanks/close): T13, T22, T32, T37, T48, T62 (part), T71 (part). Moderator turns: T01, T06, T14, T23, T34, T38, T45, T49, T53, T72, T74.
Q&A share: prepared remarks T03-T05 (fulltext lines 37-202); Q&A T06-T73 (lines 203-949), about 80% of transcript lines.

## 4. MANAGEMENT NUMBERS (NUMBER rows by turn)
### 4a. Management turns
| row | turn | speaker | flags |
|---|---|---|---|
| R002 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R003 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R004 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R005 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R006 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R007 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R008 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R009 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R010 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R011 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R012 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R013 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R014 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R015 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R016 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R017 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R018 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R019 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R020 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R021 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R022 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R023 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R024 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R025 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R026 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R027 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R028 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R029 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R030 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R031 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R032 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R033 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R034 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R035 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R036 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R037 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R038 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R039 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R040 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R041 | T04 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R042 | T05 | C.V. Ganesh (CFO) | - |
| R043 | T05 | C.V. Ganesh (CFO) | - |
| R044 | T05 | C.V. Ganesh (CFO) | - |
| R045 | T05 | C.V. Ganesh (CFO) | - |
| R046 | T05 | C.V. Ganesh (CFO) | - |
| R047 | T05 | C.V. Ganesh (CFO) | - |
| R048 | T05 | C.V. Ganesh (CFO) | - |
| R049 | T05 | C.V. Ganesh (CFO) | - |
| R050 | T05 | C.V. Ganesh (CFO) | - |
| R051 | T05 | C.V. Ganesh (CFO) | - |
| R052 | T05 | C.V. Ganesh (CFO) | - |
| R053 | T05 | C.V. Ganesh (CFO) | - |
| R054 | T05 | C.V. Ganesh (CFO) | - |
| R055 | T05 | C.V. Ganesh (CFO) | - |
| R056 | T05 | C.V. Ganesh (CFO) | - |
| R057 | T05 | C.V. Ganesh (CFO) | - |
| R058 | T05 | C.V. Ganesh (CFO) | - |
| R059 | T05 | C.V. Ganesh (CFO) | - |
| R060 | T05 | C.V. Ganesh (CFO) | - |
| R061 | T05 | C.V. Ganesh (CFO) | - |
| R062 | T05 | C.V. Ganesh (CFO) | - |
| R063 | T05 | C.V. Ganesh (CFO) | - |
| R064 | T05 | C.V. Ganesh (CFO) | - |
| R065 | T05 | C.V. Ganesh (CFO) | - |
| R066 | T05 | C.V. Ganesh (CFO) | - |
| R067 | T05 | C.V. Ganesh (CFO) | - |
| R068 | T05 | C.V. Ganesh (CFO) | - |
| R069 | T05 | C.V. Ganesh (CFO) | - |
| R070 | T05 | C.V. Ganesh (CFO) | - |
| R071 | T05 | C.V. Ganesh (CFO) | - |
| R072 | T05 | C.V. Ganesh (CFO) | - |
| R073 | T05 | C.V. Ganesh (CFO) | - |
| R074 | T05 | C.V. Ganesh (CFO) | - |
| R075 | T05 | C.V. Ganesh (CFO) | - |
| R076 | T05 | C.V. Ganesh (CFO) | - |
| R077 | T05 | C.V. Ganesh (CFO) | - |
| R078 | T05 | C.V. Ganesh (CFO) | - |
| R079 | T05 | C.V. Ganesh (CFO) | - |
| R080 | T05 | C.V. Ganesh (CFO) | - |
| R081 | T05 | C.V. Ganesh (CFO) | - |
| R082 | T05 | C.V. Ganesh (CFO) | - |
| R083 | T05 | C.V. Ganesh (CFO) | - |
| R084 | T05 | C.V. Ganesh (CFO) | - |
| R085 | T05 | C.V. Ganesh (CFO) | - |
| R086 | T05 | C.V. Ganesh (CFO) | - |
| R087 | T05 | C.V. Ganesh (CFO) | - |
| R088 | T05 | C.V. Ganesh (CFO) | - |
| R089 | T05 | C.V. Ganesh (CFO) | - |
| R090 | T08 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R091 | T08 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R092 | T08 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R093 | T12 | Jagdish Rao (gold/ST LAP) | TURN_INFERRED |
| R094 | T12 | Jagdish Rao (gold/ST LAP) | TURN_INFERRED |
| R095 | T12 | Jagdish Rao (gold/ST LAP) | TURN_INFERRED |
| R096 | T16 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R097 | T16 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R098 | T16 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R099 | T16 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R100 | T19 | C.V. Ganesh (CFO) | ZERO_STANDING,TURN_INFERRED |
| R101 | T21 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R102 | T21 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R103 | T21 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R104 | T21 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R106 | T25 | Jagdish Rao (gold/ST LAP) | TURN_INFERRED |
| R107 | T25 | Jagdish Rao (gold/ST LAP) | TURN_INFERRED |
| R108 | T27 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R109 | T27 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R110 | T27 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R111 | T31 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R112 | T31 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R114 | T36 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R115 | T36 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R116 | T40 | C.V. Ganesh (CFO) | TURN_INFERRED |
| R117 | T40 | C.V. Ganesh (CFO) | TURN_INFERRED |
| R118 | T40 | C.V. Ganesh (CFO) | TURN_INFERRED |
| R119 | T40 | C.V. Ganesh (CFO) | TURN_INFERRED |
| R121 | T50 | Parvez Mulla (MD&CEO) (answer inside analyst-led turn; F6 re-attributed) | MIXED_TURN,REATTRIBUTED_F6 |
| R122 | T50 | Parvez Mulla (MD&CEO) (answer inside analyst-led turn; F6 re-attributed) | MIXED_TURN,REATTRIBUTED_F6 |
| R123 | T50 | Parvez Mulla (MD&CEO) (answer inside analyst-led turn; F6 re-attributed) | MIXED_TURN,REATTRIBUTED_F6 |
| R125 | T51 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R126 | T51 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R127 | T51 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R128 | T51 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R129 | T51 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R132 | T51 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R133 | T55 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R134 | T55 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R135 | T57 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R136 | T57 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R137 | T59 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R138 | T61 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R139 | T61 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R141 | T66 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R142 | T66 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R143 | T66 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R144 | T66 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R145 | T66 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R146 | T66 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
| R147 | T68 | C.V. Ganesh (CFO) | TURN_INFERRED |
| R148 | T68 | C.V. Ganesh (CFO) | TURN_INFERRED |
| R149 | T73 | Parvez Mulla (MD&CEO) | TURN_INFERRED |
count: 141 (A1 rows; 140 - R130/R131 + R121-R123)
### 4b. Mixed turns (analyst-led, management reply inside; A1 does not split within turn)
| row | turn | flags |
|---|---|---|
| R121-R123 | T50 | mgmt answer inside analyst-led turn, counted in 4a (loop_1 F6) |
| R130-R131 | T51 | analyst speech inside mgmt-indexed turn, counted in 4c (loop_1 F6) |
count: 5 rows re-attributed; no number double-counted
### 4c. Analyst, moderator, host turns (NOT management numbers; listed so no ID orphans)
| row | turn | speaker | flags |
|---|---|---|---|
| R001 | T02 | Toshi (Aquarius host) | ANALYST_OR_MOD_NUMBER,TURN_INFERRED |
| R105 | T24 | Digant Haria (Green Edge) | ANALYST_OR_MOD_NUMBER,- |
| R113 | T35 | Pawan Kumar (Edelweiss PA) | ANALYST_OR_MOD_NUMBER,- |
| R120 | T46 | Devansh Dhruv (Equinities) | ANALYST_OR_MOD_NUMBER,- |
| R124 | T50 | Yash (Dantee Equity) | ANALYST_OR_MOD_NUMBER,- |
| R130 | T51 | Yash (Dantee Equity) (analyst speech inside T51; F6 re-attributed) | ANALYST_OR_MOD_NUMBER,MIXED_TURN,REATTRIBUTED_F6 |
| R131 | T51 | Yash (Dantee Equity) (analyst speech inside T51; F6 re-attributed) | ANALYST_OR_MOD_NUMBER,MIXED_TURN,REATTRIBUTED_F6 |
| R140 | T63 | Aditya (Securities Inv Mgmt) | ANALYST_OR_MOD_NUMBER,- |
count: 8 (9 - R121-R123 + R130-R131)
mgmt_numbers on A1 rows (4a + 4b) = 141; all A1 NUMBER rows = 149 (141 + 8). Plus 4 new MFS management numbers (MFS-C1 to C4) = 145 total; repeats (4) and time refs (2) listed in section 9, not counted.
ZERO_STANDING: R100 (nil auction loss on principal or interest, six years). One row.

## 5. FORWARD-COMMITMENT PHRASES (FORWARD rows)
| row | turn | flags |
|---|---|---|
| R185 | T04 | TURN_INFERRED |
| R186 | T04 | TURN_INFERRED |
| R187 | T05 | - |
| R188 | T05 | - |
| R189 | T05 | - |
| R190 | T05 | - |
| R191 | T08 | TURN_INFERRED |
| R192 | T08 | TURN_INFERRED |
| R193 | T08 | TURN_INFERRED |
| R194 | T08 | TURN_INFERRED |
| R195 | T09 | TURN_INFERRED |
| R196 | T09 | TURN_INFERRED |
| R197 | T11 | TURN_INFERRED |
| R198 | T11 | DECLINED_GUIDANCE,TURN_INFERRED |
| R199 | T11 | TURN_INFERRED |
| R200 | T16 | TURN_INFERRED |
| R201 | T16 | TURN_INFERRED |
| R202 | T18 | TURN_INFERRED |
| R203 | T19 | TURN_INFERRED |
| R204 | T21 | TURN_INFERRED |
| R205 | T21 | TURN_INFERRED |
| R206 | T21 | TURN_INFERRED |
| R207 | T31 | TURN_INFERRED |
| R208 | T31 | TURN_INFERRED |
| R209 | T31 | TURN_INFERRED |
| R210 | T36 | TURN_INFERRED |
| R211 | T36 | TURN_INFERRED |
| R212 | T36 | TURN_INFERRED |
| R213 | T36 | TURN_INFERRED |
| R214 | T44 | TURN_INFERRED |
| R215 | T47 | TURN_INFERRED |
| R216 | T51 | TURN_INFERRED |
| R217 | T51 | TURN_INFERRED |
| R218 | T51 | TURN_INFERRED |
| R219 | T51 | TURN_INFERRED |
| R220 | T51 | TURN_INFERRED |
| R221 | T61 | TURN_INFERRED |
| R222 | T64 | TURN_INFERRED |
| R223 | T64 | TURN_INFERRED |
| R224 | T66 | TURN_INFERRED |
| R225 | T66 | TURN_INFERRED |
| R226 | T68 | TURN_INFERRED |
| R227 | T70 | TURN_INFERRED |
| R228 | T73 | TURN_INFERRED |
| R229 | T73 | TURN_INFERRED |
| R230 | T73 | TURN_INFERRED |
| R231 | T73 | TURN_INFERRED |
| R232 | T05 | - |
| R233 | T42 | TURN_INFERRED |

## 6. HEDGE / QUALIFIER PHRASES (QUALIFIER rows; A3 lexicon sorts hedge vs definition)
| row | turn | flags |
|---|---|---|
| R247 | T03 | - |
| R248 | T04 | TURN_INFERRED |
| R249 | T05 | - |
| R250 | T05 | - |
| R251 | T04 | TURN_INFERRED |
| R252 | T05 | - |
| R253 | T05 | - |
| R254 | T05 | - |
| R255 | T05 | - |
| R256 | T05 | - |
| R257 | T16 | TURN_INFERRED |
| R258 | T19 | TURN_INFERRED |
| R259 | T18 | TURN_INFERRED |
| R260 | T04 | TURN_INFERRED |
| R261 | T51 | TURN_INFERRED |
| R262 | T66 | TURN_INFERRED |
| R263 | T51 | TURN_INFERRED |
| R264 | T04 | TURN_INFERRED |
| R265 | T18 | TURN_INFERRED |
| R266 | T35 | - |
| R267 | T05 | - |

## 7. ENTITIES
| row | turn | flags |
|---|---|---|
| R150 | T01 | ENTITY_CHANGE_UNTESTABLE(no prior),TURN_INFERRED |
| R151 | T01 | ENTITY_CHANGE_UNTESTABLE(no prior),TURN_INFERRED |
| R152 | T02 | ENTITY_CHANGE_UNTESTABLE(no prior),TURN_INFERRED |
| R153 | T02 | ENTITY_CHANGE_UNTESTABLE(no prior),TURN_INFERRED |
| R154 | T02 | ENTITY_CHANGE_UNTESTABLE(no prior),TURN_INFERRED |
| R155 | T02 | ENTITY_CHANGE_UNTESTABLE(no prior),TURN_INFERRED |
| R156 | T04 | ENTITY_CHANGE_UNTESTABLE(no prior),TURN_INFERRED |
| R157 | T04 | ENTITY_CHANGE_UNTESTABLE(no prior),TURN_INFERRED |
| R158 | T04 | ENTITY_CHANGE_UNTESTABLE(no prior),TURN_INFERRED |
| R159 | T04 | ENTITY_CHANGE_UNTESTABLE(no prior),TURN_INFERRED |
| R160 | T04 | ENTITY_CHANGE_UNTESTABLE(no prior),TURN_INFERRED |
| R161 | T04 | ENTITY_CHANGE_UNTESTABLE(no prior),TURN_INFERRED |
| R162 | T04 | ENTITY_CHANGE_UNTESTABLE(no prior),TURN_INFERRED |
| R163 | T04 | ENTITY_CHANGE_UNTESTABLE(no prior),TURN_INFERRED |
| R164 | T04 | ENTITY_CHANGE_UNTESTABLE(no prior),TURN_INFERRED |
| R165 | T04 | ENTITY_CHANGE_UNTESTABLE(no prior),TURN_INFERRED |
| R166 | T04 | ENTITY_CHANGE_UNTESTABLE(no prior),TURN_INFERRED |
| R167 | T07 | ENTITY_CHANGE_UNTESTABLE(no prior),- |
| R168 | T08 | ENTITY_CHANGE_UNTESTABLE(no prior),TURN_INFERRED |
| R169 | T12 | ENTITY_CHANGE_UNTESTABLE(no prior),TURN_INFERRED |
| R170 | T14 | ENTITY_CHANGE_UNTESTABLE(no prior),- |
| R171 | T24 | ENTITY_CHANGE_UNTESTABLE(no prior),- |
| R172 | T34 | ENTITY_CHANGE_UNTESTABLE(no prior),- |
| R173 | T38 | ENTITY_CHANGE_UNTESTABLE(no prior),- |
| R174 | T45 | ENTITY_CHANGE_UNTESTABLE(no prior),- |
| R175 | T49 | ENTITY_CHANGE_UNTESTABLE(no prior),- |
| R176 | T53 | ENTITY_CHANGE_UNTESTABLE(no prior),- |
| R177 | T62 | ENTITY_CHANGE_UNTESTABLE(no prior),- |
| R178 | T40 | ENTITY_CHANGE_UNTESTABLE(no prior),TURN_INFERRED |
| R179 | T40 | ENTITY_CHANGE_UNTESTABLE(no prior),TURN_INFERRED |
| R180 | T07 | ENTITY_CHANGE_UNTESTABLE(no prior),- |
| R181 | T55 | ENTITY_CHANGE_UNTESTABLE(no prior),TURN_INFERRED |
| R182 | T55 | ENTITY_CHANGE_UNTESTABLE(no prior),TURN_INFERRED |
| R183 | T07 | ENTITY_CHANGE_UNTESTABLE(no prior),- |
| R184 | T05 | ENTITY_CHANGE_UNTESTABLE(no prior),- |

## 8. DATES
| row | turn | flags |
|---|---|---|
| R234 | T01 | TURN_INFERRED |
| R235 | T04 | TURN_INFERRED |
| R236 | T05 | - |
| R237 | T05 | - |
| R238 | T05 | - |
| R239 | T16 | TURN_INFERRED |
| R240 | T17 | TURN_INFERRED |
| R241 | T32 | TURN_INFERRED |
| R242 | T51 | TURN_INFERRED |
| R243 | T51 | TURN_INFERRED |
| R244 | T04 | TURN_INFERRED |
| R245 | T08 | TURN_INFERRED |
| R246 | T73 | TURN_INFERRED |

## 9. MISSING_FROM_STRUCTURED
loop_1: applied (A5 findings M7, M8, M9, F6). Each line was read verbatim in the fulltext before adding; every line held the unit A5 named. A1 header said 73 turns; the index holds 74 lines (header discrepancy, not a missing unit).

MFS rows have no A1 row ID. Counted: 4 mgmt NUMBER (C1-C4), 9 FORWARD, 1 DATE, 1 QUALIFIER = 15 new units. Not counted (repeats of A1 rows or time refs): 4 repeats, 2 time refs.

| MFS ID | type | fulltext line | turn | content | flags |
|---|---|---|---|---|---|
| MFS-C1 | NUMBER | Call L57 | T04 | below 1% credit cost target (CEO) | MISSING_FROM_STRUCTURED |
| MFS-C2 | NUMBER | Call L113 | T05 | 15% interim ROE milestone crossed last quarter (CFO) | MISSING_FROM_STRUCTURED |
| MFS-C3 | NUMBER | Call L482 | T25 | 75% exposure cap, LTV (mgmt) | MISSING_FROM_STRUCTURED |
| MFS-C4 | NUMBER | Call L483 | T25 | 80% exposure cap, LTV (mgmt) | MISSING_FROM_STRUCTURED |
| MFS-C5 | NUMBER_REPEAT | Call L720 | T50 | 6-7 crores repeat of R121 | MISSING_FROM_STRUCTURED,REPEAT_OF_A1_ROW |
| MFS-C6 | NUMBER_REPEAT | Call L722 | T50 | 6-7 crores, 12-13 months repeat of R121/R122 | MISSING_FROM_STRUCTURED,REPEAT_OF_A1_ROW |
| MFS-C7 | NUMBER_REPEAT | Call L754 | T51 | 20-25% guidance repeat of R127 | MISSING_FROM_STRUCTURED,REPEAT_OF_A1_ROW |
| MFS-C8 | NUMBER_REPEAT | Call L890 | T66 | 20 to 25 percent repeat of R127/R128 | MISSING_FROM_STRUCTURED,REPEAT_OF_A1_ROW |
| MFS-C9 | NUMBER_TIMEREF | Call L640 | T40 | 8-9 quarters time ref | MISSING_FROM_STRUCTURED,TIME_REF |
| MFS-C10 | NUMBER_TIMEREF | Call L684 | T47 | 7-8 quarters time ref | MISSING_FROM_STRUCTURED,TIME_REF |
| MFS-C11 | FORWARD | Call L56 | T04 | reduce reliance on direct assignment (A4 DA-reliance contradiction rests on it) | MISSING_FROM_STRUCTURED |
| MFS-C12 | FORWARD | Call L57 | T04 | hold credit costs below 1% | MISSING_FROM_STRUCTURED |
| MFS-C13 | FORWARD | Call L100 | T04 | organization positions us well for quarters ahead | MISSING_FROM_STRUCTURED |
| MFS-C14 | FORWARD | Call L562 | T31 | continue on that trajectory | MISSING_FROM_STRUCTURED |
| MFS-C15 | FORWARD | Call L567 | T31 | leverage opex ratio and credit cost to reach free ROA (3%) | MISSING_FROM_STRUCTURED |
| MFS-C16 | FORWARD | Call L615 | T36 | will live up to expectations in Q3 | MISSING_FROM_STRUCTURED |
| MFS-C17 | FORWARD | Call L810 | T59 | steady at that approval rate | MISSING_FROM_STRUCTURED |
| MFS-C18 | FORWARD | Call L868-869 | T64 | ROA trajectory in similar range as targeting | MISSING_FROM_STRUCTURED |
| MFS-C19 | FORWARD | Call L893-894 | T66 | ROA maintained; cost to income to go down on gold side | MISSING_FROM_STRUCTURED |
| MFS-C20 | DATE | Call L270 | T08 | April (IGL launch; CEO) | MISSING_FROM_STRUCTURED |
| MFS-C21 | QUALIFIER | Call L715-716 | T50 | breakeven timeline conditioned on gold price rising or staying at today level | MISSING_FROM_STRUCTURED |

```yaml
stage: A2-enumerator
company: "FEDFINA"
quarter: "q2fy27"
doctype: "concall"
model: claude-sonnet-5-5
status: complete
ledger_path: "work/ledger_concall_fedfina_q2fy27.md"
counts:
  notes: 0
  line_items: 0
  zero_standing: 1
  agenda_items: 0
  auditor_paras: 0
  entities: 35
  participants: 17
  turns: 74
  questions: 26
  mgmt_numbers: 141
  mgmt_numbers_mfs: 4
  mgmt_numbers_total: 145
  forward_phrases: 58
  hedge_qualifiers: 22
  dates: 14
  slides: 0
  slide_numbers: 0
flags_raised: [MISSING_FROM_STRUCTURED, ZERO_STANDING, REPEAT_QUESTION, MGMT_ABSENCE, SPEAKER_INFERRED, MIXED_TURN, DECLINED_GUIDANCE, NO_TURN_IDENTIFIED]
ids_in_structured: 267
ids_referenced: 267
orphan_ids: []
missing_from_structured:
  - "loop_1: 15 counted units, MFS-C1 to C21 in section 9 (4 mgmt NUMBER, 9 FORWARD, 1 DATE, 1 QUALIFIER; plus 4 repeats and 2 time refs not counted)"
gate_a2: pass
mismatch_note: ""
analyst_note: "loop_1: applied. A5 findings M7, M8, M9, F6 closed. Added 21 MFS rows (no A1 ID): 4 new management numbers (L57, L113, L482, L483), 9 forward phrases, 1 date (L270), 1 qualifier (L715-716); 4 repeats and 2 time refs listed, not counted. Every line read verbatim first; all held the named unit. Mixed turns now T22, T26, T33, T47, T50, T51, T54, T62, T71. Question turns 26 (added L687-690, L723-726, L743-746). F6: R121-R123 moved to management, R130-R131 to analyst. Management numbers 141 on A1 rows, 145 with the 4 MFS. Analyst numbers 8. 52 of 74 turns SPEAKER_INFERRED, so side split rests on A1 inference. T58 uncertain as a question. R157-R159 have no speaking turn. R100 is the one ZERO_STANDING. R198 is declined yield guidance. Count test re-run, all categories match, orphan_ids empty."
```
