# A2 LEDGER: UNIMECH concall q2fy27 (ASR transcript, management tier, unverified)

=== A2 COUNT TEST ===
category: number_rows     grep_count: 101   sweep_count: 101   match: yes
category: entity_rows     grep_count: 34   sweep_count: 34   match: yes
category: forward_rows    grep_count: 75   sweep_count: 75   match: yes
category: date_rows       grep_count: 23   sweep_count: 23   match: yes
category: qualifier_rows  grep_count: 24   sweep_count: 24   match: yes
category: turns           A1_header: 65   sweep_count: 65   match: yes
category: total_ids       A1_header: 257   sweep_count: 257   match: yes
category: questions       sweep_count: 25 (manual from A1 turn table; loop 1 added Q25/T57)
category: rows_with_line_0   count: 0   (must be 0)
gate_a2: pass
=== END COUNT TEST ===

ids_in_structured: 257 | ids_referenced_in_ledger: 257 | orphan_ids: [] | match: yes

Row format: ROW_ID | fulltext line | turn | category | A2 flags | note. Values live in the A1 structured file at the ID. Fulltext line = src + 19. HDR = before T01 (fulltext lines <22).

## 1 PARTICIPANTS (ENTITY rows, people and hosts)
R103 | line 23 | T01 | participant | - | conference host (Anand Rathi) ASR-misspelled
R104 | line 31 | T02 | participant | - | host/moderator
R105 | line 34 | T02 | participant | - | Chairman and Managing Director
R106 | line 35 | T02 | participant | - | Whole-time Director and CFO
R110 | line 36 | T02 | participant | - | AGM Investor Relations
R124 | line 397 | T07 | participant | - | analyst
R126 | line 439 | T11 | participant | - | analyst
R127 | line 514 | T22 | participant | - | analyst
R129 | line 550 | T30 | participant | - | analyst
R130 | line 635 | T37 | participant | - | analyst
R131 | line 683 | T41 | participant | - | analyst
R135 | line 791 | T57 | participant | - | analyst, firm unnamed
MGMT_ABSENCE: none. CMD Anil Kumar Putnam (R105) speaks T03; WTD and CFO speak T04 and T05. Q&A answers T08-T62 are UNIDENTIFIED management in the source (speaker names not marked); no answer is attributable to a named executive.

