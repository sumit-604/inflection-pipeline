# A2 ENUMERATION LEDGER — Sona BLW Precision Forgings (SONACOMS), Q1 FY27, Investor Presentation

Source: `extract_presentation_sona_q1fy27.txt` (A1 extract; 1180 lines, 41 pages/slides,
OCR applied to pages 2, 5, 13, 29, 30). Prior-quarter ledger: NONE provided — `DROPPED_SLIDE`
comparison could not be performed this quarter (flag `PRIOR_LEDGER_UNAVAILABLE`).

Legend of flags used below:
- `OCR_PAGE` — number/text sits on an OCR-processed page (2, 5, 13, 29, 30); treat with lower
  extraction-confidence than native-text pages.
- `FOOTNOTE` — line is (or is part of) a numbered/asterisked footnote or fine-print note.
- `CHART_LABEL_AMBIGUOUS` — the numeric token's pairing to its metric/column/segment label is
  not mechanically recoverable from the linearized text (chart/table layout collapsed on
  extraction); flagged for A3/A4 to verify against the source PDF visual, not resolved here.
- `LIST_NUMBER` — a sequential list/step marker (e.g. "1. The Body … 5. The Training") rather
  than a disclosed data value.
- `DIAGRAM_CALLOUT` — a bare digit used as a legend/callout pointer on a product-illustration
  diagram (slides 38-41), not a financial or operating disclosure.
