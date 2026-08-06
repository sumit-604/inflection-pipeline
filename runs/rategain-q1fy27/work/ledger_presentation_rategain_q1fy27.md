# A2 ENUMERATOR LEDGER — RateGain Travel Technologies Limited (RATEGAIN)
Quarter: Q1 FY27 | Doctype: presentation
Source: extract_presentation_rategain_q1fy27.txt (pdftotext -layout + OCR merge, page_count_pdfinfo=30, ocr_pages=[2,7,13,15,20,25,28])
Prior-quarter ledger: not available in runs/ — DROPPED_SLIDE analysis marked N/A this run.

```
=== A2 COUNT TEST ===
category: slides                 grep_count: 30   sweep_count: 30   match: yes
category: slide_numbers          grep_count: 30   sweep_count: 30   match: yes
category: footnotes              grep_count: 6    sweep_count: 6    match: yes
category: line_items (P&L+BS)    grep_count: 58   sweep_count: 58   match: yes
category: zero_standing          grep_count: 5    sweep_count: 5    match: yes
category: pct_data_points        grep_count: 50   sweep_count: 50   match: yes
category: currency_data_points   grep_count: 8    sweep_count: 8    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep commands used (reproducible):
- slides: `grep -c -E "^\[page [0-9]+\]" extract` = 30; cross-checked against header `page_count_pdfinfo: 30` and `formfeed_count: 30`.
- footnotes: `grep -c -iE "^\s*Note\s*:" extract` = 6 (lines 270, 322, 679, 734, 769, 871).
- line_items: manual delimiting of table row ranges (P&L lines 737-767, BS lines 774-803), non-blank label lines excluding title/column-header rows = 20 (P&L) + 38 (BS) = 58.
- zero_standing: keyword grep for the 5 known dash rows (`Exceptional Expenses`, `Other intangible assets under development`, `i. Investments` [non-current], `Other non - current liabilities`, `iv. Bank balances other than (iii) above`) within lines 736-806 = 5.
- pct_data_points: `grep -noE "[0-9]+\.?[0-9]*[[:space:]]?%" extract`, excluding header line 10 (`page_coverage: 100%`) and the P&L table range (lines 738-771; BS table contributes none) = 50.
- currency_data_points: `grep -oE "INR[[:space:]]*[0-9][0-9,.]*[[:space:]]*Cr" extract`, excluding pages 23-24 tables (which use bare Cr columns, not "INR ... Cr" inline strings) = 8.

---

## TABLE A — SLIDE INVENTORY (30 slides / pages)

| # | Page marker | Title / heading | Content type | OCR status | Flags |
|---|---|---|---|---|---|
| 1 | [page 1] L34 | Reg. 30 cover letter to NSE/BSE re: Investor Presentation | text (regulatory letter) | native | SIGNATURE_BLOCK |
| 2 | [page 2] L77 | "Investor Presentation Q1 FY2027" (title slide) | text (title only) | OCR-confirmed, title+logo+page# only | OCR_THIN |
| 3 | [page 3] L84 | "Safe Harbor" | text (legal boilerplate, forward-looking statement disclaimer) | native | FORWARD_LOOKING |
| 4 | [page 4] L120 | "Our Vision" | text | native | — |
| 5 | [page 5] L132 | "Who we serve" / "What we do" | text (stat callouts) | native | — |
| 6 | [page 6] L161 | "Integrated RevMax Platform to Engage with Guests across the Entire Journey" | text/diagram (customer journey stages) | native | — |
| 7 | [page 7] L205 | "Key Business Updates Q1 FY2027" (section divider) | text (title only) | OCR-confirmed, title+section label+page#+logo only | OCR_THIN |
| 8 | [page 8] L223 | "Management Commentary" (Bhanu Chopra, Chairman & MD; Ankit Aggarwal, Interim + Deputy CFO) | text (quotes) | native | FORWARD_LOOKING |
| 9 | [page 9] L254 | "RateGain posts Robust Growth with Strong Operating Margins" | chart (3 headline metric callouts + footnote) | native | ADJ_METRIC_FOOTNOTE |
| 10 | [page 10] L272 | "Diversified Revenue Streams" | chart x4 (GRR/NRR, client count/LTV:CAC, 4 mix pie charts) + text | native | CHART_LABEL_AMBIGUOUS |
| 11 | [page 11] L327 | "Steady Growth Metrics Combined with Operational Efficiency" | text (8 KPI callout tiles) | native | — |
| 12 | [page 12] L358 | "Steady Revenue Streams Driven by Constant Product Innovation" | chart (segment growth %) + text (partnership bullets) | native | — |
| 13 | [page 13] L402 | "Award-winning Team Driving Performance" | photo/badge graphic + text | native text >100 chars; supplemental OCR run | OCR_SUPPLEMENT (badge text "BEST IN SAAS" only in OCR layer, not native text) |
| 14 | [page 14] L437 | "Reimagining People & Culture: Scaling One RateGain Through Integration, AI & Leadership Depth" | text (narrative + embedded stats) | native | — |
| 15 | [page 15] L477 | "Innovations at RateGain" (section divider) | text (title only) | OCR-confirmed, title+section label+page#+logo only | OCR_THIN |
| 16 | [page 16] L493 | "Today, we are Reimagining Hospitality with AI" | text (6 feature tiles, no numbers) | native | — |
| 17 | [page 17] L519 | "Introducing Agentic ARI: A next-generation ARI engine for faster, smarter hotel distribution" | text (product feature list) | native | — |
| 18 | [page 18] L549 | "Introducing RateIQ: Identify & Recover Hidden Revenue Across Distribution" | text (product feature list, no hard numbers) | native | — |
| 19 | [page 19] L577 | "Introducing RG Pay: A unified, intelligent payment infrastructure for seamless payments" | text (product feature list + 3 stat callouts) | native | — |
| 20 | [page 20] L603 | "Detailed Financials" (section divider) | text (title only) | OCR-confirmed, title+section label+page#+logo only | OCR_THIN |
| 21 | [page 21] L619 | "Sustained Financials and Profitability Metrics" | chart x5 (Op. Revenue, Gross Margin%, EBITDA, EBITDA Margin%, Free Cash Flow, all FY2022-Q1FY27) + text | native | CHART_LABEL_AMBIGUOUS (FCF series ordering uncertain from -layout text) |
| 22 | [page 22] L681 | "Key Financial Highlights for Q1FY2027" | chart x5 (EBITDA, PAT, Op. Revenue, EBITDA Margin%, PAT Margin%, Q1FY26/Q4FY26/Q1FY27) + text bullets | native | ADJ_METRIC_FOOTNOTE |
| 23 | [page 23] L736 | "Consolidated Profit & Loss" | table (20 line items x 8 period/variance columns) | native | see Table C |
| 24 | [page 24] L773 | "Consolidated Balance Sheet" | table (38 line items x 2 period columns, dual Assets/Equity&Liabilities layout) | native | see Table D |
| 25 | [page 25] L808 | "Company Overview" (section divider) | text (title only) | OCR-confirmed, title+section label+page#+logo only | OCR_THIN |
| 26 | [page 26] L824 | "RateGain's Offering to enable Global Clients to Unlock New Revenue with the Power of AI" | text/table (3-column business-unit overview: DaaS/Distribution/MarTech) | native | CROSS_LISTED (Adara, Sojern acquisitions listed under 2 of 3 columns) |
| 27 | [page 27] L875 | "Multiple Growth Engines to Drive Growth" | text (6 strategy pillars, no numbers) | native | FORWARD_LOOKING |
| 28 | [page 28] L905 | "Annexures" (section divider) | text (title only) | OCR-confirmed, title+section label+page#+logo only (OCR misrenders page# as "2u7,") | OCR_THIN |
| 29 | [page 29] L919 | "Key Shareholders" / "Shareholder Types (as of June 30, 2026)" | table + pie chart | native | — |
| 30 | [page 30] L951 | "Thank You" | text (contact block) | native | — |

Dropped-slide check (item A3 of INVESTOR PRESENTATION rules): **N/A** — no prior-quarter presentation ledger found under `runs/` for RATEGAIN to diff against. Flag for A3/A4: obtain prior-quarter deck if available to run `DROPPED_SLIDE` comparison; not performed this cycle.

---

## TABLE B — SLIDE-LEVEL NUMBERS & CHART DATA LABELS (by slide)

### Slide 1 (page 1) — cover letter
| Item | Value | Flag |
|---|---|---|
| Letter date | August 06, 2026 | — |
| NSE symbol | RATEGAIN | — |
| BSE code | 543417 | — |
| Quarter ended | June 30, 2026 | — |
| CIN | L72900DL2012PLC244966 | — |
| Digital signature timestamp | 2026.08.06 13:34:15 +05'30' (Mukesh Kumar, General Counsel, Company Secretary & Compliance Officer) | SIGNATURE_BLOCK |
| Membership No. | A17925 | — |
| Registered Tel | +91 120 5057000 | — |

### Slide 3 (page 3) — Safe Harbor
No numeric data. Full-paragraph forward-looking-statement disclaimer — recorded once in Table F (row F1).

### Slide 5 (page 5) — Who we serve / What we do
| Item | Value | Flag |
|---|---|---|
| Global Fortune 500 companies served | 25 | — |
| Top hotel chains served | 33 of Top 40 | — |
| OTAs & Metas | "All Leading" (qualitative, non-numeric) | — |
| Car rental companies served | 7 of Top 10 | — |
| Airlines served | 4 of Top 5 | — |
| Cruise lines | "Large" (qualitative) | — |
| DMOs | "Largest" (qualitative) | — |

### Slide 9 (page 9) — headline growth callouts
| Item | Value | Flag |
|---|---|---|
| Operating Revenue Q1FY27 | INR 785.0 Cr | — |
| Operating Revenue YoY growth | 187.6% | — |
| Adj. EBITDA Q1FY27 | INR 193.4 Cr (24.6% margin) | ADJ_METRIC |
| Adj. EBITDA YoY growth | 289.3% | — |
| Adj. PAT Q1FY27 | INR 116.8 Cr (14.9% margin) | ADJ_METRIC |
| Adj. PAT YoY growth | 148.8% | — |
| Footnote | "EBITDA and PAT are Adjusted for Deferred Deal Consideration related to the Sojern Acquisition. This expense is to be incurred for 3 years ending Q3FY29." | see Table E row E1 |

### Slide 10 (page 10) — Diversified Revenue Streams
| Item | Value(s) | Flag |
|---|---|---|
| NRR (Net Revenue Retention) series, FY2024/FY2025/FY2026/Q1FY2027 | 120.9 / 100.5 / 99.6 / 106.8 | CHART_LABEL_AMBIGUOUS (axis pairing inferred, not independently confirmed) |
| GRR (Gross Revenue Retention) series, same periods | 94.2 / 95.1 / 94.9 / 95.6 (axis ceiling label "100" also present) | CHART_LABEL_AMBIGUOUS |
| LTV:CAC series, FY2023-Q1FY2027 | 21.3 / 14.1 / 13.6 / 12.8 / 10.7 | — |
| No. of customers, FY2023-Q1FY2027 | 2,942 / 3,279 / 3,224 / 13,410 / 14,158 | — |
| Revenue by Engagement: Subscription / Transaction / Hybrid | 79.1% / 13.9% / 7.3% | CHART_LABEL_AMBIGUOUS (legend-to-value pairing inferred) |
| Revenue by Industry Type: Hospitality/DMOs/OTAs/Airlines/Car Rentals/Others | values present: 33.5%, 7.3%, 46.7%, 4.1%, 2.1%, 6.3% (6 categories, 6 values, exact pairing per legend order uncertain) | CHART_LABEL_AMBIGUOUS |
| Revenue by Geography: North America/Asia Pacific/Europe/Others | 66.2% / 20.5% / 10.8% / 2.5% | CHART_LABEL_AMBIGUOUS |
| Revenue by Customers: Top 1-10 / Others | 17.6% / 82.4% | — |
| Footnote(s) | rounding note + GRR/NRR/LTV:CAC definitions (numbered 1-3) | see Table E row E2 |

### Slide 11 (page 11) — 8 KPI tiles
| Item | Value | Flag |
|---|---|---|
| Total Pipeline | INR 664 Cr | — |
| Net Cash & Equiv. | INR 255.6 Cr | — |
| Net Debt | INR 615.4 Cr | — |
| Free Cash Flow Conversion | 78.8% | — |
| Customers (post-Sojern) | 14,158 | — |
| New Contract Wins | INR 141.0 Cr | — |
| LTV to CAC | 10.7x (compared to 14.5x in Q1FY26) | — |
| Revenue per Employee | INR 2.5 Cr, +95.3% YoY | — |
| Employees | 1,261, +47.3% YoY headcount growth | — |

### Slide 12 (page 12) — Segment growth + partnerships
| Item | Value | Flag |
|---|---|---|
| DAAS segment YoY growth Q1FY27 | 22.7% | — |
| DISTRIBUTION segment YoY growth Q1FY27 | 3.1% | — |
| MARTECH segment YoY growth Q1FY27 | 341.2% | — |
| Named partnerships (qualitative, no $/numeric value disclosed) | Philippine Airlines, Duetto, Cinko, ZentrumHub, BoxPay, Citrus Leisure (UNO Direct Stack), 2026 Best in SaaS Award | — |

### Slide 13 (page 13) — Award badge
| Item | Value | Flag |
|---|---|---|
| Consecutive award years | "3 Years in a Row" | — |
| Award category (native + OCR) | "Best Company in AI-Powered Travel Marketing"; OCR layer adds badge text "BEST IN SAAS" | OCR_SUPPLEMENT |

### Slide 14 (page 14) — People & Culture
| Item | Value | Flag |
|---|---|---|
| Attrition Rate Q1FY27 | 14.0% | — |
| New colleagues hired | 85 | — |
| Learning hours delivered | "Over 3,000" | — |
| Employee Resource Groups institutionalized | 5 | — |

### Slide 17 (page 17) — Agentic ARI
| Item | Value | Flag |
|---|---|---|
| ARI Traffic optimization | 30-40% | — |

### Slide 19 (page 19) — RG Pay
| Item | Value | Flag |
|---|---|---|
| Revenue Uplift | 15% | — |
| Reduction in Revenue Leakage | 2-4% | — |
| Lift in stay conversion | ~20% | — |
| VCC currencies supported | 25+ | — |

### Slide 21 (page 21) — 5-year financial trend charts
| Item | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 | Q1FY2027 | Flag |
|---|---|---|---|---|---|---|---|
| Operating Revenue (INR Cr) | 366.6 | 565.1 | 957.0 | 1,076.7 | 1,823.6 | 785.0 | — |
| Gross Margin (%) | 76.0 | 75.1 | 75.3 | 75.0 | 70.6 | 69.2 | — |
| EBITDA (INR Cr) | 30.6 | 84.7 | 189.7 | 232.1 | 358.3* | 193.4* | ADJ_METRIC |
| EBITDA Margin (%) | 8.3 | 15.0 | 19.8 | 21.6 | 19.6 | 24.6* | ADJ_METRIC |
| Free Cash Flow (INR Cr) | n/a | 47.5 | 113.4 | 148.1 | 230.0 | 135.2 | CHART_LABEL_AMBIGUOUS (period-to-value pairing inferred from axis-label proximity in -layout text; A3/A4 should verify) |
Additional callout: "49.3% CAGR" (Operating Revenue). Footnote: Adj. EBITDA note (Table E row E3).

### Slide 22 (page 22) — QoQ/YoY quarterly charts
| Item | Q1FY26 | Q4FY26 | Q1FY27 | Flag |
|---|---|---|---|---|
| EBITDA (INR Cr) | 49.7 | 167.9* | 193.4* | ADJ_METRIC |
| PAT (INR Cr) | 46.9 | 90.9* | 116.8* | ADJ_METRIC |
| Operating Revenue (INR Cr) | 272.9 | 715.5 | 785.0 | — |
| EBITDA Margin (%) | 18.2 | 23.5* | 24.6* | ADJ_METRIC |
| PAT Margin (%) | 17.2 | 12.7 | 14.9* | ADJ_METRIC |
Bullet text (forward/guidance-adjacent): "EBITDA and PAT are adjusted on account of deferred deal consideration related to Sojern acquisition, to be paid over 3 years up to Q3FY29" — see Table E row E4 / Table F row F4.

### Slide 26 (page 26) — Business unit overview
| Item | DaaS | Distribution | MarTech | Flag |
|---|---|---|---|---|
| Founded | 2005 | 2008 | 2019 | — |
| Revenue Mix Q1FY2027 | 12.6% | 6.3% | 81.1% | — |
| Total SAM | USD 1.1 Bn | USD 1.9 Bn | USD 5.8 Bn | — |
| Acquisitions listed | Adara (2023), Sojern (2025) | DHISCO (2018) | BCV Social (2019), MyHotelShop (2021), Adara (2023), Sojern (2025) | CROSS_LISTED — Adara and Sojern appear under both DaaS and MarTech columns |
| New AI products | Rev-AI, Demand-AI | Content-AI, Voice Connectivity (UNO VIVA), Booking Engine MCP | (shared row, not column-specific per source layout) | — |

### Slide 29 (page 29) — Shareholding
| Item | Value | Flag |
|---|---|---|
| Bhanu Chopra & Family (Promoter) holding | 48.78% | — |
| Promoter holding as of Sept 30, 2025 (comparator) | 48.16% | — |
| Sundaram Mutual Fund | 5.46% | — |
| Nippon Life India Mutual Fund | 4.49% | — |
| Paisabuddy Finance | 3.80% | — |
| Axis Mutual Fund | 2.93% | — |
| ICICI Prudential Mutual Fund | 1.85% | — |
| Plutus Wealth Management | 1.69% | — |
| CIF III Scheme I | 1.23% | — |
| Shareholder type: Promoters & Promoter Group | 48.78% | — |
| Shareholder type: Others | 17.63% | — |
| Shareholder type: Corporate Bodies | 9.41% | — |
| Shareholder type: FIIs | 5.75% | — |
| Shareholder type: Mutual Funds | 17.56% | — |
| Shareholder type: Insurance Companies | 0.87% | — |
| As-of date | June 30, 2026 | — |

### Slide 30 (page 30) — contact
| Item | Value | Flag |
|---|---|---|
| IR contact | Mr. Divik Anand | — |
| Email | investor.relations@rategain.com | — |
| CIN | L72900DL2012PLC244966 | — |

Slides with no numeric content (text/diagram/photo only, confirmed by full read, not just OCR note): 4, 6, 16, 18, 27 (page 18 and 27 carry qualitative bullet claims only, no hard figures — note for A4 as thin evidentiary support for any quantified claim inferred from them).

---

## TABLE C — CONSOLIDATED P&L LINE ITEMS (page 23, [page 23] L736-772) — 20 rows

Columns: Q1 FY27 | Q1 FY26 | YoY% | Q4 FY26 | QoQ% | FY26 | FY25 | YoY%(FY)

| # | Line item | Q1FY27 | Q1FY26 | YoY | Q4FY26 | QoQ | FY26 | FY25 | FY YoY | Flag |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Revenue | 785.0 | 272.9 | 187.6% | 715.5 | 9.7% | 1,823.6 | 1,076.7 | 69.4% | — |
| 2 | Employee Expenses | 294.8 | 109.1 | 170.1% | 269.5 | 9.4% | 711.7 | 398.8 | 78.5% | — |
| 3 | Other Expenses | 318.7 | 114.1 | 179.3% | 299.0 | 6.6% | 774.4 | 445.9 | 73.7% | — |
| 4 | Total Operating Expense | 613.5 | 223.2 | 174.8% | 568.5 | 7.9% | 1,486.1 | 844.6 | 76.0% | — |
| 5 | EBITDA | 171.5 | 49.7 | 245.4% | 147.0 | 16.7% | 337.5 | 232.1 | 45.4% | — |
| 6 | EBITDA % | 21.9% | 18.2% | — | 20.5% | — | 18.5% | 21.6% | — | — |
| 7 | Add: Sojern - Deferred Consideration | 21.9 | (blank) | — | 20.9 | — | 20.9 | (blank) | — | NOT_FOUND for Q1FY26/FY25 columns (Sojern acquisition post-dates those periods; not a zero, a structural NA) |
| 8 | Adj. EBITDA | 193.4 | 49.7 | 289.3% | 167.9 | 15.2% | 358.3 | 232.1 | 54.4% | ADJ_METRIC |
| 9 | Adj. EBITDA % | 24.6% | 18.2% | — | 23.5% | — | 19.6% | 21.6% | — | ADJ_METRIC |
| 10 | Depreciation | 3.7 | 1.9 | 100.2% | 2.6 | 41.7% | 11.4 | 6.7 | 69.1% | — |
| 11 | Amortization of Acquisition cost | 33.8 | 6.8 | 393.9% | 32.4 | 4.4% | 69.3 | 28.2 | 145.9% | — |
| 12 | Finance Costs | 16.5 | 0.3 | 5451.3% | 18.4 | -10.3% | 31.5 | 1.3 | 2380.2% | — |
| 13 | Exceptional Expenses | - | - | - | - | - | 34.6 | - | NA | **ZERO_STANDING** — dash in Q1FY27/Q1FY26/QoQ/Q4FY26/YoY cols; only FY26 col carries 34.6 (one-time item per footnote at L771) |
| 14 | Other Income | 3.1 | 20.7 | -85.1% | 2.6 | 19.9% | 61.3 | 76.4 | -19.7% | — |
| 15 | Profit/(Loss) Before Tax | 120.6 | 61.3 | 96.6% | 96.2 | 25.3% | 252.0 | 272.2 | -7.4% | — |
| 16 | Tax | 25.7 | 14.4 | 78.2% | 26.2 | -2.1% | 57.6 | 63.3 | -9.1% | — |
| 17 | Profit/(Loss) After Tax | 94.9 | 46.9 | 102.2% | 70.0 | 35.6% | 194.4 | 208.9 | -7.0% | — |
| 18 | PAT % | 12.1% | 17.2% | — | 9.8% | — | 10.7% | 19.4% | — | — |
| 19 | Adj. Profit/(Loss) After Tax | 116.8 | 46.9 | 148.8% | 90.9 | 28.5% | 249.9 | 208.9 | 19.6% | ADJ_METRIC |
| 20 | Adj. PAT % | 14.9% | 17.2% | — | 12.7% | — | 13.7% | 19.4% | — | ADJ_METRIC |

Footnotes attached (see Table E row E5): rounding note; Adj. EBITDA & PAT definition note; FY26 Adj. PAT note re: one-time exceptional expense in Q3FY26.

---

## TABLE D — CONSOLIDATED BALANCE SHEET LINE ITEMS (page 24, [page 24] L773-806) — 38 rows

Columns: Jun-26 | Mar-26 (both sides of the two-column Assets / Equity & Liabilities layout)

**Assets side (19 rows)**
| # | Line item | Jun-26 | Mar-26 | Flag |
|---|---|---|---|---|
| 1 | Non-Current Assets (subtotal) | 2,573.8 | 2,605.2 | — |
| 2 | Property, plant and equipment | 14.3 | 12.3 | — |
| 3 | Goodwill | 1,591.5 | 1,581.0 | — |
| 4 | Other intangible assets | 756.3 | 784.9 | — |
| 5 | Other intangible assets under development | - | - | **ZERO_STANDING** both periods |
| 6 | Right to use assets | 22.2 | 24.5 | — |
| 7 | i. Investments (non-current financial assets) | - | - | **ZERO_STANDING** both periods |
| 8 | ii. Other financial assets incl. Loans (non-current) | 2.3 | 2.3 | — |
| 9 | Deferred tax assets (net) | 158.3 | 167.8 | — |
| 10 | Non-Current Tax Assets | 27.9 | 31.3 | — |
| 11 | Other non-current assets | 1.0 | 1.1 | — |
| 12 | Current assets (subtotal) | 1,085.3 | 954.6 | — |
| 13 | i. Investments (current financial assets) | 19.7 | 24.5 | — |
| 14 | ii. Trade receivables | 535.7 | 471.5 | — |
| 15 | iii. Cash and cash equivalents | 226.8 | 173.1 | — |
| 16 | iv. Bank balances other than (iii) above | 9.1 | - | **ZERO_STANDING** Mar-26 only |
| 17 | Other financial assets incl. Loans (current) | 9.4 | 13.7 | — |
| 18 | Other current assets | 284.6 | 271.8 | — |
| 19 | Total assets | 3,659.1 | 3,559.8 | — |

**Equity & Liabilities side (19 rows)**
| # | Line item | Jun-26 | Mar-26 | Flag |
|---|---|---|---|---|
| 1 | Equity and Liabilities (subtotal) | 2,114.2 | 2,005.8 | — |
| 2 | Equity share capital | 11.8 | 11.8 | — |
| 3 | Equity attributable to owners of the Company | 2,102.4 | 1,994.0 | — |
| 4 | Non-current liabilities (subtotal) | 731.4 | 878.1 | — |
| 5 | Borrowings (non-current) | 533.5 | 682.6 | — |
| 6 | Lease Liabilities (non-current) | 17.0 | 18.4 | — |
| 7 | Other Financial Liabilities (non-current) | 32.7 | 25.2 | — |
| 8 | Deferred tax liabilities (net) | 132.6 | 136.9 | — |
| 9 | Provisions (non-current) | 15.2 | 15.0 | LAYOUT_WRAP — value for Jun-26 (15.2) prints on the line below Mar-26 (15.0) in the -layout text due to column wrap; not a missing/zero value |
| 10 | Other non-current liabilities | 0.4 | - | **ZERO_STANDING** Mar-26 only |
| 11 | Current liabilities (subtotal) | 813.5 | 675.9 | — |
| 12 | i. Borrowings (current) | 337.5 | 238.7 | — |
| 13 | ii. Trade payables | 257.5 | 238.3 | — |
| 14 | iii. Other financial liabilities | 84.8 | 83.0 | — |
| 15 | Lease liabilities (current) | 8.3 | 9.0 | — |
| 16 | Current tax liabilities (net) | 26.0 | 19.9 | — |
| 17 | Provisions (current) | 0.9 | 0.9 | — |
| 18 | Other current liabilities | 98.5 | 86.1 | — |
| 19 | Total equity and liabilities | 3,659.1 | 3,559.8 | — |

Structural sub-headers present but carrying no values of their own (not counted as line items): "Financial Assets" (non-current, assets side), "Financial assets" (current, assets side), "Financial liabilities" (non-current, liabilities side), "Financial liabilities" (current, liabilities side) — 4 header labels.

---

## TABLE E — FOOTNOTES (6, grep-confirmed via `Note :` marker)

| # | Line | Location | First ~15 words |
|---|---|---|---|
| E1 | L270 | page 9 | "EBITDA and PAT are Adjusted for Deferred Deal Consideration related to the Sojern Acquisition. This expense..." |
| E2 | L322-325 | page 10 | "Numbers have been rounded to nearest whole percentages or one decimal place. 1. Q1FY27 Revenue from contracts..." (includes numbered sub-notes 1-3 defining engagement basis, GRR, NRR, LTV:CAC) |
| E3 | L679 | page 21 | "*- Adjusted EBITDA - EBITDA is Adjusted for Deferred Deal Consideration related to the Sojern Acquisition..." |
| E4 | L734 | page 22 | "*- Adjusted EBITDA & PAT - Adjusted for Deferred Deal Consideration related to the Sojern Acquisition..." |
| E5 | L769-771 | page 23 | "Numbers have been rounded to nearest whole percentages or one decimal place. Adjusted EBITDA & PAT..." (includes FY26 exceptional-expense carve-out note) |
| E6 | L871-872 | page 26 | "Source: Company information, Phocuswright and 1Lattice report. Numbers have been rounded to nearest one decimal..." (includes numbered sub-notes 1-4 defining Hybrid/Subscription/Transaction models) |

---

## TABLE F — FORWARD-LOOKING / GUIDANCE / COMMITMENT STATEMENTS

| # | Page | Statement (paraphrase/excerpt) | Flag |
|---|---|---|---|
| F1 | page 3 (Safe Harbor) | Full standard forward-looking-statement legal disclaimer; company "assumes no obligation to update any forward-looking information" | FORWARD_LOOKING (boilerplate) |
| F2 | page 8 | Bhanu Chopra (Chairman & MD): "the future of AI-powered travel is still ours to redefine" | FORWARD_LOOKING (qualitative, non-quantified) |
| F3 | page 8 | Ankit Aggarwal (Interim + Deputy CFO): "gives us the room to keep investing in growth while staying firm on our financial commitments, and we head into the rest of FY27 with real confidence" | FORWARD_LOOKING (qualitative, non-quantified; note dual/interim CFO title itself is a governance flag for A3/A4) |
| F4 | page 22 | "EBITDA and PAT are adjusted on account of deferred deal consideration related to Sojern acquisition, to be paid over 3 years up to Q3FY29" | FORWARD_COMMITMENT (quantified: 3-year payment horizon to Q3FY29) |
| F5 | page 27 | "Invest in GTM teams to build up presence in high-growth geos" (Geographic Expansion pillar) | FORWARD_COMMITMENT (non-quantified) |
| F6 | page 27 | "Dedicated Strategic Investments Arm to identify Complementary Opportunities and drive synergies" (Inorganic Growth pillar) | FORWARD_COMMITMENT (non-quantified) |
| F7 | page 9 / 21 / 23 (recurring) | Deferred Deal Consideration adjustment "to be incurred for 3 years ending Q3FY29" (repeated verbatim across 3 slides) | FORWARD_COMMITMENT, quantified, repeated disclosure |

---

## FLAGS SUMMARY

- **OCR_THIN** (6 slides: pages 2, 7, 15, 20, 25, 28) — section-divider/title slides confirmed by OCR to carry no numeric or chart data beyond title/section label/page number/logo.
- **OCR_SUPPLEMENT** (1 slide: page 13) — native text >100 chars but OCR surfaced one additional badge label ("BEST IN SAAS") absent from the native text layer.
- **ADJ_METRIC** — Adj. EBITDA / Adj. PAT and their margins appear on pages 9, 21, 22, 23 as company-defined non-GAAP measures (add-back: Sojern deferred deal consideration). Flagged for A3/A4 reconciliation against reported (unadjusted) EBITDA/PAT on the same slides/pages.
- **ZERO_STANDING** (5 instances): P&L "Exceptional Expenses" (page 23); BS "Other intangible assets under development" (page 24, both periods); BS "i. Investments" non-current financial assets (page 24, both periods); BS "iv. Bank balances other than (iii) above" (page 24, Mar-26 only); BS "Other non-current liabilities" (page 24, Mar-26 only).
- **CHART_LABEL_AMBIGUOUS** (3 instances): page 10 NRR/GRR series and revenue-mix pie legends; page 21 Free Cash Flow series — pdftotext -layout column/axis-to-value pairing not independently confirmable from text alone; flagged for A3/A4 visual cross-check against the source PDF.
- **CROSS_LISTED**: page 26 lists Adara (2023) and Sojern (2025) acquisitions under both the DaaS and MarTech business-unit columns.
- **LAYOUT_WRAP**: page 24 BS "Provisions" (non-current) value wraps onto the following printed line due to column width; not a missing value.
- **SIGNATURE_BLOCK**: page 1 digitally signed 2026-08-06 13:34:15 IST by Mukesh Kumar (General Counsel, CS & Compliance Officer); this is an investor-presentation cover letter, not a Board Outcome letter, so no board-meeting-conclusion-time cross-check applies.
- **FORWARD_LOOKING / FORWARD_COMMITMENT**: 7 instances, see Table F.
- **DROPPED_SLIDE analysis**: not performed — no prior-quarter presentation ledger available this run.
