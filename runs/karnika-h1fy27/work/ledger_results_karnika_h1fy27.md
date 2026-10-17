# A2 LEDGER: results | KARNIKA | h1fy27
source: A1 structured extraction only (extracted/karnika-results-h1fy27-structured.md). Values live at the ID there; not re-copied.

ids_in_structured: 780 | ids_referenced_in_ledger: 780 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: notes_numbered      grep_count: 18   sweep_count: 18   match: yes   (fulltext grep numbered notes p6-7 and p12-13, excluding auditor paragraphs)
category: notes_unnumbered    grep_count: 2    sweep_count: 2   match: yes   (comparatives notes p7, p13, manual sweep)
category: line_items          grep_count: 210   sweep_count: 210   match: yes   (per table {'standalone balance sheet': 29, 'standalone results': 26, 'standalone cash flow': 44, 'consolidated balance sheet': 32, 'consolidated results': 35, 'consolidated cash flow': 44})
category: zero_standing       grep_count: 45   sweep_count: 45   match: yes   (A1 flag count vs value sweep of dash, 0.00, 'no ...' among NUMBER rows)
category: agenda_items        grep_count: 1   sweep_count: 1   match: yes
category: auditor_paras       grep_count: 8   sweep_count: 8   match: yes   (4 standalone + 4 consolidated, fulltext lines 90-111, 369-390)
category: entities            grep_count: 4   sweep_count: 4   match: yes   (parent, Kidcity, Elementa Lifespaces, RDB Elementa pending; all 66 ENTITY rows referenced)
category: structured_ids      grep_count: 780   sweep_count: 780   match: yes
gate_a2: pass
=== END COUNT TEST ===

## 1. NOTES LEDGER (numbered and unnumbered)
note | location | structured ROW IDs | A2 flags | cross-ref / materiality
note hdr | p6 (line 289) | R756 |  | notes heading
note 1 | p6 (line 291) | R662-R664,R709-R710 |  | board approval 10 Oct 2026, Audit Committee
note 2 | p6 (line 297) | R665 |  | Ind AS basis
note 3 | p6 (line 302) | R666,R689,R757-R758 |  | FORWARD software under development by subsidiary (no revenue/expense); single textile segment
note 4 | p6 (line 308) | R579-R587,R690,R711-R713,R759-R760 |  | warrant preferential issue; utilisation table as at 30.06.2026 (not 30.09.2026), unutilised balance value not printed; FORWARD conversion window
note 5 | p6 (line 317) | R588,R761 | ZERO_STANDING | investor complaints nil
note 6 | p6 (line 318) | R589,R667,R714-R715,R762-R764 |  | Kidcity 75%, acquired 4 Oct 2025; consolidated from acquisition; no prior-year consolidated comparatives
note U | p7 (line 334) | R716,R765 |  | unnumbered note: comparative consolidated info for Sep-25 not presented
note 11 | p7 (line 337) | R590-R593,R668,R691,R717,R766 | PENDING_ITEM | FORWARD pending subscription 26% RDB Elementa, Rs 5,20,000 not allotted, disclosed as capital commitment
note 12 | p7 (line 344) | R594-R597,R669-R670,R718,R767 | ENTITY_CHANGE | Elementa Lifespaces 40% associate from 24.07.2026, equity method
note 13 | p7 (line 350) | R671,R719 |  | NSE availability
note hdr | p12 (line 583) | R768 |  | notes heading
note 1 | p12 (line 585) | R672-R674,R720-R721 |  | board approval 10 Oct 2026, Audit Committee
note 2 | p12 (line 591) | R675 |  | Ind AS basis
note 3 | p12 (line 596) | R676,R692,R769-R770 |  | FORWARD software under development by subsidiary (no revenue/expense); single textile segment
note 4 | p12 (line 602) | R598-R606,R693,R722-R724,R771-R772 |  | warrant preferential issue; utilisation table as at 30.06.2026 (not 30.09.2026), unutilised balance value not printed; FORWARD conversion window
note 5 | p12 (line 612) | R607,R773 | ZERO_STANDING | investor complaints nil
note 6 | p12 (line 613) | R608,R677,R725-R726,R774-R776 |  | Kidcity 75%, acquired 4 Oct 2025; consolidated from acquisition; no prior-year consolidated comparatives
note U | p13 (line 632) | R727,R777 |  | unnumbered note: comparative consolidated info for Sep-25 not presented
note 11 | p13 (line 635) | R609-R612,R678,R694,R728,R778 | PENDING_ITEM | FORWARD pending subscription 26% RDB Elementa, Rs 5,20,000 not allotted, disclosed as capital commitment
note 12 | p13 (line 642) | R613-R616,R679-R680,R729,R779 | ENTITY_CHANGE | Elementa Lifespaces 40% associate from 24.07.2026, equity method
note 13 | p13 (line 648) | R681,R730 |  | NSE availability
NOTE NUMBERING GAP: notes run 1-6 then 11-13 on both pages. Notes 7, 8, 9, 10 do not appear in the filing (FLAG NOTE_NUMBER_GAP). The same notes block appears twice (p6-7 and p12-13): RESTATED, pairs listed above.

