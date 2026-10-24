=== A2 COUNT TEST ===
source: A1 structured, presentation, CYBERTECH q2fy27 (no prior ledger: DROPPED_SLIDE diff not possible)
category: number          header_count: 205   grep_count: 205   sweep_count: 205   match: yes
category: entity          header_count: 73   grep_count: 73   sweep_count: 73   match: yes
category: entity-summary  header_count: 5   grep_count: 5   sweep_count: 5   match: yes
category: forward         header_count: 1   grep_count: 1   sweep_count: 1   match: yes
category: date            header_count: 24   grep_count: 24   sweep_count: 24   match: yes
category: qualifier       header_count: 18   grep_count: 18   sweep_count: 18   match: yes
category: slides          grep_count: 16   sweep_count: 16   match: yes
category: slide_numbers   grep_count: 205   sweep_count: 205   match: yes
category: zero_standing   grep_count: 13   sweep_count: 13   match: yes  (plus near-zero R256 "(0.0)" flagged ZERO_STANDING-NEAR)
category: footnotes       grep_count: 18   sweep_count: 18   match: yes (QUALIFIER rows)
category: p15_line_items  sweep_count: 22 distinct printed lines (source L309-L337 numeric)
ID ACCOUNTABILITY: ids_in_structured: 326 | ids_referenced_in_ledger: 326 | orphan_ids: [] | match: yes
gate_a2: pass
=== END COUNT TEST ===

## 1. SLIDES (number, title, content type, rows on slide)
slide | title | content type | n_rows | A2 flags
1 | Cover | text | 4 (R001..R004) | -
2 | Safe Harbor / disclaimer | text | 5 (R005..R009) | -
3 | Agenda | text | 1 (R010..R010) | -
4 | Section divider: Company Overview | text | 1 (R011..R011) | -
5 | Company overview (specialisations, team, partners, offices) | text+icons | 21 (R013..R033) | -
6 | Company timeline | graphic timeline | 11 (R034..R044) | -
7 | Enterprise Multi-Cloud Transformation services | text/graphic | 22 (R045..R066) | -
8 | Spatialitics Platform | text/graphic | 4 (R067..R070) | -
9 | Leadership team (Vish Tadimety, Steven Jeske, Ramasubramanian S.) | text+photo | 17 (R071..R087) | -
10 | Section divider: Financial Performance | text | 1 (R012..R012) | -
11 | Financial summary Q2FY27 | text/KPI tiles | 15 (R088..R102) | -
12 | Operating revenue, EBITDA, PBT trend (3 quarters) | chart | 25 (R103..R127) | -
13 | Revenue mix: geography and industry (3 quarters) | chart | 28 (R128..R155) | -
14 | Client and operating KPIs | text/KPI tiles | 10 (R156..R165) | -
15 | Consolidated Quarterly P&L - Q2FY27 | table | 155 (R166..R320) | ZERO_STANDING,image governs over raw text layer (R319)
16 | Contact / copyright / disclaimer | text | 6 (R321..R326) | -
DROPPED_SLIDE: none assessable (no prior-quarter ledger). Agenda R010 lists 2 sections; dividers R011 (p4) and R012 (p10).

