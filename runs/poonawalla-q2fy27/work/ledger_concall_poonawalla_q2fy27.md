# A2 LEDGER: concall POONAWALLA q2fy27
Source: A1 structured (R001-R287); fulltext used for the turn spine and count-test sweep only.

=== A2 COUNT TEST ===
category: structured_rows      grep_count: 287   sweep_count: 287   header_range R001-R287 = 287   match: yes
category: type_number     header_count: 176   grep_count: 176   sweep_count: 176   match: yes
category: type_date       header_count: 20   grep_count: 20   sweep_count: 20   match: yes
category: type_forward    header_count: 45   grep_count: 45   sweep_count: 45   match: yes
category: type_entity     header_count: 30   grep_count: 30   sweep_count: 30   match: yes
category: type_qualifier  header_count: 16   grep_count: 16   sweep_count: 16   match: yes
category: turns                grep_count: 45   sweep_count: 45   match: yes   (generic label regex gave 46; extra hit is the 'Subject:' header line, excluded)
category: questions            grep_count: 10   sweep_count: 10   match: yes   (4 analysts, 13 analyst turns)
category: mgmt_numbers         grep_count: 176   sweep_count: 176   match: yes   (5 pre-call cover rows R001-R005; 161 spoken by management; 10 analyst/moderator-stated, flagged)
category: participants         grep_count: 11   sweep_count: 11   match: yes
category: zero_standing        grep_count: 0    sweep_count: 0    match: yes   (A1 states none)
gate_a2: pass
=== END COUNT TEST ===

ids_in_structured: 287 | ids_referenced_in_ledger: 287 | orphan_ids: [] | match: yes

## 1. PARTICIPANTS
| ID | name | designation | side | A2 flags |
|---|---|---|---|---|
| R248 | Arvind Kapil | MD and CEO | mgmt | - |
| R249 | Sunil Samdani | Executive Director | mgmt | - |
| R250 | Shriram Iyer | Chief Credit and Analytics Officer | mgmt | - |
| R251 | Sanjay Miranka | CFO | mgmt | on roster, omitted from moderator intro |
| R252 | Harsh Kumar | Head AI and CHRO | mgmt | - |
| R246 | Shabnum Zaman | Company Secretary | mgmt | safe-harbor turn; also Reg 30 signatory |
| R253 | Moderator | call moderator | host | - |
| R264 | Suraj Das | Sundaram Mutual Fund | analyst | - |
| R265 | Pranay Mehta | Investec India | analyst | - |
| R266 | Abhijit Tibrewal | Motilal Oswal | analyst | - |
| R267 | Avinash Singh | Emkay Global | analyst | - |
MGMT_ABSENCE: no promoter or non-executive chairperson on the roster (R248-R252 plus CS). Observation only.

