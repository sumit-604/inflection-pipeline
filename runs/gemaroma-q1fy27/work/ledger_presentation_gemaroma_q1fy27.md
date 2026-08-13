# A2 ENUMERATION LEDGER — Gem Aromatics Limited (GEMAROMA) — Q1FY27 — Investor Presentation

Source: `extract_presentation_gemaroma_q1fy27.txt` (33 PDF pages; deck runs PDF pages 2-33,
PDF page 1 is a Regulation 30 covering letter bundled into the same file). Slide number =
PDF page number per task instruction, matching the extract's `[page N]` markers, NOT the
deck's own internal footer numeral (which is offset by one on most content slides and by
two on the annexure section, per A1 header note).

Prior-quarter ledger: **NONE** — first-time coverage of this company. `DROPPED_SLIDE` check
(item 3 of the presentation enumeration branch) is therefore **not applicable this run**;
this ledger becomes the baseline against which Q2FY27's ledger will diff.

=== A2 COUNT TEST ===
```
category: slides                          grep_count: 33   sweep_count: 33   match: yes
category: ocr_pages                       grep_count: 7    sweep_count: 7    match: yes
category: charts                          grep_count: 3    sweep_count: 3    match: yes
category: financial_tables                grep_count: 5    sweep_count: 5    match: yes
category: table_line_items                grep_count: 88   sweep_count: 88   match: yes
category: footnotes_sourcenotes           grep_count: 12   sweep_count: 12   match: yes
category: slide_kpi_numbers (narrative)   sweep_pass1: 95  sweep_pass2: 95   match: yes  (method: two independent manual sweeps — no single regex reliably captures heterogeneous Rs/USD/%/count/year formats across narrative slides; grep proxy run for sanity check only, not authoritative)
category: guidance_forward_statements     sweep_pass1: 11  sweep_pass2: 11   match: yes
category: capacity_capex_margin_orderbook sweep_pass1: 14  sweep_pass2: 14   match: yes  (incl. 2 DATA_ABSENT rows: no installed-capacity tonnage disclosed, no order-book figure disclosed)
category: strategic_claims                sweep_pass1: 17  sweep_pass2: 17   match: yes
gate_a2: pass
```
=== END COUNT TEST ===

Grep commands used (reproducible):
- `grep -c -E "^\[page [0-9]+\]"` → 33
- `grep -c -E "^\[CHART"` → 3
- `grep -c -E "^\[OCR page"` → 7
- `grep -n -E "\(Rs Cr\)\s+(Q1FY27|FY23|Mar-23)"` → 5 table-header lines (pages 9, 10, 27, 28 [combined Liabilities+Assets header on one line], 29)
- `grep -n -E "^(Net Revenue From Operations|Cost of Goods Sold|Gross Profit...|...|Cash PAT)"` → 51 = 17 line items × 3 P&L tables (pages 9, 10, 27)
- Balance sheet (page 28): 12 paired liability/asset rows × 2 = 24 line items (manually verified against `sed -n '950,976p'` content)
- Cash flow (page 29): 13 line items confirmed via label-anchored grep
- `grep -n -E "Rounded off to nearest decimal|^Source:|^Note:|^\*"` → 12 footnote/source-note lines

---

## 1. SLIDE INDEX (33 slides; slide number = PDF page number)

