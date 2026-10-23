# A2 LEDGER: Fairchem Organics (FAIRCHEMOR) Q2 FY27 investor presentation
source of enumeration: extracted/fairchemor-presentation-q2fy27-structured.md (A1 structured, R001-R457). Values live at the ID; none re-copied.

=== A2 COUNT TEST ===
category: slides            grep_count: 24   sweep_count: 24   match: yes
category: slide_numbers     grep_count: 321  sweep_count: 321  match: yes
category: line_items (fin. tables p16-p20 NUMBER rows)  grep_count: 240  sweep_count: 240  match: yes
category: entities          grep_count: 60  sweep_count: 60   match: yes
category: forward           grep_count: 20   sweep_count: 20   match: yes
category: dates             grep_count: 24   sweep_count: 24   match: yes
category: footnotes_qualifiers grep_count: 87 sweep_count: 87   match: yes
category: zero_standing     grep_count: 11 (A1-flagged, 11 IDs)  sweep_count: 14 (A1 11 + A2 added 3: R180,R182,R183)  match: yes (difference explained, A2 added 3)
gate_a2: pass
=== END COUNT TEST ===

ids_in_structured: 512 | ids_referenced_in_ledger: 512 | orphan_ids: [] | match: yes
(per-table split: NUMBER 321 | ENTITY 60 | FORWARD 20 | DATE 24 | QUALIFIER 87 = 512 (loop 1: +48Q +7F))

Notes: grep_count reads A1 structured lines by TYPE; sweep_count tallies ledger rows by category. Sweep note: the grep count of ZERO_STANDING (A1 flags) is 11; A2 sweep found three more value-0 standing rows (R180 Intangible Assets FY26, R182 and R183 Intangible Assets Under Development FY26 and H1 FY27) that A1 left unflagged. Zero-standing total 14. MISSING_FROM_STRUCTURED: none. No numbered notes or agenda items apply (presentation). Carried A1 flags unresolved: LAYOUT_OFFSET (p16/p17), ORDER_INFERRED (p19), CHART_POSITION_INFERRED and CHART_UNASSIGNED (p22, p23 dividend), LAYOUT_GARBLED (p4).
RESTATED = same metric and period and value appears on more than one slide (p15/p16/p17/p18/p22); 54 rows carry it. DROPPED_SLIDE: not assessable, no prior ledger.

## SLIDE LEDGER (24 pages; page 1 = cover letter)
slide | title | content type | numbers | entities | forward | dates | qualifiers | A2 flags
---|---|---|---|---|---|---|---|---
S01 | Cover letter to exchanges (text) | - | 2 | 8 | 0 | 4 | 0 | -
S02 | Title slide: Earnings Presentation Q2 FY27 (text) | - | 0 | 0 | 0 | 1 | 0 | -
S03 | Section divider: Business Overview (text) | - | 0 | 0 | 0 | 0 | 0 | -
S04 | Company at a Glance (text) | - | 3 | 4 | 2 | 0 | 1 | LAYOUT_GARBLED
S05 | Manufacturing Process Overview (chart/flow) | - | 2 | 14 | 0 | 0 | 0 | -
S06 | Product Overview - Existing Portfolio (chart/table) | - | 0 | 13 | 2 | 0 | 2 | -
S07 | Waste-to-Wealth Manufacturing Capabilities (text/map) | - | 2 | 2 | 1 | 0 | 1 | -
S08 | Strong R&D Focus (text/photo) | - | 4 | 1 | 0 | 1 | 1 | -
S09 | Industry Standards and Regulatory Credentials (text/logos) | - | 0 | 1 | 0 | 0 | 0 | -
S10 | Fairchem's Competitive Advantage (text) | - | 3 | 1 | 0 | 1 | 2 | -
S11 | ESG Initiatives (text/table) | - | 1 | 2 | 1 | 1 | 3 | -
S12 | Manufacturing Facility Aerial Site Overview (photo) | - | 0 | 0 | 0 | 0 | 0 | -
S13 | Management and Governance (text/photo) | - | 3 | 8 | 0 | 3 | 1 | -
S14 | Section divider: Q2 FY27 Performance (text) | - | 0 | 0 | 0 | 1 | 0 | -
S15 | Q2|H1 FY27 Financial & Operational Highlights (text) | - | 16 | 1 | 1 | 2 | 3 | -
S16 | Q2 Financial Performance (table) | - | 38 | 0 | 0 | 1 | 4 | LAYOUT_NOTE,LAYOUT_OFFSET
S17 | H1 Financial Performance (table) | - | 37 | 0 | 0 | 1 | 3 | LAYOUT_NOTE,LAYOUT_OFFSET
S18 | Historical Income Statement (table) | - | 60 | 0 | 0 | 1 | 5 | LAYOUT_ORDER,ZERO_STANDING
S19 | Historical Balance Sheet (table) | - | 87 | 0 | 0 | 1 | 2 | LAYOUT_NOTE,ORDER_INFERRED,ZERO_STANDING
S20 | Historical Cash Flow Statement (table) | - | 18 | 0 | 0 | 1 | 1 | LAYOUT_ORDER,ZERO_STANDING
S21 | Business Strategy | Way forward (text) | - | 3 | 0 | 6 | 1 | 1 | -
S22 | Key Financial Highlights & Way forward (chart) | - | 28 | 0 | 0 | 1 | 3 | CHART_POSITION_INFERRED,CHART_UNASSIGNED
S23 | Capital Market Data (chart/table) | - | 14 | 2 | 0 | 3 | 4 | CHART_POSITION_INFERRED,LAYOUT_ORDER
S24 | Disclaimer and IR contact (text) | - | 0 | 3 | 0 | 0 | 2 | -

DROPPED_SLIDE: none assessable (PRIOR_LEDGER_PATH none, first quarterly run).

