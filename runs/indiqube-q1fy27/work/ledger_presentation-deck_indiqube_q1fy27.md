# A2 ENUMERATION LEDGER
Company: IndiQube Spaces Limited (INDIQUBE)
Quarter: Q1 FY27
Doctype: presentation (investor deck, 35 PDF pages, source: investor_presentation.pdf)
Extract: extract_presentation-deck_indiqube_q1fy27.txt
Prior-quarter ledger: NONE (first pipeline run for INDIQUBE — no DROPPED_SLIDE check possible this quarter; flag `NO_PRIOR_LEDGER`)

Page numbering convention: PDF page number per pdfinfo, as used by "[page N]" markers in the
extract. Printed footer numbers (which run on a different, offset sequence and are missing
entirely on 5 divider/glossary-lead pages) are recorded in the Slide Master table where present.

```
=== A2 COUNT TEST ===
category: slides             grep_count: 35   sweep_count: 35   match: yes
category: chart_flags        grep_count: 8    sweep_count: 8    match: yes
category: table_line_items   grep_count: 70   sweep_count: 70   match: yes
category: delta_callouts     grep_count: 9    sweep_count: 9    match: yes
category: all_data_points    grep_count: n/a  sweep_count: 234  match: n/a (informational total; see note)
gate_a2: pass
=== END COUNT TEST ===
```

Reconciliation notes:
- `slides`: `grep -n -E "^\[page [0-9]+\]"` on the extract returns 35, matching pdfinfo
  page_count_pdfinfo=35 in the header and my manual slide-by-slide sweep (Table 1). Match.
- `chart_flags`: `grep -n -E "^\[CHART, page [0-9]+"` returns 8, matching the header's
  ocr_pages list [2,3,4,5,7,14,24,27] and my manual sweep. Match.
- `table_line_items`: mechanical pass `grep -n -E "^\s+[A-Za-z].*[0-9]"` run separately over
  the six clean-text financial tables (pages 9, 10, 11, 12, 13, 26) returned 6+17+15+15+10+5 = 68
  raw hits. Manual sweep found 70. The 2-row gap was re-swept and explained: on pages 11 and 12
  the "Property, Plant, Equipment & Intangible Asset" sub-line of Depreciation & Amortization is
  word-wrapped across three physical lines (label on two lines, values alone on a third,
  e.g. extract lines 277-279 and 311-313), so the single-line grep pattern cannot anchor label+
  number together and silently drops it on both pages. Manually added back (+1 page 11, +1 page
  12) = 70, matching the sweep. This is exactly the class of miss GATE A2 exists to catch;
  re-swept, not dropped. Per-table reconciliation: p9=6/6, p10=17/17, p11=15→16/16, p12=15→16/16,
  p13=10/10, p26=5/5.
- `delta_callouts`: `grep -o '▲' <extract> | wc -l` returns 9 (page 8 x4, page 13 x1, page 15
  x3, page 23 x1). Manual sweep of every "▲ N% | prior-value" callout on those same four slides
  also totals 9. Match.
- `all_data_points`: informational total of every row in Table 2 (headline KPIs, table line
  items, chart/OCR data labels, axis-scale notes, footnote-embedded operating assumptions,
  glossary-embedded figures, cover-letter identifiers). This category spans 8 OCR'd chart pages
  and several narrative-quote pages where digit-level grep is unreliable by the extraction
  header's own admission (pages needed OCR precisely because they carry no machine text layer).
  It is not scored pass/fail; the four categories above carry GATE A2 and all reconcile exactly.

Flags used below: ZERO_STANDING, DUPLICATE_KPI, MGMT_GUIDANCE, ESTIMATE,
OPERATING_ASSUMPTION, ARITHMETIC_VARIANCE, MINOR_VARIANCE (rounding, per page 34 disclaimer),
LAYOUT_AMBIGUOUS, EXTRACTION_ARTIFACT, AXIS_SCALE, NO_NUMERIC_CONTENT, NO_PRIOR_LEDGER.

---
## TABLE 1 — SLIDE MASTER (35 rows)

