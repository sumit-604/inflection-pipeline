=== A2 COUNT TEST ===
category: slides         grep_count: 31    sweep_count: 31    match: yes
category: slide_numbers  grep_count: 530   sweep_count: 530   match: yes
gate_a2: pass
=== END COUNT TEST ===

Methodology note (slide_numbers count): grep pass = `grep -n -E "^\[page [0-9]+\]"` for slide
boundaries, then a Python regex pass (`(?<![A-Za-z0-9])\d[\d,]*\.?\d*`) over each slide's body
text, EXCLUDING (a) the extraction header block (lines 1-13), (b) `[OCR page N]` metadata caption
lines (extraction-process noise, e.g. "100 extracted chars", "200dpi" - not slide content), (c)
`[CHART, page N, note: ...]` metadata lines (extraction notes, not slide content), (d) the
internal deck footer page-number line (equals physical page N minus 1, pagination artifact, not
data), (e) period/axis-label tokens that are grammatically bound to a letter prefix (FY26, Q1FY27,
CY23 etc. - these are column/category headers, already excluded by construction since the regex
requires the digit not be preceded by a letter). Two hand corrections were applied after the
regex pass and verified by full manual re-read of the source lines:
  - Slide 1 (cover letter boilerplate: dates, pincodes, script code, signature timestamp) - naive
    regex over-fragmented composite values (e.g. splitting a pincode "400 001" or a signature
    timestamp "2026.07.31 17:10:06 +05'30'" into many single-digit-run tokens). Recounted by hand
    to 10 discrete disclosure items (see Slide 1 detail below); grep re-run restricted to the same
    10 item-boundaries confirms 10.
  - Slide 30 (historical balance sheet): the table's period header row ("Mar-26 Mar-25 Mar-24
    Mar-23", printed twice - once for Equity & Liabilities, once for Assets) is not preceded by a
    letter (it follows a hyphen: "Mar-26"), so the regex did not auto-exclude it as it did for
    "FY26"-style headers elsewhere. Manually excluded 8 header tokens (176 = 184 raw - 8).
  - Slide 31: regex fragmented the CIN "L31300MH1992PLC067802" into digit-runs across letter
    breaks (31, 1300, 992, 67802). Recounted as ONE identifier value (CIN), consistent with
    treating an alphanumeric registration ID as a single disclosure unit.
Both the grep pass (post-corrections) and the independent manual slide-by-slide sweep below
total 530. GATE A2: PASS.

No prior-quarter deck ledger exists for RAMRAT (first quarterly run for this ticker). DROPPED_SLIDE
comparison is therefore NOT COMPUTABLE this quarter — noted explicitly per instructions, not
silently skipped. Re-run this check at the next quarter once this ledger exists as the baseline.

---

## SECTION A — SLIDE INVENTORY (31 slides; extract line references from
`extract_presentation_ramrat_q1fy27.txt`)

| Slide | Lines | Title | Content type | OCR'd | Numeric data points | Flags |
|---|---|---|---|---|---|---|
| 1 | 14-56 | Cover letter — Reg. 30 disclosure to BSE/NSE | text (regulatory letter) | no | 10 | SIGNATURE_TIMESTAMP (see detail) |
| 2 | 57-68 | Title slide — "Investor Presentation - Q1 FY27" | photo/text (brand slide) | no | 0 | — |
| 3 | 69-97 | Safe Harbor | text (disclaimer) | no | 0 | — |
| 4 | 98-105 | Financial Highlights (section divider) | photo (background image only) | YES | 0 | — |
| 5 | 106-162 | Q1 FY27 - Financial Snapshot | chart (3 bar-chart panels, quarterly + "H1") | no | 31 | LABEL_AMBIGUITY (see detail) |
| 6 | 163-196 | Q1 FY27 - Revenue Mix | chart (2 donut charts) | no | 12 | — |
| 7 | 197-230 | Consolidated Profit & Loss Statement - Q1 FY27 | table | no | 41 | — |
| 8 | 231-238 | Company Overview (section divider) | photo (background image only) | YES | 0 | — |
| 9 | 239-270 | At a Glance | text/icons | no | 12 | footnote-qualified (see Section C) |
| 10 | 271-313 | The Journey So Far | text (timeline, 13 milestone years + narrative) | no | 27 | — |
| 11 | 314-347 | Diverse Range of Products & Applications (1) | text/photo | no | 0 | — |
| 12 | 348-387 | Diverse Range of Products & Applications (2) | text/photo | no | 0 | — |
| 13 | 388-409 | Strengthening Copper Tubes Portfolio | text/photo | no | 0 | — |
| 14 | 410-431 | Products via Joint Venture & Subsidiary | text/photo | no | 5 | — |
| 15 | 432-465 | Manufacturing Facilities | text/photo (capacity figures) | no | 7 | — |
| 16 | 466-493 | Our Esteemed Board of Directors | photo/text (11 director names/roles) | no | 1 | — |
| 17 | 494-534 | Strong Management Team | photo/text (10 profiles) | no | 4 | — |
| 18 | 535-559 | Testament to Our Quality | text/photo (certifications) | no | 2 | — |
| 19 | 560-567 | JV & Subsidiary Product Portfolio (section divider) | photo (background image only) | YES | 0 | — |
| 20 | 568-603 | BLDC & PMSM Motors via EPAVO Electricals Pvt. Ltd. | text/chart (market-size figures) | no | 32 | — |
| 21 | 604-634 | Wind Turbine Towers via Tefabo Product Pvt. Ltd. | text/chart (market-size figures) | no | 25 | — |
| 22 | 635-642 | Key Growth Drivers (section divider) | photo (background image only) | YES | 0 | — |
| 23 | 643-679 | Competitive Strengths Supporting Growth in Copper Tubes | text | no | 3 | — |
| 24 | 680-707 | Rising Demand for Winding Wires & Strips | text | no | 7 | — |
| 25 | 708-743 | ...Driving Growth in Product Applications | text | no | 19 | — |
| 26 | 744-751 | Historical Performance (section divider) | photo (background image only) | YES | 0 | — |
| 27 | 752-791 | Robust Growth Trajectory - FY24 to FY26 | chart (5 bar-chart panels) | no | 22 | LABEL_AMBIGUITY (see detail) |
| 28 | 792-824 | Financial Indicators | chart (3 bar-chart panels: ROE/ROCE/Net Debt-Equity) | no | 9 | — |
| 29 | 825-850 | Historical Consolidated Profit & Loss Statement | table (21 line items x 4 periods) | no | 84 | see EXCEPTIONAL_ITEMS note below |
| 30 | 851-883 | Historical Consolidated Balance Sheet | table (44 line items x 4 periods) | no | 176 | ZERO_STANDING check: none found (all lines nonzero in >=1 period) |
| 31 | 884-932 | Back page — CIN, IR contacts (company + RTA) | text | no | 1 | — |

