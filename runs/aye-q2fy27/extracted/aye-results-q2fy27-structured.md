=== A1 STRUCTURED EXTRACTION ===
source: AyeFinance_Q2FY27_Results_Reg33_21Oct2026.pdf (Aye Finance Limited, Q2 FY27, results filing, doctype results)
fulltext: runs/aye-q2fy27/extracted/aye-results-q2fy27-fulltext.md (line numbers below = line numbers of that file, header block included)
row_id_range: R001-R755
counts: NUMBER=568; ENTITY=43; FORWARD=7; DATE=75; QUALIFIER=62; TOTAL=755
unit: Rs crores (conversion factor x1); share data in Rs; EPS in Rs.
extraction notes (mechanical):
 - Pages 4-7, 16 and 18 text layer has labels and values out of line order in the -layout fulltext. Value-to-label and column pairing for these rows came from pdftotext -raw order and was verified by cross-footing to printed totals. The raw order was an aid only; the fulltext is -layout.
 - For scrambled pages the "line" anchor is the fulltext line of the value (balance sheet, Annexures) or the label (P&L, cash flow); the other lies within +/-3 lines.
 - P&L column order: Q2 FY27 (30-Sep-26), Q1 FY27 (30-Jun-26), Q2 FY26 (30-Sep-25), H1 FY27, H1 FY26, FY26 (31-Mar-26).
 - Cells with no text value are logged CELL_BLANK_IN_TEXT; dash cells are ZERO_STANDING; OCR/garbled glyphs logged verbatim with flag.
 - Materiality: results filing, full granularity, no grouping.

