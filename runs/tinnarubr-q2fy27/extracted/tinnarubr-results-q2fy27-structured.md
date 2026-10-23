=== A1 STRUCTURED EXTRACTION ===
source: Tinna_Q2FY27_Results_Reg33_2026-10-22.pdf
fulltext: runs/tinnarubr-q2fy27/extracted/tinnarubr-results-q2fy27-fulltext.md (line numbers refer to this file, header included)
row_id_range: R001-R927
counts: NUMBER 745, ENTITY 57, FORWARD 10, DATE 45, QUALIFIER 70
unit: Rs lakhs for statements (x0.01 to Rs Cr); narrative amounts as stated; no value converted
extraction_mode: text-only+ocr-repair (re-run 2026-10-23; supersedes the first A1 pass, whose statement rows were unusable)
STATEMENT METHOD: every statement line item (standalone and consolidated P&L, balance sheet, cash flow) is one NUMBER row per cell with its column (P&L: Q2FY27, Q1FY27, Q2FY26, H1FY27, H1FY26, FY26; balance sheet: 30-Sep-2026, 31-Mar-2026; cash flow: H1FY27, H1FY26). Dash cells are ZERO_STANDING. Value of record = read from the page image (130-170dpi) and checked against the [OCR page N] block; the line cited is the [OCR page N] block line carrying the row. OCR_CONFLICT = the value does not appear on that OCR line (OCR digit error or dropped row). The embedded text layer was not used for any statement cell. There is no segment table (single reportable segment, Note 3).
STATEMENT CHECKS: cells 692, OCR_CONFLICT 227, ARITH_FAIL 0, UNREADABLE 0, ZERO_STANDING 81, OCR_ROW_MISSING_ROWS 7
LINE-CITE CAVEAT: tesseract dropped or garbled many total and sub-total rows and some digits. For such rows the cited line is the nearest OCR line (section header or preceding row) and the cell carries OCR_CONFLICT, plus OCR_ROW_MISSING where neither label nor digits matched. The value of record is the page-image read, and it foots arithmetically (see below). Correction made during build: consolidated P&L Other expenses Q2FY27 was first read 3,533.23 (same as the OCR layer) and Total expenses failed to foot; a 300dpi crop shows 3,531.23, which foots to the filed 13,405.73.
Arithmetic tested per column: Total income = Revenue + Other income; Total expenses = sum of items; PBT = Total income - Total expenses; Total tax = sum; PAT = PBT - Total tax; TCI = PAT + OCI; balance sheet sub-totals, totals and Total assets = Total equity and liabilities; cash flow A, B, C, net change and closing cash.
Repeated page letterhead on pages 3, 4, 8, 9, 10 (company name, address, CIN) is captured once on page 2 and CIN again per page; not repeated as ENTITY rows.
Page 3 of 3 of the consolidated review report is not in the file (page 13 footer reads Page 2 of 3).
row format: R### | page N | line L | TYPE | value | context | [flags]

