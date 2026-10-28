# LEDGER presentation RAYMONDREL q2fy27 (A2 enumerator)

ids_in_structured: 1082 | ids_referenced_in_ledger: 1082 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: slides            grep_count: 46 ([page N] markers; pdfinfo 46)  sweep_count: 46 (43 slides carry rows; p18, p21, p25 are divider slides with no row)  match: yes
category: slide_numbers     grep_count: 860 (NUMBER rows; header says 860)  sweep_count: 860  match: yes
category: fulltext_numeric_sweep  tokens_in_fulltext: 1145  found_in_structured_same_page: 1101  not_found: 44  -> explained: 25 slide footer page numbers, 1 table serial no. (p26 l426), 1 statutory year (p45 l747 "Act, 2013"), 5 chart axis ticks (p6 l101-114), 6 pin/phone tokens (p1 l24,25,53), 6 text-layer marker fusions (p30 l514 garbled "~2135%%"; p33 l567 1580; p36 l615 1102; p39 l651 148; p41 l684 1728; p43 l721 1617). The five fused unit counts are covered by R840,R842,R843,R844,R846 (A1 resolved from render); the p30 garble sits beside R521 (~23% sold) and is not a separate disclosure. Net genuine miss: 1 (phone, see MISSING_FROM_STRUCTURED). match: yes (reconciled)
category: entities          grep_count: 98  sweep_count: 98  match: yes
category: forward_statements grep_count: 29  sweep_count: 29  match: yes
category: dates             grep_count: 49  sweep_count: 49  match: yes
category: footnotes_disclaimers grep_count: 46  sweep_count: 46  match: yes
category: zero_standing     grep_count: 47 ([ZERO_STANDING] tags)  sweep_count: 47 (untagged zero-valued NUMBER rows found: 0)  match: yes
category: total_ids         grep_count: 1082  sweep_count: 1082 (R001-R1082 contiguous, no gaps, no duplicates)  match: yes
gate_a2: pass
=== END COUNT TEST ===

## FLAGS RAISED
- ZERO_STANDING: 47 rows (all A1-tagged, all enumerated below)
- FOOTNOTE_UNRESOLVED: 9 rows (superscript marker 1 on Units Launched, footnote text not found by A1): R1067, R1068, R1069, R1070, R1071, R1072, R1073, R1074, R1075
- RESTATED: cross-refs in the ledger tables
- PAGE_ANCHOR_DEFECT: R840 and R1068 (page 32 stated, line 567 is on page 33)
- MISSING_FROM_STRUCTURED: 1 (below)
- DROPPED_SLIDE: not assessable (no prior ledger or deck supplied)
- ENTITY_CHANGE: not assessable (no prior list)
- MGMT_ABSENCE / REPEAT_QUESTION: not applicable to a deck

## MISSING_FROM_STRUCTURED
M1 | fulltext line 53 (page 1) | Tel.: +91 22 6837 3700 (company telephone in the CIN/contact line) | low materiality; contact data. Pin codes at lines 24-25 sit inside the R865 address block and are treated as grouped.

## SLIDE LEDGER (category: slides)
slide | title (fulltext first line) | content type | structured IDs on slide (count) | flags
1 | RAYMOND REALTY LIMITED | text | R001-R007,R861-R865,R988-R990,R1037 (16) | 
2 | Investor cover | text | R991 (1) | 
3 | Table of Contents | text | R008-R010 (3) | 
4 | Creating Legacy in Real Estate….. | chart | R011-R027,R866-R867,R959-R960,R992-R995,R1038 (26) | 
5 | GDV Breakup: Twin Engine Growth | table | R028-R048,R868,R1039-R1041 (25) | 
6 | Raymond Realty : Transitioned into an Asset light MMR platform | chart+text | R049-R064,R869-R870,R961-R962,R1042 (21) | ZERO_STANDING x2
7 | Brand Portfolio: Launched, Sold Unsold ₹ In Crs | chart | R065-R073,R871-R873 (12) | 
8 | GDV Cash Realization Profile ₹ in Crs | chart+table | R074-R092,R1043 (20) | 
9 | Strong Projected Cashflows from Planned Launches | chart+table | R093-R108,R963,R1044-R1045 (19) | ZERO_STANDING x1
10 | Going Forward Guidance FY27 | text | R109-R112,R964-R967,R996 (9) | 
11 | Capital Profile, End Use & Returns ₹ in Crs | chart+table | R113-R139,R874,R1046 (29) | 
12 | Strong Track Record ₹ in Crs | chart+table | R140-R171 (32) | 
13 | Management Team (image) | photo | R875 (1) | IMAGE_ONLY; content held only as R875
14 | Driving Growth Through Strong Governance & Independent Oversight | text+table | R172-R182,R876-R886,R1047-R1048 (24) | 
15 | Our Leadership Team | photo+text | R183-R188,R887-R892 (12) | 
16 | Our Leadership Team | photo+text | R189-R194,R893-R898 (12) | 
17 | ESG Performance | chart+table | R195-R207,R899-R901,R997-R998,R1049 (19) | 
18 | Section divider: Q2 & H1 FY27 | text | - (0) | NO_ROWS (divider/sparse page, logged by A1)
19 | Q2FY27 & H1FY27 Highlights | chart+table | R208-R224,R902,R1050-R1052 (21) | ZERO_STANDING x1
20 | Q2 & H1 FY27 Highlights EBITDA & MARGIN (%) ₹ in Crs | chart+table | R225-R252 (28) | 
21 | Section divider: Financials | text | - (0) | NO_ROWS (divider/sparse page, logged by A1)
22 | Financial Performance In ₹ Crs | table | R253-R318,R903,R1053-R1054 (69) | 
23 | Financial Position H1FY27 In ₹ Crs | table | R319-R332,R1055 (15) | 
24 | Cash Flow Position In ₹ Crs | chart+table | R333-R367,R1056-R1057 (37) | ZERO_STANDING x1
25 | Section divider: Project Details | text | - (0) | NO_ROWS (divider/sparse page, logged by A1)
26 | Ongoing Launched Projects Summary ₹ In Crs | table | R368-R481,R904-R917,R999-R1026,R1058-R1062 (161) | 
27 | Future Launch Pipeline Summary ₹ In Crs | table | R482-R498,R918-R922,R968-R972,R1027-R1036,R1063 (38) | 
28 | Own Land Portfolio ₹ in Crs | chart+table | R499-R512,R923-R933,R1064 (26) | 
29 | Aspirational: TenX Habitat | table+text | R513-R520,R934,R973-R974,R1066 (12) | 
30 | Aspirational: TenX District 9 | table+text | R521-R543,R839,R935,R975,R1067 (27) | ZERO_STANDING x5
31 | Aspirational: TenX Era | table+text | R544-R566,R936,R976 (25) | 
32 | Premium: The Address by GS, Season 1 | table+text | R567-R589,R840,R937,R977,R1068 (27) | ZERO_STANDING x3
33 | Premium: The Address by GS, Season 2 | table+text | R590-R612,R938,R978 (25) | 
34 | Premium: The Address by GS, Season 3 | table+text | R613-R635,R841,R939,R979,R1069 (27) | 
35 | Luxury: Invictus by GS – Tower A | table+text | R636-R658,R940,R980 (25) | ZERO_STANDING x1
36 | Luxury: Invictus by GS Tower B | table+text | R659-R681,R842,R941,R981,R1070 (27) | ZERO_STANDING x5
37 | High Street Retail: Park Avenue | table+text | R682-R704,R942,R982 (25) | ZERO_STANDING x1
38 | High Street Retail: Park Street | table+text | R705-R723,R943,R983,R1065 (22) | ZERO_STANDING x7
39 | High Street Retail: Raymond Retail | table+text | R724-R746,R843,R944,R1071 (26) | ZERO_STANDING x5
40 | JDA Portfolio ₹ in Crs | chart+table | R850-R860,R949-R956,R1077 (20) | 
41 | Premium: The Address by GS (Bandra) | table+text | R747-R769,R844,R945,R984,R1072 (27) | 
42 | Luxury: Invictus by GS (BKC) | table+text | R770-R792,R845,R848-R849,R946,R985,R1073,R1076 (30) | ZERO_STANDING x5
43 | Premium: The Address by GS (Wadala) | table+text | R793-R815,R846,R947,R986,R1074 (27) | ZERO_STANDING x5
44 | Premium: The Address by GS (Sion) | table+text | R816-R838,R847,R948,R987,R1075 (27) | ZERO_STANDING x5
45 | Disclaimer | text | R957,R1078-R1082 (6) | 
46 | Thank You | text | R958 (1) | 