## NUMBER
R001 | page 1 | line 23 | NUMBER | October 21, 2026 | date of letter/board meeting
R002 | page 1 | line 30 | NUMBER | 544699 | BSE scrip code
R003 | page 1 | line 43 | NUMBER | 11:15 A.M. (IST) | board meeting commencement time
R004 | page 1 | line 45 | NUMBER | 11:21 A.M. (IST) | results approved time
R005 | page 1 | line 47 | NUMBER | 48 hours | trading window closure period after announcement
R006 | page 3 | line 157 | NUMBER | Rs. 1.93 crores | Aye Employee Welfare Trust total assets, 30-Sep-26
R007 | page 3 | line 157 | NUMBER | Rs. 0.12 crores | Trust total revenues, Q2 FY27
R008 | page 3 | line 157 | NUMBER | Rs. 0.48 crores | Trust total revenues, H1 FY27
R009 | page 3 | line 158 | NUMBER | Rs. 0.12 crores | Trust net profit after tax, Q2 FY27
R010 | page 3 | line 158 | NUMBER | Rs. 0.47 crores | Trust net profit after tax, H1 FY27
R011 | page 3 | line 179 | NUMBER | 105047W/W101187 | MSKA ICAI firm registration no.
R012 | page 3 | line 188 | NUMBER | 133147 | auditor partner membership no.
R013 | page 3 | line 189 | NUMBER | 26133147DBJTDG7678 | UDIN, limited review report
R014 | page 4 | line 214 | NUMBER | 851.21 | balance sheet Cash and cash equivalents, as at 30-Sep-26
R015 | page 4 | line 214 | NUMBER | 620.38 | balance sheet Cash and cash equivalents, as at 31-Mar-26
R016 | page 4 | line 215 | NUMBER | 490.45 | balance sheet Bank balances other than cash and cash equivalents, as at 30-Sep-26
R017 | page 4 | line 215 | NUMBER | 390.69 | balance sheet Bank balances other than cash and cash equivalents, as at 31-Mar-26
R018 | page 4 | line 217 | NUMBER | 86.41 | balance sheet Derivative financial instruments, as at 30-Sep-26
R019 | page 4 | line 217 | NUMBER | 77.97 | balance sheet Derivative financial instruments, as at 31-Mar-26
R020 | page 4 | line 218 | NUMBER | 6,849.85 | balance sheet Loans, as at 30-Sep-26
R021 | page 4 | line 218 | NUMBER | 6,266.44 | balance sheet Loans, as at 31-Mar-26
R022 | page 4 | line 220 | NUMBER | 222.96 | balance sheet Investments, as at 30-Sep-26
R023 | page 4 | line 220 | NUMBER | 158.14 | balance sheet Investments, as at 31-Mar-26
R024 | page 4 | line 221 | NUMBER | 102.90 | balance sheet Other financial assets, as at 30-Sep-26
R025 | page 4 | line 221 | NUMBER | 107.33 | balance sheet Other financial assets, as at 31-Mar-26
R026 | page 4 | line 222 | NUMBER | 8,603.78 | balance sheet Total financial assets, as at 30-Sep-26
R027 | page 4 | line 222 | NUMBER | 7,620.95 | balance sheet Total financial assets, as at 31-Mar-26
R028 | page 4 | line 224 | NUMBER | 28.74 | balance sheet Current tax assets (net), as at 30-Sep-26
R029 | page 4 | line 224 | NUMBER | 19.45 | balance sheet Current tax assets (net), as at 31-Mar-26
R030 | page 4 | line 225 | NUMBER | 55.01 | balance sheet Deferred tax assets (net), as at 30-Sep-26
R031 | page 4 | line 225 | NUMBER | 53.38 | balance sheet Deferred tax assets (net), as at 31-Mar-26
R032 | page 4 | line 226 | NUMBER | 12.31 | balance sheet Property, plant and equipment, as at 30-Sep-26
R033 | page 4 | line 226 | NUMBER | 12.25 | balance sheet Property, plant and equipment, as at 31-Mar-26
R034 | page 4 | line 227 | NUMBER | 42.97 | balance sheet Right of use assets, as at 30-Sep-26
R035 | page 4 | line 227 | NUMBER | 44.83 | balance sheet Right of use assets, as at 31-Mar-26
R036 | page 4 | line 229 | NUMBER | 2.99 | balance sheet Intangible assets under development, as at 30-Sep-26
R037 | page 4 | line 229 | NUMBER | - | balance sheet Intangible assets under development, as at 31-Mar-26 [ZERO_STANDING]
R038 | page 4 | line 230 | NUMBER | 2.88 | balance sheet Intangible assets, as at 30-Sep-26
R039 | page 4 | line 230 | NUMBER | 4.65 | balance sheet Intangible assets, as at 31-Mar-26
R040 | page 4 | line 231 | NUMBER | 24.83 | balance sheet Other non-financial assets, as at 30-Sep-26
R041 | page 4 | line 231 | NUMBER | 17.43 | balance sheet Other non-financial assets, as at 31-Mar-26
R042 | page 4 | line 232 | NUMBER | 169.73 | balance sheet Total non-financial assets, as at 30-Sep-26
R043 | page 4 | line 232 | NUMBER | 151.99 | balance sheet Total non-financial assets, as at 31-Mar-26
R044 | page 4 | line 233 | NUMBER | 8,773.51 | balance sheet Total assets, as at 30-Sep-26
R045 | page 4 | line 233 | NUMBER | 7,772.94 | balance sheet Total assets, as at 31-Mar-26
R046 | page 4 | line 235 | NUMBER | 1,271.15 | balance sheet Debt securities, as at 30-Sep-26
R047 | page 4 | line 235 | NUMBER | 1,070.50 | balance sheet Debt securities, as at 31-Mar-26
R048 | page 4 | line 236 | NUMBER | 4,587.17 | balance sheet Borrowings (other than debt securities), as at 30-Sep-26
R049 | page 4 | line 236 | NUMBER | 3,947.13 | balance sheet Borrowings (other than debt securities), as at 31-Mar-26
R050 | page 4 | line 238 | NUMBER | 46.61 | balance sheet Lease liabilities, as at 30-Sep-26
R051 | page 4 | line 238 | NUMBER | 47.47 | balance sheet Lease liabilities, as at 31-Mar-26
R052 | page 4 | line 239 | NUMBER | 73.84 | balance sheet Other financial liabilities, as at 30-Sep-26
R053 | page 4 | line 239 | NUMBER | 81.75 | balance sheet Other financial liabilities, as at 31-Mar-26
R054 | page 4 | line 240 | NUMBER | 5,978.77 | balance sheet Total financial liabilities, as at 30-Sep-26
R055 | page 4 | line 240 | NUMBER | 5,146.85 | balance sheet Total financial liabilities, as at 31-Mar-26
R056 | page 4 | line 244 | NUMBER | 10.82 | balance sheet Current tax liabilities (net), as at 30-Sep-26
R057 | page 4 | line 244 | NUMBER | 4.58 | balance sheet Current tax liabilities (net), as at 31-Mar-26
R058 | page 4 | line 245 | NUMBER | 58.68 | balance sheet Provisions, as at 30-Sep-26
R059 | page 4 | line 245 | NUMBER | 54.33 | balance sheet Provisions, as at 31-Mar-26
R060 | page 4 | line 246 | NUMBER | 30.63 | balance sheet Other non-financial liabilities, as at 30-Sep-26
R061 | page 4 | line 246 | NUMBER | 34.47 | balance sheet Other non-financial liabilities, as at 31-Mar-26
R062 | page 4 | line 247 | NUMBER | 100.13 | balance sheet Total non-financial liabilities, as at 30-Sep-26
R063 | page 4 | line 247 | NUMBER | 93.38 | balance sheet Total non-financial liabilities, as at 31-Mar-26
R064 | page 4 | line 250 | NUMBER | 49.02 | balance sheet Equity share capital, as at 30-Sep-26
R065 | page 4 | line 250 | NUMBER | 48.90 | balance sheet Equity share capital, as at 31-Mar-26
R066 | page 4 | line 251 | NUMBER | 2,645.59 | balance sheet Other equity, as at 30-Sep-26
R067 | page 4 | line 251 | NUMBER | 2,483.81 | balance sheet Other equity, as at 31-Mar-26
R068 | page 4 | line 252 | NUMBER | 2,694.61 | balance sheet Total equity, as at 30-Sep-26
R069 | page 4 | line 252 | NUMBER | 2,532.71 | balance sheet Total equity, as at 31-Mar-26
R070 | page 4 | line 253 | NUMBER | 8,773.51 | balance sheet Total liabilities and equity, as at 30-Sep-26
R071 | page 4 | line 253 | NUMBER | 7,772.94 | balance sheet Total liabilities and equity, as at 31-Mar-26
R072 | page 5 | line 288 | NUMBER | 479.26 | Interest income, Q2 FY27 (qtr 30-Sep-26)
R073 | page 5 | line 288 | NUMBER | 452.67 | Interest income, Q1 FY27 (qtr 30-Jun-26)
R074 | page 5 | line 288 | NUMBER | 371.39 | Interest income, Q2 FY26 (qtr 30-Sep-25)
R075 | page 5 | line 288 | NUMBER | 931.93 | Interest income, H1 FY27 (6m 30-Sep-26)
R076 | page 5 | line 288 | NUMBER | 730.67 | Interest income, H1 FY26 (6m 30-Sep-25)
R077 | page 5 | line 288 | NUMBER | 1,549.13 | Interest income, FY26 (yr 31-Mar-26)
R078 | page 5 | line 289 | NUMBER | 20.51 | Fees and commission income, Q2 FY27 (qtr 30-Sep-26)
R079 | page 5 | line 289 | NUMBER | 19.56 | Fees and commission income, Q1 FY27 (qtr 30-Jun-26)
R080 | page 5 | line 289 | NUMBER | 18.10 | Fees and commission income, Q2 FY26 (qtr 30-Sep-25)
R081 | page 5 | line 289 | NUMBER | 40.07 | Fees and commission income, H1 FY27 (6m 30-Sep-26)
R082 | page 5 | line 289 | NUMBER | 32.69 | Fees and commission income, H1 FY26 (6m 30-Sep-25)
R083 | page 5 | line 289 | NUMBER | 73.54 | Fees and commission income, FY26 (yr 31-Mar-26)
R084 | page 5 | line 290 | NUMBER | 10.12 | Net gain/(loss) on derecognition of financial instruments (amortised cost), Q2 FY27 (qtr 30-Sep-26)
R085 | page 5 | line 290 | NUMBER | 16.28 | Net gain/(loss) on derecognition of financial instruments (amortised cost), Q2 FY26 (qtr 30-Sep-25)
R086 | page 5 | line 290 | NUMBER | 10.12 | Net gain/(loss) on derecognition of financial instruments (amortised cost), H1 FY27 (6m 30-Sep-26)
R087 | page 5 | line 290 | NUMBER | 29.32 | Net gain/(loss) on derecognition of financial instruments (amortised cost), H1 FY26 (6m 30-Sep-25)
R088 | page 5 | line 290 | NUMBER | 67.97 | Net gain/(loss) on derecognition of financial instruments (amortised cost), FY26 (yr 31-Mar-26)
R089 | page 5 | line 290 | NUMBER | (no value in text layer) | Net gain on derecognition, Q1 FY27 (June qtr) cell [CELL_BLANK_IN_TEXT]
R090 | page 5 | line 292 | NUMBER | 4.50 | Net gain on fair value changes, Q2 FY27 (qtr 30-Sep-26)
R091 | page 5 | line 292 | NUMBER | 5.14 | Net gain on fair value changes, Q1 FY27 (qtr 30-Jun-26)
R092 | page 5 | line 292 | NUMBER | 29.12 | Net gain on fair value changes, Q2 FY26 (qtr 30-Sep-25)
R093 | page 5 | line 292 | NUMBER | 9.64 | Net gain on fair value changes, H1 FY27 (6m 30-Sep-26)
R094 | page 5 | line 292 | NUMBER | 47.67 | Net gain on fair value changes, H1 FY26 (6m 30-Sep-25)
R095 | page 5 | line 292 | NUMBER | 105.79 | Net gain on fair value changes, FY26 (yr 31-Mar-26)
R096 | page 5 | line 293 | NUMBER | 514.39 | Total revenue from operations, Q2 FY27 (qtr 30-Sep-26)
R097 | page 5 | line 293 | NUMBER | 477.37 | Total revenue from operations, Q1 FY27 (qtr 30-Jun-26)
R098 | page 5 | line 293 | NUMBER | 434.89 | Total revenue from operations, Q2 FY26 (qtr 30-Sep-25)
R099 | page 5 | line 293 | NUMBER | 991.76 | Total revenue from operations, H1 FY27 (6m 30-Sep-26)
R100 | page 5 | line 293 | NUMBER | 840.35 | Total revenue from operations, H1 FY26 (6m 30-Sep-25)
R101 | page 5 | line 293 | NUMBER | 1,796.43 | Total revenue from operations, FY26 (yr 31-Mar-26)
R102 | page 5 | line 299 | NUMBER | 12.73 | Other income, Q2 FY27 (qtr 30-Sep-26)
R103 | page 5 | line 299 | NUMBER | 12.29 | Other income, Q1 FY27 (qtr 30-Jun-26)
R104 | page 5 | line 299 | NUMBER | 10.34 | Other income, Q2 FY26 (qtr 30-Sep-25)
R105 | page 5 | line 299 | NUMBER | 25.02 | Other income, H1 FY27 (6m 30-Sep-26)
R106 | page 5 | line 299 | NUMBER | 19.51 | Other income, H1 FY26 (6m 30-Sep-25)
R107 | page 5 | line 299 | NUMBER | 48.51 | Other income, FY26 (yr 31-Mar-26)
R108 | page 5 | line 300 | NUMBER | 527.12 | Total income [1+2], Q2 FY27 (qtr 30-Sep-26)
R109 | page 5 | line 300 | NUMBER | 489.66 | Total income [1+2], Q1 FY27 (qtr 30-Jun-26)
R110 | page 5 | line 300 | NUMBER | 445.23 | Total income [1+2], Q2 FY26 (qtr 30-Sep-25)
R111 | page 5 | line 300 | NUMBER | 1,016.78 | Total income [1+2], H1 FY27 (6m 30-Sep-26)
R112 | page 5 | line 300 | NUMBER | 859.86 | Total income [1+2], H1 FY26 (6m 30-Sep-25)
R113 | page 5 | line 300 | NUMBER | 1,844.94 | Total income [1+2], FY26 (yr 31-Mar-26)
R114 | page 5 | line 303 | NUMBER | 144.68 | Finance cost, Q2 FY27 (qtr 30-Sep-26)
R115 | page 5 | line 303 | NUMBER | 130.61 | Finance cost, Q1 FY27 (qtr 30-Jun-26)
R116 | page 5 | line 303 | NUMBER | 132.53 | Finance cost, Q2 FY26 (qtr 30-Sep-25)
R117 | page 5 | line 303 | NUMBER | 275.29 | Finance cost, H1 FY27 (6m 30-Sep-26)
R118 | page 5 | line 303 | NUMBER | 258.86 | Finance cost, H1 FY26 (6m 30-Sep-25)
R119 | page 5 | line 303 | NUMBER | 534.07 | Finance cost, FY26 (yr 31-Mar-26)
R120 | page 5 | line 304 | NUMBER | - | Net loss on fair value changes, Q2 FY27 (qtr 30-Sep-26) [ZERO_STANDING]
R121 | page 5 | line 304 | NUMBER | - | Net loss on fair value changes, Q1 FY27 (qtr 30-Jun-26) [ZERO_STANDING]
R122 | page 5 | line 304 | NUMBER | 18.66 | Net loss on fair value changes, Q2 FY26 (qtr 30-Sep-25)
R123 | page 5 | line 304 | NUMBER | - | Net loss on fair value changes, H1 FY27 (6m 30-Sep-26) [ZERO_STANDING]
R124 | page 5 | line 304 | NUMBER | 30.75 | Net loss on fair value changes, H1 FY26 (6m 30-Sep-25)
R125 | page 5 | line 304 | NUMBER | 66.77 | Net loss on fair value changes, FY26 (yr 31-Mar-26)
R126 | page 5 | line 305 | NUMBER | 81.90 | Impairment on financial instruments, Q2 FY27 (qtr 30-Sep-26)
R127 | page 5 | line 305 | NUMBER | 81.41 | Impairment on financial instruments, Q1 FY27 (qtr 30-Jun-26)
R128 | page 5 | line 305 | NUMBER | 86.22 | Impairment on financial instruments, Q2 FY26 (qtr 30-Sep-25)
R129 | page 5 | line 305 | NUMBER | 163.31 | Impairment on financial instruments, H1 FY27 (6m 30-Sep-26)
R130 | page 5 | line 305 | NUMBER | 172.93 | Impairment on financial instruments, H1 FY26 (6m 30-Sep-25)
R131 | page 5 | line 305 | NUMBER | 335.73 | Impairment on financial instruments, FY26 (yr 31-Mar-26)
R132 | page 5 | line 306 | NUMBER | 135.74 | Employee benefit expenses, Q2 FY27 (qtr 30-Sep-26)
R133 | page 5 | line 306 | NUMBER | 138.64 | Employee benefit expenses, Q1 FY27 (qtr 30-Jun-26)
R134 | page 5 | line 306 | NUMBER | 119.61 | Employee benefit expenses, Q2 FY26 (qtr 30-Sep-25)
R135 | page 5 | line 306 | NUMBER | 274.38 | Employee benefit expenses, H1 FY27 (6m 30-Sep-26)
R136 | page 5 | line 306 | NUMBER | 233.41 | Employee benefit expenses, H1 FY26 (6m 30-Sep-25)
R137 | page 5 | line 306 | NUMBER | 480.44 | Employee benefit expenses, FY26 (yr 31-Mar-26)
R138 | page 5 | line 307 | NUMBER | 6.43 | Depreciation and amortization expense, Q2 FY27 (qtr 30-Sep-26)
R139 | page 5 | line 307 | NUMBER | 6.17 | Depreciation and amortization expense, Q1 FY27 (qtr 30-Jun-26)
R140 | page 5 | line 307 | NUMBER | 6.24 | Depreciation and amortization expense, Q2 FY26 (qtr 30-Sep-25)
R141 | page 5 | line 307 | NUMBER | 12.60 | Depreciation and amortization expense, H1 FY27 (6m 30-Sep-26)
R142 | page 5 | line 307 | NUMBER | 11.34 | Depreciation and amortization expense, H1 FY26 (6m 30-Sep-25)
R143 | page 5 | line 307 | NUMBER | 26.31 | Depreciation and amortization expense, FY26 (yr 31-Mar-26)
R144 | page 5 | line 308 | NUMBER | 42.57 | Other expenses, Q2 FY27 (qtr 30-Sep-26)
R145 | page 5 | line 308 | NUMBER | 35.68 | Other expenses, Q1 FY27 (qtr 30-Jun-26)
R146 | page 5 | line 308 | NUMBER | 40.28 | Other expenses, Q2 FY26 (qtr 30-Sep-25)
R147 | page 5 | line 308 | NUMBER | 78.25 | Other expenses, H1 FY27 (6m 30-Sep-26)
R148 | page 5 | line 308 | NUMBER | 69.99 | Other expenses, H1 FY26 (6m 30-Sep-25)
R149 | page 5 | line 308 | NUMBER | 154.32 | Other expenses, FY26 (yr 31-Mar-26)
R150 | page 5 | line 309 | NUMBER | 411.32 | Total expenses, Q2 FY27 (qtr 30-Sep-26)
R151 | page 5 | line 309 | NUMBER | 392.51 | Total expenses, Q1 FY27 (qtr 30-Jun-26)
R152 | page 5 | line 309 | NUMBER | 403.54 | Total expenses, Q2 FY26 (qtr 30-Sep-25)
R153 | page 5 | line 309 | NUMBER | 803.83 | Total expenses, H1 FY27 (6m 30-Sep-26)
R154 | page 5 | line 309 | NUMBER | 777.28 | Total expenses, H1 FY26 (6m 30-Sep-25)
R155 | page 5 | line 309 | NUMBER | 1,597.64 | Total expenses, FY26 (yr 31-Mar-26)
R156 | page 5 | line 311 | NUMBER | 115.80 | Profit before tax [3-4], Q2 FY27 (qtr 30-Sep-26)
R157 | page 5 | line 311 | NUMBER | 97.15 | Profit before tax [3-4], Q1 FY27 (qtr 30-Jun-26)
R158 | page 5 | line 311 | NUMBER | 41.69 | Profit before tax [3-4], Q2 FY26 (qtr 30-Sep-25)
R159 | page 5 | line 311 | NUMBER | 212.95 | Profit before tax [3-4], H1 FY27 (6m 30-Sep-26)
R160 | page 5 | line 311 | NUMBER | 82.58 | Profit before tax [3-4], H1 FY26 (6m 30-Sep-25)
R161 | page 5 | line 311 | NUMBER | 247.30 | Profit before tax [3-4], FY26 (yr 31-Mar-26)
R162 | page 5 | line 314 | NUMBER | 26.93 | Current tax, Q2 FY27 (qtr 30-Sep-26)
R163 | page 5 | line 314 | NUMBER | 27.20 | Current tax, Q1 FY27 (qtr 30-Jun-26)
R164 | page 5 | line 314 | NUMBER | 0.93 | Current tax, Q2 FY26 (qtr 30-Sep-25)
R165 | page 5 | line 314 | NUMBER | 54.13 | Current tax, H1 FY27 (6m 30-Sep-26)
R166 | page 5 | line 314 | NUMBER | 14.58 | Current tax, H1 FY26 (6m 30-Sep-25)
R167 | page 5 | line 314 | NUMBER | 45.93 | Current tax, FY26 (yr 31-Mar-26)
R168 | page 5 | line 315 | NUMBER | 2.15 | Deferred tax, Q2 FY27 (qtr 30-Sep-26)
R169 | page 5 | line 315 | NUMBER | (4.55) | Deferred tax, Q1 FY27 (qtr 30-Jun-26)
R170 | page 5 | line 315 | NUMBER | 6.23 | Deferred tax, Q2 FY26 (qtr 30-Sep-25)
R171 | page 5 | line 315 | NUMBER | (2.40) | Deferred tax, H1 FY27 (6m 30-Sep-26)
R172 | page 5 | line 315 | NUMBER | 2.88 | Deferred tax, H1 FY26 (6m 30-Sep-25)
R173 | page 5 | line 315 | NUMBER | 7.74 | Deferred tax, FY26 (yr 31-Mar-26)
R174 | page 5 | line 316 | NUMBER | 29.08 | Income tax expense, Q2 FY27 (qtr 30-Sep-26)
R175 | page 5 | line 316 | NUMBER | 22.65 | Income tax expense, Q1 FY27 (qtr 30-Jun-26)
R176 | page 5 | line 316 | NUMBER | 7.16 | Income tax expense, Q2 FY26 (qtr 30-Sep-25)
R177 | page 5 | line 316 | NUMBER | 51.73 | Income tax expense, H1 FY27 (6m 30-Sep-26)
R178 | page 5 | line 316 | NUMBER | 17.46 | Income tax expense, H1 FY26 (6m 30-Sep-25)
R179 | page 5 | line 316 | NUMBER | 53.67 | Income tax expense, FY26 (yr 31-Mar-26)
R180 | page 5 | line 318 | NUMBER | 86.72 | Profit for the period/year (A), Q2 FY27 (qtr 30-Sep-26)
R181 | page 5 | line 318 | NUMBER | 74.50 | Profit for the period/year (A), Q1 FY27 (qtr 30-Jun-26)
R182 | page 5 | line 318 | NUMBER | 34.53 | Profit for the period/year (A), Q2 FY26 (qtr 30-Sep-25)
R183 | page 5 | line 318 | NUMBER | 161.22 | Profit for the period/year (A), H1 FY27 (6m 30-Sep-26)
R184 | page 5 | line 318 | NUMBER | 65.12 | Profit for the period/year (A), H1 FY26 (6m 30-Sep-25)
R185 | page 5 | line 318 | NUMBER | 193.63 | Profit for the period/year (A), FY26 (yr 31-Mar-26)
R186 | page 5 | line 323 | NUMBER | (1.91) | OCI re-measurement income/(loss) on defined benefit plans, Q2 FY27 (qtr 30-Sep-26)
R187 | page 5 | line 323 | NUMBER | (3.45) | OCI re-measurement income/(loss) on defined benefit plans, Q1 FY27 (qtr 30-Jun-26)
R188 | page 5 | line 323 | NUMBER | (0.65) | OCI re-measurement income/(loss) on defined benefit plans, Q2 FY26 (qtr 30-Sep-25)
R189 | page 5 | line 323 | NUMBER | (5.36) | OCI re-measurement income/(loss) on defined benefit plans, H1 FY27 (6m 30-Sep-26)
R190 | page 5 | line 323 | NUMBER | (0.44) | OCI re-measurement income/(loss) on defined benefit plans, H1 FY26 (6m 30-Sep-25)
R191 | page 5 | line 323 | NUMBER | (0.56) | OCI re-measurement income/(loss) on defined benefit plans, FY26 (yr 31-Mar-26)
R192 | page 5 | line 324 | NUMBER | 0.48 | OCI income tax effect (items not reclassified), Q2 FY27 (qtr 30-Sep-26)
R193 | page 5 | line 324 | NUMBER | 0.87 | OCI income tax effect (items not reclassified), Q1 FY27 (qtr 30-Jun-26)
R194 | page 5 | line 324 | NUMBER | 0.16 | OCI income tax effect (items not reclassified), Q2 FY26 (qtr 30-Sep-25)
R195 | page 5 | line 324 | NUMBER | 1.35 | OCI income tax effect (items not reclassified), H1 FY27 (6m 30-Sep-26)
R196 | page 5 | line 324 | NUMBER | 0.11 | OCI income tax effect (items not reclassified), H1 FY26 (6m 30-Sep-25)
R197 | page 5 | line 324 | NUMBER | 0.14 | OCI income tax effect (items not reclassified), FY26 (yr 31-Mar-26)
R198 | page 5 | line 328 | NUMBER | 4.68 | OCI cash flow hedge reserve, Q2 FY27 (qtr 30-Sep-26)
R199 | page 5 | line 328 | NUMBER | (3.93) | OCI cash flow hedge reserve, Q1 FY27 (qtr 30-Jun-26)
R200 | page 5 | line 328 | NUMBER | - | OCI cash flow hedge reserve, Q2 FY26 (qtr 30-Sep-25) [ZERO_STANDING]
R201 | page 5 | line 328 | NUMBER | 0.75 | OCI cash flow hedge reserve, H1 FY27 (6m 30-Sep-26)
R202 | page 5 | line 328 | NUMBER | - | OCI cash flow hedge reserve, H1 FY26 (6m 30-Sep-25) [ZERO_STANDING]
R203 | page 5 | line 328 | NUMBER | - | OCI cash flow hedge reserve, FY26 (yr 31-Mar-26) [ZERO_STANDING]
R204 | page 5 | line 329 | NUMBER | (1.18) | OCI income tax effect (items reclassified), Q2 FY27 (qtr 30-Sep-26)
R205 | page 5 | line 329 | NUMBER | 0.99 | OCI income tax effect (items reclassified), Q1 FY27 (qtr 30-Jun-26)
R206 | page 5 | line 329 | NUMBER | - | OCI income tax effect (items reclassified), Q2 FY26 (qtr 30-Sep-25) [ZERO_STANDING]
R207 | page 5 | line 329 | NUMBER | (0.19) | OCI income tax effect (items reclassified), H1 FY27 (6m 30-Sep-26)
R208 | page 5 | line 329 | NUMBER | - | OCI income tax effect (items reclassified), H1 FY26 (6m 30-Sep-25) [ZERO_STANDING]
R209 | page 5 | line 329 | NUMBER | - | OCI income tax effect (items reclassified), FY26 (yr 31-Mar-26) [ZERO_STANDING]
R210 | page 5 | line 331 | NUMBER | 2.07 | Total OCI/(loss) for the period/year (B), Q2 FY27 (qtr 30-Sep-26)
R211 | page 5 | line 331 | NUMBER | (5.52) | Total OCI/(loss) for the period/year (B), Q1 FY27 (qtr 30-Jun-26)
R212 | page 5 | line 331 | NUMBER | (0.49) | Total OCI/(loss) for the period/year (B), Q2 FY26 (qtr 30-Sep-25)
R213 | page 5 | line 331 | NUMBER | (3.45) | Total OCI/(loss) for the period/year (B), H1 FY27 (6m 30-Sep-26)
R214 | page 5 | line 331 | NUMBER | (0.33) | Total OCI/(loss) for the period/year (B), H1 FY26 (6m 30-Sep-25)
R215 | page 5 | line 331 | NUMBER | (0.42) | Total OCI/(loss) for the period/year (B), FY26 (yr 31-Mar-26)
R216 | page 5 | line 334 | NUMBER | 88.79 | Total comprehensive income (A+B), Q2 FY27 (qtr 30-Sep-26)
R217 | page 5 | line 334 | NUMBER | 68.98 | Total comprehensive income (A+B), Q1 FY27 (qtr 30-Jun-26)
R218 | page 5 | line 334 | NUMBER | 34.04 | Total comprehensive income (A+B), Q2 FY26 (qtr 30-Sep-25)
R219 | page 5 | line 334 | NUMBER | 157.77 | Total comprehensive income (A+B), H1 FY27 (6m 30-Sep-26)
R220 | page 5 | line 334 | NUMBER | 64.79 | Total comprehensive income (A+B), H1 FY26 (6m 30-Sep-25)
R221 | page 5 | line 334 | NUMBER | 193.21 | Total comprehensive income (A+B), FY26 (yr 31-Mar-26)
R222 | page 5 | line 337 | NUMBER | 3.51 | Basic EPS (Rs.), Q2 FY27 (qtr 30-Sep-26)
R223 | page 5 | line 337 | NUMBER | 3.02 | Basic EPS (Rs.), Q1 FY27 (qtr 30-Jun-26)
R224 | page 5 | line 337 | NUMBER | 1.80 | Basic EPS (Rs.), Q2 FY26 (qtr 30-Sep-25)
R225 | page 5 | line 337 | NUMBER | 6.53 | Basic EPS (Rs.), H1 FY27 (6m 30-Sep-26)
R226 | page 5 | line 337 | NUMBER | 3.40 | Basic EPS (Rs.), H1 FY26 (6m 30-Sep-25)
R227 | page 5 | line 337 | NUMBER | 9.73 | Basic EPS (Rs.), FY26 (yr 31-Mar-26)
R228 | page 5 | line 338 | NUMBER | 3.48 | Diluted EPS (Rs.), Q2 FY27 (qtr 30-Sep-26)
R229 | page 5 | line 338 | NUMBER | 3.00 | Diluted EPS (Rs.), Q1 FY27 (qtr 30-Jun-26)
R230 | page 5 | line 338 | NUMBER | 1.77 | Diluted EPS (Rs.), Q2 FY26 (qtr 30-Sep-25)
R231 | page 5 | line 338 | NUMBER | 6.49 | Diluted EPS (Rs.), H1 FY27 (6m 30-Sep-26)
R232 | page 5 | line 338 | NUMBER | 3.34 | Diluted EPS (Rs.), H1 FY26 (6m 30-Sep-25)
R233 | page 5 | line 338 | NUMBER | 9.60 | Diluted EPS (Rs.), FY26 (yr 31-Mar-26)
R234 | page 5 | line 340 | NUMBER | 2.00 | Nominal value per share (Rs.), Q2 FY27 (qtr 30-Sep-26)
R235 | page 5 | line 340 | NUMBER | 2.00 | Nominal value per share (Rs.), Q1 FY27 (qtr 30-Jun-26)
R236 | page 5 | line 340 | NUMBER | 2.00 | Nominal value per share (Rs.), Q2 FY26 (qtr 30-Sep-25)
R237 | page 5 | line 340 | NUMBER | 2.00 | Nominal value per share (Rs.), H1 FY27 (6m 30-Sep-26)
R238 | page 5 | line 340 | NUMBER | 2.00 | Nominal value per share (Rs.), H1 FY26 (6m 30-Sep-25)
R239 | page 5 | line 340 | NUMBER | 2.00 | Nominal value per share (Rs.), FY26 (yr 31-Mar-26)
R240 | page 6 | line 365 | NUMBER | 212.95 | cash flow Profit before tax, H1 FY27
R241 | page 6 | line 365 | NUMBER | 82.58 | cash flow Profit before tax, H1 FY26
R242 | page 6 | line 367 | NUMBER | 5.21 | cash flow Depreciation and impairment of PPE, H1 FY27
R243 | page 6 | line 367 | NUMBER | 5.11 | cash flow Depreciation and impairment of PPE, H1 FY26
R244 | page 6 | line 368 | NUMBER | 7.39 | cash flow Depreciation on right of use assets, H1 FY27
R245 | page 6 | line 368 | NUMBER | 6.23 | cash flow Depreciation on right of use assets, H1 FY26
R246 | page 6 | line 369 | NUMBER | - | cash flow Loss/(Gain) on fair value of cross currency swap, H1 FY27 [ZERO_STANDING]
R247 | page 6 | line 369 | NUMBER | (31.41) | cash flow Loss/(Gain) on fair value of cross currency swap, H1 FY26
R248 | page 6 | line 370 | NUMBER | 0-64) | cash flow Profit on sale of mutual fund units, H1 FY27 [OCR_GARBLED]
R249 | page 6 | line 370 | NUMBER | (16.26) | cash flow Profit on sale of mutual fund units, H1 FY26
R250 | page 6 | line 371 | NUMBER | (0.55) | cash flow Impairment of financial instruments, H1 FY27
R251 | page 6 | line 371 | NUMBER | 23.98 | cash flow Impairment of financial instruments, H1 FY26
R252 | page 6 | line 372 | NUMBER | (0.16) | cash flow Loss/(Gain) on early termination of lease, H1 FY27
R253 | page 6 | line 372 | NUMBER | (0.14) | cash flow Loss/(Gain) on early termination of lease, H1 FY26
R254 | page 6 | line 373 | NUMBER | - | cash flow Provision on investment, H1 FY27 [ZERO_STANDING]
R255 | page 6 | line 373 | NUMBER | - | cash flow Provision on investment, H1 FY26 [ZERO_STANDING]
R256 | page 6 | line 374 | NUMBER | 155.56 | cash flow Loans and advances written off, H1 FY27
R257 | page 6 | line 374 | NUMBER | 146.20 | cash flow Loans and advances written off, H1 FY26
R258 | page 6 | line 375 | NUMBER | 8.30 | cash flow Loss on settlement, H1 FY27
R259 | page 6 | line 375 | NUMBER | 2.75 | cash flow Loss on settlement, H1 FY26
R260 | page 6 | line 376 | NUMBER | - | cash flow (Profit)/Loss on sale of PPE (net), H1 FY27 [ZERO_STANDING]
R261 | page 6 | line 376 | NUMBER | (0.05) | cash flow (Profit)/Loss on sale of PPE (net), H1 FY26
R262 | page 6 | line 377 | NUMBER | 0.99 | cash flow Expense on employee stock option scheme, H1 FY27
R263 | page 6 | line 377 | NUMBER | 4.23 | cash flow Expense on employee stock option scheme, H1 FY26
R264 | page 6 | line 378 | NUMBER | (0.26) | cash flow Unrealised interest income on security deposit, H1 FY27
R265 | page 6 | line 378 | NUMBER | (0.21) | cash flow Unrealised interest income on security deposit, H1 FY26
R266 | page 6 | line 379 | NUMBER | 3.79 | cash flow Interest on lease liabilities, H1 FY27
R267 | page 6 | line 379 | NUMBER | 2.88 | cash flow Interest on lease liabilities, H1 FY26
R268 | page 6 | line 380 | NUMBER | 271.49 | cash flow Interest on borrowing, H1 FY27
R269 | page 6 | line 380 | NUMBER | 255.98 | cash flow Interest on borrowing, H1 FY26
R270 | page 6 | line 381 | NUMBER | (17.56) | cash flow Interest on fixed deposit, H1 FY27
R271 | page 6 | line 381 | NUMBER | (13.02) | cash flow Interest on fixed deposit, H1 FY26
R272 | page 6 | line 382 | NUMBER | - | cash flow Interest on income tax refund, H1 FY27 [ZERO_STANDING]
R273 | page 6 | line 382 | NUMBER | - | cash flow Interest on income tax refund, H1 FY26 [ZERO_STANDING]
R274 | page 6 | line 384 | NUMBER | 637.51 | cash flow Operating profit before working capital changes, H1 FY27
R275 | page 6 | line 384 | NUMBER | 468.85 | cash flow Operating profit before working capital changes, H1 FY26
R276 | page 6 | line 386 | NUMBER | 63.45 | cash flow Decrease/(Increase) in bank balances not cash equivalents, H1 FY27
R277 | page 6 | line 386 | NUMBER | (25.62) | cash flow Decrease/(Increase) in bank balances not cash equivalents, H1 FY26
R278 | page 6 | line 387 | NUMBER | (746.94) | cash flow Decrease/(Increase) in loan portfolio, H1 FY27
R279 | page 6 | line 387 | NUMBER | (607.44) | cash flow Decrease/(Increase) in loan portfolio, H1 FY26
R280 | page 6 | line 388 | NUMBER | 4.42 | cash flow Decrease/(Increase) in other financial assets, H1 FY27
R281 | page 6 | line 388 | NUMBER | (22.33) | cash flow Decrease/(Increase) in other financial assets, H1 FY26
R282 | page 6 | line 389 | NUMBER | (7.40) | cash flow Decrease/(Increase) in other non financial assets, H1 FY27
R283 | page 6 | line 389 | NUMBER | (9.49) | cash flow Decrease/(Increase) in other non financial assets, H1 FY26
R284 | page 6 | line 390 | NUMBER | (1.35) | cash flow (Decrease)/Increase in other financial liabilities (excl. lease), H1 FY27
R285 | page 6 | line 390 | NUMBER | 1.00 | cash flow (Decrease)/Increase in other financial liabilities (excl. lease), H1 FY26
R286 | page 6 | line 391 | NUMBER | (3.84) | cash flow (Decrease)/Increase in other non financial liabilities, H1 FY27
R287 | page 6 | line 391 | NUMBER | (2.13) | cash flow (Decrease)/Increase in other non financial liabilities, H1 FY26
R288 | page 6 | line 392 | NUMBER | (1.01) | cash flow (Decrease)/Increase in provisions, H1 FY27
R289 | page 6 | line 392 | NUMBER | 5.47 | cash flow (Decrease)/Increase in provisions, H1 FY26
R290 | page 6 | line 393 | NUMBER | (55.17) | cash flow Cash used in operations, H1 FY27
R291 | page 6 | line 393 | NUMBER | (191.69) | cash flow Cash used in operations, H1 FY26
R292 | page 6 | line 395 | NUMBER | (57.18) | cash flow Income taxes paid, H1 FY27
R293 | page 6 | line 395 | NUMBER | (24.78) | cash flow Income taxes paid, H1 FY26
R294 | page 6 | line 396 | NUMBER | (112.35) | cash flow Net cash used in operating activities (A), H1 FY27
R295 | page 6 | line 396 | NUMBER | (216.47) | cash flow Net cash used in operating activities (A), H1 FY26
R296 | page 6 | line 404 | NUMBER | (3.52) | cash flow Purchase of PPE excl. ROU assets, H1 FY27
R297 | page 6 | line 404 | NUMBER | (8.81) | cash flow Purchase of PPE excl. ROU assets, H1 FY26
R298 | page 6 | line 405 | NUMBER | 0.02 | cash flow Sale of PPE excl. ROU assets, H1 FY27
R299 | page 6 | line 405 | NUMBER | 0.24 | cash flow Sale of PPE excl. ROU assets, H1 FY26
R300 | page 6 | line 406 | NUMBER | (4,987.92) | cash flow Purchase of investments, H1 FY27
R301 | page 6 | line 406 | NUMBER | (5,081.14) | cash flow Purchase of investments, H1 FY26
R302 | page 6 | line 407 | NUMBER | 4,932.74 | cash flow Sale of investments, H1 FY27
R303 | page 6 | line 407 | NUMBER | 5,074.95 | cash flow Sale of investments, H1 FY26
R304 | page 6 | line 408 | NUMBER | (163.21) | cash flow Increase in fixed deposit, original maturity >3 months, H1 FY27
R305 | page 6 | line 408 | NUMBER | 4.55 | cash flow Increase in fixed deposit, original maturity >3 months, H1 FY26
R306 | page 6 | line 409 | NUMBER | 15.16 | cash flow Interest on fixed deposit (investing), H1 FY27
R307 | page 6 | line 409 | NUMBER | 13.02 | cash flow Interest on fixed deposit (investing), H1 FY26
R308 | page 6 | line 410 | NUMBER | (206.73) | cash flow Net cash used in/generated from investing activities (B), H1 FY27
R309 | page 6 | line 410 | NUMBER | 2.81 | cash flow Net cash used in/generated from investing activities (B), H1 FY26
R310 | page 7 | line 428 | NUMBER | 3.43 | cash flow Proceeds from issue of equity shares (incl. premium), H1 FY27
R311 | page 7 | line 428 | NUMBER | (no value in text layer) | cash flow Proceeds from issue of equity shares (incl. premium), H1 FY26 cell [CELL_BLANK_IN_TEXT]
R312 | page 7 | line 429 | NUMBER | (6.56) | cash flow Share issue expenses, H1 FY27
R313 | page 7 | line 429 | NUMBER | (no value in text layer) | cash flow Share issue expenses, H1 FY26 cell [CELL_BLANK_IN_TEXT]
R314 | page 7 | line 430 | NUMBER | 360.00 | cash flow Proceeds from issue of debt securities, H1 FY27
R315 | page 7 | line 430 | NUMBER | 375.00 | cash flow Proceeds from issue of debt securities, H1 FY26
R316 | page 7 | line 431 | NUMBER | (159.35) | cash flow Redemption of debt securities, H1 FY27
R317 | page 7 | line 431 | NUMBER | (282.20) | cash flow Redemption of debt securities, H1 FY26
R318 | page 7 | line 432 | NUMBER | 2,368.63 | cash flow Proceeds from borrowings (other than debt securities), H1 FY27
R319 | page 7 | line 432 | NUMBER | 1,607.47 | cash flow Proceeds from borrowings (other than debt securities), H1 FY26
R320 | page 7 | line 433 | NUMBER | (1,728.59) | cash flow Repayment of borrowings (other than debt securities), H1 FY27
R321 | page 7 | line 433 | NUMBER | (1,008.10) | cash flow Repayment of borrowings (other than debt securities), H1 FY26
R322 | page 7 | line 434 | NUMBER | (277.75) | cash flow Finance cost on debt securities and borrowing, H1 FY27
R323 | page 7 | line 434 | NUMBER | (255.98) | cash flow Finance cost on debt securities and borrowing, H1 FY26
R324 | page 7 | line 435 | NUMBER | (9.91) | cash flow Payment of lease liabilities (incl. interest), H1 FY27
R325 | page 7 | line 435 | NUMBER | (8.57) | cash flow Payment of lease liabilities (incl. interest), H1 FY26
R326 | page 7 | line 436 | NUMBER | 549.90 | cash flow Net cash generated from financing activities (C), H1 FY27
R327 | page 7 | line 436 | NUMBER | 427.62 | cash flow Net cash generated from financing activities (C), H1 FY26
R328 | page 7 | line 439 | NUMBER | 230.83 | cash flow Net increase/(decrease) in cash and cash equivalents (A+B+C), H1 FY27
R329 | page 7 | line 439 | NUMBER | 213.96 | cash flow Net increase/(decrease) in cash and cash equivalents (A+B+C), H1 FY26
R330 | page 7 | line 440 | NUMBER | 620.38 | cash flow Cash and cash equivalents at beginning of period, H1 FY27
R331 | page 7 | line 440 | NUMBER | 931.16 | cash flow Cash and cash equivalents at beginning of period, H1 FY26
R332 | page 7 | line 441 | NUMBER | 851.21 | cash flow Cash and cash equivalents at end of period, H1 FY27
R333 | page 7 | line 441 | NUMBER | 1,145.12 | cash flow Cash and cash equivalents at end of period, H1 FY26
R334 | page 7 | line 443 | NUMBER | 10.54 | cash flow Cash in hand, H1 FY27
R335 | page 7 | line 443 | NUMBER | 10.14 | cash flow Cash in hand, H1 FY26
R336 | page 7 | line 444 | NUMBER | 460.63 | cash flow Balance with banks - on current account, H1 FY27
R337 | page 7 | line 444 | NUMBER | 422.26 | cash flow Balance with banks - on current account, H1 FY26
R338 | page 7 | line 445 | NUMBER | 380.04 | cash flow Deposits with original maturity <=3 months, H1 FY27
R339 | page 7 | line 445 | NUMBER | 712.72 | cash flow Deposits with original maturity <=3 months, H1 FY26
R340 | page 7 | line 446 | NUMBER | 851.21 | cash flow Total cash and cash equivalents, H1 FY27
R341 | page 7 | line 446 | NUMBER | 1,145.12 | cash flow Total cash and cash equivalents, H1 FY26
R342 | page 8 | line 515 | NUMBER | 0.04 | OTR 2.0 personal loans, exposure std at 31-Mar-26 (A)
R343 | page 8 | line 515 | NUMBER | - | OTR personal loans, slipped to NPA H1 FY27 [ZERO_STANDING]
R344 | page 8 | line 515 | NUMBER | - | OTR personal loans, written off H1 FY27 [ZERO_STANDING]
R345 | page 8 | line 515 | NUMBER | 0.01 | OTR personal loans, paid by borrowers H1 FY27
R346 | page 8 | line 515 | NUMBER | 0.02 | OTR personal loans, exposure std at 30-Sep-26
R347 | page 8 | line 516 | NUMBER | - | OTR corporate persons, all five columns dash [ZERO_STANDING]
R348 | page 8 | line 517 | NUMBER | - | OTR of which MSMEs, all five columns dash [ZERO_STANDING]
R349 | page 8 | line 518 | NUMBER | - | OTR others, all five columns dash [ZERO_STANDING]
R350 | page 8 | line 520 | NUMBER | 0.04 | OTR total, exposure std at 31-Mar-26 (A)
R351 | page 8 | line 520 | NUMBER | - | OTR total, slipped to NPA H1 FY27 [ZERO_STANDING]
R352 | page 8 | line 520 | NUMBER | - | OTR total, written off H1 FY27 [ZERO_STANDING]
R353 | page 8 | line 520 | NUMBER | 0.01 | OTR total, paid by borrowers H1 FY27
R354 | page 8 | line 520 | NUMBER | 0.02 | OTR total, exposure std at 30-Sep-26
R355 | page 8 | line 534 | NUMBER | 39.95 | loans (not in default) transferred by assignment H1 FY27, Rs crores
R356 | page 8 | line 536 | NUMBER | 10% | retention of beneficial economic interest (MRR)
R357 | page 8 | line 538 | NUMBER | 90.46 | weighted average residual maturity (unit not stated)
R358 | page 8 | line 540 | NUMBER | 10.33 | weighted average holding period (unit not stated)
R359 | page 8 | line 542 | NUMBER | 0% | coverage of tangible security
R360 | page 8 | line 548 | NUMBER | Nil | instances where transferred as agreed to replace loans [ZERO_STANDING]
R361 | page 8 | line 550 | NUMBER | Nil | transferred loans replaced [ZERO_STANDING]
R362 | page 8 | line 527 | NUMBER | RBI/DOR/2025-26/359DOR.ACC.REC.No.278/21.04.018/2025-26 | RBI notification reference, 28-Nov-25
R363 | page 9 | line 574 | NUMBER | 2 | number of CLA partners
R364 | page 9 | line 575 | NUMBER | 39096 | co-lending outstanding cases (No.)
R365 | page 9 | line 576 | NUMBER | 53.31 | co-lending gross outstanding amount (unit per page header Rs crores)
R366 | page 9 | line 577 | NUMBER | 31.27% | co-lending weighted average rate of interest
R367 | page 9 | line 583 | NUMBER | 42.70 | CLA performance, standard loans (unit not stated)
R368 | page 9 | line 584 | NUMBER | 10.61 | CLA performance, non-performing loans (unit not stated)
R369 | page 9 | line 586 | NUMBER | Nil | default loss guarantee [ZERO_STANDING]
R370 | page 9 | line 579 | NUMBER | - | co-lending fees paid during the quarter [ZERO_STANDING]
R371 | page 9 | line 580 | NUMBER | - | co-lending fees charged during the quarter [ZERO_STANDING]
R372 | page 9 | line 563 | NUMBER | RR2 | SR rating Arcil Retail Loan portfolio-077-A-Trust (India Ratings)
R373 | page 9 | line 564 | NUMBER | RR1+ | SR rating Arcil Retail Loan portfolio-077-B-Trust (Crisil Ratings)
R374 | page 9 | line 565 | NUMBER | RR2 | SR rating Arcil Trust-2025-013 (India Ratings)
R375 | page 9 | line 566 | NUMBER | RR1 | SR rating Arcil Trust-2026-031 (India Ratings)
R376 | page 9 | line 589 | NUMBER | 100% | shareholding in FAME
R377 | page 9 | line 597 | NUMBER | 100% | min. first exclusive charge cover on hypothecated book debts for listed secured NCDs
R378 | page 9 | line 604 | NUMBER | 78,294,571 | IPO equity shares total
R379 | page 9 | line 604 | NUMBER | Rs. 2 | IPO face value per share
R380 | page 9 | line 604 | NUMBER | Rs. 129 | IPO issue price per share
R381 | page 9 | line 604 | NUMBER | 55,038,759 | IPO fresh issue shares
R382 | page 9 | line 605 | NUMBER | 23,255,812 | IPO offer for sale shares
R383 | page 9 | line 605 | NUMBER | Rs. 672.24 Crores | net IPO proceeds from fresh issue
R384 | page 9 | line 606 | NUMBER | Rs. 37.76 Crores | estimated offer expenses incl. pre-IPO
R385 | page 9 | line 613 | NUMBER | 672.24 | IPO object: amount to be utilised (net), Rs crores
R386 | page 9 | line 613 | NUMBER | 672.24 | IPO object: amount utilised up to 30-Sep-26, Rs crores
R387 | page 9 | line 613 | NUMBER | 0.00 | IPO object: unutilised at 30-Sep-26, Rs crores [ZERO_STANDING]
R388 | page 9 | line 618 | NUMBER | 672.24 | IPO total amount to be utilised
R389 | page 9 | line 618 | NUMBER | 672.24 | IPO total amount utilised
R390 | page 9 | line 618 | NUMBER | 0.00 | IPO total unutilised [ZERO_STANDING]
R391 | page 9 | line 620 | NUMBER | Rs. 22.63 crores | unutilised offer expenses till 30-Sep-26
R392 | page 9 | line 623 | NUMBER | 5,04,152 | equity shares transferred by Aye Employees Welfare Trust on ESOP exercise H1 FY27
R393 | page 9 | line 624 | NUMBER | 3,913 | equity shares allotted on ESOP Plan 2020 exercise H1 FY27
R394 | page 9 | line 621 | NUMBER | 2016 & 2020 | ESOP plan years named
R395 | page 10 | line 652 | NUMBER | 2.25 | debt equity ratio (times), H1 FY27
R396 | page 10 | line 653 | NUMBER | 2,621.80 | net worth, H1 FY27 (Rs crores)
R397 | page 10 | line 655 | NUMBER | 161.22 | net profit after tax, H1 FY27
R398 | page 10 | line 656 | NUMBER | 67.30% | total debts to total assets, H1 FY27
R399 | page 10 | line 657 | NUMBER | 15.86% | net profit margin, H1 FY27
R400 | page 10 | line 659 | NUMBER | 6.53 | basic EPS, H1 FY27
R401 | page 10 | line 660 | NUMBER | 6.49 | diluted EPS, H1 FY27
R402 | page 10 | line 663 | NUMBER | 4.20% | gross stage III ratio / gross NPA, 30-Sep-26
R403 | page 10 | line 667 | NUMBER | 1.62% | net stage III ratio / net NPA, 30-Sep-26
R404 | page 10 | line 673 | NUMBER | 62.42% | provision coverage ratio, 30-Sep-26
R405 | page 10 | line 676 | NUMBER | 41.01% | capital to risk-weighted assets ratio, 30-Sep-26
R406 | page 10 | line 679 | NUMBER | 404.31% | liquidity coverage ratio, 30-Sep-26
R407 | page 11 | line 719 | NUMBER | 544699 | BSE scrip code
R408 | page 11 | line 726 | NUMBER | HO/17/11/12(2)2026-DDHS-POD1/1/22420/2026 | SEBI master circular no.
R409 | page 12 | line 798 | NUMBER | July 28, 2026 | debenture trustee agreement date
R410 | page 12 | line 798 | NUMBER | June 19, 2025 | debenture trustee agreement date
R411 | page 14 | line 932 | NUMBER | INE501X07588 | ISIN with covenant breach
R412 | page 15 | line 985 | NUMBER | 26133147REFYBG8327 | UDIN, security cover report
R413 | page 22 | line 1416 | NUMBER | SEBI/HO/DDHS/DDHS-PoD-l/P/CIR/2025/0000000103 | SEBI master circular no.
R414 | page 16 | line 1036 | NUMBER | 12.31 | Annexure 1 (Catalyst), PPE, col H
R415 | page 16 | line 1036 | NUMBER | 12.31 | Annexure 1 (Catalyst), PPE, col J
R416 | page 16 | line 1038 | NUMBER | 42.97 | Annexure 1 (Catalyst), Right of Use Assets, col H
R417 | page 16 | line 1038 | NUMBER | 42.97 | Annexure 1 (Catalyst), Right of Use Assets, col J
R418 | page 16 | line 1039 | NUMBER | 2.88 | Annexure 1 (Catalyst), Intangible Assets, col H
R419 | page 16 | line 1039 | NUMBER | 2.88 | Annexure 1 (Catalyst), Intangible Assets, col J
R420 | page 16 | line 1040 | NUMBER | 2.99 | Annexure 1 (Catalyst), Intangible Assets under Development, col H
R421 | page 16 | line 1040 | NUMBER | 2.99 | Annexure 1 (Catalyst), Intangible Assets under Development, col J
R422 | page 16 | line 1048 | NUMBER | 222.96 | Annexure 1 (Catalyst), Investments, col H
R423 | page 16 | line 1048 | NUMBER | 222.96 | Annexure 1 (Catalyst), Investments, col J
R424 | page 16 | line 1050 | NUMBER | 1,376.64 | Annexure 1 (Catalyst), Loans/receivables, col C
R425 | page 16 | line 1049 | NUMBER | 4,463.73 | Annexure 1 (Catalyst), Loans/receivables, col D
R426 | page 16 | line 1050 | NUMBER | 1,009.48 | Annexure 1 (Catalyst), Loans/receivables, col H
R427 | page 16 | line 1049 | NUMBER | 6,849.85 | Annexure 1 (Catalyst), Loans/receivables, col J
R428 | page 16 | line 1050 | NUMBER | 1,376.64 | Annexure 1 (Catalyst), Loans/receivables, col K-O (as printed)
R429 | page 16 | line 1050 | NUMBER | 1,376.64 | Annexure 1 (Catalyst), Loans/receivables, col K-O (as printed)
R430 | page 16 | line 1051 | NUMBER | 180.04 | Annexure 1 (Catalyst), Bank balances other than cash, col D
R431 | page 16 | line 1061 | NUMBER | 310.41 | Annexure 1 (Catalyst), Bank balances other than cash, col H
R432 | page 16 | line 1053 | NUMBER | 490.45 | Annexure 1 (Catalyst), Bank balances other than cash, col J
R433 | page 16 | line 1052 | NUMBER | 851.21 | Annexure 1 (Catalyst), Cash and cash equivalents, col H
R434 | page 16 | line 1059 | NUMBER | 851.21 | Annexure 1 (Catalyst), Cash and cash equivalents, col J
R435 | page 16 | line 1063 | NUMBER | 297.89 | Annexure 1 (Catalyst), Others, col H
R436 | page 16 | line 1063 | NUMBER | 297.89 | Annexure 1 (Catalyst), Others, col J
R437 | page 16 | line 1065 | NUMBER | 1,376.64 | Annexure 1 (Catalyst), Total assets, col C
R438 | page 16 | line 1065 | NUMBER | 4,643.77 | Annexure 1 (Catalyst), Total assets, col D
R439 | page 16 | line 1065 | NUMBER | 2,753.10 | Annexure 1 (Catalyst), Total assets, col H
R440 | page 16 | line 1064 | NUMBER | 8,773.51 | Annexure 1 (Catalyst), Total assets, col J
R441 | page 16 | line 1065 | NUMBER | 1,376.64 | Annexure 1 (Catalyst), Total assets, col K-O (as printed)
R442 | page 16 | line 1065 | NUMBER | 1,376.64 | Annexure 1 (Catalyst), Total assets, col K-O (as printed)
R443 | page 16 | line 1068 | NUMBER | 1,261.45 | Annexure 1 (Catalyst), Listed NCD (debt securities to which certificate pertains), col C
R444 | page 16 | line 1068 | NUMBER | 1,261.45 | Annexure 1 (Catalyst), Listed NCD, col J
R445 | page 16 | line 1066 | NUMBER | 1,261.45 | Annexure 1 (Catalyst), Listed NCD, col K-O (as printed)
R446 | page 16 | line 1066 | NUMBER | 1,261.45 | Annexure 1 (Catalyst), Listed NCD, col K-O (as printed)
R447 | page 16 | line 1079 | NUMBER | 2,107.60 | Annexure 1 (Catalyst), Borrowings Bank**, col D
R448 | page 16 | line 1079 | NUMBER | 2,107.60 | Annexure 1 (Catalyst), Borrowings Bank**, col J
R449 | page 16 | line 1080 | NUMBER | 9.70 | Annexure 1 (Catalyst), Debt Securities*, col D
R450 | page 16 | line 1069 | NUMBER | 9.70 | Annexure 1 (Catalyst), Debt Securities*, col J
R451 | page 16 | line 1082 | NUMBER | 2,334.28 | Annexure 1 (Catalyst), Others**, col D
R452 | page 16 | line 1083 | NUMBER | 145.29 | Annexure 1 (Catalyst), Others**, col H
R453 | page 16 | line 1071 | NUMBER | 2,479.57 | Annexure 1 (Catalyst), Others**, col J
R454 | page 16 | line 1072 | NUMBER | 46.61 | Annexure 1 (Catalyst), Lease Liabilities, col H
R455 | page 16 | line 1087 | NUMBER | 46.61 | Annexure 1 (Catalyst), Lease Liabilities, col J
R456 | page 16 | line 1073 | NUMBER | 58.68 | Annexure 1 (Catalyst), Provisions, col H
R457 | page 16 | line 1089 | NUMBER | 58.68 | Annexure 1 (Catalyst), Provisions, col J
R458 | page 16 | line 1074 | NUMBER | 115.29 | Annexure 1 (Catalyst), Others, col H
R459 | page 16 | line 1091 | NUMBER | 115.29 | Annexure 1 (Catalyst), Others, col J
R460 | page 16 | line 1065 | NUMBER | 1,261.45 | Annexure 1 (Catalyst), Total liabilities, col C
R461 | page 16 | line 1084 | NUMBER | 4,451.58 | Annexure 1 (Catalyst), Total liabilities, col D
R462 | page 16 | line 1093 | NUMBER | 365.87 | Annexure 1 (Catalyst), Total liabilities, col H
R463 | page 16 | line 1076 | NUMBER | 6,078.90 | Annexure 1 (Catalyst), Total liabilities, col J
R464 | page 16 | line 1066 | NUMBER | 1,261.45 | Annexure 1 (Catalyst), Total liabilities, col K-O (as printed)
R465 | page 16 | line 1066 | NUMBER | 1,261.45 | Annexure 1 (Catalyst), Total liabilities, col K-O (as printed)
R466 | page 16 | line 1097 | NUMBER | 1.1 | Annexure 1 (Catalyst), Exclusive Security Cover Ratio (printed 1.1), col ratio
R467 | page 16 | line 1097 | NUMBER | 1.1 | Annexure 1 (Catalyst), Pari-Passu Security Cover Ratio (printed 1.1), col ratio
R468 | page 16 | line 1105 | NUMBER | Rs. 455 crores | Banks/NBFC borrowings for which corresponding security is not maintained due to time limit granted by lenders
R469 | page 18 | line 1180 | NUMBER | 12.31 | Annexure 2 (Mitcon), PPE, col H
R470 | page 18 | line 1180 | NUMBER | 12.31 | Annexure 2 (Mitcon), PPE, col J
R471 | page 18 | line 1182 | NUMBER | 42.97 | Annexure 2 (Mitcon), Right of Use Assets, col H
R472 | page 18 | line 1183 | NUMBER | 42.97 | Annexure 2 (Mitcon), Right of Use Assets, col J
R473 | page 18 | line 1185 | NUMBER | 2.88 | Annexure 2 (Mitcon), Intangible Assets, col H
R474 | page 18 | line 1185 | NUMBER | 2.88 | Annexure 2 (Mitcon), Intangible Assets, col J
R475 | page 18 | line 1186 | NUMBER | 2.99 | Annexure 2 (Mitcon), Intangible Assets under Development, col H
R476 | page 18 | line 1186 | NUMBER | 2.99 | Annexure 2 (Mitcon), Intangible Assets under Development, col J
R477 | page 18 | line 1192 | NUMBER | 222.96 | Annexure 2 (Mitcon), Investments, col H
R478 | page 18 | line 1192 | NUMBER | 222.96 | Annexure 2 (Mitcon), Investments, col J
R479 | page 18 | line 1193 | NUMBER | 22.02 | Annexure 2 (Mitcon), Loans/receivables, col C
R480 | page 18 | line 1193 | NUMBER | 5,818.35 | Annexure 2 (Mitcon), Loans/receivables, col D
R481 | page 18 | line 1194 | NUMBER | 1,009.48 | Annexure 2 (Mitcon), Loans/receivables, col H
R482 | page 18 | line 1194 | NUMBER | 6,849.85 | Annexure 2 (Mitcon), Loans/receivables, col J
R483 | page 18 | line 1194 | NUMBER | 22.02 | Annexure 2 (Mitcon), Loans/receivables, col K-O (as printed)
R484 | page 18 | line 1194 | NUMBER | 22.02 | Annexure 2 (Mitcon), Loans/receivables, col K-O (as printed)
R485 | page 18 | line 1198 | NUMBER | 180.04 | Annexure 2 (Mitcon), Bank balances other than cash, col D
R486 | page 18 | line 1205 | NUMBER | 310.41 | Annexure 2 (Mitcon), Bank balances other than cash, col H
R487 | page 18 | line 1200 | NUMBER | 490.45 | Annexure 2 (Mitcon), Bank balances other than cash, col J
R488 | page 18 | line 1203 | NUMBER | 851.21 (printed 8S1.21) | Annexure 2 (Mitcon), Cash and cash equivalents, col H
R489 | page 18 | line 1198 | NUMBER | 851.21 | Annexure 2 (Mitcon), Cash and cash equivalents, col J
R490 | page 18 | line 1207 | NUMBER | 297.89 | Annexure 2 (Mitcon), Others, col H
R491 | page 18 | line 1207 | NUMBER | 297.89 | Annexure 2 (Mitcon), Others, col J
R492 | page 18 | line 1209 | NUMBER | 22.02 | Annexure 2 (Mitcon), Total assets, col C
R493 | page 18 | line 1208 | NUMBER | 5,998.39 | Annexure 2 (Mitcon), Total assets, col D
R494 | page 18 | line 1209 | NUMBER | 2,753.10 | Annexure 2 (Mitcon), Total assets, col H
R495 | page 18 | line 1208 | NUMBER | 8,773.51 | Annexure 2 (Mitcon), Total assets, col J
R496 | page 18 | line 1209 | NUMBER | 22.02 | Annexure 2 (Mitcon), Total assets, col K-O (as printed)
R497 | page 18 | line 1208 | NUMBER | 22.02 | Annexure 2 (Mitcon), Total assets, col K-O (as printed)
R498 | page 18 | line 1217 | NUMBER | 20.02 | Annexure 2 (Mitcon), Listed NCD (Annexure 2A), col C
R499 | page 18 | line 1217 | NUMBER | 20.02 | Annexure 2 (Mitcon), Listed NCD, col J
R500 | page 18 | line 1210 | NUMBER | 20.02 | Annexure 2 (Mitcon), Listed NCD, col K-O (as printed)
R501 | page 18 | line 1212 | NUMBER | 20.02 | Annexure 2 (Mitcon), Listed NCD, col K-O (as printed)
R502 | page 18 | line 1215 | NUMBER | 2,107.60 | Annexure 2 (Mitcon), Borrowings Bank**, col D
R503 | page 18 | line 1215 | NUMBER | 2,107.60 | Annexure 2 (Mitcon), Borrowings Bank**, col J
R504 | page 18 | line 1216 | NUMBER | 1,251.13 | Annexure 2 (Mitcon), Debt Securities*, col D
R505 | page 18 | line 1216 | NUMBER | 1,251.13 | Annexure 2 (Mitcon), Debt Securities*, col J
R506 | page 18 | line 1228 | NUMBER | 2,334.28 | Annexure 2 (Mitcon), Others**, col D
R507 | page 18 | line 1232 | NUMBER | 145.29 | Annexure 2 (Mitcon), Others**, col H
R508 | page 18 | line 1217 | NUMBER | 2,479.57 | Annexure 2 (Mitcon), Others**, col J
R509 | page 18 | line 1236 | NUMBER | 46.61 | Annexure 2 (Mitcon), Lease Liabilities, col H
R510 | page 18 | line 1236 | NUMBER | 46.61 | Annexure 2 (Mitcon), Lease Liabilities, col J
R511 | page 18 | line 1238 | NUMBER | 58.68 | Annexure 2 (Mitcon), Provisions, col H
R512 | page 18 | line 1238 | NUMBER | 58.68 | Annexure 2 (Mitcon), Provisions, col J
R513 | page 18 | line 1240 | NUMBER | 115.29 | Annexure 2 (Mitcon), Others, col H
R514 | page 18 | line 1240 | NUMBER | 115.29 | Annexure 2 (Mitcon), Others, col J
R515 | page 18 | line 1242 | NUMBER | 20.02 | Annexure 2 (Mitcon), Total liabilities, col C
R516 | page 18 | line 1242 | NUMBER | 5,693.01 | Annexure 2 (Mitcon), Total liabilities, col D
R517 | page 18 | line 1242 | NUMBER | 365.87 | Annexure 2 (Mitcon), Total liabilities, col H
R518 | page 18 | line 1221 | NUMBER | 6,078.90 | Annexure 2 (Mitcon), Total liabilities, col J
R519 | page 18 | line 1242 | NUMBER | 20.02 | Annexure 2 (Mitcon), Total liabilities, col K-O (as printed)
R520 | page 18 | line 1242 | NUMBER | 20.02 | Annexure 2 (Mitcon), Total liabilities, col K-O (as printed)
R521 | page 18 | line 1246 | NUMBER | 1.1 | Annexure 2 (Mitcon), Exclusive Security Cover Ratio (printed 1.1), col ratio
R522 | page 18 | line 1246 | NUMBER | 1.1 | Annexure 2 (Mitcon), Pari-Passu Security Cover Ratio (printed 1.1), col ratio
R523 | page 17 | line 1116 | NUMBER | 49.01 | Annexure 1A S.No 1 amount outstanding, INE501X07570 issued 30-04-2024 (pairing from raw text order)
R524 | page 17 | line 1117 | NUMBER | 51.02 | Annexure 1A S.No 2 amount outstanding, INE501X07570 issued 13-06-2024 (pairing from raw text order)
R525 | page 17 | line 1118 | NUMBER | 206.85 | Annexure 1A S.No 3 amount outstanding, INE501X07596 issued 31-05-2024 (pairing from raw text order)
R526 | page 17 | line 1119 | NUMBER | 143.94 | Annexure 1A S.No 4 amount outstanding, INE501X07737 issued 25-06-2026 (pairing from raw text order)
R527 | page 17 | line 1120 | NUMBER | 75.47 | Annexure 1A S.No 5 amount outstanding, INE501X07638 issued 09-10-2024 (pairing from raw text order)
R528 | page 17 | line 1121 | NUMBER | 25.10 | Annexure 1A S.No 6 amount outstanding, INE501X07588 issued 17-05-2024 (pairing from raw text order)
R529 | page 17 | line 1122 | NUMBER | 220.12 | Annexure 1A S.No 7 amount outstanding, INE501X07745 issued 29-07-2026 (pairing from raw text order)
R530 | page 17 | line 1123 | NUMBER | 60.32 | Annexure 1A S.No 8 amount outstanding, INE501X07711 issued 12-09-2025 (pairing from raw text order)
R531 | page 17 | line 1124 | NUMBER | 150.78 | Annexure 1A S.No 9 amount outstanding, INE501X07729 issued 12-09-2025 (pairing from raw text order)
R532 | page 17 | line 1125 | NUMBER | 30.12 | Annexure 1A S.No 10 amount outstanding, INE501X07588 issued 15-07-2025 (pairing from raw text order)
R533 | page 17 | line 1126 | NUMBER | 50.01 | Annexure 1A S.No 11 amount outstanding, INE501X07703 issued 30-06-2025 (pairing from raw text order)
R534 | page 17 | line 1127 | NUMBER | 25.01 | Annexure 1A S.No 12 amount outstanding, INE501X07695 issued 30-06-2025 (pairing from raw text order)
R535 | page 17 | line 1128 | NUMBER | 40.12 | Annexure 1A S.No 13 amount outstanding, INE501X07679 issued 20-03-2025 (pairing from raw text order)
R536 | page 17 | line 1129 | NUMBER | 28.33 | Annexure 1A S.No 14 amount outstanding, INE501X07646 issued 31-12-2024 (pairing from raw text order)
R537 | page 17 | line 1130 | NUMBER | 25.00 | Annexure 1A S.No 15 amount outstanding, INE501X07653 issued 31-12-2024 (pairing from raw text order)
R538 | page 17 | line 1131 | NUMBER | 80.24 | Annexure 1A S.No 16 amount outstanding, INE501X07661 issued 20-03-2025 (pairing from raw text order)
R539 | page 17 | line 1134 | NUMBER | 1,261.45 | Annexure 1A total amount outstanding
R540 | page 19 | line 1257 | NUMBER | 20.02 | Annexure 2A S.No 1 amount outstanding, INE501X07687 issued 20-06-2025
R541 | page 19 | line 1258 | NUMBER | 20.02 | Annexure 2A total amount outstanding
R542 | page 20 | line 1275 | NUMBER | 10.50% | Annex 3 NCD INE501X07570 coupon
R543 | page 20 | line 1279 | NUMBER | 1,00,000 | Annex 3 INE501X07570 face value (Rs)
R544 | page 20 | line 1283 | NUMBER | 10.50% | Annex 3 NCD INE501X07588 coupon
R545 | page 20 | line 1287 | NUMBER | 11.30% | Annex 3 NCD INE501X07596 coupon
R546 | page 20 | line 1290 | NUMBER | 1,00,000 | Annex 3 INE501X07596 face value (Rs)
R547 | page 20 | line 1293 | NUMBER | 10.50% | Annex 3 NCD INE501X07638 coupon
R548 | page 20 | line 1299 | NUMBER | 10.10% | Annex 3 NCD INE501X07646 coupon
R549 | page 20 | line 1303 | NUMBER | 77,777.78 | Annex 3 INE501X07646 face value (Rs)
R550 | page 20 | line 1305 | NUMBER | 9.95% | Annex 3 NCD INE501X07653 coupon
R551 | page 20 | line 1312 | NUMBER | 9.95% | Annex 3 NCD INE501X07661 coupon
R552 | page 20 | line 1317 | NUMBER | 10.35% | Annex 3 NCD INE501X07679 coupon
R553 | page 21 | line 1343 | NUMBER | 11.00% | Annex 3 NCD INE501X07687 coupon
R554 | page 21 | line 1349 | NUMBER | 10.25% | Annex 3 NCD INE501X07703 coupon
R555 | page 21 | line 1355 | NUMBER | 10.40% | Annex 3 NCD INE501X07695 coupon
R556 | page 21 | line 1361 | NUMBER | 10.10% | Annex 3 NCD INE501X07711 coupon
R557 | page 21 | line 1367 | NUMBER | 10.05% | Annex 3 NCD INE501X07729 coupon
R558 | page 21 | line 1372 | NUMBER | 10.49% | Annex 3 NCD INE501X07737 coupon
R559 | page 21 | line 1377 | NUMBER | 9.75% | Annex 3 NCD INE501X07745 coupon
R560 | page 21 | line 1359 | NUMBER | 1,00,000 | Annex 3 face value (Rs) for ISINs 07687-07745 rows
R561 | page 23 | line 1471 | NUMBER | 140 | INE501X07737 amount raised (Rs crores)
R562 | page 23 | line 1471 | NUMBER | 140 | INE501X07737 funds utilized (Rs crores)
R563 | page 23 | line 1473 | NUMBER | 220 | INE501X07745 amount raised (Rs crores)
R564 | page 23 | line 1473 | NUMBER | 150 | INE501X07745 funds utilized (Rs crores, as printed)
R565 | page 23 | line 1487 | NUMBER | 140 | amount raised 25-06-2026 (Rs crores)
R566 | page 23 | line 1487 | NUMBER | 220 | amount raised 29-07-2026 (Rs crores)
R567 | page 23 | line 1491 | NUMBER | No | deviation/variation in use of funds raised (flag)
R568 | page 23 | line 1469 | NUMBER | 1 2 3 4 5 6 7 8 9 10 | column index numbers (decorative)

