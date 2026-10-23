# A2 LEDGER, results, Tinna Rubber (TINNARUBR) Q2 FY27
ids_in_structured: 927 | ids_referenced_in_ledger: 927 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: notes          grep_count: 10   sweep_count: 10  match: yes  (SA 1-5 + CO 1-5; grep on fulltext sees only notes 2,4,5 in embedded layer, 1,3 garbled; OCR blocks supply rest)
category: line_items     grep_count: 226  sweep_count: 226  match: yes  (SA 108, CO 118; cells 692 = A1 STATEMENT CHECKS 692)
category: zero_standing  grep_count: 81   sweep_count: 81  match: yes  (A1 header 81)
category: agenda_items   grep_count: 1    sweep_count: 1   match: yes
category: auditor_paras  grep_count: 12   sweep_count: 12  match: yes  (SA 5, CO 7; fulltext counted on embedded layer only, OCR page 13 block duplicates pages 12-13 embedded paras 6-7 and is excluded)
category: entities       grep_count: 57   sweep_count: 57  match: yes  (A1 header ENTITY 57)
category: by_type        grep_count: 927  sweep_count: 927 match: yes  (NUMBER 745 + ENTITY 57 + FORWARD 10 + DATE 45 + QUALIFIER 70)
gate_a2: pass
=== END COUNT TEST ===

Fulltext double-count handling: not used for the count test. All counts come from the structured file. Fulltext used only to confirm note and auditor-para numbering, counting the embedded layer and the OCR block of a page once (never both).
Non-statement NUMBER rows (identifiers, note figures, auditor figures): 53. Statement cells 692 + 53 = 745 NUMBER. OCR_CONFLICT 227 and OCR_ROW_MISSING 7 stay with the group rows below.

## 1. NOTES
ID | note | statement | flags / cross-ref
R880 | Note 1 | standalone | RESTATED with R912 (consolidated Note 1)
R912 | Note 1 | consolidated | RESTATED with R880
R881 | Note 2 | standalone | RESTATED with R913 (consolidated Note 2)
R913 | Note 2 | consolidated | RESTATED with R881
R882 | Note 3 | standalone | RESTATED with R914 (consolidated Note 3)
R914 | Note 3 | consolidated | RESTATED with R882
R883 | Note 4 | standalone | RESTATED with R915 (consolidated Note 4) ; forward R803-R805 ; CONSOLIDATION_LIST_GAP
R915 | Note 4 | consolidated | RESTATED with R883 ; forward R808-R810
R884 | Note 5 | standalone | RESTATED with R916 (consolidated Note 5) ; sub-rows R885-R888 (SLP, compensation, curative, mgmt view); forward R806-R807
R916 | Note 5 | consolidated | RESTATED with R884 ; sub-rows R917-R920 ; forward R811-R812
R885,R886,R887,R888,R917,R918,R919,R920 | Note 5 sub-statements | both | grouped under Note 5; auditor EoM cross-ref R893/R925
R879,R911 | notes headings | both | heading

## 2. LINE ITEMS (statements; one row per line item, IDs are its per-column cells)

