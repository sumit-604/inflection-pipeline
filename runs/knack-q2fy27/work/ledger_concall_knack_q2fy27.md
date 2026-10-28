# A2 LEDGER: KNACK Q2 FY27 CONCALL (ASR, management tier, numbers unverified)
=== A2 COUNT TEST ===
category: number     grep_count: 472 (A1 header)  sweep_count: 472  match: yes
category: entity     grep_count: 49 (A1 header)  sweep_count: 49  match: yes
category: forward    grep_count: 172 (A1 header)  sweep_count: 172  match: yes
category: date       grep_count: 216 (A1 header)  sweep_count: 216  match: yes
category: qualifier  grep_count: 25 (A1 header)  sweep_count: 25  match: yes
category: all_ids     grep_count: 934  sweep_count: 934  match: yes
category: turns       grep_count: 16 (header turn table T00-T15)  sweep_count: 16  match: yes
category: line_zero   grep_count: 0  sweep_count: 0  match: yes
gate_a2: pass
=== END COUNT TEST ===
ids_in_structured: 934 | ids_referenced_in_ledger: 934 | orphan_ids: [] | match: yes
ASR_DOUBT rows kept visible: 326 (A1 reported 326) | ZERO_STANDING: 0 | line-0 rows: 0
Row format: ROW_ID | category | A2 flags | turn, FULLTEXT line, timestamp. Verbatim values live in the A1 structured file at the ID.
Flags: ASR_DOUBT (carried from A1), ENTITY_VARIANT (CFO named three ways), RESTATED (150 crore contract), ASR_DOUBT_NAME (analyst/firm names garbled).

## 1. PARTICIPANTS (entities R473-R521; speakers not identified by ASR tool)
Management: CMD "Alpish Tulsipai Patel [ASR]" R474; CFO R475 / R476 / R478 (three spellings). IR: Air Factor PR R477. CMD introduced at T01 so no MGMT_ABSENCE; which speaker answers inside T05-T12 is not identified (SPEAKER_UNIDENTIFIED). Analysts: R494-R511.

## 2. SPEAKER TURNS (T00-T15, sequential)
turn | role | speaker/note | first..last row id | rows
T00 | preamble | ASR preamble | R001..R910 (non-contiguous across tables) | 9
T01 | moderator | Moderator opening, intro of CMD and CFO | R473..R911 (non-contiguous across tables) | 14
T02 | management | CMD opening remarks | R007..R916 (non-contiguous across tables) | 87
T03 | management | CFO financial walk-through | R036..R921 (non-contiguous across tables) | 114
T04 | moderator | Moderator opens Q&A | R103..R547 (non-contiguous across tables) | 3
T05 | analyst | Bhavna Israni, Ambit Asset Management | R105..R923 (non-contiguous across tables) | 94
T06 | analyst | Hidansha, Seven Island BMS | R143..R924 (non-contiguous across tables) | 95
T07 | analyst | Aman Chawla, Ash for Holdings | R199..R926 (non-contiguous across tables) | 69
T08 | analyst | UNNAMED at hand-off (Mr. Soura addressed line 308) | R233..R819 (non-contiguous across tables) | 50
T09 | analyst | Hitesh, SBI | R266..R928 (non-contiguous across tables) | 98
T10 | analyst | Prakash Kapadia, NCRST | R319..R931 (non-contiguous across tables) | 75
T11 | analyst | Sandeep Chhabra, Roushi Investments | R351..R932 (non-contiguous across tables) | 99
T12 | analyst | Abhijit (as addressed), INE Alpha Investment Mgmt | R399..R934 (non-contiguous across tables) | 102
T13 | moderator | Moderator: last question, hand to mgmt | R654..R654 (non-contiguous across tables) | 1
T14 | management | Management closing | R472..R908 (non-contiguous across tables) | 23
T15 | moderator | Moderator close | R909..R909 (non-contiguous across tables) | 1
Q&A turns T05-T12 = 8 analyst turns; management prepared remarks T02, T03, T14. Q&A starts 00:11:56 of 00:57:12 (about 79% of call time).

## 3. QUESTION LEDGER (28 questions) [LOOP1]
turn-Q | analyst/firm | topic | mgmt response type | flag | note
T05 | Q1 | Bhavna Israni/Ambit | Q2 volume growth and current utilisation | NUMBER (11,252 MT, 3% growth, 90-91% util) | - | 
T05 | Q2 | Bhavna Israni/Ambit | Volume path in coming quarters given 90% utilisation | QUALITATIVE (5,040 MT added Aug, Q3 better; no volume number) | - | 
T05 | Q3 | Bhavna Israni/Ambit | Price hikes taken in Q2, planned for Q3 | PARTIAL (45-50% contract, 26% RM rise, 7% GM hit; no hike % stated) | - | hike quantum deferred to Q3 if market stabilised
T05 | Q4 | Bhavna Israni/Ambit | Confirm GP/kg down ~10 Rs, EBITDA/kg 36 vs 51.52 | CONFIRMED (absolutely right) | - | analyst-supplied numbers, mgmt assent only
T05 | Q5 | Bhavna Israni/Ambit | YoY volume baseline: Q2 FY26 volume vs 11,252 (cc L164-166; rows R119-R127, R557, R772-R778) | NUMBER (9,927 MT Q2 FY26) | REPEAT_QUESTION (T09-Q2) | added [LOOP1] A5-07
T06 | Q1 | Hidansha/Seven Island BMS | Pinch bottom machinery utilisation | NUMBER (21% of revenue vs 17-18%; 60-70% util) | - | 
T06 | Q2 | Hidansha/Seven Island BMS | MT capacity of pinch bottom in Q2 | DEFLECTED (20-22 mn bags/month; finishing stage not separate capacity) | - | 
T06 | Q3 | Hidansha/Seven Island BMS | Percentage utilisation of pinch bottom | DECLINED (cannot say exactly) | REPEAT_QUESTION (T06-Q1 restated) | no figure given
T06 | Q4 | Hidansha/Seven Island BMS | Output share pinch bottom vs PLW after new 30-32k MT facility | NUMBER (42,000 MT installed to 69-72k; pinch 25-30k later) | - | ASR_DOUBT capacity figures
T07 | Q1 | Aman Chawla/Ash for Holdings | Why large EBITDA/gross margin hit despite pass-through | NUMBER (7% GM, 25-30% price rise, 1.5 month lag) | REPEAT_QUESTION (T05-Q3 theme) | 
T07 | Q2 | Aman Chawla/Ash for Holdings | Timeline to pass costs to contract and non-contract customers | QUALITATIVE (monthly/quarterly revision; no dated timeline) | REPEAT_QUESTION (T05-Q3) | no hard date
T08 | Q1 | UNNAMED (Mr. Soura?) | Pinch bottom market size limited per offer doc; how to manage | QUALITATIVE (72+ countries, dog food, no TAM number) | - | questioner unnamed: ANALYST_UNNAMED
T09 | Q1 | Hitesh/SBI | Q2 volume | NUMBER (11,252 MT) | REPEAT_QUESTION (T05-Q1) | 
T09 | Q2 | Hitesh/SBI | Volume growth YoY | NUMBER (13% YoY volume growth, cc L363; ASR 1, 3%) | REPEAT_QUESTION (T05-Q1) | asked twice, ASR clarity; 9,927 prior-year base belongs to T05-Q5 [LOOP1]
T09 | Q3 | Hitesh/SBI | Is price hike the major driver of revenue growth | CONFIRMED (qualitative) | - | 
T09 | Q4 | Hitesh/SBI | Will Q3 see significant gross margin recovery | HEDGED (99% covered, single one percent depends on market) | REPEAT_QUESTION (T07-Q1, T11-Q2) | no margin number
T09 | Q5 | Hitesh/SBI | Scalability of 150 crore international order | NUMBER (150 cr minimum per year, 3-year contract) | - | five questions, above two-question limit announced at T10
T10 | Q1 | Prakash Kapadia/NCRST | Operating cash flow fall 39 to 22 cr; receivables, tax: one-time? | PARTIAL (26.9 cr inventory build; tax and IPO items; normalisation undated) | - | 
T10 | Q2 | Prakash Kapadia/NCRST | Mexico JV breakeven timing | NUMBER (Q3 almost, Q4 targeted not very committed; 120 MT) | - | commitment hedged
T10 | Q3 | Prakash Kapadia/NCRST | Capacity by next October | DEFLECTED (reply cc L462 is about Mexico capacity, question not answered) | REPEAT_QUESTION (T11-Q3) | recoded from NUMBER [LOOP1]
T11 | Q1 | Sandeep Chhabra/Roushi | Stated questions already answered | NONE | - | no question asked
T11 | Q2 | Sandeep Chhabra/Roushi | Will lost margin be recovered or only improve from Q3 | HEDGED (very small portion recovered) | REPEAT_QUESTION (T09-Q4) | 
T11 | Q3 | Sandeep Chhabra/Roushi | Capacity added between now and October 2027 | NUMBER (rented plant, 1-2 months; rest Oct 2027) | REPEAT_QUESTION (T10-Q3) | 
T11 | Q4 | Sandeep Chhabra/Roushi | Clarify India vs Mexico capacity (5,040 / 400 MT) | NUMBER (400 MT/month installed, 1,890 MT utilised, breakeven 120-130 MT) | - | ASR_DOUBT
T11 | Q5 | Sandeep Chhabra/Roushi | Pinch-machine margin test: 5 machines vs 3 last year, Q3 margin should exceed prior-year Q3 under full pass-through (cc L501-511; rows R383-R388, R871-R878) | CONFIRMED (perfectly okay; no margin number) | - | added [LOOP1] A5-07
T12 | Q1 | Abhijit/INE Alpha | Percent vs absolute margin under cost pass-through | QUALITATIVE (30% jump, 1.5 month lag) | REPEAT_QUESTION (T07-Q1) | 
T12 | Q2 | Abhijit/INE Alpha | Can percent margins return to prior levels | HEDGED (not 100% we can get it) | REPEAT_QUESTION (T09-Q4, T11-Q2) | 
T12 | Q3 | Abhijit/INE Alpha | EBITDA per kg Q1 55 vs Q2 45; return to 54 in two quarters | NUMBER (54 Rs/kg in next two quarters; yearly target on track) | - | forward commitment, ASR_DOUBT
Totals: questions 28; REPEAT_QUESTION 12; answered with number 12; hedged/qualitative/partial/deflected 11; confirmed 3; [LOOP1] declined 1 (T06-Q3); none 1 (T11-Q1).
Repeat clusters: volume/utilisation (T05-Q1, T05-Q5, T09-Q1, T09-Q2); pass-through timeline (T05-Q3, T07-Q1, T07-Q2, T12-Q1); Q3 margin recovery (T09-Q4, T11-Q2, T12-Q2); capacity to Oct 2027 (T10-Q3, T11-Q3). No MGMT_ABSENCE. Announced two-question limit (T10 hand-off) exceeded by T09 (5), T10 (3), T11 (4), T12 (3) by count of parts.

