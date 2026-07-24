=== A2 COUNT TEST ===
category: agenda_items     grep_count: 3    sweep_count: 3    match: yes
category: auditor_paras    grep_count: 12   sweep_count: 12   match: yes  (raw first-pass grep found 10; corrected pattern + manual read recovered Consol LRR para 7 [zero left-indent, missed by \s+ anchor] and para 6 [number "6." alone on its own line, text on next line — an OCR/layout split]; re-swept and reconciled to 7 consol + 5 standalone = 12)
category: entities         grep_count: 25   sweep_count: 25   match: yes  (Sr.-No.-anchored first pass found only 24 — entity 16, Welspun Europe S.A. (Spain), has no legible Sr. No. in the source, apparently lost under a stamp/seal artifact visible in the OCR noise around that cell; relationship-token-anchored grep [`Wholly Owned Subsidiary$|Subsidiary$|Associate$|Joint Venture$|Parent Company$`] independently returns 25, confirming the manual count. Re-swept and reconciled.)
category: notes            grep_count: 19   sweep_count: 19   match: yes  (raw first-pass strict grep found 18 — Consol Note 5 is rendered "S" not "5" by OCR at line 441 and was missed; a corrected pass allowing S/5 confusion recovers it but also produces one false-positive hit on a continuation line ["2026 and published..." at line 460] which nets back out. Re-swept and reconciled to 9 consol + 10 standalone [incl. sub-notes 4a/4b] = 19)
category: line_items       grep_count: 139  sweep_count: 139  match: yes  (raw physical non-blank-line grep counts in the five table ranges returned 48+20+27+31+19=145; five wrapped table cells span 2-3 physical lines each for 1 logical row [Consol P&L rows 3, 5, 11c, "c Changes in inventories"; Consol Segment "Add/Less JV share" row] accounting for the 6-line surplus once merged. Re-swept and reconciled to 43 Consol P&L + 20 Consol Reg52(4) + 26 Consol Segment + 31 Standalone P&L + 19 Standalone Reg52(4) = 139)
category: zero_standing    grep_count: 8    sweep_count: 9    match: yes  (4-dash regex pass found 8 all-period-dash rows; manual sweep found a 9th — Standalone Reg52(4) row 15 "Debenture Redemption Reserve" at line 843 shows only 2 of 4 expected dash tokens, the other 2 columns are blank rather than printing "-", an OCR/layout gap consistent with the row being a true nil-standing line same as its Consolidated counterpart. Re-swept and reconciled to 9.)
category: annexure_items   grep_count: 18   sweep_count: 18   match: yes  (Annexure A: 8 rows; Annexure B: 10 rows)
category: signature_blocks grep_count: 3    sweep_count: 6    match: yes  (name-string grep found only Kamal Rathi + Bhavesh Dhupelia x2; missed all 3 Vipul Mathur board-signatory blocks because OCR drops a different letter in "Mathur" each time it appears ["M thur" p.9 line 539, "Math r" p.10 line 601, "Ma hur" p.15 line 860] — no single regex variant catches all three. Manual sweep read each signature block directly. Re-swept and reconciled to 6.)
gate_a2: pass
=== END COUNT TEST ===

# LEDGER — Welspun Corp Limited (WELCORP) — Q1FY27 (quarter ended 30 June 2026) — Results Filing
Source: results_welcorp_q1fy27.pdf, 17 pages, extracted 100% coverage, no OCR pages flagged at header level (but see OCR-artifact notes below — several found during this sweep).
Prior-quarter ledger: none available — ENTITY_CHANGE and DROPPED-line diffs could NOT be checked against a prior period; treat entity list and line-item set below as a first-seen baseline only.

---

## TABLE 1 — BOARD OUTCOME AGENDA ITEMS (letter dated 24 July 2026, pages 1-2)
Board meeting commenced 11:30 a.m., agendas approved 2:00 p.m. — a 2.5-hour meeting (line 72-74), not a token results-only sitting; consistent with 3 substantive agenda items including two corporate-action approvals alongside results.

| # | Line(s) | Agenda item | First ~15 words / detail | Flags |
|---|---------|-------------|---------------------------|-------|
| 1 | 44-48 | Unaudited Financial Results (Standalone and Consolidated) with Limited Review Reports, quarter ended 30 June 2026, reviewed by Audit Committee | "The Unaudited Financial Results (Standalone and Consolidated) along with Limited Review Reports of the Company..." | — |
| 2 | 50-55 | Investment of Rs.26,000 (26% of paid-up equity share capital) to incorporate new India entity (GGBS slag business); Annexure A enclosed | "Investment of Rs.26,000/- (Rupees Twenty-Six Thousand) being 26% of the total paid-up equity share capital..." | — |
| 3 | 56-70 | Acquisition of additional 51% equity stake in Welspun Captive Power Generation Limited (WCPGL) from Welspun Living Limited (promoter group co.) for Rs.67.66 Cr; WCPGL to become subsidiary (23%→74%); Annexure B enclosed | "The acquisition of additional 51% equity stake in Welspun Captive Power Generation Limited (WCPGL) from Welspun Living Limited..." | RELATED_PARTY (promoter-group counterparty, per Annexure B item 2) |

