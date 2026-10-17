# A2 LEDGER: Cyient DLM Ltd (CYIENTDLM) | q2fy27 | results
Source: extracted/cyientdlm-results-q2fy27-structured.md (A1). Claim text lives at the row ID there; not re-copied.

ids_in_structured: 993 | ids_referenced_in_ledger: 993 | orphan_ids: [] | match: yes
superseded originals (accounted as superseded, not orphans): 71 = 66 one-to-one (SUPERSEDED_BY a single R6xx-R9xx row) + 5 unplaced OCI rows R176-R180 (SUPERSEDED_BY: R858-R917)

=== A2 COUNT TEST ===
category: notes            grep_count: 8     sweep_count: 8     match: yes   (grep "QUALIFIER | Note" = 8: Notes(i) cash, Note 1, 1 cont, 2, 3, 3ii, 4, 5)
category: line_items(ids)  grep_count: 862   sweep_count: 862   match: yes   (NUMBER rows 891 minus 29 non-table numbers R547-R575; grouped into 264 line-item x scope x pass groups in L1)
category: zero_standing    grep_count: 18    sweep_count: 18    match: yes   (rows tagged [ZERO_STANDING]; 23 BLANK_STANDING cells are NOT zero, listed separately)
category: agenda_items     grep_count: 3     sweep_count: 3     match: yes   (fulltext lines 34-42 show items 1-3; A1 notes say 2, see L3)
category: auditor_paras    grep_count: 9     sweep_count: 9     match: yes   (standalone 4 paras + consolidated 5 paras)
category: entities(consol) grep_count: 3     sweep_count: 3     match: yes   (Holding + 2 subsidiaries R599-R601; A1 ENTITY rows total 35 = R576-R610)
category: signature_blocks grep_count: 5     sweep_count: 5     match: yes
category: struct_counts    A1 header number=891 entity=35 forward=5 date=20 qualifier=42 (sum 993) vs sweep 891/35/5/20/42: match yes
gate_a2: pass
=== END COUNT TEST ===

## L2 NOTES (numbered notes, footnotes)
ROW_ID | note | A2 flags | note
---|---|---|---
R654 | NOTES header, p5 | - | header only
R655 | Note 1 basis of preparation, Audit Committee and Board approval | - | board date Oct 15 2026 (R626)
R656 | Note 1 cont, limited review, unmodified | - | consolidated and standalone both unmodified
R657 | Note 2 sole segment EMS (Ind AS 108); numbers R557, R558 | - | single segment, no segment table
R658 | Note 3 Other income i. net forex gain/(loss) | - | table values R534-R545 (12 cells)
R659 | Note 3 ii earnout liability fair value gain 181.95 mn (consol, Q and HY Sep-26); value R546; entity R595 | FOOTNOTE_UNRESOLVED | text gap in source line; 181.95 sits inside Q Sep-26 consolidated other income 226.15 (R690)
R660 | Note 4 OCI fair valuation decline, IP communications Company; entity R594; forward R612, R613 | FOOTNOTE_UNRESOLVED | text gap in cause sentence; OCI (a)(iii) is dash in Q Sep-26 and Q Jun-26 (ZERO_STANDING)
R661 | Note 5 BS and cash flow in Annexure 1 and 2 | - | -
R653 | Cash flow Notes (i) cash and cash equivalents components (marker R652) | - | components in L1 (p4)
Unnumbered footnotes and markers: R644 (EPS not annualised; marker R643) | R651 (truncated closing parentheses in cash flow cells) | R666 and R672 (UDIN garbled) | R641, R642, R652 (table markers to notes 3, 4, (i)) | R646, R647, R673, R676, R677 (extraction artefacts; R677: standalone HY Sep-25 expense lines foot to 3,857.85 vs printed 4,157.85, gap 300.00) | R636-R640, R645, R648-R650 (units, audit status, face value)
A1-flagged FOOTNOTE_UNRESOLVED: R659, R660, R666, R672

## L1b NON-TABLE NUMBERS (R547-R575, 29 rows)
R547-R548 scrip codes | R549-R550 Reg 29(1), Reg 30 | R551-R552 grants (10,000 RSU units; 2,63,400 ASOP options) | R553-R554 meeting start 02:00 PM, end 04:10 PM | R555-R556 Annexure -A and -B refs | R557-R559 Ind AS 108, one segment, Section 133 | R560-R562 auditor firm no., partner membership no., UDIN p6 (garbled) | R563-R565 SRE 2410, Ind AS 34, Reg 33 | R566 Reg 33(8) | R567-R569 firm no., membership no., UDIN p8 (garbled) | R570 29 years | R571-R575 phone, fax, CIN, pincodes
R546 (note 3(ii) 181.95 mn) is counted in the L1 note-3 group.

## L3 AGENDA ITEMS (Board Outcome letter p1, Annexure-B p9)
ROW_ID | agenda item | A2 flags | note
---|---|---|---
R618, R619, R555, R626 | Item 1: approve unaudited standalone and consolidated results, Q and HY ended 30-Sep-26 (Annexure -A) | - | meeting Thursday 15-Oct-26; intimation 05-Oct-26 (R617)
R580, R556, R632, R675, R614, R674 | Item 2: appoint Mr. Sandip Mishra, Senior VP and CHRO, Senior Managerial Personnel (Annexure -B); term per employment contract | - | profile rows R570, R602-R609; no pay or notice terms
R551, R552, R581, R582, R615 | Item 3: grant 10,000 Stock Units (RSU Scheme 2023) and 2,63,400 options (ASOP Scheme 2023) to associates | A1_NOTE_MISMATCH | A1 notes say 2 items; fulltext lines 34-42 show 3. Content is in A1; only A1's count is off. Vesting, exercise price, recipients not stated (R615)
R553, R554 | Meeting 02:00 PM to 04:10 PM IST (2h10m) | - | signatures 16:24:12 (R620) and 16:24:44 (R633) are after the 16:10 close; no flag
Absent from letter: AR approval, AGM notice, record date, dividend, director appointment, auditor change, scrutinizer, capital raising (absence recorded, not a row).