ID_RANGE | page | statement line | cells | flags | note
R012-R017 | p2 | standalone P&L, Revenue from operations | 6 |  |
R018-R023 | p2 | standalone P&L, Other income | 6 | OCR_CONFLICT x2 |
R024-R029 | p2 | standalone P&L, Total income | 6 |  |
R030-R035 | p2 | standalone P&L, (a) Cost of material consumed | 6 |  |
R036-R041 | p2 | standalone P&L, (b) Purchase of stock in trade | 6 |  |
R042-R047 | p2 | standalone P&L, (c) Changes in inventories of finished goods, work in progress and stock in trade | 6 | OCR_CONFLICT x2 |
R048-R053 | p2 | standalone P&L, (d) Employee benefits expense | 6 |  |
R054-R059 | p2 | standalone P&L, (e) Finance costs | 6 | OCR_CONFLICT x3 |
R060-R065 | p2 | standalone P&L, (f) Depreciation and amortization expenses | 6 | OCR_CONFLICT x3 |
R066-R071 | p2 | standalone P&L, (g) Other expenses | 6 | OCR_CONFLICT x1 |
R072-R077 | p2 | standalone P&L, Total expenses | 6 | OCR_CONFLICT x1 |
R078-R083 | p2 | standalone P&L, Profit before tax (1-2) | 6 |  |
R084-R089 | p2 | standalone P&L, (a) Current tax | 6 |  |
R090-R095 | p2 | standalone P&L, (b) Deferred tax | 6 | OCR_CONFLICT x1 |
R096-R101 | p2 | standalone P&L, (c) Tax pertain to earlier years | 6 | ZERO_STANDING x4 |
R102-R107 | p2 | standalone P&L, Total tax expenses | 6 | OCR_CONFLICT x1 |
R108-R113 | p2 | standalone P&L, Profit for the period/year (3-4) | 6 | OCR_CONFLICT x1 |
R114-R119 | p2 | standalone P&L, Total comprehensive income for the period/year (net of tax) (5+6) | 6 | OCR_CONFLICT x2 |
R120-R125 | p2 | standalone P&L, Total other comprehensive income | 6 | ZERO_STANDING x5, OCR_CONFLICT x1 |
R126-R131 | p2 | standalone P&L, OCI (a) Re-measurement gains/(losses) on defined benefit plans | 6 | ZERO_STANDING x5, OCR_CONFLICT x1 |
R132-R137 | p2 | standalone P&L, OCI (b) Change in fair value of equity instrument through OCI | 6 | ZERO_STANDING x5 |
R138-R143 | p2 | standalone P&L, OCI (c) Income tax relating to the above items | 6 | ZERO_STANDING x5 |
R145-R150 | p2 | standalone P&L, Paid up equity share capital (Face value Rs. 10/- each) | 6 |  |
R151-R156 | p2 | standalone P&L, Other equity | 6 | ZERO_STANDING x5 |
R157-R162 | p2 | standalone P&L, Basic earning per share (Rs.) | 6 | OCR_CONFLICT x2 |
R163-R168 | p2 | standalone P&L, Diluted earning per share (Rs.) | 6 | OCR_CONFLICT x2 |
R171-R172 | p3 | standalone balance sheet, Total non-current assets | 2 | OCR_CONFLICT x2 |
R173-R174 | p3 | standalone balance sheet, Property, plant and equipment | 2 |  |
R175-R176 | p3 | standalone balance sheet, Capital work in progress | 2 |  |
R177-R178 | p3 | standalone balance sheet, Investment property | 2 |  |
R179-R180 | p3 | standalone balance sheet, Right of use assets | 2 |  |
R181-R182 | p3 | standalone balance sheet, Other intangible assets | 2 |  |
R183-R184 | p3 | standalone balance sheet, Total assets | 2 | OCR_CONFLICT x2 |
R185-R186 | p3 | standalone balance sheet, i) Investments in subsidiaries | 2 |  |
R187-R188 | p3 | standalone balance sheet, ii) Investment in associate and joint venture | 2 |  |
R189-R190 | p3 | standalone balance sheet, iii) Investments | 2 |  |
R191-R192 | p3 | standalone balance sheet, iv) Loans (non-current) | 2 | ZERO_STANDING x1 |
R193-R194 | p3 | standalone balance sheet, iv) Other financial assets (non-current) | 2 | OCR_CONFLICT x1 |
R195-R196 | p3 | standalone balance sheet, Other non-current assets | 2 | OCR_CONFLICT x1 |
R197-R198 | p3 | standalone balance sheet, Total current assets | 2 | OCR_CONFLICT x2 |
R199-R200 | p3 | standalone balance sheet, Inventories | 2 | OCR_CONFLICT x1 |
R201-R202 | p3 | standalone balance sheet, i) Trade receivables | 2 |  |
R203-R204 | p3 | standalone balance sheet, ii) Cash and cash equivalents | 2 |  |
R205-R206 | p3 | standalone balance sheet, iii) Bank balances other than (ii) above | 2 | OCR_CONFLICT x1 |
R207-R208 | p3 | standalone balance sheet, iv) Loans (current) | 2 |  |
R209-R210 | p3 | standalone balance sheet, v) Others financial assets (current) | 2 |  |
R211-R212 | p3 | standalone balance sheet, Other current assets | 2 |  |
R213-R214 | p3 | standalone balance sheet, Equity share capital | 2 |  |
R215-R216 | p3 | standalone balance sheet, Other equity | 2 |  |
R217-R218 | p3 | standalone balance sheet, Total equity | 2 | OCR_CONFLICT x1 |
R219-R220 | p3 | standalone balance sheet, Total non-current liabilities | 2 | OCR_CONFLICT x2 |
R221-R222 | p3 | standalone balance sheet, Non-current (i) Borrowings | 2 |  |
R223-R224 | p3 | standalone balance sheet, Non-current (ii) Lease liabilities | 2 | OCR_CONFLICT x1 |
R225-R226 | p3 | standalone balance sheet, Non-current Provisions | 2 | OCR_CONFLICT x1 |
R227-R228 | p3 | standalone balance sheet, Deferred tax liabilities (net) | 2 | OCR_CONFLICT x1 |
R229-R230 | p3 | standalone balance sheet, Total current liabilities | 2 | OCR_CONFLICT x2 |
R231-R232 | p3 | standalone balance sheet, Total equity and liabilities | 2 | OCR_CONFLICT x2 |
R233-R234 | p3 | standalone balance sheet, Current i) Borrowings | 2 | OCR_CONFLICT x1 |
R235-R236 | p3 | standalone balance sheet, Current ii) Lease liabilities | 2 |  |
R237-R238 | p3 | standalone balance sheet, iii)(a) Trade payables, dues of micro enterprises and small enterprises | 2 | OCR_CONFLICT x1 |
R239-R240 | p3 | standalone balance sheet, iii)(b) Trade payables, dues of creditors other than micro and small enterprises | 2 |  |
R241-R242 | p3 | standalone balance sheet, iv) Other financial liabilities | 2 |  |
R243-R244 | p3 | standalone balance sheet, Other current liabilities | 2 |  |
R245-R246 | p3 | standalone balance sheet, Current Provisions | 2 | OCR_CONFLICT x1 |
R247-R248 | p3 | standalone balance sheet, Current tax liabilities (net) | 2 | OCR_CONFLICT x1 |
R250-R251 | p4 | standalone cash flow, Cash generated from operations | 2 | OCR_CONFLICT x2 |
R252-R253 | p4 | standalone cash flow, Profit before tax | 2 |  |
R254-R255 | p4 | standalone cash flow, Depreciation and amortisation expense | 2 |  |
R256-R257 | p4 | standalone cash flow, Loss/(gain) on disposal of PPE | 2 |  |
R258-R259 | p4 | standalone cash flow, Rental income (adjustment) | 2 |  |
R260-R261 | p4 | standalone cash flow, Rental income (investing) | 2 |  |
R262-R263 | p4 | standalone cash flow, Provision for expected credit loss | 2 |  |
R264-R265 | p4 | standalone cash flow, Expenses on employees stock options scheme | 2 |  |
R266-R267 | p4 | standalone cash flow, Excess provisions written back | 2 |  |
R268-R269 | p4 | standalone cash flow, Finance cost | 2 | OCR_CONFLICT x1 |
R270-R271 | p4 | standalone cash flow, Unrealised foreign exchange gain | 2 | ZERO_STANDING x1 |
R272-R273 | p4 | standalone cash flow, Finance income | 2 |  |
R274-R275 | p4 | standalone cash flow, Operating profit before working capital changes | 2 | OCR_CONFLICT x1 |
R276-R277 | p4 | standalone cash flow, (Increase)/decrease in inventories | 2 |  |
R278-R279 | p4 | standalone cash flow, (Increase)/decrease in trade receivables | 2 |  |
R280-R281 | p4 | standalone cash flow, (Increase)/decrease in other financial assets | 2 |  |
R282-R283 | p4 | standalone cash flow, (Increase)/decrease in other assets | 2 |  |
R284-R285 | p4 | standalone cash flow, Increase/(decrease) in trade payables | 2 |  |
R286-R287 | p4 | standalone cash flow, Increase/(decrease) in other financial liabilities | 2 |  |
R288-R289 | p4 | standalone cash flow, Increase/(decrease) in other liabilities | 2 |  |
R290-R291 | p4 | standalone cash flow, Increase/(decrease) in provisions | 2 |  |
R292-R293 | p4 | standalone cash flow, Income tax paid (net of refunds) | 2 | OCR_CONFLICT x2 |
R294-R295 | p4 | standalone cash flow, Net cash flow generated from operating activities (A) | 2 | OCR_CONFLICT x2 |
R296-R297 | p4 | standalone cash flow, Purchase of property plant & equipment (net of capital advances and capital payables) | 2 |  |
R298-R299 | p4 | standalone cash flow, Proceeds from sale of property, plant and equipment | 2 |  |
R300-R301 | p4 | standalone cash flow, Loan given & received back | 2 |  |
R302-R303 | p4 | standalone cash flow, Investment in subsidiary | 2 |  |
R304-R305 | p4 | standalone cash flow, Proceeds from sale of investment | 2 | ZERO_STANDING x1 |
R306-R307 | p4 | standalone cash flow, Interest received | 2 |  |
R308-R309 | p4 | standalone cash flow, (Investing in)/redemption of term deposit | 2 |  |
R310-R311 | p4 | standalone cash flow, Net cash flow (used) in investing activities (B) | 2 | OCR_CONFLICT x2 |
R312-R313 | p4 | standalone cash flow, Proceed from issue of equity shares | 2 | ZERO_STANDING x1 |
R314-R315 | p4 | standalone cash flow, Proceeds of long term borrowings | 2 |  |
R316-R317 | p4 | standalone cash flow, Repayments from long term borrowings | 2 |  |
R318-R319 | p4 | standalone cash flow, Proceeds/(repayment) of short term borrowings | 2 |  |
R320-R321 | p4 | standalone cash flow, Payment of principal portion of lease liabilities | 2 | ZERO_STANDING x1 |
R322-R323 | p4 | standalone cash flow, Payment of interest on lease liabilities | 2 | ZERO_STANDING x1 |
R324-R325 | p4 | standalone cash flow, Dividend paid | 2 |  |
R326-R327 | p4 | standalone cash flow, Interest paid | 2 |  |
R328-R329 | p4 | standalone cash flow, Net cash flow from/(used) in financing activities (C) | 2 |  |
R330-R331 | p4 | standalone cash flow, Net increase/(decrease) in cash and cash equivalents (A+B+C) | 2 | OCR_CONFLICT x2 |
R332-R333 | p4 | standalone cash flow, Cash and cash equivalents at the beginning of the period | 2 |  |
R334-R335 | p4 | standalone cash flow, Cash and cash equivalents at the end of the period | 2 |  |
R347-R352 | p8 | consolidated P&L, Revenues from operations | 6 | OCR_CONFLICT x5 |
R353-R358 | p8 | consolidated P&L, Other income | 6 | OCR_CONFLICT x3 |
R359-R364 | p8 | consolidated P&L, Total income | 6 | OCR_CONFLICT x4 |
R365-R370 | p8 | consolidated P&L, Total expenses | 6 | OCR_CONFLICT x6 |
R371-R376 | p8 | consolidated P&L, (a) Cost of material consumed | 6 | OCR_CONFLICT x4 |
R377-R382 | p8 | consolidated P&L, (b) Purchase of stock in trade | 6 | OCR_CONFLICT x5 |
R383-R388 | p8 | consolidated P&L, (c) Changes in inventories of finished goods, work in progress and stock in trade | 6 | OCR_CONFLICT x6 |
R389-R394 | p8 | consolidated P&L, (d) Employee benefits expense | 6 | OCR_CONFLICT x3 |
R395-R400 | p8 | consolidated P&L, (e) Finance costs | 6 | OCR_CONFLICT x6 |
R401-R406 | p8 | consolidated P&L, (f) Depreciation and amortization expenses | 6 | OCR_CONFLICT x2 |
R407-R412 | p8 | consolidated P&L, (g) Other expenses | 6 | OCR_CONFLICT x2 |
R413-R418 | p8 | consolidated P&L, Profit before tax and share of profit in associates and joint venture (1-2) | 6 | OCR_CONFLICT x3 |
R419-R424 | p8 | consolidated P&L, Share of profit of an associate (net of tax) | 6 | OCR_CONFLICT x3 |
R425-R430 | p8 | consolidated P&L, Profit before tax from continuing operation | 6 | OCR_CONFLICT x3 |
R431-R436 | p8 | consolidated P&L, (a) Current tax | 6 | OCR_CONFLICT x3 |
R437-R442 | p8 | consolidated P&L, (b) Deferred tax | 6 | OCR_CONFLICT x4 |
R443-R448 | p8 | consolidated P&L, (c) Tax pertain to earlier years | 6 | ZERO_STANDING x4 |
R449-R454 | p8 | consolidated P&L, Total tax expenses | 6 |  |
R455-R460 | p8 | consolidated P&L, Total other comprehensive income (net of tax) | 6 | OCR_CONFLICT x6 |
R461-R466 | p8 | consolidated P&L, OCI (a) Re-measurement gains/(losses) on defined benefits | 6 | ZERO_STANDING x5, OCR_CONFLICT x1 |
R467-R472 | p8 | consolidated P&L, OCI (b) Change in fair value of equity instrument through OCI | 6 | ZERO_STANDING x5 |
R473-R478 | p8 | consolidated P&L, OCI (c) Income tax relating to the above items | 6 | ZERO_STANDING x5 |
R479-R484 | p8 | consolidated P&L, Foreign currency translation reserve (net of taxes) | 6 | OCR_CONFLICT x4 |
R485-R490 | p8 | consolidated P&L, Share of associates in other comprehensive income (net of taxes) | 6 | ZERO_STANDING x6 |
R491-R496 | p8 | consolidated P&L, Profit for the period/year (4-5) | 6 | OCR_CONFLICT x1 |
R497-R502 | p8 | consolidated P&L, Net profit attributable to Owners of Parent Company | 6 | OCR_CONFLICT x1 |
R503-R508 | p8 | consolidated P&L, Net profit attributable to Non controlling interest | 6 | ZERO_STANDING x6 |
R509-R514 | p8 | consolidated P&L, Total comprehensive income attributable to Non controlling interest | 6 | ZERO_STANDING x6 |
R515-R520 | p8 | consolidated P&L, Total comprehensive income for the period/year (net of tax) (6+7) | 6 | OCR_CONFLICT x2 |
R521-R526 | p8 | consolidated P&L, Total comprehensive income attributable to Owners of Parent Company | 6 | OCR_CONFLICT x2 |
R528-R533 | p8 | consolidated P&L, Paid up equity share capital (Face value Rs. 10/- each) | 6 |  |
R534-R539 | p8 | consolidated P&L, Other equity | 6 | ZERO_STANDING x5, OCR_CONFLICT x1 |
R540-R545 | p8 | consolidated P&L, Basic earning per share (Rs.) | 6 | OCR_CONFLICT x1 |
R546-R551 | p8 | consolidated P&L, Diluted earning per share (Rs.) | 6 | OCR_CONFLICT x4 |
R554-R555 | p9 | consolidated balance sheet, Total assets | 2 | OCR_CONFLICT x2 |
R556-R557 | p9 | consolidated balance sheet, Property, plant and equipment | 2 |  |
R558-R559 | p9 | consolidated balance sheet, Capital work in progress | 2 |  |
R560-R561 | p9 | consolidated balance sheet, Investment property | 2 | OCR_CONFLICT x2 |
R562-R563 | p9 | consolidated balance sheet, Right of use assets | 2 | OCR_CONFLICT x2 |
R564-R565 | p9 | consolidated balance sheet, Other intangible assets | 2 | OCR_CONFLICT x1 |
R566-R567 | p9 | consolidated balance sheet, i) Investment in associate and Joint Venture | 2 |  |
R568-R569 | p9 | consolidated balance sheet, ii) Investments | 2 |  |
R570-R571 | p9 | consolidated balance sheet, iii) Loans (non-current) | 2 | ZERO_STANDING x1 |
R572-R573 | p9 | consolidated balance sheet, iv) Other financial assets (non-current) | 2 | OCR_CONFLICT x2 |
R574-R575 | p9 | consolidated balance sheet, Other non-current assets | 2 | OCR_CONFLICT x1 |
R576-R577 | p9 | consolidated balance sheet, Total current assets | 2 | OCR_CONFLICT x2 |
R578-R579 | p9 | consolidated balance sheet, Inventories | 2 |  |
R580-R581 | p9 | consolidated balance sheet, i) Trade receivables | 2 | OCR_CONFLICT x1 |
R582-R583 | p9 | consolidated balance sheet, ii) Cash and cash equivalents | 2 |  |
R584-R585 | p9 | consolidated balance sheet, iii) Bank balances other than (ii) above | 2 | OCR_CONFLICT x1 |
R586-R587 | p9 | consolidated balance sheet, iv) Loans (current) | 2 | OCR_CONFLICT x1 |
R588-R589 | p9 | consolidated balance sheet, v) Others financial assets (current) | 2 |  |
R590-R591 | p9 | consolidated balance sheet, Total non-current assets | 2 | OCR_CONFLICT x2 |
R592-R593 | p9 | consolidated balance sheet, Other current assets | 2 |  |
R594-R595 | p9 | consolidated balance sheet, Total equity and liabilities | 2 | OCR_CONFLICT x2 |
R596-R597 | p9 | consolidated balance sheet, Equity share capital | 2 |  |
R598-R599 | p9 | consolidated balance sheet, Other equity | 2 | OCR_CONFLICT x2 |
R600-R601 | p9 | consolidated balance sheet, Total equity | 2 | OCR_CONFLICT x2 |
R602-R603 | p9 | consolidated balance sheet, Total non-current liabilities | 2 | OCR_CONFLICT x2 |
R604-R605 | p9 | consolidated balance sheet, Non-current i) Borrowings | 2 |  |
R606-R607 | p9 | consolidated balance sheet, Non-current ii) Lease liabilities | 2 | OCR_CONFLICT x1 |
R608-R609 | p9 | consolidated balance sheet, Non-current Provisions | 2 |  |
R610-R611 | p9 | consolidated balance sheet, Deferred tax liabilities (net) | 2 | OCR_CONFLICT x1 |
R612-R613 | p9 | consolidated balance sheet, Other non-current liabilities | 2 | OCR_CONFLICT x1 |
R614-R615 | p9 | consolidated balance sheet, Total current liabilities | 2 | OCR_CONFLICT x2 |
R616-R617 | p9 | consolidated balance sheet, Current i) Borrowings | 2 | OCR_CONFLICT x1 |
R618-R619 | p9 | consolidated balance sheet, Current ii) Lease liabilities | 2 |  |
R620-R621 | p9 | consolidated balance sheet, iii)(a) Trade payables, dues of micro enterprises and small enterprises | 2 | OCR_CONFLICT x1 |
R622-R623 | p9 | consolidated balance sheet, iii)(b) Trade payables, dues of creditors other than micro and small enterprises | 2 |  |
R624-R625 | p9 | consolidated balance sheet, iv) Other financial liabilities | 2 | OCR_CONFLICT x1 |
R626-R627 | p9 | consolidated balance sheet, Other current liabilities | 2 |  |
R628-R629 | p9 | consolidated balance sheet, Current Provisions | 2 |  |
R630-R631 | p9 | consolidated balance sheet, Current tax liabilities (net) | 2 |  |
R633-R634 | p10 | consolidated cash flow, Cash generated from operations | 2 | OCR_CONFLICT x2 |
R635-R636 | p10 | consolidated cash flow, Income tax paid (net of refunds) | 2 |  |
R637-R638 | p10 | consolidated cash flow, Net profit before tax | 2 | OCR_CONFLICT x1 |
R639-R640 | p10 | consolidated cash flow, Depreciation and amortisation expense | 2 | OCR_CONFLICT x2 |
R641-R642 | p10 | consolidated cash flow, Loss/(gain) on disposal of PPE | 2 | OCR_CONFLICT x1 |
R643-R644 | p10 | consolidated cash flow, Rental income (adjustment) | 2 | OCR_CONFLICT x1 |
R645-R646 | p10 | consolidated cash flow, Rental income (investing) | 2 | OCR_CONFLICT x1 |
R647-R648 | p10 | consolidated cash flow, Provision for expected credit loss | 2 | OCR_CONFLICT x2 |
R649-R650 | p10 | consolidated cash flow, Expenses on employees stock options scheme | 2 | OCR_CONFLICT x2 |
R651-R652 | p10 | consolidated cash flow, Excess provisions written back | 2 |  |
R653-R654 | p10 | consolidated cash flow, Finance cost | 2 | OCR_CONFLICT x1 |
R655-R656 | p10 | consolidated cash flow, Unrealised foreign exchange gain | 2 |  |
R657-R658 | p10 | consolidated cash flow, Finance income | 2 |  |
R659-R660 | p10 | consolidated cash flow, Share of profit/(loss) of an associate and joint venture (net of tax) | 2 |  |
R661-R662 | p10 | consolidated cash flow, Foreign currency translation reserve | 2 | OCR_CONFLICT x2 |
R663-R664 | p10 | consolidated cash flow, Operating profit before working capital changes | 2 |  |
R665-R666 | p10 | consolidated cash flow, (Increase)/decrease in inventories | 2 | OCR_CONFLICT x1 |
R667-R668 | p10 | consolidated cash flow, (Increase)/decrease in trade receivables | 2 |  |
R669-R670 | p10 | consolidated cash flow, (Increase)/decrease in other financial assets | 2 |  |
R671-R672 | p10 | consolidated cash flow, (Increase)/decrease in other assets | 2 | OCR_CONFLICT x1 |
R673-R674 | p10 | consolidated cash flow, Increase/(decrease) in trade payables | 2 | OCR_CONFLICT x1 |
R675-R676 | p10 | consolidated cash flow, Increase/(decrease) in other financial liabilities | 2 | OCR_CONFLICT x1 |
R677-R678 | p10 | consolidated cash flow, Increase/(decrease) in other liabilities | 2 |  |
R679-R680 | p10 | consolidated cash flow, Increase/(decrease) in provisions | 2 |  |
R681-R682 | p10 | consolidated cash flow, Net cash flow generated from operating activities (A) | 2 | OCR_CONFLICT x2 |
R683-R684 | p10 | consolidated cash flow, Purchase of property plant & equipment (net of capital advances and capital payables) | 2 |  |
R685-R686 | p10 | consolidated cash flow, Proceeds from sale of property, plant and equipment | 2 |  |
R687-R688 | p10 | consolidated cash flow, Loan given & received back | 2 |  |
R689-R690 | p10 | consolidated cash flow, Investment in associate and joint venture | 2 | ZERO_STANDING x1 |
R691-R692 | p10 | consolidated cash flow, Proceeds from sale of investment | 2 | ZERO_STANDING x1 |
R693-R694 | p10 | consolidated cash flow, Interest received | 2 |  |
R695-R696 | p10 | consolidated cash flow, (Investing in)/redemption of term deposit | 2 |  |
R697-R698 | p10 | consolidated cash flow, Net cash flow (used) in investing activities (B) | 2 | OCR_CONFLICT x2 |
R699-R700 | p10 | consolidated cash flow, Proceed from issue of equity shares | 2 | ZERO_STANDING x1 |
R701-R702 | p10 | consolidated cash flow, Proceeds of long term borrowings | 2 | OCR_CONFLICT x1 |
R703-R704 | p10 | consolidated cash flow, Repayments from long term borrowings | 2 |  |
R705-R706 | p10 | consolidated cash flow, Proceeds/(repayment) of short term borrowings | 2 | OCR_CONFLICT x1 |
R707-R708 | p10 | consolidated cash flow, Payment of principal portion of lease liabilities | 2 | OCR_CONFLICT x1 |
R709-R710 | p10 | consolidated cash flow, Payment of interest on lease liabilities | 2 |  |
R711-R712 | p10 | consolidated cash flow, Dividend paid | 2 | OCR_CONFLICT x2 |
R713-R714 | p10 | consolidated cash flow, Interest paid | 2 |  |
R715-R716 | p10 | consolidated cash flow, Net cash flow from/(used) in financing activities (C) | 2 |  |
R717-R718 | p10 | consolidated cash flow, Net increase/(decrease) in cash and cash equivalents (A+B+C) | 2 | OCR_CONFLICT x2 |
R719-R720 | p10 | consolidated cash flow, Cash and cash equivalents at the beginning of the period | 2 | OCR_CONFLICT x2 |
R721-R722 | p10 | consolidated cash flow, Cash and cash equivalents at the end of the period | 2 |  |

