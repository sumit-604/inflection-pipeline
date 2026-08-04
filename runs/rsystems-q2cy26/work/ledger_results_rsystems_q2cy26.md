# A2 ENUMERATION LEDGER — R Systems International Limited (RSYSTEMS)
Quarter: Q2 CY2026 (quarter and six months ended June 30, 2026)
Doctype: results (Reg 30/33/52 Board Outcome + audited standalone / unaudited consolidated financial results)
Source: runs/rsystems-q2cy26/work/extract_results_rsystems_q2cy26.txt (1412 lines, 21 pages)
Prior-quarter ledger: NOT PROVIDED in this run's inputs — entity-list and line-item diffs against the prior quarter could not be performed; flags below based on in-document evidence only (e.g. "w.e.f." dates), not a cross-filing diff.

```
=== A2 COUNT TEST ===
category: agenda_items    grep_count: 8    sweep_count: 8    match: yes
category: notes           grep_count: 31   sweep_count: 31   match: yes
category: line_items      grep_count: 281  sweep_count: 281  match: yes
category: zero_standing   grep_count: 6    sweep_count: 6    match: yes  (subset of line_items)
category: auditor_paras   grep_count: 27   sweep_count: 27   match: yes
category: entities        grep_count: 31   sweep_count: 31   match: yes
category: signature_blocks grep_count: 15  sweep_count: 15   match: yes  (not a YAML-schema key; enumerated per rule 7)
gate_a2: pass
=== END COUNT TEST ===
```

## Reconciliation notes (how each count was built two ways)
- **notes**: Grep pass 1 (`^\s*[0-9]{1,2}\s` anchored within each of the 4 "Notes:" blocks) found 9 (consolidated main), 10 (standalone main) cleanly, but undercounted the two Reg 52(4)-ratio footnote blocks (2/3 and 0/3) because OCR dropped the leading superscript digit on note 1 in both blocks ("Earning for Debt Service..." lost its "1"; standalone block shows garbled "!" and ":ii!" markers). Grep pass 2 (non-blank-line count bounded by each "Notes:" header to the next page break) resolved this to 3 and 3. Combined numbered-notes count = 9+3+10+3 = 25. Separately grepped 4 asterisk-footnotes (lines 322, 520, 999, 1207) and 2 singular "Note:" footnotes (lines 522, 1212) = 6 unnumbered. Total 25+6 = 31, matching manual sweep of 31.
- **line_items**: Grepped each of the 10 financial tables independently for lines containing a decimal-formatted value (or NA) per row; cross-checked against a manual row-by-row read of each table. Table 5 (Consolidated Segment) initial grep returned 14 vs. manual 13 — reconciled: the 14th grep hit was the Note-5 asterisk footnote line (already counted under "notes"), not a table line item. All 10 tables reconciled exactly (see per-table counts in tables below); sum = 281.
- **zero_standing**: Grepped for all-six-column "NA" rows in both Annexure A ratio tables (Debenture redemption reserve, Inventory turnover ratio — 2 each = 4) and manually confirmed the two Non-Controlling-Interest profit/TCI-attribution rows in the Consolidated P&L are dash/nil in all periods presented (2). Total 6.
- **agenda_items**: Grepped `^\s*[0-9]\.` for the 3 top-level Board Outcome items and `^\s*[a-e]\.` for the 5 postal-ballot sub-resolutions = 8, matching manual sweep.
- **auditor_paras**: Grepped numbered paragraphs 1–6 in the consolidated review report (6) plus 4 unnumbered continuation paragraphs identified by opening phrase ("We also performed procedures...", "Certain of these subsidiaries...", two "Our conclusion... not modified..." sentences) = 10. Grepped the standalone audit report's 11 heading/paragraph openers (Opinion; Basis for Opinion; Management's and BOD's Responsibilities; going-concern paragraph; oversight paragraph; Auditor's Responsibilities heading; Objectives paragraph; "As part of an audit" intro; Materiality; Communication with governance; Independence statement) + 6 bullet points = 17. Total 10+17 = 27.
- **entities**: Grepped `^\s*[0-9]{1,2}\.\s+[A-Z]` in Annexure A of the auditor's review report = 31, matching the last numbered entry ("31. Novigo Solutions B.V.").
- **signature_blocks**: Grepped "Managing Director" (9 clean hits) + "Alka Chadha" (2) + manually confirmed 2 further MD&CEO signature blocks OCR-corrupted beyond grep recognition ("Managing Oiractor" on the Consolidated Cash Flow page, line 479; "\",1anc1ging Director" on the Standalone Cash Flow page, line 1168) + 1 Deloitte-stamp-only page with no MD&CEO line (Consolidated Annexure A ratios, line 331–334) + 1 Piyush Jain digital-signature block (Board Outcome letter) = 9+2+2+1+1 = 15.

---

## 1. BOARD OUTCOME — AGENDA ITEMS (8 rows)
Meeting: commenced 06:58 P.M., concluded 07:59 P.M. on August 04, 2026 (approx. 61 minutes) — L33.

| # | Item | Line | Flags |
|---|------|------|-------|
| 1 | Audited standalone financial results of the Company for quarter and six months ended June 30, 2026 | L36-37 | — |
| 2 | Unaudited consolidated financial results of the Company for quarter and six months ended June 30, 2026 | L38-39 | — |
| 3 | Postal Ballot Notice seeking shareholder approval (parent item, 5 sub-resolutions below) | L40-41 | — |
| 3a | Appointment of Mr. Shailesh Sharad Kekre (DIN 07679583) as Independent Director, 5-year term from June 29, 2026 | L42-43 | — |
| 3b | Appointment of Ms. Sangeeta Kapil Jit Singh (DIN 06920906) as Independent Director, 5-year term from June 29, 2026 | L44-45 | — |
| 3c | Appointment of Mr. Srikanth Balachandran (DIN 02815932) as Independent Director, 5-year term from June 29, 2026 | L46-47 | — |
| 3d | Appointment of Mr. Pranav Damani (DIN 11416778) as Non-Executive Non-Independent Director (no term stated) | L58-59 | — |
| 3e | Payment of remuneration by way of commission to Non-Executive Independent Directors | L60-61 | — |