## ZERO_STANDING LEDGER
ROW_ID | slide | category | flag
R050 | 6 | slide_number | ZERO_STANDING
R052 | 6 | slide_number | ZERO_STANDING
R098 | 9 | slide_number | ZERO_STANDING
R224 | 19 | slide_number | ZERO_STANDING
R355 | 24 | slide_number | ZERO_STANDING
R524 | 30 | slide_number | ZERO_STANDING
R528 | 30 | slide_number | ZERO_STANDING
R532 | 30 | slide_number | ZERO_STANDING
R536 | 30 | slide_number | ZERO_STANDING
R540 | 30 | slide_number | ZERO_STANDING
R570 | 32 | slide_number | ZERO_STANDING
R574 | 32 | slide_number | ZERO_STANDING
R578 | 32 | slide_number | ZERO_STANDING
R645 | 35 | slide_number | ZERO_STANDING
R664 | 36 | slide_number | ZERO_STANDING
R667 | 36 | slide_number | ZERO_STANDING
R668 | 36 | slide_number | ZERO_STANDING
R672 | 36 | slide_number | ZERO_STANDING
R678 | 36 | slide_number | ZERO_STANDING
R690 | 37 | slide_number | ZERO_STANDING
R708 | 38 | slide_number | ZERO_STANDING
R710 | 38 | slide_number | ZERO_STANDING
R712 | 38 | slide_number | ZERO_STANDING
R714 | 38 | slide_number | ZERO_STANDING
R716 | 38 | slide_number | ZERO_STANDING
R718 | 38 | slide_number | ZERO_STANDING
R720 | 38 | slide_number | ZERO_STANDING
R727 | 39 | slide_number | ZERO_STANDING
R731 | 39 | slide_number | ZERO_STANDING
R735 | 39 | slide_number | ZERO_STANDING
R739 | 39 | slide_number | ZERO_STANDING
R743 | 39 | slide_number | ZERO_STANDING
R773 | 42 | slide_number | ZERO_STANDING
R777 | 42 | slide_number | ZERO_STANDING
R778 | 42 | slide_number | ZERO_STANDING
R781 | 42 | slide_number | ZERO_STANDING
R785 | 42 | slide_number | ZERO_STANDING
R796 | 43 | slide_number | ZERO_STANDING
R800 | 43 | slide_number | ZERO_STANDING
R804 | 43 | slide_number | ZERO_STANDING
R808 | 43 | slide_number | ZERO_STANDING
R812 | 43 | slide_number | ZERO_STANDING
R819 | 44 | slide_number | ZERO_STANDING
R823 | 44 | slide_number | ZERO_STANDING
R827 | 44 | slide_number | ZERO_STANDING
R831 | 44 | slide_number | ZERO_STANDING
R835 | 44 | slide_number | ZERO_STANDING

