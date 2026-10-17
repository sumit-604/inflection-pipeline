# A2 LEDGER: Aurum PropTech (AURUM) results Q2 FY27
Source: A1 structured extraction (R001-R1728). Row format: KEY | category | A2 flags | structured ROW IDs (count) | label | note
ids_in_structured: 1728 | ids_referenced_in_ledger: 1728 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: notes          grep_count: 34  sweep_count: 34  match: yes   (consol 17 + standalone 17; standalone note 1 OCR-garbled as "a" at fulltext L941, found by manual sweep)
category: line_items     grep_count: 354  sweep_count: 354  match: yes   (distinct page/line/item groups over 9 tables; 1381 table cells carry a column label)
category: zero_standing  grep_count: 201  sweep_count: 201  match: yes   (cells; 93 line items carry a nil cell; 21 nil in all periods)
category: agenda_items   grep_count: 14  sweep_count: 14  match: yes   (board letter has ONE agenda item, results approval; plus times)
category: auditor_paras  grep_count: 11  sweep_count: 11  match: yes   (consol 6 incl signature block, standalone 5 of which para 2 has no structured row (AP-S2 listed); no Emphasis of Matter or Going Concern paragraph present)
category: entities       grep_count: 16  sweep_count: 16  match: yes   (16 Sr rows in auditor table; Sr10 and Sr15 both Locon = one ID R1571; 15 IDs. Note 2 lists 15 entities (6 with ENTITY rows R1580-R1585, 9 without): MS01-MS09)
category: signature      grep_count: 10  sweep_count: 10  match: yes
gate_a2: pass
=== END COUNT TEST ===

Doctype is results: turn, question and slide categories not applicable. Prior ledger not available: ENTITY_CHANGE flags come from in-document statements only.
Observations (no interpretation): HelloWorld Living Pvt Ltd is in consolidated note 2 (wef Dec 31 2025) but NOT in auditor para 4 entity list. PropTiger effective date Sep 26 2025 (note 2) vs Sep 25 2025 (auditor list, note 6). UDINs OCR-illegible (R051, R099). Locon control date Sep 29 2026, one day before period end.


## note
N-C1 | note | - | R1637,R1698 (2) | Consolidated note 1 (lines 525-525)
N-C2 | note | ENTITY_CHANGE,OCR_VERIFY | R1580-R1585,R1638-R1639,R1699 (9) | Consolidated note 2 (lines 528-542)
N-C3 | note | RESTATED(cons/stand pair) | R054-R066,R1640-R1641,R1700 (16) | Consolidated note 3 (lines 545-555)
N-C4 | note | RESTATED(cons/stand pair),FORWARD_LOOKING | R067-R069,R1586,R1609,R1642-R1643,R1701 (8) | Consolidated note 4 (lines 558-563)
N-C5 | note | RESTATED(cons/stand pair),FORWARD_LOOKING | R1587,R1610 (2) | Consolidated note 5 (lines 567-570)
N-C6 | note | RESTATED(cons/stand pair) | R070-R073,R1644-R1645,R1702 (7) | Consolidated note 6 (lines 573-581)
N-C7 | note | RESTATED(cons/stand pair),FORWARD_LOOKING | R074-R078,R1611-R1612,R1646-R1648,R1703 (11) | Consolidated note 7 (lines 583-588)
N-C8 | note | - | R079,R1649 (2) | Consolidated note 8 (lines 591-592)
N-C9 | note | - | R080-R083 (4) | Consolidated note 9 (lines 594-596)
N-C10 | note | RESTATED(cons/stand pair) | R084-R086,R1650 (4) | Consolidated note 10 (lines 599-599)
N-C11 | note | FORWARD_LOOKING | R087-R088,R1613 (3) | Consolidated note 11 (lines 602-603)
N-C12 | note | - | R089-R090 (2) | Consolidated note 12 (lines 606-606)
N-C13 | note | RESTATED(cons/stand pair) | R091,R1588-R1589,R1651-R1652 (5) | Consolidated note 13 (lines 608-609)
N-C14 | note | - | R092-R095,R1653-R1654,R1705 (7) | Consolidated note 14 (lines 625-627)
N-C15 | note | - | R1706 (1) | Consolidated note 15 (lines 664-664)
N-C16 | note | - | R1707 (1) | Consolidated note 16 (lines 665-665)
N-C17 | note | - | R1708 (1) | Consolidated note 17 (lines 666-666)
N-S1 | note | - | R1658,R1718 (2) | Standalone note 1 (lines 941-941)
N-S2 | note | - | R1719 (1) | Standalone note 2 (lines 943-943)
N-S3 | note | RESTATED(cons/stand pair) | R101-R115,R1659-R1660,R1720 (18) | Standalone note 3 (lines 945-956)
N-S4 | note | RESTATED(cons/stand pair),FORWARD_LOOKING | R116-R118,R1594,R1614,R1661-R1662,R1721 (8) | Standalone note 4 (lines 959-966)
N-S5 | note | RESTATED(cons/stand pair),FORWARD_LOOKING | R119-R132,R1595,R1615,R1663-R1664 (18) | Standalone note 5 (lines 968-974)
N-S6 | note | RESTATED(cons/stand pair) | R133-R136,R1665-R1666,R1722 (7) | Standalone note 6 (lines 976-985)
N-S7 | note | RESTATED(cons/stand pair),FORWARD_LOOKING | R137-R141,R1616-R1617,R1667-R1669,R1723 (11) | Standalone note 7 (lines 987-992)
N-S8 | note | - | R142-R143,R1670 (3) | Standalone note 8 (lines 996-998)
N-S9 | note | - | R144-R146 (3) | Standalone note 9 (lines 1000-1000)
N-S10 | note | RESTATED(cons/stand pair) | R147-R149,R1671 (4) | Standalone note 10 (lines 1003-1003)
N-S11 | note | FORWARD_LOOKING | R150-R151,R1618 (3) | Standalone note 11 (lines 1006-1007)
N-S12 | note | - | R152-R153 (2) | Standalone note 12 (lines 1010-1010)
N-S13 | note | RESTATED(cons/stand pair) | R154,R1596-R1597,R1672-R1673 (5) | Standalone note 13 (lines 1012-1013)
N-S14 | note | - | R155-R158,R1674-R1675,R1725 (7) | Standalone note 14 (lines 1028-1030)
N-S15 | note | - | R1726 (1) | Standalone note 15 (lines 1066-1066)
N-S16 | note | - | R1727 (1) | Standalone note 16 (lines 1067-1067)
N-S17 | note | - | R1728 (1) | Standalone note 17 (lines 1068-1068)

