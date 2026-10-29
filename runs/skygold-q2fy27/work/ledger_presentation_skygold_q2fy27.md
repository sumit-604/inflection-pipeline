# A2 LEDGER: SKYGOLD presentation q2fy27
source: runs/skygold-q2fy27/extracted/skygold-presentation-q2fy27-structured.md (A1). Prior ledger: none (DROPPED_SLIDE test not runnable; no slide flagged).

ids_in_structured: 915 | ids_referenced_in_ledger: 915 | orphan_ids: [] | match: yes

```
=== A2 COUNT TEST ===
method 1 = A1 header COUNTS and R-line grep; method 2 = independent per-slide numeric-token sweep of FULLTEXT diffed against structured rows (multiset, commas/signs normalised)
category: row_ids          grep_count: 915  header_range: 915 (R001-R915)  sweep_count: 915  match: yes
category: NUMBER           header: 760  grep_count: 760  sweep_count: 760  match: yes
category: ENTITY(+SUMMARY) header: 53  grep_count: 53  sweep_count: 53  match: yes
category: FORWARD         header: 30  grep_count: 30  sweep_count: 30  match: yes
category: DATE            header: 35  grep_count: 35  sweep_count: 35  match: yes
category: QUALIFIER       header: 37  grep_count: 37  sweep_count: 37  match: yes
category: slides          pdf pages: 41  slides with rows: 41  match: yes
category: zero_standing   grep(ZERO_STANDING flag): 41  sweep: 41  match: yes
category: fulltext units with no structured row: 17 units (M001-M004 numeric/first sweep, M005-M017 text claims, loop 1) (see MISSING_FROM_STRUCTURED); all other per-slide diffs = printed page-number footers or a token restated twice in fulltext (2015 on p1)
gate_a2: pass  (orphans 0; the 17 MISSING units are logged, not count failures)
=== END COUNT TEST ===
```

## 1. SLIDES (number | title [first fulltext line] | content type | row ID range | row count | types)
| slide | title | content type | IDs | rows | note |
|---|---|---|---|---|---|
| 1 | To, / Date: 28th October 2026 | text+numbers/chart | R001-R013 | 13 | DATE:3 NUMBER:2 ENTITY:7 QUALIFIER:1 |
| 2 | Investor Presentation – Result Update | divider/text/image | R016-R016 | 1 | ENTITY-SUMMARY:1 |
| 3 | Safe Harbor Statement | divider/text/image | R014-R014 | 1 | ENTITY-SUMMARY:1 |
| 4 | Index | divider/text/image | R015-R015 | 1 | ENTITY-SUMMARY:1 |
| 5 | Q2 & H1FY27 Financials | divider/text/image | R017-R017 | 1 | ENTITY-SUMMARY:1 |
| 6 | Q2 & H1FY27 Performance Scorecard | text+numbers/chart | R024-R041 | 18 | NUMBER:16 QUALIFIER:1 DATE:1 |
| 7 | Q2 & H1FY27 Performance Highlights | table/chart (numeric) | R042-R079 | 38 | QUALIFIER:1 NUMBER:36 DATE:1 |
| 8 | Improving Financial Position / Cashflow from Operations | table/chart (numeric) | R080-R104 | 25 | NUMBER:20 QUALIFIER:3 DATE:1 FORWARD:1 |
| 9 | Q2 H1FY27 Operational PAT | table/chart (numeric) | R105-R194 | 90 | NUMBER:88 QUALIFIER:2 |
| 10 | Q2 H1FY27 Consolidated Profit & Loss Statement | table/chart (numeric) | R195-R317 | 123 | NUMBER:122 QUALIFIER:1 |
| 11 | Consolidated Balance Sheet | table/chart (numeric) | R318-R406 | 89 | NUMBER:88 DATE:1 |
| 12 | Consolidated Cash Flow Statement / Sept-26 / Sept-25 | table/chart (numeric) | R407-R438 | 32 | NUMBER:30 DATE:1 QUALIFIER:1 |
| 13 | Q2 FY27 Company & Industry Updates / Key Growth Drivers: Value-Added Products & Export Exp | text+numbers/chart | R439-R454 | 16 | NUMBER:4 ENTITY:5 FORWARD:4 DATE:1 QUALIFIER:2 |
| 14 | Vision & Growth Levers | divider/text/image | R018-R018 | 1 | ENTITY-SUMMARY:1 |
| 15 | Promoters’ Vision – “Skin In The Game” Through Dividend Only Compensation | text | R455-R463 | 9 | ENTITY:5 FORWARD:3 DATE:1 |
| 16 | Sky Gold & Diamonds Ltd: Preferred Partner in Jewelry Excellence | text+numbers/chart | R464-R472 | 9 | NUMBER:1 QUALIFIER:2 ENTITY:3 FORWARD:3 |
| 17 | Performance Track Record / What we have achieved | text+numbers/chart | R473-R500 | 28 | NUMBER:17 ENTITY:3 FORWARD:5 DATE:1 QUALIFIER:2 |
| 18 | Sky Gold’s Growth Blueprint: Strengthening Foundations for Long-Term Value | text+numbers/chart | R501-R517 | 17 | NUMBER:8 DATE:1 FORWARD:3 ENTITY:2 QUALIFIER:3 |
| 19 | Track Record of Capital Allocation and Business Evolution | text | R518-R522 | 5 | FORWARD:2 QUALIFIER:2 ENTITY:1 |
| 20 | Track Record of Successful Acquisitions | text+numbers/chart | R523-R555 | 33 | ENTITY:5 NUMBER:16 DATE:10 QUALIFIER:2 |
| 21 | Sky Gold & Diamonds: Guidance vs Delivery Scorecard | text+numbers/chart | R556-R589 | 34 | NUMBER:19 QUALIFIER:9 FORWARD:3 DATE:1 ENTITY:2 |
| 22 | Drivers of Growth | divider/text/image | R019-R019 | 1 | ENTITY-SUMMARY:1 |
| 23 | Core Pillars for Progress: Robust Growth with Focus on Positive Cash Flows Generation | text+numbers/chart | R590-R603 | 14 | NUMBER:8 DATE:1 QUALIFIER:1 FORWARD:4 |
| 24 | Company Overview | divider/text/image | R020-R020 | 1 | ENTITY-SUMMARY:1 |
| 25 | SKY Gold & Diamonds : Make in Bharat for the World | text | R604-R606 | 3 | ENTITY:1 DATE:2 |
| 26 | Crafted For Tomorrow : Sustainable, Stunning and Smart | text+numbers/chart | R607-R614 | 8 | NUMBER:7 ENTITY-SUMMARY:1 |
| 27 | Key Milestones | text+numbers/chart | R615-R628 | 14 | DATE:6 NUMBER:6 QUALIFIER:1 ENTITY:1 |
| 28 | Management Team | text+numbers/chart | R629-R634 | 6 | ENTITY:3 NUMBER:2 FORWARD:1 |
| 29 | Competitive Advantages | text+numbers/chart | R635-R639 | 5 | NUMBER:3 ENTITY:1 QUALIFIER:1 |
| 30 | Strategic Directions | text | R640-R640 | 1 | FORWARD:1 |
| 31 | Sky Sub-Brands | divider/text/image | R641-R641 | 1 | ENTITY-SUMMARY:1 |
| 32 | IIJS Bharat 2026: Product Launch and Media Highlights | text | R642-R643 | 2 | ENTITY:1 DATE:1 |
| 33 | Recognition & Reach: Prestigious Shows and Accolades | photo/image | R022-R022 | 1 | ENTITY-SUMMARY:1 |
| 34 | Glimpse of our Navi Mumbai Facility | photo/image | R023-R023 | 1 | ENTITY-SUMMARY:1 |
| 35 | Financial Delivery | divider/text/image | R021-R021 | 1 | ENTITY-SUMMARY:1 |
| 36 | Historical Profit & Loss Statement / 31-Mar-26 / 31-Mar-25 / 31-Mar-24 | table/chart (numeric) | R644-R698 | 55 | NUMBER:54 QUALIFIER:1 |
| 37 | Historical Balance Sheet | table/chart (numeric) | R699-R828 | 130 | NUMBER:130 |
| 38 | Historical Cash Flow Statement / Mar-26 / Mar-25 / Mar-24 | table/chart (numeric) | R829-R873 | 45 | NUMBER:45 |
| 39 | Key Financial Highlights / EBITDA / Net Profit | text+numbers/chart | R874-R892 | 19 | NUMBER:18 DATE:1 |
| 40 | Performance Highlights / Return Ratios | table/chart (numeric) | R893-R914 | 22 | NUMBER:20 DATE:1 QUALIFIER:1 |
| 41 | Corporate Office: Plot No. D-222/2 TTC Industrial Area, MIDC Shiravane, | divider/text/image | R915-R915 | 1 | ENTITY-SUMMARY:1 |

