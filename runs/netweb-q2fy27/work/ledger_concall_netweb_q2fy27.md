# A2 LEDGER: concall NETWEB q2fy27 (MACHINE TRANSCRIPT, ASR; all numbers ASR-UNVERIFIED, management tier)

Turn numbering: T1..T20 = the 20 TURN rows in A1 ENTITY table ordered by line (T0 = preamble before line 31). Management answers have no TURN rows of their own; they sit inside the preceding questioner's turn block. Turn number for any row = last TURN row at or before its line.

=== A2 COUNT TEST ===
ids_in_structured: 261 | ids_referenced_in_ledger: 261 | orphan_ids: [] | match: yes
category: participants   grep_count: 8 (R112-R119 attendee/host rows; R120 company)  sweep_count: 8   match: yes
category: turns          grep_count: 20 (grep 'ENTITY | TURN')  sweep_count: 20   match: yes
category: questions      grep_count: 15 (R133-R147 analyst TURN rows)  sweep_count: 15   match: yes (R133 asked, no reply, skipped)
category: numbers_all    grep_count: 111 (header) sweep_count: 111   match: yes
category: mgmt_numbers   grep_count: 90 (111 less 21 analyst-origin)  sweep_count: 90   match: yes
category: forward        grep_count: 44 (header) sweep_count: 44  match: yes
category: dates          grep_count: 27 (header) sweep_count: 27  match: yes
category: qualifiers     grep_count: 31 (header) sweep_count: 31  match: yes
category: entities_total grep_count: 48 (header) sweep_count: 48  match: yes
not applicable (concall): notes, line_items, agenda_items, auditor_paras, slides
gate_a2: pass
=== END COUNT TEST ===

## 1 PARTICIPANTS (R112-R120)
ROW_ID | category | flags | note
R112 | participant |  | host broker
R113 | participant |  | host moderator
R114 | participant |  | CMD (per context); present
R115 | participant |  | full-time director; present
R116 | participant |  | CFO; present
R117 | participant |  | sales/marketing; present
R118 | participant |  | management attendee
R119 | participant |  | IR advisor
R120 | participant |  | company, ASR name variants
MGMT_ABSENCE: none (CMD R114 and director R115 named present; ASR identity uncertain, names garbled)

## 2 SPEAKER TURNS
TURN_NO | ROW_ID | category | flags | note
T1 | R121 | turn | speaker UNIDENTIFIED (ASR) unless named | line 31
T2 | R122 | turn | speaker UNIDENTIFIED (ASR) unless named | line 52
T3 | R123 | turn | speaker UNIDENTIFIED (ASR) unless named | line 160
T4 | R124 | turn | speaker UNIDENTIFIED (ASR) unless named | line 205
T5 | R133 | turn | speaker UNIDENTIFIED (ASR) unless named | line 211
T6 | R134 | turn | speaker UNIDENTIFIED (ASR) unless named | line 214
T7 | R135 | turn | speaker UNIDENTIFIED (ASR) unless named | line 246
T8 | R136 | turn | speaker UNIDENTIFIED (ASR) unless named | line 319
T9 | R137 | turn | speaker UNIDENTIFIED (ASR) unless named | line 349
T10 | R138 | turn | speaker UNIDENTIFIED (ASR) unless named | line 382
T11 | R139 | turn | speaker UNIDENTIFIED (ASR) unless named | line 433
T12 | R140 | turn | speaker UNIDENTIFIED (ASR) unless named | line 465
T13 | R141 | turn | speaker UNIDENTIFIED (ASR) unless named | line 535
T14 | R142 | turn | speaker UNIDENTIFIED (ASR) unless named | line 550
T15 | R143 | turn | speaker UNIDENTIFIED (ASR) unless named | line 572
T16 | R144 | turn | speaker UNIDENTIFIED (ASR) unless named | line 653
T17 | R145 | turn | speaker UNIDENTIFIED (ASR) unless named | line 673
T18 | R146 | turn | speaker UNIDENTIFIED (ASR) unless named | line 695
T19 | R147 | turn | speaker UNIDENTIFIED (ASR) unless named | line 740
T20 | R148 | turn | speaker UNIDENTIFIED (ASR) unless named | line 779