| Pg | Footer# | Title / section | Content type | OCR |
|---|---|---|---|---|
| 1 | — | Reg 30 cover letter to BSE/NSE re: Q1 FY27 analyst presentation | text (regulatory letter) | no |
| 2 | — | Title slide: "Investor Presentation Q1 FY27 Aug 2026" | chart/graphic | yes |
| 3 | 2 | IndiQube's Growth Journey (funding/listing timeline) | chart (infographic) | yes |
| 4 | 3 | Our Mission / Our Vision (Grow/DesignQube/IndiQare/Eco/MiQube) | chart (infographic) | yes |
| 5 | 4 | We Are India's Integrated Managed Spaces Platform (segment map) | chart (infographic) | yes |
| 6 | 5 | Reflections from Leadership (CEO Rishi Das + Cofounder Meghna Agarwal quotes) | text (narrative + embedded KPIs) | no |
| 7 | — | Section divider: "Financial Highlights" | chart (divider) | yes |
| 8 | 7 | Highest Quarterly Revenue, Strong Growth in Profitability | table/KPI tiles | no |
| 9 | 8 | Key Financial Indicators (Net Worth / Net Debt / EPS / D-E ratio) | chart + table | no |
| 10 | 9 | Profit & Loss Statement (IGAAP Equivalent) | table | no |
| 11 | 10 | Reconciliation of IGAAP Equivalent & Ind AS (P&L build) | table | no |
| 12 | 11 | Reconciliation of IGAAP Equivalent & Ind AS (EBIT build + summary) | table | no |
| 13 | 12 | Cash EBIT & Adjusted Cash EBIT | table + chart | no |
| 14 | — | Section divider: "Operational Highlights" | chart (divider) | yes |
| 15 | 14 | Pan-India Growth with Strong Steady State Occupancy | KPI tiles + bullets | no |
| 16 | 15 | Growth Runway with 3.87 Mn Sq.Ft. in Occupancy Headroom | chart (bridge) | no |
| 17 | 16 | Expanding Footprint with Improving Steady State Occupancy | chart (grouped trend) | no |
| 18 | 17 | Asset Liability Management (breakeven/lock-in/payback timeline) | chart (timeline) | no |
| 19 | 18 | Acquiring Supply, The India Way! (sourcing mix) | KPI tiles | no |
| 20 | 19 | Fostering Workspaces For Large Size, Long Stay Enterprises | KPI tiles + charts | no |
| 21 | 20 | Scaling Horizons Across India's Growth Corridors (city map) | table (city-by-city) | no |
| 22 | 21 | Growing Contribution of Value-Added Services | chart (bar) | no |
| 23 | 22 | Digital Workplaces Powered by MiQube Tech Stack | KPI tiles + chart | no |
| 24 | — | Section divider: "Questions for Investors" | chart (divider) | yes |
| 25 | 24 | Key Questions Addressed for Investors (1/2) — profitability, Cash EBIT vs EBITDA | text + chart | no |
| 26 | 25 | Key Questions Addressed for Investors (2/2) — lease liability, ROU | text + table | no |
| 27 | — | Section divider: "Glossary" (illustration only, no text/numeric content) | photo/graphic | yes |
| 28 | 27 | Glossary (1/6): AUM, Rent Paying Area, LOI Signed, Rent Yielding Area, Occupancy | table (defs) | no |
| 29 | 28 | Glossary (2/6): IndiQube Grow, DesignQube, IndiQare, MiQube, Eco | table (defs) | no |
| 30 | 29 | Glossary (3/6): Revenue, EBITDA, EBITDA margin, EPS, Recurring/One Time Revenue | table (defs) | no |
| 31 | 30 | Glossary (4/6): Net Worth, Net Debt, Other Expense, Other Income | table (defs) | no |
| 32 | 31 | Glossary (5/6): Revenue from operations, Lease Liability, Payment of Lease Liability, Income on Finance lease | table (defs) | no |
| 33 | 32 | Glossary (6/6): ROU, Depreciation on ROU, Cash EBIT, Cash EBIT margin, Adjusted Cash EBIT (+margin), Interest on Lease Liability | table (defs) | no |
| 34 | 33 | Disclaimer (forward-looking statements + Valorem Advisors IR disclaimer + rounding note) | text | no |
| 35 | — | Thank You / contact page (CFO Pawan Jain; Valorem's Anuj Sonpal) | text | no |

DROPPED_SLIDE check: N/A — `NO_PRIOR_LEDGER`, first pipeline run for this ticker; no prior deck
to diff against. A3/A4 should treat every slide above as baseline for next quarter's diff.

---
## TABLE 2 — DATA POINT LEDGER (234 rows)
Every number / labeled data point on every slide, keyed by slide (page) number. Grouped by
slide for auditability; row IDs are sequential (D001…D234) and carry the slide number as their
own column per the anti-miss mandate.

### Page 1 — Reg 30 cover letter (11)
| ID | Pg | Label | Value | Flags |
|---|---|---|---|---|
| D001 | 1 | BSE Scrip Code | 544454 | |
| D002 | 1 | NSE Scrip Symbol | INDIQUBE | |
| D003 | 1 | Letter date | Aug 12, 2026 | |
| D004 | 1 | Prior intimation date (of the analyst call) | Aug 05, 2026 | |
| D005 | 1 | Analyst/Investor call date | Thursday, Aug 13, 2026 | |
| D006 | 1 | Analyst/Investor call time | 2:00 pm IST | |
| D007 | 1 | Quarter end date | June 30, 2026 | |
| D008 | 1 | CIN | L45400KA2015PLC133523 | DUPLICATE_KPI (repeats p35) |
| D009 | 1 | Registered office phone | +91 9900092210 | |
| D010 | 1 | Registered office pincode | 560103 | |
| D011 | 1 | Digital signature timestamp (Bhasker Dubey, CS & Compliance Officer) | 2026.08.12 17:34:06 +05'30' | |

### Page 2 — Title slide (2)
| ID | Pg | Label | Value | Flags |
|---|---|---|---|---|
| D012 | 2 | Quarter label | Q1 FY27 | NO_NUMERIC_CONTENT (label only) |
| D013 | 2 | Deck date | Aug 2026 | NO_NUMERIC_CONTENT (label only) |

### Page 3 — Growth Journey timeline (chart, OCR) (12)
| ID | Pg | Label | Value | Flags |
|---|---|---|---|---|
| D014 | 3 | Timeline marker | 2013 (Promoters identify addressable gap in Commercial Real Estate) | |
| D015 | 3 | Timeline marker | 2015 (IndiQube Incorporated) | DUPLICATE_KPI (CIN year matches, p1/p35) |
| D016 | 3 | Timeline marker | 2018 (Started foray into Tier II cities) | |
| D017 | 3 | Timeline marker | 2021 ($15 Mn strategic investment by Group company) | |
| D018 | 3 | Timeline marker | 2022 ($30 Mn funding led by WestBridge Capital) | |
| D019 | 3 | Timeline marker | Jul 30, 2025 (Listed on NSE & BSE) | |
| D020 | 3 | Timeline marker | Jun 30, 2026 (current AUM/centers/cities snapshot date) | |
| D021 | 3 | Strategic investment amount | $15 Mn | |
| D022 | 3 | WestBridge Capital funding amount | $30 Mn | |
| D023 | 3 | Cities (as of Jun 30, 2026) | 17 | DUPLICATE_KPI (p15, p21) |
| D024 | 3 | Centers (as of Jun 30, 2026) | 137 | DUPLICATE_KPI (p15, p21) |
| D025 | 3 | AUM (as of Jun 30, 2026) | 10.61 Mn Sq.ft | DUPLICATE_KPI (p15, p16, p17, p21) |

### Page 4 — Mission/Vision (1)
| ID | Pg | Label | Value | Flags |
|---|---|---|---|---|
| D026 | 4 | Mission/Vision + 5 service-line taglines (Grow, DesignQube, IndiQare, Eco, MiQube) | — no numeric content | NO_NUMERIC_CONTENT |

### Page 5 — Integrated Managed Spaces Platform (1)
| ID | Pg | Label | Value | Flags |
|---|---|---|---|---|
| D027 | 5 | Segment map: Grow / IndiQare / DesignQube / Eco descriptions | — no numeric content | NO_NUMERIC_CONTENT |

### Page 6 — Reflections from Leadership (16) — basis: IGAAP Equivalent (footer "5 | IGAAP Equivalent")
| ID | Pg | Label | Value | Flags |
|---|---|---|---|---|
| D028 | 6 | Revenue (CEO quote) | ₹428 crore | DUPLICATE_KPI (p8, p10) |
| D029 | 6 | Revenue YoY growth (CEO quote) | 37% | DUPLICATE_KPI (p8) |
| D030 | 6 | EBITDA (CEO quote) | ₹87 crore | DUPLICATE_KPI (p8, p10) |
| D031 | 6 | EBITDA YoY growth (CEO quote) | 34% | DUPLICATE_KPI (p8) |
| D032 | 6 | EBIT (CEO quote) | ₹55 crore | DUPLICATE_KPI (p8, p12) |
| D033 | 6 | EBIT YoY growth (CEO quote) | 59% | DUPLICATE_KPI (p8) |
| D034 | 6 | PAT (CEO quote) | ₹35 crore | DUPLICATE_KPI (p8, p10) |
| D035 | 6 | PAT YoY growth (CEO quote) | 91% | DUPLICATE_KPI (p8) |
| D036 | 6 | EBITDA margin (CEO quote) | 20% | DUPLICATE_KPI (p8, p10) |
| D037 | 6 | EBIT margin (CEO quote) | 13% | DUPLICATE_KPI (p8) |
| D038 | 6 | PAT margin (CEO quote) | 8% | DUPLICATE_KPI (p8, p10) |
| D039 | 6 | Steady state occupancy (Cofounder quote) | 90% | DUPLICATE_KPI (p15, p17) |
| D040 | 6 | Overall occupancy (Cofounder quote) | 86% | DUPLICATE_KPI (p15) |
| D041 | 6 | VAS revenue (Cofounder quote) | ₹72 crore | DUPLICATE_KPI (p22) |
| D042 | 6 | VAS contribution to operating revenue, prior | 11% | DUPLICATE_KPI (p22) |
| D043 | 6 | VAS contribution to operating revenue, current | 17% | DUPLICATE_KPI (p22) |

### Page 7 — Section divider "Financial Highlights" (1)
| ID | Pg | Label | Value | Flags |
|---|---|---|---|---|
| D044 | 7 | Divider text only | — no numeric content | NO_NUMERIC_CONTENT |

### Page 8 — Highest Quarterly Revenue (7) — basis: IGAAP Equivalent (footer "7 | IGAAP Equivalent")
| ID | Pg | Label | Q1 FY27 | ▲ YoY | Q1 FY26 | Flags |
|---|---|---|---|---|---|---|
| D045 | 8 | Revenue | ₹428 Cr | 37% | ₹313 Cr | DUPLICATE_KPI (p6,p10) |
| D046 | 8 | EBITDA | ₹87 Cr | 34% | ₹65 Cr | DUPLICATE_KPI (p6,p10) |
| D047 | 8 | EBIT | ₹55 Cr | 59% | ₹34 Cr | DUPLICATE_KPI (p6,p12) |
| D048 | 8 | PAT | ₹35 Cr | 91% | ₹19 Cr | DUPLICATE_KPI (p6,p10); MINOR_VARIANCE — P&L table (p10) states Q1FY26 PAT as ₹18.5 Cr, not ₹19 Cr; disclaimer (p34) attributes such gaps to rounding |
| D049 | 8 | EBITDA Margin | 20% | — | 21% | DUPLICATE_KPI (p6,p10) |
| D050 | 8 | EBIT Margin | 13% | — | 11% | DUPLICATE_KPI (p6) |
| D051 | 8 | PAT Margin | 8% | — | 6% | DUPLICATE_KPI (p6,p10) |

### Page 9 — Key Financial Indicators (13) — basis: IGAAP Equivalent (footer "8 | IGAAP Equivalent")
| ID | Pg | Label | Q1 FY26 | Q1 FY27 | Flags |
|---|---|---|---|---|---|
| D052 | 9 | Net Worth chart bars (₹ Cr) | 395 | 1194 | DUPLICATE_KPI (=D059) |
| D053 | 9 | Net Debt chart bars (₹ Cr) | 377 | (66) | DUPLICATE_KPI (=D058) |
| D054 | 9 | EPS (Annualized) chart | 4.1 | 6.6 | |
| D055 | 9 | Net Worth chart Y-axis scale | -300 to 1300, step 200 | — | AXIS_SCALE |
| D056 | 9 | EPS chart Y-axis scale | -1 to 9, step 1 | — | AXIS_SCALE |
| D057 | 9 | Table: Gross Debt (₹ Cr) | 377 | 278 | |
| D058 | 9 | Table: Bank Balances other than Cash & Cash Equivalent (₹ Cr) | 0 | 325 | ZERO_STANDING (Q1FY26=0) |
| D059 | 9 | Table: Cash & Cash Equivalents (₹ Cr) | 0 | 18 | ZERO_STANDING (Q1FY26=0) |
| D060 | 9 | Table: Net Debt (A)* (₹ Cr) | 377 | (66) | DUPLICATE_KPI (=D053) |
| D061 | 9 | Table: Net Worth (B) (₹ Cr) | 395 | 1194 | DUPLICATE_KPI (=D052) |
| D062 | 9 | Table: Debt-to-Equity Ratio = A/B | 0.95 | 0.05 | |
| D063 | 9 | Small D-to-E ratio bar chart | 0.95 | 0.05 | DUPLICATE_KPI (=D062) |
| D064 | 9 | Table column-header layout bleed ("Q3 ... FY25 ... Q3Q1 FY27 FY26") | — | — | EXTRACTION_ARTIFACT — pdftotext -layout column bleed; actual headers are simply "Q1 FY26" / "Q1 FY27" per every other slide in the deck |

Footnote D-set (p9): "Net Debt : (Gross Debt – Bank Balances other than Cash & Cash Equivalents
– Cash & Cash Equivalents)" — see Table 4.