## 2. SPEAKER TURNS
| turn | speaker | role | span | structured IDs in turn |
|---|---|---|---|---|
| T00 | pre-call cover/roster | filing | L1-87 | R001,R002,R003,R004,R005,R177,R178,R179,R180,R181,R182,R183,R242,R243,R244,R245,R246,R247,R248,R249,R250,R251,R252,R281,R286,R287 |
| T01 | Moderator | moderator | fulltext L88-104 | R006,R253 |
| T02 | Shabnum Zaman | management | fulltext L105-123 | R241,R277,R278 |
| T03 | Arvind Kapil | management | fulltext L124-327 | R007,R008,R009,R010,R011,R012,R013,R014,R015,R016,R017,R018,R019,R020,R021,R022,R023,R024,R025,R026,R027,R028,R029,R030,R031,R032,R033,R034,R035,R036,R037,R038,R039,R040,R041,R042,R043,R044,R045,R046,R047,R048,R049,R050,R051,R052,R053,R054,R055,R056,R057,R058,R059,R060,R061,R062,R063,R064,R065,R066,R067,R068,R069,R070,R184,R185,R186,R194,R197,R198,R199,R200,R201,R202,R203,R204,R254,R255,R256,R257,R258,R272,R275,R276,R280,R283 |
| T04 | Shriram Iyer | management | fulltext L328-443 | R071,R072,R073,R074,R075,R076,R077,R078,R079,R080,R081,R082,R083,R084,R085,R086,R187,R205,R206,R207,R208,R259 |
| T05 | Harsh Kumar | management | fulltext L444-577 | R087,R088,R089,R090,R091,R092,R093,R094,R095,R096,R097,R098,R099,R209,R210,R240,R260,R261,R262,R263 |
| T06 | Sunil Samdani | management | fulltext L578-623 | R100,R101,R102,R103,R104,R105,R106,R107,R108,R109,R110,R111,R112,R113,R114,R115,R116,R117,R118,R119,R120,R121,R122,R123,R124,R125,R126,R127,R128,R129,R130,R131,R132,R188,R189,R279 |
| T07 | Moderator | moderator | fulltext L624-627 | R264 |
| T08 | Suraj Das | analyst | fulltext L628-651 | - |
| T09 | Arvind Kapil | management | fulltext L652-708 | R133,R134,R135,R136,R137,R138,R139,R195,R211,R212,R213,R214,R215,R216,R217,R218 |
| T10 | Suraj Das | analyst | fulltext L709-712 | - |
| T11 | Arvind Kapil | management | fulltext L713-726 | R219 |
| T12 | Suraj Das | analyst | fulltext L727-729 | - |
| T13 | Arvind Kapil | management | fulltext L730-732 | - |
| T14 | Moderator | moderator | fulltext L733-735 | R265 |
| T15 | Pranay Mehta | analyst | fulltext L736-746 | R140 |
| T16 | Arvind Kapil | management | fulltext L747-771 | R141,R142,R143,R144,R220,R273,R274 |
| T17 | Shriram Iyer | management | fulltext L772-785 | R145,R190,R191,R221,R222,R282 |
| T18 | Arvind Kapil | management | fulltext L786-803 | R146 |
| T19 | Pranay Mehta | analyst | fulltext L804-807 | - |
| T20 | Arvind Kapil | management | fulltext L808-810 | - |
| T21 | Moderator | moderator | fulltext L811-814 | R266 |
| T22 | Abhijit Tibrewal | analyst | fulltext L815-820 | - |
| T23 | Arvind Kapil | management | fulltext L821-823 | - |
| T24 | Sanjay Miranka | management | fulltext L824-843 | R223,R224 |
| T25 | Arvind Kapil | management | fulltext L844-865 | R147,R148,R149,R150,R151,R152,R192,R225,R226,R227,R269,R284 |
| T26 | Abhijit Tibrewal | analyst | fulltext L866-881 | R153,R154,R155,R156,R157,R228 |
| T27 | Arvind Kapil | management | fulltext L882-923 | R158,R193,R229,R230,R231,R232,R233,R234 |
| T28 | Abhijit Tibrewal | analyst | fulltext L924-935 | R159 |
| T29 | Arvind Kapil | management | fulltext L936-983 | R160,R161,R162,R163,R164,R165,R235,R270 |
| T30 | Abhijit Tibrewal | analyst | fulltext L984-986 | - |
| T31 | Arvind Kapil | management | fulltext L987-989 | - |
| T32 | Moderator | moderator | fulltext L990-993 | R267 |
| T33 | Avinash Singh | analyst | fulltext L994-1007 | R166,R167,R271 |
| T34 | Arvind Kapil | management | fulltext L1008-1017 | - |
| T35 | Avinash Singh | analyst | fulltext L1018-1021 | - |
| T36 | Arvind Kapil | management | fulltext L1022-1025 | - |
| T37 | Shriram Iyer | management | fulltext L1026-1037 | R168,R169,R170,R171,R196,R236,R268 |
| T38 | Arvind Kapil | management | fulltext L1038-1041 | R172 |
| T39 | Shriram Iyer | management | fulltext L1042-1050 | R173,R174,R237,R285 |
| T40 | Arvind Kapil | management | fulltext L1051-1056 | - |
| T41 | Avinash Singh | analyst | fulltext L1057-1059 | - |
| T42 | Arvind Kapil | management | fulltext L1060-1072 | R175,R176,R238,R239 |
| T43 | Avinash Singh | analyst | fulltext L1073-1082 | - |
| T44 | Arvind Kapil | management | fulltext L1083-1085 | - |
| T45 | Moderator | moderator | fulltext L1086-1094 | - |

