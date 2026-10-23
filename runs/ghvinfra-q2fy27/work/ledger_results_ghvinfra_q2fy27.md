# A2 COMPLETENESS LEDGER: GHVINFRA Q2 FY27 (results, full Reg 33 filing, 17 pages)

Source: A1 structured extraction ghvinfra-results-q2fy27-structured.md (R001-R821). Rows are referenced by ID only; verbatim values stay in the structured file.
Prior ledger: Q1 FY27 was a 3-page Reg 30 media release (no notes, no auditor report, no entity list, no consolidation list), so entity, note and auditor diffs have no Q1 baseline (all counts new).

ids_in_structured: 821 | ids_referenced_in_ledger: 821 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: notes (standalone 8 + consolidated 11)       grep_count: 19  sweep_count: 19  match: yes
category: footnotes (EPS asterisk x2, pairs R757/R758, R798/R799)  grep_count: 2  sweep_count: 2  match: yes
category: line_items (6 statements, distinct lines)    grep_count: 196  sweep_count: 196  match: yes   [P&L S 26, BS S 35, CF S 33, P&L C 36, BS C 35, CF C 31; first manual sweep gave BS 34 by omitting line 411, re-swept and reconciled]
category: zero_standing (dash/Nil cells)               grep_count: 41  sweep_count: 41  match: yes   [39 table dash cells on 24 lines + 2 Nil subsidiary revenue qualifiers R341, R342; grep of ZERO_STANDING gives 42 incl. header line]
category: agenda_items (Board Outcome items 1-4)       grep_count: 4   sweep_count: 4   match: yes
category: annexures (Annexure 1, 2, 3)                 grep_count: 3   sweep_count: 3   match: yes
category: auditor_paras (standalone 4 + consolidated 7)  grep_count: 11  sweep_count: 11  match: yes
category: entities (consolidation list excl. parent)   grep_count: 4   sweep_count: 4   match: yes
category: turns / questions / mgmt_numbers / slides / slide_numbers   not applicable (results filing)  0 / 0 / 0 / 0 / 0
gate_a2: pass
=== END COUNT TEST ===

Key flags for A3/A4 (enumerated, not interpreted):
- ENTITY_CHANGE: 2 wholly owned subsidiaries + 2 JVs, consolidated since Dec-2025 quarter; Q1 media release carried no entity list. Consolidated Sep-2025 comparatives not presented (R810).
- MANAGEMENT_FURNISHED: two foreign subs and one JV not reviewed by auditor (R783-R791).
- Standalone vs consolidated differ for Q2 (PBT R103 vs R404; Investments R190 vs R505) and for Q1 (PAT R134 vs R425). Q1 media release figures match the standalone Q1 column.
- Resignation of Independent Director and new CFO on result day; MD signs the notes, CS signs the letter.
- Erisha EPC contract concluded with contingent legal proceedings, no provision (S5 / C8).
- Pending warrants 21,83,333 (R330/R610); promoter reclassification (S4 / C7).

## LINE ITEMS: all financial table lines, per statement (196 rows)

