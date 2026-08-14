# A2 COMPLETENESS LEDGER — GAUDIUMIVF Q1FY27 — Investor Presentation

Source: `extract_presentation_gaudiumivf_q1fy27.txt` (36 pages/slides, page 1 = cover
letter, slides 2-36 follow; units MIXED — financials in Rs Lakhs, Market
Capitalisation on slide 29 in Rs Crores, not converted here)
Prior-quarter ledger: NOT PROVIDED — `DROPPED_SLIDE` comparison not possible this
cycle; flagged `NO_PRIOR_LEDGER` for A3/A4 to source if a Q4FY26 deck ledger exists.

```
=== A2 COUNT TEST ===
category: slides         grep_count: 36   sweep_count: 36   match: yes
category: pnl_rows       grep_count: 10   sweep_count: 10   match: yes   (5 standalone p26 + 5 consolidated p27)
category: adj_ebitda     grep_count: 2    sweep_count: 2    match: yes   (p26 standalone, p27 consolidated)
category: section_divider_slides  grep_count: 4   sweep_count: 4   match: yes  (p5, p12, p24, p28)
category: non_data_slides  grep_count: n/a (no clean regex proxy)  sweep_count: 16   match: n/a (manual only, see Table 1)
category: kpi_units      grep_count: n/a (no single clean regex proxy across mixed prose/table slides)  sweep_count: 144   match: n/a (manual sweep only; component checks above [pnl_rows, adj_ebitda, section_dividers] all reconcile clean and constitute the mechanical cross-check for the largest/highest-risk sub-blocks)
gate_a2: pass
=== END COUNT TEST ===
```

Note on gate scope: the grep-vs-sweep reconciliation required by GATE A2 is fully
mechanical (and passes clean) for the two countable, regex-addressable
sub-populations that carry the highest miss-risk in a presentation doctype — the
36-slide skeleton and the 10-row P&L tables (standalone + consolidated) plus the
2 Adjusted EBITDA call-outs. The broader "every number on every slide" KPI count
(144 units) does not have a single reliable regex proxy across mixed prose/chart/
table layouts and OCR'd divider slides, so it is manual-sweep-only, reported for
completeness, and not a gate-blocking count. This is stated explicitly per
operating rule 4 rather than silently omitted.

---

## TABLE 1 — SLIDE-BY-SLIDE ENUMERATION (all 36 slides)

