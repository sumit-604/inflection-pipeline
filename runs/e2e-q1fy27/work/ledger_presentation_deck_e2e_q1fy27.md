# A2 ENUMERATION LEDGER — Investor Presentation Deck
Company: E2E Networks Limited (E2E) | Quarter: Q1 FY27
Source: `extract_presentation_deck_e2e_q1fy27.txt` (22-slide investor deck, OCR on slides 2 and 15)
Cross-check baselines in this run's `work/` folder:
- `extract_presentation_e2e_q1fy27.txt` = same-day PRESS RELEASE (2 pages, doctype tagged "presentation" by orchestrator but content is the press release)
- `extract_results_e2e_q1fy27.txt` = same-day RESULTS FILING (Board outcome letter + Annexure-I financials + two auditor limited-review reports, 7 pages, figures in Lakhs)

Scoping note on granularity: financial TABLES (slide 17 fund-raise table, slide 19, slide 20, slide 21) are enumerated at LINE-ITEM (row) grain, consistent with the results-filing convention ("every line item in every financial table"), with all period columns for that row folded into one ledger row. CHART data (slides 5, 11, 16 x2, 17, 18) are enumerated at one row per plotted data point, consistent with the extraction's own `[CHART, page N, OCR text: ...]` convention. Decorative/identifier numbers (CIN, phone numbers, page-footer numbers, email addresses, signature timestamps) are enumerated in a dedicated Identifiers table and excluded from the KPI/metric gate count, since they carry no business disclosure content — this scoping choice is stated explicitly so A3/A4 know what is and isn't inside the metrics gate.

=== A2 COUNT TEST ===
category: slides                          grep_count: 22   sweep_count: 22   match: yes
category: table_line_items                grep_count: 42   sweep_count: 42   match: yes
category: chart_data_points               grep_count: 51   sweep_count: 51   match: yes
category: footnotes_sources_disclaimers   grep_count: 16   sweep_count: 16   match: yes
category: zero_standing                   grep_count: 1    sweep_count: 1    match: yes
category: entities                        grep_count: 46   sweep_count: 46   match: yes
category: forward_looking_statements      grep_count: 12   sweep_count: 12   match: yes
gate_a2: pass
=== END COUNT TEST ===

