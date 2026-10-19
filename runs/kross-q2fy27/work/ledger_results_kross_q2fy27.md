# LEDGER results KROSS Q2 FY27 (standalone, Rs Millions)
ids_in_structured: 372 | ids_referenced_in_ledger: 372 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: notes          grep_count: 7    sweep_count: 7    match: yes (plus 2 footnotes R059, R060)
category: line_items     grep_count: 304  sweep_count: 304  match: yes (24 P&L x6 + 35 BS x2 + 45 CF x2 metrics-periods; 104 metrics)
category: zero_standing  grep_count: 18   sweep_count: 18   match: yes
category: agenda_items   grep_count: 2    sweep_count: 2    match: yes
category: auditor_paras  grep_count: 4    sweep_count: 4    match: yes
category: entities       grep_count: 0    sweep_count: 0    match: yes (standalone, no subsidiaries)
category: superseded_ids grep_count: 21   sweep_count: 21   match: yes (R008-R027, R030; R068 RESOLVED)
gate_a2: pass
=== END COUNT TEST ===

## 1. NOTES (grep_count 7 numbered; sweep 7; no unnumbered notes or footnote symbols beyond R059 '* Not Annualised')
ROW_ID | category | flags | note
--|--|--|--
R061 | note 1 |  | Note 1 (audit committee/board approval, unmodified review conclusion)
R062 | note 2 |  | Note 2 (Ind AS basis)
R063 R039 | note 3 |  | Note 3 (single segment)
R044 R029 R028 R043 R052 R053 R040 | note 4 | FORWARD; pending exchange approval; dilution item | Note 4 (preferential issue 15,00,000 shares + 15,00,000 warrants; board 31-Aug, postal ballot 30-Sep; in-principle approval pending)
R064 R042 | note 5 |  | Note 5 (no subsidiary/associate/JV)
R065 | note 6 | possible restatement; see footing gap | Note 6 (regrouped/restated comparatives)
R045 | note 7 |  | Note 7 (results on website)
R059 | footnote | | '* Not Annualised' EPS
R060 | footnote | | Total income definition under table

