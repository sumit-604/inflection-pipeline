=== A2 COUNT TEST ===
category: slides(pages)      grep_count: 3    sweep_count: 3    match: yes
category: slide_numbers      grep_count: 103  sweep_count: 103  match: yes   (header NUMBER 103)
category: line_items         grep_count: 63 (7 rows x 9 cols, R019-R081)  sweep_count: 63  match: yes
category: zero_standing      grep_count: 0    sweep_count: 0    match: yes
category: entities           grep_count: 20   sweep_count: 20   match: yes
category: forward_stmts      grep_count: 9    sweep_count: 9    match: yes   (+2 MISSING_FROM_STRUCTURED below)
category: dates              grep_count: 18   sweep_count: 18   match: yes
category: qualifiers         grep_count: 20   sweep_count: 20   match: yes
category: notes (footnotes)  grep_count: 3 unnumbered footnote lines (R158-R161 text; 0 numbered)  sweep_count: 3  match: yes
category: agenda_items / auditor_paras / turns / questions: not applicable to a press release (0)
gate_a2: pass
=== END COUNT TEST ===
ids_in_structured: 170 | ids_referenced_in_ledger: 170 | orphan_ids: [] | match: yes
Pages: p1 = 14 rows (cover letter), p2 = 104 rows (press release + P&L table), p3 = 52 rows (CMD commentary). Slides = 3 pages.

## 1. SLIDES / PAGES
ROW ID | category | flags | note
page 1 (R001-R004, R104-R107, R123, R133-R135, R151, R169) | cover letter to BSE/NSE, text | none | CIN, scrip code, signature
page 2 (R005-R081, R108-R112, R136-R143, R152-R166, R170) | press release text + P&L summary table | LAYOUT_SHIFT on 6 cells | table plus footnotes
page 3 (R082-R103, R113-R122, R124-R132, R144-R150, R167-R168) | CMD commentary + About | none | text only, no table

## 2. NUMBERS (R001-R103; referenced by ID, verbatim in structured file)
ROW ID | category | flags | note
R001-R004 | identifiers (CIN, scrip, PIN, tel) | none | non-financial
R005-R018 | headline/summary numbers p2 | RESTATED | R006=R028=R085, R007=R030=R086, R008=R037=R087, R009=R039=R088, R010=R046=R089, R011=R055=R090, R012=R057=R091, R013=R064=R092, R015=R098. R016-R018 are H1 basis; R093-R095 are Q2 basis (see R163/R164)
R019-R027 | P&L line: Total Income (9 cols) | none |
R028-R036 | P&L line: Revenue from Operations | LAYOUT_SHIFT (R030) |
R037-R045 | P&L line: Operating EBITDA | LAYOUT_SHIFT (R039) |
R046-R054 | P&L line: Op EBITDA Margin | LAYOUT_SHIFT (R048) | bps cells in YoY/QoQ columns
R055-R063 | P&L line: PAT | LAYOUT_SHIFT (R057) |
R064-R072 | P&L line: PAT Margin | LAYOUT_SHIFT (R066) | denominator Total Income per R161
R073-R081 | P&L line: Diluted EPS (non-annualized) | LAYOUT_SHIFT (R075) |
R082-R084 | CMD H1 PAT vs FY26 PAT | RESTATED | R082=R060, R083=R063
R085-R092 | CMD restatement of Q2 headline numbers | RESTATED | see R005-R018 map
R093-R095 | AI Systems Q2 revenue, share, YoY | none | share 58.4% (Q2) vs 59.9% (H1, R018)
R096-R097 | HPC, Private Cloud Q2 revenue | none | segment split covers 3 of 5 offering lines in R120
R098 | order book | RESTATED | =R015
R099 | additional L1 position | none | additional to order book (R165)
R100 | capital raise 12,000 Mn | none | material event; no use of proceeds in this doc
R101 | active pipeline | none | linked to R126
R102-R103 | founding year, offices | none | R102 also DATE R150