## 3. QUESTIONS
| Q | analyst | firm | topic | turn | flags | related IDs |
|---|---|---|---|---|---|---|
| Q01 | Suraj Das | Sundaram MF | products per customer, cross-sell, operating leverage journey | T08 | - | R211,R214,R219 |
| Q02 | Suraj Das | Sundaram MF | product-level profitability, new-product profit timing, blended ROA | T08 | - | R133,R158,R232 |
| Q03 | Suraj Das | Sundaram MF | follow-up: product per customer now vs 1 and 2 years back | T10 | REPEAT_QUESTION (repeats Q01, same analyst; no number given, R219 defers) | R219 |
| Q04 | Pranay Mehta | Investec India | where credit cost settles | T15 | REPEAT_QUESTION (credit cost also Q08, Q09) | R141,R220,R221 |
| Q05 | Pranay Mehta | Investec India | product mix evolution; analyst cites 18% new-product share | T15 | VALUE_CONFLICT 18% vs 28% | R140,R008,R146 |
| Q06 | Abhijit Tibrewal | Motilal Oswal | floating vs fixed liability mix; cost of borrowing sensitivity to 50bp repo hike | T22 | MISSING_FROM_STRUCTURED M01 | R147,R148,R223 |
| Q07 | Abhijit Tibrewal | Motilal Oswal | growth vs profitability; sustainable ROA; operating leverage vs credit cost split | T26 | - | R153,R154,R156,R157,R229 |
| Q08 | Abhijit Tibrewal | Motilal Oswal | asset quality: underwriting and seasoning vs benign cycle; AI/ML loss rates | T28 | REPEAT_QUESTION (asset quality theme, with Q04, Q09) | R159,R160,R161 |
| Q09 | Avinash Singh | Emkay Global | credit cost near 2% vs benign cycle, 60-65% of book under 12m, write-off rate | T33 | REPEAT_QUESTION (credit cost, with Q04) | R166,R167 |
| Q10 | Avinash Singh | Emkay Global | proposed insurance commission regulation: fee yield impact and offsets | T33 | asked three times (initial, re-ask after CEO missed it, chase after reply); REPEAT_QUESTION (self) | R271,R238,R239 |
Analyst turns 13: Suraj 3, Pranay 2, Abhijit 4, Avinash 4 (includes thanks-only closing turns). Q&A span L624-1093 of 1093 fulltext lines (prepared remarks L124-623).

