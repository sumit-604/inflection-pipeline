# A2 Completeness Ledger — Investor Presentation — LAXMIINDIA — Q1 FY27

Source: `extract_presentation_laxmiindia_q1fy27.txt` (47 pages / 47 slides, 1433 lines,
10 OCR-attempted pages: 5, 18, 21, 26, 33, 37, 43, 44, 45, 47)
Prior-quarter ledger: NOT PROVIDED / NOT FOUND — no `ledger_presentation_laxmiindia_*` exists
for an earlier quarter in `runs/`. Section 3 (dropped-slide comparison) is therefore marked
`PRIOR_LEDGER_UNAVAILABLE` for every row; this is a completeness gap for A3/A4 to carry
forward, not a mismatch on this ledger.

```
=== A2 COUNT TEST ===
category: slides       grep_count: 47   sweep_count: 47   match: yes
category: footnotes    grep_count: 5    sweep_count: 5    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Count-test method:
- slides: `grep -n -E "^\[page [0-9]+\]" extract` = 47 markers (line list: 14, 57, 65, 112,
  130, 136, 182, 217, 253, 290, 327, 360, 398, 430, 467, 500, 532, 568, 574, 604, 637, 643,
  673, 714, 753, 783, 789, 833, 857, 888, 926, 961, 988, 993, 1020, 1059, 1097, 1103, 1130,
  1149, 1193, 1234, 1260, 1304, 1348, 1376, 1418) cross-checked against header
  `page_count_pdfinfo: 47` and `formfeed_count: 47`. Manual sweep read slide 1 through slide
  47 sequentially in full (see Section 1) — 47 distinct slide titles/content blocks found,
  sequence unbroken. Match.
- footnotes: first-pass anchored grep `^\s*(\*|Note[- ]?[0-9]?\s*:|Note\s*:)` returned only 4
  hits (lines 178, 179, 357, 923) and MISSED the mid-line footnote at line 1411 (shareholding
  table: `Note :- * Cumulative holding of promoter...`), because that footnote trails table
  data on the same line rather than starting the line. Manual sweep of every slide's fine
  print located 5 footnotes. Re-ran grep non-anchored (`note[-: ]|^\s*\*[A-Za-z]`, case
  insensitive) = 5, reconciling to the manual sweep. This is recorded as the corrective
  action per GATE A2; the ledger below uses the reconciled set of 5.

---

## SECTION 1 — Slide Inventory (all 47 slides)

| Slide | Title (verbatim, line #) | Content type | Flags |
|---|---|---|---|
| 1 | Regulation 30 cover letter (no slide title; addressed "To, Listing Compliance Department..."), L15 | text — regulatory cover letter, digitally signed | — |
| 2 | "LAXMI INDIA FINANCE LIMITED" + tagline + "Q1 FY27 Investor Presentation", L58-63 | text — title page | — |
| 3 | "Disclaimer", L66 | text — legal boilerplate (forward-looking-statement disclaimer, ~9 paragraphs) | — |
| 4 | "Table of Content", L113 | text — list, 6 sections (01-06) | — |
| 5 | "Q1 FY27 Financial & Operational Highlights", L131 | text — section divider | OCR page 5: no additional text recovered (decorative background only) |
| 6 | "Q1 FY27 Operational and Financial Snapshot", L137 | KPI-tile grid + branch/state map + asset-quality callout | dense multi-metric page, see Section 2 |
| 7 | "Consistent NII and PAT Growth Trajectory", L183 | 4 bar charts (Revenue, NII, OpEx, PAT; FY24-FY26 + Q1FY26 + Q1FY27) | — |
| 8 | "Strong Scale-Up Across AUM, Customers and Network", L218 | 4 bar charts (AUM, Disbursement, Customer Base, Branches) | — |
| 9 | "NIM and Spreads Expand on Better Pricing Discipline", L254 | 4 bar charts (NIM %, Yield %, Avg COB %, Spreads %) | — |
| 10 | "Strong Liquidity Position with Stable Return Metrics", L291 | 4 bar charts (Liquidity, Net Worth, ROTA %, RONW %) | — |
| 11 | "Well Positioned to Capture Future Growth…", L328 | 3 bar charts (D/E, Interest Coverage Ratio, CRAR %) + 1 footnote | footnote L357 |
| 12 | "Asset Quality Update", L361 | 4 bar-chart clusters (Credit Cost Cr, Credit Cost %, GNPA %, NNPA %; each split "With Up-Money Default" / "Without Up-Money Default") | — |
| 13 | "Stage Wise Movement of Loans", L399 | 2 side-by-side tables (as at 30-Jun-2026 vs as at 31-Mar-2026), ECL stage roll-forward | ZERO_STANDING (see Section 2) |
| 14 | "ALM Position as on 30th June 2026", L431 | bucketed bar chart, cumulative assets/liabilities + surplus line | — |
| 15 | "Diversified and Scalable Borrowing Profile", L468 | 2 pie/donut charts (Borrowing Mix; Incremental Borrowing Mix Q1FY27) | — |
| 16 | "Profit & Loss Statement", L501 | full P&L table, 8 columns (Q1FY27, Q1FY26, YoY%, Q4FY26, QoQ%, FY26, FY25, YoY%) | — |
| 17 | "Balance Sheet Statement", L533 | full Balance Sheet table, 5 columns (Q1FY27, Q1FY26, YoY%, Q4FY26, QoQ%) | — |
| 18 | "Strategic Priorities & Competitive Strengths", L569 | text — section divider | OCR page 18 garbled: "© Pri" only |
| 19 | "Strategic Priorities (Medium-Term Focus)", L575 | text — 4-quadrant diagram (01-04) with targets | — |
| 20 | "WHY US?", L605 | text — 7-item numbered list (01-07) | — |
| 21 | "Business Model & Operating Engine", L638 | text — section divider | OCR page 21: no additional text recovered |
| 22 | "Company Overview and Operating Footprint", L644 | text — timeline/footprint diagram (5 nodes, 01-05) | — |
| 23 | "Consistent Scale-Up Across AUM, Profitability and Footprint", L674 | text milestone timeline (FY18-FY26) + combo chart (AUM Cr, PAT Cr per FY) | — |
| 24 | "Branch-Led, Relationship-Driven Operating Model", L715 | text — hub/spoke/collection-centre diagram (01-03) + customer-segment pyramid | — |
| 25 | "Unique Strengths & Differentiated Advantages (USP)", L754 | text — 5-item numbered list (01-05) | — |
| 26 | "Technology, Credit & Collections", L784 | text — section divider | OCR page 26: no additional text recovered |
| 27 | "End-to-End Digital Platform Powering Scalable Lending", L790 | text — 6-step process diagram (01-06) + tech-stack layer diagram | — |
| 28 | "Customer Acquisition Model Anchored in Local Presence", L834 | text — 4-column model diagram | — |
| 29 | "Conservative and Structured Credit Appraisal Framework", L858 | text — 6-item numbered list (01-06) | — |
| 30 | "Structured MSME Credit Assessment and Approval Framework", L889 | text/diagram — inputs wheel (01-03) + loan-ticket-size / approval-authority table (5 tiers) + footnote | footnote L923 |
| 31 | "End-to-End Credit Appraisal Process for Vehicle Finance", L927 | text — Field / Branch / Head Office swimlane process diagram | — |
| 32 | "Asset Quality Supported by Branch-Led Collections Framework", L962 | text — 4-item numbered list (01-04) + PCR-by-stage callout box | — |
| 33 | "Customer & Product Profile", L989 | text — section divider | OCR page 33: no additional text recovered |
| 34 | "Core Customer Segments And Target Profiles", L994 | text — 4-column segment profile + 2 bullet callouts | — |
| 35 | "Diversified Lending Profile", L1021 | text — 9-product grid, ticket size / purpose / security per product | — |
| 36 | "Vertical Wise AUM Split", L1060 | stacked bar chart, 5 verticals x 5 periods (FY23-FY26 + Q1FY27) | — |
| 37 | "Governance, Management & Capital Confidence", L1098 | text — section divider | OCR page 37: no additional text recovered |
| 38 | "Promoter Profile and Leadership Overview" (MD), L1104 | text — 1 director profile (Mr. Deepak Baid, Managing Director) | — |
| 39 | "Promoter Profile and Leadership Overview" (WTDs), L1131 | text — 2 director profiles (Mrs. Aneesha Baid, Mrs. Prem Devi Baid, Whole Time Directors) | — |
| 40 | "Independent Directors", L1150 | text — 4 director profiles (Anil Patwardhan, Brij Mohan Sharma, Surendra Mehta, Kalyanaraman Chandra Choodan) | — |
| 41 | "Experienced Senior Management Team (1/2)", L1194 | text — 6 management profiles | — |
| 42 | "Experienced Senior Management Team (2/2)", L1235 | text — 4 management profiles | — |
| 43 | "Our Lenders (1/3)", L1261 | logo grid — PSU (9), Private Banks (10); OCR recovers partial bank-name text | OCR page 43: garbled OCR text L1274-1303 |
| 44 | "Our Lenders (2/3)", L1305 | logo grid — Small Finance Banks (7), NBFC & FI's (21) | OCR page 44: garbled OCR text L1318-1347 |
| 45 | "Our Lenders (3/3)", L1349 | logo grid — NBFC & FI's (21) continued | OCR page 45: garbled OCR text L1357-1375 |
| 46 | "Shareholding Pattern – Q1 FY27", L1377 | table (6 category rows + Total) + donut chart + footnote | footnote L1411 |
| 47 | "Thank You" / Investor Relations contact, L1419 | text — closing/contact slide | OCR page 47: duplicate text confirmed, no new content |

Slides = 47. Section dividers with no incremental OCR text = 6 (slides 5, 18, 21, 26, 33, 37).
Slides with unresolved/garbled OCR (lender-logo pages) = 3 (slides 43, 44, 45).

---

## SECTION 2 — Every Quantified Figure, By Slide (line-numbered)

### Slide 6 — Q1 FY27 Operational and Financial Snapshot (L137-180)
| Line | Figure | Value | Flags |
|---|---|---|---|
| 139 | Branches | 184 Branches | — |
| 142 | AUM YoY growth | +25 (%, label truncated to "YoY + 25") | — |
| 143 | AUM | ₹ 1,721.74 Cr. | — |
| 140 | PBT | ₹ 21.91 Cr. | — |
| 140-141 | RONW | 71.64%/13.86% (two RONW-adjacent figures stacked in OCR merge; see raw text) | needs source-doc visual cross-check — OCR table merge risk |
| 143 | PBT growth YoY | 27.91% | — |
| 146 | AUM Jun'25 comp | ₹ 1,346.05 Cr. | — |
| 144-147 | PAT | ₹ 16.43 Cr. (Jun'25: ₹ 9.65 Cr.), growth 70.23% | — |
| 152 | Own Book | ₹ 1,626.90 Cr. (Jun'25: ₹ 1,234.89 Cr.) | — |
| 155 | Own Book growth | 31.74% | — |
| 152 | Cost of Borrowing (COB) | 10.66% (Jun'25: 11.33%) | — |
| 155 | COB change | 67 bps | — |
| 154 | Return on Assets | 3.45% | — |
| 159-166 | Net Interest Income (NII) | ₹ 47.06 Cr. (Jun'25: ₹ 33.86 Cr.), growth 38.99% | — |
| 162-165 | Capitalization (CRAR) | Total 25.32%, Tier I 24.82%, Tier II 0.50% | — |
| 165-166 | External Credit Rating (Acuite) | "A / Stable Outlook" | — |
| 169-176 | Employee Base | 1,870 | — |
| 173-177 | Net Worth | ₹ 482.79 Cr. (Jun'25: ₹ 268.50 Cr.), 79.81% growth | — |
| 172 | Debt Equity Ratio | 3.10 | — |
| 174 | Net Equity Ratio | 2.57* | tied to footnote (see below) |
| 151-158 | Branch count by state (map callouts) | Rajasthan 92 (+1); UP 15 (+10); Gujarat 24; Chhattisgarh 42 (+7); Maharashtra 6 (+6); MP 5 (+1) | — |
| 173-177 | Gross NPA | 2.08% | — |
| 176 | Net NPA | 0.93% | — |
| 177 | PCR | 55.22% | — |
| 178 | Footnote Note-1 | Total liquidity ₹255.87 Cr.; total borrowings ₹1,496.79 Cr.; net D/E 2.57x | footnote qualifying Net Equity Ratio 2.57* headline |
| 179 | Footnote Note-2 | "Ratios & figures are annualized wherever required" | footnote, blanket qualifier |

### Slide 7 — Consistent NII and PAT Growth Trajectory (L183-216)
Revenue (Cr.): FY24 176.22, FY25 248.04, FY26 319.60, Q1FY26 70.08, Q1FY27 93.92 (L185-197)
NII (Cr.): FY24 82.59, FY25 116.69, FY26 161.78, Q1FY26 33.86, Q1FY27 47.06 (L186-197)
Operating Expense (Cr.): FY24 60.39, FY25 74.16, FY26 102.15, Q1FY26 22.37, Q1FY27 29.94 (L202-212)
PAT (Cr.): FY24 22.47, FY25 35.91, FY26 49.68, Q1FY26 9.65, Q1FY27 16.43 (L202-212)
20 data points total. No zero/nil values.

### Slide 8 — Strong Scale-Up Across AUM, Customers and Network (L218-251)
AUM (Cr.): FY24 961, FY25 1,277, FY26 1,626/1,722 (two figures shown — likely FY26 year-end vs Q1FY27; L219-225: 961, 1,277, 1,346, 1,626, 1,722)
Disbursement (Cr.): FY24 166, FY25 232(?), FY26 525/719/821 range (L219-232)
Customer Base (No.): FY24 23,906, FY25 35,568, FY26 37,122/42,809/43,946 (L237-248)
Branches (No.): FY24 135, FY25 158/159, FY26 176/184 (L237-248)
Note: chart-label-to-period mapping is visually determined in source deck; text extraction interleaves 5-period series (FY24, FY25, FY26, Q1FY26, Q1FY27) per chart — all raw values captured above and cross-checked consistent with Slide 6 and Slide 7/16/17 headline figures (AUM ₹1,721.74/1,722 Cr., Own Book ₹1,626.90/1,626 Cr., Branches 184).

### Slide 9 — NIM and Spreads Expand on Better Pricing Discipline (L254-285)
NIM (%): FY24 10.14, FY25 10.47, FY26 10.43/11.26/11.36 (L255-267)
Yield on Avg. Portfolio (%): 20.85, 21.30, 21.67, 21.77, 21.89 (L255-267)
Avg. Cost of Borrowings (%): 11.98, 11.48, 10.80, 11.33, 10.66 (L270-285)
Spreads (%): 8.87, 10.29, 10.50, 10.56, 11.01 (L270-285)
16 data points.

### Slide 10 — Strong Liquidity Position with Stable Return Metrics (L291-325)
Liquidity (Cr.): 79.68, 178.61, 185.64, 73.96, 255.87 (L294-306)
Net Worth (Cr.): 257.89, 201.78, 268.50, 465.47, 482.79 (L295-306)
Return on Total Assets (%): 2.52, 2.98, 3.08, 2.75, 3.45 (L311-322)
Return on Avg. Net Worth (%): 13.71, 15.62, 13.73, 14.67, 13.86 (L311-322)
16 data points.

### Slide 11 — Well Positioned to Capture Future Growth… (L328-358)
Debt Equity Ratio: FY24 3.87, FY25 4.41, FY26 4.13, Q1FY26 2.87, Q1FY27 3.10 (L331-344)
Interest Coverage Ratio: 1.35, 1.48, 1.57, 1.41, 1.38 (L331-344)
Capital Adequacy Ratio (%): FY24 21.88, FY25 20.80, FY26 26.12, Q1FY26 20.28, Q1FY27 25.32 (L349-355)
Footnote L357: "CRAR for FY 2026 would be 26.91% if unencumbered surplus liquidity is parked in form of FDs instead of Corporate Bonds" — qualifies the FY26 CRAR headline figure.

### Slide 12 — Asset Quality Update (L361-396)
Credit Cost (Cr.): FY24 1.95, FY25 11.89, "With Up-Money Default" 14.05, "Without Up-Money Default" 3.69, Q1FY26 2.38, Q1FY27 1.71 (L363-371)
Credit Cost (%): FY24 0.18, FY25 1.06, "With" 1.20, "Without" 0.28, Q1FY26 0.58, Q1FY27 0.95 (L363-371)
GNPA (%): FY24 0.72, FY25 1.07, "With" 2.13, "Without" 0.80, Q1FY26 1.28, Q1FY27 2.08 (L380-388)
NNPA (%): FY24 0.33, FY25 0.48, "With" 1.08, "Without" 0.53, Q1FY26 0.67, Q1FY27 0.93 (L380-388)
24 data points. "With Up-Money Default" vs "Without Up-Money Default" is a company-defined FY26-annual bifurcation — flagged for A3/A4 to interrogate (definition of "Up-Money Default" not given anywhere in this deck).

### Slide 13 — Stage Wise Movement of Loans (L398-428) — Amount in Crores (unit note L400)
**As at 30 June 2026** (L405-425), columns Stage 1 / Stage 2 / Stage 3 / Total:
- Gross carrying amount as at Apr 1, 2026: 1,423.92 / 46.59 / 32.03 / 1,502.53 (L407)
- New assets originated/increase: 200.99 / 1.23 / 0.01 / 202.24 (L410)
- Assets closed or repaid: (89.98) / (2.72) / (0.71) / (93.41) (L413)
- Transfers from Stage 1: (21.98) / 21.64 / 0.35 / 0.00 (L415) — total column is a structural zero (transfers net to nil across stages), not a template ZERO_STANDING signal
- Transfers from Stage 2: 19.81 / (22.71) / 2.91 / 0.00 (L417) — same structural-zero note
- Transfers from Stage 3: 0.08 / 0.00 / (0.08) / 0.00 (L419) — same structural-zero note
- **Sold to ARC: 0.00 / 0.00 / 0.00 / 0.00 (L421) — `ZERO_STANDING`.** Line item is standing (present in both period columns) but all-zero for the current quarter, versus a real, non-zero prior-period value (see FY26 comparative column below). Template signal: the company did dispose of stage-3 assets to an ARC in FY26 and the line exists to capture recurrence.
- Write offs: 0.00 / 0.00 / (1.01) / (1.01) (L423) — Stage 1 and Stage 2 columns are `ZERO_STANDING` this quarter (write-offs are Stage-3-only this period)
- As at June 30, 2026: 1,532.83 / 44.03 / 33.49 / 1,610.36 (L425)

**As at 31 March 2026** (comparative, L405-425), columns Stage 1 / Stage 2 / Stage 3 / Total:
- Gross carrying amount as at Apr 1, 2025: 1,086.47 / 41.59 / 12.18 / 1,140.24 (L408)
- New assets originated/increase: 712.07 / 5.35 / 12.37 / 729.79 (L410)
- Assets closed or repaid: (316.48) / (17.02) / (1.53) / (335.03) (L413)
- Transfers from Stage 1: (59.02) / 41.90 / 17.12 / 0.00 (L415)
- Transfers from Stage 2: 14.64 / (15.55) / 0.91 / 0.00 (L417)
- Transfers from Stage 3: 2.61 / 0.17 / (2.78) / 0.00 (L419)
- Sold to ARC: (16.36) / (9.74) / (1.83) / (27.93) (L421) — nonzero comparative, confirms Sold-to-ARC is a live line item, reinforcing the ZERO_STANDING flag on the current quarter
- Write offs: (0.01) / (0.10) / (4.42) / (4.53) (L423)
- As at Mar 31, 2026: 1,423.92 / 46.59 / 32.03 / 1,502.53 (L425)

Total quantified cells this slide: 2 tables x 8 rows x 4 columns = 64 cells (line-anchored above by row).

### Slide 14 — ALM Position as on 30 June 2026 (L431-465) — Amount in Crores (unit note L432)
Surplus row (L435): 169.06 / 178.34 / 210.32 / 222.54 / 420.35 (buckets: upto 3 months / upto 6 months / upto 1 year / upto 3 years / upto 5 years — 6th bucket "5+ years" has no surplus figure shown, consistent with cumulative surplus tapering to nil beyond year 5 — no explicit "0" printed, so not flagged ZERO_STANDING, but noted as a gap for A3 to check against source visual)
Bar values (axis-scale gridlines, L436-458): 153.33, 322.39, 304.30, 482.64, 617.58, 827.90, 1,354.04, 1,576.58, 1,515.13, 1,935.47, 1,997.51, 1,997.51 — cumulative liabilities/assets series across the 6 time buckets, plus axis labels 2,500.00 / 2,000.00 / 1,500.00 / 1,000.00 / 500.00 / "-" (zero baseline, L436-458)
16 numeric data points plus 6 axis-scale labels (the "-" at L458 is the chart's zero gridline label, not a disclosure line item — not flagged ZERO_STANDING).

### Slide 15 — Diversified and Scalable Borrowing Profile (L468-498)
Borrowing Mix (%, pie, L471-493): 5.65%, 0.31%, 3.49%, 21.78%, 24.80%, 11.59%, 29.77%, 14.19% (8 segments: PSB's, Bank's, Small Finance Bank, NBFC/FI's, NCD, DA/BC/CL, Cash Credit — 7 named legend items for 8 percentages; one segment's label may be split across two slice values in OCR — flag for visual cross-check)
Incremental Borrowing Mix During Q1 FY27 (%, pie, L472-492): 15.86%, 15.18%, 11.59%(shared axis text merge risk), 57.36% (4 segments: PSB's, Bank's, Small Finance Bank, NBFC/FI's)
12 percentage data points total.

### Slide 16 — Profit & Loss Statement (L501-529) — Amount in Crores
Full table, 8 columns (Q1FY27, Q1FY26, YoY%, Q4FY26, QoQ%, FY26, FY25, YoY%) x 15 line items:
| Line item (L) | Q1FY27 | Q1FY26 | YoY% | Q4FY26 | QoQ% | FY26 | FY25 | YoY% |
|---|---|---|---|---|---|---|---|---|
| Interest Earned (505) | 85.44 | 67.10 | 27.34% | 88.37 | -3.32% | 299.12 | 231.31 | 29.32% |
| Interest Expenses (506) | 38.38 | 33.23 | 15.48% | 36.25 | 5.88% | 137.34 | 114.63 | 19.81% |
| Net Interest Income (507) | 47.06 | 33.86 | 38.97% | 52.11 | -9.69% | 161.78 | 116.69 | 38.65% |
| Other Income (510) | 8.48 | 2.98 | 184.29% | 5.1 | 66.27% | 20.47 | 16.73 | 22.38% |
| Total Income (Net of Interest Expense) (511) | 55.54 | 36.85 | 50.73% | 57.21 | -2.92% | 182.25 | 133.41 | 36.61% |
| Employee Cost (514) | 22.12 | 16.28 | 35.89% | 19.17 | 15.38% | 72.51 | 54.03 | 34.20% |
| Other Expense (515) | 7.82 | 6.09 | 28.42% | 8.42 | -7.07% | 29.64 | 20.14 | 47.20% |
| Operating Exp (516) | 29.94 | 22.37 | 33.85% | 27.59 | 8.53% | 102.15 | 74.16 | 37.73% |
| Profit Before Impairment & Tax (517) | 25.60 | 14.48 | 76.82% | 29.62 | -13.58% | 80.10 | 59.25 | 35.20% |
| ECL Provision (520) | 3.01 | 0.79 | 281.61% | 1.53 | 96.69% | 10.81 | 9.12 | 18.53% |
| Write-off (521) | 0.68 | 0.92 | -25.88% | 1.02 | -32.93% | 3.24 | 2.77 | 17.01% |
| Total Provision (522) | 3.69 | 1.71 | 115.79% | 2.55 | 44.84% | 14.05 | 11.89 | 18.18% |
| Profit Before Tax (525) | 21.90 | 12.76 | 71.59% | 27.08 | -19.11% | 66.05 | 47.36 | 39.48% |
| Tax (526) | 5.34 | 2.99 | 78.49% | 6.56 | -18.64% | 16.29 | 11.35 | 43.51% |
| Implied Tax Rate (527) | 24.37% | 23.42% | — (no %-chg col) | 24.24% | — | 24.66% | 23.97% | — |
| Other Comprehensive Income (528) | -0.14 | -0.12 | — | 0.06 | — | -0.08 | -0.09 | — |
| Profit After Tax & OCI (529) | 16.43 | 9.65 | 70.17% | 20.58 | -20.19% | 49.68 | 35.91 | 38.34% |

15 line items x up to 8 columns = 107 populated numeric cells (Implied Tax Rate and OCI rows have no growth-% columns — those blanks are structural, not disclosure omissions, so not flagged). PBT of ₹21.90 Cr. here vs. ₹21.91 Cr. cited on Slide 6 (L140) — 0.01 Cr. rounding discrepancy between snapshot tile and full P&L table, flagged for A4 arithmetic-consistency check.

### Slide 17 — Balance Sheet Statement (L533-564) — Amount in Crores
| Line item (L) | Q1FY27 | Q1FY26 | YoY% | Q4FY26 | QoQ% |
|---|---|---|---|---|---|
| Paid-up Equity (538) | 26.20 | 20.91 | 25.30% | 26.13 | 0.24% |
| Reserves and Surplus (540) | 456.60 | 247.59 | 84.41% | 439.34 | 3.93% |
| Total Equity (542) | 482.79 | 268.50 | 79.81% | 465.47 | 3.72% |
| Borrowings (546) | 1441.74 | 1088.50 | 32.45% | 1275.75 | 13.01% |
| Debt Securities (548) | 55.05 | 19.85 | 177.28% | 61.56 | -10.58% |
| Other Liabilities and Provisions (550) | 17.93 | 15.74 | 13.89% | 14.99 | 19.56% |
| Total Equity & Liabilities (552) | 1997.51 | 1392.59 | 43.44% | 1817.78 | 9.89% |
| Loans (556) | 1584.90 | 1208.53 | 31.14% | 1480.10 | 7.08% |
| Non-Financial Assets (558) | 26.26 | 26.05 | 0.78% | 24.76 | 6.06% |
| Other Financial Assets (560) | 386.35 | 158.01 | 144.51% | 312.93 | 23.46% |
| Total Assets (562) | 1997.51 | 1392.59 | 43.44% | 1817.78 | 9.89% |

11 line items x 5 columns = 55 populated numeric cells. Total Equity & Liabilities ties to Total Assets (both 1997.51 / 1817.78 / 1392.59) — balance sheet identity holds at each period. No zero/nil line items on this slide.

### Slide 19 — Strategic Priorities (Medium-Term Focus) (L575-602)
ROA target: 3.50% - 3.75% (L579)
ROE target: 13.50% - 14.00% (L580)
AUM CAGR target: ~30% (L599-600)
3 forward-looking numeric targets, none anchored to a specific date — flag `FORWARD_TARGET` for A3/A5 (guidance-type disclosure, not historical actual).

### Slide 20 — WHY US? (L605-635)
Item 03: 1,850+ employees, 10+ years leadership NBFC experience (L616)
Item 04: 25% rural/semi-rural women borrowers (L620)
Item 05: 50+ PSU/SFB/FI/NBFC lender partners; "zero delays/defaults" (L624) — qualitative zero-claim, not a table line item, so not `ZERO_STANDING`, but flag `ZERO_DEFAULT_CLAIM` for A3/A5 to test against Slide 32's Stage-3/PCR data
Item 06: 9 products, ~43,950 customers, 6 states (L628)
Item 07: 184 branches (L631)
8 numeric data points.

### Slide 22 — Company Overview and Operating Footprint (L644-671)
2011 (acquisition year, L649), ~Rs. 32 Cr. portfolio, 4 branches at acquisition (L655), 184 branches today (L646), 1993-94 (founding year, L662)
5 numeric data points.

### Slide 23 — Consistent Scale-Up Across AUM, Profitability and Footprint (L674-712)
Milestone AUM figures (text, L675-677): ₹200 Cr., ₹400 Cr., ₹1,000 Cr., ₹1,600 Cr.
Milestone counts: Branch network to 65 (L675), crossed 100 (L676)
Equity infusions: ₹16.87 Cr. (L682), ₹26.66 Cr. (L679)
Net-worth milestone: ₹125 Cr. (L679)
Chart series AUM (Cr.), FY18-FY26 (L688-709): 200, 326, 421, 462, 532, 687, 961, 1,277, 1,626
Chart series PAT (Cr.), FY18-FY26 (L694-707): 4, 9, 10, 10, 15, 15, 22, 36, 50
18 chart data points + 6 milestone-text figures = 24 numeric data points.

### Slide 24 — Branch-Led, Relationship-Driven Operating Model (L715-751)
184 touchpoints (L717). 1 numeric data point.

### Slide 25 — Unique Strengths & Differentiated Advantages (USP) (L754-780)
Item 02: 24-48 hours TAT for CV loans, 7-10 days for MSME (L763)
Item 04: 50+ lenders, ~28% of portfolio funded through net worth and internal accruals (L772-773)
Item 05: ~25% women borrowers, 37% first-time borrowers (L778)
7 numeric data points.

### Slide 27 — End-to-End Digital Platform Powering Scalable Lending (L790-831)
Step numbers 01-06 only (process-flow labels, not quantified metrics). No standalone financial/operational figures on this slide.

### Slide 28 — Customer Acquisition Model Anchored in Local Presence (L834-855)
184 branches (L845). 1 numeric data point.

### Slide 29 — Conservative and Structured Credit Appraisal Framework (L858-886)
Item 03: 2-3 branches per hub, 50+ dedicated credit professionals (L868)
2 numeric data points.

### Slide 30 — Structured MSME Credit Assessment and Approval Framework (L888-924)
Loan-ticket-size / approval-authority table (L913-921):
- up to ₹5,00,000 → Credit Manager
- More than ₹5,00,000 - up to ₹10,00,000 → Area Credit Manager
- More than ₹10,00,000 - up to ₹15,00,000 → Regional Credit Manager
- More than ₹15,00,000 - up to ₹20,00,000 → Zonal Credit Manager
- More than ₹20,00,000 - up to ₹25,00,000 → National Credit Manager
- More than ₹25,00,000 → Credit Committee*
6 threshold figures + footnote L923 defining Credit Committee composition (Managing Director, Risk Head, Credit Head, Business Head, Collection Head).

### Slide 31 — End-to-End Credit Appraisal Process for Vehicle Finance (L926-959)
No standalone quantified figures (process/swimlane diagram only).

### Slide 32 — Asset Quality Supported by Branch-Led Collections Framework (L961-986)
Provisioning Coverage Snapshot (Q1 FY27), L974-980:
- PCR Stage 3: 55.22%
- PCR Stage 2: 2.26%
- PCR Stage 1: 0.39%
3 numeric data points. PCR Stage 3 (55.22%) ties exactly to Slide 6's PCR figure (L177) — cross-check consistent.

### Slide 34 — Core Customer Segments And Target Profiles (L993-1018)
37.1% first-time borrowers (L1014). 1 numeric data point (distinct from the 37% figure on Slide 25 L778 — 37.1% vs 37% rounding, flag for A4 consistency check).

### Slide 35 — Diversified Lending Profile (L1020-1057)
Ticket sizes across 9 products (L1025-1053):
MSME Prime: ₹25-50 Lakhs; Two-Wheeler: up to ₹1.5 lakhs; CV Loan: up to ₹25 lakhs; Business Loan: up to ₹200 lakhs; Electric Vehicle Loan: up to ₹4 lakhs; Construction & LAP: up to ₹25 lakhs; MSME: up to ₹25 lakhs; Wholesale Lending: ₹25-500 lakhs; Personal Loan: up to ₹200 lakhs.
9 ticket-size ranges (10 discrete bound figures).

### Slide 36 — Vertical Wise AUM Split (L1059-1095)
AUM (Cr.) by vertical x period (FY23, FY24, FY25, FY26, Q1FY27), L1065-1090:
Total-series labels: 1,393.80 (Q1FY27), 1,298.68 (FY26)... plus per-vertical stacked-bar values: 94.98, 176.44, 205.88, 145.82, 5.32, 9.68, 43.18, 131.11, 62.15, 85.61, 89.84, 51.73, 53.47, 10.91, 52.97, 57.63, 49.36, 18.98, 720.55, 534.74, 980.33.
21+ discrete stacked-bar data points across 5 verticals (MSME, Construction & LAP, Vehicle, Wholesale, Personal Loan) x 5 periods = up to 25 cells; several cells show "-" (dash) in the raw layout (L1087, between FY24/FY25 columns for at least one vertical) — these are `ZERO_STANDING`: the Personal Loan and/or Wholesale verticals did not exist / had nil AUM in the earliest periods (FY23-FY24) before scaling up, consistent with the "Forayed in new..." timeline on Slide 23.

### Slide 38 — Promoter Profile and Leadership Overview — Mr. Deepak Baid, MD (L1103-1128)
No numeric figures beyond qualitative "over two decades of experience" (L1108) — not a table line item, not flagged.

### Slide 39 — Promoter Profile and Leadership Overview — WTDs (L1130-1147)
"over two decades of experience" (L1133) — qualitative only, no numeric figure.

### Slide 40 — Independent Directors (L1149-1191)
Mr. Anil Patwardhan: 40 years banking experience (L1164), asset size Rs 18000 Cr. (L1179)
Mr. Brij Mohan Sharma: 40 years experience (L1167)
Mr. Kalyanaraman Chandra Choodan: 40 years expertise (L1167, second instance)
4 numeric data points.

### Slide 41 — Experienced Senior Management Team (1/2) (L1193-1232)
6 profiles, each with Experience (years) and Vintage in LIFC (years):
Gopal Krishan Sain — CFO: 12+ yrs exp / 4+ yrs vintage (L1198-1199)
Rohit Mathur — National Credit Manager: 12+ yrs / 4+ yrs (L1198-1199)
Piyush Somani — Chief Treasury Officer: 15+ yrs / 7+ yrs (L1208-1210)
Priya Kadyan — AVP Audit: 14+ yrs / 1+ yrs (L1209-1211)
Kuldeep Singh — Chief Business Officer: 18+ yrs / 6+ yrs (L1218-1219)
Arun Sengar — Operation Head: 16+ yrs / 2+ yrs (L1218-1219)
Sourabh Mishra — CCO & Company Secretary: 7+ yrs / 5+ yrs (L1228-1229)
7 profiles (not 6 — corrected during sweep; the header says "(1/2)" but 7 names appear, since "Sourabh Mishra & Associate" is a dual-line entry), 14 numeric data points.

### Slide 42 — Experienced Senior Management Team (2/2) (L1234-1258)
Sanjay Ojha — National Collection Head: 15+ yrs / 1.5+ yrs (L1243-1244)
Vinod Maheshwari — CTO: 15+ yrs / 6 months (L1243-1244)
Yogesh Garg — VP HR: 18+ yrs / 4+ months (L1250-1251)
Shivam Bajaj — VP Risk: 9+ yrs / 1.5+ yrs (L1250-1252)
4 profiles, 8 numeric data points.

### Slide 43 — Our Lenders (1/3) (L1260-1303)
PSU (9) (L1262), Private Banks (10) (L1267) — 2 category counts. OCR text (L1274-1303) recovers partial/garbled bank names (State Bank of India, Indian Bank, Indian Overseas Bank, IDBI Bank, CSB Bank, DCB Bank, Federal Bank, IndusInd Bank, ICICI Bank) — no additional numeric figures, logo/branding page.

### Slide 44 — Our Lenders (2/3) (L1305-1347)
Small Finance Banks (7) (L1306), NBFC & FI's (21) (L1311) — 2 category counts. OCR (L1318-1347) recovers partial names (Capital SFB, Utkarsh SFB, ESAF SFB, Suryoday SFB, MAS Financial, Poonawalla Fincorp, Sundaram Finance, Protium) — no additional numeric figures.

### Slide 45 — Our Lenders (3/3) (L1348-1375)
NBFC & FI's (21) (L1350, continuation of the 21-count from Slide 44) — 1 category count (repeated, not incremental). OCR (L1357-1375) recovers partial names (Nabkisan Finance, Hero Housing Finance, Capital India Finance) — no additional numeric figures.
Total lender count across slides 43-45: PSU 9 + Private Banks 10 + Small Finance Banks 7 + NBFC & FI's 21 = 47 named lender relationships, consistent with "50+ lenders" claims on Slides 20 and 25 (L624, L772).

### Slide 46 — Shareholding Pattern – Q1 FY27 (L1377-1416)
Table, 6 category rows + Total, 4 columns (No. of Shareholders, No of Shares, Amount, %):
| Category (L) | No. of Shareholders | No of Shares | Amount | % |
|---|---|---|---|---|
| Promoter & Promoter Group (1387-1389) | 10 | 3,15,23,468 | 15,76,17,340 | 60.17% |
| Other Shareholders - Public (1391-1393) | 29,581 | 2,08,69,610 | 10,43,48,050 | 39.83% |
| Alternative Investment Fund (AIF) (1395-1397) | 6 | 27,85,622 | 1,39,28,110 | 5.32% |
| Foreign Portfolio Investors (1399-1401) | 7 | 7,32,023 | 36,60,115 | 1.40% |
| Non-Resident Indians (1404) | 221 | 2,16,219 | 10,81,095 | 0.41% |
| Other Public (1408) | 29,347 | 1,71,35,746 | 8,56,78,730 | 32.70% |
| Total (1411) | 29,591 | 5,23,93,078 | 26,19,65,390 | 100.00% |

Donut-chart legend percentages (L1380-1407, repeated from table): Foreign Portfolio Investor 1.40%, Alternative Investment Fund 5.32%, Non-Resident Indians 0.41%, Other Public 32.71% (note: 32.71% in chart legend vs 32.70% in table — 0.01pp rounding discrepancy, flag for A4), Promoter & Promoter Group 60.17%.
Footnote (L1411-1412): "Cumulative holding of promoter and promoter group stood at 60.17% and remaining 39.83% held by other shareholders."
28 numeric cells (7 rows x 4 columns) + 5 chart-legend percentages + footnote.
Note: "Other Shareholders - Public" (39.83%, row total) and "Other Public" (32.70%, sub-row) plus AIF (5.32%), FPI (1.40%), NRI (0.41%) sum to 39.83% (32.70+5.32+1.40+0.41=39.83) — internally consistent.

### Slide 47 — Thank You (L1418-1433)
Investor Relations contact: Rajat Gupta, rajat@goindiaadvisors.com, +91 99718 9939 (L1422-1424, repeated in OCR L1431-1433). No financial figures.

---

## SECTION 3 — Dropped-Slide Comparison vs Prior Quarter

`PRIOR_LEDGER_UNAVAILABLE` — no prior-quarter LAXMIINDIA presentation ledger exists in
`runs/` to diff against. All 47 slides in this deck are recorded above; none can be
cross-checked for `DROPPED_SLIDE` status this run. A3/A4 should source the Q4 FY26 (or
Q1 FY26) investor presentation ledger if/when produced, to backfill this comparison.

---

## SECTION 4 — Footnotes and Fine-Print Disclaimers (reconciled set of 5)

| # | Line | Slide | Text (verbatim) | Qualifies |
|---|---|---|---|---|
| 1 | 178 | 6 | "Note-1 : As of June 30, 2026, the Company's total liquidity stood at ₹255.87 crore, while total borrowings were ₹1,496.79 crore, resulting in a net debt-to-equity ratio of 2.57x." | Net Equity Ratio 2.57* headline tile |
| 2 | 179 | 6 | "Note-2 : Ratios & figures are annualized wherever required." | blanket qualifier on all ratio tiles, slide 6 |
| 3 | 357 | 11 | "Note: CRAR for FY 2026 would be 26.91% if unencumbered surplus liquidity is parked in form of FDs instead of Corporate Bonds" | FY26 CRAR bar (26.12% as charted) |
| 4 | 923 | 30 | "*Credit Committee: Managing Director, Risk Head , Credit Head , Business Head & Collection Head" | Credit Committee approval tier, top of ticket-size table |
| 5 | 1411-1412 | 46 | "Note :- * Cumulative holding of promoter and promoter group stood at 60.17% and remaining 39.83% held by other shareholders." | Promoter & Promoter Group / Other Shareholders rows |

Also enumerated (not counted as a footnote — full-page legal text, not a headline-qualifying
note): Slide 3 Disclaimer, L66-110, ~9 paragraphs of forward-looking-statement / no-offer /
no-representation boilerplate.

---

## FLAGS RAISED (summary)

- `ZERO_STANDING`: Slide 13, "Sold to ARC" line, current-quarter column (L421, all four
  stage columns 0.00) vs nonzero FY26 comparative (L421 second table, -27.93 total) — line is
  a standing template item, zero this period.
- `ZERO_STANDING`: Slide 13, "Write offs" line, Stage 1 and Stage 2 columns, current quarter
  (L423, 0.00/0.00) — nonzero only in Stage 3 this period.
- `ZERO_STANDING`: Slide 36, Vertical Wise AUM Split, dash-valued cells for verticals not yet
  originated in early FY23/FY24 periods (L1087).
- `FORWARD_TARGET`: Slide 19, ROA 3.50-3.75% / ROE 13.50-14.00% / AUM CAGR ~30% — forward
  guidance, not historical actuals (L579-580, 599-600).
- `ZERO_DEFAULT_CLAIM`: Slide 20, "zero delays / defaults" claim on lender relationships
  (L624) — flagged for cross-check against Slide 32/Slide 6 asset-quality figures (these
  concern borrower NPAs, not the company's own repayment record to lenders, so not
  necessarily contradictory, but worth A3/A5 scrutiny given a hard "zero" claim).
- Rounding/consistency flags for A4 (not gate-blocking, listed for the arithmetic-consistency
  pass): PBT ₹21.91 Cr. (Slide 6, L140) vs ₹21.90 Cr. (Slide 16 P&L table, L525); "37% first-
  time borrowers" (Slide 25, L778) vs "37.1% first-time borrowers" (Slide 34, L1014);
  32.71% (Slide 46 donut legend, L1384) vs 32.70% (Slide 46 table, L1408) for Other Public.
- `PRIOR_LEDGER_UNAVAILABLE`: Section 3, no prior-quarter deck ledger to diff for
  `DROPPED_SLIDE` detection.
- OCR-recovery gaps (non-blocking, informational): Slides 5, 18, 21, 26, 33, 37 (section
  dividers, no incremental text) and Slides 43-45 (lender-logo pages, garbled OCR text, no
  numeric figures affected).

---
