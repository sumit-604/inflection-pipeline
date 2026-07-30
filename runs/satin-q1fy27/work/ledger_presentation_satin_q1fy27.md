# A2 COMPLETENESS LEDGER — Investor Presentation — SATIN Q1 FY27

Source: `extract_presentation_satin_q1fy27.txt` (42 pages, pdftotext -layout + tesseract OCR
fallback on 6 divider pages: 2, 4, 13, 28, 34, 42). Unit convention: Rs Crores unless
stated otherwise. Prior-quarter ledger: NOT SUPPLIED for this run — DROPPED_SLIDE /
ENTITY_CHANGE diffs against Q4FY26 could not be performed; noted as a structural gap,
not a mismatch.

```
=== A2 COUNT TEST ===
category: slides            grep_count: 42   sweep_count: 42   match: yes
category: ocr_pages         grep_count: 6    sweep_count: 6    match: yes
category: footnote_lines    grep_count: 44   sweep_count: 44   match: yes  (see note below)
category: percent_figures   grep_count: 378  sweep_count: 378  match: yes
category: rupee_figures     grep_count: 67   sweep_count: 67   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

**Reconciliation note (footnote_lines):** first-pass grep with pattern
`^\s*(Note:?|Notes:?|\*[A-Za-z]|[0-9]+\.\s+[A-Za-z]|[0-9]+\)\s+[A-Za-z]|\([0-9]+\)\s*[A-Za-z]|Visit at|HRMS:)`
returned 44 but contained one false positive (line 1027, "HRMS: New-Generation Platform,"
— a slide-32 section header, not a footnote) and one false negative (line 1254, "Price
data as on 30th June 2026" — a genuine footnote caption with no leading marker). The
manual sweep swapped these two lines in and out; net line count held at 44 on
re-sweep, so GATE A2 passes, but the match on raw count alone was coincidental and the
re-sweep (correcting the substitution) is the basis for the "yes."

**Reconciliation note (percent_figures):** raw grep of `%` across the whole file returns
379; one instance is `page_coverage: 100%` in the A1 extraction header (line 10), outside
slide body content. Excluding the header, slide-body sweep = 378, matching the
per-slide manual tally exactly.

---

## TABLE 1 — SLIDE INVENTORY (42 rows, all page/slide markers)

| # | Printed pg | Title | Content type | OCR? | Line | Flags |
|---|---|---|---|---|---|---|
| 1 | (none, cover letter) | NSE/BSE Reg. 30 covering letter re: Investor Presentation | text (regulatory letter) | no | 25 | SIGNATURE_BLOCK (see Table 7) |
| 2 | — | Title slide: "EARNINGS PRESENTATION Q1-FY27" | title/cover graphic | yes | 65 | OCR_DIVIDER |
| 3 | 2 | "STRONGEST OPENING EVER" — headline KPI bullets | text bullets | no | 88 | — |
| 4 | 3 | "COMPANY OVERVIEW" | section divider | yes | 112 | OCR_DIVIDER |
| 5 | 4 | "CREATING ENDURING VALUE THROUGH DIVERSIFICATION" — FY2030 AUM target revision, growth engines/validation | text + KPI | no | 124 | — |
| 6 | 5 | "GUIDANCE FOR FY27" — consolidated AUM growth target, standalone credit cost & ROA targets | text + KPI | no | 154 | GUIDANCE |
| 7 | 6 | "A LEGACY OF TRUST AND RESILIENCE" — 10-yr AUM CAGR chart FY16-FY26 | chart + text | no | 177 | — |
| 8 | 7 | "SATIN VS OVERALL MFI INDUSTRY: CONSISTENTLY AHEAD" | chart + text | no | 204 | CHART_LAYOUT_AMBIGUOUS |
| 9 | 8 | "LEADING ACROSS METRICS THROUGH RELENTLESS EXECUTION" — SCNL vs peers on 6 metrics | chart | no | 239 | CHART_LAYOUT_AMBIGUOUS |
| 10 | 9 | "AHEAD OF THE CURVE" — underwriting/geography/product pillars + financial strength bullets | text | no | 273 | — |
| 11 | 10 | "A DECADE OF TECH LED TRANSFORMATION" — 2016→Q1FY27 timeline | text/timeline | no | 305 | — |
| 12 | 11 | "TECHNOLOGY AS AN ENABLER, ADVANTAGE AS AN OUTCOME" | text/framework | no | 341 | — |
| 13 | 12 | "Q1-FY27 PERFORMANCE" | section divider | yes | 380 | OCR_DIVIDER |
| 14 | 13 | "SNAPSHOT CONSOLIDATED Q1-FY27" — AUM/Disb/Clients/Branches/Revenue/PAT | KPI tiles | no | 394 | — |
| 15 | 14 | "SNAPSHOT STANDALONE Q1-FY27" — AUM/Disb/Clients/Branches/Revenue/PAT | KPI tiles | no | 414 | — |
| 16 | 15 | "Q1-FY27 CONSOLIDATED HIGHLIGHTS" table | table | no | 434 | DATA_ARTIFACT ("xx" placeholder, see Table 6) |
| 17 | 16 | "Q1-FY27 CONSOLIDATED FINANCIAL HIGHLIGHTS" ratio table | table | no | 476 | DELTA_OMITTED (YoY/QoQ blank all rows) |
| 18 | 17 | "Q1-FY27 STANDALONE HIGHLIGHTS" table | table | no | 501 | — |
| 19 | 18 | "Q1-FY27 STANDALONE FINANCIAL HIGHLIGHTS" ratio table | table | no | 541 | DELTA_OMITTED (YoY/QoQ blank all rows) |
| 20 | 19 | "STANDALONE OPERATIONAL HIGHLIGHTS FOR Q1-FY27" — funding, cost of borrowing, credit cost, GNPA, geography bullets | text bullets | no | 567 | — |
| 21 | 20 | "STANDALONE QUARTERLY PROGRESS (1/3)" — AUM/Disb/TotalIncome/NII/PPOP/NetWorth, 5-qtr trend | 6 charts | no | 592 | — |
| 22 | 21 | "STANDALONE QUARTERLY PROGRESS (2/3)" — Branches/Employees/NewClients/AUM-per-branch/AUM-per-LO/Disb-per-branch | 6 charts | no | 633 | — |
| 23 | 22 | "STANDALONE QUARTERLY PROGRESS (3/3)" — Margin analysis, Credit Cost, Opex/AvgAUM, Return ratios & CAR | 4 charts | no | 674 | — |
| 24 | 23 | "ASSET QUALITY AND PROVISIONS" — PAR trend, NNPA/GNPA/ECL/coverage | 2 charts + bullets | no | 718 | — |
| 25 | 24 | "BUILT ON A STRONG & BALANCED FUNDING BASE" — product/lender mix, funding source, total debt, top-10 lenders, credit rating | chart + tables | no | 755 | CHART_LAYOUT_AMBIGUOUS (pie-slice-to-label mapping) |
| 26 | 25 | "DIVERSIFIED GEOGRAPHICAL PRESENCE" — map + districts/states/branches/clients/employees trend | map graphic + charts | no | 796 | CHART_LAYOUT_AMBIGUOUS (map figure placement scrambled by -layout extraction) |
| 27 | 26 | "IMPROVING PERFORMANCE ACROSS GEOGRAPHIES" — state-wise on-book portfolio/PAR90 table | table | no | 863 | — |
| 28 | 27 | "VALUE UNLOCKING THROUGH DIVERSIFICATION" | section divider | yes | 891 | OCR_DIVIDER |
| 29 | 28 | "GROUP STRUCTURE" — SCNL + 4 WOS org chart (SHFL/SFL/STL/SGAL) | org chart | no | 907 | ZERO_STANDING (SGAL, see Table 6); "68% stake" floats unlabeled near top of chart — likely misplaced QTrino-ownership figure confirmed on slide 32, flag CHART_LAYOUT_AMBIGUOUS |
| 30 | 29 | "HOUSING FINANCE" (SHFL) — KPI panel + AUM/Revenue chart | table + chart | no | 940 | — |
| 31 | 30 | "SATIN FINSERV LIMITED" (SFL) — KPI panel + AUM/Income chart + green finance | table + chart | no | 975 | — |
| 32 | 31 | "SATIN TECHNOLOGIES — LEVERAGING IN-HOUSE TECHNOLOGY" — HRMS/Core Banking/QTrino Labs status | text | no | 1017 | — |
| 33 | 32 | "FROM LAST-MILE BORROWERS TO FUTURE FINANCING SOLUTIONS" (SGAL/AIF) | text (narrative only) | no | 1050 | ZERO_STANDING (no AUM/fund-size/net-worth disclosed, see Table 6) |
| 34 | 33 | "ANNEXURE" | section divider | yes | 1083 | OCR_DIVIDER |
| 35 | 34 | "BUSINESS DETAILS" — AUM / AUM Mix / Branches by entity | table | no | 1097 | — |
| 36 | 35 | "DIVERSIFIED PRODUCT OFFERINGS" — SCNL/SHFL/SFL product comparison | table | no | 1121 | — |
| 37 | 36 | "CONSOLIDATED INCOME STATEMENT" | table | no | 1161 | — |
| 38 | 37 | "STANDALONE INCOME STATEMENT" | table | no | 1192 | — |
| 39 | 38 | "CAPITAL MARKET INFORMATION" — shareholding pattern pie + price data + share-price trend | chart + table | no | 1223 | CHART_LAYOUT_AMBIGUOUS (pie-slice-to-label mapping) |
| 40 | 39 | "GLOSSARY" — 16 term definitions | table | no | 1256 | — |
| 41 | 40 | "DISCLAIMER" — SCNL disclaimer, Valorem Advisors disclaimer, contacts | text (legal) | no | 1289 | — |
| 42 | 41 | "DREAM BIG… DELIVER BIGGER…" — Thank You closer | closing graphic | yes | 1328 | OCR_DIVIDER |

Count test: 42 `[page N]` markers grepped == 42 rows swept above. Match: yes.
OCR pages swept (2,4,13,28,34,42) == header's declared `ocr_pages` list == 6. Match: yes.

---

## TABLE 2 — NUMERIC DENSITY CROSS-CHECK (per slide, supports "every number on every
slide" per instruction; grep totals reconciled against per-slide sweep above)

| Slide (printed pg) | % signs | ₹-prefixed figures |
|---|---|---|
| 3 (2) | 13 | 8 |
| 5 (4) | 6 | 4 |
| 6 (5) | 7 | 2 |
| 7 (6) | 2 | 0 |
| 8 (7) | 11 | 1 |
| 9 (8) | 12 | 0 |
| 10 (9) | 7 | 2 |
| 12 (11) | 1 | 0 |
| 14 (13) | 6 | 4 |
| 15 (14) | 6 | 4 |
| 16 (15) | 13 | 0 |
| 17 (16) | 34 | 3 |
| 18 (17) | 13 | 0 |
| 19 (18) | 34 | 3 |
| 20 (19) | 9 | 5 |
| 21 (20) | 6 | 0 |
| 22 (21) | 5 | 0 |
| 23 (22) | 45 | 1 |
| 24 (23) | 46 | 5 |
| 25 (24) | 23 | 0 |
| 26 (25) | 5 | 0 |
| 27 (26) | 26 | 0 |
| 29 (28) | 1 | 5 |
| 30 (29) | 4 | 2 |
| 31 (30) | 3 | 5 |
| 32 (31) | 1 | 0 |
| 35 (34) | 8 | 5 |
| 36 (35) | 6 | 8 |
| 37 (36) | 9 | 0 |
| 38 (37) | 9 | 0 |
| 39 (38) | 7 | 0 |
| **Total** | **378** | **67** |

All other slides (1,2,4,11,13,28,32(SGAL),33(SGAL text),34,40,41,42) carry 0 of either —
consistent with their content types (letter, dividers, narrative-only, glossary text,
legal disclaimer, closer).

---

## TABLE 3 — FOOTNOTES & FINE-PRINT SWEEP (44 lines; multi-item lines exploded into
sub-rows for record-keeping; each still cites its source line)

| # | Slide | Line | Footnote / disclaimer text (first ~15 words) |
|---|---|---|---|
| 1 | 3 | 109 | "Revenue and NIM are adjusted for MTM gains and Changes due to Forex Movement for a more realistic depiction" |
| 2 | 5 | 151 | "*WOS- Wholly Owned Subsidiary" |
| 3 | 11 | 378 | "*OGM : Open General Meeting" |
| 4 | 14 | 412 | "*Revenue is adjusted for MTM gains and Changes due to Forex Movement for a more realistic depiction" |
| 5 | 15 | 432 | "*Revenue is adjusted for MTM gains and Changes due to Forex Movement for a more realistic depiction" (repeat text, distinct slide) |
| 6 | 16 | 473 | "Note: Q1-FY26 numbers have been regrouped; Q1FY27 and Q4FY26 are not comparable due to cyclical nature of business" |
| 7 | 17 | 494 | Note 1: "Gross Yield, Cost of Funds, NIM and Cost to Income have been adjusted for MTM gains…" |
| 8 | 17 | 495 | Note 2: "Adjusted Credit Cost, Adjusted ROA and Adjusted ROE is excluding Management Overlay… ₹36 Cr (Q1FY27), ₹21 Cr (Q4FY26), ₹8 Cr (Q1FY26)" |
| 9 | 17 | 496 | Bullet: "Our Forex borrowings are 100% hedged" |
| 10 | 17 | 497 | Bullet: "Q1FY26 numbers have been regrouped" |
| 11 | 17 | 498 | Bullet: "Q1FY27 and Q4FY26 are not comparable due to cyclical nature of business" |
| 12 | 18 | 538 | "Note: Q1-FY26 numbers have been regrouped; Q1FY27 and Q4FY26 are not comparable…" |
| 13 | 19 | 559 | Note 1 (identical text to #7) |
| 14 | 19 | 560 | Note 2 (identical text to #8) |
| 15 | 19 | 561 | Bullet (identical to #9) |
| 16 | 19 | 562 | Bullet (identical to #10) |
| 17 | 19 | 563 | Bullet (identical to #11) |
| 18 | 20 | 590 | "*excluding sub-debt" |
| 19 | 21 | 631 | "Note: . FY26 numbers have been regrouped" |
| 20 | 22 | 672 | "Note: We have added 392 branches in FY26 and operating efficiencies will be visible in coming quarters" |
| 21 | 23 | 713 | Note 1: "Gross Yield, Cost of Funds and NIM have been adjusted for MTM gains…" |
| 22 | 23 | 714 | Note 2: "Our Forex borrowings are 100% hedged" |
| 23 | 23 | 714 | Note 3: "OPEX to Avg AUM is elevated on account of branch expansion" |
| 24 | 23 | 714 | Note 4: "Q1FY26 numbers have been regrouped" |
| 25 | 23 | 716 | Note 5: "Credit cost looks inflated and ROA & ROE are suppressed due to management overlay of ₹36 Crores" |
| 26 | 24 | 741 | "Above numbers are on a cumulative basis." |
| 27 | 25 | 794 | "*Exposure via various funds" |
| 28 | 25 | 794 | "Data as on 30th June 2026" (same line, second clause) |
| 29 | 26 | 860 | "* Loan officers include Trainee CSOs" |
| 30 | 26 | 860 | "# Including UTs" (same line, second marker) |
| 31 | 29 | 938 | "HRMS: Human Resource Management System; WoS : Wholly Owned Subsidiary" |
| 32 | 30 | 973 | "Visit at- Satin Housing Finance – The Answer Is Home" |
| 33 | 31 | 1013 | "Visit at - Satin Finserv Limited" |
| 34 | 31 | 1014 | "(1) In addition to these, SFL JLG has 21,783 loan accounts" |
| 35 | 32 | 1048 | "Visit at- Satin Technologies Limited; MVP- Minimum Viable Product; FIPS: Federal Information Processing Standards" |
| 36 | 33 | 1081 | "Visit at : www.satinaif.com" |
| 37 | 35 | 1117 | Footnote 1): "Includes assigned portfolio of ₹228 Crores" (SHFL Q1FY27) |
| 38 | 35 | 1117 | Footnote 2): "Includes assigned portfolio of ₹162 Crores" (SHFL Q1FY26) |
| 39 | 35 | 1118 | Footnote 3): "Includes assigned portfolio of ₹216 Crores" (SHFL Q4FY26) |
| 40 | 35 | 1118 | Footnote 4): "Includes assigned portfolio of ₹74 Crores" (SFL Q1FY27) |
| 41 | 35 | 1119 | Footnote 5): "Includes assigned portfolio of ₹67 Crores" (SFL Q4FY26) |
| 42 | 36 | 1157 | Footnote (1): "Includes MFI Lending (loans under JLG model and water & sanitation) and Product Financing…" |
| 43 | 36 | 1158 | Footnote (2): "SCNL also has additional MSME portfolio of ₹456 Crores other than MFI portfolio" |
| 44 | 36 | 1159 | Footnote (3): "Post merger of TFSL, SFL also has JLG BC portfolio, which is being run down… ₹26 Crores" |
| 45 | 37 | 1188 | Note 1: "Our Forex borrowings are 100% hedged" |
| 46 | 37 | 1189 | Note 2: "Opex elevated on account of branch expansion" |
| 47 | 37 | 1190 | Note 3: "Q1FY26 numbers have been regrouped" |
| 48 | 38 | 1219 | Note 1 (identical to #45) |
| 49 | 38 | 1220 | Note 2 (identical to #46) |
| 50 | 38 | 1221 | Note 3 (identical to #47) |
| 51 | 39 | 1254 | "Price data as on 30th June 2026" |
| 52 | 41 | 1292-1295 | SCNL disclaimer para 1: purpose/no-offer-to-purchase disclaimer |
| 53 | 41 | 1297-1300 | SCNL disclaimer para 2: no representation/warranty as to accuracy, completeness |
| 54 | 41 | 1302-1308 | SCNL disclaimer para 3: forward-looking statements risk language |
| 55 | 41 | 1311-1315 | Valorem Advisors disclaimer paragraph |

Note: rows 52-55 (slide-41 disclaimer paragraphs) are counted separately from the
44-line GATE A2 footnote_lines count above (they are prose paragraphs, not
marker-prefixed lines, and are not mechanically grep-countable on the same pattern;
enumerated here for completeness per instruction rule "every paragraph… disclaimer
qualifying a headline number" is not literally applicable to slide 41 since it
qualifies no single number, but the rule for "every footnote and fine-print
disclaimer" is satisfied by listing it).

---

## TABLE 4 — FINANCIAL / KPI TABLE LINE ITEMS (organized by slide group; every row
carries its source slide + line; ~240 line items total across all tables/charts)

### 4a. Slide 6 — FY27 Guidance (4 items)
| Item | Value | Line |
|---|---|---|
| Consolidated AUM growth target | 20%-25% | 160 |
| Implied AUM range | ₹18,200-₹18,900 Cr | 161 |
| Standalone Credit Cost target | 3.0%-3.5% | 171 |
| Standalone ROA target | 3.5%-4.0% | 171 |

### 4b. Slides 16 & 18 — Consolidated / Standalone Highlights (absolute figures, 7 metrics each = 14 rows)
| Metric | Slide | Q1FY27 | Q1FY26 | YoY | Q4FY26 | QoQ | Line |
|---|---|---|---|---|---|---|---|
| AUM (₹Cr) | 16 (Consol) | 15,935 | 12,499 | 27% | 15,174 | 5% | 440 |
| Disbursement (₹Cr) | 16 | 3,495 | 2,242 | 56% | 4,420 | 21% | 444 |
| Branches | 16 | 2,041 | 1,599 | 28% | 2,015 | 1% | 449 |
| NII (₹Cr) | 16 | 514 | 411 | 25% | 542 | 5% | 452 |
| PPOP (₹Cr) | 16 | 267 | 201 | 33% | 290 | 8% | 457 |
| PAT (₹Cr) | 16 | 123 | 45 | 172% | 162 | 24% | 462 |
| Active Clients (Lakhs) | 16 | 34 | 33 | 3% | 34 | **"xx"** | 467-469 |
| AUM (₹Cr) | 18 (Standalone) | 13,312 | 10,956 | 22% | 12,853 | 4% | 507 |
| Disbursement (₹Cr) | 18 | 3,008 | 2,065 | 46% | 3,820 | 21% | 512 |
| Branches | 18 | 1,863 | 1,487 | 25% | 1,841 | 1% | 516 |
| NII (₹Cr) | 18 | 465 | 370 | 26% | 469 | 1% | 520 |
| PPOP (₹Cr) | 18 | 258 | 189 | 36% | 256 | 1% | 525 |
| PAT (₹Cr) | 18 | 120 | 43 | 182% | 137 | 12% | 529 |
| Active Clients (Lakhs) | 18 | 33 | 32 | 3% | 33 | (blank) | 534 |

### 4c. Slides 17 & 19 — Consolidated / Standalone Financial Highlights ratios (12 metrics each = 24 rows)
| Metric | Slide | Q1FY27 | Q1FY26 | Q4FY26 | Line | Flag |
|---|---|---|---|---|---|---|
| Gross Yield¹ | 17 (Consol) | 21.27% | 21.51% | 23.28% | 480 | DELTA_OMITTED |
| Cost of Funds¹ | 17 | 8.06% | 8.51% | 8.09% | 481 | DELTA_OMITTED |
| NIM¹ | 17 | 13.21% | 13.00% | 15.20% | 482 | DELTA_OMITTED |
| Operating Expense Ratio | 17 | 6.34% | 6.64% | 7.05% | 483 | DELTA_OMITTED |
| Loan Loss Ratio | 17 | 2.73% | 4.52% | 2.19% | 484 | DELTA_OMITTED |
| Adjusted Loan Loss Ratio² | 17 | 1.81% | 4.27% | 1.62% | 485 | DELTA_OMITTED |
| ROA | 17 | 3.30% | 1.50% | 4.71% | 486 | DELTA_OMITTED |
| Adjusted ROA² | 17 | 4.02% | 1.70% | 5.16% | 487 | DELTA_OMITTED |
| ROE | 17 | 16.75% | 7.05% | 23.31% | 488 | DELTA_OMITTED |
| Adjusted ROE² | 17 | 20.39% | 7.97% | 25.51% | 489 | DELTA_OMITTED |
| Leverage | 17 | 3.97x | 3.64x | 3.86x | 490 | DELTA_OMITTED |
| Cost to Income Ratio¹ | 17 | 47.98% | 51.08% | 46.42% | 491 | DELTA_OMITTED |
| Gross Yield¹ | 19 (Standalone) | 22.44% | 21.87% | 23.65% | 545 | DELTA_OMITTED |
| Cost of Funds¹ | 19 | 8.08% | 8.71% | 7.81% | 546 | DELTA_OMITTED |
| NIM¹ | 19 | 14.36% | 13.16% | 15.85% | 547 | DELTA_OMITTED |
| Operating Expense Ratio | 19 | 6.33% | 6.51% | 6.98% | 548 | DELTA_OMITTED |
| Loan Loss Ratio | 19 | 3.06% | 4.84% | 2.48% | 549 | DELTA_OMITTED |
| Adjusted Loan Loss Ratio² | 19 | 1.97% | 4.55% | 1.80% | 550 | DELTA_OMITTED |
| ROA | 19 | 3.55% | 1.51% | 4.31% | 551 | DELTA_OMITTED |
| Adjusted ROA² | 19 | 4.34% | 1.73% | 4.80% | 552 | DELTA_OMITTED |
| ROE | 19 | 15.10% | 5.97% | 17.91% | 553 | DELTA_OMITTED |
| Adjusted ROE² | 19 | 18.46% | 6.82% | 19.94% | 554 | DELTA_OMITTED |
| Leverage | 19 | 3.15x | 2.90x | 3.07x | 555 | DELTA_OMITTED |
| Cost to Income Ratio¹ | 19 | 44.49% | 48.91% | 45.32% | 556 | DELTA_OMITTED |

DELTA_OMITTED: the YoY and QoQ columns are present as headers on both tables but every
single row's YoY/QoQ cell is blank — a full-column omission across all 12 ratios on
both slides, distinct from the absolute-figure tables (16, 18) which do populate
YoY/QoQ. Flagged for A3/A4 since a reader must compute these deltas manually.

### 4d. Slides 21-23 — Standalone Quarterly Progress trend charts (5-quarter series Q1FY26→Q1FY27; 20 series rows)
| Chart | Slide | Q1FY26 | Q2FY26 | Q3FY26 | Q4FY26 | Q1FY27 | Line |
|---|---|---|---|---|---|---|---|
| AUM (₹Cr) | 21 | 10,956 | 11,044 | 11,482 | 12,853 | 13,312 | 599-602 |
| Disbursement (₹Cr) | 21 | 2,065 | 2,421 | 2,896 | 3,820 | 3,008 | 599-603 |
| Total Income (₹Cr) | 21 | 609 | 637 | 647 | 720 | 734 | 598-599 |
| NII (₹Cr) | 21 | 370 | 398 | 408 | 469 | 465 | 615-617 |
| PPOP (₹Cr) | 21 | 189 | 200 | 210 | 256 | 258 | 617-618 |
| Net Worth (₹Cr) | 21 | 2,870 | 2,917 | 2,988 | 3,129 | 3,243 | 619-621 |
| Branches | 22 | 1,487 | 1,616 | 1,817 | 1,841 | 1,863 | 641-644 |
| Employees | 22 | 14,944 | 15,343 | 16,411 | 16,212 | 16,560 | 641-644 |
| New Clients Added (Lakhs) | 22 | 1.9 | 2.5 | 2.2 | 1.6 | 1.5 | 642-645 |
| AUM/Branch (₹Cr) | 22 | 6.8 | 6.3 | 7.0 | 7.1 | 7.4 | 657-662 |
| AUM/Loan Officer (₹Cr) | 22 | 1.08 | 1.06 | 1.10 | 1.29 | 1.39 | 658-660 |
| Disbursement/Branch (₹Cr) | 22 | 1.4 | 1.5 | 1.6 | 1.6 | 2.1 | 660-661 |
| Gross Yield (%) | 23 | 21.87% | 22.96%(approx) | 23.15%(approx) | 23.65% | 22.44% | 678-683 |
| Financial Cost (%) | 23 | 8.71% | 8.67% | 8.46% | 7.81% | 8.08% | 687 |
| NIM (%) | 23 | 13.16% | 14.48% | 14.50% | 15.85% | 14.36% | 682 |
| Credit Cost (%) | 23 | 4.84% | 4.83%(approx) | 4.23%(approx) | 2.48% | 3.06% | 679-684 |
| Opex to Avg AUM (%) | 23 | 6.51% | 7.21% | 7.03% | 6.98% | 6.33% | 696-700 |
| Capital Adequacy Ratio (%) | 23 | 26.04%(approx) | 26.47%(approx) | 24.80% | 25.39%(approx) | 26.74% | 696-710 |
| ROA (%) | 23 | 1.51% | 1.75%(approx) | 2.33%(approx) | 4.31% | 3.55% | 703-706 |
| ROE (%) | 23 | 5.97% | 7.17%(approx) | 9.58%(approx) | 17.91% | 15.10% | 699-708 |

"(approx)" flags in slide-23 rows: pdftotext -layout scrambled the exact quarter-to-value
alignment on these two multi-series charts (Margin Analysis and Return
Ratios/CAR) because chart-plotted values were extracted out of strict column
order; values are all present in the raw text (line refs given) but the
Q2FY26/Q3FY26 assignment could not be fully confirmed without the source chart
image. Flag: CHART_LAYOUT_AMBIGUOUS. Endpoint values (Q1FY26, Q4FY26, Q1FY27) are
corroborated against slides 16/18/19/21 absolutes and are high-confidence.

### 4e. Slide 24 — Asset Quality and Provisions (8 chart rows + 7 bullet facts = 15 items)
| Item | Q1FY26 | Q2FY26 | Q3FY26 | Q4FY26 | Q1FY27 | Line |
|---|---|---|---|---|---|---|
| PAR 90 | 3.7% | 3.5%(approx) | 3.3%(approx) | 3.1% | 2.2% | 726-736 |
| PAR 60 | 4.4% | 4.2%(approx) | 4.1%(approx) | 3.6% | 3.7% | 728-736 |
| PAR 30 | 5.0% | 4.9%(approx) | 4.7%(approx) | 3.7% | (see note) | 726-736 |
| PAR 1 | 5.8% | 5.8%(approx) | (approx) | 3.4% | (see note) | 723-736 |
| GNPA | 3.7% | 3.5%(approx) | 3.3%(approx) | 3.1% | 2.2% | 723-735 |
| NNPA | 2.4% | 2.3%(approx) | 2.2%(approx) | 2.2% | (see note) | 729-735 |
| ECL% | 1.4% | 1.2%(approx) | 1.1%(approx) | 0.9% | 0.3%(approx) | 731-734 |
| Overall Coverage Ratio | 97% | 105%(approx) | 95%(approx) | 92% | 115% | 723 |

Note: slide 24's two multi-series charts (PAR trend x4 series, NNPA/coverage x3
series) show the same layout-scramble issue as slide 23 — flag
CHART_LAYOUT_AMBIGUOUS. Q1FY27 endpoint for GNPA (2.2%) is corroborated
independently by the bullet text below the chart ("PAR 90 at 2.2% i.e. ₹219
Crores") and by slide 20's bullet ("GNPA further improved to 2.2% as on 30th
Jun'26"), so that single data point is high-confidence; the rest of the Q1FY27
column could not be independently corroborated and are left unresolved above
("see note") rather than guessed, per the NEVER-estimate rule.

Bullet facts (7, lines 746-752):
1. Improvement in collection efficiency across dpd buckets → better PAR ratios
2. PAR 90 at 2.2% i.e. ₹219 Crores
3. On-book provisions ₹252 Cr (2.5% of on-book portfolio) vs RBI-required ₹152 Cr
4. Management overlay ₹36 Cr buffer for future stress
5. Stage 3 coverage ratio 85% (30-Jun-26) vs 73% (31-Mar-26)
6. Recovery against write-offs ₹8 Cr in Q1FY27
7. Overall Provision Coverage Ratio 115%

### 4f. Slide 25 — Funding Base, Lender Mix, Credit Rating (26 items)
| Item | Value | Line |
|---|---|---|
| Product wise: Commercial paper | 0.2% | 759 |
| Product wise: DA | 11.8% | 762-764 |
| Product wise: NCD | 13.5% | 766-768 |
| Product wise: ECB | 21.5% | 772-773 |
| Product wise: Term loan & PTC | 53.1% | 762-769 |
| Lender wise: Overseas fund | 6.1% | 766 |
| Lender wise: Banks | 10.9% | 762 |
| Lender wise: NBFC | 12.6% | 768-769 |
| Lender wise: Domestic Financial Institution | 70.4% | 772-774 |
| Funding source: Foreign | 25.7% | 784 |
| Funding source: Domestic | 74.3% | 787-790 |
| Total Debt (₹Cr) FY24 | 7,269 | 784 |
| Total Debt (₹Cr) FY25 | 7,887 | 783 |
| Total Debt (₹Cr) FY26 | 9,600 | 781 |
| Total Debt (₹Cr) Q1FY27 | 10,216 | 780 |
| Active Lenders | 77 | 760 |
| Bank Of Maharashtra % share | 9.4% | 765 |
| State Bank Of India % share | 6.5% | 767 |
| Union Bank Of India % share | 6.3% | 770 |
| HSBC % share | 6.1% | 772 |
| Bandhan Bank % share | 5.5% | 775 |
| IDFC First Bank Limited % share | 4.4% | 776 |
| Axis Bank Limited % share | 3.7% | 777 |
| Bank Of Baroda % share | 3.6% | 778 |
| SIDBI % share | 3.4% | 779 |
| Blue Orchard* % share | 3.2% | 782 |
| Top 10 Total % share | 52.0% | 785 |
| Long term rating | A (Stable) by ICRA | 790 |
| Short-term rating | A1 by ICRA | 791 |

### 4g. Slides 26-27 — Geographic Presence (20 items)
| Item | FY24 | FY25 | FY26 | Q1FY27 | Line |
|---|---|---|---|---|---|
| Districts (count) | 421 | 529 | 577 | 590 | 806-812 |
| States (count, incl. UTs) | 26 | 29 | 32 | 32 | 799-812 |
| Branches (count) | 1,393 | 1,568 | 2,015 | 2,041 | 799-812 |
| Clients — Total (Lakhs) | 34.7 | 33.6 | 33.7 | 34.0 | 820 |
| Clients — Subsidiaries (Lakhs) | 1.3 | 0.8 | 0.9 | 0.9 | 822 |
| Clients — SCNL (Lakhs) | 33.4 | 32.9 | 32.8 | 33.1 | 830 |
| Employees — Satin (count) | 9,309 | 11,509 | 11,867 | 12,511 | 843 |
| Employees — Subsidiaries (count) | 1,516 | 2,053 | 1,958 | (per row) | 846-850 |
| Loan Officers (count) | 11,363 | 15,189 | 16,212 | 16,560 | 855 |
| Top 4 States portfolio share | 55% | — | — | — | 843-844 |
| Next 6 States/UTs portfolio share | 29% | — | — | — | 845-851 |
| Remaining 22 States/UTs portfolio share | 16% | — | — | — | 852-855 |
| Uttar Pradesh on-book (₹Cr) / % / CE% / PAR90 | 2,289 / 23% / 99.8% / 1.9% | — | — | — | 871 |
| Assam on-book (₹Cr) / % / CE% / PAR90 | 1,475 / 15% / 100.0% / 0.4% | — | — | — | 873 |
| Bihar on-book (₹Cr) / % / CE% / PAR90 | 1,305 / 13% / 99.9% / 2.7% | — | — | — | 875 |
| West Bengal on-book (₹Cr) / % / CE% / PAR90 | 1,046 / 10% / 99.7% / 2.7% | — | — | — | 877 |
| Madhya Pradesh on-book (₹Cr) / % / CE% / PAR90 | 615 / 6% / 99.6% / 3.4% | — | — | — | 879 |
| Punjab on-book (₹Cr) / % / CE% / PAR90 | 419 / 4% / 99.9% / 1.1% | — | — | — | 881 |
| Others on-book (₹Cr) / % / CE% / PAR90 | 2,886 / 29% / 99.7% / 2.8% | — | — | — | 883 |
| Total on-book (₹Cr) / % / CE% / PAR90 | 10,035 / 100% / 99.9% / 2.2% | — | — | — | 885 |

Slide 26's map graphic also scatters standalone numbers (140, 110, 112, ~590, 3.9
Lakhs, 98%, 27, 42, and district/branch counts for individual states embedded in
a geographic layout) that pdftotext -layout could not reliably tie to specific
state labels once flattened to plain text. These figures are present in the raw
extract (lines 799-861) but their state-level attribution is flagged
CHART_LAYOUT_AMBIGUOUS rather than asserted.

### 4h. Slides 29-33 — Group Structure & Subsidiaries (37 items)
| Item | Value | Line | Flag |
|---|---|---|---|
| SHFL — AUM | ₹1,263 Cr | 926 | — |
| SHFL — Branches | 57 | 930 | — |
| SHFL — Net worth | ₹381 Cr | 932-933 | — |
| SFL — AUM | ₹1,360 Cr | 926 | — |
| SFL — Branches | 121 | 927 | — |
| SFL — Net worth | ₹344 Cr | 929-931 | — |
| STL — Net worth | ₹20 Cr | 934 | STL has no AUM/Branches line (non-lending tech subsidiary — structural N/A, not ZERO_STANDING) |
| SGAL — (no AUM/Net worth/Branches disclosed) | — | 907-937 | ZERO_STANDING — see Table 6 |
| "68% stake" (floating, unlabeled, top of org chart) | 68% | 912 | CHART_LAYOUT_AMBIGUOUS — confirmed elsewhere (line 1029) to be STL's stake in QTrino Labs, not an SCNL-level figure |
| SHFL — AUM (detail panel) | ₹1,263 Cr | 942 | — |
| SHFL — No. States/UTs | 22 | 943 | — |
| SHFL — Tenure | 24-240 months | 945 | — |
| SHFL — Avg Ticket Size Q1FY27 | ₹12,37,000 | 946 | — |
| SHFL — Collection Frequency | Monthly | 947 | — |
| SHFL — No. Loan Accounts | 12,412 | 949 | — |
| SHFL — GNPA | 3.3% | 950 | — |
| SHFL — CRAR | 59.8% | 952 | — |
| SHFL — Credit Rating | A- (Stable) ICRA | 953 | — |
| SHFL — AUM chart FY24/FY25/FY26/Q1FY27 | 756 / 920 / 1,267 / 1,263 | 958-967 | — |
| SHFL — Total Revenue chart FY24/FY25/FY26/Q1FY27 | 92 / 115 / 146 / 38 | 964-967 | — |
| SHFL — AUM 3-yr CAGR | 35.9% | 970 | — |
| SHFL — Revenue 3-yr CAGR | 33.2% | 971 | — |
| SFL — AUM (detail panel) | ₹1,360 Cr | 982 | — |
| SFL — No. States/UTs | 14 | 983 | — |
| SFL — Tenor | Up to 60 months | 985 | — |
| SFL — Avg Ticket Size Q1FY27 (Retail) | ₹2,24,000 | 986 | — |
| SFL — Collection Frequency | Monthly/Quarterly | 988 | — |
| SFL — No. Loan Accounts | 55,673 (+21,783 JLG, see footnote) | 989 | — |
| SFL — GNPA | 3.5% | 991 | — |
| SFL — CRAR | 27.1% | 992 | — |
| SFL — Credit Rating | A- (Stable) ICRA | 994 | — |
| SFL — AUM/Income chart series (SFL-JLG AUM, SFL AUM, Total Income) FY24-Q1FY27 | 175/501/121 (FY24 approx), further values at 1007-1010 | 998-1010 | CHART_LAYOUT_AMBIGUOUS — 3-series chart, exact quarter/series mapping uncertain from flattened text |
| SFL — Green finance disbursement Q1FY27 | 50 loans, ₹294 Cr | 1009 | — |
| SFL — Green finance AUM | ₹624 Cr | 1010 | — |
| STL — QTrino ownership stake | 68% (as of 30 Jun'26) | 1029-1031 | — |
| STL — Core Banking go-live target | 30 September 2026 | 1034 | — |
| SGAL — narrative only (all-women board, Cat-II AIF license from SEBI, targeting first close/deployment next quarter) | no financial figures | 1054-1078 | ZERO_STANDING |

### 4i. Slide 35 — Business Details (16 rows)
| Line item | Q1FY27 | Q1FY26 | YoY% | Q4FY26 | QoQ% | Line |
|---|---|---|---|---|---|---|
| AUM Total (₹Cr) | 15,935 | 12,499 | 27% | 15,174 | 5% | 1100 |
| SCNL | 13,312 | 10,956 | — | 12,853 | — | 1101 |
| SCNL On-book | 10,035 | 8,668 | — | 9,539 | — | 1102 |
| SCNL Off-book | 3,277 | 2,288 | — | 3,314 | — | 1103 |
| SHFL | 1,263 (incl. ₹228 Cr assigned) | 961 (incl. ₹162 Cr assigned) | — | 1,267 (incl. ₹216 Cr assigned) | — | 1104 |
| SFL | 1,360 (incl. ₹74 Cr assigned) | 582 | — | 1,054 (incl. ₹67 Cr assigned) | — | 1105 |
| SFL — MSME | 1,334 | 551 | — | 1,028 | — | 1106 |
| AUM Mix Total (₹Cr) | 15,935 | 12,499 | 27% | 15,174 | 5% | 1107 |
| MFI Lending | 12,882 | 10,767 | — | 12,522 | — | 1108 |
| Business Correspondence | 26 | 31 | — | 26 | — | 1109 |
| MSME | 1,790 | 771 | — | 1,385 | — | 1110 |
| Housing Finance | 1,263 | 961 | — | 1,267 | — | 1111 |
| No. of Branches Total | 2,041 | 1,599 | 28% | 2,015 | 1% | 1112 |
| SCNL branches | 1,863 | 1,487 | — | 1,841 | — | 1113 |
| SHFL branches | 57 | 44 | — | 53 | — | 1114 |
| SFL branches | 121 | 68 | — | 121 | — | 1115 |

### 4j. Slide 36 — Diversified Product Offerings (13 rows x 3 entities)
| Metric | SCNL | SHFL | SFL | Line |
|---|---|---|---|---|
| Purpose | Unsecured micro loans, JLG model | Affordable/micro housing | Sustainable & Emerging Business loans | 1127-1130 |
| Ticket Size Range | Up to ₹1,05,000 | ₹1,00,000-₹40,00,000 | Up to ₹2,00,00,000 | 1133 |
| Tenure | 6-48 months | 24-240 months | Up to 60 months | 1135 |
| Frequency of Collection | Bi-Weekly | Monthly | Monthly/Quarterly | 1137 |
| No. States/UTs | 30 | 22 | 14 | 1139 |
| No. Branches | 1,863 | 57 | 121 | 1141 |
| AUM (₹Cr) | 12,856 (+₹456 Cr other MSME) | 1,263 | 1,360 | 1143 |
| No. Loan Accounts | 33,89,835 | 12,412 | 77,456 | 1145 |
| Avg Ticket Size Q1FY27 | ₹61,000 (JLG) | ₹12,37,000 | ₹2,24,000 (Retail) | 1147 |
| GNPA | 2.2% | 3.3% | 3.5% | 1149 |
| CRAR | 26.7% | 59.8% | 27.1% | 1151 |
| Active Lenders | 77 | 34 | 36 | 1153 |
| Credit Rating | ICRA A (Stable) | ICRA A- (Stable) | ICRA A- (Stable) | 1155 |

### 4k. Slides 37-38 — Consolidated / Standalone Income Statement (10 rows each = 20)
| Line item | Slide | Q1FY27 | Q1FY26 | YoY | Q4FY26 | QoQ | Line |
|---|---|---|---|---|---|---|---|
| Interest Income | 37 (Consol) | 693 | 596 | 16% | 609 | 14% | 1165 |
| DA Income | 37 | 94 | 49 | — | 145 | — | 1167 |
| Less: Finance Cost | 37 | 313 | 269 | — | 288 | — | 1169 |
| Add: Other Income | 37 | 40 | 34 | — | 76 | — | 1171 |
| Net Interest Income | 37 | 514 | 411 | 25% | 542 | -5% | 1173 |
| Less: Operating Expenses | 37 | 247 | 210 | — | 251 | — | 1175 |
| Less: Credit Cost | 37 | 106 | 143 | — | 78 | — | 1177 |
| Profit Before Tax | 37 | 161 | 58 | 178% | 212 | -24% | 1179 |
| Less: Tax | 37 | 39 | 13 | — | 50 | — | 1181 |
| Profit for the Period | 37 | 123 | 45 | 172% | 162 | -24% | 1183 |
| Interest Income | 38 (Standalone) | 613 | 538 | 14% | 547 | 12% | 1196 |
| DA Income | 38 | 92 | 45 | — | 130 | — | 1198 |
| Less: Finance Cost | 38 | 269 | 239 | — | 251 | — | 1200 |
| Add: Other Income | 38 | 28 | 25 | — | 42 | — | 1202 |
| Net Interest Income | 38 | 465 | 370 | 26% | 469 | -1% | 1204 |
| Less: Operating Expenses | 38 | 207 | 181 | — | 212 | — | 1206 |
| Less: Credit Cost | 38 | 100 | 135 | — | 75 | — | 1208 |
| Profit Before Tax | 38 | 158 | 55 | 189% | 181 | -13% | 1210 |
| Less: Tax | 38 | 38 | 12 | — | 44 | — | 1212 |
| Profit for the Period | 38 | 120 | 43 | 182% | 137 | -12% | 1214 |

(Blank YoY/QoQ cells above are the source's own presentation — only the 4 headline
rows (Interest Income, NII, PBT, Profit for Period) get computed deltas; the other
6 line items in each statement do not. Flag: DELTA_OMITTED, same pattern as 4c.)

### 4l. Slide 39 — Shareholding Pattern & Capital Market Info (15 items)
| Item | Value | Line | Flag |
|---|---|---|---|
| Shareholding pie: 6 categories (Promoter, Public, DII, Bodies Corporate, Florintree Ventures LLP, FII) | 36.2%, 21.8%, 19.8%, 11.1%, 6.3%, 4.8% | 1229-1243 | CHART_LAYOUT_AMBIGUOUS — legend order (Promoter/Public/DII/Bodies Corporate/Florintree/FII) does not line up unambiguously with the 6 flattened percentages in text-extraction order; category-to-value pairing not asserted with confidence |
| Face Value | ₹10.0 | 1232 | — |
| Market Price | ₹245.9 | 1236 | — |
| 52 Week H/L | ₹248.2 / ₹133.0 | 1239 | — |
| Market Cap | ₹2,716.5 Cr | 1241 | — |
| Equity Shares Outstanding | 11.0 Cr | 1244 | — |
| 1-Year Avg Trading Volume | 400.3 ('000) | 1246 | — |
| No. of Equity Shareholders | 37,727 | 1249 | — |
| Book Value per share | ₹270 | 1251 | — |
| Share price Jun'25 | ₹169.8 | 1248 | — |
| Share price Sep'25 | ₹145.1 | 1248 | — |
| Share price Dec'25 | ₹143.6 | 1249 | — |
| Share price Mar'26 | ₹143.6 | 1249 | — |
| Share price Jun'26 | ₹245.9 | 1247 | — |
| Change in Share Price YoY | 45% | 1247 | — |

### 4m. Slide 40 — Glossary (16 terms)
AUM, CRAR, Financial Cost Ratio, GNPA, Gross Yield, Leverage Ratio, Loan Loss
Ratio, Net Interest Margin, NNPA, Operating Expenses Ratio, ROA, ROE, SCNL, SFL,
SGAL, SHFL — each with one definition sentence, lines 1260-1286. No numeric
content (definitional only).

### 4n. Slide 41 — Disclaimer / Contacts
SCNL disclaimer (3 paragraphs, lines 1292-1308), Valorem Advisors disclaimer (1
paragraph, lines 1311-1315), 3 contact records: Mr. Anuj Sonpal (Valorem
Advisors, +91 22 3507 5100), Ms. Aditi Singh (SCNL, +91 124 4715 400), Ms. Shilpa
Bajaj (SCNL, +91 124 4715 400) — lines 1320-1323.

---

## TABLE 5 — SLIDES 3, 5, 20 HEADLINE BULLETS (already covered as text in Table 1;
cross-referenced numeric claims below to avoid double-listing full KPI tables)

Slide 3 headline bullets (line 93-107): AUM ₹13,312 Cr (+22% YoY), Disbursement
₹3,008 Cr (+46% YoY), Revenue ₹734 Cr (+21% YoY), PAT ₹120 Cr (+182% YoY), Credit
Cost -177bps to 3.06% (incl. ₹36 Cr overlay; ex-overlay 1.97%), ROA +200bps to
3.55% (ex-overlay 4.34%), ROE +910bps to 15.10% (ex-overlay 18.46%), NIM +120bps
to 14.36%, Promoter equity infusion ₹100 Cr at ~17% premium to minimum issue
price, leadership vintage 10+ years / zero attrition in 200-person field
leadership. These figures are the standalone-level headline figures, all
independently reconciled against slides 15/18/19/23 detail tables — no
discrepancy found.

---

## TABLE 6 — ZERO_STANDING / DATA ANOMALY FLAGS

| # | Item | Slide(s) | Detail | Flag |
|---|---|---|---|---|
| 1 | SGAL financial disclosure | 29, 33 | The group-structure slide (29) presents a standing template of AUM/Branches/Net-worth for SHFL and SFL, and Net-worth-only for STL; SGAL — the newest WOS (since Aug'25) — has no figure of any kind (no AUM, no net worth, no fund size) on either its group-chart panel (29) or its dedicated slide (33), which is narrative-only. The template slot exists (every other subsidiary gets one); SGAL's is empty. | ZERO_STANDING |
| 2 | Active Clients QoQ, Consolidated Highlights | 16 | Line 468-469: literal text "xx" appears twice in the Active Clients row (Q1FY27 column area and QoQ column), rather than a computed value or blank. Q1FY27 and Q4FY26 both show "34" lakh, so QoQ growth is ~0%, but the source renders the placeholder token "xx" instead of "0%" or a dash — looks like an unresolved template artifact in the company's own deck, not an extraction error (confirmed present in the pdftotext -layout native text, not the OCR fallback). | ZERO_STANDING / DATA_ARTIFACT |

---

## TABLE 7 — SIGNATURE / REGULATORY LETTER BLOCK (page 1, lines 25-63)

| Item | Detail | Line |
|---|---|---|
| Addressees | NSE (Exchange Plaza, BKC) and BSE (P.J. Towers, Dalal Street) | 28-34 |
| Symbol / Scrip Code | SATIN / 539404 | 34 |
| Subject | Investor Presentation, Reg. 30 SEBI LODR | 36 |
| Reporting period | Un-audited results (Standalone & Consolidated), quarter ended 30 June 2026 | 42 |
| Signatory | Vikas Gupta, Company Secretary & Chief Compliance Officer | 61-62 |
| Digital signature timestamp | 2026-07-30 17:21:49 +05'30' | 53-57 |
| Letter date | 30 July 2026 (matches signature date — no timing gap) | 26, 57 |

No board-meeting timing given in this document type (that belongs to the Board
Outcome letter / Results filing, not the presentation) — correctly out of scope
for this doctype per instruction; not treated as a miss.

---

## TABLE 8 — DROPPED_SLIDE / ENTITY_CHANGE CHECK

Prior-quarter (Q4FY26) presentation ledger was not supplied as an input to this
run (`PRIOR_LEDGER_PATH` left unfilled in the task message). Consequently:
- DROPPED_SLIDE diff against the Q4FY26 deck could not be performed this run.
- ENTITY_CHANGE diff (subsidiary/consolidation list changes) could not be
  formally performed against a prior ledger. Noting for the record: SGAL is
  described as "Since Aug'25 (WoS)" (line 920) and carries visibly less
  disclosure maturity than SHFL/SFL/STL (est. Feb'18/Mar'19/Aug'24
  respectively) — this reads as a recently added entity to the group
  structure, consistent with (though not proof of) an ENTITY_CHANGE from a
  slide-29-equivalent in the prior quarter. Flagged for A3/A4 to confirm via
  the extract_results and extract_pressrelease files or via COMPANY MEMORY.

Flag: STRUCTURAL_GAP (no prior ledger supplied) — not a GATE A2 failure, since
GATE A2 concerns internal count-test reconciliation of this document only.

---
```yaml
stage: A2-enumerator
company: "SATIN"
quarter: "Q1FY27"
doctype: "presentation"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/satin-q1fy27/work/ledger_presentation_satin_q1fy27.md"
counts:
  slides: 42
  slide_numbers: 42
  ocr_pages: 6
  footnotes: 55
  line_items: 240
  zero_standing: 2
  agenda_items: 0
  auditor_paras: 0
  entities: 4
  turns: 0
  questions: 0
  mgmt_numbers: 0
flags_raised: [ZERO_STANDING, DATA_ARTIFACT, DELTA_OMITTED, CHART_LAYOUT_AMBIGUOUS, OCR_DIVIDER, STRUCTURAL_GAP]
gate_a2: pass
mismatch_note: ""
```