## 4. MANAGEMENT NUMBERS (every NUMBER row, with turn)
Pre-call cover NUMBER rows (no turn): R001, R002, R003, R004, R005 (other pre-call IDs are DATE/ENTITY/QUALIFIER, see sections 7-9).
| ID | turn / speaker | line | flag |
|---|---|---|---|
| R006 | T01 Moderator | L88 | MODERATOR |
| R007 | T03 Arvind Kapil | L142 |  |
| R008 | T03 Arvind Kapil | L143 |  |
| R009 | T03 Arvind Kapil | L143 |  |
| R010 | T03 Arvind Kapil | L144 |  |
| R011 | T03 Arvind Kapil | L156 |  |
| R012 | T03 Arvind Kapil | L160 |  |
| R013 | T03 Arvind Kapil | L161 |  |
| R014 | T03 Arvind Kapil | L162 |  |
| R015 | T03 Arvind Kapil | L164 |  |
| R016 | T03 Arvind Kapil | L168 |  |
| R017 | T03 Arvind Kapil | L168 |  |
| R018 | T03 Arvind Kapil | L169 |  |
| R019 | T03 Arvind Kapil | L169 |  |
| R020 | T03 Arvind Kapil | L174 |  |
| R021 | T03 Arvind Kapil | L174 |  |
| R022 | T03 Arvind Kapil | L174 |  |
| R023 | T03 Arvind Kapil | L174 |  |
| R024 | T03 Arvind Kapil | L174 |  |
| R025 | T03 Arvind Kapil | L179 |  |
| R026 | T03 Arvind Kapil | L180 |  |
| R027 | T03 Arvind Kapil | L180 |  |
| R028 | T03 Arvind Kapil | L181 |  |
| R029 | T03 Arvind Kapil | L186 |  |
| R030 | T03 Arvind Kapil | L188 |  |
| R031 | T03 Arvind Kapil | L189 |  |
| R032 | T03 Arvind Kapil | L189 |  |
| R033 | T03 Arvind Kapil | L192 |  |
| R034 | T03 Arvind Kapil | L192 |  |
| R035 | T03 Arvind Kapil | L193 |  |
| R036 | T03 Arvind Kapil | L196 |  |
| R037 | T03 Arvind Kapil | L216 |  |
| R038 | T03 Arvind Kapil | L217 |  |
| R039 | T03 Arvind Kapil | L219 |  |
| R040 | T03 Arvind Kapil | L219 |  |
| R041 | T03 Arvind Kapil | L222 |  |
| R042 | T03 Arvind Kapil | L223 |  |
| R043 | T03 Arvind Kapil | L224 |  |
| R044 | T03 Arvind Kapil | L225 |  |
| R045 | T03 Arvind Kapil | L225 |  |
| R046 | T03 Arvind Kapil | L226 |  |
| R047 | T03 Arvind Kapil | L230 |  |
| R048 | T03 Arvind Kapil | L231 |  |
| R049 | T03 Arvind Kapil | L231 |  |
| R050 | T03 Arvind Kapil | L232 |  |
| R051 | T03 Arvind Kapil | L232 |  |
| R052 | T03 Arvind Kapil | L236 |  |
| R053 | T03 Arvind Kapil | L237 |  |
| R054 | T03 Arvind Kapil | L239 |  |
| R055 | T03 Arvind Kapil | L242 |  |
| R056 | T03 Arvind Kapil | L242 |  |
| R057 | T03 Arvind Kapil | L243 |  |
| R058 | T03 Arvind Kapil | L243 |  |
| R059 | T03 Arvind Kapil | L254 |  |
| R060 | T03 Arvind Kapil | L255 |  |
| R061 | T03 Arvind Kapil | L264 |  |
| R062 | T03 Arvind Kapil | L264 |  |
| R063 | T03 Arvind Kapil | L264 |  |
| R064 | T03 Arvind Kapil | L265 |  |
| R065 | T03 Arvind Kapil | L265 |  |
| R066 | T03 Arvind Kapil | L265 |  |
| R067 | T03 Arvind Kapil | L286 |  |
| R068 | T03 Arvind Kapil | L287 |  |
| R069 | T03 Arvind Kapil | L287 |  |
| R070 | T03 Arvind Kapil | L311 |  |
| R071 | T04 Shriram Iyer | L357 |  |
| R072 | T04 Shriram Iyer | L358 |  |
| R073 | T04 Shriram Iyer | L368 |  |
| R074 | T04 Shriram Iyer | L383 |  |
| R075 | T04 Shriram Iyer | L383 |  |
| R076 | T04 Shriram Iyer | L384 |  |
| R077 | T04 Shriram Iyer | L384 |  |
| R078 | T04 Shriram Iyer | L388 |  |
| R079 | T04 Shriram Iyer | L388 |  |
| R080 | T04 Shriram Iyer | L389 |  |
| R081 | T04 Shriram Iyer | L389 |  |
| R082 | T04 Shriram Iyer | L390 |  |
| R083 | T04 Shriram Iyer | L390 |  |
| R084 | T04 Shriram Iyer | L391 |  |
| R085 | T04 Shriram Iyer | L391 |  |
| R086 | T04 Shriram Iyer | L392 |  |
| R087 | T05 Harsh Kumar | L475 |  |
| R088 | T05 Harsh Kumar | L476 |  |
| R089 | T05 Harsh Kumar | L479 |  |
| R090 | T05 Harsh Kumar | L479 |  |
| R091 | T05 Harsh Kumar | L479 |  |
| R092 | T05 Harsh Kumar | L504 |  |
| R093 | T05 Harsh Kumar | L518 |  |
| R094 | T05 Harsh Kumar | L555 |  |
| R095 | T05 Harsh Kumar | L556 |  |
| R096 | T05 Harsh Kumar | L557 |  |
| R097 | T05 Harsh Kumar | L560 |  |
| R098 | T05 Harsh Kumar | L561 |  |
| R099 | T05 Harsh Kumar | L561 |  |
| R100 | T06 Sunil Samdani | L582 |  |
| R101 | T06 Sunil Samdani | L582 |  |
| R102 | T06 Sunil Samdani | L585 |  |
| R103 | T06 Sunil Samdani | L586 |  |
| R104 | T06 Sunil Samdani | L588 |  |
| R105 | T06 Sunil Samdani | L588 |  |
| R106 | T06 Sunil Samdani | L589 |  |
| R107 | T06 Sunil Samdani | L596 |  |
| R108 | T06 Sunil Samdani | L596 |  |
| R109 | T06 Sunil Samdani | L597 |  |
| R110 | T06 Sunil Samdani | L598 |  |
| R111 | T06 Sunil Samdani | L598 |  |
| R112 | T06 Sunil Samdani | L599 |  |
| R113 | T06 Sunil Samdani | L601 |  |
| R114 | T06 Sunil Samdani | L601 |  |
| R115 | T06 Sunil Samdani | L603 |  |
| R116 | T06 Sunil Samdani | L603 |  |
| R117 | T06 Sunil Samdani | L604 |  |
| R118 | T06 Sunil Samdani | L605 |  |
| R119 | T06 Sunil Samdani | L606 |  |
| R120 | T06 Sunil Samdani | L606 |  |
| R121 | T06 Sunil Samdani | L607 |  |
| R122 | T06 Sunil Samdani | L607 |  |
| R123 | T06 Sunil Samdani | L607 |  |
| R124 | T06 Sunil Samdani | L608 |  |
| R125 | T06 Sunil Samdani | L609 |  |
| R126 | T06 Sunil Samdani | L609 |  |
| R127 | T06 Sunil Samdani | L611 |  |
| R128 | T06 Sunil Samdani | L613 |  |
| R129 | T06 Sunil Samdani | L613 |  |
| R130 | T06 Sunil Samdani | L615 |  |
| R131 | T06 Sunil Samdani | L616 |  |
| R132 | T06 Sunil Samdani | L618 |  |
| R133 | T09 Arvind Kapil | L653 |  |
| R134 | T09 Arvind Kapil | L659 |  |
| R135 | T09 Arvind Kapil | L674 |  |
| R136 | T09 Arvind Kapil | L675 |  |
| R137 | T09 Arvind Kapil | L685 |  |
| R138 | T09 Arvind Kapil | L687 |  |
| R139 | T09 Arvind Kapil | L688 |  |
| R140 | T15 Pranay Mehta | L744 | ANALYST_STATED |
| R141 | T16 Arvind Kapil | L747 |  |
| R142 | T16 Arvind Kapil | L757 |  |
| R143 | T16 Arvind Kapil | L757 |  |
| R144 | T16 Arvind Kapil | L757 |  |
| R145 | T17 Shriram Iyer | L781 |  |
| R146 | T18 Arvind Kapil | L789 |  |
| R147 | T25 Arvind Kapil | L846 |  |
| R148 | T25 Arvind Kapil | L850 |  |
| R149 | T25 Arvind Kapil | L851 |  |
| R150 | T25 Arvind Kapil | L852 |  |
| R151 | T25 Arvind Kapil | L852 |  |
| R152 | T25 Arvind Kapil | L853 |  |
| R153 | T26 Abhijit Tibrewal | L869 | ANALYST_STATED |
| R154 | T26 Abhijit Tibrewal | L873 | ANALYST_STATED |
| R155 | T26 Abhijit Tibrewal | L873 | ANALYST_STATED |
| R156 | T26 Abhijit Tibrewal | L876 | ANALYST_STATED |
| R157 | T26 Abhijit Tibrewal | L877 | ANALYST_STATED |
| R158 | T27 Arvind Kapil | L908 |  |
| R159 | T28 Abhijit Tibrewal | L925 | ANALYST_STATED |
| R160 | T29 Arvind Kapil | L959 |  |
| R161 | T29 Arvind Kapil | L959 |  |
| R162 | T29 Arvind Kapil | L972 |  |
| R163 | T29 Arvind Kapil | L973 |  |
| R164 | T29 Arvind Kapil | L975 |  |
| R165 | T29 Arvind Kapil | L978 |  |
| R166 | T33 Avinash Singh | L995 | ANALYST_STATED |
| R167 | T33 Avinash Singh | L997 | ANALYST_STATED |
| R168 | T37 Shriram Iyer | L1027 |  |
| R169 | T37 Shriram Iyer | L1034 |  |
| R170 | T37 Shriram Iyer | L1034 |  |
| R171 | T37 Shriram Iyer | L1035 |  |
| R172 | T38 Arvind Kapil | L1038 |  |
| R173 | T39 Shriram Iyer | L1045 |  |
| R174 | T39 Shriram Iyer | L1046 |  |
| R175 | T42 Arvind Kapil | L1062 |  |
| R176 | T42 Arvind Kapil | L1062 |  |

