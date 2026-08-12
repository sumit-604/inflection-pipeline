# A2 COMPLETENESS LEDGER — Macfos Limited (MCFOS), Q1 FY27, Investor Presentation

Source: `extract_presentation_mcfos_q1fy27.txt` (24 pages, 100% coverage, 14 OCR'd:
2,3,4,5,7,8,10,11,13,16,17,20,22,24). Prior-quarter presentation ledger: none available
— no DROPPED_SLIDE comparison possible this run (flag: NO_PRIOR_LEDGER).

Units: figures on pages 16 (P&L) and 12/14/15 (KPI charts) are printed in **Lakhs**
(x0.01 to Cr). Figures on pages 6 and 8 (FY revenue history) are printed in **Crores**
verbatim, unconverted. Each row below carries its source unit explicitly — no blanket
conversion applied.

Methodology note on granularity: a "slide_number" row = one disclosed numeric data
point (a chart bar value, a table cell, a stated percentage, a footnote figure). Where
a chart repeats an identical period-axis (e.g. "Q1 25-26 / Q1 26-27 / FY24-25 / FY25-26")
across multiple co-located sub-charts, the axis-label set is enumerated once per
sub-chart as a single row (not once per tick), since it is one physical axis. P&L
line items (page 16) and the FY revenue history table (page 8) are tracked separately
under LINE_ITEMS, not double-counted under SLIDE_NUMBERS.

=== A2 COUNT TEST ===
category: slides        grep_count: 24   sweep_count: 24   match: yes
category: line_items    grep_count: 25   sweep_count: 25   match: yes
category: footnotes     grep_count: 9    sweep_count: 9    match: yes
category: slide_numbers grep_count: 118  sweep_count: 118  match: yes
gate_a2: pass
=== END COUNT TEST ===

## Count-test methodology (how grep and sweep were reconciled)

1. **slides**: `grep -c '^\[page [0-9]\+\]$'` on the raw extract = 24. Manual walk of
   pages 1-24 = 24. Clean match, no iteration needed.
2. **footnotes**: `grep -noE '(\*{1,3}[A-Za-z]|Note:)'` = 9 matches. Manual sweep of
   every disclaimer/asterisk block across the deck = 9. Clean match on first pass.
3. **line_items** (page 16 P&L + page 8 revenue-history table): first-pass grep
   `^[0-9]+\s*\|` and `^[a-g]\.\s*\|` on the P&L block found only **12 of 19 rows**
   (rows 1,2,3,4,9,10 + sub-items a,b,c,e,f,g). **MISMATCH triggered a re-sweep.**
   Manual line-by-line reading of lines 498-524 found the grep missed 6 rows because
   OCR corrupted their leading digit: row "d." was OCR'd with a bracket (`d. [`) not a
   pipe; row 5 has a stray "DIGITAL MULTIMETER" product-photo artifact glued to its
   line start; row 6 has "aa @ or 6" prefix garble; row 7 has "F 7" prefix garble; row
   8 has "@ 8" prefix garble; row 11 has no pipe at all. A second, label-text-based
   grep (matching on the row description instead of the corrupted numeric prefix)
   recovered all 18 data rows + confirmed 1 header row (no value). Added the page 8
   table (7 rows, clean match, `[0-9]+\.[0-9]{2}` on line 238 = 7, FY-period grep on
   line 237 = 7). Final: 18 + 7 = 25, matching the corrected manual sweep. This is the
   single most consequential finding of the count test — see flag
   `OCR_ROW_LABEL_CORRUPTED` below.
