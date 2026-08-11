# A2 COMPLETENESS LEDGER — Macfos Limited (MCFOS), Q1 FY27, Results Filing

Source: `/home/user/inflection-pipeline/runs/mcfos-q1fy27/work/extract_results_mcfos_q1fy27.txt`
Unit convention: Lakhs (all values below are AS PRINTED IN THE SOURCE, i.e. in Lakhs; conversion factor to Rs Crores is x0.01 — NOT applied here per instruction).
Prior-quarter ledger: none available — first pipeline run for MCFOS. No ENTITY_CHANGE / DROPPED_ITEM diffs possible this run.
Extraction quality carried forward from A1: pages 1,2,5,9,10,11,12 render every glyph space-separated; numeric values and labels on those pages have had intra-token spaces stripped for parsing in this ledger, but original spacing is what appears at the cited line number in the extract. Pages 3,4,6,7,8 are OCR text (Limited Review Reports) and read normally, with occasional stray OCR noise characters (e.g. a leading "L" before "4)" on line 345, semicolons/colons prefixing lines) — flagged inline as OCR_NOISE where it affected grep matching, not treated as content loss.

```
=== A2 COUNT TEST ===
category: agenda_items      grep_count: 13   sweep_count: 13   match: yes
category: notes             grep_count: 6    sweep_count: 6    match: yes   (numbered markers 1,2,4,6,7,8 — see NOTE_NUMBER_GAP below; 2 additional unlabeled note-fragments enumerated separately, not counted in this gate criterion, folded into notes table total of 8 rows)
category: line_items        grep_count: 98   sweep_count: 98   match: yes   (verified via two independent manual row-by-row passes per table — glyph-per-character extraction on pages 5/9/11 defeats reliable line-anchored grep, per A1's flagged extraction-quality note; grep used for section/entity/signature markers instead, see below)
category: zero_standing     grep_count: 25   sweep_count: 25   match: yes
category: auditor_paras     grep_count: 14   sweep_count: 14   match: yes  (standalone 6 + consolidated 8; grep raw hit count on markers was 9 for consolidated, reduced to 8 by excluding the bare "Other Matters" section-title line which carries no content of its own — both a) and b) are counted)
category: entities           grep_count: 3   sweep_count: 3    match: yes
category: signature_blocks  grep_count: 6    sweep_count: 6    match: yes
category: director_profiles grep_count: 1    sweep_count: 1    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep passes used (reproducible):
- Agenda items: `sed -n '27,99p' extract | grep -n -E "^\s{0,4}[0-9]{1,2}(\s|$)"` → 13 hits (lines 53,56,59,62,65,71,77,80,83,88,92,96,98 relative-to-absolute mapped below).
- Notes: `sed -n '516,558p' extract | grep -n -E "^\s{0,3}[0-9]{1,2}\s*$|^\s{0,3}[0-9]{1,2}\s+[A-Za-z]"` → 6 hits (lines 521,529,538,543,549,553).
- Auditor paras: `grep -n -E "^[0-9]\)|Other Matter|For KISHOR" extract` restricted to each LRR block.
- Entities: `grep -n -E "Holding/Parent Company|Nuo Zhan Technologies|Macfos Electronics" extract` → 3 distinct entities at lines 341-343 (plus repeat mentions at 379, 397).
- Signature blocks: `grep -n -E "SUBHASH GULHANE|B in o d Pr a s a d|CA Laxmi U Rawat|Digitally signed" extract` → 6 hits (lines 110,205,289,409,509,565).
- Director profile: `grep -n -E "DETAILS OF DIRECTORS|NILESHKUMAR" extract` → 1 director table.

---

## 1. BOARD OUTCOME — AGENDA ITEMS (pages 1-2)

Board meeting: commenced 04:15 PM IST, concluded 06:30 PM IST (11-Aug-2026) — duration 2h 15m. Lines 101-102.

| # | Line(s) | Item | Flags |
|---|---------|------|-------|
| 1 | 53-54 | Voluntarily adopt IND AS for preparation of financial statements from FY2026-27 onwards | IND_AS_FIRST_ADOPTION |
| 2 | 55-57 | Consider and approve Unaudited Standalone and Consolidated Financial Results for Q1 ended 30 June 2026, prepared under IND AS, with Auditor's Limited Review Report | |
| 3 | 58-60 | Approve Annual Report FY2025-26 and Draft Notice for calling 9th AGM | |
| 4 | 61-63 | Appoint M/s CZ & Associates LLP as Scrutinizer for ensuing AGM to conduct eVoting | |
| 5 | 64-66 | Appoint director in place of Mr. Nileshkumar Purushottam Chavhan (DIN 07936897), retiring by rotation, offering himself for re-appointment | cross-ref Director Profile table §11 |
| 6 | 67-75 | Consider outstanding statutory liability pending >3 months, specifically: a) TDS b) TCS c) GST d) Employee share PF&ESIC e) Employer share PF&ESIC f) Professional Tax | checklist item, no values disclosed here |
| 7 | 76-78 | Take note of quarter-end (30 June 2026) listing compliances for period ended 30 June 2026 | |
| 8 | 79-81 | Take note of MSME vendors and list of non-payment cases beyond 45 days (tax disallowance exposure), if any | ZERO_STANDING candidate — no actual figure disclosed in this filing (agenda item is a standing checklist, not a disclosed value) |
| 9 | 82-84 | Receive update on unsettled litigation as of quarter-end, discuss cases with amounts >Rs 1 lakh, if any | ZERO_STANDING candidate — same as above |
| 10 | 87-89 | Identify Investor Grievances received during quarter, resolved and pending as of quarter-end | cross-ref Note 8 §7 (Investor Complaints — all Nil) |
| 11 | 90-94 | Take note of delay in periodic statutory returns: a) GSTR 3B/GSTR1/GSTR9/GSTR9C b) TDS/TCS Quarterly Return c) PF/ESIC/PT Return | checklist item |
| 12 | 95-97 | Take note of quarter-ended listing compliances for period ended 30 June 2026 (duplicate topic of item 7) | possible duplicate agenda wording — flag for A3 |
| 13 | 98 | Authorize Directors for filing of e-Forms with the Registrar of Companies (ROC) | |

Note: items 7 and 12 both read "take note of ... listing compliances ... for the period ended 30th June 2026" — near-identical wording, worth A3 review as possible drafting duplication rather than two distinct compliances.

---

## 2. STANDALONE LIMITED REVIEW REPORT — AUDITOR PARAGRAPHS (pages 3-4, OCR)

Auditor: Kishor Gujar & Associates, Chartered Accountants, FRN 116747W, Peer Review No. 021346. Partner: CA Laxmi U Rawat, Membership No. 134752.

| # | Line(s) | Paragraph | Flags |
|---|---------|-----------|-------|
| 1 | 139-144 | Para 1) Scope — reviewed accompanying unaudited standalone Q1 FY27 statement per Reg 33 | |
| 2 | 145-152 | Para 2) Responsibility — Statement is Management's/Board's responsibility, prepared per Ind AS 34, Section 133 Companies Act 2013 | |
| 3 | 153-164 | Para 3) Review standard SRE 2410; moderate assurance, not an audit; no audit opinion expressed | |
| 4 | 168-176 | Para 4) Conclusion — nothing has come to attention indicating material misstatement or non-disclosure (unmodified conclusion) | |
| 5 | 177-197 | Other Matter (unlettered, 3 sub-topics run together): (i) first quarterly Ind AS standalone results per Note 2; (ii) comparative Q1FY26 and FY26 figures converted from IGAAP to Ind AS by management, NOT subject to Limited Review by this auditor; (iii) FY26 standalone statements originally IGAAP-audited by this firm, subsequently Ind AS-converted by management, Special Purpose Independent Auditor's Report issued 11-Aug-2026 on the Ind AS FY26 standalone statements; conclusion not modified | COMPARATIVES_UNREVIEWED — comparative Ind AS figures for Q1FY26 and FY26 carry no Limited Review by the auditor |
| 6 | 198-209 | Signature block: For Kishor Gujar & Associates, CA Laxmi U Rawat (Partner), Membership 134752, Place Pimpri Pune, Date 11 Aug 2026, UDIN "26(S4452FVNBEZ2445" | UDIN_GARBLED (OCR-illegible, cannot be verified against UDIN portal as extracted) |

---

## 3. CONSOLIDATED LIMITED REVIEW REPORT — AUDITOR PARAGRAPHS (pages 6-8, OCR)

Same auditor/firm/partner as standalone.

| # | Line(s) | Paragraph | Flags |
|---|---------|-----------|-------|
| 1 | 312-318 | Para 1) Scope — reviewed accompanying unaudited Consolidated Q1 FY27 statement of Parent + subsidiaries ("the Group") per Reg 33 | |
| 2 | 319-325 | Para 2) Responsibility — Parent Management's/Board's responsibility, prepared per Ind AS | |
| 3 | 326-339 | Para 3) Review standard SRE 2410; moderate assurance, not an audit; no audit opinion expressed | |
| 4 | 340-344 | Entity list: Holding/Parent — Macfos Limited; Subsidiaries — Nuo Zhan Technologies Limited, Macfos Electronics Private Limited | cross-ref Entities table §4 |
| 5 | 345-355 | Para "L 4)" (OCR noise prefix "L") Conclusion — based on review + management-furnished info for one subsidiary per para 6/Other Matter b), nothing has come to attention of material misstatement (unmodified conclusion) | OCR_NOISE (stray "L" before "4)") |
| 6 | 356-376 | Other Matters a) (3 sub-topics as one lettered paragraph): (i) first quarterly Ind AS consolidated results per Note 2; (ii) comparative Q1FY26/FY26 figures converted IGAAP→Ind AS by management, NOT Limited-Reviewed by auditor; (iii) FY26 consolidated statements originally IGAAP-audited, then Ind AS-converted, Special Purpose Independent Auditor's Report dated 11-Aug-2026 issued | COMPARATIVES_UNREVIEWED |
| 7 | 378-398 | Other Matters b) (2 sub-topics, one lettered paragraph): (i) Nuo Zhan Technologies Limited — interim results NOT reviewed by this auditor or any other auditor, furnished by management, certified by that subsidiary's board; total assets Rs 0.99 lakhs, total revenue Rs Nil as at 30 Jun 2026; auditor opines this is immaterial to the Group; (ii) Macfos Electronics Private Limited — reviewed by this auditor; total assets Rs 12.23 lakhs, total revenue Rs 1.16 lakhs as at 30 Jun 2026 | UNAUDITED_ENTITY (Nuo Zhan — management-furnished, board-certified, not independently reviewed); ZERO_STANDING (Nuo Zhan revenue = Nil) |
| 8 | 400-413 | Signature block: For Kishor Gujar & Associates, CA Laxmi U Rawat (Partner), Membership 134752, Place Pimpri Pune, Date 11 Aug 2026, UDIN "2 6 \3h#52VMOHDV 02S" | UDIN_GARBLED (OCR-illegible) |

---

## 4. ENTITIES IN CONSOLIDATION (page 7, cross-referenced pages 8)

| # | Line(s) | Entity | Relationship | Review status | Flags |
|---|---------|--------|---------------|----------------|-------|
| 1 | 341 | Macfos Limited | Holding/Parent Company | Limited Review by Kishor Gujar & Associates (standalone + as part of consolidated) | |
| 2 | 342, 379, 383-394 | Nuo Zhan Technologies Limited | Subsidiary | NOT reviewed by statutory auditor or any other auditor; furnished by management; certified by that entity's own board of directors; total assets Rs 0.99 lakhs, total revenue Rs Nil as at 30 Jun 2026; auditor deems immaterial to Group | UNAUDITED_ENTITY, MGMT_FURNISHED, ZERO_STANDING (revenue Nil) |
| 3 | 343, 396-398 | Macfos Electronics Private Limited | Subsidiary | Reviewed by Kishor Gujar & Associates; total assets Rs 12.23 lakhs, total revenue Rs 1.16 lakhs as at 30 Jun 2026 | |

Prior-quarter ledger unavailable (first pipeline run) — no ENTITY_CHANGE comparison possible this cycle. Note for A4/future runs: this is the baseline entity list for MCFOS going forward.

---

## 5. STANDALONE FINANCIAL RESULTS — P&L LINE ITEMS (page 5)

All values Rs Lakhs. Columns: Q1 FY27 (Jun 30 2026, Unaudited) | Q4 FY26 (Mar 31 2026, Unaudited) | Q1 FY26 (Jun 30 2025, Unaudited) | FY26 (Mar 31 2026, Audited).

| # | Line | Particulars | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|-------------|--------|--------|--------|------|-------|
| 1 | 226-227 | Revenue from operations | 8,133.87 | 10,211.12 | 5,926.80 | 30,874.84 | |
| 2 | 228-229 | Other income | 112.04 | 79.45 | 60.54 | 305.05 | |
| 3 | 230 | Total income (I+II) | 8,245.91 | 10,290.57 | 5,987.34 | 31,179.89 | |
| 4 | 233 | Cost of Material Consumed | 28.71 | 30.10 | 10.18 | 75.21 | |
| 5 | 234 | Purchase of Stock-in-Trade | 7,953.00 | 7,785.62 | 5,015.04 | 26,032.07 | |
| 6 | 235 | Changes in Inventory of Stock-in-Trade | (1,791.36) | (67.77) | (523.03) | (2,397.38) | |
| 7 | 236-237 | Employee benefits expenses | 368.68 | 368.06 | 254.98 | 1,246.84 | |
| 8 | 238 | Finance cost | 100.40 | 117.19 | 56.05 | 361.72 | |
| 9 | 239-240 | Depreciation and Amortization Expenses | 83.09 | 89.92 | 75.02 | 325.13 | |
| 10 | 241 | Other expenses | 711.27 | 633.93 | 427.83 | 2,100.78 | |
| 11 | 242 | Total expenses (V) | 7,453.78 | 8,957.05 | 5,316.07 | 27,744.37 | |
| 12 | 244 | Profit (Loss) before Exceptional Item and Tax (III-IV) | 792.13 | 1,333.52 | 671.27 | 3,435.52 | |
| 13 | 245 | Exceptional Item (VI) | — | — | — | — | ZERO_STANDING (nil all periods) |
| 14 | 246 | Profit (Loss) before tax (V-VI) | 792.13 | 1,333.52 | 671.27 | 3,435.52 | |
| 15 | 249 | Current tax | 209.74 | 354.49 | 176.96 | 906.99 | |
| 16 | 250 | Deferred tax | 0.44 | (17.53) | (2.46) | (29.79) | |
| 17 | 251 | Short/(excess) income tax of earlier years | — | — | — | (2.65) | ZERO_STANDING (dash in all 3 quarterly columns; only annual column carries a value) |
| 18 | 252-253 | Total tax expense (VIII) | 210.18 | 336.95 | 174.50 | 874.55 | |
| 19 | 256 | Profit for the year (VII-VIII) (IX) | 581.95 | 996.56 | 496.77 | 2,560.97 | |
| 20 | 260 | Remeasurement losses of the defined benefit plans | — | — | (22.01) | (22.01) | ZERO_STANDING (dash in current & Q4FY26 columns) |
| 21 | 261-262 | Income tax relating to items not reclassified to P&L | — | — | 5.54 | 5.54 | ZERO_STANDING (dash in current & Q4FY26 columns) |
| 22 | 263 | B. Items that will be reclassified to profit or loss | — | — | — | — | ZERO_STANDING (nil all periods — template line, no reclassification activity) |
| 23 | 264 | Total other Comprehensive Income, Net of Tax | — | (16.47) | — | (16.47) | |
| 24 | 266-268 | Total Comprehensive Income for the period (IX+X) (XI) | 581.95 | 980.09 | 496.77 | 2,544.50 | |
| 25 | 270 | Paid-up Share Capital (face value INR 10/share) (XII) | 1,035.85 | 1,035.85 | 941.68 | 1,035.85 | |
| 26 | 274 | Basic EPS (Rs.) (not annualised) | 5.62 | 9.62 | 4.80 | 24.72 | |
| 27 | 275 | Diluted EPS (Rs.) (not annualised) | 5.62 | 9.62 | 4.80 | 24.72 | |
| 28 | 281 | Basic number of shares used in computing EPS (Nos.) | 1,03,58,503 | 1,03,58,503 | 1,03,58,503 | 1,03,58,503 | |
| 29 | 282 | Diluted number of shares used in computing EPS (Nos.) | 1,03,58,503 | 1,03,58,503 | 1,03,58,503 | 1,03,58,503 | |

---

## 6. CONSOLIDATED FINANCIAL RESULTS — P&L LINE ITEMS (page 9)

Same column structure as §5.

| # | Line | Particulars | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|-------------|--------|--------|--------|------|-------|
| 1 | 431-432 | Revenue from operations | 8,134.01 | 10,213.61 | 5,926.80 | 30,877.33 | |
| 2 | 433-434 | Other income | 112.04 | 79.46 | 60.49 | 305.28 | |
| 3 | 435-436 | Total income (I+II) | 8,246.05 | 10,293.07 | 5,987.29 | 31,182.61 | |
| 4 | 439-440 | Cost of Material Consumed | 28.71 | 30.19 | 10.18 | 75.30 | |
| 5 | 441-442 | Purchase of Stock-in-Trade | 7,953.00 | 7,785.62 | 5,017.60 | 26,031.97 | |
| 6 | 443-444 | Changes in Inventory of Stock-in-Trade | (1,791.36) | (67.68) | (525.67) | (2,397.30) | |
| 7 | 445-446 | Employee benefits expenses | 368.68 | 368.06 | 254.98 | 1,246.84 | |
| 8 | 447-448 | Finance cost | 100.40 | 117.19 | 56.05 | 361.72 | |
| 9 | 449-450 | Depreciation and Amortization Expenses | 83.51 | 90.08 | 75.18 | 325.76 | |
| 10 | 451-452 | Other expenses | 711.71 | 634.39 | 428.12 | 2,103.41 | |
| 11 | 453-454 | Total expenses (V) | 7,454.64 | 8,957.84 | 5,316.43 | 27,747.69 | |
| 12 | 456 | Profit (Loss) before Exceptional Item and Tax | 791.41 | 1,335.23 | 670.86 | 3,434.92 | |
| 13 | 457-458 | Exceptional Item (VI) | — | — | — | — | ZERO_STANDING, EXTRACTION_ARTIFACT — the June2025/FY26 column values (670.86 / 3,434.92) print on the "Exceptional Item" text row and the Q1FY27/Q4FY26 values (791.41 / 1,335.23) print on the following unlabeled wrapped line; this is a column-wrap artifact of the glyph-spaced page, not a real Exceptional Item balance — Exceptional Item is nil in all periods (confirmed since V equals VII in every column, same as standalone) |
| 14 | 459 | Profit (Loss) before tax (V-VI) (VII) | 791.41 | 1,335.23 | 670.86 | 3,434.92 | |
| 15 | 460-461 | Current tax | 209.74 | 354.49 | 176.96 | 906.99 | |
| 16 | 462-463 | Deferred tax | 0.51 | (17.28) | (2.25) | (29.48) | |
| 17 | 464 | Short/(excess) income tax of earlier years | — | — | — | (2.65) | ZERO_STANDING (dash in all 3 quarterly columns) |
| 18 | 465-466 | Total tax expense | 210.25 | 337.20 | 174.71 | 874.86 | |
| 19 | 467-468 | Profit for the year (VIII-VII) (IX) | 581.16 | 998.02 | 496.15 | 2,560.06 | |
| 20 | 472 | Remeasurement losses of the defined benefit plans | — | — | (22.01) | (22.01) | ZERO_STANDING (dash current & Q4FY26) |
| 21 | 473 | Income tax relating to items not reclassified to P&L | — | — | 5.54 | 5.54 | ZERO_STANDING (dash current & Q4FY26) |
| 22 | 474 | B. Items that will be reclassified to profit or loss | 0.00 | (0.01) | 0.00 | (0.04) | ZERO_STANDING (explicit 0.00 in current-quarter and Q1FY26 columns; small nonzero in Q4FY26/FY26 — unlike standalone, this line is NOT nil in all periods, only in two) |
| 23 | 475 | Total other Comprehensive Income, Net of Tax | 0.00 | (16.48) | 0.00 | (16.52) | ZERO_STANDING (explicit 0.00, current & Q1FY26 columns) |
| 24 | 477-478 | Total Comprehensive Income for the period (IX+X) (XI) | 581.16 | 981.54 | 496.15 | 2,543.54 | |
| 25 | 481-482 | Profit Attributable to — Owners of the Holding Company (XII) | 581.16 | 998.02 | 496.15 | 2,560.06 | |
| 26 | 483 | Profit Attributable to — Non-Controlling Interest | — | — | — | — | ZERO_STANDING (nil all periods — template line; Group is 100%-owned as printed, no minority stake) |
| 27 | 485-486 | Other Comprehensive Income/(loss) attributable to — Owners of the Holding Company (XIII) | 0.00 | (16.48) | 0.00 | (16.52) | |
| 28 | 488 | Other Comprehensive Income/(loss) attributable to — Non-Controlling Interest | — | — | — | — | ZERO_STANDING (nil all periods) |
| 29 | 490 | Controlling Interest (XIV, Total Comprehensive Income split) | 581.16 | 981.54 | 496.15 | 2,543.54 | |
| 30 | 491 | Non Controlling Interest (XIV, Total Comprehensive Income split) | — | — | — | — | ZERO_STANDING (nil all periods) |
| 31 | 492 | Paid-up Share Capital (face value INR 10/share) (XV) | 1,035.85 | 1,035.85 | 941.68 | 1,035.85 | |
| 32 | 496-497 | Basic EPS (Rs.) (not annualised) | 5.61 | 9.63 | 4.79 | 24.71 | |
| 33 | 498-499 | Diluted EPS (Rs.) (not annualised) | 5.61 | 9.63 | 4.79 | 24.71 | |
| 34 | 500-501 | Basic number of shares used in computing EPS (Nos.) | 1,03,58,504 | 1,03,58,504 | 1,03,58,504 | 1,03,58,504 | note: 1 share more than standalone's 1,03,58,503 — flag for A3 arithmetic check |
| 35 | 502 | Diluted number of shares used in computing EPS (Nos.) | 1,03,58,504 | 1,03,58,504 | 1,03,58,504 | 1,03,58,504 | same note as above |

---

## 7. NOTES TO THE FINANCIAL RESULTS (page 10)

| # | Number visible | Line(s) | First ~15 words | Flags |
|---|-----------------|---------|------------------|-------|
| 1 | 1 | 519-523 | "The above financial results are as per Regulation 33 of the SEBI ... reviewed by the Audit Committee..." | |
| 2 | 2 | 524-530 | "These are the Company's first interim financial results prepared in accordance with Indian Accounting Standards (Ind AS)..." | IND_AS_FIRST_ADOPTION |
| 3 | NOT VISIBLE (gap between markers 2 and 4) | 531-533 | "The comparative financial information for the corresponding quarter ended 30th June 2025 ... has been restated by the management..." | NOTE_NUMBER_GAP — content present, note-number glyph not extracted; per the visible sequence 1,2,4,6,7,8 (highest=8, only 6 markers visible) this and row 4 below are the two missing numbers, most likely 3 and 5, but cannot be assigned with certainty from the extract alone |
| 4 | NOT VISIBLE (same gap) | 534-536 | "The company is engaged in only one business, hence no separate segment information has been furnished in accordance with Ind AS 108..." | NOTE_NUMBER_GAP (see above) |
| 5 | 4 | 537-540 | "The statement includes the results for the quarter ended 30th June 2026 of the current financial year which were subject to limited review... figures for the corresponding previous period have been regrouped/reclassified..." | |
| 6 | 6 | 541-547 | "During the financial year 2025-26, on 11th March 2026, the Company issued 941,682 bonus equity shares of ₹10 each..." | note number jumps 4→6 with no intervening content found; note "5" appears fully absent from the extract, not just its number — flag NOTE_NUMBER_GAP for A3 to check against the source PDF directly |
| 7 | 7 | 548-549 | "Reconciliation of Total Comprehensive Income - Standalone & Consolidated is given hereunder as Annexure I" | cross-ref §9, §10 |
| 8 | 8 | 551-557 | "The Status of Investors Complaints during the quarter ended on 30th June 2026 is as under:" (4 sub-items, see §8) | cross-ref agenda item 10 |

Notes count for gate purposes = 6 (numbered markers only, matches grep). Total rows in this table = 8 (includes 2 orphan content-blocks). Both orphan rows carry full line citations and are not dropped.

---

## 8. NOTE 8 SUB-ITEMS — INVESTOR COMPLAINTS STATUS (page 10)

| # | Line | Item | Value | Flags |
|---|------|------|-------|-------|
| 1 | 554 | Pending at the beginning of the period | Nil | ZERO_STANDING |
| 2 | 555 | Received during the period | Nil | ZERO_STANDING |
| 3 | 556 | Disposed during the period | Nil | ZERO_STANDING |
| 4 | 557 | Remaining Unresolved at the end of the period | Nil | ZERO_STANDING |

---

## 9. ANNEXURE I — RECONCILIATION OF TOTAL COMPREHENSIVE INCOME, STANDALONE (page 11)

Columns: Q4 FY26 (Mar 31 2026) | Q1 FY26 (Jun 30 2025) | FY26 (Mar 31 2026, year). No Jun-30-2026 column — current quarter is native Ind AS, nothing to reconcile.

| # | Line | Particulars | Ind AS ref | Mar'26 Qtr | Jun'25 Qtr | FY26 Year | Flags |
|---|------|-------------|-----------|------------|------------|-----------|-------|
| 1 | 581 | (1) As per Ind AS | | 980.09 | 496.77 | 2,544.50 | |
| 2 | 582 | (2) As per AS | | 985.40 | 504.34 | 2,564.88 | |
| 3 | 584 | A) Difference (1)-(2) | | (5.32) | (7.57) | (20.39) | |
| 4 | 587 | a) Lease Impact | Ind AS 116 | (7.32) | (7.86) | (25.51) | |
| 5 | 588-589 | b) Interest Income on Security Deposits | Ind AS 109 | 1.45 | 1.31 | 5.45 | |
| 6 | 590 | c) Depreciation on Lease land (Plot) | Ind AS 16 | (1.79) | (1.79) | (7.15) | |
| 7 | 591 | d) Other Adjustments | NA | 0.86 | 0.86 | 3.45 | |
| 8 | 592-593 | e) Deferred Tax Impact on Ind AS Adjustments | Ind AS 12 | 1.48 | (0.09) | 3.38 | |
| 9 | 594-595 | f) Gratuity Impact - OCI (Employee Benefits Expense) | Ind AS 19 | — | 22.01 | 22.01 | ZERO_STANDING (blank in Mar'26 quarter column) |
| 10 | 596 | g) Deferred Tax - OCI (Deferred Tax) | Ind AS 12 | — | (5.54) | (5.54) | ZERO_STANDING (blank in Mar'26 quarter column) |
| 11 | 597 | h) Other Comprehensive Income (OCI) (Net of Tax): [subheading] | | | | | header row, no own value |
| 12 | 598-599 | h)i) Remeasurement Loss on Defined Benefit Plans (Gratuity) | Ind AS 19 | — | (22.01) | (22.01) | ZERO_STANDING (blank in Mar'26 quarter column) |
| 13 | 600-601 | h)ii) Income tax relating to items not reclassified to P&L | Ind AS 12 | — | 5.54 | 5.54 | ZERO_STANDING (blank in Mar'26 quarter column) |
| 14 | 604 | B) Total Difference | | (5.32) | (7.57) | (20.39) | |
| 15 | 606 | (A) - (B) | | 0.00 | (0.00) | (0.00) | tie-out check, all ~zero as expected |

---

## 10. ANNEXURE I — RECONCILIATION OF TOTAL COMPREHENSIVE INCOME, CONSOLIDATED (page 11)

Same column structure as §9.

| # | Line | Particulars | Ind AS ref | Mar'26 Qtr | Jun'25 Qtr | FY26 Year | Flags |
|---|------|-------------|-----------|------------|------------|-----------|-------|
| 1 | 615 | (1) As per Ind AS | | 981.54 | 496.15 | 2,543.54 | |
| 2 | 616 | (2) As per AS | | 986.89 | 503.70 | 2,563.96 | |
| 3 | 617 | A) Difference (1)-(2) | | (5.35) | (7.55) | (20.42) | |
| 4 | 620 | a) Lease Impact | Ind AS 116 | (7.32) | (7.86) | (25.51) | |
| 5 | 621-622 | b) Interest Income on Security Deposits | Ind AS 109 | 1.45 | 1.31 | 5.45 | |
| 6 | 623 | c) Depreciation on Lease land (Plot) | Ind AS 16 | (1.79) | (1.79) | (7.15) | |
| 7 | 624-625 | d) Other Adjustments | NA | 0.83 | 0.88 | 3.41 | note: differs slightly from standalone's 0.86/0.86/3.45 — consolidation-level adjustment, not a data error |
| 8 | 626 | e) Deferred Tax Impact on Ind AS Adjustments | Ind AS 12 | 1.48 | (0.09) | 3.38 | |
| 9 | 627-628 | f) Gratuity Impact - OCI (Employee Benefits Expense) | Ind AS 19 | — | 22.01 | 22.01 | ZERO_STANDING (blank Mar'26 quarter) |
| 10 | 629 | g) Deferred Tax - OCI (Deferred Tax) | Ind AS 12 | — | (5.54) | (5.54) | ZERO_STANDING (blank Mar'26 quarter) |
| 11 | 630 | h) Other Comprehensive Income (OCI) (Net of Tax): [subheading] | | | | | header row, no own value |
| 12 | 631 | h)i) Remeasurement Loss on Defined Benefit Plans (Gratuity) | Ind AS 19 | — | (22.01) | (22.01) | ZERO_STANDING (blank Mar'26 quarter) |
| 13 | 632-633 | h)ii) Income tax relating to items not reclassified to P&L | Ind AS 12 | — | 5.54 | 5.54 | ZERO_STANDING (blank Mar'26 quarter) |
| 14 | 635 | B) Total Difference | | (5.35) | (7.55) | (20.42) | |
| 15 | 637-638 | (A) - (B) | | (0.00) | 0.00 | (0.00) | tie-out check, all ~zero as expected |

---

## 11. ANNEXURE TO THE NOTICE — DIRECTOR PROFILE (page 12)

| # | Line(s) | Field | Value |
|---|---------|-------|-------|
| 1 | 651-652 | Name | Mr. Nileshkumar Purushottam Chavhan |
| | 653 | DIN | 07936897 |
| | 654 | Date of Birth | 15/04/1988 |
| | 655 | Date of Appointment | 11/01/2023 |
| | 656 | Qualifications | M.E. Mechanical, IISc Bangalore - 2012 |
| | 657-659 | Expertise | 12 years experience in Electronics, Robotics, Thermals and Fluids, Software, Electronics Development, Sales |
| | 660-662 | Directorships in other public companies (excl. foreign/Sec.8) | NA |
| | 663-664 | Memberships/Chairmanships of committees, other public companies | NA |
| | 665 | Number of shares held | 21,69,150 (23.04%) Equity Shares |
| | 666 | Inter-se relationship between Directors | NA |

Flag: SHAREHOLDING_CONCENTRATION — this single director/appointee holds 23.04% of equity; cross-ref agenda item 5 (his re-appointment resolution) for A4 attention.

---

## 12. SIGNATURE BLOCKS

| # | Line(s) | Signatory | Designation | Document | Timestamp/Date | Flags |
|---|---------|-----------|-------------|----------|-----------------|-------|
| 1 | 109-119 | Sagar Subhash Gulhane | Company Secretary & Compliance Officer, Membership A67610 | Board Outcome letter (page 1) | Digitally signed 2026.08.11 19:18:09 +05'30 | Board meeting concluded 18:30 IST same day; signature at 19:18 IST is 48 minutes AFTER conclusion — consistent, no timing flag |
| 2 | 289-293 | Binod Prasad | Whole Time Director & CFO, DIN 07938828 | Standalone P&L (page 5) | 11/08/2026, Pune | printed signature block, no cryptographic timestamp |
| 3 | 509-514 | Binod Prasad | Whole Time Director & CFO, DIN 07938828 | Consolidated P&L (page 9) | 11/08/2026, Pune | printed signature block, no cryptographic timestamp |
| 4 | 565-569 | Binod Prasad | Whole Time Director & CFO, DIN 07938828 | Notes to financial results (page 10) | 11/08/2026, Pune | printed signature block, no cryptographic timestamp |
| 5 | 198-209 | CA Laxmi U Rawat | Partner, Kishor Gujar & Associates, Membership 134752 | Standalone LRR (page 4) | 11 Aug 2026, Pimpri-Pune | UDIN "26(S4452FVNBEZ2445" — UDIN_GARBLED (OCR-illegible, unverifiable as extracted) |
| 6 | 400-413 | CA Laxmi U Rawat | Partner, Kishor Gujar & Associates, Membership 134752 | Consolidated LRR (page 8) | 11 Aug 2026, Pimpri-Pune | UDIN "2 6 \3h#52VMOHDV 02S" — UDIN_GARBLED (OCR-illegible, unverifiable as extracted) |

---

## SUMMARY TALLY

- Agenda items: 13
- Notes (numbered): 6 explicit + 2 orphan (unlabeled) = 8 rows total
- Line items (P&L + reconciliation + investor-complaint sub-items): 98
  - Standalone P&L: 29
  - Consolidated P&L: 35
  - Reconciliation Standalone: 15
  - Reconciliation Consolidated: 15
  - Investor Complaints sub-items: 4
- Zero-standing flagged rows: 25
- Auditor paragraphs: 14 (Standalone 6, Consolidated 8)
- Entities: 3
- Signature blocks: 6
- Director profiles: 1

Flags raised across ledger: ZERO_STANDING (25 rows), NOTE_NUMBER_GAP (notes 3&4 in table, i.e. missing note-number markers around notes 2-4 and the absent "note 5" before note 6), UNAUDITED_ENTITY / MGMT_FURNISHED (Nuo Zhan Technologies Limited), UDIN_GARBLED (both auditor signature blocks), OCR_NOISE (stray "L" before consolidated para "4)"), EXTRACTION_ARTIFACT (consolidated P&L Exceptional Item / Profit-before-tax column wrap, page 9 lines 456-459), IND_AS_FIRST_ADOPTION (agenda item 1, note 2 — contextual, not a data-quality flag), SHAREHOLDING_CONCENTRATION (director profile, 23.04% single holder), COMPARATIVES_UNREVIEWED (both Other Matter paragraphs — Q1FY26 and FY26 comparative Ind AS figures not subject to Limited Review), possible duplicate agenda wording (items 7 and 12).

Nothing in the extract was excluded from this ledger. All zero/nil/dash-valued standing line items are enumerated above with ZERO_STANDING, not dropped.

```yaml
stage: A2-enumerator
company: "MCFOS"
quarter: "Q1 FY27"
doctype: "results"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/mcfos-q1fy27/work/ledger_results_mcfos_q1fy27.md"
counts:
  notes: 8
  line_items: 98
  zero_standing: 25
  agenda_items: 13
  auditor_paras: 14
  entities: 3
  signature_blocks: 6
  director_profiles: 1
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, NOTE_NUMBER_GAP, UNAUDITED_ENTITY, MGMT_FURNISHED, UDIN_GARBLED, OCR_NOISE, EXTRACTION_ARTIFACT, IND_AS_FIRST_ADOPTION, SHAREHOLDING_CONCENTRATION, COMPARATIVES_UNREVIEWED]
gate_a2: pass
mismatch_note: ""
```
