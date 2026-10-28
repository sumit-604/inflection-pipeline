# A2 LEDGER: NEOCHEM H1 FY27 results (q2fy27). Source status: connector-rebuilt copy of NSE filing (carried, not acted on).

=== A2 COUNT TEST ===
category: ids          structured header: 363 (NUMBER 273|ENTITY 29|FORWARD 4|DATE 23|QUALIFIER 34) grep_count: 363   sweep_count: 363   match: yes
category: notes        grep_count: 12 (9 numbered + 3 CF notes)   sweep_count: 12   match: yes
category: line_items   grep_count: 99 labels (31 BS + 27 results + 37 CF + 4 recon)   sweep_count: 99   match: yes
category: line_item_rows grep_count: 243 (R001-R235 + R263-R270)   sweep_count: 243   match: yes
category: zero_standing grep_count: 42 (A1 flags)   sweep_count: 42 (ledger ZERO_STANDING rows)   match: yes
category: agenda_items grep_count: 4 (fulltext numbered letter items)   sweep_count: 4   match: yes
category: auditor_paras grep_count: 7   sweep_count: 7   match: yes
category: entities     grep_count: 29   sweep_count: 29   match: yes
category: annexure_tables grep_count: 1   sweep_count: 1   match: yes
gate_a2: pass
=== END COUNT TEST ===

ids_in_structured: 363 | ids_referenced_in_ledger: 363 | orphan_ids: [] | match: yes

## NOTES
ROW_ID(s) | category | A2 flags | cross-ref / note
R343 | NOTES | - | Notes heading, p9
R344 | NOTES | - | Note 1 Board approval + unmodified LRR; cross-ref R323,R324
R345 | NOTES | - | Note 2 basis of preparation
R346 | NOTES | - | Note 3 investor query; cross-ref R258,R259,R325
R347 | NOTES | - | Note 4 H2FY26 balancing figure; cross-ref R342
R348 | NOTES | - | Note 5 single segment; cross-ref R297
R349 | NOTES | - | Note 6 EPS not annualised
R350 | NOTES | - | Note 7 no false or misleading statement
R351 | NOTES | - | Note 8 regrouping, not material
R352 | NOTES | FOOTNOTE_UNRESOLVED | Note 9 cyber fraud Jul 2026: no rupee amount and no recovered/balance split in A1 rows; cross-ref R298,R299,R303
R353 | NOTES | - | Cash flow note 1
R354 | NOTES | - | Cash flow note 2; reconciles to R263-R270
R355 | NOTES | - | Cash flow note 3 (bracket = outflow)
R358 | NOTES | AS_FILED | Footnote-type: asset-side label as filed; cross-ref R041,R042
R359 | NOTES | AS_FILED | Sign as filed; cross-ref R204,R205
R360 | NOTES | AS_FILED | Sign as filed; cross-ref R216,R217,R220,R221
R361 | NOTES | AS_FILED | Sign as filed; cross-ref R198,R199
R362 | NOTES | AS_FILED | Typo as filed; cross-ref R286
R363 | NOTES | - | MSME sub-lines of trade payables; cross-ref R019-R024

## LINE ITEMS: BALANCE SHEET (31 items x 2 dates)
ROW_ID(s) | category | A2 flags | cross-ref / note
R001-R004,R007-R040,R045-R062 | LINE ITEMS: BALANCE SHEET | - | Pairs 30.09.2026 / 31.03.2026

## LINE ITEMS: BALANCE SHEET
ROW_ID(s) | category | A2 flags | cross-ref / note
R005-R006 | LINE ITEMS: BALANCE SHEET | ZERO_STANDING | Money received against share warrants, nil both dates
R041-R044 | LINE ITEMS: BALANCE SHEET | ZERO_STANDING | Asset-side deferred tax (R041-42) and LT loans and advances (R043-44) nil both dates; label cross-ref R358

## LINE ITEMS: RESULTS (27 items x 4 periods)
ROW_ID(s) | category | A2 flags | cross-ref / note
R063-R082,R087-R114,R116-R126,R127-R129,R131,R133,R138-R145,R150-R161 | LINE ITEMS: RESULTS | - | H1FY27 / H2FY26 / H1FY26 / FY26; R116,R117,R131,R133 are nonzero FY26/H2 amounts on lines nil in H1FY27

## LINE ITEMS: RESULTS
ROW_ID(s) | category | A2 flags | cross-ref / note
R083-R086,R115,R130,R132,R134-R137,R146-R149 | LINE ITEMS: RESULTS | ZERO_STANDING | WIP/stock-in-trade nil all periods; exceptional items nil H1FY27 (61.89 in H2FY26, R116); short provision nil H1FY27 and H1FY26 (31.61 in H2FY26, R131); MAT nil all; discontinued ops nil

