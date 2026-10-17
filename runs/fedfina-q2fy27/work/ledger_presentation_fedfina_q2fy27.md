# A2 LEDGER: FEDFINA Q2 FY27 investor presentation

ids_in_structured: 1102 | ids_referenced_in_ledger: 1102 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: slides             grep_count: 42 (fulltext [page N] markers)   sweep_count: 42 (37 with rows + 5 no-row text slides: p4,p9,p20,p32,p37)   match: yes
category: slide_numbers      grep_count: 971 (header 971)   sweep_count: 971   match: yes
category: entities           grep_count: 57 (header 57)   sweep_count: 57   match: yes
category: forward_statements grep_count: 20 (header 20)   sweep_count: 20   match: yes
category: dates              grep_count: 17 (header 17)   sweep_count: 17   match: yes
category: footnotes          grep_count: 37 (header 37)   sweep_count: 37   match: yes
category: total_ids          grep_count: 1102 (header total 1102)   sweep_count: 1102   match: yes
category: zero_standing      grep_count: 1 (tag [ZERO_STANDING] in structured)   sweep_count: 1 (R1024)   match: yes
gate_a2: pass
=== END COUNT TEST ===

Notes: doctype is presentation; notes, agenda, auditor, turns and questions categories do not apply. Prior ledger ND, so DROPPED_SLIDE is not assessable. Rows are referenced by ID; verbatim values stay in the structured file.

## 1. SLIDE LEDGER (every slide; IDs grouped per slide)

| slide | title | content type | ID range | rows | NUMBER | other | A2 flags / note |
|---|---|---|---|---|---|---|---|
| 1 | Cover letter to exchanges (LODR 46(2)) | text | R001-R018 | 18 | 5 | 13 | signature timestamp R011 |
| 2 | Title slide | text | R019-R019 | 1 | 0 | 1 |  |
| 3 | Safe Harbor | text | R020-R022 | 3 | 0 | 3 |  |
| 4 | Table of Contents | text | none | 0 | 0 | 0 | NO_STRUCTURED_ROWS: text-only divider/TOC slide; no orphan |
| 5 | Executive Summary Q2 FY27 | text+numbers | R023-R046 | 24 | 23 | 1 |  |
| 6 | Q2 FY27 Result Summary | table | R047-R096 | 50 | 45 | 5 |  |
| 7 | Financials: Historical Performance | chart | R097-R179 | 83 | 81 | 2 |  |
| 8 | RoA & RoE Trajectory | chart | R180-R195 | 16 | 14 | 2 | SERIES_ATTRIBUTION_UNRESOLVED (some rows) |
| 9 | Section divider | text | none | 0 | 0 | 0 | NO_STRUCTURED_ROWS: text-only divider/TOC slide; no orphan |
| 10 | About Fedfina / Product Suite | text | R196-R204 | 9 | 3 | 6 |  |
| 11 | Board of Directors | photo+text | R205-R214 | 10 | 0 | 10 |  |
| 12 | Management Team | photo+text | R215-R221 | 7 | 0 | 7 |  |
| 13 | Shareholding Pattern | table+chart | R222-R249 | 28 | 17 | 11 |  |
| 14 | Our Growth Journey | chart/timeline | R250-R285 | 36 | 31 | 5 |  |
| 15 | Vision & Values | text | R286-R287 | 2 | 0 | 2 |  |
| 16 | Market (household credit/retail credit) | chart | R288-R311 | 24 | 16 | 8 | SERIES_ATTRIBUTION_UNRESOLVED (some rows) |
| 17 | Our Product Suite | table | R312-R332 | 21 | 18 | 3 |  |
| 18 | Our Customers | table | R333-R339 | 7 | 6 | 1 |  |
| 19 | Our Footprints (branch network) | chart+map | R340-R385 | 46 | 45 | 1 | SERIES_ATTRIBUTION_UNRESOLVED (some rows) |
| 20 | Section divider | text | none | 0 | 0 | 0 | NO_STRUCTURED_ROWS: text-only divider/TOC slide; no orphan |
| 21 | Disbursements & AUM | chart | R386-R449 | 64 | 62 | 2 |  |
| 22 | Disbursements | chart | R450-R480 | 31 | 30 | 1 |  |
| 23 | Gold Loan Key Metrics | chart | R481-R504 | 24 | 21 | 3 | SERIES_ATTRIBUTION_UNRESOLVED (some rows) |
| 24 | Geographical AUM Mix | chart | R505-R551 | 47 | 44 | 3 |  |
| 25 | Yields, CoB and Spreads | chart | R552-R584 | 33 | 30 | 3 | SERIES_ATTRIBUTION_UNRESOLVED (some rows) |
| 26 | Funding / Portfolio Profile / Quality Indicators | chart+table | R585-R625 | 41 | 35 | 6 | SERIES_ATTRIBUTION_UNRESOLVED (some rows) |
| 27 | Off-book | chart | R626-R681 | 56 | 54 | 2 |  |
| 28 | Quality of the Book | chart | R682-R700 | 19 | 14 | 5 | SERIES_ATTRIBUTION_UNRESOLVED (some rows) |
| 29 | Portfolio Quality Indicators (1/2) | chart | R701-R722 | 22 | 21 | 1 |  |
| 30 | Portfolio Quality Indicators (2/2) | chart | R723-R754 | 32 | 30 | 2 |  |
| 31 | Expected Credit Loss | table | R755-R800 | 46 | 42 | 4 |  |
| 32 | Section divider | text | none | 0 | 0 | 0 | NO_STRUCTURED_ROWS: text-only divider/TOC slide; no orphan |
| 33 | Financials (summary table) | table | R801-R891 | 91 | 90 | 1 |  |
| 34 | Balance Sheet | table | R892-R945 | 54 | 54 | 0 |  |
| 35 | Profit & Loss Statement | table | R946-R1009 | 64 | 64 | 0 |  |
| 36 | RoA Tree | table(tree) | R1010-R1078 | 69 | 68 | 1 |  |
| 37 | Section divider | text | none | 0 | 0 | 0 | NO_STRUCTURED_ROWS: text-only divider/TOC slide; no orphan |
| 38 | Technology Landscape | text | R1079-R1084 | 6 | 1 | 5 |  |
| 39 | Digital Landscape | text | R1085-R1089 | 5 | 3 | 2 |  |
| 40 | ESG | text | R1090-R1097 | 8 | 3 | 5 |  |
| 41 | Making a Change (CSR) | text+photo | R1098-R1100 | 3 | 0 | 3 |  |
| 42 | Thank You / contact | text | R1101-R1102 | 2 | 1 | 1 |  |

