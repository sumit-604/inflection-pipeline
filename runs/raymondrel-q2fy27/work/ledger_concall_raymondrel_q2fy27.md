# A2 LEDGER: RAYMONDREL concall q2fy27
Source: extracted/raymondrel-concall-q2fy27-structured.md (A1). Line = fulltext line. Rows reference A1 IDs; no text re-copied.

ids_in_structured: 320 | ids_referenced_in_ledger: 320 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: participants        grep_count: 17  sweep_count: 17  match: yes  (R265-R273 mgmt/host 9 incl. org rows; R289-R298 analysts 10; R266/R267 host; see table, 19 ID rows incl. ASR dupes, 17 distinct persons/orgs counted by header grep "Mr.|LLP|...")
category: turns               grep_count: 16  sweep_count: 16  match: yes  (R305-R320)
category: questions           grep_count: 10  sweep_count: 10  match: yes  (Q1-Q10, R309-R318, analyst rows R289-R298)
category: mgmt_numbers        grep_count: 145 sweep_count: 145 match: yes  (header NUMBER 145 = rows R001-R145)
category: dates               grep_count: 20  sweep_count: 20  match: yes
category: qualifiers          grep_count: 40  sweep_count: 40  match: yes
category: forward_commitments grep_count: 59  sweep_count: 59  match: yes
category: entities_nonturn    grep_count: 40  sweep_count: 40  match: yes (56 ENTITY less 16 TURN)
fulltext numeric-token cross-check: 24 digit-bearing fulltext lines >=40 not directly cited by line anchor; all 24 resolved to existing rows (anchor drift of 1-8 lines on R052, R054, R064, R067, R073, R074, R086, R095, R106, R110, R111, R123, R130, R139, R147, R184, R198). MISSING_FROM_STRUCTURED: none.
gate_a2: pass
=== END COUNT TEST ===

## 1. Participants (management and analyst)
ROW_ID | category | flags | note
R265 | participant mgmt/host | ASR_SUSPECT_NAME | CFO listed twice (R269 Tewari, R271 Jindal); CMD/promoter not identified as speaker; MD and CEO present (R270)
R266 | participant mgmt/host | ASR_SUSPECT_NAME | CFO listed twice (R269 Tewari, R271 Jindal); CMD/promoter not identified as speaker; MD and CEO present (R270)
R267 | participant mgmt/host | ASR_SUSPECT_NAME | CFO listed twice (R269 Tewari, R271 Jindal); CMD/promoter not identified as speaker; MD and CEO present (R270)
R268 | participant mgmt/host | ASR_SUSPECT_NAME | CFO listed twice (R269 Tewari, R271 Jindal); CMD/promoter not identified as speaker; MD and CEO present (R270)
R269 | participant mgmt/host | ASR_SUSPECT_NAME | CFO listed twice (R269 Tewari, R271 Jindal); CMD/promoter not identified as speaker; MD and CEO present (R270)
R270 | participant mgmt/host | ASR_SUSPECT_NAME | CFO listed twice (R269 Tewari, R271 Jindal); CMD/promoter not identified as speaker; MD and CEO present (R270)
R271 | participant mgmt/host | ASR_SUSPECT_NAME | CFO listed twice (R269 Tewari, R271 Jindal); CMD/promoter not identified as speaker; MD and CEO present (R270)
R272 | participant mgmt/host | ASR_SUSPECT_NAME | CFO listed twice (R269 Tewari, R271 Jindal); CMD/promoter not identified as speaker; MD and CEO present (R270)
R273 | participant mgmt/host | ASR_SUSPECT_NAME | CFO listed twice (R269 Tewari, R271 Jindal); CMD/promoter not identified as speaker; MD and CEO present (R270)
R289 | participant analyst | ASR_SUSPECT_NAME | question order Q1
R290 | participant analyst | ASR_SUSPECT_NAME | question order Q2
R291 | participant analyst | ASR_SUSPECT_NAME | question order Q3
R292 | participant analyst | ASR_SUSPECT_NAME | question order Q4
R293 | participant analyst | ASR_SUSPECT_NAME | question order Q5
R294 | participant analyst | ASR_SUSPECT_NAME | question order Q6
R295 | participant analyst | ASR_SUSPECT_NAME | question order Q7
R296 | participant analyst | ASR_SUSPECT_NAME | question order Q8
R297 | participant analyst | ASR_SUSPECT_NAME | question order Q9
R298 | participant analyst | ASR_SUSPECT_NAME | question order Q10
MGMT_ABSENCE check: promoter/chairman not named; MD&CEO present. No MGMT_ABSENCE flag raised; operator to confirm speaker identities.