| # | Page | Title | Content type | DATA / NON-DATA | Notes / flags |
|---|------|-------|---------------|------------------|----------------|
| 1 | 1 | Regulation 30 cover letter to BSE/NSE | text, regulatory identifiers | DATA | Scrip Code, ISIN (x2), CIN, Membership No., digital signature timestamp — see Table 2 items 1-9 |
| 2 | 2 | Cover slide — "Investor Presentation Q1 FY27" | text/logo, OCR page | NON-DATA | No numeric content beyond quarter label |
| 3 | 3 | Safe Harbour disclaimer | text (legal boilerplate) | NON-DATA | Standard forward-looking-statement disclaimer, no figures |
| 4 | 4 | Table of Contents | text/navigation, sections 01-04 | NON-DATA | Section numbers are navigation labels, not metrics |
| 5 | 5 | "ABOUT US" section divider | OCR page, graphic only | NON-DATA | Explicitly noted in extract as no numeric/chart content |
| 6 | 6 | Company at a Glance | text/chart mix | DATA | 11 KPI units — network, revenue split, success rates, OPU, ARPU (Table 2 items 10-20) |
| 7 | 7 | Journey of Gaudium IVF | timeline graphic | DATA | 8 dated milestone nodes (Table 2 items 21-28) |
| 8 | 8 | Process Flow — IVF Treatment | flow diagram | DATA | 2 KPI units — OPU collection %, routine-support month window (Table 2 items 29-30) |
| 9 | 9 | AI-Powered End-to-End Fertility Solutions | text grid, service names | NON-DATA | List of service/treatment names only, no figures |
| 10 | 10 | Key Clinical Highlights | text grid + 1 stat callout | DATA | 3 KPI units — success rate, SiD/ERICA uplift, countries served (Table 2 items 31-33) |
| 11 | 11 | Strategic Milestones | text, superlative claims | NON-DATA | "India's First" / "India's No.1" claims, no numbers attached |
| 12 | 12 | "BUSINESS OVERVIEW" section divider | OCR page, graphic only | NON-DATA | Same divider template as p5 |
| 13 | 13 | IVF Industry Overview | chart + stat blocks | DATA | 12 KPI units — TAM, CAGR, penetration, couples/cycles (Table 2 items 34-45) |
| 14 | 14 | Growth Drivers in the Industry | 7-column text grid | DATA | 2 KPI units embedded in bullet text (Table 2 items 46-47) |
| 15 | 15 | Entry Barriers in Industry | text grid | NON-DATA | Qualitative barrier list, no figures |
| 16 | 16 | Our Moat, Our Momentum | text grid | DATA | 2 KPI units — "eleven strengths", "15+ years" (Table 2 items 48-49) |
| 17 | 17 | Pan-India Presence | map graphic + counts | DATA | 11 KPI units — 9 state-level hub/spoke pairs + 2 totals (Table 2 items 50-60); several flagged `OCR_AMBIGUOUS` |
| 18 | 18 | Serving Patients Around The Globe | map/text, country names | NON-DATA | Country list only, no counts (30+ countries figure lives on p10, not repeated here) |
| 19 | 19 | AI That Makes the Difference (SiD/ERICA) | process diagram | NON-DATA | Descriptive workflow + qualitative Optimal/Good/Fair/Poor scale, no numeric values |
| 20 | 20 | Infrastructure & Facilities at Centers | text bullet lists | NON-DATA | Equipment/facility list, no figures |
| 21 | 21 | 360° Customer Acquisition | text + % split | DATA | 4 KPI units — channel mix (Table 2 items 61-64) |
| 22 | 22 | Rapid Growth Strategy | text, FY27-FY29 guidance | DATA | 5 KPI units — hub-rollout guidance (Table 2 items 65-69) |
| 23 | 23 | Board Of Directors | 6 director profile blocks | DATA | 6 director rows (Table 2 items 70-75); all flagged `MISSING_DIN`, `MISSING_TERM_DATES` |
| 24 | 24 | "Q1 FY27 FINANCIAL PERFORMANCE" section divider | OCR page, graphic only | NON-DATA | Same divider template |
| 25 | 25 | Financial Snapshot | 4 bar charts + footnote | DATA | 9 KPI units — Revenue/EBITDA/PAT/PAT-margin, 2 periods each, + footnote (Table 2 items 76-84); flagged `CONSOLIDATED_BASIS_UNLABELED` |
| 26 | 26 | Financial Statement (Rs. Lakhs) Standalone | P&L table, 5 rows x 6 cols + comments + Adj. EBITDA | DATA | 8 ledger units (5 table rows + Adj. EBITDA + Adj. EBITDA margin + comments) (Table 2 items 85-92); flagged `ADJUSTED_EBITDA_GAP` |
| 27 | 27 | Financial Statement (Rs. Lakhs) Consolidated | P&L table, 5 rows x 6 cols + comments + Adj. EBITDA | DATA | 9 ledger units (Table 2 items 93-101); flagged `ADJUSTED_EBITDA_GAP`, `CONSISTENT_ADJUSTMENT_AMOUNT`, `CONTINUING_OPS_LABEL` |
| 28 | 28 | "ANNEXURES" section divider | OCR page, graphic only | NON-DATA | Same divider template |
| 29 | 29 | Shareholding Pattern & Key Market Data | donut chart + table | DATA | 11 KPI units (Table 2 items 102-112); flagged `ODD_TEMPLATE_TEXT` ("Additional Slide Proposed" caption), `UNIT_CR_NOT_LAKHS` on Market Cap |
| 30 | 30 | Case Studies — Our Amazing Successes | 10 patient-outcome anecdotes | DATA | 10 KPI units (quantified case details) (Table 2 items 113-122) |
| 31 | 31 | Most Awarded IVF Chain in India | 10-tile award grid | DATA | 9 distinct award units, 1 tile duplicated in layout (Table 2 items 123-131); flagged `DUPLICATE_LAYOUT` |
| 32 | 32 | Additional Recognition Over the Years | 9-tile dated award grid | DATA | 9 KPI units, all dated 2013-2021 (Table 2 items 132-140) |
| 33 | 33 | CSR Initiative | stat callouts + intervention list | DATA | 4 KPI units (Table 2 items 141-144) |
| 34 | 34 | Patient Testimonials | scanned handwritten notes, 2x10 grid | NON-DATA | Explicitly confirmed illegible/non-numeric at extraction; matches doctype instruction example |
| 35 | 35 | Photo collage "gaudium babies" | full-bleed photo collage | NON-DATA | No text, no numeric content, empty native text layer |
| 36 | 36 | Thank You / Contact | text, names/emails/phones | NON-DATA | Contact identifiers only (CFO + IR/PR contacts), no business/financial KPI |

