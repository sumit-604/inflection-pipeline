# A2 LEDGER: press (media release) WEWORK q2fy27

ids_in_structured: 197 | ids_referenced_in_ledger: 197 | orphan_ids: [] | match: yes

```
=== A2 COUNT TEST ===
method 1 (structured header counts vs row sweep):
category: number rows      grep_count: 136  sweep_count: 136  match: yes
category: entities (17 ENTITY + 3 ENTITY-SUMMARY)  grep_count: 20  sweep_count: 20  match: yes
category: forward rows     grep_count: 12  sweep_count: 12  match: yes
category: date rows        grep_count: 15  sweep_count: 15  match: yes
category: qualifier rows   grep_count: 14  sweep_count: 14  match: yes
category: total ids        grep_count: 197 sweep_count: 197 match: yes
category: notes            grep_count: 1   sweep_count: 1   match: yes  (unnumbered Note on page 4, R184-R185; no numbered notes)
category: line_items       grep_count: 0   sweep_count: 0   match: yes  (no financial tables)
category: zero_standing    grep_count: 0   sweep_count: 0   match: yes  (no dash or nil items in fulltext)
category: slides (pages)   grep_count: 5   sweep_count: 5   match: yes  (page markers fulltext lines 17, 67, 122, 168, 215)
method 2 (independent fulltext numeric-token sweep per page vs structured NUMBER rows):
page 1: fulltext tokens 24 | NUMBER rows 4 (7 tokens) | remainder 17 = address/PIN in R142 (7), letter date R169 (2), results period R171 (2), signature timestamp R170 (6) | match: yes
page 2: fulltext tokens 93 | NUMBER rows 70 (70 tokens) | period labels Q/H/FY 18 | remainder 5 = R172 (26, 2026), R173 (30, 2026), R176 (2026) | match: yes
page 3: fulltext tokens 55 | NUMBER rows 44 (43 tokens; R081 eight cities is a word) | period labels 10 | remainder 2 = R179 (12 months), R158 (2026) | match: yes
page 4: fulltext tokens 25 | NUMBER rows 18 (16 tokens; R132 three and R135 eight are words) | period labels 6 | remainder 3 = R184 (IndAS 116), R181 (2017), R150 (Fortune 500) | match: yes
page 5: fulltext tokens 0 | NUMBER rows 0 | match: yes
page totals: NUMBER rows 4+70+44+18+0 = 136 = header count 136
differences explained: every fulltext numeric token maps to a NUMBER, DATE, ENTITY or QUALIFIER row. MISSING_FROM_STRUCTURED: none.
anchor defects (value present, A1 line number off by one): R005, R074, R088, R116, R118. Flag LINE_ANCHOR_OFF. Values are correct.
gate_a2: pass
=== END COUNT TEST ===
```

Period labels (Q2 FY27, H1 FY27, Q3 CY2026) are DATE rows R174-R177, not repeated as numbers.

## 1. Cover letter identifiers (page 1 numbers)
ROW_ID | category | A2 flags | cross-ref / materiality note
--- | --- | --- | ---
R001 | p1 L28 identifier | - | -
R002 | p1 L37 identifier | - | -
R003 | p1 L63 identifier | - | -
R004 | p1 L26 identifier | - | -
count: 4