## 2 SPEAKER TURNS (T01-T65, from A1 turn table)
T01 | fulltext 22-30 | ts 00:00:00-00:00:44 | Moderator/Operator (UNIDENTIFIED) | opening, disclaimer
T02 | fulltext 31-37 | ts 00:00:50-00:01:30 | Manish Valetia (host, Anand Rathi) with operator hand-off | introductions
T03 | fulltext 38-125 | ts 00:01:35-00:08:10 | Anil Kumar Putnam (CMD) | opening remarks (named at line 15, 18, 103)
T04 | fulltext 126-290 | ts 00:08:13-00:18:28 | Rajnekant Valaraman ("Rajni", WTD) | operational update (hand-off line 103-106, 270)
T05 | fulltext 291-383 | ts 00:18:34-00:24:19 | Ram Krishna Kamosala (CFO, "Ram") | financial update (hand-off line 270-271)
T06 | fulltext 384-396 | ts 00:24:21-00:24:50 | Operator | Q&A opening
T07 | fulltext 397-406 | ts 00:25:00-00:25:24 | Nanoshri Nivasa Reddy (Yellow Investments) | Q1 semiconductor share, LTA
T08 | fulltext 407-425 | ts 00:25:30-00:26:23 | UNIDENTIFIED management | answer (addressed 'Mr. Srinivas')
T09 | fulltext 426-430 | ts 00:26:28-00:26:37 | Nanoshri Nivasa Reddy (Yellow Investments) | Q1 follow-up, organisation strengthening
T10 | fulltext 431-438 | ts 00:27:00-00:27:25 | UNIDENTIFIED management | answer, senior hiring/incentives
T11 | fulltext 439-440 | ts 00:27:26-00:27:32 | Operator | next question Abhijit Singh
T12 | fulltext 441-443 | ts 00:27:49-00:28:02 | Abhijit Singh (Systematic) | Q 589 crore LTA/award letters
T13 | fulltext 444-475 | ts 00:28:06-00:29:32 | UNIDENTIFIED management | answer, FACC/Honeywell/French tier one
T14 | fulltext 476-479 | ts 00:29:39-00:29:49 | Abhijit Singh (Systematic) | qualify prototype first?
T15 | fulltext 480-489 | ts 00:29:50-00:30:38 | UNIDENTIFIED management | answer
T16 | fulltext 490-497 | ts 00:30:39-00:31:04 | Abhijit Singh (Systematic) | Q semiconductor business
T17 | fulltext 498-501 | ts 00:31:09-00:31:21 | UNIDENTIFIED management | answer, machining components, assemblies
T18 | fulltext 502-503 | ts 00:31:26-00:31:34 | Abhijit Singh (Systematic) | Q fundamentally different from aero?
T19 | fulltext 504-506 | ts 00:31:39-00:31:51 | UNIDENTIFIED management | answer
T20 | fulltext 507-509 | ts 00:31:57-00:32:07 | Abhijit Singh (Systematic) | Q customers count, H2 ramp
T21 | fulltext 510-511 | ts 00:32:08-00:32:19 | UNIDENTIFIED management | answer
T22 | fulltext 512-514 | ts 00:32:24-00:32:31 | Operator | thanks; next question Pajinkya Jado
T23 | fulltext 515-520 | ts 00:32:35-00:32:56 | Pajinkya Jado (CRIS PMS) | Q Honeywell components, margin
T24 | fulltext 521-533 | ts 00:33:02-00:33:48 | UNIDENTIFIED management | answer, NDA, consolidated reporting, margins vs tooling
T25 | fulltext 534-536 | ts 00:33:55-00:34:08 | Pajinkya Jado (CRIS PMS) | Q actuator?
T26 | fulltext 537-537 | ts 00:34:15-00:34:15 | UNIDENTIFIED management | answer, engine and APU
T27 | fulltext 538-538 | ts 00:34:23-00:34:23 | Pajinkya Jado (CRIS PMS) | Q French client
T28 | fulltext 539-542 | ts 00:34:31-00:35:02 | UNIDENTIFIED management | answer, door manufacturer, platforms
T29 | fulltext 543-549 | ts 00:35:07-00:35:17 | Pajinkya Jado / Operator | thanks; operator hand-off
T30 | fulltext 550-562 | ts 00:35:21-00:36:20 | Lana Tarveer Kual (Serena Alpha) | Q capacity and FY28 growth
T31 | fulltext 563-594 | ts 00:36:26-00:38:11 | UNIDENTIFIED management | answer, capacity, Saudi capex, two years
T32 | fulltext 595-598 | ts 00:38:15-00:38:32 | Lana Tarveer Kual (Serena Alpha) | Q peak revenue with existing infra
T33 | fulltext 599-604 | ts 00:38:38-00:39:08 | UNIDENTIFIED management | answer, 1000 crore aspiration, gross block
T34 | fulltext 605-615 | ts 00:39:09-00:39:40 | Lana Tarveer Kual (Serena Alpha) | acknowledgement; Q semiconductor competition
T35 | fulltext 616-626 | ts 00:39:42-00:40:41 | UNIDENTIFIED management | answer, scale not competition
T36 | fulltext 627-634 | ts 00:40:47-00:40:58 | Lana Tarveer Kual / Operator | thanks; operator hand-off
T37 | fulltext 635-641 | ts 00:41:02-00:41:39 | Fajal Kapoor (anti-Fazal) | Q fungible capacity
T38 | fulltext 642-650 | ts 00:41:42-00:42:13 | UNIDENTIFIED management | answer
T39 | fulltext 651-663 | ts 00:42:21-00:43:19 | Fajal Kapoor (anti-Fazal) | Q opportunities turned down
T40 | fulltext 664-677 | ts 00:43:23-00:44:16 | UNIDENTIFIED management | answer
T41 | fulltext 678-684 | ts 00:44:17-00:44:46 | Fajal Kapoor / Operator | thanks; operator next Angur Gaurati
T42 | fulltext 685-688 | ts 00:44:56-00:45:06 | Angur Gaurati (Genuity Capital) | Q H1 margins into H2, FY28/29 base
T43 | fulltext 689-698 | ts 00:45:16-00:45:48 | UNIDENTIFIED management | answer
T44 | fulltext 699-703 | ts 00:45:49-00:46:05 | Angur Gaurati (Genuity Capital) | Q Deia design approved
T45 | fulltext 704-713 | ts 00:46:08-00:46:49 | UNIDENTIFIED management / Angur | clarification exchange
T46 | fulltext 714-720 | ts 00:46:52-00:47:07 | UNIDENTIFIED management | answer, ongoing talks
T47 | fulltext 721-721 | ts 00:47:14-00:47:14 | Angur Gaurati (Genuity Capital) | Q revenue F28 or F29
T48 | fulltext 722-723 | ts 00:47:19-00:47:25 | UNIDENTIFIED management | answer
T49 | fulltext 724-726 | ts 00:47:32-00:47:43 | Angur Gaurati (Genuity Capital) | Q nuclear
T50 | fulltext 727-745 | ts 00:47:53-00:48:53 | UNIDENTIFIED management | answer, four reactors, qualified sub-assemblies
T51 | fulltext 746-748 | ts 00:48:58-00:49:02 | Angur Gaurati (Genuity Capital) | Q Hobel cross-selling
T52 | fulltext 749-762 | ts 00:49:04-00:50:18 | UNIDENTIFIED management | answer
T53 | fulltext 763-764 | ts 00:50:19-00:50:25 | Angur Gaurati (Genuity Capital) | Q Hobel revenue synergy
T54 | fulltext 765-766 | ts 00:50:31-00:50:43 | UNIDENTIFIED management | answer, 1000 crore vision 20%
T55 | fulltext 767-769 | ts 00:50:48-00:51:01 | Angur Gaurati (Genuity Capital) | Q fundraise use
T56 | fulltext 770-790 | ts 00:51:09-00:52:34 | UNIDENTIFIED management | answer, capacity and inorganic
T57 | fulltext 791-793 | ts 00:52:43-00:53:01 | Operator / Gaurav (firm UNIDENTIFIED) | next question
T58 | fulltext 794-800 | ts 00:53:06-00:53:53 | UNIDENTIFIED management | answer, 250 parts, serial production
T59 | fulltext 801-804 | ts 00:54:03-00:54:28 | Gaurav (firm UNIDENTIFIED) | Q UK/EU FTA
T60 | fulltext 805-808 | ts 00:54:33-00:54:58 | UNIDENTIFIED management / Operator | defer offline; follow-up answer duties
T61 | fulltext 809-819 | ts 00:55:03-00:55:58 | Operator / Serena Alpha ("Syrian Alpha") follow-up | Q product mix, margins at 1000 crore (src 799 reads 2000 CR)
T62 | fulltext 820-832 | ts 00:56:05-00:57:21 | UNIDENTIFIED management | answer, mix 50:50, margin
T63 | fulltext 833-836 | ts 00:57:26-00:57:38 | Analyst (UNIDENTIFIED) / Operator | thanks; last question; hand to management
T64 | fulltext 837-843 | ts 00:57:42-00:58:17 | UNIDENTIFIED management | closing comments
T65 | fulltext 844-847 | ts 00:58:25-00:58:37 | Operator and management | close
Turn mix: prepared remarks T01-T06 = 375 fulltext lines; Q&A T07-T65 = 451 lines (54% of turn lines).