## SLIDE NUMBERS (category: slide_numbers)
ROW_ID | slide | line | category | A2 flags | cross-ref / note
R001 | p1 | l19 | slide_number |  | 
R002 | p1 | l25 | slide_number |  | 
R003 | p1 | l26 | slide_number |  | 
R004 | p1 | l31 | slide_number |  | 
R005 | p1 | l36 | slide_number |  | 
R006 | p1 | l36 | slide_number |  | 
R007 | p1 | l53 | slide_number |  | 
R008 | p3 | l60 | slide_number |  | 
R009 | p3 | l61 | slide_number |  | 
R010 | p3 | l62 | slide_number |  | 
R011 | p4 | l68 | slide_number |  | 
R012 | p4 | l68 | slide_number |  | 
R013 | p4 | l68 | slide_number |  | 
R014 | p4 | l68 | slide_number |  | 
R015 | p4 | l68 | slide_number | RESTATED | RESTATED with R028 (p5 GDV total 52,000)
R016 | p4 | l68 | slide_number |  | 
R017 | p4 | l68 | slide_number |  | 
R018 | p4 | l68 | slide_number |  | 
R019 | p4 | l68 | slide_number |  | 
R020 | p4 | l68 | slide_number |  | 
R021 | p4 | l68 | slide_number |  | 
R022 | p4 | l68 | slide_number |  | 
R023 | p4 | l68 | slide_number |  | 
R024 | p4 | l68 | slide_number |  | 
R025 | p4 | l68 | slide_number |  | 
R026 | p4 | l68 | slide_number |  | 
R027 | p4 | l68 | slide_number |  | 
R028 | p5 | l88 | slide_number | RESTATED | RESTATED with R015
R029 | p5 | l88 | slide_number |  | 
R030 | p5 | l88 | slide_number | RESTATED | RESTATED with R850 (JDA GDV 27,000)
R031 | p5 | l89 | slide_number |  | 
R032 | p5 | l89 | slide_number |  | 
R033 | p5 | l89 | slide_number | RESTATED | RESTATED with R851 (JDA launched 11,500)
R034 | p5 | l90 | slide_number |  | 
R035 | p5 | l90 | slide_number |  | 
R036 | p5 | l90 | slide_number |  | 
R037 | p5 | l91 | slide_number |  | 
R038 | p5 | l91 | slide_number |  | 
R039 | p5 | l91 | slide_number |  | 
R040 | p5 | l92 | slide_number |  | 
R041 | p5 | l92 | slide_number |  | 
R042 | p5 | l92 | slide_number |  | 
R043 | p5 | l93 | slide_number |  | 
R044 | p5 | l93 | slide_number |  | 
R045 | p5 | l93 | slide_number |  | 
R046 | p5 | l94 | slide_number |  | 
R047 | p5 | l94 | slide_number | RESTATED | RESTATED with R852 (JDA to be launched 15,500)
R048 | p5 | l94 | slide_number |  | 
R049 | p6 | l107 | slide_number |  | 
R050 | p6 | l111 | slide_number | ZERO_STANDING | 
R051 | p6 | l107 | slide_number |  | 
R052 | p6 | l111 | slide_number | ZERO_STANDING | 
R053 | p6 | l107 | slide_number |  | 
R054 | p6 | l111 | slide_number |  | 
R055 | p6 | l107 | slide_number |  | 
R056 | p6 | l111 | slide_number |  | 
R057 | p6 | l107 | slide_number |  | 
R058 | p6 | l111 | slide_number |  | 
R059 | p6 | l107 | slide_number |  | 
R060 | p6 | l111 | slide_number |  | 
R061 | p6 | l119 | slide_number |  | 
R062 | p6 | l119 | slide_number | RESTATED | RESTATED, cross-check vs R030/R028
R063 | p6 | l121 | slide_number |  | 
R064 | p6 | l121 | slide_number |  | 
R065 | p7 | l132 | slide_number |  | 
R066 | p7 | l132 | slide_number |  | 
R067 | p7 | l132 | slide_number |  | 
R068 | p7 | l132 | slide_number |  | 
R069 | p7 | l132 | slide_number |  | 
R070 | p7 | l132 | slide_number |  | 
R071 | p7 | l132 | slide_number |  | 
R072 | p7 | l132 | slide_number |  | 
R073 | p7 | l132 | slide_number |  | 
R074 | p8 | l140 | slide_number |  | 
R075 | p8 | l140 | slide_number |  | 
R076 | p8 | l140 | slide_number |  | 
R077 | p8 | l140 | slide_number |  | 
R078 | p8 | l140 | slide_number |  | 
R079 | p8 | l140 | slide_number |  | 
R080 | p8 | l140 | slide_number |  | 
R081 | p8 | l140 | slide_number |  | 
R082 | p8 | l140 | slide_number |  | 
R083 | p8 | l140 | slide_number |  | 
R084 | p8 | l140 | slide_number |  | 
R085 | p8 | l140 | slide_number |  | 
R086 | p8 | l140 | slide_number |  | 
R087 | p8 | l140 | slide_number |  | 
R088 | p8 | l140 | slide_number |  | 
R089 | p8 | l140 | slide_number |  | 
R090 | p8 | l140 | slide_number |  | 
R091 | p8 | l140 | slide_number |  | 
R092 | p8 | l140 | slide_number |  | 
R093 | p9 | l159 | slide_number |  | 
R094 | p9 | l159 | slide_number |  | 
R095 | p9 | l159 | slide_number |  | 
R096 | p9 | l159 | slide_number |  | 
R097 | p9 | l159 | slide_number |  | 
R098 | p9 | l160 | slide_number | ZERO_STANDING | 
R099 | p9 | l160 | slide_number |  | 
R100 | p9 | l160 | slide_number |  | 
R101 | p9 | l160 | slide_number |  | 
R102 | p9 | l160 | slide_number |  | 
R103 | p9 | l161 | slide_number |  | 
R104 | p9 | l161 | slide_number |  | 
R105 | p9 | l161 | slide_number |  | 
R106 | p9 | l161 | slide_number |  | 
R107 | p9 | l161 | slide_number |  | 
R108 | p9 | l165 | slide_number |  | 
R109 | p10 | l170 | slide_number |  | 
R110 | p10 | l170 | slide_number |  | 
R111 | p10 | l170 | slide_number |  | 
R112 | p10 | l170 | slide_number |  | 
R113 | p11 | l178 | slide_number |  | 
R114 | p11 | l178 | slide_number |  | 
R115 | p11 | l178 | slide_number |  | 
R116 | p11 | l178 | slide_number |  | 
R117 | p11 | l178 | slide_number |  | 
R118 | p11 | l178 | slide_number |  | 
R119 | p11 | l178 | slide_number |  | 
R120 | p11 | l178 | slide_number |  | 
R121 | p11 | l178 | slide_number |  | 
R122 | p11 | l178 | slide_number |  | 
R123 | p11 | l178 | slide_number |  | 
R124 | p11 | l178 | slide_number |  | 
R125 | p11 | l178 | slide_number |  | 
R126 | p11 | l178 | slide_number |  | 
R127 | p11 | l178 | slide_number |  | 
R128 | p11 | l178 | slide_number |  | 
R129 | p11 | l178 | slide_number |  | 
R130 | p11 | l178 | slide_number |  | 
R131 | p11 | l178 | slide_number |  | 
R132 | p11 | l178 | slide_number |  | 
R133 | p11 | l178 | slide_number |  | 
R134 | p11 | l178 | slide_number |  | 
R135 | p11 | l178 | slide_number |  | 
R136 | p11 | l178 | slide_number |  | 
R137 | p11 | l178 | slide_number |  | 
R138 | p11 | l180 | slide_number |  | 
R139 | p11 | l186 | slide_number |  | 
R140 | p12 | l193 | slide_number |  | 
R141 | p12 | l193 | slide_number |  | 
R142 | p12 | l193 | slide_number |  | 
R143 | p12 | l193 | slide_number |  | 
R144 | p12 | l193 | slide_number |  | 
R145 | p12 | l193 | slide_number |  | 
R146 | p12 | l193 | slide_number |  | 
R147 | p12 | l193 | slide_number |  | 
R148 | p12 | l193 | slide_number |  | 
R149 | p12 | l193 | slide_number |  | 
R150 | p12 | l193 | slide_number |  | 
R151 | p12 | l193 | slide_number |  | 
R152 | p12 | l193 | slide_number |  | 
R153 | p12 | l193 | slide_number |  | 
R154 | p12 | l193 | slide_number |  | 
R155 | p12 | l193 | slide_number |  | 
R156 | p12 | l193 | slide_number |  | 
R157 | p12 | l193 | slide_number |  | 
R158 | p12 | l193 | slide_number |  | 
R159 | p12 | l193 | slide_number |  | 
R160 | p12 | l193 | slide_number |  | 
R161 | p12 | l193 | slide_number |  | 
R162 | p12 | l193 | slide_number |  | 
R163 | p12 | l193 | slide_number |  | 
R164 | p12 | l193 | slide_number |  | 
R165 | p12 | l193 | slide_number |  | 
R166 | p12 | l193 | slide_number |  | 
R167 | p12 | l193 | slide_number |  | 
R168 | p12 | l193 | slide_number |  | 
R169 | p12 | l193 | slide_number |  | 
R170 | p12 | l193 | slide_number |  | 
R171 | p12 | l193 | slide_number |  | 
R172 | p14 | l218 | slide_number |  | 
R173 | p14 | l223 | slide_number |  | 
R174 | p14 | l228 | slide_number |  | 
R175 | p14 | l221 | slide_number |  | 
R176 | p14 | l221 | slide_number |  | 
R177 | p14 | l221 | slide_number |  | 
R178 | p14 | l221 | slide_number |  | 
R179 | p14 | l221 | slide_number |  | 
R180 | p14 | l221 | slide_number |  | 
R181 | p14 | l221 | slide_number |  | 
R182 | p14 | l221 | slide_number |  | 
R183 | p15 | l248 | slide_number |  | 
R184 | p15 | l248 | slide_number |  | 
R185 | p15 | l248 | slide_number |  | 
R186 | p15 | l248 | slide_number |  | 
R187 | p15 | l248 | slide_number |  | 
R188 | p15 | l248 | slide_number |  | 
R189 | p16 | l263 | slide_number |  | 
R190 | p16 | l263 | slide_number |  | 
R191 | p16 | l263 | slide_number |  | 
R192 | p16 | l263 | slide_number |  | 
R193 | p16 | l263 | slide_number |  | 
R194 | p16 | l263 | slide_number |  | 
R195 | p17 | l275 | slide_number |  | 
R196 | p17 | l277 | slide_number |  | 
R197 | p17 | l279 | slide_number |  | 
R198 | p17 | l280 | slide_number |  | 
R199 | p17 | l282 | slide_number |  | 
R200 | p17 | l283 | slide_number |  | 
R201 | p17 | l286 | slide_number |  | 
R202 | p17 | l282 | slide_number |  | 
R203 | p17 | l287 | slide_number |  | 
R204 | p17 | l289 | slide_number |  | 
R205 | p17 | l291 | slide_number |  | 
R206 | p17 | l293 | slide_number |  | 
R207 | p17 | l295 | slide_number |  | 
R208 | p19 | l311 | slide_number |  | 
R209 | p19 | l311 | slide_number |  | 
R210 | p19 | l312 | slide_number |  | 
R211 | p19 | l312 | slide_number |  | 
R212 | p19 | l315 | slide_number |  | 
R213 | p19 | l315 | slide_number |  | 
R214 | p19 | l316 | slide_number |  | 
R215 | p19 | l316 | slide_number |  | 
R216 | p19 | l317 | slide_number |  | 
R217 | p19 | l317 | slide_number |  | 
R218 | p19 | l320 | slide_number |  | 
R219 | p19 | l320 | slide_number |  | 
R220 | p19 | l320 | slide_number |  | 
R221 | p19 | l320 | slide_number |  | 
R222 | p19 | l321 | slide_number |  | 
R223 | p19 | l322 | slide_number |  | 
R224 | p19 | l318 | slide_number | ZERO_STANDING | 
R225 | p20 | l327 | slide_number |  | 
R226 | p20 | l327 | slide_number |  | 
R227 | p20 | l327 | slide_number |  | 
R228 | p20 | l327 | slide_number |  | 
R229 | p20 | l327 | slide_number |  | 
R230 | p20 | l327 | slide_number |  | 
R231 | p20 | l327 | slide_number |  | 
R232 | p20 | l327 | slide_number |  | 
R233 | p20 | l327 | slide_number |  | 
R234 | p20 | l327 | slide_number |  | 
R235 | p20 | l327 | slide_number |  | 
R236 | p20 | l327 | slide_number |  | 
R237 | p20 | l327 | slide_number |  | 
R238 | p20 | l327 | slide_number |  | 
R239 | p20 | l327 | slide_number |  | 
R240 | p20 | l327 | slide_number |  | 
R241 | p20 | l327 | slide_number |  | 
R242 | p20 | l327 | slide_number |  | 
R243 | p20 | l327 | slide_number |  | 
R244 | p20 | l327 | slide_number |  | 
R245 | p20 | l327 | slide_number |  | 
R246 | p20 | l327 | slide_number |  | 
R247 | p20 | l327 | slide_number |  | 
R248 | p20 | l327 | slide_number |  | 
R249 | p20 | l327 | slide_number |  | 
R250 | p20 | l327 | slide_number |  | 
R251 | p20 | l327 | slide_number |  | 
R252 | p20 | l327 | slide_number |  | 
R253 | p22 | l347 | slide_number |  | 
R254 | p22 | l347 | slide_number |  | 
R255 | p22 | l347 | slide_number |  | 
R256 | p22 | l347 | slide_number |  | 
R257 | p22 | l347 | slide_number |  | 
R258 | p22 | l347 | slide_number |  | 
R259 | p22 | l347 | slide_number |  | 
R260 | p22 | l347 | slide_number |  | 
R261 | p22 | l347 | slide_number |  | 
R262 | p22 | l347 | slide_number |  | 
R263 | p22 | l347 | slide_number |  | 
R264 | p22 | l347 | slide_number |  | 
R265 | p22 | l347 | slide_number |  | 
R266 | p22 | l347 | slide_number |  | 
R267 | p22 | l347 | slide_number |  | 
R268 | p22 | l347 | slide_number |  | 
R269 | p22 | l347 | slide_number |  | 
R270 | p22 | l347 | slide_number |  | 
R271 | p22 | l347 | slide_number |  | 
R272 | p22 | l347 | slide_number |  | 
R273 | p22 | l347 | slide_number |  | 
R274 | p22 | l347 | slide_number |  | 
R275 | p22 | l347 | slide_number |  | 
R276 | p22 | l347 | slide_number |  | 
R277 | p22 | l347 | slide_number |  | 
R278 | p22 | l347 | slide_number |  | 
R279 | p22 | l347 | slide_number |  | 
R280 | p22 | l347 | slide_number |  | 
R281 | p22 | l347 | slide_number |  | 
R282 | p22 | l347 | slide_number |  | 
R283 | p22 | l347 | slide_number |  | 
R284 | p22 | l347 | slide_number |  | 
R285 | p22 | l347 | slide_number |  | 
R286 | p22 | l347 | slide_number |  | 
R287 | p22 | l347 | slide_number |  | 
R288 | p22 | l347 | slide_number |  | 
R289 | p22 | l347 | slide_number |  | 
R290 | p22 | l347 | slide_number |  | 
R291 | p22 | l347 | slide_number |  | 
R292 | p22 | l347 | slide_number |  | 
R293 | p22 | l347 | slide_number |  | 
R294 | p22 | l347 | slide_number |  | 
R295 | p22 | l347 | slide_number |  | 
R296 | p22 | l347 | slide_number |  | 
R297 | p22 | l347 | slide_number |  | 
R298 | p22 | l347 | slide_number |  | 
R299 | p22 | l347 | slide_number |  | 
R300 | p22 | l347 | slide_number |  | 
R301 | p22 | l347 | slide_number |  | 
R302 | p22 | l347 | slide_number |  | 
R303 | p22 | l347 | slide_number |  | 
R304 | p22 | l347 | slide_number |  | 
R305 | p22 | l347 | slide_number |  | 
R306 | p22 | l347 | slide_number |  | 
R307 | p22 | l347 | slide_number |  | 
R308 | p22 | l347 | slide_number |  | 
R309 | p22 | l347 | slide_number |  | 
R310 | p22 | l347 | slide_number |  | 
R311 | p22 | l364 | slide_number |  | 
R312 | p22 | l364 | slide_number |  | 
R313 | p22 | l364 | slide_number |  | 
R314 | p22 | l364 | slide_number |  | 
R315 | p22 | l365 | slide_number |  | 
R316 | p22 | l365 | slide_number |  | 
R317 | p22 | l365 | slide_number |  | 
R318 | p22 | l365 | slide_number |  | 
R319 | p23 | l372 | slide_number |  | 
R320 | p23 | l372 | slide_number |  | 
R321 | p23 | l372 | slide_number |  | 
R322 | p23 | l372 | slide_number |  | 
R323 | p23 | l372 | slide_number |  | 
R324 | p23 | l372 | slide_number |  | 
R325 | p23 | l372 | slide_number |  | 
R326 | p23 | l372 | slide_number |  | 
R327 | p23 | l372 | slide_number |  | 
R328 | p23 | l372 | slide_number |  | 
R329 | p23 | l372 | slide_number |  | 
R330 | p23 | l372 | slide_number |  | 
R331 | p23 | l372 | slide_number |  | 
R332 | p23 | l372 | slide_number |  | 
R333 | p24 | l391 | slide_number |  | 
R334 | p24 | l391 | slide_number |  | 
R335 | p24 | l391 | slide_number |  | 
R336 | p24 | l391 | slide_number |  | 
R337 | p24 | l391 | slide_number |  | 
R338 | p24 | l391 | slide_number |  | 
R339 | p24 | l391 | slide_number |  | 
R340 | p24 | l391 | slide_number |  | 
R341 | p24 | l391 | slide_number |  | 
R342 | p24 | l391 | slide_number |  | 
R343 | p24 | l391 | slide_number |  | 
R344 | p24 | l391 | slide_number |  | 
R345 | p24 | l391 | slide_number |  | 
R346 | p24 | l391 | slide_number |  | 
R347 | p24 | l391 | slide_number |  | 
R348 | p24 | l391 | slide_number |  | 
R349 | p24 | l391 | slide_number |  | 
R350 | p24 | l391 | slide_number |  | 
R351 | p24 | l391 | slide_number |  | 
R352 | p24 | l391 | slide_number |  | 
R353 | p24 | l391 | slide_number |  | 
R354 | p24 | l391 | slide_number |  | 
R355 | p24 | l391 | slide_number | ZERO_STANDING | 
R356 | p24 | l391 | slide_number |  | 
R357 | p24 | l391 | slide_number |  | 
R358 | p24 | l391 | slide_number |  | 
R359 | p24 | l391 | slide_number |  | 
R360 | p24 | l391 | slide_number |  | 
R361 | p24 | l399 | slide_number |  | 
R362 | p24 | l399 | slide_number |  | 
R363 | p24 | l399 | slide_number |  | 
R364 | p24 | l399 | slide_number |  | 
R365 | p24 | l399 | slide_number |  | 
R366 | p24 | l399 | slide_number |  | 
R367 | p24 | l399 | slide_number |  | 
R368 | p26 | l417 | slide_number |  | 
R369 | p26 | l417 | slide_number |  | 
R370 | p26 | l417 | slide_number |  | 
R371 | p26 | l417 | slide_number |  | 
R372 | p26 | l417 | slide_number |  | 
R373 | p26 | l417 | slide_number |  | 
R374 | p26 | l417 | slide_number |  | 
R375 | p26 | l417 | slide_number |  | 
R376 | p26 | l418 | slide_number |  | 
R377 | p26 | l418 | slide_number |  | 
R378 | p26 | l418 | slide_number |  | 
R379 | p26 | l418 | slide_number |  | 
R380 | p26 | l418 | slide_number |  | 
R381 | p26 | l418 | slide_number |  | 
R382 | p26 | l418 | slide_number |  | 
R383 | p26 | l418 | slide_number |  | 
R384 | p26 | l419 | slide_number |  | 
R385 | p26 | l419 | slide_number |  | 
R386 | p26 | l419 | slide_number |  | 
R387 | p26 | l419 | slide_number |  | 
R388 | p26 | l419 | slide_number |  | 
R389 | p26 | l419 | slide_number |  | 
R390 | p26 | l419 | slide_number |  | 
R391 | p26 | l419 | slide_number |  | 
R392 | p26 | l420 | slide_number |  | 
R393 | p26 | l420 | slide_number |  | 
R394 | p26 | l420 | slide_number |  | 
R395 | p26 | l420 | slide_number |  | 
R396 | p26 | l420 | slide_number |  | 
R397 | p26 | l420 | slide_number |  | 
R398 | p26 | l420 | slide_number |  | 
R399 | p26 | l420 | slide_number |  | 
R400 | p26 | l421 | slide_number |  | 
R401 | p26 | l421 | slide_number |  | 
R402 | p26 | l421 | slide_number |  | 
R403 | p26 | l421 | slide_number |  | 
R404 | p26 | l421 | slide_number |  | 
R405 | p26 | l421 | slide_number |  | 
R406 | p26 | l421 | slide_number |  | 
R407 | p26 | l421 | slide_number |  | 
R408 | p26 | l422 | slide_number |  | 
R409 | p26 | l422 | slide_number |  | 
R410 | p26 | l422 | slide_number |  | 
R411 | p26 | l422 | slide_number |  | 
R412 | p26 | l422 | slide_number |  | 
R413 | p26 | l422 | slide_number |  | 
R414 | p26 | l422 | slide_number |  | 
R415 | p26 | l422 | slide_number |  | 
R416 | p26 | l423 | slide_number |  | 
R417 | p26 | l423 | slide_number |  | 
R418 | p26 | l423 | slide_number |  | 
R419 | p26 | l423 | slide_number |  | 
R420 | p26 | l423 | slide_number |  | 
R421 | p26 | l423 | slide_number |  | 
R422 | p26 | l423 | slide_number |  | 
R423 | p26 | l423 | slide_number |  | 
R424 | p26 | l424 | slide_number |  | 
R425 | p26 | l424 | slide_number |  | 
R426 | p26 | l424 | slide_number |  | 
R427 | p26 | l424 | slide_number |  | 
R428 | p26 | l424 | slide_number |  | 
R429 | p26 | l424 | slide_number |  | 
R430 | p26 | l424 | slide_number |  | 
R431 | p26 | l424 | slide_number |  | 
R432 | p26 | l425 | slide_number |  | 
R433 | p26 | l425 | slide_number |  | 
R434 | p26 | l425 | slide_number |  | 
R435 | p26 | l425 | slide_number |  | 
R436 | p26 | l425 | slide_number |  | 
R437 | p26 | l425 | slide_number |  | 
R438 | p26 | l425 | slide_number |  | 
R439 | p26 | l425 | slide_number |  | 
R440 | p26 | l426 | slide_number |  | 
R441 | p26 | l426 | slide_number |  | 
R442 | p26 | l426 | slide_number |  | 
R443 | p26 | l426 | slide_number |  | 
R444 | p26 | l426 | slide_number |  | 
R445 | p26 | l426 | slide_number |  | 
R446 | p26 | l426 | slide_number |  | 
R447 | p26 | l426 | slide_number |  | 
R448 | p26 | l427 | slide_number |  | 
R449 | p26 | l427 | slide_number |  | 
R450 | p26 | l427 | slide_number |  | 
R451 | p26 | l427 | slide_number |  | 
R452 | p26 | l427 | slide_number |  | 
R453 | p26 | l427 | slide_number |  | 
R454 | p26 | l427 | slide_number |  | 
R455 | p26 | l427 | slide_number |  | 
R456 | p26 | l428 | slide_number |  | 
R457 | p26 | l428 | slide_number |  | 
R458 | p26 | l429 | slide_number |  | 
R459 | p26 | l429 | slide_number |  | 
R460 | p26 | l429 | slide_number |  | 
R461 | p26 | l429 | slide_number |  | 
R462 | p26 | l429 | slide_number |  | 
R463 | p26 | l429 | slide_number |  | 
R464 | p26 | l429 | slide_number |  | 
R465 | p26 | l429 | slide_number |  | 
R466 | p26 | l430 | slide_number |  | 
R467 | p26 | l430 | slide_number |  | 
R468 | p26 | l430 | slide_number |  | 
R469 | p26 | l430 | slide_number |  | 
R470 | p26 | l430 | slide_number |  | 
R471 | p26 | l430 | slide_number |  | 
R472 | p26 | l430 | slide_number |  | 
R473 | p26 | l430 | slide_number |  | 
R474 | p26 | l443 | slide_number |  | 
R475 | p26 | l443 | slide_number |  | 
R476 | p26 | l443 | slide_number |  | 
R477 | p26 | l443 | slide_number |  | 
R478 | p26 | l443 | slide_number |  | 
R479 | p26 | l443 | slide_number |  | 
R480 | p26 | l447 | slide_number |  | 
R481 | p26 | l447 | slide_number |  | 
R482 | p27 | l460 | slide_number |  | 
R483 | p27 | l460 | slide_number |  | 
R484 | p27 | l460 | slide_number |  | 
R485 | p27 | l460 | slide_number |  | 
R486 | p27 | l460 | slide_number |  | 
R487 | p27 | l460 | slide_number |  | 
R488 | p27 | l460 | slide_number |  | 
R489 | p27 | l460 | slide_number |  | 
R490 | p27 | l460 | slide_number |  | 
R491 | p27 | l460 | slide_number |  | 
R492 | p27 | l460 | slide_number |  | 
R493 | p27 | l460 | slide_number |  | 
R494 | p27 | l460 | slide_number |  | 
R495 | p27 | l460 | slide_number |  | 
R496 | p27 | l460 | slide_number |  | 
R497 | p27 | l465 | slide_number |  | 
R498 | p27 | l465 | slide_number |  | 
R499 | p28 | l473 | slide_number |  | 
R500 | p28 | l474 | slide_number |  | 
R501 | p28 | l473 | slide_number |  | 
R502 | p28 | l476 | slide_number |  | 
R503 | p28 | l476 | slide_number |  | 
R504 | p28 | l476 | slide_number |  | 
R505 | p28 | l476 | slide_number |  | 
R506 | p28 | l476 | slide_number |  | 
R507 | p28 | l476 | slide_number |  | 
R508 | p28 | l476 | slide_number |  | 
R509 | p28 | l476 | slide_number |  | 
R510 | p28 | l476 | slide_number |  | 
R511 | p28 | l476 | slide_number |  | 
R512 | p28 | l476 | slide_number |  | 
R513 | p29 | l494 | slide_number |  | 
R514 | p29 | l494 | slide_number |  | 
R515 | p29 | l494 | slide_number |  | 
R516 | p29 | l494 | slide_number |  | 
R517 | p29 | l494 | slide_number |  | 
R518 | p29 | l494 | slide_number |  | 
R519 | p29 | l494 | slide_number |  | 
R520 | p29 | l494 | slide_number |  | 
R521 | p30 | l512 | slide_number |  | 
R522 | p30 | l512 | slide_number |  | 
R523 | p30 | l512 | slide_number |  | 
R524 | p30 | l512 | slide_number | ZERO_STANDING | 
R525 | p30 | l512 | slide_number |  | 
R526 | p30 | l512 | slide_number |  | 
R527 | p30 | l512 | slide_number |  | 
R528 | p30 | l512 | slide_number | ZERO_STANDING | 
R529 | p30 | l512 | slide_number |  | 
R530 | p30 | l512 | slide_number |  | 
R531 | p30 | l512 | slide_number |  | 
R532 | p30 | l512 | slide_number | ZERO_STANDING | 
R533 | p30 | l512 | slide_number |  | 
R534 | p30 | l512 | slide_number |  | 
R535 | p30 | l512 | slide_number |  | 
R536 | p30 | l512 | slide_number | ZERO_STANDING | 
R537 | p30 | l512 | slide_number |  | 
R538 | p30 | l512 | slide_number |  | 
R539 | p30 | l512 | slide_number |  | 
R540 | p30 | l512 | slide_number | ZERO_STANDING | 
R541 | p30 | l512 | slide_number |  | 
R542 | p30 | l512 | slide_number |  | 
R543 | p30 | l512 | slide_number |  | 
R544 | p31 | l527 | slide_number |  | 
R545 | p31 | l527 | slide_number |  | 
R546 | p31 | l527 | slide_number |  | 
R547 | p31 | l527 | slide_number |  | 
R548 | p31 | l527 | slide_number |  | 
R549 | p31 | l527 | slide_number |  | 
R550 | p31 | l527 | slide_number |  | 
R551 | p31 | l527 | slide_number |  | 
R552 | p31 | l527 | slide_number |  | 
R553 | p31 | l527 | slide_number |  | 
R554 | p31 | l527 | slide_number |  | 
R555 | p31 | l527 | slide_number |  | 
R556 | p31 | l527 | slide_number |  | 
R557 | p31 | l527 | slide_number |  | 
R558 | p31 | l527 | slide_number |  | 
R559 | p31 | l527 | slide_number |  | 
R560 | p31 | l527 | slide_number |  | 
R561 | p31 | l527 | slide_number |  | 
R562 | p31 | l527 | slide_number |  | 
R563 | p31 | l527 | slide_number |  | 
R564 | p31 | l527 | slide_number |  | 
R565 | p31 | l527 | slide_number |  | 
R566 | p31 | l527 | slide_number |  | 
R567 | p32 | l545 | slide_number |  | 
R568 | p32 | l545 | slide_number |  | 
R569 | p32 | l545 | slide_number |  | 
R570 | p32 | l545 | slide_number | ZERO_STANDING | 
R571 | p32 | l545 | slide_number |  | 
R572 | p32 | l545 | slide_number |  | 
R573 | p32 | l545 | slide_number |  | 
R574 | p32 | l545 | slide_number | ZERO_STANDING | 
R575 | p32 | l545 | slide_number |  | 
R576 | p32 | l545 | slide_number |  | 
R577 | p32 | l545 | slide_number |  | 
R578 | p32 | l545 | slide_number | ZERO_STANDING | 
R579 | p32 | l545 | slide_number |  | 
R580 | p32 | l545 | slide_number |  | 
R581 | p32 | l545 | slide_number |  | 
R582 | p32 | l545 | slide_number |  | 
R583 | p32 | l545 | slide_number |  | 
R584 | p32 | l545 | slide_number |  | 
R585 | p32 | l545 | slide_number |  | 
R586 | p32 | l545 | slide_number |  | 
R587 | p32 | l545 | slide_number |  | 
R588 | p32 | l545 | slide_number |  | 
R589 | p32 | l545 | slide_number |  | 
R590 | p33 | l560 | slide_number |  | 
R591 | p33 | l560 | slide_number |  | 
R592 | p33 | l560 | slide_number |  | 
R593 | p33 | l560 | slide_number |  | 
R594 | p33 | l560 | slide_number |  | 
R595 | p33 | l560 | slide_number |  | 
R596 | p33 | l560 | slide_number |  | 
R597 | p33 | l560 | slide_number |  | 
R598 | p33 | l560 | slide_number |  | 
R599 | p33 | l560 | slide_number |  | 
R600 | p33 | l560 | slide_number |  | 
R601 | p33 | l560 | slide_number |  | 
R602 | p33 | l560 | slide_number |  | 
R603 | p33 | l560 | slide_number |  | 
R604 | p33 | l560 | slide_number |  | 
R605 | p33 | l560 | slide_number |  | 
R606 | p33 | l560 | slide_number |  | 
R607 | p33 | l560 | slide_number |  | 
R608 | p33 | l560 | slide_number |  | 
R609 | p33 | l560 | slide_number |  | 
R610 | p33 | l560 | slide_number |  | 
R611 | p33 | l560 | slide_number |  | 
R612 | p33 | l560 | slide_number |  | 
R613 | p34 | l582 | slide_number |  | 
R614 | p34 | l582 | slide_number |  | 
R615 | p34 | l582 | slide_number |  | 
R616 | p34 | l582 | slide_number |  | 
R617 | p34 | l582 | slide_number |  | 
R618 | p34 | l582 | slide_number |  | 
R619 | p34 | l582 | slide_number |  | 
R620 | p34 | l582 | slide_number |  | 
R621 | p34 | l582 | slide_number |  | 
R622 | p34 | l582 | slide_number |  | 
R623 | p34 | l582 | slide_number |  | 
R624 | p34 | l582 | slide_number |  | 
R625 | p34 | l582 | slide_number |  | 
R626 | p34 | l582 | slide_number |  | 
R627 | p34 | l582 | slide_number |  | 
R628 | p34 | l582 | slide_number |  | 
R629 | p34 | l582 | slide_number |  | 
R630 | p34 | l582 | slide_number |  | 
R631 | p34 | l582 | slide_number |  | 
R632 | p34 | l582 | slide_number |  | 
R633 | p34 | l582 | slide_number |  | 
R634 | p34 | l582 | slide_number |  | 
R635 | p34 | l582 | slide_number |  | 
R636 | p35 | l595 | slide_number |  | 
R637 | p35 | l595 | slide_number |  | 
R638 | p35 | l595 | slide_number |  | 
R639 | p35 | l595 | slide_number |  | 
R640 | p35 | l595 | slide_number |  | 
R641 | p35 | l595 | slide_number |  | 
R642 | p35 | l595 | slide_number |  | 
R643 | p35 | l595 | slide_number |  | 
R644 | p35 | l595 | slide_number |  | 
R645 | p35 | l595 | slide_number | ZERO_STANDING | 
R646 | p35 | l595 | slide_number |  | 
R647 | p35 | l595 | slide_number |  | 
R648 | p35 | l595 | slide_number |  | 
R649 | p35 | l595 | slide_number |  | 
R650 | p35 | l595 | slide_number |  | 
R651 | p35 | l595 | slide_number |  | 
R652 | p35 | l595 | slide_number |  | 
R653 | p35 | l595 | slide_number |  | 
R654 | p35 | l595 | slide_number |  | 
R655 | p35 | l595 | slide_number |  | 
R656 | p35 | l595 | slide_number |  | 
R657 | p35 | l595 | slide_number |  | 
R658 | p35 | l595 | slide_number |  | 
R659 | p36 | l607 | slide_number |  | 
R660 | p36 | l607 | slide_number |  | 
R661 | p36 | l607 | slide_number |  | 
R662 | p36 | l607 | slide_number |  | 
R663 | p36 | l607 | slide_number |  | 
R664 | p36 | l607 | slide_number | ZERO_STANDING | 
R665 | p36 | l607 | slide_number |  | 
R666 | p36 | l607 | slide_number |  | 
R667 | p36 | l607 | slide_number | ZERO_STANDING | 
R668 | p36 | l607 | slide_number | ZERO_STANDING | 
R669 | p36 | l607 | slide_number |  | 
R670 | p36 | l607 | slide_number |  | 
R671 | p36 | l607 | slide_number |  | 
R672 | p36 | l607 | slide_number | ZERO_STANDING | 
R673 | p36 | l607 | slide_number |  | 
R674 | p36 | l607 | slide_number |  | 
R675 | p36 | l607 | slide_number |  | 
R676 | p36 | l607 | slide_number |  | 
R677 | p36 | l607 | slide_number |  | 
R678 | p36 | l607 | slide_number | ZERO_STANDING | 
R679 | p36 | l607 | slide_number |  | 
R680 | p36 | l607 | slide_number |  | 
R681 | p36 | l607 | slide_number |  | 
R682 | p37 | l621 | slide_number |  | 
R683 | p37 | l621 | slide_number |  | 
R684 | p37 | l621 | slide_number |  | 
R685 | p37 | l621 | slide_number |  | 
R686 | p37 | l621 | slide_number |  | 
R687 | p37 | l621 | slide_number |  | 
R688 | p37 | l621 | slide_number |  | 
R689 | p37 | l621 | slide_number |  | 
R690 | p37 | l621 | slide_number | ZERO_STANDING | 
R691 | p37 | l621 | slide_number |  | 
R692 | p37 | l621 | slide_number |  | 
R693 | p37 | l621 | slide_number |  | 
R694 | p37 | l621 | slide_number |  | 
R695 | p37 | l621 | slide_number |  | 
R696 | p37 | l621 | slide_number |  | 
R697 | p37 | l621 | slide_number |  | 
R698 | p37 | l621 | slide_number |  | 
R699 | p37 | l621 | slide_number |  | 
R700 | p37 | l621 | slide_number |  | 
R701 | p37 | l621 | slide_number |  | 
R702 | p37 | l621 | slide_number |  | 
R703 | p37 | l621 | slide_number |  | 
R704 | p37 | l621 | slide_number |  | 
R705 | p38 | l632 | slide_number |  | 
R706 | p38 | l632 | slide_number |  | 
R707 | p38 | l632 | slide_number |  | 
R708 | p38 | l632 | slide_number | ZERO_STANDING | 
R709 | p38 | l632 | slide_number |  | 
R710 | p38 | l632 | slide_number | ZERO_STANDING | 
R711 | p38 | l632 | slide_number |  | 
R712 | p38 | l632 | slide_number | ZERO_STANDING | 
R713 | p38 | l632 | slide_number |  | 
R714 | p38 | l632 | slide_number | ZERO_STANDING | 
R715 | p38 | l632 | slide_number |  | 
R716 | p38 | l632 | slide_number | ZERO_STANDING | 
R717 | p38 | l632 | slide_number |  | 
R718 | p38 | l632 | slide_number | ZERO_STANDING | 
R719 | p38 | l632 | slide_number |  | 
R720 | p38 | l632 | slide_number | ZERO_STANDING | 
R721 | p38 | l632 | slide_number |  | 
R722 | p38 | l632 | slide_number |  | 
R723 | p38 | l632 | slide_number |  | 
R724 | p39 | l644 | slide_number |  | 
R725 | p39 | l644 | slide_number |  | 
R726 | p39 | l644 | slide_number |  | 
R727 | p39 | l644 | slide_number | ZERO_STANDING | 
R728 | p39 | l644 | slide_number |  | 
R729 | p39 | l644 | slide_number |  | 
R730 | p39 | l644 | slide_number |  | 
R731 | p39 | l644 | slide_number | ZERO_STANDING | 
R732 | p39 | l644 | slide_number |  | 
R733 | p39 | l644 | slide_number |  | 
R734 | p39 | l644 | slide_number |  | 
R735 | p39 | l644 | slide_number | ZERO_STANDING | 
R736 | p39 | l644 | slide_number |  | 
R737 | p39 | l644 | slide_number |  | 
R738 | p39 | l644 | slide_number |  | 
R739 | p39 | l644 | slide_number | ZERO_STANDING | 
R740 | p39 | l644 | slide_number |  | 
R741 | p39 | l644 | slide_number |  | 
R742 | p39 | l644 | slide_number |  | 
R743 | p39 | l644 | slide_number | ZERO_STANDING | 
R744 | p39 | l644 | slide_number |  | 
R745 | p39 | l644 | slide_number |  | 
R746 | p39 | l644 | slide_number |  | 
R747 | p41 | l676 | slide_number |  | 
R748 | p41 | l676 | slide_number |  | 
R749 | p41 | l676 | slide_number |  | 
R750 | p41 | l676 | slide_number |  | 
R751 | p41 | l676 | slide_number |  | 
R752 | p41 | l676 | slide_number |  | 
R753 | p41 | l676 | slide_number |  | 
R754 | p41 | l676 | slide_number |  | 
R755 | p41 | l676 | slide_number |  | 
R756 | p41 | l676 | slide_number |  | 
R757 | p41 | l676 | slide_number |  | 
R758 | p41 | l676 | slide_number |  | 
R759 | p41 | l676 | slide_number |  | 
R760 | p41 | l676 | slide_number |  | 
R761 | p41 | l676 | slide_number |  | 
R762 | p41 | l676 | slide_number |  | 
R763 | p41 | l676 | slide_number |  | 
R764 | p41 | l676 | slide_number |  | 
R765 | p41 | l676 | slide_number |  | 
R766 | p41 | l676 | slide_number |  | 
R767 | p41 | l676 | slide_number |  | 
R768 | p41 | l676 | slide_number |  | 
R769 | p41 | l676 | slide_number |  | 
R770 | p42 | l700 | slide_number |  | 
R771 | p42 | l700 | slide_number |  | 
R772 | p42 | l700 | slide_number |  | 
R773 | p42 | l700 | slide_number | ZERO_STANDING | 
R774 | p42 | l700 | slide_number |  | 
R775 | p42 | l700 | slide_number |  | 
R776 | p42 | l700 | slide_number |  | 
R777 | p42 | l700 | slide_number | ZERO_STANDING | 
R778 | p42 | l700 | slide_number | ZERO_STANDING | 
R779 | p42 | l700 | slide_number |  | 
R780 | p42 | l700 | slide_number |  | 
R781 | p42 | l700 | slide_number | ZERO_STANDING | 
R782 | p42 | l700 | slide_number |  | 
R783 | p42 | l700 | slide_number |  | 
R784 | p42 | l700 | slide_number |  | 
R785 | p42 | l700 | slide_number | ZERO_STANDING | 
R786 | p42 | l700 | slide_number |  | 
R787 | p42 | l700 | slide_number |  | 
R788 | p42 | l700 | slide_number |  | 
R789 | p42 | l700 | slide_number |  | 
R790 | p42 | l700 | slide_number |  | 
R791 | p42 | l700 | slide_number |  | 
R792 | p42 | l700 | slide_number |  | 
R793 | p43 | l713 | slide_number |  | 
R794 | p43 | l713 | slide_number |  | 
R795 | p43 | l713 | slide_number |  | 
R796 | p43 | l713 | slide_number | ZERO_STANDING | 
R797 | p43 | l713 | slide_number |  | 
R798 | p43 | l713 | slide_number |  | 
R799 | p43 | l713 | slide_number |  | 
R800 | p43 | l713 | slide_number | ZERO_STANDING | 
R801 | p43 | l713 | slide_number |  | 
R802 | p43 | l713 | slide_number |  | 
R803 | p43 | l713 | slide_number |  | 
R804 | p43 | l713 | slide_number | ZERO_STANDING | 
R805 | p43 | l713 | slide_number |  | 
R806 | p43 | l713 | slide_number |  | 
R807 | p43 | l713 | slide_number |  | 
R808 | p43 | l713 | slide_number | ZERO_STANDING | 
R809 | p43 | l713 | slide_number |  | 
R810 | p43 | l713 | slide_number |  | 
R811 | p43 | l713 | slide_number |  | 
R812 | p43 | l713 | slide_number | ZERO_STANDING | 
R813 | p43 | l713 | slide_number |  | 
R814 | p43 | l713 | slide_number |  | 
R815 | p43 | l713 | slide_number |  | 
R816 | p44 | l727 | slide_number |  | 
R817 | p44 | l727 | slide_number |  | 
R818 | p44 | l727 | slide_number |  | 
R819 | p44 | l727 | slide_number | ZERO_STANDING | 
R820 | p44 | l727 | slide_number |  | 
R821 | p44 | l727 | slide_number |  | 
R822 | p44 | l727 | slide_number |  | 
R823 | p44 | l727 | slide_number | ZERO_STANDING | 
R824 | p44 | l727 | slide_number |  | 
R825 | p44 | l727 | slide_number |  | 
R826 | p44 | l727 | slide_number |  | 
R827 | p44 | l727 | slide_number | ZERO_STANDING | 
R828 | p44 | l727 | slide_number |  | 
R829 | p44 | l727 | slide_number |  | 
R830 | p44 | l727 | slide_number |  | 
R831 | p44 | l727 | slide_number | ZERO_STANDING | 
R832 | p44 | l727 | slide_number |  | 
R833 | p44 | l727 | slide_number |  | 
R834 | p44 | l727 | slide_number |  | 
R835 | p44 | l727 | slide_number | ZERO_STANDING | 
R836 | p44 | l727 | slide_number |  | 
R837 | p44 | l727 | slide_number |  | 
R838 | p44 | l727 | slide_number |  | 
R839 | p30 | l520 | slide_number |  | 
R840 | p32 | l567 | slide_number | PAGE_ANCHOR_DEFECT | PAGE_ANCHOR_DEFECT: line 567 sits on fulltext page 33 (Season 2), row says page 32
R841 | p34 | l590 | slide_number |  | 
R842 | p36 | l615 | slide_number |  | 
R843 | p39 | l651 | slide_number |  | 
R844 | p41 | l684 | slide_number |  | 
R845 | p42 | l703 | slide_number |  | 
R846 | p43 | l721 | slide_number |  | 
R847 | p44 | l735 | slide_number |  | 
R848 | p42 | l708 | slide_number |  | 
R849 | p42 | l708 | slide_number |  | 
R850 | p40 | l658 | slide_number | RESTATED | RESTATED with R030
R851 | p40 | l658 | slide_number | RESTATED | RESTATED with R033
R852 | p40 | l657 | slide_number | RESTATED | RESTATED with R047
R853 | p40 | l660 | slide_number |  | 
R854 | p40 | l660 | slide_number |  | 
R855 | p40 | l660 | slide_number |  | 
R856 | p40 | l660 | slide_number |  | 
R857 | p40 | l660 | slide_number |  | 
R858 | p40 | l660 | slide_number |  | 
R859 | p40 | l660 | slide_number |  | 
R860 | p40 | l660 | slide_number |  | 

