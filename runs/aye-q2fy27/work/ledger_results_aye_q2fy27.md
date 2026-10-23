# LEDGER results AYE Q2 FY27 (A2)

Correction loop 1 (A5 COV-1..COV-4): added M06 (fulltext line 980, auditor security-cover report signature 11:09:12) and M07 (line 1438, CS cover-letter signature 11:39:14), both MISSING_FROM_STRUCTURED. Corrected the signature-timing statement: M06 at 11:09:12 precedes the 11:15 board start (fulltext line 43) and the 11:21 approval. Missing-from-structured count now 7. Structured IDs unchanged (755).

=== A2 COUNT TEST ===
category: notes (numbered)                                           grep_count: 12   sweep_count: 12   match: yes
category: notes_unnumbered (*, Note:, Notes:)                        grep_count: 4   sweep_count: 4   match: yes
category: line_items (fin tables pp4-7)                              grep_count: 328   sweep_count: 328   match: yes
category: zero_standing                                              grep_count: 30   sweep_count: 30   match: yes
category: agenda_items (considered/approved + other agenda items)    grep_count: 2   sweep_count: 2   match: yes
category: entities                                                   grep_count: 43   sweep_count: 43   match: yes
category: annexure_footnotes (pp16,18)                               grep_count: 7   sweep_count: 7   match: yes
category: structured_total_rows                                      grep_count: 755   sweep_count: 755   match: yes
gate_a2: pass
=== END COUNT TEST ===

Notes: fulltext lines 479-626 give 12 numbered notes. Unnumbered: fulltext lines 342, 449, 525, 681 = R704, R708, R715, R737.
Agenda: 1 explicit item (results approved, LRR noted) plus 1 unspecified ("other agenda items", fulltext line 46). No AR, AGM, dividend, director, ESOP-grant item stated in this letter.
Auditor paras: limited review conclusion unmodified (R695,R697,R699); Emphasis/Other Matters = Trust unreviewed (R696) and predecessor auditor (R698); no Going Concern language in structured; UDINs R013, R412; security cover report conclusion qualified "except for paragraph 12" (R739,R740).
Prior-quarter ledger NOT AVAILABLE: ENTITY_CHANGE flags rest on in-document auditor-change evidence only; no consolidation list diff possible.

ids_in_structured: 755 | ids_referenced_in_ledger: 755 | orphan_ids: [] | match: yes

## MISSING_FROM_STRUCTURED (digital signature blocks, fulltext lines)
M01 | line 69 | signature | letter digital signature timestamp 21-10-2026 11:36:53 +05:30 | MISSING_FROM_STRUCTURED
M02 | line 267 | signature | results statement digital signature, DIN 03337545 (R573), 21-10-2026 11:21:52 +05:30; same minute as approval 11:21 (R004) | MISSING_FROM_STRUCTURED
M03 | line 183 | signature | auditor LRR digital signature Ajit Burli (R579), 2026.10.21 11:24:32 +05:30 | MISSING_FROM_STRUCTURED
M04 | line 465 | signature | notes page signature, DIN 03337545, 21-10-2026 11:22:37 +05:30 | MISSING_FROM_STRUCTURED
M05 | line 746 | signature | security cover / Reg 52(7) pages signature 21-10-2026 11:38:21 +05:30 | MISSING_FROM_STRUCTURED
M06 | line 980 | signature | auditor security-cover report digital signature Ajit Burli (R579), 2026.10.21 11:09:12 +05'30; precedes board start 11:15 (R003) and approval 11:21 (R004) | MISSING_FROM_STRUCTURED, SIGNATURE_BEFORE_MEETING
M07 | line 1438 | signature | company secretary cover-letter digital signature Anuj Jain, 21-10-2026 11:39:14 +05:30 | MISSING_FROM_STRUCTURED
One signature timestamp precedes the board start: M06 (auditor security-cover report, 11:09:12) is 6 minutes before the 11:15 start (fulltext line 43) and 12 minutes before the 11:21 approval. The other signatures (M01-M05, M07) fall at or after 11:21. Letter signed 11:36:53 while meeting still continuing.