## ENTITY
R569 | page 1 | line 18 | ENTITY | Aye Finance Limited (formerly Aye Finance Private Limited), CIN L65921DL1993PLC283660 | issuer / listed company
R570 | page 1 | line 25 | ENTITY | BSE Limited | stock exchange addressee, scrip 544699
R571 | page 1 | line 25 | ENTITY | National Stock Exchange of India Limited | stock exchange addressee, symbol AYE
R572 | page 1 | line 62 | ENTITY | Anuj Jain | Company Secretary & Compliance Officer
R573 | page 1 | line 62 | ENTITY | Sanjay Sharma (DIN 03337545) | Managing Director, signs statements
R574 | page 2 | line 92 | ENTITY | M S K A & Associates LLP (formerly M S K A & Associates) | current statutory auditor / reviewer
R575 | page 2 | line 107 | ENTITY | Reserve Bank of India (RBI) | regulator
R576 | page 2 | line 123 | ENTITY | Institute of Chartered Accountants of India (ICAI) | standards body
R577 | page 3 | line 155 | ENTITY | Aye Employee Welfare Trust | unreviewed entity included in the statement
R578 | page 3 | line 171 | ENTITY | another auditor (reports dated July 22, 2026; November 10, 2025; April 27, 2026) | prior auditor, unnamed on p3
R579 | page 3 | line 186 | ENTITY | Ajit Burli | audit partner, M.No. 133147
R580 | page 8 | line 486 | ENTITY | S S Kothari Mehta & Co. LLP | previous statutory auditors
R581 | page 8 | line 479 | ENTITY | NBFC-ML (Middle Layer NBFC) registration with RBI | regulatory category
R582 | page 8 | line 515 | ENTITY | OTR 2.0 / Resolution framework 2.0 (RBI circulars Aug 06, 2020 and May 5, 2021) | COVID restructuring framework
R583 | page 9 | line 560 | ENTITY | Arcil (Asset Reconstruction Co.) trusts: Retail Loan portfolio-077-A-Trust, 077-B-Trust, Trust-2025-013, Trust-2026-031 | security receipts held
R584 | page 9 | line 562 | ENTITY | India Ratings | rating agency for SRs
R585 | page 9 | line 563 | ENTITY | Crisil Ratings | rating agency for SR (077-B-Trust)
R586 | page 9 | line 589 | ENTITY | Foundation for Advancement of Micro Enterprises (FAME) | 100% owned Section 8 company, not consolidated
R587 | page 9 | line 603 | ENTITY | National Stock Exchange of India Limited and BSE Limited | IPO listing venues, listed Feb 16, 2026
R588 | page 9 | line 621 | ENTITY | Aye Finance Employees Welfare Trust | ESOP transfer entity (ESOP Plan 2016 & 2020)
R589 | page 9 | line 603 | ENTITY | selling shareholders (unnamed) | IPO offer for sale
R590 | page 9 | line 574 | ENTITY | CLA partners (2, unnamed) | co-lending partners
R591 | page 12 | line 777 | ENTITY | Catalyst Trusteeship Limited | debenture trustee
R592 | page 12 | line 777 | ENTITY | Mitcon Credentia Trusteeship Services Limited | debenture trustee
R593 | page 1 | line 80 | ENTITY | SEBI (Listing Regulations; Master Circulars) | regulator
R594 | page 14 | line 908 | ENTITY | Ministry of Corporate Affairs (MCA), Form CHG-1 | registry filing referenced
R595 | page 20 | line 1273 | ENTITY | INE501X07570 | NCD ISIN (Annexure 3 / 1A / 2A)
R596 | page 20 | line 1273 | ENTITY | INE501X07588 | NCD ISIN (Annexure 3 / 1A / 2A)
R597 | page 20 | line 1273 | ENTITY | INE501X07596 | NCD ISIN (Annexure 3 / 1A / 2A)
R598 | page 20 | line 1273 | ENTITY | INE501X07638 | NCD ISIN (Annexure 3 / 1A / 2A)
R599 | page 20 | line 1273 | ENTITY | INE501X07646 | NCD ISIN (Annexure 3 / 1A / 2A)
R600 | page 20 | line 1273 | ENTITY | INE501X07653 | NCD ISIN (Annexure 3 / 1A / 2A)
R601 | page 20 | line 1273 | ENTITY | INE501X07661 | NCD ISIN (Annexure 3 / 1A / 2A)
R602 | page 20 | line 1273 | ENTITY | INE501X07679 | NCD ISIN (Annexure 3 / 1A / 2A)
R603 | page 21 | line 1343 | ENTITY | INE501X07687 | NCD ISIN (Annexure 3 / 1A / 2A)
R604 | page 21 | line 1343 | ENTITY | INE501X07695 | NCD ISIN (Annexure 3 / 1A / 2A)
R605 | page 21 | line 1343 | ENTITY | INE501X07703 | NCD ISIN (Annexure 3 / 1A / 2A)
R606 | page 21 | line 1343 | ENTITY | INE501X07711 | NCD ISIN (Annexure 3 / 1A / 2A)
R607 | page 21 | line 1343 | ENTITY | INE501X07729 | NCD ISIN (Annexure 3 / 1A / 2A)
R608 | page 21 | line 1343 | ENTITY | INE501X07737 | NCD ISIN (Annexure 3 / 1A / 2A)
R609 | page 21 | line 1343 | ENTITY | INE501X07745 | NCD ISIN (Annexure 3 / 1A / 2A)
R610 | page 23 | line 1470 | ENTITY | INE501X07737 and INE501X07745 private placement NCDs | Annexure I Reg 52(7) utilisation statement
R611 | page 22 | line 1394 | ENTITY | Company website www.ayefin.com | company website