Cross-reference (not a new agenda item, not double-counted): the letter separately lists "please find attached herewith" (1) audited standalone results with auditor's report, (2) unaudited consolidated results with limited-review report, at L69-75 — this is an enclosure list restating items 1 & 2, not a new resolution.

Note: the Postal Ballot Notice itself is stated to be "circulated separately" (L63-65) — its full content (record date, remote e-voting window, scrutinizer) is NOT FOUND in this extract because it is a separate document not attached to this filing.

---

## 2. NUMBERED NOTES (25 rows)

### 2a. Consolidated results — main Notes (after L190 "Notes:") — 9 notes
| Note | Line | First ~15 words |
|------|------|------------------|
| 1 | L191 | "The financial results for the quarter and six months ended June 30, 2026 have been prepared..." |
| 2 | L195 | "Additional disclosure as per Regulation 52(4) of SEBI... is set out in Annexure A." |
| 3 | L198-210 | "The Hon'ble NCLT... approved the Composite Scheme of Amalgamation of Velotio Technologies... and Scaleworx Technologies..." |
| 4 | L212-214 | "The transaction for sale of land, building and certain other assets located at Company's Noida office..." |
| 5 | L216-223 | "On November 21, 2025, the Government of India notified provisions of the Code on Wages, 2019..." |
| 6 | L225-232 | "With effect from January 01, 2026, the Company has designated certain foreign currency forward contracts as cash flow hedges..." |
| 7 | L235-236 | "During the quarter and six months ended June 30, 2026, the Company has allotted 10,627 and 89,106 equity shares..." |
| 8 | L238 | "Earnings per share for the quarter and six months ended June 30, 2026 and June 30, 2025... are not annualised." |
| 9 | L240-241 | "The Consolidated Balance Sheet, Consolidated Statement of Cash Flows and Consolidated Segment Information are set out in Annexure B, C, D." |

### 2b. Consolidated Reg 52(4) Annexure A — footnotes (after L323 "Notes:") — 3 notes (OCR dropped the leading digit on note 1)
| Note | Line | First ~15 words |
|------|------|------------------|
| 1 | L324 | "Earning for Debt Service = Net Profit for the period + Non-cash operating expenses" (superscript "1" lost to OCR) |
| 2 | L325 | "Debt service = Interest and lease payments + Scheduled principal repayments of term loans" |
| 3 | L326 | "Operating prorit [profit] = Profit before tax + Finance costs - Other income" |

### 2c. Standalone results — main Notes (after L828 "Notes:") — 10 notes
| Note | Line | First ~15 words |
|------|------|------------------|
| 1 | L829-832 | "The financial results for the quarter and six months ended June 30, 2026 have been prepared..." |
| 2 | L834-835 | "Additional disclosure as per Regulation 52(4)... is set out in Annexure A." |
| 3 | L837-858 | "The Hon'ble NCLT... approved the Composite Scheme of Amalgamation of Velotio Technologies... [with pooling-of-interest accounting and restatement of comparatives]" |
| 4 | L859-863 | "During the quarter ended March 31, 2026 the Company had received dividend income from its subsidiaries amounting to Rs. 140.60 million..." |
| 5 | L865-867 | "The transaction for sale of land, building and certain other assets located at Company's Noida office..." |
| 6 | L869-877 | "On November 21, 2025, the Government of India notified provisions of the Code on Wages, 2019..." |
| 7 | L879-888 | "With effect from January 01, 2026, the Company has designated certain foreign currency forward contracts as cash flow hedges..." |
| 8 | L890-892 | "During the quarter and six months ended June 30, 2026, the Company has allotted 10,627 and 89,106 equity shares..." |
| 9 | L894-895 | "Earnings per share for the quarter and six months ended June 30, 2026 and June 30, 2025... are not annualised." |
| 10 | L897-898 | "The Standalone Balance Sheet, Standalone Statement of Cash Flows and Standalone Segment Information are set out in Annexure B, C, D." |

### 2d. Standalone Reg 52(4) Annexure A — footnotes (after L1000 "Notes:") — 3 notes (OCR garbled markers "!" and ":ii!")
| Note | Line | First ~15 words |
|------|------|------------------|
| 1 | L1001 | "Earning for Debt Service = Net Profit for the period + Non-cash operating expenses" |
| 2 | L1003 | "Debt service = Interest and lease payments + Scheduled principal repayments of term loans" |
| 3 | L1005 | "Operating profit = Profit before tax + Finance costs - Other income" (numeral marker entirely dropped by OCR) |

---

## 3. UNNUMBERED FOOTNOTES (6 rows)
| Line | Location | Text (verbatim/first words) | Flag |
|------|----------|------------------------------|------|
| L322 | Consolidated Annexure A, row (d) | "Instrument entirely equity in nature - Optionally Convertible Redeemable Preference Share" (asterisk marker, OCR-garbled) | — |
| L520 | Consolidated Segment Annexure D | "Other unallocable expenses include Rs. 245.83 million towards impact of New Labour Codes for the year ended December 31, 2025. (refer to Note 5)" | — |
| L522-524 | Consolidated Segment Annexure D | "Note: Assets and liabilities of the Group are used interchangeably between segments... disclosure relating to segment assets and liabilities has not been provided." | — |
| L999 | Standalone Annexure A, row (d) | "Instrument entirely equity in nature - Optionally Convertible Redeemable Preference Share" (asterisk marker, OCR-garbled) | — |
| L1207 | Standalone Segment Annexure D | "Other unallocable expenses include Rs. 244.49 million towards impact of New Labour Codes for the year ended December 31, 2025. (refer to Note 6)" | — |
| L1212-1214 | Standalone Segment Annexure D | "Note: Assets and liabilities of the Company are used interchangeably between segments... disclosure relating to segment assets and liabilities has not been provided." | — |

---

