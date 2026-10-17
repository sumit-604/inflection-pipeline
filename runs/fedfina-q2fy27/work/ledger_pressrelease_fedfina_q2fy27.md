=== A2 COUNT TEST ===
category: notes (footnotes/qualifiers, no numbered notes)  grep_count: 2   sweep_count: 2   match: yes   (R245 NAPS footnote; R243 rounding note; disclaimer R247 counted under qualifiers)
category: line_items (table rows, p2-p3)  grep_count: 25   sweep_count: 25   match: yes   (15 P&L/BS rows p2, 2 business rows p2, 6 ratio rows p3, 2 franchise rows p3; 8 values each = 200 NUMBER rows R001-R200)
category: zero_standing  grep_count: 0   sweep_count: 0   match: yes   (A1 states none)
category: agenda_items  grep_count: 0   sweep_count: 0   match: yes   (not a board outcome letter; cover letter is Reg 30 intimation)
category: auditor_paras  grep_count: 0   sweep_count: 0   match: yes
category: entities  grep_count: 14   sweep_count: 14   match: yes   (R215-R228)
category: slides (pages)  grep_count: 3   sweep_count: 3   match: yes
category: slide_numbers (NUMBER rows)  grep_count: 214   sweep_count: 214   match: yes   (200 table + 14 narrative/ID)
category: forward  grep_count: 3   sweep_count: 3   match: yes
category: dates  grep_count: 11   sweep_count: 11   match: yes
category: qualifiers  grep_count: 5   sweep_count: 5   match: yes
gate_a2: pass
=== END COUNT TEST ===

ids_in_structured: 247 | ids_referenced_in_ledger: 247 | orphan_ids: [] | match: yes

## 1. Pages (slides)
PAGE | content type | IDs
1 | text (Reg 30 cover letter) | R212-R220,R227(part),R229,R232-R234,R246
2 | table + text (P&L, balance, business) | R001-R136,R201-R203,R221-R223,R236-R238,R243
3 | table + text (ratios, franchise, About, disclaimer) | R137-R200,R204-R211,R224-R226,R228,R230-R231,R239-R242,R244-R245,R247