## line_item
LI001 p8 L308 | line_item | - | R160-R165 (6) | CONSOL-RESULTS: Revenue from operations
LI002 p8 L309 | line_item | - | R166-R171 (6) | CONSOL-RESULTS: Other income
LI003 p8 L310 | line_item | - | R172-R177 (6) | CONSOL-RESULTS: Total income
LI004 p8 L312 | line_item | - | R178-R183 (6) | CONSOL-RESULTS: Employee benefit expense
LI005 p8 L313 | line_item | - | R184-R189 (6) | CONSOL-RESULTS: Finance costs
LI006 p8 L314 | line_item | - | R190-R195 (6) | CONSOL-RESULTS: Depreciation and amortization expense
LI007 p8 L315 | line_item | - | R196-R201 (6) | CONSOL-RESULTS: Other expenses
LI008 p8 L316 | line_item | - | R202-R207 (6) | CONSOL-RESULTS: Total expenses
LI009 p8 L317 | line_item | - | R208-R213 (6) | CONSOL-RESULTS: 3 Profit / (loss) before share of profit / (loss) of an associate and 
LI010 p8 L318 | line_item | - | R214-R219 (6) | CONSOL-RESULTS: 4 Share of profit / (loss) of an associate
LI011 p8 L319 | line_item | - | R220-R225 (6) | CONSOL-RESULTS: 5 Profit / (loss) before tax
LI012 p8 L321 | line_item | - | R226-R231 (6) | CONSOL-RESULTS: Income tax - current
LI013 p8 L322 | line_item | ZERO_STANDING(all periods) | R232-R237 (6) | CONSOL-RESULTS: Taxation in respect of earlier years
LI014 p8 L323 | line_item | - | R238-R243 (6) | CONSOL-RESULTS: Deferred tax charge / (benefit)
LI015 p8 L324 | line_item | - | R244-R249 (6) | CONSOL-RESULTS: Total tax
LI016 p8 L325 | line_item | - | R250-R255 (6) | CONSOL-RESULTS: 7 Profit / (loss) after tax from Continuing Operations
LI017 p8 L327 | line_item | ZERO_STANDING | R256-R261 (6) | CONSOL-RESULTS: 8 Profit / (loss) from discontinued operations
LI018 p8 L328 | line_item | ZERO_STANDING | R262-R267 (6) | CONSOL-RESULTS: Tax expense on discontinued operations
LI019 p8 L329 | line_item | ZERO_STANDING | R268-R273 (6) | CONSOL-RESULTS: Profit / (loss) after tax from Discontinued Operations
LI020 p8 L330 | line_item | - | R274-R279 (6) | CONSOL-RESULTS: 9 Net profit / (loss)
LI021 p8 L332 | line_item | - | R280-R285 (6) | CONSOL-RESULTS: (i) Items that will not be reclassified subsequently to profit or loss
LI022 p8 L333 | line_item | ZERO_STANDING | R286-R291 (6) | CONSOL-RESULTS: (ii) Income tax relating to items that will not be reclassified subseq
LI023 p8 L334 | line_item | - | R292-R297 (6) | CONSOL-RESULTS: (iii) Items that will be reclassified subsequently to profit or loss
LI024 p8 L335 | line_item | - | R298-R303 (6) | CONSOL-RESULTS: Total Comprehensive Income, net of tax
LI025 p8 L336 | line_item | - | R304-R309 (6) | CONSOL-RESULTS: 11 Total Comprehensive Income
LI026 p8 L337 | line_item | - | R310-R315 (6) | CONSOL-RESULTS: 12 Profit / (loss) from continuing operations attributable to: Equity 
LI027 p8 L338 | line_item | - | R316-R321 (6) | CONSOL-RESULTS: 12 Profit / (loss) from continuing operations attributable to: Non-con
LI028 p8 L339 | line_item | ZERO_STANDING | R322-R327 (6) | CONSOL-RESULTS: Profit / (loss) from discontinued operations attributable to: Equity s
LI029 p8 L340 | line_item | ZERO_STANDING(all periods) | R328-R333 (6) | CONSOL-RESULTS: Profit / (loss) from discontinued operations attributable to: Non-cont
LI030 p8 L341 | line_item | - | R334-R339 (6) | CONSOL-RESULTS: OCI from continuing operations attributable to: Equity shareholders of
LI031 p8 L342 | line_item | ZERO_STANDING | R340-R345 (6) | CONSOL-RESULTS: OCI from continuing operations attributable to: Non-controlling intere
LI032 p8 L343 | line_item | ZERO_STANDING(all periods) | R346-R351 (6) | CONSOL-RESULTS: OCI from discontinued operations attributable to: Equity shareholders 
LI033 p8 L344 | line_item | ZERO_STANDING(all periods) | R352-R357 (6) | CONSOL-RESULTS: OCI from discontinued operations attributable to: Non-controlling inte
LI034 p8 L345 | line_item | - | R358-R363 (6) | CONSOL-RESULTS: Total Comprehensive Income from continuing operations attributable to:
LI035 p8 L346 | line_item | - | R364-R369 (6) | CONSOL-RESULTS: Total Comprehensive Income from continuing operations attributable to:
LI036 p8 L347 | line_item | ZERO_STANDING | R370-R375 (6) | CONSOL-RESULTS: Total Comprehensive Income from discontinued operations attributable t
LI037 p8 L348 | line_item | ZERO_STANDING(all periods) | R376-R381 (6) | CONSOL-RESULTS: Total Comprehensive Income from discontinued operations attributable t
LI038 p8 L349 | line_item | - | R382-R387 (6) | CONSOL-RESULTS: 13 Paid up equity share capital
LI039 p8 L350 | line_item | - | R388-R393 (6) | CONSOL-RESULTS: 14 Reserves excluding revaluation reserves as per balance sheet
LI040 p8 L351 | line_item | - | R394-R399 (6) | CONSOL-RESULTS: 15 Earning per share of INR 5/- each (not annualized) CONTINUING OPERA
LI041 p8 L352 | line_item | - | R400-R405 (6) | CONSOL-RESULTS: 15 Earning per share CONTINUING OPERATIONS Diluted (INR)
LI042 p8 L353 | line_item | ZERO_STANDING | R406-R411 (6) | CONSOL-RESULTS: EPS DISCONTINUED OPERATIONS Basic (INR)
LI043 p8 L354 | line_item | ZERO_STANDING | R412-R417 (6) | CONSOL-RESULTS: EPS DISCONTINUED OPERATIONS Diluted (INR)
LI044 p8 L355 | line_item | - | R418-R423 (6) | CONSOL-RESULTS: EPS TOTAL Basic (INR)
LI045 p8 L356 | line_item | - | R424-R429 (6) | CONSOL-RESULTS: EPS TOTAL Diluted (INR)
LI046 p9 L367 | line_item | - | R430-R435 (6) | CONSOL-SEGMENT: 1 Segment Revenue CONTINUING OPERATIONS Rental
LI047 p9 L368 | line_item | - | R436-R441 (6) | CONSOL-SEGMENT: Segment Revenue CONTINUING OPERATIONS Distribution
LI048 p9 L369 | line_item | - | R442-R447 (6) | CONSOL-SEGMENT: Segment Revenue CONTINUING OPERATIONS Capital
LI049 p9 L370 | line_item | - | R448-R453 (6) | CONSOL-SEGMENT: Segment Revenue CONTINUING OPERATIONS Total
LI050 p9 L371 | line_item | ZERO_STANDING | R454-R459 (6) | CONSOL-SEGMENT: Segment Revenue DISCONTINUED OPERATIONS Rental
LI051 p9 L372 | line_item | - | R460-R465 (6) | CONSOL-SEGMENT: Segment Revenue Total (continuing + discontinued)
LI052 p9 L373 | line_item | - | R466-R471 (6) | CONSOL-SEGMENT: 2 Segment Results CONTINUING OPERATIONS Rental
LI053 p9 L374 | line_item | - | R472-R477 (6) | CONSOL-SEGMENT: Segment Results CONTINUING OPERATIONS Distribution
LI054 p9 L375 | line_item | - | R478-R483 (6) | CONSOL-SEGMENT: Segment Results CONTINUING OPERATIONS Capital
LI055 p9 L376 | line_item | - | R484-R489 (6) | CONSOL-SEGMENT: Segment Results CONTINUING OPERATIONS Total
LI056 p9 L377 | line_item | ZERO_STANDING | R490-R495 (6) | CONSOL-SEGMENT: Segment Results DISCONTINUED OPERATIONS Rental
LI057 p9 L378 | line_item | - | R496-R501 (6) | CONSOL-SEGMENT: Segment Results Total (continuing + discontinued)
LI058 p9 L379 | line_item | - | R502-R507 (6) | CONSOL-SEGMENT: Finance cost
LI059 p9 L380 | line_item | - | R508-R513 (6) | CONSOL-SEGMENT: Other un-allocable expenditure - net of other income
LI060 p9 L381 | line_item | - | R514-R519 (6) | CONSOL-SEGMENT: Profit / (loss) before tax
LI061 p9 L383 | line_item | - | R520-R525 (6) | CONSOL-SEGMENT: 3 Segment Assets CONTINUING OPERATIONS Rental
LI062 p9 L384 | line_item | - | R526-R531 (6) | CONSOL-SEGMENT: Segment Assets CONTINUING OPERATIONS Distribution
LI063 p9 L385 | line_item | - | R532-R537 (6) | CONSOL-SEGMENT: Segment Assets CONTINUING OPERATIONS Capital
LI064 p9 L386 | line_item | - | R538-R543 (6) | CONSOL-SEGMENT: Segment Assets CONTINUING OPERATIONS Unallocable Corporate assets
LI065 p9 L387 | line_item | - | R544-R549 (6) | CONSOL-SEGMENT: Segment Assets DISCONTINUED OPERATIONS Rental
LI066 p9 L388 | line_item | - | R550-R555 (6) | CONSOL-SEGMENT: Total Assets
LI067 p9 L389 | line_item | - | R556-R561 (6) | CONSOL-SEGMENT: 4 Segment Liabilities CONTINUING OPERATIONS Rental
LI068 p9 L390 | line_item | - | R562-R567 (6) | CONSOL-SEGMENT: Segment Liabilities CONTINUING OPERATIONS Distribution
LI069 p9 L391 | line_item | - | R568-R573 (6) | CONSOL-SEGMENT: Segment Liabilities CONTINUING OPERATIONS Capital
LI070 p9 L392 | line_item | - | R574-R579 (6) | CONSOL-SEGMENT: Segment Liabilities CONTINUING OPERATIONS Unallocable Corporate liabil
LI071 p9 L393 | line_item | - | R580-R585 (6) | CONSOL-SEGMENT: Segment Liabilities DISCONTINUED OPERATIONS Rental
LI072 p9 L394 | line_item | - | R586-R591 (6) | CONSOL-SEGMENT: Total Liabilities
LI073 p10 L403 | line_item | - | R592-R593 (2) | CONSOL-BS: Property, plant and equipment
LI074 p10 L404 | line_item | - | R594-R595 (2) | CONSOL-BS: Right of use assets
LI075 p10 L405 | line_item | - | R596-R597 (2) | CONSOL-BS: Goodwill on consolidation
LI076 p10 L406 | line_item | - | R598-R599 (2) | CONSOL-BS: Intangible assets
LI077 p10 L407 | line_item | - | R600-R601 (2) | CONSOL-BS: Capital work in progress
LI078 p10 L408 | line_item | - | R602-R603 (2) | CONSOL-BS: Intangible assets under development
LI079 p10 L409 | line_item | - | R604-R605 (2) | CONSOL-BS: Financial assets - Investments (non-current)
LI080 p10 L410 | line_item | - | R606-R607 (2) | CONSOL-BS: Financial assets - Other financial assets (non-current)
LI081 p10 L411 | line_item | ZERO_STANDING | R608-R609 (2) | CONSOL-BS: Deferred tax assets (net)
LI082 p10 L412 | line_item | - | R610-R611 (2) | CONSOL-BS: Income tax assets (net) (non-current)
LI083 p10 L413 | line_item | - | R612-R613 (2) | CONSOL-BS: Other non-current assets
LI084 p10 L414 | line_item | - | R614-R615 (2) | CONSOL-BS: Total non-current assets
LI085 p10 L416 | line_item | ZERO_STANDING | R616-R617 (2) | CONSOL-BS: Inventories
LI086 p10 L417 | line_item | - | R618-R619 (2) | CONSOL-BS: Financial assets - Investments (current)
LI087 p10 L418 | line_item | - | R620-R621 (2) | CONSOL-BS: Financial assets - Trade receivables
LI088 p10 L419 | line_item | - | R622-R623 (2) | CONSOL-BS: Financial assets - Cash and cash equivalents
LI089 p10 L420 | line_item | - | R624-R625 (2) | CONSOL-BS: Financial assets - Bank balances other than cash and cash equivalents
LI090 p10 L421 | line_item | - | R626-R627 (2) | CONSOL-BS: Financial assets - Loans
LI091 p10 L422 | line_item | - | R628-R629 (2) | CONSOL-BS: Financial assets - Other financial assets (current)
LI092 p10 L423 | line_item | - | R630-R631 (2) | CONSOL-BS: Income tax assets (net) (current)
LI093 p10 L424 | line_item | - | R632-R633 (2) | CONSOL-BS: Other current assets
LI094 p10 L425 | line_item | - | R634-R635 (2) | CONSOL-BS: Total current assets
LI095 p10 L426 | line_item | - | R636-R637 (2) | CONSOL-BS: Assets of Disposal group - classified as held for sale
LI096 p10 L427 | line_item | - | R638-R639 (2) | CONSOL-BS: Total Assets
LI097 p10 L429 | line_item | - | R640-R641 (2) | CONSOL-BS: Equity share capital
LI098 p10 L430 | line_item | - | R642-R643 (2) | CONSOL-BS: Other equity
LI099 p10 L431 | line_item | - | R644-R645 (2) | CONSOL-BS: Total equity attributable to equity holders of the company
LI100 p10 L432 | line_item | - | R646-R647 (2) | CONSOL-BS: Non-controlling interest
LI101 p10 L433 | line_item | - | R648-R649 (2) | CONSOL-BS: Total equity
LI102 p10 L434 | line_item | - | R650-R651 (2) | CONSOL-BS: Non-current liabilities - Financial liabilities Borrowings
LI103 p10 L435 | line_item | - | R652-R653 (2) | CONSOL-BS: Non-current liabilities - Lease liabilities
LI104 p10 L436 | line_item | - | R654-R655 (2) | CONSOL-BS: Non-current liabilities - Other financial liabilities
LI105 p10 L437 | line_item | ZERO_STANDING | R656-R657 (2) | CONSOL-BS: Deferred tax liabilities (net)
LI106 p10 L438 | line_item | - | R658-R659 (2) | CONSOL-BS: Provisions (non-current)
LI107 p10 L439 | line_item | - | R660-R661 (2) | CONSOL-BS: Total non-current liabilities
LI108 p10 L440 | line_item | - | R662-R663 (2) | CONSOL-BS: Current liabilities - Financial liabilities Borrowings
LI109 p10 L441 | line_item | - | R664-R665 (2) | CONSOL-BS: Current liabilities - Lease liabilities
LI110 p10 L442 | line_item | - | R666-R667 (2) | CONSOL-BS: Trade payables a) Dues of micro and small enterprises
LI111 p10 L443 | line_item | - | R668-R669 (2) | CONSOL-BS: Trade payables b) Dues of creditors other than micro and small enterpr
LI112 p10 L444 | line_item | - | R670-R671 (2) | CONSOL-BS: Current liabilities - Other financial liabilities
LI113 p10 L445 | line_item | - | R672-R673 (2) | CONSOL-BS: Provisions (current)
LI114 p10 L446 | line_item | - | R674-R675 (2) | CONSOL-BS: Current tax liabilities
LI115 p10 L447 | line_item | - | R676-R677 (2) | CONSOL-BS: Other current liabilities
LI116 p10 L448 | line_item | - | R678-R679 (2) | CONSOL-BS: Total current liabilities
LI117 p10 L449 | line_item | - | R680-R681 (2) | CONSOL-BS: Total liabilities
LI118 p10 L450 | line_item | - | R682-R683 (2) | CONSOL-BS: Liabilities directly associated with Assets of Disposal group - classi
LI119 p10 L451 | line_item | - | R684-R685 (2) | CONSOL-BS: Total equity and liabilities
LI120 p11 L460 | line_item | - | R686-R688 (3) | CONSOL-CF: Profit/ (Loss) before tax
LI121 p11 L462 | line_item | - | R689-R691 (3) | CONSOL-CF: Depreciation and amortization expense
LI122 p11 L463 | line_item | - | R692-R694 (3) | CONSOL-CF: Share based payments
LI123 p11 L464 | line_item | - | R695-R697 (3) | CONSOL-CF: Finance costs
LI124 p11 L465 | line_item | ZERO_STANDING | R698-R700 (3) | CONSOL-CF: Provision for doubtful debts
LI125 p11 L466 | line_item | - | R701-R703 (3) | CONSOL-CF: Interest income on deposits and debentures
LI126 p11 L467 | line_item | - | R704-R706 (3) | CONSOL-CF: Interest income on loans
LI127 p11 L468 | line_item | - | R707-R709 (3) | CONSOL-CF: Interest income on security deposits
LI128 p11 L469 | line_item | - | R710-R712 (3) | CONSOL-CF: Interest on income tax refund
LI129 p11 L470 | line_item | - | R713-R715 (3) | CONSOL-CF: Gain on lease terminated and lease liability no longer required writte
LI130 p11 L471 | line_item | - | R716-R718 (3) | CONSOL-CF: Profit on sale and revaluation of current investments (mutual funds)
LI131 p11 L472 | line_item | - | R719-R721 (3) | CONSOL-CF: (Gain) / loss on sale of property, plant and equipment
LI132 p11 L473 | line_item | - | R722-R724 (3) | CONSOL-CF: Reversal of provisions
LI133 p11 L474 | line_item | - | R725-R727 (3) | CONSOL-CF: Gain on foreign currency transactions and translations
LI134 p11 L475 | line_item | - | R728-R730 (3) | CONSOL-CF: Operating profit before working capital changes
LI135 p11 L477 | line_item | - | R731-R733 (3) | CONSOL-CF: (Increase) / decrease in trade receivables
LI136 p11 L478 | line_item | - | R734-R736 (3) | CONSOL-CF: Decrease in non-current and current financial assets
LI137 p11 L479 | line_item | - | R737-R739 (3) | CONSOL-CF: (Increase) in non-current and current other assets
LI138 p11 L480 | line_item | - | R740-R742 (3) | CONSOL-CF: Increase in non-current and current other financial liabilities
LI139 p11 L481 | line_item | - | R743-R745 (3) | CONSOL-CF: Increase / (Decrease) in trade payables
LI140 p11 L482 | line_item | - | R746-R748 (3) | CONSOL-CF: Increase / (Decrease) in non-current and current other current liabili
LI141 p11 L483 | line_item | - | R749-R751 (3) | CONSOL-CF: Cash generated from operations
LI142 p11 L484 | line_item | - | R752-R754 (3) | CONSOL-CF: Income tax refund/ (paid) (net)
LI143 p11 L485 | line_item | - | R755-R757 (3) | CONSOL-CF: Interest on income tax refund
LI144 p11 L486 | line_item | - | R758-R760 (3) | CONSOL-CF: Net cash flow generated from operating activities (A)
LI145 p11 L488 | line_item | - | R761-R763 (3) | CONSOL-CF: Payment for property, plant and equipment, intangible assets and intan
LI146 p11 L489 | line_item | ZERO_STANDING | R764-R766 (3) | CONSOL-CF: Proceeds from sale of property, plant and equipment
LI147 p11 L490 | line_item | ZERO_STANDING | R767-R769 (3) | CONSOL-CF: Payment for acquisition of subsidiary companies
LI148 p11 L491 | line_item | - | R770-R772 (3) | CONSOL-CF: Net Investment/ (proceeds) in financial assets - investments
LI149 p11 L492 | line_item | - | R773-R775 (3) | CONSOL-CF: Net Investment/ (proceeds) in financial assets - deposits
LI150 p11 L493 | line_item | - | R776-R778 (3) | CONSOL-CF: Interest received
LI151 p11 L494 | line_item | - | R779-R781 (3) | CONSOL-CF: Net cash flow used in investing activities (B)
LI152 p11 L496 | line_item | - | R782-R784 (3) | CONSOL-CF: Proceeds from issue of equity shares (net)
LI153 p11 L497 | line_item | ZERO_STANDING | R785-R787 (3) | CONSOL-CF: Proceeds from issue of equity shares by subsidiary
LI154 p11 L498 | line_item | ZERO_STANDING | R788-R790 (3) | CONSOL-CF: Repayment of loan - related parties
LI155 p11 L499 | line_item | ZERO_STANDING(all periods) | R791-R793 (3) | CONSOL-CF: Proceeds from borrowings- banks
LI156 p11 L500 | line_item | - | R794-R796 (3) | CONSOL-CF: Repayment of borrowings - banks
LI157 p11 L501 | line_item | - | R797-R799 (3) | CONSOL-CF: Repayment of lease liability, net of interest
LI158 p11 L502 | line_item | - | R800-R802 (3) | CONSOL-CF: Interest and other finance charges paid
LI159 p11 L503 | line_item | - | R803-R805 (3) | CONSOL-CF: Net cash flow generated from financing activities (C)
LI160 p11 L505 | line_item | - | R806-R808 (3) | CONSOL-CF: Cash flow from operating activities
LI161 p11 L506 | line_item | - | R809-R811 (3) | CONSOL-CF: Cash flow from investing activities
LI162 p11 L507 | line_item | - | R812-R814 (3) | CONSOL-CF: Cash flow from financing activities
LI163 p11 L508 | line_item | - | R815-R817 (3) | CONSOL-CF: Net cash flow from discontinued operations (D)
LI164 p11 L509 | line_item | - | R818-R820 (3) | CONSOL-CF: Net increase/ (decrease) in cash and cash equivalents (A+B+C+D)
LI165 p11 L510 | line_item | - | R821-R823 (3) | CONSOL-CF: Cash and cash equivalents at the beginning of the period / year
LI166 p11 L511 | line_item | - | R824-R826 (3) | CONSOL-CF: Cash and cash equivalents on acquisition of subsidiary
LI167 p11 L512 | line_item | ZERO_STANDING | R827-R829 (3) | CONSOL-CF: Cash and cash equivalents on subsidiaries derecognition
LI168 p11 L513 | line_item | - | R830-R832 (3) | CONSOL-CF: Cash and cash equivalents at the end of the period / year
LI169 p11 L515 | line_item | - | R833-R835 (3) | CONSOL-CF: Balances with banks
LI170 p11 L516 | line_item | - | R836-R838 (3) | CONSOL-CF: Fixed deposit with orginal maturity for less than 3 months
LI171 p11 L517 | line_item | - | R839-R841 (3) | CONSOL-CF: Total cash and cash equivalents at end of the period / year
LI172 p13 L630 | line_item | ZERO_STANDING | R842-R847 (6) | CONSOL-DISC/ASSETS: Revenue from operations
LI173 p13 L631 | line_item | ZERO_STANDING | R848-R853 (6) | CONSOL-DISC/ASSETS: Other income
LI174 p13 L632 | line_item | ZERO_STANDING | R854-R859 (6) | CONSOL-DISC/ASSETS: Total income
LI175 p13 L633 | line_item | ZERO_STANDING(all periods) | R860-R865 (6) | CONSOL-DISC/ASSETS: Employee benefit expense
LI176 p13 L634 | line_item | ZERO_STANDING | R866-R871 (6) | CONSOL-DISC/ASSETS: Finance costs
LI177 p13 L635 | line_item | ZERO_STANDING | R872-R877 (6) | CONSOL-DISC/ASSETS: Depreciation and amortization expense
LI178 p13 L636 | line_item | ZERO_STANDING | R878-R883 (6) | CONSOL-DISC/ASSETS: Other expenses
LI179 p13 L637 | line_item | ZERO_STANDING | R884-R889 (6) | CONSOL-DISC/ASSETS: Total expenses
LI180 p13 L638 | line_item | ZERO_STANDING | R890-R895 (6) | CONSOL-DISC/ASSETS: Profit / (loss) before tax
LI181 p13 L639 | line_item | ZERO_STANDING | R896-R901 (6) | CONSOL-DISC/ASSETS: Income tax - current
LI182 p13 L640 | line_item | ZERO_STANDING(all periods) | R902-R907 (6) | CONSOL-DISC/ASSETS: Taxation in respect of earlier years
LI183 p13 L641 | line_item | ZERO_STANDING | R908-R913 (6) | CONSOL-DISC/ASSETS: Deferred tax charge / (benefit)
LI184 p13 L642 | line_item | ZERO_STANDING | R914-R919 (6) | CONSOL-DISC/ASSETS: Total tax
LI185 p13 L643 | line_item | ZERO_STANDING | R920-R925 (6) | CONSOL-DISC/ASSETS: Profit / (loss) after tax
LI186 p13 L644 | line_item | ZERO_STANDING(all periods) | R926-R931 (6) | CONSOL-DISC/ASSETS: OCI (i) Items that will not be reclassified subsequently to profit or 
LI187 p13 L645 | line_item | ZERO_STANDING(all periods) | R932-R937 (6) | CONSOL-DISC/ASSETS: OCI (ii) Income tax relating to items that will not be reclassified
LI188 p13 L646 | line_item | ZERO_STANDING(all periods) | R938-R943 (6) | CONSOL-DISC/ASSETS: Total Other Comprehensive Income, net of tax
LI189 p13 L647 | line_item | ZERO_STANDING | R944-R949 (6) | CONSOL-DISC/ASSETS: Total Comprehensive Income
LI190 p13 L648 | line_item | ZERO_STANDING | R950-R955 (6) | CONSOL-DISC/ASSETS: Earning per share of INR 5/- each (not annualized) Basic (INR)
LI191 p13 L649 | line_item | ZERO_STANDING | R956-R961 (6) | CONSOL-DISC/ASSETS: Earning per share of INR 5/- each (not annualized) Diluted (INR)
LI192 p13 L652 | line_item | ZERO_STANDING | R962-R963 (2) | CONSOL-DISC/ASSETS: Non - current assets
LI193 p13 L653 | line_item | - | R964-R965 (2) | CONSOL-DISC/ASSETS: Current assets
LI194 p13 L654 | line_item | - | R966-R967 (2) | CONSOL-DISC/ASSETS: Total assets
LI195 p13 L655 | line_item | - | R968-R969 (2) | CONSOL-DISC/ASSETS: Non - current liabilities
LI196 p13 L656 | line_item | - | R970-R971 (2) | CONSOL-DISC/ASSETS: Current liabilities
LI197 p13 L657 | line_item | - | R972-R973 (2) | CONSOL-DISC/ASSETS: Total liabilities
LI198 p13 L660 | line_item | - | R974-R976 (3) | CONSOL-DISC/ASSETS: Cash flow from operating activities
LI199 p13 L661 | line_item | - | R977-R979 (3) | CONSOL-DISC/ASSETS: Cash flow from investing activities
LI200 p13 L662 | line_item | - | R980-R982 (3) | CONSOL-DISC/ASSETS: Cash flow from financing activities
LI201 p13 L663 | line_item | - | R983-R985 (3) | CONSOL-DISC/ASSETS: Total
LI202 p16 L783 | line_item | - | R986-R991 (6) | STAND-RESULTS: Revenue from operations
LI203 p16 L784 | line_item | - | R992-R997 (6) | STAND-RESULTS: Other income
LI204 p16 L785 | line_item | - | R998-R1003 (6) | STAND-RESULTS: Total income
LI205 p16 L787 | line_item | - | R1004-R1009 (6) | STAND-RESULTS: Employee benefit expense
LI206 p16 L788 | line_item | - | R1010-R1015 (6) | STAND-RESULTS: Finance costs
LI207 p16 L789 | line_item | - | R1016-R1021 (6) | STAND-RESULTS: Depreciation and amortization expense
LI208 p16 L790 | line_item | - | R1022-R1027 (6) | STAND-RESULTS: Other expenses
LI209 p16 L791 | line_item | - | R1028-R1033 (6) | STAND-RESULTS: Total expenses
LI210 p16 L792 | line_item | - | R1034-R1039 (6) | STAND-RESULTS: 3 Profit before tax
LI211 p16 L793 | line_item | ZERO_STANDING | R1040-R1045 (6) | STAND-RESULTS: 4 Tax expenses Income tax - current
LI212 p16 L794 | line_item | - | R1046-R1051 (6) | STAND-RESULTS: Tax expenses Deferred tax charge / (benefit)
LI213 p16 L795 | line_item | - | R1052-R1057 (6) | STAND-RESULTS: Total tax
LI214 p16 L796 | line_item | - | R1058-R1063 (6) | STAND-RESULTS: 5 Profit after tax from Continuing Operations
LI215 p16 L798 | line_item | ZERO_STANDING | R1064-R1069 (6) | STAND-RESULTS: 6 Profit / (loss) from discontinued operations
LI216 p16 L799 | line_item | ZERO_STANDING | R1070-R1075 (6) | STAND-RESULTS: Tax of discontinued operations
LI217 p16 L800 | line_item | ZERO_STANDING | R1076-R1081 (6) | STAND-RESULTS: Profit / (loss) after tax from Discontinued Operations
LI218 p16 L801 | line_item | - | R1082-R1087 (6) | STAND-RESULTS: 7 Net Profit
LI219 p16 L802 | line_item | ZERO_STANDING | R1088-R1093 (6) | STAND-RESULTS: 8 Other Comprehensive Income CONTINUING OPERATIONS (i) Items that will
LI220 p16 L803 | line_item | ZERO_STANDING | R1094-R1099 (6) | STAND-RESULTS: (ii) Income tax relating to items that will not be reclassified subseq
LI221 p16 L804 | line_item | ZERO_STANDING | R1100-R1105 (6) | STAND-RESULTS: Total Other Comprehensive Income, net of tax
LI222 p16 L805 | line_item | - | R1106-R1111 (6) | STAND-RESULTS: 9 Total Comprehensive Income
LI223 p16 L806 | line_item | - | R1112-R1117 (6) | STAND-RESULTS: 10 Paid up equity share capital (Face value of INR 5/- each)
LI224 p16 L807 | line_item | - | R1118-R1123 (6) | STAND-RESULTS: 11 Reserves excluding revaluation reserves as per Balance Sheet
LI225 p16 L808 | line_item | - | R1124-R1129 (6) | STAND-RESULTS: 12 Earnings per share of INR 5/- each (not annualized) CONTINUING OPER
LI226 p16 L809 | line_item | - | R1130-R1135 (6) | STAND-RESULTS: EPS CONTINUING OPERATIONS Diluted (INR)
LI227 p16 L810 | line_item | ZERO_STANDING | R1136-R1141 (6) | STAND-RESULTS: EPS DISCONTINUED OPERATIONS Basic (INR)
LI228 p16 L811 | line_item | ZERO_STANDING | R1142-R1147 (6) | STAND-RESULTS: EPS DISCONTINUED OPERATIONS Diluted (INR)
LI229 p16 L812 | line_item | - | R1148-R1153 (6) | STAND-RESULTS: EPS TOTAL Basic (INR)
LI230 p16 L813 | line_item | - | R1154-R1159 (6) | STAND-RESULTS: EPS TOTAL Diluted (INR)
LI231 p17 L822 | line_item | - | R1160-R1161 (2) | STAND-BS: Property, plant and equipment
LI232 p17 L823 | line_item | - | R1162-R1163 (2) | STAND-BS: Right of use assets
LI233 p17 L824 | line_item | - | R1164-R1165 (2) | STAND-BS: Intangible assets
LI234 p17 L825 | line_item | ZERO_STANDING(all periods) | R1166-R1167 (2) | STAND-BS: Capital work-in-progress
LI235 p17 L826 | line_item | - | R1168-R1169 (2) | STAND-BS: Intangible assets under development
LI236 p17 L827 | line_item | - | R1170-R1171 (2) | STAND-BS: Financial assets - Investments (non-current)
LI237 p17 L828 | line_item | - | R1172-R1173 (2) | STAND-BS: Financial assets - Loans (non-current)
LI238 p17 L829 | line_item | - | R1174-R1175 (2) | STAND-BS: Financial assets - Other financial assets (non-current)
LI239 p17 L830 | line_item | - | R1176-R1177 (2) | STAND-BS: Deferred tax assets (net)
LI240 p17 L831 | line_item | ZERO_STANDING(all periods) | R1178-R1179 (2) | STAND-BS: Other non-current assets
LI241 p17 L832 | line_item | - | R1180-R1181 (2) | STAND-BS: Total non-current assets
LI242 p17 L834 | line_item | - | R1182-R1183 (2) | STAND-BS: Financial assets - Investments (current)
LI243 p17 L835 | line_item | - | R1184-R1185 (2) | STAND-BS: Financial assets - Trade receivables
LI244 p17 L836 | line_item | - | R1186-R1187 (2) | STAND-BS: Financial assets - Cash and cash equivalents
LI245 p17 L837 | line_item | - | R1188-R1189 (2) | STAND-BS: Financial assets - Bank balances other than cash and cash equivalents
LI246 p17 L838 | line_item | - | R1190-R1191 (2) | STAND-BS: Financial assets - Loans (current)
LI247 p17 L839 | line_item | - | R1192-R1193 (2) | STAND-BS: Financial assets - Other financial assets (current)
LI248 p17 L840 | line_item | ZERO_STANDING(all periods) | R1194-R1195 (2) | STAND-BS: Income tax assets (net)
LI249 p17 L841 | line_item | - | R1196-R1197 (2) | STAND-BS: Other current assets
LI250 p17 L842 | line_item | - | R1198-R1199 (2) | STAND-BS: Total current assets
LI251 p17 L843 | line_item | - | R1200-R1201 (2) | STAND-BS: Assets of Disposal group - classified as held for sale
LI252 p17 L844 | line_item | - | R1202-R1203 (2) | STAND-BS: Total Assets
LI253 p17 L846 | line_item | - | R1204-R1205 (2) | STAND-BS: Equity share capital
LI254 p17 L847 | line_item | - | R1206-R1207 (2) | STAND-BS: Other equity
LI255 p17 L848 | line_item | - | R1208-R1209 (2) | STAND-BS: Total equity
LI256 p17 L849 | line_item | ZERO_STANDING(all periods) | R1210-R1211 (2) | STAND-BS: Non-current liabilities - Financial liabilities Borrowings
LI257 p17 L850 | line_item | - | R1212-R1213 (2) | STAND-BS: Non-current liabilities - Lease liabilities
LI258 p17 L851 | line_item | ZERO_STANDING | R1214-R1215 (2) | STAND-BS: Non-current liabilities - Other financial liabilities
LI259 p17 L852 | line_item | - | R1216-R1217 (2) | STAND-BS: Provisions (non-current)
LI260 p17 L853 | line_item | ZERO_STANDING(all periods) | R1218-R1219 (2) | STAND-BS: Other non-current liabilities
LI261 p17 L854 | line_item | - | R1220-R1221 (2) | STAND-BS: Total non-current liabilities
LI262 p17 L855 | line_item | ZERO_STANDING | R1222-R1223 (2) | STAND-BS: Current liabilities - Financial liabilities Borrowings
LI263 p17 L856 | line_item | - | R1224-R1225 (2) | STAND-BS: Current liabilities - Lease liabilities
LI264 p17 L857 | line_item | ZERO_STANDING(all periods) | R1226-R1227 (2) | STAND-BS: Trade payables a) Dues of micro and small enterprises
LI265 p17 L858 | line_item | - | R1228-R1229 (2) | STAND-BS: Trade payables b) Dues of creditors other than micro and small enterpr
LI266 p17 L859 | line_item | - | R1230-R1231 (2) | STAND-BS: Current liabilities - Other financial liabilities
LI267 p17 L860 | line_item | - | R1232-R1233 (2) | STAND-BS: Current tax liabilities (net)
LI268 p17 L861 | line_item | - | R1234-R1235 (2) | STAND-BS: Other current liabilities
LI269 p17 L862 | line_item | - | R1236-R1237 (2) | STAND-BS: Total current liabilities
LI270 p17 L863 | line_item | - | R1238-R1239 (2) | STAND-BS: Total liabilities
LI271 p17 L864 | line_item | - | R1240-R1241 (2) | STAND-BS: Liabilities directly associated with Assets of Disposal group - classi
LI272 p17 L865 | line_item | - | R1242-R1243 (2) | STAND-BS: Total Equity and Liabilities
LI273 p18 L874 | line_item | - | R1244-R1246 (3) | STAND-CF: Profit before tax
LI274 p18 L876 | line_item | - | R1247-R1249 (3) | STAND-CF: Depreciation and amortization expense
LI275 p18 L877 | line_item | - | R1250-R1252 (3) | STAND-CF: Share based payments
LI276 p18 L878 | line_item | - | R1253-R1255 (3) | STAND-CF: Finance costs
LI277 p18 L879 | line_item | ZERO_STANDING | R1256-R1258 (3) | STAND-CF: Provision for doubtful debts
LI278 p18 L880 | line_item | - | R1259-R1261 (3) | STAND-CF: Interest income on deposits
LI279 p18 L881 | line_item | - | R1262-R1264 (3) | STAND-CF: Interest income on loans
LI280 p18 L882 | line_item | - | R1265-R1267 (3) | STAND-CF: Interest income on debentures
LI281 p18 L883 | line_item | - | R1268-R1270 (3) | STAND-CF: Interest income on security deposits
LI282 p18 L884 | line_item | ZERO_STANDING | R1271-R1273 (3) | STAND-CF: Interest Income - Others
LI283 p18 L885 | line_item | ZERO_STANDING | R1274-R1276 (3) | STAND-CF: Interest income on income tax refund
LI284 p18 L886 | line_item | - | R1277-R1279 (3) | STAND-CF: Income on investments measured at fair value
LI285 p18 L887 | line_item | - | R1280-R1282 (3) | STAND-CF: Profit on sale of current investments ( mutual funds )
LI286 p18 L888 | line_item | ZERO_STANDING | R1283-R1285 (3) | STAND-CF: Reversal of provisions
LI287 p18 L889 | line_item | - | R1286-R1288 (3) | STAND-CF: Gain on foreign currency transactions and translations
LI288 p18 L890 | line_item | - | R1289-R1291 (3) | STAND-CF: Operating loss before working capital changes
LI289 p18 L892 | line_item | - | R1292-R1294 (3) | STAND-CF: Decrease / (increase) in trade receivables
LI290 p18 L893 | line_item | - | R1295-R1297 (3) | STAND-CF: Decrease / (increase) in non current and current financial assets
LI291 p18 L894 | line_item | - | R1298-R1300 (3) | STAND-CF: Decrease / (increase) in non-current and current other assets
LI292 p18 L895 | line_item | - | R1301-R1303 (3) | STAND-CF: Increase / (decrease) in non-current and current other financial liabi
LI293 p18 L896 | line_item | - | R1304-R1306 (3) | STAND-CF: Increase / (decrease) in trade payables
LI294 p18 L897 | line_item | - | R1307-R1309 (3) | STAND-CF: Increase / (decrease) in non-current and current other current liabili
LI295 p18 L898 | line_item | - | R1310-R1312 (3) | STAND-CF: Cash generated from / (used in) operations
LI296 p18 L899 | line_item | - | R1313-R1315 (3) | STAND-CF: Income tax ( paid ) / refund (net)
LI297 p18 L900 | line_item | ZERO_STANDING | R1316-R1318 (3) | STAND-CF: Interest income on income tax refund
LI298 p18 L901 | line_item | - | R1319-R1321 (3) | STAND-CF: Net cash flow generated from / (used in) operating activities (A)
LI299 p18 L903 | line_item | - | R1322-R1324 (3) | STAND-CF: (Payment for purchase) / proceeds from sale of property, plant and equ
LI300 p18 L904 | line_item | ZERO_STANDING | R1325-R1327 (3) | STAND-CF: Payment for intangible assets under development
LI301 p18 L905 | line_item | - | R1328-R1330 (3) | STAND-CF: Payment for investment in subsidiary companies
LI302 p18 L906 | line_item | ZERO_STANDING | R1331-R1333 (3) | STAND-CF: (Investment in) / proceeds from financial assets - non-current investm
LI303 p18 L907 | line_item | - | R1334-R1336 (3) | STAND-CF: Investment in financial assets - current investments
LI304 p18 L908 | line_item | - | R1337-R1339 (3) | STAND-CF: Proceeds from financial assets - current investments
LI305 p18 L909 | line_item | - | R1340-R1342 (3) | STAND-CF: Loan given to subsidiary companies
LI306 p18 L910 | line_item | - | R1343-R1345 (3) | STAND-CF: Loan repaid by subsidiary companies
LI307 p18 L911 | line_item | - | R1346-R1348 (3) | STAND-CF: (Investment in) / proceeds from deposits (net)
LI308 p18 L912 | line_item | - | R1349-R1351 (3) | STAND-CF: Interest received
LI309 p18 L913 | line_item | - | R1352-R1354 (3) | STAND-CF: Net cash flow generated from / (used in) investing activities (B)
LI310 p18 L915 | line_item | - | R1355-R1357 (3) | STAND-CF: Proceeds from issue of equity shares (net)
LI311 p18 L916 | line_item | ZERO_STANDING | R1358-R1360 (3) | STAND-CF: Proceeds from loan - related parties
LI312 p18 L917 | line_item | ZERO_STANDING | R1361-R1363 (3) | STAND-CF: Repayment of loan - related parties
LI313 p18 L918 | line_item | - | R1364-R1366 (3) | STAND-CF: Repayment of borrowings - bank
LI314 p18 L919 | line_item | - | R1367-R1369 (3) | STAND-CF: Repayment of lease liability, net of interest
LI315 p18 L920 | line_item | - | R1370-R1372 (3) | STAND-CF: Interest and other finance charges paid
LI316 p18 L921 | line_item | - | R1373-R1375 (3) | STAND-CF: Net cash flow generated from / (used in) financing activities (C)
LI317 p18 L923 | line_item | - | R1376-R1378 (3) | STAND-CF: Cash flow from operating activities
LI318 p18 L924 | line_item | - | R1379-R1381 (3) | STAND-CF: Cash flow from investing activities
LI319 p18 L925 | line_item | - | R1382-R1384 (3) | STAND-CF: Cash flow from financing activities
LI320 p18 L926 | line_item | - | R1385-R1387 (3) | STAND-CF: Net cash flow from discontinued operations (D)
LI321 p18 L927 | line_item | - | R1388-R1390 (3) | STAND-CF: Net increase in cash and cash equivalents (A+B+C+D)
LI322 p18 L928 | line_item | - | R1391-R1393 (3) | STAND-CF: Cash and cash equivalents at the beginning of the period / year
LI323 p18 L929 | line_item | - | R1394-R1396 (3) | STAND-CF: Cash and cash equivalents at the end of the period / year
LI324 p18 L930 | line_item | - | R1397-R1399 (3) | STAND-CF: Cash and cash equivalents comprise: Balances with banks - Current acco
LI325 p18 L931 | line_item | - | R1400-R1402 (3) | STAND-CF: Total cash and cash equivalents at end of the period / year
LI326 p20 L1033 | line_item | ZERO_STANDING | R1403-R1408 (6) | STAND-DISC/ASSETS: Revenue from operations
LI327 p20 L1034 | line_item | ZERO_STANDING | R1409-R1414 (6) | STAND-DISC/ASSETS: Other income
LI328 p20 L1035 | line_item | ZERO_STANDING | R1415-R1420 (6) | STAND-DISC/ASSETS: Total income
LI329 p20 L1036 | line_item | ZERO_STANDING(all periods) | R1421-R1426 (6) | STAND-DISC/ASSETS: Employee benefit expense
LI330 p20 L1037 | line_item | ZERO_STANDING | R1427-R1432 (6) | STAND-DISC/ASSETS: Finance costs
LI331 p20 L1038 | line_item | ZERO_STANDING | R1433-R1438 (6) | STAND-DISC/ASSETS: Depreciation and amortization expense
LI332 p20 L1039 | line_item | ZERO_STANDING | R1439-R1444 (6) | STAND-DISC/ASSETS: Other expenses
LI333 p20 L1040 | line_item | ZERO_STANDING | R1445-R1450 (6) | STAND-DISC/ASSETS: Total expenses
LI334 p20 L1041 | line_item | ZERO_STANDING | R1451-R1456 (6) | STAND-DISC/ASSETS: Profit before tax
LI335 p20 L1042 | line_item | ZERO_STANDING | R1457-R1462 (6) | STAND-DISC/ASSETS: Income tax - current
LI336 p20 L1043 | line_item | ZERO_STANDING | R1463-R1468 (6) | STAND-DISC/ASSETS: Deferred tax charge / (benefit)
LI337 p20 L1044 | line_item | ZERO_STANDING | R1469-R1474 (6) | STAND-DISC/ASSETS: Total tax
LI338 p20 L1045 | line_item | ZERO_STANDING | R1475-R1480 (6) | STAND-DISC/ASSETS: Profit after tax
LI339 p20 L1046 | line_item | ZERO_STANDING(all periods) | R1481-R1486 (6) | STAND-DISC/ASSETS: OCI (i) Items that will not be reclassified subsequently to profit or 
LI340 p20 L1047 | line_item | ZERO_STANDING(all periods) | R1487-R1492 (6) | STAND-DISC/ASSETS: OCI (ii) Income tax relating to items that will not be reclassified su
LI341 p20 L1048 | line_item | ZERO_STANDING(all periods) | R1493-R1498 (6) | STAND-DISC/ASSETS: Total Other Comprehensive Income, net of tax
LI342 p20 L1049 | line_item | ZERO_STANDING | R1499-R1504 (6) | STAND-DISC/ASSETS: Total Comprehensive Income
LI343 p20 L1050 | line_item | ZERO_STANDING | R1505-R1510 (6) | STAND-DISC/ASSETS: Earning per share of INR 5/- each (not annualized) Basic (INR)
LI344 p20 L1051 | line_item | ZERO_STANDING | R1511-R1516 (6) | STAND-DISC/ASSETS: Earning per share of INR 5/- each (not annualized) Diluted (INR)
LI345 p20 L1054 | line_item | ZERO_STANDING | R1517-R1518 (2) | STAND-DISC/ASSETS: Non - current assets
LI346 p20 L1055 | line_item | - | R1519-R1520 (2) | STAND-DISC/ASSETS: Current assets
LI347 p20 L1056 | line_item | - | R1521-R1522 (2) | STAND-DISC/ASSETS: Total assets
LI348 p20 L1057 | line_item | - | R1523-R1524 (2) | STAND-DISC/ASSETS: Non - current liabilities
LI349 p20 L1058 | line_item | - | R1525-R1526 (2) | STAND-DISC/ASSETS: Current liabilities
LI350 p20 L1059 | line_item | - | R1527-R1528 (2) | STAND-DISC/ASSETS: Total liabilities
LI351 p20 L1062 | line_item | - | R1529-R1531 (3) | STAND-DISC/ASSETS: Cash flow from operating activities
LI352 p20 L1063 | line_item | - | R1532-R1534 (3) | STAND-DISC/ASSETS: Cash flow from investing activities
LI353 p20 L1064 | line_item | - | R1535-R1537 (3) | STAND-DISC/ASSETS: Cash flow from financing activities
LI354 p20 L1065 | line_item | - | R1538-R1540 (3) | STAND-DISC/ASSETS: Total