Slide IDs are not contiguous by slide in a few cases (R014-R023 summary rows sit at the front); ranges above are min-max, membership is by page field.

## 2. SLIDE NUMBERS (every number incl. chart labels)
ROW_ID | category | A2 flags | cross-ref / note
R003 | NUMBER | - | page 1; line 24
R007 | NUMBER | - | page 1; line 59
R024 | NUMBER | - | page 6; line 105
R025 | NUMBER | - | page 6; line 105
R026 | NUMBER | - | page 6; line 105
R027 | NUMBER | - | page 6; line 105
R028 | NUMBER | - | page 6; line 109
R029 | NUMBER | - | page 6; line 109
R030 | NUMBER | - | page 6; line 109
R031 | NUMBER | - | page 6; line 109
R032 | NUMBER | - | page 6; line 113
R033 | NUMBER | - | page 6; line 113
R034 | NUMBER | - | page 6; line 113
R035 | NUMBER | - | page 6; line 111
R036 | NUMBER | - | page 6; line 117
R037 | NUMBER | - | page 6; line 117
R038 | NUMBER | - | page 6; line 117
R039 | NUMBER | - | page 6; line 115
R043 | NUMBER | - | page 7; line 131
R044 | NUMBER | - | page 7; line 131
R045 | NUMBER | - | page 7; line 131
R046 | NUMBER | - | page 7; line 131
R047 | NUMBER | - | page 7; line 129
R048 | NUMBER | - | page 7; line 129
R049 | NUMBER | - | page 7; line 131
R050 | NUMBER | - | page 7; line 131
R051 | NUMBER | - | page 7; line 131
R052 | NUMBER | - | page 7; line 131
R053 | NUMBER | - | page 7; line 127
R054 | NUMBER | - | page 7; line 127
R055 | NUMBER | - | page 7; line 127
R056 | NUMBER | - | page 7; line 127
R057 | NUMBER | - | page 7; line 129
R058 | NUMBER | - | page 7; line 129
R059 | NUMBER | - | page 7; line 145
R060 | NUMBER | - | page 7; line 145
R061 | NUMBER | - | page 7; line 145
R062 | NUMBER | - | page 7; line 145
R063 | NUMBER | - | page 7; line 141
R064 | NUMBER | - | page 7; line 141
R065 | NUMBER | - | page 7; line 141
R066 | NUMBER | - | page 7; line 141
R067 | NUMBER | - | page 7; line 143
R068 | NUMBER | - | page 7; line 143
R069 | NUMBER | - | page 7; line 145
R070 | NUMBER | - | page 7; line 145
R071 | NUMBER | - | page 7; line 145
R072 | NUMBER | - | page 7; line 145
R073 | NUMBER | - | page 7; line 141
R074 | NUMBER | - | page 7; line 141
R075 | NUMBER | - | page 7; line 141
R076 | NUMBER | - | page 7; line 141
R077 | NUMBER | - | page 7; line 143
R078 | NUMBER | - | page 7; line 143
R080 | NUMBER | - | page 8; line 157
R081 | NUMBER | - | page 8; line 157
R082 | NUMBER | - | page 8; line 157
R083 | NUMBER | - | page 8; line 157
R084 | NUMBER | - | page 8; line 157
R085 | NUMBER | - | page 8; line 157
R086 | NUMBER | - | page 8; line 160
R087 | NUMBER | - | page 8; line 160
R088 | NUMBER | - | page 8; line 160
R089 | NUMBER | - | page 8; line 162
R090 | NUMBER | - | page 8; line 162
R091 | NUMBER | - | page 8; line 162
R092 | NUMBER | - | page 8; line 162
R093 | NUMBER | - | page 8; line 163
R094 | NUMBER | - | page 8; line 163
R095 | NUMBER | - | page 8; line 163
R096 | NUMBER | - | page 8; line 163
R097 | NUMBER | - | page 8; line 173
R098 | NUMBER | - | page 8; line 173
R099 | NUMBER | - | page 8; line 173
R105 | NUMBER | - | page 9; line 189
R106 | NUMBER | - | page 9; line 189
R107 | NUMBER | - | page 9; line 189
R108 | NUMBER | - | page 9; line 189
R109 | NUMBER | - | page 9; line 189
R110 | NUMBER | - | page 9; line 189
R111 | NUMBER | - | page 9; line 189
R112 | NUMBER | - | page 9; line 189
R113 | NUMBER | - | page 9; line 190
R114 | NUMBER | - | page 9; line 190
R115 | NUMBER | - | page 9; line 190
R116 | NUMBER | - | page 9; line 190
R117 | NUMBER | - | page 9; line 190
R118 | NUMBER | - | page 9; line 190
R119 | NUMBER | - | page 9; line 190
R120 | NUMBER | - | page 9; line 190
R121 | NUMBER | - | page 9; line 191
R122 | NUMBER | - | page 9; line 191
R123 | NUMBER | - | page 9; line 191
R124 | NUMBER | - | page 9; line 191
R125 | NUMBER | - | page 9; line 191
R126 | NUMBER | - | page 9; line 191
R127 | NUMBER | - | page 9; line 191
R128 | NUMBER | - | page 9; line 191
R129 | NUMBER | - | page 9; line 192
R130 | NUMBER | - | page 9; line 192
R131 | NUMBER | - | page 9; line 192
R132 | NUMBER | - | page 9; line 192
R133 | NUMBER | - | page 9; line 192
R134 | NUMBER | - | page 9; line 192
R135 | NUMBER | - | page 9; line 192
R136 | NUMBER | - | page 9; line 192
R137 | NUMBER | - | page 9; line 193
R138 | NUMBER | - | page 9; line 193
R139 | NUMBER | - | page 9; line 193
R140 | NUMBER | - | page 9; line 193
R141 | NUMBER | - | page 9; line 193
R142 | NUMBER | - | page 9; line 193
R143 | NUMBER | - | page 9; line 193
R144 | NUMBER | - | page 9; line 193
R145 | NUMBER | - | page 9; line 194
R146 | NUMBER | - | page 9; line 194
R147 | NUMBER | - | page 9; line 194
R148 | NUMBER | - | page 9; line 194
R149 | NUMBER | - | page 9; line 194
R150 | NUMBER | - | page 9; line 194
R151 | NUMBER | - | page 9; line 194
R152 | NUMBER | - | page 9; line 194
R153 | NUMBER | - | page 9; line 195
R154 | NUMBER | - | page 9; line 195
R155 | NUMBER | - | page 9; line 195
R156 | NUMBER | - | page 9; line 195
R157 | NUMBER | - | page 9; line 195
R158 | NUMBER | - | page 9; line 195
R159 | NUMBER | - | page 9; line 195
R160 | NUMBER | - | page 9; line 195
R161 | NUMBER | - | page 9; line 196
R162 | NUMBER | - | page 9; line 196
R163 | NUMBER | - | page 9; line 196
R164 | NUMBER | - | page 9; line 196
R165 | NUMBER | - | page 9; line 196
R166 | NUMBER | - | page 9; line 196
R167 | NUMBER | - | page 9; line 196
R168 | NUMBER | - | page 9; line 196
R169 | NUMBER | - | page 9; line 197
R170 | NUMBER | - | page 9; line 197
R171 | NUMBER | - | page 9; line 197
R172 | NUMBER | - | page 9; line 197
R173 | NUMBER | - | page 9; line 197
R174 | NUMBER | - | page 9; line 197
R175 | NUMBER | - | page 9; line 197
R176 | NUMBER | - | page 9; line 197
R177 | NUMBER | - | page 9; line 198
R178 | NUMBER | - | page 9; line 198
R179 | NUMBER | - | page 9; line 198
R180 | NUMBER | - | page 9; line 198
R181 | NUMBER | - | page 9; line 198
R182 | NUMBER | - | page 9; line 198
R183 | NUMBER | - | page 9; line 198
R184 | NUMBER | - | page 9; line 198
R185 | NUMBER | - | page 9; line 199
R186 | NUMBER | - | page 9; line 199
R187 | NUMBER | - | page 9; line 199
R188 | NUMBER | - | page 9; line 199
R189 | NUMBER | - | page 9; line 199
R190 | NUMBER | - | page 9; line 199
R191 | NUMBER | - | page 9; line 199
R192 | NUMBER | - | page 9; line 199
R195 | NUMBER | - | page 10; line 208
R196 | NUMBER | - | page 10; line 208
R197 | NUMBER | - | page 10; line 208
R198 | NUMBER | - | page 10; line 208
R199 | NUMBER | - | page 10; line 208
R200 | NUMBER | - | page 10; line 208
R201 | NUMBER | - | page 10; line 208
R202 | NUMBER | - | page 10; line 208
R203 | NUMBER | - | page 10; line 210
R204 | NUMBER | - | page 10; line 210
R205 | NUMBER | - | page 10; line 210
R206 | NUMBER | - | page 10; line 210
R207 | NUMBER | - | page 10; line 210
R208 | NUMBER | - | page 10; line 212
R209 | NUMBER | - | page 10; line 212
R210 | NUMBER | - | page 10; line 212
R211 | NUMBER | - | page 10; line 212
R212 | NUMBER | - | page 10; line 212
R213 | NUMBER | - | page 10; line 214
R214 | NUMBER | - | page 10; line 214
R215 | NUMBER | - | page 10; line 214
R216 | NUMBER | - | page 10; line 214
R217 | NUMBER | - | page 10; line 214
R218 | NUMBER | - | page 10; line 215
R219 | NUMBER | - | page 10; line 215
R220 | NUMBER | - | page 10; line 215
R221 | NUMBER | - | page 10; line 215
R222 | NUMBER | - | page 10; line 215
R223 | NUMBER | - | page 10; line 215
R224 | NUMBER | - | page 10; line 215
R225 | NUMBER | - | page 10; line 215
R226 | NUMBER | - | page 10; line 216
R227 | NUMBER | - | page 10; line 216
R228 | NUMBER | - | page 10; line 216
R229 | NUMBER | - | page 10; line 216
R230 | NUMBER | - | page 10; line 216
R231 | NUMBER | - | page 10; line 216
R232 | NUMBER | - | page 10; line 216
R233 | NUMBER | - | page 10; line 216
R234 | NUMBER | - | page 10; line 217
R235 | NUMBER | - | page 10; line 217
R236 | NUMBER | - | page 10; line 217
R237 | NUMBER | - | page 10; line 217
R238 | NUMBER | - | page 10; line 217
R239 | NUMBER | - | page 10; line 218
R240 | NUMBER | - | page 10; line 218
R241 | NUMBER | - | page 10; line 218
R242 | NUMBER | - | page 10; line 218
R243 | NUMBER | - | page 10; line 218
R244 | NUMBER | - | page 10; line 219
R245 | NUMBER | - | page 10; line 219
R246 | NUMBER | - | page 10; line 219
R247 | NUMBER | - | page 10; line 219
R248 | NUMBER | - | page 10; line 219
R249 | NUMBER | - | page 10; line 219
R250 | NUMBER | - | page 10; line 219
R251 | NUMBER | - | page 10; line 219
R252 | NUMBER | - | page 10; line 220
R253 | NUMBER | - | page 10; line 220
R254 | NUMBER | - | page 10; line 220
R255 | NUMBER | - | page 10; line 220
R256 | NUMBER | - | page 10; line 220
R257 | NUMBER | - | page 10; line 220
R258 | NUMBER | - | page 10; line 220
R259 | NUMBER | - | page 10; line 220
R260 | NUMBER | - | page 10; line 221
R261 | NUMBER | - | page 10; line 221
R262 | NUMBER | - | page 10; line 221
R263 | NUMBER | - | page 10; line 221
R264 | NUMBER | - | page 10; line 221
R265 | NUMBER | - | page 10; line 222
R266 | NUMBER | - | page 10; line 222
R267 | NUMBER | - | page 10; line 222
R268 | NUMBER | - | page 10; line 222
R269 | NUMBER | - | page 10; line 222
R270 | NUMBER | - | page 10; line 224
R271 | NUMBER | - | page 10; line 224
R272 | NUMBER | - | page 10; line 224
R273 | NUMBER | - | page 10; line 224
R274 | NUMBER | - | page 10; line 224
R275 | NUMBER | - | page 10; line 224
R276 | NUMBER | - | page 10; line 224
R277 | NUMBER | - | page 10; line 224
R278 | NUMBER | - | page 10; line 225
R279 | NUMBER | - | page 10; line 225
R280 | NUMBER | - | page 10; line 225
R281 | NUMBER | - | page 10; line 225
R282 | NUMBER | - | page 10; line 225
R283 | NUMBER | - | page 10; line 226
R284 | NUMBER | ZERO_STANDING | page 10; line 226
R285 | NUMBER | ZERO_STANDING | page 10; line 226
R286 | NUMBER | - | page 10; line 226
R287 | NUMBER | ZERO_STANDING | page 10; line 226
R288 | NUMBER | - | page 10; line 227
R289 | NUMBER | - | page 10; line 227
R290 | NUMBER | - | page 10; line 227
R291 | NUMBER | - | page 10; line 227
R292 | NUMBER | - | page 10; line 227
R293 | NUMBER | - | page 10; line 227
R294 | NUMBER | - | page 10; line 227
R295 | NUMBER | - | page 10; line 227
R296 | NUMBER | - | page 10; line 228
R297 | NUMBER | - | page 10; line 228
R298 | NUMBER | - | page 10; line 228
R299 | NUMBER | - | page 10; line 228
R300 | NUMBER | - | page 10; line 228
R301 | NUMBER | - | page 10; line 229
R302 | NUMBER | - | page 10; line 229
R303 | NUMBER | - | page 10; line 229
R304 | NUMBER | - | page 10; line 229
R305 | NUMBER | - | page 10; line 229
R306 | NUMBER | - | page 10; line 229
R307 | NUMBER | - | page 10; line 229
R308 | NUMBER | - | page 10; line 229
R309 | NUMBER | - | page 10; line 230
R310 | NUMBER | - | page 10; line 230
R311 | NUMBER | - | page 10; line 230
R312 | NUMBER | - | page 10; line 230
R313 | NUMBER | - | page 10; line 230
R314 | NUMBER | - | page 10; line 230
R315 | NUMBER | - | page 10; line 230
R316 | NUMBER | - | page 10; line 230
R318 | NUMBER | - | page 11; line 238
R319 | NUMBER | - | page 11; line 238
R320 | NUMBER | - | page 11; line 239
R321 | NUMBER | - | page 11; line 239
R322 | NUMBER | ZERO_STANDING | page 11; line 240
R323 | NUMBER | - | page 11; line 240
R324 | NUMBER | - | page 11; line 241
R325 | NUMBER | - | page 11; line 241
R326 | NUMBER | - | page 11; line 242
R327 | NUMBER | - | page 11; line 242
R328 | NUMBER | ZERO_STANDING | page 11; line 244
R329 | NUMBER | - | page 11; line 244
R330 | NUMBER | - | page 11; line 244
R331 | NUMBER | - | page 11; line 244
R332 | NUMBER | - | page 11; line 247
R333 | NUMBER | ZERO_STANDING | page 11; line 247
R334 | NUMBER | - | page 11; line 249
R335 | NUMBER | - | page 11; line 249
R336 | NUMBER | - | page 11; line 249
R337 | NUMBER | - | page 11; line 249
R338 | NUMBER | - | page 11; line 252
R339 | NUMBER | - | page 11; line 252
R340 | NUMBER | ZERO_STANDING | page 11; line 253
R341 | NUMBER | ZERO_STANDING | page 11; line 253
R342 | NUMBER | - | page 11; line 254
R343 | NUMBER | - | page 11; line 254
R344 | NUMBER | - | page 11; line 255
R345 | NUMBER | - | page 11; line 255
R346 | NUMBER | - | page 11; line 257
R347 | NUMBER | - | page 11; line 257
R348 | NUMBER | - | page 11; line 258
R349 | NUMBER | - | page 11; line 258
R350 | NUMBER | - | page 11; line 259
R351 | NUMBER | - | page 11; line 259
R352 | NUMBER | - | page 11; line 260
R353 | NUMBER | ZERO_STANDING | page 11; line 260
R354 | NUMBER | - | page 11; line 260
R355 | NUMBER | - | page 11; line 260
R356 | NUMBER | - | page 11; line 262
R357 | NUMBER | - | page 11; line 262
R358 | NUMBER | - | page 11; line 263
R359 | NUMBER | - | page 11; line 263
R360 | NUMBER | - | page 11; line 264
R361 | NUMBER | - | page 11; line 264
R362 | NUMBER | - | page 11; line 237
R363 | NUMBER | - | page 11; line 237
R364 | NUMBER | - | page 11; line 238
R365 | NUMBER | - | page 11; line 238
R366 | NUMBER | - | page 11; line 239
R367 | NUMBER | - | page 11; line 239
R368 | NUMBER | - | page 11; line 240
R369 | NUMBER | - | page 11; line 240
R370 | NUMBER | - | page 11; line 241
R371 | NUMBER | - | page 11; line 241
R372 | NUMBER | - | page 11; line 244
R373 | NUMBER | - | page 11; line 244
R374 | NUMBER | - | page 11; line 245
R375 | NUMBER | - | page 11; line 245
R376 | NUMBER | ZERO_STANDING | page 11; line 247
R377 | NUMBER | ZERO_STANDING | page 11; line 247
R378 | NUMBER | - | page 11; line 248
R379 | NUMBER | - | page 11; line 248
R380 | NUMBER | ZERO_STANDING | page 11; line 249
R381 | NUMBER | - | page 11; line 249
R382 | NUMBER | - | page 11; line 250
R383 | NUMBER | - | page 11; line 250
R384 | NUMBER | - | page 11; line 252
R385 | NUMBER | - | page 11; line 252
R386 | NUMBER | - | page 11; line 254
R387 | NUMBER | - | page 11; line 254
R388 | NUMBER | ZERO_STANDING | page 11; line 255
R389 | NUMBER | ZERO_STANDING | page 11; line 255
R390 | NUMBER | - | page 11; line 256
R391 | NUMBER | - | page 11; line 256
R392 | NUMBER | - | page 11; line 257
R393 | NUMBER | - | page 11; line 257
R394 | NUMBER | - | page 11; line 258
R395 | NUMBER | - | page 11; line 258
R396 | NUMBER | - | page 11; line 259
R397 | NUMBER | - | page 11; line 259
R398 | NUMBER | - | page 11; line 260
R399 | NUMBER | - | page 11; line 260
R400 | NUMBER | - | page 11; line 261
R401 | NUMBER | - | page 11; line 261
R402 | NUMBER | - | page 11; line 262
R403 | NUMBER | - | page 11; line 262
R404 | NUMBER | - | page 11; line 263
R405 | NUMBER | - | page 11; line 263
R407 | NUMBER | - | page 12; line 268
R408 | NUMBER | - | page 12; line 268
R409 | NUMBER | - | page 12; line 269
R410 | NUMBER | - | page 12; line 269
R411 | NUMBER | - | page 12; line 270
R412 | NUMBER | - | page 12; line 270
R413 | NUMBER | - | page 12; line 271
R414 | NUMBER | - | page 12; line 271
R415 | NUMBER | - | page 12; line 272
R416 | NUMBER | - | page 12; line 272
R417 | NUMBER | - | page 12; line 273
R418 | NUMBER | - | page 12; line 273
R419 | NUMBER | - | page 12; line 274
R420 | NUMBER | - | page 12; line 274
R421 | NUMBER | - | page 12; line 275
R422 | NUMBER | - | page 12; line 275
R423 | NUMBER | - | page 12; line 276
R424 | NUMBER | - | page 12; line 276
R425 | NUMBER | - | page 12; line 277
R426 | NUMBER | - | page 12; line 277
R427 | NUMBER | - | page 12; line 278
R428 | NUMBER | - | page 12; line 278
R429 | NUMBER | ZERO_STANDING | page 12; line 281
R430 | NUMBER | - | page 12; line 281
R431 | NUMBER | - | page 12; line 282
R432 | NUMBER | - | page 12; line 282
R433 | NUMBER | ZERO_STANDING | page 12; line 283
R434 | NUMBER | - | page 12; line 283
R435 | NUMBER | - | page 12; line 284
R436 | NUMBER | - | page 12; line 284
R439 | NUMBER | - | page 13; line 290
R440 | NUMBER | - | page 13; line 290
R441 | NUMBER | - | page 13; line 288
R442 | NUMBER | - | page 13; line 309
R464 | NUMBER | - | page 16; line 352
R473 | NUMBER | - | page 17; line 381
R474 | NUMBER | - | page 17; line 381
R475 | NUMBER | - | page 17; line 381
R476 | NUMBER | - | page 17; line 382
R477 | NUMBER | - | page 17; line 382
R478 | NUMBER | - | page 17; line 383
R479 | NUMBER | - | page 17; line 379
R480 | NUMBER | - | page 17; line 379
R481 | NUMBER | - | page 17; line 379
R482 | NUMBER | - | page 17; line 380
R483 | NUMBER | - | page 17; line 380
R484 | NUMBER | - | page 17; line 384
R485 | NUMBER | - | page 17; line 385
R486 | NUMBER | RESTATED | page 17; line 386; same value also R505
R487 | NUMBER | - | page 17; line 390
R488 | NUMBER | - | page 17; line 391
R489 | NUMBER | - | page 17; line 399
R501 | NUMBER | - | page 18; line 412
R502 | NUMBER | - | page 18; line 412
R503 | NUMBER | - | page 18; line 412
R504 | NUMBER | - | page 18; line 413
R505 | NUMBER | RESTATED | page 18; line 413; same value also R486
R506 | NUMBER | - | page 18; line 414
R507 | NUMBER | - | page 18; line 426
R508 | NUMBER | - | page 18; line 410
R524 | NUMBER | - | page 20; line 464
R526 | NUMBER | - | page 20; line 466
R527 | NUMBER | - | page 20; line 464
R529 | NUMBER | - | page 20; line 466
R531 | NUMBER | - | page 20; line 468
R533 | NUMBER | - | page 20; line 470
R534 | NUMBER | - | page 20; line 468
R536 | NUMBER | - | page 20; line 470
R538 | NUMBER | - | page 20; line 472
R540 | NUMBER | - | page 20; line 474
R541 | NUMBER | - | page 20; line 472
R543 | NUMBER | - | page 20; line 474
R545 | NUMBER | - | page 20; line 477
R547 | NUMBER | - | page 20; line 479
R548 | NUMBER | - | page 20; line 477
R550 | NUMBER | - | page 20; line 479
R556 | NUMBER | - | page 21; line 489
R557 | NUMBER | - | page 21; line 489
R559 | NUMBER | - | page 21; line 490
R560 | NUMBER | - | page 21; line 490
R562 | NUMBER | - | page 21; line 491
R563 | NUMBER | - | page 21; line 491
R565 | NUMBER | - | page 21; line 492
R566 | NUMBER | - | page 21; line 492
R568 | NUMBER | - | page 21; line 493
R569 | NUMBER | - | page 21; line 493
R571 | NUMBER | - | page 21; line 494
R572 | NUMBER | - | page 21; line 494
R574 | NUMBER | - | page 21; line 495
R575 | NUMBER | - | page 21; line 495
R577 | NUMBER | - | page 21; line 490
R578 | NUMBER | - | page 21; line 494
R579 | NUMBER | - | page 21; line 498
R580 | NUMBER | - | page 21; line 486
R584 | NUMBER | ZERO_STANDING | page 21; line 505
R590 | NUMBER | - | page 23; line 531
R591 | NUMBER | - | page 23; line 531
R592 | NUMBER | - | page 23; line 531
R593 | NUMBER | - | page 23; line 527
R594 | NUMBER | - | page 23; line 520
R595 | NUMBER | - | page 23; line 523
R596 | NUMBER | - | page 23; line 521
R597 | NUMBER | - | page 23; line 524
R607 | NUMBER | - | page 26; line 562
R608 | NUMBER | - | page 26; line 562
R609 | NUMBER | - | page 26; line 562
R610 | NUMBER | - | page 26; line 562
R611 | NUMBER | - | page 26; line 562
R612 | NUMBER | - | page 26; line 562
R613 | NUMBER | - | page 26; line 562
R621 | NUMBER | - | page 27; line 590
R622 | NUMBER | - | page 27; line 590
R623 | NUMBER | - | page 27; line 590
R624 | NUMBER | - | page 27; line 590
R625 | NUMBER | - | page 27; line 590
R626 | NUMBER | - | page 27; line 590
R630 | NUMBER | - | page 28; line 609
R631 | NUMBER | - | page 28; line 607
R635 | NUMBER | - | page 29; line 636
R636 | NUMBER | - | page 29; line 636
R637 | NUMBER | - | page 29; line 636
R644 | NUMBER | - | page 36; line 692
R645 | NUMBER | - | page 36; line 692
R646 | NUMBER | - | page 36; line 692
R647 | NUMBER | - | page 36; line 693
R648 | NUMBER | - | page 36; line 693
R649 | NUMBER | - | page 36; line 693
R650 | NUMBER | - | page 36; line 694
R651 | NUMBER | ZERO_STANDING | page 36; line 694
R652 | NUMBER | ZERO_STANDING | page 36; line 694
R653 | NUMBER | - | page 36; line 695
R654 | NUMBER | - | page 36; line 695
R655 | NUMBER | - | page 36; line 695
R656 | NUMBER | - | page 36; line 696
R657 | NUMBER | - | page 36; line 696
R658 | NUMBER | - | page 36; line 696
R659 | NUMBER | - | page 36; line 697
R660 | NUMBER | - | page 36; line 697
R661 | NUMBER | - | page 36; line 697
R662 | NUMBER | - | page 36; line 698
R663 | NUMBER | - | page 36; line 698
R664 | NUMBER | - | page 36; line 698
R665 | NUMBER | - | page 36; line 699
R666 | NUMBER | - | page 36; line 699
R667 | NUMBER | - | page 36; line 699
R668 | NUMBER | - | page 36; line 700
R669 | NUMBER | - | page 36; line 700
R670 | NUMBER | - | page 36; line 700
R671 | NUMBER | - | page 36; line 701
R672 | NUMBER | - | page 36; line 701
R673 | NUMBER | - | page 36; line 701
R674 | NUMBER | - | page 36; line 702
R675 | NUMBER | - | page 36; line 702
R676 | NUMBER | - | page 36; line 702
R677 | NUMBER | - | page 36; line 703
R678 | NUMBER | - | page 36; line 703
R679 | NUMBER | - | page 36; line 703
R680 | NUMBER | - | page 36; line 704
R681 | NUMBER | - | page 36; line 704
R682 | NUMBER | - | page 36; line 704
R683 | NUMBER | - | page 36; line 705
R684 | NUMBER | - | page 36; line 705
R685 | NUMBER | - | page 36; line 705
R686 | NUMBER | - | page 36; line 706
R687 | NUMBER | - | page 36; line 706
R688 | NUMBER | - | page 36; line 706
R689 | NUMBER | - | page 36; line 707
R690 | NUMBER | - | page 36; line 707
R691 | NUMBER | - | page 36; line 707
R692 | NUMBER | - | page 36; line 708
R693 | NUMBER | - | page 36; line 708
R694 | NUMBER | - | page 36; line 708
R695 | NUMBER | - | page 36; line 709
R696 | NUMBER | - | page 36; line 709
R697 | NUMBER | - | page 36; line 709
R699 | NUMBER | - | page 37; line 717
R700 | NUMBER | - | page 37; line 717
R701 | NUMBER | - | page 37; line 717
R702 | NUMBER | ZERO_STANDING | page 37; line 718
R703 | NUMBER | - | page 37; line 718
R704 | NUMBER | - | page 37; line 718
R705 | NUMBER | - | page 37; line 719
R706 | NUMBER | - | page 37; line 719
R707 | NUMBER | - | page 37; line 719
R708 | NUMBER | - | page 37; line 720
R709 | NUMBER | - | page 37; line 720
R710 | NUMBER | ZERO_STANDING | page 37; line 720
R711 | NUMBER | - | page 37; line 721
R712 | NUMBER | - | page 37; line 721
R713 | NUMBER | ZERO_STANDING | page 37; line 721
R714 | NUMBER | - | page 37; line 722
R715 | NUMBER | - | page 37; line 722
R716 | NUMBER | - | page 37; line 722
R717 | NUMBER | - | page 37; line 724
R718 | NUMBER | - | page 37; line 724
R719 | NUMBER | - | page 37; line 724
R720 | NUMBER | - | page 37; line 725
R721 | NUMBER | - | page 37; line 725
R722 | NUMBER | - | page 37; line 725
R723 | NUMBER | - | page 37; line 726
R724 | NUMBER | - | page 37; line 726
R725 | NUMBER | - | page 37; line 726
R726 | NUMBER | - | page 37; line 727
R727 | NUMBER | - | page 37; line 727
R728 | NUMBER | - | page 37; line 727
R729 | NUMBER | - | page 37; line 729
R730 | NUMBER | - | page 37; line 729
R731 | NUMBER | - | page 37; line 729
R732 | NUMBER | ZERO_STANDING | page 37; line 731
R733 | NUMBER | ZERO_STANDING | page 37; line 731
R734 | NUMBER | ZERO_STANDING | page 37; line 731
R735 | NUMBER | - | page 37; line 732
R736 | NUMBER | - | page 37; line 732
R737 | NUMBER | - | page 37; line 732
R738 | NUMBER | - | page 37; line 733
R739 | NUMBER | - | page 37; line 733
R740 | NUMBER | - | page 37; line 733
R741 | NUMBER | - | page 37; line 734
R742 | NUMBER | - | page 37; line 734
R743 | NUMBER | - | page 37; line 734
R744 | NUMBER | - | page 37; line 736
R745 | NUMBER | - | page 37; line 736
R746 | NUMBER | - | page 37; line 736
R747 | NUMBER | - | page 37; line 737
R748 | NUMBER | - | page 37; line 737
R749 | NUMBER | - | page 37; line 737
R750 | NUMBER | ZERO_STANDING | page 37; line 738
R751 | NUMBER | ZERO_STANDING | page 37; line 738
R752 | NUMBER | ZERO_STANDING | page 37; line 738
R753 | NUMBER | - | page 37; line 739
R754 | NUMBER | - | page 37; line 739
R755 | NUMBER | - | page 37; line 739
R756 | NUMBER | - | page 37; line 740
R757 | NUMBER | - | page 37; line 740
R758 | NUMBER | - | page 37; line 740
R759 | NUMBER | - | page 37; line 741
R760 | NUMBER | ZERO_STANDING | page 37; line 741
R761 | NUMBER | ZERO_STANDING | page 37; line 741
R762 | NUMBER | - | page 37; line 742
R763 | NUMBER | - | page 37; line 742
R764 | NUMBER | - | page 37; line 742
R765 | NUMBER | - | page 37; line 717
R766 | NUMBER | - | page 37; line 717
R767 | NUMBER | - | page 37; line 717
R768 | NUMBER | - | page 37; line 717
R769 | NUMBER | - | page 37; line 717
R770 | NUMBER | - | page 37; line 717
R771 | NUMBER | - | page 37; line 719
R772 | NUMBER | - | page 37; line 719
R773 | NUMBER | - | page 37; line 719
R774 | NUMBER | - | page 37; line 720
R775 | NUMBER | ZERO_STANDING | page 37; line 720
R776 | NUMBER | ZERO_STANDING | page 37; line 720
R777 | NUMBER | - | page 37; line 721
R778 | NUMBER | - | page 37; line 721
R779 | NUMBER | - | page 37; line 721
R780 | NUMBER | - | page 37; line 725
R781 | NUMBER | - | page 37; line 725
R782 | NUMBER | - | page 37; line 725
R783 | NUMBER | - | page 37; line 725
R784 | NUMBER | - | page 37; line 725
R785 | NUMBER | - | page 37; line 725
R786 | NUMBER | ZERO_STANDING | page 37; line 726
R787 | NUMBER | ZERO_STANDING | page 37; line 726
R788 | NUMBER | ZERO_STANDING | page 37; line 726
R789 | NUMBER | - | page 37; line 728
R790 | NUMBER | - | page 37; line 728
R791 | NUMBER | - | page 37; line 728
R792 | NUMBER | - | page 37; line 729
R793 | NUMBER | - | page 37; line 729
R794 | NUMBER | - | page 37; line 729
R795 | NUMBER | - | page 37; line 730
R796 | NUMBER | - | page 37; line 730
R797 | NUMBER | - | page 37; line 730
R798 | NUMBER | - | page 37; line 732
R799 | NUMBER | - | page 37; line 732
R800 | NUMBER | - | page 37; line 732
R801 | NUMBER | - | page 37; line 732
R802 | NUMBER | - | page 37; line 732
R803 | NUMBER | - | page 37; line 732
R804 | NUMBER | ZERO_STANDING | page 37; line 733
R805 | NUMBER | - | page 37; line 734
R806 | NUMBER | - | page 37; line 734
R807 | NUMBER | - | page 37; line 734
R808 | NUMBER | - | page 37; line 735
R809 | NUMBER | - | page 37; line 735
R810 | NUMBER | - | page 37; line 735
R811 | NUMBER | - | page 37; line 738
R812 | NUMBER | - | page 37; line 738
R813 | NUMBER | - | page 37; line 738
R814 | NUMBER | - | page 37; line 739
R815 | NUMBER | - | page 37; line 739
R816 | NUMBER | - | page 37; line 739
R817 | NUMBER | - | page 37; line 740
R818 | NUMBER | - | page 37; line 740
R819 | NUMBER | - | page 37; line 740
R820 | NUMBER | - | page 37; line 741
R821 | NUMBER | - | page 37; line 741
R822 | NUMBER | - | page 37; line 741
R823 | NUMBER | - | page 37; line 742
R824 | NUMBER | - | page 37; line 742
R825 | NUMBER | - | page 37; line 742
R826 | NUMBER | - | page 37; line 743
R827 | NUMBER | - | page 37; line 743
R828 | NUMBER | - | page 37; line 743
R829 | NUMBER | - | page 38; line 747
R830 | NUMBER | - | page 38; line 747
R831 | NUMBER | - | page 38; line 747
R832 | NUMBER | - | page 38; line 748
R833 | NUMBER | - | page 38; line 748
R834 | NUMBER | - | page 38; line 748
R835 | NUMBER | - | page 38; line 749
R836 | NUMBER | - | page 38; line 749
R837 | NUMBER | - | page 38; line 749
R838 | NUMBER | - | page 38; line 750
R839 | NUMBER | - | page 38; line 750
R840 | NUMBER | - | page 38; line 750
R841 | NUMBER | - | page 38; line 751
R842 | NUMBER | - | page 38; line 751
R843 | NUMBER | - | page 38; line 751
R844 | NUMBER | - | page 38; line 752
R845 | NUMBER | - | page 38; line 752
R846 | NUMBER | - | page 38; line 752
R847 | NUMBER | - | page 38; line 753
R848 | NUMBER | - | page 38; line 753
R849 | NUMBER | - | page 38; line 753
R850 | NUMBER | - | page 38; line 754
R851 | NUMBER | - | page 38; line 754
R852 | NUMBER | - | page 38; line 754
R853 | NUMBER | - | page 38; line 755
R854 | NUMBER | - | page 38; line 755
R855 | NUMBER | - | page 38; line 755
R856 | NUMBER | - | page 38; line 756
R857 | NUMBER | - | page 38; line 756
R858 | NUMBER | - | page 38; line 756
R859 | NUMBER | - | page 38; line 757
R860 | NUMBER | - | page 38; line 757
R861 | NUMBER | - | page 38; line 757
R862 | NUMBER | - | page 38; line 758
R863 | NUMBER | - | page 38; line 758
R864 | NUMBER | ZERO_STANDING | page 38; line 758
R865 | NUMBER | - | page 38; line 759
R866 | NUMBER | ZERO_STANDING | page 38; line 759
R867 | NUMBER | ZERO_STANDING | page 38; line 759
R868 | NUMBER | - | page 38; line 760
R869 | NUMBER | ZERO_STANDING | page 38; line 760
R870 | NUMBER | ZERO_STANDING | page 38; line 760
R871 | NUMBER | - | page 38; line 761
R872 | NUMBER | - | page 38; line 761
R873 | NUMBER | - | page 38; line 761
R874 | NUMBER | - | page 39; line 775
R875 | NUMBER | - | page 39; line 775
R876 | NUMBER | - | page 39; line 775
R877 | NUMBER | - | page 39; line 775
R878 | NUMBER | - | page 39; line 775
R879 | NUMBER | - | page 39; line 775
R880 | NUMBER | - | page 39; line 775
R881 | NUMBER | - | page 39; line 775
R882 | NUMBER | - | page 39; line 775
R883 | NUMBER | - | page 39; line 775
R884 | NUMBER | - | page 39; line 774
R885 | NUMBER | - | page 39; line 774
R886 | NUMBER | - | page 39; line 774
R887 | NUMBER | - | page 39; line 774
R888 | NUMBER | - | page 39; line 774
R889 | NUMBER | - | page 39; line 768
R890 | NUMBER | - | page 39; line 766
R891 | NUMBER | - | page 39; line 766
R893 | NUMBER | - | page 40; line 786
R894 | NUMBER | - | page 40; line 786
R895 | NUMBER | - | page 40; line 786
R896 | NUMBER | - | page 40; line 786
R897 | NUMBER | - | page 40; line 786
R898 | NUMBER | - | page 40; line 786
R899 | NUMBER | - | page 40; line 786
R900 | NUMBER | - | page 40; line 786
R901 | NUMBER | - | page 40; line 799
R902 | NUMBER | - | page 40; line 799
R903 | NUMBER | - | page 40; line 799
R904 | NUMBER | - | page 40; line 799
R905 | NUMBER | - | page 40; line 805
R906 | NUMBER | - | page 40; line 805
R907 | NUMBER | - | page 40; line 805
R908 | NUMBER | - | page 40; line 805
R909 | NUMBER | - | page 40; line 810
R910 | NUMBER | - | page 40; line 810
R911 | NUMBER | - | page 40; line 810
R912 | NUMBER | - | page 40; line 810
(count 760)

