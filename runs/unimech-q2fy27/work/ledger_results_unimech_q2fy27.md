# A2 LEDGER: UNIMECH results q2fy27
ids_in_structured: 953 | ids_referenced_in_ledger: 953 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: notes (numbered)   grep_count: 17 (SA 8 + CO 9)   sweep_count: 17   match: yes
category: footnotes/labels   grep_count: 8                  sweep_count: 8    match: yes
category: line_items (distinct page:line, 8 statements)   grep_count: 250   sweep_count: 250   match: yes   (724 NUMBER rows; SA 119, CO 131)
category: zero_standing      grep_count: 49 (flag)           sweep_count: 49 (dash/Nil values)   match: yes
category: agenda_items       grep_count: 3                   sweep_count: 3    match: yes
category: auditor_paras      grep_count: 11 (SA 4 + CO 7)    sweep_count: 11   match: yes
category: entities (rows)    grep_count: 65                  sweep_count: 65   match: yes
category: consolidation_list grep_count: 6 (auditor para 4) / 6 (CO note 2)   sweep_count: 6   match: yes
category: forward            grep_count: 9   sweep_count: 9   match: yes
category: dates              grep_count: 45  sweep_count: 45  match: yes
category: qualifiers         grep_count: 72  sweep_count: 72  match: yes
category: NUMBER total       grep_count: 762 sweep_count: 762 match: yes
gate_a2: pass
=== END COUNT TEST ===

## TIE-OUTS (A1 NUMBER rows only, tolerance 0.02 lakh): 245 computed, 244 pass, 1 flag
Checked: SA and CO balance sheets (sub-totals, total assets = total equity and liabilities, both dates); SA and CO P&L for all 6 columns (total income, total expenses, PBT, tax components, PAT, OCI, TCI, CO attribution splits); Q1+Q2 = six months for every P&L line; SA and CO cash flows both periods (operating subtotal, working capital, CFO, CFI, CFF, net change, closing cash, cash component split); CF PBT and D&A = P&L; CF closing cash = BS; share capital BS = P&L; other equity Mar-26 BS = P&L line. EPS spot check: SA Q2 852.59 / 509.02 lakh shares = 1.68; CO Q2 3,177.74 / 509.02 = 6.24 (match).
No render-transcription arithmetic error found.
FLAG RECON_GAP (filing-level, not transcription): CO cash flow opening cash 4,790.22 (p15 line 688) vs CO balance sheet cash at 31-Mar-26 3,715.40 (p12 line 529): gap 1,074.82. Both values match the fulltext line as transcribed; closing cash 4,553.66 ties to BS. Likely opening cash of entities consolidated w.e.f. April 27, 2026, but the filing does not say so. Route to A3.
Standalone vs consolidated gap (information, no identity): H1 revenue SA 2,154.42 vs CO 23,061.88; H1 PBT SA 1,345.26 vs CO 8,159.53; H1 PAT SA 1,072.74 vs CO 5,963.85; total assets SA 60,611.58 vs CO 1,07,958.31. Goodwill CO 32,199.15 (nil Mar-26) and CO CF Purchase of Partnership interest (42,479.60) explain scale; SA investment in CCDs of subsidiary (14,800.00) is the funding leg. SA H1 other income 1,688.02 is 43.9% of SA total income.
Observation: SA Q1 FY27 revenue 459.06 vs Q2 1,695.36 (volatile standalone quarter). SA six months to Sep-25 PBT 2,060.92 vs Sep-26 1,345.26.

## A. NOTES (numbered; ID carries page/line)
ROW_IDS | note | A2 flags | cross-ref / materiality
R783,R855,R904 | Standalone note 1 |  | p8 line 335
R784,R905 | Standalone note 2 |  | p8 line 336
R785 | Standalone note 3 |  | p8 line 337
R856,R906 | Standalone note 4 |  | p8 line 338
R343-R345,R786,R857,R907 | Standalone note 5 | RESTATED with CO note 6 | p8 line 339
R908 | Standalone note 6 | RESTATED (duplicate of SA note 5; R908 says so) | p8 line 340
R346-R348,R787-R788,R831,R858,R909 | Standalone note 7 | SUBSEQUENT_EVENT | p8 line 341
R789-R790,R832,R859,R910 | Standalone note 8 | SUBSEQUENT_EVENT | p8 line 342
R809,R872,R941 | Consolidated note 1 |  | p16 line 702
R810-R818,R873,R942 | Consolidated note 2 | ENTITY_CHANGE (entities 3,4,5 w.e.f April 27, 2026) | p16 line 705
R819,R943-R944 | Consolidated note 3 |  | p16 line 712
R820 | Consolidated note 4 |  | p16 line 713
R874,R945 | Consolidated note 5 |  | p16 line 714
R755-R757,R875,R946 | Consolidated note 6 | RESTATED with SA note 5 | p16 line 715
R758,R821,R876,R947 | Consolidated note 7 | CO-ONLY (ESOP; no SA counterpart note) | p16 line 716
R759-R761,R822-R823,R833,R877,R948 | Consolidated note 8 | SUBSEQUENT_EVENT | p16 line 717
R834,R878,R949 | Consolidated note 9 | SUBSEQUENT_EVENT | p16 line 718

