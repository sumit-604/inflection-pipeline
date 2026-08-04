# LEDGER — Uniparts India Ltd (UNIPARTS) — Q1 FY2026-27 (quarter ended June 30, 2026) — Doctype: presentation
Source: /home/user/inflection-pipeline/runs/uniparts-q1fy27/work/extract_presentation_uniparts_q1fy27.txt (25 pages, formfeed_count 25, line_count 820, unit convention INR Mn except page 5 narrative which is native INR crore per A1 header)
Prior-quarter ledger: NONE supplied — this is the first quarterly run for this company. DROPPED_SLIDE comparison is therefore not applicable to any row below; this ledger becomes the baseline for the next quarter's diff.

=== A2 COUNT TEST ===
category: slides             grep_count: 25    sweep_count: 25    match: yes
category: numbers            grep_count: 612   sweep_count: 612   match: yes
category: footnotes          grep_count: 8     sweep_count: 8     match: yes
category: entities            grep_count: 6     sweep_count: 6     match: yes
gate_a2: pass
=== END COUNT TEST ===

Methodology note (for reconciliation, both passes applied consistently):
- SLIDES: grep `^\[page (\d+)\]$` on the extract → 25 matches (page 1 through page 25). Manual sweep read every formfeed-delimited page top to bottom → 25 distinct slides/pages, none skipped, none duplicated. Match.
- NUMBERS: grep pass used `[0-9][0-9,]*(\.[0-9]+)?%?x?` applied to every content line, EXCLUDING (a) the `[page N]` structural marker line itself (25 lines, not document content) and (b) the page-1 digital-signature DN/hash/timestamp block (lines 47-59, treated below as one signature-block row per the RESULTS FILING digital-signature convention rather than as discrete numeric tokens) → 612 raw numeric tokens. Manual sweep walked every one of the 234 content lines carrying at least one number (listed as rows N1-N234 below, each row's token count reconciled against the source line) and summed to 612. Match.
- FOOTNOTES: grep `Note:|^\s*\*+[A-Za-z]|Safe Harbor$|INR Mn, Segment revenue` → 8 raw line hits (lines 100, 261, 305, 379, 450, 534, 557, 575). Manual sweep excluded line 557 as a false positive (it is the chart-title label repeating the asterisk glyphs of the page-17 footnotes, not a footnote definition) and split line 575 into its two distinct definitions (Working Capital Days single-asterisk, Fixed Assets Turnover double-asterisk) → 8 distinct footnote/fine-print units. Match (8 = 8, coincidental cancellation of one false positive against one split).
- ENTITIES: grep count of named corporate entities on the page-23 Group Structure org chart (UIL, GFPL, GCPL, UIG, UUL, UOI) → 6. Manual sweep of the org-chart lines (753-767) confirms the same 6, including the ownership-percentage arrows (100% UIL→four subsidiaries; 100% UUL→UOI). Match.

---

## TABLE 1 — SLIDES (every page of the 25-page deck: number, title, content type, TOC section)

| Slide | Line (marker) | Title / heading | Content type | TOC section | Flags |
|---|---|---|---|---|---|
| 1 | 15 | Reg 30 covering letter to BSE/NSE (Scrip Code 543689 / Symbol UNIPARTS) | text, regulatory cover letter + digital signature block | front matter (not in TOC) | |
| 2 | 79 | Uniparts India Limited — Earnings Presentation Q1FY27 (title slide) | text, cover/title | front matter (not in TOC) | |
| 3 | 87 | Safe Harbor | text, legal/forward-looking-statement disclaimer, full page | front matter (not in TOC) | |
| 4 | 133 | Content (table of contents: Q1FY27 Performance / Business Overview / Annexures) | text, TOC | front matter (not in TOC) | |
| 5 | 152 | Management's Message | text, narrative quotes attributed to Mr. Gurdeep Soni (Promoter, Chairman & MD), co-signed Mr. Paramjit Singh Soni (Promoter, Vice Chairman & Executive Director) | Q1FY27 Performance | |
| 6 | 188 | Operating Environment Update (Construction Equipment; Small Agriculture) | text, segment commentary | Q1FY27 Performance | |
| 7 | 210 | Operating Environment Update (Large Agriculture; Aftermarket) | text, segment commentary | Q1FY27 Performance | |
| 8 | 232 | Key Takeaways from Q1 FY27 | chart + table, 3 bar-chart trios (Total Income, EBITDA & margin, PAT & margin) with YoY/data labels, plus headline KPI table (Total Income, EBITDA, PBT, PAT) | Q1FY27 Performance | |
| 9 | 267 | Q1FY27 Results (Consolidated) | table, full quarterly P&L Q1FY27 vs Q4FY26 vs Q1FY26 with QoQ/YoY change columns | Q1FY27 Performance | ZERO_STANDING (see Table 2, row N69) |
| 10 | 301 | Revenue Distribution | chart, 4 donut/pie chart groups (Product Vertical, Geographical Presence, Market Presence OEM/AFM, Segmental Presence Agri/CFM) each for FY25/FY26/Q1FY27 | Q1FY27 Performance | |
| 11 | 349 | Content (TOC repeat, divider into Business Overview) | text, TOC divider | (divider) | |
| 12 | 368 | Product Categories | photo + text, 5 product category labels (Three Point Linkage, Precision Machine Parts, Power Take Off, Fabrication, Hydraulic Cylinders) | Business Overview | |
| 13 | 382 | Additional Synergistic Offerings to Extend System Boundaries | text + table, 3-column comparison (PTO / Hydraulic Cylinders / Fabrication: Description, Key Highlights, Features) plus 4 value-proposition callouts | Business Overview | |
| 14 | 419 | Leading Global Supplier of Critical Components Solutions | text + photo, 3PL/PMP revenue-contribution split, market-size and customer-count callouts | Business Overview | |
| 15 | 453 | Warehouse and Manufacturing Facilities | text + photo/map, facility count/location and capacity callouts | Business Overview | DANGLING_FOOTNOTE (see Table 2, row N113) |
| 16 | 488 | Global Delivery Model De-Risks Clients' Supply Chain | table + chart, 3-column delivery-model comparison (Local Delivery / Direct Export / Warehouse Sales) plus customer-concentration bar chart (Top customer / Top 5 / Top 10) FY25/FY26/Q1FY27 | Business Overview | |
| 17 | 537 | Key Financial Metrics — Historical | chart, 6 trend charts FY23-FY26 (RoCE %, Reported EPS, Debt/Equity, Working Capital Days*, Fixed Assets Turnover**, Cash Flow from Operations) | Business Overview | |
| 18 | 578 | Organisational Strengths | text, 5 bullet stats (leadership experience, geographic spread, engineer headcount, BD/sales headcount, staff tenure) | Business Overview | |
| 19 | 611 | Historical Profit and Loss | table, full P&L FY24/FY25/FY26 | Business Overview | |
| 20 | 645 | Historical Balance Sheet | table, full balance sheet (Assets and Equity & Liabilities) FY24/FY25/FY26 | Business Overview | |
| 21 | 689 | Content (TOC repeat, divider into Annexures) | text, TOC divider | (divider) | |
| 22 | 708 | Key Milestones | text/timeline, company history 1994-2025 | Annexures | |
| 23 | 747 | Group Structure | chart, org chart of UIL + 5 subsidiaries/step-down subsidiaries | Annexures | |
| 24 | 770 | Leadership Team and Board | text + photo, 9 leadership/board profiles | Annexures | BIO_TEXT_MISALIGNED (see Table 4) |
| 25 | 804 | Thank You (IR contact details) | text, contact block | Annexures | |

DROPPED_SLIDE check: not applicable — no prior-quarter ledger was supplied for comparison (input explicitly states NONE). This ledger is the baseline; the next quarter's A2 run should diff its 25-slide TOC structure (front matter 4 pages / Q1 Performance 6 pages incl. 2 TOC dividers / Business Overview 9 pages / Annexures 4 pages) against this one and flag any slide present here but absent there.

---

## TABLE 2 — NUMBERS / DISCLOSURE UNITS ON EVERY SLIDE (every numeric token, grouped one row per source line; 234 rows, 612 tokens total)

| Row | Slide | Line | Token ct | Values | Context (source line, whitespace-collapsed) | Flags |
|---|---|---|---|---|---|---|
| N1 | 1 | 17 | 2 | 04, 2026 | August 04, 2026 (letter date) | |
| N2 | 1 | 20 | 1 | 1 | Phiroze Jeejeebhoy Towers Exchange Plaza, C-1, Block G (BSE/NSE address) | |
| N3 | 1 | 21 | 2 | 400, 001 | Dalal Street, Mumbai – 400 001 (BSE pincode) | |
| N4 | 1 | 22 | 2 | 400, 051 | Bandra (E), Mumbai – 400 051 (NSE pincode) | |
| N5 | 1 | 24 | 1 | 543689 | Scrip Code: 543689 (BSE) | |
| N6 | 1 | 27 | 1 | 30 | Subject: Regulation 30 (SEBI LODR reference) | |
| N7 | 1 | 28 | 2 | 30, 2026 | quarter ended June 30, 2026 | |
| N8 | 1 | 32 | 1 | 30 | Pursuant to Regulation 30 of the SEBI (LODR) Regulations | |
| N9 | 1 | 33 | 1 | 2015 | SEBI (LODR) Regulations, 2015 | |
| N10 | 1 | 34 | 1 | 30 | quarter ended June 30 (repeat reference) | |
| N11 | 1 | 35 | 1 | 2026 | 2026 (quarter end year, repeat) | |
| N12 | 1 | 72 | 5 | 5, 6, 7, 110, 070 | Regd. Office address: Gripwel House, Block-5, LSC, C 6 & 7, Vasant Kunj, New Delhi-110 070 | |
| N13 | 1 | 73 | 6 | 91, 11, 26137979, 91, 11, 26133195 | Regd office Tel +91 11 26137979 / Fax +91 11 26133195 | |
| N14 | 1 | 74 | 5 | 1, 208, 1, 2, 201305 | Corporate Office: 1st Floor, B 208, A1 & A2, Phase-II, Noida-201305 | |
| N15 | 1 | 75 | 6 | 91, 120, 4581400, 91, 120, 4581499 | Corporate office Tel +91 120 4581400 / Fax +91 120 4581499 | |
| N16 | 1 | 77 | 4 | 9001, 2008, 14001, 2004 | ISO 9001:2008 & 14001:2004 certification | |
| N17 | 1 | 78 | 3 | 74899, 1994, 061753 | CIN: L74899DL1994PLC061753 | |
| — | 1 | 46-59 | (not counted as numbers) | Jatin Mahajan / Head Legal, Company Secretary and Compliance Officer / digitally signed / DN incl. pseudonym, postal code, serial number hash / Date: 2026.08.04 17:48:09 +05'30' | Digital signature block — see Table 5 | see Table 5 |
| N18 | 2 | 86 | 2 | 1, 27 | Earnings Presentation – Q1FY27 | |
| N19 | 3 | 94 | 1 | 2013 | the Companies Act, 2013 | |
| N20 | 3 | 95 | 1 | 2018 | SEBI (ICDR) Regulations, 2018 | |
| N21 | 3 | 132 | 1 | 2 | slide footer page number "2" | |
| N22 | 4 | 138 | 3 | 1, 2, 7 | "Q1FY27 Performance" heading (stylised spacing) | |
| N23 | 4 | 151 | 1 | 3 | slide footer page number "3" | |
| N24 | 5 | 158 | 1 | 27 | "first quarter of FY27" | |
| N25 | 5 | 164 | 1 | 3 | "first customer deliveries from the warehouse expected in Q3" (Mexico) | |
| N26 | 5 | 166 | 4 | 1, 27, 27%, 55% | "Q1 FY27 performance... revenue growth of 27% YoY, EBITDA growth of 55% YoY" | |
| N27 | 5 | 167 | 1 | 64% | "PAT growth of 64% year-on-year" | |
| N28 | 5 | 173 | 3 | 39.97, 27%, 20% | TTM EPS INR 39.97; ROCE >27%; ROE 20% (narrative, native units) | |
| N29 | 5 | 174 | 2 | 1, 190 | "net cash position at the end of Q1 stands at INR 190 crore" (native crore, do not re-convert) | |
| N30 | 5 | 175 | 3 | 101, 2025, 210 | special dividend INR 101cr declared October 2025; cash balance then ~INR 210 crore (native crore) | |
| N31 | 5 | 179 | 1 | 225 | TTM new-business order book "over INR 225 crore" (native crore) | |
| N32 | 5 | 181 | 1 | 3 | "three product platforms 3PL, PMP, and fabrications" | |
| N33 | 5 | 187 | 1 | 4 | slide footer page number "4" | |
| N34 | 6 | 196 | 3 | 2025, 1, 27 | "second half of CY2025 has continued into Q1 FY27" | |
| N35 | 6 | 209 | 1 | 5 | slide footer page number "5" | |
| N36 | 7 | 218 | 1 | 2026 | "Leading OEMs have indicated that CY2026 represents the cyclical bottom" | |
| N37 | 7 | 219 | 1 | 2027 | "more meaningful recovery expected through CY2027" | |
| N38 | 7 | 224 | 3 | 12%, 1, 27 | "Aftermarket represents approximately 12% of revenues in Q1 FY27" | |
| N39 | 7 | 231 | 1 | 6 | slide footer page number "6" | |
| N40 | 8 | 233 | 2 | 1, 27 | "Key Takeaways from Q1 FY27" heading | |
| N41 | 8 | 238 | 2 | 1, 27 | "Q1FY27" column label | |
| N42 | 8 | 239 | 4 | 3,552, 898, 746, 566 | Total Income INR 3,552 Mn / EBITDA INR 898 Mn / PBT INR 746 Mn / PAT INR 566 Mn | |
| N43 | 8 | 240 | 4 | 27.2%, 55.3%, 67.0%, 64.3% | YoY growth: Total Income 27.2%, EBITDA 55.3%, PBT 67.0%, PAT 64.3% | |
| N44 | 8 | 245 | 6 | 20.7%, 24.0%, 25.3%, 12.3%, 15.1%, 15.9% | EBITDA margin trio (Q1FY26/Q4FY26/Q1FY27) + PAT margin trio | |
| N45 | 8 | 247 | 1 | 27.2% | Total Income chart YoY data label (duplicate of N43) | |
| N46 | 8 | 248 | 2 | 55.3%, 64.3% | EBITDA / PAT chart YoY data labels (duplicates of N43) | |
| N47 | 8 | 250 | 3 | 3,552, 898, 566 | Total Income / EBITDA / PAT chart bars, Q1FY27 column (duplicates of N42) | |
| N48 | 8 | 251 | 3 | 3,394, 813, 511 | Total Income / EBITDA / PAT chart bars, Q4FY26 column | |
| N49 | 8 | 252 | 1 | 2,792 | Total Income chart bar, Q1FY26 column | |
| N50 | 8 | 253 | 2 | 578, 345 | EBITDA / PAT chart bars, Q1FY26 column | |
| N51 | 8 | 254 | 3 | 4.6%, 10.4%, 10.7% | Total Income growth label 4.6% (QoQ?) + two more margin/growth data labels on chart | |
| N52 | 8 | 259 | 18 | 1,26,4,26,1,27 ×3 | X-axis period labels Q1FY26 / Q4FY26 / Q1FY27 repeated across the three charts | |
| N53 | 8 | 266 | 1 | 7 | slide footer page number "7" | |
| N54 | 9 | 268 | 2 | 1, 27 | "Q1FY27 Results (Consolidated)" heading | |
| N55 | 9 | 270 | 6 | 1,27,4,26,1,26 | Table column headers Q1FY27 / Q4FY26 / Q1FY26 | |
| N56 | 9 | 272 | 5 | 3,474, 3,389, 2,737, 2.5%, 27.0% | Revenue from Operations: 3,474 / 3,389 / 2,737; QoQ 2.5%; YoY 27.0% | |
| N57 | 9 | 273 | 3 | 78, 5, 55 | Other Income: 78 / 5 / 55 | |
| N58 | 9 | 274 | 3 | 1,161, 1,195, 941 | Cost of materials consumed (incl. inventory change): 1,161 / 1,195 / 941 | |
| N59 | 9 | 275 | 3 | 66.6%, 64.7%, 65.6% | Gross Profit Margin: 66.6% / 64.7% / 65.6% | |
| N60 | 9 | 277 | 5 | 898, 813, 578, 10.5%, 55.4% | EBITDA: 898 / 813 / 578; QoQ 10.5%; YoY 55.4% | |
| N61 | 9 | 278 | 3 | 25.3%, 24.0%, 20.7% | EBITDA Margin: 25.3% / 24.0% / 20.7% | |
| N62 | 9 | 280 | 5 | 820, 808, 523, 1.5%, 56.8% | Operating EBITDA (ex-other income): 820 / 808 / 523; QoQ 1.5%; YoY 56.8% | |
| N63 | 9 | 281 | 3 | 23.6%, 23.9%, 19.1% | Operating EBITDA Margin: 23.6% / 23.9% / 19.1% | |
| N64 | 9 | 283 | 3 | 118, 118, 111 | Depreciation & Amortization: 118 / 118 / 111 | |
| N65 | 9 | 285 | 5 | 780, 695, 467, 12.2%, 67.0% | EBIT: 780 / 695 / 467; QoQ 12.2%; YoY 67.0% | |
| N66 | 9 | 286 | 3 | 22.0%, 20.5%, 16.7% | EBIT Margin: 22.0% / 20.5% / 16.7% | |
| N67 | 9 | 288 | 3 | 34, 33, 20 | Finance Cost: 34 / 33 / 20 | |
| N68 | 9 | 290 | 5 | 746, 663, 447, 12.5%, 66.9% | PBT: 746 / 663 / 447; QoQ 12.5%; YoY 66.9% | |
| N69 | 9 | 291 | 3 | 0, 0, 0 | Exceptional Item – Impact of Labour Code: 0 / 0 / 0, all three periods | ZERO_STANDING (all 3 periods nil; standing line item — a labour-code exceptional item did occur in FY26 per Table 3/N173, so this line is a template signal, not a non-existent category) |
| N70 | 9 | 293 | 3 | 180, 151, 102 | Tax Expense: 180 / 151 / 102 | |
| N71 | 9 | 295 | 5 | 566, 511, 345, 10.8%, 64.1% | PAT: 566 / 511 / 345; QoQ 10.8%; YoY 64.1% | |
| N72 | 9 | 296 | 3 | 15.9%, 15.1%, 12.3% | PAT Margin: 15.9% / 15.1% / 12.3% | |
| N73 | 9 | 298 | 3 | 12.54, 11.33, 7.6 | Basic EPS (INR): 12.54 / 11.33 / 7.6 | |
| N74 | 9 | 300 | 1 | 8 | slide footer page number "8" | |
| N75 | 10 | 303 | 1 | 3 | "3PL and PMP Products Globally" heading | |
| N76 | 10 | 308 | 5 | 1.5%, 0.8%, 2.4%, 2.6%, 1.8% | Product Vertical / Geographical Presence donut small-slice labels (Others/PTO/Japan/etc.) | |
| N77 | 10 | 309 | 1 | 1.1% | Product Vertical donut slice label | |
| N78 | 10 | 310 | 2 | 1.1%, 1.1% | Product Vertical donut slice labels (two periods) | |
| N79 | 10 | 311 | 1 | 0.7% | Product Vertical donut slice label | |
| N80 | 10 | 312 | 3 | 14.9%, 14.3%, 12.3% | Geographical Presence donut slice labels | |
| N81 | 10 | 313 | 1 | 4.2% | Geographical Presence donut slice label | |
| N82 | 10 | 314 | 2 | 4.5%, 5.2% | Geographical Presence donut slice labels | |
| N83 | 10 | 315 | 8 | 25, 48.8%, 46.6%, 42.5%, 25, 26, 1, 27 | Product Vertical (3PL%) FY25 48.8% / FY26 46.6% / Q1FY27 42.5%, period labels | |
| N84 | 10 | 316 | 6 | 48.6%, 26, 1, 27, 54.6%, 53.2% | Product Vertical (PMP%) FY25 48.6%; Geographical Presence (Americas%) FY26 54.6% / Q1FY27 53.2% | |
| N85 | 10 | 317 | 3 | 51.5%, 21.1%, 60.6% | Product Vertical PMP% and Geographical Presence Americas% donut labels | |
| N86 | 10 | 318 | 3 | 55.7%, 23.6%, 24.7% | Product Vertical PMP% Q1FY27 55.7%; Geographical Presence Europe% labels | |
| N87 | 10 | 323 | 1 | 3 | legend "3PL PMP PTO Fabrication Others / Americas Europe Japan India Rest of the World" | |
| N88 | 10 | 331 | 3 | 19.3%, 15.0%, 12.3% | Market Presence (AFM%) FY25 19.3% / FY26 15.0% / Q1FY27 12.3% | |
| N89 | 10 | 333 | 2 | 36.9%, 38.7% | Segmental Presence (Agriculture%) FY25 36.9%, FY26 38.7% | |
| N90 | 10 | 334 | 6 | 25, 25, 26, 46.2%, 1, 27 | Segmental Presence Q1FY27 Agriculture 46.2%, period labels FY25/FY26/Q1FY27 | |
| N91 | 10 | 335 | 3 | 26, 1, 27 | Market Presence period labels FY26 / Q1FY27 | |
| N92 | 10 | 336 | 1 | 53.8% | Segmental Presence (CFM%) Q1FY27 53.8% | |
| N93 | 10 | 337 | 2 | 63.1%, 61.3% | Segmental Presence CFM% FY25 63.1% / FY26 61.3% | |
| N94 | 10 | 339 | 1 | 80.7% | Market Presence (OEM%) FY25 80.7% | |
| N95 | 10 | 340 | 2 | 85.0%, 87.7% | Market Presence OEM% FY26 85.0% / Q1FY27 87.7% | |
| N96 | 10 | 348 | 1 | 9 | slide footer page number "9" | |
| N97 | 11 | 354 | 3 | 1, 2, 7 | "Q1FY27 Performance" heading (TOC divider repeat) | |
| N98 | 11 | 367 | 1 | 10 | slide footer page number "10" | |
| N99 | 12 | 381 | 1 | 11 | slide footer page number "11" | |
| N100 | 13 | 394 | 1 | 3 | "Synergies with existing activities in the 3PL" | |
| N101 | 13 | 410 | 1 | 10 | "Estimated Market Size of ~$10 billion" | |
| N102 | 13 | 411 | 1 | 20% | "Long term margin guidance remains at 20%" (forward guidance statement) | |
| N103 | 13 | 418 | 1 | 12 | slide footer page number "12" | |
| N104 | 14 | 422 | 3 | 3, 47%, 51% | "3 Point Linkage – Revenue Contribution*: 47%" / "Precision Machined Parts – Revenue Contribution*: 51%" | |
| N105 | 14 | 433 | 1 | 70 | "Market leaders in small tractor (<70 HP) linkage system globally" | |
| N106 | 14 | 441 | 1 | 1 | "$1 billion+ Market Size" (PMP) | |
| N107 | 14 | 442 | 1 | 25 | "25+ Countries covered in sales" | |
| N108 | 14 | 450 | 1 | 26 | footnote text: "*Revenue contribution is based on FY26 finished goods sales" | (footnote — see Table 3) |
| N109 | 14 | 452 | 1 | 13 | slide footer page number "13" | |
| N110 | 15 | 473 | 5 | 7, 4, 67,320, 400, 1 | "7 Manufacturing Facilities / 4 Warehouses / 67,320 Metric tonne per annum / 400 kilonewton Test rig / 1 Distribution Facility" | |
| N111 | 15 | 475 | 4 | 6, 3, 2, 1 | Facility location breakdown: "6 in India; 3 in Ludhiana; 2 in US; 1 in Europe" | |
| N112 | 15 | 476 | 2 | 2, 1 | "2 in Noida / 1 in Mexico" | |
| N113 | 15 | 477 | 2 | 1, 1 | "1 in Visakhapatnam; 1 in US" and "capacity*" label | DANGLING_FOOTNOTE (asterisk on "Aggregate installed capacity*" has no matching footnote text anywhere on slide 15 — data gap for A3/A4 to chase against the source PDF) |
| N114 | 15 | 487 | 1 | 14 | slide footer page number "14" | |
| N115 | 16 | 492 | 1 | 10 | "Four of the Top Five Customers have been Associated with Uniparts for over 10 years" | |
| N116 | 16 | 500 | 2 | 5, 10 | "Top 5 customers / Top 10 customers" legend | |
| N117 | 16 | 505 | 1 | 84% | Top-10-customer concentration bar, Q1FY27: 84% | |
| N118 | 16 | 506 | 2 | 76%, 78% | Top-5-customer concentration bars: FY25 76%, FY26 78% | |
| N119 | 16 | 507 | 1 | 71% | Top-10-customer concentration bar, FY25: 71% | |
| N120 | 16 | 508 | 1 | 64% | Top-10-customer concentration bar, FY26: 64% | |
| N121 | 16 | 509 | 1 | 61% | Top-5-customer concentration bar, Q1FY27: 61% | |
| N122 | 16 | 511 | 1 | 0 | stray "0" glued to "Flexible batch sizes0" — likely a footnote marker or OCR artifact, no corresponding note found | DANGLING_FOOTNOTE (candidate) |
| N123 | 16 | 514 | 3 | 28%, 27%, 31% | Top-customer concentration bars: FY25 28%, FY26 27%, Q1FY27 31% | |
| N124 | 16 | 517 | 2 | 10, 10 | "Servicing all 10 leading Global OHV OEMs... half of the leading 10 players in the CFM Segment*" | |
| N125 | 16 | 519 | 4 | 25, 26, 1, 27 | Chart x-axis period labels FY25 / FY26 / Q1FY27 | |
| N126 | 16 | 522 | 1 | 3 | "3PL and PMP for OHVs globally" | |
| N127 | 16 | 526 | 1 | 70 | "Preferred component supplier for manufacturer of <70 HP Tractors" | |
| N128 | 16 | 536 | 1 | 15 | slide footer page number "15" | |
| N129 | 17 | 542 | 1 | 35.9 | RoCE chart, FY23: 35.9% | |
| N130 | 17 | 543 | 2 | 46.32, 0.11x | Reported EPS chart FY23: 46.32; Debt/Equity chart FY23: 0.11x | |
| N131 | 17 | 544 | 1 | 0.09x | Debt/Equity chart FY24: 0.09x | |
| N132 | 17 | 545 | 2 | 24.9, 35.07 | RoCE chart FY25 or FY26: 24.9%; Reported EPS chart FY26: 35.07 | |
| N133 | 17 | 546 | 2 | 28.13, 0.07x | Reported EPS chart FY24: 28.13; Debt/Equity chart FY25: 0.07x | |
| N134 | 17 | 547 | 1 | 19.5 | RoCE chart FY24: 19.5% | |
| N135 | 17 | 548 | 2 | 13.7, 19.50 | RoCE chart FY... 13.7%; Reported EPS chart FY25: 19.50 | |
| N136 | 17 | 550 | 1 | 0.02x | Debt/Equity chart FY26: 0.02x | |
| N137 | 17 | 553 | 8 | 23,24,25,26 ×2 | RoCE and Reported EPS chart x-axis labels FY23-FY26 | |
| N138 | 17 | 554 | 4 | 23, 24, 25, 26 | Reported EPS chart x-axis labels FY23-FY26 (second instance) | |
| N139 | 17 | 560 | 1 | 2.3x | Fixed Assets Turnover chart FY26: 2.3x | |
| N140 | 17 | 561 | 1 | 2,527 | CFO chart FY23: INR 2,527 Mn | |
| N141 | 17 | 562 | 2 | 154, 1.9x | Working Capital Days chart FY24: 154; Fixed Assets Turnover chart FY25: 1.9x | |
| N142 | 17 | 563 | 3 | 152, 1.7x, 1,997 | Working Capital Days chart FY23: 152; Fixed Assets Turnover chart FY24: 1.7x; CFO chart FY24: INR 1,997 Mn | |
| N143 | 17 | 564 | 3 | 1.5x, 1,820, 1,736 | Fixed Assets Turnover chart FY23: 1.5x; CFO chart FY25: INR 1,820 Mn; CFO chart FY26: INR 1,736 Mn | |
| N144 | 17 | 565 | 1 | 144 | Working Capital Days chart FY23 (alt reading): 144 | |
| N145 | 17 | 567 | 1 | 136 | Working Capital Days chart FY25/FY26: 136 | |
| N146 | 17 | 572 | 12 | 23,24,25,26 ×3 | X-axis period labels FY23-FY26 across Working Capital Days, Fixed Assets Turnover, and CFO charts | |
| N147 | 17 | 575 | 1 | 365 | Footnote formula: WC Days = (Inventory+Receivables-Payables)/Revenue*365 | (footnote — see Table 3) |
| N148 | 17 | 577 | 1 | 16 | slide footer page number "16" | |
| N149 | 18 | 593 | 1 | 250 | "250+ Engineers / Technical Diploma holders" | |
| N150 | 18 | 598 | 1 | 50 | "50+ strong Business Development and Sales / Customer Service organization" | |
| N151 | 18 | 604 | 1 | 45% | "~45% staff members working with Uniparts Group for 10+ years" | |
| N152 | 18 | 605 | 1 | 10 | "...10+ years" (tenure threshold, second half of same stat) | |
| N153 | 18 | 610 | 1 | 17 | slide footer page number "17" | |
| N154 | 19 | 613 | 3 | 24, 25, 26 | Historical P&L column headers FY24 / FY25 / FY26 | |
| N155 | 19 | 614 | 3 | 11,395, 9,637, 11,704 | Revenue from operations: 11,395 / 9,637 / 11,704 | |
| N156 | 19 | 615 | 3 | 93, 212, 176 | Other income: 93 / 212 / 176 | |
| N157 | 19 | 616 | 3 | 11,489, 9,849, 11,880 | Total income: 11,489 / 9,849 / 11,880 | |
| N158 | 19 | 617 | 3 | 3,966, 3,118, 4,246 | Cost of materials consumed: 3,966 / 3,118 / 4,246 | |
| N159 | 19 | 618 | 3 | 264, 431, (350) | Changes in inventories: 264 / 431 / (350) | |
| N160 | 19 | 619 | 3 | 7,260, 6,300, 7984 | Gross Profit: 7,260 / 6,300 / 7984 (note: FY26 lacks thousands comma, verify vs 7,984) | |
| N161 | 19 | 620 | 3 | 63%, 64%, 67% | Gross Profit Margin: 63% / 64% / 67% | |
| N162 | 19 | 621 | 3 | 2,457, 2,296, 2,559 | Employee benefits expense: 2,457 / 2,296 / 2,559 | |
| N163 | 19 | 622 | 3 | 2,694, 2,336, 2,777 | Other expenses: 2,694 / 2,336 / 2,777 | |
| N164 | 19 | 623 | 3 | 5,151, 4,632, 5,336 | Total expenses: 5,151 / 4,632 / 5,336 | |
| N165 | 19 | 624 | 3 | 2,107, 1,668, 2,648 | EBITDA: 2,107 / 1,668 / 2,648 | |
| N166 | 19 | 625 | 3 | 18%, 17%, 22% | EBITDA Margin: 18% / 17% / 22% | |
| N167 | 19 | 626 | 3 | 417, 442, 453 | Depreciation and amortization expenses: 417 / 442 / 453 | |
| N168 | 19 | 627 | 3 | 1,690, 1,226, 2,195 | EBIT: 1,690 / 1,226 / 2,195 | |
| N169 | 19 | 628 | 3 | 15%, 12%, 18% | EBIT Margin: 15% / 12% / 18% | |
| N170 | 19 | 629 | 3 | 57, 83, 104 | Finance costs: 57 / 83 / 104 | |
| N171 | 19 | 630 | 3 | 1,633, 1,143, 2,091 | PBT: 1,633 / 1,143 / 2,091 | |
| N172 | 19 | 631 | 3 | 14%, 12%, 18% | PBT Margin: 14% / 12% / 18% | |
| N173 | 19 | 632 | 3 | 0, 0, 34 | Exceptional Item – Impact of Labour Code: 0 / 0 / 34 (FY26 non-zero — contrast with N69's all-zero quarterly line) | |
| N174 | 19 | 633 | 3 | 387, 263, 474 | Total tax expenses: 387 / 263 / 474 | |
| N175 | 19 | 634 | 3 | 1,247, 880, 1,583 | PAT: 1,247 / 880 / 1,583 | |
| N176 | 19 | 635 | 3 | 11%, 9%, 13% | PAT Margin: 11% / 9% / 13% | |
| N177 | 19 | 636 | 3 | (5), (52), (67) | Other comprehensive income/(loss), net of tax: (5) / (52) / (67) | |
| N178 | 19 | 637 | 3 | 1,241, 828, 1,516 | Total Comprehensive Income: 1,241 / 828 / 1,516 | |
| N179 | 19 | 639 | 3 | 28.1, 19.5, 35.07 | Basic EPS (INR): 28.1 / 19.5 / 35.07 | |
| N180 | 19 | 640 | 3 | 27.6, 19.5, 35.04 | Diluted EPS (INR): 27.6 / 19.5 / 35.04 | |
| N181 | 19 | 644 | 1 | 18 | slide footer page number "18" | |
| N182 | 20 | 647 | 6 | 24,25,26,24,25,26 | Balance sheet column headers FY24/FY25/FY26 (both Assets side and Equity & Liabilities side) | |
| N183 | 20 | 650 | 6 | 2,001, 2,010, 1,994, 451, 451, 451 | PP&E: 2,001/2,010/1,994; Equity share capital: 451/451/451 | ZERO_STANDING candidate (equity share capital flat/unchanged 3 yrs — not a nil line, informational only) |
| N184 | 20 | 651 | 3 | 8,227, 8,421, 8,253 | Other equity: 8,227 / 8,421 / 8,253 | |
| N185 | 20 | 652 | 3 | 616, 561, 815 | Right of use assets: 616 / 561 / 815 | |
| N186 | 20 | 653 | 3 | 8,678, 8,872, 8,704 | Total equity: 8,678 / 8,872 / 8,704 | |
| N187 | 20 | 654 | 3 | 128, 96, 33 | Capital work-in-progress: 128 / 96 / 33 | |
| N188 | 20 | 656 | 3 | 664, 669, 694 | Goodwill: 664 / 669 / 694 | |
| N189 | 20 | 658 | 6 | 18, 11, 28, 22, 12, 85 | Other intangible assets: 18/11/28; Other non-current liabilities: 22/12/85 (misaligned — see below) | |
| N190 | 20 | 660 | 5 | (-), 24, 56, 318, 252, 500 | Intangible assets under development: (-)/24/56; Lease liabilities (non-current): 318/252/500 | ZERO_STANDING (Intangible assets under development shows dash "-" in FY24, i.e. nil/not-yet-existing in the earliest period — standing line item appears once activity begins) |
| N191 | 20 | 661 | 6 | 64, 89, 92, 159, 162, 200 | Other financial assets (non-current): 64/89/92; Provisions (non-current): 159/162/200 | |
| N192 | 20 | 662 | 6 | 75, 92, 85, 226, 225, 231 | Current tax assets (Net): 75/92/85; Deferred tax liabilities (Net): 226/225/231 | |
| N193 | 20 | 663 | 3 | 10, 10, 11 | Other non-current liabilities: 10 / 10 / 11 | |
| N194 | 20 | 664 | 3 | 21, 4, 71 | Other non-current assets: 21 / 4 / 71 | |
| N195 | 20 | 665 | 3 | 735, 661, 1,027 | Total non-current liabilities: 735 / 661 / 1,027 | |
| N196 | 20 | 666 | 3 | 3,587, 3,556, 3,868 | Total non-current assets: 3,587 / 3,556 / 3,868 | |
| N197 | 20 | 669 | 3 | 597, 826, 837 | Borrowings (current): 597 / 826 / 837 | |
| N198 | 20 | 670 | 6 | 4,244, 3,858, 4,301, 89, 109, 125 | Inventories: 4,244/3,858/4,301; Lease liabilities (current): 89/109/125 | |
| N199 | 20 | 672 | 3 | 1,563, 2,431, 2,030 | Investments: 1,563 / 2,431 / 2,030 | |
| N200 | 20 | 673 | 6 | 1,335, 1,126, 1,412, 134, 169, 262 | Trade receivables: 1,335/1,126/1,412; Trade payables to Micro & Small Enterprises: 134/169/262 | |
| N201 | 20 | 674 | 6 | 189, 329, 470, 708, 742, 1,092 | Cash and cash equivalents: 189/329/470; Trade payables to other than MSE: 708/742/1,092 | |
| N202 | 20 | 675 | 3 | 268, 267, 411 | Other liabilities (current): 268 / 267 / 411 | |
| N203 | 20 | 676 | 3 | 2, 2, 3 | Other balances with banks: 2 / 2 / 3 | |
| N204 | 20 | 677 | 3 | 67, 50, 65 | Provisions (current): 67 / 50 / 65 | |
| N205 | 20 | 678 | 3 | 48, 6, 4 | Other financial assets (current): 48 / 6 / 4 | |
| N206 | 20 | 679 | 3 | 10, 0, 26 | Current tax payable: 10 / 0 / 26 | |
| N207 | 20 | 680 | 3 | 320, 388, 461 | Other current assets: 320 / 388 / 461 | |
| N208 | 20 | 681 | 3 | 1,873, 2,163, 2,818 | Total current liabilities: 1,873 / 2,163 / 2,818 | |
| N209 | 20 | 682 | 6 | 7,700, 8,140, 8681, 2,609, 2,824, 3,845 | Total current assets: 7,700/8,140/8681 (FY26 lacks comma, verify vs 8,681); Total liabilities: 2,609/2,824/3,845 | |
| N210 | 20 | 684 | 6 | 11,287, 11,696, 12,549, 11,287, 11,696, 12,549 | Total Assets: 11,287/11,696/12,549 = Total Equity and Liabilities: 11,287/11,696/12,549 (balance check ties) | |
| N211 | 20 | 688 | 1 | 19 | slide footer page number "19" | |
| N212 | 21 | 694 | 3 | 1, 2, 7 | "Q1FY27 Performance" heading (TOC divider repeat, 3rd instance) | |
| N213 | 21 | 707 | 1 | 20 | slide footer page number "20" | |
| N214 | 22 | 710 | 1 | 2018 | Milestone year 2018 (Augusta USA warehousing addition) | |
| N215 | 22 | 713 | 5 | 1994, 2001, 2003, 2006, 2010 | Milestone years 1994 (incorporation), 2001-2003, 2006, 2010 | |
| N216 | 22 | 714 | 2 | 2022, 2024 | Milestone years 2022 (listed BSE/NSE), 2024 (SER certified by Caterpillar) | |
| N217 | 22 | 726 | 1 | 2020 | Milestone year 2020 (referenced in "Most Versatile Supplier 2020" context) | |
| N218 | 22 | 729 | 1 | 3 | "3 units SER certified by Caterpillar" | |
| N219 | 22 | 730 | 3 | 3, 2012, 2023 | "3PL OEM" product vertical; milestone years 2012, 2023 | |
| N220 | 22 | 733 | 1 | 11 | "11th National Kaizen Competition" | |
| N221 | 22 | 739 | 1 | 2025 | Milestone year 2025 (3 units SER certified by Caterpillar) | |
| N222 | 22 | 741 | 1 | 2020 | Milestone year 2020 (OEMs in construction sector, US) | |
| N223 | 22 | 742 | 1 | 2008 | Milestone year 2008 | |
| N224 | 22 | 743 | 1 | 2000 | Milestone year 2000 | |
| N225 | 22 | 744 | 2 | 2004, 2005 | Milestone years 2004-2005 | |
| N226 | 22 | 746 | 1 | 21 | slide footer page number "21" | |
| N227 | 23 | 754 | 1 | 100% | UIL → GFPL/GCPL/UIG/UUL ownership: 100% | |
| N228 | 23 | 763 | 1 | 100% | UUL → UOI ownership: 100% | |
| N229 | 23 | 769 | 1 | 22 | slide footer page number "22" | |
| N230 | 24 | 789 | 3 | 4, 4, 2 | "4 decades" (Gurdeep Soni), "Over 4 decades" (Paramjit Singh Soni), "2 decades" (Sandeep Taneja, spoken as extensive experience) | |
| N231 | 24 | 790 | 1 | 25 | "25+ years of global experience" (Sandeep Taneja) | |
| N232 | 24 | 791 | 1 | 3 | "Over 3 decades experience" (Herbert Coenen) | |
| N233 | 24 | 795 | 2 | 100, 3 | "$100M to $3B" P&L range (Sandeep Taneja bio) | |
| N234 | 24 | 803 | 1 | 23 | slide footer page number "23" | |

Cross-check flag: N160/N209 note possible thousands-comma formatting drops in the source PDF ("7984" vs elsewhere-styled "7,984"; "8681" vs "8,681") — not a value discrepancy, purely a formatting inconsistency in the deck's own table, worth a downstream note (FORMATTING_INCONSISTENCY) if A3/A4 checks arithmetic.

---

## TABLE 3 — FOOTNOTES AND FINE-PRINT DISCLAIMERS QUALIFYING HEADLINE NUMBERS (8 units)

| # | Slide | Line | Footnote text | Qualifies |
|---|---|---|---|---|
| F1 | 3 | 100-127 | "Safe Harbor" — full-page forward-looking-statement disclaimer (no offer/prospectus, rounding disclaimer: "Certain figures... have been rounded off to the nearest number and may not depict the exact number", no update obligation, not independently verified) | Every forward-looking or growth-oriented statement in the deck (pages 5-7 management commentary, page 13 margin guidance, etc.) |
| F2 | 8 | 261 | "Note: Total Revenue, EBITDA, PBT and PAT include other income" | Key Takeaways KPI headline figures (N42) — clarifies these are NOT ex-other-income like the "Operating EBITDA" line on slide 9 |
| F3 | 10 | 305 | "INR Mn, Segment revenue as % of finished goods sales" (unit/basis disclaimer) | All four Revenue Distribution donut charts (Product Vertical, Geographical, Market Presence, Segmental Presence) |
| F4 | 12 | 379 | "Note: We do small and medium scale Fabrication, PTO (Power Take-off) and Hydraulic components" | Scale/scope qualifier on the 5 product categories shown on slide 12 |
| F5 | 14 | 450 | "*Revenue contribution is based on FY26 finished goods sales" | 3PL 47% / PMP 51% revenue-contribution figures (N104) — clarifies these are FY26 full-year, not Q1FY27 |
| F6 | 16 | 534 | "*CFM global players outside China" | "half of the leading 10 players in the CFM Segment*" claim (N124) |
| F7 | 17 | 575 (part 1) | "*Working Capital Days = (Inventory + Receivables – Payables)/Revenue from Ops *365" | Working Capital Days chart (N141, N142, N144, N145) |
| F8 | 17 | 575 (part 2) | "**Fixed Assets Turnover = Revenue from operations/Gross block (Including right to use assets)" | Fixed Assets Turnover chart (N139, N141, N142, N143) |

Data-quality note (not a defined footnote, flagged for completeness): the asterisk on slide 15's "Aggregate installed capacity*" (N113) has NO matching footnote text anywhere on that page — see DANGLING_FOOTNOTE flag on Table 2/N113. Also the stray "0" at N122 ("Flexible batch sizes0") reads like an orphaned footnote marker with no corresponding note text on slide 16.

---

## TABLE 4 — LEADERSHIP TEAM AND BOARD PROFILES (slide 24, Annexures; 9 individuals)

| # | Name | Role (as stated) | Location | Background (as extracted) | Flags |
|---|---|---|---|---|---|
| L1 | Mr. Gurdeep Soni | Promoter, Chairman & Managing Director | India | Masters' degree in Management Studies from BITS Pilani; 4 decades of experience in the industry; in charge of the aftermarket business | |
| L2 | Mr. Paramjit Singh Soni | Promoter, Executive Director and Vice Chairman (also styled "Promoter, Vice Chairman and Executive Director" on slide 5) | USA | Bachelor's degree in Commerce from University of Delhi; over 4 decades of experience; in charge of OEM business, business growth and diversification plans | |
| L3 | Mr. Herbert Coenen | Non-Executive Director | Germany | Diploma in Mechanical Engineering from the University of Applied Science, Cologne; over 3 decades experience in global OHV market; in charge of business development, expansion and technology | |
| L4 | Ms. Tanushree Bagrodia | Wholetime Director & Group CEO | India | Bachelors' degree in Computer Engg and MBA from INSEAD; over 2 decades extensive experience across diverse geographies and sectors, spanning financial services, automotive, and start-ups; in charge of Company's group-wide operations and customer service | |
| L5 | Mr. Sandeep Taneja | Group Chief Financial Officer | India | Chartered Accountant (India) and CPA (USA) with an MBA from the U.S.; seasoned finance professional with 25+ years of global experience across India and the U.S., including leadership of large P&Ls ranging from $100M to $3B; deep expertise across accounting, audit, tax, treasury, and business partnering | |
| L6 | Mr. Ajaya Chand | Independent Director (per label at lines 775-776, positionally associated with this name at line 784) | not stated in extract | not stated in extract | BIO_TEXT_MISALIGNED — the pdftotext multi-column layout interleaves this name into the Herbert Coenen/Tanushree Bagrodia bio columns; role label and biography could not be reliably attributed from the linear text extract; verify against source PDF/visual layout |
| L7 | Ms. Celine George | not stated in extract | not stated in extract | not stated in extract | BIO_TEXT_MISALIGNED — same layout issue; name appears embedded mid-sentence inside Herbert Coenen's bio paragraph (line 789) |
| L8 | Mr. Parmeet Singh Kalra | not stated in extract | not stated in extract | not stated in extract | BIO_TEXT_MISALIGNED — name appears embedded mid-sentence inside Herbert Coenen's bio paragraph (line 793-794) |
| L9 | Mr. Sanjeev Kumar Chanana | not stated in extract | not stated in extract | not stated in extract | BIO_TEXT_MISALIGNED — name appears embedded mid-sentence inside Herbert Coenen's bio paragraph (line 798) |

This slide functions as the presentation-doctype equivalent of a director-profile annexure (Results Filing rule 4 analog). L6-L9 represent a genuine enumeration gap risk: 4 of 9 board/leadership photos on this slide have no reliably-attributed role or biography in the text layer. A3/A4 should treat these 4 names as open items requiring visual confirmation, not as confirmed board composition.

---

## TABLE 5 — DIGITAL SIGNATURE BLOCK (Reg 30 cover letter, page 1; Results Filing rule-7 analog applied to this presentation's cover letter)

| Slide | Lines | Signatory | Designation | Timestamp | Flags |
|---|---|---|---|---|---|
| 1 | 46-65 | Jatin Mahajan | Head Legal, Company Secretary and Compliance Officer | 2026.08.04 17:48:09 +05'30' | Signed same calendar date as the letter (August 04, 2026); no board-meeting time is stated anywhere in this presentation-doctype document (that data point, if it exists, belongs to the separate Board Outcome / Results Filing document for this quarter — not present in this extract) — so no signature-vs-meeting-time timing flag can be evaluated from this document alone |

---

## TABLE 6 — ENTITIES (Group Structure org chart, slide 23; 6 entities; no prior-quarter list supplied so ENTITY_CHANGE cannot be evaluated)

| # | Entity | Short name | Relationship | Ownership | Line |
|---|---|---|---|---|---|
| E1 | Uniparts India Ltd. | UIL | Parent / listed entity | — | 753 |
| E2 | Gripwel Fasteners Pvt. Ltd. | GFPL | Subsidiary of UIL | 100% (per single "100%" label spanning the four direct subsidiaries) | 759 |
| E3 | Gripwel Conag Pvt. Ltd. | GCPL | Subsidiary of UIL | 100% | 759 |
| E4 | Uniparts India GmbH | UIG | Subsidiary of UIL | 100% | 760 |
| E5 | Uniparts USA Ltd. | UUL | Subsidiary of UIL | 100% | 760 |
| E6 | Uniparts Olsen Inc | UOI | Step-down subsidiary, held by UUL | 100% (explicit second "100%" label, line 763) | 766-767 |

ENTITY_CHANGE: not evaluable — no prior-quarter entity list was supplied (input states NONE). Baseline for next quarter's diff: 6 entities (UIL + 5 subsidiaries/step-down subsidiaries) as listed above.

---

## SUMMARY OF FLAGS RAISED

1. ZERO_STANDING — slide 9 (N69): "Exceptional Item – Impact of Labour Code" reads 0/0/0 across Q1FY27, Q4FY26 and Q1FY26 on the quarterly results table. Standing line item, not dropped, because the FY26 annual P&L on slide 19 (N173) shows a non-zero 34 for this same line — confirming it is a live, templated category that simply had no quarterly impact in the three periods shown here.
2. ZERO_STANDING — slide 20 (N190): "Intangible assets under development" shows a dash "-" in FY24 (nil / not yet existing) before becoming 24 (FY25) and 56 (FY26). Flagged as the standing-line-item pattern per the SOUTHWEST convention (line exists because the transaction category is anticipated/emerging).
3. DANGLING_FOOTNOTE — slide 15 (N113): asterisk on "Aggregate installed capacity*" has no matching footnote text anywhere on that page.
4. DANGLING_FOOTNOTE (candidate) — slide 16 (N122): stray "0" glued to "Flexible batch sizes0" reads as an orphaned footnote marker; no corresponding note text found.
5. BIO_TEXT_MISALIGNED — slide 24 (Table 4, L6-L9): 4 of 9 leadership/board names (Ajaya Chand, Celine George, Parmeet Singh Kalra, Sanjeev Kumar Chanana) have no reliably-attributed role/biography in the linear text extract due to multi-column PDF layout; Ajaya Chand carries an "Independent Director" label positioned nearby but not conclusively linked in the text stream.
6. FORMATTING_INCONSISTENCY (candidate) — slide 19/20: two figures (Gross Profit FY26 "7984" and Total current assets FY26 "8681") lack the thousands-comma formatting used everywhere else in the same tables; worth a downstream arithmetic sanity check, not a value dispute.

DROPPED_SLIDE and ENTITY_CHANGE: both explicitly not evaluable this run — no prior-quarter ledger or entity list was supplied. This ledger is the baseline for both comparisons at the next quarterly run.