| # | ROW IDs (one cell per period) | page/line | category | A2 flag | note |
|---|---|---|---|---|---|
| L001 | R031-R036 | p7 l328 | line_item (standalone P&L) | - |  |
| L002 | R037-R042 | p7 l329 | line_item (standalone P&L) | - |  |
| L003 | R043-R048 | p7 l330 | line_item (standalone P&L) | - |  |
| L004 | R049-R054 | p7 l332 | line_item (standalone P&L) | - |  |
| L005 | R055-R060 | p7 l333 | line_item (standalone P&L) | - |  |
| L006 | R061-R066 | p7 l334 | line_item (standalone P&L) | - |  |
| L007 | R067-R072 | p7 l335 | line_item (standalone P&L) | ZERO_STANDING | dash cells: R070 |
| L008 | R073-R078 | p7 l336 | line_item (standalone P&L) | - |  |
| L009 | R079-R084 | p7 l337 | line_item (standalone P&L) | - |  |
| L010 | R085-R090 | p7 l338 | line_item (standalone P&L) | - |  |
| L011 | R091-R096 | p7 l339 | line_item (standalone P&L) | - |  |
| L012 | R097-R102 | p7 l340 | line_item (standalone P&L) | - |  |
| L013 | R103-R108 | p7 l341 | line_item (standalone P&L) | - |  |
| L014 | R109-R114 | p7 l343 | line_item (standalone P&L) | - |  |
| L015 | R115-R120 | p7 l344 | line_item (standalone P&L) | - |  |
| L016 | R121-R126 | p7 l345 | line_item (standalone P&L) | ZERO_STANDING | dash cells: R121-R125 |
| L017 | R127-R132 | p7 l346 | line_item (standalone P&L) | - |  |
| L018 | R133-R138 | p7 l347 | line_item (standalone P&L) | - |  |
| L019 | R139-R144 | p7 l349 | line_item (standalone P&L) | - |  |
| L020 | R145-R150 | p7 l350 | line_item (standalone P&L) | - |  |
| L021 | R151-R156 | p7 l351 | line_item (standalone P&L) | - |  |
| L022 | R157-R162 | p7 l352 | line_item (standalone P&L) | - |  |
| L023 | R163-R169 | p7 l353 | line_item (standalone P&L) | - |  |
| L024 | R170 | p7 l354 | line_item (standalone P&L) | - |  |
| L025 | R171-R176 | p7 l356 | line_item (standalone P&L) | - |  |
| L026 | R177-R182 | p7 l357 | line_item (standalone P&L) | - |  |
| L027 | R184-R185 | p8 l371 | line_item (standalone balance sheet) | - |  |
| L028 | R186-R187 | p8 l372 | line_item (standalone balance sheet) | - |  |
| L029 | R188-R189 | p8 l373 | line_item (standalone balance sheet) | - |  |
| L030 | R190-R191 | p8 l374 | line_item (standalone balance sheet) | - |  |
| L031 | R192-R193 | p8 l375 | line_item (standalone balance sheet) | - |  |
| L032 | R194-R195 | p8 l376 | line_item (standalone balance sheet) | ZERO_STANDING | dash cells: R195 |
| L033 | R196-R197 | p8 l377 | line_item (standalone balance sheet) | ZERO_STANDING | dash cells: R197 |
| L034 | R198-R199 | p8 l378 | line_item (standalone balance sheet) | - |  |
| L035 | R200-R201 | p8 l380 | line_item (standalone balance sheet) | - |  |
| L036 | R202-R203 | p8 l381 | line_item (standalone balance sheet) | - |  |
| L037 | R204-R205 | p8 l382 | line_item (standalone balance sheet) | - |  |
| L038 | R206-R207 | p8 l383 | line_item (standalone balance sheet) | ZERO_STANDING | dash cells: R207 |
| L039 | R208-R209 | p8 l384 | line_item (standalone balance sheet) | - |  |
| L040 | R210-R211 | p8 l385 | line_item (standalone balance sheet) | - |  |
| L041 | R212-R213 | p8 l386 | line_item (standalone balance sheet) | - |  |
| L042 | R214-R215 | p8 l387 | line_item (standalone balance sheet) | - |  |
| L043 | R216-R217 | p8 l388 | line_item (standalone balance sheet) | - |  |
| L044 | R218-R219 | p8 l391 | line_item (standalone balance sheet) | - |  |
| L045 | R220-R221 | p8 l392 | line_item (standalone balance sheet) | - |  |
| L046 | R222-R223 | p8 l393 | line_item (standalone balance sheet) | - |  |
| L047 | R224-R225 | p8 l396 | line_item (standalone balance sheet) | - |  |
| L048 | R226-R227 | p8 l397 | line_item (standalone balance sheet) | - |  |
| L049 | R228-R229 | p8 l398 | line_item (standalone balance sheet) | ZERO_STANDING | dash cells: R228 |
| L050 | R230-R231 | p8 l399 | line_item (standalone balance sheet) | - |  |
| L051 | R232-R233 | p8 l401 | line_item (standalone balance sheet) | - |  |
| L052 | R234-R235 | p8 l402 | line_item (standalone balance sheet) | - |  |
| L053 | R236-R237 | p8 l403 | line_item (standalone balance sheet) | - |  |
| L054 | R238-R239 | p8 l404 | line_item (standalone balance sheet) | - |  |
| L055 | R240-R241 | p8 l405 | line_item (standalone balance sheet) | - |  |
| L056 | R242-R243 | p8 l406 | line_item (standalone balance sheet) | - |  |
| L057 | R244-R245 | p8 l407 | line_item (standalone balance sheet) | - |  |
| L058 | R246-R247 | p8 l408 | line_item (standalone balance sheet) | - |  |
| L059 | R248-R249 | p8 l409 | line_item (standalone balance sheet) | - |  |
| L060 | R250-R251 | p8 l410 | line_item (standalone balance sheet) | - |  |
| L061 | R252-R253 | p8 l411 | line_item (standalone balance sheet) | - |  |
| L062 | R255-R256 | p9 l423 | line_item (standalone cash flow) | - |  |
| L063 | R257-R258 | p9 l424 | line_item (standalone cash flow) | - |  |
| L064 | R259-R260 | p9 l425 | line_item (standalone cash flow) | - |  |
| L065 | R261-R262 | p9 l426 | line_item (standalone cash flow) | ZERO_STANDING | dash cells: R262 |
| L066 | R263-R264 | p9 l427 | line_item (standalone cash flow) | - |  |
| L067 | R265-R266 | p9 l428 | line_item (standalone cash flow) | - |  |
| L068 | R267-R268 | p9 l429 | line_item (standalone cash flow) | - |  |
| L069 | R269-R270 | p9 l430 | line_item (standalone cash flow) | - |  |
| L070 | R271-R272 | p9 l431 | line_item (standalone cash flow) | ZERO_STANDING | dash cells: R271 |
| L071 | R273-R274 | p9 l432 | line_item (standalone cash flow) | - |  |
| L072 | R275-R276 | p9 l433 | line_item (standalone cash flow) | ZERO_STANDING | dash cells: R275 |
| L073 | R277-R278 | p9 l434 | line_item (standalone cash flow) | - |  |
| L074 | R279-R280 | p9 l435 | line_item (standalone cash flow) | - |  |
| L075 | R281-R282 | p9 l436 | line_item (standalone cash flow) | - |  |
| L076 | R283-R284 | p9 l437 | line_item (standalone cash flow) | - |  |
| L077 | R285-R286 | p9 l438 | line_item (standalone cash flow) | - |  |
| L078 | R287-R288 | p9 l439 | line_item (standalone cash flow) | - |  |
| L079 | R289-R290 | p9 l441 | line_item (standalone cash flow) | - |  |
| L080 | R291-R292 | p9 l442 | line_item (standalone cash flow) | ZERO_STANDING | dash cells: R292 |
| L081 | R293-R294 | p9 l443 | line_item (standalone cash flow) | ZERO_STANDING | dash cells: R294 |
| L082 | R295-R296 | p9 l444 | line_item (standalone cash flow) | - |  |
| L083 | R297-R298 | p9 l445 | line_item (standalone cash flow) | ZERO_STANDING | dash cells: R298 |
| L084 | R299-R300 | p9 l446 | line_item (standalone cash flow) | - |  |
| L085 | R301-R302 | p9 l448 | line_item (standalone cash flow) | - |  |
| L086 | R303-R304 | p9 l449 | line_item (standalone cash flow) | ZERO_STANDING | dash cells: R304 |
| L087 | R305-R306 | p9 l450 | line_item (standalone cash flow) | - |  |
| L088 | R307-R308 | p9 l451 | line_item (standalone cash flow) | ZERO_STANDING | dash cells: R308 |
| L089 | R309-R310 | p9 l452 | line_item (standalone cash flow) | - |  |
| L090 | R311-R312 | p9 l453 | line_item (standalone cash flow) | ZERO_STANDING | dash cells: R312 |
| L091 | R313-R314 | p9 l454 | line_item (standalone cash flow) | - |  |
| L092 | R315-R316 | p9 l455 | line_item (standalone cash flow) | - |  |
| L093 | R317-R318 | p9 l456 | line_item (standalone cash flow) | - |  |
| L094 | R319-R320 | p9 l457 | line_item (standalone cash flow) | - |  |
| L095 | R356-R359 | p13 l620 | line_item (consolidated P&L) | - |  |
| L096 | R360-R363 | p13 l621 | line_item (consolidated P&L) | - |  |
| L097 | R364-R367 | p13 l622 | line_item (consolidated P&L) | - |  |
| L098 | R368-R371 | p13 l624 | line_item (consolidated P&L) | - |  |
| L099 | R372-R375 | p13 l625 | line_item (consolidated P&L) | - |  |
| L100 | R376-R379 | p13 l626 | line_item (consolidated P&L) | - |  |
| L101 | R380-R383 | p13 l627 | line_item (consolidated P&L) | ZERO_STANDING | dash cells: R382 |
| L102 | R384-R387 | p13 l628 | line_item (consolidated P&L) | - |  |
| L103 | R388-R391 | p13 l629 | line_item (consolidated P&L) | - |  |
| L104 | R392-R395 | p13 l630 | line_item (consolidated P&L) | - |  |
| L105 | R396-R399 | p13 l631 | line_item (consolidated P&L) | - |  |
| L106 | R400-R403 | p13 l632 | line_item (consolidated P&L) | - |  |
| L107 | R404-R407 | p13 l633 | line_item (consolidated P&L) | - |  |
| L108 | R408-R411 | p13 l635 | line_item (consolidated P&L) | - |  |
| L109 | R412-R415 | p13 l636 | line_item (consolidated P&L) | - |  |
| L110 | R416-R419 | p13 l637 | line_item (consolidated P&L) | ZERO_STANDING | dash cells: R416-R418 |
| L111 | R420-R423 | p13 l638 | line_item (consolidated P&L) | - |  |
| L112 | R424-R427 | p13 l639 | line_item (consolidated P&L) | - |  |
| L113 | R428-R431 | p13 l641 | line_item (consolidated P&L) | - |  |
| L114 | R432-R435 | p13 l642 | line_item (consolidated P&L) | - |  |
| L115 | R436-R439 | p13 l643 | line_item (consolidated P&L) | - |  |
| L116 | R440-R443 | p13 l644 | line_item (consolidated P&L) | ZERO_STANDING | dash cells: R440-R443 |
| L117 | R444-R447 | p13 l646 | line_item (consolidated P&L) | - |  |
| L118 | R448-R451 | p13 l647 | line_item (consolidated P&L) | - |  |
| L119 | R452-R455 | p13 l649 | line_item (consolidated P&L) | - |  |
| L120 | R456-R459 | p13 l650 | line_item (consolidated P&L) | - |  |
| L121 | R460-R463 | p13 l651 | line_item (consolidated P&L) | - |  |
| L122 | R464-R467 | p13 l652 | line_item (consolidated P&L) | - |  |
| L123 | R468-R471 | p13 l653 | line_item (consolidated P&L) | ZERO_STANDING | dash cells: R468-R471 |
| L124 | R472-R475 | p13 l654 | line_item (consolidated P&L) | - |  |
| L125 | R476-R479 | p13 l655 | line_item (consolidated P&L) | - |  |
| L126 | R480-R483 | p13 l656 | line_item (consolidated P&L) | ZERO_STANDING | dash cells: R480-R483 |
| L127 | R484-R488 | p13 l657 | line_item (consolidated P&L) | - |  |
| L128 | R489 | p13 l658 | line_item (consolidated P&L) | - |  |
| L129 | R490-R493 | p13 l660 | line_item (consolidated P&L) | - |  |
| L130 | R494-R497 | p13 l661 | line_item (consolidated P&L) | - |  |
| L131 | R499-R500 | p14 l675 | line_item (consolidated balance sheet) | - |  |
| L132 | R501-R502 | p14 l676 | line_item (consolidated balance sheet) | - |  |
| L133 | R503-R504 | p14 l677 | line_item (consolidated balance sheet) | - |  |
| L134 | R505-R506 | p14 l678 | line_item (consolidated balance sheet) | - |  |
| L135 | R507-R508 | p14 l679 | line_item (consolidated balance sheet) | - |  |
| L136 | R509-R510 | p14 l680 | line_item (consolidated balance sheet) | ZERO_STANDING | dash cells: R510 |
| L137 | R511-R512 | p14 l681 | line_item (consolidated balance sheet) | ZERO_STANDING | dash cells: R512 |
| L138 | R513-R514 | p14 l682 | line_item (consolidated balance sheet) | - |  |
| L139 | R515-R516 | p14 l684 | line_item (consolidated balance sheet) | - |  |
| L140 | R517-R518 | p14 l685 | line_item (consolidated balance sheet) | - |  |
| L141 | R519-R520 | p14 l686 | line_item (consolidated balance sheet) | - |  |
| L142 | R521-R522 | p14 l687 | line_item (consolidated balance sheet) | ZERO_STANDING | dash cells: R522 |
| L143 | R523-R524 | p14 l688 | line_item (consolidated balance sheet) | - |  |
| L144 | R525-R526 | p14 l689 | line_item (consolidated balance sheet) | - |  |
| L145 | R527-R528 | p14 l690 | line_item (consolidated balance sheet) | - |  |
| L146 | R529-R530 | p14 l691 | line_item (consolidated balance sheet) | - |  |
| L147 | R531-R532 | p14 l692 | line_item (consolidated balance sheet) | - |  |
| L148 | R533-R534 | p14 l695 | line_item (consolidated balance sheet) | - |  |
| L149 | R535-R536 | p14 l696 | line_item (consolidated balance sheet) | - |  |
| L150 | R537-R538 | p14 l697 | line_item (consolidated balance sheet) | - |  |
| L151 | R539-R540 | p14 l700 | line_item (consolidated balance sheet) | - |  |
| L152 | R541-R542 | p14 l701 | line_item (consolidated balance sheet) | - |  |
| L153 | R543-R544 | p14 l702 | line_item (consolidated balance sheet) | ZERO_STANDING | dash cells: R543 |
| L154 | R545-R546 | p14 l703 | line_item (consolidated balance sheet) | - |  |
| L155 | R547-R548 | p14 l705 | line_item (consolidated balance sheet) | - |  |
| L156 | R549-R550 | p14 l706 | line_item (consolidated balance sheet) | - |  |
| L157 | R551-R552 | p14 l707 | line_item (consolidated balance sheet) | - |  |
| L158 | R553-R554 | p14 l708 | line_item (consolidated balance sheet) | - |  |
| L159 | R555-R556 | p14 l709 | line_item (consolidated balance sheet) | - |  |
| L160 | R557-R558 | p14 l710 | line_item (consolidated balance sheet) | - |  |
| L161 | R559-R560 | p14 l711 | line_item (consolidated balance sheet) | - |  |
| L162 | R561-R562 | p14 l712 | line_item (consolidated balance sheet) | - |  |
| L163 | R563-R564 | p14 l713 | line_item (consolidated balance sheet) | - |  |
| L164 | R565-R566 | p14 l714 | line_item (consolidated balance sheet) | - |  |
| L165 | R567-R568 | p14 l715 | line_item (consolidated balance sheet) | - |  |
| L166 | R570 | p15 l727 | line_item (consolidated cash flow) | - |  |
| L167 | R571 | p15 l728 | line_item (consolidated cash flow) | - |  |
| L168 | R572 | p15 l729 | line_item (consolidated cash flow) | - |  |
| L169 | R573 | p15 l730 | line_item (consolidated cash flow) | - |  |
| L170 | R574 | p15 l731 | line_item (consolidated cash flow) | - |  |
| L171 | R575 | p15 l732 | line_item (consolidated cash flow) | - |  |
| L172 | R576 | p15 l733 | line_item (consolidated cash flow) | - |  |
| L173 | R577 | p15 l734 | line_item (consolidated cash flow) | - |  |
| L174 | R578 | p15 l735 | line_item (consolidated cash flow) | - |  |
| L175 | R579 | p15 l736 | line_item (consolidated cash flow) | - |  |
| L176 | R580 | p15 l737 | line_item (consolidated cash flow) | - |  |
| L177 | R581 | p15 l738 | line_item (consolidated cash flow) | - |  |
| L178 | R582 | p15 l739 | line_item (consolidated cash flow) | - |  |
| L179 | R583 | p15 l740 | line_item (consolidated cash flow) | - |  |
| L180 | R584 | p15 l741 | line_item (consolidated cash flow) | - |  |
| L181 | R585 | p15 l742 | line_item (consolidated cash flow) | - |  |
| L182 | R586 | p15 l744 | line_item (consolidated cash flow) | - |  |
| L183 | R587 | p15 l745 | line_item (consolidated cash flow) | - |  |
| L184 | R588 | p15 l746 | line_item (consolidated cash flow) | - |  |
| L185 | R589 | p15 l747 | line_item (consolidated cash flow) | - |  |
| L186 | R590 | p15 l748 | line_item (consolidated cash flow) | - |  |
| L187 | R591 | p15 l750 | line_item (consolidated cash flow) | - |  |
| L188 | R592 | p15 l751 | line_item (consolidated cash flow) | - |  |
| L189 | R593 | p15 l752 | line_item (consolidated cash flow) | - |  |
| L190 | R594 | p15 l753 | line_item (consolidated cash flow) | - |  |
| L191 | R595 | p15 l754 | line_item (consolidated cash flow) | - |  |
| L192 | R596 | p15 l755 | line_item (consolidated cash flow) | - |  |
| L193 | R597 | p15 l756 | line_item (consolidated cash flow) | - |  |
| L194 | R598 | p15 l757 | line_item (consolidated cash flow) | - |  |
| L195 | R599 | p15 l758 | line_item (consolidated cash flow) | - |  |
| L196 | R600 | p15 l759 | line_item (consolidated cash flow) | - |  |