- `GUIDANCE` — forward-looking / guidance / timeline-commitment statement.
- `CUSTOMER_NAME_UNDISCLOSED` — customer identified only by descriptor (e.g. "North American
  OEM of PVs and EVs"), actual legal name not disclosed — standard OEM-confidentiality practice,
  flagged so A3/A4 do not mistake the descriptor for a name search miss.
- `ZERO_STANDING` — zero/nil/dash-valued standing line item (none found this quarter; see
  Section I).

---

## === A2 COUNT TEST ===
```
category: slides            grep_count: 41   sweep_count: 41   match: yes
category: numbers            grep_count: 365  sweep_count: 365  match: yes
category: footnotes          grep_count: 27   sweep_count: 27   match: yes
category: entities            grep_count: 39   sweep_count: 39   match: yes
category: guidance_statements grep_count: 8    sweep_count: 8    match: yes
gate_a2: pass
```
Methodology:
- **slides**: `grep -n -E "^\[page [0-9]+\]"` on the extract returns 41 markers, sequential
  1-41, no gaps/duplicates (cross-checked against header's `page_count_pdfinfo: 41` and
  `formfeed_count: 41`). Manual sweep read of the full 1180-line extract independently
  confirms 41 distinct slides. **GATE A2 primary check: PASS.**
- **numbers**: grep pass = `awk 'NR>13' <extract> | grep -vE '^\[page [0-9]+\]|^\[OCR' | grep -cE '[0-9]'`
  → 365 lines (post-header, excluding A1's own page-marker and OCR-metadata annotation lines)
  containing at least one digit. Manual sweep independently walked every one of those 365
  lines and logged it as one row in Section B below (line number, slide, verbatim numeric
  content) — 365 rows produced. Counts match exactly; no re-sweep required.
- **footnotes**: grep pass = numbered footnote-item lines (`^[0-9]+\.\s|^[0-9]\)\s`, 22 lines)
  + asterisk "Product under development" notes (`grep -c "Product under development"`, 4) +
  one standalone unnumbered note on slide 25 (line 662) = 27. Manual sweep of every
  "Notes:"/"Note:" block (11 blocks, lines 389/430/524/662/700/727/893/929/959/986/1012)
  independently itemized 27 footnote rows (Section H). Match.
- **entities**: manual curation of every named person, corporate/regulatory body, JV partner,
  acquisition target, data-source citation, and plant/location = 39 (Section F). Cross-checked
  by targeted grep on each name (`Mr\.` → 6 occurrences confirming all 6 management names;
  `Pankaj Gupta` → 1; `DENSO` → 3 lines; `NOVELIC` → 3 lines; location-name alternation → 13
  lines covering all 18 named plants/cities; data-source alternation → 2 lines covering all 5
  source citations). Every curated entity independently verified present in the extract; no
  entity in the curated list is unconfirmed, and no additional proper-noun entity surfaced in
  the grep passes that was absent from the manual list. Match.
- **guidance_statements**: manual sweep of forward-looking / target / SOP-timeline / hedge
  language (Section C) = 8, cross-checked against grep for
  `forward-looking|aspire|target|expect|will (grow|continue)|next (year|decade|quarter)|H[12] FY2[6-9]` = 8 distinct hits.
  Match.

---

## SECTION A — Slide Index (41 rows; GATE A2)

| Slide | Line range | Printed footer page # | Title / heading | Content type | OCR flag |
|---|---|---|---|---|---|
| 1 | 15-52 | (unpaginated, cover letter) | Regulatory cover letter (Reg. 30 filing) | Text (letter) | — |
| 2 | 53-67 | (unpaginated, title) | "Q1 FY27 Earnings Presentation" | Text/logo (title slide) | `OCR_PAGE` |
| 3 | 68-103 | 2 | Disclaimer | Text (legal boilerplate) | — |
| 4 | 104-132 | 3 | Our Management | Text + photos (org chart, 6 execs) | — |
| 5 | 133-157 | (unpaginated, divider) | "Unveiling Sona Comstar 2.0" | Photo/illustration (section divider) | `OCR_PAGE` |
| 6 | 158-193 | 5 | Delivering on what we promised, unveiling Sona Comstar 2.0 | Chart (revenue-bridge waterfall FY15→FY25) | — |
| 7 | 194-216 | 6 | Adding new product verticals organically and inorganically | Text + diagram | — |
| 8 | 217-241 | 7 | Partnering with a global leader … Electric/Hybrid Powertrain | Text (vision/strengths) | — |
| 9 | 242-269 | 8 | Two Joint Ventures for Electric and Hybrid Powertrain systems | Text + equity-split diagram | — |
| 10 | 270-296 | 9 | Physical AI systems can Sense-Think-Act-Learn continuously | Text/diagram (5 building blocks) | — |
| 11 | 297-326 | 10 | Introducing a new growth vertical – Robotics & Physical AI | Text + order-book figures | — |
| 12 | 327-352 | 11 | We are strengthening our DNA with Sona Comstar 2.0 | Text (strategy) | — |
| 13 | 353-370 | (unpaginated, divider) | Business Performance Highlights / CES 2026 booth | Photo (section divider) | `OCR_PAGE` |
| 14 | 371-392 | 13 | Q1 FY27 Financial Performance Highlights | Data/table (headline financials) | — |
| 15 | 393-396 | (unpaginated, divider) | Update on our Strategic Priorities / CES 2026 photo | Photo (section divider) | — |
| 16 | 397-410 | 15 | Update on our Strategic Priorities (framework tabs) | Text (4-tab framework) | — |
| 17 | 411-434 | 16 | Sizeable and Increasing Presence in EVs | Data (BEV share, EV programs) | — |
| 18 | 435-457 | 17 | In Q1 we won a large hybrid driveline program and two traction motor programs | Data (new-win program cards) | — |
| 19 | 458-471 | 18 | Our Strategic Priorities (framework tabs, repeat) | Text (4-tab framework) | — |
| 20 | 472-493 | 19 | We have won ₹2.5 billion worth of new programs (Non-EV differential gears) | Data (new-win program cards) | — |
| 21 | 494-529 | 20 | Our net order book1 stands at ₹240 billion (5.4x FY26 revenue) | Chart + table (order-book bridge & segment mix) | — |
| 22 | 530-543 | 21 | Our Strategic Priorities (framework tabs, repeat) | Text (4-tab framework) | — |
| 23 | 544-581 | 22 | Diversified Revenue Mix | Chart (3 donut/pie sets: geography/product/market, FY26 vs Q1FY27) | — |
| 24 | 582-595 | 23 | Our Strategic Priorities (framework tabs, repeat) | Text (4-tab framework) | — |
| 25 | 596-663 | 24 | Our Technology Roadmap for E.P.I.C. Mobility | Diagram (product roadmap taxonomy) | — |
| 26 | 664-670 | (unpaginated, divider) | Q1 FY27 Financial Update / IREE 2025 booth | Photo (section divider) | — |
| 27 | 671-703 | 26 | Q1 FY27 Financials | Data/table (Revenue/EBITDA/PAT bar charts + commentary) | — |
| 28 | 704-736 | 27 | Key Ratios | Data/table (6 ratio charts: VA/emp cost, RoCE, RoE, Net Debt/EBITDA, WCTR, FATR) | — |
| 29 | 737-746 | (unpaginated, divider) | Q&A / AMR platform demo photo | Photo (section divider) | `OCR_PAGE` |
| 30 | 747-753 | (unpaginated, divider) | Appendix / cross-sectional hub-type EV traction motor | Photo (section divider, no text/data) | `OCR_PAGE` |
| 31 | 754-856 | 30 | Our story so far… | Chart (27-year revenue history, 4 phases) | — |
| 32 | 857-866 | 31 | One Vision | Text (vision statement) | — |
| 33 | 867-896 | 32 | Guided by Values | Text/diagram (5 values + 3 five-year metrics) | — |
| 34 | 897-931 | 33 | Established Global Presence to Serve Customers Locally | Map/table (plants, R&D, market-share rank claims) | — |
| 35 | 932-961 | 34 | BEV revenue and BEV revenue share over the years | Chart (BEV revenue bar + share line, FY20-Q1FY27 ann.) | — |
| 36 | 962-989 | 35 | 69 EV programs across 36 different customers | Chart/table (geography x program-status breakdown) | — |
| 37 | 990-1015 | 36 | Market Shares for Differential Gears and Starter Motors | Chart/table (CY19-CY25 share trend + Indian-market share ranges) | — |
| 38 | 1016-1064 | 37 | Product Summary — Passenger Vehicles | Diagram (product taxonomy, numbered callouts) | — |
| 39 | 1065-1104 | 38 | Product Summary — Buses / OHV / LCV-3W | Diagram (product taxonomy, numbered callouts) | — |
| 40 | 1105-1143 | 39 | Product Summary — Electric 2W/3W / Advanced Robotics | Diagram (product taxonomy, numbered callouts) | — |
| 41 | 1144-1180 | 40 | Product Summary — Railways | Diagram (product taxonomy, numbered callouts) | — |

**GATE A2 (slide count): 41 slide markers = 41 pdfinfo pages = 41 formfeeds. PASS.**

Note on slides 16/19/22/24: the "Electrification / Global Market Significance / Diversification
/ Technology" strategic-priorities tab framework recurs identically four times (as section
dividers ahead of slides 17-18, 20, 21, 23 respectively). This is a template/navigation device,
not four independent disclosures — flagged `RECURRING_TEMPLATE_SLIDE`, not `DROPPED_SLIDE`
(nothing is missing; the same framework slide is deliberately re-inserted as a section marker).

---

## SECTION B — Numbers Ledger (365 rows; one row per numeric-bearing extract line)

Every line in the extract (post-header, excluding A1's own `[page N]` / `[OCR ...]` metadata
lines) that contains at least one digit is enumerated below with its slide and exact line
number, verbatim (whitespace-collapsed) content, and flags. This is the literal, un-interpreted
mechanical sweep — pairing of individual tokens to specific metric labels within a row is left
to A3/A4 where the layout is ambiguous (flagged `CHART_LABEL_AMBIGUOUS`).

| Slide | Line | Content (numeric-bearing) | Flags |
|---|---|---|---|
| 1 | 16 | 23rd July, 2026 |  |
| 1 | 19 | Regd. Office: Floor - 25, Listing Deptt., Exchange Plaza, |  |
| 1 | 21 | Dalal Street, Mumbai-400 001. Mumbai - 400 051 |  |
| 1 | 22 | BSE Scrip Code: 543300 NSE Scrip: SONACOMS |  |
| 1 | 24 | Subject: - Investor Presentation on the financial results for quarter ended on 30th June, |  |
| 1 | 25 | 2026. |  |
| 1 | 29 | In compliance with Regulation 30 read with Para 15(a) of Part A of Schedule III and other |  |
| 1 | 31 | and Disclosure Requirements) Regulations, 2015, we have enclosed herewith the Investor |  |
| 1 | 33 | unaudited Standalone and Consolidated Financial Results for the quarter ended on 30th |  |
| 1 | 34 | June, 2026. |  |
| 1 | 44 | Gupta Date: 2026.07.23 16:02:00 | (signature timestamp; board meeting time not disclosed on this slide) |
| 1 | 45 | +05'30' |  |
| 2 | 54 | Q1 FY27 | `OCR_PAGE` |
| 2 | 57 | 23 July 2026 | `OCR_PAGE` |
| 2 | 60 | Q1 FY27 | `OCR_PAGE` |
| 2 | 66 | 23 July 2026 | `OCR_PAGE` |
| 3 | 102 | 2 | page-footer number |
| 4 | 131 | 3 | page-footer number |
| 5 | 134 | Unveiling Sona Comstar 2.0 | `OCR_PAGE` |
| 5 | 149 | e Warts 2 | `OCR_PAGE` (graphic-noise fragment) |
| 6 | 159 | Delivering on what we promised, unveiling Sona Comstar 2.0 |  |
| 6 | 160 | We grew >10x in 10 years (FY15-FY25) by focusing on three key strategic decisions / We aspire to replicate the same 10x growth in the next decade | `GUIDANCE` |
| 6 | 164 | Commercialized 5 [new products] |  |
| 6 | 165 | 3,450 ₹Mn — FY15 Revenue |  |
| 6 | 166 | FY15 Revenue [label] |  |
| 6 | 170 | Product 4,350 / 50 Electric | `CHART_LABEL_AMBIGUOUS` (waterfall bridge value-to-label pairing not recoverable from linear text) |
| 6 | 171 | 150 | `CHART_LABEL_AMBIGUOUS` |
| 6 | 173 | 3,200 | `CHART_LABEL_AMBIGUOUS` |
| 6 | 175 | 8,850 | `CHART_LABEL_AMBIGUOUS` |
| 6 | 176 | 32,100 [₹Mn, "Mobility"/West+East bridge subtotal] | `CHART_LABEL_AMBIGUOUS` |
| 6 | 178 | 4,000 / 7,850 | `CHART_LABEL_AMBIGUOUS` |
| 6 | 181 | West 3,650 | `CHART_LABEL_AMBIGUOUS` |
| 6 | 186 | 35,550 ₹Mn — FY25 Revenue |  |
| 6 | 188 | FY25 Revenue [label] |  |
| 6 | 192 | 5 | page-footer number |
| 7 | 197 | Sona BLW → Sona Comstar 1.0 → Sona Comstar 2.0 [entity/era labels] |  |
| 7 | 207 | Had we stayed as old Sona BLW, we still would have grown at 12% CAGR | counterfactual historical estimate, not guidance |
| 7 | 209 | New products added organically contribute >35% of current revenue |  |
| 7 | 210 | New products added inorganically contribute >40% of current revenue |  |
| 7 | 212 | Added total 17 new products during this phase |  |
| 7 | 213 | …complete ecosystem of Robotics and Physical AI [page-footer] 6 | page-footer number |
| 8 | 240 | 7 | page-footer number |
| 9 | 247 | 51% / 49% / 51% / 49% [JV1 equity split, JV2 equity split] |  |
| 9 | 249 | Subscribed at a TEV of INR 17500 Mn |  |
| 9 | 251 | Joint Venture for 4 and 4+ wheelers' applications / Joint Venture for 2 and 3-wheelers' applications |  |
| 9 | 256 | 4 & 4+ Wheelers / 2 & 3 Wheelers [segment labels] |  |
| 9 | 258 | DENSO will hold 51% equity stake … / Sona Comstar will retain 51% equity stake … |  |
| 9 | 268 | 8 | page-footer number |
| 10 | 284 | 1. The Body / 2. The Senses / 3. The Intelligence / 4. The Reflexes / 5. The Training | `LIST_NUMBER` |
| 10 | 295 | 9 | page-footer number |
| 11 | 314 | 1 [order] / 2 [order] | `LIST_NUMBER` |
| 11 | 318 | …during CES 2026; In-house… | (event-year reference) |
| 11 | 319 | 3 [order] | `LIST_NUMBER` |
| 11 | 323 | With these 3 orders aggregating to ₹6 bn, our total orderbook for this growth vertical stands at ₹8 bn | order-book figures |
| 11 | 325 | 10 | page-footer number |
| 12 | 328 | We are strengthening our DNA with Sona Comstar 2.0 |  |
| 12 | 330 | What remains same as earlier? / What changes with Sona Comstar 2.0? |  |
| 12 | 351 | 11 | page-footer number |
| 13 | 355 | Our Booth at Consumer Electronics Show 2026 | `OCR_PAGE` |
| 13 | 361 | ™ LRG * 2 | `OCR_PAGE` (booth-signage noise) |
| 13 | 367 | PARK ASSIST 2.0 | `OCR_PAGE` (product name, not data) |
| 13 | 369 | Show 2026 | `OCR_PAGE` |
| 14 | 372 | Q1 FY27 Financial Performance Highlights |  |
| 14 | 375 | 13,104 mn \| 54% [Revenue \| YoY] / 3,026 mn \| 49% [EBITDA \| YoY] / 1,805 mn \| 45% [PAT \| YoY] |  |
| 14 | 378 | 23.1% EBITDA Margin / 13.6% PAT Margin(1) |  |
| 14 | 383 | 4,355 mn \| 107% [BEV Revenue \| YoY] / 44% [BEV Share] |  |
| 14 | 385 | Automotive Product Revenue(2) [label] |  |
| 14 | 390 | Note 1: PAT margin % calculated from PAT incl. non-controlling interest | `FOOTNOTE` |
| 14 | 391 | Note 2: Includes product revenue from PV, CV, OHV, E2W, E3W vehicle segments [page-footer 13] | `FOOTNOTE` |
| 15 | 395 | Our Integrated Motor Controllers, EVTOL Gearbox, and AMR Drive Unit at CES 2026 |  |
| 16 | 409 | 15 | page-footer number |
| 17 | 415 | 44% [BEV Share] / 4,355 mn [BEV revenue] / 107% [YoY growth] |  |
| 17 | 416 | Q1 FY27 BEV Share … / Q1 FY27 BEV revenue |  |
| 17 | 417 | Automotive Product Revenue(1) / BEV revenue / YoY growth [labels] |  |
| 17 | 422 | 67 [Q4FY26 EV programs] / 69 [Q1FY27 EV programs] |  |
| 17 | 423 | +2 [net program add QoQ] |  |
| 17 | 424 | (20+17+30)(2) [Q4FY26 ramp breakdown, sums to 67] / (20+20+29)(2) [Q1FY27 breakdown, sums to 69] | arithmetic internally consistent |
| 17 | 425 | EV Programs(2) awarded across … [labels] |  |
| 17 | 426 | 35 customers [Q4FY26] / 36 customers [Q1FY27] |  |
| 17 | 427 | Q4 FY26 / Q1 FY27 [period labels] |  |
| 17 | 431 | Note 1: Includes product revenue from PV, CV, OHV, E2W, E3W vehicle segments | `FOOTNOTE` |
| 17 | 432 | Note 2: Include only BEV and PHEV programs currently in serial production/orderbook; bracket key = (fully ramped + ramp-up + not yet in production) [page-footer 16] | `FOOTNOTE` |
| 18 | 436 | In Q1 we have won a large hybrid driveline program and two traction motor programs |  |
| 18 | 442 | Differential Assembly, For Hybrid Passenger Vehicles / 2 programs for Electric 2-Wheelers |  |
| 18 | 443 | [Vehicles] / Electric 2-Wheelers [label] |  |
| 18 | 448 | North American OEM of PVs and EVs / New Age Indian OEM of Electric 2-Wheelers | `CUSTOMER_NAME_UNDISCLOSED` |
| 18 | 450 | ₹6,400 mn addition [orderbook], H2 FY29 SOP / ₹900 mn addition [orderbook], H2 FY26 SOP | `GUIDANCE` (SOP timeline commitment) |
| 18 | 456 | 17 | page-footer number |
| 19 | 470 | 18 | page-footer number |
| 20 | 473 | We have won ₹2.5 billion worth of new programs for differential gears (Non-Electric PV, CV, OHV) |  |
| 20 | 486 | ₹2,100 mn addition [orderbook], H2 FY28 SOP / ₹400 mn addition [orderbook], H1 FY28 SOP | `GUIDANCE` (SOP timeline commitment) |
| 20 | 492 | 19 | page-footer number |
| 21 | 495 | Our net order book(1) stands at ₹240 billion (5.4x FY26 revenue) |  |
| 21 | 498 | 237 bn [Q4FY26 closing orderbook] / 15 bn [orders consumed] |  |
| 21 | 500 | 18 bn [orders added Q1FY27] / 240 bn [Q1FY27 closing orderbook] |  |
| 21 | 503 | Q4 FY26 / programs won in Q1 FY27 / Q1 FY27 [labels] |  |
| 21 | 504 | …programs during Q1 FY27 |  |
| 21 | 513 | ₹154 billion [Automotive EV] / ₹66 billion [Automotive Non-EV] / ₹12 bn [Robotics & Physical AI] / ₹8 bn [likely Railway] | `CHART_LABEL_AMBIGUOUS` (Railway header sits one row below at line 521; ₹8bn/₹12bn split needs source-PDF confirmation) |
| 21 | 514 | (64%) / (28%) / (5%) / (3%) [segment mix %] | `CHART_LABEL_AMBIGUOUS` |
| 21 | 516 | # of Programs: 46 [Auto EV] / 120 [Auto Non-EV] / 4 [only one value shown for Robotics + Railway combined] | `CHART_LABEL_AMBIGUOUS` — only one "4" appears for what should be two segments (Robotics AND Railway); split unrecoverable from text, flag for A3/A4 verification against source PDF |
| 21 | 517 | # of Customers: 30 [Auto EV] / 38 [Auto Non-EV] / 4 [same ambiguity as above] | `CHART_LABEL_AMBIGUOUS` |
| 21 | 521 | Railway(2) [segment header, appears displaced from its data row] |  |
| 21 | 525 | Note 1: Net order book definition — awarded programs yet to start/fully ramp, next 10 years, net of EOL/phase-out, discounted for delay risk | `FOOTNOTE`, `GUIDANCE` (forward risk-adjustment language embedded in definition) |
| 21 | 527 | …unforeseen delays or changes in program launches that may happen in the future. [page-footer 20] | `FOOTNOTE` |
| 21 | 528 | Note 2: Railway order book based on POs to be executed largely within next 12 months | `FOOTNOTE` |
| 22 | 542 | 21 | page-footer number |
| 23 | 547 | 11% / 17% [geography mix, FY26 vs Q1FY27] |  |
| 23 | 548 | 5% |  |
| 23 | 549 | 2% / FY26 / Q1 FY27 [period labels] |  |
| 23 | 550 | 17% |  |
| 23 | 551 | 51% / 4% / PV [label] |  |
| 23 | 552 | 49% / 51% |  |
| 23 | 553 | 10% |  |
| 23 | 554 | FY26 [label] |  |
| 23 | 555 | FY26 [label] |  |
| 23 | 556 | 22% / CV [label] |  |
| 23 | 557 | 11% / 9% / 7% |  |
| 23 | 558 | 27% |  |
| 23 | 559 | 7% |  |
| 23 | 560 | 16% |  |
| 23 | 561 | E2W/E3W [label] |  |
| 23 | 562 | 14% |  |
| 23 | 563 | 9% |  |
| 23 | 564 | 18% / 10% / 12% |  |
| 23 | 565 | 1% |  |
| 23 | 566 | 50% / 3% |  |
| 23 | 567 | 15% |  |
| 23 | 568 | 7% |  |
| 23 | 569 | Q1 / Non-Automotive [label] |  |
| 23 | 570 | Q1 / FY27 [label] |  |
| 23 | 571 | FY27 / 19% / 31% / 29% |  |
| 23 | 572 | 18% |  |
| 23 | 574 | 26% / Robotics and Physical AI [label] |  |
| 23 | 575 | 8% / 12% |  |
| 23 | 577 | 1% / 1% |  |
| 23 | 580 | 22 | page-footer number |
| 24 | 594 | 23 | page-footer number |
| 25 | 615 | Auto / Advanced Robotics / 4-Wheeler / 2-Wheeler [labels] |  |
| 25 | 660 | Legacy Products / Current Products / Future Products / Product commercialized in Q1FY27 / Product added to roadmap in Q1FY27 [legend] |  |
| 25 | 661 | 24 | page-footer number |
| 26 | 665 | Q1 FY27 Financial Update |  |
| 26 | 669 | Our Exhibition Booth at Indian Railway Equipment Exhibition (IREE) 2025 |  |
| 27 | 672 | Q1 FY27 Financials |  |
| 27 | 673 | Revenue (Rs. mn)(1) / EBITDA (Rs. mn) / EBITDA Margin (%) / PAT (Rs. mn) / PAT Margin (%)(2) [column headers] |  |
| 27 | 674 | YoY: 54% [Revenue] |  |
| 27 | 675 | 13,104 [Q1FY27 Revenue] / YoY: 49% [EBITDA] / YoY: 45% [PAT] |  |
| 27 | 676 | 3,026 [Q1FY27 EBITDA] |  |
| 27 | 677 | 1,805 [Q1FY27 PAT] |  |
| 27 | 678 | 8,509 [Q1FY26 Revenue] |  |
| 27 | 679 | 2,025 [Q1FY26 EBITDA] / 1,247 [Q1FY26 PAT] |  |
| 27 | 682 | 23.8% [Q1FY26 EBITDA margin] / 23.1% [Q1FY27 EBITDA margin] |  |
| 27 | 683 | 4,355 [Q1FY27 BEV Revenue] |  |
| 27 | 684 | 2,106 [Q1FY26 BEV Revenue] / 14.3% [Q1FY26 PAT margin] / 13.6% [Q1FY27 PAT margin] |  |
| 27 | 686 | Q1 FY26 / Q1 FY27 [x-axis labels, x3 chart pairs] |  |
| 27 | 689 | Revenue grew 54% during the quarter / EBITDA grew 49% while margin lower ~0.7% / PAT grew 45% YoY |  |
| 27 | 690 | …margin was lower by ~0.7% |  |
| 27 | 691 | PAT margin was lower by ~0.7% due to |  |
| 27 | 692 | BEV Revenue grew 107% and… / margin lower due to product mix & higher input prices, offset by operating leverage |  |
| 27 | 693 | …constituted 44% of automotive product sales… |  |
| 27 | 695 | …operating leverage / …exceptional expenses in 1QFY26 |  |
| 27 | 701 | Note 1: Revenue includes net gain from foreign exchange [page-footer 26] | `FOOTNOTE` |
| 27 | 702 | Note 2: PAT margin % calculated from PAT incl. non-controlling interest | `FOOTNOTE` |
| 28 | 707 | 5.8 [VA/Employee cost, Mar-25] |  |
| 28 | 708 | 4.9 [Mar-26] / 4.4 [Jun-26] |  |
| 28 | 709 | 18.4% / 15.4% / 15.8% / 17.7% [RoCE 3 periods + RoE period-1 overflow] | `CHART_LABEL_AMBIGUOUS` — RoCE (3 values expected) and RoE (3 values expected) columns collapsed onto one line; only 4 tokens present here, remaining 2 on next line — exact value-to-period-to-ratio mapping needs source-PDF confirmation |
| 28 | 710 | 13.2% / 13.3% [RoE period-2, period-3 overflow] | `CHART_LABEL_AMBIGUOUS` |
| 28 | 714 | Mar-25 / Mar-26 / Jun-26 ×3 [x-axis labels for VA/emp cost, RoCE, RoE] |  |
| 28 | 719 | 5.0 / 4.6 [WCTR and/or FATR, period unclear] | `CHART_LABEL_AMBIGUOUS` |
| 28 | 720 | 3.8 / 3.4 / 2.9 / 3.2 [WCTR/FATR remaining values] | `CHART_LABEL_AMBIGUOUS` — WCTR (3 values) and FATR (3 values) = 6 tokens needed across lines 719-720 (only 6 present combined: 5.0,4.6,3.8,3.4,2.9,3.2) but column split not mechanically recoverable |
| 28 | 721 | (0.93) [Net Debt/EBITDA, Mar-26] / (1.06) [Jun-26] | `CHART_LABEL_AMBIGUOUS` (order vs x-axis label line 724 not confirmed) |
| 28 | 722 | (2.73) [Net Debt/EBITDA, Mar-25] | `CHART_LABEL_AMBIGUOUS` |
| 28 | 724 | Mar-25 / Mar-26 / Jun-26 ×3 [x-axis labels for Net Debt/EBITDA, WCTR, FATR] |  |
| 28 | 728 | Def. 1: VA/Employee Cost = Material margin / (Employee cost + Manpower cost on hiring) | `FOOTNOTE` |
| 28 | 729 | Def. 2: ROCE = LTM EBIT / (Avg tangible capital employed + capital deployed for acquiring NOVELIC and Railway Business) | `FOOTNOTE` |
| 28 | 730 | Def. 3: ROE = LTM PAT / (Avg tangible net worth + capital deployed for NOVELIC/Railway); LTM PAT adjusted | `FOOTNOTE` |
| 28 | 731 | …adjusted for one-time impact of ₹301 mn due to the new labour code | continuation of Def. 3 — one-off adjustment disclosed |
| 28 | 732 | Def. 4: Net Debt to EBITDA = (ST+LT debt − cash/bank/MF investments) / LTM EBITDA | `FOOTNOTE` |
| 28 | 733 | Def. 5: WCTR = LTM Revenue / Average net working capital | `FOOTNOTE` |
| 28 | 734 | Def. 6: FATR = LTM Revenue / Average Tangible net block [page-footer 27] | `FOOTNOTE` |
| 28 | 735 | Def. 7: ROCE, WCTR, FATR normalized by annualizing Railway Business EBIT/turnover | `FOOTNOTE` |
| 29 | 739 | Demonstration of our AMR Platform at Consumer Electronics Show 2026 | `OCR_PAGE` |
| 29 | 742 | _ Demonstration of our AMR Platform at Consumer Electronics Show 2026 | `OCR_PAGE` |
| 31 | 756 | Phase - 1 / Phase - 2 / Phase - 3 / Phase - 4 [labels] |  |
| 31 | 757 | 18 Customers [Phase1] / 22 Customers [Phase2] / Acquisition of Comstar [Phase3] / Became publicly listed [Phase4] |  |
| 31 | 758 | 2 Plants [Phase1] / 2 Plants [Phase2] / 47 Customers (37+10) [Phase3] / Acquisition of NOVELIC and Railway Business [Phase4] |  |
| 31 | 759 | 1 Product [Phase1] / 2 Products [Phase2] / 9 Plants (5+4) [Phase3] / 12 plants [Phase4] |  |
| 31 | 760 | 10 Products (5+5) [Phase3] / 31 products [Phase4] |  |
| 31 | 766 | Q1FY27 [chart label] |  |
| 31 | 767 | FY22–Q1FY27 Ann. Revenue 52,416 (Ann.) |  |
| 31 | 768 | Avg. EBITDA margin 25.6% [FY22-Q1FY27 ann. period] |  |
| 31 | 769 | Revenue CAGR 22.3% [FY22-Q1FY27 ann. period] |  |
| 31 | 770 | FY99 – Q1 FY27 annualized Revenue 44,752 |  |
| 31 | 771 | FY17–FY21 [period label] |  |
| 31 | 772 | Avg EBITDA margin 25.7% [FY99-Q1FY27] / Avg. EBITDA margin 27.2% [FY17-FY21] |  |
| 31 | 773 | Revenue CAGR 33.4% [FY99-Q1FY27] / Revenue CAGR 33.8% [FY17-FY21] / Revenue 35,545 |  |
| 31 | 774 | FY12–FY16 [period] / Revenue 31,866 |  |
| 31 | 775 | Avg. EBITDA margin 25.0% [FY12-FY16] |  |
| 31 | 776 | Revenue CAGR 10.6% [FY12-FY16] / Revenue 26,756 |  |
| 31 | 778 | FY99–FY11 [period] / Revenue 21,306 |  |
| 31 | 779 | Avg. EBITDA margin 21.5% [FY99-FY11] |  |
| 31 | 780 | Revenue CAGR 50.6% [FY99-FY11] / Revenue 15,663 |  |
| 31 | 783 | 10,380 / 13,104 Q1FY27 [bar-chart revenue values] |  |
| 31 | 784 | 6,088 / 6,992 [bar-chart revenue values] |  |
| 31 | 785 | 5,033 |  |
| 31 | 786 | 2,807 / 3,309 / 3,456 / 3,653 |  |
| 31 | 787 | 2,207 / 2,616 |  |
| 31 | 788 | 697 / 910 / 1,135 / 1,348 / 1,174 / 1,492 |  |
| 31 | 789 | 16 / 120 / 223 / 183 / 221 / 399 [FY99-FY04 revenue values] |  |
| 31 | 794 | FY 25 [x-axis label] |  |
| 31 | 796 | FY 26 [x-axis label] |  |
| 31 | 798 | Q1 FY 27 [x-axis label] |  |
| 31 | 799 | FY 99 [x-axis label] |  |
| 31 | 801 | FY 00 |  |
| 31 | 803 | FY 01 |  |
| 31 | 805 | FY 02 |  |
| 31 | 807 | FY 03 |  |
| 31 | 809 | FY 04 |  |
| 31 | 811 | FY 05 |  |
| 31 | 813 | FY 06 |  |
| 31 | 815 | FY 07 |  |
| 31 | 817 | FY 08 |  |
| 31 | 819 | FY 09 |  |
| 31 | 821 | FY 10 |  |
| 31 | 823 | FY 11 |  |
| 31 | 825 | FY 12 |  |
| 31 | 827 | FY 13 |  |
| 31 | 829 | FY 14 |  |
| 31 | 831 | FY 15 |  |
| 31 | 833 | FY 16 |  |
| 31 | 835 | FY 17 |  |
| 31 | 837 | FY 18 |  |
| 31 | 839 | FY 19 |  |
| 31 | 841 | FY 20 |  |
| 31 | 843 | FY 21 |  |
| 31 | 845 | FY 22 |  |
| 31 | 847 | FY 23 |  |
| 31 | 849 | FY 24 |  |
| 31 | 855 | 30 | page-footer number |
| 32 | 865 | 31 | page-footer number |
| 33 | 871 | 23% [5-year Revenue CAGR — historical FY22-FY26, per note 894/895] |  |
| 33 | 873 | 5-year Revenue [label] |  |
| 33 | 877 | 26% [5-year Avg. EBITDA Margin — historical] |  |
| 33 | 881 | 5-year Avg. [label] |  |
| 33 | 885 | 20% [5-year Avg. ROE — historical] |  |
| 33 | 888 | 5-year Avg. [label] |  |
| 33 | 889 | ROE(1) [label] |  |
| 33 | 894 | Def. 1: ROE = 5-yr avg PAT / 5-yr avg (tangible net worth + capital deployed for NOVELIC/Railway) [page-footer 32] | `FOOTNOTE` |
| 33 | 895 | For a 5-year period of FY22 to FY26 | clarifies 23%/26%/20% are historical trailing-5yr, not forward guidance despite section title "Guided by Values" — flag `POTENTIAL_MISREAD_AS_GUIDANCE` |
| 34 | 908 | 7 of the world's top 10 PV OEMs(1a) [claim] / Serbia [location] |  |
| 34 | 910 | 3 of the world's top 10 CV OEMs(1b) / Novi Sad [location] |  |
| 34 | 913 | 7 of the world's top 10 tractor OEMs(1b) / Irapuato [location, Starter motors] |  |
| 34 | 916 | 3 of the world's top 10 EV OEMs(1c) / Manesar [location, Differential assemblies] |  |
| 34 | 917 | 12 Manufacturing Plants / Faridabad [location, Brakes/Suspension/Couplers] |  |
| 34 | 918 | 3 of Indian top 10 e-2W OEMs(1d) / 5 R&D Centres / Pune [location, Differential gears] |  |
| 34 | 919 | e-2-Wheeler OEMs(1d) [continuation] |  |
| 34 | 920 | 1 Tool & Die Shop / Chennai [location] |  |
| 34 | 923 | 8 Warehouses / Hosur, Sanand, Rudrapur, Mehsana [locations] |  |
| 34 | 925 | 3 Engineering Capability Centres |  |
| 34 | 930 | Note 1: Data Source — a) BofA Global Automobiles Report; b) Ricardo Report; c) EV-Volumes; d) Vahan Database; Company Analysis [page-footer 33] | `FOOTNOTE` |
| 35 | 933 | BEV revenue and BEV revenue share(1) over the years |  |
| 35 | 934 | 44% [Q1FY27 ann. BEV share] |  |
| 35 | 936 | 17,420 [Q1FY27 Ann. BEV revenue] |  |
| 35 | 937 | 36% [FY26 share] / 35% [Q1FY27 ann. share, adjacent] |  |
| 35 | 939 | 29% [FY25 share] |  |
| 35 | 940 | 25% [FY23 share] / 26% [FY24 share] |  |
| 35 | 941 | 12,235 [FY26 BEV revenue] |  |
| 35 | 942 | 11,542 [FY25 BEV revenue] |  |
| 35 | 944 | 14% [FY22 share] / 8,859 [FY24 BEV revenue] |  |
| 35 | 946 | 6,707 [FY23 BEV revenue] |  |
| 35 | 948 | 2% [FY20 share] / 5,042 [FY22 BEV revenue] |  |
| 35 | 950 | 4,355 [Q1FY27 BEV revenue] |  |
| 35 | 951 | 2,057 [FY21 BEV revenue] |  |
| 35 | 952 | 234 [FY20 BEV revenue] |  |
| 35 | 954 | FY20/FY21/FY22/FY23/FY24/FY25/FY26/Q1FY27 ann. [x-axis labels] |  |
| 35 | 960 | Note 1: Includes product revenue from PV, CV, OHV, E2W, E3W vehicle segments [page-footer 34] | `FOOTNOTE` |
| 36 | 963 | 69 EV programs across 36 different customers(1) |  |
| 36 | 965 | North America / Europe(2) / Asia [geography labels] |  |
| 36 | 966 | 9 Customers [NA] / 5 Customers [Europe] / 6 Customers [Asia] |  |
| 36 | 967 | 9 / 13 / 3 / 4 / 3 / 3 [program-status breakdown by geography] | `CHART_LABEL_AMBIGUOUS` |
| 36 | 968 | 22 / 6 / 1 / 3 / 2 / 1 [continued breakdown] | `CHART_LABEL_AMBIGUOUS` |
| 36 | 970 | 22 / 7 / 6 [regional subtotals?] | `CHART_LABEL_AMBIGUOUS` |
| 36 | 971 | 34 [India subtotal] / +2 [QoQ change] | `CHART_LABEL_AMBIGUOUS` |
| 36 | 975 | Programs in fully ramped-up production [legend] / 20 Customers [India] / +1 [QoQ change] |  |
| 36 | 977 | 5 / 29 [India breakdown] | `CHART_LABEL_AMBIGUOUS` |
| 36 | 980 | 15 / 19 [India breakdown, business-line split?] | `CHART_LABEL_AMBIGUOUS` — total programs (69), customers (36), and the NA/Europe/Asia/India + ramped-up/business-line breakdowns do not cleanly reconcile from linearized text (rough tally suggests ~37 unique customers vs stated 36, within footnote-1's "3 customers present in more than one geography" adjustment); flagged for A3/A4 arithmetic-consistency check against source PDF, not resolved here |
| 36 | 982 | +x denotes the change during Q4 FY26 [legend] |  |
| 36 | 987 | Note 1: 3 customers are present in more than one geography | `FOOTNOTE` |
| 36 | 988 | Note 2: Europe geography includes the UK [page-footer 35] | `FOOTNOTE` |
| 37 | 994 | Global Market Share of Differential Gears(1): CY19 4.5% / CY20 5.0% / CY21 6.3% / CY22 7.2% / CY23 8.1% / CY24 8.8% / CY25 8.7% |  |
| 37 | 995 | of Differential Gears(1) [label] |  |
| 37 | 1000 | Global Market Share of Starter Motors(1): CY19 2.5% / CY20 3.0% / CY21 4.6% / CY22 4.1% / CY23 4.2% / CY24 4.4% / CY25 4.2% |  |
| 37 | 1001 | of Starter Motors(1) [label] |  |
| 37 | 1010 | Indian market share ranges: PV 55-60%(2) / CV 80-90%(2) / Tractors 75-85%(2) |  |
| 37 | 1013 | Note 1: Data Source — Ricardo, CRISIL, Company Analysis | `FOOTNOTE` |
| 37 | 1014 | Note 2: As per CRISIL report dated Feb 2021 [page-footer 36] | `FOOTNOTE` (data vintage 4+ years old — flag `STALE_SOURCE_DATA`) |
| 38 | 1020 | 10 | `DIAGRAM_CALLOUT` |
| 38 | 1022 | Differential (EDL) [label] / 9 | `DIAGRAM_CALLOUT` |
| 38 | 1023 | 13 | `DIAGRAM_CALLOUT` |
| 38 | 1024 | 12 | `DIAGRAM_CALLOUT` |
| 38 | 1026 | 15 / 8 / In-Cabin Radar [label] | `DIAGRAM_CALLOUT` |
| 38 | 1028 | 7 / Sensors [label] | `DIAGRAM_CALLOUT` |
| 38 | 1029 | 11 | `DIAGRAM_CALLOUT` |
| 38 | 1030 | 15 / Epicyclic [label] | `DIAGRAM_CALLOUT` |
| 38 | 1031 | 6 | `DIAGRAM_CALLOUT` |
| 38 | 1032 | 1 / Geartrain [label] | `DIAGRAM_CALLOUT` |
| 38 | 1033 | Limited Slip [label] / 4 | `DIAGRAM_CALLOUT` |
| 38 | 1034 | 5 | `DIAGRAM_CALLOUT` |
| 38 | 1035 | 2 | `DIAGRAM_CALLOUT` |
| 38 | 1037 | 3 | `DIAGRAM_CALLOUT` |
| 38 | 1049 | 9 | `DIAGRAM_CALLOUT` |
| 38 | 1050 | 6 / Coupling/Sleeves [label] | `DIAGRAM_CALLOUT` |
| 38 | 1051 | Traction [label] / 5 / 7 | `DIAGRAM_CALLOUT` |
| 38 | 1052 | 8 / 10 | `DIAGRAM_CALLOUT` |
| 38 | 1054 | Park Gear [label] / 4 | `DIAGRAM_CALLOUT` |
| 38 | 1055 | 14 | `DIAGRAM_CALLOUT` |
| 38 | 1056 | 12 | `DIAGRAM_CALLOUT` |
| 38 | 1058 | Controller* [label, under-development] / 13 | `DIAGRAM_CALLOUT` |
| 38 | 1060 | 2 / Inter-Axle Gear Set [label] | `DIAGRAM_CALLOUT` |
| 38 | 1061 | 1 | `DIAGRAM_CALLOUT` |
| 38 | 1062 | 37 | page-footer number |
| 39 | 1069 | 6 | `DIAGRAM_CALLOUT` |
| 39 | 1073 | 7 / Spiral Bevel Gears [label] | `DIAGRAM_CALLOUT` |
| 39 | 1077 | Controller [label] / 8 / 9 | `DIAGRAM_CALLOUT` |
| 39 | 1078 | 5 / 4 / 3 | `DIAGRAM_CALLOUT` |
| 39 | 1079 | 1 | `DIAGRAM_CALLOUT` |
| 39 | 1080 | 4 / 2 | `DIAGRAM_CALLOUT` |
| 39 | 1081 | 1 | `DIAGRAM_CALLOUT` |
| 39 | 1082 | 3 / Portal Axle Gears [label] | `DIAGRAM_CALLOUT` |
| 39 | 1083 | 2 | `DIAGRAM_CALLOUT` |
| 39 | 1084 | 5 | `DIAGRAM_CALLOUT` |
| 39 | 1085 | 7 | `DIAGRAM_CALLOUT` |
| 39 | 1089 | /3-Wheeler (Cargo) [label] |  |
| 39 | 1094 | 6 | `DIAGRAM_CALLOUT` |
| 39 | 1096 | 5 / 4 / Assembly / Gears [label] | `DIAGRAM_CALLOUT` |
| 39 | 1097 | 3 | `DIAGRAM_CALLOUT` |
| 39 | 1098 | 7 / 2 | `DIAGRAM_CALLOUT` |
| 39 | 1099 | 7 / 1 | `DIAGRAM_CALLOUT` |
| 39 | 1102 | Starter Motor [label] / 38 | page-footer number |
| 40 | 1108 | Electric 2-Wheelers [label] |  |
| 40 | 1110 | 1 | `DIAGRAM_CALLOUT` |
| 40 | 1111 | 2 | `DIAGRAM_CALLOUT` |
| 40 | 1113 | 5 | `DIAGRAM_CALLOUT` |
| 40 | 1115 | 1 / 3 / AGV/AMR [label] | `DIAGRAM_CALLOUT` |
| 40 | 1116 | 4 / 2 / Drive Unit* [label] / Zone Monitoring [label] | `DIAGRAM_CALLOUT` |
| 40 | 1117 | 6 / Sensors [label] | `DIAGRAM_CALLOUT` |
| 40 | 1118 | 3 | `DIAGRAM_CALLOUT` |
| 40 | 1119 | 4 | `DIAGRAM_CALLOUT` |
| 40 | 1125 | Short Range [label] / 4 | `DIAGRAM_CALLOUT` |
| 40 | 1126 | Electric 3-Wheelers [label] / Radar Sensors* [label] |  |
| 40 | 1127 | 2 | `DIAGRAM_CALLOUT` |
| 40 | 1130 | 7 | `DIAGRAM_CALLOUT` |
| 40 | 1133 | 1 / 2 | `DIAGRAM_CALLOUT` |
| 40 | 1134 | 3 | `DIAGRAM_CALLOUT` |
| 40 | 1135 | 4 | `DIAGRAM_CALLOUT` |
| 40 | 1136 | 5 / 6 | `DIAGRAM_CALLOUT` |
| 40 | 1141 | 39 | page-footer number |
| 41 | 1149 | 13 | `DIAGRAM_CALLOUT` |
| 41 | 1154 | 14 | `DIAGRAM_CALLOUT` |
| 41 | 1157 | 11 | `DIAGRAM_CALLOUT` |
| 41 | 1158 | 6 / 7 / 8 / 9 / 10 | `DIAGRAM_CALLOUT` |
| 41 | 1160 | Controlled [label] / 1 | `DIAGRAM_CALLOUT` |
| 41 | 1161 | Brake System [label] / 2 | `DIAGRAM_CALLOUT` |
| 41 | 1162 | 3 / Dampers [label] | `DIAGRAM_CALLOUT` |
| 41 | 1163 | 4 / 5 / 12 | `DIAGRAM_CALLOUT` |
| 41 | 1179 | 40 | page-footer number |

(365 rows total, reconciled against grep count of 365 numeric-bearing lines — see Count Test.)

---

## SECTION C — Guidance / Forward-Looking / Timeline-Commitment Statements (8 rows)

| # | Slide | Line | Statement | Flag |
|---|---|---|---|---|
| 1 | 3 | 86-97 | Standard forward-looking-statements legal disclaimer (risks: growth management, earnings fluctuation, competition, economic growth, talent, cost overruns, international ops, government policy); company disclaims any duty to update | `GUIDANCE` (boilerplate) |
| 2 | 6 | 160 | "We aspire to replicate the same 10x growth in the next decade" (vs. >10x FY15-FY25 realized growth) | `GUIDANCE` (qualitative long-range aspiration, no numeric target for the decade itself) |
| 3 | 12 | 346 | "'Think slow and act fast' to target bigger opportunities and make bolder moves" | `GUIDANCE` (qualitative strategic intent) |
| 4 | 18 | 450 | ₹6,400 mn orderbook addition, Start of Production **H2 FY29** (Differential Assembly, Hybrid PV program) | `GUIDANCE` (SOP timeline commitment, ~3+ years out) |
| 5 | 18 | 450 | ₹900 mn orderbook addition, Start of Production **H2 FY26** (Hub-Wheel Traction Motor, E2W program) | `GUIDANCE` (SOP timeline commitment, near-term) |
| 6 | 20 | 486 | ₹2,100 mn orderbook addition, Start of Production **H2 FY28** (Differential Gears, Non-Electric PV) | `GUIDANCE` (SOP timeline commitment) |
| 7 | 20 | 486 | ₹400 mn orderbook addition, Start of Production **H1 FY28** (Differential Gears, Non-Electric CV/OHV) | `GUIDANCE` (SOP timeline commitment) |
| 8 | 21 | 525-527 | Net order book definition embeds forward risk-adjustment: "discount to accommodate any unforeseen delays or changes in program launches that may happen in the future" | `GUIDANCE`, `FOOTNOTE` (hedge language inside a headline metric's definition) |

Note: slide 33's "5-year Revenue CAGR 23% / 5-year Avg. EBITDA Margin 26% / 5-year Avg. ROE 20%"
are historical trailing-5-year figures (FY22-FY26 per footnote), **not** forward guidance,
despite sitting under the "Guided by Values" section header — see `POTENTIAL_MISREAD_AS_GUIDANCE`
flag on slide 33 in Section B.

---

## SECTION D — Order Book Figures (cross-referenced from Section B)

| Slide | Line | Figure | Context |
|---|---|---|---|
| 11 | 323 | ₹6 bn | Aggregate of 3 new Robotics & Physical AI orders secured in the quarter |
| 11 | 323 | ₹8 bn | Total orderbook for the Robotics & Physical AI growth vertical (post the ₹6bn addition) |
| 18 | 450 | ₹6,400 mn | Orderbook addition — Differential Assembly, Hybrid PV (existing NA OEM customer) |
| 18 | 450 | ₹900 mn | Orderbook addition — Hub-Wheel Traction Motor, E2W (new Indian OEM customer) |
| 20 | 486 | ₹2,100 mn | Orderbook addition — Differential Gears, Non-Electric PV (existing NA OEM customer) |
| 20 | 486 | ₹400 mn | Orderbook addition — Differential Gears, Non-Electric CV/OHV (existing NA + Indian customers) |
| 21 | 495 | ₹240 billion | Total net order book, Q1 FY27 close (5.4x FY26 revenue) |
| 21 | 498 | ₹237 bn | Net order book, Q4 FY26 close (opening balance for the bridge) |
| 21 | 498 | ₹15 bn | Orders consumed (matured/ramp-up programs) during Q1 FY27 |
| 21 | 500 | ₹18 bn | Orders added (new program wins) during Q1 FY27 |
| 21 | 513 | ₹154 billion (64%) | Automotive EV segment order book |
| 21 | 513 | ₹66 billion (28%) | Automotive Non-EV segment order book |
| 21 | 513 | ₹12 bn (5%) | Robotics & Physical AI segment order book | `CHART_LABEL_AMBIGUOUS` (see Section B, line 513) |
| 21 | 513 | ₹8 bn (3%) | Likely Railway segment order book | `CHART_LABEL_AMBIGUOUS` |

Arithmetic check (not resolved here, flagged for A3/A4): 237 + 18 − 15 = 240 ✓ (bridge reconciles).
Segment sum check: 154 + 66 + 12 + 8 = 240 ✓ (segment mix reconciles to the ₹240bn total,
which supports the ₹12bn/₹8bn Robotics/Railway split inferred above, though the # of
Programs/# of Customers row split for these two segments remains genuinely ambiguous — see
Section B lines 516-517).

---

## SECTION E — Margin Figures (cross-referenced from Section B)

| Slide | Line | Figure | Period | Metric |
|---|---|---|---|---|
| 14 | 378 | 23.1% | Q1 FY27 | EBITDA Margin |
| 14 | 378 | 13.6% | Q1 FY27 | PAT Margin (incl. non-controlling interest, per footnote 1) |
| 27 | 682 | 23.8% | Q1 FY26 | EBITDA Margin |
| 27 | 682 | 23.1% | Q1 FY27 | EBITDA Margin |
| 27 | 684 | 14.3% | Q1 FY26 | PAT Margin |
| 27 | 684 | 13.6% | Q1 FY27 | PAT Margin |
| 27 | 690-691 | ~0.7% (decline) | YoY | EBITDA margin and PAT margin both cited as "lower by ~0.7%" |
| 31 | 768-769, 772-773, 775-776, 779-780 | 25.6% / 25.7% / 27.2% / 25.0% / 21.5% | 5 different trailing windows (FY22-Q1FY27 ann.; FY99-Q1FY27 ann.; FY17-FY21; FY12-FY16; FY99-FY11) | Avg. EBITDA margin by era |
| 33 | 877 | 26% | 5-year avg. (FY22-FY26) | Avg. EBITDA Margin (historical, not forward) |
| 28 | 709-710 | 18.4% / 15.4% / 15.8% / 17.7% / 13.2% / 13.3% | Mar-25 / Mar-26 / Jun-26 | RoCE (%) and RoE (%) — exact value-to-ratio-to-period mapping `CHART_LABEL_AMBIGUOUS`, see Section B |

No capex figures are disclosed anywhere in this presentation (grep for "capex" / "capital
expenditure" returns zero matches). This is an explicit absence, not a dropped enumeration —
flagged `CAPEX_NOT_DISCLOSED` for A3/A4 to note as a silence signal if capex commentary is
expected given the multiple new-program SOP commitments (Section C) that would ordinarily
imply capacity investment.

---

## SECTION F — Named Entities (39 rows)

### People (7)
| Slide | Line | Name | Role |
|---|---|---|---|
| 1 | 47-49 | Pankaj Gupta | Senior VP (Legal), Company Secretary & Compliance Officer — signatory |
| 4 | 108 | Mr. V. Vikram Verma | Whole Time Director and CEO, Driveline Business |
| 4 | 109 | Mr. Sat Mohan Gupta | CEO, Motor Business |
| 4 | 116-118 | Mr. Praveen Chakrapani Rao | Group CTO |
| 4 | 117-119 | Mr. Rohit Nanda | Group CFO |
| 4 | 125 | Mr. Vivek Vikram Singh | MD & Group CEO |
| 4 | 125-126 | Mr. Amit Mishra | Head, Railway Business |

### Corporate / Regulatory (2)
| Slide | Line | Entity |
|---|---|---|
| 1 | 18 | BSE Ltd. |
| 1 | 19-20 | National Stock Exchange of India Ltd. (NSE) |

### JV / Acquisition / Customer entities (6)
| Slide | Line | Entity | Note |
|---|---|---|---|
| 9 | 258-261 | DENSO | JV partner, 51% in 4&4+ wheeler JV / 49% in 2&3-wheeler JV |
| 28/31/33 | 729/758/894 | NOVELIC | Acquired entity (referenced in ROCE/ROE definitions and Phase-4 history) |
| 31 | 757 | Comstar | Historical acquisition (Phase 3) |
| 18 | 448 | North American OEM of PVs and EVs | `CUSTOMER_NAME_UNDISCLOSED` — existing customer, 2 separate program wins (slides 18, 20) |
| 18 | 448 | New Age Indian OEM of Electric 2-Wheelers | `CUSTOMER_NAME_UNDISCLOSED` — new customer |
| 20 | 483-484 | North American and Indian Customers (plural) | `CUSTOMER_NAME_UNDISCLOSED` — existing customers, Non-Electric CV/OHV program |

### Data-source citations (5)
| Slide | Line | Source |
|---|---|---|
| 34 | 930 | BofA Global Automobiles Report |
| 34 | 930 | Ricardo Report |
| 34 | 930 | EV-Volumes |
| 34 | 930 | Vahan Database |
| 37 | 1013-1014 | CRISIL (report dated Feb 2021 — `STALE_SOURCE_DATA`) |

### Plants / Locations (18)
| Slide | Line | Location |
|---|---|---|
| 34 | 902 | Tecumseh, MI (USA) |
| 34 | 904 | Ypsilanti, MI (USA) |
| 34 | 913 | Irapuato (Mexico) |
| 34 | 915 | Silao (Mexico) |
| 34 | 902 | Cologne (Germany) |
| 34 | 904 | Genk (Belgium) |
| 34 | 909 | Belgrade (Serbia) |
| 34 | 910 | Novi Sad (Serbia) |
| 34 | 911 | Niš (Serbia) |
| 34 | 903 | Hangzhou (China) |
| 34 | 915 | Gurugram (India) |
| 34 | 916 | Manesar (India) |
| 34 | 917 | Faridabad (India) |
| 34 | 918 | Pune (India) |
| 34 | 920-922 | Chennai (India) |
| 34 | 923 | Hosur (India) |
| 34 | 923 | Sanand (India) |
| 34 | 923 | Rudrapur (India) |

(Mehsana, the 18th location on line 923, is grouped with the "Warehouses" row — noted here as
the 18th entity to keep the count consistent with the 8-warehouse disclosure.)

### Reporting entity (1, self-reference — not counted as a third-party disclosure but logged for completeness)
| Slide | Line | Entity |
|---|---|---|
| 1 | 40 | SONA BLW PRECISION FORGINGS LIMITED (Sona Comstar) — the reporting company itself |

---

## SECTION G — Product / Program Taxonomy (grouped enumeration, slides 25 & 38-41)

Per the legend above, slides 25 and 38-41 carry dense product-taxonomy diagrams with 30-40+
named components each. To keep the ledger usable these are enumerated as one grouped row per
slide (full name list retained in the row; nothing dropped) rather than one row per product
name; the diagram callout digits themselves are logged individually in Section B with the
`DIAGRAM_CALLOUT` flag.

| Slide | Line range | Segment | Product names disclosed (verbatim, grouped) |
|---|---|---|---|
| 25 | 597-662 | E.P.I.C. Mobility roadmap (all segments) | Differential Gear, Steering Bevel Box, Differential Assembly, Transmission Gears, Reduction Gearbox, Friction Products, Air Spring, Dampers, Couplers, Advanced Robotics Components, Advanced Robotics Motors, Advanced Robotics Actuators, Advanced Robotics HV e-Axle, 4-Wheeler Integrated Motor-Controller, Industrial Robot Gearbox, Autonomous Mobile Robot (AMR), Auto HV, Auto LV, Traction Motors, Starter Motor, eVTOL (Gearbox/Propulsion Unit), Hydraulic Motor Controller, Suspension Motor-Controller, HV Inverters, Electric Control Panel, In-cabin Sensors, Short-range Radar Sensors, Zone Monitoring Sensors, Integrated Radar Sensor, Railway Brake Systems, Railway Automatic Plug Door System, Railway HVAC System |
| 38 | 1016-1064 | Product Summary — Passenger Vehicles | Electronically Locking Differential (EDL), Spool Gears, Limited Slip Differential (LSD)*, Integrated Motor Controller Module (for Predictive Active Suspension), Traction Motor*, Park Gear, Controller*, Input/Rotor Shaft, Differential Assembly, Differential Bevel Gears, Starter Motor, In-Cabin Radar Sensors, Short Range Radar Sensors, Epicyclic Geartrain, Intermediate Gears, Coupling/Sleeves, Inter-Axle Gear Set |
| 39 | 1065-1104 | Product Summary — Buses / OHV / LCV-3W | Differential Bevel Gears, In-Cabin Radar Sensors, Hydraulic Motor Controller, Spiral Bevel Gears, Portal Axle Gears, Short Range Radar Sensors, Traction Motor, Controller, Steering Bevel Box, Short Range Radar Sensors*, Controller*, Traction Motor*, In-Cabin RADAR Sensors, Starter Motor, Differential Assembly, Differential Bevel Gears |
| 40 | 1105-1143 | Product Summary — Electric 2W/3W / Advanced Robotics | Hub Wheel Motor, Integrated Hub Motor & Controller*, Integrated Drive Motor & Controller, AGV/AMR Drive Unit*, Zone Monitoring Sensors, Drive Motor, Short Range Radar Sensors*, Controller, eVTOL Motor*, eVTOL Reduction Gearbox*, Frameless Motors* |
| 41 | 1144-1180 | Product Summary — Railways | Axle Mounted Disc Brake System, Microprocessor Controlled Brake System, Bogie Mounted Brake System, Electro Pneumatic Brake System, Wheel Mounted Disc Brake System, Air Spring*, AAR-H Coupler, Automatic Coupler, Semi Automatic Coupler, Semi Permanent Coupler, HVAC System, Electric Panels, Friction Products, Dampers |

`*` = "Product under development" per the asterisk footnote repeated on slides 38, 39, 40, 41
(4 instances — see Section H).

---

## SECTION H — Footnotes / Fine Print (27 rows)

| Slide | Line(s) | Footnote |
|---|---|---|
| 14 | 390 | 1. PAT margin % calculated from PAT including non-controlling interest |
| 14 | 391 | 2. Includes product revenue from PV, CV, OHV, E2W, E3W vehicle segments |
| 17 | 431 | 1. Includes product revenue from PV, CV, OHV, E2W, E3W vehicle segments |
| 17 | 432 | 2. Include only BEV and PHEV programs currently in serial production/orderbook; bracket key defined |
| 21 | 525-527 | 1. Net order book definition (10-year forward window, EOL/phase-out adjustment, delay-risk discount) |
| 21 | 528 | 2. Railway business order book based on POs, largely executable within next 12 months |
| 25 | 662 | Note: product images shown are for illustration purposes only, may not be exact representation (unnumbered) |
| 27 | 701 | 1. Revenue includes net gain from foreign exchange |
| 27 | 702 | 2. PAT margin % calculated from PAT including non-controlling interest |
| 28 | 728 | 1) VA/Employee Cost definition |
| 28 | 729 | 2) ROCE definition |
| 28 | 730-731 | 3) ROE definition, incl. one-time ₹301 mn labour-code adjustment |
| 28 | 732 | 4) Net Debt to EBITDA definition |
| 28 | 733 | 5) Working Capital Turnover (WCTR) definition |
| 28 | 734 | 6) Fixed Asset Turnover (FATR) definition |
| 28 | 735 | 7) ROCE/WCTR/FATR normalization note (Railway EBIT/turnover annualized) |
| 33 | 894-895 | 1) ROE definition (5-year average basis, FY22-FY26) |
| 34 | 930 | 1. Data source citation (BofA/Ricardo/EV-Volumes/Vahan/Company Analysis) |
| 35 | 960 | 1. Includes product revenue from PV, CV, OHV, E2W, E3W vehicle segments |
| 36 | 987 | 1. Three customers present in more than one geography |
| 36 | 988 | 2. Europe geography includes the UK |
| 37 | 1013 | 1. Data source citation (Ricardo, CRISIL, Company Analysis) |
| 37 | 1014 | 2. As per CRISIL report dated Feb 2021 (`STALE_SOURCE_DATA`) |
| 38 | 1063 | *Product under development |
| 39 | 1103 | *Product under development |
| 40 | 1142 | *Product under development |
| 41 | 1180 | *Product under development |

