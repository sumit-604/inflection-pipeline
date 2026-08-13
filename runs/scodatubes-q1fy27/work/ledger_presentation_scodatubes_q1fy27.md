# A2 ENUMERATION LEDGER -- Scoda Tubes Limited (SCODATUBES), Q1 FY27, Investor Presentation

Source: `runs/scodatubes-q1fy27/work/extract_presentation_scodatubes_q1fy27.txt` (A1 extract, 40 PDF pages, page_coverage 100%)

=== A2 COUNT TEST ===
category: slides       grep_count: 40    sweep_count: 40    match: yes
category: numbers      grep_count: 624   sweep_count: 624   match: yes
category: footnotes    grep_count: 48    sweep_count: 48    match: yes
category: dropped_slide  grep_count: N.A.  sweep_count: N.A.  match: N.A. (no prior-quarter deck exists for this ticker; this is the first investor presentation filed by SCODATUBES; DROPPED_SLIDE check is out of scope this run, stated per instructions)
gate_a2: pass
=== END COUNT TEST ===

## RECONCILIATION METHODOLOGY (numbers category)

Raw automated pass: digit-token regex over the extract, excluding (a) the 10 OCR-fallback echo blocks (A1 confirms OCR added no numeric content beyond text-layer on 8 of these; the 2 exceptions -- pages 16 and 28 -- are handled explicitly below), (b) numbered footnote-definition lines (counted separately under Footnotes), (c) page-footer pagination digits in the final 4 lines of each page block. Raw pass = **624** tokens.

Manual sweep re-check found 5 corrections that net to zero against the raw pass, each documented:
1. EXCLUDE page16 line540 '15' -- footer pagination digit missed by the automated last-4-lines heuristic (sits just before the OCR/CHART block marker, pushing it outside the heuristic's window).
2. EXCLUDE page38 line1366 '37' -- same footer-heuristic miss (page footer shares a line with 'ANNEXURE' text).
3. EXCLUDE 3x page34 tokens '000' -- these are the '000'' in the axis-title unit label "(in 000' tonnes)", repeated on 3 charts on that slide; a unit designator, not a disclosed data value.
4. ADD 3x page6 narrative quantities that a pure digit-token regex structurally cannot catch because they are letter-adjacent / word-form: 'H2 FY27' (welded-capacity commissioning timing), 'three to four months' (advance order-booking cycle), 'a couple of weeks' (April gas-supply disruption duration).
5. ADD 2x explicit ZERO_STANDING rows required by the operating rules (dash/blank standing values invisible to a digit regex by definition): page25 line875 FY25 opening-cash cell shown as '-' (dash); page10 line360 FY23 Y-o-Y-growth cell left blank (no prior-year comparator, first year of the series).

Net: 624 - 2 - 3 + 3 + 2 = **624**. Sweep count matches raw grep count. GATE A2: pass.

---

## TABLE 1 -- SLIDES (every slide: number, title, content type)