## 2. LINE ITEMS (every table line; atomic metric x period rows)
ROW_ID range | category | flags | metric (page/line from A1 row)
--|--|--|--
R069-R074 (6) | line item |  | p4 L412 P&L (1) Revenue from operations
R075-R080 (6) | line item |  | p4 L413 P&L (2) Other income
R081-R086 (6) | line item |  | p4 L414 P&L (3) Total Income
R087-R092 (6) | line item |  | p4 L415 P&L (4a) Cost of materials consumed
R093-R098 (6) | line item |  | p4 L416 P&L (4b) Changes in inventories of FG and WIP
R099-R104 (6) | line item |  | p4 L417 P&L (4c) Employee benefits expense
R105-R110 (6) | line item |  | p4 L418 P&L (4d) Finance costs
R111-R116 (6) | line item |  | p4 L419 P&L (4e) Depreciation and amortisation expense
R117-R122 (6) | line item |  | p4 L420 P&L (4f) Other expense
R123-R128 (6) | line item |  | p4 L421 P&L Total Expenses (4)
R129-R134 (6) | line item |  | p4 L422 P&L (5) Profit before tax
R135-R140 (6) | line item |  | p4 L423 P&L (6a)(i) Current tax
R141-R146 (6) | line item | ZERO_STANDING on R141,R142,R144 | p4 L424 P&L (6a)(ii) Current tax for earlier years
R147-R152 (6) | line item |  | p4 L425 P&L (6b) Deferred tax
R153-R158 (6) | line item |  | p4 L426 P&L Total Tax Expense (6)
R159-R164 (6) | line item |  | p4 L427 P&L (7) Profit for the period/year
R165-R170 (6) | line item |  | p4 L428 P&L (8a) OCI remeasurement of defined benefit plans
R171-R176 (6) | line item |  | p4 L429 P&L (8b) OCI income tax on above
R177-R182 (6) | line item |  | p4 L430 P&L Total other comprehensive income (8)
R183-R188 (6) | line item |  | p4 L431 P&L (9) Total comprehensive income
R189-R194 (6) | line item |  | p4 L432 P&L (10) EPS Basic (Rs, quarter/half not annualised)
R195-R200 (6) | line item |  | p4 L433 P&L (10) EPS Diluted (Rs, quarter/half not annualised)
R201-R206 (6) | line item |  | p4 L434 P&L (11) Paid up equity share capital (FV Rs 5)
R207-R212 (6) | line item | ZERO_STANDING on R207,R208,R209,R210,R211 | p4 L435 P&L (12) Other Equity
R213-R214 (2) | line item |  | p6 L438 BS NCA (1a) Property, plant and equipment
R215-R216 (2) | line item |  | p6 L439 BS NCA (1b) Capital work in progress
R217-R218 (2) | line item |  | p6 L440 BS NCA (1c) Right of use assets
R219-R220 (2) | line item |  | p6 L441 BS NCA (1d) Other intangible assets
R221-R222 (2) | line item |  | p6 L442 BS NCA (1e)(i) Non-current investments
R223-R224 (2) | line item |  | p6 L443 BS NCA (1e)(ii) Other non-current financial assets
R225-R226 (2) | line item |  | p6 L444 BS NCA (1f) Other non-current assets
R227-R228 (2) | line item |  | p6 L445 BS Total Non-current assets
R229-R230 (2) | line item |  | p6 L446 BS CA (2a) Inventories
R231-R232 (2) | line item |  | p6 L447 BS CA (2b)(i) Current investments
R233-R234 (2) | line item |  | p6 L448 BS CA (2b)(ii) Trade receivables
R235-R236 (2) | line item |  | p6 L449 BS CA (2b)(iii) Cash and cash equivalents
R237-R238 (2) | line item |  | p6 L450 BS CA (2b)(iv) Other bank balance
R239-R240 (2) | line item |  | p6 L451 BS CA (2b)(v) Other current financial assets
R241-R242 (2) | line item |  | p6 L452 BS CA (2c) Other current assets
R243-R244 (2) | line item |  | p6 L453 BS Total current assets
R245-R246 (2) | line item |  | p6 L454 BS Total Assets [1+2]
R247-R248 (2) | line item |  | p6 L455 BS EQ (1a) Equity share capital
R249-R250 (2) | line item |  | p6 L456 BS EQ (1b) Other equity
R251-R252 (2) | line item |  | p6 L457 BS Total equity
R253-R254 (2) | line item |  | p6 L458 BS NCL (2a)(i) Borrowings
R255-R256 (2) | line item |  | p6 L459 BS NCL (2a)(ii) Lease liabilities
R257-R258 (2) | line item |  | p6 L460 BS NCL (2b) Long-term provisions
R259-R260 (2) | line item |  | p6 L461 BS NCL (2c) Deferred tax liabilities (Net)
R261-R262 (2) | line item |  | p6 L462 BS Total Non-current liabilities
R263-R264 (2) | line item |  | p6 L463 BS CL (3a)(i) Borrowings
R265-R266 (2) | line item |  | p6 L464 BS CL (3a)(ii) Lease liabilities
R267-R268 (2) | line item |  | p6 L465 BS CL (3a)(iii) Trade payables: micro and small enterprises
R269-R270 (2) | line item |  | p6 L466 BS CL (3a)(iii) Trade payables: other than micro and small
R271-R272 (2) | line item |  | p6 L467 BS CL (3a)(iv) Other financial liabilities
R273-R274 (2) | line item |  | p6 L468 BS CL (3b) Other current liabilities
R275-R276 (2) | line item |  | p6 L469 BS CL (3c) Short-term provisions
R277-R278 (2) | line item |  | p6 L470 BS CL (3d) Current tax liabilities (Net)
R279-R280 (2) | line item |  | p6 L471 BS Total current liabilities
R281-R282 (2) | line item |  | p6 L472 BS Total Equity and Liabilities [1+2+3]
R283-R284 (2) | line item |  | p7 L475 CF (A) Profit before tax
R285-R286 (2) | line item |  | p7 L476 CF Depreciation and amortization expense
R287-R288 (2) | line item |  | p7 L477 CF Finance costs
R289-R290 (2) | line item | ZERO_STANDING on R289,R290 | p7 L478 CF Allowances for expected credit loss
R291-R292 (2) | line item |  | p7 L479 CF Unwinding of interest on long term security deposit
R293-R294 (2) | line item |  | p7 L480 CF Net fair value gains on financial assets at FVTPL
R295-R296 (2) | line item | ZERO_STANDING on R295 | p7 L481 CF (Profit)/Loss on sale of PPE
R297-R298 (2) | line item | ZERO_STANDING on R297 | p7 L482 CF (Profit)/Loss on revocation of RoU
R299-R300 (2) | line item |  | p7 L483 CF Interest Income
R301-R302 (2) | line item |  | p7 L484 CF Operating profit before changes in assets and liabilities
R303-R304 (2) | line item |  | p7 L485 CF (Inc)/Dec in Inventories
R305-R306 (2) | line item |  | p7 L486 CF (Inc)/Dec in Other non-current financial assets
R307-R308 (2) | line item |  | p7 L487 CF (Inc)/Dec in Trade receivables
R309-R310 (2) | line item |  | p7 L488 CF (Inc)/Dec in Other current financial assets
R311-R312 (2) | line item |  | p7 L489 CF (Inc)/Dec in Other current assets
R313-R314 (2) | line item |  | p7 L490 CF Inc/(Dec) in Provisions
R315-R316 (2) | line item |  | p7 L491 CF Inc/(Dec) in Trade payables
R317-R318 (2) | line item |  | p7 L492 CF Inc/(Dec) in Other current financial liabilities
R319-R320 (2) | line item |  | p7 L493 CF Inc/(Dec) in Other current liabilities
R321-R322 (2) | line item |  | p7 L494 CF Cash generated from/(used in) operations
R323-R324 (2) | line item |  | p7 L495 CF Direct Taxes Paid
R325-R326 (2) | line item |  | p7 L496 CF Net cash flow from operating activities
R327-R328 (2) | line item |  | p7 L497 CF (B) Purchase of PPE (including CWIP)
R329-R330 (2) | line item |  | p7 L498 CF Purchase of Intangible assets (incl. RoU)
R331-R332 (2) | line item | ZERO_STANDING on R331 | p7 L499 CF Proceeds from sale of PPE
R333-R334 (2) | line item |  | p7 L500 CF (Inc)/Dec in Other non current assets
R335-R336 (2) | line item |  | p7 L501 CF Interest Received
R337-R338 (2) | line item |  | p7 L502 CF Term deposits (placed)/matured (net)
R339-R340 (2) | line item | ZERO_STANDING on R339,R340 | p7 L503 CF Investment in shares
R341-R342 (2) | line item |  | p7 L504 CF Investment in mutual fund
R343-R344 (2) | line item |  | p7 L505 CF Net cash flow from investing activities
R345-R346 (2) | line item |  | p7 L506 CF (C) Proceeds from Long-term borrowings
R347-R348 (2) | line item | ZERO_STANDING on R347 | p7 L507 CF Repayment of Long-term borrowings
R349-R350 (2) | line item |  | p7 L508 CF Proceeds from/(repayment of) short-term borrowings (net)
R351-R352 (2) | line item | ZERO_STANDING on R351,R352 | p7 L509 CF Proceeds from initial public offering
R353-R354 (2) | line item |  | p7 L510 CF Increase in lease liabilities
R355-R356 (2) | line item |  | p7 L511 CF Other interest payments
R357-R358 (2) | line item |  | p7 L512 CF Net cash flow from financing activities
R359-R360 (2) | line item |  | p7 L513 CF Net increase/(decrease) in cash and cash equivalents (A+B+C)
R361-R362 (2) | line item |  | p7 L514 CF Cash and cash equivalents at beginning of period
R363-R364 (2) | line item |  | p7 L515 CF Cash and cash equivalents at end of period
R365-R366 (2) | line item |  | p7 L516 CF Components: Cash in hand
R367-R368 (2) | line item |  | p7 L517 CF Components: Balances with bank in current accounts
R369-R370 (2) | line item |  | p7 L518 CF Components: Balances with bank in deposit accounts
R371-R372 (2) | line item |  | p7 L519 CF Components: Total