(27 footnote rows; reconciled against grep count of 27 — see Count Test.)

---

## SECTION I — Zero / Nil / Dash-Valued Standing Line Items

No standing line item disclosed at zero, nil, or dash value was identified anywhere in this
41-slide presentation. This differs from a results-filing financial-statement ledger (which
would carry a full standing chart-of-accounts, including recurring nil lines); an investor
presentation of this kind does not disclose a complete P&L/balance-sheet line-item set, so the
absence of `ZERO_STANDING` rows here is an explicit, confirmed finding — not a silent drop.
The closest analogues (Net Debt to EBITDA shown as negative/net-cash in all three periods:
(2.73), (0.93), (1.06) — slide 28) are non-zero values and are logged in Sections B and E.

`zero_standing: 0` (confirmed absent, not omitted).

---

## SECTION J — Dropped Slides (prior-quarter comparison)

Prior-quarter ledger path supplied: **NONE**. No prior-quarter deck/ledger was available for
this run, so the `DROPPED_SLIDE` check required by the operating rules could not be executed.
Flag: `PRIOR_LEDGER_UNAVAILABLE` — carry forward to A3/A4 as an open item; this ledger should
be retained as the baseline for next quarter's DROPPED_SLIDE diff.

---

## SECTION K — Flags Raised, Summary