## 3 QUESTIONS (analyst ledger)
TURN_NO | ROW_ID | analyst/firm (per ASR) | topic | flags
T5 | R133 | Mohit Bansal with eternal access capital (no reply, skipped) | questioner | 
T6 | R134 | Shrenik Mehta from Indo-Alts (ASR) | question on non top-5 growth | 
T7 | R135 | Jatin from Bank of America | Taiwan, Vera Rubin questions | REPEAT_QUESTION (Taiwan, also R137)
T8 | R136 | Vinay Menon with Monash Capital (ASR) | gross margin, neoclouds, NSM 2.0 | REPEAT_QUESTION (NSM 2.0 also R142)
T9 | R137 | safe shake with a city pillar (ASR) | Taiwan ODM, working capital questions | REPEAT_QUESTION (Taiwan R135; working capital R143)
T10 | R138 | Sandeep Bisha, Equal Security (ASR) | CXMT/YMTC, multi-model, AI order mix | 
T11 | R139 | Patek Singh with IIFL Capital | 2H revenue question | REPEAT_QUESTION (pipeline/2H conversion with R141,R142)
T12 | R140 | C.A. Garveer Kowal with Sireen Alfa (ASR) | FY28 growth, cost of capital | REPEAT_QUESTION (FY28 growth 30-40% with R141,R146 area)
T13 | R141 | Nishita (firm not stated) | conservatism of 30-40% growth, execution timeline | REPEAT_QUESTION (30-40% growth, pipeline conversion)
T14 | R142 | "from graduation on our report portal" (ASR garble, firm unclear) | pipeline mix, NSM 2.0 share | REPEAT_QUESTION (pipeline mix; NSM 2.0 also R136)
T15 | R143 | Tivesh Mehta with Inlesco India mutual fund (ASR) | cash flow, free cash, CDAC | REPEAT_QUESTION (working capital also R137)
T16 | R144 | Mansimar Singh Sethi at Sethi Capital | HDFC/IDFC First, Nvidia client devices | 
T17 | R145 | Abhinay Menon with Monak Kebutu (ASR) | employee cost, ESOP | 
T18 | R146 | Pradip Nagori, an individual investor | physical AI, quantum, operating leverage | 
T19 | R147 | Basant Bansal with the NBG investment (ASR) | concerns and challenges | 