## 2. SLIDE NUMBERS (all 971 NUMBER rows are covered by the slide ID ranges above)

| ROW_ID | category | A2 flags | cross-ref / note |
|---|---|---|---|
| R025, R048 | headline number | RESTATED | p5 exec summary restated on p6 result summary |
| R027, R051 | headline number | RESTATED | p5 exec summary restated on p6 result summary |
| R041, R054 | headline number | RESTATED | p5 exec summary restated on p6 result summary |
| R024, R049 | headline number | RESTATED | p5 exec summary restated on p6 result summary |
| R026, R052 | headline number | RESTATED | p5 exec summary restated on p6 result summary |
| R042, R193 | RoA Q2 FY27 | RESTATED | slide 5 and slide 8 |
| R043, R186 | RoE Q2 FY27 | RESTATED | slide 5 and slide 8 |
| R1024 | line item (RoA tree) | ZERO_STANDING | Net Gain on DA / Average total Assets 0.0% Q2 FY27 (slide 36); template line stands, DA gain line exists |
| R180-R193 | RoE/RoA chart labels | SERIES_BY_POSITION | slide 8 |
| R289-R300 | market chart labels | SERIES_BY_POSITION | slide 16 |
| R340-R380 | branch/AUM mix labels | SERIES_NOT_RESOLVABLE | slide 19; region assignment not recoverable |
| R552-R581 | yields/spreads/CoB | SERIES_BY_POSITION | slide 25 |
| R587-R593 | funding pie | SERIES_NOT_RESOLVABLE | slide 26 |
| R687-R690 | CIBIL mix | SERIES_NOT_RESOLVABLE | slide 28 |

Rows A1 marked by-position or not-resolvable: 105


## 3. FOOTNOTES, QUALIFIERS AND FINE PRINT (37)