## FORWARD
R612 | page 1 | line 47 | FORWARD | Trading Window for dealing in securities of the Company shall remain closed until 48 hours from this announcement i.e. Friday, October 23, 2026 | trading window closure
R613 | page 1 | line 43 | FORWARD | the Meeting is continuing for consideration of other agenda items | board meeting continues
R614 | page 1 | line 84 | FORWARD | disclosure of Related Party Transactions for the half year ended September 30, 2026 ... will be filed along with XBRL for financial results | RPT disclosure to be filed
R615 | page 8 | line 494 | FORWARD | Any application guidance/clarification/directions issued by the Reserve Bank of India or other Regulators are implemented as and when they are issued/applicable | regulatory implementation approach
R616 | page 16 | line 1105 | FORWARD | Banks/NBFC borrowings worth Rs. 455 crores for which corresponding security is not maintained due to time limit granted by the lenders | security to be created within lender time limit (timing not stated)
R617 | page 20 | line 1286 | FORWARD | requisite waiver received (covenant 10.3(a) PAR 90 + write-offs / Gross Loan Portfolio, INE501X07588) | waiver; forward status not stated
R618 | page 9 | line 620 | FORWARD | Out of total estimated offer expense, Company has unutilised Rs. 22.63 crores till period ended September 30, 2026 | unutilised offer expenses balance remaining

