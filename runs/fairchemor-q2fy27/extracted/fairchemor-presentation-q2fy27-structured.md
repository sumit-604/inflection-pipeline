# A1 STRUCTURED EXTRACTION: Fairchem Organics (FAIRCHEMOR) Q2 FY27 earnings presentation
source: runs/fairchemor-q2fy27/inputs/presentation_fairchemor_q2fy27.pdf (24 pages, page 1 = cover letter)
fulltext: runs/fairchemor-q2fy27/extracted/fairchemor-presentation-q2fy27-fulltext.md (line numbers = line numbers of that file)
unit_convention: Rs Mn (Millions); conversion_factor_to_cr: x0.1 (1 Mn = 0.1 Cr); values NOT converted
ID range: R001-R512
counts: NUMBER 321, ENTITY 60, FORWARD 20, DATE 24, QUALIFIER 87
conventions: slide page-number footers and list numerals not captured. Pages 16, 17, 19 have scrambled table layout; p16/p17 rows anchor to the metric label line, values sit within lines 429-443 / 449-463 (LAYOUT_OFFSET). Page 22 chart values assigned by x-position where flagged CHART_POSITION_INFERRED, CHART_UNASSIGNED where not recoverable. Nil/dash values flagged ZERO_STANDING and anchored to the table dash line. Pages 3 and 12 (divider, aerial image) carry no data rows.