## NUMBER_NONMGMT_MODERATOR_PREAMBLE (8 rows)
R001 | number_nonmgmt_moderator_preamble | - | T00 line 39 -
R002 | number_nonmgmt_moderator_preamble | - | T00 line 39 -
R003 | number_nonmgmt_moderator_preamble | - | T00 line 39 -
R004 | number_nonmgmt_moderator_preamble | - | T00 line 39 -
R005 | number_nonmgmt_moderator_preamble | - | T00 line 39 -
R006 | number_nonmgmt_moderator_preamble | - | T00 line 39 -
R103 | number_nonmgmt_moderator_preamble | - | T04 line 129 00:11:39
R104 | number_nonmgmt_moderator_preamble | - | T04 line 130 00:11:42

## MGMT_NUMBER (464 rows)
R007 | mgmt_number | ASR_DOUBT | T02 line 53 00:01:15
R008 | mgmt_number | ASR_DOUBT | T02 line 57 00:02:09
R009 | mgmt_number | - | T02 line 58 00:02:22
R010 | mgmt_number | - | T02 line 60 00:02:39
R011 | mgmt_number | - | T02 line 63 00:02:58
R012 | mgmt_number | - | T02 line 64 00:03:03
R013 | mgmt_number | - | T02 line 64 00:03:03
R014 | mgmt_number | - | T02 line 67 00:03:25
R015 | mgmt_number | - | T02 line 69 00:03:39
R016 | mgmt_number | - | T02 line 71 00:03:54
R017 | mgmt_number | - | T02 line 72 00:04:01
R018 | mgmt_number | ASR_DOUBT | T02 line 76 00:04:27
R019 | mgmt_number | ASR_DOUBT | T02 line 76 00:04:27
R020 | mgmt_number | ASR_DOUBT | T02 line 76 00:04:27
R021 | mgmt_number | ASR_DOUBT | T02 line 76 00:04:27
R022 | mgmt_number | ASR_DOUBT | T02 line 77 00:04:39
R023 | mgmt_number | ASR_DOUBT | T02 line 77 00:04:39
R024 | mgmt_number | ASR_DOUBT | T02 line 77 00:04:39
R025 | mgmt_number | ASR_DOUBT | T02 line 77 00:04:39
R026 | mgmt_number | ASR_DOUBT | T02 line 79 00:04:55
R027 | mgmt_number | ASR_DOUBT | T02 line 79 00:04:55
R028 | mgmt_number | ASR_DOUBT | T02 line 79 00:04:55
R029 | mgmt_number | ASR_DOUBT | T02 line 80 00:05:02
R030 | mgmt_number | ASR_DOUBT | T02 line 80 00:05:02
R031 | mgmt_number | - | T02 line 88 00:05:43
R032 | mgmt_number | - | T02 line 88 00:05:43
R033 | mgmt_number | RESTATED | T02 line 89 00:05:51
R034 | mgmt_number | - | T02 line 89 00:05:51
R035 | mgmt_number | - | T02 line 89 00:05:51
R036 | mgmt_number | - | T03 line 99 00:06:47
R037 | mgmt_number | - | T03 line 100 00:06:56
R038 | mgmt_number | - | T03 line 101 00:07:04
R039 | mgmt_number | - | T03 line 101 00:07:04
R040 | mgmt_number | - | T03 line 101 00:07:04
R041 | mgmt_number | - | T03 line 101 00:07:04
R042 | mgmt_number | ASR_DOUBT | T03 line 102 00:07:19
R043 | mgmt_number | ASR_DOUBT | T03 line 102 00:07:19
R044 | mgmt_number | ASR_DOUBT | T03 line 102 00:07:19
R045 | mgmt_number | ASR_DOUBT | T03 line 102 00:07:19
R046 | mgmt_number | ASR_DOUBT | T03 line 102 00:07:19
R047 | mgmt_number | ASR_DOUBT | T03 line 106 00:07:46
R048 | mgmt_number | ASR_DOUBT | T03 line 106 00:07:46
R049 | mgmt_number | ASR_DOUBT | T03 line 106 00:07:46
R050 | mgmt_number | ASR_DOUBT | T03 line 107 00:07:54
R051 | mgmt_number | ASR_DOUBT | T03 line 107 00:07:54
R052 | mgmt_number | ASR_DOUBT | T03 line 107 00:07:54
R053 | mgmt_number | ASR_DOUBT | T03 line 107 00:07:54
R054 | mgmt_number | ASR_DOUBT | T03 line 107 00:07:54
R055 | mgmt_number | ASR_DOUBT | T03 line 108 00:08:03
R056 | mgmt_number | ASR_DOUBT | T03 line 108 00:08:03
R057 | mgmt_number | ASR_DOUBT | T03 line 108 00:08:03
R058 | mgmt_number | - | T03 line 110 00:08:19
R059 | mgmt_number | - | T03 line 110 00:08:19
R060 | mgmt_number | - | T03 line 111 00:08:26
R061 | mgmt_number | - | T03 line 111 00:08:26
R062 | mgmt_number | ASR_DOUBT | T03 line 112 00:08:34
R063 | mgmt_number | ASR_DOUBT | T03 line 112 00:08:34
R064 | mgmt_number | ASR_DOUBT | T03 line 112 00:08:34
R065 | mgmt_number | ASR_DOUBT | T03 line 112 00:08:34
R066 | mgmt_number | ASR_DOUBT | T03 line 112 00:08:34
R067 | mgmt_number | ASR_DOUBT | T03 line 112 00:08:34
R068 | mgmt_number | ASR_DOUBT | T03 line 112 00:08:34
R069 | mgmt_number | ASR_DOUBT | T03 line 113 00:08:43
R070 | mgmt_number | ASR_DOUBT | T03 line 113 00:08:43
R071 | mgmt_number | ASR_DOUBT | T03 line 113 00:08:43
R072 | mgmt_number | ASR_DOUBT | T03 line 113 00:08:43
R073 | mgmt_number | ASR_DOUBT | T03 line 114 00:08:54
R074 | mgmt_number | ASR_DOUBT | T03 line 114 00:08:54
R075 | mgmt_number | ASR_DOUBT | T03 line 114 00:08:54
R076 | mgmt_number | ASR_DOUBT | T03 line 114 00:08:54
R077 | mgmt_number | - | T03 line 115 00:09:02
R078 | mgmt_number | ASR_DOUBT | T03 line 116 00:09:08
R079 | mgmt_number | ASR_DOUBT | T03 line 117 00:09:18
R080 | mgmt_number | ASR_DOUBT | T03 line 117 00:09:18
R081 | mgmt_number | ASR_DOUBT | T03 line 117 00:09:18
R082 | mgmt_number | ASR_DOUBT | T03 line 117 00:09:18
R083 | mgmt_number | ASR_DOUBT | T03 line 117 00:09:18
R084 | mgmt_number | ASR_DOUBT | T03 line 117 00:09:18
R085 | mgmt_number | ASR_DOUBT | T03 line 118 00:09:56
R086 | mgmt_number | ASR_DOUBT | T03 line 119 00:10:00
R087 | mgmt_number | ASR_DOUBT | T03 line 119 00:10:00
R088 | mgmt_number | ASR_DOUBT | T03 line 122 00:10:23
R089 | mgmt_number | ASR_DOUBT | T03 line 122 00:10:23
R090 | mgmt_number | ASR_DOUBT | T03 line 122 00:10:23
R091 | mgmt_number | ASR_DOUBT | T03 line 122 00:10:23
R092 | mgmt_number | ASR_DOUBT | T03 line 123 00:10:32
R093 | mgmt_number | ASR_DOUBT | T03 line 123 00:10:32
R094 | mgmt_number | ASR_DOUBT | T03 line 123 00:10:32
R095 | mgmt_number | ASR_DOUBT | T03 line 124 00:10:37
R096 | mgmt_number | ASR_DOUBT | T03 line 124 00:10:37
R097 | mgmt_number | ASR_DOUBT | T03 line 124 00:10:37
R098 | mgmt_number | ASR_DOUBT | T03 line 124 00:10:37
R099 | mgmt_number | ASR_DOUBT | T03 line 125 00:10:47
R100 | mgmt_number | ASR_DOUBT | T03 line 125 00:10:47
R101 | mgmt_number | ASR_DOUBT | T03 line 125 00:10:47
R102 | mgmt_number | ASR_DOUBT | T03 line 127 00:11:02
R105 | mgmt_number | ASR_DOUBT | T05 line 138 00:12:27
R106 | mgmt_number | ASR_DOUBT | T05 line 138 00:12:27
R107 | mgmt_number | ASR_DOUBT | T05 line 139 00:12:40
R108 | mgmt_number | - | T05 line 140 00:12:47
R109 | mgmt_number | ASR_DOUBT | T05 line 142 00:12:59
R110 | mgmt_number | - | T05 line 144 00:13:16
R111 | mgmt_number | - | T05 line 152 00:13:54
R112 | mgmt_number | - | T05 line 152 00:13:54
R113 | mgmt_number | ASR_DOUBT | T05 line 156 00:14:18
R114 | mgmt_number | ASR_DOUBT | T05 line 157 00:14:23
R115 | mgmt_number | - | T05 line 159 00:14:33
R116 | mgmt_number | - | T05 line 161 00:14:56
R117 | mgmt_number | - | T05 line 161 00:14:56
R118 | mgmt_number | ASR_DOUBT | T05 line 163 00:15:07
R119 | mgmt_number | ASR_DOUBT | T05 line 164 00:15:14
R120 | mgmt_number | ASR_DOUBT | T05 line 164 00:15:14
R121 | mgmt_number | ASR_DOUBT | T05 line 164 00:15:14
R122 | mgmt_number | ASR_DOUBT | T05 line 164 00:15:14
R123 | mgmt_number | - | T05 line 165 00:15:51
R124 | mgmt_number | ASR_DOUBT | T05 line 166 00:15:53
R125 | mgmt_number | ASR_DOUBT | T05 line 166 00:15:53
R126 | mgmt_number | ASR_DOUBT | T05 line 166 00:15:53
R127 | mgmt_number | ASR_DOUBT | T05 line 166 00:15:53
R128 | mgmt_number | - | T05 line 167 00:16:05
R129 | mgmt_number | ASR_DOUBT | T05 line 171 00:16:34
R130 | mgmt_number | ASR_DOUBT | T05 line 171 00:16:34
R131 | mgmt_number | ASR_DOUBT | T05 line 171 00:16:34
R132 | mgmt_number | - | T05 line 172 00:16:41
R133 | mgmt_number | - | T05 line 172 00:16:41
R134 | mgmt_number | - | T05 line 172 00:16:41
R135 | mgmt_number | - | T05 line 172 00:16:41
R136 | mgmt_number | ASR_DOUBT | T05 line 173 00:16:46
R137 | mgmt_number | ASR_DOUBT | T05 line 173 00:16:46
R138 | mgmt_number | ASR_DOUBT | T05 line 173 00:16:46
R139 | mgmt_number | ASR_DOUBT | T05 line 173 00:16:46
R140 | mgmt_number | ASR_DOUBT | T05 line 175 00:17:00
R141 | mgmt_number | ASR_DOUBT | T05 line 175 00:17:00
R142 | mgmt_number | ASR_DOUBT | T05 line 175 00:17:00
R143 | mgmt_number | - | T06 line 177 00:17:12
R144 | mgmt_number | - | T06 line 178 00:17:30
R145 | mgmt_number | - | T06 line 180 00:17:49
R146 | mgmt_number | - | T06 line 181 00:17:53
R147 | mgmt_number | - | T06 line 181 00:17:53
R148 | mgmt_number | ASR_DOUBT | T06 line 182 00:18:01
R149 | mgmt_number | ASR_DOUBT | T06 line 182 00:18:01
R150 | mgmt_number | - | T06 line 183 00:18:09
R151 | mgmt_number | - | T06 line 183 00:18:09
R152 | mgmt_number | ASR_DOUBT | T06 line 186 00:18:24
R153 | mgmt_number | ASR_DOUBT | T06 line 186 00:18:24
R154 | mgmt_number | ASR_DOUBT | T06 line 186 00:18:24
R155 | mgmt_number | - | T06 line 188 00:18:37
R156 | mgmt_number | - | T06 line 189 00:18:43
R157 | mgmt_number | - | T06 line 190 00:18:54
R158 | mgmt_number | ASR_DOUBT | T06 line 191 00:19:03
R159 | mgmt_number | - | T06 line 195 00:19:28
R160 | mgmt_number | ASR_DOUBT | T06 line 197 00:19:42
R161 | mgmt_number | ASR_DOUBT | T06 line 197 00:19:42
R162 | mgmt_number | ASR_DOUBT | T06 line 197 00:19:42
R163 | mgmt_number | ASR_DOUBT | T06 line 199 00:20:00
R164 | mgmt_number | - | T06 line 200 00:20:08
R165 | mgmt_number | - | T06 line 204 00:20:35
R166 | mgmt_number | ASR_DOUBT | T06 line 205 00:20:42
R167 | mgmt_number | ASR_DOUBT | T06 line 205 00:20:42
R168 | mgmt_number | ASR_DOUBT | T06 line 205 00:20:42
R169 | mgmt_number | ASR_DOUBT | T06 line 206 00:20:50
R170 | mgmt_number | ASR_DOUBT | T06 line 206 00:20:50
R171 | mgmt_number | - | T06 line 211 00:21:26
R172 | mgmt_number | - | T06 line 212 00:21:33
R173 | mgmt_number | - | T06 line 212 00:21:33
R174 | mgmt_number | - | T06 line 216 00:21:57
R175 | mgmt_number | - | T06 line 228 00:22:38
R176 | mgmt_number | ASR_DOUBT | T06 line 229 00:22:46
R177 | mgmt_number | ASR_DOUBT | T06 line 229 00:22:46
R178 | mgmt_number | ASR_DOUBT | T06 line 229 00:22:46
R179 | mgmt_number | ASR_DOUBT | T06 line 232 00:23:02
R180 | mgmt_number | ASR_DOUBT | T06 line 232 00:23:02
R181 | mgmt_number | ASR_DOUBT | T06 line 233 00:23:08
R182 | mgmt_number | ASR_DOUBT | T06 line 233 00:23:08
R183 | mgmt_number | ASR_DOUBT | T06 line 234 00:23:13
R184 | mgmt_number | ASR_DOUBT | T06 line 234 00:23:13
R185 | mgmt_number | ASR_DOUBT | T06 line 234 00:23:13
R186 | mgmt_number | - | T06 line 236 00:23:23
R187 | mgmt_number | - | T06 line 236 00:23:23
R188 | mgmt_number | - | T06 line 236 00:23:23
R189 | mgmt_number | - | T06 line 238 00:23:34
R190 | mgmt_number | ASR_DOUBT | T06 line 240 00:23:42
R191 | mgmt_number | ASR_DOUBT | T06 line 240 00:23:42
R192 | mgmt_number | ASR_DOUBT | T06 line 240 00:23:42
R193 | mgmt_number | ASR_DOUBT | T06 line 240 00:23:42
R194 | mgmt_number | ASR_DOUBT | T06 line 241 00:23:52
R195 | mgmt_number | ASR_DOUBT | T06 line 241 00:23:52
R196 | mgmt_number | ASR_DOUBT | T06 line 241 00:23:52
R197 | mgmt_number | ASR_DOUBT | T06 line 241 00:23:52
R198 | mgmt_number | ASR_DOUBT | T06 line 241 00:23:52
R199 | mgmt_number | - | T07 line 244 00:24:10
R200 | mgmt_number | - | T07 line 249 00:24:50
R201 | mgmt_number | - | T07 line 249 00:24:50
R202 | mgmt_number | - | T07 line 254 00:25:22
R203 | mgmt_number | - | T07 line 257 00:25:38
R204 | mgmt_number | - | T07 line 257 00:25:38
R205 | mgmt_number | ASR_DOUBT | T07 line 258 00:25:47
R206 | mgmt_number | ASR_DOUBT | T07 line 258 00:25:47
R207 | mgmt_number | - | T07 line 261 00:26:08
R208 | mgmt_number | - | T07 line 261 00:26:08
R209 | mgmt_number | - | T07 line 261 00:26:08
R210 | mgmt_number | - | T07 line 264 00:27:00
R211 | mgmt_number | - | T07 line 264 00:27:00
R212 | mgmt_number | - | T07 line 266 00:27:12
R213 | mgmt_number | - | T07 line 266 00:27:12
R214 | mgmt_number | - | T07 line 266 00:27:12
R215 | mgmt_number | ASR_DOUBT | T07 line 271 00:27:42
R216 | mgmt_number | ASR_DOUBT | T07 line 271 00:27:42
R217 | mgmt_number | ASR_DOUBT | T07 line 271 00:27:42
R218 | mgmt_number | ASR_DOUBT | T07 line 273 00:27:55
R219 | mgmt_number | ASR_DOUBT | T07 line 273 00:27:55
R220 | mgmt_number | - | T07 line 274 00:28:04
R221 | mgmt_number | - | T07 line 274 00:28:04
R222 | mgmt_number | - | T07 line 278 00:28:40
R223 | mgmt_number | - | T07 line 285 00:29:18
R224 | mgmt_number | - | T07 line 285 00:29:18
R225 | mgmt_number | ASR_DOUBT | T07 line 286 00:29:24
R226 | mgmt_number | ASR_DOUBT | T07 line 286 00:29:24
R227 | mgmt_number | ASR_DOUBT | T07 line 286 00:29:24
R228 | mgmt_number | ASR_DOUBT | T07 line 286 00:29:24
R229 | mgmt_number | ASR_DOUBT | T07 line 286 00:29:24
R230 | mgmt_number | ASR_DOUBT | T07 line 287 00:29:29
R231 | mgmt_number | ASR_DOUBT | T07 line 287 00:29:29
R232 | mgmt_number | - | T07 line 292 00:29:55
R233 | mgmt_number | - | T08 line 296 00:30:50
R234 | mgmt_number | ASR_DOUBT | T08 line 297 00:30:54
R235 | mgmt_number | - | T08 line 299 00:31:01
R236 | mgmt_number | - | T08 line 300 00:31:06
R237 | mgmt_number | ASR_DOUBT | T08 line 304 00:31:27
R238 | mgmt_number | ASR_DOUBT | T08 line 313 00:32:14
R239 | mgmt_number | ASR_DOUBT | T08 line 315 00:32:25
R240 | mgmt_number | ASR_DOUBT | T08 line 316 00:32:30
R241 | mgmt_number | - | T08 line 323 00:33:00
R242 | mgmt_number | ASR_DOUBT | T08 line 324 00:33:06
R243 | mgmt_number | ASR_DOUBT | T08 line 324 00:33:06
R244 | mgmt_number | ASR_DOUBT | T08 line 324 00:33:06
R245 | mgmt_number | ASR_DOUBT | T08 line 325 00:33:10
R246 | mgmt_number | ASR_DOUBT | T08 line 325 00:33:10
R247 | mgmt_number | ASR_DOUBT | T08 line 325 00:33:10
R248 | mgmt_number | ASR_DOUBT | T08 line 325 00:33:10
R249 | mgmt_number | ASR_DOUBT | T08 line 325 00:33:10
R250 | mgmt_number | ASR_DOUBT | T08 line 327 00:33:21
R251 | mgmt_number | ASR_DOUBT | T08 line 328 00:33:26
R252 | mgmt_number | ASR_DOUBT | T08 line 328 00:33:26
R253 | mgmt_number | ASR_DOUBT | T08 line 328 00:33:26
R254 | mgmt_number | ASR_DOUBT | T08 line 328 00:33:26
R255 | mgmt_number | ASR_DOUBT | T08 line 328 00:33:26
R256 | mgmt_number | ASR_DOUBT | T08 line 328 00:33:26
R257 | mgmt_number | ASR_DOUBT | T08 line 330 00:33:38
R258 | mgmt_number | ASR_DOUBT | T08 line 330 00:33:38
R259 | mgmt_number | ASR_DOUBT | T08 line 330 00:33:38
R260 | mgmt_number | - | T08 line 331 00:33:44
R261 | mgmt_number | - | T08 line 332 00:33:49
R262 | mgmt_number | - | T08 line 334 00:34:07
R263 | mgmt_number | ASR_DOUBT | T08 line 339 00:34:31
R264 | mgmt_number | ASR_DOUBT | T08 line 339 00:34:31
R265 | mgmt_number | - | T08 line 341 00:34:43
R266 | mgmt_number | - | T09 line 355 00:35:14
R267 | mgmt_number | - | T09 line 355 00:35:14
R268 | mgmt_number | ASR_DOUBT | T09 line 356 00:35:23
R269 | mgmt_number | ASR_DOUBT | T09 line 356 00:35:23
R270 | mgmt_number | ASR_DOUBT | T09 line 356 00:35:23
R271 | mgmt_number | ASR_DOUBT | T09 line 360 00:35:39
R272 | mgmt_number | ASR_DOUBT | T09 line 361 00:35:42
R273 | mgmt_number | ASR_DOUBT | T09 line 361 00:35:42
R274 | mgmt_number | ASR_DOUBT | T09 line 363 00:35:59
R275 | mgmt_number | ASR_DOUBT | T09 line 364 00:36:01
R276 | mgmt_number | ASR_DOUBT | T09 line 364 00:36:01
R277 | mgmt_number | ASR_DOUBT | T09 line 376 00:36:51
R278 | mgmt_number | - | T09 line 384 00:37:38
R279 | mgmt_number | - | T09 line 384 00:37:38
R280 | mgmt_number | - | T09 line 384 00:37:38
R281 | mgmt_number | - | T09 line 386 00:37:55
R282 | mgmt_number | - | T09 line 386 00:37:55
R283 | mgmt_number | ASR_DOUBT | T09 line 388 00:38:07
R284 | mgmt_number | ASR_DOUBT | T09 line 388 00:38:07
R285 | mgmt_number | ASR_DOUBT | T09 line 389 00:38:14
R286 | mgmt_number | ASR_DOUBT | T09 line 389 00:38:14
R287 | mgmt_number | ASR_DOUBT | T09 line 389 00:38:14
R288 | mgmt_number | ASR_DOUBT | T09 line 389 00:38:14
R289 | mgmt_number | ASR_DOUBT | T09 line 389 00:38:14
R290 | mgmt_number | ASR_DOUBT | T09 line 390 00:38:22
R291 | mgmt_number | ASR_DOUBT | T09 line 390 00:38:22
R292 | mgmt_number | ASR_DOUBT | T09 line 390 00:38:22
R293 | mgmt_number | ASR_DOUBT | T09 line 390 00:38:22
R294 | mgmt_number | - | T09 line 392 00:38:35
R295 | mgmt_number | - | T09 line 392 00:38:35
R296 | mgmt_number | - | T09 line 394 00:38:47
R297 | mgmt_number | - | T09 line 394 00:38:47
R298 | mgmt_number | ASR_DOUBT | T09 line 395 00:38:52
R299 | mgmt_number | ASR_DOUBT | T09 line 395 00:38:52
R300 | mgmt_number | - | T09 line 396 00:38:56
R301 | mgmt_number | ASR_DOUBT,RESTATED | T09 line 397 00:39:06
R302 | mgmt_number | ASR_DOUBT | T09 line 397 00:39:06
R303 | mgmt_number | - | T09 line 398 00:39:14
R304 | mgmt_number | - | T09 line 402 00:39:32
R305 | mgmt_number | - | T09 line 405 00:39:43
R306 | mgmt_number | - | T09 line 405 00:39:43
R307 | mgmt_number | ASR_DOUBT,RESTATED | T09 line 406 00:39:45
R308 | mgmt_number | ASR_DOUBT | T09 line 406 00:39:45
R309 | mgmt_number | - | T09 line 407 00:39:48
R310 | mgmt_number | ASR_DOUBT,RESTATED | T09 line 408 00:39:50
R311 | mgmt_number | ASR_DOUBT | T09 line 408 00:39:50
R312 | mgmt_number | ASR_DOUBT | T09 line 410 00:39:56
R313 | mgmt_number | ASR_DOUBT | T09 line 410 00:39:56
R314 | mgmt_number | RESTATED | T09 line 411 00:40:00
R315 | mgmt_number | ASR_DOUBT,RESTATED | T09 line 412 00:40:09
R316 | mgmt_number | ASR_DOUBT | T09 line 412 00:40:09
R317 | mgmt_number | ASR_DOUBT | T09 line 412 00:40:09
R318 | mgmt_number | ASR_DOUBT | T09 line 412 00:40:09
R319 | mgmt_number | - | T10 line 422 00:41:01
R320 | mgmt_number | ASR_DOUBT | T10 line 425 00:41:17
R321 | mgmt_number | ASR_DOUBT | T10 line 425 00:41:17
R322 | mgmt_number | - | T10 line 426 00:41:24
R323 | mgmt_number | - | T10 line 426 00:41:24
R324 | mgmt_number | - | T10 line 426 00:41:24
R325 | mgmt_number | - | T10 line 427 00:41:31
R326 | mgmt_number | ASR_DOUBT | T10 line 436 00:42:27
R327 | mgmt_number | ASR_DOUBT | T10 line 436 00:42:27
R328 | mgmt_number | - | T10 line 439 00:42:48
R329 | mgmt_number | - | T10 line 439 00:42:48
R330 | mgmt_number | ASR_DOUBT | T10 line 440 00:42:57
R331 | mgmt_number | - | T10 line 441 00:43:02
R332 | mgmt_number | ASR_DOUBT | T10 line 444 00:43:20
R333 | mgmt_number | ASR_DOUBT | T10 line 445 00:43:27
R334 | mgmt_number | ASR_DOUBT | T10 line 447 00:43:38
R335 | mgmt_number | ASR_DOUBT | T10 line 447 00:43:38
R336 | mgmt_number | - | T10 line 453 00:44:21
R337 | mgmt_number | - | T10 line 454 00:44:27
R338 | mgmt_number | - | T10 line 454 00:44:27
R339 | mgmt_number | - | T10 line 456 00:44:38
R340 | mgmt_number | - | T10 line 457 00:44:45
R341 | mgmt_number | - | T10 line 460 00:45:01
R342 | mgmt_number | ASR_DOUBT | T10 line 462 00:45:08
R343 | mgmt_number | ASR_DOUBT | T10 line 462 00:45:08
R344 | mgmt_number | ASR_DOUBT | T10 line 462 00:45:08
R345 | mgmt_number | ASR_DOUBT | T10 line 463 00:45:13
R346 | mgmt_number | ASR_DOUBT | T10 line 463 00:45:13
R347 | mgmt_number | ASR_DOUBT | T10 line 464 00:45:19
R348 | mgmt_number | ASR_DOUBT | T10 line 464 00:45:19
R349 | mgmt_number | ASR_DOUBT | T10 line 464 00:45:19
R350 | mgmt_number | ASR_DOUBT | T10 line 464 00:45:19
R351 | mgmt_number | - | T11 line 476 00:45:52
R352 | mgmt_number | - | T11 line 478 00:46:05
R353 | mgmt_number | ASR_DOUBT | T11 line 481 00:46:16
R354 | mgmt_number | ASR_DOUBT | T11 line 481 00:46:16
R355 | mgmt_number | ASR_DOUBT | T11 line 481 00:46:16
R356 | mgmt_number | ASR_DOUBT | T11 line 481 00:46:16
R357 | mgmt_number | ASR_DOUBT | T11 line 482 00:46:22
R358 | mgmt_number | ASR_DOUBT | T11 line 482 00:46:22
R359 | mgmt_number | ASR_DOUBT | T11 line 482 00:46:22
R360 | mgmt_number | ASR_DOUBT | T11 line 488 00:46:57
R361 | mgmt_number | ASR_DOUBT | T11 line 488 00:46:57
R362 | mgmt_number | ASR_DOUBT | T11 line 489 00:47:01
R363 | mgmt_number | ASR_DOUBT | T11 line 489 00:47:01
R364 | mgmt_number | ASR_DOUBT | T11 line 489 00:47:01
R365 | mgmt_number | ASR_DOUBT | T11 line 489 00:47:01
R366 | mgmt_number | ASR_DOUBT | T11 line 490 00:47:08
R367 | mgmt_number | ASR_DOUBT | T11 line 490 00:47:08
R368 | mgmt_number | ASR_DOUBT | T11 line 490 00:47:08
R369 | mgmt_number | ASR_DOUBT | T11 line 490 00:47:08
R370 | mgmt_number | ASR_DOUBT | T11 line 490 00:47:08
R371 | mgmt_number | ASR_DOUBT | T11 line 490 00:47:08
R372 | mgmt_number | ASR_DOUBT | T11 line 490 00:47:08
R373 | mgmt_number | ASR_DOUBT | T11 line 490 00:47:08
R374 | mgmt_number | ASR_DOUBT | T11 line 491 00:47:14
R375 | mgmt_number | ASR_DOUBT | T11 line 491 00:47:14
R376 | mgmt_number | - | T11 line 494 00:47:37
R377 | mgmt_number | - | T11 line 494 00:47:37
R378 | mgmt_number | - | T11 line 494 00:47:37
R379 | mgmt_number | - | T11 line 494 00:47:37
R380 | mgmt_number | - | T11 line 496 00:47:52
R381 | mgmt_number | - | T11 line 496 00:47:52
R382 | mgmt_number | - | T11 line 500 00:48:14
R383 | mgmt_number | - | T11 line 501 00:48:19
R384 | mgmt_number | - | T11 line 502 00:48:29
R385 | mgmt_number | - | T11 line 503 00:48:36
R386 | mgmt_number | - | T11 line 504 00:48:44
R387 | mgmt_number | - | T11 line 510 00:49:18
R388 | mgmt_number | - | T11 line 510 00:49:18
R389 | mgmt_number | - | T11 line 512 00:49:28
R390 | mgmt_number | ASR_DOUBT | T11 line 513 00:49:33
R391 | mgmt_number | ASR_DOUBT | T11 line 513 00:49:33
R392 | mgmt_number | ASR_DOUBT | T11 line 513 00:49:33
R393 | mgmt_number | ASR_DOUBT | T11 line 513 00:49:33
R394 | mgmt_number | ASR_DOUBT | T11 line 513 00:49:33
R395 | mgmt_number | ASR_DOUBT | T11 line 514 00:49:38
R396 | mgmt_number | ASR_DOUBT | T11 line 514 00:49:38
R397 | mgmt_number | - | T11 line 517 00:49:53
R398 | mgmt_number | - | T11 line 517 00:49:53
R399 | mgmt_number | ASR_DOUBT | T12 line 521 00:50:21
R400 | mgmt_number | ASR_DOUBT | T12 line 521 00:50:21
R401 | mgmt_number | - | T12 line 522 00:50:27
R402 | mgmt_number | - | T12 line 522 00:50:27
R403 | mgmt_number | - | T12 line 522 00:50:27
R404 | mgmt_number | - | T12 line 522 00:50:27
R405 | mgmt_number | - | T12 line 524 00:50:34
R406 | mgmt_number | - | T12 line 524 00:50:34
R407 | mgmt_number | - | T12 line 525 00:50:42
R408 | mgmt_number | - | T12 line 525 00:50:42
R409 | mgmt_number | - | T12 line 528 00:50:53
R410 | mgmt_number | - | T12 line 533 00:51:19
R411 | mgmt_number | - | T12 line 533 00:51:19
R412 | mgmt_number | - | T12 line 533 00:51:19
R413 | mgmt_number | ASR_DOUBT | T12 line 534 00:51:23
R414 | mgmt_number | ASR_DOUBT | T12 line 534 00:51:23
R415 | mgmt_number | ASR_DOUBT | T12 line 534 00:51:23
R416 | mgmt_number | ASR_DOUBT | T12 line 534 00:51:23
R417 | mgmt_number | ASR_DOUBT | T12 line 535 00:51:30
R418 | mgmt_number | ASR_DOUBT | T12 line 535 00:51:30
R419 | mgmt_number | ASR_DOUBT | T12 line 535 00:51:30
R420 | mgmt_number | ASR_DOUBT | T12 line 536 00:51:38
R421 | mgmt_number | ASR_DOUBT | T12 line 536 00:51:38
R422 | mgmt_number | ASR_DOUBT | T12 line 536 00:51:38
R423 | mgmt_number | ASR_DOUBT | T12 line 536 00:51:38
R424 | mgmt_number | ASR_DOUBT | T12 line 536 00:51:38
R425 | mgmt_number | ASR_DOUBT | T12 line 537 00:51:46
R426 | mgmt_number | ASR_DOUBT | T12 line 537 00:51:46
R427 | mgmt_number | ASR_DOUBT | T12 line 537 00:51:46
R428 | mgmt_number | ASR_DOUBT | T12 line 537 00:51:46
R429 | mgmt_number | ASR_DOUBT | T12 line 538 00:51:54
R430 | mgmt_number | ASR_DOUBT | T12 line 538 00:51:54
R431 | mgmt_number | ASR_DOUBT | T12 line 538 00:51:54
R432 | mgmt_number | ASR_DOUBT | T12 line 538 00:51:54
R433 | mgmt_number | - | T12 line 540 00:52:07
R434 | mgmt_number | - | T12 line 548 00:53:00
R435 | mgmt_number | - | T12 line 551 00:53:18
R436 | mgmt_number | ASR_DOUBT | T12 line 552 00:53:25
R437 | mgmt_number | ASR_DOUBT | T12 line 552 00:53:25
R438 | mgmt_number | ASR_DOUBT | T12 line 552 00:53:25
R439 | mgmt_number | ASR_DOUBT | T12 line 552 00:53:25
R440 | mgmt_number | ASR_DOUBT | T12 line 552 00:53:25
R441 | mgmt_number | ASR_DOUBT | T12 line 552 00:53:25
R442 | mgmt_number | ASR_DOUBT | T12 line 553 00:53:30
R443 | mgmt_number | ASR_DOUBT | T12 line 553 00:53:30
R444 | mgmt_number | ASR_DOUBT | T12 line 553 00:53:30
R445 | mgmt_number | ASR_DOUBT | T12 line 553 00:53:30
R446 | mgmt_number | ASR_DOUBT | T12 line 553 00:53:30
R447 | mgmt_number | ASR_DOUBT | T12 line 553 00:53:30
R448 | mgmt_number | - | T12 line 559 00:53:58
R449 | mgmt_number | - | T12 line 561 00:54:12
R450 | mgmt_number | - | T12 line 561 00:54:12
R451 | mgmt_number | - | T12 line 561 00:54:12
R452 | mgmt_number | ASR_DOUBT | T12 line 562 00:54:18
R453 | mgmt_number | ASR_DOUBT | T12 line 562 00:54:18
R454 | mgmt_number | ASR_DOUBT | T12 line 562 00:54:18
R455 | mgmt_number | ASR_DOUBT | T12 line 562 00:54:18
R456 | mgmt_number | ASR_DOUBT | T12 line 562 00:54:18
R457 | mgmt_number | ASR_DOUBT | T12 line 563 00:54:24
R458 | mgmt_number | ASR_DOUBT | T12 line 563 00:54:24
R459 | mgmt_number | ASR_DOUBT | T12 line 563 00:54:24
R460 | mgmt_number | ASR_DOUBT | T12 line 564 00:54:28
R461 | mgmt_number | ASR_DOUBT | T12 line 565 00:54:29
R462 | mgmt_number | ASR_DOUBT | T12 line 565 00:54:29
R463 | mgmt_number | ASR_DOUBT | T12 line 566 00:54:31
R464 | mgmt_number | ASR_DOUBT | T12 line 568 00:54:33
R465 | mgmt_number | ASR_DOUBT | T12 line 568 00:54:33
R466 | mgmt_number | ASR_DOUBT | T12 line 569 00:54:34
R467 | mgmt_number | ASR_DOUBT | T12 line 569 00:54:34
R468 | mgmt_number | ASR_DOUBT | T12 line 569 00:54:34
R469 | mgmt_number | ASR_DOUBT | T12 line 570 00:54:35
R470 | mgmt_number | ASR_DOUBT | T12 line 570 00:54:35
R471 | mgmt_number | - | T12 line 573 00:54:52
R472 | mgmt_number | ASR_DOUBT | T14 line 581 00:55:47