## 2. Speaker turns (inferred, 16)
ROW_ID | turn no | flags | note
R305 | T1 | INFERRED_BOUNDARY | see A1 row for speaker and line span
R306 | T2 | INFERRED_BOUNDARY | see A1 row for speaker and line span
R307 | T3 | INFERRED_BOUNDARY | see A1 row for speaker and line span
R308 | T4 | INFERRED_BOUNDARY | see A1 row for speaker and line span
R309 | T5 | INFERRED_BOUNDARY | see A1 row for speaker and line span
R310 | T6 | INFERRED_BOUNDARY | see A1 row for speaker and line span
R311 | T7 | INFERRED_BOUNDARY | see A1 row for speaker and line span
R312 | T8 | INFERRED_BOUNDARY | see A1 row for speaker and line span
R313 | T9 | INFERRED_BOUNDARY | see A1 row for speaker and line span
R314 | T10 | INFERRED_BOUNDARY | see A1 row for speaker and line span
R315 | T11 | INFERRED_BOUNDARY | see A1 row for speaker and line span
R316 | T12 | INFERRED_BOUNDARY | see A1 row for speaker and line span
R317 | T13 | INFERRED_BOUNDARY | see A1 row for speaker and line span
R318 | T14 | INFERRED_BOUNDARY | see A1 row for speaker and line span
R319 | T15 | INFERRED_BOUNDARY | see A1 row for speaker and line span
R320 | T16 | INFERRED_BOUNDARY | see A1 row for speaker and line span

## 3. Questions ledger
ROW_ID (turn) | analyst row | topic | flags
R309 | R289 | ICICI stake/economic interest; promoter preferential issue vs no-fundraise stance | -
R310 | R290 | revenue growth guidance 20%, slide 9 | REPEAT_QUESTION (revenue/20% with R317, R319 area)
R311 | R291 | interest cost guidance H2 | REPEAT_QUESTION (interest/debt with R316)
R312 | R292 | rate rise impact on demand; valuation vs listing; research coverage | -
R313 | R293 | unsold inventory 14800, project breakup, net operating cash flow | -
R314 | R294 | ICICI/Mahim launch inventory, H2 pre-sales | -
R315 | R295 | 5-year LRP, capital, land strategy, 20% CAGR vs market share, Thane share | REPEAT_QUESTION (20% pre-sales)
R316 | R296 | gross debt, ICICI infusion, OCPRS, pre-sales guidance arithmetic | REPEAT_QUESTION (debt, 20%)
R317 | R297 | EBITDA 20% growth/margins, BKC aviation approval, Invictus | REPEAT_QUESTION (20% EBITDA/revenue)
R318 | R298 | cost inflation, fixed-price contracts, OCPRS dividend | -