## 2. LINE ITEMS (every table line, incl. zero/nil/dash). One row per table line; IDs cover all period columns.
table | page | line | ROW IDs | n_values | A2 flags
standalone balance sheet | 3 | 137 | R001-R002 | 2 | 
standalone balance sheet | 3 | 138 | R003-R004 | 2 | 
standalone balance sheet | 3 | 140 | R005-R006 | 2 | 
standalone balance sheet | 3 | 141 | R007-R008 | 2 | 
standalone balance sheet | 3 | 142 | R009-R010 | 2 | 
standalone balance sheet | 3 | 143 | R011-R012 | 2 | 
standalone balance sheet | 3 | 145 | R013-R014 | 2 | 
standalone balance sheet | 3 | 147 | R015-R016 | 2 | 
standalone balance sheet | 3 | 148 | R017-R018 | 2 | 
standalone balance sheet | 3 | 149 | R019-R020 | 2 | 
standalone balance sheet | 3 | 150 | R021-R022 | 2 | 
standalone balance sheet | 3 | 151 | R023-R024 | 2 | 
standalone balance sheet | 3 | 152 | R025-R026 | 2 | 
standalone balance sheet | 3 | 153 | R027-R028 | 2 | 
standalone balance sheet | 3 | 156 | R029-R030 | 2 | 
standalone balance sheet | 3 | 157 | R031-R032 | 2 | 
standalone balance sheet | 3 | 158 | R033-R034 | 2 | ZERO_STANDING
standalone balance sheet | 3 | 159 | R035-R036 | 2 | 
standalone balance sheet | 3 | 163 | R037-R038 | 2 | 
standalone balance sheet | 3 | 164 | R039-R040 | 2 | 
standalone balance sheet | 3 | 165 | R041-R042 | 2 | 
standalone balance sheet | 3 | 168 | R043-R044 | 2 | 
standalone balance sheet | 3 | 170 | R045-R046 | 2 | 
standalone balance sheet | 3 | 171 | R047-R048 | 2 | 
standalone balance sheet | 3 | 172 | R049-R050 | 2 | 
standalone balance sheet | 3 | 173 | R051-R052 | 2 | 
standalone balance sheet | 3 | 174 | R053-R054 | 2 | 
standalone balance sheet | 3 | 175 | R055-R056 | 2 | 
standalone balance sheet | 3 | 176 | R057-R058 | 2 | 
standalone results | 4 | 189 | R059-R064 | 6 | 
standalone results | 4 | 190 | R065-R070 | 6 | 
standalone results | 4 | 191 | R071-R076 | 6 | 
standalone results | 4 | 193 | R077-R082 | 6 | 
standalone results | 4 | 194 | R083-R088 | 6 | 
standalone results | 4 | 195 | R089-R094 | 6 | 
standalone results | 4 | 196 | R095-R100 | 6 | 
standalone results | 4 | 197 | R101-R106 | 6 | 
standalone results | 4 | 198 | R107-R112 | 6 | 
standalone results | 4 | 199 | R113-R118 | 6 | 
standalone results | 4 | 200 | R119-R124 | 6 | 
standalone results | 4 | 201 | R125-R130 | 6 | 
standalone results | 4 | 203 | R131-R136 | 6 | 
standalone results | 4 | 204 | R137-R142 | 6 | 
standalone results | 4 | 205 | R143-R148 | 6 | ZERO_STANDING
standalone results | 4 | 206 | R149-R154 | 6 | 
standalone results | 4 | 208 | R155-R160 | 6 | 
standalone results | 4 | 209 | R161-R166 | 6 | 
standalone results | 4 | 210 | R167-R172 | 6 | ZERO_STANDING
standalone results | 4 | 211 | R173-R178 | 6 | ZERO_STANDING
standalone results | 4 | 212 | R179-R184 | 6 | 
standalone results | 4 | 213 | R185-R190 | 6 | 
standalone results | 4 | 214 | R191-R196 | 6 | 
standalone results | 4 | 215 | R197 | 1 | 
standalone results | 4 | 217 | R198-R203 | 6 | 
standalone results | 4 | 218 | R204-R209 | 6 | 
standalone cash flow | 5 | 232 | R210-R211 | 2 | 
standalone cash flow | 5 | 234 | R212-R213 | 2 | 
standalone cash flow | 5 | 235 | R214-R215 | 2 | 
standalone cash flow | 5 | 236 | R216-R217 | 2 | 
standalone cash flow | 5 | 237 | R218-R219 | 2 | 
standalone cash flow | 5 | 238 | R220-R221 | 2 | ZERO_STANDING
standalone cash flow | 5 | 239 | R222-R223 | 2 | 
standalone cash flow | 5 | 240 | R224-R225 | 2 | 
standalone cash flow | 5 | 241 | R226-R227 | 2 | ZERO_STANDING
standalone cash flow | 5 | 242 | R228-R229 | 2 | ZERO_STANDING
standalone cash flow | 5 | 243 | R230-R231 | 2 | 
standalone cash flow | 5 | 244 | R232-R233 | 2 | 
standalone cash flow | 5 | 247 | R234-R235 | 2 | 
standalone cash flow | 5 | 248 | R236-R237 | 2 | 
standalone cash flow | 5 | 249 | R238-R239 | 2 | 
standalone cash flow | 5 | 250 | R240-R241 | 2 | 
standalone cash flow | 5 | 251 | R242-R243 | 2 | 
standalone cash flow | 5 | 252 | R244-R245 | 2 | 
standalone cash flow | 5 | 253 | R246-R247 | 2 | 
standalone cash flow | 5 | 254 | R248-R249 | 2 | 
standalone cash flow | 5 | 255 | R250-R251 | 2 | 
standalone cash flow | 5 | 256 | R252-R253 | 2 | 
standalone cash flow | 5 | 258 | R254-R255 | 2 | 
standalone cash flow | 5 | 259 | R256-R257 | 2 | 
standalone cash flow | 5 | 261 | R258-R259 | 2 | 
standalone cash flow | 5 | 262 | R260-R261 | 2 | 
standalone cash flow | 5 | 263 | R262-R263 | 2 | 
standalone cash flow | 5 | 264 | R264-R265 | 2 | 
standalone cash flow | 5 | 265 | R266-R267 | 2 | 
standalone cash flow | 5 | 266 | R268-R269 | 2 | ZERO_STANDING
standalone cash flow | 5 | 267 | R270-R271 | 2 | 
standalone cash flow | 5 | 268 | R272-R273 | 2 | 
standalone cash flow | 5 | 270 | R274-R275 | 2 | ZERO_STANDING
standalone cash flow | 5 | 271 | R276-R277 | 2 | ZERO_STANDING
standalone cash flow | 5 | 272 | R278-R279 | 2 | 
standalone cash flow | 5 | 273 | R280-R281 | 2 | ZERO_STANDING(all periods)
standalone cash flow | 5 | 274 | R282-R283 | 2 | 
standalone cash flow | 5 | 275 | R284-R285 | 2 | ZERO_STANDING(all periods)
standalone cash flow | 5 | 276 | R286-R287 | 2 | 
standalone cash flow | 5 | 277 | R288-R289 | 2 | 
standalone cash flow | 5 | 278 | R290-R291 | 2 | ZERO_STANDING(all periods)
standalone cash flow | 5 | 279 | R292-R293 | 2 | 
standalone cash flow | 5 | 280 | R294-R295 | 2 | 
standalone cash flow | 5 | 281 | R296-R297 | 2 | 
consolidated balance sheet | 9 | 415 | R298-R299 | 2 | 
consolidated balance sheet | 9 | 416 | R300-R301 | 2 | 
consolidated balance sheet | 9 | 417 | R302-R303 | 2 | 
consolidated balance sheet | 9 | 418 | R304-R305 | 2 | 
consolidated balance sheet | 9 | 420 | R306-R307 | 2 | 
consolidated balance sheet | 9 | 421 | R308-R309 | 2 | 
consolidated balance sheet | 9 | 422 | R310-R311 | 2 | 
consolidated balance sheet | 9 | 423 | R312-R313 | 2 | 
consolidated balance sheet | 9 | 425 | R314-R315 | 2 | 
consolidated balance sheet | 9 | 427 | R316-R317 | 2 | 
consolidated balance sheet | 9 | 428 | R318-R319 | 2 | 
consolidated balance sheet | 9 | 429 | R320-R321 | 2 | 
consolidated balance sheet | 9 | 430 | R322-R323 | 2 | 
consolidated balance sheet | 9 | 431 | R324-R325 | 2 | 
consolidated balance sheet | 9 | 432 | R326-R327 | 2 | 
consolidated balance sheet | 9 | 433 | R328-R329 | 2 | 
consolidated balance sheet | 9 | 436 | R330-R331 | 2 | 
consolidated balance sheet | 9 | 437 | R332-R333 | 2 | 
consolidated balance sheet | 9 | 438 | R334-R335 | 2 | ZERO_STANDING
consolidated balance sheet | 9 | 439 | R336-R337 | 2 | 
consolidated balance sheet | 9 | 440 | R338-R339 | 2 | 
consolidated balance sheet | 9 | 444 | R340-R341 | 2 | 
consolidated balance sheet | 9 | 445 | R342-R343 | 2 | 
consolidated balance sheet | 9 | 446 | R344-R345 | 2 | 
consolidated balance sheet | 9 | 449 | R346-R347 | 2 | 
consolidated balance sheet | 9 | 451 | R348-R349 | 2 | 
consolidated balance sheet | 9 | 452 | R350-R351 | 2 | 
consolidated balance sheet | 9 | 453 | R352-R353 | 2 | 
consolidated balance sheet | 9 | 454 | R354-R355 | 2 | 
consolidated balance sheet | 9 | 455 | R356-R357 | 2 | 
consolidated balance sheet | 9 | 456 | R358-R359 | 2 | 
consolidated balance sheet | 9 | 457 | R360-R361 | 2 | 
consolidated results | 10 | 469 | R362-R365 | 4 | 
consolidated results | 10 | 470 | R366-R369 | 4 | 
consolidated results | 10 | 471 | R370-R373 | 4 | 
consolidated results | 10 | 473 | R374-R377 | 4 | 
consolidated results | 10 | 474 | R378-R381 | 4 | 
consolidated results | 10 | 475 | R382-R385 | 4 | 
consolidated results | 10 | 476 | R386-R389 | 4 | 
consolidated results | 10 | 477 | R390-R393 | 4 | 
consolidated results | 10 | 478 | R394-R397 | 4 | 
consolidated results | 10 | 479 | R398-R401 | 4 | 
consolidated results | 10 | 480 | R402-R405 | 4 | 
consolidated results | 10 | 481 | R406-R409 | 4 | 
consolidated results | 10 | 483 | R410-R413 | 4 | 
consolidated results | 10 | 484 | R414-R417 | 4 | 
consolidated results | 10 | 485 | R418-R421 | 4 | ZERO_STANDING
consolidated results | 10 | 486 | R422-R425 | 4 | 
consolidated results | 10 | 487 | R426-R429 | 4 | ZERO_STANDING
consolidated results | 10 | 488 | R430-R433 | 4 | 
consolidated results | 10 | 490 | R434-R437 | 4 | 
consolidated results | 10 | 491 | R438-R441 | 4 | 
consolidated results | 10 | 492 | R442-R445 | 4 | ZERO_STANDING
consolidated results | 10 | 493 | R446-R449 | 4 | ZERO_STANDING
consolidated results | 10 | 494 | R450-R453 | 4 | 
consolidated results | 10 | 495 | R454-R457 | 4 | 
consolidated results | 10 | 496 | R458-R461 | 4 | 
consolidated results | 10 | 498 | R462-R465 | 4 | 
consolidated results | 10 | 499 | R466-R469 | 4 | 
consolidated results | 10 | 501 | R470-R473 | 4 | 
consolidated results | 10 | 502 | R474-R477 | 4 | ZERO_STANDING(all periods)
consolidated results | 10 | 504 | R478-R481 | 4 | 
consolidated results | 10 | 505 | R482-R485 | 4 | 
consolidated results | 10 | 506 | R486-R489 | 4 | 
consolidated results | 10 | 507 | R490 | 1 | 
consolidated results | 10 | 509 | R491-R494 | 4 | 
consolidated results | 10 | 510 | R495-R498 | 4 | 
consolidated cash flow | 11 | 526 | R499 | 1 | 
consolidated cash flow | 11 | 528 | R500 | 1 | 
consolidated cash flow | 11 | 529 | R501 | 1 | 
consolidated cash flow | 11 | 530 | R502 | 1 | 
consolidated cash flow | 11 | 531 | R503 | 1 | ZERO_STANDING(all periods)
consolidated cash flow | 11 | 532 | R504 | 1 | 
consolidated cash flow | 11 | 533 | R505 | 1 | 
consolidated cash flow | 11 | 534 | R506 | 1 | 
consolidated cash flow | 11 | 535 | R507 | 1 | 
consolidated cash flow | 11 | 536 | R508 | 1 | ZERO_STANDING(all periods)
consolidated cash flow | 11 | 537 | R509 | 1 | 
consolidated cash flow | 11 | 538 | R510 | 1 | 
consolidated cash flow | 11 | 541 | R511 | 1 | 
consolidated cash flow | 11 | 542 | R512 | 1 | 
consolidated cash flow | 11 | 543 | R513 | 1 | 
consolidated cash flow | 11 | 544 | R514 | 1 | 
consolidated cash flow | 11 | 545 | R515 | 1 | 
consolidated cash flow | 11 | 546 | R516 | 1 | 
consolidated cash flow | 11 | 547 | R517 | 1 | 
consolidated cash flow | 11 | 548 | R518 | 1 | 
consolidated cash flow | 11 | 549 | R519 | 1 | 
consolidated cash flow | 11 | 550 | R520 | 1 | 
consolidated cash flow | 11 | 552 | R521 | 1 | 
consolidated cash flow | 11 | 553 | R522 | 1 | 
consolidated cash flow | 11 | 555 | R523 | 1 | 
consolidated cash flow | 11 | 556 | R524 | 1 | 
consolidated cash flow | 11 | 557 | R525 | 1 | 
consolidated cash flow | 11 | 558 | R526 | 1 | 
consolidated cash flow | 11 | 559 | R527 | 1 | 
consolidated cash flow | 11 | 560 | R528 | 1 | ZERO_STANDING(all periods)
consolidated cash flow | 11 | 561 | R529 | 1 | 
consolidated cash flow | 11 | 562 | R530 | 1 | 
consolidated cash flow | 11 | 564 | R531 | 1 | ZERO_STANDING(all periods)
consolidated cash flow | 11 | 565 | R532 | 1 | 
consolidated cash flow | 11 | 566 | R533 | 1 | 
consolidated cash flow | 11 | 567 | R534 | 1 | ZERO_STANDING(all periods)
consolidated cash flow | 11 | 568 | R535 | 1 | 
consolidated cash flow | 11 | 569 | R536 | 1 | ZERO_STANDING(all periods)
consolidated cash flow | 11 | 570 | R537 | 1 | 
consolidated cash flow | 11 | 571 | R538 | 1 | 
consolidated cash flow | 11 | 572 | R539 | 1 | ZERO_STANDING(all periods)
consolidated cash flow | 11 | 573 | R540 | 1 | 
consolidated cash flow | 11 | 574 | R541 | 1 | 
consolidated cash flow | 11 | 575 | R542 | 1 | 

