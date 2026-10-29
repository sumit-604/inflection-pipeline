=== A2 COUNT TEST ===
category: notes          grep_count: 12  sweep_count: 12  match: yes   (9 results notes R466-R474 + 3 cash flow notes R480-R482)
category: line_items     grep_count: 124  sweep_count: 124  match: yes   (BS 38 + P&L 29 + CF 57; distinct page/line over R001-R359)
category: zero_standing  grep_count: 62  sweep_count: 62  match: yes   ([ZERO_STANDING] tags in structured = 62, all in R001-R359; 23 line items affected)
category: agenda_items   grep_count: 1   sweep_count: 1   match: yes
category: auditor_paras  grep_count: 4   sweep_count: 4   match: yes   (numbered paras 1-4 in fulltext lines 96,103,112 plus para 1 scope)
category: entities       grep_count: 36  sweep_count: 36  match: yes   (no consolidation list; standalone only)
gate_a2: pass
=== END COUNT TEST ===
ids_in_structured: 482 | ids_referenced_in_ledger: 482 | orphan_ids: [] | match: yes

# LEDGER: DYCL q2fy27 results (standalone, Rs Lakhs). Rows reference A1 IDs; no text re-copied.
Zero-standing line items: Loans non-current (R007-8), Current tax asset (R029-30), NC other fin. liab. (R047-8), DTL net (R049-50), Other NC liabilities (R053-4), Purchase of stock in trade (R101-6), Exceptional items (R149-54), OCI reclassifiable items X(b) (R197-214), CF items with ZERO cells (see rows). Zero rows are template signals; A3 should read exceptional/OCI(b) and preferential-allotment CF as expected-nil unless prior ledger shows otherwise.

## 1. NOTES
R466 | note | note 1 | board approval, limited review
R467 | note | note 2 | Ind AS basis
R468 | note | note 3 | single segment (no segment table to enumerate)
R469 | note | note 4 | Q2 is balancing figure; R475 restates (RESTATED)
R470 | note | note 5 | regrouping; R476 restates rounding (RESTATED)
R471 | note | note 6 | preferential issue proceeds fully utilised; cross-ref R380; CF R340-1 ZERO_STANDING; MATERIAL
R472 | note | note 7 | ESOP; cross-ref R381-R384; R418-9
R473 | note | note 8 | Labour Codes; RESTATED R478; forward R432; cross-ref R385-7
R474 | note | note 9 | publication
R480 | note | CF note 1 | indirect method; cross-ref R392
R481 | note | CF note 2 | brackets=outflow
R482 | note | CF note 3 | regrouping
Unnumbered footnotes: none found beyond R463-R465, R479 (unit/audit-status headers).