## 4. ANNEXURE INDEX (9 distinct annexure sections)
| Annexure | Filing | Content | Line |
|----------|--------|---------|------|
| Annexure A | Consolidated | Reg 52(4) additional disclosure (debt/coverage ratios) | L260-334 |
| Annexure B | Consolidated | Consolidated Balance Sheet as at June 30, 2026 | L336-412 |
| Annexure C | Consolidated | Consolidated Statement of Cash Flows, six months ended June 30, 2026 | L415-483 |
| Annexure D | Consolidated | Consolidated Segment Information | L486-532 |
| Annexure A | Auditor's review report | List of Entities Consolidated (31 entities) | L656-744 |
| Annexure A | Standalone | Reg 52(4) additional disclosure (debt/coverage ratios) | L917-1015 |
| Annexure B | Standalone | Standalone Balance Sheet as at June 30, 2026 | L1018-1100 |
| Annexure C | Standalone | Standalone Statement of Cash Flows, six months ended June 30, 2026 | L1103-1169 |
| Annexure D | Standalone | Standalone Segment Information | L1172-1226 |

---

## 5. CONSOLIDATED P&L LINE ITEMS (30 rows; grep=30, sweep=30, match)
| Row | Label | Line | ZERO_STANDING? |
|-----|-------|------|-----------------|
| 1(a) | Revenue from operations | L115 | no |
| 1(b) | Other income (refer to Note 4) | L116 | no |
| — | Total income | L117 | no |
| 2(a) | Employee benefits expense | L119 | no |
| 2(b) | Finance costs | L120 | no |
| 2(c) | Depreciation and amortisation expense | L121 | no |
| 2(d) | Other expenses | L122 | no |
| — | Total expenses | L123 | no |
| 3 | Profit before exceptional item and tax (1-2) | L124 | no |
| 4 | Exceptional Item: Impact of New Labour Codes (refer to Note 5) | L129 | no (nil in Q/6M columns, 245.83 in year column — not standing-zero across all periods) |
| 5 | Profit before tax (3-4) | L130 | no |
| 6(a) | Current tax | L132 | no |
| 6(b) | Deferred tax expense/(credit) | L133 | no |
| — | Total tax expense | L134 | no |
| 7 | Profit for the period/year (5-6) | L135 | no |
| 8(a) | Re-measurements of the defined benefit plans | L139 | no |
| 8(b) | Tax relating to re-measurements of defined benefit plans | L140 | no |
| 8(a) | Fair value changes on derivatives designated as cash flow hedge (refer to Note 6) | L146 | no |
| 8(b) | Tax relating to fair value changes on derivatives designated as cash flow hedge | L150 | no |
| 8(c) | Foreign currency translation reserve | L152 | no |
| — | Total other comprehensive income/(loss) | L153 | no |
| 9 | Total comprehensive income for the period/year (7+8) | L154 | no |
| 10(a) | Profit attributable to: Equity shareholders of the company | L160 | no |
| 10(b) | Profit attributable to: Non-controlling interest | L159/161 | **YES — ZERO_STANDING** (dash/nil all periods) |
| 11(a) | Total comprehensive income attributable to: Equity shareholders of the company | L166 | no |
| 11(b) | Total comprehensive income attributable to: Non-controlling interest | L165/167 | **YES — ZERO_STANDING** (dash/nil all periods) |
| 12 | Paid-up equity share capital | L169 | no |
| 13 | Other equity (refer to Note 3) | L170 | no (annual-column-only disclosure per SEBI format, not standing-zero) |
| 14(a) | Earnings per share — Basic (refer to Note 7 and Note 8) | L173 | no |
| 14(b) | Earnings per share — Diluted | L174 | no |

---

## 6. CONSOLIDATED REG 52(4) ANNEXURE A — RATIOS (19 rows; grep=19, sweep=19, match)
| Row | Label | Line | ZERO_STANDING? |
|-----|-------|------|-----------------|
| (a) | Debt equity ratio (times) | L273 | no |
| (b) | Debt service coverage ratio (times) | L276 | no |
| (c) | Interest service coverage ratio (times) | L280 | no |
| (d) | Outstanding redeemable preference shares (Rs. mn) (refer to Note 3) | L283 | no |
| (e) | Capital Redemption Reserve (Rs. mn) | L285 | no |
| (f) | Debenture redemption reserve | L286 | **YES — ZERO_STANDING** (NA in all 6 columns) |
| (g) | Net worth (Rs. mn) | L287 | no |
| (h) | Net profit for the period/year (Rs. mn) | L288 | no |
| (i)-Basic | Earnings per share — Basic | L292 | no |
| (i)-Diluted | Earnings per share — Diluted | L293 | no |
| (j) | Current ratio (times) | L294 | no |
| (k) | Long term debt to working capital (times) | L296 | no |
| (l) | Bad debts to accounts receivable ratio (times) | L303 | no (dash in one of six columns only) |
| (m) | Current liability ratio (times) | L306 | no |
| (n) | Total debts to total assets ratio (times) | L309 | no |
| (o) | Debtors' turnover ratio (times) | L313 | no |
| (p) | Inventory turnover ratio | L317 | **YES — ZERO_STANDING** (NA in all 6 columns) |
| (q) | Operating margin (%) | L318 | no |
| (r) | Net profit margin (%) | L320 | no |

---