## NUMBER TABLE
R### | page N | line L | TYPE | verbatim value | short context | flags
R001 | page 1 | line 39 | NUMBER | BSE Scrip Code 543252 | scrip code
R002 | page 1 | line 73 | NUMBER | ACS - 24293 | company secretary membership number
R003 | page 4 | line 95 | NUMBER | 30 years | legacy
R004 | page 4 | line 102 | NUMBER | ~1.25% | Acid Oil share of soft oils processed (lines 102-103)
R005 | page 4 | line 103 | NUMBER | ~0.25% | DOD share of soft oils processed
R006 | page 5 | line 118 | NUMBER | 1.25% by-product | Acid Oil as % of soft oil
R007 | page 5 | line 139 | NUMBER | 0.25% by-product | Deodorizer Distillate as % of hard oil
R008 | page 7 | line 227 | NUMBER | 100+ suppliers | suppliers on-board
R009 | page 7 | line 232 | NUMBER | 500 Km | radius of procurement/sales
R010 | page 8 | line 248 | NUMBER | average experience of 10 years in the firm | R&D team experience (lines 246-249)
R011 | page 8 | line 264 | NUMBER | 386 sq mt | R&D lab area
R012 | page 8 | line 264 | NUMBER | 13 | R&D lab employees (incl. 1 PhD)
R013 | page 8 | line 264 | NUMBER | 1 | PhD among R&D employees
R014 | page 10 | line 289 | NUMBER | more than 15 years | customer relationships
R015 | page 10 | line 290 | NUMBER | More than 20 years | key raw material supplier relationships
R016 | page 10 | line 304 | NUMBER | INR 340 Mn | recently concluded buy-back
R017 | page 11 | line 328 | NUMBER | every three years | production equipment external testing frequency
R018 | page 13 | line 357 | NUMBER | more than 32 years | work experience in chemical industry (Nahoosh Jariwala)
R019 | page 13 | line 376 | NUMBER | 44+ years | financial services industry experience (Sudhin Choksey)
R020 | page 13 | line 382 | NUMBER | last 9 years | audited by Big 4 for
R021 | page 15 | line 401 | NUMBER | Rs 1,669 Mn | Revenue from Operations, Q2 FY27
R022 | page 15 | line 401 | NUMBER | Rs 175 Mn | EBITDA, Q2 FY27
R023 | page 15 | line 401 | NUMBER | 10.51% | EBITDA margin, Q2 FY27
R024 | page 15 | line 406 | NUMBER | Rs 137 Mn | PBT, Q2 FY27
R025 | page 15 | line 406 | NUMBER | Rs 102 Mn | PAT, Q2 FY27
R026 | page 15 | line 406 | NUMBER | 6.09% | PAT margin, Q2 FY27
R027 | page 15 | line 416 | NUMBER | Rs 3,431 Mn | Revenue from Operations, H1 FY27
R028 | page 15 | line 416 | NUMBER | Rs 354 Mn | EBITDA, H1 FY27
R029 | page 15 | line 416 | NUMBER | 10.32% | EBITDA margin, H1 FY27
R030 | page 15 | line 421 | NUMBER | Rs 273 Mn | PBT, H1 FY27
R031 | page 15 | line 421 | NUMBER | Rs 202 Mn | PAT, H1 FY27
R032 | page 15 | line 421 | NUMBER | 5.88% | PAT margin, H1 FY27
R033 | page 15 | line 401 | NUMBER | 41.4% Y-o-Y | revenue from operations growth, H1 FY27
R034 | page 15 | line 405 | NUMBER | 10.32% | EBITDA margin in H1 FY27 (narrative)
R035 | page 15 | line 411 | NUMBER | 16.5% | import duty on crude soya oil, before reduction
R036 | page 15 | line 411 | NUMBER | 11.0% | import duty on crude soya oil, after reduction
R037 | page 16 | line 431 | NUMBER | 1,669 | Revenue from Operations, Q2 FY27 | LAYOUT_OFFSET: anchored to label line; values in lines 429-443
R038 | page 16 | line 431 | NUMBER | 1,115 | Revenue from Operations, Q2 FY26 | LAYOUT_OFFSET: anchored to label line; values in lines 429-443
R039 | page 16 | line 431 | NUMBER | 49.7% | Revenue from Operations, YoY change (Q2 FY27 vs Q2 FY26) | LAYOUT_OFFSET
R040 | page 16 | line 432 | NUMBER | 1,494 | Total Expenses, Q2 FY27 | LAYOUT_OFFSET: anchored to label line; values in lines 429-443
R041 | page 16 | line 432 | NUMBER | 1,073 | Total Expenses, Q2 FY26 | LAYOUT_OFFSET: anchored to label line; values in lines 429-443
R042 | page 16 | line 432 | NUMBER | 39.2% | Total Expenses, YoY change (Q2 FY27 vs Q2 FY26) | LAYOUT_OFFSET
R043 | page 16 | line 433 | NUMBER | 175 | EBITDA, Q2 FY27 | LAYOUT_OFFSET: anchored to label line; values in lines 429-443
R044 | page 16 | line 433 | NUMBER | 42 | EBITDA, Q2 FY26 | LAYOUT_OFFSET: anchored to label line; values in lines 429-443
R045 | page 16 | line 433 | NUMBER | 316.7% | EBITDA, YoY change (Q2 FY27 vs Q2 FY26) | LAYOUT_OFFSET
R046 | page 16 | line 434 | NUMBER | 10.51% | EBITDA Margins (%), Q2 FY27 | LAYOUT_OFFSET: anchored to label line; values in lines 429-443
R047 | page 16 | line 434 | NUMBER | 3.77% | EBITDA Margins (%), Q2 FY26 | LAYOUT_OFFSET: anchored to label line; values in lines 429-443
R048 | page 16 | line 434 | NUMBER | 674 Bps | EBITDA Margins (%), YoY change (Q2 FY27 vs Q2 FY26) | LAYOUT_OFFSET
R049 | page 16 | line 435 | NUMBER | 1 | Other Income, Q2 FY27 | LAYOUT_OFFSET: anchored to label line; values in lines 429-443
R050 | page 16 | line 435 | NUMBER | 4 | Other Income, Q2 FY26 | LAYOUT_OFFSET: anchored to label line; values in lines 429-443
R051 | page 16 | line 435 | NUMBER | (75.0)% | Other Income, YoY change (Q2 FY27 vs Q2 FY26) | LAYOUT_OFFSET
R052 | page 16 | line 436 | NUMBER | 28 | Depreciation, Q2 FY27 | LAYOUT_OFFSET: anchored to label line; values in lines 429-443
R053 | page 16 | line 436 | NUMBER | 28 | Depreciation, Q2 FY26 | LAYOUT_OFFSET: anchored to label line; values in lines 429-443
R054 | page 16 | line 436 | NUMBER | 0.0% | Depreciation, YoY change (Q2 FY27 vs Q2 FY26) | LAYOUT_OFFSET
R055 | page 16 | line 437 | NUMBER | 11 | Finance Cost, Q2 FY27 | LAYOUT_OFFSET: anchored to label line; values in lines 429-443
R056 | page 16 | line 437 | NUMBER | 6 | Finance Cost, Q2 FY26 | LAYOUT_OFFSET: anchored to label line; values in lines 429-443
R057 | page 16 | line 437 | NUMBER | 83.3% | Finance Cost, YoY change (Q2 FY27 vs Q2 FY26) | LAYOUT_OFFSET
R058 | page 16 | line 438 | NUMBER | 137 | PBT, Q2 FY27 | LAYOUT_OFFSET: anchored to label line; values in lines 429-443
R059 | page 16 | line 438 | NUMBER | 12 | PBT, Q2 FY26 | LAYOUT_OFFSET: anchored to label line; values in lines 429-443
R060 | page 16 | line 438 | NUMBER | 1041.7% | PBT, YoY change (Q2 FY27 vs Q2 FY26) | LAYOUT_OFFSET
R061 | page 16 | line 439 | NUMBER | 35 | Tax, Q2 FY27 | LAYOUT_OFFSET: anchored to label line; values in lines 429-443
R062 | page 16 | line 439 | NUMBER | 4 | Tax, Q2 FY26 | LAYOUT_OFFSET: anchored to label line; values in lines 429-443
R063 | page 16 | line 439 | NUMBER | 775.0% | Tax, YoY change (Q2 FY27 vs Q2 FY26) | LAYOUT_OFFSET
R064 | page 16 | line 440 | NUMBER | 102 | PAT w/o. Exceptional item, Q2 FY27 | LAYOUT_OFFSET: anchored to label line; values in lines 429-443
R065 | page 16 | line 440 | NUMBER | 8 | PAT w/o. Exceptional item, Q2 FY26 | LAYOUT_OFFSET: anchored to label line; values in lines 429-443
R066 | page 16 | line 440 | NUMBER | 1175.0% | PAT w/o. Exceptional item, YoY change (Q2 FY27 vs Q2 FY26) | LAYOUT_OFFSET
R067 | page 16 | line 441 | NUMBER | 6.09% | PAT Margins (%), Q2 FY27 | LAYOUT_OFFSET: anchored to label line; values in lines 429-443
R068 | page 16 | line 441 | NUMBER | 0.72% | PAT Margins (%), Q2 FY26 | LAYOUT_OFFSET: anchored to label line; values in lines 429-443
R069 | page 16 | line 441 | NUMBER | 537 Bps | PAT Margins (%), YoY change (Q2 FY27 vs Q2 FY26) | LAYOUT_OFFSET
R070 | page 16 | line 442 | NUMBER | 2 | Other Comprehensive Income, Q2 FY27 | LAYOUT_OFFSET: anchored to label line; values in lines 429-443
R071 | page 16 | line 442 | NUMBER | -1 | Other Comprehensive Income, Q2 FY26 | LAYOUT_OFFSET: anchored to label line; values in lines 429-443
R072 | page 16 | line 443 | NUMBER | 104 | Total Comprehensive Income, Q2 FY27 | LAYOUT_OFFSET: anchored to label line; values in lines 429-443
R073 | page 16 | line 443 | NUMBER | 7 | Total Comprehensive Income, Q2 FY26 | LAYOUT_OFFSET: anchored to label line; values in lines 429-443
R074 | page 16 | line 443 | NUMBER | 1385.7% | Total Comprehensive Income, YoY change (Q2 FY27 vs Q2 FY26) | LAYOUT_OFFSET
R075 | page 17 | line 451 | NUMBER | 3,431 | Revenue from Operations, H1 FY27 | LAYOUT_OFFSET: anchored to label line; values in lines 449-463
R076 | page 17 | line 451 | NUMBER | 2,426 | Revenue from Operations, H1 FY26 | LAYOUT_OFFSET: anchored to label line; values in lines 449-463
R077 | page 17 | line 451 | NUMBER | 41.4% | Revenue from Operations, YoY change (H1 FY27 vs H1 FY26) | LAYOUT_OFFSET
R078 | page 17 | line 452 | NUMBER | 3,077 | Total Expenses, H1 FY27 | LAYOUT_OFFSET: anchored to label line; values in lines 449-463
R079 | page 17 | line 452 | NUMBER | 2,332 | Total Expenses, H1 FY26 | LAYOUT_OFFSET: anchored to label line; values in lines 449-463
R080 | page 17 | line 452 | NUMBER | 31.9% | Total Expenses, YoY change (H1 FY27 vs H1 FY26) | LAYOUT_OFFSET
R081 | page 17 | line 453 | NUMBER | 354 | EBITDA, H1 FY27 | LAYOUT_OFFSET: anchored to label line; values in lines 449-463
R082 | page 17 | line 453 | NUMBER | 94 | EBITDA, H1 FY26 | LAYOUT_OFFSET: anchored to label line; values in lines 449-463
R083 | page 17 | line 453 | NUMBER | 276.6% | EBITDA, YoY change (H1 FY27 vs H1 FY26) | LAYOUT_OFFSET
R084 | page 17 | line 454 | NUMBER | 10.32% | EBITDA Margins (%), H1 FY27 | LAYOUT_OFFSET: anchored to label line; values in lines 449-463
R085 | page 17 | line 454 | NUMBER | 3.87% | EBITDA Margins (%), H1 FY26 | LAYOUT_OFFSET: anchored to label line; values in lines 449-463
R086 | page 17 | line 454 | NUMBER | 645 Bps | EBITDA Margins (%), YoY change (H1 FY27 vs H1 FY26) | LAYOUT_OFFSET
R087 | page 17 | line 455 | NUMBER | 5 | Other Income, H1 FY27 | LAYOUT_OFFSET: anchored to label line; values in lines 449-463
R088 | page 17 | line 455 | NUMBER | 5 | Other Income, H1 FY26 | LAYOUT_OFFSET: anchored to label line; values in lines 449-463
R089 | page 17 | line 456 | NUMBER | 56 | Depreciation, H1 FY27 | LAYOUT_OFFSET: anchored to label line; values in lines 449-463
R090 | page 17 | line 456 | NUMBER | 55 | Depreciation, H1 FY26 | LAYOUT_OFFSET: anchored to label line; values in lines 449-463
R091 | page 17 | line 456 | NUMBER | 1.8% | Depreciation, YoY change (H1 FY27 vs H1 FY26) | LAYOUT_OFFSET
R092 | page 17 | line 457 | NUMBER | 30 | Finance Cost, H1 FY27 | LAYOUT_OFFSET: anchored to label line; values in lines 449-463
R093 | page 17 | line 457 | NUMBER | 16 | Finance Cost, H1 FY26 | LAYOUT_OFFSET: anchored to label line; values in lines 449-463
R094 | page 17 | line 457 | NUMBER | 87.5% | Finance Cost, YoY change (H1 FY27 vs H1 FY26) | LAYOUT_OFFSET
R095 | page 17 | line 458 | NUMBER | 273 | PBT, H1 FY27 | LAYOUT_OFFSET: anchored to label line; values in lines 449-463
R096 | page 17 | line 458 | NUMBER | 28 | PBT, H1 FY26 | LAYOUT_OFFSET: anchored to label line; values in lines 449-463
R097 | page 17 | line 458 | NUMBER | 875.0% | PBT, YoY change (H1 FY27 vs H1 FY26) | LAYOUT_OFFSET
R098 | page 17 | line 459 | NUMBER | 71 | Tax, H1 FY27 | LAYOUT_OFFSET: anchored to label line; values in lines 449-463
R099 | page 17 | line 459 | NUMBER | 9 | Tax, H1 FY26 | LAYOUT_OFFSET: anchored to label line; values in lines 449-463
R100 | page 17 | line 459 | NUMBER | 688.9% | Tax, YoY change (H1 FY27 vs H1 FY26) | LAYOUT_OFFSET
R101 | page 17 | line 460 | NUMBER | 202 | PAT w/o. Exceptional item, H1 FY27 | LAYOUT_OFFSET: anchored to label line; values in lines 449-463
R102 | page 17 | line 460 | NUMBER | 19 | PAT w/o. Exceptional item, H1 FY26 | LAYOUT_OFFSET: anchored to label line; values in lines 449-463
R103 | page 17 | line 460 | NUMBER | 963.2% | PAT w/o. Exceptional item, YoY change (H1 FY27 vs H1 FY26) | LAYOUT_OFFSET
R104 | page 17 | line 461 | NUMBER | 5.88% | PAT Margins (%), H1 FY27 | LAYOUT_OFFSET: anchored to label line; values in lines 449-463
R105 | page 17 | line 461 | NUMBER | 0.78% | PAT Margins (%), H1 FY26 | LAYOUT_OFFSET: anchored to label line; values in lines 449-463
R106 | page 17 | line 461 | NUMBER | 510 Bps | PAT Margins (%), YoY change (H1 FY27 vs H1 FY26) | LAYOUT_OFFSET
R107 | page 17 | line 462 | NUMBER | -2 | Other Comprehensive Income, H1 FY27 | LAYOUT_OFFSET: anchored to label line; values in lines 449-463
R108 | page 17 | line 462 | NUMBER | -1 | Other Comprehensive Income, H1 FY26 | LAYOUT_OFFSET: anchored to label line; values in lines 449-463
R109 | page 17 | line 463 | NUMBER | 200 | Total Comprehensive Income, H1 FY27 | LAYOUT_OFFSET: anchored to label line; values in lines 449-463
R110 | page 17 | line 463 | NUMBER | 18 | Total Comprehensive Income, H1 FY26 | LAYOUT_OFFSET: anchored to label line; values in lines 449-463
R111 | page 17 | line 463 | NUMBER | 1011.1% | Total Comprehensive Income, YoY change (H1 FY27 vs H1 FY26) | LAYOUT_OFFSET
R112 | page 18 | line 471 | NUMBER | 6,215 | Revenue from Operations, FY24
R113 | page 18 | line 471 | NUMBER | 5,379 | Revenue from Operations, FY25
R114 | page 18 | line 471 | NUMBER | 4,596 | Revenue from Operations, FY26
R115 | page 18 | line 471 | NUMBER | 3,431 | Revenue from Operations, H1 FY27
R116 | page 18 | line 473 | NUMBER | 5,545 | Total Expenses, FY24
R117 | page 18 | line 473 | NUMBER | 4,951 | Total Expenses, FY25
R118 | page 18 | line 473 | NUMBER | 4,380 | Total Expenses, FY26
R119 | page 18 | line 473 | NUMBER | 3,077 | Total Expenses, H1 FY27
R120 | page 18 | line 475 | NUMBER | 670 | EBITDA, FY24
R121 | page 18 | line 475 | NUMBER | 428 | EBITDA, FY25
R122 | page 18 | line 475 | NUMBER | 216 | EBITDA, FY26
R123 | page 18 | line 475 | NUMBER | 354 | EBITDA, H1 FY27
R124 | page 18 | line 477 | NUMBER | 10.78% | EBITDA Margins (%), FY24
R125 | page 18 | line 477 | NUMBER | 7.96% | EBITDA Margins (%), FY25
R126 | page 18 | line 477 | NUMBER | 4.70% | EBITDA Margins (%), FY26
R127 | page 18 | line 477 | NUMBER | 10.32% | EBITDA Margins (%), H1 FY27
R128 | page 18 | line 479 | NUMBER | 11 | Other Income, FY24
R129 | page 18 | line 479 | NUMBER | 13 | Other Income, FY25
R130 | page 18 | line 479 | NUMBER | 13 | Other Income, FY26
R131 | page 18 | line 479 | NUMBER | 5 | Other Income, H1 FY27
R132 | page 18 | line 481 | NUMBER | 93 | Depreciation, FY24
R133 | page 18 | line 481 | NUMBER | 105 | Depreciation, FY25
R134 | page 18 | line 481 | NUMBER | 110 | Depreciation, FY26
R135 | page 18 | line 481 | NUMBER | 56 | Depreciation, H1 FY27
R136 | page 18 | line 483 | NUMBER | 42 | Finance Cost, FY24
R137 | page 18 | line 483 | NUMBER | 37 | Finance Cost, FY25
R138 | page 18 | line 483 | NUMBER | 37 | Finance Cost, FY26
R139 | page 18 | line 483 | NUMBER | 30 | Finance Cost, H1 FY27
R140 | page 18 | line 485 | NUMBER | 546 | PBT, FY24
R141 | page 18 | line 485 | NUMBER | 299 | PBT, FY25
R142 | page 18 | line 485 | NUMBER | 82 | PBT, FY26
R143 | page 18 | line 485 | NUMBER | 273 | PBT, H1 FY27
R144 | page 18 | line 487 | NUMBER | 141 | Tax, FY24
R145 | page 18 | line 487 | NUMBER | 79 | Tax, FY25
R146 | page 18 | line 487 | NUMBER | 20 | Tax, FY26
R147 | page 18 | line 487 | NUMBER | 71 | Tax, H1 FY27
R148 | page 18 | line 489 | NUMBER | 405 | PAT w/o. Exceptional item, FY24
R149 | page 18 | line 489 | NUMBER | 220 | PAT w/o. Exceptional item, FY25
R150 | page 18 | line 489 | NUMBER | 62 | PAT w/o. Exceptional item, FY26
R151 | page 18 | line 489 | NUMBER | 202 | PAT w/o. Exceptional item, H1 FY27
R152 | page 18 | line 491 | NUMBER | 6.52% | PAT Margins (%), FY24
R153 | page 18 | line 491 | NUMBER | 4.09% | PAT Margins (%), FY25
R154 | page 18 | line 491 | NUMBER | 1.35% | PAT Margins (%), FY26
R155 | page 18 | line 491 | NUMBER | 5.88% | PAT Margins (%), H1 FY27
R156 | page 18 | line 492 | NUMBER | - | Exceptional Item - New Labour code (Net of tax), FY24 | ZERO_STANDING LAYOUT_ORDER from line 492
R157 | page 18 | line 492 | NUMBER | - | Exceptional Item - New Labour code (Net of tax), FY25 | ZERO_STANDING LAYOUT_ORDER from line 492
R158 | page 18 | line 492 | NUMBER | 7 | Exceptional Item - New Labour code (Net of tax), FY26 | LAYOUT_ORDER from line 492
R159 | page 18 | line 492 | NUMBER | 0 | Exceptional Item - New Labour code (Net of tax), H1 FY27 | ZERO_STANDING LAYOUT_ORDER from line 492
R160 | page 18 | line 493 | NUMBER | (1) | Other Comprehensive Income, FY24 | LAYOUT_ORDER
R161 | page 18 | line 493 | NUMBER | (1) | Other Comprehensive Income, FY25 | LAYOUT_ORDER
R162 | page 18 | line 493 | NUMBER | 4 | Other Comprehensive Income, FY26 | LAYOUT_ORDER
R163 | page 18 | line 493 | NUMBER | -2 | Other Comprehensive Income, H1 FY27 | LAYOUT_ORDER
R164 | page 18 | line 498 | NUMBER | 404 | Total Comprehensive Income, FY24
R165 | page 18 | line 498 | NUMBER | 219 | Total Comprehensive Income, FY25
R166 | page 18 | line 498 | NUMBER | 59 | Total Comprehensive Income, FY26
R167 | page 18 | line 498 | NUMBER | 200 | Total Comprehensive Income, H1 FY27
R168 | page 18 | line 500 | NUMBER | 31.10 | Basic/Diluted EPS (INR per share), FY24
R169 | page 18 | line 500 | NUMBER | 16.88 | Basic/Diluted EPS (INR per share), FY25
R170 | page 18 | line 500 | NUMBER | 4.28 | Basic/Diluted EPS (INR per share), FY26
R171 | page 18 | line 500 | NUMBER | 16.02* | Basic/Diluted EPS (INR per share), H1 FY27 | asterisk marker
R172 | page 19 | line 510 | NUMBER | 1,971 | Property, Plant and Equipment, FY25
R173 | page 19 | line 510 | NUMBER | 1,962 | Property, Plant and Equipment, FY26
R174 | page 19 | line 510 | NUMBER | 2,048 | Property, Plant and Equipment, H1 FY27
R175 | page 19 | line 511 | NUMBER | 117 | Capital work-in-progress, FY25
R176 | page 19 | line 511 | NUMBER | 184 | Capital work-in-progress, FY26
R177 | page 19 | line 511 | NUMBER | 83 | Capital work-in-progress, H1 FY27
R178 | page 19 | line 512 | NUMBER | 40 | Right of use assets, FY25
R179 | page 19 | line 512 | NUMBER | 19 | Right of use assets, H1 FY27
R180 | page 19 | line 513 | NUMBER | 0 | Intangible Assets, FY26
R181 | page 19 | line 514 | NUMBER | 2 | Intangible Assets Under Development, FY25
R182 | page 19 | line 514 | NUMBER | 0 | Intangible Assets Under Development, FY26
R183 | page 19 | line 514 | NUMBER | 0 | Intangible Assets Under Development, H1 FY27
R184 | page 19 | line 515 | NUMBER | - | Financial Assets (header row), FY25 | ZERO_STANDING ZERO_STANDING
R185 | page 19 | line 515 | NUMBER | - | Financial Assets (header row), FY26 | ZERO_STANDING ZERO_STANDING
R186 | page 19 | line 516 | NUMBER | 2 | Non-current asset line, first unlabelled value, FY25 | ORDER_INFERRED
R187 | page 19 | line 516 | NUMBER | 2 | Non-current asset line, first unlabelled value, FY26 | ORDER_INFERRED
R188 | page 19 | line 516 | NUMBER | 29 | Non-current asset line, first unlabelled value, H1 FY27 | ORDER_INFERRED
R189 | page 19 | line 517 | NUMBER | 67 | Non-current asset line, second unlabelled value, FY25 | ORDER_INFERRED
R190 | page 19 | line 517 | NUMBER | 39 | Non-current asset line, second unlabelled value, FY26 | ORDER_INFERRED
R191 | page 19 | line 517 | NUMBER | 5 | Non-current asset line, second unlabelled value, H1 FY27 | ORDER_INFERRED
R192 | page 19 | line 518 | NUMBER | 13 | Non-current asset line, third unlabelled value, FY25 | ORDER_INFERRED
R193 | page 19 | line 518 | NUMBER | 3 | Non-current asset line, third unlabelled value, FY26 | ORDER_INFERRED
R194 | page 19 | line 519 | NUMBER | 2,212 | Total Non-current Assets (sum-verified), FY25 | ORDER_INFERRED
R195 | page 19 | line 519 | NUMBER | 2,191 | Total Non-current Assets (sum-verified), FY26 | ORDER_INFERRED
R196 | page 19 | line 519 | NUMBER | 2184 | Total Non-current Assets (sum-verified), H1 FY27 | ORDER_INFERRED
R197 | page 19 | line 521 | NUMBER | 883 | Inventories, FY25 | ORDER_INFERRED
R198 | page 19 | line 521 | NUMBER | 922 | Inventories, FY26 | ORDER_INFERRED
R199 | page 19 | line 521 | NUMBER | 699 | Inventories, H1 FY27 | ORDER_INFERRED
R200 | page 19 | line 523 | NUMBER | 861 | Trade receivables, FY25 | ORDER_INFERRED
R201 | page 19 | line 523 | NUMBER | 681 | Trade receivables, FY26 | ORDER_INFERRED
R202 | page 19 | line 523 | NUMBER | 1002 | Trade receivables, H1 FY27 | ORDER_INFERRED
R203 | page 19 | line 524 | NUMBER | 13 | Cash and Bank Balance, FY25 | ORDER_INFERRED
R204 | page 19 | line 524 | NUMBER | 12 | Cash and Bank Balance, FY26 | ORDER_INFERRED
R205 | page 19 | line 524 | NUMBER | 14 | Cash and Bank Balance, H1 FY27 | ORDER_INFERRED
R206 | page 19 | line 525 | NUMBER | 49 | Other current assets, FY25 | ORDER_INFERRED
R207 | page 19 | line 525 | NUMBER | 103 | Other current assets, FY26 | ORDER_INFERRED
R208 | page 19 | line 525 | NUMBER | 85 | Other current assets, H1 FY27 | ORDER_INFERRED
R209 | page 19 | line 527 | NUMBER | 1,806 | Total Current Assets (sum-verified), FY25 | ORDER_INFERRED
R210 | page 19 | line 527 | NUMBER | 1,718 | Total Current Assets (sum-verified), FY26 | ORDER_INFERRED
R211 | page 19 | line 527 | NUMBER | 1800 | Total Current Assets (sum-verified), H1 FY27 | ORDER_INFERRED
R212 | page 19 | line 528 | NUMBER | 4,018 | TOTAL ASSETS, FY25
R213 | page 19 | line 528 | NUMBER | 3,910 | TOTAL ASSETS, FY26
R214 | page 19 | line 528 | NUMBER | 3984 | TOTAL ASSETS, H1 FY27
R215 | page 19 | line 510 | NUMBER | 130 | Equity Share Capital, FY25
R216 | page 19 | line 510 | NUMBER | 126 | Equity Share Capital, FY26
R217 | page 19 | line 510 | NUMBER | 126 | Equity Share Capital, H1 FY27
R218 | page 19 | line 512 | NUMBER | 2,890 | Other Equity, FY25
R219 | page 19 | line 512 | NUMBER | 2,505 | Other Equity, FY26
R220 | page 19 | line 512 | NUMBER | 2692 | Other Equity, H1 FY27
R221 | page 19 | line 513 | NUMBER | 3,020 | Total Equity (sum-verified), FY25 | ORDER_INFERRED
R222 | page 19 | line 513 | NUMBER | 2,631 | Total Equity (sum-verified), FY26 | ORDER_INFERRED
R223 | page 19 | line 513 | NUMBER | 2818 | Total Equity (sum-verified), H1 FY27 | ORDER_INFERRED
R224 | page 19 | line 515 | NUMBER | - | Non-Current Liabilities (header row), FY25 | ZERO_STANDING ZERO_STANDING
R225 | page 19 | line 515 | NUMBER | - | Non-Current Liabilities (header row), FY26 | ZERO_STANDING ZERO_STANDING
R226 | page 19 | line 515 | NUMBER | - | Non-Current Liabilities (header row), H1 FY27 | ZERO_STANDING ZERO_STANDING
R227 | page 19 | line 517 | NUMBER | 25 | Non-current liability line, first value, FY25 | ORDER_INFERRED
R228 | page 19 | line 517 | NUMBER | 31 | Non-current liability line, first value, FY26 | ORDER_INFERRED
R229 | page 19 | line 517 | NUMBER | 16 | Non-current liability line, first value, H1 FY27 | ORDER_INFERRED
R230 | page 19 | line 518 | NUMBER | 187 | Non-current liability line, second value, FY25 | ORDER_INFERRED
R231 | page 19 | line 518 | NUMBER | 206 | Non-current liability line, second value, FY26 | ORDER_INFERRED
R232 | page 19 | line 518 | NUMBER | 45 | Non-current liability line, second value, H1 FY27 | ORDER_INFERRED
R233 | page 19 | line 519 | NUMBER | 209 | Non-current liability line, third value, H1 FY27 | ORDER_INFERRED
R234 | page 19 | line 519 | NUMBER | 212 | Total Non-current Liabilities (sum-verified), FY25 | ORDER_INFERRED
R235 | page 19 | line 519 | NUMBER | 236 | Total Non-current Liabilities (sum-verified), FY26 | ORDER_INFERRED
R236 | page 19 | line 519 | NUMBER | 270 | Total Non-current Liabilities (sum-verified), H1 FY27 | ORDER_INFERRED
R237 | page 19 | line 521 | NUMBER | 630 | Current borrowings, FY25 | ORDER_INFERRED
R238 | page 19 | line 521 | NUMBER | 837 | Current borrowings, FY26 | ORDER_INFERRED
R239 | page 19 | line 521 | NUMBER | 686 | Current borrowings, H1 FY27 | ORDER_INFERRED
R240 | page 19 | line 522 | NUMBER | 83 | Trade Payables, FY25 | ORDER_INFERRED
R241 | page 19 | line 522 | NUMBER | 110 | Trade Payables, FY26 | ORDER_INFERRED
R242 | page 19 | line 522 | NUMBER | 113 | Trade Payables, H1 FY27 | ORDER_INFERRED
R243 | page 19 | line 523 | NUMBER | 16 | Other financial liabilities, FY25 | ORDER_INFERRED
R244 | page 19 | line 523 | NUMBER | 20 | Other financial liabilities, FY26 | ORDER_INFERRED
R245 | page 19 | line 523 | NUMBER | 20 | Other financial liabilities, H1 FY27 | ORDER_INFERRED
R246 | page 19 | line 524 | NUMBER | 43 | Other current liabilities, FY25 | ORDER_INFERRED
R247 | page 19 | line 524 | NUMBER | 62 | Other current liabilities, FY26 | ORDER_INFERRED
R248 | page 19 | line 524 | NUMBER | 62 | Other current liabilities, H1 FY27 | ORDER_INFERRED
R249 | page 19 | line 525 | NUMBER | 14 | Provisions (current), FY25 | ORDER_INFERRED
R250 | page 19 | line 525 | NUMBER | 11 | Provisions (current), FY26 | ORDER_INFERRED
R251 | page 19 | line 525 | NUMBER | 9 | Provisions (current), H1 FY27 | ORDER_INFERRED
R252 | page 19 | line 526 | NUMBER | 6 | Current Tax Liabilities (Net), H1 FY27 | ORDER_INFERRED
R253 | page 19 | line 527 | NUMBER | 786 | Total Current Liabilities (sum-verified), FY25 | ORDER_INFERRED
R254 | page 19 | line 527 | NUMBER | 1,042 | Total Current Liabilities (sum-verified), FY26 | ORDER_INFERRED
R255 | page 19 | line 527 | NUMBER | 896 | Total Current Liabilities (sum-verified), H1 FY27 | ORDER_INFERRED
R256 | page 19 | line 531 | NUMBER | 4,018 | TOTAL EQUITY AND LIABILITIES, FY25
R257 | page 19 | line 531 | NUMBER | 3,910 | TOTAL EQUITY AND LIABILITIES, FY26
R258 | page 19 | line 531 | NUMBER | 3984 | TOTAL EQUITY AND LIABILITIES, H1 FY27
R259 | page 20 | line 537 | NUMBER | 0.1 | Cash and Cash Equivalents at Beginning of the year, FY25
R260 | page 20 | line 537 | NUMBER | 0.1 | Cash and Cash Equivalents at Beginning of the year, FY26
R261 | page 20 | line 537 | NUMBER | 0.1 | Cash and Cash Equivalents at Beginning of the year, H1 FY27
R262 | page 20 | line 538 | NUMBER | (168) | Cash Flow From Operating Activities, FY25
R263 | page 20 | line 538 | NUMBER | 416 | Cash Flow From Operating Activities, FY26
R264 | page 20 | line 538 | NUMBER | 240 | Cash Flow From Operating Activities, H1 FY27
R265 | page 20 | line 539 | NUMBER | (255) | Cash Flow from Investing Activities, FY25
R266 | page 20 | line 539 | NUMBER | (137) | Cash Flow from Investing Activities, FY26
R267 | page 20 | line 539 | NUMBER | (44) | Cash Flow from Investing Activities, H1 FY27
R268 | page 20 | line 540 | NUMBER | 423 | Cash Flow From Financing Activities, FY25
R269 | page 20 | line 540 | NUMBER | (279) | Cash Flow From Financing Activities, FY26
R270 | page 20 | line 540 | NUMBER | (196) | Cash Flow From Financing Activities, H1 FY27
R271 | page 20 | line 541 | NUMBER | - | Net Inc./(Dec.) in Cash and Cash Equivalent, FY25 | ZERO_STANDING dash on table lines 541-542; LAYOUT_ORDER
R272 | page 20 | line 541 | NUMBER | - | Net Inc./(Dec.) in Cash and Cash Equivalent, FY26 | ZERO_STANDING dash on table lines 541-542; LAYOUT_ORDER
R273 | page 20 | line 541 | NUMBER | - | Net Inc./(Dec.) in Cash and Cash Equivalent, H1 FY27 | ZERO_STANDING dash on table lines 541-542; LAYOUT_ORDER
R274 | page 20 | line 542 | NUMBER | 0.1 | Cash and Cash Equivalents at End of the year, FY25 | LAYOUT_ORDER
R275 | page 20 | line 542 | NUMBER | 0.1 | Cash and Cash Equivalents at End of the year, FY26 | LAYOUT_ORDER
R276 | page 20 | line 542 | NUMBER | 0.1 | Cash and Cash Equivalents at End of the year, H1 FY27 | LAYOUT_ORDER
R277 | page 21 | line 549 | NUMBER | 4 | number of key strategies
R278 | page 21 | line 564 | NUMBER | 25% | initial export target
R279 | page 21 | line 566 | NUMBER | 50% | eventual export target of sales
R280 | page 22 | line 584 | NUMBER | 6215 | Revenue chart (Rs Mn), FY24
R281 | page 22 | line 584 | NUMBER | 5379 | Revenue chart (Rs Mn), FY25
R282 | page 22 | line 584 | NUMBER | 4596 | Revenue chart (Rs Mn), FY26
R283 | page 22 | line 584 | NUMBER | 3431 | Revenue chart (Rs Mn), H1 FY27
R284 | page 22 | line 584 | NUMBER | 670 | EBITDA chart (Rs Mn), FY24 | CHART_POSITION_INFERRED
R285 | page 22 | line 584 | NUMBER | 428 | EBITDA chart (Rs Mn), FY25 | CHART_POSITION_INFERRED
R286 | page 22 | line 584 | NUMBER | 216 | EBITDA chart (Rs Mn), FY26 | CHART_POSITION_INFERRED
R287 | page 22 | line 584 | NUMBER | 354 | EBITDA chart (Rs Mn), H1 FY27 | CHART_POSITION_INFERRED
R288 | page 22 | line 584 | NUMBER | 405 | PAT chart (Rs Mn), FY24 | CHART_POSITION_INFERRED
R289 | page 22 | line 584 | NUMBER | 220 | PAT chart (Rs Mn), FY25 | CHART_POSITION_INFERRED
R290 | page 22 | line 584 | NUMBER | 62 | PAT chart (Rs Mn), FY26 | CHART_POSITION_INFERRED
R291 | page 22 | line 584 | NUMBER | 202 | PAT chart (Rs Mn), H1 FY27 | CHART_POSITION_INFERRED
R292 | page 22 | line 598 | NUMBER | 0.02 | Net Debt to Equity chart, FY24 | CHART_POSITION_INFERRED (values at lines 595-607)
R293 | page 22 | line 598 | NUMBER | 0.20 | Net Debt to Equity chart, FY25 | CHART_POSITION_INFERRED (values at lines 595-607)
R294 | page 22 | line 598 | NUMBER | 0.32 | Net Debt to Equity chart, FY26 | CHART_POSITION_INFERRED (values at lines 595-607)
R295 | page 22 | line 598 | NUMBER | 0.24 | Net Debt to Equity chart, H1 FY27 | CHART_POSITION_INFERRED (values at lines 595-607)
R296 | page 22 | line 600 | NUMBER | 76 | Cash Conversion Cycle Days chart, FY24 | CHART_POSITION_INFERRED (values at lines 600-603)
R297 | page 22 | line 600 | NUMBER | 82 | Cash Conversion Cycle Days chart, FY25 | CHART_POSITION_INFERRED (values at lines 600-603)
R298 | page 22 | line 600 | NUMBER | 99 | Cash Conversion Cycle Days chart, FY26 | CHART_POSITION_INFERRED (values at lines 600-603)
R299 | page 22 | line 600 | NUMBER | 128 | Cash Conversion Cycle Days chart, H1 FY27 | CHART_POSITION_INFERRED (values at lines 600-603)
R300 | page 22 | line 598 | NUMBER | 19.08% | Return Ratio chart (ROCE/ROE) value; series and period not recoverable from text layer | CHART_UNASSIGNED
R301 | page 22 | line 598 | NUMBER | 13.97% | Return Ratio chart (ROCE/ROE) value; series and period not recoverable from text layer | CHART_UNASSIGNED
R302 | page 22 | line 598 | NUMBER | 10.40% | Return Ratio chart (ROCE/ROE) value; series and period not recoverable from text layer | CHART_UNASSIGNED
R303 | page 22 | line 598 | NUMBER | 14.71% | Return Ratio chart (ROCE/ROE) value; series and period not recoverable from text layer | CHART_UNASSIGNED
R304 | page 22 | line 605 | NUMBER | 7.28% | Return Ratio chart (ROCE/ROE) value; series and period not recoverable from text layer | CHART_UNASSIGNED
R305 | page 22 | line 605 | NUMBER | 2.09% | Return Ratio chart (ROCE/ROE) value; series and period not recoverable from text layer | CHART_UNASSIGNED
R306 | page 22 | line 605 | NUMBER | 3.88% | Return Ratio chart (ROCE/ROE) value; series and period not recoverable from text layer | CHART_UNASSIGNED
R307 | page 22 | line 592 | NUMBER | 19.62% | Return Ratio chart (ROCE/ROE) value; series and period not recoverable from text layer | CHART_UNASSIGNED
R308 | page 23 | line 635 | NUMBER | 10.0 | Face Value (Rs)
R309 | page 23 | line 636 | NUMBER | 675.0 | Market Price (BSE) Rs
R310 | page 23 | line 637 | NUMBER | 826.8 | 52 Week High Rs
R311 | page 23 | line 637 | NUMBER | 427.9 | 52 Week Low Rs
R312 | page 23 | line 638 | NUMBER | 8502.8 | Market Cap Mn (Rs)
R313 | page 23 | line 639 | NUMBER | 12.6 | Equity Shares Outstanding (Mn)
R314 | page 23 | line 640 | NUMBER | 24.0 | 1 Year Avg Trading Volume (000)
R315 | page 23 | line 637 | NUMBER | 63.26% | Shareholding as on 30 Sep 2026, Promoters | LAYOUT_ORDER
R316 | page 23 | line 637 | NUMBER | 28.95% | Shareholding as on 30 Sep 2026, Public | LAYOUT_ORDER
R317 | page 23 | line 640 | NUMBER | 1.42% | Shareholding as on 30 Sep 2026, AIF
R318 | page 23 | line 642 | NUMBER | 6.37% | Shareholding as on 30 Sep 2026, FPI
R319 | page 23 | line 622 | NUMBER | 75% | Dividend Percentage, FY24 | CHART_POSITION_INFERRED
R320 | page 23 | line 622 | NUMBER | 75% | Dividend Percentage, FY25 | CHART_POSITION_INFERRED
R321 | page 23 | line 626 | NUMBER | 10% | Dividend Percentage, FY26 | CHART_POSITION_INFERRED

