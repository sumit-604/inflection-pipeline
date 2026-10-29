# A2 LEDGER: Larsen & Toubro Limited (LT), Q2 FY27, results filing
Source: runs/lt-q2fy27/extracted/lt-results-q2fy27-structured.md (R001-R2511). Fallback used for the second count method: fulltext (1,963 lines). Prior ledger: none (first LT run). Units Rs crore (x1). Verbatim values stay in the structured file at each ID; this ledger references IDs only (MISSING_FROM_STRUCTURED rows carry their own text and line number).

=== A2 COUNT TEST ===
category: notes           grep_count: 41   sweep_count: 41   match: yes
  grep (fulltext regex): 29 roman-numeral notes (consol (i)-(viii) + segment (I)-(VI); standalone (i)-(ix) + segment (I)-(VI); OCR forms "{111)", "{iv)", "(II}" included) + 4 ratio notes (a)-(d) + 4 CF notes (1,2 consol; 1,2 standalone) + 1 standalone ratio item 15 + 2 "Not material" inventory footnotes + 1 standalone "Note:" formulae = 41
  sweep (ledger section 6): consol 21 = (i),(ii),(iii),(iv),(v),(vi),(vii),(viii), a,b,c,d, not-material, CF1, CF2, seg I-VI; standalone 20 = (i)-(ix), item 15, formulae Note, not-material, CF1, CF2, seg I-VI. Total 41
category: line_items      grep_count: 400  sweep_count: 400  match: yes
  grep = A1 context labels grouped (C_PL 41, C_BS 54, C_SA 4, C_RAT 14, C_CF 57, C_SEG 50, S_PL 32, S_BS 48, S_RAT 14, S_CF 48, S_SEG 38). sweep = fulltext lines carrying numeric cells per table range: identical per table except S_CF (+2 stray "-" continuation lines 1130, 1138 that belong to items on lines 1129, 1137) and S_SEG (one Exceptional items label wraps lines 1210-1211: 39 lines, 38 items). After those two reconciliations 400 = 400. Cell-level sweep: 1,586 numeric tokens vs 1,567 A1 NUMBER cells on pages 11-20; the delta of 19 is token artifacts (hyphens in "Energy - X" labels, sub-total labels, header tokens, prose numbers), none a missed cell.
category: annexure1_items grep_count: 58   sweep_count: 58   match: yes
  grep = A1 labels (8 group metrics, 48 segment metric rows, 2 Note 1-2 rows). sweep = fulltext page 9: 8 group lines (377-384) + Q2 segment table 24 populated metric rows + H1 24 + Notes 1-2 = 58.
category: zero_standing   grep_count: 42   sweep_count: 42   match: yes
  grep = value regex on A1 NUMBER rows (zero, dash, NIL, 0.00): 42 (32 A1-flagged + 10 A2-raised 0.00 cells R648-R652, R1432-R1436). sweep = fulltext cell scan: 24 dash cells pp 11-20 + 2 stray-line dashes (1130, 1138) + 2 Annexure 1 (line 394) + 2 Annexure III (NIL, -) + 2 further dashes on line 1210 + 10 "0.00" tokens = 42.
category: agenda_items    grep_count: 5    sweep_count: 5    match: yes
  grep on lines 19-72: "inter alia, approved", "as Annexure I.", "as Annexure II.", "enclosed as Annexure III", "not applicable" = 5. One board resolution plus four enclosure or disclosure items.
category: auditor_paras   grep_count: 16   sweep_count: 16   match: yes
  grep of numbered paragraph starts on both LRR ranges = 16 (a 17th raw match, line 1335 "6. 94 crore", is an OCR-split decimal). Sweep: consol paras 1-9, standalone paras 1-7. Auditor units incl letterheads and signature blocks = 20.
category: entities        grep_count: 177  sweep_count: 177  match: yes
  Annexure A consolidated: serial-line sweep = 143 (107 serial+name + 36 serial-only) plus Parent line 1428 = 144; A1 holds 143 rows, so the parent is MISSING_FROM_STRUCTURED (MFS-3). Standalone: 32 serials + The Company = 33; A1 holds 33 (R2087-R2119). 144 + 33 = 177 filed entities; A1 rows 176 + 1 MFS = 177.
category: forward_rows    grep_count: 16   sweep_count: 16   match: yes
category: signature_blocks grep_count: 6  sweep_count: 6    match: yes
gate_a2: pass
=== END COUNT TEST ===

ID ACCOUNTABILITY: ids_in_structured: 2511 | ids_referenced_in_ledger: 2511 | orphan_ids: [] | match: yes
(Method: ledger ID tokens and ranges were re-expanded from this file after writing and compared with the full A1 ID set. Some IDs also appear in the section 11 indexes (zero standing, forward, restated), so a distinct-ID count is reported.)
Flags used: ZERO_STANDING, ENTITY_CHANGE, LIQUIDATION, RESTATED, BASIS_DIFFERENCE, MISSING_FROM_STRUCTURED, SIGNATURE_TIMESTAMP, MGMT_FURNISHED_UNREVIEWED, OTHER_AUDITOR_RELIED, UDIN_OCR_GARBLED, HEADING_ONLY, NO_OWN_ROW, plus A1 flags carried (RECONSTRUCTED_FROM_RENDER, NOT_APPLICABLE, PARTIAL_COLS, FOOTNOTE_MARKER*).

## 1. BOARD OUTCOME LETTER: agenda items and times
ROW_ID(s) | category | A2 flags | cross-ref / materiality note
R1885-R1887, R2140 | letter_frame | - | Board Outcome letter: header, addressee, subject (meeting of 27-Oct-2026); lines 20-39; A1 types DAT1 ENT3
R2141 | letter_frame | - | Board Outcome letter: prior intimation letter reference; lines 41; A1 types DAT1
R1888, R2142-R2144 | agenda_item | only substantive resolution | AGENDA ITEM 1: approval of consolidated and standalone unaudited results, quarter and half-year; lines 42-46; A1 types DAT3 ENT1
R2145 | agenda_item | - | AGENDA ITEM 2: Press Release enclosed as Annexure I; lines 49; A1 types DAT1
R1889, R2146, R2371 | agenda_item | - | AGENDA ITEM 3: Limited Review Report enclosed as Annexure II; lines 52-53; A1 types DAT1 ENT1 QUA1
R1890, R2147-R2148, R2372 | agenda_item | - | AGENDA ITEM 4: Statement of utilisation / deviation, Reg 52(7), 52(7A), Annexure III; lines 56-59; A1 types DAT2 ENT1 QUA1
R1891, R2149, R2373 | agenda_item | - | AGENDA ITEM 5: Reg 54(2), 54(3) security cover disclosure not applicable; lines 61-64; A1 types DAT1 ENT1 QUA1
R2150-R2151 | meeting_time | DURATION 2h45m (14:00 to 16:45) | Board meeting start and end times; lines 82; A1 types DAT2
AGENDA ABSENCE (silence signals; nothing to reference): no AR approval, AGM notice, record date, dividend, director appointment or cessation, auditor change, scrutinizer, ESOP grant, or capital-raising enabling resolution appears in the letter.

## 2. SIGNATURE BLOCKS
ROW_ID(s) | category | A2 flags | cross-ref / materiality note
R1892 | signature_block | - | Signature block: Company Secretary (digital), Board Outcome letter; lines 90
R2255 | signature_block | - | Signature block: CMD, consolidated results (page 14); lines 781
R2264-R2265 | signature_block | - | Signature block: CMD, consolidated segment page (page 15); lines 891
R2296 | signature_block | - | Signature block: CMD, standalone results (page 19); lines 1176
R2305 | signature_block | - | Signature block: CMD, standalone segment page (page 20); lines 1270
R2123, R2370 | signature_block | - | Signature block: Company Secretary, Annexure III (page 33); lines 1952-1955
Statement signature blocks (CMD S.N. Subrahmanyan, Mumbai, October 27, 2026) at pages 14, 15, 19, 20 are covered above; no signature timestamp on those pages.

## 3. PRESS RELEASE (pages 3-8), grouped by page and A1 type
ROW_ID(s) | category | A2 flags | cross-ref / materiality note
R001-R020 | press_release/number | - | Press release page 3 (headline, group revenue, PAT, order inflow); 20 rows; lines 118-144
R1893 | press_release/entity | - | Press release page 3 (headline, group revenue, PAT, order inflow); 1 rows; lines 128
R2152-R2158 | press_release/date | - | Press release page 3 (headline, group revenue, PAT, order inflow); 7 rows; lines 116-145
R2374 | press_release/qualifier | - | Press release page 3 (headline, group revenue, PAT, order inflow); 1 rows; lines 128
R021-R030 | press_release/number | - | Press release page 4 (orders, order book, CMD statement); 10 rows; lines 152-167
R1894-R1899 | press_release/entity | - | Press release page 4 (orders, order book, CMD statement); 6 rows; lines 151-161
R2124-R2126 | press_release/forward | - | Press release page 4 (orders, order book, CMD statement); 3 rows; lines 166-172
R2159-R2161 | press_release/date | - | Press release page 4 (orders, order book, CMD statement); 3 rows; lines 154-159
R2375 | press_release/qualifier | - | Press release page 4 (orders, order book, CMD statement); 1 rows; lines 158
R031-R050 | press_release/number | - | Press release page 5 (Infrastructure & Utilities; Energy - Conventional); 20 rows; lines 188-223
R1900-R1903 | press_release/entity | - | Press release page 5 (Infrastructure & Utilities; Energy - Conventional); 4 rows; lines 186-211
R2162-R2170 | press_release/date | - | Press release page 5 (Infrastructure & Utilities; Energy - Conventional); 9 rows; lines 182-222
R2376-R2377 | press_release/qualifier | - | Press release page 5 (Infrastructure & Utilities; Energy - Conventional); 2 rows; lines 181-184
R051-R075 | press_release/number | - | Press release page 6 (Energy - Green; Manufacturing & Products; Technology, Platforms & Services); 25 rows; lines 232-277
R1904-R1910 | press_release/entity | - | Press release page 6 (Energy - Green; Manufacturing & Products; Technology, Platforms & Services); 7 rows; lines 230-273
R2171-R2181 | press_release/date | - | Press release page 6 (Energy - Green; Manufacturing & Products; Technology, Platforms & Services); 11 rows; lines 233-277
R2378-R2379 | press_release/qualifier | - | Press release page 6 (Energy - Green; Manufacturing & Products; Technology, Platforms & Services); 2 rows; lines 253-273
R076-R090 | press_release/number | - | Press release page 7 (Financial Services; Realty; Development Projects); 15 rows; lines 287-325
R1911-R1917 | press_release/entity | - | Press release page 7 (Financial Services; Realty; Development Projects); 7 rows; lines 285-322
R2127-R2128 | press_release/forward | - | Press release page 7 (Financial Services; Realty; Development Projects); 2 rows; lines 305-325
R2182-R2193 | press_release/date | - | Press release page 7 (Financial Services; Realty; Development Projects); 12 rows; lines 288-324
R2380-R2382 | press_release/qualifier | - | Press release page 7 (Financial Services; Realty; Development Projects); 3 rows; lines 287-319
R091-R095 | press_release/number | WRITTEN_NUMBER | Press release page 8 (Outlook; media contact); 5 rows; lines 340-363
R1918-R1919 | press_release/entity | - | Press release page 8 (Outlook; media contact); 2 rows; lines 340-366
R2129-R2132 | press_release/forward | - | Press release page 8 (Outlook; media contact); 4 rows; lines 337-352
R2194-R2195 | press_release/date | - | Press release page 8 (Outlook; media contact); 2 rows; lines 332-344
RESTATED cross-refs (press release vs statements vs Annexure 1): see section 11c.

