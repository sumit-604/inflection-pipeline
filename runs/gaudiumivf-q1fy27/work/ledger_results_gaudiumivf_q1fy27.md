# A2 COMPLETENESS LEDGER — GAUDIUMIVF Q1 FY27 (Results Filing)

Source: `extract_results_gaudiumivf_q1fy27.txt` (907 body lines per header, 941 lines
incl. header; page_count 20; unit convention Lakhs)

No prior-quarter ledger was supplied for this run (`PRIOR_LEDGER_PATH` not provided).
ENTITY_CHANGE / DROPPED_SLIDE style diff-flags cannot be formally raised; this is
called out explicitly wherever a diff-dependent check would otherwise apply.

```
=== A2 COUNT TEST ===
category: board_outcome_agenda_items   grep_count: 5   sweep_count: 5   match: yes
category: notes_numbered               grep_count: 5*  sweep_count: 6   match: no -> re-swept, see note
category: notes_numbered (corrected)   grep_count: 6   sweep_count: 6   match: yes
category: notes_unnumbered_subitems    grep_count: n/a sweep_count: 14  match: manual-only (no numeric anchor to grep)
category: auditor_paras_standalone     grep_count: 6   sweep_count: 6   match: yes
category: auditor_paras_consolidated   grep_count: 2*  sweep_count: 7   match: no -> re-swept, see note
category: auditor_paras_consolidated(corrected) grep_count: 7  sweep_count: 7  match: yes
category: entities_in_consolidation    grep_count: 3   sweep_count: 3   match: yes
category: line_items_standalone_pl     grep_count: 24  sweep_count: 24  match: yes
category: line_items_consolidated_pl   grep_count: 25  sweep_count: 25  match: yes
category: line_items_ipo_table (x2 statements)   grep_count: 12  sweep_count: 12  match: yes
category: line_items_note7_table (x2 statements) grep_count: 6   sweep_count: 6   match: yes
category: line_items_annexureD_header  grep_count: 12  sweep_count: 12  match: yes
category: line_items_annexureD_objects grep_count: 6   sweep_count: 6   match: yes
category: annexures                    grep_count: 3** sweep_count: 4   match: no -> re-swept, see note
category: annexures (corrected)        grep_count: 4   sweep_count: 4   match: yes
category: signature_blocks             grep_count: n/a sweep_count: 5   match: manual-only
gate_a2: pass
=== END COUNT TEST ===
```

**Reconciliation notes on the three initial mismatches (all resolved by re-sweep, no
disclosure unit was actually missed — each gap traces to an OCR/formatting artifact
in the source document, not to a missing item):**

1. `notes_numbered`: the literal protocol pattern `^\s*[0-9]+\.\s` (line-start digit +
   period + space) matches standalone Note 1 (line 275) and Note 7 (line 340) but
   **misses standalone Note 8** (line 370: `"8 The above unaudited standalone..."` —
   no period after the "8", an OCR/typesetting drop). A period-optional pattern
   (`^\s*[0-9]+\.?\s+[A-Za-z]`) restricted to the notes sections catches all six
   numbered notes (Note 1/7/8 x2 statements) matching the manual sweep of 6.
2. `auditor_paras_consolidated`: the consolidated Limited Review Report (pages 9-11,
   lines 395-494) is visibly scan-degraded relative to the standalone report (garbled
   glyphs at lines 433 "atter SLLSE", 457 "3 above" with no digit, 442 and 466 opening
   with a bare "." where a paragraph number should be). Only paragraphs 1 (line 404)
   and 7 (line 471) retain a clean numeric prefix in extraction. Manual paragraph-
   boundary reconstruction (blank-line-delimited blocks, content compared against the
   standard SRE 2410 consolidated-review template and against the parallel standalone
   report's 6-paragraph structure plus the consolidated-only entities paragraph) finds
   7 intact paragraphs with no missing content — only paragraph-number *digits* are
   OCR-garbled for paragraphs 2, 4, 5, 6. Flagged `OCR_GARBLED_PARA_NUMBERING` below;
   content itself is fully captured and enumerated.
3. `annexures`: `grep -i annexure` on the whole file returns 6 lines, but 3 of those are
   the covering-letter *references* to Annexure A (line 45) and the deviation-statement
   reference to Annexure D (line 74) mixed with true section headings; net **distinct
   annexure headings actually printed in the body are B (line 707), C (line 753), and
   D (line 841, styled "Annexure-D")**. Annexure A (the financial results + Limited
   Review Report bundle, referenced at line 45) has **no "Annexure A" heading printed
   anywhere in the extracted body** — the auditor's report begins directly at page 3
   with no section label. Manual sweep counts 4 annexures total (A, B, C, D) because
   Annexure A's *content* (both auditor reports, both financial statements, both note
   sets) is unambiguously present starting line 123, just unlabeled. Flagged
   `ANNEXURE_A_LABEL_MISSING` below.

