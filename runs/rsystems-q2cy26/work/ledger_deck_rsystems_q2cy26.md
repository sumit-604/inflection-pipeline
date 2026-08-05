# A2 ENUMERATOR LEDGER — RSYSTEMS Q2 CY2026 Investor Presentation Deck

Source: `/home/user/inflection-pipeline/runs/rsystems-q2cy26/work/extract_deck_rsystems_q2cy26.txt`
Doctype: presentation (16-page/16-slide deck; page_count_pdfinfo=16, formfeed_count=16)
Unit convention: Millions (₹ in M native; US$ in M parallel column, kept labelled, not converted, not summed across currencies)
OCR-flagged pages (per A1 header, line 9): 2, 4, 9, 11, 13, 16

---

## === A2 COUNT TEST ===
```
category: slides                  grep_count: 16   sweep_count: 16   match: yes
category: kpi_tiles               grep_count: 20   sweep_count: 20   match: yes
category: chart_datapoints        grep_count: 91   sweep_count: 91   match: yes  (59 text-extractable + 32 flagged NOT_EXTRACTABLE; both counted as enumerated units)
category: table_line_items        grep_count: 58   sweep_count: 58   match: yes
category: footnotes_adjustments   grep_count: 17   sweep_count: 17   match: yes
category: key_wins_items          grep_count: 5    sweep_count: 5    match: yes
category: agenda_items            grep_count: 7    sweep_count: 7    match: yes
category: strategy_award_stmts    grep_count: 8    sweep_count: 8    match: yes
gate_a2: pass
```
Reconciliation notes:
- `slides`: `grep -n "^\[page "` on the extract returns 16 markers, matching pdfinfo page_count=16 and the manual page-by-page sweep below. MATCH.
- `chart_datapoints`: raw grep on slides 5-6 combined text blocks over-matches (e.g. "6,017", "1,207", "20.1%" each hit 2-3x) because KPI-tile text and chart-bar labels for the *current* quarter share the same source line in the jumbled multi-column extraction — both are genuine, separately-enumerated disclosure units (one KPI tile row, one chart data-point row), not a duplicate. Component-level grep (per series, restricted string sets) reproduces the manual sweep exactly: quarter-trend 24, EBITDA-bridge×2 = 8, half-year-trend 6, geography 8, concentration 8, ACV 5 = 59 text-extractable, plus 32 NOT_EXTRACTABLE (utilization + DSO line charts, axis-only, no printed data labels) = 91. MATCH.
- `table_line_items`: raw grep on slide 14-15 range returns 44 (includes 2 slide titles + 2 period-header rows, which are not line items); subtracting those 4 non-item header lines gives 40, plus slide 7 (12 rows) + slide 8 (6 rows) = 58. MATCH.
- `footnotes_adjustments`: grep on `#`/`^`/`*`-prefixed lines (7: slides 9,14,15) + grep on plain-text "Adj. EBITDA is excluding…" style footnotes with no symbol prefix (10: slides 5-8) = 17. MATCH.

---

## 1. SLIDE INDEX (16 slides/pages)

| # | Title | Content type | Line range | Flags |
|---|---|---|---|---|
| 1 | Reg. 30 submission cover letter (to NSE & BSE) | text/letter | 14-63 | — |
| 2 | "Q2 CY 2026 Investor Presentation" (title) | title/photo (OCR-flagged) | 64-87 | — |
| 3 | Disclaimer | text | 88-100 | — |
| 4 | Agenda | text/list | 101-131 | — |
| 5 | Financial Performance : Q2 2026 | KPI tiles + 2 charts + footnotes | 132-170 | — |
| 6 | Financial Performance : H1 2026 | KPI tiles + 2 charts + footnotes | 171-208 | — |
| 7 | Margin & EPS Analysis : Q2 2026 | 2 tables (YoY, QoQ) + footnotes | 209-245 | — |
| 8 | Margin & EPS Analysis : H1 2026 | 1 table (H1'26/H1'25/CY25) + footnotes | 246-277 | — |
| 9 | Operations Metrics | 4 charts (geography, concentration, utilization, DSO) + footnote; OCR duplicate block present | 278-396 | NOT_EXTRACTABLE (utilization, DSO) |
| 10 | Key Wins | 5 text case studies | 397-432 | — |
| 11 | TTM ACV Bookings Excluding Renewals ($M) | 1 line chart; OCR duplicate block present | 433-489 | — |
| 12 | Summing Up And Looking Ahead | text/strategy + award bullets | 490-516 | — |
| 13 | Appendix (divider) | text/title only (OCR-flagged) | 517-533 | — |
| 14 | Financial Performance - Contribution Analysis - Q2 2026 | table (20 line items x 3 periods x ₹M/US$M) + footnotes | 534-568 | — |
| 15 | Financial Performance - Contribution Analysis - H1 2026 | table (20 line items x 2 periods x ₹M/US$M) + footnotes | 569-603 | — |
| 16 | "Thank You" / closing, tagline "Engineered Always" (OCR) | text/photo (OCR-flagged) | 604-615 | — |

