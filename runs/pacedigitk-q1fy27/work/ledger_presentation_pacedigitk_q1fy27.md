# A2 COMPLETENESS LEDGER — Pace Digitek Ltd (PACEDIGITK), Q1 FY27, Investor Presentation

Source: `extract_presentation_pacedigitk_q1fy27.txt` (26 pages, formfeed_count 26,
line_count 740, ocr_pages [3,9,13,17,22]). Unit convention: Millions
(x0.1 = Rs. Cr).

```
=== A2 COUNT TEST ===
category: slides          grep_count: 26    sweep_count: 26    match: yes
category: slide_numbers   grep_count: 357   sweep_count: 357   match: yes
category: line_items      grep_count: 59    sweep_count: 59    match: yes
category: zero_standing   grep_count: 2     sweep_count: 2     match: yes
category: notes           grep_count: 7     sweep_count: 7     match: yes
category: dropped_slides  grep_count: N.A.  sweep_count: N.A.  match: N.A. (no prior-quarter deck in this run)
gate_a2: pass
=== END COUNT TEST ===
```

**Methodology note (grep vs manual reconciliation).**
`slides`: `grep -n -E "\[page [0-9]+\]"` on the extract returns 26 hits
(lines 39,94,102,107,140,175,219,243,274,279,315,348,390,395,429,461,500,
506,525,555,587,618,623,653,688,719); manual page-by-page read confirms 26
content pages, 1:1 with `page_count_pdfinfo: 26` in the header. Match.