## ENTITY_PARTICIPANT (49 rows)
R473 | entity_participant | - | T01 line 41 00:00:00
R474 | entity_participant | ENTITY_VARIANT | T01 line 46 00:00:28
R475 | entity_participant | ENTITY_VARIANT | T01 line 47 00:00:34
R476 | entity_participant | ENTITY_VARIANT | T02 line 53 00:01:15
R477 | entity_participant | - | T02 line 54 00:01:22
R478 | entity_participant | ENTITY_VARIANT | T02 line 98 00:06:39
R479 | entity_participant | - | T02 line 56 00:02:02
R480 | entity_participant | - | T02 line 57 00:02:09
R481 | entity_participant | - | T02 line 58 00:02:22
R482 | entity_participant | - | T02 line 60 00:02:39
R483 | entity_participant | - | T02 line 70 00:03:47
R484 | entity_participant | - | T02 line 70 00:03:47
R485 | entity_participant | - | T02 line 81 00:05:08
R486 | entity_participant | - | T02 line 79 00:04:55
R487 | entity_participant | - | T02 line 83 00:05:21
R488 | entity_participant | - | T02 line 88 00:05:43
R489 | entity_participant | - | T02 line 91 00:06:03
R490 | entity_participant | - | T02 line 97 00:06:34
R491 | entity_participant | - | T03 line 115 00:09:02
R492 | entity_participant | - | T03 line 125 00:10:47
R493 | entity_participant | - | T03 line 119 00:10:00
R494 | entity_participant | - | T05 line 133 00:11:56
R495 | entity_participant | - | T05 line 133 00:11:56
R496 | entity_participant | - | T06 line 178 00:17:30
R497 | entity_participant | - | T06 line 178 00:17:30
R498 | entity_participant | - | T07 line 245 00:24:20
R499 | entity_participant | - | T07 line 245 00:24:20
R500 | entity_participant | ASR_DOUBT_NAME | T08 line 293 00:30:33
R501 | entity_participant | - | T08 line 302 00:31:17
R502 | entity_participant | ASR_DOUBT_NAME | T09 line 346 00:34:54
R503 | entity_participant | - | T09 line 349 00:35:01
R504 | entity_participant | - | T09 line 349 00:35:01
R505 | entity_participant | - | T10 line 423 00:41:07
R506 | entity_participant | - | T10 line 423 00:41:07
R507 | entity_participant | - | T11 line 473 00:45:42
R508 | entity_participant | - | T11 line 473 00:45:42
R509 | entity_participant | ASR_DOUBT_NAME | T12 line 519 00:50:09
R510 | entity_participant | ASR_DOUBT_NAME | T12 line 519 00:50:09
R511 | entity_participant | - | T12 line 531 00:51:06
R512 | entity_participant | - | T06 line 179 00:17:39
R513 | entity_participant | - | T06 line 210 00:21:18
R514 | entity_participant | - | T06 line 225 00:22:19
R515 | entity_participant | - | T08 line 310 00:31:55
R516 | entity_participant | - | T08 line 299 00:31:01
R517 | entity_participant | - | T08 line 304 00:31:27
R518 | entity_participant | - | T08 line 335 00:34:09
R519 | entity_participant | - | T11 line 495 00:47:45
R520 | entity_participant | - | T14 line 590 00:56:41
R521 | entity_participant | - | T10 line 448 00:43:48