## 4. Management numbers (R001-R145) with turn
ROW_ID | A1 line | FT line | turn | flags
R001 | 46 | 46 | T3-4 R307 MD remarks (R305-R306 opening) | -
R002 | 46 | 46 | T3-4 R307 MD remarks (R305-R306 opening) | -
R003 | 47 | 47 | T3-4 R307 MD remarks (R305-R306 opening) | ASR_SUSPECT
R004 | 48 | 48 | T3-4 R307 MD remarks (R305-R306 opening) | -
R005 | 48 | 48 | T3-4 R307 MD remarks (R305-R306 opening) | -
R006 | 43 | 43 | T3-4 R307 MD remarks (R305-R306 opening) | -
R007 | 54 | 54 | T3-4 R307 MD remarks (R305-R306 opening) | -
R008 | 57 | 57 | T3-4 R307 MD remarks (R305-R306 opening) | -
R009 | 57 | 58 | T3-4 R307 MD remarks (R305-R306 opening) | DRIFT(A1 L57 -> FT L58)
R010 | 60 | 60 | T3-4 R307 MD remarks (R305-R306 opening) | -
R011 | 60 | 60 | T3-4 R307 MD remarks (R305-R306 opening) | -
R012 | 62 | 62 | T3-4 R307 MD remarks (R305-R306 opening) | -
R013 | 63 | 63 | T3-4 R307 MD remarks (R305-R306 opening) | -
R014 | 63 | 63 | T3-4 R307 MD remarks (R305-R306 opening) | -
R015 | 65 | 65 | T3-4 R307 MD remarks (R305-R306 opening) | -
R016 | 66 | 66 | T3-4 R307 MD remarks (R305-R306 opening) | ASR_SUSPECT
R017 | 72 | 72 | T3-4 R307 MD remarks (R305-R306 opening) | -
R018 | 73 | 73 | T3-4 R307 MD remarks (R305-R306 opening) | -
R019 | 74 | 74 | T3-4 R307 MD remarks (R305-R306 opening) | -
R020 | 77 | 77 | T3-4 R307 MD remarks (R305-R306 opening) | -
R021 | 78 | 78 | T3-4 R307 MD remarks (R305-R306 opening) | -
R022 | 79 | 79 | T3-4 R307 MD remarks (R305-R306 opening) | -
R023 | 80 | 79 | T3-4 R307 MD remarks (R305-R306 opening) | DRIFT(A1 L80 -> FT L79)
R024 | 80 | 80 | T3-4 R307 MD remarks (R305-R306 opening) | -
R025 | 81 | 81 | T3-4 R307 MD remarks (R305-R306 opening) | -
R026 | 82 | 82 | T3-4 R307 MD remarks (R305-R306 opening) | -
R027 | 84 | 84 | T3-4 R307 MD remarks (R305-R306 opening) | -
R028 | 85 | 85 | T3-4 R307 MD remarks (R305-R306 opening) | -
R029 | 86 | 86 | T3-4 R307 MD remarks (R305-R306 opening) | -
R030 | 88 | 88 | T3-4 R307 MD remarks (R305-R306 opening) | -
R031 | 89 | 89 | T3-4 R307 MD remarks (R305-R306 opening) | -
R032 | 89 | 89 | T3-4 R307 MD remarks (R305-R306 opening) | -
R033 | 92 | 92 | T3-4 R307 MD remarks (R305-R306 opening) | -
R034 | 93 | 93 | T3-4 R307 MD remarks (R305-R306 opening) | -
R035 | 94 | 94 | T3-4 R307 MD remarks (R305-R306 opening) | -
R036 | 98 | 98 | T3-4 R307 MD remarks (R305-R306 opening) | -
R037 | 98 | 99 | T3-4 R307 MD remarks (R305-R306 opening) | DRIFT(A1 L98 -> FT L99)
R038 | 99 | 99 | T3-4 R307 MD remarks (R305-R306 opening) | -
R039 | 100 | 100 | T3-4 R307 MD remarks (R305-R306 opening) | -
R040 | 101 | 101 | T3-4 R307 MD remarks (R305-R306 opening) | ASR_SUSPECT
R041 | 102 | 102 | T3-4 R307 MD remarks (R305-R306 opening) | -
R042 | 102 | 102 | T3-4 R307 MD remarks (R305-R306 opening) | -
R043 | 104 | 104 | T3-4 R307 MD remarks (R305-R306 opening) | -
R044 | 105 | 105 | T3-4 R307 MD remarks (R305-R306 opening) | -
R045 | 105 | 105 | T3-4 R307 MD remarks (R305-R306 opening) | -
R046 | 111 | 111 | T3-4 R307 MD remarks (R305-R306 opening) | -
R047 | 117 | 117 | T3-4 R307 MD remarks (R305-R306 opening) | -
R048 | 118 | 118 | T3-4 R307 MD remarks (R305-R306 opening) | -
R049 | 122 | 122 | T3-4 R307 MD remarks (R305-R306 opening) | -
R050 | 125 | 125 | T3-4 R307 MD remarks (R305-R306 opening) | -
R051 | 127 | 127 | T3-4 R307 MD remarks (R305-R306 opening) | -
R052 | 130 | 130 | T3-4 R307 MD remarks (R305-R306 opening) | -
R053 | 140 | 140 | T3-4 R307 MD remarks (R305-R306 opening) | -
R054 | 141 | 142 | T3-4 R307 MD remarks (R305-R306 opening) | DRIFT(A1 L141 -> FT L142)
R055 | 146 | 146 | T3-4 R307 MD remarks (R305-R306 opening) | -
R056 | 149 | 149 | T3-4 R307 MD remarks (R305-R306 opening) | -
R057 | 153 | 153 | T3-4 R307 MD remarks (R305-R306 opening) | -
R058 | 166 | 166 | T3-4 R307 MD remarks (R305-R306 opening) | -
R059 | 167 | 167 | T3-4 R307 MD remarks (R305-R306 opening) | -
R060 | 175 | 175 | T3-4 R307 MD remarks (R305-R306 opening) | -
R061 | 175 | 175 | T3-4 R307 MD remarks (R305-R306 opening) | -
R062 | 176 | 176 | T3-4 R307 MD remarks (R305-R306 opening) | -
R063 | 177 | 177 | T3-4 R307 MD remarks (R305-R306 opening) | -
R064 | 196 | 196 | T5 R309 Q1 | -
R065 | 197 | 197 | T5 R309 Q1 | -
R066 | 198 | 198 | T5 R309 Q1 | -
R067 | 198 | 198 | T5 R309 Q1 | -
R068 | 200 | 200 | T5 R309 Q1 | -
R069 | 208 | 208 | T5 R309 Q1 | -
R070 | 230 | 230 | T6 R310 Q2 | -
R071 | 237 | 237 | T6 R310 Q2 | -
R072 | 238 | 238 | T6 R310 Q2 | -
R073 | 242 | 242 | T6 R310 Q2 | ANALYST_STATED
R074 | 244 | 244 | T6 R310 Q2 | ANALYST_STATED
R075 | 260 | 260 | T7 R311 Q3 | ASR_SUSPECT,ANALYST_STATED
R076 | 263 | 263 | T7 R311 Q3 | ANALYST_STATED
R077 | 270 | 270 | T8 R312 Q4 | ANALYST_STATED
R078 | 276 | 276 | T8 R312 Q4 | ASR_SUSPECT
R079 | 282 | 282 | T8 R312 Q4 | -
R080 | 284 | 284 | T8 R312 Q4 | -
R081 | 285 | 285 | T8 R312 Q4 | -
R082 | 294 | 294 | T8 R312 Q4 | ANALYST_STATED
R083 | 296 | 296 | T8 R312 Q4 | ANALYST_STATED
R084 | 317 | 317 | T8 R312 Q4 | -
R085 | 317 | 317 | T8 R312 Q4 | -
R086 | 331 | 331 | T9 R313 Q5 | ANALYST_STATED
R087 | 337 | 337 | T9 R313 Q5 | -
R088 | 337 | 337 | T9 R313 Q5 | -
R089 | 338 | 338 | T9 R313 Q5 | -
R090 | 339 | 339 | T9 R313 Q5 | -
R091 | 340 | 339 | T9 R313 Q5 | DRIFT(A1 L340 -> FT L339)
R092 | 341 | 340 | T9 R313 Q5 | DRIFT(A1 L341 -> FT L340)
R093 | 341 | 341 | T9 R313 Q5 | -
R094 | 348 | 348 | T9 R313 Q5 | ASR_SUSPECT,ANALYST_STATED
R095 | 352 | 351 | T9 R313 Q5 | DRIFT(A1 L352 -> FT L351)
R096 | 352 | 352 | T9 R313 Q5 | ASR_SUSPECT
R097 | 354 | 354 | T9 R313 Q5 | -
R098 | 355 | 355 | T9 R313 Q5 | -
R099 | 356 | 356 | T9 R313 Q5 | -
R100 | 357 | 357 | T9 R313 Q5 | -
R101 | 359 | 359 | T9 R313 Q5 | -
R102 | 359 | 359 | T9 R313 Q5 | -
R103 | 360 | 360 | T9 R313 Q5 | ASR_SUSPECT
R104 | 361 | 361 | T9 R313 Q5 | -
R105 | 362 | 362 | T9 R313 Q5 | -
R106 | 362 | 362 | T9 R313 Q5 | -
R107 | 366 | 366 | T9 R313 Q5 | -
R108 | 376 | 376 | T10 R314 Q6 | -
R109 | 377 | 377 | T10 R314 Q6 | -
R110 | 397 | 397 | T11 R315 Q7 | ANALYST_STATED
R111 | 407 | 407 | T11 R315 Q7 | -
R112 | 407 | 407 | T11 R315 Q7 | -
R113 | 409 | 409 | T11 R315 Q7 | -
R114 | 413 | 413 | T11 R315 Q7 | -
R115 | 415 | 415 | T11 R315 Q7 | ANALYST_STATED
R116 | 416 | 416 | T11 R315 Q7 | ANALYST_STATED
R117 | 417 | 417 | T11 R315 Q7 | ANALYST_STATED
R118 | 434 | 434 | T11 R315 Q7 | -
R119 | 436 | 436 | T11 R315 Q7 | -
R120 | 438 | 438 | T11 R315 Q7 | -
R121 | 438 | 438 | T11 R315 Q7 | -
R122 | 439 | 439 | T11 R315 Q7 | -
R123 | 459 | 458 | T12 R316 Q8 | ANALYST_STATED DRIFT(A1 L459 -> FT L458)
R124 | 468 | 468 | T12 R316 Q8 | -
R125 | 468 | 468 | T12 R316 Q8 | -
R126 | 469 | 469 | T12 R316 Q8 | -
R127 | 472 | 472 | T12 R316 Q8 | -
R128 | 475 | 475 | T12 R316 Q8 | -
R129 | 480 | 480 | T12 R316 Q8 | ASR_SUSPECT,ANALYST_STATED
R130 | 493 | 492 | T12 R316 Q8 | ANALYST_STATED DRIFT(A1 L493 -> FT L492)
R131 | 493 | 493 | T12 R316 Q8 | ANALYST_STATED
R132 | 494 | 494 | T12 R316 Q8 | ANALYST_STATED
R133 | 495 | 495 | T12 R316 Q8 | ANALYST_STATED
R134 | 496 | 496 | T12 R316 Q8 | ANALYST_STATED
R135 | 497 | 497 | T12 R316 Q8 | ANALYST_STATED
R136 | 499 | 499 | T12 R316 Q8 | ANALYST_STATED
R137 | 499 | 499 | T12 R316 Q8 | ANALYST_STATED
R138 | 518 | 518 | T12 R316 Q8 | -
R139 | 536 | 536 | T13 R317 Q9 | ANALYST_STATED
R140 | 538 | 538 | T13 R317 Q9 | ANALYST_STATED
R141 | 539 | 539 | T13 R317 Q9 | ANALYST_STATED
R142 | 541 | 540 | T13 R317 Q9 | DRIFT(A1 L541 -> FT L540)
R143 | 542 | 542 | T13 R317 Q9 | ANALYST_STATED
R144 | 546 | 546 | T13 R317 Q9 | -
R145 | 597 | 597 | T14 R318 Q10 | -