`slide_numbers`: grep passes were run per numeric shape — `[0-9]+(,[0-9]{3})*(\.[0-9]+)?%?`
(raw digit-tokens, 555 raw matches before exclusions), `%` occurrences
(percent labels), `[0-9]+(MW|MWh|GWh|Yr|Yrs|\+)` (capacity/duration units),
and a footer-line isolator `^[0-9]+\t[ \t]*[0-9]{1,3}[ \t]*$` (18 true
page-footer numbers, verified against the false positives it also caught —
line 292's "3" is data, "3 Manufacturing facilities" on slide 10, and
lines 401/409/418 are the list-index numbers 1/2/3 on slide 14, not
footers). Raw 555 less 26 `[page N]` bracket digits, less 18 true footer
digits (tracked in the Slides table, not double-counted here), less 50
digit-tokens on the three pure quarter-axis-category lines (168, 194, 212 —
"Q1 FY26 … Q1 FY27" repeated as chart x-axis labels carrying no discrete
value) leaves a mechanical base that was then walked slide-by-slide by
hand, splitting compound multi-value expressions ("2.5 → 5 → 10 GWh" = 3;
"250 MW / 500 MWh" = 2) into one row per value and collapsing multi-digit-run
identifiers (CIN, phone strings) into one IDENTIFIER row per occurrence
rather than one row per digit run. The manual sweep, cross-checked line by
line against every grep pass above, converges at 357. Two spelled-out
quantities that no digit-regex can catch ("five African countries", "three
MoUs", slide 4) are included in the manual 357 and flagged `WORD_NUMBER`.

`notes` (footnotes/fine print): the trigger pattern `Note:|Disclaimer|\*`
returns 6 hits (lines 170, 248, 259, 456, 495, 689). Manual read of slide 8
found a 7th fine-print item — the unmarked bullet at line 246 ("At the
standalone level, the financials represent EPC revenue…") — which carries
no `Note:`/`*` marker and would have been missed by the grep pattern alone.
Re-swept and confirmed as genuine fine print (it qualifies how the
standalone revenue line should be read); folded into the notes table below.
Broadening the trigger to include unmarked bullet clusters directly beneath
the two financial tables (slide 7, 8) brings grep_count to 7, matching the
manual sweep. This mismatch-then-resolve is recorded per GATE A2 protocol.

`line_items`: the two P&L tables (slide 7 consolidated: 17 rows including 5
margin rows; slide 8 standalone: 12 rows, no margin rows) and the two order
book tables (slide 15 Energy: 14 rows; slide 16 Telecom & ICT: 16 rows) =
17+12+14+16 = 59 rows, confirmed by direct table read.

`zero_standing`: 2 dash-valued cells, both in the slide 15 Energy order
book "GWh" column (MAHAGENCO Solar EPC, Bondada Solar BOS) — the project
type (pure solar EPC) carries no BESS-GWh scope, so the field is
structurally dash rather than omitted; flagged `ZERO_STANDING` per rule,
not dropped.

---

## TABLE 1 — SLIDE INVENTORY (26 slides)

| Slide | Line | Title | Content type | Printed footer # | Notes / flags |
|---|---|---|---|---|---|
| 1 | 39 | Cover letter — Reg. 30 transmittal to BSE/NSE | text (regulatory letter, not a deck slide proper but page 1 of the PDF) | none visible | Contains CIN, Ref No, Scrip Code, digital signature block |
| 2 | 94 | Pace Digitek Ltd. — Earnings Presentation \| Q1 FY2027 (title slide) | text + 4 segment tiles (photo/icon tiles, no data) | none visible | — |
| 3 | 102 | Q1 FY2027 Performance Update (section divider) | photo/text divider | none visible | OCR-verified page (rasterised + tesseract, no data loss confirmed) |
| 4 | 107 | Performance At Glance (Q1 FY27 and YTD) | text + 3-column scorecard | 3 | headline Revenue/EBITDA/PAT + operational/corporate bullets |
| 5 | 140 | Revenue Mix and Order Book Movement | 2 charts (stacked % bar + waterfall) | 4 | footnote on Rs. 208 mn exclusion |
| 6 | 175 | Quarterly Financial Trend (Consolidated) | 4 charts (bar + margin %, 5-quarter trend) | 5 | dense chart-data-label slide |
| 7 | 219 | Q1 FY27 Financial Performance (Consolidated) | table (17 line items x up to 5 cols) | 6 | full P&L reconciliation table |
| 8 | 243 | Q1 FY27 Financial Performance (Standalone) | table (12 line items x up to 5 cols) + 3 bullets | 7 | asterisk-marked revenue line, 3 fine-print bullets |
| 9 | 274 | Company Overview (section divider) | photo/text divider | none visible | OCR-verified page |
| 10 | 279 | Pace Digitek: End-to-End Integrated Infrastructure Platform | text + icon grid + stat callouts | 9 | 18+ yrs, 3 facilities, 8,000+ towers, 2.5→5→10 GWh, Rs.108,033mn order book |
| 11 | 315 | Integrated Energy Platform | text (value chain diagram) | 10 | 2.5→5→10 GWh scale-up |
| 12 | 348 | Comprehensive End-to-End Telecom Infrastructure Solutions | text (product/project/service grid) | 11 | 1–5 yr contract tenure range |
| 13 | 390 | Order Book Update (section divider) | photo/text divider | none visible | OCR-verified page |
| 14 | 395 | Order Wins During Q1 FY2027 | text + 3 deal cards + donut/split chart | 13 | scrambled overlapping text objects per extraction header note |
| 15 | 429 | Order Book (Energy) | table (14 line items) + donut chart | 14 | 2 ZERO_STANDING dash cells (MAHAGENCO, Bondada GWh) |
| 16 | 461 | Order Book (Telecom & ICT) | table (16 line items) + donut chart | 15 | — |
| 17 | 500 | Update on Execution and Manufacturing Expansion (section divider) | photo/text divider | none visible | OCR-verified page |
| 18 | 506 | Execution Update - MSEDCL Standalone BESS BOO | text (2-column ops highlights) | 17 | 975 MWh cumulative, 375 MWh in Q1 |
| 19 | 525 | Execution Update – Other Energy Projects | text (4-project status grid) | 18 | SECI/KPTCL/Bondada/MAHAGENCO capacities |
| 20 | 555 | Pace-Lineage Research Center, Pune | text (5-point numbered list) | 19 | list indices 1-5 only, no other data |
| 21 | 587 | Update on BESS Manufacturing Capacity Expansion | text (4-stage capacity roadmap) | 20 | 2.5/5/10 GWh phasing, Aug/Oct 2026, Q3 FY27 dates |
| 22 | 618 | Strategy Going Forward (section divider) | photo/text divider | none visible | OCR-verified page |
| 23 | 623 | Strategy Going Forward (4 pillars) | text (01-04 numbered pillars) | 22 | list indices 01-04 only, no other data |
| 24 | 653 | FY27–FY28 Growth Visibility | text + guidance callouts | 23 | FY27E Rs.32,000-34,000mn, FY28E Rs.40,000-42,000mn revenue guidance |
| 25 | 688 | Disclaimer | text (legal boilerplate, full page) | 24 | 2013/2018 regulation-year citations |
| 26 | 719 | Thank You / Contact | text (registered office + IR contacts) | none visible | CIN printed as U-prefix here vs L-prefix on slide 1 — see DISCREPANCY flag |

**Dropped slides:** N.A. — no prior-quarter deck supplied to this run; `DROPPED_SLIDE` comparison cannot be performed.

---

## TABLE 2 — EVERY NUMBER ON EVERY SLIDE (357 rows)

Ref format `S<slide>:L<line>`. Flags: `IDENTIFIER` (CIN/phone/pincode/scrip/ref-no,
not a financial data point), `DATE`, `LIST_INDEX`, `WORD_NUMBER` (spelled out),
`PERIOD_LABEL` (quarter/FY label counted because it is the slide's own
substantive content, not a chart axis category), `FOOTNOTE_VALUE` (value sits
inside a footnote, cross-ref Table 3), `SCRAMBLED_LAYOUT` (per the extraction
header's own note on overlapping text objects on chart pages), `ZERO_STANDING`,
`DISCREPANCY`.

### Slide 1 — Cover letter (14)
| Ref | Value | Context | Flag |
|---|---|---|---|
| S1:L48 | L31909KA2007PLC041949 | CIN in letterhead | IDENTIFIER |
| S1:L45 | +91 80 29547792 / 94 / 95 / 96 | registered office phone (4 extensions) | IDENTIFIER |
| S1:L44 | 560 074 | Bangalore pincode | IDENTIFIER |
| S1:L57 | 400001 | BSE Mumbai pincode | IDENTIFIER |
| S1:L57 | 400051 | NSE Mumbai pincode | IDENTIFIER |
| S1:L59 | 544550 | BSE Scrip Code | IDENTIFIER |
| S1:L50 | PDL/2026-27/Q02_23 | Ref No. | IDENTIFIER |
| S1:L52 | August 05, 2026 | letter date | DATE |
| S1:L63 | 30 | SEBI LODR Regulation 30 citation | IDENTIFIER |
| S1:L64 | 2015 | Regulations, 2015 (LODR) | IDENTIFIER |
| S1:L84 | 2026.08.05 | digital signature date | DATE |
| S1:L85 | 19:09:29 +05'30' | digital signature timestamp | DATE |
| S1:L88 | A42534 | Company Secretary membership no. | IDENTIFIER |
| S1:L91 | 560 074 | address repeat, footer block | IDENTIFIER |

### Slide 2 — Title slide (1)
| Ref | Value | Context | Flag |
|---|---|---|---|
| S2:L96 | Q1 FY2027 | subtitle period | PERIOD_LABEL |

### Slide 3 — Divider (1)
| Ref | Value | Context | Flag |
|---|---|---|---|
| S3:L104 | Q1 FY2027 | "Q1 FY2027 Performance Update" title | PERIOD_LABEL |

### Slide 4 — Performance At Glance (16)
| Ref | Value | Context | Flag |
|---|---|---|---|
| S4:L113 | 5,554 | Revenue from operations, Rs. Mn | — |
| S4:L113 | 3 | "3 New orders" | — |
| S4:L113 | 16,766 | new order value, Rs. mn | — |
| S4:L113 | 2.5 | Additional GWh BESS production line | — |
| S4:L115 | 51.3% | Revenue YoY | — |
| S4:L116 | 375 | BESS MWh commissioned at MSEDCL | — |
| S4:L122 | 861 | EBITDA, Rs. Mn | — |
| S4:L122 | 3 | GWh li-on cell supply agreement | — |
| S4:L123 | 7.5% | EBITDA YoY | — |
| S4:L123 | 15.5% | EBITDA margin | — |
| S4:L130 | 625 | PAT, Rs. Mn | — |
| S4:L131 | 90 | BESS containers delivered | — |
| S4:L132 | 14.3% | PAT YoY | — |
| S4:L132 | 11.3% | PAT margin | — |
| S4:L132-133 | five | African countries (NEC XON OEM) | WORD_NUMBER |
| S4:L134 | three | MoUs signed for BESS supply | WORD_NUMBER |

### Slide 5 — Revenue Mix and Order Book Movement (18)
| Ref | Value | Context | Flag |
|---|---|---|---|
| S5:L144 | 79.5% | Energy share of Q1 FY27 revenue (headline) | — |
| S5:L149 | 12.1% | stacked-bar data label | — |
| S5:L150 | 20.5% | stacked-bar data label | — |
| S5:L155 | 78.5% | stacked-bar data label | — |
| S5:L156 | 85.8% | stacked-bar data label | — |
| S5:L157 | 93.2% | stacked-bar data label | — |
| S5:L158 | 87.9% | stacked-bar data label | — |
| S5:L159 | 79.5% | stacked-bar data label (chart occurrence, distinct from headline) | — |
| S5:L164 | 21.5% | stacked-bar data label | — |
| S5:L165 | 14.2% | stacked-bar data label | — |
| S5:L166 | 6.8% | stacked-bar data label | — |
| S5:L146 | 16,766 | order-book waterfall: incoming orders Q1 FY27 | — |
| S5:L146 | 108,033 | order-book waterfall: opening 31-Mar-2026 | — |
| S5:L147 | -5,346 | order-book waterfall: sales executed Q1 FY27 | — |
| S5:L148 | 96,613 | order-book waterfall: closing 30-Jun-2026 | — |
| S5:L167 | 31-March-2026 | waterfall x-axis opening date | DATE |
| S5:L167 | 30-June-2026 | waterfall x-axis closing date | DATE |
| S5:L170 | Rs. 208 million | footnote: sales excluded from opening order book | FOOTNOTE_VALUE |

### Slide 6 — Quarterly Financial Trend (Consolidated) (36)
| Ref | Value | Context | Flag |
|---|---|---|---|
| S6:L179 | 51.3% | Revenue YoY callout | — |
| S6:L180 | 31.9% | Gross profit margin Q1FY26 | — |
| S6:L180 | 26.5% | Gross profit margin Q2FY26 | — |
| S6:L180 | 26.3% | Gross profit margin Q3FY26 | — |
| S6:L180 | 22.7% | Gross profit margin Q4FY26 | — |
| S6:L180 | 28.0% | Gross profit margin Q1FY27 | — |
| S6:L191 | 3,671 | Revenue Q1FY26 | — |
| S6:L189 | 5,334 | Revenue Q2FY26 | — |
| S6:L188 | 6,440 | Revenue Q3FY26 | — |
| S6:L185 | 10,968 | Revenue Q4FY26 | — |
| S6:L189 | 5,554 | Revenue Q1FY27 | — |
| S6:L191 | 1,171 | Gross profit Q1FY26 | — |
| S6:L191 | 1,412 | Gross profit Q2FY26 | — |
| S6:L190 | 1,692 | Gross profit Q3FY26 | — |
| S6:L188 | 2,491 | Gross profit Q4FY26 | — |
| S6:L190 | 1,555 | Gross profit Q1FY27 | — |
| S6:L201 | 21.8% | EBITDA margin Q1FY26 | — |
| S6:L201 | 17.6% | EBITDA margin Q2FY26 | — |
| S6:L201 | 18.3% | EBITDA margin Q3FY26 | — |
| S6:L201 | 14.9% | EBITDA margin Q4FY26 | — |
| S6:L201 | 15.5% | EBITDA margin Q1FY27 | — |
| S6:L201 | 14.9% | PAT margin Q1FY26 | — |
| S6:L201 | 12.7% | PAT margin Q2FY26 | — |
| S6:L201 | 12.2% | PAT margin Q3FY26 | — |
| S6:L201 | 9.7% | PAT margin Q4FY26 | — |
| S6:L201 | 11.3% | PAT margin Q1FY27 | — |
| S6:L209 | 801 | EBITDA Q1FY26 | — |
| S6:L208 | 941 | EBITDA Q2FY26 | — |
| S6:L207 | 1,179 | EBITDA Q3FY26 | — |
| S6:L206 | 1,632 | EBITDA Q4FY26 | — |
| S6:L209 | 861 | EBITDA Q1FY27 | — |
| S6:L209 | 547 | PAT Q1FY26 | — |
| S6:L208 | 679 | PAT Q2FY26 | — |
| S6:L207 | 788 | PAT Q3FY26 | — |
| S6:L206 | 1,059 | PAT Q4FY26 | — |
| S6:L208 | 625 | PAT Q1FY27 | — |
| (excluded) | Q1 FY26…Q1 FY27 axis labels, lines 194 & 212 | pure chart x-axis category repeats (2 charts x 5 quarters, 2 rows) | PERIOD_LABEL — excluded from count, see methodology note |

### Slide 7 — Q1 FY27 Financial Performance (Consolidated) table (75)
| Ref | Row | Q1FY27 | Q1FY26 | YoY | Q4FY26 | QoQ | Flag |
|---|---|---|---|---|---|---|---|
| S7:L222 | Revenue from operations | 5,554 | 3,671 | 51.3% | 10,968 | (49.4)% | 5 values |
| S7:L223 | Gross profit | 1,555 | 1,171 | 32.8% | 2,491 | (37.6)% | 5 values |
| S7:L224 | Gross profit margin | 28.0% | 31.9% | — | 22.7% | — | 3 values |
| S7:L225 | Employee expenses | 333 | 198 | 68.4% | 272 | 22.4% | 5 values |
| S7:L226 | Other expenses | 362 | 173 | 109.5% | 587 | (38.4)% | 5 values |
| S7:L227 | EBITDA | 861 | 801 | 7.5% | 1,632 | (47.3)% | 5 values |
| S7:L228 | EBITDA margin | 15.5% | 21.8% | — | 14.9% | — | 3 values |
| S7:L229 | Depreciation & amortisation | 44 | 21 | 112.6% | 32 | 37.5% | 5 values |
| S7:L230 | EBIT | 816 | 780 | 4.7% | 1,599 | (49.0)% | 5 values |
| S7:L231 | EBIT margin | 14.7% | 21.2% | — | 14.6% | — | 3 values |
| S7:L232 | Finance costs | 283 | 97 | 191.5% | 343 | (17.3)% | 5 values |
| S7:L233 | Other income | 283 | 56 | 402.9% | 202 | 40.6% | 5 values |
| S7:L234 | Profit before tax (PBT) | 816 | 739 | 10.5% | 1,458 | (44.0)% | 5 values |
| S7:L235 | PBT margin | 14.0% | 19.8% | — | 13.1% | — | 3 values |
| S7:L236 | Taxes | 191 | 192 | (0.3)% | 399 | (52.1)% | 5 values |
| S7:L237 | Profit After Tax | 625 | 547 | 14.3% | 1,059 | (41.0)% | 5 values |
| S7:L238 | Profit After Tax Margin | 11.3% | 14.9% | — | 9.7% | — | 3 values |

Row-cell total: 12 rows x 5 + 5 rows x 3 = 60 + 15 = 75 numeric cells.

### Slide 8 — Q1 FY27 Financial Performance (Standalone) table + bullets (63)
| Ref | Row | Q1FY27 | Q1FY26 | YoY | Q4FY26 | QoQ | Flag |
|---|---|---|---|---|---|---|---|
| S8:L248 | Revenue from operations* | 2,642 | 3,397 | (22.2)% | 4,870 | (45.7)% | 5 values, headline asterisked |
| S8:L250 | Gross profit | 865 | 1,007 | (14.1)% | 1,117 | (22.6)% | 5 values |
| S8:L252 | Employee expenses | 250 | 156 | 60.7% | 213 | 17.4% | 5 values |
| S8:L254 | Other expenses | 120 | 121 | (0.9)% | 201 | (40.2)% | 5 values |
| S8:L256 | EBITDA | 494 | 730 | (32.2)% | 703 | (29.6)% | 5 values |
| S8:L258 | Depreciation & amortisation | 32 | 11 | 193.7% | 25 | 27.5% | 5 values |
| S8:L260 | EBIT | 462 | 719 | (35.7)% | 678 | (31.8)% | 5 values |
| S8:L262 | Finance costs | 79 | 89 | (11.0)% | 152 | (48.1)% | 5 values |
| S8:L264 | Other income | 189 | 59 | nm | 168 | 12.4% | 4 values ("nm" not numeric) |
| S8:L266 | Profit before tax (PBT) | 572 | 689 | (16.9)% | 694 | (17.5)% | 5 values |
| S8:L268 | Taxes | 147 | 179 | (17.6)% | 287 | (48.8)% | 5 values |
| S8:L270 | Profit After Tax (PAT) | 425 | 510 | (16.7)% | 406 | 4.7% | 5 values |

Table cell total: 59.
| S8:L253-257 | 5,151 | gross standalone revenue, fine-print bullet | FOOTNOTE_VALUE |
| S8:L255 | 2,509 | inter-company eliminations, fine-print bullet | FOOTNOTE_VALUE |
| S8:L257 | 2,642 | standalone revenue post-elimination, restated in bullet (repeat of table headline) | FOOTNOTE_VALUE |
| S8:L262 | 52% | adjusted standalone revenue YoY growth, asterisk footnote | FOOTNOTE_VALUE |

### Slide 9 — Divider (0 numbers)

### Slide 10 — End-to-End Integrated Infrastructure Platform (7)
| Ref | Value | Context | Flag |
|---|---|---|---|
| S10:L288 | 18+ | years industry experience | — |
| S10:L293 | 3 | manufacturing facilities | — |
| S10:L298 | 8,000+ | green field telecom towers installed | — |
| S10:L302-303 | 2.5 | GWh BESS capacity, phase 1 | — |
| S10:L302-303 | 5 | GWh BESS capacity, phase 2 | — |
| S10:L302-303 | 10 | GWh BESS capacity, phase 3 target | — |
| S10:L307 | Rs. 108,033 million | order book | — |

### Slide 11 — Integrated Energy Platform (3)
| Ref | Value | Context | Flag |
|---|---|---|---|
| S11:L324 | 2.5 | GWh BESS manufacturing, phase 1 | — |
| S11:L324 | 5 | GWh BESS manufacturing, phase 2 | — |
| S11:L324 | 10 | GWh BESS manufacturing, phase 3 | — |

### Slide 12 — Telecom Infrastructure Solutions (2)
| Ref | Value | Context | Flag |
|---|---|---|---|
| S12:L381 | 1 | warranty/AMC/O&M contract tenure, lower bound | — |
| S12:L381 | 5 | warranty/AMC/O&M contract tenure, upper bound (years) | — |

### Slide 13 — Divider (0 numbers)

### Slide 14 — Order Wins During Q1 FY2027 (20)
| Ref | Value | Context | Flag |
|---|---|---|---|
| S14:L398 | 16,766 | total order wins, Rs. million (headline) | — |
| S14:L400 | 7,099 | NLC India BESS EPC order value | — |
| S14:L401 | 1 | deal card index | LIST_INDEX |
| S14:L402 | 250 | NLC India MW capacity | — |
| S14:L402 | 500 | NLC India MWh capacity | — |
| S14:L404 | 1 | NLC India EPC execution, years | — |
| S14:L404 | 12 | NLC India O&M term, years | — |
| S14:L406 | 15.8% | chart segment label near NLC card | SCRAMBLED_LAYOUT |
| S14:L408 | 7,020 | DVC BESS EPC order value | — |
| S14:L409 | 2 | deal card index | LIST_INDEX |
| S14:L410 | 250 | DVC MW capacity | — |
| S14:L410 | 500 | DVC MWh capacity | — |
| S14:L410 | 16,766 | donut chart center total (repeat of headline) | — |
| S14:L413 | 1 | DVC EPC execution, years | — |
| S14:L413 | 12 | DVC O&M term, years | — |
| S14:L416 | 84.2% | Telecom & ICT/Energy split chart label | SCRAMBLED_LAYOUT |
| S14:L416 | 78.1% | Telecom & ICT/Energy split chart label | SCRAMBLED_LAYOUT |
| S14:L417 | 2,647 | BSNL BharatNet OFC EPC order value | — |
| S14:L418 | 3 | deal card index | LIST_INDEX |
| S14:L421 | 3 | BSNL BharatNet execution, years | — |

Internal cross-check: 7,099 + 7,020 + 2,647 = 16,766 = stated headline total. Reconciles.

### Slide 15 — Order Book (Energy) table + donut (32, incl. 2 ZERO_STANDING)
| Ref | Row | GWh | Value Rs.Mn | Flag |
|---|---|---|---|---|
| S15:L432 | headline "Diversified Order Book of Rs. 84,530 Mn" | — | 84,530 | — |
| S15:L437 | MESDCL, Standalone BESS, BOO | 0.80 | 8,990 | — |
| S15:L438 | SECI, Solar+BESS, BOO | 0.10 | 7,000 | — |
| S15:L439 | KPTCL, Standalone BESS, BOO | 0.50 | 7,000 | — |
| S15:L440 | KREDL, Solar+BESS, BOO | 1.10 | 17,750 | — |
| S15:L442 | BOO subtotal | 2.50 | 40,740 | — |
| S15:L445 | SECI, Standalone BESS, EPC | 1.20 | 11,593 | — |
| S15:L446 | MAHAGENCO, Solar EPC | — (dash) | 9,200 | ZERO_STANDING (GWh col.) |
| S15:L447 | NLC India, Standalone BESS, EPC | 0.50 | 7,099 | — |
| S15:L448 | DVC, Standalone BESS, EPC | 0.50 | 7,020 | — |
| S15:L449 | NTPC, Standalone BESS, EPC | 0.40 | 5,836 | — |
| S15:L450 | Bondada, Solar BOS | — (dash) | 2,920 | ZERO_STANDING (GWh col.) |
| S15:L451 | EPC subtotal | 2.60 | 43,667 | — |
| S15:L453 | Yaqin Chem, Standalone BESS, Supply | 0.0037 | 123 | — |
| S15:L454 | Total | 5.10 | 84,530 | — |
| S15:L439 | 0.1% | donut: Supply share | — |
| S15:L441 | 51.7% | donut: EPC share | — |
| S15:L452 | 48.2% | donut: BOO share | — |

Numeric-cell count (dash rows contribute the value cell only, 1 each): 1(headline)+13x2(GWh+value rows, excl. the 2 dash rows)+2x1(dash rows)+3(donut%) = 1+26+2+3 = 32, of which 2 are ZERO_STANDING dash placeholders.

### Slide 16 — Order Book (Telecom & ICT) table + donut (22)
| Ref | Row | Value Rs.Mn | Flag |
|---|---|---|---|
| S16:L464 | headline "Diversified Order Book of Rs. 23,503 Mn" | 23,503 | — |
| S16:L469 | BSNL, Telecom Infra, EPC+O&M | 14,110 | — |
| S16:L471 | RNS, Telecom Infra, EPC+O&M | 1,149 | — |
| S16:L473 | TANFINET, OFC Network, EPC+O&M | 444 | — |
| S16:L474 | EPC+O&M subtotal | 15,703 | — |
| S16:L477 | BSNL, OFC Network, EPC | 2,647 | — |
| S16:L479 | Railtel, ICT, EPC | 515 | — |
| S16:L480 | Indian Railways, Railway Kavach, EPC | 226 | — |
| S16:L481 | EPC subtotal | 3,388 | — |
| S16:L484 | BSNL, Power Management, Supply | 389 | — |
| S16:L485 | Reliance, Power Management, Supply | 1,200 | — |
| S16:L486 | BSNL, Power Management, Supply | 800 | — |
| S16:L487 | Supply subtotal | 2,389 | — |
| S16:L490 | Tata Teleservices, Telecom O&M, O&M | 1,923 | — |
| S16:L491 | O&M subtotal | 1,923 | — |
| S16:L493 | Others | 101 | — |
| S16:L494 | Total | 23,503 | — |
| S16:L472 | 10.2% | donut: Supply share | — |
| S16:L472 | 8.2% | donut: O&M share | — |
| S16:L475 | 0.4% | donut: Others share | — |
| S16:L478 | 14.4% | donut: EPC share | — |
| S16:L491 | 66.8% | donut: EPC+O&M share | — |

### Slide 17 — Divider (0 numbers)

### Slide 18 — Execution Update - MSEDCL Standalone BESS BOO (3)
| Ref | Value | Context | Flag |
|---|---|---|---|
| S18:L511 | 975 | cumulative MWh BESS capacity added | — |
| S18:L512 | 375 | MWh BESS capacity added in Q1 FY27 (repeat of slide 4 figure) | — |
| S18:L515 | 24×7 | field service support | — |

### Slide 19 — Execution Update – Other Energy Projects (7)
| Ref | Value | Context | Flag |
|---|---|---|---|
| S19:L529 | 100 | SECI project, MW Solar | — |
| S19:L529 | 50 | SECI project, MW BESS | — |
| S19:L529 | 100 | SECI project, MWh BESS | — |
| S19:L529 | 250 | KPTCL project, MW | — |
| S19:L529 | 500 | KPTCL project, MWh | — |
| S19:L541 | 300 | Bondada Solar EPC, MW | — |
| S19:L541 | 200 | MAHAGENCO Solar EPC, MW | — |

### Slide 20 — Pace-Lineage Research Center, Pune (5)
| Ref | Value | Context | Flag |
|---|---|---|---|
| S20:L561 | 1 | Research Collaboration list index | LIST_INDEX |
| S20:L565 | 2 | Research Focus list index | LIST_INDEX |
| S20:L571 | 3 | Indigenous Technology Development list index | LIST_INDEX |
| S20:L577 | 4 | Strategic Importance list index | LIST_INDEX |
| S20:L581 | 5 | Long-term Vision list index | LIST_INDEX |

### Slide 21 — Update on BESS Manufacturing Capacity Expansion (13)
| Ref | Value | Context | Flag |
|---|---|---|---|
| S21:L594 | 10 | "Phased scale-up to 10 GWh" heading | — |
| S21:L595 | 2.5 | Existing capacity, GWh | — |
| S21:L596 | 5 | New facility, GWh line | — |
| S21:L597 | 2.5 | Additional line expansion, GWh | — |
| S21:L601 | 2.5 | "2.5 GWh operational at Lineage Power" | — |
| S21:L601 | 2.5 | "Additional 2.5 GWh manufacturing line" | — |
| S21:L601-602 | 10 | "On track to achieve 10 GWh manufacturing capacity" | — |
| S21:L602-604 | August 2026 | expansion line operational date | DATE |
| S21:L603-604 | August 2026 | new facility commissioning-ready date | DATE |
| S21:L604 | FY2027 | "by the end of FY2027" 10 GWh target | PERIOD_LABEL |
| S21:L606 | 5 | "New 5 GWh facility" (repeat) | — |
| S21:L613-614 | October 2026 | machines expected receipt date | DATE |
| S21:L615-616 | Q3 FY27 | new line operational target | PERIOD_LABEL |

### Slide 22 — Divider (0 numbers)

### Slide 23 — Strategy Going Forward, 4 pillars (4)
| Ref | Value | Context | Flag |
|---|---|---|---|
| S23:L629 | 01 | pillar 1 index (Manufacturing Scale & Integration) | LIST_INDEX |
| S23:L629 | 02 | pillar 2 index (Renewable Energy Platform) | LIST_INDEX |
| S23:L629 | 03 | pillar 3 index (Telecom Business Expansion) | LIST_INDEX |
| S23:L629 | 04 | pillar 4 index (International Market Presence) | LIST_INDEX |

### Slide 24 — FY27–FY28 Growth Visibility (7)
| Ref | Value | Context | Flag |
|---|---|---|---|
| S24:L659 | 2.5 | GWh BESS capacity (current) | — |
| S24:L661 | 10 | GWh phased scale-up target | — |
| S24:L664 | ₹32,000 | FY27E revenue guidance, lower bound, mn | — |
| S24:L664 | ₹34,000 | FY27E revenue guidance, upper bound, mn | — |
| S24:L675 | ₹40,000 | FY28E revenue guidance, lower bound, mn | — |
| S24:L675 | ₹42,000 | FY28E revenue guidance, upper bound, mn | — |
| S24:L676 | ₹113,379 | order book, Mn | — |

### Slide 25 — Disclaimer (2)
| Ref | Value | Context | Flag |
|---|---|---|---|
| S25:L694 | 2013 | "Companies Act, 2013" citation | IDENTIFIER |
| S25:L695 | 2018 | "SEBI ICDR Regulations, 2018" citation | IDENTIFIER |

### Slide 26 — Thank You / Contact (6)
| Ref | Value | Context | Flag |
|---|---|---|---|
| S26:L724 | 560074 | Bengaluru registered/corporate office pincode | IDENTIFIER |
| S26:L728 | U31909KA2007PLC041949 | CIN on contact page | IDENTIFIER, **DISCREPANCY** — prefix "U" here vs "L" on slide 1 (L31909KA2007PLC041949); Indian CIN convention: L = listed company, U = unlisted. Same 21-char body (31909KA2007PLC041949), only the leading status letter differs between the two occurrences in the same document. |
| S26:L732 | +91 74839 41773 | Ajay Tambhale (IR) phone | IDENTIFIER |
| S26:L735 | 080-29547792 | registered office phone | IDENTIFIER |
| S26:L738 | +91 85911 90410 | Go India Advisors contact 1 phone | IDENTIFIER |
| S26:L738 | +91 9297761958 | Go India Advisors contact 2 phone | IDENTIFIER |

---

## TABLE 3 — FOOTNOTES / FINE PRINT (7)

| # | Slide | Line | First ~15 words | Flag |
|---|---|---|---|---|
| 1 | 5 | 170-171 | "Note: Data as of 30 June 2026. Q1 FY27 revenue execution excludes aggregating sales of Rs. 208 million..." | qualifies order-book waterfall |
| 2 | 8 | 246-249 | "At the standalone level, the financials represent EPC revenue from projects executed for both subsidiaries..." | GENERAL_NOTE — no marker, found only by manual sweep, not by grep trigger pattern |
| 3 | 8 | 252-257 | "Gross standalone revenue stood at Rs. 5,151 million. After eliminating inter-company sales of Rs. 2,509 million..." | qualifies "Revenue from operations*" headline |
| 4 | 8 | 259-262 | "*Adjusted standalone revenue from operations (before inter-company eliminations) increased by 52% YoY..." | explicit asterisk footnote to same headline |
| 5 | 15 | 456-457 | "Note: Data as of June 30, 2026" | qualifies Energy order book table |
| 6 | 16 | 495-496 | "Note: Data as of June 30, 2026" | qualifies Telecom & ICT order book table |
| 7 | 25 | 689-711 | "This presentation and the accompanying slides (the 'Presentation'), which have been prepared by Pace Digitek..." | full-page legal disclaimer, not tied to one headline number |

---

## TABLE 4 — DROPPED SLIDES

N.A. — no prior-quarter Investor Presentation was supplied to this run (no
`PRIOR_LEDGER_PATH` input), so slide-level drop comparison cannot be
performed. This should be re-run once a prior-quarter deck is available; a
dropped-slide check (`DROPPED_SLIDE`) is a standard silence signal this
pipeline exists to catch and is currently un-testable for this quarter.

---

## FLAGS SUMMARY

- `ZERO_STANDING` x2 — slide 15, MAHAGENCO and Bondada Solar EPC rows, GWh
  column dash (pure-solar projects carry no BESS GWh scope).
- `DISCREPANCY` x1 — CIN prefix mismatch between slide 1 (L31909KA2007PLC041949)
  and slide 26 (U31909KA2007PLC041949) within the same document.
- `SCRAMBLED_LAYOUT` — slide 14 chart percentage labels (15.8%, 84.2%,
  78.1%) sit in overlapping text objects per the extraction header's own
  note on pdftotext column scrambling on chart pages; values captured
  verbatim, exact chart-segment association not resolved by this ledger.
- `WORD_NUMBER` x2 — slide 4 ("five African countries", "three MoUs"),
  spelled-out quantities, not grep-catchable by digit regex.
- `FOOTNOTE_VALUE` — slide 5 (Rs. 208 mn) and slide 8 (5,151 / 2,509 / 2,642
  / 52%) figures that live inside fine print rather than the primary table.