## 4 MANAGEMENT NUMBERS (turn-tagged; feeds Role 5 arithmetic check)
ROW_ID | category | turn | flags | note
R001 | number | T2 | RESTATED | mgmt; line 56
R002 | number | T2 | RESTATED | mgmt; line 57
R003 | number | T2 |  | mgmt; line 57
R004 | number | T2 |  | mgmt; line 57
R005 | number | T2 | RESTATED | mgmt; line 58
R006 | number | T2 | RESTATED | mgmt; line 58
R007 | number | T2 | RESTATED | mgmt; line 59
R008 | number | T2 | RESTATED | mgmt; line 59
R009 | number | T2 | RESTATED | mgmt; line 59
R010 | number | T2 |  | mgmt; line 59
R011 | number | T2 | RESTATED | mgmt; line 60
R012 | number | T2 | RESTATED | mgmt; line 60
R013 | number | T2 |  | mgmt; line 63
R014 | number | T2 |  | mgmt; line 63
R015 | number | T2 | ASR_GARBLE | mgmt; line 65
R016 | number | T2 |  | mgmt; line 66
R017 | number | T2 |  | mgmt; line 66
R018 | number | T2 | RESTATED | mgmt; line 67
R019 | number | T2 |  | mgmt; line 68
R020 | number | T2 |  | mgmt; line 70
R021 | number | T2 |  | mgmt; line 120
R022 | number | T3 | RESTATED | mgmt; line 163
R023 | number | T3 | RESTATED | mgmt; line 163
R024 | number | T3 |  | mgmt; line 164
R025 | number | T3 | RESTATED | mgmt; line 165
R026 | number | T3 | RESTATED | mgmt; line 165
R027 | number | T3 |  | mgmt; line 165
R028 | number | T3 | RESTATED | mgmt; line 166
R029 | number | T3 | ASR_GARBLE | mgmt; line 166
R030 | number | T3 | RESTATED | mgmt; line 168
R031 | number | T3 |  | mgmt; line 168
R032 | number | T3 |  | mgmt; line 168
R033 | number | T3 | RESTATED | mgmt; line 169
R034 | number | T3 |  | mgmt; line 169
R035 | number | T3 |  | mgmt; line 170
R036 | number | T3 |  | mgmt; line 171
R037 | number | T3 |  | mgmt; line 171
R038 | number | T3 |  | mgmt; line 171
R039 | number | T3 |  | mgmt; line 172
R040 | number | T3 | RESTATED | mgmt; line 172
R041 | number | T3 |  | mgmt; line 172
R042 | number | T3 | ZERO_STANDING | mgmt; line 176
R043 | number | T3 |  | mgmt; line 177
R044 | number | T3 |  | mgmt; line 178
R045 | number | T3 |  | mgmt; line 180
R046 | number | T3 |  | mgmt; line 180
R047 | number | T3 |  | mgmt; line 181
R048 | number | T3 | ASR_CONFLICT | mgmt; line 183
R049 | number | T3 |  | mgmt; line 190
R050 | number | T3 |  | mgmt; line 190
R051 | number | T3 |  | mgmt; line 192
R052 | number | T6 |  | mgmt; line 219
R053 | number | T6 |  | mgmt; line 220
R054 | number | T6 |  | mgmt; line 222
R055 | number | T6 |  | mgmt; line 226
R056 | number | T6 |  | mgmt; line 236
R057 | number | T7 |  | mgmt; line 266
R058 | number | T7 |  | analyst-origin (excluded from mgmt_numbers); line 312
R059 | number | T8 |  | mgmt; line 334
R060 | number | T8 |  | analyst-origin (excluded from mgmt_numbers); line 336
R061 | number | T8 | RESTATED | mgmt; line 344
R062 | number | T8 | RESTATED | mgmt; line 344
R063 | number | T8 |  | mgmt; line 345
R064 | number | T9 |  | mgmt; line 373
R065 | number | T9 |  | mgmt; line 374
R066 | number | T9 |  | analyst-origin (excluded from mgmt_numbers); line 376
R067 | number | T9 |  | analyst-origin (excluded from mgmt_numbers); line 377
R068 | number | T9 |  | mgmt; line 378
R069 | number | T10 |  | mgmt; line 391
R070 | number | T11 | ASR_GARBLE | analyst-origin (excluded from mgmt_numbers); line 440
R071 | number | T11 | ASR_GARBLE | analyst-origin (excluded from mgmt_numbers); line 442
R072 | number | T11 | ASR_GARBLE | analyst-origin (excluded from mgmt_numbers); line 448
R073 | number | T11 |  | mgmt; line 458
R074 | number | T12 |  | analyst-origin (excluded from mgmt_numbers); line 471
R075 | number | T12 |  | analyst-origin (excluded from mgmt_numbers); line 475
R076 | number | T12 |  | mgmt; line 486
R077 | number | T12 |  | mgmt; line 489
R078 | number | T12 |  | mgmt; line 490
R079 | number | T12 |  | mgmt; line 492
R080 | number | T12 |  | mgmt; line 500
R081 | number | T12 |  | mgmt; line 506
R082 | number | T12 |  | analyst-origin (excluded from mgmt_numbers); line 511
R083 | number | T12 |  | mgmt; line 511
R084 | number | T12 |  | mgmt; line 513
R085 | number | T12 |  | mgmt; line 514
R086 | number | T12 |  | mgmt; line 527
R087 | number | T13 |  | analyst-origin (excluded from mgmt_numbers); line 539
R088 | number | T13 |  | analyst-origin (excluded from mgmt_numbers); line 540
R089 | number | T13 |  | analyst-origin (excluded from mgmt_numbers); line 540
R090 | number | T13 |  | analyst-origin (excluded from mgmt_numbers); line 542
R091 | number | T13 |  | analyst-origin (excluded from mgmt_numbers); line 545
R092 | number | T13 |  | mgmt; line 547
R093 | number | T14 |  | mgmt; line 562
R094 | number | T14 |  | mgmt; line 566
R095 | number | T14 |  | mgmt; line 567
R096 | number | T15 |  | analyst-origin (excluded from mgmt_numbers); line 575
R097 | number | T15 |  | analyst-origin (excluded from mgmt_numbers); line 580
R098 | number | T15 |  | mgmt; line 591
R099 | number | T15 | RESTATED | mgmt; line 597
R100 | number | T15 |  | analyst-origin (excluded from mgmt_numbers); line 606
R101 | number | T15 |  | mgmt; line 615
R102 | number | T15 |  | analyst-origin (excluded from mgmt_numbers); line 623
R103 | number | T17 |  | mgmt; line 674
R104 | number | T17 |  | mgmt; line 684
R105 | number | T18 |  | analyst-origin (excluded from mgmt_numbers); line 715
R106 | number | T18 |  | analyst-origin (excluded from mgmt_numbers); line 716
R107 | number | T18 |  | mgmt; line 727
R108 | number | T18 |  | mgmt; line 729
R109 | number | T19 |  | mgmt; line 749
R110 | number | T19 |  | mgmt; line 751
R111 | number | T19 |  | mgmt; line 752
Restated pairs: revenue R005/R022 (1323 cr), YoY R006/R023, EBITDA R007/R025, margin R009/R028, PAT R011/R030, PAT margin R012/R033, H1 PAT R002/R040, order book R018/R099/R062 (2,629 vs R048 26,629 conflict R257), CCC R045/R064, 14%/R059, R108 margin 13-14%, 30-40% growth R079/R091/R093/R186.
ZERO_STANDING: R042 (zero net debt Sep 2026).