## ENTITIES
ROW_ID | slide | line | category | A2 flags | cross-ref / note
R861 | p1 | l18 | entity |  | 
R862 | p1 | l21 | entity |  | 
R863 | p1 | l49 | entity |  | 
R864 | p1 | l32 | entity |  | 
R865 | p1 | l52 | entity |  | 
R866 | p4 | l80 | entity |  | 
R867 | p4 | l80 | entity |  | 
R868 | p5 | l88 | entity |  | 
R869 | p6 | l104 | entity |  | 
R870 | p6 | l121 | entity |  | 
R871 | p7 | l130 | entity |  | 
R872 | p7 | l130 | entity |  | 
R873 | p7 | l130 | entity |  | 
R874 | p11 | l189 | entity |  | 
R875 | p13 | l214 | entity |  | 
R876 | p14 | l235 | entity |  | 
R877 | p14 | l237 | entity |  | 
R878 | p14 | l218 | entity |  | 
R879 | p14 | l218 | entity |  | 
R880 | p14 | l218 | entity |  | 
R881 | p14 | l218 | entity |  | 
R882 | p14 | l233 | entity |  | 
R883 | p14 | l233 | entity |  | 
R884 | p14 | l233 | entity |  | 
R885 | p14 | l233 | entity |  | 
R886 | p14 | l223 | entity |  | 
R887 | p15 | l246 | entity |  | 
R888 | p15 | l246 | entity |  | 
R889 | p15 | l246 | entity |  | 
R890 | p15 | l246 | entity |  | 
R891 | p15 | l246 | entity |  | 
R892 | p15 | l246 | entity |  | 
R893 | p16 | l261 | entity |  | 
R894 | p16 | l261 | entity |  | 
R895 | p16 | l261 | entity |  | 
R896 | p16 | l261 | entity |  | 
R897 | p16 | l261 | entity |  | 
R898 | p16 | l261 | entity |  | 
R899 | p17 | l298 | entity |  | 
R900 | p17 | l281 | entity |  | 
R901 | p17 | l297 | entity |  | 
R902 | p19 | l319 | entity |  | 
R903 | p22 | l367 | entity |  | 
R904 | p26 | l417 | entity |  | 
R905 | p26 | l418 | entity |  | 
R906 | p26 | l419 | entity |  | 
R907 | p26 | l420 | entity |  | 
R908 | p26 | l421 | entity |  | 
R909 | p26 | l422 | entity |  | 
R910 | p26 | l423 | entity |  | 
R911 | p26 | l424 | entity |  | 
R912 | p26 | l425 | entity |  | 
R913 | p26 | l426 | entity |  | 
R914 | p26 | l427 | entity |  | 
R915 | p26 | l428 | entity |  | 
R916 | p26 | l429 | entity |  | 
R917 | p26 | l430 | entity |  | 
R918 | p27 | l460 | entity |  | 
R919 | p27 | l460 | entity |  | 
R920 | p27 | l460 | entity |  | 
R921 | p27 | l460 | entity |  | 
R922 | p27 | l460 | entity |  | 
R923 | p28 | l476 | entity |  | 
R924 | p28 | l476 | entity |  | 
R925 | p28 | l476 | entity |  | 
R926 | p28 | l476 | entity |  | 
R927 | p28 | l476 | entity |  | 
R928 | p28 | l476 | entity |  | 
R929 | p28 | l476 | entity |  | 
R930 | p28 | l476 | entity |  | 
R931 | p28 | l476 | entity |  | 
R932 | p28 | l476 | entity |  | 
R933 | p28 | l476 | entity |  | 
R934 | p29 | l494 | entity |  | 
R935 | p30 | l512 | entity |  | 
R936 | p31 | l527 | entity |  | 
R937 | p32 | l545 | entity |  | 
R938 | p33 | l560 | entity |  | 
R939 | p34 | l582 | entity |  | 
R940 | p35 | l595 | entity |  | 
R941 | p36 | l607 | entity |  | 
R942 | p37 | l621 | entity |  | 
R943 | p38 | l632 | entity |  | 
R944 | p39 | l644 | entity |  | 
R945 | p41 | l676 | entity |  | 
R946 | p42 | l700 | entity |  | 
R947 | p43 | l713 | entity |  | 
R948 | p44 | l727 | entity |  | 
R949 | p40 | l660 | entity |  | 
R950 | p40 | l660 | entity |  | 
R951 | p40 | l660 | entity |  | 
R952 | p40 | l660 | entity |  | 
R953 | p40 | l660 | entity |  | 
R954 | p40 | l660 | entity |  | 
R955 | p40 | l660 | entity |  | 
R956 | p40 | l660 | entity |  | 
R957 | p45 | l739 | entity |  | 
R958 | p46 | l760 | entity |  | 