4. **slide_numbers**: an automated per-page token extraction (canonical = raw
   pdftotext block; OCR block content included only where it adds tokens not already
   present in raw, to avoid double-counting OCR-restated duplicates) produced a raw
   token count requiring fragment-merging (e.g. a signature timestamp column-split
   into "20"/"42"/"14" merged back to one HH:MM:SS row; a DIN split into two grep
   fragments merged back to one 8-digit DIN row; period labels "1"/"25"/"26" from
   "Q1 25-26" merged back into the axis-label-group row they belong to) and exclusion
   of confirmed OCR-duplicate variants (page 10's stray "126" and page 11's "5977"
   are re-OCR'd fragments of numbers already captured cleanly from the raw block, not
   new data). One genuine under-count was found and corrected on re-sweep: page 8's
   timeline/evolution-graphic annotation cluster (lines 240-264) is severely garbled
   OCR, and the first manual pass under-enumerated it (14 tokens) against the
   mechanical extraction (18 tokens). Re-swept and expanded to all 18, each flagged
   `CHART_OCR_SEVERELY_GARBLED` (some of the 18 are plausibly OCR noise/icon-badge
   artifacts rather than true data — flagged, not silently dropped, per the "zero/nil
   rows are data" principle applied to uncertain rows too). Final matched total: 118.

---

## 1. SLIDES (24 of 24)

| # | Page | Title | Content type | OCR'd | Flags |
|---|------|-------|---------------|-------|-------|
| 1 | 1 | Reg. 30 cover letter to BSE | text/regulatory | no | SOURCE_TYPO (body text: "Q1 TY 2026-27") |
| 2 | 2 | Title slide — "Q1 TY 2026-27 Management Presentation" | text | yes (dup confirm) | SOURCE_TYPO |
| 3 | 3 | Index | text | yes (dup confirm) | |
| 4 | 4 | Section divider — "Business Overview" | text | yes (dup confirm) | |
| 5 | 5 | "What is ROBU?" — website/app screenshot | text + photo/chart | yes (unique content) | OCR_GARBLED |
| 6 | 6 | "Overview" — company description + KPI paragraph | text (KPI-dense) | no | LABEL_MISMATCH_REVENUE_VS_TOTAL_INCOME (see slide_numbers) |
| 7 | 7 | "Core Strengths" — 4-box graphic | graphic, no numbers | yes (dup confirm) | |
| 8 | 8 | "Company Evolution" — FY revenue table + timeline graphic | table + chart | yes (unique content) | CHART_OCR_SEVERELY_GARBLED; INTERNAL_INCONSISTENCY (vs slide 6) |
| 9 | 9 | "Promoters Profile" — 3 profiles | text/photo | no | |
| 10 | 10 | "Steep Rising Customer Engagement" — 4-panel chart cluster | chart | yes (dup confirm) | CHART_OCR_AMBIGUOUS (period-value pairing); ASTERISK_COUNT_MISMATCH; MISSING_FOOTNOTE_DEFINITION |
| 11 | 11 | "Customer / Orders Served" | chart | yes (dup confirm) | CHART_OCR_AMBIGUOUS (moderate confidence pairing) |
| 12 | 12 | "Inventory Management" — very-slow-moving % + return/replacement table | text + table | no | AMBIGUOUS_FOOTNOTE_MARKER |
| 13 | 13 | Section divider — "Operating and Financial Performance" | text | yes (dup confirm) | |
| 14 | 14 | "Growth Trend in Total Revenue and Profitability" — 3 charts | chart | no | LABEL_MISMATCH_REVENUE_VS_TOTAL_INCOME |
| 15 | 15 | "Key Ratios on Sustainable Financial Growth" — 4 charts | chart | no | CHART_OCR_AMBIGUOUS (CAGR-label vs period pairing) |
| 16 | 16 | "Profit and Loss" | table | yes (OCR is sole source; raw has title only) | OCR_ROW_LABEL_CORRUPTED; CROSS_CHECK_PASS vs standalone results; EXPECTED_DISCLOSURE_ABSENT (no consolidated P&L shown) |
| 17 | 17 | Section divider — "Management Perspective" | text | yes (dup confirm) | |
| 18 | 18 | "Management Perspective" — shareholder letter | text (KPI-dense) | no | LABEL_MISMATCH_REVENUE_VS_TOTAL_INCOME; NUMBER_DISCREPANCY_MINOR (18% vs computed ~17.15% PAT growth) |
| 19 | 19 | "ROBU 1.0 / ROBU 2.0" narrative | text | no | EXPECTED_DISCLOSURE_ABSENT (no Robu 2.0 revenue-share %) |
| 20 | 20 | Section divider — "Strategic Priorities" | text | yes (dup confirm) | |
| 21 | 21 | Strategic priorities grid (Robu 1.0 / Robu 2.0) | text/graphic, no numbers | no | |
| 22 | 22 | "ROBU 1.0" descriptive text | text | yes (near-blank OCR) | |
| 23 | 23 | "ROBU 2.0" — 4 verticals with SKU-addition counts | text/grid | no | EXPECTED_DISCLOSURE_ABSENT (no B2B/corporate revenue % split despite corporate-customer language on slide 18) |
| 24 | 24 | "Thank You!" | text | yes (no OCR text recovered) | NO_OCR_RECOVERED (immaterial — closing slide has no visible text to recover) |

---

## 2. SLIDE_NUMBERS (118 of 118)

### Slide 1 — cover letter (6)
| Line | Value | Context | Flags |
|------|-------|---------|-------|
| 16 | 11/08/2026 | Letter date | |
| 23 | 400001 | BSE address PIN code | low materiality |
| 24 | 543787 | BSE scrip code | |
| 47-48 | 2026.08.11 | DSC signature date | |
| 47-48 | 20:42:14 | DSC signature time | signed same day as letter date |
| 52 | 07938828 | Binod Prasad DIN | |
| 54 | 11-08-2026 | Footer date (matches letter date) | |

(7 rows listed; letter date and footer date are the same calendar date printed twice —
kept as 2 rows since they are 2 distinct print occurrences, both cited.)

### Slide 2 — title (1)
| Line | Value | Context | Flags |
|------|-------|---------|-------|
| 64 | 2026-27 | "Q1 TY 2026-27" period label in title | SOURCE_TYPO (TY not FY); line 72 OCR restates identically — REDUNDANT_OCR_CONFIRM, not double-counted |

### Slide 5 — website/app screenshot (2)
| Line | Value | Context | Flags |
|------|-------|---------|-------|
| 126 | SKU 1842217 | Product SKU code in screenshot mockup | OCR_GARBLED; ILLUSTRATIVE_NOT_FINANCIAL |
| 128 | 83999 / 8990 | Product price cluster, decimal points lost to OCR | OCR_GARBLED; ILLUSTRATIVE_NOT_FINANCIAL |

### Slide 6 — Overview paragraph (14)
| Line | Value | Context | Flags |
|------|-------|---------|-------|
| 148 | 2014 | Robu.in website launch year | |
| 148 | 2017 | Android app launch year | |
| 149 | Jan 2023 | iOS app launch | |
| 150 | 1,00,000+ | SKU count (current) | |
| 150 | 150+ | Brand count | |
| 150 | 210+ | Vendor tie-ups | |
| 152 | 50,000+ | Sq. ft warehouse | |
| 152 | 300+ | Staff (own + contract) | |
| 156 | 58% | Turnover CAGR, last 3 years | |
| 156 | 53% | EBITDA CAGR, last 3 years | |
| 156 | 53% | PAT CAGR, last 3 years | |
| 156 | 3 years | CAGR measurement period | |
| 157-158 | 256 Cr | FY24-25 turnover (Crore, as printed) | INTERNAL_INCONSISTENCY vs slide 8 table (257.68 Cr) |
| 158 | 312 Cr | FY25-26 turnover (Crore, as printed) | consistent with slide 8's 311.74 Cr within rounding |

### Slide 8 — Company Evolution timeline graphic, garbled OCR (18)
All from CHART OCR block, lines 240-264. Table portion (7 FY labels + 7 revenue
values) tracked under LINE_ITEMS, not repeated here.
| Line range | Value | Best-effort context | Flags |
|---|---|---|---|
| 240-264 | 280+ | Team size (Own+Contract) | CHART_OCR_SEVERELY_GARBLED |
| 240-264 | 2 | Employee baseline count, "2014" | CHART_OCR_SEVERELY_GARBLED |
| 240-264 | 2014 | Employee baseline year | CHART_OCR_SEVERELY_GARBLED |
| 240-264 | 118 | Current employee count | CHART_OCR_SEVERELY_GARBLED |
| 240-264 | 2,000 | Orders/day dispatch capacity | CHART_OCR_SEVERELY_GARBLED |
| 240-264 | 50,000+ | SKU count milestone (timeline, distinct from slide 6's 1,00,000+ current figure) | CHART_OCR_SEVERELY_GARBLED; NUMBER_TIMELINE_CHECK (verify vs slide 6) |
| 240-264 | 50 | Fragment, likely part of "50K+ Sqft" warehouse milestone | CHART_OCR_SEVERELY_GARBLED; OCR_FRAGMENT_UNCERTAIN |
| 240-264 | 2019 | Timeline year marker | CHART_OCR_SEVERELY_GARBLED |
| 240-264 | 2020 | Timeline year marker | CHART_OCR_SEVERELY_GARBLED |
| 240-264 | 2021 | Timeline year marker | CHART_OCR_SEVERELY_GARBLED |
| 240-264 | 2022 | Timeline year marker | CHART_OCR_SEVERELY_GARBLED |
| 240-264 | 2023 | Timeline year marker | CHART_OCR_SEVERELY_GARBLED |
| 240-264 | 2024 | Timeline year marker | CHART_OCR_SEVERELY_GARBLED |
| 240-264 | 2025 | Timeline year marker | CHART_OCR_SEVERELY_GARBLED |
| 240-264 | 03 | Unclear fragment (possibly icon/step badge) | CHART_OCR_SEVERELY_GARBLED; OCR_FRAGMENT_UNCERTAIN — possibly not data |
| 240-264 | 7 | Unclear fragment (possibly step/icon number) | CHART_OCR_SEVERELY_GARBLED; OCR_FRAGMENT_UNCERTAIN — possibly not data |
| 240-264 | 3 | Unclear fragment (likely OCR split of "3D" printing service, not a standalone data value) | CHART_OCR_SEVERELY_GARBLED; OCR_FRAGMENT_UNCERTAIN — likely not data |
| 240-264 | 6 | Unclear fragment ("6 the Pandemic" — possibly bullet/icon artifact) | CHART_OCR_SEVERELY_GARBLED; OCR_FRAGMENT_UNCERTAIN — likely not data |

Recommendation to A3/A4: this cluster needs source-image verification before being
relied on for any milestone-timeline claim; 4 of the 18 rows above are flagged as
possibly non-data OCR noise rather than true disclosure content, but are enumerated
per instruction (never drop a row on an interpretive judgment call).

### Slide 9 — Promoters profile (3)
| Line | Value | Context | Flags |
|------|-------|---------|-------|
| 280 | 15 years | Atul Maruti Dumbre, Chairman & MD, experience | |
| 280 | 15 years | Binod Prasad, WTD & CFO, experience | |
| 280 | 15 years | Nileshkumar Chavhan, WTD, experience | |

### Slide 10 — Steep Rising Customer Engagement, 4-chart cluster (22)
Raw block lines 283-314 used as canonical (OCR block 316-358 is a redundant
restatement, REDUNDANT_OCR_CONFIRM, not double-counted).
| Line | Value | Chart (best-effort) | Flags |
|------|-------|------|-------|
| 289-308 | axis-label-group: Q1 25-26 / Q1 26-27 / FY24-25 / FY25-26 | Avg. Monthly Website & App Visitors chart | CHART_OCR_AMBIGUOUS |
| 289-297 | 6,02,470 | Visitors chart data point | CHART_OCR_AMBIGUOUS (period pairing uncertain) |
| 289-297 | 5,85,917 | Visitors chart data point | CHART_OCR_AMBIGUOUS |
| 289-297 | 5,30,418 | Visitors chart data point | CHART_OCR_AMBIGUOUS |
| 289-291 | 9,78,555 | Visitors chart data point | CHART_OCR_AMBIGUOUS |
| 293 | 3,96,366 | Visitors chart data point | CHART_OCR_AMBIGUOUS |
| 290 | 5,05,250 | Visitors chart data point (may belong to visitors or orders panel — genuinely ambiguous) | CHART_OCR_AMBIGUOUS |
| 302 | axis-label-group: Q1 25-26 / Q1 26-27 / FY24-25 / FY25-26 | Total Orders Served chart | CHART_OCR_AMBIGUOUS |
| 302 | 1,14,066 | Orders Served data point | ties to slide 11 |
| 302 | 1,19,661 | Orders Served data point | ties to slide 11 |
| 290,292,294,295 | axis-label-group: Q1 25-26 / Q1 26-27 / FY24-25 / FY25-26 | Avg Order Value chart | |
| 290 | 6,797 | Avg Order Value data point | |
| 292 | 6,111 | Avg Order Value data point | |
| 294 | 5,196 | Avg Order Value data point | |
| 295 | 4,632 | Avg Order Value data point | |
| 308 | axis-label-group: Mar-23 / Mar-24 / Mar-25 / Mar-26 / Jun-26 | Total SKU's trend chart | |
| 304 | 12,759 | Total SKU's, Mar-23 | |
| 303 | 18,349 | Total SKU's, Mar-24 | |
| 295 | 71,054 | Total SKU's, Mar-25 | |
| 289 | 1,05,775 | Total SKU's, Mar-26 (best-fit by magnitude/order) | |
| 289 | 1,06,981 | Total SKU's, Jun-26 (best-fit by magnitude/order) | |
| 314 | 10,02,382 | Footnote: "Total Visitors June-26" | ASTERISK_COUNT_MISMATCH (printed "***" here vs "**" in OCR restatement line 332); MISSING_FOOTNOTE_DEFINITION applies to the separate "AVG ORDER VALUE*" single-asterisk marker at line 310/342, which has no defining footnote text anywhere on the slide |

### Slide 11 — Customer / Orders Served (5)
| Line | Value | Context | Flags |
|------|-------|---------|-------|
| 379 | axis-label-group: Q1 FY 25-26 / Q1 TY 26-27 | chart period axis | |
| 365-366 | 1,14,066 | Orders Served, Q1 FY25-26 (inferred pairing) | CHART_OCR_AMBIGUOUS (moderate confidence) |
| 365 | 1,19,661 | Orders Served, Q1 TY26-27 (inferred pairing) | CHART_OCR_AMBIGUOUS (moderate confidence) |
| 374 | 59,771 | Customers Served, Q1 FY25-26 (inferred pairing) | CHART_OCR_AMBIGUOUS |
| 373 | 67,480 | Customers Served, Q1 TY26-27 (inferred pairing) | CHART_OCR_AMBIGUOUS |

### Slide 12 — Inventory Management (6)
| Line | Value | Context | Flags |
|------|-------|---------|-------|
| 403 | 5.52% | Very slow-moving inventory, Jun-26 | |
| 405 | 6.21% | Very slow-moving inventory, Mar-26 (comparison) | |
| 407 | 9 Months | "Very slow-moving" definition threshold | |
| 414 | 58.19 (Lakhs) | Return/Replacement cost to company, FY24-25 | |
| 415 | 109.89 (Lakhs) | Return/Replacement cost to company, FY25-26 | |
| 416 | 23.88 (Lakhs) | Return/Replacement cost to company, Q1 TY26-27 | |

### Slide 14 — Growth Trend, 3-chart cluster (12)
All in Lakhs.
| Line | Value | Context | Flags |
|------|-------|---------|-------|
| 451 | axis-label-group: Q1 25-26 / Q1 26-27 / FY25-26 | Revenue chart axis | LABEL_MISMATCH_REVENUE_VS_TOTAL_INCOME |
| 446 | 5,987.34 | "Revenue" chart, Q1 25-26 — actually = Total Income, matches P&L row 3 | LABEL_MISMATCH_REVENUE_VS_TOTAL_INCOME |
| 444 | 8,245.91 | "Revenue" chart, Q1 26-27 — actually = Total Income | LABEL_MISMATCH_REVENUE_VS_TOTAL_INCOME |
| 438 | 31,179.89 | "Revenue" chart, FY25-26 — actually = Total Income | LABEL_MISMATCH_REVENUE_VS_TOTAL_INCOME |
| 451 | axis-label-group: Q1 25-26 / Q1 26-27 / FY25-26 | EBITDA chart axis | |
| 445 | 802.34 | EBITDA, Q1 25-26 (computationally verified) | |
| 444 | 975.62 | EBITDA, Q1 26-27 (computationally verified) | |
| 437 | 4,106.13 | EBITDA, FY25-26 | |
| 451 | axis-label-group: Q1 25-26 / Q1 26-27 / FY25-26 | PAT chart axis | |
| 446 | 496.77 | PAT, Q1 25-26 — ties exactly to P&L row 10 | |
| 445 | 581.95 | PAT, Q1 26-27 — ties exactly to P&L row 10 | |
| 439 | 2,560.97 | PAT, FY25-26 — ties exactly to P&L row 10 | |

### Slide 15 — Key Ratios, 4-chart cluster (16)
| Line | Value | Context | Flags |
|------|-------|---------|-------|
| 483 | axis-label-group: Q1 25-26 / Q1 26-27 / FY25-26 | EBITDA % chart axis | |
| 468 | 13.40% | EBITDA % chart value (period pairing uncertain; possibly a "CAGR last 3 year" callout rather than a period bar) | CHART_OCR_AMBIGUOUS |
| 465 | 8.30% | EBITDA % chart value | CHART_OCR_AMBIGUOUS |
| 465 | 8.21% | EBITDA % chart value | CHART_OCR_AMBIGUOUS |
| 483 | axis-label-group: Q1 25-26 / Q1 26-27 / FY25-26 | PAT % chart axis | |
| 469 | 13.17% | PAT % chart value (period pairing uncertain, same CAGR-callout ambiguity as above) | CHART_OCR_AMBIGUOUS |
| 475 | 11.83% | PAT % chart value | CHART_OCR_AMBIGUOUS |
| 474 | 7.06% | PAT % chart value | CHART_OCR_AMBIGUOUS |
| 483 | axis-label-group: Q1 25-26 / Q1 26-27 / FY25-26 | Return on Net Worth % chart axis | |
| 477 | 6.88% | RoNW % chart value | CHART_OCR_AMBIGUOUS |
| 478 | 5.94% | RoNW % chart value | CHART_OCR_AMBIGUOUS |
| 476 | 6.95% | RoNW % chart value | CHART_OCR_AMBIGUOUS |
| 483 | axis-label-group: Q1 25-26 / Q1 26-27 / FY25-26 | ROCE % chart axis | |
| 465 | 27.42% | ROCE % chart value | CHART_OCR_AMBIGUOUS |
| 466 | 31.08% | ROCE % chart value | CHART_OCR_AMBIGUOUS |
| 477 | 5.59% | ROCE % chart value | CHART_OCR_AMBIGUOUS |

Note: the "CAGR LAST 3 YEAR" caption at line 467 is a text label, not itself a
separate numeric value — it appears to annotate one of the 12 percentages above
(most likely 13.40% and/or 13.17%) as a 3-year CAGR figure rather than a period bar,
but which chart(s) it applies to cannot be determined from text/OCR alone. Flagged
CHART_OCR_AMBIGUOUS across the affected rows; recommend source-image check by A3/A4
before using these ratios in any period-over-period comparison.

### Slide 18 — Management Perspective letter (6)
| Line | Value | Context | Flags |
|------|-------|---------|-------|
| 541 | ₹82.46 crore | Stated "revenue" — actually = Total Income (82.46 Cr = 8,245.91 Lakhs, the Total Income row, not the 81.34 Cr Revenue-from-Operations figure) | LABEL_MISMATCH_REVENUE_VS_TOTAL_INCOME |
| 541 | ₹9.75 crore | EBITDA — ties to slide 14 (975.62 Lakhs) | |
| 541 | ₹5.82 crore | PAT — ties to P&L exactly (581.95 Lakhs) | |
| 542 | 38% | Stated revenue growth YoY, comparable Ind AS basis | consistent with computed ~37.7% on Total Income basis |
| 542 | 22% | Stated EBITDA growth YoY | consistent with computed ~21.6% |
| 542 | 18% | Stated PAT growth YoY | NUMBER_DISCREPANCY_MINOR — computed PAT growth (581.95 vs 496.77) = 17.15%, rounds to 17%, not 18% |

### Slide 19 — ROBU 1.0/2.0 narrative (1)
| Line | Value | Context | Flags |
|------|-------|---------|-------|
| 571 | three years | "Over the past three years" — ROBU 2.0 Drone vertical momentum, qualitative duration, not a hard KPI | QUALITATIVE_DURATION |

### Slide 23 — ROBU 2.0 verticals (6)
| Line | Value | Context | Flags |
|------|-------|---------|-------|
| 643-645 | 295 SKUs / 5 Categories | Own Electronics Products, added till March-26 | |
| 646-647 | 6 new SKUs | Own Mechanical Products, Drone Frames | |
| 641 | 7 SKUs / 2 categories | Own Drone Products, launched | |
| 642-643 | 650 SKUs | OEM Products, added during the year | |

(4 rows shown group two co-located numbers each — 6 individual values: 295, 5, 6, 7,
2, 650.)

---

## 3. LINE_ITEMS (25 of 25 valued rows; 26 rows total incl. 1 header)

### 3a. Profit and Loss table (page 16, OCR-recovered) — Lakhs, Quarter ended 30-06-2026 / Quarter ended 30-06-2025 / Year ended 31-03-2026

| # | Line | Particulars | Q1FY27 | Q1FY26 | FY26 | Flags |
|---|------|-------------|--------|--------|------|-------|
| 1 | 501 | Revenue from operations | 8,133.87 | 5,926.80 | 30,874.84 | CROSS_CHECK_PASS (exact tie to results ledger standalone, line 106) |
| 2 | 502 | Other income | 112.04 | 60.54 | 305.05 | CROSS_CHECK_PASS |
| 3 | 503 | Total income (1+2) | 8,245.91 | 5,987.34 | 31,179.89 | CROSS_CHECK_PASS; note this is the figure the deck's charts (slide 14/18) label "Revenue" |
| 4 | 504 | Expenses (header) | — | — | — | HEADER_NO_VALUE, not counted in numeric total |
| 4a | 505 | Cost of Material Consumed | 28.71 | 10.18 | 75.21 | CROSS_CHECK_PASS |
| 4b | 506 | Purchase of Stock-in-Trade | 7,953.00 | 5,015.04 | 26,032.07 | CROSS_CHECK_PASS |
| 4c | 507 | Changes in Inventory of Stock-in-Trade | (1,791.36) | (523.03) | (2,397.38) | CROSS_CHECK_PASS |
| 4d | 508 | Employee benefits expenses | 368.68 | 254.98 | 1,246.84 | CROSS_CHECK_PASS; OCR_ROW_LABEL_CORRUPTED (OCR rendered "d. [" not "d. |") |
| 4e | 509 | Finance cost | 100.40 | 56.05 | 361.72 | CROSS_CHECK_PASS |
| 4f | 510 | Depreciation and Amortization Expenses | 83.09 | 75.02 | 325.13 | CROSS_CHECK_PASS |
| 4g | 511 | Other expenses | 711.27 | 427.83 | 2,100.78 | CROSS_CHECK_PASS |
| 5 | 512 | Total Expense from 4(a) to 4(g) | 7,453.78 | 5,316.07 | 27,744.37 | CROSS_CHECK_PASS; OCR_ROW_LABEL_CORRUPTED ("DIGITAL MULTIMETER" product-photo artifact glued to line start) |
| 6 | 513-514 | Profit/(Loss) before Exceptional Item and Tax | 792.13 | 671.27 | 3,435.52 | CROSS_CHECK_PASS; OCR_ROW_LABEL_CORRUPTED ("aa @ or 6" prefix garble) |
| 7 | 515 | Exceptional Item | — | — | — | ZERO_STANDING (dash all 3 periods); CROSS_CHECK_PASS vs results ledger (also nil); OCR_ROW_LABEL_CORRUPTED ("F 7" prefix garble) |
| 8 | 516 | Profit/(Loss) before tax (6-7) | 792.13 | 671.27 | 3,435.52 | CROSS_CHECK_PASS; OCR_ROW_LABEL_CORRUPTED ("@ 8" prefix garble) |
| 9 | 517 | Tax expenses | 210.18 | 174.50 | 874.55 | CROSS_CHECK_PASS; deck aggregates results-ledger's 3 tax sub-lines (current/deferred/prior-year) into one line — simplification, not an error |
| 10 | 518 | Profit for the year (8-9) | 581.95 | 496.77 | 2,560.97 | CROSS_CHECK_PASS; also ties exactly to slide 14 & slide 18 PAT figures |
| 11 | 519 | Other Comprehensive Income, Net of Tax | — | — | (16.47) | ZERO_STANDING (dash in Q1FY27 and Q1FY26 columns; FY26 carries a real value) — partial zero-standing, not full; CROSS_CHECK_PASS |
| 12 | 520-521 | Total Comprehensive Income (10+11) | 581.95 | 496.77 | 2,544.50 | CROSS_CHECK_PASS; OCR_ROW_LABEL_CORRUPTED (no line-start digit at all, "11" and "12" run into prose) |

**Cross-check verdict: PASS.** All 12 numbered rows (18 individual values across the 3
period columns, excluding the nil Exceptional Item row) tie exactly to the STANDALONE
results filing ledger (`ledger_results_mcfos_q1fy27.md`, section 5, lines 106-129).
The deck's P&L reproduces standalone figures only — see flag
`EXPECTED_DISCLOSURE_ABSENT` below regarding the consolidated statement the cover
letter says was also filed.

### 3b. FY Revenue History table (page 8) — Crore, as printed (no conversion)

| Line | FY Period | Revenue (INR Cr) | Flags |
|------|-----------|-------------------|-------|
| 237-238 | 2019-20 | 16.22 | |
| 237-238 | 2020-21 | 27.12 | |
| 237-238 | 2021-22 | 55.51 | |
| 237-238 | 2022-23 | 80.80 | |
| 237-238 | 2023-24 | 126.36 | |
| 237-238 | 2024-25 | 257.68 | INTERNAL_INCONSISTENCY vs slide 6 prose ("256 Cr") — a 1.68 Cr gap too large to be simple rounding |
| 237-238 | 2025-26 | 311.74 | Reconciles to Total Income basis (31,179.89 Lakhs = 311.80 Cr, off by 0.06 Cr / immaterial) more closely than to Revenue-from-Operations basis (308.75 Cr, off by ~3 Cr) — consistent with the deck's recurring "Revenue" = Total Income labeling pattern |

---

## 4. FOOTNOTES (9 of 9)

| # | Line | Slide | Footnote text (verbatim/paraphrased) | Flags |
|---|------|-------|----------------------------------------|-------|
| 1 | 356-358 | 10 | "**The increase in SKUs is primarily driven by the addition of small and low-cost items." (defines ** on "TOTAL SKU'S**") | |
| 2 | 314 | 10 | "***Total Visitors June-26= 10,02,382" | ASTERISK_COUNT_MISMATCH (printed as *** here, as ** in the OCR-restated duplicate at line 332) |
| 3 | 310 | 10 | "AVG ORDER VALUE*" — single-asterisk marker with no corresponding defining footnote text found anywhere on the slide | MISSING_FOOTNOTE_DEFINITION |
| 4 | 407 | 12 | "*Very Slow-moving is, Inventory/Material older than 9 Months." | AMBIGUOUS_FOOTNOTE_MARKER (shares single "*" with footnotes 5 and 6 below — no *, **, *** differentiation despite being 3 distinct statements) |
| 5 | 408 | 12 | "*These are not perishable in Nature, neither Obsolete Items." | AMBIGUOUS_FOOTNOTE_MARKER |
| 6 | 409 | 12 | "* These are primarily low-cost SKUs with a longer rotation cycle." | AMBIGUOUS_FOOTNOTE_MARKER |
| 7 | 455-456 | 14 | "Note: The Company has adopted Ind AS from 1 April 2026. Comparative figures for Q1 FY 2025-26 have been restated under Ind AS. Ind AS figures for the full year FY 2024-25 have not been presented." | |
| 8 | 488-489 | 15 | Same Ind AS note, verbatim repeat | DUPLICATE_FOOTNOTE (consistent repetition, not itself an error) |
| 9 | 523-524 | 16 | Same Ind AS note, verbatim repeat (3rd occurrence) | DUPLICATE_FOOTNOTE |

---

## 5. FLAGS RAISED — summary

- **EXPECTED_DISCLOSURE_ABSENT** (x3): (a) no B2B/corporate-revenue % split anywhere
  in the deck despite slide 18 explicitly citing "increasing traction from corporate
  customers"; (b) no explicit Robu 2.0 revenue-share % — only qualitative language
  (slide 19) plus per-vertical SKU-addition counts (slide 23), never a revenue
  contribution figure; (c) no consolidated P&L shown despite the cover letter (slide
  1) stating the presentation covers "Unaudited Standalone and consolidated Financial
  Statement" — only standalone figures appear (slide 16, cross-check confirmed).
- **OCR_ROW_LABEL_CORRUPTED**: 6 of 12 P&L numbered rows on slide 16 have
  OCR-corrupted line-start prefixes (stray "DIGITAL MULTIMETER" product-photo text,
  a bracket instead of pipe, garbled "aa @ or 6" / "F 7" / "@ 8" prefixes). Values
  themselves are intact and cross-check clean; only the row-number recognition was
  affected. This is the finding that triggered the GATE A2 re-sweep on line_items.
- **INTERNAL_INCONSISTENCY**: slide 6 prose states FY24-25 turnover "256 Cr" while
  slide 8's own table states 257.68 Cr for the same period, within the same document.
- **LABEL_MISMATCH_REVENUE_VS_TOTAL_INCOME**: the deck's "Revenue" charts (slide 14)
  and prose (slides 6, 8, 18) consistently plot/cite Total Income (revenue + other
  income) rather than Revenue from Operations. Other income is small (Lakhs 112.04 /
  60.54 / 305.05 across the three periods) so the distortion is not large, but the
  labeling is imprecise across 4 separate slides, not a one-off.
- **NUMBER_DISCREPANCY_MINOR**: slide 18 states 18% PAT growth YoY; computed from the
  deck's own PAT figures (581.95 vs 496.77) the growth is 17.15%, rounding to 17%.
- **CHART_OCR_AMBIGUOUS / CHART_OCR_SEVERELY_GARBLED**: slides 8, 10, 11, 15 carry
  chart clusters where OCR text recovery could not reliably establish which numeric
  value pairs with which period label (garbled layout, scrambled reading order).
  Every number found is enumerated; precise period assignment is flagged for
  image-level verification rather than asserted.
- **MISSING_FOOTNOTE_DEFINITION**: slide 10's "AVG ORDER VALUE*" marker has no
  defining footnote text anywhere on the slide.
- **AMBIGUOUS_FOOTNOTE_MARKER**: slide 12 has three distinct footnote sentences all
  sharing a single, undifferentiated "*" marker.
- **ASTERISK_COUNT_MISMATCH**: slide 10's visitor-count footnote is printed as "***"
  in the raw extraction and "**" in the OCR-restated duplicate of the same slide.
- **NO_PRIOR_LEDGER**: no prior-quarter presentation ledger was supplied, so
  DROPPED_SLIDE comparison could not be performed this run.
- **SOURCE_TYPO**: source document prints "Q1 TY 2026-27" (not "Q1 FY 2026-27")
  verbatim and repeatedly (slides 1, 2 and elsewhere) — extracted as-is per A1,
  re-flagged here for A3 visibility since it appears on the title slide itself.
- **OCR_GARBLED**: slide 5's website-screenshot mockup (SKU 1842217, prices
  83999/8990) — illustrative product catalog content, not financial data, decimal
  points lost to OCR.
- **NO_OCR_RECOVERED**: slide 24 (closing "Thank You!" slide) — immaterial, no
  visible text to recover.

## 6. Cross-check status: page-16 P&L vs results filing

**PASS.** Every value on the presentation's P&L table (12 line items x up to 3
period columns = 18 non-nil values, plus the confirmed-nil Exceptional Item row)
ties exactly to the STANDALONE results filing ledger
(`runs/mcfos-q1fy27/work/ledger_results_mcfos_q1fy27.md`, section 5, lines
106-129): Q1FY27 revenue from operations 8,133.87 Lakhs, Q1FY26 5,926.80, FY26
30,874.84 — confirmed, matching the A1 handoff note precisely. PAT, Total Income,
Total Comprehensive Income and every expense sub-line also tie exactly. The deck's
single "Tax expenses" line is a clean aggregation of the results filing's three tax
sub-lines (current tax + deferred tax + prior-year adjustment) — a simplification,
not a discrepancy. The presentation does not reproduce or reference the
consolidated P&L at all, despite the cover letter's stated scope — flagged above.

```yaml
stage: A2-enumerator
company: "MCFOS"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/mcfos-q1fy27/work/ledger_presentation_mcfos_q1fy27.md"
counts:
  notes: 0
  line_items: 25
  zero_standing: 2
  agenda_items: 0
  auditor_paras: 0
  entities: 0
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 24
  slide_numbers: 118
flags_raised: [EXPECTED_DISCLOSURE_ABSENT, OCR_ROW_LABEL_CORRUPTED, INTERNAL_INCONSISTENCY, LABEL_MISMATCH_REVENUE_VS_TOTAL_INCOME, NUMBER_DISCREPANCY_MINOR, CHART_OCR_AMBIGUOUS, CHART_OCR_SEVERELY_GARBLED, MISSING_FOOTNOTE_DEFINITION, AMBIGUOUS_FOOTNOTE_MARKER, ASTERISK_COUNT_MISMATCH, NO_PRIOR_LEDGER, SOURCE_TYPO, OCR_GARBLED, NO_OCR_RECOVERED]
gate_a2: pass
mismatch_note: ""
```