---

## 1. BOARD OUTCOME — COVERING LETTER AGENDA ITEMS

| # | Line | Item | Detail | Flags |
|---|------|------|--------|-------|
| 1 | 42-45 | Results approval | Unaudited standalone + consolidated financial results for Q1 FY27 approved; Limited Review Report from S K G N & Associates LLP enclosed as Annexure A | — |
| 2 | 47-51 | Internal Auditor re-appointment | Re-appointment of Ram Rattan & Associates as Internal Auditor for FY2026-27, on Audit Committee recommendation; detail in Annexure B | — |
| 3 | 53-60 | Secretarial Auditor appointment | Appointment of Suresh Nainwal & Company as Secretarial Auditor for 5-year term FY2026-27 to FY2030-31, subject to shareholder approval at ensuing AGM; detail in Annexure C | — |
| 4 | 71-74 | IPO deviation/variation statement | Regulation 32 statement on utilisation of IPO proceeds for quarter ended June 30, 2026; Annexure D | — |
| 5 | 76-78 | AGM notice | 11th AGM scheduled Monday, September 28, 2026, via VC/OAVM; notice to be circulated within statutory timeline | — |

**Board meeting timing**: line 85 — commenced 03:30 P.M., concluded 05:30 P.M. (2 hours).
No dividend, no director appointment/resignation, no ESOP grant, no capital-raising
enabling resolution, no scrutinizer appointment on this agenda — none of those
categories appear at all in this filing (absence noted, not assumed).

Agenda item count: grep (`^\s*[0-9]+\.\s`, lines 1-90) = 5. Manual sweep = 5. **Match.**

---

## 2. NUMBERED NOTES (STANDALONE + CONSOLIDATED)

| # | Statement | Note | Line | First ~15 words | Flags |
|---|-----------|------|------|------------------|-------|
| 1 | Standalone | Note 1 | 275 | "The unaudited standalone financial results of the Company for the quarter ended 30 June 2026 were reviewed..." | — |
| 2 | Standalone | Note 7 | 340 | "Items of expenditure which exceed 10% of total expenditure are as given below" | — |
| 3 | Standalone | Note 8 | 370 | "The above unaudited standalone financial results are available on the Company's website" | grep miss — no period after "8"; recovered by manual sweep |
| 4 | Consolidated | Note 1 | 594 | "The unaudited consolidated financial results of the Company for the quarter ended 30 June 2026..." | — |
| 5 | Consolidated | Note 7 | 661 | "Items of expenditure which exceed 10% of total expenditure are as given below" | — |
| 6 | Consolidated | Note 8 | 684 | "The above unaudited consolidated financial results are available on the Company's website" | — |

Numbered notes count: corrected grep = 6, manual sweep = 6. **Match.**

### 2a. Unnumbered sub-items bundled inside "Note 1" (both statements) — manual sweep only

Standalone Note 1 (lines 275-308) and Consolidated Note 1 (lines 594-630) each bundle
what would ordinarily be 5-6 separately numbered notes into one unlabelled block. Each
sub-item is a materially distinct disclosure and is enumerated separately here so
nothing inside the bundle is lost to A3/A4.