## 2a. ZERO_STANDING rows (18)
ROW_ID | flag | materiality
--|--|--
R141 | ZERO_STANDING | P&L (6a)(ii) Current tax for earlier years, Q2 FY27
R142 | ZERO_STANDING | P&L (6a)(ii) Current tax for earlier years, Q1 FY27
R144 | ZERO_STANDING | P&L (6a)(ii) Current tax for earlier years, H1 FY27
R207 | ZERO_STANDING | P&L (12) Other Equity, Q2 FY27
R208 | ZERO_STANDING | P&L (12) Other Equity, Q1 FY27
R209 | ZERO_STANDING | P&L (12) Other Equity, Q2 FY26
R210 | ZERO_STANDING | P&L (12) Other Equity, H1 FY27
R211 | ZERO_STANDING | P&L (12) Other Equity, H1 FY26
R289 | ZERO_STANDING | CF Allowances for expected credit loss, H1 FY27 (to 30-Sep-2026)
R290 | ZERO_STANDING | CF Allowances for expected credit loss, H1 FY26 (to 30-Sep-2025)
R295 | ZERO_STANDING | CF (Profit)/Loss on sale of PPE, H1 FY27 (to 30-Sep-2026)
R297 | ZERO_STANDING | CF (Profit)/Loss on revocation of RoU, H1 FY27 (to 30-Sep-2026)
R331 | ZERO_STANDING | CF Proceeds from sale of PPE, H1 FY27 (to 30-Sep-2026)
R339 | ZERO_STANDING | CF Investment in shares, H1 FY27 (to 30-Sep-2026)
R340 | ZERO_STANDING | CF Investment in shares, H1 FY26 (to 30-Sep-2025)
R347 | ZERO_STANDING | CF Repayment of Long-term borrowings, H1 FY27 (to 30-Sep-2026)
R351 | ZERO_STANDING | CF Proceeds from initial public offering, H1 FY27 (to 30-Sep-2026)
R352 | ZERO_STANDING | CF Proceeds from initial public offering, H1 FY26 (to 30-Sep-2025)