## NUMBER
R001 | page 1 | line 29 | NUMBER | 530475 | BSE scrip code
R002 | page 1 | line 31 | NUMBER | INE015C01016 | ISIN
R003 | page 1 | line 38 | NUMBER | Regulations 30 and 33 | LODR regulations cited
R004 | page 1 | line 70 | NUMBER | ACS23729 | company secretary membership no.
R005 | page 1 | line 75 | NUMBER | L51909DL1987PLC027186 | CIN (letterhead) | OCR_ONLY
R006 | page 1 | line 77 | NUMBER | 110030 | registered office PIN (letterhead) | OCR_ONLY
R007 | page 1 | line 78 | NUMBER | (011) 35657373 (90 Lines) | telephone (letterhead) | OCR_ONLY
R008 | page 1 | line 80 | NUMBER | (011) 2680 7073 | fax (letterhead) | OCR_ONLY
R009 | page 2 | line 233 | NUMBER | 011-49518530 | telephone
R010 | page 2 | line 233 | NUMBER | 011-26807073 | fax
R011 | page 2 | line 234 | NUMBER | L51909DL1987PLC027186 | CIN
R012 | page 2 | line 243 | NUMBER | 14,956.64 | standalone P&L, Revenue from operations, Q2FY27
R013 | page 2 | line 243 | NUMBER | 15,085.10 | standalone P&L, Revenue from operations, Q1FY27
R014 | page 2 | line 243 | NUMBER | 11,685.68 | standalone P&L, Revenue from operations, Q2FY26
R015 | page 2 | line 243 | NUMBER | 30,041.74 | standalone P&L, Revenue from operations, H1FY27
R016 | page 2 | line 243 | NUMBER | 24,416.12 | standalone P&L, Revenue from operations, H1FY26
R017 | page 2 | line 243 | NUMBER | 53,323.41 | standalone P&L, Revenue from operations, FY26
R018 | page 2 | line 244 | NUMBER | 72.54 | standalone P&L, Other income, Q2FY27
R019 | page 2 | line 244 | NUMBER | 62.62 | standalone P&L, Other income, Q1FY27
R020 | page 2 | line 244 | NUMBER | 23.55 | standalone P&L, Other income, Q2FY26
R021 | page 2 | line 244 | NUMBER | 135.16 | standalone P&L, Other income, H1FY27
R022 | page 2 | line 244 | NUMBER | 59.50 | standalone P&L, Other income, H1FY26 | OCR_CONFLICT
R023 | page 2 | line 244 | NUMBER | 185.62 | standalone P&L, Other income, FY26 | OCR_CONFLICT
R024 | page 2 | line 245 | NUMBER | 15,029.18 | standalone P&L, Total income, Q2FY27
R025 | page 2 | line 245 | NUMBER | 15,147.72 | standalone P&L, Total income, Q1FY27
R026 | page 2 | line 245 | NUMBER | 11,709.23 | standalone P&L, Total income, Q2FY26
R027 | page 2 | line 245 | NUMBER | 30,176.90 | standalone P&L, Total income, H1FY27
R028 | page 2 | line 245 | NUMBER | 24,475.62 | standalone P&L, Total income, H1FY26
R029 | page 2 | line 245 | NUMBER | 53,509.03 | standalone P&L, Total income, FY26
R030 | page 2 | line 248 | NUMBER | 6,432.21 | standalone P&L, (a) Cost of material consumed, Q2FY27
R031 | page 2 | line 248 | NUMBER | 6,621.77 | standalone P&L, (a) Cost of material consumed, Q1FY27
R032 | page 2 | line 248 | NUMBER | 4,484.48 | standalone P&L, (a) Cost of material consumed, Q2FY26
R033 | page 2 | line 248 | NUMBER | 13,053.98 | standalone P&L, (a) Cost of material consumed, H1FY27
R034 | page 2 | line 248 | NUMBER | 9,387.14 | standalone P&L, (a) Cost of material consumed, H1FY26
R035 | page 2 | line 248 | NUMBER | 21,537.70 | standalone P&L, (a) Cost of material consumed, FY26
R036 | page 2 | line 249 | NUMBER | 1,292.46 | standalone P&L, (b) Purchase of stock in trade, Q2FY27
R037 | page 2 | line 249 | NUMBER | 937.15 | standalone P&L, (b) Purchase of stock in trade, Q1FY27
R038 | page 2 | line 249 | NUMBER | 1,632.04 | standalone P&L, (b) Purchase of stock in trade, Q2FY26
R039 | page 2 | line 249 | NUMBER | 2,229.61 | standalone P&L, (b) Purchase of stock in trade, H1FY27
R040 | page 2 | line 249 | NUMBER | 3,638.52 | standalone P&L, (b) Purchase of stock in trade, H1FY26
R041 | page 2 | line 249 | NUMBER | 5,924.17 | standalone P&L, (b) Purchase of stock in trade, FY26
R042 | page 2 | line 250 | NUMBER | (629.05) | standalone P&L, (c) Changes in inventories of finished goods, work in progress and stock in trade, Q2FY27 | OCR_CONFLICT
R043 | page 2 | line 250 | NUMBER | (351.36) | standalone P&L, (c) Changes in inventories of finished goods, work in progress and stock in trade, Q1FY27
R044 | page 2 | line 250 | NUMBER | (509.04) | standalone P&L, (c) Changes in inventories of finished goods, work in progress and stock in trade, Q2FY26
R045 | page 2 | line 250 | NUMBER | (980.41) | standalone P&L, (c) Changes in inventories of finished goods, work in progress and stock in trade, H1FY27
R046 | page 2 | line 250 | NUMBER | (388.91) | standalone P&L, (c) Changes in inventories of finished goods, work in progress and stock in trade, H1FY26
R047 | page 2 | line 250 | NUMBER | 522.86 | standalone P&L, (c) Changes in inventories of finished goods, work in progress and stock in trade, FY26 | OCR_CONFLICT
R048 | page 2 | line 251 | NUMBER | 1,767.43 | standalone P&L, (d) Employee benefits expense, Q2FY27
R049 | page 2 | line 251 | NUMBER | 1,513.04 | standalone P&L, (d) Employee benefits expense, Q1FY27
R050 | page 2 | line 251 | NUMBER | 1,491.14 | standalone P&L, (d) Employee benefits expense, Q2FY26
R051 | page 2 | line 251 | NUMBER | 3,280.47 | standalone P&L, (d) Employee benefits expense, H1FY27
R052 | page 2 | line 251 | NUMBER | 2,873.15 | standalone P&L, (d) Employee benefits expense, H1FY26
R053 | page 2 | line 251 | NUMBER | 5,757.27 | standalone P&L, (d) Employee benefits expense, FY26
R054 | page 2 | line 252 | NUMBER | 262.20 | standalone P&L, (e) Finance costs, Q2FY27 | OCR_CONFLICT
R055 | page 2 | line 252 | NUMBER | 287.38 | standalone P&L, (e) Finance costs, Q1FY27
R056 | page 2 | line 252 | NUMBER | 235.54 | standalone P&L, (e) Finance costs, Q2FY26 | OCR_CONFLICT
R057 | page 2 | line 252 | NUMBER | 549.58 | standalone P&L, (e) Finance costs, H1FY27
R058 | page 2 | line 252 | NUMBER | 536.82 | standalone P&L, (e) Finance costs, H1FY26 | OCR_CONFLICT
R059 | page 2 | line 252 | NUMBER | 1,076.22 | standalone P&L, (e) Finance costs, FY26
R060 | page 2 | line 253 | NUMBER | 386.46 | standalone P&L, (f) Depreciation and amortization expenses, Q2FY27
R061 | page 2 | line 253 | NUMBER | 387.84 | standalone P&L, (f) Depreciation and amortization expenses, Q1FY27
R062 | page 2 | line 253 | NUMBER | 256.23 | standalone P&L, (f) Depreciation and amortization expenses, Q2FY26 | OCR_CONFLICT
R063 | page 2 | line 253 | NUMBER | 774.30 | standalone P&L, (f) Depreciation and amortization expenses, H1FY27 | OCR_CONFLICT
R064 | page 2 | line 253 | NUMBER | 497.85 | standalone P&L, (f) Depreciation and amortization expenses, H1FY26
R065 | page 2 | line 253 | NUMBER | 1,057.60 | standalone P&L, (f) Depreciation and amortization expenses, FY26 | OCR_CONFLICT
R066 | page 2 | line 255 | NUMBER | 3,287.68 | standalone P&L, (g) Other expenses, Q2FY27
R067 | page 2 | line 255 | NUMBER | 3,050.14 | standalone P&L, (g) Other expenses, Q1FY27
R068 | page 2 | line 255 | NUMBER | 2,425.20 | standalone P&L, (g) Other expenses, Q2FY26 | OCR_CONFLICT
R069 | page 2 | line 255 | NUMBER | 6,337.82 | standalone P&L, (g) Other expenses, H1FY27
R070 | page 2 | line 255 | NUMBER | 4,759.59 | standalone P&L, (g) Other expenses, H1FY26
R071 | page 2 | line 255 | NUMBER | 10,404.85 | standalone P&L, (g) Other expenses, FY26
R072 | page 2 | line 256 | NUMBER | 12,799.39 | standalone P&L, Total expenses, Q2FY27
R073 | page 2 | line 256 | NUMBER | 12,445.96 | standalone P&L, Total expenses, Q1FY27
R074 | page 2 | line 256 | NUMBER | 10,015.59 | standalone P&L, Total expenses, Q2FY26
R075 | page 2 | line 256 | NUMBER | 25,245.35 | standalone P&L, Total expenses, H1FY27
R076 | page 2 | line 256 | NUMBER | 21,304.16 | standalone P&L, Total expenses, H1FY26 | OCR_CONFLICT
R077 | page 2 | line 256 | NUMBER | 46,280.67 | standalone P&L, Total expenses, FY26
R078 | page 2 | line 257 | NUMBER | 2,229.79 | standalone P&L, Profit before tax (1-2), Q2FY27
R079 | page 2 | line 257 | NUMBER | 2,701.76 | standalone P&L, Profit before tax (1-2), Q1FY27
R080 | page 2 | line 257 | NUMBER | 1,693.64 | standalone P&L, Profit before tax (1-2), Q2FY26
R081 | page 2 | line 257 | NUMBER | 4,931.55 | standalone P&L, Profit before tax (1-2), H1FY27
R082 | page 2 | line 257 | NUMBER | 3,171.46 | standalone P&L, Profit before tax (1-2), H1FY26
R083 | page 2 | line 257 | NUMBER | 7,228.36 | standalone P&L, Profit before tax (1-2), FY26
R084 | page 2 | line 259 | NUMBER | 456.39 | standalone P&L, (a) Current tax, Q2FY27
R085 | page 2 | line 259 | NUMBER | 651.98 | standalone P&L, (a) Current tax, Q1FY27
R086 | page 2 | line 259 | NUMBER | 379.98 | standalone P&L, (a) Current tax, Q2FY26
R087 | page 2 | line 259 | NUMBER | 1,108.37 | standalone P&L, (a) Current tax, H1FY27
R088 | page 2 | line 259 | NUMBER | 727.65 | standalone P&L, (a) Current tax, H1FY26
R089 | page 2 | line 259 | NUMBER | 1,623.03 | standalone P&L, (a) Current tax, FY26
R090 | page 2 | line 260 | NUMBER | 167.33 | standalone P&L, (b) Deferred tax, Q2FY27 | OCR_CONFLICT
R091 | page 2 | line 260 | NUMBER | 38.56 | standalone P&L, (b) Deferred tax, Q1FY27
R092 | page 2 | line 260 | NUMBER | 79.86 | standalone P&L, (b) Deferred tax, Q2FY26
R093 | page 2 | line 260 | NUMBER | 205.89 | standalone P&L, (b) Deferred tax, H1FY27
R094 | page 2 | line 260 | NUMBER | 98.59 | standalone P&L, (b) Deferred tax, H1FY26
R095 | page 2 | line 260 | NUMBER | 268.63 | standalone P&L, (b) Deferred tax, FY26
R096 | page 2 | line 261 | NUMBER | - | standalone P&L, (c) Tax pertain to earlier years, Q2FY27 | ZERO_STANDING
R097 | page 2 | line 261 | NUMBER | - | standalone P&L, (c) Tax pertain to earlier years, Q1FY27 | ZERO_STANDING
R098 | page 2 | line 261 | NUMBER | - | standalone P&L, (c) Tax pertain to earlier years, Q2FY26 | ZERO_STANDING
R099 | page 2 | line 261 | NUMBER | - | standalone P&L, (c) Tax pertain to earlier years, H1FY27 | ZERO_STANDING
R100 | page 2 | line 261 | NUMBER | 13.16 | standalone P&L, (c) Tax pertain to earlier years, H1FY26
R101 | page 2 | line 261 | NUMBER | 13.16 | standalone P&L, (c) Tax pertain to earlier years, FY26
R102 | page 2 | line 262 | NUMBER | 623.72 | standalone P&L, Total tax expenses, Q2FY27 | OCR_CONFLICT
R103 | page 2 | line 262 | NUMBER | 690.54 | standalone P&L, Total tax expenses, Q1FY27
R104 | page 2 | line 262 | NUMBER | 459.84 | standalone P&L, Total tax expenses, Q2FY26
R105 | page 2 | line 262 | NUMBER | 1,314.26 | standalone P&L, Total tax expenses, H1FY27
R106 | page 2 | line 262 | NUMBER | 839.40 | standalone P&L, Total tax expenses, H1FY26
R107 | page 2 | line 262 | NUMBER | 1,904.82 | standalone P&L, Total tax expenses, FY26
R108 | page 2 | line 263 | NUMBER | 1,606.07 | standalone P&L, Profit for the period/year (3-4), Q2FY27
R109 | page 2 | line 263 | NUMBER | 2,011.22 | standalone P&L, Profit for the period/year (3-4), Q1FY27
R110 | page 2 | line 263 | NUMBER | 1,233.80 | standalone P&L, Profit for the period/year (3-4), Q2FY26
R111 | page 2 | line 263 | NUMBER | 3,617.29 | standalone P&L, Profit for the period/year (3-4), H1FY27
R112 | page 2 | line 263 | NUMBER | 2,332.06 | standalone P&L, Profit for the period/year (3-4), H1FY26 | OCR_CONFLICT
R113 | page 2 | line 263 | NUMBER | 5,323.54 | standalone P&L, Profit for the period/year (3-4), FY26
R114 | page 2 | line 263 | NUMBER | 1,606.07 | standalone P&L, Total comprehensive income for the period/year (net of tax) (5+6), Q2FY27
R115 | page 2 | line 263 | NUMBER | 2,011.22 | standalone P&L, Total comprehensive income for the period/year (net of tax) (5+6), Q1FY27
R116 | page 2 | line 263 | NUMBER | 1,233.80 | standalone P&L, Total comprehensive income for the period/year (net of tax) (5+6), Q2FY26
R117 | page 2 | line 263 | NUMBER | 3,617.29 | standalone P&L, Total comprehensive income for the period/year (net of tax) (5+6), H1FY27
R118 | page 2 | line 263 | NUMBER | 2,332.06 | standalone P&L, Total comprehensive income for the period/year (net of tax) (5+6), H1FY26 | OCR_CONFLICT
R119 | page 2 | line 263 | NUMBER | 5,113.92 | standalone P&L, Total comprehensive income for the period/year (net of tax) (5+6), FY26 | OCR_CONFLICT
R120 | page 2 | line 264 | NUMBER | - | standalone P&L, Total other comprehensive income, Q2FY27 | ZERO_STANDING
R121 | page 2 | line 264 | NUMBER | - | standalone P&L, Total other comprehensive income, Q1FY27 | ZERO_STANDING
R122 | page 2 | line 264 | NUMBER | - | standalone P&L, Total other comprehensive income, Q2FY26 | ZERO_STANDING
R123 | page 2 | line 264 | NUMBER | - | standalone P&L, Total other comprehensive income, H1FY27 | ZERO_STANDING
R124 | page 2 | line 264 | NUMBER | - | standalone P&L, Total other comprehensive income, H1FY26 | ZERO_STANDING
R125 | page 2 | line 264 | NUMBER | (209.62) | standalone P&L, Total other comprehensive income, FY26 | OCR_CONFLICT
R126 | page 2 | line 266 | NUMBER | - | standalone P&L, OCI (a) Re-measurement gains/(losses) on defined benefit plans, Q2FY27 | ZERO_STANDING
R127 | page 2 | line 266 | NUMBER | - | standalone P&L, OCI (a) Re-measurement gains/(losses) on defined benefit plans, Q1FY27 | ZERO_STANDING
R128 | page 2 | line 266 | NUMBER | - | standalone P&L, OCI (a) Re-measurement gains/(losses) on defined benefit plans, Q2FY26 | ZERO_STANDING
R129 | page 2 | line 266 | NUMBER | - | standalone P&L, OCI (a) Re-measurement gains/(losses) on defined benefit plans, H1FY27 | ZERO_STANDING
R130 | page 2 | line 266 | NUMBER | - | standalone P&L, OCI (a) Re-measurement gains/(losses) on defined benefit plans, H1FY26 | ZERO_STANDING
R131 | page 2 | line 266 | NUMBER | (27.58) | standalone P&L, OCI (a) Re-measurement gains/(losses) on defined benefit plans, FY26 | OCR_CONFLICT
R132 | page 2 | line 267 | NUMBER | - | standalone P&L, OCI (b) Change in fair value of equity instrument through OCI, Q2FY27 | ZERO_STANDING
R133 | page 2 | line 267 | NUMBER | - | standalone P&L, OCI (b) Change in fair value of equity instrument through OCI, Q1FY27 | ZERO_STANDING
R134 | page 2 | line 267 | NUMBER | - | standalone P&L, OCI (b) Change in fair value of equity instrument through OCI, Q2FY26 | ZERO_STANDING
R135 | page 2 | line 267 | NUMBER | - | standalone P&L, OCI (b) Change in fair value of equity instrument through OCI, H1FY27 | ZERO_STANDING
R136 | page 2 | line 267 | NUMBER | - | standalone P&L, OCI (b) Change in fair value of equity instrument through OCI, H1FY26 | ZERO_STANDING
R137 | page 2 | line 267 | NUMBER | (220.51) | standalone P&L, OCI (b) Change in fair value of equity instrument through OCI, FY26
R138 | page 2 | line 269 | NUMBER | - | standalone P&L, OCI (c) Income tax relating to the above items, Q2FY27 | ZERO_STANDING
R139 | page 2 | line 269 | NUMBER | - | standalone P&L, OCI (c) Income tax relating to the above items, Q1FY27 | ZERO_STANDING
R140 | page 2 | line 269 | NUMBER | - | standalone P&L, OCI (c) Income tax relating to the above items, Q2FY26 | ZERO_STANDING
R141 | page 2 | line 269 | NUMBER | - | standalone P&L, OCI (c) Income tax relating to the above items, H1FY27 | ZERO_STANDING
R142 | page 2 | line 269 | NUMBER | - | standalone P&L, OCI (c) Income tax relating to the above items, H1FY26 | ZERO_STANDING
R143 | page 2 | line 269 | NUMBER | 38.47 | standalone P&L, OCI (c) Income tax relating to the above items, FY26
R144 | page 2 | line 272 | NUMBER | Rs. 10/- | face value per equity share (standalone P&L)
R145 | page 2 | line 272 | NUMBER | 1801.58 | standalone P&L, Paid up equity share capital (Face value Rs. 10/- each), Q2FY27
R146 | page 2 | line 272 | NUMBER | 1801.58 | standalone P&L, Paid up equity share capital (Face value Rs. 10/- each), Q1FY27
R147 | page 2 | line 272 | NUMBER | 1801.58 | standalone P&L, Paid up equity share capital (Face value Rs. 10/- each), Q2FY26
R148 | page 2 | line 272 | NUMBER | 1801.58 | standalone P&L, Paid up equity share capital (Face value Rs. 10/- each), H1FY27
R149 | page 2 | line 272 | NUMBER | 1801.58 | standalone P&L, Paid up equity share capital (Face value Rs. 10/- each), H1FY26
R150 | page 2 | line 272 | NUMBER | 1801.58 | standalone P&L, Paid up equity share capital (Face value Rs. 10/- each), FY26
R151 | page 2 | line 273 | NUMBER | - | standalone P&L, Other equity, Q2FY27 | ZERO_STANDING
R152 | page 2 | line 273 | NUMBER | - | standalone P&L, Other equity, Q1FY27 | ZERO_STANDING
R153 | page 2 | line 273 | NUMBER | - | standalone P&L, Other equity, Q2FY26 | ZERO_STANDING
R154 | page 2 | line 273 | NUMBER | - | standalone P&L, Other equity, H1FY27 | ZERO_STANDING
R155 | page 2 | line 273 | NUMBER | - | standalone P&L, Other equity, H1FY26 | ZERO_STANDING
R156 | page 2 | line 273 | NUMBER | 27,509.68 | standalone P&L, Other equity, FY26
R157 | page 2 | line 276 | NUMBER | 8.91 | standalone P&L, Basic earning per share (Rs.), Q2FY27
R158 | page 2 | line 276 | NUMBER | 11.16 | standalone P&L, Basic earning per share (Rs.), Q1FY27 | OCR_CONFLICT
R159 | page 2 | line 276 | NUMBER | 7.01 | standalone P&L, Basic earning per share (Rs.), Q2FY26
R160 | page 2 | line 276 | NUMBER | 20.08 | standalone P&L, Basic earning per share (Rs.), H1FY27
R161 | page 2 | line 276 | NUMBER | 13.41 | standalone P&L, Basic earning per share (Rs.), H1FY26
R162 | page 2 | line 276 | NUMBER | 29.90 | standalone P&L, Basic earning per share (Rs.), FY26 | OCR_CONFLICT
R163 | page 2 | line 277 | NUMBER | 8.91 | standalone P&L, Diluted earning per share (Rs.), Q2FY27
R164 | page 2 | line 277 | NUMBER | 11.16 | standalone P&L, Diluted earning per share (Rs.), Q1FY27
R165 | page 2 | line 277 | NUMBER | 7.01 | standalone P&L, Diluted earning per share (Rs.), Q2FY26
R166 | page 2 | line 277 | NUMBER | 20.06 | standalone P&L, Diluted earning per share (Rs.), H1FY27
R167 | page 2 | line 277 | NUMBER | 13.40 | standalone P&L, Diluted earning per share (Rs.), H1FY26 | OCR_CONFLICT
R168 | page 2 | line 277 | NUMBER | 29.88 | standalone P&L, Diluted earning per share (Rs.), FY26 | OCR_CONFLICT
R169 | page 2 | line 280 | NUMBER | DIN 00087088 | director DIN
R170 | page 3 | line 380 | NUMBER | L51909DL1987PLC027186 | CIN
R171 | page 3 | line 384 | NUMBER | 37,907.86 | standalone balance sheet, Total non-current assets, 30-Sep-2026 | OCR_CONFLICT
R172 | page 3 | line 384 | NUMBER | 33,673.28 | standalone balance sheet, Total non-current assets, 31-Mar-2026 | OCR_CONFLICT
R173 | page 3 | line 385 | NUMBER | 27,128.09 | standalone balance sheet, Property, plant and equipment, 30-Sep-2026
R174 | page 3 | line 385 | NUMBER | 22,281.88 | standalone balance sheet, Property, plant and equipment, 31-Mar-2026
R175 | page 3 | line 386 | NUMBER | 3,135.98 | standalone balance sheet, Capital work in progress, 30-Sep-2026
R176 | page 3 | line 386 | NUMBER | 4,119.11 | standalone balance sheet, Capital work in progress, 31-Mar-2026
R177 | page 3 | line 387 | NUMBER | 530.39 | standalone balance sheet, Investment property, 30-Sep-2026
R178 | page 3 | line 387 | NUMBER | 530.39 | standalone balance sheet, Investment property, 31-Mar-2026
R179 | page 3 | line 388 | NUMBER | 953.61 | standalone balance sheet, Right of use assets, 30-Sep-2026
R180 | page 3 | line 388 | NUMBER | 768.54 | standalone balance sheet, Right of use assets, 31-Mar-2026
R181 | page 3 | line 389 | NUMBER | 6.79 | standalone balance sheet, Other intangible assets, 30-Sep-2026
R182 | page 3 | line 389 | NUMBER | 7.34 | standalone balance sheet, Other intangible assets, 31-Mar-2026
R183 | page 3 | line 390 | NUMBER | 54,398.64 | standalone balance sheet, Total assets, 30-Sep-2026 | OCR_CONFLICT
R184 | page 3 | line 390 | NUMBER | 51,568.88 | standalone balance sheet, Total assets, 31-Mar-2026 | OCR_CONFLICT
R185 | page 3 | line 391 | NUMBER | 1,602.89 | standalone balance sheet, i) Investments in subsidiaries, 30-Sep-2026
R186 | page 3 | line 391 | NUMBER | 1,331.78 | standalone balance sheet, i) Investments in subsidiaries, 31-Mar-2026
R187 | page 3 | line 392 | NUMBER | 1,039.67 | standalone balance sheet, ii) Investment in associate and joint venture, 30-Sep-2026
R188 | page 3 | line 392 | NUMBER | 1,039.67 | standalone balance sheet, ii) Investment in associate and joint venture, 31-Mar-2026
R189 | page 3 | line 393 | NUMBER | 2,016.46 | standalone balance sheet, iii) Investments, 30-Sep-2026
R190 | page 3 | line 393 | NUMBER | 2,014.46 | standalone balance sheet, iii) Investments, 31-Mar-2026
R191 | page 3 | line 394 | NUMBER | 95.27 | standalone balance sheet, iv) Loans (non-current), 30-Sep-2026
R192 | page 3 | line 394 | NUMBER | - | standalone balance sheet, iv) Loans (non-current), 31-Mar-2026 | ZERO_STANDING
R193 | page 3 | line 395 | NUMBER | 471.20 | standalone balance sheet, iv) Other financial assets (non-current), 30-Sep-2026
R194 | page 3 | line 395 | NUMBER | 375.12 | standalone balance sheet, iv) Other financial assets (non-current), 31-Mar-2026 | OCR_CONFLICT
R195 | page 3 | line 396 | NUMBER | 927.51 | standalone balance sheet, Other non-current assets, 30-Sep-2026 | OCR_CONFLICT
R196 | page 3 | line 396 | NUMBER | 1,204.99 | standalone balance sheet, Other non-current assets, 31-Mar-2026
R197 | page 3 | line 397 | NUMBER | 16,490.78 | standalone balance sheet, Total current assets, 30-Sep-2026 | OCR_CONFLICT
R198 | page 3 | line 397 | NUMBER | 17,895.60 | standalone balance sheet, Total current assets, 31-Mar-2026 | OCR_CONFLICT
R199 | page 3 | line 398 | NUMBER | 7,721.95 | standalone balance sheet, Inventories, 30-Sep-2026 | OCR_CONFLICT
R200 | page 3 | line 398 | NUMBER | 7,082.37 | standalone balance sheet, Inventories, 31-Mar-2026
R201 | page 3 | line 400 | NUMBER | 5,180.94 | standalone balance sheet, i) Trade receivables, 30-Sep-2026
R202 | page 3 | line 400 | NUMBER | 6,528.70 | standalone balance sheet, i) Trade receivables, 31-Mar-2026
R203 | page 3 | line 401 | NUMBER | 93.30 | standalone balance sheet, ii) Cash and cash equivalents, 30-Sep-2026
R204 | page 3 | line 401 | NUMBER | 89.29 | standalone balance sheet, ii) Cash and cash equivalents, 31-Mar-2026
R205 | page 3 | line 402 | NUMBER | 325.38 | standalone balance sheet, iii) Bank balances other than (ii) above, 30-Sep-2026
R206 | page 3 | line 402 | NUMBER | 271.45 | standalone balance sheet, iii) Bank balances other than (ii) above, 31-Mar-2026 | OCR_CONFLICT
R207 | page 3 | line 403 | NUMBER | 30.34 | standalone balance sheet, iv) Loans (current), 30-Sep-2026
R208 | page 3 | line 403 | NUMBER | 37.01 | standalone balance sheet, iv) Loans (current), 31-Mar-2026
R209 | page 3 | line 404 | NUMBER | 408.05 | standalone balance sheet, v) Others financial assets (current), 30-Sep-2026
R210 | page 3 | line 404 | NUMBER | 305.70 | standalone balance sheet, v) Others financial assets (current), 31-Mar-2026
R211 | page 3 | line 405 | NUMBER | 2,730.82 | standalone balance sheet, Other current assets, 30-Sep-2026
R212 | page 3 | line 405 | NUMBER | 3,581.08 | standalone balance sheet, Other current assets, 31-Mar-2026
R213 | page 3 | line 409 | NUMBER | 1,801.58 | standalone balance sheet, Equity share capital, 30-Sep-2026
R214 | page 3 | line 409 | NUMBER | 1,801.58 | standalone balance sheet, Equity share capital, 31-Mar-2026
R215 | page 3 | line 410 | NUMBER | 30,565.80 | standalone balance sheet, Other equity, 30-Sep-2026
R216 | page 3 | line 410 | NUMBER | 27,509.68 | standalone balance sheet, Other equity, 31-Mar-2026
R217 | page 3 | line 411 | NUMBER | 32,367.38 | standalone balance sheet, Total equity, 30-Sep-2026 | OCR_CONFLICT
R218 | page 3 | line 411 | NUMBER | 29,311.26 | standalone balance sheet, Total equity, 31-Mar-2026
R219 | page 3 | line 413 | NUMBER | 6,900.38 | standalone balance sheet, Total non-current liabilities, 30-Sep-2026 | OCR_CONFLICT
R220 | page 3 | line 413 | NUMBER | 5,851.78 | standalone balance sheet, Total non-current liabilities, 31-Mar-2026 | OCR_CONFLICT
R221 | page 3 | line 415 | NUMBER | 4,445.16 | standalone balance sheet, Non-current (i) Borrowings, 30-Sep-2026
R222 | page 3 | line 415 | NUMBER | 3,818.17 | standalone balance sheet, Non-current (i) Borrowings, 31-Mar-2026
R223 | page 3 | line 416 | NUMBER | 907.08 | standalone balance sheet, Non-current (ii) Lease liabilities, 30-Sep-2026 | OCR_CONFLICT
R224 | page 3 | line 416 | NUMBER | 739.62 | standalone balance sheet, Non-current (ii) Lease liabilities, 31-Mar-2026
R225 | page 3 | line 417 | NUMBER | 521.31 | standalone balance sheet, Non-current Provisions, 30-Sep-2026 | OCR_CONFLICT
R226 | page 3 | line 417 | NUMBER | 473.05 | standalone balance sheet, Non-current Provisions, 31-Mar-2026
R227 | page 3 | line 418 | NUMBER | 1,026.83 | standalone balance sheet, Deferred tax liabilities (net), 30-Sep-2026 | OCR_CONFLICT
R228 | page 3 | line 418 | NUMBER | 820.94 | standalone balance sheet, Deferred tax liabilities (net), 31-Mar-2026
R229 | page 3 | line 419 | NUMBER | 15,130.88 | standalone balance sheet, Total current liabilities, 30-Sep-2026 | OCR_CONFLICT
R230 | page 3 | line 419 | NUMBER | 16,405.84 | standalone balance sheet, Total current liabilities, 31-Mar-2026 | OCR_CONFLICT
R231 | page 3 | line 420 | NUMBER | 54,398.64 | standalone balance sheet, Total equity and liabilities, 30-Sep-2026 | OCR_CONFLICT
R232 | page 3 | line 420 | NUMBER | 51,568.88 | standalone balance sheet, Total equity and liabilities, 31-Mar-2026 | OCR_CONFLICT
R233 | page 3 | line 421 | NUMBER | 6,683.57 | standalone balance sheet, Current i) Borrowings, 30-Sep-2026 | OCR_CONFLICT
R234 | page 3 | line 421 | NUMBER | 8,239.02 | standalone balance sheet, Current i) Borrowings, 31-Mar-2026
R235 | page 3 | line 422 | NUMBER | 85.91 | standalone balance sheet, Current ii) Lease liabilities, 30-Sep-2026
R236 | page 3 | line 422 | NUMBER | 37.63 | standalone balance sheet, Current ii) Lease liabilities, 31-Mar-2026
R237 | page 3 | line 424 | NUMBER | 832.14 | standalone balance sheet, iii)(a) Trade payables, dues of micro enterprises and small enterprises, 30-Sep-2026 | OCR_CONFLICT
R238 | page 3 | line 424 | NUMBER | 903.00 | standalone balance sheet, iii)(a) Trade payables, dues of micro enterprises and small enterprises, 31-Mar-2026
R239 | page 3 | line 426 | NUMBER | 5,010.01 | standalone balance sheet, iii)(b) Trade payables, dues of creditors other than micro and small enterprises, 30-Sep-2026
R240 | page 3 | line 426 | NUMBER | 5,058.22 | standalone balance sheet, iii)(b) Trade payables, dues of creditors other than micro and small enterprises, 31-Mar-2026
R241 | page 3 | line 428 | NUMBER | 940.66 | standalone balance sheet, iv) Other financial liabilities, 30-Sep-2026
R242 | page 3 | line 428 | NUMBER | 744.67 | standalone balance sheet, iv) Other financial liabilities, 31-Mar-2026
R243 | page 3 | line 429 | NUMBER | 901.76 | standalone balance sheet, Other current liabilities, 30-Sep-2026
R244 | page 3 | line 429 | NUMBER | 649.03 | standalone balance sheet, Other current liabilities, 31-Mar-2026
R245 | page 3 | line 430 | NUMBER | 196.20 | standalone balance sheet, Current Provisions, 30-Sep-2026 | OCR_CONFLICT
R246 | page 3 | line 430 | NUMBER | 168.39 | standalone balance sheet, Current Provisions, 31-Mar-2026
R247 | page 3 | line 431 | NUMBER | 480.63 | standalone balance sheet, Current tax liabilities (net), 30-Sep-2026 | OCR_CONFLICT
R248 | page 3 | line 431 | NUMBER | 605.88 | standalone balance sheet, Current tax liabilities (net), 31-Mar-2026
R249 | page 3 | line 435 | NUMBER | DIN 00087088 | director DIN (read from image) | IMAGE_READ
R250 | page 4 | line 523 | NUMBER | 8,055.99 | standalone cash flow, Cash generated from operations, H1FY27 | OCR_CONFLICT
R251 | page 4 | line 523 | NUMBER | 2,640.16 | standalone cash flow, Cash generated from operations, H1FY26 | OCR_CONFLICT
R252 | page 4 | line 524 | NUMBER | 4,931.55 | standalone cash flow, Profit before tax, H1FY27
R253 | page 4 | line 524 | NUMBER | 3,171.46 | standalone cash flow, Profit before tax, H1FY26
R254 | page 4 | line 526 | NUMBER | 774.30 | standalone cash flow, Depreciation and amortisation expense, H1FY27
R255 | page 4 | line 526 | NUMBER | 497.85 | standalone cash flow, Depreciation and amortisation expense, H1FY26
R256 | page 4 | line 527 | NUMBER | 0.02 | standalone cash flow, Loss/(gain) on disposal of PPE, H1FY27
R257 | page 4 | line 527 | NUMBER | (1.08) | standalone cash flow, Loss/(gain) on disposal of PPE, H1FY26
R258 | page 4 | line 528 | NUMBER | (27.00) | standalone cash flow, Rental income (adjustment), H1FY27
R259 | page 4 | line 528 | NUMBER | (18.00) | standalone cash flow, Rental income (adjustment), H1FY26
R260 | page 4 | line 528 | NUMBER | 27.00 | standalone cash flow, Rental income (investing), H1FY27
R261 | page 4 | line 528 | NUMBER | 18.00 | standalone cash flow, Rental income (investing), H1FY26
R262 | page 4 | line 529 | NUMBER | 24.13 | standalone cash flow, Provision for expected credit loss, H1FY27
R263 | page 4 | line 529 | NUMBER | 21.06 | standalone cash flow, Provision for expected credit loss, H1FY26
R264 | page 4 | line 530 | NUMBER | 24.34 | standalone cash flow, Expenses on employees stock options scheme, H1FY27
R265 | page 4 | line 530 | NUMBER | 45.45 | standalone cash flow, Expenses on employees stock options scheme, H1FY26
R266 | page 4 | line 531 | NUMBER | (46.83) | standalone cash flow, Excess provisions written back, H1FY27
R267 | page 4 | line 531 | NUMBER | 1.70 | standalone cash flow, Excess provisions written back, H1FY26
R268 | page 4 | line 532 | NUMBER | 549.58 | standalone cash flow, Finance cost, H1FY27 | OCR_CONFLICT
R269 | page 4 | line 532 | NUMBER | 536.82 | standalone cash flow, Finance cost, H1FY26
R270 | page 4 | line 533 | NUMBER | 7.57 | standalone cash flow, Unrealised foreign exchange gain, H1FY27
R271 | page 4 | line 533 | NUMBER | - | standalone cash flow, Unrealised foreign exchange gain, H1FY26 | ZERO_STANDING
R272 | page 4 | line 534 | NUMBER | (45.76) | standalone cash flow, Finance income, H1FY27
R273 | page 4 | line 534 | NUMBER | (48.73) | standalone cash flow, Finance income, H1FY26
R274 | page 4 | line 535 | NUMBER | 6,191.90 | standalone cash flow, Operating profit before working capital changes, H1FY27 | OCR_CONFLICT
R275 | page 4 | line 535 | NUMBER | 4,206.53 | standalone cash flow, Operating profit before working capital changes, H1FY26
R276 | page 4 | line 537 | NUMBER | (639.58) | standalone cash flow, (Increase)/decrease in inventories, H1FY27
R277 | page 4 | line 537 | NUMBER | (1,174.82) | standalone cash flow, (Increase)/decrease in inventories, H1FY26
R278 | page 4 | line 538 | NUMBER | 1,323.64 | standalone cash flow, (Increase)/decrease in trade receivables, H1FY27
R279 | page 4 | line 538 | NUMBER | (1,046.04) | standalone cash flow, (Increase)/decrease in trade receivables, H1FY26
R280 | page 4 | line 539 | NUMBER | (211.45) | standalone cash flow, (Increase)/decrease in other financial assets, H1FY27
R281 | page 4 | line 539 | NUMBER | (103.11) | standalone cash flow, (Increase)/decrease in other financial assets, H1FY26
R282 | page 4 | line 540 | NUMBER | 857.81 | standalone cash flow, (Increase)/decrease in other assets, H1FY27
R283 | page 4 | line 540 | NUMBER | 292.33 | standalone cash flow, (Increase)/decrease in other assets, H1FY26
R284 | page 4 | line 541 | NUMBER | (79.80) | standalone cash flow, Increase/(decrease) in trade payables, H1FY27
R285 | page 4 | line 541 | NUMBER | 393.63 | standalone cash flow, Increase/(decrease) in trade payables, H1FY26
R286 | page 4 | line 542 | NUMBER | 284.67 | standalone cash flow, Increase/(decrease) in other financial liabilities, H1FY27
R287 | page 4 | line 542 | NUMBER | (145.76) | standalone cash flow, Increase/(decrease) in other financial liabilities, H1FY26
R288 | page 4 | line 543 | NUMBER | 252.73 | standalone cash flow, Increase/(decrease) in other liabilities, H1FY27
R289 | page 4 | line 543 | NUMBER | 133.76 | standalone cash flow, Increase/(decrease) in other liabilities, H1FY26
R290 | page 4 | line 544 | NUMBER | 76.07 | standalone cash flow, Increase/(decrease) in provisions, H1FY27
R291 | page 4 | line 544 | NUMBER | 83.64 | standalone cash flow, Increase/(decrease) in provisions, H1FY26
R292 | page 4 | line 545 | NUMBER | (1,233.61) | standalone cash flow, Income tax paid (net of refunds), H1FY27 | OCR_CONFLICT
R293 | page 4 | line 545 | NUMBER | (571.86) | standalone cash flow, Income tax paid (net of refunds), H1FY26 | OCR_CONFLICT
R294 | page 4 | line 548 | NUMBER | 6,822.38 | standalone cash flow, Net cash flow generated from operating activities (A), H1FY27 | OCR_CONFLICT
R295 | page 4 | line 548 | NUMBER | 2,068.30 | standalone cash flow, Net cash flow generated from operating activities (A), H1FY26 | OCR_CONFLICT
R296 | page 4 | line 549 | NUMBER | (4,473.96) | standalone cash flow, Purchase of property plant & equipment (net of capital advances and capital payables), H1FY27
R297 | page 4 | line 549 | NUMBER | (5,320.33) | standalone cash flow, Purchase of property plant & equipment (net of capital advances and capital payables), H1FY26
R298 | page 4 | line 551 | NUMBER | 59.11 | standalone cash flow, Proceeds from sale of property, plant and equipment, H1FY27
R299 | page 4 | line 551 | NUMBER | 42.79 | standalone cash flow, Proceeds from sale of property, plant and equipment, H1FY26
R300 | page 4 | line 553 | NUMBER | (89.41) | standalone cash flow, Loan given & received back, H1FY27
R301 | page 4 | line 553 | NUMBER | 3.43 | standalone cash flow, Loan given & received back, H1FY26
R302 | page 4 | line 554 | NUMBER | (271.11) | standalone cash flow, Investment in subsidiary, H1FY27
R303 | page 4 | line 554 | NUMBER | (181.47) | standalone cash flow, Investment in subsidiary, H1FY26
R304 | page 4 | line 555 | NUMBER | - | standalone cash flow, Proceeds from sale of investment, H1FY27 | ZERO_STANDING
R305 | page 4 | line 555 | NUMBER | 500.75 | standalone cash flow, Proceeds from sale of investment, H1FY26
R306 | page 4 | line 556 | NUMBER | 44.53 | standalone cash flow, Interest received, H1FY27
R307 | page 4 | line 556 | NUMBER | 48.73 | standalone cash flow, Interest received, H1FY26
R308 | page 4 | line 557 | NUMBER | (20.15) | standalone cash flow, (Investing in)/redemption of term deposit, H1FY27
R309 | page 4 | line 557 | NUMBER | 64.47 | standalone cash flow, (Investing in)/redemption of term deposit, H1FY26
R310 | page 4 | line 559 | NUMBER | (4,723.99) | standalone cash flow, Net cash flow (used) in investing activities (B), H1FY27 | OCR_CONFLICT
R311 | page 4 | line 559 | NUMBER | (4,823.63) | standalone cash flow, Net cash flow (used) in investing activities (B), H1FY26 | OCR_CONFLICT
R312 | page 4 | line 560 | NUMBER | - | standalone cash flow, Proceed from issue of equity shares, H1FY27 | ZERO_STANDING
R313 | page 4 | line 560 | NUMBER | 7,620.30 | standalone cash flow, Proceed from issue of equity shares, H1FY26
R314 | page 4 | line 561 | NUMBER | 1,503.22 | standalone cash flow, Proceeds of long term borrowings, H1FY27
R315 | page 4 | line 561 | NUMBER | 110.89 | standalone cash flow, Proceeds of long term borrowings, H1FY26
R316 | page 4 | line 562 | NUMBER | (799.58) | standalone cash flow, Repayments from long term borrowings, H1FY27
R317 | page 4 | line 562 | NUMBER | (2,420.11) | standalone cash flow, Repayments from long term borrowings, H1FY26
R318 | page 4 | line 563 | NUMBER | (1,632.11) | standalone cash flow, Proceeds/(repayment) of short term borrowings, H1FY27
R319 | page 4 | line 563 | NUMBER | (707.65) | standalone cash flow, Proceeds/(repayment) of short term borrowings, H1FY26
R320 | page 4 | line 564 | NUMBER | (38.23) | standalone cash flow, Payment of principal portion of lease liabilities, H1FY27
R321 | page 4 | line 564 | NUMBER | - | standalone cash flow, Payment of principal portion of lease liabilities, H1FY26 | ZERO_STANDING
R322 | page 4 | line 565 | NUMBER | (48.58) | standalone cash flow, Payment of interest on lease liabilities, H1FY27
R323 | page 4 | line 565 | NUMBER | - | standalone cash flow, Payment of interest on lease liabilities, H1FY26 | ZERO_STANDING
R324 | page 4 | line 566 | NUMBER | (585.52) | standalone cash flow, Dividend paid, H1FY27
R325 | page 4 | line 566 | NUMBER | (692.70) | standalone cash flow, Dividend paid, H1FY26
R326 | page 4 | line 567 | NUMBER | (493.58) | standalone cash flow, Interest paid, H1FY27
R327 | page 4 | line 567 | NUMBER | (539.15) | standalone cash flow, Interest paid, H1FY26
R328 | page 4 | line 567 | NUMBER | (2,094.38) | standalone cash flow, Net cash flow from/(used) in financing activities (C), H1FY27 | OCR_CONFLICT|OCR_ROW_MISSING(no label or digit match in OCR; anchored to preceding OCR line)
R329 | page 4 | line 567 | NUMBER | 3,371.58 | standalone cash flow, Net cash flow from/(used) in financing activities (C), H1FY26 | OCR_CONFLICT|OCR_ROW_MISSING(no label or digit match in OCR; anchored to preceding OCR line)
R330 | page 4 | line 569 | NUMBER | 4.01 | standalone cash flow, Net increase/(decrease) in cash and cash equivalents (A+B+C), H1FY27 | OCR_CONFLICT
R331 | page 4 | line 569 | NUMBER | 616.25 | standalone cash flow, Net increase/(decrease) in cash and cash equivalents (A+B+C), H1FY26 | OCR_CONFLICT
R332 | page 4 | line 569 | NUMBER | 89.29 | standalone cash flow, Cash and cash equivalents at the beginning of the period, H1FY27
R333 | page 4 | line 569 | NUMBER | 203.71 | standalone cash flow, Cash and cash equivalents at the beginning of the period, H1FY26
R334 | page 4 | line 569 | NUMBER | 93.30 | standalone cash flow, Cash and cash equivalents at the end of the period, H1FY27 | OCR_CONFLICT|OCR_ROW_MISSING(no label or digit match in OCR; anchored to preceding OCR line)
R335 | page 4 | line 569 | NUMBER | 819.96 | standalone cash flow, Cash and cash equivalents at the end of the period, H1FY26 | OCR_CONFLICT|OCR_ROW_MISSING(no label or digit match in OCR; anchored to preceding OCR line)
R336 | page 4 | line 574 | NUMBER | DIN 00087088 | director DIN
R337 | page 5 | line 593 | NUMBER | Chilean Pesos 500,000,000 | Chile SpA authorised capital
R338 | page 5 | line 593 | NUMBER | Chilean Pesos IO each (embedded) / Chilean Pesos 10 each (OCR) | Chile SpA face value per share, Chilean Pesos 10 | OCR_CORRECTED
R339 | page 5 | line 599 | NUMBER | 34 kanals and 8 marlas | Panipat land area
R340 | page 5 | line 602 | NUMBER | 20 kanals and 12 marlas | land released from acquisition
R341 | page 5 | line 603 | NUMBER | Rs. 373.27 lakhs | HSIIDC demand for allotment of land
R342 | page 5 | line 636 | NUMBER | 5,00,00,000 equity shares | Chile SpA authorised share count (OCR layer value; embedded layer reads S,00,00,000) | OCR_CORRECTED
R343 | page 7 | line 744 | NUMBER | 000756N/N500441 | auditor firm registration no.
R344 | page 7 | line 750 | NUMBER | 512497 | partner membership no.
R345 | page 7 | line 753 | NUMBER | UDIN 26512497ESCFEY1292 | UDIN standalone
R346 | page 8 | line 840 | NUMBER | L51909DL1987PLC0271 86 (as OCR printed; CIN L51909DL1987PLC027186) | CIN | OCR_SPACE
R347 | page 8 | line 848 | NUMBER | 15,659.32 | consolidated P&L, Revenues from operations, Q2FY27 | OCR_CONFLICT
R348 | page 8 | line 848 | NUMBER | 15,618.12 | consolidated P&L, Revenues from operations, Q1FY27
R349 | page 8 | line 848 | NUMBER | 11,951.88 | consolidated P&L, Revenues from operations, Q2FY26 | OCR_CONFLICT
R350 | page 8 | line 848 | NUMBER | 31,277.44 | consolidated P&L, Revenues from operations, H1FY27 | OCR_CONFLICT
R351 | page 8 | line 848 | NUMBER | 24,979.21 | consolidated P&L, Revenues from operations, H1FY26 | OCR_CONFLICT
R352 | page 8 | line 848 | NUMBER | 54,580.74 | consolidated P&L, Revenues from operations, FY26 | OCR_CONFLICT
R353 | page 8 | line 849 | NUMBER | 72.54 | consolidated P&L, Other income, Q2FY27
R354 | page 8 | line 849 | NUMBER | 62.62 | consolidated P&L, Other income, Q1FY27
R355 | page 8 | line 849 | NUMBER | 24.18 | consolidated P&L, Other income, Q2FY26 | OCR_CONFLICT
R356 | page 8 | line 849 | NUMBER | 135.16 | consolidated P&L, Other income, H1FY27 | OCR_CONFLICT
R357 | page 8 | line 849 | NUMBER | 60.13 | consolidated P&L, Other income, H1FY26 | OCR_CONFLICT
R358 | page 8 | line 849 | NUMBER | 195.22 | consolidated P&L, Other income, FY26
R359 | page 8 | line 850 | NUMBER | 15,731.86 | consolidated P&L, Total income, Q2FY27
R360 | page 8 | line 850 | NUMBER | 15,680.74 | consolidated P&L, Total income, Q1FY27 | OCR_CONFLICT
R361 | page 8 | line 850 | NUMBER | 11,976.06 | consolidated P&L, Total income, Q2FY26 | OCR_CONFLICT
R362 | page 8 | line 850 | NUMBER | 31,412.60 | consolidated P&L, Total income, H1FY27 | OCR_CONFLICT
R363 | page 8 | line 850 | NUMBER | 25,039.34 | consolidated P&L, Total income, H1FY26
R364 | page 8 | line 850 | NUMBER | 54,775.96 | consolidated P&L, Total income, FY26 | OCR_CONFLICT
R365 | page 8 | line 851 | NUMBER | 13,405.73 | consolidated P&L, Total expenses, Q2FY27 | OCR_CONFLICT
R366 | page 8 | line 851 | NUMBER | 12,948.09 | consolidated P&L, Total expenses, Q1FY27 | OCR_CONFLICT
R367 | page 8 | line 851 | NUMBER | 10,330.70 | consolidated P&L, Total expenses, Q2FY26 | OCR_CONFLICT
R368 | page 8 | line 851 | NUMBER | 26,353.82 | consolidated P&L, Total expenses, H1FY27 | OCR_CONFLICT
R369 | page 8 | line 851 | NUMBER | 21,867.89 | consolidated P&L, Total expenses, H1FY26 | OCR_CONFLICT
R370 | page 8 | line 851 | NUMBER | 47,542.93 | consolidated P&L, Total expenses, FY26 | OCR_CONFLICT
R371 | page 8 | line 852 | NUMBER | 6,449.83 | consolidated P&L, (a) Cost of material consumed, Q2FY27
R372 | page 8 | line 852 | NUMBER | 6,580.70 | consolidated P&L, (a) Cost of material consumed, Q1FY27
R373 | page 8 | line 852 | NUMBER | 4,668.89 | consolidated P&L, (a) Cost of material consumed, Q2FY26 | OCR_CONFLICT
R374 | page 8 | line 852 | NUMBER | 13,030.53 | consolidated P&L, (a) Cost of material consumed, H1FY27 | OCR_CONFLICT
R375 | page 8 | line 852 | NUMBER | 9,744.24 | consolidated P&L, (a) Cost of material consumed, H1FY26 | OCR_CONFLICT
R376 | page 8 | line 852 | NUMBER | 22,445.25 | consolidated P&L, (a) Cost of material consumed, FY26 | OCR_CONFLICT
R377 | page 8 | line 853 | NUMBER | 1,525.45 | consolidated P&L, (b) Purchase of stock in trade, Q2FY27 | OCR_CONFLICT
R378 | page 8 | line 853 | NUMBER | 1,126.58 | consolidated P&L, (b) Purchase of stock in trade, Q1FY27 | OCR_CONFLICT
R379 | page 8 | line 853 | NUMBER | 1,363.09 | consolidated P&L, (b) Purchase of stock in trade, Q2FY26 | OCR_CONFLICT
R380 | page 8 | line 853 | NUMBER | 2,652.03 | consolidated P&L, (b) Purchase of stock in trade, H1FY27 | OCR_CONFLICT
R381 | page 8 | line 853 | NUMBER | 3,086.04 | consolidated P&L, (b) Purchase of stock in trade, H1FY26 | OCR_CONFLICT
R382 | page 8 | line 853 | NUMBER | 5,343.27 | consolidated P&L, (b) Purchase of stock in trade, FY26
R383 | page 8 | line 854 | NUMBER | (756.66) | consolidated P&L, (c) Changes in inventories of finished goods, work in progress and stock in trade, Q2FY27 | OCR_CONFLICT
R384 | page 8 | line 854 | NUMBER | (419.36) | consolidated P&L, (c) Changes in inventories of finished goods, work in progress and stock in trade, Q1FY27 | OCR_CONFLICT
R385 | page 8 | line 854 | NUMBER | (534.20) | consolidated P&L, (c) Changes in inventories of finished goods, work in progress and stock in trade, Q2FY26 | OCR_CONFLICT
R386 | page 8 | line 854 | NUMBER | (1,176.02) | consolidated P&L, (c) Changes in inventories of finished goods, work in progress and stock in trade, H1FY27 | OCR_CONFLICT
R387 | page 8 | line 854 | NUMBER | (463.34) | consolidated P&L, (c) Changes in inventories of finished goods, work in progress and stock in trade, H1FY26 | OCR_CONFLICT
R388 | page 8 | line 854 | NUMBER | 328.43 | consolidated P&L, (c) Changes in inventories of finished goods, work in progress and stock in trade, FY26 | OCR_CONFLICT
R389 | page 8 | line 856 | NUMBER | 1,964.43 | consolidated P&L, (d) Employee benefits expense, Q2FY27
R390 | page 8 | line 856 | NUMBER | 1,680.77 | consolidated P&L, (d) Employee benefits expense, Q1FY27
R391 | page 8 | line 856 | NUMBER | 1,664.58 | consolidated P&L, (d) Employee benefits expense, Q2FY26 | OCR_CONFLICT
R392 | page 8 | line 856 | NUMBER | 3,645.20 | consolidated P&L, (d) Employee benefits expense, H1FY27 | OCR_CONFLICT
R393 | page 8 | line 856 | NUMBER | 3,205.99 | consolidated P&L, (d) Employee benefits expense, H1FY26
R394 | page 8 | line 856 | NUMBER | 6,367.32 | consolidated P&L, (d) Employee benefits expense, FY26 | OCR_CONFLICT
R395 | page 8 | line 857 | NUMBER | 263.65 | consolidated P&L, (e) Finance costs, Q2FY27 | OCR_CONFLICT
R396 | page 8 | line 857 | NUMBER | 289.05 | consolidated P&L, (e) Finance costs, Q1FY27 | OCR_CONFLICT
R397 | page 8 | line 857 | NUMBER | 237.85 | consolidated P&L, (e) Finance costs, Q2FY26 | OCR_CONFLICT
R398 | page 8 | line 857 | NUMBER | 552.70 | consolidated P&L, (e) Finance costs, H1FY27 | OCR_CONFLICT
R399 | page 8 | line 857 | NUMBER | 541.59 | consolidated P&L, (e) Finance costs, H1FY26 | OCR_CONFLICT
R400 | page 8 | line 857 | NUMBER | 1,085.00 | consolidated P&L, (e) Finance costs, FY26 | OCR_CONFLICT
R401 | page 8 | line 858 | NUMBER | 427.80 | consolidated P&L, (f) Depreciation and amortization expenses, Q2FY27
R402 | page 8 | line 858 | NUMBER | 431.29 | consolidated P&L, (f) Depreciation and amortization expenses, Q1FY27
R403 | page 8 | line 858 | NUMBER | 297.06 | consolidated P&L, (f) Depreciation and amortization expenses, Q2FY26
R404 | page 8 | line 858 | NUMBER | 859.09 | consolidated P&L, (f) Depreciation and amortization expenses, H1FY27
R405 | page 8 | line 858 | NUMBER | 581.95 | consolidated P&L, (f) Depreciation and amortization expenses, H1FY26 | OCR_CONFLICT
R406 | page 8 | line 858 | NUMBER | 1,229.25 | consolidated P&L, (f) Depreciation and amortization expenses, FY26 | OCR_CONFLICT
R407 | page 8 | line 859 | NUMBER | 3,531.23 | consolidated P&L, (g) Other expenses, Q2FY27 | OCR_CONFLICT
R408 | page 8 | line 859 | NUMBER | 3,259.06 | consolidated P&L, (g) Other expenses, Q1FY27
R409 | page 8 | line 859 | NUMBER | 2,633.43 | consolidated P&L, (g) Other expenses, Q2FY26
R410 | page 8 | line 859 | NUMBER | 6,790.29 | consolidated P&L, (g) Other expenses, H1FY27
R411 | page 8 | line 859 | NUMBER | 5,171.42 | consolidated P&L, (g) Other expenses, H1FY26 | OCR_CONFLICT
R412 | page 8 | line 859 | NUMBER | 10,744.41 | consolidated P&L, (g) Other expenses, FY26
R413 | page 8 | line 861 | NUMBER | 2,326.13 | consolidated P&L, Profit before tax and share of profit in associates and joint venture (1-2), Q2FY27
R414 | page 8 | line 861 | NUMBER | 2,732.65 | consolidated P&L, Profit before tax and share of profit in associates and joint venture (1-2), Q1FY27 | OCR_CONFLICT
R415 | page 8 | line 861 | NUMBER | 1,645.36 | consolidated P&L, Profit before tax and share of profit in associates and joint venture (1-2), Q2FY26 | OCR_CONFLICT
R416 | page 8 | line 861 | NUMBER | 5,058.78 | consolidated P&L, Profit before tax and share of profit in associates and joint venture (1-2), H1FY27
R417 | page 8 | line 861 | NUMBER | 3,171.45 | consolidated P&L, Profit before tax and share of profit in associates and joint venture (1-2), H1FY26
R418 | page 8 | line 861 | NUMBER | 7,233.03 | consolidated P&L, Profit before tax and share of profit in associates and joint venture (1-2), FY26 | OCR_CONFLICT
R419 | page 8 | line 862 | NUMBER | 15.64 | consolidated P&L, Share of profit of an associate (net of tax), Q2FY27 | OCR_CONFLICT
R420 | page 8 | line 862 | NUMBER | 17.40 | consolidated P&L, Share of profit of an associate (net of tax), Q1FY27
R421 | page 8 | line 862 | NUMBER | (12.47) | consolidated P&L, Share of profit of an associate (net of tax), Q2FY26 | OCR_CONFLICT
R422 | page 8 | line 862 | NUMBER | 33.04 | consolidated P&L, Share of profit of an associate (net of tax), H1FY27
R423 | page 8 | line 862 | NUMBER | 24.53 | consolidated P&L, Share of profit of an associate (net of tax), H1FY26 | OCR_CONFLICT
R424 | page 8 | line 862 | NUMBER | (33.66) | consolidated P&L, Share of profit of an associate (net of tax), FY26
R425 | page 8 | line 863 | NUMBER | 2,341.77 | consolidated P&L, Profit before tax from continuing operation, Q2FY27 | OCR_CONFLICT
R426 | page 8 | line 863 | NUMBER | 2,750.05 | consolidated P&L, Profit before tax from continuing operation, Q1FY27
R427 | page 8 | line 863 | NUMBER | 1,632.89 | consolidated P&L, Profit before tax from continuing operation, Q2FY26 | OCR_CONFLICT
R428 | page 8 | line 863 | NUMBER | 5,091.82 | consolidated P&L, Profit before tax from continuing operation, H1FY27
R429 | page 8 | line 863 | NUMBER | 3,195.98 | consolidated P&L, Profit before tax from continuing operation, H1FY26
R430 | page 8 | line 863 | NUMBER | 7,199.37 | consolidated P&L, Profit before tax from continuing operation, FY26 | OCR_CONFLICT
R431 | page 8 | line 865 | NUMBER | 479.12 | consolidated P&L, (a) Current tax, Q2FY27
R432 | page 8 | line 865 | NUMBER | 652.90 | consolidated P&L, (a) Current tax, Q1FY27 | OCR_CONFLICT
R433 | page 8 | line 865 | NUMBER | 373.11 | consolidated P&L, (a) Current tax, Q2FY26 | OCR_CONFLICT
R434 | page 8 | line 865 | NUMBER | 1,132.02 | consolidated P&L, (a) Current tax, H1FY27
R435 | page 8 | line 865 | NUMBER | 727.65 | consolidated P&L, (a) Current tax, H1FY26
R436 | page 8 | line 865 | NUMBER | 1,619.88 | consolidated P&L, (a) Current tax, FY26 | OCR_CONFLICT
R437 | page 8 | line 866 | NUMBER | 158.72 | consolidated P&L, (b) Deferred tax, Q2FY27 | OCR_CONFLICT
R438 | page 8 | line 866 | NUMBER | 40.51 | consolidated P&L, (b) Deferred tax, Q1FY27
R439 | page 8 | line 866 | NUMBER | 83.10 | consolidated P&L, (b) Deferred tax, Q2FY26 | OCR_CONFLICT
R440 | page 8 | line 866 | NUMBER | 199.23 | consolidated P&L, (b) Deferred tax, H1FY27 | OCR_CONFLICT
R441 | page 8 | line 866 | NUMBER | 104.40 | consolidated P&L, (b) Deferred tax, H1FY26 | OCR_CONFLICT
R442 | page 8 | line 866 | NUMBER | 281.60 | consolidated P&L, (b) Deferred tax, FY26
R443 | page 8 | line 867 | NUMBER | - | consolidated P&L, (c) Tax pertain to earlier years, Q2FY27 | ZERO_STANDING
R444 | page 8 | line 867 | NUMBER | - | consolidated P&L, (c) Tax pertain to earlier years, Q1FY27 | ZERO_STANDING
R445 | page 8 | line 867 | NUMBER | - | consolidated P&L, (c) Tax pertain to earlier years, Q2FY26 | ZERO_STANDING
R446 | page 8 | line 867 | NUMBER | - | consolidated P&L, (c) Tax pertain to earlier years, H1FY27 | ZERO_STANDING
R447 | page 8 | line 867 | NUMBER | 13.16 | consolidated P&L, (c) Tax pertain to earlier years, H1FY26
R448 | page 8 | line 867 | NUMBER | 13.16 | consolidated P&L, (c) Tax pertain to earlier years, FY26
R449 | page 8 | line 867 | NUMBER | 637.84 | consolidated P&L, Total tax expenses, Q2FY27 | OCR_CONFLICT|OCR_ROW_MISSING(no label or digit match in OCR; anchored to preceding OCR line)
R450 | page 8 | line 867 | NUMBER | 693.41 | consolidated P&L, Total tax expenses, Q1FY27 | OCR_CONFLICT|OCR_ROW_MISSING(no label or digit match in OCR; anchored to preceding OCR line)
R451 | page 8 | line 867 | NUMBER | 456.21 | consolidated P&L, Total tax expenses, Q2FY26 | OCR_CONFLICT|OCR_ROW_MISSING(no label or digit match in OCR; anchored to preceding OCR line)
R452 | page 8 | line 867 | NUMBER | 1,331.25 | consolidated P&L, Total tax expenses, H1FY27 | OCR_CONFLICT|OCR_ROW_MISSING(no label or digit match in OCR; anchored to preceding OCR line)
R453 | page 8 | line 867 | NUMBER | 845.21 | consolidated P&L, Total tax expenses, H1FY26 | OCR_CONFLICT|OCR_ROW_MISSING(no label or digit match in OCR; anchored to preceding OCR line)
R454 | page 8 | line 867 | NUMBER | 1,914.64 | consolidated P&L, Total tax expenses, FY26 | OCR_CONFLICT|OCR_ROW_MISSING(no label or digit match in OCR; anchored to preceding OCR line)
R455 | page 8 | line 868 | NUMBER | 18.58 | consolidated P&L, Total other comprehensive income (net of tax), Q2FY27 | OCR_CONFLICT
R456 | page 8 | line 868 | NUMBER | 16.90 | consolidated P&L, Total other comprehensive income (net of tax), Q1FY27 | OCR_CONFLICT
R457 | page 8 | line 868 | NUMBER | 55.55 | consolidated P&L, Total other comprehensive income (net of tax), Q2FY26 | OCR_CONFLICT
R458 | page 8 | line 868 | NUMBER | 35.48 | consolidated P&L, Total other comprehensive income (net of tax), H1FY27 | OCR_CONFLICT
R459 | page 8 | line 868 | NUMBER | 61.90 | consolidated P&L, Total other comprehensive income (net of tax), H1FY26 | OCR_CONFLICT
R460 | page 8 | line 868 | NUMBER | (53.20) | consolidated P&L, Total other comprehensive income (net of tax), FY26 | OCR_CONFLICT
R461 | page 8 | line 872 | NUMBER | - | consolidated P&L, OCI (a) Re-measurement gains/(losses) on defined benefits, Q2FY27 | ZERO_STANDING
R462 | page 8 | line 872 | NUMBER | - | consolidated P&L, OCI (a) Re-measurement gains/(losses) on defined benefits, Q1FY27 | ZERO_STANDING
R463 | page 8 | line 872 | NUMBER | - | consolidated P&L, OCI (a) Re-measurement gains/(losses) on defined benefits, Q2FY26 | ZERO_STANDING
R464 | page 8 | line 872 | NUMBER | - | consolidated P&L, OCI (a) Re-measurement gains/(losses) on defined benefits, H1FY27 | ZERO_STANDING
R465 | page 8 | line 872 | NUMBER | - | consolidated P&L, OCI (a) Re-measurement gains/(losses) on defined benefits, H1FY26 | ZERO_STANDING
R466 | page 8 | line 872 | NUMBER | (27.58) | consolidated P&L, OCI (a) Re-measurement gains/(losses) on defined benefits, FY26 | OCR_CONFLICT
R467 | page 8 | line 874 | NUMBER | - | consolidated P&L, OCI (b) Change in fair value of equity instrument through OCI, Q2FY27 | ZERO_STANDING
R468 | page 8 | line 874 | NUMBER | - | consolidated P&L, OCI (b) Change in fair value of equity instrument through OCI, Q1FY27 | ZERO_STANDING
R469 | page 8 | line 874 | NUMBER | - | consolidated P&L, OCI (b) Change in fair value of equity instrument through OCI, Q2FY26 | ZERO_STANDING
R470 | page 8 | line 874 | NUMBER | - | consolidated P&L, OCI (b) Change in fair value of equity instrument through OCI, H1FY27 | ZERO_STANDING
R471 | page 8 | line 874 | NUMBER | - | consolidated P&L, OCI (b) Change in fair value of equity instrument through OCI, H1FY26 | ZERO_STANDING
R472 | page 8 | line 874 | NUMBER | (220.51) | consolidated P&L, OCI (b) Change in fair value of equity instrument through OCI, FY26
R473 | page 8 | line 877 | NUMBER | - | consolidated P&L, OCI (c) Income tax relating to the above items, Q2FY27 | ZERO_STANDING
R474 | page 8 | line 877 | NUMBER | - | consolidated P&L, OCI (c) Income tax relating to the above items, Q1FY27 | ZERO_STANDING
R475 | page 8 | line 877 | NUMBER | - | consolidated P&L, OCI (c) Income tax relating to the above items, Q2FY26 | ZERO_STANDING
R476 | page 8 | line 877 | NUMBER | - | consolidated P&L, OCI (c) Income tax relating to the above items, H1FY27 | ZERO_STANDING
R477 | page 8 | line 877 | NUMBER | - | consolidated P&L, OCI (c) Income tax relating to the above items, H1FY26 | ZERO_STANDING
R478 | page 8 | line 877 | NUMBER | 38.47 | consolidated P&L, OCI (c) Income tax relating to the above items, FY26
R479 | page 8 | line 878 | NUMBER | 18.58 | consolidated P&L, Foreign currency translation reserve (net of taxes), Q2FY27 | OCR_CONFLICT
R480 | page 8 | line 878 | NUMBER | 16.90 | consolidated P&L, Foreign currency translation reserve (net of taxes), Q1FY27 | OCR_CONFLICT
R481 | page 8 | line 878 | NUMBER | 55.55 | consolidated P&L, Foreign currency translation reserve (net of taxes), Q2FY26 | OCR_CONFLICT
R482 | page 8 | line 878 | NUMBER | 35.48 | consolidated P&L, Foreign currency translation reserve (net of taxes), H1FY27
R483 | page 8 | line 878 | NUMBER | 61.90 | consolidated P&L, Foreign currency translation reserve (net of taxes), H1FY26 | OCR_CONFLICT
R484 | page 8 | line 878 | NUMBER | 156.42 | consolidated P&L, Foreign currency translation reserve (net of taxes), FY26
R485 | page 8 | line 879 | NUMBER | - | consolidated P&L, Share of associates in other comprehensive income (net of taxes), Q2FY27 | ZERO_STANDING
R486 | page 8 | line 879 | NUMBER | - | consolidated P&L, Share of associates in other comprehensive income (net of taxes), Q1FY27 | ZERO_STANDING
R487 | page 8 | line 879 | NUMBER | - | consolidated P&L, Share of associates in other comprehensive income (net of taxes), Q2FY26 | ZERO_STANDING
R488 | page 8 | line 879 | NUMBER | - | consolidated P&L, Share of associates in other comprehensive income (net of taxes), H1FY27 | ZERO_STANDING
R489 | page 8 | line 879 | NUMBER | - | consolidated P&L, Share of associates in other comprehensive income (net of taxes), H1FY26 | ZERO_STANDING
R490 | page 8 | line 879 | NUMBER | - | consolidated P&L, Share of associates in other comprehensive income (net of taxes), FY26 | ZERO_STANDING
R491 | page 8 | line 884 | NUMBER | 1,703.93 | consolidated P&L, Profit for the period/year (4-5), Q2FY27
R492 | page 8 | line 884 | NUMBER | 2,056.64 | consolidated P&L, Profit for the period/year (4-5), Q1FY27
R493 | page 8 | line 884 | NUMBER | 1,176.68 | consolidated P&L, Profit for the period/year (4-5), Q2FY26
R494 | page 8 | line 884 | NUMBER | 3,760.57 | consolidated P&L, Profit for the period/year (4-5), H1FY27
R495 | page 8 | line 884 | NUMBER | 2,350.77 | consolidated P&L, Profit for the period/year (4-5), H1FY26
R496 | page 8 | line 884 | NUMBER | 5,284.73 | consolidated P&L, Profit for the period/year (4-5), FY26 | OCR_CONFLICT
R497 | page 8 | line 884 | NUMBER | 1,703.93 | consolidated P&L, Net profit attributable to Owners of Parent Company, Q2FY27
R498 | page 8 | line 884 | NUMBER | 2,056.64 | consolidated P&L, Net profit attributable to Owners of Parent Company, Q1FY27
R499 | page 8 | line 884 | NUMBER | 1,176.68 | consolidated P&L, Net profit attributable to Owners of Parent Company, Q2FY26
R500 | page 8 | line 884 | NUMBER | 3,760.57 | consolidated P&L, Net profit attributable to Owners of Parent Company, H1FY27
R501 | page 8 | line 884 | NUMBER | 2,350.77 | consolidated P&L, Net profit attributable to Owners of Parent Company, H1FY26
R502 | page 8 | line 884 | NUMBER | 5,284.73 | consolidated P&L, Net profit attributable to Owners of Parent Company, FY26 | OCR_CONFLICT
R503 | page 8 | line 885 | NUMBER | - | consolidated P&L, Net profit attributable to Non controlling interest, Q2FY27 | ZERO_STANDING
R504 | page 8 | line 885 | NUMBER | - | consolidated P&L, Net profit attributable to Non controlling interest, Q1FY27 | ZERO_STANDING
R505 | page 8 | line 885 | NUMBER | - | consolidated P&L, Net profit attributable to Non controlling interest, Q2FY26 | ZERO_STANDING
R506 | page 8 | line 885 | NUMBER | - | consolidated P&L, Net profit attributable to Non controlling interest, H1FY27 | ZERO_STANDING
R507 | page 8 | line 885 | NUMBER | - | consolidated P&L, Net profit attributable to Non controlling interest, H1FY26 | ZERO_STANDING
R508 | page 8 | line 885 | NUMBER | - | consolidated P&L, Net profit attributable to Non controlling interest, FY26 | ZERO_STANDING
R509 | page 8 | line 886 | NUMBER | - | consolidated P&L, Total comprehensive income attributable to Non controlling interest, Q2FY27 | ZERO_STANDING
R510 | page 8 | line 886 | NUMBER | - | consolidated P&L, Total comprehensive income attributable to Non controlling interest, Q1FY27 | ZERO_STANDING
R511 | page 8 | line 886 | NUMBER | - | consolidated P&L, Total comprehensive income attributable to Non controlling interest, Q2FY26 | ZERO_STANDING
R512 | page 8 | line 886 | NUMBER | - | consolidated P&L, Total comprehensive income attributable to Non controlling interest, H1FY27 | ZERO_STANDING
R513 | page 8 | line 886 | NUMBER | - | consolidated P&L, Total comprehensive income attributable to Non controlling interest, H1FY26 | ZERO_STANDING
R514 | page 8 | line 886 | NUMBER | - | consolidated P&L, Total comprehensive income attributable to Non controlling interest, FY26 | ZERO_STANDING
R515 | page 8 | line 887 | NUMBER | 1,722.51 | consolidated P&L, Total comprehensive income for the period/year (net of tax) (6+7), Q2FY27 | OCR_CONFLICT
R516 | page 8 | line 887 | NUMBER | 2,073.54 | consolidated P&L, Total comprehensive income for the period/year (net of tax) (6+7), Q1FY27
R517 | page 8 | line 887 | NUMBER | 1,232.23 | consolidated P&L, Total comprehensive income for the period/year (net of tax) (6+7), Q2FY26
R518 | page 8 | line 887 | NUMBER | 3,796.05 | consolidated P&L, Total comprehensive income for the period/year (net of tax) (6+7), H1FY27
R519 | page 8 | line 887 | NUMBER | 2,412.67 | consolidated P&L, Total comprehensive income for the period/year (net of tax) (6+7), H1FY26
R520 | page 8 | line 887 | NUMBER | 5,231.53 | consolidated P&L, Total comprehensive income for the period/year (net of tax) (6+7), FY26 | OCR_CONFLICT
R521 | page 8 | line 887 | NUMBER | 1,722.51 | consolidated P&L, Total comprehensive income attributable to Owners of Parent Company, Q2FY27 | OCR_CONFLICT
R522 | page 8 | line 887 | NUMBER | 2,073.54 | consolidated P&L, Total comprehensive income attributable to Owners of Parent Company, Q1FY27
R523 | page 8 | line 887 | NUMBER | 1,232.23 | consolidated P&L, Total comprehensive income attributable to Owners of Parent Company, Q2FY26
R524 | page 8 | line 887 | NUMBER | 3,796.05 | consolidated P&L, Total comprehensive income attributable to Owners of Parent Company, H1FY27
R525 | page 8 | line 887 | NUMBER | 2,412.67 | consolidated P&L, Total comprehensive income attributable to Owners of Parent Company, H1FY26
R526 | page 8 | line 887 | NUMBER | 5,231.53 | consolidated P&L, Total comprehensive income attributable to Owners of Parent Company, FY26 | OCR_CONFLICT
R527 | page 8 | line 889 | NUMBER | Rs. 10/- | face value per equity share (consolidated P&L)
R528 | page 8 | line 889 | NUMBER | 1801.58 | consolidated P&L, Paid up equity share capital (Face value Rs. 10/- each), Q2FY27
R529 | page 8 | line 889 | NUMBER | 1801.58 | consolidated P&L, Paid up equity share capital (Face value Rs. 10/- each), Q1FY27
R530 | page 8 | line 889 | NUMBER | 1801.58 | consolidated P&L, Paid up equity share capital (Face value Rs. 10/- each), Q2FY26
R531 | page 8 | line 889 | NUMBER | 1801.58 | consolidated P&L, Paid up equity share capital (Face value Rs. 10/- each), H1FY27
R532 | page 8 | line 889 | NUMBER | 1801.58 | consolidated P&L, Paid up equity share capital (Face value Rs. 10/- each), H1FY26
R533 | page 8 | line 889 | NUMBER | 1801.58 | consolidated P&L, Paid up equity share capital (Face value Rs. 10/- each), FY26
R534 | page 8 | line 890 | NUMBER | - | consolidated P&L, Other equity, Q2FY27 | ZERO_STANDING
R535 | page 8 | line 890 | NUMBER | - | consolidated P&L, Other equity, Q1FY27 | ZERO_STANDING
R536 | page 8 | line 890 | NUMBER | - | consolidated P&L, Other equity, Q2FY26 | ZERO_STANDING
R537 | page 8 | line 890 | NUMBER | - | consolidated P&L, Other equity, H1FY27 | ZERO_STANDING
R538 | page 8 | line 890 | NUMBER | - | consolidated P&L, Other equity, H1FY26 | ZERO_STANDING
R539 | page 8 | line 890 | NUMBER | 28236.02 | consolidated P&L, Other equity, FY26 | OCR_CONFLICT
R540 | page 8 | line 893 | NUMBER | 9.46 | consolidated P&L, Basic earning per share (Rs.), Q2FY27
R541 | page 8 | line 893 | NUMBER | 11.42 | consolidated P&L, Basic earning per share (Rs.), Q1FY27
R542 | page 8 | line 893 | NUMBER | 6.87 | consolidated P&L, Basic earning per share (Rs.), Q2FY26 | OCR_CONFLICT
R543 | page 8 | line 893 | NUMBER | 20.87 | consolidated P&L, Basic earning per share (Rs.), H1FY27
R544 | page 8 | line 893 | NUMBER | 13.71 | consolidated P&L, Basic earning per share (Rs.), H1FY26
R545 | page 8 | line 893 | NUMBER | 29.68 | consolidated P&L, Basic earning per share (Rs.), FY26
R546 | page 8 | line 894 | NUMBER | 9.45 | consolidated P&L, Diluted earning per share (Rs.), Q2FY27 | OCR_CONFLICT
R547 | page 8 | line 894 | NUMBER | 11.41 | consolidated P&L, Diluted earning per share (Rs.), Q1FY27 | OCR_CONFLICT
R548 | page 8 | line 894 | NUMBER | 6.86 | consolidated P&L, Diluted earning per share (Rs.), Q2FY26
R549 | page 8 | line 894 | NUMBER | 20.86 | consolidated P&L, Diluted earning per share (Rs.), H1FY27 | OCR_CONFLICT
R550 | page 8 | line 894 | NUMBER | 13.69 | consolidated P&L, Diluted earning per share (Rs.), H1FY26 | OCR_CONFLICT
R551 | page 8 | line 894 | NUMBER | 29.67 | consolidated P&L, Diluted earning per share (Rs.), FY26
R552 | page 8 | line 900 | NUMBER | DIN 00087088 (OCR read 00047088/60087088; image 00087088) | director DIN | IMAGE_READ
R553 | page 9 | line 986 | NUMBER | L51909DL1987PLC027186 | CIN
R554 | page 9 | line 991 | NUMBER | 55,983.69 | consolidated balance sheet, Total assets, 30-Sep-2026 | OCR_CONFLICT
R555 | page 9 | line 991 | NUMBER | 52,901.18 | consolidated balance sheet, Total assets, 31-Mar-2026 | OCR_CONFLICT
R556 | page 9 | line 993 | NUMBER | 28,292.31 | consolidated balance sheet, Property, plant and equipment, 30-Sep-2026
R557 | page 9 | line 993 | NUMBER | 23,530.81 | consolidated balance sheet, Property, plant and equipment, 31-Mar-2026
R558 | page 9 | line 994 | NUMBER | 3,260.99 | consolidated balance sheet, Capital work in progress, 30-Sep-2026
R559 | page 9 | line 994 | NUMBER | 4,171.77 | consolidated balance sheet, Capital work in progress, 31-Mar-2026
R560 | page 9 | line 995 | NUMBER | 530.39 | consolidated balance sheet, Investment property, 30-Sep-2026 | OCR_CONFLICT
R561 | page 9 | line 995 | NUMBER | 530.39 | consolidated balance sheet, Investment property, 31-Mar-2026 | OCR_CONFLICT
R562 | page 9 | line 996 | NUMBER | 1,003.21 | consolidated balance sheet, Right of use assets, 30-Sep-2026 | OCR_CONFLICT
R563 | page 9 | line 996 | NUMBER | 833.96 | consolidated balance sheet, Right of use assets, 31-Mar-2026 | OCR_CONFLICT
R564 | page 9 | line 997 | NUMBER | 6.79 | consolidated balance sheet, Other intangible assets, 30-Sep-2026
R565 | page 9 | line 997 | NUMBER | 7.34 | consolidated balance sheet, Other intangible assets, 31-Mar-2026 | OCR_CONFLICT
R566 | page 9 | line 999 | NUMBER | 1,422.01 | consolidated balance sheet, i) Investment in associate and Joint Venture, 30-Sep-2026
R567 | page 9 | line 999 | NUMBER | 1,388.97 | consolidated balance sheet, i) Investment in associate and Joint Venture, 31-Mar-2026
R568 | page 9 | line 1000 | NUMBER | 2,016.46 | consolidated balance sheet, ii) Investments, 30-Sep-2026
R569 | page 9 | line 1000 | NUMBER | 2,014.46 | consolidated balance sheet, ii) Investments, 31-Mar-2026
R570 | page 9 | line 1001 | NUMBER | 95.27 | consolidated balance sheet, iii) Loans (non-current), 30-Sep-2026
R571 | page 9 | line 1001 | NUMBER | - | consolidated balance sheet, iii) Loans (non-current), 31-Mar-2026 | ZERO_STANDING
R572 | page 9 | line 1002 | NUMBER | 471.20 | consolidated balance sheet, iv) Other financial assets (non-current), 30-Sep-2026 | OCR_CONFLICT
R573 | page 9 | line 1002 | NUMBER | 375.12 | consolidated balance sheet, iv) Other financial assets (non-current), 31-Mar-2026 | OCR_CONFLICT
R574 | page 9 | line 1003 | NUMBER | 927.52 | consolidated balance sheet, Other non-current assets, 30-Sep-2026
R575 | page 9 | line 1003 | NUMBER | 1,204.99 | consolidated balance sheet, Other non-current assets, 31-Mar-2026 | OCR_CONFLICT
R576 | page 9 | line 1005 | NUMBER | 17,957.54 | consolidated balance sheet, Total current assets, 30-Sep-2026 | OCR_CONFLICT
R577 | page 9 | line 1005 | NUMBER | 18,843.37 | consolidated balance sheet, Total current assets, 31-Mar-2026 | OCR_CONFLICT
R578 | page 9 | line 1006 | NUMBER | 8,392.56 | consolidated balance sheet, Inventories, 30-Sep-2026
R579 | page 9 | line 1006 | NUMBER | 7,639.96 | consolidated balance sheet, Inventories, 31-Mar-2026
R580 | page 9 | line 1008 | NUMBER | 5,660.36 | consolidated balance sheet, i) Trade receivables, 30-Sep-2026 | OCR_CONFLICT
R581 | page 9 | line 1008 | NUMBER | 6,695.73 | consolidated balance sheet, i) Trade receivables, 31-Mar-2026
R582 | page 9 | line 1009 | NUMBER | 128.59 | consolidated balance sheet, ii) Cash and cash equivalents, 30-Sep-2026
R583 | page 9 | line 1009 | NUMBER | 106.86 | consolidated balance sheet, ii) Cash and cash equivalents, 31-Mar-2026
R584 | page 9 | line 1010 | NUMBER | 325.38 | consolidated balance sheet, iii) Bank balances other than (ii) above, 30-Sep-2026 | OCR_CONFLICT
R585 | page 9 | line 1010 | NUMBER | 271.45 | consolidated balance sheet, iii) Bank balances other than (ii) above, 31-Mar-2026
R586 | page 9 | line 1011 | NUMBER | 42.30 | consolidated balance sheet, iv) Loans (current), 30-Sep-2026 | OCR_CONFLICT
R587 | page 9 | line 1011 | NUMBER | 37.01 | consolidated balance sheet, iv) Loans (current), 31-Mar-2026
R588 | page 9 | line 1012 | NUMBER | 412.28 | consolidated balance sheet, v) Others financial assets (current), 30-Sep-2026
R589 | page 9 | line 1012 | NUMBER | 306.42 | consolidated balance sheet, v) Others financial assets (current), 31-Mar-2026
R590 | page 9 | line 1013 | NUMBER | 38,026.15 | consolidated balance sheet, Total non-current assets, 30-Sep-2026 | OCR_CONFLICT
R591 | page 9 | line 1013 | NUMBER | 34,057.81 | consolidated balance sheet, Total non-current assets, 31-Mar-2026 | OCR_CONFLICT
R592 | page 9 | line 1013 | NUMBER | 2,996.07 | consolidated balance sheet, Other current assets, 30-Sep-2026
R593 | page 9 | line 1013 | NUMBER | 3,785.94 | consolidated balance sheet, Other current assets, 31-Mar-2026
R594 | page 9 | line 1015 | NUMBER | 55,983.69 | consolidated balance sheet, Total equity and liabilities, 30-Sep-2026 | OCR_CONFLICT
R595 | page 9 | line 1015 | NUMBER | 52,901.18 | consolidated balance sheet, Total equity and liabilities, 31-Mar-2026 | OCR_CONFLICT
R596 | page 9 | line 1017 | NUMBER | 1,801.58 | consolidated balance sheet, Equity share capital, 30-Sep-2026
R597 | page 9 | line 1017 | NUMBER | 1,801.58 | consolidated balance sheet, Equity share capital, 31-Mar-2026
R598 | page 9 | line 1018 | NUMBER | 31,483.76 | consolidated balance sheet, Other equity, 30-Sep-2026 | OCR_CONFLICT
R599 | page 9 | line 1018 | NUMBER | 28,236.02 | consolidated balance sheet, Other equity, 31-Mar-2026 | OCR_CONFLICT
R600 | page 9 | line 1019 | NUMBER | 33,285.34 | consolidated balance sheet, Total equity, 30-Sep-2026 | OCR_CONFLICT
R601 | page 9 | line 1019 | NUMBER | 30,037.60 | consolidated balance sheet, Total equity, 31-Mar-2026 | OCR_CONFLICT
R602 | page 9 | line 1021 | NUMBER | 6,994.47 | consolidated balance sheet, Total non-current liabilities, 30-Sep-2026 | OCR_CONFLICT
R603 | page 9 | line 1021 | NUMBER | 5,966.42 | consolidated balance sheet, Total non-current liabilities, 31-Mar-2026 | OCR_CONFLICT
R604 | page 9 | line 1023 | NUMBER | 4,445.16 | consolidated balance sheet, Non-current i) Borrowings, 30-Sep-2026
R605 | page 9 | line 1023 | NUMBER | 3,823.67 | consolidated balance sheet, Non-current i) Borrowings, 31-Mar-2026
R606 | page 9 | line 1024 | NUMBER | 924.42 | consolidated balance sheet, Non-current ii) Lease liabilities, 30-Sep-2026
R607 | page 9 | line 1024 | NUMBER | 775.44 | consolidated balance sheet, Non-current ii) Lease liabilities, 31-Mar-2026 | OCR_CONFLICT
R608 | page 9 | line 1025 | NUMBER | 564.37 | consolidated balance sheet, Non-current Provisions, 30-Sep-2026
R609 | page 9 | line 1025 | NUMBER | 508.36 | consolidated balance sheet, Non-current Provisions, 31-Mar-2026
R610 | page 9 | line 1026 | NUMBER | 1,058.51 | consolidated balance sheet, Deferred tax liabilities (net), 30-Sep-2026
R611 | page 9 | line 1026 | NUMBER | 857.07 | consolidated balance sheet, Deferred tax liabilities (net), 31-Mar-2026 | OCR_CONFLICT
R612 | page 9 | line 1027 | NUMBER | 2.01 | consolidated balance sheet, Other non-current liabilities, 30-Sep-2026
R613 | page 9 | line 1027 | NUMBER | 1.88 | consolidated balance sheet, Other non-current liabilities, 31-Mar-2026 | OCR_CONFLICT
R614 | page 9 | line 1029 | NUMBER | 15,703.88 | consolidated balance sheet, Total current liabilities, 30-Sep-2026 | OCR_CONFLICT
R615 | page 9 | line 1029 | NUMBER | 16,897.16 | consolidated balance sheet, Total current liabilities, 31-Mar-2026 | OCR_CONFLICT
R616 | page 9 | line 1031 | NUMBER | 6,697.20 | consolidated balance sheet, Current i) Borrowings, 30-Sep-2026
R617 | page 9 | line 1031 | NUMBER | 8,239.02 | consolidated balance sheet, Current i) Borrowings, 31-Mar-2026 | OCR_CONFLICT
R618 | page 9 | line 1032 | NUMBER | 123.80 | consolidated balance sheet, Current ii) Lease liabilities, 30-Sep-2026
R619 | page 9 | line 1032 | NUMBER | 73.53 | consolidated balance sheet, Current ii) Lease liabilities, 31-Mar-2026
R620 | page 9 | line 1034 | NUMBER | 832.14 | consolidated balance sheet, iii)(a) Trade payables, dues of micro enterprises and small enterprises, 30-Sep-2026
R621 | page 9 | line 1034 | NUMBER | 903.00 | consolidated balance sheet, iii)(a) Trade payables, dues of micro enterprises and small enterprises, 31-Mar-2026 | OCR_CONFLICT
R622 | page 9 | line 1037 | NUMBER | 5,381.42 | consolidated balance sheet, iii)(b) Trade payables, dues of creditors other than micro and small enterprises, 30-Sep-2026
R623 | page 9 | line 1037 | NUMBER | 5,246.82 | consolidated balance sheet, iii)(b) Trade payables, dues of creditors other than micro and small enterprises, 31-Mar-2026
R624 | page 9 | line 1038 | NUMBER | 1,010.51 | consolidated balance sheet, iv) Other financial liabilities, 30-Sep-2026
R625 | page 9 | line 1038 | NUMBER | 744.67 | consolidated balance sheet, iv) Other financial liabilities, 31-Mar-2026 | OCR_CONFLICT
R626 | page 9 | line 1039 | NUMBER | 958.14 | consolidated balance sheet, Other current liabilities, 30-Sep-2026
R627 | page 9 | line 1039 | NUMBER | 915.86 | consolidated balance sheet, Other current liabilities, 31-Mar-2026
R628 | page 9 | line 1040 | NUMBER | 196.20 | consolidated balance sheet, Current Provisions, 30-Sep-2026
R629 | page 9 | line 1040 | NUMBER | 168.39 | consolidated balance sheet, Current Provisions, 31-Mar-2026
R630 | page 9 | line 1041 | NUMBER | 504.47 | consolidated balance sheet, Current tax liabilities (net), 30-Sep-2026
R631 | page 9 | line 1041 | NUMBER | 605.87 | consolidated balance sheet, Current tax liabilities (net), 31-Mar-2026
R632 | page 9 | line 1049 | NUMBER | DIN 00087088 | director DIN
R633 | page 10 | line 1136 | NUMBER | 7,893.43 | consolidated cash flow, Cash generated from operations, H1FY27 | OCR_CONFLICT
R634 | page 10 | line 1136 | NUMBER | 326.60 | consolidated cash flow, Cash generated from operations, H1FY26 | OCR_CONFLICT
R635 | page 10 | line 1136 | NUMBER | (1,233.42) | consolidated cash flow, Income tax paid (net of refunds), H1FY27 | OCR_CONFLICT|OCR_ROW_MISSING(no label or digit match in OCR; anchored to preceding OCR line)
R636 | page 10 | line 1136 | NUMBER | (597.51) | consolidated cash flow, Income tax paid (net of refunds), H1FY26 | OCR_CONFLICT|OCR_ROW_MISSING(no label or digit match in OCR; anchored to preceding OCR line)
R637 | page 10 | line 1137 | NUMBER | 5,091.82 | consolidated cash flow, Net profit before tax, H1FY27
R638 | page 10 | line 1137 | NUMBER | 3,195.98 | consolidated cash flow, Net profit before tax, H1FY26 | OCR_CONFLICT
R639 | page 10 | line 1139 | NUMBER | 859.09 | consolidated cash flow, Depreciation and amortisation expense, H1FY27 | OCR_CONFLICT
R640 | page 10 | line 1139 | NUMBER | 581.95 | consolidated cash flow, Depreciation and amortisation expense, H1FY26 | OCR_CONFLICT
R641 | page 10 | line 1140 | NUMBER | 0.02 | consolidated cash flow, Loss/(gain) on disposal of PPE, H1FY27
R642 | page 10 | line 1140 | NUMBER | (0.45) | consolidated cash flow, Loss/(gain) on disposal of PPE, H1FY26 | OCR_CONFLICT
R643 | page 10 | line 1141 | NUMBER | (27.00) | consolidated cash flow, Rental income (adjustment), H1FY27 | OCR_CONFLICT
R644 | page 10 | line 1141 | NUMBER | (18.00) | consolidated cash flow, Rental income (adjustment), H1FY26
R645 | page 10 | line 1141 | NUMBER | 27.00 | consolidated cash flow, Rental income (investing), H1FY27 | OCR_CONFLICT
R646 | page 10 | line 1141 | NUMBER | 18.00 | consolidated cash flow, Rental income (investing), H1FY26
R647 | page 10 | line 1142 | NUMBER | 24.13 | consolidated cash flow, Provision for expected credit loss, H1FY27 | OCR_CONFLICT
R648 | page 10 | line 1142 | NUMBER | 21.06 | consolidated cash flow, Provision for expected credit loss, H1FY26 | OCR_CONFLICT
R649 | page 10 | line 1143 | NUMBER | 24.34 | consolidated cash flow, Expenses on employees stock options scheme, H1FY27 | OCR_CONFLICT
R650 | page 10 | line 1143 | NUMBER | 45.45 | consolidated cash flow, Expenses on employees stock options scheme, H1FY26 | OCR_CONFLICT
R651 | page 10 | line 1144 | NUMBER | (46.83) | consolidated cash flow, Excess provisions written back, H1FY27
R652 | page 10 | line 1144 | NUMBER | 1.70 | consolidated cash flow, Excess provisions written back, H1FY26
R653 | page 10 | line 1145 | NUMBER | 552.70 | consolidated cash flow, Finance cost, H1FY27 | OCR_CONFLICT
R654 | page 10 | line 1145 | NUMBER | 541.59 | consolidated cash flow, Finance cost, H1FY26
R655 | page 10 | line 1146 | NUMBER | 7.57 | consolidated cash flow, Unrealised foreign exchange gain, H1FY27
R656 | page 10 | line 1146 | NUMBER | (12.93) | consolidated cash flow, Unrealised foreign exchange gain, H1FY26
R657 | page 10 | line 1147 | NUMBER | (45.76) | consolidated cash flow, Finance income, H1FY27
R658 | page 10 | line 1147 | NUMBER | (48.73) | consolidated cash flow, Finance income, H1FY26
R659 | page 10 | line 1148 | NUMBER | (33.04) | consolidated cash flow, Share of profit/(loss) of an associate and joint venture (net of tax), H1FY27
R660 | page 10 | line 1148 | NUMBER | 24.53 | consolidated cash flow, Share of profit/(loss) of an associate and joint venture (net of tax), H1FY26
R661 | page 10 | line 1149 | NUMBER | 35.48 | consolidated cash flow, Foreign currency translation reserve, H1FY27 | OCR_CONFLICT
R662 | page 10 | line 1149 | NUMBER | 61.90 | consolidated cash flow, Foreign currency translation reserve, H1FY26 | OCR_CONFLICT
R663 | page 10 | line 1149 | NUMBER | 6,442.52 | consolidated cash flow, Operating profit before working capital changes, H1FY27 | OCR_CONFLICT|OCR_ROW_MISSING(no label or digit match in OCR; anchored to preceding OCR line)
R664 | page 10 | line 1149 | NUMBER | 4,394.05 | consolidated cash flow, Operating profit before working capital changes, H1FY26 | OCR_CONFLICT|OCR_ROW_MISSING(no label or digit match in OCR; anchored to preceding OCR line)
R665 | page 10 | line 1152 | NUMBER | (752.61) | consolidated cash flow, (Increase)/decrease in inventories, H1FY27 | OCR_CONFLICT
R666 | page 10 | line 1152 | NUMBER | (1,299.50) | consolidated cash flow, (Increase)/decrease in inventories, H1FY26
R667 | page 10 | line 1153 | NUMBER | 1,011.24 | consolidated cash flow, (Increase)/decrease in trade receivables, H1FY27
R668 | page 10 | line 1153 | NUMBER | (1,030.43) | consolidated cash flow, (Increase)/decrease in trade receivables, H1FY26
R669 | page 10 | line 1154 | NUMBER | (188.92) | consolidated cash flow, (Increase)/decrease in other financial assets, H1FY27
R670 | page 10 | line 1154 | NUMBER | (96.04) | consolidated cash flow, (Increase)/decrease in other financial assets, H1FY26
R671 | page 10 | line 1155 | NUMBER | 797.43 | consolidated cash flow, (Increase)/decrease in other assets, H1FY27 | OCR_CONFLICT
R672 | page 10 | line 1155 | NUMBER | (2,232.37) | consolidated cash flow, (Increase)/decrease in other assets, H1FY26
R673 | page 10 | line 1156 | NUMBER | 103.02 | consolidated cash flow, Increase/(decrease) in trade payables, H1FY27 | OCR_CONFLICT
R674 | page 10 | line 1156 | NUMBER | 504.78 | consolidated cash flow, Increase/(decrease) in trade payables, H1FY26
R675 | page 10 | line 1157 | NUMBER | 354.52 | consolidated cash flow, Increase/(decrease) in other financial liabilities, H1FY27 | OCR_CONFLICT
R676 | page 10 | line 1157 | NUMBER | (103.94) | consolidated cash flow, Increase/(decrease) in other financial liabilities, H1FY26
R677 | page 10 | line 1158 | NUMBER | 42.41 | consolidated cash flow, Increase/(decrease) in other liabilities, H1FY27
R678 | page 10 | line 1158 | NUMBER | 99.18 | consolidated cash flow, Increase/(decrease) in other liabilities, H1FY26
R679 | page 10 | line 1159 | NUMBER | 83.82 | consolidated cash flow, Increase/(decrease) in provisions, H1FY27
R680 | page 10 | line 1159 | NUMBER | 90.87 | consolidated cash flow, Increase/(decrease) in provisions, H1FY26
R681 | page 10 | line 1161 | NUMBER | 6,660.01 | consolidated cash flow, Net cash flow generated from operating activities (A), H1FY27 | OCR_CONFLICT
R682 | page 10 | line 1161 | NUMBER | (270.91) | consolidated cash flow, Net cash flow generated from operating activities (A), H1FY26 | OCR_CONFLICT
R683 | page 10 | line 1162 | NUMBER | (4,528.70) | consolidated cash flow, Purchase of property plant & equipment (net of capital advances and capital payables), H1FY27
R684 | page 10 | line 1162 | NUMBER | (2,904.01) | consolidated cash flow, Purchase of property plant & equipment (net of capital advances and capital payables), H1FY26
R685 | page 10 | line 1164 | NUMBER | 59.60 | consolidated cash flow, Proceeds from sale of property, plant and equipment, H1FY27
R686 | page 10 | line 1164 | NUMBER | 42.79 | consolidated cash flow, Proceeds from sale of property, plant and equipment, H1FY26
R687 | page 10 | line 1166 | NUMBER | (100.56) | consolidated cash flow, Loan given & received back, H1FY27
R688 | page 10 | line 1166 | NUMBER | (9.04) | consolidated cash flow, Loan given & received back, H1FY26
R689 | page 10 | line 1167 | NUMBER | - | consolidated cash flow, Investment in associate and joint venture, H1FY27 | ZERO_STANDING
R690 | page 10 | line 1167 | NUMBER | (181.47) | consolidated cash flow, Investment in associate and joint venture, H1FY26
R691 | page 10 | line 1168 | NUMBER | - | consolidated cash flow, Proceeds from sale of investment, H1FY27 | ZERO_STANDING
R692 | page 10 | line 1168 | NUMBER | 464.63 | consolidated cash flow, Proceeds from sale of investment, H1FY26
R693 | page 10 | line 1169 | NUMBER | 44.53 | consolidated cash flow, Interest received, H1FY27
R694 | page 10 | line 1169 | NUMBER | 48.73 | consolidated cash flow, Interest received, H1FY26
R695 | page 10 | line 1170 | NUMBER | (20.15) | consolidated cash flow, (Investing in)/redemption of term deposit, H1FY27
R696 | page 10 | line 1170 | NUMBER | 64.47 | consolidated cash flow, (Investing in)/redemption of term deposit, H1FY26
R697 | page 10 | line 1173 | NUMBER | (4,518.28) | consolidated cash flow, Net cash flow (used) in investing activities (B), H1FY27 | OCR_CONFLICT
R698 | page 10 | line 1173 | NUMBER | (2,455.90) | consolidated cash flow, Net cash flow (used) in investing activities (B), H1FY26 | OCR_CONFLICT
R699 | page 10 | line 1174 | NUMBER | - | consolidated cash flow, Proceed from issue of equity shares, H1FY27 | ZERO_STANDING
R700 | page 10 | line 1174 | NUMBER | 7,620.30 | consolidated cash flow, Proceed from issue of equity shares, H1FY26
R701 | page 10 | line 1175 | NUMBER | 1,503.21 | consolidated cash flow, Proceeds of long term borrowings, H1FY27
R702 | page 10 | line 1175 | NUMBER | 110.89 | consolidated cash flow, Proceeds of long term borrowings, H1FY26 | OCR_CONFLICT
R703 | page 10 | line 1176 | NUMBER | (805.07) | consolidated cash flow, Repayments from long term borrowings, H1FY27
R704 | page 10 | line 1176 | NUMBER | (2,426.26) | consolidated cash flow, Repayments from long term borrowings, H1FY26
R705 | page 10 | line 1177 | NUMBER | (1,618.48) | consolidated cash flow, Proceeds/(repayment) of short term borrowings, H1FY27 | OCR_CONFLICT
R706 | page 10 | line 1177 | NUMBER | (708.52) | consolidated cash flow, Proceeds/(repayment) of short term borrowings, H1FY26
R707 | page 10 | line 1178 | NUMBER | (54.02) | consolidated cash flow, Payment of principal portion of lease liabilities, H1FY27
R708 | page 10 | line 1178 | NUMBER | (16.34) | consolidated cash flow, Payment of principal portion of lease liabilities, H1FY26 | OCR_CONFLICT
R709 | page 10 | line 1179 | NUMBER | (50.71) | consolidated cash flow, Payment of interest on lease liabilities, H1FY27
R710 | page 10 | line 1179 | NUMBER | (2.89) | consolidated cash flow, Payment of interest on lease liabilities, H1FY26
R711 | page 10 | line 1180 | NUMBER | (585.52) | consolidated cash flow, Dividend paid, H1FY27 | OCR_CONFLICT
R712 | page 10 | line 1180 | NUMBER | (692.70) | consolidated cash flow, Dividend paid, H1FY26 | OCR_CONFLICT
R713 | page 10 | line 1181 | NUMBER | (509.41) | consolidated cash flow, Interest paid, H1FY27
R714 | page 10 | line 1181 | NUMBER | (541.02) | consolidated cash flow, Interest paid, H1FY26
R715 | page 10 | line 1181 | NUMBER | (2,120.00) | consolidated cash flow, Net cash flow from/(used) in financing activities (C), H1FY27 | OCR_CONFLICT|OCR_ROW_MISSING(no label or digit match in OCR; anchored to preceding OCR line)
R716 | page 10 | line 1181 | NUMBER | 3,343.46 | consolidated cash flow, Net cash flow from/(used) in financing activities (C), H1FY26 | OCR_CONFLICT|OCR_ROW_MISSING(no label or digit match in OCR; anchored to preceding OCR line)
R717 | page 10 | line 1184 | NUMBER | 21.73 | consolidated cash flow, Net increase/(decrease) in cash and cash equivalents (A+B+C), H1FY27 | OCR_CONFLICT
R718 | page 10 | line 1184 | NUMBER | 616.65 | consolidated cash flow, Net increase/(decrease) in cash and cash equivalents (A+B+C), H1FY26 | OCR_CONFLICT
R719 | page 10 | line 1185 | NUMBER | 106.86 | consolidated cash flow, Cash and cash equivalents at the beginning of the period, H1FY27 | OCR_CONFLICT
R720 | page 10 | line 1185 | NUMBER | 211.08 | consolidated cash flow, Cash and cash equivalents at the beginning of the period, H1FY26 | OCR_CONFLICT
R721 | page 10 | line 1185 | NUMBER | 128.59 | consolidated cash flow, Cash and cash equivalents at the end of the period, H1FY27 | OCR_CONFLICT|OCR_ROW_MISSING(no label or digit match in OCR; anchored to preceding OCR line)
R722 | page 10 | line 1185 | NUMBER | 827.73 | consolidated cash flow, Cash and cash equivalents at the end of the period, H1FY26 | OCR_CONFLICT|OCR_ROW_MISSING(no label or digit match in OCR; anchored to preceding OCR line)
R723 | page 10 | line 1191 | NUMBER | DIN 00087088 (OCR read 60087088; image 00087088) | director DIN | IMAGE_READ
R724 | page 11 | line 1212 | NUMBER | Chilean Pesos 500,000,000 | Chile SpA authorised capital
R725 | page 11 | line 1212 | NUMBER | 5,00,00,000 equity shares | Chile SpA authorised share count
R726 | page 11 | line 1212 | NUMBER | Chilean Pesos 10 | Chile SpA face value per share
R727 | page 11 | line 1217 | NUMBER | 34 kanals and 8 marlas | Panipat land area
R728 | page 11 | line 1220 | NUMBER | 20 kanals and 12 marlas | land released from acquisition
R729 | page 11 | line 1223 | NUMBER | Rs 373.27 lakhs | HSIIDC demand for allotment of land
R730 | page 13 | line 1365 | NUMBER | 2 subsidiaries | count of unreviewed subsidiaries
R731 | page 13 | line 1366 | NUMBER | Rs. 3195.77 lakhs | unreviewed subsidiaries total assets at 30 Sep 2026
R732 | page 13 | line 1366 | NUMBER | Rs. 1,123.67 lakhs | unreviewed subsidiaries total revenues, quarter ended 30 Sep 2026
R733 | page 13 | line 1367 | NUMBER | Rs. 93.35 lakhs | unreviewed subsidiaries net profit after tax, quarter
R734 | page 13 | line 1367 | NUMBER | Rs. 115.91 lakhs | unreviewed subsidiaries net profit after tax, six months
R735 | page 13 | line 1367 | NUMBER | Rs. 93.35 lakhs | unreviewed subsidiaries total comprehensive income, quarter
R736 | page 13 | line 1368 | NUMBER | Rs. 115.91 lakhs | unreviewed subsidiaries total comprehensive income, six months
R737 | page 13 | line 1368 | NUMBER | Rs. 17.72 lakhs | unreviewed subsidiaries net cash inflows, period ended 30 Sep 2026
R738 | page 13 | line 1370 | NUMBER | Rs. (24.98) lakhs | Group share of net loss after tax, JV, quarter
R739 | page 13 | line 1370 | NUMBER | Rs. (72.20) lakhs | Group share of net loss after tax, JV, six months
R740 | page 13 | line 1370 | NUMBER | Rs. (24.98) lakhs | Group share of OCI loss, JV, quarter
R741 | page 13 | line 1370 | NUMBER | Rs. (72.20) lakhs | Group share of OCI loss, JV, six months
R742 | page 13 | line 1372 | NUMBER | 1 joint venture | count of JV unreviewed
R743 | page 13 | line 1384 | NUMBER | 512497 | partner membership no.
R744 | page 13 | line 1387 | NUMBER | UDIN 26512497NOVQVW2239 | UDIN consolidated
R745 | page 13 | line 1403 | NUMBER | Rs. 1,995.11 lakhs | unreviewed subsidiaries total revenues, six months (OCR layer; embedded reads 1,995 .11) | OCR_CORRECTED