## agenda_item
AG01 p1 L26 | agenda_item | - | R001 (1) | 
AG02 p1 L26 | agenda_item | - | R002 (1) | 
AG03 p1 L30 | agenda_item | - | R003 (1) | 
AG04 p1 L32 | agenda_item | - | R004 (1) | 
AG05 p1 L21 | agenda_item | - | R1541 (1) | 
AG06 p1 L21 | agenda_item | - | R1542 (1) | 
AG07 p1 L32 | agenda_item | - | R1543 (1) | 
AG08 p1 L43 | agenda_item | - | R1544 (1) | 
AG09 p1 L18 | agenda_item | - | R1619 (1) | 
AG10 p1 L30 | agenda_item | - | R1620 (1) | 
AG11 p1 L36 | agenda_item | - | R1621 (1) | 
AG12 p1 L38 | agenda_item | - | R1622 (1) |  | meeting 11:00 to 12:30 (90 min)
AG13 p1 L38 | agenda_item | - | R1623 (1) |  | meeting 11:00 to 12:30 (90 min)
AG14 p1 L34 | agenda_item | - | R1677 (1) |  | only agenda item: results approval

## auditor_para
AP01 | auditor_para | - | R042,R1559-R1560,R1629,R1681-R1682 (6) | C-A1 scope/intro (paras 1-2)
AP02 | auditor_para | - | R043-R044,R1561,R1683 (4) | C-A3 review standard
AP03 | auditor_para | - | R045-R046,R1630-R1635 (8) | C-A4 entity list
AP04 | auditor_para | MGMT_FURNISHED_ENTITY | R047-R048,R1686 (3) | C-A6 associate mgmt-certified (Other Matter)
AP05 | auditor_para | OCR_ILLEGIBLE(UDIN) | R049-R052,R1577-R1578,R1636 (7) | C-SIG signature/UDIN block
AP06 | auditor_para | OCR_ILLEGIBLE(UDIN) | R097-R100,R1593,R1657 (6) | S-SIG signature/UDIN block
AP07 | auditor_para | - | R1592,R1656,R1709 (3) | S-A1 scope/intro
AP08 | auditor_para | - | R1684-R1685 (2) | C-A5 conclusion (unmodified)
AP09 | auditor_para | - | R1710-R1711 (2) | S-A3 review standard
AP10 | auditor_para | - | R1712 (1) | S-A4 conclusion (unmodified)
AP-S2 | auditor_para | NO_STRUCTURED_ROWS | (0) | S-A2 standalone mgmt responsibility paragraph (fulltext L701): no numeric/entity/date unit, text only

