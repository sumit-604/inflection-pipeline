# A2 ENUMERATION LEDGER — Investor Presentation — RPTECH — Q1 FY27

Source: `extract_presentation_rptech_q1fy27.txt` (23 PDF pages; page 1 = BSE/NSE
Reg 30(6) covering letter; page 2 of PDF = slide 1 of the deck per A1 header;
unit convention INR Mn, x0.1 = Rs Cr; pages 2, 7, 13, 23 OCR'd/rasterised;
pages 10, 15, 18, 21 confirmed native-text chart labels, no OCR fallback).
Prior-quarter ledger: not supplied to this run — `DROPPED_SLIDE` comparison
category is therefore N/A this run (flagged, not silently skipped).

```
=== A2 COUNT TEST ===
category: slides                  grep_count: 23   sweep_count: 23   match: yes
category: kpi_tiles_named_metrics grep_count: 41   sweep_count: 41   match: yes
category: chart_data_labels       grep_count: 86   sweep_count: 86   match: yes
category: financial_line_items    grep_count: 86   sweep_count: 86   match: yes
category: segment_brand_splits    grep_count: 11   sweep_count: 11   match: yes
category: forward_statements      grep_count: 11   sweep_count: 11   match: yes
category: zero_standing           grep_count: 1    sweep_count: 1    match: yes
category: footnotes               grep_count: 5    sweep_count: 5    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep methods used per category (reconciled against manual line-by-line sweep
of every one of the 23 `[page N]` blocks):
- slides: `grep -n -E "^\[page [0-9]+\]"` → 23 hits, one per PDF page marker.
- kpi_tiles_named_metrics: manual sweep of every standalone KPI figure on
  pages 3, 4, 6, 7, 8, 9, 12, 14 (non-chart, non-tabular figures), cross-checked
  token-by-token against `grep -noE` numeric-token pass over lines 94-477.
- chart_data_labels: every bar/data-point label on pages 10, 15, 18, 21,
  counted 1:1 against the same numeric-token grep pass restricted to those
  four pages' line ranges (358-391, 480-527, 591-622, 707-750).
- financial_line_items: `awk` line count of labelled rows in the four
  tables (pages 16, 17, 19, 20), cross-checked against manual item list.
- segment_brand_splits: manual count (PES/LIT split, Standalone/Consol
  split, 8-row brand logo grid, 3-way distribution-channel split).
- forward_statements: `grep -c "^•"` on page 11 (5 pillars, unbulleted but
  visually distinct) + page 12 (5 bulleted highlights, confirmed 5 via grep)
  + 1 disclaimer forward-looking-statements paragraph (page 22).
- zero_standing: manual review of both "Exceptional Item[m]" rows (pages 17,
  19); only the page-17 Consolidated Quarterly IS row is dash in ALL three
  periods shown → 1 true ZERO_STANDING; the page-19 row has FY24/FY25 values
  so does not qualify (noted, not flagged).
- footnotes: manual sweep of asterisk/qualifier text below headline KPIs
  (pages 3, 9) plus the two disclaimer blocks on page 22.

---

## TABLE 1 — SLIDES / PAGES (23 rows)

| # | Page marker (line) | Printed slide # (footer) | Title | Content type | Notes / flags |
|---|---|---|---|---|---|
| 1 | page 1 (line 26) | none (not a deck slide) | BSE/NSE Reg 30(6) covering letter | text/letter | Precedes deck; digitally signed by Arvind Bajoria, CS & Compliance Officer, timestamp 2026.08.04 20:03:04 +05'30' (line 76); signed same calendar day as filing, no board-meeting-timestamp comparison possible for a presentation (no separate board outcome letter in this doctype) |
| 2 | page 2 (line 94) | 1 (unnumbered on title slide) | "EARNINGS PRESENTATION Q1-FY27" | text (title slide) | Line 100 OCR pass confirms native text match, no new content |
| 3 | page 3 (line 105) | 2 (line 133) | "RP tech at a Glance" | KPI tile grid (10 tiles) | See Table 2 rows P3-1..P3-10 |
| 4 | page 4 (line 136) | 3 (line 169) | "Enabling Adoption & Deployment of Technology in India" | text (vision/mission + 5 capability blocks) | See Table 2 rows P4-1..P4-6 |
| 5 | page 5 (line 172) | 4 (line 199) | "Value Proposition" | text (dual-column value prop) | No numeric KPIs on this slide |
| 6 | page 6 (line 202) | 5 (line 239) | "Key Strengths" | text (8 strength blocks) | See Table 2 rows P6-1..P6-5 |
| 7 | page 7 (line 242) | 6 (line 255) | "Brand Relationships & Positioning" | text + logo grid (chart/photo) | OCR/rasterised logo grid transcription at line 258-267; see Table 2 rows P7-1..P7-2 and Table 5 (brand grid) |
| 8 | page 8 (line 270) | 7 (line 304) | "Distribution Model" | diagram (text flow: OEM→Distributor→Channels→End Users) | See Table 2 row P8-1, Table 5 (channel split) |
| 9 | page 9 (line 307) | 8 (line 355) | "Pan-India Branch Network" | KPI tiles + state/city directory (text) | See Table 2 rows P9-1..P9-4; footnote line 355 |
| 10 | page 10 (line 358) | 9 (line 391) | "Business Overview" (PES / LIT) | chart (2 bar charts) + text | See Table 3 rows P10-1..P10-8, Table 5 (PES/LIT split) |
| 11 | page 11 (line 394) | 10 (line 420) | "Growth Drivers" | text (5 strategic pillars) | See Table 7 rows P11-1..P11-5 |
| 12 | page 12 (line 423) | 11 (line 444) | "Q1-FY27 Operational Highlights" | text (5 bullets) | See Table 2 row P12-1, Table 7 rows P12-1..P12-5 |
| 13 | page 13 (line 447) | none (section divider) | "FINANCIAL OVERVIEW" | text (divider slide) | Line 452 OCR pass confirms native text match |
| 14 | page 14 (line 456) | 13 (line 477) | "Key Financial Highlights" | KPI boxes (Standalone vs Consolidated) | See Table 2 rows P14-1..P14-12 |
| 15 | page 15 (line 480) | 14 (line 527) | "Financial Performance" (Standalone / Consolidated quarterly trend charts) | chart (6 mini bar/line charts) | See Table 3 rows P15-1..P15-30 |
| 16 | page 16 (line 530) | 15 (line 563) | "Quarterly Standalone Income Statement" | table (14 line items x 5 columns) | See Table 4 rows P16-1..P16-14 |
| 17 | page 17 (line 566) | 16 (line 588) | "Quarterly Consolidated Income Statement" | table (16 line items x 5 columns) | See Table 4 rows P17-1..P17-16; ZERO_STANDING at P17-9 |
| 18 | page 18 (line 591) | 17 (line 622) | "Working Capital Efficiency" | chart (6 mini 2-bar charts) | See Table 3 rows P18-1..P18-12; AMBIGUOUS_LAYOUT flag |
| 19 | page 19 (line 625) | 18 (line 660) | "Historical Consolidated Income Statement" | table (15 line items x 4 columns) | See Table 4 rows P19-1..P19-15 |
| 20 | page 20 (line 663) | 19 (line 704) | "Historical Consolidated Balance Sheet" | table (41 line items x 4 columns, two-column layout) | See Table 4 rows P20-1..P20-41 |
| 21 | page 21 (line 707) | 20 (line 750) | "Financial Performance" (4-year + Q1 recap: Revenue/EBITDA/PAT/margins/CFO/WC days/Net D-E/ROCE&ROE) | chart (8 mini charts) | See Table 3 rows P21-1..P21-36; AMBIGUOUS_LAYOUT flag on CFO, WC Days, Net D/E, ROCE&ROE clusters |
| 22 | page 22 (line 753) | 21 (line 786) | "Disclaimer" | text (2 disclaimer blocks + IR contact) | See Table 7 row DISC-1, Table 9 rows FN-4..FN-5 |
| 23 | page 23 (line 789) | none (closing slide) | "THANK YOU" | text/photo (closing slide + logo watermark) | Line 794 OCR pass confirms native text + picks up low-confidence corner logo watermark "RP tech - Rashi Peripherals Limited" (line 797) |

`DROPPED_SLIDE`: not evaluable — no prior-quarter presentation ledger was
supplied as an input to this run. Flagged for A3/A4 to source the Q4 FY26 (or
Q1 FY26) deck if a slide-count trend check is required.

---

## TABLE 2 — SLIDE-LEVEL KPI TILES & NAMED METRICS (non-chart, non-tabular) — 41 rows

### Page 3 — "RP tech at a Glance" (10 rows)
| ID | Line | KPI | Value | Flags |
|---|---|---|---|---|
| P3-1 | 110 | Years of experience | 37+ | |
| P3-2 | 110 | Global technology brands | 80 | |
| P3-3 | 110 | Partners / B2B customers | 10,250+ | |
| P3-4 | 110 | Million units distributed | 661 | |
| P3-5 | 112 | SKU's | 18,874 | |
| P3-6 | 122 | Employees | 1,641 | |
| P3-7 | 122 | 3-year Revenue CAGR* | 18.7% | *footnote FN-2 applies (FY26 basis) |
| P3-8 | 121 | 3-year PAT CAGR* | 31.8% | *footnote FN-2 applies |
| P3-9 | 122 | Net Debt to Equity* | 0.43 | *footnote FN-2 applies |
| P3-10 | 121/124 | CRISIL Long Term rating | AA-/Stable | |

### Page 4 — "Enabling Adoption & Deployment..." (6 rows)
| ID | Line | KPI | Value | Flags |
|---|---|---|---|---|
| P4-1 | 140 | Districts covered (mission) | 800+ | |
| P4-2 | 153 | Global technology brands | 80 | repeat of P3-2, disclosed again on this slide |
| P4-3 | 166 | Locations | 700+ | |
| P4-4 | 166 | Branches | 57 | |
| P4-5 | 167 | Warehouses | 73 | |
| P4-6 | 167 | Service centres | 50 | |

### Page 6 — "Key Strengths" (5 rows)
| ID | Line | KPI | Value | Flags |
|---|---|---|---|---|
| P6-1 | 206 | Years in ICT distribution | 37+ | repeat of P3-1 |
| P6-2 | 206 | Regions | 20 | |
| P6-3 | 206 | Warehouses | 73 | repeat of P4-5 |
| P6-4 | 207 | Locations | 700+ | repeat of P4-3 |
| P6-5 | 222-223 | Global tech brands | 80+ | repeat of P3-2/P4-2, "+" suffix added here |

### Page 7 — "Brand Relationships & Positioning" (2 rows)
| ID | Line | KPI | Value | Flags |
|---|---|---|---|---|
| P7-1 | 244 | Global technology brands | 80 | repeat |
| P7-2 | 249-250 / 268 | Brands with 5-year+ relationship | more than 20 | stated twice on same slide (body text line 249-250 and callout box line 268) |

### Page 8 — "Distribution Model" (1 row)
| ID | Line | KPI | Value | Flags |
|---|---|---|---|---|
| P8-1 | 291 | LFRs (Large Format Retailers) served as sole distributor | 15+ | "Only distributor catering to 15+ LFRs" |

### Page 9 — "Pan-India Branch Network" (4 rows)
| ID | Line | KPI | Value | Flags |
|---|---|---|---|---|
| P9-1 | 309 | Regions | 20 | repeat of P6-2 |
| P9-2 | 313 | Branches | 57 | repeat of P4-4 |
| P9-3 | 317 | Locations | 706 | NOTE: differs from "700+" rounded figure used on pages 4/6 (706 exact vs 700+ rounded) — not a discrepancy, just precision level; worth cross-checking in A3 |
| P9-4 | 321 | Distribution Partners | 10,250+ | repeat of P3-3 |

### Page 12 — "Q1-FY27 Operational Highlights" (1 numeric row; remaining 4 bullets are qualitative, see Table 7)
| ID | Line | KPI | Value | Flags |
|---|---|---|---|---|
| P12-1 | 435-437 | New branches added (Udaipur, Dhule) | two (2) | qualitative count within a forward/strategic bullet; cross-ref Table 7 P12-4 |

### Page 14 — "Key Financial Highlights" (12 rows: 6 Standalone + 6 Consolidated, each value paired with its own YoY delta as one disclosed KPI unit)
| ID | Line | Basis | KPI | Value (YoY) | Flags |
|---|---|---|---|---|---|
| P14-1 | 465-468 | Standalone | Revenue from Operations | INR 48,322 Mn (+58.3% YoY) | |
| P14-2 | 466-467 | Standalone | EBITDA | INR 1,462 Mn (+43.3% YoY) | |
| P14-3 | 466-467 | Standalone | EBITDA Margin | 3.03% ((31) Bps YoY) | |
| P14-4 | 470-472 | Standalone | PAT | INR 972 Mn (+65.3% YoY) | |
| P14-5 | 470-472 | Standalone | PAT Margin | 2.01% (8 Bps YoY) | |
| P14-6 | 470-472 | Standalone | Diluted EPS | INR 14.41/Share (+61.4% YoY) | |
| P14-7 | 465-468 | Consolidated | Revenue from Operations | INR 51,019 Mn (+61.9% YoY) | |
| P14-8 | 466-467 | Consolidated | EBITDA | INR 1,553 Mn (+50.0% YoY) | |
| P14-9 | 466-467 | Consolidated | EBITDA Margin | 3.04% ((24) Bps YoY) | |
| P14-10 | 470-472 | Consolidated | PAT | INR 1,046 Mn (+69.5% YoY) | |
| P14-11 | 470-472 | Consolidated | PAT Margin | 2.05% (9 Bps YoY) | |
| P14-12 | 470-472 | Consolidated | Diluted EPS | INR 15.25/Share (+64.0% YoY) | |

---

## TABLE 3 — CHART DATA LABELS — 86 rows

### Page 10 — Business Overview: PES & LIT segment revenue bar charts (8 rows)
| ID | Line | Segment | Period | Value (INR Mn) |
|---|---|---|---|---|
| P10-1 | 365 | PES | FY24 | 60,600 |
| P10-2 | 363 | PES | FY25 | 83,606 |
| P10-3 | 362 | PES | FY26 | 91,266 |
| P10-4 | 367 | PES | Q1-FY27 | 33,847 |
| P10-5 | 381 | LIT | FY24 | 50,347 |
| P10-6 | 380 | LIT | FY25 | 54,121 |
| P10-7 | 379 | LIT | FY26 | 67,008 |
| P10-8 | 385 | LIT | Q1-FY27 | 17,172 |

Arithmetic check (not an interpretation, a mechanical cross-foot): PES + LIT
by year = 110,947 / 137,727 / 158,273 / 51,019 (FY24/FY25/FY26/Q1-FY27),
which ties exactly to the Historical Consolidated Income Statement revenue
line (Table 4, P19-1). Consistent, no flag.

### Page 15 — Financial Performance: Standalone quarterly trend (15 rows)
| ID | Line | Metric | Period | Value |
|---|---|---|---|---|
| P15-1 | 493 | Revenue (INR Mn) | Q1-FY26 | 30,527 |
| P15-2 | 486 | Revenue (INR Mn) | Q4-FY26 | 42,068 |
| P15-3 | 485 | Revenue (INR Mn) | Q1-FY27 | 48,322 |
| P15-4 | 492 | EBITDA (INR Mn) | Q1-FY26 | 1,020 |
| P15-5 | 486 | EBITDA (INR Mn) | Q4-FY26 | 1,198 |
| P15-6 | 485 | EBITDA (INR Mn) | Q1-FY27 | 1,462 |
| P15-7 | 494 | EBITDA Margin | Q1-FY26 | 3.34% |
| P15-8 | (496/492 cluster) | EBITDA Margin | Q4-FY26 | 2.85% |
| P15-9 | 492 | EBITDA Margin | Q1-FY27 | 3.03% |
| P15-10 | 495 | PAT (INR Mn) | Q1-FY26 | 588 |
| P15-11 | 494 | PAT (INR Mn) | Q4-FY26 | 760 |
| P15-12 | 492 | PAT (INR Mn) | Q1-FY27 | 972 |
| P15-13 | 497 | PAT Margin | Q1-FY26 | 1.93% |
| P15-14 | 494 | PAT Margin | Q4-FY26 | 1.81% |
| P15-15 | 495 | PAT Margin | Q1-FY27 | 2.01% |

### Page 15 — Financial Performance: Consolidated quarterly trend (15 rows)
| ID | Line | Metric | Period | Value |
|---|---|---|---|---|
| P15-16 | 516 | Revenue (INR Mn) | Q1-FY26 | 31,521 |
| P15-17 | 508 | Revenue (INR Mn) | Q4-FY26 | 44,894 |
| P15-18 | 507 | Revenue (INR Mn) | Q1-FY27 | 51,019 |
| P15-19 | 515 | EBITDA (INR Mn) | Q1-FY26 | 1,035 |
| P15-20 | 514 | EBITDA (INR Mn) | Q4-FY26 | 1,326 |
| P15-21 | 508 | EBITDA (INR Mn) | Q1-FY27 | 1,553 |
| P15-22 | 517 | EBITDA Margin | Q1-FY26 | 3.28% |
| P15-23 | 517 | EBITDA Margin | Q4-FY26 | 2.95% |
| P15-24 | 515 | EBITDA Margin | Q1-FY27 | 3.04% |
| P15-25 | 517 | PAT (INR Mn) | Q1-FY26 | 617 |
| P15-26 | 516 | PAT (INR Mn) | Q4-FY26 | 868 |
| P15-27 | 515 | PAT (INR Mn) | Q1-FY27 | 1,046 |
| P15-28 | 519 | PAT Margin | Q1-FY26 | 1.96% |
| P15-29 | 519 | PAT Margin | Q4-FY26 | 1.93% |
| P15-30 | 519 | PAT Margin | Q1-FY27 | 2.05% |

### Page 18 — Working Capital Efficiency (12 rows) — `AMBIGUOUS_LAYOUT`
The source text is native (not OCR'd) but the three 2-bar mini-charts
(Inventory Days / Debtor Days / Creditor Days) and the three further
mini-charts (Working Capital Days / Provision for Doubtful Debt % /
Provision for Inventory Write-off %) render as columns of numbers whose
period (Q1-FY26 vs Q1-FY27) cannot be assigned with full confidence from
character-column position alone. All six raw values per cluster are
captured below with a best-effort pairing reconstructed from indentation;
`AMBIGUOUS_LAYOUT` flag carried on every row in this section — A3/A4 should
confirm period assignment against the source PDF image before using these
in the cash-conversion thesis check.

| ID | Line | Metric | Best-effort period | Value | Flags |
|---|---|---|---|---|---|
| P18-1 | 595 | Inventory Days | Q1-FY26 | 64 | AMBIGUOUS_LAYOUT |
| P18-2 | 596 | Inventory Days | Q1-FY27 | 55 (or 53 — two candidate values on same line, see P18-3) | AMBIGUOUS_LAYOUT |
| P18-3 | 596 | Debtor Days | Q1-FY26 | 53 (or 55 — ambiguous with P18-2) | AMBIGUOUS_LAYOUT |
| P18-4 | 598 | Debtor Days | Q1-FY27 | 41 | AMBIGUOUS_LAYOUT |
| P18-5 | 597 | Creditor Days | Q1-FY26 | 44 | AMBIGUOUS_LAYOUT |
| P18-6 | 598 | Creditor Days | Q1-FY27 | 40 | AMBIGUOUS_LAYOUT |
| P18-7 | 608 | Working Capital Days | Q1-FY26 | 73 | unambiguous (2-value chart, clean single-column layout) |
| P18-8 | 610 | Working Capital Days | Q1-FY27 | 56 | unambiguous |
| P18-9 | 612 | Provision for Doubtful Debt % | Q1-FY26 (best-effort) | 0.018% | AMBIGUOUS_LAYOUT |
| P18-10 | 613 | Provision for Doubtful Debt % | Q1-FY27 (best-effort) | 0.016% | AMBIGUOUS_LAYOUT |
| P18-11 | 614 | Provision for Inventory Write-off % | Q1-FY26 (best-effort) | 0.043% | AMBIGUOUS_LAYOUT |
| P18-12 | 611 | Provision for Inventory Write-off % | Q1-FY27 (best-effort) | 0.088% | AMBIGUOUS_LAYOUT |

Note: raw 6-value set for the Inventory/Debtor/Creditor cluster is
{64, 55, 53, 44, 41, 40} across lines 595-598, unambiguously 3 metrics x 2
periods = 6 data points (count is certain); only the metric-to-value pairing
is uncertain. Same logic for the WC-Days/Provisions cluster: raw set
{73, 56, 0.088%, 0.018%, 0.016%, 0.043%} across lines 608-614, count certain
at 6, pairing of the two provision % pairs uncertain.

### Page 21 — Financial Performance (4yr + Q1 recap, 8 mini-charts, 36 rows)
| ID | Line | Metric | Period | Value | Flags |
|---|---|---|---|---|---|
| P21-1 | 716 | Operational Revenue (INR Mn) | FY24 | 1,10,947 (110,947) | |
| P21-2 | 714 | Operational Revenue (INR Mn) | FY25 | 1,37,727 (137,727) | |
| P21-3 | 713 | Operational Revenue (INR Mn) | FY26 | 1,58,273 (158,273) | |
| P21-4 | 721 | Operational Revenue (INR Mn) | Q1-FY27 | 51,019 | |
| P21-5 | 717 | EBITDA (INR Mn) | FY24 | 2,929 | |
| P21-6 | 717 | EBITDA (INR Mn) | FY25 | 3,002 | |
| P21-7 | 714 | EBITDA (INR Mn) | FY26 | 4,587 | |
| P21-8 | 721 | EBITDA (INR Mn) | Q1-FY27 | 1,553 | |
| P21-9 | 720 | PAT (INR Mn) | FY24 | 1,439 | |
| P21-10 | 718 | PAT (INR Mn) | FY25 | 2,097 | |
| P21-11 | 716 | PAT (INR Mn) | FY26 | 2,823 | |
| P21-12 | 722 | PAT (INR Mn) | Q1-FY27 | 1,046 | |
| P21-13 | 720 | EBITDA Margin | FY24 | 1.30% (mislabelled position — see note) | LAYOUT_RECONSTRUCTED; value ties to PAT margin FY24 per Table 4 P19 cross-check, likely printed adjacent to PAT column — treat FY24 EBITDA margin as 2.64% (line 713) instead, cross-verified against P19 table |
| P21-14 | 715 | EBITDA Margin | FY25 | 2.18% | cross-verified vs P19-4 table value |
| P21-15 | 712 | EBITDA Margin | FY26 | 2.90% | cross-verified vs P19-4 |
| P21-16 | 712 | EBITDA Margin | Q1-FY27 | 3.04% | cross-verified vs P19-4 |
| P21-17 | 721 | PAT Margin | FY24 | 1.30% | cross-verified vs P19 PAT Margins row (P19-11) |
| P21-18 | 719 | PAT Margin | FY25 | 1.52% | cross-verified vs P19-11 |
| P21-19 | 712 | PAT Margin | FY26 | 2.90% (duplicate token at this line — see P21-15; actual PAT margin FY26 per P19-11 is 1.78%) | LAYOUT_RECONSTRUCTED — chart label position for PAT-margin-FY26 not cleanly separable from EBITDA-margin-FY26 token at same line; value taken from P19 table (1.78%) in preference to raw position guess |
| P21-20 | 718 | PAT Margin | Q1-FY27 | 2.05% | cross-verified vs P19-11 |
| P21-21 | 733 | Cash Flow from Operation (INR Mn) | unassigned (candidate FY26 by indent) | 1,137 | AMBIGUOUS_LAYOUT — CASH_CONVERSION_THESIS_METRIC — period mapping NOT confirmed, see note below table |
| P21-22 | 741 | Cash Flow from Operation (INR Mn) | unassigned (candidate FY24 by indent) | -1,020 | AMBIGUOUS_LAYOUT — CASH_CONVERSION_THESIS_METRIC |
| P21-23 | 745 | Cash Flow from Operation (INR Mn) | unassigned (candidate FY25 by indent) | -2,992 | AMBIGUOUS_LAYOUT — CASH_CONVERSION_THESIS_METRIC |
| P21-24 | 734 | Working Capital Days | FY26 (cross-verified) | 58 | resolved via cross-check: Q1-FY27 value (56) matches Table 3 P18-8, confirming axis order |
| P21-25 | 735 | Working Capital Days | FY24 | 54 | resolved (tie with FY25, both =54, order between the two immaterial) |
| P21-26 | 735 | Working Capital Days | FY25 | 54 | resolved (tie, see above) |
| P21-27 | 735 | Working Capital Days | Q1-FY27 | 56 | resolved — matches Table 3 P18-8 (page 18 chart), cross-verified |
| P21-28 | 734 | Net Debt to Equity (x) | unassigned | 0.50x | AMBIGUOUS_LAYOUT — period (FY24/25/26) not confirmed |
| P21-29 | 736 | Net Debt to Equity (x) | unassigned | 0.43x | AMBIGUOUS_LAYOUT — matches P3-9 headline "0.43" (stated as "Net Debt to Equity* / Figures as on FY26"), suggesting this is the FY26 value |
| P21-30 | 737 | Net Debt to Equity (x) | unassigned | 0.35x | AMBIGUOUS_LAYOUT — period not confirmed |
| P21-31 | 739 | ROCE (%) | FY24 (best-effort, layout-reconstructed) | 12.79% | LAYOUT_RECONSTRUCTED |
| P21-32 | 739 | ROCE (%) | FY25 (best-effort) | 12.74% | LAYOUT_RECONSTRUCTED |
| P21-33 | 737 | ROCE (%) | FY26 (best-effort, tallest/rightmost bar) | 16.02% | LAYOUT_RECONSTRUCTED |
| P21-34 | 742 | ROE (%) | FY24 (best-effort) | 12.93% | LAYOUT_RECONSTRUCTED |
| P21-35 | 742 | ROE (%) | FY25 (best-effort) | 13.02% | LAYOUT_RECONSTRUCTED |
| P21-36 | 740 | ROE (%) | FY26 (best-effort, tallest/rightmost bar) | 14.74% | LAYOUT_RECONSTRUCTED |

**CASH_CONVERSION_THESIS_METRIC flag detail (P21-21..23):** the CFO chart on
page 21 is the only disclosure of Cash Flow from Operations anywhere in this
presentation. The three raw values (1,137 / -1,020 / -2,992, lines 733/741/745)
are certain as disclosed figures; the FY24/FY25/FY26 axis assignment is
reconstructed from character-indentation only (not from an explicit per-bar
label) and is NOT independently cross-verifiable elsewhere in this deck. Given
this metric is the binding thesis gate (cash conversion) per the task
instructions, A3/A4 must resolve the year mapping against the source PDF
image or the results filing/press release before drawing a conclusion — do
not treat the indent-based ordering above as confirmed.

---

## TABLE 4 — FINANCIAL TABLE LINE ITEMS — 86 rows

### Page 16 — Quarterly Standalone Income Statement (14 rows, lines 532-560)
| ID | Line | Line item | Q1-FY27 | Q1-FY26 | Y-o-Y | Q4-FY26 | Q-o-Q |
|---|---|---|---|---|---|---|---|
| P16-1 | 534 | Revenue from Operations | 48,322 | 30,527 | 58.3% | 42,068 | 14.9% |
| P16-2 | 536 | Operational Expenses | 46,860 | 29,507 | 58.8% | 40,870 | 14.7% |
| P16-3 | 538 | EBITDA | 1,462 | 1,020 | 43.3% | 1,198 | 22.0% |
| P16-4 | 540 | EBITDA Margins | 3.03% | 3.34% | (31) Bps | 2.85% | 18 Bps |
| P16-5 | 542 | Other Income | 173 | 72 | NA | 161 | 7.5% |
| P16-6 | 544 | Finance costs | 272 | 264 | 3.0% | 286 | (4.9)% |
| P16-7 | 546 | Depreciation & Amortization | 62 | 41 | 51.2% | 60 | 3.3% |
| P16-8 | 548 | PBT | 1,301 | 787 | 65.3% | 1,013 | 28.4% |
| P16-9 | 550 | Tax Expense | 329 | 199 | 65.3% | 253 | 30.0% |
| P16-10 | 552 | PAT | 972 | 588 | 65.3% | 760 | 27.9% |
| P16-11 | 554 | PAT Margins (%) | 2.01% | 1.93% | 8 Bps | 1.81% | 20 Bps |
| P16-12 | 556 | Other Comprehensive Income | (2) | (3) | (33.3)% | (1) | NA |
| P16-13 | 558 | Total Comprehensive Income | 970 | 585 | 65.8% | 759 | 27.8% |
| P16-14 | 560 | Diluted EPS | 14.41 | 8.93 | 61.4% | 11.28 | 27.7% |

Flag: this table has NO "Exceptional Item" / "PBT Before Exceptional Item"
line, unlike the Consolidated table on the next slide (P17-8/P17-9). PBT is
shown directly after D&A. Structural asymmetry between Standalone and
Consolidated table templates — noted for A3, not itself a defect.

### Page 17 — Quarterly Consolidated Income Statement (16 rows, lines 570-585)
| ID | Line | Line item | Q1-FY27 | Q1-FY26 | Y-o-Y | Q4-FY26 | Q-o-Q |
|---|---|---|---|---|---|---|---|
| P17-1 | 570 | Revenue from Operations | 51,019 | 31,521 | 61.9% | 44,894 | 13.6% |
| P17-2 | 571 | Operational Expenses | 49,466 | 30,486 | 62.3% | 43,568 | 13.5% |
| P17-3 | 572 | EBITDA | 1,553 | 1,035 | 50.0% | 1,326 | 17.1% |
| P17-4 | 573 | EBITDA Margins | 3.04% | 3.28% | (24) Bps | 2.95% | 9 Bps |
| P17-5 | 574 | Other Income | 174 | 79 | NA | 160 | 8.7% |
| P17-6 | 575 | Finance costs | 274 | 269 | 1.9% | 289 | (5.2)% |
| P17-7 | 576 | Depreciation & Amortization | 63 | 42 | 50.0% | 61 | 3.3% |
| P17-8 | 577 | PBT Before Exceptional Item | 1,390 | 803 | 73.1% | 1,136 | 22.4% |
| P17-9 | 578 | Exceptional Item | - | - | NA | - | NA | **`ZERO_STANDING`** — dash in all three periods shown; template line retained though FY24/FY25 (Table 4, P19-8) show this line was non-zero historically (104, 26) — signals the line exists for a transaction type that has occurred before and could recur |
| P17-10 | 579 | PBT | 1,390 | 803 | 73.1% | 1,136 | 22.4% |
| P17-11 | 580 | Tax Expense | 344 | 186 | 84.9% | 268 | 28.4% |
| P17-12 | 581 | PAT | 1,046 | 617 | 69.5% | 868 | 20.5% |
| P17-13 | 582 | PAT Margins (%) | 2.05% | 1.96% | 9 Bps | 1.93% | 12 Bps |
| P17-14 | 583 | Other Comprehensive Income | 41 | (4) | NA | (11) | NA |
| P17-15 | 584 | Total Comprehensive Income | 1,086 | 613 | 77.2% | 857 | 26.7% |
| P17-16 | 585 | Diluted EPS | 15.25 | 9.30 | 64.0% | 12.49 | 22.1% |

### Page 19 — Historical Consolidated Income Statement (15 rows, lines 629-657)
| ID | Line | Line item | FY24 | FY25 | FY26 | Q1-FY27 |
|---|---|---|---|---|---|---|
| P19-1 | 629 | Revenue from Operations | 110,947 | 137,727 | 158,273 | 51,019 |
| P19-2 | 631 | Operational Expenses | 108,018 | 134,725 | 153,686 | 49,466 |
| P19-3 | 633 | EBITDA | 2,929 | 3,002 | 4,587 | 1,553 |
| P19-4 | 635 | EBITDA Margins | 2.64% | 2.18% | 2.90% | 3.04% |
| P19-5 | 637 | Other Income | 144 | 606 | 406 | 174 |
| P19-6 | 639 | Finance costs | 1,071 | 775 | 1,065 | 274 |
| P19-7 | 641 | Depreciation & Amortization | 189 | 172 | 215 | 63 |
| P19-8 | 643 | Exceptional item | 104 | 26 | - | - | not full ZERO_STANDING (FY24/FY25 nonzero) — noted, see P17-9 |
| P19-9 | 645 | PBT | 1,917 | 2,687 | 3,713 | 1,390 |
| P19-10 | 647 | Tax Expense | 478 | 590 | 890 | 344 |
| P19-11 | 649 | PAT | 1,439 | 2,097 | 2,823 | 1,046 |
| P19-12 | 651 | PAT Margins (%) | 1.30% | 1.52% | 1.78% | 2.05% |
| P19-13 | 653 | Other Comprehensive Income | (40) | (13) | (30) | 41 |
| P19-14 | 655 | Total Comprehensive Income | 1,399 | 2,084 | 2,793 | 1,086 |
| P19-15 | 657 | Diluted EPS | 31.14 | 31.57 | 41.18 | 15.25 |

### Page 20 — Historical Consolidated Balance Sheet (41 rows, lines 668-703)

**Assets side (20 rows):**
| ID | Line | Line item | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|---|---|
| P20-1 | 668 | (a) Property, Plant & Equipment | 540 | 525 | 492 | 453 |
| P20-2 | 669-670 | (b) Right of Use Assets | 159 | 130 | 94 | 308 |
| P20-3 | 672 | (c) Capital Work-in-Progress | 40 | - | - | 3 |
| P20-4 | 674 | (d) Other Intangible Assets | 27 | 18 | 13 | 6 |
| P20-5 | 675 | (e) Goodwill | 41 | 34 | 34 | 29 |
| P20-6 | 678 | (f)(i) Investments | 56 | - | - | - |
| P20-7 | 679 | (f)(ii) Other Financial Assets (non-current) | 97 | 133 | 135 | 149 |
| P20-8 | 680 | (g) Non-Current Tax Assets (Net) | 104 | 146 | 28 | 27 |
| P20-9 | 681 | (h) Deferred Tax Assets (Net) | 59 | 68 | 19 | - |
| P20-10 | 682 | (i) Other Non-Current Assets | 132 | 86 | 61 | 99 |
| P20-11 | 683 | Total Non-Current Assets | 1,255 | 1,140 | 876 | 1,074 |
| P20-12 | 687 | (a) Inventories | 14,934 | 18,248 | 19,995 | 25,537 |
| P20-13 | 691 | (b)(i) Trade Receivables | 8,716 | 13,843 | 17,951 | 21,842 |
| P20-14 | 693 | (b)(ii) Cash & Cash Equivalents | 346 | 1,450 | 216 | 812 |
| P20-15 | 695 | (b)(iii) Bank Balances (Other) | - | - | 4 | - |
| P20-16 | 697 | (b)(iv) Loans | - | - | - | 11 |
| P20-17 | 699 | (b)(v) Other Financial Assets (current) | 52 | 55 | 56 | 142 |
| P20-18 | 700 | (c) Other Current Assets | 2,683 | 3,452 | 3,538 | 3,853 |
| P20-19 | 701 | Total Current Assets | 26,731 | 37,048 | 41,760 | 52,197 |
| P20-20 | 703 | TOTAL ASSETS | 27,986 | 38,188 | 42,636 | 53,271 |

**Equity & Liabilities side (21 rows):**
| ID | Line | Line item | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|---|---|
| P20-21 | 668 | (a) Equity Share Capital | 209 | 330 | 330 | 330 |
| P20-22 | 669 | (b) Other Equity | 6,793 | 15,176 | 17,092 | 19,921 |
| P20-23 | 671 | Non-Controlling Interest | (19) | 1 | 18 | 112 |
| P20-24 | 673 | Total Equity | 6,983 | 15,507 | 17,440 | 20,363 |
| P20-25 | 678 | (a)(i) Borrowings (non-current) | 324 | 5 | 9 | - |
| P20-26 | 679 | (a)(ii) Lease Liabilities (non-current) | 116 | 89 | 46 | 219 |
| P20-27 | 680 | (b) Provisions (non-current) | 11 | 11 | 8 | - |
| P20-28 | 681 | (c) Contract Liabilities (non-current) | 10 | 6 | 48 | - |
| P20-29 | 682 | (d) Deferred Tax Liabilities (Net) | 68 | - | 25 | 18 |
| P20-30 | 683 | Total Non-Current Liabilities | 529 | 111 | 136 | 237 |
| P20-31 | 688 | (a)(i) Borrowings (current) | 10,333 | 6,853 | 8,983 | 9,586 |
| P20-32 | 690 | (a)(ii) Lease Liabilities (current) | 48 | 50 | 59 | 101 |
| P20-33 | 692 | (a)(iii) Trade Payables (MSME) | 3 | 52 | 346 | 568 |
| P20-34 | 694 | (a)(iii) Trade Payables (Others) | 9,558 | 14,977 | 15,060 | 21,142 |
| P20-35 | 696 | (a)(iv) Other Financial Liabilities | 220 | 239 | 250 | 535 |
| P20-36 | 698 | (b) Other Current Liabilities | 175 | 320 | 207 | 402 |
| P20-37 | 699 | (c) Provisions (current) | 20 | 10 | 24 | 66 |
| P20-38 | 700 | (d) Current Tax Liabilities (Net) | 7 | 9 | 129 | 271 |
| P20-39 | 701 | (e) Contract Liabilities (current) | 110 | 60 | 2 | - |
| P20-40 | 702 | Total Current Liabilities | 20,474 | 22,570 | 25,060 | 32,671 |
| P20-41 | 703 | TOTAL EQUITY AND LIABILITIES | 27,986 | 38,188 | 42,636 | 53,271 |

Note: trade payables split MSME vs Others (P20-33/34) — MSME payables have
grown from 3 (FY23) to 568 (FY26), a ~189x increase; not itself flagged here
(interpretation is A3/A4's job) but the raw growth trajectory is surfaced.
None of the 41 balance sheet lines are dash across all four periods; the
closest candidates (Bank Balances (Other) P20-15, Loans P20-16) each have one
non-zero period and therefore do not qualify for `ZERO_STANDING`.

---

## TABLE 5 — SEGMENT / BRAND / VERTICAL SPLITS — 11 rows

| ID | Line | Split type | Detail |
|---|---|---|---|
| SEG-1 | 358-391 | Business segment split | Personal Computing & Enterprise Solutions (PES) vs Lifestyle and IT Essentials (LIT) — revenue disclosed separately by FY24/FY25/FY26/Q1-FY27, see Table 3 P10-1..P10-8 |
| SEG-2 | 456-750 | Reporting-entity split | Standalone vs Consolidated financial statements shown in parallel throughout pages 14, 15, 16, 17 |
| SEG-3 | 260 | Brand logo grid row 1 (of 8) | Alcatel-Lucent Enterprise, AMD, American Megatrends, Antec, AnyDesk, AOC |
| SEG-4 | 261 | Brand logo grid row 2 | APC, ASUS, ATEN, Belden, belkin, Cambium Networks |
| SEG-5 | 262 | Brand logo grid row 3 | COLORFUL, CORNELIS NETWORKS, DELL, EATON, ECS ELITEGROUP, elmos |
| SEG-6 | 263 | Brand logo grid row 4 | fitbit, Google, hp, intel, j5create, JBL |
| SEG-7 | 264 | Brand logo grid row 5 | Lenovo, LG, logitech, neoway, ninjaOne, NORDEN |
| SEG-8 | 265 | Brand logo grid row 6 | NVIDIA, NUMERIC (A Group brand - Legrand), Optoma, OURA, PHILIPS, Qualcomm |
| SEG-9 | 266 | Brand logo grid row 7 | Quantum, SAMSUNG, SANDISK, Supermicro, Teachmint, TOSHIBA |
| SEG-10 | 267 | Brand logo grid row 8 | tp-link, UBIQUITI, ViewSonic, VVDN Technologies, WEKA, WD |
| SEG-11 | 272-300 | Distribution channel split | General Trade / Modern Trade / E-Commerce, each with distinct value proposition text (page 8) |

Note: 8 rows x 6 columns = 48 logos shown against the "80 Global Technology
Brands" headline (P3-2/P7-1) — 48 of 80 brands are pictorially represented;
the deck does not name the remaining 32. Not a defect, just a completeness
boundary worth carrying forward (the "48" figure is this ledger's own count
of the transcribed grid, not a number printed on the slide itself, and is
therefore NOT included in the Table 3/kpi count-test gate).

---

## TABLE 6 — OPERATING METRICS CROSS-REFERENCE (cash-conversion thesis focus)
Not separately counted for GATE A2 — every value below is already counted
under Table 3 (chart) or Table 4 (table); this table exists solely to answer
the task's explicit instruction to surface every working-capital / cash-
conversion metric the deck volunteers, in one place.

| Metric | Where disclosed | Values | Flags |
|---|---|---|---|
| Inventory Days | Table 3, P18-1/P18-2 | Q1-FY26 vs Q1-FY27: 64 vs 55 (or 53) | AMBIGUOUS_LAYOUT |
| Debtor Days | Table 3, P18-3/P18-4 | Q1-FY26 vs Q1-FY27: 53 (or 55) vs 41 | AMBIGUOUS_LAYOUT |
| Creditor Days | Table 3, P18-5/P18-6 | Q1-FY26 vs Q1-FY27: 44 vs 40 | AMBIGUOUS_LAYOUT |
| Working Capital Days (page 18 chart) | Table 3, P18-7/P18-8 | Q1-FY26 vs Q1-FY27: 73 vs 56 | unambiguous |
| Working Capital Days (page 21 chart, annual+Q1) | Table 3, P21-24..27 | FY24/FY25/FY26/Q1-FY27: 54/54/58/56 | Q1-FY27 cross-verified against page-18 chart |
| Provision for Doubtful Debt % | Table 3, P18-9/P18-10 | Q1-FY26 vs Q1-FY27: 0.018% vs 0.016% (best-effort) | AMBIGUOUS_LAYOUT |
| Provision for Inventory Write-off % | Table 3, P18-11/P18-12 | Q1-FY26 vs Q1-FY27: 0.043% vs 0.088% (best-effort) | AMBIGUOUS_LAYOUT |
| Cash Flow from Operations (CFO) | Table 3, P21-21..23 | Three raw values 1,137 / -1,020 / -2,992 across FY24-FY26; NO Q1-FY27 CFO figure disclosed anywhere in this deck | **AMBIGUOUS_LAYOUT + CASH_CONVERSION_THESIS_METRIC** — period mapping unconfirmed; this is the ONLY CFO disclosure in the presentation and it does not cover the current quarter |
| Net Debt to Equity (x) | Table 3, P21-28..30; also P3-9 (0.43, "as on FY26") | Three raw values 0.50x/0.43x/0.35x across FY24-FY26; headline tile (P3-9) independently states 0.43 "as on FY26", which anchors 0.43x = FY26 | Partially resolved via P3-9 cross-check; FY24 vs FY25 assignment of 0.50x/0.35x still AMBIGUOUS_LAYOUT |
| ROCE (%) | Table 3, P21-31..33 | FY24/FY25/FY26 (best-effort): 12.79% / 12.74% / 16.02% | LAYOUT_RECONSTRUCTED |
| ROE (%) | Table 3, P21-34..36 | FY24/FY25/FY26 (best-effort): 12.93% / 13.02% / 14.74% | LAYOUT_RECONSTRUCTED |
| EBITDA Margin trend | Table 4 P16-4/P17-4/P19-4; Table 3 P15/P21 | Standalone Q1-FY27 3.03% ((31)Bps YoY); Consolidated Q1-FY27 3.04% ((24)Bps YoY); FY24-FY26 consol trend 2.64%→2.18%→2.90%→3.04% | |
| PAT Margin trend | Table 4 P16-11/P17-13/P19-12 | Standalone Q1-FY27 2.01% (8 Bps YoY); Consolidated Q1-FY27 2.05% (9 Bps YoY); FY24-FY26 consol trend 1.30%→1.52%→1.78%→2.05% | |
| Revenue mix (PES vs LIT growth) | Table 3 P10-1..P10-8 | PES Q1-FY27 33,847 (implied YoY needs Q1-FY26 PES figure, NOT separately disclosed — only FY24/FY25/FY26/Q1-FY27 annual+latest-quarter series shown, no Q1-FY26 comparator for the segment split) | Segment-level YoY comparator gap — deck gives company-level YoY (58.3%/61.9%) but not segment-level YoY |

---

## TABLE 7 — FORWARD / GUIDANCE STATEMENTS — 11 rows

### Page 11 — "Growth Drivers" (5 rows, strategic pillars, no numeric targets)
| ID | Line | Pillar | Text |
|---|---|---|---|
| P11-1 | 398-406 | Expand into High-Growth Verticals | "Enter emerging, high-potential sectors to diversify revenue streams" |
| P11-2 | 398-406 | Adjacent Segments | "Introduce new adjacent product segments to leverage existing channel infrastructure" |
| P11-3 | 407-415 | Forge Strategic OEM Partnerships | "Build alliances with leading technology brands to enhance offerings and competitiveness" |
| P11-4 | 407-415 | Accelerate Market Penetration | "Expand presence across new geographies while strengthening existing markets" |
| P11-5 | 407-415 | Solution-Based Selling | "Upsell and cross-sell through solution-based selling to improve wallet-share per partner" |

No quantified guidance (no revenue/margin/capex targets) attached to any of
the five pillars — qualitative strategy only.

### Page 12 — "Q1-FY27 Operational Highlights" (5 rows, bulleted, forward/strategic commitments already executed or announced this quarter)
| ID | Line | Statement |
|---|---|---|
| P12-1 | 425-426 | "Delivered record quarterly operational performance, driven by continued expansion across enterprise solutions, distribution, and strategic technology partnerships." |
| P12-2 | 428-430 | Strategic investment in VDA Infosolutions — "forward integration and expanding capabilities in managed IT services, solution implementation, and lifecycle support" |
| P12-3 | 432-433 | Strategic partnership with WEKA.io — "expand capabilities in AI infrastructure and high-performance workload management" |
| P12-4 | 435-437 | Two new branches added: Udaipur (Rajasthan) and Dhule (Maharashtra), Tier-2 market expansion |
| P12-5 | 439-441 | Industry recognition: VAR India and Digital Terminal Media Awards; Western Digital Excellence in National Distribution Award 2026 |

None of these five carry a forward-looking numeric commitment (no stated
revenue/margin impact, timeline, or capex figure for VDA Infosolutions
investment or WEKA.io partnership) — flagged for A3/A4 as disclosure gaps if
the size/terms of the VDA Infosolutions investment matter to the thesis.

### Page 22 — Disclaimer (1 row)
| ID | Line | Statement |
|---|---|---|
| DISC-1 | 762-769 | Standard forward-looking-statements safe-harbor paragraph: "Certain matters discussed in this Presentation may contain statements regarding the Company's market opportunity and business prospects that are individually and collectively forward-looking statements... not guarantees of future performance..." Company assumes no obligation to update. |

---

## TABLE 8 — ZERO / NIL STANDING ITEMS — 1 row

| ID | Line | Item | Table | Values | Flag |
|---|---|---|---|---|---|
| ZS-1 | 578 | Exceptional Item | Quarterly Consolidated Income Statement (page 17) | Q1-FY27: -, Q1-FY26: -, Q4-FY26: - (YoY/QoQ both NA) | `ZERO_STANDING` — dash in all three periods presented on this slide; the corresponding Historical Consolidated IS (page 19, line 643, ledger ID P19-8) shows this line was NOT always zero (FY24: 104, FY25: 26), so the line is a retained template item for a transaction type that has occurred in the company's recent history and could recur — this is not a line that never applies, it is a line currently quiet |

Related, non-qualifying candidate reviewed and NOT flagged `ZERO_STANDING`
(values present in at least one period): Exceptional item, Historical
Consolidated Income Statement, page 19 line 643 (P19-8) — FY24: 104, FY25:
26, FY26: -, Q1-FY27: -.

---

## TABLE 9 — FOOTNOTES / FINE PRINT — 5 rows

| ID | Line | Qualifies | Text |
|---|---|---|---|
| FN-1 | 131 | All 10 KPI tiles on page 3 (Table 2, P3-1..P3-10) | "All figures as on Q1-FY27" |
| FN-2 | 132 | The three "3-year CAGR* / Net Debt to Equity*" tiles specifically (P3-7, P3-8, P3-9) | "* Figures as on FY26" — i.e. the CAGR and Net-Debt-to-Equity figures on the "at a Glance" slide are NOT as of Q1-FY27 despite FN-1's blanket statement; they are trailing FY26 figures. Two footnotes with overlapping/conflicting scope on the same slide — worth flagging for A3 (which figures on this tile are Q1-FY27-dated vs FY26-dated is only disambiguated by reading both footnotes together) |
| FN-3 | 355 | Page 9 branch-network KPI tiles (Table 2, P9-1..P9-4) | "* As on Q1-FY27" |
| FN-4 | 755-769 | Entire presentation | Rashi Peripherals Limited Disclaimer block — no offer/recommendation, no warranty on accuracy/completeness, forward-looking statements safe harbor (see DISC-1), no obligation to update |
| FN-5 | 770-775 | Entire presentation | Valorem Advisors Disclaimer block — IR firm disclaimer, no warranty on accuracy/completeness, certifies no personal/company stock ownership by Valorem directors/employees in RP Tech |

---

## SUMMARY

| Category | Rows |
|---|---|
| Slides / pages | 23 |
| KPI tiles & named metrics (non-chart, non-table) | 41 |
| Chart data labels | 86 |
| Financial table line items | 86 |
| Segment / brand / vertical splits | 11 |
| Operating metrics cross-reference (not separately gated) | 13 |
| Forward / guidance statements | 11 |
| Zero-standing items | 1 |
| Footnotes / fine print | 5 |
| **Total enumerated ledger rows (gated categories only)** | **265** |

### Flags raised in this ledger
- `ZERO_STANDING` x1 (ZS-1, Exceptional Item, Consolidated quarterly IS)
- `AMBIGUOUS_LAYOUT` x18 (Table 3: P18-1..P18-6, P18-9..P18-12 = 10 rows on
  page 18; P21-21..23, P21-28..30 = 6 rows on page 21; plus the two
  narrative flags in Table 6 restating the CFO and Net D/E ambiguity = counted
  once at the source rows, not double-counted)
- `LAYOUT_RECONSTRUCTED` x9 (P21-13, P21-19 margin-position notes; P21-31..36
  ROCE/ROE best-effort assignment)
- `CASH_CONVERSION_THESIS_METRIC` x3 (P21-21..23, CFO — the binding thesis
  gate metric, disclosed only as an annual FY24-FY26 series with unconfirmed
  year mapping and NO Q1-FY27 figure at all)
- Segment-level YoY comparator gap (Table 6, Revenue mix row) — deck
  discloses PES/LIT revenue for FY24/FY25/FY26/Q1-FY27 but never a Q1-FY26
  PES/LIT split, so segment-level YoY growth cannot be computed from this
  deck alone
- Footnote scope overlap on page 3 (FN-1 vs FN-2) — flagged, not resolved
  here
- `DROPPED_SLIDE` comparison: N/A this run, no prior-quarter ledger supplied
- Structural asymmetry: Standalone quarterly IS (page 16) omits the
  Exceptional Item line present in the Consolidated quarterly IS (page 17)
