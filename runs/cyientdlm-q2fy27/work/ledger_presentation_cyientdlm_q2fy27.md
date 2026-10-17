# A2 LEDGER: CYIENT DLM Q2 FY27 INVESTOR PRESENTATION (A2 enumerator, claude-sonnet-5-5)
Source: A1 structured extraction only. Slide footer = PDF page - 1. Units INR Mn.

=== A2 COUNT TEST ===
category: slides          grep_count: 18  sweep_count: 18  match: yes   (fulltext "[page N]" markers = 18; table A = 18)
category: slide_numbers   grep_count: 280 sweep_count: 280 match: yes   (NUMBER rows R001-R280; header NUMBER=280)
category: line_items      grep_count: 34  sweep_count: 34  match: yes   (17 P&L lines x 2 tables; 51 + 51 value rows = R149-R199, R227-R277)
category: zero_standing   grep_count: 0   sweep_count: 0   match: yes   (no nil/dash/zero-valued line items in any table)
category: entities        grep_count: 20  sweep_count: 20  match: yes   (ENTITY R281-R300)
category: forward         grep_count: 21  sweep_count: 21  match: yes   (FORWARD R301-R321)
category: dates           grep_count: 21  sweep_count: 21  match: yes   (DATE R322-R342)
category: footnotes_qualifiers grep_count: 30 sweep_count: 30 match: yes (QUALIFIER R343-R372)
category: agenda/auditor/turns/questions: not applicable (presentation)
ids_in_structured: 372 | ids_referenced_in_ledger: 372 | orphan_ids: [] | match: yes
gate_a2: pass
=== END COUNT TEST ===

## A. Slide ledger (18)
| Slide (footer) | PDF page | Title | Type | Structured IDs | Flags / note |
|---|---|---|---|---|---|
| - | 1 | Exchange cover letter (BSE/NSE, 15 Oct 2026) | text | R001-R004, R281-R284, R298, R322-R324 | signature 16:35:12 IST on 15 Oct |
| - | 2 | Title: Investor Presentation Q2 FY27 | text | R325, R372 | |
| 2 | 3 | Confidentiality statement | text | R371 | boilerplate grouped |
| 3 | 4 | Today's presenters | text/photo | R285-R287 | Chairman, MD&CEO, CFO all present; no MGMT_ABSENCE |
| 4 | 5 | Section divider (Business Overview / Finance Updates) | text | none | no data rows |
| 5 | 6 | Industry/market opportunity (EMS, DC, semicap, robotics) | text+chart | R005-R029, R288-R294, R301-R311, R326-R333, R368-R370 | dense third-party and DLM-estimate figures |
| 6 | 7 | Strategy: STRENGTHEN / EXPAND / TRANSFORM and margin path | text+chart | R030-R037, R299, R312-R317, R334-R336 | margin targets 9-11% -> 11-13% -> 13-18% |
| 7 | 8 | Business overview highlights | text | R038-R041, R295-R297, R318 | ENTITY_CHANGE Altek -> Cyient DLM Electronics Inc. |
| 8 | 9 | Section divider | text | none | no data rows |
| 9 | 10 | Q2 FY27 dashboard | table/text | R042-R060, R342, R344 | |
| 10 | 11 | KEY KPI trend: revenue, EBITDA, PAT, EBITDA % | chart | R061-R093, R319, R337, R343, R345-R348 | chart labels jumbled; FOOTNOTE_UNRESOLVED |
| 11 | 12 | Order book, working-capital days, OpFCF | chart | R094-R130, R338, R349, R350 | chart labels jumbled; FOOTNOTE_UNRESOLVED |
| 12 | 13 | Revenue mix and segment growth | pie/chart | R131-R148, R300, R351, R352 | pie slices unassigned by A1 |
| 13 | 14 | Q2 financials detailed | table | R149-R205, R320, R339, R353-R359 | |
| 14 | 15 | H1 FY27 dashboard | table/text | R206-R226, R340 | |
| 15 | 16 | H1 financials detailed | table | R227-R280, R321, R341, R360-R367 | |
| 16 | 17 | Q&A | text | none | no data rows |
| 17 | 18 | Thank you | text | none | no data rows |
DROPPED_SLIDE: not assessable, prior-quarter ledger not available.

## B. Slide numbers (every NUMBER row, 280)
| IDs | Category | Flags | Note |
|---|---|---|---|
| R001-R004 | cover-letter identifiers | | date, scrip, CIN, signature |
| R005-R029 | market-size figures (p6) | RESTATED | R011/R012/R013 headline restate R005/R008 |
| R030-R037 | strategy margins/industry counts (p7) | RESTATED | R030=R035, R031=R037 |
| R038-R041 | highlights (p8) | RESTATED | R038=R043=R151, R040=R147 |
| R042-R060 | Q2 dashboard (p10) | RESTATED | R042=R149, R044=R161, R046=R194, R048=R188, R050=R099, R052=R164, R058/R059/R091=R194, R060=R078=R092=R202 |
| R061-R093 | KPI chart labels (p11) | CHART_LABEL_JUMBLED | period by position only; R072=R044, R075=R048, R084=R046, R083=R195, R076=R189, R077=R201 |
| R094-R130 | order book, DIO/DPO/DSO, advances, NWC, OpFCF (p12) | CHART_LABEL_JUMBLED | R099=R050=R214; R130 asterisk footnote R350 |
| R131-R148 | mix and segment growth (p13) | SLICE_UNASSIGNED | R140/R148 India 7% restated; R147=R040 |
| R149-R199 | Q2 P&L table value rows (p14) | | see section C |
| R200-R205 | Q2 note-embedded numbers (p14) | RESTATED | R202=R060, R204=R194 |
| R206-R226 | H1 dashboard (p15) | RESTATED | R206=R227, R208=R239, R210=R272, R212=R266, R214=R050 |
| R227-R277 | H1 P&L table value rows (p16) | | see section C |
| R278-R280 | H1 note-embedded numbers (p16) | RESTATED | R279=R201, R280=R202 |