| # | Statement | Sub-item | Lines | Content | Flags |
|---|-----------|----------|-------|---------|-------|
| 1 | Standalone | 1a | 275-280 | Board/Audit Committee approval statement; limited review, unmodified conclusion | — |
| 2 | Standalone | 1b | 282-287 | Basis of preparation — Ind AS 34, Companies Act 2013 s.133 | — |
| 3 | Standalone | 1c | 289-292 | Q4 FY26 comparative = derived/balancing figures (audited FY26 less reviewed 9M FY26) | — |
| 4 | Standalone | 1d | 294-295 | Single reportable segment — "Health Care Business" (Ind AS 108) | — |
| 5 | Standalone | 1e | 297-300 | Other income breakup — interest on FD Rs.102.24L (Q1FY27); Rs.7.96L (Q4FY26); nil (Q1FY26) | ZERO_STANDING (nil in Q1FY26 comparative) |
| 6 | Standalone | 1f | 302-308 | IPO completion narrative — 2,08,86,200 shares, Rs.79 issue price, listed NSE/BSE Feb 27, 2026 | — |
| 7 | Standalone | IPO utilisation table | 316-337 | Unnumbered table, immediately follows 1f, no note number assigned | NOTE_UNNUMBERED |
| 8 | Consolidated | 1a | 594-599 | Board/Audit Committee approval statement; limited review, unmodified conclusion | — |
| 9 | Consolidated | 1b | 602-606 | Basis of preparation — Ind AS 34, Companies Act 2013 s.133 | — |
| 10 | Consolidated | 1c | 609-613 | Q4 FY26 comparative = derived/balancing figures | — |
| 11 | Consolidated | 1d | 616-617 | Single reportable segment — "Health Care Business" | — |
| 12 | Consolidated | 1e | 619-622 | Other income breakup — same FD interest figures as standalone | ZERO_STANDING (nil in Q1FY26 comparative) |
| 13 | Consolidated | 1f | 624-630 | IPO completion narrative (identical to standalone) | — |
| 14 | Consolidated | IPO utilisation table | 638-659 | Unnumbered table, immediately follows 1f | NOTE_UNNUMBERED |

Unnumbered sub-item count: manual sweep = 14 (7 standalone + 7 consolidated). No grep
anchor exists for this category by design (rule requires manual sweep for exactly this
case).

---

## 3. FINANCIAL STATEMENT LINE ITEMS — STANDALONE P&L (lines 217-264)

