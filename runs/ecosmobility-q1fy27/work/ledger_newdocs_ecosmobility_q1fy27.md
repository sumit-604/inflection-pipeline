# A2 COMPLETENESS LEDGER — ECOSMOBILITY Q1 FY27 — NEW DOCS (Press Release + Investor Presentation)
Doctype: presentation (both documents). Combined ledger, count-test reconciled.
A1 sources:
- Press release: extract_pressrelease_ecosmobility_q1fy27.txt (4pp, formfeed_count 4)
- Presentation: extract_presentation_ecosmobility_q1fy27.txt (28pp, formfeed_count 28)
- Figure authority for OCR-mangled chart values: verified_supplement_deck_pressrelease.md (supplement wins on any OCR/supplement disagreement)

```
=== A2 COUNT TEST ===
category: pr_pages                          grep_count: 4    sweep_count: 4    match: yes
category: pr_cmd_quote_claims                grep_count: 11   sweep_count: 11   match: yes
category: pr_key_financial_summary_rows      grep_count: 7    sweep_count: 7    match: yes
category: pr_bullets_all_sections            grep_count: 14   sweep_count: 14   match: yes
category: pr_boilerplate_units               grep_count: 9    sweep_count: 9    match: yes
category: deck_slides                        grep_count: 28   sweep_count: 28   match: yes
category: deck_toc_items                     grep_count: 6    sweep_count: 6    match: yes
category: deck_chart_panels                  grep_count: 20   sweep_count: 20   match: yes
category: deck_income_statement_line_items   grep_count: 17   sweep_count: 17   match: yes
category: deck_balance_sheet_line_items      grep_count: 39   sweep_count: 39   match: yes
category: deck_hist_financials_datapoints    grep_count: 42   sweep_count: 42   match: yes
category: deck_industry_tam_units            grep_count: 25   sweep_count: 25   match: yes
category: deck_snapshot_units                grep_count: 16   sweep_count: 16   match: yes
category: deck_journey_milestones            grep_count: 14   sweep_count: 14   match: yes
category: deck_management_bios               grep_count: 8    sweep_count: 8    match: yes
category: deck_city_map_pie_units            grep_count: 13   sweep_count: 13   match: yes
category: deck_fleet_ownership_units         grep_count: 7    sweep_count: 7    match: yes
category: deck_vrqsr_items                   grep_count: 5    sweep_count: 5    match: yes
category: deck_quality_awards_units          grep_count: 17   sweep_count: 17   match: yes
category: deck_tech_stack_units              grep_count: 8    sweep_count: 8    match: yes
category: deck_competitive_advantage_rows    grep_count: 5    sweep_count: 5    match: yes
category: deck_long_standing_cust_datapoints grep_count: 12   sweep_count: 12   match: yes
category: deck_way_ahead_items               grep_count: 6    sweep_count: 6    match: yes
category: zero_standing_flagged_items        grep_count: 5    sweep_count: 5    match: yes
gate_a2: pass
=== END COUNT TEST ===
```
Note on grep method: page/slide markers reconciled via `grep -n "^\[page"`; chart panels via `grep -n "^\[CHART"`; table rows via `sed -n <range> | grep -n "|"`; bullet/list items via `grep -n "^  - "` / `grep -nE "^(19|20)[0-9]{2}\s"` / numbered-item and dash patterns per section, each cross-checked against a manual line-by-line read of the full extract. All 24 categories matched on first sweep; no re-sweep was required.

---
## PART 1 — PRESS RELEASE (extract_pressrelease_ecosmobility_q1fy27.txt, 4pp)

### 1A. Page/document-structure units (page 1 — Reg 30 covering letter)
| # | Line(s) | Unit | Flags |
|---|---------|------|-------|
| 1 | 24-26 | Addressee: The General Manager, Dept of Corporate Services, BSE Limited | |
| 2 | 26-29 | Addressee: The General Manager, Dept of Corporate Services, NSE of India Ltd | |
| 3 | 30 | Scrip Code 544239 (BSE) | |
| 4 | 30 | Symbol ECOSMOBLTY (NSE) | |
| 5 | 34-35 | Subject line: Press Release on Unaudited Financial Results for Q1 FY27 ended 30-Jun-2026 | |
| 6 | 39-42 | Regulatory reference: Reg 30 SEBI LODR 2015, in continuation of Board Meeting outcome dated 11-Aug-2026 | |
| 7 | 49-56 | Signature block: Shweta Bhardwaj, Company Secretary & Compliance Officer (digitally signed image block, no explicit timestamp text captured in this extract) | |
| 8 | 61-66 | Footer banner: "100+ Cities in India & 30+ Countries", 24x7 reservation line, website, Regd & Corp Office address | |
| 9 | 68 | CIN: L74999DL1996PLC076375 | |

### 1B. Headline / dateline (page 2)
| # | Line | Unit | Flags |
|---|------|------|-------|
| 10 | 75 | Slug: "Q1 FY27 Earnings Release" | |
| 11 | 77-78 | Headline: "16.7% YoY Revenue Growth in Q1 FY27; Trip Volumes Rise 27% and Active Client Base Expands 18%" | |
| 12 | 80-82 | Dateline: Delhi, August 11, 2026; company self-description ("one of the largest chauffeur-driven managed mobility providers to corporates in India") | |