Method notes for the count test:
- slides: `grep -c "^\[page "` = 22, matches pdfinfo page count in the A1 header (22) and the 22-row manual slide inventory below.
- table_line_items: grep of each table's row-label lines (slide 17 fund-raise table: header + 4 data rows; slide 19: header + 13 data rows; slide 20: header + 11 data rows; slide 21: header + 2 section dividers ("EQUITY AND LIABILITIES", "ASSETS") + 14 data rows), header/divider lines subtracted = 4+13+11+14 = 42. Cross-checked against manual row-by-row read of each table; match.
- chart_data_points: the 6 `[CHART, page N, OCR text: ...]` tag lines were parsed by hand for genuine plotted values (excluding period/year labels and page numbers, which a naive numeric regex over-catches — shown and discounted in the working). Page 5 = 3, page 11 = 3, page 16 EBITDA = 10, page 16 PAT = 10, page 17 Capex = 6, page 18 MRR = 19 (17 monthly points + "14.1x" growth annotation + "75.2%" margin annotation restated on this slide; the "51" and "718" that recur in the growth annotation are NOT double-counted since they duplicate the Jun-22 and Jun-26 series points already counted). Total = 51. A second independent manual pass reproduced 51.
- footnotes_sources_disclaimers: grep for `Source:|Disclaimer:|Safe Harbour Statement|Data as of|^# FY26` plus the four bare citations on slide 6's stat row (Oppenheimer/McKinsey/Gartner/NVIDIA) and two more (Knight Frank/Industry reports; PIB-MeitY/Knight Frank) that carry no "Source:" prefix — counted at individual-citation grain, excluding the `[CHART]`-tag line's duplicate echo of the Synergy Research Group and CWIP footnotes (already counted once in native slide text). One false-positive line (the A1 extraction header's own methodology note, line 16, "- Source: 22-page investor presentation PDF...") was excluded as it is not deck content. Net = 16. Manual sweep = 16. Match.
- zero_standing: one cell, "Balance funds" = 0.00 for the Q2'25 tranche in the slide-17 fund-raise table.
- entities: manual roster of 15 named persons + 31 named organisations/institutions = 46, cross-validated with a title-cue grep (Director/CEO/CFO/CTO/CBO/Company Secretary/Managing Partner/Chairman/Strategic Advisor) that independently located all eight board-slide names and all five leadership-slide names plus Ronit and the two IR-advisor names on the contact slide, with no roster member missed on re-sweep.
- forward_looking_statements: manual sweep of 12 items, cross-validated with a cue-word grep (forward-looking / planned / planning underway / expected / forecast / roadmap / by 2030 / by 2031 / this decade / accelerate) that hit all 12 locations plus the Safe Harbour paragraph itself.

---

## TABLE A — SLIDE INVENTORY (22 slides)

| Slide | Title | Content type | Notes | Flags |
|---|---|---|---|---|
| 1 | Cover letter to NSE/BSE re: Investor Presentation (Reg. 30 SEBI LODR) | text (regulatory letter) | Addressed to NSE and BSE; digitally signed by Ronit (CS&CO), signed 2026.07.21 16:45:43 +05'30' | |
| 2 | Title/cover slide — "Q1 FY27 Investor Presentation, July 21, 2026" | photo/text (OCR, page under 100-char threshold) | E2E Networks logo; content visually confirmed per A1 header note | |
| 3 | Safe Harbour Statement | text (disclaimer) | Blanket forward-looking-statement disclaimer covering AI infra capacity expansion, cloud platform capabilities, subsidiary operations, financial performance, capital allocation, industry outlook | |
| 4 | Who We Are — India's Sovereign Provider of Advanced Cloud GPUs | text/stat | 2 stats: 16+ years, 5100 GPUs | |
| 5 | A Structurally Undersupplied Market, Compounding Fast | text/stat + chart | Bar chart (Global Neocloud Market Revenue) + 3 side callout stats, each third-party sourced | |
| 6 | Sovereign AI Is Now National Infrastructure | text/stat | 8 sourced macro stats + "Data as of July 2026" note + closing narrative + bottom disclaimer | |
| 7 | Built in India, for India's AI Future | text/stat | Company history/capability stats: since 2009, GPU cloud since 2018, 100+ engineers, ~3,000 Hopper GPUs, 5,100+ GPUs live | |
| 8 | Integrated AI Platform & Monetization Models | text (descriptive) | No numeric KPIs; names TIR, Jarvislabs.ai, NVIDIA, Delhi NCR & Chennai DCs | |
| 9 | TIR AI/ML Platform | text (feature list) | No numeric KPIs; names Llama, Gemma, Stable Diffusion, vLLM, SGLang, Triton, PyTorch | |
| 10 | Jarvislabs.ai — Developer First GPU Cloud | text (feature list) | 1 date (Dec 2025 launch); GPU types H100/H200/A100/RTX Pro 6000 | |
| 11 | The Growth Story \| Capacity meets Demand | text/stat + chart | TODAY/IN DEPLOYMENT/ON THE ROADMAP columns + GPU Trajectory bar chart (FY25/FY26/FY27Q1) | |
| 12 | Board with Founders, Finance and Tech Experience | photo/text (8 director profiles) | 8 directors, each with name/role/bio/tenure figures | |
| 13 | Leadership Team | photo/text (5 profiles) | CFO, CTO, CBO, CS&CO, Strategic Advisor | |
| 14 | What's new this Quarter @E2E \| Q1 FY27 | text (4 highlight boxes) | Stock split & BSE listing; B200 1024 LIVE; SovCloud incorporated as WOS; leadership strengthened (Alok Ohrie) | |
| 15 | Section divider — "Q1 FY27 / Financial Highlights" | photo/text (OCR, page under 100-char threshold; tesseract returned empty, visually confirmed) | No data on this slide — pure divider | |
| 16 | The Quarter's Scoreboard \| Q1 FY27 | text/stat + 2 charts | Headline Revenue/EBITDA/PAT/Exit MRR + EBITDA & EBITDA-margin chart (5 qtrs) + PAT & PAT-margin chart (5 qtrs) | |
| 17 | Financial Highlights (Capex + fund-raise table) | chart + table | Capex bar chart FY22–Q1FY27 with CWIP footnote; preferential-issue fund-raise utilisation table (4 tranche rows) | ZERO_STANDING |
| 18 | Sixteen Quarters of Compounding Run-Rate | chart | Monthly Revenue Run-rate (MRR) chart, Jun-22 to Jun-26, 17 points + 14.1x growth annotation + restated 75.2% EBITDA margin | DISCLOSED_IN_DECK |
| 19 | Q1FY27 Financial Performance | table | 13-line-item quarterly P&L, Q1FY27 vs Q1FY26 vs Q4FY26 with YoY%/QoQ% | NUMERIC_INCONSISTENCY |
| 20 | Yearly Trends \| Income Statement | table | 11-line-item annual P&L, FY26/FY25/FY24/FY23 | |
| 21 | Yearly Trends \| Balance Sheet | table | 14-line-item balance sheet, Mar-26/Mar-25/Mar-24 | DISCLOSED_IN_DECK |
| 22 | Thank You / contact page | text | CS&CO contact + IR advisor (Adfactors PR) contacts | |

DROPPED_SLIDE check: no prior-quarter deck ledger was supplied for this run (no `PRIOR_LEDGER_PATH` given, and no prior E2E run folder or company memory file exists in the repo — confirmed via search). This check is therefore **not applicable** this run; not a mechanical gate failure, but flagged so A3/A4 know a slide-drop comparison could not be performed and should not be inferred as "no slides dropped."

---

## TABLE B — METRICS, KPIs & NUMBERS (per-slide, business-relevant; 124 rows)

### Slide 4 — Who We Are
| # | Metric | Value | Flags |
|---|---|---|---|
| 4.1 | Years of operational excellence | 16+ years | |
| 4.2 | Cloud GPUs live at Q1 FY27 exit (approx.) | 5,100 | |

### Slide 5 — Market sizing
| # | Metric | Value | Flags |
|---|---|---|---|
| 5.1 | Global data-centre capex needed by 2030 (~70% AI-driven) | US$6.7T | source: McKinsey, Apr 2025 |
| 5.2 | Neocloud/GPU-cloud providers active globally today | 100+ | source: DriveNets; Thunder Compute, 2026 |
| 5.3 | Share of neocloud revenue from AI inference by 2030 | 80% | source: ABI Research, 2026 |
| 5.4 | [CHART] Global Neocloud Market Revenue — 2025 (Actual) | $25B | source: Synergy Research Group, 2026 |
| 5.5 | [CHART] Global Neocloud Market Revenue — 2030 (Forecast) | $180B | source: Synergy Research Group, 2026 |
| 5.6 | [CHART] Global Neocloud Market Revenue — 2031 (Forecast) | $400B | source: Synergy Research Group, 2026 |

### Slide 6 — Sovereign AI macro stats
| # | Metric | Value | Flags |
|---|---|---|---|
| 6.1 | Estimated global sovereign-AI infra opportunity this decade | US$1.5T | source: Oppenheimer research estimate, 2025 |
| 6.2 | Global data-centre capex needed by 2030 (~70% AI-driven) | US$6.7T | source: McKinsey, 2025 (restated from slide 5) |
| 6.3 | Neocloud/GPU-cloud share of the US$267B AI-cloud market by 2030 | 20% | source: Gartner, Jun 2026; US$267B market size also disclosed inline here |
| 6.4 | GPUs South Korea committed in a single 2026 sovereign-AI deal with NVIDIA | 250,000+ | source: NVIDIA, 2026 |
| 6.5 | India's total data-centre pipeline | 8.33 GW | source: Knight Frank India, Jun 2026; "over 5x today's ~1.6 GW live capacity" stated inline |
| 6.6 | India's current live data-centre capacity (inline reference, not a headline stat) | ~1.6 GW | derived from 8.33 GW stat's own text |
| 6.7 | Investment underpinning India's data-centre capacity build-out | ~$30 bn | source: Industry reports, 2026 |
| 6.8 | GPUs under IndiaAI Mission | 38,000+ | source: PIB/MeitY, Govt. of India, 2026 |
| 6.9 | Mumbai data-centre capacity anchor | 3.75 GW | source: Knight Frank India, 2026 |
| 6.10 | Chennai data-centre capacity anchor | 1.36 GW | source: Knight Frank India, 2026 (same citation as 6.9) |
| 6.11 | Closing narrative restates pipeline scale | "8 GW+ build-out" | rounds the 8.33 GW figure (6.5) |

### Slide 7 — Built in India
| # | Metric | Value | Flags |
|---|---|---|---|
| 7.1 | Operating since | 2009 | "India's first NSE-listed cloud provider" claim |
| 7.2 | GPU cloud since | 2018 | |
| 7.3 | In-house engineers | 100+ | |
| 7.4 | Hopper GPUs deployed | nearly 3,000 | |
| 7.5 | GPUs live, powering IndiaAI Mission foundational models | 5,100+ | |

### Slide 10 — Jarvislabs.ai
| # | Metric | Value | Flags |
|---|---|---|---|
| 10.1 | E2E Platform since | December 2025 | |

### Slide 11 — Growth story / GPU trajectory
| # | Metric | Value | Flags |
|---|---|---|---|
| 11.1 | GPUs live today (incl. 1024 B200) | ~5,100 (of which 1,024 B200) | DISCLOSED_IN_DECK (1,024 B200 count not in press release) |
| 11.2 | B200s planned (in deployment) | 1,024+ | forward guidance figure; DISCLOSED_IN_DECK |
| 11.3 | [CHART] GPU Trajectory — FY25 | 1,900 | DISCLOSED_IN_DECK (historical trajectory not in press release) |
| 11.4 | [CHART] GPU Trajectory — FY26 | 3,900 | DISCLOSED_IN_DECK |
| 11.5 | [CHART] GPU Trajectory — FY27Q1 | 5,100 | consistent with 11.1 and press release's ~5,100 GPU figure |

### Slide 12 — Board profiles
| # | Metric | Value | Flags |
|---|---|---|---|
| 12.1 | Tarun Dua — years in open source/virtualization/cloud | 23+ yrs | |
| 12.2 | Srishti Baweja — years in finance & compliance | 20 yrs | |
| 12.3 | Megha Raheja — years in IT/ITES, telecom, accounting, treasury, M&A | 22+ yrs | |
| 12.4 | Karthik Reddy Bezawada — Blume Ventures AUM | ~$650M | |
| 12.5 | Shrimati Ambastha — years across Oracle/VMware/NTT | 33 yrs | |
| 12.6 | Prashant Chiranjive Jain — years across energy/oil & gas/IT consulting | 30+ yrs | |

### Slide 13 — Leadership team
| # | Metric | Value | Flags |
|---|---|---|---|
| 13.1 | Nitin Jain (CFO) — global finance leadership | two decades | |
| 13.2 | Ronit (CS&CO) — corporate governance experience | 8+ years | |
| 13.3 | Alok Ohrie — Dell Technologies India tenure | 2013–25 | |
| 13.4 | Alok Ohrie — years in IT | 35+ years | NUMERIC_INCONSISTENCY vs slide 14's "30+ years" for the same person |

### Slide 14 — Quarter highlights
| # | Metric | Value | Flags |
|---|---|---|---|
| 14.1 | Stock split ratio | 10:1 | matches results-filing note 4 |
| 14.2 | B200 GPU cluster count | 1,024 | DISCLOSED_IN_DECK (press release names "B200 cluster" with no count) |
| 14.3 | Alok Ohrie — years in enterprise tech & GTM (bio blurb, this slide) | 30+ years | NUMERIC_INCONSISTENCY vs slide 13's "35+ years" for the same person |

### Slide 16 — The Quarter's Scoreboard
| # | Metric | Value | Flags |
|---|---|---|---|
| 16.1 | Revenue | INR 1,568 Mn (+334.3% YoY, +64.0% QoQ) | NUMERIC_INCONSISTENCY (press release states +334.1% YoY / +63.9% QoQ) |
| 16.2 | EBITDA | INR 1,179 Mn, 75.2% margin | |
| 16.3 | PAT | INR 439 Mn, 28.0% margin | |
| 16.4 | Exit MRR (Jun-26) | INR 718 Mn vs ₹374 Mn (Mar-26) | DISCLOSED_IN_DECK (not in press release or results filing) |
| 16.5 | [CHART] EBITDA — Q1 FY26 | 105 (29% margin) | |
| 16.6 | [CHART] EBITDA — Q2 FY26 | 180 (41% margin) | |
| 16.7 | [CHART] EBITDA — Q3 FY26 | 397 (57% margin) | |
| 16.8 | [CHART] EBITDA — Q4 FY26 | 581 (61% margin) | consistent with slide 19 table |
| 16.9 | [CHART] EBITDA — Q1 FY27 | 1,179 (75% margin, rounded) | consistent with 16.2 |
| 16.10 | [CHART] PAT — Q1 FY26 | -28 (-8% margin) | consistent with slide 19 table |
| 16.11 | [CHART] PAT — Q2 FY26 | -135 (-31% margin) | |
| 16.12 | [CHART] PAT — Q3 FY26 | -57 (-8% margin) | |
| 16.13 | [CHART] PAT — Q4 FY26 | 64 (7% margin, rounded) | **NUMERIC_INCONSISTENCY**: slide 19 table states Q4FY26 PAT = 65 (INR Mn) for the identical metric/period — a 1 Mn discrepancy between this chart and the table on slide 19. Results-filing standalone/consolidated Q4FY26 (31-Mar-26) PAT = 643.56 Lakhs = 64.356 Mn, which rounds to 64 — supporting this chart's figure over slide 19's "65." |
| 16.14 | [CHART] PAT — Q1 FY27 | 439 (28% margin) | consistent with 16.3 |

### Slide 17 — Capex & fund-raise table
| # | Metric | Value | Flags |
|---|---|---|---|
| 17.1 | [CHART] Capex — FY22 | INR 249 Mn | DISCLOSED_IN_DECK |
| 17.2 | [CHART] Capex — FY23 | INR 350 Mn | DISCLOSED_IN_DECK |
| 17.3 | [CHART] Capex — FY24 | INR 1,853 Mn | DISCLOSED_IN_DECK |
| 17.4 | [CHART] Capex — FY25 | INR 8,700 Mn | DISCLOSED_IN_DECK |
| 17.5 | [CHART] Capex — FY26 | INR 6,962 Mn | DISCLOSED_IN_DECK; see footnote on CWIP of INR 5,334 Mn included in this figure |
| 17.6 | [CHART] Capex — Q1FY27 | INR 177 Mn | DISCLOSED_IN_DECK (press release only references "new GPU capex" qualitatively, no figure) |
| 17.7 | Fund-raise table — Q2'25 tranche (Fund raised / Utilized till FY26 / Utilized in Q1'FY27 / Balance funds) | 4,056.56 / 3,555.05 / 501.51 / 0.00 | **ZERO_STANDING** on Balance funds cell (fully utilised) |
| 17.8 | Fund-raise table — Q3'25 tranche | 10,792.78 / 10,021.98 / 468.26 / 302.54 | |
| 17.9 | Fund-raise table — Q4'26 tranche | 1,070.00 / 27.61 / 18.14 / 1,024.25 | |
| 17.10 | Fund-raise table — Total | 15,919.34 / 13,604.64 / 987.91 / 1,326.79 | |