### A2. Unnumbered notes / footnotes / markers
ROW_IDS | item | A2 flags | note
R894 | p5 line 249 footnote/label defect |  | 
R898 | p6 line 261 footnote/label defect | SOURCE_LABEL_DEFECT | 
R899 | p6 line 286 footnote/label defect | SOURCE_TYPO | 
R916 | p10 line 434 footnote/label defect |  | 
R931 | p13 line 605 footnote/label defect | SOURCE_NUMBERING_DEFECT | 
R932 | p13 line 612 footnote/label defect |  | 
R936 | p14 line 651 footnote/label defect | SOURCE_TYPO | 
R942 | p16 line 711 footnote/label defect |  | 
R891,R895,R900,R903,R927,R933,R937,R940 | "Initialed For Identification Purposes Only" stamps (8), one per statement page | | pages 4,5,6,7,12,13,14,15
R915,R920,R924 | review report page markers (3) | | consolidated report pages 1-3 of 3

## B. AGENDA ITEMS (Board outcome letter, pages 1-2)
ROW_IDS | agenda item | A2 flags | note
R766,R840,R882 | Item 1 (results) |  | 3 structured rows
R002-R003,R767-R768,R828-R830,R841,R883 | Item 2 (Hobel acquisition) | ENTITY_CHANGE (internal restructuring) | 9 structured rows
R004,R769,R842-R844,R884 | Item 3 (Naidu promotion/transfer) |  | 6 structured rows
R001,R005,R763-R765,R770-R771,R837-R839,R845 | Meeting times / signature / admin |  | 11 structured rows
Board meeting: 01:00 P.M. to 08:00 P.M. (R005) = 7 hours, long for a results meeting; three agenda items, no AR/AGM/record date/dividend/director/auditor/ESOP/fund-raise items found (NOT FOUND in filing).
Digital signature 2026.10.27 21:07:55 (R845) is after meeting end 20:00: no timing flag.

## C. AUDITOR REPORT PARAGRAPHS (Limited Review: unmodified, no EoM, no going concern language)
ROW_IDS | paragraph | A2 flags | note
R006-R008,R774,R847 | SA signature block (firm, partner, UDIN, date) |  | 
R350-R353,R863,R918-R920 | CO para 6 associate (other auditor); not-modified | OTHER_AUDITOR_RELIANCE | 
R354-R361,R801,R921-R923 | CO para 7 unreviewed subsidiary (mgmt furnished); not-modified | MGMT_FURNISHED_UNAUDITED; ZERO_STANDING (all Nil) | 
R362-R364,R802,R864,R924 | CO signature block |  | 
R772-R773 | SA heading/addressee |  | 
R792 | CO heading/addressee |  | 
R793,R861,R911 | CO para 1 scope |  | 
R794-R799,R862,R916 | CO para 4 entity list | ENTITY_CHANGE | 
R800,R917 | CO para 5 reliance on other auditor | OTHER_AUDITOR_RELIANCE | 
R846 | SA para 1 scope |  | 
R885 | SA para 2 mgmt responsibility |  | 
R886-R887 | SA para 3 review standard/scope |  | 
R888 | SA para 4 conclusion (unmodified) |  | 
R912-R915 | CO para 3 review standard/SEBI 33(8) procedures |  | 
Opinion type: limited review, unmodified conclusion both reports. No EoM. No Going Concern. UDINs: SA 26233552TMTJJF5424 (R008); CO 26233552TKLANT9133 (R364).
SA report: partner name not captured in structured rows (membership 233552, R007). Unnamed other auditor (R800) and unnamed unreviewed subsidiary (R801).

## D. SIGNATURE BLOCKS
ROW_IDS | block | A2 flags | note
R771,R845 | Board letter e-signature, Rashmi Gupta CS | | 
R006,R007,R008,R847 | SA review report signature (MSKA, UDIN) | | 
R791,R349,R860 | SA results signature, CMD Anil Puttan Kumar | | 
R802,R362,R363,R364,R864 | CO review report signature (Pankaj S Bhauwala) | | 
R824,R762,R879 | CO results signature, CMD | | 

