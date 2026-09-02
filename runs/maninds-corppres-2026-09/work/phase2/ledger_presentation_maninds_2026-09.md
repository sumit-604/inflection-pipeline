# A2 COMPLETENESS LEDGER — MANINDS Corporate Presentation (2026-09)

Source: A1 structured extraction only —
`runs/maninds-corppres-2026-09/extracted/maninds-presentation-2026-09-structured.md`
Count-test fallback used once (fulltext page-marker spine check) —
`runs/maninds-corppres-2026-09/extracted/maninds-presentation-2026-09-fulltext.md`
Prior-quarter ledger: none provided. DROPPED_SLIDE check not applicable this run.

```
=== A2 COUNT TEST ===
category: slides          grep_count: 37   sweep_count: 37   match: yes
category: numbers         grep_count: 223  sweep_count: 223  match: yes
category: entities        grep_count: 49   sweep_count: 49   match: yes
category: forward         grep_count: 20   sweep_count: 20   match: yes
category: dates           grep_count: 43   sweep_count: 43   match: yes
category: zero_standing   grep_count: 2    sweep_count: 2    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Method note. `grep_count` for numbers/entities/forward/dates = `grep -c "| TYPE |"`
against the structured file, cross-checked against the file's own `## COUNTS`
header (223 / 49 (40+9) / 20 / 43 — identical). `sweep_count` = manual
row-by-row read of all four category tables during ledger construction, same
totals. `slides`: grep_count = unique `[page N]` markers in A1 fulltext (37,
the only count-test use of fulltext, per rule 5, to confirm the structured
file's own claim of "all 37 physical pages accounted for"); sweep_count = 37
rows built below (34 data-bearing pages present in the structured file's
per-page groupings + 3 no-data divider pages named in the structured file's
RENDER/COVERAGE NOTES: pages 3, 27, 33). `zero_standing`: both counting
methods find the same two flagged rows on page 30.

---
## 1. SLIDE INVENTORY (37 slides / physical pages)

Content type inferred from the structured file's per-page row content
(NUMBER/ENTITY/FORWARD/DATE groupings and the RENDER/COVERAGE NOTES). Title
is a descriptive label built from the same context fields; the structured
file does not carry a separate literal slide-title field.

| Slide | Inferred title | Content type | Flags |
|---|---|---|---|
| 1 | Regulatory intimation cover letter (Reg 30 SEBI LODR) | text | — |
| 2 | Corporate Presentation title slide, Sep 2026 | text | — |
| 3 | Section divider (no data) | text (divider) | ZERO_STANDING (no-data slide, template signal) |
| 4 | Growth trajectory / key financial highlights FY22→FY26 | table + text | — |
| 5 | Manufacturing capacity overview: India + KSA (Dammam) + Jammu | text + table | — |
| 6 | Facility / office location world map | photo (map graphic) | — |
| 7 | Company journey timeline, 1996–2025 (era bands) | chart (timeline) | — |
| 8 | Board of Directors & senior management profiles | text + photo | — |
| 9 | Manufacturing facilities overview (land, capacity, certifications) | text | — |
| 10 | LSAW product & process specifications | table | — |
| 11 | HSAW product & process specifications | table | — |
| 12 | ERW / Hollow Section specifications | table | — |
| 13 | Internal coating & CWC specifications | table | — |
| 14 | Domestic & international client logo roster | photo (logo grid, no text layer) | ENTITY-SUMMARY (materiality-grouped) |
| 15 | Accolades & certifications roster | photo (logo grid, no text layer) | ENTITY-SUMMARY (materiality-grouped) |
| 16 | Jammu Stainless Steel Plant status update | text + table | — |
| 17 | Merino Shelters real-estate monetization update | text + table | — |
| 18 | Section divider: National Pipe Company (NPC), Saudi Arabia acquisition | text (divider) | — |
| 19 | NPC transaction overview | table | — |
| 20 | MISIC / NPC ownership & financing structure (restated) | table | — |
| 21 | NPC plant & capacity details (restated) | table | — |
| 22 | NPC client relationships (Saudi Aramco + others) | text + table | — |
| 23 | NPC EPC contractor roster | photo/text roster | ENTITY-SUMMARY (materiality-grouped) |
| 24 | Acquire vs Greenfield route comparison | table + chart | — |
| 25 | NPC acquisition strategic rationale / synergies | text | — |
| 26 | NPC CY2025 financial summary (P&L, BS extracts, ratios) | table | — |
| 27 | Section divider (no data) | text (divider) | ZERO_STANDING (no-data slide, template signal) |
| 28 | Standalone financial results, FY26 vs FY25 | table | — |
| 29 | Consolidated financial results, FY26 vs FY25 | table | — |
| 30 | Consolidated balance sheet, FY24–FY26 | table | ZERO_STANDING x2 (line items below) |
| 31 | Historical financial summary, FY23–FY26 | table | — |
| 32 | Quarterly trend, Q1 FY26–Q1 FY27 (incl. NPC consolidation note) | chart | — |
| 33 | Section divider (no data) | text (divider) | ZERO_STANDING (no-data slide, template signal) |
| 34 | 5-year strategic goals & targets | text | — |
| 35 | Glossary of abbreviations | text | ENTITY-SUMMARY (materiality-grouped) |
| 36 | Safe-harbor / forward-looking statement disclaimer | text | ENTITY-SUMMARY (materiality-grouped) |
| 37 | Investor contact details | text | — |

DROPPED_SLIDE check: no prior-quarter ledger supplied for this run, so no
slide-level diff was possible. Flagged for A3/A4 awareness, not a gate
failure (input not available, not a discovered gap).

---
## 2. NUMBER LEDGER (223 rows)

Every NUMBER row from A1's structured extraction, one row per line, page and
line number carried exactly as extracted. Verbatim value and context
preserved; flags column added where a standing/zero condition applies.

| # | Page | Line | Value | Context | Flags |
|---|---|---|---|---|---|
| 1 | 1 | 11 | Scrip Code: 513269 | BSE scrip code | — |
| 2 | 2 | 54 | 2026 | presentation title year (also DATE) | — |
| 3 | 4 | 65 | 3 | decades of experience | — |
| 4 | 4 | 65 | 1.6Mn+ MTPA* | API grade LSAW/HSAW/ERW/Coating capacity | footnote marker, resolved by row #21 |
| 5 | 4 | 65 | ₹2,178 Cr | FY22 Revenue | — |
| 6 | 4 | 65 | ₹3,592 Cr | FY26 Revenue | — |
| 7 | 4 | 64 | CAGR – 13.4% | Revenue CAGR FY22-FY26 | — |
| 8 | 4 | 71 | 3 | state of the art manufacturing facilities | — |
| 9 | 4 | 71 | 30+ | countries presence | — |
| 10 | 4 | 72 | ₹218 Cr | FY22 EBITDA | — |
| 11 | 4 | 72 | ₹468 Cr | FY26 EBITDA | — |
| 12 | 4 | 70 | CAGR – 21.0% | EBITDA CAGR FY22-FY26 | — |
| 13 | 4 | 78 | 10 | production lines | — |
| 14 | 4 | 78 | 20,000+KM | pipes supplied since inception | — |
| 15 | 4 | 80 | ₹102 Cr | FY22 PAT | — |
| 16 | 4 | 80 | ₹171 Cr | FY26 PAT | — |
| 17 | 4 | 78 | CAGR – 13.8% | PAT CAGR FY22-FY26 | — |
| 18 | 4 | 86 | 18.4% | FY26 ROCE | — |
| 19 | 4 | 86 | 9.2% | FY26 ROE | — |
| 20 | 4 | 86 | ₹2,087 Cr | FY26 Networth | — |
| 21 | 4 | 92 | 0.43Mn MTPA | footnote: NPC capacity within 1.6Mn MTPA total | resolves row #4 |
| 22 | 5 | 105 | 1.2Mn+ MTPA | India pipe capacity | — |
| 23 | 5 | 105 | 430,000 MTPA | NPC Saudi Arabia acquired pipe capacity | — |
| 24 | 5 | 109 | 250k MT HSAW | NPC HSAW capacity component | — |
| 25 | 5 | 109 | 180k MT LSAW | NPC LSAW capacity component | — |
| 26 | 5 | 115 | ₹3,564 Cr | revenue delivered in FY26, India ops | — |
| 27 | 5 | 124 | 4.0 Mn sq.m | Dammam Coating Plant (KSA) capacity | — |
| 28 | 5 | 124 | 22,000 MTPA | Jammu Stainless Steel Plant capacity | — |
| 29 | 7 | 150-152 | 50,000 TPA | LSAW pipe plant capacity, Pithampur (1996) | — |
| 30 | 7 | 155-156 | 50,000 TPA | HSAW Plant capacity established (1999) | — |
| 31 | 7 | 156-158 | 135,000 TPA | LSAW capacity increased to (1999) | — |
| 32 | 7 | 150-151 | USD 225mn | order received from USA (2007) | — |
| 33 | 7 | 153 | 200,000 MT each | two new HSAW lines added (2007) | — |
| 34 | 7 | 149-153 | 80-inch diameter | pipe exported, first Indian company (2019) | — |
| 35 | 7 | 151 | 18-mtr-long | pipe length exported (2019) | — |
| 36 | 7 | 152 | 24mm thickness | pipe wall thickness exported (2019) | — |
| 37 | 7 | 151-152 | 5-year | MoU term with Aramco Asia India (2019) | — |
| 38 | 7 | 157-158 | 1,25,000 TPA | ERW unit capacity, Anjar, Gujarat (2023) | — |
| 39 | 7 | 155-159 | 100% | equity stake acquired in NPC (2023) | — |
| 40 | 7 | 159 | USD 102 Mn | consideration for NPC acquisition (2023) | — |
| 41 | 7 | 159 | ~₹1,000 Cr | INR-equivalent consideration for NPC acquisition (2023) | — |
| 42 | 7 | 168-169 | 50,000 TPA | additional ERW capacity added (2024) | — |
| 43 | 7 | 181,183 | 2mn & 1.6mn sq.mtr. | coating plant (PE & CTE) capacity (2001) | — |
| 44 | 7 | 187-188 | 365,000 TPA | new pipe & coating complex LSAW capacity, Anjar (2005) | — |
| 45 | 7 | 194-195 | 7MW | windmill installed, Gujarat, captive consumption (2006) | — |
| 46 | 7 | 182,184 | 5,600 Ton | Hydraulic JCO press commissioned, Gujarat (2016) | — |
| 47 | 7 | 190,193 | 1,25,000 cubic meters p.a. | CWC Plant capacity, offshore pipe projects (2017) | — |
| 48 | 7 | 182,185-186 | 50,000 TPA | Spiral Mill & PU Coating capacity expansion, Pithampur (2025) | — |
| 49 | 8 | 207 | over four decade(s) | Dr. Mansukhani's industrial experience | — |
| 50 | 8 | 213-214 | 50 years | Dr. Mansukhani's manufacturing/Man Group tenure | — |
| 51 | 8 | 211 | over 9+ years | Nikhil Mansukhani's steel pipes industry experience | — |
| 52 | 8 | 224 | over four decades | Narendra Mairpady's banking experience | — |
| 53 | 8 | 236-237 | over 33 years | Esha Padmanabhan Achan's finance experience | — |
| 54 | 9 | 248 | ~182 acres | combined manufacturing facility land area | — |
| 55 | 9 | 249 | exceeding 1.2 million tonnes per annum (TPA) | combined manufacturing capacity | — |
| 56 | 10 | 274 | 16" to 56" | LSAW Outside Diameter range | — |
| 57 | 10 | 275 | 6 mm to 55 mm | LSAW Wall Thickness range | — |
| 58 | 10 | 277 | 12.20 Meters | LSAW Pipe Length (max) | — |
| 59 | 10 | 279 | Up to API 5L X-80 | LSAW Grade | — |
| 60 | 11 | 299 | 12" to 120" | HSAW Outside Diameter range | — |
| 61 | 11 | 301 | 6 mm to 25.40 mm | HSAW Wall Thickness range | — |
| 62 | 11 | 302 | 18 meters | HSAW Pipe Length (max) | — |
| 63 | 11 | 303 | Up to API 5L X-80 | HSAW Grade | — |
| 64 | 12 | 330 | 32 ton | coil weight handled by entry section | — |
| 65 | 12 | 334 | 100% coverage with 10% overlap | Strip Ultrasonic testing coverage | — |
| 66 | 12 | 341 | High Frequency (1000 KW) | ERW welding power | — |
| 67 | 12 | 346-348 | 132x132 to 350x350 and 172x92 to 500x200 & 450x250 | Square/Rectangular Hollow Section size range | — |
| 68 | 12 | 350 | 4.0 to 14.0 mm | Wall Thickness, hollow section | — |
| 69 | 12 | 352 | 5.8 to 18.2 Meter | Pipe Length range | — |
| 70 | 12 | 354 | IS: 4923, DIN 2440 | Grade standards, hollow section | — |
| 71 | 13 | 369 | 12″ to 130″ and above | Internal Coating Pipe Diameter range | — |
| 72 | 13 | 371 | 5 million sq. meters per annum | Internal coating plant capacity | — |
| 73 | 13 | 376 | Ø 8" to Ø 56" | CWC Pipe OD Range | — |
| 74 | 13 | 377 | 6 mm – 55.0 mm | CWC Pipe Wall Thickness | — |
| 75 | 13 | 378 | 9 to 12.2 meter | CWC Pipe Length | — |
| 76 | 13 | 379 | 30 to 190 mm | CWC Concrete Thickness | — |
| 77 | 13 | 380 | 100m3/Hrn | CWC Coating Capacity | — |
| 78 | 16 | 418 | 22,000 MTPA | Jammu stainless steel seamless pipe capacity | — |
| 79 | 16 | 418 | ₹350Crs | Jammu capex incurred, till Q1 FY27 | — |
| 80 | 16 | 419 | ~₹600 Cr | Jammu total planned capex | — |
| 81 | 17 | 431 | 6 Acres | Merino Shelters land, Opp. D.Y Patil Stadium | — |
| 82 | 17 | 431 | 30% | company's share of profit in developed-area sale | — |
| 83 | 17 | 431 | Rs.70 Cr | upfront amount received after JDA | — |
| 84 | 17 | 431 | Rs. 80-120 Cr | annual cashflow expected, Merino Shelters | — |
| 85 | 17 | 445 | ~20,00,000 sq. ft | Commencement Certificate area, RERA registered | — |
| 86 | 19 | 466-468 | 100% | Stake Acquired (NPC transaction) | — |
| 87 | 19 | 465,469 | 430,000 MT | Annual Production Capacity (HSAW+LSAW) | — |
| 88 | 19 | 466 | more than two decades | Aramco approval duration | — |
| 89 | 19 | 484 | 100% equity stake | Transaction Type description | — |
| 90 | 19 | 482-483 | crosses 1.2M MT | combined NPC + Man Group capacity | — |
| 91 | 19 | 487 | USD 102 Million | Total Consideration | — |
| 92 | 19 | 489 | USD 70 million | Debt financing component | — |
| 93 | 19 | 489 | USD 32 Million | Equity financing component | — |
| 94 | 19 | 491 | USD 83.0 Million | Cash & Liquid Assets | — |
| 95 | 19 | 491-492 | USD 158.6 Million | Net worth | — |
| 96 | 20 | 509-510 | 100% ownership | MISIC ownership by MAN Industries | — |
| 97 | 20 | 508 | USD 102 Mn | acquisition amount (restated) | — |
| 98 | 20 | 521 | USD 32 Mn | Equity financing (restated) | — |
| 99 | 20 | 521 | USD 70 Mn | Debt financing (restated) | — |
| 100 | 20 | 521 | USD 102 Mn | Total financing (restated) | — |
| 101 | 21 | 531 | 430,000 MT | NPC Annual Installed Capacity (restated) | — |
| 102 | 21 | 530,532 | 1 HSAW & 1 LSAW Mill | Fully Integrated Plants | — |
| 103 | 21 | 531,533 | 2+ Decades | Relationship with Saudi Aramco | — |
| 104 | 21 | 540 | 430,000 MTPA | Total Installed Capacity (restated) | — |
| 105 | 21 | 543,545,547 | 250,000 MT (58% of total capacity) | HSAW Pipes capacity | — |
| 106 | 21 | 550,552,554 | 180,000 MT (42% of total capacity) | LSAW Pipes capacity | — |
| 107 | 21 | 559 | 20"–88" (Will be Upgraded to 120") | HSAW OD range | — |
| 108 | 21 | 561 | 24"–60" | LSAW OD range | — |
| 109 | 21 | 561-563 | 6.4 mm – 45 mm | Wall Thickness range, NPC | — |
| 110 | 22 | 579 | 40+ Years | Saudi Aramco relationship length (NPC direct client) | — |
| 111 | 24 | 631 | ~US$102 Mn (US$70 Mn debt + US$32 Mn equity) | Acquire route capital outlay | — |
| 112 | 24 | 630-632 | ₹1,500–1,600 Cr | Greenfield route capital outlay (comparison) | — |
| 113 | 24 | 633 | US$83 Mn | cash & liquid assets, "what money buys" (Acquire) | — |
| 114 | 24 | 641 | US$120 Mn | Order book on day one, Acquire route | — |
| 115 | 24 | 643 | 15-18% | Acquire route EBITDA Margin | — |
| 116 | 24 | 643 | 11-14% | Acquire route PAT margin | — |
| 117 | 25 | 665-666 | ~1.60 MTPA | combined steel procurement, cost synergies | — |
| 118 | 25 | 695-696 | US$83 Mn | cash & liquid assets, capital-efficient structure | — |
| 119 | 25 | 696 | US$120 Mn | order book (restated) | — |
| 120 | 26 | 711 | Revenue SAR 792.7M / USD 211.4M | CY2025 P&L | — |
| 121 | 26 | 712 | Gross Profit SAR 214.1M / USD 57.1M | CY2025 P&L | — |
| 122 | 26 | 713 | 27.0% | Gross Margin CY2025 | — |
| 123 | 26 | 714 | EBITDA SAR 196.7M / USD 52.5M | CY2025 P&L | — |
| 124 | 26 | 715 | 24.8% | EBITDA Margin CY2025 | — |
| 125 | 26 | 716 | Depreciation SAR 31.8M / USD 8.5M | CY2025 P&L | — |
| 126 | 26 | 717 | EBIT SAR 164.9M / USD 44.0M | CY2025 P&L | — |
| 127 | 26 | 719 | 20.8% | EBIT Margin CY2025 | — |
| 128 | 26 | 720 | Finance Cost SAR 3.7M / USD 1.0M | CY2025 P&L | — |
| 129 | 26 | 721 | Other Income SAR 0.8M / USD 0.2M | CY2025 P&L | — |
| 130 | 26 | 723 | PBT SAR 162.0M / USD 43.2M | CY2025 P&L | — |
| 131 | 26 | 725 | 20.4% | PBT Margin CY2025 | — |
| 132 | 26 | 727 | Tax & Zakat SAR 18.5M / USD 4.9M | CY2025 P&L | — |
| 133 | 26 | 728 | 11.4% | Tax Rate CY2025 | — |
| 134 | 26 | 730 | PAT SAR 143.5M / USD 38.3M | CY2025 P&L | — |
| 135 | 26 | 732 | 18.1% | PAT Margin CY2025 | — |
| 136 | 26 | 712 | Cash & Bank Balances SAR 142.5M / USD 38.0M | as of Apr'2026 | — |
| 137 | 26 | 713 | Trade Receivables SAR 48.8M / USD 13.0M | as of Apr'2026 | — |
| 138 | 26 | 714 | Finished Goods Inventory SAR 120.0M / USD 32.0M | as of Apr'2026 | — |
| 139 | 26 | 715 | Total Cash & Liquid Assets SAR 311.3M / USD 83.0M | as of Apr'2026 | — |
| 140 | 26 | 716 | Net Worth SAR 594.9M / USD 158.6M | as of Apr'2026 | — |
| 141 | 26 | 722 | 25.7% | ROE CY2025 | — |
| 142 | 26 | 724 | 29.5% | ROCE CY2025 | — |
| 143 | 26 | 726 | 22.5% | ROA CY2025 | — |
| 144 | 26 | 729-730 | USD 120 Million (₹1,130–1,150 crore) | order position at time of acquisition | — |
| 145 | 26 | 736 | SAR/INR: 23.955 | disclosed FX rate | — |
| 146 | 26 | 736 | SAR/USD: 3.75 | disclosed FX rate (pegged) | — |
| 147 | 26 | 736 | INR ~1,898.9 Cr | CY2025 Revenue, INR equivalent | — |
| 148 | 26 | 736 | INR ~343.6 Cr | CY2025 PAT, INR equivalent | — |
| 149 | 28 | 749 | Revenue from Operations FY26 34,552 / FY25 31,182, YoY 10.8% | standalone, INR Mn | — |
| 150 | 28 | 751 | Other Income FY26 531 / FY25 542, YoY (2.0)% | standalone, INR Mn | — |
| 151 | 28 | 753 | Total Income FY26 35,083 / FY25 31,724, YoY 10.6% | standalone, INR Mn | — |
| 152 | 28 | 755 | Operating expenses FY26 30,155 / FY25 28,415, YoY 6.1% | standalone, INR Mn | — |
| 153 | 28 | 757 | EBITDA* FY26 4,928 / FY25 3,309, YoY 48.9% | standalone, INR Mn | footnote marker `*`, no defining footnote text captured — FOOTNOTE_UNRESOLVED |
| 154 | 28 | 759 | EBITDA Margins FY26 14.0% / FY25 10.4%, +360 Bps | standalone | — |
| 155 | 28 | 761 | Depreciation & amortization FY26 756 / FY25 433, YoY 74.6% | standalone, INR Mn | — |
| 156 | 28 | 763 | Finance costs FY26 1,542 / FY25 1,022, YoY 50.9% | standalone, INR Mn | — |
| 157 | 28 | 765 | PBT FY26 2,630 / FY25 1,854, YoY 41.8% | standalone, INR Mn | — |
| 158 | 28 | 767 | Tax FY26 672 / FY25 484, YoY 39.0% | standalone, INR Mn | — |
| 159 | 28 | 769 | PAT FY26 1,958 / FY25 1,370, YoY 42.8% | standalone, INR Mn | — |
| 160 | 28 | 771 | PAT Margins FY26 5.6% / FY25 4.3%, +130 Bps | standalone | — |
| 161 | 29 | 786 | Revenue from Operations FY26 35,639 / FY25 35,054, YoY 1.7% | consolidated, INR Mn | — |
| 162 | 29 | 788 | Other Income FY26 286 / FY25 200, YoY 43.2% | consolidated, INR Mn | — |
| 163 | 29 | 790 | Total Income FY26 35,925 / FY25 35,253, YoY 1.9% | consolidated, INR Mn | — |
| 164 | 29 | 792 | Operating expenses FY26 31,246 / FY25 31,690, YoY (1.4)% | consolidated, INR Mn | — |
| 165 | 29 | 794 | EBITDA* FY26 4,679 / FY25 3,563, YoY 31.3% | consolidated, INR Mn | footnote marker `*`, no defining footnote text captured — FOOTNOTE_UNRESOLVED |
| 166 | 29 | 796 | EBITDA Margins FY26 13.0% / FY25 10.1%, +290 Bps | consolidated | — |
| 167 | 29 | 798 | Depreciation & amortization FY26 789 / FY25 453, YoY 74.4% | consolidated, INR Mn | — |
| 168 | 29 | 800 | Finance costs FY26 1,520 / FY25 1,027, YoY 48.1% | consolidated, INR Mn | — |
| 169 | 29 | 802 | PBT FY26 2,370 / FY25 2,084, YoY 13.7% | consolidated, INR Mn | — |
| 170 | 29 | 804 | Tax FY26 665 / FY25 552, YoY 20.4% | consolidated, INR Mn | — |
| 171 | 29 | 806 | PAT FY26 1,705 / FY25 1,532, YoY 11.3% | consolidated, INR Mn | — |
| 172 | 29 | 808 | PAT Margins FY26 4.7% / FY25 4.3%, +40 Bps | consolidated | — |
| 173 | 30 | 823 | Equity Share Capital FY24 324 / FY25 324 / FY26 375 | consolidated BS, INR Mn | — |
| 174 | 30 | 825 | Other Equity FY24 13,725 / FY25 15,749 / FY26 20,490 | consolidated BS | — |
| 175 | 30 | 827 | Shareholders Fund FY24 14,049 / FY25 16,073 / FY26 20,865 | consolidated BS | — |
| 176 | 30 | 831 | Long-term Borrowings FY24 1,363 / FY25 1,385 / FY26 2,402 | consolidated BS | — |
| 177 | 30 | 832 | Lease Liabilities (non-current) FY24 141 / FY25 156 / FY26 610 | consolidated BS | — |
| 178 | 30 | 833 | Deferred tax liabilities (net) FY24 258 / FY25 276 / FY26 258 | consolidated BS | — |
| 179 | 30 | 835 | Other long term liabilities FY24 42 / FY25 73 / FY26 97 | consolidated BS | — |
| 180 | 30 | 837 | Total Non-current Liabilities FY24 1,803 / FY25 1,890 / FY26 3,367 | consolidated BS | — |
| 181 | 30 | 841 | Short-term Borrowings FY24 1,722 / FY25 3,175 / FY26 2,595 | consolidated BS | — |
| 182 | 30 | 842 | Lease Liabilities (current) FY24 34 / FY25 47 / FY26 674 | consolidated BS | — |
| 183 | 30 | 843 | Trade payables FY24 5,028 / FY25 12,002 / FY26 14,712 | consolidated BS | — |
| 184 | 30 | 845 | Current tax liabilities FY24 54 / FY25 21 / FY26 275 | consolidated BS | — |
| 185 | 30 | 847 | Other financial liabilities FY24 278 / FY25 301 / FY26 5,797 | consolidated BS | — |
| 186 | 30 | 849 | Other current liabilities FY24 1,184 / FY25 4,283 / FY26 1,921 | consolidated BS | — |
| 187 | 30 | 851 | Total Current Liabilities FY24 8,300 / FY25 19,829 / FY26 25,974 | consolidated BS | — |
| 188 | 30 | 852 | Total Equity and Liabilities FY24 24,152 / FY25 37,792 / FY26 50,206 | consolidated BS | — |
| 189 | 30 | 824 | Property, Plant and Equipment FY24 5,234 / FY25 5,539 / FY26 6,546 | consolidated BS assets | — |
| 190 | 30 | 826 | Right-of-use Assets FY24 163 / FY25 186 / FY26 1,389 | consolidated BS assets | — |
| 191 | 30 | 828 | Capital WIP FY24 305 / FY25 1,334 / FY26 3,258 | consolidated BS assets | — |
| 192 | 30 | 829 | Goodwill on Consolidation FY24 639 / FY25 688 / FY26 688 | consolidated BS assets | — |
| 193 | 30 | 830 | Investment Properties FY24 14 / FY25 14 / FY26 14 | consolidated BS assets | — |
| 194 | 30 | 831 | Intangible assets FY24 - / FY25 5 / FY26 3 | consolidated BS assets | ZERO_STANDING (FY24) |
| 195 | 30 | 832 | Trade Receivables (non-current) FY24 967 / FY25 973 / FY26 2,385 | consolidated BS assets | — |
| 196 | 30 | 833 | Other Financial Assets (non-current) FY24 173 / FY25 524 / FY26 154 | consolidated BS assets | — |
| 197 | 30 | 834 | Other Non-current Assets FY24 658 / FY25 1,023 / FY26 438 | consolidated BS assets | — |
| 198 | 30 | 836 | Total non-current assets FY24 8,154 / FY25 10,286 / FY26 14,875 | consolidated BS assets | — |
| 199 | 30 | 840 | Inventories FY24 6,456 / FY25 12,685 / FY26 15,350 | consolidated BS assets | — |
| 200 | 30 | 841 | Investments FY24 2,280 / FY25 260 / FY26 708 | consolidated BS assets | — |
| 201 | 30 | 842 | Trade Receivables (current) FY24 3,551 / FY25 8,959 / FY26 10,098 | consolidated BS assets | — |
| 202 | 30 | 843 | Cash & Bank Balances FY24 2,549 / FY25 3,792 / FY26 6,572 | consolidated BS assets | — |
| 203 | 30 | 844 | Loans FY24 22 / FY25 2 / FY26 157 | consolidated BS assets | — |
| 204 | 30 | 846 | Other Financial Assets (current) FY24 105 / FY25 98 / FY26 201 | consolidated BS assets | — |
| 205 | 30 | 848 | Other Current Assets FY24 1,035 / FY25 1,710 / FY26 2,245 | consolidated BS assets | — |
| 206 | 30 | 850 | Current Tax Assets FY24 - / FY25 - / FY26 - | consolidated BS assets | ZERO_STANDING (all 3 years) |
| 207 | 30 | 851 | Total Current Assets FY24 15,998 / FY25 27,506 / FY26 35,331 | consolidated BS assets | — |
| 208 | 30 | 852 | Total Assets FY24 24,152 / FY25 37,792 / FY26 50,206 | consolidated BS assets | — |
| 209 | 31 | 867 | Total Income FY23 22,703 / FY24 31,942 / FY25 35,253 / FY26 35,925 | historical, INR Mn | — |
| 210 | 31 | 866-869 | Gross Profit FY23 4,973 / FY24 7,907 / FY25 7,905 / FY26 13,639 | historical, INR Mn | — |
| 211 | 31 | 869-870 | Gross Profit Margin FY23 21.9% / FY24 24.8% / FY25 22.4% / FY26 38.0% | historical | — |
| 212 | 31 | 881-883 | EBITDA FY23 1,760 / FY24 2,932 / FY25 3,563 / FY26 4,679 | historical, INR Mn | — |
| 213 | 31 | 883-885 | EBITDA Margins FY23 7.8% / FY24 9.2% / FY25 10.1% / FY26 13.0% | historical | — |
| 214 | 31 | 879-882 | PAT FY23 670 / FY24 1,051 / FY25 1,532 / FY26 1,705 | historical, INR Mn | — |
| 215 | 31 | 885-886 | PAT Margins FY23 3.0% / FY24 3.3% / FY25 4.3% / FY26 4.7% | historical | — |
| 216 | 32 | 900,901,903 | Total Income Q1FY26 7,736 / Q2FY26 8,148 / Q3FY26 8,386 / Q4FY26 11,655 / Q1FY27 10,650 | quarterly trend, INR Mn | — |
| 217 | 32 | 899,904-909 | Gross Profit & Margin bar-chart: 6,269; 3,820; 3,409; 1,833; 2,128; margins 53.8%; 40.6%; 35.9%; 23.7%; 26.1% | quarterly trend Q1FY26-Q1FY27 | per-quarter mapping not resolvable from flattened layout (A1 note) |
| 218 | 32 | 917-927 | EBITDA & Margin bar-chart: 806; 1,018; 1,376; 1,480; 1,553; margins 10.4%; 12.5%; 16.4%; 12.7%; 14.6% | quarterly trend Q1FY26-Q1FY27 | per-quarter mapping not resolvable (A1 note) |
| 219 | 32 | 917-927 | PAT & Margin bar-chart: 276; 370; 550; 509; 614; margins 3.6%; 4.5%; 6.6%; 4.4%; 5.8% | quarterly trend Q1FY26-Q1FY27 | per-quarter mapping not resolvable (A1 note) |
| 220 | 32 | 935-938 | 40 days | NPC contribution period reflected in Q1 FY27 results | — |
| 221 | 34 | 965 | 20-25% | Revenue CAGR target, next 5 years | — |
| 222 | 34 | 970 | 15% | long-term stable EBITDA margin target | — |
| 223 | 37 | 1050 | +91 9619438448 | Vijay Gyanchandani contact number | — |

Zero-value / dash-valued standing line items enumerated per rule 3: rows
#194 and #206 above. Both are template signals inside the consolidated
balance sheet (page 30) — the line exists across all three comparison years
because the item type recurs (Intangible assets goes from nil to non-zero
across FY24→FY26; Current Tax Assets stays nil across all three years shown)
— never dropped.

---
## 3. ENTITY LEDGER (49 rows: 40 individual + 9 ENTITY-SUMMARY)

| # | Page | Line | Entity | Context | Flags |
|---|---|---|---|---|---|
| 1 | 1 | 4 | BSE Limited | filing recipient, stock exchange | — |
| 2 | 1 | 5 | National Stock Exchange of India Ltd. | filing recipient, stock exchange | — |
| 3 | 1 | 11 | MANINDS | NSE scrip ID | — |
| 4 | 1 | 29 | Man Industries (India) Limited | issuer company (self) | — |
| 5 | 1 | 47 | Rahul Rawat, Company Secretary | signing officer / KMP | — |
| 6 | 5 | 109 | Anjar (Gujarat) plant | operating facility | — |
| 7 | 5 | 109 | Pithampur (M.P.) plant | operating facility | — |
| 8 | 5 | 112 | Saudi Aramco | Aramco-approved vendor status referenced | — |
| 9 | 5 | 124 | Dammam Coating Plant (KSA) | greenfield facility under construction | — |
| 10 | 5 | 124 | Jammu Stainless Steel Plant | greenfield facility under construction | — |
| 11 | 6 | 138,143,145 | ENTITY-SUMMARY: world map graphic (MP/Pithampur marker, NPC office marker) | facility/office location map | ENTITY-SUMMARY |
| 12 | 7 | 151-152 | Aramco Asia India | 5-year MoU counterparty (2019) | — |
| 13 | 7 | 156,158 | Kobe Steel Ltd., Japan | strategic relationship counterparty (2012) | — |
| 14 | 7 | 156,159 | National Pipe Company (NPC), Saudi Arabia | acquisition target (2023) | — |
| 15 | 7 | 165,167 | MISIC (MAN International Steel Industries Company) | wholly-owned acquisition vehicle | — |
| 16 | 7 | 189,191 | Qatar Energy LNG | certified vendor status approved (2025) | — |
| 17 | 7 | 194-195 | Merino Shelters Real Estate | asset monetized (2025) | — |
| 18 | 8 | 204-215 | Dr. Ramesh C. Mansukhani, Chairman | promoter/director | — |
| 19 | 8 | 204,207-215 | Mr. Nikhil Mansukhani, Managing Director | promoter/director | — |
| 20 | 8 | 221-230 | Mr. Narendra Mairpady, Non-Exec. Independent Director | Ex-Chairman Indian Overseas Bank | — |
| 21 | 8 | 221,223-232 | Mr. Rabi Bastia (Padma Shri Dr. Rabi Narayan Bastia), Non-Exec. Independent Director | hydrocarbon industry veteran | — |
| 22 | 8 | 234-238 | Mrs. Renu Jalan, Non-Exec. Independent Director | Arts/Marketing/Finance experience | — |
| 23 | 8 | 234,236-239 | Mrs. Esha Padmanabhan Achan, Non-Exec. Independent Director | ex-Glenmark, ex-Bajaj finance professional | — |
| 24 | 8 | 221 | Mr. Sandeep Kumar Garg, Chief Financial Officer | KMP - CFO | — |
| 25 | 8 | 221 | Mr. Jaspreet Bhatia, Sr. VP - Operations | senior management | — |
| 26 | 8 | 225,227 | Mr. Swatantra Joshi, Plant Head - Anjar Facility | senior management | — |
| 27 | 8 | 232-233 | Mr. Sushil Shukla, Plant Head - Pithampur Facility | senior management | — |
| 28 | 9 | 247-248 | Anjar, Kutch District, Gujarat plant | manufacturing facility | — |
| 29 | 9 | 247-248 | Pithampur, Madhya Pradesh plant | manufacturing facility | — |
| 30 | 9 | 251 | ENTITY-SUMMARY: certifications ISO 9001:2015, ISO 14001:2015, ISO 45001:2018 | quality certification list | ENTITY-SUMMARY |
| 31 | 10 | 285-286 | CHR Haeusler of Switzerland | equipment supplier | — |
| 32 | 14 | 390 | ENTITY-SUMMARY: Domestic & International Clients logo roster (names not extractable, image logos) | customer logo roster slide | ENTITY-SUMMARY |
| 33 | 15 | 397 | ENTITY-SUMMARY: accolades & certifications roster (image logos, no text layer) | award/certification roster slide | ENTITY-SUMMARY |
| 34 | 17 | 440-441 | Merino Shelters Private Ltd | wholly owned subsidiary | — |
| 35 | 17 | 439-441 | Paradise Green-Spaces LLP (Paradise Group) | JDA counterparty | — |
| 36 | 18 | 452 | National Pipe Company Saudi Arabia (KSA) | acquisition target (divider slide) | — |
| 37 | 19 | 476-477 | MAN International Steel Industries Company (MISIC) | acquirer, wholly owned subsidiary | — |
| 38 | 19 | 480-482 | National Pipe Company Limited (NPC), Kingdom of Saudi Arabia | acquisition target | — |
| 39 | 20 | 504-508 | MAN Industries (India) Limited | acquirer parent, BSE:513269, NSE:MANINDS | — |
| 40 | 20 | 506 | National Pipe Company (NPC), KSA | acquisition target, 100% stake | — |
| 41 | 22 | 578-579 | Saudi Aramco | Primary Client, 40+ Years (NPC direct client) | — |
| 42 | 22 | 578-586 | ENTITY-SUMMARY: NPC direct client roster (KOC, Qatar Petroleum, Bapco Refining, Saudi Water Authority, SWPC, WTTCO, National Water Co., ADWEA) | client roster, no distinct facts per member | ENTITY-SUMMARY |
| 43 | 23 | 604-612 | ENTITY-SUMMARY: NPC EPC contractor roster (McDermott, L&T, SAIPEM, Subsea 7, Hyundai E&C, Sapura, Petrofac, Lamprell, NPCC, S.S.E.M.) | EPC partner roster | ENTITY-SUMMARY |
| 44 | 25 | 688-689 | KOC, Qatar Energy, Bapco | long-standing NPC customer relationships named | — |
| 45 | 35 | 983-1005 | ENTITY-SUMMARY: glossary of abbreviations (API, FBE, DEBE, CWC, NDT, CNC, GMAW, LPE, LPP, ERW, HSAW, LSAW) | glossary slide | ENTITY-SUMMARY |
| 46 | 36 | 1013-1037 | ENTITY-SUMMARY: Man Industries safe-harbor / forward-looking statement disclaimer | legal disclaimer boilerplate | ENTITY-SUMMARY |
| 47 | 37 | 1048-1050 | Mr. Vijay Gyanchandani, DGM - Investor Relations | IR contact | — |
| 48 | 37 | 1048-1049 | Mr. Rahul Rawat, Company Secretary | IR contact (restated) | — |
| 49 | 37 | 1050-1051 | ENTITY-SUMMARY: contact email addresses (cs@maninds.org, Vijay.gyanchandani@maninds.org) | contact email block | ENTITY-SUMMARY |

ENTITY_CHANGE check: no prior-quarter entity list supplied for this run;
cross-check not possible. Flagged for A3/A4 awareness (not a gate failure).

---
## 4. FORWARD LEDGER (20 rows)

| # | Page | Line | Statement | Context |
|---|---|---|---|---|
| 1 | 5 | 124-125 | Dammam Coating Plant (KSA) - Production Targeted: Mar'2027 | commissioning target |
| 2 | 5 | 124-125 | Jammu Stainless Steel Plant - Production Targeted: Mar'2027 | commissioning target |
| 3 | 5 | 128-130 | Dammam coating plant adds value-added margin layer, completes delivered-pipe offering | strategic rationale, coating capacity add |
| 4 | 5 | 128-132 | Jammu plant: new product line, higher-margin mix; SS seamless mother/pilgered pipes targeting chemical, defence, marine, nuclear, power, refinery applications | strategic rationale, Jammu SS plant |
| 5 | 16 | 418-419 | Production starting March 2027 | Jammu plant production timeline |
| 6 | 17 | 433 | Annual Cashflow from FY28 | expected recurring cashflow start, Merino Shelters |
| 7 | 17 | 440 | Rs. 700-800 Cr Revenue in next 5-6 Years | Merino Shelters revenue projection |
| 8 | 17 | 445-446 | Project launch on track for Mid-September 2026 | Merino Shelters project launch timeline |
| 9 | 17 | 446 | Expected Rs. 35-50Cr Cashflow in FY27 | Merino Shelters cashflow guidance |
| 10 | 24 | 637 | Time to first revenue: Immediate (Acquire) vs Three years or more (Greenfield) | comparative revenue timing claim |
| 11 | 24 | 639 | Time to Aramco approval: Already held (Acquire) vs 1-2 years of plant audits and test lots (Greenfield) | comparative approval timing claim |
| 12 | 25 | 699 | Zero debt at closing | NPC balance sheet condition at acquisition |
| 13 | 25 | 692-696 | Acquisition unlocks immediate US$120 Mn order book, deeper Saudi market access, expands addressable order pipeline, lifts group profitability | acquisition value-creation thesis |
| 14 | 32 | 935-941 | Full financial impact and earnings contribution from NPC expected to be reflected from Q2 FY27 onwards | NPC consolidation ramp-up guidance |
| 15 | 34 | 947-951 | Optimize overall utilization by relocating spare capacity from India to markets with strong long term demand visibility, diversify into high-growth geographies, shift mix toward higher-margin products | 5-year strategic goal overview |
| 16 | 34 | 953-959 | Relocation of Spare Capacity: identify overseas locations with strong demand visibility, shift spare/underutilized equipment from India | strategic pillar 1 |
| 17 | 34 | 954-962 | Diversification into New Geographies: enter new high-growth markets using existing product offering, build local presence and ecosystem in target regions | strategic pillar 2 |
| 18 | 34 | 966-976 | Focus on Higher-Margin Products: prioritize Stainless Steel pipes as key growth product, increase value-added offerings (Coating, Bends); debottlenecking to enhance production and utilization | strategic pillar 3 |
| 19 | 34 | 965-966 | Revenue CAGR of 20-25%, led by relocation of spare capacity to high-demand markets and entry into new high-growth geographies | 5-year revenue growth target |
| 20 | 34 | 969-972 | Further improvement in EBITDA margin to a long-term stable rate of 15%, driven by higher utilization, higher Stainless Steel share, diversification | 5-year EBITDA margin target |

---
## 5. DATE LEDGER (43 rows)

| # | Page | Line | Date | Context |
|---|---|---|---|---|
| 1 | 1 | 2 | September 1, 2026 | letter date, header |
| 2 | 1 | 15-16 | Regulation 30 of SEBI (LODR) Regulations, 2015 | regulatory basis |
| 3 | 1 | 22 | September 1, 2026 | Investor/Analyst Meeting date, "held today" |
| 4 | 1 | 42 | 2026.09.01 11:19:14 +05'30' | digital signature timestamp |
| 5 | 2 | 54 | 2026 | corporate presentation title year |
| 6 | 4 | 63 | FY22 | comparison base year, growth trajectory table |
| 7 | 4 | 63 | FY26 | comparison end year, growth trajectory table |
| 8 | 5 | 125 | Mar'2027 | Dammam Coating Plant production target |
| 9 | 5 | 125 | Mar'2027 | Jammu Stainless Steel Plant production target |
| 10 | 7 | 148 | 1996 | timeline milestone: LSAW plant Pithampur |
| 11 | 7 | 154 | 1999 | timeline milestone: HSAW plant established |
| 12 | 7 | 148 | 2007 | timeline milestone: USD 225mn order + HSAW lines |
| 13 | 7 | 148 | 2019 | timeline milestone: export milestone + Aramco MoU |
| 14 | 7 | 155 | 2012 | timeline milestone: Kobe Steel relationship |
| 15 | 7 | 155 | 2023 | timeline milestone: ERW unit + NPC acquisition |
| 16 | 7 | 166 | 2024 | timeline milestone: additional ERW capacity |
| 17 | 7 | 180 | 2001 | timeline milestone: coating plant PE&CTE |
| 18 | 7 | 185 | 2005 | timeline milestone: Anjar LSAW complex |
| 19 | 7 | 193 | 2006 | timeline milestone: windmill installed |
| 20 | 7 | 180 | 2016 | timeline milestone: JCO press commissioned |
| 21 | 7 | 188 | 2017 | timeline milestone: CWC plant capacity |
| 22 | 7 | 180 | 2025 | timeline milestone: Spiral Mill/PU Coating + Qatar Energy LNG vendor status + Merino Shelters monetized |
| 23 | 7 | 174 | era brackets: 1970-1999, 2000-2006, 2007-2012, 2013-2017, 2018-2024, 2025, FY2026 | timeline header bands |
| 24 | 8 | 210 | since 2011 | Nikhil Mansukhani associated with company |
| 25 | 16 | 408 | Q1 FY27 | Jammu plant status "as of" date |
| 26 | 16 | 418 | Mar 2027 | Jammu plant production timeline target |
| 27 | 17 | 433 | Q4FY25 | JDA upfront amount received |
| 28 | 17 | 433 | FY28 | annual cashflow commencement, Merino Shelters |
| 29 | 17 | 445-446 | Mid-September 2026 | Merino Shelters project launch target |
| 30 | 17 | 446 | FY27 | Merino Shelters cashflow guidance period |
| 31 | 22 | 569 | 40+ Year | NPC relationships with Saudi Arabia's & GCC's leading organizations |
| 32 | 24 | 639 | since 2005 | Aramco approval held continuously (Acquire route) |
| 33 | 25 | 685 | since 2005 | Aramco approved-vendor status held (restated) |
| 34 | 26 | 706 | CY2025 | NPC financial summary period |
| 35 | 26 | 709 | April'2026 | Cash & Liquid Assets as-of date |
| 36 | 28 | 744 | FY26, FY25 | standalone financial comparison periods |
| 37 | 29 | 781 | FY26, FY25 | consolidated financial comparison periods |
| 38 | 30 | 821 | FY24, FY25, FY26 | balance sheet comparison periods |
| 39 | 31 | 872,887 | FY23, FY24, FY25, FY26 | historical comparison periods |
| 40 | 32 | 912 | Q1-FY26, Q2-FY26, Q3-FY26, Q4-FY26, Q1-FY27 | quarterly comparison periods |
| 41 | 32 | 938 | 21st May 2026 | NPC acquisition completion date (100% stake) |
| 42 | 32 | 941 | Q2 FY27 | full NPC earnings contribution expected onward |
| 43 | 34 | 969 | next 5 years | goal and aspiration horizon |

---
## 6. FOOTNOTES

| # | Page | Line | Marker | Resolution |
|---|---|---|---|---|
| 1 | 4 | 65/92 | `1.6Mn+ MTPA*` | RESOLVED — footnote text captured at line 92: "0.43Mn MTPA... NPC capacity within 1.6Mn MTPA total" |
| 2 | 28 | 757 | `EBITDA*` (standalone) | FOOTNOTE_UNRESOLVED — asterisk marker present, no defining footnote text captured anywhere in the structured extraction (likely an EBITDA-definition footnote e.g. "before exceptional items" not rendered/OCR'd) |
| 3 | 29 | 794 | `EBITDA*` (consolidated) | FOOTNOTE_UNRESOLVED — same condition as #2 |
| 4 | 36 | 1013-1037 | Safe-harbor / forward-looking statement disclaimer | full boilerplate text, captured as ENTITY-SUMMARY row (entity ledger #46) |

---
## SUMMARY

- Slides enumerated: 37 (34 data-bearing, 3 no-data dividers: pages 3, 27, 33)
- Numbers enumerated: 223 (2 ZERO_STANDING, 3 with quarterly-mapping ambiguity noted by A1, 2 with unresolved footnote markers)
- Entities enumerated: 49 (40 individual + 9 ENTITY-SUMMARY grouped rows)
- Forward-looking statements enumerated: 20
- Dates enumerated: 43
- Total discrete disclosure units on ledger: 335 (matches A1's own `## COUNTS` header) + 37 slide-inventory rows (slide inventory is a structural index over the same 335 units, not additive to them)
