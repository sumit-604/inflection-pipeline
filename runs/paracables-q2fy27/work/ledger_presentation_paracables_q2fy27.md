# A2 COMPLETENESS LEDGER: PARACABLES presentation Q2 FY27

Source: A1 structured extraction (R001-R525). Claim text stays in the structured file at each ID. Prior-quarter ledger: none, so DROPPED_SLIDE is not testable.

ids_in_structured: 525 | ids_referenced_in_ledger: 525 | orphan_ids: [] | match: yes

```
=== A2 COUNT TEST ===
category: slides        grep_count: 37 (fulltext [page N] markers)   sweep_count: 37   match: yes
category: slide_numbers grep_count: 407 (header 404 + 3 A1 follow-up rows, '| NUMBER |' grep)   sweep_count: 407   match: yes
category: entities      grep_count: 32   sweep_count: 32   match: yes
category: forward       grep_count: 25   sweep_count: 25   match: yes
category: dates         grep_count: 37   sweep_count: 37   match: yes
category: footnotes_qualifiers grep_count: 24   sweep_count: 24   match: yes
category: zero_standing grep_count: 3 (ZERO_STANDING tag in structured)   sweep_count: 3   match: yes
category: layout_flagged grep_count: 210 (LAYOUT_ tag grep)   sweep_count: 210   match: yes
total_ids: 525 (R001-R525 contiguous, no gaps, no duplicates)
gate_a2: pass
=== END COUNT TEST ===
```

## 1. SLIDES (37)
slide | title / content type | structured IDs on slide | A2 flags

1 | Cover (text) | R405..R476 (2) | -
2 | Safe Harbour Statement (text) | R430..R501 (4) | -
3 | Management Commentary (text, quote) | R406..R440 (5) | -
4 | Table of Contents (text) | R431..R431 (1) | -
5 | Section divider 01 Paramount at a Glance (text) | none | NO_STRUCTURED_ROWS (divider)
6 | A Platform built for the next Infrastructure Cycle (text/KPI) | R001..R503 (15) | -
7 | Our Value Chain (text/graphic) | R011..R433 (6) | -
8 | Seven Decades of Capability Building (timeline) | R015..R475 (20) | -
9 | A High-Growth Trajectory (chart+text) | R017..R504 (14) | -
10 | Why Paramount (text) | R029..R441 (4) | -
11 | Section divider 02 Sector at a Glance (text) | none | NO_STRUCTURED_ROWS (divider)
12 | Structural Demand across Power, Digital and Infrastructure (chart/text) | R032..R505 (16) | -
13 | Section divider 03 Operating Scale (text) | none | NO_STRUCTURED_ROWS (divider)
14 | Diversified Product Portfolio (text/lists) | R041..R432 (3) | -
15 | Manufacturing Depth Today; Capacity Expansion (text/chart) | R043..R507 (20) | -
16 | Domestic Platform with Growing Global Footprint (text/map) | R052..R445 (12) | -
17 | Revenue Mix (table/chart) LAYOUT | R061..R509 (39) | LAYOUT_SCRAMBLED_TABLE
18 | Export Flexibility through Market Cycles (chart/table) | R098..R487 (38) | -
19 | Domestic Power Orders anchor near-term opportunity (chart/text) | R135..R446 (16) | -
20 | Section divider 04 Platforms Growth (text) | none | NO_STRUCTURED_ROWS (divider)
21 | HTLS Conductors: More Capacity, Same Corridors (text) | R150..R512 (15) | -
22 | Data Centres: Emerging Growth Opportunity (text) | R420..R449 (2) | -
23 | Narmadapuram Greenfield Project: Execution and Progress (text) | R155..R461 (5) | -
24 | Section divider 05 Financial Performance (text) | none | NO_STRUCTURED_ROWS (divider)
25 | Q2 FY27 Performance Update (chart) | R156..R525 (24) | -
26 | H1 FY27 Performance Update (chart) | R178..R491 (15) | -
27 | H1 FY27 Performance Update, KPIs (text/chart) | R192..R519 (11) | -
28 | Income Statement (table) LAYOUT | R201..R514 (97) | LAYOUT_SCRAMBLED_TABLE
29 | Performance Trajectory 5 Year Financial Highlights (table) LAYOUT | R296..R517 (53) | LAYOUT_SCRAMBLED_TABLE
30 | Balance Sheet (table) LAYOUT | R346..R518 (44) | LAYOUT_SCRAMBLED_TABLE
31 | Section divider 06 FY27 Outlook (text) | none | NO_STRUCTURED_ROWS (divider) outlook divider; numeric guidance absent, forward text on slide 32
32 | FY27 Roadmap (text) | R389..R496 (8) | -
33 | Section divider 07 Annexures (text) | none | NO_STRUCTURED_ROWS (divider)
34 | Experienced Leadership (text/photo) | R390..R498 (16) | -
35 | Long-standing Relationships and Key Certifications (logos/photo) | R435..R435 (1) | -
36 | Stock Performance and Shareholding (chart/table) | R398..R521 (13) | -
37 | Thank You / contacts (text) | R427..R436 (3) | -

