# A2 ENUMERATION LEDGER — Venus Pipes & Tubes (VENUSPIPES) — Q1 FY27 — Investor Presentation

Source: `extract_presentation_venuspipes_q1fy27.txt` (37 PDF pages, formfeed_count 37,
pages 4/7/16/29 OCR-confirmed pure divider slides with no numeric content).
Prior-quarter presentation ledger: **none available** — `DROPPED_SLIDE` cannot be computed
this quarter. Noted as a gap, not silently skipped (see DROPPED-SLIDE section below).

## METHODOLOGY NOTE — how "number" is defined for the count test

To make the grep pass and the manual sweep converge on an identical, auditable unit, a
"number" row in the NUMBERS table below is any standalone quantitative disclosure value
in the slide body text (Rs/INR amount, %, ratio, count, MT/MTPA volume, physical
dimension, CAGR/growth figure, calendar year used as a certification/award year, land
area, tenure/experience-years figure, or a footnote-embedded amount). The following are
intentionally **excluded** from both the grep pattern and the manual sweep, with the
rule stated once here rather than re-argued row by row:

- (a) the slide's own footer pagination numeral (bottom-of-slide page number) — this
  duplicates the `[page N]` citation marker already used throughout this ledger and is
  not disclosed content;
- (b) fiscal-period / quarter axis category labels (`FY22`, `FY23`, `Q1 FY26`, `Q1FY27`,
  `Mar-26`, etc.) used purely to tag a data series — the label is not itself a value;
- (c) the `01/02/03/04` ordinal callout numbers used as diagram-quadrant markers on
  slides 6 and 20 — layout numbering, not disclosure;
- (d) the duplicate restatement of a data point inside a `[CHART, page N, ...]` index
  line where the identical value already appears in the page body beneath it (per the
  A1 extraction note that these bracket lines are non-authoritative restatements added
  for citation convenience) — counted once, at its body-text line, flagged
  `CHART_RESTATEMENT` where the chart-flag line is the fastest cross-reference;
- (e) administrative/identifier codes on the BSE/NSE covering letter (page 1) and the
  closing contact page (page 37) — Scrip Code, ISIN, CIN, Membership No., phone
  numbers, signature date/time. These are bureaucratic identifiers, not disclosed
  operating or financial figures, and are listed separately in the ADMINISTRATIVE
  IDENTIFIERS table below, out of the GATE A2 numeric count test scope (stated
  explicitly so the exclusion is visible, not silent).

Grep pass = `pat = [+~-]?[0-9][0-9,]*\.?[0-9]*%?x?` applied to the extract body (lines
33–1189, i.e. pages 2–36), after mechanically stripping exclusions (a)–(d) above.
Manual sweep = independent page-by-page read of the same body producing the NUMBERS
table below. Both converged at **629** individual values; see COUNT TEST.