## LINE ITEMS: CASH FLOW (37 items x 2 periods)
ROW_ID(s) | category | A2 flags | cross-ref / note
R162-R167,R171,R174-R187,R190-R197,R199-R205,R208-R211,R214-R217,R220-R221,R225-R235,R177 | LINE ITEMS: CASH FLOW | - | Includes H1 CFO R200 and capex R210

## LINE ITEMS: CASH FLOW
ROW_ID(s) | category | A2 flags | cross-ref / note
R168-R170,R172-R173,R176,R188-R189,R198,R206-R207,R212-R213,R218-R219,R222-R224 | LINE ITEMS: CASH FLOW | ZERO_STANDING | Nil standing lines; R198 direct taxes paid H1 nil vs R126 provision; R224 equity issue nil H1 vs R225 FY26; R170,R176,R198,R224 nil in H1 only

## LINE ITEMS: CASH AND EQUIVALENTS RECON (4 items x 2 dates)
ROW_ID(s) | category | A2 flags | cross-ref / note
R263-R266,R269-R270 | LINE ITEMS: CASH AND EQUIVALENTS RECON | - | Reconciles to R234,R235

## LINE ITEMS: CASH AND EQUIVALENTS RECON
ROW_ID(s) | category | A2 flags | cross-ref / note
R267-R268 | LINE ITEMS: CASH AND EQUIVALENTS RECON | ZERO_STANDING | Fixed deposits under 12m nil both dates

## AGENDA ITEMS (letter items 1-4)
ROW_ID(s) | category | A2 flags | cross-ref / note
R308,R309,R310,R323,R334 | AGENDA ITEMS | - | Item 1: results + LRR, half year ended 30.09.2026; cross-ref R279

## AGENDA ITEMS
ROW_ID(s) | category | A2 flags | cross-ref / note
R280,R283,R311 | AGENDA ITEMS | - | Item 2: CFO appointment (KMP) on NRC recommendation
R281,R312 | AGENDA ITEMS | - | Item 3: CCO appointment (SMP)
R282,R313 | AGENDA ITEMS | - | Item 4: Solanki ceases as CFO/KMP, re-designated senior management; continues employed (R304)

## AGENDA: MEETING TIMES
ROW_ID(s) | category | A2 flags | cross-ref / note
R236,R237 | AGENDA: MEETING TIMES | - | 05:20 PM to 06:30 PM = 70 minutes

## ANNEXURE A (1 table, 4 rows x 3 persons)
ROW_ID(s) | category | A2 flags | cross-ref / note
R244-R248,R284,R287-R292,R304,R314 | ANNEXURE A | - | Shah (R244,R287,R288), Nair (R245,R289), Solanki (R246-R248,R290-R292)

## ANNEXURE A
ROW_ID(s) | category | A2 flags | cross-ref / note
M1,M2 | ANNEXURE A | MISSING_FROM_STRUCTURED | See MISSING section

## AUDITOR PARAS (7 units)
ROW_ID(s) | category | A2 flags | cross-ref / note
R249,R250,R251,R279,R293,R294,R300,R317 | AUDITOR PARAS | - | Addressee, firm, FRN, partner, UDIN, date

## AUDITOR PARAS
ROW_ID(s) | category | A2 flags | cross-ref / note
R252,R253,R254,R256,R295,R335,R336,R337 | AUDITOR PARAS | - | Scope/standards: SRE 2410, s.143(10), s.133, Reg 33, no audit opinion
R338 | AUDITOR PARAS | - | Conclusion, unmodified. No Emphasis of Matter, Other Matter or Going Concern paragraph found (absence recorded)

## ENTITIES (29 rows; standalone only, no subsidiary list)
ROW_ID(s) | category | A2 flags | cross-ref / note
R274-R302 | ENTITIES | - | Consolidation list: none. ENTITY_CHANGE: not assessable, no prior ledger. R285,R286 former names

## SIGNATURE BLOCKS
ROW_ID(s) | category | A2 flags | cross-ref / note
R255,R321,R328,M3 | SIGNATURE BLOCKS | - | MD Makati DIN 00188382; BS signed 27-10-2026 (R321); notes (R328); results and CF blocks M3. No timestamps in A1 to compare with 06:30 PM close

## DATES (remaining)
ROW_ID(s) | category | A2 flags | cross-ref / note
R307,R315,R316,R318-R320,R322,R324-R327,R329 | DATES | RESTATED(R315,R316 = R247,R248) | Period-end and column dates

