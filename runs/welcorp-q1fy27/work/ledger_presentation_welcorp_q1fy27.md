=== A2 COUNT TEST ===
category: slides                        grep_count: 19   sweep_count: 19   match: yes
category: cover_letter_data_points       grep_count: 11   sweep_count: 11   match: yes
category: title_disclaimer_data_points  grep_count: 4    sweep_count: 4    match: yes
category: agenda_items                  grep_count: 6    sweep_count: 6    match: yes
category: mgmt_commentary_figures       grep_count: 1    sweep_count: 1    match: yes
category: portfolio_spec                grep_count: 1    sweep_count: 1    match: yes
category: sales_volume_chart            grep_count: 8    sweep_count: 8    match: yes
category: financial_performance_chart   grep_count: 9    sweep_count: 9    match: yes
category: balance_sheet_chart           grep_count: 9    sweep_count: 9    match: yes
category: pnl_table_line_items          grep_count: 12   sweep_count: 12   match: yes
category: pnl_table_values              grep_count: 60   sweep_count: 60   match: yes
category: guidance_chart                grep_count: 12   sweep_count: 12   match: yes
category: guardrails_orderbook          grep_count: 5    sweep_count: 5    match: yes
category: business_env_figures          grep_count: 3    sweep_count: 3    match: yes  (first-pass grep on Table13's line range 354-406 for standalone quantity/warranty/km-style tokens found 2 [30,000+ km; 50-year]; manual sweep of the same slides found a 3rd — "11 states" [line 402] — a plain cardinal number without a unit-suffix the first grep pattern anchored on. Re-swept with a broadened numeral pattern and reconciled to 3/3.)
category: business_env_bullets          grep_count: 22   sweep_count: 25   match: yes  (raw first-pass grep on "•" glyph found 22; manual sweep reading full prose found 25 — slide 14's KSA-column has 3 real key-driver bullets ["Vision 2030: 30,000+ km...", "Favorable domestic demand dynamics...opportunities", "Reconstruction in the Middle East..."] that carry NO bullet glyph in the extraction because the two-column layout [INDIA col with glyphs | KSA col without] collapsed asymmetrically. Re-swept with a content-line pass on the KSA column specifically [lines 360, 362+364-tail, 365] and reconciled to 25/25.)
category: sintex_channel_chart          grep_count: 18   sweep_count: 18   match: yes
category: esg_slide                     grep_count: 15   sweep_count: 15   match: yes
category: closing_slide                 grep_count: 3    sweep_count: 3    match: yes
category: footnotes                     grep_count: 3    sweep_count: 3    match: yes
category: entities_referenced           grep_count: 2    sweep_count: 2    match: yes
category: zero_standing                 grep_count: 4    sweep_count: 4    match: yes
gate_a2: pass
=== END COUNT TEST ===

# LEDGER — Welspun Corp Limited (WELCORP) — Q1FY27 (quarter ended 30 June 2026) — Investor Presentation

Source: presentation_welcorp_q1fy27.pdf, 19 pages, 100% coverage, page 2 additionally OCR-captured (`ocr_pages: [2]` in A1 header) — same slide content appears twice in the extract (text layer at lines 58-64, OCR pass at lines 65-74). Flag: `OCR_DUPLICATE_CAPTURE` (informational — not a second slide; physical page count is 19 per `pdfinfo`, matching the 19 `[page N]` markers).

Prior-quarter ledger: **none available**. `DROPPED_SLIDE` comparison and `ENTITY_CHANGE` cross-check could NOT be performed against a prior deck — treat the slide list and entity mentions below as a first-seen baseline only. Flag: `NO_PRIOR_LEDGER`.

Chart data-label-to-period mapping method: this is a text-layer PDF (not OCR for pages other than 2), so bar values are extracted without axis binding. Every chart pairing below was resolved by (a) exact character-column alignment of each value against its nearest x-axis label, using precise offset counts (verified with `awk`/character-position scripts, not eyeballing), and (b) cross-validated against independent evidence already present in the deck (e.g., Sintex "~1.5x / ~2x / ~21x" multiplier callouts reproduce exactly from the resolved Jun-24→Jun-26 endpoints; the FY27E "756 (Q1)" EBITDA actual matches the Q1FY27 EBITDA of 756 disclosed independently on slide 8; the P&L snapshot table on slide 10 reproduces the slide 8 chart values exactly). No unresolved pairing ambiguity remains.

---

## TABLE 1 — SLIDE INVENTORY (all 19 pages)

| Slide | Line(s) | Title | Content type | Notes / Flags |
|---|---|---|---|---|
| 1 | 15-56 | Regulation 30 submission letter to BSE/NSE | Text (cover letter) | Not a deck slide but page 1 of the filed PDF; signed by Company Secretary |
| 2 | 58-74 | Investor Presentation — Q1FY27 (title page) | Text (title) | `OCR_DUPLICATE_CAPTURE` — identical content re-captured via OCR at lines 65-74 |
| 3 | 75-113 | Disclaimer | Text (legal / forward-looking-statement boilerplate) | Standard FLS cautionary language qualifying entire deck |
| 4 | 114-128 | Agenda | Text (numbered list, 6 items) | See Table 4 |
| 5 | 130-153 | Management Commentary | Text (quote) | Attributed to Mr. Vipul Mathur, MD & CEO; contains forward-looking language (see Table 5) |
| 6 | 154-186 | Portfolio Engineered for Sustained Growth (business verticals) | Text/diagram (4 verticals x geography/product/application) | WSSL footnote-defined |
| 7 | 188-210 | Operational Performance: Q1FY27 Sales Volume (in KMT) | Chart (4 mini bar-charts, 2 bars each) | See Table 7 |
| 8 | 211-235 | Financial Performance: Q1FY27 | Chart (4 mini bar-charts, 2 bars each) + footnote | See Table 8 |
| 9 | 236-260 | Healthy Balance Sheet | Chart (2 line/bar charts, 4 points each) + 2 footnotes | See Table 9 |
| 10 | 261-278 | P&L Snapshot: Q1FY27 | Table (12 line items x 5 periods) + footnote | See Table 10 |
| 11 | 280-304 | FY27 Guidance | Chart (Revenue: 4 bars; EBITDA: guidance+actual pairs x4 years) + footnote | See Table 11 |
| 12 | 306-329 | Guardrails / Order Book | Text (2 guardrail metrics) + figure (order book) + footnote | See Table 12 |
| 13 | 331-352 | Business Environment: Line Pipes (USA/KSA/India) | Text (10 key-driver bullets, no numeric data) | Forward-looking market commentary |
| 14 | 354-367 | Business Environment: Ductile Iron Pipes (India/KSA) | Text (6 key-driver bullets, 1 numeric figure) | See Table 13 |
| 15 | 369-378 | Business Environment: Stainless Steel Bars + Pipes & Tubes | Text (2 key-driver bullets, no numeric data) | Forward-looking market commentary |
| 16 | 380-406 | Business Environment: Sintex (Water Storage Tanks & Pipes) | Text (7 key-driver bullets, 2 numeric figures) | See Table 13 |
| 17 | 407-432 | Sintex: Channel Expansion Underway | Chart (3 mini charts x 5 time points + 3 multiplier callouts) | See Table 14 |
| 18 | 434-461 | ESG Focus | Text (2 ranking claims) + chart (DJSI score, 6 years) + 2 sustainability targets + footnote | See Table 15 |
| 19 | 462-477 | Thank You / Contact | Text (CIN + 2 IR contacts) | See Table 16 |

Slide-count reconciliation: `pdfinfo` header reports `page_count_pdfinfo: 19` and `formfeed_count: 19`; manual sweep of `[page N]` markers = 19. Match.

---

## TABLE 2 — COVER LETTER DATA POINTS (Slide 1, lines 16-54)

| # | Line | Item | Value | Flags |
|---|---|---|---|---|
| 1 | 16 | Company reference number | WCL/SEC/2026 | — |
| 2 | 16 | Letter date | 24 July, 2026 | — |
| 3 | 22 | Mumbai PIN (BSE) | 400 001 | — |
| 4 | 22 | Mumbai PIN (NSE) | 400 051 | — |
| 5 | 23 | Scrip Code (BSE, Equity) | 532144 | — |
| 6 | 24 | NCD scrip code | 973309 | — |
| 7 | 31-32 | Regulation cited | Regulation 30, SEBI LODR Regulations, 2015 | — |
| 8 | 34 | ISIN | INE191B01025 | — |
| 9 | 37 | Quarter-end date referenced | 30 June, 2026 | — |
| 10 | 49-50 | Digital signature timestamp | 2026.07.24, 15:21:03 +05'30' | No board-meeting time is stated in this cover letter (it is a Reg. 30 submission, not a Board Outcome letter), so no pre-conclusion-signing check is possible here — not a flag |
| 11 | 54 | Company Secretary membership no. | ACS-18182 | — |

---

## TABLE 3 — TITLE & DISCLAIMER DATA POINTS (Slides 2-3)

| # | Line | Slide | Item | Value | Flags |
|---|---|---|---|---|---|
| 1 | 60 | 2 | Quarter label (title) | Q1FY27 | Repeated verbatim in OCR pass, line 71 |
| 2 | 64 | 2 | Presentation date (title) | 24th July, 2026 | Repeated verbatim in OCR pass, line 73 |
| 3 | 88 | 3 | Legal-instrument year cited | Companies Act, 2013 | — |
| 4 | 89 | 3 | Legal-instrument year cited | SEBI (ICDR) Regulations, 2009 | — |

No numeric financial data appears on slide 3; disclaimer is pure FLS/legal boilerplate qualifying the entire deck (words: "expects," "plans," "will," "estimates," "forecast," "project," "anticipate," "likely," "target," etc., line 104-105).

---

## TABLE 4 — AGENDA ITEMS (Slide 4, lines 118-128)

| # | Line | Agenda item | Flags |
|---|---|---|---|
| 1 | 118 | Business Verticals | — |
| 2 | 120 | Operational Performance | — |
| 3 | 122 | Financial Performance | — |
| 4 | 124 | Business Environment | — |
| 5 | 126 | Project Update | Note: this agenda item is listed but slide(s) covering "Project Update" content do NOT appear to be present in the deck as extracted (slides 13-16 are titled "Business Environment", slide 17 is Sintex-specific, slide 18 is ESG) — `POSSIBLE_DROPPED_CONTENT` (agenda promises a section that is not separately findable by title in the 19-slide sequence; cannot confirm as `DROPPED_SLIDE` without a prior deck, but flagged for A3/A4 attention as an agenda-vs-content gap within this single deck) |
| 6 | 128 | ESG | — |

---

## TABLE 5 — MANAGEMENT COMMENTARY (Slide 5, lines 130-153)

| # | Line | Item | Detail | Flags |
|---|---|---|---|---|
| 1 | 134 | Numeric figure | "ROCE crossing 23%" | Cross-references slide 9 chart Q1FY27 ROCE = 23.1% (Table 9) |
| 2 | 132-133 | Forward/superlative claim | "highest-ever quarterly EBITDA" | Superlative claim, no comparison baseline stated in the quote itself (baseline is on slide 8) |
| 3 | 137-138 | Forward commitment | "strategic expansions in the USA and KSA are on track for commissioning within FY27" | Timeline commitment, no specific date/capacity given on this slide |
| 4 | 140-142 | Hedge phrase | "Despite a challenging geopolitical backdrop, we remain confident in our growth trajectory" | Hedge + forward confidence framing |
| 5 | 152 | Attribution | Mr. Vipul Mathur, MD & CEO, Welspun Corp Limited | — |

---

## TABLE 6 — PORTFOLIO VERTICALS (Slide 6, lines 154-186)

| # | Line | Item | Value | Flags |
|---|---|---|---|---|
| 1 | 174 | Ductile Iron Pipes product-range spec | "Pipes up to DN 2600 mm (among few plants globally)" | — |

Footnote: line 186, "*WSSL: Welspun Specialty Solutions Limited" — defines the WSSL abbreviation used on this slide (see Table 17, Entities).

---

## TABLE 7 — OPERATIONAL PERFORMANCE: SALES VOLUME CHART (Slide 7, lines 188-210)

| # | Line | Metric | Q1FY26 | Q1FY27 | Unit | Flags |
|---|---|---|---|---|---|---|
| 1 | 192-198 | Line Pipes (India + USA) | 182 | 193 | KMT | +6% implied YoY |
| 2 | 192-198 | DI Pipes | 65 | 69 | KMT | +6% implied YoY |
| 3 | 202-209 | Stainless Steel Bars & Pipes | 8.3 | 6.3 | KMT | -24% implied YoY (volume decline) |
| 4 | 202-209 | TMT Rebars | 40 | 47 | KMT | +18% implied YoY |

(8 discrete values across the 4 metrics x 2 periods.)

---

## TABLE 8 — FINANCIAL PERFORMANCE CHART (Slide 8, lines 211-235)

| # | Line | Metric | Q1FY26 | Q1FY27 | Unit | Flags |
|---|---|---|---|---|---|---|
| 1 | 216/215 | Revenue from Operations | 3,551 | 4,081 | INR cr. | Matches P&L snapshot table, Table 10 row 1 |
| 2 | 216/214 | EBITDA | 560 | 756 | INR cr. | Matches P&L snapshot table row 3; also matches FY27 Guidance chart FY27E "Actual (Q1)" annotation, Table 11 |
| 3 | 227/225 | PBT | 412 | 586 | INR cr. | Matches P&L snapshot table row 7 |
| 4 | 229/225 | PAT (after Minorities, Associates & JVs) | 350 | 1,046 | INR cr. | Matches P&L snapshot table row 10 |
| 5 | 234 | Footnote figure | — | INR 548 cr. | one-time gain | "Q1FY27 PAT includes one-time gain of INR 548 cr. on partial stake sale in EPIC (KSA)" — cross-references P&L table "Exceptional Items" row (Table 10 row 9) and entity EPIC (Table 17) |

(8 chart values + 1 footnote figure = 9.)

---

## TABLE 9 — HEALTHY BALANCE SHEET CHART (Slide 9, lines 236-260)

| # | Line | Metric | FY24 | FY25 | FY26 | Q1FY27 | Unit | Flags |
|---|---|---|---|---|---|---|---|---|
| 1 | 242/249/252/255 | Net Debt / (Cash) | 387 | (1,049) | (1,627) | (2,336) | INR cr. | Net cash position since FY25; deepening net cash each period |
| 2 | 254/249/245/243 | ROCE | 20.0% | 21.0% | 22.3% | 23.1% | % | Q1FY27 figure is annualized (footnote, line 259); matches slide 5 commentary "ROCE crossing 23%" (Table 5) |

Footnotes (line 259): "Q1FY27 Net Cash position after capex of ~INR 834 cr." (1 additional figure — Q1 capex); "Annualized ROCE for Q1FY27" (qualifier, no new figure).

(8 chart values + 1 footnote figure = 9.)

---

## TABLE 10 — P&L SNAPSHOT TABLE (Slide 10, lines 262-278)

Full table, 12 line items x 5 periods (Q1FY27, Q1FY26, YoY Gr., Q4FY26, QoQ Gr.) = 60 populated cells, including dash/zero cells (never dropped, per `ZERO_STANDING` rule).

| # | Line | Line item | Q1FY27 | Q1FY26 | YoY Gr. | Q4FY26 | QoQ Gr. | Flags |
|---|---|---|---|---|---|---|---|---|
| 1 | 264 | Revenue from Operations | 4,081 | 3,551 | +15% | 4,313 | -5% | — |
| 2 | 265 | Other income | 64 | 35 | +82% | 36 | +79% | — |
| 3 | 266 | EBITDA | 756 | 560 | +35% | 539 | 40% | — |
| 4 | 267 | EBITDA Margin (%) | 18.5% | 15.8% | +270 bps | 12.5% | +600 bps | — |
| 5 | 268 | Depreciation and Amortisation | 125 | 85 | +47% | 93 | +34% | — |
| 6 | 269 | Finance Cost | 45 | 63 | -28% | 49 | -8% | — |
| 7 | 270 | Profit before tax and share of JVs | 586 | 412 | +42% | 397 | +48% | — |
| 8 | 271 | Share of profit/(loss) from Associates and JVs | 73 | 49 | +49% | 107 | -32% | — |
| 9 | 272 | Exceptional Items* | 548 | **-** | **-** | **0** | **-** | `ZERO_STANDING` x4 — Q1FY26, YoY Gr. and QoQ Gr. cells are dash; Q4FY26 cell is literal zero. This is the line item behind the 548cr EPIC one-time gain (line 234, 278); the line exists in the template precisely because an exceptional/one-off transaction occurred this quarter — canonical `ZERO_STANDING` pattern, retained not dropped |
| 10 | 273 | PAT after Minorities, Associates & JVs | 1,046 | 350 | +199% | 370 | 185% | — |
| 11 | 274 | EPS | 39.7 | 13.3 | +198% | 14.0 | 183% | — |
| 12 | 276 | PAT without Exceptional Items | 499 | 350 | +42% | 370 | 36% | — |

Footnote (line 278): "* One time gain on partial stake sale in East Pipes Integrated Company for Industry (EPIC), KSA" — qualifies row 9 and cross-references slide 8 footnote (Table 8 row 5).

---

## TABLE 11 — FY27 GUIDANCE CHART (Slide 11, lines 280-304)

Revenue (single series, actual-to-date + FY27E guidance):

| # | Line | Year | Value (INR cr.) | Flags |
|---|---|---|---|---|
| 1 | 287 | FY24 | 17,340 | — |
| 2 | 290 | FY25 | 13,978 | Revenue declined FY24→FY25 before recovering — non-monotonic, flagged for A4 interpretation, not explained on this slide |
| 3 | 288 | FY26 | 16,770 | — |
| 4 | 285 | FY27E | 20,000 | Stated as "the stated Guidance" per footnote, line 304 |

EBITDA (dual series — Guidance vs. Actual, legend at line 302):

| # | Line | Year | Guidance (INR cr.) | Actual (INR cr.) | Flags |
|---|---|---|---|---|---|
| 5-6 | 292/290 | FY24 | 1,500 | 1,804 | Actual beat guidance |
| 7-8 | 291/290 | FY25 | 1,700 | 1,858 | Actual beat guidance |
| 9-10 | 288/287 | FY26 | 2,200 | 2,371 | Actual beat guidance |
| 11-12 | 284/296 | FY27E | 2,850 | 756 (Q1 only, annotated "(Q1)") | Partial-year actual only; matches Q1FY27 EBITDA disclosed on slide 8 (Table 8 row 2) and slide 10 (Table 10 row 3) |

(4 Revenue values + 8 EBITDA values = 12.)

---

## TABLE 12 — GUARDRAILS / GLOBAL ORDER BOOK (Slide 12, lines 306-329)

| # | Line | Item | Value | Flags |
|---|---|---|---|---|
| 1 | 317-319 | ROCE guardrail | Sustained above the 20% threshold (">20%") | Forward commitment / guardrail, not a period-specific actual |
| 2 | 321-324 | Net Debt / EBITDA guardrail | "<1x" | Forward commitment / guardrail |
| 3 | 320 | Global Order Book | INR 24,750 crore | Forward revenue-visibility figure |
| 4 | 329 | Footnote cutoff date | "Based on execution upto 30th June" | Qualifies order book figure (row 3) |
| 5 | 329 | Footnote cutoff date | "and new orders upto 22nd July" | Qualifies order book figure (row 3); note the order book is dated 22 July, two days before the 24 July presentation date — new-order cutoff precedes the deck's own cover date by 2 days, consistent |

---

## TABLE 13 — BUSINESS ENVIRONMENT: NUMERIC FIGURES (Slides 14, 16)

| # | Line | Slide | Item | Value | Flags |
|---|---|---|---|---|---|
| 1 | 361 | 14 (DI Pipes, KSA) | Vision 2030 water/sewage network build-out target | "30,000+ km of new water & sewage networks" | Forward market-sizing figure, third-party framed (KSA govt. Vision 2030), not a company target |
| 2 | 386 | 16 (Sintex) | Sintex Eterno WST product claim | "industry-first 50-year warranty" | Product spec / marketing claim |
| 3 | 402 | 16 (Sintex, Pipes) | Channel footprint | "Extended footprint to 11 states" | — |

## TABLE 13B — BUSINESS ENVIRONMENT: QUALITATIVE KEY-DRIVER BULLETS (Slides 13-16, all forward-looking market commentary)

| Slide | Geography/segment | # bullets | Lines | Flags |
|---|---|---|---|---|
| 13 | Line Pipes — USA | 4 | 335-338 | LNG Exports; Domestic Power demand for AI Data Centers; NGL Demand; Resurgence of Oil Pipe Lines |
| 13 | Line Pipes — KSA | 3 | 343-345 | Oil & Gas (Aramco); Water (desalination transport); Exports (Middle East reconstruction) |
| 13 | Line Pipes — India | 3 | 350-352 | Exports (marquee projects); Domestic O&G; Domestic Water (Jal Jeevan Mission) |
| 14 | DI Pipes — India | 3 | 362,364,366 | Jal Jeevan/Amrut 2.0 funding constraints (a caution, not a tailwind); Export potential Europe/ME/Africa; Pig Iron exports |
| 14 | DI Pipes — KSA | 3 | 360,362+364,365 | Vision 2030 (30,000+ km, row 1 above); favorable domestic demand dynamics; reconstruction in Middle East | `LOW_BULLET_GLYPH_RISK` — these 3 KSA bullets carry no "•" glyph in extraction (two-column layout merge); confirmed present by manual read, see Count Test note |
| 15 | Stainless Steel Bars+Pipes — India | 2 | 373-378 | Thermal/Nuclear/Defence/Aerospace/O&G demand + Make in India; geopolitical/tariff headwind on exports (hedge) |
| 16 | Sintex — Water Storage Tanks | 5 | 386,389-390,392-393,395,397-398 | Premiumisation (50-yr warranty); Economy segment growth; Channel expansion; Tier-2 urbanization growth; Branding campaign |
| 16 | Sintex — Pipes | 2 | 402-403,405 | 11-state footprint + SWR anti-rodent range; OPVC approvals momentum |

Total qualitative bullets = 25 (10 + 6 + 2 + 7). None of slides 13/15 carry a headline numeric figure — pure forward-looking qualitative commentary.

---

## TABLE 14 — SINTEX: CHANNEL EXPANSION CHART (Slide 17, lines 407-432)

| # | Line | Metric | Jun-24 | Dec-24 | Jun-25 | Dec-25 | Jun-26 | Multiplier callout | Flags |
|---|---|---|---|---|---|---|---|---|---|
| 1-5 | 412-416 | Distributors | 356 | 374 | 438 | 493 | 545 | ~1.5x (line 431) | 545/356 = 1.53x, consistent with callout |
| 6-10 | 417-418,414-415,412 | Retailers ('000s) | 20 | 21 | 26 | 30 | 37 | ~2x (line 431) | 37/20 = 1.85x, rounds to callout |
| 11-15 | 424,422,417,414,413 | Plumbers ('000s) | 4 | 19 | 52 | 73 | 86 | ~21x (line 431) | 86/4 = 21.5x, consistent with callout |

(15 chart values + 3 multiplier callouts = 18. All three chart-to-callout ratios independently validate the column pairing.)

---

## TABLE 15 — ESG FOCUS (Slide 18, lines 434-461)

| # | Line | Item | Value | Flags |
|---|---|---|---|---|
| 1 | 436 | Ranking claim (overall) | "Ranked 5th globally and 2nd in India overall — Steel Sector — 2025" | 3 embedded facts: 5th (global rank), 2nd (India rank), 2025 (ranking edition/year) |
| 2 | 437 | Ranking claim (Governance & Economic Dimension) | "ranked 3rd globally and 2nd in India — Steel Sector — 2025" | 3 embedded facts: 3rd, 2nd, 2025 |
| 3-8 | 441-450 | S&P Global (DJSI) ESG Ratings, by year | 2020=9, 2021=41, 2022=57, 2023=68, 2024=73, 2025=78 | Monotonic year-on-year improvement across all 6 years shown |
| 9 | 457 | Sustainability goal | Water Neutrality by 2040 | Forward target, 14-year horizon from FY27 |
| 10 | 457 | Sustainability goal | Carbon Neutrality by 2040 | Forward target, 14-year horizon from FY27 |
| — | 457 | Sustainability goal (non-numeric) | Zero waste to landfill | No target year stated — no number to enumerate |
| — | 460 | Footnote date | DJSI score "as on 27th Jan, 2026" | Qualifies row 3-8 timing (the FY2025 DJSI cycle score reported here was assessed in Jan 2026, i.e. after the fiscal year it is named for) |

(2 ranking-claim rows [6 embedded facts] + 6 DJSI-year values + 2 target-year goals = counted as 15 distinct data points for the Count Test, treating each embedded fact within the 2 ranking-claim sentences as one point: 3+3+6+2+1[footnote date] = 15.)

---

## TABLE 16 — CLOSING / CONTACT SLIDE (Slide 19, lines 462-477)

| # | Line | Item | Detail | Flags |
|---|---|---|---|---|
| 1 | 465 | CIN | L27100GJ1995PLC025609 | — |
| 2 | 469-471 | IR contact | Mr. Goutam Chakraborty, Head – Investor Relations, goutam_chakraborty@welspun.com | — |
| 3 | 469-471 | IR contact | Mr. Harsh Rungta, Group Head – Investor Relations, harsh_rungta@welspun.com | Two IR contacts of differing seniority (Head vs. Group Head) both listed — not itself a flag, but named for completeness |

---

## TABLE 17 — ENTITIES REFERENCED (no formal consolidation list in a presentation doctype)

| # | Entity | Relationship (as disclosed on this deck) | Line(s) | Flags |
|---|---|---|---|---|
| 1 | Welspun Specialty Solutions Limited (WSSL) | Business vertical / stainless-steel-making entity, footnote-defined | 161,186 | `ENTITY_CHANGE` not determinable — no prior-quarter ledger to diff against |
| 2 | East Pipes Integrated Company for Industry (EPIC), KSA | Associate/JV in which the Company held a stake; **partial stake sale completed this quarter**, generating the INR 548 cr. one-time gain (Table 8 row 5, Table 10 row 9) | 234,278 | `ENTITY_CHANGE` not determinable on this deck alone (no prior list), but the partial-stake divestment itself is a substantive quarter-over-quarter change in economic interest — flagged for A3/A4 as a real event, not a data-completeness gap |

---

## SUMMARY OF ALL FLAGS RAISED
- `ZERO_STANDING` x4 — P&L Snapshot table, "Exceptional Items*" row: Q1FY26 (dash), YoY Gr. (dash), Q4FY26 (literal 0), QoQ Gr. (dash) — line 272.
- `OCR_DUPLICATE_CAPTURE` — slide 2 title/date content extracted twice (text layer + OCR pass), lines 58-64 and 65-74.
- `NO_PRIOR_LEDGER` — `DROPPED_SLIDE` and `ENTITY_CHANGE` checks could not be run; no prior-quarter deck/ledger was supplied to this run.
- `POSSIBLE_DROPPED_CONTENT` — Agenda item 5, "Project Update" (line 126), has no slide in the 19-slide sequence that carries that title or an obviously matching section; flagged for A3/A4 to confirm whether this is (a) folded into another titled slide, (b) genuinely absent versus the stated agenda, or (c) a labeling artifact.
- `LOW_BULLET_GLYPH_RISK` — slide 14 KSA-column key-driver bullets (3 of them) carry no bullet-glyph in extraction due to two-column layout collapse; caught only by manual sweep, not by glyph-anchored grep — see Count Test resolution for `business_env_bullets`.
- Cross-slide figure consistency (not a flag, noted for A3/A4 convenience): Q1FY27 EBITDA = 756 appears identically on slide 8 (chart), slide 10 (table), and slide 11 (guidance-chart "Actual (Q1)" annotation). Q1FY27 Revenue = 4,081 and ROCE ≈23% also reproduce consistently across slides 8-10 and 5/9 respectively.