### Slide 18 — MRR run-rate chart
| # | Metric | Value | Flags |
|---|---|---|---|
| 18.1–18.17 | [CHART] Monthly Revenue Run-rate, Jun-22 through Jun-26 (17 monthly points) | Jun-22:51, Sep-22:56, Dec-22:58, Mar-23:61, Jun-23:68, Sep-23:72, Dec-23:85, Mar-24:109, Jun-24:113, Sep-24:112, Dec-24:145, Mar-25:145, Jun-25:165, Sep-25:160, Dec-25:280, Mar-26:374, Jun-26:718 (all INR Mn) | DISCLOSED_IN_DECK — full MRR history not in press release/results filing |
| 18.18 | MRR growth multiple annotation | 14.1x in four years (₹51 Mn → ₹718 Mn) | DISCLOSED_IN_DECK |
| 18.19 | Q1 FY27 EBITDA margin (restated annotation on this slide) | 75.2% | repeat of 16.2's margin |

### Slide 19 — Q1FY27 Financial Performance table (13 line items, all values INR Mn unless %)
| # | Line item | Q1FY27 | Q1FY26 | YoY% | Q4FY26 | QoQ% | Flags |
|---|---|---|---|---|---|---|---|
| 19.1 | Operational Revenue | 1,568 | 361 | 334.3% | 956 | 64.0% | NUMERIC_INCONSISTENCY (see 16.1) |
| 19.2 | Total expenses | 389 | 256 | 51.9% | 375 | 3.7% | |
| 19.3 | EBITDA | 1,179 | 105 | 1022.8% | 581 | 102.9% | |
| 19.4 | EBITDA Margin % | 75.2% | 29.1% | 4,610 bps | 60.7% | 1,450 bps | NUMERIC_INCONSISTENCY: press release bullet list states +4,609 bps YoY / +1,446 bps QoQ (1–4 bps off this table); press release headline stat box separately states +1,450 bps QoQ, matching this table but conflicting with its own bullet list |
| 19.5 | Other Income | 114 | 150 | (24.0)% | 55 | 107.3% | |
| 19.6 | Depreciation | 606 | 274 | 121.2% | 513 | 18.1% | consistent with press release "₹606 Mn, up ₹93 Mn QoQ" (606−513=93) |
| 19.7 | Finance Cost | 101 | 18 | 449.0% | 37 | 173.0% | |
| 19.8 | PBT | 586 | (37) | 1683.8% | 86 | 581.4% | matches press release and results filing (5,862.64 Lakhs = 586.264 Mn) |
| 19.9 | Tax | 147 | (9) | 1733.3% | 21 | 600.0% | |
| 19.10 | PAT | 439 | (28) | 1667.9% | 65 | 575.4% | NUMERIC_INCONSISTENCY: see 16.13 (slide 16 chart shows Q4FY26 = 64, not 65) |
| 19.11 | PAT Margin % | 28.0% | (7.9)% | 3,590 bps | 6.7% | 2,130 bps | |
| 19.12 | Basic EPS | 2.14 | (0.14) | 1628.6% | 0.32 | 568.8% | matches results filing exactly |
| 19.13 | Diluted EPS | 2.10 | (0.14) | 1600.0% | 0.32 | 556.3% | matches results filing and press release exactly |