### 4a. RESTATED groups
- RESTATED PAT Q2 Rs375cr: R031, R125
- RESTATED AUM Rs74,008cr: R007, R100, R155
- RESTATED ROA 2.18%: R033, R070, R136, R149, R157
- RESTATED credit cost Q2 2.19%: R022, R084, R115, R141
- RESTATED GNPA 1.20%: R023, R066, R074, R082, R119, R159
- RESTATED NIM 9.26%: R017, R107
- RESTATED opex/AUM 4.15%: R029, R112
- RESTATED new products 28%: R008, R137, R146
- RESTATED portfolio yield 14.08%: R013, R151
- RESTATED 6MOB 30+ 0.35%: R025, R073, R142
- RESTATED 6MOB prior 0.67%: R027, R143
- RESTATED AI projects 143: R068, R088
- RESTATED AI live 84: R069, R089
- RESTATED Stage 1/2/3 Q2 levels: R062, R078, R064, R080, R066, R082
- RESTATED credit cost Q1 2.4%: R021, R085, R116
- RESTATED 12MoB 90+ 53%: R145, R168
- RESTATED NNPA 0.61%: R076, R121
- RESTATED AUM growth ~10%: R059, R101, R173
- RESTATED PAT growth 22%: R032, R126
- RESTATED June 2028 ROA commitment: R152, R192, R225

