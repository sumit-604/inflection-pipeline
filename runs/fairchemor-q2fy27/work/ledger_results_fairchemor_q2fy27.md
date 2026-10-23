# A2 LEDGER: Fairchem Organics (FAIRCHEMOR) Q2 FY27 results filing 22-Oct-2026
Source: A1 structured extraction (R001-R484). Rows reference IDs only; values stay in the structured file.
Prior ledger: none (first run). ENTITY_CHANGE diff not possible; NOT FOUND.

ids_in_structured: 484 | ids_referenced_in_ledger: 484 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: notes          grep_count: 9    sweep_count: 9    match: yes   (Notes 1-7, cash flow Note 1, Note 6 continuation)
category: footnotes      grep_count: 8    sweep_count: 8    match: yes   (unnumbered: R456 R458 R459 R462 R463 R464 R467 R474)
category: line_items     grep_count: 353  sweep_count: 353  match: yes   (P&L 151 + BS 76 + CF 72 + segment 54)
category: zero_standing  grep_count: 19   sweep_count: 19   match: yes   (NUMBER rows with value "-" = rows flagged)
category: agenda_items   grep_count: 2    sweep_count: 2    match: yes   (Board outcome items 1 and 2)
category: auditor_paras  grep_count: 3    sweep_count: 3    match: yes   (R450 R451 R452; no EoM / Other Matters / Going Concern found)
category: entities       grep_count: 36   sweep_count: 36   match: yes   (R376-R411; header ENTITY 36)
category: signatures     grep_count: 3    sweep_count: 3    match: yes   (R423 R426 R446)
gate_a2: pass
=== END COUNT TEST ===

## 1. NOTES (numbered)
ROW ID | category | A2 flags | note
R468 | CF Note 1 (Indirect Method, Ind AS 7) | - | cash flow statement note, p7
R469 | Note 1 | - | review, Board approval 22-Oct-2026
R470 | Note 2 | - | Ind AS basis
R471 | Note 3 | - | single segment; domestic revenue
R475 | Note 4 | - | no subsidiary/associate/JV
R476 | Note 5 | - | Labour Codes exceptional Rs 88.27 L (FY26 only); FY27 periods nil (see ZERO_STANDING)
R477 | Note 6 | - | buyback 4,25,000 sh at Rs 800, cap Rs 34 Cr
R478 | Note 6 cont. | - | settled 21-Jan-2026, extinguished 27-Jan-2026
R479 | Note 7 | - | results on websites

## 2. FOOTNOTES (unnumbered)
R456 | Exceptional Item (Refer Note 5) | - | pointer
R458 | EPS "*Not annualised" | - | defines asterisk
R459 | asterisk on EPS values | - | see R458
R462 | unlabelled CA subtotal 17,600.86/16,793.56 | FOOTNOTE_UNRESOLVED | between Other Current Assets and Asset Held for Sale
R463 | "Tota Equity" typo | - | label typo only
R464 | unlabelled CL subtotal 8,862.94/10,326.16 | FOOTNOTE_UNRESOLVED | before Liabilities held for sale
R467 | stray label "Changes" in CF | FOOTNOTE_UNRESOLVED | no value attached
R474 | segment "Less Exceptional Items (Note 5)" | - | cross-ref

## 3. LINE ITEMS (grouped by statement; every ID listed)
ROW ID range | statement | flags | note
R009-R159 | Statement of P&L p5, 151 rows (Q2FY27, Q1FY27, Q2FY26, H1FY27, H1FY26, FY26) | ZERO_STANDING on R009 R010 R011 R036 R078 | Exceptional Item row; FY26 value R086 = 88.27 non-zero; R141 Other Equity FY26 only
R160-R235 | Balance sheet p6, 76 rows | ZERO_STANDING on R160 R161 R162; FOOTNOTE_UNRESOLVED on R192 R193 R226 R227 (unlabelled subtotals) | Held for sale R194 R195 R228 R229 non-zero at both dates; lease rows R165 R206 present at 30-Sep-2026, nil at 31-Mar-2026
R236-R307 | Cash flow p7, 72 rows | ZERO_STANDING on R236 R245 R247 R258 R267 | five nil in H1 FY26 only; R287 R288 R295 R298 populated in H1 FY27
R309-R362 | Segment table p8, 54 rows (R308 is a note number, section 10) | RESTATED; ZERO_STANDING on R309 R310 R311 R335 R342 R344 | segment revenue R312-R317 restates R013 R012 R014 R017 R018 R015; segment PBT R345-R350 restates P&L PBT; exceptional rows nil in FY27 periods and H1 FY26

## 4. ZERO_STANDING register (19)
R009 R010 R011 R036 R078 (P&L Exceptional Item nil: Q2FY27, Q1FY27, Q2FY26, H1FY27, H1FY26)
R160 R161 R162 (BS dash at 31-Mar-2026: Right to Use Asset, Lease Liabilities non-current, Current Tax Liabilities)
R236 R245 R247 R258 R267 (CF H1 FY26 dashes: Provision for NC Tax Assets, Initial Direct Cost ROU, FD redemption, lease repayment, restricted bank balance)
R309 R310 R311 R335 R342 R344 (segment: Add Interest Income Q1FY27; Less Exceptional Items nil Q2FY27, Q1FY27, Q2FY26, H1FY27, H1FY26)
Materiality: the Exceptional Item line stands nil in every FY27 period while Note 5 labels FY26 Rs 88.27 L as the Labour Code charge. Lease lines nil at FY26 end, populated at 30-Sep-2026.