### Page 10 — Profit & Loss Statement (17) — ₹ Cr, basis IGAAP Equivalent (footer "9 | IGAAP Equivalent")
| ID | Pg | Line item | Q1 FY27 | Q4 FY26 | Q1 FY26 | Flags |
|---|---|---|---|---|---|---|
| D065 | 10 | Revenue | 428 | 407 | 313 | DUPLICATE_KPI (p6,p8) |
| D066 | 10 | Recurring Revenue | 395 | 372 | 307 | |
| D067 | 10 | One Time Revenue | 33 | 35 | 7 | |
| D068 | 10 | Expenses | 342 | 327 | 248 | |
| D069 | 10 | Purchase of Traded Goods | 27 | 26 | 10 | |
| D070 | 10 | Employee Benefit Expense | 24 | 24 | 20 | |
| D071 | 10 | Other expenses | 291 | 276 | 218 | |
| D072 | 10 | EBITDA | 87 | 80 | 65 | DUPLICATE_KPI (p6,p8) |
| D073 | 10 | EBITDA Margin % | 20% | 20% | 21% | DUPLICATE_KPI (p6,p8) |
| D074 | 10 | Less: Finance Cost | 11 | 9 | 10 | |
| D075 | 10 | Less: Depreciation & Amortization | 40 | 41 | 30 | |
| D076 | 10 | Add: Other Income | 8 | 8 | 0 | ZERO_STANDING (Q1FY26=0) |
| D077 | 10 | Profit Before Tax | 43 | 38 | 25 | |
| D078 | 10 | PBT Margin % | 10% | 9% | 8% | |
| D079 | 10 | Less: Tax Expenses | 8 | 9 | 6 | |
| D080 | 10 | PAT | 35 | 30 | 18.5 | DUPLICATE_KPI (p6,p8); MINOR_VARIANCE — Q1FY26 value here (18.5) vs p8's rounded 19 |
| D081 | 10 | PAT Margin % | 8% | 7% | 6% | DUPLICATE_KPI (p6,p8) |

