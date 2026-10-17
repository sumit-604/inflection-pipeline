# A2 LEDGER: INDORAMA Q2 FY27 pressrelease (Reg 30 cover + media release, 3 pages)
ids_in_structured: 132 | ids_referenced_in_ledger: 132 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: all_ids            grep_count: 132  sweep_count: 132  match: yes
category: type NUMBER        grep_count: 94   sweep_count: 94   match: yes
category: type ENTITY(+SUM)  grep_count: 16   sweep_count: 16   match: yes (13+3)
category: type FORWARD       grep_count: 3    sweep_count: 3    match: yes
category: type DATE          grep_count: 8    sweep_count: 8    match: yes
category: type QUALIFIER     grep_count: 11   sweep_count: 11   match: yes
category: line_items (table rows)  grep_count: 6  sweep_count: 6  match: yes
category: notes              grep_count: 0    sweep_count: 0    match: yes (no numbered notes; doc is press release)
category: auditor_paras      0 (none in doc)   agenda_items 0 (none)   entities_consolidation 0 (none)
category: slides/pages       grep_count: 3    sweep_count: 3    match: yes
gate_a2: pass
=== END COUNT TEST ===

## A. Pages (slides): 3
| ID range | page | content | flags/note |
|---|---|---|---|
| R001-R020 | 1 | Reg 30 cover letter, addressees, signature | text |
| R021-R100 | 2 | headline, cards, table, narrative | table + text |
| R101-R132 | 3 | CMD quote, outlook, about, disclaimer | text |

## B. Financial table line items (page 2, columns Q2FY27, Q2FY26, YoY, Q1FY27, QoQ, H1FY27, H1FY26, H1 chg)
| ROW IDs | line item | flags | note |
|---|---|---|---|
| R033-R040 | Total Income | none | H1 -9.7% (R040) stated cause R080 |
| R041-R048 | EBITDA | none | |
| R049-R053 | EBITDA Margin | none | no YoY/QoQ cells |
| R054-R061 | EBIT | none | |
| R062-R069 | PAT | OCR_GLYPH_DOUBT on R063 | R063 table 246 vs R092 body 24.6; R064 201.8% fits 24.6 |
| R070-R074 | PAT Margin | none | |
Table-basis: R031 (consolidated), R032 (unit glyph). zero_standing: 0 (no nil or dash rows).

## C. Restated numbers (flag RESTATED)
| ROW IDs | value |
|---|---|
| R014,R021,R035,R076 | Revenue +10% / 10.0% YoY |
| R015,R022,R064,R093 | PAT +202% / 201.8% |
| R027,R033,R075,R105 | Total Income Q2FY27 1,344 |
| R028,R041,R083,R106 | EBITDA Q2FY27 117.7 |
| R029,R062,R091,R108 | PAT Q2FY27 74.1 |
| R037,R077 | QoQ 43.0% |
| R038,R078,R109 | H1 Total Income 2,284.2 |
| R040,R079 | H1 -9.7% |
| R042,R084 | EBITDA Q2FY26 80.4 |
| R043,R082 | EBITDA YoY 46.4% |
| R046,R086,R110 | EBITDA H1 225.7 |
| R048,R085 | EBITDA H1 +24.9% |
| R049,R087,R107 | margin 8.8% |
| R050,R088 | margin 6.6% |
| R052,R089,R111 | margin 9.9% |
| R053,R090 | margin 7.1% |
| R063,R092 | PAT Q2FY26 (conflict 246 vs 24.6) |
| R067,R095,R112 | PAT H1 137.8 |
| R069,R094 | PAT H1 +78.3% |
| R070,R096 | PAT margin 5.5% |
| R071,R097 | 2.0% |
| R073,R098 | 6.0% |
| R074,R099 | 3.1% |
| R100 | periods |
| R011,R001,R023 | letter/release dates |
| R012,R025 | results period |
| R019,R130 | CIN |
| R020,R130 | contact/address |

## D. Remaining row accounting by category
| IDs | category | flags / note |
|---|---|---|
| R002,R005,R006,R009,R017,R019 | admin identifiers | none |
| R003,R004,R007,R008 | exchange addressees/codes | none |
| R010 | Reg 30 basis | |
| R013 | unaudited results | unaudited; no auditor report in doc |
| R016,R017,R018 | signatory: Ashok Yadav CS, ACS 14223, timestamp 2026.10.16 21:47:58 +05'30' | timestamp vs board meeting end: board times NOT in doc |
| R020,R130 | address/contact blocks | |
| R024 | issuer | |
| R026,R030 | card basis; card YoY values missing | FOOTNOTE_UNRESOLVED (R030) |
| R031,R032 | table basis, unit | |
| R080,R081 | H1 degrowth cause: Middle East supply chain | materiality: management attribution, no figures |
| R101-R104 | CMD (Om Prakash Lohia) quote, crude-cost driver | CMD present as quoted speaker |
| R113 | FORWARD focus, no figures | hedge-type, no numbers |
| R114,R115,R116 | FORWARD Rs 200 cr capex, 12-18 months, specialty fibre/filament | key; GROUP; no funding source stated in doc |
| R117 | FORWARD expected benefits | |
| R118-R129 | company profile: capacities 6.72 lakh TPA, PET 2.52, DTY 1.75, 71.08 MW standby captive, 19 states, 28 countries | R129 qualifier standby |
| R126 | tech providers | |
| R131,R132 | safe harbor | covers R113-R117 |

## E. Absences (units expected but not in doc)
Board outcome agenda, board meeting times, auditor report/limited review, consolidation entity list, segment data, balance sheet, cash flow, notes: none present (press release only). Card YoY percentages unresolved (R030).
MISSING_FROM_STRUCTURED: none.
