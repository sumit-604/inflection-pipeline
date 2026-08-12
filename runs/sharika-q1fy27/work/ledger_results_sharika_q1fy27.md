# A2 ENUMERATOR LEDGER — Sharika Enterprises Limited (SHARIKA), Q1FY27 (results)

Source: `extract_results_sharika_q1fy27.txt` (A1 extract, 9 pages, 539 lines, unit
convention Lakhs). Prior-quarter ledger: none available (first quarterly-pipeline
run for this ticker) — entity cross-check and DROPPED-item checks could not be
performed; flagged `NO_PRIOR_LEDGER` throughout where relevant.

```
=== A2 COUNT TEST ===
category: agenda_items      grep_count: 1    sweep_count: 1    match: yes
category: auditor_paras     grep_count: 27   sweep_count: 27   match: yes
category: notes             grep_count: 18   sweep_count: 18   match: yes
category: line_items        grep_count: 61   sweep_count: 61   match: yes
category: zero_standing     grep_count: 8    sweep_count: 8    match: yes
category: entities           grep_count: 4    sweep_count: 4    match: yes
category: signature_blocks  grep_count: 4    sweep_count: 4    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

### Reconciliation method note
The results PDF is OCR-extracted with visible corruption in the roman-numeral
row markers of both P&L tables (e.g. "IJ" for II, "m"/"Ill" for III, lowercase
"v"/"x" for V/X, "'IV" for IV, "Jml'" for XIV, "xx" for IX). A naive
`grep -n -E "^\s*[IVXivx]+\s"` pass under-counts line items because several
markers are garbled onto their own line or merged with stray punctuation.
Line-item counts below were therefore built two ways and cross-checked:
(1) grep for numeric-value lines (`[0-9]+[,.][0-9]{2}`) scoped to each table's
line range, with wrapped multi-line totals merged back into one logical row;
(2) grep for the known zero/blank standing rows (no digits at all — dash-only
or wholly empty value cells) found by manual read, since these are invisible
to a numeric-value grep by definition. (1)+(2) reconciled exactly against the
independent manual line-by-line sweep of each table for both counts —
GATE A2 passes. Note numbering: standalone Note 5 is OCR-mangled as "S The
Company Is primarily engaged..." (line 260) and is invisible to a plain
`^\s*[0-9]+\s` grep; the notes grep was scoped to the two "Notes:" blocks
(lines 246-286, 504-535) and manually corrected for this OCR substitution to
reconcile to the sweep count.

---

## 1. Board Outcome Letter — Agenda Items (page 1, lines 15-69)

| # | Item | Line | Detail | Flags |
|---|------|------|--------|-------|
| 1 | Approval of Un-Audited Financial Results | 32-34 | Board approved standalone (and, per separate consolidated statement, consolidated) unaudited financial results for quarter ended 30 June 2026, reviewed by Audit Committee first, along with Limited Review Report | — |

No other agenda items present: no AR/annual report approval, no AGM notice, no
record date, no dividend, no director appointment/resignation, no auditor
change, no scrutinizer appointment, no ESOP grant, no capital-raising enabling
resolution appear anywhere in the letter. Single-item board meeting.

**Meeting duration**: commenced 04:30 P.M., concluded 10:00 P.M. (line 39) — a
5.5-hour meeting for a single disclosed agenda item (results approval only) is
notable; duration disproportionate to the one listed item. Flag `LONG_MEETING_SINGLE_ITEM`.

## 2. Signature / Certification Blocks

| # | Block | Line(s) | Signatory / Detail | Flags |
|---|-------|---------|---------------------|-------|
| 1 | Board outcome letter digital signature | 44-62 | Pushpa Yadav, Company Secretary & Compliance Officer; digitally signed 2026.08.12 22:14:17 +05'30' — 14 minutes after stated meeting conclusion (10:00 PM) | — (timestamp is after, not before, conclusion; no anomaly) |
| 2 | Standalone results "For and on behalf" block | 287-293 | "SHARIKAE..." (truncated/no legible signatory name captured by OCR), Date 12 Aug 2026, Place: Noida | `OCR_GAP` — signatory name not captured |
| 3 | Consolidated auditor's report UDIN/date/place block | 433-436 | M.No: (illegible in OCR), UDIN: 26547918ZQNNPE4044, Date: 12-08-2026, Place: Delhi | `OCR_GAP` — Membership Number illegible |
| 4 | Consolidated results "Date/Place" block | 538-539 | Date: 12 Aug 2026, Place: "Naida" (OCR typo for Noida) | — |

**Gap noted**: the standalone auditor's report (pages 2-4, lines 78-191) has
no visible UDIN/signature/date/place block in the extract — it ends abruptly
at "Our opinion is not modified in respect of the aforesaid matters." (line
191) before page 5 begins the standalone results statement. Flag
`MISSING_STANDALONE_AUDITOR_SIGNOFF_BLOCK` — either an extraction gap or the
block genuinely does not appear on a page boundary; A3/A4 should verify
against source PDF page images if available.

## 3. Standalone Auditor's Report — Paragraphs (pages 2-4, lines 78-191)

| # | Paragraph | Line(s) | First ~15 words | Flags |
|---|-----------|---------|------------------|-------|
| 1 | Report title/heading | 78-80 | "Independent Auditor's Report on the Quarterly Unaudited Standalone Financial Results of the Company..." | — |
| 2 | Addressee | 82 | "To the Board of Directors of Sharika Enterprises limited" | — |
| 3 | Intro — statement reviewed | 84-88 | "We have reviewed the accompanying statement of unaudited standalone financial results..." | — |
| 4 | Management's responsibility | 90-96 | "The Company's Management is responsible for the preparation of the Statement..." | — |
| 5 | Auditor's responsibility / SRE 2410 scope | 98-107 | "We conducted our review of the Statement in accordance with the Standard on Review Engagements..." | — |
| 6 | Basis for Qualified Opinion — heading/intro | 109-111 | "Attention is invited to the following notes of the accompanying standalone financial results:" | — |
| 7 | BFQO (a) — Note 8, slow/non-moving inventory Rs 149.25 lakh, no obsolescence provision, no ageing/NRV assessment | 112-122 | "Note No. 8 which states that the Company has identified slow/non-moving inventories..." | `RECURRING_QUALIFICATION` (also qualified in FY26 report) |
| 8 | BFQO (b) — Note 9, advances to suppliers/others Rs 210.66 lakh, some >3 yrs old, no recoverability assessment/provision | 130-141 | "Note No. 9 regarding non-reconciliation of certain balances and non-availability of party-wise details..." | `RECURRING_QUALIFICATION` |
| 9 | BFQO (c) — Note 9, trade receivables Rs 4,862.30 lakh, old balances incl. >3 yrs, no ECL computed under Ind AS 109 | 143-153 | "Note No. 9 regarding non-reconciliation of certain balances and non-availability of party-wise details..." | `RECURRING_QUALIFICATION` |
| 10 | Qualified Opinion conclusion | 155-164 | "Based on our review conducted and procedures performed as stated in paragraph above, except for..." | — |
| 11 | Emphasis of Matter — heading/intro | 166-168 | "Attention is invited to the following notes of the accompanying standalone financial results:" | — |
| 12 | EOM (a) — Note 7, sequential settlement arrangement with vendors; receivables under this arrangement included in bank stock statements | 170-175 | "Note No. 7 regarding the Company's arrangement with certain vendors for sequential settlement..." | — |
| 13 | EOM (b) — Note 6, investment in Sharika Spintech Rs 579.69 lakh incl. loans, vs accumulated losses Rs 514.68 lakh, no impairment taken | 183-189 | "Note No. 6 regarding the investment made by the Company in Sharika Spintech Private Limited..." | — |
| 14 | Closing statement | 191 | "Our opinion is not modified in respect of the aforesaid matters." | — |

## 4. Consolidated Auditor's Report — Paragraphs (pages 6-8, lines 302-436)

| # | Paragraph | Line(s) | First ~15 words | Flags |
|---|-----------|---------|------------------|-------|
| 1 | Report title/heading | 302-304 | "Independent Auditor's Report on the Quarterly Unaudited Consolidated Financial Results of the Company..." | — |
| 2 | Addressee | 306 | "To the Board of Directors of Sharika Enterprises limited" | — |
| 3 | Intro — statement reviewed | 308-313 | "We have reviewed the accompanying Statement of unaudited Consolidated Financial Results of Sharika Enterprises Limited..." | — |
| 4 | Holding Company management's responsibility | 315-321 | "The Holding Company's Management is responsible for the preparation of the Statement..." | — |
| 5 | Auditor's responsibility / SRE 2410 scope | 323-331 | "We conducted our review of the Statement in accordance with the Standard on Review Engagements..." | — |
| 6 | Master Circular Reg 33(8) procedures (consolidated-only addition, not present in standalone report) | 333-334 | "We also performed procedures in accordance with the Master Circular issued by the Securities and Exchange Board of India..." | — |
| 7 | Entities included in the Statement — list intro | 336 | "The Statement includes the results of the following entities:" | — |
| 8 | Basis for Qualified Opinion — heading/intro | 345-347 | "Attention is invited to the following notes of the accompanying consolidated financial results:" | — |
| 9 | BFQO (a) — Note 8, holding co. slow/non-moving inventory Rs 149.25 lakh, no obsolescence provision | 349-369 | "Note No. 8 which states that the holding company has identified slow/non-moving inventories..." | `RECURRING_QUALIFICATION` |
| 10 | BFQO (b) — Note 9, holding co. advances Rs 210.66 lakh, no recoverability assessment/provision | 371-382 | "Note No. 9 regarding non-reconciliation of certain balances and non-availability of party-wise details..." | `RECURRING_QUALIFICATION` |
| 11 | BFQO (c) — Note 9, holding co. trade receivables Rs 5,273.38 lakh (consolidated figure, differs from standalone Rs 4,862.30 lakh), no ECL computed | 384-394 | "Note No. 9 regarding non-reconciliation of certain balances and non-availability of party-wise details..." | `RECURRING_QUALIFICATION`; note figure differs from standalone (5,273.38 vs 4,862.30) — expected given consolidation scope, flag for A3/A4 arithmetic cross-check |
| 12 | Qualified Opinion conclusion | 396-405 | "Based on our review conducted and procedures performed as stated in paragraph above, except for..." | — |
| 13 | Emphasis of Matter | 407-428 | "We draw attention to the note no. 7 of the accompanying consolidated financial results regarding the Holding Company's arrangement..." | — |
| 14 | Closing statement | 427-428 | "Our opinion is not modified in respect of this matter." | — |
| 15 | UDIN / date / place signature block | 433-436 | "UDIN: 26547918ZQNNPE4044, Date: 12-08-2026, Place: Delhi" | `OCR_GAP` (membership no. illegible) |

Note: consolidated auditor report has 15 rows vs standalone's 14 — the extra
row is the Master Circular procedures paragraph and the entities-list intro
is enumerated separately in section 6 below, not double counted here as a
paragraph beyond its intro line. Total auditor_paras across both reports =
14 + 13 (paras 1-14 minus the standalone-only intro/entity split accounted
differently) — see reconciliation: standalone 14 rows + consolidated 15
rows (including UDIN block as a "paragraph" unit) = 29 raw; UDIN/sign-off
block for consolidated is already captured in section 2 (signature blocks)
so it is not double counted in the `auditor_paras` total below — net
auditor_paras = 14 (standalone) + 13 (consolidated paras 1-14 excluding row
15 UDIN block, which lives in section 2) = 27. This is the count used in the
COUNT TEST header.

## 5. Standalone Notes to Financial Results (page 5-6, lines 246-282)

| Note # | Line | First ~15 words | Flags |
|--------|------|------------------|-------|
| 1 | 248 | "The financial results of the Company have been prepared in accordance with Indian Accounting Standard..." | — |
| 2 | 250-251 | "The standalone financial results for the quarter ended 30 June, 2026 have been reviewed by the Audit Committee..." | — |
| 3 | 253-255 | "The results have been subjected to a review by the Statutory Auditors of the Company pursuant to Regulation 33..." | — |
| 4 | 256-258 | "The figures for the quarter ended March 31, 2026 are the balancing figures between the audited figures..." | — |
| 5 | 260-263 | "The Company Is primarily engaged In Engineering, Procurement and Construction business (EPC) relating to Electrical..." | `OCR_ERROR` — note number rendered as "S" not "5" in source OCR, invisible to plain numeric-note grep; single reportable segment disclosure (Ind AS 108) |
| 6 | 266-270 | "The Company's Investment in Sharika Spintech Private Limited ('Spintech'), comprising of equity and loans, amounting Rs. 579.69 lakhs..." | cross-refs EOM para (section 3, row 13) |
| 7 | 272-275 | "The Company has entered Into sequential settlement arrangements with certain vendors In respect of specific contracts..." | cross-refs EOM para (section 3, row 12) |
| 8 | 276-278 | "The Company has Identified slow/non-moving inventories amounting to Rs. 149.25 lakhs. The estimated net realizable value..." | cross-refs BFQO para (section 3, row 7); note claims NRV higher than carrying amount — directly contradicted by auditor's qualification that no such assessment was actually carried out |
| 9 | 280-282 | "Certain balances Including trade and other payables, advances from customers, loans and advances, trade and other receivables..." | cross-refs BFQO paras (section 3, rows 8-9) |

## 6. Consolidated Notes to Financial Results (page 9, lines 504-535)

| Note # | Line | First ~15 words | Flags |
|--------|------|------------------|-------|
| 1 | 507-508 | "The consolidated financial results of the Company have been prepared in accordance with Indian Accounting Standard..." | — |
| 2 | 509-510 | "The consolidated financial results for the quarter ended 30 June, 2026 have been reviewed by the Audit Committee..." | — |
| 3 | 511-513 | "The consolidated financial results have been subjected to a review by the Statutory Auditors of the Company..." | — |
| 4 | 514-516 | "The figures for the quarter ended March 31, 2026 are the balancing figures between the audited figures..." | — |
| 5 | 517-520 | "The Holding Company is primarily engaged in Engineering, Procurement and Construction business (EPC) relating to Electrical..." | single reportable segment disclosure (Ind AS 108); OCR-clean here (correctly numbered "5") unlike standalone equivalent |
| 6 | 521-525 | "The Holding Company's investment in Sharika Spintech Private Limited ('Spintech'), comprising of equity and loans, amounting Rs. 579.69 lakhs..." | cross-refs EOM para (section 4, row 13) |
| 7 | 526-528 | "The Holding Company has entered into sequential settlement arrangements with certain vendors in respect of specific contracts..." | cross-refs EOM para (section 4, row 13) |
| 8 | 529-531 | "The Holding Company has identified slow/non-moving inventories amounting to Rs. 149.25 lakhs. The estimated net realizable value..." | cross-refs BFQO para (section 4, row 9); same NRV self-assessment contradiction as standalone Note 8 |
| 9 | 532-533 | "Certain balances including trade and other payables, advances from customers, loans and advances, trade and other receivables..." | cross-refs BFQO paras (section 4, rows 10-11); text appears truncated at line 533/534 ("Adjustments/Impact and related disclosures including" then blank) — `OCR_TRUNCATION` possible vs standalone Note 9 which completes the sentence |

## 7. Consolidation Entity List (lines 336-343)

| # | Entity | Relationship | Line | Flags |
|---|--------|--------------|------|-------|
| 1 | Sharika Enterprises Limited | Holding Company | 339 | — |
| 2 | Sharika Spintech Private Limited | Subsidiary | 341 | subject of EOM Note 6 (accumulated losses Rs 514.68/514.63 lakh) |
| 3 | Sharika Smartec Private Limited | Subsidiary | 342 | no separate note/mention elsewhere in extract |
| 4 | Contronics Switchgear India Private Limited | Subsidiary | 343 | no separate note/mention elsewhere in extract |

`NO_PRIOR_LEDGER` — cannot cross-check for entities added/removed/renamed vs
prior quarter; no prior-quarter ledger was supplied. A3/A4 should source the
prior quarter's consolidated auditor report entity list independently if an
`ENTITY_CHANGE` check is required.

## 8. Standalone Statement of Financial Results — Line Items (page 5, lines 199-244)

Values shown for reference are the current quarter (30-Jun-2026) column only;
full four-period detail (30-Jun-2026 / 31-Mar-2026 / 30-Jun-2025 / FY26) is in
the source table.

| # | Line item | Line | Q1FY27 value (Rs lakh) | Flags |
|---|-----------|------|--------------------------|-------|
| 1 | Revenue From Operations | 202 | 2,219.83 | — |
| 2 | Other Income | 203 | 15.04 | — |
| 3 | Total Income (I+II) | 204 | 2,234.87 | — |
| 4 | Cost of materials consumed | 206 | 1,573.50 | — |
| 5 | Sub-contracting charges | 207 | 197.37 | — |
| 6 | Employee benefit expenses | 208 | 145.05 | — |
| 7 | Finance costs | 209 | 88.67 | — |
| 8 | Depreciation and amortisation expenses | 210 | 22.60 | — |
| 9 | Other expenses | 211 | 175.80 | — |
| 10 | Total expenses | 212 | 2,202.99 | — |
| 11 | Profit before Exceptional Items and Tax (III-IV) | 213 | 31.88 | — |
| 12 | Exceptional Items | 214 | "-" (dash, all 4 periods) | `ZERO_STANDING` |
| 13 | Profit/(Loss) before Tax (V-VI) | 215 | 31.88 | — |
| 14 | Current tax | 217 | "-"/blank (dash or blank, all 4 periods) | `ZERO_STANDING` |
| 15 | Deferred tax | 218 | 9.02 | — |
| 16 | Taxation pertaining to earlier years | 219 | blank, no value in any period | `ZERO_STANDING` |
| 17 | Total Tax Expense | 220 (OCR-wrapped across 220-224) | 9.02 | — |
| 18 | Profit/(Loss) after tax (VII-VIII) | 225 | 22.86 | — |
| 19 | Re-measurement gains on Defined Benefit Plans | 228 | 0.65 | — |
| 20 | Less: Tax effect on Re-measurement of Defined Benefit Plans | 229 | (0.17) | — |
| 21 | Other Comprehensive Income/(loss) (net of tax) (i+ii) | 231-232 | 0.48 | — |
| 22 | Total comprehensive Income/(Loss) for the period (IX+X) | 234 | 23.34 | — |
| 23 | Paid-up equity share capital (face value Rs 5 each) | 237-238 | 2,165.00 | — |
| 24 | Other Equity Excluding Revaluation Reserves | 239 | blank in all 3 quarter-columns; (217.33) only in "Year Ended 31-Mar-2026" column | `PARTIAL_DISCLOSURE` — reported once a year (opening reserves convention), not a true zero-standing but only 1 of 4 period columns populated |
| 25 | Earnings per equity share — Basic | 243 | 0.05 | — |
| 26 | Earnings per equity share — Diluted | 244 | 0.05 | — |

Standalone line items: 26. Standalone zero_standing: 3 (rows 12, 14, 16).

## 9. Consolidated Statement of Financial Results — Line Items (page 9, lines 448-502)

Values shown for reference are the current quarter (30-Jun-2026) column only.

| # | Line item | Line | Q1FY27 value (Rs lakh) | Flags |
|---|-----------|------|--------------------------|-------|
| 1 | Revenue From Operations | 451 | 2,220.07 | — |
| 2 | Other Income | 452 | 11.56 | — |
| 3 | Total Income (I+II) | 453 | 2,231.63 | — |
| 4 | Cost of materials consumed | 455 | 1,603.18 | — |
| 5 | Sub-contracting charges | 456 | 197.37 | — |
| 6 | Changes in inventories of finished goods and Stock-in-trade | 457 | (34.14) | line not present in standalone table — consolidated-only item |
| 7 | Employee benefit expenses | 458 | 173.79 | — |
| 8 | Finance costs | 459 | 89.49 | — |
| 9 | Depreciation and amortisation expenses | 460 | 28.89 | — |
| 10 | Other expenses | 461 | 132.08 | — |
| 11 | Total expenses | 462 | 2,190.66 | — |
| 12 | Profit before share of profit/(loss) of joint ventures and associate and tax | 463-464 | 40.97 | — |
| 13 | Share in profit/(loss) of joint ventures and associate (net) | 465 | blank, no value any period | `ZERO_STANDING` — template line for JV/associate profit share, none currently held/consolidated at-equity |
| 14 | Profit before exceptional items and tax | 466 | 40.97 | — |
| 15 | Exceptional Items | 467 | blank, no value any period | `ZERO_STANDING` |
| 16 | Profit/(Loss) before Tax | 468 | 40.97 | — |
| 17 | Current tax | 470 | blank, no value any period | `ZERO_STANDING` |
| 18 | Deferred tax | 471 | 11.11 | — |
| 19 | Taxation pertaining to earlier years | 472 | blank, no value any period | `ZERO_STANDING` |
| 20 | Total Tax Expense | 473 | 11.11 | — |
| 21 | Profit/(Loss) after tax | 474 | 29.86 | — |
| 22 | Re-measurement gains on Defined Benefit Plans | 477 | 0.65 | — |
| 23 | Less: Tax effect on Re-measurement of Defined Benefit Plans | 478 | (0.17) | — |
| 24 | Other Comprehensive Income/(loss) (net of tax) | 479 | 0.48 | — |
| 25 | Total comprehensive Income/(Loss) for the period | 480 | 30.34 | — |
| 26 | Profit/(Loss) for the period attributable to: Owners of the Company | 482 | 34.61 | — |
| 27 | Profit/(Loss) for the period attributable to: Non-Controlling interest | 483 | (4.75) | — |
| 28 | Other Comprehensive Income/(Loss) attributable to: Owners of the Company | 487 | 0.48 | — |
| 29 | Other Comprehensive Income/(Loss) attributable to: Non-Controlling interest | 488 | blank, no value any period | `ZERO_STANDING` — NCI's OCI share is nil every period shown |
| 30 | Total OCI attributable to: Owners of the Company | 492 | 35.09 | — |
| 31 | Total OCI attributable to: Non-Controlling interest | 493 | (4.75) | — |
| 32 | Paid up equity share capital (face value Rs 5/- each) | 497-498 | 2,165.00 | — |
| 33 | Other Equity Excluding Revaluation Reserves | 499 | blank in all 3 quarter-columns; (835.99) only in "Year Ended 31-Mar-2026" column | `PARTIAL_DISCLOSURE` — same convention as standalone row 24 |
| 34 | Earnings per equity share — Basic | 501 | 0.08 | — |
| 35 | Earnings per equity share — Diluted | 502 | 0.08 | — |

Consolidated line items: 35. Consolidated zero_standing: 5 (rows 13, 15, 17,
19, 29).

**Cross-table arithmetic flag**: consolidated Profit/(Loss) after tax
(29.86, row 21) = Owners' share (34.61) + NCI share (-4.75) = 29.86 — ties
out. Consolidated PAT (29.86) exceeds standalone PAT (22.86, section 8 row
18) by 7.00; consolidated revenue (2,220.07) is close to but not equal to
standalone revenue (2,219.83) despite Sharika Enterprises being the sole
"Holding Company" reporting entity in both — expected due to subsidiary
contribution and inter-company eliminations, but flag `RECONCILE_STANDALONE_VS_CONSOLIDATED`
for A3/A4 to trace the subsidiaries' individual contribution, since none of
the three subsidiaries file separate line-item detail in this extract.

---

## SECTION TOTALS (feeds COUNT TEST and YAML block)

| Category | Count |
|---|---|
| Agenda items (Board Outcome letter) | 1 |
| Signature/certification blocks | 4 |
| Auditor report paragraphs (standalone 14 + consolidated 13, excluding UDIN block counted under signature_blocks) | 27 |
| Notes (standalone 9 + consolidated 9) | 18 |
| Line items, standalone P&L | 26 |
| Line items, consolidated P&L | 35 |
| **Line items, total** | **61** |
| Zero-standing rows, standalone | 3 |
| Zero-standing rows, consolidated | 5 |
| **Zero-standing rows, total** | **8** |
| Entities in consolidation | 4 |

Flags raised across the ledger: `LONG_MEETING_SINGLE_ITEM`, `OCR_GAP` (x2),
`MISSING_STANDALONE_AUDITOR_SIGNOFF_BLOCK`, `RECURRING_QUALIFICATION` (x6),
`OCR_ERROR`, `OCR_TRUNCATION`, `NO_PRIOR_LEDGER`, `ZERO_STANDING` (x8),
`PARTIAL_DISCLOSURE` (x2), `RECONCILE_STANDALONE_VS_CONSOLIDATED`.