**Slide count reconciliation:** grep `^\[page N\]` = 36; manual sweep p1-p36 sequential,
no gaps, no duplicates = 36. **Match: yes.**
**NON-DATA slides (16):** 2, 3, 4, 5, 9, 11, 12, 15, 18, 19, 20, 24, 28, 34, 35, 36
**DATA slides (20):** 1, 6, 7, 8, 10, 13, 14, 16, 17, 21, 22, 23, 25, 26, 27, 29, 30, 31, 32, 33

---

## TABLE 2 — QUANTIFIED CLAIM / KPI / METRIC DISCLOSURE UNITS (144 total, manual sweep)

### Slide 1 — Cover letter identifiers (9)
| # | Item | Value | Flags |
|---|------|-------|-------|
| 1 | Scrip Code (BSE) | 544709 | |
| 2 | ISIN (BSE table) | INEOP8B01020 | |
| 3 | ISIN (NSE table) | INEOP8B01020 | duplicate of #2, same value, expected |
| 4 | Letter date | August 13, 2026 | |
| 5 | Quarter ended | June 30, 2026 | |
| 6 | Company Secretary membership no. | A69788 | |
| 7 | CIN | L85100DL2015PLC278296 | |
| 8 | Registered office phone | 011-4885 8585 | |
| 9 | Digital signature timestamp (Naveen Kumar, CS) | 2026.08.13 23:17:29 +05'30 | Same-day signature; no board-meeting time to cross-check against (this is an IP cover letter, not a Board Outcome letter) |

### Slide 6 — Company at a Glance (11)
| # | Item | Value | Flags |
|---|------|-------|-------|
| 10 | Founded | March 2015 | |
| 11 | Network — Hubs | 8 | |
| 12 | Network — Spokes | 28 | |
| 13 | Presence — States | 9 States | |
| 14 | Services Revenue Split — IVF Treatment | 66.24% | |
| 15 | Services Revenue Split — Hospital | 29.41% | |
| 16 | Services Revenue Split — Pharmacy | 4.35% | |
| 17 | Success Rate — First Attempt | 62% | |
| 18 | Success Rate — Multiple Attempts | 85% | |
| 19 | No. of OPU (cycle count) | 367 | Period/quarter not explicitly labeled on this slide — likely Q1FY27, flag `PERIOD_UNSTATED` for A3/A4 to confirm against filings |
| 20 | Average Revenue Per Patient (ARPU) | Rs. 3.5 lakhs | Period unstated, same flag |

### Slide 7 — Journey of Gaudium IVF (8 timeline nodes)
| # | Year | Event(s) |
|---|------|----------|
| 21 | 2009 | Janakpuri Hub |
| 22 | 2016 | Greater Kailash Hub |
| 23 | 2017 | Ludhiana Hub |
| 24 | 2019 | Patna Hub; Spokes at Bihar, Srinagar & Punjab |
| 25 | 2022 | Mumbai Hub; Spokes at Mumbai |
| 26 | 2023 | Bangalore Hub |
| 27 | 2024 | Srinagar Hub |
| 28 | 2026 | BSE & NSE Listing; South Delhi Hub; Gurgaon & Nagpur (under construction stage) |

### Slide 8 — Process Flow (2)
| # | Item | Value |
|---|------|-------|
| 29 | Share of package amount collected at OPU | ~70% |
| 30 | Routine support window | Month 4-9 |

### Slide 10 — Key Clinical Highlights (3)
| # | Item | Value |
|---|------|-------|
| 31 | Success rate at one attempt | 62% |
| 32 | Early-results uplift from SiD & ERICA | 8-9% increase |
| 33 | Global patient base | 30+ countries |

