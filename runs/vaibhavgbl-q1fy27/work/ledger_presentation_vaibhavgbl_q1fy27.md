# A2 ENUMERATION LEDGER — Vaibhav Global Limited (VAIBHAVGBL), Q1 FY27

Doctype: `presentation` (Q1 FY27 Investor Presentation, 39 slides, unit Crores).

Source: `/home/user/inflection-pipeline/runs/vaibhavgbl-q1fy27/work/extract_presentation_vaibhavgbl_q1fy27.txt`

Line count: 1168. Page count: 39 (pdfinfo-confirmed). No prior-quarter ledger exists (first-time coverage) — DROPPED_SLIDE comparison is NOT APPLICABLE this run.


```
=== A2 COUNT TEST ===
category: slides                 grep_count: 39   sweep_count: 39   match: yes
category: chart_data_blocks      grep_count: 9    sweep_count: 9    match: yes
category: numbers_on_slides      grep_count: 304  sweep_count: 304  match: yes
category: footnotes_disclaimers  grep_count: 14   sweep_count: 14   match: yes  (line 540 carries 2 distinct footnote statements -> 15 ledger rows from 14 lines, documented in Table F)
category: entities_segments      grep_count: 39   sweep_count: 39   match: yes
category: guidance_targets_kpi   grep_count: 11   sweep_count: 11   match: yes
category: leadership_profiles    grep_count: 10   sweep_count: 10   match: yes
category: ocr_flagged_pages      grep_count: 6    sweep_count: 6    match: yes
category: zero_standing_items    grep_count: 1    sweep_count: 1    match: yes
TOTAL DISCLOSURE UNITS ENUMERATED (slides + chart blocks + numbers + footnotes + entities + guidance + leadership + OCR flags): 432
gate_a2: pass
=== END COUNT TEST ===
```

Reconciliation notes:
- `slides`: grep `^\[page [0-9]+\]$` against the full extract returns 39 sequential markers (page 1 through page 39, no gaps); manual sweep of every `[page N]` boundary + title text matched 1:1. Match confirmed.
- `chart_data_blocks`: grep `\[CHART` returns 9 matches; manual sweep of the same 9 confirmed, each block itemized in Table B below, including a page-offset anomaly found on 8 of 9 (flag `CHART_PAGE_OFFSET`, see Table B notes).
- `numbers_on_slides`: grep `[0-9]` on lines 15-1168, excluding lines that are pure `[page N]` or `[OCR page N]` markers, returns 304 lines carrying numeric content. Manual sweep (visual pass slide-by-slide against the same exclusion rule) independently reached 304; first pass mistakenly also excluded 2 lines that were only partial marker matches — re-swept per GATE A2 rule 4, corrected, now reconciled.
- `footnotes_disclaimers`: grep for `Note`, `rounded off`, `As on FY26`, `refer to products`, `Source`, `Data as of`, `Revenue breakup based on`, `FY22: Germany`, and leading-`*` lines returns 14 distinct lines; manual sweep confirmed the same 14, one of which (line 540) bundles two footnote statements into a single printed line — both statements are enumerated as separate rows in Table F.
- `entities_segments`: 39 distinct named organizations/geographies confirmed present via individual grep passes (brand subsidiaries, exchanges, auditor/IR advisor, rating agencies, ESG partners, certification bodies, external data-source citations, regulator, and 7 named geographies); manual read-through found no additional entity beyond this list.
- `guidance_targets_kpi`: grep for `target|Target|targeted|Targeting|by FY30|by FY40|expected to contribute|expected to strengthen` returns candidate lines that resolve to 11 discrete forward-looking/target statements after splitting two compound lines (1018/1019, 1142) into their two distinct target clauses each; manual sweep reached the same 11.
- `leadership_profiles`: grep `Mr\. [A-Za-z]+ [A-Za-z]+` returns 10 unique named executives (5 on slide 36, 5 on slide 37); manual sweep of the bio grid on both slides confirmed 10, no unnamed/anonymous profile rows.
- `ocr_flagged_pages`: A1 header lists `ocr_pages: [2, 5, 10, 19, 23, 30]` (6 pages); grep `\[OCR page` returns 6 matches; manual sweep of each confirmed degraded/garbled text consistent with the OCR flag. Match confirmed.
- `zero_standing_items`: exactly one genuine zero-valued standing KPI found (`0% marketplace take-rate on primary channels`, slide 16, line 472); all other apparent "0" tokens found by grep (line 953, chart y-axis gridline labels "0 0") are axis-scale labels, not standing disclosure line items, and are excluded from this count per instruction (they are still captured as numeric content in Table C).

---