Slide count: grep (`[page N]` markers) = 31. Manual sweep (sequential read, slide 1 through
slide 31, no gaps, no repeats) = 31. **Match: yes.**

Numeric data point total: sum of "Numeric data points" column above = 530, reconciling exactly
with the grep-pass total after the two documented hand corrections. **Match: yes.**

---

## SECTION B — NUMERIC DATA POINT DETAIL (every number, by slide)

### Slide 1 — Cover letter (Reg. 30 disclosure), lines 14-56
| # | Value | Description | Line |
|---|---|---|---|
| 1 | July 31, 2026 | Letter date | 15 |
| 2 | 400 001 | BSE Mumbai pincode | 19 |
| 3 | 400 051 | NSE Mumbai pincode | 20 |
| 4 | 522281 | BSE Script Code | 22 |
| 5 | 30 | Regulation 30, SEBI LODR (Sub. line) | 24 |
| 6 | 2015 | SEBI LODR Regulations year | 24 |
| 7 | 30 | Regulation 30 (repeat mention, "Pursuant to...") | 30 |
| 8 | June 30, 2026 | Quarter-end date | 31-32 |
| 9 | 2026.07.31 17:10:06 +05'30' | Digital signature timestamp (Saurabh Gupta, CS) | 45-49 |
| 10 | F13652 | Company Secretary membership number | 53 |

FLAG `SIGNATURE_TIMESTAMP`: signature timestamp 17:10:06 IST on 31-Jul-2026, same calendar date
as the letter. This is a Reg. 30 investor-presentation cover letter, not a Board Outcome letter —
no board meeting start/end time is stated anywhere in this document to check the timestamp
against. Flagged for record only; no board-meeting-timing inconsistency can be assessed from this
doctype alone.

### Slide 2 — Title slide, lines 57-68: 0 numbers.

### Slide 3 — Safe Harbor, lines 69-97: 0 numbers (pure disclaimer text).

### Slide 4 — Financial Highlights divider (OCR'd), lines 98-105: 0 numbers. Extraction note:
"slide under 100 extracted chars; rasterised 200dpi + tesseract; section-divider slide,
background photo only, no data."

### Slide 5 — Q1 FY27 Financial Snapshot, lines 106-162 (31 numbers)
Quarterly panel (Q1 FY26 / Q4 FY26 / Q1 FY27):
| # | Value | Description | Line |
|---|---|---|---|
| 1 | 4.4% | EBITDA margin, Q1 FY26 | 112 |
| 2 | 5.3% | EBITDA margin, Q4 FY26 | 112 |
| 3 | 4.8% | EBITDA margin, Q1 FY27 | 112 |
| 4 | 1.6% | PAT margin, Q1 FY26 | 112 |
| 5 | 2.2% | PAT margin, Q4 FY26 | 112 |
| 6 | 1.9% | PAT margin, Q1 FY27 | 112 |
| 7 | +89% | Revenue YoY growth (Q1FY27 vs Q1FY26) | 116 |
| 8 | +109% | EBITDA YoY growth | 116 |
| 9 | 121% | PAT YoY growth | 116 |
| 10 | 1,752.9 | Revenue, Q4 FY26 | 123 |
| 11 | 1,853.3 | Revenue, Q1 FY27 | 123 |
| 12 | 93.2 | EBITDA, Q4 FY26 | 123 |
| 13 | 89.6 | EBITDA, Q1 FY27 | 123 |
| 14 | 39.2 | PAT, Q4 FY26 | 123-124 |
| 15 | 35.2 | PAT, Q1 FY27 | 123-124 |
| 16 | 982.5 | Revenue, Q1 FY26 | 126 |
| 17 | 42.9 | EBITDA, Q1 FY26 | 126 |
| 18 | 15.9 | PAT, Q1 FY26 | 126 |

