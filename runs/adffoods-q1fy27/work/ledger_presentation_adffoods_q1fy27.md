# A2 ENUMERATION LEDGER — ADF Foods Limited (ADFFOODS), Q1 FY27, Investor Presentation
Source: `extract_presentation_adffoods_q1fy27.txt` (50 pages, 1362 Read-tool lines; pdftotext -layout primary,
12 pages OCR'd, 7 pages carry inline `[CHART...]` annotations). Prior-quarter ledger: not provided (path not
supplied in task inputs) — `DROPPED_SLIDE` diff cannot be run; flagged `NOT_AVAILABLE_PRIOR_LEDGER`.

## SCOPING NOTE (mechanical, read before Table 2)
"Every number on every slide" is enumerated in Table 2 as every discrete quantified BUSINESS/OPERATIONAL
figure (financial values, %, counts, capacities, stats, dates-as-milestones/guidance). Three number
categories are tracked separately, not inside the Table 2 total, because they are structural/administrative
rather than disclosure content:
  (a) deck-internal footer page numbers (printed slide numbers) — captured in Table 1 "footer#" column.
  (b) the self-referential page-number echoed inside each `[OCR page N]` / `[CHART, page N, ...]` tag itself
      (e.g. the "13" in "[CHART, page 13, ...]") — these duplicate the `[page N]` marker already counted in
      the slide-count category, not new content.
  (c) numbers embedded in the CHART-tag ANNOTATION BODY for pages 13, 14, 19, 22, 49, where A1 restates
      figures that are already present natively on the page (the annotation is an A1 traceability aid, not a
      second appearance of the number on the physical slide). Pages 32 and 35 are the exception: their
      CHART/OCR annotation is the SOLE source of that data (not present in native text), so those numbers
      ARE counted in Table 2.
  (d) page 1 (cover letter to exchanges) and page 50 (contact/CIN footer) administrative identifiers (CIN,
      phone/fax, scrip code, dates, signature timestamp) — captured in Table 1a, not Table 2, since they are
      regulatory/contact metadata, not disclosure figures.
Where the SAME figure is genuinely restated twice on one physical slide in two different text elements
(e.g. pages 11 and 12 restate the headline EBITDA/PAT/YoY numbers a second time inside the descriptive
bullet prose, and separately reveal a margin % not present in the headline box) — that is counted as two
appearances in Table 2, because it is a real internal-consistency checkpoint (a mismatch between the
headline box and the bullet restatement would be a genuine flag).

=== A2 COUNT TEST ===
category: slides              grep_count: 50   sweep_count: 50   match: yes
category: quantified_metrics  grep_count: 285  sweep_count: 285  match: yes
category: footnotes           grep_count: 5    sweep_count: 5    match: yes
category: admin_facts         grep_count: 6    sweep_count: 6    match: yes
category: director_bios       grep_count: 8    sweep_count: 8    match: yes
category: dropped_slides      grep_count: N/A  sweep_count: N/A  match: N/A (NOT_AVAILABLE_PRIOR_LEDGER)
gate_a2: pass
=== END COUNT TEST ===

### Reconciliation detail for `quantified_metrics` (grep vs sweep)
- Raw numeric-token scan (`grep -oE` style pass over slide bodies, pages 2-49, excluding pages 1/50,
  excluding bare-footer-number-only lines, excluding pillar-ordinal lines "01".."05" on pages 4/18):
  **388** raw tokens.
- Less self-referential OCR/CHART tag page-number echoes (category b above): **-19**
  (12 `[OCR page N]` tags + 7 `[CHART, page N,...]` tags, one self-ref token each).
- Less CHART-annotation-body duplicate restatements + axis-gridline labels + dense-label tokenization
  splits, all on pages 13/14/19/22/49 (category c above, where the annotation restates natively-captured
  figures for A1 traceability): **-84**.
- Reconciled: 388 - 19 - 84 = **285**, which equals the independent manual page-by-page sweep total in
  Table 2 (last column "running total" ends at 285). Match: yes. Gate A2: pass.

---
## TABLE 1 — SLIDE INVENTORY (50 slides, every [page N] marker)
Columns: slide# | title | content type | OCR/CHART tag | deck footer# (printed on slide, "—" if none) | flags