## 3. DATES / PERIODS
ROW_ID | category | A2 flags | cross-ref / note
R001 | DATE | - | page 1; line 18
R002 | DATE | - | page 1; line 35
R010 | DATE | - | page 1; line 54
R041 | DATE | - | page 6; line 103
R079 | DATE | - | page 7; line 137
R103 | DATE | - | page 8; line 162
R406 | DATE | - | page 11; line 235
R437 | DATE | - | page 12; line 266
R452 | DATE | - | page 13; line 303
R459 | DATE | - | page 15; line 327
R498 | DATE | - | page 17; line 377
R509 | DATE | - | page 18; line 412
R525 | DATE | - | page 20; line 464
R528 | DATE | - | page 20; line 464
R532 | DATE | - | page 20; line 468
R535 | DATE | - | page 20; line 468
R539 | DATE | - | page 20; line 472
R542 | DATE | - | page 20; line 472
R546 | DATE | - | page 20; line 477
R549 | DATE | - | page 20; line 477
R551 | DATE | - | page 20; line 475
R552 | DATE | - | page 20; line 480
R585 | DATE | - | page 21; line 502
R598 | DATE | - | page 23; line 535
R605 | DATE | - | page 25; line 547
R606 | DATE | - | page 25; line 545
R615 | DATE | - | page 27; line 586
R616 | DATE | - | page 27; line 586
R617 | DATE | - | page 27; line 586
R618 | DATE | - | page 27; line 586
R619 | DATE | - | page 27; line 586
R620 | DATE | - | page 27; line 586
R643 | DATE | - | page 32; line 675
R892 | DATE | - | page 39; line 777
R913 | DATE | - | page 40; line 816
(count 35)