### Page 11 — Reconciliation of IGAAP Equivalent & Ind AS, table 1 (16) — ₹ Cr (footer "10 |")
Columns per period: Ind AS | Ind AS Adj. | IGAAP Eq.
| ID | Pg | Line item | Q1 FY27 (IndAS/Adj/Eq) | Q4 FY26 (IndAS/Adj/Eq) | Q1 FY26 (IndAS/Adj/Eq) | Flags |
|---|---|---|---|---|---|---|
| D082 | 11 | Revenue from operations | 423/(6)/428 | 401/(5)/407 | 309/(4)/313 | |
| D083 | 11 | Other income | 26/18/8 | 24/16/8 | 15/15/0 | ZERO_STANDING (Q1FY26 IGAAP Eq.=0) |
| D084 | 11 | Total Income | 449/13/436 | 426/11/415 | 324/11/313 | |
| D085 | 11 | Purchases of traded goods | 27/0/27 | 26/0/26 | 10/0/10 | ZERO_STANDING (Ind AS Adj.=0 every period — line exists only to show no Ind AS adjustment applies) |
| D086 | 11 | Employee benefit expense | 24/0/24 | 24/0/24 | 20/0/20 | ZERO_STANDING (Ind AS Adj.=0 every period) |
| D087 | 11 | Finance costs | 127/116/11 | 119/111/9 | 110/100/10 | |
| D088 | 11 | — Interest on borrowings | 11/0/11 | 9/0/9 | 10/0/10 | ZERO_STANDING (Ind AS Adj.=0 every period) |
| D089 | 11 | — Interest on lease liabilities | 116/116/0 | 111/111/0 | 100/100/0 | ZERO_STANDING (IGAAP Eq.=0 every period — canonical template signal: lease-liability interest does not exist on the IGAAP-equivalent basis) |
| D090 | 11 | Depreciation & Amortization expense | 188/148/40 | 177/136/41 | 143/113/30 | |
| D091 | 11 | — Property, Plant, Equipment & Intangible Asset | 40/0/40 | 41/0/41 | 30/0/30 | ZERO_STANDING (Ind AS Adj.=0 every period); word-wrapped label across extract lines 277-279, caught only on manual re-sweep (see reconciliation note) |
| D092 | 11 | — ROU (Right-of-use Assets) | 148/148/0 | 136/136/0 | 113/113/0 | ZERO_STANDING (IGAAP Eq.=0 every period — canonical template signal, ROU depreciation is an Ind AS-only construct) |
| D093 | 11 | Other expenses | 113/178/291 | 103/(173)/276 | 91/(127)/218 | |
| D094 | 11 | Total expenses | 479/86/393 | 450/73/376 | 374/86/289 | |
| D095 | 11 | Profit/(loss) before tax | (30)/(74)/43 | (24)/(62)/38 | (50)/(74)/25 | |
| D096 | 11 | Tax expense | (7)/(15)/8 | (1)/(10)/9 | (13)/(19)/6 | |
| D097 | 11 | Profit/(loss) after tax | (24)/(59)/35 | (23)/(52)/30 | (37)/(55)/19 | DUPLICATE_KPI (IGAAP Eq. column = PAT, matches p8/p10) |

### Page 12 — Reconciliation of IGAAP Equivalent & Ind AS, table 2 + EBIT summary (16) — ₹ Cr (footer "11 |")
| ID | Pg | Line item | Q1 FY27 (IndAS/Adj/Eq) | Q4 FY26 (IndAS/Adj/Eq) | Q1 FY26 (IndAS/Adj/Eq) | Flags |
|---|---|---|---|---|---|---|
| D098 | 12 | Revenue from operations | 423/(6)/428 | 401/(5)/407 | 309/(4)/313 | DUPLICATE_KPI (=D082) |
| D099 | 12 | Other income | 26/18/8 | 24/16/8 | 15/15/0 | DUPLICATE_KPI (=D083); ZERO_STANDING |
| D100 | 12 | Total Income (A) | 449/13/436 | 426/11/415 | 324/11/313 | DUPLICATE_KPI (=D084) |
| D101 | 12 | Purchases of traded goods (B) | 27/0/27 | 26/0/26 | 10/0/10 | DUPLICATE_KPI (=D085); ZERO_STANDING |
| D102 | 12 | Employee benefit expense (C) | 24/0/24 | 24/0/24 | 20/0/20 | DUPLICATE_KPI (=D086); ZERO_STANDING |
| D103 | 12 | Depreciation & Amortization expense (D) | 188/148/40 | 177/136/41 | 143/113/30 | DUPLICATE_KPI (=D090) |
| D104 | 12 | — Property, Plant, Equipment & Intangible Asset | 40/0/40 | 41/0/41 | 30/0/30 | DUPLICATE_KPI (=D091); ZERO_STANDING; word-wrapped label (extract lines 311-313), caught on manual re-sweep |
| D105 | 12 | — ROU (Right-of-use Assets) | 148/148/0 | 136/136/0 | 113/113/0 | DUPLICATE_KPI (=D092); ZERO_STANDING |
| D106 | 12 | Other expenses (E) | 113/178/291 | 103/(173)/276 | 91/(127)/218 | DUPLICATE_KPI (=D093) |
| D107 | 12 | Total expenses | 479/86/393 | 450/73/376 | 374/86/289 | DUPLICATE_KPI (=D094) |
| D108 | 12 | EBIT (A – B – C – D – E) | 96/41/55 | 95/48/47 | 60/26/34 | ARITHMETIC_VARIANCE — Ind AS column (96) for Q1FY27 disagrees with the Reconciliation Summary's "EBIT (Ind AS)" of 97 two rows below on the same slide (D109); manual check: Total Income(449) − Purchases(27) − Employee benefit(24) − D&A(188) − Other expenses(113) = 97, i.e. the summary row's 97 foots correctly and the "96" in this row does not. Q4FY26 (95=95) and Q1FY26 (60=60) tie out cleanly across both rows — only the Q1FY27 Ind AS EBIT cell is inconsistent. Flag for A3/A4 forensic follow-up. |
| D109 | 12 | RECONCILIATION SUMMARY — EBIT (Ind AS) | 97 | 95 | 60 | ARITHMETIC_VARIANCE — see D108 |
| D110 | 12 | RECONCILIATION SUMMARY — Add: Depreciation on ROU* | 148 | 136 | 113 | DUPLICATE_KPI (=D105 Ind AS Adj. column) |
| D111 | 12 | RECONCILIATION SUMMARY — Less: Other Income* | 13 | 11 | 11 | DUPLICATE_KPI (=D100 Adj. column) |
| D112 | 12 | RECONCILIATION SUMMARY — Less: Other Expenses** | 178 | 173 | 127 | DUPLICATE_KPI (=D106 Adj. column) |
| D113 | 12 | RECONCILIATION SUMMARY — EBIT (IGAAP Equivalent) | 55 | 47 | 34 | DUPLICATE_KPI (=D047/EBIT p8, p6) |

