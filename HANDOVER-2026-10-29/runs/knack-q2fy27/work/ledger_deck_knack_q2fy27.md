# A2 LEDGER: KNACK Q2 FY27 investor presentation (deck)

ids_in_structured: 798 | ids_referenced_in_ledger: 798 | orphan_ids: [] | match: yes
(plus 6 MISSING_FROM_STRUCTURED rows M01-M06, carrying their own fulltext line numbers)

```
=== A2 COUNT TEST ===
METHOD 1 grep/parse of structured row-type tags | METHOD 2 A1 header counts | METHOD 3 independent digit-token sweep of FULLTEXT reconciled to rows
category: slide_numbers          grep_count: 589   sweep_count(header): 589   match: yes
category: entities               grep_count: 69   sweep_count(header): 69   match: yes
category: forward_statements     grep_count: 23   sweep_count(header): 23   match: yes
category: dates                  grep_count: 57   sweep_count(header): 57   match: yes
category: footnotes_qualifiers   grep_count: 60   sweep_count(header): 60   match: yes
category: slides                 grep_count: 36   sweep_count: 36 ([page N] markers; OCR pages 5,13,14 sit inside these)   match: yes
category: total_rows             grep_count: 798  sweep_count: 798 (R001-R798 contiguous, 0 duplicates, every line anchor inside the matching page)   match: yes
category: zero_standing          grep_count: 15   sweep_count: 15 (14 dash cells via value regex + R103 text-zero; A1 tags the same 15)   match: yes
category: fulltext_digit_tokens  fulltext tokens (lines 19-847): 1025; structured value tokens: 848
  independent residual: 136 fulltext tokens whose value is absent from every row text of their page; reconciled:
    slide-number footers, "(1/2)" title fractions, KPI row serials: about 38 (not disclosure)
    chart axis tick labels p28-p30 (36,000.00 ... 0.00, 5%..60%, garbled doubles such as 13,5000.00): about 92 (scale, not data)
    p1 address and signature numerals: 5 -> added as M01-M05; p13 OCR "14%": 1 -> M06; p6 garble "(FY26)": 1, covered by R711
  reverse residual (row value tokens absent from fulltext): p30-p35 text layer is scrambled, A1 read values from 150dpi renders; p5/p13/p14 values come from OCR/renders; p6 ranges (75+, 2040+) tokenise differently. Row anchors point to row-label lines, so token order does not map one to one. Not an error.
gate_a2: pass   (no orphan ids; type counts match; 6 unrowed numbers added as MISSING_FROM_STRUCTURED)
=== END COUNT TEST ===
```

Flags raised: ZERO_STANDING 15 | RESTATED 16 rows | FOOTNOTE_UNRESOLVED 6 | FORWARD_COMMIT 23 | IMAGE_PAGE | MISSING_FROM_STRUCTURED 6. ENTITY_CHANGE and DROPPED_SLIDE: not assessable (no prior ledger or prior deck; first review).

## 1. SLIDES (36)
| slide(page) | title | content type | rows N/E/F/D/Q | A2 flags | note |
|---|---|---|---|---|---|
| 1 | Exchange cover letter | text | 4/4/0/4/2 | - | fulltext L19; ids R001..R703 (ids by row order, not contiguous) |
| 2 | Earnings Call title | text | 0/0/0/1/0 | - | fulltext L50; ids R655..R655 (ids by row order, not contiguous) |
| 3 | Safe Harbor | text | 0/1/0/0/3 | - | fulltext L55; ids R626..R706 (ids by row order, not contiguous) |
| 4 | Divider: Company Overview (photo, footer 3) | divider | 0/0/0/0/0 | DIVIDER_NO_ROWS | fulltext L76; ids none (ids by row order, not contiguous) |
| 5 | Knack Founding Vision | image (OCR) | 6/3/0/1/4 | IMAGE_PAGE | fulltext L78; ids R005..R767 (ids by row order, not contiguous) |
| 6 | Knack Packaging Limited Snapshot | text+tiles | 24/3/0/6/6 | - | fulltext L82; ids R006..R712 (ids by row order, not contiguous) |
| 7 | Journey Over The Years | timeline | 4/4/0/13/3 | - | fulltext L104; ids R030..R715 (ids by row order, not contiguous) |
| 8 | Divider (photo, footer 7) | divider | 0/0/0/0/0 | DIVIDER_NO_ROWS | fulltext L143; ids none (ids by row order, not contiguous) |
| 9 | Tailored Packaging Solutions For Every Need | text+image | 3/0/0/1/2 | IMAGE_PAGE | fulltext L145; ids R034..R717 (ids by row order, not contiguous) |
| 10 | Benefits of PLWPP Pinch Bottom Bags | text+list | 1/2/1/0/2 | - | fulltext L149; ids R037..R719 (ids by row order, not contiguous) |
| 11 | Growth in PLWPP Pinch Bottom Machinery | chart | 6/0/0/4/0 | - | fulltext L172; ids R038..R679 (ids by row order, not contiguous) |
| 12 | Knack Infrastructure | image-only | 0/1/0/0/0 | IMAGE_PAGE | fulltext L188; ids R589..R589 (ids by row order, not contiguous) |
| 13 | Manufacturing and Sales Office Facilities: India & Global | image map (OCR) | 2/9/0/5/2 | IMAGE_PAGE | fulltext L191; ids R590..R784 (ids by row order, not contiguous) |
| 14 | Vertically Integrated Manufacturing Process | image (OCR) | 7/7/0/0/1 | IMAGE_PAGE | fulltext L194; ids R591..R798 (ids by row order, not contiguous) |
| 15 | Sayem Knack: JV Plant in Mexico | text+photo | 2/2/0/2/0 | - | fulltext L200; ids R044..R681 (ids by row order, not contiguous) |
| 16 | Recent Update: Order Received & Contract Renewal | text | 5/2/3/1/2 | - | fulltext L211; ids R046..R721 (ids by row order, not contiguous) |
| 17 | Knack Unique Proposition / Early movers | text | 7/1/1/2/3 | - | fulltext L226; ids R051..R724 (ids by row order, not contiguous) |
| 18 | Entry Barrier | image-only | 0/1/0/0/0 | IMAGE_PAGE | fulltext L243; ids R592..R592 (ids by row order, not contiguous) |
| 19 | Growth Strategies | text | 1/1/10/2/1 | - | fulltext L246; ids R058..R725 (ids by row order, not contiguous) |
| 20 | Divider: Experienced Management (photo) | divider | 0/0/0/0/0 | DIVIDER_NO_ROWS | fulltext L266; ids none (ids by row order, not contiguous) |
| 21 | Experienced Management & Qualified Workforce (1) | text+photo | 3/8/0/1/0 | - | fulltext L267; ids R059..R687 (ids by row order, not contiguous) |
| 22 | Experienced Management & Qualified Workforce (2, Independent Directors) | text+photo | 3/7/0/3/0 | - | fulltext L288; ids R062..R690 (ids by row order, not contiguous) |
| 23 | Experienced Management & Qualified Workforce (3) | text+photo | 2/8/0/4/1 | - | fulltext L309; ids R065..R726 (ids by row order, not contiguous) |
| 24 | Divider (photo, footer 23) | divider | 0/0/0/0/0 | DIVIDER_NO_ROWS | fulltext L335; ids none (ids by row order, not contiguous) |
| 25 | Sustainability (divider) | divider | 0/1/0/0/0 | - | fulltext L337; ids R627..R627 (ids by row order, not contiguous) |
| 26 | Executive Summary | table+text | 37/1/3/3/5 | - | fulltext L339; ids R067..R731 (ids by row order, not contiguous) |
| 27 | Financial Highlights | table | 85/0/0/0/2 | - | fulltext L358; ids R104..R733 (ids by row order, not contiguous) |
| 28 | Revenue Analysis | chart+text | 20/0/2/0/3 | - | fulltext L371; ids R189..R736 (ids by row order, not contiguous) |
| 29 | EBITDA Analysis | chart | 36/0/0/0/2 | - | fulltext L401; ids R209..R738 (ids by row order, not contiguous) |
| 30 | Key Financial Ratios - Consolidated | table+chart+text | 50/0/3/1/4 | - | fulltext L432; ids R245..R742 (ids by row order, not contiguous) |
| 31 | Restated Consolidated Statement of Profit and Loss | table | 139/0/0/2/5 | - | fulltext L469; ids R295..R747 (ids by row order, not contiguous) |
| 32 | Restated Consolidated Statement of Assets and Liabilities (1/2) | table | 35/0/0/0/2 | - | fulltext L507; ids R434..R749 (ids by row order, not contiguous) |
| 33 | Restated Consolidated Statement of Assets and Liabilities (2/2) | table | 37/0/0/0/2 | - | fulltext L538; ids R469..R751 (ids by row order, not contiguous) |
| 34 | Consolidated Statement of Cash Flows (1/2) | table | 45/0/0/1/2 | - | fulltext L570; ids R506..R753 (ids by row order, not contiguous) |
| 35 | Consolidated Statement of Cash Flows (2/2) | table | 23/0/0/0/1 | - | fulltext L604; ids R550..R754 (ids by row order, not contiguous) |
| 36 | Thank You / contact block | text | 2/3/0/0/0 | - | fulltext L625; ids R574..R625 (ids by row order, not contiguous) |