## ROW LEDGER (every structured ID)
ROW_ID | page | line | category | A2 flags | cross-ref / materiality
---|---|---|---|---|---
R001 | 1 | 39 | slide_number | - | -
R002 | 1 | 73 | slide_number | - | -
R003 | 4 | 95 | slide_number | - | -
R004 | 4 | 102 | slide_number | - | -
R005 | 4 | 103 | slide_number | - | -
R006 | 5 | 118 | slide_number | - | -
R007 | 5 | 139 | slide_number | - | -
R008 | 7 | 227 | slide_number | - | -
R009 | 7 | 232 | slide_number | - | -
R010 | 8 | 248 | slide_number | - | -
R011 | 8 | 264 | slide_number | - | -
R012 | 8 | 264 | slide_number | - | -
R013 | 8 | 264 | slide_number | - | -
R014 | 10 | 289 | slide_number | - | -
R015 | 10 | 290 | slide_number | - | -
R016 | 10 | 304 | slide_number | - | -
R017 | 11 | 328 | slide_number | - | -
R018 | 13 | 357 | slide_number | - | -
R019 | 13 | 376 | slide_number | - | -
R020 | 13 | 382 | slide_number | - | -
R021 | 15 | 401 | slide_number | RESTATED | same value also at R037
R022 | 15 | 401 | slide_number | RESTATED | same value also at R043
R023 | 15 | 401 | slide_number | RESTATED | same value also at R046
R024 | 15 | 406 | slide_number | RESTATED | same value also at R058
R025 | 15 | 406 | slide_number | - | -
R026 | 15 | 406 | slide_number | - | -
R027 | 15 | 416 | slide_number | RESTATED | same value also at R075,R115,R283
R028 | 15 | 416 | slide_number | RESTATED | same value also at R081,R123,R287
R029 | 15 | 416 | slide_number | RESTATED | same value also at R084,R127
R030 | 15 | 421 | slide_number | RESTATED | same value also at R095,R143
R031 | 15 | 421 | slide_number | RESTATED | same value also at R291
R032 | 15 | 421 | slide_number | - | -
R033 | 15 | 401 | slide_number | - | -
R034 | 15 | 405 | slide_number | - | -
R035 | 15 | 411 | slide_number | - | -
R036 | 15 | 411 | slide_number | - | -
R037 | 16 | 431 | slide_number+line_item | LAYOUT_OFFSET,RESTATED | same value also at R021
R038 | 16 | 431 | slide_number+line_item | LAYOUT_OFFSET | -
R039 | 16 | 431 | slide_number+line_item | LAYOUT_OFFSET | -
R040 | 16 | 432 | slide_number+line_item | LAYOUT_OFFSET | -
R041 | 16 | 432 | slide_number+line_item | LAYOUT_OFFSET | -
R042 | 16 | 432 | slide_number+line_item | LAYOUT_OFFSET | -
R043 | 16 | 433 | slide_number+line_item | LAYOUT_OFFSET,RESTATED | same value also at R022
R044 | 16 | 433 | slide_number+line_item | LAYOUT_OFFSET | -
R045 | 16 | 433 | slide_number+line_item | LAYOUT_OFFSET | -
R046 | 16 | 434 | slide_number+line_item | LAYOUT_OFFSET,RESTATED | same value also at R023
R047 | 16 | 434 | slide_number+line_item | LAYOUT_OFFSET | -
R048 | 16 | 434 | slide_number+line_item | LAYOUT_OFFSET | -
R049 | 16 | 435 | slide_number+line_item | LAYOUT_OFFSET | -
R050 | 16 | 435 | slide_number+line_item | LAYOUT_OFFSET | -
R051 | 16 | 435 | slide_number+line_item | LAYOUT_OFFSET | -
R052 | 16 | 436 | slide_number+line_item | LAYOUT_OFFSET | -
R053 | 16 | 436 | slide_number+line_item | LAYOUT_OFFSET | -
R054 | 16 | 436 | slide_number+line_item | LAYOUT_OFFSET | -
R055 | 16 | 437 | slide_number+line_item | LAYOUT_OFFSET | -
R056 | 16 | 437 | slide_number+line_item | LAYOUT_OFFSET | -
R057 | 16 | 437 | slide_number+line_item | LAYOUT_OFFSET | -
R058 | 16 | 438 | slide_number+line_item | LAYOUT_OFFSET,RESTATED | same value also at R024
R059 | 16 | 438 | slide_number+line_item | LAYOUT_OFFSET | -
R060 | 16 | 438 | slide_number+line_item | LAYOUT_OFFSET | -
R061 | 16 | 439 | slide_number+line_item | LAYOUT_OFFSET | -
R062 | 16 | 439 | slide_number+line_item | LAYOUT_OFFSET | -
R063 | 16 | 439 | slide_number+line_item | LAYOUT_OFFSET | -
R064 | 16 | 440 | slide_number+line_item | LAYOUT_OFFSET | -
R065 | 16 | 440 | slide_number+line_item | LAYOUT_OFFSET | -
R066 | 16 | 440 | slide_number+line_item | LAYOUT_OFFSET | -
R067 | 16 | 441 | slide_number+line_item | LAYOUT_OFFSET | -
R068 | 16 | 441 | slide_number+line_item | LAYOUT_OFFSET | -
R069 | 16 | 441 | slide_number+line_item | LAYOUT_OFFSET | -
R070 | 16 | 442 | slide_number+line_item | LAYOUT_OFFSET | -
R071 | 16 | 442 | slide_number+line_item | LAYOUT_OFFSET | -
R072 | 16 | 443 | slide_number+line_item | LAYOUT_OFFSET | -
R073 | 16 | 443 | slide_number+line_item | LAYOUT_OFFSET | -
R074 | 16 | 443 | slide_number+line_item | LAYOUT_OFFSET | -
R075 | 17 | 451 | slide_number+line_item | LAYOUT_OFFSET,RESTATED | same value also at R027,R115,R283
R076 | 17 | 451 | slide_number+line_item | LAYOUT_OFFSET | -
R077 | 17 | 451 | slide_number+line_item | LAYOUT_OFFSET | -
R078 | 17 | 452 | slide_number+line_item | LAYOUT_OFFSET,RESTATED | same value also at R119
R079 | 17 | 452 | slide_number+line_item | LAYOUT_OFFSET | -
R080 | 17 | 452 | slide_number+line_item | LAYOUT_OFFSET | -
R081 | 17 | 453 | slide_number+line_item | LAYOUT_OFFSET,RESTATED | same value also at R028,R123,R287
R082 | 17 | 453 | slide_number+line_item | LAYOUT_OFFSET | -
R083 | 17 | 453 | slide_number+line_item | LAYOUT_OFFSET | -
R084 | 17 | 454 | slide_number+line_item | LAYOUT_OFFSET,RESTATED | same value also at R029,R127
R085 | 17 | 454 | slide_number+line_item | LAYOUT_OFFSET | -
R086 | 17 | 454 | slide_number+line_item | LAYOUT_OFFSET | -
R087 | 17 | 455 | slide_number+line_item | LAYOUT_OFFSET,RESTATED | same value also at R131
R088 | 17 | 455 | slide_number+line_item | LAYOUT_OFFSET | -
R089 | 17 | 456 | slide_number+line_item | LAYOUT_OFFSET,RESTATED | same value also at R135
R090 | 17 | 456 | slide_number+line_item | LAYOUT_OFFSET | -
R091 | 17 | 456 | slide_number+line_item | LAYOUT_OFFSET | -
R092 | 17 | 457 | slide_number+line_item | LAYOUT_OFFSET,RESTATED | same value also at R139
R093 | 17 | 457 | slide_number+line_item | LAYOUT_OFFSET | -
R094 | 17 | 457 | slide_number+line_item | LAYOUT_OFFSET | -
R095 | 17 | 458 | slide_number+line_item | LAYOUT_OFFSET,RESTATED | same value also at R030,R143
R096 | 17 | 458 | slide_number+line_item | LAYOUT_OFFSET | -
R097 | 17 | 458 | slide_number+line_item | LAYOUT_OFFSET | -
R098 | 17 | 459 | slide_number+line_item | LAYOUT_OFFSET,RESTATED | same value also at R147
R099 | 17 | 459 | slide_number+line_item | LAYOUT_OFFSET | -
R100 | 17 | 459 | slide_number+line_item | LAYOUT_OFFSET | -
R101 | 17 | 460 | slide_number+line_item | LAYOUT_OFFSET,RESTATED | same value also at R151
R102 | 17 | 460 | slide_number+line_item | LAYOUT_OFFSET | -
R103 | 17 | 460 | slide_number+line_item | LAYOUT_OFFSET | -
R104 | 17 | 461 | slide_number+line_item | LAYOUT_OFFSET,RESTATED | same value also at R155
R105 | 17 | 461 | slide_number+line_item | LAYOUT_OFFSET | -
R106 | 17 | 461 | slide_number+line_item | LAYOUT_OFFSET | -
R107 | 17 | 462 | slide_number+line_item | LAYOUT_OFFSET,RESTATED | same value also at R163
R108 | 17 | 462 | slide_number+line_item | LAYOUT_OFFSET | -
R109 | 17 | 463 | slide_number+line_item | LAYOUT_OFFSET,RESTATED | same value also at R167
R110 | 17 | 463 | slide_number+line_item | LAYOUT_OFFSET | -
R111 | 17 | 463 | slide_number+line_item | LAYOUT_OFFSET | -
R112 | 18 | 471 | slide_number+line_item | RESTATED | same value also at R280
R113 | 18 | 471 | slide_number+line_item | RESTATED | same value also at R281
R114 | 18 | 471 | slide_number+line_item | RESTATED | same value also at R282
R115 | 18 | 471 | slide_number+line_item | RESTATED | same value also at R027,R075,R283
R116 | 18 | 473 | slide_number+line_item | - | -
R117 | 18 | 473 | slide_number+line_item | - | -
R118 | 18 | 473 | slide_number+line_item | - | -
R119 | 18 | 473 | slide_number+line_item | RESTATED | same value also at R078
R120 | 18 | 475 | slide_number+line_item | RESTATED | same value also at R284
R121 | 18 | 475 | slide_number+line_item | RESTATED | same value also at R285
R122 | 18 | 475 | slide_number+line_item | RESTATED | same value also at R286
R123 | 18 | 475 | slide_number+line_item | RESTATED | same value also at R028,R081,R287
R124 | 18 | 477 | slide_number+line_item | - | -
R125 | 18 | 477 | slide_number+line_item | - | -
R126 | 18 | 477 | slide_number+line_item | - | -
R127 | 18 | 477 | slide_number+line_item | RESTATED | same value also at R029,R084
R128 | 18 | 479 | slide_number+line_item | - | -
R129 | 18 | 479 | slide_number+line_item | - | -
R130 | 18 | 479 | slide_number+line_item | - | -
R131 | 18 | 479 | slide_number+line_item | RESTATED | same value also at R087
R132 | 18 | 481 | slide_number+line_item | - | -
R133 | 18 | 481 | slide_number+line_item | - | -
R134 | 18 | 481 | slide_number+line_item | - | -
R135 | 18 | 481 | slide_number+line_item | RESTATED | same value also at R089
R136 | 18 | 483 | slide_number+line_item | - | -
R137 | 18 | 483 | slide_number+line_item | - | -
R138 | 18 | 483 | slide_number+line_item | - | -
R139 | 18 | 483 | slide_number+line_item | RESTATED | same value also at R092
R140 | 18 | 485 | slide_number+line_item | - | -
R141 | 18 | 485 | slide_number+line_item | - | -
R142 | 18 | 485 | slide_number+line_item | - | -
R143 | 18 | 485 | slide_number+line_item | RESTATED | same value also at R030,R095
R144 | 18 | 487 | slide_number+line_item | - | -
R145 | 18 | 487 | slide_number+line_item | - | -
R146 | 18 | 487 | slide_number+line_item | - | -
R147 | 18 | 487 | slide_number+line_item | RESTATED | same value also at R098
R148 | 18 | 489 | slide_number+line_item | - | -
R149 | 18 | 489 | slide_number+line_item | - | -
R150 | 18 | 489 | slide_number+line_item | - | -
R151 | 18 | 489 | slide_number+line_item | RESTATED | same value also at R101
R152 | 18 | 491 | slide_number+line_item | - | -
R153 | 18 | 491 | slide_number+line_item | - | -
R154 | 18 | 491 | slide_number+line_item | - | -
R155 | 18 | 491 | slide_number+line_item | RESTATED | same value also at R104
R156 | 18 | 492 | slide_number+line_item | ZERO_STANDING,LAYOUT_ORDER | -
R157 | 18 | 492 | slide_number+line_item | ZERO_STANDING,LAYOUT_ORDER | -
R158 | 18 | 492 | slide_number+line_item | LAYOUT_ORDER | -
R159 | 18 | 492 | slide_number+line_item | ZERO_STANDING,LAYOUT_ORDER | -
R160 | 18 | 493 | slide_number+line_item | LAYOUT_ORDER | -
R161 | 18 | 493 | slide_number+line_item | LAYOUT_ORDER | -
R162 | 18 | 493 | slide_number+line_item | LAYOUT_ORDER | -
R163 | 18 | 493 | slide_number+line_item | LAYOUT_ORDER,RESTATED | same value also at R107
R164 | 18 | 498 | slide_number+line_item | - | -
R165 | 18 | 498 | slide_number+line_item | - | -
R166 | 18 | 498 | slide_number+line_item | - | -
R167 | 18 | 498 | slide_number+line_item | RESTATED | same value also at R109
R168 | 18 | 500 | slide_number+line_item | - | -
R169 | 18 | 500 | slide_number+line_item | - | -
R170 | 18 | 500 | slide_number+line_item | - | -
R171 | 18 | 500 | slide_number+line_item | - | EPS asterisk pair R171/R443/R444 (* Not annualized)
R172 | 19 | 510 | slide_number+line_item | - | -
R173 | 19 | 510 | slide_number+line_item | - | -
R174 | 19 | 510 | slide_number+line_item | - | -
R175 | 19 | 511 | slide_number+line_item | - | -
R176 | 19 | 511 | slide_number+line_item | - | -
R177 | 19 | 511 | slide_number+line_item | - | -
R178 | 19 | 512 | slide_number+line_item | - | -
R179 | 19 | 512 | slide_number+line_item | - | -
R180 | 19 | 513 | slide_number+line_item | ZERO_STANDING | value 0 standing line item; A1 did not flag, A2 added
R181 | 19 | 514 | slide_number+line_item | - | -
R182 | 19 | 514 | slide_number+line_item | ZERO_STANDING | value 0 standing line item; A1 did not flag, A2 added
R183 | 19 | 514 | slide_number+line_item | ZERO_STANDING | value 0 standing line item; A1 did not flag, A2 added
R184 | 19 | 515 | slide_number+line_item | ZERO_STANDING | header row dash, FY25/FY26
R185 | 19 | 515 | slide_number+line_item | ZERO_STANDING | header row dash, FY25/FY26
R186 | 19 | 516 | slide_number+line_item | ORDER_INFERRED | -
R187 | 19 | 516 | slide_number+line_item | ORDER_INFERRED | -
R188 | 19 | 516 | slide_number+line_item | ORDER_INFERRED | -
R189 | 19 | 517 | slide_number+line_item | ORDER_INFERRED | -
R190 | 19 | 517 | slide_number+line_item | ORDER_INFERRED | -
R191 | 19 | 517 | slide_number+line_item | ORDER_INFERRED | -
R192 | 19 | 518 | slide_number+line_item | ORDER_INFERRED | -
R193 | 19 | 518 | slide_number+line_item | ORDER_INFERRED | -
R194 | 19 | 519 | slide_number+line_item | ORDER_INFERRED | -
R195 | 19 | 519 | slide_number+line_item | ORDER_INFERRED | -
R196 | 19 | 519 | slide_number+line_item | ORDER_INFERRED | -
R197 | 19 | 521 | slide_number+line_item | ORDER_INFERRED | -
R198 | 19 | 521 | slide_number+line_item | ORDER_INFERRED | -
R199 | 19 | 521 | slide_number+line_item | ORDER_INFERRED | -
R200 | 19 | 523 | slide_number+line_item | ORDER_INFERRED | -
R201 | 19 | 523 | slide_number+line_item | ORDER_INFERRED | -
R202 | 19 | 523 | slide_number+line_item | ORDER_INFERRED | -
R203 | 19 | 524 | slide_number+line_item | ORDER_INFERRED | -
R204 | 19 | 524 | slide_number+line_item | ORDER_INFERRED | -
R205 | 19 | 524 | slide_number+line_item | ORDER_INFERRED | -
R206 | 19 | 525 | slide_number+line_item | ORDER_INFERRED | -
R207 | 19 | 525 | slide_number+line_item | ORDER_INFERRED | -
R208 | 19 | 525 | slide_number+line_item | ORDER_INFERRED | -
R209 | 19 | 527 | slide_number+line_item | ORDER_INFERRED | -
R210 | 19 | 527 | slide_number+line_item | ORDER_INFERRED | -
R211 | 19 | 527 | slide_number+line_item | ORDER_INFERRED | -
R212 | 19 | 528 | slide_number+line_item | - | -
R213 | 19 | 528 | slide_number+line_item | - | -
R214 | 19 | 528 | slide_number+line_item | - | -
R215 | 19 | 510 | slide_number+line_item | - | -
R216 | 19 | 510 | slide_number+line_item | - | -
R217 | 19 | 510 | slide_number+line_item | - | -
R218 | 19 | 512 | slide_number+line_item | - | -
R219 | 19 | 512 | slide_number+line_item | - | -
R220 | 19 | 512 | slide_number+line_item | - | -
R221 | 19 | 513 | slide_number+line_item | ORDER_INFERRED | -
R222 | 19 | 513 | slide_number+line_item | ORDER_INFERRED | -
R223 | 19 | 513 | slide_number+line_item | ORDER_INFERRED | -
R224 | 19 | 515 | slide_number+line_item | ZERO_STANDING | -
R225 | 19 | 515 | slide_number+line_item | ZERO_STANDING | -
R226 | 19 | 515 | slide_number+line_item | ZERO_STANDING | -
R227 | 19 | 517 | slide_number+line_item | ORDER_INFERRED | -
R228 | 19 | 517 | slide_number+line_item | ORDER_INFERRED | -
R229 | 19 | 517 | slide_number+line_item | ORDER_INFERRED | -
R230 | 19 | 518 | slide_number+line_item | ORDER_INFERRED | -
R231 | 19 | 518 | slide_number+line_item | ORDER_INFERRED | -
R232 | 19 | 518 | slide_number+line_item | ORDER_INFERRED | -
R233 | 19 | 519 | slide_number+line_item | ORDER_INFERRED | -
R234 | 19 | 519 | slide_number+line_item | ORDER_INFERRED | -
R235 | 19 | 519 | slide_number+line_item | ORDER_INFERRED | -
R236 | 19 | 519 | slide_number+line_item | ORDER_INFERRED | -
R237 | 19 | 521 | slide_number+line_item | ORDER_INFERRED | -
R238 | 19 | 521 | slide_number+line_item | ORDER_INFERRED | -
R239 | 19 | 521 | slide_number+line_item | ORDER_INFERRED | -
R240 | 19 | 522 | slide_number+line_item | ORDER_INFERRED | -
R241 | 19 | 522 | slide_number+line_item | ORDER_INFERRED | -
R242 | 19 | 522 | slide_number+line_item | ORDER_INFERRED | -
R243 | 19 | 523 | slide_number+line_item | ORDER_INFERRED | -
R244 | 19 | 523 | slide_number+line_item | ORDER_INFERRED | -
R245 | 19 | 523 | slide_number+line_item | ORDER_INFERRED | -
R246 | 19 | 524 | slide_number+line_item | ORDER_INFERRED | -
R247 | 19 | 524 | slide_number+line_item | ORDER_INFERRED | -
R248 | 19 | 524 | slide_number+line_item | ORDER_INFERRED | -
R249 | 19 | 525 | slide_number+line_item | ORDER_INFERRED | -
R250 | 19 | 525 | slide_number+line_item | ORDER_INFERRED | -
R251 | 19 | 525 | slide_number+line_item | ORDER_INFERRED | -
R252 | 19 | 526 | slide_number+line_item | ORDER_INFERRED | -
R253 | 19 | 527 | slide_number+line_item | ORDER_INFERRED | -
R254 | 19 | 527 | slide_number+line_item | ORDER_INFERRED | -
R255 | 19 | 527 | slide_number+line_item | ORDER_INFERRED | -
R256 | 19 | 531 | slide_number+line_item | - | -
R257 | 19 | 531 | slide_number+line_item | - | -
R258 | 19 | 531 | slide_number+line_item | - | -
R259 | 20 | 537 | slide_number+line_item | - | -
R260 | 20 | 537 | slide_number+line_item | - | -
R261 | 20 | 537 | slide_number+line_item | - | -
R262 | 20 | 538 | slide_number+line_item | - | -
R263 | 20 | 538 | slide_number+line_item | - | -
R264 | 20 | 538 | slide_number+line_item | - | -
R265 | 20 | 539 | slide_number+line_item | - | -
R266 | 20 | 539 | slide_number+line_item | - | -
R267 | 20 | 539 | slide_number+line_item | - | -
R268 | 20 | 540 | slide_number+line_item | - | -
R269 | 20 | 540 | slide_number+line_item | - | -
R270 | 20 | 540 | slide_number+line_item | - | -
R271 | 20 | 541 | slide_number+line_item | ZERO_STANDING,LAYOUT_ORDER | dash net change in cash; FY25 flows sum to 0 (-168-255+423), A3 to check FY26/H1
R272 | 20 | 541 | slide_number+line_item | ZERO_STANDING,LAYOUT_ORDER | dash net change in cash; FY25 flows sum to 0 (-168-255+423), A3 to check FY26/H1
R273 | 20 | 541 | slide_number+line_item | ZERO_STANDING,LAYOUT_ORDER | dash net change in cash; FY25 flows sum to 0 (-168-255+423), A3 to check FY26/H1
R274 | 20 | 542 | slide_number+line_item | LAYOUT_ORDER | -
R275 | 20 | 542 | slide_number+line_item | LAYOUT_ORDER | -
R276 | 20 | 542 | slide_number+line_item | LAYOUT_ORDER | -
R277 | 21 | 549 | slide_number | - | -
R278 | 21 | 564 | slide_number | - | -
R279 | 21 | 566 | slide_number | - | -
R280 | 22 | 584 | slide_number (chart data label) | RESTATED | same value also at R112
R281 | 22 | 584 | slide_number (chart data label) | RESTATED | same value also at R113
R282 | 22 | 584 | slide_number (chart data label) | RESTATED | same value also at R114
R283 | 22 | 584 | slide_number (chart data label) | RESTATED | same value also at R027,R075,R115
R284 | 22 | 584 | slide_number (chart data label) | CHART_POSITION_INFERRED,RESTATED | same value also at R120
R285 | 22 | 584 | slide_number (chart data label) | CHART_POSITION_INFERRED,RESTATED | same value also at R121
R286 | 22 | 584 | slide_number (chart data label) | CHART_POSITION_INFERRED,RESTATED | same value also at R122
R287 | 22 | 584 | slide_number (chart data label) | CHART_POSITION_INFERRED,RESTATED | same value also at R028,R081,R123
R288 | 22 | 584 | slide_number (chart data label) | CHART_POSITION_INFERRED | -
R289 | 22 | 584 | slide_number (chart data label) | CHART_POSITION_INFERRED | -
R290 | 22 | 584 | slide_number (chart data label) | CHART_POSITION_INFERRED | -
R291 | 22 | 584 | slide_number (chart data label) | CHART_POSITION_INFERRED,RESTATED | same value also at R031
R292 | 22 | 598 | slide_number (chart data label) | CHART_POSITION_INFERRED | -
R293 | 22 | 598 | slide_number (chart data label) | CHART_POSITION_INFERRED | -
R294 | 22 | 598 | slide_number (chart data label) | CHART_POSITION_INFERRED | -
R295 | 22 | 598 | slide_number (chart data label) | CHART_POSITION_INFERRED | -
R296 | 22 | 600 | slide_number (chart data label) | CHART_POSITION_INFERRED | -
R297 | 22 | 600 | slide_number (chart data label) | CHART_POSITION_INFERRED | -
R298 | 22 | 600 | slide_number (chart data label) | CHART_POSITION_INFERRED | -
R299 | 22 | 600 | slide_number (chart data label) | CHART_POSITION_INFERRED | -
R300 | 22 | 598 | slide_number (chart data label) | CHART_UNASSIGNED | ROCE/ROE series/period unassigned; do not resolve
R301 | 22 | 598 | slide_number (chart data label) | CHART_UNASSIGNED | ROCE/ROE series/period unassigned; do not resolve
R302 | 22 | 598 | slide_number (chart data label) | CHART_UNASSIGNED | ROCE/ROE series/period unassigned; do not resolve
R303 | 22 | 598 | slide_number (chart data label) | CHART_UNASSIGNED | ROCE/ROE series/period unassigned; do not resolve
R304 | 22 | 605 | slide_number (chart data label) | CHART_UNASSIGNED | ROCE/ROE series/period unassigned; do not resolve
R305 | 22 | 605 | slide_number (chart data label) | CHART_UNASSIGNED | ROCE/ROE series/period unassigned; do not resolve
R306 | 22 | 605 | slide_number (chart data label) | CHART_UNASSIGNED | ROCE/ROE series/period unassigned; do not resolve
R307 | 22 | 592 | slide_number (chart data label) | CHART_UNASSIGNED | ROCE/ROE series/period unassigned; do not resolve
R308 | 23 | 635 | slide_number | - | -
R309 | 23 | 636 | slide_number | - | -
R310 | 23 | 637 | slide_number | - | -
R311 | 23 | 637 | slide_number | - | -
R312 | 23 | 638 | slide_number | - | -
R313 | 23 | 639 | slide_number | - | -
R314 | 23 | 640 | slide_number | - | -
R315 | 23 | 637 | slide_number | LAYOUT_ORDER | -
R316 | 23 | 637 | slide_number | LAYOUT_ORDER | -
R317 | 23 | 640 | slide_number | - | -
R318 | 23 | 642 | slide_number | - | -
R319 | 23 | 622 | slide_number | CHART_POSITION_INFERRED | -
R320 | 23 | 622 | slide_number | CHART_POSITION_INFERRED | -
R321 | 23 | 626 | slide_number | CHART_POSITION_INFERRED | -
R322 | 1 | 19 | slide_entity | - | -
R323 | 1 | 21 | slide_entity | - | -
R324 | 1 | 29 | slide_entity | - | -
R325 | 1 | 32 | slide_entity | - | -
R326 | 1 | 34 | slide_entity | - | -
R327 | 1 | 39 | slide_entity | - | -
R328 | 1 | 40 | slide_entity | - | -
R329 | 1 | 59 | slide_entity | - | -
R330 | 4 | 91 | slide_entity | - | -
R331 | 4 | 89 | slide_entity | - | -
R332 | 4 | 106 | slide_entity | - | -
R333 | 4 | 103 | slide_entity | - | -
R334 | 5 | 116 | slide_entity | - | -
R335 | 5 | 116 | slide_entity | - | -
R336 | 5 | 116 | slide_entity | - | -
R337 | 5 | 116 | slide_entity | - | -
R338 | 5 | 116 | slide_entity | - | -
R339 | 5 | 116 | slide_entity | - | -
R340 | 5 | 116 | slide_entity | - | -
R341 | 5 | 116 | slide_entity | - | -
R342 | 5 | 116 | slide_entity | - | -
R343 | 5 | 116 | slide_entity | - | -
R344 | 5 | 116 | slide_entity | - | -
R345 | 5 | 116 | slide_entity | - | -
R346 | 5 | 116 | slide_entity | - | -
R347 | 5 | 152 | slide_entity | - | -
R348 | 6 | 164 | slide_entity | - | -
R349 | 6 | 159 | slide_entity | - | -
R350 | 6 | 159 | slide_entity | - | -
R351 | 6 | 159 | slide_entity | - | -
R352 | 6 | 159 | slide_entity | - | -
R353 | 6 | 159 | slide_entity | - | -
R354 | 6 | 159 | slide_entity | - | -
R355 | 6 | 159 | slide_entity | - | -
R356 | 6 | 159 | slide_entity | - | -
R357 | 6 | 159 | slide_entity | - | -
R358 | 6 | 159 | slide_entity | - | -
R359 | 6 | 159 | slide_entity | - | -
R360 | 6 | 162 | slide_entity | - | -
R361 | 7 | 199 | slide_entity | - | -
R362 | 7 | 216 | slide_entity | - | -
R363 | 8 | 267 | slide_entity | - | -
R364 | 9 | 274 | slide_entity | - | -
R365 | 10 | 298 | slide_entity | - | -
R366 | 11 | 313 | slide_entity | - | -
R367 | 11 | 324 | slide_entity | - | -
R368 | 13 | 348 | slide_entity | - | -
R369 | 13 | 348 | slide_entity | - | -
R370 | 13 | 362 | slide_entity | - | -
R371 | 13 | 362 | slide_entity | - | -
R372 | 13 | 381 | slide_entity | - | -
R373 | 13 | 381 | slide_entity | - | -
R374 | 13 | 381 | slide_entity | - | -
R375 | 13 | 346 | slide_entity | - | -
R376 | 15 | 408 | slide_entity | - | -
R377 | 23 | 632 | slide_entity | - | -
R378 | 23 | 639 | slide_entity | - | -
R379 | 24 | 646 | slide_entity | - | -
R380 | 24 | 661 | slide_entity | - | -
R381 | 24 | 670 | slide_entity | - | -
R382 | 4 | 95 | slide_forward | - | p4 expansion text garbled; pair R382/R419
R383 | 4 | 97 | slide_forward | - | -
R384 | 6 | 157 | slide_forward | - | -
R385 | 6 | 180 | slide_forward | - | -
R386 | 7 | 237 | slide_forward | - | -
R387 | 11 | 321 | slide_forward | - | -
R388 | 15 | 408 | slide_forward | - | -
R389 | 21 | 549 | slide_forward | - | -
R390 | 21 | 564 | slide_forward | - | -
R391 | 21 | 558 | slide_forward | - | -
R392 | 21 | 558 | slide_forward | - | -
R393 | 21 | 558 | slide_forward | - | -
R394 | 21 | 576 | slide_forward | - | -
R395 | 1 | 31 | slide_date | - | -
R396 | 1 | 45 | slide_date | - | -
R397 | 1 | 48 | slide_date | - | -
R398 | 1 | 69 | slide_date | - | -
R399 | 2 | 79 | slide_date | - | -
R400 | 8 | 264 | slide_date | - | -
R401 | 10 | 304 | slide_date | - | -
R402 | 11 | 336 | slide_date | - | -
R403 | 13 | 350 | slide_date | - | -
R404 | 13 | 375 | slide_date | - | -
R405 | 13 | 390 | slide_date | - | -
R406 | 14 | 392 | slide_date | - | -
R407 | 15 | 399 | slide_date | - | -
R408 | 15 | 414 | slide_date | - | -
R409 | 16 | 427 | slide_date | - | -
R410 | 17 | 447 | slide_date | - | -
R411 | 18 | 469 | slide_date | - | -
R412 | 19 | 508 | slide_date | - | -
R413 | 20 | 535 | slide_date | - | -
R414 | 21 | 547 | slide_date | - | -
R415 | 22 | 580 | slide_date | - | -
R416 | 23 | 617 | slide_date | - | -
R417 | 23 | 634 | slide_date | - | -
R418 | 23 | 626 | slide_date | - | -
R419 | 4 | 97 | footnote/qualifier | LAYOUT_GARBLED | p4 expansion text garbled; pair R382/R419
R420 | 6 | 191 | footnote/qualifier | - | footnote marker/text pair R420/R421 or R426/R427
R421 | 6 | 193 | footnote/qualifier | - | footnote marker/text pair R420/R421 or R426/R427
R422 | 7 | 230 | footnote/qualifier | - | -
R423 | 8 | 260 | footnote/qualifier | - | -
R424 | 10 | 294 | footnote/qualifier | - | -
R425 | 10 | 303 | footnote/qualifier | - | -
R426 | 11 | 331 | footnote/qualifier | - | footnote marker/text pair R420/R421 or R426/R427
R427 | 11 | 336 | footnote/qualifier | - | footnote marker/text pair R420/R421 or R426/R427
R428 | 11 | 319 | footnote/qualifier | - | -
R429 | 13 | 381 | footnote/qualifier | - | -
R430 | 15 | 402 | footnote/qualifier | - | -
R431 | 15 | 405 | footnote/qualifier | - | -
R432 | 15 | 408 | footnote/qualifier | - | -
R433 | 16 | 429 | footnote/qualifier | - | -
R434 | 17 | 449 | footnote/qualifier | - | -
R435 | 16 | 440 | footnote/qualifier | - | -
R436 | 17 | 460 | footnote/qualifier | - | -
R437 | 16 | 432 | footnote/qualifier | - | -
R438 | 16 | 431 | footnote/qualifier | LAYOUT_NOTE | -
R439 | 17 | 451 | footnote/qualifier | LAYOUT_NOTE | -
R440 | 18 | 469 | footnote/qualifier | - | -
R441 | 18 | 489 | footnote/qualifier | - | -
R442 | 18 | 493 | footnote/qualifier | - | -
R443 | 18 | 500 | footnote/qualifier | - | EPS asterisk pair R171/R443/R444 (* Not annualized)
R444 | 18 | 504 | footnote/qualifier | - | EPS asterisk pair R171/R443/R444 (* Not annualized)
R445 | 19 | 508 | footnote/qualifier | - | -
R446 | 19 | 508 | footnote/qualifier | LAYOUT_NOTE | -
R447 | 20 | 535 | footnote/qualifier | - | -
R448 | 21 | 562 | footnote/qualifier | - | -
R449 | 22 | 580 | footnote/qualifier | - | -
R450 | 22 | 611 | footnote/qualifier | CHART_UNASSIGNED | -
R451 | 22 | 582 | footnote/qualifier | - | -
R452 | 23 | 617 | footnote/qualifier | - | -
R453 | 23 | 634 | footnote/qualifier | - | -
R454 | 23 | 640 | footnote/qualifier | - | -
R455 | 23 | 638 | footnote/qualifier | - | -
R456 | 24 | 647 | footnote/qualifier | - | -
R457 | 24 | 662 | footnote/qualifier | - | -