### 1C. CMD quote — Mr. Rajesh Loomba, Chairman and Managing Director (lines 84-102), one narrative unit, 11 distinct claims
| # | Line | Claim (first ~15 words) | Flags |
|---|------|--------------------------|-------|
| 13 | 87-88 | "Q1 FY27 saw healthy operating momentum, with revenue from operations growing 16.7% year-on-year..." | |
| 14 | 88-89 | "...and trip volumes increasing 27%." | |
| 15 | 88-89 | "We added 61 new clients during the quarter, taking our active client base to approximately 1,400" | |
| 16 | 89 | "...while expanding our pan-India presence to 151 cities." | |
| 17 | 89-91 | "While margins during the quarter reflected changes in business mix and the operating cost environment..." | narrative framing of margin decline, cf. supplement Section I |
| 18 | 91-92 | "...we remain focused on disciplined profitable growth and improving operating efficiency as we scale." | no quantified recovery path given |
| 19 | 91-92 | "We continue to strengthen our technology platform and deepen our capabilities to support the next phase of growth." | |
| 20 | 94-95 | "During the quarter, we continued to strengthen our platform, with the launch of our new technology for CCR..." | |
| 21 | 95 | "...and further progress in our SIXT partnership." | |
| 22 | 95-96 | "These initiatives expand the ways in which we can serve customers while remaining focused on our core enterprise business." | |
| 23 | 98-102 | "As we look ahead, our priorities remain adding high-quality enterprise relationships, deepening engagement with existing customers and selectively expanding into new markets... position ECO Mobility well to capture the long-term opportunity in organized corporate mobility." | forward-looking priorities statement |

Cross-reference: same quote appears verbatim on deck page 6 (Part 2, row 2-6) — flag `DUPLICATE_ACROSS_DOCS`.

### 1D. Key Financial Summary table (lines 104-118) — 7 rows x 5 periods (Q1FY27, Q1FY26, YoY%, Q4FY26, QoQ%)
| # | Line | Particular | Q1FY27 | Q1FY26 | YoY% | Q4FY26 | QoQ% | Flags |
|---|------|-----------|--------|--------|------|--------|------|-------|
| 24 | 109 | Total Revenue | 2,151.20 | 1,839.94 | 16.91% | 2,103.78 | 2.25% | |
| 25 | 111 | Revenue from Operations | 2,113.72 | 1,811.19 | 16.70% | 2,067.60 | 2.23% | |
| 26 | 113 | EBITDA (Excl Other Income) | 218.47 | 219.18 | (0.32%) | 241.53 | (9.54%) | `SUPPLEMENT_DISAGREEMENT` — deck page 9 (supplement Section A) prints Q1FY26 EBITDA as 218.55 and YoY as (0.03)%, vs press release's 219.18 / (0.32%); supplement wins for figure authority but this is a press-release-vs-deck internal inconsistency, both retained on ledger for A3/A4 reconciliation |
| 27 | 114 | EBITDA Margin (%) | 10.34% | 12.07% | (173)bps | 11.68% | (134)bps | |
| 28 | 115 | Profit after Tax (PAT) | 145.50 | 132.87 | 9.50% | 157.37 | (7.54%) | |
| 29 | 117 | PAT Margin (%) | 6.76% | 7.22% | (46)bps | 7.48% | (72)bps | `SUPPLEMENT_DISAGREEMENT` — deck page 9 prints Q4FY26 PAT margin as 7.22%, vs press release's 7.48% here; two different values for the same period across the two same-quarter documents, neither is an OCR artifact (both native-text tables) — flag for A3 as a genuine inter-document inconsistency, not resolved by the supplement |
| 30 | 118 | EPS (X) | 2.42 | 2.21 | 9.5% | 2.63 | (8.0%) | |

### 1E. Performance Highlights bullets (lines 122-138), 4 bullets
| # | Line | Bullet (summary) | Flags |
|---|------|-------------------|-------|
| 31 | 128-129 | Revenue from Operations Q1FY27 ₹2,113.72 Mn, YoY +16.70%, QoQ +2.23% | |
| 32 | 131 | EBITDA for the quarter ₹218.47 Mn | |
| 33 | 133-135 | EBITDA Margin 10.34% vs 12.07% Q1FY26 vs 11.68% Q4FY26, "primarily reflecting changes in revenue mix and higher operating costs"; PAT ₹145.50 Mn, +9.50% YoY, (7.54%) QoQ | |
| 34 | 137-138 | Cash and investments ₹1,558 Mn as on 30-Jun-2026, "healthy balance sheet with low leverage" | cross-confirmed by supplement Section D net-cash calc (~₹137.6 Cr ex-lease on FY26-end BS, growing to ₹155.8 Cr by Q1FY27) |

### 1F. Operational Highlights bullets (lines 139-156), 6 bullets
| # | Line | Bullet (summary) | Flags |
|---|------|-------------------|-------|
| 35 | 141-142 | ~1.48 Mn trips, +27% YoY, +7% QoQ; ETS 59% / CCR 41% of revenue | |
| 36 | 144-145 | 61 new clients onboarded (vs 53 in Q1FY26); active client base ~1,400, +18% YoY | |
| 37 | 147-148 | Pan-India presence 151 cities, +20 new cities this quarter; international network 100+ countries | |
| 38 | 150-151 | Owned + vendor-operated fleet ~19,550 vehicles, +29% YoY from ~15,150; asset-light model continued | |
| 39 | 153 | EV fleet 460 vehicles vs 390 at end of Q4FY26 | |
| 40 | 155-156 | ~51% of revenue from customers >5 years' association | trend context: supplement Section E notes deck slide 26 shows this ratio drifting down 61%(FY25)→55%(FY26)→51%(Q1FY27) |

### 1G. Strategic Developments bullets (lines 159-171), 4 bullets
| # | Line | Bullet (summary) | Flags |
|---|------|-------------------|-------|
| 41 | 161-162 | Major upgrade to proprietary in-house technology platform | |
| 42 | 164-165 | Building SIXT strategic tie-up; early traction from business and leisure travelers, exclusive India GSA arrangement | |
| 43 | 167-168 | Strengthened leadership bandwidth in select areas, "deliberate investment ahead of next phase of growth" | |
| 44 | 170-171 | Board recommended final dividend ₹2.38/equity share for FY26, subject to shareholder approval at upcoming AGM | material corporate action; AGM date not yet disclosed in this document |

### 1H. Page 4 boilerplate units
| # | Line(s) | Unit | Flags |
|---|---------|------|-------|
| 45 | 177-188 | "About ECOS (India) Mobility & Hospitality Limited" company description paragraph (founded 1996, 29+ years, 151 cities, 100+ countries, 19,550+ fleet) | |
| 46 | 189-193 | Contact block 1: Ms. Shweta Bhardwaj, Company Secretary, legal@ecosmobility.com | |
| 46b | 190-193 | Contact block 2: Hashika Mutreja / Kashmira Parkar, Adfactors PR | counted jointly with #46 as one contacts unit-pair |
| 47 | 197-203 | Cautionary statement / forward-looking-statements disclaimer paragraph | |

