# A2 ENUMERATION LEDGER — GNG Electronics Limited (EBGNG) — Q1 FY27 — Investor Presentation

Source: `/home/user/inflection-pipeline/runs/ebgng-q1fy27/work/extract_presentation_ebgng_q1fy27.txt`
Extraction: pymupdf 1.28, born-digital workaround (poppler/tesseract unavailable), 8 pages / 285 extract lines, page_coverage 100%, slide 6 chart visually verified per header.
Prior-quarter ledger: not provided — `DROPPED_SLIDE` check cannot be performed; flagged `NO_PRIOR_DECK`.

```
=== A2 COUNT TEST ===
category: slides                    grep_count: 8    sweep_count: 8    match: yes
category: slide7_line_items         grep_count: 16   sweep_count: 16   match: yes
category: slide7_numeric_cells      grep_count: 82   sweep_count: 82   match: yes
category: slide6_kpi_numbers        grep_count: 10   sweep_count: 10   match: yes
category: slide6_axis_scale_labels  grep_count: 20   sweep_count: 20   match: yes (non-disclosure, excluded from main tally)
category: slide5_kpi_numbers        grep_count: 6    sweep_count: 6    match: yes
category: slide5_qual_claims        grep_count: 9    sweep_count: 9    match: yes
category: slide1_disclosure_facts   grep_count: 10   sweep_count: 10   match: yes
category: slide1_excluded_address   grep_count: 2    sweep_count: 2    match: yes (non-disclosure, excluded from main tally)
category: slide8_numbers            grep_count: 1    sweep_count: 1    match: yes
category: safe_harbor_clauses       grep_count: 13   sweep_count: 13   match: yes (5 clauses + 7 lettered risk factors (a)-(g) + 1 closing clause)
category: absent_disclosure_cats    grep_count: 5    sweep_count: 5    match: yes (structural silence rows, not present in text — see Table 8)
category: total_kpi_numbers_deck    grep_count: 109  sweep_count: 109  match: yes (=10+6+10+82+1, slides 1/5/6/7/8, excludes axis-scale + address artifacts)
gate_a2: pass
=== END COUNT TEST ===
```

Methodology note: grep passes used `grep -n -c "^\[page"` for slide markers; `awk` block-isolation per `[page N]` marker plus a value/label-pattern grep (`^[0-9,.\-]+%?$|^-?[0-9]+ bps$` vs header/label exclusion) for the slide-7 table; targeted digit-token greps (`grep -n -o -E '[0-9]+([,.][0-9]+)*%?( bps)?'`) scoped to each slide's line range for slides 1, 5, 6, 8; and direct-text confirmation for the safe-harbor lettered risk factors (grep regex under-matched one lettered item due to case handling, corrected by manual line read — both methods converge on 7). Every grep count below was independently cross-checked against a manual line-by-line sweep of the same slide block; all rows reconciled per GATE A2 above.

---

## TABLE 1 — Slides (content type inventory)

| # | Slide | Title / heading | Content type | Line range | Flags |
|---|-------|------------------|--------------|------------|-------|
| 1 | 1 | Reg-30 cover letter to NSE/BSE | text (regulatory letter) | 16-79 | — |
| 2 | 2 | "Q1 FY27 \| Investor Presentation" title page | text (cover) | 80-83 | — |
| 3 | 3 | Safe Harbor | text (disclaimer) | 84-104 | — |
| 4 | 4 | "KEY HIGHLIGHTS – Q1 FY27" | text (section divider) | 105-109 | — |
| 5 | 5 | Management Comment (Mr. Sharad Khandelwal, MD) | text (qualitative + embedded KPIs) | 110-136 | — |
| 6 | 6 | Consolidated Financial Highlights | chart (3 bar/column charts: Revenue, EBITDA & margin, PAT & margin) | 137-179 | — |
| 7 | 7 | Consolidated Income Statement – Quarterly | table (16 line items x up to 6 periods) | 180-287 | — |
| 8 | 8 | Thank You / contact page | text (IR contacts) | 288-300 | — |

Slides total: 8 (grep on `^\[page` markers = 8; manual sweep = 8; match).
Dropped-slide check vs prior quarter: **not performable** — no prior-quarter ledger path was supplied. Flag `NO_PRIOR_DECK`.

---