## DATE
R619 | page 1 | line 23 | DATE | October 21, 2026 | Board meeting and letter date
R620 | page 1 | line 36 | DATE | October 12, 2026 | earlier intimation date
R621 | page 1 | line 38 | DATE | quarter and year to date ended September 30, 2026 | results period
R622 | page 1 | line 43 | DATE | 11:15 A.M. (IST); 11:21 A.M. (IST) | meeting commenced; results approved
R623 | page 1 | line 48 | DATE | Friday, October 23, 2026 | trading window reopening reference
R624 | page 1 | line 81 | DATE | September 28, 2026 | SEBI Master Circular for Debenture Trustees date
R625 | page 1 | line 83 | DATE | July 11, 2025 | SEBI Master Circular date (Reg 52(7)/(7A))
R626 | page 2 | line 100 | DATE | quarter and half year ended September 30, 2026 | review period
R627 | page 3 | line 157 | DATE | as at September 30, 2026; quarter ended 30 September 2026; half year ended September 30, 2026 | Trust interim info dates
R628 | page 3 | line 169 | DATE | quarter ended June 30, 2026; quarter and half year ended September 30, 2025; year ended 31 March 2026 | prior periods reviewed by other auditor
R629 | page 3 | line 171 | DATE | July 22, 2026; November 10, 2025; April 27, 2026 | dates of prior auditor reports
R630 | page 3 | line 192 | DATE | October 21, 2026 (Mumbai) | review report date
R631 | page 4 | line 206 | DATE | as at September 30, 2026; as at March 31, 2026 | balance sheet dates
R632 | page 4 | line 260 | DATE | October 21, 2026 (Gurugram) | signing date
R633 | page 5 | line 283 | DATE | Quarter ended September 30, 2026; June 30, 2026; September 30, 2025; Half year ended September 30, 2026; September 30, 2025; Year ended March 31, 2026 | P&L column periods
R634 | page 6 | line 359 | DATE | half year ended September 30, 2026; September 30, 2025 | cash flow periods
R635 | page 8 | line 481 | DATE | 21 October 2026 | auditor unmodified conclusion date
R636 | page 8 | line 496 | DATE | RBI circular dated August 06, 2020 and May 5, 2021; as at September 30, 2026; position as at March 31, 2026 | OTR 2.0 dates
R637 | page 8 | line 527 | DATE | November 28, 2025 | RBI notification date
R638 | page 9 | line 603 | DATE | February 16, 2026 | equity listing date on NSE and BSE
R639 | page 9 | line 620 | DATE | September 30, 2026 | IPO proceeds utilisation reporting date
R640 | page 10 | line 646 | DATE | as at September 30, 2026; half year ended September 30, 2026 | Reg 52(4) disclosure date
R641 | page 11 | line 726 | DATE | September 28,2026; Oct 21, 2026 | SEBI circular; letter date
R642 | page 12 | line 798 | DATE | July 28, 2026 and June 19, 2025 | agreements with Debenture Trustees
R643 | page 15 | line 987 | DATE | October 21, 2026 (Mumbai) | security cover report date
R644 | page 17 | line 1116 | DATE | 30-04-2024 | Annexure 1A issuance date, S.No 1 INE501X07570
R645 | page 17 | line 1117 | DATE | 13-06-2024 | Annexure 1A issuance date, S.No 2 INE501X07570
R646 | page 17 | line 1118 | DATE | 31-05-2024 | Annexure 1A issuance date, S.No 3 INE501X07596
R647 | page 17 | line 1119 | DATE | 25-06-2026 | Annexure 1A issuance date, S.No 4 INE501X07737
R648 | page 17 | line 1120 | DATE | 09-10-2024 | Annexure 1A issuance date, S.No 5 INE501X07638
R649 | page 17 | line 1121 | DATE | 17-05-2024 | Annexure 1A issuance date, S.No 6 INE501X07588
R650 | page 17 | line 1122 | DATE | 29-07-2026 | Annexure 1A issuance date, S.No 7 INE501X07745
R651 | page 17 | line 1123 | DATE | 12-09-2025 | Annexure 1A issuance date, S.No 8 INE501X07711
R652 | page 17 | line 1124 | DATE | 12-09-2025 | Annexure 1A issuance date, S.No 9 INE501X07729
R653 | page 17 | line 1125 | DATE | 15-07-2025 | Annexure 1A issuance date, S.No 10 INE501X07588
R654 | page 17 | line 1126 | DATE | 30-06-2025 | Annexure 1A issuance date, S.No 11 INE501X07703
R655 | page 17 | line 1127 | DATE | 30-06-2025 | Annexure 1A issuance date, S.No 12 INE501X07695
R656 | page 17 | line 1128 | DATE | 20-03-2025 | Annexure 1A issuance date, S.No 13 INE501X07679
R657 | page 17 | line 1129 | DATE | 31-12-2024 | Annexure 1A issuance date, S.No 14 INE501X07646
R658 | page 17 | line 1130 | DATE | 31-12-2024 | Annexure 1A issuance date, S.No 15 INE501X07653
R659 | page 17 | line 1131 | DATE | 20-03-2025 | Annexure 1A issuance date, S.No 16 INE501X07661
R660 | page 19 | line 1257 | DATE | 20-06-2025 | Annexure 2A issuance date INE501X07687
R661 | page 16 | line 1109 | DATE | 21 October, 2026 | Annexure 1 date
R662 | page 20 | line 1275 | DATE | 30-APR-27 | Annexure 3 maturity INE501X07570
R663 | page 20 | line 1276 | DATE | April 29, 2024 and June 12, 2024 | Annexure 3 trust deed dates INE501X07570
R664 | page 20 | line 1282 | DATE | 17-NOV-26 | Annexure 3 maturity INE501X07588
R665 | page 20 | line 1283 | DATE | May 16, 2024 and July 14, 2025 | Annexure 3 trust deed dates INE501X07588
R666 | page 20 | line 1288 | DATE | 30-MAY-29 | Annexure 3 maturity INE501X07596
R667 | page 20 | line 1290 | DATE | May 28, 2024 | Annexure 3 trust deed date INE501X07596
R668 | page 20 | line 1294 | DATE | 09-OCT-27 | Annexure 3 maturity INE501X07638
R669 | page 20 | line 1292 | DATE | October 7, 2024 | Annexure 3 trust deed date INE501X07638
R670 | page 20 | line 1300 | DATE | 31-MAR-27 | Annexure 3 maturity INE501X07646
R671 | page 20 | line 1295 | DATE | December 30, 2024 | Annexure 3 trust deed date INE501X07646/07653
R672 | page 20 | line 1306 | DATE | 31-DEC-26 | Annexure 3 maturity INE501X07653
R673 | page 20 | line 1301 | DATE | March 19, 2025 | Annexure 3 trust deed date INE501X07661/07679
R674 | page 20 | line 1312 | DATE | 20-MAR-27 | Annexure 3 maturity INE501X07661
R675 | page 20 | line 1318 | DATE | 20-DEC-27 | Annexure 3 maturity INE501X07679
R676 | page 21 | line 1344 | DATE | 17-APR-29 | Annexure 3 maturity INE501X07687
R677 | page 21 | line 1343 | DATE | June 19, 2025 | Annexure 3 trust deed date INE501X07687
R678 | page 21 | line 1350 | DATE | 30-JUN-27 | Annexure 3 maturity INE501X07703
R679 | page 21 | line 1347 | DATE | June 27, 2025 | Annexure 3 trust deed date INE501X07703/07695
R680 | page 21 | line 1355 | DATE | 3O-MAR-28 (printed) | Annexure 3 maturity INE501X07695
R681 | page 21 | line 1362 | DATE | 12-MAR-28 | Annexure 3 maturity INE501X07711
R682 | page 21 | line 1352 | DATE | September 11, 2025 | Annexure 3 trust deed date INE501X07711/07729
R683 | page 21 | line 1368 | DATE | 12-SEP-27 | Annexure 3 maturity INE501X07729
R684 | page 21 | line 1373 | DATE | 25-JUN-31 | Annexure 3 maturity INE501X07737
R685 | page 21 | line 1355 | DATE | June 19,2026 | Annexure 3 trust deed date INE501X07737
R686 | page 21 | line 1378 | DATE | 28-JUL-28 | Annexure 3 maturity INE501X07745
R687 | page 21 | line 1356 | DATE | July 28, 2026 | Annexure 3 trust deed date INE501X07745
R688 | page 22 | line 1409 | DATE | quarter & year to date ended September 30, 2026 | Reg 52(7)/(7A) statement period
R689 | page 22 | line 1399 | DATE | October 21, 2026 | letter date
R690 | page 22 | line 1416 | DATE | July 11, 2025 | SEBI master circular date
R691 | page 23 | line 1464 | DATE | 25-06-2026 | date of raising funds INE501X07737
R692 | page 23 | line 1466 | DATE | 29-07-2026 | date of raising funds INE501X07745
R693 | page 23 | line 1489 | DATE | quarter ended September 30, 2026 | report filed for quarter