## 2. Page 2 numbers
ROW_ID | category | A2 flags | cross-ref / materiality note
--- | --- | --- | ---
R005 | p2 L68 number | RESTATED, LINE_ANCHOR_OFF | same value as R021, R088; line anchor says 68, value is at fulltext line 70
R006 | p2 L70 number | RESTATED | same value as R019, R089
R007 | p2 L70 number | RESTATED | same value as R024, R092
R008 | p2 L72 number | RESTATED | same value as R030, R098
R009 | p2 L74 number | RESTATED | same value as R044
R010 | p2 L74 number | RESTATED | same value as R048, R079
R011 | p2 L75 number | RESTATED | same value as R034, R119
R012 | p2 L75 number | RESTATED | same value as R035, R120
R013 | p2 L75 number | RESTATED | same value as R041, R125
R014 | p2 L77 number | RESTATED | same value as R075
R015 | p2 L77 number | RESTATED | same value as R076, R136
R016 | p2 L77 number | RESTATED | same value as R078
R017 | p2 L77 number | RESTATED | same value as R077
R018 | p2 L78 number | RESTATED | same value as R047
R019 | p2 L80 number | RESTATED | same value as R006, R089
R020 | p2 L80 number | RESTATED | same value as R090
R021 | p2 L80 number | RESTATED | same value as R005, R088
R022 | p2 L80 number | RESTATED | same value as R093
R023 | p2 L80 number | RESTATED | same value as R094
R024 | p2 L81 number | RESTATED | same value as R007, R092
R025 | p2 L81 number | RESTATED | same value as R095
R026 | p2 L81 number | RESTATED | same value as R097
R027 | p2 L81 number | RESTATED | same value as R096
R028 | p2 L81 number | RESTATED | same value as R099
R029 | p2 L82 number | RESTATED | same value as R100
R030 | p2 L82 number | RESTATED | same value as R008, R098
R031 | p2 L82 number | RESTATED | same value as R101
R032 | p2 L82 number | RESTATED | same value as R103
R033 | p2 L82 number | RESTATED | same value as R102
R034 | p2 L84 number | RESTATED | same value as R011, R119
R035 | p2 L84 number | RESTATED | same value as R012, R120
R036 | p2 L84 number | RESTATED | same value as R122
R037 | p2 L84 number | RESTATED | same value as R121
R038 | p2 L85 number | RESTATED | same value as R124
R039 | p2 L85 number | RESTATED | same value as R123
R040 | p2 L85 number | RESTATED | same value as R126
R041 | p2 L85 number | RESTATED | same value as R013, R125
R042 | p2 L86 number | RESTATED | same value as R128
R043 | p2 L86 number | RESTATED | same value as R127
R044 | p2 L88 number | RESTATED | same value as R009
R045 | p2 L89 number | - | -
R046 | p2 L89 number | - | -
R047 | p2 L89 number | RESTATED | same value as R018
R048 | p2 L89 number | RESTATED | same value as R010, R079
R049 | p2 L90 number | RESTATED | same value as R086
R050 | p2 L92 number | RESTATED | same value as R107
R051 | p2 L92 number | RESTATED | same value as R108
R052 | p2 L93 number | RESTATED | same value as R106
R053 | p2 L93 number | RESTATED | same value as R109
R054 | p2 L93 number | RESTATED | same value as R111
R055 | p2 L94 number | RESTATED | same value as R112
R056 | p2 L94 number | RESTATED | same value as R110
R057 | p2 L94 number | RESTATED | same value as R113
R058 | p2 L94 number | RESTATED | same value as R115
R059 | p2 L94 number | RESTATED | same value as R114
R060 | p2 L95 number | RESTATED | same value as R118
R061 | p2 L98 number | RESTATED | same value as R091
R062 | p2 L100 number | RESTATED | same value as R104
R063 | p2 L102 number | - | -
R064 | p2 L102 number | - | -
R065 | p2 L102 number | RESTATED | same value as R082, R134
R066 | p2 L103 number | RESTATED | same value as R080, R133
R067 | p2 L103 number | RESTATED | same value as R081, R135
R068 | p2 L103 number | RESTATED | same value as R087, R131
R069 | p2 L104 number | - | -
R070 | p2 L104 number | - | -
R071 | p2 L104 number | - | -
R072 | p2 L105 number | - | -
R073 | p2 L105 number | - | -
R074 | p2 L114 number | LINE_ANCHOR_OFF | line anchor says 114, value is at fulltext line 115
count: 70

## 3. Page 3 numbers
ROW_ID | category | A2 flags | cross-ref / materiality note
--- | --- | --- | ---
R075 | p3 L123 number | RESTATED | same value as R014
R076 | p3 L124 number | RESTATED | same value as R015, R136
R077 | p3 L124 number | RESTATED | same value as R017
R078 | p3 L124 number | RESTATED | same value as R016
R079 | p3 L124 number | RESTATED | same value as R010, R048
R080 | p3 L127 number | RESTATED | same value as R066, R133
R081 | p3 L127 number | RESTATED | same value as R067, R135
R082 | p3 L127 number | RESTATED | same value as R065, R134
R083 | p3 L128 number | - | -
R084 | p3 L128 number | - | -
R085 | p3 L129 number | - | -
R086 | p3 L130 number | RESTATED | same value as R049
R087 | p3 L132 number | RESTATED | same value as R068, R131
R088 | p3 L135 number | RESTATED, LINE_ANCHOR_OFF | same value as R005, R021; line anchor says 135, value is at fulltext line 136
R089 | p3 L136 number | RESTATED | same value as R006, R019
R090 | p3 L136 number | RESTATED | same value as R020
R091 | p3 L137 number | RESTATED | same value as R061
R092 | p3 L138 number | RESTATED | same value as R007, R024
R093 | p3 L138 number | RESTATED | same value as R022
R094 | p3 L138 number | RESTATED | same value as R023
R095 | p3 L138 number | RESTATED | same value as R025
R096 | p3 L139 number | RESTATED | same value as R027
R097 | p3 L139 number | RESTATED | same value as R026
R098 | p3 L140 number | RESTATED | same value as R008, R030
R099 | p3 L140 number | RESTATED | same value as R028
R100 | p3 L140 number | RESTATED | same value as R029
R101 | p3 L140 number | RESTATED | same value as R031
R102 | p3 L140 number | RESTATED | same value as R033
R103 | p3 L140 number | RESTATED | same value as R032
R104 | p3 L142 number | RESTATED | same value as R062
R105 | p3 L142 number | - | -
R106 | p3 L147 number | RESTATED | same value as R052
R107 | p3 L147 number | RESTATED | same value as R050
R108 | p3 L147 number | RESTATED | same value as R051
R109 | p3 L147 number | RESTATED | same value as R053
R110 | p3 L148 number | RESTATED | same value as R056
R111 | p3 L148 number | RESTATED | same value as R054
R112 | p3 L148 number | RESTATED | same value as R055
R113 | p3 L149 number | RESTATED | same value as R057
R114 | p3 L149 number | RESTATED | same value as R059
R115 | p3 L149 number | RESTATED | same value as R058
R116 | p3 L149 number | LINE_ANCHOR_OFF | line anchor says 149, value is at fulltext line 150
R117 | p3 L150 number | - | -
R118 | p3 L150 number | RESTATED, LINE_ANCHOR_OFF | same value as R060; line anchor says 150, value is at fulltext line 151
count: 44