## LETTERHEAD / IDENTIFIERS / REGULATORY
ROW_ID(s) | category | A2 flags | cross-ref / note
R238-R243,R257,R258,R260-R262,R301,R302 | LETTERHEAD / IDENTIFIERS / REGULATORY | - | Pin, phone, CIN, GSTIN, ISIN, Reg 30, Rule 7; Note 3 items R258,R259 cross-ref R346
R259 | LETTERHEAD / IDENTIFIERS / REGULATORY | ZERO_STANDING | NIL investor complaints pending 30-Sep-2026; cross-ref R346

## FORWARD / DISCLOSURE STATEMENTS
ROW_ID(s) | category | A2 flags | cross-ref / note
R303,R304,R305,R306 | FORWARD / DISCLOSURE STATEMENTS | - | R303 cyber-fraud recovery in process (cross-ref R298,R299,R352); R306 is a provenance instruction

## PROVENANCE (connector-rebuilt copy; carried, not acted on)
ROW_ID(s) | category | A2 flags | cross-ref / note
R271-R273,R330-R333 | PROVENANCE | SOURCE_CONNECTOR_COPY | Numbers pending verification against NSE original

## QUALIFIERS (remaining)
ROW_ID(s) | category | A2 flags | cross-ref / note
R339-R342,R356,R357 | QUALIFIERS | - | Unit/status labels; R342 balancing column; R357 CF comparative full-year FY26

## MISSING_FROM_STRUCTURED (loop back to A1)
M1 | fulltext line 88-90 | MISSING_FROM_STRUCTURED | Annexure A row 4 'Disclosure of relationships between directors': Shah, Nair, Solanki each 'Not applicable. He is not related to any Director or KMP of the Company.' (3 cells)
M2 | fulltext line 83 | MISSING_FROM_STRUCTURED | Annexure A row 3, Nair: 'Holds a degree in Chemical Engineering and a diploma in business administration'
M3 | fulltext lines 216, 291 | MISSING_FROM_STRUCTURED | Signature blocks 'Place: Ahmedabad. Date: 27-10-2026 ... Swapnil R Makati, Managing Director' on the results statement (line 216) and cash flow statement (line 291); A1 holds only the BS block (R321)

## ZERO_STANDING ROWS (A1 IDs, 42)
R005, R006, R041, R042, R043, R044, R083, R084, R085, R086, R115, R130, R132, R134, R135, R136, R137, R146, R147, R148, R149, R168, R169, R170, R172, R173, R176, R188, R189, R198, R206, R207, R212, R213, R218, R219, R222, R223, R224, R259, R267, R268

## MATERIALITY FLAGS (enumerated, not interpreted)
- Nil in H1FY27 but nonzero in H2FY26/FY26: Exceptional items (R115 vs R116), Short provision (R130 vs R131), Direct taxes paid (R198 vs R199), Equity issue proceeds (R224 vs R225), Loss on sale of PPE (R170 vs R171).
- Board meeting 70 minutes (R236,R237); CFO change at the results meeting (items 2-4).
- Note 9 cyber fraud: no amount in structured rows (FOOTNOTE_UNRESOLVED).
- Limited review only; no EoM / Other Matter / Going Concern paragraph present.

```yaml
stage: A2-enumerator
company: "NEOCHEM"
quarter: "q2fy27"
doctype: "results"
model: claude-sonnet-5-5
status: complete
ledger_path: "runs/neochem-q2fy27/work/ledger_results_neochem_q2fy27.md"
counts:
  notes: 12
  line_items: 99
  zero_standing: 42
  agenda_items: 4
  auditor_paras: 7
  entities: 29
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, FOOTNOTE_UNRESOLVED, AS_FILED, RESTATED, SOURCE_CONNECTOR_COPY, MISSING_FROM_STRUCTURED]
ids_in_structured: 363
ids_referenced: 363
orphan_ids: []
missing_from_structured: [M1 Annexure A relationship disclosure (fulltext 88-90), M2 Nair education (line 83), M3 results and cash flow signature blocks (lines 216, 291)]
gate_a2: pass
mismatch_note: ""
analyst_note: "Source is a connector-rebuilt copy of the NSE filing; carried, not acted on. 42 rows are ZERO_STANDING (A1 flags, all matched). Nil in H1FY27 but nonzero in H2FY26/FY26: exceptional items, short provision for prior year, direct taxes paid, equity issue proceeds, loss on sale of PPE. Note 9 (July 2026 cyber fraud) gives no rupee amount in A1 rows, so FOOTNOTE_UNRESOLVED; A3 should read it. Limited review only, no EoM or going concern paragraph. Standalone filing, no subsidiary list, ENTITY_CHANGE not assessable (no prior ledger). Board met 70 minutes and changed the CFO at the results meeting. Three small A1 gaps (M1-M3) need no re-extraction for ledger purposes."
```