## FORWARD_COMMITMENT (140 rows)
R522 | forward_commitment | - | T00 line 39 -
R523 | forward_commitment | - | T01 line 42 00:00:06
R524 | forward_commitment | - | T01 line 42 00:00:06
R525 | forward_commitment | - | T01 line 44 00:00:18
R526 | forward_commitment | - | T01 line 45 00:00:22
R527 | forward_commitment | - | T01 line 47 00:00:34
R528 | forward_commitment | - | T01 line 49 00:00:42
R529 | forward_commitment | - | T02 line 53 00:01:15
R530 | forward_commitment | - | T02 line 60 00:02:39
R531 | forward_commitment | - | T02 line 66 00:03:18
R532 | forward_commitment | - | T02 line 68 00:03:33
R533 | forward_commitment | - | T02 line 82 00:05:14
R534 | forward_commitment | - | T02 line 86 00:05:36
R535 | forward_commitment | - | T02 line 93 00:06:10
R536 | forward_commitment | - | T02 line 93 00:06:10
R537 | forward_commitment | - | T02 line 95 00:06:22
R538 | forward_commitment | - | T02 line 98 00:06:39
R539 | forward_commitment | - | T02 line 98 00:06:39
R540 | forward_commitment | - | T03 line 100 00:06:56
R541 | forward_commitment | - | T03 line 103 00:07:30
R542 | forward_commitment | - | T03 line 114 00:08:54
R543 | forward_commitment | - | T03 line 119 00:10:00
R544 | forward_commitment | - | T03 line 120 00:10:10
R545 | forward_commitment | - | T03 line 121 00:10:17
R546 | forward_commitment | - | T03 line 127 00:11:02
R547 | forward_commitment | - | T04 line 132 00:11:51
R548 | forward_commitment | - | T05 line 133 00:11:56
R549 | forward_commitment | - | T05 line 141 00:12:54
R550 | forward_commitment | - | T05 line 143 00:13:08
R551 | forward_commitment | - | T05 line 144 00:13:16
R552 | forward_commitment | - | T05 line 144 00:13:16
R553 | forward_commitment | - | T05 line 148 00:13:36
R554 | forward_commitment | - | T05 line 150 00:13:46
R555 | forward_commitment | - | T05 line 159 00:14:33
R556 | forward_commitment | - | T05 line 159 00:14:33
R557 | forward_commitment | - | T05 line 164 00:15:14
R558 | forward_commitment | - | T05 line 171 00:16:34
R559 | forward_commitment | - | T05 line 172 00:16:41
R560 | forward_commitment | - | T05 line 176 00:17:05
R561 | forward_commitment | - | T06 line 178 00:17:30
R562 | forward_commitment | - | T06 line 183 00:18:09
R563 | forward_commitment | - | T06 line 185 00:18:18
R564 | forward_commitment | - | T06 line 196 00:19:34
R565 | forward_commitment | - | T06 line 199 00:20:00
R566 | forward_commitment | - | T06 line 200 00:20:08
R567 | forward_commitment | - | T06 line 202 00:20:21
R568 | forward_commitment | - | T06 line 203 00:20:27
R569 | forward_commitment | - | T06 line 212 00:21:33
R570 | forward_commitment | - | T06 line 214 00:21:46
R571 | forward_commitment | - | T06 line 216 00:21:57
R572 | forward_commitment | - | T06 line 229 00:22:46
R573 | forward_commitment | - | T06 line 230 00:22:52
R574 | forward_commitment | - | T06 line 231 00:22:58
R575 | forward_commitment | - | T06 line 236 00:23:23
R576 | forward_commitment | - | T06 line 237 00:23:29
R577 | forward_commitment | - | T06 line 237 00:23:29
R578 | forward_commitment | - | T06 line 237 00:23:29
R579 | forward_commitment | - | T07 line 245 00:24:20
R580 | forward_commitment | - | T07 line 248 00:24:42
R581 | forward_commitment | - | T07 line 256 00:25:33
R582 | forward_commitment | - | T07 line 258 00:25:47
R583 | forward_commitment | - | T07 line 262 00:26:15
R584 | forward_commitment | - | T07 line 277 00:28:30
R585 | forward_commitment | - | T07 line 285 00:29:18
R586 | forward_commitment | - | T07 line 292 00:29:55
R587 | forward_commitment | - | T07 line 292 00:29:55
R588 | forward_commitment | - | T08 line 294 00:30:42
R589 | forward_commitment | - | T08 line 295 00:30:46
R590 | forward_commitment | - | T08 line 299 00:31:01
R591 | forward_commitment | - | T08 line 312 00:32:08
R592 | forward_commitment | - | T08 line 322 00:32:54
R593 | forward_commitment | - | T08 line 322 00:32:54
R594 | forward_commitment | - | T08 line 326 00:33:16
R595 | forward_commitment | - | T08 line 332 00:33:49
R596 | forward_commitment | - | T08 line 333 00:33:55
R597 | forward_commitment | - | T09 line 350 00:35:04
R598 | forward_commitment | - | T09 line 356 00:35:23
R599 | forward_commitment | - | T09 line 356 00:35:23
R600 | forward_commitment | - | T09 line 368 00:36:10
R601 | forward_commitment | - | T09 line 369 00:36:16
R602 | forward_commitment | - | T09 line 371 00:36:29
R603 | forward_commitment | - | T09 line 371 00:36:29
R604 | forward_commitment | - | T09 line 373 00:36:40
R605 | forward_commitment | - | T09 line 380 00:37:17
R606 | forward_commitment | - | T09 line 381 00:37:22
R607 | forward_commitment | - | T09 line 384 00:37:38
R608 | forward_commitment | - | T09 line 385 00:37:45
R609 | forward_commitment | - | T09 line 385 00:37:45
R610 | forward_commitment | - | T09 line 388 00:38:07
R611 | forward_commitment | - | T09 line 388 00:38:07
R612 | forward_commitment | - | T09 line 394 00:38:47
R613 | forward_commitment | - | T09 line 394 00:38:47
R614 | forward_commitment | - | T09 line 416 00:40:31
R615 | forward_commitment | - | T10 line 421 00:40:56
R616 | forward_commitment | - | T10 line 423 00:41:07
R617 | forward_commitment | - | T10 line 432 00:42:05
R618 | forward_commitment | - | T10 line 433 00:42:11
R619 | forward_commitment | - | T10 line 433 00:42:11
R620 | forward_commitment | - | T10 line 433 00:42:11
R621 | forward_commitment | - | T10 line 442 00:43:09
R622 | forward_commitment | - | T10 line 454 00:44:27
R623 | forward_commitment | - | T10 line 456 00:44:38
R624 | forward_commitment | - | T10 line 457 00:44:45
R625 | forward_commitment | - | T10 line 460 00:45:01
R626 | forward_commitment | - | T10 line 463 00:45:13
R627 | forward_commitment | - | T10 line 464 00:45:19
R628 | forward_commitment | - | T10 line 465 00:45:27
R629 | forward_commitment | - | T10 line 465 00:45:27
R630 | forward_commitment | - | T10 line 467 00:45:34
R631 | forward_commitment | - | T11 line 474 00:45:45
R632 | forward_commitment | - | T11 line 476 00:45:52
R633 | forward_commitment | - | T11 line 477 00:46:02
R634 | forward_commitment | - | T11 line 479 00:46:11
R635 | forward_commitment | - | T11 line 479 00:46:11
R636 | forward_commitment | - | T11 line 483 00:46:30
R637 | forward_commitment | - | T11 line 487 00:46:52
R638 | forward_commitment | - | T11 line 491 00:47:14
R639 | forward_commitment | - | T11 line 493 00:47:31
R640 | forward_commitment | - | T11 line 493 00:47:31
R641 | forward_commitment | - | T11 line 496 00:47:52
R642 | forward_commitment | - | T12 line 520 00:50:15
R643 | forward_commitment | - | T12 line 521 00:50:21
R644 | forward_commitment | - | T12 line 524 00:50:34
R645 | forward_commitment | - | T12 line 527 00:50:48
R646 | forward_commitment | - | T12 line 540 00:52:07
R647 | forward_commitment | - | T12 line 541 00:52:14
R648 | forward_commitment | - | T12 line 545 00:52:41
R649 | forward_commitment | - | T12 line 547 00:52:53
R650 | forward_commitment | - | T12 line 551 00:53:18
R651 | forward_commitment | - | T12 line 555 00:53:40
R652 | forward_commitment | - | T12 line 570 00:54:35
R653 | forward_commitment | - | T12 line 577 00:55:16
R654 | forward_commitment | - | T13 line 579 00:55:29
R655 | forward_commitment | - | T14 line 585 00:56:10
R656 | forward_commitment | - | T14 line 586 00:56:16
R657 | forward_commitment | - | T14 line 586 00:56:16
R658 | forward_commitment | - | T14 line 588 00:56:27
R659 | forward_commitment | - | T14 line 589 00:56:34
R660 | forward_commitment | - | T14 line 589 00:56:34
R661 | forward_commitment | - | T14 line 590 00:56:41