## 4. FORWARD-LOOKING / COMMITMENT STATEMENTS
ROW_ID | category | A2 flags | cross-ref / note
R104 | FORWARD | NOT_FORWARD | page 8; line 154
R448 | FORWARD | - | page 13; line 293
R449 | FORWARD | - | page 13; line 310
R450 | FORWARD | - | page 13; line 307
R451 | FORWARD | - | page 13; line 294
R458 | FORWARD | - | page 15; line 327
R460 | FORWARD | - | page 15; line 321
R462 | FORWARD | - | page 15; line 336
R469 | FORWARD | - | page 16; line 362
R470 | FORWARD | - | page 16; line 371
R471 | FORWARD | - | page 16; line 359
R493 | FORWARD | - | page 17; line 390
R494 | FORWARD | - | page 17; line 387
R495 | FORWARD | - | page 17; line 401
R496 | FORWARD | - | page 17; line 398
R497 | FORWARD | - | page 17; line 402
R510 | FORWARD | - | page 18; line 412
R511 | FORWARD | - | page 18; line 421
R512 | FORWARD | - | page 18; line 427
R518 | FORWARD | - | page 19; line 433
R522 | FORWARD | - | page 19; line 445
R581 | FORWARD | - | page 21; line 486
R582 | FORWARD | - | page 21; line 502
R583 | FORWARD | - | page 21; line 504
R600 | FORWARD | - | page 23; line 515
R601 | FORWARD | - | page 23; line 522
R602 | FORWARD | - | page 23; line 529
R603 | FORWARD | - | page 23; line 535
R634 | FORWARD | - | page 28; line 610
R640 | FORWARD | - | page 30; line 649
(count 30)