Printed slide number = page minus 1. DROPPED_SLIDE test not run (no prior deck).

## 2. SLIDE NUMBERS (every number; 589 rows)
| ROW_ID | page/line | A2 flags | cross-ref / note |
|---|---|---|---|
| R001 | p1 L20 | - | - |
| R002 | p1 L27 | RESTATED | also R574 |
| R003 | p1 L48 | - | - |
| R004 | p1 L43 | - | - |
| R005 | p5 L80 | - | - |
| R006 | p6 L90 | - | - |
| R007 | p6 L90 | - | - |
| R008 | p6 L94 | - | - |
| R009 | p6 L94 | - | - |
| R010 | p6 L94 | - | - |
| R011 | p6 L94 | - | - |
| R012 | p6 L95 | - | - |
| R013 | p6 L95 | - | - |
| R014 | p6 L96 | RESTATED | also R024 |
| R015 | p6 L96 | RESTATED | also R025 |
| R016 | p6 L97 | RESTATED | also R021 |
| R017 | p6 L97 | RESTATED | also R022 |
| R018 | p6 L99 | - | - |
| R019 | p6 L99 | - | - |
| R020 | p6 L99 | - | - |
| R021 | p6 L99 | RESTATED | also R016 |
| R022 | p6 L99 | RESTATED | also R017 |
| R023 | p6 L101 | - | - |
| R024 | p6 L101 | RESTATED | also R014 |
| R025 | p6 L101 | RESTATED | also R015 |
| R026 | p6 L101 | - | - |
| R027 | p6 L101 | - | - |
| R028 | p6 L87 | - | - |
| R029 | p6 L87 | - | - |
| R030 | p7 L124 | - | - |
| R031 | p7 L107 | - | - |
| R032 | p7 L131 | - | - |
| R033 | p7 L137 | - | - |
| R034 | p9 L147 | - | - |
| R035 | p9 L147 | - | - |
| R036 | p9 L147 | - | - |
| R037 | p10 L158 | - | - |
| R038 | p11 L174 | - | - |
| R039 | p11 L174 | - | - |
| R040 | p11 L174 | - | - |
| R041 | p11 L174 | - | - |
| R042 | p11 L185 | - | - |
| R043 | p11 L184 | - | - |
| R044 | p15 L209 | - | - |
| R045 | p15 L206 | - | - |
| R046 | p16 L213 | - | - |
| R047 | p16 L218 | - | - |
| R048 | p16 L219 | - | - |
| R049 | p16 L220 | - | - |
| R050 | p16 L215 | - | - |
| R051 | p17 L230 | - | - |
| R052 | p17 L238 | - | - |
| R053 | p17 L234 | - | - |
| R054 | p17 L235 | - | - |
| R055 | p17 L236 | - | - |
| R056 | p17 L237 | - | - |
| R057 | p17 L237 | - | - |
| R058 | p19 L260 | - | - |
| R059 | p21 L275 | - | - |
| R060 | p21 L275 | - | - |
| R061 | p21 L275 | - | - |
| R062 | p22 L299 | - | - |
| R063 | p22 L296 | - | - |
| R064 | p22 L297 | - | - |
| R065 | p23 L320 | - | A1:NAME_MAPPING_UNRESOLVED |
| R066 | p23 L332 | - | - |
| R067 | p26 L341 | - | - |
| R068 | p26 L343 | - | - |
| R069 | p26 L344 | - | - |
| R070 | p26 L341 | - | - |
| R071 | p26 L343 | - | - |
| R072 | p26 L344 | - | - |
| R073 | p26 L341 | - | - |
| R074 | p26 L343 | - | - |
| R075 | p26 L344 | - | - |
| R076 | p26 L341 | - | - |
| R077 | p26 L343 | - | - |
| R078 | p26 L344 | - | - |
| R079 | p26 L341 | - | - |
| R080 | p26 L343 | - | - |
| R081 | p26 L344 | - | - |
| R082 | p26 L345 | - | - |
| R083 | p26 L347 | - | - |
| R084 | p26 L348 | - | - |
| R085 | p26 L347 | - | - |
| R086 | p26 L348 | - | - |
| R087 | p26 L345 | - | - |
| R088 | p26 L347 | - | - |
| R089 | p26 L348 | - | - |
| R090 | p26 L345 | - | - |
| R091 | p26 L347 | - | - |
| R092 | p26 L348 | - | - |
| R093 | p26 L347 | - | - |
| R094 | p26 L348 | - | - |
| R095 | p26 L350 | - | - |
| R096 | p26 L350 | - | - |
| R097 | p26 L350 | - | - |
| R098 | p26 L350 | - | - |
| R099 | p26 L350 | - | - |
| R100 | p26 L352 | - | - |
| R101 | p26 L353 | - | - |
| R102 | p26 L355 | - | - |
| R103 | p26 L356 | ZERO_STANDING | zero JV revenue offset (text) |
| R104 | p27 L363 | - | - |
| R105 | p27 L363 | - | - |
| R106 | p27 L363 | - | - |
| R107 | p27 L363 | - | - |
| R108 | p27 L363 | - | - |
| R109 | p27 L363 | - | - |
| R110 | p27 L364 | - | - |
| R111 | p27 L364 | - | - |
| R112 | p27 L364 | - | - |
| R113 | p27 L364 | - | - |
| R114 | p27 L364 | - | - |
| R115 | p27 L364 | - | - |
| R116 | p27 L365 | - | - |
| R117 | p27 L365 | - | - |
| R118 | p27 L365 | - | - |
| R119 | p27 L365 | - | - |
| R120 | p27 L365 | - | - |
| R121 | p27 L365 | - | - |
| R122 | p27 L366 | - | - |
| R123 | p27 L366 | - | - |
| R124 | p27 L366 | - | - |
| R125 | p27 L366 | - | - |
| R126 | p27 L366 | - | - |
| R127 | p27 L366 | - | - |
| R128 | p27 L367 | - | - |
| R129 | p27 L367 | - | - |
| R130 | p27 L367 | - | - |
| R131 | p27 L367 | - | - |
| R132 | p27 L367 | - | - |
| R133 | p27 L367 | - | - |
| R134 | p27 L368 | - | - |
| R135 | p27 L368 | - | - |
| R136 | p27 L368 | - | - |
| R137 | p27 L368 | - | - |
| R138 | p27 L368 | - | - |
| R139 | p27 L368 | - | - |
| R140 | p27 L369 | - | - |
| R141 | p27 L369 | - | - |
| R142 | p27 L369 | - | - |
| R143 | p27 L369 | - | - |
| R144 | p27 L369 | - | - |
| R145 | p27 L369 | - | - |
| R146 | p27 L363 | - | - |
| R147 | p27 L363 | - | - |
| R148 | p27 L363 | - | - |
| R149 | p27 L363 | - | - |
| R150 | p27 L363 | - | - |
| R151 | p27 L363 | - | - |
| R152 | p27 L364 | - | - |
| R153 | p27 L364 | - | - |
| R154 | p27 L364 | - | - |
| R155 | p27 L364 | - | - |
| R156 | p27 L364 | - | - |
| R157 | p27 L364 | - | - |
| R158 | p27 L365 | - | - |
| R159 | p27 L365 | - | - |
| R160 | p27 L365 | - | - |
| R161 | p27 L365 | - | - |
| R162 | p27 L365 | - | - |
| R163 | p27 L365 | - | - |
| R164 | p27 L366 | - | - |
| R165 | p27 L366 | - | - |
| R166 | p27 L366 | - | - |
| R167 | p27 L366 | - | - |
| R168 | p27 L366 | - | - |
| R169 | p27 L366 | - | - |
| R170 | p27 L367 | - | - |
| R171 | p27 L367 | - | - |
| R172 | p27 L367 | - | - |
| R173 | p27 L367 | - | - |
| R174 | p27 L367 | - | - |
| R175 | p27 L367 | - | - |
| R176 | p27 L368 | - | - |
| R177 | p27 L368 | - | - |
| R178 | p27 L368 | - | - |
| R179 | p27 L368 | - | - |
| R180 | p27 L368 | - | - |
| R181 | p27 L368 | - | - |
| R182 | p27 L369 | - | - |
| R183 | p27 L369 | - | - |
| R184 | p27 L369 | - | - |
| R185 | p27 L369 | - | - |
| R186 | p27 L369 | - | - |
| R187 | p27 L369 | - | - |
| R188 | p27 L360 | RESTATED | also R433,R468,R505,R572,R573 |
| R189 | p28 L378 | - | - |
| R190 | p28 L378 | - | - |
| R191 | p28 L378 | - | - |
| R192 | p28 L375 | - | - |
| R193 | p28 L395 | - | - |
| R194 | p28 L385 | - | - |
| R195 | p28 L391 | - | - |
| R196 | p28 L388 | - | - |
| R197 | p28 L378 | - | A1:HIDDEN_SERIES |
| R198 | p28 L376 | - | A1:HIDDEN_SERIES |
| R199 | p28 L391 | - | A1:HIDDEN_SERIES |
| R200 | p28 L389 | - | A1:HIDDEN_SERIES |
| R201 | p28 L377 | - | - |
| R202 | p28 L378 | - | - |
| R203 | p28 L378 | - | - |
| R204 | p28 L380 | - | - |
| R205 | p28 L385 | - | - |
| R206 | p28 L393 | - | - |
| R207 | p28 L393 | - | - |
| R208 | p28 L393 | - | - |
| R209 | p29 L413 | - | - |
| R210 | p29 L409 | - | - |
| R211 | p29 L413 | - | - |
| R212 | p29 L411 | - | - |
| R213 | p29 L413 | - | - |
| R214 | p29 L409 | - | - |
| R215 | p29 L413 | - | - |
| R216 | p29 L405 | - | - |
| R217 | p29 L430 | - | - |
| R218 | p29 L422 | - | - |
| R219 | p29 L430 | - | - |
| R220 | p29 L424 | - | - |
| R221 | p29 L430 | - | - |
| R222 | p29 L422 | - | - |
| R223 | p29 L430 | - | - |
| R224 | p29 L420 | - | - |
| R225 | p29 L413 | - | - |
| R226 | p29 L409 | - | - |
| R227 | p29 L413 | - | - |
| R228 | p29 L407 | - | - |
| R229 | p29 L413 | - | - |
| R230 | p29 L407 | - | - |
| R231 | p29 L430 | - | - |
| R232 | p29 L424 | - | - |
| R233 | p29 L430 | - | - |
| R234 | p29 L422 | - | - |
| R235 | p29 L430 | - | - |
| R236 | p29 L420 | - | - |
| R237 | p29 L413 | - | A1:HIDDEN_SERIES |
| R238 | p29 L410 | - | A1:HIDDEN_SERIES |
| R239 | p29 L413 | - | A1:HIDDEN_SERIES |
| R240 | p29 L404 | - | A1:HIDDEN_SERIES |
| R241 | p29 L430 | - | A1:HIDDEN_SERIES |
| R242 | p29 L428 | - | A1:HIDDEN_SERIES |
| R243 | p29 L430 | - | A1:HIDDEN_SERIES |
| R244 | p29 L422 | - | A1:HIDDEN_SERIES |
| R245 | p30 L436 | - | - |
| R246 | p30 L436 | - | - |
| R247 | p30 L436 | - | - |
| R248 | p30 L436 | - | - |
| R249 | p30 L436 | - | - |
| R250 | p30 L436 | - | - |
| R251 | p30 L438 | - | - |
| R252 | p30 L438 | - | - |
| R253 | p30 L438 | - | - |
| R254 | p30 L438 | - | - |
| R255 | p30 L438 | - | - |
| R256 | p30 L438 | - | - |
| R257 | p30 L440 | - | - |
| R258 | p30 L440 | - | - |
| R259 | p30 L440 | - | - |
| R260 | p30 L440 | - | - |
| R261 | p30 L440 | - | - |
| R262 | p30 L440 | - | - |
| R263 | p30 L442 | - | - |
| R264 | p30 L442 | - | - |
| R265 | p30 L442 | - | - |
| R266 | p30 L442 | - | - |
| R267 | p30 L442 | - | - |
| R268 | p30 L442 | - | - |
| R269 | p30 L443 | - | - |
| R270 | p30 L443 | - | - |
| R271 | p30 L443 | - | - |
| R272 | p30 L443 | - | - |
| R273 | p30 L443 | - | - |
| R274 | p30 L443 | - | - |
| R275 | p30 L446 | - | - |
| R276 | p30 L446 | - | - |
| R277 | p30 L447 | - | - |
| R278 | p30 L447 | - | - |
| R279 | p30 L453 | - | - |
| R280 | p30 L460 | - | - |
| R281 | p30 L460 | - | - |
| R282 | p30 L462 | - | - |
| R283 | p30 L456 | - | - |
| R284 | p30 L456 | - | - |
| R285 | p30 L448 | - | - |
| R286 | p30 L453 | - | - |
| R287 | p30 L439 | - | - |
| R288 | p30 L452 | - | - |
| R289 | p30 L455 | - | A1:HIDDEN_SERIES PERIOD_UNMAPPED |
| R290 | p30 L455 | - | A1:HIDDEN_SERIES PERIOD_UNMAPPED |
| R291 | p30 L449 | - | A1:HIDDEN_SERIES PERIOD_UNMAPPED |
| R292 | p30 L447 | - | A1:HIDDEN_SERIES PERIOD_UNMAPPED |
| R293 | p30 L451 | - | A1:HIDDEN_SERIES PERIOD_UNMAPPED |
| R294 | p30 L451 | - | A1:HIDDEN_SERIES PERIOD_UNMAPPED |
| R295 | p31 L473 | - | - |
| R296 | p31 L473 | - | - |
| R297 | p31 L473 | - | - |
| R298 | p31 L473 | - | - |
| R299 | p31 L473 | - | - |
| R300 | p31 L473 | - | - |
| R301 | p31 L474 | - | - |
| R302 | p31 L474 | - | - |
| R303 | p31 L474 | - | - |
| R304 | p31 L474 | - | - |
| R305 | p31 L474 | - | - |
| R306 | p31 L474 | - | - |
| R307 | p31 L476 | - | - |
| R308 | p31 L476 | - | - |
| R309 | p31 L476 | - | - |
| R310 | p31 L476 | - | - |
| R311 | p31 L476 | - | - |
| R312 | p31 L476 | - | - |
| R313 | p31 L479 | - | - |
| R314 | p31 L479 | - | - |
| R315 | p31 L479 | - | - |
| R316 | p31 L479 | - | - |
| R317 | p31 L479 | - | - |
| R318 | p31 L479 | - | - |
| R319 | p31 L480 | - | - |
| R320 | p31 L480 | - | - |
| R321 | p31 L480 | - | - |
| R322 | p31 L480 | - | - |
| R323 | p31 L480 | - | - |
| R324 | p31 L480 | - | - |
| R325 | p31 L481 | - | - |
| R326 | p31 L481 | - | - |
| R327 | p31 L481 | - | - |
| R328 | p31 L481 | - | - |
| R329 | p31 L481 | - | - |
| R330 | p31 L481 | - | - |
| R331 | p31 L482 | - | - |
| R332 | p31 L482 | - | - |
| R333 | p31 L482 | - | - |
| R334 | p31 L482 | - | - |
| R335 | p31 L482 | - | - |
| R336 | p31 L482 | - | - |
| R337 | p31 L483 | - | - |
| R338 | p31 L483 | - | - |
| R339 | p31 L483 | - | - |
| R340 | p31 L483 | - | - |
| R341 | p31 L483 | - | - |
| R342 | p31 L483 | - | - |
| R343 | p31 L484 | - | - |
| R344 | p31 L484 | - | - |
| R345 | p31 L484 | - | - |
| R346 | p31 L484 | - | - |
| R347 | p31 L484 | - | - |
| R348 | p31 L484 | - | - |
| R349 | p31 L485 | - | - |
| R350 | p31 L485 | - | - |
| R351 | p31 L485 | - | - |
| R352 | p31 L485 | - | - |
| R353 | p31 L485 | - | - |
| R354 | p31 L485 | - | - |
| R355 | p31 L486 | - | - |
| R356 | p31 L486 | - | - |
| R357 | p31 L486 | - | - |
| R358 | p31 L486 | - | - |
| R359 | p31 L486 | - | - |
| R360 | p31 L486 | - | - |
| R361 | p31 L487 | - | - |
| R362 | p31 L487 | - | - |
| R363 | p31 L487 | - | - |
| R364 | p31 L487 | - | - |
| R365 | p31 L487 | - | - |
| R366 | p31 L487 | - | - |
| R367 | p31 L488 | ZERO_STANDING | - |
| R368 | p31 L488 | ZERO_STANDING | - |
| R369 | p31 L488 | ZERO_STANDING | - |
| R370 | p31 L488 | ZERO_STANDING | - |
| R371 | p31 L488 | ZERO_STANDING | - |
| R372 | p31 L488 | - | - |
| R373 | p31 L489 | - | - |
| R374 | p31 L489 | - | - |
| R375 | p31 L489 | - | - |
| R376 | p31 L489 | - | - |
| R377 | p31 L489 | - | - |
| R378 | p31 L489 | - | - |
| R379 | p31 L490 | - | - |
| R380 | p31 L490 | - | - |
| R381 | p31 L490 | - | - |
| R382 | p31 L490 | - | - |
| R383 | p31 L490 | - | - |
| R384 | p31 L490 | - | - |
| R385 | p31 L491 | - | - |
| R386 | p31 L491 | - | - |
| R387 | p31 L491 | - | - |
| R388 | p31 L491 | - | - |
| R389 | p31 L491 | - | - |
| R390 | p31 L491 | - | - |
| R391 | p31 L492 | - | - |
| R392 | p31 L492 | - | - |
| R393 | p31 L492 | - | - |
| R394 | p31 L492 | - | - |
| R395 | p31 L492 | - | - |
| R396 | p31 L492 | - | - |
| R397 | p31 L493 | - | - |
| R398 | p31 L493 | - | - |
| R399 | p31 L493 | - | - |
| R400 | p31 L493 | - | - |
| R401 | p31 L493 | - | - |
| R402 | p31 L493 | - | - |
| R403 | p31 L494 | - | - |
| R404 | p31 L494 | - | - |
| R405 | p31 L494 | - | - |
| R406 | p31 L494 | - | - |
| R407 | p31 L494 | - | - |
| R408 | p31 L494 | - | - |
| R409 | p31 L495 | - | - |
| R410 | p31 L495 | - | - |
| R411 | p31 L495 | - | - |
| R412 | p31 L495 | - | - |
| R413 | p31 L495 | - | - |
| R414 | p31 L495 | - | - |
| R415 | p31 L496 | - | - |
| R416 | p31 L496 | - | - |
| R417 | p31 L496 | - | - |
| R418 | p31 L496 | - | - |
| R419 | p31 L496 | - | - |
| R420 | p31 L496 | - | - |
| R421 | p31 L497 | - | - |
| R422 | p31 L497 | - | - |
| R423 | p31 L497 | - | - |
| R424 | p31 L497 | - | - |
| R425 | p31 L497 | - | - |
| R426 | p31 L497 | - | - |
| R427 | p31 L498 | - | - |
| R428 | p31 L498 | - | - |
| R429 | p31 L498 | - | - |
| R430 | p31 L498 | - | - |
| R431 | p31 L498 | - | - |
| R432 | p31 L498 | - | - |
| R433 | p31 L471 | RESTATED | also R188,R468,R505,R572,R573 |
| R434 | p32 L512 | - | - |
| R435 | p32 L512 | - | - |
| R436 | p32 L513 | - | - |
| R437 | p32 L513 | - | - |
| R438 | p32 L514 | - | - |
| R439 | p32 L514 | - | - |
| R440 | p32 L515 | ZERO_STANDING | - |
| R441 | p32 L515 | - | - |
| R442 | p32 L516 | - | - |
| R443 | p32 L516 | - | - |
| R444 | p32 L517 | - | - |
| R445 | p32 L517 | ZERO_STANDING | - |
| R446 | p32 L518 | - | - |
| R447 | p32 L518 | - | - |
| R448 | p32 L520 | - | - |
| R449 | p32 L520 | - | - |
| R450 | p32 L523 | - | - |
| R451 | p32 L523 | - | - |
| R452 | p32 L526 | - | - |
| R453 | p32 L526 | - | - |
| R454 | p32 L527 | - | - |
| R455 | p32 L527 | - | - |
| R456 | p32 L528 | - | - |
| R457 | p32 L528 | - | - |
| R458 | p32 L529 | - | - |
| R459 | p32 L529 | - | - |
| R460 | p32 L530 | - | - |
| R461 | p32 L530 | - | - |
| R462 | p32 L532 | - | - |
| R463 | p32 L532 | - | - |
| R464 | p32 L533 | - | - |
| R465 | p32 L533 | - | - |
| R466 | p32 L535 | - | - |
| R467 | p32 L535 | - | - |
| R468 | p32 L509 | RESTATED | also R188,R433,R505,R572,R573 |
| R469 | p33 L544 | - | - |
| R470 | p33 L544 | - | - |
| R471 | p33 L545 | - | - |
| R472 | p33 L545 | - | - |
| R473 | p33 L546 | - | - |
| R474 | p33 L546 | - | - |
| R475 | p33 L551 | - | - |
| R476 | p33 L551 | - | - |
| R477 | p33 L552 | - | - |
| R478 | p33 L552 | - | - |
| R479 | p33 L553 | ZERO_STANDING | - |
| R480 | p33 L553 | - | - |
| R481 | p33 L554 | - | - |
| R482 | p33 L554 | ZERO_STANDING | - |
| R483 | p33 L555 | - | - |
| R484 | p33 L555 | - | - |
| R485 | p33 L559 | - | - |
| R486 | p33 L559 | - | - |
| R487 | p33 L560 | - | - |
| R488 | p33 L560 | - | - |
| R489 | p33 L562 | - | - |
| R490 | p33 L562 | - | - |
| R491 | p33 L563 | - | - |
| R492 | p33 L563 | - | - |
| R493 | p33 L564 | - | - |
| R494 | p33 L564 | - | - |
| R495 | p33 L565 | - | - |
| R496 | p33 L565 | - | - |
| R497 | p33 L566 | - | - |
| R498 | p33 L566 | - | - |
| R499 | p33 L567 | - | - |
| R500 | p33 L567 | - | - |
| R501 | p33 L568 | - | - |
| R502 | p33 L568 | - | - |
| R503 | p33 L569 | - | - |
| R504 | p33 L569 | - | - |
| R505 | p33 L540 | RESTATED | also R188,R433,R468,R572,R573 |
| R506 | p34 L576 | - | - |
| R507 | p34 L576 | - | - |
| R508 | p34 L579 | - | - |
| R509 | p34 L579 | - | - |
| R510 | p34 L580 | - | - |
| R511 | p34 L580 | - | - |
| R512 | p34 L581 | - | - |
| R513 | p34 L581 | - | - |
| R514 | p34 L582 | - | - |
| R515 | p34 L582 | - | - |
| R516 | p34 L583 | - | - |
| R517 | p34 L583 | - | - |
| R518 | p34 L584 | - | - |
| R519 | p34 L584 | - | - |
| R520 | p34 L585 | - | - |
| R521 | p34 L585 | - | - |
| R522 | p34 L586 | - | - |
| R523 | p34 L586 | - | - |
| R524 | p34 L588 | - | - |
| R525 | p34 L588 | - | - |
| R526 | p34 L589 | - | - |
| R527 | p34 L589 | - | - |
| R528 | p34 L590 | - | - |
| R529 | p34 L590 | - | - |
| R530 | p34 L591 | - | - |
| R531 | p34 L591 | - | - |
| R532 | p34 L592 | - | - |
| R533 | p34 L592 | - | - |
| R534 | p34 L593 | - | - |
| R535 | p34 L593 | - | - |
| R536 | p34 L596 | - | - |
| R537 | p34 L596 | - | - |
| R538 | p34 L597 | - | - |
| R539 | p34 L597 | - | - |
| R540 | p34 L598 | ZERO_STANDING | - |
| R541 | p34 L598 | - | - |
| R542 | p34 L599 | - | - |
| R543 | p34 L599 | ZERO_STANDING | - |
| R544 | p34 L600 | - | - |
| R545 | p34 L600 | - | - |
| R546 | p34 L601 | - | - |
| R547 | p34 L601 | - | - |
| R548 | p34 L603 | - | - |
| R549 | p34 L603 | - | - |
| R550 | p35 L610 | ZERO_STANDING | - |
| R551 | p35 L610 | - | - |
| R552 | p35 L611 | - | - |
| R553 | p35 L611 | - | - |
| R554 | p35 L612 | - | - |
| R555 | p35 L612 | ZERO_STANDING | - |
| R556 | p35 L613 | - | - |
| R557 | p35 L613 | ZERO_STANDING | - |
| R558 | p35 L614 | - | - |
| R559 | p35 L614 | - | - |
| R560 | p35 L615 | - | - |
| R561 | p35 L615 | - | - |
| R562 | p35 L616 | - | - |
| R563 | p35 L616 | - | - |
| R564 | p35 L617 | - | - |
| R565 | p35 L617 | - | - |
| R566 | p35 L619 | - | - |
| R567 | p35 L619 | - | - |
| R568 | p35 L620 | - | - |
| R569 | p35 L620 | - | - |
| R570 | p35 L621 | - | - |
| R571 | p35 L621 | - | - |
| R572 | p34 L571 | RESTATED | also R188,R433,R468,R505,R573 |
| R573 | p35 L606 | RESTATED | also R188,R433,R468,R505,R572 |
| R574 | p36 L626 | RESTATED | also R002 |
| R575 | p36 L635 | - | - |
| R755 | p5 L79 | - | - |
| R757 | p5 L79 | - | - |
| R758 | p5 L79 | - | - |
| R759 | p5 L79 | - | - |
| R760 | p5 L79 | - | - |
| R779 | p13 L192 | - | - |
| R781 | p13 L192 | - | - |
| R785 | p14 L195 | - | - |
| R786 | p14 L195 | - | - |
| R788 | p14 L195 | - | - |
| R790 | p14 L195 | - | - |
| R792 | p14 L195 | - | - |
| R794 | p14 L195 | - | - |
| R796 | p14 L195 | - | - |