## ENTITY
R746 | page 1 | line 23 | ENTITY | BSE Limited | exchange addressee
R747 | page 1 | line 25 | ENTITY | National Stock Exchange of India Ltd | exchange addressee
R748 | page 1 | line 29 | ENTITY | BSE Scrip 530475 | scrip code
R749 | page 1 | line 29 | ENTITY | NSE Symbol TINNARUBR | symbol
R750 | page 1 | line 31 | ENTITY | ISIN INE015C01016 | ISIN
R751 | page 1 | line 34 | ENTITY | Tinna Rubber and Infrastructure Limited | company
R752 | page 1 | line 38 | ENTITY | SEBI LODR Regulations 2015, Reg 30 and 33 | regulation
R753 | page 1 | line 43 | ENTITY | Statutory Auditors | limited review
R754 | page 1 | line 44 | ENTITY | Audit Committee | recommended results
R755 | page 1 | line 66 | ENTITY | Sanjay Kumar Rawat, Company Secretary | signatory
R756 | page 1 | line 77 | ENTITY | Tinna Rubber And Infrastructure Limited, Regd. Office Tinna House, No-6, Sultanpur, Mandi Road, Mehrauli, New Delhi-110030 (INDIA) | registered office (letterhead) | OCR_ONLY
R757 | page 1 | line 80 | ENTITY | FOR STRONG ROADS | company tagline (letterhead) | OCR_ONLY
R758 | page 1 | line 81 | ENTITY | tinna.delhi@tinna.in | company email (letterhead) | OCR_ONLY
R759 | page 1 | line 82 | ENTITY | www.tinna.in | company website (letterhead) | OCR_ONLY
R760 | page 2 | line 232 | ENTITY | Tinna Rubber and Infrastructure Limited, Tinna House No.6, Sultanpur, Mandi Road, Mehrauli, New Delhi-110030 | registered office
R761 | page 2 | line 234 | ENTITY | CIN L51909DL1987PLC027186 | CIN
R762 | page 2 | line 279 | ENTITY | FOR TINNA RUBBER AND INFRASTRUCTURE LIMITED (company seal) | signature block
R763 | page 2 | line 280 | ENTITY | Bhupinder Kumar Sekhri, Managing Director (name partly illegible in text layers; read from image) | signatory director | IMAGE_READ
R764 | page 2 | line 280 | ENTITY | S S Kothari Mehta & Co. LLP, Chartered Accountants, New Delhi (firm stamp on page, image read) | auditor stamp | IMAGE_READ
R765 | page 3 | line 435 | ENTITY | Bhupinder Kumar Sekhri, Managing Director (read from image) | signatory director | IMAGE_READ
R766 | page 3 | line 435 | ENTITY | S S Kothari Mehta & Co. LLP, Chartered Accountants, New Delhi (firm stamp on page, image read) | auditor stamp | IMAGE_READ
R767 | page 4 | line 572 | ENTITY | Bhupinder Kumar Sekhri, Managing Director (read from image) | signatory director | IMAGE_READ
R768 | page 4 | line 572 | ENTITY | S S Kothari Mehta & Co. LLP, Chartered Accountants, New Delhi (firm stamp on page, image read) | auditor stamp | IMAGE_READ
R769 | page 5 | line 590 | ENTITY | Crumb Rubber | product
R770 | page 5 | line 590 | ENTITY | Crumb Rubber Modifier | product
R771 | page 5 | line 590 | ENTITY | Bitumen | product
R772 | page 5 | line 590 | ENTITY | Bitumen Emulsion | product
R773 | page 5 | line 593 | ENTITY | Tinna Rubber Chile SpA | wholly owned subsidiary
R774 | page 5 | line 599 | ENTITY | Panipat, Haryana plant | plant
R775 | page 5 | line 600 | ENTITY | Haryana State Industrial and Infrastructure Development Corporation Limited (HSIIDC) | counterparty
R776 | page 5 | line 604 | ENTITY | Hon'ble Supreme Court of India | forum
R777 | page 5 | line 606 | ENTITY | Principal Secretary, Department of Industries, Government of Haryana, Chandigarh | representation addressee
R778 | page 6 | line 683 | ENTITY | S S Kothari Mehta & Co. LLP, Chartered Accountants (letterhead) | statutory auditor
R779 | page 7 | line 742 | ENTITY | S S Kothari Mehta & Co. LLP, FRN 000756N/N500441 | auditor firm
R780 | page 7 | line 748 | ENTITY | Ashish Kumar Mishra, Partner | audit partner
R781 | page 8 | line 898 | ENTITY | Bhupinder Kumar Sekhri, Managing Director (read from image) | signatory director | IMAGE_READ
R782 | page 8 | line 898 | ENTITY | S S Kothari Mehta & Co. LLP, Chartered Accountants, New Delhi (firm stamp on page, image read) | auditor stamp | IMAGE_READ
R783 | page 9 | line 1048 | ENTITY | Bhupinder Kumar Sekhri, Managing Director (read from image) | signatory director | IMAGE_READ
R784 | page 9 | line 1048 | ENTITY | S S Kothari Mehta & Co. LLP, Chartered Accountants, New Delhi (firm stamp on page, image read) | auditor stamp | IMAGE_READ
R785 | page 10 | line 1190 | ENTITY | Bhupinder Kumar Sekhri, Managing Director (read from image) | signatory director | IMAGE_READ
R786 | page 10 | line 1190 | ENTITY | S S Kothari Mehta & Co. LLP, Chartered Accountants, New Delhi (firm stamp on page, image read) | auditor stamp | IMAGE_READ
R787 | page 11 | line 1208 | ENTITY | Crumb Rubber | product
R788 | page 11 | line 1208 | ENTITY | Crumb Rubber Modifier | product
R789 | page 11 | line 1208 | ENTITY | Modified Bitumen | product
R790 | page 11 | line 1208 | ENTITY | Bitumen Emulsion | product
R791 | page 11 | line 1211 | ENTITY | Tinna Rubber Chile SpA | subsidiary
R792 | page 11 | line 1217 | ENTITY | Panipat, Haryana plant | plant
R793 | page 11 | line 1218 | ENTITY | Haryana State Industrial and Infrastructure Development Corporation Limited (HSIIDC) | counterparty
R794 | page 11 | line 1225 | ENTITY | Hon'ble Supreme Court of India | forum
R795 | page 11 | line 1227 | ENTITY | Principal Secretary, Department of Industries, Government of Haryana, Chandigarh | representation addressee
R796 | page 12 | line 1299 | ENTITY | S S Kothari Mehta & Co. LLP, Chartered Accountants (letterhead) | auditor
R797 | page 12 | line 1309 | ENTITY | Tinna Rubber and Infrastructure Limited (Parent Company) | parent
R798 | page 12 | line 1338 | ENTITY | Tinna Rubber Arabia Ltd.- Saudi Arabia (Wholly owned subsidiary) | subsidiary
R799 | page 12 | line 1339 | ENTITY | Global Recycle LLC - Oman (Wholly owned subsidiary) | subsidiary
R800 | page 12 | line 1340 | ENTITY | T.P. Buildtech Private Limited- India (Associate) | associate
R801 | page 12 | line 1341 | ENTITY | Mbodla Investment (PTY) Limited - South Africa (Joint Venture) | joint venture
R802 | page 13 | line 1382 | ENTITY | Ashish Kumar Mishra, Partner | audit partner