## 7. CONSOLIDATED BALANCE SHEET (42 rows; grep=42, sweep=42, match)
| Section | Label | Line |
|---------|-------|------|
| A(a) | Property, plant and equipment | L347 |
| A(b) | Capital work in progress | L348 |
| A(c) | Investment property | L349 |
| A(d) | Right-of-use assets | L350 |
| A(e) | Goodwill | L351 |
| A(f) | Other intangible assets | L352 |
| A(g)(i) | Investments | L354 |
| A(g)(ii) | Other financial assets | L355 |
| A(h) | Deferred tax assets (net) | L356 |
| A(i) | Non-current tax assets (net) | L357 |
| A(j) | Other non-current assets | L358 |
| — | Total non-current assets (A) | L359 |
| B(a)(i) | Trade receivables | L362 |
| B(a)(ii) | Cash and cash equivalents | L363 |
| B(a)(iii) | Bank balances other than cash and cash equivalents | L364 |
| B(a)(iv) | Other financial assets | L365 |
| B(b) | Other current assets | L366 |
| — | Total current assets (B) | L367 |
| — | Total assets (A+B) | L368 |
| A(a) | Equity share capital | L374 |
| A(b) | Instrument entirely equity in nature (refer to note 3) | L375 |
| A(c) | Other equity | L376 |
| — | Total equity attributable to equity shareholders of the Company | L377 |
| A(d) | Non-controlling interests | L378 |
| — | Total equity (A) | L379 |
| B(a)(i) | Borrowings (non-current) | L384 |
| B(a)(ii) | Lease liabilities (non-current) | L385 |
| B(a)(iii) | Other financial liabilities (non-current) | L386 |
| B(b) | Provisions (non-current) | L387 |
| B(c) | Deferred tax liabilities (net) | L388 |
| — | Total non-current liabilities (B) | L389 |
| C(a)(i) | Borrowings (current) | L392 |
| C(a)(ii) | Lease liabilities (current) | L393 |
| C(a)(iii) | Trade payables — micro/small enterprises | L395 |
| C(a)(iii) | Trade payables — other than micro/small enterprises | L397 |
| C(a)(iv) | Other financial liabilities (current) | L399 |
| C(b) | Other current liabilities | L400 |
| C(c) | Provisions (current) | L401 |
| C(d) | Current tax liabilities (net) | L402 |
| — | Total current liabilities (C) | L403 |
| — | Total liabilities (B+C) | L404 |
| — | Total equity and liabilities (A+B+C) | L405 |

No ZERO_STANDING rows in this table (Deferred tax liabilities shows 0.17→nil transition but is not zero in all periods).

---

## 8. CONSOLIDATED CASH FLOW (42 rows; grep=42, sweep=42, match)
| Section | Label | Line |
|---------|-------|------|
| A | Profit for the period | L424 |
| A-adj | Tax expense | L426 |
| A-adj | Depreciation and amortisation expense | L427 |
| A-adj | (Reversal)/Provision for doubtful debts (net) | L428 |
| A-adj | Provision for doubtful advances/other assets (net) | L429 |
| A-adj | Employee share based payment expense | L430 |
| A-adj | Unrealised foreign exchange gain | L431 |
| A-adj | Interest income | L432 |
| A-adj | Rental income from investment property | L433 |
| A-adj | Loss/(Profit) on sale/disposal of PP&E (net) | L436 |
| A-adj | (Profit)/Loss on discard of right-of-use assets | L437 |
| A-adj | Liability no longer required written back | L438 |
| A-adj | Interest expenses | L439 |
| — | Operating profit before working capital changes | L440 |
| A-wc | Decrease/(Increase) in trade receivables | L442 |
| A-wc | (Increase)/Decrease in other assets | L443 |
| A-wc | (Decrease)/Increase in provisions | L444 |
| A-wc | (Decrease)/Increase in trade payables and other liabilities | L445 |
| — | Cash generated from operations | L446 |
| A | Direct taxes paid, net of refunds | L447 |
| — | Net cash from operating activities (A) | L448 |
| B | Purchase of property, plant and equipment | L450 |
| B | Purchase of intangible assets | L451 |
| B | Proceeds from sale of PP&E (net of capital gain tax) (refer to Note 4) | L452 |
| B | Investment in fixed deposits | L453 |
| B | Proceeds from fixed deposits | L454 |
| B | Interest received | L455 |
| B | Rental income from investment property | L456 |
| — | Net cash (used in)/from investing activities (B) | L457 |
| C | Proceeds from long-term borrowings | L459 |
| C | Repayment of long-term borrowings | L460 |
| C | (Repayment of)/Proceeds from short-term borrowings (net) | L461 |
| C | Payment of lease rentals | L462 |
| C | Proceeds from other non-current assets | L463 |
| C | Proceeds from exercise of Restricted Stock Units (refer to Note 7) | L464 |
| C | Interest paid | L465 |
| C | Interim dividend paid | L466 |
| — | Net cash used in financing activities (C) | L467 |
| — | Net increase in cash and cash equivalents (A+B+C) | L468 |
| — | Add: Cash and cash equivalents at beginning of period | L469 |
| — | Add: Effect of exchange rate changes on cash held in foreign currency | L470 |
| — | Cash and cash equivalents at the end of the period | L471 |

No ZERO_STANDING rows.

---

## 9. CONSOLIDATED SEGMENT INFORMATION (13 rows; grep=14 raw / 13 net of footnote, sweep=13, match)
| Row | Label | Line |
|-----|-------|------|
| 1 | Segment revenue — Information technology services | L503 |
| 1 | Segment revenue — Knowledge services | L504 |
| 1 | Segment revenue — Total | L505 |
| 1 | Less: Elimination of intersegment sales | L506 |
| 1 | Revenue from operations | L507 |
| 2 | Segment results — Information technology services | L510 |
| 2 | Segment results — Knowledge services | L511 |
| 2 | Segment results — Total | L512 |
| 2(i) | Finance costs | L514 |
| 2(ii) | Interest income | L515 |
| 2(iii) | Other unallocable income (refer to Note 4) | L516 |
| 2(iv) | Other unallocable expenses* | L517 |
| 2 | Profit before tax | L518 |

Note: assets/liabilities not disclosed at segment level per Ind AS 108 (footnote L522-524, counted under Notes section 3, not a line item).

---

