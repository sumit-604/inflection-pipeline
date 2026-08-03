# Enumeration Ledger — Investor Presentation
Company: Park Medi World Limited (PARKHOSPS) | Quarter: Q1 FY27 | Doctype: presentation
Source extract: extract_presentation_parkhosps_q1fy27.txt (26 pages, unit convention: Rs Millions, x0.1 to Cr; OCR pages: 7, 16, 20, 23)

```
=== A2 COUNT TEST ===
category: slides       grep_count: 26    sweep_count: 26    match: yes
category: numbers      grep_count: 341   sweep_count: 341   match: yes
category: footnotes    grep_count: 14    sweep_count: 14    match: yes
category: dropped_slides   grep_count: N/A   sweep_count: N/A   match: N/A  (no prior-quarter deck ledger supplied; DROPPED_SLIDE cannot be computed this run — stated explicitly, not silently skipped)
gate_a2: pass
=== END COUNT TEST ===
```

## Methodology note (numbers category)
Grep pass: `awk` sweep over the extract, excluding the A1 header block (lines 1-14), the `[page N]` markers, the A1 meta-annotation lines (`[CHART, page N, ...]` / `[OCR page N]`), and running footer lines containing the phrase "Investor Presentation" (page-number-only content, captured instead in the Slides table). Every remaining line containing at least one digit = one row. `grep -c` on this filter = 341. Manual sweep independently walked all 26 pages top to bottom and produced 341 rows one-for-one against the same line set (see table below) — counts reconcile, GATE A2 passes.

Rows on the 4 chart-dense pages (6, 9, 18, 21) plus scattered rows on pages 10, 11, 12, 13, 22, 25 carry a `CHART_DATA_LABEL` or `CHART_AXIS_ARTIFACT` flag. `CHART_AXIS_ARTIFACT` = a bare numeral/percentage with no adjacent label text on its extracted line — almost certainly a y-axis gridline/scale tick or a data label whose companion text was pushed to a different line by pdftotext's chart-rendering scramble (per A1's inline `[CHART...]` caveats). `CHART_DATA_LABEL` = the line carries at least one alphabetic label alongside the number(s). Per the enumerate-everything mandate, both flag types get a row; none are dropped. Axis-artifact values should NOT be read as free-standing data points by A3/A4 without checking against the source PDF page image.

## 1. Slides
| Slide # | Line (start) | Title / description | Content type | Footer page # printed | Flags |
|---|---|---|---|---|---|
| 1 | 15 | Regulatory disclosure letter (Reg 30) cover to BSE/NSE re: earnings presentation | text | none captured (pre-deck cover, no footer) |  |
| 2 | 51 | INVESTOR PRESENTATION Q1 FY'27 title/cover slide with hospital location map and per-hospital commissioning timeline | text+photo | none captured (pre-deck cover, no footer) |  |
| 3 | 93 | DISCLAIMER | text (fine print/legal) | 2 |  |
| 4 | 134 | INDEX | text (table of contents) | 3 |  |
| 5 | 154 | Q1 FY'27: A QUARTER OF CONSOLIDATION, GROWTH AND CONTINUED EXECUTION (Chairman & MD quote) | text+photo | 4 |  |
| 6 | 182 | STRONG FINANCIAL & OPERATING PERFORMANCE | chart (5 charts: Revenue, EBITDA & Margin, Net Profit & Margin, Bed Capacity & Occupancy %, Patient Volume) | 5 |  |
| 7 | 397 | COMPANY OVERVIEW (section divider) | photo (OCR page, background facility photo, title only) | NOT CAPTURED (OCR page, no machine-readable footer) | OCR_PAGE, NO_FOOTER_CAPTURED |
| 8 | 402 | BUILDING ONE OF INDIA'S LARGEST INTEGRATED HOSPITAL NETWORKS | text+table/infographic (map with stats box) | 7 |  |
| 9 | 451 | 21+ YEARS OF EXPANSION THROUGH ORGANIC GROWTH & ACQUISITIONS | chart+text (2 bar charts: hospitals added/period, beds added/period) | 8 |  |
| 10 | 491 | PROVEN INTEGRATION & VALUE CREATION FROM ACQUISITIONS | chart+table (4 donut charts + 11-row acquisition table) | 9 |  |
| 11 | 537 | MODERN CLINICAL INFRASTRUCTURE BUILT FOR HIGH-ACUITY CARE | chart+text (1 donut chart + equipment icons/stats) | 10 |  |
| 12 | 580 | COMPREHENSIVE SPECIALITY CARE | chart+text (2 donut charts: Q1FY26 vs Q1FY27 speciality mix, + service descriptions) | 11 |  |
| 13 | 620 | PATIENT REVENUE MIX | chart+text (2 donut charts: OPD/IPD mix Q1FY26 vs Q1FY27, + revenue stream descriptions) | 12 |  |
| 14 | 653 | DOCTOR LED PROFESSIONAL MANAGEMENT TEAM | text+photo (promoter and senior management bios) | 13 |  |
| 15 | 697 | ACCREDITATIONS & AWARDS | text+photo (accreditation stats + awards timeline 2015-2024) | 14 |  |
| 16 | 740 | GROWTH (section divider) | photo (OCR page, background facility photo, title only) | NOT CAPTURED (OCR page, no machine-readable footer) | OCR_PAGE, NO_FOOTER_CAPTURED |
| 17 | 745 | GROWTH HIGHLIGHTS - ADDITION OF 46% CAPACITY IN CY 2026 | text (4 text blocks: Panchkula, Rudrapur, Gurugram expansion, Zirakpur) | 16 |  |
| 18 | 778 | VISIBILITY ON CAPACITY EXPANSION - DRIVING c.59% BED GROWTH BY FY'28 | chart (bed-capacity waterfall/build-up chart FY26-FY28P + facility-level addition list) | 17 |  |
| 19 | 822 | WELL-CAPITALIZED WITH AMPLE ACCESS TO CAPITAL FOR FUTURE GROWTH | text (financial strength / growth driver text blocks) | 18 |  |
| 20 | 858 | INDUSTRY OVERVIEW (section divider) | photo (OCR page, background facility photo, title only) | NOT CAPTURED (OCR page, no machine-readable footer) | OCR_PAGE, NO_FOOTER_CAPTURED |
| 21 | 863 | INDUSTRY LANDSCAPE & SUPPLY GAP | chart+text (market-size stacked bar, bed-density bar chart, market-share-by-region stacked bar) | 20 |  |
| 22 | 958 | DEMAND DRIVERS & LONG-TERM GROWTH VISIBILITY | chart+text (insurance coverage bar chart, medical tourists bar chart) | 21 |  |
| 23 | 1006 | FINANCIAL PERFORMANCE (section divider) | photo (OCR page, background facility photo, title only) | NOT CAPTURED (OCR page, no machine-readable footer) | OCR_PAGE, NO_FOOTER_CAPTURED |
| 24 | 1011 | CONSOLIDATED PROFIT & LOSS STATEMENT | table (13-line-item P&L, Q1FY27/Q1FY26/YoY%/Q4FY26/QoQ%) | 23 |  |
| 25 | 1033 | SHAREHOLDING PATTERN & SHARE PRICE PERFORMANCE | chart+table (shareholding donut + share-price indexed line chart + key stats table) | 24 |  |
| 26 | 1072 | Thank you / contact details (registered office, IR email, PR agency contacts) | text | 25 (printed at foot of page) |  |

