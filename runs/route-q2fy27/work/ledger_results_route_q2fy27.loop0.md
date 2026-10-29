# A2 ENUMERATION LEDGER: Route Mobile Limited (ROUTE), Q2 FY27, RESULTS FILING
Source: A1 structured extraction route-results-q2fy27-structured.md (R001-R1129). Prior ledger: Q1 FY27 (older format), used for diffs only.
ids_in_structured: 1129 | ids_referenced_in_ledger: 1129 | orphan_ids: [] | match: yes

```
=== A2 COUNT TEST ===
category: notes          grep_count: 19   sweep_count: 23   match: yes (reconciled)
  (grep: 17 numbered "N)" notes [consol 1-9, standalone 1-8] + 2 "Note:" lines = 19;
   sweep adds 4 unnumbered sub-lettered notes: consol 3a, 7a, 7b, standalone 3a = 23)
category: line_items     grep_count: 244 (+12 table rows) sweep_count: 244 (+12) match: yes
  (distinct page+line keys on statement pages 7-10, 14-16 = 244; label-group sweep gave 246,
   the 2 extra groups are R1128-R1129 re-extraction cells that fill the existing hedge rows
   L357/L358, merged. Table rows added: IPO consol 5, IPO standalone 5, FX 1, subsidiary dividend 1.
   CIN row R048 excluded.)
category: zero_standing  grep_count: 42 cells  sweep_count: 42 cells (32 line rows)  match: yes
  (flag grep on structured: 40 ZERO_STANDING-ending rows + 2 re-extraction rows R1128-R1129 = 42;
   sweep by line: 23 statement lines + 4 consol IPO rows + 4 standalone IPO rows + 1 dividend row = 32)
category: agenda_items   grep_count: 5    sweep_count: 5    match: yes
category: auditor_paras  grep_count: 13   sweep_count: 14   match: yes (13 numbered: consol 8 + standalone 5; sweep adds consol para 6 continuation L211)
category: entities       grep_count: 33   sweep_count: 33   match: yes (+ blank Sr.33 row R965, flagged; A1 ENTITY table 77 rows incl. non-subsidiary entities)
category: signature_blocks grep_count: 6  sweep_count: 6    match: yes
category: annexures      grep_count: 2    sweep_count: 2    match: yes (Annexure 1 entity list, Annexure 2 Reg 30 disclosures)
category: turns / questions / mgmt_numbers / slides / slide_numbers: n/a for results filing
gate_a2: pass
=== END COUNT TEST ===
```

Flag key: ZERO_STANDING, ENTITY_CHANGE (auditor change; entity list itself unchanged 33 vs 33), RESTATED, NEW_ITEM_VS_Q1, FOOTNOTE_UNRESOLVED, MEETING_TIME. Claim text stays in the structured file at the row ID.


## 1. BOARD OUTCOME LETTER AGENDA (5 items) AND LETTER ITEMS

| ROW IDs | category | A2 flags | note |
|---|---|---|---|
| R001-R004, R1014 | agenda item 1 results / letter header | - | Reg 30/33/42 refs, scrip 543228; results unaudited |
| R005-R010, R989-R993, R1015-R1020, R1061-R1062 | agenda item 2 second interim dividend Rs4 (40%) | NEW_ITEM_VS_Q1 | Q1 declared FIRST interim Rs4 (record 29 Jul 2026); now SECOND interim, record date 02 Nov 2026; TDS deadline same day |
| R011-R012, R919, R1063 | agenda item 3 ESOP lapse (2,860 options, Plan 2021) | - | - |
| R013-R014, R920, R994-R995, R1021 | agenda item 4 rescission of 7 May 2026 IPO-proceeds variation | NEW_ITEM_VS_Q1 | Rs650m Mumbai office premises; ties to IPO tables |
| R015, R910-R911, R986-R988, R996, R1005-R1011, R1022, R1059, R1064, R1127 | agenda item 5 MOA alteration + Annexure 2 (Reg 30 disclosure) | NEW_ITEM_VS_Q1 | Object clause expansion (AI, GenAI, ML, digital identity, cloud, CPaaS); shareholder approval pending |
| R016-R017, R1024 | board meeting times | MEETING_TIME | 9:00 PM to 10:35 PM IST = 95 min; Q1 was 6:45-8:45 PM (120 min) |
| R921, R997, R1023 | insider trading window reopening 30 Oct 2026 | - | - |
| R912-R918, R923-R925, R1012-R1013, R1060 | letter addressees, exchanges, cc, results-unaudited qualifier, meeting date | - | - |

## 2. SIGNATURE BLOCKS (6)