Second panel, printed under mixed "H1"/"FY" labels (see flag below):
| # | Value | Description | Line |
|---|---|---|---|
| 19 | 4.3% | EBITDA margin, labelled prior-period column | 135 |
| 20 | 5.1% | EBITDA margin, labelled current-period column | 135 |
| 21 | 1.9% | PAT margin, prior-period column | 135 |
| 22 | 2.1% | PAT margin, current-period column | 135 |
| 23 | +40.8% | Revenue growth, this panel | 138 |
| 24 | +68.7% | EBITDA growth, this panel | 138 |
| 25 | +54.7% | PAT growth, this panel | 138 |
| 26 | 5,176.6 | Revenue, current-period column | 144 |
| 27 | 263.6 | EBITDA, current-period column | 144 |
| 28 | 108.6 | PAT, current-period column | 144 |
| 29 | 3,676.7 | Revenue, prior-period column | 151 |
| 30 | 156.3 | EBITDA, prior-period column | 152 |
| 31 | 70.2 | PAT, prior-period column | 152 |

FLAG `LABEL_AMBIGUITY`: this second panel's row labels in the extracted text mix "H1FY25" (line
146), a bare "H1" (line 153), and plain "FY25"/"FY26" (lines 139, 145, 158). The panel's absolute
values (Revenue 5,176.6 / EBITDA 263.6 / PAT 108.6 for the "current" column; 3,676.7 / 156.3 /
70.2 for "prior") are IDENTICAL to the FULL-YEAR FY26 and FY25 figures shown in the Historical
P&L on Slide 29 (line 828, 836, 847), not half-year actuals. The panel's own construction implies
it should show H1 (6-month) figures parallel to the quarterly panel above it, but the numbers
printed are full-year FY26/FY25, not H1FY26/H1FY25. This is a genuine disclosure/labelling
question for A3/A4: is the second panel mislabelled ("H1" heading over full-year data), or is
there a real H1 comparison intended elsewhere that is simply not shown? Flag for review; not
resolved here (enumeration only).

### Slide 6 — Q1 FY27 Revenue Mix, lines 163-196 (12 numbers)
| # | Value | Description | Line |
|---|---|---|---|
| 1 | 8% | Export mix, Q1 FY26 | 174 |
| 2 | 92% | Domestic mix, Q1 FY26 | 180 |
| 3 | 6% | Export mix, Q1 FY27 | 174 |
| 4 | 94% | Domestic mix, Q1 FY27 | 180 |
| 5 | 84% | Enamelled Wires & Strips mix, Q1 FY26 | 173 |
| 6 | 72% | Enamelled Wires & Strips mix, Q1 FY27 | 175 |
| 7 | 14% | Copper Tubes & Pipes mix, Q1 FY26 | 183 |
| 8 | 26% | Copper Tubes & Pipes mix, Q1 FY27 | 181 |
| 9 | 2% | Others mix, Q1 FY26 | 184 |
| 10 | 1% | Others mix, Q1 FY27 | 184 |
| 11 | 14% | Commentary repeat ("improved... from 14%...") | 189 |
| 12 | 26% | Commentary repeat ("...to 26%") | 189 |

### Slide 7 — Consolidated P&L Statement, Q1 FY27 (table), lines 197-230 (9 line items, 41 values)
| Line item | Q1 FY27 | Q1 FY26 | Y-o-Y | Q4 FY26 | FY26 | Line |
|---|---|---|---|---|---|---|
| Revenue from Operations | 1,853.3 | 982.5 | +88.6% | 1,752.9 | 5,176.6 | 203 |
| Gross Profit | 164.8 | 96.3 | +71.2% | 168.5 | 522.4 | 206 |
| GP % | 8.9% | 9.8% | — (n/a) | 9.6% | 10.1% | 209 |
| Operating EBITDA | 89.6 | 42.9 | +109.0% | 93.2 | 263.6 | 212 |
| EBITDA % | 4.8% | 4.4% | — (n/a) | 5.3% | 5.1% | 215 |
| PBT | 46.1 | 22.4 | +105.8% | 57.4 | 153.0 | 218 |
| PBT % | 2.5% | 2.3% | — (n/a) | 3.3% | 3.0% | 221 |
| Profit for the period | 35.2 | 15.9 | +120.8% | 39.2 | 108.6 | 224 |
| PAT % | 1.9% | 1.6% | — (n/a) | 2.2% | 2.1% | 227 |

Value count: 5+5+4+5+4+5+4+5+4 = 41 (margin rows carry no Y-o-Y column). Matches.

### Slide 8 — Company Overview divider (OCR'd), lines 231-238: 0 numbers.

### Slide 9 — At a Glance, lines 239-270 (12 numbers)
| # | Value | Description | Line |
|---|---|---|---|
| 1 | 3 (decades) | "Over 3 decades of Manufacturing expertise" | 244 |
| 2 | 25% | ROCE* | 245 |
| 3 | 0.016 mm | Enamelled wire range, lower bound | 246 |
| 4 | 5.000 mm | Enamelled wire range, upper bound | 246 |
| 5 | ~76% | Capacity utilisation, Winding Wires & Strips | 251 |
| 6 | ~45% | Capacity utilisation, Copper Tubes & Pipes | 251/256 |
| 7 | 7% | Ecovadis ranking, top 7% worldwide | 262 |
| 8 | 70% | Supplies to Large OEMs, lower bound | 262 |
| 9 | 75% | Supplies to Large OEMs, upper bound | 262 |
| 10 | 5 (years) | Revenue/PAT CAGR period | 263/265 |
| 11 | 28% | Revenue CAGR (5yr) | 263 |
| 12 | 47% | PAT CAGR (5yr) | 265 |