## FORWARD_STATEMENT (32 rows)
R662 | forward_statement | - | T02 line 66 00:03:18
R663 | forward_statement | - | T02 line 93 00:06:10
R664 | forward_statement | - | T02 line 95 00:06:22
R665 | forward_statement | - | T02 line 97 00:06:34
R666 | forward_statement | - | T03 line 110 00:08:19
R667 | forward_statement | - | T03 line 120 00:10:10
R668 | forward_statement | - | T03 line 127 00:11:02
R669 | forward_statement | - | T05 line 142 00:12:59
R670 | forward_statement | - | T05 line 158 00:14:27
R671 | forward_statement | - | T06 line 199 00:20:00
R672 | forward_statement | - | T06 line 202 00:20:21
R673 | forward_statement | - | T06 line 234 00:23:13
R674 | forward_statement | - | T06 line 237 00:23:29
R675 | forward_statement | - | T06 line 241 00:23:52
R676 | forward_statement | - | T09 line 374 00:36:42
R677 | forward_statement | - | T09 line 384 00:37:38
R678 | forward_statement | - | T09 line 385 00:37:45
R679 | forward_statement | - | T11 line 479 00:46:11
R680 | forward_statement | - | T10 line 454 00:44:27
R681 | forward_statement | - | T10 line 463 00:45:13
R682 | forward_statement | - | T11 line 485 00:46:44
R683 | forward_statement | - | T11 line 496 00:47:52
R684 | forward_statement | - | T11 line 499 00:48:09
R685 | forward_statement | - | T12 line 570 00:54:35
R686 | forward_statement | - | T12 line 575 00:55:02
R687 | forward_statement | - | T14 line 586 00:56:16
R688 | forward_statement | - | T14 line 588 00:56:27
R689 | forward_statement | - | T14 line 589 00:56:34
R690 | forward_statement | - | T14 line 592 00:56:53
R691 | forward_statement | - | T09 line 413 00:40:14
R692 | forward_statement | - | T08 line 333 00:33:55
R693 | forward_statement | - | T05 line 137 00:12:20