### Slide 20 — Yearly Trends: Income Statement (11 line items, INR Million)
| # | Line item | FY26 | FY25 | FY24 | FY23 | Flags |
|---|---|---|---|---|---|---|
| 20.1 | Operational Revenue | 2,456 | 1,640 | 945 | 662 | |
| 20.2 | Total Expenses | 1,193 | 673 | 466 | 331 | |
| 20.3 | EBITDA | 1,263 | 967 | 479 | 331 | |
| 20.4 | EBITDA Margin % | 51.4% | 59.0% | 50.6% | 50.0% | |
| 20.5 | Other Income | 340 | 394 | 16 | 8 | |
| 20.6 | Depreciation & Amortization Expense | 1,693 | 601 | 157 | 201 | |
| 20.7 | Finance Cost | 122 | 132 | 36 | 5 | |
| 20.8 | PBT | (212) | 628 | 302 | 132 | |
| 20.9 | Tax Expenses | (56) | 153 | 84 | 33 | |
| 20.10 | PAT | (156) | 475 | 219 | 99 | DISCLOSED_IN_DECK — annual trend not in press release/results filing (results filing only carries quarterly + FY26-YTD columns) |
| 20.11 | PAT Margin % | (6.3)% | 29.0% | 23.2% | 14.9% | |

