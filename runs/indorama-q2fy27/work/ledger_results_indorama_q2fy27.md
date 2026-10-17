# A2 LEDGER: INDORAMA Q2 FY27 results (A1 structured source; prior ledger ND, so no ENTITY_CHANGE diff possible)
```
=== A2 COUNT TEST ===
category: notes          grep_count: 12  sweep_count: 12  match: yes   (8 numbered Notes 1-4 x2 filings + 4 table-heading Note labels R696,R697,R712,R713)
category: line_items     grep_count: 198  sweep_count: 198  match: yes   (distinct page/line/label groups over 626 table cells R001-R626)
category: zero_standing  grep_count: 85  sweep_count: 85  match: yes   (cells; 22 line items carry >=1)
category: agenda_items   grep_count: 2  sweep_count: 2  match: yes   (items a and b; board times R629,R630)
category: auditor_paras  grep_count: 10  sweep_count: 10  match: yes  (R690-692,R704-707 + UDIN/firm/partner R634-637,R639-641 grouped)
category: entities       grep_count: 24  sweep_count: 24  match: yes
gate_a2: pass
=== END COUNT TEST ===
```
ids_in_structured: 721 | ids_referenced_in_ledger: 721 | orphan_ids: [] | match: yes

## 1 Notes
R700 | note | | standalone Note 1 basis (p6)
R701 | note | | standalone Note 2 approval (p6)
R702 | note | | standalone Note 3 segment (p6)
R703 | note | | standalone Note 4 reference (p6)
R716 | note | | consol Note 1 (p12)
R717 | note | | consol Note 2 Ind AS 110 (p12)
R718 | note | | consol Note 3 segment (p12)
R719 | note | | consol Note 4 reference (p12)
R696 | note | | table label Note:1 BS standalone (p4)
R697 | note | | table label Note:2 CF standalone (p5)
R712 | note | | table label Note No.1 BS consol (p10)
R713 | note | | table label Note No.2 CF consol (p11)
Unnumbered/footnote qualifiers (no asterisk footnotes found): R686-R699, R704-R715 grouped as QUALIFIER rows, each referenced by ID; R720,R721 extractor flags (EXTRACTOR_FLAG, not source).