## 5 FORWARD COMMITMENTS AND HEDGES
ROW_ID | category | turn | flags | note
R160 | forward | T2 | | line 69
R161 | forward | T2 | | line 72
R162 | forward | T2 | | line 117
R163 | forward | T2 | | line 120
R164 | forward | T2 | | line 137
R165 | forward | T2 | | line 147
R166 | forward | T2 | | line 153
R167 | forward | T2 | | line 155
R168 | forward | T3 | | line 196
R169 | forward | T3 | | line 198
R170 | forward | T7 | | line 268
R171 | forward | T7 | | line 281
R172 | forward | T7 | | line 297
R173 | forward | T7 | | line 295
R174 | forward | T7 | | line 306
R175 | forward | T7 | | line 314
R176 | forward | T8 | | line 326
R177 | forward | T8 | | line 334
R178 | forward | T8 | | line 347
R179 | forward | T9 | | line 368
R180 | forward | T9 | | line 374
R181 | forward | T9 | | line 381
R182 | forward | T10 | | line 391
R183 | forward | T11 | | line 458
R184 | forward | T12 | | line 492
R185 | forward | T12 | | line 501
R186 | forward | T12 | | line 508
R187 | forward | T12 | | line 513
R188 | forward | T12 | | line 532
R189 | forward | T13 | | line 546
R190 | forward | T14 | | line 562
R191 | forward | T14 | | line 566
R192 | forward | T14 | | line 570
R193 | forward | T15 | | line 647
R194 | forward | T15 | | line 631
R195 | forward | T16 | | line 661
R196 | forward | T16 | | line 669
R197 | forward | T17 | | line 692
R198 | forward | T18 | | line 704
R199 | forward | T18 | | line 711
R200 | forward | T18 | | line 724
R201 | forward | T18 | | line 729
R202 | forward | T18 | | line 732
R203 | forward | T19 | | line 757
Hedge/qualifier phrases (QUALIFIER table, same turn rule):
R231 | qualifier/hedge | T0 | ASR_DEFECT | line 24
R232 | qualifier/hedge | T1 | FOOTNOTE_UNRESOLVED | line 48
R233 | qualifier/hedge | T3 | FOOTNOTE_UNRESOLVED | line 165
R234 | qualifier/hedge | T2 |  | line 68
R235 | qualifier/hedge | T8 |  | line 345
R236 | qualifier/hedge | T3 | ASR_DEFECT | line 175
R237 | qualifier/hedge | T3 |  | line 182
R238 | qualifier/hedge | T3 |  | line 191
R239 | qualifier/hedge | T8 |  | line 325
R240 | qualifier/hedge | T8 |  | line 329
R241 | qualifier/hedge | T2 |  | line 124
R242 | qualifier/hedge | T2 |  | line 121
R243 | qualifier/hedge | T6 |  | line 221
R244 | qualifier/hedge | T8 |  | line 340
R245 | qualifier/hedge | T14 |  | line 554
R246 | qualifier/hedge | T13 |  | line 546
R247 | qualifier/hedge | T18 |  | line 729
R248 | qualifier/hedge | T12 |  | line 527
R249 | qualifier/hedge | T15 |  | line 594
R250 | qualifier/hedge | T15 |  | line 611
R251 | qualifier/hedge | T15 |  | line 614
R252 | qualifier/hedge | T10 | ASR_DEFECT | line 427
R253 | qualifier/hedge | T11 | ASR_DEFECT | line 438
R254 | qualifier/hedge | T13 | ASR_DEFECT | line 540
R255 | qualifier/hedge | T15 | ASR_DEFECT | line 580
R256 | qualifier/hedge | T9 | ASR_DEFECT | line 376
R257 | qualifier/hedge | T3 | ASR_DEFECT | line 183
R258 | qualifier/hedge | T7 |  | line 266
R259 | qualifier/hedge | T13 |  | line 548
R260 | qualifier/hedge | T12 | ASR_DEFECT | line 483
R261 | qualifier/hedge | T2 | ASR_DEFECT | line 157

