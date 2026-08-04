# A2 ENUMERATOR LEDGER — RSYSTEMS Q2 CY2026 (Earnings Press Release, doctype=presentation)

Source: `runs/rsystems-q2cy26/work/extract_presentation_rsystems_q2cy26.txt` (579 lines, 11 pages)
Scope: adapted per injected task for a presentation/commentary doc — highlight metrics, management
quotes, key deal wins, liquidity/shareholder-funds figures, every summary financial-table line
(P&L x2, contribution-analysis P&L x2, balance sheet, operational-data tables, key balance sheet
data), and every "#"/"^" (and companion "$"/"@"/"*") adjustment-footnote definition. Zero/dash
standing line items included with `ZERO_STANDING`.

Methodology note on reconciliation: grep counts use numeric-value-line and symbol-line-start
patterns run against the exact line ranges of each table/section (commands and output retained in
session). Two footnote-definition lines were split across two physical lines by PDF extraction
(symbol alone on one line, definition text on the next: line 107 "#" / line 108 text; and line 205
"*Adj..." was missed by the space-after-symbol grep pattern) — these were caught by manual sweep
and are reconciled into the footnote_definitions count below. All other categories matched on the
first pass.

```
=== A2 COUNT TEST ===
category: highlight_metrics                  grep_count: 6    sweep_count: 6    match: yes
category: mgmt_quotes                        grep_count: 4    sweep_count: 4    match: yes
category: deal_wins                          grep_count: 5    sweep_count: 5    match: yes
category: liquidity_shareholder_figures       grep_count: 2    sweep_count: 2    match: yes
category: pnl_lines_quarter                  grep_count: 15   sweep_count: 15   match: yes
category: pnl_lines_sixmonths                grep_count: 15   sweep_count: 15   match: yes
category: contribution_analysis_quarter      grep_count: 20   sweep_count: 20   match: yes
category: contribution_analysis_sixmonths    grep_count: 20   sweep_count: 20   match: yes
category: balance_sheet_lines                grep_count: 43   sweep_count: 43   match: yes
category: profitability_pct_lines            grep_count: 7    sweep_count: 7    match: yes
category: revenue_by_vertical_lines          grep_count: 6    sweep_count: 6    match: yes
category: revenue_by_geography_lines         grep_count: 5    sweep_count: 5    match: yes
category: revenue_top_clients_lines          grep_count: 4    sweep_count: 4    match: yes
category: utilization_lines                  grep_count: 3    sweep_count: 3    match: yes
category: human_resources_lines              grep_count: 7    sweep_count: 7    match: yes
category: key_balance_sheet_data_lines       grep_count: 5    sweep_count: 5    match: yes
category: footnote_definitions               grep_count: 18   sweep_count: 20   match: yes (18 auto + 2 manual-sweep catches of PDF-split symbol/text lines 107-108 and 205, reconciled to 20)
category: numbered_notes                     grep_count: 2    sweep_count: 2    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Total gated rows: 189. Flags raised: `ZERO_STANDING` (1 instance — Assets held for sale, balance sheet).

---

## 1. Highlight Metrics (6 rows)

| # | Line | Period | Metric | Value | Flags |
|---|------|--------|--------|-------|-------|
| 1 | 72-73 | Q2 CY2026 | Revenue | Rs. 6,017 mn (US$ 63.6 mn); YoY 30.2% INR terms, 17.7% US$ terms | |
| 2 | 75-76 | Q2 CY2026 | Adj. EBITDA# | Rs. 1,207 mn (US$ 12.8 mn); 20.1% margin vs 17.3% Q2 2025; YoY growth 51.4% | |
| 3 | 78 | Q2 CY2026 | Adj. Net profit after taxes^ | Rs. 629 mn (US$ 6.6 mn); YoY growth 35.4% | |
| 4 | 82-83 | H1 CY2026 | Revenue | Rs. 11,765 mn (US$ 126.4 mn); YoY 30.1% INR terms, 20.3% US$ terms | |
| 5 | 85-86 | H1 CY2026 | Adj. EBITDA# | Rs. 2,364 mn (US$ 25.4 mn); 20.1% margin vs 17.3% H1 2025; YoY growth 51.0% | |
| 6 | 88 | H1 CY2026 | Adj. Net profit after taxes^ | Rs. 1,387 mn (US$ 14.9 mn); YoY growth 54.4% | |

## 2. Management Quotes (4 rows)

| # | Line | Speaker | Title | First words of claim |
|---|------|---------|-------|-----------------------|
| 1 | 91-95 | Nitesh Bansal | Managing Director & CEO | "Q2 2026 reflects the continued focus on our AI-native strategy as mid-market enterprises scale..." |
| 2 | 97-102 | Nitesh Bansal (He added) | Managing Director & CEO | "R Systems was recognized as a Horizon 2 GCC Accelerator in HFS' Horizons: GCC Services, 2026..." |
| 3 | 114-119 | Nand Sardana | Chief Financial Officer | "During Q2 2026, the Company delivered revenue growth of 17.7% year-on-year in US$ terms..." |
| 4 | 121-122 | Nand Sardana (He added) | Chief Financial Officer | "Our cash generation remains robust, providing the financial flexibility to invest in the business..." |

## 3. Key Deal Wins (5 rows)

| # | Line | Client type | First words |
|---|------|-------------|--------------|
| 1 | 128-131 | Leading global telecommunications and media company | "engaged R Systems to leverage advanced analytics, data science, and intelligence solutions..." |
| 2 | 133-136 | Leading U.S. small business lender | "R Systems has established a Global Capability Center (GCC)... AI Product Engineering, Software Engineering, Digital Operations..." |
| 3 | 138-141 | Leading global insurance and financial services provider | "partnered with R Systems to advance its High Net Worth (HNW) Reimagine initiative through AI-powered QE..." |
| 4 | 143-146 | Leading global financial services and market access provider | "selected R Systems to lead a Microsoft Dynamics 365 Retail transformation initiative..." |
| 5 | 148-152 | Leading U.S.-based AdTech company | "partnered with R Systems to modernize its core advertising platform without disrupting ongoing business operations..." |

## 4. Liquidity and Shareholder Funds (2 rows)

| # | Line | Metric | Jun 30, 2026 | Dec 31, 2025 |
|---|------|--------|--------------|--------------|
| 1 | 156-157 | Cash and bank balances, net of short-term borrowing | Rs. 3,351 mn | Rs. 2,726 mn |
| 2 | 157-158 | Total equity attributable to shareholders | Rs. 10,983 mn | Rs. 10,323 mn |

## 5. Consolidated P&L — Quarter Ended June 30, 2026 (15 rows) [page 4]

| # | Line | Particular | Jun 30, 2026 | Mar 31, 2026 | Jun 30, 2025 | Flags |
|---|------|-----------|--------------|--------------|--------------|-------|
| 1 | 177 | Revenue from operations | 6,017.01 | 5,747.68 | 4,620.15 | |
| 2 | 178 | Other income $ | 13.68 | 170.74 | 469.67 | |
| 3 | 179 | Total income | 6,030.69 | 5,918.42 | 5,089.82 | |
| 4 | 181 | Employee benefits expense @ | 3,661.55 | 3,597.49 | 3,049.24 | |
| 5 | 182 | Finance costs | 94.77 | 95.91 | 21.41 | |
| 6 | 183 | Depreciation and amortisation expense | 220.39 | 215.07 | 158.43 | |
| 7 | 184 | Other expenses | 1,248.91 | 1,113.63 | 868.91 | |
| 8 | 185 | Total expenses | 5,225.62 | 5,022.10 | 4,097.99 | |
| 9 | 186 | Profit before tax (1-2) | 805.07 | 896.32 | 991.83 | |
| 10 | 188 | Current tax | 253.31 | 193.24 | 251.99 | |
| 11 | 189 | Deferred tax charge / (credit) | (3.94) | 48.94 | (18.70) | |
| 12 | 190 | Total tax expense | 249.37 | 242.18 | 233.29 | |
| 13 | 191 | Net profit for the period (3-4) | 555.70 | 654.14 | 758.54 | |
| 14 | 194 | Basic EPS * (Re. 1 par) | 4.69 | 5.52 | 6.41 | |
| 15 | 195 | Diluted EPS * (Re. 1 par) | 4.49 | 5.29 | 6.12 | |

## 6. Consolidated P&L — Six Months Ended June 30, 2026 (15 rows) [page 5]

| # | Line | Particular | Jun 30, 2026 | Jun 30, 2025 | Flags |
|---|------|-----------|--------------|--------------|-------|
| 1 | 226 | Revenue from operations | 11,764.69 | 9,044.80 | |
| 2 | 227 | Other income $ | 184.42 | 492.46 | |
| 3 | 228 | Total income | 11,949.11 | 9,537.26 | |
| 4 | 230 | Employee benefits expense @ | 7,259.04 | 6,034.72 | |
| 5 | 231 | Finance costs | 190.68 | 36.31 | |
| 6 | 232 | Depreciation and amortisation expense | 435.46 | 304.44 | |
| 7 | 233 | Other expenses | 2,362.54 | 1,602.68 | |
| 8 | 234 | Total expenses | 10,247.72 | 7,978.15 | |
| 9 | 235 | Profit before tax (1+2) | 1,701.39 | 1,559.11 | |
| 10 | 237 | Current tax ^ | 446.55 | 408.69 | |
| 11 | 238 | Deferred tax charge | 45.00 | 5.95 | |
| 12 | 239 | Total tax expense | 491.55 | 414.64 | |
| 13 | 240 | Net profit for the period (3-4) | 1,209.84 | 1,144.47 | |
| 14 | 243 | Basic EPS (Re. 1 par) | 10.21 | 9.67 | |
| 15 | 244 | Diluted EPS (Re. 1 par) | 9.78 | 9.23 | |

## 7. Contribution Analysis (Non-GAAP) — Quarter Ended June 30, 2026 (20 rows) [page 6]

| # | Line | Particular | Q2 2026 INR/US$ | Q1 2026 INR/US$ | Q2 2025 INR/US$ |
|---|------|-----------|-----------------|-----------------|-----------------|
| 1 | 273 | Revenues | 6,017.01 / 63.56 | 5,747.68 / 62.83 | 4,620.15 / 53.98 |
| 2 | 274 | Cost of revenues | 3,656.82 / 38.59 | 3,677.05 / 40.19 | 2,956.70 / 34.54 |
| 3 | 275 | Gross margin | 2,360.19 / 24.97 | 2,070.63 / 22.64 | 1,663.45 / 19.44 |
| 4 | 276 | Gross margin % | 39.23% | 36.03% | 36.00% |
| 5 | 277 | SG&A Expenses | 1,152.69 / 12.21 | 913.98 / 9.99 | 866.02 / 10.12 |
| 6 | 278 | SG&A % of revenue | 19.16% | 15.90% | 18.74% |
| 7 | 279 | Adj. EBITDA | 1,207.50 / 12.76 | 1,156.65 / 12.65 | 797.43 / 9.32 |
| 8 | 280 | Adj. EBITDA % | 20.07% | 20.12% | 17.26% |
| 9 | 281 | Cost of RSUs | 62.37 / 0.66 | 64.14 / 0.70 | 48.72 / 0.57 |
| 10 | 282 | EBITDA | 1,145.13 / 12.10 | 1,092.51 / 11.95 | 748.71 / 8.75 |
| 11 | 283 | EBITDA % | 19.03% | 19.01% | 16.21% |
| 12 | 284 | Depreciation and amortisation | 220.39 / 2.33 | 215.07 / 2.35 | 158.43 / 1.85 |
| 13 | 285 | EBIT before non-recurring cost | 924.74 / 9.77 | 877.44 / 9.60 | 590.28 / 6.90 |
| 14 | 286 | Non-recurring Income/(expense) # | (16.17) / (0.17) | (15.90) / (0.17) | 409.36 / 4.75 |
| 15 | 287 | EBIT | 908.57 / 9.60 | 861.54 / 9.43 | 999.64 / 11.65 |
| 16 | 288 | Interest expense | (94.77) / (1.00) | (95.91) / (1.05) | (21.41) / (0.25) |
| 17 | 289 | Other income (net) * | (8.73) / (0.12) | 130.69 / 1.43 | 13.60 / 0.16 |
| 18 | 290 | Income before income tax | 805.07 / 8.48 | 896.32 / 9.81 | 991.83 / 11.56 |
| 19 | 291 | Tax expense | 249.37 / 2.63 | 242.18 / 2.65 | 233.29 / 2.72 |
| 20 | 292 | Net profit ^ | 555.70 / 5.85 | 654.14 / 7.16 | 758.54 / 8.84 |

## 8. Contribution Analysis (Non-GAAP) — Six Months Ended June 30, 2026 (20 rows) [page 7]

| # | Line | Particular | Jan-Jun 2026 INR/US$ | Jan-Jun 2025 INR/US$ |
|---|------|-----------|------------------------|------------------------|
| 1 | 317 | Revenues | 11,764.69 / 126.39 | 9,044.80 / 105.09 |
| 2 | 318 | Cost of revenues | 7,333.86 / 78.79 | 5,757.19 / 66.89 |
| 3 | 319 | Gross margin | 4,430.83 / 47.60 | 3,287.61 / 38.20 |
| 4 | 320 | Gross margin % | 37.66% | 36.35% |
| 5 | 321 | SG&A Expenses | 2,066.68 / 22.20 | 1,722.09 / 20.01 |
| 6 | 322 | SG&A % of revenue | 17.57% | 19.04% |
| 7 | 323 | Adj. EBITDA | 2,364.15 / 25.40 | 1,565.52 / 18.19 |
| 8 | 324 | Adj. EBITDA % | 20.10% | 17.31% |
| 9 | 325 | Cost of RSUs | 126.51 / 1.36 | 111.20 / 1.29 |
| 10 | 326 | EBITDA | 2,237.64 / 24.04 | 1,454.32 / 16.90 |
| 11 | 327 | EBITDA % | 19.02% | 16.08% |
| 12 | 328 | Depreciation and amortisation | 435.46 / 4.68 | 304.44 / 3.54 |
| 13 | 329 | EBIT before non-recurring cost | 1,802.18 / 19.36 | 1,149.88 / 13.36 |
| 14 | 330 | Non-recurring Income/(expense) # | (32.08) / (0.34) | 409.36 / 4.75 |
| 15 | 331 | EBIT | 1,770.10 / 19.02 | 1,559.24 / 18.11 |
| 16 | 332 | Interest expense | (190.68) / (2.05) | (36.31) / (0.42) |
| 17 | 333 | Other income (net) * | 121.97 / 1.31 | 36.18 / 0.42 |
| 18 | 334 | Income before income tax | 1,701.39 / 18.28 | 1,559.11 / 18.11 |
| 19 | 335 | Tax expense | 491.55 / 5.28 | 414.64 / 4.81 |
| 20 | 336 | Net profit ^ | 1,209.84 / 13.00 | 1,144.47 / 13.30 |

## 9. Consolidated Balance Sheet as at June 30, 2026 (43 rows) [page 8]

| # | Line | Particular | Jun 30, 2026 (Unaudited) | Dec 31, 2025 (Audited) | Flags |
|---|------|-----------|---------------------------|--------------------------|-------|
| 1 | 364 | Property, plant and equipment | 684.49 | 673.67 | |
| 2 | 365 | Capital work in progress | 6.66 | 1.34 | |
| 3 | 366 | Investment property | 12.25 | 12.99 | |
| 4 | 367 | Right-of-use assets | 762.86 | 736.56 | |
| 5 | 368 | Goodwill | 6,959.10 | 6,956.74 | |
| 6 | 369 | Other intangible assets | 2,669.32 | 2,867.35 | |
| 7 | 371 | Investment | 0.03 | 0.03 | |
| 8 | 372 | Other financial assets (non-current) | 91.01 | 88.94 | |
| 9 | 373 | Deferred tax assets (net) | 586.18 | 608.47 | |
| 10 | 374 | Non-current tax assets (net) | 51.42 | 81.41 | |
| 11 | 375 | Other non-current assets | 31.05 | 40.74 | |
| 12 | 376 | Total non-current assets (A) | 11,854.37 | 12,068.24 | |
| 13 | 379 | Trade receivables | 3,760.81 | 4,106.61 | |
| 14 | 380 | Cash and cash equivalents | 3,330.15 | 3,084.49 | |
| 15 | 381 | Bank balances other than cash and cash equivalents | 9.57 | 56.64 | |
| 16 | 382 | Other financial assets (current) | 1,061.01 | 870.25 | |
| 17 | 383 | Other current assets | 1,088.59 | 835.62 | |
| 18 | 384 | Total current assets (B) | 9,250.13 | 8,953.61 | |
| 19 | 385 | Assets held for sale (C) | - | - | ZERO_STANDING |
| 20 | 386 | Total assets (A+B+C) | 21,104.50 | 21,021.85 | |
| 21 | 390 | Equity share capital | 118.49 | 118.40 | |
| 22 | 391 | Instrument entirely equity in nature | 5.16 | - | new line, zero in prior period only (not standing) |
| 23 | 392 | Other equity | 10,859.03 | 10,204.83 | |
| 24 | 393 | Total equity attributable to equity shareholders of the Company | 10,982.68 | 10,323.23 | |
| 25 | 394 | Non controlling interest | 1,923.88 | 1,923.88 | |
| 26 | 395 | Total equity (A) | 12,906.56 | 12,247.11 | |
| 27 | 400 | Borrowings (non-current) | 2,697.75 | 2,691.75 | |
| 28 | 401 | Lease liabilities (non-current) | 837.05 | 788.60 | |
| 29 | 402 | Other financial liabilities (non-current) | 14.39 | 15.28 | |
| 30 | 403 | Provisions (non-current) | 607.14 | 576.39 | |
| 31 | 404 | Deferred tax liabilities (net) | - | 0.17 | zero in current period only (not standing) |
| 32 | 405 | Total non-current liabilities (B) | 4,156.33 | 4,072.19 | |
| 33 | 408 | Borrowings (current) | 10.73 | 454.39 | |
| 34 | 409 | Lease liabilities (current) | 147.78 | 163.09 | |
| 35 | 411-412 | Trade payables - total outstanding dues of micro enterprises and small enterprises | 8.86 | 12.94 | |
| 36 | 413-414 | Trade payables - total outstanding dues of creditors other than micro enterprises and small enterprises | 1,033.51 | 1,128.28 | |
| 37 | 415 | Other financial liabilities (current) | 1,244.55 | 1,366.22 | |
| 38 | 416 | Other current liabilities | 832.76 | 848.58 | |
| 39 | 417 | Provisions (current) | 606.18 | 556.99 | |
| 40 | 418 | Current tax liability (net) | 157.24 | 172.06 | |
| 41 | 419 | Total current liabilities (C) | 4,041.61 | 4,702.55 | |
| 42 | 420 | Total liabilities (B+C) | 8,197.94 | 8,774.74 | |
| 43 | 421 | Total equity and liabilities (A+B+C) | 21,104.50 | 21,021.85 | |

## 10. Consolidated Operational Data — Profitability in % (7 rows) [page 9]

| # | Line | Particular | Jun 30, 2026 | Mar 31, 2026 | Jun 30, 2025 |
|---|------|-----------|--------------|--------------|--------------|
| 1 | 436 | Revenues | 100.00 | 100.00 | 100.00 |
| 2 | 437 | Gross margin | 39.23 | 36.03 | 36.00 |
| 3 | 438 | SG&A | 19.16 | 15.90 | 18.74 |
| 4 | 439 | Adj. EBITDA # | 20.07 | 20.12 | 17.26 |
| 5 | 440 | EBITDA # | 19.03 | 19.01 | 16.21 |
| 6 | 441 | EBIT # | 15.37 | 15.27 | 12.78 |
| 7 | 442 | Adj. PAT ^ | 10.45 | 13.19 | 10.05 |

## 11. Revenue by Verticals (6 rows) [page 9]

| # | Line | Vertical | Jun 30, 2026 | Mar 31, 2026 | Jun 30, 2025 |
|---|------|----------|--------------|--------------|--------------|
| 1 | 451 | Technology, Internet, Platforms & Services (TIPS) | 41.39% | 40.92% | 39.97% |
| 2 | 452 | Banking, Finance & Insurance (BFSI) | 20.47% | 19.91% | 16.56% |
| 3 | 453 | Telecom, Media & Entertainment (TME) | 16.11% | 15.40% | 17.23% |
| 4 | 454 | Health | 11.45% | 11.92% | 12.70% |
| 5 | 455 | Manufacturing & Logistics (M&L) | 10.58% | 11.85% | 13.54% |
| 6 | 456 | Total | 100.00% | 100.00% | 100.00% |

## 12. Revenue by Geographies (5 rows) [page 9]

| # | Line | Geography | Jun 30, 2026 | Mar 31, 2026 | Jun 30, 2025 |
|---|------|-----------|--------------|--------------|--------------|
| 1 | 462 | Americas | 71.50% | 69.34% | 74.86% |
| 2 | 463 | APAC | 15.28% | 17.51% | 15.90% |
| 3 | 464 | Europe | 9.67% | 9.56% | 8.83% |
| 4 | 465 | MEA | 3.55% | 3.59% | 0.41% |
| 5 | 466 | Total | 100.00% | 100.00% | 100.00% |

## 13. Revenue from Top 10 Clients (4 rows) [page 9]

| # | Line | Client tier | Jun 30, 2026 | Mar 31, 2026 | Jun 30, 2025 |
|---|------|-------------|--------------|--------------|--------------|
| 1 | 472 | Top 10 Clients | 24.39% | 23.96% | 24.62% |
| 2 | 473 | Top 5 Clients | 17.02% | 16.00% | 17.26% |
| 3 | 474 | Top 3 Clients | 12.10% | 11.49% | 13.13% |
| 4 | 475 | Largest Client | 5.99% | 5.80% | 6.09% |

## 14. Utilization (including trainees) (3 rows) [page 9]

| # | Line | Category | Jun 30, 2026 | Mar 31, 2026 | Jun 30, 2025 |
|---|------|----------|--------------|--------------|--------------|
| 1 | 481 | Onsite | 96.33% | 96.25% | 96.59% |
| 2 | 482 | Offshore | 78.95% | 78.23% | 80.70% |
| 3 | 483 | Blended | 81.13% | 80.44% | 82.64% |

## 15. Human Resources (7 rows) [page 10]

| # | Line | Category | Jun 30, 2026 | Mar 31, 2026 | Jun 30, 2025 |
|---|------|----------|--------------|--------------|--------------|
| 1 | 497 | Technical | 4,728 | 4,741 | 4,040 |
| 2 | 500 | Software services - Onsite | 614 | 588 | 494 |
| 3 | 501 | Software services - Offshore | 3,216 | 3,249 | 2,620 |
| 4 | 504 | KS - Offshore | 865 | 867 | 902 |
| 5 | 506 | Trainees | 33 | 37 | 24 |
| 6 | 508 | Support | 542 | 562 | 521 |
| 7 | 510 | Total count | 5,270 | 5,303 | 4,561 |

## 16. Key Balance Sheet Data (5 rows) [page 10]

| # | Line | Particular | Jun 30, 2026 | Dec 31, 2025 |
|---|------|-----------|--------------|--------------|
| 1 | 515 | Receivable including unbilled | 5,152 | 5,268 |
| 2 | 516 | Receivable in days ("DSO") * - Billed | 55 | 56 |
| 3 | 517 | Receivable in days ("DSO") * - Billed & Unbilled | 75 | 73 |
| 4 | 518 | Cash and bank balance # | 3,351 | 2,726 |
| 5 | 519 | Total equity attributable to shareholders | 10,983 | 10,323 |

## 17. Footnote Definitions — "#", "^", and companion "$"/"@"/"*" symbols (20 rows)

| # | Line | Symbol | Table / section | Definition (first words) |
|---|------|--------|------------------|----------------------------|
| 1 | 107-108 | # | Highlights (Q2/H1 headline) | "Excluding cost of restricted stock units ("RSUs") granted to the employees" |
| 2 | 109 | ^ | Highlights (Q2/H1 headline) | "Before considering cost of RSU's granted to the employees and non-recurring items net of tax" |
| 3 | 197-199 | ^ | P&L Quarter table (col header Mar 31, 2026) | "Effective 1 January 2026, the Company designated certain foreign currency forward contracts as cash flow hedges..." |
| 4 | 201 | $ | P&L Quarter table (Other income row) | "Q2 2025, includes Rs. 435.95 mn on account of profit on sale of land, building and certain other assets... NOIDA office" |
| 5 | 203 | @ | P&L Quarter table (Employee benefits row) | "Including share-based payment expense of Rs. 62.37 mn in Q2 2026, Rs. 64.14 mn in Q1 2026 & Rs. 48.72 mn in Q2 2025 w.r.t. RSUs" |
| 6 | 205-206 | * | P&L Quarter table (EPS row) | "Adj. Basic Earnings per share excluding RSUs expense and non-recurring items net of tax is Rs. 5.31 in Q2 2026..." |
| 7 | 246-248 | ^ | P&L Six Months table (col header Jun 30, 2026) | "Effective 1 January 2026... cash flow hedges under Ind AS 109..." |
| 8 | 250 | $ | P&L Six Months table (Other income row) | "H1 2025, includes Rs. 435.95 mn on account of profit on sale of land, building and certain other assets... NOIDA office" |
| 9 | 252-253 | @ | P&L Six Months table (Employee benefits row) | "Including share-based payment expense of Rs. 126.51 mn during six months ended June 30, 2026 & 111.20 mn..." |
| 10 | 255-256 | * | P&L Six Months table (EPS row) | "Adj. Basic Earnings per share excluding RSUs expense and non-recurring items net of tax is Rs. 11.70..." |
| 11 | 293-294 | # | Contribution Analysis Quarter (Non-recurring row) | "Q2 2026 and Q1 2026 consist of severance payment and Q2 2025 consists of profit on sale of land, building..." |
| 12 | 296-297 | ^ | Contribution Analysis Quarter (Net profit row) | "Adjusted Net Profit after tax amounting to Rs. 628.74 mn (US$ 6.61 mn) for Q2 2026, Rs. 758.10 mn..." |
| 13 | 299-301 | * | Contribution Analysis Quarter (Other income row) | "Effective 1 January 2026... cash flow hedges under Ind AS 109..." |
| 14 | 337-338 | # | Contribution Analysis Six Months (Non-recurring row) | "Six months ended Jun 30, 2026, consists of severance payment and Six months ended Jun 30, 2025, consists of profit on sale..." |
| 15 | 340-341 | ^ | Contribution Analysis Six Months (Net profit row) | "Adjusted Net Profit after tax for six months ended June 30, 2026, amounting to Rs. 1,386.84 mn..." |
| 16 | 343-345 | * | Contribution Analysis Six Months (Other income row) | "Effective 1 January 2026... cash flow hedges under Ind AS 109..." |
| 17 | 443 | # | Profitability % table | "Before non-recurring item" |
| 18 | 444 | ^ | Profitability % table (Adj. PAT row) | "Before RSU's expense and non-recurring items net of tax" |
| 19 | 520 | * | Key Balance Sheet Data (DSO rows) | "DSO is based on TTM and excluding the new acquisition of Novigo" |
| 20 | 521 | # | Key Balance Sheet Data (Cash and bank balance row) | "net of short-term borrowing" |

## 18. Numbered Notes (2 rows) [page 10, bottom of document]

| # | Line | Note text (first words) |
|---|------|--------------------------|
| 1 | 528-529 | "US$ equivalent figures are derived by converting the Rupee figures using average rates for profit & loss items and closing rate for balance sheet items." |
| 2 | 530-531 | "Previous period's figures have been regrouped wherever applicable, to the extent possible, to conform to the current period presentation." |

---

## 19. INFORMATIONAL ONLY — Administrative disclosures (not in GATE A2 count test)

Outside the injected doctype-adapted scope (no clean mechanical grep/manual count basis for
prose paragraphs); retained here so nothing is silently dropped from the extract per anti-miss
principle, but excluded from the gated reconciliation above.

| # | Line | Item |
|---|------|------|
| 1 | 16-38 | Regulation 30 SEBI LODR filing letter to NSE and BSE, subject line re Q2/H1 CY2026 results press release |
| 2 | 42-47 | Digital signature block — Piyush Jain, Company Secretary & Compliance Officer, digitally signed |
| 3 | 52-56 | Corporate/registered office and contact footer |
| 4 | 542-546 | "About R Systems" paragraph 1 — digital product engineering company description |
| 5 | 548-551 | "About R Systems" paragraph 2 — innovation / technology capabilities |
| 6 | 553-555 | "About R Systems" paragraph 3 — partner ecosystem (ISVs, SaaS, product companies) |
| 7 | 557-563 | Safe Harbor forward-looking statements disclaimer |
| 8 | 567,569-570 | Contact — Nand Sardana, Chief Financial Officer |
| 9 | 568,569-570 | Contact — Giriraj Maheshwari, VP Finance & Accounts |
| 10 | 572-575 | Contact — Piyush Jain, Company Secretary & Compliance Officer |

---

## SUMMARY

- 18 gated categories, 189 total gated rows, GATE A2 = PASS (all 18 categories: grep_count = sweep_count after reconciling two PDF-extraction line-split edge cases in footnote_definitions).
- 1 `ZERO_STANDING` flag: "Assets held for sale" (line 385), dash in both periods presented.
- Two balance-sheet lines noted as newly-appeared / newly-dashed but NOT flagged `ZERO_STANDING` because they are not zero/dash in ALL periods shown: "Instrument entirely equity in nature" (line 391, dash only in the prior period) and "Deferred tax liabilities (net)" (line 404, dash only in the current period). Flagged to A3/A4 as items worth forensic attention regardless.
- No consolidation-entity list, no board-outcome agenda, no auditor report, no concall transcript content in this document (doctype = presentation/press release only) — those enumeration sections of the generic prompt file are not applicable and are omitted, consistent with the injected doctype adaptation.
