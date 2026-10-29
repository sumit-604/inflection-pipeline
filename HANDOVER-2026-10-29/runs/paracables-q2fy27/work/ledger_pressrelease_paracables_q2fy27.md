# A2 LEDGER: PARACABLES Q2 FY27 press release (Reg 30), 3 pages
Source: extracted/paracables-pressrelease-q2fy27-structured.md (IDs only; values live there)
ids_in_structured: 157 | ids_referenced_in_ledger: 157 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: ids_total          grep_count: 157  sweep_count: 157  match: yes
category: NUMBER             grep_count: 103  sweep_count: 103  match: yes (header 103)
category: ENTITY             grep_count: 20   sweep_count: 20   match: yes
category: FORWARD            grep_count: 7    sweep_count: 7    match: yes
category: DATE               grep_count: 15   sweep_count: 15   match: yes
category: QUALIFIER          grep_count: 12   sweep_count: 12   match: yes
category: notes (numbered)   grep_count: 0    sweep_count: 0    match: yes (no numbered notes; footnote-type items are QUALIFIER rows)
category: line_items         grep_count: 9 table rows + 4 tiles   sweep_count: 9 + 4  match: yes
category: agenda_items       grep_count: 0    sweep_count: 0    match: yes (not a board outcome letter)
category: auditor_paras      grep_count: 0    sweep_count: 0    match: yes (results unaudited, R146)
category: slides             grep_count: 3    sweep_count: 3    match: yes
category: zero_standing      grep_count: 0    sweep_count: 0    match: yes
gate_a2: pass
=== END COUNT TEST ===

## 1. SLIDES / PAGES (3)
| ROW_ID | category | flags | note |
| R001-R005, R104-R110, R131-R134, R146-R147 | page 1 cover letter to exchanges, text | OCR_UNVERIFIED (R147) | letter dated 26.10.2026, sig 20:42:52 (R133) |
| R006-R016, R017-R097, R111-R113, R124-R129, R135-R142, R148-R154 | page 2 press release: KPI tiles + standalone snapshot table + CEO quote | CORRECTED_FROM_IMAGE (R041-R048, R057-R064) | table is STANDALONE (R148) |
| R089-R103, R114-R123, R130, R143-R145, R155-R157 | page 3 order book, mix chart, company profile, IR contacts, safe harbour | CORRECTED_FROM_IMAGE (R089, R090, R092-R097) | |

## 2. LINE ITEMS (financial tables)
Tiles (page 2, text/tile):
| R006-R009 | tile values Rev/OpProfit/EBITDA/PAT | RESTATED | = table Q2 FY27 R017, R033, R049, R065 |
| R010-R013 | tile YoY | RESTATED | = R021, R037, R053, R069 |
| R014-R016 | tile margins | RESTATED | = R041, R057, R073 |
Snapshot table rows (Q2 FY27, Q1 FY27, QoQ, Q2 FY26, YoY, H1 FY27, H1 FY26, YoY H1):
| R017-R024 | Revenue from Operations | | |
| R025-R032 | Total Income | | |
| R033-R040 | Operating Profit excl OI | | YoY 616.5% on 5.7 base, base effect |
| R041-R048 | Operating Margin excl OI | CORRECTED_FROM_IMAGE | bps changes |
| R049-R056 | EBITDA incl OI | | |
| R057-R064 | EBITDA Margin incl OI | CORRECTED_FROM_IMAGE | |
| R065-R072 | PAT | | |
| R073-R080 | PAT Margin | | R078 printed "4%" |
| R081-R088 | EPS Rs | | |
Absent line items (not in A1): interest, depreciation, tax, other income value, segment profit, balance sheet, cash flow. Not on the release; no MISSING row.

## 3. NOTES / FOOTNOTES / QUALIFIERS
| R146 | unaudited basis | | |
| R147 | company email | OCR_UNVERIFIED | |
| R148 | standalone basis of snapshot | | consolidated not shown |
| R149-R152 | metric definitions excl/incl OI | | tile and table restated |
| R153 | units Rs Cr, EPS Rs | | |
| R154 | margin change in bps | | |
| R155 | order book "approximately" | | FOOTNOTE_UNRESOLVED: executed/unexecuted basis not stated |
| R156 | safe harbour (single row) | | |
| R157 | export share basis "of revenue" | RESTATED | with R091, R093, R099 (28.2%); R098 71.8% domestic |

## 4. ENTITIES (20)
| R104-R123 | addressees, regulation, company, signatory, quoted exec, facilities (R114-R115), IR agency/contacts (R116-R118, R122), products (R119), sectors (R120), segments (R121), disclaimer (R123) | no ENTITY_CHANGE (no consolidation list, no prior ledger) | |
No subsidiary list on this doc; consolidation entities N/A.

## 5. FORWARD-LOOKING (7)
| R124-R130 | management outlook and priorities, order book visibility | | R127 "restoring operating profitability"; R130 visibility claim with no execution timeline |
MGMT_ABSENCE: n/a (no call). No numeric guidance rows.

## 6. DATES (15)
| R131-R145 | letter, period, signature, dateline, column headings, order book as-of | | R133 signature 20:42 on 26 Oct; board meeting times not on doc |

## 7. SLIDE NUMBERS (NUMBER rows, 103)
R001-R103 as in sections 1-2 plus: R001-R005 identifiers (page 1), R089-R099 order book/export/mix (page 3, RESTATED among R090/R091/R093/R099, R092-R097 sum to 100.0), R100-R103 profile figures.
DROPPED_SLIDE: not assessable (no prior ledger).

## ID ACCOUNTABILITY
R001-R157 all referenced above (ranges contiguous across sections 1-7). orphan_ids: []

```yaml
stage: A2-enumerator
company: "PARACABLES"
quarter: "Q2 FY27"
doctype: "pressrelease"
model: claude-sonnet-5-5
status: complete
ledger_path: "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/qr-paracables-q2fy27-a220cd/runs/paracables-q2fy27/work/ledger_pressrelease_paracables_q2fy27.md"
counts:
  notes: 0
  line_items: 13
  zero_standing: 0
  agenda_items: 0
  auditor_paras: 0
  entities: 20
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 3
  slide_numbers: 103
flags_raised: [RESTATED, CORRECTED_FROM_IMAGE, OCR_UNVERIFIED, FOOTNOTE_UNRESOLVED]
ids_in_structured: 157
ids_referenced: 157
orphan_ids: []
missing_from_structured: []
gate_a2: pass
mismatch_note: ""
analyst_note: "Press release only, standalone snapshot (R148); consolidated figures not in this doc. No zero standing rows. 24 rows carry CORRECTED_FROM_IMAGE (margins R041-R048, R057-R064, order book/export/mix R089-R090, R092-R097); A3 should verify these against the image. Order book R089/R155 basis (executed vs unexecuted) unstated. Operating profit YoY 616.5% rests on a 5.7 Cr base. No prior ledger, so ENTITY_CHANGE and DROPPED_SLIDE not assessable."
```