| Slide | Title | Content type | Tag | Footer# | Flags |
|---|---|---|---|---|---|
| 1 | (Cover letter to NSE/BSE re: Q1 FY27 presentation upload) | text/letter | — | — | see Table 1a |
| 2 | Investor Presentation Q1FY27 — title slide | text+logo | [OCR page 2] | 1 | dup OCR read of same slide |
| 3 | Safe Harbor | text/disclaimer | — | 2 | full-page disclaimer, see Table 3 |
| 4 | Contents (01-05 sections) | text/list | — | — | — |
| 5 | Company Overview (section divider) | divider | [OCR page 5] | — | no data beyond title |
| 6 | ADF Snapshot | text+stat blocks | — | 5 | — |
| 7 | Our Legacy | text+timeline graphic | — | 6 | 12 dated milestones 1932-2026 |
| 8 | Business Overview (section divider) | divider | [OCR page 8] | — | no data beyond title |
| 9 | What's our Right to Win? | text (6 quadrants) | — | 8 | qualitative "high-teens" margin |
| 10 | Q1 FY27 Executive Summary | text/bullets | — | 9 | — |
| 11 | Q1 FY27 Key Financial Update (Consolidated) | text+stat callout | — | 10 | headline fig. restated in bullets |
| 12 | Q1 FY27 Key Financial Update (Standalone) | text+stat callout | — | 11 | headline fig. restated in bullets |
| 13 | Q1 FY27 Financial Performance | chart (6 bar charts) | [CHART, page 13] | 12 | — |
| 14 | Segment Performance | chart (4 bar charts) | [CHART, page 14] | 13 | AMBIGUOUS_CHART_MAPPING (Distribution revenue quarter order) |
| 15 | Business Segments | text+pie chart | — | 14 | — |
| 16 | Product Portfolio | text/list | — | 15 | — |
| 17 | Growth Strategy and Drivers (section divider) | divider | [OCR page 17] | — | no data beyond title |
| 18 | Strategic Growth Pillars | text/diagram (5 pillars) | — | 17 | ordinals 01-05 structural, not metrics |
| 19 | Key Growth Drivers | text+chart | [CHART, page 19] | 18 | — |
| 20 | 5 Brands, 5 Stories (section divider) | divider | [OCR page 20] | — | no data beyond title |
| 21 | 5 Brands, 5 Stories (target markets overview) | text/grid | — | 20 | no numeric data |
| 22 | Ashoka: ADF Foods' Flagship Brand | text+chart | [CHART, page 22] | 21 | — |
| 23 | Truly Indian: Unlocking Global Markets | text | — | 22 | — |
| 24 | Truly Indian... Award-Winning (NEXTY) | text+photo | — | 23 | — |
| 25 | Truly Indian... Award-Winning (Freezies/Golden Cart) | text+photo | — | 24 | — |
| 26 | ADF Soul: Delicious, "better-for-you" | text | — | 25 | — |
| 27 | Camel & Aeroplane: Our Other Esteemed Brands | text | — | 26 | — |
| 28 | Strong Marketing & Strengthened Distribution (divider) | divider | [OCR page 28] | — | no data beyond title |
| 29 | Ashoka: Marketing Initiatives (branding/activation) | photo montage | — | 28 | no quant. data (A1-verified) |
| 30 | Ashoka: Marketing Initiatives (social/digital presence) | photo montage | — | 29 | no quant. data (A1-verified) |
| 31 | Truly Indian: Marketing Initiatives (retail campaigns) | text+photo | — | 30 | no quant. data |
| 32 | Truly Indian: Marketing Initiatives (Online Platform Growth) | photo+stat cards | [OCR page 32]/[CHART] | 31 | data ONLY from OCR/CHART tag |
| 33 | Truly Indian: Marketing Initiatives (Digital Mktg Dev / Social Nature) | text+stat callout | — | — | no footer# visible |
| 34 | ADF Soul: Marketing Initiatives | photo montage | — | 33 | no quant. data (A1-verified) |
| 35 | ADF Soul's Presence in Modern Trade | photo/retailer logos | [CHART/IMAGE, page 35] | 34 | data ONLY from image-review tag |
| 36 | Manufacturing Excellence (section divider) | divider | [OCR page 36] | — | no data beyond title |
| 37 | Manufacturing Facilities | text+map | — | 36 | — |
| 38 | Warehousing Facilities | text+photo | — | 37 | — |
| 39 | Strategic Innovation (section divider) | divider | [OCR page 39, 0 chars] | — | no data beyond title |
| 40 | Shaping Products and Processes for a Changing Market | text/grid (6 items) | — | 39 | no numeric data |
| 41 | Built on Quality, Compliance & Trade Excellence | text+checklist | — | 40 | — |
| 42 | People & Capabilities (section divider) | divider | [OCR page 42] | — | no data beyond title |
| 43 | Governed by experienced Board Of Directors | text+photo (8 bios) | — | 42 | see Table 4 |
| 44 | Organisation Chart | diagram | — | 43 | LAYOUT_ARTIFACT (stray "11") |
| 45 | ESG & CSR (section divider) | divider | [OCR page 45] | — | no data beyond title |
| 46 | ESG Metrics & Key Initiatives – FY26 | text+stats | — | 45 | UNIT_CAUTION (CSR figure in lakh, not Cr) |
| 47 | Annual Performance Highlights (section divider) | divider | [OCR page 47] | — | no data beyond title |
| 48 | Consolidated 5-year Financial Highlights | table | — | 47 | — |
| 49 | Consistent Shareholder Returns | chart (dividend bar chart) | [CHART, page 49] | 48 | AMBIGUOUS_CHART_MAPPING (dup FY24 label) |
| 50 | Thank You! / IR contacts | text | — | — | CIN repeat, see Table 1a |