### Slide 21 — Yearly Trends: Balance Sheet (14 line items, In INR Million)
| # | Line item | Mar-26 | Mar-25 | Mar-24 | Flags |
|---|---|---|---|---|---|
| 21.1 | Equity share capital | 206 | 200 | 145 | |
| 21.2 | Other equity | 16,645 | 15,728 | 564 | |
| 21.3 | Borrowings | 1,032 | 114 | 1,031 | DISCLOSED_IN_DECK — no balance sheet at all in press release; component of any net-debt calculation |
| 21.4 | Lease liability | 559 | 616 | 410 | DISCLOSED_IN_DECK |
| 21.5 | Other Non-Current liabilities | 197 | 245 | 93 | |
| 21.6 | Other Current liabilities | 4,643 | 8,904 | 309 | |
| 21.7 | TOTAL EQUITY AND LIABILITIES | 23,282 | 25,807 | 2,552 | |
| 21.8 | Property, plant and equipment | 14,966 | 9,471 | 1,558 | |
| 21.9 | Intangible Assets | 167 | 149 | 122 | |
| 21.10 | Right of Use Asset | 557 | 635 | 424 | |
| 21.11 | Non-Current Financial Assets and tax assets | 1,506 | 66 | 63 | |
| 21.12 | Current Financial assets | 3,982 | 13,702 | 153 | DISCLOSED_IN_DECK — likely includes cash/cash-equivalent balances relevant to any net-debt figure; deck does not itself label or compute a "net debt" figure anywhere |
| 21.13 | Other current assets | 2,104 | 1,784 | 232 | |
| 21.14 | TOTAL ASSETS | 23,282 | 25,807 | 2,552 | |