## FORWARD-LOOKING STATEMENTS
ROW_ID | slide | line | category | A2 flags | cross-ref / note
R959 | p4 | l78 | forward_statement |  | 
R960 | p4 | l83 | forward_statement |  | 
R961 | p6 | l123 | forward_statement |  | 
R962 | p6 | l124 | forward_statement |  | 
R963 | p9 | l164 | forward_statement |  | 
R964 | p10 | l170 | forward_statement |  | 
R965 | p10 | l171 | forward_statement |  | 
R966 | p10 | l172 | forward_statement |  | 
R967 | p10 | l173 | forward_statement |  | 
R968 | p27 | l460 | forward_statement |  | 
R969 | p27 | l460 | forward_statement |  | 
R970 | p27 | l460 | forward_statement |  | 
R971 | p27 | l460 | forward_statement |  | 
R972 | p27 | l460 | forward_statement |  | 
R973 | p29 | l494 | forward_statement |  | 
R974 | p29 | l505 | forward_statement |  | 
R975 | p30 | l519 | forward_statement |  | 
R976 | p31 | l538 | forward_statement |  | 
R977 | p32 | l553 | forward_statement |  | 
R978 | p33 | l567 | forward_statement |  | 
R979 | p34 | l579 | forward_statement |  | 
R980 | p35 | l601 | forward_statement |  | 
R981 | p36 | l613 | forward_statement |  | 
R982 | p37 | l621 | forward_statement |  | 
R983 | p38 | l632 | forward_statement |  | 
R984 | p41 | l686 | forward_statement |  | 
R985 | p42 | l704 | forward_statement |  | 
R986 | p43 | l720 | forward_statement |  | 
R987 | p44 | l734 | forward_statement |  | 