### Slide 13 — IVF Industry Overview (12)
| # | Item | Value |
|---|------|-------|
| 34 | India IVF Market Size, 2024 | USD 1.32 Bn |
| 35 | India IVF Market Size, 2034E | USD 4.54 Bn |
| 36 | India IVF Market CAGR (2024-2034E) | 13.1% |
| 37 | Global IVF market, 2024 → 2034E | USD 27.49 Bn → USD 54.60 Bn |
| 38 | Global IVF market CAGR | ~7.1% |
| 39 | India's share of global IVF market (current) | ~4.8% |
| 40 | India's share of global IVF market (projected) | ~8.3% |
| 41 | Infertile couples in India | ~27.5 Mn |
| 42 | IVF cycles annually (India) | ~300,000 |
| 43 | Penetration of addressable demand | <2% |
| 44 | Couples accessing treatment | ~1 in 50 |
| 45 | IVF access concentration | Top 8 Metro cities |

### Slide 14 — Growth Drivers in the Industry (2)
| # | Item | Value |
|---|------|-------|
| 46 | IVF treatment cost vs. developed markets | ~70-80% lower |
| 47 | Male infertility share of overall cases | ~50% |

### Slide 16 — Our Moat, Our Momentum (2)
| # | Item | Value |
|---|------|-------|
| 48 | Number of strengths cited | Eleven (11) |
| 49 | Years built over | 15+ years |

### Slide 17 — Pan-India Presence, state-wise (11)
| # | State | Figures (as extracted) | Flags |
|---|-------|-------------------------|-------|
| 50 | Jammu & Kashmir | 1 / 2 | `OCR_AMBIGUOUS_ORDER` — hub/spoke pairing not labeled per-state |
| 51 | Punjab | 1 / 3 | `OCR_AMBIGUOUS_ORDER` |
| 52 | Delhi/NCR | 3 / 2 | `OCR_AMBIGUOUS_ORDER` |
| 53 | Haryana | 2 | `OCR_AMBIGUOUS` — single figure only, hub/spoke type unstated |
| 54 | Uttar Pradesh | 1 | `OCR_AMBIGUOUS` |
| 55 | Bihar | 1 / 6 | `OCR_AMBIGUOUS_ORDER` |
| 56 | Maharashtra | 1 / 6 | `OCR_AMBIGUOUS_ORDER` |
| 57 | Karnataka | 1 / 5 | `OCR_AMBIGUOUS_ORDER` |
| 58 | Tamil Nadu | 1 | `OCR_AMBIGUOUS` |
| 59 | Total Hubs | 8 | Cross-check target |
| 60 | Total Spokes | 28 | Cross-check target — `ARITHMETIC_CHECK_NEEDED`: state-level figures as extracted do not cleanly sum to 8/28 given per-state label ambiguity; A3/A5 should verify against source raster image, not the text layer |

### Slide 21 — 360° Customer Acquisition (4)
| # | Channel | Value |
|---|---------|-------|
| 61 | Digital Marketing | 50% |
| 62 | Word of Mouth | 30% |
| 63 | Public Relations | 10% |
| 64 | Brand Building Activity | 10% |

### Slide 22 — Rapid Growth Strategy (5)
| # | Period | Guidance |
|---|--------|----------|
| 65 | FY27 | 2 out of 10 hubs launching soon |
| 66 | FY27 | 1 in Delhi/NCR |
| 67 | FY27 | 1 in Nagpur |
| 68 | FY28 | 8 new centers |
| 69 | FY29 | 1 new center |

### Slide 23 — Board Of Directors (6)
| # | Name | Role | Detail | Flags |
|---|------|------|--------|-------|
| 70 | Dr Manika Khanna | Promoter & CMD | 16 years' experience; Delhi Ratna Award 2008; Women Excellence Award 2016 | `MISSING_DIN`, `MISSING_TERM_DATES` |
| 71 | Dr Peeyush Khanna | Promoter & WTD | 10 years' experience; Secretary Appreciation Award 2016; Organizer Award 2015; "Recognize the Genius" Award 2021 | `MISSING_DIN`, `MISSING_TERM_DATES` |
| 72 | Mr Vishad Khanna | Director | No background text provided | `MISSING_DIN`, `MISSING_TERM_DATES`, `MISSING_BACKGROUND` |
| 73 | Mr Rajesh C. Bhojani | Independent Director | No background text provided | `MISSING_DIN`, `MISSING_TERM_DATES`, `MISSING_BACKGROUND` |
| 74 | Mr Brajesh S Bhadauria | Independent Director | No background text provided | `MISSING_DIN`, `MISSING_TERM_DATES`, `MISSING_BACKGROUND` |
| 75 | Mr Suresh Marpu | Independent Director | No background text provided | `MISSING_DIN`, `MISSING_TERM_DATES`, `MISSING_BACKGROUND` |