## Board outcome letter (p1) (7)
ROW_ID | category | A2 flags | cross-ref / note
R001 | agenda_items | - | RESTATED R619
R002 | agenda_items | - | RESTATED R407
R003 | agenda_items | SHORT_MEETING | meeting start 11:15; with R004 = 6 min to results approval; see M02-M06
R004 | agenda_items | SHORT_MEETING | results approved 11:21; see R003, R622
R005 | agenda_items | - | -
R694 | agenda_items | - | -
R755 | agenda_items | - | -

## Financial table line items (BS p4, P&L p5, CF pp6-7) (328)
ROW_ID | category | A2 flags | cross-ref / note
R014 | line_items | - | -
R015 | line_items | - | -
R016 | line_items | - | -
R017 | line_items | - | -
R018 | line_items | - | -
R019 | line_items | - | -
R020 | line_items | - | -
R021 | line_items | - | -
R022 | line_items | - | -
R023 | line_items | - | -
R024 | line_items | - | -
R025 | line_items | - | -
R026 | line_items | - | -
R027 | line_items | - | -
R028 | line_items | - | -
R029 | line_items | - | -
R030 | line_items | - | -
R031 | line_items | - | -
R032 | line_items | - | RESTATED R414,R469 (PPE annexure col H)
R033 | line_items | - | -
R034 | line_items | - | -
R035 | line_items | - | -
R036 | line_items | - | -
R037 | line_items | ZERO_STANDING | -
R038 | line_items | - | -
R039 | line_items | - | -
R040 | line_items | - | -
R041 | line_items | - | -
R042 | line_items | - | -
R043 | line_items | - | -
R044 | line_items | - | -
R045 | line_items | - | -
R046 | line_items | - | -
R047 | line_items | - | -
R048 | line_items | - | -
R049 | line_items | - | -
R050 | line_items | - | -
R051 | line_items | - | -
R052 | line_items | - | -
R053 | line_items | - | -
R054 | line_items | - | -
R055 | line_items | - | -
R056 | line_items | - | -
R057 | line_items | - | -
R058 | line_items | - | -
R059 | line_items | - | -
R060 | line_items | - | -
R061 | line_items | - | -
R062 | line_items | - | -
R063 | line_items | - | -
R064 | line_items | - | -
R065 | line_items | - | -
R066 | line_items | - | -
R067 | line_items | - | -
R068 | line_items | - | -
R069 | line_items | - | -
R070 | line_items | - | -
R071 | line_items | - | -
R072 | line_items | - | -
R073 | line_items | - | -
R074 | line_items | - | -
R075 | line_items | - | -
R076 | line_items | - | -
R077 | line_items | - | -
R078 | line_items | - | -
R079 | line_items | - | -
R080 | line_items | - | -
R081 | line_items | - | -
R082 | line_items | - | -
R083 | line_items | - | -
R084 | line_items | - | -
R085 | line_items | - | -
R086 | line_items | - | -
R087 | line_items | - | -
R088 | line_items | - | -
R089 | line_items | CELL_BLANK_IN_TEXT | -
R090 | line_items | - | -
R091 | line_items | - | -
R092 | line_items | - | -
R093 | line_items | - | -
R094 | line_items | - | -
R095 | line_items | - | -
R096 | line_items | - | -
R097 | line_items | - | -
R098 | line_items | - | -
R099 | line_items | - | -
R100 | line_items | - | -
R101 | line_items | - | -
R102 | line_items | - | -
R103 | line_items | - | -
R104 | line_items | - | -
R105 | line_items | - | -
R106 | line_items | - | -
R107 | line_items | - | -
R108 | line_items | - | -
R109 | line_items | - | -
R110 | line_items | - | -
R111 | line_items | - | -
R112 | line_items | - | -
R113 | line_items | - | -
R114 | line_items | - | -
R115 | line_items | - | -
R116 | line_items | - | -
R117 | line_items | - | -
R118 | line_items | - | -
R119 | line_items | - | -
R120 | line_items | ZERO_STANDING | -
R121 | line_items | ZERO_STANDING | -
R122 | line_items | - | -
R123 | line_items | ZERO_STANDING | -
R124 | line_items | - | -
R125 | line_items | - | -
R126 | line_items | - | -
R127 | line_items | - | -
R128 | line_items | - | -
R129 | line_items | - | -
R130 | line_items | - | -
R131 | line_items | - | -
R132 | line_items | - | -
R133 | line_items | - | -
R134 | line_items | - | -
R135 | line_items | - | -
R136 | line_items | - | -
R137 | line_items | - | -
R138 | line_items | - | -
R139 | line_items | - | -
R140 | line_items | - | -
R141 | line_items | - | -
R142 | line_items | - | -
R143 | line_items | - | -
R144 | line_items | - | -
R145 | line_items | - | -
R146 | line_items | - | -
R147 | line_items | - | -
R148 | line_items | - | -
R149 | line_items | - | -
R150 | line_items | - | -
R151 | line_items | - | -
R152 | line_items | - | -
R153 | line_items | - | -
R154 | line_items | - | -
R155 | line_items | - | -
R156 | line_items | - | -
R157 | line_items | - | -
R158 | line_items | - | -
R159 | line_items | - | -
R160 | line_items | - | -
R161 | line_items | - | -
R162 | line_items | - | -
R163 | line_items | - | -
R164 | line_items | - | -
R165 | line_items | - | -
R166 | line_items | - | -
R167 | line_items | - | -
R168 | line_items | - | -
R169 | line_items | - | -
R170 | line_items | - | -
R171 | line_items | - | -
R172 | line_items | - | -
R173 | line_items | - | -
R174 | line_items | - | -
R175 | line_items | - | -
R176 | line_items | - | -
R177 | line_items | - | -
R178 | line_items | - | -
R179 | line_items | - | -
R180 | line_items | - | -
R181 | line_items | - | -
R182 | line_items | - | -
R183 | line_items | - | -
R184 | line_items | - | -
R185 | line_items | - | -
R186 | line_items | - | -
R187 | line_items | - | -
R188 | line_items | - | -
R189 | line_items | - | -
R190 | line_items | - | -
R191 | line_items | - | -
R192 | line_items | - | -
R193 | line_items | - | -
R194 | line_items | - | -
R195 | line_items | - | -
R196 | line_items | - | -
R197 | line_items | - | -
R198 | line_items | - | -
R199 | line_items | - | -
R200 | line_items | ZERO_STANDING | -
R201 | line_items | - | -
R202 | line_items | ZERO_STANDING | -
R203 | line_items | ZERO_STANDING | -
R204 | line_items | - | -
R205 | line_items | - | -
R206 | line_items | ZERO_STANDING | -
R207 | line_items | - | -
R208 | line_items | ZERO_STANDING | -
R209 | line_items | ZERO_STANDING | -
R210 | line_items | - | -
R211 | line_items | - | -
R212 | line_items | - | -
R213 | line_items | - | -
R214 | line_items | - | -
R215 | line_items | - | -
R216 | line_items | - | -
R217 | line_items | - | -
R218 | line_items | - | -
R219 | line_items | - | -
R220 | line_items | - | -
R221 | line_items | - | -
R222 | line_items | - | -
R223 | line_items | - | -
R224 | line_items | - | -
R225 | line_items | - | -
R226 | line_items | - | -
R227 | line_items | - | -
R228 | line_items | - | -
R229 | line_items | - | -
R230 | line_items | - | -
R231 | line_items | - | -
R232 | line_items | - | -
R233 | line_items | - | -
R234 | line_items | - | -
R235 | line_items | - | -
R236 | line_items | - | -
R237 | line_items | - | -
R238 | line_items | - | -
R239 | line_items | - | -
R240 | line_items | - | -
R241 | line_items | - | -
R242 | line_items | - | -
R243 | line_items | - | -
R244 | line_items | - | -
R245 | line_items | - | -
R246 | line_items | ZERO_STANDING | -
R247 | line_items | - | -
R248 | line_items | OCR_GARBLED | -
R249 | line_items | - | -
R250 | line_items | - | -
R251 | line_items | - | -
R252 | line_items | - | -
R253 | line_items | - | -
R254 | line_items | ZERO_STANDING | -
R255 | line_items | ZERO_STANDING | -
R256 | line_items | - | -
R257 | line_items | - | -
R258 | line_items | - | -
R259 | line_items | - | -
R260 | line_items | ZERO_STANDING | -
R261 | line_items | - | -
R262 | line_items | - | -
R263 | line_items | - | -
R264 | line_items | - | -
R265 | line_items | - | -
R266 | line_items | - | -
R267 | line_items | - | -
R268 | line_items | - | -
R269 | line_items | - | -
R270 | line_items | - | -
R271 | line_items | - | -
R272 | line_items | ZERO_STANDING | -
R273 | line_items | ZERO_STANDING | -
R274 | line_items | - | -
R275 | line_items | - | -
R276 | line_items | - | -
R277 | line_items | - | -
R278 | line_items | - | -
R279 | line_items | - | -
R280 | line_items | - | -
R281 | line_items | - | -
R282 | line_items | - | -
R283 | line_items | - | -
R284 | line_items | - | -
R285 | line_items | - | -
R286 | line_items | - | -
R287 | line_items | - | -
R288 | line_items | - | -
R289 | line_items | - | -
R290 | line_items | - | -
R291 | line_items | - | -
R292 | line_items | - | -
R293 | line_items | - | -
R294 | line_items | - | -
R295 | line_items | - | -
R296 | line_items | - | -
R297 | line_items | - | -
R298 | line_items | - | -
R299 | line_items | - | -
R300 | line_items | - | -
R301 | line_items | - | -
R302 | line_items | - | -
R303 | line_items | - | -
R304 | line_items | - | -
R305 | line_items | - | -
R306 | line_items | - | -
R307 | line_items | - | -
R308 | line_items | - | -
R309 | line_items | - | -
R310 | line_items | - | -
R311 | line_items | CELL_BLANK_IN_TEXT | -
R312 | line_items | - | -
R313 | line_items | CELL_BLANK_IN_TEXT | -
R314 | line_items | - | -
R315 | line_items | - | -
R316 | line_items | - | -
R317 | line_items | - | -
R318 | line_items | - | -
R319 | line_items | - | -
R320 | line_items | - | -
R321 | line_items | - | -
R322 | line_items | - | -
R323 | line_items | - | -
R324 | line_items | - | -
R325 | line_items | - | -
R326 | line_items | - | -
R327 | line_items | - | -
R328 | line_items | - | -
R329 | line_items | - | -
R330 | line_items | - | -
R331 | line_items | - | -
R332 | line_items | - | -
R333 | line_items | - | -
R334 | line_items | - | -
R335 | line_items | - | -
R336 | line_items | - | -
R337 | line_items | - | -
R338 | line_items | - | -
R339 | line_items | - | -
R340 | line_items | - | -
R341 | line_items | - | -