## 2b. NON-STATEMENT NUMBERS (identifiers, note figures, auditor figures)

ID_RANGE | page | what | cells | flags
R001 | page 1 | BSE scrip code | 1 | 
R002 | page 1 | ISIN | 1 | 
R003 | page 1 | LODR regulations cited | 1 | 
R004 | page 1 | company secretary membership no. | 1 | 
R005 | page 1 | CIN (letterhead) | 1 | OCR_ONLY
R006 | page 1 | registered office PIN (letterhead) | 1 | OCR_ONLY
R007 | page 1 | telephone (letterhead) | 1 | OCR_ONLY
R008 | page 1 | fax (letterhead) | 1 | OCR_ONLY
R009 | page 2 | telephone | 1 | 
R010 | page 2 | fax | 1 | 
R011 | page 2 | CIN | 1 | 
R144 | page 2 | face value per equity share (standalone P&L) | 1 | 
R169 | page 2 | director DIN | 1 | 
R170 | page 3 | CIN | 1 | 
R249 | page 3 | director DIN (read from image) | 1 | IMAGE_READ
R336 | page 4 | director DIN | 1 | 
R337 | page 5 | Chile SpA authorised capital | 1 | 
R338 | page 5 | Chile SpA face value per share | 1 | OCR_CORRECTED
R339 | page 5 | Panipat land area | 1 | 
R340 | page 5 | land released from acquisition | 1 | 
R341 | page 5 | HSIIDC demand for allotment of land | 1 | 
R342 | page 5 | Chile SpA authorised share count (OCR layer value; embedded layer reads S,00,00,000) | 1 | OCR_CORRECTED
R343 | page 7 | auditor firm registration no. | 1 | 
R344 | page 7 | partner membership no. | 1 | 
R345 | page 7 | UDIN standalone | 1 | 
R346 | page 8 | CIN | 1 | OCR_SPACE
R527 | page 8 | face value per equity share (consolidated P&L) | 1 | 
R552 | page 8 | director DIN | 1 | IMAGE_READ
R553 | page 9 | CIN | 1 | 
R632 | page 9 | director DIN | 1 | 
R723 | page 10 | director DIN | 1 | IMAGE_READ
R724 | page 11 | Chile SpA authorised capital | 1 | 
R725 | page 11 | Chile SpA authorised share count | 1 | 
R726 | page 11 | Chile SpA face value per share | 1 | 
R727 | page 11 | Panipat land area | 1 | 
R728 | page 11 | land released from acquisition | 1 | 
R729 | page 11 | HSIIDC demand for allotment of land | 1 | 
R730 | page 13 | count of unreviewed subsidiaries | 1 | 
R731 | page 13 | unreviewed subsidiaries total assets at 30 Sep 2026 | 1 | 
R732-R745 | page 13 | unreviewed subsidiaries total revenues | 2 | OCR_CORRECTED
R733-R734 | page 13 | unreviewed subsidiaries net profit after tax | 2 | 
R735-R736 | page 13 | unreviewed subsidiaries total comprehensive income | 2 | 
R737 | page 13 | unreviewed subsidiaries net cash inflows | 1 | 
R738-R739 | page 13 | Group share of net loss after tax, JV | 2 | 
R740-R741 | page 13 | Group share of OCI loss, JV | 2 | 
R742 | page 13 | count of JV unreviewed | 1 | 
R743 | page 13 | partner membership no. | 1 | 
R744 | page 13 | UDIN consolidated | 1 | 