| # | Page | Title / First words | Content type | OCR'd | Notes |
|---|------|---------------------|---------------|-------|-------|
| 1 | 1 | "Manufacturer & Exporters of Essential Oils..." (Reg 30 covering letter) | text (cover letter, bundled non-deck page) | No | BSE 544491 / NSE GEMAROMA (line 41), CIN L24246MH1997PLC111057 (line 30), dated Aug 13 2026 (line 34), digitally signed by Akshita Deepak Gohil, CS & Compliance Officer, timestamp 2026.08.13 19:13:15 +05'30' (lines 63-66) |
| 2 | 2 | "Investor Presentation Q1FY27" (title slide) | text/title | **Yes** | native text 26 chars; OCR confirms same |
| 3 | 3 | "Disclaimer" | text (legal boilerplate) | No | Forward-looking-statement disclaimer qualifying entire deck; footer "2" (line 121) |
| 4 | 4 | "Table of Contents" | text/list | **Yes** | 4 sections: Q1FY27 Highlights, Company Overview, Annual Financials, Annexure (line 128-146); footer "3" (line 150) |
| 5 | 5 | "Q1FY27 Highlights" (section divider) | text/title | **Yes** | No footer numeral visible in extract |
| 6 | 6 | "Management Commentary" | text (CEO quote) | No | Speaker: Yash Vipul Parekh, MD & CEO (line 195-196); footer "5" (line 202); no numeric figures |
| 7 | 7 | "Q1FY27 Financial Performance" | text + chart (dashboard tiles) | No | 23 discrete KPI figures — see Section 3; footer "6" (line 247); chart at line 250 |
| 8 | 8 | "Key Business Updates" | text (5 subsections) | No | Contains 3 GUIDANCE items (Cooling Agents/Safranal/Phenol Derivatives) — see Section 5; footer "7" (line 283) |
| 9 | 9 | "Standalone Profit & Loss Statement" | table | No | 17 line items, Q1FY27/Q1FY26/YoY%/Q4FY26/QoQ% — see Section 2; footer "8" (line 326) |
| 10 | 10 | "Consolidated Profit & Loss Statement" | table | No | 17 line items, same period columns — see Section 2; footer "9" (line 369) |
| 11 | 11 | "Company Overview" (section divider) | text/title | **Yes** | native text 15 chars |
| 12 | 12 | "~A Journey of 3 Decades leading to Growth and Transformation…" | text/timeline (12 milestones, 1997-2026) | No | 7 numeric milestone figures — see Section 3; footer "11" (line 412) |
| 13 | 13 | "…Established Scale with a Strong Market Presence" | text/stat-tiles | No | 7 capability stats — see Section 3; footer "12" (line 446) |
| 14 | 14 | "Mint & Mint Derivative – Well Established Business" | text/segment page | No | 6 market-sizing + revenue figures — see Section 3; source footnote (line 480); footer "13" |
| 15 | 15 | "Clove & Clove Derivatives – High-Value Segment with Leadership in Eugenol" | text/segment page | No | 6 figures; source footnote (line 514); footer "14" |
| 16 | 16 | "Entering Advanced Chemistry with Phenol Derivatives" | text/segment page | No | 6 figures; source footnote (line 548); footer "15" |
| 17 | 17 | "Citral Chemistry (New Products) and Other Natural & Synthetic Ingredients" | text/segment page | No | 3 figures incl. ~58% Eucalyptus Oil market-share claim; source footnote (line 583); footer "16" |
| 18 | 18 | "Focus on Growing Value-Added Products – From Base to Advanced Molecules" | table (product mapping) | No | Qualitative product-category map, no new numeric figures; footer "17" |
| 19 | 19 | "Experienced Promoters and Management Team…(1/2)" | text/bios (3 directors) | No | 3 figures — see Section 3; footer "18" |
| 20 | 20 | "Experienced Promoters and Management Team…(2/2)" | text/bios (7 directors) | No | 4 figures — see Section 3; footer "19" |
| 21 | 21 | "Strategically Located Manufacturing Facilities with Advanced Capabilities" | text/map + facility cards | No | 3 establishment years + 5 certification numbers — see Section 3; footnote (line 735); footer "20" |
| 22 | 22 | "Fueling Future Growth – Greenfield Project at Dahej" | text (Krystal Ingredients Dahej deep-dive) | No | Repeats page-8 Cooling Agents/Safranal/Phenol Derivatives guidance verbatim (flag `REPEAT_DISCLOSURE`); ~Rs 270 Cr investment, 15% tax rate — see Sections 5-6; footer "21" |
| 23 | 23 | "From India to the World: Strengthening Our Global Presence" | text + chart (donut + world map) | No | Repeats 240/44/20 customer-country stats (page 13); Geography split chart — see Sections 3-4; footnote (line 816-817); footer "22" |
| 24 | 24 | "With Complex and Advanced End-to-End Processes" | text/process flow ("Journey of a Molecule") | No | Qualitative process-technology and reaction-chemistry claims, no numeric KPIs; footer "23" |
| 25 | 25 | "Strong and Robust R&D Capabilities Driving Innovation" | text | No | 13 Qualified Scientists (repeat of page 13); footer "24" |
| 26 | 26 | "Annual Financials" (section divider) | text/title | **Yes** | native text 16 chars |
| 27 | 27 | "Consolidated Profit & Loss Statement" (FY23-FY26) | table | No | 17 line items — see Section 2; footer "26" (line 944) |
| 28 | 28 | "Consolidated Balance Sheet" (Mar-23 to Mar-26) | table | No | 24 line items — see Section 2; footer "27" (line 978) |
| 29 | 29 | "Consolidated Cash Flow Statement" (FY23-FY26) | table | No | 13 line items — see Section 2; footer "28" (line 1015) |
| 30 | 30 | "Annexure" (section divider) | text/title | **Yes** | native text 8 chars |
| 31 | 31 | "Dahej Plant Pictures" | photo | **Yes** | No numeric content; footer "30" |
| 32 | 32 | "Stock Information & Shareholding Pattern" | text + chart (pie) | No | 9 figures + 4 shareholding % — see Sections 3-4; footer "31" (line 1072) |
| 33 | 33 | "Thank You" (contact/IR page) | text | No | CIN L24246MH1997PLC111057 (repeat); contact details for company and Stellar IR Advisors; no other numerics |

**Slide count reconciliation:** grep `^\[page N\]` markers = 33; manual sweep of the table above = 33. **Match: yes.**

---

## 2. FINANCIAL TABLES — FULL LINE-ITEM INVENTORY (5 tables, 88 line items)

All five tables carry the "Rounded off to nearest decimal" footnote. **Zero-standing check
performed across all periods in all five tables: no line item is zero, nil, or dash in
every period shown. `ZERO_STANDING` count = 0** (all cells are populated, including
negative figures such as Consolidated PAT Rs (7.9) Cr, which is a real negative value, not
a nil/dash template line, and therefore does not qualify for the flag).

### 2a. Standalone P&L Statement — page 9, lines 289-323 (Q1FY27 / Q1FY26 / YoY% / Q4FY26 / QoQ%)
| # | Line item | Line # | Q1FY27 | Q1FY26 | YoY% | Q4FY26 | QoQ% | Flags |
|---|-----------|--------|--------|--------|------|--------|------|-------|
| 1 | Net Revenue From Operations | 291 | 83.0 | 76.4 | 8.6% | 112.2 | -26.1% | |
| 2 | Cost of Goods Sold | 293 | 68.3 | 57.3 | — | 86.0 | — | no YoY/QoQ% given for this row |
| 3 | Gross Profit | 295 | 14.7 | 19.1 | -23.2% | 26.2 | -44.0% | |
| 4 | Gross Profit Margin (%) | 297 | 17.7% | 25.0% | -734 bps | 23.4% | -566 bps | |
| 5 | Employee Expenses | 299 | 3.1 | 3.4 | — | 2.6 | — | no YoY/QoQ% given |
| 6 | Other Expenses | 301 | 3.1 | 5.2 | — | 8.5 | — | no YoY/QoQ% given |
| 7 | EBITDA | 303 | 8.5 | 10.5 | -19.0% | 15.1 | -43.4% | |
| 8 | EBITDA Margin (%) | 305 | 10.3% | 13.8% | -350 bps | 13.4% | -315 bps | |
| 9 | Other Income | 307 | 4.2 | 2.6 | — | 3.8 | — | no YoY/QoQ% given |
| 10 | Finance Cost | 309 | 1.3 | 2.9 | — | 1.5 | — | no YoY/QoQ% given |
| 11 | Depreciation | 311 | 1.6 | 1.4 | — | 1.4 | — | no YoY/QoQ% given |
| 12 | PBT Before Exceptional Items | 313 | 9.7 | 8.7 | 11.5% | 16.0 | -39.1% | |
| 13 | Tax Expense | 315 | 2.5 | 2.2 | — | 4.1 | — | no YoY/QoQ% given |
| 14 | PAT | 317 | 7.3 | 6.5 | 11.2% | 11.9 | -38.9% | |
| 15 | PAT Margin (%) | 319 | 8.7% | 8.5% | 20 bps | 10.6% | -183 bps | |
| 16 | EPS (Rs) | 321 | 1.4 | 1.4 | — | 2.3 | — | no YoY/QoQ% given |
| 17 | Cash PAT | 323 | 8.9 | 8.0 | 11.3% | 13.3 | -33.2% | |