## Numbered notes (pp8-9) (69)
ROW_ID | category | A2 flags | cross-ref / note
R342 | notes | - | Note 4
R343 | notes | ZERO_STANDING | Note 4
R344 | notes | ZERO_STANDING | Note 4
R345 | notes | - | Note 4
R346 | notes | - | Note 4
R347 | notes | ZERO_STANDING | Note 4
R348 | notes | ZERO_STANDING | Note 4
R349 | notes | ZERO_STANDING | Note 4
R350 | notes | - | Note 4
R351 | notes | ZERO_STANDING | Note 4
R352 | notes | ZERO_STANDING | Note 4
R353 | notes | - | Note 4
R354 | notes | - | Note 4
R355 | notes | - | Note 5
R356 | notes | - | Note 5
R357 | notes | - | Note 5
R358 | notes | - | Note 5
R359 | notes | - | Note 5
R360 | notes | ZERO_STANDING | Note 5
R361 | notes | ZERO_STANDING | Note 5
R362 | notes | - | Note 5
R363 | notes | - | Note 5
R364 | notes | - | Note 5
R365 | notes | - | Note 5
R366 | notes | - | Note 5
R367 | notes | - | Note 5
R368 | notes | - | Note 5
R369 | notes | ZERO_STANDING | Note 5
R370 | notes | ZERO_STANDING | Note 5
R371 | notes | ZERO_STANDING | Note 5
R372 | notes | - | Note 5
R373 | notes | - | Note 5
R374 | notes | - | Note 5
R375 | notes | - | Note 5
R376 | notes | - | Note 7
R377 | notes | - | Note 8
R378 | notes | - | Note 10
R379 | notes | - | Note 10
R380 | notes | - | Note 10
R381 | notes | - | Note 10
R382 | notes | - | Note 10
R383 | notes | - | Note 10
R384 | notes | - | Note 10
R385 | notes | - | Note 10
R386 | notes | - | Note 10
R387 | notes | ZERO_STANDING | Note 10
R388 | notes | - | Note 10
R389 | notes | - | Note 10
R390 | notes | ZERO_STANDING | Note 10
R391 | notes | - | RESTATED R618
R392 | notes | - | Note 11
R393 | notes | - | Note 11
R394 | notes | - | Note 11
R711 | notes | - | Note None
R712 | notes | - | Note 2
R713 | notes | - | Note 3
R714 | notes | - | Note 4
R716 | notes | - | Note 4
R717 | notes | - | Note 5
R718 | notes | - | Note 5
R719 | notes | - | Note 5
R720 | notes | - | Note 5
R721 | notes | - | Note 6
R722 | notes | - | Note 7
R723 | notes | - | Note 8
R724 | notes | - | Note 9
R725 | notes | - | Note 10
R726 | notes | - | Note 11
R727 | notes | - | Note 12