## 2. SLIDE NUMBERS (every NUMBER row)
ROW_ID | category | A2 flags | cross-ref / materiality note
R016 | p5 L76 number | RESTATED | also R160
R017 | p5 L78 number | - | -
R018 | p5 L79 number | - | -
R077 | p9 L153 number | - | -
R088 | p11 L179 number | RESTATED | also R182
R089 | p11 L179 number | RESTATED | also R184
R090 | p11 L179 number | RESTATED | also R186
R091 | p11 L180 number | RESTATED | also R105,R166
R092 | p11 L180 number | RESTATED | also R107,R168
R093 | p11 L180 number | RESTATED | also R106,R170
R094 | p11 L181 number | RESTATED | also R110
R095 | p11 L181 number | RESTATED | also R113
R096 | p11 L182 number | RESTATED | also R118,R238
R097 | p11 L182 number | RESTATED | also R121
R098 | p11 L183 number | RESTATED | also R261
R099 | p11 L183 number | - | -
R103 | p12 L222 number | RESTATED | also R169
R104 | p12 L222 number | RESTATED | also R167
R105 | p12 L222 number | RESTATED | also R091,R166
R106 | p12 L222 number | RESTATED | also R093,R170
R107 | p12 L222 number | RESTATED | also R092,R168
R108 | p12 L223 number | - | -
R109 | p12 L223 number | - | -
R110 | p12 L223 number | RESTATED | also R094
R111 | p12 L223 number | - | -
R112 | p12 L223 number | - | -
R113 | p12 L223 number | RESTATED | also R095
R114 | p12 L223 number | - | -
R115 | p12 L223 number | - | EBITDA QoQ de-growth
R116 | p12 L224 number | RESTATED | also R241
R117 | p12 L224 number | RESTATED | also R239
R118 | p12 L224 number | RESTATED | also R096,R238
R119 | p12 L224 number | - | -
R120 | p12 L224 number | - | -
R121 | p12 L224 number | RESTATED | also R097
R122 | p12 L224 number | RESTATED | also R242
R123 | p12 L224 number | RESTATED | also R240
R128 | p13 L246 number | - | -
R129 | p13 L246 number | - | -
R130 | p13 L246 number | - | -
R131 | p13 L246 number | - | -
R132 | p13 L246 number | - | -
R133 | p13 L246 number | - | -
R134 | p13 L247 number | - | -
R135 | p13 L247 number | - | -
R136 | p13 L247 number | - | -
R137 | p13 L247 number | - | -
R138 | p13 L247 number | - | -
R139 | p13 L247 number | - | -
R140 | p13 L247 number | - | -
R141 | p13 L247 number | - | -
R142 | p13 L247 number | - | -
R143 | p13 L247 number | - | -
R144 | p13 L247 number | - | -
R145 | p13 L247 number | - | -
R156 | p14 L252 number | - | -
R157 | p14 L253 number | - | -
R158 | p14 L254 number | - | -
R159 | p14 L255 number | - | -
R160 | p14 L258 number | RESTATED | also R016
R161 | p14 L261 number | - | -
R166 | p15 L309 number | RESTATED | also R091,R105
R167 | p15 L309 number | RESTATED | also R104
R168 | p15 L309 number | RESTATED | also R092,R107
R169 | p15 L309 number | RESTATED | also R103
R170 | p15 L309 number | RESTATED | also R093,R106
R171 | p15 L309 number | - | -
R172 | p15 L309 number | - | -
R173 | p15 L309 number | - | -
R174 | p15 L310 number | - | -
R175 | p15 L310 number | - | -
R176 | p15 L310 number | - | -
R177 | p15 L310 number | - | -
R178 | p15 L310 number | - | -
R179 | p15 L310 number | - | -
R180 | p15 L310 number | - | -
R181 | p15 L310 number | - | -
R182 | p15 L311 number | RESTATED | also R088
R183 | p15 L311 number | - | -
R184 | p15 L311 number | RESTATED | also R089
R185 | p15 L311 number | - | -
R186 | p15 L311 number | RESTATED | also R090
R187 | p15 L311 number | - | -
R188 | p15 L311 number | - | -
R189 | p15 L311 number | - | -
R190 | p15 L313 number | - | -
R191 | p15 L313 number | - | -
R192 | p15 L313 number | - | -
R193 | p15 L313 number | - | -
R194 | p15 L313 number | - | -
R195 | p15 L313 number | - | -
R196 | p15 L313 number | - | -
R197 | p15 L313 number | - | -
R198 | p15 L314 number | - | -
R199 | p15 L314 number | - | -
R200 | p15 L314 number | - | -
R201 | p15 L314 number | - | -
R202 | p15 L314 number | - | -
R203 | p15 L314 number | - | -
R204 | p15 L314 number | - | -
R205 | p15 L314 number | - | -
R206 | p15 L315 number | - | -
R207 | p15 L315 number | - | -
R208 | p15 L315 number | - | -
R209 | p15 L315 number | - | -
R210 | p15 L315 number | - | finance cost +104.3% YoY off small base
R211 | p15 L315 number | - | -
R212 | p15 L315 number | - | -
R213 | p15 L315 number | - | -
R214 | p15 L316 number | - | -
R215 | p15 L316 number | - | -
R216 | p15 L316 number | - | -
R217 | p15 L316 number | - | -
R218 | p15 L316 number | - | -
R219 | p15 L316 number | - | -
R220 | p15 L316 number | - | -
R221 | p15 L316 number | - | -
R222 | p15 L317 number | - | -
R223 | p15 L317 number | - | -
R224 | p15 L317 number | - | -
R225 | p15 L317 number | - | -
R226 | p15 L317 number | - | -
R227 | p15 L317 number | - | -
R228 | p15 L317 number | - | -
R229 | p15 L317 number | - | -
R230 | p15 L318 number | - | -
R231 | p15 L318 number | - | -
R232 | p15 L318 number | - | -
R233 | p15 L318 number | - | -
R234 | p15 L318 number | - | -
R235 | p15 L318 number | - | -
R236 | p15 L318 number | - | -
R237 | p15 L318 number | - | -
R238 | p15 L319 number | RESTATED | also R096,R118
R239 | p15 L319 number | RESTATED | also R117
R240 | p15 L319 number | RESTATED | also R123
R241 | p15 L319 number | RESTATED | also R116
R242 | p15 L319 number | RESTATED | also R122
R243 | p15 L319 number | - | -
R244 | p15 L319 number | - | -
R245 | p15 L319 number | - | -
R246 | p15 L321 number | - | -
R247 | p15 L321 number | - | -
R248 | p15 L321 number | - | -
R249 | p15 L321 number | - | -
R250 | p15 L321 number | - | -
R251 | p15 L322 number | - | -
R252 | p15 L322 number | - | -
R253 | p15 L322 number | - | negative deferred tax in Q2FY26
R254 | p15 L322 number | - | -
R255 | p15 L322 number | - | -
R256 | p15 L323 number | ZERO_STANDING-NEAR | near-zero printed (0.0), rounds to zero; flagged ZERO_STANDING-NEAR, not in A1 count of 13
R257 | p15 L323 number | - | -
R258 | p15 L323 number | ZERO_STANDING | dash in Q2FY26 and H1FY26; non-zero in Q1FY27/H1FY27 (R257,R259)
R259 | p15 L323 number | - | -
R260 | p15 L323 number | ZERO_STANDING | -
R261 | p15 L324 number | RESTATED | also R098
R262 | p15 L324 number | - | -
R263 | p15 L324 number | - | -
R264 | p15 L324 number | - | -
R265 | p15 L324 number | - | -
R266 | p15 L324 number | - | -
R267 | p15 L324 number | - | -
R268 | p15 L324 number | - | -
R269 | p15 L327 number | ZERO_STANDING | -
R270 | p15 L327 number | ZERO_STANDING | -
R271 | p15 L327 number | - | -
R272 | p15 L327 number | ZERO_STANDING | -
R273 | p15 L327 number | - | -
R274 | p15 L328 number | ZERO_STANDING | -
R275 | p15 L328 number | ZERO_STANDING | -
R276 | p15 L328 number | - | -
R277 | p15 L328 number | ZERO_STANDING | -
R278 | p15 L328 number | - | -
R279 | p15 L330 number | - | -
R280 | p15 L330 number | - | -
R281 | p15 L330 number | - | -
R282 | p15 L330 number | - | -
R283 | p15 L330 number | - | -
R284 | p15 L331 number | ZERO_STANDING | label printed identical to R274 (not-reclassified) under the may-be-reclassified heading; duplicate label as printed
R285 | p15 L331 number | ZERO_STANDING | -
R286 | p15 L331 number | ZERO_STANDING | -
R287 | p15 L331 number | ZERO_STANDING | -
R288 | p15 L331 number | ZERO_STANDING | -
R289 | p15 L332 number | - | -
R290 | p15 L332 number | - | -
R291 | p15 L332 number | - | -
R292 | p15 L332 number | - | -
R293 | p15 L332 number | - | -
R294 | p15 L333 number | - | -
R295 | p15 L333 number | - | -
R296 | p15 L333 number | - | paid-up capital differs across periods, no explanation on slide (R294-R298)
R297 | p15 L333 number | - | -
R298 | p15 L333 number | - | -
R299 | p15 L336 number | - | -
R300 | p15 L336 number | - | -
R301 | p15 L336 number | - | -
R302 | p15 L336 number | - | -
R303 | p15 L336 number | - | -
R304 | p15 L337 number | - | -
R305 | p15 L337 number | - | -
R306 | p15 L337 number | - | -
R307 | p15 L337 number | - | -
R308 | p15 L337 number | - | -
R314 | p15 L333 number | - | -

