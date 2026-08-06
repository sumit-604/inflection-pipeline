# LEDGER — TRANSRAIL Q1FY27 — Investor/Earnings-Call Presentation (Reg 30)
Source: extract_presentation_transrail_q1fy27.txt (32 pages, formfeed_count 32, page_coverage 100%)
Prior-quarter ledger: NOT PROVIDED / NOT FOUND — DROPPED_SLIDE check could not be performed against a prior deck; noted, not silently skipped.

```
=== A2 COUNT TEST ===
category: slides                 grep_count: 32   sweep_count: 32   match: yes
category: chart_ocr_pages        grep_count: 3    sweep_count: 3    match: yes
category: footnotes_disclaimers  grep_count: 4    sweep_count: 4    match: yes
category: data_points            grep_count: 221  sweep_count: 221  match: yes
  (methodology: manual sweep produced the 221-row DP table below, one row per
  distinct disclosure unit per slide, cross-checked line-by-line against the
  source; grep_count is a mechanical `grep -c "^| DP[0-9]"` pass over this
  ledger file confirming zero rows were dropped/duplicated in transcription
  from the sweep. A single source-wide regex cannot enumerate "every number"
  in free-form slide prose/charts at matching granularity — see rule 4 note
  below — so the source-side check for this doctype is the page-marker and
  chart-OCR-marker greps above, both of which match the deck's stated 32-page
  extent and 3-page OCR supplement extent exactly.)
category: section_divider_slides grep_count: 5    sweep_count: 5    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Note on rule 4 for this doctype: `grep -c -E "^\[page [0-9]+\]" extract` = 32, matching
`page_count_pdfinfo: 32` / `formfeed_count: 32` in the A1 header — this is the
doctype's primary mechanical gate (every slide accounted for). `grep -c -E
"^\[CHART" extract` = 3, matching the 3 pages (8, 14, 31) the A1 header flags as
OCR-supplemented — confirms no OCR chart was missed or invented.

---
## TABLE A — SLIDE INDEX (32 rows, grep vs sweep both = 32, match)

| # | Slide | Line | Title | Content type |
|---|-------|------|-------|--------------|
| 1 | 1 | 14 | Reg 30 cover letter to BSE/NSE | text/letter |
| 2 | 2 | 67 | Q1 FY27 Investor Presentation (cover) | text/title |
| 3 | 3 | 84 | Disclaimer | text |
| 4 | 4 | 106 | Section divider: Corporate Overview | text/divider |
| 5 | 5 | 114 | Transrail at a Glance: A Snapshot of Our Scale | text + stat tiles |
| 6 | 6 | 147 | Our Strengths (01-06 framework) | text + numbered tiles |
| 7 | 7 | 176 | Four Decades of Growth (1984-2026 timeline) | text/timeline |
| 8 | 8 | 217 | Performance Snapshot (5-yr Order Book/Revenue/EBITDA/PAT) | chart + [CHART OCR] |
| 9 | 9 | 262 | Board of Directors (13 members) | text/photo grid |
| 10 | 10 | 298 | Management Team (10 members, 2 bios) | text/photo grid |
| 11 | 11 | 336 | Section divider: Q1FY27 Highlights | text/divider |
| 12 | 12 | 344 | Q1FY27 performance at a glance (1/2) | text + KPI tiles |
| 13 | 13 | 368 | Q1FY27 performance at a glance (2/2) | text/3-column bullets |
| 14 | 14 | 398 | Q1 Performance Trend (Q1FY25-Q1FY27) | chart + [CHART OCR] |
| 15 | 15 | 440 | Financial Highlights: Q1FY27 Consolidated P&L | table |
| 16 | 16 | 469 | Order Book Strength | chart + text |
| 17 | 17 | 503 | A glimpse of ongoing projects (8 projects) | text/photo grid |
| 18 | 18 | 524 | Balance sheet strength (1/2) | table + rating graphic |
| 19 | 19 | 566 | Balance sheet strength (2/2) | 4 charts |
| 20 | 20 | 623 | Section divider: Business Overview | text/divider |
| 21 | 21 | 631 | Our Portfolio (5 business verticals) | text |
| 22 | 22 | 672 | Today: A Global T&D Execution Expertise | text/map |
| 23 | 23 | 711 | Manufacturing facilities | text/photo grid |
| 24 | 24 | 740 | Capacity expansion for growing demands / Update on Capex | table + text |
| 25 | 25 | 771 | Section divider: Industry Tailwinds | text/divider |
| 26 | 26 | 779 | We're in a multi decade T&D growth story (India / Global) | text |
| 27 | 27 | 820 | Enjoying multiple avenues for long-term growth | text |
| 28 | 28 | 847 | Section divider: ESG, CSR and Awards | text/divider |
| 29 | 29 | 856 | Striving for Global ESG Standards | text |
| 30 | 30 | 890 | Our CSR initiatives in Q1FY2027 | text + stats |
| 31 | 31 | 924 | Recognised for Excellence | text/photo + [CHART OCR] |
| 32 | 32 | 946 | Thank You / Contact | text |

DROPPED_SLIDE: cannot be assessed — no prior-quarter presentation ledger was
supplied or found in runs/. Flagged as `PRIOR_LEDGER_UNAVAILABLE`, not silently
skipped.

---
## TABLE B — DATA POINTS / DISCLOSURE UNITS (221 rows, DP001-DP221)
Columns: DP#, Slide, Line(s), Category, Content, Flags

| DP# | Slide | Line(s) | Category | Content | Flags |
|---|---|---|---|---|---|
| DP001 | 1 | 15 | OTHER | Letter date: August 6, 2026 | |
| DP002 | 1 | 26 | OTHER | Scrip Code (BSE): 544317 | |
| DP003 | 1 | 26 | OTHER | Scrip Symbol (NSE): TRANSRAILL | |
| DP004 | 1 | 29-30 | OTHER | Subject quarter: quarter ended June 30, 2026 | |
| DP005 | 1 | 41 | STRATEGIC | Earnings Call scheduled Friday, August 7, 2026 | |
| DP006 | 1 | 48-52 | GOVERNANCE | Digital signature block: Monica Gandhi / Tanay Gandhi, dated 2026.08.06 20:39:25 +05'30 | signature name shown as "Tanay Gandhi" against "Monica Gandhi" signatory line below — SIGNATORY_NAME_MISMATCH |
| DP007 | 1 | 55-56 | GOVERNANCE | Monica Gandhi, Company Secretary and Compliance Officer | |
| DP008 | 1 | 65 | OTHER | CIN: L31506MH2008PLC179012 | |
| DP009 | 2 | 71 | OTHER | Period label: Q1 FY27 Investor Presentation | |
| DP010 | 2 | 77-79 | STRATEGIC | Tagline: "Building Scale / Creating Value / Expanding Globally" | |
| DP011 | 3 | 92-95 | DISCLAIMER | Forward-looking statements disclaimer (no obligation to update) | |
| DP012 | 3 | 97-98 | DISCLAIMER | Confidentiality / non-distribution clause | |
| DP013 | 5 | 128 | CAPACITY | 4 decades+ of expertise | |
| DP014 | 5 | 129 | CAPACITY | 37,300+ CKM transmission lines constructed (cumulative) | |
| DP015 | 5 | 129 | CAPACITY | 20,500+ Man-months of design & engineering experience | |
| DP016 | 5 | 133 | SCALE | 64 countries; footprints across six continents | |
| DP017 | 5 | 134 | CAPACITY | 231,000+ KM of conductors supplied (cumulative) | |
| DP018 | 5 | 134 | CAPACITY | 5 integrated manufacturing facilities | |
| DP019 | 5 | 138 | SCALE | 2,800+ employees | |
| DP020 | 5 | 138 | CAPACITY | 1.50 Mn+ MT towers supplied (cumulative) | |
| DP021 | 5 | 139 | ORDER_BOOK | ₹16,035 Cr unexecuted order book, including L1 of Rs.400 Cr | cross-checks DP133 (slide 16) — consistent |
| DP022 | 6 | 159-162 | STRATEGIC | "01 Operational prowess" — disciplined operations & financial management | |
| DP023 | 6 | 165 | STRATEGIC | "02 Experienced leadership" — deep domain expertise | |
| DP024 | 6 | 159-162 | STRATEGIC/CAPACITY | "03 Backward integration" — towers, conductors, poles manufactured in-house | |
| DP025 | 6 | 165-168 | STRATEGIC | "04 Design & Engineering excellence" — in-house design, engineering, testing | |
| DP026 | 6 | 159-162 | STRATEGIC | "05 Execution track record" — established global T&D presence | |
| DP027 | 6 | 166-167 | ORDER_BOOK | "06 Order-book visibility" — more than 2.3x orderbook-to-revenue ratio | |
| DP028 | 7 | 181-187 | MILESTONE | 1984: Transrail Engineering Company (TEC) started; first foundation work on 132kV line | |
| DP029 | 7 | 183-187 | MILESTONE | 1987: First direct 400 kV transmission line job received | |
| DP030 | 7 | 182-186 | MILESTONE | 1993: Factory for tower manufacturing in Baroda | |
| DP031 | 7 | 182-184 | MILESTONE | 2007: Factory for conductor manufacturing established in Silvassa | |
| DP032 | 7 | 183-184 | MILESTONE | 2008: First international turnkey project | |
| DP033 | 7 | 192-196 | MILESTONE | 2009: Factory for manufacturing of tower at Deoli, Wardha | |
| DP034 | 7 | 192-195 | MILESTONE | 2010: Tower testing unit started, Deoli | |
| DP035 | 7 | 192-195 | MILESTONE | 2010: Factory for pole manufacturing at Silvassa | |
| DP036 | 7 | 192-193 | MILESTONE | 2012: First 800 kV HVDC line (Champa-Kurukshetra) | |
| DP037 | 7 | 201-208 | MILESTONE | 2017: First 220kV & 400kV turnkey substation project orders; rly electrification turnkey job received | |
| DP038 | 7 | 202-209 | MILESTONE | 2018: Established Civil division of Transrail | |
| DP039 | 7 | 203-210 | MILESTONE | 2022: Completed first underground cabling project | |
| DP040 | 7 | 202-207 | MILESTONE | 2024: Listed on stock exchanges; Special Appreciation Awards for 765kV TL projects from PGCIL | |
| DP041 | 7 | 203-207 | MILESTONE | 2025: Foray into Solar EPC; Deoli Plant awarded 'A Grade' by PGCIL | |
| DP042 | 7 | 201-210 | MILESTONE | 2026: Tower & Conductor manufacturing capacity being doubled | |
| DP043 | 8 | 223-233 | FINANCIAL(trend) | Closing Order Book (₹Cr): FY22 5,908 / FY23 9,619 / FY24 10,100 / FY25 14,551 / FY26 16,313 | |
| DP044 | 8 | 223-233 | FINANCIAL(trend) | Revenue (₹Cr): FY22 2,350 / FY23 3,152 / FY24 4,077 / FY25 5,308 / FY26 6,880 | |
| DP045 | 8 | 238-250 | FINANCIAL(trend) | EBITDA (₹Cr): FY22 206 / FY23 294 / FY24 478 / FY25 676 / FY26 820 | |
| DP046 | 8 | 238-250 | FINANCIAL(trend) | PAT (₹Cr): FY22 65 / FY23 108 / FY24 233 / FY25 327 / FY26 421* | |
| DP047 | 8 | 255 | FOOTNOTE | *PAT excludes provision of ₹17 Cr made in Q3FY26 towards new labour code | qualifies DP046 FY26 421 figure |
| DP048 | 8 | 260 | GUIDANCE/CAGR | [CHART OCR] Closing Order Book CAGR 26% (FY22-FY26) | OCR-supplemented, not in text layer |
| DP049 | 8 | 260 | GUIDANCE/CAGR | [CHART OCR] Revenue CAGR 31% (FY22-FY26) | OCR-supplemented |
| DP050 | 8 | 260 | GUIDANCE/CAGR | [CHART OCR] EBITDA CAGR 41% (FY22-FY26) | OCR-supplemented |
| DP051 | 8 | 260 | GUIDANCE/CAGR | [CHART OCR] PAT CAGR 59% (FY22-FY26) | OCR-supplemented |
| DP052 | 9 | 267-269 | GOVERNANCE | Digambar Bagde — Executive Chairman | |
| DP053 | 9 | 267-269 | GOVERNANCE | Sanjay Kumar Verma — Non-Executive Vice Chairman | |
| DP054 | 9 | 267-269 | GOVERNANCE | Randeep Narang — Managing Director & CEO | |
| DP055 | 9 | 274-276 | GOVERNANCE | D Suryanarayana — Whole-time Director | |
| DP056 | 9 | 274-276 | GOVERNANCE | Shrikant Chaturvedi — Non-Executive Director | |
| DP057 | 9 | 274-276 | GOVERNANCE | I. S. Jha — Non-Executive Director | |
| DP058 | 9 | 281-283 | GOVERNANCE | Ranjit Jatar — Independent Director | |
| DP059 | 9 | 281-283 | GOVERNANCE | Ashish Gupta — Independent Director | |
| DP060 | 9 | 281-283 | GOVERNANCE | Vinod Dasari — Independent Director | |
| DP061 | 9 | 288-291 | GOVERNANCE | Ravita Punwani — Independent Director | |
| DP062 | 9 | 288-291 | GOVERNANCE | Maj Gen Dr. Dilawar Singh (Retd.) — Independent Director | |
| DP063 | 9 | 288-291 | GOVERNANCE | Dr. D S Gangwar, IAS (Retd.) — Independent Director | |
| DP064 | 9 | 288-291 | GOVERNANCE | Rajeev Jain — Independent Director | |
| DP065 | 10 | 302-314 | GOVERNANCE | Digambar Bagde bio — Executive Chairman, Promoter, 5 decades experience, BSc Civil Engg (M.S. University Baroda), started Transrail 1984 | |
| DP066 | 10 | 302-314 | GOVERNANCE | Randeep Narang bio — MD & CEO, 35+ yrs experience, BCom (Delhi University), PG Diploma Marketing (IMM New Delhi); prior Bharti Airtel COO (West), CEAT Kelani Holdings Sri Lanka MD/CEO, KEC International President-International (T&D, Solar) & Cables | |
| DP067 | 10 | 318-320 | GOVERNANCE | D Suryanarayana — Whole-time Director | duplicate of DP055 |
| DP068 | 10 | 318-321 | GOVERNANCE | Rajesh Neelakantan — Group CFO & Chief Strategy Officer | DUAL_CFO_TITLE with DP069 |
| DP069 | 10 | 318-320 | GOVERNANCE | Deepak Khandewal — Chief Financial Officer | DUAL_CFO_TITLE with DP068 — two "CFO"-labelled roles on one slide, unclear which holds statutory CFO responsibility |
| DP070 | 10 | 318-320 | GOVERNANCE | Chandrakant Majgaonkar — President, Design & Engineering | |
| DP071 | 10 | 326-328 | GOVERNANCE | Anant Kadiwal — Head, Civil Business | |
| DP072 | 10 | 326-328 | GOVERNANCE | Ashok Rawat — Head, Pole & Lighting Business | |
| DP073 | 10 | 326-328 | GOVERNANCE | Sonal Raj — CHRO | |
| DP074 | 10 | 326-328 | GOVERNANCE | Monica Gandhi — Company Secretary | duplicate of DP007 |
| DP075 | 12 | 355,358 | FINANCIAL(Q1FY27 vs Q1FY26 YoY) | Revenue from Operations: Rs.1,736 Cr, 5% YoY | |
| DP076 | 12 | 354-355,359 | FINANCIAL(Q1FY27 vs Q1FY26 YoY) | EBITDA: Rs.203 Cr, 1% YoY; EBITDA Margin 11.7% | |
| DP077 | 12 | 354-355,359 | FINANCIAL(Q1FY27 vs Q1FY26 YoY) | PAT: ₹108 Cr, 3% YoY; PAT Margin 6.2% | |
| DP078 | 12 | 360-361 | STRATEGIC | "Delivered resilient performance despite geopolitical and supply chain disruptions, supported by execution excellence and close monitoring" | REPEAT_DATA_POINT with DP079 (slide 13) |
| DP079 | 13 | 375-378 | STRATEGIC | Same resilience commentary repeated verbatim | REPEAT_DATA_POINT with DP078 |
| DP080 | 13 | 381 | FINANCIAL | Revenue of Rs.1,736 Cr, up 5% YoY | REPEAT_DATA_POINT with DP075 |
| DP081 | 13 | 383-384 | FINANCIAL | EBITDA of Rs.203 Cr with 11.7% EBITDA Margin | REPEAT_DATA_POINT with DP076 |
| DP082 | 13 | 386 | FINANCIAL | PAT of Rs.108 Cr, up 3% YoY | REPEAT_DATA_POINT with DP077 |
| DP083 | 13 | 388-390 | BALANCE_SHEET | Credit Rating upgraded to IND AA-/Stable by India Ratings, reflecting strengthened business and financial profile | cross-checked against DP113 (slide 18) — consistent |
| DP084 | 13 | 375-377 | STRATEGIC/CAPACITY | Commissioned eco-friendly Butibori Plant at Nagpur, strengthening tower manufacturing capacity | cross-ref DP144 (slide 23), DP155 (slide 24) |
| DP085 | 13 | 379-382 | STRATEGIC/GEOGRAPHY | Entered Australia with the Company's first Monopole project, expanding global footprint to 6 continents | |
| DP086 | 13 | 383-384 | STRATEGIC/ORDER_BOOK | Continued T&D EPC order wins across the MENA region | |
| DP087 | 13 | 375-377 | STRATEGIC (M&A) | Acquisition of Gactel Turnkey Projects, strengthening cooling tower EPC capabilities | M&A_DISCLOSURE — first/only mention of this acquisition in the deck; no consideration, date, or stake % disclosed here |
| DP088 | 13 | 379-382 | GUIDANCE | Healthy domestic and international bidding pipeline supporting long-term growth | qualitative, no % given |
| DP089 | 13 | 384-387 | OTHER (award) | Recognised as ET Edge "Best Organisations to Work" 2026 | REPEAT_DATA_POINT with DP212 (slide 31) |
| DP090 | 13 | 389-392 | OTHER (award) | Awarded RoSPA Silver Award for Cameroon TL project, health & safety | REPEAT_DATA_POINT with DP213 (slide 31) |
| DP091 | 14 | 406-413 | FINANCIAL(trend) | Revenue from operations (₹Cr): Q1FY25 916 / Q1FY26 1,660 / Q1FY27 1,736 | |
| DP092 | 14 | 406-413 | FINANCIAL(trend) | EBITDA (₹Cr): Q1FY25 120 / Q1FY26 200 / Q1FY27 203 | |
| DP093 | 14 | 423-430 | FINANCIAL(trend) | Profit before tax (₹Cr): Q1FY25 77 / Q1FY26 147 / Q1FY27 144 | |
| DP094 | 14 | 423-430 | FINANCIAL(trend) | Profit after tax (₹Cr): Q1FY25 52 / Q1FY26 106 / Q1FY27 108 | DATA_INCONSISTENCY — Q1FY26 PAT shown as 106 here vs 105 in Table (DP103, slide 15, line 459); both are internal to the same deck |
| DP095 | 14 | 438 | GUIDANCE/CAGR | [CHART OCR] Revenue from operations CAGR 38% (Q1FY25-Q1FY27) | OCR-supplemented |
| DP096 | 14 | 438 | GUIDANCE/CAGR | [CHART OCR] EBITDA CAGR 30% (Q1FY25-Q1FY27) | OCR-supplemented |
| DP097 | 14 | 438 | GUIDANCE/CAGR | [CHART OCR] Profit before tax CAGR 36% (Q1FY25-Q1FY27) | OCR-supplemented |
| DP098 | 14 | 438 | GUIDANCE/CAGR | [CHART OCR] Profit after tax CAGR 44% (Q1FY25-Q1FY27) | OCR-supplemented |
| DP099 | 15 | 450 | FINANCIAL(table) | Revenue from Operations: Q1FY27 1,736 \| Q1FY26 1,660 (YoY 5%) \| Q4FY26 1,863 (QoQ -7%) \| FY26 6,880 | |
| DP100 | 15 | 451 | FINANCIAL(table) | EBITDA: 203 \| 200 (YoY 1%) \| 207 (QoQ -2%) \| FY26 820 | |
| DP101 | 15 | 452 | FINANCIAL(table) | EBITDA margin %: 11.7% \| 12.0% \| 11.1% \| FY26 11.9% | |
| DP102 | 15 | 453 | FINANCIAL(table) | Depreciation & Amortisation: 19 \| 15 (YoY 33%) \| 20 (QoQ -0.3%) \| FY26 66 | |
| DP103 | 15 | 454 | FINANCIAL(table) | Other Income: 17 \| 11 (YoY 46%) \| 11 (QoQ 57%) \| FY26 49 | |
| DP104 | 15 | 455 | FINANCIAL(table) | Interest Expenses: 56 \| 50 (YoY 12%) \| 54 (QoQ 3%) \| FY26 219 | |
| DP105 | 15 | 456 | FINANCIAL(table) | PBT: 144 \| 147 (YoY -2%) \| 144 (QoQ 0.3%) \| FY26 584 | |
| DP106 | 15 | 457 | FINANCIAL(table) | *Exceptional Items: Q1FY27 "-" \| Q1FY26 "-" \| Q4FY26 "-" \| FY26 17 | ZERO_STANDING for Q1FY27/Q1FY26/Q4FY26 columns — line exists because a one-time labour-code provision transaction occurred in FY26 (Q3FY26 per DP047) and is nil in the current/comparative quarters; template signal, not dropped |
| DP107 | 15 | 458 | FINANCIAL(table) | Taxes: 36 \| 42 (YoY -13%) \| 47 (QoQ -23%) \| FY26 163 | |
| DP108 | 15 | 459 | FINANCIAL(table) | Profit After Tax: 108 \| 105 (YoY 3%) \| 97 (QoQ 12%) \| FY26 404 | see DATA_INCONSISTENCY flag on DP094 |
| DP109 | 15 | 460 | FINANCIAL(table) | PAT margin %: 6.2% \| 6.3% \| 5.2% \| FY26 5.8% | |
| DP110 | 15 | 461 | FINANCIAL(table) | EPS Basic: 8.04 \| 7.84 \| 7.21 \| FY26 30.09 | |
| DP111 | 15 | 462 | FINANCIAL(table) | EPS Diluted: 7.99 \| 7.78 \| 7.17 \| FY26 29.92 | |
| DP112 | 15 | 465 | FOOTNOTE | *Exceptional item includes the impact of additional provision as per new labour code | qualifies DP106/DP047 |
| DP113 | 16 | 474-475 | MIX | Order Inflow geography mix: Domestic 37% / International 63% | |
| DP114 | 16 | 480-482 | ORDER_BOOK | Order Intake for Q1FY27: Rs.1,034 cr | |
| DP115 | 16 | 474,476,485,487 | MIX | Order inflow segment mix (pie labels): Power T&D 88%; remaining ~7% and ~5% split across Civil / Pole & Lighting | CHART_VALUE_ORDER_AMBIGUOUS — pdftotext extraction order of pie-chart % labels vs segment legend not visually confirmable from text layer alone; page not flagged for OCR in A1 header |
| DP116 | 16 | 474-475 | MIX | Un-executed Order Book geography mix: Domestic 59% / International 41% | |
| DP117 | 16 | 480-481 | ORDER_BOOK | Un-executed Order Book: Rs.15,635 cr as of June 2026 | 15,635 + L1 400 (DP119) = 16,035, internally consistent |
| DP118 | 16 | 475-476,485,487 | MIX | Un-executed order book segment mix (pie labels): Power T&D 92%; remaining ~2%, ~1%, ~5% split across Civil / Railways / Pole & Lighting | CHART_VALUE_ORDER_AMBIGUOUS, same caveat as DP115 |
| DP119 | 16 | 493 | ORDER_BOOK | Total Un-executed Orderbook Rs.16,035 cr as on 30 June 2026 (incl. L1 of Rs.400 cr) | cross-checks DP021 (slide 5) exactly — consistent |
| DP120 | 16 | 496-498 | GUIDANCE/STRATEGIC | Five callouts: stable order inflow across businesses; Power T&D primary growth driver; balanced domestic/international mix; healthy margin-led new orders; robust tender pipeline | qualitative, no numeric backing given |
| DP121 | 17 | 510 | ORDER_BOOK(project) | Koppal-II PS – Narendra 765 kV D/C line, Karnataka | |
| DP122 | 17 | 510 | ORDER_BOOK(project) | TaZa 400 kV D/C line, Tanzania — cross-country project | |
| DP123 | 17 | 510 | ORDER_BOOK(project) | 220 kV D/C Phyang-North Pullu T/L, Ladakh — high-altitude project | |
| DP124 | 17 | 510 | ORDER_BOOK(project) | Begusarai elevated road project, Bihar | |
| DP125 | 17 | 516 | ORDER_BOOK(project) | 275 m tall Twin Flue RCC chimney, Koderma (KTPS) Phase-II, Jharkhand | |
| DP126 | 17 | 516 | ORDER_BOOK(project) | 765 kV D/C Dausa-Ghiror TL project, Rajasthan | |
| DP127 | 17 | 516 | ORDER_BOOK(project) | Mmamabula 400 kV substation, Botswana | |
| DP128 | 17 | 516 | ORDER_BOOK(project) | 400 kV Quad New Butwal to Indian Border Transmission Line Project, Nepal | |
| DP129 | 18 | 529 | BALANCE_SHEET | LT Borrowings: 30 Jun 2026 58.92 \| 31 Mar 2026 88.53 \| Inc/(Dec) -29.61 | |
| DP130 | 18 | 536 | BALANCE_SHEET | ST Borrowings: 716.97 \| 572.23 \| 144.74 | |
| DP131 | 18 | 537 | BALANCE_SHEET | Cash and cash equivalents (Less): 228.18 \| 393.77 \| -165.59 | |
| DP132 | 18 | 539 | BALANCE_SHEET | IPO Funds (Less): 81.29 \| 92.79 | no Inc/(Dec) figure shown for this row — blank cell, not a dash; distinct from ZERO_STANDING |
| DP133 | 18 | 540 | BALANCE_SHEET | Net Debt with IPO Funds: 466.42 \| 174.2 \| 292.22 | NOTABLE_SWING — net debt +168% QoQ (174.2 to 466.42) |
| DP134 | 18 | 541 | FOOTNOTE | Previous period figures are restated | |
| DP135 | 18 | 529-538 | BALANCE_SHEET | India Ratings upgraded credit rating to IND AA-/Stable in August 2026, reflecting strengthened business and financial profile | duplicate of DP083 |
| DP136 | 18 | 561 | BALANCE_SHEET | Long Term Credit Rating: CRISIL AA-/Stable | |
| DP137 | 18 | 561 | BALANCE_SHEET | Long Term Credit Rating: IND AA-/Stable | |
| DP138 | 18 | 561 | BALANCE_SHEET | Short Term Credit Rating: CRISIL A1+ | |
| DP139 | 18 | 561 | BALANCE_SHEET | Short Term Credit Rating: IND A1+ | |
| DP140 | 18 | 548,554,558 | OTHER | Decorative rating-scale graphic (A / A+ / AA- / AA / B+ / A1 / A1+ ladder) framing the four ratings above | visual reference only, no new numeric disclosure |
| DP141 | 19 | 580,583,589,600 | BALANCE_SHEET | Debt to Equity (x) by year — values present in source text: 0.78, 0.56, 0.34, 0.29, 0.32 against axis FY23/FY24/FY25/FY26/Q1FY27 | CHART_VALUE_ORDER_AMBIGUOUS — chart-derived text extracted out of visual left-to-right order by pdftotext; value-to-year pairing above is presented in raw reading order, not confirmed against the rendered chart |
| DP142 | 19 | 572,580,582,589,599 | BALANCE_SHEET | Net Debt (₹Cr) by year — values present in source text: 480, 502, 533, 267, 548 against axis FY23/FY24/FY25/FY26/Q1FY27 | CHART_VALUE_ORDER_AMBIGUOUS; also DEFINITION_MISMATCH_NET_DEBT — none of these values equal DP133's "Net Debt with IPO Funds" (466.42 for Q1FY27), so this chart appears to use a different net-debt definition (e.g., without IPO-fund offset) that is not labelled as such |
| DP143 | 19 | 572 | BALANCE_SHEET | Net Debt to EBITDA (x) by year — values present in source text: 1.63, 1.12, 0.74, 0.33, 0.67 against axis FY23/FY24/FY25/FY26/Q1FY27 | CHART_VALUE_ORDER_AMBIGUOUS |
| DP144 | 19 | 609,611,617 | FINANCIAL | Return on Capital Employed (%): FY23 18.27% / FY24 24.33% / FY25 24.70% / FY26 25.76% / Q1FY27 23.58% | axis order given directly in source (line 616/617), lower ambiguity than DP141-143 |
| DP145 | 19 | 608,610,612,615 | BALANCE_SHEET | Working Capital Days: FY23 53 / FY24 73 / FY25 91 / FY26 81 / Q1FY27 85 | axis order given directly in source (line 615) |
| DP146 | 19 | 619 | FOOTNOTE | Previous period figures are restated wherever applicable | |
| DP147 | 21 | 635-667 | CAPACITY | Power T&D capabilities: manufacturing (towers, conductors & monopoles); EPC — TL up to 1200 kV, AIS/GIS substations up to 765 kV, UG cabling, rural electrification, HVDC lines 800 kV, HTLS conductors | |
| DP148 | 21 | 635-644 | SEGMENT | Civil Construction capabilities: bridges, tunnels, elevated roads, cooling towers | |
| DP149 | 21 | 635-648 | SEGMENT | Poles & Lighting capabilities: high masts/flag masts, street poles, luminaries, stadium lighting, derrick structures, railway portals, road gantries & signages, solar streetlights, decorative poles | |
| DP150 | 21 | 651-664 | SEGMENT | Railways capabilities: overhead electrification, traction substation, signaling & telecom services, track laying, other composite works | |
| DP151 | 21 | 651-666 | SEGMENT | Solar EPC (International) capabilities: institutional solar, commercial & industrial solar, solar parks, utility scale projects, mini grids | |
| DP152 | 22 | 676-677 | GEOGRAPHY | India: ongoing projects 50+; over 300 projects completed | |
| DP153 | 22 | 678-682 | CAPACITY | India capability detail: 765kV/800kV HVDC turnkey EPC, AIS & GIS substations, rural electrification, UG cabling, factories for towers/conductors/monopoles, diversified Railways/Civil/Poles & Lighting presence | |
| DP154 | 22 | 685 | GEOGRAPHY | Africa: footprint in over 28 African countries across all regions | |
| DP155 | 22 | 686-689 | STRATEGIC | Africa projects funded by World Bank, AfDB, EBID, KfW, and BOAD | |
| DP156 | 22 | 692-694 | GEOGRAPHY | Rest of Asia: strong presence across SAARC, Southeast Asia | |
| DP157 | 22 | 696-698 | GEOGRAPHY | GCC: supply of towers and poles; turnkey EPC of transmission lines | |
| DP158 | 22 | 700-702 | GEOGRAPHY | Americas & Europe: supply of towers and conductors; solar EPC projects being executed | |
| DP159 | 22 | 704-705 | GEOGRAPHY | Australia: supply of engineered products | cross-ref DP085 (first Monopole project in Australia, Q1FY27) |
| DP160 | 22 | 701-703 | GEOGRAPHY/SCALE | Footprint across 64 countries & 6 continents; Active Projects in India: 50+; Active Countries: 20+; Projects: 30+ | |
| DP161 | 23 | 719 | CAPACITY | Tower Factory — Deoli | |
| DP162 | 23 | 719 | CAPACITY | Conductor Factory — Silvassa | |
| DP163 | 23 | 726 | CAPACITY | Tower Factory — Vadodara | |
| DP164 | 23 | 726 | CAPACITY | Pole Factory — Silvassa | |
| DP165 | 23 | 735 | CAPACITY | Tower Testing Facility — Deoli | |
| DP166 | 23 | 735 | CAPACITY | New Tower Factory — Butibori | cross-ref DP084 (commissioning announced Q1FY27) |
| DP167 | 23 | 714-726 | STRATEGIC | Global-grade technology: precision CNC systems (Italy); high-capacity galvanizing (UK) | |
| DP168 | 23 | 720-724 | CAPACITY | In-house testing & R&D: NABL-accredited tower testing; certified quality systems (CE, ISO, NABL) | |
| DP169 | 23 | 726 | CAPACITY | "Engineered for scale and complexity, supporting projects up to 1200 kV" | |
| DP170 | 23 | 730-734 | OTHER (awards) | NSCI Certificate of Merit 2025 – Deoli Plant; Deoli Tower Plant 'A Grade' – POWERGRID; European conformity certified; ISO certified; NABL Certified | |
| DP171 | 24 | 745-746 | CAPACITY | "Tower manufacturing capacity was doubled to 172,400 MTPA in FY26" (narrative headline) | DATA_INCONSISTENCY vs DP172: 84,000 MTPA doubled = 168,000 MTPA, not 172,400; also does not equal the 196,000 MTPA post-CAPEX total stated in the table on the same slide |
| DP172 | 24 | 751 | CAPACITY | Towers: Pre-CAPEX 84,000 MTPA -> Post-CAPEX (Phase 1 + Phase 2) 196,000 MTPA | DATA_INCONSISTENCY vs DP171 — three different tower-capacity figures appear across one slide (172,400 narrative; 84,000 pre / 196,000 post table) with no reconciling note |
| DP173 | 24 | 752 | CAPACITY | Conductors: Pre-CAPEX 24,000 km -> Post-CAPEX 49,500 km | |
| DP174 | 24 | 749-751 | GUIDANCE(timeline) | Towers — Phase 1 brownfield: Completed; Phase 1 greenfield: Completed; Phase 2 brownfield: By Q2FY27 | |
| DP175 | 24 | 749-752 | GUIDANCE(timeline) | Conductors — Phase 1 brownfield: By Q2FY27; Phase 1 greenfield: Not applicable; Phase 2 brownfield: By Q3FY27 | |
| DP176 | 24 | 756-760 | STRATEGIC | Brownfield expansion: existing tower, conductor and pole manufacturing plants being enhanced | |
| DP177 | 24 | 756-759 | STRATEGIC/CAPACITY | Butibori production started: new eco-friendly tower plant near Nagpur commissioned | duplicate of DP084/DP166 |
| DP178 | 24 | 764-765 | CAPEX/GUIDANCE | Additional CAPEX: ₹203 crore approved on 26 May 2026, mainly for construction equipment | |
| DP179 | 26 | 785-786 | GUIDANCE(industry) | National Electricity Plan: 191,000 CKM transmission line addition by 2032, 38% of India's total grid | industry-wide, not company-specific guidance |
| DP180 | 26 | 791-794 | GUIDANCE(industry) | 500 GW non-fossil capacity target by 2030; target 900 GW Renewable Energy by 2036 | industry-wide |
| DP181 | 26 | 797 | STRATEGIC | Manufacturing & Urbanisation: data centers, EVs and industrial corridors to drive power demand | STRATEGIC_NEW_VERTICAL — data centre demand named as a tailwind |
| DP182 | 26 | 799-801 | STRATEGIC(industry) | Government Policy Support: 1150 kV UHV line integration; Hydro Evacuation Plan | |
| DP183 | 26 | 805-806 | STRATEGIC(industry) | Private Sector Participation: growing private participation in TBCB and grid automation | |
| DP184 | 26 | 811-812 | GUIDANCE(industry) | High investment potential: ₹9.15 lakh crore transmission investments planned by 2032 | industry-wide, not company order book |
| DP185 | 26 | 792 | GUIDANCE(industry) | Global electricity demand expected to nearly double by 2050 | industry-wide |
| DP186 | 26 | 797 | STRATEGIC(industry) | Africa's Electrification & Connectivity Drive: Mission 300 to connect 300 million people to electricity | industry-wide |
| DP187 | 26 | 799-800 | STRATEGIC(industry) | Policy Push & Green Financing Support for T&D investments | industry-wide |
| DP188 | 26 | 805-806 | STRATEGIC(industry) | Smart Grid Technologies and Digitalisation enhancing reliability and efficiency | industry-wide |
| DP189 | 26 | 811-812 | STRATEGIC(industry) | Cross Border Power Connectivity Initiatives: regional interconnections strengthening energy security | industry-wide |
| DP190 | 27 | 824-830 | STRATEGIC | Core Capabilities (7 bullets): integrated EPC & manufacturing; proven TL/substation execution; in-house D&E and testing; global presence; increased capacities; robust financials; strong customer relations | |
| DP191 | 27 | 835-839 | STRATEGIC | Conventional-business growth drivers: grid additions in India; more renewable share; ICB (MDB-funded) market prominence in Africa/SAARC | |
| DP192 | 27 | 835-840 | STRATEGIC | New-age requirements growth drivers: HVDC transmission lines; HTLS conductors; supply to developed economies; Power Infra EPC for data centers; BESS EPC | STRATEGIC_NEW_VERTICAL — explicit BESS EPC and data-centre power infra named as growth avenues; no revenue/order contribution yet disclosed |
| DP193 | 27 | 835-840 | STRATEGIC | Diversification growth drivers: railway opportunities (India/Africa); civil infra (tunnels/bridges/cooling towers); Solar EPC (mainly international); Pole & Lighting (vast product range) | |
| DP194 | 29 | 860-861 | ESG | Commitment to building stronger communities: healthcare, education, sanitation, inclusive growth | qualitative, no metric |
| DP195 | 29 | 864-867 | ESG | Environment pillar: reduce environmental impact via efficient use/recycling/reuse; sustainability embedded across operations | qualitative |
| DP196 | 29 | 871-874 | ESG | Social pillar: healthcare, education, rural development, skill development; NGO partnerships; gender diversity emphasis | qualitative |
| DP197 | 29 | 878-884 | ESG/GOVERNANCE | Governance pillar: robust governance framework; policies aligned with sustainability/reliability/ethics; community development initiatives; health camps/awareness programs | qualitative |
| DP198 | 30 | 894-895 | CSR | Two CSR flagship programs: "Transrail Aarogya" and "Transrail Saksharta" | |
| DP199 | 30 | 900-902 | CSR | 3,235 free treatments and services provided (general medical treatment) | |
| DP200 | 30 | 903-904 | CSR | 110 eye screening and treatment with free spectacle support through camps | |
| DP201 | 30 | 905-906 | CSR | 230 mentally abled children benefited with free medical treatment | |
| DP202 | 30 | 907 | CSR | 48 cataract surgeries support in Bihar | |
| DP203 | 30 | 909-910 | CSR (forward) | Additional free medical treatment and support planned in due course | |
| DP204 | 30 | 912-913 | CSR | 975 students from 8th to 10th continuing supported classes | |
| DP205 | 30 | 914-915 | CSR | STEM Lab developed in Govt school Vadodara; 350 children benefiting through STEM classes | |
| DP206 | 30 | 917-918 | CSR (forward) | Education material distribution for children is in process | |
| DP207 | 30 | 909-910 | CSR | 45 learners in continuing training | |
| DP208 | 30 | 912 | CSR | 45 continuing skill training course in two centers on BFSI, Tally and BPO & Retail | |
| DP209 | 30 | 913 | CSR | 100 students mobilized for training skill training | |
| DP210 | 30 | 914 | CSR | Mobilization through awareness & home visit of students | qualitative |
| DP211 | 30 | 916 | CSR | Placement process for students | qualitative |
| DP212 | 31 | 931-934 | STRATEGIC/PR | MD & CEO Randeep Narang represented the Company as panelist at India Energy Forum's National Conference on Power Transmission | |
| DP213 | 31 | 939-940 | OTHER (award) | Awarded ET Edge "Best Organisations to Work" 2026 | REPEAT_DATA_POINT with DP089 (slide 13) |
| DP214 | 31 | 939-940 | OTHER (award) | Awarded RoSPA Silver Award for Cameroon TL project, Health & Safety | REPEAT_DATA_POINT with DP090 (slide 13) |
| DP215 | 31 | 939-940 | OTHER | Participation at IEEE PES T&D 2026, Chicago | |
| DP216 | 31 | 944 | OTHER | [CHART OCR] Event banner text: "National Conference on Power Transmission — Powering Viksit Bharat 2047: The Transmission Imperative, Friday 29th May 2026, Hotel Le Meridien, New Delhi" | OCR-supplemented, photo banner not in text layer |
| DP217 | 32 | 948-952 | OTHER | Corporate Office address: A Wing, 5th Floor, Fortune 2000, BKC, Bandra East, Mumbai – 400051, India | |
| DP218 | 32 | 954-956 | OTHER | Investor Relations contact: Manasi Bodas, investor.relations@transraillighting.com | |
| DP219 | 32 | 957 | OTHER | Website: www.transrail.in | |
| DP220 | 32 | 958 | OTHER | CIN: L31506MH2008PLC179012 \| NSE: TRANSRAILL \| BSE: 544317 | |
| DP221 | 4/11/20/25/28 | 106,336,623,771,847 | OTHER | Five section-divider slides carrying only a title and page number, no data content: "Corporate Overview" (4), "Q1FY27 Highlights" (11), "Business Overview" (20), "Industry Tailwinds" (25), "ESG , CSR and Awards" (28) | grouped as one ledger row per rule against dropping content-free slides — each divider is individually indexed in Table A |

---
## TABLE C — FOOTNOTES & FINE-PRINT DISCLAIMERS (4 rows, grep=4, sweep=4, match)

| # | Slide | Line | Text | Qualifies |
|---|---|---|---|---|
| F1 | 8 | 255 | "* PAT excludes provision made of ₹17 Cr in Q3 FY26 towards new labour code" | DP046 (FY26 PAT 421 in the 5-yr chart) |
| F2 | 15 | 465 | "*Exceptional item includes the impact of additional provision as per new labour code" | DP106/DP112 (Exceptional Items row, FY26 column = 17) |
| F3 | 18 | 541 | "Previous period figures are restated" | DP129-DP133 (balance sheet comparatives) |
| F4 | 19 | 619 | "Previous period figures are restated wherever applicable" | DP141-DP145 (leverage/RoCE/WC-days comparatives) |

Note: F1/F2 are the same underlying ₹17 Cr labour-code provision referenced twice
(FY26 P&L chart and FY26 Exceptional Items table row) — internally consistent,
not a duplicate disclosure error.

---
## TABLE D — CHART OCR SUPPLEMENTS (3 rows, grep=3, sweep=3, match)

| # | Slide | Line | OCR content |
|---|---|---|---|
| C1 | 8 | 260 | CAGR WordArt labels: Order Book 26%, Revenue 31%, EBITDA 41%, PAT 59% (FY22-FY26) |
| C2 | 14 | 438 | CAGR WordArt labels: Revenue 38%, EBITDA 30%, PBT 36%, PAT 44% (Q1FY25-Q1FY27) |
| C3 | 31 | 944 | Event banner photo text: National Conference on Power Transmission, 29 May 2026, Hotel Le Meridien New Delhi |

---
## TABLE E — FLAGS RAISED (summary, cross-referenced to DP rows above)

| Flag | Instances | DP rows |
|---|---|---|
| ZERO_STANDING | 1 | DP106 |
| DATA_INCONSISTENCY | 2 | DP094/DP108 (Q1FY26 PAT: 106 vs 105); DP171/DP172 (tower capacity: 172,400 narrative vs 84,000->196,000 table) |
| CHART_VALUE_ORDER_AMBIGUOUS | 5 | DP115, DP118, DP141, DP142, DP143 |
| DEFINITION_MISMATCH_NET_DEBT | 1 | DP142 vs DP133 |
| REPEAT_DATA_POINT | 7 pairs | DP075/DP080, DP076/DP081, DP077/DP082, DP078/DP079, DP089/DP213, DP090/DP214, DP055/DP067 |
| DUAL_CFO_TITLE | 1 | DP068/DP069 |
| M&A_DISCLOSURE | 1 | DP087 (Gactel Turnkey Projects acquisition, no terms disclosed on this slide) |
| STRATEGIC_NEW_VERTICAL | 2 | DP181 (data centre demand), DP192 (BESS EPC / data centre power infra) |
| NOTABLE_SWING | 1 | DP133 (net debt +168% QoQ) |
| SIGNATORY_NAME_MISMATCH | 1 | DP006 (digital signature shows "Tanay Gandhi" against printed signatory "Monica Gandhi") |
| PRIOR_LEDGER_UNAVAILABLE | 1 | Table A note (DROPPED_SLIDE check not performable) |

Explicitly checked and absent from this deck: no mention of QIP / equity capital
raise, and no mention of defence-sector entry (grep -in "QIP\|qualified
institutions placement\|defence\|defense" = no matches). Noted as confirmed
absent, not merely unsearched.

---
## OUTPUT PATH
/home/user/inflection-pipeline/runs/transrail-q1fy27/work/ledger_presentation_transrail_q1fy27.md