## TABLE A: filing metadata (3 rows)

| # | ROW IDs | category | A2 flags | note |
|---|---|---|---|---|
| A01 | R001-R002,R004-R006,R009,R017,R022,R030,R183,R254,R355,R498,R569,R626 | filing_meta | - | letterhead, scrip, SEBI circular ref, contacts, CIN per page, registered office |
| A02 | R616-R619 | filing_meta | - | BSE addressee, scrip ID, Reg 30 invocation, board body |
| A03 | R704,R706,R708 | filing_meta | DATE_CHECK | letter date equals board meeting date 22-Oct-2026 (R705); results period; Master Circular date |

## TABLE B: Board Outcome agenda items and meeting times (5 rows)

| # | ROW IDs | category | A2 flags | note |
|---|---|---|---|---|
| B01 | R007-R008,R705 | agenda_item | BOARD_TIMES | 04:30 PM to 06:45 PM = 2h15m; digital signature R711 is after end time, no premature-signature flag |
| B02 | R618-R621,R697,R706,R746 | agenda_item | AGENDA_1_RESULTS | Item 1: unaudited standalone and consolidated results, LRR by Manubhai & Shah LLP |
| B03 | R002,R622-R623,R707 | agenda_item | AGENDA_2_CFO | Item 2: Salim Yahoo appointed CFO (KMP) w.e.f. 22-Oct-2026; Annexure 1 |
| B04 | R003,R624-R625,R709 | agenda_item | AGENDA_3_ID_RESIGN | Item 3: Independent Director Ravi Kumar Seth resigns, leaves Audit and NRC; Annexures 2 and 3 |
| B05 | R627-R631,R710 | agenda_item | AGENDA_4_KMP_AUTH | Item 4: Reg 30(5) authorised KMPs (MD, WTD, CFO, CS). No AR approval, AGM notice, dividend, record date, auditor change, ESOP or fundraising item |