Rows are ordered by ID, so IDs on a slide may be non-contiguous. Pages with rows: 1, 2, 3, 4, 6, 7, 8, 9, 10, 12, 14, 15, 16, 17, 18, 19, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 34, 35, 36, 37.

## 2. SLIDE NUMBERS (407)
ROW_ID | category | page/line | A2 flags | cross-ref / materiality
R001 | slide_number | p6 L85 |  | -
R002 | slide_number | p6 L85 |  | -
R003 | slide_number | p6 L85 |  | -
R004 | slide_number | p6 L88 | RESTATED | also R136,R148,R196,R477,R492,R502
R005 | slide_number | p6 L88 | RESTATED | also R046
R006 | slide_number | p6 L88 | RESTATED | also R014,R029,R056
R007 | slide_number | p6 L92 |  | -
R008 | slide_number | p6 L93 |  | -
R009 | slide_number | p6 L93 | RESTATED | also R012,R030,R052
R010 | slide_number | p6 L94 |  | -
R011 | slide_number | p7 L111 |  | -
R012 | slide_number | p7 L115 | RESTATED | also R009,R030,R052
R013 | slide_number | p7 L116 | RESTATED | also R053,R094
R014 | slide_number | p7 L118 | RESTATED | also R006,R029,R056
R015 | slide_number | p8 L140 |  | -
R016 | slide_number | p8 L139 |  | -
R017 | slide_number | p9 L148 |  | -
R018 | slide_number | p9 L148 |  | -
R019 | slide_number | p9 L148 |  | -
R020 | slide_number | p9 L148 |  | -
R021 | slide_number | p9 L148 | RESTATED | also R022
R022 | slide_number | p9 L148 | RESTATED | also R021
R023 | slide_number | p9 L149 |  | -
R024 | slide_number | p9 L150 |  | -
R025 | slide_number | p9 L151 |  | -
R026 | slide_number | p9 L152 |  | -
R027 | slide_number | p9 L156 |  | -
R028 | slide_number | p9 L156 |  | -
R029 | slide_number | p10 L158 | RESTATED | also R006,R014,R056
R030 | slide_number | p10 L160 | RESTATED | also R009,R012,R052
R031 | slide_number | p10 L166 |  | -
R032 | slide_number | p12 L176 |  | -
R033 | slide_number | p12 L176 |  | -
R034 | slide_number | p12 L177 |  | -
R035 | slide_number | p12 L176 |  | -
R036 | slide_number | p12 L176 |  | -
R037 | slide_number | p12 L177 |  | -
R038 | slide_number | p12 L176 |  | -
R039 | slide_number | p12 L183 |  | -
R040 | slide_number | p12 L183 |  | -
R041 | slide_number | p14 L205 |  | -
R042 | slide_number | p14 L205 |  | -
R043 | slide_number | p15 L214 |  | -
R044 | slide_number | p15 L214 |  | -
R045 | slide_number | p15 L214 |  | -
R046 | slide_number | p15 L214 | RESTATED | also R005
R047 | slide_number | p15 L211 |  | -
R048 | slide_number | p15 L211 |  | -
R049 | slide_number | p15 L214 |  | -
R050 | slide_number | p15 L218 | RESTATED | also R444
R051 | slide_number | p15 L219 | RESTATED | also R444
R052 | slide_number | p16 L224 | RESTATED | also R009,R012,R030
R053 | slide_number | p16 L224 | RESTATED | also R013,R094
R054 | slide_number | p16 L226 |  | -
R055 | slide_number | p16 L226 |  | -
R056 | slide_number | p16 L228 | RESTATED | also R006,R014,R029
R057 | slide_number | p16 L236 |  | -
R058 | slide_number | p16 L236 |  | -
R059 | slide_number | p16 L239 |  | -
R060 | slide_number | p16 L239 |  | -
R061 | slide_number | p17 L249 | LAYOUT_SCRAMBLED LAYOUT_TABLE_SLIDE | -
R062 | slide_number | p17 L250 | LAYOUT_SCRAMBLED LAYOUT_TABLE_SLIDE | -
R063 | slide_number | p17 L250 | LAYOUT_SCRAMBLED LAYOUT_TABLE_SLIDE | -
R064 | slide_number | p17 L251 | LAYOUT_SCRAMBLED LAYOUT_TABLE_SLIDE | -
R065 | slide_number | p17 L253 | LAYOUT_SCRAMBLED LAYOUT_TABLE_SLIDE | -
R066 | slide_number | p17 L254 | LAYOUT_SCRAMBLED LAYOUT_TABLE_SLIDE | -
R067 | slide_number | p17 L253 | LAYOUT_SCRAMBLED LAYOUT_TABLE_SLIDE | -
R068 | slide_number | p17 L256 | LAYOUT_SCRAMBLED LAYOUT_TABLE_SLIDE | -
R069 | slide_number | p17 L258 | LAYOUT_SCRAMBLED LAYOUT_TABLE_SLIDE | -
R070 | slide_number | p17 L259 | LAYOUT_SCRAMBLED LAYOUT_TABLE_SLIDE | -
R071 | slide_number | p17 L262 | LAYOUT_SCRAMBLED LAYOUT_TABLE_SLIDE | -
R072 | slide_number | p17 L258 | LAYOUT_SCRAMBLED LAYOUT_TABLE_SLIDE | -
R073 | slide_number | p17 L259 | LAYOUT_SCRAMBLED LAYOUT_TABLE_SLIDE | -
R074 | slide_number | p17 L260 | LAYOUT_SCRAMBLED LAYOUT_TABLE_SLIDE | -
R075 | slide_number | p17 L260 | LAYOUT_SCRAMBLED LAYOUT_TABLE_SLIDE | -
R076 | slide_number | p17 L260 | LAYOUT_SCRAMBLED LAYOUT_TABLE_SLIDE | -
R077 | slide_number | p17 L260 | LAYOUT_SCRAMBLED LAYOUT_TABLE_SLIDE | -
R078 | slide_number | p17 L260 | LAYOUT_SCRAMBLED LAYOUT_TABLE_SLIDE | -
R079 | slide_number | p17 L262 | LAYOUT_SCRAMBLED LAYOUT_TABLE_SLIDE | -
R080 | slide_number | p17 L262 | LAYOUT_SCRAMBLED LAYOUT_TABLE_SLIDE | -
R081 | slide_number | p17 L262 | LAYOUT_SCRAMBLED LAYOUT_TABLE_SLIDE | -
R082 | slide_number | p17 L262 | LAYOUT_SCRAMBLED LAYOUT_TABLE_SLIDE | -
R083 | slide_number | p17 L263 | LAYOUT_SCRAMBLED LAYOUT_TABLE_SLIDE | -
R084 | slide_number | p17 L263 | LAYOUT_SCRAMBLED LAYOUT_TABLE_SLIDE | -
R085 | slide_number | p17 L263 | LAYOUT_SCRAMBLED LAYOUT_TABLE_SLIDE | -
R086 | slide_number | p17 L263 | LAYOUT_SCRAMBLED LAYOUT_TABLE_SLIDE | -
R087 | slide_number | p17 L260 | LAYOUT_TABLE_SLIDE | -
R088 | slide_number | p17 L260 | LAYOUT_TABLE_SLIDE | -
R089 | slide_number | p17 L260 | LAYOUT_TABLE_SLIDE | -
R090 | slide_number | p17 L263 | LAYOUT_TABLE_SLIDE | -
R091 | slide_number | p17 L263 | LAYOUT_TABLE_SLIDE | -
R092 | slide_number | p17 L264 | LAYOUT_TABLE_SLIDE | -
R093 | slide_number | p17 L264 | LAYOUT_TABLE_SLIDE | -
R094 | slide_number | p17 L265 | LAYOUT_TABLE_SLIDE RESTATED | also R013,R053
R095 | slide_number | p17 L265 | LAYOUT_TABLE_SLIDE | -
R096 | slide_number | p17 L265 | LAYOUT_TABLE_SLIDE | -
R097 | slide_number | p17 L261 | LAYOUT_TABLE_SLIDE ZERO_STANDING | -
R098 | slide_number | p18 L271 |  | -
R099 | slide_number | p18 L271 |  | -
R100 | slide_number | p18 L271 |  | -
R101 | slide_number | p18 L271 |  | -
R102 | slide_number | p18 L272 |  | -
R103 | slide_number | p18 L272 |  | -
R104 | slide_number | p18 L272 |  | -
R105 | slide_number | p18 L272 |  | -
R106 | slide_number | p18 L274 |  | -
R107 | slide_number | p18 L274 |  | -
R108 | slide_number | p18 L274 |  | -
R109 | slide_number | p18 L274 |  | -
R110 | slide_number | p18 L275 |  | -
R111 | slide_number | p18 L275 |  | -
R112 | slide_number | p18 L275 |  | -
R113 | slide_number | p18 L275 |  | -
R114 | slide_number | p18 L275 | LAYOUT_ROW_LABELS_SHIFTED | A1 note: row labels shifted, label per A1 arithmetic
R115 | slide_number | p18 L275 | LAYOUT_ROW_LABELS_SHIFTED | A1 note: row labels shifted, label per A1 arithmetic
R116 | slide_number | p18 L275 | LAYOUT_ROW_LABELS_SHIFTED | A1 note: row labels shifted, label per A1 arithmetic
R117 | slide_number | p18 L275 | LAYOUT_ROW_LABELS_SHIFTED | A1 note: row labels shifted, label per A1 arithmetic
R118 | slide_number | p18 L278 | LAYOUT_ROW_LABELS_SHIFTED | A1 note: row labels shifted, label per A1 arithmetic
R119 | slide_number | p18 L278 | LAYOUT_ROW_LABELS_SHIFTED | A1 note: row labels shifted, label per A1 arithmetic
R120 | slide_number | p18 L278 | LAYOUT_ROW_LABELS_SHIFTED | A1 note: row labels shifted, label per A1 arithmetic
R121 | slide_number | p18 L278 | LAYOUT_ROW_LABELS_SHIFTED | A1 note: row labels shifted, label per A1 arithmetic
R122 | slide_number | p18 L279 | LAYOUT_ROW_LABELS_SHIFTED | A1 note: row labels shifted, label per A1 arithmetic
R123 | slide_number | p18 L279 | LAYOUT_ROW_LABELS_SHIFTED | A1 note: row labels shifted, label per A1 arithmetic
R124 | slide_number | p18 L279 | LAYOUT_ROW_LABELS_SHIFTED | A1 note: row labels shifted, label per A1 arithmetic
R125 | slide_number | p18 L279 | LAYOUT_ROW_LABELS_SHIFTED | A1 note: row labels shifted, label per A1 arithmetic
R126 | slide_number | p18 L281 |  | -
R127 | slide_number | p18 L281 |  | -
R128 | slide_number | p18 L282 |  | -
R129 | slide_number | p18 L284 |  | -
R130 | slide_number | p18 L284 |  | -
R131 | slide_number | p18 L284 |  | -
R132 | slide_number | p18 L285 |  | -
R133 | slide_number | p18 L285 |  | -
R134 | slide_number | p18 L284 |  | -
R135 | slide_number | p19 L287 |  | -
R136 | slide_number | p19 L287 | RESTATED | also R004,R148,R196,R477,R492,R502
R137 | slide_number | p19 L288 |  | -
R138 | slide_number | p19 L289 |  | -
R139 | slide_number | p19 L289 |  | -
R140 | slide_number | p19 L291 |  | -
R141 | slide_number | p19 L292 |  | -
R142 | slide_number | p19 L291 |  | -
R143 | slide_number | p19 L293 |  | -
R144 | slide_number | p19 L293 |  | -
R145 | slide_number | p19 L293 |  | -
R146 | slide_number | p19 L294 |  | -
R147 | slide_number | p19 L294 |  | -
R148 | slide_number | p19 L294 | RESTATED | also R004,R136,R196,R477,R492,R502
R149 | slide_number | p19 L296 |  | -
R150 | slide_number | p21 L302 |  | -
R151 | slide_number | p21 L303 |  | -
R152 | slide_number | p21 L315 |  | -
R153 | slide_number | p21 L324 |  | -
R154 | slide_number | p21 L325 |  | -
R155 | slide_number | p23 L361 |  | -
R156 | slide_number | p25 L378 |  | -
R157 | slide_number | p25 L376 |  | -
R158 | slide_number | p25 L376 |  | -
R159 | slide_number | p25 L380 |  | -
R160 | slide_number | p25 L377 |  | -
R161 | slide_number | p25 L376 |  | -
R162 | slide_number | p25 L379 |  | -
R163 | slide_number | p25 L377 |  | -
R164 | slide_number | p25 L376 |  | -
R165 | slide_number | p25 L382 |  | -
R166 | slide_number | p25 L382 |  | -
R167 | slide_number | p25 L382 |  | -
R168 | slide_number | p25 L382 |  | -
R169 | slide_number | p25 L382 |  | -
R170 | slide_number | p25 L382 |  | -
R171 | slide_number | p25 L387 |  | -
R172 | slide_number | p25 L387 |  | -
R173 | slide_number | p25 L386 |  | -
R174 | slide_number | p25 L384 |  | -
R175 | slide_number | p25 L384 |  | -
R176 | slide_number | p25 L385 |  | -
R177 | slide_number | p25 L383 |  | -
R178 | slide_number | p26 L393 |  | -
R179 | slide_number | p26 L394 |  | -
R180 | slide_number | p26 L395 |  | -
R181 | slide_number | p26 L394 |  | -
R182 | slide_number | p26 L394 |  | -
R183 | slide_number | p26 L393 |  | -
R184 | slide_number | p26 L397 |  | -
R185 | slide_number | p26 L398 |  | -
R186 | slide_number | p26 L397 |  | -
R187 | slide_number | p26 L401 |  | -
R188 | slide_number | p26 L403 |  | -
R189 | slide_number | p26 L402 |  | -
R190 | slide_number | p26 L399 |  | -
R191 | slide_number | p26 L400 |  | -
R192 | slide_number | p27 L406 |  | -
R193 | slide_number | p27 L408 |  | -
R194 | slide_number | p27 L406 |  | -
R195 | slide_number | p27 L408 |  | -
R196 | slide_number | p27 L407 | RESTATED | also R004,R136,R148,R477,R492,R502
R197 | slide_number | p27 L410 |  | -
R198 | slide_number | p27 L412 |  | -
R199 | slide_number | p27 L410 |  | -
R200 | slide_number | p27 L412 |  | -
R201 | slide_number | p28 L416 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R202 | slide_number | p28 L416 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R203 | slide_number | p28 L416 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R204 | slide_number | p28 L416 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R205 | slide_number | p28 L416 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R206 | slide_number | p28 L416 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R207 | slide_number | p28 L416 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R208 | slide_number | p28 L418 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R209 | slide_number | p28 L417 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R210 | slide_number | p28 L417 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R211 | slide_number | p28 L417 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R212 | slide_number | p28 L417 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R213 | slide_number | p28 L417 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R214 | slide_number | p28 L417 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R215 | slide_number | p28 L417 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R216 | slide_number | p28 L419 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R217 | slide_number | p28 L419 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R218 | slide_number | p28 L419 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R219 | slide_number | p28 L418 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R220 | slide_number | p28 L418 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R221 | slide_number | p28 L418 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R222 | slide_number | p28 L419 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R223 | slide_number | p28 L418 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R224 | slide_number | p28 L420 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R225 | slide_number | p28 L420 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R226 | slide_number | p28 L420 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R227 | slide_number | p28 L419 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R228 | slide_number | p28 L419 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R229 | slide_number | p28 L419 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R230 | slide_number | p28 L420 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R231 | slide_number | p28 L419 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R232 | slide_number | p28 L421 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R233 | slide_number | p28 L421 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R234 | slide_number | p28 L421 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R235 | slide_number | p28 L420 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R236 | slide_number | p28 L420 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R237 | slide_number | p28 L420 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R238 | slide_number | p28 L421 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R239 | slide_number | p28 L420 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R240 | slide_number | p28 L422 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R241 | slide_number | p28 L422 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R242 | slide_number | p28 L422 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R243 | slide_number | p28 L421 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R244 | slide_number | p28 L421 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R245 | slide_number | p28 L421 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R246 | slide_number | p28 L422 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R247 | slide_number | p28 L421 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R248 | slide_number | p28 L423 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R249 | slide_number | p28 L423 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R250 | slide_number | p28 L423 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R251 | slide_number | p28 L422 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R252 | slide_number | p28 L422 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R253 | slide_number | p28 L422 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R254 | slide_number | p28 L423 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R255 | slide_number | p28 L422 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R256 | slide_number | p28 L424 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R257 | slide_number | p28 L424 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R258 | slide_number | p28 L424 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R259 | slide_number | p28 L423 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R260 | slide_number | p28 L423 | CORRECTED_FROM_IMAGE LAYOUT_TABLE_SLIDE | -
R261 | slide_number | p28 L424 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R262 | slide_number | p28 L423 | CORRECTED_FROM_IMAGE LAYOUT_TABLE_SLIDE | -
R263 | slide_number | p28 L424 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R264 | slide_number | p28 L425 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R265 | slide_number | p28 L424 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R266 | slide_number | p28 L424 | CORRECTED_FROM_IMAGE LAYOUT_TABLE_SLIDE | -
R267 | slide_number | p28 L425 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R268 | slide_number | p28 L425 | CORRECTED_FROM_IMAGE LAYOUT_TABLE_SLIDE | -
R269 | slide_number | p28 L426 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R270 | slide_number | p28 L426 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R271 | slide_number | p28 L425 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R272 | slide_number | p28 L425 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R273 | slide_number | p28 L425 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R274 | slide_number | p28 L426 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R275 | slide_number | p28 L425 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R276 | slide_number | p28 L427 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R277 | slide_number | p28 L427 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R278 | slide_number | p28 L427 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R279 | slide_number | p28 L426 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R280 | slide_number | p28 L426 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R281 | slide_number | p28 L426 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R282 | slide_number | p28 L427 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R283 | slide_number | p28 L426 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R284 | slide_number | p28 L428 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R285 | slide_number | p28 L428 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R286 | slide_number | p28 L428 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R287 | slide_number | p28 L427 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R288 | slide_number | p28 L427 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R289 | slide_number | p28 L427 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R290 | slide_number | p28 L428 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R291 | slide_number | p28 L427 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R292 | slide_number | p28 L429 | LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R293 | slide_number | p28 L423 | CORRECTED_FROM_IMAGE LAYOUT_TABLE_SLIDE | -
R294 | slide_number | p28 L424 | CORRECTED_FROM_IMAGE LAYOUT_TABLE_SLIDE | -
R295 | slide_number | p28 L427 | LAYOUT_TABLE_SLIDE | -
R296 | slide_number | p29 L433 | LAYOUT_TABLE_SLIDE | -
R297 | slide_number | p29 L433 | LAYOUT_TABLE_SLIDE | -
R298 | slide_number | p29 L433 | LAYOUT_TABLE_SLIDE | -
R299 | slide_number | p29 L433 | LAYOUT_TABLE_SLIDE | -
R300 | slide_number | p29 L433 | LAYOUT_TABLE_SLIDE | -
R301 | slide_number | p29 L434 | LAYOUT_TABLE_SLIDE | -
R302 | slide_number | p29 L434 | LAYOUT_TABLE_SLIDE | -
R303 | slide_number | p29 L434 | LAYOUT_TABLE_SLIDE | -
R304 | slide_number | p29 L434 | LAYOUT_TABLE_SLIDE | -
R305 | slide_number | p29 L434 | LAYOUT_TABLE_SLIDE | -
R306 | slide_number | p29 L435 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R307 | slide_number | p29 L435 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R308 | slide_number | p29 L435 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R309 | slide_number | p29 L435 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R310 | slide_number | p29 L435 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R311 | slide_number | p29 L436 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R312 | slide_number | p29 L436 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R313 | slide_number | p29 L436 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R314 | slide_number | p29 L436 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R315 | slide_number | p29 L436 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R316 | slide_number | p29 L437 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R317 | slide_number | p29 L437 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R318 | slide_number | p29 L437 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R319 | slide_number | p29 L437 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R320 | slide_number | p29 L437 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R321 | slide_number | p29 L438 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R322 | slide_number | p29 L438 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R323 | slide_number | p29 L438 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R324 | slide_number | p29 L438 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R325 | slide_number | p29 L438 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R326 | slide_number | p29 L439 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R327 | slide_number | p29 L439 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R328 | slide_number | p29 L439 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R329 | slide_number | p29 L439 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R330 | slide_number | p29 L439 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R331 | slide_number | p29 L440 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R332 | slide_number | p29 L440 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R333 | slide_number | p29 L440 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R334 | slide_number | p29 L440 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R335 | slide_number | p29 L440 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R336 | slide_number | p29 L441 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R337 | slide_number | p29 L441 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R338 | slide_number | p29 L441 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R339 | slide_number | p29 L441 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R340 | slide_number | p29 L441 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R341 | slide_number | p29 L442 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R342 | slide_number | p29 L442 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R343 | slide_number | p29 L442 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R344 | slide_number | p29 L442 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R345 | slide_number | p29 L442 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R346 | slide_number | p30 L447 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R347 | slide_number | p30 L447 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R348 | slide_number | p30 L448 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R349 | slide_number | p30 L448 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R350 | slide_number | p30 L449 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R351 | slide_number | p30 L449 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R352 | slide_number | p30 L450 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R353 | slide_number | p30 L450 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R354 | slide_number | p30 L451 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R355 | slide_number | p30 L451 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R356 | slide_number | p30 L452 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R357 | slide_number | p30 L452 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R358 | slide_number | p30 L453 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R359 | slide_number | p30 L453 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R360 | slide_number | p30 L454 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R361 | slide_number | p30 L454 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R362 | slide_number | p30 L455 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R363 | slide_number | p30 L455 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R364 | slide_number | p30 L456 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R365 | slide_number | p30 L456 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R366 | slide_number | p30 L458 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R367 | slide_number | p30 L458 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R368 | slide_number | p30 L447 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R369 | slide_number | p30 L448 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R370 | slide_number | p30 L448 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R371 | slide_number | p30 L450 | LAYOUT_SCRAMBLED LAYOUT_TABLE_SLIDE ZERO_STANDING | -
R372 | slide_number | p30 L449 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R373 | slide_number | p30 L451 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R374 | slide_number | p30 L450 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R375 | slide_number | p30 L452 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R376 | slide_number | p30 L451 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R377 | slide_number | p30 L452 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R378 | slide_number | p30 L453 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R379 | slide_number | p30 L454 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R380 | slide_number | p30 L455 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R381 | slide_number | p30 L456 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R382 | slide_number | p30 L458 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R383 | slide_number | p30 L457 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R384 | slide_number | p30 L459 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R385 | slide_number | p30 L454 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R386 | slide_number | p30 L455 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R387 | slide_number | p30 L456 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R388 | slide_number | p30 L457 | LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC LAYOUT_TABLE_SLIDE | -
R389 | slide_number | p32 L481 |  | -
R390 | slide_number | p34 L498 |  | -
R391 | slide_number | p34 L495 |  | -
R392 | slide_number | p34 L489 |  | -
R393 | slide_number | p34 L502 |  | -
R394 | slide_number | p34 L512 |  | -
R395 | slide_number | p34 L517 |  | -
R396 | slide_number | p34 L512 |  | -
R397 | slide_number | p34 L519 |  | -
R398 | slide_number | p36 L547 |  | -
R399 | slide_number | p36 L548 |  | -
R400 | slide_number | p36 L550 |  | -
R401 | slide_number | p36 L546 | CHART_LABEL_ORDER | -
R402 | slide_number | p36 L547 | CHART_LABEL_ORDER | -
R403 | slide_number | p36 L549 | CHART_LABEL_ORDER | -
R404 | slide_number | p36 L551 | CHART_LABEL_ORDER | -
R523 | slide_number | p28 L425 | CORRECTED_FROM_IMAGE LAYOUT_TABLE_SLIDE | A1 follow-up row (A5 M1)
R524 | slide_number | p28 L426 | CORRECTED_FROM_IMAGE LAYOUT_TABLE_SLIDE | A1 follow-up row (A5 M1)
R525 | slide_number | p30 L453 | LAYOUT_SCRAMBLED LAYOUT_TABLE_SLIDE ZERO_STANDING | A1 follow-up row (A5 M1)

