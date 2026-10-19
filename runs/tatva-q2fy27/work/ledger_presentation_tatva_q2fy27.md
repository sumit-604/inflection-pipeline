# A2 LEDGER: TATVA Q2 FY27 Investor Presentation (Updated, 42 pp)
source: runs/tatva-q2fy27/extracted/tatva-presentation-q2fy27-structured.md (A1; no source access)

=== A2 COUNT TEST ===
category: slides              grep_count: 42   sweep_count: 42   match: yes   (fulltext [page N] markers 42; pdfinfo 42)
category: slide_numbers       grep_count: 591  sweep_count: 591  match: yes   (567 active + 24 superseded, all listed)
category: entities            grep_count: 51   sweep_count: 51   match: yes
category: forward             grep_count: 17   sweep_count: 17   match: yes
category: dates               grep_count: 46   sweep_count: 46   match: yes
category: footnotes_qualifiers grep_count: 33  sweep_count: 33   match: yes
category: zero_standing       grep_count: 6    sweep_count: 6    match: yes
category: superseded_ids      grep_count: 24   sweep_count: 24   match: yes
category: version_diff_units  grep_count: 5    sweep_count: 5    match: yes   (A1 header lists 5 diff items)
gate_a2: pass
=== END COUNT TEST ===
ids_in_structured: 738 | ids_referenced_in_ledger: 738 | orphan_ids: [] | match: yes
(grep side = A1 header type totals; sweep side = independent tally of the row type column.)

## 1. VERSION DIFF UNITS (Updated 42pp vs Original 41pp)
V1 | VERSION_DIFF p1: ref no 00056->00057, subject now Updated, body text replaced, timestamp 18:05:26->20:54:24 | rows: R002, R006, R009, R010, R012
V2 | VERSION_DIFF p2: new annexure page, absent in Original | rows: R013, R018
V3 | VERSION_DIFF RoE H1FY27 2.6% -> 6.3% (R015 earlier, R014 updated, R207 live on p14) | rows: R014, R015, R207
V4 | VERSION_DIFF Debt/EBITDA H1FY27 4.30 -> 1.16 (R017 earlier, R016 updated, R217 live on p14) | rows: R016, R017, R217
V5 | VERSION_DIFF p14 notes: (2) Debt to EBITDA is annualized added (R019 annexure, R171 live) | rows: R019, R171
Note: footer page numbers run 2 below PDF page numbers (PDF p13 footer reads 11), so the annexure 'page no. 12' is PDF p14 (Consolidated Financial Highlights). Consistent with V3 and V4.
Prior-quarter deck not supplied: no DROPPED_SLIDE assessment possible, none raised.

## 2. SUPERSEDED ID ACCOUNTING (24 IDs, kept in section 4 with flag SUPERSEDED)
R165-R169 (p13 Q2FY27 split, attribution unresolved) -> R714-R718 (image, attributed)
R622-R627 (p29 R&D spend, period unresolved) -> R719-R724
R642-R650 (p36 country share, attribution unresolved) -> R725-R733
R692-R695 (p40 holding, attribution unresolved) -> R735-R738 (R734 PROMOTER 72.02% has no superseded predecessor row)
Downstream: read successors, treat superseded as non-evidence. p26 revenue-by-category rows keep CHART_ORDER_UNRESOLVED (not rendered).

## 3. SLIDES (42)
S01 | Cover letter (Updated filing) | text | rows=12 | -
S02 | Annexure: updated vs earlier p12 | table | rows=7 | -
S03 | Title | title | rows=3 | -
S04 | Contents | text | rows=1 | -
S05 | CMD message 1 | text | rows=6 | -
S06 | CMD message 2 | text | rows=12 | -
S07 | CMD message 3 | text | rows=9 | -
S08 | CMD message 4 | text | rows=6 | -
S09 | CMD message 5 | text | rows=4 | -
S10 | Section divider Consolidated Financial | divider | rows=0 | NO_A1_ROWS (divider/photo, no extractable numeric content)
S11 | Q2FY27 result highlights | chart | rows=41 | -
S12 | Q2FY27 consolidated numbers | table | rows=58 | -
S13 | Operational highlights revenue split | chart | rows=16 | -
S14 | Consolidated financial highlights | chart+table | rows=48 | -
S15 | Consolidated P&L | table | rows=129 | -
S16 | Consolidated balance sheet | table | rows=158 | -
S17 | Section divider TATVA CHINTAN | divider | rows=0 | NO_A1_ROWS (divider/photo, no extractable numeric content)
S18 | At a glance | text | rows=17 | -
S19 | Section divider Product Categories | divider | rows=0 | NO_A1_ROWS (divider/photo, no extractable numeric content)
S20 | PTC | text | rows=7 | -
S21 | SDA | text | rows=7 | -
S22 | Electrolysis | text | rows=4 | -
S23 | ESS | text | rows=7 | -
S24 | PASC | text | rows=8 | -
S25 | Continuous flow chemistry | text | rows=1 | -
S26 | Revenue by product category | chart | rows=25 | -
S27 | Section divider Leading Sustainable | divider | rows=0 | NO_A1_ROWS (divider/photo, no extractable numeric content)
S28 | Manufacturing facilities | text | rows=36 | -
S29 | R&D centre | chart+text | rows=19 | -
S30 | Green chemistry | text | rows=2 | -
S31 | Section divider international presence | divider | rows=0 | NO_A1_ROWS (divider/photo, no extractable numeric content)
S32 | Clientele and global presence | text | rows=5 | -
S33 | Section divider Why TATVA CHINTAN | divider | rows=0 | NO_A1_ROWS (divider/photo, no extractable numeric content)
S34 | Investment rationale | text | rows=3 | -
S35 | Section divider Industry Outlook | divider | rows=0 | NO_A1_ROWS (divider/photo, no extractable numeric content)
S36 | Industry outlook global chemical share | chart+text | rows=26 | -
S37 | Section divider Our Business | divider | rows=0 | NO_A1_ROWS (divider/photo, no extractable numeric content)
S38 | Milestones | text(timeline) | rows=25 | -
S39 | Leadership and management | photo+text | rows=7 | -
S40 | Shareholder information | chart+table | rows=23 | -
S41 | Safe harbor | text | rows=2 | -
S42 | Closing slide | closing | rows=4 | -