## DATES
ROW_ID | slide | line | category | A2 flags | cross-ref / note
R988 | p1 | l20 | date |  | 
R989 | p1 | l29 | date |  | 
R990 | p1 | l47 | date |  | 
R991 | p2 | l57 | date |  | 
R992 | p4 | l67 | date |  | 
R993 | p4 | l67 | date |  | 
R994 | p4 | l67 | date |  | 
R995 | p4 | l74 | date |  | 
R996 | p10 | l169 | date |  | 
R997 | p17 | l291 | date |  | 
R998 | p17 | l298 | date |  | 
R999 | p26 | l417 | date |  | 
R1000 | p26 | l417 | date |  | 
R1001 | p26 | l418 | date |  | 
R1002 | p26 | l418 | date |  | 
R1003 | p26 | l419 | date |  | 
R1004 | p26 | l419 | date |  | 
R1005 | p26 | l420 | date |  | 
R1006 | p26 | l420 | date |  | 
R1007 | p26 | l421 | date |  | 
R1008 | p26 | l421 | date |  | 
R1009 | p26 | l422 | date |  | 
R1010 | p26 | l422 | date |  | 
R1011 | p26 | l423 | date |  | 
R1012 | p26 | l423 | date |  | 
R1013 | p26 | l424 | date |  | 
R1014 | p26 | l424 | date |  | 
R1015 | p26 | l425 | date |  | 
R1016 | p26 | l425 | date |  | 
R1017 | p26 | l426 | date |  | 
R1018 | p26 | l426 | date |  | 
R1019 | p26 | l427 | date |  | 
R1020 | p26 | l427 | date |  | 
R1021 | p26 | l428 | date |  | 
R1022 | p26 | l428 | date |  | 
R1023 | p26 | l429 | date |  | 
R1024 | p26 | l429 | date |  | 
R1025 | p26 | l430 | date |  | 
R1026 | p26 | l430 | date |  | 
R1027 | p27 | l460 | date |  | 
R1028 | p27 | l460 | date |  | 
R1029 | p27 | l460 | date |  | 
R1030 | p27 | l460 | date |  | 
R1031 | p27 | l460 | date |  | 
R1032 | p27 | l460 | date |  | 
R1033 | p27 | l460 | date |  | 
R1034 | p27 | l460 | date |  | 
R1035 | p27 | l460 | date |  | 
R1036 | p27 | l460 | date |  | 