Cross-references among table lines (RESTATED across statements, no interpretation):
- Standalone BS cash 30.09.2026 R017 = cash flow closing R296 | R017,R296 | RESTATED
- Standalone BS cash 31.03.2026 R018 = cash flow opening R294 | R018,R294 | RESTATED
- Standalone H1 PBT R128 = cash flow PBT R210; H1 Sep-25 R129 (1690.41) vs R211 (1690.42) | R128,R210,R129,R211 | RESTATED (Sep-25 differs by 0.01)
- Standalone H1 finance cost R104 (272.49) vs cash flow R214 (271.94) | R104,R214 | RESTATED_DIFFERS
- Standalone H1 current tax R134 = tax paid R254 | R134,R254 | RESTATED
- Standalone H1 depreciation R110/R111 = cash flow R212/R213 | R110,R111,R212,R213 | RESTATED
- Standalone loans R019/R020 = consolidated loans R320/R321 | R019,R020,R320,R321 | RESTATED
- Share warrant money R033 = cash flow warrant proceeds R276 = consolidated R334 | R033,R276,R334 | RESTATED
- Paid-up share capital 6,199.75 repeated across periods | R029,R030,R191-R196 | RESTATED

## 3. NON-TABLE NUMBERS (meeting, identifiers, note figures)
group | ROW IDs | flags | note
Board meeting start 19:00 and end 20:30 | R543-R544 |  | 90 minutes; DATE R696
Letterhead identifiers (phone, GSTIN, CIN, DIN) p1 | R545-R548 |  | 
Auditor standalone: FRN, membership no, statutes, UDIN (p2) | R549-R553 |  | UDIN R553
Auditor consolidated: FRN, membership no, statutes, UDIN (p8) | R554-R558 |  | UDIN R558
Signature page DIN/CIN identifiers p3,4,5,9,10,11 | R559-R576 |  | 
Face value Rs 10 (p4, p10) | R577-R578 |  | 
Note 4 warrant figures p6 | R579-R587 |  | utilisation as at 30.06.2026
Note 5 investor complaints nil p6 | R588 | ZERO_STANDING | 
Note 6 Kidcity 75% p6 | R589 |  | 
Notes 11-12 figures p7 | R590-R597 |  | Elementa Lifespaces share of loss 24.07.2026 to 30.09.2026
Note 4 warrant figures p12 | R598-R606 |  | 
Note 5 investor complaints nil p12 | R607 | ZERO_STANDING | 
Note 6 Kidcity 75% p12 | R608 |  | 
Notes 11-12 figures p13 | R609-R616 |  | 
Declaration page p14 phone, GSTIN, CIN | R617-R619 |  | 
ISIN p14 | R620 | OCR_UNCERTAIN | third character zero or letter O
DIN p14 | R621 |  | 