## 5. ENTITIES (incl. divider, image, disclaimer, contact summaries)
ROW_ID | category | A2 flags | cross-ref / note
R004 | ENTITY | - | page 1; line 26
R005 | ENTITY | - | page 1; line 21
R006 | ENTITY | - | page 1; line 57
R008 | ENTITY | - | page 1; line 49
R009 | ENTITY | - | page 1; line 40
R012 | ENTITY | - | page 1; line 28
R013 | ENTITY | - | page 1; line 60
R014 | ENTITY-SUMMARY | - | page 3; line 67
R015 | ENTITY-SUMMARY | - | page 4; line 91
R016 | ENTITY-SUMMARY | - | page 2; line 63
R017 | ENTITY-SUMMARY | - | page 5; line 99
R018 | ENTITY-SUMMARY | - | page 14; line 313
R019 | ENTITY-SUMMARY | - | page 22; line 509
R020 | ENTITY-SUMMARY | - | page 24; line 540
R021 | ENTITY-SUMMARY | - | page 35; line 689
R022 | ENTITY-SUMMARY | - | page 33; line 681
R023 | ENTITY-SUMMARY | - | page 34; line 685
R443 | ENTITY | - | page 13; line 290
R444 | ENTITY | - | page 13; line 299
R445 | ENTITY | - | page 13; line 300
R446 | ENTITY | - | page 13; line 294
R447 | ENTITY | - | page 13; line 293
R455 | ENTITY | - | page 15; line 321
R456 | ENTITY | - | page 15; line 327
R457 | ENTITY | - | page 15; line 336
R461 | ENTITY | - | page 15; line 332
R463 | ENTITY | - | page 15; line 321
R466 | ENTITY | - | page 16; line 355
R467 | ENTITY | - | page 16; line 365
R468 | ENTITY | - | page 16; line 371
R490 | ENTITY | - | page 17; line 395
R491 | ENTITY | - | page 17; line 400
R492 | ENTITY | - | page 17; line 401
R513 | ENTITY | - | page 18; line 418
R514 | ENTITY | - | page 18; line 411
R521 | ENTITY | - | page 19; line 442
R523 | ENTITY | - | page 20; line 464
R530 | ENTITY | - | page 20; line 468
R537 | ENTITY | - | page 20; line 472
R544 | ENTITY | - | page 20; line 477
R555 | ENTITY | - | page 20; line 462
R586 | ENTITY | - | page 21; line 500
R587 | ENTITY | - | page 21; line 502
R604 | ENTITY | - | page 25; line 549
R614 | ENTITY-SUMMARY | - | page 26; line 570
R628 | ENTITY | - | page 27; line 590
R629 | ENTITY | - | page 28; line 605
R632 | ENTITY | - | page 28; line 613
R633 | ENTITY | - | page 28; line 621
R638 | ENTITY | - | page 29; line 638
R641 | ENTITY-SUMMARY | - | page 31; line 668
R642 | ENTITY | - | page 32; line 677
R915 | ENTITY-SUMMARY | - | page 41; line 822
(count 53)