## entity
E-R1562 | entity | - | R1562 (1) | consolidation list line 229
E-R1563 | entity | ENTITY_CHANGE(renamed) | R1563 (1) | consolidation list line 230
E-R1564 | entity | - | R1564 (1) | consolidation list line 231
E-R1565 | entity | ENTITY_CHANGE(renamed) | R1565 (1) | consolidation list line 232
E-R1566 | entity | - | R1566 (1) | consolidation list line 233
E-R1567 | entity | ENTITY_CHANGE(renamed) | R1567 (1) | consolidation list line 234
E-R1568 | entity | ENTITY_CHANGE(added, eff Sep-25) | R1568 (1) | consolidation list line 235
E-R1569 | entity | ENTITY_CHANGE(eff Apr-24) | R1569 (1) | consolidation list line 236
E-R1570 | entity | ENTITY_CHANGE(added, eff Jul-25) | R1570 (1) | consolidation list line 237
E-R1571 | entity | ENTITY_CHANGE(added, eff Sep-26),DUPLICATE_LISTING(Sr10+Sr15) | R1571 (1) | consolidation list line 238
E-R1572 | entity | - | R1572 (1) | consolidation list line 239
E-R1573 | entity | - | R1573 (1) | consolidation list line 240
E-R1574 | entity | - | R1574 (1) | consolidation list line 241
E-R1575 | entity | - | R1575 (1) | consolidation list line 242
E-R1576 | entity | ENTITY_CHANGE(subsidiary to associate Jul-25) | R1576 (1) | consolidation list line 244