## 3. DATES (57 rows)
| ROW_ID | page/line | A2 flags | cross-ref / note |
|---|---|---|---|
| R651 | p1 L20 | - | - |
| R652 | p1 L31 | - | - |
| R653 | p1 L32 | - | - |
| R654 | p1 L33 | - | - |
| R655 | p2 L54 | - | - |
| R656 | p6 L87 | - | - |
| R657 | p6 L87 | - | - |
| R658 | p6 L90 | - | - |
| R659 | p6 L100 | - | - |
| R660 | p6 L100 | - | - |
| R661 | p6 L94 | - | - |
| R662 | p7 L113 | - | - |
| R663 | p7 L135 | - | - |
| R664 | p7 L120 | - | - |
| R665 | p7 L134 | - | - |
| R666 | p7 L115 | - | - |
| R667 | p7 L136 | - | - |
| R668 | p7 L110 | - | - |
| R669 | p7 L133 | - | - |
| R670 | p7 L107 | - | - |
| R671 | p7 L127 | - | - |
| R672 | p7 L129 | - | - |
| R673 | p7 L106 | - | - |
| R674 | p7 L133 | - | - |
| R675 | p9 L148 | - | - |
| R676 | p11 L184 | - | - |
| R677 | p11 L184 | - | - |
| R678 | p11 L184 | - | - |
| R679 | p11 L184 | - | - |
| R680 | p15 L205 | - | - |
| R681 | p15 L206 | - | - |
| R682 | p16 L220 | - | - |
| R683 | p17 L234 | - | - |
| R684 | p17 L234 | - | - |
| R685 | p19 L249 | - | - |
| R686 | p19 L251 | - | - |
| R687 | p21 L271 | - | - |
| R688 | p22 L304 | - | - |
| R689 | p22 L304 | - | - |
| R690 | p22 L307 | - | - |
| R691 | p23 L311 | - | A1:NAME_MAPPING_UNRESOLVED |
| R692 | p23 L328 | - | - |
| R693 | p23 L315 | - | A1:NAME_MAPPING_UNRESOLVED |
| R694 | p23 L311 | - | - |
| R695 | p26 L353 | - | - |
| R696 | p26 L355 | - | - |
| R697 | p26 L344 | - | - |
| R698 | p30 L434 | - | - |
| R699 | p31 L472 | - | - |
| R700 | p31 L473 | - | - |
| R701 | p34 L572 | - | - |
| R756 | p5 L79 | - | - |
| R769 | p13 L192 | - | - |
| R771 | p13 L192 | - | - |
| R773 | p13 L192 | - | - |
| R775 | p13 L192 | - | - |
| R777 | p13 L192 | - | - |