## 3. ENTITIES (32)
ROW_ID | category | page/line | A2 flags | cross-ref / materiality
R405 | entity | p1 L18 | - | -
R406 | entity | p3 L42 | - | -
R407 | entity | p6 L92 | - | -
R408 | entity | p7 L113 | - | -
R409 | entity | p8 L129 | - | -
R410 | entity | p8 L128 | - | -
R411 | entity | p8 L128 | - | -
R412 | entity | p8 L135 | - | -
R413 | entity | p15 L209 | - | -
R414 | entity | p15 L209 | - | -
R415 | entity | p15 L209 | - | -
R416 | entity | p16 L238 | - | -
R417 | entity | p21 L322 | - | -
R418 | entity | p21 L310 | - | -
R419 | entity | p12 L193 | - | -
R420 | entity | p22 L336 | - | -
R421 | entity | p34 L486 | - | -
R422 | entity | p34 L500 | - | -
R423 | entity | p34 L500 | - | -
R424 | entity | p34 L510 | - | -
R425 | entity | p34 L510 | - | -
R426 | entity | p34 L492 | - | -
R427 | entity | p37 L560 | - | -
R428 | entity | p37 L557 | - | -
R429 | entity | p36 L544 | - | -
R430 | entity | p2 L23 | - | -
R431 | entity | p4 L59 | - | -
R432 | entity | p14 L198 | - | -
R433 | entity | p7 L121 | - | -
R434 | entity | p16 L239 | - | -
R435 | entity | p35 L524 | - | -
R436 | entity | p37 L555 | - | -

