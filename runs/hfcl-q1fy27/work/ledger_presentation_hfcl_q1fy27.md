# Ledger: HFCL Q1FY27 Earnings Presentation (22-page investor deck)
Doctype: presentation | Source: presentation_hfcl_q1fy27.pdf | A1 extract: extract_presentation_hfcl_q1fy27.txt
Prior-quarter ledger: NOT PROVIDED / NOT FOUND in runs/ — DROPPED_SLIDE comparison (rule 3, INVESTOR PRESENTATION section) could not be performed with evidence. This is recorded as a methodology gap, not a finding of "no drops."

=== A2 COUNT TEST ===
category: slides              grep_count: 22   sweep_count: 22   match: yes
category: slide_numbers       grep_count: 313  sweep_count: 313  match: yes
category: line_items          grep_count: 18   sweep_count: 18   match: yes
category: zero_standing       grep_count: 1    sweep_count: 1    match: yes
category: footnotes           grep_count: 15   sweep_count: 15   match: yes
gate_a2: pass
=== END COUNT TEST ===

Methodology note: "grep_count" for slides = page-break markers `^\[page N\]` matched with `grep -n`
against the extract (22, ties to A1 header page_count_pdfinfo:22 and formfeed_count:22).
"grep_count" for slide_numbers = a deterministic awk pass extracting every numeric token
(pattern `[0-9][0-9,]*\.?[0-9]*%?`) from the extracted body text, EXCLUDING the running
header/footer banner line ("HFCL LIMITED | INVESTOR PRESENTATION 2026...APPENDIX..."), the
`[page N]` / `[CHART,...]` / `[OCR page...]` / `[raw pdftotext...]` machine-notes, and the A1
extraction-header metadata block above "=== BEGIN EXTRACTED TEXT ===". This produced 313
tokens at 100 distinct original-file line numbers. The manual sweep (Table 2 below)
independently walked every slide line-by-line and assigned a disclosure context to each of
those same 313 tokens; zero tokens were found with a missing/uncertain context after the
sweep, so grep_count = sweep_count = 313 and GATE A2 passes for this category.
"line_items" = the 18 row labels in the Income Statement table (slide 8, lines 240-261),
counted independently via grep on row-initial alphabetic labels and via manual read of the
table; both = 18. "zero_standing" = 1 (Exceptional Items row, dash in all three periods).
"footnotes" = 15 qualifying disclaimers/unit-labels/hedge-phrases identified via keyword grep
("crore|all numbers|map not to scale|aspiration|estimate|target|proposed|expected") plus
manual read of every slide's fine print; both = 15.

## TABLE 1 — SLIDE ENUMERATION (22 of 22)