## 4. ENTITIES (69 rows)
| ROW_ID | page/line | A2 flags | cross-ref / note |
|---|---|---|---|
| R576 | p1 L21 | - | - |
| R577 | p1 L23 | - | - |
| R578 | p1 L39 | - | - |
| R579 | p1 L46 | - | - |
| R580 | p6 L103 | - | - |
| R581 | p6 L84 | - | - |
| R582 | p6 L101 | - | - |
| R583 | p7 L108 | - | - |
| R584 | p7 L109 | - | - |
| R585 | p7 L136 | - | - |
| R586 | p7 L139 | - | - |
| R587 | p10 L167 | - | - |
| R588 | p10 L150 | - | A1:SUMMARY SUMMARY |
| R589 | p12 L189 | IMAGE_PAGE | A1:IMAGE_PAGE |
| R590 | p13 L192 | IMAGE_PAGE | A1:IMAGE_PAGE |
| R591 | p14 L195 | IMAGE_PAGE | A1:IMAGE_PAGE |
| R592 | p18 L244 | IMAGE_PAGE | A1:IMAGE_PAGE |
| R593 | p15 L201 | - | - |
| R594 | p15 L208 | - | - |
| R595 | p16 L216 | - | - |
| R596 | p16 L222 | - | - |
| R597 | p17 L242 | - | - |
| R598 | p19 L251 | - | - |
| R599 | p21 L269 | - | - |
| R600 | p21 L269 | - | - |
| R601 | p21 L269 | - | - |
| R602 | p21 L277 | - | - |
| R603 | p21 L279 | - | - |
| R604 | p21 L281 | - | - |
| R605 | p21 L282 | - | - |
| R606 | p21 L284 | - | - |
| R607 | p22 L291 | - | - |
| R608 | p22 L291 | - | - |
| R609 | p22 L291 | - | - |
| R610 | p22 L302 | - | - |
| R611 | p22 L299 | - | - |
| R612 | p22 L299 | - | - |
| R613 | p22 L303 | - | - |
| R614 | p23 L333 | - | - |
| R615 | p23 L326 | - | A1:NAME_MAPPING_UNRESOLVED |
| R616 | p23 L325 | - | - |
| R617 | p23 L322 | - | - |
| R618 | p23 L320 | - | - |
| R619 | p23 L319 | - | - |
| R620 | p23 L329 | - | - |
| R621 | p23 L319 | - | - |
| R622 | p26 L355 | - | - |
| R623 | p36 L631 | - | - |
| R624 | p36 L626 | - | - |
| R625 | p36 L638 | - | A1:SUMMARY SUMMARY |
| R626 | p3 L56 | - | A1:SUMMARY SUMMARY |
| R627 | p25 L338 | - | A1:SUMMARY |
| R761 | p5 L79 | - | - |
| R762 | p5 L79 | - | - |
| R763 | p5 L79 | - | - |
| R768 | p13 L192 | - | - |
| R770 | p13 L192 | - | - |
| R772 | p13 L192 | - | - |
| R774 | p13 L192 | - | - |
| R776 | p13 L192 | - | - |
| R778 | p13 L192 | - | - |
| R780 | p13 L192 | - | - |
| R782 | p13 L192 | - | - |
| R787 | p14 L195 | - | - |
| R789 | p14 L195 | - | - |
| R791 | p14 L195 | - | - |
| R793 | p14 L195 | - | - |
| R795 | p14 L195 | - | - |
| R797 | p14 L195 | - | - |

