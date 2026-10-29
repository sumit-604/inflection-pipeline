# A2 LEDGER: Route Mobile Limited (ROUTE), Q2 FY27, Investor Presentation

Source: A1 structured R001-R368 (23 slides). Rows referenced by ID; claim text stays in the structured file.

=== A2 COUNT TEST ===
category: slides        grep_count: 23   sweep_count: 23   match: yes   (grep -c '^\[page' fulltext; 20 slides carry rows, 3 dividers p6/p11/p15 carry none, p23 closing carries 1)
category: slide_numbers  grep_count: 252   sweep_count: 252   match: yes   (grep '| NUMBER |' = header NUMBER 252; per-slide sweep below sums to 252)
category: zero_standing  grep_count: 18   sweep_count: 18   match: yes   (grep -c ZERO_STANDING; all on slide 19 reconciliation table)
category: entities     grep_count: 32   sweep_count: 32   match: yes   (ENTITY 30 + ENTITY-SUMMARY 2)
category: forward      grep_count: 19   sweep_count: 19   match: yes
category: dates        grep_count: 32   sweep_count: 32   match: yes
category: qualifiers   grep_count: 33   sweep_count: 33   match: yes   (footnotes and fine print)
gate_a2: pass
=== END COUNT TEST ===

ids_in_structured: 368 | ids_referenced_in_ledger: 368 | orphan_ids: [] | match: yes

## TABLE 1 SLIDE INVENTORY (23)
| # | Title | Type | IDs on slide | Flags |
|---|---|---|---|---|
| 1 | Reg 30 covering letter | text | R001-R012 (12) | - |
| 2 | Earnings Update H1 FY 26-27 (title) | text | R013-R014 (2) | - |
| 3 | Safe Harbor | text | R015-R017 (3) | - |
| 4 | Route Mobile - Industry Leading Global CPaaS Platform | text+stat callouts | R018-R038 (21) | - |
| 5 | Global Diaspora - Footprint & Super Network | map/infographic | R039-R058 (20) | - |
| 6 | Key Developments | section divider, no data | none (no rows) (0) | SECTION_DIVIDER |
| 7 | Commercial Highlights | text | R059-R068 (10) | - |
| 8 | Heltar - Strategic fit with Route Mobile | text/graphic | R069-R077 (9) | NEW_SLIDE |
| 9 | From marquee anchor customers to a scaling AI business (Heltar) | text/graphic | R078-R095 (18) | NEW_SLIDE |
| 10 | Focus on Expanding Product Portfolio | text+chart | R096-R103 (8) | - |
| 11 | Key Business Metrics | section divider, no data | none (no rows) (0) | SECTION_DIVIDER |
| 12 | Diverse Customer Base | chart | R104-R130 (27) | OCR_RE-EXTRACTED |
| 13 | Customer Cohort Analysis | chart | R131-R154 (24) | RE-EXTRACTED |
| 14 | Strong Recurring Revenue | chart+text | R155-R163 (9) | NEW_SLIDE |
| 15 | Financial Highlights | section divider, no data | none (no rows) (0) | SECTION_DIVIDER |
| 16 | Analysis of Q2 FY 26-27 Performance | chart+text | R164-R185 (22) | - |
| 17 | Analysis of Q2 FY 26-27 Performance (continued) | chart+text | R186-R223, R352 (39) | RE-EXTRACTED |
| 18 | H1 FY 26-27 Performance | chart+text | R224-R247 (24) | NEW_SLIDE ; RE-EXTRACTED |
| 19 | Adjusted EBITDA/PAT | table | R248-R302, R353-R367 (70) | ZERO_STANDING ; RE-EXTRACTED |
| 20 | Cash Flow Conversion | table | R303-R322 (20) | NEW_SLIDE ; RE-EXTRACTED |
| 21 | Working Capital Trend | chart | R323-R334 (12) | NEW_SLIDE ; RE-EXTRACTED |
| 22 | Human Resource Capital | chart | R335-R350, R368 (17) | RE-EXTRACTED |
| 23 | Thank You | closing, website only | R351 (1) | - |

Page 17 also holds R352; page 19 holds R353-R367; page 22 holds R368 (added by re-extraction, out of page order in the structured file).