## 3. AGENDA ITEMS / BOARD OUTCOME LETTER (page 1)
ID | item | flags / note
R813,R814,R815,R816 | Item 1: approval of un-audited standalone and consolidated results Q2/H1 FY27, meeting 22-Oct-2026 | only agenda item in letter; no AR, AGM, dividend, director, auditor, ESOP or capital-raise items present (absence noted, not interpreted)
R858,R753,R754 | results status, limited review by statutory auditors, Audit Committee recommendation | -
R817,R818 | meeting start 11:30 AM and end 02:05 PM (2h35m) | duration recorded
R819,R859,R755,R004 | digital signature: Sanjay Kumar Rawat, Company Secretary, ACS23729, timestamp 14:10:06 +05:30 | signature 5 min after meeting end 02:05 PM; not before conclusion, no flag
R860,R752,R001,R002,R003,R746,R747,R748,R749,R750,R751 | enclosure line, regulation, addressees, scrip identifiers | -
R756,R757,R758,R759,R005,R006,R007,R008 | letterhead contact details | OCR_ONLY

## 4. AUDITOR PARAS (limited review reports)
PARA | report | IDs | flags
Title/addressing | standalone | R889,R778 | -
Para 1 (scope, statement reviewed) | standalone | R836,R837 | -
Para 2 (management responsibility) | standalone | R890 | -
Para 3 (SRE 2410 review, moderate assurance) | standalone | R890 | -
Para 4 (conclusion, unmodified) | standalone | R891 | -
Para 5 (Emphasis of Matter, Note 5 HSIIDC Panipat) | standalone | R893 | EOM; cross-ref R884-R888
Sign-off (firm FRN, partner, UDIN, date) | standalone | R779,R780,R343,R344,R345,R838,R892,R894 | UDIN given
Title | consolidated | R921,R796 | -
Para 1 (statement reviewed) | consolidated | R854,R855 | -
Para 2 (management responsibility) | consolidated | R922 | -
Para 3 (SRE 2410 / Reg 33(8)) | consolidated | R922,R923 | -
Para 4 (entities included) | consolidated | R797,R798,R799,R800,R801 | entity list; see entities
Para 5 (conclusion, unmodified) | consolidated | R924 | -
Para 6 (Emphasis of Matter) | consolidated | R925 | EOM; RESTATED with R893
Para 7 (Other matter: 2 subsidiaries + 1 JV unreviewed, management-certified) | consolidated | R926,R856,R730,R731,R732,R745,R733,R734,R735,R736,R737,R738,R739,R740,R741,R742 | UNREVIEWED_ENTITIES
Sign-off (partner, UDIN, date, page marker) | consolidated | R802,R743,R744,R857,R927 | PAGE_MISSING: page 3 of 3 absent (R927)