## 4. FORWARD-LOOKING STATEMENTS (25)
ROW_ID | category | page/line | A2 flags | cross-ref / materiality
R437 | forward | p3 L45 | FORWARD_LOOKING | -
R438 | forward | p3 L51 | FORWARD_LOOKING | -
R439 | forward | p3 L53 | FORWARD_LOOKING | -
R440 | forward | p3 L55 | FORWARD_LOOKING | -
R441 | forward | p10 L166 | FORWARD_LOOKING | -
R442 | forward | p12 L192 | FORWARD_LOOKING | -
R443 | forward | p15 L212 | FORWARD_LOOKING RESTATED | also R452,R456,R484
R444 | forward | p15 L216 | FORWARD_LOOKING RESTATED | also R050,R051
R445 | forward | p16 L244 | FORWARD_LOOKING | -
R446 | forward | p19 L296 | FORWARD_LOOKING | -
R447 | forward | p21 L325 | FORWARD_LOOKING | -
R448 | forward | p21 L315 | FORWARD_LOOKING | -
R449 | forward | p22 L337 | FORWARD_LOOKING | -
R450 | forward | p23 L353 | FORWARD_LOOKING | -
R451 | forward | p23 L358 | FORWARD_LOOKING | -
R452 | forward | p23 L361 | FORWARD_LOOKING RESTATED | also R443,R456,R484
R453 | forward | p32 L465 | FORWARD_LOOKING | -
R454 | forward | p32 L466 | FORWARD_LOOKING | -
R455 | forward | p32 L467 | FORWARD_LOOKING | -
R456 | forward | p32 L475 | FORWARD_LOOKING RESTATED | also R443,R452,R484
R457 | forward | p32 L474 | FORWARD_LOOKING | -
R458 | forward | p32 L481 | FORWARD_LOOKING | -
R459 | forward | p21 L326 | FORWARD_LOOKING | -
R460 | forward | p15 L214 | FORWARD_LOOKING | -
R461 | forward | p23 L366 | FORWARD_LOOKING | -