## 4. ROW LEDGER (ROW_ID | category | page/line | A2 flags | cross-ref / materiality)
R001 | date | p1 L23 | - | -
R002 | slide_number | p1 L23 | VERSION_DIFF | VERSION_DIFF p1: ref no 00056->00057, subject now Updated, body text replaced, timestamp 18:05:26->20:54:24
R003 | entity | p1 L28 | - | -
R004 | slide_number | p1 L32 | - | -
R005 | entity | p1 L27 | - | -
R006 | entity | p1 L34 | VERSION_DIFF | VERSION_DIFF p1: ref no 00056->00057, subject now Updated, body text replaced, timestamp 18:05:26->20:54:24
R007 | date | p1 L38 | - | -
R008 | date | p1 L39 | - | -
R009 | footnote_qualifier | p1 L41 | VERSION_DIFF | VERSION_DIFF p1: ref no 00056->00057, subject now Updated, body text replaced, timestamp 18:05:26->20:54:24
R010 | footnote_qualifier | p1 L45 | VERSION_DIFF | VERSION_DIFF p1: ref no 00056->00057, subject now Updated, body text replaced, timestamp 18:05:26->20:54:24
R011 | entity | p1 L68 | - | -
R012 | date | p1 L65 | VERSION_DIFF | VERSION_DIFF p1: ref no 00056->00057, subject now Updated, body text replaced, timestamp 18:05:26->20:54:24
R013 | footnote_qualifier | p2 L76 | VERSION_DIFF | VERSION_DIFF p2: new annexure page, absent in Original
R014 | slide_number | p2 L78 | VERSION_DIFF | VERSION_DIFF RoE H1FY27 2.6% -> 6.3%
R015 | slide_number | p2 L78 | VERSION_DIFF | VERSION_DIFF RoE H1FY27 2.6% -> 6.3%
R016 | slide_number | p2 L79 | VERSION_DIFF | VERSION_DIFF Debt/EBITDA H1FY27 4.30 -> 1.16
R017 | slide_number | p2 L79 | VERSION_DIFF | VERSION_DIFF Debt/EBITDA H1FY27 4.30 -> 1.16
R018 | date | p2 L77 | VERSION_DIFF | VERSION_DIFF p2: new annexure page, absent in Original
R019 | footnote_qualifier | p2 L81 | VERSION_DIFF | VERSION_DIFF p14 notes:
R020 | entity | p3 L85 | - | -
R021 | date | p3 L87 | - | -
R022 | date | p3 L88 | - | -
R023 | date | p5 L114 | - | -
R024 | slide_number | p5 L114 | - | -
R025 | entity | p5 L121 | - | -
R026 | entity | p5 L122 | - | -
R027 | entity | p5 L123 | - | -
R028 | forward_statement | p5 L123 | - | -
R029 | slide_number | p6 L134 | - | -
R030 | slide_number | p6 L134 | - | -
R031 | slide_number | p6 L138 | - | -
R032 | slide_number | p6 L139 | - | -
R033 | entity | p6 L136 | - | -
R034 | date | p6 L141 | - | -
R035 | forward_statement | p6 L141 | - | -
R036 | forward_statement | p6 L141 | - | -
R037 | forward_statement | p6 L142 | - | -
R038 | forward_statement | p6 L144 | - | -
R039 | forward_statement | p6 L153 | - | -
R040 | entity | p6 L150 | - | -
R041 | entity | p7 L160 | - | -
R042 | entity | p7 L160 | - | -
R043 | forward_statement | p7 L164 | - | -
R044 | entity | p7 L167 | - | -
R045 | forward_statement | p7 L168 | - | -
R046 | entity | p7 L173 | - | -
R047 | entity | p7 L173 | - | -
R048 | forward_statement | p7 L176 | - | -
R049 | forward_statement | p7 L178 | - | -
R050 | entity | p8 L185 | - | -
R051 | slide_number | p8 L185 | - | -
R052 | forward_statement | p8 L188 | - | -
R053 | entity | p8 L194 | - | -
R054 | forward_statement | p8 L194 | - | -
R055 | forward_statement | p8 L196 | - | -
R056 | forward_statement | p9 L208 | - | -
R057 | forward_statement | p9 L211 | - | -
R058 | slide_number | p9 L214 | - | -
R059 | entity | p9 L219 | - | -
R060 | footnote_qualifier | p11 L318 | - | -
R061 | footnote_qualifier | p11 L235 | - | -
R062 | footnote_qualifier | p11 L233 | - | -
R063 | footnote_qualifier | p11 L279 | LAYOUT_SCRAMBLED | -
R064 | slide_number | p11 L302 | LAYOUT_SCRAMBLED | -
R065 | slide_number | p11 L302 | LAYOUT_SCRAMBLED | -
R066 | slide_number | p11 L302 | LAYOUT_SCRAMBLED | -
R067 | slide_number | p11 L302 | LAYOUT_SCRAMBLED | -
R068 | slide_number | p11 L302 | LAYOUT_SCRAMBLED | -
R069 | slide_number | p11 L255 | - | -
R070 | slide_number | p11 L303 | - | -
R071 | slide_number | p11 L302 | LAYOUT_SCRAMBLED | -
R072 | slide_number | p11 L302 | LAYOUT_SCRAMBLED | -
R073 | slide_number | p11 L302 | LAYOUT_SCRAMBLED | -
R074 | slide_number | p11 L302 | LAYOUT_SCRAMBLED | -
R075 | slide_number | p11 L302 | LAYOUT_SCRAMBLED | -
R076 | slide_number | p11 L237 | LAYOUT_SCRAMBLED | -
R077 | slide_number | p11 L237 | LAYOUT_SCRAMBLED | -
R078 | slide_number | p11 L237 | LAYOUT_SCRAMBLED | -
R079 | slide_number | p11 L237 | LAYOUT_SCRAMBLED | -
R080 | slide_number | p11 L237 | LAYOUT_SCRAMBLED | -
R081 | slide_number | p11 L249 | - | -
R082 | slide_number | p11 L305 | - | -
R083 | slide_number | p11 L302 | LAYOUT_SCRAMBLED | -
R084 | slide_number | p11 L302 | LAYOUT_SCRAMBLED | -
R085 | slide_number | p11 L302 | LAYOUT_SCRAMBLED | -
R086 | slide_number | p11 L302 | LAYOUT_SCRAMBLED | -
R087 | slide_number | p11 L302 | LAYOUT_SCRAMBLED | -
R088 | slide_number | p11 L237 | LAYOUT_SCRAMBLED | -
R089 | slide_number | p11 L237 | LAYOUT_SCRAMBLED | -
R090 | slide_number | p11 L237 | LAYOUT_SCRAMBLED | -
R091 | slide_number | p11 L291 | LAYOUT_SCRAMBLED | -
R092 | slide_number | p11 L291 | LAYOUT_SCRAMBLED | -
R093 | slide_number | p11 L253 | - | -
R094 | slide_number | p11 L297 | - | -
R095 | slide_number | p11 L242 | LAYOUT_SCRAMBLED | -
R096 | slide_number | p11 L242 | LAYOUT_SCRAMBLED | -
R097 | slide_number | p11 L242 | LAYOUT_SCRAMBLED | -
R098 | slide_number | p11 L291 | LAYOUT_SCRAMBLED | -
R099 | slide_number | p11 L291 | LAYOUT_SCRAMBLED | -
R100 | date | p11 L233 | - | -
R101 | footnote_qualifier | p12 L324 | - | -
R102 | slide_number | p12 L326 | LAYOUT_SCRAMBLED | -
R103 | slide_number | p12 L326 | LAYOUT_SCRAMBLED | -
R104 | slide_number | p12 L326 | LAYOUT_SCRAMBLED | -
R105 | slide_number | p12 L326 | LAYOUT_SCRAMBLED | -
R106 | slide_number | p12 L326 | LAYOUT_SCRAMBLED | -
R107 | slide_number | p12 L326 | LAYOUT_SCRAMBLED | -
R108 | slide_number | p12 L326 | LAYOUT_SCRAMBLED | -
R109 | slide_number | p12 L326 | LAYOUT_SCRAMBLED | -
R110 | slide_number | p12 L327 | LAYOUT_SCRAMBLED | -
R111 | slide_number | p12 L327 | LAYOUT_SCRAMBLED | -
R112 | slide_number | p12 L327 | LAYOUT_SCRAMBLED | -
R113 | slide_number | p12 L327 | LAYOUT_SCRAMBLED | -
R114 | slide_number | p12 L327 | LAYOUT_SCRAMBLED | -
R115 | slide_number | p12 L327 | LAYOUT_SCRAMBLED | -
R116 | slide_number | p12 L327 | LAYOUT_SCRAMBLED | -
R117 | slide_number | p12 L327 | LAYOUT_SCRAMBLED | -
R118 | slide_number | p12 L328 | LAYOUT_SCRAMBLED | -
R119 | slide_number | p12 L328 | LAYOUT_SCRAMBLED | -
R120 | slide_number | p12 L328 | LAYOUT_SCRAMBLED | -
R121 | slide_number | p12 L328 | LAYOUT_SCRAMBLED | -
R122 | slide_number | p12 L328 | LAYOUT_SCRAMBLED | -
R123 | slide_number | p12 L328 | LAYOUT_SCRAMBLED | -
R124 | slide_number | p12 L328 | LAYOUT_SCRAMBLED | -
R125 | slide_number | p12 L328 | LAYOUT_SCRAMBLED | -
R126 | slide_number | p12 L329 | LAYOUT_SCRAMBLED | -
R127 | slide_number | p12 L329 | LAYOUT_SCRAMBLED | -
R128 | slide_number | p12 L329 | LAYOUT_SCRAMBLED | -
R129 | slide_number | p12 L329 | LAYOUT_SCRAMBLED | -
R130 | slide_number | p12 L329 | LAYOUT_SCRAMBLED | -
R131 | slide_number | p12 L329 | LAYOUT_SCRAMBLED | -
R132 | slide_number | p12 L329 | LAYOUT_SCRAMBLED | -
R133 | slide_number | p12 L329 | LAYOUT_SCRAMBLED | -
R134 | slide_number | p12 L330 | LAYOUT_SCRAMBLED | -
R135 | slide_number | p12 L330 | LAYOUT_SCRAMBLED | -
R136 | slide_number | p12 L330 | LAYOUT_SCRAMBLED | -
R137 | slide_number | p12 L330 | LAYOUT_SCRAMBLED | -
R138 | slide_number | p12 L330 | LAYOUT_SCRAMBLED | -
R139 | slide_number | p12 L330 | LAYOUT_SCRAMBLED | -
R140 | slide_number | p12 L330 | LAYOUT_SCRAMBLED | -
R141 | slide_number | p12 L330 | LAYOUT_SCRAMBLED | -
R142 | slide_number | p12 L331 | LAYOUT_SCRAMBLED | -
R143 | slide_number | p12 L331 | LAYOUT_SCRAMBLED | -
R144 | slide_number | p12 L331 | LAYOUT_SCRAMBLED | -
R145 | slide_number | p12 L331 | LAYOUT_SCRAMBLED | -
R146 | slide_number | p12 L331 | LAYOUT_SCRAMBLED | -
R147 | slide_number | p12 L331 | LAYOUT_SCRAMBLED | -
R148 | slide_number | p12 L331 | LAYOUT_SCRAMBLED | -
R149 | slide_number | p12 L331 | LAYOUT_SCRAMBLED | -
R150 | slide_number | p12 L332 | LAYOUT_SCRAMBLED | -
R151 | slide_number | p12 L332 | LAYOUT_SCRAMBLED | -
R152 | slide_number | p12 L332 | LAYOUT_SCRAMBLED | -
R153 | slide_number | p12 L332 | LAYOUT_SCRAMBLED | -
R154 | slide_number | p12 L332 | LAYOUT_SCRAMBLED | -
R155 | slide_number | p12 L332 | LAYOUT_SCRAMBLED | -
R156 | slide_number | p12 L332 | LAYOUT_SCRAMBLED | -
R157 | slide_number | p12 L332 | LAYOUT_SCRAMBLED | -
R158 | footnote_qualifier | p12 L328 | - | -
R159 | date | p13 L342 | - | -
R160 | slide_number | p13 L351 | LAYOUT_SCRAMBLED | -
R161 | slide_number | p13 L347 | LAYOUT_SCRAMBLED | -
R162 | slide_number | p13 L352 | LAYOUT_SCRAMBLED | -
R163 | slide_number | p13 L354 | LAYOUT_SCRAMBLED | -
R164 | slide_number | p13 L346 | LAYOUT_SCRAMBLED | -
R165 | superseded_number | p13 L353 | SUPERSEDED,CHART_ORDER_UNRESOLVED | superseded by R714-R718 (use successor)
R166 | superseded_number | p13 L351 | SUPERSEDED,CHART_ORDER_UNRESOLVED | superseded by R714-R718 (use successor)
R167 | superseded_number | p13 L354 | SUPERSEDED,CHART_ORDER_UNRESOLVED | superseded by R714-R718 (use successor)
R168 | superseded_number | p13 L362 | SUPERSEDED,CHART_ORDER_UNRESOLVED | superseded by R714-R718 (use successor)
R169 | superseded_number | p13 L354 | SUPERSEDED,CHART_ORDER_UNRESOLVED | superseded by R714-R718 (use successor)
R170 | footnote_qualifier | p14 L368 | - | -
R171 | footnote_qualifier | p14 L415 | VERSION_DIFF | VERSION_DIFF p14 notes:
R172 | footnote_qualifier | p14 L370 | - | -
R173 | slide_number | p14 L373 | LAYOUT_SCRAMBLED | -
R174 | slide_number | p14 L373 | LAYOUT_SCRAMBLED | -
R175 | slide_number | p14 L373 | LAYOUT_SCRAMBLED | -
R176 | slide_number | p14 L373 | LAYOUT_SCRAMBLED | -
R177 | slide_number | p14 L373 | LAYOUT_SCRAMBLED | -
R178 | slide_number | p14 L370 | LAYOUT_SCRAMBLED | -
R179 | slide_number | p14 L370 | LAYOUT_SCRAMBLED | -
R180 | slide_number | p14 L370 | LAYOUT_SCRAMBLED | -
R181 | slide_number | p14 L370 | LAYOUT_SCRAMBLED | -
R182 | slide_number | p14 L370 | LAYOUT_SCRAMBLED | -
R183 | slide_number | p14 L379 | LAYOUT_SCRAMBLED | -
R184 | slide_number | p14 L379 | LAYOUT_SCRAMBLED | -
R185 | slide_number | p14 L379 | LAYOUT_SCRAMBLED | -
R186 | slide_number | p14 L379 | LAYOUT_SCRAMBLED | -
R187 | slide_number | p14 L379 | LAYOUT_SCRAMBLED | -
R188 | slide_number | p14 L373 | LAYOUT_SCRAMBLED | -
R189 | slide_number | p14 L373 | LAYOUT_SCRAMBLED | -
R190 | slide_number | p14 L373 | LAYOUT_SCRAMBLED | -
R191 | slide_number | p14 L373 | LAYOUT_SCRAMBLED | -
R192 | slide_number | p14 L373 | LAYOUT_SCRAMBLED | -
R193 | slide_number | p14 L379 | LAYOUT_SCRAMBLED | -
R194 | slide_number | p14 L379 | LAYOUT_SCRAMBLED | -
R195 | slide_number | p14 L379 | LAYOUT_SCRAMBLED | -
R196 | slide_number | p14 L379 | LAYOUT_SCRAMBLED | -
R197 | slide_number | p14 L379 | LAYOUT_SCRAMBLED | -
R198 | slide_number | p14 L372 | LAYOUT_SCRAMBLED | -
R199 | slide_number | p14 L372 | LAYOUT_SCRAMBLED | -
R200 | slide_number | p14 L372 | LAYOUT_SCRAMBLED | -
R201 | slide_number | p14 L372 | LAYOUT_SCRAMBLED | -
R202 | slide_number | p14 L372 | LAYOUT_SCRAMBLED | -
R203 | slide_number | p14 L397 | LAYOUT_SCRAMBLED | -
R204 | slide_number | p14 L397 | LAYOUT_SCRAMBLED | -
R205 | slide_number | p14 L397 | LAYOUT_SCRAMBLED | -
R206 | slide_number | p14 L397 | LAYOUT_SCRAMBLED | -
R207 | slide_number | p14 L397 | LAYOUT_SCRAMBLED,VERSION_DIFF | VERSION_DIFF RoE H1FY27 2.6% -> 6.3%
R208 | slide_number | p14 L402 | LAYOUT_SCRAMBLED | -
R209 | slide_number | p14 L402 | LAYOUT_SCRAMBLED | -
R210 | slide_number | p14 L402 | LAYOUT_SCRAMBLED | -
R211 | slide_number | p14 L402 | LAYOUT_SCRAMBLED | -
R212 | slide_number | p14 L402 | LAYOUT_SCRAMBLED | -
R213 | slide_number | p14 L407 | LAYOUT_SCRAMBLED | -
R214 | slide_number | p14 L407 | LAYOUT_SCRAMBLED | -
R215 | slide_number | p14 L407 | LAYOUT_SCRAMBLED | -
R216 | slide_number | p14 L407 | LAYOUT_SCRAMBLED | -
R217 | slide_number | p14 L407 | LAYOUT_SCRAMBLED,VERSION_DIFF | VERSION_DIFF Debt/EBITDA H1FY27 4.30 -> 1.16
R218 | slide_number | p15 L427 | LAYOUT_SCRAMBLED | -
R219 | slide_number | p15 L427 | LAYOUT_SCRAMBLED | -
R220 | slide_number | p15 L427 | LAYOUT_SCRAMBLED | -
R221 | slide_number | p15 L427 | LAYOUT_SCRAMBLED | -
R222 | slide_number | p15 L427 | LAYOUT_SCRAMBLED | -
R223 | slide_number | p15 L427 | LAYOUT_SCRAMBLED | -
R224 | slide_number | p15 L427 | LAYOUT_SCRAMBLED | -
R225 | slide_number | p15 L429 | LAYOUT_SCRAMBLED | -
R226 | slide_number | p15 L429 | LAYOUT_SCRAMBLED | -
R227 | slide_number | p15 L429 | LAYOUT_SCRAMBLED | -
R228 | slide_number | p15 L429 | LAYOUT_SCRAMBLED | -
R229 | slide_number | p15 L429 | LAYOUT_SCRAMBLED | -
R230 | slide_number | p15 L429 | LAYOUT_SCRAMBLED | -
R231 | slide_number | p15 L429 | LAYOUT_SCRAMBLED | -
R232 | slide_number | p15 L431 | LAYOUT_SCRAMBLED | -
R233 | slide_number | p15 L431 | LAYOUT_SCRAMBLED | -
R234 | slide_number | p15 L431 | LAYOUT_SCRAMBLED | -
R235 | slide_number | p15 L431 | LAYOUT_SCRAMBLED | -
R236 | slide_number | p15 L431 | LAYOUT_SCRAMBLED | -
R237 | slide_number | p15 L431 | LAYOUT_SCRAMBLED | -
R238 | slide_number | p15 L431 | LAYOUT_SCRAMBLED | -
R239 | slide_number | p15 L435 | LAYOUT_SCRAMBLED | -
R240 | slide_number | p15 L435 | LAYOUT_SCRAMBLED | -
R241 | slide_number | p15 L435 | LAYOUT_SCRAMBLED | -
R242 | slide_number | p15 L435 | LAYOUT_SCRAMBLED | -
R243 | slide_number | p15 L435 | LAYOUT_SCRAMBLED | -
R244 | slide_number | p15 L435 | LAYOUT_SCRAMBLED | -
R245 | slide_number | p15 L435 | LAYOUT_SCRAMBLED | -
R246 | slide_number | p15 L437 | LAYOUT_SCRAMBLED | -
R247 | slide_number | p15 L437 | LAYOUT_SCRAMBLED | -
R248 | slide_number | p15 L437 | LAYOUT_SCRAMBLED | -
R249 | slide_number | p15 L437 | LAYOUT_SCRAMBLED | -
R250 | slide_number | p15 L437 | LAYOUT_SCRAMBLED | -
R251 | slide_number | p15 L437 | LAYOUT_SCRAMBLED | -
R252 | slide_number | p15 L437 | LAYOUT_SCRAMBLED | -
R253 | slide_number | p15 L439 | LAYOUT_SCRAMBLED | -
R254 | slide_number | p15 L439 | LAYOUT_SCRAMBLED | -
R255 | slide_number | p15 L439 | LAYOUT_SCRAMBLED | -
R256 | slide_number | p15 L439 | LAYOUT_SCRAMBLED | -
R257 | slide_number | p15 L439 | LAYOUT_SCRAMBLED | -
R258 | slide_number | p15 L439 | LAYOUT_SCRAMBLED | -
R259 | slide_number | p15 L439 | LAYOUT_SCRAMBLED | -
R260 | slide_number | p15 L441 | LAYOUT_SCRAMBLED | -
R261 | slide_number | p15 L441 | LAYOUT_SCRAMBLED | -
R262 | slide_number | p15 L441 | LAYOUT_SCRAMBLED | -
R263 | slide_number | p15 L441 | LAYOUT_SCRAMBLED | -
R264 | slide_number | p15 L441 | LAYOUT_SCRAMBLED | -
R265 | slide_number | p15 L441 | LAYOUT_SCRAMBLED | -
R266 | slide_number | p15 L441 | LAYOUT_SCRAMBLED | -
R267 | slide_number | p15 L443 | LAYOUT_SCRAMBLED | -
R268 | slide_number | p15 L443 | LAYOUT_SCRAMBLED | -
R269 | slide_number | p15 L443 | LAYOUT_SCRAMBLED | -
R270 | slide_number | p15 L443 | LAYOUT_SCRAMBLED | -
R271 | slide_number | p15 L443 | LAYOUT_SCRAMBLED | -
R272 | slide_number | p15 L443 | LAYOUT_SCRAMBLED | -
R273 | slide_number | p15 L443 | LAYOUT_SCRAMBLED | -
R274 | slide_number | p15 L445 | LAYOUT_SCRAMBLED | -
R275 | slide_number | p15 L445 | LAYOUT_SCRAMBLED | -
R276 | slide_number | p15 L445 | LAYOUT_SCRAMBLED | -
R277 | slide_number | p15 L445 | LAYOUT_SCRAMBLED | -
R278 | slide_number | p15 L445 | LAYOUT_SCRAMBLED | -
R279 | slide_number | p15 L445 | LAYOUT_SCRAMBLED | -
R280 | slide_number | p15 L445 | LAYOUT_SCRAMBLED | -
R281 | slide_number | p15 L447 | LAYOUT_SCRAMBLED | -
R282 | slide_number | p15 L447 | LAYOUT_SCRAMBLED | -
R283 | slide_number | p15 L447 | LAYOUT_SCRAMBLED | -
R284 | slide_number | p15 L447 | LAYOUT_SCRAMBLED | -
R285 | slide_number | p15 L447 | LAYOUT_SCRAMBLED | -
R286 | slide_number | p15 L447 | LAYOUT_SCRAMBLED | -
R287 | slide_number | p15 L447 | LAYOUT_SCRAMBLED | -
R288 | slide_number | p15 L449 | ZERO_STANDING,LAYOUT_SCRAMBLED | -
R289 | slide_number | p15 L449 | ZERO_STANDING,LAYOUT_SCRAMBLED | -
R290 | slide_number | p15 L449 | LAYOUT_SCRAMBLED | -
R291 | slide_number | p15 L449 | ZERO_STANDING,LAYOUT_SCRAMBLED | -
R292 | slide_number | p15 L449 | ZERO_STANDING,LAYOUT_SCRAMBLED | -
R293 | slide_number | p15 L449 | ZERO_STANDING,LAYOUT_SCRAMBLED | -
R294 | slide_number | p15 L449 | LAYOUT_SCRAMBLED | -
R295 | slide_number | p15 L451 | LAYOUT_SCRAMBLED | -
R296 | slide_number | p15 L451 | LAYOUT_SCRAMBLED | -
R297 | slide_number | p15 L451 | LAYOUT_SCRAMBLED | -
R298 | slide_number | p15 L451 | LAYOUT_SCRAMBLED | -
R299 | slide_number | p15 L451 | LAYOUT_SCRAMBLED | -
R300 | slide_number | p15 L451 | LAYOUT_SCRAMBLED | -
R301 | slide_number | p15 L451 | LAYOUT_SCRAMBLED | -
R302 | slide_number | p15 L453 | LAYOUT_SCRAMBLED | -
R303 | slide_number | p15 L453 | LAYOUT_SCRAMBLED | -
R304 | slide_number | p15 L453 | LAYOUT_SCRAMBLED | -
R305 | slide_number | p15 L453 | LAYOUT_SCRAMBLED | -
R306 | slide_number | p15 L453 | LAYOUT_SCRAMBLED | -
R307 | slide_number | p15 L453 | LAYOUT_SCRAMBLED | -
R308 | slide_number | p15 L453 | LAYOUT_SCRAMBLED | -
R309 | slide_number | p15 L455 | LAYOUT_SCRAMBLED | -
R310 | slide_number | p15 L455 | LAYOUT_SCRAMBLED | -
R311 | slide_number | p15 L455 | LAYOUT_SCRAMBLED | -
R312 | slide_number | p15 L455 | LAYOUT_SCRAMBLED | -
R313 | slide_number | p15 L455 | LAYOUT_SCRAMBLED | -
R314 | slide_number | p15 L455 | LAYOUT_SCRAMBLED | -
R315 | slide_number | p15 L455 | LAYOUT_SCRAMBLED | -
R316 | slide_number | p15 L457 | LAYOUT_SCRAMBLED | -
R317 | slide_number | p15 L457 | LAYOUT_SCRAMBLED | -
R318 | slide_number | p15 L457 | LAYOUT_SCRAMBLED | -
R319 | slide_number | p15 L457 | LAYOUT_SCRAMBLED | -
R320 | slide_number | p15 L457 | LAYOUT_SCRAMBLED | -
R321 | slide_number | p15 L457 | LAYOUT_SCRAMBLED | -
R322 | slide_number | p15 L457 | LAYOUT_SCRAMBLED | -
R323 | slide_number | p15 L459 | LAYOUT_SCRAMBLED | -
R324 | slide_number | p15 L459 | LAYOUT_SCRAMBLED | -
R325 | slide_number | p15 L459 | LAYOUT_SCRAMBLED | -
R326 | slide_number | p15 L459 | LAYOUT_SCRAMBLED | -
R327 | slide_number | p15 L459 | LAYOUT_SCRAMBLED | -
R328 | slide_number | p15 L459 | LAYOUT_SCRAMBLED | -
R329 | slide_number | p15 L459 | LAYOUT_SCRAMBLED | -
R330 | slide_number | p15 L461 | LAYOUT_SCRAMBLED | -
R331 | slide_number | p15 L461 | LAYOUT_SCRAMBLED | -
R332 | slide_number | p15 L461 | LAYOUT_SCRAMBLED | -
R333 | slide_number | p15 L461 | LAYOUT_SCRAMBLED | -
R334 | slide_number | p15 L461 | LAYOUT_SCRAMBLED | -
R335 | slide_number | p15 L461 | LAYOUT_SCRAMBLED | -
R336 | slide_number | p15 L461 | LAYOUT_SCRAMBLED | -
R337 | slide_number | p15 L463 | LAYOUT_SCRAMBLED | -
R338 | slide_number | p15 L463 | LAYOUT_SCRAMBLED | -
R339 | slide_number | p15 L463 | LAYOUT_SCRAMBLED | -
R340 | slide_number | p15 L463 | LAYOUT_SCRAMBLED | -
R341 | slide_number | p15 L463 | LAYOUT_SCRAMBLED | -
R342 | slide_number | p15 L463 | LAYOUT_SCRAMBLED | -
R343 | slide_number | p15 L463 | LAYOUT_SCRAMBLED | -
R344 | footnote_qualifier | p15 L422 | - | -
R345 | footnote_qualifier | p15 L421 | - | -
R346 | date | p15 L421 | - | -
R347 | slide_number | p16 L475 | LAYOUT_SCRAMBLED | -
R348 | slide_number | p16 L475 | LAYOUT_SCRAMBLED | -
R349 | slide_number | p16 L475 | LAYOUT_SCRAMBLED | -
R350 | slide_number | p16 L475 | LAYOUT_SCRAMBLED | -
R351 | slide_number | p16 L475 | LAYOUT_SCRAMBLED | -
R352 | slide_number | p16 L475 | LAYOUT_SCRAMBLED | -
R353 | slide_number | p16 L475 | LAYOUT_SCRAMBLED | -
R354 | slide_number | p16 L477 | LAYOUT_SCRAMBLED | -
R355 | slide_number | p16 L477 | LAYOUT_SCRAMBLED | -
R356 | slide_number | p16 L477 | LAYOUT_SCRAMBLED | -
R357 | slide_number | p16 L477 | LAYOUT_SCRAMBLED | -
R358 | slide_number | p16 L477 | LAYOUT_SCRAMBLED | -
R359 | slide_number | p16 L477 | LAYOUT_SCRAMBLED | -
R360 | slide_number | p16 L477 | LAYOUT_SCRAMBLED | -
R361 | slide_number | p16 L479 | LAYOUT_SCRAMBLED | -
R362 | slide_number | p16 L479 | LAYOUT_SCRAMBLED | -
R363 | slide_number | p16 L479 | LAYOUT_SCRAMBLED | -
R364 | slide_number | p16 L479 | LAYOUT_SCRAMBLED | -
R365 | slide_number | p16 L479 | LAYOUT_SCRAMBLED | -
R366 | slide_number | p16 L479 | LAYOUT_SCRAMBLED | -
R367 | slide_number | p16 L479 | LAYOUT_SCRAMBLED | -
R368 | slide_number | p16 L481 | LAYOUT_SCRAMBLED | -
R369 | slide_number | p16 L481 | LAYOUT_SCRAMBLED | -
R370 | slide_number | p16 L481 | LAYOUT_SCRAMBLED | -
R371 | slide_number | p16 L481 | LAYOUT_SCRAMBLED | -
R372 | slide_number | p16 L481 | LAYOUT_SCRAMBLED | -
R373 | slide_number | p16 L481 | LAYOUT_SCRAMBLED | -
R374 | slide_number | p16 L481 | LAYOUT_SCRAMBLED | -
R375 | slide_number | p16 L483 | LAYOUT_SCRAMBLED | -
R376 | slide_number | p16 L483 | LAYOUT_SCRAMBLED | -
R377 | slide_number | p16 L483 | LAYOUT_SCRAMBLED | -
R378 | slide_number | p16 L483 | LAYOUT_SCRAMBLED | -
R379 | slide_number | p16 L483 | LAYOUT_SCRAMBLED | -
R380 | slide_number | p16 L483 | LAYOUT_SCRAMBLED | -
R381 | slide_number | p16 L483 | LAYOUT_SCRAMBLED | -
R382 | slide_number | p16 L485 | LAYOUT_SCRAMBLED | -
R383 | slide_number | p16 L485 | LAYOUT_SCRAMBLED | -
R384 | slide_number | p16 L485 | LAYOUT_SCRAMBLED | -
R385 | slide_number | p16 L485 | LAYOUT_SCRAMBLED | -
R386 | slide_number | p16 L485 | LAYOUT_SCRAMBLED | -
R387 | slide_number | p16 L485 | LAYOUT_SCRAMBLED | -
R388 | slide_number | p16 L485 | LAYOUT_SCRAMBLED | -
R389 | slide_number | p16 L487 | LAYOUT_SCRAMBLED | -
R390 | slide_number | p16 L487 | LAYOUT_SCRAMBLED | -
R391 | slide_number | p16 L487 | LAYOUT_SCRAMBLED | -
R392 | slide_number | p16 L487 | LAYOUT_SCRAMBLED | -
R393 | slide_number | p16 L487 | LAYOUT_SCRAMBLED | -
R394 | slide_number | p16 L487 | LAYOUT_SCRAMBLED | -
R395 | slide_number | p16 L487 | LAYOUT_SCRAMBLED | -
R396 | slide_number | p16 L489 | LAYOUT_SCRAMBLED | -
R397 | slide_number | p16 L489 | LAYOUT_SCRAMBLED | -
R398 | slide_number | p16 L489 | LAYOUT_SCRAMBLED | -
R399 | slide_number | p16 L489 | LAYOUT_SCRAMBLED | -
R400 | slide_number | p16 L489 | LAYOUT_SCRAMBLED | -
R401 | slide_number | p16 L489 | LAYOUT_SCRAMBLED | -
R402 | slide_number | p16 L489 | LAYOUT_SCRAMBLED | -
R403 | slide_number | p16 L491 | LAYOUT_SCRAMBLED | -
R404 | slide_number | p16 L491 | LAYOUT_SCRAMBLED | -
R405 | slide_number | p16 L491 | LAYOUT_SCRAMBLED | -
R406 | slide_number | p16 L491 | LAYOUT_SCRAMBLED | -
R407 | slide_number | p16 L491 | LAYOUT_SCRAMBLED | -
R408 | slide_number | p16 L491 | LAYOUT_SCRAMBLED | -
R409 | slide_number | p16 L491 | LAYOUT_SCRAMBLED | -
R410 | slide_number | p16 L493 | LAYOUT_SCRAMBLED | -
R411 | slide_number | p16 L493 | LAYOUT_SCRAMBLED | -
R412 | slide_number | p16 L493 | LAYOUT_SCRAMBLED | -
R413 | slide_number | p16 L493 | LAYOUT_SCRAMBLED | -
R414 | slide_number | p16 L493 | LAYOUT_SCRAMBLED | -
R415 | slide_number | p16 L493 | LAYOUT_SCRAMBLED | -
R416 | slide_number | p16 L493 | LAYOUT_SCRAMBLED | -
R417 | slide_number | p16 L495 | LAYOUT_SCRAMBLED | -
R418 | slide_number | p16 L495 | LAYOUT_SCRAMBLED | -
R419 | slide_number | p16 L495 | LAYOUT_SCRAMBLED | -
R420 | slide_number | p16 L495 | LAYOUT_SCRAMBLED | -
R421 | slide_number | p16 L495 | LAYOUT_SCRAMBLED | -
R422 | slide_number | p16 L495 | LAYOUT_SCRAMBLED | -
R423 | slide_number | p16 L495 | LAYOUT_SCRAMBLED | -
R424 | slide_number | p16 L499 | LAYOUT_SCRAMBLED | -
R425 | slide_number | p16 L499 | LAYOUT_SCRAMBLED | -
R426 | slide_number | p16 L499 | LAYOUT_SCRAMBLED | -
R427 | slide_number | p16 L499 | LAYOUT_SCRAMBLED | -
R428 | slide_number | p16 L499 | LAYOUT_SCRAMBLED | -
R429 | slide_number | p16 L499 | LAYOUT_SCRAMBLED | -
R430 | slide_number | p16 L499 | LAYOUT_SCRAMBLED | -
R431 | slide_number | p16 L501 | LAYOUT_SCRAMBLED | -
R432 | slide_number | p16 L501 | LAYOUT_SCRAMBLED | -
R433 | slide_number | p16 L501 | LAYOUT_SCRAMBLED | -
R434 | slide_number | p16 L501 | LAYOUT_SCRAMBLED | -
R435 | slide_number | p16 L501 | LAYOUT_SCRAMBLED | -
R436 | slide_number | p16 L501 | LAYOUT_SCRAMBLED | -
R437 | slide_number | p16 L501 | LAYOUT_SCRAMBLED | -
R438 | slide_number | p16 L503 | LAYOUT_SCRAMBLED | -
R439 | slide_number | p16 L503 | LAYOUT_SCRAMBLED | -
R440 | slide_number | p16 L503 | LAYOUT_SCRAMBLED | -
R441 | slide_number | p16 L503 | LAYOUT_SCRAMBLED | -
R442 | slide_number | p16 L503 | LAYOUT_SCRAMBLED | -
R443 | slide_number | p16 L503 | LAYOUT_SCRAMBLED | -
R444 | slide_number | p16 L503 | LAYOUT_SCRAMBLED | -
R445 | slide_number | p16 L509 | LAYOUT_SCRAMBLED | -
R446 | slide_number | p16 L509 | LAYOUT_SCRAMBLED | -
R447 | slide_number | p16 L509 | LAYOUT_SCRAMBLED | -
R448 | slide_number | p16 L509 | LAYOUT_SCRAMBLED | -
R449 | slide_number | p16 L509 | ZERO_STANDING,LAYOUT_SCRAMBLED | -
R450 | slide_number | p16 L509 | LAYOUT_SCRAMBLED | -
R451 | slide_number | p16 L509 | LAYOUT_SCRAMBLED | -
R452 | slide_number | p16 L511 | LAYOUT_SCRAMBLED | -
R453 | slide_number | p16 L511 | LAYOUT_SCRAMBLED | -
R454 | slide_number | p16 L511 | LAYOUT_SCRAMBLED | -
R455 | slide_number | p16 L511 | LAYOUT_SCRAMBLED | -
R456 | slide_number | p16 L511 | LAYOUT_SCRAMBLED | -
R457 | slide_number | p16 L511 | LAYOUT_SCRAMBLED | -
R458 | slide_number | p16 L511 | LAYOUT_SCRAMBLED | -
R459 | slide_number | p16 L513 | LAYOUT_SCRAMBLED | -
R460 | slide_number | p16 L513 | LAYOUT_SCRAMBLED | -
R461 | slide_number | p16 L513 | LAYOUT_SCRAMBLED | -
R462 | slide_number | p16 L513 | LAYOUT_SCRAMBLED | -
R463 | slide_number | p16 L513 | LAYOUT_SCRAMBLED | -
R464 | slide_number | p16 L513 | LAYOUT_SCRAMBLED | -
R465 | slide_number | p16 L513 | LAYOUT_SCRAMBLED | -
R466 | slide_number | p16 L517 | LAYOUT_SCRAMBLED | -
R467 | slide_number | p16 L517 | LAYOUT_SCRAMBLED | -
R468 | slide_number | p16 L517 | LAYOUT_SCRAMBLED | -
R469 | slide_number | p16 L517 | LAYOUT_SCRAMBLED | -
R470 | slide_number | p16 L517 | LAYOUT_SCRAMBLED | -
R471 | slide_number | p16 L517 | LAYOUT_SCRAMBLED | -
R472 | slide_number | p16 L517 | LAYOUT_SCRAMBLED | -
R473 | slide_number | p16 L519 | LAYOUT_SCRAMBLED | -
R474 | slide_number | p16 L519 | LAYOUT_SCRAMBLED | -
R475 | slide_number | p16 L519 | LAYOUT_SCRAMBLED | -
R476 | slide_number | p16 L519 | LAYOUT_SCRAMBLED | -
R477 | slide_number | p16 L519 | LAYOUT_SCRAMBLED | -
R478 | slide_number | p16 L519 | LAYOUT_SCRAMBLED | -
R479 | slide_number | p16 L519 | LAYOUT_SCRAMBLED | -
R480 | slide_number | p16 L521 | LAYOUT_SCRAMBLED | -
R481 | slide_number | p16 L521 | LAYOUT_SCRAMBLED | -
R482 | slide_number | p16 L521 | LAYOUT_SCRAMBLED | -
R483 | slide_number | p16 L521 | LAYOUT_SCRAMBLED | -
R484 | slide_number | p16 L521 | LAYOUT_SCRAMBLED | -
R485 | slide_number | p16 L521 | LAYOUT_SCRAMBLED | -
R486 | slide_number | p16 L521 | LAYOUT_SCRAMBLED | -
R487 | slide_number | p16 L523 | LAYOUT_SCRAMBLED | -
R488 | slide_number | p16 L523 | LAYOUT_SCRAMBLED | -
R489 | slide_number | p16 L523 | LAYOUT_SCRAMBLED | -
R490 | slide_number | p16 L523 | LAYOUT_SCRAMBLED | -
R491 | slide_number | p16 L523 | LAYOUT_SCRAMBLED | -
R492 | slide_number | p16 L523 | LAYOUT_SCRAMBLED | -
R493 | slide_number | p16 L523 | LAYOUT_SCRAMBLED | -
R494 | slide_number | p16 L525 | LAYOUT_SCRAMBLED | -
R495 | slide_number | p16 L525 | LAYOUT_SCRAMBLED | -
R496 | slide_number | p16 L525 | LAYOUT_SCRAMBLED | -
R497 | slide_number | p16 L525 | LAYOUT_SCRAMBLED | -
R498 | slide_number | p16 L525 | LAYOUT_SCRAMBLED | -
R499 | slide_number | p16 L525 | LAYOUT_SCRAMBLED | -
R500 | slide_number | p16 L525 | LAYOUT_SCRAMBLED | -
R501 | footnote_qualifier | p16 L470 | - | -
R502 | footnote_qualifier | p16 L469 | - | -
R503 | footnote_qualifier | p16 L503 | - | -
R504 | date | p16 L469 | - | -
R505 | date | p18 L540 | - | -
R506 | entity | p18 L539 | - | -
R507 | entity | p18 L542 | - | -
R508 | slide_number | p18 L543 | - | -
R509 | slide_number | p18 L543 | - | -
R510 | date | p18 L543 | - | -
R511 | entity | p18 L546 | - | -
R512 | date | p18 L553 | - | -
R513 | slide_number | p18 L555 | - | -
R514 | slide_number | p18 L557 | - | -
R515 | entity | p18 L561 | - | -
R516 | entity | p18 L563 | - | -
R517 | slide_number | p18 L553 | - | -
R518 | slide_number | p18 L555 | - | -
R519 | slide_number | p18 L557 | - | -
R520 | slide_number | p18 L561 | - | -
R521 | slide_number | p18 L563 | - | -
R522 | date | p20 L578 | - | -
R523 | slide_number | p20 L582 | - | -
R524 | slide_number | p20 L582 | - | -
R525 | slide_number | p20 L591 | - | -
R526 | slide_number | p20 L591 | - | -
R527 | footnote_qualifier | p20 L597 | - | -
R528 | entity | p20 L597 | - | -
R529 | date | p21 L610 | - | -
R530 | slide_number | p21 L614 | - | -
R531 | slide_number | p21 L614 | - | -
R532 | slide_number | p21 L623 | - | -
R533 | slide_number | p21 L623 | - | -
R534 | footnote_qualifier | p21 L629 | - | -
R535 | entity | p21 L610 | - | -
R536 | date | p22 L645 | - | -
R537 | date | p22 L647 | - | -
R538 | slide_number | p22 L653 | - | -
R539 | footnote_qualifier | p22 L656 | - | -
R540 | date | p23 L670 | - | -
R541 | slide_number | p23 L674 | - | -
R542 | slide_number | p23 L674 | - | -
R543 | footnote_qualifier | p23 L676 | LABEL_MISMATCH | -
R544 | slide_number | p23 L681 | - | -
R545 | slide_number | p23 L681 | - | -
R546 | footnote_qualifier | p23 L688 | - | -
R547 | date | p24 L701 | - | -
R548 | slide_number | p24 L705 | - | -
R549 | slide_number | p24 L705 | - | -
R550 | footnote_qualifier | p24 L707 | LABEL_MISMATCH | -
R551 | slide_number | p24 L712 | - | -
R552 | slide_number | p24 L712 | - | -
R553 | footnote_qualifier | p24 L698 | - | -
R554 | entity | p24 L699 | - | -
R555 | date | p25 L725 | - | -
R556 | footnote_qualifier | p26 L768 | - | -
R557 | footnote_qualifier | p26 L743 | - | -
R558 | slide_number | p26 L745 | CHART_ORDER_UNRESOLVED | -
R559 | slide_number | p26 L748 | CHART_ORDER_UNRESOLVED | -
R560 | slide_number | p26 L750 | CHART_ORDER_UNRESOLVED | -
R561 | slide_number | p26 L751 | CHART_ORDER_UNRESOLVED | -
R562 | slide_number | p26 L748 | CHART_ORDER_UNRESOLVED | -
R563 | slide_number | p26 L749 | CHART_ORDER_UNRESOLVED | -
R564 | slide_number | p26 L751 | CHART_ORDER_UNRESOLVED | -
R565 | slide_number | p26 L752 | CHART_ORDER_UNRESOLVED | -
R566 | slide_number | p26 L748 | CHART_ORDER_UNRESOLVED | -
R567 | slide_number | p26 L749 | CHART_ORDER_UNRESOLVED | -
R568 | slide_number | p26 L751 | CHART_ORDER_UNRESOLVED | -
R569 | slide_number | p26 L752 | CHART_ORDER_UNRESOLVED | -
R570 | slide_number | p26 L757 | CHART_ORDER_UNRESOLVED | -
R571 | slide_number | p26 L760 | CHART_ORDER_UNRESOLVED | -
R572 | slide_number | p26 L761 | CHART_ORDER_UNRESOLVED | -
R573 | slide_number | p26 L746 | CHART_ORDER_UNRESOLVED | -
R574 | slide_number | p26 L748 | CHART_ORDER_UNRESOLVED | -
R575 | slide_number | p26 L754 | CHART_ORDER_UNRESOLVED | -
R576 | slide_number | p26 L755 | CHART_ORDER_UNRESOLVED | -
R577 | slide_number | p26 L758 | CHART_ORDER_UNRESOLVED | -
R578 | slide_number | p26 L751 | CHART_ORDER_UNRESOLVED | -
R579 | slide_number | p26 L753 | CHART_ORDER_UNRESOLVED | -
R580 | slide_number | p26 L754 | CHART_ORDER_UNRESOLVED | -
R581 | date | p28 L785 | - | -
R582 | date | p28 L788 | - | -
R583 | date | p28 L785 | - | -
R584 | slide_number | p28 L793 | LAYOUT_SCRAMBLED | -
R585 | slide_number | p28 L793 | LAYOUT_SCRAMBLED | -
R586 | slide_number | p28 L793 | LAYOUT_SCRAMBLED | -
R587 | slide_number | p28 L793 | LAYOUT_SCRAMBLED | -
R588 | slide_number | p28 L793 | LAYOUT_SCRAMBLED | -
R589 | slide_number | p28 L793 | LAYOUT_SCRAMBLED | -
R590 | slide_number | p28 L793 | LAYOUT_SCRAMBLED | -
R591 | slide_number | p28 L793 | LAYOUT_SCRAMBLED | -
R592 | slide_number | p28 L793 | LAYOUT_SCRAMBLED | -
R593 | slide_number | p28 L793 | LAYOUT_SCRAMBLED | -
R594 | slide_number | p28 L813 | LAYOUT_SCRAMBLED | -
R595 | slide_number | p28 L813 | LAYOUT_SCRAMBLED | -
R596 | slide_number | p28 L813 | LAYOUT_SCRAMBLED | -
R597 | slide_number | p28 L813 | LAYOUT_SCRAMBLED | -
R598 | slide_number | p28 L813 | LAYOUT_SCRAMBLED | -
R599 | slide_number | p28 L813 | LAYOUT_SCRAMBLED | -
R600 | slide_number | p28 L813 | LAYOUT_SCRAMBLED | -
R601 | slide_number | p28 L813 | LAYOUT_SCRAMBLED | -
R602 | slide_number | p28 L813 | LAYOUT_SCRAMBLED | -
R603 | slide_number | p28 L813 | LAYOUT_SCRAMBLED | -
R604 | slide_number | p28 L826 | LAYOUT_SCRAMBLED | -
R605 | slide_number | p28 L826 | LAYOUT_SCRAMBLED | -
R606 | slide_number | p28 L826 | LAYOUT_SCRAMBLED | -
R607 | slide_number | p28 L826 | LAYOUT_SCRAMBLED | -
R608 | slide_number | p28 L826 | LAYOUT_SCRAMBLED | -
R609 | slide_number | p28 L826 | LAYOUT_SCRAMBLED | -
R610 | slide_number | p28 L826 | LAYOUT_SCRAMBLED | -
R611 | slide_number | p28 L826 | LAYOUT_SCRAMBLED | -
R612 | slide_number | p28 L826 | LAYOUT_SCRAMBLED | -
R613 | slide_number | p28 L826 | LAYOUT_SCRAMBLED | -
R614 | slide_number | p28 L788 | - | -
R615 | entity | p28 L784 | - | -
R616 | entity | p28 L843 | - | -
R617 | slide_number | p29 L858 | - | -
R618 | slide_number | p29 L858 | - | -
R619 | date | p29 L859 | - | -
R620 | slide_number | p29 L855 | - | -
R621 | slide_number | p29 L855 | - | -
R622 | superseded_number | p29 L864 | SUPERSEDED,CHART_ORDER_UNRESOLVED | superseded by R719-R724 (use successor)
R623 | superseded_number | p29 L865 | SUPERSEDED,CHART_ORDER_UNRESOLVED | superseded by R719-R724 (use successor)
R624 | superseded_number | p29 L866 | SUPERSEDED,CHART_ORDER_UNRESOLVED | superseded by R719-R724 (use successor)
R625 | superseded_number | p29 L867 | SUPERSEDED,CHART_ORDER_UNRESOLVED | superseded by R719-R724 (use successor)
R626 | superseded_number | p29 L869 | SUPERSEDED,CHART_ORDER_UNRESOLVED | superseded by R719-R724 (use successor)
R627 | superseded_number | p29 L870 | SUPERSEDED,CHART_ORDER_UNRESOLVED | superseded by R719-R724 (use successor)
R628 | footnote_qualifier | p29 L850 | - | -
R629 | entity | p29 L851 | - | -
R630 | date | p30 L892 | - | -
R631 | entity | p30 L896 | - | -
R632 | slide_number | p32 L915 | - | -
R633 | entity | p32 L919 | - | -
R634 | entity | p32 L920 | - | -
R635 | entity | p32 L924 | - | -
R636 | entity | p32 L913 | - | -
R637 | slide_number | p34 L939 | - | -
R638 | forward_statement | p34 L936 | - | -
R639 | entity | p34 L934 | - | -
R640 | footnote_qualifier | p36 L998 | - | -
R641 | date | p36 L983 | - | -
R642 | superseded_number | p36 L983 | SUPERSEDED,CHART_ORDER_UNRESOLVED | superseded by R725-R733 (use successor)
R643 | superseded_number | p36 L983 | SUPERSEDED,CHART_ORDER_UNRESOLVED | superseded by R725-R733 (use successor)
R644 | superseded_number | p36 L983 | SUPERSEDED,CHART_ORDER_UNRESOLVED | superseded by R725-R733 (use successor)
R645 | superseded_number | p36 L983 | SUPERSEDED,CHART_ORDER_UNRESOLVED | superseded by R725-R733 (use successor)
R646 | superseded_number | p36 L983 | SUPERSEDED,CHART_ORDER_UNRESOLVED | superseded by R725-R733 (use successor)
R647 | superseded_number | p36 L983 | SUPERSEDED,CHART_ORDER_UNRESOLVED | superseded by R725-R733 (use successor)
R648 | superseded_number | p36 L983 | SUPERSEDED,CHART_ORDER_UNRESOLVED | superseded by R725-R733 (use successor)
R649 | superseded_number | p36 L983 | SUPERSEDED,CHART_ORDER_UNRESOLVED | superseded by R725-R733 (use successor)
R650 | superseded_number | p36 L983 | SUPERSEDED,CHART_ORDER_UNRESOLVED | superseded by R725-R733 (use successor)
R651 | slide_number | p36 L973 | - | -
R652 | slide_number | p36 L975 | - | -
R653 | slide_number | p36 L969 | - | -
R654 | forward_statement | p36 L981 | - | -
R655 | date | p36 L979 | - | -
R656 | entity | p36 L989 | - | -
R657 | date | p38 L1009 | - | -
R658 | date | p38 L1021 | - | -
R659 | date | p38 L1009 | - | -
R660 | date | p38 L1021 | - | -
R661 | date | p38 L1009 | - | -
R662 | date | p38 L1021 | - | -
R663 | date | p38 L1009 | - | -
R664 | date | p38 L1021 | - | -
R665 | date | p38 L1009 | - | -
R666 | date | p38 L1021 | - | -
R667 | date | p38 L1009 | - | -
R668 | date | p38 L1021 | - | -
R669 | slide_number | p38 L1012 | - | -
R670 | slide_number | p38 L1024 | - | -
R671 | slide_number | p38 L1015 | - | -
R672 | slide_number | p38 L1030 | - | -
R673 | slide_number | p38 L1029 | - | -
R674 | slide_number | p38 L1035 | - | -
R675 | slide_number | p38 L1035 | - | -
R676 | slide_number | p38 L1036 | - | -
R677 | slide_number | p38 L1036 | - | -
R678 | date | p38 L1028 | - | -
R679 | entity | p38 L1030 | - | -
R680 | entity | p38 L1018 | - | -
R681 | entity | p38 L1027 | - | -
R682 | entity | p39 L1043 | - | -
R683 | entity | p39 L1043 | - | -
R684 | entity | p39 L1043 | - | -
R685 | entity | p39 L1043 | - | -
R686 | entity | p39 L1043 | - | -
R687 | entity | p39 L1043 | - | -
R688 | slide_number | p39 L1050 | - | -
R689 | footnote_qualifier | p40 L1075 | - | -
R690 | footnote_qualifier | p40 L1066 | - | -
R691 | slide_number | p40 L1067 | - | -
R692 | superseded_number | p40 L1067 | SUPERSEDED,CHART_ORDER_UNRESOLVED | superseded by R734-R738 (use successor)
R693 | superseded_number | p40 L1070 | SUPERSEDED,CHART_ORDER_UNRESOLVED | superseded by R734-R738 (use successor)
R694 | superseded_number | p40 L1071 | SUPERSEDED,CHART_ORDER_UNRESOLVED | superseded by R734-R738 (use successor)
R695 | superseded_number | p40 L1072 | SUPERSEDED,CHART_ORDER_UNRESOLVED | superseded by R734-R738 (use successor)
R696 | slide_number | p40 L1066 | - | -
R697 | slide_number | p40 L1067 | - | -
R698 | slide_number | p40 L1068 | - | -
R699 | slide_number | p40 L1069 | - | -
R700 | slide_number | p40 L1070 | - | -
R701 | slide_number | p40 L1071 | - | -
R702 | slide_number | p40 L1073 | - | -
R703 | date | p40 L1065 | - | -
R704 | date | p40 L1065 | - | -
R705 | entity | p40 L1063 | - | -
R706 | entity | p40 L1073 | - | -
R707 | footnote_qualifier | p41 L1081 | - | -
R708 | entity | p41 L1081 | - | -
R709 | date | p42 L1096 | - | -
R710 | entity | p42 L1098 | - | -
R711 | entity | p42 L1099 | - | -
R712 | footnote_qualifier | p42 L1101 | - | -
R713 | entity | p4 L90 | - | -
R714 | slide_number | p13 L1106 | - | image-transcription successor group start
R715 | slide_number | p13 L1106 | - | -
R716 | slide_number | p13 L1106 | - | -
R717 | slide_number | p13 L1106 | - | -
R718 | slide_number | p13 L1106 | - | -
R719 | slide_number | p29 L1108 | - | image-transcription successor group start
R720 | slide_number | p29 L1108 | - | -
R721 | slide_number | p29 L1108 | - | -
R722 | slide_number | p29 L1108 | - | -
R723 | slide_number | p29 L1108 | - | -
R724 | slide_number | p29 L1108 | - | -
R725 | slide_number | p36 L1109 | - | image-transcription successor group start
R726 | slide_number | p36 L1109 | - | -
R727 | slide_number | p36 L1109 | - | -
R728 | slide_number | p36 L1109 | - | -
R729 | slide_number | p36 L1109 | - | -
R730 | slide_number | p36 L1109 | - | -
R731 | slide_number | p36 L1109 | - | -
R732 | slide_number | p36 L1109 | - | -
R733 | slide_number | p36 L1109 | - | -
R734 | slide_number | p40 L1110 | - | image-transcription successor group start
R735 | slide_number | p40 L1110 | - | -
R736 | slide_number | p40 L1110 | - | -
R737 | slide_number | p40 L1110 | - | -
R738 | slide_number | p40 L1110 | - | -

## 5. ZERO_STANDING
R288 R289 R291 R292 R293 (p15 Exceptional items, dash for FY21, FY22, FY24, FY25, FY26; FY23 R290 not nil). R449 (p16 Long-term borrowings FY25, dash).

## 6. MISSING_FROM_STRUCTURED
none

## 7. OTHER FLAGS
LABEL_MISMATCH: R543 (p23) and R550 (p24) print 'Revenue in Q1FY27' where other slides say H1FY27.
ENTITY_CHANGE: none (no consolidation list in a presentation).