## 6 DATES (R204-R230)
ROW_ID | category | turn | note
R204 | date | T0 | line 24
R205 | date | T1 | line 32
R206 | date | T2 | line 57
R207 | date | T2 | line 57
R208 | date | T2 | line 67
R209 | date | T2 | line 71
R210 | date | T3 | line 177
R211 | date | T3 | line 183
R212 | date | T3 | line 193
R213 | date | T6 | line 219
R214 | date | T6 | line 220
R215 | date | T6 | line 237
R216 | date | T7 | line 307
R217 | date | T7 | line 313
R218 | date | T8 | line 347
R219 | date | T8 | line 344
R220 | date | T11 | line 446
R221 | date | T12 | line 469
R222 | date | T12 | line 477
R223 | date | T12 | line 482
R224 | date | T12 | line 500
R225 | date | T12 | line 511
R226 | date | T9 | line 378
R227 | date | T17 | line 685
R228 | date | T17 | line 688
R229 | date | T17 | line 690
R230 | date | T19 | line 749

## 7 OTHER ENTITIES (non-participant, non-turn)
ROW_ID | category | note
R125 | entity | mention; line 65
R126 | entity | mention; line 63
R127 | entity | mention; line 76
R128 | entity | mention; line 109
R129 | entity | mention; line 131
R130 | entity | mention; line 132
R131 | entity | ENTITY_CHANGE (new Taiwan subsidiary approved, no prior list); line 148
R132 | entity | mention; line 70
R149 | entity | mention; line 335
R150 | entity | mention; line 335
R151 | entity | mention; line 624
R152 | entity | mention; line 289
R153 | entity | mention; line 257
R154 | entity | mention; line 384
R155 | entity | mention; line 354
R156 | entity | mention; line 654
R157 | entity | mention; line 219
R158 | entity | mention; line 505
R159 | entity | mention; line 743

## MISSING_FROM_STRUCTURED
none found (sweep of structured file; fulltext not opened)

```yaml
stage: A2-enumerator
company: "NETWEB"
quarter: "q2fy27"
doctype: "concall"
model: claude-sonnet-5-5
status: complete
ledger_path: "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/qr-netweb-q2fy27-a60c5c/runs/netweb-q2fy27/work/ledger_concall_netweb_q2fy27.md"
counts:
  notes: 0
  line_items: 0
  zero_standing: 1
  agenda_items: 0
  auditor_paras: 0
  entities: 48
  turns: 20
  questions: 15
  mgmt_numbers: 90
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, REPEAT_QUESTION, RESTATED, ASR_CONFLICT, ASR_GARBLE, ENTITY_CHANGE, FOOTNOTE_UNRESOLVED]
ids_in_structured: 261
ids_referenced: 261
orphan_ids: []
missing_from_structured: []
gate_a2: pass
mismatch_note: ""
analyst_note: "Turns: only 20 TURN rows exist (host and analyst boundaries); management answers sit inside the questioner block, so T-numbers locate answers by block, not by separate speaker turn. Management-number count 90 excludes 21 rows tagged analyst-origin by A2 judgement from A1 descriptions (e.g. R058, R060, R066, R074, R087-R091). Order book conflict: R018/R099/R062 say 2,629/2,600 crore, R048 says 26,629 (R257 flags ASR error). R066 '14 days' is likely 84 (R068). R029 and R015 are garbled. R133 asked but unanswered. No prior ledger, so ENTITY_CHANGE on Taiwan subsidiary R131 is a new-entity mention only."
```