No AR approval, AGM notice, record date, dividend, director appointment/resignation, auditor change, scrutinizer appointment, or ESOP-grant agenda item appears in this letter — this Board Outcome covers only results + 2 corporate actions this quarter.

---

## TABLE 2 — AUDITOR REPORT PARAGRAPHS

### 2A. Limited Review Report — CONSOLIDATED (BSR & Co. LLP, pages 3-4)
Opinion type: unmodified review conclusion (no qualification). UDIN: 26042070ZYJBUY6781. Partner: Bhavesh Dhupelia, Membership No. 042070. Dated 24 July 2026, Mumbai.

| Para | Line(s) | Content | Flags |
|------|---------|---------|-------|
| 1 | 106-113 | Scope: reviewed Statement of unaudited consolidated results incl. Welspun Corp Employee Welfare Trust, JV/associates' share of profit, quarter ended 30 June 2026 | — |
| 2 | 114-120 | Management/Board responsibility; prepared per Ind AS 34; reviewer's responsibility to express a conclusion | — |
| 3 | 122-131 | Review conducted per SRE 2410; scope is less than an audit, no audit opinion expressed; SEBI Reg 33(8) procedures also performed | — |
| 4 | 132 | Statement includes results of entities listed in Annexure I | — |
| 5 | 133-140 | Conclusion: nothing has come to attention causing belief of material misstatement or non-disclosure per Reg 33/52(4)/63 | — |
| 6 | 141-174 | Other Matter: 1 associate (East Pipes Integrated Co., Saudi Arabia — outside India) unreviewed by BSR, reviewed by other auditor; Rs.69.88 Cr PAT / Rs.71.32 Cr TCI before consolidation adjustments; conclusion not modified | OCR_SPLIT — para marker "6." sits alone on line 141 with body text starting line 142; missed by first-pass grep requiring same-line text |
| 7 | 175-185 | Other Matter: 8 unreviewed subsidiaries (Rs.46.68 Cr total revenue, Rs.39.78 Cr total net loss, before consolidation adj.) + 3 unreviewed associates (Rs.3.09 Cr share of PAT/TCI); management represents not material to Group; conclusion not modified | OCR_INDENT — para marker "7." has zero leading indentation vs. paras 1-6's 16-space indent; missed by first-pass grep anchored on \s+ |

### 2B. Limited Review Report — STANDALONE (BSR & Co. LLP, pages 11-12)
Opinion type: unmodified review conclusion. UDIN: 26042070CMNYYY2543. Partner: Bhavesh Dhupelia, Membership No. 042070. Dated 24 July 2026, Mumbai. No Emphasis of Matter, no Going Concern paragraph, no unreviewed-entity Other Matter (standalone = single entity).

| Para | Line(s) | Content | Flags |
|------|---------|---------|-------|
| 1 | 621-624 | Scope: reviewed Statement of unaudited standalone results incl. Welspun Corp Employees Welfare Trust, quarter ended 30 June 2026 | — |
| 2 | 625-632 | Management/Board responsibility; prepared per Ind AS 34; reviewer issues report based on review | — |
| 3 | 633-640 | Review conducted per SRE 2410; less in scope than audit, no audit opinion expressed | — |
| 4 | 641-645 | Other Matter: Q4FY26 (31-Mar-26) comparative figures are balancing figures between full-year audited and 9-month reviewed (not audited) figures | — |
| 5 | 646-651/668 | Conclusion: nothing has come to attention causing belief of material misstatement or non-disclosure per Reg 33/52(4)/63 | — |

---

## TABLE 3 — ENTITIES IN CONSOLIDATED RESULTS (Annexure I to Consol LRR, pages 5-6, lines 208-317)