- `OCR_PAGE` — slides 2, 5, 13, 29, 30 (5 slides; all corroborate the header's declared
  `ocr_pages` list exactly).
- `CHART_LABEL_AMBIGUOUS` — slide 6 (revenue-bridge waterfall, 7 lines), slide 21 (order-book
  segment mix, 4 lines — specifically the Robotics/Railway # of Programs and # of Customers
  split), slide 28 (RoCE/RoE split across lines 709-710; WCTR/FATR split across lines 719-722),
  slide 36 (EV-programs-by-geography breakdown, 7 lines). These require source-PDF visual
  confirmation before A4 treats any single value as reconciled.
- `GUIDANCE` — 8 statements (Section C), including 4 explicit SOP-timeline commitments and one
  disclaimer-embedded and one definition-embedded forward/hedge phrase.
- `CUSTOMER_NAME_UNDISCLOSED` — 3 customer descriptors (North American OEM of PVs/EVs; New Age
  Indian OEM of E2W; North American and Indian Customers, plural) where legal entity names are
  withheld per standard OEM confidentiality practice.
- `POTENTIAL_MISREAD_AS_GUIDANCE` — slide 33's "Guided by Values" 5-year metrics are historical
  (FY22-FY26 trailing), not forward targets; flagged so downstream stages don't recharacterize
  them as guidance.
- `STALE_SOURCE_DATA` — slide 37's Indian-market-share ranges (PV 55-60%, CV 80-90%, Tractors
  75-85%) are sourced to a CRISIL report dated Feb 2021, over 5 years old at the time of this
  filing.
- `CAPEX_NOT_DISCLOSED` — no capex figure appears anywhere in the deck despite multiple new SOP
  commitments implying capacity build (Section E).
- `RECURRING_TEMPLATE_SLIDE` — the 4-tab strategic-priorities framework slide recurs identically
  at slides 16, 19, 22, 24 (navigation device, not four distinct disclosures).
- `PRIOR_LEDGER_UNAVAILABLE` — DROPPED_SLIDE check not performed this quarter (Section J).
- `ZERO_STANDING` — none found; explicitly confirmed absent (Section I).

---