## 3. FOOTNOTES / FINE PRINT / QUALIFIERS
ROW_ID | category | A2 flags | note
R004 | p1 L25 qualifier | - | -
R006 | p2 L38 qualifier | - | -
R007 | p2 L36 qualifier | - | -
R008 | p2 L35 qualifier | - | -
R100 | p11 L181 qualifier | - | margin denominator = total revenue; slide 12 titles operating revenue but margins tie to total revenue basis (R095-R097 vs R111-R113)
R101 | p11 L179 qualifier | - | -
R127 | p12 L224 qualifier | - | chart label legibility
R155 | p13 L246 qualifier | - | series mapping from image only
R163 | p14 L253 qualifier | - | -
R164 | p14 L254 qualifier | FOOTNOTE_UNRESOLVED | concentration period unstated
R165 | p14 L261 qualifier | FOOTNOTE_UNRESOLVED | project count period unstated
R315 | p15 L268 qualifier | - | -
R316 | p15 L269 qualifier | - | -
R317 | p15 L336 qualifier | - | -
R318 | p15 L313 qualifier | - | -
R319 | p15 L266 qualifier | - | extractor note, not a source claim
R324 | p16 L344 qualifier | - | -
R325 | p16 L344 qualifier | - | -

## 4. FORWARD-LOOKING
ROW_ID | category | flags | note
R009 | p2 L35 forward | - | only forward-looking text in deck; no numeric guidance

