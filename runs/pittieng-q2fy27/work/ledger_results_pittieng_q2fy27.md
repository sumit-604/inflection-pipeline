# A2 LEDGER: PITTIENG results Q2 FY27
=== A2 COUNT TEST ===
category: notes          grep_count: 7    sweep_count: 7    match: yes   (fulltext lines 337,340,342,345,382,388,402 vs Note tags 1-7 in R418-R539)
category: line_items     grep_count: 126  sweep_count: 126  match: yes   (distinct page+line among table NUMBER rows vs label-run groups; P&L 32, BS 37, CF 40, recon 11, segment 6)
category: zero_standing  grep_count: 35  sweep_count: 35  match: yes   (A1 [ZERO_STANDING] value tags across 13 line items; plus R560 NA noted)
category: agenda_items   grep_count: 6    sweep_count: 6    match: yes   (fulltext lines 37,42,44,51,55,59; plus meeting time and signature rows)
category: auditor_paras  grep_count: 5    sweep_count: 5    match: yes   (numbered paras 1,2,3,5 plus unnumbered conclusion para; signature block separate)
category: entities       grep_count: 42  sweep_count: 42  match: yes   (A1 header ENTITY 42)
category: A1 type counts NUMBER 501 ENTITY 42 FORWARD 20 DATE 35 QUALIFIER 45 = 643  match: yes (grep per type reproduced)
category: turns, questions, mgmt_numbers, slides: not applicable (results filing)
gate_a2: pass
=== END COUNT TEST ===

ids_in_structured: 643 | ids_referenced_in_ledger: 643 | orphan_ids: [] | match: yes

Units: tables in Rs lakhs; Rs 450 cr capex in crores. MISSING_FROM_STRUCTURED: none.
Flag set: ZERO_STANDING, ENTITY_CHANGE, RESTATED, FOOTNOTE_UNRESOLVED, ARITH_CHECK.

## 1. NOTES (numbered 1-7) and footnotes

| Note | Row IDs | Content tag | Flags / xref |
|---|---|---|---|
| N1 | R418-R419 | Review/approval dates, Audit Committee and Board 22-Oct-2026 |  |
| N2 | R420-R421 | Interim dividend Rs 2/- (40%) | RESTATED vs R008-R010,R012 |
| N3 | R422 | Basis of preparation Ind AS |  |
| N4 | R423-R432 | Amalgamation PIPL+DFPL into Company, appointed date 1-Apr-2026, effective 23-Sep-2026; restated comparatives | ENTITY_CHANGE; RESTATED; xref EoM R050-R058, recon tables R433-R493 |
| N5 | R494-R499 | ESOP Trust 7,40,000 shares treasury; EPS anti-dilutive |  |
| N6 | R500-R502 | Single segment; geographic table | FOOTNOTE_UNRESOLVED R502 column label as printed (H 31.03.2026) |
| N7 | R539 | Regrouping of previous figures |  |
| FN-a | R066,R067,R068 | Restated-column and unit qualifiers on results table | RESTATED |
| FN-b | R244,R257 | Qualifiers below P&L table (page 5) | read by A3 |
| FN-c | R258,R259,R334,R335,R336,R417,R482,R544 | Table headings, page stamps, authentication |  |
| FN-d | R457,R483,R487,R501 | Reconciliation unit qualifiers |  |

## 2. LINE ITEMS (every table line, incl. zero/nil)