---

## TABLE C — FORWARD-LOOKING / GUIDANCE STATEMENTS (12 items)

| # | Slide | Statement | Type |
|---|---|---|---|
| C.1 | 3 | Safe Harbour Statement — blanket disclaimer covering forward-looking statements on AI infra capacity expansion, cloud platform capabilities, subsidiary operations, financial performance, capital allocation, industry outlook; "undertakes no obligation to update" | master disclaimer |
| C.2 | 5 | Global Neocloud Market Revenue forecast: $180B by 2030, $400B by 2031 | third-party market forecast cited by company |
| C.3 | 5 | US$6.7T global data-centre capex needed by 2030 | third-party forecast |
| C.4 | 5 | 80% of neocloud revenue from AI inference by 2030 | third-party forecast |
| C.5 | 6 | US$1.5T sovereign-AI infra opportunity "this decade" | third-party forecast |
| C.6 | 6 | 20% neocloud share of US$267B AI-cloud market by 2030 | third-party forecast |
| C.7 | 6 | India's 8.33 GW data-centre pipeline (vs ~1.6 GW live today) | third-party forward buildout context |
| C.8 | 6 | Closing narrative: "India's 8 GW+ build-out is bringing sovereign compute within reach, and E2E Networks is building it at home" | company aspirational positioning statement, unquantified |
| C.9 | 11 | "1,024+ B200s planned" (IN DEPLOYMENT) | explicit company capacity guidance |
| C.10 | 11 | "B300 / Vera Rubin — Next-generation Compute planning underway" (ON THE ROADMAP) | forward technology roadmap statement, unquantified |
| C.11 | 14 | SovCloud — "Deploying large-scale GPU infrastructure and enabling funding arrangements to accelerate AI infrastructure expansion" | forward statement on subsidiary plans, unquantified |
| C.12 | 14 | "Further senior leadership hires across business and technology functions" | forward hiring statement, unquantified |

Notable absence: the deck contains **no quantified company guidance** anywhere (no stated FY28/next-quarter revenue, EBITDA, margin, or capex target from management itself) — every quantified forward figure on the deck is a third-party market forecast (McKinsey/Gartner/Synergy/ABI/Oppenheimer/Knight Frank/etc.) or a capacity-deployment figure (1,024+ B200s), not a company financial target.

---

## TABLE D — FOOTNOTES, SOURCES & DISCLAIMERS (16 items)

| # | Slide | Item | First words |
|---|---|---|---|
| D.1 | 3 | Safe Harbour Statement (full disclaimer paragraph) | "This presentation has been prepared by E2E Networks..." |
| D.2 | 5 | Source citation for US$6.7T stat | "McKinsey & Company, 'The cost of compute' (Apr 2025)" |
| D.3 | 5 | Source citation for 100+ providers stat | "DriveNets; Thunder Compute (2026)" |
| D.4 | 5 | Source citation for market-revenue chart | "Synergy Research Group (2026)" |
| D.5 | 5 | Source citation for 80% stat | "ABI Research, 'The State of Neocloud' (2026)" |
| D.6 | 6 | Page-level data currency note | "Data as of July 2026" |
| D.7 | 6 | Source citation for US$1.5T stat | "Oppenheimer research estimate, 2025" |
| D.8 | 6 | Source citation for US$6.7T stat (repeat) | "McKinsey, 2025" |
| D.9 | 6 | Source citation for 20%/US$267B stat | "Gartner, Jun 2026" |
| D.10 | 6 | Source citation for 250,000+ GPU stat | "NVIDIA, 2026" |
| D.11 | 6 | Source citation for 8.33 GW stat | "Knight Frank India, Jun 2026" |
| D.12 | 6 | Source citation for ~$30bn stat | "Industry reports, 2026" |
| D.13 | 6 | Source citation for 38,000+ GPU stat | "PIB / MeitY, Govt. of India, 2026" |
| D.14 | 6 | Source citation for Chennai/Mumbai capacity stat | "Knight Frank India, 2026" |
| D.15 | 6 | Bottom-of-page disclaimer on third-party figures | "All third-party figures and any references to companies or individuals are drawn from publicly available sources..." |
| D.16 | 17 | Capex-chart footnote on CWIP | "# FY26 includes CWIP of INR 5,334 Mn for GPU's, deployed in May 2026" |

---

## TABLE E — NAMED PERSONS, PARTNERS & ENTITIES (46 items)

