# A2 ENUMERATION LEDGER: Tejas Networks (TEJASNET), Q2 FY27, Doctype: presentation
Source: A1 structured extraction only (R001-R210). Cover p1 is BSE letter; slides = pp2-13.
Prior-quarter baseline: Q1 FY27 ledger was a 3-page PRESS RELEASE (not a deck), so slide-level DROPPED_SLIDE diff is basis-limited. Q1 carried an 'About Tejas' profile, a SAFE HARBOUR disclaimer and MD/CFO quotes; none appear in the Q2 deck (see R210 and Table 2).

ids_in_structured: 210 | ids_referenced_in_ledger: 210 | orphan_ids: [] | match: yes

```
=== A2 COUNT TEST ===
category: slides             grep_count: 13   sweep_count: 13   match: yes (page tags p1-p13)
category: slide_numbers      grep_count: 98   sweep_count: 98   match: yes (R001-R098)
category: entities           grep_count: 29   sweep_count: 29   match: yes (R099-R127, incl 2 summary)
category: forward_statements grep_count: 48   sweep_count: 48   match: yes (R128-R175)
category: dates              grep_count: 15   sweep_count: 15   match: yes (R176-R190)
category: footnotes_qualifiers grep_count: 20 sweep_count: 20   match: yes (R191-R210)
category: zero_standing      grep_count: 3    sweep_count: 3    match: yes (R024,R026,R028)
category: all_ids            grep_count: 210  sweep_count: 210  match: yes (per-page sum 14+5+23+48+32+19+6+8+23+14+8+8+2=210; no duplicate IDs)
gate_a2: pass
=== END COUNT TEST ===
```

## TABLE 1: SLIDE INVENTORY

| Page | Slide title (inferred from A1 contexts) | Content type | A1 rows | Flags |
|---|---|---|---|---|
| 1 | BSE cover letter (Reg 30 / 46 intimation) | text+signature | R001-R178 (14) | cover, not a slide |
| 2 | Title: Q2FY27 results presentation, 16-Oct-2026 | text | R126-R210 (5) |  |
| 3 | Q2-FY27 key updates | text+table+KPI | R006-R209 (23) |  |
| 4 | Financial update | table+callouts | R019-R198 (48) |  |
| 5 | Balance sheet update | table+callouts | R060-R205 (32) |  |
| 6 | Order wins / business updates | text | R081-R135 (19) |  |
| 7 | Recognitions, IP and standards | text | R085-R118 (6) |  |
| 8 | IMC 2026 and 6G showcase | text+photo | R087-R189 (8) |  |
| 9 | Market drivers, wireless and wireline | text+chart (image data) | R089-R208 (23) | CHART_DATA_NOT_EXTRACTED |
| 10 | Product focus | text | R096-R159 (14) |  |
| 11 | Business and finance/ops focus | text | R124-R166 (8) |  |
| 12 | Key takeaways | text | R167-R174 (8) |  |
| 13 | Contact / thank you | text | R098-R125 (2) |  |

## TABLE 2: DROPPED_SLIDE vs Q1 FY27

| Item in Q1 FY27 document | In Q2 deck | Flag |
|---|---|---|
| SAFE HARBOUR forward-looking disclaimer | absent (R210) | DROPPED_SLIDE |
| About Tejas Networks company profile | absent | DROPPED_SLIDE |
| MD and CFO quotes | absent | DROPPED_SLIDE (basis: press release vs deck) |
| Headline P&L table | present, expanded on p4 (R019-R053) | none |

## TABLE 3: ROW LEDGER

