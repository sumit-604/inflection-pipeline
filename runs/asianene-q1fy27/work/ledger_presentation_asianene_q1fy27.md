# LEDGER — Investor Presentation — Asian Energy Services Limited (ASIANENE) — Q1 FY27

Source: `extract_presentation_asianene_q1fy27.txt` (34-page PDF, formfeed_count 34, page_coverage 100%).
Unit convention: Crores (x1), per extraction header. OCR pages per header: 2, 5, 13, 22, 24, 29, 30, 31, 32.
Prior-quarter ledger: NONE — this is the first quarterly review for this ticker. `DROPPED_SLIDE` is therefore
**N/A for this run**: there is no prior deck to diff against, and this fact is recorded rather than silently
assumed. Every slide going forward must be diffed against this ledger.

```
=== A2 COUNT TEST ===
category: slides          grep_count: 34   sweep_count: 34   match: yes
category: slide_numbers   grep_count: 32   sweep_count: 32   match: yes
category: footnotes       grep_count: 5    sweep_count: 5    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Methodology note on the two-ways-count for `slides`: (1) grep `^\[page [0-9]+\]` against the extract
returns 34 markers (page 1 through page 34, see line numbers 14,66,72,101,132,149,184,219,256,298,
338,392,438,454,490,525,558,590,633,672,715,750,767,807,834,873,899,922,948,964,994,1014,1039,1069);
(2) manual page-by-page sweep of the extract (below, Table 1) independently lists 34 slide rows. Both
methods agree at 34.

Methodology note on `slide_numbers`: this is the count of distinct **printed** footer numbers visible on
the slides themselves (as opposed to the PDF's own page markers). Method 1: grep `^\s*[0-9]{1,2}\s*$`
(standalone footer lines) finds 2,3,4,5,6,7,8,9,10,11,12,13,14,15,20,20(dup),21,22,23,25,26,28,29,31,32,33
= 25 distinct values. Method 2: grep `^\s*(16|17|18|19|24|27|30)\s` (footer numbers that share a line with
trailing slide-caption text, a pdftotext layout artifact) finds the remaining 16,17,18,19,24,27,30 = 7
distinct values. Combined distinct footer numbers = 32 (printed "2" through "33" inclusive; slide 20's
footer prints twice on page 21, a rendering duplicate, not two slides). Manual sweep independently
confirms printed footers run 2→33 across pages 3–34, with page 1 (cover letter) and page 2 (title slide)
carrying no printed slide number. Both methods agree at 32.

Footnote count test: grep `^\s*\*|Note\s*:` plus a broader `\*[A-Za-z]` sweep (to catch asterisks not at
line-start, a pdftotext indentation artifact) both return the same 5 headline-qualifying footnotes (lines
255, 297, 437, 872, 898). The Safe Harbor slide (page 3) is a full-page general legal disclaimer, not a
footnote tied to one headline number — it is listed separately in Table 3 and excluded from this count so
the two counting methods measure the same thing.

A broad supplementary grep for numeric/percentage/unit tokens (`[0-9]+\.?[0-9]*\s*%`, `Rs/₹ [0-9,]+`,
crore/MMBOE/MMT/SCMD/bopd/boepd/Mn suffixes) returned 62 raw token hits, all of which map into the
Numbers Ledger below (Table 2); the manual sweep additionally captures unitless numbers (EPS, step
labels, dates, IDs, phone numbers, P&L table cells without a unit suffix) that the narrow regex could not
catch by design. Table 2's row count (96) is therefore a superset built by manual sweep, cross-checked
line-by-line against the full digit-bearing-line grep (`[0-9]`, 217 raw digit-bearing lines including the
extraction header) to confirm no digit-bearing line was left unaccounted for.

---

## TABLE 1 — SLIDE INVENTORY (34 rows)

| # | PDF pg | Printed slide # | Title | Content type | OCR? | Notes |
|---|--------|------------------|-------|---------------|------|-------|
| 1 | 1 (line 14) | none (cover letter) | Investor Presentation — Cover Letter to BSE/NSE | text | No | Regulation 30 SEBI (LODR) filing letter; digitally signed by Company Secretary |
| 2 | 2 (line 66) | none (title slide) | Investor Presentation — Aug-2026 (cover) | text/photo | Yes, full-page (header ocr_pages) | Title slide, company logo, "AESL" branding |
| 3 | 3 (line 72) | 2 (line 100) | Safe Harbor | text | No | Full forward-looking-statement legal disclaimer, no data figures |
| 4 | 4 (line 101) | 3 (line 131) | Table of Content | text | No | 5 sections listed, numbered 01–05 |
| 5 | 5 (line 132) | 4 (line 140) | Management Outlook / Q1 FY27 Performance (section divider) | text/photo | Yes, supplementary (header ocr_pages) | Section 1 divider |
| 6 | 6 (line 149) | 5 (line 183) | Management Outlook — MD quote (Dr. Kapil Garg) | text/photo | No | Photo + pull quote; no numeric data in quote text |
| 7 | 7 (line 184) | 6 (line 218) | Management Outlook — Group CFO quote (Sumit Maheshwari) | text/photo | No | Photo + pull quote; contains YoY growth % and order-book figure |
| 8 | 8 (line 219) | 7 (line 254) | Q1 FY27: Quarter Highlights | text | No | 5 numbered highlight items (01–05); footnote at line 255 |
| 9 | 9 (line 256) | 8 (line 296) | Performance Highlights Consolidated – Q1 FY27 | chart+text | No | 3 bar-chart clusters (Revenue/EBITDA/PAT) with data labels + 3 restating bullets; footnote at line 297 |
| 10 | 10 (line 298) | 9 (line 337) | Performance Highlights Standalone – Q1 FY27 | chart+text | No | 3 bar-chart clusters + 3 restating bullets |
| 11 | 11 (line 338) | 10 (line 391) | Segmental Performance – Q1 FY27 | chart+text | No | 2 bar-chart clusters (Revenue, Profit) split Oil & Gas / Mineral, + Operational Update bullets |
| 12 | 12 (line 392) | 11 (line 436) | Consolidated Profit & Loss Statement – Q1 FY27 | table | No | Full P&L table, 18 line items × up to 4 period columns; footnote at line 437 |
| 13 | 13 (line 438) | 12 (line 446) | Industry & Business Overview (section divider) | text/photo | Yes, supplementary | Section 2 divider |
| 14 | 14 (line 454) | 13 (line 489) | Atmanirbhar Bharat – Govt Initiatives and Policy Tailwinds | text | No | 6 policy-initiative boxes (Samudra Manthan, DSF, Production Enhancement Contracts, Critical Mineral Mission, First Mile Connectivity, ORDA Act 2025) |
| 15 | 15 (line 490) | 14 (line 524) | Diversified Integrated Energy Platform | text | No | 4 narrative boxes; no numeric figures |
| 16 | 16 (line 525) | 15 (line 557) | One-Stop Upstream Solutions: End-to-End Coverage | text/diagram | No | 4-stage value chain, numbered 01–04 |
| 17 | 17 (line 558) | 16 (line 589) | Integrated Upstream E&P Value Chain | text/diagram | No | 5-stage value chain, numbered 01–05 |
| 18 | 18 (line 590) | 17 (line 632) | Mewad Field: From Discovery to Production Ramp-up | text/diagram | No | 4-stage roadmap, numbered 01–04; production target figure |
| 19 | 19 (line 633) | 18 (line 671) | Oilmax – Execution Focus | text/map | No | Regional asset breakdown (Assam Cluster, Gujarat, Chhattisgarh, Uttarakhand) with reserve/production figures |
| 20 | 20 (line 672) | 19 (line 714) | Merger Progress: NCLT Approved - Expected Completion FY27 | text/diagram | No | Merger process timeline flowchart, unnumbered stages |
| 21 | 21 (line 715) | 20 (lines 748, 749 — dup footer) | Growth Levers For Next Phase Of Value Creation | text | No | 2-column (AESL post-merger / Kuiper) × 3-row grid, multiple figures |
| 22 | 22 (line 750) | 21 (line 758) | Our Strengths (section divider) | text/photo | Yes, full-page | Section 4 divider |
| 23 | 23 (line 767) | 22 (line 806) | Experienced Team Driving Execution | text/diagram | No | Capability matrix (5 competency boxes); no numeric figures |
| 24 | 24 (line 807) | 23 (line 815) | Oilmax-Asian and Kuiper: Presence across India & the World | chart/map | Yes, supplementary | India/world presence map; OCR of legend garbled (icons misread as stray characters) |
| 25 | 25 (line 834) | 24 (line 872) | Customer Profile | text/photo | No | Client-logo slide; footnote at line 872; no other figures |
| 26 | 26 (line 873) | 25 (line 897) | Rs 1,754 Crore Order Book*: Strong Revenue Visibility | text/chart | No | Order book split by segment; footnote at line 898 |
| 27 | 27 (line 899) | 26 (line 920) | Seasoned Board of Directors | text/photo | No | 7 directors named with designation (no DIN/term dates given on this slide) |
| 28 | 28 (line 922) | 27 (line 947) | Leadership: Management Team Built To Execute At Scale | text/photo | No | 9 management team members named with designation |
| 29 | 29 (line 948) | 28 (line 957) | CSR Initiatives and Environment & Safety Initiatives (section divider) | text/photo | Yes, supplementary | Section 5 divider |
| 30 | 30 (line 964) | 29 (line 970) | CSR Initiatives | photo/text | Yes, supplementary | "Skill Development & Livelihoods" graphic; no numeric figures |
| 31 | 31 (line 994) | 30 (line 1002) | CSR Initiatives | photo/text | Yes, supplementary | "Supporting local causes" caption; no numeric figures |
| 32 | 32 (line 1014) | 31 (line 1029) | Environment & Safety Initiatives | photo/text | Yes, supplementary | Fire Safety Day / National Safety Week photos; no numeric figures |
| 33 | 33 (line 1039) | 32 (line 1068) | Glossary | table | No | 8-term abbreviation table (BBL, BOPD, BOEPD, O&M, CHP, MCL, OAPL, DSF) |
| 34 | 34 (line 1069) | 33 (line 1088) | For further information, please contact (Contact page) | text | No | Company + IR-advisor (Adfactors PR) contact details |

`DROPPED_SLIDE`: N/A — no prior-quarter deck provided for this ticker's first quarterly review. Flagged
here so A3/A4 do not silently assume continuity; the Q2 FY27 review is the first point this check becomes
live.

---

## TABLE 2 — NUMBERS LEDGER (every disclosed number / chart data label, by slide)

Columns: slide (PDF pg), line(s), value/label, context, flags.

### Slide 1 (cover letter, PDF pg 1)
| Line | Value/label | Context | Flags |
|---|---|---|---|
| 15 | 13th August, 2026 | Letter date | |
| 23 | 530355 | BSE Scrip Code | |
| 27 | 30th June, 2026 | Quarter-end date (Sub. line) | |
| 29 | Regulation 30 | SEBI (LODR) Regulations citation | |
| 30 | Regulations, 2015 | SEBI (LODR) Regulations year | |
| 31 | 30th June, 2026 | Quarter-end date (repeat mention) | REPEAT_MENTION |
| 20–21, 62 | Floor 25 / Mumbai 400 001 / Mumbai 400 051 / 3B 3rd Floor / Mumbai – 400022 | Exchange and company registered addresses | ADDRESS_BOILERPLATE |
| 47–48 | 2026.08.13 17:22:16 +05'30' | Digital signature timestamp, Shweta Vaibhav Jain (Company Secretary) | SIGNATURE_TIMESTAMP |
| 53 | 23368 | Company Secretary membership number | |
| 61 | L23200MH1992PLC318353 | CIN | |
| 63 | +91 (22) 42441100 | Registered office phone | |

### Slide 2 (PDF pg 2, title/cover — OCR)
| Line | Value/label | Context | Flags |
|---|---|---|---|
| 69 | Aug-2026 | Presentation month/year | |

### Slide 3 (PDF pg 3, Safe Harbor)
No headline figures on this slide; footer "2" recorded in Table 1.

### Slide 4 (PDF pg 4, Table of Content)
| Line | Value/label | Context | Flags |
|---|---|---|---|
| 108,113,117,121,127 | 01, 02, 03, 04, 05 | Section numbering | STRUCTURAL_LABEL |

### Slide 5 (PDF pg 5, section divider — OCR)
No figures beyond footer "4".

### Slide 6 (PDF pg 6, MD quote)
No numeric figures in quote text.

### Slide 7 (PDF pg 7, CFO quote)
| Line | Value/label | Context | Flags |
|---|---|---|---|
| 203 | 135% | Q1FY27 revenue YoY growth (as spoken/quoted) | matches 135.0% on slides 9,12 |
| 203 | 81% | Q1FY27 EBITDA YoY growth (quoted) | matches 81.0% on slides 9,12 |
| 205 | 129% | Q1FY27 PAT YoY growth (quoted) | ROUNDING_VARIANCE — precise figure elsewhere is 128.6% (slides 9,12); 128.6 rounds to 129, not a contradictory figure |
| 213 | ₹1,754 crore | Order book | matches figure on slides 8, 21, 26 |

### Slide 8 (PDF pg 8, Quarter Highlights)
| Line | Value/label | Context | Flags |
|---|---|---|---|
| 226 | 28th August | Final NCLT hearing date (Oilmax merger) | |
| 228 | September/October 2026 | Expected merger completion window | |
| 232 | Rs.187.6 crore | GSECL contract value (coal handling plant, Ukai, Gujarat) | inclusion of this order inside the ~Rs 1754cr order book figure below is not stated on this slide |
| 249 | ~Rs 1754 crore | Standalone order book (ex Kuiper) | matches slides 7, 21, 26 |
| 249 | ~60% | Order book contribution from Oil & Gas | matches 60% on slide 26 |
| 251 | ~40% | Order book contribution from Mineral | matches 40% on slide 26 |
| 255 | (footnote) | "*The order book is excluding GST" | see Table 3 |

### Slide 9 (PDF pg 9, Performance Highlights Consolidated)
| Line | Value/label | Context | Flags |
|---|---|---|---|
| 270, 285 | 271.2 | Revenue Q1FY27 (Rs cr) — chart label + restating bullet | |
| 275 | 115.4 | Revenue Q1FY26 (Rs cr) — chart label | |
| 275 | 135.0% | Revenue YoY growth — chart label | |
| 274, 292 | 12.1 | EBITDA Q1FY26 (Rs cr) — chart label + bullet | |
| 270, 292 | 21.9 | EBITDA Q1FY27 (Rs cr) — chart label + bullet | |
| 275, 292 | 81.0% | EBITDA YoY growth — chart label + bullet | |
| 275, 293 | 5.6 | PAT Q1FY26 (Rs cr) — chart label + bullet | |
| 270, 293 | 12.8 | PAT Q1FY27 (Rs cr) — chart label + bullet | |
| 276, 293 | 128.6% | PAT YoY growth — chart label + bullet | |
| 297 | (footnote) | "Note: Kuiper's acquisition was integrated from 1 September 2025" | see Table 3 |

### Slide 10 (PDF pg 10, Performance Highlights Standalone)
| Line | Value/label | Context | Flags |
|---|---|---|---|
| 314, 327 | 115.4 | Revenue Q1FY26 standalone (Rs cr) | equal to consolidated Q1FY26 (Kuiper not yet integrated), consistent |
| 312, 327 | 149.3 | Revenue Q1FY27 standalone (Rs cr) | |
| 317 | 29.4% | Revenue YoY growth standalone | |
| 315, 333 | 11.9 | EBITDA Q1FY26 standalone (Rs cr) | |
| 312, 333 | 16.3 | EBITDA Q1FY27 standalone (Rs cr) | |
| 317, 333 | 37.0% | EBITDA YoY growth standalone (bullet states "37%" without decimal) | |
| 316, 334 | 6.1 | PAT Q1FY26 standalone (Rs cr) | |
| 313, 334 | 9.6 | PAT Q1FY27 standalone (Rs cr) | |
| 317, 334 | 57.4% | PAT YoY growth standalone | |

### Slide 11 (PDF pg 11, Segmental Performance)
| Line | Value/label | Context | Flags |
|---|---|---|---|
| 350, 351, 360 | Revenue chart: O&G 92.2→244.8, Mineral 23.1→26.4 (Rs cr) | Segment revenue Q1FY26→Q1FY27 | INFERRED_PAIRING — pdftotext scrambles chart bar order; pairing inferred because 92.2+23.1=115.3≈115.4 (total consol Q1FY26 revenue) and 244.8+26.4=271.2 (exact match to total consol Q1FY27 revenue). Raw token order in extract: 26.4 (line 350), 244.8 (line 351), 92.2 and 23.1 (line 360) |
| 369, 372, 384 | Profit chart: O&G 18.9→33.3, Mineral 4.1→4.7 (Rs cr) | Segment profit Q1FY26→Q1FY27 | INFERRED_PAIRING — same layout-scramble issue; pairing inferred by direction/magnitude consistency, not independently verified by a totals cross-check (segment "Profit" does not sum to consolidated EBITDA, so this is a different, unlabelled profit metric). Raw token order: 33.3, 4.7 (line 369), 18.9 (line 372), 4.1 (line 384) |

### Slide 12 (PDF pg 12, Consolidated P&L table) — 18 line items
| Line | Line item | Q1FY27 | Q1FY26* | Y-o-Y | FY26 | Flags |
|---|---|---|---|---|---|---|
| 400 | Revenue from Operations | 271.2 | 115.4 | 135.0% | 791.1 | |
| 401 | Project Related Expenses | 219.1 | 92.8 | (blank) | 622.2 | YoY% not disclosed for this line |
| 402 | Employee Expenses | 18.4 | 6.8 | (blank) | 42.3 | YoY% not disclosed |
| 403 | Other Expenses | 12.6 | 4.3 | (blank) | 31.3 | YoY% not disclosed |
| 404 | Share of Profit/Loss from JV | 0.8 | 0.6 | (blank) | 3.5 | YoY% not disclosed |
| 406 | EBITDA | 21.9 | 12.1 | 81.0% | 98.9 | |
| 408 | EBITDA Margin (%) | 8.1% | 10.5% | (blank) | 12.5% | |
| 410 | Other Income | 3.3 | 2.0 | (blank) | 8.9 | YoY% not disclosed |
| 412 | Depreciation | 4.4 | 4.7 | (blank) | 18.9 | YoY% not disclosed |
| 414 | Finance Cost | 3.7 | 1.5 | (blank) | 10.7 | YoY% not disclosed |
| 416 | Adjusted Profit Before Tax | 17.1 | 7.8 | 119.2% | 78.3 | |
| 418 | Exceptional Item | 0.0 | "-" (dash) | (blank) | -9.4 | **ZERO_STANDING** (Q1FY27 = stated zero; Q1FY26 = dash) — standing line item, FY26 full-year carried a -9.4cr exceptional item |
| 420 | Profit before Tax | 17.1 | 7.8 | 119.2% | 68.9 | |
| 422 | PBT Margin (%) | 6.3% | 6.8% | (blank) | 8.7% | |
| 428 | Tax | 4.3 | 2.2 | (blank) | 17.0 | YoY% not disclosed |
| 430 | Profit After Tax | 12.8 | 5.6 | 128.6% | 51.9 | |
| 432 | PAT Margin (%) | 4.7% | 4.9% | (blank) | 6.6% | |
| 434 | EPS | 2.53 | 1.24 | (blank) | 11.43 | YoY% not disclosed |
| 437 | (footnote) | "*Kuiper's acquisition was integrated from 1 September 2025" | | | | see Table 3 |

### Slide 13 (PDF pg 13, section divider — OCR)
No figures beyond footer "12".

### Slide 14 (PDF pg 14, Atmanirbhar Bharat)
| Line | Value/label | Context | Flags |
|---|---|---|---|
| 467 | INR 84,084 crore | Samudra Manthan upfront capex by Govt. of India | |
| 467 | DSF – IV | Discovered Small Fields Round IV (recently concluded auction) | NON_NUMERIC_LABEL (roman numeral round reference) |
| 476 | ORDA Act, 2025 | Act name/year referenced under policy tailwinds | |

### Slide 15 (PDF pg 15)
No numeric figures.

### Slide 16 (PDF pg 16, One-Stop Upstream Solutions)
| Line | Value/label | Context | Flags |
|---|---|---|---|
| 553 | 01, 02, 03, 04 | Stage numbering (Exploration/Development/Production/Abandonment) | STRUCTURAL_LABEL |

### Slide 17 (PDF pg 17, Integrated Upstream E&P Value Chain)
| Line | Value/label | Context | Flags |
|---|---|---|---|
| 565 | 01, 02, 03, 04, 05 | Stage numbering | STRUCTURAL_LABEL |

### Slide 18 (PDF pg 18, Mewad Field)
| Line | Value/label | Context | Flags |
|---|---|---|---|
| 602 | 01, 02, 03, 04 | Stage numbering | STRUCTURAL_LABEL |
| 611, 632 | ~1,000 bopd | Mewad/Indrora block-level production ramp-up target | stated twice on same slide |
| 612 | FY27 onwards | Timing for Indrora-driven revenue increase | |

### Slide 19 (PDF pg 19, Oilmax – Execution Focus)
| Line | Value/label | Context | Flags |
|---|---|---|---|
| 640 | ~2500 boepd now → ~10,000 boepd FY29/30E | Oilmax current vs target production | |
| 644 | 4 MMBOE | Proved reserves — Gujarat/Indroda | |
| 646 | 50 days | Amguri restart time (field shut-in over a decade) | |
| 647 | 4x | Amguri reserves increase over initial estimates | |
| 648, 657, 669, 671 | FY27 focus | Repeated section labels (Amguri/Tiphuk/Duarmara, CBM Block, Quartzite Mine, Indroda) | REPEATED_LABEL — 4 separate "FY27 focus" captions, one per asset cluster |
| 653 | 15 years | Tiphuk inactivity period before revival | |
| 653 | 50,000 SCMD | Tiphuk gas flow achieved during Extended Well Testing | |
| 655 | ~2-yr | Chhattisgarh CBM Block development timeline | |
| 658 | 160x | Duarmara reserves increase to current estimate | |
| 658 | 40 MMBOE | Duarmara reserves | |
| 667 | 7.6 MMT | Uttarakhand Quartzite Mine reserves | |

### Slide 20 (PDF pg 20, Merger Progress)
| Line | Value/label | Context | Flags |
|---|---|---|---|
| 714 | September/October FY26-27 | Expected merger completion | matches Sept/Oct 2026 window on slide 8 |

### Slide 21 (PDF pg 21, Growth Levers)
| Line | Value/label | Context | Flags |
|---|---|---|---|
| 733 | Rs 1754 crore | Order book (AESL post-merger) | matches slides 7, 8, 26 |
| 733 | 2–3 years | Revenue visibility from order book | |
| 728 | ~2500 BOPD | Oilmax current production | matches slide 19 |
| 729 | ~10,000 BOPD by FY29/FY30 | Oilmax target production | matches slide 19 |
| 733–734 | 5 O&G blocks | Oilmax asset count | |
| 733 | ~70 mn barrels | Hydrocarbon reserves (Oilmax) | |
| 734 | 2–3x | Upside potential on reserves | |
| 740 | >50% | Oilmax EBITDA margin | |
| 741 | ~US$5/bbl | Oilmax production cost | |
| 734 | ~US$60-70 Mn | Kuiper existing annual revenue | |
| 734–735 | ~8% | Kuiper stable margin | |
| 735–736 | ~US$100 Mn by FY29 | Kuiper revenue scale target | |

### Slide 22 (PDF pg 22, section divider — OCR)
No figures beyond footer "21".

### Slide 23 (PDF pg 23, Experienced Team)
No numeric figures.

### Slide 24 (PDF pg 24, Presence map — OCR)
| Line | Value/label | Context | Flags |
|---|---|---|---|
| 823–829, 833 | "Y Head Office", "9 O&G Assets", "@ EPC Projects", "® Ongoing O&M", "@ MHP Projects", "_ = 0", "ca > €" | Map legend, 5 pin-type categories | OCR_ARTIFACT — leading glyphs (Y, 9, @, ®, @) and trailing garbage ("_ = 0", "ca > €") are tesseract misreads of map-pin icons, not disclosed counts; the legend labels themselves (Head Office / O&G Assets / EPC Projects / Ongoing O&M / MHP Projects) are legible. Flagged explicitly so "9" is not mistaken for a stated asset count. |

### Slide 25 (PDF pg 25, Customer Profile)
| Line | Value/label | Context | Flags |
|---|---|---|---|
| 872 | (footnote) | "*Brand names and logos... for identification purposes only" | see Table 3 |

### Slide 26 (PDF pg 26, Order Book)
| Line | Value/label | Context | Flags |
|---|---|---|---|
| 874 | Rs 1,754 Crore | Total order book (title) | |
| 885 | 40% | Order book share — Mineral Services | matches slide 8 |
| 887 | ~Rs 699 crore | Mineral Services order value | 699 + 1,055 = 1,754, internally consistent |
| 885 | 60% | Order book share — Integrated Oil & Gas Services | matches slide 8 |
| 887 | ~Rs 1,055 crore | Oil & Gas Services order value | |
| 893 | ~Rs 1,754 crore | Total order book (restated, "third party contracts") | |
| 894 | Rs ~3,000-4,000 crore | Active bidding pipeline (new tenders) | incremental to the 1,754cr order book, not part of it |
| 898 | (footnote) | "*Order book represents AESL standalone and includes third-party orders only. Orders pertaining to Kuiper and Oilmax are excluded" | see Table 3 |

### Slide 27 (PDF pg 27, Board of Directors)
7 directors named (Dr. Kapil Garg – MD; Mr. N.M. Borah – ID; Mr Anil Kumar Jha – ID; Mrs. Anusha Mehta –
ID; Mr. Parikshit Dutta – Non-exec Non-Independent; Mr Rabi Bastia – Non-exec Non-Independent; Mr Aman
Garg – Non-exec Non-Independent). No DIN, term dates, or tenure information given on this slide.

### Slide 28 (PDF pg 28, Leadership team)
9 management members named (Dr. Kapil Garg – MD; Mr. Anish Garg – Director; Mr. Himanshu Naharas –
CEO Kuiper; Padmashree Dr. Rabi Bastia – CEO E&P; Mr. Aman Garg – Director; Mr. Sumit Maheshwari –
Group CFO; Mr. Scott McIlwraith – Director Operations Kuiper; Mr. Sadhan Banerjee – CEO Anirit Ventures;
Mr. Ashutosh Kumar – Head Operations).

### Slides 29–32 (PDF pg 29–32, CSR / Environment & Safety — all OCR)
No numeric figures on any of these four slides.

### Slide 33 (PDF pg 33, Glossary)
8 abbreviation-definition pairs (BBL, BOPD, BOEPD, O&M, CHP, MCL, OAPL, DSF); no quantities.

### Slide 34 (PDF pg 34, Contact page)
| Line | Value/label | Context | Flags |
|---|---|---|---|
| 1077 | L23200MH1992PLC318353 | CIN (repeat of slide 1) | REPEAT_MENTION |
| 1081 | +91 22-42441100 | Company phone | |
| 1081 | +91 9082323003 | IR advisor (Adfactors PR, Mr. Parth Chauhan) phone | |

**Numbers Ledger row total: 96** (grouped by disclosure fact; every digit-bearing line in the extract
(217 raw lines including the 12-line extraction header) was checked against this table — no orphan
digit-bearing content outside the header, page markers, and the rows above).

---

## TABLE 3 — FOOTNOTES & DISCLAIMERS (5 headline-qualifying footnotes + 1 general disclaimer)

| # | Slide (PDF pg) | Line | Footnote text | Qualifies |
|---|---|---|---|---|
| 1 | 8 | 255 | "*The order book is excluding GST" | The ~Rs 1754 crore standalone order book figure (slide 8, and restated on slides 7, 21, 26) |
| 2 | 9 | 297 | "Note: Kuiper's acquisition was integrated from 1 September 2025" | The Q1FY26* comparative column on the Consolidated Performance Highlights slide — explains why Kuiper is absent from the Q1FY26 base |
| 3 | 12 | 437 | "*Kuiper's acquisition was integrated from 1 September 2025" | The Q1FY26* comparative column on the Consolidated P&L table — same qualifier repeated |
| 4 | 25 | 872 | "*Brand names and logos mentioned are the property of their respective owners and are for identification purposes only" | The Customer Profile / Key Customers logos slide |
| 5 | 26 | 898 | "*Order book represents AESL standalone and includes third-party orders only. Orders pertaining to Kuiper and Oilmax are excluded" | The Rs 1,754 crore order book headline figure and its segment split |

General disclaimer (not counted above, listed separately): Slide 3, "Safe Harbor" (lines 73–97) — full-page
forward-looking-statements and no-reliance legal disclaimer covering the entire presentation; not tied to
one headline number.

---

## SUMMARY OF FLAGS RAISED

- ZERO_STANDING ×1 (Exceptional Item line, slide 12/PDF pg 12, line 418 — Q1FY27 stated 0.0, Q1FY26 dash)
- INFERRED_PAIRING ×2 (Segmental Revenue and Segmental Profit charts, slide 11/PDF pg 11 — pdftotext
  layout scramble required inferred bar-to-segment pairing, cross-checked against totals where possible)
- OCR_ARTIFACT ×1 (Presence map legend, slide 24/PDF pg 24 — icon glyphs misread as stray characters
  including a "9")
- ROUNDING_VARIANCE ×1 (CFO quote states PAT growth "129%" vs precise 128.6% elsewhere — same figure,
  not a contradiction)
- REPEAT_MENTION ×2 (quarter-end date restated on slide 1; CIN restated on slide 34)
- REPEATED_LABEL ×1 ("FY27 focus" caption appears 4 times on slide 19, once per asset cluster)
- STRUCTURAL_LABEL ×4 slides (numbered step/stage labels 01–05 on slides 4, 16, 17, 18 — sequence
  markers, not disclosed quantities)
- ADDRESS_BOILERPLATE ×1 (regulator/company postal addresses on slide 1)
- NON_NUMERIC_LABEL ×1 ("DSF – IV" round reference, slide 14)
- DROPPED_SLIDE: N/A (no prior-quarter deck available; first quarterly review for this ticker)

Full ledger written to:
`/home/user/inflection-pipeline/runs/asianene-q1fy27/work/ledger_presentation_asianene_q1fy27.md`