## 4. AGENDA ITEMS (Board Outcome letter, p1)
item | ROW IDs | flags | note
Agenda 1: approve Un-Audited Standalone and Consolidated results, half year and quarter ended 30.09.2026, on Audit Committee recommendation | R626,R629,R688,R698,R733-R734 |  | only agenda item; no AR/AGM/dividend/record date/director/auditor/ESOP/fund-raise item in the letter (NOT DISCLOSED)
Meeting date 10 Oct 2026 (Saturday), venue Howrah | R627,R695-R696 |  | venue R627
Meeting times 19:00 to 20:30 | R543-R544 |  | 90 minutes
Letter addressee/signatory | R622-R625,R628,R697,R735 |  | digital signature 22:12:45 IST, after meeting concluded 20:30

## 5. AUDITOR REPORT PARAGRAPHS (limited review; standalone p2, consolidated p8)
para | scope | ROW IDs | flags
S1 intro: reviewed standalone statement | standalone | R630-R632,R637,R699-R700 | 
S2 management responsibility | standalone | R634-R635 | 
S3 scope: SRE 2410 review, moderate assurance, no audit opinion | standalone | R633,R736-R737 | 
S4 conclusion: unmodified, nothing came to attention | standalone | R738 | 
Signature block: partner, offices, UDIN | standalone | R549-R553,R636 | UDIN present
C1 intro: reviewed consolidated statement | consolidated | R638,R640,R645,R701-R702 | 
C2 management responsibility | consolidated | R642-R643 | 
C3 scope: SRE 2410 review, no audit opinion | consolidated | R641,R739-R740 | 
C4 conclusion: unmodified | consolidated | R741 | 
Entity list reviewed: Kidcity Solutions Pvt Ltd only | consolidated | R646 | associate Elementa Lifespaces not named in reviewed list
Signature block: partner, offices, UDIN | consolidated | R554-R558,R639,R644 | UDIN present
No Emphasis of Matter, Other Matters, Going Concern or qualification paragraph found (fulltext grep: none). Opinion: unmodified conclusion on limited review (not audit). Unaudited/management-furnished entities: not stated. Cash flow statements labelled 'Audited' on a half-year (R754, R755): FLAG LABEL_INCONSISTENT.