## Unnumbered notes / footnotes (4)
ROW_ID | category | A2 flags | cross-ref / note
R704 | notes_unnumbered | - | -
R708 | notes_unnumbered | - | -
R715 | notes_unnumbered | - | -
R737 | notes_unnumbered | - | -

## Reg 52(4) ratios (p10) (12)
ROW_ID | category | A2 flags | cross-ref / note
R395 | ratios | - | -
R396 | ratios | - | -
R397 | ratios | - | -
R398 | ratios | - | -
R399 | ratios | - | -
R400 | ratios | - | -
R401 | ratios | - | -
R402 | ratios | - | -
R403 | ratios | - | -
R404 | ratios | - | -
R405 | ratios | - | -
R406 | ratios | - | -

## Annexure tables: security cover 1/1A/2/2A/3/Annexure I (155)
ROW_ID | category | A2 flags | cross-ref / note
R414 | annexure_numbers | - | RESTATED R032
R415 | annexure_numbers | - | -
R416 | annexure_numbers | - | -
R417 | annexure_numbers | - | -
R418 | annexure_numbers | - | -
R419 | annexure_numbers | - | -
R420 | annexure_numbers | - | -
R421 | annexure_numbers | - | -
R422 | annexure_numbers | - | -
R423 | annexure_numbers | - | -
R424 | annexure_numbers | - | -
R425 | annexure_numbers | - | -
R426 | annexure_numbers | - | -
R427 | annexure_numbers | - | -
R428 | annexure_numbers | - | -
R429 | annexure_numbers | - | -
R430 | annexure_numbers | - | -
R431 | annexure_numbers | - | -
R432 | annexure_numbers | - | -
R433 | annexure_numbers | - | -
R434 | annexure_numbers | - | -
R435 | annexure_numbers | - | -
R436 | annexure_numbers | - | -
R437 | annexure_numbers | - | -
R438 | annexure_numbers | - | -
R439 | annexure_numbers | - | -
R440 | annexure_numbers | - | -
R441 | annexure_numbers | - | -
R442 | annexure_numbers | - | -
R443 | annexure_numbers | - | -
R444 | annexure_numbers | - | -
R445 | annexure_numbers | - | -
R446 | annexure_numbers | - | -
R447 | annexure_numbers | - | -
R448 | annexure_numbers | - | -
R449 | annexure_numbers | - | -
R450 | annexure_numbers | - | -
R451 | annexure_numbers | - | -
R452 | annexure_numbers | - | -
R453 | annexure_numbers | - | -
R454 | annexure_numbers | - | -
R455 | annexure_numbers | - | -
R456 | annexure_numbers | - | -
R457 | annexure_numbers | - | -
R458 | annexure_numbers | - | -
R459 | annexure_numbers | - | -
R460 | annexure_numbers | - | -
R461 | annexure_numbers | - | -
R462 | annexure_numbers | - | -
R463 | annexure_numbers | - | -
R464 | annexure_numbers | - | -
R465 | annexure_numbers | - | -
R466 | annexure_numbers | - | -
R467 | annexure_numbers | - | -
R468 | annexure_numbers | - | -
R469 | annexure_numbers | - | RESTATED R032
R470 | annexure_numbers | - | -
R471 | annexure_numbers | - | -
R472 | annexure_numbers | - | -
R473 | annexure_numbers | - | -
R474 | annexure_numbers | - | -
R475 | annexure_numbers | - | -
R476 | annexure_numbers | - | -
R477 | annexure_numbers | - | -
R478 | annexure_numbers | - | -
R479 | annexure_numbers | - | -
R480 | annexure_numbers | - | -
R481 | annexure_numbers | - | -
R482 | annexure_numbers | - | -
R483 | annexure_numbers | - | -
R484 | annexure_numbers | - | -
R485 | annexure_numbers | - | -
R486 | annexure_numbers | - | -
R487 | annexure_numbers | - | -
R488 | annexure_numbers | - | -
R489 | annexure_numbers | - | -
R490 | annexure_numbers | - | -
R491 | annexure_numbers | - | -
R492 | annexure_numbers | - | -
R493 | annexure_numbers | - | -
R494 | annexure_numbers | - | -
R495 | annexure_numbers | - | -
R496 | annexure_numbers | - | -
R497 | annexure_numbers | - | -
R498 | annexure_numbers | - | -
R499 | annexure_numbers | - | -
R500 | annexure_numbers | - | -
R501 | annexure_numbers | - | -
R502 | annexure_numbers | - | -
R503 | annexure_numbers | - | -
R504 | annexure_numbers | - | -
R505 | annexure_numbers | - | -
R506 | annexure_numbers | - | -
R507 | annexure_numbers | - | -
R508 | annexure_numbers | - | -
R509 | annexure_numbers | - | -
R510 | annexure_numbers | - | -
R511 | annexure_numbers | - | -
R512 | annexure_numbers | - | -
R513 | annexure_numbers | - | -
R514 | annexure_numbers | - | -
R515 | annexure_numbers | - | -
R516 | annexure_numbers | - | -
R517 | annexure_numbers | - | -
R518 | annexure_numbers | - | -
R519 | annexure_numbers | - | -
R520 | annexure_numbers | - | -
R521 | annexure_numbers | - | -
R522 | annexure_numbers | - | -
R523 | annexure_numbers | - | -
R524 | annexure_numbers | - | -
R525 | annexure_numbers | - | -
R526 | annexure_numbers | - | -
R527 | annexure_numbers | - | -
R528 | annexure_numbers | - | -
R529 | annexure_numbers | - | -
R530 | annexure_numbers | - | -
R531 | annexure_numbers | - | -
R532 | annexure_numbers | - | -
R533 | annexure_numbers | - | -
R534 | annexure_numbers | - | -
R535 | annexure_numbers | - | -
R536 | annexure_numbers | - | -
R537 | annexure_numbers | - | -
R538 | annexure_numbers | - | -
R539 | annexure_numbers | - | -
R540 | annexure_numbers | - | -
R541 | annexure_numbers | - | -
R542 | annexure_numbers | - | -
R543 | annexure_numbers | - | -
R544 | annexure_numbers | - | -
R545 | annexure_numbers | - | -
R546 | annexure_numbers | - | -
R547 | annexure_numbers | - | -
R548 | annexure_numbers | - | -
R549 | annexure_numbers | - | -
R550 | annexure_numbers | - | -
R551 | annexure_numbers | - | -
R552 | annexure_numbers | - | -
R553 | annexure_numbers | - | -
R554 | annexure_numbers | - | -
R555 | annexure_numbers | - | -
R556 | annexure_numbers | - | -
R557 | annexure_numbers | - | -
R558 | annexure_numbers | - | -
R559 | annexure_numbers | - | -
R560 | annexure_numbers | - | -
R561 | annexure_numbers | - | -
R562 | annexure_numbers | - | -
R563 | annexure_numbers | - | -
R564 | annexure_numbers | - | -
R565 | annexure_numbers | - | -
R566 | annexure_numbers | - | -
R567 | annexure_numbers | - | -
R568 | annexure_numbers | - | -