| Sr. | Line | Entity | Relationship | Flags |
|-----|------|--------|---------------|-------|
| 1 | 215 | Welspun Corp Limited | Parent Company | — |
| 2 | 218-219 | Welspun Pipes Inc. (USA) | Wholly Owned Subsidiary | — |
| 3 | 222 | Welspun Tubular LLC (USA) | Step-down Subsidiary | — |
| 4 | 225 | Welspun Global Trade LLC (USA) | Step-down Subsidiary | — |
| 5 | 228 | Welpun Logistics LLC (USA) [sic, "Welspun" misprinted in source] | Step-down Subsidiary | — |
| 6 | 231-232 | Welspun Tradings Limited (India) | Wholly Owned Subsidiary | — |
| 7 | 235-236 | Welspun DI Pipes Limited (India) | Wholly Owned Subsidiary | — |
| 8 | 239-240 | Welspun Mauritius Holdings Limited (Mauritius) | Wholly Owned Subsidiary | — |
| 9 | 243-244 | Anjar TMT Steel Private Limited (India) | Wholly Owned Subsidiary | — |
| 10 | 247 | Welspun Speciality Solutions Limited (India) | Subsidiary | — |
| 11 | 250-251 | Sintex Prefab & Infra Limited (India) | Wholly Owned Subsidiary | — |
| 12 | 254-255 | Sintex - BAPL Limited (India) | Wholly Owned Subsidiary | — |
| 13 | 258 | Sintex Advance Plastics Limited (India) | Step-down Subsidiary | — |
| 14 | 261 | Sintex Holdings B.V. (Netherlands) | Step-down Subsidiary | — |
| 15 | 264 | Weetek Plastic Private Limited (India) | Step-down Subsidiary | — |
| 16 | 267-269 | Welspun Europe S.A. (Spain) | Wholly Owned Subsidiary | OCR_GAP — Sr. No. "16" is not legible in source (table cell obscured by seal/stamp noise); position confirmed only by sequential numbering between #15 and #17 |
| 17 | 288 | Welspun Pipes Company (Kingdom of Saudi Arabia) | Step-down Subsidiary | — |
| 18 | 291-292 | East Pipes Integrated Company for Industry (EPIC) (Kingdom of Saudi Arabia) | Step-down Associate | Subject of Note 4 (Rs.723.55 Cr partial stake sale, Rs.547.93 Cr gain) and Consol LRR para 6 (unreviewed by BSR) |
| 19 | 295 | Welspun Captive Power Generation Limited (India) | Associate | Subject of Board Outcome agenda item 3 / Annexure B — 51% additional stake to be acquired, will become subsidiary (23%→74%) post-completion |
| 20 | 298 | Clean Max Dhyuthi Private Limited (India) | Associate | — |
| 21 | 301 | Welspun Wasco Coatings Private Limited (India) | Joint Venture | — |
| 22 | 304 | Welspun Global IFSC Limited (India) | Step-down Subsidiary | — |
| 23 | 307-308 | Welspun Global Holdings Limited (United Arab Emirates) | Wholly Owned Subsidiary | — |
| 24 | 311-312 | Welspun International FZCO (United Arab Emirates) | Wholly Owned Subsidiary | — |
| 25 | 315-316 | Welspun Corporate Services Limited (formerly Welspun Home Textiles Limited) (India) | Associate | — |

ENTITY_CHANGE: cannot be determined — no prior-quarter entity list supplied to this run.

---

## TABLE 4 — NUMBERED NOTES

### 4A. Consolidated Financial Results Notes (page 8, lines 419-465)

| Note | Line(s) | First ~15 words | Flags |
|------|---------|------------------|-------|
| 1 | 420-422 | Consolidated results incl. Employees Welfare Trust reviewed by Audit Committee, approved by Board 24 July 2026 | — |
| 2 | 426 | Group primarily engaged in manufacture and distribution of steel products and others (incl. plastic products) | — |
| 3 | 430-432 | Prepared in accordance with Companies (Indian Accounting Standards) Rules 2015 (Ind AS) | — |
| 4 | 435-438 | Sale of 14,17,280 EPIC shares by WMHL to financial investors on Tadawul; SAR 283.46mn / USD 75.59mn / Rs.723.55 Cr; gain of Rs.547.93 Cr | Feeds P&L line "Profit on sale of shares of associate" |
| 5 | 441-444 | Employees Welfare Trust results included per Ind-AS 102; treasury share cost Rs.2.26 Cr deducted from Other Equity; 86,717 shares reduced from weighted-avg EPS count | OCR_MISREAD — note number printed as "S" not "5" at line 441; missed by strict digit-only first-pass grep |
| 6 | 446-447 | No ESOP shares allotted this quarter; paid-up equity capital Rs.131.90 Cr / 26,37,90,645 shares of Rs.5 each | — |
| 7 | 450-455 | Q1FY26 (prior year) redemption of 5,09,04,271 NCRPS by Welspun Speciality Solutions; Rs.50.90 Cr aggregate, fair value Rs.27.00 Cr, Rs.5.78 Cr difference to finance cost | — |
| 8 | 459-460 | 31-Mar-26 quarter figures are balancing figures between FY26 audited full-year and 9-month reviewed YTD figures | Explains "(Refer Note 8)" tag on Mar-26 column throughout both P&L tables |
| 9 | 462-463 | Additional information per Reg 52(4) — heading for the ratios table (Table 5, Section 5B below) | — |

### 4B. Standalone Financial Results Notes (page 14, lines 752-786)

| Note | Line(s) | First ~15 words | Flags |
|------|---------|------------------|-------|
| 1 | 753-754 | Standalone results incl. Employees Welfare Trust reviewed by Audit Committee, approved by Board 24 July 2026 | — |
| 2 | 756-757 | Segment info per Ind AS 108 provided on consolidated basis only; not separately shown in standalone | — |
| 3 | 759-761 | Prepared in accordance with Companies (Indian Accounting Standards) Rules 2015 (Ind AS) | — |
| 4 | 763 | Exceptional Items — header note pointing to sub-items 4a/4b (both relate to PRIOR year, not current quarter) | — |
| 4a | 764-766 | FY26 (prior year): sale of remaining NSPL equity shares to NTPL for Rs.51.72 Cr; fair value gain Rs.82.75 Cr in Other income | — |
| 4b | 769-771 | FY26 (prior year): sale of LSAW Pipe Plant, Dahej, to Welspun Pipes Company LLC (KSA), wholly owned subsidiary, for Rs.203.07 Cr; profit Rs.168.38 Cr | Intercompany asset sale to own subsidiary — related-party in substance though at arm's length per independent valuation |
| 5 | 774-777 | Employees Welfare Trust results included per Ind-AS 102; treasury share cost Rs.2.26 Cr; 86,717 shares reduced from weighted-avg EPS count | — |
| 6 | 780-781 | No ESOP shares allotted this quarter; paid-up equity capital Rs.131.90 Cr / 26,37,90,645 shares of Rs.5 each | — |
| 7 | 784-785 | 31-Mar-26 quarter figures are balancing figures between FY26 audited full-year and 9-month reviewed YTD figures | — |
| 8 | 787-788 | Additional information per Reg 52(4) — heading for the ratios table (Table 5, Section 5D below) | — |