## 4. ANNEXURE 1 (page 9): one row per metric; ANNEXURE 2 (page 10)
ROW_ID(s) | category | A2 flags | cross-ref / materiality note
R096-R101 | annexure1_item | - | Annexure 1 group: Revenue from operations; 6 cells; line 377
R102-R105 | annexure1_item | - | Annexure 1 group: International revenue %; 4 cells; line 378
R106-R111 | annexure1_item | - | Annexure 1 group: Total operational expenses; 6 cells; line 379
R112-R117 | annexure1_item | - | Annexure 1 group: EBITDA; 6 cells; line 380
R118-R121 | annexure1_item | - | Annexure 1 group: EBITDA %; 4 cells; line 381
R122-R127 | annexure1_item | - | Annexure 1 group: Finance costs; 6 cells; line 382
R128-R133 | annexure1_item | - | Annexure 1 group: Depreciation & Amortisation; 6 cells; line 383
R134-R139 | annexure1_item | - | Annexure 1 group: Consolidated Profit After Tax; 6 cells; line 384
R140-R141 | annexure1_item | - | Annexure 1 segment Infrastructure & Utilities, Order inflow; 2 cells; line 387
R142-R143 | annexure1_item | - | Annexure 1 segment Infrastructure & Utilities, Customer revenue; 2 cells; line 387
R144-R145 | annexure1_item | - | Annexure 1 segment Infrastructure & Utilities, EBITDA margin; 2 cells; line 387
R146-R147 | annexure1_item | - | Annexure 1 segment Energy - Conventional, Order inflow; 2 cells; line 388
R148-R149 | annexure1_item | - | Annexure 1 segment Energy - Conventional, Customer revenue; 2 cells; line 388
R150-R151 | annexure1_item | - | Annexure 1 segment Energy - Conventional, EBITDA margin; 2 cells; line 388
R152-R153 | annexure1_item | - | Annexure 1 segment Energy - Green, Order inflow; 2 cells; line 389
R154-R155 | annexure1_item | - | Annexure 1 segment Energy - Green, Customer revenue; 2 cells; line 389
R156-R157 | annexure1_item | - | Annexure 1 segment Energy - Green, EBITDA margin; 2 cells; line 389
R158-R159 | annexure1_item | - | Annexure 1 segment Manufacturing & Products, Order inflow; 2 cells; line 390
R160-R161 | annexure1_item | - | Annexure 1 segment Manufacturing & Products, Customer revenue; 2 cells; line 390
R162-R163 | annexure1_item | - | Annexure 1 segment Manufacturing & Products, EBITDA margin; 2 cells; line 390
R164-R165 | annexure1_item | - | Annexure 1 segment Technology, Platforms & Services, Order inflow; 2 cells; line 391
R166-R167 | annexure1_item | - | Annexure 1 segment Technology, Platforms & Services, Customer revenue; 2 cells; line 391
R168-R169 | annexure1_item | - | Annexure 1 segment Technology, Platforms & Services, EBITDA margin; 2 cells; line 391
R170-R171 | annexure1_item | - | Annexure 1 segment Financial Services, Order inflow; 2 cells; line 392
R172-R173 | annexure1_item | - | Annexure 1 segment Financial Services, Customer revenue; 2 cells; line 392
R174-R175 | annexure1_item | - | Annexure 1 segment Realty, Order inflow; 2 cells; line 393
R176-R177 | annexure1_item | - | Annexure 1 segment Realty, Customer revenue; 2 cells; line 393
R178-R179 | annexure1_item | - | Annexure 1 segment Realty, EBITDA margin; 2 cells; line 393
R180-R181 | annexure1_item | ZERO_STANDING | Annexure 1 segment Development Projects, Order inflow; 2 cells; line 394
R182-R183 | annexure1_item | ZERO_STANDING | Annexure 1 segment Development Projects, Customer revenue; 2 cells; line 394
R184-R185 | annexure1_item | - | Annexure 1 segment Total, Order inflow; 2 cells; line 395
R186-R187 | annexure1_item | - | Annexure 1 segment Total, Customer revenue; 2 cells; line 395
R188-R189 | annexure1_item | - | Annexure 1 segment Infrastructure & Utilities, Order inflow; 2 cells; line 401
R190-R191 | annexure1_item | - | Annexure 1 segment Infrastructure & Utilities, Customer revenue; 2 cells; line 401
R192-R193 | annexure1_item | - | Annexure 1 segment Infrastructure & Utilities, EBITDA margin; 2 cells; line 401
R194-R195 | annexure1_item | - | Annexure 1 segment Energy - Conventional, Order inflow; 2 cells; line 402
R196-R197 | annexure1_item | - | Annexure 1 segment Energy - Conventional, Customer revenue; 2 cells; line 402
R198-R199 | annexure1_item | - | Annexure 1 segment Energy - Conventional, EBITDA margin; 2 cells; line 402
R200-R201 | annexure1_item | - | Annexure 1 segment Energy - Green, Order inflow; 2 cells; line 403
R202-R203 | annexure1_item | - | Annexure 1 segment Energy - Green, Customer revenue; 2 cells; line 403
R204-R205 | annexure1_item | - | Annexure 1 segment Energy - Green, EBITDA margin; 2 cells; line 403
R206-R207 | annexure1_item | - | Annexure 1 segment Manufacturing & Products, Order inflow; 2 cells; line 404
R208-R209 | annexure1_item | - | Annexure 1 segment Manufacturing & Products, Customer revenue; 2 cells; line 404
R210-R211 | annexure1_item | - | Annexure 1 segment Manufacturing & Products, EBITDA margin; 2 cells; line 404
R212-R213 | annexure1_item | - | Annexure 1 segment Technology, Platforms & Services, Order inflow; 2 cells; line 405
R214-R215 | annexure1_item | - | Annexure 1 segment Technology, Platforms & Services, Customer revenue; 2 cells; line 405
R216-R217 | annexure1_item | - | Annexure 1 segment Technology, Platforms & Services, EBITDA margin; 2 cells; line 405
R218-R219 | annexure1_item | - | Annexure 1 segment Financial Services, Order inflow; 2 cells; line 406
R220-R221 | annexure1_item | - | Annexure 1 segment Financial Services, Customer revenue; 2 cells; line 406
R222-R223 | annexure1_item | - | Annexure 1 segment Realty, Order inflow; 2 cells; line 407
R224-R225 | annexure1_item | - | Annexure 1 segment Realty, Customer revenue; 2 cells; line 407
R226-R227 | annexure1_item | - | Annexure 1 segment Realty, EBITDA margin; 2 cells; line 407
R228-R229 | annexure1_item | - | Annexure 1 segment Development Projects, Order inflow; 2 cells; line 408
R230-R231 | annexure1_item | - | Annexure 1 segment Development Projects, Customer revenue; 2 cells; line 408
R232-R233 | annexure1_item | - | Annexure 1 segment Total, Order inflow; 2 cells; line 409
R234-R235 | annexure1_item | - | Annexure 1 segment Total, Customer revenue; 2 cells; line 409
R236-R239 | annexure1_item | - | Annexure 1 Note: Financial Services NIM + Fees %; 4 cells; line 416
R240-R243 | annexure1_item | - | Annexure 1 Note: Development Projects EBIT (Rs crore); 4 cells; line 419
R2196-R2219 | annexure1_date | - | Annexure 1 period column headers; 24 rows; lines 376-418
R2383-R2389 | annexure1_qualifier | - | Annexure 1 table headers, refer-note markers, Note 1-2 headers; 7 rows; lines 376-417
R1920-R1927 | annexure2_entity | - | Annexure 2 segment composition; 8 rows; lines 429-451
R2390 | annexure2_qualifier | - | Annexure 2 segment composition; 1 rows; lines 451