## DATE_PERIOD (216 rows)
R694 | date_period | - | T00 line 39 -
R695 | date_period | - | T01 line 41 00:00:00
R696 | date_period | - | T01 line 41 00:00:00
R697 | date_period | - | T01 line 41 00:00:00
R698 | date_period | - | T01 line 47 00:00:34
R699 | date_period | - | T02 line 54 00:01:22
R700 | date_period | - | T02 line 54 00:01:22
R701 | date_period | - | T02 line 55 00:01:55
R702 | date_period | - | T02 line 63 00:02:58
R703 | date_period | ASR_DOUBT | T02 line 63 00:02:58
R704 | date_period | - | T02 line 67 00:03:25
R705 | date_period | ASR_DOUBT | T02 line 67 00:03:25
R706 | date_period | - | T02 line 76 00:04:27
R707 | date_period | - | T02 line 76 00:04:27
R708 | date_period | - | T02 line 77 00:04:39
R709 | date_period | ASR_DOUBT | T02 line 77 00:04:39
R710 | date_period | - | T02 line 78 00:04:47
R711 | date_period | - | T02 line 79 00:04:55
R712 | date_period | - | T02 line 79 00:04:55
R713 | date_period | - | T02 line 80 00:05:02
R714 | date_period | - | T02 line 80 00:05:02
R715 | date_period | - | T02 line 80 00:05:02
R716 | date_period | ASR_DOUBT | T02 line 82 00:05:14
R717 | date_period | - | T02 line 88 00:05:43
R718 | date_period | - | T02 line 88 00:05:43
R719 | date_period | - | T02 line 93 00:06:10
R720 | date_period | - | T02 line 94 00:06:16
R721 | date_period | - | T02 line 95 00:06:22
R722 | date_period | - | T03 line 99 00:06:47
R723 | date_period | - | T03 line 99 00:06:47
R724 | date_period | ASR_DOUBT | T03 line 99 00:06:47
R725 | date_period | - | T03 line 100 00:06:56
R726 | date_period | ASR_DOUBT | T03 line 101 00:07:04
R727 | date_period | - | T03 line 102 00:07:19
R728 | date_period | - | T03 line 105 00:07:39
R729 | date_period | ASR_DOUBT | T03 line 106 00:07:46
R730 | date_period | - | T03 line 106 00:07:46
R731 | date_period | ASR_DOUBT | T03 line 107 00:07:54
R732 | date_period | - | T03 line 111 00:08:26
R733 | date_period | ASR_DOUBT | T03 line 111 00:08:26
R734 | date_period | - | T03 line 112 00:08:34
R735 | date_period | ASR_DOUBT | T03 line 112 00:08:34
R736 | date_period | - | T03 line 112 00:08:34
R737 | date_period | - | T03 line 113 00:08:43
R738 | date_period | - | T03 line 115 00:09:02
R739 | date_period | - | T03 line 115 00:09:02
R740 | date_period | - | T03 line 116 00:09:08
R741 | date_period | - | T03 line 116 00:09:08
R742 | date_period | - | T03 line 116 00:09:08
R743 | date_period | - | T03 line 121 00:10:17
R744 | date_period | ASR_DOUBT | T03 line 122 00:10:23
R745 | date_period | ASR_DOUBT | T03 line 122 00:10:23
R746 | date_period | ASR_DOUBT | T03 line 123 00:10:32
R747 | date_period | ASR_DOUBT | T03 line 123 00:10:32
R748 | date_period | ASR_DOUBT | T03 line 124 00:10:37
R749 | date_period | ASR_DOUBT | T03 line 124 00:10:37
R750 | date_period | - | T03 line 124 00:10:37
R751 | date_period | - | T05 line 137 00:12:20
R752 | date_period | - | T05 line 137 00:12:20
R753 | date_period | - | T05 line 138 00:12:27
R754 | date_period | - | T05 line 138 00:12:27
R755 | date_period | - | T05 line 141 00:12:54
R756 | date_period | - | T05 line 142 00:12:59
R757 | date_period | - | T05 line 144 00:13:16
R758 | date_period | - | T05 line 144 00:13:16
R759 | date_period | ASR_DOUBT | T05 line 144 00:13:16
R760 | date_period | - | T05 line 147 00:13:30
R761 | date_period | - | T05 line 148 00:13:36
R762 | date_period | - | T05 line 149 00:13:40
R763 | date_period | - | T05 line 150 00:13:46
R764 | date_period | - | T05 line 155 00:14:12
R765 | date_period | - | T05 line 155 00:14:12
R766 | date_period | - | T05 line 156 00:14:18
R767 | date_period | - | T05 line 159 00:14:33
R768 | date_period | - | T05 line 161 00:14:56
R769 | date_period | - | T05 line 162 00:15:02
R770 | date_period | - | T05 line 162 00:15:02
R771 | date_period | - | T05 line 162 00:15:02
R772 | date_period | - | T05 line 164 00:15:14
R773 | date_period | ASR_DOUBT | T05 line 164 00:15:14
R774 | date_period | - | T05 line 164 00:15:14
R775 | date_period | ASR_DOUBT | T05 line 164 00:15:14
R776 | date_period | - | T05 line 164 00:15:14
R777 | date_period | - | T05 line 165 00:15:51
R778 | date_period | - | T05 line 165 00:15:51
R779 | date_period | - | T05 line 167 00:16:05
R780 | date_period | - | T05 line 167 00:16:05
R781 | date_period | - | T05 line 169 00:16:16
R782 | date_period | - | T05 line 173 00:16:46
R783 | date_period | - | T05 line 174 00:16:52
R784 | date_period | - | T05 line 175 00:17:00
R785 | date_period | - | T05 line 176 00:17:05
R786 | date_period | - | T05 line 176 00:17:05
R787 | date_period | - | T06 line 177 00:17:12
R788 | date_period | - | T06 line 195 00:19:28
R789 | date_period | - | T06 line 197 00:19:42
R790 | date_period | - | T06 line 200 00:20:08
R791 | date_period | - | T06 line 202 00:20:21
R792 | date_period | - | T06 line 204 00:20:35
R793 | date_period | - | T06 line 211 00:21:26
R794 | date_period | - | T06 line 211 00:21:26
R795 | date_period | - | T06 line 236 00:23:23
R796 | date_period | - | T06 line 237 00:23:29
R797 | date_period | - | T07 line 253 00:25:15
R798 | date_period | - | T07 line 261 00:26:08
R799 | date_period | - | T07 line 261 00:26:08
R800 | date_period | - | T07 line 266 00:27:12
R801 | date_period | - | T07 line 268 00:27:24
R802 | date_period | - | T07 line 268 00:27:24
R803 | date_period | - | T07 line 270 00:27:37
R804 | date_period | - | T07 line 270 00:27:37
R805 | date_period | - | T07 line 270 00:27:37
R806 | date_period | - | T07 line 279 00:28:45
R807 | date_period | - | T07 line 280 00:28:50
R808 | date_period | - | T07 line 280 00:28:50
R809 | date_period | - | T07 line 281 00:28:55
R810 | date_period | - | T07 line 281 00:28:55
R811 | date_period | - | T07 line 281 00:28:55
R812 | date_period | - | T07 line 282 00:29:01
R813 | date_period | - | T07 line 282 00:29:01
R814 | date_period | - | T07 line 284 00:29:13
R815 | date_period | - | T07 line 284 00:29:13
R816 | date_period | - | T07 line 285 00:29:18
R817 | date_period | - | T07 line 286 00:29:24
R818 | date_period | - | T07 line 287 00:29:29
R819 | date_period | - | T08 line 327 00:33:21
R820 | date_period | - | T09 line 355 00:35:14
R821 | date_period | - | T09 line 356 00:35:23
R822 | date_period | - | T09 line 356 00:35:23
R823 | date_period | - | T09 line 365 00:36:03
R824 | date_period | - | T09 line 371 00:36:29
R825 | date_period | - | T09 line 372 00:36:35
R826 | date_period | - | T09 line 373 00:36:40
R827 | date_period | - | T09 line 374 00:36:42
R828 | date_period | - | T09 line 374 00:36:42
R829 | date_period | - | T09 line 374 00:36:42
R830 | date_period | - | T09 line 384 00:37:38
R831 | date_period | - | T09 line 384 00:37:38
R832 | date_period | - | T09 line 384 00:37:38
R833 | date_period | - | T09 line 385 00:37:45
R834 | date_period | - | T09 line 385 00:37:45
R835 | date_period | - | T09 line 385 00:37:45
R836 | date_period | - | T09 line 394 00:38:47
R837 | date_period | - | T09 line 396 00:38:56
R838 | date_period | - | T10 line 425 00:41:17
R839 | date_period | - | T10 line 428 00:41:40
R840 | date_period | - | T10 line 428 00:41:40
R841 | date_period | - | T10 line 429 00:41:48
R842 | date_period | - | T10 line 433 00:42:11
R843 | date_period | - | T10 line 438 00:42:42
R844 | date_period | - | T10 line 441 00:43:02
R845 | date_period | - | T10 line 441 00:43:02
R846 | date_period | - | T10 line 452 00:44:16
R847 | date_period | - | T10 line 453 00:44:21
R848 | date_period | - | T10 line 453 00:44:21
R849 | date_period | - | T10 line 454 00:44:27
R850 | date_period | - | T10 line 454 00:44:27
R851 | date_period | - | T10 line 455 00:44:33
R852 | date_period | - | T10 line 457 00:44:45
R853 | date_period | - | T10 line 460 00:45:01
R854 | date_period | - | T10 line 463 00:45:13
R855 | date_period | - | T10 line 463 00:45:13
R856 | date_period | - | T10 line 465 00:45:27
R857 | date_period | - | T11 line 477 00:46:02
R858 | date_period | - | T11 line 478 00:46:05
R859 | date_period | - | T11 line 479 00:46:11
R860 | date_period | - | T11 line 483 00:46:30
R861 | date_period | - | T11 line 486 00:46:47
R862 | date_period | - | T11 line 492 00:47:19
R863 | date_period | - | T11 line 492 00:47:19
R864 | date_period | - | T11 line 493 00:47:31
R865 | date_period | - | T11 line 493 00:47:31
R866 | date_period | - | T11 line 493 00:47:31
R867 | date_period | - | T11 line 494 00:47:37
R868 | date_period | - | T11 line 498 00:48:04
R869 | date_period | - | T11 line 499 00:48:09
R870 | date_period | - | T11 line 499 00:48:09
R871 | date_period | - | T11 line 502 00:48:29
R872 | date_period | - | T11 line 502 00:48:29
R873 | date_period | - | T11 line 504 00:48:44
R874 | date_period | - | T11 line 505 00:48:52
R875 | date_period | - | T11 line 508 00:49:09
R876 | date_period | - | T11 line 508 00:49:09
R877 | date_period | - | T11 line 509 00:49:14
R878 | date_period | - | T11 line 510 00:49:18
R879 | date_period | - | T11 line 512 00:49:28
R880 | date_period | - | T11 line 512 00:49:28
R881 | date_period | - | T11 line 513 00:49:33
R882 | date_period | - | T11 line 513 00:49:33
R883 | date_period | - | T11 line 513 00:49:33
R884 | date_period | - | T11 line 514 00:49:38
R885 | date_period | - | T11 line 515 00:49:44
R886 | date_period | - | T11 line 515 00:49:44
R887 | date_period | - | T11 line 517 00:49:53
R888 | date_period | - | T11 line 517 00:49:53
R889 | date_period | - | T12 line 533 00:51:19
R890 | date_period | - | T12 line 533 00:51:19
R891 | date_period | - | T12 line 535 00:51:30
R892 | date_period | - | T12 line 535 00:51:30
R893 | date_period | - | T12 line 540 00:52:07
R894 | date_period | - | T12 line 561 00:54:12
R895 | date_period | - | T12 line 561 00:54:12
R896 | date_period | - | T12 line 562 00:54:18
R897 | date_period | - | T12 line 570 00:54:35
R898 | date_period | - | T12 line 576 00:55:09
R899 | date_period | ASR_DOUBT | T14 line 581 00:55:47
R900 | date_period | - | T14 line 581 00:55:47
R901 | date_period | - | T14 line 581 00:55:47
R902 | date_period | - | T14 line 582 00:55:57
R903 | date_period | - | T14 line 582 00:55:57
R904 | date_period | - | T14 line 586 00:56:16
R905 | date_period | - | T14 line 586 00:56:16
R906 | date_period | - | T14 line 588 00:56:27
R907 | date_period | - | T14 line 588 00:56:27
R908 | date_period | - | T14 line 590 00:56:41
R909 | date_period | - | T15 line 593 00:56:59