DROPPED_SLIDE check: prior-quarter ledger not supplied (PRIOR_LEDGER_PATH not injected) — comparison N/A, not a gate failure.

---

## 2. COVER LETTER / DISCLAIMER / STRUCTURAL SLIDES (non-numeric content)

| Slide | Item | Line | Flag |
|---|---|---|---|
| 1 | Recipient: Managing Director, NSE (Exchange Plaza, BKC) | 18-22 | — |
| 1 | Recipient: General Manager, BSE (Phiroze Jeejeebhoy Towers) | 18-22 | — |
| 1 | Subject: Submission of Presentation for Analysts/Investors Meeting | 28 | — |
| 1 | Reference: intimation dated July 28, 2026 of Investor/Analyst call | 30-32 | — |
| 1 | Regulation cited: SEBI (LODR) Regulations 2015, Reg. 30 | 34-37 | — |
| 1 | Meeting date/time: Wednesday, August 05, 2026, 10:00 AM (IST) | 31-36 | — |
| 1 | Digital signature block: Piyush Jain, Company Secretary & Compliance Officer, signed 2026.08.04 21:37:13 +05'30' | 46-53 | flag: signature dated 1 day before the 10:00 AM Aug 5 call — routine pre-filing, not a same-day-of-meeting timestamp anomaly |
| 1 | Corporate/registered office address block, CIN L74899DL1993PLC053579 | 58-62 | — |
| 3 | Disclaimer: forward-looking-statement caution paragraph | 91-94 | — |
| 13 | "Appendix" divider title only, no data | 518 | — |
| 16 | "THANK YOU!" closing text | 605-606 | — |
| 16 | Tagline "…gineered Always" (OCR-garbled, likely "Engineered Always") | 611-612 | NOT_EXTRACTABLE (OCR quality) |

Headcount: NOT FOUND anywhere in deck (grep for "headcount"/"employee" = 0 hits). No headcount slide/KPI present this quarter.
Balance-sheet / cash figures: NOT FOUND anywhere in deck (grep for "balance sheet"/"cash and cash equivalent"/"net cash"/"total assets"/"total equity"/"borrowings" = 0 hits). Deck is P&L/operating-metrics only; no balance-sheet or cash-position slide.
Explicit forward numeric guidance (revenue/margin target for a future period): NOT FOUND — slide 12 contains only qualitative outlook language (see §7), no numeric guidance figure.

---

## 3. AGENDA ITEMS (Slide 4) — 7 items

| # | Item | Line |
|---|---|---|
| 1 | Financial Performance Q2 & H1 2026 | 104 |
| 2 | Margin & EPS Analysis Q2 & H1 2026 | 105 |
| 3 | Adj. EBITDA & Adj. Net Profit Trend | 106 |
| 4 | Operations Metrics | 107 |
| 5 | Key Wins Q2 2026 | 108 |
| 6 | TTM ACV Bookings Excluding Renewals | 109 |
| 7 | Summing Up And Looking Ahead | 110 |

---

## 4. KPI TILES — Slides 5 & 6 (20 items)

### Slide 5 — Financial Performance : Q2 2026 (10 tiles)
| Label | Value | Line |
|---|---|---|
| Revenue | INR 6,017M ($63.6M) | 139 |
| Revenue YoY | 30.2% | 141 |
| Adj. EBITDA | INR 1,207M ($12.8M) | 145 |
| Adj. EBITDA % | 20.1% | 146 |
| Adj. EBITDA YoY | 51.4% | 148 |
| Adj. Net Profit | INR 629M ($6.6M) | 153 |
| Adj. Net Profit % | 10.5% | 154 |
| Adj. Net Profit YoY | 35.4% | 155 |
| Adj. EPS | INR 5.3 | 158 |
| Adj. EPS YoY | 35.3% | 159 |

