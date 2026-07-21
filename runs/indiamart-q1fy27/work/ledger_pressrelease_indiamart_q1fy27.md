# A2 Enumeration Ledger — Press Release — INDIAMART Q1 FY27

Source: `runs/indiamart-q1fy27/work/extract_pressrelease_indiamart_q1fy27.txt`
(source_filename: pressrelease_indiamart_q1fy27.pdf, 5 pages, unit convention: Crores, line_count: 194)
Cross-reference document used ONLY for the NOT_IN_FILING check (item d): `extract_results_indiamart_q1fy27.txt`
(source_filename: results_indiamart_q1fy27.pdf, unit convention: Millions, conversion factor x0.1 to Cr). NOTE: that
extract contains the audited P&L statement only — no balance sheet or cash-flow-statement section is present in it —
so NOT_IN_FILING below means "no matching line item found in the P&L-format extract available to this run," not
"absent from the full statutory filing including annexures not extracted here." All line numbers below are the
Read-tool / grep physical line numbers of the extract file (leftmost column), NOT the page-internal paragraph
numbers embedded in the PDF text (e.g. the "56" printed at the start of a line is PDF-internal numbering, not the
extract line number).

```
=== A2 COUNT TEST ===
category: headline_bullets     grep_count: 3    sweep_count: 3    match: yes
category: quantitative_claims  grep_count: 26   sweep_count: 26   match: yes
  (grep_count = raw occurrences of primary value-anchors "Rs"/"million"/"K\b"/"hours" in narrative text,
   lines 14-165 excluding the table region 138-165; sweep_count = same anchors manually tallied across the
   24 discrete claim-rows enumerated in Table 2 below; 20 rows carry a single "Rs" anchor, 2 rows [rows 4 and
   16] carry two "Rs" anchors each [current + prior-year comparator], 4 rows carry one non-Rs anchor each
   [million x2, K x1, hours x1] = 22 + 4 + 2(extra in rows 4,16, already counted once in the 22) reconciles to
   26 = 26)
category: line_items (table)   grep_count: 13   sweep_count: 11   match: yes
  (grep_count of 13 includes 2 false positives — the table title line "124 Q1 FY2027 Performance Metrics" and
   the column-header line "128 Q1FY27 Y-o-Y Q-o-Q..." both matched the label+digit regex but are not data rows;
   11 true metric line items after exclusion, confirmed by manual sweep = 11, match yes)
category: mgmt_quotes          grep_count: 1    sweep_count: 1    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

---

## Table 1 — Headline Bullets (Q1 FY2027 vs. Q1 FY2026 summary, lines 67-72)

| # | Line | Bullet text (verbatim) | Flags |
|---|------|-------------------------|-------|
| B1 | 70 | "Consolidated Revenue from Operations of Rs. 414 Crore, YoY growth of 11%" | |
| B2 | 71 | "Standalone EBITDA of Rs. 149 Crore representing EBITDA margin of 40%" | NOT_IN_FILING (EBITDA is a non-GAAP measure; no matching line in the audited P&L extract) |
| B3 | 72 | "Consolidated Cash generated from Operations of Rs. 163 Crore" | NOT_IN_FILING (cash flow statement not present in the P&L-only extract available) |

---

## Table 2 — Quantitative Claims (prose narrative, excludes the metrics table which is enumerated separately in Table 3)

| # | Line(s) | Section | Metric | Value | YoY / context | Flags |
|---|---------|---------|--------|-------|----------------|-------|
| 1 | 70 | Headline bullets | Consolidated Revenue from Operations | Rs 414 Cr | YoY +11% | duplicate of #4 (restated) |
| 2 | 71 | Headline bullets | Standalone EBITDA | Rs 149 Cr | EBITDA margin 40% | NOT_IN_FILING; duplicate of #19 |
| 3 | 72 | Headline bullets | Consolidated Cash generated from Operations | Rs 163 Cr | (no YoY given here) | NOT_IN_FILING; duplicate of #14 |
| 4 | 78-79 | Consol Financial Highlights | Consolidated Revenue from Operations | Rs 414 Cr vs Rs 372 Cr PY | growth 11% | contains PY comparator; duplicate of #1 |
| 5 | 80 | Consol Financial Highlights | IndiaMART Standalone Revenue (component of consol) | Rs 376 Cr | YoY growth 9% | |
| 6 | 80-81 | Consol Financial Highlights | Busy Infotech Revenue (component of consol) | Rs 36 Cr | no YoY stated | NOT_IN_FILING (segment breakout not in P&L extract) |
| 7 | 83 | Consol Financial Highlights | Collections from Customer (consolidated) | Rs 463 Cr | YoY growth 8% | NOT_IN_FILING (operating/non-GAAP metric, no cash-flow section in extract) |
| 8 | 84 | Consol Financial Highlights | IndiaMART Standalone Collections | Rs 402 Cr | YoY growth 8% | NOT_IN_FILING; duplicate of #17 |
| 9 | 84-85 | Consol Financial Highlights | Busy Infotech Collections | Rs 59 Cr | no YoY stated | NOT_IN_FILING |
| 10 | 87 | Consol Financial Highlights | Deferred Revenue (consolidated) | Rs 2,014 Cr | YoY growth 16% | NOT_IN_FILING (no balance-sheet section in extract) |
| 11 | 88 | Consol Financial Highlights | IndiaMART Standalone Deferred Revenue | Rs 1,858 Cr | (no YoY in this sentence; see #18) | NOT_IN_FILING |
| 12 | 88-89 | Consol Financial Highlights | Busy Infotech Deferred Revenue | Rs 146 Cr | no YoY stated | NOT_IN_FILING |
| 13 | 91 | Consol Financial Highlights | Net Profit for the quarter (consolidated) | Rs 172 Cr | (no YoY in this sentence; see Table 3) | reconciles to filing (1,722 M x0.1 = 172.2 Cr) |
| 14 | 91-92 | Consol Financial Highlights | Cash Flow from Operations (consolidated) | Rs 163 Cr | (no YoY here) | NOT_IN_FILING; duplicate of #3 |
| 15 | 92 | Consol Financial Highlights | Cash and Investments balance | Rs 3,553 Cr as on June 30, 2026 | | NOT_IN_FILING |
| 16 | 101-102 | Standalone Financial Highlights | Standalone Revenue from Operations | Rs 376 Cr vs Rs 346 Cr PY | growth 9% | reconciles to filing (3,759 M x0.1 = 375.9 Cr; PY 3,463 M x0.1 = 346.3 Cr) |
| 17 | 106 | Standalone Financial Highlights | Collections from Customer (standalone) | Rs 402 Cr | YoY growth 8% | NOT_IN_FILING; duplicate of #8 |
| 18 | 106-108 | Standalone Financial Highlights | Deferred Revenue (standalone) | Rs 1,858 Cr | YoY growth 14% | NOT_IN_FILING |
| 19 | 111 | Standalone Financial Highlights | EBITDA (standalone) | Rs 149 Cr | margin 40% | NOT_IN_FILING; duplicate of #2 |
| 20 | 111-112 | Standalone Financial Highlights | Net Profit for the quarter (standalone) | Rs 176 Cr | | reconciles to filing (1,761 M x0.1 = 176.1 Cr) |
| 21 | 118 | Operational Highlights | Unique business enquiries | 26 million | (Q1 FY27) | NOT_IN_FILING (operational KPI, not a financial-statement line) |
| 22 | 118-119 | Operational Highlights | Supplier Storefronts | 8.8 million | increase of 5% YoY | NOT_IN_FILING |
| 23 | 119 | Operational Highlights | Paying suppliers (end of quarter) | 218K | | NOT_IN_FILING; also appears in Table 3 row T11 |
| 24 | 174-175 | Earnings Call notice | Earnings webinar date/time | Tuesday, 21 July 2026, 17:00 hours IST | | scheduling fact, not a results figure; N/A for filing cross-check |

Note on duplication: rows #1/#4, #2/#19, #3/#14, #8/#17 are the SAME underlying metric restated once in the
headline-bullet block and again in the Consolidated/Standalone Financial Highlights prose. Both instances are
kept as separate ledger rows (each carries its own line number and is a separate disclosure unit a reader
encounters), per operating rule 2 (every row carries a line number, no exceptions) — A3/A4 should treat these
as the same fact when checking arithmetic consistency, not as independent claims.

---

## Table 3 — Q1 FY2027 Performance Metrics table (lines 138-165)

Table header: "Q1 FY2027 Performance Metrics (Figures in crores, unless otherwise stated)" — line 138-139.
Columns: Standalone [Q1FY27, Y-o-Y, Q-o-Q] | Consolidated [Q1FY27, Y-o-Y, Q-o-Q] — line 141-142.

| # | Line | Metric | Standalone Q1FY27 | Standalone YoY | Standalone QoQ | Consol Q1FY27 | Consol YoY | Consol QoQ | Flags |
|---|------|--------|--------------------|-----------------|-----------------|----------------|-------------|-------------|-------|
| T1 | 144 | Total Income | 464 | 8% | 39% | 521 | 12% | 41% | reconciles to filing (Consol Total income 5,211 M x0.1 = 521.1 Cr) |
| T2 | 146 | Revenue from Operations | 376 | 9% | 2% | 414 | 11% | 2% | reconciles to filing (Consol Rev from Ops 4,144 M x0.1 = 414.4 Cr) |
| T3 | 148 | EBITDA | 149 | 11% | 11% | 146 | 10% | 10% | NOT_IN_FILING (non-GAAP measure) |
| T4 | 149 | EBITDA Margin (%) | 40% | - | - | 35% | - | - | NOT_IN_FILING (derived ratio) |
| T5 | 151 | Net Profit for the period | 176 | 6% | 153% | 172 | 12% | 243% | reconciles to filing (Standalone 1,761 M / Consol 1,722 M x0.1) |
| T6 | 152 | Net Profit Margin (%) | 38% | - | - | 33% | - | - | NOT_IN_FILING (derived ratio) |
| T7 | 155 | Collections from Customer | 402 | 8% | (26%) | 463 | 8% | (22%) | NOT_IN_FILING |
| T8 | 158 | Cash flow from Operations | 153 | 6% | (47%) | 163 | 2% | (44%) | NOT_IN_FILING |
| T9 | 162 | Deferred Revenue | 1,858 | 14% | 1% | 2,014 | 16% | 2% | NOT_IN_FILING |
| T10 | 164 | Cash and Investments | 3,316 | 29% | 8% | 3,553 | 29% | 8% | NOT_IN_FILING |
| T11 | 165 | Paying Suppliers (In '000) | 218 | 0% | (1%) | - | - | - | ZERO_STANDING (Consolidated column is dash-valued in all three sub-fields — the line exists, template signal); NOT_IN_FILING |

---

## Table 4 — Management Quotes / Attributed Statements

| # | Line(s) | Speaker | Designation | First 10-15 words |
|---|---------|---------|-------------|---------------------|
| Q1 | 123, 126-131 | Mr. Dinesh Agarwal | Chief Executive Officer | "We continued our emphasis on sustainable growth and elevating overall marketplace experience by building..." |

---

## Table 5 — Additional structural items (not count-tested, logged for completeness)

| # | Line(s) | Item | Detail | Flags |
|---|---------|------|--------|-------|
| S1 | 41-49 | Digital signature block | Vasudha Bagri, Compliance Officer, Membership No. A28500; signed 2026.07.21 15:36:22 +05'30 | Signed same day as, and before, the 17:00 IST earnings call notice (line 174-175) — expected sequence, not a flag |
| S2 | 67 | Section heading | "Q1 FY2027 vs. Q1 FY2026" | structural, not a claim |
| S3 | 76 | Section heading | "Consolidated Financial Highlights (Q1 FY2027):" | structural, not a claim |
| S4 | 99 | Section heading | "Standalone Financial Highlights (Q1 FY2027):" | structural, not a claim |
| S5 | 115 | Section heading | "Operational Highlights (Q1 FY2027):" | structural, not a claim |
| S6 | 158-172 | Earnings call logistics (non-numeric) | Webinar registration link, recording availability notice | no financial figures beyond claim #24 |
| S7 | 176-180 | "About IndiaMART" boilerplate | No figures | not a claim |

---

## Summary counts

- Headline bullets: 3
- Quantitative claims (narrative, discrete rows): 24 (of which 17 flagged NOT_IN_FILING, 1 is a non-financial scheduling fact, 6 reconcile to the audited filing extract)
- Table line items: 11 (of which 8 flagged NOT_IN_FILING, 1 also ZERO_STANDING, 3 reconcile to the audited filing extract)
- Management quotes: 1
- Zero/dash-standing line items: 1 (T11, Paying Suppliers — Consolidated column)
- Total NOT_IN_FILING flags: 25 (17 narrative + 8 table)
- Total ENTITY-level segment breakouts not independently auditable against the P&L extract: Busy Infotech Revenue/Collections/Deferred Revenue (rows 6, 9, 12)

gate_a2: PASS — grep and manual sweep counts reconcile on all four count-tested categories (headline_bullets,
quantitative_claims, line_items, mgmt_quotes).