## 10. STANDALONE P&L LINE ITEMS (25 rows; grep=25, sweep=25, match)
| Row | Label | Line | ZERO_STANDING? |
|-----|-------|------|-----------------|
| 1(a) | Revenue from operations | L764 | no |
| 1(b) | Other income (refer to Note 4 and Note 5) | L765 | no |
| — | Total income | L767 | no |
| 2(a) | Employee benefits expense | L769 | no |
| 2(b) | Finance costs | L770 | no |
| 2(c) | Depreciation and amortisation | L771 | no |
| 2(d) | Other expenses | L772 | no |
| — | Total expenses | L773 | no |
| 3 | Profit before exceptional item and tax (1-2) | L774 | no |
| 4 | Exceptional Item: Impact of New Labour Codes (refer to Note 6) | L777 | no (nil Q/6M, 244.49 year column) |
| 5 | Profit before tax (3-4) | L779 | no |
| 6(a) | Current tax | L781 | no |
| 6(b) | Deferred tax expense/(credit) | L782 | no |
| — | Total tax expense | L783 | no |
| 7 | Profit for the period/year (5-6) | L784 | no |
| 8(a) | Re-measurements of the defined benefit plans | L790 | no |
| 8(b) | Tax relating to re-measurements of defined benefit plans | L792 | no |
| 8(a) | Fair value changes on derivatives designated as cash flow hedge (refer to Note 7) | L796 | no |
| 8(b) | Tax relating to fair value changes on derivatives designated as cash flow hedge | L799 | no |
| — | Total other comprehensive income/(loss) | L802 | no |
| 9 | Total comprehensive income for the period/year (7+8) | L804 | no |
| 10 | Paid-up equity share capital | L806 | no |
| 11 | Other equity (refer to Note 3) | L807 | no |
| 12(a) | Earnings per share — Basic (refer to Note 8 and Note 9) | L812 | no |
| 12(b) | Earnings per share — Diluted | L813 | no |

Note: standalone P&L has no NCI attribution rows (10-11 in consolidated) — consistent with a standalone (non-consolidated) filer.

---

## 11. STANDALONE REG 52(4) ANNEXURE A — RATIOS (19 rows; grep=19, sweep=19, match)
| Row | Label | Line | ZERO_STANDING? |
|-----|-------|------|-----------------|
| (a) | Debt equity ratio (times) | L928 | no |
| (b) | Debt service coverage ratio (times) | L932 | no |
| (c) | Interest service coverage ratio (times) | L938 | no |
| (d) | Outstanding redeemable preference shares (Rs. mn) (refer to Note 3) | L944 | no |
| (e) | Capital redemption reserve (Rs. mn) | L948 | no |
| (f) | Debenture redemption reserve | L949 | **YES — ZERO_STANDING** (NA all columns) |
| (g) | Net worth (Rs. mn) | L950 | no |
| (h) | Net profit for the period/year (Rs. mn) | L951 | no |
| (i)-Basic | Earnings per share — Basic | L956 | no |
| (i)-Diluted | Earnings per share — Diluted | L957 | no |
| (j) | Current ratio (times) | L958 | no |
| (k) | Long term debt to working capital (times) | L962 | no |
| (l) | Bad debts to accounts receivable ratio (times) | L970 | no |
| (m) | Current liability ratio (times) | L977 | no |
| (n) | Total debts to total assets ratio (times) | L981 | no |
| (o) | Debtors' turnover ratio (times) | L986 | no |
| (p) | Inventory turnover ratio | L991 | **YES — ZERO_STANDING** (NA all columns) |
| (q) | Operating margin (%) | L992 | no |
| (r) | Net profit margin (%) | L996 | no |

---

## 12. STANDALONE BALANCE SHEET (39 rows; grep=39, sweep=39, match)
| Section | Label | Line |
|---------|-------|------|
| A(a) | Property, plant and equipment | L1030 |
| A(b) | Capital work in progress | L1031 |
| A(c) | Investment property | L1032 |
| A(d) | Right-of-use assets | L1033 |
| A(e) | Goodwill | L1034 |
| A(f) | Other intangible assets | L1035 |
| A(g)(i) | Investments | L1037 |
| A(g)(ii) | Other financial assets | L1038 |
| A(h) | Deferred tax assets (net) | L1039 |
| A(i) | Non-current tax assets (net) | L1040 |
| A(j) | Other non-current assets | L1041 |
| — | Total non-current assets (A) | L1042 |
| B(a)(i) | Trade receivables | L1046 |
| B(a)(ii) | Cash and cash equivalents | L1047 |
| B(a)(iii) | Bank balances other than cash and cash equivalents | L1048 |
| B(a)(iv) | Other financial assets | L1049 |
| B(b) | Other current assets | L1050 |
| — | Total current assets (B) | L1051 |
| — | Total assets (A+B) | L1053 |
| A(a) | Equity share capital | L1058 |
| A(b) | Instruments entirely equity in nature (refer to Note 3) | L1059 |
| A(c) | Other equity | L1060 |
| — | Total equity (A) | L1061 |
| B(a)(i) | Borrowings (non-current) | L1070 |
| B(a)(ii) | Lease liabilities (non-current) | L1071 |
| B(a)(iii) | Other financial liabilities (non-current) | L1072 |
| B(b) | Provisions (non-current) | L1073 |
| — | Total non-current liabilities (B) | L1074 |
| C(a)(i) | Borrowings (current) | L1078 |
| C(a)(ii) | Lease liabilities (current) | L1079 |
| C(a)(iii) | Trade payables — micro/small enterprises | L1081 |
| C(a)(iii) | Trade payables — other than micro/small enterprises | L1083 |
| C(a)(iv) | Other financial liabilities (current) | L1085 |
| C(b) | Other current liabilities | L1086 |
| C(c) | Provisions (current) | L1087 |
| C(d) | Current tax liabilities (net) | L1088 |
| — | Total current liabilities (C) | L1089 |
| — | Total liabilities (B+C) | L1090 |
| — | Total equity and liabilities (A+B+C) | L1091 |

Note: standalone balance sheet has no NCI equity line and no deferred-tax-liabilities line under non-current liabilities (present in consolidated) — structural difference, not a missing disclosure.

---