## 5. DATES (37)
ROW_ID | category | page/line | A2 flags | cross-ref / materiality
R462 | date | p8 L126 | - | -
R463 | date | p8 L126 | - | -
R464 | date | p8 L126 | - | -
R465 | date | p8 L126 | - | -
R466 | date | p8 L126 | - | -
R467 | date | p8 L132 | - | -
R468 | date | p8 L132 | - | -
R469 | date | p8 L132 | - | -
R470 | date | p8 L132 | - | -
R471 | date | p8 L138 | - | -
R472 | date | p8 L138 | - | -
R473 | date | p8 L138 | - | -
R474 | date | p8 L138 | - | -
R475 | date | p8 L138 | - | -
R476 | date | p1 L20 | - | -
R477 | date | p6 L91 | RESTATED | also R004,R136,R148,R196,R492,R502
R478 | date | p6 L94 | - | -
R479 | date | p9 L155 | - | -
R480 | date | p12 L177 | - | -
R481 | date | p12 L177 | - | -
R482 | date | p12 L177 | - | -
R483 | date | p12 L183 | - | -
R484 | date | p15 L212 | RESTATED | also R443,R452,R456
R485 | date | p15 L217 | - | -
R486 | date | p15 L217 | - | -
R487 | date | p18 L285 | - | -
R488 | date | p21 L309 | - | -
R489 | date | p21 L325 | - | -
R490 | date | p25 L381 | - | -
R491 | date | p26 L396 | - | -
R492 | date | p27 L409 | RESTATED | also R004,R136,R148,R196,R477,R502
R493 | date | p36 L533 | - | -
R494 | date | p36 L545 | - | -
R495 | date | p36 L545 | - | -
R496 | date | p32 L481 | - | -
R497 | date | p34 L495 | - | -
R498 | date | p34 L498 | - | -