## L4 ANNEXURES
ROW_ID | annexure / table | flags | note
---|---|---|---
R555 | Annexure -A: P&L p2, Balance Sheet p3 (Annexure 1), Cash Flow p4 (Annexure 2) | - | line items in L1
R556, R674 | Annexure -B p9: Sl.1 reason, Sl.2 date and term (R632, R614), Sl.3 profile (R570, R602-R609), Sl.4 director relationships | MISSING_FROM_STRUCTURED (Sl.4) | see MISSING section
Director profiles: none (appointee is senior management, not a director; no DIN). Profile rows: R580 name, R570 experience, R602 Prodapt Group (latest), R603-R607 prior employers, R608-R609 education.

## L5 AUDITOR REPORTS (paragraph level)
ROW_ID | report / paragraph | flags | note
---|---|---|---
R662, R596 | Standalone p1: scope, limited review of unaudited standalone results | - | S.R. Batliboi & Associates LLP
R564, R559 | Standalone p2: management responsibility, Ind AS 34 | - | -
R563, R663, R664 | Standalone p3: SRE 2410, moderate assurance, no audit opinion | - | -
R665 | Standalone p4: conclusion, nothing came to attention | - | unmodified limited review conclusion
R667 | Consolidated p1: scope, Group limited review | - | -
R564, R565, R559 | Consolidated p2: management responsibility, Reg 33 | - | -
R563, R668, R669, R566 | Consolidated p3: SRE 2410, extra procedures per SEBI Master Circular Reg 33(8) | - | extra para vs standalone
R670, R599, R600, R601 | Consolidated p4: entity list | ENTITY_CHANGE | R601 renamed (formerly Altek Electronics Inc.); no prior ledger to diff
R671 | Consolidated p5: conclusion, no qualification | - | -
No Emphasis of Matter, Other Matters, Going Concern or unreviewed-subsidiary paragraph in either report (checked against fulltext lines 313-470). No entity declared unaudited or management-furnished.
UDINs: standalone R562/R666, consolidated R569/R672, all garbled in A1. Report dates R629, R631 (Oct 15 2026). Partner R597, R561, R568; firm R560, R567.

## L6 ENTITIES (A1 R576-R610, 35 rows)
R576-R577 exchanges | R578 issuer | R579 SEBI LODR | R580 Sandip Mishra | R581-R582 RSU/ASOP schemes | R583 S. Krithika | R584 website | R585-R586 registered office | R587-R588 signatory Rajendra Velagapudi (CEO and MD), place | R589 EMS segment | R590-R593 Audit Committee, Board, Statutory Auditors, SEBI | R594 IP communications Company (unnamed investee, impaired) | R595 earnout liability | R596-R598 auditor firm, partner, ICAI | R599-R601 consolidation list (ENTITY_CHANGE on R601 rename) | R602-R609 appointee employers and institutions | R610 address block
Consolidation: Holding Cyient DLM Limited; subsidiaries Cyient DLM Inc. (USA) and Cyient DLM Electronics Inc. (USA). Prior list not available.

## L7 SIGNATURE BLOCKS
ROW_ID | signatory | timestamp | flags
---|---|---|---
R620, R583 | S. Krithika, CS and Compliance Officer, p1 letter | 2026.10.15 16:24:12 +05:30 | none
R633, R583 | S. Krithika, Annexure-B p9 | 2026.10.15 16:24:44 +05:30 | none
R587, R588, R627 | Rajendra Velagapudi, CEO and MD, results sign-off p5 | date Oct 15 2026, no time | none
R597, R629 | Harish Khemnani, partner, standalone report p6 | date Oct 15 2026 | FOOTNOTE_UNRESOLVED (UDIN)
R597, R631 | Harish Khemnani, partner, consolidated report p8 | date Oct 15 2026 | FOOTNOTE_UNRESOLVED (UDIN)

## L8 FORWARD / DATES / QUALIFIERS (all referenced)
FORWARD R611-R615: R612 (investment value expected to improve as products launch over next few years), R613 (cause, text gap), R615 grants (vesting unstated), R614 term unspecified, R611 website.
DATES R616-R635 (20): letter, intimation, meeting, periods, signature stamps, auditor dates, appointment date, R634 "next few years", R635 meeting time.
QUALIFIERS R636-R677 (42): see L2 and L5.

## ZERO_STANDING (dash cells, 18)
OCI (a)(iii) fair valuation: R882, R883 (CONS Q Sep-26, Q Jun-26), R888, R889, R891 (STAND Q Sep-26, Q Jun-26, HY Sep-26) | OCI (b)(i) FX translation: R900, R902, R903, R904 (STAND) | OCI (b)(ii) cash flow hedge: R906, R907, R909 (CONS), R912, R913, R915 (STAND) | Standalone non-current borrowings R990, R991 (30-Sep-26, 31-Mar-26) | Standalone current borrowings 31-Mar-26 R993 (30-Sep-26 = 287.91, R992).
BLANK_STANDING (23, not zero): R885, R901, R905, R942-R946, R948-R952, R954-R958, R960-R964 (paid-up capital and other equity quarterly cells, expected blank).
R647 old text-layer blanks (standalone HY Sep-26 revenue, other income) are filled by the image transcription (R687 5,776.79 FAINT, R699 49.75 FAINT).

## MISSING_FROM_STRUCTURED
M1 | fulltext line 508 | Annexure-B Sl.4 "Disclosure of relationships between directors (in case of appointment of a director)": "Not applicable" | low materiality (appointee not a director)