## FORWARD
R803 | page 5 | line 594 | FORWARD | objective to expand our global footprint and strengthening our global supply chain of ELTs from around the world | Chile subsidiary objective
R804 | page 5 | line 595 | FORWARD | carrying on the business of recycling and processing of end-of-life tyres (ELTs), plastic waste and scrap, battery waste and scrap, and other allied waste management and recycling activities | Chile subsidiary business scope
R805 | page 5 | line 597 | FORWARD | Capital infusion is under process | Chile SpA capital infusion pending
R806 | page 5 | line 614 | FORWARD | Company is in the process of evaluating various alternatives for relocating the plant | plant relocation
R807 | page 5 | line 614 | FORWARD | Company expects to receive compensation sanctioned from the concerned authority | compensation expected
R808 | page 11 | line 1213 | FORWARD | objective to expand our global footprint and strengthening our global supply chain of ELTs from around the world | Chile subsidiary objective
R809 | page 11 | line 1214 | FORWARD | carrying on the business of recycling and processing of end-of-life tyres (ELTs), plastic waste and scrap, battery waste and scrap, and other allied waste management and recycling activities | Chile business scope
R810 | page 11 | line 1215 | FORWARD | Capital infusion is under process | Chile capital infusion pending
R811 | page 11 | line 1233 | FORWARD | Parent Company is in the process of evaluating various alternatives for relocating the plant | plant relocation
R812 | page 11 | line 1233 | FORWARD | Parent Company expects to receive compensation from the concerned authority | compensation expected