### Slide 6 — Financial Performance : H1 2026 (10 tiles)
| Label | Value | Line |
|---|---|---|
| Revenue | INR 11,765M ($126.4M) | 178 |
| Revenue YoY | 30.1% | 180 |
| Adj. EBITDA | INR 2,364M ($25.4M) | 184 |
| Adj. EBITDA % | 20.1% | 185 |
| Adj. EBITDA YoY | 51.0% | 186 |
| Adj. Net Profit | INR 1387M ($14.9M) | 190 |
| Adj. Net Profit % | 11.8% | 191 |
| Adj. Net Profit YoY | 54.4% | 192 |
| Adj. EPS | INR 11.7 | 194 |
| Adj. EPS YoY | 54.3% | 196 |

---

## 5. CHART DATA-POINTS / SERIES (91 items: 59 extractable + 32 NOT_EXTRACTABLE)

### Slide 5 — "Quarter Trend (INR M)" (24 pts) — lines 136-152
Quarters: Q3'24, Q4'24, Q1'25, Q2'25, Q3'25, Q4'25, Q1'26, Q2'26 (8 periods x 3 series)
| Series | Q3'24 | Q4'24 | Q1'25 | Q2'25 | Q3'25 | Q4'25 | Q1'26 | Q2'26 | Line |
|---|---|---|---|---|---|---|---|---|---|
| Revenue (INR M) | 4,441 | 4,490 | 4,425 | 4,620 | 4,986 | 5,551 | 5,748 | 6,017 | 140-143 |
| Adj. EBITDA (INR M) | 796 | 801 | 768 | 797 | 844 | 1,017 | 1,157 | 1,207 | 150 |
| Adj. EBITDA % | 17.9% | 17.8% | 17.4% | 17.3% | 16.9% | 18.3% | 20.1% | 20.1% | 137,139,140 |

### Slide 5 — "Adj. EBITDA Bridge (INR M)" (4 pts) — lines 156-166
| Step | Value | Line |
|---|---|---|
| Q1'26 Adj. EBITDA (start) | 1,157 | 158 |
| Rupee depreciation (increase) | +98 | 158 |
| Standard operations (decrease) | -47 | 159 |
| Q2'26 Adj. EBITDA (end) | 1,207 | 158 |

### Slide 6 — "Half Year Trend (INR M)" (6 pts) — lines 174-191
| Series | H1'25 | H1'26 | Line |
|---|---|---|---|
| Revenue (INR M) | 9,045 | 11,765 | 178,181 |
| Adj. EBITDA (INR M) | 1,566 | 2,364 | 184,188 |
| Adj. EBITDA % | 17.3% | 20.1% | 176,179,185 |

### Slide 6 — "Adj. EBITDA Bridge (INR M)" (4 pts) — lines 193-204
| Step | Value | Line |
|---|---|---|
| H1'25 Adj. EBITDA (start) | 1,566 | 197 |
| Rupee depreciation (increase) | +552 | 196 |
| Standard operations (increase) | +247 | 195 |
| H1'26 Adj. EBITDA (end) | 2,364 | 195 |

### Slide 9 — "Revenue by Geography (%)" (8 pts) — lines 281-296
| Region | Q1 2026 | Q2 2026 | Line |
|---|---|---|---|
| Americas | 69.3% | 71.5% | 283 |
| APAC | 17.5% | 15.3% | 289 |
| Europe | 9.6% | 9.7% | 290 |
| MEA | 3.6% | 3.6% | 291 |

### Slide 9 — "Client Concentration (%)" (8 pts) — lines 281-296
| Bucket | Q1 2026 | Q2 2026 | Line |
|---|---|---|---|
| Top Client | 5.8% | 6.0% | 289 |
| Top 3 Clients | 11.5% | 12.1% | 287 |
| Top 5 Clients | 16.0% | 17.0% | 285 |
| Top 10 Clients | 24.0% | 24.4% | 283 |

### Slide 9 — "Utilization (%)" (16 pts, ALL NOT_EXTRACTABLE) — lines 298-310
Two series ("Actual Utilization %", "Desired Utilization %") plotted across 8 quarters (Q3 2024-Q2 2026). Only y-axis gridlines (78%-85%) and x-axis quarter labels are text-extractable; no per-point data labels are present in either the primary text layer or the OCR pass. Recorded per A2 rule as explicit not-extractable rows rather than estimated.
| Series | Quarters (8) | Status | Line |
|---|---|---|---|
| Actual Utilization % | Q3'24…Q2'26 | NOT_EXTRACTABLE — axis-only, no data labels | 299-309 |
| Desired Utilization % | Q3'24…Q2'26 | NOT_EXTRACTABLE — axis-only, no data labels | 299-309 |