## TABLE 2 SLIDE NUMBERS (NUMBER rows, 252) by slide
| Slide | NUMBER IDs | n | Flags |
|---|---|---|---|
| 1 | R001, R003, R012 | 3 | - |
| 4 | R018-R031 | 14 | - |
| 5 | R039-R055 | 17 | - |
| 9 | R078-R083 | 6 | - |
| 10 | R096-R100 | 5 | - |
| 12 | R105-R124 | 20 | - |
| 13 | R131-R150 | 20 | - |
| 14 | R155-R158 | 4 | - |
| 16 | R164-R181 | 18 | - |
| 17 | R186-R214, R352 | 30 | - |
| 18 | R224-R243 | 20 | - |
| 19 | R248-R292, R353-R367 | 60 | ZERO_STANDING on R290-R292, R353-R367 |
| 20 | R303-R315 | 13 | - |
| 21 | R323-R332 | 10 | - |
| 22 | R335-R345, R368 | 12 | - |

## TABLE 3 ZERO_STANDING (dash-valued standing items, slide 19 reconciliation, 18)
IDs: R290-R292, R353-R367. Lines: ESOP expense (add-back) Q2FY27/Q1FY27/H1FY27 = R290-R292; FX net loss Q2FY27/Q1FY27/Q2FY26/H1FY27 = R353-R356; Capital advance loss allowance Q2FY27/Q2FY26/H1FY26 = R357-R359; Masivian breach fees Q2FY26/H1FY26 = R360-R361; Exceptional item Q2FY27/Q1FY27/H1FY27 = R362-R364; Tax impact Q2FY27/Q1FY27/H1FY27 = R365-R367. Note: Q2FY27 has no ESOP add-back and no exceptional item while the standing lines remain in template. R214 (0.0% chart axis tick) is not a zero standing item.

## TABLE 4 FOOTNOTES AND FINE PRINT (QUALIFIER, 33)
IDs: R008, R016-R017, R057, R089, R125-R128, R153-R154, R160-R161, R219-R223, R245-R247, R297-R302, R317-R321, R348. Key: R125-R126 (top-50 countries 85%, top-150 customers 91%), R154 (concentration annualized), R160-R161 (recurring and NRR definitions), R223 (Adj. PAT includes forex gain), R297-R299 (EBITDA definition, non-GAAP), R318-R319 (vendor advance in CFO), R348 (headcount excludes Call2Connect). Flag FOOTNOTE_UNRESOLVED: none raised.

## TABLE 5 ENTITIES (32)
IDs: R004-R005, R009, R011, R015, R036-R038, R058-R059, R061-R065, R067, R069, R076, R090-R092, R095, R101-R102, R129-R130, R295-R296, R322, R349-R351. ENTITY_CHANGE vs Q1: Heltar Technologies acquired (R059, R069, R090 Route Connect acquirer, R092); Marko Erkic Masiv CEO (R061). Call2Connect named as excluded from headcount (R349).

## TABLE 6 FORWARD-LOOKING (19)
IDs: R032, R070-R075, R077, R087-R088, R093-R094, R163, R182-R184, R215-R217.

## TABLE 7 DATES (32)
IDs: R002, R006-R007, R010, R013-R014, R033-R035, R056, R060, R066, R068, R084-R086, R103-R104, R151-R152, R159, R162, R185, R218, R244, R293-R294, R316, R333-R334, R346-R347.

## TABLE 8 CROSS-REFERENCES AND FLAGS
- RESTATED: 280+ direct MNO R022 / R055; 20+ data centers R028 / R053; sept-30 date R034 / R056; Adj. EBITDA/PAT footnote refs R221-R222 / R246-R247 -> slide 19 (R248-R302).
- DUPLICATE_CAPTURE: header mentions it but no row carries the marker (grep finds only the header line); all 368 IDs accounted.
- DROPPED_SLIDE vs Q1 deck: Q1 slide 'Technological Advancements' (Product, Platform & Innovation) is absent; replaced by Heltar slides 8-9. Q1 'Focus on Expanding Product Portfolio' retained as slide 10. Q1 'Human Resource Capital', 'Customer Cohort Analysis', 'Diverse Customer Base', 'Adjusted EBITDA/PAT' retained.
- NEW vs Q1: slides 8, 9 (Heltar), 14 (Strong Recurring Revenue), 18 (H1 Performance), 20 (Cash Flow Conversion), 21 (Working Capital Trend).
- MGMT_ABSENCE, REPEAT_QUESTION: not applicable to a presentation.
- MISSING_FROM_STRUCTURED: none found.