### Persons (15)
| # | Name | Role | Slide(s) |
|---|---|---|---|
| E.1 | Ronit | Company Secretary & Compliance Officer | 1, 13, 22 |
| E.2 | Tarun Dua | Managing Director, Co-founder | 12 |
| E.3 | Srishti Baweja | Whole-Time Director | 12 |
| E.4 | Megha Raheja | Whole-Time Director | 12 |
| E.5 | Gaurav Munjal | Chairman, Independent Director | 12 |
| E.6 | Sonu Gosain Soni | Independent Director | 12 |
| E.7 | Karthik Reddy Bezawada | Independent Director; Co-founder & Managing Partner, Blume Ventures | 12 |
| E.8 | Shrimati Ambastha | Non-Executive Non-Independent Director; CEO, L&T-Cloudfiniti | 12 |
| E.9 | Prashant Chiranjive Jain | Non-Executive Non-Independent Director; ex-MD GE Power India | 12 |
| E.10 | Nitin Jain | Chief Financial Officer | 13 |
| E.11 | Mohammed Imran | Chief Technology Officer | 13 |
| E.12 | Bakshish Dutta | Chief Business Officer | 13 |
| E.13 | Alok Ohrie | Strategic Advisor; ex-President & MD, Dell Technologies India | 13, 14 |
| E.14 | Snighter Albuquerque | Investor Relations Advisor, Adfactors PR | 22 |
| E.15 | Vanessa Fernandes | Investor Relations Advisor, Adfactors PR | 22 |

### Organisations / institutions (31)
| # | Name | Context | Slide(s) |
|---|---|---|---|
| E.16 | National Stock Exchange of India Ltd. (NSE) | listing exchange | 1 |
| E.17 | BSE Limited | listing exchange | 1, 14 |
| E.18 | E2E Networks Limited | the company | throughout |
| E.19 | SEBI | Regulation 30 LODR reference | 1 |
| E.20 | TIR | in-house AI/ML platform | 7, 8, 9, 11, 14 |
| E.21 | Jarvislabs.ai | in-house GPU-cloud platform | 7, 8, 10 |
| E.22 | NVIDIA | GPU supplier (Hopper, Blackwell, B200) | 6, 7, 8, 10, 14 |
| E.23 | SovCloud / Sovcloud Technologies Limited | wholly owned subsidiary | 14 |
| E.24 | Infollion Research | Gaurav Munjal's principal role | 12 |
| E.25 | Blume Ventures | Karthik Reddy Bezawada's firm (~$650M AUM) | 12 |
| E.26 | L&T-Cloudfiniti | Shrimati Ambastha's employer | 12 |
| E.27 | Oracle | prior employer cited in bio | 12 |
| E.28 | VMware | prior employer cited in bio | 12 |
| E.29 | NTT | prior employer cited in bio | 12 |
| E.30 | GE Power India | Prashant Chiranjive Jain's prior role | 12 |
| E.31 | Dell Technologies India | Alok Ohrie's prior role | 13, 14 |
| E.32 | ASSOCHAM National Council of Electronics Manufacturing | Alok Ohrie chairmanship | 13 |
| E.33 | Atal Innovation Mission (Govt. of India) | Alok Ohrie "Super Mentor" role | 13 |
| E.34 | Adfactors PR Pvt. Ltd. | IR advisors | 22 |
| E.35 | McKinsey & Company | market-data source | 5, 6 |
| E.36 | Synergy Research Group | market-data source | 5 |
| E.37 | DriveNets | market-data source | 5 |
| E.38 | Thunder Compute | market-data source | 5 |
| E.39 | ABI Research | market-data source | 5 |
| E.40 | Oppenheimer | market-data source | 6 |
| E.41 | Gartner | market-data source | 6 |
| E.42 | Knight Frank India | market-data source | 6 |
| E.43 | PIB / MeitY, Govt. of India | market-data source | 6 |
| E.44 | IndiaAI Mission | national programme referenced | 6, 7 |
| E.45 | IIT Bombay | Gaurav Munjal's education | 12 |
| E.46 | IIM Bangalore | Sonu Gosain Soni's education | 12 |

Named products/technologies (not gated in the entities count, listed for completeness): Hopper, Blackwell, B200, B300, Vera Rubin, H100, H200, A100, RTX Pro 6000 (GPU models); Llama, Gemma, Stable Diffusion, vLLM, SGLang, Triton, PyTorch (AI/ML software).

**Named customers: ZERO across all 22 slides.** No customer name, logo, or case study appears anywhere in the deck, despite the claim on slide 7 that E2E's GPUs are "powering the IndiaAI Mission's foundational models." Flag: `ZERO_STANDING` — customer-name disclosure is a standing category that is nil in this deck, same as any zero-valued financial line item; not to be silently dropped from review.

---

## TABLE F — IDENTIFIERS / CONTACT INFO (not gated in metrics count, enumerated for completeness)

| # | Slide | Item |
|---|---|---|
| F.1 | 1 | CIN: L72900DL2009PLC341980 |
| F.2 | 1 | Phone: +91-11-4084-4964 |
| F.3 | 1 | Email: cs@e2enetworks.com |
| F.4 | 1 | Date: July 21, 2026 |
| F.5 | 1 | Scrip Code (BSE): 544783 |
| F.6 | 1 | Membership No. (Ronit, ICSI): A59215 |
| F.7 | 1 | Digital signature timestamp: 2026.07.21 16:45:43 +05'30' |
| F.8 | 22 | Contact email: investors@e2enetworks.com |
| F.9 | 22 | Tel: +91-11-4113 3905 |
| F.10 | 22 | Snighter Albuquerque mobile: +91 9819123804 |
| F.11 | 22 | Vanessa Fernandes mobile: +91 9773355200 |

---

## TABLE G — CROSS-CHECK vs PRESS RELEASE AND RESULTS FILING