## 3 QUESTION LEDGER (analyst, firm, topic, turn)
Q# | turn | analyst | firm | topic | flags
Q01 | T07 | Nanoshri Nivasa Reddy | Yellow Investments | Q1 semiconductor share, LTA | -
Q02 | T09 | Nanoshri Nivasa Reddy | Yellow Investments | follow-up, organisation strengthening | -
Q03 | T12 | Abhijit Singh | Systematic | 589 crore LTA/award letters | -
Q04 | T14 | Abhijit Singh | Systematic | qualify prototype first? | -
Q05 | T16 | Abhijit Singh | Systematic | semiconductor business | -
Q06 | T18 | Abhijit Singh | Systematic | semi fundamentally different from aero? | -
Q07 | T20 | Abhijit Singh | Systematic | customers count, H2 ramp | -
Q08 | T23 | Pajinkya Jado | CRIS PMS | Honeywell components, margin | -
Q09 | T25 | Pajinkya Jado | CRIS PMS | actuator? | -
Q10 | T27 | Pajinkya Jado | CRIS PMS | French client | -
Q11 | T30 | Lana Tarveer Kual | Serena Alpha | capacity and FY28 growth | topic overlap T37
Q12 | T32 | Lana Tarveer Kual | Serena Alpha | peak revenue with existing infra | topic overlap T61 (1000 cr)
Q13 | T34 | Lana Tarveer Kual | Serena Alpha | semiconductor competition | -
Q14 | T37 | Fajal Kapoor | anti-Fazal (as heard) | fungible capacity | REPEAT_QUESTION (T30)
Q15 | T39 | Fajal Kapoor | anti-Fazal (as heard) | opportunities turned down | -
Q16 | T42 | Angur Gaurati | Genuity Capital | H1 margins into H2, FY28/29 base | -
Q17 | T44 | Angur Gaurati | Genuity Capital | Deia design approved | -
Q18 | T47 | Angur Gaurati | Genuity Capital | revenue F28 or F29 | REPEAT_QUESTION (T42 FY28/29 base)
Q19 | T49 | Angur Gaurati | Genuity Capital | nuclear | -
Q20 | T51 | Angur Gaurati | Genuity Capital | Hobel cross-selling | -
Q21 | T53 | Angur Gaurati | Genuity Capital | Hobel revenue synergy | REPEAT_QUESTION (T51)
Q22 | T55 | Angur Gaurati | Genuity Capital | fundraise use | -
Q23 | T59 | Gaurav | firm UNIDENTIFIED | UK/EU FTA | -
Q24 | T61 | Serena Alpha follow-up (as heard) | Serena Alpha | product mix, margins at 1000 crore | REPEAT_QUESTION (T32/T33 1000 cr aspiration)
Q25 | T57 | Gaurav | firm UNIDENTIFIED | serial-production count and quarterly run-rate of the 250 qualified parts (fulltext l.792-794; added loop 1, out of turn order) | -
Note: T63 is an unidentified analyst saying last question and handing to management; A1 gives no topic; not counted. T45 is a clarification exchange; not counted. 7 identified analysts (Nanoshri, Abhijit, Pajinkya, Lana, Fajal, Angur, Gaurav) plus the Serena Alpha follow-up at T61; 25 question turns (Gaurav now 2: T57, T59).