## 13. STANDALONE CASH FLOW (41 rows; grep=41, sweep=41, match)
| Section | Label | Line |
|---------|-------|------|
| A | Profit for the period | L1115 |
| A-adj | Tax expense | L1117 |
| A-adj | Depreciation and amortisation expense | L1118 |
| A-adj | Provision for doubtful debts (net) | L1119 |
| A-adj | Employee share based payment expense | L1120 |
| A-adj | Unrealised foreign exchange gain | L1121 |
| A-adj | Interest income | L1122 |
| A-adj | Rental income from investment property | L1123 |
| A-adj | Profit on sale/disposal of PP&E (net) | L1124 |
| A-adj | Dividend income (refer to Note 4) | L1125 |
| A-adj | Interest expenses | L1126 |
| — | Operating profit before working capital changes | L1127 |
| A-wc | (Increase)/Decrease in trade receivables | L1129 |
| A-wc | (Increase)/Decrease in other assets | L1130 |
| A-wc | Increase/(Decrease) in provisions | L1131 |
| A-wc | Increase/(Decrease) in trade payables and other liabilities | L1132 |
| — | Cash generated from operations | L1133 |
| A | Direct taxes paid, net of refunds | L1134 |
| — | Net cash from operating activities (A) | L1135 |
| B | Purchase of property, plant and equipment | L1137 |
| B | Purchase of intangible assets | L1138 |
| B | Proceeds from sale of PP&E (net of capital gain tax) (refer to Note 5) | L1139 |
| B | Investment in fixed deposits with scheduled banks | L1141 |
| B | Proceeds from fixed deposits with scheduled banks | L1142 |
| B | Interest received | L1143 |
| B | Rental income from investment property | L1144 |
| B | Dividend income (refer to Note 4) | L1145 |
| — | Net cash from investing activities (B) | L1146 |
| C | Proceeds from long-term borrowings | L1148 |
| C | Repayment of long-term borrowings | L1149 |
| C | (Repayment of)/Proceeds from short-term borrowings (net) | L1150 |
| C | Proceeds from margin money deposits | L1151 |
| C | Payment of lease rentals | L1152 |
| C | Proceeds from exercise of Restricted Stock Units (refer to Note 8) | L1153 |
| C | Interest paid | L1154 |
| C | Interim dividend paid | L1155 |
| — | Net cash used in financing activities (C) | L1156 |
| — | Net increase in cash and cash equivalents (A+B+C) | L1157 |
| — | Add: Cash and cash equivalents at beginning of period | L1158 |
| — | Add: Effect of exchange rate changes on cash held in foreign currency | L1159 |
| — | Cash and cash equivalents at the end of the period | L1161 |

No ZERO_STANDING rows.

---

## 14. STANDALONE SEGMENT INFORMATION (11 rows; grep=11, sweep=11, match)
| Row | Label | Line |
|-----|-------|------|
| 1 | Segment revenue — Information technology services | L1190 |
| 1 | Segment revenue — Knowledge services | L1191 |
| 1 | Revenue from operations | L1192 |
| 2 | Segment results — Information technology services | L1198 |
| 2 | Segment results — Knowledge services | L1199 |
| 2 | Segment results — Total | L1200 |
| 2(i) | Finance costs | L1201 |
| 2(ii) | Interest income | L1202 |
| 2(iii) | Other unallocable income (refer to Note 4 and Note 5) | L1203 |
| 2(iv) | Other unallocable expenses* | L1205 |
| 2 | Profit before tax | L1206 |

Note: standalone segment table has no "Total" or "Less: elimination" row for segment revenue (structural, standalone has no intersegment eliminations, unlike consolidated).

---

## 15. ENTITIES CONSOLIDATED (31 rows) — Annexure A to auditor's review report (L656-744)
| # | Entity | Relationship | Line | Flag |
|---|--------|--------------|------|------|
| 1 | R Systems International Limited | Parent | L660 | — |
| 2 | R Systems, Inc. ("RSI") | Wholly owned subsidiary of Parent | L662 | — |
| 3 | R Systems Technologies Limited | Wholly owned subsidiary of Parent | L664 | — |
| 4 | RSYS Technologies Ltd. | Wholly owned subsidiary of Parent | L666 | — |
| 5 | R Systems Computaris International Limited ("RCIL") | Wholly owned subsidiary of Parent | L668 | — |
| 6 | R Systems Computaris S.R.L. | Wholly owned subsidiary of RCIL | L670 | — |
| 7 | R Systems Computaris Malaysia Sdn. Bhd. | Wholly owned subsidiary of RCIL | L672 | — |
| 8 | R Systems Computaris Poland Sp. Z 0.0. | Wholly owned subsidiary of RCIL | L674 | — |
| 9 | R Systems Computaris Europe S.R.L. | Wholly owned subsidiary of RCIL | L676 | — |
| 10 | R Systems Computaris Philippines Pte. Ltd. Inc. | Wholly owned subsidiary of RCIL | L678 | — |
| 11 | R Systems Computaris Suisse Sarl | Wholly owned subsidiary of RCIL | L680 | — |
| 12 | R Systems (Singapore) Pte Limited ("RSS") | Wholly owned subsidiary of Parent | L682 | — |
| 13 | R Systems IBIZCS Pte. Ltd. ("IBIZCS") | Wholly owned subsidiary of RSS | L684 | — |
| 14 | R Systems IBIZCS Sdn. Bhd. | Wholly owned subsidiary of IBIZCS | L686 | — |
| 15 | PT R Systems IBIZCS International | Wholly owned subsidiary of IBIZCS | L688 | — |
| 16 | IBIZ Consulting Services Limited ("IBIZ HK") | Wholly owned subsidiary of IBIZCS | L690 | — |
| 17 | IBIZ Consulting Services (Shanghai) Co., Ltd. | Wholly owned subsidiary of IBIZ HK | L692 | — |
| 18 | IBIZ Consulting (Thailand) Co., Ltd. | Wholly owned subsidiary of IBIZCS | L694 | — |
| 19 | R Systems Consulting Services Limited ("RSCSL") | Subsidiary of Parent (not stated "wholly owned") | L696 | — |
| 20 | R Systems Consulting Services (M) Sdn. Bhd. | Wholly owned subsidiary of RSCSL | L698 | — |
| 21 | R Systems Consulting Services (Hong Kong) Limited | Wholly owned subsidiary of RSCSL | L700 | — |
| 22 | R Systems Consulting Services (Thailand) Co., Ltd. | Wholly owned subsidiary of RSCSL | L702 | — |
| 23 | R Systems Consulting Services Kabushiki Kaisha | Wholly owned subsidiary of RSCSL | L704 | — |
| 24 | R Systems Consulting Services (Shanghai) Co., Ltd. | Wholly owned subsidiary of RSCSL | L706 | — |
| 25 | R Systems Consulting Services Company Limited | Wholly owned subsidiary of RSCSL | L708 | — |
| 26 | RSIL Mexico, S. de R.L. de C.V. | Wholly owned subsidiary of Parent | L720 | — |
| 27 | Novigo Solutions Private Limited ("Novigo") | Subsidiary of Parent, w.e.f. 13 November 2025 (not stated "wholly owned") | L722 | ENTITY_CHANGE (recent addition per in-doc date) |
| 28 | Novigo Solutions Inc | Wholly owned subsidiary of Novigo, w.e.f. 13 November 2025 | L724 | ENTITY_CHANGE |
| 29 | Novigo Solutions Limited | Wholly owned subsidiary of Novigo, w.e.f. 13 November 2025 | L726 | ENTITY_CHANGE |
| 30 | Novigo for Information Technology | Wholly owned subsidiary of Novigo, w.e.f. 13 November 2025 | L728 | ENTITY_CHANGE |
| 31 | Novigo Solutions B.V. | Wholly owned subsidiary of Novigo, w.e.f. 13 November 2025 | L731 | ENTITY_CHANGE |