### 2b. Consolidated P&L Statement — page 10, lines 332-366 (same period columns)
| # | Line item | Line # | Q1FY27 | Q1FY26 | YoY% | Q4FY26 | QoQ% | Flags |
|---|-----------|--------|--------|--------|------|--------|------|-------|
| 1 | Net Revenue From Operations | 334 | 98.9 | 87.6 | 12.8% | 110.4 | -10.5% | |
| 2 | Cost of Goods Sold | 336 | 82.3 | 61.8 | — | 76.7 | — | |
| 3 | Gross Profit | 338 | 16.5 | 25.9 | -36.2% | 33.7 | -51.0% | |
| 4 | Gross Profit Margin (%) | 340 | 16.7% | 29.5% | -1282 bps | 30.5% | -1384 bps | |
| 5 | Employee Expenses | 342 | 7.1 | 4.1 | — | 6.2 | — | |
| 6 | Other Expenses | 344 | 6.1 | 7.0 | — | 11.9 | — | |
| 7 | EBITDA | 346 | 3.3 | 14.9 | -77.7% | 15.7 | -79.0% | |
| 8 | EBITDA Margin (%) | 348 | 3.3% | 17.0% | -1361 bps | 14.2% | -1089 bps | note: standalone margin narrative on page 7 cites Q1FY26 EBITDA margin as 16.9%, this table cites 17.0% — sub-1pt rounding discrepancy, flag for A3/A4 arithmetic check |
| 9 | Other Income | 350 | 0.2 | 1.3 | — | 0.3 | — | |
| 10 | Finance Cost | 352 | 2.9 | 3.5 | — | 3.0 | — | |
| 11 | Depreciation | 354 | 9.1 | 1.8 | — | 9.0 | — | |
| 12 | PBT Before Exceptional Items | 356 | -8.5 | 10.8 | -179.2% | 4.0 | -312.0% | |
| 13 | Tax Expense | 358 | -0.7 | 2.8 | — | 3.0 | — | |
| 14 | PAT | 360 | -7.9 | 8.0 | -198.6% | 1.0 | -877.3% | negative PAT |
| 15 | PAT Margin (%) | 362 | -8.0% | 9.1% | -1708 bps | 0.9% | -888 bps | |
| 16 | EPS (Rs) | 364 | -1.6 | 1.7 | — | 0.2 | — | |
| 17 | Cash PAT | 366 | 1.3 | 9.8 | -87.2% | 10.0 | -87.5% | |

### 2c. Consolidated P&L Statement (Annual) — page 27, lines 922-941 (FY23/FY24/FY25/FY26)
| # | Line item | Line # | FY23 | FY24 | FY25 | FY26 |
|---|-----------|--------|------|------|------|------|
| 1 | Net Revenue From Operations | 922 | 424.8 | 452.5 | 504.0 | 366.5 |
| 2 | Cost of Goods Sold | 924 | 317.4 | 341.2 | 378.7 | 276.1 |
| 3 | Gross Profit | 925 | 107.4 | 111.3 | 125.2 | 90.3 |
| 4 | Gross Profit Margin (%) | 926 | 25.3% | 24.6% | 24.8% | 24.6% |
| 5 | Employee Expenses | 927 | 10.8 | 11.1 | 12.8 | 16.4 |
| 6 | Other Expenses | 928 | 30.4 | 21.8 | 23.9 | 33.2 |
| 7 | EBITDA | 929 | 66.2 | 78.4 | 88.5 | 40.8 |
| 8 | EBITDA Margin (%) | 930 | 15.6% | 17.3% | 17.6% | 11.1% |
| 9 | Other Income | 931 | 0.3 | 1.8 | 1.4 | 0.9 |
| 10 | Finance Cost | 932 | 5.6 | 6.3 | 8.1 | 12.7 |
| 11 | Depreciation | 933 | 4.8 | 6.3 | 7.3 | 22.6 |
| 12 | PBT Before Exceptional Items | 935 | 56.1 | 67.6 | 74.4 | 6.4 |
| 13 | Tax Expense | 937 | 11.4 | 17.5 | 21.0 | 4.9 |
| 14 | PAT | 938 | 44.7 | 50.1 | 53.4 | 1.4 |
| 15 | PAT Margin (%) | 939 | 10.5% | 11.1% | 10.6% | 0.4% |
| 16 | EPS (Rs) | 940 | 9.53 | 10.69 | 11.39 | 0.28 |
| 17 | Cash PAT | 941 | 49.4 | 56.4 | 60.7 | 24.0 |

FY26 EBITDA (40.8) and PAT (1.4) confirm the sharp margin compression already visible in
the Q1FY27 quarterly tables — cross-reference for A4.

