=== A2 COUNT TEST ===
category: ids_total          grep_count: 141  sweep_count: 141  match: yes
category: NUMBER             grep_count: 79   sweep_count: 79   match: yes
category: DATE               grep_count: 13   sweep_count: 13   match: yes
category: ENTITY             grep_count: 23   sweep_count: 23   match: yes
category: FORWARD            grep_count: 13   sweep_count: 13   match: yes
category: QUALIFIER          grep_count: 13   sweep_count: 13   match: yes
category: notes (numbered)   grep_count: 0    sweep_count: 0    match: yes
category: notes (unnumbered, "Note:" block) grep_count: 1 sweep_count: 1 match: yes
category: line_items         grep_count: 14   sweep_count: 14   match: yes (Q2 table 8 rows lines 94-101; H1 table 6 rows lines 106-111)
category: table_cells        grep_count: 55   sweep_count: 55   match: yes (R013-R067)
category: zero_standing (blank cells) grep_count: 5 sweep_count: 5 match: yes
category: agenda_items       0 (no board outcome letter; cover letter + press release only)
category: auditor_paras      0 (unaudited; no auditor report in document)
category: entities           23 (R093-R115); no prior ledger, ENTITY_CHANGE not testable
category: slides             4 pages (press release run as presentation-class)
ids_in_structured: 141 | ids_referenced_in_ledger: 141 | orphan_ids: [] | match: yes
gate_a2: pass
=== END COUNT TEST ===

Note: the doc is a 4-page press release, not a deck. Slides = pages 1-4. No prior ledger: no DROPPED_SLIDE test.

## 1. Pages (slide analogue)
page | content type | IDs
1 | text (cover letter to BSE/NSE) | R074-R083 (R080-R083 dates), R093-R098, R114, R134-R136
2 | text (press release, CEO quote) | R001-R012, R073, R084-R086, R099-R106, R116-R125, R132-R133
3 | table + text (Q2 table, H1 table, business highlights) | R013-R071, R087-R091, R107-R108, R126-R127, R129-R131, R141
4 | text (About, contacts, safe-harbor Note) | R072, R092, R109-R113, R115, R128, R137-R140

## 2. Financial table line items (Q2 table, page 3)
ROW_ID range | line item | flags | note
R013-R017 | Operating revenue (Q2FY27, Q2FY26, YoY, Q1FY27, QoQ) | | headline 24.7% YoY matches R004
R018-R022 | Total revenue | | R001/R006 restate R018; R002/R007 restate R020
R023-R027 | EBITDA | | R025 YoY 2.0% (image-corrected); R027 QoQ -7.8%
R028-R031 | EBITDA margin | ZERO_STANDING (R030 blank YoY) | margin 18.8 to 16.4
R032-R036 | PBT | | R034 YoY 1.2% (image-corrected); R036 QoQ -8.5%
R037-R040 | PBT margin | ZERO_STANDING (R039 blank YoY) |
R041-R045 | PAT | | R043 YoY 0.3% (image-corrected); R008 restates R041; R045 -8.4% QoQ
R046-R049 | PAT margin | ZERO_STANDING (R048 blank YoY) |

## 3. Financial table line items (H1 table, page 3)
R050-R052 | Operating revenue H1 | RESTATED | R009/R010 restate R052/R050
R053-R055 | Total revenue H1 | |
R056-R058 | EBITDA H1 | | R058 YoY 8.9% (image-corrected)
R059-R061 | EBITDA margin H1 | ZERO_STANDING (R061 blank YoY) |
R062-R064 | PAT H1 | | R064 YoY 7.9% (image-corrected); R012 restates R062
R065-R067 | PAT margin H1 | ZERO_STANDING (R067 blank YoY) | R011 states 7.9% as PAT growth, consistent with R064
Note: no PBT row in H1 table (Q2 table has one). No other-income or finance-cost lines in either table.

## 4. ZERO_STANDING rows (blank cells)
R030, R039, R048, R061, R067 (count 5). All are YoY cells on margin rows (blank in the rendered image). Profit-row YoY cells R025, R034, R043, R058, R064 now carry values (A1 correction, R141). COLUMN_ANOMALY retracted: it was a text-layer extraction artifact.

## 5. Notes
Numbered notes: none.
Unnumbered Note block (page 4, lines 140-145): R137, R138, R139, R140 (one note, four rows). Companion R128 safe-harbor opener.
Table unit qualifiers: R129, R130 (currency symbol absent from text layer; units INR million per A1 header).

## 6. Other numbers (non-table)
R001-R012 headline/quote numbers, RESTATED from tables. R005 7.1% QoQ = R017.
R068-R071 | business highlights: 96 clients (LTM, R131), 68% Technology (R069 / R107), 99% US (R070 / R108), 529 employees (R071)
R072 | founding year 1995 (RESTATED R092)
R073, R074 | BSE scrip code 532173, appears twice
R075-R079 | admin/identifier numbers, low materiality

## 7. Dates
R080 cover 23 Oct 2026; R084 press release dateline 22 Oct 2026. Flag DATE_MISMATCH: one day apart (R080 vs R084).
R083 signature timestamp 2026.10.23 16:09:02 +05:30. No board meeting time in this document; sign-before-meeting test not possible.
R081, R082, R085, R086, R087, R088, R089, R090, R091, R092: period and as-of dates.

## 8. Entities (R093-R115, 23)
R093 BSE; R094 NSE; R095 SEBI LODR; R096 Sarita Leelaramani; R097 filer; R098 website; R099 CMMI Level 3; R100 Vish Tadimety; R101 Esri Platinum (CEO quote); R102 Managed ArcGIS; R103 GeoAI; R104 SAP S/4HANA/BTP; R105 SAP Migration Factory; R106 AWS, Azure; R107 Technology sector; R108 US business; R109 Esri Gold, SAP Gold (About); R110 service lines; R111 industries; R112 footprint; R113 Saumitra Banerjee; R114 summary letterhead; R115 summary contact.
Flags: R101 vs R109 = PARTNER_TIER_CONFLICT (Esri Platinum p2 vs Gold p4). R114, R115 summary rows (no new entity). No subsidiaries or consolidation list in document. No prior list: ENTITY_CHANGE not testable.

## 9. Forward-looking (R116-R128, 13)
R116-R127 management statements, all qualitative, no quantified guidance. R128 safe-harbor. Flag NO_QUANT_GUIDANCE. R117 claims revenue grew faster than delivery costs with no figure (UNQUANTIFIED_CLAIM); table shows EBITDA margin fell 18.8 to 16.4.

## 10. Qualifiers (R129-R141, 13)
R129, R130 units; R131 LTM; R132 two revenue measures (operating vs total); R133 PAT explanation "lower other income" (only profit driver named); R134 UNAUDITED; R135 signature; R136 Encl; R137-R140 safe-harbor Note; R141 records the A1 page-3 YoY column offset (text layer shifted YoY one row down; image governs; rows corrected).
Flags: R134 UNAUDITED_SOURCE.

## 11. Missing from structured
None found. Fulltext grep for Note:/asterisk/numbered patterns found only line 140, captured as R137.

## 12. ID accountability
R001-R141 all referenced above (R001-R012, R013-R067, R068-R079, R080-R092, R093-R115, R116-R128, R129-R141). orphan_ids: []