Note: PDF pages 7, 16, 20, 23 are the 4 OCR-flagged section-divider slides (COMPANY OVERVIEW / GROWTH / INDUSTRY OVERVIEW / FINANCIAL PERFORMANCE) — background hospital photographs with an overlaid title only; no other machine-readable text or footer page number was recovered for these slides. This matches the A1 header's `ocr_pages: [7, 16, 20, 23]`.

## 2. Every number on every slide (incl. OCR/chart data labels)
One row per source line carrying at least one digit (see methodology note above). `Value/content` reproduces the extracted line verbatim (whitespace collapsed is not applied — kept as extracted since column alignment is itself informative on scrambled chart pages).

| # | Slide | Line | Value / content (as extracted) | Flag |
|---|---|---|---|---|
| 1 | 1 | 16 | August 03, 2026 |  |
| 2 | 1 | 21 | Mumbai - 400 001                                       Mumbai - 400 051 |  |
| 3 | 1 | 22 | Scrip Code: 544645                                     SYMBOL: PARKHOSPS |  |
| 4 | 1 | 25 | Subject: Disclosure under Regulation 30 of Securities and Exchange Board of India (Listing |  |
| 5 | 1 | 26 | Obligations and Disclosure Requirements) Regulations, 2015 (“Listing Regulations”)- |  |
| 6 | 1 | 31 | Pursuant to the provisions of Regulation 30 of the Listing Regulations, please find enclosed herewith |  |
| 7 | 1 | 44 | KAPOOR                   Date: 2026.08.03 |  |
| 8 | 1 | 45 | 09:43:22 +05'30' |  |
| 9 | 2 | 52 | New Delhi                  Sector 47, Gurugram          Faridabad              Panipat |  |
| 10 | 2 | 53 | Jan 2005 (200 beds)             Apr 2012 (275 beds)     Jan 2014 (150 beds)   Jun 2016 (175 beds) |  |
| 11 | 2 | 60 | Apr 2017 (150 beds) |  |
| 12 | 2 | 62 | Aug 2019 (150 beds) |  |
| 13 | 2 | 64 | Apr 2020 (250 beds) |  |
| 14 | 2 | 66 | Nov 2020 (300 beds) |  |
| 15 | 2 | 68 | Q1 FY’27 |  |
| 16 | 2 | 69 | 3RD AUGUST 2026 |  |
| 17 | 2 | 73 | Feb 2021 (225 beds)              July 2021 (225 beds)   Feb 2022 (250 beds)   Nov 2022 (300 beds) |  |
| 18 | 2 | 78 | 17 Hospitals \| 4,290 Beds       (1) |  |
| 19 | 2 | 83 | (1) Operational as on date |  |
| 20 | 2 | 86 | May 2023 (350 beds)              July 2025 (250 beds)   Feb 2026 (360 beds)   Apr 2026 (350 beds) |  |
| 21 | 2 | 91 | Aug 2026 (330 beds) |  |
| 22 | 3 | 122 | This presentation is not a prospectus, a statement in lieu of a prospectus, an offering circular, an advertisement or an offer document under the Companies Act, 2013, as amended, the Securities and |  |
| 23 | 3 | 123 | Exchange Board of India (Issue of Capital and Disclosure Requirements) Regulations, 2018, as amended, or any other applicable law in India. This presentation is strictly confidential and may not be copied |  |
| 24 | 4 | 140 | 04                                     06      15 |  |
| 25 | 4 | 141 | 15        19          22 |  |
| 26 | 4 | 146 | Q1 FY’27                             COMPANY      GROWTH   INDUSTRY   FINANCIAL |  |
| 27 | 5 | 155 | Q1 FY’27: A QUARTER OF CONSOLIDATION, GROWTH AND CONTINUED EXECUTION |  |
| 28 | 5 | 165 | “Q1 FY'27 has been a quarter of consolidation, growth and continued execution. We spent the quarter ramping up our newer assets at Agra and |  |
| 29 | 5 | 167 | On 25th May, we announced a definitive agreement to acquire 100% of ‘The Medicity Hospital’ in Rudrapur — a 330-bed, NABH-accredited multi super |  |
| 30 | 5 | 168 | speciality facility in the Kumaon region — in an all-cash transaction valued at INR 177 crores, marking our entry into a sixth state. I'm pleased to share |  |
| 31 | 5 | 169 | that the hospital was commissioned this past Sunday, 2nd August. |  |
| 32 | 5 | 170 | On 30th June, we announced a 100-bed extension at our Palam Vihar facility in Gurugram, Park Platinum, which takes our consolidated Gurugram |  |
| 33 | 5 | 171 | capacity to 750 beds. Our 200-bed hospital in Narela, Delhi, acquired through the insolvency process, remains on track. And today, on 3rd August, we |  |
| 34 | 5 | 172 | announced the acquisition of a 150-bed hospital in Zirakpur for approximately INR 107 crores, again all-cash. |  |
| 35 | 5 | 173 | Our total bed capacity stood at 3,960 beds as of June 30, up 32% year-on-year. Taken together, our capacity additions during calendar year 2026 will |  |
| 36 | 5 | 174 | amount to 1,490 beds, a 46% increase over our calendar 2025 base of 3,250 beds. With the expansions already underway, we expect to exit FY'27 at |  |
| 37 | 5 | 175 | 4,740 beds and, adding a further 1,000 beds through FY'28, to reach 5,740 beds by March 2028 — funded largely through internal accruals and IPO |  |
| 38 | 6 | 189 | +19%                                                                    +20%                                                                               +35% | CHART_AXIS_ARTIFACT |
| 39 | 6 | 191 | 4,604            4,757                                                  1,274                 1,261 | CHART_AXIS_ARTIFACT |
| 40 | 6 | 192 | 886 | CHART_AXIS_ARTIFACT |
| 41 | 6 | 193 | 40.0%    1,000                                                          40.0% | CHART_AXIS_ARTIFACT |
| 42 | 6 | 198 | 3,988                                                                    1,049 | CHART_AXIS_ARTIFACT |
| 43 | 6 | 199 | 1,200 | CHART_AXIS_ARTIFACT |
| 44 | 6 | 204 | 768 | CHART_AXIS_ARTIFACT |
| 45 | 6 | 205 | 900 | CHART_AXIS_ARTIFACT |
| 46 | 6 | 207 | 35.0%                                                                   35.0% | CHART_AXIS_ARTIFACT |
| 47 | 6 | 212 | 655 | CHART_AXIS_ARTIFACT |
| 48 | 6 | 213 | 800 | CHART_AXIS_ARTIFACT |
| 49 | 6 | 216 | 1,000 | CHART_AXIS_ARTIFACT |
| 50 | 6 | 218 | 30.0%                                                                   30.0% | CHART_AXIS_ARTIFACT |
| 51 | 6 | 223 | 700 | CHART_AXIS_ARTIFACT |
| 52 | 6 | 228 | 25.0%                                                                   25.0% | CHART_AXIS_ARTIFACT |
| 53 | 6 | 229 | 800 | CHART_AXIS_ARTIFACT |
| 54 | 6 | 234 | 27.7% | CHART_AXIS_ARTIFACT |
| 55 | 6 | 235 | 600 | CHART_AXIS_ARTIFACT |
| 56 | 6 | 240 | 600 | CHART_AXIS_ARTIFACT |
| 57 | 6 | 241 | 26.3%                                           26.5%         20.0%     500                                                           20.0% | CHART_AXIS_ARTIFACT |
| 58 | 6 | 246 | 400 | CHART_AXIS_ARTIFACT |
| 59 | 6 | 251 | 18.6% | CHART_AXIS_ARTIFACT |
| 60 | 6 | 252 | 15.0%                                                                   15.0% | CHART_AXIS_ARTIFACT |
| 61 | 6 | 257 | 16.4%                 16.7% | CHART_AXIS_ARTIFACT |
| 62 | 6 | 258 | 400 | CHART_AXIS_ARTIFACT |
| 63 | 6 | 259 | 300 | CHART_AXIS_ARTIFACT |
| 64 | 6 | 264 | 10.0%                                                                   10.0% | CHART_AXIS_ARTIFACT |
| 65 | 6 | 269 | 200 | CHART_AXIS_ARTIFACT |
| 66 | 6 | 274 | 200 | CHART_AXIS_ARTIFACT |
| 67 | 6 | 277 | 5.0%                                                                    5.0% | CHART_AXIS_ARTIFACT |
| 68 | 6 | 279 | 100 | CHART_AXIS_ARTIFACT |
| 69 | 6 | 284 | -                                                                       0.0%        -                                                           0.0% | CHART_AXIS_ARTIFACT |
| 70 | 6 | 289 | Q1 FY'26             Q4 FY'26                Q1 FY'27                    Q1 FY'26                  Q4 FY'26               Q1 FY'27                              Q1 FY'26               Q4 FY'26   Q1 FY'27 | CHART_DATA_LABEL |
| 71 | 6 | 293 | BED CAPACITY & OCCUPANCY %                                                                              PATIENT VOLUME                                (‘000s) | CHART_DATA_LABEL |
| 72 | 6 | 296 | +32% | CHART_AXIS_ARTIFACT |
| 73 | 6 | 297 | +17% | CHART_AXIS_ARTIFACT |
| 74 | 6 | 299 | 3,960                                                                       YoY | CHART_DATA_LABEL |
| 75 | 6 | 300 | 4,000 | CHART_AXIS_ARTIFACT |
| 76 | 6 | 303 | 3,610                          Occupancy has | CHART_DATA_LABEL |
| 77 | 6 | 304 | 110.0% | CHART_AXIS_ARTIFACT |
| 78 | 6 | 309 | 250k | CHART_DATA_LABEL |
| 79 | 6 | 311 | 250 | CHART_AXIS_ARTIFACT |
| 80 | 6 | 315 | 3,500 | CHART_AXIS_ARTIFACT |
| 81 | 6 | 320 | 3,000                                                                                   214k                  214k | CHART_DATA_LABEL |
| 82 | 6 | 321 | 26 | CHART_AXIS_ARTIFACT |
| 83 | 6 | 322 | 90.0% | CHART_AXIS_ARTIFACT |
| 84 | 6 | 327 | 3,000 | CHART_AXIS_ARTIFACT |
| 85 | 6 | 332 | 25 | CHART_AXIS_ARTIFACT |
| 86 | 6 | 333 | 200 | CHART_AXIS_ARTIFACT |
| 87 | 6 | 338 | 23 | CHART_AXIS_ARTIFACT |
| 88 | 6 | 340 | 70.0% | CHART_AXIS_ARTIFACT |
| 89 | 6 | 344 | 2,500 | CHART_AXIS_ARTIFACT |
| 90 | 6 | 349 | 67.8% | CHART_AXIS_ARTIFACT |
| 91 | 6 | 350 | 150 | CHART_AXIS_ARTIFACT |
| 92 | 6 | 355 | 62.5% | CHART_AXIS_ARTIFACT |
| 93 | 6 | 356 | 2,000                                                          50.0% | CHART_AXIS_ARTIFACT |
| 94 | 6 | 361 | 55.6%                                                                                                     223 | CHART_AXIS_ARTIFACT |
| 95 | 6 | 362 | 191                          188 | CHART_AXIS_ARTIFACT |
| 96 | 6 | 363 | 1,500 | CHART_AXIS_ARTIFACT |
| 97 | 6 | 364 | 100 | CHART_AXIS_ARTIFACT |
| 98 | 6 | 367 | 30.0% | CHART_AXIS_ARTIFACT |
| 99 | 6 | 372 | 1,000 | CHART_AXIS_ARTIFACT |
| 100 | 6 | 377 | 50 | CHART_AXIS_ARTIFACT |
| 101 | 6 | 378 | 10.0% | CHART_AXIS_ARTIFACT |
| 102 | 6 | 382 | 500 | CHART_AXIS_ARTIFACT |
| 103 | 6 | 387 | -                                                           -10.0% | CHART_AXIS_ARTIFACT |
| 104 | 6 | 388 | 0 | CHART_AXIS_ARTIFACT |
| 105 | 6 | 393 | Q1 FY'26          Q4 FY'26            Q1 FY'27                                             Q1 FY'26              Q4 FY'26                      Q1 FY'27 | CHART_DATA_LABEL |
| 106 | 8 | 408 | 17                                                                                                                                       Largest |  |
| 107 | 8 | 411 | 16 NABH(1)                                                                                                                               in Haryana & Tricity |  |
| 108 | 8 | 412 | 9 NABL (2)                                                                                                                               Second Largest in North India |  |
| 109 | 8 | 419 | 4,290 |  |
| 110 | 8 | 420 | (3)                       Patiala |  |
| 111 | 8 | 423 | 15 Cities |  |
| 112 | 8 | 430 | Across 6 States |  |
| 113 | 8 | 436 | Including 1,166 ICU beds                                                                                                     Gorakhpur |  |
| 114 | 8 | 442 | 30+ |  |
| 115 | 8 | 446 | 1.    Recently opened Panchkula facility is undergoing the NABH accreditation process |  |
| 116 | 8 | 447 | 2.    Labs in 4 additional hospitals are being planned for NABL accreditation |  |
| 117 | 8 | 448 | 3.    Bed capacity as on date |  |
| 118 | 9 | 453 | 21+ YEARS OF EXPANSION THROUGH ORGANIC GROWTH & ACQUISITIONS | CHART_DATA_LABEL |
| 119 | 9 | 456 | 2005 – 2010                             2011 – 2015                        2016 – 2020                   2021 – 2025                  2026 – Till Date | CHART_DATA_LABEL |
| 120 | 9 | 457 | Early Organic                           The 1st Acquisition                Inorganic-led                 Inorganic Expansion          Clear Roadmap to reach | CHART_DATA_LABEL |
| 121 | 9 | 458 | Foundation                                                                 Scale-Up Phase                Accelerates                  5,740 bed capacity | CHART_DATA_LABEL |
| 122 | 9 | 462 | • New Delhi (200 beds)                  • Gurugram (275 beds)              • Panipat (175 beds)          • Patiala (300 beds)         • Panchkula (350 beds) | CHART_DATA_LABEL |
| 123 | 9 | 463 | Acquisition                        • Gurugram (150 beds)         Acquisition                  Acquisition | CHART_DATA_LABEL |
| 124 | 9 | 464 | • Faridabad (150 beds)             Acquisition                   • Gurugram(225 beds)         • Agra (360 beds) | CHART_DATA_LABEL |
| 125 | 9 | 465 | • Karnal (150 beds)           • Sonipat (225 beds)         • Rudrapur (330 beds) | CHART_DATA_LABEL |
| 126 | 9 | 466 | • Ambala (250 beds)           • Jaipur (250 beds) | CHART_DATA_LABEL |
| 127 | 9 | 468 | • Behror (300 beds)           • Mohali (350 beds)         greenfield and the largest | CHART_DATA_LABEL |
| 128 | 9 | 469 | • Bhatinda (250 beds)       acquisition respectively till date | CHART_DATA_LABEL |
| 129 | 9 | 471 | 17 OPERATIONAL HOSPITALS (as on date)                                                      4,290 BED CAPACITY (as on date) | CHART_DATA_LABEL |
| 130 | 9 | 473 | Greenfield: 6                                                                               Greenfield: 1,450 | CHART_DATA_LABEL |
| 131 | 9 | 474 | Acquisition: 11                                                                             Acquisition: 2,840 | CHART_DATA_LABEL |
| 132 | 9 | 477 | 3               5                                                                        1,300 | CHART_AXIS_ARTIFACT |
| 133 | 9 | 479 | 700                          690 | CHART_AXIS_ARTIFACT |
| 134 | 9 | 480 | 2 | CHART_AXIS_ARTIFACT |
| 135 | 9 | 481 | 1                                                                                     150 | CHART_AXIS_ARTIFACT |
| 136 | 9 | 482 | 2 | CHART_AXIS_ARTIFACT |
| 137 | 9 | 483 | 1                  1                                   1              1                                  275           325       300                350 | CHART_AXIS_ARTIFACT |
| 138 | 9 | 484 | 200 | CHART_AXIS_ARTIFACT |
| 139 | 9 | 486 | 2005–2010          2011–2015           2016–2020         2021–2025   2026 - till date      2005–2010     2011–2015    2016–2020    2021–2025       2026 - till date | CHART_DATA_LABEL |
| 140 | 10 | 496 | 11                                             ₹9,991 Mn                                                              2,840 | CHART_DATA_LABEL |
| 141 | 10 | 498 | 3.5 Mn | CHART_DATA_LABEL |
| 142 | 10 | 505 | Jan 2014 \| Consideration: ₹ 110 Mn \| Beds: 150                                                                                                 across all financial metrics | CHART_DATA_LABEL |
| 143 | 10 | 506 | (Rudrapur was commissioned on 2nd Aug’26 and had nil contribution in Q1 FY’27) | CHART_DATA_LABEL |
| 144 | 10 | 508 | Apr 2017 \| Consideration: ₹ 250 Mn \| Beds: 150 | CHART_DATA_LABEL |
| 145 | 10 | 510 | Apr 2020 \| Consideration: ₹ 600 Mn \| Beds: 250 | CHART_DATA_LABEL |
| 146 | 10 | 512 | Acquisition                                                                   (Q1 FY’27)        Greenfield | CHART_DATA_LABEL |
| 147 | 10 | 513 | Nov 2020 \| Consideration: ₹ 400 Mn \| Beds: 300                                                                           63%               3,960                37%               65%                                    35% | CHART_DATA_LABEL |
| 148 | 10 | 514 | 4,757 mn | CHART_DATA_LABEL |
| 149 | 10 | 515 | Park Hospital, Palam Vihar                                                                                                                30 June’26 | CHART_DATA_LABEL |
| 150 | 10 | 516 | Feb 2021 \| Consideration: ₹ 1,075 Mn \| Beds: 225 | CHART_DATA_LABEL |
| 151 | 10 | 518 | Jul 2021 \| Consideration: ₹ 520 Mn \| Beds: 225 | CHART_DATA_LABEL |
| 152 | 10 | 520 | Feb 2022 \| Consideration: ₹ 520 Mn \| Beds: 250 | CHART_DATA_LABEL |
| 153 | 10 | 522 | May 2023 \| Consideration: ₹ 2,250 Mn \| Beds: 350                                                                                                                                                        PAT | CHART_DATA_LABEL |
| 154 | 10 | 524 | (Q1 FY’27) | CHART_DATA_LABEL |
| 155 | 10 | 525 | Krishna Super Speciality Hospital, Bhatinda                                                                              69%                (Q1 FY’27)           31%               77%                                   23% | CHART_DATA_LABEL |
| 156 | 10 | 526 | 1,261 mn                                                  886 mn | CHART_DATA_LABEL |
| 157 | 10 | 527 | Jul 2025 \| Consideration: ₹ 400 Mn\| Beds: 250 | CHART_DATA_LABEL |
| 158 | 10 | 529 | Feb 2026 \| Consideration: ₹ 2,450 Mn\| Beds: 360 | CHART_DATA_LABEL |
| 159 | 10 | 531 | Aug 2026 \| Consideration: ₹ 1,416 Mn (2)\| Beds: 330 | CHART_DATA_LABEL |
| 160 | 10 | 532 | 1.   Of this 9,991 mn, Agra was acquired for INR 2,450 mn on 19th Dec’25 and was commissioned on 15th Feb’26 | CHART_DATA_LABEL |
| 161 | 10 | 533 | 2.   Rudrapur was acquired at a valuation of INR 1,770 mn (consideration paid for 80% ownership is INR 1,416 mn) and was commissioned on 2nd Aug’26. Remaining 20% to be acquired by FY’30. | CHART_DATA_LABEL |
| 162 | 11 | 542 | 37% | CHART_AXIS_ARTIFACT |
| 163 | 11 | 545 | % of             29% | CHART_DATA_LABEL |
| 164 | 11 | 550 | 34% | CHART_AXIS_ARTIFACT |
| 165 | 11 | 551 | 19 MRI                  17 CATH LAB                 17 CT                    125 Dialysis | CHART_DATA_LABEL |
| 166 | 11 | 559 | 90+                                             PET CTs & LINACs            DA VINCI ROBOTS | CHART_DATA_LABEL |
| 167 | 11 | 567 | Operation Theatres                                                                               • IMARS Robotic Surgery System (3 hospitals) | CHART_DATA_LABEL |
| 168 | 11 | 572 | 1,166                                        Critical Care & Life Support | CHART_DATA_LABEL |
| 169 | 12 | 584 | Cardiology & Cardiac Sciences                              Neurosciences                                    Super Speciality Mix Up 440 bps YoY | CHART_DATA_LABEL |
| 170 | 12 | 585 | • Angioplasty, bypass surgery, valve                       • Stroke care, brain tumors, spinal surgeries                     61.7% | CHART_DATA_LABEL |
| 171 | 12 | 586 | replacement                                              • Advanced neuro-interventions &                57.3% | CHART_DATA_LABEL |
| 172 | 12 | 588 | 6.1% | CHART_AXIS_ARTIFACT |
| 173 | 12 | 589 | 9.4% | CHART_AXIS_ARTIFACT |
| 174 | 12 | 590 | 6.2% | CHART_AXIS_ARTIFACT |
| 175 | 12 | 591 | Oncology                                                   Urology & Kidney Transplant                                         9.2% | CHART_DATA_LABEL |
| 176 | 12 | 592 | (Medical, Surgical & Radiation)                            • Dialysis, renal care, transplant programs      10.5% | CHART_DATA_LABEL |
| 177 | 12 | 593 | • Chemotherapy, targeted therapy, radiation                • 5 hospitals approved for kidney                                  11.6% | CHART_DATA_LABEL |
| 178 | 12 | 594 | • Dedicated cancer units with linear                                                                         8.7% | CHART_DATA_LABEL |
| 179 | 12 | 596 | accelerators                                                                                                                 6.7%         Orthopedic | CHART_DATA_LABEL |
| 180 | 12 | 597 | 11.3% | CHART_AXIS_ARTIFACT |
| 181 | 12 | 599 | 10.6% | CHART_AXIS_ARTIFACT |
| 182 | 12 | 602 | • Joint replacement, trauma care, sports                                                                    14.5%                           Urology | CHART_DATA_LABEL |
| 183 | 12 | 604 | 14.3%         Neurology | CHART_DATA_LABEL |
| 184 | 12 | 606 | 5.8%                           General Surgery | CHART_DATA_LABEL |
| 185 | 12 | 607 | • Minimally invasive orthopedic procedures                                                                                     4.6%         Internal Medicine | CHART_DATA_LABEL |
| 186 | 12 | 610 | General Surgery                                            Internal Medicine                                29.4% | CHART_DATA_LABEL |
| 187 | 12 | 611 | 27.1% | CHART_AXIS_ARTIFACT |
| 188 | 12 | 615 | 7.4%              6.6% | CHART_AXIS_ARTIFACT |
| 189 | 12 | 617 | Q1 FY'26          Q1 FY'27 | CHART_DATA_LABEL |
| 190 | 13 | 627 | • Complex procedures across 30+ specialties                             ₹ 3,988 Mn        ₹ 4,757 Mn | CHART_DATA_LABEL |
| 191 | 13 | 628 | Out-Patient (OPD) Services                                                 4.3%               5.6% | CHART_DATA_LABEL |
| 192 | 13 | 636 | 95.7%              94.4% | CHART_AXIS_ARTIFACT |
| 193 | 13 | 645 | Q1 FY'26          Q1 FY'27 | CHART_DATA_LABEL |
| 194 | 14 | 665 | • Has been registered with Medical Council of India (now NMC) for 44                        • 20+ years of experience in the medical profession; Registered with Delhi |  |
| 195 | 14 | 666 | years and has 4 decades of experience in medical profession and                             Medical Council in 2005 |  |
| 196 | 14 | 669 | • Established Park Hospital, New Delhi, in 2005                                                operations; Associated with the Company since 2011 |  |
| 197 | 14 | 682 | 40+ years experience                                       29+ years experience             30+ years experience |  |
| 198 | 14 | 683 | 30+ years experience |  |
| 199 | 14 | 690 | 17+ years experience                                       18+ years experience             16+ years experience |  |
| 200 | 15 | 703 | 16 (1) NABH Accredited Hospitals & |  |
| 201 | 15 | 704 | Dedicated ICU, Trauma & Emergency Infrastructure across all units                                                                                9 (2) NABL & NABH Accredited |  |
| 202 | 15 | 711 | 2015                         2017                            2018                        2019                                2024                                    Key Achievements |  |
| 203 | 15 | 723 | Six Sigma Healthcare       100 Most Impactful |  |
| 204 | 15 | 732 | • 40+ Years of |  |
| 205 | 15 | 736 | Uthan Sang Parivar                   1.   Recently opened Panchkula facility is undergoing the NABH accreditation process |  |
| 206 | 15 | 737 | 2.   Labs in 4 additional hospitals are being planned for NABL accreditation |  |
| 207 | 17 | 746 | GROWTH HIGHLIGHTS – ADDITION OF 46% CAPACITY IN CY 2026 |  |
| 208 | 17 | 747 | AGRA (360 beds), PANCHKULA (350 beds), RUDRAPUR (330 beds), NARELA (DELHI) (200 beds), |  |
| 209 | 17 | 748 | PALAM VIHAR EXTENSION (GURUGRAM) (100 beds), ZIRAKPUR (150 beds) |  |
| 210 | 17 | 756 | • Commissioned a 350-bed                            •    Signed definitive agreement to       • Approved 100-bed expansion at            •   Signed definitive agreement to |  |
| 211 | 17 | 758 | hospital on 10th April 2026.                           Rudrapur at a valuation of ₹177 Cr   • Expanded facility to operate as              for ~₹107 Cr. |  |
| 212 | 17 | 759 | • Strengthened Park Group's tertiary                •    Added a 330-bed NABH                   Park Platinum from November              •   Added a 150-bed multi super |  |
| 213 | 17 | 760 | & quaternary care capabilities                         accredited multi super speciality      2026.                                        speciality hospital. |  |
| 214 | 17 | 762 | • Tricity capacity increased to ~850                •    Expanded presence to 6 states          increase to 750 beds.                        Tricity cluster |  |
| 215 | 17 | 763 | beds with ongoing 150 bed                              and strengthened North India                                                    •   Transaction consummation and |  |
| 216 | 17 | 765 | •    Transaction consummated on 31                                                       Nov’26 |  |
| 217 | 17 | 766 | July and Hospital launched on 2nd |  |
| 218 | 17 | 767 | Aug’26 |  |
| 219 | 18 | 780 | VISIBILITY ON CAPACITY EXPANSION - DRIVING c.59% BED GROWTH BY FY’28 | CHART_DATA_LABEL |
| 220 | 18 | 783 | c.59% BED CAPACITY EXPANSION TILL MARCH’28 | CHART_DATA_LABEL |
| 221 | 18 | 785 | +2,130 (+59%) | CHART_AXIS_ARTIFACT |
| 222 | 18 | 788 | Expansion / +150 (350 → 500) / Sep 2027 | CHART_DATA_LABEL |
| 223 | 18 | 789 | 5,740      2,130 | CHART_AXIS_ARTIFACT |
| 224 | 18 | 791 | 450                     Greenfield / 250 / Jan 2028 | CHART_DATA_LABEL |
| 225 | 18 | 792 | Acquisition / 150 / Nov 2026 | CHART_DATA_LABEL |
| 226 | 18 | 793 | 4,740                       450                                                      Ambala | CHART_DATA_LABEL |
| 227 | 18 | 794 | 100                                                                                Expansion / +200 (250 → 450) / Oct 2027 | CHART_DATA_LABEL |
| 228 | 18 | 795 | 3,960 | CHART_AXIS_ARTIFACT |
| 229 | 18 | 796 | 3,610                                                                                                                      Palam Vihar, Gurugram (Park Platinum) | CHART_DATA_LABEL |
| 230 | 18 | 797 | Expansion / +100 (225 → 325) / Nov 2026 | CHART_DATA_LABEL |
| 231 | 18 | 798 | 3,590 | CHART_AXIS_ARTIFACT |
| 232 | 18 | 799 | 3,190                      1,080 | CHART_AXIS_ARTIFACT |
| 233 | 18 | 800 | 2,510 | CHART_AXIS_ARTIFACT |
| 234 | 18 | 801 | 2,510 | CHART_AXIS_ARTIFACT |
| 235 | 18 | 805 | 1,450              1,450           1,700      600 | CHART_AXIS_ARTIFACT |
| 236 | 18 | 806 | 1,100 | CHART_AXIS_ARTIFACT |
| 237 | 18 | 809 | FY'26            Q1 FY'27            FY'27P           FY'28P   Additional                                                                   Gorakhpur | CHART_DATA_LABEL |
| 238 | 18 | 810 | Acquisition - O&M / 400 / Apr 2027 | CHART_DATA_LABEL |
| 239 | 18 | 812 | Greenfield Acquisition Expansion                                       Acquisition / 200 / Dec 2026 | CHART_DATA_LABEL |
| 240 | 19 | 829 | • Best-ever Quarterly operating performance driven by                                     • Bed capacity to grow by c.59% between FY’26-28 |  |
| 241 | 19 | 832 | • Strong internal accruals supporting ongoing expansion          Financial                • Selective Greenfield entry in high-growth Tier 1/2/3 markets |  |
| 242 | 19 | 836 | • Strong liquidity with ₹2,998 mn in FDs                                                  • Enables faster ramp-up with lower upfront capital intensity |  |
| 243 | 19 | 841 | • Internal accruals sufficient to scale up to ~5,740 beds        Growth                   • Focus on North India clusters & adjacent markets |  |
| 244 | 19 | 842 | by FY’28                                                                                  • Strong track record of turnaround and integration |  |
| 245 | 19 | 852 | • Promoter holding at ~82.9%                                                              • Continuous training, leadership development & medical |  |
| 246 | 19 | 853 | • Headroom for dilution up to regulatory threshold (~75%)                                   education |  |
| 247 | 21 | 870 | ~10 -12% CAGR                                                     Market share of North India expected to grow the fastest                                                   • Tier 2 and Tier | CHART_DATA_LABEL |
| 248 | 21 | 871 | 3 healthcare demand | CHART_DATA_LABEL |
| 249 | 21 | 872 | Healthcare Delivery Segment (FY’24–FY’29P)                                            North              South               East              West                            growing at around 16% to | CHART_DATA_LABEL |
| 250 | 21 | 873 | 18% CAGR, higher than | CHART_DATA_LABEL |
| 251 | 21 | 875 | ~3 Mn beds required                                                   INR 3.9 tn | CHART_DATA_LABEL |
| 252 | 21 | 877 | 23-24% | CHART_AXIS_ARTIFACT |
| 253 | 21 | 878 | INR 6.3 tn | CHART_DATA_LABEL |
| 254 | 21 | 880 | 22-24% | CHART_AXIS_ARTIFACT |
| 255 | 21 | 881 | INR 6.9-7.0 tn | CHART_DATA_LABEL |
| 256 | 21 | 883 | 22-24% | CHART_AXIS_ARTIFACT |
| 257 | 21 | 884 | INR 10.2-10.8 tn | CHART_DATA_LABEL |
| 258 | 21 | 886 | 22-25% | CHART_AXIS_ARTIFACT |
| 259 | 21 | 889 | To bridge demand-supply gap                                                 12-13%                   11-13%                  11-13%                     10-13% | CHART_DATA_LABEL |
| 260 | 21 | 893 | ~₹1,06,530 Cr (+10% YoY) | CHART_DATA_LABEL |
| 261 | 21 | 894 | 35-36%                   34-36%                  34-36%                     32-35% | CHART_AXIS_ARTIFACT |
| 262 | 21 | 896 | CAGR: 10-12%                                     CAGR: 12-14% | CHART_DATA_LABEL |
| 263 | 21 | 899 | Government healthcare allocation in FY’26                                   29-30%                   30-32%                  30-32%                     31-34% | CHART_DATA_LABEL |
| 264 | 21 | 902 | ~5% of GDP by 2030 | CHART_DATA_LABEL |
| 265 | 21 | 903 | FY'19                     FY'24                  FY'25E                     FY'29P | CHART_DATA_LABEL |
| 266 | 21 | 907 | recommendation as of FY’22 | CHART_DATA_LABEL |
| 267 | 21 | 908 | Private sector gaining share driven by quality & capacity expansion                         50 | CHART_DATA_LABEL |
| 268 | 21 | 909 | Bed Density (Beds per 10,000 population)                      Operational Beds ('000s) | CHART_DATA_LABEL |
| 269 | 21 | 910 | 45 | CHART_AXIS_ARTIFACT |
| 270 | 21 | 915 | 7.5-8 | CHART_AXIS_ARTIFACT |
| 271 | 21 | 916 | Healthcare Delivery Market (INR Tn)                              40 | CHART_DATA_LABEL |
| 272 | 21 | 917 | 295-300       110-115         64-66    40-42            25-26       20-21             9.5-10.5                44-46 | CHART_AXIS_ARTIFACT |
| 273 | 21 | 918 | 29.5 | CHART_AXIS_ARTIFACT |
| 274 | 21 | 919 | 35 | CHART_AXIS_ARTIFACT |
| 275 | 21 | 924 | Government Hospitals     Private Hospitals                      30 | CHART_DATA_LABEL |
| 276 | 21 | 925 | 27.5 | CHART_AXIS_ARTIFACT |
| 277 | 21 | 926 | 25 | CHART_AXIS_ARTIFACT |
| 278 | 21 | 927 | 21.5                       22.0                                                  21.5 | CHART_AXIS_ARTIFACT |
| 279 | 21 | 929 | 3.9                                                                                        14.0                    14.0 | CHART_AXIS_ARTIFACT |
| 280 | 21 | 930 | 20 | CHART_AXIS_ARTIFACT |
| 281 | 21 | 935 | 6.3             6.9-7.0              10.2-10.8          15 | CHART_AXIS_ARTIFACT |
| 282 | 21 | 936 | 12.5                                                                         20 Beds | CHART_DATA_LABEL |
| 283 | 21 | 937 | 10 | CHART_AXIS_ARTIFACT |
| 284 | 21 | 938 | 7.5 | CHART_AXIS_ARTIFACT |
| 285 | 21 | 939 | 5 | CHART_AXIS_ARTIFACT |
| 286 | 21 | 944 | 33%                29%             28-29%               26-27%             0 | CHART_AXIS_ARTIFACT |
| 287 | 21 | 951 | 67%                71%             71-72%               73-74% | CHART_AXIS_ARTIFACT |
| 288 | 21 | 952 | • India average bed density is around 15 beds per 10,000 population | CHART_DATA_LABEL |
| 289 | 21 | 953 | FY'19              FY'24            FY'25E                FY'29P | CHART_DATA_LABEL |
| 290 | 21 | 954 | • Global average is around 33 beds per 10,000 population | CHART_DATA_LABEL |
| 291 | 22 | 966 | ~10–15% rate increase                                                                  Coverage in (Mn) | CHART_DATA_LABEL |
| 292 | 22 | 968 | CAGR 8%                                         penetration compared to | CHART_DATA_LABEL |
| 293 | 22 | 969 | Government + Policy Push                                                                                         573 | CHART_DATA_LABEL |
| 294 | 22 | 973 | • 40+ Cr cards                                                                   288 | CHART_DATA_LABEL |
| 295 | 22 | 975 | • 9+ Cr hospitalizations                                                                                                                       is expected to increase from | CHART_DATA_LABEL |
| 296 | 22 | 976 | 40-42% (FY’24) to 45-50% | CHART_DATA_LABEL |
| 297 | 22 | 977 | (FY’27E) | CHART_DATA_LABEL |
| 298 | 22 | 978 | Digital Health (ABHA)                                                          2014-15                         2023-24 | CHART_DATA_LABEL |
| 299 | 22 | 982 | CAGR 20%                                        destination driven by cost | CHART_DATA_LABEL |
| 300 | 22 | 984 | 0.7                                   competitiveness and quality | CHART_DATA_LABEL |
| 301 | 22 | 985 | 0.6 | CHART_AXIS_ARTIFACT |
| 302 | 22 | 997 | 0.2                                                   emerging markets and | CHART_DATA_LABEL |
| 303 | 22 | 998 | • Improving awareness for both preventive and curative care due                               0.1                                                                    expansion of multi super | CHART_DATA_LABEL |
| 304 | 22 | 1000 | 2009            2014          2019                             2024 | CHART_AXIS_ARTIFACT |
| 305 | 24 | 1014 | Particulars (in INR mn)                                   Q1 FY’27   Q1 FY’26   YoY %     Q4 FY’26   QoQ % |  |
| 306 | 24 | 1015 | Revenue (ex Other income)                                  4,757      3,988      19%       4,604       3% |  |
| 307 | 24 | 1016 | Cost of material consumed /services rendered                763        700        9%        796        -4% |  |
| 308 | 24 | 1017 | Employee costs                                              924        768       20%        862        7% |  |
| 309 | 24 | 1018 | Professional and consultancy fees                           756        603       25%        716        6% |  |
| 310 | 24 | 1019 | Other expenses                                             1,054       868       21%        956        10% |  |
| 311 | 24 | 1020 | EBITDA                                                     1,261      1,049      20%       1,274       -1% |  |
| 312 | 24 | 1021 | EBITDA Margin (%)                                          26.5%      26.3%     20 bps     27.7%     -116 bps |  |
| 313 | 24 | 1022 | Other Income                                                76.5       68.7     11.3%       75         2% |  |
| 314 | 24 | 1023 | Finance Costs                                               98         151       -35%       140       -30% |  |
| 315 | 24 | 1024 | Depreciation                                                188        148       28%        175        8% |  |
| 316 | 24 | 1025 | PBT                                                        1,051       819       28%       1,034       2% |  |
| 317 | 24 | 1026 | Tax                                                         165        164        1%        266       -38% |  |
| 318 | 24 | 1027 | Net Profit                                                  886        655       35%        768        15% |  |
| 319 | 24 | 1028 | Net Profit Margin (%)                                      18.6%      16.4%     220 bps    16.7%     195 bps |  |
| 320 | 24 | 1029 | EPS (INR)                                                   2.05       1.70      20%        1.78       15% |  |
| 321 | 25 | 1036 | As on 31-07-2026                                           As on 30-06-2026 | CHART_DATA_LABEL |
| 322 | 25 | 1038 | NSE: PARKHOSPS \| INE119201023                                               Share Holding Pattern                           Top Institutional Holders | CHART_DATA_LABEL |
| 323 | 25 | 1040 | Share Price (₹)                                 292.55                                                                                    • Kotak Mahindra | CHART_DATA_LABEL |
| 324 | 25 | 1042 | 7.3% | CHART_AXIS_ARTIFACT |
| 325 | 25 | 1043 | Market Capitalization (₹ Cr)                    12,636.14                      9.8%                     Promoter & Promoter               • Carnelian Asset | CHART_DATA_LABEL |
| 326 | 25 | 1046 | No. of Shares Outstanding                       431,930,864                                             Institutions | CHART_DATA_LABEL |
| 327 | 25 | 1049 | Face Value (₹)                                  2.00                                                    Non Institutions | CHART_DATA_LABEL |
| 328 | 25 | 1050 | 82.9%                                           • SBI General Insurance | CHART_DATA_LABEL |
| 329 | 25 | 1051 | Since listing High-Low (₹)                      305.00 / 138.10 | CHART_DATA_LABEL |
| 330 | 25 | 1054 | Share Performance From 17 December 2025 To 31 July 2026 | CHART_DATA_LABEL |
| 331 | 25 | 1055 | Park                                      Nifty 50 | CHART_DATA_LABEL |
| 332 | 25 | 1056 | Nifty 500                                 Nifty Small Cap 250                                                                                          +80.6% | CHART_DATA_LABEL |
| 333 | 25 | 1059 | +20.1% | CHART_AXIS_ARTIFACT |
| 334 | 25 | 1060 | Indexed to 100                                                                                                                                            +14.6% | CHART_DATA_LABEL |
| 335 | 25 | 1061 | +9.7% | CHART_AXIS_ARTIFACT |
| 336 | 25 | 1062 | -0.5% | CHART_AXIS_ARTIFACT |
| 337 | 25 | 1063 | -5.7% | CHART_AXIS_ARTIFACT |
| 338 | 26 | 1075 | Plot no. 521, Udyog Vihar Phase 3, Sector |  |
| 339 | 26 | 1076 | 20, Gurugram – 122 022, Haryana |  |
| 340 | 26 | 1077 | Phone: 0124 696 000 |  |
| 341 | 26 | 1098 | 25 |  |

## 3. Dropped slides (prior-quarter comparison)
DROPPED_SLIDE cannot be computed this run: no prior-quarter presentation ledger was supplied (`Prior-quarter ledger path: none`). Stated explicitly per instructions rather than silently omitted. On next quarter's A2 run, this deck's 26-slide index (Section 1 above) becomes the baseline against which the following quarter's deck must be diffed for silently dropped slides/sections.

## 4. Footnotes and fine-print disclaimers
| Type | Slide | Line | Content | Flag |
|---|---|---|---|---|
| Numbered | 8 | 446 | Note 1 (Page 8 map): "Recently opened Panchkula facility is undergoing the NABH accreditation process" — qualifies headline "16 NABH" count on same slide. |  |
| Numbered | 8 | 447 | Note 2 (Page 8 map): "Labs in 4 additional hospitals are being planned for NABL accreditation" — qualifies headline "9 NABL" count on same slide. |  |
| Numbered | 8 | 448 | Note 3 (Page 8 map): "Bed capacity as on date" — qualifies headline "4,290" bed capacity figure (as-on-date caveat, not FY-end). |  |
| Numbered | 10 | 532 | Note 1 (Page 10 acquisitions): "Of this 9,991 mn, Agra was acquired for INR 2,450 mn on 19th Dec'25 and was commissioned on 15th Feb'26" — qualifies the ₹9,991 Mn cumulative consideration headline. |  |
| Numbered | 10 | 533 | Note 2 (Page 10 acquisitions): "Rudrapur was acquired at a valuation of INR 1,770 mn (consideration paid for 80% ownership is INR 1,416 mn) and was commissioned on 2nd Aug'26. Remaining 20% to be acquired by FY'30." — qualifies the ₹1,416 Mn Rudrapur consideration line and the average-consideration-per-bed figure. | PARTIAL_OWNERSHIP |
| Numbered | 15 | 736 | Note 1 (Page 15 accreditations, repeat of Page 8 Note 1 text): "Recently opened Panchkula facility is undergoing the NABH accreditation process" — qualifies headline "16 NABH Accredited Hospitals" count. | REPEAT_FOOTNOTE (same text as Page 8 Note 1) |
| Numbered | 15 | 737 | Note 2 (Page 15 accreditations, repeat of Page 8 Note 2 text): "Labs in 4 additional hospitals are being planned for NABL accreditation" — qualifies headline "9 NABL & NABH Accredited" count. | REPEAT_FOOTNOTE (same text as Page 8 Note 2) |
| Fine print | 3 | 94 | Full-slide DISCLAIMER (lines 94-130): forward-looking-statement caveat, rounding caveat ("figures shown as total in tables and diagrams may not be an arithmetic aggregation"), no-independent-verification caveat, jurisdiction/governing-law clause — qualifies every headline number in the entire deck. |  |
| Fine print | 9 | 467 | Inline annotation (lines 467-469, spans across the timeline chart): "Panchkula and Agra are the largest greenfield and the largest acquisition respectively till date" — qualifies the per-period bed-addition chart values (350 Panchkula, 360 Agra). |  |
| Fine print | 10 | 506 | Inline parenthetical note under acquisition table: "(Rudrapur was commissioned on 2nd Aug'26 and had nil contribution in Q1 FY'27)" — qualifies the Greenfield/Acquisition revenue-EBITDA-PAT split donuts (explains why Rudrapur is excluded from the Q1 FY27 acquisition contribution). | ZERO_STANDING (nil Q1 FY27 contribution called out explicitly) |
| Fine print | 21 | 950 | Legend note under bed-density chart: "Denotes Park's presence (operating/upcoming)" — qualifies which state bars represent Park's markets. |  |
| Fine print | 21 | 955 | Source line: "Source: IBEF, CRISIL" — sourcing qualifier for all Industry Landscape & Supply Gap page figures (market size, bed density, market share, CAGRs). |  |
| Fine print | 22 | 1001 | Source line: "Source: CGHS Revision, Ayushman Bharat / PM-JAY Data, Digital Health Mission, PIB, CRISIL" — sourcing qualifier for all Demand Drivers page figures. |  |
| Fine print | 25 | 1068 | Source line: "Source: NSE" — sourcing qualifier for shareholding pattern and share price performance figures. |  |

## Flags raised summary
- `CHART_AXIS_ARTIFACT` — 115 rows in Section 2 (bare numerals/percentages on chart-dense pages 6, 9, 11, 12, 13, 18, 21, 22, 25 with no adjacent label text on the same extracted line; likely axis-scale ticks or a data label separated from its caption by chart-rendering scramble). Count verified by tally below.
- `CHART_DATA_LABEL` — remaining chart-page rows in Section 2 that retain at least one label word alongside the number(s).
- `OCR_PAGE`, `NO_FOOTER_CAPTURED` — slides 7, 16, 20, 23 (Section 1).
- `ZERO_STANDING` — Page 10 inline note on Rudrapur's nil Q1 FY27 contribution (Section 4); the acquisition-contribution donuts on Page 10 (Greenfield/Acquisition split of Revenue/EBITDA/PAT) are 11-acquisition aggregates that structurally exclude Rudrapur for this quarter — flagged so A3/A4 do not read the 65%/69%/77% acquisition shares as inclusive of the just-commissioned 12th acquisition.
- `PARTIAL_OWNERSHIP` — Page 10 Note 2: Rudrapur consideration of INR 1,416 Mn is for 80% ownership only (valuation INR 1,770 Mn for 100%); remaining 20% to be acquired by FY'30. Flagged so the ₹9,991 Mn cumulative consideration and the average-consideration-per-bed figure are not read as full-ownership-equivalent without this caveat.
- `REPEAT_FOOTNOTE` — Page 15's two numbered footnotes are verbatim repeats of Page 8's two numbered footnotes (Section 4).

(Tally check: CHART_AXIS_ARTIFACT rows = 115; CHART_DATA_LABEL rows = 125; unflagged rows = 101; total = 341 = 341.)