## 6. ENTITIES (consolidation list and all ENTITY rows)
entity | role | ROW IDs | flags
Karnika Industries Limited | registrant (parent) | R624,R632,R640,R659-R660,R687 | 
Kidcity Solutions Private Limited | 75% subsidiary, kids-wear retail, acquired 4 Oct 2025, full consolidation | R646,R662,R667,R672,R677 | ENTITY_CHANGE vs prior-year H1 (no consolidated comparatives)
Elementa Lifespaces Private Limited | 40% associate from 24.07.2026, equity method | R661,R669-R670,R679-R680 | ENTITY_CHANGE (new associate this half)
RDB Elementa Sports Academy Private Limited | counterparty, 26% subscription pending, not an associate | R668,R678 | PENDING_ITEM
AAAJ & Associates (formerly Uttam Agarwal & Associates), CA Deepak Agarwal | statutory auditor; firm renamed | R630-R631,R636-R639,R644-R645 | ENTITY_CHANGE (auditor firm name)
Signatories: Niranjan Mundhra MD, Mahesh Kumar Mundhra WTD, Krishan Kumar Karnani CFO | signatories | R625,R647-R658,R685-R686 | 
NSE, Audit Committee, regulations, standards, addresses | other | R622-R623,R626-R629,R633-R635,R641-R643,R663-R666,R671,R673-R676,R681-R684 | 

