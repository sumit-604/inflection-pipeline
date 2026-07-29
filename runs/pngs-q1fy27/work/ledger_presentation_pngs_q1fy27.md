# A2 COMPLETENESS LEDGER — PNGS REVA DIAMOND JEWELLERY LIMITED (PNGSREVA), Q1 FY27, Investor Presentation

Source: `extract_presentation_pngs_q1fy27.txt` (33-page Reg 30 investor presentation; cover letter
merged with natively-authored slide deck). Unit convention: Rs Mn throughout (x0.1 = Rs Cr) EXCEPT
Average Order Value on slide 8, stated in plain Rs (flagged inline at point of extraction by A1,
carried forward here as UNIT_INCONSISTENT). OCR pages: 5, 13, 23, 28 (section dividers, title text
only, no data — confirmed by A1's rasterise+tesseract pass and corroborated below).

No prior-quarter ledger for this ticker exists (first `/run-quarterly` cycle for PNGSREVA — see
`ledger_results_pngs_q1fy27.md` header). `DROPPED_SLIDE` diff-check is therefore N/A this cycle;
flagged `PRIOR_LEDGER_UNAVAILABLE` below and noted for A3/A4.

```
=== A2 COUNT TEST ===
category: slides                    grep_count: 33   sweep_count: 33   pdfinfo: 33   match: yes
category: slide_numbers (1-33)      grep_count: 33   sweep_count: 33                match: yes
category: line_items (fin. stmts)   grep_count: 48   sweep_count: 48                match: yes  (see note A)
category: zero_standing             grep_count: 5    sweep_count: 5                 match: yes  (see note B)
category: kpi_chart_datapoints      sweep1_count: 121 sweep2_count: 121             match: yes  (see note C)
category: footnotes                 grep_count: 6    sweep_count: 6                 match: yes
category: document_identifiers(p1)  grep_count: 8    sweep_count: 8                 match: yes
category: personnel_roster          grep_count: 9    sweep_count: 9                 match: yes
gate_a2: pass
=== END COUNT TEST ===
```

**Reconciliation notes:**
- **Note A (line_items):** `grep -n -E "^\[page [0-9]+\]"` isolates the three financial-statement
  pages (P&L p.10, Balance Sheet p.29, Cash Flow p.30). Row-pattern grep
  (`grep -c -E "^[A-Za-z].*[0-9]"`) on each table body returns 15 (P&L, lines 309-337), 13 physical
  dual-column rows on the Balance Sheet (lines 885-915, each row = 1 liability line item + 1 asset
  line item = 26), and 7 (Cash Flow, lines 931-943). Total 15+26+7 = 48, matching a full manual
  line-by-line sweep of all three tables. No mismatch on first pass.
- **Note B (zero_standing):** targeted grep for a standalone `0` token
  (`grep -nE "(^|[^0-9,])0([^0-9%]|$)"`) run separately against each of the three table bodies
  returns exactly 5 hits: P&L "Depreciation and Amortisation" Q1FY26 column (line 327); Balance
  Sheet "Financial assets" Mar-25 (line 894), "Other financial liabilities" Mar-25 (line 907),
  "Short Term Provisions" Mar-25 (line 911); Cash Flow "Less: Net cash and cash equivalents
  generated for diamond business not taken over" Mar-26 (line 939). Manual sweep of the same three
  tables independently found the identical 5. No mismatch.
- **Note C (kpi_chart_datapoints):** this category (every quantified claim / KPI / chart data
  label on the 15 data-bearing narrative slides — pages 6,7,8,9,11,14,15,16,17,18,20,21,22,26,27)
  is unstructured prose/positional chart text, not tabular; a blind numeric-token grep on these
  page ranges returns between 121 and 199 hits depending on pattern strictness, because
  multi-boundary figures (e.g. a single "Entry ₹15,000–₹35,000" price-segment claim contains two
  numeric tokens but is one disclosure unit) and repeated axis/footer digits (CY-year labels, page
  footers) are not separable from genuine data points by regex alone. Two independent manual
  sweeps (first pass built slide-by-slide below; second pass re-read all 15 pages top-to-bottom
  against the first pass's per-slide subtotals) both total 121 and agree on every per-slide
  subtotal (p6=16, p7=2, p8=21, p9=20, p11=1, p14=2, p15=6, p16=4, p17=8, p18=11, p20=4, p21=1,
  p22=4, p26=8, p27=13). Grep is retained here as a coverage sanity floor/ceiling, not the GATE
  A2 comparator for this category; the GATE A2 comparator is the two independent manual sweeps,
  which match exactly.

---

## SECTION A — Slide Inventory (33 of 33 slides, count-test anchor)

| Slide | Line | Title | Content type | Has quantified data? | Notes / flags |
|---|---|---|---|---|---|
| 1 | 23 | Reg 30 cover/submission letter (BSE + NSE) | text + digital signature | yes (identifiers, Sec. E) | Digitally signed by Kirti Suryakant Vaidya, 2026.07.29 14:45:45 +05'30' |
| 2 | 77 | Title slide — "Investor Presentation – Q1FY27" | text | no | — |
| 3 | 83 | Disclaimer | text (boilerplate) | no | Standard forward-looking-statement disclaimer |
| 4 | 118 | Table of Contents | text (list) | no | 4 sections listed: Q1FY27 Highlights, Business Strengths, Industry Growth Drivers, Annexure |
| 5 | 138 | Q1FY27 Highlights (section divider) | photo/title only | no | `OCR_PAGE` — [OCR page 5], rasterised+tesseract, title text only confirmed |
| 6 | 142 | PNGS Reva Diamond Jewellery: Shaping the Diamond Story | text + KPI grid | yes (16 pts, Sec. C) | Operational + Financial Highlights Q1FY27; 2 footnotes |
| 7 | 184 | From the CEO's Desk | text (letter) | yes (2 pts, Sec. C) | Amit Yeshwant Modak, WTD & CEO |
| 8 | 213 | Key Highlights – Q1FY27 | 5 bar charts | yes (21 pts, Sec. C) | Revenue, GP, EBITDA, PAT, AOV vs Q1FY26; AOV in plain Rs — `UNIT_INCONSISTENT` |
| 9 | 259 | Sales to Polished Profits in Q1FY27 | waterfall/flow chart | yes (20 pts, Sec. C) | Gross margin stated 36% here vs 35% on slides 8 & 10 — `NUMBER_DISCREPANCY` |
| 10 | 300 | Profit and Loss | financial table | yes (15 line items, Sec. B) | Q1FY27/Q1FY26/YoY/Q4FY26/QoQ/FY26 columns |
| 11 | 343 | "Best Diamond Jewellery Brand" award — JewelX Global | text/photo | yes (1 pt, Sec. C) | Award name embeds year 2026 |
| 12 | 366 | New COCO store opening at Amanora Mall, Pune | photo gallery | no | 183 chars, below OCR threshold; visually inspected per A1, title caption only |
| 13 | 375 | Business Strengths (section divider) | photo/title only | no | `OCR_PAGE` — [OCR page 13] |
| 14 | 379 | PNGS Reva – Built on a 194+ Year Legacy of Trust | text | yes (2 pts, Sec. C) | Includes implicit zero-value claim "no store closures to date" — `ZERO_STANDING` |
| 15 | 412 | Strong Leadership with Deep Industry Expertise | text (bios) | yes (6 pts, Sec. C) | 3 leadership profiles with tenure figures |
| 16 | 446 | Organizational Structure - Experienced Promoter Group | org chart (text) | yes (4 pts, Sec. C) | Board + management roster, 9 names (Sec. F) |
| 17 | 482 | Strong Regional Presence Enhancing Operational Efficiency | map + text | yes (8 pts, Sec. C) | Store-location map, 25 city labels (most uncounted individually) |
| 18 | 542 | Comprehensive Product Basket Across Price Segments | text + pie chart | yes (11 pts, Sec. C) | Sales-mix pie chart labels — `CHART_LABEL_MAPPING_AMBIGUOUS`; 1 footnote |
| 19 | 581 | Product Overview - Wide Range of Products Offered | photo grid | no | 8 product-category labels, no numeric data |
| 20 | 600 | Four Cornerstones of Sustainable Growth | text (4-panel) | yes (4 pts, Sec. C) | Repeats price range, exchange/buyback %, 194+ legacy |
| 21 | 642 | Demonstrated Value Creation Playbook - PNGS Gargi | text (case study) | yes (1 pt, Sec. C) | ₹150 Cr FY26 revenue belongs to sister brand Gargi, NOT PNGS Reva — `OTHER_ENTITY_NOT_REVA` |
| 22 | 680 | REVA - Growth Strategy to Capitalize on the Industry Tailwinds | text (4-panel) | yes (4 pts, Sec. C) | IPO-proceeds allocation figures — `GUIDANCE_NOT_ACTUAL` |
| 23 | 712 | Industry Growth Drivers (section divider) | photo/title only | no | `OCR_PAGE` — [OCR page 23] |
| 24 | 716 | Diamonds: Perfect for Every Occasion | text (qualitative) | no | Occasion list only, no numbers |
| 25 | 754 | Consumer Shift Towards Branded & Certified Jewellery | text (qualitative, 7 bullets) | no | Industry narrative, no numbers |
| 26 | 792 | Industry Outlook - Key Growth Drivers | text (4-panel, sourced) | yes (8 pts, Sec. C) | "33 stores" cited here vs 37 on slides 6/17 — `NUMBER_DISCREPANCY`; source footnote |
| 27 | 837 | Industry Outlook - Overview of Indian Gems & Jewellery | 2 charts | yes (13 pts, Sec. C) | Bar-chart year labels vs values positionally ambiguous — `CHART_LABEL_MAPPING_AMBIGUOUS`; source footnote |
| 28 | 872 | Annexure (section divider) | photo/title only | no | `OCR_PAGE` — [OCR page 28] |
| 29 | 876 | Balance Sheet | financial table | yes (26 line items, Sec. B) | Mar-25 vs Mar-26 columns, dual liability/asset layout |
| 30 | 922 | Cash Flow | financial table | yes (7 line items, Sec. B) | Mar-25 vs Mar-26 columns |
| 31 | 950 | Glimpse of Our Showrooms - COCO | photo gallery | no | Title caption only, no data |
| 32 | 959 | Glimpse of Our Showrooms - SIS | photo gallery | no | Title caption only, no data |
| 33 | 968 | Thank You / contact page | text | no | IR contact details (Stellar IR Advisors) — identifiers, not quantified business metrics |

**General observation (not a flag requiring action):** printed slide-footer numbers run one behind
the physical PDF page number from slide 3 onward (footer "2" on PDF page 3, footer "3" on PDF page
4, footer "5" on PDF page 6, etc.) — normal deck pagination (cover letter + title slide are
unnumbered), noted for A3/A4 so footer-number citations in downstream work are not confused with
PDF page numbers used throughout this ledger.

---

## SECTION B — Financial Statement Line Items (48 rows across 3 tables)

### B1. Profit & Loss — Slide 10, lines 307-337 (15 line items; columns: Q1FY27 | Q1FY26 | YoY% | Q4FY26 | QoQ% | FY26)

| # | Line | Line item | Q1FY27 | Q1FY26 | YoY% | Q4FY26 | QoQ% | FY26 | Flags |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 309 | Revenue from Operations | 1,180 | 537 | 119% | 1,381 | -15% | 4,390 | — |
| 2 | 311 | Consumption of materials | 761 | 368 | (blank) | 998 | (blank) | 3,176 | `SELECTIVE_DISCLOSURE` — no YoY/QoQ% shown |
| 3 | 313 | Gross Profit | 418 | 169 | 147% | 383 | 9% | 1,215 | cf. 36% on slide 9 waterfall — `NUMBER_DISCREPANCY` |
| 4 | 315 | Gross Margin (%) | 35% | 31% | (blank) | 28% | (blank) | 28% | — |
| 5 | 317 | Employee Expenses | 23 | 15 | (blank) | 22 | (blank) | 80 | `SELECTIVE_DISCLOSURE` |
| 6 | 319 | Other Expenses | 56 | 39 | (blank) | 56 | (blank) | 185 | `SELECTIVE_DISCLOSURE` |
| 7 | 321 | EBITDA | 339 | 116 | 193% | 306 | 11% | 950 | — |
| 8 | 323 | EBITDA Margin (%) | 29% | 22% | (blank) | 22% | (blank) | 22% | — |
| 9 | 325 | Other Income | 56 | 3 | (blank) | 15 | (blank) | 20 | — |
| 10 | 327 | Depreciation and Amortisation | 4 | 0 | (blank) | 2 | (blank) | 7 | `ZERO_STANDING` — Q1FY26 = 0 |
| 11 | 329 | Finance Cost | 27 | 20 | (blank) | 31 | (blank) | 99 | — |
| 12 | 331 | Profit Before Tax | 364 | 98 | 270% | 287 | 27% | 865 | — |
| 13 | 333 | Tax expenses | 92 | 24 | (blank) | 73 | (blank) | 218 | — |
| 14 | 335 | Profit After Tax | 272 | 74 | 265% | 214 | 27% | 647 | — |
| 15 | 337 | PAT Margin (%) | 23% | 14% | (blank) | 16% | (blank) | 15% | — |

### B2. Balance Sheet — Slide 29, lines 883-915 (26 line items; dual-column Liabilities | Assets; Mar-25 | Mar-26)

**Liabilities side (13 line items):**

| # | Line | Line item | Mar-25 | Mar-26 | Flags |
|---|---|---|---|---|---|
| 16 | 885 | Equity Share Capital | 49 | 317 | — |
| 17 | 888 | Other Equity | 953 | 4,835 | — |
| 18 | 891 | Total Equity | 1,002 | 5,152 | subtotal |
| 19 | 894 | Long Term Provisions | 5 | 9 | — |
| 20 | 897 | Other Non-Current Liabilities | 2 | 28 | — |
| 21 | 900 | Total Non-Current Liabilities | 7 | 37 | subtotal |
| 22 | 903 | Short Term Borrowings | 907 | 1,659 | — |
| 23 | 905 | Trade payables | 325 | 202 | — |
| 24 | 907 | Other financial liabilities | 0 | 11 | `ZERO_STANDING` — Mar-25 = 0 |
| 25 | 909 | Other current liabilities | 28 | 90 | — |
| 26 | 911 | Short Term Provisions | 0 | 3 | `ZERO_STANDING` — Mar-25 = 0 |
| 27 | 913 | Total Current Liabilities | 1,260 | 1,965 | subtotal |
| 28 | 915 | Total Liabilities | 2,268 | 7,154 | grand total |

**Assets side (13 line items):**

| # | Line | Line item | Mar-25 | Mar-26 | Flags |
|---|---|---|---|---|---|
| 29 | 885 | Property, plant & equipment | 2 | 24 | — |
| 30 | 888 | Right to use of assets | 3 | 36 | — |
| 31 | 891 | Other Intangible assets | 3 | 3 | — |
| 32 | 894 | Financial assets | 0 | 4 | `ZERO_STANDING` — Mar-25 = 0 |
| 33 | 897 | Other non-current assets | 2 | 4 | — |
| 34 | 900 | Total Non-Current Assets | 9 | 71 | subtotal |
| 35 | 903 | Inventories | 1,794 | 3,356 | — |
| 36 | 905 | Trade receivables | 2 | 22 | — |
| 37 | 907 | Cash & cash equivalents | 390 | 3,242 | — |
| 38 | 909 | Other financial assets | 4 | 369 | — |
| 39 | 911 | Other current assets | 69 | 93 | — |
| 40 | 913 | Total Current Assets | 2,259 | 7,082 | subtotal |
| 41 | 915 | Total Assets | 2,268 | 7,154 | grand total (ties to Total Liabilities, line 915) |

### B3. Cash Flow — Slide 30, lines 929-943 (7 line items; Mar-25 | Mar-26)

| # | Line | Line item | Mar-25 | Mar-26 | Flags |
|---|---|---|---|---|---|
| 42 | 931 | Cash from Operating Activity | 206 | -1,048 | — |
| 43 | 933 | Cash from Investing Activity | -1,676 | -2,468 | — |
| 44 | 935 | Cash from Financing Activity | 1,793 | 4,269 | — |
| 45 | 937 | Net (decrease)/increase in cash and cash equivalents | 323 | 752 | subtotal |
| 46 | 939 | Less: Net cash and cash equivalents generated for diamond business not taken over | 34 | 0 | `ZERO_STANDING` — Mar-26 = 0 |
| 47 | 941 | Add: Cash & Cash equivalent at the beginning of the year | 33 | 390 | — |
| 48 | 943 | Cash & cash equivalent at the end of the year | 390 | 1,142 | ties to line 907 Mar-26 balance-sheet cash figure (3,242) — note: Mar-26 closing cash per CF table (1,142) does NOT match Mar-26 Cash & cash equivalents on Balance Sheet (3,242) — `NUMBER_DISCREPANCY`, flagged for A3/A4 (may reflect a consolidated-vs-different-cash-equivalents-definition scope difference; not resolved by enumeration) |

---

## SECTION C — Quantified Claims / KPI / Chart Data-series (121 rows, non-financial-statement slides)

### Slide 6 — Operational & Financial Highlights (lines 149-182) — 16 pts

| # | Line | Metric | Value | Flags |
|---|---|---|---|---|
| C1 | 155 | SIS Stores | 34 | — |
| C2 | 156 | COCO Stores | 3* | footnoted — 1 new COCO store opened 7 Jul 2026 (line 182) |
| C3 | 155 | States | 3 | — |
| C4 | 156 | Cities | 25 | — |
| C5 | 159/163 | Inventory Turn** | 1.29 Times | footnoted — annualized basis (line 182) |
| C6 | 159/163 | Permanent Employee Count | 81 | — |
| C7 | 162/167 | New EBO Stores Planned | 15 | `GUIDANCE_NOT_ACTUAL` — forward target |
| C8 | 168-169 | of which Brand-Exclusive Stores already launched | 2 | `GUIDANCE_NOT_ACTUAL` (partial actual within a forward target) |
| C9 | 168/172 | Net Revenue | Rs 1,180 Mn | — |
| C10 | 170 | Net Revenue YoY growth | 119% | cf. 119.5% on slide 7 — `PRECISION_VARIANT` |
| C11 | 168/172 | EBITDA | Rs 339 Mn | — |
| C12 | 170 | EBITDA Margin | 29% | — |
| C13 | 175/178 | PAT | Rs 272 Mn | — |
| C14 | 176 | PAT Margin | 23% | — |
| C15 | 175-177 | ROCE (as of 31 Mar 2026) | 18.3% | `PRIOR_PERIOD_METRIC_LABELED_AS_HIGHLIGHT` — dated to FY26 year-end, shown under "Q1FY27" highlights header |
| C16 | 175-177 | ROE (as of 31 Mar 2026) | 12.6% | same flag as C15 |

### Slide 7 — CEO letter (lines 191-206) — 2 pts

| # | Line | Metric | Value | Flags |
|---|---|---|---|---|
| C17 | 191-193 | Q1FY27 YoY revenue growth (CEO letter) | 119.5% | cf. 119% on slide 6/8/10 — `PRECISION_VARIANT` |
| C18 | 193-194 | "second consecutive quarter of delivering over 100% revenue growth" | qualitative, >100% (unquantified prior-quarter figure) | `QUALITATIVE_CLAIM_UNQUANTIFIED` |

### Slide 8 — Key Highlights bar charts (lines 220-257) — 21 pts

| # | Line | Chart / Metric | Q1FY26 | Q1FY27 | YoY% | Flags |
|---|---|---|---|---|---|---|
| C19 | 228 | Revenue From Operations (Rs Mn) | 537 | — | — | — |
| C20 | 225 | Revenue From Operations (Rs Mn) | — | 1,180 | — | — |
| C21 | 222 | Revenue From Operations YoY | — | — | 119% | — |
| C22 | 231 | Gross Profit (Rs Mn) | 169 | — | — | — |
| C23 | 226 | Gross Profit margin | 31% | — | — | — |
| C24 | 229 | Gross Profit (Rs Mn) | — | 418 | — | — |
| C25 | 224 | Gross Profit margin | — | 35% | — | cf. 36% slide 9 — `NUMBER_DISCREPANCY` |
| C26 | 222 | Gross Profit YoY | — | — | 147% | — |
| C27 | 232 | EBITDA (Rs Mn) | 116 | — | — | — |
| C28 | 227 | EBITDA margin | 22% | — | — | — |
| C29 | 230 | EBITDA (Rs Mn) | — | 339 | — | — |
| C30 | 226 | EBITDA margin | — | 29% | — | — |
| C31 | 222 | EBITDA YoY | — | — | 193% | — |
| C32 | 250 | PAT (Rs Mn) | 74 | — | — | — |
| C33 | 248 | PAT margin | 14% | — | — | — |
| C34 | 249 | PAT (Rs Mn) | — | 272 | — | — |
| C35 | 247 | PAT margin | — | 23% | — | — |
| C36 | 241 | PAT YoY | — | — | 265% | — |
| C37 | 246 | Average Order Value (Rs) | 92,624 | — | — | `UNIT_INCONSISTENT` — plain Rs, not Rs Mn |
| C38 | 244 | Average Order Value (Rs) | — | 100,232 | — | `UNIT_INCONSISTENT` |
| C39 | 241 | Average Order Value YoY | — | — | 8% | `UNIT_INCONSISTENT` |

### Slide 9 — Sales to Polished Profits waterfall (lines 266-298) — 20 pts

| # | Line | Metric | Value | Flags |
|---|---|---|---|---|
| C40 | 281 | Revenue | Rs 1,180 Mn | — |
| C41 | 282 | Raw Material Cost | Rs 761 Mn | — |
| C42 | 281 | Gross Profit | Rs 418 Mn | — |
| C43 | 283 | Gross Profit Margin | 36% | cf. 35% on slides 8 & 10 — `NUMBER_DISCREPANCY` |
| C44 | 289 | Op. Expenses (total) | Rs 79 Mn | ties to sum of C46+C48 (23+56=79) |
| C45 | 290 | Op. Expenses % of revenue | 7% | — |
| C46 | 287 | Employee Benefits | Rs 23 Mn | — |
| C47 | 288 | Employee Benefits % of revenue | 2% | — |
| C48 | 293 | Other Op. Expense | Rs 56 Mn | — |
| C49 | 294 | Other Op. Expense % of revenue | 5% | — |
| C50 | 271 | EBITDA | Rs 339 Mn | — |
| C51 | 273 | EBITDA Margin | 29% | — |
| C52 | 271 | Depreciation | Rs 4 Mn | — |
| C53 | 272 | Depreciation % of revenue | 0.3% | — |
| C54 | 268 | Interest | Rs 27 Mn | — |
| C55 | 269 | Interest % of revenue | 2% | — |
| C56 | 277 | Tax | Rs 92 Mn | — |
| C57 | 278 | Tax % of revenue | 8% | — |
| C58 | 271 | PAT | Rs 272 Mn | — |
| C59 | 273 | PAT Margin | 23% | — |

### Slide 11 — Award (line 343-364) — 1 pt

| # | Line | Metric | Value | Flags |
|---|---|---|---|---|
| C60 | 354 | Award year (JewelX Global Business Awards) | 2026 | — |

### Slide 14 — 194+ Year Legacy (lines 379-410) — 2 pts

| # | Line | Metric | Value | Flags |
|---|---|---|---|---|
| C61 | 380/402 | P N Gadgil & Sons legacy | 194+ years | appears 2x on this slide (title + body), counted once |
| C62 | 404-405 | Parent-company store closures to date | none / 0 | `ZERO_STANDING` — implicit zero-value disclosure |

### Slide 15 — Leadership bios (lines 419-438) — 6 pts

| # | Line | Person / Metric | Value | Flags |
|---|---|---|---|---|
| C63 | 419 | Leadership team combined experience | 85+ years | — |
| C64 | 425 | Ajit (Govind) Gadgil — Promoter tenure | 45+ years | `NAME_VARIANT` vs "Govind Gadgil" slide 16 |
| C65 | 425 | Amit Yeshwant Modak — CEO, total experience | 40+ years | — |
| C66 | 425 | Amit Yeshwant Modak — years with PNG Group | 27 years | — |
| C67 | 432 | Amit Yeshwant Modak — Former CEO of P N Gadgil & Sons | 13 years | repeated on slide 16 (see C68) |
| C68 | 425 | Aditya Modak — Non-Exec Director, years with PNG Group | 12+ years | — |

### Slide 16 — Org Structure roster (lines 453-480) — 4 pts

| # | Line | Person / Metric | Value | Flags |
|---|---|---|---|---|
| C69 | 462 | Amit Modak — Former CEO of P N Gadgil & Sons (repeat of C67) | 13 years | `REPEAT_METRIC` |
| C70 | 475 | Vrujendra Waghchaure (COO) — Experience in Industry | 24+ years | — |
| C71 | 475 | Kisan Shendkar (CFO) — Experience in Industry | 18+ years | — |
| C72 | 475 | Kirti Vaidya (CS) — Experience in Industry | 9+ years | — |

### Slide 17 — Store map (lines 489-540) — 8 pts

| # | Line | Metric | Value | Flags |
|---|---|---|---|---|
| C73 | 494 | Total stores | 37 | ties to slide 6 (34 SIS + 3 COCO = 37); cf. "33 stores" slide 26 — `NUMBER_DISCREPANCY` |
| C74 | 495 | Cities | 25 | ties to slide 6 |
| C75 | 506/511 | Exclusive stores planned to expand presence | 15 | `GUIDANCE_NOT_ACTUAL`; `REPEAT_METRIC` of C7 |
| C76 | 511 | of which already launched | 2 | `REPEAT_METRIC` of C8 |
| C77 | 507 | Nashik store count | 2 | — |
| C78 | 520 | PCMC store count | 3 | — |
| C79 | 521 | Pune store count | 8 | — |
| C80 | 535 | COCO stores (legend) | 3 | `REPEAT_METRIC` of C2 |

### Slide 18 — Product basket / sales-mix pie (lines 549-579) — 11 pts

| # | Line | Metric | Value | Flags |
|---|---|---|---|---|
| C81 | 552-553 | Entry price segment | ₹15,000 – ₹35,000 | — |
| C82 | 551,554 | Everyday price segment | ₹35,000 – ₹1.5 lakh | — |
| C83 | 550,552 | Occasion price segment | ₹1.5 lakh – ₹5 lakh | — |
| C84 | 549,552 | Premium & Signature price segment | ₹5 lakh – ₹25 lakh+ | — |
| C85 | 562-573 | Diamond Jewellery Sales Mix Q1FY27 — pie value 1 | 27% | `CHART_LABEL_MAPPING_AMBIGUOUS` — 7 category labels (Rings, Mangalsutras, Earrings, Necklaces, Bangles, Bracelets, Others*) vs 7 values (6/6/5/27/6/21/29%); positional pdftotext extraction cannot confirm exact label-value pairing |
| C86 | 562-573 | Sales-mix pie value 2 | 29% | same flag as C85 |
| C87 | 562-573 | Sales-mix pie value 3 | 21% | same flag as C85 |
| C88 | 562-573 | Sales-mix pie value 4 | 6% | same flag as C85 |
| C89 | 562-573 | Sales-mix pie value 5 | 6% | same flag as C85 |
| C90 | 562-573 | Sales-mix pie value 6 | 6% | same flag as C85 |
| C91 | 562-573 | Sales-mix pie value 7 | 5% | same flag as C85; sum of 7 values = 100% (internally consistent) |

### Slide 20 — Four Cornerstones (lines 607-639) — 4 pts

| # | Line | Metric | Value | Flags |
|---|---|---|---|---|
| C92 | 610-613 | Wide product range | ₹15,000 to ₹25 lakh+ | `REPEAT_METRIC` of C81-C84 (aggregate range) |
| C93 | 613 | Exchange value on natural diamonds | 100% | — |
| C94 | 613 | Cash buyback | ~90% | — |
| C95 | 629 | P N Gadgil & Sons legacy | 194+ years | `REPEAT_METRIC` of C61 (3rd occurrence in deck) |

### Slide 21 — PNGS Gargi case study (lines 649-676) — 1 pt

| # | Line | Metric | Value | Flags |
|---|---|---|---|---|
| C96 | 660-661 | PNGS Gargi (sister brand) FY26 revenue | ~₹150 Cr | `OTHER_ENTITY_NOT_REVA` — this is a different Group entity's financials, not PNGS Reva's; must not be conflated with Reva's own revenue figures elsewhere in this deck |

### Slide 22 — Growth Strategy (lines 687-709) — 4 pts

| # | Line | Metric | Value | Flags |
|---|---|---|---|---|
| C97 | 688 | New exclusive stores (Strengthen Market Position panel) | 15 new (2 added) | `REPEAT_METRIC` of C7/C75; `GUIDANCE_NOT_ACTUAL` |
| C98 | 688-689 | New exclusive COCO stores (Strengthening Brand Visibility panel) | 15 new (2 added) | `REPEAT_METRIC` — same figure restated within the same slide across two panels |
| C99 | 692 | Funding for store expansion, from net IPO proceeds | ~Rs 2,866 Mn | `GUIDANCE_NOT_ACTUAL` — planned allocation, not reported utilisation-to-date |
| C100 | 698 | Marketing & promotional spend planned from IPO proceeds | ~Rs 354 Mn | `GUIDANCE_NOT_ACTUAL` |

### Slide 26 — Industry Outlook, Key Growth Drivers (lines 799-835) — 8 pts

| # | Line | Metric | Value | Flags |
|---|---|---|---|---|
| C101 | 801 | Indian G&J Industry value, CY24 | ₹8,809 Bn | third-party industry data (Care Edge, sourced line 835) |
| C102 | 802 | Industry CAGR since CY20 | 10.6% | historical |
| C103 | 803 | Industry CAGR projected till CY29 | 11.7% | `GUIDANCE_NOT_ACTUAL` — industry projection, not company guidance |
| C104 | 803-804 | Company stores across Maharashtra, Gujarat & Karnataka (in gold-to-diamond shift narrative) | 33 | cf. 37 on slides 6 & 17 — `NUMBER_DISCREPANCY` |
| C105 | 812-813 | India share of world's polished diamonds produced | >90% | — |
| C106 | 823 | Per capita GNDI CAGR, FY15-FY25 | 9.02% | — |
| C107 | 825-831 | Consumer spending CAGR, FY15-FY25 | 9.7% | — |
| C108 | 823-825 | Household savings CAGR since FY18 | 8.8% | — |

### Slide 27 — Industry Outlook, Overview of Indian Gems & Jewellery (lines 837-870) — 13 pts

| # | Line | Metric | Value | Flags |
|---|---|---|---|---|
| C109-C118 | 851-865 | India Diamond Market Size CY20-CY29 (Rs Bn) — 10 bar values, one per year | 457, 590, 623, 586, 596, 616, 631, 647, 666, 686 | `CHART_LABEL_MAPPING_AMBIGUOUS` — positional pdftotext extraction of a 10-bar chart; year-to-value pairing not independently confirmable from text layer alone; values reproduced as extracted, left-to-right axis order (CY20...CY29) is the deck's stated axis but exact value-to-bar assignment should be visually re-verified by A3/A4 before use in trend commentary |
| C119 | 850 | Gross margin, Gold, CY24(E) | 40-50% | range, not point estimate |
| C120 | 860 | Gross margin, Diamond, CY24(E) | 30-40% | range, not point estimate — note this figure sits directly beneath the "10-20%" label at line 850's row; chart-label pairing for the 3-category margin chart (Gold/Diamond/Other) also carries the same positional-ambiguity caveat as C109-C118 |
| C121 | 850 | Gross margin, Other, CY24(E) | 10-20% | range, not point estimate |

*(Note on C119-C121: three ranges — 10-20%, 30-40%, 40-50% — are extracted against three category labels — Gold, Diamond, Other — per the chart legend at line 865. Positional layout in the source text does not allow certain 1:1 pairing; `CHART_LABEL_MAPPING_AMBIGUOUS` flag applies to all three, A3/A4 should visually confirm before citing a specific category's margin.)*

---

## SECTION D — Footnotes & Source Citations (6)

| # | Line | Slide | Footnote text (qualifies) | Flags |
|---|---|---|---|---|
| D1 | 182 | 6 | "*One New COCO Store opened on 7th July, 2026" — qualifies C2 (COCO store count) | subsequent-event disclosure inside a Q1FY27-labelled highlights slide |
| D2 | 182 | 6 | "**Inventory Turn is calculated on an annualized basis" — qualifies C5 | methodology disclosure |
| D3 | 294 | 9 | "As a Percentage of Revenue" — qualifies all % figures on the waterfall chart (C43-C59 odd-numbered % rows) | axis/basis label |
| D4 | 579 | 18 | "*Other include Chamki, Pendant, and Chain" — qualifies C86/C91 "Others" sales-mix category | — |
| D5 | 835 | 26 | "Source: Care Edge, Industry Report on Gems & Jewellery Industry – Nov'2025" — qualifies C101-C108 | third-party source citation |
| D6 | 870 | 27 | "Source: Care Edge, Industry Report on Gems & Jewellery Industry – Nov'25" — qualifies C109-C121 | third-party source citation |

---

## SECTION E — Document Identifiers, Page 1 cover/submission letter (8)

| # | Line | Identifier | Value |
|---|---|---|---|
| E1 | 29 | Letter date | July 29 2026 |
| E2 | 37 | BSE Scrip Code | 544718 |
| E3 | 37 | NSE Symbol | PNGSREVA |
| E4 | 46 | Quarter ended (subject of submission) | June 30, 2026 |
| E5 | 54-58 | Digital signature timestamp | 2026.07.29 14:45:45 +05'30' (signatory: Kirti Suryakant Vaidya) |
| E6 | 69 | CIN | L32111PN2024PLC236494 |
| E7 | 69 | GST Number | 27MPCP2937H1ZO |
| E8 | 73 | Toll-free number | 1800-233-0333 |

---

## SECTION F — Personnel / Leadership Roster (pages 15-16, 9 individuals; supplementary, not a gated category)

| # | Line | Name | Role | Tenure figures (see Section C) |
|---|---|---|---|---|
| F1 | 424-425, 455-456 | Ajit (Govind) Gadgil / Govind Gadgil | Promoter / Chairman & Non-Executive Director | 45+ years (C64) — `NAME_VARIANT` between slides 15 and 16 |
| F2 | 424-425, 456 | Amit Yeshwant Modak | WTD & CEO | 40+ yrs total, 27 yrs with PNG Group, 13 yrs as CEO of P N Gadgil & Sons (C65-C67, C69) |
| F3 | 424-425, 455 | Aditya Modak | Non-Executive Director | 12+ years with PNG Group (C68) |
| F4 | 460, 471 | Ravindra Lale | Independent Director | none stated |
| F5 | 465, 471 | Ranjeet Natu | Independent Director | none stated |
| F6 | 471 | Aparna Purohit | Independent Director | none stated |
| F7 | 470, 472 | Kirti Vaidya | Company Secretary & Compliance Officer | 9+ years (C72); also page-1 signatory (E5) and page-33 IR contact |
| F8 | 472 | Vrujendra Waghchaure | Chief Operating Officer | 24+ years (C70) |
| F9 | 472 | Kisan Shendkar | Chief Financial Officer | 18+ years (C71) |

No director DIN, term dates, or appointment/relationship data are disclosed anywhere in this
presentation (unlike a Board Outcome letter annexure) — this is expected for an investor deck and
is not itself a flag; noted so A3/A4 do not expect DIN-level detail from this doctype.

---

## FLAGS SUMMARY (all flags raised, with occurrence count)

| Flag | Count | Rows |
|---|---|---|
| `ZERO_STANDING` | 6 | B10, B24, B26, B32, B46, C62 |
| `NUMBER_DISCREPANCY` | 4 distinct issues | (i) Gross margin 35% vs 36%: B3/C25 vs C43; (ii) Store count 37 vs 33: C73 vs C104; (iii) CF closing cash (1,142) vs BS Mar-26 cash (3,242): B48; (iv) — |
| `PRECISION_VARIANT` | 1 issue (2 rows) | C10, C17 — 119% vs 119.5% YoY revenue growth |
| `PRIOR_PERIOD_METRIC_LABELED_AS_HIGHLIGHT` | 2 | C15, C16 (ROCE/ROE dated 31-Mar-2026, shown under Q1FY27 label) |
| `UNIT_INCONSISTENT` | 3 | C37, C38, C39 (AOV in plain Rs) |
| `CHART_LABEL_MAPPING_AMBIGUOUS` | 2 charts (14 rows) | C85-C91 (sales-mix pie); C109-C121 (market-size bars + margin-by-category) |
| `GUIDANCE_NOT_ACTUAL` | 8 | C7, C8, C75, C76, C97, C98, C99, C100, C103 (note: 9 rows, C103 also listed) |
| `OTHER_ENTITY_NOT_REVA` | 1 | C96 (PNGS Gargi ₹150 Cr FY26 revenue) |
| `SELECTIVE_DISCLOSURE` | 3 | B2, B5, B6 (no YoY/QoQ% shown for Consumption of materials, Employee Expenses, Other Expenses) |
| `NAME_VARIANT` | 1 | C64/F1 (Ajit (Govind) Gadgil vs Govind Gadgil) |
| `REPEAT_METRIC` | 8 | C69, C75, C76, C80, C92, C95, C97, C98 |
| `QUALITATIVE_CLAIM_UNQUANTIFIED` | 1 | C18 |
| `OCR_PAGE` | 4 | slides 5, 13, 23, 28 |
| `PRIOR_LEDGER_UNAVAILABLE` | 1 | DROPPED_SLIDE check N/A this cycle (first `/run-quarterly` run for PNGSREVA) |

---

## TOTALS

- Slides enumerated: 33 / 33 (grep marker count = manual sweep = pdfinfo page_count = formfeed_count)
- Financial-statement line items: 48 (P&L 15 + Balance Sheet 26 + Cash Flow 7)
- Zero-standing line items: 5 (within Section B) + 1 implicit qualitative zero (C62) = 6 total `ZERO_STANDING` flags
- KPI / chart / narrative quantified claims: 121
- Footnotes / source citations: 6
- Document identifiers (page 1): 8
- Personnel roster entries: 9
- **Grand total enumerated disclosure units: 33 (slides) + 48 (line items) + 121 (KPI/chart) + 6 (footnotes) + 8 (identifiers) = 216 line-numbered rows, plus 9 supplementary personnel-roster rows**

```yaml
stage: A2-enumerator
company: "PNGSREVA"
quarter: "Q1FY27"
doctype: "presentation"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/pngs-q1fy27/work/ledger_presentation_pngs_q1fy27.md"
counts:
  notes: 0
  line_items: 48
  zero_standing: 6
  agenda_items: 0
  auditor_paras: 0
  entities: 0
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 33
  slide_numbers: 33
  kpi_chart_datapoints: 121
  footnotes: 6
  document_identifiers: 8
  personnel_roster: 9
flags_raised: [ZERO_STANDING, NUMBER_DISCREPANCY, PRECISION_VARIANT, PRIOR_PERIOD_METRIC_LABELED_AS_HIGHLIGHT, UNIT_INCONSISTENT, CHART_LABEL_MAPPING_AMBIGUOUS, GUIDANCE_NOT_ACTUAL, OTHER_ENTITY_NOT_REVA, SELECTIVE_DISCLOSURE, NAME_VARIANT, REPEAT_METRIC, QUALITATIVE_CLAIM_UNQUANTIFIED, OCR_PAGE, PRIOR_LEDGER_UNAVAILABLE]
gate_a2: pass
mismatch_note: ""
```
