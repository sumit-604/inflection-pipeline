# LEDGER (A2 ENUMERATOR) - Paisalo Digital Limited (PAISALO) - Q2 FY27 - results filing
# Enumeration source: A1 structured file only. Fulltext used for the grep half of the count test only.
# Row format: ROW_ID | category | A2 flags | cross-ref / materiality. Claim text stays in the structured file at the cited ID.
# Units: statements Rs Lakhs; note 5 issuance table Rs Cr. Lender (NBFC). No prior-quarter ledger: ENTITY_CHANGE diffs cannot be run (baseline quarter).
=== A2 COUNT TEST ===
category: notes            grep_count: 9     sweep_count: 9     match: yes 
category: footnotes        grep_count: 8     sweep_count: 8     match: yes 
category: line_items       grep_count: 283   sweep_count: 283   match: yes (statements 251+ratio 22+note5 10; sweep includes 8 MISSING_FROM_STRUCTURED ratio rows)
category: zero_standing_rows grep_count: 402   sweep_count: 402   match: yes (dash-valued NUMBER rows vs A1 ZERO_STANDING flags; A2 adds 0.00 ratio l x2 and Nil ratio d x2 on top)
category: agenda_items     grep_count: 2     sweep_count: 2     match: yes 
category: auditor_paras    grep_count: 10    sweep_count: 10    match: yes 
category: entities         grep_count: 92    sweep_count: 92    match: yes 
category: signature_blocks grep_count: 10    sweep_count: 10    match: yes 
category: dates            grep_count: 78    sweep_count: 78    match: yes 
category: qualifiers       grep_count: 62    sweep_count: 62    match: yes 
category: numbers          grep_count: 1140  sweep_count: 1140  match: yes 
category: forward          grep_count: 0     sweep_count: 0     match: yes 
ids_in_structured: 1372 | ids_referenced_in_ledger: 1372 | orphan_ids: [] | match: yes
missing_from_structured: 8 ratio-table rows (b, c, d, f value, o, p, q, s), see section 2B
gate_a2: pass
=== END COUNT TEST ===

## 1. NOTES (numbered notes 1-9, then unnumbered notes and footnotes)
ROW_ID(s) | category | A2 flags | cross-ref / materiality
R1013-R1015,R1186,R1288,R1339 | NOTE 1 |  | board approval date and statutory auditor review (review, not audit)
R1187-R1188,R1340 | NOTE 2 |  | defines consolidation scope: sole subsidiary Nupur Finvest (R1187)
R1016-R1021,R1189,R1341 | NOTE 3 |  | basis of preparation (Ind AS, Regs 33/52/63)
R1022,R1190,R1342 | NOTE 4 |  | single segment: financing; no segment table exists
R1023-R1065,R1191-R1200,R1289-R1299,R1343-R1350 | NOTE 5 |  | issuance table = 10 line items, see section 2C; amounts in Rs Cr (unit differs from statements)
R1066-R1070,R1201,R1351 | NOTE 6 |  | share issue on FCCB conversion; cross-ref paid-up capital lines (SA R266-R272; CON R780-R786) and FCCB entity R1201
R1352 | NOTE 7 | RESTATED_COMPARATIVES(unquantified) | comparatives reclassified or regrouped; prior-period figures not strictly like-for-like
R1071,R1202,R1300,R1353-R1354 | NOTE 8 |  | asset cover on secured NCDs; ties to note 5 secured series
R1072-R1105,R1203-R1204,R1301-R1306,R1355-R1364 | NOTE 9 |  | Reg 52(4)/52(6) ratio table; row-level items in section 2B
R1333 | FOOTNOTE (unnumbered) | FOOTNOTE_UNRESOLVED | asterisk with no footnote text on page 5
R1346 | FOOTNOTE (unnumbered) |  | CP series 1 discounted price
R1348 | FOOTNOTE (unnumbered) |  | CP series 2 discounted price
R1350 | FOOTNOTE (unnumbered) |  | CP series 3 discounted price
R1358 | FOOTNOTE (unnumbered) |  | DRR exemption footnote under ratio f
R1360 | FOOTNOTE (unnumbered) |  | Net Worth definition footnote under ratio g
R1368 | FOOTNOTE (unnumbered) | FOOTNOTE_UNRESOLVED | UDIN text garbled (standalone review report)
R1230-R1232 | FOOTNOTE-class identifier | FOOTNOTE_UNRESOLVED | consolidated review report UDIN garbled in text layer (same cause as R1368)