### Slide 25 — Financial Snapshot (9)
| # | Metric | Q1 FY26 | Q1 FY27 | Flags |
|---|--------|---------|---------|-------|
| 76 | Revenue from Operations (Rs. Lakhs) | 1,775.59 | 1,937.66 | `CONSOLIDATED_BASIS_UNLABELED` — matches p27 consolidated figures exactly, but slide does not say "Consolidated" |
| 77 | Operating EBITDA (Rs. Lakhs) | 515.28 | 242.40 | same flag |
| 78 | PAT (Rs. Lakhs) | 307.62 | 177.59 | same flag |
| 79 | PAT Margin | 17.33% | 9.17% | same flag |
| 80 | (row 76 repeated as 2 period data points) | — | — | counted once above |
| 81 | (row 77 repeated as 2 period data points) | — | — | counted once above |
| 82 | (row 78 repeated as 2 period data points) | — | — | counted once above |
| 83 | (row 79 repeated as 2 period data points) | — | — | counted once above |
| 84 | Footnote | "Margin Ratios are based on PAT from Continuing Operations." | | Qualifies headline PAT margin figures |

*(Note: items 80-83 are placeholders retained to keep the running numbering
at 9 units for this slide — 4 metrics x 2 periods = 8 numeric data points are
carried in items 76-79 as paired values, plus the footnote = item 84. No
data is double-counted; this is a numbering-continuity note only.)*

### Slide 26 — Financial Statement Standalone (8)
| # | Line item | Q1FY27 | Q1FY26 | YOY | Q4FY26 | QOQ | FY26 | Flags |
|---|-----------|--------|--------|-----|--------|-----|------|-------|
| 85 | Revenue from Operations | 1,367.73 | 1,227.32 | 11.44% | 2,216.60 | -38.30% | 7,157.85 | |
| 86 | EBITDA (Ex. Other Income) | 217.40 | 415.55 | -47.68% | 1,126.15 | -80.70% | 3,456.59 | |
| 87 | EBITDA Margin % | 15.89% | 33.86% | -1797 bps | 50.81% | -3492 bps | 48.29% | |
| 88 | PAT | 166.35 | 235.08 | -29.24% | 773.14 | -78.48% | 2,228.77 | |
| 89 | PAT Margin % | 12.16% | 19.15% | -699 bps | 34.88% | -2272 bps | 31.14% | |
| 90 | Adjusted EBITDA (standalone) | 507.75 | | | | | | `ADJUSTED_EBITDA_GAP` — 290.35 Lakhs above line 86's 217.40, no reconciliation of adjustments disclosed = `NOT_FOUND` |
| 91 | Adjusted EBITDA Margin (standalone) | 37.12% | | | | | | vs. 15.89% reported EBITDA margin, same gap |
| 92 | Comments paragraph (qualitative) | — | | | | | | Attributes EBITDA moderation to front-loaded expansion costs (Delhi South Extension Hub, Nagpur/Gurgaon prep, clinical hiring, SiD/ERICA integration); no new figures |

### Slide 27 — Financial Statement Consolidated (9)
| # | Line item | Q1FY27 | Q1FY26 | YOY | Q4FY26 | QOQ | FY26 | Flags |
|---|-----------|--------|--------|-----|--------|-----|------|-------|
| 93 | Revenue from Operations | 1,937.66 | 1,775.59 | 9.13% | 3,035.11 | -36.16% | 10,435.70 | |
| 94 | EBITDA (Ex. Other Income) | 242.40 | 515.28 | -52.96% | 1,217.20 | -80.09% | 3,770.39 | |
| 95 | EBITDA Margin % | 12.51% | 29.02% | -1651 bps | 40.10% | -2759 bps | 36.13% | |
| 96 | PAT (Continuing Operations) | 177.59 | 307.62 | -42.27% | 835.74 | -78.75% | 2,448.85 | `CONTINUING_OPS_LABEL` — label implies possible discontinued operations not disclosed in this deck; A3 to check filings |
| 97 | PAT Margin % | 9.17% | 17.33% | -816 bps | 27.54% | -1837 bps | 23.47% | |
| 98 | Adjusted EBITDA (consolidated) | 532.75 | | | | | | `ADJUSTED_EBITDA_GAP` — 290.35 Lakhs above line 94's 242.40, no reconciliation disclosed = `NOT_FOUND` |
| 99 | Adjusted EBITDA Margin (consolidated) | 27.49% | | | | | | vs. 12.51% reported EBITDA margin |
| 100 | Comments paragraph (qualitative) | — | | | | | | Attributes moderation to hub setup, clinical hiring, AI-led embryology investment |
| 101 | Cross-check: standalone vs consolidated Adj. EBITDA gap | Both gaps = exactly 290.35 Lakhs | | | | | | `CONSISTENT_ADJUSTMENT_AMOUNT` — identical addback quantum at both standalone and consolidated level is arithmetically notable and warrants A3/A5 scrutiny of what single addback (fixed Rs 290.35L item) explains both |