Per task instruction: flag deck metrics dropped from the press release with `DISCLOSED_IN_DECK`; flag deck-vs-filing conflicts with `NUMERIC_INCONSISTENCY`.

| # | Metric class | In deck? | In press release? | In results filing? | Flag |
|---|---|---|---|---|---|
| G.1 | Exit MRR (₹718 Mn Jun-26, vs ₹374 Mn Mar-26) | Yes (16.4) | No | No | DISCLOSED_IN_DECK |
| G.2 | Full MRR history, Jun-22–Jun-26 (17 points) + 14.1x growth stat | Yes (18.1–18.18) | No | No | DISCLOSED_IN_DECK |
| G.3 | Capex by year, FY22–Q1FY27 (6 figures) + CWIP footnote | Yes (17.1–17.6) | No (only qualitative "new GPU capex" mention) | No | DISCLOSED_IN_DECK |
| G.4 | Balance sheet (Borrowings, Lease liability, all other line items, 3-year trend) | Yes (21.1–21.14) | No | No (results filing carries P&L + EPS only, no balance sheet) | DISCLOSED_IN_DECK |
| G.5 | GPU utilisation % (numeric) | **No** — deck itself has no numeric utilisation figure | No (press release states "utilization... remains strong" qualitatively only) | No | Not applicable — neither document discloses a number; note for A3/A4 that this KPI is absent company-wide, not merely dropped from the press release |
| G.6 | Realised GPU-hour pricing | No | No | No | Not applicable — not disclosed anywhere in this run's document set |
| G.7 | Contract duration / customer commitment terms | No | No | No | Not applicable — not disclosed anywhere; consistent with zero named customers (Table E) |
| G.8 | Net debt (explicitly labelled/computed figure) | No — deck gives Borrowings and Lease liability separately (21.3, 21.4) and Current Financial assets (21.12, likely includes cash) but never nets them into a stated "net debt" line | No | No | Not applicable as a labelled figure; components are DISCLOSED_IN_DECK (see G.4) but the net figure itself would require A3/A4 computation, not something enumerated as stated |
| G.9 | GPU count total (~5,100) | Yes (4.2, 7.5, 11.1, 11.5) | Yes ("approximately 5,100 GPUs") | No | Consistent — no flag; only the breakdown (1,024 B200, historical FY25/FY26 trajectory) is deck-exclusive (see G.10) |
| G.10 | B200 GPU count (1,024) and GPU trajectory (FY25: 1,900, FY26: 3,900) | Yes (11.1–11.4, 14.2) | No (press release names "B200 cluster" without a count) | No | DISCLOSED_IN_DECK |
| G.11 | Revenue YoY/QoQ growth % | Deck: +334.3% YoY / +64.0% QoQ (16.1, 19.1) | +334.1% YoY / +63.9% QoQ | Recomputable from Lakhs figures: (1,567.599−361.102)/361.102 = 334.1%; (1,567.599−956.427)/956.427 = 63.9% — matches the **press release**, not the deck | **NUMERIC_INCONSISTENCY**: deck's own 334.3%/64.0% is ~0.2pp off both the press release and the results-filing-derived recomputation |
| G.12 | EBITDA Margin % bps change | Deck (slide 19 table): 4,610 bps YoY / 1,450 bps QoQ | Bullet list: +4,609 bps YoY / +1,446 bps QoQ; headline stat box: +1,450 bps QoQ (conflicts with its own bullet list) | Not disclosed (results filing has no EBITDA line) | NUMERIC_INCONSISTENCY — small (1–4 bps) but present; also exposes an internal inconsistency within the press release itself between its headline box and bullet list |
| G.13 | Q4FY26 PAT (₹ Mn) | Deck slide 16 chart: 64; deck slide 19 table: 65 | Not separately disclosed (press release only gives PAT margin comparison "6.7% in Q4 FY'26") | Recomputable: 643.56 Lakhs = 64.356 Mn → rounds to 64 | **NUMERIC_INCONSISTENCY** — internal to the deck (chart vs table), with the results-filing-derived figure supporting the chart's "64" over the table's "65" |
| G.14 | Alok Ohrie years of experience | Slide 13: "35+ years in IT"; slide 14: "30+ years in enterprise tech & GTM" | Not applicable (advisor bio not in press release) | Not applicable | NUMERIC_INCONSISTENCY — internal to the deck, same person, two different figures across two slides |
| G.15 | PBT, PAT (headline), Basic/Diluted EPS, Depreciation | Deck matches press release and results filing (after Lakhs→Mn conversion) on all of these | — | — | No flag — confirms the deck, press release, and results filing agree on the core headline P&L figures; only the growth-rate percentages/bps and the Q4FY26 PAT chart-vs-table cell show discrepancies |

---

## SUMMARY COUNTS (feeds YAML below)
- slides: 22
- table_line_items (financial-table rows, slides 17/19/20/21): 42
- chart_data_points (slides 5, 11, 16 x2, 17, 18): 51
- footnotes/sources/disclaimers: 16
- zero_standing: 1
- entities (persons + organisations): 46
- forward_looking/guidance statements: 12
- Total metric/KPI rows in Table B: 124 (of which table_line_items=42 and chart_data_points=51 are subsets counted with their own grain in Table B; the remaining 31 are slide-level stat callouts not part of a table or chart)