## 7. SIGNATURE BLOCKS
block | ROW IDs | note
Outcome letter digital signature, NIRANJAN MUNDHRA, MD, 2026.10.10 22:12:45 +05:30 | R625,R697,R735 | after meeting end 20:30
Auditor signature, CA Deepak Agarwal, Partner, 10 Oct 2026 (standalone, consolidated) | R631,R639,R699,R701 | UDINs R553 R558
Financial statement signature pages (p3,4,5,9,10,11) | R647-R658 | MD and WTD on each
Declaration Reg 33(3)(d) p14, MD and CFO, 10.10.2026 | R684-R686,R731-R732,R780 | declaration

## 8. DATES, FORWARD, QUALIFIERS
group | ROW IDs | flags | note
DATES letter/audit/period/notes p1-p14 | R695-R696,R698-R732 |  | 
DATE digital signature timestamp | R697 |  | after board end time
FORWARD items (availability, software under development, warrant conversion at Rs 121 within 18 months, RDB Elementa 26% pending) | R688-R694 | FORWARD | no guidance numbers; duplicated p6/p12
QUALIFIERS: unaudited/limited review/review scope/units/EPS/status/notes | R733-R744,R746-R752,R756-R758,R761-R764,R766-R770,R773-R776,R778-R780 |  | 
Asterisk on consolidated cash line, no footnote | R745 | FOOTNOTE_UNRESOLVED | fulltext grep confirms asterisk only at line 428
No prior-year consolidated comparative columns | R753,R765,R777 | NO_COMPARATIVE | Sep-25 consolidated columns absent
Cash flow labelled Audited on half year | R754-R755 | LABEL_INCONSISTENT | 
Utilisation summary as at 30.06.2026; unutilised balance blank | R759-R760,R771-R772 | BALANCE_NOT_PRINTED | value not printed

## MISSING_FROM_STRUCTURED
none found (fulltext spot-checked for notes, agenda, going concern, asterisks)