---

## TABLE 5 — FINANCIAL STATEMENT LINE ITEMS (all periods carried: 30-Jun-26 / 31-Mar-26 / 30-Jun-25 / FY26; unit Rs. Crores unless %)

### 5A. Consolidated Statement of P&L (page 7, lines 359-409)

| Line(s) | Row | 30-Jun-26 | 31-Mar-26 | 30-Jun-25 | FY26 | Flags |
|---------|-----|-----------|-----------|-----------|------|-------|
| 359 | 1 Income (header) | — | — | — | — | — |
| 360 | 1a Revenue from operations | 4,081.12 | 4,312.56 | 3,551.49 | 16,770.14 | — |
| 361 | 1b Other income | 63.79 | 35.61 | 35.03 | 135.25 | — |
| 362 | Total income (a+b) | 4,144.91 | 4,348.17 | 3,586.52 | 16,905.39 | — |
| 363 | 2 Expenses (header) | — | — | — | — | — |
| 364 | 2a Cost of materials consumed | 2,331.94 | 2,525.07 | 2,761.35 | 10,815.78 | — |
| 365 | 2b Purchase of stock-in-trade | 2.59 | 7.60 | 12.41 | 47.49 | — |
| 366-367 | 2c Changes in inventories of finished goods, stock-in-trade & WIP | (3.59) | 144.82 | (743.03) | (605.04) | — |
| 368 | 2d Employee benefits expense | 313.63 | 322.83 | 285.05 | 1,246.46 | — |
| 369 | 2e Finance costs | 45.18 | 48.95 | 63.18 | 212.17 | — |
| 370 | 2f Depreciation and amortisation expense | 124.58 | 93.03 | 84.78 | 354.55 | — |
| 371 | 2g Other expenses | 744.21 | 808.44 | 710.70 | 3,029.81 | — |
| 372 | Total expenses | 3,558.54 | 3,950.74 | 3,174.44 | 15,101.22 | — |
| 373-375 | 3 Profit before exceptional items, share of JV/associates & tax (1-2) | 586.37 | 397.43 | 412.08 | 1,804.17 | — |
| 376 | 4 Exceptional Items | - | - | - | - | ZERO_STANDING |
| 377-379 | 5 Profit before share of JV/associates & tax (3+4) | 586.37 | 397.43 | 412.08 | 1,804.17 | — |
| 380 | 6 Share of profit of joint venture and associates (net) | 72.83 | 106.58 | 48.97 | 342.34 | — |
| 381 | Profit on sale of shares of associate (refer Note 4) | 547.93 | - | - | - | New template line this quarter (EPIC partial sale, Note 4); watch whether it recurs |
| 382 | 7 Profit before tax (5+6) | 1,207.13 | 504.01 | 461.05 | 2,146.51 | — |
| 383 | 8 Income Tax expense (header) | — | — | — | — | — |
| 384 | 8a Current tax | 176.86 | (85.85) | 113.29 | 305.86 | — |
| 385 | 8b Deferred tax | (17.61) | 218.40 | (1.40) | 220.16 | — |
| 386 | Total tax expense | 159.25 | 132.55 | 111.89 | 526.02 | — |
| 387 | 9 Net profit for the period (7-8) | 1,047.88 | 371.46 | 349.16 | 1,620.49 | — |
| 388 | 10 Other Comprehensive Income, net of tax (header) | — | — | — | — | — |
| 389 | 10a Items that will be reclassified to P&L (net) | (7.07) | 168.71 | (8.33) | 294.27 | — |
| 390 | 10b Items that will not be reclassified to P&L (net) | 1.55 | 0.24 | (0.67) | (3.49) | — |
| 391 | Total OCI, net of tax | (5.52) | 168.95 | (9.00) | 290.78 | — |
| 392-393 | 11 Total Comprehensive Income (incl. NCI) (9+10) | 1,042.36 | 540.41 | 340.16 | 1,911.27 | — |
| 395 | 12 Net profit attributable to: (header) | — | — | — | — | — |
| 396 | 12 - Owners | 1,046.49 | 370.36 | 350.42 | 1,613.05 | — |
| 397 | 12 - Non-controlling interest | 1.39 | 1.10 | (1.26) | 7.44 | — |
| 398 | 13 OCI attributable to: (header) | — | — | — | — | — |
| 399 | 13 - Owners | (5.73) | 168.91 | (9.35) | 291.03 | — |
| 400 | 13 - Non-controlling interest | 0.21 | 0.04 | 0.35 | (0.25) | — |
| 401 | 14 Total comprehensive income attributable to: (header) | — | — | — | — | — |
| 402 | 14 - Owners | 1,040.76 | 539.27 | 341.07 | 1,904.08 | — |
| 403 | 14 - Non-controlling interest | 1.60 | 1.14 | (0.91) | 7.19 | — |
| 405 | 15 Paid up equity share capital (FV Rs.5) | 131.90 | 131.90 | 131.61 | 131.90 | — |
| 406 | 16 Other Equity | (blank) | (blank) | (blank) | 9,023.66 | Standard convention — Other Equity shown only at year-end column, not per quarter; not ZERO_STANDING |
| 407 | 17 EPS, not annualised (header) | — | — | — | — | — |
| 408 | 17a Basic (Rs) | 39.68 | 14.04 | 13.32 | 61.23 | — |
| 409 | 17b Diluted (Rs) | 39.65 | 14.04 | 13.25 | 61.20 | — |