Additional entity-status event (not on the 31-entity list but structurally relevant — flag **ENTITY_CHANGE**): per Note 3 (both filings, L198-210 consolidated / L837-858 standalone), Velotio Technologies Private Limited and Scaleworx Technologies Private Limited were amalgamated INTO R Systems International Limited under an NCLT-approved Composite Scheme (order dated April 16, 2026, effective May 1, 2026, appointed date April 1, 2024); standalone comparatives were restated for the pooling-of-interest accounting. These two entities do not appear as separate lines in the consolidation list because they have ceased to exist as separate legal entities — this is a positive/expected absence, not a miss, but is flagged because it is a material entity-structure change this quarter (retrospective restatement of prior-period standalone comparatives).

Caveat: PRIOR_LEDGER_PATH was not supplied to this run, so the above ENTITY_CHANGE flags are based on in-document "(w.e.f. 13 November, 2025)" annotations and the Note 3 narrative, not a line-by-line diff against the prior quarter's entity list. A3/A4 should confirm against the Q1 CY2026 (or Q4 CY2025) filing whether the Novigo entities already appeared last quarter.

---

## 16. AUDITOR REPORT PARAGRAPHS — CONSOLIDATED REVIEW REPORT (10 rows; L549-645)
Report type: Independent Auditor's Review Report on Review of Interim Consolidated Financial Results (SRE 2410, limited review — not an audit). Conclusion: unmodified ("nothing has come to our attention... has not disclosed the information required... or that it contains any material misstatement"). No Emphasis of Matter paragraph. Has Other Matters content (paras 4 and 6). No explicit Going Concern paragraph in this report.

| # | Paragraph | Line |
|---|-----------|------|
| 1 | Scope statement — reviewed the Statement of Consolidated Unaudited Financial Results | L555-559 |
| 2 | Responsibility statement — Statement is Parent Management's responsibility, approved by Parent's Board | L561-566 |
| 3 | Basis of review — SRE 2410, review substantially less in scope than audit, no audit opinion expressed | L568-575 |
| 3-cont | Additional SEBI Regulation 33(8) circular procedures performed | L577-579 |
| 4 | Other Matters — Statement includes results of entities listed in Annexure A | L581 |
| 5 | Conclusion — unmodified, based on review and other auditors' review reports | L583-590 |
| 6 | Other Matters — did not review 21 subsidiaries; total assets Rs.3,020.85mn, revenues Rs.1,605.36mn(Q)/Rs.3,119.30mn(6M), PAT Rs.114.58mn(Q)/Rs.147.96mn(6M), TCI Rs.76.81mn(Q)/Rs.103.18mn(6M), net cash flows Rs.81.27mn(6M) — reviewed by other auditors, furnished to principal auditor by Management | L592-615 |
| 6-cont | Certain subsidiaries located outside India — converted to Indian GAAP by Parent management, conversion adjustments reviewed by principal auditor | L617-626 |
| 6-cont | "Our conclusion... is not modified in respect of this matter" (foreign-subsidiary conversion) | L626 |
| 6-cont | "Our conclusion... is not modified in respect of our reliance on the interim financial information certified by the Management" | L628-629 |

Signature: Alka Chadha, Partner, Membership No. 93474, For Deloitte Haskins & Sells LLP (Firm Reg. No. 117366W/W-100018), UDIN 26093474PAFJDT8742, Place Greater Noida, Date August 4, 2026 — L632-645.

---

## 17. AUDITOR REPORT PARAGRAPHS — STANDALONE AUDIT REPORT (17 rows; L1247-1407)
Report type: Independent Auditor's Report on Audit of Interim Standalone Financial Results (full audit under SA, Section 143(10)). Opinion: unmodified/unqualified — results "are presented in accordance with... Regulation 33 and 52" and "give a true and fair view." No Emphasis of Matter or Other Matters paragraph identified in this report (no reference to unaudited components — standalone entity only).