## E. ENTITIES (all 65 ENTITY rows; consolidation list flagged)
ROW_IDS | group | A2 flags | note
R794,R795,R796,R797,R798,R799 | Consolidation list per auditor para 4 (6 entities) | ENTITY_CHANGE on R796,R797,R798 (consolidated w.e.f April 27, 2026) | no prior ledger to diff; change evidenced inside filing
R811,R812,R813,R815,R816,R818 | Consolidation list per CO note 2 (6 entities) | ENTITY_CHANGE on R813,R815,R816 | matches auditor list: 6 = 6
R787,R822 | Kanoo Unimech Saudi (51% ODI, Oct 1, 2026, INR 3,935.72 lakhs) | ENTITY_CHANGE (new, post-quarter, not in consolidation list) | R346-R348,R759-R761 numbers; R831,R833 FORWARD
R801 | Unreviewed subsidiary (unnamed) | MGMT_FURNISHED; ZERO_STANDING figures R354-R361 | which of 5 subsidiaries is unnamed
R767,R768,R789,R790,R810,R814,R827 | Hobel acquisition parties | ENTITY_CHANGE (intra-group transfer pending) | 
R786,R799,R817,R818 | Dheya (associate) | 27.24% after dilution; loss share R350-R353 | 
R763-R766,R769-R774,R783-R785,R788,R791-R793,R800,R802,R809,R819-R821,R823-R826 | Auditor / signatories / regulators / venues |  | 
R775-R782,R803-R808 | Company identity, address, statement-line labels (cash flow items, BS lines, goodwill, NCI) | | 14 rows

