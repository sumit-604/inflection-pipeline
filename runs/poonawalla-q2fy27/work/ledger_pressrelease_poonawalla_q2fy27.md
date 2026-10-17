# A2 LEDGER: Poonawalla Fincorp press release Q2FY27 (doctype presentation, 3 pages)
ids_in_structured: 96 | ids_referenced_in_ledger: 96 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: notes/footnotes        grep_count: 0   sweep_count: 0   match: yes (no numbered notes, asterisks or Note: lines in fulltext; A1 header agrees)
category: slides(pages)          grep_count: 3   sweep_count: 3   match: yes (p1 18 rows, p2 59, p3 19 = 96)
category: slide_numbers (NUMBER) grep_count: 51  sweep_count: 51  match: yes
category: entities               grep_count: 13  sweep_count: 13  match: yes
category: forward                grep_count: 8   sweep_count: 8   match: yes
category: dates                  grep_count: 13  sweep_count: 13  match: yes
category: qualifiers             grep_count: 11  sweep_count: 11  match: yes
category: zero_standing          grep_count: 0   sweep_count: 0   match: yes
gate_a2: pass
=== END COUNT TEST ===

## 1. Slides (pages)
| Page | Title / type | IDs |
| 1 | Reg 30 cover letter (text) | R001-R008, R052-R056, R073-R075, R086-R087 |
| 2 | Press release body, results (text, no tables) | R009-R048, R057, R065-R066, R076-R083, R088-R095 |
| 3 | CEO quote and company boilerplate (text) | R049-R051, R058-R064, R067-R072, R084-R085, R096 |
Prior deck: ND, so no DROPPED_SLIDE test possible.

## 2. Numbers (all NUMBER rows; page/line via A1 ID)
| ROW_ID | category | flags | note |
| R001-R008 | number/admin (cover) | none | codes, pincodes, dates; low materiality |
| R009, R012, R018, R050 | number/AUM 74,008 | RESTATED | four mentions, consistent |
| R010, R011, R019, R020 | number/PAT | RESTATED (R011=R019) | Q2 375 vs Q1 308; R010 21.8% QoQ |
| R013, R024, R025, R026 | number/RoA | RESTATED (R013=R024) | 2.18 / 1.98 / 1.81 three-quarter series |
| R014, R027, R028, R015 | number/credit cost | RESTATED (R014=R027) | 2.19 vs 2.40; 21 bps |
| R016, R034, R017, R033 | number/NII | RESTATED | lead para omits inc.-fees qualifier, see R095 |
| R021, R022, R023 | number/NIM | none | 9.26 vs 9.10, 16 bps |
| R029-R032 | number/asset quality | none | GNPA, NNPA |
| R035, R036 | number/PPoP | none | |
| R037-R039 | number/mix, Stage 1 | none | |
| R040-R043 | number/capital, liquidity | none | R042 is regulatory min |
| R044, R045 | number/cost of borrowing | none | |
| R046-R048 | number/AI projects | none | 42 new, 143 total, 84 implemented |
| R049, R051 | number/company facts | none | headcount 7,313 |

## 3. Entities
R052-R064 (13 rows): all single rows, no consolidation list. Flags: none; ENTITY_CHANGE not testable (no prior). R062 lists 13 product lines. R059 promoter group.

## 4. Forward-looking statements
R065-R072 (8 rows). R067-R072 are CEO claims, narrative only, no numeric guidance. R066 growth headroom claim.

## 5. Dates
R073-R085 (13 rows). R075 signature timestamp 2026.10.09 16:28:49 +05:30; board meeting times not stated in document, so no signature-vs-meeting test. Flag: BOARD_TIMES_ABSENT.

## 6. Qualifiers / fine print
R086-R096 (11 rows). R087/R088 unaudited. R095 flags FOOTNOTE-style qualifier omission in lead paragraph (NII incl. fees, cf. R091). A1 states no footnotes or disclaimers exist: FOOTNOTE_UNRESOLVED none.

## 7. ZERO_STANDING
None. No tables and no zero/nil/dash items.

## 8. MISSING_FROM_STRUCTURED
None found. Absences noted for A3 (not rows): no guidance numbers, no segment or AUM mix table, no borrowing mix, no disbursement figure, no ROE/EPS.