## DATE
R813 | page 1 | line 21 | DATE | October 22, 2026 | letter date
R814 | page 1 | line 34 | DATE | THURSDAY, OCTOBER 22, 2026 | board meeting date (subject line)
R815 | page 1 | line 41 | DATE | Thursday, October 22, 2026 | board approval date
R816 | page 1 | line 42 | DATE | second quarter and half year ended on September 30, 2026 | results period
R817 | page 1 | line 48 | DATE | 11:30 AM | meeting start time
R818 | page 1 | line 48 | DATE | 02:05 PM | meeting end time
R819 | page 1 | line 61 | DATE | 2026.10.22 14:10:06 +05'30' | digital signature timestamp
R820 | page 2 | line 235 | DATE | FOR THE QUARTER AND HALF YEAR ENDED SEPTEMBER 30, 2026 | standalone P&L period
R821 | page 2 | line 280 | DATE | October 22, 2026 | standalone results signing date (Date: October 22, 2026)
R822 | page 3 | line 375 | DATE | October 21, 2026 | embedded layer: standalone BS signing date | OCR_CONFLICT
R823 | page 3 | line 381 | DATE | AS AT SEPTEMBER 30, 2026 | standalone balance sheet date
R824 | page 3 | line 381 | DATE | As at March 31, 2026 | comparative date (audited column); column header not legible in either text layer, read from image | IMAGE_READ
R825 | page 3 | line 381 | DATE | As at September 30, 2026 | current date (unaudited column); column header read from image | IMAGE_READ
R826 | page 3 | line 436 | DATE | October 22, 2026 | OCR layer and page image: standalone BS signing date
R827 | page 4 | line 519 | DATE | FOR THE HALF YEAR ENDED SEPTEMBER 30, 2026 | standalone CF period
R828 | page 4 | line 520 | DATE | September 30, 2025 | comparative half year
R829 | page 4 | line 572 | DATE | October 22, 2026 | standalone CF signing date
R830 | page 5 | line 582 | DATE | 22 October 2026 | board approval date (note 1)
R831 | page 5 | line 599 | DATE | financial year 2006-07 (printed 2006-07) | HSIIDC notified land as industrial area
R832 | page 5 | line 603 | DATE | 2001--02 | plant operational at site since
R833 | page 5 | line 606 | DATE | 15 May 2025 | representation date
R834 | page 5 | line 607 | DATE | 16 June 2006 | Land Acquisition Act notification date
R835 | page 5 | line 620 | DATE | October 22, 2026 | notes signing date
R836 | page 6 | line 693 | DATE | 30 September 2026 | review period end
R837 | page 6 | line 694 | DATE | April 01, 2026 to September 30, 2026 | YTD period
R838 | page 7 | line 752 | DATE | October 22, 2026 | report date (standalone)
R839 | page 8 | line 841 | DATE | FOR THE QUARTER AND HALF YEAR ENDED SEPTEMBER 30, 2026 | consolidated P&L period
R840 | page 8 | line 898 | DATE | October 22, 2026 | consolidated results signing date
R841 | page 9 | line 987 | DATE | AS AT SEPTEMBER 30, 2026 | consolidated BS date
R842 | page 9 | line 987 | DATE | As at March 31, 2026 | comparative date (audited column); read from image | IMAGE_READ
R843 | page 9 | line 987 | DATE | As at September 30, 2026 | current date (unaudited column); read from image | IMAGE_READ
R844 | page 9 | line 1048 | DATE | October 22, 2026 | consolidated BS signing date
R845 | page 10 | line 1132 | DATE | FOR THE HALF YEAR ENDED SEPTEMBER 30, 2026 | consolidated CF period
R846 | page 10 | line 1134 | DATE | September 30, 2025 | comparative half year
R847 | page 10 | line 1190 | DATE | October 22, 2026 | consolidated CF signing date
R848 | page 11 | line 1200 | DATE | October 22, 2026 | board approval date (note 1)
R849 | page 11 | line 1218 | DATE | financial year 2006--07 | HSIIDC notified land as industrial area
R850 | page 11 | line 1223 | DATE | 2001--02 | plant operational at site since
R851 | page 11 | line 1226 | DATE | 15 May 2025 | representation date
R852 | page 11 | line 1229 | DATE | 16 June 2006 | Land Acquisition Act notification date
R853 | page 11 | line 1239 | DATE | October 22, 2026 | notes signing date
R854 | page 12 | line 1311 | DATE | 30 September 2026 | review period end
R855 | page 12 | line 1312 | DATE | April 01, 2026 to September 30, 2026 | YTD period
R856 | page 13 | line 1368 | DATE | September 30, 2026 | unreviewed subsidiaries period end
R857 | page 13 | line 1386 | DATE | October 22, 2026 | report date (consolidated)