## 2 Line items (ID range, cells; cells = periods/dates; ZERO_STANDING cells listed)
R001-R006 (6) | line_item |  | page 3 line 196; standalone Revenue from operations
R007-R012 (6) | line_item |  | page 3 line 197; standalone Other income
R013-R018 (6) | line_item |  | page 3 line 198; standalone Total income (1+2)
R019-R024 (6) | line_item |  | page 3 line 199; standalone (a) Cost of materials consumed
R025-R030 (6) | line_item |  | page 3 line 200; standalone (b) Purchase of stock-in-trade
R031-R036 (6) | line_item |  | page 3 line 201; standalone (c) Changes in inventories of finished goods, WIP and stock-in-trade
R037-R042 (6) | line_item |  | page 3 line 202; standalone (d) Employee benefits expense
R043-R048 (6) | line_item |  | page 3 line 203; standalone (e) Other expenses
R049-R054 (6) | line_item |  | page 3 line 204; standalone Total expenses before D&A, finance costs and FX loss/(gain)
R055-R060 (6) | line_item |  | page 3 line 205; standalone Profit from operations before D&A, finance costs and FX loss/(gain) (3-4)
R061-R066 (6) | line_item |  | page 3 line 206; standalone Depreciation and amortisation expense
R067-R072 (6) | line_item |  | page 3 line 207; standalone Finance costs
R073-R078 (6) | line_item |  | page 3 line 208; standalone Foreign exchange fluctuation loss
R079-R084 (6) | line_item |  | page 3 line 209; standalone Total expenses before tax (4+6+7+8)
R085-R090 (6) | line_item |  | page 3 line 210; standalone Profit before exceptional items and tax (3-9)
R091-R096 (6) | line_item | ZERO_STANDING:R091,R092,R093,R094,R095 | page 3 line 211; standalone Exceptional items - Employee benefit expenses
R097-R102 (6) | line_item |  | page 3 line 212; standalone Profit/(loss) before tax (10-11)
R103-R108 (6) | line_item | ZERO_STANDING:R103,R104,R105,R106,R107,R108 | page 3 line 213; standalone Tax expense/(credit)
R109-R114 (6) | line_item | ZERO_STANDING:R109,R110,R111,R112,R113,R114 | page 3 line 214; standalone Deferred tax (credit)/expense
R115-R120 (6) | line_item |  | page 3 line 215; standalone Net profit/(loss) for the period (12-13)
R121-R126 (6) | line_item | ZERO_STANDING:R121,R122,R123,R124,R125 | page 3 line 216; standalone OCI (i) Items not reclassified to profit or loss
R127-R132 (6) | line_item | ZERO_STANDING:R127,R128,R129,R130,R131,R132 | page 3 line 217; standalone OCI (ii) Income tax on items not reclassified
R133-R138 (6) | line_item |  | page 3 line 218; standalone Total comprehensive income for the period (14+15)
R139-R144 (6) | line_item |  | page 3 line 219; standalone Paid-up equity share capital (FV Rs 10)
R145-R145 (1) | line_item |  | page 3 line 220; standalone Other equity
R146-R151 (6) | line_item |  | page 3 line 221; standalone EPS (a) Basic (Rs, not annualised for quarters)
R152-R157 (6) | line_item |  | page 3 line 222; standalone EPS (b) Diluted (Rs, not annualised for quarters)
R158-R159 (2) | line_item |  | page 4 line 288; standalone Property, plant and equipment
R160-R161 (2) | line_item |  | page 4 line 289; standalone Right of use assets
R162-R163 (2) | line_item |  | page 4 line 290; standalone Capital work-in-progress
R164-R165 (2) | line_item | ZERO_STANDING:R165 | page 4 line 291; standalone Intangible assets
R166-R167 (2) | line_item |  | page 4 line 292; standalone Investments (non-current)
R168-R169 (2) | line_item |  | page 4 line 293; standalone Loans (non-current)
R170-R171 (2) | line_item |  | page 4 line 294; standalone Other financial assets (non-current)
R172-R173 (2) | line_item |  | page 4 line 295; standalone Deferred tax assets (net)
R174-R175 (2) | line_item |  | page 4 line 296; standalone Non-current tax assets (net)
R176-R177 (2) | line_item |  | page 4 line 297; standalone Other non-current assets
R178-R179 (2) | line_item |  | page 4 line 298; standalone Total non-current assets
R180-R181 (2) | line_item |  | page 4 line 299; standalone Inventories
R182-R183 (2) | line_item |  | page 4 line 300; standalone Trade receivables
R184-R185 (2) | line_item |  | page 4 line 301; standalone Cash and cash equivalents
R186-R187 (2) | line_item |  | page 4 line 302; standalone Bank balances other than cash and cash equivalents
R188-R189 (2) | line_item |  | page 4 line 303; standalone Loans (current)
R190-R191 (2) | line_item |  | page 4 line 304; standalone Other financial assets (current)
R192-R193 (2) | line_item |  | page 4 line 305; standalone Other current assets
R194-R195 (2) | line_item |  | page 4 line 306; standalone Total current assets
R196-R197 (2) | line_item |  | page 4 line 307; standalone TOTAL ASSETS
R198-R199 (2) | line_item |  | page 4 line 308; standalone Equity share capital
R200-R201 (2) | line_item |  | page 4 line 309; standalone Other equity
R202-R203 (2) | line_item |  | page 4 line 310; standalone Total equity
R204-R205 (2) | line_item |  | page 4 line 311; standalone Borrowings (non-current)
R206-R207 (2) | line_item |  | page 4 line 312; standalone Lease liabilities (non-current)
R208-R209 (2) | line_item |  | page 4 line 313; standalone Provisions (non-current)
R210-R211 (2) | line_item |  | page 4 line 314; standalone Total non-current liabilities
R212-R213 (2) | line_item |  | page 4 line 315; standalone Borrowings (current)
R214-R215 (2) | line_item |  | page 4 line 316; standalone Lease liabilities (current)
R216-R217 (2) | line_item |  | page 4 line 317; standalone Trade payables MSME
R218-R219 (2) | line_item |  | page 4 line 318; standalone Trade payables other than MSME
R220-R221 (2) | line_item |  | page 4 line 319; standalone Other financial liabilities (current)
R222-R223 (2) | line_item |  | page 4 line 320; standalone Other current liabilities
R224-R225 (2) | line_item |  | page 4 line 321; standalone Provisions (current)
R226-R227 (2) | line_item |  | page 4 line 322; standalone Total current liabilities
R228-R229 (2) | line_item |  | page 4 line 323; standalone TOTAL EQUITY AND LIABILITIES
R230-R231 (2) | line_item |  | page 5 line 374; standalone cash flow Profit/(loss) before tax
R232-R233 (2) | line_item |  | page 5 line 375; standalone cash flow Depreciation and amortisation expense
R234-R235 (2) | line_item |  | page 5 line 376; standalone cash flow (Gain)/Loss on disposal of PPE
R236-R237 (2) | line_item |  | page 5 line 377; standalone cash flow Finance costs
R238-R239 (2) | line_item |  | page 5 line 378; standalone cash flow Interest income
R240-R241 (2) | line_item |  | page 5 line 379; standalone cash flow Debts/advances written off
R242-R243 (2) | line_item |  | page 5 line 380; standalone cash flow Operating profit before working capital changes
R244-R245 (2) | line_item |  | page 5 line 381; standalone cash flow Changes in trade receivables
R246-R247 (2) | line_item |  | page 5 line 382; standalone cash flow Changes in other financial assets and loans
R248-R249 (2) | line_item |  | page 5 line 383; standalone cash flow Changes in other assets
R250-R251 (2) | line_item |  | page 5 line 384; standalone cash flow Changes in inventories
R252-R253 (2) | line_item |  | page 5 line 385; standalone cash flow Changes in trade payables
R254-R255 (2) | line_item |  | page 5 line 386; standalone cash flow Changes in provisions
R256-R257 (2) | line_item |  | page 5 line 387; standalone cash flow Changes in other financial liabilities
R258-R259 (2) | line_item |  | page 5 line 388; standalone cash flow Changes in other liabilities
R260-R261 (2) | line_item |  | page 5 line 389; standalone cash flow Cash generated from operations before tax
R262-R263 (2) | line_item |  | page 5 line 390; standalone cash flow Income taxes refund/(paid) net
R264-R265 (2) | line_item |  | page 5 line 391; standalone cash flow Net cash from operating activities [A]
R266-R267 (2) | line_item |  | page 5 line 392; standalone cash flow Purchase of PPE incl CWIP, capital advances and creditors
R268-R269 (2) | line_item | ZERO_STANDING:R268 | page 5 line 393; standalone cash flow Proceeds from sale of PPE
R270-R271 (2) | line_item |  | page 5 line 394; standalone cash flow Loans to subsidiaries (net)
R272-R273 (2) | line_item |  | page 5 line 395; standalone cash flow Bank balances other than cash and cash equivalents [net]
R274-R275 (2) | line_item |  | page 5 line 396; standalone cash flow Interest received
R276-R277 (2) | line_item |  | page 5 line 397; standalone cash flow Net cash from investing activities [B]
R278-R279 (2) | line_item |  | page 5 line 398; standalone cash flow Repayment of non-current borrowings
R280-R281 (2) | line_item | ZERO_STANDING:R280 | page 5 line 399; standalone cash flow Proceeds from non-current borrowings
R282-R283 (2) | line_item |  | page 5 line 400; standalone cash flow Movement in current borrowings [net]
R284-R285 (2) | line_item |  | page 5 line 401; standalone cash flow Payment of lease liabilities (principal)
R286-R287 (2) | line_item |  | page 5 line 402; standalone cash flow Payment of lease liabilities (interest)
R288-R289 (2) | line_item |  | page 5 line 403; standalone cash flow Finance costs paid
R290-R291 (2) | line_item |  | page 5 line 404; standalone cash flow Net cash from financing activities [C]
R292-R293 (2) | line_item |  | page 5 line 405; standalone cash flow Net increase/(decrease) in cash [A+B+C]
R294-R295 (2) | line_item |  | page 5 line 406; standalone cash flow Opening balance of cash
R296-R297 (2) | line_item |  | page 5 line 407; standalone cash flow Closing balance of cash
R298-R303 (6) | line_item |  | page 9 line 590; consolidated Revenue from operations
R304-R309 (6) | line_item |  | page 9 line 591; consolidated Other income
R310-R315 (6) | line_item |  | page 9 line 592; consolidated Total income (1+2)
R316-R321 (6) | line_item |  | page 9 line 593; consolidated (a) Cost of materials consumed
R322-R327 (6) | line_item |  | page 9 line 594; consolidated (b) Purchase of stock-in-trade
R328-R333 (6) | line_item |  | page 9 line 595; consolidated (c) Changes in inventories of finished goods, WIP and stock-in-trade
R334-R339 (6) | line_item |  | page 9 line 596; consolidated (d) Employee benefits expense
R340-R345 (6) | line_item |  | page 9 line 597; consolidated (e) Other expenses
R346-R351 (6) | line_item |  | page 9 line 598; consolidated Total expenses before D&A, finance costs and FX loss/(gain)
R352-R357 (6) | line_item |  | page 9 line 599; consolidated Profit from operations before D&A, finance costs and FX loss/(gain) (3-4)
R358-R363 (6) | line_item |  | page 9 line 600; consolidated Depreciation and amortisation expense
R364-R369 (6) | line_item |  | page 9 line 601; consolidated Finance costs
R370-R375 (6) | line_item |  | page 9 line 602; consolidated Foreign exchange fluctuation loss
R376-R381 (6) | line_item |  | page 9 line 603; consolidated Total expenses before tax (4+6+7+8)
R382-R387 (6) | line_item |  | page 9 line 604; consolidated Profit before exceptional items and tax (3-9)
R388-R393 (6) | line_item | ZERO_STANDING:R388,R389,R390,R391,R392 | page 9 line 605; consolidated Exceptional item - Employee benefit expenses
R394-R399 (6) | line_item |  | page 9 line 606; consolidated Profit/(loss) before tax (10-11)
R400-R405 (6) | line_item | ZERO_STANDING:R400,R401,R402,R403,R404,R405 | page 9 line 607; consolidated Tax expense
R406-R411 (6) | line_item | ZERO_STANDING:R407,R408,R410,R411 | page 9 line 608; consolidated Deferred tax (credit)
R412-R417 (6) | line_item |  | page 9 line 609; consolidated Net profit/(loss) for the period (12-13)
R418-R423 (6) | line_item | ZERO_STANDING:R418,R419,R420,R421,R422 | page 9 line 610; consolidated OCI (i) Items not reclassified to profit or loss
R424-R429 (6) | line_item | ZERO_STANDING:R424,R425,R426,R427,R428,R429 | page 9 line 611; consolidated OCI (ii) Income tax on items not reclassified
R430-R435 (6) | line_item |  | page 9 line 612; consolidated Total comprehensive income for the period (14+15)
R436-R441 (6) | line_item |  | page 9 line 613; consolidated Profit attributable to Owners of the parent
R442-R447 (6) | line_item | ZERO_STANDING:R442,R443,R444,R445,R446,R447 | page 9 line 614; consolidated Profit attributable to Non Controlling interest
R448-R453 (6) | line_item | ZERO_STANDING:R448,R449,R450,R451,R452 | page 9 line 615; consolidated OCI attributable to Owners of the parent
R454-R459 (6) | line_item | ZERO_STANDING:R454,R455,R456,R457,R458,R459 | page 9 line 616; consolidated OCI attributable to Non Controlling interest
R460-R465 (6) | line_item |  | page 9 line 617; consolidated Total comprehensive income attributable to Owners of the parent
R466-R471 (6) | line_item | ZERO_STANDING:R466,R467,R468,R469,R470,R471 | page 9 line 618; consolidated Total comprehensive income attributable to Non Controlling interest
R472-R477 (6) | line_item |  | page 9 line 619; consolidated Paid-up equity share capital (FV Rs 10)
R478-R478 (1) | line_item |  | page 9 line 620; consolidated Other equity
R479-R484 (6) | line_item |  | page 9 line 621; consolidated EPS (a) Basic (Rs, not annualised for quarters)
R485-R490 (6) | line_item |  | page 9 line 622; consolidated EPS (b) Diluted (Rs, not annualised for quarters)
R491-R492 (2) | line_item |  | page 10 line 680; consolidated Property, plant and equipment
R493-R494 (2) | line_item |  | page 10 line 681; consolidated Right of use assets
R495-R496 (2) | line_item |  | page 10 line 682; consolidated Capital work-in-progress
R497-R498 (2) | line_item | ZERO_STANDING:R498 | page 10 line 683; consolidated Intangible assets
R499-R500 (2) | line_item |  | page 10 line 684; consolidated Other financial assets (non-current)
R501-R502 (2) | line_item |  | page 10 line 685; consolidated Deferred tax assets (net)
R503-R504 (2) | line_item |  | page 10 line 686; consolidated Non-current tax assets (net)
R505-R506 (2) | line_item |  | page 10 line 687; consolidated Other non-current assets
R507-R508 (2) | line_item |  | page 10 line 688; consolidated Total non-current assets
R509-R510 (2) | line_item |  | page 10 line 689; consolidated Inventories
R511-R512 (2) | line_item |  | page 10 line 690; consolidated Trade receivables
R513-R514 (2) | line_item |  | page 10 line 691; consolidated Cash and cash equivalents
R515-R516 (2) | line_item |  | page 10 line 692; consolidated Bank balances other than cash and cash equivalents
R517-R518 (2) | line_item |  | page 10 line 693; consolidated Loans (current)
R519-R520 (2) | line_item |  | page 10 line 694; consolidated Other financial assets (current)
R521-R522 (2) | line_item |  | page 10 line 695; consolidated Other current assets
R523-R524 (2) | line_item |  | page 10 line 696; consolidated Total current assets
R525-R526 (2) | line_item |  | page 10 line 697; consolidated TOTAL ASSETS
R527-R528 (2) | line_item |  | page 10 line 698; consolidated Equity share capital
R529-R530 (2) | line_item |  | page 10 line 699; consolidated Other equity
R531-R532 (2) | line_item |  | page 10 line 700; consolidated Total equity
R533-R534 (2) | line_item |  | page 10 line 701; consolidated Borrowings (non-current)
R535-R536 (2) | line_item |  | page 10 line 702; consolidated Lease liabilities (non-current)
R537-R538 (2) | line_item |  | page 10 line 703; consolidated Provisions (non-current)
R539-R540 (2) | line_item | ZERO_STANDING:R540 | page 10 line 704; consolidated Deferred tax liabilities (net)
R541-R542 (2) | line_item |  | page 10 line 705; consolidated Total non-current liabilities
R543-R544 (2) | line_item |  | page 10 line 706; consolidated Borrowings (current)
R545-R546 (2) | line_item |  | page 10 line 707; consolidated Lease liabilities (current)
R547-R548 (2) | line_item |  | page 10 line 708; consolidated Trade payables MSME
R549-R550 (2) | line_item |  | page 10 line 709; consolidated Trade payables other than MSME
R551-R552 (2) | line_item |  | page 10 line 710; consolidated Other financial liabilities (current)
R553-R554 (2) | line_item |  | page 10 line 711; consolidated Other current liabilities
R555-R556 (2) | line_item |  | page 10 line 712; consolidated Provisions (current)
R557-R558 (2) | line_item |  | page 10 line 713; consolidated Total current liabilities
R559-R560 (2) | line_item |  | page 10 line 714; consolidated TOTAL EQUITY AND LIABILITIES
R561-R562 (2) | line_item |  | page 11 line 767; consolidated cash flow Profit before tax
R563-R564 (2) | line_item |  | page 11 line 768; consolidated cash flow Depreciation and amortisation expense
R565-R566 (2) | line_item |  | page 11 line 769; consolidated cash flow (Gain)/Loss on disposal of PPE
R567-R568 (2) | line_item |  | page 11 line 770; consolidated cash flow Finance costs
R569-R570 (2) | line_item |  | page 11 line 771; consolidated cash flow Interest income
R571-R572 (2) | line_item |  | page 11 line 772; consolidated cash flow Debts/advances written off
R573-R574 (2) | line_item |  | page 11 line 773; consolidated cash flow Operating profit before working capital changes
R575-R576 (2) | line_item |  | page 11 line 774; consolidated cash flow Changes in trade receivables
R577-R578 (2) | line_item |  | page 11 line 775; consolidated cash flow Changes in other financial assets and loans
R579-R580 (2) | line_item |  | page 11 line 776; consolidated cash flow Changes in other assets
R581-R582 (2) | line_item |  | page 11 line 777; consolidated cash flow Changes in inventories
R583-R584 (2) | line_item |  | page 11 line 778; consolidated cash flow Changes in trade payables
R585-R586 (2) | line_item |  | page 11 line 779; consolidated cash flow Changes in provisions
R587-R588 (2) | line_item |  | page 11 line 780; consolidated cash flow Changes in other financial liabilities
R589-R590 (2) | line_item |  | page 11 line 781; consolidated cash flow Changes in other liabilities
R591-R592 (2) | line_item |  | page 11 line 782; consolidated cash flow Cash generated from operations before tax
R593-R594 (2) | line_item |  | page 11 line 783; consolidated cash flow Income taxes (paid)/refund net
R595-R596 (2) | line_item |  | page 11 line 784; consolidated cash flow Net cash from operating activities [A]
R597-R598 (2) | line_item |  | page 11 line 785; consolidated cash flow Purchase of PPE incl CWIP, capital advances and creditors
R599-R600 (2) | line_item | ZERO_STANDING:R599 | page 11 line 786; consolidated cash flow Proceeds from sale of PPE
R601-R602 (2) | line_item | ZERO_STANDING:R601 | page 11 line 787; consolidated cash flow Bank balances other than cash and cash equivalents [net]
R603-R604 (2) | line_item |  | page 11 line 788; consolidated cash flow Interest received
R605-R606 (2) | line_item |  | page 11 line 789; consolidated cash flow Net cash from investing activities [B]
R607-R608 (2) | line_item |  | page 11 line 790; consolidated cash flow Repayment of non-current borrowings
R609-R610 (2) | line_item | ZERO_STANDING:R609 | page 11 line 791; consolidated cash flow Proceeds from non-current borrowings
R611-R612 (2) | line_item |  | page 11 line 792; consolidated cash flow Movement in current borrowings [net]
R613-R614 (2) | line_item |  | page 11 line 793; consolidated cash flow Payment of lease liabilities (principal)
R615-R616 (2) | line_item |  | page 11 line 794; consolidated cash flow Payment of lease liabilities (interest)
R617-R618 (2) | line_item |  | page 11 line 795; consolidated cash flow Finance costs paid
R619-R620 (2) | line_item |  | page 11 line 796; consolidated cash flow Net cash from financing activities [C]
R621-R622 (2) | line_item |  | page 11 line 797; consolidated cash flow Net increase/(decrease) in cash [A+B+C]
R623-R624 (2) | line_item |  | page 11 line 798; consolidated cash flow Opening balance of cash
R625-R626 (2) | line_item |  | page 11 line 799; consolidated cash flow Closing balance of cash