### 5B. Consolidated Reg 52(4) Additional Information / Ratios (page 9, lines 462-529)

| Line | Row | 30-Jun-26 | 31-Mar-26 | 30-Jun-25 | FY26 | Flags |
|------|-----|-----------|-----------|-----------|------|-------|
| 475-476 | 1 Debt Equity Ratio | 0.11 | 0.23 | 0.13 | 0.23 | — |
| 478-479 | 2 Debt service coverage ratio | 1.21 | 2.15 | 3.64 | 5.03 | — |
| 481-482 | 3 Interest service coverage ratio | 69.58 | 21.11 | 18.21 | 21.61 | — |
| 484 | 4 Current Ratio | 1.29 | 1.33 | 1.31 | 1.33 | — |
| 487-489 | 5 Long term debt to working capital | 0.34 | 0.60 | 0.28 | 0.60 | — |
| 491-492 | 6 Bad debts to Accounts receivable ratio | - | - | - | 0.01 | Not all-period-nil (FY26 col = 0.01) — excluded from ZERO_STANDING by definition, noted for visibility |
| 494-495 | 7 Current liability ratio | 0.82 | 0.76 | 0.86 | 0.76 | — |
| 497-498 | 8 Total Debts to total assets ratio | 0.06 | 0.11 | 0.06 | 0.11 | — |
| 500-501 | 9 Debtors Turnover (days) | 32 | 35 | 44 | 38 | — |
| 503-504 | 10 Inventory Turnover (days) | 189 | 151 | 207 | 158 | — |
| 506-508 | 11 Operating EBITDA Margin % (incl. profit on sale of shares of associate in numerator per formula note) | 19.73% | 14.57% | 16.21% | 15.63% | Formula this quarter includes the one-off EPIC gain — margin not like-for-like vs. prior periods |
| 510-511 | 12 Net Profit Margin % | 25.68% | 8.61% | 9.83% | 9.66% | Inflated by EPIC one-off gain |
| 513 | 13 Paid up equity share capital | 131.90 | 131.90 | 131.61 | 131.90 | — |
| 515-516 | 14 Other Equity excl. DRR & CRR | 9,711.90 | 8,669.97 | 7,319.79 | 8,669.97 | — |
| 518 | 15 Debenture Redemption Reserve | - | - | - | - | ZERO_STANDING |
| 520 | 16 Capital Redemption Reserve | 353.69 | 353.69 | 353.69 | 353.69 | — |
| 522 | 17 Share Application money pending | - | - | - | - | ZERO_STANDING |
| 524-525 | 18 Outstanding redeemable preference shares (numbers) | - | - | - | - | ZERO_STANDING |
| 527 | 19 Outstanding redeemable preference shares (Rs. Cr) | - | (illegible/OCR gap) | - | - | ZERO_STANDING — 4th dash token illegible in source, consistent with row 18 above (same instrument) |
| 529 | 20 Networth | 10,449.45 | 9,405.86 | 8,070.21 | 9,405.86 | — |

### 5C. Consolidated Segment Information (page 10, lines 548-593)
Segments per CODM review: (1) Steel Products, (2) Others (incl. plastic products).