## 5. ENTITIES
ID | entity | relationship | flags
R797 | Tinna Rubber and Infrastructure Limited | Parent | -
R798 | Tinna Rubber Arabia Ltd (Saudi Arabia) | wholly owned subsidiary | -
R799 | Global Recycle LLC (Oman) | wholly owned subsidiary | -
R800 | T.P. Buildtech Private Limited (India) | associate | -
R801 | Mbodla Investment (PTY) Limited (South Africa) | joint venture | -
R773,R791 | Tinna Rubber Chile SpA | wholly owned subsidiary per Note 4 | CONSOLIDATION_LIST_GAP: named in Note 4 but absent from auditor para-4 entity list R797-R801. Prior list absent so ENTITY_CHANGE not testable. A3 to resolve.
R746-R759,R760,R761 | exchanges, company, regulators, letterhead items | page 1-2 | -
R762-R768,R781-R786 | signature blocks and auditor stamps (MD Bhupinder Kumar Sekhri; S S Kothari Mehta & Co LLP) pages 2,3,4,8,9,10 | IMAGE_READ | signatory per statement
R769-R772,R787-R790 | products (Crumb Rubber, CRM, Bitumen/Modified Bitumen, Emulsion) | segment | R771 'Bitumen' vs R789 'Modified Bitumen' wording differs standalone vs consolidated
R774,R792 | Panipat plant | plant | -
R775,R793,R776,R794,R777,R795 | HSIIDC, Supreme Court, Principal Secretary Haryana | land dispute parties | cross-ref Note 5
R778,R779,R780,R796,R802 | auditor firm and partner | auditor | -