## TABLE C: annexures, director profiles, signature (5 rows)

| # | ROW IDs | category | A2 flags | note |
|---|---|---|---|---|
| C01 | R010-R016,R633-R644,R712-R713 | annexure | ANNEXURE_1_CFO_PROFILE | profile row: Salim Yahoo, KMP, DIN Not Applicable, relationships Not Applicable |
| C02 | R018-R021,R645-R650,R714-R715 | annexure | ANNEXURE_2_ID_PROFILE | profile row: Ravi Kumar Seth DIN 02427404, two other listed directorships; fields Not Applicable |
| C03 | R748-R749 | annexure | - | confirmation of no other material reason, annexure 2 item 8 |
| C04 | R615,R692-R696,R744-R745,R820-R821 | annexure | ANNEXURE_3_RESIGNATION_LETTER | stated reason: pre-occupation and other professional commitments; no other material reason |
| C05 | R632,R711,R747 | annexure | SIGNATURE | CS Daksh Mewada digital signature, timestamp 20:45:53 on 22-Oct-2026 |

## TABLE D: auditor report paragraphs (11 rows)

| # | ROW IDs | category | A2 flags | note |
|---|---|---|---|---|
| D01 | R651-R657 | auditor_para | AUDITOR_STANDALONE_P1_3 | Standalone paras 1-3: engagement, management responsibility, scope under SRE 2410 (R656) |
| D02 | R023-R029,R716,R750-R751 | auditor_para | AUDITOR_STANDALONE_SCOPE_UDIN | scope limits, no audit opinion; LLP id, FRN, membership no, UDIN 26114753SVSGKS8783 |
| D03 | R658-R659,R717,R752 | auditor_para | AUDITOR_STANDALONE_P4 | Standalone para 4: unmodified conclusion; no Going Concern, EOM or Other Matters paragraph; partner signature |
| D04 | R335-R336,R672-R673,R727,R777-R778 | auditor_para | AUDITOR_CONSOL_P1_3 | Consolidated paras 1-3: engagement, scope includes JV share |
| D05 | R337-R338,R779-R781 | auditor_para | AUDITOR_CONSOL_P3 | no audit opinion, Reg 33(8) procedures; OCR phone variance 3558 vs R026 3658 |
| D06 | R674-R677 | auditor_para | AUDITOR_CONSOL_P4_ENTITY_LIST | Consolidated para 4: entities included |
| D07 | R782 | auditor_para | AUDITOR_CONSOL_P5 | Consolidated para 5 conclusion by reference to paras 6 and 7; unmodified |
| D08 | R339-R347,R728,R783,R785-R787 | auditor_para | AUDITOR_CONSOL_P6_UNREVIEWED_SUBS MANAGEMENT_FURNISHED | two foreign subsidiaries neither reviewed by auditor nor their own auditors; assets 4,075.53 L, revenue Nil, H1 net loss 482.78 L; conclusion not modified |
| D09 | R348-R351,R729,R784 | auditor_para | AUDITOR_CONSOL_P6_UNREVIEWED_JV MANAGEMENT_FURNISHED | one JV unreviewed; share profit 9.97 L qtr, loss (6.74) L H1 |
| D10 | R788-R791 | auditor_para | AUDITOR_CONSOL_P7 | para 7: JV not commenced (BIL), no share recognised; not material; conclusion not modified |
| D11 | R352-R354,R678-R679,R730 | auditor_para | AUDITOR_CONSOL_SIGN | FRN, membership 114753, UDIN 26114753FOLTCE5978, place Mumbai |