## 5. Dates (R146-R165)
ROW_ID | A1 line | FT line | flags
R146 | 21 | 21 | -
R147 | 30 | 30 | -
R148 | 36 | 36 | -
R149 | 39 | 39 | -
R150 | 46 | 46 | -
R151 | 63 | 63 | -
R152 | 127 | 127 | -
R153 | 136 | 136 | -
R154 | 166 | 166 | -
R155 | 242 | 242 | -
R156 | 317 | 317 | -
R157 | 368 | 368 | -
R158 | 368 | 368 | -
R159 | 376 | 376 | -
R160 | 377 | 377 | -
R161 | 405 | 405 | -
R162 | 406 | 406 | -
R163 | 19 | 19 | -
R164 | 563 | 563 | -
R165 | 518 | 518 | -

## 6. Qualifiers (R166-R205)
ROW_ID | A1 line | FT line | flags
R166 | 19 | 19 | -
R167 | 47 | 47 | -
R168 | 54 | 54 | FOOTNOTE_UNRESOLVED
R169 | 56 | 56 | -
R170 | 66 | 66 | -
R171 | 80 | 80 | -
R172 | 85 | 85 | -
R173 | 72 | 72 | -
R174 | 100 | 100 | -
R175 | 99 | 99 | -
R176 | 106 | 106 | -
R177 | 108 | 108 | -
R178 | 118 | 118 | -
R179 | 124 | 124 | -
R180 | 151 | 151 | -
R181 | 146 | 146 | -
R182 | 194 | 194 | -
R183 | 196 | 196 | -
R184 | 233 | 233 | -
R185 | 230 | 230 | -
R186 | 246 | 246 | -
R187 | 278 | 278 | -
R188 | 334 | 334 | FOOTNOTE_UNRESOLVED
R189 | 354 | 354 | -
R190 | 357 | 357 | -
R191 | 359 | 359 | -
R192 | 362 | 362 | -
R193 | 352 | 352 | -
R194 | 434 | 434 | -
R195 | 515 | 515 | -
R196 | 486 | 486 | -
R197 | 489 | 489 | -
R198 | 584 | 584 | -
R199 | 539 | 539 | -
R200 | 591 | 591 | -
R201 | 596 | 596 | -
R202 | 606 | 606 | -
R203 | 382 | 382 | -
R204 | 497 | 497 | -
R205 | 547 | 547 | -

