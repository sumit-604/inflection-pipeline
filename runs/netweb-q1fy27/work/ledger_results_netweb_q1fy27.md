# LEDGER — Netweb Technologies India Limited (NETWEB), Q1 FY27, Results Filing
Source: A1 extract `extract_results_netweb_q1fy27.txt` (6 OCR pages, forced 300-DPI
re-OCR + crop re-OCR + footing reconciliation; reconciled table, lines 283-328,
used as authoritative wherever a raw-pass cell carried a [LOW-CONF OCR] tag).
Prior-quarter ledger: none supplied — no diff possible for ENTITY_CHANGE /
DROPPED_SLIDE-type checks this run; noted, not treated as a gap in this ledger.

Extraction-meta context (not a disclosure unit, not counted): header block
lines 1-13; REWORK NOTE lines 15-34; companion-file scope note lines 36-43.
RECONCILIATION NOTES (lines 246-282, 7 numbered items) are the A1 agent's own
OCR-audit trail, not filing disclosure — excluded from the notes/count-test
categories below and listed separately for completeness only (see Appendix R).

```
=== A2 COUNT TEST ===
category: notes           grep_count: 6    sweep_count: 6    match: yes
category: line_items      grep_count: 26   sweep_count: 26   match: yes
category: zero_standing   grep_count: 1    sweep_count: 1    match: yes
category: agenda_items    grep_count: 4    sweep_count: 4    match: yes
category: auditor_paras   grep_count: 4    sweep_count: 4    match: yes
category: entities        grep_count: 2    sweep_count: 2    match: yes
category: annexure_items  grep_count: 4    sweep_count: 4    match: yes
category: signature_blocks grep_count: 3   sweep_count: 3    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep commands used (run against the extract file):
- notes: `sed -n '370,421p' <extract> | grep -n -E "^[0-9]+\.\s"` -> 6
- line_items: `sed -n '283,328p' <extract> | grep -n "|"` -> 28 raw hits, minus 2
  column-header continuation lines (not data rows) = 26
- agenda_items: `grep -n -E "^(Financial Results|Dividend|Annual General Meeting|Appointment of Cost Auditor)$" <extract>` -> 4
- auditor_paras: `sed -n '124,180p' <extract> | grep -n -E "^[0-9]+\.\s"` -> 4
- annexure_items: `sed -n '423,449p' <extract> | grep -n -E "^[0-9]+\.\s"` -> 4
- entities: `grep -n -E "Netweb Foundation|Netweb Technologies India Limited\b" <extract>` -> distinct entities = 2 (reporting entity + subsidiary)
- signature_blocks: manual sweep of all "Place:" / signatory-name / designation blocks -> 3
Manual sweep confirmed each category independently by reading the full extract
top to bottom; no additional numbered/unnumbered items found beyond the above.

---

## 1. NOTES — "Other Notes" section (page 5, lines 371-415)

| # | Line | First 15 words | Flags |
|---|------|-----------------|-------|
| 1 | 373 | "The financial results of the Company have been prepared in accordance with the recognition and" | Basis of preparation / Ind AS 34, Reg 33 compliance, Board approval reference |
| 2 | 382 | "The figures of the quarter ended March 31, 2026, being the balancing figure between the audited" | Standard Q4-as-balancing-figure note |
| 3 | 386 | "The Company has one subsidiary, Netweb Foundation, which is a not-for-profit entity incorporated" | Section 8 subsidiary; consolidation NOT applicable — see ENTITIES table |
| 4 | 391 | "According to Indian Accounting Standards (Ind-AS) 108 on \"Operating Segment\" the Company has" | Single segment: "Computer servers" |
| 5 | 394 | "On November 21, 2025, the Government of India notified the four Labour Codes - the Code on" | Labour Codes impact assessment; company states no material incremental impact for period ended March 31, 2026 (note: this note discusses the *prior* FY-end period, not the current quarter — carried note, flag CARRIED_NOTE) |
| 6 | 412 | "The Company has granted 4,935 ESOPs to the employees and Key managerial personnel of the" | ESOP grant dated Jan 18, 2025; vesting 1-2 yrs; cost recognised INR 0.38mn for Q1 FY27 |

Footnote (unnumbered, qualifies the EPS line items in the financial table, not
part of the "Other Notes" section — tracked here for completeness, not counted
in the notes gate above to keep grep/sweep scoping clean):
| Line(s) | Text | Flags |
|---|---|---|
| 244 (raw pass), 328 (reconciled, authoritative) | "* Not annualised for the quarter ended" | Qualifies Basic/Diluted EPS rows in all three quarter columns; duplicate appearance is an artifact of the extract showing both raw-OCR and reconciled table passes, not two distinct footnotes |

---

## 2. LINE ITEMS — Statement of Financial Results (reconciled table, lines 283-328)
Columns: Q1 FY27 (30-06-2026, Unaudited) | Q4 FY26 (31-03-2026, Audited) |
Q1 FY26 (30-06-2025, Unaudited) | FY26 (31-03-2026, Year, Audited). All Rs millions.

| # | Line | Item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|------|--------|--------|--------|------|-------|
| 1 | 288 | Revenue from operations | 8,196.86 | 7,737.02 | 3,012.12 | 21,835.63 | Q4FY26 value is the reconciled/footed figure (raw OCR ambiguous "1137202"; see Appendix R item 1) |
| 2 | 289 | Other income | 84.72 | 102.35 | 11.05 | 188.42 | |
| 3 | 290 | Total income (subtotal) | 8,281.58 | 7,839.37 | 3,023.17 | 22,024.05 | Footing PASS |
| 4 | 293 | Cost of materials consumed | 7,432.77 | 6,236.92 | 2,046.10 | 17,154.80 | |
| 5 | 294 | Change in inventories of finished goods and work-in-progress | (970.39) | (78.72) | 194.37 | 128.11 | Sign flips period to period — inventory drawdown in Q1FY27 |
| 6 | 295 | Employee benefits expense | 246.86 | 214.33 | 160.79 | 802.85 | |
| 7 | 296 | Finance costs | 115.24 | 81.53 | 9.78 | 129.53 | FY26 value reconciled (raw OCR "129.58"; see Appendix R item 2) |
| 8 | 297 | Depreciation and amortisation expenses | 33.25 | 38.34 | 33.23 | 142.11 | Q1FY27 value reconciled (raw OCR "33,25)"; see Appendix R item 3) |
| 9 | 298 | Other expenses | 282.47 | 398.75 | 162.84 | 901.45 | |
| 10 | 299 | Total expenses (subtotal) | 7,140.20 | 6,891.15 | 2,607.11 | 19,258.85 | Footing PASS |
| 11 | 301 | Profit before exceptional items and tax (subtotal) | 1,141.38 | 948.22 | 416.06 | 2,765.20 | |
| 12 | 302 | Exceptional items (net) | - | - | - | - | **ZERO_STANDING** — dash in all 4 periods; template row (SOUTHWEST-type: line exists for a transaction category that has not occurred) |
| 13 | 303 | Profit before tax (subtotal) | 1,141.38 | 948.22 | 416.06 | 2,765.20 | Identical to line 11 since exceptional items = nil |
| 14 | 306 | Current tax | 324.09 | 233.47 | 109.87 | 696.03 | |
| 15 | 307 | Adjustment of tax relating to earlier period | - | - | - | (0.68) | Dash in 3 of 4 periods, non-zero only in FY26 annual column — NOT flagged ZERO_STANDING (not dash in all periods) |
| 16 | 308 | Deferred tax charge (credit) | (35.94) | 8.82 | 1.40 | 11.69 | Sign flip Q1FY27 (credit) vs prior periods (charge) |
| 17 | 309 | Total tax expense (subtotal) | 288.15 | 242.29 | 111.27 | 707.04 | Footing PASS |
| 18 | 311 | Profit for the period / year (subtotal) | 853.23 | 705.93 | 304.79 | 2,058.16 | Footing PASS; Q1FY26 value reconciled punctuation only (raw "304,79"; see Appendix R item 5) |
| 19 | 315 | Re-measurement gains/(losses) on defined benefit plans (OCI) | 1.15 | 0.80 | 1.16 | 0.52 | Q1FY27 value reconciled (raw OCR "115"; see Appendix R item 4) |
| 20 | 316 | Income tax relating to items that will not be reclassified (OCI) | (0.29) | (0.20) | (0.29) | (0.13) | |
| 21 | 317 | Total other comprehensive income (loss), net of tax (subtotal) | 0.86 | 0.60 | 0.87 | 0.39 | Footing PASS |
| 22 | 319 | Total comprehensive income for the period / year (subtotal) | 854.09 | 706.53 | 305.66 | 2,058.55 | Footing PASS |
| 23 | 321 | Paid up equity share capital (face value Rs 2/share) | 113.88 | 113.88 | 113.31 | 113.88 | Q1FY26 differs slightly (113.31) — share count change between Q1FY26 and later periods |
| 24 | 322 | Other equity | - | - | - | 7,119.10 | Dash in all 3 quarter columns, populated only in FY26 annual (audited) column — standard annual-only balance-sheet disclosure; NOT flagged ZERO_STANDING (non-dash in one period) |
| 25 | 325 | Basic EPS (in INR) | 14.98 | 12.43 | 5.38 | 36.30 | Qualified by "*Not annualised for the quarter ended" footnote (line 328) |
| 26 | 326 | Diluted EPS (in INR) | 14.98 | 12.43 | 5.38 | 36.30 | Identical to Basic in every period (no dilutive instruments effect); FY26 value reconciled (raw OCR "36,30)"; see Appendix R item 6). Same footnote as line 25 |

zero_standing detail: 1 row (line 12, Exceptional items (net)).

---

## 3. AGENDA ITEMS — Board Outcome letter (pages 1-2, lines 45-121)

| # | Line(s) | Agenda item | Detail | Flags |
|---|---------|-------------|--------|-------|
| 1 | 66-69 | Financial Results | Q1FY27 unaudited results + limited review report approved, attached as Annexure-1, available on company website | |
| 2 | 71-76 | Dividend | Record date fixed: Friday, Aug 7, 2026, for FY2025-26 final dividend; payment within 30 days of AGM if shareholder-approved; continuation of prior intimation dated 02.05.2026 | |
| 3 | 78-88 | Annual General Meeting | 27th AGM: Saturday, Sep 19, 2026, 3:00 p.m., via VC/OAVM; register/share transfer books closed Sep 12-19, 2026; cut-off date Sep 11, 2026; remote e-voting window Sep 16 (9:00 AM) to Sep 18 (5:00 PM); Scrutinizer appointed: Mr. P.C. Jain, Practicing Company Secretary (M.No. F4103) | Sub-item: Scrutinizer appointment (line 87) |
| 4 | 90-95 | Appointment of Cost Auditor | M/s. Sunny Chhabra & Co., Cost Accountants (Membership No. 32469), appointed Cost Auditor for FY2026-27; Reg 30/Schedule III disclosure attached as Annexure-2 | See ANNEXURE-2 table below |

Board meeting timing (line 107): commenced 01:00 P.M., concluded 2:08 P.M. —
duration approx. 68 minutes for a meeting that approved 4 substantive agenda
items (results + dividend record date + AGM notice + cost auditor
appointment). Not flagged as anomalously short/long on its own; informational.

Letter date (line 49) and Subject line (line 58): "OUTCOME OF THE BOARD
MEETING HELD TODAY, i.e., JULY 28, 2026" — same-day letter, consistent with
board meeting date.

---

## 4. AUDITOR REPORT — Limited Review Report, S S Kothari Mehta & Co LLP (page 3, lines 124-179)

Report heading / addressee (structural, not counted in the auditor_paras gate,
listed for completeness):
| Line | Element |
|------|---------|
| 124-129 | Firm letterhead + report title: "Independent Auditor's Limited Review Report... pursuant to Regulation 33... as amended" |
| 131-133 | Addressee: "To the Board of Directors of Netweb Technologies India Limited" |

Numbered substantive paragraphs (gated category, grep=sweep=4):
| # | Line | First 15 words | Type |
|---|------|-----------------|------|
| 1 | 135 | "We have reviewed the accompanying Statement of Unaudited Financial Results of" | Scope paragraph — identifies statement reviewed, period (Q ended Jun 30 2026 and YTD Apr 1-Jun 30 2026), Reg 33 basis |
| 2 | 142 | "This Statement is the responsibility of the Company's management and approved by the Board of" | Management's responsibility paragraph — Ind AS 34, Companies Act 2013 s.133 basis |
| 3 | 149 | "We conducted our review of the Statement in accordance with the Standard on Review Engagement" | Basis of review paragraph — SRE 2410; explicitly states review provides less assurance than audit, no audit opinion expressed |
| 4 | 157 | "Based on our review conducted as above, nothing has come to our attention that causes us to believe" | Conclusion/opinion paragraph — **unmodified/clean conclusion** (no material misstatement noted) |

Report attributes (rule 5 checklist):
- Opinion type: unmodified (clean) limited-review conclusion, para 4.
- Emphasis of Matter: none present.
- Other Matters: none present.
- Going Concern language: none present (no adverse going-concern language raised).
- Entity list reviewed: standalone only — Netweb Technologies India Limited.
  No subsidiary/associate reviewed (consistent with Note 3, page 5: sole
  subsidiary Netweb Foundation excluded from consolidation, Section 8 entity).
- Unaudited / management-furnished entities: none disclosed (standalone
  statement, wholly reviewed by the statutory auditor).

Signature block (line 165-176):
| Line | Element | Value |
|------|---------|-------|
| 165 | Firm | For S S Kothari Mehta & Co. LLP, Chartered Accountants |
| 167 | ICAI Registration No. | 000756N/N500441 |
| 169 | Partner | Jalaj Soni |
| 171 | Membership No. | 528799 |
| 173 | UDIN | 26528799ZOYT106256 |
| 175 | Place | Faridabad |
| 176 | Date | July 28, 2026 |

---

## 5. ENTITIES (consolidation-relevant list; no prior-quarter ledger to diff against)

| # | Line | Entity | Relationship | Consolidation status | Flags |
|---|------|--------|--------------|----------------------|-------|
| 1 | 46 (first mention) | Netweb Technologies India Limited | Reporting entity | Standalone financials only | |
| 2 | 386-389 | Netweb Foundation (CIN U80902HR2022NPL103903) | Subsidiary, Section 8 not-for-profit company | Explicitly NOT consolidated ("requirement for consolidation of financial statements is not applicable") — profits not distributable per Sec 8 | No prior list supplied, so ENTITY_CHANGE cannot be evaluated this run (informational gap, not a filing-side flag) |

---

## 6. ANNEXURE-2 — Cost Auditor Reg-30/Schedule-III disclosure (page 6, lines 427-442)

| # | Line | Particular | Remark |
|---|------|------------|--------|
| 1 | 433-435 | Reason for change (appointment/re-appointment/resignation/removal/death) | Re-Appointment of M/s Sunny Chhabra & Co. as the Cost Auditors of the Company |
| 2 | 436 | Date of appointment | July 28, 2026 |
| 3 | 437 | Term of appointment | FY 2026-27 |
| 4 | 438-442 | Brief Profile | Sunny Chhabra & Co., Cost Auditors, registered with ICMAI, engaged in Cost Audit & Assurance Services and Advisory |

Annexure-1 (referenced at line 68, "Financial Results" agenda item) = the
Q1FY27 financial results statement + limited review report; already fully
enumerated above under LINE ITEMS and AUDITOR REPORT — not double-counted
here.

---

## 7. DIGITAL SIGNATURE BLOCKS (rule 7)

| # | Line(s) | Signatory | Designation | Timestamp present? | Flags |
|---|---------|-----------|-------------|---------------------|-------|
| 1 | 113-115 | Lohit Ghhe | Company Secretary & Compliance Officer (for Netweb Technologies India Limited, Board Outcome letter) | Date only (letter dated 28.07.2026, line 49); no time-of-day stamp | Cannot evaluate "signed before board meeting concluded" — no intraday timestamp in extract |
| 2 | 169-176 | Jalaj Soni | Partner, S S Kothari Mehta & Co. LLP (statutory auditor) | Date only (July 28, 2026); UDIN 26528799ZOYT106256 present; no time-of-day stamp | Same limitation as above |
| 3 | 419-421 | Sanjay Lodha (DIN 00461913) | Managing Director | Date only (28-07-2026); no time-of-day stamp | Same limitation as above |

All three signature dates are same-day as the board meeting (July 28, 2026,
commenced 1:00 PM / concluded 2:08 PM per Board Outcome letter, line 107);
none of the three blocks carries a finer-grained timestamp in the OCR'd
extract, so the "signed before meeting concluded" check cannot be
mechanically evaluated this run — noted as a limitation, not a flag.

---

## Appendix R — A1's own OCR reconciliation notes (mechanical audit trail, NOT
a filing disclosure; excluded from the count-test gate above; listed here
only so nothing in the extract goes unaccounted for)

| # | Line | Cell | Raw OCR | Resolved (footing-confirmed) |
|---|------|------|---------|-------------------------------|
| 1 | 247-252 | Revenue from operations, Q4FY26 col | "1137202" | 7,737.02 |
| 2 | 253-256 | Finance costs, FY26 col | "129.58" | 129.53 |
| 3 | 257-259 | Depreciation & amortisation, Q1FY27 col | "33,25)" | 33.25 |
| 4 | 260-263 | Re-measurement gains/(losses), Q1FY27 col | "115" | 1.15 |
| 5 | 264-268 | Profit for the period, Q1FY26 col | "304,79" | 304.79 (punctuation only) |
| 6 | 269-271 | Diluted EPS, FY26 col | "36,30)" | 36.30 |
| 7 | 272-279 | Current tax (Q4FY26) / Total tax expense & Total expenses (Q1FY26) | low-confidence OCR (68-79%) | confirmed unchanged after crop re-OCR + footing |

No cell remains [AMBIGUOUS]; all 5 footing checks (Total income, Total
expenses, Total tax expense, Profit for the period, Total OCI, Total
comprehensive income) pass across all 4 columns (lines 330-368 of extract).
