# A2 ENUMERATOR LEDGER — Presentation — GANECOS Q1 FY27

Source: `extract_presentation_ganecos_q1fy27.txt` (34 pages/slides, pdfinfo=34, formfeed=34, OCR pages [2,5,13,17,31], units INR Crore x1, unless stated as TPA/MT/INR000s/INR per share).
Prior-quarter presentation ledger: NOT AVAILABLE (no `ganecos-q4fy26` presentation extract/ledger found in repo — only a results extract exists for that quarter). DROPPED_SLIDE comparison therefore cannot be run this cycle; recorded as `PRIOR_LEDGER_UNAVAILABLE`, not a pass/fail.

```
=== A2 COUNT TEST ===
category: slides          grep_count: 34   sweep_count: 34   match: yes
category: slide_numbers   grep_count: 34   sweep_count: 34   match: yes
category: ocr_pages       grep_count: 5    sweep_count: 5    match: yes
category: chart_slides    grep_count: 7    sweep_count: 7    match: yes
category: pl_line_items   grep_count: 28   sweep_count: 28   match: yes   (14 consolidated + 14 standalone)
category: footnote_marks  grep_count: 5    sweep_count: 5    match: yes  (4x "*Production Data excluding captive consumption" + 1x "*Another brownfield expansion...")
category: zero_standing   grep_count: 0    sweep_count: 0    match: yes  (no P&L line item is nil/dash in ALL four periods on either statement)
category: notes                n/a (not a results filing doctype) — 0 / not present
category: agenda_items          n/a (not a board-outcome doctype) — 0 / not present
category: auditor_paras         n/a (no auditor report in a presentation) — 0 / not present
category: entities              n/a (no consolidation-scope schedule on these slides; 3 subsidiaries named qualitatively on slide 15, tabulated below) — 0 formal entity-list rows / not present
category: turns/questions/mgmt_numbers  n/a (concall-only categories) — 0 / not present
gate_a2: pass
=== END COUNT TEST ===
```

Reconciliation note: pdfinfo page count (34) = `[page N]` marker grep count (34) = manual slide-by-slide sweep below (34 rows in Table A). All three agree. The 5 `[OCR page N]` merge tags (pages 2, 5, 13, 17, 31 — all section-divider slides where the rendered title graphic required OCR per the A1 header) do not add slides; they duplicate content already present in the primary text layer for the same page number, confirmed by manual read (each OCR block simply repeats "GESL / 0N / <section title>"). The 7 `[CHART, page N]` flags (pages 6,7,8,9,10,11,18) were each manually opened and their numeric labels enumerated in Table B.

---

## TABLE A — Slide Index (all 34 slides)

| Slide | Line (start) | Title / Section | Content type | Flags |
|---|---|---|---|---|
| 1 | 15 | Regulation 30 cover letter to BSE/NSE (transmittal of presentation) | text (regulatory letter) | — |
| 2 | 61 (OCR 65) | Title slide: "Ganesha Ecosphere — Investors Presentation \| Q1FY27" | text/photo | — |
| 3 | 70 | Safe Harbour Statement | text (disclaimer) | covers whole deck |
| 4 | 83 | Towards A Greener Future — Our Vision / Our Mission | text | — |
| 5 | 95 (OCR 98) | Section divider: "01 Financial Overview" | text (divider) | — |
| 6 | 103 | Q1FY27 Consolidated Performance Highlights (QoQ) | chart | CHART |
| 7 | 132 | Q1FY27 Standalone Performance Highlights (QoQ) | chart | CHART |
| 8 | 161 | Q1FY27 Consolidated Performance Highlights (YoY) | chart | CHART |
| 9 | 193 | Q1FY27 Standalone Performance Highlights (YoY) | chart | CHART |
| 10 | 223 | Quarter Wise Performance (5-qtr trend, both entities) | chart | CHART |
| 11 | 267 | Production vs Sales Volume in MT (5-qtr trend, both entities) | chart | CHART |
| 12 | 294 | Highlights of Q1FY27 (7 management bullets) | text (commentary) | GUIDANCE-adjacent metrics; see Table C |
| 13 | 311 (OCR 314) | Section divider: "02 Business Overview" | text (divider) | — |
| 14 | 319 | Ganesha Ecosphere \| Leading PET Plastic Recycling Company (company stat tiles) | text/infographic | — |
| 15 | 331 | Company Structure (subsidiaries, Warangal/Nepal ops) | text/org chart | — |
| 16 | 362 | Awards, recognition and industry visibility (3 awards) | text/photo | — |
| 17 | 372 (OCR 375) | Section divider: "03 Industry Overview" | text (divider) | — |
| 18 | 380 | India's PET Market growth chart + India EPR Rules table | chart + table | CHART |
| 19 | 411 | Key Growth Drivers for Recycled PET | text | no numeric data |
| 20 | 425 | Section divider: "04 Key Strengths" | text (divider) | — |
| 21 | 431 | Key Strengths — list of 5 | text (list) | — |
| 22 | 449 | Strength 1 detail — PET recycling revolution, capacity/revenue milestones timeline | text/infographic | GUIDANCE (capacity ramp figures) |
| 23 | 479 | Strength 2 detail — value-chain diagram, domain expertise | text/diagram | — |
| 24 | 511 | Strength 3 detail — GoRewise brand | text | — |
| 25 | 531 | New Products Under GoRewise (rPET Chips vs rPET Fibers & Yarns) | table (qualitative) | — |
| 26 | 548 | State-of-the-art manufacturing facilities — capacity table by facility (TPA) | table | GUIDANCE (footnote: brownfield expansion) |
| 27 | 581 | Experienced Management and Board of Directors (8 profiles) | text/table | — |
| 28 | 616 | ...driven towards a sustainable future (ESG/solar/water/zero-discharge) | text | — |
| 29 | 633 | Section divider: "05 Key Strategies" | text (divider) | — |
| 30 | 639 | The Way Forward — 5 forward strategy points | text (list) | GUIDANCE x3 |
| 31 | 662 (OCR 665) | Section divider: "06 Financial Summary" | text (divider) | — |
| 32 | 670 | Profit & Loss Statement — Consolidated (4-period table) | table | — |
| 33 | 691 | Profit & Loss Statement — Standalone (4-period table) | table | — |
| 34 | 713 | Thank You / contact details | text | — |