## 2b Non-table numbers (header/auditor/signature)
R627 | identifier/number |  | page 1 line 34
R628 | identifier/number |  | page 1 line 36
R629 | identifier/number |  | page 1 line 63
R630 | identifier/number |  | page 1 line 63
R631 | identifier/number |  | page 1 line 80
R632 | identifier/number |  | page 1 line 41
R633 | identifier/number |  | page 1 line 58
R634 | identifier/number |  | page 2 line 142
R635 | identifier/number |  | page 2 line 134
R636 | identifier/number |  | page 2 line 141
R637 | identifier/number |  | page 2 line 114
R638 | identifier/number |  | page 6 line 436
R639 | identifier/number |  | page 8 line 526
R640 | identifier/number |  | page 8 line 520
R641 | identifier/number |  | page 8 line 525
R642 | identifier/number |  | page 12 line 831

## 3 Agenda items and meeting times
R667 | agenda item b (extract publication) | | p1 l58; R668 website publication
R689 | agenda scope items a and b only | | no AR/AGM/dividend/director item
R688 | MISMATCH_NOTE | FOOTNOTE_UNRESOLVED | item b heading says Audited, body Un-audited
R629,R630 | board start/end time | | p1 l63
R669-R671 | dates letter/meeting/period

## 4 Annexures / director profiles
None present in filing (no annexure, no director profile rows). Segment note R702,R718.