## FOOTNOTES AND DISCLAIMERS
ROW_ID | slide | line | category | A2 flags | cross-ref / note
R1037 | p1 | l29 | footnote_disclaimer |  | 
R1038 | p4 | l77 | footnote_disclaimer |  | 
R1039 | p5 | l96 | footnote_disclaimer |  | 
R1040 | p5 | l97 | footnote_disclaimer |  | 
R1041 | p5 | l88 | footnote_disclaimer |  | 
R1042 | p6 | l119 | footnote_disclaimer |  | 
R1043 | p8 | l149 | footnote_disclaimer |  | 
R1044 | p9 | l165 | footnote_disclaimer |  | 
R1045 | p9 | l166 | footnote_disclaimer |  | 
R1046 | p11 | l178 | footnote_disclaimer |  | 
R1047 | p14 | l218 | footnote_disclaimer |  | 
R1048 | p14 | l235 | footnote_disclaimer |  | 
R1049 | p17 | l282 | footnote_disclaimer |  | 
R1050 | p19 | l317 | footnote_disclaimer |  | 
R1051 | p19 | l318 | footnote_disclaimer |  | 
R1052 | p19 | l321 | footnote_disclaimer |  | 
R1053 | p22 | l346 | footnote_disclaimer |  | 
R1054 | p22 | l363 | footnote_disclaimer |  | 
R1055 | p23 | l371 | footnote_disclaimer |  | 
R1056 | p24 | l385 | footnote_disclaimer |  | 
R1057 | p24 | l386 | footnote_disclaimer |  | 
R1058 | p26 | l444 | footnote_disclaimer |  | 
R1059 | p26 | l445 | footnote_disclaimer |  | 
R1060 | p26 | l446 | footnote_disclaimer |  | 
R1061 | p26 | l447 | footnote_disclaimer |  | 
R1062 | p26 | l415 | footnote_disclaimer |  | 
R1063 | p27 | l455 | footnote_disclaimer |  | 
R1064 | p28 | l476 | footnote_disclaimer |  | 
R1065 | p38 | l632 | footnote_disclaimer |  | 
R1066 | p29 | l494 | footnote_disclaimer |  | 
R1067 | p30 | l520 | footnote_disclaimer | FOOTNOTE_UNRESOLVED | 
R1068 | p32 | l567 | footnote_disclaimer | FOOTNOTE_UNRESOLVED,PAGE_ANCHOR_DEFECT | PAGE_ANCHOR_DEFECT: same as R840
R1069 | p34 | l590 | footnote_disclaimer | FOOTNOTE_UNRESOLVED | 
R1070 | p36 | l615 | footnote_disclaimer | FOOTNOTE_UNRESOLVED | 
R1071 | p39 | l651 | footnote_disclaimer | FOOTNOTE_UNRESOLVED | 
R1072 | p41 | l684 | footnote_disclaimer | FOOTNOTE_UNRESOLVED | 
R1073 | p42 | l703 | footnote_disclaimer | FOOTNOTE_UNRESOLVED | 
R1074 | p43 | l721 | footnote_disclaimer | FOOTNOTE_UNRESOLVED | 
R1075 | p44 | l735 | footnote_disclaimer | FOOTNOTE_UNRESOLVED | 
R1076 | p42 | l708 | footnote_disclaimer |  | 
R1077 | p40 | l660 | footnote_disclaimer |  | 
R1078 | p45 | l742 | footnote_disclaimer |  | 
R1079 | p45 | l743 | footnote_disclaimer |  | 
R1080 | p45 | l744 | footnote_disclaimer |  | 
R1081 | p45 | l739 | footnote_disclaimer |  | 
R1082 | p45 | l752 | footnote_disclaimer |  | 