## Annexure footnotes (7)
ROW_ID | category | A2 flags | cross-ref / note
R742 | annexure_footnotes | - | -
R743 | annexure_footnotes | - | -
R744 | annexure_footnotes | - | RESTATED R616 (Rs 455 cr security not maintained, lender time limit)
R745 | annexure_footnotes | - | -
R746 | annexure_footnotes | FOOTNOTE_UNRESOLVED | -
R747 | annexure_footnotes | - | -
R748 | annexure_footnotes | FOOTNOTE_UNRESOLVED | -

## Auditor / security cover report paragraphs and signatory numbers (19)
ROW_ID | category | A2 flags | cross-ref / note
R006 | auditor_paras | - | RESTATED R696
R007 | auditor_paras | - | -
R008 | auditor_paras | - | -
R009 | auditor_paras | - | -
R010 | auditor_paras | - | -
R011 | auditor_paras | - | -
R012 | auditor_paras | - | -
R013 | auditor_paras | - | -
R411 | auditor_paras | - | xref R739,R749
R412 | auditor_paras | - | -
R695 | auditor_paras | - | -
R696 | auditor_paras | UNREVIEWED_COMPONENT | RESTATED R006-R010 (Trust unreviewed)
R697 | auditor_paras | - | -
R698 | auditor_paras | - | -
R699 | auditor_paras | - | -
R738 | auditor_paras | - | -
R739 | auditor_paras | COVENANT_BREACH_FLAG | covenant breach; xref R411,R617,R749
R740 | auditor_paras | COVENANT_BREACH_FLAG | -
R741 | auditor_paras | - | -

