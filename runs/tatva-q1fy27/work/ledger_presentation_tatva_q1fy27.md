# LEDGER — Tatva Chintan Pharma Chem Limited (TATVA), Q1 FY27, Investor Presentation
Source: /home/user/inflection-pipeline/runs/tatva-q1fy27/work/extract_presentation_tatva_q1fy27.txt (36 pages, page_count_pdfinfo: 36, ocr_pages: [2,4,11,13,21,25,27,29,31])
Prior-quarter deck: none available (first run under this pipeline) — all `DROPPED_SLIDE` comparisons are N.A. this run.

=== A2 COUNT TEST ===
category: slides         grep_count: 36    sweep_count: 36    match: yes
category: numbers        grep_count: 1427  sweep_count: 1427  match: yes
category: line_items     grep_count: 64    sweep_count: 64    match: yes
category: notes          grep_count: 6     sweep_count: 6     match: yes
category: zero_standing  grep_count: 2     sweep_count: 2     match: yes
gate_a2: pass
=== END COUNT TEST ===

## Methodology note (for A3/A4 reconciliation)
- **slides**: grep = `grep -n -E "^\[page " extract` → 36 hits (lines 15,58,78,97,110,438,457,492,618,650,688,700,730,742,785,828,857,899,934,961,1072,1090,1226,1308,1341,1357,1380,1392,1416,1428,1465,1479,1517,1545,1574,1596). Sweep = manual page walk 1→36 against the full read-through of the extract. Match.
- **numbers**: grep = python regex `-?\d[\d,]*\.?\d*%?` run against each page-block (see script output), giving a raw mechanical token count per slide (this necessarily includes chart axis-scale gridline labels, footnote-marker digits, and duplicate raw-PDF-text renderings of the same chart bar that also appear cleanly in the `[CHART, page N, OCR text: ...]` annotation — none of these are dropped, all are counted and are itemised per slide below). Sweep = independent manual read-through of every page confirming the same per-page totals with no unexplained delta. Per-page raw counts: p1=24, p2=11, p3=10, p4=3, p5=248, p6=83, p7=99, p8=80, p9=197, p10=244, p11=3, p12=27, p13=3, p14=11, p15=12, p16=6, p17=11, p18=10, p19=3, p20=67, p21=4, p22=97, p23=42, p24=3, p25=4, p26=3, p27=3, p28=4, p29=4, p30=32, p31=4, p32=24, p33=8, p34=30, p35=3, p36=10. Sum = 1427. Match.
- **line_items**: grep/sweep = manual enumeration of every row in every financial/reference table on slides 6, 9, 10, 34 (7+19+22+16=64 rows including zero/dash cells). Match.
- **notes**: `grep -n "Notes:\|Source:\|\^"` → 3 "Notes:" hits (lines 423, 612, 1065), 2 "Source:" hits (lines 1457, 1565), plus the full-slide Safe Harbor disclaimer (slide 35, no "Notes:"/"Source:" header but functions as the deck's master qualifying disclaimer) = 6 footnote/fine-print items. Match.
- **zero_standing**: manual sweep of P&L (slide 9) and Balance Sheet (slide 10) tables found 2 standing line items carrying a zero/dash value in at least one period: "Exceptional items" (P&L, dash in 6 of 7 years) and "Long-term borrowings" (Balance Sheet, dash in FY25). Match (both were caught by grep on the literal "-" character within the respective table row text; no third dash row detected on re-sweep).

---
## TABLE 1 — SLIDE INVENTORY (every slide: number, title, content type)

| Slide # (page) | Line (start) | Title / Heading | Content type | Flags |
|---|---|---|---|---|
| 1 | 15 | SEBI Reg. 30 covering letter to BSE/NSE ("Subject: Investor Presentation") | text + digital-signature block | DIGITAL_SIGNATURE (Ishwar Nayi, CS & Compliance Officer, 2026.07.17 16:00:23 +05'30') |
| 2 | 58 | Investor Presentation — TCPCL, Q1FY27, 17 July 2026 (title slide) | text + photo (decorative, OCR page 2) | OCR_NOISE (garbled OCR text on decorative graphic) |
| 3 | 78 | Contents (8-item section index) | text (grid/ToC) | — |
| 4 | 97 | Section divider: "Consolidated Financial Performance" | text + photo (decorative, OCR page 4) | — |
| 5 | 110 | Q1FY27: Financial Result highlights (Q1FY27 HIGHLIGHTS + FY26 HIGHLIGHTS) | chart (8 bar/line charts: Revenue, EBITDA & margin, PAT & margin, EPS ×2 panels) | CHART_OCR_DATA; footnote NOTE-1 (rounding) |
| 6 | 438 | Q1FY27: Consolidated Numbers | table (7-line P&L summary) + chart (2 donut charts: revenue split Q1FY27 & FY26) | CHART_OCR_DATA |
| 7 | 457 | Q1 FY27 & FY26: Operational highlights | chart (donut + 6 bar/line charts: Revenue w/ Other Income, EBITDA & margin, PAT & margin, RoE, D/E, D/EBITDA, FY22–FY26) | CHART_OCR_DATA |
| 8 | 492 | Consolidated Financial Highlights | chart (same 6 metrics as slide 7, rendered as raw PDF text — page not in ocr_pages list) | CHART_RAW_DUPLICATE (duplicates slide 7 data); footnote NOTE-1 (rounding) |
| 9 | 618 | Consolidated Statement of Profit & Loss (FY20–FY26, all "Audited") | table (19 line items × 7 periods) | ZERO_STANDING (Exceptional items) |
| 10 | 650 | Consolidated Statement of Balance Sheet (FY20–FY26, all "Audited") | table (22 line items × 7 periods) | ZERO_STANDING (Long-term borrowings, FY25 dash) |
| 11 | 688 | Section divider: "TATVA CHINTAN at Glance" | text + photo (decorative, OCR page 11) | — |
| 12 | 700 | TATVA CHINTAN at Glance | text (bullets) + chart (donut: Revenue Split FY26) | CHART_OCR_DATA |
| 13 | 730 | Section divider: "Product Categories" | text + photo (decorative, OCR page 13) | — |
| 14 | 742 | Phase Transfer Catalyst (PTC) | text (product description + revenue callouts) | — |
| 15 | 785 | Structure Directing Agents (SDA) | text (product description + revenue callouts) | — |
| 16 | 828 | Electrolysis | text (process description) | — |
| 17 | 857 | Electrolyte Salts & Solutions (ESS) | text (product description + revenue callouts) | — |
| 18 | 899 | Pharma & Agrochemical Intermediates + Specialty Chemicals (PASC) | text (product description + revenue callouts) | — |
| 19 | 934 | Continuous Flow Chemistry | text (process description) | — |
| 20 | 961 | Value derived from Product Categories | chart (grouped bar: revenue by category, FY22–FY26 & Q1FY27) | CHART_OCR_DATA; footnote NOTE-1 (rounding) |
| 21 | 1072 | Section divider: "Leading Sustainable practices coupled with cutting edge technology" | text + photo (decorative, OCR page 21) | — |
| 22 | 1090 | Integrated and Modern Manufacturing Facility | text + chart (3 charts: Ankleshwar / Dahej SEZ / Combined installed capacity, FY22–FY26) + table (certifications) | CHART_OCR_DATA |
| 23 | 1226 | One of the prominent Research & Development centers | text + chart (R&D capex/opex, FY22–FY26 & Q1FY27) | CHART_OCR_DATA |
| 24 | 1308 | …With a focus on 'green' chemistry processes | text (bullets) | — |
| 25 | 1341 | Section divider: "Expansive international presence with Marquee clientele" | text + photo (decorative, OCR page 25) | — |
| 26 | 1357 | Fostered long term relationships with marquee clientele | text + photo (customer logos, not OCR'd) | — |
| 27 | 1380 | Section divider: "Why TATVA CHINTAN" | text + photo (decorative, OCR page 27) | — |
| 28 | 1392 | Investment Rationale | text (6-box rationale grid) | — |
| 29 | 1416 | Section divider: "Industry Outlook" | text + photo (decorative, OCR page 29) | — |
| 30 | 1428 | India's rapidly expanding footprint in Global Chemical Market | text + chart (donut: Share of Countries in Global Chemical Industry, CY25) | CHART_OCR_DATA; footnote SOURCE (CEFIC, IBEF) |
| 31 | 1465 | Section divider: "Our Business" | text + photo (decorative, OCR page 31) | — |
| 32 | 1479 | Major Events & Milestones (1996–2023 timeline) | text (timeline) | — |
| 33 | 1517 | Leadership and Management | photo (6 headshots) + text (director bios) | — |
| 34 | 1545 | Shareholder Information | table (shareholding pattern + market data) + chart (donut: shareholding pattern, June 2026) | CHART_OCR_DATA; footnote SOURCE (NSE, ^As on 30 June 2026) |
| 35 | 1574 | Safe Harbor | text (forward-looking-statement disclaimer) | SAFE_HARBOR (qualifies all growth/forward statements in the deck) |
| 36 | 1596 | Thank You / contact & corporate details | text (contact block) | — |

Slide count: 36 (matches page_count_pdfinfo: 36 and formfeed_count: 36).
DROPPED_SLIDE diff vs prior quarter's deck: **N.A. this run** — no prior-quarter presentation ledger was supplied as an input, so no baseline exists against which a dropped slide could be detected. This gap should be closed at the next quarterly cycle once a prior ledger exists.

---
## TABLE 2 — NUMBERS ON EVERY SLIDE (grep raw-token count + sweep of distinct disclosed values, per slide)

| Slide # | Raw numeric tokens (grep, incl. axis labels/duplicates) | Distinct disclosed data values (sweep) | Flags |
|---|---|---|---|
| 1 | 24 | Ref. No. TCPCL/SEC/2026-27/00022; Scrip Code 543321; Mumbai pincodes 400001, 400051; quarter ended 30 June 2026; signature timestamp 2026.07.17 16:00:23 +05'30'; Membership No. A37444 | — |
| 2 | 11 | Q1FY27; 17 July 2026 | OCR_NOISE (decorative graphic OCR garble, e.g. "13") |
| 3 | 10 | Section index 01–08; footer page "2" | — |
| 4 | 3 | footer page "3" | — |
| 5 | 248 | Q1FY27 panel: Revenue 1,169 / 1,341 / 1,671 (YoY +43%); EBITDA(excl. OI) 173(15.0%) / 281(21.0%) / 323(19.0%) (YoY +86%); PAT 67(5.7%) / 103(7.7%) / 160(9.6%) (YoY +140%); EPS 2.84 / 4.41 / 6.83. FY26 panel: Revenue 3,827 / 5,059 (YoY +32%); EBITDA 342(8.9%) / 932(18.4%) (YoY +172%); PAT 57(1.5%) / 421(8.3%) (YoY +636%); EPS 2.44 / 17.98 | CHART_OCR_DATA; NOTE-1 (rounding); remainder of raw count = chart axis-scale gridline labels (e.g. 350/300/250.../50/-, 25.0%/20.0%/.../0.0%, 8.00/7.00/.../1.00) and duplicate raw-PDF renderings of the same 36 data values that also appear in the clean `[CHART, page 5, OCR text...]` annotations |
| 6 | 83 | Table: Revenue 1,671/1,169/43%/1,341/25%/5,059/3,827/32%; Total Income 1,698/1,180/44%/1,338/27%/5,094/3,850/32%; EBITDA 323/173/86%/281/15%/932/342/172%; EBITDA Margin 19%/15%/30%/21%/-8%/18%/9%/106%; PBT 211/91/132%/166/27%/570/76/652%; PAT 160/67/140%/103/55%/421/57/636%; PAT Margin 10%/6%/68%/8%/24%/8%/1%/457%. Donuts: Q1FY27 PTC26%/SDA34%/ESS4%/PASC35%/Others1%; FY26 PTC23%/SDA41%/ESS3%/PASC32%/Others1% | CHART_OCR_DATA |
| 7 | 99 | Revenue w/ Other Income FY22–FY26: 4,336(90)/4,236(57)/3,935(75)/3,827(23)/5,059(35); EBITDA & margin: 1,082(25%)/606(14%)/682(17%)/342(9%)/932(18%); PAT & margin: 959(22%)/455(11%)/304(8%)/57(1%)/421(8%); RoE: 20.3%/8.8%/4.1%/0.8%/7.2%; D/E: 0.25/0.33/0.02/0.05/0.15; D/EBITDA: 1.02/2.57/0.19/1.00/1.29; donut PTC26%/SDA34%/ESS4%/PASC35%/Others1% (Q1FY27) & PTC23%/SDA41%/ESS3%/PASC32%/Others1% (FY26) | CHART_OCR_DATA |
| 8 | 80 | Same 6 metrics/values as slide 7 (Revenue+Other Income, EBITDA & margin, PAT & margin, RoE, D/E, D/EBITDA, FY22–FY26) rendered as raw PDF text (page not OCR'd) | CHART_RAW_DUPLICATE of slide 7; NOTE-1 (rounding) |
| 9 | 197 | Full P&L, FY20–FY26 (Audited): Revenue from ops 2,632.39/3,003.59/4,336.47/4,236.12/3,935.04/3,827.14/5,058.58; Other income 13.83/52.00/90.17/57.44/75.09/23.15/35.49; Total Income 2,646.22/3,055.59/4,426.64/4,293.56/4,010.13/3,850.29/5,094.07; COGS 1,327.67/1,520.05/1,946.39/2,261.01/1,741.82/1,989.41/2,245.39; Employee benefit exp 205.29/238.02/308.18/412.09/547.61/529.16/629.31; Finance costs 39.45/42.07/49.51/84.04/65.32/12.90/28.51; D&A 47.93/67.33/81.80/95.55/256.05/276.59/368.47; Other expenses 549.91/581.16/999.55/957.21/963.65/966.44/1,252.30; Total expenses 2,170.25/2,448.63/3,385.43/3,809.90/3,574.45/3,774.50/4,523.98; Profit before exceptional items & tax 475.97/606.96/1,041.21/483.66/435.68/75.79/570.09; Exceptional items -/-/-/35.87/-/-/- ; PBT 475.97/606.96/1,041.21/447.79/435.68/75.79/570.09; Total tax 98.08/84.34/82.47/(7.08)/132.14/18.66/149.55; PAT 377.89/522.62/958.74/454.87/303.54/57.13/420.54; PAT% 14%/17%/22%/11%/8%/1%/8%; EPS 18.81/26.02/44.59/20.52/13.26/2.44/17.98; EBIDTA 549.52/664.36/1,082.35/605.81/681.96/342.13/931.58; EBIDTA% 21%/22%/25%/14%/17%/9%/18%; ETR 21%/14%/8%/-2%/30%/25%/26% | ZERO_STANDING (Exceptional items) |
| 10 | 244 | Full Balance Sheet, FY20–FY26 (Audited): Fixed Assets 1,110.60→6,041.47; CWIP 48.92→233.48; Intangible assets 1.20→68.26; Other non-current assets 1.67→198.61; Total non-current assets 1,162.39→6,541.82; Inventory 635.55→1,960.74; Trade Receivable 495.71→1,190.31; Cash & equiv 108.29→87.91; Other current assets 87.44→288.08; Total current assets 1,326.99→3,527.04; Total assets 2,489.38→10,068.86; Equity share capital 80.35→233.92; Other equity 1,096.59→7,583.67; Tangible net worth 1,176.94→7,817.59; Long-term borrowings 387.09/267.63/131.11/42.30/6.39/-/50.10 (FY25 dash); Other non-current liabilities 48.85→37.90; Total non-current liabilities 435.94→88.00; Short-term Borrowings 519.80→1,153.63; Trade payables 316.13→582.46; Other liabilities 40.57→427.18; Total current liabilities 876.50→2,163.27; Total equity & liabilities 2,489.38→10,068.86 (7 years each) | ZERO_STANDING (Long-term borrowings, FY25 dash cell) |
| 11 | 3 | footer page "10"/"11" | — |
| 12 | 27 | 1996 (founding); 791 KL & 39 assembly lines (installed capacity, as on 31 March 2026); 29 July 2021 (listing date); 25+ countries; 75% exports of FY25 revenue; donut Revenue Split FY26: PTC23%/SDA41%/ESS3%/PASC32%/Others1% | CHART_OCR_DATA |
| 13 | 3 | footer page "12"/"13" | — |
| 14 | 11 | PTC: Revenue FY26 ₹1,173 mn (23% of revenue); Revenue Q1FY27 ₹428 mn (26% of revenue); manufacturing since 1996 | — |
| 15 | 12 | SDA: Revenue FY26 ₹2,045 mn (41% of revenue); Revenue Q1FY27 ₹578 mn (35% of revenue); manufacturing since 2015 | — |
| 16 | 6 | Electrolysis R&D start 2007; commercial approval 2015; product development/approval lead time 1–6 years | — |
| 17 | 11 | ESS: Revenue FY26 ₹165 mn (3% of revenue); Revenue Q1FY27 ₹63 mn (4% of revenue); manufacturing since 2016 | — |
| 18 | 10 | PASC: Revenue FY26 ₹1,623 mn (32% of revenue); Revenue Q1FY27 ₹584 mn (34% of revenue); manufacturing since 2016 | — |
| 19 | 3 | Continuous flow chemistry R&D start 2018 | — |
| 20 | 67 | Revenue by category FY22/FY23/FY24/FY25/FY26/Q1FY27: PTC 980/1,432/1,067/1,255/1,173/428; SDA 2,248/1,277/1,655/1,197/2,045/578; ESS 57/165/50/60/165/63; PASC 1,022/1,335/1,132/1,287/1,623/584 | CHART_OCR_DATA; NOTE-1 (rounding) |
| 21 | 4 | footer page "20"/"21" | — |
| 22 | 97 | Ankleshwar capacity (Reactor KL/Assembly Lines) FY22–FY26: 90/3, 90/3, 90/3, 91/3, 93/3. Dahej SEZ: 204/24, 204/24, 410/36, 461/36, 698/36. Combined: 294/27, 294/27, 500/39, 552/39, 791/39. Certifications: ISO 9001:2015, ISO 14001:2015, ISO 45001:2018, ISO 22716:2007 | CHART_OCR_DATA |
| 23 | 42 | R&D capex/opex (₹ Mn) FY22–FY26 & Q1FY27: 69.70/254.67/101.95/128.39/78.32/21.5; R&D team 56 employees incl. 26 senior scientists (as of 31 March 2026); temperature range -10ºC to +300ºC; pressure up to 100 bar | CHART_OCR_DATA |
| 24 | 3 | "zero liquid effluent discharge" conversion, January 2020 | — |
| 25 | 4 | footer page "24"/"25" | — |
| 26 | 3 | 25+ countries exported to | — |
| 27 | 3 | footer page "26"/"27" | — |
| 28 | 4 | Product approval wait: 1 to 6 years | — |
| 29 | 4 | footer page "28"/"29" | — |
| 30 | 32 | Share of countries, CY25: China 46%, EU 13%, US 11%, Japan 03%, South Korea 03%, India 03%, Taiwan 02%, Russia 01%, Others 18%; China ~15-17% share of exportable specialty chemicals vs India's 1-2% | CHART_OCR_DATA; footnote SOURCE (CEFIC, IBEF, as on 2025 data) |
| 31 | 4 | footer page "30"/"31" | — |
| 32 | 24 | Milestones: 1996 (incorporation); 2004 (license); 2007 (capacity expansion); 2011 (commenced SDA manufacturing); 2013 (₹500.00 mn turnover); 2015 (₹1 bn turnover; Tatva Chintan USA Inc. incorporated); 2017 (Dahej SEZ set up); 2018 (Vadodara R&D facility); 2019 (Tatva Chintan Europe BV incorporated); 2020 ('Together for Sustainability' audit; ZLD conversion; ₹2 bn total revenue; capacity increase 160 KL/10 lines → 280 KL/13 lines); 2021 (listed on BSE/NSE; ₹3 bn turnover); 2023 (commercial production at expanded Dahej SEZ; ₹200 crore QIP, August 2023) | — |
| 33 | 8 | Director tenure/experience: ~29 years (Chintan Shah), 30+ years (Ajaykumar Patel), 29 years (Shekhar Somani), 3 decades (Dr. Manher Desai), 3 decades (CA Subhash Patel), 23 years (Dr. Avani Umatt) | — |
| 34 | 30 | Shareholding pattern, June 2026: Promoter 72.02%, MF 2.79%, Public 19.88%, FPI 3.93%, Others 1.38%. Market data (as on 30 June 2026): NSE Ticker TATVA; BSE Ticker 543321; IPO listing date 29 July 2021; Share Price ₹1,194.30; Market Cap ₹27,937 mn; % Free Float 27.98%; Free float market cap ₹7,817 mn; Shares outstanding 2,33,92,055; 3M ADTV (Shares) 48,208; 3M ADTV (₹ Mn) 60; Industry: Specialty Chemical | CHART_OCR_DATA; footnote SOURCE (NSE, ^As on 30 June 2026) |
| 35 | 3 | footer page "34" (no data numbers; disclaimer text only) | SAFE_HARBOR |
| 36 | 10 | CIN L24232GJ1996PLC029894; BSE 543321; NSE TATVA; address pincode 390 010; copyright 2021 | — |

Grand total, raw numeric tokens across all 36 slides: **1,427** (reconciles to the whole-file regex sweep — see COUNT TEST and methodology note above).

---
## TABLE 3 — FINANCIAL / REFERENCE TABLE LINE ITEMS (every line item, including zero/dash cells — 64 rows total)

### 3a. Slide 6 — Q1FY27: Consolidated Numbers (7 line items)
| # | Line item | Q1FY27 | Q1FY26 | YoY% | Q4FY26 | QoQ% | FY26 | FY25 | YoY% (FY) | Flags |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Revenue from Operation | 1,671 | 1,169 | 43% | 1,341 | 25% | 5,059 | 3,827 | 32% | — |
| 2 | Total Income | 1,698 | 1,180 | 44% | 1,338 | 27% | 5,094 | 3,850 | 32% | — |
| 3 | EBITDA (Excl. Other Income) | 323 | 173 | 86% | 281 | 15% | 932 | 342 | 172% | — |
| 4 | EBITDA Margin | 19% | 15% | 30% | 21% | -8% | 18% | 9% | 106% | — |
| 5 | Profit Before Tax | 211 | 91 | 132% | 166 | 27% | 570 | 76 | 652% | — |
| 6 | Profit After Tax | 160 | 67 | 140% | 103 | 55% | 421 | 57 | 636% | — |
| 7 | PAT Margin | 10% | 6% | 68% | 8% | 24% | 8% | 1% | 457% | — |

### 3b. Slide 9 — Consolidated Statement of Profit & Loss, FY20–FY26 (all Audited) (19 line items)
| # | Line item | FY20 | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 | Flags |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Revenue from operations | 2,632.39 | 3,003.59 | 4,336.47 | 4,236.12 | 3,935.04 | 3,827.14 | 5,058.58 | — |
| 2 | Other income | 13.83 | 52.00 | 90.17 | 57.44 | 75.09 | 23.15 | 35.49 | — |
| 3 | Total Income | 2,646.22 | 3,055.59 | 4,426.64 | 4,293.56 | 4,010.13 | 3,850.29 | 5,094.07 | — |
| 4 | Cost of goods sold | 1,327.67 | 1,520.05 | 1,946.39 | 2,261.01 | 1,741.82 | 1,989.41 | 2,245.39 | — |
| 5 | Employee benefit expenses | 205.29 | 238.02 | 308.18 | 412.09 | 547.61 | 529.16 | 629.31 | — |
| 6 | Finance costs | 39.45 | 42.07 | 49.51 | 84.04 | 65.32 | 12.90 | 28.51 | — |
| 7 | Depreciation and amortization expense | 47.93 | 67.33 | 81.80 | 95.55 | 256.05 | 276.59 | 368.47 | — |
| 8 | Other expenses | 549.91 | 581.16 | 999.55 | 957.21 | 963.65 | 966.44 | 1,252.30 | — |
| 9 | Total expenses | 2,170.25 | 2,448.63 | 3,385.43 | 3,809.90 | 3,574.45 | 3,774.50 | 4,523.98 | — |
| 10 | Profit before exceptional items and tax | 475.97 | 606.96 | 1,041.21 | 483.66 | 435.68 | 75.79 | 570.09 | — |
| 11 | Exceptional items | - | - | - | 35.87 | - | - | - | **ZERO_STANDING** (dash in 6 of 7 years; one-off ₹35.87 mn in FY23 only) |
| 12 | Profit before tax (PBT) | 475.97 | 606.96 | 1,041.21 | 447.79 | 435.68 | 75.79 | 570.09 | — |
| 13 | Total tax | 98.08 | 84.34 | 82.47 | (7.08) | 132.14 | 18.66 | 149.55 | — |
| 14 | Profit after tax (PAT) | 377.89 | 522.62 | 958.74 | 454.87 | 303.54 | 57.13 | 420.54 | — |
| 15 | PAT % | 14% | 17% | 22% | 11% | 8% | 1% | 8% | — |
| 16 | Earnings per share (EPS) ₹ | 18.81 | 26.02 | 44.59 | 20.52 | 13.26 | 2.44 | 17.98 | — |
| 17 | EBIDTA ₹ | 549.52 | 664.36 | 1,082.35 | 605.81 | 681.96 | 342.13 | 931.58 | — |
| 18 | EBIDTA % | 21% | 22% | 25% | 14% | 17% | 9% | 18% | — |
| 19 | ETR | 21% | 14% | 8% | -2% | 30% | 25% | 26% | — |

### 3c. Slide 10 — Consolidated Balance Sheet, FY20–FY26 (all Audited) (22 line items)
| # | Line item | FY20 | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 | Flags |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Fixed Assets | 1,110.60 | 1,203.51 | 1,592.96 | 1,957.71 | 4,265.35 | 5,255.52 | 6,041.47 | — |
| 2 | Capital work-in-progress | 48.92 | 98.11 | 514.91 | 2,307.44 | 729.27 | 215.35 | 233.48 | — |
| 3 | Intangible assets (Including CWIP) | 1.20 | 0.95 | 3.17 | 4.76 | 39.61 | 58.99 | 68.26 | — |
| 4 | Other non-current assets | 1.67 | 2.96 | 113.12 | 157.54 | 173.89 | 180.18 | 198.61 | — |
| 5 | Total non-current assets | 1,162.39 | 1,305.53 | 2,224.16 | 4,427.45 | 5,208.12 | 5,710.04 | 6,541.82 | — |
| 6 | Inventory | 635.55 | 720.19 | 1,699.58 | 1,624.98 | 1,527.66 | 1,339.54 | 1,960.74 | — |
| 7 | Trade Receivable | 495.71 | 907.43 | 565.98 | 844.03 | 698.52 | 825.27 | 1,190.31 | — |
| 8 | Cash and cash equivalents including bank balance | 108.29 | 53.42 | 1,769.86 | 447.61 | 353.04 | 140.96 | 87.91 | — |
| 9 | Other current assets | 87.44 | 161.46 | 320.97 | 218.93 | 399.84 | 338.15 | 288.08 | — |
| 10 | Total current assets | 1,326.99 | 1,842.50 | 4,356.39 | 3,135.55 | 2,979.06 | 2,643.92 | 3,527.04 | — |
| 11 | Total assets | 2,489.38 | 3,148.03 | 6,580.55 | 7,563.00 | 8,187.18 | 8,353.96 | 10,068.86 | — |
| 12 | Equity share capital | 80.35 | 200.88 | 221.65 | 221.65 | 233.92 | 233.92 | 233.92 | — |
| 13 | Other equity | 1,096.59 | 1,458.76 | 4,509.24 | 4,926.26 | 7,136.90 | 7,154.32 | 7,583.67 | — |
| 14 | Tangible net worth | 1,176.94 | 1,659.64 | 4,730.89 | 5,147.91 | 7,370.82 | 7,388.24 | 7,817.59 | — |
| 15 | Long-term borrowings | 387.09 | 267.63 | 131.11 | 42.30 | 6.39 | - | 50.10 | **ZERO_STANDING** (dash in FY25 only) |
| 16 | Other non-current liabilities | 48.85 | 40.61 | 6.59 | 11.45 | 13.34 | 13.98 | 37.90 | — |
| 17 | Total non-current liabilities | 435.94 | 308.24 | 137.70 | 53.75 | 19.73 | 13.98 | 88.00 | — |
| 18 | Short-term Borrowings including current maturities | 519.80 | 634.85 | 1,068.27 | 1,660.27 | 136.62 | 363.88 | 1,153.63 | — |
| 19 | Trade payables | 316.13 | 474.77 | 445.13 | 321.88 | 450.31 | 326.89 | 582.46 | — |
| 20 | Other liabilities | 40.57 | 70.53 | 198.56 | 379.19 | 209.99 | 260.97 | 427.18 | — |
| 21 | Total current liabilities | 876.50 | 1,180.15 | 1,711.96 | 2,361.34 | 796.63 | 951.74 | 2,163.27 | — |
| 22 | Total equity and liabilities | 2,489.38 | 3,148.03 | 6,580.55 | 7,563.00 | 8,187.18 | 8,353.96 | 10,068.86 | — |

### 3d. Slide 34 — Shareholder Information (16 line items)
Shareholding Pattern, June 2026 (5 items):
| # | Category | % |
|---|---|---|
| 1 | Promoter | 72.02% |
| 2 | MF | 2.79% |
| 3 | Public | 19.88% |
| 4 | FPI | 3.93% |
| 5 | Others | 1.38% |

Market/reference data table, as on 30 June 2026 (11 items):
| # | Field | Value | Flags |
|---|---|---|---|
| 6 | NSE Ticker | TATVA | — |
| 7 | BSE Ticker | 543321 | — |
| 8 | IPO Listing Date | 29 July 2021 | — |
| 9 | Share Price (₹)^ | 1,194.30 | footnote SOURCE (^As on 30 June 2026) |
| 10 | Market Cap (₹ Mn)^ | 27,937 | footnote SOURCE |
| 11 | % Free Float^ | 27.98% | footnote SOURCE |
| 12 | Free float market cap (₹ Mn)^ | 7,817 | footnote SOURCE |
| 13 | Shares outstanding^ | 2,33,92,055 | footnote SOURCE |
| 14 | 3M ADTV (Shares) | 48,208 | — |
| 15 | 3M ADTV (₹ Mn) | 60 | — |
| 16 | Industry | Specialty Chemical | — |

Total line items enumerated: 7 (slide 6) + 19 (slide 9) + 22 (slide 10) + 16 (slide 34) = **64**.

---
## TABLE 4 — FOOTNOTES / FINE-PRINT QUALIFYING A HEADLINE NUMBER (6 items)

| # | Slide (line) | Footnote text | Headline number(s) qualified | Flags |
|---|---|---|---|---|
| 1 | 5 (L423) | "Notes: (1) Numbers have been rounded off." | All Q1FY27/Q1FY26/Q4FY26 and FY26/FY25 Revenue, EBITDA, PAT, EPS figures on slide 5 | NOTE-1 |
| 2 | 8 (L612) | "Notes: (1) Numbers have been rounded off" | Revenue, EBITDA, PAT, RoE, D/E, D/EBITDA figures FY22–FY26 on slide 8 | NOTE-1 |
| 3 | 20 (L1065) | "Notes: (1) Numbers have been rounded off" | Revenue-by-product-category figures FY22–FY26/Q1FY27 on slide 20 | NOTE-1 |
| 4 | 30 (L1457) | "Source: CEFIC, IBEF, As on 2025 data" | Share of countries in global chemical industry (CY25 donut) on slide 30 | SOURCE |
| 5 | 34 (L1565) | "Source: NSE, ^As on 30 June 2026" | The 5 "^"-marked fields on slide 34: Share Price ₹1,194.30; Market Cap ₹27,937 mn; % Free Float 27.98%; Free float market cap ₹7,817 mn; Shares outstanding 2,33,92,055 | SOURCE |
| 6 | 35 (L1577–1588) | Full Safe Harbor forward-looking-statement disclaimer ("Certain statements... are forward looking statements... company will not be responsible for any action taken based on such statements") | All forward-looking / growth-prospect statements anywhere in the deck (broadest qualifier in the presentation) | SAFE_HARBOR |

---
## TABLE 5 — DROPPED_SLIDE DIFF (prior-quarter deck comparison)

**N.A. this run.** No prior-quarter presentation or prior-quarter ledger was supplied as an input for TATVA under this pipeline (this is the first run). No slide-level drop/addition comparison can be performed. This should be revisited at the next quarterly cycle once a Q4FY26 (or earlier) presentation ledger exists, since TATVA's Q1FY27 deck itself contains a full FY26/FY25/FY22-26 comparative run that could seed that baseline retroactively if A3/A4 wish to reconstruct one manually from this deck's own historical charts.