## 2. Line items (ROW_ID range | category | flags | note)
R001-R008 | line_item Interest Income (Q2FY26,Q1FY27,Q2FY27,QoQ,YoY,H1FY26,H1FY27,H1YoY) | line 80 | -
R009-R016 | line_item Interest Expenses (Q2FY26,Q1FY27,Q2FY27,QoQ,YoY,H1FY26,H1FY27,H1YoY) | line 81 | -
R017-R024 | line_item Net Interest Income (Core) (Q2FY26,Q1FY27,Q2FY27,QoQ,YoY,H1FY26,H1FY27,H1YoY) | line 82 | -
R025-R032 | line_item Net Gain on Direct Assignment (Q2FY26,Q1FY27,Q2FY27,QoQ,YoY,H1FY26,H1FY27,H1YoY) | line 83 | -
R033-R040 | line_item Net Interest Income (Q2FY26,Q1FY27,Q2FY27,QoQ,YoY,H1FY26,H1FY27,H1YoY) | line 84 | -
R041-R048 | line_item Other Income (Q2FY26,Q1FY27,Q2FY27,QoQ,YoY,H1FY26,H1FY27,H1YoY) | line 85 | -
R049-R056 | line_item Net Total Income (Q2FY26,Q1FY27,Q2FY27,QoQ,YoY,H1FY26,H1FY27,H1YoY) | line 86 | -
R057-R064 | line_item Operating Expenses (Q2FY26,Q1FY27,Q2FY27,QoQ,YoY,H1FY26,H1FY27,H1YoY) | line 87 | -
R065-R072 | line_item Operating Profit (Q2FY26,Q1FY27,Q2FY27,QoQ,YoY,H1FY26,H1FY27,H1YoY) | line 88 | -
R073-R080 | line_item Credit Cost (Q2FY26,Q1FY27,Q2FY27,QoQ,YoY,H1FY26,H1FY27,H1YoY) | line 89 | -
R081-R088 | line_item Profit Before tax (Q2FY26,Q1FY27,Q2FY27,QoQ,YoY,H1FY26,H1FY27,H1YoY) | line 90 | -
R089-R096 | line_item Tax Expenses (Q2FY26,Q1FY27,Q2FY27,QoQ,YoY,H1FY26,H1FY27,H1YoY) | line 91 | -
R097-R104 | line_item Profit After Tax (Q2FY26,Q1FY27,Q2FY27,QoQ,YoY,H1FY26,H1FY27,H1YoY) | line 92 | -
R105-R112 | line_item Shareholder's Fund (Q2FY26,Q1FY27,Q2FY27,QoQ,YoY,H1FY26,H1FY27,H1YoY) | line 93 | -
R113-R120 | line_item Book Value Per Share (Q2FY26,Q1FY27,Q2FY27,QoQ,YoY,H1FY26,H1FY27,H1YoY) | line 94 | -
R121-R128 | line_item Asset Under Management (Q2FY26,Q1FY27,Q2FY27,QoQ,YoY,H1FY26,H1FY27,H1YoY) | line 102 | -
R129-R136 | line_item Disbursements (Q2FY26,Q1FY27,Q2FY27,QoQ,YoY,H1FY26,H1FY27,H1YoY) | line 103 | -
R137-R144 | line_item Cost to Income (Q2FY26,Q1FY27,Q2FY27,QoQ,YoY,H1FY26,H1FY27,H1YoY) | line 123 | -
R145-R152 | line_item Return on Average Assets (Q2FY26,Q1FY27,Q2FY27,QoQ,YoY,H1FY26,H1FY27,H1YoY) | line 124 | -
R153-R160 | line_item Return on Average Equity (Q2FY26,Q1FY27,Q2FY27,QoQ,YoY,H1FY26,H1FY27,H1YoY) | line 125 | -
R161-R168 | line_item Gross NPA (Q2FY26,Q1FY27,Q2FY27,QoQ,YoY,H1FY26,H1FY27,H1YoY) | line 126 | -
R169-R176 | line_item Net NPA (Q2FY26,Q1FY27,Q2FY27,QoQ,YoY,H1FY26,H1FY27,H1YoY) | line 127 | -
R177-R184 | line_item CRAR (Q2FY26,Q1FY27,Q2FY27,QoQ,YoY,H1FY26,H1FY27,H1YoY) | line 128 | -
R185-R192 | line_item Branches (Q2FY26,Q1FY27,Q2FY27,QoQ,YoY,H1FY26,H1FY27,H1YoY) | line 135 | -
R193-R200 | line_item Employees* (Q2FY26,Q1FY27,Q2FY27,QoQ,YoY,H1FY26,H1FY27,H1YoY) | line 136 | -

Cross-refs: RESTATED R201=R099 PAT; R202=R147 ROA; R203=R155 ROE; R204 credit cost 0.6% narrative (no table counterpart as % ; compare R075 27.1 Cr); R207=R163 and R208=R171 (Gross/Net Stage III restate GNPA/NNPA); R205=R164; R206=R172; R210=R187 (831 branches); R209=R211 (18 states); R119/R118 = R115/R113 and R126-R128, R134-R136, R190-R192, R198-R200 are point-in-time H1 duplicates of Q2 values (flag RESTATED).
Materiality: R026/R027/R031 Net Gain on Direct Assignment turned negative (loss) in Q1FY27, Q2FY27, H1FY27 (R028/R029/R032 growth percentages not meaningful); R164 Gross NPA +27bps QoQ and R172 Net NPA +22bps QoQ; R132 disbursements down 1.2% QoQ; R076 credit cost down 20.5% QoQ yet R204 narrative 0.6%; R045/R048 Other Income YoY decline; R140 cost to income improved only 36bps QoQ.