## signature
SG01 p13 L670 | signature | - | R096 (1) | 
SG02 p20 L1072 | signature | - | R159 (1) | 
SG03 p1 L49 | signature | - | R1545 (1) | 
SG04 p13 L668 | signature | - | R1590 (1) | 
SG05 p13 L671 | signature | - | R1591 (1) | 
SG06 p20 L1070 | signature | - | R1598 (1) | 
SG07 p20 L1073 | signature | - | R1599 (1) | 
SG08 p1 L46 | signature | - | R1624 (1) |  | digital signature 12:33:37 is after meeting end 12:30
SG09 p13 L672 | signature | - | R1655 (1) | 
SG10 p20 L1074 | signature | - | R1676 (1) | 

## press_release
PR001 p2 L52 | press_release | - | R005 (1) | 
PR002 p2 L54 | press_release | - | R006 (1) | 
PR003 p2 L64 | press_release | - | R007-R009 (3) | 
PR004 p2 L65 | press_release | FOOTNOTE_UNRESOLVED | R010-R012,R1678 (4) | 
PR005 p2 L66 | press_release | - | R013-R015 (3) | 
PR006 p2 L73 | press_release | - | R016 (1) | 
PR007 p2 L74 | press_release | - | R017 (1) | 
PR008 p3 L93 | press_release | - | R018-R020 (3) | 
PR009 p3 L103 | press_release | - | R021-R022 (2) | 
PR010 p3 L104 | press_release | - | R023-R024,R1628 (3) | 
PR011 p3 L105 | press_release | - | R025,R1551,R1607 (3) | 
PR012 p3 L113 | press_release | - | R026-R027 (2) | 
PR013 p3 L114 | press_release | - | R028 (1) | 
PR014 p3 L115 | press_release | - | R029-R030 (2) | 
PR015 p3 L126 | press_release | - | R031-R032 (2) | 
PR016 p3 L127 | press_release | - | R033 (1) | 
PR017 p3 L128 | press_release | - | R034-R035 (2) | 
PR018 p4 L133 | press_release | - | R036-R037 (2) | 
PR019 p4 L134 | press_release | - | R038-R039 (2) | 
PR020 p4 L135 | press_release | - | R040 (1) | 
PR021 p4 L141 | press_release | - | R041 (1) | 
PR022 p2 L53 | press_release | - | R1546 (1) | 
PR023 p2 L70 | press_release | - | R1547 (1) | 
PR024 p3 L91 | press_release | - | R1548 (1) | 
PR025 p3 L94 | press_release | - | R1549 (1) | 
PR026 p3 L101 | press_release | - | R1550 (1) | 
PR027 p3 L111 | press_release | - | R1552 (1) | 
PR028 p3 L124 | press_release | - | R1553 (1) | 
PR029 p4 L131 | press_release | - | R1554 (1) | 
PR030 p4 L142 | press_release | - | R1555 (1) | 
PR031 p4 L146 | press_release | - | R1556 (1) | 
PR032 p4 L161 | press_release | - | R1557-R1558 (2) | 
PR033 p2 L56 | press_release | - | R1600 (1) | 
PR034 p2 L57 | press_release | - | R1601 (1) | 
PR035 p2 L75 | press_release | - | R1602 (1) | 
PR036 p2 L77 | press_release | - | R1603 (1) | 
PR037 p2 L78 | press_release | - | R1604 (1) | 
PR038 p2 L82 | press_release | - | R1605 (1) | 
PR039 p3 L95 | press_release | - | R1606 (1) | 
PR040 p4 L154 | press_release | - | R1608 (1) | 
PR041 p2 L60 | press_release | - | R1625 (1) | 
PR042 p2 L63 | press_release | - | R1626-R1627 (2) | 
PR043 p4 L153 | press_release | - | R1679 (1) | 
PR044 p4 L166 | press_release | - | R1680 (1) | 