### 2d. Consolidated Balance Sheet — page 28, lines 952-975 (Mar-23/24/25/26)
| # | Liability line item | Line # | Mar-23 | Mar-24 | Mar-25 | Mar-26 | Asset line item (same row) | Mar-23 | Mar-24 | Mar-25 | Mar-26 |
|---|----------------------|--------|--------|--------|--------|--------|------------------------------|--------|--------|--------|--------|
| 1 | Share Capital | 952 | 1.8 | 9.4 | 9.4 | 10.4 | Property, Plant & Equipment and Intangible Assets | 26.4 | 40.3 | 43.4 | 243.1 |
| 2 | Reserves & Surplus | 955 | 177.7 | 221.2 | 274.6 | 439.5 | Capital Works-in-progress | 10.9 | 30.4 | 125.5 | 6.1 |
| 3 | Shareholders' Funds | 957 | 179.5 | 230.5 | 284.0 | 449.9 | Right To Use Assets | 9.4 | 9.3 | 11.0 | 10.4 |
| 4 | Long Term Borrowings | 959 | 0.3 | 24.0 | 68.7 | 21.7 | Other Non-current Assets | 4.7 | 8.1 | 12.4 | 18.2 |
| 5 | Other Non-Current Liabilities | 961 | 0.5 | 0.3 | 2.1 | 1.8 | Total Non-current Assets | 51.4 | 88.1 | 192.3 | 277.7 |
| 6 | Total Non-Current Liabilities | 963 | 0.8 | 24.3 | 70.7 | 23.5 | Inventories | 142.5 | 174.5 | 166.1 | 233.7 |
| 7 | Short Term Borrowings | 965 | 89.1 | 87.1 | 155.6 | 128.1 | Trade Receivables | 79.6 | 45.3 | 141.0 | 76.7 |
| 8 | Trades Payable | 967 | 21.1 | 18.9 | 16.7 | 19.2 | Cash And Cash Equivalents | 10.6 | 16.4 | 4.1 | 15.9 |
| 9 | Other Financial Liabilities | 969 | 3.7 | 1.2 | 8.0 | 19.3 | Other Financial Assets | 0.5 | 13.9 | 0.2 | 0.3 |
| 10 | Other Current Liabilities | 971 | 1.5 | 6.5 | 1.4 | 1.9 | Other Current Assets | 11.2 | 30.4 | 32.8 | 37.5 |
| 11 | Total Current Liabilities | 973 | 115.5 | 113.7 | 181.7 | 168.5 | Total Current Assets | 244.4 | 280.5 | 344.1 | 364.1 |
| 12 | Total Equity and Liabilities | 975 | 295.8 | 368.6 | 536.4 | 641.9 | Total Assets | 295.8 | 368.6 | 536.4 | 641.9 |

24 line items (12 liability + 12 asset). Note: PP&E jump from Rs 43.4 Cr (Mar-25) to Rs
243.1 Cr (Mar-26) is the Dahej capitalisation referenced narratively on pages 7/8/22 —
cross-check for A4 (~Rs 265 Cr capitalised implies ~Rs 200 Cr of the jump is Dahej-specific
net of other additions/depreciation).

### 2e. Consolidated Cash Flow Statement — page 29, lines 986-1012 (FY23/FY24/FY25/FY26)
| # | Line item | Line # | FY23 | FY24 | FY25 | FY26 |
|---|-----------|--------|------|------|------|------|
| 1 | Net Profit Before Tax and Extraordinary Items | 986 | 56.1 | 67.6 | 74.4 | 6.4 |
| 2 | Adjustments for: Non-Cash Items / Other Investment or Financial Items | 988-990 | 15.8 | 10.4 | 15.4 | 40.1 |
| 3 | Operating Profit Before Working Capital Changes | 992 | 71.9 | 78.0 | 89.8 | 46.4 |
| 4 | Changes in Working Capital | 994 | -39.1 | -22.2 | -89.5 | -5.5 |
| 5 | Cash Generated From Operations | 996 | 32.8 | 55.9 | 0.3 | 40.9 |
| 6 | Direct Taxes Paid (Net of Refund) | 998 | -17.5 | -15.7 | -25.2 | -11.3 |
| 7 | Net Cash From Operating Activities | 1000 | 15.3 | 40.1 | -24.9 | 29.6 |
| 8 | Net Cash From Investing Activities | 1002 | -14.4 | -51.1 | -92.5 | -101.5 |
| 9 | Net Cash From Financing Activities | 1004 | 6.4 | 15.4 | 104.5 | 77.6 |
| 10 | Net Decrease/Increase in Cash and Cash Equivalents | 1006 | 7.4 | 4.4 | -12.9 | 5.7 |
| 11 | Add: Cash & Cash Equivalents at the Beginning of the Period | 1008 | 6.5 | 10.6 | 15.9 | 3.0 |
| 12 | Effect of exchange rate changes | 1010 | -3.3 | 0.9 | 0.1 | -0.6 |
| 13 | Cash & Cash Equivalents at the End of the Period | 1012 | 10.6 | 15.9 | 3.0 | 8.1 |

FY25 Net Cash From Operating Activities of -24.9 Cr against Cash Generated From Operations
of only 0.3 Cr (working capital drag of -89.5 Cr) is a notable historical data point for A3/A4.

**Table line-item reconciliation:** grep-anchored P&L label count = 51 (17 × 3 tables) +
manually verified balance sheet 24 + manually verified cash flow 13 = **88 total**. Manual
sweep of Sections 2a-2e above = **88. Match: yes.**

---

## 3. SLIDE-LEVEL NUMBERS & KPIs OUTSIDE THE FIVE MAIN FINANCIAL TABLES (95 items)