## 6. FORWARD / DATE / QUALIFIER (all rows referenced)
IDS | category | flags
R803-R812 | FORWARD (10) | RESTATED pairs: R803/R808, R804/R809, R805/R810, R806/R811, R807/R812
R813-R857 | DATE (45) | R822 DATE_CONFLICT: embedded layer reads 21-Oct-2026 on standalone BS page, OCR and image read 22-Oct-2026 (R826, R871)
R858-R927 | QUALIFIER (70) | IMAGE_READ, OCR_SPELLING, R906 OCR digit conflict (ROU assets), R866 OCI dashes in period columns, R869 stray dash EPS cell

## 7. ZERO_STANDING cells (81; every one is also in section 2 group rows)
R096 R097 R098 R099 R120 R121 R122 R123 R124 R126 R127 R128 R129 R130 R132 R133 R134 R135 R136 R138 R139 R140 R141 R142 R151 R152 R153 R154 R155 R192 R271 R304 R312 R321 R323 R443 R444 R445 R446 R461 R462 R463 R464 R465 R467 R468 R469 R470 R471 R473 R474 R475 R476 R477 R485 R486 R487 R488 R489 R490 R503 R504 R505 R506 R507 R508 R509 R510 R511 R512 R513 R514 R534 R535 R536 R537 R538 R571 R689 R691 R699
Zero-standing line items (group, cells): SA P&L tax of earlier years (4), OCI total and OCI a/b/c (5 each), Other equity cells (5); SA BS non-current loans (1); SA CF unrealised FX, proceeds from sale of investment, proceeds from issue of equity, lease principal, lease interest (1 each); CO P&L tax of earlier years (4), OCI a/b/c (5 each), Associates OCI (6), NCI profit (6), NCI TCI (6), Other equity (5); CO BS non-current loans (1); CO CF investment in associate/JV, sale of investment, equity issue (1 each). Template signals: equity issue, investment sale, lease payments, NCI and associate OCI lines exist but are nil.