## 5. AGENDA ITEMS (Board outcome letter p1-2) and meeting times
R002 R003 | meeting 03.30 pm to 04.15 pm (45 minutes) | - |
R448 R449 R416 R417 R418 | Item 1: approve unaudited results Q2/H1 FY27 with limited review report | - | unmodified review conclusion
R004 R412 R386 R380 R385 | Item 2: RPT, purchase of 2 pieces of land from CMD and relatives | RELATED_PARTY | Audit Committee recommended; Annexure B detail R413 R414 R415 R409 R410 R411 R480 R481 R482 R483 R484 R372 R373 R374 R375
No AR approval, AGM, record date, dividend, director appointment, auditor change, scrutinizer, ESOP or capital-raising item found in the structured file. NOT FOUND.

## 6. ANNEXURES / PAGE-LEVEL IDENTIFIERS
R001 R005 R376 R377 R378 R387 R388 R422 R423 | p1-2 header, Annexure B basis, CS signature | - |
R006 R007 R008 R383 R393 R420 R421 R426 R427 | auditor identity, UDIN, signature | SIGNATURE_BEFORE_MEETING_END | auditor stamp 15:59:19 earlier than Board conclusion 16.15
R371 R408 R446 R447 | CMD DIN, signature 15:41:45 | SIGNATURE_BEFORE_MEETING_END | CMD stamp before Board conclusion 16.15
Director profiles: none in this filing (no appointment item). NOT FOUND.

## 7. AUDITOR PARAGRAPHS (3)
R450 | para 2 basis of preparation Ind AS 34 | - |
R451 | review-not-audit scope | - | SRE 2410 R391 R392
R452 | unmodified conclusion | - | no EoM, Other Matters or Going Concern language found
Supporting: R389 R390 R424 R425

## 8. ENTITIES (36, R376-R411)
R376-R411 | all entity rows | ENTITY_CHANGE not assessable (no prior ledger) | R400 states no subsidiaries/associates/JVs, so the consolidation list is empty; R395 R396 R399 product/segment names; R386 R409 R410 related parties (CMD, relatives, promoters)

## 9. SIGNATURES (3)
R423 | CS Jatin Jain 2026.10.22 16:24:05 | - | after Board conclusion
R426 | auditor Jeyur Shah 15:59:19 | SIGNATURE_BEFORE_MEETING_END | 16 minutes before conclusion
R446 | CMD 15:41:45 | SIGNATURE_BEFORE_MEETING_END | 34 minutes before conclusion

## 10. REMAINING NUMBER ROWS (non-table items)
R308 | Note 3 segment count (1) | - | ties to R471
R363 R364 R343 | Labour Codes count 4; Rs 88.27 L (R364) ties to P&L R086 and segment R343 | RESTATED
R365 R366 R367 R368 R369 R370 | buyback numbers: 4,25,000 sh, 3.26%, FV Rs 10, Rs 800, Rs 34 Cr | RESTATED across R477 R478
R372 R373 R374 R375 | Annexure B land numbers: 2 pieces, Rs 12.01 Cr, 6.07% shareholding, 6,182 sq m | RELATED_PARTY | ties R412-R415

## 11. FORWARD (4): R412 R413 R414 R415 | land RPT only; no guidance, capex or targets in filing (A1 header)

## 12. DATES (32): R416-R447
R416-R447 | date rows | - | R436 postal ballot 26-Dec-2025; R438 Labour Codes 21-Nov-2025; R440-R445 buyback timeline Nov-2025 to Jan-2026; R423 R426 R446 signature stamps (section 9); R434 R435 truncated "30, 2026"/"30, 2025" as printed

## 13. QUALIFIERS (37): R448-R484
R448-R484 | qualifier rows | placed per sections 1, 2, 5; remaining here | R449 unaudited; R451 review not audit; R453 R460 R465 R472 unit qualifiers; R454 R455 R461 R466 R473 audited/unaudited column marks; R457 face value; R477-R484 per sections 1 and 5

## Coverage index (primary placement)
R001-R008 sec5/6/10 | R009-R159 sec3 | R160-R235 sec3 | R236-R307 sec3 | R308 sec10 | R309-R362 sec3 | R363-R375 sec10 | R376-R411 sec8 | R412-R415 sec11 | R416-R447 sec12 | R448-R484 sec13 (with secs 1, 2, 5)

```yaml
stage: A2-enumerator
company: "FAIRCHEMOR"
quarter: "q2fy27"
doctype: "results"
model: claude-sonnet-5-5
status: complete
ledger_path: "runs/fairchemor-q2fy27/work/ledger_results_fairchemor_q2fy27.md"
counts:
  notes: 9
  line_items: 353
  zero_standing: 19
  agenda_items: 2
  auditor_paras: 3
  entities: 36
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, FOOTNOTE_UNRESOLVED, RESTATED, RELATED_PARTY, SIGNATURE_BEFORE_MEETING_END]
ids_in_structured: 484
ids_referenced: 484
orphan_ids: []
missing_from_structured: []
gate_a2: pass
mismatch_note: ""
analyst_note: "Auditor (15:59:19) and CMD (15:41:45) signature stamps precede the 16.15 Board conclusion; CS stamp 16:24:05 follows it. The 45-minute Board meeting carried two items: results, and a Rs 12.01 Cr land RPT with the CMD and relatives (6,182 sq m, adjoining plant). Exceptional Item is nil in all FY27 periods; the FY26 Rs 88.27 L is the Labour Code charge. Unlabelled subtotals (R192/R193, R226/R227) and a stray CF label (R467) sit near held-for-sale lines, which are non-zero at both dates (R194/R195, R228/R229). Lease lines are nil at FY26 end but present at 30-Sep-2026. No prior ledger, so ENTITY_CHANGE was not tested; Note 4 states no subsidiaries."
```