## 6. FOOTNOTES, FINE PRINT AND QUALIFIERS
ROW_ID | category | A2 flags | cross-ref / note
R011 | QUALIFIER | - | page 1; line 30
R040 | QUALIFIER | - | page 6; line 119
R042 | QUALIFIER | - | page 7; line 123
R100 | QUALIFIER | - | page 8; line 180
R101 | QUALIFIER | - | page 8; line 184
R102 | QUALIFIER | - | page 8; line 182
R193 | QUALIFIER | - | page 9; line 202
R194 | QUALIFIER | - | page 9; line 188
R317 | QUALIFIER | - | page 10; line 204
R438 | QUALIFIER | - | page 12; line 266
R453 | QUALIFIER | - | page 13; line 288
R454 | QUALIFIER | - | page 13; line 291
R465 | QUALIFIER | - | page 16; line 351
R472 | QUALIFIER | - | page 16; line 355
R499 | QUALIFIER | - | page 17; line 379
R500 | QUALIFIER | - | page 17; line 381
R515 | QUALIFIER | - | page 18; line 426
R516 | QUALIFIER | - | page 18; line 414
R517 | QUALIFIER | - | page 18; line 412
R519 | QUALIFIER | - | page 19; line 449
R520 | QUALIFIER | - | page 19; line 453
R553 | QUALIFIER | - | page 20; line 472
R554 | QUALIFIER | - | page 20; line 477
R558 | QUALIFIER | - | page 21; line 489
R561 | QUALIFIER | - | page 21; line 490
R564 | QUALIFIER | - | page 21; line 491
R567 | QUALIFIER | - | page 21; line 492
R570 | QUALIFIER | - | page 21; line 493
R573 | QUALIFIER | - | page 21; line 494
R576 | QUALIFIER | - | page 21; line 495
R588 | QUALIFIER | - | page 21; line 493
R589 | QUALIFIER | - | page 21; line 507
R599 | QUALIFIER | - | page 23; line 538
R627 | QUALIFIER | - | page 27; line 588
R639 | QUALIFIER | - | page 29; line 633
R698 | QUALIFIER | - | page 36; line 691
R914 | QUALIFIER | - | page 40; line 814
(count 37)