## QUALIFIER
R694 | page 1 | line 43 | QUALIFIER | Meeting continuing after results approval for other agenda items | results approved 11:21 A.M., meeting continues
R695 | page 2 | line 99 | QUALIFIER | Review report is on UNAUDITED results (limited review, moderate assurance; "we do not express an audit opinion") | review not audit
R696 | page 3 | line 155 | QUALIFIER | Trust interim financial information "has not been reviewed by its auditor"; furnished by Management; "not material to the Company"; total assets Rs 1.93 cr, revenue Rs 0.12/0.48 cr, PAT Rs 0.12/0.47 cr | unreviewed component included in the Statement
R697 | page 3 | line 166 | QUALIFIER | Our conclusion is not modified in respect of the above matter (Trust) | emphasis, no modification
R698 | page 3 | line 169 | QUALIFIER | Q1 FY27, Q2 FY26, H1 FY26 results reviewed and FY26 audited by another auditor (unmodified) | comparatives from predecessor auditor
R699 | page 3 | line 175 | QUALIFIER | Our conclusion is not modified in respect of above matter (predecessor auditor figures) | 
R700 | page 4 | line 212 | QUALIFIER | Balance sheet 30-Sep-26 column is Unaudited; 31-Mar-26 column is Audited | column status
R701 | page 4 | line 208 | QUALIFIER | (All amounts are in Rs. crores unless otherwise stated) | unit statement
R702 | page 5 | line 283 | QUALIFIER | Q2 FY27, Q1 FY27, Q2 FY26, H1 FY27, H1 FY26 columns Unaudited; year ended 31-Mar-26 Audited | column status
R703 | page 5 | line 336 | QUALIFIER | Marker * on "10 Earnings per share *" | asterisk marker
R704 | page 5 | line 342 | QUALIFIER | * Earnings per share for the interim periods are not annualised | EPS footnote
R705 | page 5 | line 281 | QUALIFIER | (All amounts are in Rs. crores unless otherwise stated) | unit statement
R706 | page 6 | line 357 | QUALIFIER | (All amounts are in Rs. crores unless otherwise stated); cash flow columns Unaudited | unit statement
R707 | page 6 | line 370 | QUALIFIER | "Profit on sale of mutual fund units" current-period cell reads "0-64)" in text layer | text-layer garble
R708 | page 7 | line 449 | QUALIFIER | Note: The above cash flow statement has been prepared under the "Indirect Method" as set out in Indian Accounting Standard (Ind AS) 7 - "Statement of Cash Flows". | method note
R709 | page 7 | line 428 | QUALIFIER | Financing section: prior-period cells for equity proceeds and share issue expenses carry no text value; values paired to labels by cross-footing to net financing totals | extraction pairing note
R710 | page 5 | line 290 | QUALIFIER | P&L, balance sheet, cash flow and Annexure tables: text-layer value order is scrambled vs labels; values paired using pdftotext -raw order and cross-foot | extraction pairing note
R711 | page 8 | line 478 | QUALIFIER | Notes: (1) Aye Finance Limited is a Middle Layer NBFC (NBFC-ML) registered with RBI | note 1
R712 | page 8 | line 481 | QUALIFIER | Note 2: results subject to limited review by MSKA; unmodified conclusion 21 October 2026; reviewed by Audit Committee and approved by Board on Oct 21, 2026; Q1 FY27, Q2 FY26, H1 FY26 reviewed and FY26 audited by S S Kothari Mehta & Co. LLP | note 2
R713 | page 8 | line 490 | QUALIFIER | Note 3: results prepared per Reg 33 and 52 read with 63(2) SEBI LODR, Ind AS (s.133 Companies Act); RBI guidance implemented as and when issued/applicable | note 3
R714 | page 8 | line 496 | QUALIFIER | Note 4: resolution plan details under RBI resolution framework 1.0/2.0 (circulars Aug 06, 2020 and May 5, 2021) as at September 30, 2026; (All amounts are in Rs. Crores) | note 4
R715 | page 8 | line 525 | QUALIFIER | * Consist of unbilled and overdue principal. | footnote on OTR table (markers "(A) *" and "2026*")
R716 | page 8 | line 526 | QUALIFIER | # Includes restructuring implemented pursuant to OTR 2.0 for personal loans, individual business loans and small business loans. | footnote on Personal loans #
R717 | page 8 | line 527 | QUALIFIER | Note 5: Disclosure pursuant to RBI notification RBI/DOR/2025-26/359 dated November 28, 2025 (transfers of loan exposures) | note 5
R718 | page 8 | line 546 | QUALIFIER | (b)(i) The Company has not acquired any loans through assignment during the half year ended September 30, 2026 | negative disclosure
R719 | page 8 | line 552 | QUALIFIER | (c)(i) The Company has not transferred any stressed loans during the half year ended September 30, 2026. | negative disclosure
R720 | page 9 | line 569 | QUALIFIER | (c)(iii) The Company has not acquired any stressed loan during the half year ended September 30, 2026. | negative disclosure
R721 | page 9 | line 588 | QUALIFIER | Note 6: no separate reportable segment per Ind AS 108 | note 6
R722 | page 9 | line 589 | QUALIFIER | Note 7: FAME (100% owned, Section 8 non-profit) not consolidated: no control under Ind AS 110 since company cannot earn variable returns | note 7
R723 | page 9 | line 596 | QUALIFIER | Note 8: all listed secured NCDs secured by first exclusive charge on hypothecated book debts up to minimum 100% of amount outstanding | note 8
R724 | page 9 | line 600 | QUALIFIER | Note 9: Reg 52(4) disclosures for half year ended Sep 30, 2026 attached as Annexure I | note 9
R725 | page 9 | line 603 | QUALIFIER | Note 10: IPO listed Feb 16, 2026; net proceeds Rs 672.24 Crores after estimated offer expenses Rs 37.76 Crores (incl. pre-IPO); OFS proceeds remitted to selling shareholders net of expenses borne by them; unutilised offer expenses Rs 22.63 crores | note 10
R726 | page 9 | line 621 | QUALIFIER | Note 11: ESOP transfers and allotment during H1 FY27 | note 11
R727 | page 9 | line 626 | QUALIFIER | Note 12: previous period figures regrouped/rearranged/reclassified wherever necessary | note 12
R728 | page 10 | line 649 | QUALIFIER | (All amounts are in Rs. crores unless otherwise stated); ratios are for the Half year ended September 30, 2026 | unit / period
R729 | page 10 | line 652 | QUALIFIER | (Refer Note 1) Debt equity ratio = (Debt securities + Borrowings other than debt securities + Subordinated liabilities (lease liabilities)) / Net worth. | definition
R730 | page 10 | line 653 | QUALIFIER | (Refer Note 2) Net worth = Total equity - Deferred tax - Intangible assets including intangible assets under development - Prepaid expenses. | definition
R731 | page 10 | line 656 | QUALIFIER | (Refer Note 3) Total debt to total assets = (Debt securities + Borrowings other than debt securities + Subordinated liabilities (lease liabilities)) / Total assets. | definition
R732 | page 10 | line 657 | QUALIFIER | (Refer Note 4) Net profit margin = Net profit for the period / Total income for the period. | definition
R733 | page 10 | line 665 | QUALIFIER | Gross stage III ratio = Gross stage III loans / Total loans | definition
R734 | page 10 | line 671 | QUALIFIER | Net stage III ratio = (Gross stage III loans - ECL on Gross stage III) / (Total loans - ECL on Gross stage III) | definition
R735 | page 10 | line 676 | QUALIFIER | Provision coverage ratio = ECL on Gross stage III / Gross stage III | definition
R736 | page 10 | line 677 | QUALIFIER | Capital to risk-weighted assets ratio calculated as per RBI guidelines | definition
R737 | page 10 | line 691 | QUALIFIER | Note 5: DSCR, ISCR, redeemable preference shares, current ratio, CRR/DRR, long term debt to working capital, bad debts to receivable, current liability ratio, debtors turnover, inventory turnover and operating margin are not applicable / relevant to the Company | not applicable ratios
R738 | page 12 | line 932 | QUALIFIER | Security cover report: addressed to Board for submission to debenture trustees; limited assurance; Guidance Note on Reports or Certificates for Special Purposes | report basis
R739 | page 14 | line 932 | QUALIFIER | Observation 12: in respect of ISIN INE501X07588, the Company is in breach of the required financial covenant of (PAR 90 + Write off)/Gross Loan Portfolio. Disclosed by Management in its Statement. | auditor observation
R740 | page 15 | line 950 | QUALIFIER | Conclusion 13: "except for paragraph 12" nothing has come to attention re security cover, book values agreement, financial covenants compliance | qualified conclusion
R741 | page 15 | line 965 | QUALIFIER | Restriction on Use: report solely for compliance with SEBI Listing Regulations and for debenture trustees | restriction
R742 | page 16 | line 1101 | QUALIFIER | Value of assets is considered as Principal Outstanding amount for Col C and Col D. Since market value is not ascertainable, amount shown in Col L; market value unascertainable because book/debt receivables are provided as security cover as hypothecation | Annexure 1 footnote (marker "Loans #", "$" garbled as "B")
R743 | page 16 | line 1104 | QUALIFIER | * All other NCDs whether held by banks or others have been considered in the "Debt securities" | Annexure 1 footnote on Debt Securities*
R744 | page 16 | line 1105 | QUALIFIER | ** Contains Banks/NBFC borrowings worth Rs. 455 crores for which corresponding security is not maintained due to time limit granted by the lenders | Annexure 1 footnote on Bank** and Others**
R745 | page 16 | line 1002 | QUALIFIER | Annexure 1 header: Exclusive/Pari-passu security columns A-O, Rupees In Crores; Annexure 1 for Catalyst Trusteeship Limited | unit / scope
R746 | page 16 | line 1050 | QUALIFIER | Marker "Loans#" on Annexure 1 / 2; "#" definition not located in text layer (the footnote beginning "Value of assets is considered as Principal Outstanding" is printed with a garbled marker) | FOOTNOTE_UNRESOLVED [FOOTNOTE_UNRESOLVED]
R747 | page 18 | line 1250 | QUALIFIER | Annexure 2 footnote: Value of assets considered as Principal Outstanding amount for Col C and Col D ... market value unascertainable; hypothecation of book/debt receivables | Annexure 2 footnote (marker garbled)
R748 | page 18 | line 1229 | QUALIFIER | Markers "Debt Securities*" and "Others**" on Annexure 2: footnote text for "*" and "**" not printed on this page | FOOTNOTE_UNRESOLVED on page 18 (text appears on Annexure 1 page 16) [FOOTNOTE_UNRESOLVED]
R749 | page 20 | line 1279 | QUALIFIER | Annexure 3: INE501X07588 "Complied except clause 10.3(a) Ratio of PAR 90 and write-offs divided by Gross Loan Portfolio"; reason: "Increase in write-offs in this financial year due to higher delinquencies, industry wide stress in Miro Business Loans and MFI Loans, requisite waiver received." | covenant non-compliance with reason
R750 | page 20 | line 1270 | QUALIFIER | Annexure 3: quarterly compliance with financial covenants as on September 30, 2026 for Catalyst Trusteeship Limited and MITCON Credentia Trusteeship Services Limited; compliance column Y for all other ISINs | covenant compliance scope
R751 | page 21 | line 1382 | QUALIFIER | Rows 15 (INE501X07737) and 15 (INE501X07745): S.No printed as "15." twice (no 16); covenant clause 17.4 (a) and 10.3 (a) respectively | S.No duplicate as printed
R752 | page 23 | line 1457 | QUALIFIER | Annexure-I A: Statement of utilization of issue proceeds; funds utilized 140 (INE501X07737) and 150 (INE501X07745) vs raised 140 and 220; Any deviation: No | utilisation statement
R753 | page 23 | line 1491 | QUALIFIER | B: Is there a deviation/variation in use of funds raised? No; comments of audit committee: Nil; comments of auditors: Nil | deviation statement
R754 | page 24 | line 1528 | QUALIFIER | Deviation could mean: a) Deviation in the objects or purposes for which the funds have been raised. b) Deviation in the amount of funds actually utilized as against what was originally disclosed. | definition
R755 | page 1 | line 74 | QUALIFIER | Enclosures: Unaudited Financial Results with Limited Review Report; Security Cover Certificate (Reg 54(3)); Statement under Reg 52(7) & (7A); RPT disclosure for half year to follow with XBRL | enclosure list