## 5 Auditor report paragraphs
R690 | auditor_para | | standalone scope limit
R691 | auditor_para | | standalone no audit opinion
R692 | auditor_para | | standalone unmodified conclusion; no EoM/Going Concern language in structured file
R704 | auditor_para | | consol scope limit
R705 | auditor_para | | consol no audit opinion
R706 | auditor_para | | consol SEBI circular procedures
R707 | auditor_para | | consol unmodified conclusion
R708 | auditor_para | | consolidation perimeter 4 subs
R634,R635,R636,R637 | auditor_para | | standalone UDIN, firm reg, partner membership, SRE 2410
R639,R640,R641 | auditor_para | | consol UDIN, firm reg, partner membership
R650,R651,R652,R663 auditor entities. R672,R680 report dates (16 Oct 2026, same day as board meeting).

## 6 Entities (consolidation list)
R643 | entity |  | page 1 line 22
R644 | entity |  | page 1 line 24
R645 | entity |  | page 1 line 71
R646 | entity |  | page 1 line 76
R647 | entity |  | page 1 line 85
R648 | entity |  | page 1 line 86
R649 | entity |  | page 1 line 87
R650 | entity |  | page 2 line 89
R651 | entity |  | page 2 line 139
R652 | entity |  | page 2 line 115
R653 | entity |  | page 6 line 419
R654 | entity |  | page 6 line 426
R655 | entity |  | page 6 line 429
R656 | entity |  | page 6 line 435
R657 | entity |  | page 7 line 460
R658 | entity |  | page 7 line 487
R659 | entity | ENTITY_CHANGE_UNKNOWN(no prior) | page 8 line 506
R660 | entity | ENTITY_CHANGE_UNKNOWN(no prior) | page 8 line 507
R661 | entity | ENTITY_CHANGE_UNKNOWN(no prior) | page 8 line 508
R662 | entity | ENTITY_CHANGE_UNKNOWN(no prior) | page 8 line 509
R663 | entity |  | page 8 line 523
R664 | entity |  | page 12 line 829
R665 | entity |  | page 12 line 813
R666 | entity |  | page 12 line 819

## 7 Signature blocks
R656,R664 (CMD Om Prakash Lohia), R638,R642 DIN, R678,R685 signature date 16 Oct 2026. No clock timestamp captured; signature-before-meeting-end check not possible (flag SIGNATURE_TIME_ND).

## 8 Remaining rows
R653,R665 audit committee; R654,R666 segment; R655 sites; R657 holding company; R658 SEBI circular; R643-R649 addresses/ids; R673-R685 dates; R693-R695,R698-R699,R709-R711,R714-R715 qualifiers/units/audit status; R627,R628,R631-R633 identifiers.