| # | Paragraph/heading | Line |
|---|---------------------|------|
| 1 | Opinion (incl. sub-clauses (i) presentation compliance and (ii) true-and-fair view) | L1253-1271 |
| 2 | Basis for Opinion | L1273-1283 |
| 3 | Management's and Board of Directors' Responsibilities for the Statement (heading + main content) | L1285-1301 |
| 4 | Going concern responsibility ("In preparing the Standalone Financial Results, the Board...") | L1319-1322 |
| 5 | Board also responsible for overseeing financial reporting process | L1324 |
| 6 | Auditor's Responsibilities for audit heading + scope statement | L1326-1335 |
| 7 | "As part of an audit in accordance with SAs, we exercise professional judgment..." (intro to bullets) | L1337-1338 |
| 7a (bullet 1) | Identify and assess risks of material misstatement | L1340-1344 |
| 7b (bullet 2) | Obtain understanding of internal control | L1346-1349 |
| 7c (bullet 3) | Evaluate appropriateness of accounting policies and estimates | L1350-1351 |
| 7d (bullet 4) | Evaluate appropriateness/reasonableness of disclosures | L1353-1354 |
| 7e (bullet 5) | Conclude on going concern basis of accounting | L1356-1362 |
| 7f (bullet 6) | Evaluate overall presentation, structure and content | L1364-1366 |
| 8 | Materiality statement | L1368-1372 |
| 9 | Communication with those charged with governance — scope and timing | L1374-1376 |
| 10 | Independence statement — compliance with ethical requirements | L1388-1390 |

Signature: For Deloitte Haskins & Sells LLP, Chartered Accountants (Firm Reg. No. 117366W/W-100018), Alka Chadha, Partner, Membership No. 93474, UDIN 26093474MNSQFR2592, Place Greater Noida, Date August 4, 2026 — L1394-1407.

Cross-check: same partner (Alka Chadha, Membership 93474) signed both reports with two distinct UDINs (26093474PAFJDT8742 for consolidated review; 26093474MNSQFR2592 for standalone audit) — expected practice for two separate reports, not a flag.

---

## 18. SIGNATURE / IDENTIFICATION BLOCKS (15 rows)
| # | Location | Signatory / Stamp | Designation | Timestamp | Line |
|---|----------|--------------------|-----|-----------|------|
| 1 | Board Outcome letter | Piyush Jain (digitally signed) | Company Secretary & Compliance Officer | NOT FOUND (date-only: August 04, 2026; no time-of-day captured in extract) | L84-90 |
| 2 | Consolidated P&L page | Nitesh Bansal (MD&CEO, DIN 10170738) + Deloitte "For Identification Only" stamp | Managing Director & CEO | Date only (Aug 4, 2026, no time) | L181-188 |
| 3 | Consolidated Notes page | MD&CEO signature + Deloitte "For Identification Only" stamp | Managing Director & CEO | Place Greater Noida, Date Aug 4, 2026 | L245-257 |
| 4 | Consolidated Annexure A (ratios) | Deloitte "For Identification Only" stamp only — no MD&CEO line on this page | — | — | L331-334 |
| 5 | Consolidated Balance Sheet | MD&CEO signature + Deloitte identification stamp | Managing Director & CEO | — | L406-412 |
| 6 | Consolidated Cash Flow | MD&CEO signature (OCR-garbled "Managing Oiractor") + Deloitte "For Identification Only" stamp | Managing Director & CEO | — | L476-483 |
| 7 | Consolidated Segment | Nitesh Bansal signature + "For Identification Only" + Deloitte stamp | Managing Director & CEO | — | L526-532 |
| 8 | Consolidated auditor's review report | Alka Chadha, Partner | Partner, Deloitte Haskins & Sells LLP | Place Greater Noida, Date Aug 4, 2026, UDIN 26093474PAFJDT8742 | L632-645 |
| 9 | Standalone P&L page | MD&CEO signature + Deloitte "For Identification Only" stamp | Managing Director & CEO | — | L820-825 |
| 10 | Standalone Notes page | "For and on behalf of Board" + MD&CEO signature (Nitesh Bansal) + Deloitte stamp | Managing Director & CEO | Place Greater Noida, Date Aug 4, 2026 | L902-914 |
| 11 | Standalone Annexure A (ratios) | MD&CEO signature (DIN cited) + Deloitte stamp | Managing Director & CEO | — | L1010-1015 |
| 12 | Standalone Balance Sheet | MD&CEO signature + Deloitte stamp | Managing Director & CEO | — | L1096-1100 |
| 13 | Standalone Cash Flow | MD&CEO signature (OCR-garbled "\",1anc1ging Director") — no "For Identification Only" text captured on this page | Managing Director & CEO | — | L1165-1169 |
| 14 | Standalone Segment | Nitesh Bansal signature + Deloitte stamp | Managing Director & CEO | — | L1216-1226 |
| 15 | Standalone audit report | Alka Chadha, Partner | Partner, Deloitte Haskins & Sells LLP | Place Greater Noida, Date Aug 4, 2026, UDIN 26093474MNSQFR2592 | L1394-1407 |

Assessment: cannot determine whether any signature timestamp precedes the 07:59 P.M. board meeting conclusion — the extract captures dates only, no time-of-day, for every signature/stamp block. Not flagged as an anomaly; flagged as a data-capture limit for A3/A4 awareness.

---

## SUMMARY OF FLAGS RAISED
- **ZERO_STANDING** (6 instances): Consolidated P&L rows 10(b) and 11(b) Non-controlling interest attribution (L159/161, L165/167); Consolidated Annexure A ratios (f) Debenture redemption reserve and (p) Inventory turnover ratio (L286, L317); Standalone Annexure A ratios (f) Debenture redemption reserve and (p) Inventory turnover ratio (L949, L991).
- **ENTITY_CHANGE** (6 instances, in-document evidence only, no prior-ledger diff available): 5 Novigo group entities (#27-31, L722-731) tagged "w.e.f. 13 November, 2025"; plus the Velotio Technologies / Scaleworx Technologies amalgamation into the Parent (NCLT order April 16, 2026, effective May 1, 2026, appointed date April 1, 2024, standalone comparatives restated) per Note 3 in both filings.

No MGMT_ABSENCE, REPEAT_QUESTION, or DROPPED_SLIDE flags — not applicable to this doctype (results filing, not concall/presentation).