## 3. LINE ITEMS (financial table, 7 lines)
ROW ID | category | flags | note
R019-R027 Total Income | line item | none |
R028-R036 Revenue from Operations | line item | none |
R037-R045 Operating EBITDA | line item | none |
R046-R054 Op EBITDA Margin | line item | none |
R055-R063 PAT | line item | none |
R064-R072 PAT Margin | line item | none |
R073-R081 Diluted EPS | line item | none |
ZERO_STANDING: none found (no nil or dash cells). Not printed in this doc: Other Income, Finance cost, Depreciation, PBT, Tax lines; no balance sheet, cash flow or segment P&L.

## 4. ENTITIES (R104-R123)
ROW ID | category | flags | note
R104-R105 | exchanges | none |
R106 | signatory CS | none | signature R135/R169
R107-R108 | registrant / issuer | none | no consolidation list in this doc; ENTITY_CHANGE not testable (no prior ledger)
R109-R112 | segment/industry/body | none |
R113 | CMD Sanjay Lodha | none | promoter quoted
R114-R116 | HPC, Private Cloud, L1 | none |
R117-R119 | NSM 2.0, Make in India, Neocloud/CSP | none | demand-side names
R120-R121 | offering lines, plant | none | HPS, Data Centre Servers, HCI not quantified
R122-R123 | contact, address block | none |

## 5. FORWARD STATEMENTS (R124-R132) plus added rows
ROW ID | category | flags | note
R124-R132 | forward / demand-outlook | none | pipeline 1,11,518 Mn (R126/R127); no quantified guidance, no dated target
M001 | forward/qualitative | MISSING_FROM_STRUCTURED | line 160: "a strengthened balance sheet following the recent capital raise and a robust order book" (CMD quote); links R100
M002 | forward/qualitative | MISSING_FROM_STRUCTURED | line 159: "sustained investment in innovation and a chip-agnostic design philosophy" (CMD quote)

## 6. CLAIM / HEADLINE ROWS added by sweep
M003 | headline claim | MISSING_FROM_STRUCTURED | line 63: "Netweb's H1 FY27 profits exceeds full-year FY26" (first clause of headline; R166 holds only the second clause)
M004 | superlative claim | MISSING_FROM_STRUCTURED | line 116: "another record quarter ... highest-ever quarterly Revenue from Operations and Profit After Tax" (CMD); no prior-quarter comparatives printed to test it

## 7. DATES (R133-R150)
ROW ID | category | flags | note
R133-R135 | letter date, period end, signature timestamp | none | signature 16:06:27 IST on 24.10.2026; board meeting start/end times NOT FOUND in this doc
R136-R138 | press release / board meeting / period | RESTATED | R136=R137=R133 date
R139-R146 | Q2 FY27, Net Debt/Order Book dates, periods | RESTATED | R140=R141=R146 (30-Sep-2026)
R147-R150 | listing July 2023, founding 1999 | RESTATED | R147=R149, R150=R102

## 8. FOOTNOTES / QUALIFIERS (R151-R170)
ROW ID | category | flags | note
R151-R152 | unaudited status | none | no auditor limited-review mention in this doc
R153-R157 | footnote markers on table rows | none | markers 1,2,* map to R158-R161
R158-R161 | footnotes (non-annualized; EBITDA def; margin def; PAT margin on Total Income) | none | all markers resolve; no FOOTNOTE_UNRESOLVED
R162 | unit label Millions | none |
R163-R165 | period/L1 qualifiers | none | H1 vs Q2 basis difference
R166-R170 | headline, raise, attribution, signature, Net Debt bracket | none | R170: bracket sign undefined

## 9. ID ACCOUNTABILITY
R001-R170 all referenced in sections 2-8 (ranges contiguous and complete; qualifiers R151-R170 and entities R104-R123 in sections 8 and 4). Orphans: none.