## ENTITY TABLE
R### | page N | line L | TYPE | verbatim value | short context | flags
R322 | page 1 | line 19 | ENTITY | Fairchem Organics Limited | issuer, cover letter
R323 | page 1 | line 21 | ENTITY | Regd. Office & Works: 253/P and 312, Village Chekhala, Sanand-Kadi Highway, Sanand, Ahmedabad 382115, Gujarat; phone (02717) 687900/687901/+91 90163 24095; cs@fairchem.in; www.fairchem.in | ENTITY-SUMMARY address block (lines 21-29)
R324 | page 1 | line 29 | ENTITY | CIN: L24200GJ2019PLC129759 | company identification number
R325 | page 1 | line 32 | ENTITY | National Stock Exchange of India Limited (NSE), Exchange Plaza, BKC, Mumbai 400051 | addressee exchange
R326 | page 1 | line 34 | ENTITY | BSE Limited, Department of Corporate Services, Phiroze Jeejeebhoy Towers, Mumbai 400001 | addressee exchange
R327 | page 1 | line 39 | ENTITY | NSE symbol FAIRCHEMOR | trading symbol
R328 | page 1 | line 40 | ENTITY | SEBI (LODR) Regulations, 2015, Regulation 30 / Schedule III Part A | regulator and rule cited
R329 | page 1 | line 59 | ENTITY | Jatin Jain, Company Secretary & Compliance Officer, ACS-24293 | signatory (lines 59,71,73)
R330 | page 4 | line 91 | ENTITY | Fairfax India Holdings | promoter (Promoted by Fairfax India Holdings)
R331 | page 4 | line 89 | ENTITY | Monomer (Monobasic) Acid; Isostearic Acid | forward integration products from co-product stream
R332 | page 4 | line 106 | ENTITY | critical equipment/design from Germany & Switzerland | equipment origin (lines 106-108)
R333 | page 4 | line 103 | ENTITY | Export of Isostearic Acid to several countries | export statement
R334 | page 5 | line 116 | ENTITY | Acid Oil | process/product in manufacturing flow (lines 114-148)
R335 | page 5 | line 116 | ENTITY | Soft Oil (Soya/Sun/Cotton/Canola/Rice/Groundnut) | process/product in manufacturing flow (lines 114-148)
R336 | page 5 | line 116 | ENTITY | Hard Oil (Palm/Coconut) | process/product in manufacturing flow (lines 114-148)
R337 | page 5 | line 116 | ENTITY | Deodorizer Distillate | process/product in manufacturing flow (lines 114-148)
R338 | page 5 | line 116 | ENTITY | Glycerine | process/product in manufacturing flow (lines 114-148)
R339 | page 5 | line 116 | ENTITY | Fatty Acid | process/product in manufacturing flow (lines 114-148)
R340 | page 5 | line 116 | ENTITY | Linoleic Acid/Palmitic Acid | process/product in manufacturing flow (lines 114-148)
R341 | page 5 | line 116 | ENTITY | Crude Dimer | process/product in manufacturing flow (lines 114-148)
R342 | page 5 | line 116 | ENTITY | Dimer Acid/Monomer Acid | process/product in manufacturing flow (lines 114-148)
R343 | page 5 | line 116 | ENTITY | Isostearic Acid | process/product in manufacturing flow (lines 114-148)
R344 | page 5 | line 116 | ENTITY | Distilled Fatty Acid | process/product in manufacturing flow (lines 114-148)
R345 | page 5 | line 116 | ENTITY | Tocopherols/Sterol | process/product in manufacturing flow (lines 114-148)
R346 | page 5 | line 116 | ENTITY | Polyamides for Paints & Inks, Epoxy Hardeners | process/product in manufacturing flow (lines 114-148)
R347 | page 5 | line 152 | ENTITY | End industries: Paints & Inks, Soaps, Animal Feed, Cosmetics, Pharmaceuticals, FMCG, Nutraceuticals | ENTITY-SUMMARY end-industry list (lines 116-153)
R348 | page 6 | line 164 | ENTITY | Existing markets: Europe, Japan, South Korea, USA, UAE, Middle East | export markets (lines 164-170)
R349 | page 6 | line 159 | ENTITY | Acid Oil | existing portfolio product (lines 157-189)
R350 | page 6 | line 159 | ENTITY | Palmitic acid | existing portfolio product (lines 157-189)
R351 | page 6 | line 159 | ENTITY | Dimer acid | existing portfolio product (lines 157-189)
R352 | page 6 | line 159 | ENTITY | Isostearic Acid | existing portfolio product (lines 157-189)
R353 | page 6 | line 159 | ENTITY | Monomer acid | existing portfolio product (lines 157-189)
R354 | page 6 | line 159 | ENTITY | Glycerine | existing portfolio product (lines 157-189)
R355 | page 6 | line 159 | ENTITY | Pitch/Residue | existing portfolio product (lines 157-189)
R356 | page 6 | line 159 | ENTITY | Distilled fatty acid | existing portfolio product (lines 157-189)
R357 | page 6 | line 159 | ENTITY | Tocopherols/Sterols | existing portfolio product (lines 157-189)
R358 | page 6 | line 159 | ENTITY | Linoleic/Soya fatty acid | existing portfolio product (lines 157-189)
R359 | page 6 | line 159 | ENTITY | Deodorizer Distillate | existing portfolio product (lines 157-189)
R360 | page 6 | line 162 | ENTITY | Use-cases: fast drying coatings, animal feed for lactating animals, epoxy hardeners, lubricants (cold rolling mills), nylon, cosmetics, stoving paints, furnace oil substitute, undercoats, natural vitamin E, corticosteroids | ENTITY-SUMMARY use-case descriptors (lines 159-189)
R361 | page 7 | line 199 | ENTITY | Map of Indian states and Bangladesh/USA: Himachal Pradesh, Punjab, U.P, Rajasthan, Gujarat, West Bengal, Madhya Pradesh, Chhattisgarh, Dadra and Nagar Haveli, Maharashtra, Telangana, Sanand Ahmedabad; Bangladesh; USA | ENTITY-SUMMARY key customers/suppliers map (lines 199-224)
R362 | page 7 | line 216 | ENTITY | Sanand, Ahmedabad | plant location
R363 | page 8 | line 267 | ENTITY | Critical lab equipment from Switzerland, Germany (European countries) | equipment origin (lines 264-268)
R364 | page 9 | line 274 | ENTITY | ISO 9001:2015, ISO 14001:2015, ISO 45001:2018 | ENTITY-SUMMARY certification list (Quality, Environmental, Occupational Health & Safety)
R365 | page 10 | line 298 | ENTITY | Fairfax India Holdings | promoter institution
R366 | page 11 | line 313 | ENTITY | Dr. Jivraj Mehta Smarak Health Foundation | CSR recipient: sonography machines
R367 | page 11 | line 324 | ENTITY | GPCB (approved solid waste disposal site; registered recycler/co-processor) | regulator/approver (lines 324,333)
R368 | page 13 | line 348 | ENTITY | Nahoosh Jariwala, Managing Director and Chairman; formerly MD of Fairchem Speciality Limited (now Privi Speciality Chemicals Limited); bachelor of commerce Gujarat University | director (lines 348-357)
R369 | page 13 | line 348 | ENTITY | Sumit Maheshwari, Non-Executive Director; MD and CEO of Fairbridge Capital Private Limited; formerly KPMG; MBA ISB; ICAI associate member | director (lines 348-354)
R370 | page 13 | line 362 | ENTITY | Venkatraman Srinivasan, Independent Director; B.Com Univ. of Bombay; FCA; independent director at Amal Ltd, Eimco Elecon (India) Ltd, HDFC Life Insurance Co Ltd, Mahindra Logistics Ltd | director (lines 362-371)
R371 | page 13 | line 362 | ENTITY | Darius Dinshaw Pandole, Independent Director; recently retired MD and CEO of JM Financial; formerly Partner New Silk Route Advisors and IDFC Private Equity; Harvard and Univ. of Chicago | director (lines 362-368)
R372 | page 13 | line 381 | ENTITY | Sonal Vimal Ambani, Independent Director; formerly AVP at Morgan Stanley Dean Witter; masters in business administration (marketing and finance) and doctorate | director (lines 375-381)
R373 | page 13 | line 381 | ENTITY | Sudhin Choksey, Independent Director; MD of Gruh Finance until Oct 2019; independent director Gujarat Ambuja Exports Ltd, CSB Bank Ltd, Sandesh Ltd; Nominee Director India Shelter Finance Corporation Ltd; University of Mumbai; ICAI member since 1978 | director (lines 375-390)
R374 | page 13 | line 381 | ENTITY | KPMG, current statutory auditors; one of Big 4 | auditor
R375 | page 13 | line 346 | ENTITY | Governance framework: risk framework by audit committee, internal controls testing by statutory auditors, IT systems upgraded, online compliance management, business continuity plan for all plants, helpline for whistle blowing and sexual harassment | ENTITY-SUMMARY governance practices (lines 346-375)
R376 | page 15 | line 408 | ENTITY | Middle east crisis; US tariff; FTA with UK and EU; crude soya oil import duty | named external factors (lines 408-412)
R377 | page 23 | line 632 | ENTITY | Sensex (comparator index in stock chart) | comparator index
R378 | page 23 | line 639 | ENTITY | AIF; FPI; Promoters; Public (shareholding categories) | ENTITY-SUMMARY shareholder categories
R379 | page 24 | line 646 | ENTITY | Fairchem Organics Limited disclaimer and Valorem Advisors disclaimer (safe-harbor, no liability, forward-looking statements caution, Valorem certifies no stock ownership) | ENTITY-SUMMARY disclaimer legal text (lines 646-666)
R380 | page 24 | line 661 | ENTITY | Valorem Advisors, Independent Investor Relations Management Service company | investor relations adviser
R381 | page 24 | line 670 | ENTITY | Mr. Anuj Sonpal, Valorem Advisors; Tel +91-22-4903-9500; farichem@valoremadvisors.com; https://www.valoremadvisors.com/fairchem | IR contact (lines 670-674)