## 7. ZERO_STANDING (subset of section 2, listed again)
R284, R285, R287, R322, R328, R333, R340, R341, R353, R376, R377, R380, R388, R389, R429, R433, R584, R651, R652, R702, R710, R713, R732, R733, R734, R750, R751, R752, R760, R761, R775, R776, R786, R787, R788, R804, R864, R866, R867, R869, R870  (count 41)

## 8. MISSING_FROM_STRUCTURED (fulltext units with no structured row; loop back to A1, low materiality)
ROW_ID | category | flags | claim text (fulltext line)
M001 | ENTITY/address | MISSING_FROM_STRUCTURED | line 22: BSE addressee address pin code 'Mumbai 400001'
M002 | ENTITY/address | MISSING_FROM_STRUCTURED | line 24: NSE addressee address 'Exchange Plaza, Plot No. C/1, G Block, ... Mumbai 400051'
M003 | NUMBER/chart axis | MISSING_FROM_STRUCTURED | lines 160-175 (page 8 CFO chart): y-axis scale ticks 250,200,150,100,50,0,-50,-100,-150,-200 (decorative scale, no data)
M004 | TEXT/claim | MISSING_FROM_STRUCTURED | line 396 (page 17): 'Presence in light-weight jewellery, with dominance in 22kt and ...' (product-mix claim; R496 covers only the shift to lower-kt, so the 22kt dominance claim has no row)