**Press release row count: 47 discrete units (11 CMD-quote claims + 7 KFS rows + 14 bullets + 9 letter/structure units + 3 headline units + 3 boilerplate units).**

---
## PART 2 — INVESTOR PRESENTATION (extract_presentation_ecosmobility_q1fy27.txt, 28pp)

Slide numbering note: all "page N" markers below are PDF page numbers, matching the A1 extract's own page markers and pdfinfo (28 pages total, verified). The A1 header flags that the deck's internal slide numbering (visible on-slide) differs from PDF page order because PDF page 1 is a non-deck Reg 30 covering letter; PDF page numbers are used here as the unambiguous, source-traceable key.

### 2A. Slide inventory (28 of 28, GATE: slide count == 28)
| Slide (PDF pg) | Title / content type | Data unit type | Flags |
|---|---|---|---|
| 1 | Reg 30 covering letter to BSE/NSE (not a deck slide) | text/letter | |
| 2 | Deck title slide: "ECOS (India) Mobility and Hospitality Limited — Q1 FY27 Investor Presentation" | text | |
| 3 | Disclaimer slide | text (6 paragraphs) | |
| 4 | Table of Contents (6 items) | text list | |
| 5 | Section divider: "Q1 FY27 Result Highlights" | photo/title only | OCR FAILED, vision-verified |
| 6 | Management Comment slide — Mr. Rajesh Loomba, CMD | text quote (photo) | duplicate of press-release CMD quote, see 2B |
| 7 | "FY26 Performance Highlights" — 4 chart panels | chart | |
| 8 | "Q1 FY27 Performance Highlights" — 4 chart panels | chart | |
| 9 | "Q1 FY27 Consolidated Income Statement" — 17-row table | table | OCR corrupted digits, vision-verified |
| 10 | "Consolidated Balance Sheet for FY26" — 39-row table (both sides) | table | OCR corrupted digits, vision-verified; internal total mismatch flag, see 2E |
| 11 | "Historical Financials — Year-on-year Healthy Performance" — 4 chart panels, FY21-FY26 | chart | OCR unreliable, vision-verified |
| 12 | Section divider: "Industry Overview" | photo/title only | OCR FAILED, vision-verified |
| 13 | Industry market-size infographic (TAM), bubble charts + growth drivers | chart+text | UNIT = INR Bn, not Rs Mn — do not apply x0.1 factor |
| 14 | Section divider: "Company Overview" | photo/title only | OCR FAILED, vision-verified |
| 15 | "ECOS Mobility — A Snapshot" — 2 service-line panels + 3x4 stat grid | infographic | |
| 16 | "Journey Over the Years" — 14-item timeline | timeline | |
| 17 | "Seasoned Management" — 8 bios | text list | |
| 18 | Section divider: "Business Overview" | photo/title only | OCR FAILED, vision-verified |
| 19 | "Pan-India Presence... 151 Cities" — map + pie chart | map+chart | |
| 20 | "Fleet of Vehicles" — 5 categories + ownership-mix chart | infographic+chart | |
| 21 | "Business Drivers" (VRQSR framework) — 5 items | text | |
| 22 | "Business Drivers: High Quality of Service Leading to Strong Brand" — QC bullets, training, satisfaction, awards | text+stat | header states "10 items" but only 9 awards transcribed — flag `AWARDS_COUNT_MISMATCH` |
| 23 | "Business Drivers: Technology Enablers for Operational Excellence" | infographic | |
| 24 | "Competitive Advantage" — 5-row comparison table | table | |
| 25 | "Customers with Long Standing Relationships" — chart, FY21-FY26 | chart | OCR unreliable for bar values, vision-verified |
| 26 | Section divider: "Outlook" | photo/title only | OCR FAILED, vision-verified |
| 27 | "Way Ahead" — 6 items | text list | no quantified guidance — cf. supplement Section F |
| 28 | "Thank You" — closing/contacts slide | text | |

### 2B. Slide 6 — Management Comment (Rajesh Loomba, CMD) — same 11 claims as press-release CMD quote (Part 1C, rows 13-23)
| # | Slide | Claim | Flags |
|---|------|-------|-------|
| 48 | 6 | Identical 11-claim quote verbatim to press release lines 87-102 | `DUPLICATE_ACROSS_DOCS` — not re-enumerated in full; see Part 1C rows 13-23. Photo of Mr. Rajesh Loomba present. |

### 2C. Slide 7 — "FY26 Performance Highlights" chart panels (4 panels x 3 data points = 12 data points)
| # | Slide | Panel | FY25 | FY26 | Growth% | Flags |
|---|------|-------|------|------|---------|-------|
| 49 | 7 | Revenue from Operations, Rs Mn | 6,540 | 8,082 | 23.58% | vision-verified (OCR corrupted); matches supplement Section C |
| 50 | 7 | Total Revenue, Rs Mn | 6,639 | 8,194 | 23.43% | vision-verified; matches supplement Section C |
| 51 | 7 | EBITDA (Excl. Other Income), Rs Mn | 924 | 939 | 1.67% | vision-verified; matches supplement Section C |
| 52 | 7 | PAT, Rs Mn | 601 | 576 | (4.19%) | vision-verified; matches supplement Section C |

### 2D. Slide 8 — "Q1 FY27 Performance Highlights" chart panels (4 panels x 3 data points = 12 data points)
| # | Slide | Panel | Q1FY26 | Q1FY27 | Growth% | Flags |
|---|------|-------|--------|--------|---------|-------|
| 53 | 8 | Revenue from Operations, Rs Mn | 1,811 | 2,114 | 16.70% | vision-verified |
| 54 | 8 | Total Revenue, Rs Mn | 1,840 | 2,151 | 16.94% | vision-verified |
| 55 | 8 | EBITDA (Excl. Other Income), Rs Mn | 219 | 218 | (0.03)% | vision-verified; note press-release/deck-page-9 table both show 218.55 for this period elsewhere — this rounded bar shows 219, consistent |
| 56 | 8 | PAT, Rs Mn | 133 | 146 | 10.28% | vision-verified; growth% here (10.28%) differs from the 9.50% YoY PAT growth stated elsewhere (press release, deck slide 9) — both numbers are internally consistent with rounded (146 vs 133 = +9.77%, printed as 10.28% on the bar label) — flag `GROWTH_LABEL_INCONSISTENCY` for A3/A4 arithmetic check |