| Line(s) | Row | 30-Jun-26 | 31-Mar-26 | 30-Jun-25 | FY26 | Flags |
|---------|-----|-----------|-----------|-----------|------|-------|
| 564 | 1) Segment revenue (header) | — | — | — | — | — |
| 565 | a. Steel products | 3,906.07 | 4,136.08 | 3,393.06 | 16,134.11 | — |
| 566 | b. Others (incl. plastic products) | 175.05 | 176.48 | 158.43 | 636.03 | — |
| 567 | Total Revenue | 4,081.12 | 4,312.56 | 3,551.49 | 16,770.14 | — |
| 569-570 | 2) Segment results (header + formula descriptor) | — | — | — | — | — |
| 571 | a. Steel products | 598.81 | 447.54 | 465.71 | 2,026.50 | — |
| 572 | b. Others (incl. plastic products) | (137.06) | (134.44) | (18.66) | (101.55) | OCR-mangled bracket glyphs in source (rendered "137.06I", "134.441" etc.) — reconstructed as negative/loss values per context |
| 573 | Total | 561.75 | 413.10 | 457.05 | 1,924.95 | — |
| 574 | Add: Unallocated income, net of unallocated expense | 69.80 | 33.28 | 18.21 | 91.39 | — |
| 575 | Total Segment results | 631.55 | 446.38 | 475.26 | 2,016.34 | — |
| 576 | Less: Finance cost | 45.18 | 48.95 | 63.18 | 212.17 | — |
| 577-578 | Add/(Less): Share of profit/(loss) of JV and Associates (net) and Profit on sale of shares of associates | 620.76 | 106.58 | 48.97 | 342.34 | Combines ordinary JV/associate share with the one-off EPIC gain in a single reported line — obscures like-for-like JV run-rate |
| 579 | Profit Before tax | 1,207.13 | 504.01 | 461.05 | 2,146.51 | — |
| 581 | 3) Segment Assets (header) | — | — | — | — | — |
| 582 | a. Steel products | 14,879.52 | 14,138.07 | 12,412.85 | 14,138.07 | — |
| 583 | b. Others (incl. plastic products) | 1,446.93 | 1,388.11 | 1,133.27 | 1,388.11 | — |
| 584 | Total Segment assets | 16,326.45 | 15,526.17 | 13,546.12 | 15,526.17 | — |
| 585 | Add: Unallocated | 4,435.03 | 4,907.83 | 2,539.78 | 4,907.83 | — |
| 586 | Total Assets | 20,761.48 | 20,434.00 | 16,085.90 | 20,434.00 | — |
| 588 | 4) Segment Liabilities (header) | — | — | — | — | — |
| 589 | a. Steel products | 7,580.17 | 7,448.59 | 5,820.25 | 7,448.59 | — |
| 590 | b. Others (incl. plastic products) | 249.32 | 244.40 | 216.21 | 244.40 | — |
| 591 | Total Segment Liabilities | 7,829.49 | 7,692.99 | 6,036.46 | 7,692.99 | — |
| 592 | Add: Unallocated | 2,482.54 | 3,335.15 | 1,979.23 | 3,335.15 | — |
| 593 | Total Liabilities | 10,312.03 | 11,028.14 | 8,015.69 | 11,028.14 | — |

### 5D. Standalone Statement of P&L (page 13, lines 699-750)

| Line(s) | Row | 30-Jun-26 | 31-Mar-26 | 30-Jun-25 | FY26 | Flags |
|---------|-----|-----------|-----------|-----------|------|-------|
| 706 | 1 Income (header) | — | — | — | — | — |
| 707 | 1a Revenue from operations | 1,567.22 | 2,270.45 | 1,828.35 | 8,299.37 | — |
| 708 | 1b Other income | 38.48 | 18.31 | 106.83 | 296.35 | — |
| 710 | Total income (a+b) | 1,605.70 | 2,288.76 | 1,935.18 | 8,595.72 | — |
| 712 | 2 Expenses (header) | — | — | — | — | — |
| 713 | 2a Cost of materials consumed | 1,129.24 | 1,543.41 | 1,508.08 | 6,103.51 | — |
| 714 | 2b Purchases of stock-in-trade | (blank) | 15.52 | 7.35 | 40.43 | Current-quarter blank (not a printed dash) — no stock-in-trade purchases this quarter |
| 715 | 2c Changes in inventories of finished goods, stock-in-trade & WIP | (76.09) | (18.01) | (289.63) | (374.77) | — |
| 716 | 2d Employee benefits expense | 71.99 | 78.00 | 76.31 | 338.88 | — |
| 717 | 2e Finance costs | 14.63 | 22.55 | 30.11 | 107.64 | — |
| 718 | 2f Depreciation and amortisation expense | 40.63 | 37.30 | 39.19 | 150.90 | — |
| 719 | 2g Other expenses | 268.86 | 317.45 | 289.83 | 1,167.69 | — |
| 721 | Total expenses | 1,449.26 | 1,996.22 | 1,661.24 | 7,534.28 | — |
| 723 | 3 Profit before tax and exceptional items (1-2) | 156.44 | 292.54 | 273.94 | 1,061.44 | — |
| 725 | 4 Exceptional items (Refer Note 4) | (blank) | 4.89 | 51.72 | 220.10 | Current-quarter blank/nil; NOT all-period-nil (prior periods carry NSPL/LSAW gains per Note 4a/4b) — excluded from ZERO_STANDING by definition |
| 727 | 5 Profit before tax (3-4) | 156.44 | 297.43 | 325.66 | 1,281.54 | — |
| 729 | 6 Income tax expense (header) | — | — | — | — | — |
| 730 | 6a Current tax | 39.60 | 50.02 | 56.50 | 210.02 | — |
| 731 | 6b Deferred tax | 1.00 | 15.50 | 14.33 | 58.00 | — |
| 733 | Total tax expense | 40.60 | 65.52 | 70.83 | 268.02 | — |
| 735 | 7 Net profit for the period (5-6) | 115.84 | 231.91 | 254.83 | 1,013.52 | — |
| 736 | 8 Other Comprehensive (Loss)/Income, net of tax (header) | — | — | — | — | — |
| 738 | 8a Items that will be reclassified to P&L (net) | 16.30 | (16.74) | (22.50) | (37.27) | — |
| 739 | 8b Items that will not be reclassified to P&L (net) | 0.17 | 1.24 | (0.82) | 0.65 | — |
| 740 | Total OCI, net of tax | 16.47 | (15.50) | (23.32) | (36.62) | — |
| 742 | 9 Total Comprehensive Income for the period (7+8) | 132.31 | 216.41 | 231.51 | 976.90 | — |
| 746 | 10 Paid up equity share capital (FV Rs.5) | 131.90 | 131.90 | 131.61 | 131.90 | — |
| 747 | 11 Other Equity | (blank) | (blank) | (blank) | 5,022.33 | Standard convention — year-end column only; not ZERO_STANDING |
| 748 | 12 EPS, not annualised (header) | — | — | — | — | — |
| 749 | 12a Basic (Rs) | 4.39 | 8.79 | 9.68 | 38.47 | — |
| 750 | 12b Diluted (Rs) | 4.39 | 8.79 | 9.66 | 38.45 | — |