## HEDGE_QUALIFIER (25 rows)
R910 | hedge_qualifier | - | T00 line 39 
R911 | hedge_qualifier | - | T01 line 49 00:00:42
R912 | hedge_qualifier | - | T02 line 55 00:01:55
R913 | hedge_qualifier | - | T02 line 62 00:02:52
R914 | hedge_qualifier | - | T02 line 64 00:03:03
R915 | hedge_qualifier | - | T02 line 67 00:03:25
R916 | hedge_qualifier | - | T02 line 72 00:04:01
R917 | hedge_qualifier | - | T03 line 100 00:06:56
R918 | hedge_qualifier | - | T03 line 110 00:08:19
R919 | hedge_qualifier | - | T03 line 114 00:08:54
R920 | hedge_qualifier | - | T03 line 119 00:10:00
R921 | hedge_qualifier | - | T03 line 124 00:10:37
R922 | hedge_qualifier | - | T05 line 157 00:14:23
R923 | hedge_qualifier | - | T05 line 168 00:16:13
R924 | hedge_qualifier | - | T06 line 187 00:18:30
R925 | hedge_qualifier | - | T07 line 268 00:27:24
R926 | hedge_qualifier | - | T07 line 278 00:28:40
R927 | hedge_qualifier | - | T09 line 386 00:37:55
R928 | hedge_qualifier | RESTATED | T09 line 407 00:39:48
R929 | hedge_qualifier | - | T10 line 445 00:43:27
R930 | hedge_qualifier | - | T10 line 447 00:43:38
R931 | hedge_qualifier | - | T10 line 455 00:44:33
R932 | hedge_qualifier | - | T11 line 495 00:47:45
R933 | hedge_qualifier | - | T12 line 559 00:53:58
R934 | hedge_qualifier | - | T12 line 576 00:55:09