## 2. LINE ITEMS
### 2A. Financial statements pages 2-7 (one row per statement line; IDs cover all period columns)
ROW_ID(s) | statement/page/line | A2 flags | label; SA-CON pair
R014-R019 | SA-P&L p2 l799 |  | I Revenue from operations > (i) Interest Income; CON pair R492-R497
R020-R025 | SA-P&L p2 l800 | ZERO_STANDING(2/6 cols) | I Revenue from operations > (ii) Dividend Income; CON pair R498-R503
R026-R031 | SA-P&L p2 l801 | ZERO_STANDING(all periods) | (iii) Rental Income; CON pair R504-R509
R032-R037 | SA-P&L p2 l802 |  | (iv) Fees and commission Income; CON pair R510-R515
R038-R043 | SA-P&L p2 l803 | ZERO_STANDING(2/6 cols) | (v) Net gain on fair value changes; CON pair R516-R521
R044-R049 | SA-P&L p2 l804 | ZERO_STANDING(all periods) | (vi) Net gain on derecognition of financial inst; CON pair R522-R527
R050-R055 | SA-P&L p2 l805 | ZERO_STANDING(all periods) | (vii) Sale of products (including Excise Duty); CON pair R528-R533
R056-R061 | SA-P&L p2 l806 | ZERO_STANDING(all periods) | (viii) Sale of services; CON pair R534-R539
R062-R067 | SA-P&L p2 l807 | ZERO_STANDING(all periods) | (ix) Others; CON pair R540-R545
R068-R073 | SA-P&L p2 l808 |  | Total Revenue from operations (I); CON pair R546-R551
R074-R079 | SA-P&L p2 l809 | ZERO_STANDING(all periods) | I Revenue from operations > II Other Income; CON pair R552-R557
R080-R085 | SA-P&L p2 l810 |  | Total Income (I+II); CON pair R558-R563
R086-R091 | SA-P&L p2 l812 |  | III Expenses > (i) Finance Costs; CON pair R564-R569
R092-R097 | SA-P&L p2 l813 | ZERO_STANDING(all periods) | III Expenses > (ii) Fees and commission expense; CON pair R570-R575
R098-R100,R103,R105-R106 | SA-P&L p2 l814 | ZERO_STANDING(3/6 cols) | (iii) Net loss on fair value changes; CON pair R576-R578,R581,R583-R584
R101-R102,R104,R107-R109 | SA-P&L p2 l815 | ZERO_STANDING(all periods) | (iv) Net loss on derecognition of financial inst; CON pair R579-R580,R582,R585-R587
R110-R112,R115,R117-R118 | SA-P&L p2 l816 |  | (v) Impairment on financial instruments; CON pair R588-R590,R593,R595-R596
R113-R114,R116,R119-R121 | SA-P&L p2 l817 | ZERO_STANDING(all periods) | (vi) Cost of materials consumed; CON pair R591-R592,R594,R597-R599
R122-R127 | SA-P&L p2 l818 | ZERO_STANDING(all periods) | (vii) Purchases of Stock-in-trade; CON pair R600-R605
R128-R133 | SA-P&L p2 l819 | ZERO_STANDING(all periods) | (viii) Changes in Inventories of finished goods,; CON pair R606-R611
R134-R136,R139,R141-R142 | SA-P&L p2 l820 |  | (ix) Employee Benefits Expenses; CON pair R612-R614,R617,R619-R620
R137-R138,R140,R143-R145 | SA-P&L p2 l821 |  | (x) Depreciation, amortization and impairment; CON pair R615-R616,R618,R621-R623
R146-R149,R152,R154 | SA-P&L p2 l822 |  | (xi) Other expenses; no consolidated pair by label
R150-R151,R153,R155-R157 | SA-P&L p2 l823 |  | Total Expenses (III); CON pair R628-R629,R631,R633-R635
R158-R163 | SA-P&L p2 l824 |  | III Expenses > IV Profit/(loss) before exception; CON pair R636-R641
R164-R169 | SA-P&L p2 l825 | ZERO_STANDING(5/6 cols) | III Expenses > V Exceptional items; CON pair R642-R647
R170-R175 | SA-P&L p2 l826 |  | III Expenses > VI Profit/(loss) before tax (IV-V; CON pair R648-R653
R176-R181 | SA-P&L p2 l828 |  | VII Tax Expense > (1) Current Tax; CON pair R654-R659
R182-R187 | SA-P&L p2 l829 |  | VII Tax Expense > (2) Deferred Tax; CON pair R660-R665
R188-R193 | SA-P&L p2 l830 |  | VIII Profit/(loss) for the period from continuin; CON pair R666-R671
R194-R199 | SA-P&L p2 l831 | ZERO_STANDING(all periods) | IX Profit/(loss) from discontinued operations; CON pair R672-R677
R200-R205 | SA-P&L p2 l832 | ZERO_STANDING(all periods) | X Tax Expense of discontinued operations; CON pair R678-R683
R206-R211 | SA-P&L p2 l833 | ZERO_STANDING(all periods) | XI Profit/(loss) from discontinued operations (A; CON pair R684-R689
R212-R217 | SA-P&L p2 l834 |  | XII Profit/(loss) for the period (VIII+XI); CON pair R690-R695
R218-R223 | SA-P&L p2 l836 | ZERO_STANDING(all periods) | (A) (i) Items that will not be reclassified to p; CON pair R696-R701
R224-R229 | SA-P&L p2 l837 | ZERO_STANDING(all periods) | XIII Other Comprehensive Income > (ii) Income ta; CON pair R702-R707
R230-R235 | SA-P&L p2 l838 | ZERO_STANDING(all periods) | Subtotal (A); CON pair R708-R713
R236-R241 | SA-P&L p2 l839 | ZERO_STANDING(all periods) | (B) (i) Items that will be reclassified to profi; CON pair R714-R719
R242-R247 | SA-P&L p2 l840 | ZERO_STANDING(all periods) | XIII Other Comprehensive Income > (ii) Income ta; CON pair R702-R707
R248-R253 | SA-P&L p2 l841 | ZERO_STANDING(all periods) | Subtotal (B); CON pair R726-R731
R254-R259 | SA-P&L p2 l842 | ZERO_STANDING(all periods) | Other Comprehensive Income (A+B); CON pair R732-R737
R260-R265 | SA-P&L p2 l843 |  | XIV Total Comprehensive Income for the period; CON pair R738-R743
R266-R272 | SA-P&L p2 l845 |  | XV Paid-up equity share capital (face value of R; no consolidated pair by label
R273-R278 | SA-P&L p2 l846 | ZERO_STANDING(5/6 cols) | XVI Other equity as per statement of assets and ; no consolidated pair by label
R279-R284 | SA-P&L p2 l848 |  | XVII Earnings per equity share (for continuing o; no consolidated pair by label
R285-R290 | SA-P&L p2 l849 |  | XVII Earnings per equity share (for continuing o; no consolidated pair by label
R291-R296 | SA-P&L p2 l853 | ZERO_STANDING(all periods) | Earnings per equity share (for discontinued oper; no consolidated pair by label
R297-R302 | SA-P&L p2 l854 | ZERO_STANDING(all periods) | Earnings per equity share (for discontinued oper; no consolidated pair by label
R303-R308 | SA-P&L p2 l856 |  | XIX Earnings per equity share (for continuing an; no consolidated pair by label
R309-R314 | SA-P&L p2 l857 |  | XIX Earnings per equity share (for continuing an; no consolidated pair by label
R315,R317 | SA-BS p3 l880 |  | (a) Cash & Cash Equivalents; CON pair R829,R831
R316,R319 | SA-BS p3 l881 |  | (b) Bank Balances other than (a) above; CON pair R830,R833
R318,R320 | SA-BS p3 l882 | ZERO_STANDING(all periods) | (c) Derivative Financial Instruments; CON pair R832,R834
R321,R323 | SA-BS p3 l884 |  | (i) Trade Receivables; CON pair R835,R837
R322,R324 | SA-BS p3 l885 | ZERO_STANDING(all periods) | (ii) Other Receivables; CON pair R836,R838
R325,R327 | SA-BS p3 l886 |  | (e) Loans; CON pair R839,R841
R326,R329 | SA-BS p3 l887 |  | (f) Investments; CON pair R840,R843
R328,R330 | SA-BS p3 l888 |  | (g) Other Financial Assets; CON pair R842,R844
R331,R333 | SA-BS p3 l890 | ZERO_STANDING(1/2 cols) | (a) Current Tax Assets (Net); CON pair R845,R847
R332,R334 | SA-BS p3 l891 | ZERO_STANDING(all periods) | (b) Deferred Tax Asset (Net); CON pair R846,R848
R335-R336 | SA-BS p3 l892 | ZERO_STANDING(all periods) | (c) Investment Property; CON pair R849-R850
R337,R339 | SA-BS p3 l893 | ZERO_STANDING(all periods) | (d) Biological Assets other than Bearer plants; CON pair R851,R853
R338,R342 | SA-BS p3 l894 |  | (e) Property, Plant and Equipments; CON pair R852,R856
R340-R341 | SA-BS p3 l895 | ZERO_STANDING(all periods) | (f) Capital Work-in-Progress; CON pair R854-R855
R343-R344 | SA-BS p3 l896 | ZERO_STANDING(all periods) | (g) Intangible Assets under development; CON pair R857-R858
R345,R350 | SA-BS p3 l898 |  | (i) Other Intangible Assets; CON pair R859,R864
R346,R348 | SA-BS p3 l897 | ZERO_STANDING(all periods) | (h) Goodwill; CON pair R860,R862
R347,R352 | SA-BS p3 l899 |  | (j) Other Non-Financial Assets; CON pair R861,R866
R349,R353 | SA-BS p3 l900 |  | Total Assets; CON pair R863,R867
R351,R356 | SA-BS p3 l903 | ZERO_STANDING(all periods) | (a) Derivative Financial Instruments; CON pair R865,R870
R354,R358 | SA-BS p3 l906 |  | (I) Trade Payables > (i) Total outstanding dues ; CON pair R868,R872
R355,R360 | SA-BS p3 l907 |  | (I) Trade Payables > (ii) Total outstanding dues; CON pair R869,R874
R357,R363 | SA-BS p3 l909 | ZERO_STANDING(all periods) | (II) Other Payables > (i) Total outstanding dues; CON pair R871,R877
R359,R364 | SA-BS p3 l910 |  | (II) Other Payables > (ii) Total outstanding due; CON pair R873,R878
R361,R366 | SA-BS p3 l911 |  | (c) Debt Securities; CON pair R875,R880
R362,R368 | SA-BS p3 l912 |  | (d) Borrowings (Other than Debt Securities); CON pair R876,R882
R365,R370 | SA-BS p3 l913 | ZERO_STANDING(all periods) | (e) Deposits; CON pair R879,R884
R367,R372 | SA-BS p3 l914 |  | (f) Subordinated Liabilities; CON pair R881,R886
R369,R374 | SA-BS p3 l915 |  | (g) Other Financial Liabilities; CON pair R883,R888
R371,R377 | SA-BS p3 l917 | ZERO_STANDING(1/2 cols) | (a) Current Tax Liabilities (Net); CON pair R885,R891
R373,R378 | SA-BS p3 l918 |  | (b) Provisions; CON pair R887,R892
R375,R380 | SA-BS p3 l919 |  | (c) Deferred Tax Liabilities (Net); CON pair R889,R894
R376,R383 | SA-BS p3 l920 |  | (d) Other non-financial Liabilities; CON pair R890,R897
R379,R384 | SA-BS p3 l922 |  | (a) Equity Share Capital; CON pair R893,R899
R381,R385 | SA-BS p3 l923 |  | (b) Other Equity; CON pair R895,R901
R382,R386 | SA-BS p3 l924 |  | Total Equity & Liabilities; CON pair R896,R902
R387-R389 | SA-CF p4 l947 |  | Net Profit before tax and extraordinary items an; CON pair R908-R910
R390-R391,R394 | SA-CF p4 l949 |  | Adjustments for > I Depreciation; CON pair R911-R912,R915
R392-R393,R397 | SA-CF p4 l950 |  | Adjustments for > II Deferred Expense W/O; CON pair R913-R914,R918
R395-R396,R400 | SA-CF p4 l951 |  | Adjustments for > III Impairment on financial in; CON pair R916-R917,R921
R398-R399,R401 | SA-CF p4 l952 |  | Adjustments for > IV Expenditure on CSR; CON pair R919-R920,R922
R402-R403,R406 | SA-CF p4 l953 | ZERO_STANDING(1/3 cols) | Adjustments for > V Dividend Income; CON pair R923-R924,R927
R404-R405,R407 | SA-CF p4 l954 |  | Adjustments for > VI Profit/Loss on Sale of Shar; CON pair R925-R926,R928
R408-R409,R412 | SA-CF p4 l955 |  | Adjustments for > VII Profit/Loss on Sale of Inv; CON pair R929-R931
R410-R411,R413 | SA-CF p4 l956 |  | Operating Profit before working capital changes; CON pair R932-R934
R414-R415,R418 | SA-CF p4 l958 |  | Adjustments for > I Change in Other Financial As; CON pair R935-R937
R416-R417,R419 | SA-CF p4 l959 |  | Adjustments for > II Change in Loans & Receivabl; CON pair R938-R940
R420-R421,R424 | SA-CF p4 l960 |  | Adjustments for > III Change in Payable & non fi; CON pair R941-R943
R422-R423,R426 | SA-CF p4 l961 | ZERO_STANDING(1/3 cols) | Adjustments for > IV Change in other non-financi; CON pair R944-R946
R425,R427-R428 | SA-CF p4 l962 |  | Cash generated from Operations; CON pair R947-R949
R429,R431-R432 | SA-CF p4 l963 |  | Adjustments for > I Interest paid; CON pair R950-R951,R953
R430,R434-R435 | SA-CF p4 l964 |  | Adjustments for > II Income Tax paid; CON pair R952,R954,R956
R433,R436-R437 | SA-CF p4 l965 |  | Adjustments for > III Paid Expenses on CSR; CON pair R955,R957-R958
R438-R440 | SA-CF p4 l966 |  | Cash flow before Extraordinary Items; CON pair R959-R961
R441,R443-R444 | SA-CF p4 l967 | ZERO_STANDING(2/3 cols) | Adjustments for > I Extraordinary items; CON pair R962-R963,R965
R442,R445-R446 | SA-CF p4 l968 |  | Net Cash from Operating Activities; CON pair R964,R966-R967
R447,R449-R450 | SA-CF p4 l970 |  | B Cash Flows from Investing Activities > I Purch; CON pair R968-R969,R971
R448,R451-R452 | SA-CF p4 l971 |  | B Cash Flows from Investing Activities > II Sale; CON pair R970,R972-R973
R453-R454,R456 | SA-CF p4 l972 | ZERO_STANDING(1/3 cols) | B Cash Flows from Investing Activities > III Pur; CON pair R974-R975,R977
R455,R457-R458 | SA-CF p4 l973 |  | Net Cash from Investing activities; CON pair R976,R978-R979
R459,R461-R462 | SA-CF p4 l975 |  | C Net Cash from Financing Activities > I Proceed; CON pair R980-R981,R983
R460,R463-R464 | SA-CF p4 l976 |  | C Net Cash from Financing Activities > II Procee; CON pair R982,R984-R985
R465-R466,R469 | SA-CF p4 l977 |  | C Net Cash from Financing Activities > III Proce; CON pair R986-R988
R467-R468,R471 | SA-CF p4 l978 | ZERO_STANDING(2/3 cols) | C Net Cash from Financing Activities > IV Procee; CON pair R989-R991
R470,R472,R474 | SA-CF p4 l979 | ZERO_STANDING(1/3 cols) | C Net Cash from Financing Activities > V Dividen; CON pair R992-R994
R473,R475-R476 | SA-CF p4 l980 | ZERO_STANDING(1/3 cols) | C Net Cash from Financing Activities > VI Purcha; CON pair R995-R997
R477-R479 | SA-CF p4 l981 |  | C Net Cash from Financing Activities > VII Money; CON pair R998-R1000
R480-R482 | SA-CF p4 l982 |  | Net Cash from Financing activities; CON pair R1001-R1003
R483-R484,R486 | SA-CF p4 l983 |  | Net Increase/(decrease) in cash & cash equivalen; CON pair R1004-R1006
R485,R487-R488 | SA-CF p4 l984 |  | Cash & Cash equivalents at beginning of period; CON pair R1007-R1009
R489-R491 | SA-CF p4 l985 |  | Cash & Cash equivalent at end of period; CON pair R1010-R1012
R492-R497 | CON-P&L p5 l1004 |  | I Revenue from operations > (i) Interest Income; SA pair R014-R019
R498-R503 | CON-P&L p5 l1005 | ZERO_STANDING(2/6 cols) | I Revenue from operations > (ii) Dividend Income; SA pair R020-R025
R504-R509 | CON-P&L p5 l1006 | ZERO_STANDING(all periods) | (iii) Rental Income; SA pair R026-R031
R510-R515 | CON-P&L p5 l1007 |  | (iv) Fees and commission Income; SA pair R032-R037
R516-R521 | CON-P&L p5 l1008 | ZERO_STANDING(2/6 cols) | (v) Net gain on fair value changes; SA pair R038-R043
R522-R527 | CON-P&L p5 l1009 | ZERO_STANDING(all periods) | (vi) Net gain on derecognition of financial inst; SA pair R044-R049
R528-R533 | CON-P&L p5 l1010 | ZERO_STANDING(all periods) | (vii) Sale of products (including Excise Duty); SA pair R050-R055
R534-R539 | CON-P&L p5 l1011 | ZERO_STANDING(all periods) | (viii) Sale of services; SA pair R056-R061
R540-R545 | CON-P&L p5 l1012 | ZERO_STANDING(all periods) | (ix) Others; SA pair R062-R067
R546-R551 | CON-P&L p5 l1013 |  | Total Revenue from operations (I); SA pair R068-R073
R552-R557 | CON-P&L p5 l1014 | ZERO_STANDING(all periods) | I Revenue from operations > II Other Income; SA pair R074-R079
R558-R563 | CON-P&L p5 l1015 |  | Total Income (I+II); SA pair R080-R085
R564-R569 | CON-P&L p5 l1017 |  | III Expenses > (i) Finance Costs; SA pair R086-R091
R570-R575 | CON-P&L p5 l1018 | ZERO_STANDING(all periods) | III Expenses > (ii) Fees and commission expense; SA pair R092-R097
R576-R578,R581,R583-R584 | CON-P&L p5 l1019 | ZERO_STANDING(3/6 cols) | (iii) Net loss on fair value changes; SA pair R098-R100,R103,R105-R106
R579-R580,R582,R585-R587 | CON-P&L p5 l1020 | ZERO_STANDING(all periods) | (iv) Net loss on derecognition of financial inst; SA pair R101-R102,R104,R107-R109
R588-R590,R593,R595-R596 | CON-P&L p5 l1021 |  | (v) Impairment on financial instruments; SA pair R110-R112,R115,R117-R118
R591-R592,R594,R597-R599 | CON-P&L p5 l1022 | ZERO_STANDING(all periods) | (vi) Cost of materials consumed; SA pair R113-R114,R116,R119-R121
R600-R605 | CON-P&L p5 l1023 | ZERO_STANDING(all periods) | (vii) Purchases of Stock-in-trade; SA pair R122-R127
R606-R611 | CON-P&L p5 l1024 | ZERO_STANDING(all periods) | (viii) Changes in Inventories of finished goods,; SA pair R128-R133
R612-R614,R617,R619-R620 | CON-P&L p5 l1025 |  | (ix) Employee Benefits Expenses; SA pair R134-R136,R139,R141-R142
R615-R616,R618,R621-R623 | CON-P&L p5 l1026 |  | (x) Depreciation, amortization and impairment; SA pair R137-R138,R140,R143-R145
R624-R627,R630,R632 | CON-P&L p5 l1027 |  | (xi) Others expenses; no standalone pair by label
R628-R629,R631,R633-R635 | CON-P&L p5 l1028 |  | Total Expenses (III); SA pair R150-R151,R153,R155-R157
R636-R641 | CON-P&L p5 l1029 |  | III Expenses > IV Profit/(loss) before exception; SA pair R158-R163
R642-R647 | CON-P&L p5 l1030 | ZERO_STANDING(5/6 cols) | III Expenses > V Exceptional items; SA pair R164-R169
R648-R653 | CON-P&L p5 l1031 |  | III Expenses > VI Profit/(loss) before tax (IV-V; SA pair R170-R175
R654-R659 | CON-P&L p5 l1033 |  | VII Tax Expense > (1) Current Tax; SA pair R176-R181
R660-R665 | CON-P&L p5 l1034 |  | VII Tax Expense > (2) Deferred Tax; SA pair R182-R187
R666-R671 | CON-P&L p5 l1035 |  | VIII Profit/(loss) for the period from continuin; SA pair R188-R193
R672-R677 | CON-P&L p5 l1036 | ZERO_STANDING(all periods) | IX Profit/(loss) from discontinued operations; SA pair R194-R199
R678-R683 | CON-P&L p5 l1037 | ZERO_STANDING(all periods) | X Tax Expense of discontinued operations; SA pair R200-R205
R684-R689 | CON-P&L p5 l1038 | ZERO_STANDING(all periods) | XI Profit/(loss) from discontinued operations (A; SA pair R206-R211
R690-R695 | CON-P&L p5 l1039 |  | XII Profit/(loss) for the period (VIII+XI); SA pair R212-R217
R696-R701 | CON-P&L p5 l1041 | ZERO_STANDING(all periods) | (A) (i) Items that will not be reclassified to p; SA pair R218-R223
R702-R707 | CON-P&L p5 l1042 | ZERO_STANDING(all periods) | XIII Other Comprehensive Income > (ii) Income ta; SA pair R224-R229
R708-R713 | CON-P&L p5 l1043 | ZERO_STANDING(all periods) | Subtotal (A); SA pair R230-R235
R714-R719 | CON-P&L p5 l1044 | ZERO_STANDING(all periods) | (B) (i) Items that will be reclassified to profi; SA pair R236-R241
R720-R725 | CON-P&L p5 l1045 | ZERO_STANDING(all periods) | XIII Other Comprehensive Income > (ii) Income ta; SA pair R224-R229
R726-R731 | CON-P&L p5 l1046 | ZERO_STANDING(all periods) | Subtotal (B); SA pair R248-R253
R732-R737 | CON-P&L p5 l1047 | ZERO_STANDING(all periods) | Other Comprehensive Income (A+B); SA pair R254-R259
R738-R743 | CON-P&L p5 l1048 |  | XIV Total Comprehensive Income for the period; SA pair R260-R265
R744-R749 | CON-P&L p5 l1051 |  | Owners of the holding company; no standalone pair by label
R750-R755 | CON-P&L p5 l1052 | ZERO_STANDING(all periods) | Non-controlling interest; no standalone pair by label
R756-R761 | CON-P&L p5 l1054 | ZERO_STANDING(all periods) | Owners of the holding company; no standalone pair by label
R762-R767 | CON-P&L p5 l1055 | ZERO_STANDING(all periods) | Non-controlling interest; no standalone pair by label
R768-R773 | CON-P&L p5 l1057 |  | Owners of the holding company; no standalone pair by label
R774-R779 | CON-P&L p5 l1058 | ZERO_STANDING(all periods) | Non-controlling interest; no standalone pair by label
R780-R786 | CON-P&L p5 l1059 |  | XVII Paid-up equity share capital (face value of; no standalone pair by label
R787-R792 | CON-P&L p5 l1060 | ZERO_STANDING(5/6 cols) | XIX Other equity as per statement of assets and ; no standalone pair by label
R793-R798 | CON-P&L p5 l1062 |  | XX Earnings per equity share (for continuing ope; no standalone pair by label
R799-R804 | CON-P&L p5 l1063 |  | XX Earnings per equity share (for continuing ope; no standalone pair by label
R805-R810 | CON-P&L p5 l1065 | ZERO_STANDING(all periods) | XXI Earnings per equity share (for discontinued ; no standalone pair by label
R811-R816 | CON-P&L p5 l1066 | ZERO_STANDING(all periods) | XXI Earnings per equity share (for discontinued ; no standalone pair by label
R817-R822 | CON-P&L p5 l1068 |  | XXII Earnings per equity share (for continuing a; no standalone pair by label
R823-R828 | CON-P&L p5 l1069 |  | XXII Earnings per equity share (for continuing a; no standalone pair by label
R829,R831 | CON-BS p6 l1093 |  | (a) Cash & Cash Equivalents; SA pair R315,R317
R830,R833 | CON-BS p6 l1094 |  | (b) Bank Balances other than (a) above; SA pair R316,R319
R832,R834 | CON-BS p6 l1095 | ZERO_STANDING(all periods) | (c) Derivative Financial Instruments; SA pair R318,R320
R835,R837 | CON-BS p6 l1097 |  | (i) Trade Receivables; SA pair R321,R323
R836,R838 | CON-BS p6 l1098 | ZERO_STANDING(all periods) | (ii) Other Receivables; SA pair R322,R324
R839,R841 | CON-BS p6 l1099 |  | (e) Loans; SA pair R325,R327
R840,R843 | CON-BS p6 l1100 |  | (f) Investments; SA pair R326,R329
R842,R844 | CON-BS p6 l1101 |  | (g) Other Financial Assets; SA pair R328,R330
R845,R847 | CON-BS p6 l1103 | ZERO_STANDING(1/2 cols) | (a) Current Tax Assets (Net); SA pair R331,R333
R846,R848 | CON-BS p6 l1104 | ZERO_STANDING(all periods) | (b) Deferred Tax Asset (Net); SA pair R332,R334
R849-R850 | CON-BS p6 l1105 | ZERO_STANDING(all periods) | (c) Investment Property; SA pair R335-R336
R851,R853 | CON-BS p6 l1106 | ZERO_STANDING(all periods) | (d) Biological Assets other than Bearer plants; SA pair R337,R339
R852,R856 | CON-BS p6 l1107 |  | (e) Property, Plant and Equipments; SA pair R338,R342
R854-R855 | CON-BS p6 l1108 | ZERO_STANDING(all periods) | (f) Capital Work-in-Progress; SA pair R340-R341
R857-R858 | CON-BS p6 l1109 | ZERO_STANDING(all periods) | (g) Intangible Assets under development; SA pair R343-R344
R859,R864 | CON-BS p6 l1111 |  | (i) Other Intangible Assets; SA pair R345,R350
R860,R862 | CON-BS p6 l1110 | ZERO_STANDING(all periods) | (h) Goodwill; SA pair R346,R348
R861,R866 | CON-BS p6 l1112 |  | (j) Other Non-Financial Assets; SA pair R347,R352
R863,R867 | CON-BS p6 l1113 |  | Total Assets; SA pair R349,R353
R865,R870 | CON-BS p6 l1116 | ZERO_STANDING(all periods) | (a) Derivative Financial Instruments; SA pair R351,R356
R868,R872 | CON-BS p6 l1119 |  | (I) Trade Payables > (i) Total outstanding dues ; SA pair R354,R358
R869,R874 | CON-BS p6 l1120 |  | (I) Trade Payables > (ii) Total outstanding dues; SA pair R355,R360
R871,R877 | CON-BS p6 l1122 | ZERO_STANDING(all periods) | (II) Other Payables > (i) Total outstanding dues; SA pair R357,R363
R873,R878 | CON-BS p6 l1123 |  | (II) Other Payables > (ii) Total outstanding due; SA pair R359,R364
R875,R880 | CON-BS p6 l1124 |  | (c) Debt Securities; SA pair R361,R366
R876,R882 | CON-BS p6 l1125 |  | (d) Borrowings (Other than Debt Securities); SA pair R362,R368
R879,R884 | CON-BS p6 l1126 | ZERO_STANDING(all periods) | (e) Deposits; SA pair R365,R370
R881,R886 | CON-BS p6 l1127 |  | (f) Subordinated Liabilities; SA pair R367,R372
R883,R888 | CON-BS p6 l1128 |  | (g) Other Financial Liabilities; SA pair R369,R374
R885,R891 | CON-BS p6 l1130 | ZERO_STANDING(1/2 cols) | (a) Current Tax Liabilities (Net); SA pair R371,R377
R887,R892 | CON-BS p6 l1131 |  | (b) Provisions; SA pair R373,R378
R889,R894 | CON-BS p6 l1132 |  | (c) Deferred Tax Liabilities (Net); SA pair R375,R380
R890,R897 | CON-BS p6 l1133 |  | (d) Other non-financial Liabilities; SA pair R376,R383
R893,R899 | CON-BS p6 l1135 |  | (a) Equity Share Capital; SA pair R379,R384
R895,R901 | CON-BS p6 l1136 |  | (b) Other Equity; SA pair R381,R385
R896,R902 | CON-BS p6 l1137 |  | Total Equity & Liabilities; SA pair R382,R386
R898,R904 | CON-BS p6 l1138 |  | Equity attributable to equity holders of the hol; no standalone pair by label
R900,R905-R906 | CON-BS p6 l1139 | ZERO_STANDING(all periods) | Non; no standalone pair by label
R903,R907 | CON-BS p6 l1140 |  | Total Equity; no standalone pair by label
R908-R910 | CON-CF p7 l1162 |  | Net Profit before tax and extraordinary items an; SA pair R387-R389
R911-R912,R915 | CON-CF p7 l1164 |  | Adjustments for > I Depreciation; SA pair R390-R391,R394
R913-R914,R918 | CON-CF p7 l1165 |  | Adjustments for > II Deferred Expense W/O; SA pair R392-R393,R397
R916-R917,R921 | CON-CF p7 l1166 |  | Adjustments for > III Impairment on financial in; SA pair R395-R396,R400
R919-R920,R922 | CON-CF p7 l1167 |  | Adjustments for > IV Expenditure on CSR; SA pair R398-R399,R401
R923-R924,R927 | CON-CF p7 l1168 | ZERO_STANDING(1/3 cols) | Adjustments for > V Dividend Income; SA pair R402-R403,R406
R925-R926,R928 | CON-CF p7 l1169 |  | Adjustments for > VI Profit/Loss on Sale of Shar; SA pair R404-R405,R407
R929-R931 | CON-CF p7 l1170 |  | Adjustments for > VII Profit/Loss on Sale of Inv; SA pair R408-R409,R412
R932-R934 | CON-CF p7 l1171 |  | Operating Profit before working capital changes; SA pair R410-R411,R413
R935-R937 | CON-CF p7 l1173 |  | Adjustments for > I Change in Other Financial As; SA pair R414-R415,R418
R938-R940 | CON-CF p7 l1174 |  | Adjustments for > II Change in Loans & Receivabl; SA pair R416-R417,R419
R941-R943 | CON-CF p7 l1175 |  | Adjustments for > III Change in Payable & non fi; SA pair R420-R421,R424
R944-R946 | CON-CF p7 l1176 |  | Adjustments for > IV Change in other Non Financi; SA pair R422-R423,R426
R947-R949 | CON-CF p7 l1177 |  | Cash generated from Operations; SA pair R425,R427-R428
R950-R951,R953 | CON-CF p7 l1178 |  | Adjustments for > I Interest paid; SA pair R429,R431-R432
R952,R954,R956 | CON-CF p7 l1179 |  | Adjustments for > II Income Tax paid; SA pair R430,R434-R435
R955,R957-R958 | CON-CF p7 l1180 |  | Adjustments for > III Paid Expenses on CSR; SA pair R433,R436-R437
R959-R961 | CON-CF p7 l1181 |  | Cash flow before Extraordinary Items; SA pair R438-R440
R962-R963,R965 | CON-CF p7 l1182 | ZERO_STANDING(2/3 cols) | Adjustments for > I Extraordinary items; SA pair R441,R443-R444
R964,R966-R967 | CON-CF p7 l1183 |  | Net Cash from Operating Activities; SA pair R442,R445-R446
R968-R969,R971 | CON-CF p7 l1185 |  | B Cash Flows from Investing Activities > I Purch; SA pair R447,R449-R450
R970,R972-R973 | CON-CF p7 l1186 |  | B Cash Flows from Investing Activities > II Sale; SA pair R448,R451-R452
R974-R975,R977 | CON-CF p7 l1187 | ZERO_STANDING(1/3 cols) | B Cash Flows from Investing Activities > III Pur; SA pair R453-R454,R456
R976,R978-R979 | CON-CF p7 l1188 |  | Net Cash from Investing activities; SA pair R455,R457-R458
R980-R981,R983 | CON-CF p7 l1190 |  | C Net Cash from Financing Activities > I Proceed; SA pair R459,R461-R462
R982,R984-R985 | CON-CF p7 l1191 |  | C Net Cash from Financing Activities > II Procee; SA pair R460,R463-R464
R986-R988 | CON-CF p7 l1192 |  | C Net Cash from Financing Activities > III Proce; SA pair R465-R466,R469
R989-R991 | CON-CF p7 l1193 | ZERO_STANDING(2/3 cols) | C Net Cash from Financing Activities > IV Procee; SA pair R467-R468,R471
R992-R994 | CON-CF p7 l1194 | ZERO_STANDING(1/3 cols) | C Net Cash from Financing Activities > V Dividen; SA pair R470,R472,R474
R995-R997 | CON-CF p7 l1195 | ZERO_STANDING(1/3 cols) | C Net Cash from Financing Activities > VI Purcha; SA pair R473,R475-R476
R998-R1000 | CON-CF p7 l1196 |  | C Net Cash from Financing Activities > VII Money; SA pair R477-R479
R1001-R1003 | CON-CF p7 l1197 |  | Net Cash from Financing activities; SA pair R480-R482
R1004-R1006 | CON-CF p7 l1198 |  | Net Increase/(decrease) in cash & cash equivalen; SA pair R483-R484,R486
R1007-R1009 | CON-CF p7 l1199 |  | Cash & Cash equivalents at beginning of period; SA pair R485,R487-R488
R1010-R1012 | CON-CF p7 l1200 |  | Cash & Cash equivalent at end of period; SA pair R489-R491

### 2B. Regulation 52(4)/(6) ratio table (page 8), 22 sub-rows a to s-iii
ROW_ID(s) | ratio row | A2 flags | cross-ref
R1077-R1078 | ratio a |  | Debt-Equity
M-b (new, fulltext line 1215) | ratio b | MISSING_FROM_STRUCTURED | Debt service coverage ratio: Not applicable (Standalone and Consolidated)
M-c (new, fulltext line 1216) | ratio c | MISSING_FROM_STRUCTURED | Interest service coverage ratio: Not applicable (Standalone and Consolidated)
M-d (new, fulltext line 1217) | ratio d | MISSING_FROM_STRUCTURED; ZERO_STANDING | Outstanding redeemable preference shares: Nil (Standalone and Consolidated)
R1080-R1081 | ratio e |  | Capital Redemption Reserve
R1079 | ratio f | citation only; value row is M-f | Debenture Redemption Reserve
R1082-R1083 | ratio g |  | Net Worth
R1084-R1085 | ratio h | RESTATED | Net Profit after tax; same value on statement pages R191,R215,R263,R669,R693,R741,R747,R771
R1086-R1087 | ratio i | RESTATED | EPS; same value on statement pages R282,R288,R306,R312,R796,R802,R820,R824
R1088-R1089 | ratio j |  | Current ratio
R1090-R1091 | ratio k |  | LT debt to WC
R1092-R1093 | ratio l | ZERO_STANDING(0.00 value, A2-raised; A1 did not flag) | Bad debts to receivable
R1094-R1095 | ratio m |  | Current liability ratio
R1096-R1097 | ratio n |  | Total debts to total assets
M-o (new, fulltext line 1230) | ratio o | MISSING_FROM_STRUCTURED | Debtors turnover: Not applicable (Standalone and Consolidated)
M-p (new, fulltext line 1231) | ratio p | MISSING_FROM_STRUCTURED | Inventory turnover: Not applicable (Standalone and Consolidated)
M-q (new, fulltext line 1232) | ratio q | MISSING_FROM_STRUCTURED | Operating margin (%): Not applicable (Standalone and Consolidated)
R1098-R1099 | ratio r |  | Net profit margin
M-s (new, fulltext line 1234) | ratio s | MISSING_FROM_STRUCTURED | Sector specific equivalent ratios header: no value (parent of s-i to s-iii)
R1100-R1101 | ratio s-i |  | NIM
R1102-R1103 | ratio s-ii |  | GNPA
R1104-R1105 | ratio s-iii |  | NNPA
M-f (new, fulltext line 1219) | ratio f value | MISSING_FROM_STRUCTURED | Debenture Redemption Reserve value: Not applicable (Standalone and Consolidated); R1079 holds only the 2019 citation

### 2C. Note 5 issuance table (Rs Cr), 10 line items
ROW_ID(s) | series | A2 flags | cross-ref
R1023-R1026 | NCD 9.00% secured | | note 5; allotment date row R1290
R1027-R1030 | NCD 9.15% secured | | note 5; allotment date row R1291
R1031-R1034 | NCD 9.50% secured | | note 5; allotment date row R1292
R1035-R1038 | NCD 9.92% secured | | note 5; allotment date row R1293
R1039-R1042 | NCD 10.00% secured | | note 5; allotment date row R1294
R1043-R1046 | NCD 10.47% secured | | note 5; allotment date row R1295
R1047-R1050 | NCD 12.00% unsecured | | note 5; allotment date row R1296
R1051-R1055 | CP series 1 (Jul-26) | | note 5; allotment date row R1297
R1056-R1060 | CP series 2 (Sep-26, 151d) | | note 5; allotment date row R1298
R1061-R1065 | CP series 3 (Sep-26, 180d) | | note 5; allotment date row R1299

## 3. AGENDA ITEMS (Board outcome letter, page 1)
ROW_ID(s) | item | A2 flags | note
R011,R1234,R1236,R1311 | A1: approve Unaudited Financial Results (Standalone and Consolidated), quarter and half year ended 30-Sep-2026 | | only operative agenda item disclosed; letter says "inter alia"
R1235 | prior intimation letter dated 12-Oct-2026 | | board meeting notice reference
R1237-R1238 | A2: Auditor Limited Review Reports (Standalone and Consolidated), Annexure I item 2 | | meeting 09:30 to 10:25 = 55 minutes
R001-R010 | regulation citations (Regs 30, 33, 52, 63; LODR 2015) | CITATION | not metrics
R012-R013,R1182-R1183 | CC listing venues (Afrinex, IIEL IFSC), cc list numbered 1 and 2 | | 
(none) | AR approval, AGM notice, record date, dividend, director appointment, auditor change, scrutinizer, ESOP, capital-raising enabling resolution | | none disclosed; letter wording "inter alia" leaves other items undisclosed; absence recorded as fact

## 4. ANNEXURES AND TABLES
ROW_ID(s) | table | A2 flags | note
R011,R1311 | Annexure I index (item 1 results, item 2 review reports) | | contains 6 statements, notes, 2 review reports
R014-R314,R1184-R1185,R1242-R1251,R1313-R1323 | Standalone results (P&L) p2 | | 50 line items; header dates, units, status rows included
R315-R386,R1252-R1257,R1324-R1325 | Standalone assets and liabilities p3 | | 36 line items; header dates, units, status rows included
R387-R491,R1258-R1264,R1326-R1328 | Standalone cash flow p4 | | 35 line items; header dates, units, status rows included
R492-R828,R1265-R1274,R1329-R1333 | Consolidated results (P&L) p5 | | 56 line items; header dates, units, status rows included
R829-R907,R1275-R1280,R1334-R1335 | Consolidated assets and liabilities p6 | | 39 line items; header dates, units, status rows included
R908-R1012,R1281-R1287,R1336-R1338 | Consolidated cash flow p7 | | 35 line items; header dates, units, status rows included
R1013-R1105,R1186-R1204,R1288-R1306,R1339-R1364 | Page 8: notes, note 5 table, ratio table, signature | | see sections 1, 2B, 2C
(none) | Director profiles | | no director profile annexure in this filing; zero rows

## 5. AUDITOR REPORT PARAGRAPHS
ROW_ID(s) | paragraph | A2 flags | note
R1205-R1214 | SA letterhead (Saket Jain & Co, Agra/Gurugram) |  | 
R1106-R1108 | SA title and addressee |  | 
R1109-R1111,R1307 | SA para1 scope (statement reviewed) |  | 
R1112-R1115 | SA para2 management responsibility, Ind AS 34 |  | 
R1116,R1215,R1365-R1366 | SA para3 SRE 2410 moderate assurance, no audit opinion |  | 
R1117-R1121,R1367 | SA para4 conclusion: nothing came to attention (unmodified) | UNMODIFIED_REVIEW | 
R1216-R1219,R1308,R1368 | SA signature block (place, date 22.10.2026, membership, UDIN) | FOOTNOTE_UNRESOLVED(UDIN garbled) | 
R1220-R1227 | CON letterhead |  | 
R1122-R1124 | CON title and addressee |  | 
R1125-R1127,R1309 | CON para1 scope (Group = parent + WOS Nupur Finvest) |  | 
R1128-R1131 | CON para2 management responsibility, Ind AS 34 |  | 
R1132,R1369 | CON para3 SRE 2410 moderate assurance |  | 
R1133-R1134,R1228,R1370 | CON para4 Reg 33(8) circular procedures |  | 
R1371 | CON para5 statement includes WOS results | SUBSIDIARY_BASIS_NOT_STATED | report does not say whether Nupur results were reviewed by another auditor or management-furnished
R1135-R1139,R1372 | CON para6 conclusion: nothing came to attention (unmodified) | UNMODIFIED_REVIEW | 
R1140,R1229-R1232,R1310 | CON signature block (place, date 22.10.2026, membership, UDIN) | FOOTNOTE_UNRESOLVED(UDIN garbled) | 
(none) | Emphasis of Matter | | none in either report
(none) | Other Matters | | none in either report
(none) | Going Concern language | | none in either report; both are limited reviews (SRE 2410), no audit opinion
Entities reviewed: Standalone = Paisalo only; Consolidated = Paisalo + Nupur Finvest Pvt Ltd (WOS). Unaudited or management-furnished entity list: not stated in either report.

## 6. ENTITIES (92 A1 ENTITY rows; identifier rows grouped by line)
ROW_ID(s) | kind | A2 flags | note
R1141 | named entity or reference | | parent (consolidation list)
R1142 | named entity or reference | | 
R1143 | named entity or reference | | 
R1144 | identifier/code l24 (scrip, phone, address, UDIN class) | | not an entity
R1145-R1148 | identifier/code l25 (scrip, phone, address, UDIN class) | | not an entity
R1149 | identifier/code l27 (scrip, phone, address, UDIN class) | | not an entity
R1150-R1157 | identifier/code l29 (scrip, phone, address, UDIN class) | | not an entity
R1158 | named entity or reference | | 
R1159-R1167 | identifier/code l30 (scrip, phone, address, UDIN class) | | not an entity
R1168-R1175 | identifier/code l31 (scrip, phone, address, UDIN class) | | not an entity
R1176-R1179 | identifier/code l32 (scrip, phone, address, UDIN class) | | not an entity
R1180 | named entity or reference | | 
R1181 | named entity or reference | | 
R1182 | named entity or reference | | 
R1183 | named entity or reference | | 
R1184 | named entity or reference | | 
R1185 | named entity or reference | | 
R1186 | named entity or reference | | 
R1187 | named entity or reference | | wholly owned subsidiary (consolidation list)
R1188 | named entity or reference | | 
R1189 | named entity or reference | | 
R1190 | named entity or reference | | 
R1191 | named entity or reference | | 
R1192 | named entity or reference | | 
R1193 | named entity or reference | | 
R1194 | named entity or reference | | 
R1195 | named entity or reference | | 
R1196 | named entity or reference | | 
R1197 | named entity or reference | | 
R1198 | named entity or reference | | 
R1199 | named entity or reference | | 
R1200 | named entity or reference | | 
R1201 | named entity or reference | | 
R1202 | named entity or reference | | 
R1203 | named entity or reference | | 
R1204 | named entity or reference | | 
R1205 | named entity or reference | | 
R1206 | named entity or reference | | 
R1207-R1208 | identifier/code l662 (scrip, phone, address, UDIN class) | | not an entity
R1209-R1214 | identifier/code l663 (scrip, phone, address, UDIN class) | | not an entity
R1215 | named entity or reference | | 
R1216 | named entity or reference | | 
R1217 | identifier/code l715 (scrip, phone, address, UDIN class) | | not an entity
R1218-R1219 | identifier/code l717 (scrip, phone, address, UDIN class) | | not an entity
R1220-R1221 | identifier/code l724 (scrip, phone, address, UDIN class) | | not an entity
R1222-R1227 | identifier/code l726 (scrip, phone, address, UDIN class) | | not an entity
R1228 | named entity or reference | | 
R1229 | identifier/code l782 (scrip, phone, address, UDIN class) | | not an entity
R1230-R1232 | identifier/code l784 (scrip, phone, address, UDIN class) | | not an entity
CONSOLIDATION LIST: (1) Paisalo Digital Limited, parent; (2) Nupur Finvest Private Limited, wholly owned subsidiary, RBI registered NBFC (R1187, R1340, R1371). No prior ledger: ENTITY_CHANGE not assessable, no flag raised.

## 7. SIGNATURE BLOCKS AND DATE/TIME ROWS
ROW_ID(s) | block | A2 flags | note
R1181,R1239-R1241,R1312 | CS Manendra Singh, intimation letter p1, 22-Oct-2026 10:30:07 +05:30 |  | after board conclusion 10:25
R1185,R1249-R1251,R1323 | MD Sunil Purushottam Agarwal, standalone results p2, 10:09:01 | SIGNATURE_BEFORE_MEETING_END | 10:09 is before 10:25 conclusion
R1255-R1257 | MD, standalone balance sheet p3, 10:09:15 | SIGNATURE_BEFORE_MEETING_END | 
R1262-R1264 | MD, standalone cash flow p4, 10:09:25 | SIGNATURE_BEFORE_MEETING_END | 
R1272-R1274 | MD, consolidated results p5, 10:09:33 | SIGNATURE_BEFORE_MEETING_END | 
R1278-R1280 | MD, consolidated balance sheet p6, 10:09:42 | SIGNATURE_BEFORE_MEETING_END | 
R1285-R1287 | MD, consolidated cash flow p7, 10:09:51 | SIGNATURE_BEFORE_MEETING_END | 
R1204,R1303-R1306 | MD, notes page 8, 22.10.2026 10:10:02 | SIGNATURE_BEFORE_MEETING_END; SPELLING_VARIANT | name rendered Purushottanm in signature text vs Purushottam (R1185 vs R1204)
R1206,R1216,R1308 | Auditor Saket Jain & Co, standalone report, 22.10.2026 |  | date only, no time stamp
R1310 | Auditor Saket Jain & Co, consolidated report, 22.10.2026 |  | date only, no time stamp
R1233-R1238 | Letter dates and meeting times (22-Oct-2026; start 09:30, end 10:25; prior intimation 12-Oct-2026; period end 30-Sep-2026) | | meeting 55 min
R1242-R1248,R1252-R1254,R1258-R1261,R1265-R1271,R1275-R1277,R1281-R1284 | period header dates, column headers and remaining signature stamp rows (statements p2-p7) | | column order per A1 read-me
R1288-R1289,R1300-R1302,R1307,R1309 | note-body and report-body dates (30-Sep-2026, 22-Oct-2026, 16-Aug-2019 DRR rule date) | | 
R1290-R1299 | note 5 allotment dates (19-Aug-2026 x6, 18-Sep-2026, 14-Jul-2026, 24-Sep-2026 x2) | | cross-ref 2C

## 8. QUALIFIERS AND FINE PRINT (62 A1 QUALIFIER rows)
ROW_ID(s) | type | A2 flags | note
R1311 | AUDIT-STATUS p1 l43 |  | 
R1312 | SIGNATURE p1 l64 |  | 
R1313 | AUDIT-STATUS p2 l79 |  | 
R1314 | UNIT p2 l81 |  | 
R1315 | AUDIT-STATUS p2 l85 |  | 
R1316 | AUDIT-STATUS p2 l87 |  | 
R1317 | DEFINITION p2 l95 |  | 
R1318 | DEFINITION p2 l122 |  | 
R1319 | DEFINITION p2 l139 |  | 
R1320 | DEFINITION p2 l155 |  | 
R1321 | FINE-PRINT p2 l157 |  | 
R1322 | DEFINITION p2 l168 |  | 
R1323 | SIGNATURE p2 l172 |  | 
R1324 | UNIT p3 l183 |  | 
R1325 | AUDIT-STATUS p3 l185 |  | 
R1326 | UNIT p4 l250 |  | 
R1327 | AUDIT-STATUS p4 l252 |  | 
R1328 | DEFINITION p4 l254 |  | 
R1329 | AUDIT-STATUS p5 l316 |  | 
R1330 | UNIT p5 l318 |  | 
R1331 | AUDIT-STATUS p5 l325 |  | 
R1332 | FINE-PRINT p5 l407 |  | 
R1333 | SIGNATURE p5 l422 | FOOTNOTE_UNRESOLVED | 
R1334 | UNIT p6 l432 |  | 
R1335 | AUDIT-STATUS p6 l434 |  | 
R1336 | UNIT p7 l499 |  | 
R1337 | AUDIT-STATUS p7 l501 |  | 
R1338 | DEFINITION p7 l503 |  | 
R1339 | NOTE-HEAD p8 l564 |  | 
R1340 | NOTE-HEAD p8 l567 |  | 
R1341 | NOTE-HEAD p8 l568 |  | 
R1342 | NOTE-HEAD p8 l572 |  | 
R1343 | NOTE-HEAD p8 l573 |  | 
R1344 | UNIT p8 l577 |  | 
R1345 | FINE-PRINT p8 l587 |  | 
R1346 | FINE-PRINT p8 l588 |  | 
R1347 | FINE-PRINT p8 l591 |  | 
R1348 | FINE-PRINT p8 l592 |  | 
R1349 | FINE-PRINT p8 l595 |  | 
R1350 | FINE-PRINT p8 l596 |  | 
R1351 | NOTE-HEAD p8 l598 |  | 
R1352 | NOTE-HEAD p8 l601 |  | 
R1353 | NOTE-HEAD p8 l603 |  | 
R1354 | FINE-PRINT p8 l604 |  | 
R1355 | NOTE-HEAD p8 l607 |  | 
R1356 | AUDIT-STATUS p8 l610 |  | 
R1357 | UNIT p8 l616 |  | 
R1358 | FINE-PRINT p8 l619 |  | 
R1359 | UNIT p8 l626 |  | 
R1360 | DEFINITION p8 l627 |  | 
R1361 | UNIT p8 l629 |  | 
R1362 | FINE-PRINT p8 l637 |  | 
R1363 | DEFINITION p8 l640 |  | 
R1364 | DEFINITION p8 l641 |  | 
R1365 | REVIEW-SCOPE p9 l694 |  | 
R1366 | REVIEW-SCOPE p9 l696 |  | 
R1367 | REVIEW-SCOPE p9 l699 |  | 
R1368 | FINE-PRINT p9 l717 | FOOTNOTE_UNRESOLVED | 
R1369 | REVIEW-SCOPE p10 l756 |  | 
R1370 | FINE-PRINT p10 l760 |  | 
R1371 | FINE-PRINT p10 l765 |  | 
R1372 | REVIEW-SCOPE p10 l767 |  | 

## 9. FORWARD-LOOKING TABLE
(none) | A1 FORWARD table has 0 rows | | A2 sweep concurs: no guidance, outlook, target or plan language in the structured file

```yaml
stage: A2-enumerator
company: "PAISALO"
quarter: "Q2 FY27"
doctype: "results"
model: claude-sonnet-5-5
status: complete
ledger_path: "C:\Users\SUMIT SHARMA\repos\inflection-pipeline\.claude\worktrees\quarterly-paisalo-q2fy27-095262\runs\paisalo-q2fy27\work\ledger_results_paisalo_q2fy27.md"
counts:
  notes: 9
  line_items: 283
  zero_standing: 102
  agenda_items: 2
  auditor_paras: 10
  entities: 92
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, MISSING_FROM_STRUCTURED, FOOTNOTE_UNRESOLVED, SIGNATURE_BEFORE_MEETING_END, SUBSIDIARY_BASIS_NOT_STATED, RESTATED, RESTATED_COMPARATIVES, SPELLING_VARIANT, CITATION]
ids_in_structured: 1372
ids_referenced: 1372
orphan_ids: []
missing_from_structured: ["ratio b DSCR Not applicable (fulltext l.1215)", "ratio c ISCR Not applicable (l.1216)", "ratio d redeemable pref shares Nil, ZERO_STANDING (l.1217)", "ratio f DRR value Not applicable (l.1219)", "ratio o debtors turnover Not applicable (l.1230)", "ratio p inventory turnover Not applicable (l.1231)", "ratio q operating margin Not applicable (l.1232)", "ratio s sector-specific header (l.1234)"]
gate_a2: pass
mismatch_note: ""
analyst_note: "Count tests match on every category. A1 gave no rows for ratio-table cells holding Nil or Not applicable; A2 added 8 rows from fulltext lines 1215-1234 (ratio d, redeemable preference shares, is a Nil standing line). zero_standing 102 = 100 line items A1 flagged (402 dash rows) plus ratio l (0.00 bad debts, A2-raised) and ratio d. Seven MD-signed statement stamps (10:09:01 to 10:10:02) precede the 10:25 board conclusion; the CS letter is stamped 10:30:07, after it. Both review reports are limited reviews with unmodified conclusions, no EoM, no Other Matters, no going concern text; the consolidated report does not say how Nupur Finvest results were reviewed. Both UDINs are garbled in the text layer. One stray asterisk on page 5 (R1333) has no footnote text. No prior ledger exists, so ENTITY_CHANGE could not be assessed. No director profiles, no forward statements, no dividend or AGM items in this filing."
```