## QUALIFIER
R858 | page 1 | line 42 | QUALIFIER | Un-audited financial results (Consolidated and Standalone) with Limited Review Report of Statutory Auditors | results status
R859 | page 1 | line 58 | QUALIFIER | Digitally signed by SANJAY KUMAR RAWAT | signature note
R860 | page 1 | line 72 | QUALIFIER | Enclosure: as above | enclosure line
R861 | page 2 | line 235 | QUALIFIER | STATEMENT OF STANDALONE UN-AUDITED FINANCIAL RESULTS (title reads STANDLONE in the OCR layer) | statement title | OCR_SPELLING
R862 | page 2 | line 237 | QUALIFIER | Rs. in lakhs except per share data | standalone P&L unit statement
R863 | page 2 | line 240 | QUALIFIER | (Unaudited) for Q2FY27, Q1FY27, Q2FY26, H1FY27, H1FY26; (Audited) for year ended 31-Mar-26 | standalone P&L audit status per column
R864 | page 2 | line 262 | QUALIFIER | Row 'Total tax expenses' present in the page image; the OCR layer dropped its label | standalone P&L row label
R865 | page 2 | line 265 | QUALIFIER | Item that will not be reclassified to profit or loss | OCI heading (standalone)
R866 | page 2 | line 266 | QUALIFIER | Standalone P&L OCI items (a),(b),(c) and Total OCI carry values only in the Year Ended 31-Mar-26 column; all period columns show dashes | OCI row structure
R867 | page 2 | line 272 | QUALIFIER | Paid up equity share capital (Face value of Rs. 10/- Each) | face value statement
R868 | page 2 | line 274 | QUALIFIER | Earnings per equity share from continuing operation (Nominal value of share Rs. 10/-) | EPS definition (standalone)
R869 | page 2 | line 276 | QUALIFIER | H1FY26 basic EPS printed as '- 13.41' (stray leading dash mark in cell); value read as 13.41; diluted H1FY26 13.40 | standalone P&L EPS cell mark | IMAGE_READ
R870 | page 2 | line 278 | QUALIFIER | See accompanying notes to standalone financial results | notes pointer
R871 | page 3 | line 375 | QUALIFIER | Embedded layer reads Date: October 21, 2026 on the balance sheet page; OCR layer and the page image read Date: October 22, 2026, same as every other page. The October 21 reading is an embedded-layer error | date conflict between layers | OCR_CONFLICT
R872 | page 3 | line 381 | QUALIFIER | UNAUDITED STANDALONE STATEMENT OF ASSETS AND LIABILITIES (title reads STANDLONE and LIABILTIES in the OCR layer) | standalone BS title | OCR_SPELLING
R873 | page 3 | line 381 | QUALIFIER | (Unaudited) at 30-Sep-2026, (Audited) at 31-Mar-2026 | standalone BS audit status per column; read from image | IMAGE_READ
R874 | page 3 | line 382 | QUALIFIER | (Rs. in lakhs) | standalone BS unit (read from image; OCR line garbled) | IMAGE_READ
R875 | page 4 | line 519 | QUALIFIER | UNAUDITED STANDALONE STATEMENT OF CASH FLOWS | standalone CF title
R876 | page 4 | line 521 | QUALIFIER | (Rs.in Lakhs) unit statement, read from image; not in OCR line | standalone CF unit | IMAGE_READ
R877 | page 4 | line 522 | QUALIFIER | Unaudited (both half-year columns) | standalone CF audit status
R878 | page 4 | line 549 | QUALIFIER | Purchase of property plant & equipment (net of capital advances and capital payables) | CF line definition
R879 | page 5 | line 580 | QUALIFIER | Notes to the Standalone Financial Statement | notes heading
R880 | page 5 | line 582 | QUALIFIER | Note 1: results reviewed by Audit Committee and approved by Board on 22 October 2026 | note 1
R881 | page 5 | line 585 | QUALIFIER | Note 2: prepared per Ind AS (Companies (Indian Accounting Standards) Rules 2015, Section 133) and Reg 33 LODR | note 2
R882 | page 5 | line 590 | QUALIFIER | Note 3: one reportable operating segment (Ind AS 108): manufacturing and trading of Crumb Rubber, Crumb Rubber Modifier, Bitumen and Bitumen Emulsion and allied products | note 3 segment
R883 | page 5 | line 593 | QUALIFIER | Note 4: Tinna Rubber Chile SpA wholly owned subsidiary incorporated; capital infusion is under process | note 4
R884 | page 5 | line 599 | QUALIFIER | Note 5: Panipat plant land dispute with HSIIDC; auditor Emphasis of Matter applies | note 5
R885 | page 5 | line 604 | QUALIFIER | Special Leave Petition filed by the Company before Hon'ble Supreme Court dismissed | SLP outcome
R886 | page 5 | line 608 | QUALIFIER | Company has till date not claimed compensation sanctioned by State Government and deposited with appropriate authority | compensation unclaimed
R887 | page 5 | line 611 | QUALIFIER | Curative petition before Supreme Court dismissed during the quarter | curative petition outcome
R888 | page 5 | line 616 | QUALIFIER | Management believes matter not expected to have any material impact on the Company's operation and financial results | management assessment
R889 | page 6 | line 683 | QUALIFIER | Independent Auditor's Review Report on un-audited standalone results, quarter ended 30 September 2026 and YTD 1 April 2026 to 30 September 2026 | report title
R890 | page 6 | line 710 | QUALIFIER | Review per SRE 2410, moderate assurance; substantially less in scope than an audit; no audit opinion expressed | review scope limitation
R891 | page 6 | line 718 | QUALIFIER | Nothing has come to attention indicating statement not per Ind AS / Reg 33 or contains material misstatement (unmodified conclusion) | review conclusion
R892 | page 6 | line 725 | QUALIFIER | Page 1 of 2 | page marker
R893 | page 7 | line 733 | QUALIFIER | Emphasis of matter: Note 5, HSIIDC land acquisition at Panipat plant, curative petition dismissed; management view no material financial impact; conclusion not modified | auditor EoM (standalone)
R894 | page 7 | line 755 | QUALIFIER | Page 2 of 2 | page marker
R895 | page 8 | line 841 | QUALIFIER | STATEMENT OF CONSOLIDATED UN-AUDITED FINANCIAL RESULTS | consolidated P&L title
R896 | page 8 | line 843 | QUALIFIER | (Rs, in lakhs except per share data) | consolidated P&L unit statement
R897 | page 8 | line 845 | QUALIFIER | Consolidated P&L row 3 label: Profit before tax & share of profit in associates & joint venture (1-2); row 4 label: Profit before tax from continuing operation | consolidated P&L row definitions | IMAGE_READ
R898 | page 8 | line 846 | QUALIFIER | (Unaudited) for five period columns, (Audited) for year ended 31-Mar-26 (read from image) | consolidated P&L audit status per column | IMAGE_READ
R899 | page 8 | line 862 | QUALIFIER | Consolidated P&L: 'Share of profit of an associates (net of tax)' printed beneath 'Profit before tax & share of profit in associates & joint venture(1-2)' | consolidated P&L row definition
R900 | page 8 | line 869 | QUALIFIER | Item that will not to be reclassified subsequent to profit & loss | OCI heading (consolidated)
R901 | page 8 | line 883 | QUALIFIER | Net profit attributable to Owners of Parent Company and Non controlling interest (NCI shows dashes) | attribution rows
R902 | page 8 | line 891 | QUALIFIER | Earnings per equity share from continuing operation (nominal value of share Rs.10/-) | consolidated EPS definition
R903 | page 9 | line 987 | QUALIFIER | UNAUDITED CONSOLIDATED STATEMENT OF ASSETS AND LIABILITIES (title reads LIABLITIES in the OCR layer) | consolidated BS title | OCR_SPELLING
R904 | page 9 | line 987 | QUALIFIER | (Unaudited) at 30-Sep-2026, (Audited) at 31-Mar-2026 | consolidated BS audit status per column; read from image | IMAGE_READ
R905 | page 9 | line 987 | QUALIFIER | (Rs. in lakhs) | consolidated BS unit statement; read from image | IMAGE_READ
R906 | page 9 | line 996 | QUALIFIER | Consolidated ROU assets 30-Sep-2026 read 1,003.21 from image; OCR layer reads 1,603.21; the filed non-current assets total foots with 1,003.21 | consolidated BS OCR digit conflict | OCR_CONFLICT
R907 | page 10 | line 1132 | QUALIFIER | UNAUDITED CONSOLIDATED STATEMENT OF CASH FLOWS | consolidated CF title
R908 | page 10 | line 1133 | QUALIFIER | (Rs.in Lakhs) unit statement, read from image; not legible in OCR line | consolidated CF unit | IMAGE_READ
R909 | page 10 | line 1135 | QUALIFIER | Unaudited (both half-year columns) | consolidated CF audit status
R910 | page 10 | line 1162 | QUALIFIER | Purchase of property plant & equipment (net of capital advances and capital payables) | CF line definition
R911 | page 11 | line 1198 | QUALIFIER | Notes to the Consolidated Financial Results | heading
R912 | page 11 | line 1200 | QUALIFIER | Note 1: results reviewed by Audit Committee and approved by Board on October 22, 2026 | note 1
R913 | page 11 | line 1203 | QUALIFIER | Note 2: prepared per Ind AS and Reg 33 LODR | note 2
R914 | page 11 | line 1208 | QUALIFIER | Note 3: Group has one reportable operating segment (Ind AS 108): manufacturing Crumb Rubber, Crumb Rubber Modifier, Modified Bitumen & Bitumen Emulsion and allied products | note 3 segment
R915 | page 11 | line 1211 | QUALIFIER | Note 4: Parent incorporated Tinna Rubber Chile SpA wholly owned subsidiary; capital infusion is under process | note 4
R916 | page 11 | line 1217 | QUALIFIER | Note 5: Panipat plant land dispute with HSIIDC (consolidated wording of standalone Note 5) | note 5
R917 | page 11 | line 1225 | QUALIFIER | Special Leave Petition filed by the parent Company before Hon'ble Supreme Court dismissed | SLP outcome
R918 | page 11 | line 1229 | QUALIFIER | Parent Company has till date not claimed compensation sanctioned by State Government and deposited with appropriate authority | compensation unclaimed
R919 | page 11 | line 1231 | QUALIFIER | Curative petition before Supreme Court dismissed during the quarter | curative petition outcome
R920 | page 11 | line 1235 | QUALIFIER | Management believes matter not expected to have any material impact on the parent Company's operation and financial results | management assessment
R921 | page 12 | line 1299 | QUALIFIER | Independent Auditor's Review Report on unaudited consolidated results, quarter ended 30 September 2026 and YTD 1 April to 30 September 2026 | report title
R922 | page 12 | line 1325 | QUALIFIER | Review per SRE 2410, moderate assurance, no audit opinion | review scope
R923 | page 12 | line 1332 | QUALIFIER | Procedures also per SEBI circular under Regulation 33(8) LODR to extent applicable | Reg 33(8)
R924 | page 12 | line 1343 | QUALIFIER | Conclusion: nothing came to attention indicating non-disclosure under Reg 33 or material misstatement (unmodified) | review conclusion
R925 | page 13 | line 1356 | QUALIFIER | Emphasis of matter: Note 5 HSIIDC Panipat land acquisition; curative petition dismissed; management view no material financial impact; conclusion not modified | auditor EoM (consolidated)
R926 | page 13 | line 1364 | QUALIFIER | Other matter: interim results of 2 subsidiaries and 1 joint venture furnished by management, not reviewed by us or other auditors; conclusion based solely on management-certified results; not material to the Group | other matter paragraph
R927 | page 13 | line 1389 | QUALIFIER | Page 2 of 3 (footer on page 13); page 3 of 3 of the consolidated review report is not in the file | page marker, possible missing page