## F. LINE ITEMS IN EVERY FINANCIAL TABLE (one row per page+line; IDs = period columns)
Format: page:line | statement | ID span | n_periods | ZERO_STANDING periods
p4:l160 | SA BS | R009-R010 | 2 | -
p4:l161 | SA BS | R011-R012 | 2 | -
p4:l162 | SA BS | R013-R014 | 2 | -
p4:l163 | SA BS | R015-R016 | 2 | -
p4:l164 | SA BS | R017-R018 | 2 | -
p4:l166 | SA BS | R019-R020 | 2 | -
p4:l167 | SA BS | R021-R022 | 2 | -
p4:l168 | SA BS | R023-R024 | 2 | -
p4:l169 | SA BS | R025-R026 | 2 | -
p4:l170 | SA BS | R027-R028 | 2 | -
p4:l171 | SA BS | R029-R030 | 2 | -
p4:l173 | SA BS | R031-R032 | 2 | -
p4:l175 | SA BS | R033-R034 | 2 | -
p4:l176 | SA BS | R035-R036 | 2 | -
p4:l177 | SA BS | R037-R038 | 2 | -
p4:l178 | SA BS | R039-R040 | 2 | -
p4:l179 | SA BS | R041-R042 | 2 | -
p4:l180 | SA BS | R043-R044 | 2 | -
p4:l181 | SA BS | R045-R046 | 2 | -
p4:l182 | SA BS | R047-R048 | 2 | -
p4:l183 | SA BS | R049-R050 | 2 | -
p4:l184 | SA BS | R051-R052 | 2 | -
p4:l187 | SA BS | R053-R054 | 2 | -
p4:l188 | SA BS | R055-R056 | 2 | -
p4:l189 | SA BS | R057-R058 | 2 | -
p4:l193 | SA BS | R059-R060 | 2 | R060
p4:l194 | SA BS | R061-R062 | 2 | -
p4:l195 | SA BS | R063-R064 | 2 | -
p4:l196 | SA BS | R065-R066 | 2 | -
p4:l199 | SA BS | R067-R068 | 2 | R068
p4:l200 | SA BS | R069-R070 | 2 | -
p4:l202 | SA BS | R071-R072 | 2 | -
p4:l203 | SA BS | R073-R074 | 2 | -
p4:l204 | SA BS | R075-R076 | 2 | -
p4:l205 | SA BS | R077-R078 | 2 | -
p4:l206 | SA BS | R079-R080 | 2 | -
p4:l207 | SA BS | R081-R082 | 2 | R082
p4:l208 | SA BS | R083-R084 | 2 | -
p4:l209 | SA BS | R085-R086 | 2 | -
p4:l210 | SA BS | R087-R088 | 2 | -
p5:l221 | SA P&L | R089-R094 | 6 | -
p5:l222 | SA P&L | R095-R100 | 6 | -
p5:l223 | SA P&L | R101-R106 | 6 | -
p5:l225 | SA P&L | R107-R112 | 6 | -
p5:l226 | SA P&L | R113-R118 | 6 | -
p5:l227 | SA P&L | R119-R124 | 6 | -
p5:l228 | SA P&L | R125-R130 | 6 | -
p5:l229 | SA P&L | R131-R136 | 6 | -
p5:l230 | SA P&L | R137-R142 | 6 | -
p5:l231 | SA P&L | R143-R148 | 6 | -
p5:l232 | SA P&L | R149-R154 | 6 | -
p5:l233 | SA P&L | R155-R160 | 6 | -
p5:l236 | SA P&L | R161-R166 | 6 | -
p5:l237 | SA P&L | R167-R172 | 6 | R168
p5:l238 | SA P&L | R173-R178 | 6 | -
p5:l239 | SA P&L | R179-R184 | 6 | -
p5:l240 | SA P&L | R185-R190 | 6 | -
p5:l243 | SA P&L | R191-R196 | 6 | -
p5:l244 | SA P&L | R197-R202 | 6 | R200
p5:l245 | SA P&L | R203-R208 | 6 | -
p5:l246 | SA P&L | R209-R214 | 6 | -
p5:l247 | SA P&L | R215-R221 | 7 | -
p5:l248 | SA P&L | R222 | 1 | -
p5:l250 | SA P&L | R223-R228 | 6 | -
p5:l251 | SA P&L | R229-R234 | 6 | -
p6:l262 | SA CF-1 | R235-R236 | 2 | -
p6:l264 | SA CF-1 | R237-R238 | 2 | -
p6:l265 | SA CF-1 | R239-R240 | 2 | -
p6:l266 | SA CF-1 | R241-R242 | 2 | -
p6:l267 | SA CF-1 | R243-R244 | 2 | -
p6:l268 | SA CF-1 | R245-R246 | 2 | -
p6:l269 | SA CF-1 | R247-R248 | 2 | R247
p6:l270 | SA CF-1 | R249-R250 | 2 | -
p6:l271 | SA CF-1 | R251-R252 | 2 | R251
p6:l272 | SA CF-1 | R253-R254 | 2 | R254
p6:l273 | SA CF-1 | R255-R256 | 2 | -
p6:l274 | SA CF-1 | R257-R258 | 2 | -
p6:l276 | SA CF-1 | R259-R260 | 2 | -
p6:l277 | SA CF-1 | R261-R262 | 2 | -
p6:l278 | SA CF-1 | R263-R264 | 2 | -
p6:l279 | SA CF-1 | R265-R266 | 2 | -
p6:l280 | SA CF-1 | R267-R268 | 2 | -
p6:l281 | SA CF-1 | R269-R270 | 2 | -
p6:l282 | SA CF-1 | R271-R272 | 2 | -
p6:l283 | SA CF-1 | R273-R274 | 2 | -
p6:l284 | SA CF-1 | R275-R276 | 2 | -
p6:l285 | SA CF-1 | R277-R278 | 2 | -
p6:l286 | SA CF-1 | R279-R280 | 2 | -
p6:l287 | SA CF-1 | R281-R282 | 2 | -
p6:l288 | SA CF-1 | R283-R284 | 2 | -
p6:l289 | SA CF-1 | R285-R286 | 2 | -
p6:l291 | SA CF-1 | R287-R288 | 2 | -
p6:l292 | SA CF-1 | R289-R290 | 2 | -
p6:l293 | SA CF-1 | R291-R292 | 2 | -
p6:l294 | SA CF-1 | R293-R294 | 2 | R294
p6:l295 | SA CF-1 | R295-R296 | 2 | R296
p6:l296 | SA CF-1 | R297-R298 | 2 | -
p6:l297 | SA CF-1 | R299-R300 | 2 | -
p6:l298 | SA CF-1 | R301-R302 | 2 | R302
p6:l299 | SA CF-1 | R303-R304 | 2 | -
p6:l300 | SA CF-1 | R305-R306 | 2 | -
p6:l301 | SA CF-1 | R307-R308 | 2 | -
p6:l302 | SA CF-1 | R309-R310 | 2 | -
p7:l313 | SA CF-2 | R311-R312 | 2 | R312
p7:l314 | SA CF-2 | R313-R314 | 2 | R314
p7:l315 | SA CF-2 | R315-R316 | 2 | R316
p7:l316 | SA CF-2 | R317-R318 | 2 | R318
p7:l317 | SA CF-2 | R319-R320 | 2 | R320
p7:l318 | SA CF-2 | R321-R322 | 2 | -
p7:l319 | SA CF-2 | R323-R324 | 2 | -
p7:l320 | SA CF-2 | R325-R326 | 2 | -
p7:l321 | SA CF-2 | R327-R328 | 2 | -
p7:l322 | SA CF-2 | R329-R330 | 2 | -
p7:l323 | SA CF-2 | R331-R332 | 2 | -
p7:l324 | SA CF-2 | R333-R334 | 2 | -
p7:l327 | SA CF-2 | R335-R336 | 2 | -
p7:l328 | SA CF-2 | R337-R338 | 2 | -
p7:l329 | SA CF-2 | R339-R340 | 2 | -
p7:l330 | SA CF-2 | R341-R342 | 2 | -
p12:l512 | CO BS | R365-R366 | 2 | -
p12:l513 | CO BS | R367-R368 | 2 | -
p12:l514 | CO BS | R369-R370 | 2 | -
p12:l515 | CO BS | R371-R372 | 2 | R372
p12:l516 | CO BS | R373-R374 | 2 | -
p12:l517 | CO BS | R375-R376 | 2 | -
p12:l519 | CO BS | R377-R378 | 2 | -
p12:l520 | CO BS | R379-R380 | 2 | -
p12:l521 | CO BS | R381-R382 | 2 | -
p12:l522 | CO BS | R383-R384 | 2 | -
p12:l523 | CO BS | R385-R386 | 2 | -
p12:l525 | CO BS | R387-R388 | 2 | -
p12:l527 | CO BS | R389-R390 | 2 | -
p12:l528 | CO BS | R391-R392 | 2 | -
p12:l529 | CO BS | R393-R394 | 2 | -
p12:l530 | CO BS | R395-R396 | 2 | -
p12:l531 | CO BS | R397-R398 | 2 | -
p12:l532 | CO BS | R399-R400 | 2 | -
p12:l533 | CO BS | R401-R402 | 2 | -
p12:l534 | CO BS | R403-R404 | 2 | -
p12:l535 | CO BS | R405-R406 | 2 | -
p12:l538 | CO BS | R407-R408 | 2 | -
p12:l539 | CO BS | R409-R410 | 2 | -
p12:l540 | CO BS | R411-R412 | 2 | R412
p12:l541 | CO BS | R413-R414 | 2 | -
p12:l545 | CO BS | R415-R416 | 2 | -
p12:l546 | CO BS | R417-R418 | 2 | -
p12:l547 | CO BS | R419-R420 | 2 | -
p12:l548 | CO BS | R421-R422 | 2 | -
p12:l551 | CO BS | R423-R424 | 2 | -
p12:l552 | CO BS | R425-R426 | 2 | -
p12:l554 | CO BS | R427-R428 | 2 | -
p12:l555 | CO BS | R429-R430 | 2 | -
p12:l556 | CO BS | R431-R432 | 2 | -
p12:l557 | CO BS | R433-R434 | 2 | -
p12:l558 | CO BS | R435-R436 | 2 | -
p12:l559 | CO BS | R437-R438 | 2 | -
p12:l560 | CO BS | R439-R440 | 2 | -
p12:l561 | CO BS | R441-R442 | 2 | -
p12:l562 | CO BS | R443-R444 | 2 | -
p13:l573 | CO P&L | R445-R450 | 6 | -
p13:l574 | CO P&L | R451-R456 | 6 | -
p13:l575 | CO P&L | R457-R462 | 6 | -
p13:l577 | CO P&L | R463-R468 | 6 | -
p13:l578 | CO P&L | R469-R474 | 6 | -
p13:l579 | CO P&L | R475-R480 | 6 | -
p13:l580 | CO P&L | R481-R486 | 6 | -
p13:l581 | CO P&L | R487-R492 | 6 | -
p13:l582 | CO P&L | R493-R498 | 6 | -
p13:l583 | CO P&L | R499-R504 | 6 | -
p13:l584 | CO P&L | R505-R510 | 6 | -
p13:l585 | CO P&L | R511-R516 | 6 | -
p13:l588 | CO P&L | R517-R522 | 6 | -
p13:l589 | CO P&L | R523-R528 | 6 | R524
p13:l590 | CO P&L | R529-R534 | 6 | -
p13:l591 | CO P&L | R535-R540 | 6 | -
p13:l592 | CO P&L | R541-R546 | 6 | -
p13:l593 | CO P&L | R547-R552 | 6 | -
p13:l594 | CO P&L | R553-R558 | 6 | -
p13:l597 | CO P&L | R559-R564 | 6 | -
p13:l598 | CO P&L | R565-R570 | 6 | R568
p13:l599 | CO P&L | R571-R576 | 6 | R572-R573,R575
p13:l600 | CO P&L | R577-R582 | 6 | -
p13:l601 | CO P&L | R583-R588 | 6 | -
p13:l603 | CO P&L | R589-R594 | 6 | -
p13:l604 | CO P&L | R595-R600 | 6 | R597,R599-R600
p13:l606 | CO P&L | R601-R606 | 6 | -
p13:l608 | CO P&L | R607-R612 | 6 | -
p13:l609 | CO P&L | R613-R618 | 6 | R615,R617-R618
p13:l610 | CO P&L | R619-R625 | 7 | -
p13:l611 | CO P&L | R626 | 1 | -
p13:l613 | CO P&L | R627-R632 | 6 | -
p13:l614 | CO P&L | R633-R638 | 6 | -
p14:l625 | CO CF-1 | R639-R640 | 2 | -
p14:l627 | CO CF-1 | R641-R642 | 2 | -
p14:l628 | CO CF-1 | R643-R644 | 2 | -
p14:l629 | CO CF-1 | R645-R646 | 2 | -
p14:l630 | CO CF-1 | R647-R648 | 2 | R648
p14:l631 | CO CF-1 | R649-R650 | 2 | -
p14:l632 | CO CF-1 | R651-R652 | 2 | -
p14:l633 | CO CF-1 | R653-R654 | 2 | R653
p14:l634 | CO CF-1 | R655-R656 | 2 | -
p14:l635 | CO CF-1 | R657-R658 | 2 | -
p14:l636 | CO CF-1 | R659-R660 | 2 | -
p14:l637 | CO CF-1 | R661-R662 | 2 | R662
p14:l638 | CO CF-1 | R663-R664 | 2 | -
p14:l639 | CO CF-1 | R665-R666 | 2 | -
p14:l641 | CO CF-1 | R667-R668 | 2 | -
p14:l642 | CO CF-1 | R669-R670 | 2 | -
p14:l643 | CO CF-1 | R671-R672 | 2 | -
p14:l644 | CO CF-1 | R673-R674 | 2 | -
p14:l645 | CO CF-1 | R675-R676 | 2 | -
p14:l646 | CO CF-1 | R677-R678 | 2 | -
p14:l647 | CO CF-1 | R679-R680 | 2 | -
p14:l648 | CO CF-1 | R681-R682 | 2 | -
p14:l649 | CO CF-1 | R683-R684 | 2 | -
p14:l650 | CO CF-1 | R685-R686 | 2 | -
p14:l651 | CO CF-1 | R687-R688 | 2 | -
p14:l652 | CO CF-1 | R689-R690 | 2 | -
p14:l653 | CO CF-1 | R691-R692 | 2 | -
p14:l654 | CO CF-1 | R693-R694 | 2 | -
p14:l656 | CO CF-1 | R695-R696 | 2 | -
p14:l657 | CO CF-1 | R697-R698 | 2 | -
p14:l658 | CO CF-1 | R699-R700 | 2 | -
p14:l659 | CO CF-1 | R701-R702 | 2 | R702
p14:l660 | CO CF-1 | R703-R704 | 2 | R704
p14:l661 | CO CF-1 | R705-R706 | 2 | R706
p14:l662 | CO CF-1 | R707-R708 | 2 | R708
p14:l663 | CO CF-1 | R709-R710 | 2 | -
p14:l664 | CO CF-1 | R711-R712 | 2 | -
p14:l665 | CO CF-1 | R713-R714 | 2 | -
p14:l666 | CO CF-1 | R715-R716 | 2 | -
p15:l677 | CO CF-2 | R717-R718 | 2 | R718
p15:l678 | CO CF-2 | R719-R720 | 2 | R720
p15:l679 | CO CF-2 | R721-R722 | 2 | R722
p15:l680 | CO CF-2 | R723-R724 | 2 | -
p15:l681 | CO CF-2 | R725-R726 | 2 | -
p15:l682 | CO CF-2 | R727-R728 | 2 | R728
p15:l683 | CO CF-2 | R729-R730 | 2 | -
p15:l684 | CO CF-2 | R731-R732 | 2 | -
p15:l685 | CO CF-2 | R733-R734 | 2 | -
p15:l686 | CO CF-2 | R735-R736 | 2 | -
p15:l687 | CO CF-2 | R737-R738 | 2 | -
p15:l688 | CO CF-2 | R739-R740 | 2 | -
p15:l689 | CO CF-2 | R741-R742 | 2 | -
p15:l690 | CO CF-2 | R743-R744 | 2 | -
p15:l693 | CO CF-2 | R745-R746 | 2 | -
p15:l694 | CO CF-2 | R747-R748 | 2 | -
p15:l695 | CO CF-2 | R749-R750 | 2 | -
p15:l696 | CO CF-2 | R751-R752 | 2 | R752
p15:l697 | CO CF-2 | R753-R754 | 2 | -

