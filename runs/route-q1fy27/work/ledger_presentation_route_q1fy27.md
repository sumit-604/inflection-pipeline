# A2 ENUMERATOR LEDGER — Route Mobile Limited (ROUTE), Q1 FY27, Investor Presentation

Source: investor_presentation.pdf (18 pages, page_count_pdfinfo=18, formfeed_count=18).
Unit convention per A1 header: **Millions** (x0.1 to convert to Rs Crores). All figures below
are carried in their stated slide unit (₹ mn, %, counts, bn transactions) — no conversion applied.
OCR pages per A1 header: 6, 10, 13, 18 (all four confirmed section-divider/closing slides with
no numeric content beyond the heading text).

Prior-quarter ledger: **none available** — DROPPED_SLIDE comparison (rule 3, INVESTOR
PRESENTATION enumeration) could not be performed. Flagged as `NO_PRIOR_LEDGER`, not a
gate failure.

## METHODOLOGY NOTE — numbers count reconciliation
Raw mechanical grep pass: `grep -n -oE '[0-9][0-9,]*\.?[0-9]*%?' <extract>` on lines 15–561
(post-header) returns **407** numeric-token matches. Of these, **26** are self-referential
extraction artifacts, not slide content: 18 are the digit inside each `[page N]` marker line
(one per slide, A1's own pagination tag) and 8 are the digit inside the `[OCR page N]` /
`[CHART, page N, ...]` annotation lines A1 inserted for the four OCR'd divider slides
(6, 10, 13, 18 — 2 tokens each). Excluding these 26 leaves **381** genuine slide-content
numeric tokens. The manual sweep below independently walks all 18 slides top-to-bottom,
grouping the same 381 tokens into 121 semantic rows (chart series, table cells, bullet
figures, dates, footnote figures, printed footer page numbers); each row's token count is
shown in the `Tok` column, and the column sums to 381, confirming the two counts reconcile
token-for-token.

```
=== A2 COUNT TEST ===
category: slides         grep_count: 18    sweep_count: 18    match: yes
category: numbers        grep_count: 381   sweep_count: 381   match: yes
category: zero_standing  grep_count: 6     sweep_count: 6     match: yes
category: footnotes      grep_count: 10    sweep_count: 10    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

---

## TABLE 1 — SLIDE INVENTORY (18 slides, grep_count=18 via `grep -c "^\[page"`, sweep_count=18)

| # | Extract page tag | Printed deck footer # | Title | Content type | Flags |
|---|---|---|---|---|---|
| 1 | [page 1] | (none) | Regulation 30 covering letter to BSE/NSE ("Investor Presentation") | text (regulatory letter) | — |
| 2 | [page 2] | (none) | "Earnings Update Q1 FY 26-27 — Investor Presentation, July 23, 2026" (title slide) | text | — |
| 3 | [page 3] | 2 | Safe Harbor | text (disclaimer, full-page) | — |
| 4 | [page 4] | 3 | Route Mobile - Industry Leading Global CPaaS Platform | text + stat callouts | — |
| 5 | [page 5] | 4 | Global Diaspora - Footprint & Super Network | map/infographic with data labels | — |
| 6 | [page 6] | (none captured) | Key Developments | chart/section-divider (OCR'd) | SECTION_DIVIDER, ZERO content |
| 7 | [page 7] | 6 | Commercial Highlights (Partnerships & Market Expansion) | text (3-panel narrative) | — |
| 8 | [page 8] | 7 | Technological Advancements (Product, Platform & Innovation) | text/graphic (world-map, mostly non-extractable diagonal labels) | — |
| 9 | [page 9] | 8 | Focus on Expanding Product Portfolio | text + chart (New Products Revenue) | — |
| 10 | [page 10] | (none captured) | Key Business Metrics | chart/section-divider (OCR'd) | SECTION_DIVIDER, ZERO content |
| 11 | [page 11] | 10 | Diverse Customer Base | chart (industry mix, top-50-countries, HQ-continent) | OCR_LAYOUT_AMBIGUOUS |
| 12 | [page 12] | 11 | Customer Cohort Analysis | chart (account-size buckets, concentration) | OCR_LAYOUT_AMBIGUOUS |
| 13 | [page 13] | (none captured) | Financial Highlights | chart/section-divider (OCR'd) | SECTION_DIVIDER, ZERO content |
| 14 | [page 14] | 13 | Analysis of Q1 FY 26-27 Performance | chart + text (Revenue, Gross Profit) | — |
| 15 | [page 15] | 14 | Analysis of Q1 FY 26-27 Performance (continued) | chart + text (Adj. EBITDA, Adj. PAT) | — |
| 16 | [page 16] | 15 | Adjusted EBITDA / PAT | table (2 reconciliation tables + disclaimer) | ZERO_STANDING |
| 17 | [page 17] | 16 | Human Resource Capital | chart (location/function headcount) | OCR_LAYOUT_AMBIGUOUS |
| 18 | [page 18] | (none captured) | Thank You | chart/closing slide (OCR'd) | SECTION_DIVIDER, ZERO content |

Note: deck-internal footer numbering runs 2–16 starting on slide 3; slides 2 (title), 6, 10,
13 and 18 (all section dividers/cover/close) carry no visible footer digit in the extracted
text — a consistent, expected pattern, not a defect.

---

## TABLE 2 — NUMBERS / CHART-DATA-LABEL LEDGER (121 rows, 381 tokens)

### Slide 1 — Regulation 30 covering letter (lines 15–54)
| Row | Line | Description / values | Tok | Flags |
|---|---|---|---|---|
| R1 | 16 | Ref No: RML/2026-27/693 | 3 | — |
| R2 | 18 | Submission date: July 23, 2026 | 2 | — |
| R3 | 22 | Scrip Code: 543228 | 1 | — |
| R4 | 28 | Regulation 30 of SEBI (LODR) Regulations 2015 | 2 | — |
| R5 | 29 | Presentation date to analysts: Friday, July 24, 2026 | 2 | — |
| R6 | 31 | Quarter-end reference: June 30, 2026 | 2 | — |
| R7 | 44 | Digital signature date: 2026.07.23 | 2 | — |
| R8 | 46 | Digital signature time: 22:11:19 +05'30' | 5 | — |
| R9 | 51 | ICSI Membership No.: A34829 | 1 | — |

### Slide 2 — Title slide (lines 55–66)
| Row | Line | Description / values | Tok | Flags |
|---|---|---|---|---|
| R10 | 57 | Quarter label "Q1 FY 26-27" (title) | 3 | — |
| R11 | 60 | Presentation date: July 23, 2026 | 2 | — |

### Slide 3 — Safe Harbor (lines 67–89)
| Row | Line | Description / values | Tok | Flags |
|---|---|---|---|---|
| R12 | 80 | "COVID-19" reference in risk-factor list | 1 | — |
| R13 | 88 | Printed slide footer number: 2 | 1 | PAGE_FOOTER |

### Slide 4 — Key metrics (lines 90–127)
| Row | Line | Description / values | Tok | Flags |
|---|---|---|---|---|
| R14 | 94 | Revenue for LTM ended 30 June 2026: ₹45,089 mn | 3 | — |
| R15 | 98 | 280+ direct MNO connects | 1 | — |
| R16 | 99 | EBITDA for LTM ended 30 June 2026: ₹5,195 mn | 3 | — |
| R17 | 100 | 900+ MNOs (Super Network) | 1 | — |
| R18 | 103 | 20+ locations | 1 | — |
| R19 | 104 | 45.80 bn billable transactions processed in Q1 26-27 | 4 | — |
| R20 | 105 | 2,100+ active billable clients | 1 | — |
| R21 | 108 | 20+ data centers | 1 | — |
| R22 | 109 | Net Cash as on 30 June 2026: ₹13,452 mn | 3 | — |
| R23 | 110 | 6 SMSCs globally | 1 | — |
| R24 | 115 | EPS in Q1 26-27: ₹9.94 | 4 | — |
| R25 | 119 | "Visionary in Magic Quadrant for CPaaS 2025 – Gartner" | 1 | — |
| R26 | 120 | Board recommended ₹4 per share interim dividend | 1 | — |
| R27 | 121 | "Tier 1 A2P SMS vendor – Rocco" / "four Hype Cycle Reports" label fragments | 2 | LAYOUT_FRAGMENT |
| R28 | 126 | Printed slide footer number: 3 | 1 | PAGE_FOOTER |

### Slide 5 — Global footprint / super network (lines 128–170)
| Row | Line | Description / values | Tok | Flags |
|---|---|---|---|---|
| R29 | 133 | Europe — Direct MNO: 110 | 1 | — |
| R30 | 136 | Europe — Employees: 32 | 1 | — |
| R31 | 136 | APAC — Direct MNO: 36 | 1 | — |
| R32 | 139 | APAC — Employees: 7 | 1 | — |
| R33 | 145 | Americas — Direct MNO: 53 | 1 | — |
| R34 | 145 | "12 Firewalls deployed" | 1 | — |
| R35 | 147 | Americas — Employees: 209 | 1 | — |
| R36 | 147 | India — Direct MNO: 6 | 1 | — |
| R37 | 148 | "20+ virtualized Data Centers" | 1 | — |
| R38 | 151 | "18 Hubs" | 1 | — |
| R39 | 152 | India — Employees: 502 | 1 | — |
| R40 | 154 | Total "783 Employees" | 1 | — |
| R41 | 155 | Middle East — Direct MNO: 15 | 1 | — |
| R42 | 158 | Middle East — Employees: 31 | 1 | — |
| R43 | 158 | "280+ Super Network" | 1 | — |
| R44 | 160 | Africa — Direct MNO: 64 | 1 | — |
| R45 | 163 | Africa — Employees: 2 | 1 | — |
| R46 | 164 | "Data as on June 30, 2026" | 2 | — |
| R47 | 169 | Printed slide footer number: 4 | 1 | PAGE_FOOTER |

### Slide 6 — "Key Developments" (lines 171–179)
No content rows. OCR-confirmed section-divider heading only; zero numeric content, per A1
header note. Flag `SECTION_DIVIDER`.

### Slide 7 — Commercial Highlights (lines 180–202)
| Row | Line | Description / values | Tok | Flags |
|---|---|---|---|---|
| R48 | 192 | CCGA 2026 award (Konera/Network APIs "Best Application Service Provider") | 1 | — |
| R49 | 193 | MWC Shanghai 2026 (brand-visibility forum) | 1 | — |
| R50 | 201 | Printed slide footer number: 6 | 1 | PAGE_FOOTER |

### Slide 8 — Technological Advancements (lines 203–228)
| Row | Line | Description / values | Tok | Flags |
|---|---|---|---|---|
| R51 | 227 | Printed slide footer number: 7 | 1 | PAGE_FOOTER |

No other numeric content — slide body is a garbled world-map graphic (country-name
fragments, "Coming Soon" markers) with no digits recoverable from pdftotext.

### Slide 9 — Focus on Expanding Product Portfolio (lines 229–282)
| Row | Line | Description / values | Tok | Flags |
|---|---|---|---|---|
| R52 | 243 | Bill-example header: "Jun 2026" | 1 | — |
| R53 | 248 | New Products Revenue Y-o-Y growth: 13.9% | 1 | — |
| R54 | 250 | New Products Revenue Q-o-Q growth: 10.5% | 1 | — |
| R55 | 253 | Bill-example Total Amount Due: ₹1,248.00 | 1 | — |
| R56 | 255 | Bill-example "Bill Period: Jun 2026" | 1 | — |
| R57 | 257 | Bill-example "Due Date: 28 Jun 2026" | 2 | — |
| R58 | 259 | Bill-example "Units Consumed: 182 kWh" | 1 | — |
| R59 | 273 | New Products Revenue chart series (₹ mn): 830 (Q1 25-26), 855 (Q4 25-26), 945 (Q1 26-27) | 3 | — |
| R60 | 276 | Chart x-axis period labels: Q1 25-26 / Q4 25-26 / Q1 26-27 | 9 | PERIOD_LABEL |
| R61 | 281 | Printed slide footer number: 8 | 1 | PAGE_FOOTER |

### Slide 10 — "Key Business Metrics" (lines 283–291)
No content rows. OCR-confirmed section-divider heading only; zero numeric content, per A1
header note. Flag `SECTION_DIVIDER`.

### Slide 11 — Diverse Customer Base (lines 292–333)
| Row | Line | Description / values | Tok | Flags |
|---|---|---|---|---|
| R62 | 294 | Title date: "...in Q1 26-27" | 3 | — |
| R63 | 295 | Chart heading fragment "Top 50" (Revenue for Top 50 countries by termination) | 1 | LAYOUT_FRAGMENT |
| R64 | 296 | Layout-fragment digit, source position unclear (industry-mix list area) | 1 | LAYOUT_FRAGMENT, OCR_LAYOUT_AMBIGUOUS |
| R65 | 299,300,303,304,305,307,313,316,317,319,323,324 | Percentage figures across industry-mix / "Revenue for Top 50 countries by termination" / "Revenue by customer HQ continent" sub-charts. Raw values in document order: 15%, 36%, 12%, 16%, 13%, 9%, 7%, 5%, 10%, 8%, 35%, 34%, 3%, 20%, 2%, 3%. Exact per-category attribution not extractable from flattened columnar layout. | 16 | OCR_LAYOUT_AMBIGUOUS |
| R66 | 313,313,314 | Layout-fragment digits (superscript/label artifacts near "Tier 1 CPaaS partners" and "Ecommerce" rows) | 3 | LAYOUT_FRAGMENT |
| R67 | 327 | Footnote (1): "Top 50 countries contribute c. 86% of Q1 26-27 revenue from operations" | 6 | — |
| R68 | 328 | Footnote (2): "Top 150 customers contribute c. 92% of Q1 26-27 revenue from operations" | 6 | — |
| R69 | 332 | Printed slide footer number: 10 | 1 | PAGE_FOOTER |

### Slide 12 — Customer Cohort Analysis (lines 334–376)
| Row | Line | Description / values | Tok | Flags |
|---|---|---|---|---|
| R70 | 342,349,355,361 | Clients by Account Size — FY25-26 counts: >$15mn=5, >$10mn=8, >$5mn=21, >$1mn=73 | 4 | — |
| R71 | 343,349,355,361 | Clients by Account Size — Q1 26-27 counts: >$15mn=5, >$10mn=10, >$5mn=21, >$1mn=77 | 4 | — |
| R72 | 343,349,355,361 | Account-size bucket threshold labels ($15mn / $10mn / $5mn / $1mn) | 4 | LAYOUT_FRAGMENT |
| R73 | 342,349,352 | Client Concentration category labels "Top 50 / Top 10 / Top 5" | 3 | LAYOUT_FRAGMENT |
| R74 | 344,351,352,354,355,356 | Client Concentration percentages — Top 50: 75%,76%,76%,75%; Top 10: 44%,48%,43%,43%; Top 5: 32%,33%,33%,31% (across FY23-24/FY24-25/FY25-26/Q1 26-27; period mapping inferred from source layout order, not independently confirmed) | 12 | OCR_LAYOUT_AMBIGUOUS |
| R75 | 364,365 | Chart x-axis period labels "FY 23-24 / FY 24-25 / FY 25-26 / Q1 26-27" (appears under both charts) | 15 | PERIOD_LABEL |
| R76 | 370 | Footnote (1): "3M FY26-27 Annualized" | 4 | — |
| R77 | 375 | Printed slide footer number: 11 | 1 | PAGE_FOOTER |

### Slide 13 — "Financial Highlights" (lines 377–386)
No content rows. OCR-confirmed section-divider heading only; zero numeric content, per A1
header note. Flag `SECTION_DIVIDER`.

### Slide 14 — Analysis of Q1 FY 26-27 Performance (lines 387–420)
| Row | Line | Description / values | Tok | Flags |
|---|---|---|---|---|
| R78 | 388,389 | Slide title / heading period refs ("Analysis of Q1 FY 26-27 Performance", "Q1 26-27 revenue performance") | 6 | — |
| R79 | 390 | Bullet: "Revenue increased by 1.8% Q-o-Q, and 9.6% Y-o-Y" | 2 | — |
| R80 | 391 | Bullet: "Sustained Q4 25-26 revenue momentum in Q1 26-27" | 6 | — |
| R81 | 392 | Billable transactions chart series (bn): 39.3 (Q1 25-26), 45.1 (Q4 25-26), 45.8 (Q1 26-27) | 3 | — |
| R82 | 393 | Bullet: "New gen product revenues grew at 10.5% Q-o-Q and 13.9% Y-o-Y" | 2 | — |
| R83 | 398 | Revenue chart series (₹ mn): 10,508 (Q1 25-26), 11,309 (Q4 25-26), 11,515 (Q1 26-27) | 3 | — |
| R84 | 400 | Chart x-axis period labels: Q1 25-26 / Q4 25-26 / Q1 26-27 | 9 | PERIOD_LABEL |
| R85 | 406,407,408,409 | Gross Profit Margin chart values (21.4% Q1 25-26, 23.3% Q4 25-26, 20.9% Q1 26-27) + bullets ("decreased 8.9% Q-o-Q, increased 6.8% Y-o-Y"; "margin declined to 20.9% in Q1 26-27 vs. 23.3% in Q4 25-26 vs. 21.4% in Q1 25-26") | 17 | — |
| R86 | 413 | Gross Profit chart series (₹ mn): 2,251 (Q1 25-26), 2,639 (Q4 25-26), 2,404 (Q1 26-27) | 3 | — |
| R87 | 414 | Chart x-axis period labels: Q1 25-26 / Q4 25-26 / Q1 26-27 | 9 | PERIOD_LABEL |
| R88 | 419 | Printed slide footer number: 13 | 1 | PAGE_FOOTER |

### Slide 15 — Analysis of Q1 FY 26-27 Performance (continued) (lines 421–465)
| Row | Line | Description / values | Tok | Flags |
|---|---|---|---|---|
| R89 | 422,423 | Title/superscript refs ("...Performance (continued)", "Adj. EBITDA(1)") | 4 | — |
| R90 | 426,427,429 | Adj. EBITDA margin chart values (11.0% Q1 25-26, 11.9% Q4 25-26, 9.5% Q1 26-27) + bullet "decreased by 18.9% Q-o-Q and 5.6% Y-o-Y" | 5 | — |
| R91 | 430 | Superscript ref "non-core items(3)" | 1 | — |
| R92 | 435 | Adj. EBITDA chart series (₹ mn): 1,154 (Q1 25-26), 1,343 (Q4 25-26), 1,089 (Q1 26-27) | 3 | — |
| R93 | 437 | Chart x-axis period labels: Q1 25-26 / Q4 25-26 / Q1 26-27 | 9 | PERIOD_LABEL |
| R94 | 442,443,444,446,447 | Adj. PAT margin chart axis gridlines/values + bullet %ages (12.0%, 10.1%, 40.1%, 16.6%, 10.0%, 8.0%, 6.0%) | 12 | — |
| R95 | 447,449 | Bullet: "Adj. PAT includes Forex gain of INR 6 mn in Q1 26-27, INR 181 mn in Q4 25-26 and forex loss of INR 247mn in Q1 25-26. Refer Slide 15 for calculation of Adj. PAT" | 13 | — |
| R96 | 455 | Adj. PAT chart series (₹ mn): 588 (Q1 25-26), 1,144 (Q4 25-26), 686 (Q1 26-27) | 3 | — |
| R97 | 458 | Chart x-axis period labels: Q1 25-26 / Q4 25-26 / Q1 26-27 | 9 | PERIOD_LABEL |
| R98 | 462 | Footnote 1: "Refer Slide 15 for calculation of EBITDA (Non-GAAP)" | 2 | — |
| R99 | 463 | Footnote 2: "Refer Slide 15 for calculation of Adj. PAT" | 2 | — |
| R100 | 464 | Footnote 3 + printed slide footer number 14: "Non core items includes Employee stock option expense and Net loss on foreign currency transactions and translation" | 2 | PAGE_FOOTER |

### Slide 16 — Adjusted EBITDA / PAT (lines 466–505)
| Row | Line | Description / values | Tok | Flags |
|---|---|---|---|---|
| R101 | 470 | Table 1 (EBITDA recon) header dates: 30.06.2026 / 31.03.2026 / 30.06.2025 / 31.03.2026 (TTM) | 8 | — |
| R102 | 472 | EBITDA row: 1,054.8 / 1,362.3 / 938.9 / 5,372.5 | 4 | — |
| R103 | 474 | "(+) Employee stock option expense (non cash)" row: - / - / 5.7 / 10.1 | 2 | ZERO_STANDING |
| R104 | 476 | "(+) Net loss on foreign currency transactions and translation" row: - / - / 247.3 / - | 1 | ZERO_STANDING |
| R105 | 478 | "(-) Intangible assets under development" row: 28.1 / 19.3 / 38.0 / 123.5 | 4 | — |
| R106 | 479 | "(+) Loss allowance – Capital advance (one time impact)" row: 49.0 / - / - / - | 1 | ZERO_STANDING |
| R107 | 480 | "(+) Professional fees related to Masivian security incident remediation" row: 13.6 / - / - / - | 1 | ZERO_STANDING |
| R108 | 481 | "Adjusted EBITDA (Non-GAAP)" row: 1,089.3 / 1,343.0 / 1,153.9 / 5,259.1 | 4 | — |
| R109 | 483 | "EBITDA margin % on a Non-GAAP basis" row: 9.5% / 11.9% / 11.0% / 11.9% | 4 | — |
| R110 | 488 | Table 2 (PAT recon) header dates: 30.06.2026 / 31.03.2026 / 30.06.2025 / 31.03.2026 (TTM) | 8 | — |
| R111 | 489 | "Reported PAT" row: 685.5 / 1,144.3 / 587.8 / 2,569.4 | 4 | — |
| R112 | 490 | "(+) Exceptional Item" row: - / - / - / 1,358.7 | 1 | ZERO_STANDING |
| R113 | 491 | "(-) Tax Impact on above" row: - / - / - / 166.9 | 1 | ZERO_STANDING |
| R114 | 492 | "Adjusted PAT" row: 685.5 / 1,144.3 / 587.8 / 3,761.2 | 4 | — |
| R115 | 495 | Footnote (1): "EBITDA = Profit before exceptional item minus Other income plus Finance cost and depreciation" | 1 | — |
| R116 | 504 | Printed slide footer number: 15 | 1 | PAGE_FOOTER |

Non-GAAP disclaimer paragraph (lines 497–499, no digits) qualifying the whole table is
carried separately in Table 4 (Footnotes & Disclaimers), not counted in the numbers total.

### Slide 17 — Human Resource Capital (lines 506–542)
| Row | Line | Description / values | Tok | Flags |
|---|---|---|---|---|
| R117 | 512,513,516,517,518,519,519,519,520,523 | HR chart data labels — Location wise break-up (India 502, International 281, Total 783) and Function wise break-up (6 categories: Tech & Tech Support, Sales & Marketing, Firewall & other operator solutions, General & Admin, Strategy/Accounts & Finance, Corporate-Business Heads; values 15, 65, 100, 346, 28, 229 in document order, sum=783 confirming total). Exact category-to-value mapping order not confirmable from flattened chart layout. | 10 | OCR_LAYOUT_AMBIGUOUS |
| R118 | 531 | "35 New Employees joined in Q1 FY26-27" | 4 | — |
| R119 | 533 | "60 Employees left in Q1 FY26-27" | 4 | — |
| R120 | 537 | Footnote: "As on June 30, 2026, Employee information excludes Call2Connect" | 3 | — |
| R121 | 541 | Printed slide footer number: 16 | 1 | PAGE_FOOTER |

### Slide 18 — Thank You (lines 543–561)
No content rows. OCR-confirmed closing slide (logo, tagline, social-media glyphs); zero
numeric content, per A1 header note. Flag `SECTION_DIVIDER`.

**Row-count check:** 9+2+2+15+19+0+3+1+10+0+8+8+0+11+12+16+5+0 = 121 rows.
**Token-count check:** 20+5+2+28+20+0+3+1+21+0+37+47+0+61+65+49+22+0 = 381 tokens. Matches
GATE A2 numbers line.

---

## TABLE 3 — ZERO / DASH-STANDING LINE ITEMS (6 rows, all on Slide 16)

All six rows below are standing reconciliation line items in the Adjusted EBITDA/PAT tables
that carry a literal "-" (dash) in one or more of the four reported periods (Quarter ended
30.06.2026, 31.03.2026, 30.06.2025; Twelve Months 31.03.2026). None of the six is dash in
*all* four periods, but per the operating rule ("never drop a nil row"), every dash cell is
enumerated rather than silently omitted.

| Row | Line | Line item | 30.06.2026 | 31.03.2026 | 30.06.2025 | TTM 31.03.2026 | Flag |
|---|---|---|---|---|---|---|---|
| R103 | 474 | (+) Employee stock option expense (non cash) | - | - | 5.7 | 10.1 | ZERO_STANDING |
| R104 | 476 | (+) Net loss on foreign currency transactions and translation | - | - | 247.3 | - | ZERO_STANDING |
| R106 | 479 | (+) Loss allowance – Capital advance (one time impact) | 49.0 | - | - | - | ZERO_STANDING |
| R107 | 480 | (+) Professional fees related to Masivian security incident remediation | 13.6 | - | - | - | ZERO_STANDING |
| R112 | 490 | (+) Exceptional Item | - | - | - | 1,358.7 | ZERO_STANDING |
| R113 | 491 | (-) Tax Impact on above | - | - | - | 166.9 | ZERO_STANDING |

---

## TABLE 4 — FOOTNOTES & FINE-PRINT DISCLAIMERS (10 items)

| Row | Slide | Line(s) | Text (verbatim or close paraphrase) | Qualifies |
|---|---|---|---|---|
| F1 | 3 | 71–83 | Full Safe Harbor / forward-looking-statements paragraph | Entire presentation — every forward-looking figure and statement in the deck |
| F2 | 11 | 327 | "(1) Top 50 countries contribute c. 86% of Q1 26-27 revenue from operations" | "Revenue for Top 50 countries by termination" chart |
| F3 | 11 | 328 | "(2) Top 150 customers - contribute c. 92% of Q1 26-27 revenue from operations" | "Revenue by customer HQ continent" chart |
| F4 | 12 | 370 | "(1) 3M FY26-27 Annualized" | Q1 26-27 column in the "Clients by Account Size" chart |
| F5 | 15 | 462 | "1. Refer Slide 15 for calculation of EBITDA (Non GAAP)" | Adj. EBITDA figures cited on Slide 15 |
| F6 | 15 | 463 | "2. Refer Slide 15 for calculation of Adj. PAT" | Adj. PAT figures cited on Slide 15 |
| F7 | 15 | 464 | "3. Non core items includes Employee stock option expense and Net loss on foreign currency transactions and translation" | "adjusted for non-core items" language in the Adj. EBITDA bullet on Slide 15 |
| F8 | 16 | 495 | "(1) EBITDA = Profit before exceptional item minus (-) Other income plus (+) Finance cost and depreciation." | EBITDA definition used throughout the reconciliation table |
| F9 | 16 | 497–499 | "Management uses the non-GAAP financial information... should not be considered a substitute for financial information presented in accordance with Ind AS, and may be different from similarly titled non-GAAP measures used by other companies." | Entire Adjusted EBITDA/PAT reconciliation table (both sub-tables) |
| F10 | 17 | 537 | "As on June 30, 2026, Employee information excludes Call2Connect" | All headcount figures on the HR Capital slide (502/281/783 total, function breakdown, 35 joined/60 left) |

---

## TABLE 5 — DROPPED-SLIDE COMPARISON (rule 3, INVESTOR PRESENTATION enumeration)

Prior-quarter ledger path supplied: **none available**. No comparison performed; flag
`NO_PRIOR_LEDGER`. This must be revisited once a Q4 FY26 (or earlier) presentation ledger
exists so any slide dropped between quarters can be flagged `DROPPED_SLIDE`.

---