## 2. LINE ITEMS (ID range | category | flags | location: item)
R001..R002 (2 ids) | line_item |  | page 3 line 201: Property, plant and equipment
R003..R004 (2 ids) | line_item |  | page 3 line 202: Capital Work in Progress
R005..R006 (2 ids) | line_item |  | page 3 line 203: Other Intangible assets
R007..R008 (2 ids) | line_item | ZERO_STANDING | page 3 line 204: Financial assets - Loans (non-current)
R009..R010 (2 ids) | line_item |  | page 3 line 205: Financial assets - Other Financial Assets (non-current)
R011..R012 (2 ids) | line_item |  | page 3 line 206: Deferred Tax Asset (Net)
R013..R014 (2 ids) | line_item |  | page 3 line 207: Other non-current assets
R015..R016 (2 ids) | line_item |  | page 3 line 208: Total Non Current Assets
R017..R018 (2 ids) | line_item |  | page 3 line 209: Inventories
R019..R020 (2 ids) | line_item |  | page 3 line 210: Current financial assets - Investments
R021..R022 (2 ids) | line_item |  | page 3 line 211: Current financial assets - Trade receivables
R023..R024 (2 ids) | line_item |  | page 3 line 212: Current financial assets - Cash and cash equivalents
R025..R026 (2 ids) | line_item |  | page 3 line 213: Current financial assets - Bank balances other than cash and
R027..R028 (2 ids) | line_item |  | page 3 line 214: Current financial assets - Other financial assets
R029..R030 (2 ids) | line_item | ZERO_STANDING | page 3 line 215: Current tax Asset (net)
R031..R032 (2 ids) | line_item |  | page 3 line 216: Other current assets
R033..R034 (2 ids) | line_item |  | page 3 line 217: Total Current assets
R035..R036 (2 ids) | line_item |  | page 3 line 218: TOTAL ASSETS
R037..R038 (2 ids) | line_item |  | page 3 line 219: Equity share capital
R039..R040 (2 ids) | line_item |  | page 3 line 220: Other equity
R041..R042 (2 ids) | line_item |  | page 3 line 221: Total Equity
R043..R044 (2 ids) | line_item |  | page 3 line 222: Non-current Borrowings
R045..R046 (2 ids) | line_item |  | page 3 line 223: Non-current Lease liabilities
R047..R048 (2 ids) | line_item | ZERO_STANDING | page 3 line 224: Non-current Other financial liabilities
R049..R050 (2 ids) | line_item | ZERO_STANDING | page 3 line 225: Deferred Tax Liability (Net)
R051..R052 (2 ids) | line_item |  | page 3 line 226: Non-current Provisions
R053..R054 (2 ids) | line_item | ZERO_STANDING | page 3 line 227: Other non current liabilities
R055..R056 (2 ids) | line_item |  | page 3 line 228: Total Non-Current Liabilities
R057..R058 (2 ids) | line_item |  | page 3 line 229: Current Borrowings
R059..R060 (2 ids) | line_item |  | page 3 line 230: Current Lease Liabilities
R061..R062 (2 ids) | line_item |  | page 3 line 231: Trade payables - dues of micro enterprises and small enterpr
R063..R064 (2 ids) | line_item |  | page 3 line 232: Trade payables - dues of creditors other than micro enterpri
R065..R066 (2 ids) | line_item |  | page 3 line 233: Current Other financial liabilities
R067..R068 (2 ids) | line_item |  | page 3 line 234: Other current liabilities
R069..R070 (2 ids) | line_item |  | page 3 line 235: Current Provisions
R071..R072 (2 ids) | line_item |  | page 3 line 236: Current tax Liabilities (net)
R073..R074 (2 ids) | line_item |  | page 3 line 237: Total Current Liabilities
R075..R076 (2 ids) | line_item |  | page 3 line 238: TOTAL EQUITY & LIABILITIES
R077..R082 (6 ids) | line_item |  | page 4 line 329: I Revenue from operations
R083..R088 (6 ids) | line_item |  | page 4 line 330: II Other Income
R089..R094 (6 ids) | line_item |  | page 4 line 331: III Total Income (I+II)
R095..R100 (6 ids) | line_item |  | page 4 line 332: IV(a) Cost of materials consumed
R101..R106 (6 ids) | line_item | ZERO_STANDING | page 4 line 333: IV(b) Purchase of stock in trade
R107..R112 (6 ids) | line_item |  | page 4 line 334: IV(c) Changes in inventories of finished goods, work-in-prog
R113..R118 (6 ids) | line_item |  | page 4 line 335: IV(d) Employee benefit expense
R119..R124 (6 ids) | line_item |  | page 4 line 336: IV(e) Financial Costs
R125..R130 (6 ids) | line_item |  | page 4 line 337: IV(f) Depreciation and amortisation expense
R131..R136 (6 ids) | line_item |  | page 4 line 338: IV(g) Other Expenses
R137..R142 (6 ids) | line_item |  | page 4 line 339: Total Expenses (a to g)
R143..R148 (6 ids) | line_item |  | page 4 line 340: V Profit/(Loss) before exceptional items & tax
R149..R154 (6 ids) | line_item | ZERO_STANDING | page 4 line 341: VI Exceptional items
R155..R160 (6 ids) | line_item |  | page 4 line 342: VII Profit before tax (V-VI)
R161..R166 (6 ids) | line_item |  | page 4 line 343: VIII(1) Current Tax
R167..R172 (6 ids) | line_item |  | page 4 line 344: VIII(2) Deferred Tax
R173..R178 (6 ids) | line_item |  | page 4 line 345: IX Profit/(Loss) for the period (VII-VIII)
R179..R184 (6 ids) | line_item |  | page 4 line 346: X(a)(i) Items that will not be reclassified to Profit or Los
R185..R190 (6 ids) | line_item |  | page 4 line 347: X(a)(ii) Tax effect on items that will not be reclassified t
R191..R196 (6 ids) | line_item |  | page 4 line 348: X Total (a)
R197..R202 (6 ids) | line_item | ZERO_STANDING | page 4 line 349: X(b)(i) Items that will be reclassified to Profit or Loss
R203..R208 (6 ids) | line_item | ZERO_STANDING | page 4 line 350: X(b)(ii) Tax effect on items that will be reclassified to Pr
R209..R214 (6 ids) | line_item | ZERO_STANDING | page 4 line 351: X Total (b)
R215..R220 (6 ids) | line_item |  | page 4 line 352: Total Other Comprehensive Income
R221..R226 (6 ids) | line_item |  | page 4 line 353: XI Total Comprehensive Income for the period (IX+X)
R227..R232 (6 ids) | line_item |  | page 4 line 354: XII Paid up Equity share capital (face value Rs. 10)
R233..R233 (1 ids) | line_item |  | page 4 line 355: XIII Other Equity excluding revaluation reserves
R234..R239 (6 ids) | line_item |  | page 4 line 356: XIV(1) Basic EPS (in INR)
R240..R245 (6 ids) | line_item |  | page 4 line 357: XIV(2) Diluted EPS (in INR)
R246..R247 (2 ids) | line_item |  | page 5 line 458: Net Profit before tax
R248..R249 (2 ids) | line_item |  | page 5 line 459: Depreciation and amortisation expense
R250..R251 (2 ids) | line_item |  | page 5 line 460: (Profit)/Loss on sale of Property, Plant and Equipments
R252..R253 (2 ids) | line_item |  | page 5 line 461: Interest income
R254..R255 (2 ids) | line_item | ZERO_STANDING | page 5 line 462: Commission income against Financial Liability
R256..R257 (2 ids) | line_item | ZERO_STANDING | page 5 line 463: Other income against security deposit received
R258..R259 (2 ids) | line_item |  | page 5 line 464: Unrealized Gain (Loss) on Fair Value Of MF (Indirect Income)
R260..R261 (2 ids) | line_item |  | page 5 line 465: Lease rent
R262..R263 (2 ids) | line_item |  | page 5 line 466: Interest on lease liabilities
R264..R265 (2 ids) | line_item | ZERO_STANDING | page 5 line 467: Interest on financial liabilities
R266..R267 (2 ids) | line_item | ZERO_STANDING | page 5 line 468: Interest on Income tax
R268..R269 (2 ids) | line_item | ZERO_STANDING | page 5 line 469: Interest cost on Security deposit received
R270..R271 (2 ids) | line_item |  | page 5 line 470: Remeasurement of acturial gain/loss
R272..R273 (2 ids) | line_item | ZERO_STANDING (partial 1/2 cells) | page 5 line 471: Unrealized foreign exchange (gain)/loss
R274..R275 (2 ids) | line_item | ZERO_STANDING (partial 1/2 cells) | page 5 line 472: Claim, discount and written off
R276..R277 (2 ids) | line_item |  | page 5 line 473: Provision for expected credit loss
R278..R279 (2 ids) | line_item | ZERO_STANDING | page 5 line 474: Bad debts recovered
R280..R281 (2 ids) | line_item | ZERO_STANDING (partial 1/2 cells) | page 5 line 475: Interest income on Financial Assets
R282..R283 (2 ids) | line_item | ZERO_STANDING (partial 1/2 cells) | page 5 line 476: Employee Compensation Expenses
R284..R285 (2 ids) | line_item |  | page 5 line 477: Finance Cost
R286..R287 (2 ids) | line_item |  | page 5 line 478: Total adjustments (subtotal printed)
R288..R289 (2 ids) | line_item |  | page 5 line 479: Operating Profit before Working Capital Changes
R290..R291 (2 ids) | line_item |  | page 5 line 480: Increase / Decrease in Inventories
R292..R293 (2 ids) | line_item |  | page 5 line 481: Increase / Decrease in Trade receivables
R294..R295 (2 ids) | line_item |  | page 5 line 482: Increase / Decrease in Other current financial assets
R296..R297 (2 ids) | line_item |  | page 5 line 483: Increase / Decrease in Other current assets
R298..R299 (2 ids) | line_item |  | page 5 line 484: Increase / Decrease in Trade payable
R300..R301 (2 ids) | line_item |  | page 5 line 485: Increase / Decrease in Other financial liabilities
R302..R303 (2 ids) | line_item |  | page 5 line 486: Increase / Decrease in Other current liabilities
R304..R305 (2 ids) | line_item |  | page 5 line 487: Increase / Decrease in current provisions
R306..R307 (2 ids) | line_item | ZERO_STANDING | page 5 line 488: Increase / Decrease in current tax liabilities
R308..R309 (2 ids) | line_item |  | page 5 line 489: Increase / Decrease in Non current provisions
R310..R311 (2 ids) | line_item |  | page 5 line 490: Increase / Decrease in Non current financial liabilities
R312..R313 (2 ids) | line_item | ZERO_STANDING | page 5 line 491: Increase/Decrease in Other non current liability
R314..R315 (2 ids) | line_item |  | page 5 line 492: Total working capital changes (subtotal printed)
R316..R317 (2 ids) | line_item |  | page 5 line 493: Cash Generated from Operations
R318..R319 (2 ids) | line_item |  | page 5 line 494: Direct Taxes Paid (Net)
R320..R321 (2 ids) | line_item |  | page 5 line 495: Net Cash Inflow/(outflow) from Operating Activities (A)
R322..R323 (2 ids) | line_item |  | page 5 line 496: Purchase / Acquisition of Property, Plant and Equipment
R324..R325 (2 ids) | line_item |  | page 5 line 497: Proceeds from sale of Property, Plant and Equipments
R326..R327 (2 ids) | line_item |  | page 5 line 498: Interest received
R328..R329 (2 ids) | line_item |  | page 5 line 499: Lease rent received
R330..R331 (2 ids) | line_item |  | page 5 line 500: Increase / Decrease in Non current financial assets
R332..R333 (2 ids) | line_item |  | page 5 line 501: Increase / Decrease in Other non current assets
R334..R335 (2 ids) | line_item |  | page 5 line 502: Increase / Decrease in Other current bank balances
R336..R337 (2 ids) | line_item |  | page 5 line 503: Increase / Decrease in current financial assets - Investment
R338..R339 (2 ids) | line_item |  | page 5 line 504: Net Cash Inflow/(outflow) from Investing Activities (B)
R340..R341 (2 ids) | line_item | ZERO_STANDING | page 5 line 505: Proceeds from Preferential allotment
R342..R343 (2 ids) | line_item |  | page 5 line 506: Payment of Dividend
R344..R345 (2 ids) | line_item |  | page 5 line 507: Proceeds of Non current borrowings
R346..R347 (2 ids) | line_item |  | page 5 line 508: Repayment of Non current borrowings
R348..R349 (2 ids) | line_item |  | page 5 line 509: Proceeds/(Repayment) of Current borrowings (net)
R350..R351 (2 ids) | line_item |  | page 5 line 510: Finance Cost
R352..R353 (2 ids) | line_item |  | page 5 line 511: Net Cash Inflow/(outflow) from Financing Activities (C)
R354..R355 (2 ids) | line_item |  | page 5 line 512: Net increase/(decrease) in cash and cash equivalents (A+B+C)
R356..R357 (2 ids) | line_item |  | page 5 line 513: Opening Balance of Cash and Cash equivalents
R358..R359 (2 ids) | line_item |  | page 5 line 514: Closing Balance of Cash and Cash equivalents