## 6. FOOTNOTES AND QUALIFIERS (24)
ROW_ID | category | page/line | A2 flags | cross-ref / materiality
R499 | footnote_qualifier | p2 L27 | - | -
R500 | footnote_qualifier | p2 L28 | - | -
R501 | footnote_qualifier | p2 L31 | - | -
R502 | footnote_qualifier | p6 L91 | RESTATED | also R004,R136,R148,R196,R477,R492
R503 | footnote_qualifier | p6 L91 | - | -
R504 | footnote_qualifier | p9 L156 | - | -
R505 | footnote_qualifier | p12 L193 | - | -
R506 | footnote_qualifier | p15 L211 | - | -
R507 | footnote_qualifier | p15 L216 | - | -
R508 | footnote_qualifier | p17 L260 | - | -
R509 | footnote_qualifier | p17 L264 | - | -
R510 | footnote_qualifier | p21 L310 | - | -
R511 | footnote_qualifier | p21 L315 | - | -
R512 | footnote_qualifier | p21 L301 | - | -
R513 | footnote_qualifier | p28 L421 | - | -
R514 | footnote_qualifier | p28 L414 | - | -
R515 | footnote_qualifier | p29 L436 | - | -
R516 | footnote_qualifier | p29 L434 | - | -
R517 | footnote_qualifier | p29 L437 | - | -
R518 | footnote_qualifier | p30 L446 | - | -
R519 | footnote_qualifier | p27 L412 | - | -
R520 | footnote_qualifier | p36 L545 | - | -
R521 | footnote_qualifier | p36 L545 | - | -
R522 | footnote_qualifier | p25 L374 | - | -

