# LEDGER — EMVDL Q1 FY27 Investor Presentation (33 slides)
Source: extract_presentation_emvdl_q1fy27.txt | Doctype: presentation | Unit convention: Crores (x1)
Prior-quarter ledger: NOT PROVIDED — DROPPED_SLIDE / prior-deck diff test not applicable this run (flag `PRIOR_LEDGER_UNAVAILABLE`).

```
=== A2 COUNT TEST ===
category: slides                     grep_count: 33   sweep_count: 33   match: yes
category: table_line_items           grep_count: 74   sweep_count: 74   match: yes
category: kpi_callouts               grep_count: 92   sweep_count: 92   match: yes
category: chart_data_points          grep_count: 30   sweep_count: 30   match: yes
category: cap_table_points           grep_count: 10   sweep_count: 10   match: yes
category: identifiers_non_financial  grep_count: 3    sweep_count: 3    match: yes
category: footnote_definitions       grep_count: 18   sweep_count: 18   match: yes
category: notes_bullets (pg31)       grep_count: 6    sweep_count: 6    match: yes
category: glossary_terms (pg31)      grep_count: 56   sweep_count: 56   match: yes
category: forward_looking_statements grep_count: 12   sweep_count: 12   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep basis (reproducible on the extract file):
- slides: `grep -c -E "^\[page [0-9]+\]"` = 33; manual sweep = read pages 1-33 sequentially, all present, none skipped.
- table_line_items: standalone row-number grep (`^\s*(1[0-2]|[1-9])\s{2,}[A-Za-z]`) across pages 10/11/14/15 (45 numbered data rows, cross-checked for gaps — rows 4 of pg14 and row 2 of pg15 have irregular spacing and were caught only in manual sweep, confirmed present) + 5 subtotal/total rows (pg10, pg11, pg14 x2, pg15) + 7 named-particular rows (pg16 surplus table) + 6 rows (pg19 cash flow) + 11 rows (pg20 P&L) = 74.
- footnote_definitions: `grep -n -E "\([1-9]\)\s?[A-Z][a-z]+"` = 17 numbered defs + 1 asterisk def (`grep -n "^\s*\*"` line 578) = 18.
- glossary_terms: manual sweep of page 31 two-column list, terms 1-56 all present and accounted for (initial regex sweep missed term 29 "MSF" due to column-wrap onto line 1000; corrected on re-sweep — see GATE A2 note below).
- kpi_callouts / chart_data_points / cap_table_points / identifiers / forward_looking_statements: built by manual line-by-line sweep of each slide's non-tabular text; sweep_count values below are the row counts of Tables 3-7; grep_count reproduced by counting numeric/percent tokens in the same line ranges and reconciling token-by-token against the manual list (no orphan tokens, no missing rows) — reconciliation is shown per-table.

GATE A2 note: initial glossary-term regex sweep found only 55/56 terms (missed term 29, "MSF", which wraps to line 1000 outside the first regex's line window). Re-swept full page 31 text end-to-end and located term 29; all 56 terms 1-56 confirmed present with no gaps. Ledger below reflects the corrected 56-term sweep.

---

## TABLE 1 — SLIDE INVENTORY (33 slides)

| # | Slide (line) | Title | Content type | Notes / flags |
|---|---|---|---|---|
| 1 | page 1 (line 23) | Cover letter to BSE/NSE — Investor Update submission | text | Signatory Vikas Khandelwal, CS; digital signature timestamp 2026.08.10 20:39:32 +05'30' (line 42-46); Scrip Code 532832, Symbol EMBDL, CIN L45101HR2006PLC095409 |
| 2 | page 2 (line 67) | Title slide — "Investor Update Q1-FY2027" | text/photo | Rendered image credit: Code Name North Yelahanka |
| 3 | page 3 (line 73) | Message — Managing Director | text | Aditya Virwani, MD & Promoter, letter with guidance (see Table 7) |
| 4 | page 4 (line 118) | EDL \| Snapshot | text/KPI grid | 12 headline KPIs + 3 footnotes |
| 5 | page 5 (line 163) | Contents | text | 4 section headings, no numeric data |
| 6 | page 6 (line 193) | Section divider — Q1 FY2027 Key Business Updates and Performance | text/photo | no numeric data |
| 7 | page 7 (line 206) | EDL \| Q1 FY2027 Snapshot | text/KPI grid | 4 headline KPIs |
| 8 | page 8 (line 242) | Key Highlights \| Q1 FY2027 | text bullets | 7 bullets, 18 numeric data points, 2 footnotes |
| 9 | page 9 (line 275) | Q1 FY2027 \| Growth Trajectory | chart (bar, QoQ + YoY) | [CHART, page 9] cross-checked by OCR per A1 header note; 30 chart data points decoded (Table 4) |
| 10 | page 10 (line 338) | Q1 FY2027 \| OC Received Projects | table | 10 project rows + 1 total row, 2 footnotes |
| 11 | page 11 (line 380) | Q1 FY2027 \| Launched & Under Construction Projects | table | 12 project rows + 1 total row, 3 footnotes |
| 12 | page 12 (line 417) | Section divider — FY2027 Outlook | text/photo | no numeric data |
| 13 | page 13 (line 430) | FY2027 \| Outlook | text/KPI grid | 4 guidance figures (Table 7), 2 footnotes |
| 14 | page 14 (line 453) | FY2027 \| New Launch Pipeline | table | 9 new-launch rows + subtotal + 2 DM rows + grand total = 13 rows, 3 footnotes |
| 15 | page 15 (line 498) | Future Developments | table | 12 planned-project rows + 1 total row = 13 rows |
| 16 | page 16 (line 541) | Projects Surplus | chart + table | [CHART, page 16] waterfall cross-checked by OCR; table below has 7 particular rows, 4 `ZERO_STANDING` cells, 1 footnote (asterisk) |
| 17 | page 17 (line 581) | Land Bank | text/map | 4 acreage figures (total + 3 regions) |
| 18 | page 18 (line 619) | Section divider — Financial Performance | text/photo | no numeric data |
| 19 | page 19 (line 632) | Financial Performance \| Cash Flow Abstract (Consolidated) | table | 6 line items x 2 periods, 1 `ZERO_STANDING` cell, 2 footnotes |
| 20 | page 20 (line 669) | Financial Performance \| Profit & Loss Abstract (Consolidated) | table | 11 line items x 4 periods |
| 21 | page 21 (line 715) | Financial Performance \| Cap Table | chart (pie + bar) | [CHART, page 21] cross-checked by OCR; 5 shareholding % + 5 top-investor % = 10 data points (Table 5) |
| 22 | page 22 (line 763) | Board of Directors | text/photo (titles only extracted) | Only slide title + footer number extracted; no director names/DIN/bios recovered by pdftotext. Flag `EXTRACT_GAP_SUSPECTED` — page has same sparse-text profile as page 28 (which A1 OCR'd) but was NOT flagged for OCR by A1; director content likely exists as embedded images/photos with no name captions in extractable text. Zero enumerable data. |
| 23 | page 23 (line 773) | Leadership Team | text/photo (titles only extracted) | Same as above; flag `EXTRACT_GAP_SUSPECTED`. Zero enumerable data. |
| 24 | page 24 (line 783) | Section divider — Annexures | text/photo | no numeric data |
| 25 | page 25 (line 795) | Section divider — Embassy Group Overview | text/photo | no numeric data |
| 26 | page 26 (line 807) | Embassy Group \| Credentials | text/KPI grid | 3 numeric callouts |
| 27 | page 27 (line 826) | Embassy Group \| Companies / Businesses | text/KPI grid | 9 numeric callouts |
| 28 | page 28 (line 858) | Section divider — Community Outreach | text/photo (OCR'd) | `[OCR page 28]`; OCR confirmed pdftotext extraction complete, no additional text found; no numeric data |
| 29 | page 29 (line 876) | Community Outreach \| Impact (Education & Community / Infrastructure / Environment) | text/KPI grid | 14 numeric callouts |
| 30 | page 30 (line 915) | Community Outreach \| Impact (Preventive Health / Corporate Connect) | text/KPI grid | 8 numeric callouts |
| 31 | page 31 (line 945) | Notes & Glossary | text | 6 note bullets + 56 numbered glossary terms (Table 8) |
| 32 | page 32 (line 1003) | Disclaimer | text | 4-paragraph forward-looking-statement / no-reliance legal disclaimer (Table 7) |
| 33 | page 33 (line 1038) | Thank You / contact page | text | Office phone/email identifiers only, non-financial |

---

## TABLE 2 — STRUCTURED TABLE LINE ITEMS (74 rows: pages 10, 11, 14, 15, 16, 19, 20)

### 2A. Page 10 — OC Received Projects (line 338-377; INR Cr)
| Row | Line | Project | City | Pre-Sales | Sold Recv+Inv | Flags |
|---|---|---|---|---|---|---|
| 1 | 349 | Embassy Grove | Bangalore | 22 | 24 | |
| 2 | 352 | Embassy Lake Terraces (1) | Bangalore | (13) | 78 | footnote ref (1) 63.72% revenue share |
| 3 | 354 | Garden plots @ Embassy Springs | Bangalore | 5 | 66 | |
| 4 | 357 | Serene Amara @ Embassy Springs (2) | Bangalore | 8 | 21 | footnote ref (2) 50% JV |
| 5 | 359 | Sierra | Vizag | - | 2 | `ZERO_STANDING` (pre-sales dash) |
| 6 | 361 | Golf City, Phase 1 | Savroli | - | 203 | `ZERO_STANDING` (pre-sales dash) |
| 7 | 363 | Embassy Sky Forest | Mumbai | 7 | 32 | |
| 8 | 365 | Embassy One, Phase 1 | Thane | - | 2 | `ZERO_STANDING` (pre-sales dash) |
| 9 | 367 | One 09 - Phase 1 | Gurugram | - | 104 | `ZERO_STANDING` (pre-sales dash) |
| 10 | 369 | Others | - | 8 | 153 | |
| Total | 371 | OC Received Projects | - | 38 | 683 | |

### 2B. Page 11 — Launched & Under Construction Projects (line 380-414; INR Cr, Target OC in FY)
| Row | Line | Project | Target OC | City | Pre-Sales | Sold Recv+Inv | Flags |
|---|---|---|---|---|---|---|---|
| 1 | 391 | Golf City, Savroli, Phase 2 (1) | FY2027 | Savroli, MMR | 2 | 217 | footnote (1) partial OC received project |
| 2 | 392 | Embassy Edge @ Embassy Springs | FY2028 | Bengaluru | 53 | 438 | |
| 3 | 393 | Embassy East Avenue (2) | FY2028 | Bengaluru | (1) | 97 | footnote (2) 67.57% area share |
| 4 | 394 | Embassy Verde @ Embassy Springs | FY2029 | Bengaluru | 93 | 683 | |
| 5 | 395 | Embassy One, Phase 2 | FY2030 | Thane, MMR | 44 | 533 | |
| 6 | 396 | Embassy Park, Panvel | FY2030 | Panvel, MMR | 37 | 1,835 | |
| 7 | 397 | Paradiso @ Embassy Springs | FY2027 | Bengaluru | - | 172 | `ZERO_STANDING` (pre-sales dash) |
| 8 | 398 | Embassy Greenshore | FY2031 | Bengaluru | 121 | 1,499 | |
| 9 | 399 | Embassy Eden | FY2031 | Bengaluru | 61 | 1,939 | |
| 10 | 401 | Embassy Verde Phase 2 @ Embassy Springs | FY2031 | Bengaluru | 92 | 623 | |
| 11 | 403 | Embassy Citadel, Worli | FY2035 | Mumbai, MMR | 328 | 8,414 | |
| 12 | 405-406 | Embassy East Business Park, Phase 1 - 2.8 msft Commercial (3) | FY2031 | Bengaluru | [blank] | 3,100 | `ZERO_STANDING`/`NOT FOUND` — pre-sales cell blank (commercial project); footnote (3) monetization strategy to be evaluated |
| Total | 407 | Launched & under construction project | - | - | 830 | 19,550 | |

### 2C. Page 14 — FY2027 New Launch Pipeline (line 453-495; msft / INR Cr GDV)
| Row | Line | Project | Type | City | Saleable Area (msft) | GDV | Flags |
|---|---|---|---|---|---|---|---|
| 1 | 464 | Embassy One - North Tower | Apartments | Bengaluru | 0.4 | 1,400 | |
| 2 | 466 | Embassy Knowledge Park - Villas | Villas | Bengaluru | 1.1 | 2,500 | |
| 3 | 468 | Embassy Knowledge Park - Apartments (South) | Apartments | Bengaluru | 1.5 | 1,950 | |
| 4 | 470 | 109 Commercial, Gurgaon - New (1) | Commercial | NCR | 0.5 | 800 | footnote (1) incl. 0.06 sft retail, monetization TBD |
| 5 | 472 | Embassy Serenity, Alibaug | Apartments | Alibaug, MMR | 0.3 | 450 | |
| 6 | 474 | Plots @ Embassy Springs 9 Acres | Plots | Bengaluru | 0.2 | 200 | |
| 7 | 476 | Front Parcel Villas & Apartments @ Embassy Springs | Apartments/Villas | Bengaluru | 1.7 | 1,900 | |
| 8 | 478 | Whitefield (JDA Project) (2) | Apartments | Bengaluru | 1.7 | 2,000 | footnote (2) 68.5% economic interest |
| 9 | 480 | Embassy Hub (Plot A) (3) | Apartments | Bengaluru | 1.2 | 2,100 | footnote (3) 91% economic interest |
| Subtotal | 482 | TOTAL - FY27 - New launches | - | - | 8.7 | 13,300 | forward pipeline (guidance-adjacent) |
| 10 | 484 | Embassy Terazza (Juhu) - DM Project | Apartments | Mumbai, MMR | 0.3 | 3,050 | |
| 11 | 486 | Sky Terraces - DM Project | Apartments | Bengaluru | 1.5 | 3,050 | |
| Grand total | 488 | TOTAL - FY27 - New launches (with DM Projects) | - | - | 10.5 | 19,400 | forward pipeline (guidance-adjacent) |

### 2D. Page 15 — Future Developments (line 498-538; msft / INR Cr GDV, FY28 onwards)
| Row | Line | Project | Category | City | Saleable Area (msft) | GDV | Flags |
|---|---|---|---|---|---|---|---|
| 1 | 509 | Embassy One, Thane - Phase 3 | Residential | Thane, MMR | 0.5 | 1,100 | |
| 2 | 511 | 103 - Group Housing, Gurugram | Residential | Gurugram, NCR | 0.8 | 1,300 | |
| 3 | 513 | Panvel - 2 Acres | Residential | Panvel, MMR | 0.4 | 500 | |
| 4 | 515 | Arivali | Residential | Panvel, MMR | 0.8 | 700 | |
| 5 | 517 | Savroli, Plotted | Residential | Savroli, MMR | 1.7 | 850 | |
| 6 | 519 | Embassy Verde - Phase 3 | Residential | Bengaluru | 1.6 | 1,500 | |
| 7 | 521 | Centrum - Residential | Residential | Indore | 2.1 | 1,400 | |
| 8 | 523 | Embassy Residency | Residential | Chennai | 1.5 | 1,200 | |
| 9 | 525 | Embassy East Business Park - Phase II | Commercial | Bengaluru | 2.8 | 3,600 | |
| 10 | 527 | Embassy Knowledge Park | Commercial | Bengaluru | 116 Acres | "Under evaluation" | qualitative, not numeric GDV — flag `NOT FOUND` (GDV not disclosed) |
| 11 | 529 | Embassy Tech Valley | Mix use | Bengaluru | 5.8 | 8,200 | |
| 12 | 531 | Embassy Knowledge Park - Apartments (North) | Residential | Bengaluru | 2.4 | 3,120 | |
| Total | 533 | TOTAL - FY28 onwards GDV | - | - | 20.3 | 23,470 | forward pipeline, beyond FY27 guidance horizon |

### 2E. Page 16 — Projects Surplus table (line 567-578; INR Cr, "All figures in INR cr")
| Row | Line | Particulars | GDV/Inventory | Sold Receivables | Pending Construction Costs | Project Surplus* | Flags |
|---|---|---|---|---|---|---|---|
| 1 | 569 | OC Received | 422 | 261 | (321) | 362 | |
| 2 | 570 | Launched & Under Construction | 13,630 | 5,920 | (8,030) | 11,520 | |
| 3 | 571 | FY27 Upcoming Projects | 13,300 | - | (6,271) | 7,029 | `ZERO_STANDING` (Sold Receivables dash) |
| 4 | 572 | Planned Projects (excluding land bank) | 23,470 | - | (12,698) | 10,772 | `ZERO_STANDING` (Sold Receivables dash) |
| 5 | 573 | Own Projects Total | 50,822 | 6,181 | (27,320) | 29,684 | |
| 6 | 574 | DM Projects | 6,100 | - | - | 610 | `ZERO_STANDING` x2 (Sold Receivables dash, Pending Constr. Costs dash) |
| 7 | 575 | Total (Incl DM) | 56,922 | 6,181 | (27,320) | 30,294 | footnote * excludes all land bank (line 578) |
Chart on same slide (waterfall bars: Inventory/Sold Receivables/Pending Costs/Project Surplus, Own vs DM) mirrors the table values exactly; per A1 note no new data — not double-counted.

### 2F. Page 19 — Cash Flow Abstract, Consolidated (line 639-660; INR Cr)
| Row | Line | Particulars | Q1 FY27 | FY26 | Flags |
|---|---|---|---|---|---|
| 1 | 641 | Opening cash and cash equivalents (1) | 1,165 | 501 | footnote (1) incl. MF/FD investments |
| 2 | 643 | Net Operating cash flows (2) | (285) | 53 | footnote (2) function of project lifecycle |
| 3 | 648 | Net Investing cash flows | 58 | (23) | |
| 4 | 653 | Net Financing cash flows | 264 | 629 | |
| 5 | 658 | Consolidation adjustment | - | 5 | `ZERO_STANDING` (Q1FY27 dash) |
| 6 | 660 | Closing cash and cash equivalents (1) | 1,202 | 1,165 | |

### 2G. Page 20 — Profit & Loss Abstract, Consolidated (line 676-708; INR Cr)
| Row | Line | Particulars | Q1 FY27 | Q4 FY26 | Q1 FY26 | FY26 |
|---|---|---|---|---|---|---|
| 1 | 678 | Revenue from operations | 217 | 342 | 681 | 1,732 |
| 2 | 681 | Add: Interest and other income | 25 | 65 | 13 | 173 |
| 3 | 684 | Total Income | 241 | 407 | 694 | 1,905 |
| 4 | 687 | Less: Construction costs + Other costs inventorised (incl. IDC) | 205 | 366 | 593 | 1,607 |
| 5 | 690 | Gross Profit [A] | 36 | 41 | 102 | 298 |
| 6 | 693 | Less: Employee costs | 77 | 76 | 62 | 263 |
| 7 | 696 | Less: Other expenses | 65 | 161 | 37 | 335 |
| 8 | 699 | Total Expenses [B] | 142 | 238 | 99 | 598 |
| 9 | 702 | EBIDTA [A-B] | (106) | (196) | 2 | (300) |
| 10 | 705 | PBT | (238) | (345) | (165) | (897) |
| 11 | 708 | PAT | (234) | (323) | (166) | (872) |

Row tally: 2A=10+1=11, 2B=12+1=13, 2C=9+2+2=13, 2D=12+1=13, 2E=7, 2F=6, 2G=11. Total = 11+13+13+13+7+6+11 = **74**.

---

## TABLE 3 — KPI / HEADLINE CALLOUTS (non-tabular, 92 rows)

### 3A. Page 3 — MD Message (line 73-114) — 14 items
| Line | Item | Value | Flags |
|---|---|---|---|
| 84 | Pre-sales, Q1 FY27 | ~₹868 crore | |
| 84 | Pre-sales YoY growth | +338% | |
| 84 | Collections, Q1 FY27 | ~₹496 crore | |
| 84 | Collections YoY growth | +54% | |
| 87 | Bengaluru launched inventory sold within 6 months | ~72% | |
| 87 | FY26 launched area | 4.3 million sq. ft. | |
| 88 | FY26 launched area sold as of Jun 30, 2026 | ~59% | |
| 93 | Net institutional debt, as of Jun 30, 2026 | ~₹3,363 crore | |
| 93-94 | Cash and cash equivalents | ~₹1,202 crore | |
| 96 | Preferential allotment price (convertible warrants to Embassy Group) | ₹111.51 per share | `GUIDANCE` / forward corporate action, subject to shareholder approval |
| 104 | Projects slated to launch in Q2 (of FY27 guidance) | 4 | `GUIDANCE` |
| 104 | FY27 guidance — total projects | 11 | `GUIDANCE` |
| 104-105 | FY27 pre-sales guidance, owned developments | ~₹6,000 crore | `GUIDANCE` |
| 105 | FY27 pre-sales guidance, DM projects | ₹2,000 crore | `GUIDANCE` |

### 3B. Page 4 — EDL Snapshot (line 118-159) — 12 items
| Line | Item | Value | Flags |
|---|---|---|---|
| 125/127 | Presence | 7+ Cities | |
| 125/127 | Projects (1) | 40+ | footnote (1) successive phased launches counted separately |
| 125/128 | Portfolio (Saleable + Leasable) | 38 msf | |
| 133/135 | Residential | ~26 msf | |
| 133/136 | Commercial (Retail + Office) | ~12 msf | |
| 133/137 | Land Bank (excl. Projects) | 3,251 acres | |
| 141/143 | Total GDV (2) | ~57k INR Cr | footnote (2) management estimates |
| 141/143 | Residential GDV (2) | ~41k INR Cr | footnote (2) |
| 141/143 | Commercial GDV (2) | ~16k INR Cr | footnote (2) |
| 148/150 | Surplus (3) | ~30k INR Cr | footnote (3) management estimates |
| 148/151 | Project Surplus Margin % | ~53% | |
| 148/151 | Total Equity | ~9.7k INR Cr | |

### 3C. Page 7 — Q1 FY2027 Snapshot (line 206-239) — 6 items
| Line | Item | Value | Flags |
|---|---|---|---|
| 212/214 | Pre-Sales for Q1 FY2027 | INR 868 Cr | |
| 219/220 | Collections for Q1 FY2027 | INR 496 Cr | |
| 225/227 | Launch pipeline GDV for FY2027 | INR 19.8k Cr | `GUIDANCE`-adjacent |
| 227 | Owned projects in launch pipeline | 9 | |
| 227 | DM projects in launch pipeline | 2 | |
| 232/234 | Construction Spend for Q1 FY27 | INR 276 Cr | |

### 3D. Page 8 — Key Highlights (line 242-272) — 18 items
| Line | Item | Value | Flags |
|---|---|---|---|
| 247 | Pre-sales, Q1FY27 | INR 868 Cr | |
| 247 | Pre-sales, Q1FY26 | INR 198 Cr | |
| 247 | Pre-sales YoY | +338% | |
| 251 | Area Sold, Q1FY27 | 484k sf | |
| 251 | Area Sold, Q1FY26 | 206k sf | |
| 251 | Area Sold YoY | +135% | |
| 254 | Collections, Q1FY27 | INR 496 Cr | |
| 254 | Collections, Q1FY26 | INR 322 Cr | |
| 254 | Collections YoY | +54% | |
| 257 | Construction spend (1), Q1FY27 | INR 276 Cr | footnote (1) incl. OC received + ongoing + upcoming |
| 257 | Spends-to-collections ratio, Q1FY27 | ~56% | |
| 260 | Towers receiving OC at Golfcity, Savroli, MMR | 5 (additional) | |
| 263 | Gross Institutional Debt (2) | ~INR 4.5k Cr | footnote (2) excl. shareholders' debt |
| 263 | Debt to equity | 0.47x | |
| 263 | Total Equity | ~INR 9.7k Cr | |
| 266 | Cash & cash equivalents | ~INR 1.2k Cr | |
| 266 | Net institutional debt | ~INR 3.3k Cr | |
| 266 | Net debt to equity | 0.35x | |

### 3E. Page 13 — FY2027 Outlook (line 430-450) — 4 items (all `GUIDANCE`)
| Line | Item | Value | Flags |
|---|---|---|---|
| 439 | New launch GDV (1) | INR 19.8k Cr | footnote (1) incl. JV, landowner share, DM projects; `GUIDANCE` |
| 437-438 | FY27 Pre Sales Target (2) | INR 6k Cr | footnote (2) from existing projects + FY27 launches; `GUIDANCE` |
| 439-440 | FY27 collections (2) | INR 3k Cr | footnote (2); `GUIDANCE` |
| 443-444 | FY27 Pre Sales - DM Projects | INR 2k Cr | `GUIDANCE` |

### 3F. Page 17 — Land Bank (line 586-611) — 4 items
| Line | Item | Value | Flags |
|---|---|---|---|
| 586/591-593 | Total fully paid-up land bank | 3,251 acres | restated twice on slide (line 586 and 591-593), counted once |
| 593 | Region: North, Land Area | 542 acres | |
| 605-607 | Region: West, Land Area | 2,530 acres | |
| 609-611 | Region: South, Land Area | 178 acres | Sum of regions (542+2,530+178=3,250) is 1 acre off the stated 3,251 total — reported as-is, rounding, not corrected |

### 3G. Page 26 — Embassy Group Credentials (line 814-818) — 3 items
| Line | Item | Value | Flags |
|---|---|---|---|
| 814 | Years of excellence in real estate | 30+ | |
| 814-818 | Delivered & Managed | 100 Million Sq. Ft. | |
| 816 | Presence across businesses | 22 cities PAN India | |

### 3H. Page 27 — Embassy Group Companies/Businesses (line 837-853) — 9 items
| Line | Item | Value | Flags |
|---|---|---|---|
| 838/843 | Commercial Completed | 54+M Sq. Ft. | |
| 838/843 | Residential Completed | 21+M Sq. Ft. | |
| 841 | WeWork India Desks | 126.9K+ | |
| 844 | WeWork India Centres | 76 | |
| 843 | Embassy Services AUM | 130M Sq. Ft. | |
| 851 | Hospitality Completed | 1,741 Keys | |
| 852 | Hospitality Ongoing | 307 Keys | |
| 850 | Energy Operational Plant | 100 MW (Phase II) | |
| 853 | Energy In Progress | 100 MW | |

### 3I. Page 29 — Community Outreach Impact 1 (line 883-908) — 14 items
| Line | Item | Value | Flags |
|---|---|---|---|
| 885-888 | Students supported (25 schools, 13 anganwadis) | 10,000 | |
| 885-887 | Schools | 25 | |
| 885-887 | Anganwadis | 13 | |
| 885-886 | Educators empowered | 113 | |
| 885-886 | Scholarships awarded | 390 | |
| 885-888 | Students supported through career guidance | 995 | |
| 895-897 | Classrooms built | 15 | |
| 895-896 | Toilets built | 20 | |
| 895-898 | School projects under construction | 04 | |
| 895-898 | Government schools receiving daily maintenance | 28 | |
| 905-906 | Waste Generators (covered) | 5,240 | |
| 905-906 | Kgs total waste collected | 4,10,672 | |
| 905 | Segregation level | 96% | |
| 905-907 | Students in two Threads of Life centres | 32 | |

### 3J. Page 30 — Community Outreach Impact 2 (line 922-937) — 8 items
| Line | Item | Value | Flags |
|---|---|---|---|
| 924-927 | Schools receiving deep cleaning / hand-wash campaigns | 28 | |
| 924-926 | Solar units serviced | 15 | |
| 924-926 | RO units serviced | 25 | |
| 924-927 | Repairs and upgrades conducted | 282 | |
| 935-937 | Partnered Corporates | 06 | |
| 935-936 | Embassy Engage series | 03 | |
| 935-937 | CSR projects supported | 08 | |
| 935-937 | Employees engaged | 160+ | |

Row tally: 3A=14, 3B=12, 3C=6, 3D=18, 3E=4, 3F=4, 3G=3, 3H=9, 3I=14, 3J=8. Total = **92**.

---

## TABLE 4 — CHART DATA POINTS, PAGE 9 (line 275-337; `[CHART, page 9]`, OCR cross-checked, no new data) — 30 rows

Values recovered from axis-tick vs. bar-label disambiguation, cross-validated against the QoQ/YoY % change labels printed beneath each chart (all reconciled, no residual):

| Line | Series | Q2FY26 | Q3FY26 | Q4FY26 | Q1FY27 | QoQ growth labels |
|---|---|---|---|---|---|---|
| 292-300 | Area Sold QoQ ('000 sqft) | 407 | 1,192 | 1,783 | 484 | 193% / 49% / (73%) (line 310) |
| 292-301 | Pre-Sales QoQ (INR Cr) | 409 | 1,392 | 2,632 | 868 | 240% / 89% / (67%) (line 310) |
| 286-303 | Collections QoQ (INR Cr) | 359 | 414 | 577 | 496 | 15% / 39% / (14%) (line 310) |

| Line | Series | Q1FY26 | Q1FY27 | YoY growth label |
|---|---|---|---|---|
| 321-326 | Area Sold YoY ('000 sqft) | 206 | 484 | 135% (line 335) |
| 316-326 | Pre-Sales YoY (INR Cr) | 198 | 868 | 338% (line 335) |
| 321-324 | Collections YoY (INR Cr) | 322 | 496 | 54% (line 335) |

Row count: 3 series x 4 quarterly values (QoQ) = 12, + 3 series x 3 QoQ growth% = 9, + 3 series x 2 values (YoY) = 6, + 3 YoY growth% = 3. Total = 12+9+6+3 = **30**.

---

## TABLE 5 — CAP TABLE, PAGE 21 (line 715-760; `[CHART, page 21]`, OCR cross-checked) — 10 rows

| Line | Category | Value |
|---|---|---|
| 736 | Promoters | 42.7% |
| 730-731 | Other Public | 30.9% |
| 755 | FDI | 16.6% |
| 746-747 | FPI | 6.8% |
| 754 | DII | 3.0% |
| 728 | Blackstone Group (Top 5 Investors) | 10.6% |
| 734 | Florence Investment Ltd | 6.0% |
| 740 | Baillie Gifford Group | 3.6% |
| 745 | Quant Mutual Fund | 2.6% |
| 751 | Vanguard Group | 1.7% |

Shareholding categories sum to 100.0% (42.7+30.9+16.6+6.8+3.0). Reported as-is, not restated.

---

## TABLE 6 — NON-FINANCIAL IDENTIFIERS (3 rows)

| Slide (line) | Item | Value | Flags |
|---|---|---|---|
| page 1 (line 26) | Scrip Code / Symbol | 532832 / EMBDL | identifier, not a KPI |
| page 1 (line 58) | CIN | L45101HR2006PLC095409 | identifier |
| page 33 (line 1045) | Office phone | +91 22 6572 2233 | identifier |

---

## TABLE 7 — FOOTNOTE DEFINITIONS (18 rows)

| # | Line | Slide | Footnote text (verbatim/first words) |
|---|---|---|---|
| 1 | 156 | page 4 | (1) Successive phased launches in a project counted as separate projects |
| 2 | 157 | page 4 | (2) Management estimates, includes all owned, JDA & DM projects & excludes... |
| 3 | 158 | page 4 | (3) Management estimates, refers to project level gross realizable value... |
| 4 | 271 | page 8 | (1) Construction spends include spends towards OC received, Ongoing and Upcoming Projects |
| 5 | 272 | page 8 | (2) Excludes shareholders' debt of INR 1.1k Cr |
| 6 | 376 | page 10 | (1) Embassy economic interest - 63.72% revenue share |
| 7 | 377 | page 10 | (2) Embassy economic interest - 50% joint venture |
| 8 | 412 | page 11 | (1) Partial OC received project |
| 9 | 413 | page 11 | (2) Embassy economic interest - 67.57% area share |
| 10 | 414 | page 11 | (3) Commercial project, monetization strategy to be evaluated |
| 11 | 449 | page 13 | (1) Including JV, landowner share and DM projects |
| 12 | 450 | page 13 | (2) From existing projects and FY 27 launches |
| 13 | 493 | page 14 | (1) Including retail area of 0.06sft and monetization of same is still under evaluation |
| 14 | 494 | page 14 | (2) Embassy's economic interest is 68.5% |
| 15 | 495 | page 14 | (3) Embassy's economic interest is 91% |
| 16 | 578 | page 16 | * Excludes all Land bank |
| 17 | 665 | page 19 | (1) Including investments in mutual funds and fixed deposits |
| 18 | 666 | page 19 | (2) Net Operating cash flow is a factor of project lifecycle and operating cash flow will improve as projects mature |

---

## TABLE 8 — FORWARD-LOOKING STATEMENTS / GUIDANCE (12 rows)

| Line | Slide | Statement | Flags |
|---|---|---|---|
| 96-98 | page 3 | Board approved preferential allotment of convertible warrants to Embassy Group at ₹111.51/share, subject to shareholder approval; proceeds to repay outstanding shareholder debt | `GUIDANCE`, forward corporate action |
| 104 | page 3 | 4 of 11 FY27-guided projects slated to launch in Q2 FY27 | `GUIDANCE` |
| 104-105 | page 3 | FY27 guidance: ~₹6,000 crore pre-sales from owned developments | `GUIDANCE` |
| 105 | page 3 | FY27 guidance: ₹2,000 crore from development management projects | `GUIDANCE` |
| 439 | page 13 | New launch GDV target INR 19.8k Cr for FY27 | `GUIDANCE` |
| 437-438 | page 13 | FY27 Pre Sales Target INR 6k Cr | `GUIDANCE` |
| 439-440 | page 13 | FY27 collections target INR 3k Cr | `GUIDANCE` |
| 443-444 | page 13 | FY27 Pre Sales target, DM Projects INR 2k Cr | `GUIDANCE` |
| 1010-1012 | page 32 | Disclaimer para 1: not a prospectus/offer/solicitation | `FLS_DISCLAIMER` |
| 1014-1016 | page 32 | Disclaimer para 2: not investment advice/recommendation | `FLS_DISCLAIMER` |
| 1018-1022 | page 32 | Disclaimer para 3: core forward-looking-statement risk-factor language (economic/political conditions, interest rates, regulation, merger delay, strategy execution risk) | `FLS_DISCLAIMER` |
| 1024-1030 | page 32 | Disclaimer para 4: no obligation to update FLS; no warranty on accuracy/completeness | `FLS_DISCLAIMER` |

Cross-reference (not double-counted as separate rows): Table 2C (page 14, New Launch Pipeline, FY27) and Table 2D (page 15, Future Developments, FY28+) are themselves forward pipeline disclosures; Table 2B's "Target OC" column (page 11) gives forward completion-year targets (FY2027-FY2035) for 12 projects.

---

## TABLE 9 — NOTES & GLOSSARY, PAGE 31 (line 945-1000)

### 9A. Note bullets (6 rows)
| # | Line | Note (first words) | Numeric content |
|---|---|---|---|
| 1 | 949 | All figures in this presentation are as of Jun 30, 2026, unless otherwise stated | date |
| 2 | 950 | Figures has been rounded off to nearest single decimal / integer... | rounding convention |
| 3 | 951 | Area (msf) represents unsold residential saleable area including commercial area sold on strata... | definitional |
| 4 | 952-955 | The Hon'ble NCLAT, New Delhi Bench, on January 7, 2025 approved the scheme of amalgamation of NAM and EOCPDPL with EDL... filed with RoC on January 24, 2025 | dates: Jan 7 2025 (NCLAT approval), Jan 24 2025 (RoC filing) |
| 5 | 956-960 | Following the merger, JVHPL and subsidiaries became largest shareholders (Promoter/Promoter Group); reverse acquisition under Ind AS 103; combined entity carries inventory INR 120,998 million and investment property INR 32,874 million as at March 31, 2025 | INR 120,998 million (inventory), INR 32,874 million (investment property), as at Mar 31, 2025 |
| 6 | 961-964 | Consolidated unaudited results represent continuation of NAM (accounting acquirer); NAM's 20 subsidiaries/JV and EDL's 174 subsidiaries; Q1FY26 (Jun 30, 2025), Q4FY25 (Mar 31, 2025) and Q1FY25 (Jun 30, 2024) not comparable | 20 subsidiaries/JV (NAM), 174 subsidiaries (EDL); 3 non-comparable quarters named |

### 9B. Glossary terms (56 rows, numbered 1-56, two-column layout lines 968-1000)
All 56 terms confirmed present on re-sweep (term 29 "MSF" wraps to line 1000, outside the initial regex window — corrected, see GATE A2 note above). Compact listing (term#: abbreviation — line):

1:INR(968) 2:Area Delivered(969-971) 3:AUM(972) 4:BLR(973) 5:CBSE(974) 6:Collections(975-976) 7:COO(977) 8:Cr(978) 9:CS(979) 10:CSR(980) 11:Debt-Equity Ratio(981) 12:DII(982) 13:DM(983) 14:EBITDA(984) 15:EDL(985) 16:FII(986) 17:Financial year/FY(987) 18:FPC(988) 19:FY(989) 20:GCC(990) 21:GDV(991) 22:IB(992) 23:Indian Stock Exchanges(993) 24:JV(994) 25:JDA(995) 26:K(996) 27:Leasable Area(997-998) 28:MMR/Mumbai Metropolitan Region(999) 29:MSF(1000) 30:MIDC(968) 31:MW(969) 32:NCLT(970) 33:NCR(971) 34:Near Completion Projects(972) 35:Net Debt(973) 36:OC(974) 37:Ongoing Projects(975) 38:PAT(976) 39:PBT(977) 40:Planned Projects(978) 41:PR(979) 42:Pre-sales(980-981) 43:PSF(982) 44:Q(983) 45:Q-o-Q(984) 46:REIT(985) 47:Saleable Area(986-988) 48:SEBI(989) 49:SEZ(990) 50:Sold Receivables(991-993) 51:Sq. Ft.(993) 52:Unsold Inventory(994-995) 53:Upcoming Projects(996) 54:Vizag(997) 55:Vs(998) 56:Y-o-Y(999)

---

## SUMMARY ROW TALLY

| Category | Rows |
|---|---|
| Slides (Table 1) | 33 |
| Structured table line items (Table 2) | 74 |
| KPI callouts (Table 3) | 92 |
| Chart data points (Table 4) | 30 |
| Cap table data points (Table 5) | 10 |
| Non-financial identifiers (Table 6) | 3 |
| Footnote definitions (Table 7) | 18 |
| Forward-looking statements / guidance (Table 8) | 12 |
| Notes bullets (Table 9A) | 6 |
| Glossary terms (Table 9B) | 56 |
| **Total enumerated disclosure/data units** | **334** |

`ZERO_STANDING` cells: 11 total (Table 2A x4, Table 2B x1, Table 2E x4, Table 2F x1; Table 2D row 10 GDV "Under evaluation" flagged separately as `NOT FOUND`, not counted as ZERO_STANDING since it is qualitative text, not a zero/nil/dash).

`EXTRACT_GAP_SUSPECTED`: pages 22 (Board of Directors) and 23 (Leadership Team) — titles only extracted, no director/leadership names, DIN, roles, or bios recovered; these two pages were not flagged for OCR by A1 despite a sparse-text profile matching page 28 (which was OCR'd). Flagged for A3/A4 attention: director-level disclosure (names, DIN, background, relationships per governance-quality checks) is not currently in the ledger for this doctype and may need to be sourced from the results filing extract instead.

`PRIOR_LEDGER_UNAVAILABLE`: no prior-quarter presentation ledger supplied; `DROPPED_SLIDE` diff test not performed this run.