(correction loop 1: M005-M017 added after the A5 audit and a second whole-fulltext text-claim sweep; M005-M010 are the six A5 units, M011-M017 are further units found)
M005 | TEXT/claim p16 | MISSING_FROM_STRUCTURED | lines 368-369: 'Product Superiority & Agility: ... specialize in light-weight and superior finish jewelry within a highly compressed manufacturing cycle ... directly increases the customer's willingness to pay' (pricing-power claim; R468-R470 cover ERP, value-added share and recognition only). Materiality: medium, pricing-power evidence is unquantified.
M006 | TEXT/claim p17 | MISSING_FROM_STRUCTURED | line 384: 'Promoter-led operations with early steps toward professionalisation and governance strengthening' (FY23 baseline descriptor, continues line 386). Materiality: low-medium, governance baseline used against later governance claims.
M007 | TEXT/claim p17 | MISSING_FROM_STRUCTURED | lines 393-394: 'Portfolio strengthened through strategic acquisitions, expanding TAM and product depth' (growth lever). Materiality: medium, acquisition-led TAM claim, unquantified.
M008 | TEXT/claim p17 | MISSING_FROM_STRUCTURED | lines 396-397: 'Board of Directors reinforced with industry veterans, alongside key leadership hires across domains' (R497 covers only 'strengthening of Board'). Related: M004 (22kt dominance, line 396). Materiality: low-medium, governance claim.
M009 | TEXT/claim p19 | MISSING_FROM_STRUCTURED | lines 433-435: 'Indian jewellery industry continues to witness an increasing presence of organised manufacturers ... favourable backdrop for companies with established capabilities, scale and customer relationships' (industry tailwind claim; R518 covers only the first sentence). Materiality: medium, unquantified market-structure claim.
M010 | TEXT/claim p19 | MISSING_FROM_STRUCTURED | lines 446-447 and 455-456: 'asset-light advance gold model has helped minimize working capital intensity'; 'contributed to positive operating cash flow generation and healthy returns on invested capital' (R522 covers returns above cost of capital only). Materiality: medium-high, the cash-conversion claim has no number on the slide.
M011 | TEXT/claim p13 | MISSING_FROM_STRUCTURED | lines 296-297: Purvi Gems acquisition 'Provides access to an established business, customer relationships, manufacturing capabilities and an experienced team'. Materiality: low-medium (R448 covers the export benefit only).
M012 | TEXT/claim p13 | MISSING_FROM_STRUCTURED | lines 305-306: new internal auditor 'brings expertise in risk-based internal audits, process improvement, compliance reviews, and data-driven control assessments'. Materiality: low.
M013 | TEXT/claim p16 | MISSING_FROM_STRUCTURED | line 347: 'differentiates itself through technological innovation, creative scalability and light weight fine jewelery products' (slide thesis statement). Materiality: low.
M014 | TEXT/claim p16 | MISSING_FROM_STRUCTURED | lines 351-353: 'design engine has evolved into a significant competitive moat'; multigenerational team balances senior expertise with junior designers' local market insight (R465 holds only the ~180 count). Materiality: medium, moat claim.
M015 | TEXT/claim p18 | MISSING_FROM_STRUCTURED | line 413: 'execution has exceeded expectations, and we have progressively upgraded our guidance' (R509-R510 hold the original guidance only). Materiality: medium, links to the p21 guidance-vs-delivery scorecard.
M016 | TEXT/claim p18 | MISSING_FROM_STRUCTURED | lines 418-419: advance gold model 'eliminates inventory risk, reduces capital intensity, and enables high-volume scalability' (R513 holds the model description only). Materiality: medium.
M017 | TEXT/claim p28 | MISSING_FROM_STRUCTURED | lines 615-618: Mahendra Chauhan bio detail: investment in plant and machinery 'elevated operational efficiency', advanced automation and modernised design capability (R632 holds role only). Materiality: low.

## 9. DROPPED_SLIDE
No prior ledger. Not tested. Zero rows flagged.

## 10. ID ACCOUNTABILITY
Sections 2-6 reference every structured ID exactly once by TYPE (760+35+30+53+37 = 915). Zero orphans.