### 4b. VALUE_CONFLICT / label / tie notes
- R116: VALUE_CONFLICT vs R021/R085 (2.41% vs 2.40%/2.4%)
- R140: VALUE_CONFLICT analyst 18% vs mgmt 28% (R008,R137,R146)
- R175: VALUE_CONFLICT 14.8% vs 14.08% (R013,R151)
- R062: rounding 97.9% vs R078 97.86%
- R032: rounding vs R126 21.8%
- R059: rounding vs R101 10.4%
- R150: mgmt almost 200bp portfolio vs disbursement yield; cross-check R012/R014
- R280: METRIC_LABEL_AMBIGUITY NIM+fees vs NIM both 9.26%
- R017: label NIM plus fees; R107 calls it NIM
- R154: analyst 55% AUM YoY; mgmt QoQ 10.4% R101
- R153: analyst cites 35-40% CAGR vs 55% YoY (R154)
- R012: portfolio yield +45bps; cross-check R014 disb yield +20bps
- R015: Q1 comparative 50bps vs R014 20bps this Q
- R167: analyst 60-65% of book <12m seasoned
- R160: 30 vs 35 models spoken (R161)
- R161: 30 vs 35 models spoken (R160)
- R043: +90 branches ties to R044-R045 (550-460)
- R044: ties R043
- R176: 200bp vs R150 'almost 200' vs R284 'at the minimum 200'

## 5. FORWARD COMMITMENTS
| ID | turn / speaker | line | flag |
|---|---|---|---|
| R197 | T03 Arvind Kapil | L131 |  |
| R198 | T03 Arvind Kapil | L134 |  |
| R199 | T03 Arvind Kapil | L151 |  |
| R200 | T03 Arvind Kapil | L181 |  |
| R201 | T03 Arvind Kapil | L197 |  |
| R202 | T03 Arvind Kapil | L226 |  |
| R203 | T03 Arvind Kapil | L301 |  |
| R204 | T03 Arvind Kapil | L303 |  |
| R205 | T04 Shriram Iyer | L374 |  |
| R206 | T04 Shriram Iyer | L402 |  |
| R207 | T04 Shriram Iyer | L412 |  |
| R208 | T04 Shriram Iyer | L431 |  |
| R209 | T05 Harsh Kumar | L565 |  |
| R210 | T05 Harsh Kumar | L572 |  |
| R211 | T09 Arvind Kapil | L653 |  |
| R212 | T09 Arvind Kapil | L663 |  |
| R213 | T09 Arvind Kapil | L664 |  |
| R214 | T09 Arvind Kapil | L667 |  |
| R215 | T09 Arvind Kapil | L672 |  |
| R216 | T09 Arvind Kapil | L687 |  |
| R217 | T09 Arvind Kapil | L688 |  |
| R218 | T09 Arvind Kapil | L697 |  |
| R219 | T11 Arvind Kapil | L723 |  |
| R220 | T16 Arvind Kapil | L748 |  |
| R221 | T17 Shriram Iyer | L772 |  |
| R222 | T17 Shriram Iyer | L782 |  |
| R223 | T24 Sanjay Miranka | L839 |  |
| R224 | T24 Sanjay Miranka | L841 |  |
| R225 | T25 Arvind Kapil | L854 |  |
| R226 | T25 Arvind Kapil | L855 |  |
| R227 | T25 Arvind Kapil | L861 |  |
| R228 | T26 Abhijit Tibrewal | L869 | ANALYST_FRAMED |
| R229 | T27 Arvind Kapil | L882 |  |
| R230 | T27 Arvind Kapil | L895 |  |
| R231 | T27 Arvind Kapil | L900 |  |
| R232 | T27 Arvind Kapil | L908 |  |
| R233 | T27 Arvind Kapil | L911 |  |
| R234 | T27 Arvind Kapil | L913 |  |
| R235 | T29 Arvind Kapil | L961 |  |
| R236 | T37 Shriram Iyer | L1029 |  |
| R237 | T39 Shriram Iyer | L1047 |  |
| R238 | T42 Arvind Kapil | L1060 |  |
| R239 | T42 Arvind Kapil | L1063 |  |
| R240 | T05 Harsh Kumar | L513 |  |
| R241 | T02 Shabnum Zaman | L106 |  |