## TABLE E: consolidation entities (6 rows)

| # | ROW IDs | category | A2 flags | note |
|---|---|---|---|---|
| E01 | R654,R660,R673 | entity | ENTITY_PARENT | GHV Infra Projects Limited, reporting entity (formerly Sindu Valley Technologies) |
| E02 | R669,R674,R681,R689 | entity | ENTITY_CHANGE RESTATED | wholly owned sub GHV Infra FZ-LLC (UAE), also Erisha EPC contractor; not in Q1 media release; consolidated since Dec-2025 quarter (R738) |
| E03 | R675,R682 | entity | ENTITY_CHANGE RESTATED | wholly owned sub GHV Infra Inc., Ohio USA |
| E04 | R676,R683 | entity | ENTITY_CHANGE RESTATED | JV GHV Infra Projects-RKS-TCIPL |
| E05 | R677,R684,R736 | entity | ENTITY_CHANGE RESTATED FOOTNOTE_UNRESOLVED | JV GHV Infra Projects-BIL; no transactions to 30-Sep-2026; relationship cell not captured by OCR (R677), resolved by R808 as JV |
| E06 | R661-R662,R680 | entity | - | Partnership Firm share-of-loss line and subsidiary investment line; entity name not stated in the cash flow |

## TABLE F: numbered notes and footnotes (21 rows)