```yaml
stage: A2-enumerator
company: "RAYMONDREL"
quarter: "q2fy27"
doctype: "presentation"
model: claude-sonnet-5-5
status: complete
ledger_path: "runs/raymondrel-q2fy27/work/ledger_presentation_raymondrel_q2fy27.md"
counts:
  notes: 0
  line_items: 0
  zero_standing: 47
  agenda_items: 0
  auditor_paras: 0
  entities: 98
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 46
  slide_numbers: 860
flags_raised: [ZERO_STANDING, FOOTNOTE_UNRESOLVED, RESTATED, PAGE_ANCHOR_DEFECT, MISSING_FROM_STRUCTURED]
ids_in_structured: 1082
ids_referenced: 1082
orphan_ids: []
missing_from_structured: ["M1 fulltext line 53 (p1): Tel +91 22 6837 3700 (contact data, low materiality)"]
gate_a2: pass
mismatch_note: ""
analyst_note: "Fulltext numeric sweep: 1145 tokens, 44 not found in same-page structured rows; all explained (25 slide footers, 1 serial, 1 statutory year, 5 chart axis ticks, 6 pin/phone, 6 marker-fused unit counts of which 5 covered by R839-R847 and one garbled '~2135%%' on p30 l514 beside R521). Page anchor defect: R840 and R1068 say page 32 but line 567 is on fulltext page 33 (Season 2); A1 should correct. Nine Units Launched footnote markers (R1067-R1075) have no footnote text found. Pages 18, 21, 25 are dividers with no rows; page 13 is image-only (R875). No prior deck, so DROPPED_SLIDE and ENTITY_CHANGE are not assessable."
```
