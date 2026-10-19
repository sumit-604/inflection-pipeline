# LEDGER: Kross Q2 FY27 press release (A2)

ids_in_structured: 135 | ids_referenced_in_ledger: 135 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: notes (footnotes/qualifier rows)  grep_count: 6   sweep_count: 6   match: yes   (R088-R093; no numbered notes in a press release)
category: line_items (table cells, 7 rows x 6 cols)  grep_count: 42  sweep_count: 42  match: yes   (R094-R135; superseded twins R004-R045 = 42, match)
category: zero_standing  grep_count: 0   sweep_count: 0   match: yes
category: numbers_active (NUMBER minus superseded)  grep_count: 57  sweep_count: 57  match: yes  (R001-R003, R046-R057 =15 + R094-R135 =42)
category: entities  grep_count: 12  sweep_count: 12  match: yes
category: forward_statements  grep_count: 10  sweep_count: 10  match: yes
category: dates  grep_count: 8   sweep_count: 8   match: yes
category: superseded_ids  grep_count: 42  sweep_count: 42  match: yes
category: total_ids  grep_count: 135  sweep_count: 135  match: yes
gate_a2: pass
=== END COUNT TEST ===

Doctype adaptation: press release has no slides, turns, agenda, auditor report. Categories used: line items, numbers, entities, forwards, dates, qualifiers.

## 1. Financial table line items (page 1, fulltext L118-124, image transcription)
Metric rows x columns (Q2FY27, Q2FY26, Q2 YoY, H1FY27, H1FY26, H1 YoY). Superseded twin in brackets.
ROW_ID | category | A2 flags | cross-ref / note
R094 | line_item | CANONICAL | twin of R004 (superseded); Revenue
R095 | line_item | CANONICAL | twin of R005 (superseded); Revenue
R096 | line_item | CANONICAL | twin of R006 (superseded); Revenue
R097 | line_item | CANONICAL | twin of R007 (superseded); Revenue
R098 | line_item | CANONICAL | twin of R008 (superseded); Revenue
R099 | line_item | CANONICAL | twin of R009 (superseded); Revenue
R100 | line_item | CANONICAL | twin of R010 (superseded); TotalExp
R101 | line_item | CANONICAL | twin of R011 (superseded); TotalExp
R102 | line_item | CANONICAL | twin of R012 (superseded); TotalExp
R103 | line_item | CANONICAL | twin of R013 (superseded); TotalExp
R104 | line_item | CANONICAL | twin of R014 (superseded); TotalExp
R105 | line_item | CANONICAL | twin of R015 (superseded); TotalExp
R106 | line_item | CANONICAL | twin of R016 (superseded); EBITDA
R107 | line_item | CANONICAL | twin of R017 (superseded); EBITDA
R108 | line_item | CANONICAL | twin of R018 (superseded); EBITDA
R109 | line_item | CANONICAL | twin of R019 (superseded); EBITDA
R110 | line_item | CANONICAL | twin of R020 (superseded); EBITDA
R111 | line_item | CANONICAL | twin of R021 (superseded); EBITDA
R112 | line_item | CANONICAL | twin of R022 (superseded); EBITDAmargin
R113 | line_item | CANONICAL | twin of R023 (superseded); EBITDAmargin
R114 | line_item | CANONICAL | twin of R024 (superseded); EBITDAmargin
R115 | line_item | CANONICAL | twin of R025 (superseded); EBITDAmargin
R116 | line_item | CANONICAL | twin of R026 (superseded); EBITDAmargin
R117 | line_item | CANONICAL | twin of R027 (superseded); EBITDAmargin
R118 | line_item | CANONICAL | twin of R028 (superseded); PAT
R119 | line_item | CANONICAL | twin of R029 (superseded); PAT
R120 | line_item | CANONICAL | twin of R030 (superseded); PAT
R121 | line_item | CANONICAL | twin of R031 (superseded); PAT
R122 | line_item | CANONICAL | twin of R032 (superseded); PAT
R123 | line_item | CANONICAL | twin of R033 (superseded); PAT
R124 | line_item | CANONICAL | twin of R034 (superseded); PATmargin
R125 | line_item | CANONICAL | twin of R035 (superseded); PATmargin
R126 | line_item | CANONICAL | twin of R036 (superseded); PATmargin
R127 | line_item | CANONICAL | twin of R037 (superseded); PATmargin
R128 | line_item | CANONICAL | twin of R038 (superseded); PATmargin
R129 | line_item | CANONICAL | twin of R039 (superseded); PATmargin
R130 | line_item | CANONICAL | twin of R040 (superseded); EPS
R131 | line_item | CANONICAL | twin of R041 (superseded); EPS
R132 | line_item | CANONICAL | twin of R042 (superseded); EPS
R133 | line_item | CANONICAL | twin of R043 (superseded); EPS
R134 | line_item | CANONICAL | twin of R044 (superseded); EPS
R135 | line_item | CANONICAL | twin of R045 (superseded); EPS