Footnote (line 269): "*The figures are for FY26" — qualifies item #2 (ROCE 25%) only. See
Section C.

### Slide 10 — The Journey So Far, lines 271-313 (27 numbers)
| # | Value | Description | Line |
|---|---|---|---|
| 1-7 | 1992, 1997, 2011, 2018, 2022, 2024, 2026 | Top-row timeline milestone years | 277 |
| 8 | 1st | "1st ISO Certification" (ordinal) | 281 |
| 9 | 3,600 | Ongoing capex: MTPA addition at Silvassa | 281 |
| 10-11 | 1, 1 | "1:1 Bonus" (2018 milestone) | 282 |
| 12 | 2027 | Silvassa expansion commissioning target month | 285 |
| 13 | 1992 | "Incorporation of RRWL... on July 1992" (repeat) | 286 |
| 14 | 60% | "Acquisition of 60% stake in Tefabo" (2024 milestone) | 287-289 |
| 15 | 1995 | "BSE Listing on Feb 1995" | 296 |
| 16 | 2024 | "Rajasthan Investment Promotion Scheme (RIPS-2024)" | 297 |
| 17 | 4% | "Acquired an additional 4% stake in Tefabo" | 299 |
| 18 | 1st | "...effective 1st July 2025" (ordinal) | 299 |
| 19 | 2025 | "...effective 1st July 2025" | 300 |
| 20-21 | 1, 1 | "Bonus equity shares issued (1:1 ratio)" (repeat mention) | 302 |
| 22-27 | 1995, 2005, 2017, 2020, 2023, 2025 | Bottom-row timeline milestone years | 308 |

Cross-check: Tefabo stake 60% (2024, item 14) + additional 4% (2025, item 17) = 64%, consistent
with the 64% ownership stated on Slides 14 and 21. No arithmetic flag.

### Slides 11, 12, 13 — Product/application slides, lines 314-409: 0 numbers each (pure
descriptive text/photo, product categories and applications, no figures).

### Slide 14 — Products via JV & Subsidiary, lines 410-431 (5 numbers)
| # | Value | Description | Line |
|---|---|---|---|
| 1 | 2020 | EPAVO Electricals established | 413 |
| 2 | 2018 | Tefabo Product established | 413 |
| 3-4 | 50, 50 | EPAVO 50:50 JV split with EPACK Durable Ltd | 414 |
| 5 | 64% | Tefabo stake acquired | 414 |

### Slide 15 — Manufacturing Facilities, lines 432-465 (7 numbers)
| # | Value | Description | Line |
|---|---|---|---|
| 1 | 5 | "5 State of the art Manufacturing Plants" (total) | 435 |
| 2 | 3 PLANTS | Current capacity plants, Dadra & Nagar Haveli/Daman & Diu | 438 |
| 3 | 54,000 MTPA | Total installed capacity, those 3 plants | 444 |
| 4 | 1 PLANT | New Expansion — Bhiwadi, Rajasthan | 443 |
| 5 | 24,000 MTPA | Installed capacity, Bhiwadi plant | 454 |
| 6 | 1 PLANT | Baroda, Gujarat | 455 |
| 7 | 12,000 MTPA | Installed capacity, Baroda plant | 461 |

### Slide 16 — Board of Directors, lines 466-493 (1 number)
| # | Value | Description | Line |
|---|---|---|---|
| 1 | 2018 | Padma Shri Awardee (Trade & Industry) — Shri Rameshwarlal Kabra | 481 |

### Slide 17 — Strong Management Team, lines 494-534 (4 numbers)
| # | Value | Description | Line |
|---|---|---|---|
| 1 | 23+ | Iqbal Singh Saggu — years of experience (Finance/CFO) | 503 |
| 2 | 35+ | Vijay Chandak — years of experience (Development) | 511 |
| 3 | 1995 | Satish Kumar Agarwal — "lead public issue in 1995" | 512 |
| 4 | 35 | Sudhir Kasat — years of experience (electrical industry) | 521 |

### Slide 18 — Testament to Our Quality, lines 535-559 (2 numbers)
| # | Value | Description | Line |
|---|---|---|---|
| 1 | 16949 | IATF 16949 certification standard number | 555 |
| 2 | 2016 | IATF 16949:2016 certification year | 555 |

### Slide 19 — JV & Subsidiary Product Portfolio divider (OCR'd), lines 560-567: 0 numbers.

### Slide 20 — BLDC & PMSM Motors via EPAVO, lines 568-603 (32 numbers)
| # | Value | Description | Line |
|---|---|---|---|
| 1-2 | 50, 50 | 50:50 JV with EPACK Durable Ltd | 573 |
| 3 | 30 Lakh | Installed capacity, motors/annum | 573 |
| 4-5 | 27, 28 | PMSM/HVLS power consumption, 27-28W | 573/577 |
| 6 | >90% | Localisation on PMSM HVLS fan motors | 573/578 |
| 7-8 | 75, 85 | Traditional fan power consumption, 75-85W | 577 |
| 9-10 | 15, 45 | BLDC Motors for RAC, 15W-45W range | 584 |
| 11-12 | 22, 25 | Global BLDC/high-efficiency motor market 2025, USD 22-25 Bn | 584 |
| 13 | 2025 | Market-size base year | 584 |
| 14-15 | 38, 45 | Projected market by 2030, USD 38-45 Bn | 584 |
| 16 | 2030 | Projection year | 584 |
| 17-18 | 7, 9 | CAGR range, ~7-9% | 584 |
| 19-20 | 11, 11.5 | FY26 India RAC sales, 11-11.5 million units | 589 |
| 21-22 | 27, 28 | BLDC Kits/Ceiling Fans, 27W-28W (repeat range) | 590 |
| 23 | 5-star | BEE star rating | 590 |
| 24-25 | 22, 23 | BLDC motor demand, 22-23 million units | 592-593 |
| 26 | >90% | HVLS/PMSM localisation (repeat mention) | 596-598 |
| 27 | 15 | PMSM global market 2025, USD 15 Bn | 599 |
| 28 | 2025 | PMSM market base year | 599 |
| 29 | 25 | PMSM projected market by 2032, USD 25 Bn | 599 |
| 30 | 2032 | PMSM projection year | 599 |
| 31-32 | 8, 9 | PMSM CAGR range, ~8-9% | 599 |