### Slide 9 — "DSO (Days) #" (16 pts, ALL NOT_EXTRACTABLE) — lines 298-312
Two series ("DSO (Billed)", "DSO (Billed & Unbilled)") plotted across the same 8 quarters. Only y-axis gridlines (0-80) are text-extractable; no per-point data labels present.
| Series | Quarters (8) | Status | Line |
|---|---|---|---|
| DSO (Billed) | Q3'24…Q2'26 | NOT_EXTRACTABLE — axis-only, no data labels | 300-309 |
| DSO (Billed & Unbilled) | Q3'24…Q2'26 | NOT_EXTRACTABLE — axis-only, no data labels | 300-309 |

### Slide 11 — "TTM ACV Bookings Excluding Renewals ($M)" (5 pts) — lines 436-450
| Quarter | ACV ($M) | Line |
|---|---|---|
| Q2-2025 | 74.0 | 446 |
| Q3-2025 | 74.0 | 446 |
| Q4-2025 | 76.5 | 444 |
| Q1-2026 | 82.3 | 440 |
| Q2-2026 | 82.9 | 440 |

---

## 6. FINANCIAL TABLE LINE ITEMS (58 rows)

### Slide 7 — Margin & EPS Analysis : Q2 2026 — YoY table (6 rows) — lines 216-231
| Line item | Q2 2026 | Q2 2025 | YoY | Line |
|---|---|---|---|---|
| Revenue | 6,017 | 4,620 | 30.2% | 216 |
| Adj. EBITDA | 1,207 | 797 | 51.4% | 219 |
| Adj. EBITDA % | 20.1% | 17.3% | 281bps | 222 |
| Adj. Net Profit | 629 | 464 | 35.4% | 225 |
| Adj. Net Profit % | 10.5% | 10.1% | 40bps | 228 |
| Adj. Basic EPS | 5.3 | 3.9 | 35.3% | 231 |

### Slide 7 — Margin & EPS Analysis : Q2 2026 — QoQ table (6 rows) — lines 216-231
| Line item | Q2 2026 | Q1 2026 | QoQ | Line |
|---|---|---|---|---|
| Revenue | 6,017 | 5,748 | 4.7% | 216 |
| Adj. EBITDA | 1,207 | 1,157 | 4.4% | 219 |
| Adj. EBITDA % | 20.1% | 20.1% | (6bps) | 222 |
| Adj. Net Profit | 629 | 758 | (17.1)% | 225 |
| Adj. Net Profit % | 10.5% | 13.2% | (274bps) | 228 |
| Adj. Basic EPS | 5.3 | 6.4 | (17.1)% | 231 |

### Slide 8 — Margin & EPS Analysis : H1 2026 (6 rows) — lines 253-264
| Line item | H1 2026 | H1 2025 | Growth% YoY | CY 2025 | Line |
|---|---|---|---|---|---|
| Revenue | 11,765 | 9,045 | 30.1% | 19,582 | 253 |
| Adj. EBITDA | 2,364 | 1,566 | 51.0% | 3,427 | 255 |
| Adj. EBITDA % | 20.1% | 17.3% | 279bps | 17.5% | 257 |
| Adj. Net Profit | 1,387 | 898 | 54.4% | 1,936 | 259 |
| Adj. Net Profit % | 11.8% | 9.9% | 186bps | 9.9% | 262 |
| Adj. Basic EPS | 11.7 | 7.6 | 54.3% | 16.4 | 264 |