| Slide | Title | Content Type | Line (page marker) | Flags |
|---|---|---|---|---|
| 1 | SEBI Reg. 30 covering letter to BSE/NSE re: Earnings' Presentation submission | text (correspondence) | 21 | — |
| 2 | "Earnings Presentation" cover slide (HFCL Limited, //July 2026) | photo/text (background photo-heavy; low native-text yield, OCR'd) | 76 | OCR_UNCERTAIN |
| 3 | "Inside this Presentation" — Table of Contents | text/graphic (5-chapter TOC with page ranges) | 94 | — |
| 4 | "Message From the MD" — chapter divider | text/photo (chapter divider) | 118 | — |
| 5 | "Message from The Managing Director" — MD commentary + Q1FY27 KPI callouts (Revenue/EBITDA & margin/PAT & margin) | text + data callout | 134 | — |
| 6 | "Our Financials" — chapter divider + 3-item sub-TOC (slides 06-08) | text divider | 184 | — |
| 7 | "Q1FY27 Financial Highlights" — bar charts: Revenue, EBITDA & EBITDA Margin, PAT & PAT Margin (Q1FY26/Q4FY26/Q1FY27) | chart | 200 | CHART (native vector text, page 7 confirmed zero embedded raster images per A1 pdfimages check); CHART_LABEL_INFERRED |
| 8 | "Income Statement – Q1FY27" — full P&L table, 18 line items x up to 5 columns | table | 234 | ZERO_STANDING (Exceptional Items row) |
| 9 | "Strong & Diversified Order Book – Q1FY27" — bar charts: Category Wise, Customer Wise, Total Order Book | chart | 265 | CHART (native vector text, page 9 confirmed zero embedded raster images); CHART_LABEL_INFERRED |
| 10 | "HFCL – A Differentiated Technology-Led Play" — chapter divider + 5-item sub-TOC (slides 10-14) | text divider | 301 | — |
| 11 | "A Differentiated, Fully Integrated Platform Serving Telecom and Defence" — stat infographic + product-category grid | text/graphic | 323 | — |
| 12 | "With Presence Across 60+ Countries Supporting 80+ Marquee Customers" — overseas-office map + capability callouts | photo/graphic + text | 375 | — |
| 13 | "Driving Product Innovation Through Deep In-house R&D" — R&D headcount infographic (225 total across 4 teams + 3 centres) | graphic/text | 406 | — |
| 14 | "Complemented By State-of-the-art Manufacturing Infrastructure For Scalable Execution" — capacity/capex infographic | graphic/text | 443 | — |
| 15 | "High-End Customised Product Portfolio" — product grid (OF/OFC/PCS/DCS, Telecom, Defence, New Products) + Defence order-book callout | graphic/text | 462 | — |
| 16 | "HFCL – Strategic Focus" — chapter divider + 2-item sub-TOC (slides 16-17) | text divider | 508 | — |
| 17 | "Well-Defined Growth Levers To Accelerate Revenues And Profitability" — 3 strategic priorities with FY26-FY29 targets | text/graphic | 526 | — |
| 18 | "Making HFCL A Differentiated Play Across OFC, Telecom And Defence Products" — 5-column thematic comparison | table/text | 558 | — |
| 19 | "Appendix" — chapter divider + 2-item sub-TOC | text divider | 589 | — |
| 20 | "Shareholders Information" — shareholding pie/donut chart + share-info table (market cap, ADTV, shares outstanding) | chart + table | 604 | CHART (pie-chart % labels are native vector text; one decorative 1929x166px background-strip image present, no data content, per A1 pdfimages check) |
| 21 | "Abbreviations / Description" — glossary table, 18 abbreviation rows | table | 634 | ZERO_NUMBERS (no numeric tokens on this slide — expected for a text glossary; confirmed by grep, 0 tokens) |
| 22 | "Thank You" — closing/contact slide (Corporate Office address, Amit Agarwal / Head-IR contact) | text/photo | 657 | — |

Notable structural observation (not a DROPPED_SLIDE finding, since no prior deck is available
for comparison): this deck carries no standalone "Forward-Looking Statements / Safe Harbor"
disclaimer slide of the kind common to Indian investor decks. Every forward-looking figure in
this deck (40% FY27 revenue growth aspiration, FY26-FY29 margin targets, FY27 export/product
mix targets, the acquisition-contingent defence order-book figures) is hedged only inline,
within body text on slides 5, 15, 17 and 18 (see Table 3, footnote rows). Flagged for A3/A4
attention as an inline-only observation, not asserted as a drop.

## TABLE 2 — EVERY NUMBER ON EVERY SLIDE (313 of 313)

| Slide | Line | Value | Context |
|---|---|---|---|
| 1 | 22 | 26 | Letter reference/document control number "HFCL/SEC/26-27" |
| 1 | 22 | 27 | Letter reference/document control number "HFCL/SEC/26-27" |
| 1 | 23 | 22, | Letter date: July 22, 2026 |
| 1 | 23 | 2026 | Letter date: July 22, 2026 |
| 1 | 26 | 1 | BSE/NSE address floor refs (1st Floor / 5th Floor / C-1 Block G) - administrative, non-financial |
| 1 | 26 | 5 | BSE/NSE address floor refs (1st Floor / 5th Floor / C-1 Block G) - administrative, non-financial |
| 1 | 26 | 1, | BSE/NSE address floor refs (1st Floor / 5th Floor / C-1 Block G) - administrative, non-financial |
| 1 | 28 | 400001 | Mumbai PIN codes 400001 (BSE) and 400051 (NSE) in addressee block |
| 1 | 28 | 400051 | Mumbai PIN codes 400001 (BSE) and 400051 (NSE) in addressee block |
| 1 | 30 | 500183 | BSE Security Code No. 500183 for HFCL |
| 1 | 32 | 30 | SEBI (LODR) Regulation 30 citation |
| 1 | 33 | 2015. | SEBI Listing Regulations, 2015 (year) citation |
| 1 | 41 | 30 | SEBI (LODR) Regulation 30 citation (repeat, "read with Para A of Part A of Schedule III") |
| 1 | 42 | 2015 | SEBI Listing Regulations, 2015 (year) citation (repeat) |
| 1 | 44 | 1 | "1st Quarter ended June 30, 2026" - quarter reference and quarter-end date |
| 1 | 44 | 30, | "1st Quarter ended June 30, 2026" - quarter reference and quarter-end date |
| 1 | 44 | 2026, | "1st Quarter ended June 30, 2026" - quarter reference and quarter-end date |
| 1 | 45 | 2026 | "Financial Year 2026-27" reference |
| 1 | 45 | 27, | "Financial Year 2026-27" reference |
| 1 | 46 | 22, | "Wednesday, July 22, 2026 at 04:30 p.m." - earnings call date and time |
| 1 | 46 | 2026 | "Wednesday, July 22, 2026 at 04:30 p.m." - earnings call date and time |
| 1 | 46 | 04 | "Wednesday, July 22, 2026 at 04:30 p.m." - earnings call date and time |
| 1 | 46 | 30 | "Wednesday, July 22, 2026 at 04:30 p.m." - earnings call date and time |
| 1 | 49 | 22, | Board meeting date July 22, 2026 - results approval date |
| 1 | 49 | 2026. | Board meeting date July 22, 2026 - results approval date |
| 1 | 61 | 2026.07 | Digital signature date component 2026.07.22 (Manoj Baid, President & Company Secretary) |
| 1 | 61 | 22 | Digital signature date component 2026.07.22 (Manoj Baid, President & Company Secretary) |
| 1 | 62 | 14 | Digital signature time/timezone components 14:34:03 +05'30' |
| 1 | 62 | 34 | Digital signature time/timezone components 14:34:03 +05'30' |
| 1 | 62 | 03 | Digital signature time/timezone components 14:34:03 +05'30' |
| 1 | 62 | 05 | Digital signature time/timezone components 14:34:03 +05'30' |
| 1 | 62 | 30 | Digital signature time/timezone components 14:34:03 +05'30' |
| 1 | 69 | 8, | Regd Office address PIN 173213; Tel (01792) 230644/230645/230647; Fax (01792) 231902 |
| 1 | 69 | 173213 | Regd Office address PIN 173213; Tel (01792) 230644/230645/230647; Fax (01792) 231902 |
| 1 | 69 | 01792 | Regd Office address PIN 173213; Tel (01792) 230644/230645/230647; Fax (01792) 231902 |
| 1 | 69 | 230644, | Regd Office address PIN 173213; Tel (01792) 230644/230645/230647; Fax (01792) 231902 |
| 1 | 69 | 230645, | Regd Office address PIN 173213; Tel (01792) 230644/230645/230647; Fax (01792) 231902 |
| 1 | 69 | 230647 | Regd Office address PIN 173213; Tel (01792) 230644/230645/230647; Fax (01792) 231902 |
| 1 | 69 | 01792 | Regd Office address PIN 173213; Tel (01792) 230644/230645/230647; Fax (01792) 231902 |
| 1 | 69 | 231902 | Regd Office address PIN 173213; Tel (01792) 230644/230645/230647; Fax (01792) 231902 |
| 1 | 70 | 64200 | Corporate Identity Number L64200HP1987PLC007466 |
| 1 | 70 | 1987 | Corporate Identity Number L64200HP1987PLC007466 |
| 1 | 70 | 007466 | Corporate Identity Number L64200HP1987PLC007466 |
| 1 | 71 | 2026 | Footer date "//July 2026" on letter page |
| 2 | 79 | 202603 | OCR-garbled token from [OCR page 2] raw output "pryuly 202603" - unreliable, cross-check below |
| 2 | 85 | 2026 | Cover slide footer date "//July 2026" (raw pdftotext cross-check for OCR page 2) |
| 3 | 100 | 03 | TOC page-range labels: 03-04 (Message from MD), 05-08 (Financials), 09-14 (HFCL - A Differentiated Play) |
| 3 | 100 | 04 | TOC page-range labels: 03-04 (Message from MD), 05-08 (Financials), 09-14 (HFCL - A Differentiated Play) |
| 3 | 100 | 05 | TOC page-range labels: 03-04 (Message from MD), 05-08 (Financials), 09-14 (HFCL - A Differentiated Play) |
| 3 | 100 | 08 | TOC page-range labels: 03-04 (Message from MD), 05-08 (Financials), 09-14 (HFCL - A Differentiated Play) |
| 3 | 100 | 09 | TOC page-range labels: 03-04 (Message from MD), 05-08 (Financials), 09-14 (HFCL - A Differentiated Play) |
| 3 | 100 | 14 | TOC page-range labels: 03-04 (Message from MD), 05-08 (Financials), 09-14 (HFCL - A Differentiated Play) |
| 3 | 105 | 01 | TOC chapter numbers: 01/ Message From MD, 02/ Financials, 03/ HFCL - A Differentiated Play |
| 3 | 105 | 02 | TOC chapter numbers: 01/ Message From MD, 02/ Financials, 03/ HFCL - A Differentiated Play |
| 3 | 105 | 03 | TOC chapter numbers: 01/ Message From MD, 02/ Financials, 03/ HFCL - A Differentiated Play |
| 3 | 109 | 15 | TOC page-range labels: 15-17 (Strategic Focus), 18-20 (Appendix) |
| 3 | 109 | 17 | TOC page-range labels: 15-17 (Strategic Focus), 18-20 (Appendix) |
| 3 | 109 | 18 | TOC page-range labels: 15-17 (Strategic Focus), 18-20 (Appendix) |
| 3 | 109 | 20 | TOC page-range labels: 15-17 (Strategic Focus), 18-20 (Appendix) |
| 3 | 114 | 04 | TOC chapter numbers: 04/ Strategic Focus, 05/ Appendix |
| 3 | 114 | 05 | TOC chapter numbers: 04/ Strategic Focus, 05/ Appendix |
| 4 | 122 | 04 | "//CHAPTER 04" chapter marker on MD-message divider slide |
| 4 | 132 | 04 | Sub-TOC entry "04 Message from The Managing Director" |
| 5 | 142 | 27 | Body text reference "the first quarter of FY27" |
| 5 | 153 | 1 | Callout heading "KEY PERFORMANCE METRICS FOR Q1FY27" |
| 5 | 153 | 27 | Callout heading "KEY PERFORMANCE METRICS FOR Q1FY27" |
| 5 | 156 | 1914.98 | KPI callout: Revenue (Rs in Crore) = 1,914.98, Q1FY27 |
| 5 | 161 | 27 | Body text "...increased our FY27 revenue growth aspiration..." |
| 5 | 162 | 40% | FY27 revenue growth aspiration guidance = 40% ("best of our estimates", hedged forward guidance) |
| 5 | 164 | 445.27 | KPI callout: EBITDA (Rs Cr) = 445.27 & EBITDA Margin = 23.25%, Q1FY27 |
| 5 | 164 | 23.25% | KPI callout: EBITDA (Rs Cr) = 445.27 & EBITDA Margin = 23.25%, Q1FY27 |
| 5 | 165 | 23% | Body text restating "EBITDA margin of over 23% in the very first quarter" |
| 5 | 171 | 245.64 | KPI callout: PAT (Rs Cr) = 245.64 & PAT Margin = 12.83%, Q1FY27 |
| 5 | 171 | 12.83% | KPI callout: PAT (Rs Cr) = 245.64 & PAT Margin = 12.83%, Q1FY27 |
| 6 | 185 | 05 | "//CHAPTER 05" chapter marker on Financials divider slide |
| 6 | 194 | 06 | Sub-TOC entry "06 Q1FY27 Financial Highlights" |
| 6 | 194 | 1 | Sub-TOC entry "06 Q1FY27 Financial Highlights" |
| 6 | 194 | 27 | Sub-TOC entry "06 Q1FY27 Financial Highlights" |
| 6 | 195 | 07 | Sub-TOC entry "07 Income Statement - Q1FY27" |
| 6 | 195 | 1 | Sub-TOC entry "07 Income Statement - Q1FY27" |
| 6 | 195 | 27 | Sub-TOC entry "07 Income Statement - Q1FY27" |
| 6 | 196 | 08 | Sub-TOC entry "08 Strong & Diversified Order Book" |
| 7 | 202 | 1 | Slide title "Q1FY27 Financial Highlights" |
| 7 | 202 | 27 | Slide title "Q1FY27 Financial Highlights" |
| 7 | 210 | 445 | [CHART p7, CHART_LABEL_INFERRED] Bar value 445 - EBITDA Q1FY27 (Rs Cr), cross-validated vs slide 8 table 445.27 |
| 7 | 211 | 246 | [CHART p7, CHART_LABEL_INFERRED] Bar value 246 - PAT Q1FY27 (Rs Cr), cross-validated vs slide 8 table 245.64 (rounded) |
| 7 | 212 | 184 | [CHART p7, CHART_LABEL_INFERRED] Bar value 184 - PAT Q4FY26 (Rs Cr), cross-validated vs slide 8 table 184.45 (rounded) |
| 7 | 213 | 1,915 | [CHART p7, CHART_LABEL_INFERRED] Bar value 1,915 (Revenue Q1FY27, Rs Cr) and 18.5% (EBITDA Margin Q4FY26) co-located in raw layout |
| 7 | 213 | 18.5% | [CHART p7, CHART_LABEL_INFERRED] Bar value 1,915 (Revenue Q1FY27, Rs Cr) and 18.5% (EBITDA Margin Q4FY26) co-located in raw layout |
| 7 | 214 | 1,824 | [CHART p7, CHART_LABEL_INFERRED] Bar value 1,824 - Revenue Q4FY26 (Rs Cr) |
| 7 | 215 | 23.3% | [CHART p7, CHART_LABEL_INFERRED] 23.3% - EBITDA Margin Q1FY27 (headline MD-message rounds to 23.25%) |
| 7 | 216 | 12.8% | [CHART p7, CHART_LABEL_INFERRED] 12.8% - PAT Margin Q1FY27 (headline table shows 12.83%) |
| 7 | 217 | 10.1% | [CHART p7, CHART_LABEL_INFERRED] 10.1% - PAT Margin Q4FY26 (table shows 10.11%) |
| 7 | 218 | 337 | [CHART p7, CHART_LABEL_INFERRED] Bar value 337 - EBITDA Q4FY26 (Rs Cr), table shows 336.93 |
| 7 | 221 | 3.4% | [CHART p7, CHART_LABEL_INFERRED] -3.4% - PAT Margin Q1FY26 (table shows -3.36%) |
| 7 | 222 | 4.9% | [CHART p7, CHART_LABEL_INFERRED] 4.9% - EBITDA Margin Q1FY26 (table shows 4.93%) |
| 7 | 223 | 871 | [CHART p7, CHART_LABEL_INFERRED] Bar value 871 - Revenue Q1FY26 (Rs Cr), table shows 871.02 |
| 7 | 227 | 29 | [CHART p7, CHART_LABEL_INFERRED] Bar value -29 - PAT Q1FY26 (Rs Cr), sign lost in token extraction, table shows -29.30 |
| 7 | 228 | 43 | [CHART p7, CHART_LABEL_INFERRED] Bar value 43 - EBITDA Q1FY26 (Rs Cr), table shows 42.93 |
| 7 | 230 | 1 | Chart x-axis period labels repeated under each of the 3 sub-charts: Q1FY26 / Q4FY26 / Q1FY27 (appears 3x, 6 tokens each = 18 tokens) |
| 7 | 230 | 26 | Chart x-axis period labels repeated under each of the 3 sub-charts: Q1FY26 / Q4FY26 / Q1FY27 (appears 3x, 6 tokens each = 18 tokens) |
| 7 | 230 | 4 | Chart x-axis period labels repeated under each of the 3 sub-charts: Q1FY26 / Q4FY26 / Q1FY27 (appears 3x, 6 tokens each = 18 tokens) |
| 7 | 230 | 26 | Chart x-axis period labels repeated under each of the 3 sub-charts: Q1FY26 / Q4FY26 / Q1FY27 (appears 3x, 6 tokens each = 18 tokens) |
| 7 | 230 | 1 | Chart x-axis period labels repeated under each of the 3 sub-charts: Q1FY26 / Q4FY26 / Q1FY27 (appears 3x, 6 tokens each = 18 tokens) |
| 7 | 230 | 27 | Chart x-axis period labels repeated under each of the 3 sub-charts: Q1FY26 / Q4FY26 / Q1FY27 (appears 3x, 6 tokens each = 18 tokens) |
| 7 | 230 | 1 | Chart x-axis period labels repeated under each of the 3 sub-charts: Q1FY26 / Q4FY26 / Q1FY27 (appears 3x, 6 tokens each = 18 tokens) |
| 7 | 230 | 26 | Chart x-axis period labels repeated under each of the 3 sub-charts: Q1FY26 / Q4FY26 / Q1FY27 (appears 3x, 6 tokens each = 18 tokens) |
| 7 | 230 | 4 | Chart x-axis period labels repeated under each of the 3 sub-charts: Q1FY26 / Q4FY26 / Q1FY27 (appears 3x, 6 tokens each = 18 tokens) |
| 7 | 230 | 26 | Chart x-axis period labels repeated under each of the 3 sub-charts: Q1FY26 / Q4FY26 / Q1FY27 (appears 3x, 6 tokens each = 18 tokens) |
| 7 | 230 | 1 | Chart x-axis period labels repeated under each of the 3 sub-charts: Q1FY26 / Q4FY26 / Q1FY27 (appears 3x, 6 tokens each = 18 tokens) |
| 7 | 230 | 27 | Chart x-axis period labels repeated under each of the 3 sub-charts: Q1FY26 / Q4FY26 / Q1FY27 (appears 3x, 6 tokens each = 18 tokens) |
| 7 | 230 | 1 | Chart x-axis period labels repeated under each of the 3 sub-charts: Q1FY26 / Q4FY26 / Q1FY27 (appears 3x, 6 tokens each = 18 tokens) |
| 7 | 230 | 26 | Chart x-axis period labels repeated under each of the 3 sub-charts: Q1FY26 / Q4FY26 / Q1FY27 (appears 3x, 6 tokens each = 18 tokens) |
| 7 | 230 | 4 | Chart x-axis period labels repeated under each of the 3 sub-charts: Q1FY26 / Q4FY26 / Q1FY27 (appears 3x, 6 tokens each = 18 tokens) |
| 7 | 230 | 26 | Chart x-axis period labels repeated under each of the 3 sub-charts: Q1FY26 / Q4FY26 / Q1FY27 (appears 3x, 6 tokens each = 18 tokens) |
| 7 | 230 | 1 | Chart x-axis period labels repeated under each of the 3 sub-charts: Q1FY26 / Q4FY26 / Q1FY27 (appears 3x, 6 tokens each = 18 tokens) |
| 7 | 230 | 27 | Chart x-axis period labels repeated under each of the 3 sub-charts: Q1FY26 / Q4FY26 / Q1FY27 (appears 3x, 6 tokens each = 18 tokens) |
| 8 | 235 | 1 | Slide title "Income Statement - Q1FY27" |
| 8 | 235 | 27 | Slide title "Income Statement - Q1FY27" |
| 8 | 240 | 1 | Table column headers: Q1FY27, Q4FY26, Q1FY26 (period columns; Q-o-Q and Y-o-Y are text labels, non-numeric) |
| 8 | 240 | 27 | Table column headers: Q1FY27, Q4FY26, Q1FY26 (period columns; Q-o-Q and Y-o-Y are text labels, non-numeric) |
| 8 | 240 | 4 | Table column headers: Q1FY27, Q4FY26, Q1FY26 (period columns; Q-o-Q and Y-o-Y are text labels, non-numeric) |
| 8 | 240 | 26 | Table column headers: Q1FY27, Q4FY26, Q1FY26 (period columns; Q-o-Q and Y-o-Y are text labels, non-numeric) |
| 8 | 240 | 1 | Table column headers: Q1FY27, Q4FY26, Q1FY26 (period columns; Q-o-Q and Y-o-Y are text labels, non-numeric) |
| 8 | 240 | 26 | Table column headers: Q1FY27, Q4FY26, Q1FY26 (period columns; Q-o-Q and Y-o-Y are text labels, non-numeric) |
| 8 | 242 | 1,914.98 | Income Statement row "Revenue from Operations": 1,914.98 (Q1FY27) / 1824.12 (Q4FY26) / 4.98% (QoQ) / 871.02 (Q1FY26) / 119.85% (YoY) |
| 8 | 242 | 1824.12 | Income Statement row "Revenue from Operations": 1,914.98 (Q1FY27) / 1824.12 (Q4FY26) / 4.98% (QoQ) / 871.02 (Q1FY26) / 119.85% (YoY) |
| 8 | 242 | 4.98% | Income Statement row "Revenue from Operations": 1,914.98 (Q1FY27) / 1824.12 (Q4FY26) / 4.98% (QoQ) / 871.02 (Q1FY26) / 119.85% (YoY) |
| 8 | 242 | 871.02 | Income Statement row "Revenue from Operations": 1,914.98 (Q1FY27) / 1824.12 (Q4FY26) / 4.98% (QoQ) / 871.02 (Q1FY26) / 119.85% (YoY) |
| 8 | 242 | 119.85% | Income Statement row "Revenue from Operations": 1,914.98 (Q1FY27) / 1824.12 (Q4FY26) / 4.98% (QoQ) / 871.02 (Q1FY26) / 119.85% (YoY) |
| 8 | 243 | 31.15 | Income Statement row "Other Income": 31.15 (Q1FY27) / 22.26 (Q4FY26) / 14.53 (Q1FY26) - no QoQ%/YoY% shown |
| 8 | 243 | 22.26 | Income Statement row "Other Income": 31.15 (Q1FY27) / 22.26 (Q4FY26) / 14.53 (Q1FY26) - no QoQ%/YoY% shown |
| 8 | 243 | 14.53 | Income Statement row "Other Income": 31.15 (Q1FY27) / 22.26 (Q4FY26) / 14.53 (Q1FY26) - no QoQ%/YoY% shown |
| 8 | 244 | 1,946.13 | Income Statement row "TOTAL INCOME": 1,946.13 / 1,846.38 / 5.40% / 885.55 / 119.77% |
| 8 | 244 | 1,846.38 | Income Statement row "TOTAL INCOME": 1,946.13 / 1,846.38 / 5.40% / 885.55 / 119.77% |
| 8 | 244 | 5.40% | Income Statement row "TOTAL INCOME": 1,946.13 / 1,846.38 / 5.40% / 885.55 / 119.77% |
| 8 | 244 | 885.55 | Income Statement row "TOTAL INCOME": 1,946.13 / 1,846.38 / 5.40% / 885.55 / 119.77% |
| 8 | 244 | 119.77% | Income Statement row "TOTAL INCOME": 1,946.13 / 1,846.38 / 5.40% / 885.55 / 119.77% |
| 8 | 245 | 1,500.86 | Income Statement row "Total Expenses": 1,500.86 / 1509.45 / 842.62 - no QoQ%/YoY% shown |
| 8 | 245 | 1509.45 | Income Statement row "Total Expenses": 1,500.86 / 1509.45 / 842.62 - no QoQ%/YoY% shown |
| 8 | 245 | 842.62 | Income Statement row "Total Expenses": 1,500.86 / 1509.45 / 842.62 - no QoQ%/YoY% shown |
| 8 | 246 | 445.27 | Income Statement row "EBITDA": 445.27 / 336.93 / 32.16% / 42.93 / 937.20% |
| 8 | 246 | 336.93 | Income Statement row "EBITDA": 445.27 / 336.93 / 32.16% / 42.93 / 937.20% |
| 8 | 246 | 32.16% | Income Statement row "EBITDA": 445.27 / 336.93 / 32.16% / 42.93 / 937.20% |
| 8 | 246 | 42.93 | Income Statement row "EBITDA": 445.27 / 336.93 / 32.16% / 42.93 / 937.20% |
| 8 | 246 | 937.20% | Income Statement row "EBITDA": 445.27 / 336.93 / 32.16% / 42.93 / 937.20% |
| 8 | 247 | 23.25% | Income Statement row "EBITDA MARGIN (%)": 23.25% / 18.47% / 478 (Bps QoQ) / 4.93% / 1832 (Bps YoY) |
| 8 | 247 | 18.47% | Income Statement row "EBITDA MARGIN (%)": 23.25% / 18.47% / 478 (Bps QoQ) / 4.93% / 1832 (Bps YoY) |
| 8 | 247 | 478 | Income Statement row "EBITDA MARGIN (%)": 23.25% / 18.47% / 478 (Bps QoQ) / 4.93% / 1832 (Bps YoY) |
| 8 | 247 | 4.93% | Income Statement row "EBITDA MARGIN (%)": 23.25% / 18.47% / 478 (Bps QoQ) / 4.93% / 1832 (Bps YoY) |
| 8 | 247 | 1832 | Income Statement row "EBITDA MARGIN (%)": 23.25% / 18.47% / 478 (Bps QoQ) / 4.93% / 1832 (Bps YoY) |
| 8 | 248 | 51.25 | Income Statement row "Depreciation": 51.25 / 45.48 / 32.20 - no QoQ%/YoY% shown |
| 8 | 248 | 45.48 | Income Statement row "Depreciation": 51.25 / 45.48 / 32.20 - no QoQ%/YoY% shown |
| 8 | 248 | 32.20 | Income Statement row "Depreciation": 51.25 / 45.48 / 32.20 - no QoQ%/YoY% shown |
| 8 | 249 | 62.48 | Income Statement row "Finance Cost": 62.48 / 62.78 / 55.62 - no QoQ%/YoY% shown |
| 8 | 249 | 62.78 | Income Statement row "Finance Cost": 62.48 / 62.78 / 55.62 - no QoQ%/YoY% shown |
| 8 | 249 | 55.62 | Income Statement row "Finance Cost": 62.48 / 62.78 / 55.62 - no QoQ%/YoY% shown |
| 8 | 251 | 0.02 | Income Statement row "Share of net profits/(loss) of JV's accounted using equity method": -0.02 / -0.74 / 0.19 (signs lost in token extraction) - no QoQ%/YoY% shown |
| 8 | 251 | 0.74 | Income Statement row "Share of net profits/(loss) of JV's accounted using equity method": -0.02 / -0.74 / 0.19 (signs lost in token extraction) - no QoQ%/YoY% shown |
| 8 | 251 | 0.19 | Income Statement row "Share of net profits/(loss) of JV's accounted using equity method": -0.02 / -0.74 / 0.19 (signs lost in token extraction) - no QoQ%/YoY% shown |
| 8 | 254 | 331.52 | Income Statement row "PBT": 331.52 / 227.93 / 45.45% / -44.70 (sign lost, Q1FY26 was a loss) |
| 8 | 254 | 227.93 | Income Statement row "PBT": 331.52 / 227.93 / 45.45% / -44.70 (sign lost, Q1FY26 was a loss) |
| 8 | 254 | 45.45% | Income Statement row "PBT": 331.52 / 227.93 / 45.45% / -44.70 (sign lost, Q1FY26 was a loss) |
| 8 | 254 | 44.70 | Income Statement row "PBT": 331.52 / 227.93 / 45.45% / -44.70 (sign lost, Q1FY26 was a loss) |
| 8 | 255 | 17.31% | Income Statement row "PBT MARGIN (%)": 17.31% / 12.50% / 481 (Bps QoQ) / -5.13% (sign lost) |
| 8 | 255 | 12.50% | Income Statement row "PBT MARGIN (%)": 17.31% / 12.50% / 481 (Bps QoQ) / -5.13% (sign lost) |
| 8 | 255 | 481 | Income Statement row "PBT MARGIN (%)": 17.31% / 12.50% / 481 (Bps QoQ) / -5.13% (sign lost) |
| 8 | 255 | 5.13% | Income Statement row "PBT MARGIN (%)": 17.31% / 12.50% / 481 (Bps QoQ) / -5.13% (sign lost) |
| 8 | 256 | 85.88 | Income Statement row "Tax": 85.88 / 43.48 / -15.40 (sign lost) - no QoQ%/YoY% shown |
| 8 | 256 | 43.48 | Income Statement row "Tax": 85.88 / 43.48 / -15.40 (sign lost) - no QoQ%/YoY% shown |
| 8 | 256 | 15.40 | Income Statement row "Tax": 85.88 / 43.48 / -15.40 (sign lost) - no QoQ%/YoY% shown |
| 8 | 257 | 245.64 | Income Statement row "PROFIT AFTER TAX": 245.64 / 184.45 / 33.17% / -29.30 (sign lost, Q1FY26 loss) |
| 8 | 257 | 184.45 | Income Statement row "PROFIT AFTER TAX": 245.64 / 184.45 / 33.17% / -29.30 (sign lost, Q1FY26 loss) |
| 8 | 257 | 33.17% | Income Statement row "PROFIT AFTER TAX": 245.64 / 184.45 / 33.17% / -29.30 (sign lost, Q1FY26 loss) |
| 8 | 257 | 29.30 | Income Statement row "PROFIT AFTER TAX": 245.64 / 184.45 / 33.17% / -29.30 (sign lost, Q1FY26 loss) |
| 8 | 258 | 12.83% | Income Statement row "PAT MARGIN (%)": 12.83% / 10.11% / 272 (Bps QoQ) / -3.36% (sign lost) |
| 8 | 258 | 10.11% | Income Statement row "PAT MARGIN (%)": 12.83% / 10.11% / 272 (Bps QoQ) / -3.36% (sign lost) |
| 8 | 258 | 272 | Income Statement row "PAT MARGIN (%)": 12.83% / 10.11% / 272 (Bps QoQ) / -3.36% (sign lost) |
| 8 | 258 | 3.36% | Income Statement row "PAT MARGIN (%)": 12.83% / 10.11% / 272 (Bps QoQ) / -3.36% (sign lost) |
| 8 | 259 | 72.16 | Income Statement row "Other Comprehensive Income": 72.16 / -39.23 (sign lost) / 38.92 - no QoQ%/YoY% shown |
| 8 | 259 | 39.23 | Income Statement row "Other Comprehensive Income": 72.16 / -39.23 (sign lost) / 38.92 - no QoQ%/YoY% shown |
| 8 | 259 | 38.92 | Income Statement row "Other Comprehensive Income": 72.16 / -39.23 (sign lost) / 38.92 - no QoQ%/YoY% shown |
| 8 | 260 | 317.80 | Income Statement row "TOTAL COMPREHENSIVE INCOME": 317.80 / 145.22 / 9.62 - no QoQ%/YoY% shown |
| 8 | 260 | 145.22 | Income Statement row "TOTAL COMPREHENSIVE INCOME": 317.80 / 145.22 / 9.62 - no QoQ%/YoY% shown |
| 8 | 260 | 9.62 | Income Statement row "TOTAL COMPREHENSIVE INCOME": 317.80 / 145.22 / 9.62 - no QoQ%/YoY% shown |
| 8 | 261 | 1.49 | Income Statement row "EPS (Diluted Rs)": 1.49 / 1.21 / -0.22 (sign lost, Q1FY26 loss) |
| 8 | 261 | 1.21 | Income Statement row "EPS (Diluted Rs)": 1.49 / 1.21 / -0.22 (sign lost, Q1FY26 loss) |
| 8 | 261 | 0.22 | Income Statement row "EPS (Diluted Rs)": 1.49 / 1.21 / -0.22 (sign lost, Q1FY26 loss) |
| 9 | 267 | 1 | Slide title "Strong & Diversified Order Book - Q1FY27" |
| 9 | 267 | 27 | Slide title "Strong & Diversified Order Book - Q1FY27" |
| 9 | 279 | 26,665 | [CHART p9, CHART_LABEL_INFERRED] Total Order Book bar value 26,665 (Rs Cr), Q1FY27 |
| 9 | 280 | 4,227 | [CHART p9, CHART_LABEL_INFERRED] Category-wise bar value 4,227 (Rs Cr) - likely "Products" category per slide 11 cross-ref |
| 9 | 283 | 10,502 | [CHART p9, CHART_LABEL_INFERRED] Customer-wise bar value 10,502 (Rs Cr) and Total Order Book bar 21,206 (Rs Cr, Q4FY26) co-located |
| 9 | 283 | 21,206 | [CHART p9, CHART_LABEL_INFERRED] Customer-wise bar value 10,502 (Rs Cr) and Total Order Book bar 21,206 (Rs Cr, Q4FY26) co-located |
| 9 | 285 | 5,099 | [CHART p9, CHART_LABEL_INFERRED] Category-wise bar value 5,099 (Rs Cr) - likely "O&M" category |
| 9 | 286 | 16,164 | [CHART p9, CHART_LABEL_INFERRED] Customer-wise bar value 16,164 (Rs Cr) - likely "Private" customer segment |
| 9 | 287 | 17,339 | [CHART p9, CHART_LABEL_INFERRED] Category-wise bar value 17,339 (Rs Cr) - likely "Networks" category |
| 9 | 288 | 11,125 | [CHART p9, CHART_LABEL_INFERRED] Customer-wise bar value 11,125 (Rs Cr, likely Total Order Book Q3FY26) or Governments segment |
| 9 | 293 | 3 | Chart labels/axis text: category legend (Networks/O&M/Products), customer legend (Governments/Private), period legend Q3FY26/Q4FY26/Q1FY27 |
| 9 | 293 | 26 | Chart labels/axis text: category legend (Networks/O&M/Products), customer legend (Governments/Private), period legend Q3FY26/Q4FY26/Q1FY27 |
| 9 | 293 | 4 | Chart labels/axis text: category legend (Networks/O&M/Products), customer legend (Governments/Private), period legend Q3FY26/Q4FY26/Q1FY27 |
| 9 | 293 | 26 | Chart labels/axis text: category legend (Networks/O&M/Products), customer legend (Governments/Private), period legend Q3FY26/Q4FY26/Q1FY27 |
| 9 | 293 | 1 | Chart labels/axis text: category legend (Networks/O&M/Products), customer legend (Governments/Private), period legend Q3FY26/Q4FY26/Q1FY27 |
| 9 | 293 | 27 | Chart labels/axis text: category legend (Networks/O&M/Products), customer legend (Governments/Private), period legend Q3FY26/Q4FY26/Q1FY27 |
| 10 | 302 | 01 | Sub-TOC entry "10 A Differentiated, Fully Integrated Platform Serving Telecom And Defence" |
| 10 | 312 | 10 | Sub-TOC entry "11 With Presence Across 60+ Countries Supporting 80+ Marquee Customers" |
| 10 | 314 | 11 | Sub-TOC entry "11..." continuation: 60+ Countries, 80+ Marquee Customers (repeat of TOC line figures) |
| 10 | 314 | 60 | Sub-TOC entry "11..." continuation: 60+ Countries, 80+ Marquee Customers (repeat of TOC line figures) |
| 10 | 314 | 80 | Sub-TOC entry "11..." continuation: 60+ Countries, 80+ Marquee Customers (repeat of TOC line figures) |
| 10 | 316 | 12 | Sub-TOC entry "12 Driving Product Innovation Through Deep In-house R&D" |
| 10 | 317 | 13 | Sub-TOC entry "13 Complemented By State-of-the-art Manufacturing Infrastructure..." |
| 10 | 319 | 14 | Sub-TOC entry "14 High-End Customised Product Portfolio" |
| 11 | 326 | 1 | Infographic stat callout "#1 OPTICAL FIBRE CABLE SUPPLIER IN INDIA" (rank, not a count) |
| 11 | 328 | 6 | Infographic stat callout "6 MANUFACTURING FACILITIES" |
| 11 | 330 | 3 | Infographic stat callout "3 R&D CENTRES" |
| 11 | 332 | 60 | Infographic stat callout "60+ COUNTRIES PRESENCE" |
| 11 | 334 | 80 | Infographic stat callout "80+ MARQUEE CUSTOMERS" |
| 11 | 336 | 26,665 | Infographic stat callout "~26,665 Cr ROBUST ORDER BOOK" |
| 11 | 350 | 5, | Product category numbering artifacts within "OF/OFC" bullet list column (list markers, not disclosed metrics) |
| 11 | 350 | 6 | Product category numbering artifacts within "OF/OFC" bullet list column (list markers, not disclosed metrics) |
| 11 | 350 | 7 | Product category numbering artifacts within "OF/OFC" bullet list column (list markers, not disclosed metrics) |
| 11 | 357 | 2 | Product category numbering artifacts within "PCS" bullet list column (list markers, not disclosed metrics) |
| 11 | 357 | 3 | Product category numbering artifacts within "PCS" bullet list column (list markers, not disclosed metrics) |
| 11 | 359 | 5 | Product category numbering artifact "5" within OF/OFC bullet list column |
| 11 | 369 | 4 | Product category numbering artifact within "Telecom & Networking" bullet list column |
| 11 | 369 | 5 | Product category numbering artifact within "Telecom & Networking" bullet list column |
| 12 | 376 | 60 | Infographic stat callout "60+ COUNTRIES" (map slide header repeat) |
| 12 | 377 | 80 | Infographic stat callout "80+ MARQUEE CUSTOMERS" (map slide header repeat) |
| 12 | 389 | 1 | Body text reference "1" embedded in list marker, non-metric |
| 12 | 404 | 012 | Deck footer pagination number "012" (internal page numbering, page 12 of PDF) |
| 13 | 421 | 3 | R&D headcount infographic total dedicated centres "3" |
| 13 | 423 | 55 | R&D headcount by team: "55 5G PRODUCTS" |
| 13 | 424 | 5 | R&D infographic marker "5" (bullet/callout formatting artifact) |
| 13 | 425 | 69 | R&D headcount by team: "69 WIRELESS AND SWITCHING" |
| 13 | 428 | 52 | R&D headcount by team: "52 TECHNOLOGY & DEFENCE" |
| 13 | 431 | 49 | R&D headcount by team: "49 OPTIC FIBER & OPTICAL FIBER CABLE" |
| 13 | 434 | 225 | R&D headcount total: "225 TOTAL" (sum check: 55+69+52+49=225, reconciles) |
| 14 | 447 | 6 | Manufacturing infographic: "6 MANUFACTURING FACILITIES IN INDIA"; "28 MN FKM/ANNUM" optical fiber capacity; "34 MN FKM/ANNUM" optical fiber cable capacity |
| 14 | 447 | 28 | Manufacturing infographic: "6 MANUFACTURING FACILITIES IN INDIA"; "28 MN FKM/ANNUM" optical fiber capacity; "34 MN FKM/ANNUM" optical fiber cable capacity |
| 14 | 447 | 34 | Manufacturing infographic: "6 MANUFACTURING FACILITIES IN INDIA"; "28 MN FKM/ANNUM" optical fiber capacity; "34 MN FKM/ANNUM" optical fiber cable capacity |
| 14 | 449 | 33.9 | Optical fiber capacity expansion target "33.9 MN FKM/ANNUM" |
| 14 | 450 | 42.3 | Optical fiber cable capacity expansion target "42.3 MN FKM/ANNUM" |
| 14 | 455 | 580 | Capex callouts: "Rs580 Cr" preform project capex; "Rs275 Cr" Phase 1 MMHG facility capex |
| 14 | 455 | 275 | Capex callouts: "Rs580 Cr" preform project capex; "Rs275 Cr" Phase 1 MMHG facility capex |
| 14 | 456 | 1 | Qualifier: "Phase1 for creating facility for MMHG in upcoming 1000 Acre Andhra Ammunition Complex" (Rs275 Cr capex context) |
| 14 | 457 | 300 | Capex targets: "300 MT/ANNUM BY JULY 2029" preform capacity target; "1000 Acre" Andhra Ammunition Complex land parcel |
| 14 | 457 | 2029 | Capex targets: "300 MT/ANNUM BY JULY 2029" preform capacity target; "1000 Acre" Andhra Ammunition Complex land parcel |
| 14 | 457 | 1000 | Capex targets: "300 MT/ANNUM BY JULY 2029" preform capacity target; "1000 Acre" Andhra Ammunition Complex land parcel |
| 15 | 472 | 5 | Product portfolio grid label "5G Indoor & Outdoor FWA CPE" (model/spec numbers "5" and "2" from "5G"/product grid formatting, non-metric) |
| 15 | 472 | 2 | Product portfolio grid label "5G Indoor & Outdoor FWA CPE" (model/spec numbers "5" and "2" from "5G"/product grid formatting, non-metric) |
| 15 | 480 | 2 | Product model name "HFCL A2-180 Fiber" - model number, not a metric |
| 15 | 480 | 180 | Product model name "HFCL A2-180 Fiber" - model number, not a metric |
| 15 | 490 | 5, | Product grid formatting artifacts (list markers within product portfolio grid, non-metric) |
| 15 | 490 | 6 | Product grid formatting artifacts (list markers within product portfolio grid, non-metric) |
| 15 | 490 | 7 | Product grid formatting artifacts (list markers within product portfolio grid, non-metric) |
| 15 | 498 | 2,300 | Defence order book callout: "~Rs2,300 Cr total Defence order book" |
| 15 | 498 | 2000 | Defence order book callout: "~Rs2,300 Cr total Defence order book" |
| 15 | 504 | 1 | Bullet list marker within defence order-book callout column, non-metric |
| 16 | 509 | 02 | Deck footer pagination number "02" (internal numbering, chapter divider "Strategic Focus") |
| 16 | 519 | 16 | Sub-TOC entry "16 Well-Defined Growth Levers To Accelerate Revenues And Profitability" |
| 16 | 521 | 17 | Sub-TOC entry "17 Making HFCL A Differentiated Play Across Telecom And Defence Products" |
| 17 | 531 | 01 | Strategic priority numbering "01" (Increased Focus on Higher Margin Product Revenue) and "02" (Expanding Manufacturing Capacities / Optimising Revenue Mix, listed twice) |
| 17 | 531 | 02 | Strategic priority numbering "01" (Increased Focus on Higher Margin Product Revenue) and "02" (Expanding Manufacturing Capacities / Optimising Revenue Mix, listed twice) |
| 17 | 531 | 02 | Strategic priority numbering "01" (Increased Focus on Higher Margin Product Revenue) and "02" (Expanding Manufacturing Capacities / Optimising Revenue Mix, listed twice) |
| 17 | 536 | 16.7% | Strategic target: EBITDA margin "~16.7% in FY26" baseline expanding "to 22-25% by FY29" (target range) |
| 17 | 536 | 80 | Strategic target: EBITDA margin "~16.7% in FY26" baseline expanding "to 22-25% by FY29" (target range) |
| 17 | 536 | 85% | Strategic target: EBITDA margin "~16.7% in FY26" baseline expanding "to 22-25% by FY29" (target range) |
| 17 | 537 | 26 | Strategic target: Revenue mix targeting "80-85% Revenue from Product" and "more than 60% Revenue from Export by FY27" |
| 17 | 537 | 22 | Strategic target: Revenue mix targeting "80-85% Revenue from Product" and "more than 60% Revenue from Export by FY27" |
| 17 | 537 | 25% | Strategic target: Revenue mix targeting "80-85% Revenue from Product" and "more than 60% Revenue from Export by FY27" |
| 17 | 537 | 29 | Strategic target: Revenue mix targeting "80-85% Revenue from Product" and "more than 60% Revenue from Export by FY27" |
| 17 | 537 | 60% | Strategic target: Revenue mix targeting "80-85% Revenue from Product" and "more than 60% Revenue from Export by FY27" |
| 17 | 538 | 27 | Strategic target continuation "...by FY27" (27 token, FY27 reference) |
| 17 | 543 | 43 | Capacity expansion target: OFC/OF capacity "~43 mn fkm p.a." and "~34 mn fkm p.a." respectively |
| 17 | 543 | 34 | Capacity expansion target: OFC/OF capacity "~43 mn fkm p.a." and "~34 mn fkm p.a." respectively |
| 17 | 543 | 56% | Capacity expansion target: OFC/OF capacity "~43 mn fkm p.a." and "~34 mn fkm p.a." respectively |
| 17 | 544 | 60% | Export revenue target: "60%+ from FY27 onwards"; body text also references exports "at 56% of revenues" |
| 17 | 544 | 27 | Export revenue target: "60%+ from FY27 onwards"; body text also references exports "at 56% of revenues" |
| 17 | 545 | 300 | Preform manufacturing capacity target "300 MT p.a." |
| 17 | 546 | 92% | Private-sector revenue share: "increased to 92%, reflecting a strategic shift from Government to Private customers" |
| 18 | 567 | 85% | Products-segment revenue share "~85% of revenues"; column count reference "#1 in OFC" |
| 18 | 567 | 1 | Products-segment revenue share "~85% of revenues"; column count reference "#1 in OFC" |
| 18 | 568 | 26,000 | Order book size claim "more than Rs. 26,000 crore" (diversified order book) |
| 18 | 570 | 2,000 | Defence export order book qualifier: "Rs.~2,000 crores through proposed aerospace business being acquired" - contingent on pending acquisition |
| 18 | 572 | 56% | Export revenue share "~56% of revenues" positioning HFCL as global player |
| 18 | 578 | 92% | Private-customer revenue share "92% of revenues" lowering working-capital intensity |
| 19 | 590 | 07 | Sub-TOC entry "19 Shareholders Information" |
| 19 | 599 | 19 | Sub-TOC entry "19 Shareholders Information" (repeat numbering in appendix chapter TOC) |
| 19 | 600 | 20 | Sub-TOC entry "20 Abbreviations / Description" |
| 20 | 607 | 30, | Slide subtitle "SHAREHOLDING AS ON JUNE 30, 2026" (date reference, appears twice due to two-column subtitle repeat) |
| 20 | 607 | 2026 | Slide subtitle "SHAREHOLDING AS ON JUNE 30, 2026" (date reference, appears twice due to two-column subtitle repeat) |
| 20 | 607 | 30, | Slide subtitle "SHAREHOLDING AS ON JUNE 30, 2026" (date reference, appears twice due to two-column subtitle repeat) |
| 20 | 607 | 2026 | Slide subtitle "SHAREHOLDING AS ON JUNE 30, 2026" (date reference, appears twice due to two-column subtitle repeat) |
| 20 | 613 | 500183 | Share info table: "NSE TICKER HFCL"; "BSE TICKER 500183" |
| 20 | 615 | 28.29% | Shareholding pie chart: Promoter 45.05% (see line 618) cross-ref; here "28.29%" DII/MF segment and Share info "MARKET CAP (Rs Crores) 32,563.57" |
| 20 | 615 | 32,563.57 | Shareholding pie chart: Promoter 45.05% (see line 618) cross-ref; here "28.29%" DII/MF segment and Share info "MARKET CAP (Rs Crores) 32,563.57" |
| 20 | 617 | 71.69% | Share info table: "% FREE-FLOAT 71.69%" |
| 20 | 618 | 45.05% | Shareholding pie chart: "45.05%" Promoter segment |
| 20 | 619 | 23,343.34 | Share info table: "FREE-FLOAT MARKET CAP (Rs Crores) 23,343.34" |
| 20 | 621 | 10.92% | Shareholding pie chart: "10.92%" FII's & FPI's segment |
| 20 | 622 | 1,53,06,02,463 | Share info table: "SHARES OUTSTANDING 1,53,06,02,463" |
| 20 | 624 | 15.74% | Shareholding pie chart: "15.74%" Others segment |
| 20 | 625 | 3 | Share info table: "3M ADTV (SHARES) 59296662" |
| 20 | 625 | 59296662 | Share info table: "3M ADTV (SHARES) 59296662" |
| 20 | 627 | 3 | Share info table: "3M ADTV (Rs Crores) 847.52" |
| 20 | 627 | 847.52 | Share info table: "3M ADTV (Rs Crores) 847.52" |
| 22 | 663 | 8, | Corporate office address "8, Commercial Complex, Masjid Moth..." |
| 22 | 665 | 2, | Corporate office address "Greater Kailash Part 2, New Delhi, Delhi - 110048" (PIN code component "2,") |
| 22 | 666 | 110048 | Corporate office PIN code "110048" |
| 22 | 672 | 91 | IR contact: "Tel: +91-11-3520 9400" (Amit Agarwal, Head - Investor Relations) |
| 22 | 672 | 11 | IR contact: "Tel: +91-11-3520 9400" (Amit Agarwal, Head - Investor Relations) |
| 22 | 672 | 3520 | IR contact: "Tel: +91-11-3520 9400" (Amit Agarwal, Head - Investor Relations) |
| 22 | 672 | 9400 | IR contact: "Tel: +91-11-3520 9400" (Amit Agarwal, Head - Investor Relations) |

## TABLE 3 — SLIDE 8 INCOME STATEMENT: EVERY LINE ITEM (18 of 18, per general operating rule 3 — zero/nil/dash standing items enumerated, never dropped)

| # | Line item | Line | Q1FY27 | Q4FY26 | Q-o-Q | Q1FY26 | Y-o-Y | Flags |
|---|---|---|---|---|---|---|---|---|
| 1 | Revenue from Operations | 242 | 1,914.98 | 1824.12 | 4.98% | 871.02 | 119.85% | — |
| 2 | Other Income | 243 | 31.15 | 22.26 | (not shown) | 14.53 | (not shown) | — |
| 3 | TOTAL INCOME | 244 | 1,946.13 | 1,846.38 | 5.40% | 885.55 | 119.77% | — |
| 4 | Total Expenses | 245 | 1,500.86 | 1509.45 | (not shown) | 842.62 | (not shown) | — |
| 5 | EBITDA | 246 | 445.27 | 336.93 | 32.16% | 42.93 | 937.20% | — |
| 6 | EBITDA MARGIN (%) | 247 | 23.25% | 18.47% | 478 Bps | 4.93% | 1832 Bps | — |
| 7 | Depreciation | 248 | 51.25 | 45.48 | (not shown) | 32.20 | (not shown) | — |
| 8 | Finance Cost | 249 | 62.48 | 62.78 | (not shown) | 55.62 | (not shown) | — |
| 9 | Share of net profits/(loss) of JV's accounted using equity method | 250-252 | -0.02 | -0.74 | (not shown) | 0.19 | (not shown) | — |
| 10 | Exceptional Items | 253 | – | – | (not shown) | – | (not shown) | **ZERO_STANDING** — dash in all 3 periods; canonical template-signal line (a line the company anticipates could carry a transaction of this type; presence of the row itself is the disclosure) |
| 11 | PBT | 254 | 331.52 | 227.93 | 45.45% | -44.70 | (not shown) | Q1FY26 was a pre-tax loss |
| 12 | PBT MARGIN (%) | 255 | 17.31% | 12.50% | 481 Bps | -5.13% | (not shown) | — |
| 13 | Tax | 256 | 85.88 | 43.48 | (not shown) | -15.40 | (not shown) | — |
| 14 | PROFIT AFTER TAX | 257 | 245.64 | 184.45 | 33.17% | -29.30 | (not shown) | Q1FY26 was a net loss |
| 15 | PAT MARGIN (%) | 258 | 12.83% | 10.11% | 272 Bps | -3.36% | (not shown) | — |
| 16 | Other Comprehensive Income | 259 | 72.16 | -39.23 | (not shown) | 38.92 | (not shown) | — |
| 17 | TOTAL COMPREHENSIVE INCOME | 260 | 317.80 | 145.22 | (not shown) | 9.62 | (not shown) | — |
| 18 | EPS (Diluted ₹) | 261 | 1.49 | 1.21 | (not shown) | -0.22 | (not shown) | Q1FY26 was a per-share loss |

## TABLE 4 — FOOTNOTES / FINE-PRINT / QUALIFYING DISCLAIMERS (15 of 15)

| # | Slide | Line | Text / substance | Flags |
|---|---|---|---|---|
| 1 | 5 | 161 | "(₹ IN CRORE)" — unit label qualifying the Revenue KPI callout | — |
| 2 | 5 | 169 | "(₹ IN CRORE & %)" — unit label qualifying the EBITDA & EBITDA Margin KPI callout | — |
| 3 | 5 | 174 | "(₹ IN CRORE & %)" — unit label qualifying the PAT & PAT Margin KPI callout | — |
| 4 | 5 | 162 | "...increased our FY27 revenue growth aspiration...to the best of our estimates to 40%..." — the 40% FY27 revenue growth figure is explicitly hedged as an "aspiration" / "estimate," not firm guidance | HEDGE_PHRASE |
| 5 | 7 | 203 | "All numbers in Rs. Crore" (extracted with OCR-artifact letter-spacing "Al l n umb ers i n Rs. Crore") — unit disclaimer for the Financial Highlights chart slide | — |
| 6 | 8 | 236 | "ALL NUMBERS IN RS. CRORE" (extracted with spaced-caps rendering artifact) — unit disclaimer for the Income Statement table | — |
| 7 | 9 | 268 | "All numbers in Rs. Crore" — unit disclaimer for the Order Book chart slide | — |
| 8 | 9 | 274 | "(₹ IN CRORES)" — sub-label under the Customer Wise order-book chart | — |
| 9 | 9 | 297 | "Diversified and growing Order book provides strong revenue visibility across telecom and defence" — qualifying caption under the order-book chart | — |
| 10 | 12 | 401 | "Map not to Scale only for illustration purpose" — disclaimer under the overseas-offices map graphic | — |
| 11 | 14 | 456-458 | "As Phase1 for creating facility for MMHG in upcoming 1000 Acre Andhra Ammunition Complex" — qualifies the ₹275 Cr capex figure as a Phase-1 tranche only, not the full facility cost | — |
| 12 | 15 | 498-499 | "~₹2,300 Cr total Defence order book (~INR 2000 crs through an entity proposed to be acquired)" — roughly 87% of the stated defence order book is contingent on an acquisition that has not yet closed | **HEDGE_PHRASE / ACQUISITION_CONTINGENT** |
| 13 | 17 | 536 | "EBITDA margin to expand from ~16.7% in FY26 to 22-25% by FY29" — forward multi-year target range, tilde-approximated baseline | FORWARD_TARGET |
| 14 | 17 | 544 | "target to reach 60%+ from FY27 onwards" (export revenue) | FORWARD_TARGET |
| 15 | 18 | 570 | "Rs.~2,000 crores through proposed aerospace business being acquired" — repeats the acquisition-contingent defence export order-book qualifier from slide 15 | **HEDGE_PHRASE / ACQUISITION_CONTINGENT** (repeat) |

## SUMMARY OF FLAGS RAISED

- **ZERO_STANDING** (1): Slide 8, Income Statement, "Exceptional Items" row — dash in Q1FY27, Q4FY26 and Q1FY26.
- **OCR_UNCERTAIN** (1 slide, 1 token): Slide 2 cover slide — pdftotext yielded only 57 characters; OCR output "pryuly 202603" is garbled and its numeric content ("202603") is not reliably resolvable to a specific figure. Raw pdftotext cross-check (line 85) confirms only "//July 2026" is legible; no reliable page-number token could be recovered for this slide.
- **CHART_LABEL_INFERRED** (2 slides — 7 and 9, 33 tokens combined): the bar-chart data on these two slides is native vector text per A1's pdfimages check, but pdftotext -layout scatters the labels non-spatially across the page (values, axis labels and percentage labels are not reliably left-to-right/top-to-bottom aligned to their bars in the raw extraction). Every value on slides 7 and 9 was cross-validated against the Income Statement table (slide 8) and the order-book/product infographics (slides 9, 11) where a match exists; where no independent cross-check exists (order-book category/customer segment bars), the likely label is offered with "likely" hedging rather than asserted as certain. A3/A4 should treat slide 7/9 bar-to-label mapping as inferred, not read directly off the deck.
- **HEDGE_PHRASE / ACQUISITION_CONTINGENT** (3 occurrences across slides 5, 15, 17, 18): the 40% FY27 revenue growth figure (slide 5) is stated as "aspiration"/"best estimate," not committed guidance; and roughly ₹2,000 Cr of the stated ~₹2,300 Cr defence order book (slides 15, 18) is contingent on an aerospace-business acquisition that is "proposed" (not closed) as of this presentation date.
- **FORWARD_TARGET** (2 occurrences, slide 17): FY26-to-FY29 EBITDA margin target range (~16.7% -> 22-25%) and FY27-onwards export-revenue target (60%+) are multi-year targets, not current-quarter results.
- **DROPPED_SLIDE**: not assessable — no prior-quarter ledger was available at the injected `PRIOR_LEDGER_PATH` for this run; comparison could not be performed with evidence. Recorded as a methodology gap only; zero DROPPED_SLIDE flags are raised because none could be evidenced, not because none occurred.
- **ZERO_NUMBERS** (1 slide): Slide 21 (Abbreviations/Description glossary) carries zero numeric tokens — expected and consistent with its content type (pure text/table of abbreviation-to-description pairs).

```yaml
stage: A2-enumerator
company: "HFCL"
quarter: "q1fy27"
doctype: "presentation"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/hfcl-q1fy27/work/ledger_presentation_hfcl_q1fy27.md"
counts:
  notes: 0
  line_items: 18
  zero_standing: 1
  agenda_items: 0
  auditor_paras: 0
  entities: 0
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 22
  slide_numbers: 313
flags_raised: [ZERO_STANDING, OCR_UNCERTAIN, CHART_LABEL_INFERRED, HEDGE_PHRASE, ACQUISITION_CONTINGENT, FORWARD_TARGET]
gate_a2: pass
mismatch_note: ""
```