## FORWARD TABLE
R### | page N | line L | TYPE | verbatim value | short context | flags
R382 | page 4 | line 95 | FORWARD | Proposal to add one new throughput capacity expansion (raw material falling...) | proposed capacity addition (lines 95-99, text garbled)
R383 | page 4 | line 97 | FORWARD | The recent announcement of level playing tariff with US and proposed FTA with EU/UK augers well for our export strategy | tariff/FTA export outlook (lines 97-101)
R384 | page 6 | line 157 | FORWARD | Fairchem Organics is also entering new global markets | new markets (lines 157-158, 176)
R385 | page 6 | line 180 | FORWARD | Targeting to increase the export market share in all its prime product | export share target (lines 180-181)
R386 | page 7 | line 237 | FORWARD | "Make-in-India, Buy within India" strategy providing strong competitive moats | strategy statement
R387 | page 11 | line 321 | FORWARD | We will have Scrubber System in place in near future | air emission control
R388 | page 15 | line 408 | FORWARD | we are consciously optimistic due to lower tariff in US, FTA/likely FTA with UK and EU, recent reduction in import duty on crude soya oil from 16.5% to 11.0% likely to improve availability of raw material and in turn our capacity utilization during the year | outlook (lines 408-412)
R389 | page 21 | line 549 | FORWARD | We have currently working on 4 key strategies: 1. Cost optimization 2. Product upgradation 3. New product 4. Geographical diversification | strategy list (lines 549-554)
R390 | page 21 | line 564 | FORWARD | With current level playing tariff with US and proposed FTA with EU/UK, we aim to increase the adoption in export to initially by 25% and eventually at 50% of the sales | export share target (lines 558-566)
R391 | page 21 | line 558 | FORWARD | Cost optimization: energy savings via energy audit with significant reduction in energy; substitution of imported catalyst with domestic sourced catalyst | cost strategy (lines 558-570)
R392 | page 21 | line 558 | FORWARD | Product Upgradation: Low titre Linoleic Acid used in oil drilling industry; Distilled dimer; Fatty oil upgradation to be used in heating | product upgradation items (lines 558-570)
R393 | page 21 | line 558 | FORWARD | New product: By pass fat to be produced from PFAD; Isostearic Acid adoption in cosmetic industry; adoption of one more raw material to produce niche chemical | new product items (lines 558-574)
R394 | page 21 | line 576 | FORWARD | The above strategy will result to agile/cost efficient production operations and diversification in raw material, industry segment and geography | strategy outcome claim