### Slide 14 — Contribution Analysis Q2 2026, Un-audited (20 rows) — lines 539-558
Columns: Q2 2026 (₹M, US$M) / Q1 2026 (₹M, US$M) / Q2 2025 (₹M, US$M)
| Line item | Q2'26 ₹M | Q2'26 US$M | Q1'26 ₹M | Q1'26 US$M | Q2'25 ₹M | Q2'25 US$M | Line |
|---|---|---|---|---|---|---|---|
| Revenues | 6,017.0 | 63.6 | 5,747.7 | 62.8 | 4,620.1 | 54.0 | 539 |
| Cost of revenues | 3,656.8 | 38.6 | 3,677.1 | 40.2 | 2,956.7 | 34.6 | 540 |
| Gross margin | 2,360.2 | 25.0 | 2,070.6 | 22.6 | 1,663.4 | 19.4 | 541 |
| % of Revenue (gross margin) | 39.2% | — | 36.0% | — | 36.0% | — | 542 |
| SG&A Expenses | 1,152.7 | 12.2 | 914.0 | 10.0 | 866.0 | 10.1 | 543 |
| % of Revenue (SG&A) | 19.2% | — | 15.9% | — | 18.7% | — | 544 |
| Adj. EBITDA | 1,207.5 | 12.8 | 1,156.6 | 12.6 | 797.4 | 9.3 | 545 |
| % of Revenue (Adj. EBITDA) | 20.1% | — | 20.1% | — | 17.3% | — | 546 |
| Cost of RSUs | 62.4 | 0.7 | 64.1 | 0.7 | 48.7 | 0.5 | 547 |
| EBITDA | 1,145.1 | 12.1 | 1,092.5 | 11.9 | 748.7 | 8.8 | 548 |
| % of Revenue (EBITDA) | 19.0% | — | 19.0% | — | 16.2% | — | 549 |
| Depreciation and amortization | 220.4 | 2.3 | 215.1 | 2.3 | 158.4 | 1.9 | 550 |
| EBIT before non-recurring cost | 924.7 | 9.8 | 877.4 | 9.6 | 590.3 | 6.9 | 551 |
| Non-recurring Income/(expense) # | (16.1) | (0.2) | (15.9) | (0.2) | 409.3 | 4.7 | 552 |
| EBIT | 908.6 | 9.6 | 861.5 | 9.4 | 999.6 | 11.6 | 553 |
| Interest expense | (94.8) | (1.0) | (95.9) | (1.0) | (21.4) | (0.3) | 554 |
| Other income (net) * | (8.7) | (0.1) | 130.7 | 1.4 | 13.6 | 0.2 | 555 |
| Income before income tax | 805.1 | 8.5 | 896.3 | 9.8 | 991.8 | 11.5 | 556 |
| Tax expense | 249.4 | 2.6 | 242.2 | 2.6 | 233.3 | 2.7 | 557 |
| Net profit ^ | 555.7 | 5.9 | 654.1 | 7.2 | 758.5 | 8.8 | 558 |

### Slide 15 — Contribution Analysis H1 2026, Un-audited (20 rows) — lines 574-593
Columns: H1 2026 (₹M, US$M) / H1 2025 (₹M, US$M)
| Line item | H1'26 ₹M | H1'26 US$M | H1'25 ₹M | H1'25 US$M | Line |
|---|---|---|---|---|---|
| Revenues | 11,764.7 | 126.4 | 9,044.8 | 105.1 | 574 |
| Cost of revenues | 7,333.9 | 78.8 | 5,757.2 | 66.9 | 575 |
| Gross margin | 4,430.8 | 47.6 | 3,287.6 | 38.2 | 576 |
| % of Revenue (gross margin) | 37.7% | — | 36.3% | — | 577 |
| SG&A Expenses | 2,066.7 | 22.2 | 1,722.1 | 20.0 | 578 |
| % of Revenue (SG&A) | 17.6% | — | 19.0% | — | 579 |
| Adj. EBITDA | 2,364.1 | 25.4 | 1,565.5 | 18.2 | 580 |
| % of Revenue (Adj. EBITDA) | 20.1% | — | 17.3% | — | 581 |
| Cost of RSUs | 126.5 | 1.4 | 111.2 | 1.3 | 582 |
| EBITDA | 2,237.6 | 24.0 | 1,454.3 | 16.9 | 583 |
| % of Revenue (EBITDA) | 19.0% | — | 16.1% | — | 584 |
| Depreciation and amortization | 435.4 | 4.7 | 304.5 | 3.5 | 585 |
| EBIT before non-recurring cost | 1,802.2 | 19.3 | 1,149.8 | 13.4 | 586 |
| Non-recurring Income/(expense) # | (32.1) | (0.3) | 409.4 | 4.7 | 587 |
| EBIT | 1,770.1 | 19.0 | 1,559.2 | 18.1 | 588 |
| Interest expense | (190.7) | (2.0) | (36.3) | (0.4) | 589 |
| Other income (net) * | 122.0 | 1.3 | 36.2 | 0.4 | 590 |
| Income before income tax | 1,701.4 | 18.3 | 1,559.1 | 18.1 | 591 |
| Tax expense | 491.6 | 5.3 | 414.6 | 4.8 | 592 |
| Net profit ^ | 1,209.8 | 13.0 | 1,144.5 | 13.3 | 593 |