## Table A — Slide Manifest (slide-number test, 39/39)
| Slide | Line (page marker) | Title | Content type |
|---|---|---|---|
| 1 | 15 | Cover letter / SEBI Reg 30(6) transmittal to NSE & BSE | text (regulatory letter) |
| 2 | 56 | Title slide: "Investor Presentation, Vaibhav Global Ltd." | text + photo (OCR page, garbled) |
| 3 | 71 | Disclaimer (forward-looking statements) | text |
| 4 | 91 | Table of Contents | text (page-ref list) |
| 5 | 108 | Section divider: "01 VGL – At a Glance" | text (OCR page, garbled) |
| 6 | 128 | VGL: An Omnichannel Consumer Company with Global Scale | text/diagram |
| 7 | 153 | From Gemstone Trading to Integrated Consumer Ecosystem (company timeline) | text/diagram (6 eras) |
| 8 | 185 | A Multi-Category Consumer Portfolio: Expanding Beyond Jewellery | text + photo + brand logos |
| 9 | 219 | Q1 FY27 Performance Update (headline KPI tiles) | text/KPI tiles + certification badges |
| 10 | 250 | Section divider: "02 Structural Growth Drivers" | text (OCR page, garbled) |
| 11 | 263 | Growth Drivers Driving Long-Term Value Creation (hub-and-spoke diagram) | diagram/text |
| 12 | 303 | Vertical Integration Driving Superior Gross Margins | text + bar comparison |
| 13 | 340 | Diversified Global Footprint Across Manufacturing, Retail and Sourcing (map) | map/diagram (OCR page, garbled) |
| 14 | 373 | Strong Global Revenue Mix with Improving Profitability | table (USA/UK/Europe) + text |
| 15 | 406 | Strengthening Brand Equity | chart (in-house brand % trend) + stacked bar (sales bifurcation) |
| 16 | 445 | AI-Enabled Commerce powered by First-Party Data | diagram (channel wheel) + text |
| 17 | 477 | A High-Engagement Customer Ecosystem | text/KPI tiles; embeds CHART data-label block (page-offset, see Table B) |
| 18 | 509 | Q1 FY27 Performance Update — Consolidated Performance | 3 bar charts (Revenue/EBITDA/PAT) |
| 19 | 542 | Section divider: "03 Financial & Operational Update" | text (OCR page, garbled); embeds CHART data-label block (page-offset, see Table B) |
| 20 | 559 | Q1 FY27 Segmental Highlights | 4 bar charts (TV/Digital revenue, volume, ASP) |
| 21 | 597 | EBITDA Margin Walk | waterfall chart |
| 22 | 632 | Revenue Mix Overview | 4 stacked-bar charts (product/geography/format/Budget Pay) |
| 23 | 672 | Section divider: "04 Key Strengths" | text (OCR page, garbled) |
| 24 | 683 | Resilience Through Cycles | text (5 checklist items) |
| 25 | 714 | A Portfolio of Scalable Consumer Brands | text + brand logos |
| 26 | 730 | Strong Cash Generation, Disciplined Deployment | bar+line chart (FCF & Net Cash) + FY26 FCF allocation waterfall |
| 27 | 766 | Strong Fundamentals Driving Sustainable Value Creation | text tiles (4 pillars) |
| 28 | 800 | Voice of Customer as a Strategic Asset | 4 stacked-bar charts + text; embeds CHART data-label block for ROE/ROCE (page-offset, see Table B) |
| 29 | 841 | Consistent Shareholder Returns | text tiles (4 KPI) + 2 bar charts (ROE, ROCE) |
| 30 | 872 | Section divider: "04 Growth Strategy" (duplicate section number, see flags) | text (OCR page, garbled); embeds CHART data-label block for TAM data (page-offset, see Table B) |
| 31 | 884 | Expanding Addressable Markets Supporting Long-Term Growth | 3 bar charts (USA/UK/Germany TAM) + text; embeds CHART data-label block for Ideal World/Germany revenue (page-offset, see Table B) |
| 32 | 926 | Emerging Growth Engines (Ideal World, Mindful Souls, Germany) | text tiles + 2 bar charts |
| 33 | 967 | Lab-Grown Diamonds: A Structural Growth Opportunity | bar chart (market size) + text |
| 34 | 1001 | Growth Drivers & FY30 Roadmap | text (6 pillar panels) |
| 35 | 1036 | What Sets Us Apart | table (6 rows: Platform Strength vs FY26 Reality) |
| 36 | 1075 | Strong Leadership | photo/bio grid (5 executives) |
| 37 | 1100 | Management team | photo/bio grid (5 executives) |
| 38 | 1127 | ESG — Social Impact Beyond the Financials | text (5 panels) |
| 39 | 1156 | Thank You (contacts) | text (company + IR advisor contacts) |

---