## G. ZERO_STANDING INVENTORY (every dash/Nil row)
ROW_IDS | A2 flag | note
R060,R068,R082,R168,R200,R247,R251,R254,R294,R296,R302,R312,R314,R316,R318,R320,R354-R361,R372,R412,R524,R568,R572-R573,R575,R597,R599-R600,R615,R617-R618,R648,R653,R662,R702,R704,R706,R708,R718,R720,R722,R728,R752 | ZERO_STANDING | 49 rows: flagged by A1 49; dash/Nil valued 49
Template-signal items worth reading: CO BS Non-controlling interest 1.11 (nil Mar-26), Loss on derivative options Sep-26 nil vs Sep-25 53.12 (both SA and CO), CCD investment in subsidiary SA CF (-14,800) with nil comparative, Partnership interest purchase CO CF (-42,479.60) nil comparative, Goodwill Mar-26 nil vs 32,199.15, working capital borrowings CO CF 3,885.26 nil comparative, Current tax liabilities Mar-26 nil SA.

## H. FORWARD-LOOKING STATEMENTS
ROW_IDS | page:line | note
R828 | p1:l49 | post-acquisition ownership
R829 | p1:l50 | stated purpose of Hobel acquisition
R830 | p1:l55 | future disclosure
R831 | p8:l341 | standalone note 7 new overseas subsidiary
R832 | p8:l342 | standalone note 8 post-completion ownership
R833 | p16:l717 | consolidated note 8 new overseas subsidiary
R834 | p16:l718 | consolidated note 9 post-completion ownership
R835 | p17:l738 | reason for promotion
R836 | p17:l749 | role expansion

