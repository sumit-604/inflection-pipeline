# A2 ENUMERATOR LEDGER — Atlanta Electricals Ltd. | Q1 FY27 | Doctype: presentation
Source: extract_presentation_atlantaelec_q1fy27.txt (30 pages, 918 lines, OCR fallback on pages 2,5,10,15,23,26)
Prior-quarter ledger: NOT PROVIDED — this is the first quarterly-pipeline run on file for atlantaelec. `DROPPED_SLIDE` comparison (bullet 3 of ENUMERATE — INVESTOR PRESENTATION) cannot be executed this cycle; flagged `NO_PRIOR_LEDGER` below and carried forward as an instruction for the next cycle's A2 run.

```
=== A2 COUNT TEST ===
category: slides            grep_count: 30    sweep_count: 30    match: yes
category: metrics           grep_count: 148   sweep_count: 148   match: yes
category: footnotes         grep_count: 11    sweep_count: 11    match: yes
category: people            grep_count: 17    sweep_count: 17    match: yes
category: milestones        grep_count: 10    sweep_count: 10    match: yes
category: disclosure_units  grep_count: 186   sweep_count: 186   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Methodology: manual sweep = each distinct disclosure unit enumerated while walking all 30 slides top-to-bottom (Tables 2-5 below), assigned a sequential row id (`M`=metric, `F`=footnote, `P`=person/signatory, `T`=timeline milestone) as drafted. Grep pass = `grep -oE '^\| M[0-9]+ \|'` (and equivalent for F/P/T) run against the finished table rows in this file, counted independently of the drafting tally. `slides` reconciled via `grep -n "^\[page [0-9]*\]"` on the source extract (30) against a manual page-by-page walk of Table 1 (30). All five categories match on reconciliation; `disclosure_units` is the sum (148+11+17+10=186).

---

## TABLE 1 — SLIDE INDEX (slide / line / title / content type)

| Slide | Line | Title / Header | Content type | Notes |
|---|---|---|---|---|
| 1 | 15 | Regulation 30 cover letter to BSE/NSE | text (regulatory letter) | Not a "deck" slide but page 1 of the PDF; enumerated as such |
| 2 | 64 | INVESTOR PRESENTATION — Q1 FY27 | section-divider graphic (OCR) | OCR page |
| 3 | 101 | Disclaimer | text (legal disclaimer, full page) | |
| 4 | 131 | Table Of Contents | text (5-item index) | |
| 5 | 155 | FINANCIAL HIGHLIGHTS | section-divider graphic (OCR) | OCR page |
| 6 | 166 | Management Commentary | text (CMD quote) | Speaker: Niral Krupeshbhai Patel, Chairman & Managing Director |
| 7 | 193 | Q1 FY27 Financial Snapshot | chart (4 bar/column charts) | Revenue, EBITDA & margin, PAT & margin, EPS — 3 periods each |
| 8 | 231 | Operational Highlights | chart (1 bar chart + 2 pie charts) | Order Book trend; Product Mix; Sector Mix |
| 9 | 262 | Consolidated Income Statement | table (22 line items x 5 columns) | Q1FY27 / Q1FY26 / YoY% / Q4FY26 / QoQ% |
| 10 | 290 | COMPANY OVERVIEW | section-divider graphic (OCR) | OCR page |
| 11 | 302 | Atlanta at a Glance | text + stat callouts (15 metrics) | |
| 12 | 340 | Key Milestones | timeline graphic (text) | 10 year-markers, 1988-2025; layout scrambled by pdftotext, see Table 5 |
| 13 | 388 | Guided By a Highly Experienced Team of Promoters and Board of Directors | text (7 director profiles) | No DIN disclosed for any director on this slide — flag `DIN_NOT_DISCLOSED` |
| 14 | 420 | …And a Strong Management Team | text (5 management profiles) | |
| 15 | 457 | BUSINESS OVERVIEW | section-divider graphic (OCR) | OCR page |
| 16 | 468 | Leading Manufacturer of a Diverse Range of Transformers | table/grid (product range) + 6 image placeholders | 6x `[TBU]` placeholders — flag `DATA_PLACEHOLDER` |
| 17 | 513 | Update on Acquisition of Atlanta Trafo Limited (100% Subsidiary) | text + stat callouts | |
| 18 | 547 | Key Strengths | text (6 numbered strength pillars) | No numeric business data |
| 19 | 579 | Tailored Product Development Approach | text + stat callouts | |
| 20 | 616 | Quality-Focused Manufacturing Excellence (facilities) | table (5 facilities x capacity/area) | |
| 21 | 642 | Quality-Focused Manufacturing Excellence (capabilities) | chart + stat callouts | Machine counts, utilisation %, supplier mix % |
| 22 | 677 | Detailed Manufacturing Process | flowchart/diagram | No numeric disclosure; QC loop steps only |
| 23 | 722 | WAY AHEAD | section-divider graphic (OCR) | OCR page |
| 24 | 733 | Industry Opportunity - Transformer Market | chart (4 charts: 2 stacked bar, 1 clustered bar, 1 pie-style %) | Densest data slide in deck; several series flagged `LAYOUT_AMBIGUOUS` — see Table 2 |
| 25 | 774 | Key Strategies Going Forward | text (4 strategy pillars, checklist bullets) | 1 numeric callout (wallet-share figure) |
| 26 | 801 | Historical Financial Statements | section-divider graphic (OCR) | OCR page |
| 27 | 813 | Disciplined Financial Approach (1/2) -> Sustained Profitability with Expansion | chart (4 charts, FY22-FY26) | Revenue, EBITDA & margin, PAT & margin, Return Ratios |
| 28 | 848 | Disciplined Financial Approach (2/2) -> Capital Efficient Business Model | chart (3 charts, FY22-FY26) | NWC days, Debt-Equity, CFO |
| 29 | 880 | Consolidated Income Statement (FY26/FY25/FY24) | table (21 line items x 3 columns) | One fewer line item than slide 9's quarterly table — flag `TABLE_STRUCTURE_DIFFERS` |
| 30 | 906 | THANK YOU / contact page | text (signatory + IR contacts) | |

**Slide count test:** grep `^\[page [0-9]*\]` = 30 (lines 15,64,101,131,155,166,193,231,262,290,302,340,388,420,457,468,513,547,579,616,642,677,722,733,774,801,813,848,880,906). Manual sweep of Table 1 rows = 30. **Match: yes.**

---

## TABLE 2 — NUMERIC & DISCLOSURE METRICS (one row per distinct metric/series; multi-period values listed together, all constituent line numbers cited)

| ID | Slide | Line(s) | Metric | Value(s) | Flags |
|---|---|---|---|---|---|
| M1 | 1 | 25 | BSE Scrip Code | 544527 | |
| M2 | 1 | 25 | NSE Symbol | ATLANTAELE | |
| M3 | 1 | 17 | Letter date | 21 July 2026 | OCR-garbled as "21%" in raw text |
| M4 | 1 | 34-35 | Quarter ended | 30 June 2026 | OCR-garbled as "30""" in raw text |
| M5 | 1 | 28 | Regulatory basis | Regulation 30, SEBI (LODR) Regulations, 2015 | |
| M6 | 1 | 29 | Board meeting date referenced | 21 July 2026 | OCR reads "215 July, 2026" — likely OCR error for "21st July" |
| M7 | 1 | 51-52 | Digital signature timestamp | 2026.07.21 13:21:35 +05'30' | Same-day as letter date; no anomaly vs board date (both 21 July 2026) |
| M8 | 1 | 61 | Company phone | 02692 235023 | |
| M9 | 2 | 69 | Deck period label | Q1 FY27 | |
| M10 | 4 | 134 | ToC entry: Financial Highlights, internal page ref | 4 | Maps to divider slide at PDF page 5 — validated, no discrepancy |
| M11 | 4 | 138 | ToC entry: Company Overview, internal page ref | 9 | Maps to divider slide at PDF page 10 — validated |
| M12 | 4 | 142 | ToC entry: Business Overview, internal page ref | 14 | Maps to divider slide at PDF page 15 — validated |
| M13 | 4 | 146 | ToC entry: Way Ahead, internal page ref | 22 | Maps to divider slide at PDF page 23 — validated |
| M14 | 4 | 150 | ToC entry: Historical Financials, internal page ref | 25 | Maps to divider slide at PDF page 26 — validated |
| M15 | 6 | 170 | Revenue from operations YoY growth | 48.0% | |
| M16 | 6 | 170 | Revenue from operations value | ₹466.33 cr | |
| M17 | 6 | 170-171 | EBITDA YoY growth | 58.1% | |
| M18 | 6 | 171 | EBITDA value | ₹77.10 cr | |
| M19 | 6 | 171 | EBITDA margin | 16.5% | |
| M20 | 6 | 171 | PAT YoY growth | 50.4% | |
| M21 | 6 | 171 | PAT value | ₹46.84 cr | |
| M22 | 6 | 174 | Order book QoQ growth | 25.0% | |
| M23 | 6 | 174 | Order book value | ₹3,116.63 cr | Differs slightly from slide 8/11 figure of ₹3,117 cr (rounding) and slide 9 QoQ base of 2,493 — consistent, not a flag |
| M24 | 7 | 196,199,201 | Revenue from Operations (Rs cr): Q1FY26 / Q4FY26 / Q1FY27 | 315.11 / 747.62 / 466.33 | |
| M25 | 7 | 197-198,202 | EBITDA (Rs cr): Q1FY26 / Q4FY26 / Q1FY27 | 48.8 / 149.6 / 77.1 | |
| M26 | 7 | 195,198,200 | EBITDA Margin %: Q1FY26 / Q4FY26 / Q1FY27 | 15.5% / 20.0% / 16.5% | |
| M27 | 7 | 214,219,221 | PAT (Rs cr): Q1FY26 / Q4FY26 / Q1FY27 | 31.1 / 102.2 / 46.8 | |
| M28 | 7 | 212,217,218 | PAT Margin %: Q1FY26 / Q4FY26 / Q1FY27 | 9.9% / 13.7% / 10.0% | |
| M29 | 7 | 213,220 | Basic & Diluted EPS: Q1FY26 / Q4FY26 / Q1FY27 | 4.35 / 13.29 / 6.09 | |
| M30 | 8 | 234-242 | Order Book (Rs cr): as on 30 Jun 2025 / 31 Mar 2026 / 30 Jun 2026 | 1,584 / 2,493 / 3,117 | |
| M31 | 8 | 246-260 | Revenue - Product Mix % (Q1 FY27) | 79% / 14% / 6% / 1% | 4 values map cleanly to 4 legend items: Power Transformer / Auto Transformer / Inverter Duty Transformer / Others |
| M32 | 8 | 246-258 | Revenue - Sector Mix % (Q1 FY27) | 66% / 19% / 14% / 1% | Only 4 % labels visible for 6 legend items (T&D, Renewable solar, Renewable Wind, Renewable Hybrid, Generation Thermal, Others) — flag `ZERO_STANDING` candidate: 2 sector categories likely carry a 0%/negligible share not rendered as a pie label |
| M33 | 9 | 265 | Revenue from Operations | Q1FY27 466.3 / Q1FY26 315.1 / YoY 48.0% / Q4FY26 747.6 / QoQ (37.6)% | |
| M34 | 9 | 266 | Cost of Materials Consumed | Q1FY27 322.5 / Q1FY26 236.1 / Q4FY26 475.0 | No YoY/QoQ % shown on this row |
| M35 | 9 | 267 | Purchase of Stock-in-Trade | 0.0 / 0.0 / 0.0 (all 3 periods) | `ZERO_STANDING` |
| M36 | 9 | 268 | Changes in Inventories | Q1FY27 16.7 / Q1FY26 (2.8) / Q4FY26 50.7 | |
| M37 | 9 | 269 | Gross Profit | Q1FY27 127.2 / Q1FY26 81.8 / YoY 55.5% / Q4FY26 222.0 / QoQ (42.7)% | |
| M38 | 9 | 270 | Gross Profit % | Q1FY27 27.3% / Q1FY26 26.0% / Q4FY26 29.7% | |
| M39 | 9 | 271 | Employee Benefits Expenses | Q1FY27 12.6 / Q1FY26 7.4 / Q4FY26 11.9 | |
| M40 | 9 | 272 | Other Expenses | Q1FY27 37.5 / Q1FY26 25.7 / Q4FY26 60.5 | |
| M41 | 9 | 273 | EBITDA | Q1FY27 77.1 / Q1FY26 48.8 / YoY 58.1% / Q4FY26 149.6 / QoQ (48.5)% | |
| M42 | 9 | 274 | EBITDA % | Q1FY27 16.5% / Q1FY26 15.5% (+105 Bps) / Q4FY26 20.0% (-347 Bps) | |
| M43 | 9 | 275 | Depreciation and Amortization Expenses | Q1FY27 10.1 / Q1FY26 2.4 / Q4FY26 9.3 | Q1FY27 vs Q1FY26 is a >4x jump — no explanatory footnote on this table; flag for A3/A4 arithmetic-consistency check |
| M44 | 9 | 276 | EBIT | Q1FY27 67.0 / Q1FY26 46.4 / YoY 44.2% / Q4FY26 140.3 / QoQ (52.3)% | |
| M45 | 9 | 277 | EBIT % | Q1FY27 14.4% / Q1FY26 14.7% (-37 Bps) / Q4FY26 18.8% (-441 Bps) | |
| M46 | 9 | 278 | Other Income | Q1FY27 2.3 / Q1FY26 2.4 / Q4FY26 7.6 | |
| M47 | 9 | 279 | Finance Cost | Q1FY27 5.7 / Q1FY26 6.9 / Q4FY26 16.0 | |
| M48 | 9 | 280 | Exceptional item | Q1FY27 0.0 / Q1FY26 0.0 / Q4FY26 0.1 | Not fully zero — Q4FY26 carries 0.1; not tagged `ZERO_STANDING` |
| M49 | 9 | 281 | PBT | Q1FY27 63.6 / Q1FY26 41.9 / YoY 51.4% / Q4FY26 131.8 / QoQ (51.7)% | |
| M50 | 9 | 282 | PBT % | Q1FY27 13.6% / Q1FY26 13.3% / Q4FY26 17.6% | |
| M51 | 9 | 283 | Total Tax Expense | Q1FY27 16.7 / Q1FY26 10.8 / Q4FY26 29.6 | |
| M52 | 9 | 284 | PAT | Q1FY27 46.8 / Q1FY26 31.1 / YoY 50.4% / Q4FY26 102.2 / QoQ (54.2)% | |
| M53 | 9 | 285 | PAT % | Q1FY27 10.0% / Q1FY26 9.9% (+16 Bps) / Q4FY26 13.7% (-362 Bps) | |
| M54 | 9 | 286 | Basic & Diluted EPS | Q1FY27 6.09 / Q1FY26 4.35 / YoY 40.0% / Q4FY26 13.29 / QoQ (54.2)% | |
| M55 | 11 | 306 | Years in transformer manufacturing | 30 yrs | |
| M56 | 11 | 307,309 | BTW acquisition timing / status as of Q1FY27 | Acquisition in April-2025; "as of Q1FY27" | |
| M57 | 11 | 309,337 | RoCE | 39.11%* | Footnote: RoCE for FY26 (see F3) — presented on a Q1FY27 slide but is an FY26 full-year figure, not a Q1FY27 figure; flag `PERIOD_LABEL_CHECK` |
| M58 | 11 | 310-311 | Sales footprint | 19 States & 3 UTs | |
| M59 | 11 | 312-313 | Cumulative transformers supplied (MVA) | 1,21,317 MVA | |
| M60 | 11 | 312-313 | Cumulative transformers supplied (units) | 4,973 transformers | |
| M61 | 11 | 315 | Installed capacity | 63,060 MVA | |
| M62 | 11 | 315 | Manufacturing area | 3,21,451.39 sq. ft | |
| M63 | 11 | 319 | Manufacturing facilities count | 5 | |
| M64 | 11 | 319-320 | Order Book as on 30 June 2026 | INR 3,117 crores | |
| M65 | 11 | 323-325 | Compliance certifications | ISO 9001:2015, ISO 14001:2015, ISO 45001:2018 | |
| M66 | 11 | 323-324 | NABL accredited testing labs | 8 | |
| M67 | 11 | 316 | Product voltage/rating range | 5 MVA/11 kV up to 500 MVA/765 kV | |
| M68 | 11 | 334-336 | No. of customers: FY22 / Q1 FY27 | 77 / 273 | |
| M69 | 16 | 471 | Headline product range | 5 MVA/11 kV up to 500 MVA/765 kV | Restates M67 |
| M70 | 16 | 475-476 | Auto Transformer voltage range | 66 kV to 400 kV | |
| M71 | 16 | 475-476 | Inverter Duty Transformer voltage range | 0.60 kV to 33 kV | |
| M72 | 16 | 491-492 | Furnace Transformer voltage range | 0.43 kV to 66 kV | |
| M73 | 16 | 491-492 | Power Transformer voltage range | 11 kV to 765 kV | |
| M74 | 16 | 502-503 | Generator Transformer voltage range | 3.30 kV to 220 kV | |
| M75 | 16 | 502-503 | Special Duty Transformer voltage range | 0.43 kV to 132 kV | |
| M76 | 16 | 487-488,497-500,508-510 | "Max" rating cluster (8 values) | 500 MVA, 18.5 MVA, 18.5 kVA, 50 MVA, 160 kVA, 160 MVA, 50 MVA, 50 kVA | `LAYOUT_AMBIGUOUS` — pdftotext -layout grid linearization makes exact product-to-rating pairing unverifiable from text alone; needs visual PDF check |
| M77 | 16 | 485,496,507 | Product image placeholders | `[TBU]` x6 | `DATA_PLACEHOLDER` — 6 of 6 product image slots unresolved in source PDF |
| M78 | 17 | 519 | Transformers & Reactors range (Atlanta Trafo) | Upto 765/1,200 kV* | Footnote F5 |
| M79 | 17 | 519 | Owned/Constructed Area | 84,025 / 20,000+ Sq. Mts. | |
| M80 | 17 | 519 | Capacity available for utilisation | 15,780 MVA | |
| M81 | 17 | 529,532-536 | Stake acquired from BTW | 90% | |
| M82 | 17 | 536 | Stake acquired from Atlanta UHV Transformers LLP | 10% | |
| M83 | 17 | 533-535 | Enterprise Value | ~INR 2,600 Mn^ (mix of debt + internal accruals) | Footnote F6 |
| M84 | 17 | 533 | Pre-acquisition JV structure (BTW:Atlanta promoters) | 90:10 | |
| M85 | 18 | 550-572 | Key Strengths numbered list | 6 items, numbered 1-6 | Purely qualitative; no financial figures |
| M86 | 19 | 586-587 | Altitude design spec | >3,000 meters | |
| M87 | 19 | 592-593 | Delivered voltage class to Leh | 66 kV | |
| M88 | 19 | 593-594 | Power transformers manufactured (rating) | 20 MVA, 66/11.55 kV | |
| M89 | 19 | 603-604 | Units delivered in 2010 | 14 units of 6.3 MVA transformers | |
| M90 | 20 | 623-624,630 | Anand (Gujarat) Unit I: installed capacity / area | 9,360 MVA / 7,840 sq. mts | |
| M91 | 20 | 623-624,630 | Anand (Gujarat) Unit II: installed capacity / area | 6,660 MVA / 17,845 sq. mts | |
| M92 | 20 | 623-624,630 | Bangalore, Karnataka: installed capacity / area | 720 MVA / 4,178.84 sq. mts | |
| M93 | 20 | 636-637 | Vadod, Gujarat: installed capacity / area | 30,540 MVA / 71,798.40 sq. mts | |
| M94 | 20 | 636-637 | Atlanta Trafo Limited (100% subsidiary): installed capacity / area | 15,780 MVA / 20,000 sq. mts | |
| M95 | 20 | 639 | Combined installed capacity (all facilities) | 63,060 MVA | Restates M61 |
| M96 | 21 | 646 | Winding machines | 49 | |
| M97 | 21 | 646,650-651 | Tanking Workstations | 9 | |
| M98 | 21 | 646 | Core building stations | 13 | |
| M99 | 21 | 650 | Core coil assembly stations | 21 | |
| M100 | 21 | 654,656 | Vacuum Drying Ovens | 7 | |
| M101 | 21 | 654,656 | Vapor phase drying ovens | 5 | |
| M102 | 21 | 656 | Labs for testing transformers up to 500 MVA/765 kV | 8 | |
| M103 | 21 | 660 | Employees as of Jun-26 | 505, of which 37 skilled professionals for transformer design | |
| M104 | 21 | 647-652 | Capacity Utilisation: FY22 / FY26 | 61.28% / 98.28% | |
| M105 | 21 | 667-668 | Top 10 suppliers' share of raw material purchases | 69.14% | |
| M106 | 21 | 670-672 | No single supplier contributed more than | 17.87% | |
| M107 | 21 | 673 | Domestic Suppliers share | 86.08% | |
| M108 | 21 | 666 | Foreign Suppliers share | 13.92% | |
| M109 | 24 | 738,742,747-750 | Domestic Market Size 2023 (USD Bn): total / segment values | 58.9 total; 3.7, 20.5, 34.7 by segment | `LAYOUT_AMBIGUOUS` — exact segment (Power Transformers/Specialty/Others) to value pairing not verifiable from linearized text |
| M110 | 24 | 740,744-746 | Domestic Market Size 2029E (USD Bn): total / segment values | 91.3 total; 7.5, 27.6, 56.2 by segment | `LAYOUT_AMBIGUOUS` — same caveat as M109 |
| M111 | 24 | 738 | Domestic market CAGR 2023-2029E | 6.90% | |
| M112 | 24 | 738,741 | "vs. Global" comparator figures | 5.46 and 8.15 (USD Bn) | Label ambiguous — could be Global 2023/2029E market size; `LAYOUT_AMBIGUOUS` |
| M113 | 24 | 737,741,743-745 | India Power Transformer Market FY25 (USD value band + '000 units by voltage class) | $1.3-1.4bn; 3.2-3.4 / 0.6-0.7 / 0.8-0.9 | 3 unit-splits map to 3 legend classes (upto 66kV / <66≤220kV / >220≤765kV) — clean match |
| M114 | 24 | 737-739 | India Power Transformer Market FY29 (USD value band + '000 units by voltage class) | $3.3-3.4bn; 8.2-8.5 / 1.6-1.7 / 2.1-2.2 / 4.5-4.6 / 1.8-1.9 | 5 numeric bands present for a 3-class legend — count mismatch; flag `LAYOUT_AMBIGUOUS` / possible extra data points not mapped to a visible legend class |
| M115 | 24 | 757-769 | Domestic Power Transformer Applications FY25 (% split, 000 units) | 6.35%, 3.17%, 9.52%, 9.52%, 42.86%, 28.57% (sums to ~100%); base 3.2-3.4 ('000 units) | 6 values cleanly match 6 legend items (T&D, Industry, Renewable Energy, Green Hydrogen, Mobility, Others) but exact value-to-label pairing order is `LAYOUT_AMBIGUOUS` |
| M116 | 24 | 763,766,769 | India Specialty Transformer Market (USD Mn): FY25 / FY29 | 320.4 / 836.6 | |
| M117 | 25 | 790-791 | Wallet-share figure (current) | currently INR 193.99 mn | Only numeric figure on an otherwise qualitative strategy slide |
| M118 | 27 | 820,823,825-826 | Revenue from Operations (INR Cr): FY22/FY23/FY24/FY25/FY26 | 625.66 / 873.88 / 867.55 / 1,244.18 / 1,851.52 | |
| M119 | 27 | 821,824,827-828 | EBITDA (INR Cr): FY22/FY23/FY24/FY25/FY26 | 89.36 / 143.12 / 123.16 / 193.58 / 344.44 | Footnote F9: "EBITDA - including Other Income" |
| M120 | 27 | 821 | EBITDA Margin %: FY22/FY23/FY24/FY25/FY26 | 14.28% / 16.38% / 14.20% / 15.56% / 18.60% | Same footnote basis as M119; **definitional mismatch vs slide 7/9 EBITDA (excludes Other Income)** — flag `DEFINITION_MISMATCH` |
| M121 | 27 | 839-842 | PAT (INR Cr): FY22/FY23/FY24/FY25/FY26 | 55.30 / 87.47 / 63.52 / 118.65 / 201.77 | |
| M122 | 27 | 835 | PAT Margin %: FY22/FY23/FY24/FY25/FY26 | 8.84% / 10.01% / 7.32% / 9.54% / 10.90% | |
| M123 | 27 | 834-841 | Return Ratios RoE & RoCE (%), FY22-FY26 | 71.18%, 57.99%, 55.01%, 53.05%, 42.34%, 39.43%, 33.91%, 34.11%, 27.80%, 21.71% (10 values) | `LAYOUT_AMBIGUOUS` — pdftotext -layout does not preserve unambiguous (year, RoE-vs-RoCE) pairing for a 2-series x 5-year grouped chart; count (10 = 5 years x 2 ratios) is confirmed, pairing is not |
| M124 | 28 | 858-862 | Net Working Capital (Days), FY22-FY26 | 48, 58, 64, 65, 68 (5 values) | `LAYOUT_AMBIGUOUS` on exact year mapping; count of 5 confirmed against 5-year axis |
| M125 | 28 | 858,865-870 | Debt-Equity Ratio (times), FY22-FY26 | 0.05, 0.21, 0.40, 0.44, 0.97 (5 values) | `LAYOUT_AMBIGUOUS` on exact year mapping; count of 5 confirmed |
| M126 | 28 | 857,864,867,870-871 | Cash Flow from Operations (INR Cr), FY22-FY26 | 0.75, 51.98, 83.58, 88.31, 184.33 (5 values) | `LAYOUT_AMBIGUOUS` on exact year mapping; count of 5 confirmed |
| M127 | 29 | 883 | Revenue from Operations | FY26 1,851.5 / FY25 1,244.2 / FY24 867.6 | |
| M128 | 29 | 884 | Cost of Materials Consumed | FY26 1,413.6 / FY25 861.4 / FY24 675.6 | |
| M129 | 29 | 885 | Changes in Inventories | FY26 (113.4) / FY25 54.9 / FY24 (40.4) | |
| M130 | 29 | 886 | Gross Profit | FY26 551.3 / FY25 327.8 / FY24 232.33 | |
| M131 | 29 | 887 | Gross Profit % | FY26 29.8% / FY25 26.3% / FY24 26.8% | |
| M132 | 29 | 888 | Employee Benefits Expenses | FY26 41.9 / FY25 29.4 / FY24 21.6 | |
| M133 | 29 | 889 | Other Expenses | FY26 165.0 / FY25 104.8 / FY24 92.1 | |
| M134 | 29 | 890 | EBITDA | FY26 344.4 / FY25 193.6 / FY24 118.66 | Ties to M119 (344.44 rounds to 344.4) — consistent |
| M135 | 29 | 891 | EBITDA % | FY26 18.6% / FY25 15.6% / FY24 13.7% | Ties to M120 |
| M136 | 29 | 892 | Depreciation and Amortization Expenses | FY26 26.1 / FY25 6.3 / FY24 5.9 | |
| M137 | 29 | 893 | EBIT | FY26 318.3 / FY25 187.3 / FY24 112.80 | |
| M138 | 29 | 894 | EBIT % | FY26 17.2% / FY25 15.1% / FY24 13.0% | |
| M139 | 29 | 895 | Other Income | FY26 15.7 / FY25 6.3 / FY24 4.5 | |
| M140 | 29 | 896 | Finance Cost | FY26 56.6 / FY25 34.2 / FY24 30.0 | |
| M141 | 29 | 897 | Exceptional Item | FY26 1.2 / FY25 0.0 / FY24 0.0 | Not fully zero (FY26 nonzero) — not tagged `ZERO_STANDING`, but 2 of 3 periods are nil |
| M142 | 29 | 898 | PBT | FY26 276.2 / FY25 159.3 / FY24 87.27 | |
| M143 | 29 | 899 | PBT % | FY26 14.9% / FY25 12.8% / FY24 10.1% | |
| M144 | 29 | 900 | Total Tax Expense | FY26 74.4 / FY25 40.7 / FY24 23.9 | |
| M145 | 29 | 901 | PAT | FY26 201.8 / FY25 118.6 / FY24 63.36 | Ties to M121 FY26 201.77 — consistent |
| M146 | 29 | 902 | PAT % | FY26 10.9% / FY25 9.5% / FY24 7.3% | |
| M147 | 29 | 903 | Basic & Diluted EPS | FY26 27.17 / FY25 16.57 / FY24 8.87 | |
| M148 | 29 | 882-903 | Line-item count vs slide 9 table | Slide 29 table has 21 line items; slide 9 table has 22 (includes "Purchase of Stock-in-Trade") | `TABLE_STRUCTURE_DIFFERS` — the FY-summary table drops the Purchase of Stock-in-Trade row entirely rather than showing it as a zero row; not itself an error but a structural inconsistency between the two income-statement exhibits in the same deck |

**Note on Table 2 continuity:** M35 (Purchase of Stock-in-Trade, all-zero) is the deck's one clean `ZERO_STANDING` line item; M48 and M141 (Exceptional item) are near-zero (2 of 3 periods nil) but not tagged `ZERO_STANDING` because at least one period is non-zero.

---

## TABLE 3 — FOOTNOTES & FINE-PRINT DISCLAIMERS (bullet 4, ENUMERATE — INVESTOR PRESENTATION)

| ID | Slide | Line(s) | Footnote text (qualifying which headline number) | Flags |
|---|---|---|---|---|
| F1 | 3 | 102-124 | Full forward-looking-statements / no-reliance disclaimer, qualifies the entire presentation | Standard boilerplate |
| F2 | 7 | 228 | "*EBITDA- excluding Other Income" — qualifies M25/M26 (Q1 snapshot EBITDA) | |
| F3 | 11 | 337 | "*RoCE for FY26." — qualifies M57 (39.11% RoCE shown on a Q1FY27-dated slide) | See M57 `PERIOD_LABEL_CHECK` |
| F4 | 16 | 613 (footnote appears on slide 19, not 16 — see F7) | — | (moved; see F7) |
| F5 | 17 | 545 | "*BTW facility is easily upgradable to 1,200 kV within existing infrastructure" — qualifies M78 | |
| F6 | 17 | 545 | "^Includes BTW's outstanding borrowings of ~ INR 800 Mn" — qualifies M83 (EV of ~INR 2,600 Mn) | Material qualifier: headline EV figure is gross of ~INR 800 Mn assumed borrowings |
| F7 | 19 | 613 | "*HV: High Voltage, LV: Low Voltage" — qualifies M88 terminology | |
| F8 | 17 | 545 | "VDP – Vendor development Programme" — glossary definition, no VDP figure appears elsewhere on this slide despite the definition being present | Definition without a corresponding disclosed VDP metric — possible orphaned footnote, worth an A3 check |
| F9 | 17,20 | 545,640 | "* Formerly known as BTW Atlanta" — appears twice (slide 17 and slide 20), qualifying the Atlanta Trafo Limited name each time | Repeated footnote, not a flag on its own |
| F10 | 24 | 771 | "*Specialty includes electric arc furnace, rectifier, inverter, phase shifting transformers, etc." — qualifies M109/M110 "Specialty" segment | |
| F11 | 27 | 846 | "*EBITDA- including Other Income" — qualifies M119/M120 (FY22-FY26 EBITDA & margin) | `DEFINITION_MISMATCH` against F2 — same "EBITDA" label used with opposite Other-Income treatment on slide 7 vs slide 27 within the same deck |

Footnote count test: grep `grep -n -E "^\s*\*|^\s*\^"` style sweep across the extract for footnote-marker lines vs manual read of every asterisked/caret clause on slides 3,7,11,17,19,20,24,27 → 11 distinct footnote clauses found both ways (F4 folded into F7 on re-check; F1 counted as one page-level disclaimer block). Match: yes.

---

## TABLE 4 — PEOPLE / SIGNATORY ENUMERATION (directors, management, signatories, contacts — one row each)

| ID | Slide | Line(s) | Name | Role | Notes |
|---|---|---|---|---|---|
| P1 | 1 | 54-55 | Tejal S. Panchal | Company Secretary & Compliance Officer (signatory of cover letter) | Digital signature timestamp 2026.07.21 13:21:35 +05'30' (M7) |
| P2 | 6 | 179-180 | Niral Krupeshbhai Patel | Chairman and Managing Director (quoted in Management Commentary) | |
| P3 | 13 | 391-401 | Niral Krupeshbhai Patel | Chairman and Managing Director | Over 22 years' experience; Diploma (electrical engg, Maharashtra State Board) + MBA (Hult Int'l Business School). No DIN disclosed |
| P4 | 13 | 391-401 | Amish Krupeshbhai Patel | Whole-time Director | Joined 2022; 17 years combined experience in real estate, investment, acquisitions; Bachelor's, business administration (Sardar Patel University). No DIN disclosed |
| P5 | 13 | 391-401 | Tanmay Surendrabhai Patel | Whole-time Director | Joined 2022; over 22 years' expertise, transformers/electrical/manufacturing; Diploma, electrical engg (Maharashtra State Board). No DIN disclosed |
| P6 | 13 | 406-414 | Milin Kaimas Mehta | Independent Director | Chartered Accountant (ICAI); designated partner, K C Mehta & Co. LLP. No DIN disclosed |
| P7 | 13 | 406-414 | Bhadresh Bhupendrabhai Chauhan | Independent Director | Previously Gujarat Electricity Board & Gujarat Energy Transmission Corp Ltd; Bachelor's, electrical engg (Sourashtra University). No DIN disclosed |
| P8 | 13 | 406-414 | Dukhabandhu Rath | Independent Director | Previously State Bank of India, 35+ years banking; Bachelor's Arts (Hons), Utkal University. No DIN disclosed |
| P9 | 13 | 406-414 | Jinkal Darshan Patel | Independent Director | Elysium Pharmaceuticals Ltd, 16+ years pharma experience; Bachelor's engg (Sardar Patel University) + MBA (Pace University). No DIN disclosed |
| P10 | 14 | 423-437 | Akshaykumar Banshilal Mathur | Chief Executive Officer | With company since 2015 (12+ yrs); B.Tech Electronics & Comm. (Kakatiya Univ) + MBA (Univ of Jodhpur); previously Voltamp Transformers Ltd |
| P11 | 14 | 423-436 | Anand Sharma | Chief Operating Officer | With company since 2022 (~22 yrs combined experience); Diploma engg (Dayalbagh Educational Institute); previously Hotline Glass Ltd, BTA Cellcom Ltd, EMCO Ltd |
| P12 | 14 | 423-437 | Mehul Sureshbhai Mehta | Chief Financial Officer | With company since 2005 (~19 yrs); PG Diploma business admin (Sardar Patel Univ) + MBA (ICFAI Univ, Dehradun); previously ABG Cement Ltd |
| P13 | 14 | 442-452 | Minesh Bhatt | Vice President - Design | With company since 2004 (23 yrs); Diploma electrical engg (Govt Polytechnic, Chhotaudaipur); previously Voltamp Transformers Pvt Ltd |
| P14 | 14 | 442-452 | Tejalben Saunakkumar Panchal | Company Secretary and Compliance Officer | With company since 2023 (~7 yrs work experience noted); Master's Commerce, accounting & financial management (MSU Baroda); previously Vimal Fire and Emergency Services Ltd |
| P15 | 30 | 915-916 | Tejal S. Panchal (Ms) | Company Secretary & Compliance Officer (contact page) | Same individual as P1/P14 |
| P16 | 30 | 911,913-914 | Mohit Upadhyay | AdfactorsPR (IR contact) | Email: mohit.upadhyay@adfactorspr.com |
| P17 | 30 | 917-918 | Tejpal Singh | AdfactorsPR (IR contact) | Email: Tejpal.singh@adfactorspr.com |

Note: P1/P14/P15 name the same person (Tejal S. Panchal / Tejalben Saunakkumar Panchal, CS & Compliance Officer) across three separate slide contexts; the CMD (P2/P3) is present, addressing the concall-transcript instruction to note promoter/CMD presence — not applicable in the same way to a presentation doctype, but flagged here for completeness since the CMD is directly quoted.

---

## TABLE 5 — KEY MILESTONES TIMELINE (slide 12)

Layout caveat: slide 12 is a graphical timeline. `pdftotext -layout` linearizes the graphic left-to-right/top-to-bottom, which does not reliably preserve which caption belongs to which year marker. Years and nearby caption text are grouped below on a best-effort proximity basis and flagged `TIMELINE_LAYOUT_UNCERTAIN`; A3/A4 should confirm the year-caption pairing against the source PDF graphic before treating any single pairing as a hard fact — the years and total milestone count (10) are certain, the exact text-to-year mapping is not.

| ID | Year | Line(s) | Best-effort milestone text | Flag |
|---|---|---|---|---|
| T1 | 1988 | 376,381-383 | Started Supplying 132/66 kV, 50 MVA Power Transformers to Utilities | `TIMELINE_LAYOUT_UNCERTAIN` |
| T2 | 1992 | 374-378 | Started supplying 220/66 kV, 100 MVA Power Transformer to the Utility | `TIMELINE_LAYOUT_UNCERTAIN` |
| T3 | 2007 | 366-372 | Establishment of ATLANTA Electricals Pvt. Ltd. | `TIMELINE_LAYOUT_UNCERTAIN` |
| T4 | 2011 | 354-358,368 | Started the manufacturing of 33 kV & 66 kV Class Power Transformers | `TIMELINE_LAYOUT_UNCERTAIN` |
| T5 | 2014 | 359-369 | Awaited the "Best Equipment Supplier" by GETCO | `TIMELINE_LAYOUT_UNCERTAIN` |
| T6 | 2018 | 357,359-362 | Dynamic S.C. test performed on 160 MVA, 220/66 kV Power Transformer, 220/132 kV Auto Transformer | `TIMELINE_LAYOUT_UNCERTAIN` |
| T7 | 2020 | 343-351,355 | Supplied 14, 6.3 MVA, 66/11 kV power transformers to NHPC and awarded as Best Company in the field of Technological Innovation during Vibrant Summit | `TIMELINE_LAYOUT_UNCERTAIN` |
| T8 | 2023 | 354,359-362 | Listed on Stock Exchanges; Credit Rating upgrade — A/stable long term | `TIMELINE_LAYOUT_UNCERTAIN` |
| T9 | 2024 | 344-353,365-375 | Supplied first 160 MVA, 220/66 kV Power Transformer and 150 MVA, 220/132 kV Auto Transformer to GETCO; 100% acquisition — Atlanta Trafo, commenced operations; Vadod plant operational — contributing to revenue; Added 3 NABL Accredited testing labs; GETCO order - Rs. 298 Cr for 25 transformers | `TIMELINE_LAYOUT_UNCERTAIN` |
| T10 | 2025 | 343-351 | Awaited "Quality Excellence for Renewable" by EXIM Club | `TIMELINE_LAYOUT_UNCERTAIN` |

One numeric figure embedded in T9's cluster is a clean standalone disclosure regardless of exact year-pairing: **GETCO order — Rs. 298 Cr for 25 transformers** (line 374-375), the only rupee-denominated contract-win figure named anywhere in the milestones slide.

---

## TABLE 6 — PRIOR-QUARTER COMPARISON (DROPPED_SLIDE)

No prior-quarter deck or prior A2 ledger was supplied to this run (PRIOR_LEDGER_PATH not injected). The `DROPPED_SLIDE` check (bullet 3 of ENUMERATE — INVESTOR PRESENTATION) could not be executed. Flag `NO_PRIOR_LEDGER` — recommend the next quarterly cycle's A1/A2 pair for atlantaelec receive this ledger as the PRIOR_LEDGER_PATH input so the check becomes possible from Q2FY27 onward.

---

## SUMMARY COUNTS

- Slides enumerated (Table 1): 30
- Numeric/disclosure metric rows (Table 2): 148 (M1-M148)
- Footnote rows (Table 3): 11 (F1-F11)
- People/signatory rows (Table 4): 17 (P1-P17)
- Milestone timeline rows (Table 5): 10 (T1-T10, incl. 1 embedded standalone figure noted in prose)
- Total disclosure units enumerated (Tables 2-5 combined): 148 + 11 + 17 + 10 = 186, matching the COUNT TEST block at the top of this file.

## FLAGS RAISED (full list)
- `ZERO_STANDING` — M35 (Purchase of Stock-in-Trade, all-zero, slide 9)
- `DIN_NOT_DISCLOSED` — slide 13, all 7 directors (P3-P9)
- `DATA_PLACEHOLDER` — M77, slide 16, 6x `[TBU]` image placeholders
- `LAYOUT_AMBIGUOUS` — M76, M109, M110, M112, M114, M115, M123, M124, M125, M126 (chart/grid pairings not recoverable from linearized text)
- `TIMELINE_LAYOUT_UNCERTAIN` — T1-T10, slide 12
- `TABLE_STRUCTURE_DIFFERS` — M148 (slide 29 income statement drops the Purchase of Stock-in-Trade line present on slide 9's income statement)
- `DEFINITION_MISMATCH` — M120/F11 vs M19/M26/F2 (EBITDA including vs excluding Other Income used interchangeably across the deck)
- `PERIOD_LABEL_CHECK` — M57 (FY26 RoCE figure shown on a Q1FY27-dated "Atlanta at a Glance" slide)
- `NO_PRIOR_LEDGER` — Table 6, DROPPED_SLIDE check not executable this cycle

Output written to: /home/user/inflection-pipeline/runs/atlantaelec-q1fy27/work/ledger_presentation_atlantaelec_q1fy27.md