| # | ROW IDs | category | A2 flags | note |
|---|---|---|---|---|
| F01 | R764-R765 | note | NOTE_S1 | Standalone note 1: Ind AS basis (header R764) |
| F02 | R766 | note | NOTE_S2 | Standalone note 2: Audit Committee review, Board approval 22-Oct-2026 |
| F03 | R321-R330,R663-R664,R698,R723,R767 | note | NOTE_S3 WARRANT_CONVERSION | Standalone note 3: promoter JHV Commercials LLP balance 5,000.01 L; 16,16,667 warrants to 83,33,335 shares; 21,83,333 warrants pending (dilution). Restated as C6 |
| F04 | R331-R333,R665-R666,R724,R768 | note | NOTE_S4 PROMOTER_RECLASS | Standalone note 4: Husena Musamji 37,50,000 shares (5.20%) Promoter to Public |
| F05 | R667-R670,R699-R700,R725,R769-R773 | note | NOTE_S5 CONTINGENCY | Standalone note 5: Erisha RAKEZ UAE EPC contract concluded, delays and West Asia, legal proceedings, no provision, forward reassessment |
| F06 | R774 | note | NOTE_S6 | Standalone note 6: single segment |
| F07 | R775 | note | NOTE_S7 | Standalone note 7: regrouping |
| F08 | R776 | note | NOTE_S8 | Standalone note 8: availability |
| F09 | R805-R806 | note | NOTE_C1 | Consolidated note 1: Ind AS basis (header R805) |
| F10 | R807 | note | NOTE_C2 | Consolidated note 2: review and approval |
| F11 | R601,R681-R684,R808 | note | NOTE_C3 RESTATED | Consolidated note 3: scope two subs and two JVs |
| F12 | R736,R809 | note | NOTE_C4 | Consolidated note 4: BIL JV not commenced |
| F13 | R737-R739,R793-R794,R803,R810 | note | NOTE_C5 NO_PRIOR_YEAR_COMPARATIVE | Consolidated note 5: no Sep-2025 consolidated quarter or half-year comparatives; markers R793, R803 |
| F14 | R602-R610,R685,R701,R740,R811 | note | NOTE_C6 RESTATED | Consolidated note 6 restates standalone note 3 (R767) |
| F15 | R611-R613,R686,R741,R812 | note | NOTE_C7 RESTATED | Consolidated note 7 restates standalone note 4 (R768) |
| F16 | R687-R690,R702-R703,R742,R813-R816 | note | NOTE_C8 CONTINGENCY RESTATED | Consolidated note 8 restates standalone note 5 (R769); no provision |
| F17 | R817 | note | NOTE_C9 | Consolidated note 9: single segment |
| F18 | R818 | note | NOTE_C10 | Consolidated note 10: regrouping |
| F19 | R819 | note | NOTE_C11 | Consolidated note 11: availability |
| F20 | R755-R758 | note | FOOTNOTE EPS_ASTERISK | Standalone EPS asterisk footnote: bonus and sub-division restatement, Ind AS 33 para 64 |
| F21 | R796-R799 | note | FOOTNOTE EPS_ASTERISK RESTATED | Consolidated EPS asterisk footnote |

## TABLE G: residual dates, qualifiers, forwards (6 rows)

| # | ROW IDs | category | A2 flags | note |
|---|---|---|---|---|
| G01 | R169,R488 | residual | UNIT | face value Rs 5 per share, in paid-up capital lines |
| G02 | R334,R614,R671,R691,R726,R735,R743 | residual | SIGNATURE_DIN | MD Ajay Hans signatory of results; board approval date 22-Oct-2026 |
| G03 | R718-R722,R731-R734 | residual | PERIOD_DATES | statement periods and balance sheet dates |
| G04 | R753-R754,R759-R763,R792,R800-R802,R804 | residual | TABLE_QUALIFIERS | unit, audit-status and cash flow method markers |
| G05 | R795 | residual | FOOTNOTE_UNRESOLVED | source label anomaly: consolidated TCI-to-owners row carries a Micro Enterprises dues label; values equal TCI |
| G06 | R697-R703 | residual | FORWARD | R697 website upload; R698/R701 pending warrants; R699/R702 Erisha monitoring; R700/R703 future disclosure |