## 7. ZERO_STANDING ROWS (3)
R097 | p17 L261 | ZERO_STANDING
R371 | p30 L450 | ZERO_STANDING
R525 | p30 L453 | ZERO_STANDING
R371 (L450) CWIP FY26 and R525 (L453) investments FY26 are dashes (LAYOUT_SCRAMBLED). Slide 23 shows Narmadapuram construction in progress. A3/A4 to check; A2 does not resolve.

## 8. LAYOUT FLAG REGISTER (carried from A1, none resolved by A2)
LAYOUT_ROW_LABELS_SHIFTED: 12
LAYOUT_SCRAMBLED: 28
LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC: 82
LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC: 88
LAYOUT_UNRESOLVED IDs: none (A1 correction log resolved R293-R295 and R385-R388)
LAYOUT_ROW_LABELS_SHIFTED IDs: R114-R125 (slide 18)
CORRECTED_FROM_IMAGE rows (A1 image check, slide 28): R260, R262, R266, R268, R293, R294, R523, R524
Layout-flagged row count by page: p17=26, p18=12, p28=88, p29=40, p30=44

## 9. MISSING_FROM_STRUCTURED
none found in sweep (page markers, dividers and page coverage checked; chart axis ticks and phone numbers excluded by A1 by stated rule).