### Page 13 — Cash EBIT & Adjusted Cash EBIT (12) — ₹ Cr, basis Ind AS (footer "12 | Ind AS")
| ID | Pg | Line item | Q1 FY27 | Q4 FY26 | Q1 FY26 | Flags |
|---|---|---|---|---|---|---|
| D114 | 13 | Revenue from operations | 423 | 401 | 309 | DUPLICATE_KPI (=D082 Ind AS col) |
| D115 | 13 | Less: Purchases of traded goods | 27 | 26 | 10 | DUPLICATE_KPI (=D085 Ind AS col) |
| D116 | 13 | Less: Employee benefits expense | 24 | 24 | 20 | DUPLICATE_KPI (=D086 Ind AS col) |
| D117 | 13 | Less: Other expenses | 113 | 103 | 91 | DUPLICATE_KPI (=D093 Ind AS col) |
| D118 | 13 | Expenses (subtotal) | 165 | 153 | 121 | |
| D119 | 13 | Less: Payment of lease liabilities | 190 | 185 | 140 | DUPLICATE_KPI (=D125/D127 on p26 for Q1FY27/Q1FY26) |
| D120 | 13 | Cash EBIT | 68 | 63 | 48 | |
| D121 | 13 | Add: Income on finance lease | 6 | 5 | 4 | |
| D122 | 13 | Adjusted Cash EBIT | 75 | 68 | 52 | DUPLICATE_KPI (chart below repeats these) |
| D123 | 13 | Adjusted Cash EBIT % Revenue from operations | 18% | 17% | 17% | |
| D124 | 13 | Adjusted Cash EBIT chart bars (₹ Cr) | 75 | 68 | 52 (Q1FY26) | DUPLICATE_KPI (=D122) |
| D125 | 13 | Chart callouts "96%" / "43%" adjacent to a lone "▲" | 96%, 43% | — | — | LAYOUT_AMBIGUOUS — neither figure reconciles to a simple period-over-period growth rate on the visible bar values (68/52=30.8%, 75/68=10.3%); association with a specific comparison pair could not be determined from extracted text/layout alone; visual PDF check recommended before use |

### Page 14 — Section divider "Operational Highlights" (1)
| ID | Pg | Label | Value | Flags |
|---|---|---|---|---|
| D126 | 14 | Divider text only | — no numeric content | NO_NUMERIC_CONTENT |

### Page 15 — Pan-India Growth with Strong Steady State Occupancy (9) — as of Q1 FY27
| ID | Pg | Label | Current | ▲ YoY | Prior (Q1FY26) | Flags |
|---|---|---|---|---|---|---|
| D127 | 15 | Area Under Management | 10.61 Mn Sq.ft | 22% | 8.7 Mn Sq.ft | DUPLICATE_KPI (p3,p16,p17,p21) |
| D128 | 15 | Centers | 137 | 14% | 120 Centers | DUPLICATE_KPI (p3,p21) |
| D129 | 15 | Cities | 17 (8 Tier I & 9 Tier II) | — | — | DUPLICATE_KPI (p3,p21) |
| D130 | 15 | No of Seats | 236 K | 22% | 193 K Seats | |
| D131 | 15 | Steady State Occupancy | 90% | — | 87% | DUPLICATE_KPI (p6,p17) |
| D132 | 15 | Overall Occupancy | 86% | — | 85% | DUPLICATE_KPI (p6) |
| D133 | 15 | Key Highlight: North India expansion, office supply on Noida Expressway | 3.9 Lakh Sq.ft | — | — | MGMT_GUIDANCE — forward capacity-addition commitment, not yet operational |
| D134 | 15 | Key Highlight: Design & Build project signed, Bengaluru (Canadian VFX/animation client) | 39K sq.ft | — | — | MGMT_GUIDANCE — signed deal, forward revenue recognition |
| D135 | 15 | Key Highlight: workspace deal signed, Bangalore (consulting/mgmt services client) | ₹52 Cr | — | — | MGMT_GUIDANCE — signed deal value, forward revenue commitment |

### Page 16 — Growth Runway with 3.87 Mn Sq.Ft. Occupancy Headroom (6) — Mn Sq.ft.
| ID | Pg | Label | Value | Flags |
|---|---|---|---|---|
| D136 | 16 | Headline headroom (title figure) | 3.87 Mn Sq.ft | arithmetically consistent: 10.61 − 6.74 = 3.87 |
| D137 | 16 | Rent Yielding Area | 6.74 | DUPLICATE_KPI (p17) |
| D138 | 16 | Rent Paying Area | 7.84 | DUPLICATE_KPI (p17) |
| D139 | 16 | Rent Paying & yet to be Rent Yielding | 1.1 | consistent: 7.84 − 6.74 = 1.10 |
| D140 | 16 | Area Under Management | 10.61 | DUPLICATE_KPI (p3,p15,p17,p21) |
| D141 | 16 | LOI Signed & yet to be Rent Paying | 2.77 | consistent: 10.61 − 7.84 = 2.77 |

### Page 17 — Expanding Footprint with Improving Steady State Occupancy (5) — Mn Sq.ft.
| ID | Pg | Label | Q1 FY26 | Q4 FY26 | Q1 FY27 | Flags |
|---|---|---|---|---|---|---|
| D142 | 17 | Area Under Management (trend) | 8.70 | 9.66 | 10.61 | DUPLICATE_KPI (endpoints = p3/p15/p16/p21) |
| D143 | 17 | Rent Paying Area (trend) | 6.50 | 7.84 | 7.84 | LAYOUT_AMBIGUOUS — bar/value pairing across the 3-period grouped chart could not be confirmed from pdftotext layout alone (two "7.84" labels appear adjacent); visual check recommended |
| D144 | 17 | Rent Yielding Area (trend) | 5.54 | 6.33 | 6.74 | LAYOUT_AMBIGUOUS — same grouping caveat as D143; Q1FY27 endpoint (6.74) DUPLICATE_KPI of p16 |
| D145 | 17 | "YoY Growth" % labels beside the trend chart | 22% | 21% | 21% | LAYOUT_AMBIGUOUS — exact metric each % attaches to (AUM vs. Rent Paying vs. Rent Yielding YoY) not resolvable from extracted layout |
| D146 | 17 | Steady State Occupancy % (trend) | 87% | 88% | 90% | DUPLICATE_KPI (endpoints = p6/p15) |

### Page 18 — Asset Liability Management (9) — timeline in months from Rent Commencement Date
| ID | Pg | Label | Value | Flags |
|---|---|---|---|---|
| D147 | 18 | Operational Breakeven — occupancy range | 55%-60% | at 6M on timeline |
| D148 | 18 | Steady State Center — occupancy range | 85%-90% | at 12M on timeline; DUPLICATE_KPI concept of Steady State Occupancy 90% actual (p6/p15/p17) |
| D149 | 18 | Client Lock-in — Contractual Obligation | — (duration marker only) | at 35M on timeline |
| D150 | 18 | Capex Payback period — fit-out capex recovered | ₹1,650/sq.ft | at 36M on timeline |
| D151 | 18 | IndiQube Lock-in with Landlords — sole option to continue/vacate | — (duration marker only) | at 38M on timeline |
| D152 | 18 | Revenue to Rent Ratio | 2.21 | |
| D153 | 18 | Fit out Cost (Interior + Renovation) | ₹1,650 per Sq.ft | DUPLICATE_KPI (=D150) |
| D154 | 18 | Landlord Lock-in with IndiQube | 10-20 Yrs | |
| D155 | 18 | Narrative: "one cycle of ~3 years" (client lock-in + landlord lock-in + capex payback alignment) | ~3 years | OPERATING_ASSUMPTION |