| LI | Row IDs | Table / page / line | Line item | Flags |
|---|---|---|---|---|
| LI001 | R069-R074 | P&L p5 l187 | (a) Revenue from operations |  |
| LI002 | R075-R080 | P&L p5 l188 | (b) Other income |  |
| LI003 | R081-R086 | P&L p5 l189 | Total Income |  |
| LI004 | R087-R092 | P&L p5 l191 | (a) Cost of materials consumed |  |
| LI005 | R093-R098 | P&L p5 l192 | (b) Purchase of Stock-in-trade | ZERO_STANDING (2 of 6 periods) |
| LI006 | R099-R104 | P&L p5 l193 | (c) Changes in inventories of finished goods work-in-progres |  |
| LI007 | R105-R110 | P&L p5 l194 | (d) Employee benefit expenses |  |
| LI008 | R111-R116 | P&L p5 l195 | (e) Finance costs |  |
| LI009 | R117-R122 | P&L p5 l196 | (f) Depreciation and amortization expenses |  |
| LI010 | R123-R128 | P&L p5 l197 | (g) Other Expenses |  |
| LI011 | R129-R134 | P&L p5 l198 | Total expenses |  |
| LI012 | R135-R140 | P&L p5 l199 | 3 Profit / (loss) before exceptional and extraordinary items |  |
| LI013 | R141-R146 | P&L p5 l200 | 4 Exceptional items | ZERO_STANDING (all periods) |
| LI014 | R147-R152 | P&L p5 l201 | 5 Profit / (loss) before extraordinary items and taxation (3 |  |
| LI015 | R153-R158 | P&L p5 l202 | 6 Extraordinary items | ZERO_STANDING (all periods) |
| LI016 | R159-R164 | P&L p5 l203 | 7 Profit / (loss) before taxation (5-6) |  |
| LI017 | R165-R170 | P&L p5 l205 | (a) Current tax charge / (Credit) |  |
| LI018 | R171-R176 | P&L p5 l206 | (b) Tax relating to earlier years charge / (Credit) | ZERO_STANDING (1 of 6 periods) |
| LI019 | R177-R182 | P&L p5 l207 | (c) Deferred tax charge / (Credit) |  |
| LI020 | R183-R188 | P&L p5 l208 | Total tax expenses |  |
| LI021 | R189-R194 | P&L p5 l209 | 9 Profit / (loss) for the period (7 - 8) |  |
| LI022 | R195-R200 | P&L p5 l212 | Remeasurement of the net defined benefit liability/assets |  |
| LI023 | R201-R206 | P&L p5 l213 | Change in fair value of investment | ZERO_STANDING (all periods) |
| LI024 | R207-R212 | P&L p5 l214 | Income Tax on items that will be not be reclassified Subsequ |  |
| LI025 | R213-R218 | P&L p5 l216 | Fair value of Changes in Cashflow Hedge | ZERO_STANDING (2 of 6 periods) |
| LI026 | R219-R224 | P&L p5 l217 | Income Tax on items that will be reclassified into Profit &  | ZERO_STANDING (2 of 6 periods) |
| LI027 | R225-R230 | P&L p5 l218 | Total other comprehensive income, net of income tax |  |
| LI028 | R231-R236 | P&L p5 l219 | 11 Total Comprehensive income (9+10) |  |
| LI029 | R237-R242 | P&L p5 l220 | 12 Paid up Share Capital (face value of Rs 5/- per share) |  |
| LI030 | R243 | P&L p5 l221 | 13 Reserves Excluding Revaluation Reserves |  |
| LI031 | R245-R250 | P&L p5 l223 | (a) Basic (Rs) |  |
| LI032 | R251-R256 | P&L p5 l224 | (b) Diluted (Rs) |  |
| LI033 | R260-R261 | BS p6 l233 | (a) Property, plant and equipment |  |
| LI034 | R262-R263 | BS p6 l234 | (b) Capital work-in-progress |  |
| LI035 | R264-R265 | BS p6 l235 | (c) Intangible Assets |  |
| LI036 | R266-R267 | BS p6 l236 | (d) Capital work-in-progress - Intangible | ZERO_STANDING (all periods) |
| LI037 | R268-R269 | BS p6 l237 | (e) Right of use of Assets |  |
| LI038 | R270-R271 | BS p6 l239 | (i) Investments |  |
| LI039 | R272-R273 | BS p6 l240 | (ii) Other Financial Assets |  |
| LI040 | R274-R275 | BS p6 l241 | (g) Other non-current assets |  |
| LI041 | R276-R277 | BS p6 l242 | TOTAL NON - CURRENT ASSETS |  |
| LI042 | R278-R279 | BS p6 l244 | (a) Inventories |  |
| LI043 | R280-R281 | BS p6 l246 | (i) Investments |  |
| LI044 | R282-R283 | BS p6 l247 | (ii) Trade receivables |  |
| LI045 | R284-R285 | BS p6 l248 | (iii) Cash and Cash equivalents |  |
| LI046 | R286-R287 | BS p6 l249 | (iv) Other bank balances |  |
| LI047 | R288-R289 | BS p6 l250 | (v) Other financial assets |  |
| LI048 | R290-R291 | BS p6 l251 | (c) Other current assets |  |
| LI049 | R292-R293 | BS p6 l252 | TOTAL CURRENT ASSETS |  |
| LI050 | R294-R295 | BS p6 l253 | TOTAL ASSETS |  |
| LI051 | R296-R297 | BS p6 l256 | (a) Equity share capital |  |
| LI052 | R298-R299 | BS p6 l257 | (b) Other equity |  |
| LI053 | R300-R301 | BS p6 l258 | TOTAL EQUITY |  |
| LI054 | R302-R303 | BS p6 l262 | (i) Borrowings |  |
| LI055 | R304-R305 | BS p6 l263 | (ii) Lease Liability |  |
| LI056 | R306-R307 | BS p6 l264 | (iii) Others |  |
| LI057 | R308-R309 | BS p6 l265 | (b) Provisions |  |
| LI058 | R310-R311 | BS p6 l266 | (c) Deferred tax liabilities (net) |  |
| LI059 | R312-R313 | BS p6 l267 | TOTAL NON-CURRENT LIABILITIES |  |
| LI060 | R314-R315 | BS p6 l270 | (i) Borrowings |  |
| LI061 | R316-R317 | BS p6 l271 | (ii) Lease liability |  |
| LI062 | R318-R319 | BS p6 l273 | Dues to micro and small enterprises |  |
| LI063 | R320-R321 | BS p6 l274 | Dues to others |  |
| LI064 | R322-R323 | BS p6 l275 | (iv) Other financial liabilities |  |
| LI065 | R324-R325 | BS p6 l276 | (b) Other current liabilities |  |
| LI066 | R326-R327 | BS p6 l277 | (c) Provisions |  |
| LI067 | R328-R329 | BS p6 l278 | (d) Income tax liabilities (net) |  |
| LI068 | R330-R331 | BS p6 l279 | TOTAL CURRENT LIABILITIES |  |
| LI069 | R332-R333 | BS p6 l280 | TOTAL EQUITY AND LIABILITIES |  |
| LI070 | R337-R338 | CF p7 l288 | Net Proift before tax |  |
| LI071 | R339-R340 | CF p7 l290 | Depreciation and amortization expenses |  |
| LI072 | R341-R342 | CF p7 l291 | Interest Income |  |
| LI073 | R343-R344 | CF p7 l292 | Credit Risk Impaired |  |
| LI074 | R345-R346 | CF p7 l293 | Credit Risk Allowance |  |
| LI075 | R347-R348 | CF p7 l294 | (Gain) / Loss on sale of property, plant and equipment (incl |  |
| LI076 | R349-R350 | CF p7 l295 | Loss/ (Profit) on Lease modification |  |
| LI077 | R351-R352 | CF p7 l296 | Re-measurement gains/(losses) on employee defined benefit pl |  |
| LI078 | R353-R354 | CF p7 l297 | Re-measurement (gains)/losses on Investments |  |
| LI079 | R355-R356 | CF p7 l298 | Fair value of Changes in Cashflow Hedge | ZERO_STANDING (1 of 2 periods) |
| LI080 | R357-R358 | CF p7 l299 | Unrealised foreign exchange differences |  |
| LI081 | R359-R360 | CF p7 l300 | Finance Costs |  |
| LI082 | R361-R362 | CF p7 l301 | Dividend income | ZERO_STANDING (1 of 2 periods) |
| LI083 | R363-R364 | CF p7 l302 | Share based payment expenses(net) |  |
| LI084 | R365-R366 | CF p7 l303 | Operating Profit before Working Capital changes |  |
| LI085 | R367-R368 | CF p7 l304 | Change in working capital |  |
| LI086 | R369-R370 | CF p7 l305 | Cash generated from operations |  |
| LI087 | R371-R372 | CF p7 l306 | Direct Taxes Paid |  |
| LI088 | R373-R374 | CF p7 l307 | Net cash flow from operating activities (A) |  |
| LI089 | R375-R376 | CF p7 l309 | Investments | ZERO_STANDING (1 of 2 periods) |
| LI090 | R377-R378 | CF p7 l310 | Purchase of Property, Plant & equipment and intangibles (inc |  |
| LI091 | R379-R380 | CF p7 l311 | Right of use of Assets |  |
| LI092 | R381-R382 | CF p7 l312 | Proceeds from sale of property, plant & equipment |  |
| LI093 | R383-R384 | CF p7 l313 | Dividend Income | ZERO_STANDING (1 of 2 periods) |
| LI094 | R385-R386 | CF p7 l314 | Interest income received |  |
| LI095 | R387-R388 | CF p7 l315 | Net cash used in Investing Activities - (B) |  |
| LI096 | R389-R390 | CF p7 l317 | Finance charges |  |
| LI097 | R391-R392 | CF p7 l318 | Cash Payments for Principal portion of lease liability |  |
| LI098 | R393-R394 | CF p7 l319 | Cash Payments for interest portion of lease liability |  |
| LI099 | R395-R396 | CF p7 l320 | Proceeds from Borrowings - Noncurrent (including current mat |  |
| LI100 | R397-R398 | CF p7 l321 | Repayment of Borrowings - Noncurrent (including current matu |  |
| LI101 | R399-R400 | CF p7 l322 | Proceeds/(repayments) of short-term borrowings (Net) |  |
| LI102 | R401-R402 | CF p7 l323 | Proceeds from ESOP Trust/(Purchase) of treasury shares by ES | ZERO_STANDING (1 of 2 periods) |
| LI103 | R403-R404 | CF p7 l324 | Term Deposit Accounts with financial institutions |  |
| LI104 | R405-R406 | CF p7 l325 | Payment of Dividend |  |
| LI105 | R407-R408 | CF p7 l326 | Unclaimed Dividend |  |
| LI106 | R409-R410 | CF p7 l327 | Net Cash used in Finance Activities - (C) |  |
| LI107 | R411-R412 | CF p7 l328 | Net Increase/(Decrease) in Cash & Cash Equivalents (A+B+C) |  |
| LI108 | R413-R414 | CF p7 l329 | Opening Balance in Cash and cash equivalents |  |
| LI109 | R415-R416 | CF p7 l330 | Closing Balance in Cash and cash equivalents |  |
| LI110 | R433-R438 | Recon Standalone p8 l358 | Total Income | RESTATED |
| LI111 | R439-R444 | Recon Standalone p8 l359 | Profit before tax | RESTATED |
| LI112 | R445-R450 | Recon Standalone p8 l360 | Profit after tax | RESTATED |
| LI113 | R451-R456 | Recon Standalone p8 l361 | Total Comprehensive Income | RESTATED |
| LI114 | R458-R463 | Recon Standalone p8 l365 | Total Income | RESTATED |
| LI115 | R464-R469 | Recon Standalone p8 l366 | Profit before tax | RESTATED |
| LI116 | R470-R475 | Recon Standalone p8 l367 | Profit after tax | RESTATED |
| LI117 | R476-R481 | Recon Standalone p8 l368 | Total Comprehensive Income | RESTATED |
| LI118 | R484-R486 | Recon Statement  p9 l375 | Total Assets and Liabilities | RESTATED |
| LI119 | R488-R490 | Recon Standalone p9 l379 | Net Increase/(Decrease) in Cash & Cash E | RESTATED |
| LI120 | R491-R493 | Recon Standalone p9 l380 | Closing Balance in Cash and cash equival | RESTATED |
| LI121 | R503-R508 | Segment p9 l394 | a) India | RESTATED |
| LI122 | R509-R514 | Segment p9 l395 | b) Outside India | RESTATED |
| LI123 | R515-R520 | Segment p9 l396 | Revenue from Operations | RESTATED |
| LI124 | R521-R526 | Segment p9 l398 | a) India | RESTATED |
| LI125 | R527-R532 | Segment p9 l399 | b) Outside India | RESTATED |
| LI126 | R533-R538 | Segment p9 l400 | Total | RESTATED |

## 3. AGENDA ITEMS (Board Outcome letter) and signature

| Item | Row IDs | Content tag | Flags / xref |
|---|---|---|---|
| A1 | R006,R007 | Approval of unaudited results Q and H1 ended 30-Sep-2026, Reg 33; limited review report |  |
| A2 | R008-R011,R001 | Interim dividend Rs 2/- (40%) FV Rs 5/-, FY2026-27 | RESTATED in Note 2 R421 |
| A3 | R012-R014 | Record date 2-Nov-2026; payment by 21-Nov-2026 | FORWARD R013 |
| A4 | R015-R019 | Capex Rs 450 cr, Karnataka lamination consolidation, phased to FY2030-31 | FORWARD R016,R018; xref Annexure 1 R565,R563; capex in crores vs tables in lakhs |
| A5 | R020-R024 | Second ESOP grant 5,77,500 options at Rs 736.72, NRC 22-Oct-2026 | xref Annexure 2 R573,R574 |
| A6 | R025-R032 | Re-designation of 2 SMP and promotion of 1 to Deputy COO, effective 22-Oct-2026 | ENTITY_CHANGE (management roles) R026-R028 |
| A-time | R033-R034 | Board meeting 4:30 PM to 5:10 PM (40 minutes) | short meeting for 6 items incl. Rs 450 cr capex |
| A-sig | R035-R038 | Digital signature Mary Monica Braganza, CS and CCO, FCS 5532, timestamp 2026.10.22 18:13:04 +05:30 | timestamp 63 minutes after meeting end; no flag |

## 4. AUDITOR REPORT PARAGRAPHS

| Para | Row IDs | Content tag | Flags / xref |
|---|---|---|---|
| AP1 | R039-R041 | Addressee, report title, review period, Talati & Talati LLP Ahmedabad |  |
| AP2 | R042 | Paragraph on Ind AS 34 basis |  |
| AP3 | R043-R046 | Review per SRE 2410, ICAI, moderate assurance |  |
| AP4 | R047-R048 | Review limitation; conclusion unmodified (limited review) | opinion type: unmodified conclusion |
| AP5 | R049 | Auditor office postcode |  |
| AP6 | R050-R058 | Emphasis of Matter para 5, Note 4 amalgamation, NCLT 8-Sep-2026, appointed date 1-Apr-2026, Appendix C Ind AS 103 | ENTITY_CHANGE; conclusion not modified; no Going Concern language in A1 rows; no Other Matters para; no unaudited or management-furnished entity list (standalone) |
| AP7 | R059-R064 | Signature block: firm reg no, CA Amit Shah partner, place Delhi, date, membership 122131, UDIN | FOOTNOTE_UNRESOLVED R059 (text layer), R062 (day unreadable), R064 (UDIN as extracted) |
| AP8 | R065-R068 | Results statement header: registrant, unaudited standalone, Rs lakhs, restated columns | RESTATED |

## 5. ANNEXURES, SMP PROFILES, RESULTS SIGNATURE

| Item | Row IDs | Content tag | Flags / xref |
|---|---|---|---|
| ANX1 | R545-R571 | Annexure 1 capex and capacity: existing 1,08,000 MT sheet metal, 8,13,600 machine hours; utilisation ~78% and ~85%; capacity table; Rs 450 cr; financing internal accruals and debt, no split | FORWARD R550,R563,R567-R571; ZERO_STANDING-type NA R560; ARITH_CHECK for A3: R556 (1,60,000 post) with R560 NA addition; R558 (13,14,000 post) vs R561 + R562 |
| ANX2 | R572-R586 | Annexure 2 ESOP Grant 2: 5,77,500 options, Rs 736.72, discount 23.03% to Rs 957.20 close 21-Oct-2026, pool 13,00,000 | RESTATED vs R020,R021; FOOTNOTE_UNRESOLVED R577 (page text scrambled) |
| ANX2v | R587-R622 | ESOP vesting: 75% TBO and 25% PBO, 8-year schedule, 5-year exercise window, 80,000 first-grant options cancelled | ZERO_STANDING R593,R594,R596 (Nil vesting); FORWARD R589,R595,R598,R601,R604,R607,R610,R613,R616,R617 |
| ANX3a | R623-R630 | Annexure 3 profile 1 of 3: Shri Sandip Agarwala, age 50, joined May 2013, to Deputy CEO | FORWARD R629; no relationships R630 |
| ANX3b | R631-R636 | Profile 2 of 3: Shri Chaitra Sundaresh, age 48, Deputy COO since May 2024, to COO M&G | no relationships R636 |
| ANX3c | R637-R643 | Profile 3 of 3: Shri Avinash Arun Patil, age 44, joined May 2024 from CG Power, to Deputy COO | no relationships R643 |
| SIG2 | R540-R544 | Results signatory Akshay S Pitti MD&CEO DIN 00078760, Hyderabad, 22-Oct-2026 |  |

## 6. ENTITIES (all A1 ENTITY rows; standalone, no consolidation list; prior ledger not supplied, change flags from Note 4 and EoM only)

| Row ID | Page/line | Flag |
|---|---|---|
| R002 | p1 l22 |  |
| R003 | p1 l24 |  |
| R007 | p1 l38 |  |
| R017 | p1 l52 |  |
| R022 | p1 l56 |  |
| R023 | p1 l57 |  |
| R026 | p2 l66 |  |
| R027 | p2 l68 |  |
| R028 | p2 l71 |  |
| R030 | p2 l77 |  |
| R037 | p2 l93 |  |
| R039 | p3 l101 |  |
| R040 | p3 l104 |  |
| R042 | p3 l120 |  |
| R043 | p3 l127 |  |
| R045 | p3 l129 |  |
| R050 | p4 l155 |  |
| R052 | p4 l159 |  |
| R053 | p4 l161 | ENTITY_CHANGE: PIPL amalgamated, dissolved |
| R054 | p4 l162 | ENTITY_CHANGE: DFPL amalgamated, dissolved |
| R057 | p4 l168 |  |
| R060 | p4 l176 |  |
| R061 | p4 l176 |  |
| R065 | p5 l183 |  |
| R419 | p8 l337 |  |
| R426 | p8 l348 |  |
| R428 | p8 l349 |  |
| R495 | p9 l382 |  |
| R498 | p9 l385 |  |
| R540 | p9 l406 |  |
| R542 | p9 l409 |  |
| R545 | p10 l414 |  |
| R547 | p10 l417 |  |
| R569 | p10 l450 |  |
| R572 | p11 l462 |  |
| R575 | p11 l469 |  |
| R584 | p11 l494 |  |
| R623 | p13 l571 |  |
| R627 | p13 l592 |  |
| R631 | p14 l620 |  |
| R637 | p15 l653 |  |
| R642 | p15 l680 |  |

## 7. CROSS-REFERENCES

| X | Row IDs | Tie | Flag |
|---|---|---|---|
| X1 | R069 = R515 | Revenue from operations 30.09.2026 quarter tie, P&L and segment | RESTATED |
| X2 | R008-R010 = R421 | Dividend in letter and Note 2 | RESTATED |
| X3 | R015 = R565 ; R018 = R563 | Capex amount and phasing in letter and Annexure 1 | RESTATED |
| X4 | R020,R021 = R573,R574 = R578 | ESOP quantity and price repeated | RESTATED |
| X5 | R051,R055 = R424,R427 | NCLT order and appointed date in EoM and Note 4 | RESTATED |
| X6 | R026-R028 = R623-R637 | SMP re-designation in letter and Annexure 3 | RESTATED |
| X7 | R001,R024,R025,R029 | 22-Oct-2026 repeated as meeting, NRC, effective dates | RESTATED |