## TABLE 2 — Slide 1: Reg-30 cover letter disclosure units

| # | Disclosure unit | Line(s) | Value | Flags |
|---|------------------|---------|-------|-------|
| 1.1 | Letter date | 20 | July 30, 2026 | — |
| 1.2 | Addressee 1 | 22-24 | National Stock Exchange of India Limited, Exchange Plaza, ... Mumbai 400051 | — |
| 1.3 | Addressee 1 pin code | 24 | 400051 | — |
| 1.4 | Addressee 2 | 25-28 | BSE Limited, Phiroze Jeejeebhoy Towers, Dalal Street, Mumbai 400001 | — |
| 1.5 | Addressee 2 pin code | 28 | 400001 | — |
| 1.6 | NSE Symbol (identifier, non-numeric) | 29 | EBGNG | — |
| 1.7 | Scrip Code | 30 | 544455 | — |
| 1.8 | Regulatory citation: Regulation 30 | 32, 38 | "Regulation 30" (cited twice — subject line and body) | — |
| 1.9 | Regulatory citation: Part A of Schedule III | 38 | "Part A of Schedule III" | — |
| 1.10 | Regulatory citation: SEBI LODR year | 33-34, 39-40 | "Regulations, 2015" (cited three times) | — |
| 1.11 | Earnings call schedule | 41 | Thursday, July 30, 2026, 06:00 PM (IST) | — |
| 1.12 | Signatory membership number | 54 | Membership No. A59547 | — |
| 1.13 | Signatory | 52-54 | Sarita Vishwakarma, Company Secretary & Compliance Officer | — |
| 1.14 | Digital signature timestamp | 73-78 | SARITA TUFANI VISHWAKARMA, digitally signed, Date: 2026.07.30 17:01:22 +05'30' | `SIGNATURE_TIMESTAMP_NOTED` — no board-meeting time is stated in this doctype to cross-check against (unlike a Board Outcome letter); no anomaly detectable from this document alone |

Excluded from disclosure count as non-substantive address artifacts (still enumerated here for completeness, per "enumerate everything"):
| # | Item | Line | Flags |
|---|------|------|-------|
| 1.15 | Floor number in NSE address | 23 | "5th Floor" | `NON_DISCLOSURE_ADDRESS` |
| 1.16 | Block code in NSE address | 23 | "C-1, Block G" | `NON_DISCLOSURE_ADDRESS` |

Distinct disclosure facts (1.1-1.14, deduped by fact, not by mention): 10 (1.2/1.4 are addressee names not numbers, 1.6 is alphabetic, 1.13 is a name — the "numbers" sub-count of this table is 10: date, pin1, pin2, scrip, Reg30, ScheduleIII, 2015, earnings-call datetime, membership no., signature timestamp).

---

## TABLE 3 — Slide 3: Safe Harbor (disclaimer / footnote-equivalent)