## table_qualifier
TQ001 p8 L301 | table_qualifier | - | R053 (1) | 
TQ002 p8 L301 | table_qualifier | - | R1579 (1) | 
TQ003 p8 L302 | table_qualifier | - | R1687 (1) | 
TQ004 p8 L305 | table_qualifier | - | R1688 (1) | 
TQ005 p8 L350 | table_qualifier | - | R1689 (1) | 
TQ006 p8 L351 | table_qualifier | - | R1690 (1) | 
TQ007 p9 L361 | table_qualifier | - | R1691 (1) | 
TQ008 p9 L363 | table_qualifier | - | R1692 (1) | 
TQ009 p9 L365 | table_qualifier | - | R1693 (1) | 
TQ010 p9 L380 | table_qualifier | - | R1694 (1) | 
TQ011 p10 L399 | table_qualifier | - | R1695 (1) | 
TQ012 p10 L401 | table_qualifier | - | R1696 (1) | 
TQ013 p11 L456 | table_qualifier | - | R1697 (1) | 
TQ014 p13 L623 | table_qualifier | - | R1704 (1) | 
TQ015 p16 L778 | table_qualifier | - | R1713 (1) | 
TQ016 p16 L807 | table_qualifier | - | R1714 (1) | 
TQ017 p16 L808 | table_qualifier | - | R1715 (1) | 
TQ018 p17 L818 | table_qualifier | - | R1716 (1) | 
TQ019 p18 L870 | table_qualifier | - | R1717 (1) | 
TQ020 p20 L1026 | table_qualifier | - | R1724 (1) | 