## 3. AGENDA ITEMS (Board Outcome letter)
R456,R457 | agenda | item 1 only: approve unaudited results, take on record LRR | no AR/AGM/dividend/director/auditor/ESOP/fund-raise agenda item disclosed (MGMT_ABSENCE not applicable); R434 date; R433 letter date
R366,R367 | meeting times | 12:00 PM start, 12:35 PM end (35 min) | short meeting; R368 signature 12:43:45 after conclusion, no flag
R431,R438,R361 | trading window | closure to 48h after dissemination | FORWARD
R360,R362,R363,R364,R365,R395-R403,R436,R437,R439,R435 | letter header/admin | addressees, scrip, CIN, signatory Company Secretary

## 4. ANNEXURES / DIRECTOR PROFILES
No director profiles or annexures beyond statements. Signatory: R411,R428,R429,R389,R393,R378 (Ashish Mangal MD, DIN; RESTATED across pages).

## 5. AUDITOR REPORT PARAGRAPHS
R458,R462,R404,R410,R369,R376,R377 | addressee/scope | review of standalone only
R459,R460,R405,R406,R372 | para 3 scope SRE 2410 | moderate assurance, no audit opinion
R407,R408,R373,R374,R375,R417 | para 2 basis Ind AS 34 / s.133
R461,R477 | para 4 conclusion | unmodified; NO Emphasis of Matter, Other Matters, Going Concern language found
R409,R370,R371,R440,R441 | signing partner Vivek Gupta, UDIN, date | UDIN present
R415,R413 | auditor roles
No unaudited/management-furnished subsidiary entities (standalone only).

## 6. ENTITIES
R395-R430 (36 ids) | entity | no consolidation list; no subsidiary/associate/JV disclosed; ENTITY_CHANGE not assessable (no prior ledger)
Statutory/regulatory refs: R401,R402,R416,R417,R420-R426,R436,R439

## 7. SIGNATURE BLOCKS
R399,R368 | Naina Gupta, CS, 2026.10.27 12:43:45 | after R367 conclusion 12:35, consistent
R409,R371,R370 | Vivek Gupta, Partner, UDIN
R411,R428,R429 | Ashish Mangal MD signatures; dates R444,R452,R455

## 8. REMAINING ID GROUPS (accounted)
Numeric admin/identifier: R360-R394 (referenced above or by group: ESOP R381-384, Labour R385-387, CIN R362,R379,R390,R394, face value R391, preferential R380)
Dates: R433-R455 all DATE rows | Forward: R431,R432 | Qualifiers: R456-R482 (notes above)
Flag: RESTATED R469/R475, R470/R476, R473/R478, R466/R477.