## Table B — Chart Data-Label Blocks (9/9)
Every `[CHART...]` annotation the A1 extractor captured, verbatim, with the slide the marker cites vs. the slide the same data visually renders on. 8 of 9 blocks show a consistent -1 page offset (marker cites the page immediately BEFORE the one carrying the rendered bars/labels) — flag `CHART_PAGE_OFFSET`. This is a systematic A1 extraction artifact (or an intentional "preview strip" design element); either way A3/A4 must anchor these numbers to the RENDERED slide, not the marker's stated page.
| # | Line | Marker states page | Rendered data actually on slide | Content (verbatim) | Flags |
|---|------|---------------------|----------------------------------|---------------------|-------|
| 1 | 478 | 17 | 18 | [CHART, page 17, data labels: Q1FY26/Q4FY26/Q1FY27 Revenue 814/935/917, EBITDA 75/96/102 (9%/10%/11% margin), PAT 38/44/56 (5%/5%/6% margin)] | CHART_PAGE_OFFSET |
| 2 | 543 | 19 | 20 | [CHART, page 19, data labels: TV Revenue 444/485/484; Digital Revenue 329/400/398; TV volume 1343/1373/1291(k), ASP $38.8/$40.5/$37.1; Digital volume 1139/1131/1123(k), ASP $33.8/$38.5/$37.0] | CHART_PAGE_OFFSET |
| 3 | 560 | 20 | 21 | [CHART, page 20, data labels: EBITDA margin walk Q1FY26 4.2 -> Gross Margin(brand mix) +9.2 -> Employee Cost(tech leverage) +1.6 -> Digital Marketing -1.2 -> SG&A -1.7 -> Other Income -1.0 -> Q1FY27 11.1] | CHART_PAGE_OFFSET |
| 4 | 598 | 21 | 22 | [CHART, page 21, data labels: B2C by product Jewellery/Lifestyle 36/64,33/67,40/60 (Q1FY26/Q4FY26/Q1FY27); by geography US/UK/Europe 59/29/12,59/29/12,60/28/12; by format TV/Digital 57/43,55/45,55/45; Budget Pay 38/39/36] | CHART_PAGE_OFFSET |
| 5 | 731 | 26 | 26 | [CHART, page 26, data labels: FCF & Net Cash (Rs Cr) by year FY21-FY26: FCF -214/103/268/178/230/272; Net Cash 90/127/167/170/296/387] | (none — self-consistent) |
| 6 | 801 | 28 | 29 | [CHART, page 28, data labels: ROE FY23-Q1FY27: 9/10/12/15/18; ROCE FY23-Q1FY27: 19/19/14/24/24] | CHART_PAGE_OFFSET |
| 7 | 873 | 30 | 31 | [CHART, page 30, data labels: USA Video/Live Commerce TAM $50bn(2023)->$68bn(2026F); UK Online Retail GBP123bn(2023)/127bn(2024)/132bn(2025); Germany E-commerce EUR89bn(2024)/92bn(2025)/96bn(2026F)] | CHART_PAGE_OFFSET |
| 8 | 885 | 31 | 32 | [CHART, page 31, data labels: Ideal World Net Revenue(GBPmn)/Unique Customers('000) FY24/25/26: 7/20/30 revenue, 69/138/142 customers approx per layout; Germany revenue EUR mn FY22-26: 4/14/21/26/27] | CHART_PAGE_OFFSET |
| 9 | 927 | 32 | 33 | [CHART, page 32, data labels: Global lab-grown diamond market USD bn: 34.0 (2026) -> 92.0 (2034); VGL Q1FY27 lab-grown diamond revenue contribution 13% of jewellery/gemstone mix] | CHART_PAGE_OFFSET |

---

## Table C — Every Number on Every Slide (manual+grep sweep, 304/304)
One row per source line carrying numeric content (the atomic disclosure unit for a heavily laid-out slide deck where individual digits are not separably addressable in the extracted text layer). Chart-label lines are cross-referenced to Table B. The one confirmed zero-valued standing item is flagged `ZERO_STANDING`.
| Slide | Line | Content (verbatim, whitespace-collapsed) | Flags |
|---|---|---|---|
| 1 | 17 | Ref: VGL/CS/2026/69 Date: 04th August, 2026 |  |
| 1 | 20 | Exchange Plaza, C-1, Block G, Phiroze Jeejeebhoy Towers, |  |
| 1 | 22 | Bandra, Mumbai – 400 051 Mumbai – 400 001 |  |
| 1 | 23 | Symbol: VAIBHAVGBL Scrip Code: 532156 |  |
| 1 | 29 | Pursuant to Regulation 30(6) of the SEBI (Listing Obligations and Disclosure Requirements) |  |
| 1 | 30 | Regulations, 2015 please find enclosed Financial Results Presentation of Q1 FY27. |  |
| 1 | 40 | PAREEK Date: 2026.08.04 |  |
| 1 | 41 | 23:06:38 +05'30' |  |
| 1 | 45 | M. No.: A39220 |  |
| 1 | 53 | Registered Office: E-69, EPIP, Sitapura Industrial Area, Jaipur-302022, Rajasthan, India • Phone: +91-141-2770648; +91-141-2771975 |  |
| 1 | 54 | CIN: L36911RJ1989PLC004945 • Email: investor_relations@vaibhavglobal.com • Website: www.vaibhavglobal.com |  |
| 2 | 64 | an Vertically Integrated, Omnichannel Consumer Platform 7 |  |
| 2 | 69 | Q1 FY27 Results / Aug 2026 / NSE: VAIBHAVGBL / BSE: 532156 |  |
| 4 | 94 | VGL – At a Glance 4 |  |
| 4 | 97 | Structural Growth Drivers 9 |  |
| 4 | 100 | Financial & Operational Update 18 |  |
| 4 | 103 | Key Strengths 22 |  |
| 4 | 106 | Growth Strategy 29 |  |
| 5 | 109 | 01 |  |
| 5 | 113 | 4 |  |
| 5 | 116 | O07 |  |
| 6 | 151 | 5 |  |
| 7 | 158 | 1980s–89 1996–97 2003–2008 |  |
| 7 | 162 | ▪ Established as a gemstone sourcing & trading ▪ Entered jewellery manufacturing with ▪ Expanded into B2C retail through TV shopping |  |
| 7 | 164 | ▪ Incorporated in 1989, laying the foundation ▪ Successfully listed, raising growth capital & ▪ Navigated global financial crisis through strategic |  |
| 7 | 171 | 2010–2012 2013–2021 2023–2026 |  |
| 7 | 175 | in 2010 products platform capabilities & category expansion |  |
| 7 | 176 | ▪ Completed full repayment of obligations ▪ Strengthened D2C capabilities via owned digital ▪ Increased share of digital revenues to ~45% through |  |
| 7 | 178 | financial resilience & disciplined execution ▪ Re-entered German market in 2021, expanding ▪ Enhanced scalability via AI-led planning tools and |  |
| 7 | 183 | 6 |  |
| 8 | 196 | ~100 new products |  |
| 8 | 199 | • ~14,000–15,000 new jewellery designs launched annually, with freshness and relevance |  |
| 8 | 200 | ~30,000+ SKUs available at any given time |  |
| 8 | 201 | • In-house testing lab and manufacturing • A rich product basket of ~5,000 unique SKUs |  |
| 8 | 202 | • Covers 7 different metals (Silver, Gold, Platinum, Steel, Brass, • Facilitated by innovation & a global sourcing base |  |
| 8 | 217 | 7 |  |
| 9 | 220 | Q1 FY27 Performance Update |  |
| 9 | 222 | INR 917 Crores INR 398 Crores INR 484 Crores |  |
| 9 | 225 | 13% YoY 21% YoY 9% YoY |  |
| 9 | 229 | INR 102 Crores INR 56 Crores |  |
| 9 | 232 | 37% YoY 50% YoY |  |
| 9 | 234 | Margin at 11% Margin at 6% |  |
| 9 | 244 | ‘Combined ESG Rating’ to ‘74 (Strong)’’ Trusted Brands of 2026” |  |
| 9 | 247 | 8 |  |
| 10 | 251 | 02 |  |
| 10 | 255 | 9 |  |
| 10 | 258 | 02 |  |
| 11 | 275 | 24% ROCE and ₹296 Cr net cash |  |
| 11 | 276 | position Digital share targeted 50%+ |  |
| 11 | 294 | 127mn+ household reach across |  |
| 11 | 300 | 10 |  |
| 11 | 301 | As on FY26 |  |
| 12 | 310 | 2,000+ |  |
| 12 | 315 | 5 units 1,69,000 sq.ft. Mumbai 1,000+ |  |
| 12 | 321 | 30+ ~5 mn pieces ~100 ~14–15K |  |
| 12 | 325 | designs per year 250+ |  |
| 12 | 330 | ₹121 Cr VGL (vertically integrated) ~60% |  |
| 12 | 331 | Mfg/Sourcing EBITDA, 130+ |  |
| 12 | 332 | +33% YoY |  |
| 12 | 334 | Typical importer / retailer ~40% |  |
| 12 | 337 | 11 |  |
| 12 | 338 | As on FY26 |  |
| 13 | 359 | 30+ |  |
| 13 | 371 | 12 |  |
| 14 | 376 | Q1FY27 Revenue Mix |  |
| 14 | 379 | FY26 FY26 FY26 |  |
| 14 | 381 | ₹2,058 Cr ₹194 Cr ₹1,032 Cr ₹77 Cr ₹404 Cr ₹7 Cr |  |
| 14 | 382 | Q1FY27 Q1FY27 Q1FY27 |  |
| 14 | 384 | ₹ 530 Cr ₹ 58 Cr ₹ 248 Cr ₹ 12 Cr ₹ 103 Cr ₹1 Cr |  |
| 14 | 385 | Largest market Revenue grew 9.5% YoY, driven Given the seasonal nature of the |  |
| 14 | 386 | 63mn households reached by the improving performance of business and evolving buying |  |
| 14 | 387 | Revenue +8%, EBITDA +9% in the Ideal World and Rachel Galley patterns, margins are expected to |  |
| 14 | 388 | FY26 businesses, supported by higher strengthen meaningfully over the |  |
| 14 | 389 | USA 60% UK 28% Europe 12% brand awareness. course of the year |  |
| 14 | 397 | Production is order-basis, gold price Gemstone, diamond, lab-grown $5–$1,000 across ~35,000 SKUs, |  |
| 14 | 403 | 13 |  |
| 15 | 410 | 57.2% In-House Brand Revenue Contribution (%) |  |
| 15 | 411 | 57.2% |  |
| 15 | 414 | 48.8% |  |
| 15 | 415 | of B2C revenue from own |  |
| 15 | 416 | brands (Q1FY27) Customer loyalty |  |
| 15 | 417 | 29.8% |  |
| 15 | 418 | 26.3% Brand equity accrues to VGL, not to a third-party licensor |  |
| 15 | 422 | FY24 FY25 FY26 Q1 FY27 constraints. |  |
| 15 | 427 | Achieved ~57% of gross B2C sales Strategic brand matrix focused |  |
| 15 | 429 | quarter 30% 33% 35% offering |  |
| 15 | 432 | 70% 67% 65% |  |
| 15 | 434 | Achieved the Target of ~50% of Enhancing repeat purchases and |  |
| 15 | 435 | gross B2C sales, a year in advance retention through Brand |  |
| 15 | 436 | than anticipated FY24 FY25 FY26 |  |
| 15 | 443 | 14 |  |
| 16 | 451 | 127mn HH |  |
| 16 | 453 | Every transaction on every surface 677K unique customer |  |
| 16 | 458 | Recent AI-assisted Shopify migration completed in ~6 months at roughly one-third of the earlier |  |
| 16 | 470 | 677K unique customer records · 3.5 lakh new registrations (TTM) |  |
| 16 | 472 | Social Retail 23 pieces/customer/year · 0% marketplace take-rate on primary channels | ZERO_STANDING (0% marketplace take-rate) |
| 16 | 475 | 15 |  |
| 17 | 478 | [CHART, page 17, data labels: Q1FY26/Q4FY26/Q1FY27 Revenue 814/935/917, EBITDA 75/96/102 (9%/10%/11% margin), PAT 38/44/56 (5%/5%/6% margin)] | CHART_LABEL (see Table B) |
| 17 | 482 | 127mn+ HH 3.5 Lakh 38% 23 40+ |  |
| 17 | 483 | 4 Reach Registration & Retention Average Repeat pieces Core customer age band |  |
| 17 | 494 | Baby Boomers & Gen X ~30,000 SKUs $30-$45 |  |
| 17 | 507 | 16 |  |
| 18 | 510 | Q1 FY27 Performance Update |  |
| 18 | 517 | 9% 10% 11% 5% 5% 6% |  |
| 18 | 520 | 13% YoY 37% YoY * 50% YoY |  |
| 18 | 522 | 935 |  |
| 18 | 523 | 917 |  |
| 18 | 524 | 102 |  |
| 18 | 525 | 96 56 |  |
| 18 | 527 | 814 |  |
| 18 | 528 | 44 |  |
| 18 | 529 | 75 |  |
| 18 | 530 | 38 |  |
| 18 | 535 | Q1 FY26 Q4 FY26 Q1 FY27 Q1 FY26 Q4 FY26 Q1 FY27 Q1 FY26 Q4 FY26 Q1 FY27 |  |
| 18 | 539 | 17 |  |
| 18 | 540 | Note: Q4FY26 PAT is excluding MAT credit of INR 47.2 cr : Numbers are rounded off to nearest figure |  |
| 19 | 543 | [CHART, page 19, data labels: TV Revenue 444/485/484; Digital Revenue 329/400/398; TV volume 1343/1373/1291(k), ASP $38.8/$40.5/$37.1; Digital volume 1139/1131/1123(k), ASP $33.8/$38.5/$37.0] | CHART_LABEL (see Table B) |
| 19 | 544 | 03 |  |
| 19 | 548 | 18 |  |
| 19 | 551 | 05 |  |
| 20 | 560 | [CHART, page 20, data labels: EBITDA margin walk Q1FY26 4.2 -> Gross Margin(brand mix) +9.2 -> Employee Cost(tech leverage) +1.6 -> Digital Marketing -1.2 -> SG&A -1.7 -> Other Income -1.0 -> Q1FY27 11.1] | CHART_LABEL (see Table B) |
| 20 | 561 | Q1 FY27 Segmental Highlights |  |
| 20 | 567 | 400 398 |  |
| 20 | 568 | 485 484 329 |  |
| 20 | 571 | 444 |  |
| 20 | 575 | Q1 FY26 Q4 FY26 Q1 FY27 Q1 FY26 Q4 FY26 Q1 FY27 |  |
| 20 | 580 | Sales Volume ('000s) Average Selling Price US$ Sales Volume ('000s) Average Selling Price US$ |  |
| 20 | 581 | 1,373 38.5 |  |
| 20 | 582 | 37.0 |  |
| 20 | 583 | 1,343 33.8 |  |
| 20 | 584 | 1,139 1,131 |  |
| 20 | 585 | 38.8 40.5 |  |
| 20 | 586 | 1,291 37.1 1,123 |  |
| 20 | 591 | Q1 FY26 Q4 FY26 Q1 FY27 Q1 FY26 Q4 FY26 Q1 FY27 Q1 FY26 Q4 FY26 Q1 FY27 Q1 FY26 Q4 FY26 Q1 FY27 |  |
| 20 | 595 | 19 |  |
| 21 | 598 | [CHART, page 21, data labels: B2C by product Jewellery/Lifestyle 36/64,33/67,40/60 (Q1FY26/Q4FY26/Q1FY27); by geography US/UK/Europe 59/29/12,59/29/12,60/28/12; by format TV/Digital 57/43,55/45,55/45; Budget Pay 38/39/36] | CHART_LABEL (see Table B) |
| 21 | 602 | 11.1 |  |
| 21 | 604 | 9.2 of In-House brands, |  |
| 21 | 610 | 4.2 digital to further Higher freight and |  |
| 21 | 615 | x 1.6 |  |
| 21 | 620 | -1.2 -1.0 |  |
| 21 | 621 | -1.7 |  |
| 21 | 624 | Q1 FY26 Gross Margin Employee Cost Digital Marketing SG&A Other Income Q1 FY27 |  |
| 21 | 630 | 20 |  |
| 22 | 635 | B2C Revenues by Product B2C Revenues by Geography |  |
| 22 | 637 | 12% 12% 12% |  |
| 22 | 639 | 29% 29% 28% |  |
| 22 | 640 | 36% 33% 40% |  |
| 22 | 642 | 64% 67% 60% 59% 59% 60% |  |
| 22 | 646 | Q1FY26 Q4FY26 Q1FY27 |  |
| 22 | 647 | Q1FY26 Q4FY26 Q1FY27 |  |
| 22 | 653 | B2C Revenues by Format Budget Pay (% to B2C Revenues) |  |
| 22 | 658 | 43% 41% 45% |  |
| 22 | 659 | 38% 39% 36% |  |
| 22 | 661 | 57% 55% 55% 62% 61% 64% |  |
| 22 | 663 | Q1FY26 Q4FY26 Q1FY27 Q1FY26 Q4FY26 Q1FY27 |  |
| 22 | 670 | 21 |  |
| 23 | 673 | 04 |  |
| 23 | 677 | 22 |  |
| 23 | 680 | 04 |  |
| 24 | 691 | Gemstones → Jewellery manufacturing → lifestyle products → retail → digital Entered Corporate Debt Restructuring in 2010 with repayment due by 2020; |  |
| 24 | 692 | platform. Each transition changed the revenue model, not just the product the obligation was fully repaid by 2012— years ahead of schedule |  |
| 24 | 697 | ✓ 19% CAGR in market cap since listing ✓ Germany: first full year of positive EBITDA |  |
| 24 | 698 | From ~₹8 Cr listing raise in 1997 to a ~₹3,075 Cr market cap and ~₹3,692 Cr Margins came under pressure due to the economic slowdown and evolving |  |
| 24 | 700 | shareholder return) Company to deliver its first full year of positive EBITDA in FY26 |  |
| 24 | 706 | 78,000+ ideas generated, 1,821+ new products launched, 3 design patents Most long-tenured employees stayed through loss-making periods on the |  |
| 24 | 712 | 23 |  |
| 25 | 718 | 16 brands across categories and markets |  |
| 25 | 728 | 24 |  |
| 26 | 731 | [CHART, page 26, data labels: FCF & Net Cash (Rs Cr) by year FY21-FY26: FCF -214/103/268/178/230/272; Net Cash 90/127/167/170/296/387] | CHART_LABEL (see Table B) |
| 26 | 735 | How FY26 Free Cash Flow (₹272 Cr) was allocated: |  |
| 26 | 737 | FCF generated ₹272 Cr |  |
| 26 | 738 | 387 |  |
| 26 | 739 | 296 |  |
| 26 | 740 | 268 272 −₹100 Cr |  |
| 26 | 741 | 230 Dividends paid |  |
| 26 | 742 | 178 167 170 (~37%) |  |
| 26 | 743 | 127 |  |
| 26 | 744 | 103 90 |  |
| 26 | 745 | Retained capital ₹172 Cr |  |
| 26 | 750 | -214 |  |
| 26 | 752 | FY21 FY22 FY23 FY24 FY25 FY26 |  |
| 26 | 757 | FY22: Germany / Ideal World investment phase |  |
| 26 | 764 | 25 |  |
| 27 | 769 | ~90% Revenue in USD, GBP Expansion Funded Through Internal |  |
| 27 | 779 | ₹686 Cr Cumulative Dividends Paid Since |  |
| 27 | 780 | FY20 |  |
| 27 | 782 | ~51% payout ratio |  |
| 27 | 789 | 16 Owned Brands ~23 Products Purchased Per Customer |  |
| 27 | 790 | ~49% of B2C Revenue Annually |  |
| 27 | 797 | 26 |  |
| 27 | 798 | Note : Data as of FY26 |  |
| 28 | 801 | [CHART, page 28, data labels: ROE FY23-Q1FY27: 9/10/12/15/18; ROCE FY23-Q1FY27: 19/19/14/24/24] | CHART_LABEL (see Table B) |
| 28 | 804 | B2C Revenues by Format Budget Pay (% to B2C Revenues) B2C Revenues by Product |  |
| 28 | 808 | 33% 41% 44% 22% 33% 35% emails, messages, social media |  |
| 28 | 809 | 39% 39% 38% platforms, and product returns. |  |
| 28 | 810 | 67% 78% 67% 65% |  |
| 28 | 811 | 59% 56% 61% 61% 62% |  |
| 28 | 813 | FY20 FY25 FY26 FY20 FY25 FY26 FY20 FY25 FY26 |  |
| 28 | 819 | B2C Revenues by Geography Live monitoring platform that flags |  |
| 28 | 820 | Unique Customer Base (in 000') |  |
| 28 | 822 | 12% 11% intervention. |  |
| 28 | 823 | 31% |  |
| 28 | 824 | 29% 30% 710 681 |  |
| 28 | 825 | 585 Closed-Loop Feedback |  |
| 28 | 826 | 497 461 |  |
| 28 | 827 | 69% System |  |
| 28 | 828 | 59% 59% |  |
| 28 | 831 | FY20 FY25 FY26 continuous improvement. |  |
| 28 | 833 | FY22 FY23 FY24 FY25 FY26 Strong Customer Satisfaction |  |
| 28 | 836 | 96%+ CSAT across key markets |  |
| 28 | 837 | and NPS above 57% in US & UK |  |
| 28 | 838 | during FY26 |  |
| 28 | 839 | 27 |  |
| 29 | 847 | 15–20 38% ₹100 Cr ₹686 Cr |  |
| 29 | 848 | Consecutive quarters of dividend Of FY26 FCF (₹100 Cr) returned as Total dividends paid in FY26 Cumulative dividends paid since |  |
| 29 | 849 | payout funded entirely from FCFs dividends FY20 (~51% payout) |  |
| 29 | 854 | Market capitalisation has compounded at 19% CAGR since listing, excluding the dividend stream entirely |  |
| 29 | 856 | ROE 18% ROCE |  |
| 29 | 857 | 15% 24% 24% |  |
| 29 | 858 | 12% 19% 19% |  |
| 29 | 859 | 9% 10% |  |
| 29 | 860 | 14% |  |
| 29 | 865 | FY23 FY24 FY25 FY26 Q1 FY27 FY23 FY24 FY25 FY26 Q1 FY27 |  |
| 29 | 870 | 28 |  |
| 30 | 873 | [CHART, page 30, data labels: USA Video/Live Commerce TAM $50bn(2023)->$68bn(2026F); UK Online Retail GBP123bn(2023)/127bn(2024)/132bn(2025); Germany E-commerce EUR89bn(2024)/92bn(2025)/96bn(2026F)] | CHART_LABEL (see Table B) |
| 30 | 874 | 04 |  |
| 30 | 878 | 29 |  |
| 30 | 881 | 04 |  |
| 31 | 885 | [CHART, page 31, data labels: Ideal World Net Revenue(GBPmn)/Unique Customers('000) FY24/25/26: 7/20/30 revenue, 69/138/142 customers approx per layout; Germany revenue EUR mn FY22-26: 4/14/21/26/27] | CHART_LABEL (see Table B) |
| 31 | 891 | 68 132 96 |  |
| 31 | 894 | 50 |  |
| 31 | 895 | 127 92 |  |
| 31 | 897 | 89 |  |
| 31 | 898 | 123 |  |
| 31 | 903 | 2023 2026F 2023 2024 2025 2024 2025 2026F |  |
| 31 | 906 | Immediate TAM: $14–15 bn Immediate TAM: $2–2.5 bn Immediate TAM: ~$3bn (incl. Austria) |  |
| 31 | 907 | 3rd largest e-commerce market globally EU's largest consumer economy; content-driven shopping habit |  |
| 31 | 912 | VGL Shop LC anchors ~$232mn revenue — under 0.3% of this TJC + Ideal World combined ~£87mn — a fraction of the |  |
| 31 | 913 | Shop LC Germany at €27mn, now turning profitable |  |
| 31 | 919 | Aggregate platform TAM: ~$20bn · VGL's combined FY26 revenue of ~₹3,692 Cr (~$416mn) represents scope for high penetration |  |
| 31 | 923 | Sources: USA: Statista-sourced US livestreaming/video commerce sales. UK: ONS online retail sales (2023/2024 actuals, via Retail Gazette analysis, Feb 2025); 2025 growth rate per eMarketer forecast (Netguru, Nov 2025), Germany: HDE (Handelsverband Deutschland) Online Monitor 2025, cross- 30 |  |
| 31 | 924 | referenced by bevh using Destatis data; 2025/2026 are HDE's own forecasts. |  |
| 32 | 927 | [CHART, page 32, data labels: Global lab-grown diamond market USD bn: 34.0 (2026) -> 92.0 (2034); VGL Q1FY27 lab-grown diamond revenue contribution 13% of jewellery/gemstone mix] | CHART_LABEL (see Table B) |
| 32 | 931 | Q1 FY27 revenue £ 6 mn Q1 FY27 Revenue ~$ 4 mn Q1 FY27 revenue € 6 mn |  |
| 32 | 933 | Unique customer (TTM) 143K* Unique customer (TTM) 99K Digital sales mix ~24% |  |
| 32 | 935 | Sustained Strong ~32% |  |
| 32 | 936 | Profitability 28% New customer Lifestyle Products’ |  |
| 32 | 943 | 30 138 142 150 26 27 |  |
| 32 | 944 | Lower recurring subscription revenues 21 |  |
| 32 | 945 | 14 |  |
| 32 | 946 | due to reduced customer acquisition 4 |  |
| 32 | 947 | 20 69 100 |  |
| 32 | 949 | 21 24 FY22 FY23 FY24 FY25 FY26 |  |
| 32 | 950 | 10 50 |  |
| 32 | 952 | 7 |  |
| 32 | 953 | 0 0 |  |
| 32 | 954 | FY24 FY25 FY26 Sustained market Better product mix & |  |
| 32 | 956 | Net Revenue Unique Customers Launched 145 new products during Q1 |  |
| 32 | 957 | (£ in mn) (in '000) FY27 Digital performance |  |
| 32 | 959 | at 68% improved to ~24% |  |
| 32 | 960 | * Including 18K common customers of TJC |  |
| 32 | 965 | 31 |  |
| 33 | 971 | 92.0 |  |
| 33 | 974 | 34.0 |  |
| 33 | 978 | 2026 2034 |  |
| 33 | 982 | Rising consumer acceptance Lab grown diamond business Q1 FY27 Revenue contribution (VGL) Chemically, physically and |  |
| 33 | 989 | Attractive price-value 13% Increasing penetration across |  |
| 33 | 999 | *Fortune Business Insights 32 |  |
| 34 | 1002 | Growth Drivers & FY30 Roadmap |  |
| 34 | 1004 | Revenue Target of ₹5,000–5,500 Crores by FY30 |  |
| 34 | 1008 | ▪ FY27 target: 50% of B2C revenue from digital (up from 44% in ▪ Live commerce becomes a bigger medium |  |
| 34 | 1009 | FY26). ▪ Meta and TikTok marketing broaden customer acquisition |  |
| 34 | 1010 | ▪ All channel websites now on Shopify, a D2C-first platform ▪ Global livestream e-commerce is growing at a ~41% CAGR |  |
| 34 | 1018 | ▪ Both acquisitions delivered profitably in FY26, now growth ▪ Brands Targeting 60%+ of B2C revenue by FY27 (from 48.8%); |  |
| 34 | 1019 | contributors ▪ Lifestyle products targeting 50% of B2C revenue medium- |  |
| 34 | 1020 | term (from 35% today) |  |
| 34 | 1027 | ▪ First full year of positive EBITDA achieved in FY26 ▪ AI product-scheduling tool now in production |  |
| 34 | 1028 | ▪ Expected to contribute towards profitability from FY27 ▪ Generative AI scaling content and SEO |  |
| 34 | 1034 | 33 |  |
| 35 | 1039 | Platform Strength Platform Reality (FY26) |  |
| 35 | 1042 | Growth quality 26% EBITDA growth + 74% PAT growth on 9.2% topline growth. EPS up 73% to ₹16.0 |  |
| 35 | 1047 | Margin durability 63.5% gross margin underpinned by ~49% in-house brand mix (streamlined from 33 to 16 brands) + owned manufacturing |  |
| 35 | 1052 | Capital efficiency ROCE 24%; net-cash balance sheet (₹296 Cr); FCF-funded growth — no equity raised, no net debt |  |
| 35 | 1057 | Channel resilience 44% digital and rising toward 50% FY27 target; OTT + social distribution; all 4 channel sites migrated to Shopify. |  |
| 35 | 1062 | Geographic diversification Europe now 11% and fastest-growing; Germany's first full year of positive EBITDA; Mindful Souls and Ideal World both profitable |  |
| 35 | 1066 | Majority-independent board (62.5%); ICSI Governance Award; Big Four audit; FCF-anchored dividend policy; credit-rated ICRA |  |
| 35 | 1073 | 34 |  |
| 36 | 1084 | Total Exp – 46 years Total Exp – 16 years Total Exp – 27 years Total Exp – 20 years Total Exp – 15 years |  |
| 36 | 1085 | VGL Exp – 46 years VGL Exp – 15 years VGL Exp – 6 years VGL Exp – 20 years VGL Exp – 12 years |  |
| 36 | 1089 | • Founded Vaibhav process improvements • Former Country Finance • Driven double-digit revenue 2014 |  |
| 36 | 1090 | Enterprises in 1980 • Established the German Controller (Italy/Germany) at growth at TJC • Previous leadership roles in |  |
| 36 | 1098 | 35 |  |
| 37 | 1109 | Total Exp – 26 years Total Exp – 21 years Total Exp – 27 years Total Exp – 21 years Total Exp – 27 years |  |
| 37 | 1110 | VGL Exp – 1 years VGL Exp – 18 years VGL Exp – 23 years VGL Exp – 3 years VGL Exp – 23 years |  |
| 37 | 1125 | 36 |  |
| 38 | 1132 | ▪ 115mn+ meals distributed to date, ~58,000 meals served every school day — funded by every product sold across VGL's platforms |  |
| 38 | 1133 | ▪ Long-term mission: 1 million meals per school day by FY40 — a formal, board-level ambition, not a slogan |  |
| 38 | 1141 | Jaipur SEZ is LEED Platinum, Net Zero Energy certified (India's 16th such certification). Two Aligned to the Science Based Targets initiative (SBTi) and the 1.5°C Paris pathway: Scope |  |
| 38 | 1142 | India units now fully solar-powered; UK & Germany facilities 100% renewable. 1&2 down 60% absolute by 2035, Scope 3 intensity down 70% by 2035 (FY24-25 baseline). |  |
| 38 | 1148 | Budget Pay, VGL's no-interest instalment programme, reached 38% of B2C revenue in ICRA Combined ESG Rating of 74 ('Strong') — an independent, third-party-verified score, |  |
| 38 | 1149 | FY26 — broadening affordability for value-conscious customers. not a self-assessment. |  |
| 38 | 1154 | 37 |  |
| 39 | 1162 | Group CFO Vikash.Verma1@in.ey.com |  |

---

## Table D — Guidance / Targets / KPI Ledger (11/11)
| # | Slide | Line | Statement | Type |
|---|---|---|---|---|
| 1 | 11 | 276 | Digital share targeted 50%+ supported by live commerce | forward target, no explicit date |
| 2 | 15 | 434 | "Achieved the Target of ~50% of gross B2C sales, a year in advance than anticipated" | target-achieved KPI (retrospective) |
| 3 | 34 | 1004 | Revenue Target of Rs5,000-5,500 Crores by FY30 | forward revenue target |
| 4 | 34 | 1008 | FY27 target: 50% of B2C revenue from digital (up from 44% in FY26) | forward target |
| 5 | 34 | 1018 | Brands Targeting 60%+ of B2C revenue by FY27 (from 48.8%) | forward target |
| 6 | 34 | 1019 | Lifestyle products targeting 50% of B2C revenue medium-term (from 35% today) | forward target, no explicit date |
| 7 | 34 | 1028 | Germany "Expected to contribute towards profitability from FY27" | forward guidance |
| 8 | 35 | 1057 | Channel resilience: 44% digital and rising toward 50% FY27 target | forward target (restated) |
| 9 | 38 | 1133 | Long-term mission: 1 million meals per school day by FY40 | forward ESG target, board-level per text |
| 10 | 38 | 1142 | Scope 1&2 down 60% absolute by 2035 (FY24-25 baseline) | forward ESG/climate target |
| 11 | 38 | 1142 | Scope 3 intensity down 70% by 2035 (FY24-25 baseline) | forward ESG/climate target |

---

## Table E — Entities / Segments Named (39/39)
| # | Entity | First-mention line | Type |
|---|---|---|---|
| 1 | Vaibhav Global Limited (VGL) | 36 | issuer / parent company |
| 2 | NSE (National Stock Exchange of India Limited) | 19 | stock exchange |
| 3 | BSE Limited | 19 | stock exchange |
| 4 | TJC | 210 | owned brand/subsidiary (UK) |
| 5 | Ideal World | 174 | owned brand/subsidiary (UK), acquired |
| 6 | Rachel Galley | 210 | owned brand |
| 7 | Shop LC | 243 | owned brand (USA, implied by shoplc.com domain and Q1 headline) |
| 8 | STS Jewels | 214 | owned brand/domain (stsjewels.com) |
| 9 | Mindful Souls | 174 | owned brand/subsidiary, acquired |
| 10 | Shop LC Germany | 214 | owned brand/subsidiary (shoplc.de) |
| 11 | Ernst & Young LLP (EY) | 1159 | Investor Relations Advisor |
| 12 | ICRA | 243 | credit / ESG rating agency |
| 13 | CARE | 1068 | credit rating agency (CARE A+) |
| 14 | Akshaya Patra Foundation | 1134 | ESG partner (India, meal program) |
| 15 | No Kid Hungry | 1134 | ESG partner (US, meal program) |
| 16 | Backpack Friends | 1134 | ESG partner (US, meal program) |
| 17 | Magic Breakfast | 1134 | ESG partner (UK, meal program) |
| 18 | Felix Project | 1135 | ESG partner (UK, meal program) |
| 19 | Great Place to Work | 240 | certification body |
| 20 | Responsible Jewellery Council (RJC) | 240 | certification body |
| 21 | ICSI | 1066 | governance award body |
| 22 | SBTi (Science Based Targets initiative) | 1141 | climate framework body |
| 23 | Statista | 923 | external data source (USA TAM) |
| 24 | ONS | 923 | external data source (UK TAM) |
| 25 | Retail Gazette | 923 | external data source (UK TAM analysis) |
| 26 | eMarketer | 923 | external data source (UK growth forecast) |
| 27 | Netguru | 923 | external data source (forecast attribution) |
| 28 | HDE (Handelsverband Deutschland) | 923 | external data source (Germany TAM) |
| 29 | Destatis | 924 | external data source (Germany, cross-reference) |
| 30 | Fortune Business Insights | 999 | external data source (lab-grown diamond market) |
| 31 | USA TODAY | 243 | external recognition/press citation |
| 32 | SEBI | 29 | regulator (Reg 30(6) cited) |
| 33 | USA | 146 | geographic segment |
| 34 | UK | 146 | geographic segment |
| 35 | Germany | 484 | geographic segment |
| 36 | Europe | 268 | geographic segment (roll-up of UK+Germany+other for reporting) |
| 37 | India | 19 | geography (manufacturing/sourcing/registered office) |
| 38 | China | 318 | geography (manufacturing) |
| 39 | Canada | 344 | geography (map callout) |

---

## Table F — Footnotes / Fine-Print Disclaimers (14 lines / 15 statements)
| # | Slide | Line | Footnote text |
|---|---|---|---|
| 1 | 3 | 72 | Full disclaimer: "This presentation contains 'forward looking statements'...Vaibhav Global Limited undertakes no obligation to periodically revise any forward-looking statements..." |
| 2 | 9 | 248 | "Numbers are rounded off to nearest figure" |
| 3 | 11 | 301 | "As on FY26" (qualifies ROCE 24% / net cash Rs296 Cr and all wheel-diagram stats on slide 11) |
| 4 | 12 | 338 | "As on FY26" (qualifies vertical-integration capacity/scale stats on slide 12) |
| 5 | 14 | 404 | "Numbers are rounded off to nearest figure" |
| 6 | 18 | 540 | "Note: Q4FY26 PAT is excluding MAT credit of INR 47.2 cr" (first part of compound footnote line 540) |
| 7 | 18 | 540 | "Numbers are rounded off to nearest figure" (second part of compound footnote line 540) |
| 8 | 22 | 654 | "Budget Pay revenues refer to products sold on EMI basis" |
| 9 | 26 | 757 | "FY22: Germany / Ideal World investment phase" (annotation on the FCF/Net Cash chart explaining the FY22 dip) |
| 10 | 27 | 798 | "Note : Data as of FY26" |
| 11 | 28 | 806 | "Budget Pay revenues refer to products sold on EMI basis" (repeated definition) |
| 12 | 28 | 834 | "Revenue breakup based on figures in USD mn" |
| 13 | 31 | 923 | Sources block: Statista (USA), ONS + Retail Gazette + eMarketer/Netguru (UK), HDE/Destatis (Germany) — full text spans lines 923-924 |
| 14 | 32 | 960 | "* Including 18K common customers of TJC" (qualifies Ideal World 143K TTM unique-customer figure) |
| 15 | 33 | 999 | "*Fortune Business Insights" (source for lab-grown diamond market-size chart) |

---

## Table G — Leadership / Management Profiles (10/10, one row each)
| # | Slide | Line | Name | Role | Total Exp | VGL Exp | Background |
|---|---|---|---|---|---|---|---|
| 1 | 36 | 1081 | Sunil Agrawal | Managing Director | 46 yrs | 46 yrs | First generation entrepreneur; Founded Vaibhav Enterprises in 1980; veteran of gems and jewelry industry |
| 2 | 36 | 1081 | Nitin Panwad | Group CFO | 16 yrs | 15 yrs | Chartered Accountant; cost optimization and process improvements; established the German subsidiary |
| 3 | 36 | 1081 | Vineet Ganeriwala | President, Shop LC (US) | 27 yrs | 6 yrs | Chartered Accountant; IIM Kolkata alumnus; former Country Finance Controller (Italy/Germany) at Vodafone |
| 4 | 36 | 1081 | Deepak Mishra | Managing Director, TJC | 20 yrs | 20 yrs | Expert in TV home shopping and e-commerce; drove double-digit revenue growth at TJC |
| 5 | 36 | 1081 | Raghuveer Patnala | Managing Director, Germany | 15 yrs | 12 yrs | IIM Udaipur MBA; joined as Management Trainee 2014; prior leadership roles in China and UK |
| 6 | 37 | 1106 | Sabaresh Kumar | CHRO, VGL Group | 26 yrs | 1 yr | BS Computer Science, Calicut University; two-time Edtech startup founder |
| 7 | 37 | 1106 | Aswini Agarwal | Head of Supply Chain-Asia | 21 yrs | 18 yrs | MBA, University of Rajasthan; secured Great Place to Work certification for VGL India; two-time Rajasthan State Award winner for exports |
| 8 | 37 | 1106 | Ankur Sogani | Vice President, Commercial (US) | 27 yrs | 23 yrs | MBA in Marketing & Finance; specialist in TV shopping and digital marketplaces |
| 9 | 37 | 1106 | Mohammed Farooq | Chief Technology Officer, VGL Group | 21 yrs | 3 yrs | Expert in AI, MLOps, digital scaling; background in space, defense, high-tech sectors |
| 10 | 37 | 1106 | Ashish Dawra | Vice President, Global IT | 27 yrs | 23 yrs | M.Sc. Computer Science; two-decade VGL tenure; built TV shopping and ERP platforms |

---

## Table H — OCR-Flagged Pages (6/6, per A1 header `ocr_pages`)
| # | Slide | Line (OCR marker) | Quality note |
|---|---|---|---|
| 1 | 2 | 58 | Cover/title slide OCR badly degraded: fragments "ve: a Se )", stray characters — company name/tagline recoverable but layout garbled |
| 2 | 5 | 115 | Section divider OCR degraded: "O07" (should read section icon/number), otherwise recoverable |
| 3 | 10 | 257 | Section divider OCR duplicated section marker as "02" (matches text layer) but page content thin |
| 4 | 19 | 550 | Section divider OCR shows stray "05" and "LP" artifacts not matching the "03" section text-layer number |
| 5 | 23 | 679 | Section divider OCR shows "04" duplicate consistent with text layer (see SECTION_NUMBERING_ANOMALY flag) |
| 6 | 30 | 880 | Section divider OCR shows "04" duplicate consistent with text layer (see SECTION_NUMBERING_ANOMALY flag) |

---

## Table I — Zero/Nil/Dash-Valued Standing Items (1/1)
| # | Slide | Line | Item | Value | Flag |
|---|---|---|---|---|---|
| 1 | 16 | 472 | Marketplace take-rate on primary channels | 0% | ZERO_STANDING — the line exists because VGL's proprietary/owned channels carry no third-party marketplace commission; the metric is a standing comparator (implicitly vs. marketplace-dependent competitors) and must not be dropped as "no data". |

---

## Flags raised (summary)
- `ZERO_STANDING` x1 — slide 16, line 472 (0% marketplace take-rate).
- `CHART_PAGE_OFFSET` x8 — 8 of 9 `[CHART...]` marker blocks cite a page number one slide earlier than where the labeled data visually renders (Table B). Only the FY21-FY26 FCF & Net Cash chart (line 731, slide 26) is self-consistent.
- `SECTION_NUMBERING_ANOMALY` x1 — the deck's section-divider numbering is inconsistent: slide 23 ("Key Strengths") and slide 30 ("Growth Strategy") are BOTH labeled section "04" in the text layer and confirmed again in the corresponding OCR passes (lines 673/680 for slide 23; lines 874/881 for slide 30). The Table of Contents (slide 4) lists 5 distinct sections (VGL at a Glance, Structural Growth Drivers, Financial & Operational Update, Key Strengths, Growth Strategy) implying sections should run 01-05, but the printed section badges only go 01-04 with "04" reused. Mechanical numbering defect in the source deck, not a content miss — flagged for A3/A4 visibility.
- `OCR_QUALITY_ISSUE` x6 — pages 2, 5, 10, 19, 23, 30 per A1 header `ocr_pages`; manual sweep confirms degraded/garbled OCR text on all 6 (Table H). None of the 6 carry primary financial data (all are cover/section-divider slides), so no numeric disclosure is at OCR risk, but titles/taglines on these pages should be cross-checked against the source PDF visually if precision on section titling matters downstream.
- `PRIOR_LEDGER_UNAVAILABLE` — no prior-quarter presentation ledger exists for VAIBHAVGBL; `DROPPED_SLIDE` comparison (rule 3) is NOT APPLICABLE this run. Flag for A3/A4: from Q2 FY27 onward, diff this slide manifest (Table A) against the current one to catch any dropped disclosure.

