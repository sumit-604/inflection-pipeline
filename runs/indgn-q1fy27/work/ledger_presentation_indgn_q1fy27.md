# LEDGER — Investor Presentation — INDGN Q1 FY27

Source: `work/extract_presentation_indgn_q1fy27.txt` (A1 extract; page_count_pdfinfo 22,
formfeed_count 22, ocr_pages [2,12,15,20], unit_convention Millions, conversion factor
to Cr = x0.1). Line numbers below are the A1 extract's own physical line numbers
(reproducible via `grep -n` on the extract file — confirmed offset-consistent with the
extract's internal per-line numbering throughout).

Cross-reference file used for DECK_ONLY determination: `work/extract_results_indgn_q1fy27.txt`
(Reg 33 results filing extract, same run). Every DECK_ONLY flag below was confirmed by a
negative grep on that file for the relevant term(s) before being marked, in addition to the
manual sweep.

```
=== A2 COUNT TEST ===
category: slides         grep_count: 22   sweep_count: 22   match: yes
category: slide_numbers  grep_count: 22   sweep_count: 22   match: yes
  (grep: `grep -c -E "\[page [0-9]+\]" extract_presentation_indgn_q1fy27.txt` -> 22,
   sequence 1..22 with no gap/dupe on manual read)
supplementary: ocr_pages grep_count: 4    sweep_count: 4    match: yes
  (grep: `grep -c -E "\[OCR page [0-9]+\]"` -> 4; matches header ocr_pages: [2,12,15,20])
gate_a2: pass
=== END COUNT TEST ===
```

---

## TABLE 1 — SLIDE INDEX (22 slides, PDF page = slide)

| Slide | Line | Title / role | Content type | OCR | Flags |
|---|---|---|---|---|---|
| 1 | 15 | Reg 30 cover letter (BSE/NSE intimation) | text, cover | no | COVER_LETTER |
| 2 | 64 | "Investor Presentation Q1'FY27" title slide | title/photo | **yes** | OCR_LOWCONF |
| 3 | 81 | Disclaimer | text | no | DISCLAIMER_TEXT, NO_QUANTIFIED_METRICS |
| 4 | 103 | Quarterly Performance — headline KPI cards | text/KPI | no | DIRECTION_UNCLEAR (PAT, DSO YoY arrows) |
| 5 | 134 | Revenue Re-Acceleration with Resilient Margins | chart x2 | no | CHART_LAYOUT_RECONSTRUCTED |
| 6 | 166 | Two Growth Engines Driving Revenue Expansion | text/chart x2 | no | CHART_LAYOUT_RECONSTRUCTED, CHART_LAYOUT_AMBIGUOUS |
| 7 | 214 | Q1'FY27 Business Highlights | text/KPI grid | no | FOOTNOTE_CAVEAT (headcount def.) |
| 8 | 252 | Management Commentary (CEO + CFO quotes) | text | no | FORWARD_LOOKING_STATEMENT |
| 9 | 278 | "Indegene is a new category" (E-D-G-E framework) | text | no | — |
| 10 | 321 | Strategic Priorities FY27 | text | no | NO_QUANTIFIED_METRICS |
| 11 | 353 | Recognized for Innovation and Excellence (2025-26) | text/logos | no | NO_QUANTIFIED_METRICS |
| 12 | 381 | "Financial Highlights" section divider | title | **yes** | OCR_LOWCONF, NO_QUANTIFIED_METRICS |
| 13 | 390 | Q1'FY27 Consolidated Financials (P&L table) | table | no | ZERO_STANDING (Exceptional items), FOOTNOTE_CAVEAT, DECK_ONLY (ETR%) |
| 14 | 414 | Q1'FY27 Stable Business Mix (3 charts) | chart x3 | no | CHART_LAYOUT_RECONSTRUCTED, DECK_ONLY, FOOTNOTE_CAVEAT |
| 15 | 444 | "Annexure" section divider | title | **yes** | OCR_LOWCONF, NO_QUANTIFIED_METRICS |
| 16 | 452 | "We operate at the intersection of healthcare and technology" | text | no | NO_QUANTIFIED_METRICS |
| 17 | 476 | Large addressable market / TAM | text/figures | no | DECK_ONLY, UNSOURCED_TAM |
| 18 | 522 | Full-Stack Capabilities & GenAI Platforms (client vignettes) | text | no | NO_QUANTIFIED_METRICS |
| 19 | 563 | Dual-Pronged GenAI Strategy (product map) | text | no | NO_QUANTIFIED_METRICS |
| 20 | 610 | "Thank You!" closing | title | **yes** | OCR_LOWCONF, NO_QUANTIFIED_METRICS |
| 21 | 622 | Fact Sheet p.1 — Operational & Financial Metrics, service mix, geography mix | table x3 | no | DECK_ONLY (most rows), FOOTNOTE_CAVEAT |
| 22 | 685 | Fact Sheet p.2 — Industry mix, client data, employee metrics, liquidity metrics | table x4 | no | DECK_ONLY (most rows), FOOTNOTE_CAVEAT x4 |

DROPPED_SLIDE check: no prior-quarter presentation ledger was supplied to this run
(`PRIOR_LEDGER_PATH` not provided) — comparison N/A, noted for A3/A4 to source if a
Q4 FY26 deck ledger becomes available.

---

## TABLE 2 — QUANTIFIED METRICS / CLAIMS LEDGER (per slide)

### Slide 1 — Cover letter (line 15)
| Line | Item | Value |
|---|---|---|
| 19 | Letter date | 30 July 2026 |
| 26 | Scrip Code (BSE) / Trading symbol (NSE) | 544172 / INDGN |
| 62 | CIN | L73100KA1998PLC102040 |
| 58 | Registered phone | +91 80 4674 4567, +91 80 4644 7777 |
| 41 | Digital signature timestamp | 2026.07.30 19:17:12 +05'30' (Srishti Ramesh Kaushik, Company Secretary and Compliance Officer, line 43-44) |

### Slide 2 — Title (OCR, line 64) — LOW CONFIDENCE
| Line | Item | Value |
|---|---|---|
| 66 | Quarter label | Q1'FY27 |
| 72-79 | OCR artifact text ("Siiat POOP Baie", "0y00% CRM") | unreadable / not a disclosure — OCR noise, do not cite as content |

### Slide 3 — Disclaimer (line 81)
No quantified metrics. Line 101: page footer "2" (internal deck page numbering starts here, i.e. offset -1 vs PDF page).

### Slide 4 — Quarterly Performance KPI cards (line 103)
| Line | Metric | Value | YoY | QoQ | Flag |
|---|---|---|---|---|---|
| 117 | Revenue from Operations | INR 10,631 M / USD 112.5 M | — | — | |
| 118-119 | Revenue growth | — | ▲39.7% (INR), ▲26.5% (USD) | ▲6.0% (INR), ▲2.5% (USD) | |
| 124-127 | EBITDA | ₹1,795 M, 16.9% of Revenue | ▲16.9% | ▲8.9% | |
| 124-127 | PAT | ₹1,162 M, 10.9% of Revenue | "0.2% YoY" — no directional arrow shown | ▲45.9% | DIRECTION_UNCLEAR — PAT actually declined YoY (-0.2%, confirmed against slide 13/21); headline card shows unsigned "0.2%" with no down-arrow, unlike every other KPI on this card |
| 124-127 | DSO | 67 Days | "4 days YoY" — no arrow shown | ▲4 days QoQ | DIRECTION_UNCLEAR — DSO improved YoY (71→67 per slide 22) but the "up" glyph convention used elsewhere is absent for this cell |
| 124-127 | RPE | $77.1 K | ▲14.2% | ▲3.2% | |

### Slide 5 — Revenue Re-Acceleration (line 134)
| Line | Metric | Value |
|---|---|---|
| 137-139 | Headline | +39.7% Q1'FY27 Revenue Growth YoY; 16.9% Q1'FY27 EBITDA Margin; 10.9% Q1'FY27 PAT Margin |
| 143-159 | Revenue (₹M) by quarter, reconstructed | Q1'FY26 7,608 / Q2'FY26 8,042 / Q3'FY26 9,421 / Q4'FY26 10,034 / Q1'FY27 10,631 — CHART_LAYOUT_RECONSTRUCTED (raw pdftotext layout interleaves the two side-by-side charts' data labels out of visual order; mapping reconstructed by value-matching against slide 13/21 baselines, which agree exactly) |
| 147-160 | EBITDA & PAT margin (%) by quarter, reconstructed | Q1'FY26: EBITDA 20.2% / PAT 15.3%; Q2'FY26: 17.6% / 12.7%; Q3'FY26: 17.5% / 10.9%; Q4'FY26: 16.4% / 7.9%; Q1'FY27: 16.9% / 10.9% — CHART_LAYOUT_RECONSTRUCTED, cross-validated against slide 13 and slide 21 (exact match on Q1'FY27, Q4'FY26, Q1'FY26 columns) |