ZERO_STANDING template signals: IPO proceeds line exists (nil both halves, IPO done before FY26); Investment in shares nil; Repayment of LT borrowings nil H1 FY27 (non-nil H1 FY26); ECL allowance nil both halves; Other equity line blank in quarter columns (only FY26 year-end 4,575.10 shown, R212).

## 2b. SUPERSEDED / RESOLVED IDs (explicit accounting)
ROW_ID | status | superseded by
--|--|--
R008 | SUPERSEDED_BY | R069 (authoritative; garbled original not used)
R009 | SUPERSEDED_BY | R070 (authoritative; garbled original not used)
R010 | SUPERSEDED_BY | R071 (authoritative; garbled original not used)
R011 | SUPERSEDED_BY | R072 (authoritative; garbled original not used)
R012 | SUPERSEDED_BY | R073 (authoritative; garbled original not used)
R013 | SUPERSEDED_BY | R074 (authoritative; garbled original not used)
R014 | SUPERSEDED_BY | R159 (authoritative; garbled original not used)
R015 | SUPERSEDED_BY | R160 (authoritative; garbled original not used)
R016 | SUPERSEDED_BY | R161 (authoritative; garbled original not used)
R017 | SUPERSEDED_BY | R162 (authoritative; garbled original not used)
R018 | SUPERSEDED_BY | R163 (authoritative; garbled original not used)
R019 | SUPERSEDED_BY | R164 (authoritative; garbled original not used)
R020 | SUPERSEDED_BY | R183 (authoritative; garbled original not used)
R021 | SUPERSEDED_BY | R184 (authoritative; garbled original not used)
R022 | SUPERSEDED_BY | R185 (authoritative; garbled original not used)
R023 | SUPERSEDED_BY | R186 (authoritative; garbled original not used)
R024 | SUPERSEDED_BY | R187 (authoritative; garbled original not used)
R025 | SUPERSEDED_BY | R188 (authoritative; garbled original not used)
R026 | SUPERSEDED_BY | R189 (authoritative; garbled original not used)
R027 | SUPERSEDED_BY | R212 (authoritative; garbled original not used)
R030 | SUPERSEDED_BY | R283 (authoritative; garbled original not used)
R068 | RESOLVED | grid caveat closed by image re-read; no live caveat