## 3. Narrative/ID numbers (ROW_ID | category | flags)
R201 | number (non-table) | RESTATED where noted above | -
R202 | number (non-table) | RESTATED where noted above | -
R203 | number (non-table) | RESTATED where noted above | -
R204 | number (non-table) | RESTATED where noted above | -
R205 | number (non-table) | RESTATED where noted above | -
R206 | number (non-table) | RESTATED where noted above | -
R207 | number (non-table) | RESTATED where noted above | -
R208 | number (non-table) | RESTATED where noted above | -
R209 | number (non-table) | RESTATED where noted above | -
R210 | number (non-table) | RESTATED where noted above | -
R211 | number (non-table) | RESTATED where noted above | -
R212 | number (non-table) | RESTATED where noted above | -
R213 | number (non-table) | RESTATED where noted above | -
R214 | number (non-table) | RESTATED where noted above | -

## 4. Zero standing
none (A1: No ZERO_STANDING values). No nil/dash rows seen; R027 negative not zero.

## 5. Entities (R215-R228)
R215 | entity | - | -
R216 | entity | - | -
R217 | entity | - | -
R218 | entity | - | -
R219 | entity | - | -
R220 | entity | - | -
R221 | entity | - | -
R222 | entity | - | -
R223 | entity | - | -
R224 | entity | - | -
R225 | entity | - | -
R226 | entity | - | -
R227 | entity | - | ENTITY_SUMMARY group row
R228 | entity | - | ENTITY_SUMMARY group row
ENTITY_CHANGE: none flaggable (no prior ledger, ND). No consolidation list in this document.

## 6. Forward statements
R229 | forward | - | upload intent
R230 | forward | - | generic caveat, no guidance
R231 | forward | - | no-update clause
No quantitative guidance anywhere in the document.

## 7. Dates
R232 | date | - | -
R233 | date | - | -
R234 | date | - | -
R235 | date | - | -
R236 | date | - | -
R237 | date | - | -
R238 | date | - | -
R239 | date | - | -
R240 | date | - | -
R241 | date | - | -
R242 | date | - | -
DROPPED_SLIDE: not assessable (no prior ledger). Signature timestamp R234 12:28:36 IST on 2026-10-15; no board-meeting time in document to compare.

## 8. Qualifiers / footnotes
R243 | rounding note | p2 tables
R244 | asterisk marker on Employees | links R245
R245 | footnote NAPS exclusion | FOOTNOTE resolved (R244->R245)
R246 | signature qualifier
R247 | disclaimer label | links R228,R230,R231

## 9. MISSING_FROM_STRUCTURED
none

```yaml
stage: A2-enumerator
company: "FEDFINA"
quarter: "q2fy27"
doctype: "presentation"
model: claude-sonnet-5-5
status: complete
ledger_path: "C:\Users\SUMIT SHARMA\repos\inflection-pipeline\.claude\worktrees\q2fy27\runs\fedfina-q2fy27\work\ledger_pressrelease_fedfina_q2fy27.md"
counts:
  notes: 2
  line_items: 25
  zero_standing: 0
  agenda_items: 0
  auditor_paras: 0
  entities: 14
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 3
  slide_numbers: 214
flags_raised: [RESTATED]
ids_in_structured: 247
ids_referenced: 247
orphan_ids: []
missing_from_structured: []
gate_a2: pass
mismatch_note: ""
analyst_note: "Press release, 3 pages, no guidance. 200 of 214 numbers are 25 table rows x 8 values; H1 columns for AUM, disbursements, BVPS, branches, employees duplicate Q2 point values. Watch items for A3/A4: Net Gain on Direct Assignment negative (R026,R027,R031); Gross NPA +27bps and Net NPA +22bps QoQ (R164,R172); disbursements -1.2% QoQ (R132); credit cost Rs 27.1 Cr down 20.5% QoQ while narrative cites 0.6% (R204, basis not stated); Other Income down YoY. No ZERO_STANDING rows, no prior ledger so ENTITY_CHANGE and DROPPED_SLIDE not assessable."
```