### Slide 6 — Two Growth Engines (line 166)
| Line | Metric | Value |
|---|---|---|
| 175-177 | Top-20 revenue | ₹7,080 M (Q1'FY27 TTM), +9.5% QoQ |
| 175-177 | Top-5 revenue | ₹3,231 M (Q1'FY27 TTM), +3.4% QoQ |
| 175-177 | Top-5 customer tier claim | "3 of 5 Top-5 customers now at $25 M+" |
| 176-177 | Active clients⁽¹⁾ | 105 (Q1'FY26: 70; +35 new additions) |
| 176-177 | $1M+ clients | 54 (Q1'FY26: 40; +14 new additions) |
| 176-177 | Active clients added since FY22 | +59 |
| 184-202 | Revenue from Top-5 & Top-20 customers (₹M), by year, reconstructed | Top-20: FY22 14,320 / FY23 19,321 / FY24 21,657 / FY25 22,082 / FY26 24,190 / Q1'FY27 TTM 26,480. Top-5: FY22 9,176 / FY23 11,345 / FY24 11,984 / FY25 11,347 / FY26 12,078 / Q1'FY27 TTM 12,491 — CHART_LAYOUT_RECONSTRUCTED, series-label mapping inferred from bar-height ordering, not independently cross-validated elsewhere in the deck |
| 183-197 | Growing accounts by revenue tier (count of clients), by year | Values present in extract (23, 26, 26, 31, 43, 42 and 2, 3, 4, 4, 7, 9 and other unlabelled series) but tier-to-series assignment cannot be reliably reconstructed from the layout-extracted text alone — **CHART_LAYOUT_AMBIGUOUS / LOW_CONFIDENCE_EXTRACTION**; recommend direct image check before citing tier-level counts in A3/A4 |
| 205 | Caption | "$1M+ clients nearly doubled from 28 in FY22 to 54 in Q1'FY27." — new baseline datum: FY22 $1M+ clients = 28 |
| 208 | Footnote (1) | Active clients definition: "$0.25 M or more over the trailing twelve months rounded off to nearest thousands" |

### Slide 7 — Business Highlights (line 214)
| Line | Metric | Value | YoY comparator |
|---|---|---|---|
| 222-226 | Active client relationships⁽¹⁾ | 105 | Q1'FY26: 70; ▲35 new clients \| 50.0% |
| 229-233 | Clients with $1M+ revenue | 54 | Q1'FY26: 40; ▲14 new addition \| 35% |
| 236-240 | Revenue per employee | $77.1K | Q1'FY26: $67.5K; ▲14.2% YoY |
| 223-226 | Healthcare delivery expertise (share of delivery team with domain skills) | 29.0% | Q1'FY26: 24.8%; ▲420 bps YoY |
| 230-233 | Voluntary attrition (TTM) | 15.7% | Q1'FY26: 16.8%; ▼110 bps improvement |
| 237-240 | Total / Delivery employees⁽²⁾ | 5,826 / 4,983 | Q1'FY26: 5,087 / 4,394; ▲14.5% / 13.4% YoY |
| 245 | Footnote (1) | Active clients definition (repeat of line 208 text) |
| 246 | Footnote (2) | "Includes overseas contract resources on third-party payrolls currently being transitioned to direct employment." — **FOOTNOTE_CAVEAT**: reported headcount (and therefore RPE, since RPE = revenue / headcount) includes third-party-payroll contractors, not just direct employees |

### Slide 8 — Management Commentary (line 252)
| Line | Speaker | Quantified claim |
|---|---|---|
| 255-265 | Manish Gupta, Chairman & CEO (line 270) | "sequential USD revenue growth of 2.5% — strongest sequential growth in a first quarter in four years"; "active client base to more than 100"; "revenue per employee rising to $77K — the highest in our peer group"; "12 customers now generating more than $10 million in annual revenue each" (cross-checked against slide 22 client-data table: $10-25M tier = 9 + >$25M tier = 3 → 12, consistent) |
| 255-262 | Suhas Prabhu, CFO (line 271) | "39.7% YoY revenue growth in INR terms and 26.5% in USD"; "expanded our active client base by 14 sequentially to 105"; qualitative: EBITDA and PAT margins "expanding sequentially"; **FORWARD_LOOKING_STATEMENT**: "we expect operating leverage to improve further and profitability to strengthen in the second half of the year" (no number attached — directional guidance only) |

### Slide 9 — "Indegene is a new category" / E-D-G-E framework (line 278)
| Line | Metric | Value |
|---|---|---|
| 283-286 | Revenue / employee (repeat) | $77.1K — "highest in industry" |
| 292-293 | Years of life-sciences experience | 27+ years |
| 292-293 | Employees from healthcare background | 29%+ |
| 300-304 | Years delivering AI | 10+ years |
| 312-315 | Revenue outcome-aligned | ~60% |

### Slide 10 — Strategic Priorities FY27 (line 321)
No quantified metrics — NO_QUANTIFIED_METRICS. Qualitative initiative names only (Tectonic, Agentic AOR, Generative Engine Optimization (GEO), One-Click Submission, Medico-Legal Review Platform, Medical Writing Platform, Content Super App, Transform AI).

### Slide 11 — Recognized for Innovation and Excellence 2025-26 (line 353)
No quantified business metrics — NO_QUANTIFIED_METRICS. Award-cycle years (2025-26, 2026) and an ESG rating "Leader Rating (80/100)" (line 372, ESG score, not a financial/operating KPI) and "Silver rating (Top 15%)" sustainability rating (line 372).

### Slide 12 — "Financial Highlights" divider (OCR, line 381) — LOW CONFIDENCE
No metrics; section title only, OCR garbled.

### Slide 13 — Q1'FY27 Consolidated Financials (line 390), Amount in ₹M, cols: Q1FY27 / Q4FY26 / Q1FY26 / QoQ% / YoY%
| Line | Line item | Q1 FY27 | Q4 FY26 | Q1 FY26 | QoQ% | YoY% | Flag |
|---|---|---|---|---|---|---|---|
| 395 | Revenue from Operations | 10,631 | 10,034 | 7,608 | 6.0% | 39.7% | |
| 396 | Employee Benefit Expenses | 6,591 | 6,324 | 4,815 | 4.2% | 36.9% | |
| 397 | Other Expenses | 2,298 | 2,074 | 1,240 | 10.8% | 85.4% | |
| 398 | Other Income/(loss) | 52 | 13 | (17) | 312.6% | -412.7% | |
| 399-400 | EBITDA (%age) | 1,795 (16.9%) | 1,648 (16.4%) | 1,536 (20.2%) | 8.9% (0.5 pts) | 16.9% (-3.3 pts) | |
| 401 | Interest Income | 237 | 95 | 238 | 148.9% | -0.3% | |
| 402 | Finance cost | 64 | 72 | 37 | -11.0% | 72.2% | |
| 403 | Depreciation & Amortization | 441 | 418 | 216 | 5.7% | 104.0% | |
| 404 | Exceptional items(1) | **-** | 203 | **-** | -100.0% | 0.0% | **ZERO_STANDING** — dash in Q1FY27 and Q1FY26 columns, template line only populated in Q4FY26; cross-checked against filing (extract_results lines 227-229, 397-414: the TCPA class-action settlement provision, ₹203M booked in Q4FY26 and confirmed nil incremental provision expected as of 30 June 2026) — line item is real (litigation-driven) and must stay on the ledger as a standing line even at nil |
| 405 | Profit before taxes | 1,527 | 1,051 | 1,521 | 45.3% | 0.4% | |
| 406 | Taxes(2) | 365 | 255 | 357 | 43.4% | 2.3% | |
| 407-408 | Profit after taxes (%age) | 1,162 (10.9%) | 797 (7.9%) | 1,164 (15.3%) | 45.9% (3.0 pts) | -0.2% (-4.4 pts) | |
| 410 | Footnote (1) | "One-time provision towards the estimated cost of settlement of lawsuit alleging breach of Telephone Consumer Protection Act." | | | | | FOOTNOTE_CAVEAT — litigation; present in filing, not deck-only |
| 412 | Footnote (2) | "Increased tax cost estimated basis Effective Tax Rate (ETR) of 23.9% for Q1'FY27 and 24.2% for Q4'FY26 respectively." | | | | | **DECK_ONLY** — explicit ETR% not found anywhere in `extract_results_indgn_q1fy27.txt` (grep for "effective tax rate"/"ETR" = 0 hits); filing discloses tax amounts only, not the rate |

### Slide 14 — Q1'FY27 Stable Business Mix (line 414), three charts
| Line | Chart | Q1'FY26 | Q4'FY26 | Q1'FY27 | Flag |
|---|---|---|---|---|---|
| 420-435 | Revenue from Service offering ($M), total | 88.9 | 109.7 | 112.5 | |
| 420-435 | — Enterprise Medical Solutions (%) | 28.0% | 25.3% | 25.7% | CHART_LAYOUT_RECONSTRUCTED (cross-validated vs. slide 21, exact match) |
| 420-435 | — Enterprise Commercial Solutions (%) | 68.5% | 71.7% | 70.6% | CHART_LAYOUT_RECONSTRUCTED (cross-validated) |
| 420-435 | — Others (%) | 3.5% | 3.0% | 3.7% | CHART_LAYOUT_RECONSTRUCTED (cross-validated) |
| 421-434 | Revenue by Customer Industry (%) — Biopharma / Medical Devices / Emerging Biotech / Others | 94.1/2.5/2.3/1.1* | 89.9/3.9/4.6/1.6* | 91.6/3.1/3.3/2.0 | Q1'FY27 values cross-validated vs slide 22/17; prior-quarter columns (*) inferred from slide 22, not separately labelled on slide 14 itself |
| 425-437 | Revenue by Customer Geography (%) — North America / Europe / India / RoW | n/a on this slide | n/a on this slide | 75.1 / 22.2 / 0.5 / 2.2 | only current-quarter split shown on slide 14; historical split on slide 21 |
| 442 | Footnote (*) | "Revenue from Agencies are mapped to the end consumer for the calculation of Industry mix" | | | | FOOTNOTE_CAVEAT, methodology; **DECK_ONLY** (not in filing) |

DECK_ONLY (whole slide): none of the service-offering / industry / geography revenue mix
percentages on this slide appear in the results filing extract (filing's own segment note,
lines 330-350, discloses only the 2-segment ₹ absolute split — Enterprise Medical Solutions
₹2,736 / Enterprise Commercial Solutions ₹7,502 for the quarter — a different unit and
basis than the deck's 3-way %-of-revenue split incl. "Others"; the two do not sum to the
same total and the reconciliation is left to A3/A4).

### Slide 15 — "Annexure" divider (OCR, line 444) — LOW CONFIDENCE
No metrics.

### Slide 16 — Healthcare/technology intersection framework (line 452)
No quantified metrics — NO_QUANTIFIED_METRICS. Qualitative bullets only (healthcare market understanding, regulatory navigation, digital-first approach, GenAI tools).

### Slide 17 — Large addressable market / TAM (line 476)
| Line | Metric | Value | Flag |
|---|---|---|---|
| 491 | Marketing and Sales spend | $55 B | |
| 498 | Regulatory and Medical Affairs spend | $24 B | |
| 501 | Pharmacovigilance spend | $21 B | |
| 506 | Drug Discovery and Clinical Trial spend | $36 B | |
| 511 | Mfg, Supply Chain and Distribution spend | $21 B | |
| 495 | "Our Market Opportunity" (total addressable) | $135 B+ | note: sum of the five verticals above (55+24+21+36+21=157) does not equal $135B+ headline; overlap/subset methodology not disclosed on the slide — worth an A3/A4 question |
| 486 | Outsourcing operations CAGR | ~9-14% (2022-2026) | no source cited on slide |
| 492/502/514 | Biopharma / Medical Devices / Emerging Biotech revenue contribution (repeat) | 91.6% / 3.1% / 3.3% | cross-ref footnote 517-518 |
| 517-518 | Footnote (1) | "Indicates revenue contribution by customer industry for Q1'FY27. Remaining 2.0% from other industry." | |

Whole-slide flag: **DECK_ONLY, UNSOURCED_TAM** — no TAM/market-sizing figures of any kind
appear in the results filing; the $B figures and the 9-14% CAGR carry no cited external
source (e.g., no "Source: [research firm], [year]" attribution visible in the extracted
text) — treat as management estimate, not third-party-verified, until confirmed.

### Slide 18 — Full-Stack Capabilities & GenAI Platforms (line 522)
No quantified metrics — NO_QUANTIFIED_METRICS. Four client vignettes (Top 10 Pharma
Company, Large Medical Devices Client, Mid-Sized Biotech Player, Mid-Sized Pharma
Customer) described qualitatively only; no revenue, deal size, or contract-value figures
given for any of the four.

### Slide 19 — Dual-Pronged GenAI Strategy (line 563)
No quantified metrics — NO_QUANTIFIED_METRICS. Product/platform map only (NCCA, MLR,
CORTEX, NCCI, NAEM, Content Super App, Medical Writing Platform).

### Slide 20 — "Thank You!" (OCR, line 610) — LOW CONFIDENCE
No metrics; closing slide + website URL.

### Slide 21 — Fact Sheet p.1 (line 622), (in INR Mn unless noted), cols: Jun-30-2026 / Mar-31-2026 / Jun-30-2025, Growth YoY/QoQ
**Operational & Financial Metrics** (lines 637-654):
| Line | # | Particulars | Q1FY27 | Q4FY26 | Q1FY26 | YoY | QoQ | Flag |
|---|---|---|---|---|---|---|---|---|
| 637 | 1 | Active clients(1) (No.) | 105 | 91 | 70 | 50.0% | 15.4% | DECK_ONLY |
| 638 | 2 | Revenue from operations | 10,631 | 10,034 | 7,608 | 39.7% | 6.0% | in filing |
| 639 | 3 | Revenue from operations ($Mn) | 112.5 | 109.7 | 88.9 | 26.5% | 2.5% | USD conv., DECK_ONLY as $ |
| 640 | 4 | YoY revenue growth(2) (%) | 39.7% | 32.8% | 12.5% | — | — | derived metric |
| 642 | 5 | EBITDA(3) | 1,795 | 1,648 | 1,536 | 16.9% | 8.9% | in filing |
| 644 | 6 | EBITDA margin (%) | 16.9% | 16.4% | 20.2% | — | — | derived |
| 645 | 7 | Profit after tax | 1,162 | 797 | 1,164 | -0.2% | 45.9% | in filing |
| 646 | 8 | Profit margin (%) | 10.9% | 7.9% | 15.3% | — | — | derived |
| 647 | 9 | RPE ($k) | 77.1 | 74.7 | 67.5 | — | — | DECK_ONLY |
| 650 | | Footnote (1) | Active clients definition (3rd instance in deck) | | | | | |
| 652 | | Footnote (2) | "Based on INR revenue" | | | | | |
| 653-654 | | Footnote (3) | EBITDA definition: "profit/(loss) for the period before income tax expense, finance costs, depreciation and amortization expense, interest income and any exceptional items" — note EBITDA here explicitly EXCLUDES interest income (i.e. not a standard "earnings before interest" in the usual two-way sense; interest income is carved out on top of interest expense) | | | | | FOOTNOTE_CAVEAT — definitional, worth an A3 check against filing's EBITDA reconciliation if any |

**Revenue by service offering (%)** (lines 663-666): Enterprise Medical Solutions
25.7/25.3/28.0 (YoY 28.4%, QoQ 7.9%); Enterprise Commercial Solutions 70.6/71.7/68.5
(YoY 44.0%, QoQ 4.3%); Others 3.7/3.0/3.5 (YoY 48.1%, QoQ 29.3%); Total 100.0/100.0/100.0.
DECK_ONLY (%-basis; filing has only the 2-segment ₹-absolute basis, see slide 14 note).

**Revenue by customer geography (%)** (lines 674-678): North America 75.1/74.1/70.2
(YoY 49.6%, QoQ 7.4%); Europe 22.2/23.2/27.1 (YoY 14.3%, QoQ 1.2%); India 0.5/0.4/0.3
(YoY 122.0%, QoQ 48.5%); ROW 2.2/2.3/2.4 (YoY 28.5%, QoQ 0.1%); Total 100.0/100.0/100.0.
DECK_ONLY — no geography split in filing extract.

### Slide 22 — Fact Sheet p.2 (line 685), cols: Jun-30-2026 / Mar-31-2026 / Jun-30-2025
**Revenue by customer industry (%)** (lines 695-699): Biopharma 91.6/89.9/94.1
(YoY 36.0%, QoQ 7.9%); Medical Devices 3.1/3.9/2.5 (YoY 74.9%, QoQ -15.2%); Emerging
Biotech 3.3/4.6/2.3 (YoY 99.0%, QoQ -23.8%); Others 2.0/1.6/1.1 (YoY 160.5%, QoQ 31.9%);
Total 100.0/100.0/100.0. DECK_ONLY.

**Client data** (lines 706-715):
| Line | Particulars | Q1FY27 | Q4FY26 | Q1FY26 | Flag |
|---|---|---|---|---|---|
| 707 | Clients >$25M | 3 | 3 | 2 | DECK_ONLY |
| 708 | Clients $10-25M | 9 | 7 | 7 | DECK_ONLY |
| 709 | Clients $1-10M | 42 | 43 | 31 | DECK_ONLY |
| 711 | Top client concentration | 9.0% | 9.3% | 12.4% | DECK_ONLY |
| 712 | Top 5 clients concentration | 30.4% | 31.2% | 37.9% | DECK_ONLY |
| 713 | Top 10 clients concentration | 45.7% | 47.3% | 56.1% | DECK_ONLY |
| 714 | Top 20 clients concentration | 66.6% | 68.6% | 76.2% | DECK_ONLY |
| 715 | Footnote (*) | "TTM (Trailing twelve months) revenues" | | | |

**Employee metrics** (lines 722-732):
| Line | Particulars | Q1FY27 | Q4FY26 | Q1FY26 | Flag |
|---|---|---|---|---|---|
| 722 | Total employees(1) | 5,826 | 5,666 | 5,087 | DECK_ONLY |
| 723 | — Delivery | 4,983 | 4,904 | 4,394 | DECK_ONLY |
| 724 | — Sales & Support | 843 | 762 | 693 | DECK_ONLY |
| 725 | Offshore Mix | 82.1% | 82.6% | 83.6% | DECK_ONLY |
| 726 | Onsite Mix | 17.9% | 17.4% | 16.4% | DECK_ONLY |
| 728 | Healthcare-related educational background(2) | 29.0% | 27.3% | 24.8% | DECK_ONLY |
| 729 | Voluntary Attrition % (LTM) | 15.7% | 15.8% | 16.8% | DECK_ONLY |
| 730 | % of Women Employees | 46.9% | 46.8% | 45.9% | DECK_ONLY |
| 731 | Footnote (1) | "Includes overseas contract resources on third-party payrolls currently being transitioned to direct employment." (repeat of slide 7 footnote 2) | | | FOOTNOTE_CAVEAT |
| 732 | Footnote (2) | "Based on Delivery employees." | | | |

**Liquidity metrics** (lines 740-744):
| Line | Particulars | Q1FY27 | Q4FY26 | Q1FY26 | Flag |
|---|---|---|---|---|---|
| 740 | Net DSO (Days)(1) | 67 | 63 | 71 | DECK_ONLY |
| 742 | Cash and Cash Equivalents(2) (INR Mn) | 14,602 | 15,385 | 17,280 | DECK_ONLY |
| 743 | Footnote (1) | "Billed + Unbilled – Unearned" (DSO definition) | | | FOOTNOTE_CAVEAT — non-standard DSO formula, includes unbilled revenue as a receivable-equivalent |
| 744 | Footnote (2) | "Includes Cash and Cash Equivalents, Current Investments, Bank balances and Non-Current Bank Deposits" | | | FOOTNOTE_CAVEAT — broadened "liquidity" definition, not a standard cash-and-equivalents line; not in filing (which has no balance sheet section at all in a Reg 33 quarterly filing) |

---

## TABLE 3 — FOOTNOTES / DEFINITIONAL CAVEATS (manual sweep, 15 total)

| # | Slide | Line | Text (verbatim or near-verbatim) |
|---|---|---|---|
| 1 | 6 | 208 | "1. Active clients with revenue of $0.25 M or more over the trailing twelve months rounded off to nearest thousands." |
| 2 | 7 | 245 | Same active-clients definition (repeat) |
| 3 | 7 | 246 | "2. Includes overseas contract resources on third-party payrolls currently being transitioned to direct employment." |
| 4 | 13 | 410 | "(1) One-time provision towards the estimated cost of settlement of lawsuit alleging breach of Telephone Consumer Protection Act." |
| 5 | 13 | 412 | "(2) Increased tax cost estimated basis Effective Tax Rate (ETR) of 23.9% for Q1'FY27 and 24.2% for Q4'FY26 respectively." |
| 6 | 14 | 442 | "* Revenue from Agencies are mapped to the end consumer for the calculation of Industry mix" |
| 7 | 17 | 517-518 | "(1) Indicates revenue contribution by customer industry for Q1'FY27. Remaining 2.0% from other industry." |
| 8 | 21 | 650-651 | "(1) Active clients are clients from whom the Company have earned $0.25 million or more in revenues for the last twelve months preceding the relevant date." (3rd instance, slightly reworded) |
| 9 | 21 | 652 | "(2) Based on INR revenue" |
| 10 | 21 | 653-654 | "(3) Earnings before interest, taxes, depreciation and amortization ("EBITDA") represents profit/(loss) for the period before income tax expense, finance costs, depreciation and amortization expense, interest income and any exceptional items." |
| 11 | 22 | 715 | "* TTM (Trailing twelve months) revenues" |
| 12 | 22 | 731 | "(1) Includes overseas contract resources on third-party payrolls currently being transitioned to direct employment." (2nd instance) |
| 13 | 22 | 732 | "(2) Based on Delivery employees." |
| 14 | 22 | 743 | "(1) Billed + Unbilled – Unearned" |
| 15 | 22 | 744 | "(2) Includes Cash and Cash Equivalents, Current Investments, Bank balances and Non-Current Bank Deposits" |

Grep reconciliation for this table: a single regex cannot cleanly isolate footnote-definition
lines from the Fact Sheet's numbered row labels ("1. Active clients...", "2. Revenue from
operations..." on slide 21, lines 637-647, which are table row numbers, not footnotes) without
over- or under-matching depending on the exact whitespace pattern pdftotext produced (mixed
tab/space runs, inconsistent "N." vs "N. " vs "(N)" formatting across slides). The manual sweep
above (15 items) is the authoritative count for this sub-category; footnotes are not a formal
GATE A2 category for the `presentation` doctype (only `slides` is gated per the A2 spec's count
fields), so this is reported for completeness rather than as a pass/fail gate.

---

## TABLE 4 — ZERO / DASH-VALUED STANDING ITEMS

| Slide | Line | Item | Values | Flag |
|---|---|---|---|---|
| 13 | 404 | Exceptional items(1) | Q1FY27: **-** / Q4FY26: 203 / Q1FY26: **-** | ZERO_STANDING — line item present as a standing row because the underlying event (TCPA class-action settlement provision) is real and ongoing (per filing note, settlement agreement execution still pending as of 30 June 2026); dash in the current and YoY-comparator columns must not be read as "no item," it is "no incremental charge this quarter" |

No other dash/nil/zero values found in any table on the deck (all other line items in Tables
1-22 carry non-zero, non-dash values in every period shown).

---

## TABLE 5 — DECK-ONLY DISCLOSURES (not found in results filing extract)

Cross-checked against `extract_results_indgn_q1fy27.txt` (654 lines; contains P&L, notes,
segment note, Board Outcome-style signature block — **no balance sheet / liquidity section**,
consistent with a standard Reg 33 quarterly-only filing).

| Category | Slides | Confirmed absent from filing |
|---|---|---|
| Active clients count & definition | 6, 7, 21 | yes (0 hits for "active client") |
| $1M+ / $10-25M / >$25M client tiers, client concentration % | 6, 7, 22 | yes |
| Revenue per employee (RPE) | 4, 7, 9, 21 | yes |
| Voluntary attrition % | 7, 22 | yes |
| Employee headcount detail (Delivery/Sales&Support split, Offshore/Onsite mix, % women, healthcare-education %) | 7, 22 | yes |
| DSO (days) and its "Billed+Unbilled-Unearned" definition | 4, 22 | yes |
| Cash and Cash Equivalents (broadened liquidity definition) | 22 | yes — no balance sheet in filing at all |
| TAM / addressable market figures ($55B/$24B/$21B/$36B/$21B/$135B+, CAGR 9-14%) | 17 | yes |
| Effective Tax Rate % (23.9% / 24.2%) | 13 | yes — filing gives tax amounts (₹365M/₹255M/₹357M) but not the rate |
| Revenue mix by service offering (%-of-revenue basis), by geography, by industry | 14, 17, 21, 22 | yes — filing's own segment note (lines 330-350) discloses only a 2-segment ₹-absolute split that does not reconcile 1:1 to the deck's 3-way %-of-revenue basis (see slide 14 note above) |

Not deck-only (also in filing, values agree): Revenue from Operations, EBITDA (₹ and %),
PAT (₹ and %), Employee Benefit Expenses, Other Expenses, Other Income/(loss), Interest
Income, Finance cost, Depreciation & Amortization, Exceptional items (TCPA provision),
Profit before taxes, Taxes — all slide 13/21 P&L lines.

---

## TABLE 6 — FLAGS SUMMARY

| Flag | Count | Slides |
|---|---|---|
| OCR_LOWCONF | 4 | 2, 12, 15, 20 |
| NO_QUANTIFIED_METRICS | 9 | 3, 10, 11, 12, 15, 16, 18, 19, 20 |
| CHART_LAYOUT_RECONSTRUCTED | 3 | 5, 6 (Top-5/20 chart), 14 |
| CHART_LAYOUT_AMBIGUOUS / LOW_CONFIDENCE_EXTRACTION | 1 | 6 (Growing accounts by revenue tier chart) |
| ZERO_STANDING | 1 | 13 |
| FOOTNOTE_CAVEAT | 7 instances (of 15 footnotes) | 7, 13, 14, 21, 22 |
| DECK_ONLY | 9 metric categories across | 4/13, 14, 17, 21, 22 |
| UNSOURCED_TAM | 1 | 17 |
| DIRECTION_UNCLEAR | 2 (PAT YoY, DSO YoY) | 4 |
| FORWARD_LOOKING_STATEMENT | 1 | 8 |
| COVER_LETTER | 1 | 1 |
| DISCLAIMER_TEXT | 1 | 3 |

---

## COUNT TEST RECAP

Slides: grep count = 22 (via `grep -c -E "\[page [0-9]+\]" extract_presentation_indgn_q1fy27.txt`),
manual sweep = 22 (sequential read, page 1 through page 22, no gap, no duplicate, all 22
`[page N]` markers accounted for in Table 1). **Match: yes. GATE A2: pass.**

OCR pages: grep count = 4 (`[OCR page N]` markers), manual sweep = 4, matches header's
`ocr_pages: [2, 12, 15, 20]` exactly. Slides 2, 12, 15, 20 are flagged OCR_LOWCONF throughout
this ledger; their content is section-divider/title text with no numeric disclosures at
stake, so the OCR-confidence risk on this document is contained (no quantified KPI sits on
an OCR'd slide).

```yaml
stage: A2-enumerator
company: "INDGN"
quarter: "Q1FY27"
doctype: "presentation"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/indgn-q1fy27/work/ledger_presentation_indgn_q1fy27.md"
counts:
  slides: 22
  slide_numbers: 22
  zero_standing: 1
flags_raised: [OCR_LOWCONF, NO_QUANTIFIED_METRICS, CHART_LAYOUT_RECONSTRUCTED, CHART_LAYOUT_AMBIGUOUS, ZERO_STANDING, FOOTNOTE_CAVEAT, DECK_ONLY, UNSOURCED_TAM, DIRECTION_UNCLEAR, FORWARD_LOOKING_STATEMENT]
gate_a2: pass
mismatch_note: ""
```