## I. DATES
ROW_IDS | page:line | note
R837 | p1:l19 | date of intimation letter
R838 | p1:l32 | earlier intimation date
R839 | p1:l35 | board meeting date
R840 | p1:l40 | result period
R841 | p1:l54 | SEBI Master Circular date, item 2
R842 | p1:l62 | promotion effective date
R843 | p1:l65 | cessation as Senior Management effective
R844 | p1:l68 | SEBI Master Circular date, item 3
R845 | p2:l83 | digital signature timestamp
R846 | p3:l108 | standalone review period
R847 | p3:l144 | standalone review report date
R848 | p4:l157 | balance sheet date, current
R849 | p4:l157 | balance sheet date, comparative
R850 | p5:l219 | result column periods, quarter
R851 | p5:l219 | result column periods, six months
R852 | p5:l219 | result column period, full year
R853 | p6:l260 | cash flow comparison periods
R854 | p7:l311 | cash flow comparison periods
R855 | p8:l335 | standalone note 1 Board meeting date
R856 | p8:l338 | standalone balancing figure periods
R857 | p8:l339 | Dheya acquisition period, standalone note 5
R858 | p8:l341 | ODI date, standalone note 7
R859 | p8:l342 | Board approval of Hobel acquisition, standalone note 8
R860 | p8:l349 | standalone signing date
R861 | p9:l368 | consolidated review period
R862 | p10:l434 | entities 3, 4, 5 consolidated from
R863 | p10:l446 | associate loss periods
R864 | p11:l494 | consolidated review report date
R865 | p12:l509 | balance sheet date, current
R866 | p12:l509 | balance sheet date, comparative
R867 | p13:l571 | result column periods, quarter
R868 | p13:l571 | result column periods, six months
R869 | p13:l571 | result column period, full year
R870 | p14:l623 | cash flow comparison periods
R871 | p15:l675 | cash flow comparison periods
R872 | p16:l702 | consolidated note 1 Board meeting date
R873 | p16:l711 | entities 3, 4, 5 consolidated from
R874 | p16:l714 | consolidated balancing figure periods
R875 | p16:l715 | Dheya acquisition period, consolidated note 6
R876 | p16:l716 | ESOP allotment period, consolidated note 7
R877 | p16:l717 | ODI date, consolidated note 8
R878 | p16:l718 | Board approval of Hobel acquisition, consolidated note 9
R879 | p16:l725 | consolidated signing date
R880 | p17:l757 | ceased to be Senior Management effective
R881 | p17:l759 | date of appointment/cessation

