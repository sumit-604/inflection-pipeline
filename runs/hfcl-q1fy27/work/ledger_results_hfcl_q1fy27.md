# LEDGER — HFCL Q1 FY27 RESULTS FILING (A2 Enumerator)
Source: `extract_results_hfcl_q1fy27.txt` (7 pages, 506 extract lines incl. header)

```
=== A2 COUNT TEST ===
category: agenda_items       grep_count: 2    sweep_count: 2    match: yes
category: notes               grep_count: 7    sweep_count: 7    match: yes
category: line_items_pnl      grep_count: 32   sweep_count: 32   match: yes
category: line_items_segment  grep_count: 26   sweep_count: 26   match: yes
category: line_items_headers  grep_count: 11   sweep_count: 11   match: yes
category: auditor_paras       grep_count: 15   sweep_count: 15   match: yes
category: entities_note4      grep_count: 15   sweep_count: 15   match: yes
category: entities_auditorpar grep_count: 11   sweep_count: 11   match: yes
category: signature_blocks    grep_count: 6    sweep_count: 6    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

## RECONCILIATION NOTES (how initial grep/sweep mismatches were closed)
1. **line_items_pnl**: naive numeric grep (`[0-9]+[,.][0-9]`) found 31 of 32 rows.
   Missing row: line 363 "VI Exceptional items" — ALL columns (standalone AND
   consolidated, all 4 periods each) are dash, so it contains no digit at all
   and is invisible to numeric regex. A supplementary dash-density grep
   (`^\s*[A-Za-z].*-\s+-\s+-\s+-`) recovered it. Manual sweep had already
   caught it on first read. Reconciled count: 32 = 32. This is the canonical
   ZERO_STANDING case for this filing.
2. **line_items_segment**: naive numeric grep found 25 of 26 rows. Missing:
   line 448 "e. Un-allocated" (Segment Assets) — OCR renders the value as
   "887 .13" with a stray space before the decimal point, which the strict
   `[0-9]+[,.][0-9]` pattern does not match. A space-tolerant pattern
   (`[0-9]+\s*[,.]\s*[0-9]`) recovered it. Reconciled: 26 = 26.
3. **auditor_paras**: naive grep on `^\s*[0-9]+\.\s` found only 11 of 15
   (3 standalone + 8 consolidated). Two numbered-paragraph openers are
   OCR-corrupted: standalone para 1 renders as "I ." (line 140, roman-numeral
   misread) and consolidated para 1 renders as "l." (line 199, lowercase-L
   misread); consolidated para 5 opener is buried in scan noise "~~-- 5."
   (line 244). An OCR-tolerant numbering pattern recovered all three
   (13 numbered paragraphs total: 4 standalone + 9 consolidated). Two further
   paragraphs carry NO number at all — line 224 ("We also performed
   procedures...") and line 286 ("Our conclusion...is not modified") — found
   by manual read and confirmed by targeted phrase-grep. Reconciled: 15 = 15.
4. **entities_note4**: naive grep on `^\s*[a-o]\.\s` found 14 of 15 — entity
   "l." (BigCat Wireless, line 489) is OCR-misread as capital "I." An
   OCR-tolerant class recovered it. Reconciled: 15 = 15.
5. **entities_auditorpara4**: naive grep on `^\s*[a-h]\.\s` found 10 of 11 —
   the 9th subsidiary (HFCL B.V. Netherlands, line 238) is OCR-misread as
   "1." instead of "i." (lowercase, roman numeral 9 of the sub-list). An
   OCR-tolerant class recovered it. Reconciled: 11 = 11.

All mismatches were OCR/scan artifacts, not missing disclosures. Gate A2:
**PASS**.

---

## 1. BOARD OUTCOME LETTER — MEETING TIMING & AGENDA ITEMS
Meeting held: July 22, 2026. Commencement 12:00 Noon; conclusion 1:00 P.M.
(lines 31-32) — 60-minute meeting covering a results approval plus a ~₹215
crore capex decision.

| # | Line | Agenda Item | First 15 words | Flags |
|---|------|-------------|-----------------|-------|
| 1 | 44 | Financial Results approval | "Un-audited Financial Results of the Company for the 1st Quarter ended June 30, 2026, of the..." | — |
| 2 | 61 | New manufacturing facility — Data Center Connectivity Products | "Setting up of a state-of-the-art manufacturing facility for Data Center Connectivity Products: The Board has approved..." | MATERIAL_CAPEX |

No other agenda items present in this letter (no AR approval, AGM notice,
record date, dividend, director appointment/resignation, auditor change,
scrutinizer appointment, or ESOP grant items — this is a results-only board
meeting plus one capex resolution). Absence of dividend declaration and of
any director-appointment annexure is noted, not assumed.

### 1a. Item 2 sub-disclosure (Reg 30 / Schedule III snapshot — annexure-style)
| Line(s) | Field | Detail |
|---|---|---|
| 84-88 | Snapshot table (1 data row) | Product: Data Center Connectivity Products; Existing Capacity & Utilization: N.A.; Capacity Addition: 2,70,000 assemblies/annum; Estimated Investment/Capex: ~₹215 crore |
| 90 | (a) Period for capacity addition | Expected commissioning by September 2027 |
| 92 | (b) Mode of financing | Appropriate mix of internal accruals and/or debt financing |
| 94-97 | (c) Strategic Rationale | Capitalize on global demand for next-gen data center connectivity, expand manufacturing, strengthen presence, cater to domestic/international demand |
| 104-106 | Context note | New facility is in addition to existing HTL Limited (subsidiary) facility; will augment consolidated capacity |

No director profiles / DIN / term-date annexures present this quarter (zero
new appointments disclosed) — recorded as absence, not omission.

---

## 2. FINANCIAL STATEMENTS — MAIN P&L TABLE (Standalone & Consolidated), page 6
All values Rs. in Crore. Columns per block: Q1FY27 (Jun-26) | Q4FY26 (Mar-26)
| Q1FY26 (Jun-25) | FY26 (Mar-26 FY). "H" = header/label row (no data).

| Line | Item | Standalone zero/dash? | Consolidated zero/dash? | Flags |
|---|---|---|---|---|
| 337 | I. INCOME (H) | — | — | — |
| 338 | Revenue from Operations | no | no | — |
| 339 | Other Income | no | no | — |
| 340 | Total Income (subtotal) | no | no | — |
| 342 | II. EXPENSES (H) | — | — | — |
| 343 | Cost of materials/services consumed | no | no | — |
| 344 | Purchases of stock-in-trade | no | no | — |
| 345-346 | Change in inventories of FG/WIP/stock-in-trade | no | no | — |
| 347 | Employee benefits expense (Refer Note 4) | no | no | — |
| 348 | Finance costs | no | no | — |
| 349-350 | Depreciation, Impairment and Amortisation | no | no | — |
| 351 | Other expenses | no | no | — |
| 352 | Total Expenses (subtotal) | no | no | — |
| 354-355 | III. Profit/(Loss) before exceptional items and tax (I-II) | no | no | — |
| 357-358 | IV. Share of net profits/(loss) of JCEs (equity method) | **all dash, all periods** | no (has values) | ZERO_STANDING (standalone only — line structurally exists only for consol group accounting) |
| 360-361 | V. Profit/(Loss) before exceptional items and tax (III+IV) | no | no | — |
| 363-364 | VI. Exceptional items | **all dash, all periods** | **all dash, all periods** | ZERO_STANDING (both blocks — canonical template-signal row) |
| 365 | VII. Profit/(Loss) before tax (V-VI) | no | no | — |
| 367 | VIII. Tax expense (H) | — | — | — |
| 368 | Current Tax | no (one period dash: standalone Jun-25, loss quarter) | no | not standing — single-period nil due to loss, not flagged |
| 369 | Deferred Tax/(Benefits) | no | no | — |
| 371-372 | IX. Profit/(Loss) after tax, continuing ops (VII-VIII) | no | no | — |
| 374 | X. Other Comprehensive Income/(Loss) (H) | — | — | — |
| 375 | Items not reclassified to P&L | no | no | — |
| 376 | Income tax on above item | no | no | — |
| 377 | Items that will be reclassified to P&L | no | no | — |
| 378-379 | Other comprehensive income/(loss) for period (subtotal) | no | no | — |
| 382-383 | XI. Total comprehensive income/(Loss) for period (IX+X) | no | no | — |
| 386 | XII. Profit/(Loss) attributable to: (H) | — | — | — |
| 387 | — Owners of the Parent | **all dash, all periods** | no | ZERO_STANDING (standalone — attribution split is a consol-only concept) |
| 388 | — Non-controlling interests | **all dash, all periods** | no | ZERO_STANDING (standalone) |
| 390-391 | XIII. Total comprehensive income attributable to: (H) | — | — | — |
| 392 | — Owners of the Parent | **all dash, all periods** | no | ZERO_STANDING (standalone) |
| 393 | — Non-controlling interests | **all dash, all periods** | no | ZERO_STANDING (standalone) |
| 395-396 | XIV. Paid-up Equity Share Capital (FV Re.1) | no | no | — |
| 398 | XV. Other Equity | **dash in all 3 quarterly cols, value only in FY col** | **dash in all 3 quarterly cols, value only in FY col** | ZERO_STANDING (quarterly columns, both blocks — FY-end-only line by convention) |
| 400-401 | XVI. Earnings/(Loss) per Share (H) | — | — | — |
| 402 | — Basic (Re./Rs.) | no | no | — |
| 403 | — Diluted (Re./Rs.) | no | no | — |

**39 rows** (7 header/label rows + 32 value rows). **7 ZERO_STANDING rows.**

---

## 3. SEGMENT TABLE (Standalone & Consolidated), page 7

| Line | Item | Standalone zero/dash? | Consolidated zero/dash? | Flags |
|---|---|---|---|---|
| 422 | 1. Segment Revenue (H) | — | — | — |
| 423 | a. Telecom Products | no | no | — |
| 424 | b. Defence Product & Services | no | no | — |
| 425 | c. Turnkey Contracts and Services | no | no | — |
| 426 | d. Others | **blank/no cells** | no | ZERO_STANDING (standalone — segment does not exist standalone, consol-only revenue line) |
| 427 | Revenue from Operations (subtotal, ties to line 338) | no | no | — |
| 429-430 | 2. Segment Results — PBT & interest by segment (H) | — | — | — |
| 431 | a. Telecom Products | no | no | — |
| 432 | b. Defence Product & Services | no | no | — |
| 433 | c. Turnkey Contracts and Services | no | no | — |
| 434 | d. Others | **blank** | no | ZERO_STANDING (standalone) |
| 435 | Total (subtotal) | no | no | — |
| 437 | Less: i. Interest | no | no | — |
| 438 | Less: ii. Other un-allocable expenditure net off | no | no | — |
| 439 | Less: iii. Un-allocable income | no | no | — |
| 441 | Total Profit/(Loss) before Tax (ties to line 365) | no | no | — |
| 443 | 3. Segment Assets (H) | — | — | — |
| 444 | a. Telecom Products | no | no | — |
| 445 | b. Defence Product & Services | no | no | — |
| 446 | c. Turnkey Contracts and Services | no | no | — |
| 447 | d. Others | **blank** | no | ZERO_STANDING (standalone) |
| 448 | e. Un-allocated | no (OCR: "887 .13" space artifact) | no | — |
| 449 | Total (subtotal) | no | no | — |
| 451 | 4. Segment Liabilities (H) | — | — | — |
| 452 | a. Telecom Products | no | no | — |
| 453 | b. Defence Product & Services | no | no | — |
| 454 | c. Turnkey Contracts and Services | no | no | — |
| 455 | d. Others | **blank** | no | ZERO_STANDING (standalone) |
| 456 | e. Un-allocated | no | no | — |
| 457 | Total (subtotal) | no | no | — |

**30 rows** (4 header rows + 26 value rows). **4 ZERO_STANDING rows** (all
"d. Others" standalone cells across Revenue/Results/Assets/Liabilities — the
Others segment is disclosed only at consolidated level, standalone has no
such business line).

**Combined financial-table total: 69 rows (11 headers + 58 value rows);
11 ZERO_STANDING flags overall.**

---

## 4. NUMBERED NOTES (financial statement footnotes, page 7 bottom)

| Note | Line(s) | First 15 words | Flags |
|---|---|---|---|
| 1 | 459-460 | "The above Un-audited Standalone & Consolidated Financial Results of the Company for the first quarter..." | — |
| 2 | 461-462 | "The above Results are in compliance with the Indian Accounting Standards (Ind-AS) as prescribed..." | — |
| 3 | 463-476 | "(i) During the previous year, the Company had issued 8,79,29,651 equity shares of face value..." Two sub-items: (i) QIP of ₹550 Cr, ₹513.72 Cr utilized, ₹36.28 Cr balance in FD/monitoring a/c; (ii) warrants to Promoters, 7,50,00,000 @ Rs.74, 25% received (₹138.75 Cr), ₹48.75 Cr utilized, ₹90 Cr balance in FD | CAPITAL_RAISE (dual: QIP carryover + promoter warrants, both partially unutilized) |
| 4 | 477-492 | "The Consolidated financial results for the first quarter ended 30th June, 2026 includes the results of the following entities" — 15-entity list (see Section 5) | see entity cross-check below |
| 5 | 493 | "Earning per share is not annualised for the Quarter ended 30th June, 2026, 31st March, 2026 and..." | — |
| 6 | 494-495 | "The Figures of the quarter ended March 31, 2026 were balancing figures between audited figures in..." | — |
| 7 | 500 | "The figures of the previous periods have been re-grouped/re-arranged wherever considered necessary." | — |

**7 notes.** No unnumbered/asterisk/dagger footnotes found elsewhere in the
extract (checked; none present).

---

## 5. AUDITOR REPORTS — PARAGRAPH-BY-PARAGRAPH

### 5a. Standalone Review Report (S Bhandari & Co LLP + Oswal Sunil & Company), pages 3-4
| Para | Line(s) | Type | First 15 words | Flags |
|---|---|---|---|---|
| 1 | 140-151 | Scope/subject matter | "We have reviewed the accompanying Statement of the Unaudited Standalone Financial Results ('the Statement')..." | OCR: opener rendered "I ." not "1." |
| 2 | 152-160 | Basis of review (SRE 2410) | "We conducted our review of the Statement in accordance with the Standard on Review Engagements..." | — |
| 3 | 162-168 | Conclusion (unmodified) | "Based on our review conducted as above, nothing has come to our attention that causes us..." | — |
| — (heading) | 170 | "Other Matter" heading | — | — |
| 4 | 171-174 | Other Matter | "The Statement includes the results for the quarter ended March 31, 2026 being the balancing figure..." | — |

Entities reviewed: standalone parent only (HFCL Limited); no unaudited /
management-furnished entities in this report (single-entity scope). UDIN:
Oswal Sunil & Co partner = 26056931FGSYCG7719 (line 187). S Bhandari & Co LLP
partner name/UDIN not shown in this report's signature block (see Section 7,
flag SIGNATURE_BLOCK_INCOMPLETE). No Emphasis of Matter, no Going Concern
language present.

### 5b. Consolidated Review Report (S Bhandari & Co LLP + Oswal Sunil & Company), pages 4-5
| Para | Line(s) | Type | First 15 words | Flags |
|---|---|---|---|---|
| 1 | 199-204 | Scope/subject matter | "We have reviewed the accompanying Statement of the Unaudited Consolidated Financial Results ('the Statement')..." | OCR: opener rendered "l." not "1." |
| 2 | 206-211 | Basis/responsibility | "This Statement, which is the responsibility of the Parent's Management and approved by the Parent's..." | — |
| 3 | 213-222 | Basis of review (SRE 2410) | "We conducted our review of the Statement in accordance with the Standard on Review Engagements..." | — |
| — | 224-225 | Unnumbered — additional procedures | "We also performed procedures in accordance with the circular issued by the SEBI under Regulation 33(8)..." | UNNUMBERED_PARA |
| 4 | 227-243 | Entity list (scope statement) | "The Statement includes the results of following Subsidiaries and Jointly Controlled Entities:" — 9 subsidiaries + 2 JCEs (see Section 6) | — |
| 5 | 244-255 | Conclusion (unmodified, subject to other-auditor reliance) | "Based on our review conducted and procedures performed as stated in paragraph 3 above and based on..." | OCR: opener buried as "~~-- 5." |
| 6 | 257-267 | Other-auditor reliance — unreviewed entities | "We did not review the interim financial information/financial results of two subsidiaries included in the..." Rs Nil revenue, PAT Rs 0.01 Cr, TCI Rs 0.01 Cr; + 2 JCEs, Group share PAT (0.02) Cr | UNAUDITED_MANAGEMENT_FURNISHED (2 subsidiaries + 2 JCEs, immaterial size) |
| 7 | 269-274 | Other-auditor reliance — one joint auditor only | "The interim financial information/financial results of five subsidiaries included in the unaudited consolidated financial results..." Revenue Rs 549.21 Cr, PAT Rs 84.92 Cr, TCI Rs 62.96 Cr — reviewed by only ONE of the two joint auditors | AUDITOR_SCOPE_LIMITATION (5 subsidiaries, ~28.7% of consol revenue this quarter, reviewed by one joint auditor only, not both) |
| 8 | 276-285 | Other-auditor reliance — foreign subsidiaries | "The interim financial information/financial results of two foreign subsidiaries (which includes consolidated financial results/financial information of one of such foreign subsidiaries incorporating results of its step-down subsidiaries)..." Revenue Rs 712.85 Cr, PAT Rs 30.38 Cr, TCI Rs 19.55 Cr — reviewed by foreign-country independent auditors, not the Indian joint auditors; step-down subsidiaries not individually named | AUDITOR_SCOPE_LIMITATION (2 foreign subsidiaries, ~37.2% of consol revenue, reviewed under foreign regs only; step-down subs unnamed) |
| — | 286-287 | Unnumbered — conclusion on paras 6-8 | "Our conclusion on the Statement in respect of matters stated in paragraphs 6, 7 and 8 above is not modified." | UNNUMBERED_PARA |
| — (heading) | 288 | "Other Matter" heading | — | — |
| 9 | 289-292 | Other Matter | "The Statement includes the results for the quarter ended March 31, 2026 being the balancing figure..." | — |

**Standalone: 4 paragraphs. Consolidated: 9 numbered + 2 unnumbered = 11
paragraphs. Combined total: 15 auditor-report paragraphs.**

**Material observation (AUDITOR_SCOPE_LIMITATION):** paragraphs 6+7+8 show
Rs 549.21 Cr + Rs 712.85 Cr = Rs 1,262.06 Cr of the Rs 1,914.98 Cr Q1FY27
consolidated revenue (~65.9%) was reviewed either by only ONE of the two
joint statutory auditors (para 7) or by foreign-jurisdiction auditors outside
the Indian joint-audit structure entirely (para 8), not by both signing
Indian auditors jointly. No going-concern language and no modified opinion
in either report.

---

## 6. CONSOLIDATION ENTITY LISTS — CROSS-CHECK

### 6a. Note 4 list (financial statements, lines 478-492) — 15 entities
| Row | Line | Entity | Relationship |
|---|---|---|---|
| a | 478 | HFCL Limited (HFCL) | Holding Company |
| b | 479 | HTL Limited | Subsidiary |
| c | 480 | Raddef Private Limited | Subsidiary |
| d | 481 | Moneta Finance Private Limited | Wholly Owned Subsidiary |
| e | 482 | Polixel Security Systems Private Limited | Wholly Owned Subsidiary |
| f | 483 | HFCL Advance Systems Private Limited | Wholly Owned Subsidiary |
| g | 484 | DragonWave HFCL India Private Limited | Wholly Owned Subsidiary |
| h | 485 | HFCL Technologies Private Limited | Wholly Owned Subsidiary |
| i | 486 | HFCL Inc. (USA) | Wholly Owned Subsidiary |
| j | 487 | HFCL B.V. (Netherlands) | Wholly Owned Subsidiary |
| k | 488 | Nimpaa Telecommunications Private Limited | Jointly Controlled Entity |
| l | 489 | BigCat Wireless Private Limited (OCR shows "I.") | Jointly Controlled Entity |
| m | 490 | HFCL Canada Inc. | Wholly Owned Sub of HFCL B.V. (step-down) |
| n | 491 | HFCL UK Limited | Wholly Owned Sub of HFCL B.V. (step-down) |
| o | 492 | HFCL Ply Limited, Australia | Wholly Owned Sub of HFCL B.V. (step-down) |

### 6b. Auditor Report para 4 list (lines 229-242) — 11 entities
| Row | Line | Entity | Relationship |
|---|---|---|---|
| — | 229 | Subsidiaries (header) | — |
| a | 230 | HTL Limited | Subsidiary |
| b | 231 | Polixel Security Systems Private Limited | Subsidiary |
| c | 232 | Moneta Finance Private Limited | Subsidiary |
| d | 233 | HFCL Advance Systems Private Limited | Subsidiary |
| e | 234 | Raddef Private Limited | Subsidiary |
| f | 235 | Dragon Wave HFCL India Private Limited | Subsidiary |
| g | 236 | HFCL Technologies Private Limited | Subsidiary |
| h | 237 | HFCL Inc. (USA) | Subsidiary |
| 9th (OCR "1.") | 238 | HFCL B.V. (Netherlands) | Subsidiary |
| — | 240 | Jointly Controlled Entities (header) | — |
| a | 241 | Nimpaa Telecommunications Private Limited | JCE |
| b | 242 | BigCat Wireless Private Limited | JCE |

**Cross-check result:** Auditor's para-4 list (11 entities) is a strict
subset of Note 4's list (15 entities): it omits the parent itself (HFCL
Limited — implicit as "the Parent") and the 3 step-down subsidiaries of
HFCL B.V. Netherlands (HFCL Canada, HFCL UK, HFCL Ply Australia). This is
consistent with auditor para 8's acknowledgement that one foreign
subsidiary's reviewed results "includes...results of its step-down
subsidiaries" without naming them individually — not necessarily an error,
but flagged as **ENTITY_LIST_DISCREPANCY** for A3/A4 to confirm the 3
unnamed step-down entities are fully captured in the Rs 712.85 Cr foreign-
subsidiary figure in para 8. No prior-quarter ledger path was supplied to
this run, so quarter-over-quarter ENTITY_CHANGE comparison could not be
performed — noted as a gap, not silently skipped.

---

## 7. DIGITAL SIGNATURE BLOCKS

| # | Line(s) | Signatory | Designation | Timestamp | Flags |
|---|---|---|---|---|---|
| 1 | 115-121 | Manoj Baid | President & Company Secretary | Digitally signed 2026.07.22 13:10:30 +05'30' | Meeting concluded 1:00 PM (13:00); signature at 13:10:30 is 10 minutes AFTER conclusion — correct sequencing, NOT flagged |
| 2 | 176-178, 295-297 | S Bhandari & Co LLP (Firm Reg. 000560C/C400334) — standalone report | Chartered Accountants (firm) | Date: July 22, 2026 | **SIGNATURE_BLOCK_INCOMPLETE** — no partner name, Membership No., or UDIN shown for this firm in the standalone report (contrast with Oswal Sunil, which is complete) |
| 3 | 184-187 | Nawin K Lahoty | Partner, Oswal Sunil & Company, Membership No. 056931 | Date: July 22, 2026; UDIN 26056931FGSYCG7719 | — (complete) |
| 4 | 303-306, 311 | J.S.P. Bansal | Partner, S Bhandari & Co LLP, Membership No. shown as "070" | Date: July 22, 2026; UDIN 26070980CFHVFF4134 | OCR-truncated membership number (UDIN prefix 070980 implies full no. is 070980, only "070" legible in extract) |
| 5 | 307-311 | Nawin K [Lahoty] | Partner, Oswal Sunil & Company, Membership No. shown as "0569" | Date: July 22, 2026; UDIN 26056931UQ[...] | OCR-truncated membership number and UDIN (partial match to line 187's 056931) |
| 6 | 503-505 | Mahendra Nahata | Managing Director, DIN 00052898 | Place: New Delhi; Date: 22nd July, 2026 | — |

**6 signature blocks total.**

---