### Slide 21 — Wind Turbine Towers via Tefabo, lines 604-634 (25 numbers)
| # | Value | Description | Line |
|---|---|---|---|
| 1 | 64% | Ownership stake | 609 |
| 2 | ~40 | Towers/month installed capacity | 609 |
| 3-4 | 30, 40 | Market share range, 30-40% | 609 |
| 5 | 2 Plants | Bengaluru & Vadodara | 609 |
| 6 | ~40 | Bengaluru capacity, towers/month | 617 |
| 7 | ~40 | Vadodara current capacity, towers/month | 618-619 |
| 8 | ~80 | Vadodara target expanded capacity, towers/month | 618-619 |
| 9-10 | 48, 50 | Global wind turbine tower market by 2030, USD 48-50 Bn | 627 |
| 11 | 2030 | Global market projection year | 628 |
| 12-13 | 31, 32 | Global market base 2025, USD 31-32 Bn | 628 |
| 14 | 2025 | Global market base year | 628 |
| 15 | 8 | Global CAGR ~8% | 628 |
| 16-17 | 2.4, 2.5 | India wind turbine & tower market by 2030, USD 2.4-2.5 Bn | 627 |
| 18-19 | 1.5, 1.6 | India market base 2025, USD 1.5-1.6 Bn | 629 |
| 20 | 2025 | India market base year | 629 |
| 21-22 | 8, 9 | India CAGR range, 8-9% | 629 |
| 23-24 | 53, 55 | India installed wind capacity FY26, 53-55 GW | 627 |
| 25 | 2030 | Second "by 2030" reference (India installed wind capacity outlook) | 628 |

### Slide 22 — Key Growth Drivers divider (OCR'd), lines 635-642: 0 numbers.

### Slide 23 — Competitive Strengths, Copper Tubes, lines 643-679 (3 numbers)
| # | Value | Description | Line |
|---|---|---|---|
| 1 | ~70% | India's copper tube import dependency | 650 |
| 2 | 36,000 MTPA | Total installed capacity (copper tubes) | 657-659 |
| 3 | 200+ | Distribution presence, cities | 672 |

Note: Slide 23's "36,000 MTPA" total installed copper-tube capacity does not match the sum of
Bhiwadi (24,000 MTPA, Slide 15) + Baroda (12,000 MTPA, Slide 15) = 36,000 MTPA exactly — this
reconciles. No flag.