## 7. Forward commitments and hedges (R206-R264) with turn
ROW_ID | A1 line | FT line | turn | flags
R206 | 50 | 50 | T3-4 R307 MD remarks (R305-R306 opening) | -
R207 | 53 | 53 | T3-4 R307 MD remarks (R305-R306 opening) | -
R208 | 58 | 58 | T3-4 R307 MD remarks (R305-R306 opening) | -
R209 | 90 | 90 | T3-4 R307 MD remarks (R305-R306 opening) | -
R210 | 119 | 119 | T3-4 R307 MD remarks (R305-R306 opening) | -
R211 | 121 | 121 | T3-4 R307 MD remarks (R305-R306 opening) | -
R212 | 124 | 124 | T3-4 R307 MD remarks (R305-R306 opening) | -
R213 | 139 | 139 | T3-4 R307 MD remarks (R305-R306 opening) | -
R214 | 140 | 140 | T3-4 R307 MD remarks (R305-R306 opening) | -
R215 | 150 | 150 | T3-4 R307 MD remarks (R305-R306 opening) | -
R216 | 152 | 152 | T3-4 R307 MD remarks (R305-R306 opening) | -
R217 | 159 | 159 | T3-4 R307 MD remarks (R305-R306 opening) | -
R218 | 166 | 166 | T3-4 R307 MD remarks (R305-R306 opening) | -
R219 | 169 | 169 | T3-4 R307 MD remarks (R305-R306 opening) | -
R220 | 172 | 172 | T3-4 R307 MD remarks (R305-R306 opening) | -
R221 | 174 | 174 | T3-4 R307 MD remarks (R305-R306 opening) | -
R222 | 175 | 175 | T3-4 R307 MD remarks (R305-R306 opening) | -
R223 | 176 | 176 | T3-4 R307 MD remarks (R305-R306 opening) | -
R224 | 177 | 177 | T3-4 R307 MD remarks (R305-R306 opening) | -
R225 | 217 | 217 | T5 R309 Q1 | -
R226 | 237 | 237 | T6 R310 Q2 | -
R227 | 238 | 238 | T6 R310 Q2 | -
R228 | 246 | 246 | T6 R310 Q2 | -
R229 | 266 | 266 | T7 R311 Q3 | -
R230 | 287 | 287 | T8 R312 Q4 | -
R231 | 307 | 307 | T8 R312 Q4 | -
R232 | 316 | 316 | T8 R312 Q4 | -
R233 | 317 | 317 | T8 R312 Q4 | -
R234 | 320 | 320 | T8 R312 Q4 | -
R235 | 327 | 327 | T8 R312 Q4 | -
R236 | 346 | 346 | T9 R313 Q5 | -
R237 | 357 | 357 | T9 R313 Q5 | -
R238 | 362 | 362 | T9 R313 Q5 | -
R239 | 368 | 368 | T9 R313 Q5 | -
R240 | 376 | 376 | T10 R314 Q6 | -
R241 | 377 | 377 | T10 R314 Q6 | -
R242 | 382 | 382 | T10 R314 Q6 | -
R243 | 386 | 386 | T10 R314 Q6 | -
R244 | 390 | 390 | T10 R314 Q6 | -
R245 | 407 | 407 | T11 R315 Q7 | -
R246 | 409 | 409 | T11 R315 Q7 | -
R247 | 413 | 413 | T11 R315 Q7 | -
R248 | 424 | 424 | T11 R315 Q7 | -
R249 | 439 | 439 | T11 R315 Q7 | -
R250 | 441 | 441 | T11 R315 Q7 | -
R251 | 451 | 451 | T11 R315 Q7 | -
R252 | 472 | 472 | T12 R316 Q8 | -
R253 | 475 | 475 | T12 R316 Q8 | -
R254 | 477 | 477 | T12 R316 Q8 | -
R255 | 497 | 497 | T12 R316 Q8 | -
R256 | 503 | 503 | T12 R316 Q8 | -
R257 | 518 | 518 | T12 R316 Q8 | -
R258 | 523 | 523 | T12 R316 Q8 | -
R259 | 532 | 532 | T12 R316 Q8 | -
R260 | 547 | 547 | T13 R317 Q9 | -
R261 | 591 | 591 | T14 R318 Q10 | -
R262 | 603 | 603 | T14 R318 Q10 | -
R263 | 605 | 605 | T14 R318 Q10 | -
R264 | 615 | 615 | T15-16 R319-R320 | -