## 6. HEDGE PHRASES (regex: probably|approximately|almost|around|maybe|perhaps|I think|roughly|hopefully|should|expect|likely; management turns only; A3 holds the final lexicon)
hedge_hits: 80
| tag | turn | line | term |
|---|---|---|---|
| H | T03 Arvind Kapil | L160 | approximately |
| H | T03 Arvind Kapil | L163 | approximately |
| H | T03 Arvind Kapil | L164 | approximately |
| H | T03 Arvind Kapil | L179 | approximately |
| H | T03 Arvind Kapil | L180 | approximately |
| H | T03 Arvind Kapil | L193 | approximately |
| H | T03 Arvind Kapil | L206 | probably |
| H | T03 Arvind Kapil | L226 | approximately |
| H | T03 Arvind Kapil | L239 | around |
| H | T03 Arvind Kapil | L254 | approximately |
| H | T09 Arvind Kapil | L652 | i think |
| H | T09 Arvind Kapil | L653 | i think |
| H | T09 Arvind Kapil | L654 | probably |
| H | T09 Arvind Kapil | L656 | maybe |
| H | T09 Arvind Kapil | L664 | probably |
| H | T09 Arvind Kapil | L668 | probably |
| H | T09 Arvind Kapil | L672 | should |
| H | T09 Arvind Kapil | L674 | almost |
| H | T09 Arvind Kapil | L675 | i think |
| H | T09 Arvind Kapil | L675 | should |
| H | T09 Arvind Kapil | L680 | should |
| H | T09 Arvind Kapil | L685 | i think |
| H | T09 Arvind Kapil | L685 | i think |
| H | T09 Arvind Kapil | L687 | probably |
| H | T09 Arvind Kapil | L687 | probably |
| H | T11 Arvind Kapil | L714 | probably |
| H | T11 Arvind Kapil | L723 | i think |
| H | T16 Arvind Kapil | L749 | maybe |
| H | T16 Arvind Kapil | L755 | i think |
| H | T16 Arvind Kapil | L757 | i think |
| H | T16 Arvind Kapil | L757 | almost |
| H | T16 Arvind Kapil | L757 | almost |
| H | T16 Arvind Kapil | L758 | i think |
| H | T16 Arvind Kapil | L763 | i think |
| H | T17 Shriram Iyer | L772 | i think |
| H | T17 Shriram Iyer | L772 | expect |
| H | T17 Shriram Iyer | L782 | i think |
| H | T17 Shriram Iyer | L783 | expect |
| H | T18 Arvind Kapil | L786 | i think |
| H | T18 Arvind Kapil | L796 | almost |
| H | T18 Arvind Kapil | L797 | approximately |
| H | T18 Arvind Kapil | L800 | probably |
| H | T23 Arvind Kapil | L821 | i think |
| H | T24 Sanjay Miranka | L825 | i think |
| H | T24 Sanjay Miranka | L839 | i think |
| H | T24 Sanjay Miranka | L839 | should |
| H | T24 Sanjay Miranka | L841 | i think |
| H | T25 Arvind Kapil | L844 | should |
| H | T25 Arvind Kapil | L852 | almost |
| H | T25 Arvind Kapil | L854 | i think |
| H | T25 Arvind Kapil | L854 | should |
| H | T25 Arvind Kapil | L855 | probably |
| H | T25 Arvind Kapil | L861 | i think |
| H | T25 Arvind Kapil | L862 | i think |
| H | T27 Arvind Kapil | L885 | i think |
| H | T27 Arvind Kapil | L900 | i think |
| H | T27 Arvind Kapil | L904 | around |
| H | T27 Arvind Kapil | L908 | almost |
| H | T27 Arvind Kapil | L908 | probably |
| H | T27 Arvind Kapil | L911 | should |
| H | T27 Arvind Kapil | L911 | expect |
| H | T27 Arvind Kapil | L914 | should |
| H | T29 Arvind Kapil | L936 | i think |
| H | T29 Arvind Kapil | L944 | i think |
| H | T29 Arvind Kapil | L954 | probably |
| H | T29 Arvind Kapil | L975 | almost |
| H | T29 Arvind Kapil | L975 | probably |
| H | T29 Arvind Kapil | L978 | i think |
| H | T36 Arvind Kapil | L1022 | i think |
| H | T37 Shriram Iyer | L1027 | almost |
| H | T37 Shriram Iyer | L1035 | almost |
| H | T39 Shriram Iyer | L1045 | approximately |
| H | T39 Shriram Iyer | L1046 | i think |
| H | T42 Arvind Kapil | L1060 | i think |
| H | T42 Arvind Kapil | L1061 | i think |
| H | T42 Arvind Kapil | L1063 | should |
| H | T42 Arvind Kapil | L1063 | probably |
| H | T42 Arvind Kapil | L1064 | probably |
| H | T42 Arvind Kapil | L1069 | i think |
| H | T42 Arvind Kapil | L1069 | probably |