### Page 19 — Acquiring Supply, The India Way! (7) — % of AUM (footer "18 | % of AUM")
| ID | Pg | Label | Value | Flags |
|---|---|---|---|---|
| D156 | 19 | Full Buildings | 55% | |
| D157 | 19 | Renovated Properties | 23% | |
| D158 | 19 | Tech Parks | 20% | note: 55+23+20 = 98%, 2 pts short of 100% — MINOR_VARIANCE (rounding, per p34 disclaimer) |
| D159 | 19 | Metro Proximity (centers <3 KM from operational/planned metro stations) | 82% | |
| D160 | 19 | Green Certified, total | 4.4 Mn Sq.ft | |
| D161 | 19 | Green Certified, breakdown — certified | 3.46 Mn Sq.ft (35 centers) | consistent with D160/D162: 3.46+0.96=4.42≈4.4 |
| D162 | 19 | Green Certified, breakdown — under certification | 0.96 Mn Sq.ft (7 centers) | see D161 |

### Page 20 — Fostering Workspaces For Large Size, Long Stay Enterprises (18) — as on 30 June 2026
| ID | Pg | Label | Value | Flags |
|---|---|---|---|---|
| D163 | 20 | Clients (PAN India) | 855 | |
| D164 | 20 | Brand Led Acquisition | 62% | |
| D165 | 20 | Brokerage to Ops Revenue | 2.03% | |
| D166 | 20 | GCC Share — Revenue Contribution | 53% | |
| D167 | 20 | Multi Center Clients — Revenue Contribution | 41% | |
| D168 | 20 | Occupied Area Share — Startups | 11% | sums with D169-171 to 100% (11+12+49+28) |
| D169 | 20 | Occupied Area Share — Unicorns | 12% | |
| D170 | 20 | Occupied Area Share — GCCs | 49% | |
| D171 | 20 | Occupied Area Share — Indian Enterprises | 28% | |
| D172 | 20 | Client Lease Duration (months) — 0-50 Seats | 26 | |
| D173 | 20 | Client Lease Duration (months) — 51-100 Seats | 30 | |
| D174 | 20 | Client Lease Duration (months) — 101-300 Seats | 37 | |
| D175 | 20 | Client Lease Duration (months) — 300+ Seats | 47 | |
| D176 | 20 | Client Lease Duration (months) — Portfolio (overall) | 43 | |
| D177 | 20 | Occupancy Split — 0-50 Seats | 4% | sums with D178-180 to 100% (4+6+25+65) |
| D178 | 20 | Occupancy Split — 51-100 Seats | 6% | |
| D179 | 20 | Occupancy Split — 101-300 Seats | 25% | |
| D180 | 20 | Occupancy Split — 300+ Seats | 65% | |

### Page 21 — Scaling Horizons Across India's Growth Corridors (21) — city-by-city, footer "20 |"
| ID | Pg | City (Tier) | Centers | Sq.ft | Seats | Flags |
|---|---|---|---|---|---|---|
| D181 | 21 | Bangalore (I) | 76 | 6.68M | 148K | |
| D182 | 21 | Chennai (I) | 16 | 1.17M | 26K | |
| D183 | 21 | Pune (I) | 11 | 755K | 17K | |
| D184 | 21 | Gurugram (I) | 4 | 139K | 3K | |
| D185 | 21 | Hyderabad (I) | 5 | 411K | 9K | |
| D186 | 21 | Mumbai (I) | 5 | 183K | 4K | |
| D187 | 21 | Noida (I) | 2 | 420K | 9K | |
| D188 | 21 | Kolkata (I) | 2 | 60K | 1K | |
| D189 | 21 | Coimbatore (II) | 5 | 457K | 10K | |
| D190 | 21 | Kochi (II) | 4 | 140K | 3K | |
| D191 | 21 | Madurai (II) | 1 | 37K | 1K | |
| D192 | 21 | Visakhapatnam (II) | 1 | 20K | 0.5K | |
| D193 | 21 | Jaipur (II) | 1 | 21K | 0.5K | |
| D194 | 21 | Kozhikode (II) | 1 | 20K | 0.4K | |
| D195 | 21 | Mohali (II) | 1 | 17K | 0.4K | |
| D196 | 21 | Indore (II) | 1 | 26K | 0.6K | |
| D197 | 21 | Bhubaneswar (II) | 1 | 45K | 1K | |
| D198 | 21 | TOTAL — Cities | 17 | — | — | DUPLICATE_KPI (p3,p15) |
| D199 | 21 | TOTAL — Centers | 137 | — | — | DUPLICATE_KPI (p3,p15); arithmetic check: sum of 17 city rows = 137, ties out |
| D200 | 21 | TOTAL — AUM | 10.61 M Sq.ft | — | — | DUPLICATE_KPI (p3,p15,p16,p17) |
| D201 | 21 | TOTAL — Capacity | 235,675 Seats | — | — | New precise figure not shown elsewhere; sum of city-level seat counts (≈234.4K) is consistent within city-table rounding; distinct from the rounded "236K Seats" headline on p15 (occupied/current seats, not total capacity) — not a discrepancy, two different metrics |

### Page 22 — Growing Contribution of Value-Added Services (4) — ₹ Cr (footer "21 |")
| ID | Pg | Label | Q1 FY26 | Q1 FY27 | Flags |
|---|---|---|---|---|---|
| D202 | 22 | VAS Recurring | 27 | 33 | |
| D203 | 22 | VAS One Time | 7 | 39 | |
| D204 | 22 | VAS Total | 34 | 72 | arithmetic check: 27+7=34 ✓, 33+39=72 ✓; DUPLICATE_KPI (=D041, p6) |
| D205 | 22 | VAS % Ops Revenue | 11% | 17% | DUPLICATE_KPI (=D042/D043, p6) |