ZERO_STANDING check: every line item above carries a nonzero (or negative) value in every period shown; no zero/nil/dash standing line items exist in these tables this quarter. zero_standing count = 0.

---

## 7. FOOTNOTES / ADJUSTMENT DEFINITIONS (17 items)

| Slide | # | Text (verbatim or truncated) | Line |
|---|---|---|---|
| 5 | 1 | "Adj. EBITDA is excluding RSUs expenses, non-recurring costs" | 163 |
| 5 | 2 | "Adj. Net Profit and Adj. Basic EPS is excluding RSUs expense and non-recurring items net of tax" | 165-166 |
| 6 | 1 | "Adj. EBITDA is excluding RSUs expenses, non-recurring costs" | 201 |
| 6 | 2 | "Adj. Net Profit and Adj. Basic EPS is excluding RSUs expense and non-recurring items net of tax" | 203-204 |
| 7 | 1 | "Adj. EBITDA is excluding RSUs expenses, non-recurring costs" | 235 |
| 7 | 2 | "Adj. Net Profit and Adj. Basic EPS is excluding RSUs expense and non-recurring items net of tax" | 236 |
| 7 | 3 | "Adj. Net Profit and Adj. Basic EPS further reflect the impact of the Company's adoption of cash flow hedge accounting under Ind AS 109, effective 1 January 2026. As a result, other income for Q1 2026 was higher by ₹180.47 million…" | 237-239 |
| 8 | 1 | "Adj. EBITDA is excluding RSUs expenses, non-recurring costs" | 269 |
| 8 | 2 | "Adj. Net Profit and Adj. Basic EPS is excluding RSUs expense and non-recurring items net of tax" | 270 |
| 8 | 3 | "Adj. Net Profit and Adj. Basic EPS further reflect the impact of the Company's adoption of cash flow hedge accounting under Ind AS 109, effective 1 January 2026." | 271 |
| 9 | 1 (#) | "Basis Trailing Twelve months and excluding the new acquisition of Novigo" (applies to DSO chart; duplicated verbatim in OCR block at line 390) | 312 |
| 14 | 1 (#) | "Q2 2026 and Q1 2026 consists of severance payment and Q2 2025 consists of profit on sale of land, building and certain other assets located at Company's NOIDA office as offset by finding fees paid for Chief Revenue Officer." | 560 |
| 14 | 2 (^) | "Adjusted Net Profit after tax amounting to Rs. 628.7 M (US$ 6.6 M) for Q2 2026, Rs. 758.1 M (US$ 8.3 M) for Q1 2026 and Rs. 464.4 M (US$ 5.4 M) for Q2 2025." | 562 |
| 14 | 3 (*) | "Effective 1 January 2026, the Company designated certain foreign currency forward contracts as cash flow hedges under Ind AS 109…" | 563 |
| 15 | 1 (#) | "Six months ended Jun 30, 2026, consists of severance payment and six months ended Jun 30, 2025, consists of profit on sale of land, building and certain other assets located at Company's NOIDA office as offset by finding fees paid for Chief Revenue Officer." | 595 |
| 15 | 2 (^) | "Adjusted Net Profit after tax for six months ended June 30, 2026, amounting to Rs. 1,386.84 mn (US$ 14.9 mn) as against Rs. 898.10 mn (US$ 10.4 mn) for the same period last year." | 597 |
| 15 | 3 (*) | "Effective 1 January 2026, the Company designated certain foreign currency forward contracts as cash flow hedges under Ind AS 109…" | 598 |

Note: slide 14 footnote ^ value (Rs. 628.7M / US$6.6M for Q2 2026) matches the headline Adj. Net Profit KPI tile on slide 5 (INR 629M / $6.6M) within rounding — cross-check is A3/A4 scope, flagged here only as an enumerated pair for reconciliation (line 153 vs line 562).

---

## 8. KEY WINS (Slide 10) — 5 items — lines 397-432

| # | Client type / deal | Line (start) |
|---|---|---|
| 1 | Global telecommunications and media company — advanced analytics, data science, intelligence solutions | 401 |
| 2 | U.S. small business lender — Global Capability Center (GCC): AI Product Engineering, Software Engineering, Digital Operations | 407 |
| 3 | Global insurance and financial services provider — HNW Reimagine initiative, AI-powered quality engineering | 412/414 |
| 4 | Global financial services / market access provider — Microsoft Dynamics 365 Retail transformation | 419 |
| 5 | U.S.-based AdTech company — core advertising platform modernization | 424 |

---

## 9. STRATEGY / OUTLOOK / AWARD STATEMENTS (Slide 12) — 8 items — lines 490-516

| # | Type | Statement | Line |
|---|---|---|---|
| 1 | Award/recognition | "R Systems was recognized as a Horizon 2 GCC Accelerator in HFS' Horizons: GCC Services, 2026 Report" | 493-494 |
| 2 | Award sub-detail | "Validation of our AI-first GCC model and platform-led delivery" | 495 |
| 3 | Award sub-detail | "Our portfolio of proprietary accelerators have been recognized as key differentiators enabling GCCs in this transformation" | 496-497 |
| 4 | Strategy claim | "Agentic Business Operations seeing traction" | 498 |
| 5 | Strategy claim | "Modernization continues to be big theme" | 499 |
| 6 | Trend (2026 outlook) | "Organizations are beginning to look at the cost of running AI as an important factor; hence turning towards expert product engineering providers like RSI to architect AI efficient end to end systems" | 504-506 |
| 7 | Trend (2026 outlook) | "Legacy Modernization continues to be a very large total addressable market (TAM) across legacy code bases, legacy data estates and reporting landscapes" | 507-508 |
| 8 | Trend (2026 outlook) | "Enterprises are seeing Engineering Velocity as key differentiator for achieving return on investment (ROI) from AI Initiatives" | 509-510 |

No numeric guidance figure (revenue/margin target for a future period) is stated anywhere on slide 12 or elsewhere in the deck — NOT FOUND.

---

## 10. CAPABILITY / ACCELERATOR / AWARD NAMES

| Name | Context | Line |
|---|---|---|
| "Horizon 2 GCC Accelerator" | HFS Horizons: GCC Services, 2026 Report classification | 493-494 |
| "HFS Horizons: GCC Services, 2026 Report" | third-party analyst report name | 493-494 |
| "Agentic Business Operations" | named capability/theme | 498 |
| "AI-first GCC model" | named platform/delivery model | 495 |

No named proprietary accelerator products are individually listed by name in this deck (only the generic phrase "portfolio of proprietary accelerators," line 496) — NOT FOUND at the individual-product-name level.

---

## Summary

- Total slides enumerated: 16 / 16 (100% page coverage, matches A1 header)
- Total discrete enumerated disclosure units across all categories: 16 (slides) + 20 (KPI tiles) + 91 (chart datapoints, 59 extractable + 32 flagged not-extractable) + 58 (table line items) + 17 (footnotes) + 5 (key wins) + 7 (agenda items) + 8 (strategy/award statements) + 12 (structural/cover-letter items, §2) + 4 (capability/award names, §10) = 238 rows
- GATE A2: PASS — every category's grep count reconciles to its manual sweep count (see §Reconciliation notes above)
- Explicit NOT FOUND items flagged for A3/A4 attention: headcount, balance-sheet/cash figures, numeric forward guidance, named individual accelerator products, utilization chart data-labels, DSO chart data-labels
- Output ledger path: `/home/user/inflection-pipeline/runs/rsystems-q2cy26/work/ledger_deck_rsystems_q2cy26.md`

```yaml
stage: A2-enumerator
company: "R Systems International Limited"
ticker: "RSYSTEMS"
quarter: "Q2 CY2026"
doctype: "presentation"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/rsystems-q2cy26/work/ledger_deck_rsystems_q2cy26.md"
counts:
  slides: 16
  slide_numbers: 16
  kpi_tiles: 20
  chart_datapoints: 91
  chart_datapoints_extractable: 59
  chart_datapoints_not_extractable: 32
  table_line_items: 58
  zero_standing: 0
  footnotes_adjustments: 17
  key_wins_items: 5
  agenda_items: 7
  strategy_award_statements: 8
  capability_award_names: 4
flags_raised: [NOT_EXTRACTABLE, ZERO_STANDING]
gate_a2: pass
mismatch_note: ""
```