| ROW IDs | category | A2 flags | note |
|---|---|---|---|
| R018, R922, R1025 | sig 1: Company Secretary (letter), ts 2026.10.27 23:49:25 | SIG_AFTER_MEETING | after 22:35 meeting end; expected |
| R044-R046, R931, R1036 | sig 2: MSKA consolidated report, UDIN 26100623CVWZCH6481, 27 Oct 2026 | - | - |
| R969 | sig 3: MD, consolidated statement header block (p7) | - | - |
| R594, R979, R1042, R1047-R1048 | sig 4: MD, Brussels, consolidated statement 27 Oct 2026 | - | - |
| R595-R596, R982, R1052 | sig 5: MSKA standalone report, UDIN 26100623OXJGBO9420, ts 23:18:16 | - | - |
| R909, R985, R1056, R1058 | sig 6: MD, standalone statement 27 Oct 2026 | - | - |

## 3. AUDITOR REPORT PARAGRAPHS (14)

| ROW IDs | category | A2 flags | note |
|---|---|---|---|
| R019-R023, R926-R927, R1026-R1027, R1065-R1066 | consol paras 1-5: scope, standards, review basis (5 numbered) | LIMITED_REVIEW | no audit opinion; unmodified conclusion |
| R024-R032, R928, R1028-R1029, R1067-R1068, R1070 | consol para 6: 24 subsidiaries reviewed by other auditors (Rs1,852.94 Cr assets) | RELIANCE_OTHER_AUDITORS | - |
| R033, R1069 | consol para 6 continuation: 11 overseas subs converted from local GAAP | CONTINUATION_PARA | - |
| R034-R042, R1071-R1072 | consol para 7: 7 subsidiaries not reviewed by auditors, management-furnished | UNREVIEWED_ENTITIES | Rs45.28 Cr assets; stated not material |
| R043, R929-R930, R1030-R1035, R1073-R1074 | consol para 8: predecessor auditor on prior periods/year | AUDITOR_CHANGE; ENTITY_CHANGE | MSKA now; prior report dates 23 Jul 2026, 3 Nov 2025, 7 May 2026. Q1 report was by Walker Chandiok (Q1 ledger) |
| R980, R1105-R1106 | standalone paras 1-4: scope, review basis, conclusion | LIMITED_REVIEW | - |
| R981, R1049-R1051, R1107 | standalone para 5: predecessor auditor on prior periods | AUDITOR_CHANGE; ENTITY_CHANGE | - |

## 4. ENTITIES AND ANNEXURE 1 (consolidation list 33 vs Q1 33: no add/remove/rename)

| ROW IDs | category | A2 flags | note |
|---|---|---|---|
| R916-R917 | statutory auditors, Audit Committee (letter) | - | - |
| R932-R964 | Annexure 1 named subsidiaries (33 names; Sr.18 carries two lines) | - | All 33 Q1 names present in Q2; no addition or removal vs Q1 ledger |
| R047, R965, R1075 | Annexure 1 Sr.33 blank in text layer; count 33 | FOOTNOTE_UNRESOLVED | Name absent; Q2 note 1 says 33 subsidiaries |
| R966-R968, R983 | statement headers, registered office, Proximus Global brand | - | - |
| R970-R971, R1084 | reportable segments India/Overseas | - | - |
| R972-R978, R984, R1043-R1046 | entities in notes (Holding Co, QIP, Route Connect, Heltar, BTA, unnamed vendors, dividend payers) | - | Heltar slump sale 29 Jul 2026: business purchase, not a new consolidated entity |

## 5. LINE ITEMS (financial tables, zero rows flagged)

| ROW IDs | category | A2 flags | note |
|---|---|---|---|
| R048 | CIN (p7) | - | - |
| R049-R269, R1037-R1038, R1076-R1082, R1128-R1129 | consolidated P&L and OCI, 6 period columns (R1128-1129 fill Q2 FY26 hedge cells) | ZERO_STANDING (exceptional item, hedge rows) | FY26 exceptional item (135.87) from note 7 |
| R270-R395, R1039, R1083, R1085-R1086 | consolidated segment table | ZERO_STANDING (exceptional item row) | - |
| R396-R475, R1040, R1087-R1088 | consolidated balance sheet 30.09.2026 vs 31.03.2026 | ZERO_STANDING (current borrowings) | - |
| R476-R561, R1041, R1089-R1090 | consolidated cash flow H1 FY27 vs H1 FY26 | ZERO_STANDING (several rows) | - |
| R597-R723, R1053, R1108-R1112 | standalone P&L and OCI | - | - |
| R724-R799, R1054, R1113-R1114 | standalone balance sheet | ZERO_STANDING (CWIP prior year) | - |
| R800-R883, R1055, R1115-R1116 | standalone cash flow | ZERO_STANDING (several rows) | - |
| R563-R577, R1094 | IPO utilisation table consolidated (5 rows x 3 cols) | ZERO_STANDING; RESTATED | restated standalone R884-898; unutilised Rs65.00 Cr R998 |
| R884-R898, R1119-R1120 | IPO utilisation table standalone (5 rows) | ZERO_STANDING; RESTATED | - |
| R579-R584, R1095 | net FX gain/loss table (1 row, 6 cols) | - | note 5 |
| R900-R905, R1057 | dividend from subsidiaries table (1 row) | ZERO_STANDING | column header printed 30.06.2025 (R901, R1057) as printed |