## 5. FORWARD-LOOKING STATEMENTS (23 rows)
| ROW_ID | page/line | A2 flags | cross-ref / note |
|---|---|---|---|
| R628 | p10 L163 | FORWARD_COMMIT | - |
| R629 | p16 L215 | FORWARD_COMMIT | - |
| R630 | p16 L220 | FORWARD_COMMIT | - |
| R631 | p16 L218 | FORWARD_COMMIT | - |
| R632 | p17 L238 | FORWARD_COMMIT | - |
| R633 | p19 L248 | FORWARD_COMMIT | - |
| R634 | p19 L250 | FORWARD_COMMIT | - |
| R635 | p19 L253 | FORWARD_COMMIT | - |
| R636 | p19 L258 | FORWARD_COMMIT | - |
| R637 | p19 L260 | FORWARD_COMMIT | - |
| R638 | p19 L262 | FORWARD_COMMIT | - |
| R639 | p19 L249 | FORWARD_COMMIT | - |
| R640 | p19 L251 | FORWARD_COMMIT | - |
| R641 | p19 L261 | FORWARD_COMMIT | - |
| R642 | p19 L258 | FORWARD_COMMIT | - |
| R643 | p26 L353 | FORWARD_COMMIT | - |
| R644 | p26 L356 | FORWARD_COMMIT | - |
| R645 | p26 L355 | FORWARD_COMMIT | - |
| R646 | p28 L388 | FORWARD_COMMIT | - |
| R647 | p28 L394 | FORWARD_COMMIT | - |
| R648 | p30 L458 | FORWARD_COMMIT | - |
| R649 | p30 L455 | FORWARD_COMMIT | - |
| R650 | p30 L463 | FORWARD_COMMIT | - |