## 4 NUMBERS (NUMBER rows)
R001 | line 20 | HDR | header_meta | - | call recording duration
R083 | line 558 | T30 | analyst_number | - | blended utilization by end FY27 (analyst assumption)
R088 | line 605 | T34 | analyst_number | MISHEARING_CANDIDATE | analyst "2x add a term", garbled
R096 | line 818 | T61 | analyst_number | MISHEARING_CANDIDATE | revenue mark in analyst question
R002 | line 44 | T03 | mgmt_number | - | H1 FY27 consolidated revenue YoY growth
R003 | line 44 | T03 | mgmt_number | - | H1 FY27 consolidated revenue
R004 | line 45 | T03 | mgmt_number | - | H1 FY27 EBITDA margin ("Evita")
R005 | line 58 | T03 | mgmt_number | - | consolidated order book as of Sep 30
R006 | line 59 | T03 | mgmt_number | MISHEARING_CANDIDATE | order book YoY increase, garbled
R007 | line 62 | T03 | mgmt_number | - | core pillars of strategy
R008 | line 82 | T03 | mgmt_number | MISHEARING_CANDIDATE | semiconductor development effort duration
R009 | line 87 | T03 | mgmt_number | - | qualified across PCA customer base as of H1 end
R010 | line 88 | T03 | mgmt_number | MISHEARING_CANDIDATE | parts in qualification pipeline, garbled
R011 | line 97 | T03 | mgmt_number | MISHEARING_CANDIDATE | initial equity investment Saudi JV
R012 | line 155 | T04 | mgmt_number | MISHEARING_CANDIDATE | FACC LTA value
R013 | line 155 | T04 | mgmt_number | - | FACC LTA tenure
R014 | line 163 | T04 | mgmt_number | - | French tier 1 program award value
R015 | line 163 | T04 | mgmt_number | - | French tier 1 program award spread
R016 | line 165 | T04 | mgmt_number | - | Honeywell Aerospace LTA tenure
R017 | line 166 | T04 | mgmt_number | - | Honeywell LTA extension
R018 | line 169 | T04 | mgmt_number | MISHEARING_CANDIDATE | targeted qualification in full year FY27
R019 | line 177 | T04 | mgmt_number | MISHEARING_CANDIDATE | semiconductor investment duration
R020 | line 180 | T04 | mgmt_number | - | semiconductor first article inspections qualified
R021 | line 186 | T04 | mgmt_number | - | semiconductor components/assemblies targeted by end of calen
R022 | line 227 | T04 | mgmt_number | - | initial equity investment Saudi JV
R023 | line 235 | T04 | mgmt_number | - | Unimech equity stake in Deia Engineering
R024 | line 240 | T04 | mgmt_number | - | Deia valuation at Avana Capital investment
R025 | line 243 | T04 | mgmt_number | - | thrust engine in advanced development
R026 | line 248 | T04 | mgmt_number | - | Deia engine variant thrust
R027 | line 248 | T04 | mgmt_number | - | Deia engine variant thrust
R028 | line 248 | T04 | mgmt_number | - | Deia engine variant thrust
R029 | line 248 | T04 | mgmt_number | - | Deia engine variant thrust
R030 | line 273 | T04 | mgmt_number | RESTATED | xref R101; qualified parts expected by end of year
R031 | line 275 | T04 | mgmt_number | - | qualified base
R032 | line 275 | T04 | mgmt_number | - | parts currently in pipeline
R033 | line 276 | T04 | mgmt_number | - | qualified parts by close of FY27
R034 | line 281 | T04 | mgmt_number | - | consolidated order book
R035 | line 282 | T04 | mgmt_number | MISHEARING_CANDIDATE | order book increase, garbled
R036 | line 301 | T05 | mgmt_number | - | Q2 FY27 consolidated revenue
R037 | line 301 | T05 | mgmt_number | - | Q2 revenue sequential growth
R038 | line 302 | T05 | mgmt_number | - | Q2 revenue YoY growth
R039 | line 308 | T05 | mgmt_number | - | H1 FY27 consolidated revenue
R040 | line 308 | T05 | mgmt_number | - | H1 revenue YoY growth
R041 | line 310 | T05 | mgmt_number | MISHEARING_CANDIDATE | H1 revenue as share of full year FY26 revenue
R042 | line 312 | T05 | mgmt_number | - | aero tooling share of H1 revenue
R043 | line 313 | T05 | mgmt_number | - | PCA business share of H1 revenue
R044 | line 315 | T05 | mgmt_number | MISHEARING_CANDIDATE | COBEL contribution to H1 consolidated revenue
R045 | line 320 | T05 | mgmt_number | - | other income Q2 FY27, approx
R046 | line 321 | T05 | mgmt_number | - | other income H1 FY27, approx
R047 | line 324 | T05 | mgmt_number | - | consolidated gross margin H1
R048 | line 324 | T05 | mgmt_number | - | Q2 gross margin
R049 | line 325 | T05 | mgmt_number | MISHEARING_CANDIDATE | cost percentage of revenue, garbled
R050 | line 326 | T05 | mgmt_number | - | Q2 EBITDA margin ("Hebeda")
R051 | line 326 | T05 | mgmt_number | MISHEARING_CANDIDATE | H1 EBITDA margin, garbled
R052 | line 329 | T05 | mgmt_number | MISHEARING_CANDIDATE | H1 employee cost as % of revenue, garbled ("15% working perc
R053 | line 330 | T05 | mgmt_number | - | total employees
R054 | line 332 | T05 | mgmt_number | - | Q2 FY27 PAT, approx
R055 | line 332 | T05 | mgmt_number | - | Q2 PAT margin
R056 | line 333 | T05 | mgmt_number | - | Q2 PAT sequential growth over Q1 FY27
R057 | line 333 | T05 | mgmt_number | - | Q2 PAT YoY growth vs Q2 FY26
R058 | line 335 | T05 | mgmt_number | - | H1 FY27 PAT
R059 | line 335 | T05 | mgmt_number | - | H1 PAT YoY growth
R060 | line 337 | T05 | mgmt_number | - | H1 PAT as share of FY26 PAT
R061 | line 340 | T05 | mgmt_number | - | annualized H1 ROCE ("ROC"), approx
R062 | line 340 | T05 | mgmt_number | - | annualized H1 ROE, approx
R063 | line 349 | T05 | mgmt_number | - | working capital days expected by end FY27
R064 | line 352 | T05 | mgmt_number | - | manufacturing utilization, approx
R065 | line 353 | T05 | mgmt_number | MISHEARING_CANDIDATE | capacity share dedicated to development, garbled
R066 | line 411 | T08 | mgmt_number | - | PCA share of revenues
R067 | line 412 | T08 | mgmt_number | MISHEARING_CANDIDATE | semiconductor share within PCA, "primarily 3%"
R068 | line 441 | T12 | mgmt_number | MISHEARING_CANDIDATE | long-term wins/LTA and award letters
R069 | line 444 | T13 | mgmt_number | - | long-term wins number
R070 | line 448 | T13 | mgmt_number | - | entities under long-term wins
R071 | line 450 | T13 | mgmt_number | - | FACC contract tenure
R072 | line 455 | T13 | mgmt_number | - | FACC contract value
R073 | line 460 | T13 | mgmt_number | - | Honeywell contract
R074 | line 461 | T13 | mgmt_number | - | Honeywell extendable
R075 | line 468 | T13 | mgmt_number | - | French aerospace tier one indication
R076 | line 469 | T13 | mgmt_number | - | French tier one visibility
R077 | line 474 | T13 | mgmt_number | - | visibility figure ("589-floor")
R078 | line 475 | T13 | mgmt_number | - | span of 589 visibility
R079 | line 483 | T15 | mgmt_number | - | qualified semiconductor parts moving to revenue
R080 | line 510 | T21 | mgmt_number | - | established semiconductor customer
R081 | line 510 | T21 | mgmt_number | - | semiconductor customers in pipeline
R082 | line 511 | T21 | mgmt_number | - | aerospace customers
R084 | line 565 | T31 | mgmt_number | MISHEARING_CANDIDATE | available capacity multiple, garbled ("available hospitals")
R085 | line 574 | T31 | mgmt_number | - | Saudi JV capex outlay
R086 | line 601 | T33 | mgmt_number | - | revenue aspiration
R087 | line 603 | T33 | mgmt_number | - | gross block by end of this financial year incl JV
R089 | line 727 | T50 | mgmt_number | - | new nuclear reactors in bidding stage
R090 | line 737 | T50 | mgmt_number | - | nuclear sub-assemblies and systems qualified
R091 | line 752 | T52 | mgmt_number | - | time since Hobel acquisition
R092 | line 765 | T54 | mgmt_number | - | vision incl Hobel
R093 | line 765 | T54 | mgmt_number | - | Hobel contribution to total vision
R094 | line 781 | T56 | mgmt_number | - | capacity addition to production time
R095 | line 797 | T58 | mgmt_number | - | of qualified 250 moving to serial production
R097 | line 824 | T62 | mgmt_number | - | revenue mark
R098 | line 825 | T62 | mgmt_number | - | mix of tooling and precision components at 1000 CR
R099 | line 829 | T62 | mgmt_number | - | margin compression for R and D
R100 | line 839 | T64 | mgmt_number | - | order book (closing)
R101 | line 840 | T64 | mgmt_number | RESTATED | xref R030; qualified parts by year end (closing)
Counts: mgmt_number 97 | analyst_number 3 | header_meta 1 | total 101

## 5 FORWARD-COMMITMENT AND HEDGE PHRASES (FORWARD rows; A1 does not split hedge vs commitment, A3 applies lexicons)
R136 | line 39 | T03 | forward_commitment | - | Strategy: transform into integrated multi-industry precision engineeri
R137 | line 67 | T03 | forward_commitment | - | Expanding into high visibility contracts
R138 | line 69 | T03 | forward_commitment | - | Negotiating long-term supply agreements with existing customers for hi
R139 | line 71 | T03 | forward_commitment | - | Convert opportunities to layer multi-year revenue on short cycle PO bu
R140 | line 83 | T03 | forward_commitment | - | Semiconductor revenue step-up expected in H2
R141 | line 91 | T03 | forward_commitment | - | Qualified parts to move to serial production giving multi-year visibil
R142 | line 94 | T03 | forward_commitment | - | Actively preparing to bid on upcoming nuclear opportunities
R143 | line 98 | T03 | forward_commitment | - | Saudi JV funds infrastructure readiness for regional localization dema
R144 | line 106 | T03 | forward_commitment | - | Special process cells trial runs this month, submission by December
R145 | line 107 | T03 | forward_commitment | - | NACAF certification targeted for March 27
R146 | line 144 | T04 | forward_commitment | - | Possible tooling opportunities beyond aerospace if Dutch OEM account s
R147 | line 147 | T04 | forward_commitment | - | Second phase opportunity: high-volume precision parts for the OEM
R148 | line 160 | T04 | forward_commitment | - | FACC contract tenure can potentially double
R149 | line 169 | T04 | forward_commitment | - | Targeting qualification of over 320 parts in FY27
R150 | line 173 | T04 | forward_commitment | - | Revenue ramp layers into FY28 and beyond
R151 | line 175 | T04 | forward_commitment | - | Possibility of exponential scale in semiconductors
R152 | line 186 | T04 | forward_commitment | - | Another 20 parts targeted by end of calendar year
R153 | line 188 | T04 | forward_commitment | - | Discussions with another global semiconductor OEM underway
R154 | line 204 | T04 | forward_commitment | - | Augmenting shop floor, clean room and machining capacity ahead of dema
R155 | line 211 | T04 | forward_commitment | - | Hobel demand bullish for coming year
R156 | line 213 | T04 | forward_commitment | - | Absorbing additional capacity requests with available infrastructure
R157 | line 216 | T04 | forward_commitment | - | Engagements with new clients for turbine switchgear, locomotive exhaus
R158 | line 222 | T04 | forward_commitment | - | AS9100 certification targeted by Ceph27
R159 | line 224 | T04 | forward_commitment | - | Evaluating timing of new capex expansion
R160 | line 229 | T04 | forward_commitment | - | Saudi facility commercial manufacturing readiness March or April 27
R161 | line 231 | T04 | forward_commitment | - | Immediate production ramp-up once Saudi infrastructure operational
R162 | line 232 | T04 | forward_commitment | - | Overflow demand to be fulfilled by Indian manufacturing base
R163 | line 248 | T04 | forward_commitment | - | Deia four thrust variants available by March 27
R164 | line 252 | T04 | forward_commitment | - | ECU development in parallel across variants
R165 | line 262 | T04 | forward_commitment | - | Critical design review before December 26
R166 | line 265 | T04 | forward_commitment | - | Final design approval certification by FEP-27
R167 | line 273 | T04 | forward_commitment | - | Expect to exceed 590 qualified parts by end of year
R168 | line 276 | T04 | forward_commitment | - | More than 590 qualified parts by close of FY27
R169 | line 280 | T04 | forward_commitment | - | Recurring revenue starting next year
R170 | line 306 | T05 | forward_commitment | - | Confident of stronger revenue in forthcoming quarters
R171 | line 318 | T05 | forward_commitment | - | PCA highest share of growth and revenue contribution expected in comin
R172 | line 330 | T05 | forward_commitment | - | Current margin range sustainable going forward for this year
R173 | line 349 | T05 | forward_commitment | - | Working capital days to move to 150 to 160 days by end FY27
R174 | line 358 | T05 | forward_commitment | - | Capacity expansion to be initiated if needed
R175 | line 366 | T05 | forward_commitment | - | Equity fund raise expected to be considered in early calendar year
R176 | line 370 | T05 | forward_commitment | - | Fund raise to help achieve minimum public shareholding
R177 | line 415 | T08 | forward_commitment | - | Expecting better semiconductor numbers
R178 | line 417 | T08 | forward_commitment | - | More qualifications to lead to long-term supply agreement in semicondu
R179 | line 425 | T08 | forward_commitment | - | Semiconductor expected to be a significant contributor
R180 | line 486 | T15 | forward_commitment | - | Forecast schedules supported by POs to form revenues from next year on
R181 | line 488 | T15 | forward_commitment | - | Fairly confident all parts will be qualified
R182 | line 541 | T28 | forward_commitment | - | Qualification on platforms gives snowballing effect with other tier on
R183 | line 573 | T31 | forward_commitment | - | Special process cell commissioning
R184 | line 574 | T31 | forward_commitment | - | Saudi JV capex of 200 to 250 crore outlay
R185 | line 580 | T31 | forward_commitment | - | Sufficient capacity for next two years
R186 | line 588 | T31 | forward_commitment | - | Contemplating timing of newer capacity
R187 | line 592 | T31 | forward_commitment | - | Might have to do early investment; will indicate once plans finalised
R188 | line 601 | T33 | forward_commitment | - | Aspiration of 1000 crore revenue
R189 | line 603 | T33 | forward_commitment | - | Gross block roughly 500 crores by end of this financial year
R190 | line 626 | T35 | forward_commitment | - | Upward ramp cycle for the semiconductor industry
R191 | line 689 | T43 | forward_commitment | - | Margins confident to sustain in H2 at H1 level
R192 | line 697 | T43 | forward_commitment | - | Margin guidance one year at a time; FY28/FY29 base not guided
R193 | line 721 | T47 | forward_commitment | - | Deia revenue F28 or F29
R194 | line 727 | T50 | forward_commitment | - | Participation in four new nuclear reactor bids through VGS
R195 | line 744 | T50 | forward_commitment | - | Confident to participate in upcoming bids
R196 | line 765 | T54 | forward_commitment | - | Hobel approx 20% of 1000 crore vision
R197 | line 769 | T55 | forward_commitment | - | Capacity infra for 1000 crore vision mostly complete by this year
R198 | line 772 | T56 | forward_commitment | - | 1000 crore vision needs no external money, internal accruals sufficien
R199 | line 777 | T56 | forward_commitment | - | Further capacity addition needed beyond 1000 crore
R200 | line 781 | T56 | forward_commitment | - | Capacity addition takes 18 to 24 months
R201 | line 789 | T56 | forward_commitment | - | Fundraise for capacity addition and potentially inorganic expansion
R202 | line 798 | T58 | forward_commitment | - | 60-70% of 250 parts to move into serial production
R203 | line 799 | T58 | forward_commitment | - | Compounding effect next year; this year a beginning
R204 | line 800 | T58 | forward_commitment | - | Next year is a qualification year
R205 | line 822 | T62 | forward_commitment | - | H2 margins same as H1
R206 | line 825 | T62 | forward_commitment | - | Mix around 50 50 at 1000 crore
R207 | line 827 | T62 | forward_commitment | - | Some margin compression but not large
R208 | line 829 | T62 | forward_commitment | - | 1 to 2 percent margin compression for R and D
R209 | line 840 | T64 | forward_commitment | - | 590 qualified parts coming online by year end
R210 | line 842 | T64 | forward_commitment | - | Committed to delivering disciplined high margin growth

## 6 OTHER ENTITIES (non-participant)
R102 | line 22 | T01 | entity | - | company
R107 | line 35 | T02 | entity | - | Whole-time Director
R108 | line 36 | T02 | entity | - | Whole-time Director
R109 | line 36 | T02 | entity | - | Whole-time Director
R111 | line 48 | T03 | entity | - | acquired entity; ASR variants Mobile Bellows, HOBLE, Hobl
R112 | line 95 | T03 | entity | - | Saudi JV partner (QANU line 209)
R113 | line 107 | T03 | entity | - | certification, garbled
R114 | line 141 | T04 | entity | - | prospective tooling account
R115 | line 155 | T04 | entity | - | aerospace LTA customer
R116 | line 162 | T04 | entity | - | aircraft door components customer
R117 | line 164 | T04 | entity | - | 10-year LTA customer
R118 | line 220 | T04 | entity | - | major exploring partnerships, garbled
R119 | line 223 | T04 | entity | - | quality certification
R120 | line 235 | T04 | entity | - | 27% associate, micro gas turbine
R121 | line 240 | T04 | entity | - | investor in Deia
R122 | line 259 | T04 | entity | - | certification authority, garbled
R123 | line 371 | T05 | entity | - | minimum public shareholding
R125 | line 432 | T10 | entity | - | senior leadership incentive, garbled
R128 | line 539 | T28 | entity | - | platforms for door components
R132 | line 723 | T48 | entity | - | product
R133 | line 729 | T50 | entity | - | nuclear bidders
R134 | line 754 | T52 | entity | - | existing customers visited Hobel
ENTITY_CHANGE: not assessable, no prior ledger.

## 7 DATES
R211 | line 20 | HDR | date | - | 2026-10-28 / production date of transcript header
R212 | line 22 | T01 | date | - | Q2 and FY27 / earnings call quarter
R213 | line 44 | T03 | date | - | H1 FY27 / period
R214 | line 57 | T03 | date | - | September 30th / order book date
R215 | line 83 | T03 | date | - | H2 / semiconductor step-up period
R216 | line 106 | T03 | date | - | December / special process submission completion
R217 | line 107 | T03 | date | - | March 27 / NACAF certification target
R218 | line 169 | T04 | date | - | FY27 / qualification target year
R219 | line 174 | T04 | date | - | FY28 / revenue ramp period
R220 | line 223 | T04 | date | - | Ceph27 / AS9100 completion target, garbled
R221 | line 229 | T04 | date | - | March or April 27 / Saudi facility readiness
R222 | line 239 | T04 | date | - | 26 September / Avana Capital investment in Deia
R223 | line 250 | T04 | date | - | March 27 / four Deia variants availability
R224 | line 263 | T04 | date | - | December 26th / critical design review target
R225 | line 265 | T04 | date | - | FEP-27 / final design approval target, garbled
R226 | line 277 | T04 | date | - | 527 / close of FY27, garbled
R227 | line 298 | T05 | date | - | Q2 is 527 / financial update period, garbled
R228 | line 350 | T05 | date | - | 5-27 / end of FY27, garbled
R229 | line 367 | T05 | date | - | early calendar year / equity fund raise timing
R230 | line 562 | T30 | date | - | FY28 / capacity question
R231 | line 705 | T45 | date | - | F28 or may be F29 / commercial engine production
R232 | line 708 | T45 | date | - | 2728 / series production, garbled
R233 | line 721 | T47 | date | - | F28 or maybe F29 / Deia revenue timing

## 8 QUALIFIERS
R234 | line 20 | HDR | qualifier | - | Machine transcript (ASR), faster-whisper small.en; management tier, un
R235 | line 20 | HDR | qualifier | - | Speaker names not marked in source; turns segmented from cues
R236 | line 24 | T01 | qualifier | - | Forward-looking statements disclaimer: not guarantees; involve risk an
R237 | line 57 | T03 | qualifier | - | Order book is consolidated, as of September 30
R238 | line 87 | T03 | qualifier | - | 250 qualified parts figure as of H1 end
R239 | line 160 | T04 | qualifier | - | FACC contract doubling is potential, tied to qualification and ongoing
R240 | line 283 | T04 | qualifier | - | Order book anchored by firm POs and multi-year LTAs and award letters
R241 | line 316 | T05 | qualifier | - | Excluding COBEL (Hobel?), PCA momentum just begun; COBEL 30% of H1 rev
R242 | line 320 | T05 | qualifier | - | Other income stated as approximate
R243 | line 339 | T05 | qualifier | - | ROCE and ROE are annualized H1 and approximate
R244 | line 352 | T05 | qualifier | - | 65% utilization includes capacity dedicated to new production, provos 
R245 | line 368 | T05 | qualifier | - | Equity fund raise subject to final requirement and market conditions
R246 | line 461 | T13 | qualifier | - | Honeywell 12-year extension is "extendable", not committed
R247 | line 469 | T13 | qualifier | - | French tier one 43 million is an indication of visibility, not a firm 
R248 | line 481 | T15 | qualifier | - | Qualification is a continued process before production
R249 | line 521 | T24 | qualifier | - | Honeywell component details restricted by NDA
R250 | line 528 | T24 | qualifier | - | Internal policy: margins reported only on consolidated basis, not by v
R251 | line 532 | T24 | qualifier | - | Directional: PCA margins equal to or less than tooling
R252 | line 599 | T33 | qualifier | - | Management not giving forward-looking guidance over next two years; 10
R253 | line 603 | T33 | qualifier | - | Gross block of ~500 crores includes all JV business
R254 | line 697 | T43 | qualifier | - | Margin visibility limited to one year at a time
R255 | line 765 | T54 | qualifier | - | 1000 crore vision includes ~20% from Hobel
R256 | line 794 | T58 | qualifier | - | Not all 250 qualified parts enter serial production; indication of val
R257 | line 829 | T62 | qualifier | - | Margin compression of 1-2% for R and D factored in

## 9 MISSING_FROM_STRUCTURED
none found. ZERO_STANDING: none (transcript has no line items).

## LOOP 1 CHANGE LOG
- Added Q25 | T57 | Gaurav (firm UNIDENTIFIED) | serial-production count and run-rate of 250 qualified parts | fulltext l.792-794 (confirmed read). Gap source: A5 audit, tag MISSING.
- Questions count 24 -> 25 (count-test line, Section 3 note, per-analyst tally: Gaurav 1 -> 2). Q# kept stable, no renumbering.
- Nothing else changed. Gate A2: pass (grep/fresh count 25 = sweep 25).