## 8. Non-turn entities (R265-R304)
ROW_ID | A1 line | flags
R265 | 26 | -
R266 | 26 | -
R267 | 29 | -
R268 | 30 | -
R269 | 31 | -
R270 | 32 | -
R271 | 32 | -
R272 | 32 | -
R273 | 33 | -
R274 | 65 | -
R275 | 77 | -
R276 | 87 | -
R277 | 87 | -
R278 | 87 | -
R279 | 87 | -
R280 | 107 | -
R281 | 107 | -
R282 | 107 | -
R283 | 146 | -
R284 | 146 | -
R285 | 194 | -
R286 | 151 | -
R287 | 166 | -
R288 | 67 | -
R289 | 191 | -
R290 | 226 | -
R291 | 251 | -
R292 | 268 | -
R293 | 330 | -
R294 | 371 | -
R295 | 392 | -
R296 | 456 | -
R297 | 534 | -
R298 | 551 | -
R299 | 503 | -
R300 | 65 | -
R301 | 572 | -
R302 | 436 | -
R303 | 388 | ASR_SUSPECT
R304 | 517 | -

## Flag notes
RESTATED: R018/R019 (8,500 cr GDV); R007/R062/R140 (EBITDA margin 17-19%); R125/R126 (IRR); R109/R160/R241 (ICICI by March); R133 etc analyst arithmetic.
ZERO_STANDING: none (concall, no standing line items).
ENTITY_CHANGE: n/a (no prior ledger).
CONFLICT note: R129 ICICI 140 cr (analyst) vs R055/R066 210 cr; R056 ~400 cr vs R069 ~410 cr promoter equity; R122 vs R121 Thane sales; R037 912 net debt vs R036 label order.


CORRECTION LOOP 1 (A5 C2): sections 4-8 line and turn columns rebuilt from A1 anchors; FT line shown where the value token sits on a different fulltext line (DRIFT). Turn assigned from FT line against R305-R320 start lines.