## 6. NOTES (23)

| ROW IDs | category | A2 flags | note |
|---|---|---|---|
| R562, R1091 | consol note 1 basis of preparation, 33 subsidiaries | - | - |
| R1092 | consol note 2 review and approval | - | - |
| R1093 | consol note 3 IPO utilisation | - | - |
| R998, R1096 | consol note 3a unutilised IPO in bank deposits | - | - |
| R578, R999, R1097 | consol note 4 QIP Rs867.50 Cr | RESTATED | standalone note 4 R899, R1122, R1003 |
| R1098 | consol note 5 FX presentation | - | - |
| R585-R588, R1000, R1099 | consol note 6 Heltar acquisition (Rs9.78 Cr deferred at 18 months) | NEW_ITEM_VS_Q1 | - |
| R1100 | consol note 7 exceptional items FY26 | - | - |
| R589, R1101 | consol note 7a | - | - |
| R590, R1102 | consol note 7b | - | - |
| R591-R593, R1001, R1103 | consol note 8 interim dividend 40% | RESTATED | standalone note 7 R906-908, R1004, R1125 |
| R1104 | consol note 9 regrouping | - | - |
| R1117 | standalone note 1 | - | - |
| R1118 | standalone note 2 | - | - |
| R1119 | standalone note 3 (ref IPO table) | - | - |
| R899, R1002-R1003, R1121-R1122 | standalone note 3a and note 4 QIP | RESTATED | - |
| R1123 | standalone note 5 segments Ind AS 108 | - | - |
| R1124 | standalone note 6 other income includes subsidiary dividends | - | - |
| R906-R908, R1004, R1125 | standalone note 7 dividend | RESTATED | - |
| R1126 | standalone note 8 regrouping | - | - |
| R1089, R1115 | cash flow indirect-method Note lines (unnumbered) | - | - |

## 7. ZERO_STANDING INDEX (42 cells; cell IDs by flag in structured file)
Consolidated P&L: exceptional item R109, R110, R112 (nil); hedge R166, R167, R171, R172 plus re-extraction R1128, R1129. Segment exceptional item: 3 cells in R336-R341. Balance sheet: current borrowings R454, R455. Consolidated cash flow: 7 line pairs between R484 and R545. Standalone: CWIP R727; cash flow lines R824-R829, R848-R849, R854-R855, R858-R859. Tables: IPO unutilised cells R565, R568, R570, R574, R886, R889, R891, R895; subsidiary dividend R900, R902. Canonical template signal: the exceptional item row (nil in Q2 FY27 and Q1 FY27, Rs135.87 Cr in Q2 FY26).

## 8. DIFFS VS Q1 FY27
- Auditor changed to MSKA (Q1: Walker Chandiok): AUDITOR_CHANGE. Predecessor named only as "another auditor".
- Board meeting 95 min (Q1 120 min). Agenda 5 items (Q1 4): new items are IPO variation rescission and MOA alteration.
- Dividend is second interim (Q1 first interim), Rs4, record date 02 Nov 2026.
- New note 6 Heltar business acquisition (29 Jul 2026), notes 3a/4 IPO and QIP carried.
- Entity list unchanged by name (33 vs 33); Sr.33 name blank in text layer (R965).

## 9. MISSING_FROM_STRUCTURED
None.

```yaml
stage: A2-enumerator
company: "ROUTE"
quarter: "q2fy27"
doctype: "results"
model: claude-sonnet-5-5
status: complete
ledger_path: "runs/route-q2fy27/work/ledger_results_route_q2fy27.md"
counts:
  notes: 23
  line_items: 256
  zero_standing: 42
  agenda_items: 5
  auditor_paras: 14
  entities: 77
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, ENTITY_CHANGE, RESTATED, NEW_ITEM_VS_Q1, FOOTNOTE_UNRESOLVED, MEETING_TIME, AUDITOR_CHANGE, RELIANCE_OTHER_AUDITORS, UNREVIEWED_ENTITIES, SIG_AFTER_MEETING]
ids_in_structured: 1129
ids_referenced: 1129
orphan_ids: []
missing_from_structured: []
gate_a2: pass
mismatch_note: ""
analyst_note: "Line_items 256 = 244 statement lines + 12 table rows (IPO x2, FX, subsidiary dividend); R1128-R1129 merged into existing hedge rows. zero_standing is 42 cells across 32 line rows. Consolidation list is unchanged by name versus Q1 (33 vs 33), but Annexure 1 Sr.33 name is blank in the text layer (R965), so a rename cannot be excluded. The auditor changed to MSKA; the predecessor is unnamed in the filing and is Walker Chandiok per the Q1 ledger. Board meeting ran 95 min against 120 min in Q1. New agenda items are the IPO variation rescission and the MOA object-clause expansion. Pages 7-11 and 14-16 are scrambled; ledger rows reference ID ranges, so A3 should read values from the structured file by ID."
```