| # | Page | Line # | Figure | Flags |
|---|------|--------|--------|-------|
| 1 | 7 | 220 | Standalone Revenue Rs 83.0 Cr | |
| 2 | 7 | 221 | Standalone Revenue YoY 9% | |
| 3 | 7 | 213 | Standalone Gross Margin 17.7% | |
| 4 | 7 | 219 | Standalone Gross Margin Q1FY26 comparator 25.0% | |
| 5 | 7 | 221 | Standalone EBITDA Margin 10.3% | |
| 6 | 7 | 223 | Standalone EBITDA Margin Q1FY26 comparator 13.8% | |
| 7 | 7 | 220 | Standalone PAT Rs 7.3 Cr | |
| 8 | 7 | 221 | Standalone PAT YoY 11% | |
| 9 | 7 | 220 | Standalone Cash PAT Rs 8.9 Cr | |
| 10 | 7 | 221 | Standalone Cash PAT YoY 11% | |
| 11 | 7 | 235 | Consolidated Revenue Rs 98.9 Cr | |
| 12 | 7 | 236 | Consolidated Revenue YoY 13% | |
| 13 | 7 | 228 | Consolidated Gross Margin 16.7% | |
| 14 | 7 | 234 | Consolidated Gross Margin Q1FY26 comparator 29.5% | |
| 15 | 7 | 236 | Consolidated EBITDA Margin 3.3% | |
| 16 | 7 | 238 | Consolidated EBITDA Margin Q1FY26 comparator 16.9% | note: page-10 table says 17.0% for the same comparator — 0.1pt rounding gap, flag for A3 |
| 17 | 7 | 235 | Consolidated PAT Rs (7.9) Cr | negative |
| 18 | 7 | 236 | Consolidated PAT YoY -199% | steep decline |
| 19 | 7 | 235 | Consolidated Cash PAT Rs 1.3 Cr | |
| 20 | 7 | 236 | Consolidated Cash PAT YoY -87% | steep decline |
| 21 | 7 | 243 | Higher non-cash depreciation Rs 9.1 Cr | |
| 22 | 7 | 243 | Dahej capex capitalised ~Rs 265 Cr | |
| 23 | 7 | 243 | Total planned Dahej capex ~Rs 270 Cr | |
| 24 | 8 | 267 | Depreciation Rs 9.1 Cr (repeat) | `REPEAT_DISCLOSURE` of #21 |
| 25 | 8 | 267-268 | Dahej capex ~Rs 265 Cr (repeat) | `REPEAT_DISCLOSURE` of #22 |
| 26 | 12 | 387-388 | Rs 1,648 Mn FY18 revenue | |
| 27 | 12 | 389 | >100% YoY revenue growth (FY18) | |
| 28 | 12 | 397 | $202,608 first Material Subsidiary sale (2020) | |
| 29 | 12 | 396 | Rs 4,248 Mn FY23 consolidated revenue | |
| 30 | 12 | 396 | Listing date 26th Aug'25 | |
| 31 | 12 | 396-398 | Commercial production of GEM Cool 5/Safranal at Dahej, 26th Feb'26 | |
| 32 | 12 | 407-408 | Brazil subsidiary incorporation approved June 2026 | |
| 33 | 13 | 432-433 | 3 Decades of Experience | |
| 34 | 13 | 432,434 | 80+ Products Across Categories | |
| 35 | 13 | 432,435 | 3 Manufacturing Facilities | |
| 36 | 13 | 432,436 | 13 Scientists Leading R&D | |
| 37 | 13 | 439-440 | 20 Countries Served Globally | |
| 38 | 13 | 439-440 | 240 Domestic Customers | |
| 39 | 13 | 439-441 | 44 Global Customers | |
| 40 | 14 | 467 | Mint Global Market Size ~USD 1.8-2.0 Bn | |
| 41 | 14 | 467 | Mint India Market Size ~USD 900 Mn | |
| 42 | 14 | 467 | Mint India Production Size ~USD 1.2 Bn | |
| 43 | 14 | 467,469 | Mint India Positioning ~53-55% share of global supply | |
| 44 | 14 | 474 | Mint FY26 Segment Revenue Rs 237 Cr | |
| 45 | 14 | 475 | Mint ~65% of Total Revenue | |
| 46 | 15 | 500 | Clove Global Market Size ~USD 217 Mn | |
| 47 | 15 | 500 | Clove India Market Size ~USD 34 Mn | |
| 48 | 15 | 500 | Clove India Production Size ~USD 29 Mn | |
| 49 | 15 | 499,501 | Clove India Positioning ~13% share of global supply | |
| 50 | 15 | 508 | Clove FY26 Segment Revenue Rs 85 Cr | |
| 51 | 15 | 509 | Clove ~23% of Total Revenue | |
| 52 | 16 | 534 | Phenol Global Market Size ~USD 880 Mn | |
| 53 | 16 | 534 | Phenol India Market Size ~USD 210 Mn | |
| 54 | 16 | 534 | Phenol India Production Size ~USD 200 Mn | |
| 55 | 16 | 533,535 | Phenol India Positioning ~20-25% share of global supply | |
| 56 | 16 | 542 | Phenol FY26 Segment Revenue Rs 5 Cr | smallest disclosed segment |
| 57 | 16 | 543 | Phenol ~1% of Total Revenue | |
| 58 | 17 | 554-555 | Eucalyptus Oil ~58% India market share (FY25) | |
| 59 | 17 | 572 | Citral/Other FY26 Segment Revenue Rs 36 Cr | |
| 60 | 17 | 573 | Citral/Other ~10% of Total Revenue | |
| 61 | 19 | 639-640 | Yash Parekh associated since April 2011 | |
| 62 | 19 | 640-642 | Company grew "from Rs 15 Cr to Rs 500 Cr and beyond" under his tenure | unanchored baseline period not stated |
| 63 | 19 | 653 | Export Excellence Award years: 2021-2022, 2018-19, 2017-18 | |
| 64 | 20 | 675 | Shrenik Vora 25+ years experience | |
| 65 | 20 | 680-681 | Dinesh T V 25+ years experience | |
| 66 | 20 | 680 | Vishakha Bhagvat 30+ years experience | |
| 67 | 20 | 677 | Dr. Shubhangi Umbarkar at NCL Pune since 2002 | |
| 68 | 21 | 709 | Silvassa Facility established 1997 | |
| 69 | 21 | 709 | Budaun Facility established 2016 | |
| 70 | 21 | 709 | Dahej Facility established 2024 | |
| 71 | 21 | 730 | Certification ISO 9001:2015 | |
| 72 | 21 | 730 | Certification ISO 14001:2015 | |
| 73 | 21 | 730 | Certification ISO 45001:2018 | |
| 74 | 21 | 730 | Certification FSSC 22000:2018 | |
| 75 | 21 | 730 | Certification Ts 22002-1:2009 | |
| 76 | 22 | 757 | ~Rs 270 Cr Investment via Internal Accruals & Debt | `REPEAT_DISCLOSURE` of #23 (total planned Dahej capex) |
| 77 | 22 | 760 | 15% Corporate Tax Rate under Government Incentives till perpetuity | |
| 78 | 23 | 778 | 240 domestic customers (repeat) | `REPEAT_DISCLOSURE` of #38 |
| 79 | 23 | 779 | 44 international customers (repeat) | `REPEAT_DISCLOSURE` of #39 |
| 80 | 23 | 781 | 20 countries served (repeat) | `REPEAT_DISCLOSURE` of #37 |
| 81 | 23 | 820 | Geography split FY26 — India 56% | chart data label |
| 82 | 23 | 820 | Geography split FY26 — USA 28% | chart data label |
| 83 | 23 | 820 | Geography split FY26 — Rest of World 7% | chart data label |
| 84 | 23 | 820 | Geography split FY26 — Brazil 6% | chart data label |
| 85 | 23 | 820 | Geography split FY26 — China 3% | chart data label |
| 86 | 25 | 895 | 13 Qualified Scientists (repeat) | `REPEAT_DISCLOSURE` of #36 |
| 87 | 32 | 1051 | BSE/NSE Code 544491/GEMAROMA | |
| 88 | 32 | 1056 | CMP Rs 174.90 (as on 13th Aug 2026) | |
| 89 | 32 | 1060 | Market Cap Rs 914.15 Cr | |
| 90 | 32 | 1064 | Shares outstanding 5.2 Cr | |
| 91 | 32 | 1067 | Face Value Rs 2.00 | |
| 92 | 32 | 1075 | Shareholding — Promoters 57.4% (as on 30th June 2026) | chart data label |
| 93 | 32 | 1075 | Shareholding — Public 37.0% | chart data label |
| 94 | 32 | 1075 | Shareholding — DII's 4.8% | chart data label |
| 95 | 32 | 1075 | Shareholding — FII's 0.8% | chart data label |