## 5. DATES
ROW_ID | category | flags | note
R001 | p1 L23 date | - | -
R002 | p1 L21 date | - | -
R034 | p6 L96 date | RESTATED | also R039
R035 | p6 L94 date | - | -
R036 | p6 L95 date | - | -
R037 | p6 L94 date | - | -
R038 | p6 L94 date | RESTATED | also R044
R074 | p9 L147 date | - | -
R075 | p9 L157 date | - | -
R076 | p9 L152 date | - | -
R102 | p11 L177 date | RESTATED | also R126,R154
R124 | p12 L222 date | - | -
R125 | p12 L222 date | - | -
R126 | p12 L222 date | RESTATED | also R102,R154
R152 | p13 L242 date | - | -
R153 | p13 L242 date | - | -
R154 | p13 L242 date | RESTATED | also R102,R126
R162 | p14 L258 date | - | -
R309 | p15 L268 date | - | -
R310 | p15 L268 date | - | -
R311 | p15 L268 date | - | -
R312 | p15 L268 date | - | -
R313 | p15 L268 date | - | -
R326 | p16 L343 date | - | -

## 6. ENTITIES (grouped by slide; ENTITY_CHANGE not assessable, no prior)
p1 | entity | - | 1 rows: R003
p2 | entity | - | 1 rows: R005
p3 | entity | - | 1 rows: R010
p4 | entity | - | 1 rows: R011
p5 | entity | - | 18 rows: R013, R014, R015, R019, R020, R021, R022, R023, R024, R025, R026, R027, R028, R029, R030, R031, R032, R033
p6 | entity | - | 6 rows: R039, R040, R041, R042, R043, R044
p7 | entity | - | 22 rows: R045, R046, R047, R048, R049, R050, R051, R052, R053, R054, R055, R056, R057, R058, R059, R060, R061, R062, R063, R064, R065, R066
p8 | entity | - | 4 rows: R067, R068, R069, R070
p9 | entity | - | 13 rows: R071, R072, R073, R078, R079, R080, R081, R082, R083, R084, R085, R086, R087
p10 | entity | - | 1 rows: R012
p13 | entity | - | 6 rows: R146, R147, R148, R149, R150, R151
p15 | entity | - | 1 rows: R320
p16 | entity | - | 3 rows: R321, R322, R323

## 7. P&L LINE ITEMS (slide 15), one row per printed line
source line | line label | IDs | A2 flags
L309 | Revenue from Operations | R166-R173 (8) | -
L310 | Other Income | R174-R181 (8) | -
L311 | Total Revenue (1+2) | R182-R189 (8) | -
L313 | a) Cost of Hardware / Software package/ for service delivery Outsourced project cost | R190-R197 (8) | -
L314 | b) Employee Benefits expense | R198-R205 (8) | -
L315 | c) Finance Costs | R206-R213 (8) | -
L316 | d) Depreciation and amortization expense | R214-R221 (8) | -
L317 | e) Other expenses | R222-R229 (8) | -
L318 | Total Expenses | R230-R237 (8) | -
L319 | Profit before Tax (3-4) | R238-R245 (8) | -
L321 | a) Current Tax | R246-R250 (5) | -
L322 | b) Deferred Tax | R251-R255 (5) | -
L323 | c) Tax adjustments for earlier years | R256-R260 (5) | ZERO_STANDING-NEAR (R256)
L324 | Profit for the period (5-6) | R261-R268 (8) | -
L327 | a) Remeasurement of the net defined benefit liabilities | R269-R273 (5) | ZERO_STANDING (R269,R270,R272)
L328 | b) Income tax relating to items that will not be reclassified to profit and loss | R274-R278 (5) | ZERO_STANDING (R274,R275,R277)
L330 | a) Foreign currency translation reserve | R279-R283 (5) | -
L331 | b) Income tax relating to items that will not be reclassified to profit and loss | R284-R288 (5) | ZERO_STANDING (R284,R285,R286,R287,R288) ALL-PERIOD NIL standing line
L332 | Total Comprehensive Income for the period (7+8) | R289-R293 (5) | -
L333 | Paid up equity share capital (Face value: Rs.10 per share) | R294-R314 (6) | -
L336 | Basic (Not annualised) | R299-R303 (5) | -
L337 | Diluted (Not annualised) | R304-R308 (5) | -
p15 line items: 22

## 8. ZERO_STANDING LIST
R258, R260, R269, R270, R272, R274, R275, R277, R284, R285, R286, R287, R288