## DATE TABLE
R### | page N | line L | TYPE | verbatim value | short context | flags
R395 | page 1 | line 31 | DATE | October 22, 2026 | cover letter date
R396 | page 1 | line 45 | DATE | Q2 (F.Y. 2026-27) | earnings presentation subject period
R397 | page 1 | line 48 | DATE | quarter and six months ended on September 30, 2026 | presentation reporting period (lines 48-49)
R398 | page 1 | line 69 | DATE | 2026.10.22 21:33:04 +05'30' | digital signature timestamp
R399 | page 2 | line 79 | DATE | Q2 | FY27 | title slide period
R400 | page 8 | line 264 | DATE | 2018 | R&D lab established
R401 | page 10 | line 304 | DATE | Jan-26 | buy-back concluded
R402 | page 11 | line 336 | DATE | November 2012 | fire incident
R403 | page 13 | line 350 | DATE | April, 2010 | served as MD of Fairchem Speciality since
R404 | page 13 | line 375 | DATE | Oct 2019 | Sudhin Choksey MD of Gruh Finance until
R405 | page 13 | line 390 | DATE | 1978 | ICAI membership since (Sudhin Choksey)
R406 | page 14 | line 392 | DATE | Q2 FY27 | section divider
R407 | page 15 | line 399 | DATE | Q2 FY27 | financial performance period
R408 | page 15 | line 414 | DATE | H1 FY27 | financial performance period
R409 | page 16 | line 427 | DATE | Q2 FY27, Q2 FY26, Y-O-Y | table column periods
R410 | page 17 | line 447 | DATE | H1 FY27, H1 FY26, Y-O-Y | table column periods
R411 | page 18 | line 469 | DATE | FY24, FY25, FY26, H1 FY27 | table column periods
R412 | page 19 | line 508 | DATE | FY25, FY26, H1 FY27 | balance sheet columns
R413 | page 20 | line 535 | DATE | FY25, FY26, H1 FY27 | cash flow columns
R414 | page 21 | line 547 | DATE | Business Strategy | Way forward | section
R415 | page 22 | line 580 | DATE | FY24, FY25, FY26, H1 FY27 | chart periods
R416 | page 23 | line 617 | DATE | As on 30th September, 2026 | stock market performance date
R417 | page 23 | line 634 | DATE | 30th September 2026 | price data and shareholding date
R418 | page 23 | line 626 | DATE | Oct-25 to Sep-26 | stock chart axis range (monthly)