## 6. FOOTNOTES, FINE PRINT AND QUALIFIERS (60 rows)
| ROW_ID | page/line | A2 flags | cross-ref / note |
|---|---|---|---|
| R702 | p1 L31 | - | - |
| R703 | p1 L40 | - | - |
| R704 | p3 L56 | - | - |
| R705 | p3 L69 | - | - |
| R706 | p3 L62 | - | - |
| R707 | p6 L103 | - | - |
| R708 | p6 L92 | - | - |
| R709 | p6 L93 | - | - |
| R710 | p6 L99 | - | - |
| R711 | p6 L102 | FOOTNOTE_UNRESOLVED | A1:FOOTNOTE_UNRESOLVED LAYOUT_INTERLEAVED |
| R712 | p6 L90 | - | - |
| R713 | p7 L140 | - | - |
| R714 | p7 L122 | - | - |
| R715 | p7 L137 | - | - |
| R716 | p9 L148 | - | - |
| R717 | p9 L147 | FOOTNOTE_UNRESOLVED | A1:FOOTNOTE_UNRESOLVED |
| R718 | p10 L171 | - | - |
| R719 | p10 L151 | - | - |
| R720 | p16 L225 | - | - |
| R721 | p16 L219 | - | - |
| R722 | p17 L242 | - | - |
| R723 | p17 L231 | - | - |
| R724 | p17 L233 | - | - |
| R725 | p19 L265 | - | A1:LAYOUT_INTERLEAVED LAYOUT_INTERLEAVED |
| R726 | p23 L311 | FOOTNOTE_UNRESOLVED | A1:FOOTNOTE_UNRESOLVED NAME_MAPPING_UNRESOLVED |
| R727 | p26 L344 | - | - |
| R728 | p26 L342 | - | - |
| R729 | p26 L342 | FOOTNOTE_UNRESOLVED | A1:FOOTNOTE_UNRESOLVED FOOTNOTE_UNRESOLVED |
| R730 | p26 L352 | - | - |
| R731 | p26 L351 | - | - |
| R732 | p27 L370 | - | - |
| R733 | p27 L363 | - | - |
| R734 | p28 L400 | - | - |
| R735 | p28 L375 | - | - |
| R736 | p28 L373 | - | A1:LAYOUT_INTERLEAVED |
| R737 | p29 L403 | FOOTNOTE_UNRESOLVED | A1:FOOTNOTE_UNRESOLVED FOOTNOTE_UNRESOLVED |
| R738 | p29 L413 | - | - |
| R739 | p30 L452 | - | - |
| R740 | p30 L434 | FOOTNOTE_UNRESOLVED | A1:FOOTNOTE_UNRESOLVED FOOTNOTE_UNRESOLVED |
| R741 | p30 L461 | - | A1:LAYOUT_INTERLEAVED |
| R742 | p30 L437 | - | - |
| R743 | p31 L470 | - | - |
| R744 | p31 L471 | - | - |
| R745 | p31 L488 | - | - |
| R746 | p31 L489 | - | - |
| R747 | p31 L476 | - | A1:LAYOUT_INTERLEAVED |
| R748 | p32 L508 | - | - |
| R749 | p32 L528 | - | - |
| R750 | p33 L539 | - | - |
| R751 | p33 L569 | - | - |
| R752 | p34 L571 | - | - |
| R753 | p34 L573 | - | A1:LAYOUT_INTERLEAVED |
| R754 | p35 L606 | - | A1:LAYOUT_INTERLEAVED |
| R764 | p5 L79 | - | - |
| R765 | p5 L79 | - | - |
| R766 | p5 L79 | - | - |
| R767 | p5 L79 | - | - |
| R783 | p13 L192 | - | - |
| R784 | p13 L192 | - | - |
| R798 | p14 L195 | - | - |