---

## TABLE B — Chart / Table Numeric Disclosure Units (slides 6–11, 18, 26)

Each row is one metric cluster (both/all period values as printed). Where the extracted text layer scrambles bar-label order relative to axis position, this is flagged `CHART_ORDER_APPROX` — the values are enumerated as printed; period-to-value assignment is best-effort using the anchor values in Table F (P&L) where possible, and should not be treated as authoritative attribution without cross-check at A3/A4.

| Slide | Line(s) | Metric | Values as printed | Flags |
|---|---|---|---|---|
| 6 | 106–115 | Revenue from operations (INR Cr), QoQ, Consolidated | Q4FY26 423.9 / Q1FY27 423.7 | — |
| 6 | 106–115 | EBITDA (INR Cr), QoQ, Consolidated | Q4FY26 52.4 / Q1FY27 59.8 | — |
| 6 | 106–115 | EBITDA Margin %, QoQ, Consolidated | Q4FY26 12.4% / Q1FY27 14.1% | — |
| 6 | 106–115 | EBITDA/Ton (INR '000s), QoQ, Consolidated | Q4FY26 11.6 / Q1FY27 14.9 | — |
| 6 | 116–128 | PAT (INR Cr), QoQ, Consolidated | Q4FY26 23.2 / Q1FY27 29.0 | matches P&L table 23.21/29.03 (rounded) |
| 6 | 116–128 | Cash Profits (INR Cr), QoQ, Consolidated | Q4FY26 40.4 / Q1FY27 46.4 | — |
| 6 | 116–128 | Production Volume (MT), QoQ, Consolidated | values printed: 41,268 / 42,826 | CHART_ORDER_APPROX |
| 6 | 116–128 | Sales Volume (MT), QoQ, Consolidated | values printed: 40,113 / 45,162 | CHART_ORDER_APPROX |
| 6 | 116–128 | EPS (INR), QoQ, Consolidated | Q4FY26 8.68 / Q1FY27 10.86 | consistent with higher Q1FY27 PAT |
| 6 | 130 | Footnote | "*Production Data excluding captive consumption" | applies to Production Volume row |
| 7 | 135–144 | Revenue from operations (INR Cr), QoQ, Standalone | Q4FY26 260.3 / Q1FY27 262.3 | — |
| 7 | 135–144 | EBITDA (INR Cr), QoQ, Standalone | Q4FY26 20.9 / Q1FY27 23.8 | — |
| 7 | 135–144 | EBITDA Margin %, QoQ, Standalone | Q4FY26 8.0% / Q1FY27 9.1% | — |
| 7 | 135–144 | EBITDA/Ton (INR '000s), QoQ, Standalone | Q4FY26 7.2 / Q1FY27 9.4 | — |
| 7 | 146–157 | PAT (INR Cr), QoQ, Standalone | Q4FY26 13.8 / Q1FY27 16.4 | wait — flagged below |
| 7 | 146–157 | Cash Profits (INR Cr), QoQ, Standalone | Q4FY26 20.6 / Q1FY27 23.6 | — |
| 7 | 146–157 | Production/Sales Volume (MT), QoQ, Standalone | values printed: 25,321 / 27,294 / 28,209 / 29,234 | CHART_ORDER_APPROX |
| 7 | 146–157 | EPS (INR), QoQ, Standalone | values printed 5.13 and 6.12 → Q4FY26 6.12 / Q1FY27 5.13 (inferred from PAT anchor: Q4FY26 PAT 16.41cr > Q1FY27 PAT 13.75cr per Table F) | ANCHOR-RESOLVED |
| 7 | 146–157 | **PAT re-check** | Chart shows 13.8 and 16.4; P&L table (slide 33) gives Q1FY27 standalone PAT 13.75, Q4FY26 16.41 — chart values map Q1FY27=13.8, Q4FY26=16.4, consistent | — |
| 7 | 159 | Footnote | "*Production Data excluding captive consumption" | — |
| 8 | 164–173 | Revenue (INR Cr), YoY, Consolidated | Q1FY26 337.1 / Q1FY27 423.7 | — |
| 8 | 164–173 | EBITDA (INR Cr), YoY, Consolidated | Q1FY26 36.3 / Q1FY27 59.8 | — |
| 8 | 164–173 | EBITDA Margin %, YoY, Consolidated | Q1FY26 10.8% / Q1FY27 14.1% | — |
| 8 | 164–173 | EBITDA/Ton (INR '000s), YoY, Consolidated | Q1FY26 10.8 / Q1FY27 14.9 | — |
| 8 | 174–189 | PAT (INR Cr), YoY, Consolidated | Q1FY26 10.8 / Q1FY27 29.0 | matches P&L 10.75/29.03 (rounded) |
| 8 | 174–189 | Cash Profits (INR Cr), YoY, Consolidated | Q1FY26 26.3 / Q1FY27 46.4 | — |
| 8 | 174–189 | Production/Sales Volume (MT), YoY, Consolidated | values printed: 33,650 / 36,049 / 40,113 / 42,826 | CHART_ORDER_APPROX |
| 8 | 174–189 | Basic EPS (INR), YoY, Consolidated | Q1FY26 4.23 / Q1FY27 10.86 | — |
| 8 | 191 | Footnote | "*Production Data excluding captive consumption" | — |
| 9 | 197–206 | Revenue (INR Cr), YoY, Standalone | Q1FY26 221.5 / Q1FY27 262.3 | — |
| 9 | 197–206 | EBITDA (INR Cr), YoY, Standalone | Q1FY26 9.3 / Q1FY27 23.8 | — |
| 9 | 197–206 | EBITDA Margin %, YoY, Standalone | Q1FY26 4.2% / Q1FY27 9.1% | — |
| 9 | 197–206 | EBITDA/Ton (INR '000s), YoY, Standalone | Q1FY26 3.9 / Q1FY27 9.4 | — |
| 9 | 207–219 | PAT (INR Cr), YoY, Standalone | Q1FY26 7.7 / Q1FY27 13.8 | matches P&L 7.66/13.75 (rounded) |
| 9 | 207–219 | Cash Profits (INR Cr), YoY, Standalone | Q1FY26 13.5 / Q1FY27 20.6 | — |
| 9 | 207–219 | Production/Sales Volume (MT), YoY, Standalone | values printed: 24,040 / 25,321 / 25,392 / 27,294 | CHART_ORDER_APPROX |
| 9 | 207–219 | Basic EPS (INR), YoY, Standalone | Q1FY26 3.01 / Q1FY27 5.13 | — |
| 9 | 221 | Footnote | "*Production Data excluding captive consumption" | — |
| 10 | 226–247 | Total Income (INR Cr), 5-qtr trend, Consolidated | Q1FY26 340.5 / Q2FY26 368.7 / Q3FY26 361.4 / Q4FY26 428.5 / Q1FY27 427.3 | CHART_ORDER_APPROX (axis order as printed) |
| 10 | 226–247 | EBITDA (INR Cr) + Margin %, 5-qtr trend, Consolidated | values printed 22.3, 30.7, 36.3, 52.4, 59.8; margins 6.1%, 8.6%, 10.8%, 12.4%, 14.1% | CHART_ORDER_APPROX |
| 10 | 226–247 | PAT (INR Cr), 5-qtr trend, Consolidated | values printed 10.8, 4.7, -0.5, 23.2, 29.0 | CHART_ORDER_APPROX; note Q3FY26 negative (-0.5) |
| 10 | 249–264 | Total Income (INR Cr), 5-qtr trend, Standalone | 229.6, 270.0, 284.1, 270.2, 265.8 | CHART_ORDER_APPROX |
| 10 | 249–264 | EBITDA (INR Cr) + Margin %, 5-qtr trend, Standalone | 8.2, 9.3, 18.5, 20.9, 23.8; margins 3.2%, 4.2%, 6.8%, 8.0%, 9.1% | CHART_ORDER_APPROX |
| 10 | 249–264 | PAT (INR Cr), 5-qtr trend, Standalone | 7.7, 7.8, 15.9, 16.4, 13.8 | CHART_ORDER_APPROX |
| 11 | 270–280 | Production Volume Standalone (MT), 5-qtr trend | 25,392 / 29,088 / 28,209 / 27,294 / 25,689 (order as printed) | CHART_ORDER_APPROX |
| 11 | 271–279 | Production Volume Consolidated (MT), 5-qtr trend | 38,845 / 38,768 / 41,268 / 42,826 / 36,049 (order as printed) | CHART_ORDER_APPROX |
| 11 | 282–289 | Sales Volume Standalone (MT), 5-qtr trend | 31,107 / 29,234 / 29,068 / 25,321 / 24,040 (order as printed) | CHART_ORDER_APPROX |
| 11 | 283–291 | Sales Volume Consolidated (MT), 5-qtr trend | 45,162 / 40,233 / 40,113 / 39,132 / 33,650 (order as printed) | CHART_ORDER_APPROX |
| 18 | 383–401 | Global PET Bottle Production (Mn Ton), CY17/CY24/CY29F, CAGR 4% | PET Bottle series: 11.9 / 15.4 / 19.1; rPET Bottle series: 3.5 / 5.0 / 7.1 | series legend "PET Bottle / rPET Bottle" per line 403 |
| 18 | 383–401 | India PET Bottle Production (Mn Ton), CY17/CY24/CY29F, CAGR 10% | values printed: 0.8 / 1.3 / 2.3 | CHART_ORDER_APPROX |
| 18 | 387–406 | India EPR Rules table: Recycling Target (FY25→FY28) | Rigid Plastics 50%→80%; Flexible Packaging 30%→60%; Multi-Layer Packaging 30%→60%; Compostable Plastic 50%→80% | GUIDANCE (regulatory targets, not company-specific) |
| 18 | 387–406 | India EPR Rules table: Recycling Content Use Target (FY26→FY29) | Rigid Plastics 30%→60%; Flexible Packaging 10%→20%; Multi-Layer Packaging 5%→10%; Compostable Plastic 0%→0% | GUIDANCE |
| 18 | 387–406 | India EPR Rules table: Reuse Target (FY26→FY29) | Rigid Plastics 10%→25%; Flexible Packaging 0%→0%; Multi-Layer Packaging 0%→0%; Compostable Plastic 0%→0% | GUIDANCE; ZERO_STANDING-style (explicit 0% targets across categories — recorded, not dropped) |
| 18 | 407 | Callout stat | "15 Lac Ton India PET Bottle expected consumption in CY25" | forward estimate |
| 18 | 408 | Callout stat | "40% India Recycled content use EPR Target in PET bottles in FY27" | GUIDANCE (regulatory) |
| 26 | 552–578 | Facility capacity table (TPA) | Kanpur 10,200; rPET Fibre 7,200; Dyed Textured Yarn 3,000; Rudrapur 39,600; rPET Fibre 39,600; Bilaspur & Temra 57,000; rPET Fiber 49,800; rPET SpunYarn 7,200; Warangal 77,640; rPET Granules 64,500*; B2F Chips/Filament yarn 12,240; RPSF 12,600; PPSF 10,800; Nepal 12,000; Washed Flakes 12,000 | 15 capacity line items |
| 26 | 575–577 | Footnote to Warangal rPET Granules 64,500 TPA | "*Another brownfield expansion of 22,500 TPA is underway" | GUIDANCE — forward capacity-expansion commitment |

---

## TABLE C — Textual / Qualitative Disclosure Units (bullets, infographic stat tiles)

| Slide | Line(s) | Unit | Content (first ~15 words / value) | Flags |
|---|---|---|---|---|
| 1 | 17 | Letter reference | GESL/2026-27 | — |
| 1 | 18 | Letter date | August 3, 2026 | — |
| 1 | 34–35 | Scrip identifiers | Scrip Symbol GANECOS; Scrip Code 514167 | — |
| 1 | 36–42 | Regulatory basis | Regulation 30 and Regulation 46 of SEBI (LODR) Regulations, 2015 | — |
| 1 | 41 | Period covered | "quarter ended 30th June, 2026" | — |
| 1 | 51–52 | Digital signature timestamp | 2026.08.03 21:08:12 +05'30' | — |
| 1 | 53–54 | Signatory | Bharat Kumar Sajnani, Company Secretary-cum-Compliance Officer | — |
| 1 | 58 | CIN | L51109UP1987PLC009090 | — |
| 3 | 72–80 | Safe Harbour Statement full text | forward-looking-statement disclaimer, lists trigger words and risk factors | qualifies every guidance/forward number in the deck |
| 4 | 85–92 | Vision statement | "To become a global corporate citizen, committed to recycle every PET bottle..." | — |
| 4 | 85–92 | Mission statement | "We will continue to deliver enhanced value for our stakeholders..." | — |
| 12.1 | 296 | Bullet 1 | "Strong performance continued from Q4FY26 across standalone and consolidated businesses" | — |
| 12.2 | 297 | Bullet 2 | "Production volumes rose by 3.8%, reflecting operational efficiency" | numeric: 3.8% |
| 12.3 | 298–299 | Bullet 3 | "Consolidated sales declined by 11.2% due to a 13.4% drop in standalone sales volumes, driven by weaker demand amid higher polymer prices and geopolitical tensions" | numeric: 11.2%, 13.4% |
| 12.4 | 300 | Bullet 4 | "Legacy business operated at 102% and Warangal unit operated at 72% capacity" | numeric: 102%, 72% capacity utilisation — not shown as a chart elsewhere in deck |
| 12.5 | 301–303 | Bullet 5 | "Both businesses delivered strong margin performance... Consolidated margins improved to 14.11%, up 176 bps QoQ; standalone margins rose to 9.07%, up 103 bps" | numeric: 14.11%, 176bps, 9.07%, 103bps (precise vs. chart-rounded 14.1%/9.1%) |
| 12.6 | 304–305 | Bullet 6 | "Consolidated PAT growth surged 25% QoQ to ₹29.03 crore, highlighting resilience..." | numeric: 25% QoQ, ₹29.03cr — matches P&L table |
| 12.7 | 306–308 | Bullet 7 | "Standalone other income dropped from ₹9.86 crore to ₹3.53 crore due to discontinuation of interest income on subsidiary loans converted into equity" | numeric: 9.86cr→3.53cr; **NUMBER_DISCREPANCY**: P&L table (slide 33, line 695) shows standalone Other Income Q1FY27 = 3.52, not 3.53 — 0.01cr rounding mismatch between commentary and table |
| 14 | 321 | Stat tile | "3+ Decades" rich industry experience | — |
| 14 | 321 | Stat tile | "500+ Product Variants" | — |
| 14 | 322 | Stat tile | "400+ Customers across 16+ countries" | — |
| 14 | 324,326 | Stat tile | "6 Manufacturing Facilities" | — |
| 14 | 324 | Stat tile | "218,940 MTPA Recycling & Washing Capacity" | — |
| 14 | 325 | Stat tile | "300+ Supplier Network Pan India" | — |
| 14 | 327 | Stat tile | "8.5 bn+ Scrap bottles recycled annually" | — |
| 14 | 327 | Stat tile | "150,000+ MTPA PET Waste converted" | — |
| 14 | 327 | Stat tile | "2,800+ Employees" | — |
| 15 | 334 | Incorporation fact | "Incorporated in 1987 by Mr. Shyam S. Sharmma" | — |
| 15 | 341–342 | Subsidiary 1 | Ganesha Ecopet Private Limited, wholly owned | — |
| 15 | 341–342 | Subsidiary 2 | Ganesha Ecotech Private Limited, wholly owned | — |
| 15 | 341–342 | Subsidiary 3 | Ganesha Overseas Private Limited, wholly owned | — |
| 15 | 345–347 | Commencement dates | Ecopet partial Apr 1 2023; Ecotech Feb 1 2023; Overseas Feb 1 2023 | — |
| 15 | 343 | Total installed capacity | "218,940 tons across products" | — |
| 15 | 357 | Collection network stat | "mobilizes ~450 tons of PET bottle waste every day" | — |
| 15 | 351–354 | Warangal / Nepal ops | rPET chips (Bottle & Textile grade), rPET Filament Yarn, RPSF, PPSF at Warangal; Washed PET Flakes at Nepal | — |
| 16 | 365,369 | Award 1 | Global Leadership in Circular Textiles — ATEXCON 2026, Govt of Telangana | — |
| 16 | 366,369 | Award 2 | Sarvashrestha Udyam Puraskar — Govt of Uttar Pradesh, plastic-waste recycling | — |
| 16 | 366,368 | Award 3 | Industry Thought Leadership — Injection & Blow Moulding Conference, Yash Sharma | — |
| 19 | 413–422 | Growth driver 1 | rising demand for sustainable packaging, global regulations compelling brands to adopt rPET | no hard numeric |
| 19 | 413–422 | Growth driver 2 | durability/safety/recyclability making rPET preferred option | no hard numeric |
| 19 | 413–422 | Growth driver 3 | innovations in recycling technology enhancing quality/cost | no hard numeric |
| 19 | 418–422 | Growth driver 4 | standards/certifications from FSSAI, FDA, EFSA strengthening consumer confidence | regulatory-body names, no numeric |
| 21 | 435–446 | Strength 1 (list label) | "Leading the PET recycling revolution with early-mover dominance..." | — |
| 21 | 436–438 | Strength 2 (list label) | "Cultivating Deep Domain Expertise..." | — |
| 21 | 439–441 | Strength 3 (list label) | "Expanding product portfolio... GoRewise" | — |
| 21 | 443–444 | Strength 4 (list label) | "State-of-the-art manufacturing facilities... realigning product portfolio towards high-margin, value-added products" | — |
| 21 | 446 | Strength 5 (list label) | "Experienced Management and Board of Directors" | — |
| 22 | 457,460 | Milestone | Crossed INR 500 crore Revenue (timeline year unlabeled precisely, positioned among 2012–2025 axis) | CHART_ORDER_APPROX |
| 22 | 461–462 | Milestone | Crossed INR 1,000 crore Revenue | CHART_ORDER_APPROX |
| 22 | 468,472 | Capacity fact | Temra facility capacity 21,600 TPA | — |
| 22 | 467,471 | Capacity fact | Temra→Nepal expansion 12,000 TPA; Warangal expansion 50,000 TPA | GUIDANCE (historical expansion narrative, dated) |
| 22 | 473 | Capacity fact | Total capacity after Temra expansion 45,000 TPA | — |
| 22 | 469–472 | Capacity fact | "Ramping up capacities in rPET granules to 42,000 TPA" | GUIDANCE |
| 22 | 463–464,466 | Stat | "150,000+ MTPA of PET waste converted in FY26" | — |
| 22 | 467,475 | Stat | "8+ Billion of PET bottles recycled in FY26" | — |
| 22 | 465 | Timeline years | 2012, 2014, 2017, 2019, 2023, 2024, 2025 | — |
| 23 | 500 | JV fact | "Strategic JV with Race Eco Chain (49:51) to secure PET flakes supply" | — |
| 23 | 500 | Sales office count | "Company has 6 sales offices across the expanse of India" | — |
| 23 | 505–507 | Reach stat | "reach to 400+ clients in India as well as globally to 16+ countries" | — |
| 23 | 502–504 | Supplier stat | "strong relations and collection network of 300+ suppliers across India" | — |
| 23 | 506 | Collection stat | "mobilizes ~450 tons of PET waste every day" (repeats slide-15 figure) | duplicate of slide 15 |
| 24 | 526 | Experience stat | "average of 25+ years experience" (management) | — |
| 24 | 520 | ESG fact | "Zero Liquid Discharge facility" | — |
| 25 | 536–545 | Product table (qualitative) | rPET Chips – Bottle Grade vs rPET Fibers & Yarns: target customers, differentiation, certifications (USFDA/EFSA/FSSAI; GRS/Oekotex) | no numeric values |
| 26 | header | Facility map note | facility locations: Rudrapur, Bilaspur & Temra, Nepal, Kanpur, Warangal | — |
| 26 | 569–571 | Qualitative note | "Additional approvals for food grade applications in Warangal" | GUIDANCE-adjacent |
| 27.1 | 584–597 | Director 1 | Shyam Sunder Sharmma, Founder & Non-Executive Chairman, 60+ yrs experience | no DIN/term dates on this slide (normal for IR deck) |
| 27.2 | 585–597 | Director 2 | Sharad Sharma, Managing Director, 35+ yrs experience | — |
| 27.3 | 585–597 | Director 3 | Vishnu Dutt Khandelwal, Executive Vice-Chairman, 50+ yrs experience | — |
| 27.4 | 585–597 | Director 4 | Rajesh Sharma, Joint Managing Director, 35+ yrs experience | — |
| 27.5 | 598–613 | Director 5 | Jagat Jit Singh, Non-Executive Independent Director, 35+ yrs experience | — |
| 27.6 | 598–613 | Director 6 | Dr. Shobha Chaturvedi, Non-Executive Independent Director, 30+ yrs experience, PhD Pollution Abatement (HBTI Kanpur) | — |
| 27.7 | 598–613 | Director 7 | Akshay Kumar Gupta, Non-Executive Independent Director, 40+ yrs experience, CA | — |
| 27.8 | 598–613 | Director 8 | Rajiv Kumar Saxena, Non-Executive Independent Director, 35+ yrs experience, ex-CGM SBI | — |
| 28 | 619–625 | ESG fact | "total installed capacity of 16.53 MWp of Rooftop Solar power installations" | — |
| 28 | 620–624 | ESG fact | "Warangal facility equipped to recycle ~90% of water required in operations and only ~10% freshwater is needed" | — |
| 28 | 627 | ESG fact | "Zero discharge facility at Warangal" | duplicate concept of slide 24 ZLD claim |
| 28 | 626 | ESG fact | "Partnership with a leading IPP for supply of Solar Power for captive consumption" | — |
| 30.1 | 642–643 | Strategy point 1 | "Working with 40+ brands across various stages of approvals to provide rPET products" | GUIDANCE |
| 30.2 | 647,649–650 | Strategy point 2 | "Unlock the potential of high margin products. Target revenue contribution of value added products ~65% (vs 40% currently)" | GUIDANCE — explicit forward target, distinct enumerated unit for filing cross-check |
| 30.3 | 653,656–658 | Strategy point 3 | "Seize the demand for rPET in bottle grade applications; capitalize on regulations, one of few companies to have a large B2B facility" | — |
| 30.4 | 647–648 | Strategy point 4 | "Constantly strengthen our overseas presence through participation in international events and exhibitions" | — |
| 30.5 | 652,657–659 | Strategy point 5 | "Increasing rPET granules capacities to meet the growing demand; focus on increasing market share in technical textiles and household textiles sector" | GUIDANCE — no specific target number given (qualitative capacity-increase intent) |
| 34 | 715–717 | Contact details | registered address, email secretarial@ganeshaecosphere.com | — |

---

## TABLE D — Footnotes / Fine-print Disclaimers Qualifying Headline Numbers

| Line(s) | Slide | Footnote text | Qualifies |
|---|---|---|---|
| 130 | 6 | "*Production Data excluding captive consumption" | Production Volume, Consolidated QoQ |
| 159 | 7 | "*Production Data excluding captive consumption" | Production Volume, Standalone QoQ |
| 191 | 8 | "*Production Data excluding captive consumption" | Production Volume, Consolidated YoY |
| 221 | 9 | "*Production Data excluding captive consumption" | Production Volume, Standalone YoY |
| 575–577 | 26 | "*Another brownfield expansion of 22,500 TPA is underway" | Warangal rPET Granules capacity line (64,500 TPA) |
| 72–80 | 3 | Safe Harbour Statement (forward-looking-statement disclaimer) | every guidance/target number in the deck (slides 22, 26, 30) |

---

## TABLE E — Forward-Looking Guidance Numbers (distinct enumerated units for filing cross-check)

| Slide | Line(s) | Guidance statement | Flag |
|---|---|---|---|
| 22 | 467,471 | Historical/completed expansion narrative: Temra→Nepal 12,000 TPA, Warangal 50,000 TPA (already operationalized per slide text) | GUIDANCE (retrospective, verify against filing capacity disclosures) |
| 22 | 469–472 | "Ramping up capacities in rPET granules to 42,000 TPA" | GUIDANCE |
| 26 | 575–577 | Brownfield expansion of 22,500 TPA underway (Warangal rPET Granules, base 64,500 TPA) | GUIDANCE — forward capex/capacity commitment |
| 30 | 649–650 | Target revenue contribution of value-added products ~65% (vs 40% currently) | GUIDANCE — explicit numeric target |
| 30 | 642–643 | "Working with 40+ brands across various stages of approvals" | GUIDANCE — pipeline metric, not a hard target |
| 30 | 652 | "Increasing rPET granules capacities to meet the growing demand" | GUIDANCE — qualitative, no number given |
| 18 | 387–408 | India EPR regulatory targets (FY25–FY29, by category) and "40% India Recycled content use EPR Target in PET bottles in FY27" | GUIDANCE — regulatory (external), not company-specific, but company positions itself against these targets |

---

## TABLE F — P&L Line Items (Table Category — GATE-relevant)

### Consolidated (slide 32, lines 670–689) — Q1FY27 / Q4FY26 / Q1FY26 / FY26 (INR Cr)

| # | Line | Line item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|---|
| 1 | 673 | Net Revenue from operations | 423.67 | 423.94 | 337.12 | 1481.66 | — |
| 2 | 674 | Other Income | 3.62 | 4.54 | 3.38 | 17.42 | — |
| 3 | 675 | Total Income | 427.29 | 428.48 | 340.50 | 1499.08 | subtotal |
| 4 | 677–678 | Cost of materials consumed / traded goods | 303.52 | 245.61 | 226.70 | 928.37 | — |
| 5 | 679 | Changes in inventories | (35.56) | 26.89 | (8.80) | 46.85 | — |
| 6 | 680 | Employee benefits expense | 24.48 | 26.93 | 23.56 | 99.76 | — |
| 7 | 681 | Finance costs | 8.87 | 8.79 | 9.84 | 40.32 | — |
| 8 | 682 | Depreciation and amortization | 17.34 | 17.16 | 15.50 | 64.81 | — |
| 9 | 683 | Other expenses (incl. share of loss of an associate) | 71.55 | 72.22 | 59.38 | 265.02 | — |
| 10 | 684 | Profit before tax | 37.09 | 30.88 | 14.32 | 53.95 | subtotal |
| 11 | 685 | Tax Expense | (8.06) | (7.67) | (3.57) | (15.74) | — |
| 12 | 686 | Net Profit after tax | 29.03 | 23.21 | 10.75 | 38.21 | subtotal |
| 13 | 687 | Other Comprehensive income | 1.00 | (1.89) | (0.22) | (6.23) | — |
| 14 | 688 | Total Comprehensive Income | 30.03 | 21.32 | 10.53 | 31.98 | subtotal |

### Standalone (slide 33, lines 691–711) — Q1FY27 / Q4FY26 / Q1FY26 / FY26 (INR Cr)

| # | Line | Line item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|---|
| 1 | 694 | Net Revenue from operations | 262.30 | 260.33 | 221.47 | 1014.10 | — |
| 2 | 695 | Other Income | 3.52 | 9.86 | 8.17 | 39.80 | see NUMBER_DISCREPANCY at Table C row 12.7 (bullet says 3.53) |
| 3 | 696 | Total Income | 265.82 | 270.19 | 229.64 | 1053.90 | subtotal |
| 4 | 698–699 | Cost of materials consumed / traded goods | 201.08 | 172.16 | 161.17 | 669.38 | — |
| 5 | 700 | Changes in inventories | (25.79) | 1.53 | (5.40) | 40.95 | — |
| 6 | 701 | Employee benefits expense | 17.66 | 19.94 | 17.89 | 74.44 | — |
| 7 | 702 | Finance costs | 2.00 | 1.38 | 1.32 | 6.91 | — |
| 8 | 703 | Depreciation and amortization | 6.85 | 7.22 | 5.87 | 25.37 | — |
| 9 | 704 | Other expenses | 45.56 | 45.77 | 38.51 | 172.38 | — |
| 10 | 705 | Profit before tax | 18.46 | 22.19 | 10.28 | 64.47 | subtotal |
| 11 | 706 | Tax Expense | 4.71 | (5.78) | (2.62) | (16.64) | note sign flip vs consolidated convention — Q1FY27 standalone tax expense is positive 4.71 (a tax charge), unlike consolidated where all periods show a tax credit in parentheses; not a data error per se, flagged for A3 review |
| 12 | 707 | Net Profit after tax | 13.75 | 16.41 | 7.66 | 47.83 | subtotal |
| 13 | 708 | Other Comprehensive income | 1.00 | (2.05) | (0.23) | (6.41) | — |
| 14 | 709–710 | Total Comprehensive Income | 14.75 | 14.36 | 7.43 | 41.42 | subtotal |

ZERO_STANDING check: no line item on either statement is 0/nil/dash across all four periods. None enumerated with `ZERO_STANDING` this cycle (explicitly recorded, not silently omitted).

---

## TABLE G — Categories Not Present in This Doctype (recorded explicitly per rule)

| Category | Status |
|---|---|
| Numbered notes / footnote-to-accounts schedule | 0 / not present (this is an investor presentation, not the results filing) |
| Board Outcome agenda items | 0 / not present (covered in `ledger_boardoutcome_ganecos_q1fy27.md`) |
| Auditor report paragraphs (opinion, EOM, Other Matters, Going Concern, UDIN) | 0 / not present |
| Formal consolidation-scope entity list (with relationship type, cross-checked to prior quarter) | 0 formal schedule; 3 subsidiaries named qualitatively on slide 15 (Ganesha Ecopet Pvt Ltd, Ganesha Ecotech Pvt Ltd, Ganesha Overseas Pvt Ltd), no ENTITY_CHANGE determinable without a prior-quarter presentation ledger to diff against |
| Digital signature blocks (results-filing style, multiple) | 1 found — on the cover transmittal letter only (slide 1, line 51–52), signatory Bharat Kumar Sajnani, timestamp 2026.08.03 21:08:12 — same-day as letter date, no pre-meeting-conclusion flag applicable (no board meeting times disclosed on these slides) |
| Concall turns / questions / repeat-question flags / management spoken numbers | 0 / not present (concall doctype not in scope of this ledger) |

---

## TABLE H — DROPPED_SLIDE Check

No prior-quarter presentation ledger or extract exists in `runs/ganecos-q4fy26/` (only `extract_results_ganecos_q4fy26.txt` is present; no presentation PDF was processed that quarter per repo contents checked at enumeration time). Comparison flagged `PRIOR_LEDGER_UNAVAILABLE` — cannot assert any slide was dropped or added this quarter. This should be surfaced to A3/A4 as a coverage gap for trend-continuity checks, not treated as a clean pass.

---

## SUMMARY OF FLAGS RAISED

- `CHART_ORDER_APPROX` — bar-chart numeric labels on slides 6–11 and 18 are enumerated as printed; text-layer extraction does not guarantee value-to-period axis alignment. 18 instances (see Table B).
- `GUIDANCE` — 7 distinct forward-looking/target numeric or capacity-expansion disclosures (Table E), to be cross-checked against the filing and prior-quarter guidance at A3/A4.
- `NUMBER_DISCREPANCY` — standalone Other Income Q1FY27: bullet commentary states ₹3.53 crore (slide 12, line 306) vs P&L table ₹3.52 crore (slide 33, line 695). 0.01cr rounding gap.
- `PRIOR_LEDGER_UNAVAILABLE` — DROPPED_SLIDE check could not be run; no prior-quarter presentation ledger exists to diff against.
- Tax Expense sign-convention note on standalone P&L Q1FY27 (line 706) flagged for A3 review (positive tax charge vs consolidated's tax credit pattern across periods) — not an enumeration error, recorded for interpretive follow-up.

Total enumerated disclosure-unit rows across Tables B–F: 34 slides + 45 chart/table metric clusters (Table B) + 60 textual/qualitative units (Table C) + 6 footnotes (Table D) + 7 guidance units (Table E, subset already counted in B/C) + 28 P&L line items (Table F) = ledger is exhaustive per manual sweep; slide-count GATE A2 passes at 34 = 34 = 34.