| # | Clause | Line(s) | Summary (first ~12 words) | Flags |
|---|--------|---------|----------------------------|-------|
| 3.1 | Responsibility / binding clause | 86-87 | "prepared by and is the sole responsibility of GNG Electronics Limited... agreeing to be bound" | — |
| 3.2 | No offer/inducement/solicitation clause | 88-90 | "does not constitute or form part of any offer or invitation or inducement to sell" | — |
| 3.3 | Not a prospectus clause | 90-91 | "not intended to be a prospectus or offer document under the applicable laws" | — |
| 3.4 | No representation/warranty; no obligation to update | 91-94 | "No representation or warranty... is made as to... fairness, accuracy, completeness" | — |
| 3.5 | Forward-looking statement definition + identifying terminology | 95-98 | defines FLS; lists identifying words ("aim", "anticipate", "believe"..."would") | `FORWARD_LOOKING_UNQUANTIFIED` (frames all of slide 5's forward language) |
| 3.6a | Risk factor (a) | 98-100 | "our ability to successfully implement our strategy" | — |
| 3.6b | Risk factor (b) | 100 | "our growth and expansion plans" | — |
| 3.6c | Risk factor (c) | 100 | "changes in regulatory norms applicable to the Company" | — |
| 3.6d | Risk factor (d) | 100-101 | "technological changes" | — |
| 3.6e | Risk factor (e) | 101 | "investment income" | — |
| 3.6f | Risk factor (f) | 101 | "cash flow projections" | — |
| 3.6g | Risk factor (g) | 101 | "other risks" | — |
| 3.7 | General information purpose / no obligation to notify of changes | 102-103 | "for general information purposes only... Company may alter, modify or otherwise change" | — |

Total safe-harbor clauses: 13 (5 narrative clauses + 7 lettered risk factors + 1 closing clause). Grep/sweep reconciled at 13 (grep regex under-matched item (d) on first pass; corrected by direct text read — both converge at 7 lettered items).

---

## TABLE 4 — Slide 5: Management Comment — embedded numeric KPIs

| # | KPI | Line(s) | Value | Flags |
|---|-----|---------|-------|-------|
| 5.1 | Revenue | 117 | ₹412.5 crore | duplicated on slide 6 (chart) and slide 7 (table) |
| 5.2 | Revenue growth YoY | 118 | 32% YoY | slide 7 table states 32.1% — 0.1pp rounding difference between prose (32%) and table (32.1%); flag `ROUNDING_VARIANCE` |
| 5.3 | EBITDA margin | 118 | 12.8% | duplicated on slide 6 and slide 7 |
| 5.4 | EBITDA margin improvement | 119 | 156 bps YoY | matches slide 7 EBITDA Margins row exactly |
| 5.5 | Country reach | 122 | 49 countries | not disclosed elsewhere in deck (no prior-quarter comparison available) |
| 5.6 | Customer touchpoints | 122 | 5,100+ | not disclosed elsewhere in deck; "over 5,100" is an approximation, not an exact figure |

Speaker identification: Mr. Sharad Khandelwal, Managing Director (lines 111-112) — sole quoted management voice in this document; no analyst/Q&A content exists in this doctype. Flag `SINGLE_SPEAKER_ONLY` (expected for an investor-presentation doctype, noted for completeness, not itself an anomaly).

## TABLE 4B — Slide 5: Qualitative strategic claims (non-numeric)

| # | Claim | Line(s) | Flags |
|---|-------|---------|-------|
| 5.7 | Structural shift narrative: global ICT industry shifting to professionally refurbished computing, driven by enterprise adoption, cost optimization, sustainability | 114-117 | `FORWARD_LOOKING_UNQUANTIFIED` |
| 5.8 | "Strong note" start-to-FY27 framing (ties to 5.1/5.2 numbers) | 117 | — |
| 5.9 | Global presence expansion / supplier base diversification narrative | 121-123 | ties to 5.5/5.6 numbers, no target/plan figure given |
| 5.10 | Dealer meets across India | 123-124 | no count, date, or location given |
| 5.11 | EB Elite Program (new distributor initiative, named but undescribed) | 124-125 | `NO_QUANTIFIED_TARGET` — no enrolment, revenue contribution, or timeline figure disclosed |
| 5.12 | Strategic partnership with Redington Limited | 126-127 | `NO_QUANTIFIED_TARGET` — no deal terms, revenue contribution, exclusivity, or duration disclosed; candidate for A3/A4 follow-up on materiality |
| 5.13 | Forward confidence statement: long-term opportunity in refurbished ICT industry | 128-131 | `FORWARD_LOOKING_UNQUANTIFIED` |
| 5.14 | Capability claim: "integrated global platform, expanding distribution ecosystem, strong execution capabilities" | 132-133 | `FORWARD_LOOKING_UNQUANTIFIED` |
| 5.15 | Commitment statement: sustainable growth, improving profitability, long-term stakeholder value | 133-135 | `FORWARD_LOOKING_UNQUANTIFIED` — no explicit FY27 numeric guidance anywhere in this deck (see Table 8) |

Slide 5 qualitative claims count: 9 (5.7-5.15).

---

## TABLE 5 — Slide 6: Consolidated Financial Highlights (chart)

| # | Metric | Line | Q1 FY26 | Q1 FY27 | Flags |
|---|--------|------|---------|---------|-------|
| 6.1 | Revenue from operations (Rs. Cr) | 138-139 | 312.3 | 412.5 | matches slide 7 exactly |
| 6.2 | EBITDA (Rs. Cr) | 143-144 | 35.2 | 52.9 | matches slide 7 exactly |
| 6.3 | EBITDA Margin (%) | 145-146 | 11.3% | 12.8% | matches slide 7 exactly |
| 6.4 | PAT (Rs. Cr) | 162-163 | 18.5 | 28.9 | matches slide 7 exactly |
| 6.5 | PAT Margin (%) | 164-165 | 5.9% | 7.0% | matches slide 7 exactly |

Slide 6 KPI numbers: 10 (5 metrics x 2 periods). All ten cross-checked against slide 7's table — zero variance found (unlike the 32%/32.1% prose/table variance on slide 5).

Chart axis-scale gridline labels (non-disclosure, listed for completeness, excluded from KPI count):
| # | Chart | Line(s) | Values | Flags |
|---|-------|---------|--------|-------|
| 6.6 | EBITDA chart y-axis scale | 147-157 | 10,15,20,25,30,35,40,45,50,55,60 (11 values) | `CHART_AXIS_LABEL` — non-disclosure |
| 6.7 | PAT-margin chart y-axis scale | 166-174 | 0.00% through 8.00% in 1pp steps (9 values) | `CHART_AXIS_LABEL` — non-disclosure |

Axis-scale labels total: 20 (11 + 9), separately reconciled, excluded from the 109-number deck total.

---

## TABLE 6 — Slide 7: Consolidated Income Statement – Quarterly (full table, 16 line items)

Columns: Q1 FY27 | Q1 FY26 | YoY | Q4 FY26 | QoQ | FY26 (Rs Cr; % and bps as stated)

| # | Line item | Line(s) | Q1 FY27 | Q1 FY26 | YoY | Q4 FY26 | QoQ | FY26 | Flags |
|---|-----------|---------|---------|---------|-----|---------|-----|------|-------|
| 7.1 | Revenue from operations | 188-194 | 412.5 | 312.3 | 32.1% | 651.7 | -36.7% | 1,891.1 | prose (slide 5) states "32%" vs table "32.1%" — `ROUNDING_VARIANCE` (see 5.2) |
| 7.2 | Other Income | 195-199 | 3.5 | 2.9 | 0.6 | 4.3 | (blank) | (blank) | `NO_YOY_QOQ_SHOWN`; note value "0.6" in the YoY position is an absolute change in Rs Cr, not a percentage (inconsistent format vs row 7.1's YoY%) — flag `FORMAT_INCONSISTENCY`; FY26 full-year Other Income value not disclosed |
| 7.3 | Total income | 200-206 | 416.0 | 315.1 | 32.0% | 652.3 | -36.2% | 1,895.4 | — |
| 7.4 | Gross Profit | 207-213 | 101.7 | 66.7 | 52.4% | 125.3 | -18.8% | 380.9 | — |
| 7.5 | Gross Profit Margins | 214-220 | 24.6% | 21.4% | 329 bps | 19.2% | 542 bps | 20.1% | — |
| 7.6 | Employee benefits expenses | 221-225 | 31.9 | 22.3 | (blank) | 33.0 | (blank) | 104.6 | `NO_YOY_QOQ_SHOWN` |
| 7.7 | Other expenses | 226-230 | 20.4 | 12.1 | (blank) | 28.9 | (blank) | 80.2 | `NO_YOY_QOQ_SHOWN` |
| 7.8 | EBITDA | 231-237 | 52.9 | 35.2 | 50.4% | 64.0 | -17.3% | 200.5 | — |
| 7.9 | EBITDA Margins | 238-244 | 12.8% | 11.3% | 156 bps | 9.8% | 300 bps | 10.6% | — |
| 7.10 | Depreciation and amortization expenses | 245-249 | 3.3 | 2.0 | (blank) | 3.2 | (blank) | 10.4 | `NO_YOY_QOQ_SHOWN` |
| 7.11 | Finance cost | 250-254 | 13.9 | 10.7 | (blank) | 14.4 | (blank) | 42.4 | `NO_YOY_QOQ_SHOWN` |
| 7.12 | PBT | 255-261 | 35.7 | 22.5 | 59.1% | 46.4 | -22.9% | 147.7 | — |
| 7.13 | Less: tax expenses | 262-266 | 6.8 | 4.0 | (blank) | 4.2 | (blank) | 15.7 | `NO_YOY_QOQ_SHOWN` |
| 7.14 | PAT | 267-273 | 28.9 | 18.5 | 56.2% | 42.1 | -31.3% | 132.0 | — |
| 7.15 | PAT Margins | 274-280 | 7.0% | 5.9% | 108 bps | 6.5% | 55 bps | 7.0% | — |
| 7.16 | EPS Basic | 281-285 | 2.54 | 1.91 | (blank) | 3.70 | (blank) | 11.58 | `NO_YOY_QOQ_SHOWN`; no EPS growth % shown despite PAT growth of 56.2% disclosed above it — implies a share-count change not surfaced; candidate for A3/A4 dilution check |

Line items: 16 (grep on Particulars labels within the `[page 7]` block = 16; manual sweep = 16; match).
Numeric data cells: 82 (9 rows carry the full 6-column set = 54; 7 rows carry only 4 columns [Q1FY27, Q1FY26, Q4FY26, FY26, no YoY%/QoQ%] = 28; 54+28=82). Zero/nil/dash-valued rows: **none** — every cell present in this table carries a nonzero populated value. No `ZERO_STANDING` flags apply to this table.

---

## TABLE 7 — Slide 8: Thank You / contact page

| # | Item | Line | Value | Flags |
|---|------|------|-------|-------|
| 8.1 | Company contact | 291-292 | GNG Electronics Limited, Ms. Sarita Tufani Vishwakarma | — |
| 8.2 | Phone number | 293 | +91 22 3123 6588 | — |
| 8.3 | Email | 294 | compliance@electronicsbazaar.com | — |
| 8.4 | IR advisor firm | 296 | Adfactors PR Ltd | — |
| 8.5 | IR advisor contacts | 297-299 | Mr. Sumit Kinikar / Ms. Disha Mody, emails | — |

Numbers on slide 8: 1 (the phone number).

---

## TABLE 8 — Absent disclosure categories (structural silence, F16 candidates for A3)

The entire 8-slide deck contains none of the following, at any line. These are enumerated as absence-rows per the operating instruction to never drop a nil/absent disclosure signal; there is no line number to cite because the category does not appear anywhere across lines 16-300 (full document body).

| # | Absent category | Present in deck? | Flags |
|---|------------------|-------------------|-------|
| A.1 | Balance sheet (standalone or consolidated) | No | `DISCLOSURE_ABSENT` — no debt, net worth, reserves, or asset figures anywhere in the deck |
| A.2 | Cash flow statement | No | `DISCLOSURE_ABSENT` — no operating/investing/financing cash flow, no explicit cash conversion figure |
| A.3 | Segment / geography split (domestic vs. export revenue) | No | `DISCLOSURE_ABSENT` — the "49 countries" claim (5.5) is qualitative reach only, no revenue-by-geography breakdown |
| A.4 | Debt, working capital, or inventory figures | No | `DISCLOSURE_ABSENT` — Finance cost (7.11) is disclosed as a P&L expense line but no debt quantum, tenor, or cost-of-debt %; no inventory days or WC cycle figure |
| A.5 | Explicit forward FY27 numeric guidance | No | `DISCLOSURE_ABSENT` — slide 5's forward language (5.13-5.15) is entirely qualitative; no revenue/EBITDA/margin/capex target number for FY27 stated anywhere |

Absent-category count: 5 (grep for balance-sheet/cash-flow/segment/debt/guidance keyword stems across the full extract returned zero matches for each category; manual sweep of all 8 slides independently confirms zero matches for each; both methods converge at 5/5).

---

## GATE A2 RECONCILIATION SUMMARY

All 13 count-test categories (slides, slide7 line items, slide7 numeric cells, slide6 KPI numbers, slide6 axis labels, slide5 KPI numbers, slide5 qualitative claims, slide1 disclosure facts, slide1 excluded address items, slide8 numbers, safe-harbor clauses, absent-disclosure categories, total deck KPI numbers) show grep_count = sweep_count. No mismatch. **GATE A2: PASS.**

Flags raised across this ledger: `NO_PRIOR_DECK`, `NON_DISCLOSURE_ADDRESS`, `CHART_AXIS_LABEL`, `ROUNDING_VARIANCE`, `FORMAT_INCONSISTENCY`, `NO_YOY_QOQ_SHOWN`, `NO_QUANTIFIED_TARGET`, `FORWARD_LOOKING_UNQUANTIFIED`, `SINGLE_SPEAKER_ONLY`, `SIGNATURE_TIMESTAMP_NOTED`, `DISCLOSURE_ABSENT`.