## 4. Page 4 numbers
ROW_ID | category | A2 flags | cross-ref / materiality note
--- | --- | --- | ---
R119 | p4 L172 number | RESTATED | same value as R011, R034
R120 | p4 L173 number | RESTATED | same value as R012, R035
R121 | p4 L173 number | RESTATED | same value as R037
R122 | p4 L173 number | RESTATED | same value as R036
R123 | p4 L173 number | RESTATED | same value as R039
R124 | p4 L173 number | RESTATED | same value as R038
R125 | p4 L174 number | RESTATED | same value as R013, R041
R126 | p4 L174 number | RESTATED | same value as R040
R127 | p4 L174 number | RESTATED | same value as R043
R128 | p4 L174 number | RESTATED | same value as R042
R129 | p4 L175 number | - | -
R130 | p4 L175 number | - | -
R131 | p4 L185 number | RESTATED | same value as R068, R087
R132 | p4 L198 number | - | -
R133 | p4 L198 number | RESTATED | same value as R066, R080
R134 | p4 L199 number | RESTATED | same value as R065, R082
R135 | p4 L199 number | RESTATED | same value as R067, R081
R136 | p4 L200 number | RESTATED | same value as R015, R076
count: 18

## 5. Entities
ROW_ID | category | A2 flags | cross-ref / materiality note
--- | --- | --- | ---
R137 | p1 L32 entity | - | -
R138 | p1 L32 entity | - | -
R139 | p1 L18 entity | - | -
R140 | p1 L56 entity | - | -
R141 | p1 L37 entity | - | -
R142 | p1 L22 entity | - | -
R143 | p2 L114 entity | - | -
R144 | p2 L98 entity | - | -
R145 | p2 L95 entity | - | rating agency not named
R146 | p3 L154 entity | - | -
R147 | p3 L142 entity | - | -
R148 | p4 L180 entity | - | -
R149 | p4 L199 entity | - | -
R150 | p4 L200 entity | - | -
R151 | p4 L206 entity | - | -
R152 | p4 L208 entity | - | -
R153 | p4 L201 entity | - | -
R154 | p4 L193 entity | - | -
R155 | p2 L105 entity | - | -
R156 | p4 L212 entity | - | -
count: 20

## 6. Forward-looking statements
ROW_ID | category | A2 flags | cross-ref / materiality note
--- | --- | --- | ---
R157 | p2 L88 forward statement | - | -
R158 | p3 L130 forward statement | - | -
R159 | p3 L132 forward statement | - | -
R160 | p4 L185 forward statement | - | -
R161 | p4 L188 forward statement | - | -
R162 | p3 L166 forward statement | - | -
R163 | p3 L151 forward statement | - | -
R164 | p2 L112 forward statement | - | -
R165 | p3 L165 forward statement | - | -
R166 | p3 L154 forward statement | - | -
R167 | p3 L157 forward statement | - | -
R168 | p4 L201 forward statement | - | -
count: 12