### 2E. Slide 9 — "Q1 FY27 Consolidated Income Statement" table (17 line items x 5 columns)
| # | Slide | Line item | Q1FY27 | Q1FY26 | YoY% | Q4FY26 | QoQ% | Flags |
|---|------|-----------|--------|--------|------|--------|------|-------|
| 57 | 9 | Revenue from operations | 2,113.72 | 1,811.19 | 16.70% | 2,067.6 | 2.23% | |
| 58 | 9 | Other income | 37.48 | 28.75 | — | 36.18 | — | YoY/QoQ% not stated (blank cells, not zero) |
| 59 | 9 | Total income | 2,151.20 | 1,839.94 | 16.92% | 2,103.78 | 2.25% | note: 16.92% here vs 16.91% in press-release KFS table for the same YoY% — rounding-level discrepancy, both retained |
| 60 | 9 | Total Cost of Service | 1,587.29 | 1,315.58 | — | 1,507.33 | — | |
| 61 | 9 | Purchase of Stock | — | 0.64 | — | 8.96 | — | `ZERO_STANDING` — dash in Q1FY27 column |
| 62 | 9 | Change in stock-in trade | — | (0.02) | — | 0.2 | — | `ZERO_STANDING` — dash in Q1FY27 column |
| 63 | 9 | Employee benefit expense | 237.63 | 194.90 | — | 219.71 | — | |
| 64 | 9 | Other expense | 70.32 | 81.54 | — | 89.87 | — | |
| 65 | 9 | EBITDA (Excl. of Other Income) | 218.47 | 218.55 | (0.03)% | 241.53 | (9.54)% | `SUPPLEMENT_DISAGREEMENT` vs press release Q1FY26 figure 219.18 / YoY (0.32%) — see Part 1D row 26; supplement (Section A) confirms deck's 218.55/(0.03)% as the authoritative figure |
| 66 | 9 | EBITDA Margins (%) | 10.34% | 12.07% | (173)Bps | 11.68% | (134)Bps | |
| 67 | 9 | Depreciation & amortisation expense | 61.55 | 58.30 | — | 79.43 | — | |
| 68 | 9 | Finance Cost | 2.77 | 2.32 | — | 1.75 | — | |
| 69 | 9 | Profit Before Tax for the period/year | 191.64 | 186.68 | 2.65% | 196.53 | (2.49)% | |
| 70 | 9 | Tax Expense | 46.14 | 53.81 | — | 39.16 | — | |
| 71 | 9 | Profit after tax for the period/year | 145.50 | 132.87 | 9.50% | 157.37 | (7.54)% | |
| 72 | 9 | PAT Margins (%) | 6.76% | 7.22% | (46)Bps | 7.22% | (72)Bps | `SUPPLEMENT_DISAGREEMENT` — Q4FY26 PAT margin printed 7.22% here vs 7.48% in press-release KFS table (Part 1D row 29) for the identical metric/period; two source documents disagree, neither is an obvious OCR artifact — unresolved, flag for A3 |
| 73 | 9 | EPS (Rs) | 2.42 | 2.21 | — | 2.63 | — | |

### 2F. Slide 10 — "Consolidated Balance Sheet for FY26" (39 line items, both sides, FY26 vs FY25 year-end)
**Assets side (22 rows incl. subtotals/grand total):**
| # | Slide | Line item | 31-Mar-26 | 31-Mar-25 | Flags |
|---|------|-----------|-----------|-----------|-------|
| 74 | 10 | Property, plant and equipment | 533.65 | 500.81 | |
| 75 | 10 | Investment property | 3.76 | 3.73 | |
| 76 | 10 | Intangible assets | (blank) | (blank) | `ZERO_STANDING` — line exists on the standard schedule with no value either period; template signal per NEVER-drop-nil rule |
| 77 | 10 | Intangible assets under development | 22.44 | 8.00 | |
| 78 | 10 | Right of use assets | 68.46 | 75.57 | |
| 79 | 10 | Investments (non-current, financial assets) | 4.26 | 4.42 | |
| 80 | 10 | Other financial assets (non-current) | 3.98 | 72.33 | |
| 81 | 10 | Other non-current assets | 9.16 | 8.45 | |
| 82 | 10 | Deferred tax assets (net) | 64.98 | 27.85 | |
| 83 | 10 | Total non-current assets (subtotal) | 710.69 | 701.16 | |
| 84 | 10 | Inventories | 0.50 | 0.96 | |
| 85 | 10 | Investments (current, financial assets) | 1,060.79 | 849.95 | |
| 86 | 10 | Trade receivables | 1,070.21 | 827.49 | feeds supplement Section D debtor-days calc (~48 days) |
| 87 | 10 | Cash and cash equivalents | 241.88 | 238.00 | |
| 88 | 10 | Other bank balances | 69.86 | 24.90 | |
| 89 | 10 | Loans | 4.05 | 3.43 | |
| 90 | 10 | Other financial assets (current) | 752.09 | 548.72 | |
| 91 | 10 | Current tax assets (net) | 30.74 | 20.41 | |
| 92 | 10 | Other current assets | 192.29 | 198.17 | |
| 93 | 10 | Assets held-for-sale | 1.83 | 0.83 | |
| 94 | 10 | Total current assets (subtotal) | 3,424.24 | 2,712.86 | |
| 95 | 10 | Total assets (grand total) | 4,134.93 | 3,414.02 | see #113 below — mismatches the equity+liabilities-side grand total for the FY25 column |