### Page 23 — Digital Workplaces Powered by MiQube Tech Stack (4) — footer "22 |"
| ID | Pg | Label | Value | Flags |
|---|---|---|---|---|
| D206 | 23 | Lifetime App Downloads | 148K+ | |
| D207 | 23 | Transactions in FY26 | 1.5 Mn+ | |
| D208 | 23 | Play Store rating | 4.0 Stars | |
| D209 | 23 | MiQube Transactions Volume ('000s), Q1FY26 → Q1FY27, ▲31% | 352 → 462 | arithmetic check: 462/352=31.3% ≈31% ✓ |

### Page 24 — Section divider "Questions for Investors" (1)
| ID | Pg | Label | Value | Flags |
|---|---|---|---|---|
| D210 | 24 | Divider text only (OCR returned only stray icon fragments, no data) | — no numeric content | NO_NUMERIC_CONTENT |

### Page 25 — Key Questions Addressed (1/2) (6) — footer "24 |"
| ID | Pg | Label | Value | Flags |
|---|---|---|---|---|
| D211 | 25 | Current (Income) Tax Expense — FY24 Audited (₹ Cr) | 8.4 | |
| D212 | 25 | Current (Income) Tax Expense — FY25 Audited (₹ Cr) | 7.67 | |
| D213 | 25 | Current (Income) Tax Expense — FY26 Audited (₹ Cr) | 21.73 | |
| D214 | 25 | Current (Income) Tax Expense — Q1 FY27 Estimated (₹ Cr) | 8.14 | ESTIMATE — explicitly labeled "Estimated" on the slide, not an audited/final actual; distinct basis from the three prior columns |
| D215 | 25 | Narrative: centers take "5-6 months to break even" | 5-6 months | OPERATING_ASSUMPTION |
| D216 | 25 | Narrative: rentals capitalized "~45-60 days annually" for newly commissioned buildings | ~45-60 days | OPERATING_ASSUMPTION |

### Page 26 — Key Questions Addressed (2/2) (6) — ₹ Cr, footer "25 |"
| ID | Pg | Label | Q1 FY27 | Q1 FY26 | Flags |
|---|---|---|---|---|---|
| D217 | 26 | Narrative: contractual lock-in period | ~3.5 years | — | OPERATING_ASSUMPTION; note vs. D155 (p18) which states "~3 years" for the same underlying client/landlord lock-in cycle — worth a consistency check |
| D218 | 26 | Interest on Lease Liabilities | 116 | 100 | DUPLICATE_KPI (Ind AS col, =D089) |
| D219 | 26 | Depreciation on Right of Use Assets | 148 | 113 | DUPLICATE_KPI (Ind AS Adj. col, =D092) |
| D220 | 26 | Total Ind AS 116 Impact | 264 | 213 | arithmetic check: 116+148=264 ✓; 100+113=213 ✓ |
| D221 | 26 | Payment of Lease Liabilities | (190) | (140) | DUPLICATE_KPI (=D119) |
| D222 | 26 | Net Impact on P&L | 75 | 73 | ARITHMETIC_VARIANCE — Q1FY26: 213−140=73 ✓ ties exactly; Q1FY27: 264−190=74, but slide states 75 (off by ₹1 Cr). MINOR_VARIANCE per p34 rounding disclaimer, but flagged for A3 given it sits directly beside an exact-tying prior-period column |

### Page 27 — Section divider "Glossary" (1)
| ID | Pg | Label | Value | Flags |
|---|---|---|---|---|
| D223 | 27 | Divider page — illustration + word "Glossary" only; OCR (incl. --psm 6 rerun) returned zero clean text | — no numeric content | NO_NUMERIC_CONTENT |

### Page 28 — Glossary (1/6) (2) — footer "27 |"
| ID | Pg | Label | Value | Flags |
|---|---|---|---|---|
| D224 | 28 | Glossary defs: AUM, Rent Paying Area, LOI Signed, Rent Yielding Area, Occupancy (5 terms) | — no numeric content | NO_NUMERIC_CONTENT |
| D225 | 28 | LOI Signed definitional timeframe: "expected to become operational in next 12 to 18 months" | 12-18 months | forward-looking definitional assumption |

### Page 29 — Glossary (2/6) (1) — footer "28 |"
| ID | Pg | Label | Value | Flags |
|---|---|---|---|---|
| D226 | 29 | Glossary defs: IndiQube Grow, DesignQube, IndiQare, MiQube, Eco (5 terms) | — no numeric content | NO_NUMERIC_CONTENT |

### Page 30 — Glossary (3/6) (1) — footer "29 | IGAAP Equivalent"
| ID | Pg | Label | Value | Flags |
|---|---|---|---|---|
| D227 | 30 | Glossary defs: Revenue, EBITDA, EBITDA margin (%), EPS, Recurring Revenue, One Time Revenue (6 terms) | — no numeric content | NO_NUMERIC_CONTENT |

### Page 31 — Glossary (4/6) (1) — footer "30 | IGAAP Equivalent"
| ID | Pg | Label | Value | Flags |
|---|---|---|---|---|
| D228 | 31 | Glossary defs: Net Worth, Net Debt, Other Expense, Other Income (4 terms) | — no numeric content | NO_NUMERIC_CONTENT |

### Page 32 — Glossary (5/6) (3) — footer "31 | Ind AS"
| ID | Pg | Label | Value | Flags |
|---|---|---|---|---|
| D229 | 32 | Lease Liability def: typical landlord lease span | 15-20 years | |
| D230 | 32 | Lease Liability def: non-cancellable lock-in period, average | ~38 months | DUPLICATE_KPI (=D151, p18 "38M" landlord lock-in marker) |
| D231 | 32 | Lease Liability def: lock-in as % of contractual lease term | ~20% | derived from D229/D230 relationship as described in the definition text |

### Page 33 — Glossary (6/6) (1) — footer "32 | Ind AS"
| ID | Pg | Label | Value | Flags |
|---|---|---|---|---|
| D232 | 33 | Glossary defs: ROU, Depreciation on ROU, Cash EBIT, Cash EBIT margin (%), Adjusted Cash EBIT, Adjusted Cash EBIT margin, Interest on Lease Liability (7 terms) | — no numeric content | NO_NUMERIC_CONTENT |

### Page 34 — Disclaimer (1) — footer "33 |"
| ID | Pg | Label | Value | Flags |
|---|---|---|---|---|
| D233 | 34 | Rounding disclosure: "Certain figures may reflect minor casting differences arising from the rounding of numbers... not material" | — (disclosure text, no standalone figure) | governs MINOR_VARIANCE flags at D048, D080, D158, D222 |

### Page 35 — Thank You / Contact (1)
| ID | Pg | Label | Value | Flags |
|---|---|---|---|---|
| D234 | 35 | Contact block: CFO Pawan Jain; Valorem Founder & CEO Anuj Sonpal (IR firm, not IndiQube); CIN L45400KA2015PLC133523; Tel +91-22-4903 9500 | — (identifiers) | DUPLICATE_KPI (CIN = D008); note "Founder & CEO" title belongs to Valorem Advisors (the IR agency), not to IndiQube — IndiQube's CEO is Rishi Das per p6 — annotation only, not an inconsistency in the filing |

---
## TABLE 3 — CHART FLAGS (8 rows, OCR'd pages)
Every `[CHART, page N, OCR text: ...]` tag in the extract, with its raw OCR payload and my
parsed interpretation. Cross-references to Table 2 IDs where the chart contains enumerable data.

| Pg | Raw OCR text (verbatim) | Parsed content | Table 2 refs |
|---|---|---|---|
| 2 | "©2026 INDIQUBE SPACES LIMITED EIINDIOUBE Investor Presentation Q1 FY27 Aug 2026" | Title slide, no numeric KPI | D012-D013 |
| 3 | "2 \| IndiQube's Growth Journey 2013 2015 2018 2021 2022 Jul 30, 2025 ... $15 Mn ... $30 Mn ... Listed on NSE & BSE Jun 30, 2026 ... 17 Tenants ... Cities ... 137 ... Centers ... 10.61 Mn Sq.ft AUM ..." | Growth timeline infographic — funding, listing, footprint milestones | D014-D025 |
| 4 | "3 \| Our Mission ... Our Vision ... GROW ... DESIGNQUBE ... INDIQARE ... ECO ... MIQUBE ..." | Mission/vision + 5 service-line taglines, no numeric content | D026 |
| 5 | "4\| We Are India's Integrated Managed Spaces Platform! Grow ... IndiQare ... DesignQube ... Eco ..." | Segment/business-line map, no numeric content | D027 |
| 7 | "Financial Highlights" | Section divider only | D044 |
| 14 | "Operational Highlights" | Section divider only | D126 |
| 24 | "©2026 INDIQUBE SPACES LIMITED Questions for Investors \| \ . / -" | Section divider only (trailing characters are graphic/icon artifacts) | D210 |
| 27 | "" (empty — OCR at default and --psm 6 both returned zero text) | Glossary section divider illustration, no text/numeric content at all | D223 |

---
## TABLE 4 — FOOTNOTES / FINE-PRINT DISCLAIMERS QUALIFYING HEADLINE NUMBERS
Every slide-footer definitional note or disclaimer, keyed by page.

| Pg | Footnote text (as extracted) | Qualifies |
|---|---|---|
| 8 (footer "7") | "IGAAP Equivalent" basis tag | All KPIs on p8 (D045-D051) |
| 9 (footer "8") | "Net Debt : (Gross Debt – Bank Balances other than Cash & Cash Equivalents – Cash & Cash Equivalents)" | D052-D064 |
| 10 (footer "9") | "IGAAP Equivalent" basis tag | D065-D081 |
| 11 (footer "10") | Full paragraph explaining the IGAAP-Equivalent supplementary-disclosure rationale (excludes Ind AS 116 lease-accounting impacts to show "underlying business performance") | D082-D097 |
| 12 (footer "11") | "*Depreciation on ROU and Other Income are Ind AS related non-cash and notional items \| **Other Expenses are cash based and mainly rental expenses paid to landlords." | D108-D113 |
| 13 (footer "12") | "Ind AS" basis tag (contrast with the IGAAP Equivalent basis used pp.6-12) | D114-D125 |
| 14 (footer "14") | "Area Under Management : Rent Paying Area + LOI Signed & Yet to be Rent Paying Area \| Rent Paying Area : Area for which IndiQube is paying rentals to landlords" | D127-D135 |
| 16 (footer "15") | "Rent Yielding Area : ... \| Rent Paying Area : ... \| LOI Signed : ... \| Area Under Management : ..." (4 definitions) | D136-D141 |
| 17 (footer "16") | "Occupancy % : Rent Yielding Area divided by Rent Paying Area \| Steady State Occupancy : Occupancy of mature centers that are > 12 months old" | D142-D146 |
| 18 (footer "17") | "Figures are on an average basis at a portfolio level (From Rent Commencement Date)" | D147-D155 |
| 19 (footer "18") | "% of AUM" | D156-D162 |
| 20 (footer "19") | "As on 30th June 2026" | D163-D180 |
| 25 (footer "24") | Implicit basis note within Q&A text: FY24-FY26 columns are "Audited", Q1FY27 column is "Estimated" | D211-D214 |
| 30 (footer "29") | "IGAAP Equivalent" basis tag | Glossary terms only |
| 31 (footer "30") | "IGAAP Equivalent" basis tag | Glossary terms only |
| 32 (footer "31") | "Ind AS" basis tag | Glossary terms only |
| 33 (footer "32") | "Ind AS" basis tag | Glossary terms only |
| 34 (footer "33") | Full forward-looking-statement disclaimer + rounding disclosure + Valorem Advisors independence disclaimer | D233; governs MINOR_VARIANCE flags throughout |

---
## TABLE 5 — ZERO_STANDING ITEMS (10 rows)
Every standing line item that is zero, nil, or dash in at least one presented period — enumerated
per rule, never dropped.

| ID (Table 2) | Pg | Line item | Zero in |
|---|---|---|---|
| D058 | 9 | Bank Balances other than Cash & Cash Equivalent | Q1 FY26 |
| D059 | 9 | Cash & Cash Equivalents | Q1 FY26 |
| D076 | 10 | Add: Other Income | Q1 FY26 |
| D083 | 11 | Other income — IGAAP Eq. column | Q1 FY26 |
| D085 | 11/12 | Purchases of traded goods — Ind AS Adj. column | all 3 periods (every period, both slides) |
| D086 | 11/12 | Employee benefit expense — Ind AS Adj. column | all 3 periods (every period, both slides) |
| D088 | 11 | Interest on borrowings — Ind AS Adj. column | all 3 periods |
| D089 | 11/26 | Interest on lease liabilities — IGAAP Eq. column | all 3 periods |
| D091 | 11/12 | PP&E & Intangible Asset — Ind AS Adj. column | all 3 periods (word-wrapped row, caught on re-sweep) |
| D092 | 11/12 | ROU (Right-of-use Assets) — IGAAP Eq. column | all 3 periods |

---
## TABLE 6 — MANAGEMENT GUIDANCE / FORWARD-LOOKING NUMBERS
Every forward-looking or guidance figure, flagged `MGMT_GUIDANCE` — commitments not yet reflected
in the reported quarter's financials.

| ID | Pg | Statement |
|---|---|---|
| D133 | 15 | North India expansion: 3.9 Lakh Sq.ft office supply on Noida Expressway (future supply, not yet in AUM) |
| D134 | 15 | Signed 39K sq.ft Design & Build project, Bengaluru — signed but future revenue recognition |
| D135 | 15 | Signed ₹52 Cr workspace deal, Bangalore — signed but future revenue recognition |
| — | 22 | Footnote narrative (p21/22): one-time VAS revenue "expected to remain a recurring feature of our revenue mix" going forward — a forward claim about revenue mix durability, not a hard number, still a management commitment worth tracking next quarter |
| D214 | 25 | Q1 FY27 current tax expense of ₹8.14 Cr explicitly labeled "Estimated" (not final/audited) |

---
## SUMMARY FLAG COUNTS
- ZERO_STANDING: 10 rows (Table 5)
- DUPLICATE_KPI: ~55 rows (same metric repeated verbatim across slides — expected in an investor
  deck; listed inline in Table 2, not separately tabled given volume)
- MGMT_GUIDANCE: 4 rows (Table 6, plus 1 narrative-only forward claim)
- ESTIMATE: 1 row (D214)
- OPERATING_ASSUMPTION: 5 rows (D155, D215, D216, D217, D229-D231 group)
- ARITHMETIC_VARIANCE: 2 findings (D108/D109 — EBIT Ind AS 96 vs 97 on p12; D222 — Net Impact on
  P&L 75 vs computed 74 on p26)
- MINOR_VARIANCE (rounding): 3 findings (D048/D080 — PAT Q1FY26 19 vs 18.5; D158 — sourcing mix
  sums to 98% not 100%; D222 overlaps with ARITHMETIC_VARIANCE above)
- LAYOUT_AMBIGUOUS: 4 rows (D125, D143, D144, D145 — all on OCR-adjacent or dense-overlay charts
  where pdftotext -layout could not be trusted to preserve bar/label pairing; visual PDF
  confirmation recommended before A4/A5 rely on these values)
- EXTRACTION_ARTIFACT: 1 row (D064)
- NO_NUMERIC_CONTENT: 12 rows (pure divider/mission/glossary-label slides)
- NO_PRIOR_LEDGER: deck-level (no DROPPED_SLIDE check possible this quarter)