**Reconciliation:** two independent manual sweeps of the deck (pass 1 and pass 2, tallied
per page then summed) both total **95. Match: yes.**

---

## 4. CHARTS — FULL DATA-LABEL INVENTORY (3 charts)

| # | Page | Line # | Chart description | Data labels enumerated |
|---|------|--------|--------------------|--------------------------|
| 1 | 7 | 250 | Dashboard tiles with directional arrow icons (green up-triangle = increase, red down-triangle = decrease) beside each YoY% figure | Standalone: Revenue 9% YoY (up-green); Gross+EBITDA Margin block (no arrow, narrative decline note only); PAT 11% YoY (up-green); Cash PAT 11% YoY (up-green). Consolidated: Revenue 13% YoY (up-green); PAT 199% YoY (down-red — decline framed as red despite the underlying number being a magnitude, i.e., PAT fell 199% YoY into negative territory); Cash PAT 87% YoY (down-red). No numeric values beyond what appears in the KPI text (Section 3, items 1-20). |
| 2 | 23 | 820 | Donut/pie chart, "Revenue split by Geography (FY26)", overlaid on a world map with customer-country markers (USA, UK, Germany, Bulgaria, Ireland, Netherlands, France, Turkey, Israel, Spain, China, Hong Kong, Vietnam, Thailand, Nepal, Indonesia, Singapore, Australia, Brazil, India) | India 56% (largest wedge), USA 28%, Rest of World 7%, Brazil 6%, China 3%. Legend order top-to-bottom: India, USA, Brazil, China, Rest of World. Sums to 100%. |
| 3 | 32 | 1075 | Pie chart, "Shareholding Pattern (as on 30th June 2026)" (deck's own internal footer numbers this slide "31") | Promoters 57.4%, Public 37.0%, DII's 4.8%, FII's 0.8%. Sums to 100.0%. |

**Reconciliation:** grep `^\[CHART` = 3; manual sweep of the deck's visual/chart elements = 3
(page 7 dashboard-tile chart, page 23 geography donut, page 32 shareholding pie). No
additional un-flagged charts found on manual re-read (world map on page 23 is embedded in
the same chart unit, not a separate chart; page 12 timeline and page 18 product-mapping
grid are structured graphics but carry no data-label chart, correctly excluded). **Match: yes.**

---

## 5. GUIDANCE / FORWARD-LOOKING STATEMENTS (11 items)

| # | Page | Line # | Statement | Flags |
|---|------|--------|-----------|-------|
| 1 | 6 | 192-193 | "the proposed Brazil subsidiary expected to enhance our distribution reach in Latin America" | forward-commitment |
| 2 | 6 | 195-197 | "our focus now on progressively scaling Krystal Ingredients' Dahej facility, strengthening our product capabilities and expanding our presence across global markets" | forward-commitment, hedge-adjacent (no dates) |
| 3 | 8 | 263 | "as capacity utilization improves and the contribution from higher-value products increases, we expect margins to gradually improve" | hedge phrase ("gradually"), no quantified target or date |
| 4 | 8 | 271-273 | Brazil WOS approved to distribute essential oils, aromatic chemicals and specialty chemicals, strengthening presence across Brazil/Latin America | forward-commitment |
| 5 | 8 | 277 | Cooling Agents (GEM Cool 03/05/23): customer audits completed, initial orders secured; revenue contribution expected from Q3FY27 | dated guidance |
| 6 | 8 | 278 | Safranal: revenue contribution expected towards end of Q2FY27, more meaningfully from Q3FY27 | dated guidance |
| 7 | 8 | 279-280 | Phenol Derivatives: trial production expected end Q2FY27; commercial production targeted Q3FY27; revenue contribution expected from Q4FY27 | dated guidance, 3-stage cascade |
| 8 | 22 | 743-744 | Cooling Agents guidance repeated verbatim | `REPEAT_DISCLOSURE` of #5 |
| 9 | 22 | 746 | Safranal guidance repeated verbatim | `REPEAT_DISCLOSURE` of #6 |
| 10 | 22 | 748-750 | Phenol Derivatives guidance repeated verbatim | `REPEAT_DISCLOSURE` of #7 |
| 11 | 22 | 760 | "15% Corporate Tax Rate under Government Incentives till perpetuity" | forward-commitment, "till perpetuity" is an unusually strong/unqualified claim — flag for A3/A4 scrutiny (no sunset date, no citation of the specific incentive scheme) |

**Reconciliation:** two independent manual sweeps = 11 / 11. **Match: yes.**

---

## 6. CAPACITY / CAPEX / MARGIN / ORDER-BOOK NUMBERS (14 items, incl. 2 absence flags)

| # | Page | Line # | Item | Flags |
|---|------|--------|------|-------|
| 1 | 7 | 243 | Dahej capex capitalised ~Rs 265 Cr | |
| 2 | 7 | 243 | Total planned Dahej capex ~Rs 270 Cr | |
| 3 | 8 | 267-268 | Repeat of #1/#2 with same figures | `REPEAT_DISCLOSURE` |
| 4 | 22 | 757 | ~Rs 270 Cr Investment via Internal Accruals & Debt (funding-source detail added) | `REPEAT_DISCLOSURE` of #2, new detail: funding mix (internal accruals + debt, no split given) |
| 5 | 22 | 760 | 15% Corporate Tax Rate under Government Incentives till perpetuity | see Section 5 #11 |
| 6 | 7 | 213,219 | Margin — Standalone Gross Margin 17.7% vs 25.0% Q1FY26 | -730bps compression |
| 7 | 7 | 221,223 | Margin — Standalone EBITDA Margin 10.3% vs 13.8% Q1FY26 | -350bps compression |
| 8 | 7 | 228,234 | Margin — Consolidated Gross Margin 16.7% vs 29.5% Q1FY26 | -1282bps compression |
| 9 | 7 | 236,238 | Margin — Consolidated EBITDA Margin 3.3% vs 16.9%/17.0% Q1FY26 | -1361/1370bps compression, largest margin move in the deck |
| 10 | 27 | 926 | Margin — Annual Gross Profit Margin FY23-26: 25.3% / 24.6% / 24.8% / 24.6% | relatively stable historically |
| 11 | 27 | 930 | Margin — Annual EBITDA Margin FY23-26: 15.6% / 17.3% / 17.6% / 11.1% | FY26 already showed compression before Q1FY27 |
| 12 | 27 | 939 | Margin — Annual PAT Margin FY23-26: 10.5% / 11.1% / 10.6% / 0.4% | FY26 PAT margin collapse to near-zero, pre-dates this quarter |
| 13 | n/a | n/a | **Installed production capacity (tonnage/MT/TPA) for Silvassa, Budaun, or Dahej** | `DATA_ABSENT` — no capacity figure in any unit is disclosed anywhere in the 33-page deck for any facility; only qualitative "capacity utilization improves" language (page 8, line 262-263) |
| 14 | n/a | n/a | **Order book / backlog value** | `DATA_ABSENT` — no order-book Rs figure or unit count disclosed anywhere; management states "initial orders secured" for Cooling Agents (page 8, line 277) with no accompanying value |

**Reconciliation:** two independent manual sweeps = 14 / 14. **Match: yes.**

---

## 7. STRATEGIC CLAIMS (17 items)

| # | Page | Line # | Claim | Flags |
|---|------|--------|-------|-------|
| 1 | 6 | 179-182 | Revenue YoY growth narrative; focus shifting to "utilising and monetising the expanded manufacturing platform at Dahej" and scaling Krystal Ingredients | |
| 2 | 12 | 403-404 | Silvassa plant received EcoVadis Platinum sustainability rating (2025) | |
| 3 | 13 | 418-419 | "One of the leading Indian manufacturer of specialty ingredients..." | unquantified leadership claim |
| 4 | 13 | 421-424 | Broad product range across Mint/Clove/Phenol + expansion into Citral Chemistry and Phenol Derivatives | |
| 5 | 14 | 467,469 | Mint segment ~53-55% India positioning (% share of global supply) | sourced to Frost & Sullivan (2025) |
| 6 | 15 | 487 | "One of the largest processors of Clove Oil and Eugenol (by volume in India, FY25)" | unquantified leadership claim |
| 7 | 15 | 499,501 | Clove segment ~13% India positioning (% share of global supply) | sourced to Frost & Sullivan (2025) |
| 8 | 16 | 522 | Entry into "limited-competition, high-margin molecules" via Phenol Derivatives forward integration | |
| 9 | 16 | 533,535 | Phenol segment ~20-25% India positioning (% share of global supply) | widest range of any positioning claim in the deck |
| 10 | 17 | 554-555 | "Largest processor of Eucalyptus Oil in India with ~58% market share (FY25)" | sourced to Frost & Sullivan (2025) |
| 11 | 21 | 702-724 | Strategic-location claims: Dahej (Phenol access, Expressway/Ports connectivity), Silvassa (JN Port proximity), Budaun (mint cultivation belt) | |
| 12 | 22 | 755 | "Focus on High Value Specialty Molecules enables Superior Margins and Stronger Market Positioning" | forward-looking, unquantified |
| 13 | 22 | 761-762 | Backward and Forward Integration claimed to provide "robust control over process, product quality" and customisation avenues | |
| 14 | 22 | 763 | "Installed manufacturing capabilities can be deployed across varied models like CRO, CMO and CDMO" | business-model optionality claim, no contracts/revenue cited |
| 15 | 22 | 765-766 | Strategic location near Phenol supply, Mumbai-Delhi Expressway, and JN Port cited for "reduced logistics cost and faster exports" | |
| 16 | 24 | 838-862 | Process-technology capability claims: DCS/process automation, Fixed-Bed Reaction Technology, High-Pressure Reaction Technology, Continuous Reaction Technology, High-Vacuum Distillation, plus named complex-chemistry capabilities (Grignard, Amide Coupling, Friedel-Crafts, Cross-Coupling, Photochemical, Green Methoxylation) | |
| 17 | 25 | 889-898 | R&D achievement claims: Citral chemistry led to Safranal/Damascone launch; effluent-free vapor-phase process for Anisole/Synthetic Anethole; cooling agents developed from menthol; Anisole converted to MEHQ/Guaiacol/4-MAP in-house | |

**Reconciliation:** two independent manual sweeps = 17 / 17. **Match: yes.**

---

## 8. FOOTNOTES, SOURCE NOTES & FINE PRINT (13 items — 12 grep-anchored + 1 full-page disclaimer)

| # | Page | Line # | Footnote text (qualifying number/claim) |
|---|------|--------|-------------------------------------------|
| 1 | 3 | 96-116 | Full-page Disclaimer: no offer/recommendation, no representation/warranty on accuracy/completeness, forward-looking-statement risk language, no obligation to update, third-party statements not adopted. Qualifies every figure in the entire deck. (Not grep-anchored by the "Rounded off/Source/Note/*" pattern — counted separately, cited under Slide Index #3.) |
| 2 | 7 | 247 | "Rounded off to nearest decimal" | qualifies page-7 dashboard |
| 3 | 9 | 326 | "Rounded off to nearest decimal" | qualifies Standalone Q1 P&L |
| 4 | 10 | 369 | "Rounded off to nearest decimal" | qualifies Consolidated Q1 P&L |
| 5 | 14 | 480 | "Source: Frost & Sullivan Market Study (2025) including Peppermint Oil, Menthol & DMO in Industry Landscape" | qualifies Mint market-sizing figures |
| 6 | 15 | 514 | "Source: Frost & Sullivan Market Study (2025) including Clove Oil, Eugenol in Industry Landscape" | qualifies Clove market-sizing figures |
| 7 | 16 | 548 | "Source: Frost & Sullivan Market Study (2025) including Anethole, MEHQ, Guaiacol, BHA, 4-MAP in Industry Landscape" | qualifies Phenol market-sizing figures |
| 8 | 17 | 583 | "*Frost & Sullivan Market Study (2025)" | qualifies Eucalyptus Oil ~58% market-share claim |
| 9 | 21 | 735 | "*Including Eucalyptus Oil, Lemongrass Oil, Basil Oil, Turmeric/Ginger Oil" | qualifies "Other Synthetic and Natural Ingredients*" product-manufactured labels |
| 10 | 23 | 816-817 | "Note: Rest of the world includes Singapore, Australia, France, Indonesia, Ireland, Nepal, Netherlands, Thailand, Spain, Germany, Uganda, United Kingdom, Hong Kong..., Bulgaria, Israel, Vietnam, Turkey and Switzerland" | qualifies the 7% "Rest of World" geography-chart wedge — note Uganda and Switzerland appear in this footnote list but are NOT shown as markers on the page-23 world map, a minor internal inconsistency worth flagging for A3 |
| 11 | 27 | 944 | "Rounded off to nearest decimal" | qualifies Annual Consolidated P&L |
| 12 | 28 | 978 | "Rounded off to nearest decimal" | qualifies Consolidated Balance Sheet |
| 13 | 29 | 1015 | "Rounded off to nearest decimal" | qualifies Consolidated Cash Flow Statement |

**Reconciliation (grep-anchored subset, items 2-13):** grep
`Rounded off to nearest decimal|^Source:|^Note:|^\*` = 12; manual sweep of the same
prefix-matchable items = 12. **Match: yes.** Item 1 (full-page Disclaimer) is counted
separately since it is not prefix-matchable by the mechanical pattern; it is already
captured in Section 1 (Slide Index, slide 3) and is listed here for completeness, bringing
the total footnote/fine-print inventory to 13.

---

## 9. OCR'D PAGES (7 of 33 — flagged per task instruction)

Pages 2, 4, 5, 11, 26, 30, 31 were rasterised at 200dpi and OCR'd (native pdftotext yielded
below the 100-character threshold on each). All seven are section-divider/title/photo
slides (Title, Table of Contents, "Q1FY27 Highlights" divider, "Company Overview" divider,
"Annual Financials" divider, "Annexure" divider, "Dahej Plant Pictures" photo page) — manual
review confirms **none carry numeric KPI content**; OCR output on all seven matches or is a
degraded superset of the native text with no additional numbers introduced. No data-integrity
risk from the OCR pass on this run.

---

## 10. PRIOR-QUARTER DIFF (DROPPED_SLIDE CHECK)

Not applicable — no prior-quarter ledger provided (first-time coverage of GEMAROMA in this
pipeline). This ledger is the baseline; Q2FY27's A2 enumerator should diff against this file
for `DROPPED_SLIDE` and any newly silent disclosure (e.g., if the Krystal Ingredients
Q3FY27/Q4FY27 revenue-contribution guidance items in Section 5 are not repeated or updated
next quarter, that omission should be flagged against this baseline).

---

## SUMMARY OF FLAGS RAISED

- `REPEAT_DISCLOSURE` — 9 instances: Dahej capex figures (Section 3 #24-25, Section 6 #3-4),
  Krystal Ingredients guidance block (Section 5 #8-10), customer/country stats (Section 3
  #78-80), scientist count (Section 3 #86). Repetition across slides is not itself adverse
  (decks routinely restate headline KPIs) but is flagged so A3/A4 do not double-count these
  as independent evidence points.
- `DATA_ABSENT` — 2 instances: no installed-capacity tonnage disclosed for any facility
  (Section 6 #13); no order-book/backlog value disclosed anywhere in the deck (Section 6
  #14). Both are silences worth testing against the concall/notes doctypes when reconciled.
- `ZERO_STANDING` — 0 instances. All 88 financial-table line items carry real (including
  negative) values in every period shown; no nil/dash template rows found in any of the 5
  tables.
- Internal-consistency notes (not formal flags, carried for A3/A4): (a) Consolidated Q1FY26
  EBITDA margin comparator cited as 16.9% on page 7 narrative vs 17.0% on the page-10 table
  (Section 3 #16); (b) Rest-of-World footnote (page 23) lists Uganda and Switzerland, which
  do not appear as markers on the same page's world map (Section 8 #10).