## J. QUALIFIERS / FINE PRINT
ROW_IDS | page:line | note
R882 | p1:l39 | results are unaudited, limited review
R883 | p1:l45 | Hobel acquisition is intra-group
R884 | p1:l64 | promotion and transfer same date
R885 | p3:l115 | standalone basis of preparation
R886 | p3:l120 | standalone review standard
R887 | p3:l124 | standalone limited review scope
R888 | p3:l129 | standalone review conclusion
R889 | p4:l156 | standalone statement unit convention, p4
R890 | p4:l157 | Sep-26 column unaudited; Mar-26 column audited
R891 | p4:l211 | stamp on standalone statement page
R892 | p5:l218 | standalone statement unit convention, p5
R893 | p5:l219 | audit status of result columns
R894 | p5:l249 | standalone EPS basis
R895 | p5:l252 | stamp on standalone statement page
R896 | p6:l259 | standalone statement unit convention, p6
R897 | p6:l260 | cash flow columns unaudited
R898 | p6:l261 | standalone CF header wording
R899 | p6:l286 | line label spelt 'workings' in source
R900 | p6:l303 | stamp on standalone statement page
R901 | p7:l310 | standalone statement unit convention, p7
R902 | p7:l311 | cash flow columns unaudited
R903 | p7:l331 | stamp on standalone statement page
R904 | p8:l335 | standalone note 1 basis of preparation
R905 | p8:l336 | standalone segment note
R906 | p8:l338 | standalone quarter derivation note
R907 | p8:l339 | standalone note 5 dilution and shareholding
R908 | p8:l340 | standalone note 6 duplicate of note 5
R909 | p8:l341 | standalone note 7 subsequent event
R910 | p8:l342 | standalone note 8 subsequent event
R911 | p9:l367 | scope includes associate share
R912 | p9:l382 | consolidated review standard
R913 | p9:l386 | consolidated limited review scope
R914 | p9:l392 | additional procedures
R915 | p9:l394 | review report page marker
R916 | p10:l434 | marker on entities 3, 4, 5 (consolidated from)
R917 | p10:l437 | para 5 reliance
R918 | p10:l447 | associate not reviewed by principal auditor
R919 | p10:l453 | unmodified conclusion, other auditor matter
R920 | p10:l456 | review report page marker
R921 | p11:l469 | para 7 management-prepared subsidiary results
R922 | p11:l478 | materiality statement by management
R923 | p11:l480 | unmodified conclusion, subsidiary matter
R924 | p11:l496 | review report page marker
R925 | p12:l508 | consolidated statement unit convention, p12
R926 | p12:l509 | Sep-26 column unaudited; Mar-26 column audited
R927 | p12:l563 | stamp on consolidated statement page
R928 | p13:l570 | consolidated statement unit convention, p13
R929 | p13:l571 | audit status of result columns
R930 | p13:l592 | consolidated PAT defined before associate loss
R931 | p13:l605 | consolidated result item numbering
R932 | p13:l612 | consolidated EPS basis
R933 | p13:l615 | stamp on consolidated statement page
R934 | p14:l622 | consolidated statement unit convention, p14
R935 | p14:l623 | cash flow columns unaudited
R936 | p14:l651 | line label spelt 'workings' in source
R937 | p14:l667 | stamp on consolidated statement page
R938 | p15:l674 | consolidated statement unit convention, p15
R939 | p15:l675 | cash flow columns unaudited
R940 | p15:l698 | stamp on consolidated statement page
R941 | p16:l702 | consolidated note 1 basis of preparation
R942 | p16:l711 | marker on entities 3, 4, 5 (consolidated from)
R943 | p16:l712 | consolidated segment note
R944 | p16:l712 | consolidated segment description wider than standalone
R945 | p16:l714 | consolidated quarter derivation note
R946 | p16:l715 | consolidated note 6 shareholding
R947 | p16:l716 | consolidated note 7
R948 | p16:l717 | consolidated note 8 subsequent event
R949 | p16:l718 | consolidated note 9 subsequent event
R950 | p17:l729 | Annexure II basis
R951 | p17:l753 | Annexure II reason
R952 | p17:l769 | Annexure II item 4
R953 | p17:l773 | Annexure II item 5