## 7. Dates and periods
ROW_ID | category | A2 flags | cross-ref / materiality note
--- | --- | --- | ---
R169 | p1 L30 date/period | - | -
R170 | p1 L59 date/period | - | signature 21:07:59 IST on 26-Oct-2026; board meeting times not in this document
R171 | p1 L44 date/period | - | -
R172 | p2 L108 date/period | - | -
R173 | p2 L109 date/period | - | -
R174 | p2 L68 date/period | - | -
R175 | p2 L84 date/period | - | -
R176 | p2 L90 date/period | - | -
R177 | p2 L114 date/period | - | -
R178 | p2 L115 date/period | - | -
R179 | p3 L128 date/period | - | -
R180 | p3 L150 date/period | - | -
R181 | p4 L197 date/period | - | -
R182 | p4 L198 date/period | - | -
R183 | p4 L201 date/period | - | -
count: 15

## 8. Footnotes, notes and qualifiers
ROW_ID | category | A2 flags | cross-ref / materiality note
--- | --- | --- | ---
R184 | p4 L191 footnote/qualifier | NOTE_BASIS | note 1, unnumbered; IGAAP-equivalent basis
R185 | p4 L193 footnote/qualifier | FOOTNOTE_UNRESOLVED | reconciliation held in investor presentation, not in this release
R186 | p1 L43 footnote/qualifier | UNAUDITED | results unaudited; no auditor paragraph in this release
R187 | p1 L41 footnote/qualifier | UNAUDITED | results unaudited; no auditor paragraph in this release
R188 | p2 L98 footnote/qualifier | - | core revenue undefined
R189 | p2 L103 footnote/qualifier | RESTATED | same definition as R192; includes LOIs
R190 | p2 L74 footnote/qualifier | - | record claim, no prior-period comparator
R191 | p2 L116 footnote/qualifier | - | -
R192 | p3 L132 footnote/qualifier | RESTATED | same definition as R189; includes LOIs
R193 | p3 L128 footnote/qualifier | - | -
R194 | p3 L146 footnote/qualifier | - | capex funding claim; no capex figure in release
R195 | p3 L123 footnote/qualifier | - | -
R196 | p2 L93 footnote/qualifier | - | formula not stated
R197 | p4 L207 footnote/qualifier | - | -
count: 14

## 9. Page inventory (slide equivalent)
page | content type | note
--- | --- | ---
1 | text, cover letter to NSE/BSE | R001-R004, R137-R142, R169-R171, R186-R187
2 | text, headline bullets and opening narrative | numbers R005-R074
3 | text, narrative and CEO quote | numbers R075-R118
4 | text, narrative, note, about, safe harbour start | numbers R119-R136
5 | text, safe harbour continuation, no numbers | R156, R168, R197

## 10. ZERO_STANDING
none. No tables, no nil or dash items. Net cash 23.1 Cr (R116) and net debt 310.5 Cr a year ago (R117) are non-zero.

## 11. Absence observations (enumerated, not interpreted)
- No tables: no segment, rent, lease liability, capex, debt or cash balance disclosure. Growth rates and selected levels only; Q1 FY27 and Q2 FY26 absolute comparators not stated.
- Capex amount not given though R194 says H1 capex was fully funded from operating cash flow. Net debt comparator is a year ago (R180), no date.
- Rating agency for A+ (R145) not named; core revenue (R188) undefined; FCFF and FCFO formulas not stated (R196).
- All financials IGAAP-equivalent, excluding IndAS 116 straight-lining (R184); reconciliation not in this release (R185).
- No board meeting times and no auditor or limited-review paragraph: media release only.
```yaml
stage: A2-enumerator
company: "WEWORK"
quarter: "q2fy27"
doctype: "press"
model: claude-sonnet-5-5
status: complete
ledger_path: "runs/wework-q2fy27/work/ledger_press_wework_q2fy27.md"
counts:
  notes: 1
  line_items: 0
  zero_standing: 0
  agenda_items: 0
  auditor_paras: 0
  entities: 20
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 5
  slide_numbers: 136
flags_raised: [RESTATED, LINE_ANCHOR_OFF, FOOTNOTE_UNRESOLVED, UNAUDITED, NOTE_BASIS]
ids_in_structured: 197
ids_referenced: 197
orphan_ids: []
missing_from_structured: []
gate_a2: pass
mismatch_note: ""
analyst_note: "Press release, no tables, so no line items or ZERO_STANDING. Fulltext numeric sweep per page reconciles to structured NUMBER rows (4/70/44/18/0 = 136); every leftover token maps to a DATE, ENTITY or QUALIFIER row. Five A1 line anchors are off by one (R005, R074, R088, R116, R118); values are correct, but A3/A4 should cite page, not line, for these. Absences worth A3 attention: no capex amount despite the H1 fully-funded-by-operating-cash claim (R194), rating agency unnamed (R145), core revenue and FCFO/FCFF formulas undefined (R188, R196), IGAAP-equivalent basis excludes IndAS 116 straight-lining with reconciliation held in the investor presentation (R184, R185). 'Largest half-year of openings' (R190) has no comparator."
```