## 7. MISSING_FROM_STRUCTURED (6 rows; loop back to A1)
| ID | page | fulltext line | claim text | materiality |
|---|---|---|---|---|
| M01 | p1 | L22 | 5th (Floor) in NSE address "Exchange Plaza 5th Floor, Plot no. C/1" | MISSING_FROM_STRUCTURED; address ordinal, low materiality |
| M02 | p1 | L24 | 400051 (NSE PIN code) | MISSING_FROM_STRUCTURED; address, low materiality |
| M03 | p1 | L25 | 25th (Floor) in BSE address "25th Floor, P J Towers" | MISSING_FROM_STRUCTURED; address ordinal, low materiality |
| M04 | p1 | L26 | 400001 (BSE PIN code) | MISSING_FROM_STRUCTURED; address, low materiality |
| M05 | p1 | L45 | +05'30' (time-zone offset in digital signature block) | MISSING_FROM_STRUCTURED; signature block, pairs with R004 timestamp |
| M06 | p13 | L704 | 14% (stray OCR token between "nine" and "UNIT-5" on the India map slide; no label recoverable from OCR) | MISSING_FROM_STRUCTURED; UNLABELLED; may be a utilisation or share figure; loop back to A1 render check |

## 8. ZERO_STANDING INDEX (15)
| ROW_ID | page/line | line item |
|---|---|---|
| R103 | p26 L356 | JV revenue offset in consolidated PAT, today [ZERO_STANDING] |
| R367 | p31 L488 | consolidated P&L Exceptional Item -- Labour Codes, Q2 FY27 (3M Sep 30 2026) [RENDER_CHECKED ZERO_STANDING] |
| R368 | p31 L488 | consolidated P&L Exceptional Item -- Labour Codes, Q1 FY27 (3M Jun 30 2026) [RENDER_CHECKED ZERO_STANDING] |
| R369 | p31 L488 | consolidated P&L Exceptional Item -- Labour Codes, Q2 FY26 (3M Sep 30 2025) [RENDER_CHECKED ZERO_STANDING] |
| R370 | p31 L488 | consolidated P&L Exceptional Item -- Labour Codes, H1 FY27 (6M Sep 30 2026) [RENDER_CHECKED ZERO_STANDING] |
| R371 | p31 L488 | consolidated P&L Exceptional Item -- Labour Codes, H1 FY26 (6M Sep 30 2025) [RENDER_CHECKED ZERO_STANDING] |
| R440 | p32 L515 | consolidated balance sheet Investments accounted for equity method, As at Sept 30, 2026 [RENDER_CHECKED ZERO_S |
| R445 | p32 L517 | consolidated balance sheet Deferred Tax Assets (Net), As at March 31, 2026 [RENDER_CHECKED ZERO_STANDING] |
| R479 | p33 L553 | consolidated balance sheet Deferred Tax Liabilities (Net), As at Sept 30, 2026 [RENDER_CHECKED ZERO_STANDING] |
| R482 | p33 L554 | consolidated balance sheet Non-current Provisions, As at March 31, 2026 [RENDER_CHECKED ZERO_STANDING] |
| R540 | p34 L598 | consolidated cash flow Purchase of equity investment measured at cost, H1 FY27 (Sept 30, 2026 Unaudited) [REND |
| R543 | p34 L599 | consolidated cash flow Investment in FD, H1 FY26 (Sept 30, 2025 Unaudited) [RENDER_CHECKED ZERO_STANDING] |
| R550 | p35 L610 | consolidated cash flow Proceed from long term borrowings, H1 FY27 (Sept 30, 2026 Unaudited) [RENDER_CHECKED ZE |
| R555 | p35 L612 | consolidated cash flow Proceeds from issue of share capital, H1 FY26 (Sept 30, 2025 Unaudited) [RENDER_CHECKED |
| R557 | p35 L613 | consolidated cash flow Share issue expense (net of tax), H1 FY26 (Sept 30, 2025 Unaudited) [RENDER_CHECKED ZER |

## 9. RESTATED GROUPS
- R002, R574 : 544814
- R014, R024 : 19.14%
- R015, R025 : 9.76%
- R016, R021 : 32.31%
- R017, R022 : 21.29%
- R188, R433, R468, R505, R572, R573 : Rs In Million