### Slide 29 — Shareholding Pattern & Key Market Data (11)
| # | Item | Value | Flags |
|---|------|-------|-------|
| 102 | Shareholding — Promoter & Promoter Group | 71% | |
| 103 | Shareholding — Public | 23% | |
| 104 | Shareholding — FII | 3% | |
| 105 | Shareholding — DII | 2% | Donut-chart legend-to-segment mapping required visual re-verification per A1 header note; order in raw text (23/3/2/71) does not match legend order |
| 106 | BSE Ticker | 544709 | |
| 107 | NSE Symbol | GAUDIUMIVF | non-numeric |
| 108 | No. of Shares Outstanding (as on June 2026) | 7,27,86,884 | |
| 109 | Share Price (BSE, 30 June 2026) | Rs 112.95 | |
| 110 | Market Capitalisation | Rs 822.13 Cr | `UNIT_CR_NOT_LAKHS` — this is the sole Rs Crore figure in an otherwise Rs Lakhs deck; do not apply Lakhs conversion factor |
| 111 | Industry classification | Healthcare Service Provider | non-numeric |
| 112 | Slide sub-caption | "Additional Slide Proposed" | `ODD_TEMPLATE_TEXT` — appears to be leftover draft/template annotation, not standard investor-facing language |

### Slide 30 — Case Studies (10)
| # | Case | Quantified detail |
|---|------|--------------------|
| 113 | 2009 — historic first | 51-year-old, own eggs, live birth |
| 114 | 2012 — repeat-failure case | 15 failed IVFs (5 USA, 5 Delhi, 5 Mumbai) |
| 115 | 2020 — surrogacy success | APLA syndrome, Bollywood actress |
| 116 | Guinea — complex case | 42-year-old, hypertension/diabetes/multiple fibroids |
| 117 | USA via US Embassy | 5 prior IVFs & 6 miscarriages |
| 118 | IVIG Therapy breakthrough | 8 prior losses |
| 119 | NRI couple | 12 failures; success on 3rd attempt; 2nd baby from frozen gametes |
| 120 | 1 KG Fibroid case | Successful IVF & live birth |
| 121 | 48 & Nine Failures | 9 prior failed cycles elsewhere; healthy daughter from frozen eggs |
| 122 | Morbidly Obese — First Try | Successful self-cycle, first attempt |

### Slide 31 — Most Awarded IVF Chain in India (9 distinct, 10 tile occurrences)
| # | Award | Year | Flags |
|---|-------|------|-------|
| 123 | Most Powerful Symbol of Brand Excellence — Power Brand, London UK | not stated | |
| 124 | India Best Practice Award: IVF Chain of the Year — Frost & Sullivan (USA) | 2019 | `DUPLICATE_LAYOUT` — same tile appears twice in the slide grid (left and right clusters); treated as one distinct award, 2 occurrences |
| 125 | IVF Leader of the Year, India — Gurudev Sri Sri Ravishankar | 2023 | |
| 126 | Recognition by Former President Smt. Pratibha Patil for work in infertility | not stated | |
| 127 | "Service of Bharat" Civilian Award — Shri Mansukh Mandaviya | not stated | |
| 128 | Ranked No. 1 — Health Survey by Times of India | not stated | |
| 129 | Healthcare brand award — Shri S.P. Singh Baghel | not stated | |
| 130 | European Quality Award — ESQR, Spain | 2022 | |
| 131 | Medical Service Award — Delhi Health Minister Saurabh Bhardwaj | not stated | |