| ROW_ID | page/line | category | A2 flags | cross-ref / note |
|---|---|---|---|---|
| R001 | p1 L23 | slide_number |  |  |
| R002 | p1 L30 | slide_number |  |  |
| R003 | p1 L30 | slide_number |  |  |
| R004 | p1 L30 | slide_number |  |  |
| R005 | p1 L43 | slide_number |  | signature time stamp |
| R006 | p3 L58 | slide_number |  | RESTATED R019,R029,R054 |
| R007 | p3 L58 | slide_number |  | RESTATED R030,R055 |
| R008 | p3 L59 | slide_number |  | RESTATED R049,R058 |
| R009 | p3 L59 | slide_number |  | RESTATED R050,R059 |
| R010 | p3 L85 | slide_number |  | order book basis undefined, see R209 |
| R011 | p3 L85 | slide_number |  | Q1 order book; matches prior ledger 1,529 |
| R012 | p3 L87 | slide_number |  |  |
| R013 | p3 L88 | slide_number |  |  |
| R014 | p3 L90 | slide_number |  |  |
| R015 | p3 L91 | slide_number |  |  |
| R016 | p3 L93 | slide_number |  | related R081 (18k+ vs 18,685); R128,R129 |
| R017 | p3 L97 | slide_number |  | cumulative R018,R085 |
| R018 | p3 L97 | slide_number |  | RESTATED R085 |
| R019 | p4 L128 | slide_number |  | RESTATED R006,R029,R054 |
| R020 | p4 L128 | slide_number |  | sales and service 257 + other op 5 = R030 262 |
| R021 | p4 L128 | slide_number |  |  |
| R022 | p4 L128 | slide_number |  |  |
| R023 | p4 L128 | slide_number |  | Q1 revenue matches prior ledger 402; also R033 |
| R024 | p4 L129 | slide_number | ZERO_STANDING |  |
| R025 | p4 L129 | slide_number |  |  |
| R026 | p4 L129 | slide_number | ZERO_STANDING |  |
| R027 | p4 L129 | slide_number |  |  |
| R028 | p4 L129 | slide_number | ZERO_STANDING |  |
| R029 | p4 L130 | slide_number |  | RESTATED R006,R019,R054 |
| R030 | p4 L130 | slide_number |  | RESTATED R007,R055 |
| R031 | p4 L130 | slide_number |  |  |
| R032 | p4 L130 | slide_number |  |  |
| R033 | p4 L130 | slide_number |  | Q1 matches prior ledger 402 |
| R034 | p4 L131 | slide_number |  | RESTATED R056 |
| R035 | p4 L131 | slide_number |  | RESTATED R057 |
| R036 | p4 L131 | slide_number |  |  |
| R037 | p4 L131 | slide_number |  |  |
| R038 | p4 L131 | slide_number |  |  |
| R039 | p4 L132 | slide_number |  |  |
| R040 | p4 L132 | slide_number |  |  |
| R041 | p4 L132 | slide_number |  |  |
| R042 | p4 L132 | slide_number |  |  |
| R043 | p4 L132 | slide_number |  |  |
| R044 | p4 L133 | slide_number |  |  |
| R045 | p4 L133 | slide_number |  |  |
| R046 | p4 L133 | slide_number |  |  |
| R047 | p4 L133 | slide_number |  |  |
| R048 | p4 L133 | slide_number |  | Q1 PBT (271) matches prior ledger |
| R049 | p4 L134 | slide_number |  | RESTATED R008,R058 |
| R050 | p4 L134 | slide_number |  | RESTATED R009,R059 |
| R051 | p4 L134 | slide_number |  |  |
| R052 | p4 L134 | slide_number |  |  |
| R053 | p4 L134 | slide_number |  | Q1 PAT (202) matches prior ledger |
| R054 | p4 L135 | slide_number |  | RESTATED R006,R019,R029 |
| R055 | p4 L135 | slide_number |  | RESTATED R007,R030 |
| R056 | p4 L136 | slide_number |  | RESTATED R034 |
| R057 | p4 L136 | slide_number |  | RESTATED R035 |
| R058 | p4 L138 | slide_number |  | RESTATED R008,R049 |
| R059 | p4 L138 | slide_number |  | RESTATED R009,R050 |
| R060 | p5 L163 | slide_number |  |  |
| R061 | p5 L163 | slide_number |  | RESTATED R076 |
| R062 | p5 L163 | slide_number |  | RESTATED R075 |
| R063 | p5 L166 | slide_number |  |  |
| R064 | p5 L166 | slide_number |  |  |
| R065 | p5 L166 | slide_number |  |  |
| R066 | p5 L167 | slide_number |  |  |
| R067 | p5 L167 | slide_number |  | RESTATED R078 |
| R068 | p5 L167 | slide_number |  | RESTATED R077 |
| R069 | p5 L168 | slide_number |  |  |
| R070 | p5 L168 | slide_number |  | Q1 cash matches prior ledger 589 |
| R071 | p5 L168 | slide_number |  |  |
| R072 | p5 L169 | slide_number |  |  |
| R073 | p5 L169 | slide_number |  | RESTATED R080; Q1 net debt matches prior ledger |
| R074 | p5 L169 | slide_number |  | RESTATED R079 |
| R075 | p5 L170 | slide_number |  | RESTATED R062 |
| R076 | p5 L170 | slide_number |  | RESTATED R061 |
| R077 | p5 L173 | slide_number |  | RESTATED R068 |
| R078 | p5 L173 | slide_number |  | RESTATED R067 |
| R079 | p5 L176 | slide_number |  | RESTATED R074 |
| R080 | p5 L176 | slide_number |  | RESTATED R073 |
| R081 | p6 L187 | slide_number |  | related R016 |
| R082 | p6 L184 | slide_number |  |  |
| R083 | p6 L187 | slide_number |  |  |
| R084 | p6 L200 | slide_number |  |  |
| R085 | p7 L223 | slide_number |  | RESTATED R018 |
| R086 | p7 L229 | slide_number |  |  |
| R087 | p8 L237 | slide_number |  |  |
| R088 | p8 L233 | slide_number |  |  |
| R089 | p9 L254 | slide_number |  | RESTATED R140 |
| R090 | p9 L254 | slide_number |  |  |
| R091 | p9 L252 | slide_number |  | RESTATED R139,R187 |
| R092 | p9 L251 | slide_number | CHART_DATA_NOT_EXTRACTED | chart p9 |
| R093 | p9 L247 | slide_number | CHART_DATA_NOT_EXTRACTED | chart p9 |
| R094 | p9 L271 | slide_number | CHART_DATA_NOT_EXTRACTED | chart p9 |
| R095 | p9 L272 | slide_number |  |  |
| R096 | p10 L284 | slide_number |  |  |
| R097 | p10 L293 | slide_number |  |  |
| R098 | p13 L347 | slide_number |  |  |
| R099 | p1 L18 | entity |  |  |
| R100 | p1 L19 | entity |  |  |
| R101 | p1 L38 | entity |  |  |
| R102 | p1 L40 | entity |  |  |
| R103 | p1 L30 | entity |  |  |
| R104 | p3 L69 | entity |  |  |
| R105 | p3 L72 | entity |  |  |
| R106 | p3 L71 | entity |  |  |
| R107 | p6 L187 | entity |  |  |
| R108 | p6 L184 | entity |  |  |
| R109 | p6 L185 | entity |  |  |
| R110 | p6 L190 | entity |  |  |
| R111 | p6 L198 | entity |  |  |
| R112 | p6 L201 | entity |  |  |
| R113 | p6 L195 | entity |  |  |
| R114 | p6 L199 | entity |  |  |
| R115 | p7 L209 | entity |  |  |
| R116 | p7 L209 | entity |  |  |
| R117 | p7 L217 | entity |  |  |
| R118 | p7 L229 | entity |  |  |
| R119 | p8 L237 | entity |  |  |
| R120 | p8 L238 | entity |  |  |
| R121 | p8 L242 | entity |  |  |
| R122 | p8 L241 | entity |  |  |
| R123 | p9 L276 | entity |  | chart p9 |
| R124 | p11 L308 | entity |  |  |
| R125 | p13 L346 | entity |  |  |
| R126 | p2 L54 | entity |  | repeats pp2-13 |
| R127 | p1 L18 | entity |  |  |
| R128 | p3 L69 | forward_statement |  |  |
| R129 | p6 L187 | forward_statement |  |  |
| R130 | p6 L185 | forward_statement |  |  |
| R131 | p6 L190 | forward_statement |  | L1 only, award pending |
| R132 | p6 L196 | forward_statement |  |  |
| R133 | p6 L195 | forward_statement |  |  |
| R134 | p6 L199 | forward_statement |  |  |
| R135 | p6 L201 | forward_statement |  |  |
| R136 | p5 L174 | forward_statement |  | links R068 |
| R137 | p5 L175 | forward_statement |  | links R129 |
| R138 | p9 L251 | forward_statement |  |  |
| R139 | p9 L252 | forward_statement |  |  |
| R140 | p9 L254 | forward_statement |  | RESTATED R089 |
| R141 | p9 L257 | forward_statement |  |  |
| R142 | p9 L258 | forward_statement |  |  |
| R143 | p9 L265 | forward_statement |  |  |
| R144 | p9 L269 | forward_statement |  |  |
| R145 | p9 L270 | forward_statement |  |  |
| R146 | p9 L271 | forward_statement |  |  |
| R147 | p9 L274 | forward_statement |  |  |
| R148 | p10 L283 | forward_statement |  |  |
| R149 | p10 L284 | forward_statement |  |  |
| R150 | p10 L286 | forward_statement |  |  |
| R151 | p10 L287 | forward_statement |  |  |
| R152 | p10 L288 | forward_statement |  |  |
| R153 | p10 L289 | forward_statement |  |  |
| R154 | p10 L291 | forward_statement |  |  |
| R155 | p10 L292 | forward_statement |  |  |
| R156 | p10 L293 | forward_statement |  |  |
| R157 | p10 L294 | forward_statement |  |  |
| R158 | p10 L296 | forward_statement |  |  |
| R159 | p10 L297 | forward_statement |  |  |
| R160 | p11 L305 | forward_statement |  |  |
| R161 | p11 L308 | forward_statement |  |  |
| R162 | p11 L309 | forward_statement |  |  |
| R163 | p11 L313 | forward_statement |  | links R129,R137 |
| R164 | p11 L314 | forward_statement |  | links R136,R173 |
| R165 | p11 L317 | forward_statement |  |  |
| R166 | p11 L318 | forward_statement |  |  |
| R167 | p12 L324 | forward_statement |  |  |
| R168 | p12 L326 | forward_statement |  |  |
| R169 | p12 L328 | forward_statement |  |  |
| R170 | p12 L330 | forward_statement |  |  |
| R171 | p12 L332 | forward_statement |  |  |
| R172 | p12 L334 | forward_statement |  |  |
| R173 | p12 L337 | forward_statement |  | links R136,R164 |
| R174 | p12 L339 | forward_statement |  |  |
| R175 | p8 L242 | forward_statement |  |  |
| R176 | p1 L18 | date_period |  | RESTATED R180 |
| R177 | p1 L32 | date_period |  |  |
| R178 | p1 L43 | date_period |  | signature date same as R176 |
| R179 | p2 L50 | date_period |  |  |
| R180 | p2 L52 | date_period |  | RESTATED R176 |
| R181 | p3 L56 | date_period |  |  |
| R182 | p3 L58 | date_period |  |  |
| R183 | p3 L60 | date_period |  |  |
| R184 | p4 L125 | date_period |  |  |
| R185 | p5 L162 | date_period |  |  |
| R186 | p5 L173 | date_period |  |  |
| R187 | p9 L252 | date_period |  | RESTATED R091 |
| R188 | p9 L271 | date_period |  |  |
| R189 | p8 L233 | date_period |  |  |
| R190 | p2 L54 | date_period |  | copyright year |
| R191 | p3 L77 | footnote_qualifier |  |  |
| R192 | p3 L86 | footnote_qualifier |  | pairs R191 |
| R193 | p4 L119 | footnote_qualifier |  |  |
| R194 | p4 L120 | footnote_qualifier |  |  |
| R195 | p4 L131 | footnote_qualifier |  | pairs R194 |
| R196 | p4 L132 | footnote_qualifier |  | pairs R193 |
| R197 | p4 L135 | footnote_qualifier |  |  |
| R198 | p4 L102 | footnote_qualifier |  |  |
| R199 | p5 L178 | footnote_qualifier |  |  |
| R200 | p5 L180 | footnote_qualifier |  |  |
| R201 | p5 L163 | footnote_qualifier |  | pairs R199 |
| R202 | p5 L168 | footnote_qualifier |  | pairs R200 |
| R203 | p5 L165 | footnote_qualifier |  |  |
| R204 | p5 L172 | footnote_qualifier |  |  |
| R205 | p5 L177 | footnote_qualifier |  |  |
| R206 | p9 L276 | footnote_qualifier |  | chart p9 |
| R207 | p9 L278 | footnote_qualifier |  | chart p9 |
| R208 | p9 L247 | footnote_qualifier | CHART_DATA_NOT_EXTRACTED | chart p9 |
| R209 | p3 L85 | footnote_qualifier | FOOTNOTE_UNRESOLVED |  |
| R210 | p2 L54 | footnote_qualifier | DROPPED_SLIDE (safe-harbour absent vs Q1) |  |