## QUALIFIER TABLE
R### | page N | line L | TYPE | verbatim value | short context | flags
R419 | page 4 | line 97 | QUALIFIER | "with minimal capex and ... (falling ... under Oleo Chemicals only)" fragments | scope qualifier on expansion, text garbled (lines 96-99) | LAYOUT_GARBLED
R420 | page 6 | line 191 | QUALIFIER | By-products(1) | footnote marker on By-products
R421 | page 6 | line 193 | QUALIFIER | (1) Pitch/Residue are outputs of the processes run on both raw materials - Acid Oil and Deodorizer Distillate | footnote text for marker (1)
R422 | page 7 | line 230 | QUALIFIER | (in case of domestic sales) vast majority procured or sold within 500 Km radius | scope qualifier (lines 228-232)
R423 | page 8 | line 260 | QUALIFIER | "Near-zero rejections" of output stemming from strict quality controls | qualitative claim wording
R424 | page 10 | line 294 | QUALIFIER | "Leading manufacturer in India for substantial part of the overall revenue" | scope qualifier on leadership claim
R425 | page 10 | line 303 | QUALIFIER | "Majority of the capacity expansion has been undertaken primarily through internal accruals" | funding qualifier
R426 | page 11 | line 331 | QUALIFIER | Near-zero factory accidents since inception(1) | footnote marker (1)
R427 | page 11 | line 336 | QUALIFIER | (1) Fire in November 2012 (with no casualties or injuries) was the only major incident since inception | footnote text for marker (1)
R428 | page 11 | line 319 | QUALIFIER | Air emission: currently bag filters are there | current state qualifier
R429 | page 13 | line 381 | QUALIFIER | "Current auditors are KPMG, and audited by one of the Big 4 for the last 9 years" | auditor statement wording (lines 381-382)
R430 | page 15 | line 402 | QUALIFIER | Revenue improvement "on account of higher price realization primarily due to higher raw material cost and higher import finished product cost" | driver statement for H1 revenue growth (lines 401-404)
R431 | page 15 | line 405 | QUALIFIER | EBITDA margin improved "due to better realization in domestic market due to lower imports" | driver statement (lines 405-406)
R432 | page 15 | line 408 | QUALIFIER | "While the macros are uncertain due to middle east crisis" | macro caveat (line 408)
R433 | page 16 | line 429 | QUALIFIER | PARTICULARS (Rs Mn) | unit of table: Rs Million
R434 | page 17 | line 449 | QUALIFIER | PARTICULARS (Rs Mn) | unit of table: Rs Million
R435 | page 16 | line 440 | QUALIFIER | PAT w/o. Exceptional item | metric excludes exceptional item
R436 | page 17 | line 460 | QUALIFIER | PAT w/o. Exceptional item | metric excludes exceptional item
R437 | page 16 | line 432 | QUALIFIER | YoY for EBITDA margin and PAT margin shown in Bps (674 Bps, 537 Bps) | margin changes in basis points
R438 | page 16 | line 431 | QUALIFIER | Table value columns are scrambled in layout text; values mapped in pdftotext raw order; Other Comprehensive Income YoY blank in source | A1 note on layout reading | LAYOUT_NOTE
R439 | page 17 | line 451 | QUALIFIER | Table value columns scrambled in layout text; Other Income YoY and OCI YoY blank in source | A1 note on layout reading | LAYOUT_NOTE
R440 | page 18 | line 469 | QUALIFIER | PARTICULARS (Rs Mn) | unit of table: Rs Million
R441 | page 18 | line 489 | QUALIFIER | PAT w/o. Exceptional item | metric excludes exceptional item
R442 | page 18 | line 493 | QUALIFIER | Exceptional Item - New Labour code (Net of tax) | exceptional item defined net of tax; new labour code
R443 | page 18 | line 500 | QUALIFIER | 16.02* | asterisk marker on H1 FY27 EPS
R444 | page 18 | line 504 | QUALIFIER | * Not annualized | footnote text for EPS asterisk
R445 | page 19 | line 508 | QUALIFIER | ASSETS (Rs Mn) / EQUITY AND LIABILITIES (Rs Mn) | unit of table: Rs Million
R446 | page 19 | line 508 | QUALIFIER | Table text layer scrambled; values assigned to rows by pdftotext raw (content-stream) order and checked by sums (FY25 NC assets 1971+117+40+2+2+67+13=2212; current assets 883+861+13+49=1806; total 4018). Rows flagged ORDER_INFERRED; layout lines 508-531 show shifted labels. | A1 note on layout reading | LAYOUT_NOTE
R447 | page 20 | line 535 | QUALIFIER | PARTICULARS (Rs Mn) | unit of table: Rs Million (opening/closing cash shown as 0.1)
R448 | page 21 | line 562 | QUALIFIER | Export target wording ("increase ... initially by 25% and eventually at 50% of the sales") ambiguous in source; basis not stated | target wording qualifier (lines 558-566)
R449 | page 22 | line 580 | QUALIFIER | Rs Mn | unit label on Key Financial Highlights slide
R450 | page 22 | line 611 | QUALIFIER | Return Ratio chart legend: ROCE, ROE; 8 percentage values, series/period assignment not recoverable from text layer | A1 note on chart reading | CHART_UNASSIGNED
R451 | page 22 | line 582 | QUALIFIER | Slide heading spells EBITDA as "EBIDTA" | source spelling
R452 | page 23 | line 617 | QUALIFIER | Stock Market Performance (As on 30th September, 2026) | as-of date for chart
R453 | page 23 | line 634 | QUALIFIER | Price Data as of 30th September 2026 Rs | price data in Rs, as-of date
R454 | page 23 | line 640 | QUALIFIER | 1 Year Avg Trading Volume ('000) | unit thousands
R455 | page 23 | line 638 | QUALIFIER | Market Cap (Mn) | unit Rs Million
R456 | page 24 | line 647 | QUALIFIER | Information current only as of its date; no obligation to update; contains forward-looking statements; actual results may differ materially | disclaimer qualifier (lines 647-659)
R457 | page 24 | line 662 | QUALIFIER | Valorem Advisors presentation based on information the Company considers reliable; no representation or warranty on accuracy | disclaimer qualifier (lines 662-666)

## APPENDED ROWS (correction loop 1; management claims and policy bullets)
R458 | page 4 | line 95 | QUALIFIER | 30 years of legacy; Leading manufacturer in India; One of a kind manufacturing process using by-products of vegetable oils | management claim, company at a glance (lines 95-101)
R459 | page 4 | line 95 | QUALIFIER | High emphasis on Sustainability and Corporate Governance standards | management claim (lines 95-101)
R460 | page 4 | line 102 | QUALIFIER | revenue generated in very small quantities of ~1.25% (for Acid Oil) and ~0.25% (for DOD) of soft oils processed | raw material share claim (lines 100-104)
R461 | page 4 | line 103 | QUALIFIER | State-of-the-art manufacturing unit already in place with critical equipment/design from Germany & Switzerland | capability claim (lines 103-108)
R462 | page 7 | line 206 | QUALIFIER | Strong moat of secure and low-cost raw material supply | management claim (lines 206-208)
R463 | page 7 | line 199 | QUALIFIER | Green chemicals are the ingredients of choice to achieve a circular economy | management claim (lines 199-202)
R464 | page 7 | line 201 | QUALIFIER | Processing waste from edible oil refining process to produce high value oleochemicals | capability claim
R465 | page 7 | line 204 | QUALIFIER | Focus on green manufacturing processes which reduces effluents to ensure sustainability | policy claim (lines 204-205)
R466 | page 7 | line 209 | QUALIFIER | One of the Lowest Cost Producer enabling Fairchem to be the lowest cost producer globally | management claim (lines 209-212)
R467 | page 7 | line 213 | QUALIFIER | Low cost of raw material as Fairchem purchases globally waste products from oil refineries | cost claim (lines 213-214)
R468 | page 7 | line 216 | QUALIFIER | Efficient manufacturing process comparable to global peers enables it to be highly cost competitive | cost claim (lines 216-217)
R469 | page 7 | line 217 | QUALIFIER | Large off-take capability enabling strong purchasing power with suppliers | management claim (lines 217-219)
R470 | page 7 | line 220 | QUALIFIER | Operational excellence with a strategically located facility | management claim (lines 220-221)
R471 | page 7 | line 226 | QUALIFIER | Fairchem has long and meaningful relationships with the supplier base (100+ suppliers on-board) | supplier claim (lines 226-227)
R472 | page 7 | line 228 | QUALIFIER | Vast majority of Fairchem's raw material and finished products are procured or sold (in case of domestic sales) in a radius of 500 Km | sourcing claim (lines 228-232)
R473 | page 7 | line 229 | QUALIFIER | Bulk procurement at prices superior to alternative disposal options for suppliers - refineries | sourcing claim (lines 229-231)
R474 | page 7 | line 233 | QUALIFIER | Buys directly from refineries, on an 'as-is-where-is' basis at the factory gate on short payment cycles | sourcing/payment terms claim (lines 233-235)
R475 | page 8 | line 243 | QUALIFIER | Continued Investment in R&D and Innovation; state-of-the-art R&D Lab | management claim (lines 243-244)
R476 | page 8 | line 246 | QUALIFIER | Highly skilled employee base with strong engineering focus and deep experience (average experience of 10 years in the firm) | R&D claim (lines 246-249)
R477 | page 8 | line 251 | QUALIFIER | Capable of offering blends specific to customer requirements at short notice | R&D claim (lines 251-253)
R478 | page 8 | line 255 | QUALIFIER | Low switching cost of process lines | R&D claim (line 255)
R479 | page 8 | line 257 | QUALIFIER | Built the capability to expand and contract production as required | R&D claim (lines 257-258)
R480 | page 8 | line 260 | QUALIFIER | 'Near-zero rejections' of output stemming from strict quality controls | R&D claim (lines 260-261)
R481 | page 10 | line 282 | QUALIFIER | Major Player in the Indian Oleo Chemical Market Using Renewable Resources | management claim (line 282)
R482 | page 10 | line 283 | QUALIFIER | Processing waste generated during edible oil refining process to produce high value oleo chemicals giving it price advantage | competitive claim
R483 | page 10 | line 284 | QUALIFIER | Enjoy Leadership Position in the industry due to barriers to entry | competitive claim
R484 | page 10 | line 285 | QUALIFIER | Focus on green manufacturing processes which reduce effluents to ensure sustainability | policy claim
R485 | page 10 | line 288 | QUALIFIER | Well entrenched Customer Relationships in high growth industries like Paint, Inks, FMCG, lubricants, cosmetics | customer claim
R486 | page 10 | line 289 | QUALIFIER | Long lasting customer relationships of more than 15 years with various customers | customer claim
R487 | page 10 | line 290 | QUALIFIER | More than 20 years relationship with key raw material suppliers | supplier claim
R488 | page 10 | line 293 | QUALIFIER | Low cost of raw material and efficient manufacturing process enables it to be highly cost competitive vis a vis global peers | cost claim
R489 | page 10 | line 294 | QUALIFIER | Leading manufacturer in India for substantial part of the overall revenue | competitive claim
R490 | page 10 | line 295 | QUALIFIER | Position to market entire quantity of Prime Products it produces | demand claim
R491 | page 10 | line 298 | QUALIFIER | Fairchem is well supported by an esteemed Promoter Institution - Fairfax India Holdings | promoter claim
R492 | page 10 | line 299 | QUALIFIER | Strong and experienced management team that have positioned business well for continued growth and development | management claim
R493 | page 10 | line 300 | QUALIFIER | Strong R&D team focusing on integration and green chemistry | management claim
R494 | page 10 | line 303 | QUALIFIER | Majority of the capacity expansion has been undertaken primarily through internal accruals | capital efficiency claim
R495 | page 10 | line 304 | QUALIFIER | Recently concluded buy-back of INR 340 Mn in Jan-26 | capital allocation claim
R496 | page 10 | line 305 | FORWARD | Judicious strategy on capacity expansion by evaluating market demand-supply scenario and working very closely with its customer base | capacity expansion policy
R497 | page 11 | line 313 | QUALIFIER | Dr. Jivraj Mehta Smarak Health Foundation - Purchase of advanced high-end sonography machines; measures benefitting Armed forces, Police Forces, Paramilitary forces, veterans, war widows and dependents; equipment for animal welfare | CSR/social initiatives (lines 313-323)
R498 | page 11 | line 313 | QUALIFIER | Effluent: Water Discharge - Zero Liquid Discharge by Multi Effect Evaporator and Agitated Thin Film Dryer | environment claim (lines 313-316)
R499 | page 11 | line 324 | QUALIFIER | Solid waste (non-hazardous) sent to GPCB approved Solid Waste Disposable site; hazardous waste sent to GPCB approved registered Recycler / Co-processor | environment claim (lines 324-333)
R500 | page 11 | line 313 | FORWARD | Always be adequately capitalized | governance policy (line 313)
R501 | page 11 | line 315 | FORWARD | Not overleverage the balance sheet | governance policy (line 315)
R502 | page 11 | line 316 | FORWARD | Secure sources of sustainable raw material supply | governance policy (lines 316-318)
R503 | page 11 | line 319 | FORWARD | Invest in backward and forward integration | governance policy (line 319)
R504 | page 11 | line 320 | FORWARD | Transparent communications with all the stakeholders | governance policy (line 320)
R505 | page 11 | line 323 | FORWARD | Low volatility in the cash flow generation | governance policy (line 323)
R506 | page 11 | line 324 | QUALIFIER | Employees are given training on fire safety, first aid, housekeeping and cleanliness practices | social claim (lines 324-327)
R507 | page 11 | line 328 | QUALIFIER | Production equipment tested every three years by external firm | safety claim (lines 328-329)
R508 | page 11 | line 331 | QUALIFIER | Near-zero factory accidents since inception(1) | safety claim (lines 331-332), footnote at line 336
R509 | page 13 | line 344 | QUALIFIER | High profile Board which has taken several initiatives to improve the corporate governance framework | governance claim
R510 | page 6 | line 173 | QUALIFIER | Designed especially to produce stoving paints; fast drying protective coating with lighter color; improved bonding; increases life span of nylon | product claims (lines 159-171)
R511 | page 6 | line 180 | QUALIFIER | Utilized as a substitute for burning fuel i.e. furnace oil | product claim (line 180)
R512 | page 6 | line 188 | QUALIFIER | To be used as natural anti-oxidant and to manufacture Natural vitamin E; raw material for cortico steroids | product claim (lines 188-189)