## K. NON-STATEMENT NUMBERS (identifiers, note figures, associate/unreviewed-subsidiary figures)
ROW_IDS | page:line | A2 flags | note

## L. ANNEXURES
Annexure I = results (pages 3-16: review reports, SA statements p4-8, CO statements p9-16). Annexure II = Regulation 30 disclosure p17 (Senior Management change, Mr. Prathap B. Naidu): 5 items, rows below.
R825-R827,R835-R836,R880-R881,R950-R953 | Annexure II rows (11) | FORWARD R835,R836; ENTITY_CHANGE (transfer to Innomech subsidiary)
No director profiles (no director appointments). Annexure II item 4 profile: Not Applicable (R952).
```yaml
stage: A2-enumerator
company: "UNIMECH"
quarter: "q2fy27"
doctype: "results"
model: claude-sonnet-5-5
status: complete
ledger_path: "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/qr-unimech-q2fy27-1b1895/runs/unimech-q2fy27/work/ledger_results_unimech_q2fy27.md"
counts:
  notes: 17
  line_items: 250
  zero_standing: 49
  agenda_items: 3
  auditor_paras: 11
  entities: 65
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, ENTITY_CHANGE, RESTATED, RECON_GAP, MGMT_FURNISHED_UNAUDITED, OTHER_AUDITOR_RELIANCE, SUBSEQUENT_EVENT, SOURCE_TYPO, SOURCE_NUMBERING_DEFECT, SOURCE_LABEL_DEFECT]
ids_in_structured: 953
ids_referenced: 953
orphan_ids: []
missing_from_structured: []
gate_a2: pass
mismatch_note: ""
analyst_note: "Tie-outs: 244 of 245 pass (balance sheets, P&L all six columns, Q1+Q2=H1, cash flows, CF to BS). One filing-level gap, not a render error: consolidated CF opening cash 4,790.22 vs Mar-26 BS cash 3,715.40 (diff 1,074.82); both match fulltext. Likely cash of entities consolidated w.e.f. April 27, 2026; filing silent. Consolidation list 6 entities, entities 3-5 (Uniflux, Hobel Bellows Pvt, Hobel Bellows Co) new from April 27, 2026 (ENTITY_CHANGE; no prior ledger). One unnamed subsidiary is management-furnished with all-Nil figures (R354-R361). Kanoo Unimech Saudi (51% ODI Oct 1, 2026) post-quarter, not yet in the list. SA notes 5 and 6 duplicate. Meeting ran 1pm to 8pm."
```