### Slide 24 — Rising Demand for Winding Wires & Strips, lines 680-707 (7 numbers)
| # | Value | Description | Line |
|---|---|---|---|
| 1 | 4.22 | Indian magnet winding wire market, CY23, USD Bn | 693 |
| 2 | 5.25 | Projected market, CY28, USD Bn | 694 |
| 3 | 4.5% | Projected CAGR | 695 |
| 4 | 2 | "2-wheelers" (EV segment) | 695 |
| 5 | 3 | "3-wheelers" (EV segment) | 695 |
| 6 | 4 | "4-wheelers" (EV segment) | 695 |
| 7 | 6 | "6wresearch" — source-citation firm name (digit is part of the firm's brand name, not a data value) | 706 |

### Slide 25 — ...Driving Growth in Product Applications, lines 708-743 (19 numbers)
| # | Value | Description | Line |
|---|---|---|---|
| 1 | 2026 | India Power Transformers market valuation year | 722-723 |
| 2 | 3.25 | India Power Transformers Market, USD Billion, 2026 | 722-723 |
| 3 | 55.3 | Smart meters installed under RDSS, Mn (as of June 2026) | 722 |
| 4 | 2026 | "As of June 2026" (repeat) | 722 |
| 5 | 130 | Electrical/electronics sector market size, USD billion | 723 |
| 6 | 4.82 | Transformer market projection, USD Billion, by 2031 | 724 |
| 7 | 9.4% | Electric motor market CAGR | 722-723 |
| 8 | 2026 | CAGR period start (repeat) | 722-723 |
| 9 | 2034 | CAGR period end | 723 |
| 10 | 72.4 | Total smart meters installed nationwide, Mn | 724 |
| 11 | 25 | Export target, USD billion | 724 |
| 12 | 2031 | Transformer market projection year | 724 |
| 13 | 8.22% | Transformer market CAGR | 725 |
| 14 | 2030 | Export target year | 724 |
| 15 | 500 GW | Non-fossil fuel capacity target | 732-733 |
| 16 | 2030 | Non-fossil fuel target year | 732-733 |
| 17 | 2030 | "largest market for smart electricity meters by 2030" (repeat) | 729-732 |
| 18 | 4.75 | Power transmission investment, Rs. trillion | 734 |
| 19 | 2027 | Power transmission investment expected-by year | 735-736 |

### Slide 26 — Historical Performance divider (OCR'd), lines 744-751: 0 numbers.

### Slide 27 — Robust Growth Trajectory, FY24-FY26, lines 752-791 (22 numbers)
| # | Value | Description | Line |
|---|---|---|---|
| 1 | +73.5% | Revenue growth, FY24-FY26 | 761 |
| 2 | 5,176.6 | Revenue, FY26 | 761 |
| 3 | +121.5% | EBITDA growth | 761 |
| 4 | 263.6 | EBITDA, FY26 | 761 |
| 5 | +105.1% | PBT growth | 761 |
| 6 | 153.0 | PBT, FY26 | 761 |
| 7 | 3,676.7 | Revenue, FY25 | 762 |
| 8 | 97.2 | PBT, FY25 | 762 |
| 9 | 2,983.3 | Revenue, FY24 | 763 |
| 10 | 156.3 | EBITDA, FY25 | 763 |
| 11 | 119.0 | EBITDA, FY24 | 764 |
| 12 | 74.6 | PBT, FY24 | 764 |
| 13 | +98.9% | PAT growth | 778 |
| 14 | 108.6 | PAT, FY26 | 778 |
| 15 | 5.0# | Dividend (Rs/Share), FY26 column (hash-flagged) | 778 |
| 16 | 70.2 | PAT, FY25 | 780 |
| 17 | 54.6 | PAT, FY24 | 781 |
| 18 | 2.5 | Dividend (Rs/Share), FY24 column | 781 |
| 19 | 2.5 | Dividend (Rs/Share), FY25 column | 781 |
| 20 | 2.50 | Footnote: special interim dividend | 789 |
| 21 | 2.50 | Footnote: final dividend | 789 |
| 22 | 23-24 (FY23-24) | Footnote: period the interim+final dividend relates to | 789 |

FLAG `LABEL_AMBIGUITY`: footnote (line 789, item 22) states "Rs. 2.50 Special interim & Rs 2.50
final dividend for FY23-24" (i.e., total Rs. 5.00 relates to FY24), but the "#" hash mark in the
chart body is attached to the value shown under the FY26 dividend column (item 15, "5.0#"), while
the FY24 column shows only "2.5" (item 18) with no hash. Either the hash is misplaced against the
wrong bar, or the FY24 bar itself understates the full-year total implied by its own footnote.
Flag for A3/A4 verification against the statutory dividend history (board/AGM records); not
resolved here.

### Slide 28 — Financial Indicators, lines 792-824 (9 numbers)
| # | Value | Description | Line |
|---|---|---|---|
| 1 | 14.4% | ROE, FY24 | 808 |
| 2 | 15.3% | ROE, FY25 | 807 |
| 3 | 20.9% | ROE, FY26 | 804 |
| 4 | 18.8% | ROCE, FY24 | 807 |
| 5 | 22.4% | ROCE, FY25 | 805 |
| 6 | 25.1% | ROCE, FY26 | 804 |
| 7 | 0.20 | Net Debt/Equity, FY24 | 811 |
| 8 | 0.34 | Net Debt/Equity, FY25 | 807 |
| 9 | 0.46 | Net Debt/Equity, FY26 | 804 |

Footnote (line 822) defines the Net Debt/Equity formula; contains no additional numeric values.

### Slide 29 — Historical Consolidated P&L (table), lines 825-850 (21 line items, 84 values;
FY26 / FY25 / FY24 / FY23 columns)
| Line item | FY26 | FY25 | FY24 | FY23 | Line |
|---|---|---|---|---|---|
| Revenue from Operations | 5,176.6 | 3,676.7 | 2,983.3 | 2,649.6 | 828 |
| Cost of Materials Consumed | 4,821.1 | 3,355.4 | 2,690.1 | 2,455.5 | 829 |
| Purchase of stock-in-trade | 41.2 | 19.4 | 0.2 | 0.0 | 830 |
| Changes in Inventories (FG & WIP) | -208.1 | -33.9 | 22.8 | -51.7 | 831 |
| Gross Profit | 522.4 | 335.9 | 270.1 | 245.8 | 832 |
| GP % | 10.1% | 9.1% | 9.1% | 9.3% | 833 |
| Employee Benefits Expense | 96.5 | 66.9 | 55.5 | 47.6 | 834 |
| Other Expenses | 162.2 | 112.7 | 95.7 | 89.5 | 835 |
| EBITDA | 263.6 | 156.3 | 119.0 | 108.7 | 836 |
| EBITDA % | 5.1% | 4.3% | 4.0% | 4.1% | 837 |
| Other Income | 18.5 | 17.8 | 15.0 | 6.9 | 838 |
| Depreciation & Amortisation | 37.9 | 22.1 | 19.7 | 18.5 | 839 |
| EBIT | 244.2 | 152.0 | 114.3 | 97.2 | 840 |
| Finance Costs | 83.8 | 53.7 | 40.0 | 33.0 | 841 |
| Share of Profit of JV (net of tax) | -3.9 | -1.1 | 0.3 | 0.3 | 842 |
| Profit before exceptional items & tax | 156.5 | 97.2 | 74.6 | 64.4 | 843 |
| Exceptional items | 3.6 | 0.0 | 0.0 | 0.0 | 844 |
| Profit before tax | 153.0 | 97.2 | 74.6 | 64.4 | 845 |
| Total Tax Expense | 44.4 | 27.0 | 20.0 | 17.4 | 846 |
| Profit for the period | 108.6 | 70.2 | 54.6 | 47.0 | 847 |
| PAT % | 2.1% | 1.9% | 1.8% | 1.8% | 848 |