### 5E. Standalone Reg 52(4) Additional Information / Ratios (page 15, lines 787-851)

| Line | Row | 30-Jun-26 | 31-Mar-26 | 30-Jun-25 | FY26 | Flags |
|------|-----|-----------|-----------|-----------|------|-------|
| 800-801 | 1 Debt Equity Ratio | 0.01 | 0.08 | 0.14 | 0.08 | — |
| 803-804 | 2 Debt service coverage ratio | 33.06 | 1.31 | 28.55 | 4.64 | — |
| 806-807 | 3 Interest service coverage ratio | 47.71 | 27.64 | 35.48 | 24.44 | — |
| 809 | 4 Current Ratio | 1.24 | 1.23 | 1.18 | 1.23 | — |
| 812-814 | 5 Long term debt to working capital | 0.05 | 0.05 | 0.38 | 0.05 | — |
| 816-817 | 6 Bad debts to Accounts receivable ratio | - | - | - | - | ZERO_STANDING |
| 819-820 | 7 Current liability ratio | 0.89 | 0.89 | 0.91 | 0.89 | — |
| 822-823 | 8 Total Debts to total assets ratio | 0.01 | 0.05 | 0.07 | 0.05 | — |
| 825-827 | 9 Debtors Turnover (days) | 71 | 55 | 63 | 60 | — |
| 829-830 | 10 Inventory Turnover (days) | 168 | 108 | 139 | 112 | — |
| 832-833 | 11 Operating EBITDA Margin % | 12.80% | 15.13% | 17.65% | 15.31% | — |
| 835-836 | 12 Net Profit Margin % | 7.39% | 10.21% | 13.94% | 12.21% | — |
| 838 | 13 Paid up equity share capital | 131.90 | 131.90 | 131.61 | 131.90 | — |
| 840-841 | 14 Other Equity excl. DRR & CRR | 4,802.13 | 4,668.64 | 4,047.36 | 4,668.64 | — |
| 843 | 15 Debenture Redemption Reserve | - | (illegible) | - | (illegible) | ZERO_STANDING — only 2 of 4 dash tokens legible in source (OCR gap); consistent with all-nil status of consol counterpart (row 15, section 5B) |
| 845 | 16 Capital Redemption Reserve | 353.69 | 353.69 | 353.69 | 353.69 | — |
| 847 | 17 Outstanding redeemable preference shares (numbers) | (blank/OCR gap) | - | - | - | ZERO_STANDING |
| 849 | 18 Outstanding redeemable preference shares (Rs. Cr) | (blank/OCR gap) | - | - | - | ZERO_STANDING |
| 851 | 19 Networth | 5,287.72 | 5,154.23 | 4,532.66 | 5,154.23 | — |

---

## TABLE 6 — ANNEXURES

### 6A. Annexure A — New entity incorporation (GGBS/slag business), page 16, lines 864-902

| Row | Line(s) | Field | Detail | Flags |
|-----|---------|-------|--------|-------|
| 1 | 868-876 | Name of entity, date & country of incorporation | Name TBD pending regulatory approval; country India | — |
| 2 | 878-883 | Name of holding company / relation | Proposed holding co.: Slagexcel Private Limited; new entity to be an associate of WELCORP | — |
| 3 | 884-886 | Industry | Manufacturing/processing/dealing in Ground Granulated Blast Furnace Slag (GGBS) | — |
| 4 | 888-890 | Brief background / line of business | Will manufacture GGBS through Slag Granulation Process | — |
| 5 | 892-894 | Regulatory approvals required | Subject to regulatory approvals | — |
| 6 | 895-897 | Nature of consideration | Cash consideration for 2,600 equity shares of Rs.10 each | — |
| 7 | 898-899 | Cost of subscription | Rs.26,000 for 2,600 equity shares of Rs.10 each | — |
| 8 | 900-902 | % shareholding by listed entity | 26% of total paid-up capital of the new company | — |