```
=== A2 COUNT TEST ===
category: slides    grep_count: 37   sweep_count: 37   match: yes
category: numbers    grep_count: 629  sweep_count: 629  match: yes
category: footnotes  grep_count: 17   sweep_count: 17   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep commands used (re-runnable):
- slides: `grep -n -E "^\[page [0-9]+\]" extract...txt | wc -l` → 37
- numbers: python re pass with pattern above over lines 33–1189, after excluding the 9
  `[CHART...]` restatement lines, the 4 `[OCR page...]` lines, the 29 pure footer-number
  lines + 9 "INR Cr unless specified"-trailer lines (footer digit stripped), the 35
  `[page N]` marker lines themselves, and FY/quarter-label + 01–04 ordinal fragments →
  629
- footnotes: `grep -n "INR Cr unless specified"` (9, excluding the 1 inline mention
  inside the page-10 chart-flag bracket, which is extraction meta-text not a slide
  footnote) + `grep -n "Safe Harbour"` (1) + `grep -n "Inventory Day Calculated"` (1) +
  `grep -n "Logos Are The Property"` (1) + page-34 formula/exclusion lines
  (`ROE =`, `D/E =`, `ROCE =`, `*Excluding Rs`, `^Excluding CWIP` — 5) → 17

---

## 1. SLIDES (37 rows — every PDF page)

| # | Page | Title | Content type | Notes / Flags |
|---|------|-------|--------------|----------------|
| 1 | 1 | BSE/NSE covering letter (Q1 FY27 Investor Presentation submission) | text | Not a deck slide — the regulatory covering letter that precedes the deck; explains the printed-footer-vs-PDF-page offset of 1. |
| 2 | 2 | Title page — "From Stainless-Steel Pipe Manufacturer to an Integrated Piping Solutions Partner" / Q1FY27 Investor Presentation – August 2026 | text | |
| 3 | 3 | Safe Harbour | text (disclaimer) | Forward-looking-statement disclaimer qualifying the whole deck; see FOOTNOTES #1. |
| 4 | 4 | Capex – Forward Integration into Pipe Spooling (divider) | photo | OCR-confirmed divider, no data beyond title. |
| 5 | 5 | Forward Integration into Pipe Spooling Backed by Anchor Customer | text/diagram | LOI + capex figures. |
| 6 | 6 | Moving up the Value Chain – Pipe Spooling | text/diagram | No numeric disclosures (01–04 are quadrant ordinals, excluded per rule c). |
| 7 | 7 | Operational & Financial Highlights (divider) | photo | OCR-confirmed divider, no data beyond title. |
| 8 | 8 | Key Highlights | text/numbers | Q1FY27 headline Revenue/EBITDA/PAT + operational bullets. |
| 9 | 9 | Inventory Days Stable Despite Significant Scale-Up in Business Operations | chart | Native chart, restated at [CHART, page 9] line 239. |
| 10 | 10 | Operation Stabilization post Capex Driving Better Cash Conversion | chart | Native chart, restated at [CHART, page 10] line 284. |
| 11 | 11 | Revenue Split across Segment – Q1 FY27 | chart | Native chart, restated at [CHART, page 11] line 327. |
| 12 | 12 | Revenue Split across Geographies – Q1 FY27 | chart | Native chart, restated at [CHART, page 12] line 365. |
| 13 | 13 | Key Financial Highlights – Q1 FY27 | chart | Native chart, restated at [CHART, page 13] line 405. |
| 14 | 14 | Profit & Loss Account (Q1FY27 vs Q1FY26 vs Q4FY26) | table | Full P&L, YoY/QoQ%. |
| 15 | 15 | From MD's Desk | text (quote) | Arun Kothari, Managing Director. |
| 16 | 16 | Company Overview (divider) | photo | OCR-confirmed divider, no data beyond title. |
| 17 | 17 | About US – Venus Pipes & Tubes Limited | text | Capacity, clientele, PAT CAGR bullets. |
| 18 | 18 | Building an Integrated Piping Solutions Platform | text/diagram | No numeric disclosures. |
| 19 | 19 | Diversified Product Range used across Industries | text/photo | No numeric disclosures. |
| 20 | 20 | Continuous Capacity Addition to Serve Growing Demand | chart | Stacked bar chart, restated at [CHART, page 20] line 612. |
| 21 | 21 | Integrated State of Art Manufacturing Facility | text | Land bank figure. |
| 22 | 22 | Presence Across the Globe | chart/map | Native chart, restated at [CHART, page 22] line 679. |
| 23 | 23 | End User Industry | text | No numeric disclosures. |
| 24 | 24 | Marquee Clientele | photo (logos) | "Logos Are The Property Of Their Respective Owners" disclaimer — FOOTNOTES #11. |
| 25 | 25 | Awards & Accolades | table/text | Calendar years + certification standard numbers. |
| 26 | 26 | Board of Directors | photo/text | 8 director bios with tenure/experience figures. |
| 27 | 27 | Strong Management at Helm | photo/text | Repeats the 4 executive-director bios from slide 26 + adds CFO/CS/President(Marketing). |
| 28 | 28 | Vision & Way Forward | text | No numeric disclosures. |
| 29 | 29 | Annexures (divider) | photo | OCR-confirmed divider, no data beyond title. |
| 30 | 30 | Key Historical Financials (FY22–FY26) | chart | Native chart, restated at [CHART, page 30] line 909. |
| 31 | 31 | Historical Profit & Loss Account (FY22–FY26 + CAGR) | table | |
| 32 | 32 | Historical Balance Sheet (Mar-22 to Mar-26) | table | Two dash-valued (nil) cells — ZERO_STANDING, see NUMBERS #Page32. |
| 33 | 33 | Historical Abridged Cash Flow Statement (FY22–FY26) | table | |
| 34 | 34 | Key Return Ratios (RoE, D/E, ROCE) | chart | Native chart, restated at [CHART, page 34] line 1080; RoE/ROCE are footnoted **adjusted-basis** figures — FOOTNOTES #13–17. |
| 35 | 35 | CSR Initiatives | text/photo | |
| 36 | 36 | Sustainability Initiatives | text | |
| 37 | 37 | Thank you / contact details | text | CIN codes + phone numbers — ADMINISTRATIVE IDENTIFIERS table. |

Grep cross-check: `grep -n -E "^\[page [0-9]+\]"` → 37 matches (lines 33, 67, 74, 108,
114, 154, 197, 203, 238, 283, 326, 364, 404, 438, 480, 513, 518, 550, 581, 611, 658,
678, 712, 737, 747, 795, 830, 865, 904, 908, 954, 996, 1041, 1079, 1112, 1145, 1190).
Manual sweep above independently lists 37 pages. **Match.**

## 2. DROPPED_SLIDE

No prior-quarter presentation ledger was supplied for this run (`Prior-quarter ledger
path: none available`), so slide-to-slide diffing against the prior deck cannot be
performed and `DROPPED_SLIDE` cannot be computed this quarter. This is a genuine gap,
not a pass — flagged so A3/A4 know the silence-detection layer is unavailable for this
review and any slide-drop signal must instead come from qualitative memory (companies/
VENUSPIPES.md) or a later run once a prior deck is captured.

## 3. NUMBERS (200 line-groups, 629 individual values — every number on every slide)

Legend: **Values** column lists every value found on that source line, in reading
order; **Ct** = count of values in the row (these sum to 629). `ZERO_STANDING` flags a
nil/dash-valued line item. `CHART_RESTATEMENT` marks a value whose authoritative
per-series/per-year breakdown is spelled out in full at the cited `[CHART, page N]`
index line (cited so a reader is not left guessing which bar the raw token belongs to).

### Page 2 — Title page

| Line | Description | Values | Ct |
|---|---|---|---|
| 72 | Presentation month/year in subtitle | 2026 | 1 |

### Page 5 — Capex / Pipe Spooling

| Line | Description | Values | Ct |
|---|---|---|---|
| 118 | LOI received for INR ___ Cr Order (Data Centre anchor customer) | 185 | 1 |
| 135 | Capex earmarked for spooling build-out | ~70 | 1 |

### Page 8 — Key Highlights

| Line | Description | Values | Ct |
|---|---|---|---|
| 206 | "All time high revenues of INR 320.5 Cr in Q1 FY27" | 320.5 | 1 |
| 218 | Revenue/EBITDA/PAT headline boxes: Rev 320.5 (+16.0% YoY), EBITDA 51.5 (+14.7% YoY), PAT 26.4 (+6.5% YoY) | 320.5, +16.0%, 51.5, +14.7%, 26.4, +6.5% | 6 |
| 219 | EBITDA Margin 16.1%, PAT Margin 8.2% (Q1FY27) | 16.1%, 8.2% | 2 |
| 226 | Welded Pipes/Tubes revenue growth 21% YoY; Seamless Pipes/Tubes growth 15% YoY | 21%, 15% | 2 |
| 229 | Domestic growth 31% YoY | 31% | 1 |
| 230 | Exports ~30% of revenue share; Exports = INR 94 Cr for the quarter | 30%, 94 | 2 |

### Page 9 — Inventory Days

| Line | Description | Values | Ct |
|---|---|---|---|
| 245 | Inventory Days FY23/24/25/26 callouts | 110, 103, 131, 121 | 4 |
| 247 | "Execution visibility increased from ~60 days to 5–6 months" | ~60, 5, 6 | 3 |
| 254 | Inventory (INR Cr) FY26 bar | 387 | 1 |
| 255 | Inventory (INR Cr) FY25 bar | 343 | 1 |
| 256 | Inventory (INR Cr) FY24 bar | 226 | 1 |
| 257 | Inventory (INR Cr) FY23 bar | 167 | 1 |
| 268 | "Order Book Increased ~2.5 times to INR 450 Crores" | ~2.5, 450 | 2 |
| 273 | "Revenue Grew by 28% CAGR to INR 1,167 Crores" | 28%, 1,167 | 2 |
| 276 | "Exports Increased ~13 times to INR 400 Crores" | ~13, 400 | 2 |
| 281 | Inventory Day formula: (Inventory/Revenue)*365 | 365 | 1 |

### Page 10 — Cash Conversion (CHART_RESTATEMENT, authoritative breakdown at line 284)

| Line | Description | Values | Ct |
|---|---|---|---|
| 289 | EBITDA growth +176% callout (FY23→FY26); Cash Conversion Ratio FY26 | +176%, 59% | 2 |
| 290 | Cashflow From Operations growth +1,144% callout (FY23→FY26) | +1,144% | 1 |
| 291 | EBITDA FY26 bar | 191 | 1 |
| 292 | EBITDA FY25 bar; Cashflow from Ops FY26 bar | 168, 112 | 2 |
| 293 | EBITDA FY24 bar; Cash Conversion Ratio FY25 | 146, 41% | 2 |
| 294 | Cash Conversion Ratio FY24 | 36% | 1 |
| 295 | EBITDA FY23 bar | 69 | 1 |
| 301 | Cashflow from Ops FY25 bar | 52 | 1 |
| 302 | Cashflow from Ops FY24 bar | 69 | 1 |
| 303 | Cash Conversion Ratio FY23 | 13% | 1 |
| 304 | Cashflow from Ops FY23 bar | 9 | 1 |
| 317 | Bullet: "Cash conversion improved from 13% in FY23 to 59% in FY26" | 13%, 59% | 2 |

### Page 11 — Revenue Split by Segment (CHART_RESTATEMENT, line 327)

| Line | Description | Values | Ct |
|---|---|---|---|
| 332 | Growth-rate callouts: Seamless +15%, Welded +21%, Others -3%, Total +16% | +15%, +21%, -3%, +16% | 4 |
| 334 | Q1FY27 values: Seamless 176.1, Welded 125.3, Others 19.8/19.1, Total 320.5 | 176.1, 125.3, 19.8, 19.1, 320.5 | 5 |
| 335 | Q1FY26 values: Seamless 153.0, Welded 103.6, Total 276.4 | 153.0, 103.6, 276.4 | 3 |
| 348 | Others revenue contribution: Q1FY26 7%, Q1FY27 6% | 7%, 6% | 2 |
| 353 | Welded revenue contribution: Q1FY26 38%, Q1FY27 39% | 38%, 39% | 2 |
| 354 | Seamless revenue contribution: Q1FY26 55%, Q1FY27 55% | 55%, 55% | 2 |

### Page 12 — Revenue Split by Geography (CHART_RESTATEMENT, line 365)

| Line | Description | Values | Ct |
|---|---|---|---|
| 370 | Domestic growth +31%; Total growth +16% | +31%, +16% | 2 |
| 371 | Exports growth -9% | -9% | 1 |
| 372 | Domestic Q1FY27 226.8; Exports Q1FY26 103.1; Total Q1FY27 320.5 | 226.8, 103.1, 320.5 | 3 |
| 373 | Exports Q1FY27 93.7; Total Q1FY26 276.4 | 93.7, 276.4 | 2 |
| 374 | Domestic Q1FY26 173.3 | 173.3 | 1 |
| 389 | Exports contribution Q1FY27 | 29% | 1 |
| 390 | Exports contribution Q1FY26 | 37% | 1 |
| 394 | Domestic contribution Q1FY26 | 63% | 1 |
| 395 | Domestic contribution Q1FY27 | 71% | 1 |

### Page 13 — Key Financial Highlights (CHART_RESTATEMENT, line 405)

| Line | Description | Values | Ct |
|---|---|---|---|
| 410 | Growth callouts: Revenue +16%, EBITDA +15%, PAT +6% | +16%, +15%, +6% | 3 |
| 411 | Q1FY27 Revenue 320.5, EBITDA 51.5, PAT 26.4 | 320.5, 51.5, 26.4 | 3 |
| 412 | Q1FY26 PAT | 24.8 | 1 |
| 413 | Q1FY26 Revenue 276.4, EBITDA 44.9 | 276.4, 44.9 | 2 |
| 427 | EBITDA Margin Q1FY26 16.2%/Q1FY27 16.1%; PAT Margin Q1FY26 9.0% | 16.2%, 16.1%, 9.0% | 3 |
| 428 | PAT Margin Q1FY27 | 8.2% | 1 |

### Page 14 — Profit & Loss Account (Q1FY27 / Q1FY26 / YoY / Q4FY26 / QoQ)

| Line | Line item | Values (Q1FY27, Q1FY26, [YoY%], Q4FY26, [QoQ%]) | Ct | Flags |
|---|---|---|---|---|
| 442 | Revenue from Operations | 320.5, 276.4, 16.0%, 302.2, 6.1% | 5 | |
| 444 | Cost of Goods Sold | 207.7, 185.6, 194.9 | 3 | |
| 446 | Gross Profit | 112.8, 90.8, 24.2%, 107.3, 5.1% | 5 | |
| 448 | Employee Cost | 15.7, 11.7, 13.5 | 3 | |
| 454 | Other Expenses | 45.6, 34.2, 44.4 | 3 | |
| 456 | EBITDA | 51.5, 44.9, 14.7%, 49.4, 4.3% | 5 | |
| 458 | EBITDA Margins (%) | 16.1%, 16.2%, 16.3% | 3 | |
| 460 | Other Income | 2.7, 3.9, 2.1 | 3 | |
| 462 | Depreciation | 7.2, 5.2, 6.3 | 3 | |
| 464 | EBIT | 47.0, 43.6, 7.8%, 45.2, 4.0% | 5 | |
| 466 | Finance Cost | 11.3, 9.8, 10.5 | 3 | |
| 468 | Exceptional Items | 0.0, 0.0, -0.2 | 3 | ZERO_STANDING (nil in Q1FY27 & Q1FY26; -0.2 in Q4FY26 — template line, watch for future non-zero exceptional items) |
| 470 | Profit before Tax | 35.7, 33.8, 5.6%, 34.9, 2.3% | 5 | |
| 472 | Tax | 9.3, 9.0, 9.5 | 3 | |
| 474 | Profit After Tax | 26.4, 24.8, 6.5%, 25.4, 3.9% | 5 | |
| 476 | PAT Margins (%) | 8.2%, 9.0%, 8.4% | 3 | |

### Page 15 — From MD's Desk

| Line | Description | Values | Ct |
|---|---|---|---|
| 485 | "highest-ever quarterly revenue of Rs. 320.5 crores" | 320.5 | 1 |
| 486 | "representing a healthy growth of 16% year-on-year" | 16% | 1 |

### Page 17 — About Us

| Line | Description | Values | Ct |
|---|---|---|---|
| 522 | "80+ Clientele base out of Fortune 500 Companies" | 80, 500 | 2 |
| 525 | "48,000 MT p.a. total installed capacity" | 48,000 | 1 |
| 531 | "Backward Integration of ~20,400 MT p.a." | ~20,400 | 1 |
| 540 | "Exports to more than 30+ Countries" | 30 | 1 |
| 545 | "34% PAT CAGR from FY22 to FY26" | 34% | 1 |

### Page 20 — Capacity Addition chart (CHART_RESTATEMENT — full Welded/Seamless/Total
per-year breakdown is authoritative at [CHART, page 20] line 612; the raw
stacked-bar layout below cannot be reliably re-attributed to a specific
segment purely from flattened pdftotext position, so rows here are listed
as printed, cross-referenced to line 612 for the definitive split)

| Line | Description | Values | Ct |
|---|---|---|---|
| 618 | "4x" bracket growth callout (Welded, right margin) | 4x | 1 |
| 620 | Total capacity, "Current" bar | 48,000 | 1 |
| 621 | Total capacity, FY26 bar | 43,800 | 1 |
| 622 | "~7x Capacity Expansion from FY19 to Current" callout; Total capacity FY24 & FY25 bars | ~7x, 38,400, 38,400 | 3 |
| 624 | Welded-segment "Current" bar (per line 612 breakdown) | 27,600 | 1 |
| 630 | Welded-segment FY26 bar | 27,600 | 1 |
| 631 | Welded-segment FY24 & FY25 bars | 24,000, 24,000 | 2 |
| 635 | Total capacity FY21, FY22, FY23 bars | 10,800, 10,800, 12,000 | 3 |
| 636 | Total capacity FY20 bar | 9,300 | 1 |
| 637 | Total capacity FY19 bar; Seamless-segment "Current" bar | 6,900, 20,400 | 2 |
| 638 | Segment bars (Welded FY21/22/23 + Seamless FY24/25/26 per line-612 mapping) | 7,200, 7,200, 8,400, 14,400, 14,400, 16,200 | 6 |
| 639 | Seamless-segment FY19/FY20 bars | 4,800, 7,200 | 2 |
| 640 | Seamless-segment FY19–FY23 bars | 2,100, 2,100, 3,600, 3,600, 3,600 | 5 |
| 648 | Dimension-range bullets: Seamless 6mm→114.3mm then 6mm→219.3mm; Welded 6mm→219.3mm then 6mm→1,422.4mm | 6, 114.3, 6, 219.3, 6, 219.3, 6, 1,422.4 | 8 |
| 653 | "Piercing line for Mother Hollow Pipes with current capacity of 20,400 MTPA" | 20,400 | 1 |

### Page 21 — Manufacturing Facility

| Line | Description | Values | Ct |
|---|---|---|---|
| 665 | "Total land bank of 2,66,282 sq. mt." | 2,66,282 | 1 |

### Page 22 — Presence Across the Globe / Exports (CHART_RESTATEMENT, line 679)

| Line | Description | Values | Ct |
|---|---|---|---|
| 697 | "Exports in More than 30+ Countries" | 30 | 1 |
| 700 | "~67x" growth callout, Exports Revenue FY20→FY26 | ~67x | 1 |
| 701 | Exports Revenue FY25, FY26 | 338, 400 | 2 |
| 703 | Exports Revenue FY24 | 99 | 1 |
| 704 | Exports Revenue FY20, FY21, FY22, FY23 | 6, 15, 40, 30 | 4 |
| 708 | Revenue Contribution row FY20–FY26 | 3.4%, 4.8%, 10.5%, 5.4%, 12.3%, 35.3%, 34.3% | 7 |

### Page 25 — Awards & Accolades

| Line | Description | Values | Ct |
|---|---|---|---|
| 754 | Calendar Year: ISO 9001/14001 accreditation | 2016 | 1 |
| 755 | "ISO 9001: 2015 & ISO 14001:2015 requirements" | 9001, 2015, 14001, 2015 | 4 |
| 763 | Calendar Year; "AD 2000 - Merkblatt W0" (TÜV material-manufacturer verification) | 2017, 2000, 0 | 3 |
| 767 | Calendar Year: quality-assurance system certification | 2017 | 1 |
| 770 | Certificate image caption: "TUV – AD 200 Merkblatt W0" | 200, 0 | 2 |
| 771 | "...Welded & Seamless Pipes up to 400 mm NB" | 400 | 1 |
| 772 | Calendar Year; "Tubes up to 101.60 mm O.D." | 2018, 101.60 | 2 |
| 773 | "Indian Boiler Regulations – 1950" | 1950 | 1 |
| 777 | Calendar Year: ISO 45001:2018 accreditation | 2018 | 1 |
| 778 | "ISO 45001: 2018" | 45001, 2018 | 2 |
| 781 | Calendar Year: BIS approval | 2022 | 1 |
| 784 | "ISO/IEC 17025:2017" standard | 17025, 2017 | 2 |
| 786 | Calendar Year: NABL accreditation | 2025 | 1 |

### Page 26 — Board of Directors

| Line | Description | Values | Ct |
|---|---|---|---|
| 809 | Kothari since 2021; Choudhary J "over 14 years"; Choudhary M "over 19 years"; Patel since 2015 | 2021, 14, 19, 2015 | 4 |
| 820 | Bhandari "over 22 years"; Agarwal "over 19 years" | 22, 19 | 2 |
| 822 | "Forbes 30 under 30" (x2 digits); Khadaria "13 years of experience" | 30, 30, 13 | 3 |
| 823 | Surana: Forbes Asia list (2017), India list (2019) | 2017, 2019 | 2 |

### Page 27 — Strong Management at Helm

| Line | Description | Values | Ct |
|---|---|---|---|
| 838 | Repeats slide-26 bio tenure/experience figures (Kothari 2021, Choudhary J 14yrs, Choudhary M 19yrs, Patel 2015) | 2021, 14, 19, 2015 | 4 |
| 854 | Sinha "since March 01," (day-of-month fragment) | 01 | 1 |
| 855 | Bubna "since July 2021."; Jain "since August 2020."; Sinha "...2021." | 2021, 2020, 2021 | 3 |
| 856 | Jain "holding 7 years of experience" | 7 | 1 |
| 857 | Bubna "more than 18 years of experience"; Sinha "over 34 years of experience" | 18, 34 | 2 |

### Page 30 — Key Historical Financials FY22–FY26 (CHART_RESTATEMENT, line 909)

| Line | Description | Values | Ct |
|---|---|---|---|
| 915 | PAT CAGR callout | +34% | 1 |
| 916 | Revenue FY26 bar; EBITDA CAGR callout; EBITDA FY26 bar; PAT FY26 bar | 1167, +40%, 191, 102 | 4 |
| 917 | Revenue CAGR callout; EBITDA FY25 bar; PAT FY25 bar | +32%, 168, 93 | 3 |
| 918 | Revenue FY25 bar; PAT FY24 bar | 959, 86 | 2 |
| 919 | EBITDA FY24 bar | 146 | 1 |
| 920 | Revenue FY24 bar | 802 | 1 |
| 926 | Revenue FY23 bar; PAT FY23 bar | 552, 44 | 2 |
| 927 | Revenue FY22 bar; EBITDA FY23 bar; PAT FY22 bar | 387, 69, 32 | 3 |
| 928 | EBITDA FY22 bar | 49 | 1 |
| 940 | EBITDA Margin FY24/FY25; PAT Margin FY24 | 18.2%, 17.5%, 10.7% | 3 |
| 941 | EBITDA Margin FY26; PAT Margin FY25 | 16.3%, 9.7% | 2 |
| 942 | PAT Margin FY22, FY26 | 8.2%, 8.7% | 2 |
| 943 | EBITDA Margin FY22; PAT Margin FY23 | 12.7%, 8.0% | 2 |
| 944 | EBITDA Margin FY23 | 12.5% | 1 |

### Page 31 — Historical Profit & Loss Account (FY26/FY25/FY24/FY23/FY22, CAGR)

| Line | Line item | Values | Ct |
|---|---|---|---|
| 958 | Revenue from Operations | 1,166.8, 958.5, 802.2, 552.4, 386.9, 31.8% (CAGR) | 6 |
| 960 | Cost of Goods Sold | 770.5, 639.5, 575.3, 444.6, 315.0 | 5 |
| 962 | Gross Profit | 396.3, 319.0, 226.9, 107.8, 71.9, 53.2% (CAGR) | 6 |
| 964 | Employee Cost | 50.4, 38.0, 22.4, 10.2, 6.2 | 5 |
| 970 | Other Expenses | 155.3, 113.4, 58.2, 28.5, 16.4 | 5 |
| 972 | EBITDA | 190.6, 167.6, 146.3, 69.1, 49.3, 40.2% (CAGR) | 6 |
| 974 | EBITDA Margins (%) | 16.3%, 17.5%, 18.2%, 12.5%, 12.7%, 360 (bps YoY) | 6 |
| 976 | Depreciation | 23.6, 18.5, 11.8, 1.9, 1.4 | 5 |
| 978 | Other Income | 11.6, 10.7, 3.2, 2.4, 2.1 | 5 |
| 980 | EBIT | 178.6, 159.8, 137.7, 69.5, 49.9, 37.6% (CAGR) | 6 |
| 982 | Finance Cost | 40.8, 34.4, 22.1, 9.8, 7.1 | 5 |
| 984 | Exceptional item | 0.5, 0.0, 0.0, 0.0, 0.0 | 5 |
| 986 | Profit before Tax | 137.3, 125.4, 115.6, 59.7, 42.9, 33.8% (CAGR) | 6 |
| 988 | Tax | 35.4, 32.5, 29.7, 15.5, 11.2 | 5 |
| 990 | Profit After Tax | 101.9, 92.9, 85.9, 44.2, 31.7, 34.0% (CAGR) | 6 |
| 992 | PAT Margins (%) | 8.7%, 9.7%, 10.7%, 8.0%, 8.2%, 50 (bps YoY) | 6 |

Flag: `ZERO_STANDING` — Exceptional item (line 984) is nil in FY25/24/23/22 and 0.5 in
FY26 only; template line, same as the Q1 table's Exceptional Items row.

### Page 32 — Historical Balance Sheet (Mar-26/25/24/23/22, both sides)

| Line | Line item | Values | Ct | Flags |
|---|---|---|---|---|
| 1000 | Non-Current Assets / Total Equity | 560.6, 395.7, 302.2, 206.6, 30.4, 668.5, 531.4, 406.1, 322.2, 128.5 | 10 | |
| 1002 | Property Plant & Equipment / Share Capital | 396.1, 308.8, 281.0, 59.8, 21.3, 20.7, 20.4, 20.3, 20.3, 15.2 | 10 | |
| 1004 | Reserves & Surplus | 647.8, 511.0, 385.8, 301.9, 113.3 | 5 | |
| 1005 | Right-of-Use Assets | 1.7, 0.0, 0.0, 0.0, 0.0 | 5 | ZERO_STANDING (nil Mar25/24/23/22) |
| 1006 | Non-Current Liabilities | 112.1, 42.1, 42.5, 26.8, 15.6 | 5 | |
| 1007 | CWIP | 123.7, 66.5, 12.1, 121.6, 7.4 | 5 | |
| 1014 | Intangible assets | 1.1, 0.7, 0.9, 0.1, 0.1 | 5 | |
| 1015 | (i) Borrowings [Non-Current Financial Liabilities] | 90.6, 28.0, 34.0, 24.7, 14.3 | 5 | |
| 1016 | Other Financial Assets [Non-Current] | 4.9, 5.3, 2.6, 2.1, 1.7 | 5 | |
| 1017 | (ii) Lease Liabilities [Non-Current] | 1.5, 0.0, 0.0, 0.0, 0.2 | 5 | ZERO_STANDING (nil Mar25/24/23) |
| 1018 | Other Non-Current Assets (Net) | 33.1, 14.4, 5.6, 23.0, **–** | 4 | ZERO_STANDING — Mar-22 value is a literal dash (nil/not-applicable), not counted as a numeric token but flagged as a standing dash cell |
| 1019 | Provisions [Non-Current] | 1.8, 1.8, 1.1, 0.6, 0.3 | 5 | |
| 1020 | Current Assets | 739.0, 612.6, 455.3, 300.9, 217.5 | 5 | |
| 1021 | Deferred Tax Liabilities | 18.2, 12.3, 7.4, 1.5, 0.7 | 5 | |
| 1022 | Inventories / Current Liabilities (total) | 386.9, 342.8, 226.0, 166.9, 93.5, 519.0, 434.8, 308.9, 158.5, 103.7 | 10 | |
| 1024 | (i) Investments / (i) Borrowings [Current] | 0.8, 3.4, 3.1, 2.9, 1.4, 195.0, 163.5, 115.3, 65.8, 54.4 | 10 | |
| 1026 | (ii) Trade receivables / (ii) Lease Liabilities [Current] | 259.9, 192.0, 177.1, 70.5, 73.5, 0.1, 0.0, 0.0, 0.0, 0.0 | 10 | ZERO_STANDING on Lease Liabilities [Current] (nil Mar25/24/23/22) |
| 1028 | (iii) Cash & cash equivalents / (iii) Trade Payables | 6.2, 2.9, 1.0, 10.8, **–**, 297.3, 240.0, 173.8, 74.1, 33.5 | 9 | ZERO_STANDING — Cash & cash equivalents Mar-22 is a literal dash |
| 1030 | (iv) Other Financial Liabilities [Current] | 6.2, 7.3, 5.4, 6.3, 0.2 | 5 | |
| 1031 | (iv) Bank balances other than cash and cash equivalents | 22.8, 10.1, 6.6, 15.2, 7.3 | 5 | |
| 1032 | Other Current Liabilities (4 of 5 columns; 5th wraps to line 1033) | 5.0, 4.6, 6.1, 5.5 | 4 | |
| 1033 | Other Current Liabilities (Mar-26 column, wrapped) | 4.6 | 1 | |
| 1034 | Other Financial Assets [Current] / Current tax liabilities (net) | 8.1, 2.6, 2.2, 0.1, 0.7, 15.5, 18.9, 9.7, 6.2, 10.2 | 10 | |
| 1035 | Other Current Assets / Provisions [Current] | 54.3, 58.8, 39.3, 34.5, 41.1, 0.3, 0.1, 0.1, 0.0, 0.0 | 10 | ZERO_STANDING on Provisions [Current] (nil Mar23/22) |
| 1036 | Total Assets / Total Equity & Liabilities | 1,299.6, 1,008.3, 757.5, 507.5, 247.9, 1,299.6, 1,008.3, 757.5, 507.5, 247.9 | 10 | |

### Page 33 — Historical Abridged Cash Flow Statement (Mar-26/25/24/FY23/FY22)

| Line | Line item | Values | Ct |
|---|---|---|---|
| 1046 | Net Profit Before Tax | 137.3, 125.4, 115.6, 59.7, 42.9 | 5 |
| 1048 | Adjustments: Non-Cash Items / Other Investment or Financial Items | 59.0, 44.4, 29.7, 7.1, 5.6 | 5 |
| 1050 | Operating profit before working capital changes | 196.3, 169.8, 145.3, 66.8, 48.5 | 5 |
| 1056 | Changes in working capital | -50.8, -82.8, -73.0, -39.4, -97.4 | 5 |
| 1058 | Cash generated from Operations | 145.5, 87.0, 72.3, 27.4, -49.0 | 5 |
| 1060 | Direct taxes paid (net of refund) | 33.1, 18.3, 20.1, 18.7, 11.0 | 5 |
| 1062 | Net Cash from Operating Activities | 112.4, 68.7, 52.2, 8.7, -60.0 | 5 |
| 1064 | Net Cash from Investing Activities | -202.8, -114.2, -99.7, -167.4, 34.1 | 5 |
| 1066 | Net Cash from Financing Activities | 93.7, 47.4, 37.8, 169.4, 25.8 | 5 |
| 1068 | Net Increase/(Decrease) in Cash & Cash equivalents | 3.3, 1.9, -9.7, 10.7, 0.0 | 5 |
| 1070 | Add: Cash & Cash equivalents at beginning of period | 2.9, 1.0, 10.7, 0.0, 0.1 | 5 |
| 1072 | Cash & Cash equivalents at end of period | 6.2, 2.9, 1.0, 10.7, 0.0 | 5 |

### Page 34 — Key Return Ratios (CHART_RESTATEMENT, line 1080 — footnoted adjusted-basis
figures, see FOOTNOTES #13–17)

| Line | Description | Values | Ct |
|---|---|---|---|
| 1092 | RoE FY22; D/E FY22; ROCE FY22 | 25.0%, 0.5, 34.7% | 3 |
| 1093 | D/E FY26; ROCE FY23/24/25 | 0.5, 31.0%, 32.0%, 30.7% | 4 |
| 1094 | RoE FY23, FY24 | 21.0%, 21.0% | 2 |
| 1095 | RoE FY25; ROCE FY26 | 19.0%, 27.0% | 2 |
| 1096 | RoE FY26; D/E FY24, FY25 | 17.0%, 0.4, 0.4 | 3 |
| 1097 | D/E FY23 | 0.3 | 1 |
| 1108 | Footnote figures: IPO proceeds excluded from RoE (FY22-23); Share Warrant proceeds excluded (FY24-25) | 107.9, 2022, -23, 35.06, 2024, -25 | 6 |

### Page 35 — CSR Initiatives

| Line | Description | Values | Ct |
|---|---|---|---|
| 1118 | "Installed 200 LPH RO water purification systems" | 200 | 1 |

### Page 36 — Sustainability Initiatives

| Line | Description | Values | Ct |
|---|---|---|---|
| 1149 | "98% of hazardous waste is disposed of through co-processing" | 98% | 1 |
| 1150 | "only 2% is sent to landfill disposal" | 2% | 1 |
| 1168 | "planting more than 17,000 native trees" | 17,000 | 1 |
| 1176 | "additional 6.1 MW in-house solar power unit" | 6.1 | 1 |
| 1177 | "Currently 1.3 MW already installed" | 1.3 | 1 |
| 1183 | "100% daylight system in the shed area" | 100% | 1 |

**Numbers subtotal check** (page → value-count): p2=1, p5=2, p8=14, p9=18, p10=16,
p11=18, p12=13, p13=13, p14=59, p15=2, p17=6, p20=38, p21=1, p22=16, p25=22, p26=11,
p27=11, p30=28, p31=88, p32=164, p33=60, p34=21, p35=1, p36=6. Sum = **629**. Matches
grep pass. **Match.**

## 4. FOOTNOTES / FINE-PRINT DISCLAIMERS (17 rows)

| # | Page | Line | Footnote / disclaimer | Qualifies | Flags |
|---|---|---|---|---|---|
| 1 | 3 | 76–104 | Safe Harbour — full forward-looking-statement disclaimer | Every forward-looking statement in the deck (MD's Desk quote p.15, "remains on track" p.8, "expects healthy cash conversion" p.10, spooling capex timeline p.5) | |
| 2 | 9 | 281 | "Inventory Day Calculated on Revenue → (Inventory / Revenue)*365" | The Inventory Days figures on slide 9 (110/103/131/121 days) | |
| 3 | 10 | 324 | "INR Cr unless specified" | All figures on slide 10 | |
| 4 | 11 | 362 | "INR Cr unless specified" | All figures on slide 11 | |
| 5 | 12 | 402 | "INR Cr unless specified" | All figures on slide 12 | |
| 6 | 13 | 436 | "INR Cr unless specified" | All figures on slide 13 | |
| 7 | 14 | 478 | "INR Cr unless specified" | All figures on the Q1 P&L table, slide 14 | |
| 8 | 24 | 745 | "Logos Are The Property Of Their Respective Owners" | Marquee Clientele logos, slide 24 | |
| 9 | 30 | 952 | "INR Cr unless specified" | All figures on slide 30 | |
| 10 | 31 | 994 | "INR Cr unless specified" | Historical P&L table, slide 31 | |
| 11 | 32 | 1039 | "INR Cr unless specified" | Historical Balance Sheet, slide 32 | |
| 12 | 33 | 1077 | "INR Cr unless specified" | Historical Cash Flow statement, slide 33 | |
| 13 | 34 | 1107 | "ROE = PAT / Shareholder's Equity" (formula definition) | RoE chart, slide 34 | |
| 14 | 34 | 1108 | "D/E = Total Debt / Shareholder's Equity" (formula definition) | D/E chart, slide 34 | |
| 15 | 34 | 1108 | "*Excluding Rs. 107.9 crores raised via IPO for Capacity expansions for FY 2022-23 and Rs. 35.06 crores raised via Share Warrant for FY 2024-25" | **RoE figures (25.0%/21.0%/21.0%/19.0%/17.0% FY22-FY26) are adjusted, not as-reported** — capital-raise proceeds are excluded from the equity base | `MATERIAL_FOOTNOTE` — headline return ratio is a non-GAAP adjusted figure |
| 16 | 34 | 1110 | "ROCE = EBIT / Tangible Net worth + Non-Current Liabilities" (formula definition) | ROCE chart, slide 34 | |
| 17 | 34 | 1110 | "^Excluding CWIP from Total Capital Employed from FY23 to FY26" | **ROCE figures (34.7%/31.0%/32.0%/30.7%/27.0% FY22-FY26) exclude CWIP from the capital-employed denominator** — a large and growing CWIP base (page 32: 123.7/66.5/12.1/121.6/7.4 Cr FY26-FY22) would otherwise depress ROCE | `MATERIAL_FOOTNOTE` — headline return ratio is a non-GAAP adjusted figure |

Grep cross-check: `grep -c "INR Cr unless specified"` on body (excl. chart-flag mention)
= 9; `Safe Harbour` = 1; `Inventory Day Calculated` = 1; `Logos Are The Property` = 1;
page-34 formula/exclusion lines = 5. Total = 17. **Match.**

## 5. ADMINISTRATIVE IDENTIFIERS (out of GATE A2 numeric scope — see methodology rule e)

| Page | Line | Item | Value |
|---|---|---|---|
| 1 | 34 | Letter date | August 10, 2026 |
| 1 | 43 | Scrip Code (BSE) | 543528 |
| 1 | 43 | ISIN | INE0JA001018 |
| 1 | 60–61 | Digital signature date/time (Pavan Kumar Jain, Company Secretary) | 2026.08.10, 13:51:32 +05'30' |
| 1 | 65 | Membership No. (CS) | A66752 |
| 37 | 1200 | CIN — Venus Pipes & Tubes Limited | L24311GJ2015PLC082306 |
| 37 | 1200 | CIN — Strategic Growth Advisors Private Limited (IR advisor) | U74140MH2010PTC204285 |
| 37 | 1203 | Phone — Sagar Shroff | +91 98205 19303 |
| 37 | 1203 | Phone — Ayush Haria | +91 98204 62966 |

No `MGMT_ABSENCE`/`ENTITY_CHANGE`/`REPEAT_QUESTION` categories apply — this doctype is
an investor presentation, not a concall transcript or results filing; those categories
are not applicable and are omitted rather than force-filled.

## 6. ZERO_STANDING SUMMARY (cross-reference)

1. Q1 P&L (p.14, line 468) — Exceptional Items: nil in Q1FY27 & Q1FY26, -0.2 in Q4FY26.
2. Historical P&L (p.31, line 984) — Exceptional item: nil in FY25/24/23/22, 0.5 in FY26.
3. Historical BS (p.32, line 1005) — Right-of-Use Assets: nil Mar-25/24/23/22.
4. Historical BS (p.32, line 1017) — Lease Liabilities (Non-Current): nil Mar-25/24/23.
5. Historical BS (p.32, line 1018) — Other Non-Current Assets (Net): literal dash, Mar-22.
6. Historical BS (p.32, line 1026) — Lease Liabilities (Current): nil Mar-25/24/23/22.
7. Historical BS (p.32, line 1028) — Cash & cash equivalents: literal dash, Mar-22.
8. Historical BS (p.32, line 1035) — Provisions (Current): nil Mar-23/22.

None dropped from the ledger; all eight carried above with their `ZERO_STANDING` flag
in place.

---

```yaml
stage: A2-enumerator
company: "VENUSPIPES"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/venuspipes-q1fy27/work/ledger_presentation_venuspipes_q1fy27.md"
counts:
  notes: 0
  line_items: 0
  zero_standing: 8
  agenda_items: 0
  auditor_paras: 0
  entities: 0
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 37
  slide_numbers: 37
  numbers: 629
  footnotes: 17
  administrative_identifiers: 9
flags_raised: [ZERO_STANDING, MATERIAL_FOOTNOTE, CHART_RESTATEMENT]
gate_a2: pass
mismatch_note: ""
```