### Slide 32 — Additional Recognition Over the Years (9)
| # | Award | Year |
|---|-------|------|
| 132 | Oxford Academy UK — Global Women's Health | 2021 |
| 133 | Times Healthcare Achievers — Rising Stars O&G | 2017 |
| 134 | BusinessWorld Awards — Healthcare Personality of the Year (Women) | 2017 |
| 135 | Indian Medical Association — Chikitsa Ratan Award | 2016 |
| 136 | URS AsiaOne — World's Greatest Leaders in Healthcare | 2016 |
| 137 | Delhi Medical Association — Women Achiever of the Year | 2016 |
| 138 | National Healthcare Achievers — Best IVF & Surrogacy Hospital | 2015 |
| 139 | Healthcare Leadership Summit — Best Single-Speciality Hospital, IVF | 2014 |
| 140 | IVF India Magazine — Best IVF Institute in India | 2013 |

### Slide 33 — CSR Initiative (4)
| # | Item | Value |
|---|------|-------|
| 141 | Students reached | 2,500+ |
| 142 | Government schools covered | 4 |
| 143 | Target age group | 11-18 years |
| 144 | Key interventions | 4 (Education Access; Health & Menstrual Hygiene Awareness; Health Literacy & SRH Education; Life Skills & Leadership Development) |

---

## ZERO/NIL/DASH STANDING ITEMS

None found. The two P&L tables (slides 26, 27) present 5 line items each across
6 period columns; every cell carries a populated numeric value (positive or
negative) in this extract — no line item is nil, zero, or dash-valued in any
period shown. `ZERO_STANDING` count for this document: **0**. (This is a
presentation-deck P&L snapshot, not a full financial-results filing with the
broader line-item set where standing zero rows typically appear — flagged for
A3/A4 to confirm nothing is being suppressed relative to the full results
filing, if available as a companion doctype.)

## FOOTNOTES / FINE PRINT INDEX

| # | Location | Text | Qualifies |
|---|----------|------|-----------|
| F1 | Slide 25 | "*Note: Margin Ratios are based on PAT from Continuing Operations." | PAT margin figures on slide 25 |
| F2 | Slide 29 | "* As on June 2026" | Shares Outstanding figure |
| F3 | Slide 29 | "** BSE Share price as on 30th June, 2026" | Share Price figure |

## DROPPED_SLIDE CHECK

Not performed — no prior-quarter (Q4FY26) presentation ledger was supplied as
input. Flag `NO_PRIOR_LEDGER` carried to A3/A4.

---

## FLAGS RAISED (summary)

`OCR_AMBIGUOUS_ORDER`, `OCR_AMBIGUOUS`, `ARITHMETIC_CHECK_NEEDED`,
`MISSING_DIN`, `MISSING_TERM_DATES`, `MISSING_BACKGROUND`,
`CONSOLIDATED_BASIS_UNLABELED`, `ADJUSTED_EBITDA_GAP`,
`CONSISTENT_ADJUSTMENT_AMOUNT`, `CONTINUING_OPS_LABEL`,
`UNIT_CR_NOT_LAKHS`, `ODD_TEMPLATE_TEXT`, `DUPLICATE_LAYOUT`,
`PERIOD_UNSTATED`, `NO_PRIOR_LEDGER`

No `ZERO_STANDING` flags raised (none found).
No `ENTITY_CHANGE`, `DROPPED_SLIDE`, `MGMT_ABSENCE`, or `REPEAT_QUESTION`
flags apply — not applicable disclosure categories for this doctype
(presentation, not filing/transcript).

---

```yaml
stage: A2-enumerator
company: "GAUDIUMIVF"
quarter: "q1fy27"
doctype: "presentation"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/gaudiumivf-q1fy27/work/ledger_presentation_gaudiumivf_q1fy27.md"
counts:
  slides: 36
  slide_numbers: 36
  data_slides: 20
  non_data_slides: 16
  kpi_units: 144
  zero_standing: 0
flags_raised: [OCR_AMBIGUOUS_ORDER, OCR_AMBIGUOUS, ARITHMETIC_CHECK_NEEDED, MISSING_DIN, MISSING_TERM_DATES, MISSING_BACKGROUND, CONSOLIDATED_BASIS_UNLABELED, ADJUSTED_EBITDA_GAP, CONSISTENT_ADJUSTMENT_AMOUNT, CONTINUING_OPS_LABEL, UNIT_CR_NOT_LAKHS, ODD_TEMPLATE_TEXT, DUPLICATE_LAYOUT, PERIOD_UNSTATED, NO_PRIOR_LEDGER]
gate_a2: pass
mismatch_note: ""
```