## MISSING_FROM_STRUCTURED
None found in the structured-only sweep.

```yaml
stage: A2-enumerator
company: "TEJASNET"
quarter: "q2fy27"
doctype: "presentation"
model: claude-sonnet-5-5
status: complete
ledger_path: "runs/tejasnet-q2fy27/work/ledger_presentation_tejasnet_q2fy27.md"
counts:
  notes: 0
  line_items: 0
  zero_standing: 3
  agenda_items: 0
  auditor_paras: 0
  entities: 29
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 13
  slide_numbers: 98
flags_raised: [ZERO_STANDING, DROPPED_SLIDE, FOOTNOTE_UNRESOLVED, CHART_DATA_NOT_EXTRACTED, RESTATED]
ids_in_structured: 210
ids_referenced: 210
orphan_ids: []
missing_from_structured: []
gate_a2: pass
mismatch_note: ""
analyst_note: "Q1 baseline was a press release, so DROPPED_SLIDE is basis-limited: the safe-harbour disclaimer, About Tejas profile and MD/CFO quotes in Q1 are absent from the Q2 deck (R210). Order book 2,315 Cr (R010) has no inclusion basis (FOOTNOTE_UNRESOLVED R209). Page 9 chart data is image-only, so Omdia series values are unavailable downstream. Three Other Operating Revenue cells are nil (R024,R026,R028) after 5 Cr in the Q2/H1 FY26 comparators. Net debt (R074) has no stated definition. Q1 comparators (402, 271, 202, 1,529, 4,277, 589) match the prior ledger."
```