## Entities (43)
ROW_ID | category | A2 flags | cross-ref / note
R569 | entities | - | -
R570 | entities | - | -
R571 | entities | - | -
R572 | entities | - | -
R573 | entities | - | -
R574 | entities | ENTITY_CHANGE | auditor change: S S Kothari Mehta (R580) to MSKA (R574); predecessor reports R578
R575 | entities | - | -
R576 | entities | - | -
R577 | entities | UNREVIEWED_COMPONENT | -
R578 | entities | ENTITY_CHANGE | auditor change: S S Kothari Mehta (R580) to MSKA (R574); predecessor reports R578
R579 | entities | - | -
R580 | entities | ENTITY_CHANGE | auditor change: S S Kothari Mehta (R580) to MSKA (R574); predecessor reports R578
R581 | entities | - | -
R582 | entities | - | -
R583 | entities | - | -
R584 | entities | - | -
R585 | entities | - | -
R586 | entities | - | unconsolidated 100% sub (Note 7)
R587 | entities | - | -
R588 | entities | - | -
R589 | entities | - | -
R590 | entities | - | -
R591 | entities | - | -
R592 | entities | - | -
R593 | entities | - | -
R594 | entities | - | -
R595 | entities | - | ISIN: also in Annexure 1A/3 NUMBER/DATE rows
R596 | entities | - | ISIN: also in Annexure 1A/3 NUMBER/DATE rows
R597 | entities | - | ISIN: also in Annexure 1A/3 NUMBER/DATE rows
R598 | entities | - | ISIN: also in Annexure 1A/3 NUMBER/DATE rows
R599 | entities | - | ISIN: also in Annexure 1A/3 NUMBER/DATE rows
R600 | entities | - | ISIN: also in Annexure 1A/3 NUMBER/DATE rows
R601 | entities | - | ISIN: also in Annexure 1A/3 NUMBER/DATE rows
R602 | entities | - | ISIN: also in Annexure 1A/3 NUMBER/DATE rows
R603 | entities | - | ISIN: also in Annexure 1A/3 NUMBER/DATE rows
R604 | entities | - | ISIN: also in Annexure 1A/3 NUMBER/DATE rows
R605 | entities | - | ISIN: also in Annexure 1A/3 NUMBER/DATE rows
R606 | entities | - | ISIN: also in Annexure 1A/3 NUMBER/DATE rows
R607 | entities | - | ISIN: also in Annexure 1A/3 NUMBER/DATE rows
R608 | entities | - | ISIN: also in Annexure 1A/3 NUMBER/DATE rows
R609 | entities | - | ISIN: also in Annexure 1A/3 NUMBER/DATE rows
R610 | entities | - | ISIN: also in Annexure 1A/3 NUMBER/DATE rows
R611 | entities | - | -