21 rows x 4 = 84. Matches.

Note (not `ZERO_STANDING` — not zero in ALL periods, but flagged as a near-miss pattern worth A3
attention): "Exceptional items" is 0.0 in FY23, FY24 and FY25, and 3.6 only in FY26 — a first
appearance of an exceptional item after three years of nil, with no narrative on the deck
identifying its nature. Flag `EMERGING_LINE_ITEM`.

### Slide 30 — Historical Consolidated Balance Sheet (table), lines 851-883 (44 line items, 176
values; Mar-26 / Mar-25 / Mar-24 / Mar-23 columns)

Equity & Liabilities side (21 rows):
| Line item | Mar-26 | Mar-25 | Mar-24 | Mar-23 | Line |
|---|---|---|---|---|---|
| Equity Share Capital | 46.7 | 22.0 | 22.0 | 22.0 | 854 |
| Other Equity | 532.8 | 461.3 | 404.2 | 289.6 | 855 |
| Non-Controlling Interest | 5.4 | 4.4 | 4.6 | 14.2 | 856 |
| Total Equity | 584.9 | 487.7 | 430.7 | 325.8 | 857 |
| Borrowings (Non-current, i) | 265.3 | 191.0 | 102.4 | 96.4 | 859 |
| Lease liabilities (Non-current, ii) | 18.2 | 0.0 | 11.2 | 0.4 | 860 |
| Other Financial Liabilities (Non-current, iii) | 0.2 | 0.3 | 0.3 | 0.2 | 861 |
| Provisions (Non-current) | 4.5 | 1.8 | 1.5 | 1.2 | 862 |
| Deferred Income | 12.8 | 11.1 | 0.8 | 0.1 | 863 |
| Deferred Tax Liabilities (Net) | 17.6 | 10.5 | 4.4 | 21.1 | 864 |
| Total Non-Current Liabilities | 318.7 | 214.6 | 120.6 | 119.4 | 865 |
| Borrowings (Current, i) | 388.8 | 105.2 | 125.2 | 169.5 | 867 |
| Lease liabilities (Current, ii) | 2.8 | 8.7 | 10.4 | 0.2 | 868 |
| Trade payables — micro & small enterprises (iii-a) | 2.3 | 11.2 | 1.8 | 4.5 | 870-871 |
| Trade payables — other than micro & small (iii-b) | 638.9 | 413.6 | 241.7 | 187.7 | 873-875 |
| Other Financial Liabilities (Current, iv) | 40.2 | 43.7 | 9.5 | 8.0 | 876 |
| Provisions (Current) | 1.2 | 1.2 | 2.0 | 1.5 | 877 |
| Income Tax Liabilities (Net) | 1.0 | 3.8 | 0.3 | 1.7 | 878 |
| Other Current Liabilities | 14.6 | 10.6 | 9.7 | 10.4 | 879 |
| Total Current Liabilities | 1,089.9 | 598.0 | 400.7 | 383.5 | 880 |
| TOTAL EQUITY & LIABILITIES | 1,993.5 | 1,300.4 | 952.0 | 828.7 | 881 |

Assets side (23 rows):
| Line item | Mar-26 | Mar-25 | Mar-24 | Mar-23 | Line |
|---|---|---|---|---|---|
| Property, Plant and Equipment | 565.4 | 351.7 | 171.8 | 143.1 | 854 |
| Capital Work-in-Progress | 33.6 | 113.5 | 28.6 | 3.5 | 855 |
| Goodwill | 24.8 | 24.8 | 0.0 | 1.4 | 856 |
| Intangible Assets | 0.1 | 0.1 | 1.7 | 2.1 | 857 |
| Right-of-Use Assets | 48.9 | 27.8 | 40.6 | 0.6 | 858 |
| Investments in Joint Venture (i) | 15.8 | 19.0 | 5.9 | 5.6 | 860 |
| Other Investments (ii) | 0.0 | 0.0 | 0.0 | 68.9 | 861 |
| Loans, Non-current (iii) | 21.4 | 17.9 | 0.1 | 0.1 | 862 |
| Other Financial Assets, Non-current (iv) | 2.1 | 2.9 | 0.9 | 0.7 | 863 |
| Income Tax Assets (Net) | 6.8 | 1.3 | 7.8 | 1.1 | 864 |
| Other Non-Current Assets | 22.6 | 29.0 | 48.1 | 14.6 | 865 |
| Total Non-Current Assets | 741.6 | 588.0 | 305.7 | 241.7 | 866 |
| Inventories | 486.1 | 233.7 | 195.9 | 187.0 | 868 |
| Investments, Current (i) | 0.3 | 0.0 | 37.4 | 5.0 | 870 |
| Trade Receivables (ii) | 640.6 | 390.1 | 322.7 | 341.4 | 871 |
| Cash and Cash Equivalents (iii) | 7.8 | 1.7 | 1.9 | 8.6 | 873 |
| Bank Balances other than above (iv) | 6.0 | 22.2 | 21.9 | 1.7 | 875 |
| Loans, Current (v) | 0.2 | 0.3 | 0.3 | 0.2 | 876 |
| Other Current Financial Assets (vi) | 5.4 | 4.3 | 6.4 | 0.6 | 877 |
| Assets Held for Sale | 0.3 | 0.2 | 4.5 | 11.1 | 878 |
| Other Current Assets | 105.1 | 60.0 | 55.5 | 31.5 | 879 |
| Total Current Assets | 1,252.0 | 712.4 | 646.4 | 587.0 | 880 |
| TOTAL ASSETS | 1,993.5 | 1,300.4 | 952.0 | 828.7 | 881 |