## 10. DROPPED_SLIDE
Not testable: no prior-quarter deck or ledger supplied.

```yaml
stage: A2-enumerator
company: "PARACABLES"
quarter: "Q2 FY27"
doctype: "presentation"
model: claude-sonnet-5-5
status: complete
ledger_path: "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/qr-paracables-q2fy27-a220cd/runs/paracables-q2fy27/work/ledger_presentation_paracables_q2fy27.md"
counts:
  notes: 0
  line_items: 0
  zero_standing: 3
  agenda_items: 0
  auditor_paras: 0
  entities: 32
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 37
  slide_numbers: 407
flags_raised: [ZERO_STANDING, RESTATED, FORWARD_LOOKING, LAYOUT_SCRAMBLED, LAYOUT_SCRAMBLED_ASSIGNED_BY_ARITHMETIC, LAYOUT_SCRAMBLED_ROW_ASSIGNED_BY_ARITHMETIC, LAYOUT_ROW_LABELS_SHIFTED, CORRECTED_FROM_IMAGE]
ids_in_structured: 525
ids_referenced: 525
orphan_ids: []
missing_from_structured: []
gate_a2: pass
mismatch_note: ""
analyst_note: "Rebuilt after A1 follow-up (R523-R525, correction log). 210 NUMBER rows carry A1 LAYOUT flags (slides 17, 18, 28, 29, 30): 28 SCRAMBLED, 82+88 placed by arithmetic, 12 ROW_LABELS_SHIFTED (slide 18, R114-R125). A1 resolved the former LAYOUT_UNRESOLVED rows (R293-R295, R385-R388); none remain. CORRECTED_FROM_IMAGE rows: R260, R262, R266, R268 (depreciation and finance cost Q2/H1 FY26 swap fixed), R293, R294, R523, R524. ZERO_STANDING: R097, R371 (CWIP FY26, L450), R525 (investments FY26, L453); slide 23 shows Narmadapuram construction in progress, so check CWIP placement. 7 slides are dividers with no rows. No prior deck, so DROPPED_SLIDE untestable."
```