## 5. FINANCIAL TABLES: every line item (one row per label; ZERO_STANDING and A1 flags carried)
ROW_ID(s) | category | A2 flags | cross-ref / materiality note
### C_PL (CONSOL P&L (statement i); fulltext lines 456-513)
R244-R249 | line_item/C_PL | - | consol P&L a) Revenue from operations; 6 cells; line 468
R250-R255 | line_item/C_PL | - | consol P&L b) Other income (net); 6 cells; line 469
R256-R261 | line_item/C_PL | - | consol P&L Total Income; 6 cells; line 470
R262-R267 | line_item/C_PL | - | consol P&L i) Cost of raw materials and components consumed; 6 cells; line 473
R268-R273 | line_item/C_PL | - | consol P&L ii) Construction materials consumed; 6 cells; line 474
R274-R279 | line_item/C_PL | - | consol P&L iii) Purchase of stock-in-trade; 6 cells; line 475
R280-R285 | line_item/C_PL | - | consol P&L iv) Stores. spares and loose tools consumed; 6 cells; line 476
R286-R291 | line_item/C_PL | - | consol P&L v) Sub-contracting charges; 6 cells; line 477
R292-R297 | line_item/C_PL | - | consol P&L vi) Changes in inventories of finished goods, stock-in-trade and; 6 cells; line 478
R298-R303 | line_item/C_PL | - | consol P&L vii) Other manufacturing, construction and operating expenses; 6 cells; line 479
R304-R309 | line_item/C_PL | - | consol P&L b) Finance cost of financial services business and finance; 6 cells; line 480
R310-R315 | line_item/C_PL | - | consol P&L c) Employee benefits expense; 6 cells; line 481
R316-R321 | line_item/C_PL | - | consol P&L d) Sales, administration and other expenses; 6 cells; line 482
R322-R327 | line_item/C_PL | - | consol P&L e) Finance costs; 6 cells; line 483
R328-R333 | line_item/C_PL | - | consol P&L f) Depreciation. amortisation. impairment and obsolescence; 6 cells; line 484
R334-R339 | line_item/C_PL | - | consol P&L Total Expenses; 6 cells; line 485
R340-R345 | line_item/C_PL | - | consol P&L Profit before exceptional items and tax {1-2); 6 cells; line 486
R346-R351 | line_item/C_PL | ZERO_STANDING | consol P&L Exceptional items [loss]; 6 cells; line 487
R352-R357 | line_item/C_PL | - | consol P&L Profit before tax (3+4); 6 cells; line 488
R358-R363 | line_item/C_PL | - | consol P&L a) Current tax; 6 cells; line 490
R364-R369 | line_item/C_PL | - | consol P&L b) Deferred tax; 6 cells; line 491
R370-R375 | line_item/C_PL | - | consol P&L Total tax expense; 6 cells; line 492
R376-R381 | line_item/C_PL | - | consol P&L Net profit after tax (5-6); 6 cells; line 493
R382-R387 | line_item/C_PL | - | consol P&L Share in profiU(loss) after tax of joint ventures/associates (net}; 6 cells; line 494
R388-R393 | line_item/C_PL | - | consol P&L Net profit after tax including share in profit/{loss) of; 6 cells; line 495
R394-R399 | line_item/C_PL | - | consol P&L Attributable to: Owners of the Company; 6 cells; line 496
R400-R405 | line_item/C_PL | - | consol P&L Non-eontrolling interests; 6 cells; line 497
R406-R411 | line_item/C_PL | - | consol P&L a) i) Items that will not be reclassified to; 6 cells; line 499
R412-R417 | line_item/C_PL | - | consol P&L ii} Income tax relating to items that will nol; 6 cells; line 500
R418-R423 | line_item/C_PL | - | consol P&L b) i) Items lhal will be reclassified to profit; 6 cells; line 501
R424-R429 | line_item/C_PL | - | consol P&L ii) Income tax relating to items that will be; 6 cells; line 502
R430-R435 | line_item/C_PL | - | consol P&L Other comprehensive income [net of tax] (a+b); 6 cells; line 503
R436-R441 | line_item/C_PL | - | consol P&L Allributable to: Owners of lhe Company; 6 cells; line 504
R442-R447 | line_item/C_PL | - | consol P&L Non-controlling interests; 6 cells; line 505
R448-R453 | line_item/C_PL | - | consol P&L Total comprehensive income (9+10); 6 cells; line 506
R454-R459 | line_item/C_PL | - | consol P&L Attributable to: Owners of the Company; 6 cells; line 507
R460-R465 | line_item/C_PL | - | consol P&L Non-controlling Interests; 6 cells; line 508
R466-R471 | line_item/C_PL | - | consol P&L Paid-up equity share capital (face value of share: t; 6 cells; line 509
R472 | line_item/C_PL | PARTIAL_COLS(right-aligned) | consol P&L Other equity attributable to owners of the Company; 1 cells; line 510
R473-R478 | line_item/C_PL | - | consol P&L (a) Basic EPS (t); 6 cells; line 512
R479-R484 | line_item/C_PL | - | consol P&L (b) Diluted EPS (~); 6 cells; line 513
R2220-R2226 | C_PL_date | - | table headers, period labels, qualifiers for C_PL; 7 rows; lines 461-463
R2391-R2395 | C_PL_qualifier | - | table headers, period labels, qualifiers for C_PL; 5 rows; lines 461-511
### C_BS (CONSOL Balance Sheet (note iii statement); fulltext lines 520-594)
R486-R487 | line_item/C_BS | - | consol BS Property, plant and equipment; 2 cells; line 530
R488-R489 | line_item/C_BS | - | consol BS Capital work-in-progress; 2 cells; line 531
R490-R491 | line_item/C_BS | - | consol BS Investment property; 2 cells; line 532
R492-R493 | line_item/C_BS | - | consol BS Investment property under construction; 2 cells; line 533
R494-R495 | line_item/C_BS | - | consol BS Goodwill; 2 cells; line 534
R496-R497 | line_item/C_BS | - | consol BS Other intangible assets; 2 cells; line 535
R498-R499 | line_item/C_BS | - | consol BS Intangible assets under development; 2 cells; line 536
R500-R501 | line_item/C_BS | - | consol BS Right-of-use assets; 2 cells; line 537
R502-R503 | line_item/C_BS | - | consol BS Investments in joint ventures and associates; 2 cells; line 539
R504-R505 | line_item/C_BS | - | consol BS Other investments; 2 cells; line 540
R506-R507 | line_item/C_BS | - | consol BS Loans towards financing activities; 2 cells; line 541
R508-R509 | line_item/C_BS | - | consol BS Other loans; 2 cells; line 542
R510-R511 | line_item/C_BS | - | consol BS Other financial assets; 2 cells; line 543
R512-R513 | line_item/C_BS | - | consol BS Deferred tax assets (net); 2 cells; line 544
R514-R515 | line_item/C_BS | - | consol BS Current tax assets (net); 2 cells; line 545
R516-R517 | line_item/C_BS | - | consol BS Other non-current assets; 2 cells; line 546
R518-R519 | line_item/C_BS | - | consol BS Sub-total - Non-current assets; 2 cells; line 547
R520-R521 | line_item/C_BS | - | consol BS Inventories; 2 cells; line 549
R522-R523 | line_item/C_BS | - | consol BS Investments; 2 cells; line 551
R524-R525 | line_item/C_BS | - | consol BS Trade receivables; 2 cells; line 552
R526-R527 | line_item/C_BS | - | consol BS Cash and cash equivalents; 2 cells; line 553
R528-R529 | line_item/C_BS | - | consol BS Other bank balances; 2 cells; line 554
R530-R531 | line_item/C_BS | - | consol BS Loans towards financing activities; 2 cells; line 555
R532-R533 | line_item/C_BS | - | consol BS Other loans; 2 cells; line 556
R534-R535 | line_item/C_BS | - | consol BS Other financial assets; 2 cells; line 557
R536-R537 | line_item/C_BS | - | consol BS Other current assets; 2 cells; line 558
R538-R539 | line_item/C_BS | - | consol BS Sub-total - Current assets; 2 cells; line 559
R540-R541 | line_item/C_BS | - | consol BS Group(s) of assets classified as held for sale; 2 cells; line 560
R542-R543 | line_item/C_BS | - | consol BS TOTAL ASSETS; 2 cells; line 561
R544-R545 | line_item/C_BS | - | consol BS Equity share capital; 2 cells; line 564
R546-R547 | line_item/C_BS | - | consol BS Other equity; 2 cells; line 565
R548-R549 | line_item/C_BS | - | consol BS Equity attributable to owners of the Company; 2 cells; line 566
R550-R551 | line_item/C_BS | - | consol BS Non-controlling interest; 2 cells; line 567
R552-R553 | line_item/C_BS | - | consol BS TOTAL EQUITY; 2 cells; line 568
R554-R555 | line_item/C_BS | - | consol BS Borrowings; 2 cells; line 572
R556-R557 | line_item/C_BS | - | consol BS Lease liabilities; 2 cells; line 573
R558-R559 | line_item/C_BS | - | consol BS Other financial liabilities; 2 cells; line 574
R560-R561 | line_item/C_BS | - | consol BS Provisions; 2 cells; line 575
R562-R563 | line_item/C_BS | - | consol BS Deferred tax liabilities (net); 2 cells; line 576
R564-R565 | line_item/C_BS | - | consol BS Other non-current liabilities; 2 cells; line 577
R566-R567 | line_item/C_BS | - | consol BS Sub-total • Non-current liabilities; 2 cells; line 578
R568-R569 | line_item/C_BS | - | consol BS Borrowings; 2 cells; line 581
R570-R571 | line_item/C_BS | - | consol BS Current maturities of long term borrowings; 2 cells; line 582
R572-R573 | line_item/C_BS | - | consol BS Lease liabilities; 2 cells; line 583
R574-R575 | line_item/C_BS | - | consol BS Due to micro enterprises and small enterprises; 2 cells; line 585
R576-R577 | line_item/C_BS | - | consol BS Due to others; 2 cells; line 586
R578-R579 | line_item/C_BS | - | consol BS Other financial liabilities; 2 cells; line 587
R580-R581 | line_item/C_BS | - | consol BS Other current liabilities; 2 cells; line 588
R582-R583 | line_item/C_BS | - | consol BS Provisions; 2 cells; line 589
R584-R585 | line_item/C_BS | - | consol BS Current tax liabilities (net); 2 cells; line 590
R586-R587 | line_item/C_BS | - | consol BS Sub-total - Current liabilities; 2 cells; line 591
R588-R589 | line_item/C_BS | - | consol BS Liabilities associated with group(s) of assets classified as held; 2 cells; line 592
R590-R591 | line_item/C_BS | - | consol BS TOTAL LIABILITIES; 2 cells; line 593
R592-R593 | line_item/C_BS | - | consol BS TOTAL EQUITY AND LIABILITIES; 2 cells; line 594
R2231-R2232 | C_BS_date | - | table headers, period labels, qualifiers for C_BS; 2 rows; lines 525
R2398-R2400 | C_BS_qualifier | - | table headers, period labels, qualifiers for C_BS; 3 rows; lines 521-527
### C_SA (Consol note (iv) table: standalone specified items (revenue, PBT, PAT); fulltext lines 597-618)
R594-R599 | line_item/C_SA | - | standalone items (consol note iv) Revenue from operations; 6 cells; line 603
R600-R605 | line_item/C_SA | - | standalone items (consol note iv) Profit before exceptional items and tax; 6 cells; line 605
R606-R611 | line_item/C_SA | - | standalone items (consol note iv) Profit/(loss) before tax (after exceptional items); 6 cells; line 609
R612-R617 | line_item/C_SA | - | standalone items (consol note iv) Net profit/(loss) after tax (after exceptional items); 6 cells; line 615
R2233-R2238 | C_SA_date | - | table headers, period labels, qualifiers for C_SA; 6 rows; lines 598
R2402-R2403 | C_SA_qualifier | - | table headers, period labels, qualifiers for C_SA; 2 rows; lines 597-601
### C_RAT (CONSOL Reg 52(4) ratios (note v statement); fulltext lines 619-640)
R618-R623 | line_item/C_RAT | - | consol ratios Debt equity ratio; 6 cells; line 627
R624-R629 | line_item/C_RAT | - | consol ratios Debt service coverage ratio (DSCR); 6 cells; line 628
R630-R635 | line_item/C_RAT | - | consol ratios Interest service coverage ratio (ISCR); 6 cells; line 629
R636-R641 | line_item/C_RAT | - | consol ratios Current ratio; 6 cells; line 630
R642-R647 | line_item/C_RAT | - | consol ratios Long term debt to working capital ratio; 6 cells; line 631
R648-R653 | line_item/C_RAT | ZERO_STANDING | consol ratios Bad debts to accounts receivable ratio; 6 cells; line 632
R654-R659 | line_item/C_RAT | - | consol ratios Current liability ratio; 6 cells; line 633
R660-R665 | line_item/C_RAT | - | consol ratios Total debt to total assets ratio; 6 cells; line 634
R666-R671 | line_item/C_RAT | - | consol ratios Debtors turnover ratio; 6 cells; line 635
R672-R677 | line_item/C_RAT | - | consol ratios Operating margin (%); 6 cells; line 636
R678-R683 | line_item/C_RAT | - | consol ratios Net profit margin(%); 6 cells; line 637
R684-R689 | line_item/C_RAT | NOT_APPLICABLE | consol ratios Inventory turnover ratio [refer note (d)(12)); 6 cells; line 638
R690-R695 | line_item/C_RAT | - | consol ratios Capital Redemption Reserve/Debenture Redemption Reserver' Crore); 6 cells; line 639
R696-R701 | line_item/C_RAT | - | consol ratios Net worth r' Crore) (As per section 2(57) of; 6 cells; line 640
R2239-R2245 | C_RAT_date | - | table headers, period labels, qualifiers for C_RAT; 7 rows; lines 620-621
R2404 | C_RAT_qualifier | - | table headers, period labels, qualifiers for C_RAT; 1 rows; lines 620
### C_CF (CONSOL Cash Flow (note vi statement); page 14 reconstructed from render; fulltext lines 702-769)
R704-R705 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Profit before exceptional items and tax; 2 cells; line 708
R706-R707 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Dividend received; 2 cells; line 710
R708-R709 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Depreciation, amortisation, impairment and obsolescence; 2 cells; line 711
R710-R711 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Exchange difference on items grouped under financing/investing activities; 2 cells; line 712
R712-R713 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Effect of exchange rate changes on cash and cash; 2 cells; line 713
R714-R715 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Finance costs; 2 cells; line 714
R716-R717 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Interest income; 2 cells; line 715
R718-R719 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: (Profit)/loss on sale of Property, plant and equipment, Investment; 2 cells; line 716
R720-R721 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: (Profit)/loss on sale/fair valuation of investments (net); 2 cells; line 717
R722-R723 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Bad debts and advances written off & Allowances for; 2 cells; line 718
R724-R725 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Employee stock option-discount; 2 cells; line 719
R726-R727 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER, ZERO_STANDING | consol CF: (Gain)/loss on disposal of subsidiary/associate/business undertaking; 2 cells; line 720
R728-R729 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: (Profit)/loss on investments/loans towards financing activity (net); 2 cells; line 721
R730-R731 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Others; 2 cells; line 722
R732-R733 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Operating profit before working capital changes; 2 cells; line 723
R734-R735 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: (Increase)/decrease in trade and other receivables; 2 cells; line 725
R736-R737 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: (Increase)/decrease in inventories; 2 cells; line 726
R738-R739 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Increase/(decrease) in trade and other payables; 2 cells; line 727
R740-R741 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Cash generated from operations before financing activities; 2 cells; line 728
R742-R743 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: (Increase)/decrease in loans and advances towards financing activities; 2 cells; line 729
R744-R745 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Cash generated from operations; 2 cells; line 730
R746-R747 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Direct taxes paid (net); 2 cells; line 731
R748-R749 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Net cash generated from operating activities; 2 cells; line 732
R750-R751 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Purchase of Property, plant and equipment, Investment property and; 2 cells; line 734
R752-R753 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Sale of Property, plant and equipment, Investment property and; 2 cells; line 735
R754-R755 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Purchase of non-current investments; 2 cells; line 736
R756-R757 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Sale of non-current investments; 2 cells; line 737
R758-R759 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: (Purchase)/sale of current investments (net); 2 cells; line 738
R760-R761 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Change in other bank balance and cash not available; 2 cells; line 739
R762-R763 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Deposits/loans given to associates, joint ventures and third parties; 2 cells; line 740
R764-R765 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Deposits/loans repaid by associates, joint ventures and third parties; 2 cells; line 741
R766-R767 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Interest received; 2 cells; line 742
R768-R769 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Dividend received from joint ventures/associates; 2 cells; line 743
R770-R771 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Dividend received from other investments; 2 cells; line 744
R772-R773 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER, ZERO_STANDING | consol CF: Consideration received on transfer of business undertaking; 2 cells; line 745
R774-R775 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER, ZERO_STANDING | consol CF: Consideration received on disposal of subsidiaries/ divestment of part; 2 cells; line 746
R776-R777 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER, ZERO_STANDING | consol CF: Consideration paid on acquisition of business; 2 cells; line 747
R778-R779 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Consideration paid on acquisition of Subsidiaries (including contingent consideration); 2 cells; line 748
R780-R781 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER, ZERO_STANDING | consol CF: Cash and cash equivalents acquired pursuant to acquisition of; 2 cells; line 749
R782-R783 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER, ZERO_STANDING | consol CF: Consideration paid on acquisition of stake in an associate/joint; 2 cells; line 750
R784-R785 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Net cash generated from/(used in) investing activities; 2 cells; line 751
R786-R787 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Proceeds from issue of share capital (including share application; 2 cells; line 753
R788-R789 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Proceeds from non-current borrowings; 2 cells; line 754
R790-R791 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Repayment of non-current borrowings; 2 cells; line 755
R792-R793 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Proceeds from/(repayment of) other borrowings (net); 2 cells; line 756
R794-R795 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER, ZERO_STANDING | consol CF: Payment made for acquisition of additional stake in a; 2 cells; line 757
R796-R797 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Other payments (to)/from non-controlling interest (net); 2 cells; line 758
R798-R799 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Settlement of derivative contracts related to borrowings; 2 cells; line 759
R800-R801 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Dividends paid; 2 cells; line 760
R802-R803 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Repayment of lease liability; 2 cells; line 761
R804-R805 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Interest paid on lease liability; 2 cells; line 762
R806-R807 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Interest paid (including cash flows on account of interest; 2 cells; line 763
R808-R809 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Net cash generated from/(used in) financing activities; 2 cells; line 764
R810-R811 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Net increase/(decrease) in cash and cash equivalents (A+ B; 2 cells; line 765
R812-R813 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Cash and cash equivalents at beginning of the period; 2 cells; line 766
R814-R815 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Effect of exchange rate changes on cash and cash; 2 cells; line 767
R816-R817 | line_item/C_CF | RECONSTRUCTED_FROM_RENDER | consol CF: Cash and cash equivalents at end of the period; 2 cells; line 768
R2250-R2251 | C_CF_date | - | table headers, period labels, qualifiers for C_CF; 2 rows; lines 704
R2427-R2429 | C_CF_qualifier | - | table headers, period labels, qualifiers for C_CF; 3 rows; lines 703-706
### C_SEG (CONSOL Segment revenue, results, assets, liabilities; fulltext lines 786-847)
R818-R823 | line_item/C_SEG | - | consol segment Gross segment revenue: Infrastructure & Utilities; 6 cells; line 795
R824-R829 | line_item/C_SEG | - | consol segment Gross segment revenue: Energy - Conventional; 6 cells; line 796
R830-R835 | line_item/C_SEG | - | consol segment Gross segment revenue: Energy - Green; 6 cells; line 797
R836-R841 | line_item/C_SEG | - | consol segment Gross segment revenue: Manufacturing & Products; 6 cells; line 798
R842-R847 | line_item/C_SEG | - | consol segment Gross segment revenue: Technology, Platforms & Services; 6 cells; line 799
R848-R853 | line_item/C_SEG | - | consol segment Gross segment revenue: Financial Services; 6 cells; line 800
R854-R859 | line_item/C_SEG | - | consol segment Gross segment revenue: Realty; 6 cells; line 801
R860-R865 | line_item/C_SEG | ZERO_STANDING | consol segment Gross segment revenue: Development Projects; 6 cells; line 802
R866-R871 | line_item/C_SEG | - | consol segment Gross segment revenue: Total; 6 cells; line 803
R872-R877 | line_item/C_SEG | - | consol segment Gross segment revenue: Less: Inter-segment revenue; 6 cells; line 804
R878-R883 | line_item/C_SEG | - | consol segment Gross segment revenue: Net seg ment revenue; 6 cells; line 805
R884-R889 | line_item/C_SEG | - | consol segment Segment results: Infrastructure & Utilities; 6 cells; line 807
R890-R895 | line_item/C_SEG | - | consol segment Segment results: Energy. Conventional; 6 cells; line 808
R896-R901 | line_item/C_SEG | - | consol segment Segment results: Energy• Green; 6 cells; line 809
R902-R907 | line_item/C_SEG | - | consol segment Segment results: M anufacturing & Products; 6 cells; line 810
R908-R913 | line_item/C_SEG | - | consol segment Segment results: Technology, P latforms & Services; 6 cells; line 811
R914-R919 | line_item/C_SEG | - | consol segment Segment results: Financial Services; 6 cells; line 812
R920-R925 | line_item/C_SEG | - | consol segment Segment results: Realty; 6 cells; line 813
R926-R931 | line_item/C_SEG | - | consol segment Segment results: Development Projects; 6 cells; line 814
R932-R937 | line_item/C_SEG | - | consol segment Segment results: Total; 6 cells; line 815
R938-R943 | line_item/C_SEG | - | consol segment Segment results: Less: Inter-segment margins on capital jobs; 6 cells; line 816
R944-R949 | line_item/C_SEG | - | consol segment Segment results: Less: Finance costs; 6 cells; line 817
R950-R955 | line_item/C_SEG | - | consol segment Segment results: Add: Unallocable corporate income net of expenditure; 6 cells; line 818
R956-R961 | line_item/C_SEG | - | consol segment Segment results: Profit before exceptional it ems and tax; 6 cells; line 819
R962-R967 | line_item/C_SEG | ZERO_STANDING | consol segment Segment results: Addl(less): Exceptional items (loss); 6 cells; line 820
R968-R973 | line_item/C_SEG | - | consol segment Segment results: Profit before tax (including exceptional items); 6 cells; line 821
R974-R979 | line_item/C_SEG | - | consol segment Segment assets: Infrastructure & Utilities; 6 cells; line 823
R980-R985 | line_item/C_SEG | - | consol segment Segment assets: Energy - Conventional; 6 cells; line 824
R986-R991 | line_item/C_SEG | - | consol segment Segment assets: Energy ~ Green; 6 cells; line 825
R992-R997 | line_item/C_SEG | - | consol segment Segment assets: Manufacturing & Products; 6 cells; line 826
R998-R1003 | line_item/C_SEG | - | consol segment Segment assets: T echnology, Platforms & Services; 6 cells; line 827
R1004-R1009 | line_item/C_SEG | - | consol segment Segment assets: Financial Services; 6 cells; line 828
R1010-R1015 | line_item/C_SEG | - | consol segment Segment assets: Realty; 6 cells; line 829
R1016-R1021 | line_item/C_SEG | - | consol segment Segment assets: Development Projects; 6 cells; line 830
R1022-R1027 | line_item/C_SEG | - | consol segment Segment assets: Total segment asset s; 6 cells; line 831
R1028-R1033 | line_item/C_SEG | - | consol segment Segment assets: Less: Inter.segment assets; 6 cells; line 832
R1034-R1039 | line_item/C_SEG | - | consol segment Segment assets: Add: Unallocable corporate assets; 6 cells; line 833
R1040-R1045 | line_item/C_SEG | - | consol segment Segment assets: Total assets; 6 cells; line 834
R1046-R1051 | line_item/C_SEG | - | consol segment Segment liabilities: Infrastructure & Utilities; 6 cells; line 836
R1052-R1057 | line_item/C_SEG | - | consol segment Segment liabilities: Energy• Conventional; 6 cells; line 837
R1058-R1063 | line_item/C_SEG | - | consol segment Segment liabilities: Energy - Green; 6 cells; line 838
R1064-R1069 | line_item/C_SEG | - | consol segment Segment liabilities: Manufacturing & Products; 6 cells; line 839
R1070-R1075 | line_item/C_SEG | - | consol segment Segment liabilities: Technology, Platforms & Services; 6 cells; line 840
R1076-R1081 | line_item/C_SEG | - | consol segment Segment liabilities: F inancial Services; 6 cells; line 841
R1082-R1087 | line_item/C_SEG | - | consol segment Segment liabilities: Realty; 6 cells; line 842
R1088-R1093 | line_item/C_SEG | - | consol segment Segment liabilities: Development Projects; 6 cells; line 843
R1094-R1099 | line_item/C_SEG | - | consol segment Segment liabilities: Total s egment liab ilities; 6 cells; line 844
R1100-R1105 | line_item/C_SEG | - | consol segment Segment liabilities: Less: Inter.segment liabilities; 6 cells; line 845
R1106-R1111 | line_item/C_SEG | - | consol segment Segment liabilities: Add: Unallocable corporate liabilities; 6 cells; line 846
R1112-R1117 | line_item/C_SEG | - | consol segment Segment liabilities: Total liabilit ies; 6 cells; line 847
R2256-R2261 | C_SEG_date | - | table headers, period labels, qualifiers for C_SEG; 6 rows; lines 789
R2434-R2435 | C_SEG_qualifier | - | table headers, period labels, qualifiers for C_SEG; 2 rows; lines 787-788
### S_PL (STANDALONE P&L; fulltext lines 904-956)
R1118-R1123 | line_item/S_PL | - | standalone P&L Revenue from operations; 6 cells; line 916
R1124-R1129 | line_item/S_PL | - | standalone P&L Other income(net}; 6 cells; line 918
R1130-R1135 | line_item/S_PL | - | standalone P&L Total Income; 6 cells; line 919
R1136-R1141 | line_item/S_PL | - | standalone P&L i} Cost of raw materials and components consumed; 6 cells; line 922
R1142-R1147 | line_item/S_PL | - | standalone P&L ii) Construction materials consumed; 6 cells; line 923
R1148-R1153 | line_item/S_PL | - | standalone P&L iii) Purchases of stock-In-trade; 6 cells; line 924
R1154-R1159 | line_item/S_PL | - | standalone P&L iv) Stores, spares and loose tools consumed; 6 cells; line 925
R1160-R1165 | line_item/S_PL | - | standalone P&L v) Sub-contracting charges; 6 cells; line 926
R1166-R1171 | line_item/S_PL | - | standalone P&L vi) Changes In inventories of finished goods, stock-in-trade and; 6 cells; line 927
R1172-R1177 | line_item/S_PL | - | standalone P&L vii) Other manufacturing, construction and operating expenses; 6 cells; line 928
R1178-R1183 | line_item/S_PL | - | standalone P&L Employee benefi,ts expense; 6 cells; line 929
R1184-R1189 | line_item/S_PL | - | standalone P&L cl Sales, administration and other expenses; 6 cells; line 930
R1190-R1195 | line_item/S_PL | - | standalone P&L Finance costs; 6 cells; line 932
R1196-R1201 | line_item/S_PL | - | standalone P&L Depreciation, amortisation, impairment and obsolescence; 6 cells; line 933
R1202-R1207 | line_item/S_PL | - | standalone P&L Total Expenses; 6 cells; line 934
R1208-R1213 | line_item/S_PL | - | standalone P&L Profit before exceptional Items and tax (1-2); 6 cells; line 935
R1214-R1219 | line_item/S_PL | ZERO_STANDING | standalone P&L Exceptional Items (loss); 6 cells; line 936
R1220-R1225 | line_item/S_PL | - | standalone P&L Profll/(loss) before tax {3+4); 6 cells; line 937
R1226-R1231 | line_item/S_PL | - | standalone P&L Current tax; 6 cells; line 939
R1232-R1237 | line_item/S_PL | - | standalone P&L Deferred tax; 6 cells; line 941
R1238-R1243 | line_item/S_PL | - | standalone P&L Total tax expense; 6 cells; line 942
R1244-R1249 | line_item/S_PL | - | standalone P&L Net profil/(loss} after tax (5-6); 6 cells; line 943
R1250-R1255 | line_item/S_PL | - | standalone P&L i) Items that will not be reclassified to profit; 6 cells; line 945
R1256-R1261 | line_item/S_PL | - | standalone P&L ii) Income tax relating to items that will not; 6 cells; line 946
R1262-R1267 | line_item/S_PL | - | standalone P&L i) Items that will be reclassified to profit and; 6 cells; line 948
R1268-R1273 | line_item/S_PL | - | standalone P&L ii) Income tax relating to items that will be; 6 cells; line 949
R1274-R1279 | line_item/S_PL | - | standalone P&L Other i::omprehensive income [net of tax] (a+b); 6 cells; line 950
R1280-R1285 | line_item/S_PL | - | standalone P&L Total comprehensive income (7+8); 6 cells; line 951
R1286-R1291 | line_item/S_PL | - | standalone P&L Paid-up equity share capital (face value or share:~ 2; 6 cells; line 952
R1292 | line_item/S_PL | PARTIAL_COLS(right-aligned) | standalone P&L Other equity; 1 cells; line 953
R1293-R1298 | line_item/S_PL | - | standalone P&L (a) Basic EPS (~; 6 cells; line 955
R1299-R1304 | line_item/S_PL | - | standalone P&L b) Diluted EPS (~; 6 cells; line 956
R2266-R2272 | S_PL_date | - | table headers, period labels, qualifiers for S_PL; 7 rows; lines 908-910
R2442-R2445 | S_PL_qualifier | - | table headers, period labels, qualifiers for S_PL; 4 rows; lines 908-954
### S_BS (STANDALONE Balance Sheet (note v statement); fulltext lines 972-1045)
R1306-R1307 | line_item/S_BS | - | standalone BS Property, plant and equipment; 2 cells; line 981
R1308-R1309 | line_item/S_BS | - | standalone BS Capital work-in-progress; 2 cells; line 982
R1310-R1311 | line_item/S_BS | - | standalone BS Investment property; 2 cells; line 983
R1312-R1313 | line_item/S_BS | - | standalone BS Investment property under construction; 2 cells; line 984
R1314-R1315 | line_item/S_BS | - | standalone BS Goodwill; 2 cells; line 985
R1316-R1317 | line_item/S_BS | - | standalone BS Other intangible assets; 2 cells; line 986
R1318-R1319 | line_item/S_BS | - | standalone BS Intangible assets under development; 2 cells; line 987
R1320-R1321 | line_item/S_BS | - | standalone BS Right-of-use assets; 2 cells; line 988
R1322-R1323 | line_item/S_BS | - | standalone BS Investments; 2 cells; line 990
R1324-R1325 | line_item/S_BS | - | standalone BS Loans; 2 cells; line 991
R1326-R1327 | line_item/S_BS | - | standalone BS other financial assets; 2 cells; line 992
R1328-R1329 | line_item/S_BS | - | standalone BS Deferred tax assets (net); 2 cells; line 993
R1330-R1331 | line_item/S_BS | - | standalone BS Current tax assets (net); 2 cells; line 994
R1332-R1333 | line_item/S_BS | - | standalone BS other non-current assets; 2 cells; line 995
R1334-R1335 | line_item/S_BS | - | standalone BS Sub total - Non-current assets; 2 cells; line 996
R1336-R1337 | line_item/S_BS | - | standalone BS Inventories; 2 cells; line 998
R1338-R1339 | line_item/S_BS | - | standalone BS Investments; 2 cells; line 1000
R1340-R1341 | line_item/S_BS | - | standalone BS Trade receivables; 2 cells; line 1001
R1342-R1343 | line_item/S_BS | - | standalone BS Cash and cash equivalents; 2 cells; line 1002
R1344-R1345 | line_item/S_BS | - | standalone BS other bank balances; 2 cells; line 1003
R1346-R1347 | line_item/S_BS | - | standalone BS Loans; 2 cells; line 1004
R1348-R1349 | line_item/S_BS | - | standalone BS Other financial assets; 2 cells; line 1005
R1350-R1351 | line_item/S_BS | - | standalone BS Other current assets; 2 cells; line 1006
R1352-R1353 | line_item/S_BS | - | standalone BS Sub total • Current assets; 2 cells; line 1007
R1354-R1355 | line_item/S_BS | - | standalone BS Group(s) of assets classified as held for sale; 2 cells; line 1008
R1356-R1357 | line_item/S_BS | - | standalone BS TOT AL ASSETS; 2 cells; line 1009
R1358-R1359 | line_item/S_BS | - | standalone BS Equity share capital; 2 cells; line 1012
R1360-R1361 | line_item/S_BS | - | standalone BS Other equity; 2 cells; line 1013
R1362-R1363 | line_item/S_BS | - | standalone BS TOT AL EQUITY; 2 cells; line 1014
R1364-R1365 | line_item/S_BS | - | standalone BS Borrowings; 2 cells; line 1018
R1366-R1367 | line_item/S_BS | - | standalone BS Lease liabilities; 2 cells; line 1019
R1368-R1369 | line_item/S_BS | - | standalone BS Other financial liabilities; 2 cells; line 1020
R1370-R1371 | line_item/S_BS | - | standalone BS Provisions; 2 cells; line 1021
R1372-R1373 | line_item/S_BS | - | standalone BS Other non-current liabilities; 2 cells; line 1022
R1374-R1375 | line_item/S_BS | - | standalone BS Sub total • Non-current liabilities; 2 cells; line 1023
R1376-R1377 | line_item/S_BS | - | standalone BS Borrowings; 2 cells; line 1026
R1378-R1379 | line_item/S_BS | - | standalone BS Current maturities of !ong term borrowings; 2 cells; line 1027
R1380-R1381 | line_item/S_BS | - | standalone BS Lease liabilities; 2 cells; line 1028
R1382-R1383 | line_item/S_BS | - | standalone BS Due to micro enterprises and small enterprises; 2 cells; line 1030
R1384-R1385 | line_item/S_BS | - | standalone BS Due to others; 2 cells; line 1031
R1386-R1387 | line_item/S_BS | - | standalone BS Other financial liabilities; 2 cells; line 1032
R1388-R1389 | line_item/S_BS | - | standalone BS Other current liabilities; 2 cells; line 1033
R1390-R1391 | line_item/S_BS | - | standalone BS Provisions; 2 cells; line 1034
R1392-R1393 | line_item/S_BS | - | standalone BS Current tax liabilities (net); 2 cells; line 1035
R1394-R1395 | line_item/S_BS | - | standalone BS Sub total - Current liabilities; 2 cells; line 1036
R1396-R1397 | line_item/S_BS | - | standalone BS Liabilities associated with the group(s) of assets classified as; 2 cells; line 1038
R1398-R1399 | line_item/S_BS | - | standalone BS TOTAL LIABILITIES; 2 cells; line 1040
R1400-R1401 | line_item/S_BS | - | standalone BS TOTAL EQUITY AND LIABILITIES; 2 cells; line 1042
R2282-R2283 | S_BS_date | - | table headers, period labels, qualifiers for S_BS; 2 rows; lines 976
R2450-R2451 | S_BS_qualifier | - | table headers, period labels, qualifiers for S_BS; 2 rows; lines 973-974
### S_RAT (STANDALONE Reg 52(4) ratios incl CRR/DRR and net worth (note vi statement); fulltext lines 1046-1064)
R1402-R1407 | line_item/S_RAT | - | standalone ratios Debt equity ratio; 6 cells; line 1051
R1408-R1413 | line_item/S_RAT | - | standalone ratios Debt service coverage ratio (DSCR); 6 cells; line 1052
R1414-R1419 | line_item/S_RAT | - | standalone ratios Interest service coverage ratio (lSCR); 6 cells; line 1053
R1420-R1425 | line_item/S_RAT | - | standalone ratios Current ratio; 6 cells; line 1054
R1426-R1431 | line_item/S_RAT | - | standalone ratios Long tenn debt to working capital ratio; 6 cells; line 1055
R1432-R1437 | line_item/S_RAT | ZERO_STANDING | standalone ratios Bad debts to accounts receivable ratio; 6 cells; line 1056
R1438-R1443 | line_item/S_RAT | - | standalone ratios Current liability ratio; 6 cells; line 1057
R1444-R1449 | line_item/S_RAT | - | standalone ratios Total debt to total assets ratio; 6 cells; line 1058
R1450-R1455 | line_item/S_RAT | - | standalone ratios Debtors turnover ratio; 6 cells; line 1059
R1456-R1461 | line_item/S_RAT | - | standalone ratios Operating margin (%); 6 cells; line 1060
R1462-R1467 | line_item/S_RAT | - | standalone ratios Net profit margin(%); 6 cells; line 1061
R1468-R1473 | line_item/S_RAT | NOT_APPLICABLE | standalone ratios Inventory turnover ratio (refer note 12); 6 cells; line 1062
R1474-R1479 | line_item/S_RAT | - | standalone ratios Capita! Redemption Reserve/Debenture Redemption Reserve [ ( Crore]; 6 cells; line 1063
R1480-R1485 | line_item/S_RAT | - | standalone ratios Net worth [ ( Crore] (As per section 2(57}; 6 cells; line 1064
R2284-R2290 | S_RAT_date | - | table headers, period labels, qualifiers for S_RAT; 7 rows; lines 1047-1048
R2452 | S_RAT_qualifier | - | table headers, period labels, qualifiers for S_RAT; 1 rows; lines 1047
### S_CF (STANDALONE Cash Flow (note vii statement); fulltext lines 1095-1160)
R1487-R1488 | line_item/S_CF | - | standalone CF Profit before exceptional Items and tax; 2 cells; line 1103
R1489-R1490 | line_item/S_CF | - | standalone CF Dividend received; 2 cells; line 1105
R1491-R1492 | line_item/S_CF | - | standalone CF Depreciation, amortisation, impairment and obsolescence; 2 cells; line 1106
R1493-R1494 | line_item/S_CF | - | standalone CF Exchange difference on items grouped under financing/investing activities; 2 cells; line 1107
R1495-R1496 | line_item/S_CF | - | standalone CF Effect of exchange rate changes on cash and cash; 2 cells; line 1108
R1497-R1498 | line_item/S_CF | - | standalone CF Finance costs; 2 cells; line 1109
R1499-R1500 | line_item/S_CF | - | standalone CF Interest lncome; 2 cells; line 1110
R1501-R1502 | line_item/S_CF | - | standalone CF Intangible assets (net); 2 cells; line 1112
R1503-R1504 | line_item/S_CF | - | standalone CF (Profit)/loss on sale/fair valuation of investments (net); 2 cells; line 1113
R1505-R1506 | line_item/S_CF | - | standalone CF Bad debts/Allowance for expected credit loss (net); 2 cells; line 1114
R1507-R1508 | line_item/S_CF | - | standalone CF Employee stock option-discount; 2 cells; line 1115
R1509-R1510 | line_item/S_CF | - | standalone CF others; 2 cells; line 1116
R1511-R1512 | line_item/S_CF | - | standalone CF Operating profit before working capital changes; 2 cells; line 1117
R1513-R1514 | line_item/S_CF | - | standalone CF (lncrease)/decrease in trade and other receivables; 2 cells; line 1119
R1515-R1516 | line_item/S_CF | - | standalone CF (lncrease)/decrease in inventories; 2 cells; line 1120
R1517-R1518 | line_item/S_CF | - | standalone CF lncrease/(decrease) in trade and other payables; 2 cells; line 1121
R1519-R1520 | line_item/S_CF | - | standalone CF Cash generated from operations; 2 cells; line 1122
R1521-R1522 | line_item/S_CF | - | standalone CF Direct taxes paid (net); 2 cells; line 1123
R1523-R1524 | line_item/S_CF | - | standalone CF Net cash generated from operating activities; 2 cells; line 1124
R1525-R1526 | line_item/S_CF | - | standalone CF Purchase of Property, plant and equipment, Investment property and; 2 cells; line 1126
R1527-R1528 | line_item/S_CF | - | standalone CF Sale of Property, plant and equipment, Investment property and; 2 cells; line 1127
R1529-R1530 | line_item/S_CF | - | standalone CF Investment In subsidiaries, associates and joint venture companies; 2 cells; line 1128
R1531-R1532 | line_item/S_CF | ZERO_STANDING | standalone CF Divestment of stake In subsidiaries, associates and joint venture; 2 cells; line 1129
R1533-R1534 | line_item/S_CF | - | standalone CF Purchase of non-current Investments; 2 cells; line 1131
R1535-R1536 | line_item/S_CF | ZERO_STANDING | standalone CF Sale of non-current Investments; 2 cells; line 1132
R1537-R1538 | line_item/S_CF | - | standalone CF (Purchase)/sale of current Investments (net); 2 cells; line 1133
R1539-R1540 | line_item/S_CF | - | standalone CF Change In other bank balances and cash not availabe; 2 cells; line 1134
R1541-R1542 | line_item/S_CF | - | standalone CF long term deposits/loans (given) - subsidiaries, associates, joint venture; 2 cells; line 1135
R1543-R1544 | line_item/S_CF | ZERO_STANDING | standalone CF long term deposits/loans repaid - subsidiaries, associates, Joint venture; 2 cells; line 1137
R1545-R1546 | line_item/S_CF | - | standalone CF Short term deposits/loans (given)/repaid (net) - subsidiaries, associates, joint; 2 cells; line 1140
R1547-R1548 | line_item/S_CF | - | standalone CF Interest received; 2 cells; line 1142
R1549-R1550 | line_item/S_CF | - | standalone CF Dividend received from subsidiaries, joint venture and associate companies; 2 cells; line 1143
R1551-R1552 | line_item/S_CF | - | standalone CF Dividend received on other investments; 2 cells; line 1144
R1553-R1554 | line_item/S_CF | - | standalone CF Net cash generated from! (used in) Investing activities; 2 cells; line 1145
R1555-R1556 | line_item/S_CF | - | standalone CF Proceeds from issue of share capital (including share application; 2 cells; line 1147
R1557-R1558 | line_item/S_CF | - | standalone CF Proceeds from non-currerit borrowings; 2 cells; line 1148
R1559-R1560 | line_item/S_CF | ZERO_STANDING | standalone CF Repayments of non-current borrowings; 2 cells; line 1149
R1561-R1562 | line_item/S_CF | - | standalone CF Proceeds/(repayments) from other borrowings (net); 2 cells; line 1150
R1563-R1564 | line_item/S_CF | - | standalone CF Settlement of derivative contracts related to borrowings; 2 cells; line 1151
R1565-R1566 | line_item/S_CF | - | standalone CF Interest paid on lease liability; 2 cells; line 1152
R1567-R1568 | line_item/S_CF | - | standalone CF Repayment of lease liability; 2 cells; line 1153
R1569-R1570 | line_item/S_CF | - | standalone CF Dividends paid; 2 cells; line 1154
R1571-R1572 | line_item/S_CF | - | standalone CF Interest paid (including cash flows from interest rate swaps); 2 cells; line 1155
R1573-R1574 | line_item/S_CF | - | standalone CF Net cash used in financing activities; 2 cells; line 1156
R1575-R1576 | line_item/S_CF | - | standalone CF Net lncrease/(decrease) in cash and cash equivalents (A+ B; 2 cells; line 1157
R1577-R1578 | line_item/S_CF | - | standalone CF Cash and cash equlvalents at beginning of the period; 2 cells; line 1158
R1579-R1580 | line_item/S_CF | - | standalone CF Effect of exchange rate changes on cash and cash; 2 cells; line 1159
R1581-R1582 | line_item/S_CF | - | standalone CF Cash and cash equivalents at end of the period; 2 cells; line 1160
R2291-R2292 | S_CF_date | - | table headers, period labels, qualifiers for S_CF; 2 rows; lines 1099
R2468-R2469 | S_CF_qualifier | - | table headers, period labels, qualifiers for S_CF; 2 rows; lines 1097-1098
### S_SEG (STANDALONE Segment revenue, results, assets, liabilities; fulltext lines 1181-1232)
R1583-R1588 | line_item/S_SEG | - | standalone segment Gross segment revenue: Infrastructure & Utilities; 6 cells; line 1190
R1589-R1594 | line_item/S_SEG | - | standalone segment Gross segment revenue: Energy - Conventional; 6 cells; line 1191
R1595-R1600 | line_item/S_SEG | - | standalone segment Gross segment revenue: Energy - Green; 6 cells; line 1192
R1601-R1606 | line_item/S_SEG | - | standalone segment Gross segment revenue: Manufacturing & Products; 6 cells; line 1193
R1607-R1612 | line_item/S_SEG | - | standalone segment Gross segment revenue: Others; 6 cells; line 1194
R1613-R1618 | line_item/S_SEG | - | standalone segment Gross segment revenue: Total; 6 cells; line 1195
R1619-R1624 | line_item/S_SEG | - | standalone segment Gross segment revenue: Less: Inter-segment revenue; 6 cells; line 1196
R1625-R1630 | line_item/S_SEG | - | standalone segment Gross segment revenue: Net segment revenue; 6 cells; line 1197
R1631-R1636 | line_item/S_SEG | - | standalone segment Segment results: Infrastructure & Uti!ities; 6 cells; line 1199
R1637-R1642 | line_item/S_SEG | - | standalone segment Segment results: Energy - Conventional; 6 cells; line 1200
R1643-R1648 | line_item/S_SEG | - | standalone segment Segment results: Energy - Green; 6 cells; line 1201
R1649-R1654 | line_item/S_SEG | - | standalone segment Segment results: Manufacturing & Products; 6 cells; line 1202
R1655-R1660 | line_item/S_SEG | - | standalone segment Segment results: Others; 6 cells; line 1203
R1661-R1666 | line_item/S_SEG | - | standalone segment Segment results: Total; 6 cells; line 1204
R1667-R1672 | line_item/S_SEG | - | standalone segment Segment results: Less: Inter-segment margins on capital jobs; 6 cells; line 1205
R1673-R1678 | line_item/S_SEG | - | standalone segment Segment results: Less: Finance costs; 6 cells; line 1206
R1679-R1684 | line_item/S_SEG | - | standalone segment Segment results: Add: Unallocable corporate income net of expenditure; 6 cells; line 1207
R1685-R1690 | line_item/S_SEG | - | standalone segment Segment results: Profit before exceptional Items and tax; 6 cells; line 1208
R1691-R1696 | line_item/S_SEG | ZERO_STANDING | standalone Segment results: Exceptional items (loss); 6 cells; line 1210-1211
R1697-R1702 | line_item/S_SEG | - | standalone segment Segment results: ProfiU(loss) before tax; 6 cells; line 1212
R1703-R1708 | line_item/S_SEG | - | standalone segment Segment assets: Infrastructure & Utilities; 6 cells; line 1214
R1709-R1714 | line_item/S_SEG | - | standalone segment Segment assets: Energy - Conventional; 6 cells; line 1215
R1715-R1720 | line_item/S_SEG | - | standalone segment Segment assets: Energy - Green; 6 cells; line 1216
R1721-R1726 | line_item/S_SEG | - | standalone segment Segment assets: Manufacturing & Products; 6 cells; line 1217
R1727-R1732 | line_item/S_SEG | - | standalone segment Segment assets: Others; 6 cells; line 1218
R1733-R1738 | line_item/S_SEG | - | standalone segment Segment assets: Total segment assets; 6 cells; line 1219
R1739-R1744 | line_item/S_SEG | - | standalone segment Segment assets: Less: Inter-segment assets; 6 cells; line 1220
R1745-R1750 | line_item/S_SEG | - | standalone segment Segment assets: Add: Unallocable corporate assets; 6 cells; line 1221
R1751-R1756 | line_item/S_SEG | - | standalone segment Segment assets: Total assets; 6 cells; line 1222
R1757-R1762 | line_item/S_SEG | - | standalone segment Segment liabilities: Infrastructure & Utilities; 6 cells; line 1224
R1763-R1768 | line_item/S_SEG | - | standalone segment Segment liabilities: Energy - Conventional; 6 cells; line 1225
R1769-R1774 | line_item/S_SEG | - | standalone segment Segment liabilities: Energy- Green; 6 cells; line 1226
R1775-R1780 | line_item/S_SEG | - | standalone segment Segment liabilities: Manufacturing & Products; 6 cells; line 1227
R1781-R1786 | line_item/S_SEG | - | standalone segment Segment liabilities: Others; 6 cells; line 1228
R1787-R1792 | line_item/S_SEG | - | standalone segment Segment liabilities: Total segment liabilities; 6 cells; line 1229
R1793-R1798 | line_item/S_SEG | - | standalone segment Segment liabilities: Less : Inter-segment liabilities; 6 cells; line 1230
R1799-R1804 | line_item/S_SEG | - | standalone segment Segment liabilities: Add : Unallocable corporate liabilities; 6 cells; line 1231
R1805-R1810 | line_item/S_SEG | - | standalone segment Segment liabilities: Total liabilities; 6 cells; line 1232
R2297-R2302 | S_SEG_date | - | table headers, period labels, qualifiers for S_SEG; 6 rows; lines 1184
R2474-R2475 | S_SEG_qualifier | - | table headers, period labels, qualifiers for S_SEG; 2 rows; lines 1182-1183

## 6. NOTES (numbered and lettered notes, footnotes, formula notes)
ROW_ID(s) | category | A2 flags | cross-ref / materiality note
R485, R2396 | note/N_C_i | - | Consol note (i): ESOP allotment 1,65,811 shares; 2 A1 rows; lines 515. RESTATED consol vs standalone (same 1,65,811 shares).
R1928-R1929, R2133, R2227-R2230, R2397 | note/N_C_ii | - | Consol note (ii): SPA with Hyderabad Metro Rail Ltd, divestment of LTMRHL, held for sale; 8 A1 rows; lines 516-518. RESTATED consol vs standalone (LTMRHL divestment); also press release page 7.
R2401 | note/N_C_iv | - | Consol note (iv): standalone specified items disclosed; 1 A1 rows; lines 595.
R2405 | note/N_C_a | - | Consol ratio note (a): diversified nature of businesses; 1 A1 rows; lines 642.
R2246-R2247, R2406 | note/N_C_b | - | Consol ratio note (b): ratios exclude held-for-sale; 3 A1 rows; lines 643.
R702, R2248-R2249, R2407 | note/N_C_c | - | Consol ratio note (c): debt-equity including HFS borrowings; 4 A1 rows; lines 645-646.
R703, R2408-R2425 | note/N_C_d | - | Consol ratio note (d): formulae 1-12 and asterisk footnotes; 19 A1 rows; lines 647-688.
R2426 | note/N_C_nm | - | Consol ratio footnote: inventory turnover not material to the Group; 1 A1 rows; lines 698.
R2252, R2430 | note/N_C_cf1 | - | Consol CF note 1: indirect method, Ind AS 7; 2 A1 rows; lines 770-771.
R2431 | note/N_C_cf2 | - | Consol CF note 2: PPE and intangibles adjusted for CWIP movement; 1 A1 rows; lines 772.
R2432 | note/N_C_vii | - | Consol note (vii): regrouping of previous periods; 1 A1 rows; lines 774.
R2253-R2254, R2433 | note/N_C_viii | - | Consol note (viii): basis of preparation, Audit Committee review, Board approval 27-Oct-2026; 3 A1 rows; lines 775-778.
R2436 | note/N_C_sI | - | Consol segment note (I): Ind AS 108; 1 A1 rows; lines 849.
R1930, R2134, R2262-R2263, R2437 | note/N_C_sII | - | Consol segment note (II): Lakshya 2031 re-segmentation from 01-Apr-2026; 5 A1 rows; lines 852. Segment realignment; prior periods regrouped (comparability, for A3).
R2438 | note/N_C_sIII | - | Consol segment note (III): revised segment composition; 1 A1 rows; lines 860.
R2439 | note/N_C_sIV | - | Consol segment note (IV): segment revenue/result definitions, unallocable items; 1 A1 rows; lines 876.
R2440 | note/N_C_sV | - | Consol segment note (V): revenue and margin do not accrue uniformly; 1 A1 rows; lines 884.
R2441 | note/N_C_sVI | - | Consol segment note (VI): regrouping of previous periods; 1 A1 rows; lines 885.
R1305, R2446 | note/N_S_i | - | Standalone note (i): ESOP allotment 1,65,811 shares; 2 A1 rows; lines 958. RESTATED consol vs standalone (same 1,65,811 shares).
R1931-R1932, R2135, R2273-R2275, R2447 | note/N_S_ii | - | Standalone note (ii): Scheme of Arrangement, Realty Undertaking slump sale to LTRPL, NCLT approval pending; 7 A1 rows; lines 959-962. Standalone-only note; no consolidated equivalent note.
R1933, R2136, R2276-R2278, R2448 | note/N_S_iii | - | Standalone note (iii): SPA for LTMRHL divestment, completion revised to 31-Dec-2026; 6 A1 rows; lines 964-966. RESTATED consol vs standalone (LTMRHL divestment); also press release page 7.
R1934-R1935, R2137, R2279-R2281, R2449 | note/N_S_iv | - | Standalone note (iv): BTA data center and cloud business to Vyoma.AI; LTNS stake SPA; held for sale; 7 A1 rows; lines 967-970. Standalone-only note; no consolidated equivalent note.
R2453 | note/N_S_r15 | - | Standalone ratio item 15: no secured listed NCDs issued; 1 A1 rows; lines 1065. No secured listed NCDs; compare Annexure III NCD (Rs 500 crore, tokenised).
R1486, R2454-R2466 | note/N_S_form | - | Standalone ratio Note: formulae 1-12; 14 A1 rows; lines 1066-1092.
R2467 | note/N_S_nm | - | Standalone ratio footnote: inventory turnover not material to the Company; 1 A1 rows; lines 1094.
R2293, R2470 | note/N_S_cf1 | - | Standalone CF note 1: indirect method, Ind AS 7; 2 A1 rows; lines 1162-1163.
R2471 | note/N_S_cf2 | - | Standalone CF note 2: PPE and intangibles adjusted for CWIP movement; 1 A1 rows; lines 1164.
R2472 | note/N_S_viii | - | Standalone note (viii): regrouping of previous periods; 1 A1 rows; lines 1166.
R2294-R2295, R2473 | note/N_S_ix | - | Standalone note (ix): basis of preparation, Audit Committee review, Board approval 27-Oct-2026; 3 A1 rows; lines 1167-1170.
R2476 | note/N_S_sI | - | Standalone segment note (I): Ind AS 108; 1 A1 rows; lines 1234.
R2138, R2303-R2304, R2477 | note/N_S_sII | - | Standalone segment note (II): Lakshya 2031 re-segmentation; 4 A1 rows; lines 1236. Segment realignment; prior periods regrouped (comparability, for A3).
R2478 | note/N_S_sIII | - | Standalone segment note (III): revised segment composition; 1 A1 rows; lines 1244.
R2479 | note/N_S_sIV | - | Standalone segment note (IV): definitions, unallocable items; 1 A1 rows; lines 1256.
R2480 | note/N_S_sV | - | Standalone segment note (V): revenue and margin do not accrue uniformly; 1 A1 rows; lines 1259.
R2481 | note/N_S_sVI | - | Standalone segment note (VI): regrouping of previous periods; 1 A1 rows; lines 1260.
R486 | note/C(iii) | HEADING_ONLY | Consol note (iii): Statement of Assets and Liabilities heading; heading at fulltext line 521 (no own A1 row); anchor = first table row of C_BS at line 530
R618 | note/C(v) | HEADING_ONLY | Consol note (v): Reg 52(4) additional disclosures heading; heading at fulltext line 620 (no own A1 row); anchor = first table row of C_RAT at line 627
R704 | note/C(vi) | HEADING_ONLY | Consol note (vi): Statement of Cash Flows heading; heading at fulltext line 703 (no own A1 row); anchor = first table row of C_CF at line 708
R1306 | note/S(v) | HEADING_ONLY | Standalone note (v): Statement of Assets and Liabilities heading; heading at fulltext line 973 (no own A1 row); anchor = first table row of S_BS at line 981
R1402 | note/S(vi) | HEADING_ONLY | Standalone note (vi): Reg 52(4) additional disclosures heading; heading at fulltext line 1047 (no own A1 row); anchor = first table row of S_RAT at line 1051
R1487 | note/S(vii) | HEADING_ONLY | Standalone note (vii): Statement of Cash Flows heading; heading at fulltext line 1097 (no own A1 row); anchor = first table row of S_CF at line 1103

## 7. AUDITOR REPORTS (both limited review reports), paragraph by paragraph
ROW_ID(s) | category | A2 flags | cross-ref / materiality note
R1936, R2306 | auditor_para/AC0 | - | CONSOL LRR: letterhead, title, addressee; 2 rows; lines 1285-1287; types DAT1 ENT1
R2307-R2310 | auditor_para/AC1 | - | CONSOL LRR para 1: scope, entities, review period; 4 rows; lines 1292-1297; types DAT4
R2311 | auditor_para/AC2 | - | CONSOL LRR para 2: management responsibility, Ind AS 34; 1 rows; lines 1301; types DAT1
R2482 | auditor_para/AC3 | - | CONSOL LRR para 3: SRE 2410 review scope, Reg 33(8) circular; 1 rows; lines 1305; types QUA1
R2483 | auditor_para/AC4 | NO_OWN_ROW (prose with no number/entity/date; anchored to nearest A1 row) | CONSOL LRR para 4: entities listed in Annexure A; lines 1315-1316
R2483 | auditor_para/AC5 | UNMODIFIED_CONCLUSION; no EOM; no going concern text | CONSOL LRR para 5: conclusion (unmodified; relies on other auditors, paras 6-7); 1 rows; lines 1317; types QUA1
R1811 | auditor_para/ACF1 | NO_OWN_ROW (prose with no number/entity/date; anchored to nearest A1 row) | CONSOL LRR page 21 footer (registered office, offices); lines 1324-1327
R1811-R1819, R2312-R2317, R2484-R2485 | auditor_para/AC6 | OTHER_AUDITOR_RELIED | CONSOL LRR para 6: 11 joint operations not reviewed by us (other auditors); conclusion not modified; 17 rows; lines 1332-1343; types DAT6 NUM9 QUA2
R1820-R1834, R2318-R2326, R2486-R2487 | auditor_para/AC7 | OTHER_AUDITOR_RELIED | CONSOL LRR para 7: 42 subsidiaries reviewed by other auditors; conclusion not modified; 26 rows; lines 1345-1361; types DAT9 NUM15 QUA2
R1835-R1849, R2327-R2335, R2488-R2489 | auditor_para/AC8 | MGMT_FURNISHED_UNREVIEWED | CONSOL LRR para 8: 41 subsidiaries not reviewed by their auditors (management furnished); 26 rows; lines 1363-1388; types DAT9 NUM15 QUA2
R1850-R1858, R2336-R2341, R2490-R2492 | auditor_para/AC9 | MGMT_FURNISHED_UNREVIEWED | CONSOL LRR para 9: 23 joint operations not subject to review (management furnished); 18 rows; lines 1390-1401; types DAT6 NUM9 QUA3
R1937-R1939, R2342 | auditor_para/ACS | UDIN_OCR_GARBLED | CONSOL LRR signature: firm, partner, membership, UDIN, place, date; 4 rows; lines 1406-1414; types DAT1 ENT3
R1940 | auditor_para/ACF2 | NO_OWN_ROW (prose with no number/entity/date; anchored to nearest A1 row) | CONSOL LRR page 23 footer; lines 1415-1418
R2083 | auditor_para/ACF3 | NO_OWN_ROW (prose with no number/entity/date; anchored to nearest A1 row) | Annexure A page 28 footer; lines 1669-1673
R2083, R2348 | auditor_para/AS0 | - | STANDALONE LRR: letterhead, title, addressee; 2 rows; lines 1684-1686; types DAT1 ENT1
R2349-R2352 | auditor_para/AS1 | - | STANDALONE LRR para 1: scope incl joint operations proportionate; 4 rows; lines 1690-1694; types DAT4
R2353 | auditor_para/AS2 | - | STANDALONE LRR para 2: management responsibility; 1 rows; lines 1698; types DAT1
R2500 | auditor_para/AS3 | - | STANDALONE LRR para 3: SRE 2410 review scope; 1 rows; lines 1701; types QUA1
R2501 | auditor_para/AS4 | NO_OWN_ROW (prose with no number/entity/date; anchored to nearest A1 row) | STANDALONE LRR para 4: joint operations in Annexure A; lines 1711-1711
R2501 | auditor_para/AS5 | UNMODIFIED_CONCLUSION; no EOM; no going concern text | STANDALONE LRR para 5: conclusion (unmodified); 1 rows; lines 1712; types QUA1
R1859-R1867, R2354-R2359, R2502-R2503 | auditor_para/AS6 | OTHER_AUDITOR_RELIED | STANDALONE LRR para 6: 10 joint operations reviewed by other auditors; conclusion not modified; 17 rows; lines 1727-1738; types DAT6 NUM9 QUA2
R1868-R1876, R2360-R2365, R2504-R2506 | auditor_para/AS7 | MGMT_FURNISHED_UNREVIEWED | STANDALONE LRR para 7: 22 joint operations not subject to review (management furnished); 18 rows; lines 1740-1752; types DAT6 NUM9 QUA3
R2084-R2086, R2366 | auditor_para/ASS | UDIN_OCR_GARBLED | STANDALONE LRR signature: firm, partner, membership, UDIN, place, date; 4 rows; lines 1757-1765; types DAT1 ENT3
R2087 | auditor_para/ASF | NO_OWN_ROW (prose with no number/entity/date; anchored to nearest A1 row) | STANDALONE LRR page 30 footer; lines 1766-1769
Arithmetic cross-ref only: consolidated joint operations 11 (other auditors) + 23 (unreviewed) = 34 = joint operations in the consolidated Annexure A; standalone 10 + 22 = 32 = joint operations in the standalone Annexure A. Consolidated subsidiaries 42 + 41 = 83 of 94 listed; 11 remainder reviewed by MSKA directly. A3 to reconcile.

## 8. ANNEXURE A ENTITIES (consolidated list pages 24-27, standalone list page 31): one row per entity
ROW_ID(s) | category | A2 flags | cross-ref / materiality note
R1940 | entity/subsidiary #1 | - | Annexure A consolidated list; line 1430
R1941 | entity/subsidiary #2 | - | Annexure A consolidated list; line 1431
R1942 | entity/subsidiary #3 | - | Annexure A consolidated list; line 1432
R1943 | entity/subsidiary #4 | - | Annexure A consolidated list; line 1433
R1944 | entity/subsidiary #5 | - | Annexure A consolidated list; line 1434
R1945 | entity/subsidiary #6 | LIQUIDATION(symbol a) | Annexure A consolidated list; line 1435
R1946 | entity/subsidiary #7 | - | Annexure A consolidated list; line 1436
R1947 | entity/subsidiary #8 | - | Annexure A consolidated list; line 1437
R1948 | entity/subsidiary #9 | - | Annexure A consolidated list; line 1438
R1949 | entity/subsidiary #10 | - | Annexure A consolidated list; line 1439
R1950 | entity/subsidiary #11 | - | Annexure A consolidated list; line 1440
R1951 | entity/subsidiary #12 | - | Annexure A consolidated list; line 1441
R1952 | entity/subsidiary #13 | - | Annexure A consolidated list; line 1442
R1953 | entity/subsidiary #14 | - | Annexure A consolidated list; line 1443
R1954 | entity/subsidiary #15 | LIQUIDATION(symbol a) | Annexure A consolidated list; line 1444
R1955 | entity/subsidiary #16 | - | Annexure A consolidated list; line 1445
R1956 | entity/subsidiary #17 | - | Annexure A consolidated list; line 1446
R1957 | entity/subsidiary #18 | - | Annexure A consolidated list; line 1447
R1958 | entity/subsidiary #19 | - | Annexure A consolidated list; line 1448
R1959 | entity/subsidiary #20 | - | Annexure A consolidated list; line 1449
R1960 | entity/subsidiary #21 | - | Annexure A consolidated list; line 1450
R1961 | entity/subsidiary #22 | - | Annexure A consolidated list; line 1451
R1962 | entity/subsidiary #23 | - | Annexure A consolidated list; line 1452
R1963 | entity/subsidiary #24 | - | Annexure A consolidated list; line 1454
R1964 | entity/subsidiary #25 | - | Annexure A consolidated list; line 1455
R1965 | entity/subsidiary #26 | - | Annexure A consolidated list; line 1456
R1966 | entity/subsidiary #27 | - | Annexure A consolidated list; line 1457
R1967 | entity/subsidiary #28 | - | Annexure A consolidated list; line 1458
R1968 | entity/subsidiary #29 | - | Annexure A consolidated list; line 1459
R1969 | entity/subsidiary #30 | - | Annexure A consolidated list; line 1460
R1970 | entity/subsidiary #31 | - | Annexure A consolidated list; line 1461
R1971 | entity/subsidiary #32 | - | Annexure A consolidated list; line 1462
R1972 | entity/subsidiary #33 | - | Annexure A consolidated list; line 1463
R1973 | entity/subsidiary #34 | - | Annexure A consolidated list; line 1475
R1974 | entity/subsidiary #35 | - | Annexure A consolidated list; line 1476
R1975 | entity/subsidiary #36 | - | Annexure A consolidated list; line 1477
R1976 | entity/subsidiary #37 | - | Annexure A consolidated list; line 1478
R1977 | entity/subsidiary #38 | - | Annexure A consolidated list; line 1479
R1978 | entity/subsidiary #39 | - | Annexure A consolidated list; line 1480
R1979 | entity/subsidiary #40 | - | Annexure A consolidated list; line 1481
R1980 | entity/subsidiary #41 | - | Annexure A consolidated list; line 1482
R1981 | entity/subsidiary #42 | - | Annexure A consolidated list; line 1483
R1982 | entity/subsidiary #43 | - | Annexure A consolidated list; line 1484
R1983 | entity/subsidiary #44 | - | Annexure A consolidated list; line 1485
R1984 | entity/subsidiary #45 | - | Annexure A consolidated list; line 1486
R1985 | entity/subsidiary #46 | - | Annexure A consolidated list; line 1487
R1986 | entity/subsidiary #47 | - | Annexure A consolidated list; line 1488
R1987 | entity/subsidiary #48 | - | Annexure A consolidated list; line 1489
R1988 | entity/subsidiary #49 | - | Annexure A consolidated list; line 1490
R1989 | entity/subsidiary #50 | - | Annexure A consolidated list; line 1491
R1990 | entity/subsidiary #51 | - | Annexure A consolidated list; line 1492
R1991 | entity/subsidiary #52 | - | Annexure A consolidated list; line 1493
R1992 | entity/subsidiary #53 | - | Annexure A consolidated list; line 1494
R1993 | entity/subsidiary #54 | - | Annexure A consolidated list; line 1495
R1994 | entity/subsidiary #55 | - | Annexure A consolidated list; line 1496
R1995 | entity/subsidiary #56 | - | Annexure A consolidated list; line 1497
R1996 | entity/subsidiary #57 | - | Annexure A consolidated list; line 1498; LTMRHL held for sale, still listed; xref R1929, R1933
R1997 | entity/subsidiary #58 | - | Annexure A consolidated list; line 1499
R1998 | entity/subsidiary #59 | - | Annexure A consolidated list; line 1500
R1999 | entity/subsidiary #60 | ENTITY_CHANGE(divested, symbol f) | Annexure A consolidated list; line 1501; xref R1914 (press release: divested 25-Jun-2026); OCR marker
R2000 | entity/subsidiary #61 | - | Annexure A consolidated list; line 1502
R2001 | entity/subsidiary #62 | - | Annexure A consolidated list; line 1503
R2002 | entity/subsidiary #63 | - | Annexure A consolidated list; line 1504
R2003 | entity/subsidiary #64 | - | Annexure A consolidated list; line 1505
R2004 | entity/subsidiary #65 | - | Annexure A consolidated list; line 1506
R2005 | entity/subsidiary #66 | - | Annexure A consolidated list; line 1507
R2006 | entity/subsidiary #67 | - | Annexure A consolidated list; line 1508
R2007 | entity/subsidiary #68 | - | Annexure A consolidated list; line 1509
R2008 | entity/subsidiary #69 | - | Annexure A consolidated list; line 1510
R2009 | entity/subsidiary #70 | - | Annexure A consolidated list; line 1511
R2010 | entity/subsidiary #71 | - | Annexure A consolidated list; line 1512
R2011 | entity/subsidiary #72 | - | Annexure A consolidated list; line 1513
R2012 | entity/subsidiary #73 | - | Annexure A consolidated list; line 1560
R2013 | entity/subsidiary #74 | - | Annexure A consolidated list; line 1561
R2014 | entity/subsidiary #75 | - | Annexure A consolidated list; line 1562
R2015 | entity/subsidiary #76 | - | Annexure A consolidated list; line 1563
R2016 | entity/subsidiary #77 | - | Annexure A consolidated list; line 1564
R2017 | entity/subsidiary #78 | - | Annexure A consolidated list; line 1565
R2018 | entity/subsidiary #79 | - | Annexure A consolidated list; line 1566
R2019 | entity/subsidiary #80 | - | Annexure A consolidated list; line 1567
R2020 | entity/subsidiary #81 | - | Annexure A consolidated list; line 1568
R2021 | entity/subsidiary #82 | - | Annexure A consolidated list; line 1569
R2022 | entity/subsidiary #83 | - | Annexure A consolidated list; line 1570
R2023 | entity/subsidiary #84 | - | Annexure A consolidated list; line 1571
R2024 | entity/subsidiary #85 | - | Annexure A consolidated list; line 1572
R2025 | entity/subsidiary #86 | - | Annexure A consolidated list; line 1573
R2026 | entity/subsidiary #87 | - | Annexure A consolidated list; line 1574
R2027 | entity/subsidiary #88 | - | Annexure A consolidated list; line 1575
R2028 | entity/subsidiary #89 | - | Annexure A consolidated list; line 1576
R2029 | entity/subsidiary #90 | - | Annexure A consolidated list; line 1577
R2030 | entity/subsidiary #91 | ENTITY_CHANGE(added, symbol b) | Annexure A consolidated list; line 1578
R2031 | entity/subsidiary #92 | ENTITY_CHANGE(added, symbol c) | Annexure A consolidated list; line 1579; xref R1934 (standalone note iv)
R2032 | entity/subsidiary #93 | ENTITY_CHANGE(added, symbol e) | Annexure A consolidated list; line 1580
R2033 | entity/subsidiary #94 | ENTITY_CHANGE(added, symbol e) | Annexure A consolidated list; line 1581
R2034 | entity/associate #1 | LIQUIDATION(symbol a) | Annexure A consolidated list; line 1583
R2035 | entity/associate #2 | LIQUIDATION(symbol a) | Annexure A consolidated list; line 1584
R2036 | entity/associate #3 | LIQUIDATION(symbol a) | Annexure A consolidated list; line 1585
R2037 | entity/associate #4 | - | Annexure A consolidated list; line 1586
R2038 | entity/associate #5 | - | Annexure A consolidated list; line 1587
R2039 | entity/associate #6 | ENTITY_CHANGE(added, symbol d) | Annexure A consolidated list; line 1588
R2040 | entity/joint venture #1 | - | Annexure A consolidated list; line 1590
R2041 | entity/joint venture #2 | - | Annexure A consolidated list; line 1591
R2042 | entity/joint venture #3 | - | Annexure A consolidated list; line 1592
R2043 | entity/joint venture #4 | - | Annexure A consolidated list; line 1593
R2044 | entity/joint venture #5 | - | Annexure A consolidated list; line 1594
R2045 | entity/joint venture #6 | - | Annexure A consolidated list; line 1595
R2046 | entity/joint venture #7 | - | Annexure A consolidated list; line 1596
R2047 | entity/joint venture #8 | - | Annexure A consolidated list; line 1608
R2048 | entity/joint venture #9 | - | Annexure A consolidated list; line 1609
R2049 | entity/joint operation #1 | - | Annexure A consolidated list; line 1611
R2050 | entity/joint operation #2 | - | Annexure A consolidated list; line 1612
R2051 | entity/joint operation #3 | - | Annexure A consolidated list; line 1613
R2052 | entity/joint operation #4 | - | Annexure A consolidated list; line 1614
R2053 | entity/joint operation #5 | - | Annexure A consolidated list; line 1615
R2054 | entity/joint operation #6 | - | Annexure A consolidated list; line 1616
R2055 | entity/joint operation #7 | - | Annexure A consolidated list; line 1617
R2056 | entity/joint operation #8 | - | Annexure A consolidated list; line 1618
R2057 | entity/joint operation #9 | - | Annexure A consolidated list; line 1619
R2058 | entity/joint operation #10 | - | Annexure A consolidated list; line 1620
R2059 | entity/joint operation #11 | - | Annexure A consolidated list; line 1621
R2060 | entity/joint operation #12 | - | Annexure A consolidated list; line 1622
R2061 | entity/joint operation #13 | - | Annexure A consolidated list; line 1623
R2062 | entity/joint operation #14 | - | Annexure A consolidated list; line 1624
R2063 | entity/joint operation #15 | - | Annexure A consolidated list; line 1625
R2064 | entity/joint operation #16 | - | Annexure A consolidated list; line 1626
R2065 | entity/joint operation #17 | - | Annexure A consolidated list; line 1627
R2066 | entity/joint operation #18 | - | Annexure A consolidated list; line 1628
R2067 | entity/joint operation #19 | - | Annexure A consolidated list; line 1629
R2068 | entity/joint operation #20 | - | Annexure A consolidated list; line 1630
R2069 | entity/joint operation #21 | - | Annexure A consolidated list; line 1631
R2070 | entity/joint operation #22 | - | Annexure A consolidated list; line 1632
R2071 | entity/joint operation #23 | - | Annexure A consolidated list; line 1635
R2072 | entity/joint operation #24 | - | Annexure A consolidated list; line 1636
R2073 | entity/joint operation #25 | - | Annexure A consolidated list; line 1637
R2074 | entity/joint operation #26 | - | Annexure A consolidated list; line 1638
R2075 | entity/joint operation #27 | - | Annexure A consolidated list; line 1639
R2076 | entity/joint operation #28 | - | Annexure A consolidated list; line 1640
R2077 | entity/joint operation #29 | - | Annexure A consolidated list; line 1641
R2078 | entity/joint operation #30 | - | Annexure A consolidated list; line 1642
R2079 | entity/joint operation #31 | - | Annexure A consolidated list; line 1643
R2080 | entity/joint operation #32 | - | Annexure A consolidated list; line 1644
R2081 | entity/joint operation #33 | - | Annexure A consolidated list; line 1645
R2082 | entity/joint operation #34 | - | Annexure A consolidated list; line 1646
R2087 | entity/parent / holding company | - | Annexure A standalone list; line 1810
R2088 | entity/joint operation #1 | - | Annexure A standalone list; line 1812
R2089 | entity/joint operation #2 | - | Annexure A standalone list; line 1813
R2090 | entity/joint operation #3 | - | Annexure A standalone list; line 1814
R2091 | entity/joint operation #4 | - | Annexure A standalone list; line 1815
R2092 | entity/joint operation #5 | - | Annexure A standalone list; line 1816
R2093 | entity/joint operation #6 | - | Annexure A standalone list; line 1817
R2094 | entity/joint operation #7 | - | Annexure A standalone list; line 1818
R2095 | entity/joint operation #8 | - | Annexure A standalone list; line 1819
R2096 | entity/joint operation #9 | - | Annexure A standalone list; line 1820
R2097 | entity/joint operation #10 | - | Annexure A standalone list; line 1821
R2098 | entity/joint operation #11 | - | Annexure A standalone list; line 1822
R2099 | entity/joint operation #12 | - | Annexure A standalone list; line 1823
R2100 | entity/joint operation #13 | - | Annexure A standalone list; line 1824
R2101 | entity/joint operation #14 | - | Annexure A standalone list; line 1825
R2102 | entity/joint operation #15 | - | Annexure A standalone list; line 1826
R2103 | entity/joint operation #16 | - | Annexure A standalone list; line 1827
R2104 | entity/joint operation #17 | - | Annexure A standalone list; line 1828
R2105 | entity/joint operation #18 | - | Annexure A standalone list; line 1829
R2106 | entity/joint operation #19 | - | Annexure A standalone list; line 1830
R2107 | entity/joint operation #20 | - | Annexure A standalone list; line 1831
R2108 | entity/joint operation #21 | - | Annexure A standalone list; line 1832
R2109 | entity/joint operation #22 | - | Annexure A standalone list; line 1833
R2110 | entity/joint operation #23 | - | Annexure A standalone list; line 1834
R2111 | entity/joint operation #24 | - | Annexure A standalone list; line 1835
R2112 | entity/joint operation #25 | - | Annexure A standalone list; line 1836
R2113 | entity/joint operation #26 | - | Annexure A standalone list; line 1837
R2114 | entity/joint operation #27 | - | Annexure A standalone list; line 1838
R2115 | entity/joint operation #28 | - | Annexure A standalone list; line 1839
R2116 | entity/joint operation #29 | - | Annexure A standalone list; line 1840
R2117 | entity/joint operation #30 | - | Annexure A standalone list; line 1841
R2118 | entity/joint operation #31 | - | Annexure A standalone list; line 1842
R2119 | entity/joint operation #32 | - | Annexure A standalone list; line 1843
R2493 | annexureA_other | - | non-entity A1 rows inside Annexure A lists (QUA1); lines 1501
R2343-R2347, R2494-R2499 | annexureA_legend | - | symbol a-f definitions; lines 1663-1668; DATE R2343-R2347; QUALIFIER R2494-R2499
ENTITY_CHANGE basis: no prior-quarter ledger (first LT run). Flags come from the filed symbol footnotes (b, c, d, e additions; f divestment), not a list diff.

## 9. OTHER ENTITIES (regulators, exchanges, counterparties, segments, businesses, auditor identifiers, instruments)
ROW_ID(s) | category | A2 flags | cross-ref / materiality note
R1885-R1887 | entity_other/AG0 | - | Board Outcome letter: header, addressee, subject (meeting of 27-Oct-2026); 3 rows; lines 20-30
R1888 | entity_other/AG1 | - | AGENDA ITEM 1: approval of consolidated and standalone unaudited results, quarter and half-year; 1 rows; lines 42
R1889 | entity_other/AG3 | - | AGENDA ITEM 3: Limited Review Report enclosed as Annexure II; 1 rows; lines 53
R1890 | entity_other/AG4 | - | AGENDA ITEM 4: Statement of utilisation / deviation, Reg 52(7), 52(7A), Annexure III; 1 rows; lines 58
R1891 | entity_other/AG5 | - | AGENDA ITEM 5: Reg 54(2), 54(3) security cover disclosure not applicable; 1 rows; lines 61
R1892 | entity_other/SIG1 | - | Signature block: Company Secretary (digital), Board Outcome letter; 1 rows; lines 90
R1893 | entity_other/PR3 | - | Press release page 3 (headline, group revenue, PAT, order inflow); 1 rows; lines 128
R1894-R1899 | entity_other/PR4 | - | Press release page 4 (orders, order book, CMD statement); 6 rows; lines 151-161
R1900-R1903 | entity_other/PR5 | - | Press release page 5 (Infrastructure & Utilities; Energy - Conventional); 4 rows; lines 186-211
R1904-R1910 | entity_other/PR6 | - | Press release page 6 (Energy - Green; Manufacturing & Products; Technology, Platforms & Services); 7 rows; lines 230-273
R1911-R1917 | entity_other/PR7 | - | Press release page 7 (Financial Services; Realty; Development Projects); 7 rows; lines 285-322
R1918-R1919 | entity_other/PR8 | - | Press release page 8 (Outlook; media contact); 2 rows; lines 340-366
R1920-R1927 | entity_other/AN2 | - | Annexure 2 Segment Composition; 8 rows; lines 429-451
R1928-R1929 | entity_other/N_C_ii | - | Consol note (ii): SPA with Hyderabad Metro Rail Ltd, divestment of LTMRHL, held for sale; 2 rows; lines 516-517
R1930 | entity_other/N_C_sII | - | Consol segment note (II): Lakshya 2031 re-segmentation from 01-Apr-2026; 1 rows; lines 852
R1931-R1932 | entity_other/N_S_ii | - | Standalone note (ii): Scheme of Arrangement, Realty Undertaking slump sale to LTRPL, NCLT approval pending; 2 rows; lines 959-962
R1933 | entity_other/N_S_iii | - | Standalone note (iii): SPA for LTMRHL divestment, completion revised to 31-Dec-2026; 1 rows; lines 965
R1934-R1935 | entity_other/N_S_iv | - | Standalone note (iv): BTA data center and cloud business to Vyoma.AI; LTNS stake SPA; held for sale; 2 rows; lines 968-969
R1936 | entity_other/AC0 | - | CONSOL LRR: letterhead, title, addressee; 1 rows; lines 1285
R1937-R1939 | entity_other/ACS | - | CONSOL LRR signature: firm, partner, membership, UDIN, place, date; 3 rows; lines 1406-1412
R2083 | entity_other/AS0 | - | STANDALONE LRR: letterhead, title, addressee; 1 rows; lines 1684
R2084-R2086 | entity_other/ASS | - | STANDALONE LRR signature: firm, partner, membership, UDIN, place, date; 3 rows; lines 1757-1761
R2120-R2121 | entity_other/A3A | - | Annexure III Part A: statement of utilisation of issue proceeds (NCD ISIN INE018A08BO8); 2 rows; lines 1884-1887
R2122 | entity_other/A3B | - | Annexure III Part B: statement of deviation/variation; 1 rows; lines 1897
R2123 | entity_other/SIG6 | - | Signature block: Company Secretary, Annexure III (page 33); 1 rows; lines 1952

## 10. ANNEXURE III (utilisation / deviation statements, pages 32-33)
ROW_ID(s) | category | A2 flags | cross-ref / materiality note
R1877-R1878 | annexure3/A3A/number | - | Annexure III Part A: statement of utilisation of issue proceeds (NCD ISIN INE018A08BO8); 2 rows; lines 1892
R2120-R2121 | annexure3/A3A/entity | - | Annexure III Part A: statement of utilisation of issue proceeds (NCD ISIN INE018A08BO8); 2 rows; lines 1884-1887
R2367 | annexure3/A3A/date | - | Annexure III Part A: statement of utilisation of issue proceeds (NCD ISIN INE018A08BO8); 1 rows; lines 1889
R2507 | annexure3/A3A/qualifier | - | Annexure III Part A: statement of utilisation of issue proceeds (NCD ISIN INE018A08BO8); 1 rows; lines 1849
R1879 | annexure3/A3B/number | - | Annexure III Part B: statement of deviation/variation; 1 rows; lines 1900
R2122 | annexure3/A3B/entity | - | Annexure III Part B: statement of deviation/variation; 1 rows; lines 1897
R2368-R2369 | annexure3/A3B/date | - | Annexure III Part B: statement of deviation/variation; 2 rows; lines 1899-1901
R2508-R2509 | annexure3/A3B/qualifier | - | Annexure III Part B: statement of deviation/variation; 2 rows; lines 1901-1902
R1880-R1884 | annexure3/A3C/number | ZERO_STANDING | Annexure III objects table and deviation definitions; 5 rows; lines 1938-1946
R2510-R2511 | annexure3/A3C/qualifier | - | Annexure III objects table and deviation definitions; 2 rows; lines 1934-1947
R2139 | annexure3/A3C/forward | - | Annexure III objects table and deviation definitions; 1 rows; lines 1939

## 11. INDEXES: ZERO_STANDING, FORWARD, RESTATED, ENTITY_CHANGE
ROW_ID(s) | category | A2 flags | cross-ref / materiality note
### 11a ZERO_STANDING (42 cells; 32 A1-flagged, 10 raised by A2: "0.00" bad-debt ratio cells that round to zero while FY26 column shows 0.01)
R181 | zero_standing | ZERO_STANDING | Annexure 1 segment Development Projects, Order inflow; 1 cells; line 394
R183 | zero_standing | ZERO_STANDING | Annexure 1 segment Development Projects, Customer revenue; 1 cells; line 394
R346-R350 | zero_standing | ZERO_STANDING | consol P&L Exceptional items [loss]; 5 cells; line 487
R648-R652 | zero_standing | ZERO_STANDING (A2-raised, 0.00) | consol ratios Bad debts to accounts receivable ratio; 5 cells; line 632
R727 | zero_standing | ZERO_STANDING | consol CF: (Gain)/loss on disposal of subsidiary/associate/business undertaking; 1 cells; line 720
R773 | zero_standing | ZERO_STANDING | consol CF: Consideration received on transfer of business undertaking; 1 cells; line 745
R775 | zero_standing | ZERO_STANDING | consol CF: Consideration received on disposal of subsidiaries/ divestment of part; 1 cells; line 746
R776 | zero_standing | ZERO_STANDING | consol CF: Consideration paid on acquisition of business; 1 cells; line 747
R780 | zero_standing | ZERO_STANDING | consol CF: Cash and cash equivalents acquired pursuant to acquisition of; 1 cells; line 749
R782 | zero_standing | ZERO_STANDING | consol CF: Consideration paid on acquisition of stake in an associate/joint; 1 cells; line 750
R795 | zero_standing | ZERO_STANDING | consol CF: Payment made for acquisition of additional stake in a; 1 cells; line 757
R860 | zero_standing | ZERO_STANDING | consol segment Gross segment revenue: Development Projects; 1 cells; line 802
R962-R966 | zero_standing | ZERO_STANDING | consol segment Segment results: Addl(less): Exceptional items (loss); 5 cells; line 820
R1214-R1215, R1217 | zero_standing | ZERO_STANDING | standalone P&L Exceptional Items (loss); 3 cells; line 936
R1432-R1436 | zero_standing | ZERO_STANDING (A2-raised, 0.00) | standalone ratios Bad debts to accounts receivable ratio; 5 cells; line 1056
R1532 | zero_standing | ZERO_STANDING | standalone CF Divestment of stake In subsidiaries, associates and joint venture; 1 cells; line 1129
R1536 | zero_standing | ZERO_STANDING | standalone CF Sale of non-current Investments; 1 cells; line 1132
R1544 | zero_standing | ZERO_STANDING | standalone CF long term deposits/loans repaid - subsidiaries, associates, Joint venture; 1 cells; line 1137
R1559 | zero_standing | ZERO_STANDING | standalone CF Repayments of non-current borrowings; 1 cells; line 1149
R1691-R1692, R1694 | zero_standing | ZERO_STANDING | standalone Segment results: Exceptional items (loss); 3 cells; line 1210-1211
R1883 | zero_standing | ZERO_STANDING | Annexure III: amount of deviation/variation for the quarter; 1 cells; line 1946
R1884 | zero_standing | ZERO_STANDING | Annexure III: deviation percentage; 1 cells; line 1946
### 11b FORWARD rows (16): forward-looking statement index
R2124 | forward_statement | FORWARD | page 4 line 166; bucket PR4
R2125 | forward_statement | FORWARD | page 4 line 168; bucket PR4
R2126 | forward_statement | FORWARD | page 4 line 172; bucket PR4
R2127 | forward_statement | FORWARD | page 7 line 305; bucket PR7
R2128 | forward_statement | FORWARD | page 7 line 325; bucket PR7
R2129 | forward_statement | FORWARD | page 8 line 337; bucket PR8
R2130 | forward_statement | FORWARD | page 8 line 343; bucket PR8
R2131 | forward_statement | FORWARD | page 8 line 347; bucket PR8
R2132 | forward_statement | FORWARD | page 8 line 352; bucket PR8
R2133 | forward_statement | FORWARD | page 11 line 516; bucket N_C_ii
R2134 | forward_statement | FORWARD | page 15 line 852; bucket N_C_sII
R2135 | forward_statement | FORWARD | page 16 line 959; bucket N_S_ii
R2136 | forward_statement | FORWARD | page 16 line 964; bucket N_S_iii
R2137 | forward_statement | FORWARD | page 16 line 967; bucket N_S_iv
R2138 | forward_statement | FORWARD | page 20 line 1236; bucket N_S_sII
R2139 | forward_statement | FORWARD | page 33 line 1939; bucket A3C
### 11c RESTATED headline numbers
Consol revenue Q2: R001, R007 (PR 78,750) | R097, R187 (Annexure 1) | R244 (P&L 78749.94) | R878 (segment net revenue) | restated_xref | RESTATED | cross-reference only; verbatim values at the IDs
Consol revenue H1: R011 (PR 146,692) | R247 (P&L 146691.68) | R881 (segment) | restated_xref | RESTATED | cross-reference only; verbatim values at the IDs
Consol PAT Q2: R003, R015 (PR 5,202) | R135 (Annexure 1) | R394 (owners attributable 5202.10) vs R376, R388 (net profit after tax 5915.15, 5949.15 incl NCI) | restated_xref | RESTATED; BASIS_DIFFERENCE (PR PAT = owners attributable) | cross-reference only; verbatim values at the IDs
Consol PAT H1: R017 (PR 9,325) | R138 (Annexure 1) | restated_xref | RESTATED | cross-reference only; verbatim values at the IDs
LTMRHL held for sale: R1928, R1929 (consol note ii) | R1933 (standalone note iii) | R1915, R1916 (PR p7) | R1996 (Annexure A) | restated_xref | RESTATED | cross-reference only; verbatim values at the IDs
Nabha Power divested 25-Jun-2026: R1914 (PR p7) | R1999 (Annexure A symbol f, OCR) | R2347 (legend date) | restated_xref | RESTATED; ENTITY_CHANGE | cross-reference only; verbatim values at the IDs
Lakshya 2031 re-segmentation: R1930, R2134 (consol note II) | R2138 (standalone note II) | restated_xref | RESTATED | cross-reference only; verbatim values at the IDs
Vyoma.AI Limited: R1934 (standalone note iv) | R2031 (Annexure A subsidiary #92, incorporated 22-Apr-2026) | restated_xref | RESTATED; ENTITY_CHANGE | cross-reference only; verbatim values at the IDs
### 11d ENTITY_CHANGE rows: R1999, R2030-R2033, R2039 ; LIQUIDATION rows (symbol a): R1945, R1954, R2034-R2036

## 12. MISSING_FROM_STRUCTURED (A2 sweep found units A1 lacks; loop to A1)
ROW_ID(s) | category | A2 flags | cross-ref / materiality note
MFS-1 | missing_from_structured | MISSING_FROM_STRUCTURED; SIGNATURE_TIMESTAMP | fulltext lines 89-92: Board Outcome letter digital signature of Narayan Subramanian, Date 2026.10.27 17:04:53 +05:30 (no DATE row). 19 minutes after the meeting concluded at 4:45 p.m. (R2151): not a pre-conclusion flag.
MFS-2 | missing_from_structured | MISSING_FROM_STRUCTURED; SIGNATURE_TIMESTAMP | fulltext lines 1959-1963: Annexure III digital signature, glyph-encoded text decodes to Date 2026.10.27 17:01:26 +05'30' (no DATE row; only R2123 and '27th October 2026' captured). After the 16:45 conclusion: no flag.
MFS-3 | missing_from_structured | MISSING_FROM_STRUCTURED; ENTITY | fulltext lines 1427-1428: Annexure A consolidated list, Parent / Holding Company = Larsen & Toubro Limited (no ENTITY row; the standalone list's parent is R2087). Consolidated list A1 rows = 143 (94 subsidiaries, 6 associates, 9 joint ventures, 34 joint operations); with the parent the filed list has 144 entities. Loop to A1.

```yaml
stage: A2-enumerator
company: "LT"
quarter: "q2fy27"
doctype: "results"
model: claude-sonnet-5-5
status: complete
ledger_path: "runs/lt-q2fy27/work/ledger_results_lt_q2fy27.md"
counts:
  notes: 41
  line_items: 400
  zero_standing: 42
  agenda_items: 5
  auditor_paras: 16
  entities: 177
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
  annexure1_items: 58
  other_entity_rows: 63
  forward_rows: 16
  signature_blocks: 6
  press_release_numbers: 95
flags_raised: [ZERO_STANDING, ENTITY_CHANGE, LIQUIDATION, RESTATED, BASIS_DIFFERENCE, MISSING_FROM_STRUCTURED, SIGNATURE_TIMESTAMP, MGMT_FURNISHED_UNREVIEWED, OTHER_AUDITOR_RELIED, UDIN_OCR_GARBLED, HEADING_ONLY, NO_OWN_ROW]
ids_in_structured: 2511
ids_referenced: 2511
orphan_ids: []
missing_from_structured: ["MFS-1 board letter digital signature timestamp 2026.10.27 17:04:53 (fulltext line 92)", "MFS-2 Annexure III digital signature timestamp 2026.10.27 17:01:26 (fulltext lines 1959-1963)", "MFS-3 consolidated Annexure A parent entity Larsen & Toubro Limited (fulltext line 1428)"]
gate_a2: pass
mismatch_note: ""
analyst_note: "Board letter carries one resolution only (results); no dividend, AR, director, auditor or capital item, and 14:00 to 16:45 is a 2h45m sitting. 42 ZERO_STANDING cells: Exceptional items are nil in consol (all periods) and standalone current periods while standalone Q2 FY26 shows an exceptional loss, and CF acquisition, disposal and divestment lines are nil: M&A template lines to read against LTMRHL, Vyoma.AI and Realty transfers. 10 of the 42 are 0.00 bad-debt ratio cells A1 did not flag. Press release PAT 5,202 equals owners-attributable (R394); statement net profit incl NCI is 5,949.15 (R388). Standalone notes (ii) and (iv) have no consolidated twin. LTMRHL is still a listed subsidiary (R1996), held for sale, completion now 31-Dec-2026. 6 ENTITY_CHANGE rows from filed symbols (4 added incl Vyoma.AI; Nabha Power divested); no prior list, so no diff. Auditor: unmodified, no EOM or going concern text; 41 subsidiaries and 23 joint operations are management-furnished. UDIN garbled in A1. 3 MFS rows loop to A1: two signature timestamps and the consolidated parent entity."
```