## 2. Superseded IDs (account explicitly)
ROW_ID | category | A2 flags | cross-ref
R004 | superseded_number | SUPERSEDED_BY R094 | not reviewed; use R094
R005 | superseded_number | SUPERSEDED_BY R095 | not reviewed; use R095
R006 | superseded_number | SUPERSEDED_BY R096 | not reviewed; use R096
R007 | superseded_number | SUPERSEDED_BY R097 | not reviewed; use R097
R008 | superseded_number | SUPERSEDED_BY R098 | not reviewed; use R098
R009 | superseded_number | SUPERSEDED_BY R099 | not reviewed; use R099
R010 | superseded_number | SUPERSEDED_BY R100 | not reviewed; use R100
R011 | superseded_number | SUPERSEDED_BY R101 | not reviewed; use R101
R012 | superseded_number | SUPERSEDED_BY R102 | not reviewed; use R102
R013 | superseded_number | SUPERSEDED_BY R103 | not reviewed; use R103
R014 | superseded_number | SUPERSEDED_BY R104 | not reviewed; use R104
R015 | superseded_number | SUPERSEDED_BY R105 | not reviewed; use R105
R016 | superseded_number | SUPERSEDED_BY R106 | not reviewed; use R106
R017 | superseded_number | SUPERSEDED_BY R107 | not reviewed; use R107
R018 | superseded_number | SUPERSEDED_BY R108 | not reviewed; use R108
R019 | superseded_number | SUPERSEDED_BY R109 | not reviewed; use R109
R020 | superseded_number | SUPERSEDED_BY R110 | not reviewed; use R110
R021 | superseded_number | SUPERSEDED_BY R111 | not reviewed; use R111
R022 | superseded_number | SUPERSEDED_BY R112 | not reviewed; use R112
R023 | superseded_number | SUPERSEDED_BY R113 | not reviewed; use R113
R024 | superseded_number | SUPERSEDED_BY R114 | not reviewed; use R114
R025 | superseded_number | SUPERSEDED_BY R115 | not reviewed; use R115
R026 | superseded_number | SUPERSEDED_BY R116 | not reviewed; use R116
R027 | superseded_number | SUPERSEDED_BY R117 | not reviewed; use R117
R028 | superseded_number | SUPERSEDED_BY R118 | not reviewed; use R118
R029 | superseded_number | SUPERSEDED_BY R119 | not reviewed; use R119
R030 | superseded_number | SUPERSEDED_BY R120 | not reviewed; use R120
R031 | superseded_number | SUPERSEDED_BY R121 | not reviewed; use R121
R032 | superseded_number | SUPERSEDED_BY R122 | not reviewed; use R122
R033 | superseded_number | SUPERSEDED_BY R123 | not reviewed; use R123
R034 | superseded_number | SUPERSEDED_BY R124 | not reviewed; use R124
R035 | superseded_number | SUPERSEDED_BY R125 | not reviewed; use R125
R036 | superseded_number | SUPERSEDED_BY R126 | not reviewed; use R126
R037 | superseded_number | SUPERSEDED_BY R127 | not reviewed; use R127
R038 | superseded_number | SUPERSEDED_BY R128 | not reviewed; use R128
R039 | superseded_number | SUPERSEDED_BY R129 | not reviewed; use R129
R040 | superseded_number | SUPERSEDED_BY R130 | not reviewed; use R130
R041 | superseded_number | SUPERSEDED_BY R131 | not reviewed; use R131
R042 | superseded_number | SUPERSEDED_BY R132 | not reviewed; use R132
R043 | superseded_number | SUPERSEDED_BY R133 | not reviewed; use R133
R044 | superseded_number | SUPERSEDED_BY R134 | not reviewed; use R134
R045 | superseded_number | SUPERSEDED_BY R135 | not reviewed; use R135

## 3. Other numbers (active)
ROW_ID | category | A2 flags | cross-ref / note
R001 | headline_number | RESTATED | = R096 (79.6% revenue YoY)
R002 | headline_number | RESTATED | = R108 (107.4% EBITDA YoY)
R003 | headline_number | RESTATED | = R120 (143.5% PAT YoY)
R046 | bullet_number | RESTATED | = R094
R047 | bullet_number | RESTATED | = R095
R048 | bullet_number | RESTATED | = R106
R049 | bullet_number | RESTATED | = R107
R050 | bullet_number | RESTATED | = R118
R051 | bullet_number | RESTATED | = R119
R052 | bullet_number | RESTATED | = R112, R113, R114
R053 | bullet_number | RESTATED | = R124, R125, R126
R054 | operating_number | - | axle beam utilisation 60-65%; only operating metric; material (capacity headroom)
R055 | descriptive_number | - | = R087
R056 | identifier | - | BSE code
R057 | contact | - | phones

## 4. Entities
R058-R069 | entity | - | 12 rows. R069 contact block (ENTITY-SUMMARY). No customer named (A1 note L97). R059 CMD Sudhir Rai quoted at R076-R079.

## 5. Forward statements
R070-R079 | forward | - | 10 rows. Dated: R070 (H2 FY27 = R084), R071 (Feb-Mar 2027 = R085), R077 (FY27 = R086). Undated: R072-R076, R078, R079. No numeric guidance (revenue/margin/capex) given.

## 6. Dates
R080-R087 | date | - | 8 rows. R087 = R055.

## 7. Qualifiers / footnotes
R088 | qualifier | - | standalone basis
R089 | qualifier | - | unit INR million
R090 | qualifier | FOOTNOTE_UNRESOLVED | layout scramble; resolved by image transcription R094-R135
R091 | qualifier | - | driver attribution, no quantified split
R092 | qualifier | - | safe-harbor
R093 | qualifier | - | margin driver, input cost pressure mentioned unquantified

## Flags
RESTATED (R001-R003, R046-R053), FOOTNOTE_UNRESOLVED (R090, resolved), SUPERSEDED (R004-R045). ZERO_STANDING none: table has no nil rows. Note: table omits other income, D&A, interest, PBT, tax; standalone only; no segment or balance-sheet data.