Four columns each row: Q1FY27 (Jun 30 2026, Unaudited) | Q4FY26 (Mar 31 2026, "Refer
Note 03") | Q1FY26 (Jun 30 2025, Unaudited) | FY26 (Mar 31 2026, Audited).

| # | Line | Line item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|-----------|--------|--------|--------|------|-------|
| 1 | 222 | Revenue from operations | 1,367.73 | 2,216.60 | 1,227.32 | 7,157.85 | — |
| 2 | 223 | Other income | 112.36 | 17.66 | - | 49.81 | ZERO_STANDING (Q1FY26 dash) |
| 3 | 224 | Total income | 1,480.09 | 2,234.26 | 1,227.32 | 7,207.66 | — |
| 4 | 227 | Cost of rendering services | 105.92 | 219.30 | 109.41 | 844.60 | — |
| 5 | 228 | Purchase of drugs and medical consumables | 92.35 | 85.87 | 119.04 | 450.20 | — |
| 6 | 229 | Changes in inventories of drugs and medical consumables | 28.28 | 34.23 | (27.60) | 24.60 | — |
| 7 | 231 | Employee benefit expenses | 220.67 | 203.07 | 176.44 | 772.43 | — |
| 8 | 232 | Finance costs | 32.26 | 123.62 | 49.69 | 336.19 | — |
| 9 | 233 | Depreciation and amortisation expenses | 67.54 | 60.85 | 58.02 | 243.66 | — |
| 10 | 234 | Other expenses | 703.11 | 547.98 | 434.48 | 1,609.43 | OCR: "$47.98" printed for 547.98 |
| 11 | 235 | Total expenses | 1,250.13 | 1,274.92 | 919.48 | 4,281.11 | — |
| 12 | 236 | Profit before tax | 229.96 | 959.34 | 307.84 | 2,926.55 | — |
| 13 | 240 | Current tax | 61.54 | 226.72 | 76.41 | 728.87 | — |
| 14 | 242 | Taxes for prior years | - | (37.65) | - | (24.62) | ZERO_STANDING (dash Q1FY27 and Q1FY26) |
| 15 | 243 | Deferred tax | 2.07 | (2.87) | (3.65) | (6.48) | — |
| 16 | 244 | Total tax expenses | 63.61 | 186.20 | 72.76 | 697.78 | — |
| 17 | 245 | Profit for the Period/year | 166.35 | 773.14 | 235.08 | 2,228.77 | — |
| 18 | 249 | OCI — items not reclassified to P&L | 3.22 | 2.39 | 2.58 | 10.13 | — |
| 19 | 251 | Income tax on items not reclassified | (0.81) | (0.60) | (0.65) | (2.55) | — |
| 20 | 253 | OCI for the period/year, net of tax | 2.41 | 1.79 | 1.93 | 7.58 | OCR: "7,58" printed for 7.58 |
| 21 | 256 | Total comprehensive income for the Period/year | 168.76 | 774.93 | 237.01 | 2,236.34 | — |
| 22 | 259 | Paid-up equity share capital (FV Rs.5) | 3,639.34 | 3,639.34 | 3,069.72 | 3,639.34 | — |
| 23 | 262 | Other Equity | — | — | — | 11,287.14 | ZERO_STANDING (blank in all 3 quarterly columns, year-end-only presentation) |
| 24 | 264 | EPS Basic and Diluted (Rs.) | 0.23 | 1.24 | 0.39 | 3.59 | — |

Standalone P&L line items: grep (numeric-row pattern) = 24, manual sweep = 24. **Match.**

## 3a. FINANCIAL STATEMENT LINE ITEMS — CONSOLIDATED P&L (lines 503-576)

Same four-column structure as standalone.

| # | Line | Line item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|-----------|--------|--------|--------|------|-------|
| 1 | 512-513 | Revenue from operations | 1,937.66 | 3,035.11 | 1,775.59 | 10,435.70 | — |
| 2 | 514-515 | Other income | 112.36 | 17.74 | - | 53.12 | ZERO_STANDING (Q1FY26 dash) |
| 3 | 516-517 | Total income | 2,050.02 | 3,052.85 | 1,775.59 | 10,488.82 | — |
| 4 | 520-521 | Cost of rendering services | 105.92 | 219.30 | 109.41 | 844.60 | — |
| 5 | 522-523 | Purchase of drugs and medical consumables | 707.37 | 792.87 | 238.14 | 2,992.04 | — |
| 6 | 524-526 | Changes in inventories of drugs and medical consumables | (79.78) | 33.15 | 282.57 | 368.51 | — |
| 7 | 527-528 | Employee benefit expenses | 228.31 | 210.18 | 182.43 | 798.63 | — |
| 8 | 529-530 | Finance costs | 37.62 | 129.03 | 49.74 | 349.16 | — |
| 9 | 531-532 | Depreciation and amortisation expenses | 72.17 | 63.69 | 60.76 | 254.79 | — |
| 10 | 533-534 | Other expenses | 733.43 | 562.41 | 447.76 | 1,661.53 | — |
| 11 | 535-536 | Total expenses | 1,805.04 | 2,010.63 | 1,370.81 | 7,269.26 | — |
| 12 | 537-538 | Profit before tax | 244.98 | 1,042.22 | 404.78 | 3,219.56 | OCR: "244,98" printed for 244.98 |
| 13 | 540-541 | Current tax | 64.65 | 244.70 | 100.39 | 798.24 | — |
| 14 | 543-544 | Taxes for prior years | - | (37.65) | - | (24.62) | ZERO_STANDING (dash Q1FY27 and Q1FY26) |
| 15 | 545-546 | Deferred tax | 2.74 | (0.57) | (3.23) | (2.91) | OCR: closing paren missing on FY26 figure |
| 16 | 547-548 | Total tax expenses | 67.39 | 206.48 | 97.16 | 770.72 | — |
| 17 | 549-550 | Profit for the Period/year | 177.59 | 835.74 | 307.62 | 2,448.85 | — |
| 18 | 552-554 | Profit/(loss) for the period/year from discontinued operation | - | - | (0.24) | (2.75) | ZERO_STANDING (nil Q1FY27 and Q4FY26); ties to EKK Global Private Limited exit — see Section 5 |
| 19 | 557-559 | OCI — items not reclassified to P&L | 3.22 | 2.39 | 2.58 | 10.13 | — |
| 20 | 560-562 | Income tax on items not reclassified | (0.81) | (0.60) | (0.65) | (2.55) | — |
| 21 | 563-566 | OCI for the period/year, net of tax | 2.41 | 1.79 | 1.93 | 7.58 | — |
| 22 | 567-568 | Total comprehensive income for the period/year | 180.00 | 837.53 | 309.31 | 2,453.66 | — |
| 23 | 570-571 | Paid-up equity share capital (FV Rs.5) | 3,639.34 | 3,639.34 | 3,069.72 | 3,639.34 | — |
| 24 | 572-573 | Other Equity | — | — | — | 11,590.87 | ZERO_STANDING (blank in all 3 quarterly columns) |
| 25 | 574-576 | EPS Basic and Diluted (Rs.) | 0.25 | 1.34 | 0.50 | 3.94 | — |

Consolidated P&L line items: grep = 25, manual sweep = 25. **Match.**

Note: standalone EPS (0.23/1.24/0.39/3.59) vs consolidated EPS (0.25/1.34/0.50/3.94) —
consolidated EPS exceeds standalone EPS in every period despite the discontinued-
operations drag in the Q1FY26/FY26 comparatives; carried forward as an item for A3/A4,
not interpreted here.

## 3b. IPO PROCEEDS UTILISATION TABLE (appears identically in both statements)

Standalone: lines 316-337. Consolidated: lines 638-659.

| # | Line (SA / Consol) | Object | Amount per prospectus | Utilised till Jun 30 2026 | Remaining unutilised | Flags |
|---|---|---|---|---|---|---|
| 1 | 324-326 / 646-648 | Funding capex — new IVF Centres | 5,000.00 | 102.95 | 4,897.05 | — |
| 2 | 328-330 / 650-652 | Repayment/pre-payment of outstanding loans | 2,000.00 | 1,807.37 | 192.63 | — |
| 3 | 332 / 654 | General Corporate Purposes | 1,228.19 | 721.02 | 507.17 | — |
| 4 | 333 / 655 | Fresh issue related expenses | 771.89 | 771.89 | - | ZERO_STANDING (fully utilised, nil remaining) |
| 5 | 335 / 657 | Interest on Fixed Deposit | - | - | 14.71 | ZERO_STANDING (structural dash in first 2 columns — FD interest is not a prospectus object) |
| 6 | 337 / 659 | Total | 9,000.08 | 3,403.23 | 5,611.56 | — |

IPO table line items (both statements combined): grep = 12, manual sweep = 12. **Match.**

## 3c. "ITEMS EXCEEDING 10% OF TOTAL EXPENDITURE" TABLE (Note 7, both statements)

Standalone: lines 340-356. Consolidated: lines 661-677.

| # | Line (SA / Consol) | Item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 |
|---|---|---|---|---|---|---|
| 1 | 348-349 / 669-670 | Sales and marketing expenses | 382.96 / 404.33 | 233.70 / 236.70 | 159.72 / 162.72 | 672.97 / 684.97 |
| 2 | 352 / 673 | Rent | 63.12 / 72.12 | 58.64 / 67.64 | 55.32 / 64.32 | 231.76 / 267.76 |
| 3 | 354-355 / 675-676 | Legal and professional fees | 146.36 / 146.95 | 95.53 / 95.71 | 140.27 / 140.27 | 265.83 / 266.71 |

Note the standalone/consolidated gap on "Sales and marketing" and "Rent" (consolidated
higher, reflecting subsidiary Gaudium International's spend); "Legal and professional
fees" Q1FY26 is identical (140.27) across standalone and consolidated, worth a
consistency check by A3/A4.

Note 7 table line items (both statements combined): grep = 6, manual sweep = 6. **Match.**

---

## 4. AUDITOR REPORTS — LIMITED REVIEW (STANDALONE + CONSOLIDATED)

### 4a. Standalone Limited Review Report (lines 123-208)

Opinion type: **unmodified review conclusion** (SRE 2410 — moderate assurance, not an
audit opinion; explicitly: "we do not express an audit opinion," line 159).

| Para | Line | Content | Flags |
|---|---|---|---|
| 1 | 133-138 | Introduction — statement reviewed, entity, period, regulatory basis | — |
| 2 | 140-147 | Management responsibility; Ind AS 34 basis; auditor responsibility to conclude | — |
| 3 | 149-159 | Scope — SRE 2410, moderate assurance, not an audit, no audit opinion expressed | — |
| 4 | 169-176 | **Conclusion** — unmodified: nothing to indicate non-compliance/material misstatement | — |
| 5 | 179-183 | Other Matter — Q1FY26 comparative figures not reviewed, management-compiled | UNAUDITED_COMPARATIVE (Q1FY26 col) |
| 6 | 185-191 | Other Matter — Q4FY26 figures are balancing figures (audited FY26 less reviewed 9M) | — |

Entities reviewed: standalone = Company only (no subsidiary consolidation applicable).
Going Concern paragraph: none present.
Signatory: Sumit Kumar Goyal, Partner, SKGN & Associates LLP, Firm Reg. 023403N/N500052
(lines 196-208). UDIN as extracted: `2654 5UOGNAPTO P3368` (line 206) — **illegible /
OCR-garbled**, does not match standard UDIN format (should be 18 char alphanumeric
starting with membership no. 515406); flag `UDIN_ILLEGIBLE`. Date as extracted:
`|3 Avqust 2026` (line 208) — garbled but resolvable to August 13, 2026, consistent
with board meeting date.

### 4b. Consolidated Limited Review Report (lines 395-494)

Opinion type: **unmodified review conclusion** (same SRE 2410 basis as standalone).
This report is visibly scan-degraded (garbled glyphs at lines 114-118, 433, 457); see
count-test reconciliation note 2 above for the paragraph-numbering recovery method.

| Para | Line | Content | Flags |
|---|---|---|---|
| 1 | 404-411 | Introduction — Statement reviewed, Holding Company + subsidiary ("the Group"), period, regulatory basis | — |
| 2 | 413-421 | Management responsibility; Ind AS 34 basis (number garbled/absent in extraction) | OCR_GARBLED_PARA_NUMBERING |
| 3 | 422-440 | Scope — SRE 2410, moderate assurance, no audit opinion, plus Master Circular Reg 33(8) procedures (number garbled/absent) | OCR_GARBLED_PARA_NUMBERING |
| 4 | 442-453 | Entity list: Holding Company + 2 subsidiaries (number garbled, extracted as bare ".") | OCR_GARBLED_PARA_NUMBERING; see Section 5 for entity detail |
| 5 | 456-464 | **Conclusion** — unmodified, referencing "paragraph 3 above" (number garbled, extracted with no leading digit) | OCR_GARBLED_PARA_NUMBERING |
| 6 | 466-469 | Other Matter — Q1FY26 comparative figures not reviewed, management-compiled (number garbled, extracted as bare ".") | OCR_GARBLED_PARA_NUMBERING; UNAUDITED_COMPARATIVE (Q1FY26 col) |
| 7 | 471-478 | Other Matter — Q4FY26 figures are balancing figures (cleanly numbered "7." in extraction) | — |

Entities reviewed (para 4, lines 442-453): 3 total — see Section 5.
Going Concern paragraph: none present.
Master Circular procedures paragraph (Reg 33(8), lines 438-440): present, folded into
para 3's scope discussion in this extraction.
Signatory: Sumit Kumar Goyal, Partner, SKGN & Associates LLP, Firm Reg. 023403N/N500052
(lines 482-494) — same individual signs both standalone and consolidated reports.
UDIN as extracted: `26525406NZYFITES8sy` (line 492) — **illegible/OCR-garbled**; flag
`UDIN_ILLEGIBLE`. Date as extracted: `{344 Kugad 202 6.` (line 494) — garbled but
resolvable to August 13/14, 2026.

Auditor paragraph totals: standalone 6 + consolidated 7 = **13**.

---

## 5. ENTITIES IN CONSOLIDATION (lines 442-453)

| # | Line | Entity | Relationship | Status | Flags |
|---|------|--------|--------------|--------|-------|
| 1 | 447-448 | Gaudium IVF and Women Health Limited | Holding Company | Active | — |
| 2 | 451 | Gaudium International Private Limited | Subsidiary | Active | — |
| 3 | 452 | EKK Global Private Limited | Subsidiary | **Ceased "till August 05, 2025"** | Entity still listed in the Q1FY27 (Apr-Jun 2026) report's entity table roughly 11 months after its stated cessation date; ties directly to the "Profit/(loss) from discontinued operation" line (consolidated P&L, row 18, lines 552-554) which is nil in the current and immediately preceding quarter and non-zero in the Jun'25/FY26 comparatives. No prior-quarter ledger supplied, so a formal `ENTITY_CHANGE` (added/removed/renamed *this quarter*) cannot be confirmed either way — flagging `PRIOR_LEDGER_UNAVAILABLE` and surfacing the stale-looking retained reference for A3/A4 to chase. |

Entity count: grep (list-marker lines) = 3, manual sweep = 3. **Match.**

---

## 6. ANNEXURES

| # | Label | Line (heading) | Content | Flags |
|---|-------|------|---------|-------|
| A | Annexure A | *not printed* (referenced line 45) | Unaudited standalone + consolidated financial results and both Limited Review Reports — content spans lines 123-702, fully present, but no "Annexure A" section heading appears anywhere in the extracted body | `ANNEXURE_A_LABEL_MISSING` |
| B | Annexure B | 707 | Internal Auditor re-appointment disclosure (Reg 30 / Sch III Part A) — Ram Rattan & Associates, FY2026-27 term. 4 fields: reason for change (716-718), date/term of (re)appointment (719-722), brief profile (723-735), director-relationship disclosure — "Not Applicable" (736-737) | — |
| C | Annexure C | 753 | Secretarial Auditor appointment disclosure — Suresh Nainwal & Company, 5-year term FY2026-27 to FY2030-31, subject to shareholder approval. 4 fields: reason for change (760-766), date of appointment/term (767-779), brief profile incl. proprietor bio and expertise areas (780-823), director-relationship disclosure — "NA" (825-826) | — |
| D | Annexure-D | 841 | Statement on deviation/variation of IPO proceeds, Q1FY27. 12 header fields (Section 7 table below) + 6-row objects table (Section 8) + explanatory Note No. 1 on reallocation (919-934) | — |

Annexure count: corrected grep = 4, manual sweep = 4. **Match.**

---

## 7. ANNEXURE D — DEVIATION/VARIATION STATEMENT HEADER FIELDS (lines 843-871)

| # | Line | Field | Value | Flags |
|---|------|-------|-------|-------|
| 1 | 848 | Name of listed entity | Gaudium IVF and Women Health Limited | — |
| 2 | 850 | Mode of Fund Raising | Public Issue (IPO) | — |
| 3 | 852-854 | Date of Raising Funds | Feb 27, 2026 (listing); Basis of Allotment Feb 25, 2026 | — |
| 4 | 855 | Amount Raised | Rs. 9,000.08 Lakhs (Fresh Issue Gross Proceeds) | — |
| 5 | 857 | Report filed for Quarter ended | Q1 FY2026-27 (Jun 30, 2026) | — |
| 6 | 859 | Monitoring Agency Name | Infomerics Valuation and Rating Limited | — |
| 7 | 860 | Is there a Deviation/Variation in use of funds raised | No | ZERO_STANDING (template field, nil answer) |
| 8 | 862-863 | If yes, pursuant to change in contract/objects terms | Not applicable | ZERO_STANDING |
| 9 | 865 | If Yes, Date of shareholder Approval | Not applicable | ZERO_STANDING |
| 10 | 866 | Explanation for the Deviation/Variation | Not applicable | ZERO_STANDING |
| 11 | 868 | Comments of the Audit Committee after review | None | ZERO_STANDING |
| 12 | 870 | Comments of the auditors, if any | None | ZERO_STANDING |

Header field count: grep = 12, manual sweep = 12. **Match.**

## 8. ANNEXURE D — OBJECTS/DEVIATION TABLE (lines 873-899) and explanatory note

| # | Line | Object | Modified object? | Original allocation | Modified allocation? | Utilised till Jun 30 2026 | Deviation? | Flags |
|---|------|--------|---|---|---|---|---|---|
| 1 | 881-883 | Funding capex — new IVF Centres | No | 5,000.00 | No | 102.95 | No Deviation | — |
| 2 | 884-889 | Repayment/pre-payment of outstanding borrowings | No | 2,000.00 | No | 1,807.37 | No Deviation — "Refer Note No. 1" | Cross-refs explanatory note below |
| 3 | 892-894 | General Corporate Purposes (GCP)* | No | 1,228.19 | No | 721.02 | No Deviation | *footnote at line 901: GCP utilisation stays within 25% of Gross Fresh Issue Proceeds |
| 4 | 895 | Net Proceeds (subtotal) | — | 8,228.19 | — | 2,631.34 | — | — |
| 5 | 897 | Issue Expenses | No | 771.89 | No | 771.89 | No Deviation | — |
| 6 | 899 | Total | — | 9,000.08 | — | 3,403.23 | — | — |

Objects table count: grep = 6, manual sweep = 6. **Match.**

**Explanatory Note No. 1** (lines 919-934): the Rs.2,000.00L earmarked for loan
repayment was fulfilled in full using Rs.1,807.37L (entire outstanding borrowing repaid
as of Jun 30, 2026, none remaining outstanding); Board approved on Aug 13, 2026
reallocation of the balance Rs.192.63L to GCP, confirmed to remain within the 25%-of-
Gross-Proceeds GCP cap and within the 10% permissible deviation limit (lines 930-934).
Definitional boilerplate on what constitutes a "deviation or variation" also appears
(lines 913-916), not a disclosure unit in its own right — noted, not separately rowed.

---

## 9. DIGITAL SIGNATURE / SIGNATORY BLOCKS

| # | Line | Signatory | Designation | Document | Timestamp | Flags |
|---|------|-----------|-------------|----------|-----------|-------|
| 1 | 95-103 | Naveen Kumar | Company Secretary and Compliance Officer (Membership A69788) | Covering / Board Outcome letter | 2026.08.13 18:43:59 +05'30' | Signed ~1h13m after board meeting concluded (05:30 PM) — normal sequencing, not before-conclusion, no flag |
| 2 | 196-208 | Sumit Kumar Goyal | Partner, SKGN & Associates LLP (Membership 515406) | Standalone Limited Review Report | "|3 Avqust 2026" (garbled, resolves to Aug 13, 2026) | UDIN garbled — see Section 4a |
| 3 | 380-386 | Dr. Manika Khanna | Chairperson and Managing Director (DIN 07090907) | Standalone financial results | August 13, 2026 | — |
| 4 | 482-494 | Sumit Kumar Goyal | Partner, SKGN & Associates LLP (Membership 515406) | Consolidated Limited Review Report | "{344 Kugad 202 6." (garbled, resolves to Aug 13/14, 2026) | UDIN garbled — see Section 4b |
| 5 | 690-702 | Dr. Manika Khanna | Chairperson and Managing Director (DIN 07090907) | Consolidated financial results | August 13, 2026 | — |

Signature block count: manual sweep only (no numeric anchor) = 5.

Also noted, not counted as a signature block: "For Identification only" auditor
watermark stamps appear on financial-statement pages at lines 360-362 (standalone) and
581-583 (consolidated) — routine identification stamping, not a signature.

---

## SUMMARY COUNTS

| Category | Count |
|---|---|
| Board Outcome agenda items | 5 |
| Numbered notes (standalone + consolidated) | 6 |
| Unnumbered note sub-items (bundled in Note 1, both statements) | 14 |
| Auditor report paragraphs (standalone 6 + consolidated 7) | 13 |
| Entities in consolidation | 3 |
| Financial statement line items — standalone P&L | 24 |
| Financial statement line items — consolidated P&L | 25 |
| Financial statement line items — IPO utilisation table (both statements) | 12 |
| Financial statement line items — Note 7 (>10% expenditure) table (both statements) | 6 |
| Financial statement line items — Annexure D header fields | 12 |
| Financial statement line items — Annexure D objects table | 6 |
| **Total line items (financial tables, all)** | **85** |
| Annexures | 4 |
| Digital signature blocks | 5 |
| **ZERO_STANDING flagged rows** | **15** |

```yaml
stage: A2-enumerator
company: "GAUDIUMIVF"
quarter: "q1fy27"
doctype: "results"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/gaudiumivf-q1fy27/work/ledger_results_gaudiumivf_q1fy27.md"
counts:
  notes: 20
  line_items: 85
  zero_standing: 15
  agenda_items: 5
  auditor_paras: 13
  entities: 3
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, NOTE_UNNUMBERED, OCR_GARBLED_PARA_NUMBERING, UDIN_ILLEGIBLE, ANNEXURE_A_LABEL_MISSING, PRIOR_LEDGER_UNAVAILABLE, UNAUDITED_COMPARATIVE]
gate_a2: pass
mismatch_note: ""
```