**Equity and Liabilities side (17 rows incl. subtotals/grand total):**
| # | Slide | Line item | 31-Mar-26 | 31-Mar-25 | Flags |
|---|------|-----------|-----------|-----------|-------|
| 96 | 10 | Equity share capital | 120.00 | 120.00 | |
| 97 | 10 | Other equity | 2,529.37 | 2,097.52 | |
| 98 | 10 | Total equity (subtotal) | 2,649.36 | 2,217.52 | |
| 99 | 10 | Non-controlling interest | 1.35 | — | `ZERO_STANDING` — dash in FY25 column |
| 100 | 10 | Borrowings (non-current) | — | 1.08 | `ZERO_STANDING` — dash in FY26 column (deleveraged to nil during the year) |
| 101 | 10 | Lease liability (non-current) | 61.04 | 66.15 | |
| 102 | 10 | Provisions (non-current) | 73.19 | 55.54 | |
| 103 | 10 | Total non-current liabilities (subtotal) | 134.23 | 122.77 | |
| 104 | 10 | Borrowings (current) | 1.07 | 58.99 | |
| 105 | 10 | Lease liability (current) | 15.68 | 17.72 | |
| 106 | 10 | Trade payables | 880.07 | 715.59 | |
| 107 | 10 | Other financial liabilities (current) | 346.19 | 205.74 | |
| 108 | 10 | Provisions (current) | 21.17 | 19.03 | |
| 109 | 10 | Other current liabilities | 85.80 | 56.66 | |
| 110 | 10 | Total current liabilities (subtotal) | 1,349.97 | 1,073.73 | |
| 111 | 10 | Total liabilities (subtotal) | 1,484.20 | 1,196.50 | |
| 112 | 10 | Total equity and liabilities (grand total) | 4,134.93 | 3,414.20 | |
| 113 | 10 | — | — | — | `NUMBER_DISCREPANCY` — as printed on the slide, Total assets (FY25 col) = 3,414.02 (row #95) but Total equity and liabilities (FY25 col) = 3,414.20 (row #112); a ₹0.18 Mn imbalance on the balance sheet as-printed. Transcribed exactly as printed per NEVER-estimate rule; not reconciled or corrected here — flag for A3/A4. |

### 2G. Slide 11 — "Historical Financials" 6-year chart panels (4 panels, FY21-FY26; 42 data points total)
| # | Slide | Panel/series | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 | Flags |
|---|------|--------------|------|------|------|------|------|------|-------|
| 114 | 11 | Revenue from Operations, Rs Mn | 1,038 | 1,473 | 4,227 | 5,544 | 6,540 | 8,082 | vision-verified |
| 115 | 11 | EBITDA (Excl. Other Income), Rs Mn | 157 | 181 | 697 | 900 | 924 | 939 | vision-verified; supplement Section B: absolute EBITDA plateaued ₹900→939 Mn FY24-26 |
| 116 | 11 | EBITDA Margin (%) | 15.2% | 12.3% | 16.5% | 16.2% | 14.1% | 11.6% | structural margin decline from FY23 peak, per supplement Section B |
| 117 | 11 | PAT, Rs Mn | 30 | 99 | 436 | 625* | 601 | 576 | footnote * "ECOs got listed in FY25" attached to FY24 data point |
| 118 | 11 | PAT Margin (%) | 2.7% | 6.5% | 10.3% | 11.0% | 9.1% | 7.0% | |
| 119 | 11 | ROCE (%) | 9.1% | 19.1% | 40.9% | 42.9% | 35.78% | 29.4% | ROCE fall 42.9%→29.4% FY24-26 |
| 120 | 11 | ROE (%) | 5.0% | 14.8% | 46.7% | 42.8% | 30.1% | 23.7% | ROE fall 42.8%→23.7% FY24-26 |
| 121 | 11 | Footnote | — | — | — | — | — | — | "* ECOs got listed in FY25" — footnote text unit, separate from #117 |

### 2H. Slide 13 — Industry TAM infographic (25 units: 4 markets x 3 data points = 12, GCC chart 3, bubble-bullets 3, growth-driver bullets 6, source note 1)
| # | Slide | Unit | 2023e/2023 | 2030f/2030 | CAGR | Flags |
|---|------|------|-----------|-----------|------|-------|
| 122 | 13 | Total CCR Market, INR Bn | 392.4 | 731.8 | 9.3% | UNIT = INR Bn, not Rs Mn |
| 123 | 13 | Organized CCR Market, INR Bn | 98.10 | 226.87 | 12.7% | UNIT = INR Bn |
| 124 | 13 | Total ETS Market, INR Bn | 503.5 | 1,097.6 | 11.8% | UNIT = INR Bn |
| 125 | 13 | Organized ETS Market, INR Bn | 78.04 | 197.57 | 14.2% | UNIT = INR Bn |
| 126 | 13 | GCCs (#) | 1,580 (2023) | 2,400 (2030) | — | intermediate point 1,800 (2025) also disclosed |
| 127 | 13 | Bubble-chart bullet 1: "Corporate need for reliability & accountability" | | | | |
| 128 | 13 | Bubble-chart bullet 2: "Operational efficiency & safety" | | | | |
| 129 | 13 | Bubble-chart bullet 3: "Scale & resources required" | | | | |
| 130 | 13 | Growth driver 1: "Tier II & III city expansion" | | | | |
| 131 | 13 | Growth driver 2: "Improved road networks drive ground travel" | | | | |
| 132 | 13 | Growth driver 3: "Huge expansion of GCCs in India" | | | | |
| 133 | 13 | Growth driver 4: "Increased Airport Connectivity fuels demand for chauffeur driven mobility" | | | | |
| 134 | 13 | Growth driver 5: "Business travel expected to reach pre covid level by CY2025" | | | | |
| 135 | 13 | Growth driver 6: "Formalization fuels growth" | | | | |
| 136 | 13 | GCC bullet: "Increasing employee expectations for convenient commutes" | | | | |
| 137 | 13 | Source note: "Source: F&S Report" | | | | |

(Row count for 2H = 16 rows covering 25 individual data/text units per the count-test line; market data points counted individually within rows 122-126 for the sweep total.)

### 2I. Slide 15 — "ECOS Mobility - A Snapshot" (16 units: 6 descriptive + 10 stat-grid)
| # | Slide | Unit | Value | Flags |
|---|------|------|-------|-------|
| 138 | 15 | CCR service line description | "economy to luxury cars with professionally trained chauffeurs" | |
| 139 | 15 | CCR service offerings | Corporates & Institutions, Events, B2B2C travel | |
| 140 | 15 | CCR scale & presence | 151+ cities Pan-India & 30+ countries worldwide | |
| 141 | 15 | ETS service line description | "daily home-office-home transportation... 24x7 multi shift operations" | |
| 142 | 15 | ETS service offerings | GCCs, IT & ITES, Manufacturing | |
| 143 | 15 | ETS scale & presence | 11 Major cities across India | |
| 144 | 15 | Stat: Years of experience | 30+ | |
| 145 | 15 | Stat: Fleet size | 19,500+ | "one of the largest fleet size in India" |
| 146 | 15 | Stat: Vendor owned fleet | 90%+ | asset-light framing |
| 147 | 15 | Stat: Fortune 500 companies served | 70+ | |
| 148 | 15 | Stat: BSE 500 companies served | 75+ | |
| 149 | 15 | Stat: Organizations (clients) | 1,400+ | footnoted "*as of Q1 FY27" |
| 150 | 15 | Stat: Cities | 151 | "widest PAN India presence" |
| 151 | 15 | Stat: Employees | 1,300+ | |
| 152 | 15 | Stat: Trips as on FY26 | 5.23 Mn | cumulative, distinct from quarterly 1.48 Mn trip figure |
| 153 | 15 | Stat: Partnerships (icon only, no numeric value) | (icon only) | "major credit card companies and commercial real estate players" — qualitative, ZERO_STANDING not applicable (no numeric field to be zero) |

### 2J. Slide 16 — "Journey Over the Years" timeline (14 milestones)
| # | Slide | Year | Milestone |
|---|------|------|-----------|
| 154 | 16 | 1996 | Incorporation |
| 155 | 16 | 2001 | Contract to provide transportation services at a prestigious NCR hotel |
| 156 | 16 | 2006 | Included on the panel of transporter of MEA |
| 157 | 16 | 2008 | Designed & developed exclusive software for business operations |
| 158 | 16 | 2012 | Establishment of vendor network across India |
| 159 | 16 | 2015 | Crossed Rs 1,000 Mn revenue mark for the first time |
| 160 | 16 | 2017 | Launched online booking tool & integrated APIs to digitize reservations |
| 161 | 16 | 2018 | Winner of Today's Traveler award for Best Luxury Ground Handler |
| 162 | 16 | 2019 | Expanded network outside India and "ECO driver application" |
| 163 | 16 | 2020 | Crossed Rs 4,000 Mn revenue mark for the first time |
| 164 | 16 | 2023 | Provided premium transport to G20 delegates |
| 165 | 16 | 2024 | Got listed on NSE and BSE on 4th September |
| 166 | 16 | 2025 | Reached a revenue milestone of Rs 650 Crs |
| 167 | 16 | 2026 | Reached a revenue milestone of Rs 800 Crs |

### 2K. Slide 17 — "Seasoned Management" bios (8 people)
| # | Slide | Name | Role | Background (2 bullets each) | Flags |
|---|------|------|------|------------------------------|-------|
| 168 | 17 | Rajesh Loomba | Chairman and Managing Director | Bachelor's Commerce, Delhi Univ.; 'Global Hall of Fame' 2019, World Auto Forum | no DIN disclosed in this document |
| 169 | 17 | Aditya Loomba | Joint Managing Director | PGM S.P. Jain Institute; 'Leadership Excellence Award' 2014, Brands Academy | no DIN disclosed |
| 170 | 17 | Deepali Dev | Chief Operating Officer | BA Delhi Univ.; ex-Idea Cellular, ex-Sistema Shyam TeleServices | |
| 171 | 17 | Hem Kumar Upadhyay | Chief Financial Officer | Member ICAI; ex-Carzonrent, ex-Rahul Cargo, ex-DHTC | |
| 172 | 17 | Sanjay Kumar Sharma | Chief Business Officer - ETS | Bachelor's Commerce, Chirawa College; ex-Detta Vehicle Support, ex-Deneb, ex-Pollex Tours | |
| 173 | 17 | Rini Ajeet | Head - Human Resources | PGDBA Symbiosis; ex-Bureau Veritas Global Shared Service Centre | |
| 174 | 17 | Rajnish Sharma | Senior VP - Sales | PGDBA Symbiosis; ex-Avis India Mobility Solutions, ex-Tex Corp | |
| 175 | 17 | Shweta Bhardwaj | Company Secretary & Compliance Officer | Member ICSI, law degree Chaudhary Charan Singh Univ.; ex-Vivo Mobile India | |

Note: supplement Section G flags Nidhi Seth (non-executive director, per results filing board) is not on this management slide — consistent, she is not an executive officer; not a completeness gap for this deck.

### 2L. Slide 19 — Map + city revenue-mix pie (13 units: 2 map legend + 11 cities)
| # | Slide | Unit | Value | Flags |
|---|------|------|-------|-------|
| 176 | 19 | Map legend: Cities (Own Offices) | 14 | |
| 177 | 19 | Map legend: Cities (Presence via Vendor Vehicles) | 137 | 14+137=151, ties to headline city count |
| 178 | 19 | Pie: Bangalore | 22.3% | |
| 179 | 19 | Pie: Gurgaon | 14.1% | |
| 180 | 19 | Pie: Delhi | 14.6% | |
| 181 | 19 | Pie: Mumbai | 11.2% | |
| 182 | 19 | Pie: Hyderabad | 10.6% | |
| 183 | 19 | Pie: Pune | 6.7% | |
| 184 | 19 | Pie: Chennai | 6.8% | |
| 185 | 19 | Pie: Noida | 6.8% | |
| 186 | 19 | Pie: Kolkatta | 3.1% | |
| 187 | 19 | Pie: Jaipur | 1.8% | |
| 188 | 19 | Pie: Ahmedabad | 2.0% | sum of all 11 = 100.0%, verified in extract |

### 2M. Slide 20 — Fleet composition + ownership mix (7 units: 5 categories + 2 ownership-mix data points)
| # | Slide | Unit | Content | Flags |
|---|------|------|---------|-------|
| 189 | 20 | Premium category models | Toyota Innova Hycross, Honda City, Toyota Innova Crysta, Toyota Fortuner | |
| 190 | 20 | Luxury category models | Mercedes Benz E class, BMW 5 series, Audi A6, Range Rover | |
| 191 | 20 | Economy category models | Maruti Suzuki Dzire, Maruti Suzuki Ciaz | |
| 192 | 20 | Buses & Vans category models | Mercedes V class, Toyota Commuter, Volvo | |
| 193 | 20 | Hybrid/EV category models | BYD E6, MG ZS, Tata Tigor | |
| 194 | 20 | Vehicle Ownership Mix: Owned | 5% | ties to supplement Section E, asset-light confirmed, no drift |
| 195 | 20 | Vehicle Ownership Mix: Vendor Operated | 95% | |

### 2N. Slide 21 — Business Drivers VRQSR (5 items)
| # | Slide | Driver | Description |
|---|------|--------|--------------|
| 196 | 21 | V - Variety | Comprehensive solutions, economy to luxury cars, mini vans & buses/vans |
| 197 | 21 | R - Reach | PAN India operations in 151 cities, direct presence in 30 cities |
| 198 | 21 | Q - Quality | High service quality, comprehensive technology, established brand |
| 199 | 21 | S - Safety | Professionally trained & verified chauffeurs, quality control/testing/certifications |
| 200 | 21 | R - Reliability | "Largest and most profitable chauffeur driven mobility provider to corporates in India" |

### 2O. Slide 22 — Quality & Awards infographic (17 units)
| # | Slide | Unit | Content | Flags |
|---|------|------|---------|-------|
| 201 | 22 | QC item 1 | High standards of safety & hygiene | |
| 202 | 22 | QC item 2 | Stringent specifications of customers | |
| 203 | 22 | QC item 3 | Panic Buttons | |
| 204 | 22 | QC item 4 | GPS Tracking | |
| 205 | 22 | Training quote 1 | "Manage the entire cycle of logistics and to ensure operational efficiency" | |
| 206 | 22 | Training quote 2 | "Seamless Integration across front end applications & back end systems" | |
| 207 | 22 | L&D team description | Induction, Skill Development, Behavioral Training | |
| 208 | 22 | Customer satisfaction stat | FY26 Average Rating: 4.8 | |
| 209 | 22 | Award 1 | National Tourism Award by GoI, FY14-FY17 | |
| 210 | 22 | Award 2 | Dun & Bradstreet SME Business Excellence Award, 2017 | |
| 211 | 22 | Award 3 | Today's Traveler award, Best Luxury Ground Handler, 2018 | |
| 212 | 22 | Award 4 | India's Best Employee Transportation Company, iNFHRA 2021 | |
| 213 | 22 | Award 5 | Most innovative and fastest growing transportation & car rental company, 2012 | |
| 214 | 22 | Award 6 | Best Luxury Ground Transportation Company, 2013 & 2014 | |
| 215 | 22 | Award 7 | TV9 Network Leaders of Road Transport Awards, 2022 | |
| 216 | 22 | Award 8 | Service Provider of the Year, ET Travel & Tourism, 2023 | |
| 217 | 22 | Award 9 | Luxury Car Tourist Transport Operator of the Year, SATTE Awards, 2024 | `AWARDS_COUNT_MISMATCH` — slide caption states "10 items" but the A1 extract transcribes only 9 distinct award entries; the 10th award (if present on the physical slide) is not captured in the extract. Flagged for A3/A4; not resolvable from this A1 text alone. |

### 2P. Slide 23 — Technology stack infographic (8 units)
| # | Slide | Unit | Content |
|---|------|------|---------|
| 218 | 23 | Header quote | "Seamless integrations across front end applications and back-end systems" |
| 219 | 23 | Customer Facing item 1 | Customer App |
| 220 | 23 | Customer Facing item 2 | CabDrive Pro |
| 221 | 23 | Customer Facing item 3 | Online Booking Tool |
| 222 | 23 | Internal Control item 1 | Driver App |
| 223 | 23 | Internal Control item 2 | 24x7 contact center |
| 224 | 23 | Center | RentNet - Central Transport Management System |
| 225 | 23 | APIs connect statement | Software as a Service Tools <-> Corporate Travel Tools of Clients; Outcome: High operational efficiency |

### 2Q. Slide 24 — Competitive Advantage table (5 rows)
| # | Slide | Category | ECO Mobility (self) | App-Based Aggregators |
|---|------|----------|----------------------|-------------------------|
| 226 | 24 | (segment) | B2B segment (Corporate travel demands) | Primarily B2C segment |
| 227 | 24 | RESOURCES & SERVICE LEVELS | Extensive dedicated fleets and experienced drivers | Limited dedicated fleet and drivers |
| 228 | 24 | TECHNOLOGY | Established FMS for efficient operations | Less investment in fleet management systems |
| 229 | 24 | SERVICE DIFFERENTIATION | Consistent and reliable service tailored to corporate needs | Inconsistent service experience |
| 230 | 24 | DRIVER PROFESSIONALISM | Professional and well-trained drivers | Concerns regarding driver professionalism & conduct |

### 2R. Slide 25 — Long-standing-customer chart (12 data points: 6 years x 2 series)
| # | Slide | FY | Revenue from customers >5yr (Rs Mn) | As % of total revenue | Flags |
|---|------|----|--------------------------------------|-------------------------|-------|
| 231 | 25 | FY21 | 355 | 34% | |
| 232 | 25 | FY22 | 561 | 38% | |
| 233 | 25 | FY23 | 2,313 | 55% | |
| 234 | 25 | FY24 | 3,168 | 57% | |
| 235 | 25 | FY25 | 3,806 | 61% | peak stickiness ratio |
| 236 | 25 | FY26 | 4,266 | 55% | highlighted/boxed on slide as latest year |
| 237 | 25 | (note) | — | — | Q1FY27 press-release figure of 51% (Part 1F row 40) is a further step down from FY26's 55%; deck chart itself stops at FY26 — the Q1FY27 51% figure is press-release-only, not on this chart, cf. supplement Section E |

### 2S. Slide 27 — "Way Ahead" outlook items (6 items)
| # | Slide | Item |
|---|------|------|
| 238 | 27 | Increasing wallet share from existing customers |
| 239 | 27 | Acquisition of new customers: expanding skilled sales team |
| 240 | 27 | Expanding presence in Tier-II and Tier-III cities and new geographies |
| 241 | 27 | Focus on brand building strategies |
| 242 | 27 | Strengthen technology and talent pool for scale and operational excellence |
| 243 | 27 | Expanding services in existing networks |

Note (supplement Section F): no quantified guidance anywhere in the deck; no restatement of any prior EBITDA/PAT margin band; no FY28 revenue target mentioned. `NO_QUANTIFIED_GUIDANCE` flag applies to the "Way Ahead" slide as a whole.

### 2T. Slide 28 — Closing/contacts slide (2 units)
| # | Slide | Unit |
|---|------|------|
| 244 | 28 | ECOS contact: Ms. Shweta Bhardwaj, Company Secretary & Compliance Officer, legal@ecosmobility.com |
| 245 | 28 | Adfactors PR contact: Hashika Mutreja / Kashmira Parkar |

### 2U. Slides 2, 3, 4 — front matter (already counted in slide inventory 2A; disclaimer paragraphs itemised for completeness)
| # | Slide | Unit |
|---|------|------|
| 246 | 3 | Disclaimer para 1: no representation/warranty as to accuracy/completeness |
| 247 | 3 | Disclaimer para 2: presentation current as of its date; company may alter without notice; forward-looking statements caveat |
| 248 | 3 | Disclaimer para 3: based on publicly available information incl. website and Annual Reports |
| 249 | 3 | Disclaimer para 4: general information purposes only |
| 250 | 3 | Disclaimer para 5: investment risk / loss of principal warning |
| 251 | 3 | Disclaimer para 6: not an offer or invitation to purchase/subscribe for shares |
| 252 | 4 | TOC item 01: Q1 FY27 Result Highlights |
| 253 | 4 | TOC item 02: Historical Financials |
| 254 | 4 | TOC item 03: Industry Overview |
| 255 | 4 | TOC item 04: Company Overview |
| 256 | 4 | TOC item 05: Business Overview |
| 257 | 4 | TOC item 06: Outlook |

**Presentation ledger row count: 210 discrete data/content units across 28 slides (rows 48-257).**

---
## PART 3 — DROPPED_SLIDE / PRIOR-QUARTER COMPARISON
No prior-quarter deck ledger exists in `runs/` for ECOSMOBILITY (only the current-quarter results-filing ledger, `ledger_results_ecosmobility_q1fy27.md`, was found; no prior investor-presentation or press-release ledger). `DROPPED_SLIDE` comparison is therefore **not applicable this run** — noted as a gap for the next quarterly cycle to establish baseline, not a flag against this quarter's disclosure.

---
## PART 4 — FLAGS SUMMARY
| Flag | Count | Locations |
|------|-------|-----------|
| `ZERO_STANDING` | 5 | PR none; Deck: Purchase of Stock (row 61), Change in stock-in-trade (row 62), Intangible assets (row 76), Non-controlling interest (row 99), Borrowings non-current (row 100) |
| `SUPPLEMENT_DISAGREEMENT` | 3 | PR row 26 vs deck row 65 (EBITDA Q1FY26); PR row 29 vs deck row 72 (PAT margin Q4FY26); deck row 59 vs PR row 24 (Total income YoY% 16.92 vs 16.91, minor) |
| `DUPLICATE_ACROSS_DOCS` | 1 (11 sub-claims) | CMD quote, PR rows 13-23 = deck row 48 |
| `NUMBER_DISCREPANCY` | 1 | Deck balance sheet FY25 column, Total assets vs Total equity+liabilities (row 113) |
| `GROWTH_LABEL_INCONSISTENCY` | 1 | Deck slide 8 PAT growth label 10.28% (row 56) vs 9.50%/9.77% elsewhere |
| `AWARDS_COUNT_MISMATCH` | 1 | Deck slide 22, caption says 10 items, 9 transcribed (row 217) |
| `NO_QUANTIFIED_GUIDANCE` | 1 | Deck slide 27 "Way Ahead" (row 238-243) |

---
## PART 5 — CATEGORY TOTALS (for YAML counts block)
- Press release units: 47
- Presentation units: 210
- Combined ledger rows: 257
- Slides: 28 (28 of 28 accounted)
- Zero-standing flagged: 5
- Flags raised (distinct types): 7 (ZERO_STANDING, SUPPLEMENT_DISAGREEMENT, DUPLICATE_ACROSS_DOCS, NUMBER_DISCREPANCY, GROWTH_LABEL_INCONSISTENCY, AWARDS_COUNT_MISMATCH, NO_QUANTIFIED_GUIDANCE)

```yaml
stage: A2-enumerator
company: "ECOSMOBILITY"
quarter: "Q1FY27"
doctype: "presentation"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/ecosmobility-q1fy27/work/ledger_newdocs_ecosmobility_q1fy27.md"
counts:
  notes: 0
  line_items: 56
  zero_standing: 5
  agenda_items: 0
  auditor_paras: 0
  entities: 0
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 28
  slide_numbers: 28
flags_raised: [ZERO_STANDING, SUPPLEMENT_DISAGREEMENT, DUPLICATE_ACROSS_DOCS, NUMBER_DISCREPANCY, GROWTH_LABEL_INCONSISTENCY, AWARDS_COUNT_MISMATCH, NO_QUANTIFIED_GUIDANCE]
gate_a2: pass
mismatch_note: ""
```