## MISSING_FROM_STRUCTURED
none found.

## FLAG TOTALS
ASR_DOUBT: 326
RESTATED: 7
ENTITY_VARIANT: 4
ASR_DOUBT_NAME: 4
REPEAT_QUESTION: 12 [LOOP1]
```yaml
stage: A2-enumerator
company: "KNACK"
quarter: "q2fy27"
doctype: "concall"
model: claude-sonnet-5-5
status: complete
ledger_path: "runs/knack-q2fy27/work/ledger_concall_knack_q2fy27.md"
counts:
  notes: 0
  line_items: 0
  zero_standing: 0
  agenda_items: 0
  auditor_paras: 0
  entities: 49
  turns: 16
  questions: 28
  mgmt_numbers: 464
  slides: 0
  slide_numbers: 0
flags_raised: [ASR_DOUBT, REPEAT_QUESTION, ENTITY_VARIANT, RESTATED, ASR_DOUBT_NAME, ANALYST_UNNAMED, SPEAKER_UNIDENTIFIED]
ids_in_structured: 934
ids_referenced: 934
orphan_ids: []
missing_from_structured: []
gate_a2: pass
mismatch_note: ""
analyst_note: "ASR_DOUBT 326 rows carried from A1; all numbers management tier, unverified. 28 questions (loop1: +T05-Q5, +T11-Q5; T09-Q2 now 13%; T10-Q3 DEFLECTED), 12 flagged REPEAT_QUESTION; main clusters are volume/utilisation, pass-through timing, Q3 margin recovery, capacity to Oct 2027. Management gave no quantified Q3 margin or price-hike figure; only 54 Rs/kg EBITDA in two quarters and Mexico break-even Q3 (Q4 not committed). Pinch-bottom utilisation percent declined (T06-Q3). Speakers inside Q&A not identified by ASR; no MGMT_ABSENCE raised. T08 questioner unnamed. mgmt_numbers 464 includes analyst-spoken figures inside analyst turns (not separable mechanically). Zero ZERO_STANDING rows; no line-0 rows."
```