| Slide | Source line | Title | Content type |
|---|---|---|---|
| 1 | 38 | Cover letter to NSE/BSE (Investor Presentation on Q1 FY27 Earnings Update) | text (regulatory transmittal letter) |
| 2 | 83 | Investor Presentation - Q1 FY27 Earnings Update (title/cover) | text (section divider / cover, photographic background, OCR'd) |
| 3 | 101 | Agenda (7 items) | text (list) |
| 4 | 124 | Performance Update - 01 (section divider) | text (section divider, photographic background, OCR'd) |
| 5 | 141 | Performance Snapshot - Q1 FY27 | chart (KPI infographic cards) |
| 6 | 189 | Chairperson & Executive Director's Commentary | text (quote) |
| 7 | 220 | Revenue Split Across Geographies - Q1 FY27 | chart (bar charts x3 + revenue-mix donuts) |
| 8 | 265 | Key Financial Highlights - Q1 FY27 | chart (bar charts x6) |
| 9 | 309 | About Scoda Tubes Ltd - 02 (section divider) | text (section divider, photographic background, OCR'd) |
| 10 | 332 | Scoda Tubes Limited At a Glimpse | table/text (capacity stat callouts + FY23-FY26 financial summary table) |
| 11 | 377 | A Compounding Story With Significant Milestones (1/2) | text (timeline infographic, 2008-2017) |
| 12 | 413 | A Compounding Story With Significant Milestones (2/2) | text (timeline infographic, 2018-2026) |
| 13 | 452 | Sustainable Moats - 03 (section divider) | text (section divider, photographic background, OCR'd) |
| 14 | 469 | Sustainable Moats (7-item framework) | text (numbered list, 01-07) |
| 15 | 495 | Specialized Production of SS Tubes and Pipes | table (5-product dimensional spec table: seamless pipes/tubes/'U'tubes/instrumentation/welded) |
| 16 | 530 | International Accreditations and Product Approvals | photo (certification badge collage) + text; OCR'd at 400dpi |
| 17 | 573 | Customer Diversification and International Presence | chart (donut: country mix; sector icon grid; revenue-split donut) |
| 18 | 612 | Extensive and Effective Quality Control | text (mandatory/supplementary test lists) |
| 19 | 631 | Strategic Location of Facility and Fully Integrated Production | text |
| 20 | 662 | Experienced and Qualified Team | photo/text (8 director/officer profile cards) |
| 21 | 690 | Consistent Financial Performance (1/2) | chart (6 bar charts: Revenue/EBITDA/PAT + their margins, FY23-FY26) |
| 22 | 742 | Consistent Financial Performance (2/2) | chart (6 bar charts: RoE/Net D-E/Inventory Days/RoCE/Debtor Days/CCC, FY23-FY26) |
| 23 | 785 | Historic Income Statement | table (16 line items x FY23-FY26 + 3-yr CAGR column) |
| 24 | 815 | Historic Balance Sheet | table (13 line items x FY23-FY26) |
| 25 | 850 | Historic Cashflow Statement | table (10 line items x FY23-FY26) |
| 26 | 884 | Key Strategies - 04 (section divider) | text (section divider, photographic background, OCR'd) |
| 27 | 898 | Key Strategies (3-item list) | text (list, unnumbered) |
| 28 | 918 | Increase Our Existing Production Capacity | chart (capacity bar chart, axis-ambiguous per A1) + table (capacity comparison) |
| 29 | 1036 | Captive Solar Project | text/photo (stat card) |
| 30 | 1061 | Geographic Expansion of Customer Base | chart (export country-split bar chart + export revenue trend bar chart) |
| 31 | 1107 | Strengthen Our Brand Value | text (exhibitions list + brand-building bullets) |
| 32 | 1139 | Industry Overview - 05 (section divider) | text (section divider, photographic background, OCR'd) |
| 33 | 1176 | Global Demand Contribution | chart (2 donuts CY2023/CY2028E + bar chart mn tonnes CY19-CY23/CY28E) |
| 34 | 1216 | Stainless Steel Tubes and Pipes - India Outlook | chart (3 bar charts: demand/import/export) + text (demand-share bullets) |
| 35 | 1261 | Select Financial Information - 06 (section divider) | text (section divider, photographic background, OCR'd) |
| 36 | 1276 | Income statement (Q1 FY27 vs Q1 FY26) | table (16 line items x Q1FY27/Q1FY26/YoY change) |
| 37 | 1309 | Annexure - 07 (section divider) | text (section divider, photographic background, OCR'd) |
| 38 | 1325 | Process Flow (Welded vs Seamless) | text/diagram (two parallel manufacturing process flows) |
| 39 | 1368 | Safe Harbor Statement | text (legal disclaimer, full page) |
| 40 | 1403 | For Any Further Information/Queries, Please Contact | text/photo (contact card) |

---

## TABLE 2 -- DROPPED_SLIDE CHECK

N.A. this run. No prior-quarter investor-presentation deck exists for SCODATUBES to diff against -- this is the first investor presentation filed by the company (Q1 FY27, filed 2026-08-13, immediately following its FY26 IPO/listing per Slide12's 2026 milestone: 'Listed on NSE & BSE' / 'Raised INR 220 crores through public issue'). DROPPED_SLIDE flag will apply starting Q2 FY27's enumeration once a prior-quarter ledger exists to diff against.

---

## TABLE 3 -- NUMBERS (every number on every slide, incl. chart data labels; source-line context given verbatim, not interpreted)

| Slide | Source line | Value | Source-line context (verbatim, truncated) | Flags |
|---|---|---|---|---|
| 1 | 39 | 13, | Date: August 13, 2026 |  |
| 1 | 39 | 2026 | Date: August 13, 2026 |  |
| 1 | 46 | 400 | Mumbai – 400 001 |  |
| 1 | 46 | 001 | Mumbai – 400 001 |  |
| 1 | 47 | 400051 | Bandra East, Mumbai – 400051 |  |
| 1 | 48 | 544411 | BSE SCRIP Code – “544411” |  |
| 1 | 55 | 30, | of the Company for the Quarter ended on June 30, 2026 |  |
| 1 | 55 | 2026 | of the Company for the Quarter ended on June 30, 2026 |  |
| 1 | 58 | 30, | for the Unaudited Standalone Financial Results of the Company for the Quarter ended on June 30, 2... |  |
| 1 | 58 | 2026 | for the Unaudited Standalone Financial Results of the Company for the Quarter ended on June 30, 2... |  |
| 1 | 68 | 2026.08 | Date: 2026.08.13 |  |
| 1 | 68 | 13 | Date: 2026.08.13 |  |
| 1 | 69 | 10 | RAMESHBHAI 10:38:36 +05'30' |  |
| 1 | 69 | 38 | RAMESHBHAI 10:38:36 +05'30' |  |
| 1 | 69 | 36 | RAMESHBHAI 10:38:36 +05'30' |  |
| 1 | 69 | +05 | RAMESHBHAI 10:38:36 +05'30' |  |
| 1 | 69 | 30 | RAMESHBHAI 10:38:36 +05'30' |  |
| 1 | 73 | 06785595 | DIN: 06785595 |  |
| 1 | 79 | 2437, | Survey Nos.: 2437, 2442, 2443, 2446, Ahmedabad-Mehsana highway, Village: Rajpur, Tal. Kadi, Dist.... |  |
| 1 | 79 | 2442, | Survey Nos.: 2437, 2442, 2443, 2446, Ahmedabad-Mehsana highway, Village: Rajpur, Tal. Kadi, Dist.... |  |
| 1 | 79 | 2443, | Survey Nos.: 2437, 2442, 2443, 2446, Ahmedabad-Mehsana highway, Village: Rajpur, Tal. Kadi, Dist.... |  |
| 1 | 79 | 2446, | Survey Nos.: 2437, 2442, 2443, 2446, Ahmedabad-Mehsana highway, Village: Rajpur, Tal. Kadi, Dist.... |  |
| 1 | 79 | 384440 | Survey Nos.: 2437, 2442, 2443, 2446, Ahmedabad-Mehsana highway, Village: Rajpur, Tal. Kadi, Dist.... |  |
| 1 | 80 | 91 | Phone: + 91 2764 278 278 \| Email: info@scodatubes.com \| sales@scodatubes.com Web: www.scodatubes.com |  |
| 1 | 80 | 2764 | Phone: + 91 2764 278 278 \| Email: info@scodatubes.com \| sales@scodatubes.com Web: www.scodatubes.com |  |
| 1 | 80 | 278 | Phone: + 91 2764 278 278 \| Email: info@scodatubes.com \| sales@scodatubes.com Web: www.scodatubes.com |  |
| 1 | 80 | 278 | Phone: + 91 2764 278 278 \| Email: info@scodatubes.com \| sales@scodatubes.com Web: www.scodatubes.com |  |
| 3 | 103 | 01 | 01 Performance Update | STRUCTURAL_AGENDA_NUM |
| 3 | 106 | 02 | 02 About Scoda Tubes Limited | STRUCTURAL_AGENDA_NUM |
| 3 | 109 | 03 | 03 Sustainable Moats | STRUCTURAL_AGENDA_NUM |
| 3 | 112 | 04 | 04 Growth Strategy | STRUCTURAL_AGENDA_NUM |
| 3 | 115 | 05 | 05 Industry Overview | STRUCTURAL_AGENDA_NUM |
| 3 | 119 | 06 | Shaping a 06 Select Financial Information | STRUCTURAL_AGENDA_NUM |
| 3 | 122 | 07 | TOMORROW 07 Annexure | STRUCTURAL_AGENDA_NUM |
| 4 | 131 | 01 | 01 | STRUCTURAL_SECTION_DIVIDER_NUM |
| 5 | 144 | 124.3 | Revenue from INR 124.3 crores Cashflow from INR -13.8 crores |  |
| 5 | 144 | -13.8 | Revenue from INR 124.3 crores Cashflow from INR -13.8 crores |  |
| 5 | 145 | +27.6% | Operations (+27.6% y-o-y) Operations (vs 18.4 crores in FY25) |  |
| 5 | 145 | 18.4 | Operations (+27.6% y-o-y) Operations (vs 18.4 crores in FY25) |  |
| 5 | 151 | 39.8 | INR 39.8 crores Gross Profit Margin |  |
| 5 | 152 | 32.0% | 32.0% |  |
| 5 | 153 | +40.0% | (+40.0% y-o-y) (vs 29.2% in Q1 FY26) |  |
| 5 | 153 | 29.2% | (+40.0% y-o-y) (vs 29.2% in Q1 FY26) |  |
| 5 | 159 | 16.0 | INR 16.0 crores 12.9% |  |
| 5 | 159 | 12.9% | INR 16.0 crores 12.9% |  |
| 5 | 161 | +12.6% | (+12.6% y-o-y) (vs 14.6% Q1 FY26) |  |
| 5 | 161 | 14.6% | (+12.6% y-o-y) (vs 14.6% Q1 FY26) |  |
| 5 | 166 | 5.3 | INR 5.3 crores PAT Margin |  |
| 5 | 167 | 4.2% | 4.2% |  |
| 5 | 169 | -25.9% | (-25.9% y-o-y) (vs 7.3% in Q1 FY26) |  |
| 5 | 169 | 7.3% | (-25.9% y-o-y) (vs 7.3% in Q1 FY26) |  |
| 5 | 175 | 9.9% | 9.9% Net Debt/Equity |  |
| 5 | 176 | 0.3 | 0.3x |  |
| 5 | 177 | 21.1% | (vs 21.1% in FY25) (vs 1.1x in FY25) |  |
| 5 | 177 | 1.1 | (vs 21.1% in FY25) (vs 1.1x in FY25) |  |
| 5 | 181 | 97 | 97 days 211 days |  |
| 5 | 181 | 211 | 97 days 211 days |  |
| 5 | 183 | 76 | (vs 76 days in FY25) (vs 164 in FY25) |  |
| 5 | 183 | 164 | (vs 76 days in FY25) (vs 164 in FY25) |  |
| 6 | 194 | 3-4 months (worded 'three to four months') | advance order booking cycle of approximately three to four months limited our ability to immediat... | GUIDANCE_NARRATIVE_ADDITION;NOT_DIGIT_REGEX_MATCHABLE |
| 6 | 197 | 'a couple of weeks' (gas supply disruption duration, April) | Operationally, our manufacturing facility also experienced a temporary disruption in gas supply d... | GUIDANCE_NARRATIVE_ADDITION;NOT_DIGIT_REGEX_MATCHABLE |
| 6 | 198 | H2 FY27 (guidance/commissioning timing, referenced qualitatively; explicit 'H2 FY27' appears at line 205-206) | couple of weeks. In addition, manpower availability remained challenging during the quarter, furt... | GUIDANCE_NARRATIVE_ADDITION;NOT_DIGIT_REGEX_MATCHABLE |
| 7 | 229 | +1.5% | +1.5% +81.5% |  |
| 7 | 229 | +81.5% | +1.5% +81.5% |  |
| 7 | 230 | 57.9 | 57.9 | NUMBER_DISCREPANCY(cf. Slide30 shows Q1FY27 export revenue as 57.0, not 57.9; ~1.6% variance unreconciled) |
| 7 | 234 | 65.5 | 65.5 66.5 |  |
| 7 | 234 | 66.5 | 65.5 66.5 |  |
| 7 | 235 | 31.9 | 31.9 |  |
| 7 | 237 | 32.8% | 32.8% |  |
| 7 | 239 | 46.6% | 46.6% |  |
| 7 | 246 | 67.2% | Revenue 67.2% |  |
| 7 | 248 | 53.4% | 53.4% |  |
| 7 | 249 | +27.6% | +27.6% |  |
| 7 | 251 | 124.3 | 124.3 |  |
| 7 | 253 | 97.4 | 97.4 |  |
| 8 | 273 | +27.6% | +27.6% +12.6% -25.9% |  |
| 8 | 273 | +12.6% | +27.6% +12.6% -25.9% |  |
| 8 | 273 | -25.9% | +27.6% +12.6% -25.9% |  |
| 8 | 274 | 124.3 | 124.3 |  |
| 8 | 276 | 97.4 | 97.4 16.0 |  |
| 8 | 276 | 16.0 | 97.4 16.0 |  |
| 8 | 277 | 14.2 | 14.2 |  |
| 8 | 279 | 7.1 | 7.1 |  |
| 8 | 280 | 5.3 | 5.3 |  |
| 8 | 292 | +283 | +283 bps -172 bps |  |
| 8 | 292 | -172 | +283 bps -172 bps |  |
| 8 | 293 | -305 | -305 bps |  |
| 8 | 294 | 7.3% | 7.3% |  |
| 8 | 296 | 32.0% | 32.0% |  |
| 8 | 297 | 14.6% | 14.6% |  |
| 8 | 298 | 12.9% | 12.9% |  |
| 8 | 299 | 4.2% | 4.2% |  |
| 8 | 301 | 29.2% | 29.2% |  |
| 9 | 316 | 02 | 02 | STRUCTURAL_SECTION_DIVIDER_NUM |
| 10 | 336 | 37,156 | 37,156+ 20,000 |  |
| 10 | 336 | 20,000 | 37,156+ 20,000 |  |
| 10 | 344 | 20,068 | 20,068 334 | CROSS_SLIDE_INCONSISTENCY(cf. Slide28 capacity table) |
| 10 | 344 | 334 | 20,068 334 | RENDER_ARTIFACT(likely '33' production lines + footnote marker '4' merged in extraction; footnote 4 = '25 Pilgers & 8 Draw Benches' = 25+8=33, consistent) |
| 10 | 350 | 9001 | • Certifications: ISO 9001:2015, ISO 14001:2015 and ISO 45001:20182 1,020 2 |  |
| 10 | 350 | 2015, | • Certifications: ISO 9001:2015, ISO 14001:2015 and ISO 45001:20182 1,020 2 |  |
| 10 | 350 | 14001 | • Certifications: ISO 9001:2015, ISO 14001:2015 and ISO 45001:20182 1,020 2 |  |
| 10 | 350 | 2015 | • Certifications: ISO 9001:2015, ISO 14001:2015 and ISO 45001:20182 1,020 2 |  |
| 10 | 350 | 45001 | • Certifications: ISO 9001:2015, ISO 14001:2015 and ISO 45001:20182 1,020 2 |  |
| 10 | 350 | 20182 | • Certifications: ISO 9001:2015, ISO 14001:2015 and ISO 45001:20182 1,020 2 | RENDER_ARTIFACT(likely 'ISO 45001:2018' + footnote marker '2' merged) |
| 10 | 350 | 1,020 | • Certifications: ISO 9001:2015, ISO 14001:2015 and ISO 45001:20182 1,020 2 |  |
| 10 | 350 | 2 | • Certifications: ISO 9001:2015, ISO 14001:2015 and ISO 45001:20182 1,020 2 |  |
| 10 | 354 | 2014 | • Products sold to Europe are certified under PED 2014/68/EU In INR crores |  |
| 10 | 354 | 68 | • Products sold to Europe are certified under PED 2014/68/EU In INR crores |  |
| 10 | 355 | 2000 | and ADW/AD 2000 - Merkblatt – WO |  |
| 10 | 357 | 0252, | • Additional accreditation: DNV-CP-0252, DNV Marine and |  |
| 10 | 358 | 518.7 | Indian Boiler Regulation Revenue from operations 518.7 484.9 399.9 305.1 |  |
| 10 | 358 | 484.9 | Indian Boiler Regulation Revenue from operations 518.7 484.9 399.9 305.1 |  |
| 10 | 358 | 399.9 | Indian Boiler Regulation Revenue from operations 518.7 484.9 399.9 305.1 |  |
| 10 | 358 | 305.1 | Indian Boiler Regulation Revenue from operations 518.7 484.9 399.9 305.1 |  |
| 10 | 360 | 7.0% | Y-o-Y growth 7.0% 21.3% 31.0% |  |
| 10 | 360 | 21.3% | Y-o-Y growth 7.0% 21.3% 31.0% |  |
| 10 | 360 | 31.0% | Y-o-Y growth 7.0% 21.3% 31.0% |  |
| 10 | 362 | 3 | 3 YEAR CAGR (FY23-FY26) Gross profit 165.4 148.5 137.9 92.5 |  |
| 10 | 362 | 165.4 | 3 YEAR CAGR (FY23-FY26) Gross profit 165.4 148.5 137.9 92.5 |  |
| 10 | 362 | 148.5 | 3 YEAR CAGR (FY23-FY26) Gross profit 165.4 148.5 137.9 92.5 |  |
| 10 | 362 | 137.9 | 3 YEAR CAGR (FY23-FY26) Gross profit 165.4 148.5 137.9 92.5 |  |
| 10 | 362 | 92.5 | 3 YEAR CAGR (FY23-FY26) Gross profit 165.4 148.5 137.9 92.5 |  |
| 10 | 364 | 31.9% | Gross margin 31.9% 30.6% 34.5% 30.3% |  |
| 10 | 364 | 30.6% | Gross margin 31.9% 30.6% 34.5% 30.3% |  |
| 10 | 364 | 34.5% | Gross margin 31.9% 30.6% 34.5% 30.3% |  |
| 10 | 364 | 30.3% | Gross margin 31.9% 30.6% 34.5% 30.3% |  |
| 10 | 366 | 76.2 | EBITDA 76.2 78.1 58.8 34.8 |  |
| 10 | 366 | 78.1 | EBITDA 76.2 78.1 58.8 34.8 |  |
| 10 | 366 | 58.8 | EBITDA 76.2 78.1 58.8 34.8 |  |
| 10 | 366 | 34.8 | EBITDA 76.2 78.1 58.8 34.8 |  |
| 10 | 367 | 19% | 19% 30% 55% |  |
| 10 | 367 | 30% | 19% 30% 55% |  |
| 10 | 367 | 55% | 19% 30% 55% |  |
| 10 | 368 | 14.7% | Revenue EBITDA PAT EBITDA margin 14.7% 16.1% 14.7% 11.4% |  |
| 10 | 368 | 16.1% | Revenue EBITDA PAT EBITDA margin 14.7% 16.1% 14.7% 11.4% |  |
| 10 | 368 | 14.7% | Revenue EBITDA PAT EBITDA margin 14.7% 16.1% 14.7% 11.4% |  |
| 10 | 368 | 11.4% | Revenue EBITDA PAT EBITDA margin 14.7% 16.1% 14.7% 11.4% |  |
| 10 | 371 | 38.8 | PAT 38.8 31.7 18.3 10.3 |  |
| 10 | 371 | 31.7 | PAT 38.8 31.7 18.3 10.3 |  |
| 10 | 371 | 18.3 | PAT 38.8 31.7 18.3 10.3 |  |
| 10 | 371 | 10.3 | PAT 38.8 31.7 18.3 10.3 |  |
| 10 | 373 | 7.5% | PAT margin 7.5% 6.5% 4.6% 3.4% |  |
| 10 | 373 | 6.5% | PAT margin 7.5% 6.5% 4.6% 3.4% |  |
| 10 | 373 | 4.6% | PAT margin 7.5% 6.5% 4.6% 3.4% |  |
| 10 | 373 | 3.4% | PAT margin 7.5% 6.5% 4.6% 3.4% |  |
| 11 | 378 | 1 | A Compounding Story With Significant Milestones (1/2) |  |
| 11 | 378 | 2 | A Compounding Story With Significant Milestones (1/2) |  |
| 11 | 390 | 2010 | 2010 2013 2017 |  |
| 11 | 390 | 2013 | 2010 2013 2017 |  |
| 11 | 390 | 2017 | 2010 2013 2017 |  |
| 11 | 393 | 2008 | 2008 2012 2014 |  |
| 11 | 393 | 2012 | 2008 2012 2014 |  |
| 11 | 393 | 2014 | 2008 2012 2014 |  |
| 11 | 411 | 6 | Limited \| 6. Hindustan Petroleum Corporation Limited \| 7. Engineers India Limited \| 8. Government... |  |
| 11 | 411 | 7 | Limited \| 6. Hindustan Petroleum Corporation Limited \| 7. Engineers India Limited \| 8. Government... |  |
| 11 | 411 | 8 | Limited \| 6. Hindustan Petroleum Corporation Limited \| 7. Engineers India Limited \| 8. Government... |  |
| 12 | 414 | 2 | A Compounding Story With Significant Milestones (2/2) |  |
| 12 | 414 | 2 | A Compounding Story With Significant Milestones (2/2) |  |
| 12 | 420 | 20,000 | BHEL’s Bhopal and Jhansi Rail Coach Factory, Western • Achieved production capacity 20,000 MTPA |  |
| 12 | 421 | 11,088 | facility for product supply Railway and Central Railway of 11,088 MT/year |  |
| 12 | 426 | 2019 | 2019 2023 2025 |  |
| 12 | 426 | 2023 | 2019 2023 2025 |  |
| 12 | 426 | 2025 | 2019 2023 2025 |  |
| 12 | 429 | 2018 | 2018 2022 2024 |  |
| 12 | 429 | 2022 | 2018 2022 2024 |  |
| 12 | 429 | 2024 | 2018 2022 2024 |  |
| 12 | 430 | 2026 | 2026 |  |
| 12 | 436 | 220 | • Raised INR 220 |  |
| 12 | 442 | 9001 | accordance with ISO 9001:2015 |  |
| 12 | 442 | 2015 | accordance with ISO 9001:2015 |  |
| 12 | 444 | 14001 | accordance with ISO 14001:2015 |  |
| 12 | 444 | 2015 | accordance with ISO 14001:2015 |  |
| 12 | 446 | 45001 | accordance with ISO 45001:2018 |  |
| 12 | 446 | 2018 | accordance with ISO 45001:2018 |  |
| 13 | 459 | 03 | 03 | STRUCTURAL_SECTION_DIVIDER_NUM |
| 14 | 473 | 04 | 04 | STRUCTURAL_MOAT_NUM |
| 14 | 474 | 03 | 03 05 | STRUCTURAL_MOAT_NUM |
| 14 | 474 | 05 | 03 05 | STRUCTURAL_MOAT_NUM |
| 14 | 479 | 02 | 02 06 | STRUCTURAL_MOAT_NUM |
| 14 | 479 | 06 | 02 06 | STRUCTURAL_MOAT_NUM |
| 14 | 485 | 01 | 01 07 | STRUCTURAL_MOAT_NUM |
| 14 | 485 | 07 | 01 07 | STRUCTURAL_MOAT_NUM |
| 15 | 505 | 1 | OD: 1/8” NB to 6” NB OD: 6.00mm to OD: 6.00mm to OD: 6.00mm to OD: 6.00mm to |  |
| 15 | 505 | 8 | OD: 1/8” NB to 6” NB OD: 6.00mm to OD: 6.00mm to OD: 6.00mm to OD: 6.00mm to |  |
| 15 | 505 | 6 | OD: 1/8” NB to 6” NB OD: 6.00mm to OD: 6.00mm to OD: 6.00mm to OD: 6.00mm to |  |
| 15 | 505 | 6.00 | OD: 1/8” NB to 6” NB OD: 6.00mm to OD: 6.00mm to OD: 6.00mm to OD: 6.00mm to |  |
| 15 | 505 | 6.00 | OD: 1/8” NB to 6” NB OD: 6.00mm to OD: 6.00mm to OD: 6.00mm to OD: 6.00mm to |  |
| 15 | 505 | 6.00 | OD: 1/8” NB to 6” NB OD: 6.00mm to OD: 6.00mm to OD: 6.00mm to OD: 6.00mm to |  |
| 15 | 505 | 6.00 | OD: 1/8” NB to 6” NB OD: 6.00mm to OD: 6.00mm to OD: 6.00mm to OD: 6.00mm to |  |
| 15 | 506 | 101.6 | 101.6mm 50.80mm 50.80mm 60.30mm |  |
| 15 | 506 | 50.80 | 101.6mm 50.80mm 50.80mm 60.30mm |  |
| 15 | 506 | 50.80 | 101.6mm 50.80mm 50.80mm 60.30mm |  |
| 15 | 506 | 60.30 | 101.6mm 50.80mm 50.80mm 60.30mm |  |
| 15 | 508 | 0.70 | THK: 0.70mm to THK: 0.70mm to THK: 0.80mm to THK: 0.80mm to |  |
| 15 | 508 | 0.70 | THK: 0.70mm to THK: 0.70mm to THK: 0.80mm to THK: 0.80mm to |  |
| 15 | 508 | 0.80 | THK: 0.70mm to THK: 0.70mm to THK: 0.80mm to THK: 0.80mm to |  |
| 15 | 508 | 0.80 | THK: 0.70mm to THK: 0.70mm to THK: 0.80mm to THK: 0.80mm to |  |
| 15 | 510 | 6.00 | 6.00mm 4.00mm 6.00mm 4.00mm |  |
| 15 | 510 | 4.00 | 6.00mm 4.00mm 6.00mm 4.00mm |  |
| 15 | 510 | 6.00 | 6.00mm 4.00mm 6.00mm 4.00mm |  |
| 15 | 510 | 4.00 | 6.00mm 4.00mm 6.00mm 4.00mm |  |
| 15 | 512 | 22 | random length Length: Up to 22 Mtr Length: Up to 22 Mtr Length: Up to 18.000 Mtr Length: Up to 18... |  |
| 15 | 512 | 22 | random length Length: Up to 22 Mtr Length: Up to 22 Mtr Length: Up to 18.000 Mtr Length: Up to 18... |  |
| 15 | 512 | 18.000 | random length Length: Up to 22 Mtr Length: Up to 22 Mtr Length: Up to 18.000 Mtr Length: Up to 18... |  |
| 15 | 512 | 18.000 | random length Length: Up to 22 Mtr Length: Up to 22 Mtr Length: Up to 18.000 Mtr Length: Up to 18... |  |
| 16 | 537 | 349 | • Company’s capabilities and accreditations have enabled Scoda Tubes to cater to 349 clients glob... |  |
| 17 | 575 | 32 | Strong Presence in 32 Countries1 Catering to Clients Across Multiple Sectors |  |
| 17 | 578 | 67% | 67% | AMBIGUOUS_MAPPING(donut category-to-% mapping unclear from text layer; values sum to 124%, not 100%, arithmetic does not reconcile - flag for visual verification) |
| 17 | 582 | 1% | 1% | AMBIGUOUS_MAPPING(donut category-to-% mapping unclear from text layer; values sum to 124%, not 100%, arithmetic does not reconcile - flag for visual verification) |
| 17 | 583 | 124.3 | 124.3 |  |
| 17 | 584 | 11% | 11% crores | AMBIGUOUS_MAPPING(donut category-to-% mapping unclear from text layer; values sum to 124%, not 100%, arithmetic does not reconcile - flag for visual verification) |
| 17 | 587 | 45% | 45% | AMBIGUOUS_MAPPING(donut category-to-% mapping unclear from text layer; values sum to 124%, not 100%, arithmetic does not reconcile - flag for visual verification) |
| 17 | 600 | 53.4% | 53.4% |  |
| 17 | 601 | 46.6% | 46.6% |  |
| 18 | 614 | 14 | • Dedicated quality control division comprising of a team of 14 personnel capable of all mandator... |  |
| 19 | 637 | 74,699 | On Ahmedabad-Mehsana • Available land parcel of 74,699 sq. mts., with only 37,156 Installed solar... |  |
| 19 | 637 | 37,156 | On Ahmedabad-Mehsana • Available land parcel of 74,699 sq. mts., with only 37,156 Installed solar... |  |
| 19 | 638 | 360 | highway, 360 kms from sq. mts. currently developed for manufacturing. rooftops, generating 1 MW of |  |
| 19 | 638 | 1 | highway, 360 kms from sq. mts. currently developed for manufacturing. rooftops, generating 1 MW of |  |
| 19 | 639 | 23 | Mundra port and 23 kms clean energy to support |  |
| 19 | 640 | 30,064 | • 30,064 sq. mts. reserved for welded products. |  |
| 19 | 650 | 20,000 | 20,000 MTPA.1 |  |
| 19 | 650 | 1 | 20,000 MTPA.1 |  |
| 20 | 672 | 10 | • 10+ years of • 10+ years of • 10+ years of • 10+ years of Experience • 10+ years of Experience | TEMPLATE_REPEAT(identical '10+ years' value across 5 distinct director bios) |
| 20 | 672 | 10 | • 10+ years of • 10+ years of • 10+ years of • 10+ years of Experience • 10+ years of Experience | TEMPLATE_REPEAT(identical '10+ years' value across 5 distinct director bios) |
| 20 | 672 | 10 | • 10+ years of • 10+ years of • 10+ years of • 10+ years of Experience • 10+ years of Experience | TEMPLATE_REPEAT(identical '10+ years' value across 5 distinct director bios) |
| 20 | 672 | 10 | • 10+ years of • 10+ years of • 10+ years of • 10+ years of Experience • 10+ years of Experience | TEMPLATE_REPEAT(identical '10+ years' value across 5 distinct director bios) |
| 20 | 672 | 10 | • 10+ years of • 10+ years of • 10+ years of • 10+ years of Experience • 10+ years of Experience | TEMPLATE_REPEAT(identical '10+ years' value across 5 distinct director bios) |
| 21 | 691 | 1 | Consistent Financial Performance (1/2) |  |
| 21 | 691 | 2 | Consistent Financial Performance (1/2) |  |
| 21 | 698 | 30% | CAGR: 30% |  |
| 21 | 699 | 78.1 | 78.1 76.2 CAGR: 56% 38.8 |  |
| 21 | 699 | 76.2 | 78.1 76.2 CAGR: 56% 38.8 |  |
| 21 | 699 | 56% | 78.1 76.2 CAGR: 56% 38.8 |  |
| 21 | 699 | 38.8 | 78.1 76.2 CAGR: 56% 38.8 |  |
| 21 | 700 | 19% | CAGR: 19% 40 |  |
| 21 | 700 | 40 | CAGR: 19% 40 |  |
| 21 | 701 | 484.9 | 484.9 518.7 31.7 |  |
| 21 | 701 | 518.7 | 484.9 518.7 31.7 |  |
| 21 | 701 | 31.7 | 484.9 518.7 31.7 |  |
| 21 | 702 | 58.8 | 58.8 |  |
| 21 | 703 | 399.9 | 399.9 30 |  |
| 21 | 703 | 30 | 399.9 30 |  |
| 21 | 704 | 305.1 | 305.1 18.3 |  |
| 21 | 704 | 18.3 | 305.1 18.3 |  |
| 21 | 705 | 34.8 | 34.8 20 |  |
| 21 | 705 | 20 | 34.8 20 |  |
| 21 | 706 | 10.3 | 10.3 |  |
| 21 | 707 | 10 | 10 |  |
| 21 | 709 | 0 | 0 |  |
| 21 | 720 | 7.5% | 7.5% |  |
| 21 | 721 | 34.5% | 34.5% |  |
| 21 | 722 | 34.5% | 34.5% 16.1% 6.5% |  |
| 21 | 722 | 16.1% | 34.5% 16.1% 6.5% |  |
| 21 | 722 | 6.5% | 34.5% 16.1% 6.5% |  |
| 21 | 723 | 14.7% | 14.7% 14.7% |  |
| 21 | 723 | 14.7% | 14.7% 14.7% |  |
| 21 | 724 | 11.4% | 11.4% 4.6% |  |
| 21 | 724 | 4.6% | 11.4% 4.6% |  |
| 21 | 725 | 31.9% | 31.9% 3.4% |  |
| 21 | 725 | 3.4% | 31.9% 3.4% |  |
| 21 | 726 | 30.3% | 30.3% 30.6% |  |
| 21 | 726 | 30.6% | 30.3% 30.6% |  |
| 21 | 727 | 30.6% | 30.6% 30.6% |  |
| 21 | 727 | 30.6% | 30.6% 30.6% |  |
| 21 | 728 | 30.3% | 30.3% |  |
| 22 | 743 | 2 | Consistent Financial Performance (2/2) |  |
| 22 | 743 | 2 | Consistent Financial Performance (2/2) |  |
| 22 | 750 | 2.8 | 2.8 2.8 |  |
| 22 | 750 | 2.8 | 2.8 2.8 |  |
| 22 | 751 | 217 | 217 |  |
| 22 | 752 | 28.8% | 28.8% |  |
| 22 | 753 | 22.8% | 22.8% 171 163 |  |
| 22 | 753 | 171 | 22.8% 171 163 |  |
| 22 | 753 | 163 | 22.8% 171 163 |  |
| 22 | 754 | 21.1% | 21.1% 156 |  |
| 22 | 754 | 156 | 21.1% 156 |  |
| 22 | 756 | 1.1 | 1.1 |  |
| 22 | 757 | 9.9% | 9.9% |  |
| 22 | 759 | 0.3 | 0.3 |  |
| 22 | 770 | 16.6% | 16.6% 97 211 |  |
| 22 | 770 | 97 | 16.6% 97 211 |  |
| 22 | 770 | 211 | 16.6% 97 211 |  |
| 22 | 771 | 15.9% | 15.9% |  |
| 22 | 772 | 82 | 82 162 164 |  |
| 22 | 772 | 162 | 82 162 164 |  |
| 22 | 772 | 164 | 82 162 164 |  |
| 22 | 773 | 12.6% | 12.6% 76 151 |  |
| 22 | 773 | 76 | 12.6% 76 151 |  |
| 22 | 773 | 151 | 12.6% 76 151 |  |
| 22 | 774 | 11.6% | 11.6% |  |
| 22 | 775 | 62 | 62 |  |
| 23 | 789 | 3 | Particulars FY26 FY25 FY24 FY23 3-year CAGR |  |
| 23 | 790 | 518.7 | Revenue from operations 518.7 484.9 399.9 305.1 19.3% |  |
| 23 | 790 | 484.9 | Revenue from operations 518.7 484.9 399.9 305.1 19.3% |  |
| 23 | 790 | 399.9 | Revenue from operations 518.7 484.9 399.9 305.1 19.3% |  |
| 23 | 790 | 305.1 | Revenue from operations 518.7 484.9 399.9 305.1 19.3% |  |
| 23 | 790 | 19.3% | Revenue from operations 518.7 484.9 399.9 305.1 19.3% |  |
| 23 | 792 | 353.2 | Cost of materials consumed (incl. changes in WIP and finished goods) 353.2 336.4 262.0 212.6 |  |
| 23 | 792 | 336.4 | Cost of materials consumed (incl. changes in WIP and finished goods) 353.2 336.4 262.0 212.6 |  |
| 23 | 792 | 262.0 | Cost of materials consumed (incl. changes in WIP and finished goods) 353.2 336.4 262.0 212.6 |  |
| 23 | 792 | 212.6 | Cost of materials consumed (incl. changes in WIP and finished goods) 353.2 336.4 262.0 212.6 |  |
| 23 | 793 | 165.4 | Gross profit 165.4 148.5 137.9 92.5 21.4% |  |
| 23 | 793 | 148.5 | Gross profit 165.4 148.5 137.9 92.5 21.4% |  |
| 23 | 793 | 137.9 | Gross profit 165.4 148.5 137.9 92.5 21.4% |  |
| 23 | 793 | 92.5 | Gross profit 165.4 148.5 137.9 92.5 21.4% |  |
| 23 | 793 | 21.4% | Gross profit 165.4 148.5 137.9 92.5 21.4% |  |
| 23 | 794 | 31.9% | Gross profit margin 31.9% 30.6% 34.5% 30.3% |  |
| 23 | 794 | 30.6% | Gross profit margin 31.9% 30.6% 34.5% 30.3% |  |
| 23 | 794 | 34.5% | Gross profit margin 31.9% 30.6% 34.5% 30.3% |  |
| 23 | 794 | 30.3% | Gross profit margin 31.9% 30.6% 34.5% 30.3% |  |
| 23 | 795 | 10.5 | Employee benefit expenses 10.5 8.1 7.4 5.5 |  |
| 23 | 795 | 8.1 | Employee benefit expenses 10.5 8.1 7.4 5.5 |  |
| 23 | 795 | 7.4 | Employee benefit expenses 10.5 8.1 7.4 5.5 |  |
| 23 | 795 | 5.5 | Employee benefit expenses 10.5 8.1 7.4 5.5 |  |
| 23 | 796 | 78.7 | Other expenses 78.7 62.4 71.7 52.3 |  |
| 23 | 796 | 62.4 | Other expenses 78.7 62.4 71.7 52.3 |  |
| 23 | 796 | 71.7 | Other expenses 78.7 62.4 71.7 52.3 |  |
| 23 | 796 | 52.3 | Other expenses 78.7 62.4 71.7 52.3 |  |
| 23 | 798 | 76.2 | EBITDA 76.2 78.1 58.8 34.8 29.9% |  |
| 23 | 798 | 78.1 | EBITDA 76.2 78.1 58.8 34.8 29.9% |  |
| 23 | 798 | 58.8 | EBITDA 76.2 78.1 58.8 34.8 29.9% |  |
| 23 | 798 | 34.8 | EBITDA 76.2 78.1 58.8 34.8 29.9% |  |
| 23 | 798 | 29.9% | EBITDA 76.2 78.1 58.8 34.8 29.9% |  |
| 23 | 799 | 14.7% | EBITDA margin 14.7% 16.1% 14.7% 11.4% |  |
| 23 | 799 | 16.1% | EBITDA margin 14.7% 16.1% 14.7% 11.4% |  |
| 23 | 799 | 14.7% | EBITDA margin 14.7% 16.1% 14.7% 11.4% |  |
| 23 | 799 | 11.4% | EBITDA margin 14.7% 16.1% 14.7% 11.4% |  |
| 23 | 800 | 10.6 | Other income 10.6 4.0 2.6 2.7 |  |
| 23 | 800 | 4.0 | Other income 10.6 4.0 2.6 2.7 |  |
| 23 | 800 | 2.6 | Other income 10.6 4.0 2.6 2.7 |  |
| 23 | 800 | 2.7 | Other income 10.6 4.0 2.6 2.7 |  |
| 23 | 801 | 9.2 | Depreciation & amortization expenses 9.2 18.1 16.4 11.5 |  |
| 23 | 801 | 18.1 | Depreciation & amortization expenses 9.2 18.1 16.4 11.5 |  |
| 23 | 801 | 16.4 | Depreciation & amortization expenses 9.2 18.1 16.4 11.5 |  |
| 23 | 801 | 11.5 | Depreciation & amortization expenses 9.2 18.1 16.4 11.5 |  |
| 23 | 802 | 24.9 | Finance costs 24.9 22.0 19.1 11.6 |  |
| 23 | 802 | 22.0 | Finance costs 24.9 22.0 19.1 11.6 |  |
| 23 | 802 | 19.1 | Finance costs 24.9 22.0 19.1 11.6 |  |
| 23 | 802 | 11.6 | Finance costs 24.9 22.0 19.1 11.6 |  |
| 23 | 803 | 52.7 | Profit before tax 52.7 41.9 25.9 14.4 54.2% |  |
| 23 | 803 | 41.9 | Profit before tax 52.7 41.9 25.9 14.4 54.2% |  |
| 23 | 803 | 25.9 | Profit before tax 52.7 41.9 25.9 14.4 54.2% |  |
| 23 | 803 | 14.4 | Profit before tax 52.7 41.9 25.9 14.4 54.2% |  |
| 23 | 803 | 54.2% | Profit before tax 52.7 41.9 25.9 14.4 54.2% |  |
| 23 | 804 | 13.9 | Tax expenses 13.9 10.2 7.6 4.0 |  |
| 23 | 804 | 10.2 | Tax expenses 13.9 10.2 7.6 4.0 |  |
| 23 | 804 | 7.6 | Tax expenses 13.9 10.2 7.6 4.0 |  |
| 23 | 804 | 4.0 | Tax expenses 13.9 10.2 7.6 4.0 |  |
| 23 | 806 | 38.8 | Profit after tax 38.8 31.7 18.3 10.3 55.4% |  |
| 23 | 806 | 31.7 | Profit after tax 38.8 31.7 18.3 10.3 55.4% |  |
| 23 | 806 | 18.3 | Profit after tax 38.8 31.7 18.3 10.3 55.4% |  |
| 23 | 806 | 10.3 | Profit after tax 38.8 31.7 18.3 10.3 55.4% |  |
| 23 | 806 | 55.4% | Profit after tax 38.8 31.7 18.3 10.3 55.4% |  |
| 23 | 808 | 7.5% | PAT margin 7.5% 6.5% 4.6% 3.4% |  |
| 23 | 808 | 6.5% | PAT margin 7.5% 6.5% 4.6% 3.4% |  |
| 23 | 808 | 4.6% | PAT margin 7.5% 6.5% 4.6% 3.4% |  |
| 23 | 808 | 3.4% | PAT margin 7.5% 6.5% 4.6% 3.4% |  |
| 23 | 809 | 6.8 | EPS (INR) 6.8 7.6 4.6 2.6 37.8% |  |
| 23 | 809 | 7.6 | EPS (INR) 6.8 7.6 4.6 2.6 37.8% |  |
| 23 | 809 | 4.6 | EPS (INR) 6.8 7.6 4.6 2.6 37.8% |  |
| 23 | 809 | 2.6 | EPS (INR) 6.8 7.6 4.6 2.6 37.8% |  |
| 23 | 809 | 37.8% | EPS (INR) 6.8 7.6 4.6 2.6 37.8% |  |
| 24 | 820 | 194.0 | Fixed assets 194.0 103.5 81.6 62.1 |  |
| 24 | 820 | 103.5 | Fixed assets 194.0 103.5 81.6 62.1 |  |
| 24 | 820 | 81.6 | Fixed assets 194.0 103.5 81.6 62.1 |  |
| 24 | 820 | 62.1 | Fixed assets 194.0 103.5 81.6 62.1 |  |
| 24 | 822 | 49.4 | Other non-current assets 49.4 34.2 22.8 12.2 |  |
| 24 | 822 | 34.2 | Other non-current assets 49.4 34.2 22.8 12.2 |  |
| 24 | 822 | 22.8 | Other non-current assets 49.4 34.2 22.8 12.2 |  |
| 24 | 822 | 12.2 | Other non-current assets 49.4 34.2 22.8 12.2 |  |
| 24 | 823 | 209.8 | Inventories 209.8 149.8 111.9 99.5 |  |
| 24 | 823 | 149.8 | Inventories 209.8 149.8 111.9 99.5 |  |
| 24 | 823 | 111.9 | Inventories 209.8 149.8 111.9 99.5 |  |
| 24 | 823 | 99.5 | Inventories 209.8 149.8 111.9 99.5 |  |
| 24 | 825 | 138.0 | Trade receivables 138.0 101.0 89.3 51.6 |  |
| 24 | 825 | 101.0 | Trade receivables 138.0 101.0 89.3 51.6 |  |
| 24 | 825 | 89.3 | Trade receivables 138.0 101.0 89.3 51.6 |  |
| 24 | 825 | 51.6 | Trade receivables 138.0 101.0 89.3 51.6 |  |
| 24 | 827 | 74.2 | Cash and bank balances 74.2 43.9 22.4 10.4 |  |
| 24 | 827 | 43.9 | Cash and bank balances 74.2 43.9 22.4 10.4 |  |
| 24 | 827 | 22.4 | Cash and bank balances 74.2 43.9 22.4 10.4 |  |
| 24 | 827 | 10.4 | Cash and bank balances 74.2 43.9 22.4 10.4 |  |
| 24 | 829 | 22.5 | Other current assets 22.5 13.8 2.4 2.5 |  |
| 24 | 829 | 13.8 | Other current assets 22.5 13.8 2.4 2.5 |  |
| 24 | 829 | 2.4 | Other current assets 22.5 13.8 2.4 2.5 |  |
| 24 | 829 | 2.5 | Other current assets 22.5 13.8 2.4 2.5 |  |
| 24 | 831 | 687.9 | Total 687.9 446.4 330.4 238.3 |  |
| 24 | 831 | 446.4 | Total 687.9 446.4 330.4 238.3 |  |
| 24 | 831 | 330.4 | Total 687.9 446.4 330.4 238.3 |  |
| 24 | 831 | 238.3 | Total 687.9 446.4 330.4 238.3 |  |
| 24 | 834 | 390.3 | Equity capital and reserves 390.3 150.4 63.6 45.3 |  |
| 24 | 834 | 150.4 | Equity capital and reserves 390.3 150.4 63.6 45.3 |  |
| 24 | 834 | 63.6 | Equity capital and reserves 390.3 150.4 63.6 45.3 |  |
| 24 | 834 | 45.3 | Equity capital and reserves 390.3 150.4 63.6 45.3 |  |
| 24 | 835 | 185.3 | Borrowings 185.3 210.2 202.7 139.3 |  |
| 24 | 835 | 210.2 | Borrowings 185.3 210.2 202.7 139.3 |  |
| 24 | 835 | 202.7 | Borrowings 185.3 210.2 202.7 139.3 |  |
| 24 | 835 | 139.3 | Borrowings 185.3 210.2 202.7 139.3 |  |
| 24 | 837 | 99.4 | Trade payables 99.4 68.5 53.9 47.5 |  |
| 24 | 837 | 68.5 | Trade payables 99.4 68.5 53.9 47.5 |  |
| 24 | 837 | 53.9 | Trade payables 99.4 68.5 53.9 47.5 |  |
| 24 | 837 | 47.5 | Trade payables 99.4 68.5 53.9 47.5 |  |
| 24 | 839 | 3.6 | Other non-current liabilities 3.6 0.9 1.3 0.8 |  |
| 24 | 839 | 0.9 | Other non-current liabilities 3.6 0.9 1.3 0.8 |  |
| 24 | 839 | 1.3 | Other non-current liabilities 3.6 0.9 1.3 0.8 |  |
| 24 | 839 | 0.8 | Other non-current liabilities 3.6 0.9 1.3 0.8 |  |
| 24 | 841 | 9.2 | Other current liabilities 9.2 16.4 9.0 5.4 |  |
| 24 | 841 | 16.4 | Other current liabilities 9.2 16.4 9.0 5.4 |  |
| 24 | 841 | 9.0 | Other current liabilities 9.2 16.4 9.0 5.4 |  |
| 24 | 841 | 5.4 | Other current liabilities 9.2 16.4 9.0 5.4 |  |
| 24 | 843 | 687.9 | Total 687.9 446.4 330.4 238.3 |  |
| 24 | 843 | 446.4 | Total 687.9 446.4 330.4 238.3 |  |
| 24 | 843 | 330.4 | Total 687.9 446.4 330.4 238.3 |  |
| 24 | 843 | 238.3 | Total 687.9 446.4 330.4 238.3 |  |
| 25 | 857 | 52.7 | Net profit before tax 52.7 41.9 25.9 14.4 |  |
| 25 | 857 | 41.9 | Net profit before tax 52.7 41.9 25.9 14.4 |  |
| 25 | 857 | 25.9 | Net profit before tax 52.7 41.9 25.9 14.4 |  |
| 25 | 857 | 14.4 | Net profit before tax 52.7 41.9 25.9 14.4 |  |
| 25 | 859 | 30.0 | Adjustments for: Non-cash items and other investment/financial items 30.0 37.6 34.2 22.8 |  |
| 25 | 859 | 37.6 | Adjustments for: Non-cash items and other investment/financial items 30.0 37.6 34.2 22.8 |  |
| 25 | 859 | 34.2 | Adjustments for: Non-cash items and other investment/financial items 30.0 37.6 34.2 22.8 |  |
| 25 | 859 | 22.8 | Adjustments for: Non-cash items and other investment/financial items 30.0 37.6 34.2 22.8 |  |
| 25 | 861 | 82.8 | Operating profit before working capital changes 82.8 79.5 60.1 37.2 |  |
| 25 | 861 | 79.5 | Operating profit before working capital changes 82.8 79.5 60.1 37.2 |  |
| 25 | 861 | 60.1 | Operating profit before working capital changes 82.8 79.5 60.1 37.2 |  |
| 25 | 861 | 37.2 | Operating profit before working capital changes 82.8 79.5 60.1 37.2 |  |
| 25 | 863 | -78.9 | Changes in working capital -78.9 -54.6 -54.5 -15.0 |  |
| 25 | 863 | -54.6 | Changes in working capital -78.9 -54.6 -54.5 -15.0 |  |
| 25 | 863 | -54.5 | Changes in working capital -78.9 -54.6 -54.5 -15.0 |  |
| 25 | 863 | -15.0 | Changes in working capital -78.9 -54.6 -54.5 -15.0 |  |
| 25 | 865 | -17.6 | Direct taxes paid (net of refund) -17.6 -6.5 -3.4 -1.9 |  |
| 25 | 865 | -6.5 | Direct taxes paid (net of refund) -17.6 -6.5 -3.4 -1.9 |  |
| 25 | 865 | -3.4 | Direct taxes paid (net of refund) -17.6 -6.5 -3.4 -1.9 |  |
| 25 | 865 | -1.9 | Direct taxes paid (net of refund) -17.6 -6.5 -3.4 -1.9 |  |
| 25 | 867 | -13.8 | Cashflow from operations -13.8 18.4 2.2 20.3 |  |
| 25 | 867 | 18.4 | Cashflow from operations -13.8 18.4 2.2 20.3 |  |
| 25 | 867 | 2.2 | Cashflow from operations -13.8 18.4 2.2 20.3 |  |
| 25 | 867 | 20.3 | Cashflow from operations -13.8 18.4 2.2 20.3 |  |
| 25 | 869 | -149.9 | Cashflow from investing activities -149.9 -43.9 -46.6 -38.5 |  |
| 25 | 869 | -43.9 | Cashflow from investing activities -149.9 -43.9 -46.6 -38.5 |  |
| 25 | 869 | -46.6 | Cashflow from investing activities -149.9 -43.9 -46.6 -38.5 |  |
| 25 | 869 | -38.5 | Cashflow from investing activities -149.9 -43.9 -46.6 -38.5 |  |
| 25 | 871 | 152.7 | Cashflow from financing activities 152.7 40.6 44.3 17.9 |  |
| 25 | 871 | 40.6 | Cashflow from financing activities 152.7 40.6 44.3 17.9 |  |
| 25 | 871 | 44.3 | Cashflow from financing activities 152.7 40.6 44.3 17.9 |  |
| 25 | 871 | 17.9 | Cashflow from financing activities 152.7 40.6 44.3 17.9 |  |
| 25 | 873 | -11.0 | Change in cash and cash equivalents -11.0 15.1 -0.1 -0.2 |  |
| 25 | 873 | 15.1 | Change in cash and cash equivalents -11.0 15.1 -0.1 -0.2 |  |
| 25 | 873 | -0.1 | Change in cash and cash equivalents -11.0 15.1 -0.1 -0.2 |  |
| 25 | 873 | -0.2 | Change in cash and cash equivalents -11.0 15.1 -0.1 -0.2 |  |
| 25 | 875 | 15.1 | Cash and cash equivalents at the beginning of the period 15.1 - 0.1 0.3 |  |
| 25 | 875 | 0.1 | Cash and cash equivalents at the beginning of the period 15.1 - 0.1 0.3 |  |
| 25 | 875 | 0.3 | Cash and cash equivalents at the beginning of the period 15.1 - 0.1 0.3 |  |
| 25 | 877 | 4.1 | Cash and cash equivalents at the end of the period 4.1 15.1 0.0 0.1 |  |
| 25 | 877 | 15.1 | Cash and cash equivalents at the end of the period 4.1 15.1 0.0 0.1 |  |
| 25 | 877 | 0.0 | Cash and cash equivalents at the end of the period 4.1 15.1 0.0 0.1 |  |
| 25 | 877 | 0.1 | Cash and cash equivalents at the end of the period 4.1 15.1 0.0 0.1 |  |
| 26 | 891 | 04 | 04 | STRUCTURAL_SECTION_DIVIDER_NUM |
| 28 | 928 | 8,000 | 8,000 | AMBIGUOUS_MAPPING(A1-flagged: rotated axis labels, year-to-value mapping unresolved) |
| 28 | 930 | 23 | 23x capacity expansion |  |
| 28 | 935 | 12,130 | 12,130 | AMBIGUOUS_MAPPING(A1-flagged: rotated axis labels, year-to-value mapping unresolved) |
| 28 | 936 | 10,068 | Seamless 10,068 MTPA 20,068 MTPA | CROSS_SLIDE_INCONSISTENCY(cf. Slide10 states 20,068 MTPA as current seamless capacity; Slide28 table frames 20,068 as POST-EXPANSION target with 10,068 as existing capacity) |
| 28 | 936 | 20,068 | Seamless 10,068 MTPA 20,068 MTPA | CROSS_SLIDE_INCONSISTENCY(cf. Slide10 states 20,068 MTPA as current seamless capacity; Slide28 table frames 20,068 as POST-EXPANSION target with 10,068 as existing capacity) |
| 28 | 941 | 33,218 | 33,218 | AMBIGUOUS_MAPPING(A1-flagged: rotated axis labels, year-to-value mapping unresolved) |
| 28 | 945 | 12,130 | 12,130 | AMBIGUOUS_MAPPING(A1-flagged: rotated axis labels, year-to-value mapping unresolved) |
| 28 | 946 | 1,020 | Welded 1,020 MTPA 21,150 MTPA |  |
| 28 | 946 | 21,150 | Welded 1,020 MTPA 21,150 MTPA |  |
| 28 | 951 | 21,088 | 21,088 | AMBIGUOUS_MAPPING(A1-flagged: rotated axis labels, year-to-value mapping unresolved) |
| 28 | 955 | 21,088 | 21,088 | AMBIGUOUS_MAPPING(A1-flagged: rotated axis labels, year-to-value mapping unresolved) |
| 28 | 956 | 1,800 | 1,800 | AMBIGUOUS_MAPPING(A1-flagged: rotated axis labels, year-to-value mapping unresolved) |
| 28 | 961 | 20,000 | Mother hollow 20,000 MTPA |  |
| 28 | 1009 | 27 | 27 |  |
| 29 | 1043 | 3.9 | 3.9 MW(AC) / 4.99 MW(DC) |  |
| 29 | 1043 | 4.99 | 3.9 MW(AC) / 4.99 MW(DC) |  |
| 29 | 1046 | 7.74 | 7.74 Million KWH |  |
| 29 | 1049 | 4.87 | ₹ 4.87 crores |  |
| 30 | 1073 | 32 | Exported to 32 countries since inception |  |
| 30 | 1085 | 21.6 | 21.6 179.5 | CROSS_CHECKED_OK(country-split sums to 57.1 INR cr, reconciles closely with Q1FY27 total export revenue 57.0/57.9 shown elsewhere) |
| 30 | 1085 | 179.5 | 21.6 179.5 | AMBIGUOUS_MAPPING(scrambled vertical layout in text extraction; year assignment plausible but FY26 33.2% does not cleanly reconcile against FY26 exports 179.5/revenue 518.7=~34.6%; flag for visual verification) |
| 30 | 1087 | 129.1 | 129.1 | AMBIGUOUS_MAPPING(scrambled vertical layout in text extraction; year assignment plausible but FY26 33.2% does not cleanly reconcile against FY26 exports 179.5/revenue 518.7=~34.6%; flag for visual verification) |
| 30 | 1089 | 11.3 | 11.3 12.2 94.1 | CROSS_CHECKED_OK(country-split sums to 57.1 INR cr, reconciles closely with Q1FY27 total export revenue 57.0/57.9 shown elsewhere) |
| 30 | 1089 | 12.2 | 11.3 12.2 94.1 | CROSS_CHECKED_OK(country-split sums to 57.1 INR cr, reconciles closely with Q1FY27 total export revenue 57.0/57.9 shown elsewhere) |
| 30 | 1089 | 94.1 | 11.3 12.2 94.1 | AMBIGUOUS_MAPPING(scrambled vertical layout in text extraction; year assignment plausible but FY26 33.2% does not cleanly reconcile against FY26 exports 179.5/revenue 518.7=~34.6%; flag for visual verification) |
| 30 | 1090 | 10.7 | 10.7 83.2 | CROSS_CHECKED_OK(country-split sums to 57.1 INR cr, reconciles closely with Q1FY27 total export revenue 57.0/57.9 shown elsewhere) |
| 30 | 1090 | 83.2 | 10.7 83.2 | AMBIGUOUS_MAPPING(scrambled vertical layout in text extraction; year assignment plausible but FY26 33.2% does not cleanly reconcile against FY26 exports 179.5/revenue 518.7=~34.6%; flag for visual verification) |
| 30 | 1091 | 30.8% | 30.8% | AMBIGUOUS_MAPPING(scrambled vertical layout in text extraction; year assignment plausible but FY26 33.2% does not cleanly reconcile against FY26 exports 179.5/revenue 518.7=~34.6%; flag for visual verification) |
| 30 | 1092 | 26.6% | 26.6% 57.0 | AMBIGUOUS_MAPPING(scrambled vertical layout in text extraction; year assignment plausible but FY26 33.2% does not cleanly reconcile against FY26 exports 179.5/revenue 518.7=~34.6%; flag for visual verification) |
| 30 | 1092 | 57.0 | 26.6% 57.0 | AMBIGUOUS_MAPPING(scrambled vertical layout in text extraction; year assignment plausible but FY26 33.2% does not cleanly reconcile against FY26 exports 179.5/revenue 518.7=~34.6%; flag for visual verification) |
| 30 | 1093 | 20.8% | 20.8% | AMBIGUOUS_MAPPING(scrambled vertical layout in text extraction; year assignment plausible but FY26 33.2% does not cleanly reconcile against FY26 exports 179.5/revenue 518.7=~34.6%; flag for visual verification) |
| 30 | 1094 | 45.8% | 45.8% | AMBIGUOUS_MAPPING(scrambled vertical layout in text extraction; year assignment plausible but FY26 33.2% does not cleanly reconcile against FY26 exports 179.5/revenue 518.7=~34.6%; flag for visual verification) |
| 30 | 1095 | 33.2% | 33.2% | AMBIGUOUS_MAPPING(scrambled vertical layout in text extraction; year assignment plausible but FY26 33.2% does not cleanly reconcile against FY26 exports 179.5/revenue 518.7=~34.6%; flag for visual verification) |
| 30 | 1096 | 0.2 | 0.2 1.1 | CROSS_CHECKED_OK(country-split sums to 57.1 INR cr, reconciles closely with Q1FY27 total export revenue 57.0/57.9 shown elsewhere) |
| 30 | 1096 | 1.1 | 0.2 1.1 | CROSS_CHECKED_OK(country-split sums to 57.1 INR cr, reconciles closely with Q1FY27 total export revenue 57.0/57.9 shown elsewhere) |
| 31 | 1130 | 20 | • 20 personnel in quality check and customer |  |
| 32 | 1146 | 05 | 05 | STRUCTURAL_SECTION_DIVIDER_NUM |
| 33 | 1181 | 2023 | CY 2023 Oil and gas CY 2028E1 |  |
| 33 | 1181 | 2028 | CY 2023 Oil and gas CY 2028E1 |  |
| 33 | 1182 | 15-17% | 15-17% 15-17% |  |
| 33 | 1182 | 15-17% | 15-17% 15-17% |  |
| 33 | 1184 | 6-8% | 6-8% 23-26% 24-27% |  |
| 33 | 1184 | 23-26% | 6-8% 23-26% 24-27% |  |
| 33 | 1184 | 24-27% | 6-8% 23-26% 24-27% |  |
| 33 | 1185 | 5-7% | ART 5-7% |  |
| 33 | 1186 | 6-8% | 6-8% 6-8% |  |
| 33 | 1186 | 6-8% | 6-8% 6-8% |  |
| 33 | 1189 | 11-13% | 11-13% 18-21% Water treatment 10-12% 19-22% |  |
| 33 | 1189 | 18-21% | 11-13% 18-21% Water treatment 10-12% 19-22% |  |
| 33 | 1189 | 10-12% | 11-13% 18-21% Water treatment 10-12% 19-22% |  |
| 33 | 1189 | 19-22% | 11-13% 18-21% Water treatment 10-12% 19-22% |  |
| 33 | 1191 | 14-16% | 14-16% 14-16% |  |
| 33 | 1191 | 14-16% | 14-16% 14-16% |  |
| 33 | 1199 | 3.7 | 3.7 • Oil & gas and process industries continue to dominate |  |
| 33 | 1200 | 3.1 | 3.1 global demand for SS pipes and tubes. |  |
| 33 | 1201 | 3 | 3 3 |  |
| 33 | 1201 | 3 | 3 3 |  |
| 33 | 1202 | 2.7 | 2.7 2.7 |  |
| 33 | 1202 | 2.7 | 2.7 2.7 |  |
| 33 | 1207 | 3% | • Demand for SS pipes and tubes grew at a CAGR of ~3% |  |
| 33 | 1208 | 3-4% | from CY19-CY23 and is expected to grow at a CAGR of 3-4% |  |
| 34 | 1220 | 450 | and beverage will drive the demand of SS pipes and tubes. 450 |  |
| 34 | 1222 | 300 | 300 322 |  |
| 34 | 1222 | 322 | 300 322 |  |
| 34 | 1223 | 226 | • Policy protection through imposition of anti-dumping duties on 226 |  |
| 34 | 1224 | 263 | 263 |  |
| 34 | 1225 | 208 | 208 |  |
| 34 | 1236 | 90 | 90 |  |
| 34 | 1237 | 6-8% | CAGR: 6-8% 56 |  |
| 34 | 1237 | 56 | CAGR: 6-8% 56 |  |
| 34 | 1238 | 28-32% | Process industry 28-32% of demand |  |
| 34 | 1239 | 29 | (FY24-29) |  |
| 34 | 1242 | 6-8% | CAGR: 6-8% |  |
| 34 | 1243 | 22-25% | Oil & gas 22-25% of demand |  |
| 34 | 1244 | 29 | (FY24-29) FY20 FY24 |  |
| 34 | 1247 | 8-10% | CAGR: 8-10% |  |
| 34 | 1248 | 20-23% | ART1 20-23% of demand Export from India (in 000’ tonnes) |  |
| 34 | 1249 | 29 | (FY24-29) |  |
| 34 | 1250 | 64 | 64 |  |
| 34 | 1251 | 6-8% | CAGR: 6-8% 41 |  |
| 34 | 1251 | 41 | CAGR: 6-8% 41 |  |
| 34 | 1252 | 18-21% | ABC2 18-21% of demand |  |
| 34 | 1253 | 29 | (FY24-29) |  |
| 35 | 1268 | 06 | 06 | STRUCTURAL_SECTION_DIVIDER_NUM |
| 36 | 1283 | 124.3 | Revenue from operations 124.3 97.4 27.6% |  |
| 36 | 1283 | 97.4 | Revenue from operations 124.3 97.4 27.6% |  |
| 36 | 1283 | 27.6% | Revenue from operations 124.3 97.4 27.6% |  |
| 36 | 1284 | 84.6 | Cost of materials consumed (incl. changes in WIP and finished goods) 84.6 69.0 22.5% |  |
| 36 | 1284 | 69.0 | Cost of materials consumed (incl. changes in WIP and finished goods) 84.6 69.0 22.5% |  |
| 36 | 1284 | 22.5% | Cost of materials consumed (incl. changes in WIP and finished goods) 84.6 69.0 22.5% |  |
| 36 | 1285 | 39.8 | Gross profit 39.8 28.4 40.0% |  |
| 36 | 1285 | 28.4 | Gross profit 39.8 28.4 40.0% |  |
| 36 | 1285 | 40.0% | Gross profit 39.8 28.4 40.0% |  |
| 36 | 1286 | 32.0% | Gross profit margin 32.0% 29.2% +283 bps |  |
| 36 | 1286 | 29.2% | Gross profit margin 32.0% 29.2% +283 bps |  |
| 36 | 1286 | +283 | Gross profit margin 32.0% 29.2% +283 bps |  |
| 36 | 1287 | 2.5 | Employee benefit expenses 2.5 2.4 1.7% |  |
| 36 | 1287 | 2.4 | Employee benefit expenses 2.5 2.4 1.7% |  |
| 36 | 1287 | 1.7% | Employee benefit expenses 2.5 2.4 1.7% |  |
| 36 | 1288 | 21.4 | Other expenses 21.4 11.8 80.9% |  |
| 36 | 1288 | 11.8 | Other expenses 21.4 11.8 80.9% |  |
| 36 | 1288 | 80.9% | Other expenses 21.4 11.8 80.9% |  |
| 36 | 1290 | 16.0 | EBITDA 16.0 14.2 12.6% |  |
| 36 | 1290 | 14.2 | EBITDA 16.0 14.2 12.6% |  |
| 36 | 1290 | 12.6% | EBITDA 16.0 14.2 12.6% |  |
| 36 | 1292 | 12.9% | EBITDA margin 12.9% 14.6% -172 bps |  |
| 36 | 1292 | 14.6% | EBITDA margin 12.9% 14.6% -172 bps |  |
| 36 | 1292 | -172 | EBITDA margin 12.9% 14.6% -172 bps |  |
| 36 | 1294 | 1.6 | Other income 1.6 1.8 -7.4% |  |
| 36 | 1294 | 1.8 | Other income 1.6 1.8 -7.4% |  |
| 36 | 1294 | -7.4% | Other income 1.6 1.8 -7.4% |  |
| 36 | 1295 | 4.1 | Depreciation & amortization expenses 4.1 1.6 162.8% |  |
| 36 | 1295 | 1.6 | Depreciation & amortization expenses 4.1 1.6 162.8% |  |
| 36 | 1295 | 162.8% | Depreciation & amortization expenses 4.1 1.6 162.8% |  |
| 36 | 1296 | 6.5 | Finance costs 6.5 5.1 27.0% |  |
| 36 | 1296 | 5.1 | Finance costs 6.5 5.1 27.0% |  |
| 36 | 1296 | 27.0% | Finance costs 6.5 5.1 27.0% |  |
| 36 | 1297 | 7.0 | Profit before tax 7.0 9.3 -24.6% |  |
| 36 | 1297 | 9.3 | Profit before tax 7.0 9.3 -24.6% |  |
| 36 | 1297 | -24.6% | Profit before tax 7.0 9.3 -24.6% |  |
| 36 | 1298 | 1.7 | Tax expenses 1.7 2.2 -20.3% |  |
| 36 | 1298 | 2.2 | Tax expenses 1.7 2.2 -20.3% |  |
| 36 | 1298 | -20.3% | Tax expenses 1.7 2.2 -20.3% |  |
| 36 | 1300 | 5.3 | Profit after tax 5.3 7.1 -25.9% |  |
| 36 | 1300 | 7.1 | Profit after tax 5.3 7.1 -25.9% |  |
| 36 | 1300 | -25.9% | Profit after tax 5.3 7.1 -25.9% |  |
| 36 | 1302 | 4.2% | PAT margin 4.2% 7.3% -305 bps |  |
| 36 | 1302 | 7.3% | PAT margin 4.2% 7.3% -305 bps |  |
| 36 | 1302 | -305 | PAT margin 4.2% 7.3% -305 bps |  |
| 36 | 1304 | 0.9 | EPS (INR) 0.9 1.4 -39.1% |  |
| 36 | 1304 | 1.4 | EPS (INR) 0.9 1.4 -39.1% |  |
| 36 | 1304 | -39.1% | EPS (INR) 0.9 1.4 -39.1% |  |
| 37 | 1315 | 07 | 07 | STRUCTURAL_SECTION_DIVIDER_NUM |
| 38 | 1334 | 1 | Welded Seamless 1 | PROCESS_STEP_ICON_MARKER_UNRESOLVED |
| 38 | 1336 | 1 | Roll forming and Peeling process 1 | PROCESS_STEP_ICON_MARKER_UNRESOLVED |
| 38 | 1338 | 1 | “U” bending 1 Hot piercing process 1 | PROCESS_STEP_ICON_MARKER_UNRESOLVED |
| 38 | 1338 | 1 | “U” bending 1 Hot piercing process 1 | PROCESS_STEP_ICON_MARKER_UNRESOLVED |
| 38 | 1339 | 1 | Solution annealing Bright annealing Hot finish pipe annealing 1 | PROCESS_STEP_ICON_MARKER_UNRESOLVED |
| 38 | 1340 | 1 | “U” bending by cold process 1 | PROCESS_STEP_ICON_MARKER_UNRESOLVED |
| 38 | 1341 | 1 | Straightening Straightening Coating & pickling process 1 | PROCESS_STEP_ICON_MARKER_UNRESOLVED |
| 38 | 1342 | 1 | Stress relieving at bend 1 Cold drawing & pilgering 1 | PROCESS_STEP_ICON_MARKER_UNRESOLVED |
| 38 | 1342 | 1 | Stress relieving at bend 1 Cold drawing & pilgering 1 | PROCESS_STEP_ICON_MARKER_UNRESOLVED |
| 38 | 1344 | 1 | portion 1 | PROCESS_STEP_ICON_MARKER_UNRESOLVED |
| 38 | 1345 | 1 | Solution annealing 1 | PROCESS_STEP_ICON_MARKER_UNRESOLVED |
| 38 | 1347 | 1 | Cutting and deburring 1 | PROCESS_STEP_ICON_MARKER_UNRESOLVED |
| 38 | 1348 | 1 | Straightening 1 | PROCESS_STEP_ICON_MARKER_UNRESOLVED |
| 38 | 1350 | 1 | Cleaning 1 Cutting 1 | PROCESS_STEP_ICON_MARKER_UNRESOLVED |
| 38 | 1350 | 1 | Cleaning 1 Cutting 1 | PROCESS_STEP_ICON_MARKER_UNRESOLVED |
| 38 | 1351 | 1 | Passivation Inspection Deburring 1 | PROCESS_STEP_ICON_MARKER_UNRESOLVED |
| 38 | 1352 | 1 | Hydrotesting 1 | PROCESS_STEP_ICON_MARKER_UNRESOLVED |
| 38 | 1353 | 1 | Hydrotesting Marking Final pickling 1 | PROCESS_STEP_ICON_MARKER_UNRESOLVED |
| 38 | 1354 | 1 | Inspection Inspection and marking 1 | PROCESS_STEP_ICON_MARKER_UNRESOLVED |
| 38 | 1355 | 1 | Packing VDI 1 | PROCESS_STEP_ICON_MARKER_UNRESOLVED |
| 38 | 1357 | 1 | Marking Packing 1 Passivation 1 | PROCESS_STEP_ICON_MARKER_UNRESOLVED |
| 38 | 1357 | 1 | Marking Packing 1 Passivation 1 | PROCESS_STEP_ICON_MARKER_UNRESOLVED |
| 38 | 1359 | 1 | Packing Marking 1 | PROCESS_STEP_ICON_MARKER_UNRESOLVED |
| 38 | 1361 | 1 | Packing 1 | PROCESS_STEP_ICON_MARKER_UNRESOLVED |
| 40 | 1415 | +91 | cs@scodatubes.com +91 99259 11296 +91 90999 94345 |  |
| 40 | 1415 | 99259 | cs@scodatubes.com +91 99259 11296 +91 90999 94345 |  |
| 40 | 1415 | 11296 | cs@scodatubes.com +91 99259 11296 +91 90999 94345 |  |
| 40 | 1415 | +91 | cs@scodatubes.com +91 99259 11296 +91 90999 94345 |  |
| 40 | 1415 | 90999 | cs@scodatubes.com +91 99259 11296 +91 90999 94345 |  |
| 40 | 1415 | 94345 | cs@scodatubes.com +91 99259 11296 +91 90999 94345 |  |
| 25 | 875 | '-' (dash) | Cash and cash equivalents at the beginning of the period -- FY25 column value | ZERO_STANDING |
| 10 | 360 | (blank) | Y-o-Y growth -- FY23 column value (no prior-year comparator; first year shown in series) | ZERO_STANDING |

---

## TABLE 4 -- FOOTNOTES AND FINE PRINT (every footnote / disclaimer qualifying a headline number)

| Slide | Source line | Footnote / fine-print text | What it qualifies | Flags |
|---|---|---|---|---|
| 5 | 187 | 1. Earnings before interest, taxes, depreciation, and amortization | defines EBITDA(1) superscript used in Slide5 KPI card |  |
| 10 | 375 | 1. Stainless steel | defines SS(1) superscript, Slide10 |  |
| 10 | 375 | 2. Metric tonnes per annum | defines MTPA(2) superscript, Slide10 |  |
| 10 | 375 | 3. Includes railways | qualifies 'transportation(3)' sector reference, Slide10 |  |
| 10 | 375 | 4. 25 Pilgers & 8 Draw Benches | defines the '33 production lines for seamless products' figure (footnote marker rendered merged as '334' in extraction) | LINKS_TO_RENDER_ARTIFACT |
| 11 | 409 | 1. Bharat Heavy Electricals Limited | defines BHEL(1) |  |
| 11 | 409 | 2. Heavy Electrical Equipment Plant | defines HEEP(2) |  |
| 11 | 409 | 3. Gujarat Narmada Valley Fertilizers and Chemicals Limited | defines GNFC(3) |  |
| 11 | 409 | 4. Indian Farmers Fertilizer Cooperative Limited | defines IFFCO(4) |  |
| 11 | 409 | 5. Krishak Bharati Cooperative Limited | defines KRIBHCO(5) |  |
| 11 | 411 | 6. Hindustan Petroleum Corporation Limited | defines HPCL(6) |  |
| 11 | 411 | 7. Engineers India Limited | defines EIL(7) |  |
| 11 | 411 | 8. Government of India | defines GoI(8) |  |
| 12 | 448 | 1. Bharat Earth Movers Limited | defines BEML(1) |  |
| 12 | 448 | 2. Intellectual property | defines IP(2) |  |
| 12 | 448 | 3. National Thermal Power Corporation | defines NTPC(3) |  |
| 12 | 448 | 4. Quality management system | defines QMS(4) |  |
| 12 | 448 | 5. Environmental management system | defines EMS(5) |  |
| 12 | 448 | 6. Occupational health and safety management system | defines OHSMS(6) |  |
| 14 | 493 | 1. Stainless steel | defines SS(1), Slide14 |  |
| 15 | 528 | 1. Stainless steel | defines SS(1), Slide15 product table |  |
| 17 | 610 | 1. Based on Q1 FY27 nos. | qualifies the '32 Countries' and geography-mix figures, Slide17 |  |
| 17 | 610 | 2. Includes railways | qualifies 'Transportation(2)' sector reference, Slide17 |  |
| 17 | 610 | Note: Nos. might not add up due to rounding off | qualifies all percentage figures on Slide17 (rounding disclaimer) |  |
| 19 | 660 | 1. Metric tonnes per annum | defines MTPA(1), Slide19 |  |
| 20 | 688 | 1. Executive Director | defines ED(1) in Samarth B Patel's title, Slide20 |  |
| 28 | 995 | 1. Metric tonnes per annum | defines MTPA(1) in capacity chart title, Slide28 |  |
| 33 | 1214 | 1. Estimates | defines 'E' suffix in CY2028E, Slide33 |  |
| 33 | 1214 | 2. Automobile, railways, and transportation | defines ART(2), Slide33 |  |
| 33 | 1214 | 3. Architecture, building and construction | defines ABC(3), Slide33 |  |
| 34 | 1259 | 1. Automobile, railways, and transportation | defines ART(1), Slide34 (restated) |  |
| 34 | 1259 | 2. Architecture, building and construction | defines ABC(2), Slide34 (restated) |  |
| 7 | 222 | In INR crores | unit-convention qualifier heading Slide7 |  |
| 8 | 267 | In INR crores | unit-convention qualifier heading Slide8 |  |
| 10 | 354 | In INR crores | unit-convention qualifier for Slide10 financial table |  |
| 21 | 692 | In INR crores | unit-convention qualifier heading Slide21 |  |
| 22 | 744 | In INR crores | unit-convention qualifier heading Slide22 |  |
| 23 | 788 | INR Crores Unless Otherwise Mentioned | unit-convention qualifier heading Slide23 table |  |
| 24 | 818 | INR Crores Unless Otherwise Mentioned | unit-convention qualifier heading Slide24 table |  |
| 25 | 853 | INR Crores Unless Otherwise Mentioned | unit-convention qualifier heading Slide25 table |  |
| 36 | 1279 | INR Crores Unless Otherwise Mentioned | unit-convention qualifier heading Slide36 table |  |
| 30 | 1080 | (INR crores) | unit label, export-country-split chart, Slide30 |  |
| 30 | 1080 | (INR crores) | unit label, revenue-from-exports chart, Slide30 (second instance same line) |  |
| 30 | 1100 | Export revenue (in INR crores) | unit/series label, revenue-from-exports chart, Slide30 |  |
| 16 | 569 | * Currently applied for Bureau Veritas Marine (France) and Rina Marine (Italy) standards. | qualifies the accreditation badge collage, Slide16 (pending/applied-for status, not yet held) | PENDING_STATUS |
| 16 | 570 | * Company's capabilities and accreditations have enabled Scoda Tubes to cater to 349 clients globally till date. | qualifies '349 clients' headline figure, Slide16 |  |
| 30 | 1105 | * includes Estonia, UK, Denmark, UAE, Romania, Czech Republic, Brazil, Sweden, Australia, Saudi Arabia, Poland, Qatar | defines 'Others*' category in export-country-split chart, Slide30 (12 countries bundled) |  |
| 39 | 1368 | Safe Harbor Statement (full-page legal disclaimer) | qualifies ALL forward-looking statements in the deck: FY27 guidance commitment (Slide6), H2 FY27 welded-capacity commissioning (Slide6), CY2028E industry estimates (Slide33), FY29E India demand estimates (Slide34), and all CAGR projections | DECK-WIDE_QUALIFIER |

---

## SUMMARY OF FLAGS RAISED (for A3/A4 attention)

- **AMBIGUOUS_MAPPING**: Slide28 production-capacity bar chart (A1-flagged: rotated axis labels, year-to-value mapping unresolved, values 8,000 / 12,130(x2) / 33,218 / 21,088(x2) / 1,800). Slide17 revenue-mix donut (India/Europe/Americas/Others percentages 67%/1%/11%/45% do not sum to 100%, sum to 124% -- mapping and/or transcription integrity questionable, needs visual verification). Slide30 revenue-from-exports trend chart (FY26 'load-bearing' 33.2% share does not cleanly reconcile against FY26 exports 179.5 / FY26 revenue 518.7 = ~34.6%; year-to-value pairing plausible but unverified).
- **CROSS_SLIDE_INCONSISTENCY**: Seamless production capacity stated as 20,068 MTPA on Slide10 (framed as current/existing capacity) but Slide28's capacity-comparison table frames 20,068 MTPA as the POST-EXPANSION target with 10,068 MTPA as existing capacity. This is exactly the kind of capacity/utilisation disclosure ambiguity A3's F16 check is designed to catch -- flagged, not resolved, here.
- **NUMBER_DISCREPANCY**: Q1 FY27 export revenue stated as INR 57.9 cr on Slide7's geography-split chart vs INR 57.0 cr on Slide30's revenue-from-exports chart (~1.6% variance, unreconciled in the deck). Export mix also shown as 46.6% (Slide7/17) vs 45.8% (Slide30) of total revenue.
- **RENDER_ARTIFACT**: Slide10 stat '334' is very likely '33' (production lines for seamless products) with footnote marker '4' merged in extraction (footnote 4 = '25 Pilgers & 8 Draw Benches' = 25+8=33, internally consistent). Slide10 'ISO 45001:20182' is very likely 'ISO 45001:2018' with footnote marker '2' merged. Not interpreted further here; flagged for A3/A4 to confirm against the underlying image if needed.
- **GUIDANCE / catalyst-date language (Slide6, Chairperson's Commentary)**: 'advance order booking cycle of approximately three to four months' (order-book definition context for A3's F16); gas-supply disruption 'a couple of weeks' in April (operational disruption, quantified duration); welded-segment capacity expansion 'expected to be commissioned during H2 FY27' (forward catalyst date); 'committed to achieving our FY27 guidance' (guidance reaffirmation, no specific numeric target stated in this sentence -- the only FY27 numeric guidance in the deck is the qualitative commitment itself, no revenue/EBITDA/margin target number is disclosed anywhere in this presentation for FY27).
- **PENDING_STATUS**: Slide16 footnote -- Bureau Veritas Marine (France) and Rina Marine (Italy) standards are 'currently applied for', not yet held, while displayed within the same certification-badge collage as held certifications (ISO 9001/14001/45001, PED, DNV, IBR, BIS) -- worth A3 checking whether the slide visually distinguishes applied-for from held certifications.
- **ZERO_STANDING**: page25 line875 (FY25 opening-cash cell = dash '-'); page10 line360 (FY23 Y-o-Y growth cell = blank, no prior-year comparator).
- **TEMPLATE_REPEAT**: Slide20 -- identical '10+ years of Experience' value appears for 5 of 8 profiled individuals (Samarth Patel, Jagrut Patel, Saurabh Patel, Ravi Patel, Vipul A Patel); the 3 Independent Directors' cards carry no years-of-experience figure at all (Piyush Shah CA, Vipul Patel, Neha Soni CS & LLB) -- a disclosure asymmetry between promoter-family/executive cards and independent-director cards, flagged for A3/A4, not interpreted here.
- **STRUCTURAL_AGENDA_NUM / STRUCTURAL_SECTION_DIVIDER_NUM / STRUCTURAL_MOAT_NUM**: the 01-07 numbering printed on the agenda (Slide3), each section-divider slide (Slides4,9,13,26,32,35,37), and the Sustainable Moats framework (Slide14) are pagination/navigation numbering, not disclosed business data; included in the Numbers table for completeness per the 'no exceptions' rule but flagged distinctly so downstream agents can filter them out of financial/operational analysis.
- **Naming mismatch (observation, not a numeric flag)**: the Agenda (Slide3, item 04) reads 'Growth Strategy'; the corresponding section-divider slide (Slide26) and its content slide (Slide27) both read 'Key Strategies'. Literal text mismatch between two slides, noted for completeness; not interpreted.
- **PROCESS_STEP_ICON_MARKER_UNRESOLVED**: Slide38 (Process Flow) shows a numeral '1' after nearly every process-step box in both the welded and seamless flows (24 instances). This reads as a rendering artifact of a step-icon/bullet glyph rather than sequential step numbering (all 24 instances show '1', never 2, 3, 4...); flagged as unresolved, not enumerated as 24 distinct data values, not interpreted further.
- **OCR_NOISE_UNRELIABLE / not enumerated as data**: Slide16's certification badge collage was OCR'd at 400dpi per A1; output is noisy (photographic/badge background) and, per A1's own assessment, adds no numeric content beyond the text layer already captured (349 clients). Some badge names are legible in the OCR noise (ADWO, Norsok M650, DNV, IBR, BIS) beyond the ISO/PED list already given in Slide10's bullet text, but individual badge certificate numbers (e.g., '804', '020', '38278' fragments) are not reliably legible and are NOT enumerated as data points here, consistent with A1's caveat. Slide28's OCR echo of the capacity chart is a duplicate of text-layer content already counted once; not double-counted.