## 3. AGENDA ITEMS (Board Outcome letter p1)
ROW_ID | category | flags | note
--|--|--|--
R046 R047 R041 | agenda 1 | | approve unaudited results Q2/H1 FY27, Audit Committee reviewed; letter dated 17-Oct-2026
R033 R049 | agenda 2 | | noted Limited Review Report, S.K. Naredi & Co LLP
R003 R004 | meeting times | | 04:00 PM to 05:56 PM = 116 min (results-only agenda, no dividend, AGM, director, auditor, ESOP or capital-raising item in letter; preferential issue only in Note 4)
R031 R032 R001 R002 R037 R038 | letter identity | | exchanges, scrip code, ISIN, symbol, CIN

## 4. ANNEXURES / DIRECTOR PROFILES
None present in filing (no annexure tables, no director profiles). Count 0.

## 5. AUDITOR REPORT PARAGRAPHS (p3)
ROW_ID | category | flags | note
--|--|--|--
R005 R006 | UDIN/membership | | UDIN 26414050MQFBNG4074, M.No 414050
R048 R066 | para: scope/review standard (SRE 2410, moderate assurance) | | limited review, not audit opinion
R035 R050 R049 | signature/firm info | | partner Abhishek Agarwal; LLP conversion 20-Jun-2025; dated 17-Oct-2026
Paragraph inventory (fulltext p3): addressee+scope (1), management responsibility (2), review standard (3), conclusion unmodified (4) = 4 paras. No Emphasis of Matter, no Other Matters, no Going Concern language, no entity list (standalone), no unaudited-subsidiary carve-out. Absence flagged: no explicit comparative-period reference.

## 6. ENTITIES (consolidation)
ROW_ID | category | flags | note
--|--|--|--
R042 R064 | consolidation | | no subsidiary/associate/JV; standalone only; entities listed 0; prior ledger none, ENTITY_CHANGE not testable
R039 R036 R034 | segment/signatories | | single segment; CMD Sudhir Rai DIN 00512423 signed results; CS Debolina Karmakar signed letter

## 7. SIGNATURE BLOCKS
ROW_ID | note
--|--
R056 | digital signature 17:57:25 IST, 1 min AFTER meeting end 17:56 (R004): no flag
R036 | CMD signature on results statement p5 dated 17-Oct-2026, Jamshedpur

## 8. OTHER A1 ROWS (qualifiers/dates/unit)
ROW_ID | category | flags | note
--|--|--|--
R007 | number basis/period | | unit of statement
R051 | date basis/period | | column periods
R054 | date basis/period | | balance sheet dates
R055 | date basis/period | | cash flow periods
R057 | qualifier basis/period | | unit basis
R058 | qualifier basis/period | | audit status
R067 | qualifier basis/period | | cash flow basis

## 9. CROSS-PERIOD FLAGS
R129-R134 R130 R283 R284 | FOOTING_GAP RESTATED | H1 FY27 PBT 449.46 vs Q1+Q2 447.81 (diff 1.65); also PAT R162 vs Q1+Q2; Total Expenses R126; source: H1 inventory change (20.46) equals Q2 alone; A1 footing check lines 562-600; not adjusted. Question for A3: unreconciled; Note 6 regrouping may explain.