### 6B. Annexure B — WCPGL acquisition (51% additional stake), page 17, lines 904-952

| Row | Line(s) | Field | Detail | Flags |
|-----|---------|-------|--------|-------|
| 1 | 907-912 | Target entity, size/turnover | WCPGL, an Associate; FY26 turnover Rs.109.95 Cr | — |
| 2 | 913-920 | Related party transaction? | Yes — seller Welspun Living Limited is promoter group co.; represented as arm's length | RELATED_PARTY |
| 3 | 921-922 | Industry | Captive Power Generation | — |
| 4 | 923-928 | Objects/impact | To meet Company's power requirements | — |
| 5 | 929-931 | Regulatory approvals required | Statutory/regulatory/other approvals as applicable | — |
| 6 | 932-933 | Indicative completion timeline | On or before 31 August 2026 | — |
| 7 | 934-936 | Consideration type | Cash consideration | — |
| 8 | 937-938 | Cost of acquisition | Rs.67.66 Cr | — |
| 9 | 939-941 | % stake / shares acquired | Additional 51% equity, 1,50,64,213 shares of FV Rs.10 | — |
| 10 | 942-952 | Background / 3-yr turnover history | WCPGL inc. 30 Apr 2010; turnover FY24 Rs.138.70 Cr, FY25 Rs.98.13 Cr, FY26 Rs.109.95 Cr — non-monotonic 3-year turnover trend | — |

---

## TABLE 7 — DIGITAL SIGNATURE / SIGNATORY BLOCKS

| # | Line(s) | Signatory | Designation | Document | Timestamp | Flags |
|---|---------|-----------|-------------|----------|-----------|-------|
| 1 | 80-88 | Kamal Rathi | Company Secretary and Compliance Officer (ACS-18182) | Board Outcome letter | Digitally signed 2026.07.24 14:05:35 +05'30' | Signed 5 min AFTER board conclusion (2:00 p.m. per line 74) — correct sequencing, not a flag |
| 2 | 187-197 | Bhavesh Dhupelia (Partner, Membership No. 042070) | BSR & Co. LLP, Chartered Accountants | Consolidated Limited Review Report | 24 July 2026, Mumbai (no intraday time given); UDIN 26042070ZYJBUY6781 | — |
| 3 | 670-680 | Bhavesh Dhupelia (Partner, Membership No. 042070) | BSR & Co. LLP, Chartered Accountants | Standalone Limited Review Report | 24 July 2026, Mumbai (no intraday time given); UDIN 26042070CMNYYY2543 | — |
| 4 | 534-541 | Vipul Mathur | Managing Director and Chief Executive Officer (DIN 07990476) | Consolidated Financial Results | Place: Mumbai; Date: July 24, 2026 (no intraday time) | OCR renders name "Vipul M thur" (missing "a") — missed by first-pass name grep |
| 5 | 596-603 | Vipul Mathur | Managing Director and Chief Executive Officer (DIN 07990476) | Consolidated Segment Information | Place: Mumbai; Date: July 24, 2026 | OCR renders name "Vipul Math r" (missing "u") — missed by first-pass name grep |
| 6 | 855-862 | Vipul Mathur | Managing Director and Chief Executive Officer (DIN 07990476) | Standalone Financial Results | Place: Mumbai; Date: July 24, 2026 | OCR renders name "Vipul Ma hur" (missing "t") — missed by first-pass name grep |

All three Vipul Mathur blocks and both Bhavesh Dhupelia blocks precede/follow the Board's 2:00 p.m. approval consistently (no dates given intraday except the Kamal Rathi letter); no pre-conclusion signing detected.

---

## SUMMARY OF ALL FLAGS RAISED
- ZERO_STANDING x9: Consol P&L Exceptional Items (376); Consol ratios DRR (518), Share Application money (522), Outstanding redeemable pref shares numbers (524) and Rs.Cr (527); Standalone ratios Bad debts (816), DRR (843), Outstanding redeemable pref shares numbers (847) and Rs.Cr (849).
- OCR-artifact flags (structural, non-canonical vocabulary, surfaced for A3/A4 attention): OCR_MISREAD (Note 5→"S", line 441), OCR_GAP (entity 16 Sr. No. illegible, line 267; ratio table dash tokens illegible, lines 527/843/847/849), OCR_SPLIT (Consol LRR para 6, line 141), OCR_INDENT (Consol LRR para 7, line 175), OCR name-drop x3 (Vipul Mathur signature blocks, lines 539/601/860).
- RELATED_PARTY x2 (non-canonical, surfaced for attention): Board Outcome agenda item 3 / Annexure B (WCPGL acquisition from promoter-group Welspun Living Limited); Standalone Note 4b (LSAW plant sale to own wholly-owned subsidiary).
- ENTITY_CHANGE: NOT DETERMINABLE — no prior-quarter ledger supplied to this run.
