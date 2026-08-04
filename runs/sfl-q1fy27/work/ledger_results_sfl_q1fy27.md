# A2 ENUMERATION LEDGER — Sheela Foam Ltd (SFL) — Q1 FY27 (quarter ended 30 June 2026) — Results Filing

Source: extract_results_sfl_q1fy27.txt (12 pages, 846 lines incl. header, page_coverage: 100%)

```
=== A2 COUNT TEST ===
category: numbered_notes      grep_count: 19   sweep_count: 19   match: yes
category: footnotes           grep_count: 4    sweep_count: 4    match: yes
category: auditor_paras       grep_count: 11   sweep_count: 11   match: yes
category: line_items          grep_count: 138  sweep_count: 138  match: yes
category: zero_standing       grep_count: 38   sweep_count: 38   match: yes
category: agenda_items        grep_count: 2    sweep_count: 2    match: yes
category: signature_blocks    grep_count: 5    sweep_count: 5    match: yes
category: entities            grep_count: 11   sweep_count: 11   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep commands used (reproducible):
- numbered_notes: `sed -n '195,294p;558,679p' extract | grep -nE "^\s{0,3}[0-9]{1,2}\s+[A-Za-z\*]"` → 9 standalone + 10 consolidated = 19
- footnotes: `grep -nE "^\s*\*" extract` → 4 (lines 266, 268, 629, 631)
- auditor_paras: `grep -cE "^\s*[0-9]+\.\s" extract` → 11 (4 standalone + 7 consolidated)
- line_items: per-table `grep -c -E "[0-9]+\.[0-9]{2}|\s-\s"` summed across 6 tables → 30+41+16+16+4+31 = 138
- zero_standing: manual dash/0.0%-in-all-periods sweep cross-checked against grep hits on each candidate line, plus `grep -c "NIL" ` on Security Cover table (lines 709-846) = 31 → total 3+1+3+31 = 38
- agenda_items: manual sweep of Board Outcome letter body (lines 24-41), cross-checked, no numbered-agenda markup in source (letter is prose) → 2
- signature_blocks: manual sweep for "Digitally signed by" occurrences → `grep -c "Digitally signed"` = 5
- entities: `sed -n '372,410p' extract | grep -cE "^\s*[0-9]{1,2}\s+[A-Za-z]"` → 11

---

## 1. BOARD OUTCOME LETTER — AGENDA ITEMS (page 1, lines 16-51)

| # | Item | Line(s) | Detail | Flags |
|---|------|---------|--------|-------|
| 1 | Approval of Un-Audited Standalone and Consolidated Financial Results for quarter ended June 30, 2026 | 29-35 | "please find enclosed herewith, Un-Audited Standalone and Consolidated Financial Results along with line item as per Regulation 52(4)... as approved by the Board of Directors in its meeting held on August 04, 2026" | — |
| 2 | NIL Certificate of Security Cover (Reg 54, unsecured redeemable listed taxable NCDs) | 37-39 | "pursuant to the provisions of Regulation 54... a NIL certificate of Security Cover in respect of Unsecured, Redeemable, Listed, Taxable Non-Convertible Debentures is also enclosed" | ZERO_STANDING (see Section 7) |

**Board meeting timing** (line 41): commenced 11:15 AM, concluded 03:45 PM — duration 4h 30m.

**FLAG — EXPECTED_AGENDA_ITEM_NOT_FOUND**: The injected task brief for this run states "this filing accompanies a same-day director appointment" and instructs enumeration of "every board action." The A1 extract (header claims 12/12 pages, 100% page_coverage) contains **no director-appointment agenda item, no AR approval, no AGM notice/record date item, no fresh dividend resolution (note 8/9 only reference a prior FY26 dividend already paid), no auditor-change item, no scrutinizer appointment, no ESOP grant resolution, and no capital-raising enabling resolution** anywhere in the Board Outcome letter body (lines 16-51) or elsewhere in the extract. Only the two items above are disclosed as board actions. This is either (a) a genuinely single-agenda Board Outcome letter with the director appointment disclosed under a separate same-day filing not included in this extract, or (b) an extraction/sourcing gap. Route to A3 for verification against the BSE/NSE filing index for a companion same-day director-appointment disclosure; do not assume it is covered here.

---

## 2. SIGNATURE BLOCKS (all digitally signed)

| # | Signatory | Designation | Document | Line(s) | Timestamp | Flags |
|---|-----------|-------------|----------|---------|-----------|-------|
| 1 | Md. Iquebal Ahmad | Company Secretary & Compliance Officer | Board Outcome cover letter | 46-51 | 2026.08.04 16:19:16 +05'30' | — (after meeting concluded 15:45, as expected) |
| 2 | Nipun Gupta (M S K A & Associates LLP, ICAI FRN 105047W/W101187) | Partner, Membership No. 502896 | Standalone Auditor's Review Report; UDIN 26502896AVQMJB7358 | 107-118 | 2026.08.04 15:44:30 +05'30' | **SIGNATURE_BEFORE_MEETING_CONCLUDED** — 30 sec before board's stated 03:45 PM conclusion (line 41) |
| 3 | Rahul Gautam | Managing Director, DIN 00192999 | Standalone financial results statement | 297-322 | 2026.08.04 15:32:07 +05'30' | **SIGNATURE_BEFORE_MEETING_CONCLUDED** — 13 min before board's stated 03:45 PM conclusion |
| 4 | Nipun Gupta (M S K A & Associates LLP, ICAI FRN 105047W/W101187) | Partner, Membership No. 502896 | Consolidated Auditor's Review Report; UDIN 26502896PLIAZG7028 | 451-464 | 2026.08.04 15:45:09 +05'30' | Borderline — 9 sec after stated conclusion; flag for A3 given block 2/3/5 all precede conclusion |
| 5 | Rahul Gautam | Managing Director, DIN 00192999 | Consolidated financial results statement | 681-707 | 2026.08.04 15:32:54 +05'30' | **SIGNATURE_BEFORE_MEETING_CONCLUDED** — 12 min before board's stated 03:45 PM conclusion |

**Reconciliation note**: 3 of 5 signature blocks (standalone results, standalone auditor report, consolidated results) carry timestamps earlier than the board's own stated meeting-conclusion time of 03:45 PM (line 41). The 4th (consolidated auditor report) clears it by only 9 seconds. Only the Company Secretary's cover-letter signature (16:19:16) is unambiguously after conclusion. This is a material timing-consistency flag for A3/A4: either the stated "concluded at 03:45 PM" is inaccurate, or the documents were finalized/signed before formal board conclusion.

---

## 3. AUDITOR REVIEW REPORTS — PARAGRAPH-BY-PARAGRAPH (auditor_paras = 11)

### 3a. Standalone Review Report (M S K A & Associates LLP), pages 2, lines 72-126

| Para | Line | Content (first ~15 words) | Flags |
|------|------|---------------------------|-------|
| 1 | 79-83 | "We have reviewed the accompanying Statement of standalone unaudited financial results..." (scope) | — |
| 2 | 85-90 | "This Statement, which is the responsibility of Company's Management and has been approved..." (management responsibility, Ind AS 34 basis) | — |
| 3 | 92-99 | "We conducted our review... Standard on Review Engagement (SRE) 2410... Accordingly, we do not express an audit opinion." | Review only, not an audit — cap conclusion strength accordingly |
| 4 | 101-105 | "Based on our review conducted... nothing has come to our attention that causes us to believe..." (unmodified review conclusion) | Opinion type: unmodified review conclusion. No Emphasis of Matter, no Other Matters, no Going Concern paragraph present. |

Entity list reviewed (standalone): single legal entity (Sheela Foam Limited), no subsidiaries in standalone scope.
UDIN: 26502896AVQMJB7358 (line 118).

### 3b. Consolidated Review Report (M S K A & Associates LLP), pages 6-8, lines 333-448

| Para | Line | Content (first ~15 words) | Flags |
|------|------|---------------------------|-------|
| 1 | 341-348 | "We have reviewed the accompanying Statement of consolidated unaudited financial results of Sheela Foam Limited..." (scope, Holding Co + subsidiaries + JV) | — |
| 2 | 350-356 | "This Statement, which is the responsibility of the Holding Company's Management and has been approved..." | — |
| 3 | 358-367 | "We conducted our review... SRE 2410... We also performed procedures in accordance with the circular issued by SEBI under Regulation 33(8)..." | Review only, not audit |
| 4 | 370-410 | "This Statement includes the results of the Holding Company and the following entities:" — entity table (11 entities, see Section 6) | Contains the consolidation entity list |
| 5 | 412-418 | "Based on our review conducted and procedures performed... and based on the consideration of the review reports of the other auditors..." (unmodified review conclusion, relies on component auditors) | Opinion type: unmodified, but explicitly relies on other auditors (component reliance) |
| 6 | 420-428 | "We did not review the financial results of 9 subsidiaries included in the Statement, whose financial results reflects total revenues of Rs. 284.14 crores, total net profit after tax of Rs. 15.22 crores and total comprehensive income of Rs. 15.09 crores..." | **Other-Matters-type paragraph.** 9 of 11 consolidated entities NOT reviewed by MSKA — reviewed by other/component auditors, furnished to MSKA by Management. Materiality: Rs 284.14 cr revenue, Rs 15.22 cr PAT, Rs 15.09 cr TCI of the quarter flow through unreviewed-by-principal-auditor components. |
| 7 | 430-436 | "Certain subsidiaries are located outside India whose financial results have been prepared in accordance with the accounting principles generally accepted in their respective countries..." (foreign GAAP conversion, reviewed by other auditors under local standards) | Foreign-entity conversion reliance flag |
| (cont.) | 443-448 | "We have reviewed these conversion adjustments made by the Holding Company's Management. Our conclusion... is based on the report of other auditors and the conversion adjustments... Our conclusion is not modified..." | Conclusion not modified despite reliance |

No Going Concern paragraph in either report. No explicit "Emphasis of Matter" heading in either report; paras 6-7 (consolidated) function as Other-Matters-style component-reliance disclosures without that heading.
UDIN: 26502896PLIAZG7028 (line 461).

---

## 4. NUMBERED NOTES (numbered_notes = 19)

### 4a. Standalone financial results notes (page 3-5, lines 194-294) — 9 notes

| Note | Line | First ~15 words | Flags |
|------|------|------------------|-------|
| 1 | 195-196 | "These standalone financial results have been reviewed by the Audit Committee and subsequently approved by the Board..." | — |
| 2 | 197-199 | "These standalone financial results have been prepared in accordance with the recognition and measurement principles laid down in Ind AS 34..." | — |
| 3 | 202 | "Additional disclosures as per Regulation 52(4) of SEBI (LODR) Regulations, 2015" — header for ratios table (Section 5a) | — |
| 4 | 272-274 | "The Company is engaged in the manufacturing of the products of same type/class and has no overseas operations/units and as such there are no reportable segments..." | No standalone segment reporting (contrast with consolidated note 4, which does report geographic segments) |
| 5 | 276-283 | "Exceptional items: a) Results for the year ended March 31, 2026 includes net gain of ₹7.93 Crores on account of sale of certain land and buildings... b) Results for the quarter ended June 30, 2026 includes gain of ₹6.26 Crores on account of sale of certain land and building situated at Haridwar..." | Two sub-items (a: FY26 land/building sale gain Roorkee/Dabaspet/Jhagadia ₹7.93 cr; b: Q1FY27 Haridwar land/building sale gain ₹6.26 cr, already held-for-sale) |
| 6 | 285-286 | "During the quarter ended June 30, 2026, the Company has issued 4,390 equity shares of face value of ₹5 each on exercise of employee stock options under the 'SF ESOP - 2022' scheme." | ESOP exercise disclosure — ties to same-quarter ESOP activity |
| 7 | 288-289 | "The figures for the quarter ended March 31, 2026 is the balancing figure between audited figures in respect of the full financial year..." | Explains derivation of Q4FY26 comparative column |
| 8 | 291-292 | "For financial year ended March 31, 2026, the Board recommended a final dividend of ₹1 per share (20% on an equity share of ₹5 each). The same was approved by the shareholders in the AGM... held on July 16, 2026 and paid on July 30, 2026." | FY26 dividend already approved/paid before this filing; not a new dividend action this quarter |
| 9 | 294 | "Figures for previous periods/year have been regrouped/reclassified wherever necessary to correspond with the current quarter's classification." | Standard regrouping note |

### 4b. Consolidated financial results notes (pages 9-11, lines 556-679) — 10 notes

| Note | Line | First ~15 words | Flags |
|------|------|------------------|-------|
| 1 | 558-559 | "These consolidated financial results have been reviewed by the Audit Committee and subsequently approved by the Board..." | — |
| 2 | 561-564 | "These consolidated financial results of Sheela Foam Limited ('the Holding Company') and its subsidiaries ('the Group') together with jointly controlled entity..." | — |
| 3 | 567 | "Additional disclosures as per Regulation 52(4) of SEBI (LODR) Regulations, 2015" — header for ratios table (Section 5b) | — |
| 4 | 635-652 | "Segment Reporting as per Ind AS 108... The Group is mainly engaged in manufacturing of the products of same type/class, and therefore there is no reportable Business Segments. The Group has geographical segments..." | Contains geographic segment table (Section 5c) — consolidated DOES report geographic segments though standalone note 4 says none reportable (different scope: standalone = no segments at all; consolidated = geographic only, no business segments) |
| 5 | 654-656 | "The Holding Company has acquired 17.70% equity stake w.e.f. August 29, 2023 in 'House of Kieraya Limited (Furlenco)' which has been increased to 43.89%... subsequently... reduced to 34.53% on issuance of fresh issue of 83,72,392 equity shares..." | Stake dilution disclosure on JV (Furlenco) — from 43.89% to 34.53% via non-participation in JV's fresh issue (SFL subscribed only 20,09,377 of 83,72,392 new shares) |
| 6 | 659-666 | "Exceptional items: a) Results for the year ended March 31, 2026 includes net gain of ₹7.93 Crores... b) Results for the quarter ended June 30, 2026 includes gain of ₹6.26 Crores..." | Same two sub-items as standalone note 5 |
| 7 | 669-670 | "During the quarter ended June 30, 2026, the holding company has issued 4,390 equity shares of face value of ₹5 each on exercise of employee stock options..." | Same ESOP disclosure as standalone note 6 |
| 8 | 672-673 | "The figures for the quarter ended March 31, 2026 is the balancing figure between audited figures in respect of the full financial year..." | Same as standalone note 7 |
| 9 | 675-676 | "For financial year March 31, 2026, the Board recommended a final dividend of ₹1 per share (20% on an equity share of ₹5 each)... approved... AGM... held on July 16, 2026 and paid on July 30, 2026." | Same as standalone note 8 |
| 10 | 679 | "Figures for previous periods/year have been regrouped/reclassified wherever necessary to correspond with the current quarter's classification." | Same as standalone note 9 |

---

## 5. UNNUMBERED NOTES / FOOTNOTES (footnotes = 4)

| # | Line | Table | Text (first ~15 words) |
|---|------|-------|--------------------------|
| 1 | 266-267 | Standalone Reg 52(4) ratio formulas | "* Cost of goods sold includes Cost of materials consumed, Purchases of Stock-in-trade, Changes in Inventories of Finished Goods, Stock-in-trade and Work-in-progress and Other manufacturing expenses." |
| 2 | 268-269 | Standalone Reg 52(4) ratio formulas | "** Net worth has been computed on the basis as stated in Clause(2) of SEBI (LODR) Regulations 2015 i.e. Net worth as defined in subsection (57) of section 2 of the Companies Act, 2013." |
| 3 | 629-630 | Consolidated Reg 52(4) ratio formulas | "* Cost of goods sold includes Cost of materials consumed, Purchases of Stock-in-trade and Changes in Inventories of Finished Goods, Stock-in-trade and Work-in-progress and Other manufacturing expenses." |
| 4 | 631-632 | Consolidated Reg 52(4) ratio formulas | "** Net worth has been computed on the basis as stated in Clause(2) of SEBI (LODR) Regulations 2015 i.e. Net worth as defined in subsection (57) of section 2 of the Companies Act, 2013." |

Inline note back-references (not counted as new footnotes, already point to numbered notes above): "(refer note 7)" at line 143 (standalone P&L, March 31 2026 column); "(Refer Note 8)" at line 488 (consolidated P&L, March 31 2026 column).

---

## 6. CONSOLIDATION ENTITY LIST (entities = 11) — pages 6-7, lines 372-407

No prior-quarter ledger was supplied for this run (PRIOR_LEDGER_PATH not provided), so cross-quarter ENTITY_CHANGE comparison cannot be performed against a prior ledger. However, the document itself discloses an exit within the list — flagged below.

| Sr. No | Line | Entity | Relationship | Flags |
|--------|------|--------|--------------|-------|
| 1 | 375 | Staqo Software Private Limited (SSPL) | Wholly Owned Subsidiary | — |
| 2 | 377 | Sleepwell Enterprises Private Limited | Wholly Owned Subsidiary | — |
| 3 | 379 | Staqo Incorporated | Wholly Owned Subsidiary of SSPL | — |
| 4 | 391 | Staqo Technologies LLC | Subsidiary of SSPL | — |
| 5 | 393 | Joyce Foam Pty Limited (JFPL Australia) | Wholly Owned Subsidiary | — |
| 6 | 395-396 | Joyce WC NSW Pty Limited | Wholly Owned Subsidiary of JFPL Australia | — |
| 7 | 398-399 | International Foam Technologies Spain, S.L.U (IFTS Spain) | Wholly Owned Subsidiary | — |
| 8 | 401 | Interplasp S.L | Subsidiary of IFTS Spain | — |
| 9 | 403 | Sheela Foam Trading L.L.C | Wholly Owned Subsidiary | — |
| 10 | 405 | House of Kieraya Limited | Jointly Controlled Entity | Stake reduced 43.89% → 34.53% per note (Section 4b, note 5) |
| 11 | 407-408 | Furlenco Global Pte. Ltd. | Subsidiary of Jointly Controlled Entity, marked "(upto 01.04.2026)" | **ENTITY_CHANGE** — entity dated as exiting the consolidation scope effective 01.04.2026 (i.e., no longer consolidated as of/after this date, disclosed within the current entity table itself) |

Of these 11 entities, 9 subsidiaries' financial results were **not reviewed by the principal auditor** (MSKA) — reviewed instead by other/component auditors and furnished to MSKA by Management (auditor para 6, Section 3b). The extract does not name which 9 of the 11; route to A3 to confirm from full report/annexures if available elsewhere.

---

## 7. FINANCIAL STATEMENT LINE ITEMS (line_items = 138; zero_standing = 38 of the 138, tagged below)

### 7a. Standalone Statement of Financial Results (page 3, lines 144-189) — 30 line items

| Line | Item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|------|------|--------|--------|--------|------|-------|
| 145 | a) Revenue from operations | 760.92 | 819.20 | 634.63 | 2,962.27 | — |
| 146 | b) Other Income | 13.63 | 16.11 | 8.35 | 40.32 | — |
| 147 | Total Income [(a)+(b)] | 774.55 | 835.31 | 642.98 | 3,002.59 | — |
| 150 | a) Cost of materials consumed | 461.88 | 427.33 | 333.32 | 1,598.62 | — |
| 151 | b) Purchase of stock-in-trade | 21.13 | 31.11 | 27.01 | 100.31 | — |
| 152-154 | c) Changes in inventories of FG/stock-in-trade/WIP | (7.87) | 5.28 | (7.71) | (7.73) | — |
| 155 | d) Other manufacturing expenses | 26.97 | 28.42 | 28.67 | 113.04 | — |
| 156 | e) Employee benefits expenses | 75.42 | 101.18 | 74.51 | 322.58 | — |
| 157 | f) Finance costs | 12.28 | 15.13 | 22.80 | 70.98 | — |
| 158 | g) Depreciation and amortisation expenses | 17.24 | 16.76 | 29.91 | 110.20 | — |
| 159 | h) Other expenses | 115.01 | 135.51 | 118.58 | 537.85 | — |
| 160 | Total Expenses [(a) to (h)] | 722.06 | 760.72 | 627.09 | 2,845.85 | — |
| 162 | III Profit before tax and Exceptional Items | 52.49 | 74.59 | 15.89 | 156.74 | — |
| 163 | IV Exceptional items | (6.26) | (15.77) | - | (7.93) | — |
| 164 | V Profit before tax | 58.75 | 90.36 | 15.89 | 164.67 | — |
| 166 | Current tax | - | - | - | - | **ZERO_STANDING** — dash all 4 periods |
| 167 | Earlier tax adjustment | 0.02 | (9.69) | - | (9.44) | — |
| 168 | Deferred tax | 14.79 | 24.53 | 5.19 | 43.54 | — |
| 169 | Total Tax Expenses | 14.81 | 14.84 | 5.19 | 34.10 | — |
| 171 | VII Profit for the period/year | 43.94 | 75.52 | 10.70 | 130.57 | — |
| 175 | Remeasurements gain/(loss) of net defined benefit plans | (2.19) | (1.58) | (1.08) | (1.29) | — |
| 176 | Income tax effect on above (item a) | - | - | - | - | **ZERO_STANDING** |
| 178 | Fair value gain/(loss) on investments and other financial instruments | (0.76) | (1.11) | (0.17) | (0.80) | — |
| 179 | Income tax effect on above (item b) | - | - | - | - | **ZERO_STANDING** |
| 180-181 | Total OCI for the period/year | (2.95) | (2.69) | (1.25) | (2.09) | — |
| 183 | IX Total Comprehensive Income | 40.99 | 72.83 | 9.45 | 128.48 | — |
| 185 | X Paid up Equity Share Capital (FV ₹5) | 54.60 | 54.60 | 54.60 | 54.60 | — |
| 186 | XI Other Equity | (blank) | (blank) | (blank) | 2,857.58 | Reported only in FY26 (annual) column, per standard quarterly template — not a dash/nil, structurally not applicable to quarter columns |
| 188 | Basic EPS | 4.02 | 6.92 | 0.98 | 11.96 | — |
| 189 | Diluted EPS | 4.02 | 6.90 | 0.98 | 11.93 | — |

### 7b. Standalone Reg 52(4) Additional Disclosures (page 4, lines 209-224) — 16 line items

| Line | Item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|------|------|--------|--------|--------|------|-------|
| 209 | a) Net Worth (₹ Cr) | 2,954.72 | 2,912.18 | 2,787.78 | 2,912.18 | — |
| 210 | b) Outstanding Unsecured NCDs (₹ Cr) | 181.25 | 362.50 | 543.75 | 362.50 | — |
| 211 | c) Debt service coverage ratio (x) | 0.20 | 0.24 | 0.11 | 0.68 | — |
| 212 | d) Interest service coverage ratio (x) | 5.27 | 5.93 | 1.70 | 3.21 | — |
| 213 | e) Debt equity ratio (x) | 0.15 | 0.16 | 0.31 | 0.16 | — |
| 214 | f) Current Ratio (x) | 0.79 | 0.73 | 0.82 | 0.73 | — |
| 215 | g) Long term debt to working capital ratio (x) | (1.34) | (1.57) | (3.23) | (1.57) | — |
| 216 | h) Bad debts to Account receivable ratio (%) | 0.0% | 0.0% | 0.0% | 0.0% | **ZERO_STANDING** — 0.0% all 4 periods |
| 217 | i) Current liability ratio (x) | 0.88 | 0.89 | 0.77 | 0.89 | — |
| 218 | j) Total debts to total assets (x) | 0.11 | 0.11 | 0.20 | 0.11 | — |
| 219 | k) Debtors Turnover Ratio (x) | 2.72 | 3.24 | 3.11 | 11.80 | — |
| 220 | l) Inventory Turnover Ratio (x) | 1.78 | 1.86 | 1.59 | 6.86 | — |
| 221 | m) Basic EPS (₹) | 4.02 | 6.92 | 0.98 | 11.96 | — |
| 222 | n) Diluted EPS (₹) | 4.02 | 6.90 | 0.98 | 11.93 | — |
| 223 | o) Operating margin (%) | 34.0% | 39.9% | 39.9% | 39.1% | — |
| 224 | p) Net profit margin (%) | 5.8% | 9.2% | 1.7% | 4.4% | — |

### 7c. Consolidated Statement of Financial Results (page 9, lines 490-553) — 41 line items

| Line | Item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|------|------|--------|--------|--------|------|-------|
| 490 | a) Revenue from operations | 1,031.94 | 1,050.06 | 821.41 | 3,820.84 | — |
| 491 | b) Other Income | 16.13 | 18.34 | 9.74 | 54.27 | — |
| 492 | Total Income [(a)+(b)] | 1,048.07 | 1,068.40 | 831.15 | 3,875.11 | — |
| 494 | a) Cost of materials consumed | 594.69 | 568.80 | 434.10 | 2,054.52 | — |
| 495 | b) Purchase of stock-in-trade | 24.28 | 34.02 | 27.01 | 106.40 | — |
| 496-498 | c) Changes in inventories of FG/stock-in-trade/WIP | (5.65) | (18.58) | (6.15) | (11.64) | — |
| 499 | d) Other manufacturing expenses | 36.93 | 39.89 | 36.70 | 149.65 | — |
| 500 | e) Employee benefits expenses | 124.71 | 147.78 | 115.21 | 495.13 | — |
| 501 | f) Finance costs | 17.82 | 20.88 | 29.17 | 95.15 | — |
| 502 | g) Depreciation and amortisation expenses | 33.88 | 35.60 | 46.12 | 178.58 | — |
| 503 | h) Other expenses | 148.08 | 161.53 | 139.31 | 633.41 | — |
| 504 | Total Expenses [(a) to (h)] | 974.74 | 989.92 | 821.47 | 3,701.20 | — |
| 505 | III Profit before tax and Exceptional Items | 73.33 | 78.48 | 9.68 | 173.91 | — |
| 506 | IV Exceptional items | (6.26) | (15.77) | - | (7.93) | — |
| 507 | V Profit before tax | 79.59 | 94.25 | 9.68 | 181.84 | — |
| 509 | Current tax | 3.53 | (1.03) | 1.38 | 7.24 | — (differs from standalone, which is ZERO_STANDING at consolidated level — flag interpretive note for A4: consolidated Current tax is non-zero even though standalone is nil in every period, i.e. tax is arising entirely at subsidiary/JV level) |
| 510 | Earlier tax adjustment | 0.04 | (9.69) | - | (9.55) | — |
| 511 | Deferred tax | 16.79 | 27.52 | 3.47 | 44.69 | — |
| 512 | Total Tax Expenses | 20.36 | 16.80 | 4.85 | 42.38 | — |
| 514-516 | VII Profit for period before JV share | 59.23 | 77.45 | 4.83 | 139.46 | — |
| 517 | VIII Share in profit of Joint venture (equity method) | 3.11 | 14.32 | 1.72 | 21.39 | — |
| 518 | IX Profit for the period/year | 62.34 | 91.77 | 6.55 | 160.85 | — |
| 522 | Re-measurements gain/(loss) of net defined benefit plans | (2.36) | (1.30) | (1.05) | (0.93) | — |
| 523 | Income tax effect on above (defined benefit) | 0.04 | (0.07) | - | (0.09) | — |
| 524-526 | Share of OCI of JV (defined benefit), equity method | - | (0.17) | - | (0.17) | Not all-zero (2 of 4 periods non-zero) — not flagged ZERO_STANDING |
| 528 | Fair value gain/(loss) on investments and other financial instruments | (0.76) | (1.11) | (0.17) | (0.80) | — |
| 529 | Income tax effect on above (fair value) | - | - | - | - | **ZERO_STANDING** |
| 530-532 | Share of OCI of JV (fair value), equity method | - | - | - | - | **ZERO_STANDING** |
| 533 | (c) Exchange difference on translation of foreign operations | (2.56) | 20.54 | 24.55 | 69.91 | — |
| 534 | Total OCI for the period/year (a+b+c) | (5.64) | 17.89 | 23.33 | 67.92 | — |
| 536 | XI Total Comprehensive Income | 56.70 | 109.66 | 29.88 | 228.77 | — |
| 538 | Profit attributable to: Shareholders of parent | 61.44 | 91.28 | 6.54 | 159.61 | — |
| 539 | Profit attributable to: Non-controlling Interest | 0.90 | 0.49 | 0.01 | 1.24 | — |
| 542 | OCI attributable to: Shareholders of parent | (5.64) | 17.89 | 23.33 | 67.92 | — |
| 543 | OCI attributable to: Non-controlling Interest | - | - | - | - | **ZERO_STANDING** |
| 546 | TCI attributable to: Shareholders of parent | 55.80 | 109.17 | 29.87 | 227.53 | — |
| 547 | TCI attributable to: Non-controlling Interest | 0.90 | 0.49 | 0.01 | 1.24 | — |
| 549 | XV Paid up Equity Share Capital (FV ₹5) | 54.60 | 54.60 | 54.60 | 54.60 | — |
| 550 | XVI Other Equity | (blank) | (blank) | (blank) | 3,197.36 | Annual-column-only, not a dash/nil |
| 552 | Basic EPS | 5.63 | 8.36 | 0.60 | 14.62 | — |
| 553 | Diluted EPS | 5.62 | 8.34 | 0.60 | 14.59 | — |

### 7d. Consolidated Reg 52(4) Additional Disclosures (page 10, lines 573-588) — 16 line items

| Line | Item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|------|------|--------|--------|--------|------|-------|
| 573 | a) Net Worth (₹ Cr) | 3,318.38 | 3,260.25 | 3,057.57 | 3,260.25 | — |
| 574 | b) Outstanding Unsecured NCDs (₹ Cr) | 181.25 | 362.50 | 543.75 | 362.50 | — |
| 575 | c) Debt service coverage ratio (x) | 0.18 | 0.20 | 0.09 | 0.59 | — |
| 576 | d) Interest service coverage ratio (x) | 5.12 | 4.76 | 1.33 | 2.83 | — |
| 577 | e) Debt equity ratio (x) | 0.27 | 0.28 | 0.46 | 0.28 | — |
| 578 | f) Current Ratio (x) | 0.81 | 0.76 | 0.82 | 0.76 | — |
| 579 | g) Long term debt to working capital ratio (x) | (2.03) | (2.06) | (3.78) | (2.06) | — |
| 580 | h) Bad debts to Account receivable ratio (%) | 0.0% | 0.0% | 0.0% | 0.2% | Not ZERO_STANDING — FY26 column is 0.2%, unlike the standalone table's all-zero equivalent (line 216). Flag for A4: bad debts exist at consolidated (subsidiary) level despite standalone nil. |
| 581 | i) Current liability ratio (x) | 0.81 | 0.81 | 0.70 | 0.81 | — |
| 582 | j) Total debts to total assets (x) | 0.18 | 0.18 | 0.27 | 0.18 | — |
| 583 | k) Debtors Turnover Ratio (x) | 2.29 | 2.57 | 2.45 | 9.71 | — |
| 584 | l) Inventory Turnover Ratio (x) | 1.61 | 1.70 | 1.44 | 6.19 | — |
| 585 | m) Basic EPS (₹) | 5.63 | 8.36 | 0.60 | 14.62 | — |
| 586 | n) Diluted EPS (₹) | 5.62 | 8.34 | 0.60 | 14.59 | — |
| 587 | o) Operating margin (%) | 37.0% | 40.6% | 40.1% | 39.8% | — |
| 588 | p) Net profit margin (%) | 6.0% | 8.7% | 0.8% | 4.2% | — |

### 7e. Consolidated Geographic Segment Table (page 11, lines 647-652) — 4 line items

| Line | Item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|------|------|--------|--------|--------|------|-------|
| 648 | Revenue from operations — Within India | 769.21 | 825.08 | 636.56 | 2,974.70 | — |
| 649 | Revenue from operations — Outside India | 262.73 | 224.98 | 184.85 | 846.14 | — |
| 651 | Non Current Assets — Within India | (blank) | (blank) | (blank) | 2,950.96 | Annual-column-only per template |
| 652 | Non Current Assets — Outside India | (blank) | (blank) | (blank) | 855.95 | Annual-column-only per template |

Note: standalone note 4 (line 272-274) states no reportable segments exist at the standalone level ("no overseas operations/units"); consolidated note 4 (line 635-637) states no reportable **business** segments but does disclose **geographic** segments — the two notes are not contradictory but the scope difference should be read together, not in isolation.

### 7f. Format of Security Cover — NIL (page 12, lines 709-846) — 31 line items, ALL ZERO_STANDING

This is a Regulation 54 template filed as NIL because SFL's outstanding NCDs are unsecured (per Board Outcome letter, Section 1, item 2). Per operating rule #3, every one of these template rows is enumerated as a standing (structural) disclosure unit, not dropped.

| # | Line | Item (Column A) | Section | Flags |
|---|------|------------------|---------|-------|
| 1 | 735-737 | Property, Plant and Equipment | ASSETS | ZERO_STANDING |
| 2 | 739-742 | Capital Work-in-Progress | ASSETS | ZERO_STANDING |
| 3 | 744-745 | Right of Use Assets | ASSETS | ZERO_STANDING |
| 4 | 747-748 | Goodwill | ASSETS | ZERO_STANDING |
| 5 | 751-752 | Intangible Assets | ASSETS | ZERO_STANDING |
| 6 | 757-759 | Intangible Assets under Development | ASSETS | ZERO_STANDING |
| 7 | 761-762 | Investments | ASSETS | ZERO_STANDING |
| 8 | 764-766 | Loans | ASSETS | ZERO_STANDING |
| 9 | 767-769 | Inventories | ASSETS | ZERO_STANDING |
| 10 | 770-772 | Trade Receivables | ASSETS | ZERO_STANDING |
| 11 | 774-776 | Cash and Cash Equivalents | ASSETS | ZERO_STANDING |
| 12 | 781-784 | Bank Balances other than Cash and Cash Equivalents | ASSETS | ZERO_STANDING |
| 13 | 787-788 | Others | ASSETS | ZERO_STANDING |
| 14 | 789 | Total (Assets) | ASSETS | ZERO_STANDING |
| 15 | 795-797 | Debt securities to which this certificate pertains | LIABILITIES | ZERO_STANDING |
| 16 | 801-805 | Other debt sharing pari-passu charge with above debt | LIABILITIES | ZERO_STANDING |
| 17 | 807-808 | Other Debt | LIABILITIES | ZERO_STANDING |
| 18 | 810-811 | Subordinated debt | LIABILITIES | ZERO_STANDING |
| 19 | 813-814 | Borrowings | LIABILITIES | ZERO_STANDING |
| 20 | 816-817 | Bank | LIABILITIES | ZERO_STANDING |
| 21 | 819-820 | Debt Securities (marked "Not to be filled") | LIABILITIES | ZERO_STANDING |
| 22 | 822-823 | Others | LIABILITIES | ZERO_STANDING |
| 23 | 826-827 | Trade payables | LIABILITIES | ZERO_STANDING |
| 24 | 829-830 | Lease Liabilities | LIABILITIES | ZERO_STANDING |
| 25 | 832-833 | Provisions | LIABILITIES | ZERO_STANDING |
| 26 | 835-837 | Others | LIABILITIES | ZERO_STANDING |
| 27 | 838 | Total (Liabilities) | LIABILITIES | ZERO_STANDING |
| 28 | 839-840 | Cover on Book Value | Summary | ZERO_STANDING |
| 29 | 841-842 | Cover on Market Value (ix) | Summary | ZERO_STANDING |
| 30 | 843-845 | Exclusive Security Cover Ratio | Summary | ZERO_STANDING |
| 31 | 843-845 | Pari Passu Security Cover Ratio | Summary | ZERO_STANDING |

---

## 8. ANNEXURES

Beyond the Security Cover NIL format (Section 7f, an annexure to the Board Outcome letter), no further annexures (e.g., director profile annexures, ESOP grant annexures) are present in this extract. This is consistent with the absence noted in Section 1 (no director appointment agenda item found), but is flagged again here per instruction item 4 ("every annexure and every table inside every annexure") since the task brief's premise of a same-day director appointment would normally carry a director-profile annexure (name, DIN, role, term dates, background, relationships) — none exists in this extract.

---

## 9. FLAGS SUMMARY

| Flag | Count | Where |
|------|-------|-------|
| ZERO_STANDING | 38 | Section 7 (line items 166, 176, 179, 216 standalone; 529, 530-532, 543 consolidated; all 31 rows of Security Cover NIL table) |
| ENTITY_CHANGE | 1 | Section 6 — Furlenco Global Pte. Ltd. marked "(upto 01.04.2026)", exiting consolidation |
| SIGNATURE_BEFORE_MEETING_CONCLUDED | 3 (+1 borderline) | Section 2 — Rahul Gautam (standalone 15:32:07, consolidated 15:32:54) and Nipun Gupta standalone report (15:44:30) all precede the stated 03:45 PM board conclusion (line 41); Nipun Gupta consolidated report (15:45:09) clears by 9 seconds only |
| EXPECTED_AGENDA_ITEM_NOT_FOUND | 1 | Section 1 — task brief asserts a same-day director appointment; not present anywhere in this extract |