## 7. DATES
| ID | page | line | turn | A2 flags / note |
|---|---|---|---|---|
| R177 | 1 | 18 | T00 | cover-letter date set: letter Oct 14 vs call Oct 09 |
| R178 | 1 | 36 | T00 | cover-letter date set: letter Oct 14 vs call Oct 09 |
| R179 | 1 | 36 | T00 | cover-letter date set: letter Oct 14 vs call Oct 09 |
| R180 | 1 | 38 | T00 | period label |
| R181 | 1 | 39 | T00 |  |
| R182 | 1 | 30 | T00 | period label |
| R183 | 1 | 57 | T00 | signature 2026.10.14 17:15, five days after the call (R181 Oct 09) |
| R184 | 3 | 124 | T03 |  |
| R185 | 4 | 160 | T03 |  |
| R186 | 4 | 193 | T03 |  |
| R187 | 7 | 392 | T04 |  |
| R188 | 11 | 615 | T06 |  |
| R189 | 11 | 618 | T06 |  |
| R190 | 14 | 781 | T17 |  |
| R191 | 14 | 782 | T17 |  |
| R192 | 15 | 853 | T25 | RESTATED June 2028 (R152,R192,R225) |
| R193 | 16 | 908 | T27 |  |
| R194 | 3 | 144 | T03 |  |
| R195 | 12 | 659 | T09 |  |
| R196 | 18 | 1035 | T37 |  |

## 8. ENTITIES
| ID | page | line | turn | A2 flags / note |
|---|---|---|---|---|
| R242 | 1 | 20 | T00 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |
| R243 | 1 | 20 | T00 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |
| R244 | 1 | 25 | T00 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |
| R245 | 1 | 52 | T00 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |
| R246 | 1 | 60 | T00 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |
| R247 | 1 | 30 | T00 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |
| R248 | 2 | 71 | T00 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |
| R249 | 2 | 73 | T00 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |
| R250 | 2 | 74 | T00 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |
| R251 | 2 | 76 | T00 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |
| R252 | 2 | 77 | T00 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |
| R253 | 3 | 91 | T01 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |
| R254 | 5 | 216 | T03 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |
| R255 | 5 | 222 | T03 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |
| R256 | 5 | 229 | T03 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |
| R257 | 5 | 236 | T03 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |
| R258 | 5 | 242 | T03 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |
| R259 | 8 | 425 | T04 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |
| R260 | 9 | 491 | T05 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |
| R261 | 9 | 518 | T05 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |
| R262 | 10 | 534 | T05 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |
| R263 | 10 | 555 | T05 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |
| R264 | 11 | 625 | T07 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |
| R265 | 13 | 733 | T14 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |
| R266 | 14 | 811 | T21 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |
| R267 | 16 | 990 | T32 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |
| R268 | 18 | 1033 | T37 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |
| R269 | 15 | 846 | T25 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |
| R270 | 17 | 966 | T29 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |
| R271 | 18 | 1003 | T33 | no consolidation list in a concall; ENTITY_CHANGE n/a (no prior ledger) |

## 9. QUALIFIERS
| ID | page | line | turn | A2 flags / note |
|---|---|---|---|---|
| R272 | 4 | 182 | T03 |  |
| R273 | 13 | 756 | T16 |  |
| R274 | 13 | 758 | T16 |  |
| R275 | 4 | 160 | T03 |  |
| R276 | 4 | 193 | T03 |  |
| R277 | 3 | 105 | T02 | safe harbor group (R241,R277,R278) |
| R278 | 3 | 112 | T02 | safe harbor group (R241,R277,R278) |
| R279 | 10 | 587 | T06 |  |
| R280 | 4 | 168 | T03 | METRIC_LABEL_AMBIGUITY NIM+fees vs NIM both 9.26% |
| R281 | 1 | 29 | T00 |  |
| R282 | 14 | 781 | T17 |  |
| R283 | 3 | 130 | T03 |  |
| R284 | 15 | 852 | T25 |  |
| R285 | 18 | 1044 | T39 |  |
| R286 | 2 | 83 | T00 |  |
| R287 | 1 | 53 | T00 |  |

## 10. MISSING_FROM_STRUCTURED
| ID | fulltext line | speaker | claim |
|---|---|---|---|
| M01 | L817 | Abhijit Tibrewal (analyst) | 'sensitivity of our cost of borrowings to, let's say, a 50 basis points hike in the repo rate' |
| M02 | L827 | Sanjay Miranka | 'visible from the last 3 months of tightening cycle' (rate-cycle context for cost of borrowing) |
| M03 | L845 | Arvind Kapil | 'One-third is clearly NCDs at a very favorable price' (restates R147 30%) |

## 11. ZERO_STANDING
none (A1 states no zero, nil or dash standing values; a concall has no financial tables)

## 12. ID ACCOUNTABILITY
ids_in_structured: 287 | ids_referenced_in_ledger: 287 | orphan_ids: [] | match: yes