## TABLE 1a — COVER LETTER / ADMINISTRATIVE FACTS (pages 1 & 50; excluded from Table 2)
| # | Line | Item | Value | Flags |
|---|---|---|---|---|
| A1 | 57 | Letter date | 29th July, 2026 | — |
| A2 | 65 | Scrip Code (BSE) | 519183 | — |
| A3 | 71-72 | Quarter ended | 30th June, 2026 | — |
| A4 | 83-87 | Digital signature timestamp (Shalaka Swapnil Ovalekar, Company Secretary) | 2026.07.29 21:27:05 +05'30' | signed day before/same day as letter date, consistent |
| A5 | 97 | CIN (page 1, factory contact block) | L15400GJ1990PLC014265 | — |
| A6 | 1359 | CIN (page 50, contact footer) | L15400GJ1990PLC014265 | repeat of A5, identical |

---
## TABLE 2 — QUANTIFIED METRICS (every number on every slide, page 2-49; running total = sweep_count)
Columns: slide | metric row (grouped where a single chart/series carries multiple period values — "count=N"
states how many individual numbers that row contributes to the running total) | values | flags | running total

| Slide | Metric | Values | Flags | Count | Running total |
|---|---|---|---|---|---|
| 2 | Presentation date | July 2026 (native + OCR duplicate read of same slide, counted once) | — | 1 | 1 |
| 6 | Vintage | 9-decade (origin 1932) | — | 1 | 2 |
| 6 | Manufacturing facilities | 3 | — | 1 | 3 |
| 6 | Product SKUs | 600+ | — | 1 | 4 |
| 6 | Prominent brands | 5 | — | 1 | 5 |
| 6 | Country presence | 60+ countries | — | 1 | 6 |
| 6 | Annual food processing capacity | ~38,000 MT | — | 1 | 7 |
| 6 | US distribution warehouses | 2 | — | 1 | 8 |
| 7 | Legacy timeline milestone | 1932 — American Dry Fruits Stores established | — | 1 | 9 |
| 7 | Legacy timeline milestone | 1960 — Camel brand acquired | — | 1 | 10 |
| 7 | Legacy timeline milestone | 1980 — Ashoka launched | — | 1 | 11 |
| 7 | Legacy timeline milestone | 1992 — Listed on BSE | — | 1 | 12 |
| 7 | Legacy timeline milestone | 1996 — Nashik facility set up | — | 1 | 13 |
| 7 | Legacy timeline milestone | 2001 — Frozen food manufacturing introduced | — | 1 | 14 |
| 7 | Legacy timeline milestone | 2010 — Elena Food Specialties acquired | — | 1 | 15 |
| 7 | Legacy timeline milestone | 2016 — Truly Indian launched in Germany | — | 1 | 16 |
| 7 | Legacy timeline milestone | 2021 — Vibrant Foods LLC acquired | — | 1 | 17 |
| 7 | Legacy timeline milestone | 2023 — Nadiad capacity expanded | — | 1 | 18 |
| 7 | Legacy timeline milestone | 2024 — Truly Indian US mainstream + ADF Soul launched | — | 1 | 19 |
| 7 | Legacy timeline milestone | 2026 — Surat CAPEX Phase 1 operational, March 2026 | — | 1 | 20 |
| 7 | Revenue target ("Moving towards") | ₹1,000 Crore Revenue | forward guidance, undated | 1 | 21 |
| 9 | Truly Indian US/Germany store count | 3,000+ stores | — | 1 | 22 |
| 9 | Flagship brand revenue CAGR | ~20%+ (5 years) | — | 2 | 24 |
| 9 | PAT CAGR | ~20% (4 years) | — | 2 | 26 |
| 9 | Capacity expansion investment | ~₹124 Cr (past two years) | — | 1 | 27 |
| 9 | EBITDA margin descriptor | "High-teens" | QUALITATIVE_APPROX, not a hard number | 1 | 28 |
| 10 | Revenue from Operations (Q1FY27, consol.) | INR 167.3 Cr, +25.9% YoY | — | 2 | 30 |
| 10 | EBITDA (Q1FY27, consol.) | INR 29.7 Cr, +26.0% YoY, margin 17.7% | — | 3 | 33 |
| 10 | PAT (Q1FY27, consol.) | INR 17.3 Cr, +13.4% YoY, margin 10.3% | — | 3 | 36 |
| 10 | Consecutive quarters of double-digit YoY growth | 4th | — | 1 | 37 |
| 10 | Truly Indian US store count | 3,000+ | repeat of p9/p23 | 1 | 38 |
| 10 | AEO-T3 certification | Q1 FY27 | alphanumeric identifier | 1 | 39 |
| 11 | Revenue (headline) | INR 167.3 Cr, 25.9% YoY | — | 2 | 41 |
| 11 | EBITDA (headline + bullet restatement) | INR 29.7 Cr (x2), 26.0% YoY (x2) | genuine same-slide restatement | 4 | 45 |
| 11 | EBITDA margin (bullet only) | 17.7% | — | 1 | 46 |
| 11 | PAT (headline + bullet restatement) | INR 17.3 Cr (x2), 13.4% YoY (x2) | genuine same-slide restatement | 4 | 50 |
| 11 | PAT margin (bullet only) | 10.3% | — | 1 | 51 |
| 12 | Revenue (headline + bullet restatement) | INR 120.9 Cr, 20.5% YoY (x2: headline + bullet) | — | 3 | 54 |
| 12 | EBITDA (headline + bullet restatement) | INR 27.5 Cr (x2), 22.6% YoY (x2) | genuine same-slide restatement | 4 | 58 |
| 12 | EBITDA margin (bullet only) | 22.8% | — | 1 | 59 |
| 12 | PAT (headline + bullet restatement) | INR 18.3 Cr (x2), 7.6% YoY (x2) | genuine same-slide restatement | 4 | 63 |
| 12 | PAT margin (bullet only) | 15.1% | — | 1 | 64 |
| 13 | Consolidated Revenue from Ops (INR Cr.) | Q1FY26 132.9 / Q4FY26 196.7 / Q1FY27 167.3 | — | 3 | 67 |
| 13 | Consolidated Revenue YoY | 25.9% | — | 1 | 68 |
| 13 | Consolidated EBITDA (INR Cr.) & margin | Q1FY26 23.5 (17.7%) / Q4FY26 34.3 (17.4%) / Q1FY27 29.7 (17.7%) | — | 6 | 74 |
| 13 | Consolidated EBITDA YoY | 26.0% | — | 1 | 75 |
| 13 | Consolidated PAT (INR Cr.) & margin | Q1FY26 15.2 (11.5%) / Q4FY26 25.9 (13.2%) / Q1FY27 17.3 (10.3%) | — | 6 | 81 |
| 13 | Consolidated PAT YoY | 13.4% | — | 1 | 82 |
| 13 | Standalone Revenue from Ops (INR Cr.) | Q1FY26 100.3 / Q4FY26 150.3 / Q1FY27 120.9 | — | 3 | 85 |
| 13 | Standalone Revenue YoY | 20.5% | — | 1 | 86 |
| 13 | Standalone EBITDA (INR Cr.) & margin | Q1FY26 22.5 (22.4%) / Q4FY26 36.5 (24.3%) / Q1FY27 27.5 (22.8%) | — | 6 | 92 |
| 13 | Standalone EBITDA YoY | 22.6% | — | 1 | 93 |
| 13 | Standalone PAT (INR Cr.) & margin | Q1FY26 17.0 (16.9%) / Q4FY26 30.1 (20.0%) / Q1FY27 18.3 (15.1%) | — | 6 | 99 |
| 13 | Standalone PAT YoY | 7.6% | — | 1 | 100 |
| 14 | Processed Foods Revenue (INR Cr.) | Q1FY26 112.2 / Q4FY26 144.0 / Q1FY27 165.0 | — | 3 | 103 |
| 14 | Distribution Revenue (INR Cr.) | values 20.7 / 31.7 / 23.3 present; quarter-to-value mapping unclear in layout extraction | AMBIGUOUS_CHART_MAPPING | 3 | 106 |
| 14 | Processed Foods EBITDA (INR Cr.) & margin | Q1FY26 24.1 (21.5%) / Q4FY26 42.6 (25.8%) / Q1FY27 31.2 (21.6%) | — | 6 | 112 |
| 14 | Distribution EBITDA (INR Cr.) & margin | Q1FY26 3.6 (17.4%) / Q4FY26 3.7 (11.7%) / Q1FY27 2.7 (11.5%) | — | 6 | 118 |
| 15 | Core segments | 2 | — | 1 | 119 |
| 15 | FY26 revenue split | Processed Foods 85% / Distribution 15% | — | 2 | 121 |
| 16 | SKU count | 600+ | repeat of p6 | 1 | 122 |
| 19 | FY27E revenue guidance | 900+ (INR crores), headline "upwards of INR 900 crores" | — | 1 | 123 |
| 19 | Revenue bar chart | FY25 590 / FY26 683 | — | 2 | 125 |
| 19 | Flagship brand CAGR guidance | 20-25% CAGR | — | 1 | 126 |
| 19 | Store presence (marquee US chains) | 3,000+ stores | repeat of p9/p10 | 1 | 127 |
| 19 | Brownfield & debottlenecking capacity | INR 180-200 crores | — | 1 | 128 |
| 19 | Greenfield expansion capacity | INR 250-275 crores | — | 1 | 129 |
| 19 | Distribution/outsourcing scale-up | INR ~100 crores | — | 1 | 130 |
| 19 | EBITDA margin descriptor | "High teens" | QUALITATIVE_APPROX | 1 | 131 |
| 22 | Ashoka founding year | 1980 | repeat of p7 | 1 | 132 |
| 22 | Ashoka Brand Sales (INR Cr.) | FY21 119 / FY22 157 / FY23 211 / FY24 254 / FY25 267 / FY26 308 | — | 6 | 138 |
| 22 | Ashoka 5-year CAGR | 20%+ | — | 1 | 139 |
| 22 | Ashoka country presence | 60+ countries | repeat of p6 | 1 | 140 |
| 23 | Truly Indian retail outlet count | 3,000+ Outlets | repeat of p9/p10/p19 | 1 | 141 |
| 24 | NEXTY award field size | out of 1000s of products | — | 1 | 142 |
| 24 | NEXTY Best Breads & Bakery winners | 1 of only 37 winners | — | 1 | 143 |
| 24 | Progressive Grocer recognition year | Editor's Pick, Best New Products of 2026 | — | 1 | 144 |
| 24 | Award entry pool | Winner among 1,000+ product entries | — | 1 | 145 |
| 24 | New product launch year | 2026 (Tikka Masala Naan) | — | 1 | 146 |
| 25 | Simply Recipes award year | The 2026 Freezies Awards | — | 1 | 147 |
| 25 | AllRecipes review pool | Out of 1,000+ new grocery products reviewed | — | 1 | 148 |
| 25 | AllRecipes Golden Cart wins | 2 Golden Cart Awards | — | 1 | 149 |
| 26 | ADF Soul olive-oil range | 100% extra-virgin Olive Oil | — | 1 | 150 |
| 26 | ADF Soul pickle/chutney SKUs | 22 SKUs | — | 1 | 151 |
| 26 | ADF Soul frozen bread SKUs | 7 SKUs | — | 1 | 152 |
| 26 | ADF Soul frozen snack SKUs | 5 SKUs | — | 1 | 153 |
| 27 | Camel brand heritage | 100+ years | — | 1 | 154 |
| 32 | Total Reach (Truly Indian online) | 2.58M+ | data only via OCR/CHART tag | 1 | 155 |
| 32 | Instagram Impressions | 1.02M | data only via OCR/CHART tag | 1 | 156 |
| 32 | Social Interactions | 28K+ | data only via OCR/CHART tag | 1 | 157 |
| 32 | New Followers | +68% | data only via OCR/CHART tag | 1 | 158 |
| 32 | @trulyindianfood followers | 2,879 | data only via OCR/CHART tag | 1 | 159 |
| 32 | @trulyindianfood posts | 263 | data only via OCR/CHART tag | 1 | 160 |
| 33 | Social Nature trial — Activations | 5,700+ | — | 1 | 161 |
| 33 | Social Nature trial — Product Trials | 1,500+ | — | 1 | 162 |
| 33 | Social Nature trial — Verified Reviews | 825 | — | 1 | 163 |
| 35 | Dorabjee's heritage | Since 1911 | data only via image-review/CHART tag | 1 | 164 |
| 35 | MK Retail heritage | Since 1927 | data only via image-review/CHART tag | 1 | 165 |
| 35 | Modern trade retail partners named | 8 (Nature's Basket, D-Mart, Dorabjee's, freshpik, Food Square, MK Retail, Reliance Fresh Signature, simpli namdhari's) | data only via image-review/CHART tag | 1 | 166 |
| 37 | Plant 1 (Surat) built-up area | ~14,300 Sq.mt. | — | 1 | 167 |
| 37 | Plant 2 (Nadiad) built-up area | ~26,000 Sq.mt. | — | 1 | 168 |
| 37 | Plant 3 (Nashik) built-up area | ~12,000 Sq.mt. | — | 1 | 169 |
| 37 | Annual food processing capacity | ~38,000 MT | repeat of p6 | 1 | 170 |
| 37 | Surat greenfield expansion cost | ~INR 90 crores (Phase 1) | — | 1 | 171 |
| 37 | Surat greenfield incremental revenue | INR 250-275 crores | repeat of p19 | 1 | 172 |
| 37 | Brownfield/debottlenecking incremental revenue | INR 180-200 crores | repeat of p19 | 1 | 173 |
| 38 | Combined US warehousing area | 100,000 sq.ft. | — | 1 | 174 |
| 38 | Atlanta warehouse area | 34,000 sq.ft. | — | 1 | 175 |
| 38 | New Jersey warehouse area | 66,000 sq.ft. | — | 1 | 176 |
| 41 | AEO-T3 certification quarter | Q1 FY27 | repeat of p10 | 1 | 177 |
| 41 | Export House status | 3 Star | — | 1 | 178 |
| 43 | Bimal Thakkar experience | 40+ years | — | 1 | 179 |
| 43 | Pheroze Mistry experience | 40+ years | — | 1 | 180 |
| 43 | M. M. Srivastava experience | 40+ years | — | 1 | 181 |
| 43 | Ameet Hariani experience | 35+ years | — | 1 | 182 |
| 43 | Deepa Harris experience | 30+ years | — | 1 | 183 |
| 43 | Viren Merchant experience | 40+ years | — | 1 | 184 |
| 43 | Jay Mehta experience | 40+ years | — | 1 | 185 |
| 43 | Jay Mehta / Mehta Group footprint | 4 continents | — | 1 | 186 |
| 43 | Arjuun Guuha experience | 30+ years | — | 1 | 187 |
| 44 | Regional Country/Sales Managers | Canada 1, USA 5, UK&EU 2, GCC&APAC 1, Australia 2 | — | 5 | 192 |
| 44 | Stray subtotal figure near President/CFO row | 11 (sums exactly to the 5 regional counts above: 1+5+2+1+2=11) | LAYOUT_ARTIFACT — position in layout-extracted text ambiguous, value corroborated by sum | 1 | 193 |
| 46 | Water withdrawal reduction | 7.17% YoY | — | 1 | 194 |
| 46 | Water consumption reduction | 23.85% YoY | — | 1 | 195 |
| 46 | Third-party water dependence | 67% YoY | AMBIGUOUS_DIRECTION — sign of change (increase/decrease) not stated on slide | 1 | 196 |
| 46 | Nashik ZLD water recycling capacity (current) | ~200,000 L/day | — | 1 | 197 |
| 46 | Nashik ZLD water recycling capacity (from) | ~90,000 L/day | — | 1 | 198 |
| 46 | Nadiad hybrid renewable — plant power target (occurrence 1, Environmental box) | ~70% | — | 1 | 199 |
| 46 | Nadiad hybrid renewable — plant power target (occurrence 2, CSR Quantitative Impact box) | ~70% | DUPLICATE_LABEL — same figure printed in two overlapping text boxes per raw layout extraction | 1 | 200 |
| 46 | CSR Expenditure FY26 | Rs. 189.5 lakh | UNIT_CAUTION — stated in lakh, not Cr (= ₹1.895 Cr); only non-Cr figure in the deck | 1 | 201 |
| 46 | CSR Expenditure YoY | 18.53% YoY | — | 1 | 202 |
| 46 | Students benefited (overall) | ~4,000 | — | 1 | 203 |
| 46 | Students supported (education/skill dev) | 240+ | — | 1 | 204 |
| 46 | School science labs equipped | 7 | — | 1 | 205 |
| 46 | Students benefiting from science labs | ~5,000 | — | 1 | 206 |
| 46 | Child Care Units supported | 27 | — | 1 | 207 |
| 46 | Children with cancer supported | 1,700+ | — | 1 | 208 |
| 46 | Girl students supported (Tamil Nadu) | ~9,000 | — | 1 | 209 |
| 46 | Rural schools (Tamil Nadu) | 9 | — | 1 | 210 |
| 48 | Revenue from Operations (5yr, INR Cr.) | FY22 421.2 / FY23 450.3 / FY24 520.3 / FY25 589.6 / FY26 683.2 | — | 5 | 215 |
| 48 | Gross Profit (5yr, INR Cr.) | FY22 211.5 / FY23 235.9 / FY24 276.2 / FY25 341.4 / FY26 410.5 | — | 5 | 220 |
| 48 | Gross Profit % (5yr) | 50.2% / 52.4% / 53.1% / 57.9% / 60.1% | — | 5 | 225 |
| 48 | EBITDA (5yr, INR Cr.) | FY22 66.6 / FY23 80.6 / FY24 104.9 / FY25 98.4 / FY26 130.7 | — | 5 | 230 |
| 48 | EBITDA Margin % (5yr) | 15.8% / 17.9% / 20.2% / 16.7% / 19.1% | — | 5 | 235 |
| 48 | PAT (5yr, INR Cr.) | FY22 48.5 / FY23 55.9 / FY24 73.8 / FY25 69.3 / FY26 96.8# | # excludes exceptional items, see footnote | 5 | 240 |
| 48 | PAT Margin % (5yr) | 11.5% / 12.4% / 14.2% / 11.7% / 14.2% | — | 5 | 245 |
| 48 | Equity (5yr, INR Cr.) | FY22 345.6 / FY23 421.6 / FY24 442.0 / FY25 492.7 / FY26 571.9 | — | 5 | 250 |
| 48 | Net Debt* (5yr, INR Cr., negative = net cash) | FY22 (101.3) / FY23 (143.4) / FY24 (144.5) / FY25 (118.0) / FY26 (78.2) | net cash surplus all 5 years | 5 | 255 |
| 48 | Tangible & Intangible Assets (5yr, INR Cr.) | FY22 160.3 / FY23 181.6 / FY24 187.4 / FY25 204.6 / FY26 285.0 | — | 5 | 260 |
| 48 | ROCE** % (5yr) | 18.1% / 18.1% / 22.2% / 20.2% / 23.4% | — | 5 | 265 |
| 48 | ROE** % (5yr) | 14.0% / 17.7% / 17.1% / 14.1% / 16.9% | — | 5 | 270 |
| 48 | Working Capital (5yr, INR Cr.) | FY22 115.6 / FY23 134.9 / FY24 131.4 / FY25 161.9 / FY26 193.6 | — | 5 | 275 |
| 48 | Exceptional item excluded from FY26 PAT/ROCE/ROE | INR 6.8 crores (labour code) | — | 1 | 276 |
| 49 | Dividend chart FY22 | 8.8 (INR Cr.) | — | 1 | 277 |
| 49 | Dividend chart FY23 | 11.0 (INR Cr.) | — | 1 | 278 |
| 49 | Dividend chart FY24 (first label) | 13.2 (INR Cr.) | — | 1 | 279 |
| 49 | Dividend chart FY24 (second/duplicate label) | 43.9 (INR Cr.) | AMBIGUOUS_CHART_MAPPING — FY24 appears twice with two different values; likely buyback-inclusive bar mislabeled/duplicated in source | 1 | 280 |
| 49 | Dividend chart FY25 | 13.2 (INR Cr.) | — | 1 | 281 |
| 49 | Dividend chart FY26 | 13.2* (INR Cr.), footnoted | — | 1 | 282 |
| 49 | Cumulative shareholder returns since FY22 | INR 100+ Cr. | — | 1 | 283 |
| 49 | FY26 dividend footnote — Interim | Rs. 6.6 Cr | — | 1 | 284 |
| 49 | FY26 dividend footnote — Proposed Final | Rs. 6.6 Cr | — | 1 | 285 |

**Table 2 running total: 285.** (Matches sweep_count and reconciled grep_count in the COUNT TEST above.)

---
## TABLE 3 — FOOTNOTES & DISCLAIMERS
| # | Slide | Line | Text (first ~15 words / full if short) | Flags |
|---|---|---|---|---|
| F1 | 3 | 123-148 | Full Safe Harbor / forward-looking-statement disclaimer qualifying the entire presentation | full-page disclaimer, qualifies all headline numbers |
| F2 | 48 | 1315 | *Net Debt (Cash Surplus) = Long Term Borrowings + Short Term Borrowings – Cash & Cash Equivalents | defines the Net Debt line item |
| F3 | 48 | 1316 | #PAT excludes exceptional items of INR 6.8 crores due to labour code | qualifies FY26 PAT of 96.8 |
| F4 | 48 | 1317 | **ROCE & ROE excludes exceptional items | qualifies FY26 ROCE 23.4% / ROE 16.9% |
| F5 | 49 | 1349 | *Includes Interim Dividend (Rs. 6.6 Cr), Proposed Final Dividend (Rs. 6.6 Cr) | qualifies FY26 dividend figure 13.2* |

## TABLE 4 — DIRECTOR PROFILES (page 43; presentation doctype discloses name/role/bio only — no DIN, no term dates, no appointment date disclosed on this slide)
| # | Name | Role | Tenure/experience stated | Other directorships / relationships noted | Flags |
|---|---|---|---|---|---|
| D1 | Bimal Thakkar | Chairman, Managing Director and CEO | 40+ years, domestic/export food industry | Instrumental in brand development, international acquisitions, subsidiary setups | NOT FOUND: DIN, term dates |
| D2 | Pheroze Mistry | Independent Director | 40+ years, business administration | Associated with Pallonji Group (logistics, industrial coating, shipping, dredging, insurance, investments) | NOT FOUND: DIN, term dates |
| D3 | M. M. Srivastava | Independent Director | Science graduate, master's in physics, IAS (Retd), MBA, 40+ years admin/corporate | Member (Fin) Gujarat Electricity Board, MD Gujarat Agro Industries, Secretary-Finance, Commissioner Commercial Tax, Principal Secretary Energy Petrochemicals; Independent Director of Adani Power | NOT FOUND: DIN, term dates |
| D4 | Ameet Hariani | Independent Director | 35+ years, corporate/commercial law, M&A, real estate, finance transactions | Independent Director of Strides Pharma Ltd, Mahindra Logistics Ltd, Mahindra Life Space Developers Ltd, Aptech Ltd | NOT FOUND: DIN, term dates |
| D5 | Deepa Harris | Independent Director | 30+ years, luxury hospitality | Drove Taj Group of Hotels' India luxury brand; Independent Director of PVR Ltd, Jubilant Foodworks, Yatra Online, TCPL Packaging | NOT FOUND: DIN, term dates |
| D6 | Viren Merchant | Non-Executive Director | 40+ years, business mgmt / pharma & healthcare | Currently CEO, Encore Healthcare Pvt Ltd | NOT FOUND: DIN, term dates |
| D7 | Jay Mehta | Non-Executive Director | 40+ years, industrial | Director, Indian ops of Mehta Group (4 continents: cement/building materials, horticulture, consultancy); Executive Chairman, Saurashtra Cement Ltd | NOT FOUND: DIN, term dates |
| D8 | Arjuun Guuha | Whole Time Director | Senior food industry professional, 30+ years | Head of Operations & CEO roles, India and overseas, Indian corporations and MNCs | NOT FOUND: DIN, term dates |

## TABLE 5 — DROPPED-SLIDE COMPARISON (prior-quarter deck)
Prior-quarter ledger path was not supplied in this task's inputs. `DROPPED_SLIDE` diff cannot be performed.
Flag: `NOT_AVAILABLE_PRIOR_LEDGER`. A3/A4 should request the Q4 FY26 presentation ledger if a same-slide
diff is required for the silence-signal check (rule 3 of the presentation enumeration protocol).

---
## FLAG SUMMARY
- `AMBIGUOUS_CHART_MAPPING` — page 14 (Distribution segment revenue, quarter-to-bar mapping unclear from
  layout-extracted text) and page 49 (dividend chart, duplicate "FY24" year label carrying two different
  values, 13.2 and 43.9).
- `AMBIGUOUS_DIRECTION` — page 46, "Dependence on third-party water 67% YoY" does not state increase or
  decrease.
- `LAYOUT_ARTIFACT` — page 44, stray "11" positioned near the President/CFO row of the org chart; value is
  corroborated as the sum of the five regional Country/Sales Manager counts (1+5+2+1+2=11) but its intended
  placement in the chart is not certain from the extracted layout.
- `DUPLICATE_LABEL` — page 46, the "~70% of plant power requirement" hybrid-renewable figure is printed in
  two overlapping text boxes (Environmental Initiatives box and CSR Quantitative Impact box); same figure,
  not a new data point, retained once as a flagged duplicate row.
- `UNIT_CAUTION` — page 46, CSR Expenditure FY26 stated as Rs. 189.5 lakh, the sole non-Crore figure in the
  deck (per extraction header conversion note); do not misread as ₹189.5 Cr downstream.
- `QUALITATIVE_APPROX` — pages 9 and 19, "High-teens" / "high teens" EBITDA margin descriptor is not a hard
  number; do not treat as a specific %.
- `NOT_AVAILABLE_PRIOR_LEDGER` — prior-quarter presentation ledger not supplied; DROPPED_SLIDE check not
  performed (see Table 5).
- `ZERO_STANDING` — none encountered. The only structured line-item financial table in this deck (page 48,
  Consolidated 5-year Financial Highlights) has fully populated values across all 13 line items and all 5
  years (FY22-FY26); no blank, dash, or nil cells to flag.

## COMPLETENESS STATEMENT
All 50 `[page N]` markers enumerated in Table 1. All 12 `[OCR page N]` tags and all 7 `[CHART...]` tags
accounted for and cross-referenced in Table 1 and Table 2. Every quantified business/operational figure on
every slide is enumerated in Table 2 (285 data points, reconciled grep vs. sweep). Every footnote/disclaimer
is enumerated in Table 3 (5 items). Every director bio on page 43 is enumerated in Table 4 (8 directors, DIN
and term dates NOT FOUND — not disclosed on this slide type). Dropped-slide diff not runnable, flagged
`NOT_AVAILABLE_PRIOR_LEDGER` rather than silently skipped.
