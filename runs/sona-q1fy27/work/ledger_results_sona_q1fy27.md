# A2 ENUMERATION LEDGER — SONACOMS Q1 FY27 — RESULTS FILING
Source: `extract_results_sona_q1fy27.txt` (results_sona_q1fy27.pdf, 10 pages, Reg 33 Board Outcome +
Standalone financials + Consolidated financials; unit = Rs Millions, x0.1 to Cr)
Prior-quarter ledger: NONE (first quarterly-pipeline run for SONACOMS) — no ENTITY_CHANGE /
DROPPED_SLIDE style diff is possible this run; all "new" items are flagged NEW_ENTITY /
FIRST_RUN_BASELINE instead.

```
=== A2 COUNT TEST ===
category: notes            grep_count: 14   sweep_count: 14   match: yes
category: line_items       grep_count: 65   sweep_count: 65   match: yes
category: zero_standing    grep_count: 8    sweep_count: 8    match: yes
category: agenda_items     grep_count: 1    sweep_count: 1    match: yes
category: auditor_paras    grep_count: 9    sweep_count: 9    match: yes
category: entities         grep_count: 17   sweep_count: 17   match: yes
category: signature_blocks grep_count: 5    sweep_count: 5    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

### Count-test methodology note (read before the tables)
The extract is OCR'd from a scanned/re-flowed PDF and numerals are corrupted in six of the
fourteen note headers (see NOTES table). A naive mechanical grep therefore undercounts on the
first pass and must be widened with content anchors before it can be trusted as the "grep" leg
of GATE A2. Both passes are shown so the reconciliation is auditable, not asserted.

- **notes**: naive `grep -n -E "^\s*[0-9]+[.\s]"` on the whole file returns only 8 hits (note 2 and
  4 standalone at lines 244, 262; notes 2,3,4,5,6,7 consolidated at lines 542, 545, 563, 571, 581,
  583) because standalone notes 1, 3, 5, 6, 7 have OCR-dropped or garbled leading numerals (note 6
  standalone renders as `(,` at line 280; note 7 standalone renders as `x` at line 284; notes 1, 3,
  5 have no numeral captured at all). A second grep pass anchored on note-body content
  (`Notes:` / `completed acquisition` / `Exceptional Items` / `[Pp]ursuant to:` / `DENSO` /
  `Annual General Meeting held on July 15` / `reportable business segment`) returns exactly 2 hits
  per anchor (7 anchors x 2 statements = 14), which is confirmed against the manual sweep. Re-grep,
  not re-sweep, closed this one — documented per Gate A2's re-sweep-on-mismatch instruction.
- **line_items**: a decimal-value grep (`[0-9]+\.[0-9]{2}`) over the standalone P&L block returns
  28 (misses "Total reserves", which is blank in literally every column, standalone, i.e. the
  canonical zero-standing template row that never prints a number at all) and over the
  consolidated P&L block returns 36 (consolidated "Total reserves" does carry the FY26 annual
  figure, so it prints and is caught). Adding the one label-only blank row
  (`grep -n -E "^Total reserves\s*$"` -> line 220, standalone) brings the reconciled grep total to
  65, matching the manual sweep of 29 (standalone) + 36 (consolidated).
- **agenda_items / auditor_paras / entities**: clean on first pass, no OCR corruption encountered.

---

## 1. BOARD OUTCOME LETTER — AGENDA ITEMS (page 1, lines 14-60)

| # | Line | Item | Detail | Flags |
|---|------|------|--------|-------|
| 1 | 28-31 | Approval of Q1 FY27 unaudited financial results (Standalone AND Consolidated), bundled as a single resolution | "considered and approved the Unaudited Financial Results (Standalone and Consolidated) of the Company for the quarter ended 30th June, 2026" | — |

**No other agenda items disclosed** — no AR approval, no AGM notice, no record date, no dividend
declaration (dividend was an AGM item on a separate date, see Note 6), no director
appointment/resignation, no auditor change, no scrutinizer appointment, no ESOP-committee board
resolution (the ESOP grant in Note 4 was by the NRC, not the Board, and not on this letter), no
capital-raising enabling resolution. Enumerated as absent, not dropped.

**Board meeting timing** (line 43-44): commenced 2:15 p.m. IST, concluded 4:03 p.m. IST — duration
1h48m. Not a rubber-stamp short meeting.

**Signature block 1 (letter)**: Pankaj Gupta, SVP (Legal), Company Secretary & Compliance Officer,
digitally signed, timestamp 2026.07.23 16:08:22 (line 51-58) — 5 minutes AFTER board conclusion
(16:03). Expected sequencing.

---

## 2. AUDITOR REPORTS — PARAGRAPH-BY-PARAGRAPH (both entities)

### 2A. Standalone limited review report (Walker Chandiok & Co LLP, pages 2-3, lines 78-156)

| Para | Line | Content | Flags |
|------|------|---------|-------|
| 1 | 85-90 | Scope statement: reviewed standalone unaudited results for quarter/YTD ended 30 Jun 2026 | — |
| 2 | 92-98 | Management responsibility; prepared per Ind AS 34 / Reg 33 | — |
| 3 | 100-108 | Review conducted per SRE 2410; review is less in scope than audit; no audit opinion expressed | — |
| 4 (conclusion) | 125-131 | Unmodified conclusion — nothing came to attention indicating non-disclosure or material misstatement | — |
| Emphasis of Matter | — | NONE present | ZERO_STANDING (qualitative) |
| Other Matters | — | NONE present (single entity, no other-auditor reliance) | ZERO_STANDING (qualitative) |
| Going Concern | — | NONE present | ZERO_STANDING (qualitative) |
| Entity reviewed | 83-90 | Sona BLW Precision Forgings Limited only | — |
| UDIN | 152 | 26517273YBOMPO5482 | — |
| Signatory | 140-155 | Arun Tandon, Partner, Walker Chandiok & Co LLP, Membership No. 517273, digitally signed **2026.07.23 14:40:58** | **AUDITOR_SIGNED_BEFORE_BOARD_CONCLUSION** — signed at 14:40:58, mid-meeting (board ran 14:15-16:03); auditor sign-off pre-dates board's own approval timestamp by ~83 minutes |

### 2B. Consolidated limited review report (Walker Chandiok & Co LLP, pages 6-8, lines 311-452)

| Para | Line | Content | Flags |
|------|------|---------|-------|
| 1 | 317-324 | Scope statement: reviewed consolidated results, Holding Co + subsidiaries (Group), refers to Annexure 1 for entity list | — |
| 2 | 326-333 | Management responsibility; Ind AS 34 / Reg 33 | — |
| 3 | 335-343 | Review conducted per SRE 2410; less scope than audit; no audit opinion expressed | — |
| 3-addendum (unnumbered) | 345-346 | "We also performed procedures in accordance with the circular issued by SEBI under Regulation 33(8)" — appended to para 3 without its own numeral | — |
| 4 (conclusion) | 363-370 | Unmodified conclusion, subject to reliance on other auditor per para 5 | — |
| 5 (Other Matters) | 372-389 | Did NOT review 5 subsidiaries (revenue Rs 178.61mn, net loss Rs 29.75mn, total comprehensive loss Rs 29.27mn for the quarter); reviewed by another auditor per ISRE 2410 in their home jurisdiction, all located outside India, review furnished by management; conclusion not modified re: reliance | **OTHER_AUDITOR_RELIANCE** — 5 of 16 subsidiaries unreviewed by primary auditor; extract does not name which 5 |
| Going Concern | — | NONE present | ZERO_STANDING (qualitative) |
| Entity reviewed | 317-320 | Holding Co + subsidiaries per Annexure 1 (17 entities total, see Section 5) | — |
| UDIN | 406 | 26517273VYZZJC2363 | — |
| Signatory | 393-409 | Arun Tandon, Partner, Membership No. 517273, digitally signed **2026.07.23 14:11:24** | **AUDITOR_SIGNED_BEFORE_BOARD_START** — signed at 14:11:24, i.e. 4 minutes BEFORE the board meeting even commenced (14:15); the more material of the two reports (consolidated) was signed off earliest of all three signature events in the filing |

**auditor_paras count**: 4 (standalone: paras 1,2,3,4) + 5 (consolidated: paras 1,2,3,4,5) = **9**.

---

## 3. STANDALONE P&L — LINE ITEMS (page 4, lines 162-226)

Columns: Q1 FY27 (Jun-26, unaudited) | Q4 FY26 (Mar-26, unaudited, balancing figure) | Q1 FY26
(Jun-25, unaudited) | FY26 (Mar-26, audited, full year)

| # | Line | Line item | Q1FY27 value | Flags |
|---|------|-----------|--------------|-------|
| 1 | 177 | Revenue from operations | 11,572.38 | — |
| 2 | 178 | Foreign exchange gain (net) | 83.04 | — |
| 3 | 179 | Other income | 817.83 | — |
| 4 | 180 | **Total income** (subtotal) | 12,473.25 | — |
| 5 | 183 | Cost of materials consumed | 6,101.36 | — |
| 6 | 184-186 | Changes in inventories of finished goods and work-in-progress | (321.41) | — |
| 7 | 187 | Employee benefits expense | 1,039.11 | — |
| 8 | 188 | Finance costs | 71.11 | — |
| 9 | 189 | Depreciation and amortisation expense | 693.32 | — |
| 10 | 190 | Other expenses | 2,133.55 | — |
| 11 | 191 | **Total expenses** (subtotal) | 9,717.04 | — |
| 12 | 192 | **Profit before exceptional items and tax** (subtotal) | 2,756.21 | — |
| 13 | 193 | Exceptional items (Refer Note No. 3) | blank/dash | **ZERO_STANDING** — blank Q1FY27 & Q4FY26; populated Q1FY26 (91.74) and FY26 (507.91); real transaction type, just none this quarter |
| 14 | 194 | **Profit before tax** (subtotal) | 2,756.21 | — |
| 15 | 197 | Current tax | 435.30 | — |
| 16 | 198 | Tax related to previous years | blank | **ZERO_STANDING** — blank Q1FY27 & Q1FY26; populated Q4FY26 (9.13) and FY26 (9.13) |
| 17 | 199 | Deferred tax (credit)/charge | 119.85 | — |
| 18 | 200 | **Total tax expense** (subtotal) | 555.15 | — |
| 19 | 202 | **Profit for the period/year** (subtotal) | 2,201.06 | — |
| 20 | 206 | Remeasurements gains/(losses) on defined benefit plans | (0.03) | — |
| 21 | 207 | Income tax relating to above mentioned item (OCI-1) | 0.00 | **ZERO_STANDING** — explicit 0.00 print, Q1FY27 only |
| 22 | 209-210 | Effective portion of gain on designated portion of hedging instruments in a cash flow hedge | 238.42 | — |
| 23 | 212 | Income tax relating to above mentioned items (OCI-2, hedge) | (60.01) | — |
| 24 | 213-215 | **Other comprehensive (loss)/income for the period/year** (subtotal) | 178.38 | — |
| 25 | 216 | **Total comprehensive income for the period/year** (subtotal) | 2,379.44 | — |
| 26 | 218 | Paid up equity share capital (FV Rs 10) | 6,220.35 | — |
| 27 | 220 | Total reserves | blank in ALL 4 columns | **ZERO_STANDING** — no figure in any period shown, standalone-only omission (balance-sheet-type line not disclosed at all in a P&L-only quarterly filing) |
| 28 | 224 | Earnings per share (Basic), Rs | 3.54 | — |
| 29 | 225 | Earnings per share (Diluted), Rs | 3.54 | — |

Section headers enumerated but not counted as line items (no values attach to them): "Income"
(176), "Expenses" (182), "Other comprehensive income" (204), "Items that will not be reclassified
to profit or loss" (205), "Items that will be reclassified to profit or loss" (208).

---

## 4. CONSOLIDATED P&L — LINE ITEMS (page 9, lines 461-521)

Same four columns as standalone.

| # | Line | Line item | Q1FY27 value | Flags |
|---|------|-----------|--------------|-------|
| 1 | 469 | Revenue from operations | 13,012.01 | — |
| 2 | 470 | Foreign exchange (loss)/gain (net) | 91.69 | — |
| 3 | 471 | Other income | 256.96 | — |
| 4 | 472 | **Total income** (subtotal) | 13,360.66 | — |
| 5 | 474 | Cost of materials consumed | 6,798.56 | — |
| 6 | 475 | Changes in inventories of finished goods and work-in-progress | (298.45) | — |
| 7 | 476 | Employee benefits expense | 1,288.42 | — |
| 8 | 477 | Finance costs | 104.77 | — |
| 9 | 478 | Depreciation and amortisation expense | 768.81 | — |
| 10 | 479 | Other expenses | 2,289.13 | — |
| 11 | 480 | **Total expenses** (subtotal) | 10,951.24 | — |
| 12 | 481 | **Profit before exceptional items and tax** (subtotal) | 2,409.42 | — |
| 13 | 482 | Exceptional items (Refer Note No. 3) | blank/dash | **ZERO_STANDING** — blank Q1FY27 & Q4FY26; populated Q1FY26 (91.74) and FY26 (509.81) |
| 14 | 483 | **Profit before tax** (subtotal) | 2,409.42 | — |
| 15 | 485 | Current tax | 512.28 | — |
| 16 | 486 | Tax related to previous years | blank | **ZERO_STANDING** — blank Q1FY27 & Q1FY26; populated Q4FY26 (8.26) and FY26 (8.26) |
| 17 | 487 | Deferred tax (credit)/charge | 112.01 | — |
| 18 | 488 | **Total tax expense** (subtotal) | 624.29 | — |
| 19 | 490 | **Profit for the period/year** (subtotal) | 1,785.13 | — |
| 20 | 494 | Remeasurements gains/(losses) on defined benefit plans | (0.04) | — |
| 21 | 495 | Income tax relating to above mentioned items (OCI-1) | 0.00 | **ZERO_STANDING** — explicit 0.00 print, Q1FY27 only |
| 22 | 498 | Exchange differences on translation of foreign operations | 36.46 | — |
| 23 | 499-501 | Effective portion of gain/(loss) on designated portion of hedging instruments in a cash flow hedge | 238.42 | — |
| 24 | 502 | Income tax relating to above mentioned items (OCI-2, hedge) | (60.01) | — |
| 25 | 503 | **Other comprehensive income for the period/year** (subtotal) | 214.83 | — |
| 26 | 504 | **Total comprehensive income for the period/year** (subtotal) | 1,999.96 | — |
| 27 | 506 | Profit attributable to: a) Owners of the parent | 1,804.68 | — |
| 28 | 507 | Profit attributable to: b) Non-controlling interests | (19.55) | — |
| 29 | 509 | OCI attributable to: a) Owners of the parent | 214.61 | — |
| 30 | 510 | OCI attributable to: b) Non-controlling interests | 0.22 | — |
| 31 | 512 | Total comprehensive income attributable to: a) Owners of the parent | 2,019.29 | — |
| 32 | 513 | Total comprehensive income attributable to: b) Non-controlling interests | (19.33) | — |
| 33 | 514 | Paid up equity share capital (FV Rs 10) | 6,220.35 | — |
| 34 | 515 | Total reserves | blank in 3 quarterly columns; FY26 annual = 53,610.75 | **ZERO_STANDING** — blank for the current (and comparative quarterly) columns; only the audited annual column carries a figure |
| 35 | 519 | Earnings per share (Basic), Rs | 2.90 | — |
| 36 | 520 | Earnings per share (Diluted), Rs | 2.90 | — |

Section headers enumerated but not counted: "Income" (468), "Expenses" (473), "Other
comprehensive income" (492), "Items that will not be reclassified to profit or loss" (493), "Items
that will be reclassified to profit or loss" (497), "Profit attributable to:" (505), "Other
comprehensive income attributable to:" (508), "Total comprehensive income attributable to:" (511).

**line_items total = 29 (standalone) + 36 (consolidated) = 65. zero_standing total = 4 + 4 = 8.**

---

## 5. NOTES — STANDALONE (page 5, lines 235-296) AND CONSOLIDATED (page 10, lines 534-593)

| Note # | Statement | Line | First ~15 words | Flags |
|--------|-----------|------|------------------|-------|
| 1 | Standalone | 235-242 | "The Standalone Unaudited Financial Results ... have been prepared in accordance with the Indian Accounting Standards..." Basis of preparation; Mar-26 quarter is a balancing figure; unmodified auditor report | numeral not captured by OCR (implicit note 1) |
| 1 | Consolidated | 534-540 | Same basis-of-preparation note, consolidated version | numeral not captured by OCR |
| 2 | Standalone | 244-246 | "The Company completed acquisition of the Railway Business of Escorts Kubota Limited on June 01, 2025..." slump sale, consideration Rs 16,426.32mn | — |
| 2 | Consolidated | 542-544 | Same Railway Business acquisition note, consolidated version | — |
| 3 | Standalone | 248-260 | Exceptional Items table: costs re acquisition opportunities, Statutory impact of New Labour Codes, Total — all nil/blank in Q1FY27 & Q4FY26 columns | note numeral not captured by OCR; table itself is the note referenced as "Note No. 3" in the P&L |
| 3 | Consolidated | 545-560 | Same Exceptional Items table, consolidated version, numeral "3" visible | — |
| 4 | Standalone | 262-268 | Pursuant to: a) ESOP Plan 2023 — NRC granted 1,00,000 options 16-Jun-2026 at FMV Rs 596.35; b) Performance Share Plan 2025 — NRC approved allotment of 1,70,747 equity shares to MD & Group CEO | sub-items 4a (ESOP grant) and 4b (PSP allotment) — both distinct disclosure events folded into one numbered note |
| 4 | Consolidated | 563-569 | Same ESOP + Performance Share Plan note, consolidated version | same sub-item structure |
| 5 | Standalone | 270-278 | "On 22nd July 2026, the company (SONA) signed definitive agreements with DENSO Corporation Japan ... to form two Joint Ventures..." 51:49 EV motor JVs, EV of Rs 17,500mn for 49% stake | note numeral not captured by OCR; material subsequent/concurrent event, signed one day before this board meeting and not listed as a separate board-outcome agenda item |
| 5 | Consolidated | 571-579 | Same DENSO JV note, consolidated version, numeral "5" visible | same JV_DISCLOSED_VIA_NOTES_ONLY observation |
| 6 | Standalone | 280-282 | "In the Annual General Meeting held on July 15, 2026, shareholders have approved a final dividend of Rs. 1.80 per equity share..."; also dividend received of Rs 594.63mn from a wholly-owned subsidiary on 19-Jun | numeral OCR-garbled to "(," |
| 6 | Consolidated | 581-582 | Same AGM final dividend note, consolidated version, numeral "6" visible | — |
| 7 | Standalone | 284-286 | "The Company operates in a single reportable business segment viz, 'Mobility components, systems and sub-systems.'" | numeral OCR-garbled to "x" |
| 7 | Consolidated | 583 | "The Group operates in a single reportable business segment..." consolidated version, numeral "7" visible | — |

**notes total = 7 (standalone) + 7 (consolidated) = 14.**

---

## 6. CONSOLIDATION ENTITY LIST — Annexure 1 to consolidated auditor report (page 8, lines 422-447)

No prior-quarter ledger exists for this ticker, so no ENTITY_CHANGE diff is possible this run;
every entity below is the FIRST_RUN_BASELINE for future-quarter diffing.

| # | Line | Entity | Relationship | Flags |
|---|------|--------|--------------|-------|
| 1 | 427 | Sona BLW Precisions Forgings Limited | Holding company | — |
| 2 | 430 | Comstar Automotive Technologies Services Private Limited | Subsidiary | — |
| 3 | 431 | Comstar Automotive USA LLC | Subsidiary | — |
| 4 | 432 | Comstar Automotive Hongkong Limited | Subsidiary | — |
| 5 | 433 | Comestel Automotive Technologies Mexicana Ltd | Subsidiary | — |
| 6 | 434 | Comstar Automotive (Hangzhou) Co., Ltd | Subsidiary | — |
| 7 | 435 | Comenergia Automotive Technologies Mexicana, S. DE R.L. DE C.V | Subsidiary | — |
| 8 | 436 | Comestel Automotive Technologies Mexicana, S. DE R.L. DE C.V | Subsidiary | — |
| 9 | 437 | Comstar Hong Kong Mexico No. 1, LLC | Subsidiary | — |
| 10 | 438 | Sona Comstar eDrive Private Limited | Subsidiary | note: this is the EV Motors/controllers subsidiary referenced in Note 4/5 as the entity 49% of which will be sold to DENSO |
| 11 | 439 | Sona BLW eDrive Mexicana, S.A.P.I. DE C.V. | Subsidiary | — |
| 12 | 440 | Novelic d.o.o. Beograd | Subsidiary | — |
| 13 | 441 | Nirsen SRL | Subsidiary | — |
| 14 | 442 | Novelic ESC DOOEL SKOPJE | Subsidiary | — |
| 15 | 443 | Nirsen D.O.O | Subsidiary | — |
| 16 | 444 | Novelic GMBH | Subsidiary | — |
| 17 | 445-447 | Novelic India Private Limited* (*incorporated 28 Nov 2025) | Subsidiary | **NEW_ENTITY** — most recently incorporated entity in the list, footnoted |

**entities total = 17** (1 holding + 16 subsidiaries).

Auditor report para 5 (Section 2B) states 5 of these 16 subsidiaries are unreviewed by the primary
auditor and located outside India; the extract does not name which 5 — **data limitation, not an
enumeration gap** (nothing to enumerate that isn't in the source).

---

## 7. SIGNATURE / TIMESTAMP BLOCKS (all pages)

| # | Line | Signatory | Designation | Timestamp | Flags |
|---|------|-----------|-------------|-----------|-------|
| 1 | 51-58 | Pankaj Gupta | SVP (Legal), Company Secretary & Compliance Officer | 2026.07.23 16:08:22 | — (5 min after board conclusion 16:03, expected) |
| 2 | 140-155 | Arun Tandon (Walker Chandiok & Co LLP) | Partner, standalone review report | 2026.07.23 14:40:58 | **AUDITOR_SIGNED_BEFORE_BOARD_CONCLUSION** |
| 3 | 397-409 | Arun Tandon (Walker Chandiok & Co LLP) | Partner, consolidated review report | 2026.07.23 14:11:24 | **AUDITOR_SIGNED_BEFORE_BOARD_START** — earliest of all 3 signature timestamps, 4 min before the 14:15 board start |
| 4 | 288-296 | (name/designation not OCR-legible) | Authorized signatory, standalone financial results | not visible in extract | **OCR_GAP** — standalone results signature block did not extract a name; consolidated equivalent (row 5) did |
| 5 | 588-593 | Vivek Vikram Singh (rendered "Viv Vikram Singh" by OCR) | Managing Director and Group Chief Executive Officer, DIN 07698495 | not shown as digitally-signed w/ timestamp in extract | — |

**signature_blocks total = 5.**

Board meeting window for reference: commenced 14:15, concluded 16:03 (line 43-44).

---

## 8. NOT APPLICABLE TO THIS DOCTYPE (results filing, not concall/presentation)

No transcript participants, speaker turns, questions, or spoken management numbers to enumerate
(concall doctype). No slides, slide titles, chart data labels, or footnotes to enumerate
(investor-presentation doctype). No balance sheet or cash-flow statement line items to enumerate
in EITHER statement — this is expected for a Q1 Reg 33 filing (SEBI mandates balance sheet /
cash-flow disclosure only for H1 and full-year filings, not Q1/Q3), not a completeness gap.

---

## 9. EXTRACTION-QUALITY OBSERVATION (not a GATE A2 category, flagged for downstream awareness)

A1 extraction header (line 6) states `line_count: 580`; the file as read is 593 lines
(`wc -l` confirms 593). **EXTRACT_LINE_COUNT_MISMATCH** — 13-line discrepancy between the header's
self-reported count and the actual file. Does not affect this ledger's completeness (every line in
the actual 593-line file was swept), but A3/A4 should know the header metadata is stale.

---

## FLAGS SUMMARY (all instances)

- **ZERO_STANDING** x8 (line items 13, 16, 21, 27 standalone; 13, 16, 21, 34 consolidated)
- **AUDITOR_SIGNED_BEFORE_BOARD_CONCLUSION** x1 (standalone auditor, 14:40:58 vs 16:03 conclusion)
- **AUDITOR_SIGNED_BEFORE_BOARD_START** x1 (consolidated auditor, 14:11:24 vs 14:15 start — the
  more material report signed before the meeting that was to approve it had even convened)
- **OTHER_AUDITOR_RELIANCE** x1 (5 of 16 subsidiaries, unnamed, reviewed by other auditor)
- **NEW_ENTITY** x1 (Novelic India Private Limited, incorporated 28 Nov 2025)
- **OCR_GAP** x2 (standalone results signatory name illegible; 6 of 14 note numerals OCR-corrupted)
- **JV_DISCLOSED_VIA_NOTES_ONLY** x1 (DENSO JV, signed 22-Jul, disclosed only via Note 5, not as
  its own Board Outcome agenda item on the 23-Jul letter)
- **EXTRACT_LINE_COUNT_MISMATCH** x1 (header 580 vs actual 593 lines)