44 rows x 4 = 176. Matches. `ZERO_STANDING` check performed line-by-line across both sides: no
line item is zero/nil/dash in ALL FOUR periods (every row has at least one non-zero period).
Nearest candidates ("Other Investments" — zero Mar24-Mar26, non-zero 68.9 at Mar23; "Goodwill" —
zero only at Mar24) do not qualify as all-periods-zero. No `ZERO_STANDING` rows to flag this
quarter.

### Slide 31 — Back page, IR contacts, lines 884-932 (1 number)
| # | Value | Description | Line |
|---|---|---|---|
| 1 | L31300MH1992PLC067802 | CIN (Corporate Identification Number) | 886 |

---

## SECTION C — FOOTNOTES AND SOURCE CITATIONS

| # | Slide | Line | Text | Qualifies |
|---|---|---|---|---|
| 1 | 9 | 269 | "*The figures are for FY26" | ROCE 25% (Slide 9, item 2) |
| 2 | 27 | 789 | "# Rs. 2.50 Special interim & Rs 2.50 final dividend for FY23-24." | Dividend chart, FY26 column value "5.0#" (see `LABEL_AMBIGUITY` flag, Slide 27) |
| 3 | 28 | 822 | "* Net Debt/Equity Ratio= (Non-current Borrowings + Non-current Lease Liabilities - Cash & Cash Equivalents (incl. bank balances) / Total Equity" | Net Debt/Equity ratio, all 3 years (Slide 28) |
| 4 | 20 | 602 | Source: Grand View Research, MarketsandMarkets, IMARC Group, IEEMA Journal, GlobeNewswire, ICRA Research Summary, CRISIL Ratings | All market-size/TAM figures on Slide 20 (third-party, not company-reported) |
| 5 | 21 | 633 | Source: Grand View Research, MarketsandMarkets, IMARC Group, Mordor Intelligence, Ministry of New and Renewable Energy (MNRE) | All market-size/TAM figures on Slide 21 |
| 6 | 23 | 678 | Source: IMARC Group, IEEMA Journal, GlobeNewswire, Grand View Research, MarketsandMarkets | Import-dependency and market figures on Slide 23 |
| 7 | 24 | 706 | Source: IMARC Group, CareEdge Report, 6wresearch | Winding wire market-size figures on Slide 24 |
| 8 | 25 | 742 | Source: IMARC Group, globenewswire, expertmarketresearch, www.pib.gov.in, indiamanufacturingreview, researchandmarkets, Ministry of Power, mordorintelligence | All market-size figures on Slide 25 |

Note: items 4-8 are source-attribution lines for third-party market-sizing data (TAM/SAM figures),
not footnotes qualifying a company-reported headline number — flagged separately from items 1-3
(genuine qualifying footnotes) so A3/A4 can distinguish "our number, our caveat" from "external
data, external source."

---

## SECTION D — DROPPED_SLIDE / ENTITY_CHANGE (prior-quarter comparison)

No prior-quarter deck ledger exists for RAMRAT (`Prior-quarter ledger path: none` — first
quarterly-pipeline run for this ticker). Per instructions, this is recorded explicitly rather than
silently skipped:
- `DROPPED_SLIDE`: NOT COMPUTABLE this quarter. No baseline slide list exists to diff against.
  This ledger becomes the baseline for the next quarter's A2 run.
- `ENTITY_CHANGE`: NOT COMPUTABLE this quarter for the same reason. Entities named in this deck
  (for baseline purposes going forward): Global Copper Pvt Ltd (GCPL) — subsidiary being merged
  into RRWL per NCLT approval (Slide 10); Epavo Electricals Pvt. Ltd. — 50:50 JV with EPACK
  Durable Ltd. (Slides 10, 14, 20); Tefabo Product Pvt. Ltd. — 64% stake (Slides 10, 14, 21).

---

## SECTION E — FLAGS RAISED (summary)

- `SIGNATURE_TIMESTAMP` — Slide 1, digital signature timestamp recorded (no board-meeting time
  available in this doctype to cross-check against).
- `LABEL_AMBIGUITY` — Slide 5, second panel mixes "H1"/"FY" labels while showing full-year FY26/
  FY25 values (matches Slide 29's historical P&L exactly); Slide 27, dividend footnote period
  (FY23-24) does not clearly align with the hash-marked chart value (shown under FY26).
- `EMERGING_LINE_ITEM` — Slide 29, "Exceptional items" nil for FY23-FY25, first non-zero (3.6) in
  FY26, with no narrative disclosure of its nature on this deck.
- `ZERO_STANDING` — checked across Slide 29 (P&L) and Slide 30 (Balance Sheet) line items; none
  found (no line is zero/nil/dash in ALL periods presented).
- `DROPPED_SLIDE` / `ENTITY_CHANGE` — NOT COMPUTABLE, no prior-quarter ledger baseline exists.