## L1 LINE ITEMS (financial tables, incl. zero/dash/blank)
ROW_IDS | page | table-pass | line item | scope | n_ids | A2 flags | note
---|---|---|---|---|---|---|---
R001-R006 | p2 | first-pass | consolidated Revenue from operations | - | 6 | SUPERSEDED_ORIGINALS R002; RESTATED in R678-R993 block | line 85
R007-R011 | p2 | first-pass | standalone Revenue from operations | - | 5 | SUPERSEDED_ORIGINALS R010; RESTATED in R678-R993 block | line 85
R012-R017 | p2 | first-pass | consolidated Other income | - | 6 | SUPERSEDED_ORIGINALS R014; RESTATED in R678-R993 block | line 86
R018-R022 | p2 | first-pass | standalone Other income | - | 5 | SUPERSEDED_ORIGINALS R022; RESTATED in R678-R993 block | line 86
R023-R028 | p2 | first-pass | consolidated Total income | - | 6 | RESTATED in R678-R993 block | line 87
R029-R034 | p2 | first-pass | standalone Total income | - | 6 | RESTATED in R678-R993 block | line 87
R035-R040 | p2 | first-pass | consolidated Cost of materials consumed | - | 6 | RESTATED in R678-R993 block | line 89
R041-R046 | p2 | first-pass | standalone Cost of materials consumed | - | 6 | SUPERSEDED_ORIGINALS R041-R043,R045-R046; RESTATED in R678-R993 block | line 89
R047-R052 | p2 | first-pass | consolidated Changes in inventories of FG, stock-in-trade, WIP | - | 6 | SUPERSEDED_ORIGINALS R052; RESTATED in R678-R993 block | line 90
R053-R058 | p2 | first-pass | standalone Changes in inventories of FG, stock-in-trade, WIP | - | 6 | SUPERSEDED_ORIGINALS R053,R055-R058; RESTATED in R678-R993 block | line 90
R059-R064 | p2 | first-pass | consolidated Employee benefits expense | - | 6 | SUPERSEDED_ORIGINALS R063-R064; RESTATED in R678-R993 block | line 91
R065-R070 | p2 | first-pass | standalone Employee benefits expense | - | 6 | SUPERSEDED_ORIGINALS R065-R066,R069-R070; RESTATED in R678-R993 block | line 91
R071-R076 | p2 | first-pass | consolidated Finance costs | - | 6 | SUPERSEDED_ORIGINALS R072,R075; RESTATED in R678-R993 block | line 92
R077-R082 | p2 | first-pass | standalone Finance costs | - | 6 | SUPERSEDED_ORIGINALS R081-R082; RESTATED in R678-R993 block | line 92
R083-R088 | p2 | first-pass | consolidated Depreciation and amortisation expense | - | 6 | SUPERSEDED_ORIGINALS R085-R086; RESTATED in R678-R993 block | line 93
R089-R094 | p2 | first-pass | standalone Depreciation and amortisation expense | - | 6 | SUPERSEDED_ORIGINALS R089-R090,R093-R094; RESTATED in R678-R993 block | line 93
R095-R100 | p2 | first-pass | consolidated Other expenses | - | 6 | RESTATED in R678-R993 block | line 94
R101-R106 | p2 | first-pass | standalone Other expenses | - | 6 | SUPERSEDED_ORIGINALS R105; RESTATED in R678-R993 block | line 94
R107-R112 | p2 | first-pass | consolidated Total expenses | - | 6 | SUPERSEDED_ORIGINALS R109; RESTATED in R678-R993 block | line 95
R113-R118 | p2 | first-pass | standalone Total expenses | - | 6 | SUPERSEDED_ORIGINALS R115; RESTATED in R678-R993 block | line 95
R119-R124 | p2 | first-pass | consolidated Profit before tax | - | 6 | RESTATED in R678-R993 block | line 96
R125-R130 | p2 | first-pass | standalone Profit before tax | - | 6 | SUPERSEDED_ORIGINALS R129; RESTATED in R678-R993 block | line 96
R131-R136 | p2 | first-pass | consolidated Current tax | - | 6 | SUPERSEDED_ORIGINALS R131-R132,R136; RESTATED in R678-R993 block | line 98
R137-R141 | p2 | first-pass | standalone Current tax | - | 5 | RESTATED in R678-R993 block | line 98
R142-R147 | p2 | first-pass | consolidated Deferred tax | - | 6 | SUPERSEDED_ORIGINALS R142; RESTATED in R678-R993 block | line 99
R148-R153 | p2 | first-pass | standalone Deferred tax | - | 6 | SUPERSEDED_ORIGINALS R151,R153; RESTATED in R678-R993 block | line 99
R154-R158 | p2 | first-pass | consolidated Total tax expense | - | 5 | SUPERSEDED_ORIGINALS R157-R158; RESTATED in R678-R993 block | line 100
R159-R163 | p2 | first-pass | standalone Total tax expense | - | 5 | SUPERSEDED_ORIGINALS R159-R160; RESTATED in R678-R993 block | line 100
R164-R169 | p2 | first-pass | consolidated Net profit for the period | - | 6 | RESTATED in R678-R993 block | line 101
R170-R175 | p2 | first-pass | standalone Net profit for the period | - | 6 | SUPERSEDED_ORIGINALS R170,R174; RESTATED in R678-R993 block | line 101
R176 | p2 | first-pass | OCI remeasurement of net defined benefit liability | - | 1 | SUPERSEDED_ORIGINALS R176; RESTATED in R678-R993 block | line 104
R177 | p2 | first-pass-misc | Income tax effect on OCI remeasurement | - | 1 | SUPERSEDED_ORIGINALS R177 | line 105
R178 | p2 | first-pass-misc | Fair valuation changes on financial instruments (refer note 4) | - | 1 | SUPERSEDED_ORIGINALS R178 | line 106
R179 | p2 | first-pass-misc | Exchange differences on translating foreign operations | - | 1 | SUPERSEDED_ORIGINALS R179 | line 109
R180 | p2 | first-pass-misc | Effective portion of gain/loss on hedging instruments in cash flow hedge | - | 1 | SUPERSEDED_ORIGINALS R180 | line 110
R181-R186 | p2 | first-pass | consolidated Total other comprehensive income/(loss) | - | 6 | SUPERSEDED_ORIGINALS R182; RESTATED in R678-R993 block | line 111
R187-R192 | p2 | first-pass | standalone Total other comprehensive income/(loss) | - | 6 | SUPERSEDED_ORIGINALS R188,R191; RESTATED in R678-R993 block | line 111
R193-R198 | p2 | first-pass | consolidated Total comprehensive income/(loss) | - | 6 | SUPERSEDED_ORIGINALS R194,R196; RESTATED in R678-R993 block | line 112
R199-R204 | p2 | first-pass | standalone Total comprehensive income/(loss) | - | 6 | SUPERSEDED_ORIGINALS R199,R201-R202,R204; RESTATED in R678-R993 block | line 112
R205 | p2 | first-pass | consolidated paid up equity share capital | - | 1 | SUPERSEDED_ORIGINALS R205; RESTATED in R678-R993 block | line 113
R206 | p2 | first-pass | standalone paid up equity share capital | - | 1 | SUPERSEDED_ORIGINALS R206; RESTATED in R678-R993 block | line 113
R207 | p2 | first-pass | consolidated other equity | - | 1 | RESTATED in R678-R993 block | line 114
R208 | p2 | first-pass | standalone other equity | - | 1 | SUPERSEDED_ORIGINALS R208; RESTATED in R678-R993 block | line 114
R209 | p2 | first-pass-misc | face value per share, Rs | - | 1 | - | line 115
R210-R214 | p2 | first-pass | consolidated Basic EPS (Rs) | - | 5 | SUPERSEDED_ORIGINALS R210,R213; RESTATED in R678-R993 block | line 116
R215-R219 | p2 | first-pass | standalone Basic EPS (Rs) | - | 5 | SUPERSEDED_ORIGINALS R218; RESTATED in R678-R993 block | line 116
R220-R224 | p2 | first-pass | consolidated Diluted EPS (Rs) | - | 5 | SUPERSEDED_ORIGINALS R223; RESTATED in R678-R993 block | line 117
R225-R230 | p2 | first-pass | standalone Diluted EPS (Rs) | - | 6 | SUPERSEDED_ORIGINALS R225,R230; RESTATED in R678-R993 block | line 117
R231-R232 | p3 | first-pass | balance sheet Property, plant and equipment, consolidated | - | 2 | - | line 135
R233-R234 | p3 | first-pass | balance sheet Property, plant and equipment, standalone | - | 2 | - | line 135
R235-R236 | p3 | first-pass | balance sheet Capital work-in-progress, consolidated | - | 2 | - | line 136
R237-R238 | p3 | first-pass | balance sheet Capital work-in-progress, standalone | - | 2 | - | line 136
R239-R240 | p3 | first-pass | balance sheet Goodwill, consolidated | - | 2 | - | line 137
R241-R242 | p3 | first-pass | balance sheet Goodwill, standalone | - | 2 | - | line 137
R243-R244 | p3 | first-pass | balance sheet Other intangible assets, consolidated | - | 2 | - | line 138
R245-R246 | p3 | first-pass | balance sheet Other intangible assets, standalone | - | 2 | - | line 138
R247-R248 | p3 | first-pass | balance sheet Right of use assets, consolidated | - | 2 | - | line 139
R249-R250 | p3 | first-pass | balance sheet Right of use assets, standalone | - | 2 | - | line 139
R251-R252 | p3 | first-pass | balance sheet Non-current investments, consolidated | - | 2 | - | line 141
R253-R254 | p3 | first-pass | balance sheet Non-current investments, standalone | - | 2 | - | line 141
R255-R256 | p3 | first-pass | balance sheet Other non-current financial assets, consolidated | - | 2 | - | line 142
R257-R258 | p3 | first-pass | balance sheet Other non-current financial assets, standalone | - | 2 | - | line 142
R259-R260 | p3 | first-pass | balance sheet Deferred tax assets (net), consolidated | - | 2 | - | line 143
R261-R262 | p3 | first-pass | balance sheet Deferred tax assets (net), standalone | - | 2 | - | line 143
R263-R264 | p3 | first-pass | balance sheet Other non-current assets, consolidated | - | 2 | - | line 144
R265-R266 | p3 | first-pass | balance sheet Other non-current assets, standalone | - | 2 | - | line 144
R267-R268 | p3 | first-pass | balance sheet Total non-current assets, consolidated | - | 2 | - | line 145
R269-R270 | p3 | first-pass | balance sheet Total non-current assets, standalone | - | 2 | - | line 145
R271-R272 | p3 | first-pass | balance sheet Inventories, consolidated | - | 2 | - | line 148
R273-R274 | p3 | first-pass | balance sheet Inventories, standalone | - | 2 | - | line 148
R275-R276 | p3 | first-pass | balance sheet Contract assets, consolidated | - | 2 | - | line 149
R277-R278 | p3 | first-pass | balance sheet Contract assets, standalone | - | 2 | - | line 149
R279 | p3 | first-pass | balance sheet Current investments, consolidated | - | 1 | - | line 151
R280 | p3 | first-pass | balance sheet Current investments, standalone | - | 1 | - | line 151
R281-R282 | p3 | first-pass | balance sheet Trade receivables, consolidated | - | 2 | - | line 152
R283-R284 | p3 | first-pass | balance sheet Trade receivables, standalone | - | 2 | - | line 152
R285-R286 | p3 | first-pass | balance sheet Cash and cash equivalents, consolidated | - | 2 | - | line 153
R287-R288 | p3 | first-pass | balance sheet Cash and cash equivalents, standalone | - | 2 | - | line 153
R289-R290 | p3 | first-pass | balance sheet Other bank balances, consolidated | - | 2 | - | line 154
R291-R292 | p3 | first-pass | balance sheet Other bank balances, standalone | - | 2 | - | line 154
R293-R294 | p3 | first-pass | balance sheet Other current financial assets, consolidated | - | 2 | - | line 155
R295-R296 | p3 | first-pass | balance sheet Other current financial assets, standalone | - | 2 | - | line 155
R297-R298 | p3 | first-pass | balance sheet Other current assets, consolidated | - | 2 | - | line 156
R299-R300 | p3 | first-pass | balance sheet Other current assets, standalone | - | 2 | - | line 156
R301-R302 | p3 | first-pass | balance sheet Total current assets, consolidated | - | 2 | - | line 157
R303-R304 | p3 | first-pass | balance sheet Total current assets, standalone | - | 2 | - | line 157
R305-R306 | p3 | first-pass | balance sheet Total assets, consolidated | - | 2 | - | line 159
R307-R308 | p3 | first-pass | balance sheet Total assets, standalone | - | 2 | - | line 159
R309-R310 | p3 | first-pass | balance sheet Equity share capital, consolidated | - | 2 | - | line 163
R311-R312 | p3 | first-pass | balance sheet Equity share capital, standalone | - | 2 | - | line 163
R313-R314 | p3 | first-pass | balance sheet Other equity, consolidated | - | 2 | - | line 164
R315-R316 | p3 | first-pass | balance sheet Other equity, standalone | - | 2 | - | line 164
R317-R318 | p3 | first-pass | balance sheet Total equity, consolidated | - | 2 | - | line 165
R319-R320 | p3 | first-pass | balance sheet Total equity, standalone | - | 2 | - | line 165
R321-R322 | p3 | first-pass | balance sheet Non-current borrowings, consolidated | - | 2 | - | line 170
R323-R324 | p3 | first-pass | balance sheet Non-current lease liabilities, consolidated | - | 2 | - | line 171
R325-R326 | p3 | first-pass | balance sheet Non-current lease liabilities, standalone | - | 2 | - | line 171
R327-R328 | p3 | first-pass | balance sheet Non-current provisions, consolidated | - | 2 | - | line 172
R329-R330 | p3 | first-pass | balance sheet Non-current provisions, standalone | - | 2 | - | line 172
R331-R332 | p3 | first-pass | balance sheet Total non-current liabilities, consolidated | - | 2 | - | line 173
R333-R334 | p3 | first-pass | balance sheet Total non-current liabilities, standalone | - | 2 | - | line 173
R335-R336 | p3 | first-pass | balance sheet Current borrowings, consolidated | - | 2 | - | line 177
R337 | p3 | first-pass | balance sheet Current borrowings, standalone | - | 1 | SUPERSEDED_ORIGINALS R337 | line 177
R338-R339 | p3 | first-pass | balance sheet Current lease liabilities, consolidated | - | 2 | - | line 178
R340-R341 | p3 | first-pass | balance sheet Current lease liabilities, standalone | - | 2 | - | line 178
R342-R343 | p3 | first-pass | balance sheet Trade payables MSME, consolidated | - | 2 | - | line 180
R344-R345 | p3 | first-pass | balance sheet Trade payables MSME, standalone | - | 2 | - | line 180
R346-R347 | p3 | first-pass | balance sheet Trade payables other than MSME, consolidated | - | 2 | - | line 181
R348-R349 | p3 | first-pass | balance sheet Trade payables other than MSME, standalone | - | 2 | - | line 181
R350-R351 | p3 | first-pass | balance sheet Other current financial liabilities, consolidated | - | 2 | - | line 183
R352-R353 | p3 | first-pass | balance sheet Other current financial liabilities, standalone | - | 2 | - | line 183
R354-R355 | p3 | first-pass | balance sheet Other current liabilities, consolidated | - | 2 | - | line 184
R356-R357 | p3 | first-pass | balance sheet Other current liabilities, standalone | - | 2 | - | line 184
R358-R359 | p3 | first-pass | balance sheet Current provisions, consolidated | - | 2 | - | line 185
R360-R361 | p3 | first-pass | balance sheet Current provisions, standalone | - | 2 | - | line 185
R362-R363 | p3 | first-pass | balance sheet Income tax liabilities (net), consolidated | - | 2 | - | line 186
R364-R365 | p3 | first-pass | balance sheet Income tax liabilities (net), standalone | - | 2 | - | line 186
R366-R367 | p3 | first-pass | balance sheet Total current liabilities, consolidated | - | 2 | - | line 187
R368-R369 | p3 | first-pass | balance sheet Total current liabilities, standalone | - | 2 | - | line 187
R370-R371 | p3 | first-pass | balance sheet Total liabilities, consolidated | - | 2 | - | line 189
R372-R373 | p3 | first-pass | balance sheet Total liabilities, standalone | - | 2 | - | line 189
R374-R375 | p3 | first-pass | balance sheet Total equity and liabilities, consolidated | - | 2 | - | line 190
R376-R377 | p3 | first-pass | balance sheet Total equity and liabilities, standalone | - | 2 | - | line 190
R378-R379 | p4 | first-pass | cash flow Profit before tax, consolidated | - | 2 | - | line 206
R380-R381 | p4 | first-pass | cash flow Profit before tax, standalone | - | 2 | - | line 206
R382-R383 | p4 | first-pass | cash flow Depreciation and amortisation, consolidated | - | 2 | - | line 208
R384-R385 | p4 | first-pass | cash flow Depreciation and amortisation, standalone | - | 2 | - | line 208
R386 | p4 | first-pass | cash flow Loss on disposal of PPE (net), consolidated | - | 1 | - | line 209
R387-R388 | p4 | first-pass | cash flow Net unrealised exchange loss/(gain), consolidated | - | 2 | - | line 210
R389-R390 | p4 | first-pass | cash flow Net unrealised exchange loss/(gain), standalone | - | 2 | - | line 210
R391-R392 | p4 | first-pass | cash flow Finance costs, consolidated | - | 2 | - | line 211
R393-R394 | p4 | first-pass | cash flow Finance costs, standalone | - | 2 | - | line 211
R395-R396 | p4 | first-pass | cash flow Interest income, consolidated | - | 2 | - | line 212
R397-R398 | p4 | first-pass | cash flow Interest income, standalone | - | 2 | - | line 212
R399-R400 | p4 | first-pass | cash flow Gain on fair valuation of financial liability, consolidated | - | 2 | - | line 213
R401-R402 | p4 | first-pass | cash flow Share based payment expenses, consolidated | - | 2 | - | line 214
R403-R404 | p4 | first-pass | cash flow Share based payment expenses, standalone | - | 2 | - | line 214
R405 | p4 | first-pass | cash flow Dividend from mutual funds, consolidated | - | 1 | - | line 215
R406 | p4 | first-pass | cash flow Dividend from mutual funds, standalone | - | 1 | - | line 215
R407-R408 | p4 | first-pass | cash flow Provision for expected credit loss (net of write-off), consolidated | - | 2 | - | line 216
R409-R410 | p4 | first-pass | cash flow Provision for expected credit loss (net of write-off), standalone | - | 2 | - | line 216
R411-R412 | p4 | first-pass | cash flow Operating profit before working capital changes, consolidated | - | 2 | - | line 217
R413-R414 | p4 | first-pass | cash flow Operating profit before working capital changes, standalone | - | 2 | - | line 217
R415-R416 | p4 | first-pass | cash flow WC change trade receivables, consolidated | - | 2 | - | line 220
R417-R418 | p4 | first-pass | cash flow WC change trade receivables, standalone | - | 2 | - | line 220
R419-R420 | p4 | first-pass | cash flow WC change inventories, consolidated | - | 2 | - | line 221
R421-R422 | p4 | first-pass | cash flow WC change inventories, standalone | - | 2 | - | line 221
R423-R424 | p4 | first-pass | cash flow WC change contract assets, consolidated | - | 2 | - | line 222
R425-R426 | p4 | first-pass | cash flow WC change contract assets, standalone | - | 2 | - | line 222
R427-R428 | p4 | first-pass | cash flow WC change other assets and other financial assets, consolidated | - | 2 | - | line 223
R429-R430 | p4 | first-pass | cash flow WC change other assets and other financial assets, standalone | - | 2 | - | line 223
R431-R432 | p4 | first-pass | cash flow WC change trade payables, consolidated | - | 2 | - | line 225
R433-R434 | p4 | first-pass | cash flow WC change trade payables, standalone | - | 2 | - | line 225
R435-R436 | p4 | first-pass | cash flow WC change provisions and other liabilities, consolidated | - | 2 | - | line 226
R437-R438 | p4 | first-pass | cash flow WC change provisions and other liabilities, standalone | - | 2 | - | line 226
R439-R440 | p4 | first-pass | cash flow Cash generated from/(used in) operations, consolidated | - | 2 | - | line 227
R441-R442 | p4 | first-pass | cash flow Cash generated from/(used in) operations, standalone | - | 2 | - | line 227
R443-R444 | p4 | first-pass | cash flow Income taxes paid, consolidated | - | 2 | - | line 228
R445-R446 | p4 | first-pass | cash flow Income taxes paid, standalone | - | 2 | - | line 228
R447-R448 | p4 | first-pass | cash flow Net cash from operating activities (A), consolidated | - | 2 | - | line 229
R449-R450 | p4 | first-pass | cash flow Net cash from operating activities (A), standalone | - | 2 | - | line 229
R451 | p4 | first-pass | cash flow Loan repaid by subsidiary, standalone | - | 1 | - | line 232
R452 | p4 | first-pass | cash flow Payment towards acquisition of business, consolidated | - | 1 | - | line 233
R453-R454 | p4 | first-pass | cash flow Payment for purchase of PPE and intangibles, consolidated | - | 2 | - | line 234
R455-R456 | p4 | first-pass | cash flow Payment for purchase of PPE and intangibles, standalone | - | 2 | - | line 234
R457 | p4 | first-pass | cash flow Proceeds from sale of mutual fund investments, consolidated | - | 1 | - | line 235
R458 | p4 | first-pass | cash flow Proceeds from sale of mutual fund investments, standalone | - | 1 | - | line 235
R459-R460 | p4 | first-pass | cash flow Investment in deposits, consolidated | - | 2 | - | line 236
R461-R462 | p4 | first-pass | cash flow Investment in deposits, standalone | - | 2 | - | line 236
R463-R464 | p4 | first-pass | cash flow Proceeds from maturity/withdrawal of deposits, consolidated | - | 2 | - | line 237
R465-R466 | p4 | first-pass | cash flow Proceeds from maturity/withdrawal of deposits, standalone | - | 2 | - | line 237
R467-R468 | p4 | first-pass | cash flow Interest received, consolidated | - | 2 | - | line 238
R469-R470 | p4 | first-pass | cash flow Interest received, standalone | - | 2 | - | line 238
R471-R472 | p4 | first-pass | cash flow Net cash (used in)/from investing activities (B), consolidated | - | 2 | - | line 239
R473-R474 | p4 | first-pass | cash flow Net cash (used in)/from investing activities (B), standalone | - | 2 | - | line 239
R475-R476 | p4 | first-pass | cash flow Proceeds from shares issued on exercise of options, consolidated | - | 2 | - | line 242
R477-R478 | p4 | first-pass | cash flow Proceeds from shares issued on exercise of options, standalone | - | 2 | - | line 242
R479-R480 | p4 | first-pass | cash flow Proceeds from current borrowings, consolidated | - | 2 | - | line 243
R481-R482 | p4 | first-pass | cash flow Proceeds from current borrowings, standalone | - | 2 | - | line 243
R483 | p4 | first-pass | cash flow Repayments of current borrowings, consolidated | - | 1 | - | line 244
R484 | p4 | first-pass | cash flow Repayments of current borrowings, standalone | - | 1 | - | line 244
R485-R486 | p4 | first-pass | cash flow Repayments of non current borrowings, consolidated | - | 2 | - | line 245
R487 | p4 | first-pass | cash flow Repayments of non current borrowings, standalone | - | 1 | - | line 245
R488-R489 | p4 | first-pass | cash flow Payment of principal portion of lease liabilities, consolidated | - | 2 | - | line 246
R490-R491 | p4 | first-pass | cash flow Payment of principal portion of lease liabilities, standalone | - | 2 | - | line 246
R492-R493 | p4 | first-pass | cash flow Payment of interest portion of lease liabilities, consolidated | - | 2 | - | line 247
R494-R495 | p4 | first-pass | cash flow Payment of interest portion of lease liabilities, standalone | - | 2 | - | line 247
R496-R497 | p4 | first-pass | cash flow Interest paid, consolidated | - | 2 | - | line 248
R498-R499 | p4 | first-pass | cash flow Interest paid, standalone | - | 2 | - | line 248
R500-R501 | p4 | first-pass | cash flow Net cash (used in)/from financing activities (C), consolidated | - | 2 | - | line 249
R502-R503 | p4 | first-pass | cash flow Net cash (used in)/from financing activities (C), standalone | - | 2 | - | line 249
R504-R505 | p4 | first-pass | cash flow Net increase/(decrease) in cash (A+B+C), consolidated | - | 2 | - | line 251
R506-R507 | p4 | first-pass | cash flow Net increase/(decrease) in cash (A+B+C), standalone | - | 2 | - | line 251
R508-R509 | p4 | first-pass | cash flow Cash at beginning of period, consolidated | - | 2 | - | line 252
R510-R511 | p4 | first-pass | cash flow Cash at beginning of period, standalone | - | 2 | - | line 252
R512-R513 | p4 | first-pass | cash flow Effect of exchange differences on cash, consolidated | - | 2 | - | line 253
R514-R515 | p4 | first-pass | cash flow Effect of exchange differences on cash, standalone | - | 2 | - | line 253
R516-R517 | p4 | first-pass | cash flow Cash at end of period, consolidated | - | 2 | - | line 254
R518-R519 | p4 | first-pass | cash flow Cash at end of period, standalone | - | 2 | - | line 254
R520-R521 | p4 | first-pass | cash flow Cash comprises balances with banks in current accounts, consolidated | - | 2 | - | line 259
R522-R523 | p4 | first-pass | cash flow Cash comprises balances with banks in current accounts, standalone | - | 2 | - | line 259
R524 | p4 | first-pass | cash flow Cash comprises term deposits (original maturity <3 months), consolidated | - | 1 | - | line 260
R525 | p4 | first-pass | cash flow Cash comprises term deposits (original maturity <3 months), standalone | - | 1 | - | line 260
R526-R527 | p4 | first-pass | cash flow Cash comprises cash on hand, consolidated | - | 2 | - | line 261
R528-R529 | p4 | first-pass | cash flow Cash comprises cash on hand, standalone | - | 2 | - | line 261
R530-R531 | p4 | first-pass | cash flow Cash comprises total, consolidated | - | 2 | - | line 262
R532-R533 | p4 | first-pass | cash flow Cash comprises total, standalone | - | 2 | - | line 262
R534-R539 | p5 | first-pass | note 3(i) net forex gain/(loss) standalone | - | 6 | - | line 285
R540-R545 | p5 | first-pass | note 3(i) net forex gain/(loss) consolidated | - | 6 | - | line 286
R546 | p5 | first-pass | note 3(ii) gain on fair valuation of earnout liability, consolidated Q and HY Sep-26 | - | 1 | - | line 288
R678-R683 | p2 | transcription | Revenue from operations | CONS | 6 | - | line 538
R684-R689 | p2 | transcription | Revenue from operations | STAND | 6 | A1:FAINT/PARTIAL_LEGIBILITY | line 538
R690-R695 | p2 | transcription | Other income (refer note 3) | CONS | 6 | - | line 539
R696-R701 | p2 | transcription | Other income (refer note 3) | STAND | 6 | A1:FAINT | line 539
R702-R707 | p2 | transcription | Total income | CONS | 6 | - | line 540
R708-R713 | p2 | transcription | Total income | STAND | 6 | A1:PARTIAL_LEGIBILITY | line 540
R714-R719 | p2 | transcription | Cost of materials consumed | CONS | 6 | - | line 541
R720-R725 | p2 | transcription | Cost of materials consumed | STAND | 6 | A1:PARTIAL_LEGIBILITY | line 541
R726-R731 | p2 | transcription | Changes in inventories of FG, stock-in-trade and WIP | CONS | 6 | - | line 542
R732-R737 | p2 | transcription | Changes in inventories of FG, stock-in-trade and WIP | STAND | 6 | - | line 542
R738-R743 | p2 | transcription | Employee benefits expense | CONS | 6 | - | line 543
R744-R749 | p2 | transcription | Employee benefits expense | STAND | 6 | A1:PARTIAL_LEGIBILITY | line 543
R750-R755 | p2 | transcription | Finance costs | CONS | 6 | - | line 544
R756-R761 | p2 | transcription | Finance costs | STAND | 6 | - | line 544
R762-R767 | p2 | transcription | Depreciation and amortisation expense | CONS | 6 | - | line 545
R768-R773 | p2 | transcription | Depreciation and amortisation expense | STAND | 6 | - | line 545
R774-R779 | p2 | transcription | Other expenses | CONS | 6 | - | line 546
R780-R785 | p2 | transcription | Other expenses | STAND | 6 | A1:PARTIAL_LEGIBILITY | line 546
R786-R791 | p2 | transcription | Total expenses | CONS | 6 | - | line 547
R792-R797 | p2 | transcription | Total expenses | STAND | 6 | - | line 547
R798-R803 | p2 | transcription | Profit before tax (1-2) | CONS | 6 | - | line 548
R804-R809 | p2 | transcription | Profit before tax (1-2) | STAND | 6 | A1:PARTIAL_LEGIBILITY | line 548
R810-R815 | p2 | transcription | Current tax | CONS | 6 | - | line 549
R816-R821 | p2 | transcription | Current tax | STAND | 6 | A1:FAINT | line 549
R822-R827 | p2 | transcription | Deferred tax | CONS | 6 | - | line 550
R828-R833 | p2 | transcription | Deferred tax | STAND | 6 | - | line 550
R834-R839 | p2 | transcription | Total tax expense | CONS | 6 | A1:FAINT | line 551
R840-R845 | p2 | transcription | Total tax expense | STAND | 6 | A1:FAINT | line 551
R846-R851 | p2 | transcription | Net profit for the period/year (3-4) | CONS | 6 | - | line 552
R852-R857 | p2 | transcription | Net profit for the period/year (3-4) | STAND | 6 | A1:PARTIAL_LEGIBILITY | line 552
R858-R863 | p2 | transcription | OCI (a)(i) Remeasurements of net defined benefit liability | CONS | 6 | A1:FAINT | line 553
R864-R869 | p2 | transcription | OCI (a)(i) Remeasurements of net defined benefit liability | STAND | 6 | - | line 553
R870-R875 | p2 | transcription | OCI (a)(ii) Income tax effect on above | CONS | 6 | - | line 554
R876-R881 | p2 | transcription | OCI (a)(ii) Income tax effect on above | STAND | 6 | - | line 554
R882-R887 | p2 | transcription | OCI (a)(iii) Fair valuation changes on financial instruments (refer note 4) | CONS | 6 | ZERO_STANDING(partial: R882-R883); BLANK_STANDING(not zero; R885) | line 555
R888-R893 | p2 | transcription | OCI (a)(iii) Fair valuation changes on financial instruments (refer note 4) | STAND | 6 | ZERO_STANDING(partial: R888-R889,R891); A1:PARTIAL_LEGIBILITY | line 555
R894-R899 | p2 | transcription | OCI (b)(i) Exchange differences in translating foreign operations | CONS | 6 | A1:FAINT | line 556
R900-R905 | p2 | transcription | OCI (b)(i) Exchange differences in translating foreign operations | STAND | 6 | ZERO_STANDING(partial: R900,R902-R904); BLANK_STANDING(not zero; R901,R905) | line 556
R906-R911 | p2 | transcription | OCI (b)(ii) Effective portion of gain/(loss) on hedging instruments in cash flow hedge | CONS | 6 | ZERO_STANDING(partial: R906-R907,R909) | line 557
R912-R917 | p2 | transcription | OCI (b)(ii) Effective portion of gain/(loss) on hedging instruments in cash flow hedge | STAND | 6 | ZERO_STANDING(partial: R912-R913,R915); A1:FAINT | line 557
R918-R923 | p2 | transcription | Total other comprehensive income/(loss) | CONS | 6 | - | line 558
R924-R929 | p2 | transcription | Total other comprehensive income/(loss) | STAND | 6 | A1:PARTIAL_LEGIBILITY | line 558
R930-R935 | p2 | transcription | Total comprehensive income/(loss) (5+6) | CONS | 6 | - | line 559
R936-R941 | p2 | transcription | Total comprehensive income/(loss) (5+6) | STAND | 6 | - | line 559
R942-R947 | p2 | transcription | Paid up equity share capital | CONS | 6 | BLANK_STANDING(not zero; R942-R946) | line 560
R948-R953 | p2 | transcription | Paid up equity share capital | STAND | 6 | BLANK_STANDING(not zero; R948-R952) | line 560
R954-R959 | p2 | transcription | Other equity | CONS | 6 | BLANK_STANDING(not zero; R954-R958) | line 561
R960-R965 | p2 | transcription | Other equity | STAND | 6 | BLANK_STANDING(not zero; R960-R964) | line 561
R966-R971 | p2 | transcription | EPS (a) Basic (Rs) | CONS | 6 | A1:FAINT | line 562
R972-R977 | p2 | transcription | EPS (a) Basic (Rs) | STAND | 6 | A1:FAINT | line 562
R978-R983 | p2 | transcription | EPS (b) Diluted (Rs) | CONS | 6 | A1:FAINT | line 563
R984-R989 | p2 | transcription | EPS (b) Diluted (Rs) | STAND | 6 | - | line 563
R990-R991 | p3 | transcription | Standalone non-current borrowings | - | 2 | ZERO_STANDING | line 565
R992-R993 | p3 | transcription | Standalone current borrowings | - | 2 | ZERO_STANDING(partial: R993) | line 565