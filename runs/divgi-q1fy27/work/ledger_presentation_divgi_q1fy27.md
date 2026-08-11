# A2 COMPLETENESS LEDGER — Investor Presentation — DIVGI — Q1FY27

Source: `runs/divgi-q1fy27/work/extract_presentation_divgi_q1fy27.txt` (1344 lines, 41 pages per A1 header: `page_count_pdfinfo: 41`, `formfeed_count: 41`)

```
=== A2 COUNT TEST ===
category: slides       grep_count: 41   sweep_count: 41   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

**Grep method:** `grep -n -E "^\[page [0-9]+\]"` on the extract file returns 41 matches (page 1 at line 39 through page 41 at line 1315), matching the A1 header's `page_count_pdfinfo: 41` and `formfeed_count: 41`.

**Manual sweep method:** Read the full extract top to bottom (lines 1-1344) and enumerated each `[page N]` marker in sequence with its slide title (Table 1 below). 41 distinct slides confirmed, numbered 1 through 41 with no gaps, no duplicates, no skips. Slides 15, 22, 32 are section dividers where A1 supplemented the text layer with an inline `[OCR page N]` confirmation line (no additional content beyond title/page number found by OCR).

**Reconciliation: grep_count (41) == sweep_count (41) == expected (41, per A1 header). GATE A2: PASS.**

Prior-quarter ledger: not available in `runs/divgi-q1fy27/work/` (no ledger file matching `*ledger*divgi*` found in `runs/`). `DROPPED_SLIDE` diffing against a prior deck could not be performed — flagged as `PRIOR_LEDGER_UNAVAILABLE`. This should be revisited once a Q4FY26 (or earlier) presentation ledger exists.

---

## TABLE 1 — SLIDE MASTER (all 41 slides)

| Slide | Title (as printed) | Content type | Line ref (start) | Disclosure units on slide | Flags |
|---|---|---|---|---|---|
| 1 | (Regulation 30 covering letter — no slide title; addressed to BSE/NSE) | text / signature block | 39 | Cover letter re "Sub: Investor Presentation"; BSE Scrip Code 543812; NSE Scrip Code DIVGIITTS; digital signature block (Aniket Kokane, CS & Compliance Officer, M No. A51571, signed 2026-08-11 18:58:11 +05'30') | SIGNATURE_BLOCK |
| 2 | "Preparing for the Next Orbit" / Divgi TorqTransfer Systems Limited — Investor Presentation – Q1 FY27 | title/cover slide | 90 | Deck title, quarter tag | — |
| 3 | Safe Harbor | text / legal disclaimer | 102 | Full forward-looking-statement safe-harbor disclaimer (applies to entire deck) | FORWARD_LOOKING (blanket disclaimer) |
| 4 | Index | table (contents) | 131 | 8 section rows w/ slide-no ranges: (1) Achieving New Quarterly Milestone p.4; (2) Entering Next Orbit of Growth p.6; (3) Growing Trend Across Key Segments p.7; (4) Highlights from Management p.8-9; (5) Financial Performance p.10-13; (6) Future Growth Strategies p.15-20; (7) About Divgi p.22-30; (8) Historical Performance p.32-39 | — |
| 5 | Achieving New Quarterly Milestone – Q1FY27 | KPI + 3 mini bar charts | 158 | Total Income, EBITDA, EBITDA Margin, PAT, PAT Margin (3-quarter trend) | QUANT_CLAIM (see Table 2) |
| 6 | Update on Project Mayflower \| US Operations | text (2-column: Plan Ahead / Q1FY27 Progress vs Q2FY27 & Beyond) | 195 | US subsidiary formation (Divgi Transmission Technologies and Systems Inc, South Carolina), customer response commentary, forward plan bullets | FORWARD_LOOKING |
| 7 | Entering the Next Orbit of Growth – FY27 & Beyond | bar chart (9 quarters, FY25-FY27) + narrative | 223 | Total Income by quarter FY25 Q1-Q4, FY26 Q1-Q4, FY27 Q1; period averages "~55crs+" / "~90crs+"; 3 yearly narrative blocks with checkmark bullets | QUANT_CLAIM, FORWARD_LOOKING (heavy — FY27 & Beyond column) |
| 8 | Growing Trend Across Key Segments | 3 bar charts (Transfer Case, E-Gear Drive, Components) | 267 | Quarterly segment revenue FY25 Q1-Q4, FY26 Q1-Q4, FY27 Q1 for each of 3 segments; period averages; 1 forward/outlook line per segment | QUANT_CLAIM, FORWARD_LOOKING |
| 9 | Highlights from Management | text (MD quote + bullets) | 309 | Jitendra Divgi (MD) quote; Q1FY27 performance highlights (Total Income ~Rs 142 Cr, EBITDA ~Rs 42 Cr, margin ~30%); 3 segmental highlight blocks (Transfer Case, Components & Exports incl. exports ~Rs 23 cr, EV Transmission) | QUANT_CLAIM |
| 10 | Highlights from Management — FY27 & Beyond | text (4 numbered guidance blocks) | 343 | Transfer Case outlook; Exports outlook (FY27 component exports target ~Rs 80 crore); EV Transmission outlook (Sigma production start Q2FY27); Components & New Transmission Opportunities (Toyota Tsusho partnership, AT/MT programmes) | FORWARD_LOOKING (all 4 blocks are guidance), QUANT_CLAIM (Rs 80 cr export target) |
| 11 | Revenue Walk – Q1FY27 | waterfall/bridge charts (5 panels) | 375 | Total Income bridge (Other Income + Revenue from Operations, Q1FY26/Q4FY26/Q1FY27); Transfer Case bridge (+93%); E-Gear Drive bridge (-20%); Components & Exports bridge (+83%, +4.8x); Other Business bridge (+229%, NexTrac/Synchro/ALH/After Market/Tooling & Other Operating Income series incl. negative values -0.5, -0.4); Geographic Mix % (Domestic/Exports, Q1FY27: 84%/16%); Total Income Mix % (Q1FY27: Transfer Case 53%, Components 24%(?), E-Gear Drive 18%(?), Others 4%(?) — see note) | QUANT_CLAIM, **CHART_LAYOUT_AMBIGUOUS** — multi-panel pdftotext -layout output (lines 380-414) interleaves 5 chart panels' numeric labels; column-to-series attribution for the "Other Business" sub-series (NexTrac/Synchro/ALH/After Market/Tooling) and the exact Total Income Mix % ordering could not be confirmed from text layer alone; flagged for visual cross-check against rendered slide before A4 uses these figures |
| 12 | Financial Snapshot – Q1FY27 | 3 bar charts + 2 margin-trend charts | 419 | Total Income (+78%), EBITDA (+92%), PAT (+189%) 3-quarter bars; EBITDA % trend (Q1FY26 24.9%, Q4FY26 24.5%, Q1FY27 29.4%); PAT % trend (Q1FY26 11.6%, Q4FY26 13.6%, Q1FY27 17.8%) | QUANT_CLAIM |
| 13 | Key Focus Areas | table (3 product revenue series) + text (Focus Areas / Update on Other Focus Areas) | 458 | Transfer Case, E-Gear Drive, Components revenue by quarter Q1FY26-Q1FY27 with Total Income Share %; Focus Areas narrative (Domestic Growth, Export Growth incl. Indonesia Pik-Up 4x4 program, production expected from CY26); Automatic Transmission update (quote submitted, PoC completion "estimated Q3 FY27"); Manual Transmission update (5-speed MT proposal submitted); Transmission for Hybrids update (OEMs assessing policy) | QUANT_CLAIM, FORWARD_LOOKING (multiple: "production expected from CY26", "estimated completion by Q3 FY27", "New products at the approval stage, expected to convert into orders soon") |
| 14 | Profit & Loss Statement | financial table | 498 | Line items: Revenue From Operations, Other Income, Total Income, Raw Materials, Gross Profit, Gross Profit Margin %, Employee Benefit Expenses, Other Expenses, EBITDA, EBITDA Margin %, Depreciation & Amortization, EBIT, Interest Expense, Profit Before Tax, Tax Expense, Profit After Tax, Profit After Tax Margin % — each across Q1FY27/Q1FY26/Y-o-Y/Q4FY26/Q-o-Q/FY26/FY25/Y-o-Y (17 line items, see Table 2a for full enumeration) | QUANT_CLAIM |
| 15 | Future Growth Strategies (section divider) | divider / OCR page | 533 | Section-divider text only: "Future Growth Strategies", page no. "14" | OCR_PAGE (A1 flag) |
| 16 | Strategic Partnership in Domestic market – Key growth catalyst | text (3 partner panels: M&M, TATA, Force Motors) | 543 | Partnership descriptions x3 (qualitative, no numeric KPI); disclaimer footnote re brand names/logos | FOOTNOTE |
| 17 | Strategic Partnership in Global market – Key growth catalyst | text (3 partner panels: BorgWarner, MAGNA, Toyota Tsusho) | 574 | Partnership descriptions x3 (qualitative); same brand/logo disclaimer footnote | FOOTNOTE |
| 18 | Progress in Our EV Transmission Business | photo (Sigma Prototype) + 6-chart NVH panel | 600 | "Approval has been received from customer for production supplies, SOP expected to commence from Q2 FY27" (forward statement); NVH Quality Report — 6 line-plot charts (D-TU/D-TD x Overall/Input Gear1/DIFF Gear1 Vibration of Order Tracking), axis ranges dB g 40-160 / RPM 1.0k-8.0k, legend numeric readouts (e.g. "110.81", "108.32") flagged by A1 as below OCR resolution and NOT machine-verifiable | FORWARD_LOOKING, **CHART_DATA_UNVERIFIABLE** (A1-carried flag — NVH legend values sub-OCR-resolution) |
| 19 | Growth Strategy | diagram (9 strategic pillars) | 614 | 4WD/AWD Products, Electric Vehicle Powertrain, Manual Transmissions and Synchronizers, Automatic Transmissions, Technology-Led Innovation, Financial Discipline, Product & Application Diversity, Manufacturing Excellence, Customer & Geographic Diversity, Collaboration — qualitative pillars, no numeric data | — |
| 20 | Near Term Growth Outlook | text (3 columns: EV Transmission* / Component Business / Core Product Portfolio) | 650 | EV Transmission ramp-up commentary (approval received, SOP "expected to start in Q2 FY27"); Component Business — export focus, "additional revenue potential of ~10 to 12 crores per month"; Core Product Portfolio — Transfer Case (US manufacturing footprint evaluation), Automatic Transmission (PoC demo), Manual Transmission (RFQ feasibility); footnote "* Domestic Business" | FORWARD_LOOKING (all 3 columns), QUANT_CLAIM (Rs 10-12 cr/month potential), FOOTNOTE |
| 21 | Long Term Growth Outlook | table (5 segments x strategy/focus/annual revenue potential) | 676 | 4-Wheel Drive System ~INR 300 Cr; Manual Transmission, Synchronizer system ~INR 300 Cr; EV Transmission ~INR 250 Cr; Automatic, Hybrid Transmission ~INR 1,000 Cr; Exports ~INR 200 Cr; total "Potential Annual Revenues of Rs. 2,000+ Crores" | FORWARD_LOOKING, QUANT_CLAIM (long-range revenue-potential guidance, not near-term) |
| 22 | About Divgi (section divider) | divider / OCR page | 716 | Section-divider text only: "About Divgi", page no. "21" | OCR_PAGE (A1 flag) |
| 23 | Company Overview | text/table (facts + Vision + Strategies + FY20 vs FY25 KPI trio) | 726 | "1964 Incorporated"; "60+ Years of experience"; "4 Manufacturing facilities"; Vision statement; Strategies list (6); Product Leadership list; Total Income* / EBITDA* / PAT* FY20 vs FY25 with % change (+7%, +4%, -3%) | QUANT_CLAIM, **FIGURE_ORDER_AMBIGUOUS** — layout (lines 739-757) places 240/171 (Total Income), 59/49 (EBITDA), 28/24 (PAT) without unambiguous FY20-vs-FY25 column alignment in the text layer; recommend visual confirmation before treating as anchored |
| 24 | Journey so far | timeline (11 year-markers, 1964-2024) | 763 | Milestones 1964, 1995, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024; quantitative: "raised Rs. 412.12 Crores through its IPO" (2023), listing on NSE/BSE March 2023 | QUANT_CLAIM (IPO proceeds Rs 412.12 Cr) |
| 25 | Manufacturing Capabilities | table (4 facilities) | 801 | Sirsi (Karnataka, 1984, Components/Synchronisers); Shivare (Maharashtra, 1991, Precision Grinding & Honing); Bhosari (Maharashtra, 1996, 4WD Transfer case); Shirwal (Maharashtra, 2023, EV Assembly/Export Components/Manual & Automatic Transmission) | — |
| 26 | Product Portfolio | applicability matrix (6 products x 5 categories) | 829 | Torque Transfer Systems, Manual Transmissions, Synchronizers, Automatic/Dual Clutch Transmissions, EV Transmission, Key Components — cross-tabbed against ICE(4WD/AWD), ICE(Manual), ICE(Automatic), Hybrid, BEV; matrix cells are graphical checkmarks, not text | **CHART_DATA_UNVERIFIABLE** (A1-carried flag — checkmark matrix; A1 provided a visual-read transcription at lines 852-858, itself unverifiable by machine, must be spot-checked) |
| 27 | Product Application | photo gallery (4 categories, representative images) | 860 | 4WD/AWD Products; Manual Transmissions and Synchronizers; Electric Vehicle Transmission; Next generation transmission products (Hybrid/Automatic) — photographs only, no embedded text data | — |
| 28 | Marquee Customers | text (6 client relationship blocks) | 879 | 6 relationship-tenure figures: 30+, 50+, 50+, 10+, 10+, 10+ years; associated product/scope descriptions per client (Transfer case components; EV transmission/Transfer Case/Synchronisers; MT Components/Transfer Cases & EV Transmissions/ALH/Nextrac; Transmission Components; Transfer Cases/Synchronisers; Engine Timing Components) | QUANT_CLAIM (tenure figures) |
| 29 | Presence Across the World | world map | 910 | Country markers: USA, Mexico, UK, Portugal, Germany, India, South Africa, Indonesia, China, Japan, Korea, Thailand; disclaimer footnote (map accuracy/political boundaries) | FOOTNOTE |
| 30 | Experienced Board Members | org chart (8 directors) | 942 | Praveen Kadle (Chairman & Independent Director); Jitendra Divgi (Managing Director); Hirendra Divgi (Executive Director); Pradip Dubhashi (Independent Director); Pundalik Dinkar Kudva (Independent Director); Geeta Tolia (Independent Director); Bharat Divgi (Non-Executive Director); Sanjay Divgi (Non-Executive Director) — 8 director rows, see Table 3 | — |
| 31 | Strong Leadership Team | org chart (9 leadership members) | 975 | Jitendra Divgi (MD); Satvinder Singh Sabharwal (Chief Growth Officer); Zubair Kachi (Mktg, Sales & ABD); Prasanna Deshpande (Engineering & Product Development); Deepak Vani (COO & Purchase); Nilesh Shukla (Mfg Engineering & Advanced Tech.); Sudhir Mirjankar (Finance); Gopal Dalvi (Human Resource); Mark John (Intl. Comm. Operations) — 9 rows, see Table 3 | — |
| 32 | Historical Performance (section divider) | divider / OCR page | 1006 | Section-divider text only: "Historical Performance", page no. "31" | OCR_PAGE (A1 flag) |
| 33 | Product Diversification – Delivered Strong Results | 3 bar charts + % of Total Income rows + narrative | 1016 | Total Income FY23-FY26 (278.7 / 273.0(?) / 240.1 / 375.2 — layout order to verify); Transfer Case FY23-FY26 w/ % of Total Income (68%/57%/46%/49%); E-Gear Drive FY23-FY26 w/ %(0%/9%/11%/8%); Components FY23-FY26 w/ %(12%/13%/21%/30%); 3 narrative outlook bullets (Indonesia project on track, strategic win secured, export recovery) | QUANT_CLAIM, FORWARD_LOOKING (3 bullets), **CHART_LAYOUT_AMBIGUOUS** (FY23-FY26 column order for the Total Income series at lines 1023-1033 should be visually confirmed) |
| 34 | Geographic Diversification – Expanding Global Presence | map + 2 charts | 1053 | Region markers (North America: US, Mexico; Europe: UK, Germany, Portugal; Asia-Pacific: Indonesia, Japan, Thailand, China, South Korea; South Africa); Products legend (Transfer Case, EV Transmission, Manual Transmission, Components); "Expanding Market Reach" list (Thailand, Indonesia, Europe, South Korea, USA, China, Mexico, Japan, South Africa); board-approved US subsidiary statement; Exports Revenue FY23-FY26 (13.55 / 3.42 / 10.80 / 66.90 INR Cr) w/ "6.2x" growth callout; Exports Share % of Total Revenue FY23-FY26 (1%/5%/6%/18%); map disclaimer footnote | QUANT_CLAIM, FOOTNOTE |
| 35 | P&L – Historical Chart | 4 bar/line charts (FY21-FY26) | 1092 | Total Income FY21-FY26 (195/242/279/273/240(?)/375); EBITDA FY21-FY26 (60/74/82/73/59(?)/92); PAT FY21-FY26 (24/40/47/51/46(?)/38 — see ambiguity note); EBITDA % FY21-FY26 (31.0/30.5/29.5/26.6/24.4/24.6); PAT % FY21-FY26 (19.6/19.1/18.4/14.6/10.2/12.5) | QUANT_CLAIM, **CHART_LAYOUT_AMBIGUOUS** (lines 1099-1125 — 6-year multi-series bar chart column order for Total Income/EBITDA/PAT absolute values needs visual cross-check; % trend rows are labeled and align more clearly with FY21-FY26 axis at lines 1116/1125) |
| 36 | Financial Ratios | 3 charts (FAT ratio, Working Capital days, Leverage/Net Debt) | 1130 | Fixed Assets Turnover Ratio (x) FY21-FY26: 1.16/1.30/1.39/0.97/0.92/0.63; Working Capital days (Inventory/Debtor/Creditor days) FY21-FY26, multiple series (values 46-99 range, see line 1140-1164 for full grid); Leverage ratios (x) FY21-FY26: 0.0/0.0/0.0/0.0/0.0/0.0 (all periods); Net Debt (Rs Cr) FY21-FY26: (117.9)/(133.1)/(262.7)/(225.1)/(243.5)/(232.6) — all negative (net cash) | QUANT_CLAIM, **ZERO_STANDING** (Leverage ratios (x) — zero in all 6 periods FY21-FY26, line 1163) |
| 37 | Capex and Cash | 2 bar charts + 2 % trend charts | 1171 | Cash Reserves & Capex FY21-FY26 (Capex: 26/40/68/78/44/27(?); Cash Reserves: 159/173/264/285/295/311(?) — see line 1180-1201, order to verify); "IPO proceeds capex – Rs. 169.66 crores of which ~Rs. 96.92* crores already deployed" (* As of 31st March 2026); RoCE % FY21-FY26 (17.8/18.3/12.5/9.3/5.6/9.9); RoIC % FY21-FY26 (32.4/33.4/25.6/11.0/4.2/12.7); footnote "# RoCE excludes Other Income" | QUANT_CLAIM, FOOTNOTE, **STALE_FOOTNOTE_DATE** — footnote "* As of 31st March 2026" appears in a Q1FY27 deck (quarter ended June 30, 2026); the deployed-capex figure is dated to the prior quarter-end, not restated to Jun-26; flag for A3/A4 to confirm whether this is a stale carryover or intentional (year-end capex deployment disclosure) |
| 38 | Historical P&L Statement | financial table (FY26-FY21) | 1211 | Same 12 line items as slide 14 (Revenue From Operations, Other Income, Total Income, Raw Materials, Gross Profit, Employee Benefit Expenses, Other Expenses, EBITDA, D&A, EBIT, Interest Expense, PBT, Tax Expense, PAT) across FY26/FY25/FY24/FY23/FY22/FY21 — see Table 2b | QUANT_CLAIM |
| 39 | Balance Sheet | financial table (Mar-26/Mar-25/Mar-24/Mar-23, two-column Assets / Equity & Liabilities layout) | 1248 | 27 line items — see Table 2c; includes 1 zero-standing line: "(i) Non-current investments" = 0.0 in all 4 periods | QUANT_CLAIM, **ZERO_STANDING** (Non-current investments, line 1263) |
| 40 | Cashflow | financial table (Mar-26/Mar-25/Mar-24/Mar-23) | 1282 | 11 line items — see Table 2d | QUANT_CLAIM |
| 41 | Contact Information | text (company + IR advisor contact block) | 1315 | Divgi TorqTransfer Systems Limited, CIN L32201MH1964PLC013085; Aniket Kokane (CS) email/phone; Strategic Growth Advisors Pvt Ltd (IR Advisor), CIN U74140MH2010PTC204285; Neha Shroff / Dhruvil Jani email/phone | — |

**Slide count reconciliation: 41 rows in Table 1 = grep_count 41 = sweep_count 41 = A1 header page_count_pdfinfo 41. GATE A2: PASS.**

---

## TABLE 2 — QUANTITATIVE CLAIMS LEDGER (cross-check targets for A3/A4 against results filing)

### 2a. Slide 14 — Profit & Loss Statement (line items, Q1FY27 focus columns)

| # | Line item | Q1FY27 | Q1FY26 | Y-o-Y | Q4FY26 | Q-o-Q | FY26 | FY25 | Y-o-Y(FY) | Line ref |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Revenue From Operations | 137.1 | 71.7 | — | 107.6 | — | 352.9 | 218.9 | — | 501 |
| 2 | Other Income | 4.6 | 5.1 | — | 6.2 | — | 22.3 | 21.2 | — | 503 |
| 3 | Total Income | 141.8 | 76.8 | 85% | 113.8 | 25% | 375.2 | 240.1 | 56% | 505 |
| 4 | Raw Materials | 53.2 | 28.5 | — | 40.7 | — | 136.8 | 88.1 | — | 507 |
| 5 | Gross Profit | 88.6 | 48.3 | 83% | 73.1 | 21% | 238.4 | 152.0 | 57% | 508 |
| 6 | Gross Profit Margin (%) | 62.5% | 62.9% | — | 64.3% | — | 63.5% | 63.3% | — | 509 |
| 7 | Employee Benefit Expenses | 13.5 | 8.3 | — | 14.3 | — | 41.5 | 25.1 | — | 511 |
| 8 | Other Expenses | 33.5 | 20.9 | — | 31.0 | — | 104.5 | 68.4 | — | 513 |
| 9 | EBITDA | 41.6 | 19.1 | 118% | 27.8 | 50% | 92.3 | 58.6 | 58% | 514 |
| 10 | EBITDA Margin (%) | 29.4% | 24.9% | — | 24.5% | — | 24.6% | 24.4% | — | 515 |
| 11 | Depreciation & Amortization | 7.8 | 6.9 | — | 7.6 | — | 29.2 | 25.2 | — | 517 |
| 12 | EBIT | 33.8 | 12.1 | — | 20.3 | — | 63.1 | 33.4 | — | 519 |
| 13 | Interest Expense | 0.1 | 0.1 | — | 0.1 | — | 0.3 | 0.4 | — | 521 |
| 14 | Profit Before Tax | 33.8 | 12.1 | — | 20.2 | — | 62.7 | 33.0 | — | 522 |
| 15 | Tax Expense | 8.5 | 3.2 | — | 4.7 | — | 15.8 | 8.6 | — | 523 |
| 16 | Profit After Tax | 25.2 | 8.9 | 183% | 15.5 | 63% | 46.9 | 24.4 | 92% | 525 |
| 17 | Profit After Tax Margin (%) | 17.8% | 11.6% | — | 13.6% | — | 12.5% | 10.2% | — | 527 |

Note: PBT of 33.8 vs EBIT 33.8 minus Interest 0.1 = 33.7, not 33.8 — a 0.1 rounding discrepancy in the deck's own arithmetic (EBIT 33.8 - Interest 0.1 = 33.7 ≠ stated PBT 33.8 for Q1FY27). Flag for A3/A4: **ARITHMETIC_ROUNDING_NOTE** (likely rounding of underlying unrounded figures; not necessarily an error, but worth a one-line footnote in A3).

### 2b. Slide 38 — Historical P&L Statement (FY26-FY21), line ref 1211-1245

| # | Line item | FY26 | FY25 | FY24 | FY23 | FY22 | FY21 | Line ref |
|---|---|---|---|---|---|---|---|---|
| 1 | Revenue From Operations | 352.9 | 218.9 | 253.4 | 271.0 | 233.8 | 186.6 | 1215 |
| 2 | Other Income | 22.3 | 21.2 | 19.6 | 7.6 | 8.1 | 8.5 | 1217 |
| 3 | Total Income | 375.2 | 240.1 | 273.0 | 278.7 | 241.9 | 195.1 | 1219 |
| 4 | Raw Materials | 136.8 | 88.1 | 106.2 | 111.4 | 93.6 | 67.0 | 1221 |
| 5 | Gross Profit | 238.4 | 152.0 | 166.8 | 167.3 | 148.2 | 128.1 | 1223 |
| 6 | Employee Benefit Expenses | 41.5 | 25.1 | 24.1 | 24.5 | 22.5 | 21.8 | 1225 |
| 7 | Other Expenses | 104.5 | 68.4 | 70.0 | 60.7 | 52.0 | 45.9 | 1227 |
| 8 | EBITDA | 92.3 | 58.6 | 72.6 | 82.1 | 73.7 | 60.4 | 1229 |
| 9 | Depreciation & Amortization | 29.2 | 25.2 | 18.7 | 13.0 | 11.4 | 7.6 | 1231 |
| 10 | EBIT | 63.1 | 33.4 | 53.9 | 69.1 | 62.3 | 52.8 | 1233 |
| 11 | Interest Expense | 0.3 | 0.4 | 0.4 | 0.3 | 0.2 | 0.2 | 1235 |
| 12 | Profit Before Tax | 62.7 | 33.0 | 53.5 | 68.8 | 62.2 | 52.6 | 1237 |
| 13 | Tax Expense | 15.8 | 8.6 | 13.8 | 17.7 | 16.0 | 14.3 | 1239 |
| 14 | Profit After Tax | 46.9 | 24.4 | 39.7 | 51.2 | 46.2 | 38.3 | 1241 |

Note: Total Income FY22 here = 241.9, but slide 23's FY20-vs-FY25 KPI trio and slide 35's chart both use overlapping FY21-FY26 windows with figures that do not always match to the decimal (e.g. slide 35 chart shows Total Income "279" for what appears to be FY23 vs this table's FY23 = 278.7 — rounding to nearest whole crore in the chart rendering, consistent). No hard contradiction found on spot check, but full reconciliation is an A4 arithmetic-consistency task, not A2's.

### 2c. Slide 39 — Balance Sheet (Mar-26/Mar-25/Mar-24/Mar-23), line ref 1248-1276

| # | Line item (Assets side) | Mar-26 | Mar-25 | Mar-24 | Mar-23 | Line ref | Flags |
|---|---|---|---|---|---|---|---|
| 1 | Property, plant and equipment | 247.1 | 243.4 | 211.7 | 111.1 | 1253 | — |
| 2 | Capital work-in-progress | 17.7 | 1.6 | 25.4 | 80.9 | 1254 | — |
| 3 | Right-of-use assets | 1.9 | 1.2 | 1.5 | 2.5 | 1255 | — |
| 4 | Intangible assets | 9.6 | 10.9 | 13.9 | 3.2 | 1256 | — |
| 5 | Intangible assets under development | 1.2 | 0.2 | 0.0 | 11.8 | 1257-1259 | — |
| 6 | (i) Non-current investments | 0.0 | 0.0 | 0.0 | 0.0 | 1263 | **ZERO_STANDING** |
| 7 | (ii) Other non-current financial assets | 1.9 | 3.9 | 3.8 | 3.7 | 1264-1266 | — |
| 8 | Other non-current assets | 1.7 | 3.8 | 5.4 | 1.0 | 1267 | — |
| 9 | Inventories | 58.8 | 38.7 | 35.7 | 31.9 | 1269 | — |
| 10 | (i) Trade receivables | 79.3 | 55.5 | 63.1 | 73.2 | 1271 | — |
| 11 | (ii) Cash and Cash Equivalents | 31.5 | 15.4 | 31.6 | 4.8 | 1272 | — |
| 12 | (iii) Bank Balances other than Cash | 263.0 | 269.4 | 232.7 | 306.6 | 1273 | — |
| 13 | (ii) Other Financial Assets | 11.4 | 13.3 | 13.5 | 4.3 | 1274 | — |
| 14 | Other Current Assets | 6.3 | 3.1 | 2.6 | 7.1 | 1275 | — |
| 15 | Total Assets | 731.4 | 660.5 | 641.4 | 642.0 | 1276 | — |

| # | Line item (Equity & Liabilities side) | Mar-26 | Mar-25 | Mar-24 | Mar-23 | Line ref | Flags |
|---|---|---|---|---|---|---|---|
| 16 | Equity Share Capital | 15.3 | 15.3 | 15.3 | 15.3 | 1253 | — |
| 17 | Other Equity | 620.2 | 581.5 | 565.1 | 536.0 | 1254 | — |
| 18 | (i) Borrowings (non-current) | 0.0 | 0.1 | 0.3 | 0.3 | 1260 | — |
| 19 | (ii) Lease Liabilities (non-current) | 0.9 | 0.4 | 0.8 | 1.5 | 1262 | — |
| 20 | Long-Term Provisions | 2.3 | 2.9 | 2.7 | 3.3 | 1264 | — |
| 21 | Deferred Tax Liabilities (net) | 3.5 | 3.7 | 2.6 | 0.4 | 1266 | — |
| 22 | (i) Borrowings (current) | 0.1 | 0.1 | 0.1 | 0.1 | 1269 | — |
| 23 | (ii) Lease Liabilities (current) | 0.8 | 0.4 | 0.4 | 0.6 | 1270 | — |
| 24 | (iii) Trade Payables | 60.1 | 40.3 | 37.6 | 46.2 | 1271 | — |
| 25 | (iv) Other Financial Liabilities | 17.7 | 8.9 | 8.9 | 27.5 | 1272 | — |
| 26 | Other Current Liabilities | 1.1 | 0.9 | 2.0 | 2.3 | 1273 | — |
| 27 | Provisions | 4.0 | 1.9 | 2.1 | 2.2 | 1274 | — |
| 28 | Current Tax Liabilities (Net) | 5.5 | 4.1 | 3.5 | 6.2 | 1275 | — |
| 29 | Total Equity & Liabilities | 731.4 | 660.5 | 641.4 | 642.0 | 1276 | — |

### 2d. Slide 40 — Cashflow (Mar-26/Mar-25/Mar-24/Mar-23), line ref 1282-1312

| # | Line item | Mar-26 | Mar-25 | Mar-24 | Mar-23 | Line ref |
|---|---|---|---|---|---|---|
| 1 | Profit Before Tax | 62.7 | 33.0 | 53.5 | 68.8 | 1286 |
| 2 | Adjustments for: Non-Cash Items / Other Investment or Financial Items | 9.7 | 5.1 | 0.0 | 6.3 | 1288 |
| 3 | Operating profit before working capital changes | 72.4 | 38.1 | 53.5 | 75.2 | 1291 |
| 4 | Changes in working capital | (16.8) | 4.0 | (6.7) | (16.9) | 1293 |
| 5 | Cash generated from Operations | 55.6 | 42.1 | 46.8 | 58.2 | 1295 |
| 6 | Direct taxes paid (net of refund) | (14.5) | (6.9) | (14.3) | (17.4) | 1297 |
| 7 | Net Cash from Operating Activities | 41.1 | 35.2 | 32.5 | 40.8 | 1299 |
| 8 | Net Cash from Investing Activities | (16.1) | (42.5) | 6.1 | (213.1) | 1301 |
| 9 | Net Cash from Financing Activities | (8.9) | (8.8) | (11.7) | 159.7 | 1303 |
| 10 | Net Decrease/Increase in Cash and Cash equivalents | 16.1 | (16.1) | 26.8 | (12.6) | 1305 |
| 11 | Cash & Cash equivalents, beginning of period | 15.4 | 31.6 | 4.8 | 17.4 | 1307 |
| 12 | Cash & Cash equivalents, end of period | 31.5 | 15.4 | 31.6 | 4.8 | 1309 |

Note (2d row 10 label): printed as "Net Decrease in Cash and Cash equivalents" but Mar-26 value (16.1) is a positive/increase against a beginning balance of 15.4 rising to 31.5 — label says "Decrease" but the sign convention in the source table is ambiguous (could be a signed decrease-basis convention where positive = decrease-of-a-negative, i.e., consistent with a cash increase). Flag **LABEL_SIGN_AMBIGUOUS** for A3/A4 to resolve against the cash flow statement in the results filing.

### 2e. Chart/KPI slides — all other quantitative claims by slide (summary; full figures already listed in Table 1 disclosure-units column)

| Slide | KPI/series | Line ref | Flags |
|---|---|---|---|
| 5 | Total Income / EBITDA / EBITDA Margin / PAT / PAT Margin, 3-quarter trend + YoY/QoQ % | 162-188 | QUANT_CLAIM |
| 7 | Total Income by quarter, FY25-FY27, 9 data points + 2 period averages | 226-236 | QUANT_CLAIM |
| 8 | Transfer Case / E-Gear Drive / Components quarterly revenue, FY25-FY27, 27 data points + 6 period averages | 273-303 | QUANT_CLAIM |
| 9 | Total Income ~Rs 142 Cr, EBITDA ~Rs 42 Cr (~30% margin), Exports ~Rs 23 cr | 319-332 | QUANT_CLAIM |
| 10 | FY27 export target ~Rs 80 crore | 356 | QUANT_CLAIM, FORWARD_LOOKING |
| 11 | Revenue-walk bridge figures (all panels) | 380-414 | QUANT_CLAIM, CHART_LAYOUT_AMBIGUOUS |
| 12 | Total Income/EBITDA/PAT 3-quarter bars + margin trend | 424-452 | QUANT_CLAIM |
| 13 | Transfer Case/E-Gear Drive/Components revenue + Total Income Share %, 5-quarter series | 463-490 | QUANT_CLAIM |
| 20 | Export revenue potential ~10-12 crores/month | 666-667 | QUANT_CLAIM, FORWARD_LOOKING |
| 21 | Segment annual revenue potential: ~300/~300/~250/~1,000/~200 INR Cr; total 2,000+ Cr | 681-711 | QUANT_CLAIM, FORWARD_LOOKING |
| 23 | Total Income/EBITDA/PAT FY20 vs FY25 + % change | 739-757 | QUANT_CLAIM, FIGURE_ORDER_AMBIGUOUS |
| 24 | IPO proceeds Rs 412.12 Crores (2023) | 790 | QUANT_CLAIM |
| 28 | Customer relationship tenure: 30+/50+/50+/10+/10+/10+ years | 886-888 | QUANT_CLAIM |
| 33 | Total Income/Transfer Case/E-Gear Drive/Components FY23-FY26 + % of Total Income | 1023-1036 | QUANT_CLAIM, CHART_LAYOUT_AMBIGUOUS |
| 34 | Exports Revenue FY23-FY26 (13.55/3.42/10.80/66.90 Cr, "6.2x"); Exports Share % (1%/5%/6%/18%) | 1085-1086 | QUANT_CLAIM |
| 35 | Total Income/EBITDA/PAT FY21-FY26 (absolute + %) | 1099-1125 | QUANT_CLAIM, CHART_LAYOUT_AMBIGUOUS |
| 36 | FAT ratio, Working Capital days (Inventory/Debtor/Creditor), Leverage ratio, Net Debt, FY21-FY26 | 1137-1163 | QUANT_CLAIM, ZERO_STANDING |
| 37 | Capex/Cash Reserves FY21-FY26; IPO capex deployed Rs 96.92 cr of Rs 169.66 cr; RoCE %/RoIC % FY21-FY26 | 1177-1205 | QUANT_CLAIM, CHART_LAYOUT_AMBIGUOUS, STALE_FOOTNOTE_DATE |

---

## TABLE 3 — DIRECTOR / LEADERSHIP ROSTER (slides 30-31)

| # | Name | Role | Slide | Line ref | Flags |
|---|---|---|---|---|---|
| 1 | Praveen Kadle | Chairman and Independent Director | 30 | 949-950, 957 | — |
| 2 | Jitendra Divgi | Managing Director | 30 | 951-952 | (also appears slide 9, 31) |
| 3 | Hirendra Divgi | Executive Director | 30 | 953-954 | — |
| 4 | Pradip Dubhashi | Independent Director | 30 | 955-956 | — |
| 5 | Pundalik Dinkar Kudva | Independent Director | 30 | 966-967 | — |
| 6 | Geeta Tolia | Independent Director | 30 | 966-967 | — |
| 7 | Bharat Divgi | Non-Executive Director | 30 | 966-967 | — |
| 8 | Sanjay Divgi | Non-Executive Director | 30 | 966-967 | — |
| 9 | Jitendra Divgi | Managing Director (repeat, leadership slide) | 31 | 990-991 | — |
| 10 | Satvinder Singh Sabharwal | Chief Growth Officer | 31 | 981-984 | — |
| 11 | Zubair Kachi | Mktg., Sales & ABD | 31 | 981-983 | — |
| 12 | Prasanna Deshpande | Engineering & Product Development | 31 | 982-985 | — |
| 13 | Deepak Vani | Chief Operating Officer & Purchase | 31 | 982-984 | — |
| 14 | Nilesh Shukla | Mfg Engineering & Advanced Tech. | 31 | 996-1000 | — |
| 15 | Sudhir Mirjankar | Finance | 31 | 997-999 | — |
| 16 | Gopal Dalvi | Human Resource | 31 | 996-998 | — |
| 17 | Mark John | Intl. Comm. Operations | 31 | 996-998 | (also plotted on world-map slide 29 as a location pin label "Mark John / Intl. Comm. Operations" at line 925-926 — likely a map-label rendering artifact, not a geography claim; note for A3) |

No DIN, term dates, or background given for any director/leadership member on this deck (investor-presentation format, not the results-filing annexure format) — this is expected for doctype=presentation and is not itself a gap to flag against the Results Filing enumeration protocol (that applies to the separate results-filing extract, not this document).

---

## TABLE 4 — FORWARD-LOOKING / GUIDANCE STATEMENTS (feeds A3 lexicon check + Questions-for-Management table)

| # | Slide | Statement (paraphrase/quote) | Line ref | Type |
|---|---|---|---|---|
| 1 | 3 | Blanket safe-harbor disclaimer covering all forward-looking statements in the deck | 103-123 | BOILERPLATE |
| 2 | 6 | "Continue assessing business case for local manufacturing in US" | 211 | FORWARD_COMMITMENT (soft) |
| 3 | 6 | "Existing customers - New RFQs: Quote submission, negotiations" / "New customers: Engage with OEMs, Tier 1s to generate RFQs" (Q2FY27 & Beyond) | 209-210 | FORWARD_PLAN |
| 4 | 7 | "Revenue growth expected to be supported by strong contract execution, including the Indonesian market opportunity in FY27, with recurring business potential" | 241-243 | GUIDANCE |
| 5 | 7 | "H2 FY27 expected to sustain the revenue momentum driven by new platforms and facelift programs with key OEM customers" | 245-246 | GUIDANCE |
| 6 | 7 | "EV business impacted in Q1... Expected to see a healthy volume trajectory from Q2 onwards for the existing programs and launch of new Sigma program in mass production" | 249-256 | GUIDANCE (with hedge on Q1 miss) |
| 7 | 7 | "Export growth expected to accelerate through entry into newer geographies and increased contribution from the components business" | 258-260 | GUIDANCE |
| 8 | 7 | "Strong export outlook from OEM customers, with plans to expand globally alongside existing OEM relationships" | 261-262 | GUIDANCE |
| 9 | 8 | "Supported by higher volumes from our OEM customers for domestic and export markets" (Transfer Case, FY27 outlook) | 278-279 | GUIDANCE |
| 10 | 8 | "Expected to ramp up to higher volumes on existing platforms, and with approvals on previously submitted prototypes for new programs in the pipeline" (E-Gear Drive) | 285-290 | GUIDANCE |
| 11 | 8 | "Improved realizations driven by a higher mix of precision components and continued growth in the export business" (Components) | 298-301 | GUIDANCE |
| 12 | 9 | MD quote: "As we move forward, we remain focused on converting the opportunities built over the past few years into sustainable and profitable growth business" | 314-315 | FORWARD_COMMITMENT (soft) |
| 13 | 10 | "Continued momentum expected from the Indonesia programme...Incremental Indonesia volumes are expected to continue for the upcoming quarters of FY27" | 349-350 | GUIDANCE |
| 14 | 10 | "H2 FY27 expected to witness a ramp-up in the domestic end market volumes with launch of new and facelift programs by key OEM customers" | 351 | GUIDANCE |
| 15 | 10 | "Exports expected to remain a key growth engine, with FY27 component exports targeted at ~Rs. 80 crore" | 356 | GUIDANCE (numeric target) |
| 16 | 10 | "North America expansion expected to strengthen engagement with global customers" | 358 | GUIDANCE |
| 17 | 10 | "Sigma production expected to commence in Q2FY27, following customer approval" | 362 | GUIDANCE (near-term, dated) |
| 18 | 10 | "Ongoing localisation and validation programmes are expected to support the transition towards commercial-scale EV transmission business" | 363 | GUIDANCE |
| 19 | 10 | "Components expected to scale further through export programmes and new customer opportunities" | 368 | GUIDANCE |
| 20 | 13 | "...production expected from CY26" (Indonesia Pik-Up 4x4 program) | 470-471 | GUIDANCE (near-term, dated) |
| 21 | 13 | "New products at the approval stage, expected to convert into orders soon" (Export, E-Gear Drive) | 487-488 | GUIDANCE (soft timing) |
| 22 | 13 | "...estimated completion by Q3 FY27" (Automatic Transmission PoC) | 472-473 | GUIDANCE (dated) |
| 23 | 13 | "OEMs assessing upcoming policy, regulations and customer needs for Hybrids to decide on investment for mass production" | 490-493 | HEDGE (contingent on OEM decision, not company commitment) |
| 24 | 18 | "SOP expected to commence from Q2 FY27" (Sigma) | 607 | GUIDANCE (near-term, dated) |
| 25 | 20 | "We expect ramp up in production with several models of one of India's preeminent EV manufacturer" | 659-661 | GUIDANCE |
| 26 | 20 | "...manufacturing/ SOP expected to start in Q2 FY27" | 665-666 | GUIDANCE (dated) |
| 27 | 20 | "...additional revenue potential of ~10 to 12 crores per month" (export parts, final production approval received) | 665-667 | GUIDANCE (numeric) |
| 28 | 20 | "Transfer Case: Globalization of our portfolio, evaluate manufacturing footprint in US market" | 659-662 | FORWARD_PLAN |
| 29 | 21 | Long-term annual revenue potential by segment (~300/~300/~250/~1,000/~200 Cr; total 2,000+ Cr) | 681-711 | LONG_RANGE_GUIDANCE (undated, multi-year "potential" framing — not a near-term commitment) |
| 30 | 33 | "Indonesia project progressing as planned, with execution remaining firmly on track" | 1040-1042 | STATUS_UPDATE (forward-adjacent) |
| 31 | 34 | "The board has approved setting up a 100% wholly owned subsidiary to strengthen presence and expand opportunities in the US Markets" | 1073-1076 | FORWARD_COMMITMENT (board-approved, factual not aspirational) |

Note on slide 6 vs slide 34: both reference a US subsidiary. Slide 6 (line 208-209) states the subsidiary is already "established" (Divgi Transmission Technologies and Systems Inc, South Carolina). Slide 34 (line 1073-1076) states "the board has approved setting up" the subsidiary — phrased prospectively. Flag **TIMING_INCONSISTENCY** for A3: one slide describes the US subsidiary as a completed step, the other as a board-approved-but-forward step. Worth a Question-for-Management item on subsidiary formation date vs board approval date.

---

## TABLE 5 — ZERO_STANDING ITEMS

| # | Line item | Slide | All-period values | Line ref | Flag |
|---|---|---|---|---|---|
| 1 | (i) Non-current investments | 39 (Balance Sheet) | 0.0 / 0.0 / 0.0 / 0.0 (Mar-26/25/24/23) | 1263 | ZERO_STANDING |
| 2 | Leverage ratios (x) | 36 (Financial Ratios) | 0.0 across all 6 periods FY21-FY26 | 1163 | ZERO_STANDING |

---

## TABLE 6 — FOOTNOTES / DISCLAIMERS

| # | Slide | Footnote text | Line ref |
|---|---|---|---|
| 1 | 3 | Full Safe Harbor / forward-looking-statement disclaimer (deck-wide) | 103-123 |
| 2 | 16 | "Disclaimer: The Brand Names and Logos mentioned are the property of their respective owners and are used here for identification purposes only" | 571 |
| 3 | 17 | Same brand/logo disclaimer, repeated | 597 |
| 4 | 20 | "* Domestic Business" (qualifies "EV Transmission*" column header) | 672 |
| 5 | 23 | "*" superscript on Total Income*/EBITDA*/PAT* (basis of the FY20-vs-FY25 figures not defined on-slide — no footnote text found qualifying the asterisk; flag **UNDEFINED_FOOTNOTE_MARKER**) | 739 |
| 6 | 29 | Map disclaimer: "This presentation and the accompanying...generalized illustration only...not intended to be used for reference purposes...does not warrant or represent any kind in connection to its accuracy or completeness" | 938-939 |
| 7 | 34 | Same map disclaimer, repeated | 1088-1089 |
| 8 | 37 | "# RoCE excludes Other Income" | 1207 |
| 9 | 37 | "* As of 31st March 2026" (qualifies the "~Rs. 96.92 crores already deployed" IPO capex figure) | 1208 |

---

## TABLE 7 — A1-CARRIED FLAGS (OCR / graphical-data notes, propagated verbatim per orchestrator instruction)

| # | Slide | A1 note | Line ref |
|---|---|---|---|
| 1 | 15 | OCR fallback used (divider slide, low character count); OCR confirms text layer already captured title + page number, no additional content | 534 |
| 2 | 18 | NVH Quality Report chart legend values below OCR resolution at source image quality — legend labels/axis ranges captured, precise numeric readouts NOT machine-verifiable | 612 |
| 3 | 22 | OCR fallback used (divider slide, low character count, low-contrast background graphic); OCR confirms text layer already captured title + page number | 717 |
| 4 | 26 | Product-applicability matrix uses graphical checkmark icons, not extractable as text; A1 provided a visual-read transcription (itself requiring independent spot-check) | 852-858 |
| 5 | 32 | OCR fallback used (divider slide, low character count); OCR confirms text layer already captured title + page number | 1007 |

Unit convention (A1 header, carried forward): all figures stated "Rs. In Crores" throughout, conversion factor x1, no conversion applied. Applies to every quantitative claim in Tables 2 and 5.

---

## TABLE 8 — DROPPED_SLIDE CHECK

Prior-quarter (Q4FY26 or earlier) presentation ledger not found in `runs/` at time of this enumeration. `DROPPED_SLIDE` comparison cannot be performed this cycle. Flag: **PRIOR_LEDGER_UNAVAILABLE** — carry to A3/A4 as a known gap, not a finding. Once a prior-quarter presentation ledger exists, re-run this comparison retroactively.

---

## SUMMARY FLAG LIST (for YAML)

FORWARD_LOOKING, QUANT_CLAIM, ZERO_STANDING, OCR_PAGE, CHART_DATA_UNVERIFIABLE, CHART_LAYOUT_AMBIGUOUS, FIGURE_ORDER_AMBIGUOUS, FOOTNOTE, STALE_FOOTNOTE_DATE, UNDEFINED_FOOTNOTE_MARKER, ARITHMETIC_ROUNDING_NOTE, LABEL_SIGN_AMBIGUOUS, TIMING_INCONSISTENCY, PRIOR_LEDGER_UNAVAILABLE, SIGNATURE_BLOCK

```yaml
stage: A2-enumerator
company: "divgi"
quarter: "q1fy27"
doctype: "presentation"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/divgi-q1fy27/work/ledger_presentation_divgi_q1fy27.md"
counts:
  slides: 41
  slide_numbers: 41
  quantitative_claim_rows: 63
  forward_looking_statements: 31
  footnotes: 9
  zero_standing: 2
  director_leadership_rows: 17
  ocr_flagged_pages: 3
flags_raised: [FORWARD_LOOKING, QUANT_CLAIM, ZERO_STANDING, OCR_PAGE, CHART_DATA_UNVERIFIABLE, CHART_LAYOUT_AMBIGUOUS, FIGURE_ORDER_AMBIGUOUS, FOOTNOTE, STALE_FOOTNOTE_DATE, UNDEFINED_FOOTNOTE_MARKER, ARITHMETIC_ROUNDING_NOTE, LABEL_SIGN_AMBIGUOUS, TIMING_INCONSISTENCY, PRIOR_LEDGER_UNAVAILABLE, SIGNATURE_BLOCK]
gate_a2: pass
mismatch_note: ""
```