| ROW_ID | slide | line | A2 flags | note |
|---|---|---|---|---|
| R014 | 1 | 55 |  | enclosure note |
| R018 | 1 | 62 |  | classification label |
| R022 | 3 | 89 |  | map qualifier |
| R063 | 6 | 149 |  | markers paired to lines 159-160 |
| R094 | 6 | 159 |  | footnote 1 Borrowings definition |
| R095 | 6 | 159 |  | footnote 3 Employees |
| R096 | 6 | 160 |  | footnote 2 Credit cost |
| R097 | 7 | 164 |  | table unit |
| R302 | 16 | 431 |  | P suffix marker |
| R309 | 16 | 452 |  | footnote 1 |
| R310 | 16 | 452 |  | footnote 2 |
| R311 | 16 | 452 |  | footnote 3 |
| R331 | 17 | 485 |  | footnote definition |
| R332 | 17 | 485 |  | footnote |
| R368 | 19 | 534 |  | map colour thresholds |
| R503 | 23 | 691 | FOOTNOTE_QUALIFIES_HEADLINE | footnote on 16.9 AUM per branch |
| R504 | 23 | 691 |  | definition |
| R550 | 24 | 734 |  | rounding note |
| R551 | 24 | 734 |  | definition |
| R583 | 25 | 768 |  | averaging basis |
| R584 | 25 | 768 |  | annualisation |
| R586 | 26 | 776 |  | ALM basis |
| R624 | 26 | 815 | FOOTNOTE_QUALIFIES_HEADLINE | footnote * |
| R625 | 26 | 815 |  | footnote # |
| R662 | 27 | 834 |  | footnote ^ on Total |
| R681 | 27 | 854 | FOOTNOTE_QUALIFIES_HEADLINE | footnote * Q1 FY26, Q2 FY26 |
| R695 | 28 | 880 |  | definition |
| R698 | 28 | 889 |  | footnote 1 |
| R699 | 28 | 889 |  | footnote 2 |
| R700 | 28 | 889 |  | rounding note |
| R754 | 30 | 952 |  | definition |
| R797 | 31 | 979 | FOOTNOTE_QUALIFIES_HEADLINE | footnote * |
| R798 | 31 | 980 | FOOTNOTE_QUALIFIES_HEADLINE | footnote * |
| R799 | 31 | 981 |  | footnote ^ |
| R800 | 31 | 982 |  | footnote ^ |
| R891 | 33 | 1021 | FOOTNOTE_QUALIFIES_HEADLINE | footnote * Net Total Income |
| R1078 | 36 | 1105 |  | FY 26 column basis |

## 4. FORWARD-LOOKING STATEMENTS (20)

| ROW_ID | slide | line | A2 flags | note |
|---|---|---|---|---|
| R021 | 3 | 86 |  | safe harbor no-update undertaking |
| R195 | 8 | 221 |  | slide tagline RoA RoE trend |
| R288 | 16 | 417 |  | chart title and projected value |
| R307 | 16 | 450 |  | slide tagline |
| R449 | 21 | 613 |  | slide tagline |
| R480 | 22 | 654 |  | slide tagline |
| R502 | 23 | 689 |  | slide tagline |
| R549 | 24 | 732 |  | slide tagline |
| R582 | 25 | 767 |  | slide tagline |
| R623 | 26 | 813 |  | slide tagline |
| R697 | 28 | 887 |  | slide tagline |
| R722 | 29 | 921 |  | slide tagline |
| R753 | 30 | 950 |  | slide tagline |
| R1081 | 38 | 1135 |  | technology aspiration |
| R1084 | 38 | 1160 |  | slide tagline |
| R1089 | 39 | 1183 |  | slide tagline |
| R1091 | 40 | 1194 |  | KPI metrics under development |
| R1097 | 40 | 1224 |  | slide tagline |
| R1099 | 41 | 1231 |  | CSR initiative |
| R1100 | 41 | 1235 |  | CSR aim |

## 5. DATES (17)

| ROW_ID | slide | line | A2 flags | note |
|---|---|---|---|---|
| R001 | 1 | 18 |  | letter date |
| R006 | 1 | 30 |  | earlier letter intimating earnings call |
| R007 | 1 | 35 |  | results period |
| R011 | 1 | 49 |  | digital signature timestamp |
| R019 | 2 | 66 |  | deck period |
| R023 | 5 | 113 |  | executive summary period |
| R047 | 6 | 135 |  | result summary period |
| R098 | 7 | 166 |  | historical table periods |
| R194 | 8 | 216 |  | RoA RoE chart periods |
| R205 | 11 | 266 |  | board as-of date |
| R222 | 13 | 322 |  | shareholding date |
| R250 | 14 | 348 |  | growth journey phases |
| R301 | 16 | 431 |  | retail credit chart periods |
| R308 | 16 | 452 |  | BIS source date |
| R417 | 21 | 591 |  | chart periods |
| R585 | 26 | 774 |  | ALM as-of date |
| R1095 | 40 | 1211 |  | Stree Sakthi Gold Loan Schemes launch |

## 6. ENTITIES (57)