## C. Line items (34 lines; value rows referenced)
Q2 table (p14): Revenue R149-R151 | Material cost R152-R154 | Employee cost R155-R157 | Other expense R158-R160 | EBITDA R161-R163 | EBITDA % R164-R166 | D&A R167-R169 | EBIT R170-R172 | EBIT % R173-R175 | Finance cost R176-R178 | Other income R179-R181 | PBT R182-R184 | Tax R185-R187 | Reported PAT R188-R190 | Reported PAT % R191-R193 | Normalized PAT R194-R196 | Normalized PAT % R197-R199.
H1 table (p16): Revenue R227-R229 | Material R230-R232 | Employee R233-R235 | Other expense R236-R238 | EBITDA R239-R241 | EBITDA % R242-R244 | D&A R245-R247 | EBIT R248-R250 | EBIT % R251-R253 | Finance cost R254-R256 | Other income R257-R259 | PBT R260-R262 | Tax R263-R265 | Reported PAT R266-R268 | Reported PAT % R269-R271 | Normalized PAT R272-R274 | Normalized PAT % R275-R277.
ZERO_STANDING: none. All 34 lines carry non-zero values. Notes R355/R362 reference a "DMC %" that no table line shows (note reference, not a MISSING row).

## D. Entities (20)
| IDs | Type | Flags / note |
|---|---|---|
| R281, R282 | exchange addressees | |
| R283 | signatory (Company Secretary) | |
| R284 | issuer | |
| R285-R287 | presenters | |
| R288-R293 | third-party sources | |
| R294 | ISM (policy) | |
| R295, R296 | Altek Electronics / Cyient DLM Electronics Inc. | ENTITY_CHANGE (renamed, integration completed) |
| R297 | B2S strategy | |
| R298-R300 | grouped summaries (addresses, verticals, segments) | |

## E. Forward statements (21)
R301-R311 market forecasts and company estimates (p6) | R312-R318 strategy plans and margin targets (p7-8) | R319-R321 "continued investment" cost commentary (p11, p14, p16). R320 and R321 restate the employee-cost line in two phrasings.

## F. Dates (21)
R322-R324 cover letter | R325 deck quarter | R326-R333 source and forecast years | R334-R336 stage labels | R337-R341 chart/comparison periods | R342 dashboard. R322/R324 restate within cover letter.

## G. Footnotes and qualifiers (30)
| IDs | Item | Flags |
|---|---|---|
| R343 | marker "1" on KPI trend title | FOOTNOTE_UNRESOLVED |
| R344-R348 | normalized basis definitions (p10-11) | |
| R349 | unit note p12 | |
| R350 | asterisk, OpFCF Rs 172 Mn | FOOTNOTE_UNRESOLVED (marker not on a metric) |
| R351, R352 | mix definitions p13 | |
| R353-R359 | Q2 table unit and notes | |
| R360-R367 | H1 table unit and notes | |
| R368-R370 | source and estimate qualifiers p6 | |
| R371 | confidentiality boilerplate | grouped |
| R372 | confidential footer on every slide | grouped |
Cross-ref: R358/R359 vs R367 restate the earnout reversal (196M FY26, 182M FY27). R357 (10.4%) and R365 (21%) cover different periods.

## H. MISSING_FROM_STRUCTURED
None found.

```yaml
stage: A2-enumerator
company: "CYIENTDLM"
quarter: "q2fy27"
doctype: "presentation"
model: claude-sonnet-5-5
status: complete
ledger_path: "runs/cyientdlm-q2fy27/work/ledger_presentation_cyientdlm_q2fy27.md"
counts:
  notes: 30
  line_items: 34
  zero_standing: 0
  agenda_items: 0
  auditor_paras: 0
  entities: 20
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 18
  slide_numbers: 280
flags_raised: [ENTITY_CHANGE, FOOTNOTE_UNRESOLVED, RESTATED, CHART_LABEL_JUMBLED, SLICE_UNASSIGNED]
ids_in_structured: 372
ids_referenced: 372
orphan_ids: []
missing_from_structured: []
gate_a2: pass
mismatch_note: ""
analyst_note: "No ZERO_STANDING rows exist; both P&L tables carry 17 non-zero lines. Notes reference a DMC % line that no table shows. DROPPED_SLIDE could not be run: no prior ledger. Chart pages 11-12 and the p13 pie carry period or slice assignments A1 could not fix, so A3/A4 must not read period meaning into R061-R148 labels without the fulltext. Two unresolved footnotes: marker 1 (R343) and the OpFCF asterisk (R350). The earnout reversal (196M FY26, 182M FY27) is restated on pp 10, 11, 14, 15, 16 and drives the normalized-vs-reported PAT gap."
```