## Forward-looking statements (7)
ROW_ID | category | A2 flags | cross-ref / note
R612 | forward | - | -
R613 | forward | OTHER_AGENDA_UNSPECIFIED | -
R614 | forward | - | -
R615 | forward | - | -
R616 | forward | - | RESTATED R744
R617 | forward | COVENANT_BREACH_FLAG | xref R739,R749
R618 | forward | - | RESTATED R391

## Dates (75)
ROW_ID | category | A2 flags | cross-ref / note
R619 | dates | - | RESTATED R001
R620 | dates | - | -
R621 | dates | - | -
R622 | dates | - | RESTATED R003,R004
R623 | dates | - | -
R624 | dates | - | -
R625 | dates | - | -
R626 | dates | - | -
R627 | dates | - | -
R628 | dates | - | -
R629 | dates | - | -
R630 | dates | - | -
R631 | dates | - | -
R632 | dates | - | -
R633 | dates | - | -
R634 | dates | - | -
R635 | dates | - | -
R636 | dates | - | -
R637 | dates | - | -
R638 | dates | - | -
R639 | dates | - | xref R385-R391
R640 | dates | - | -
R641 | dates | - | -
R642 | dates | - | -
R643 | dates | - | -
R644 | dates | - | -
R645 | dates | - | -
R646 | dates | - | -
R647 | dates | - | -
R648 | dates | - | -
R649 | dates | - | -
R650 | dates | - | -
R651 | dates | - | -
R652 | dates | - | -
R653 | dates | - | -
R654 | dates | - | -
R655 | dates | - | -
R656 | dates | - | -
R657 | dates | - | -
R658 | dates | - | -
R659 | dates | - | -
R660 | dates | - | -
R661 | dates | - | -
R662 | dates | - | -
R663 | dates | - | -
R664 | dates | - | -
R665 | dates | - | -
R666 | dates | - | -
R667 | dates | - | -
R668 | dates | - | -
R669 | dates | - | -
R670 | dates | - | -
R671 | dates | - | -
R672 | dates | - | -
R673 | dates | - | -
R674 | dates | - | -
R675 | dates | - | -
R676 | dates | - | -
R677 | dates | - | -
R678 | dates | - | -
R679 | dates | - | -
R680 | dates | - | -
R681 | dates | - | -
R682 | dates | - | -
R683 | dates | - | -
R684 | dates | - | -
R685 | dates | - | -
R686 | dates | - | -
R687 | dates | - | -
R688 | dates | - | -
R689 | dates | - | -
R690 | dates | - | -
R691 | dates | - | -
R692 | dates | - | -
R693 | dates | - | -