## CORRECTION LOOP 1 ADDENDUM: R458-R512 (A1 appended; 48 QUALIFIER, 7 FORWARD)
ROW_ID | page | line | category | A2 flags | cross-ref / materiality
---|---|---|---|---|---
R458 | page 4 | line 95 | management_claim/policy (QUALIFIER) | RESTATED | restates R003 (30 years)
R459 | page 4 | line 95 | management_claim/policy (QUALIFIER) | - | cross-ref R465,R484,R509
R460 | page 4 | line 102 | management_claim/policy (QUALIFIER) | RESTATED | restates R004/R005 (p4 numbers) and R006/R007 (p5)
R461 | page 4 | line 103 | management_claim/policy (QUALIFIER) | RESTATED | restates R332 (equipment origin)
R462 | page 7 | line 206 | management_claim/policy (QUALIFIER) | CLAIM_TO_TEST | TEST: low-cost secure supply vs raw material cost-driven revenue note R430
R463 | page 7 | line 199 | management_claim/policy (QUALIFIER) | - | -
R464 | page 7 | line 201 | management_claim/policy (QUALIFIER) | DUPLICATE_WORDING | duplicate wording of R482 (p7 vs p10)
R465 | page 7 | line 204 | management_claim/policy (QUALIFIER) | DUPLICATE_WORDING | duplicate wording of R484 (p7 vs p10)
R466 | page 7 | line 209 | management_claim/policy (QUALIFIER) | CLAIM_TO_TEST | TEST: lowest cost producer globally vs EBITDA margin 4.70% FY26, 10.51% Q2 FY27 (R126,R046) and peer evidence NOT FOUND in deck
R467 | page 7 | line 213 | management_claim/policy (QUALIFIER) | - | -
R468 | page 7 | line 216 | management_claim/policy (QUALIFIER) | CLAIM_TO_TEST | TEST: vs margin history R124-R127
R469 | page 7 | line 217 | management_claim/policy (QUALIFIER) | - | -
R470 | page 7 | line 220 | management_claim/policy (QUALIFIER) | - | -
R471 | page 7 | line 226 | management_claim/policy (QUALIFIER) | RESTATED | restates R008 (100+ suppliers)
R472 | page 7 | line 228 | management_claim/policy (QUALIFIER) | RESTATED | restates R422 (500 Km qualifier) and R009
R473 | page 7 | line 229 | management_claim/policy (QUALIFIER) | - | -
R474 | page 7 | line 233 | management_claim/policy (QUALIFIER) | CLAIM_TO_TEST | TEST: short payment cycles vs trade payables R240-R242 and cash conversion cycle 76/82/99/128 days R296-R299
R475 | page 8 | line 243 | management_claim/policy (QUALIFIER) | - | -
R476 | page 8 | line 246 | management_claim/policy (QUALIFIER) | RESTATED | restates R010
R477 | page 8 | line 251 | management_claim/policy (QUALIFIER) | - | -
R478 | page 8 | line 255 | management_claim/policy (QUALIFIER) | - | -
R479 | page 8 | line 257 | management_claim/policy (QUALIFIER) | - | -
R480 | page 8 | line 260 | management_claim/policy (QUALIFIER) | RESTATED | restates R423
R481 | page 10 | line 282 | management_claim/policy (QUALIFIER) | - | -
R482 | page 10 | line 283 | management_claim/policy (QUALIFIER) | DUPLICATE_WORDING | duplicate wording of R464
R483 | page 10 | line 284 | management_claim/policy (QUALIFIER) | CLAIM_TO_TEST | TEST: leadership claim vs R424 scope qualifier
R484 | page 10 | line 285 | management_claim/policy (QUALIFIER) | DUPLICATE_WORDING | duplicate wording of R465
R485 | page 10 | line 288 | management_claim/policy (QUALIFIER) | - | -
R486 | page 10 | line 289 | management_claim/policy (QUALIFIER) | RESTATED | restates R014
R487 | page 10 | line 290 | management_claim/policy (QUALIFIER) | RESTATED | restates R015
R488 | page 10 | line 293 | management_claim/policy (QUALIFIER) | DUPLICATE_WORDING | duplicate theme of R468
R489 | page 10 | line 294 | management_claim/policy (QUALIFIER) | RESTATED | restates R424
R490 | page 10 | line 295 | management_claim/policy (QUALIFIER) | CLAIM_TO_TEST | TEST: market entire quantity vs Q2 revenue -5.2% QoQ (Q2 R021 vs H1 R027 implies Q1 1,762) and inventories R197-R199, receivables R200-R202
R491 | page 10 | line 298 | management_claim/policy (QUALIFIER) | RESTATED | restates R330/R365
R492 | page 10 | line 299 | management_claim/policy (QUALIFIER) | CLAIM_TO_TEST | TEST: cross-ref R388 optimism vs H1 numbers
R493 | page 10 | line 300 | management_claim/policy (QUALIFIER) | - | -
R494 | page 10 | line 303 | management_claim/policy (QUALIFIER) | RESTATED | restates R425; TEST vs borrowings R237-R239 and CFO R262-R264
R495 | page 10 | line 304 | management_claim/policy (QUALIFIER) | RESTATED | restates R016 and R401
R496 | page 10 | line 305 | forward policy statement (FORWARD) | - | policy; TEST vs capex/CWIP R175-R177 and p4 expansion R382/R419
R497 | page 11 | line 313 | management_claim/policy (QUALIFIER) | - | -
R498 | page 11 | line 313 | management_claim/policy (QUALIFIER) | - | environment claim; cross-ref R428 scrubber R387
R499 | page 11 | line 324 | management_claim/policy (QUALIFIER) | - | cross-ref R367 GPCB
R500 | page 11 | line 313 | forward policy statement (FORWARD) | CLAIM_TO_TEST | TEST: adequately capitalized vs Total Equity R221-R223, Net debt/equity R292-R295
R501 | page 11 | line 315 | forward policy statement (FORWARD) | CLAIM_TO_TEST | TEST: not overleverage vs Net debt/equity 0.02/0.20/0.32/0.24 (R292-R295), borrowings R237-R239, finance cost R136-R139
R502 | page 11 | line 316 | forward policy statement (FORWARD) | - | policy; cross-ref R467,R473
R503 | page 11 | line 319 | forward policy statement (FORWARD) | - | policy; cross-ref R331, R393, capex R265-R267
R504 | page 11 | line 320 | forward policy statement (FORWARD) | - | -
R505 | page 11 | line 323 | forward policy statement (FORWARD) | CLAIM_TO_TEST | TEST: low volatility in cash flow vs CFO (168) / 416 / 240 (R262-R264) and CCC R296-R299
R506 | page 11 | line 324 | management_claim/policy (QUALIFIER) | - | -
R507 | page 11 | line 328 | management_claim/policy (QUALIFIER) | RESTATED | restates R017
R508 | page 11 | line 331 | management_claim/policy (QUALIFIER) | RESTATED | restates R426/R427 (footnote (1) fire Nov 2012)
R509 | page 13 | line 344 | management_claim/policy (QUALIFIER) | - | cross-ref board R368-R373
R510 | page 6 | line 173 | management_claim/policy (QUALIFIER) | - | product claims; cross-ref R360
R511 | page 6 | line 180 | management_claim/policy (QUALIFIER) | - | cross-ref R360 furnace oil substitute
R512 | page 6 | line 188 | management_claim/policy (QUALIFIER) | - | cross-ref R357 tocopherols

Slide row deltas (qualifier/forward added): S04 +4Q; S06 +3Q; S07 +13Q; S08 +6Q; S10 +15Q +1F; S11 +6Q +6F; S13 +1Q. Total +48Q +7F = 55. Slide-ledger count columns for these slides in the table above exclude the addendum rows.