| ROW_ID | slide | line | A2 flags | note |
|---|---|---|---|---|
| R002 | 1 | 20 |  | addressee exchange |
| R003 | 1 | 20 |  | addressee exchange |
| R008 | 1 | 37 |  | regulation cited |
| R009 | 1 | 38 |  | company website |
| R010 | 1 | 45 |  | issuer |
| R012 | 1 | 51 |  | Company Secretary & Compliance Officer |
| R016 | 1 | 60 | GROUPED_SUMMARY | postal addresses |
| R020 | 3 | 72 | GROUPED_SUMMARY | decorative disclaimer |
| R196 | 10 | 241 |  | majority owner of Fedfina |
| R198 | 10 | 255 |  | rating agency AA+/Stable |
| R199 | 10 | 255 |  | rating agency AA+/Stable |
| R202 | 10 | 256 |  | rating agency AA+/Stable |
| R203 | 10 | 256 |  | rating agency AA+/Stable |
| R204 | 10 | 256 |  | products |
| R206 | 11 | 269 |  | director |
| R207 | 11 | 269 |  | director |
| R208 | 11 | 269 |  | director |
| R209 | 11 | 269 |  | director |
| R210 | 11 | 275 |  | director |
| R211 | 11 | 275 |  | director |
| R212 | 11 | 275 |  | director |
| R213 | 11 | 275 |  | director |
| R214 | 11 | 281 |  | management |
| R215 | 12 | 299 |  | management |
| R216 | 12 | 299 |  | management |
| R217 | 12 | 299 |  | management |
| R218 | 12 | 299 |  | management |
| R219 | 12 | 306 |  | management |
| R220 | 12 | 307 |  | management |
| R221 | 12 | 307 |  | management |
| R231 | 13 | 329 |  | shareholder |
| R233 | 13 | 330 |  | shareholder |
| R235 | 13 | 331 |  | shareholder |
| R237 | 13 | 332 |  | shareholder |
| R239 | 13 | 333 |  | shareholder |
| R241 | 13 | 335 |  | shareholder |
| R243 | 13 | 337 |  | shareholder |
| R245 | 13 | 338 |  | shareholder |
| R247 | 13 | 339 |  | shareholder |
| R249 | 13 | 340 |  | shareholder |
| R256 | 14 | 356 |  | upgraded to AA+/Stable |
| R258 | 14 | 358 |  | long-term rating assigned AA/Positive then AA+/Stable |
| R261 | 14 | 366 |  | upgraded to AA |
| R263 | 14 | 370 |  | joined as strategic partner |
| R286 | 15 | 398 |  | values group |
| R287 | 15 | 400 | GROUPED_SUMMARY | values glossary |
| R330 | 17 | 478 |  | underwriting method |
| R333 | 18 | 488 |  | illustrative customers |
| R622 | 26 | 807 |  | rating agencies |
| R1079 | 38 | 1122 |  | integrations |
| R1080 | 38 | 1133 |  | real time API integration |
| R1082 | 38 | 1138 |  | cloud and security |
| R1085 | 39 | 1164 |  | mobile apps |
| R1090 | 40 | 1193 |  | ESG governance |
| R1094 | 40 | 1210 |  | product scheme |
| R1098 | 41 | 1229 |  | CSR initiative |
| R1102 | 42 | 1246 | GROUPED_SUMMARY | address block |

## 7. MISSING_FROM_STRUCTURED

None found. All 42 fulltext pages covered; pages 4, 9, 20, 32, 37 hold only section-title text.

## ID ACCOUNTABILITY
ids_in_structured: 1102 | ids_referenced_in_ledger: 1102 | orphan_ids: [] | match: yes

```yaml
stage: A2-enumerator
company: "FEDFINA"
quarter: "q2fy27"
doctype: "presentation"
model: claude-sonnet-5-5
status: complete
ledger_path: "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/q2fy27/runs/fedfina-q2fy27/work/ledger_presentation_fedfina_q2fy27.md"
counts:
  slides: 42
  slide_numbers: 971
  line_items: 1
  zero_standing: 1
  entities: 57
  forward_statements: 20
  dates: 17
  footnotes: 37
flags_raised: [ZERO_STANDING, RESTATED, SERIES_BY_POSITION, SERIES_NOT_RESOLVABLE, NO_STRUCTURED_ROWS]
ids_in_structured: 1102
ids_referenced: 1102
orphan_ids: []
missing_from_structured: []
gate_a2: pass
mismatch_note: ""
analyst_note: "Presentation only; DROPPED_SLIDE not assessable (no prior ledger). Slides 4, 9, 20, 32, 37 are text dividers with no rows. One ZERO_STANDING row (R1024, DA gain over assets 0.0 percent on the RoA tree). Series attribution on slides 8, 16, 19, 25, 26, 28 rests on layout position; A3 should cross-check before relying on it, e.g. spread = yield minus CoB on slide 25."
```
