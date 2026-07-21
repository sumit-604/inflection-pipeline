# A2 ENUMERATOR LEDGER — SOUTHWEST Q1 FY27 — Investor Presentation
Source: `extract_presentation_southwest_q1fy27.txt` (40 pages, pdfinfo page_count=40, formfeed_count=40, OCR pages [2,4,10,11,12,23,27,31,34,40])
Prior-quarter ledger: none available (first quarterly run for SOUTHWEST) → DROPPED_SLIDE check is N/A this run; baseline for next quarter.

```
=== A2 COUNT TEST ===
category: slides                grep_count: 40   sweep_count: 40   match: yes
category: slide_numbers         grep_count: 40   sweep_count: 40   match: yes
category: chart_annotations     grep_count: 8    sweep_count: 8    match: yes
category: ocr_pages             grep_count: 10   sweep_count: 10   match: yes
category: line_items (p33+35+36+38)  grep_count: 80   sweep_count: 80   match: yes
  -- sub: p33 line items        grep_count: 16   sweep_count: 16   match: yes  (raw grep "^[A-Za-z]" on lines 1031-1063 = 17, minus 1 header row = 16)
  -- sub: p35 line items        grep_count: 16   sweep_count: 16   match: yes  (raw grep "^[A-Za-z]" on lines 1074-1106 = 17, minus 1 header row = 16)
  -- sub: p36 line items        grep_count: 42   sweep_count: 42   match: yes  (label-match grep on lines 1110-1143 initially returned 45; investigated 3 excess hits = substring false positives: "Current Liabilities" matched inside "Non Current Liabilities" and "Other Current Liabilities" [+2], "Provisions" matched inside "Short term Provisions" [+1]; corrected grep = 42, reconciles exactly with manual column-by-column sweep of 22 asset-side + 20 equity/liabilities-side items)
  -- sub: p38 table line items  grep_count: 6    sweep_count: 6    match: yes
category: zero_standing         grep_count: 7    sweep_count: 7    match: yes  (dash/blank cell present in at least one period, flagged per row)
category: chart_data_points     grep_count: 110  sweep_count: 110  match: yes  (p3:8, p5:8, p17:6, p18:11, p25:25, p26:6, p32:12, p37:32, p38:2; p38 line chart itself carries 0 captured data labels, flagged DATA_GAP separately, not counted in the 110)
category: footnotes             grep_count: 7    sweep_count: 7    match: yes
category: signature_blocks      grep_count: 1    sweep_count: 1    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

---

## TABLE 1 — SLIDE ENUMERATION (all 40 slides)

| Slide | Line (start) | Title | Content type | Notes / embedded numbers | Flags |
|---|---|---|---|---|---|
| 1 | 14 | Cover letter to NSE/BSE — "Updated Investor's Presentation" | text/letter + digital signature | Date 21.07.2026; addressed to NSE (Exchange Plaza, BKC) and BSE (Scrip Code 543986); Symbol SOUTHWEST; subject line "Investor's Presentation for Q1 FY 2026-27" | — |
| 1 | 48-66 | Signature block | digital signature | Signatory: VAISHALI, Company Secretary & Compliance Officer; digitally signed; timestamp 2026.07.21 08:28:19 +05'30' | see Table 8 |
| 2 | 68 | Investor Presentation (title page) | text/title (OCR page) | "Investor Presentation, July 2026" | — |
| 3 | 80 | Snapshot | stat-card infographic (OCR-adjacent chart) | 8 stat cards — see Table 6 | footnote (Table 7 row 1) |
| 4 | 102 | Company Overview (section divider) | text (OCR page) | divider only, no data | — |
| 5 | 107 | Company Overview | text + bar chart | narrative bullets (est. 2006, 43 rigs up to 2,500m, 15 geoscientists, 165+ projects, 20 active, 3.2 Mn meters drilled, zero LTI since inception); bar chart Revenue & EBITDA Margins — see Table 6 | — |
| 6 | 142 | Journey So Far | text/timeline (7 periods: 2006-2009 … 2025-26 onwards) | embedded numbers not separately line-itemed (narrative, not a structured table): INR 1,000+ Mn CGWB contracts; INR 307 crore single order from Hindustan Zinc subsidiary; 84 Mn tons coal reserves; USD 125 Mn 11-yr copper mining contract; 35% stake Alara Resources LLC; 150+ / 50+ project counts; Rs. 166 Cr CBM extension from RIL | note: INR 307 crore (Hindustan Zinc, historical, 2024-25 period) vs INR 3,070 Mn Q1-FY27 Rajasthan order on slide 32 are numerically similar magnitude but are two different orders/periods per the text — do not conflate at A3/A4 |
| 7 | 189 | Board of Directors | text/photo | Mr. Vikas Jain (Promoter, MD & Chairman, 22 yrs exp, MBA Johnson & Wales USA); Mr. Piyush Jain (Co-Promoter & Joint MD, joined board 2009, 15 yrs exp, MSc Nottingham Trent UK + BSc IILM) | no DIN / term dates disclosed on this slide — NOT FOUND |
| 8 | 219 | Board of Directors (Independent Directors) | text/photo | 4 IDs: Rajendra Prasad Ritolia (Non-Exec Dir eff. 12-Aug-2024 per slide text, though captioned "Independent Director" — caption/body inconsistency to flag), Meenakshi Anand (ID eff. 14-Aug-2023), Shivi Sabharwal (ID eff. 14-Aug-2023), Hari Narain Singh Rajpoot (ID eff. 30-Jun-2024) | flag: DISCLOSURE_INCONSISTENCY — Ritolia captioned "Independent Director" in the heading but body text describes him as appointed "Non-Executive Director effective August 12, 2024"; no DIN disclosed for any of the 4 |
| 9 | 253 | Geographical Presence | map/graphic | States listed: Haryana, Rajasthan, UP, Assam, Jharkhand, Gujarat, MP, Chhattisgarh, Maharashtra, Odisha, Telangana, Andhra Pradesh, Karnataka, Tamil Nadu; + Oman (international) — 14 India locations + 1 international shown on map, vs "8 States" cited on slide 32 operational highlights | flag: cross-check — map shows presence markers in up to 14 states/labels but slide 32 text says "20 Operations across 8 States"; map may show all-time footprint vs slide 32's current-quarter count — reconcile at A3 |
| 10 | 288 | Awards | photo/graphic (OCR page) | ISO 9001:2015, ISO 45001:2018, ISO 14001:2015 certificates; IADC (International Association of Drilling Contractors) South Central Asia Chapter membership 2025 | OCR text garbled ("ee CERTINCANON" etc.) — low OCR confidence, flag |
| 11 | 336 | Marquee Clients | logo/graphic (OCR page) | Client logos: Hindustan Copper Ltd, Reliance Industries, Alara Resources, De Beers, Dart Energy, JSW Steel, Vedanta, Hindustan Zinc, Tata Steel, Aditya Birla, Odisha (state entity), SK Cement, Hindalco, MECL, OCPL, Kolar (Coal and Power Limited) | OCR text garbled ("path West Marquee Clients" etc.) — low OCR confidence, flag |
| 12 | 372 | Business Overview (section divider) | text (OCR page) | divider only | — |
| 13 | 377 | Our Key Verticals | text/icon grid | 8 verticals listed: CBM Exploration Services, Underground Drilling, CBM Production Services, Aquifer Mapping, Coal & Other Minerals Exploration Services, Geological & Geophysical Services, 2D/3D Seismic Exploration, Exploration using Passive Seismic Tromography | — |
| 14 | 403 | Business Segment (1 of 3) | text | CBM Exploration Services (200+ core wells, "Highest in India"), CBM Production Services (60+ production wells up to 1,200m, contract renewed, 2 imported CBM rigs deployed), Coal & Other Minerals Exploration Services (~33 lakh meters drilled) | — |
| 15 | 444 | Business Segment (2 of 3) | text | 2D/3D Seismic Exploration; Geological & Geophysical Services (team of 15 geoscientists) | — |
| 16 | 475 | Business Segment (3 of 3) | text | Aquifer Mapping; Underground Drilling (order from Hindustan Copper Ltd, 4 advanced rigs commissioned); Exploration using Passive Seismic Tomography (PST) (2 large Oil India projects completed over last 3 years) | — |
| 17 | 514 | Project and order book Details | table + bar chart + pie chart | Table: segment-wise ongoing projects (5 rows) + segment-wise order book value (6 rows incl. Total) — see Table 9; charts — see Table 6 | — |
| 18 | 548 | Infrastructure | text + bar chart | Fleet: 43 top-drive hydrostatic rigs + 2 Schramm CBM rigs; 3 digital 2D/3D seismic recording systems, ~8,000-8,500 seismic channels, 1 vibroseis unit; 4 geophysical logging units, DGPS & total stations; bar chart Total Cumulative Drilling (KM) 2017-Q1FY27 — see Table 6; footer stat line: 33 lakh meters drilled, 6.5 lakh meters geophysical logging, 515 sq km 3D seismic, 411 LKM 2D seismic | — |
| 19 | 583 | Various Projects Handled | photo/text | 8 project captions (CBM Production Drilling Sohagpur MP for Reliance; CBM Production Drilling Reliance — 100 wells completed; CBM Exploratory Drilling Satpura MP for Dart Energy; Large Diameter Kimberlite core for Rio Tinto at Bunder MP, 352m depth "largest coring done in India till date"; CBM Multi-Lateral Well x2 for Reliance; Core drilling for Chromite for Tata Steel; Seismic Project for Coal Exploration) | — |
| 20 | 603 | Operations in Oman (1 of 2) | text/graphic | Rationale narrative + 5 numbered points (Oman 2nd-largest GCC country; MDO regulatory body; employment creation; 2 JVs established; 1st JV 2018, 2nd JV 2024) | — |
| 21 | 637 | Operations in Oman (2 of 2) | text | 1st JV (Alara Resources, formed 2018, 11-yr copper mining contract USD 125 Mn awarded 2021-22, mining commenced Feb 2022, 4 rigs); 2nd JV (formed 2024, 4 partners incl. Alara, awarded Block 22-B Jan 2025, airborne survey completed, data analysis under prep) | — |
| 22 | 666 | Coal Block Acquisition (Jharkhand) | text | Block Area 2.66 sq km; Estimated Geological Reserves 84 MT; Coal Grade W-IV; DGPS survey completed; accredited prospecting agency notification; exploration activities completed; GR being finalised; production target FY2027-28 | — |
| 23 | 692 | Industry Overview (section divider) | text (OCR page) | divider only | — |
| 24 | 697 | Industry Overview | text | Global Mineral Exploration Services Market: USD 10.31 Bn (2024) → USD 10.84 Bn (2025E) → USD 18 Bn (2035E), CAGR ~5.2%; mining equipment market ~USD 6.4 Bn (2024) → ~USD 11.34 Bn (2033E), CAGR ~6.05%; qualitative sections: India's Untapped Geological Potential, South West Pinnacle's Strategic Advantage (165+ projects, 3.3 Mn meters, zero LTI), Key Industry Tailwinds, Market Outlook | source footnote (Table 7 row 2) |
| 25 | 738 | Composition of India's Metals and Mining Sector | bar chart + pie chart | Metallic/Non-metallic minerals production USD Bn FY18-FY26*; states' share of mineral production FY26 pie; text: iron ore ~289 MT FY24-25 (~70% of mineral production value); Odisha ~38% of India's mineral production value, >50% of iron ore output | charts — see Table 6; footnote (Table 7 rows 3-4) |
| 26 | 855 | Coal Momentum: Powering India's Energy Core | text + bar chart | Coal production 1,047.52 MT FY24-25 (+~5% YoY from 997.83 MT), 5-yr CAGR 7.5%; coal ~55% of energy mix, ~70% of power generation; demand ~1.5-1.8 Bn tonnes by 2030; imports down ~7.9% FY24-25; govt targets ~1,404 MT by 2027, ~1,577 MT by 2030; geological reserves 344 Bn tonnes, crossed 1 Bn tons production mark FY24-25 | chart — see Table 6; footnote (Table 7 row 5) |
| 27 | 907 | Strategic Overview (section divider) | text (OCR page) | divider only | — |
| 28 | 912 | Key Strengths | text/icon (6 numbered items) | Presence Across Various Domains, Capability of Successful Projects Deliveries, Qualification Credentials, Experienced Management Team, Client Retention, Robust Order Book | — |
| 29 | 937 | Growth Opportunities | text | 5 opportunity categories: Coal & Mineral Exploration (500+ mineral blocks up for auction), Oil & Gas Exploration (100% FDI upstream), Aquifer Mapping & Groundwater Management, Unconventional Sources of Energy (CBM/shale/geothermal), International Exploration & Mining | — |
| 30 | 969 | Strategic Overseas Investments | text | Investment A: Alara Resources Ltd (ARL) — AUD 0.5 Mn investment, participating in ARL rights issue, ARL holds 51% of Oman JV; Investment B: Al Hadeetha Mining LLC (AHML) — 17.50% share, awarded mining block, exploration started, airborne survey being awarded | — |
| 31 | 995 | Financial Highlights (section divider) | text (OCR page) | divider only | — |
| 32 | 1000 | Financial & Operational Highlights | stat cards + text bullets | Q1-FY27 stat cards (6, each with YoY delta) — see Table 6; 10 operational-highlight bullets — see notes below and Table 6 for embedded figures | — |
| 33 | 1029 | Quarterly Consolidated Income Statement | table | 16 line items × (Q1 FY27, Q1 FY26, Y-o-Y) — see Table 2 | ZERO_STANDING (1 row) |
| 34 | 1067 | Financial Overview (section divider) | text (OCR page) | divider only | — |
| 35 | 1072 | Historical Consolidated Income Statement | table | 16 line items × (FY24, FY25, FY26, Q1-FY27) — see Table 3 | ZERO_STANDING (1 row) |
| 36 | 1110 | Historical Consolidated Balance Sheet | table (2-column layout: Assets / Equity & Liabilities) | 42 line items × (FY24, FY25, FY26) — see Table 4 | ZERO_STANDING (5 rows) |
| 37 | 1145 | Consolidated Financial Performance | 6-panel chart | Revenue, EBITDA & Margins, PAT & Margins, Net Worth, Debt/Equity, ROE & ROCE — see Table 6 | flag DATA_GAP — Net Worth, Debt/Equity and ROE/ROCE panels carry only FY24-FY26, no Q1-FY27 data point (unlike the Revenue/EBITDA/PAT panels which do carry Q1-FY27) |
| 38 | 1183 | Capital Market Information | table + line chart + pie chart | Price/share data table (6 items) — see Table 5; share-price-vs-Sensex line chart (Jul-25 to Jun-26); shareholding pattern pie (Promoter 64.81% / Public 35.19%) | flag DATA_GAP — line chart has no per-point data labels captured in text/OCR layer (axis only, -40% to 100%); cannot verify absolute return values from this extract |
| 39 | 1215 | Disclaimer | text/legal | South West Pinnacle disclaimer (forward-looking-statement language) + Valorem Advisors (IR agency) disclaimer + IR contact block (Mr. Anuj Sonpal / Valorem Advisors; Mr. Dinesh Agarwal, CFO) | footnote/disclaimer (Table 7 rows 6-7) |
| 40 | 1251 | Thank You (closing slide) | text (OCR page) | closing slide only | — |

---

## TABLE 2 — LINE ITEMS: Quarterly Consolidated Income Statement (Slide 33, lines 1031-1063)

Columns: Q1 FY27 | Q1 FY26 | Y-o-Y

| # | Line item | Line | Q1 FY27 | Q1 FY26 | Y-o-Y | Flags |
|---|---|---|---|---|---|---|
| 1 | Revenue from Operations | 1033 | 617 | 402 | 53.5% | — |
| 2 | Total Expenses | 1035 | 468 | 344 | 36.0% | — |
| 3 | EBITDA | 1037 | 149 | 58 | NA | — |
| 4 | EBITDA Margins (%) | 1039 | 24.15% | 14.43% | 972 Bps | — |
| 5 | Other Income | 1041 | 4 | 11 | (63.6)% | — |
| 6 | Depreciation | 1043 | 30 | 21 | 42.9% | — |
| 7 | Finance Cost | 1045 | 17 | 20 | (15.0)% | — |
| 8 | Profit Before Share of Profit from JVs | 1047 | 106 | 28 | NA | — |
| 9 | Share of Profit/(Loss) from JVs | 1049 | 13 | 3 | NA | — |
| 10 | PBT | 1051 | 119 | 31 | NA | — |
| 11 | Tax | 1053 | 26 | 7 | NA | — |
| 12 | PAT | 1055 | 93 | 24 | NA | — |
| 13 | PAT Margins (%) | 1057 | 15.07% | 5.97% | 910 Bps | — |
| 14 | Other Comprehensive Income | 1059 | 6 | **-** | NA | ZERO_STANDING (Q1 FY26 cell is dash) |
| 15 | Total Comprehensive Income | 1061 | 99 | 24 | NA | — |
| 16 | Diluted EPS (INR) | 1063 | 3.06 | 0.79 | NA | — |

Note: 16 line items = distinct disclosure rows (grep raw hit count on lines 1031-1063 was 17, includes 1 header row "Particulars(in INR Mn) Q1 FY27 Q1 FY26 Y-o-Y" — subtract header = 16, matches manual sweep).

---

## TABLE 3 — LINE ITEMS: Historical Consolidated Income Statement (Slide 35, lines 1074-1106)

Columns: FY24 | FY25 | FY26 | Q1-FY27

| # | Line item | Line | FY24 | FY25 | FY26 | Q1-FY27 | Flags |
|---|---|---|---|---|---|---|---|
| 1 | Revenue from Operations | 1076 | 1,334 | 1,803 | 2,430 | 617 | — |
| 2 | Total Expenses | 1078 | 1,087 | 1,467 | 1,847 | 468 | — |
| 3 | EBITDA | 1080 | 247 | 336 | 583 | 149 | — |
| 4 | EBITDA Margins (%) | 1082 | 18.52% | 18.64% | 23.99% | 24.15% | — |
| 5 | Other Income | 1084 | 24 | 48 | 36 | 4 | — |
| 6 | Depreciation | 1086 | 88 | 96 | 114 | 30 | — |
| 7 | Finance Cost | 1088 | 85 | 87 | 84 | 17 | — |
| 8 | Profit Before Share of Profit from JVs | 1090 | 98 | 201 | 421 | 106 | — |
| 9 | Share of Profit/(Loss) from JVs | 1092 | 11 | 13 | 14 | 13 | — |
| 10 | PBT | 1094 | 109 | 214 | 435 | 119 | — |
| 11 | Tax | 1096 | 26 | 50 | 105 | 26 | — |
| 12 | PAT | 1098 | 83 | 164 | 330 | 93 | — |
| 13 | PAT Margins (%) | 1100 | 6.22% | 9.10% | 13.58% | 15.07% | — |
| 14 | Other Comprehensive Income | 1102 | **-** | (1) | (1) | 6 | ZERO_STANDING (FY24 cell is dash) |
| 15 | Total Comprehensive Income | 1104 | 83 | 163 | 329 | 99 | — |
| 16 | Diluted EPS (INR) | 1106 | 2.96 | 5.83 | 10.82 | 3.06 | — |

Cross-check note (for A3/A4, not interpreted here): Slide 33 Q1 FY27 column and Slide 35 Q1-FY27 column both show Revenue 617 / EBITDA 149 / PAT 93 / Diluted EPS 3.06 — internally consistent between the two tables at face value.

16 line items — matches Table 2's grep/sweep methodology (17 raw hits minus 1 header row).

---

## TABLE 4 — LINE ITEMS: Historical Consolidated Balance Sheet (Slide 36, lines 1113-1142)

Columns: FY24 | FY25 | FY26. Two sub-tables (Assets; Equity & Liabilities) presented side by side on the slide.

### 4A. ASSETS (22 items)

| # | Line item | Line | FY24 | FY25 | FY26 | Flags |
|---|---|---|---|---|---|---|
| 1 | Total Non Current Assets | 1113 | 1,003 | 970 | 1,378 | — |
| 2 | Property, plant & equipment | 1114 | 725 | 625 | 918 | — |
| 3 | Capital Work-in-progress | 1115 | **-** | 7 | 4 | ZERO_STANDING (FY24 dash) |
| 4 | Right of use assets | 1117 | 17 | 14 | 11 | — |
| 5 | Investment property | 1118 | 31 | 28 | 26 | — |
| 6 | Intangible assets under development | 1119 | 108 | 143 | 193 | — |
| 7 | Goodwill | 1120 | 1 | 1 | 1 | — |
| 8 | Financial assets (i) Investments | 1122 | 41 | 53 | 90 | — |
| 9 | Financial assets (ii) Loans | 1124 | 4 | 9 | 26 | — |
| 10 | Financial assets (iii) Other financial assets | 1126 | 71 | 57 | 86 | — |
| 11 | Other non-current assets | 1127 | 5 | 33 | 23 | — |
| 12 | Total Current Assets | 1128 | 1,346 | 1,791 | 1,943 | — |
| 13 | Inventories | 1129 | 434 | 462 | 509 | — |
| 14 | Financial assets (i) Trade Receivable | 1132 | 574 | 763 | 1,166 | — |
| 15 | Financial assets (ii) Cash and cash equivalents | 1134 | 6 | 194 | 13 | — |
| 16 | Financial assets (iii) Other bank balances | 1135 | 83 | 216 | 104 | — |
| 17 | Financial assets (iv) Loans | 1136 | **-** | **-** | (blank/NOT FOUND) | ZERO_STANDING (dash both FY24 & FY25; FY26 cell not captured — verify against source PDF image) |
| 18 | Financial assets (v) Other financial assets | 1137 | 19 | 17 | 32 | — |
| 19 | Current tax assets (net) | 1138 | 2 | 2 | 4 | — |
| 20 | Other current assets | 1139 | 159 | 137 | 115 | — |
| 21 | Assets classified as held for sale | 1141 | 69 | **-** | (blank/NOT FOUND) | ZERO_STANDING (FY25 dash; FY26 cell not present — line item appears dropped after FY24; template signal of a completed one-off disposal) |
| 22 | Total Assets | 1142 | 2,349 | 2,761 | 3,321 | — |

### 4B. EQUITY AND LIABILITIES (20 items)

| # | Line item | Line | FY24 | FY25 | FY26 | Flags |
|---|---|---|---|---|---|---|
| 1 | Shareholders Funds | 1113 | 1,215 | 1,706 | 2,035 | — |
| 2 | Share Capital | 1114 | 279 | 298 | 298 | — |
| 3 | Other Equity | 1116 | 936 | 1,408 | 1,737 | — |
| 4 | Non Controlling Interest | 1118 | **-** | **-** | (blank/NOT FOUND) | ZERO_STANDING (dash/blank all periods — template signal; company has no NCI currently but line kept as standing item, canonical case per operating rules) |
| 5 | Non Current Liabilities | 1119 | 359 | 203 | 229 | — |
| 6 | Long Term Borrowings | 1120 | 257 | 122 | 160 | — |
| 7 | Lease Liability (non-current) | 1121 | 18 | 15 | 13 | — |
| 8 | Provisions (non-current) | 1123 | 7 | 8 | 4 | — |
| 9 | Other Financial Liabilities (non-current) | 1125 | 7 | 4 | 3 | — |
| 10 | Deferred tax liabilities | 1127 | 47 | 51 | 47 | — |
| 11 | Other non-current liabilities | 1128 | 23 | 3 | 2 | — |
| 12 | Current Liabilities | 1129 | 775 | 852 | 1,057 | — |
| 13 | Short term Borrowings | 1131 | 650 | 507 | 626 | — |
| 14 | Trade Payables | 1133 | 65 | 187 | 232 | — |
| 15 | Lease Liability (current) | 1135 | 2 | 2 | 3 | — |
| 16 | Other Financial Liabilities (current) | 1136 | 29 | 54 | 60 | — |
| 17 | Other Current Liabilities | 1137 | 15 | 74 | 60 | — |
| 18 | Short term Provisions | 1138 | 14 | 15 | 20 | — |
| 19 | Current Tax Liability (Net) | 1140 | **-** | 13 | 56 | ZERO_STANDING (FY24 dash) |
| 20 | Total Equity & Liabilities | 1142 | 2,349 | 2,761 | 3,321 | — |

42 total line items (22 assets + 20 equity/liabilities). Grep methodology and reconciliation documented in the COUNT TEST header.

---

## TABLE 5 — LINE ITEMS: Capital Market Information table (Slide 38, lines 1199-1210)

| # | Line item | Line | Value | Flags |
|---|---|---|---|---|
| 1 | Face Value (INR) | 1200 | 10.00 | — |
| 2 | CMP (INR) | 1202 | 216.30 | — |
| 3 | 52 Week H/L (INR) | 1204 | 287.95/120.55 | — |
| 4 | Market Cap (INR Mn) | 1206 | 6,452.23 | — |
| 5 | No. of Share outstanding (Mn) | 1208 | 29.83 | — |
| 6 | 1 Year Avg. Trading Volume ('000) | 1210 | 249.02 | — |

All "as on 30th June 2026". No zero/dash cells on this table.

---

## TABLE 6 — CHART DATA LABELS (all chart/infographic slides), 110 individual data points

| Slide | Line | Chart | Data points | Count | Flags |
|---|---|---|---|---|---|
| 3 | 100 | Snapshot stat cards | 33+ Lakhs Mtrs Drilled \| 165+ Successful Project Deliveries \| 20 Ongoing Project \| 19+ Years of Experiences \| INR 7,613 Mn Robust Order Book \| 54% 3 Year PAT CAGR \| 23% ROCE \| 0.39 Debt/Equity | 8 | footnote qualifies Order Book figure (as of 30-Jun-2026) |
| 5 | 140 | Bar chart 'Operating Revenue(INR Mn) & EBITDA Margins (%)' | Revenue: FY24 1,334 \| FY25 1,803 \| FY26 2,430 \| Q1-FY27 617; EBITDA Margin: FY24 18.52% \| FY25 18.64% \| FY26 23.99% \| Q1-FY27 24.15% | 8 | — |
| 17 | 546 | Bar 'Order book (INR Mn)' + Pie 'Q1-FY27 Order book: Type (%)' | Bar: FY24 2,157 \| FY25 3,287 \| FY26 5,812 \| Q1-FY27 7,613; Pie: Government 23% \| Private 77% | 6 | — |
| 18 | 581 | Bar 'Total Cumulative Drilling (KM)' | 2017 796 \| 2018 1,050 \| 2019 1,400 \| 2020 1,850 \| 2021 2,000 \| 2022 2,130 \| 2023 2,280 \| 2024 2,600 \| 2025 2,800 \| 2026 3,200 \| Q1-FY27 3,300 | 11 | — |
| 25 | 853 | Bar 'Production of metallic/non-metallic minerals (USD Bn)' + Pie 'Share of states FY26' | Metallic: FY18 6.96 \| FY19 8.42 \| FY20 8.96 \| FY21 9.47 \| FY22 12.76 \| FY23 14.69 \| FY24 15.03 \| FY25 16.02 \| FY26* 8.22 (9 pts); Non-metallic: FY18 1.16 \| FY19 1.21 \| FY20 1.25 \| FY21 1.28 \| FY22 1.39 \| FY23 1.47 \| FY24 1.57 \| FY25 1.5 \| FY26* 0.79 (9 pts); Pie: Odisha 38% \| Chhattisgarh 10% \| Rajasthan 6% \| Karnataka 5% \| Jharkhand 4% \| Maharashtra (%unlabeled) \| Others (%unlabeled) (7 pts) | 25 | flags: axis pairing of metallic/non-metallic series is "approximate per OCR/text-layer read" per A1 annotation — verify against source image; 2 of 7 pie slices (Maharashtra, Others) carry no numeric label in extracted text — DATA_GAP; FY26* is a stub year (through Sep-2025 only per footnote) |
| 26 | 905 | Bar 'Coal Production (million tonnes)', 5-yr CAGR 7.5% | FY20 716.1 \| FY21 730.9 \| FY22 778.2 \| FY23 893.2 \| FY24 997.8 \| FY25 1,047.5 | 6 | — |
| 32 | n/a (1009-1016) | Q1-FY27 stat cards (Financial & Operational Highlights) | Operational Revenue INR 617 Mn (+53.5% YoY) \| EBITDA INR 149 Mn (+156.9% YoY) \| EBITDA Margin 24.15% (+972 Bps YoY) \| PAT INR 93 Mn (+287.5% YoY) \| PAT Margin 15.07% (+910 Bps YoY) \| Diluted EPS INR 3.06/Share (+287.3% YoY) | 12 | cross-check: all 6 headline values and 5 of 6 YoY deltas reconcile arithmetically against Table 2 (Slide 33) Q1FY27/Q1FY26/YoY columns — flag for A5 arithmetic-consistency pass to formally verify EBITDA Margin Bps (972) and PAT Margin Bps (910) deltas |
| 37 | 1181 | 6-panel: Revenue, EBITDA & Margin, PAT & Margin, Net Worth, Debt/Equity, ROE & ROCE | Revenue: FY24 1,334\|FY25 1,803\|FY26 2,430\|Q1-FY27 617 (4); EBITDA/Margin: FY24 247/18.52%\|FY25 336/18.64%\|FY26 583/23.99%\|Q1-FY27 149/24.15% (8); PAT/Margin: FY24 83/6.22%\|FY25 164/9.10%\|FY26 330/13.58%\|Q1-FY27 93/15.07% (8); Net Worth: FY24 1,215\|FY25 1,706\|FY26 2,035 (3); D/E: FY24 0.75\|FY25 0.37\|FY26 0.39 (3); ROE&ROCE: FY24 12%/7%\|FY25 16%/10%\|FY26 23%/16% (6) | 32 | flag DATA_GAP — Net Worth, D/E, ROE/ROCE panels have no Q1-FY27 point (Revenue/EBITDA/PAT panels do); ROE/ROCE pairing flagged "approximate per axis label positions" by A1, verify against source image |
| 38 | 1213 | Line 'Share Price Data' (Company vs Sensex) + Pie 'Shareholding Pattern' | Line chart: no per-point data labels captured (monthly Jul-25 to Jun-26, axis -40% to 100%, 0 data points extracted); Pie: Promoter 64.81% \| Public 35.19% | 2 | flag DATA_GAP — share price line chart carries zero extractable data labels; absolute/indexed return values NOT FOUND in this extract |

**Total chart/stat-card data points: 110** (8+8+6+11+25+6+12+32+2). Line chart on slide 38 excluded from the 110 (0 data labels present), tracked separately as DATA_GAP.

---

## TABLE 7 — FOOTNOTES / FINE PRINT (7 items)

| # | Slide | Line | Text | Qualifies |
|---|---|---|---|---|
| 1 | 3 | 98 | "* Order Book as of 30th June 2026" | Robust Order Book INR 7,613 Mn stat card |
| 2 | 24 | 735 | "www.wiseguyreports.com, mines.gov.in, www.imarcgroup.com" | Market-size figures (USD 10.31 Bn / USD 18 Bn TAM, mining equipment market) |
| 3 | 25 | 846 | "*Until September 2025; Source: Ministry of Mines" | FY26* bar (metallic/non-metallic minerals production) — FY26* is a stub/partial year |
| 4 | 25 | 851 | "www.ibef.org" | Slide 25 statistics generally |
| 5 | 26 | 903 | "www.ibef.org" | Coal production statistics |
| 6 | 39 | 1217-1233 | South West Pinnacle disclaimer — forward-looking-statement language, no offer/inducement, no obligation to update | Entire presentation |
| 7 | 39 | 1235-1240 | Valorem Advisors (IR agency) disclaimer — prepared by Valorem based on company-provided data, liability disclaimed, Valorem staff certify no personal/company stock ownership | Entire presentation |

---

## TABLE 8 — DIGITAL SIGNATURE BLOCK (Slide 1)

| Signatory | Designation | Timestamp | Line | Flags |
|---|---|---|---|---|
| VAISHALI | Company Secretary & Compliance Officer | 2026.07.21 08:28:19 +05'30' | 63 | Letter date stated as 21.07.2026 (line 27), consistent with signature date; no board meeting time given on this cover letter (it is a presentation cover note, not a results/Board Outcome intimation) — board meeting start/end times NOT FOUND in this document (out of scope for presentation doctype; check the outcome-letter/results filing extract if enumerating that doctype separately) |

---

## TABLE 9 — Slide 17 supporting tables (Project & Order Book Details), lines 519-543

### 9A. Segment-wise ongoing projects (5 rows)

| # | Segment | Line | Number of Projects |
|---|---|---|---|
| 1 | Survey And Exploration of Mineral | 519 | 12 |
| 2 | Aquifer Mapping | 521 | 6 |
| 3 | CBM Production | 523 | 1 |
| 4 | Seismic Exploration Services using Passive Seismic Tomography | 525 | 1 |
| 5 | Total | 527 | 20 |

Cross-check: Total of 20 matches "20 Ongoing Project" stat card on Slide 3 and "20 Operations" bullet on Slide 32.

### 9B. Segment-wise order book value (INR Mn) (6 rows)

| # | Segment | Line | Value (INR Mn) |
|---|---|---|---|
| 1 | CBM Production | 532 | 2,222 |
| 2 | Aquifer Mapping | 534 | 575 |
| 3 | Seismic Exploration Services using Passive Seismic Tomography | 536 | 72 |
| 4 | Seismic & Coal Drilling | 538 | 238 |
| 5 | Survey And Exploration of Mineral | 540 | 4,506 |
| 6 | Total | 542 | 7,613 |

Cross-check: Total 7,613 matches Slide 3 stat card and Slide 17 bar-chart Q1-FY27 order book value.

---

## DROPPED_SLIDE CHECK

No prior-quarter ledger available for SOUTHWEST (first quarterly run for this ticker). DROPPED_SLIDE comparison is N/A this run. This ledger's 40-slide, title-level index (Table 1) is the baseline against which next quarter's deck should be diffed.

---

## SUMMARY OF FLAGS RAISED

- ZERO_STANDING — 7 rows (Table 2: 1; Table 3: 1; Table 4: 5)
- DATA_GAP — 4 instances (Slide 25 pie 2 unlabeled slices; Slide 37 Net Worth/D-E/ROE-ROCE panels missing Q1-FY27; Slide 38 line chart with 0 captured data labels; Slide 36 Financial assets (iv) Loans / Assets classified for sale FY26 cells not captured)
- DISCLOSURE_INCONSISTENCY — 1 instance (Slide 8: Ritolia captioned "Independent Director" but body text says "Non-Executive Director")
- Cross-check notes (not flags, for A3/A4 arithmetic-consistency pass) — 3 instances (Slide 6 vs Slide 32 order-value magnitude; Slide 9 map states vs Slide 32 "8 States"; Slide 32 stat cards vs Slide 33 table YoY reconciliation)
- Low-OCR-confidence pages — Slides 10, 11 (garbled OCR text on award certificates / client logos)