## missing
MS01 fulltext L530 | note2 entity | MISSING_FROM_STRUCTURED,RESTATED | no ID | Liv Real Solutions: second listing in consolidated note 2 group list; entity already in auditor list rows
MS02 fulltext L532 | note2 entity | MISSING_FROM_STRUCTURED,RESTATED | no ID | HelloWorld Technologies: second listing in consolidated note 2 group list; entity already in auditor list rows
MS03 fulltext L533 | note2 entity | MISSING_FROM_STRUCTURED,RESTATED | no ID | Integrow: second listing in consolidated note 2 group list; entity already in auditor list rows
MS04 fulltext L534 | note2 entity | MISSING_FROM_STRUCTURED,RESTATED | no ID | Aurum Analytica: second listing in consolidated note 2 group list; entity already in auditor list rows
MS05 fulltext L537 | note2 entity | MISSING_FROM_STRUCTURED,RESTATED | no ID | Cuneate: second listing in consolidated note 2 group list; entity already in auditor list rows
MS06 fulltext L538 | note2 entity | MISSING_FROM_STRUCTURED,RESTATED | no ID | NestAway Technologies: second listing in consolidated note 2 group list; entity already in auditor list rows
MS07 fulltext L540 | note2 entity | MISSING_FROM_STRUCTURED,RESTATED | no ID | NestAway PropTech Mena: second listing in consolidated note 2 group list; entity already in auditor list rows
MS08 fulltext L541 | note2 entity | MISSING_FROM_STRUCTURED,RESTATED | no ID | PropTiger Marketing (wef Sep 26 2025): second listing in consolidated note 2 group list; entity already in auditor list rows
MS09 fulltext L543 | note2 entity | MISSING_FROM_STRUCTURED,RESTATED | no ID | Locon Solutions (wef Sep 29 2026): second listing in consolidated note 2 group list; entity already in auditor list rows