## Other qualifiers / definitions (24)
ROW_ID | category | A2 flags | cross-ref / note
R700 | qualifiers_other | - | -
R701 | qualifiers_other | - | -
R702 | qualifiers_other | - | -
R703 | qualifiers_other | - | -
R705 | qualifiers_other | - | -
R706 | qualifiers_other | - | -
R707 | qualifiers_other | - | -
R709 | qualifiers_other | - | -
R710 | qualifiers_other | - | -
R728 | qualifiers_other | - | -
R729 | qualifiers_other | - | -
R730 | qualifiers_other | - | -
R731 | qualifiers_other | - | -
R732 | qualifiers_other | - | -
R733 | qualifiers_other | - | -
R734 | qualifiers_other | - | -
R735 | qualifiers_other | - | -
R736 | qualifiers_other | - | -
R749 | qualifiers_other | COVENANT_BREACH_FLAG | xref R411,R617,R739
R750 | qualifiers_other | - | -
R751 | qualifiers_other | - | -
R752 | qualifiers_other | - | -
R753 | qualifiers_other | - | -
R754 | qualifiers_other | - | -

## Other numbers (5)
ROW_ID | category | A2 flags | cross-ref / note
R407 | other_numbers | - | RESTATED R002
R408 | other_numbers | - | -
R409 | other_numbers | - | -
R410 | other_numbers | - | -
R413 | other_numbers | - | -
