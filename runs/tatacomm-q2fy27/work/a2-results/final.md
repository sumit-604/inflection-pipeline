# A2 COMPLETENESS LEDGER - Tata Communications Limited (TATACOMM) - results - q2fy27
source of truth: runs/tatacomm-q2fy27/extracted/tatacomm-results-q2fy27-structured.md (R001-R1778). Rows reference A1 IDs; verbatim values stay in the structured file.
Prior-quarter ledger: not available (ND). ENTITY_CHANGE flags rest on in-document wef/upto qualifiers only; no list-vs-list diff possible.

=== A2 COUNT TEST ===
category: notes            grep_count: 18   sweep_count: 18   match: yes
category: footnotes        grep_count: 28   sweep_count: 28   match: yes   (+3 FOOTNOTE_UNRESOLVED in 2c)
category: line_items (fulltext lines with decimal cells vs ledger lines)  grep_count: 330   sweep_count: 330   match: yes
category: line_item_cells  grep_count: 1260   sweep_count: 1260   match: yes   (ledger line rows: 356)
category: zero_standing    grep_count: 87   sweep_count: 87   match: yes   (lines with a zero cell: 36)
category: agenda_items     grep_count: 3   sweep_count: 3   match: yes   (letter items (i)-(iii); A4 timing and A5 absence rows added)
category: auditor_paras    grep_count: 11   sweep_count: 11   match: yes
category: entities_consol  grep_count: 75   sweep_count: 75   match: yes
category: entities_total   grep_count: 132   sweep_count: 132   match: yes
category: dates            grep_count: 71   sweep_count: 71   match: yes
category: forward          grep_count: 32   sweep_count: 32   match: yes
category: signatures       grep_count: 4   sweep_count: 4   match: yes
category: slides / turns / questions: not applicable (results filing)
ids_in_structured: 1778 | ids_referenced_in_ledger: 1778 (primary placement: 1778) | orphan_ids: [] | match: yes
gate_a2: pass
=== END COUNT TEST ===

## 1. AGENDA ITEMS (Board Outcome letter, pp1-2) - cross-reference rows
Board meeting: commenced 10:30 IST, concluded 13:45 IST on 15-Oct-2026 = 3h15m (R006, R007, R1583). Letter signed by Company Secretary 13:52:19 (R015, R1586).
| AGENDA_ID | item | supporting ROW IDs | A2 flags / note |
|---|---|---|---|
| A1 | (i) Unaudited standalone and consolidated results, quarter and half-year to 30-Sep-2026, with Limited Review Report (unmodified) and press release | R1424,R1584,R1587,R1643,R1653 | Attachments A, B, C |
| A2 | (ii) Other Restructuring: transfer of entire Kaleyra, Inc. shareholding to Tata Communications (Netherlands) B.V. (TCNL), consideration in TCNL shares at FMV | R1402-R1410,R1425-R1426,R1546-R1547,R1550-R1552,R1574-R1579,R1650 | Attachment D. ENTITY_CHANGE candidate (Kaleyra becomes direct subsidiary of TCNL, R1578). Intra-group; benefit to promoter Nil (R1778, R1410). Cross-check: Kaleyra Africa (Pty) deconsolidated upto 04-Sep-2026 (R1509, R1634, R1757). |
| A3 | (iii) Change in KMP: appointment of Ms. Ridhi Sood as Company Secretary and Compliance Officer w.e.f. 01-Nov-2026 | R014,R1411-R1417,R1428-R1430,R1548-R1549,R1553-R1554,R1580-R1581,R1585,R1651-R1652 | Attachment E. Incumbent signatory Zubin Adil Patel (R1430); letter does not say whether he leaves. |
| A4 | Meeting timing | R006-R007,R1583 | 3h15m meeting. |
| A5 | Standard items NOT on this agenda: annual report approval, AGM notice, record date, dividend, director appointment, auditor change, scrutinizer, ESOP grant, capital-raising resolution | R1582 | ABSENCE row. Letter lists only items (i)-(iii). No dividend item. |

## 2. NOTES (numbered / lettered) and FOOTNOTES
### 2a Notes
| ROW_ID | note | A2 flags | cross-ref / materiality |
|---|---|---|---|
| R1678 | consol note 1 (limited review, approval 15-Oct-2026) | RESTATED | restated on standalone at R1733 |
| R1684 | consol note 2a (staff cost optimisation) | RESTATED | restated on standalone at R1739 |
| R1685 | consol note 2b (gain on sale of held-for-sale assets) | RESTATED | restated on standalone at R1740 |
| R1686 | consol note 2c (Labour Codes provision and reversal) | RESTATED | restated on standalone at R1741; Rs 60.58cr FY26 provision, Rs 18.52cr Q1 FY27 reversal sit in qualifier text |
| R1687 | consol note 2d (accidental damages / fire at third party DC) | RESTATED | restated on standalone at R1742; ties to exceptional item d |
| R1688 | consol note 2e (provision, contractual obligation) | RESTATED | restated on standalone at R1743 |
| R1689 | consol note 3 (DOT demand notices) | RESTATED,CONTINGENT_LIABILITY | restated on standalone at R1744; also auditor emphasis paragraph (section 5) |
| R1690 | consol note 3 classification (contingent vs remote) | CONTINGENT_LIABILITY | also auditor emphasis paragraph (section 5) |
| R1691 | consol note 4 (foreign subsidiary VAT) | CONTINGENT_LIABILITY | also auditor emphasis paragraph (section 5) |
| R1692 | consol note 5 (discontinued ops, subsidiary deconsolidated) | DISCONTINUED_OPS | - |
| R1696 | consol note 6 (FY26 OCI gain, DTL) | - | - |
| R1733 | standalone note 1 | RESTATED | restates R1678 |
| R1739 | standalone note a | RESTATED | restates R1684 |
| R1740 | standalone note b | RESTATED | restates R1685 |
| R1741 | standalone note c | RESTATED | restates R1686 |
| R1742 | standalone note d | RESTATED | restates R1687 |
| R1743 | standalone note e | RESTATED | restates R1688 |
| R1744 | standalone note 3 | RESTATED | restates R1689 |
Standalone has no notes 4-6 (consolidated only): note 4 VAT, note 5 discontinued ops, note 6 OCI. Numeric facts inside notes sit in section 7b.
### 2b Footnotes and markers (asterisk, @, #, $, bracket convention)
| ROW_ID | page/line | A2 flags | pairing |
|---|---|---|---|
| R1670 | p9/L403 | RESOLVED | marker -> text R1676 |
| R1672 | p9/L417 | RESOLVED | marker -> text R1677 |
| R1675 | p10/L493 | RESOLVED | cash-flow bracket convention |
| R1676 | p10/L494 | RESOLVED | text for R1670 |
| R1677 | p10/L495 | RESOLVED | text for R1672 |
| R1693 | p12/L593 | RESOLVED | marker -> text R1695 |
| R1694 | p12/L595 | RESOLVED | marker -> text R1695 |
| R1695 | p12/L597 | RESOLVED | text for R1693,R1694 |
| R1700 | p17/L819 | RESOLVED | marker -> text R1707 |
| R1703 | p17/L851 | RESOLVED | marker -> text R1706 |
| R1704 | p18/L879 | RESOLVED | marker -> text R1706 |
| R1705 | p18/L888 | RESOLVED | cash-flow bracket convention |
| R1706 | p18/L889 | RESOLVED | text for R1703,R1704 |
| R1707 | p18/L890 | RESOLVED | text for R1700 |
| R1710 | p18/L904 | RESOLVED | marker -> text R1714 |
| R1712 | p18/L909 | RESOLVED | marker -> text R1715 |
| R1714 | p18/L917 | RESOLVED | text for R1710 |
| R1715 | p18/L918 | RESOLVED | text for R1712 (refers to note 2) |
| R1716 | p19/L928 | RESOLVED | marker -> text R1731 |
| R1719 | p19/L935 | RESOLVED | marker -> text R1730 |
| R1721 | p19/L938 | RESOLVED | marker -> text R1732 |
| R1722 | p19/L940 | RESOLVED | marker -> text R1730 |
| R1726 | p19/L948 | RESOLVED | marker -> text R1730 |
| R1730 | p19/L955 | RESOLVED | text for R1719,R1722,R1726 |
| R1731 | p19/L956 | RESOLVED | text for R1716 |
| R1732 | p19/L957 | RESOLVED | text for R1721 |
| R1770 | p29/L1387 | RESOLVED | marker -> text R1771 |
| R1771 | p29/L1389 | RESOLVED | text for R1770 |
### 2c Unresolved footnotes
| ROW_ID | page/line | A2 flags | note |
|---|---|---|---|
| R1766 | p28/L1363 | FOOTNOTE_UNRESOLVED | press release headline metric stated without a definition; no reconciliation to the filed P&L |
| R1767 | p28/L1365 | FOOTNOTE_UNRESOLVED | press release headline metric stated without a definition; no reconciliation to the filed P&L |
| R1768 | p28/L1366 | FOOTNOTE_UNRESOLVED | press release headline metric stated without a definition; no reconciliation to the filed P&L |
### 2d Note-reference and column qualifiers
| ROW_ID | page/line | A2 flags | note |
|---|---|---|---|
| R1654 | p3/L129 | - | refer-note / column qualifier |
| R1655 | p3/L134 | - | refer-note / column qualifier |
| R1656 | p3/L134 | - | refer-note / column qualifier |
| R1657 | p3/L148 | - | refer-note / column qualifier |
| R1658 | p3/L152 | - | refer-note / column qualifier |
| R1659 | p3/L162 | - | refer-note / column qualifier |
| R1660 | p4/L185 | - | refer-note / column qualifier |
| R1661 | p4/L188 | - | refer-note / column qualifier |
| R1662 | p4/L200 | - | refer-note / column qualifier |
| R1663 | p4/L205 | - | refer-note / column qualifier |
| R1671 | p9/L413 | - | refer-note / column qualifier |
| R1673 | p9/L418 | - | refer-note / column qualifier |
| R1674 | p10/L461 | - | refer-note / column qualifier |
| R1679 | p11/L515 | - | refer-note / column qualifier |
| R1680 | p11/L518 | - | refer-note / column qualifier |
| R1681 | p11/L520 | - | refer-note / column qualifier |
| R1682 | p11/L522 | - | refer-note / column qualifier |
| R1683 | p11/L525 | - | refer-note / column qualifier |
| R1697 | p13/L620 | - | refer-note / column qualifier |
| R1698 | p13/L632 | - | refer-note / column qualifier |
| R1699 | p13/L649 | - | refer-note / column qualifier |
| R1701 | p17/L821 | - | refer-note / column qualifier |
| R1702 | p17/L849 | - | refer-note / column qualifier |
| R1708 | p18/L892 | - | refer-note / column qualifier |
| R1734 | p19/L972 | - | refer-note / column qualifier |
| R1735 | p19/L975 | - | refer-note / column qualifier |
| R1736 | p19/L978 | - | refer-note / column qualifier |
| R1737 | p19/L979 | - | refer-note / column qualifier |
| R1738 | p19/L982 | - | refer-note / column qualifier |
| R1763 | p25/L1265 | - | blank-page placeholder |
| R1769 | p29/L1380 | - | refer-note / column qualifier |
### 2e Segment definitions and ratio definitions
| ROW_ID | page/line | A2 flags | note |
|---|---|---|---|
| R1664 | p6/L288 | - | segment definition |
| R1665 | p6/L291 | - | segment definition |
| R1666 | p6/L292 | - | segment definition |
| R1667 | p6/L293 | - | segment definition |
| R1668 | p6/L297 | - | segment definition |
| R1669 | p6/L301 | - | segment definition |
| R1709 | p18/L903 | - | ratio/margin definition |
| R1711 | p18/L908 | - | ratio/margin definition |
| R1713 | p18/L914 | - | ratio/margin definition |
| R1717 | p19/L929 | - | ratio/margin definition |
| R1718 | p19/L933 | - | ratio/margin definition |
| R1720 | p19/L936 | - | ratio/margin definition |
| R1723 | p19/L941 | - | ratio/margin definition |
| R1724 | p19/L944 | - | ratio/margin definition |
| R1725 | p19/L947 | - | ratio/margin definition |
| R1727 | p19/L950 | - | ratio/margin definition |
| R1728 | p19/L953 | - | ratio/margin definition |
| R1729 | p19/L954 | - | ratio/margin definition |
Consolidated has 5 segments (R1431); standalone has 3 (R1443). Data Services includes digital platforms and connected services (R1666).
### 2f Legal and Attachment D qualifiers
| ROW_ID | page/line | A2 flags | note |
|---|---|---|---|
| R1772 | p30/L1454 | - | disclaimer / image alt text |
| R1773 | p30/L1461 | - | disclaimer / image alt text |
| R1774 | p31/L1482 | - | disclaimer / image alt text |
| R1775 | p32/L1501 | - | Attachment D qualifier |
| R1776 | p32/L1511 | - | Attachment D qualifier |
| R1777 | p32/L1512 | - | Attachment D qualifier |
| R1778 | p32/L1514 | - | Attachment D qualifier |

## 3. FINANCIAL TABLE LINE ITEMS (every line, including zero and dash cells)
One row per table line (page/line). Cells are the period columns, referenced by ID range. Label shown for lookup only.
| page/line | label | ROW IDs | cells | A2 flags |
|---|---|---|---|---|
| **p3** | **CONSOL P&L** | | | |
| p3/L135 | 1 Income from operations | R019-R024 | 6 | - |
| p3/L136 | 2 Other income/(loss), net | R025-R030 | 6 | - |
| p3/L137 | 3 Total income (1 + | R031-R036 | 6 | - |
| p3/L139 | a. Network and transmission expense | R037-R042 | 6 | - |
| p3/L140 | b. Employee benefits expense | R043-R048 | 6 | - |
| p3/L141 | c. Finance costs | R049-R054 | 6 | - |
| p3/L142 | d. Depreciation and amortisation expense | R055-R060 | 6 | - |
| p3/L143 | e. Other expenses | R061-R066 | 6 | - |
| p3/L144 | Total expenses (4a to 4e) | R067-R072 | 6 | - |
| p3/L146 | 5 Profit before exceptional items, tax & | R073-R078 | 6 | - |
| p3/L147 | share in profit of associates (3 - | R079 | 1 | - |
| p3/L148 | 6 Exceptional items (Refer note | R080-R085 | 6 | - |
| p3/L150 | 7 Profit before tax and share in profit of | R086-R091 | 6 | - |
| p3/L151 | associates (5 + | R092 | 1 | - |
| p3/L152 | 8 Tax expense/(benefit): (Refer note | R093 | 1 | - |
| p3/L153 | a. Current tax | R094-R099 | 6 | - |
| p3/L154 | b. Deferred tax | R100-R105 | 6 | - |
| p3/L156 | 9 Profit before share in profit/(losses) of | R106-R111 | 6 | - |
| p3/L157 | associates for the period/year (7 - | R112 | 1 | - |
| p3/L158 | 10 Share in profit/(losses) of associates | R113-R118 | 6 | - |
| p3/L160 | 11 Profit after tax for the period/ year fro | R119-R124 | 6 | - |
| p3/L161 | continuing operations (9 + | R125 | 1 | - |
| p3/L162 | 12 Loss on sale of subsidiary (refer note | R126-R131 | 6 | ZERO_STANDING 4 of 6 cells (R126-R129) |
| p3/L163 | 13 Loss after tax from discontinued operatio | R132-R137 | 6 | ZERO_STANDING 4 of 6 cells (R132-R135) |
| p3/L164 | 14 Profit for the period/year (11+13) | R138-R143 | 6 | - |
| p3/L166 | Equity holders of the parent | R144-R149 | 6 | - |
| p3/L167 | Non-controlling interest | R150-R155 | 6 | - |
| **p4** | **CONSOL P&L (OCI/EPS)** | | | |
| p4/L188 | Other Comprehensive Income/(loss) | R157-R162 | 6 | - |
| p4/L189 | (net of tax) (refer note | R163 | 1 | - |
| p4/L191 | Equity holders of the parent | R164-R169 | 6 | - |
| p4/L192 | Non-controlling interest | R170-R175 | 6 | - |
| p4/L194 | Total Comprehensive income/(loss) for the pe | R176-R181 | 6 | - |
| p4/L197 | Equity holders of the parent | R182-R187 | 6 | - |
| p4/L198 | Non-controlling interest | R188-R193 | 6 | - |
| p4/L200 | Paid up equity share capital (Face value of  | R194-R199 | 6 | - |
| p4/L201 | face value per share Rs, paid-up capital lin | R200 | 1 | - |
| p4/L203 | face value per share Rs (EPS basis), consoli | R201 | 1 | - |
| p4/L204 | Earnings per share (of ` 10/- each) (not ann | R202 | 1 | - |
| p4/L207 | (i) Basic (`) | R203-R208 | 6 | - |
| p4/L208 | (ii) Diluted earnings per share (`) | R209-R214 | 6 | - |
| p4/L210 | (i) Basic (`) | R215-R220 | 6 | ZERO_STANDING 4 of 6 cells (R215-R218) |
| p4/L211 | (ii) Diluted earnings per share (`) | R221-R226 | 6 | ZERO_STANDING 4 of 6 cells (R221-R224) |
| p4/L213 | (i) Basic (`) | R227-R232 | 6 | - |
| p4/L214 | (ii) Diluted earnings per share (`) | R233-R238 | 6 | - |
| **p5** | **CONSOL SEGMENT RESULTS** | | | |
| p5/L234 | Voice Solutions | R240-R245 | 6 | - |
| p5/L235 | Data Services | R246-R251 | 6 | - |
| p5/L236 | Transformation Services | R252-R257 | 6 | - |
| p5/L237 | Real Estate | R258-R263 | 6 | - |
| p5/L238 | Campaign Registry | R264-R269 | 6 | - |
| p5/L239 | Less: Inter Segment Revenue | R270-R275 | 6 | - |
| p5/L240 | Total | R276-R281 | 6 | - |
| p5/L242 | Voice Solutions | R282-R287 | 6 | - |
| p5/L243 | Data Services | R288-R293 | 6 | - |
| p5/L244 | Transformation Services | R294-R299 | 6 | - |
| p5/L245 | Real Estate | R300-R305 | 6 | - |
| p5/L246 | Campaign Registry | R306-R311 | 6 | - |
| p5/L247 | Total | R312-R317 | 6 | - |
| p5/L249 | (i) Finance Costs | R318-R323 | 6 | - |
| p5/L251 | (ii) Other un-allocable (income) net of un-a | R324-R329 | 6 | - |
| p5/L254 | Profit before tax and share in profit of ass | R330-R335 | 6 | - |
| **p6** | **CONSOL SEGMENT ASSETS/LIABS** | | | |
| p6/L269 | Voice Solutions | R337-R340 | 4 | - |
| p6/L270 | Data Services | R341-R344 | 4 | - |
| p6/L271 | Transformation Services | R345-R348 | 4 | - |
| p6/L272 | Real Estate | R349-R352 | 4 | - |
| p6/L273 | Campaign Registry | R353-R356 | 4 | - |
| p6/L274 | (unlabelled row) | R357-R360 | 4 | - |
| p6/L275 | Unallocated Assets | R361-R364 | 4 | - |
| p6/L276 | Total Segment Assets | R365-R368 | 4 | - |
| p6/L278 | Voice Solutions | R369-R372 | 4 | - |
| p6/L279 | Data Services | R373-R376 | 4 | - |
| p6/L280 | Transformation Services | R377-R380 | 4 | - |
| p6/L281 | Real Estate | R381-R384 | 4 | - |
| p6/L282 | Campaign Registry | R385-R388 | 4 | - |
| p6/L283 | (unlabelled row) | R389-R392 | 4 | - |
| p6/L284 | Unallocated Liabilities | R393-R396 | 4 | - |
| p6/L285 | Total Segment Liabilities | R397-R400 | 4 | - |
| **p7** | **CONSOL BS (assets)** | | | |
| p7/L317 | (a) Property, plant and equipment | R402-R403 | 2 | - |
| p7/L318 | (b) Capital work-in-progress | R404-R405 | 2 | - |
| p7/L319 | (c) Right-of-use assets | R406-R407 | 2 | - |
| p7/L320 | (d) Investment property | R408-R409 | 2 | - |
| p7/L321 | (e) Goodwill | R410-R411 | 2 | - |
| p7/L322 | (f) Other intangible assets | R412-R413 | 2 | - |
| p7/L323 | (g) Intangible assets under development | R414-R415 | 2 | - |
| p7/L326 | (a) Investments in associates | R416-R417 | 2 | - |
| p7/L327 | (b) Other investments | R418-R419 | 2 | - |
| p7/L328 | (ii) Other financial assets | R420-R421 | 2 | - |
| p7/L329 | (i) Deferred tax assets (net) | R422-R423 | 2 | - |
| p7/L330 | (j) Non-current tax assets (net) | R424-R425 | 2 | - |
| p7/L331 | (k) Other non-current assets | R426-R427 | 2 | - |
| p7/L332 | Total Non-current assets | R428-R429 | 2 | - |
| p7/L335 | (a) Inventories | R430-R431 | 2 | - |
| p7/L337 | (i) Other investments | R432-R433 | 2 | - |
| p7/L338 | (ii) Trade receivables | R434-R435 | 2 | - |
| p7/L339 | (iii) Cash and cash equivalents | R436-R437 | 2 | - |
| p7/L340 | (iv) Bank balances other than (iii) above | R438-R439 | 2 | - |
| p7/L341 | (v) Other financial assets | R440-R441 | 2 | - |
| p7/L342 | (c) Other current assets | R442-R443 | 2 | - |
| p7/L343 | (unlabelled row) | R444-R445 | 2 | - |
| p7/L344 | Assets classified as held for sale | R446-R447 | 2 | - |
| p7/L345 | Total Current assets | R448-R449 | 2 | - |
| p7/L346 | TOTAL ASSETS | R450-R451 | 2 | - |
| **p8** | **CONSOL BS (equity/liabs)** | | | |
| p8/L361 | (a) Equity share capital | R453-R454 | 2 | - |
| p8/L362 | (b) Other equity | R455-R456 | 2 | - |
| p8/L363 | Equity attributable to equity holders of the | R457-R458 | 2 | - |
| p8/L366 | Non-controlling interests | R459-R460 | 2 | - |
| p8/L368 | Total Equity | R461-R462 | 2 | - |
| p8/L373 | (i) Borrowings | R463-R464 | 2 | - |
| p8/L374 | (ia) Lease liabilities | R465-R466 | 2 | - |
| p8/L375 | (ii) Other financial liabilities | R467-R468 | 2 | - |
| p8/L376 | (b) Provisions | R469-R470 | 2 | - |
| p8/L377 | (c) Deferred tax liabilities (net) | R471-R472 | 2 | - |
| p8/L378 | (d) Other non-current liabilities | R473-R474 | 2 | - |
| p8/L379 | Total Non-current liabilities | R475-R476 | 2 | - |
| p8/L382 | (i) Borrowings | R477-R478 | 2 | - |
| p8/L383 | (ia) Lease liabilities | R479-R480 | 2 | - |
| p8/L384 | (ii) Trade payables | R481-R482 | 2 | - |
| p8/L385 | (iii) Other financial liabilities | R483-R484 | 2 | - |
| p8/L386 | (b) Provisions | R485-R486 | 2 | - |
| p8/L387 | (c) Current tax liabilities (net) | R487-R488 | 2 | - |
| p8/L388 | (d) Other current liabilities | R489-R490 | 2 | - |
| p8/L389 | Total Current liabilities | R491-R492 | 2 | - |
| p8/L390 | TOTAL EQUITY AND LIABILITIES | R493-R494 | 2 | - |
| **p9** | **CONSOL CASH FLOW (operating)** | | | |
| p9/L407 | Continuing Operations | R496-R498 | 3 | - |
| p9/L408 | Discontinued Operations | R499-R501 | 3 | ZERO_STANDING 1 of 3 cells (R499) |
| p9/L409 | Continuing and Discontinued Operations | R502-R504 | 3 | - |
| p9/L411 | Depreciation and amortisation expense | R505-R507 | 3 | - |
| p9/L412 | Gain on disposal of property, plant and equi | R508-R510 | 3 | - |
| p9/L413 | Gain on disposal of assets held for sale (re | R511-R513 | 3 | ZERO_STANDING 1 of 3 cells (R511) |
| p9/L414 | Gain on modification/ termination of lease | R514-R516 | 3 | - |
| p9/L415 | Interest income on financial assets carried  | R517-R519 | 3 | - |
| p9/L416 | Finance cost | R520-R522 | 3 | - |
| p9/L417 | Accidental damages (refer note 2d)** | R523-R525 | 3 | ZERO_STANDING 2 of 3 cells (R524-R525) |
| p9/L418 | Reclassification of FCTR to P&L on sale of s | R526-R528 | 3 | ZERO_STANDING 1 of 3 cells (R526) |
| p9/L419 | Bad debts written off | R529-R531 | 3 | - |
| p9/L420 | Allowance/(Reversal) for trade receivables | R532-R534 | 3 | - |
| p9/L421 | Provision for inventories and CWIP | R535-R537 | 3 | - |
| p9/L422 | Accrual for share-based payments | R538-R540 | 3 | - |
| p9/L423 | Allowance for doubtful advances | R541-R543 | 3 | - |
| p9/L424 | Gain on investments carried at fair value th | R544-R546 | 3 | - |
| p9/L425 | Exchange fluctuation | R547-R549 | 3 | - |
| p9/L427 | OPERATING PROFIT BEFORE WORKING CAPITAL CHAN | R550-R552 | 3 | - |
| p9/L431 | Inventories | R553-R555 | 3 | - |
| p9/L432 | Trade receivables | R556-R558 | 3 | - |
| p9/L433 | Other assets | R559-R561 | 3 | - |
| p9/L435 | Trade payables | R562-R564 | 3 | - |
| p9/L436 | Other liabilities | R565-R567 | 3 | - |
| p9/L437 | Provisions | R568-R570 | 3 | - |
| p9/L438 | Adjustment of translation differences on wor | R571-R573 | 3 | - |
| p9/L439 | Cash generated from operations before tax | R574-R576 | 3 | - |
| p9/L440 | Income tax (paid)/refund (net) | R577-R579 | 3 | - |
| p9/L441 | NET CASH FLOW FROM OPERATING ACTIVITIES | R580-R582 | 3 | - |
| **p10** | **CONSOL CASH FLOW (invest/finance)** | | | |
| p10/L458 | Payment to purchase of property, plant and e | R584-R586 | 3 | - |
| p10/L459 | Proceeds from disposal of property, plant an | R587-R589 | 3 | - |
| p10/L460 | Advance received towards assets held for sal | R590-R592 | 3 | - |
| p10/L461 | Proceeds from disposal of asset held for sal | R593-R595 | 3 | ZERO_STANDING 1 of 3 cells (R593) |
| p10/L462 | Purchase of investments in associates | R596-R598 | 3 | - |
| p10/L463 | Acquisition of Subsidiary (net off acquired  | R599-R601 | 3 | ZERO_STANDING 2 of 3 cells (R599-R600) |
| p10/L464 | Proceeds towards return of capital on non-cu | R602-R604 | 3 | - |
| p10/L465 | Proceeds from sale of non-current investment | R605-R607 | 3 | ZERO_STANDING 1 of 3 cells (R605) |
| p10/L466 | Purchase of current investments | R608-R610 | 3 | - |
| p10/L467 | Proceeds from sale of current investments | R611-R613 | 3 | - |
| p10/L468 | Fixed deposits liquidated/(placed) (net) | R614-R616 | 3 | - |
| p10/L469 | Earmarked funds liquidated/(placed) (net) | R617-R619 | 3 | - |
| p10/L470 | Interest received | R620-R622 | 3 | - |
| p10/L471 | NET CASH USED IN INVESTING ACTIVITIES | R623-R625 | 3 | - |
| p10/L473 | (unlabelled row) | R626 | 1 | - |
| p10/L474 | Proceeds from Short-term borrowings | R627-R629 | 3 | - |
| p10/L475 | Repayment of Short-term borrowings | R630-R632 | 3 | - |
| p10/L476 | Proceeds from Long-term borrowings | R633-R635 | 3 | - |
| p10/L477 | Repayment of Long-term borrowings | R636-R638 | 3 | - |
| p10/L478 | Repayment of lease liabilities | R639-R641 | 3 | - |
| p10/L479 | Dividends paid | R642-R644 | 3 | - |
| p10/L480 | Interest paid | R645-R647 | 3 | - |
| p10/L481 | Proceeds from exercise of share options | R648-R650 | 3 | ZERO_STANDING 2 of 3 cells (R649-R650) |
| p10/L482 | NET CASH USED IN FINANCING ACTIVITIES | R651-R653 | 3 | - |
| p10/L483 | NET (DECREASE)/INCREASE IN CASH AND CASH EQU | R654-R656 | 3 | - |
| p10/L485 | CASH AND CASH EQUIVALENTS AS AT THE BEGINNIN | R657-R659 | 3 | - |
| p10/L488 | Exchange difference on translation of foreig | R660-R662 | 3 | - |
| p10/L491 | CASH AND CASH EQUIVALENTS AS AT THE END OF T | R663-R665 | 3 | - |
| **p11** | **CONSOL EXCEPTIONAL ITEMS TABLE (note 2)** | | | |
| p11/L515 | 1. Staff cost optimization (Refer note a) | R667-R672 | 6 | - |
| p11/L517 | 2. Gain on sale of asset “held for sale” (Re | R673-R678 | 6 | ZERO_STANDING 3 of 6 cells (R673-R674,R676) |
| p11/L520 | 3. Statutory impact of new Labour Codes (Ref | R679-R684 | 6 | ZERO_STANDING 3 of 6 cells (R679,R681,R683) |
| p11/L522 | 4. Accidental damages (Refer note d) | R685-R690 | 6 | ZERO_STANDING 4 of 6 cells (R685,R687,R689-R690) |
| p11/L524 | 5. Provision for contractual obligation (Ref | R691-R696 | 6 | ZERO_STANDING 4 of 6 cells (R691,R693,R695-R696) |
| p11/L526 | Total | R697-R702 | 6 | - |
| **p12** | **CONSOL DISCONTINUED OPS TABLE (note 5)** | | | |
| p12/L589 | Revenue from Operations | R718-R722 | 5 | ZERO_STANDING 3 of 5 cells (R718-R720) |
| p12/L591 | Profit/(Loss) after tax from discontinued op | R723-R727 | 5 | ZERO_STANDING all 5 cells |
| p12/L593 | Loss on sale of subsidiary | R728-R732 | 5 | ZERO_STANDING 3 of 5 cells (R728-R730) |
| p12/L595 | Total Profit/(Loss) after tax from discontin | R733-R737 | 5 | ZERO_STANDING 3 of 5 cells (R733-R735) |
| **p13** | **STANDALONE P&L** | | | |
| p13/L621 | 1 Income from operations | R742-R747 | 6 | - |
| p13/L622 | 2 Other income, net | R748-R753 | 6 | - |
| p13/L623 | 3 Total Income (1+2) | R754-R759 | 6 | - |
| p13/L625 | a. Network and transmission expense | R760-R765 | 6 | - |
| p13/L626 | b. Employee benefits expense | R766-R771 | 6 | - |
| p13/L627 | c. Finance costs | R772-R777 | 6 | - |
| p13/L628 | d. Depreciation and amortisation expense | R778-R783 | 6 | - |
| p13/L629 | e. Other expenses | R784-R789 | 6 | - |
| p13/L630 | f. Total expenses (4a to 4e) | R790-R795 | 6 | - |
| p13/L631 | 5 Profit before exceptional items and tax (3 | R796-R801 | 6 | - |
| p13/L632 | 6 Exceptional items (refer note | R802-R807 | 6 | - |
| p13/L633 | 7 Profit before tax (5 + | R808-R813 | 6 | - |
| p13/L635 | a. Current tax | R814-R819 | 6 | - |
| p13/L636 | b. Deferred tax | R820-R825 | 6 | - |
| p13/L637 | 9 Profit for the period/ year (7 - | R826-R831 | 6 | - |
| p13/L639 | Other Comprehensive Income / (Loss) (net of  | R832-R837 | 6 | - |
| p13/L642 | Total Comprehensive Income / (Loss) for | R838-R843 | 6 | - |
| p13/L643 | the period/ year (9 + | R844 | 1 | - |
| p13/L645 | Paid up equity share capital (Face value of  | R845-R850 | 6 | - |
| p13/L646 | face value per share Rs, standalone | R851 | 1 | - |
| p13/L647 | 13 Reserves excluding Revaluation reserve | R852 | 1 | - |
| p13/L648 | 14 Net worth | R853 | 1 | - |
| p13/L649 | EPS face value, standalone | R854 | 1 | NONNUMERIC_VALUE (label fragment or text cell) |
| p13/L650 | Earnings per share (of ₹ 10/- each) (not ann | R855 | 1 | - |
| p13/L652 | Basic earnings per share (₹) | R856-R861 | 6 | - |
| p13/L653 | Diluted earnings per share (₹) | R862-R867 | 6 | - |
| **p14** | **STANDALONE SEGMENT (results + A&L)** | | | |
| p14/L670 | Voice Solutions | R869-R874 | 6 | - |
| p14/L671 | Data Services | R875-R880 | 6 | - |
| p14/L672 | Real Estate | R881-R886 | 6 | - |
| p14/L673 | Total | R887-R892 | 6 | - |
| p14/L675 | Voice Solutions | R893-R898 | 6 | - |
| p14/L676 | Data Services | R899-R904 | 6 | - |
| p14/L677 | Real Estate | R905-R910 | 6 | - |
| p14/L678 | Total | R911-R916 | 6 | - |
| p14/L680 | (i) Finance Costs | R917-R922 | 6 | - |
| p14/L682 | (ii) Other un-allocable (income) net of un-a | R923-R928 | 6 | - |
| p14/L685 | Profit/(Loss) before taxes | R929-R934 | 6 | - |
| p14/L693 | Voice Solutions | R935-R938 | 4 | - |
| p14/L694 | Data Services | R939-R942 | 4 | - |
| p14/L695 | Real Estate | R943-R946 | 4 | - |
| p14/L696 | Subtotal | R947-R950 | 4 | - |
| p14/L697 | Unallocable Assets | R951-R954 | 4 | - |
| p14/L698 | Total Assets | R955-R958 | 4 | - |
| p14/L700 | Voice Solutions | R959-R962 | 4 | - |
| p14/L701 | Data Services | R963-R966 | 4 | - |
| p14/L702 | Real Estate | R967-R970 | 4 | - |
| p14/L703 | Subtotal | R971-R974 | 4 | - |
| p14/L704 | Unallocable Liabilities | R975-R978 | 4 | - |
| p14/L705 | Total Liabilities | R979-R982 | 4 | - |
| **p15** | **STANDALONE BS (assets)** | | | |
| p15/L730 | (a) Property, plant and equipment | R984-R985 | 2 | - |
| p15/L731 | (b) Capital work-in-progress | R986-R987 | 2 | - |
| p15/L732 | (c) Right of Use Asset | R988-R989 | 2 | - |
| p15/L733 | (d) Investment property | R990-R991 | 2 | - |
| p15/L734 | (e) Other Intangible assets | R992-R993 | 2 | - |
| p15/L735 | (f) Intangible assets under development | R994-R995 | 2 | - |
| p15/L737 | (i) Investments | R996-R997 | 2 | - |
| p15/L738 | (ii) Loans | R998-R999 | 2 | - |
| p15/L739 | (iii) Other financial assets | R1000-R1001 | 2 | - |
| p15/L740 | h) Deferred tax assets (net) | R1002-R1003 | 2 | - |
| p15/L741 | i) Non – current tax assets (net) | R1004-R1005 | 2 | - |
| p15/L742 | (j) Other Non-current assets | R1006-R1007 | 2 | - |
| p15/L743 | Total Non-current assets | R1008-R1009 | 2 | - |
| p15/L745 | (a) Inventories | R1010-R1011 | 2 | - |
| p15/L747 | (i) Other Investments | R1012-R1013 | 2 | - |
| p15/L748 | (ii) Trade receivables | R1014-R1015 | 2 | - |
| p15/L749 | (iii) Cash and cash equivalents | R1016-R1017 | 2 | - |
| p15/L750 | (iv) Bank balances other than (iii) above | R1018-R1019 | 2 | - |
| p15/L751 | (v) Loans | R1020-R1021 | 2 | - |
| p15/L752 | (vi) Other financial assets | R1022-R1023 | 2 | - |
| p15/L753 | (c) Other Current assets | R1024-R1025 | 2 | - |
| p15/L754 | (unlabelled row) | R1026-R1027 | 2 | - |
| p15/L755 | Assets classified as held for sale | R1028-R1029 | 2 | - |
| p15/L756 | Total Current assets | R1030-R1031 | 2 | - |
| p15/L757 | TOTAL ASSETS | R1032-R1033 | 2 | - |
| **p16** | **STANDALONE BS (equity/liabs)** | | | |
| p16/L774 | (a) Equity share capital | R1035-R1036 | 2 | - |
| p16/L775 | (b) Other equity | R1037-R1038 | 2 | - |
| p16/L776 | LIABILITIES | R1039-R1040 | 2 | - |
| p16/L780 | (i) Borrowings | R1041-R1042 | 2 | - |
| p16/L781 | (ia) Lease liabilities | R1043-R1044 | 2 | - |
| p16/L782 | (ii) Other financial liabilities | R1045-R1046 | 2 | - |
| p16/L783 | (b) Provisions | R1047-R1048 | 2 | - |
| p16/L784 | (c) Other non - current liabilities | R1049-R1050 | 2 | - |
| p16/L785 | Total Non-current liabilities | R1051-R1052 | 2 | - |
| p16/L788 | (i) Borrowings | R1053-R1054 | 2 | - |
| p16/L789 | (ia) Lease liabilities | R1055-R1056 | 2 | - |
| p16/L791 | (A) Total outstanding dues of micro enterpri | R1057-R1058 | 2 | - |
| p16/L793 | (B) Total outstanding dues of creditors othe | R1059-R1060 | 2 | - |
| p16/L795 | (iii) Other financial liabilities | R1061-R1062 | 2 | - |
| p16/L796 | (b) Provisions | R1063-R1064 | 2 | - |
| p16/L797 | (c) Current tax liability (net) | R1065-R1066 | 2 | - |
| p16/L798 | (d) Other current liabilities | R1067-R1068 | 2 | - |
| p16/L799 | Total Current liabilities | R1069-R1070 | 2 | - |
| p16/L800 | TOTAL EQUITY AND LIABILITIES | R1071-R1072 | 2 | - |
| **p17** | **STANDALONE CASH FLOW (operating/invest)** | | | |
| p17/L814 | Profit from operations before tax for the pe | R1074-R1076 | 3 | - |
| p17/L816 | Depreciation and amortization expenses | R1077-R1079 | 3 | - |
| p17/L817 | Interest income on financial assets carried  | R1080-R1082 | 3 | - |
| p17/L818 | Finance cost | R1083-R1085 | 3 | - |
| p17/L819 | Accidental damages (refer note | R1086-R1088 | 3 | ZERO_STANDING 2 of 3 cells (R1087-R1088) |
| p17/L820 | Accrual for share-based payments | R1089-R1091 | 3 | - |
| p17/L821 | Gain on disposal of assets held for sale (re | R1092-R1094 | 3 | ZERO_STANDING 1 of 3 cells (R1092) |
| p17/L822 | Gain on investments carried at fair value th | R1095-R1097 | 3 | - |
| p17/L823 | Dividend income | R1098-R1100 | 3 | ZERO_STANDING 1 of 3 cells (R1098) |
| p17/L824 | Exchange fluctuation | R1101-R1103 | 3 | - |
| p17/L825 | Allowance/(Reversal) for doubtful trade rece | R1104-R1106 | 3 | - |
| p17/L826 | Gain on modification/ termination of lease | R1107-R1109 | 3 | - |
| p17/L827 | Provision for inventories and capital work-i | R1110-R1112 | 3 | - |
| p17/L828 | Allowance/(Reversal) for doubtful advances | R1113-R1115 | 3 | - |
| p17/L829 | Bad Debts written off | R1116-R1118 | 3 | - |
| p17/L830 | Advances written off | R1119-R1120 | 2 | ZERO_STANDING 1 of 2 cells (R1120) |
| p17/L831 | Gain on disposal of property, plant and equi | R1121-R1123 | 3 | - |
| p17/L832 | Operating Profit before working capital chan | R1124-R1126 | 3 | - |
| p17/L834 | Inventories | R1127-R1129 | 3 | - |
| p17/L835 | Trade receivables | R1130-R1132 | 3 | - |
| p17/L836 | Other assets | R1133-R1135 | 3 | - |
| p17/L838 | Trade payables | R1136-R1138 | 3 | - |
| p17/L839 | Other liabilities | R1139-R1141 | 3 | - |
| p17/L840 | Provisions | R1142-R1144 | 3 | - |
| p17/L841 | Cash generated from operations before tax | R1145-R1147 | 3 | - |
| p17/L842 | Income tax refund/(paid) (net) | R1148-R1150 | 3 | - |
| p17/L843 | Net cash flow from operating activities | R1151-R1153 | 3 | - |
| p17/L845 | Purchase of property, plant and equipment an | R1154-R1156 | 3 | - |
| p17/L847 | Proceeds from disposal of property, plant an | R1157-R1159 | 3 | - |
| p17/L849 | Proceeds from disposal of assets held for sa | R1160-R1162 | 3 | ZERO_STANDING 1 of 3 cells (R1160) |
| p17/L850 | Purchase of non-current investments | R1163-R1165 | 3 | - |
| p17/L851 | Proceeds from sale of non-current investment | R1166-R1167 | 2 | ZERO_STANDING all 2 cells |
| p17/L852 | Purchase of current investments | R1168-R1170 | 3 | - |
| p17/L853 | Proceeds from sale of current investments | R1171-R1173 | 3 | - |
| p17/L854 | Loan given to subsidiaries | R1174-R1176 | 3 | - |
| p17/L855 | Loan repaid by subsidiaries | R1177-R1179 | 3 | - |
| p17/L856 | Advance received towards assets held for sal | R1180-R1182 | 3 | - |
| p17/L857 | Dividend income from subsidiaries | R1183-R1185 | 3 | ZERO_STANDING 1 of 3 cells (R1183) |
| p17/L858 | Interest received | R1186-R1188 | 3 | - |
| p17/L859 | Fixed deposits placed (net) | R1189-R1191 | 3 | ZERO_STANDING 1 of 3 cells (R1190) |
| p17/L860 | Earmarked funds liquidated | R1192-R1194 | 3 | ZERO_STANDING 2 of 3 cells (R1192-R1193) |
| p17/L861 | Net cash from /(used in) investing activitie | R1195-R1197 | 3 | - |
| **p18** | **STANDALONE CASH FLOW (financing) + Reg52(4) margins** | | | |
| p18/L875 | Proceeds from short-term borrowings | R1199-R1201 | 3 | - |
| p18/L876 | Repayment of short-term borrowings | R1202-R1204 | 3 | - |
| p18/L877 | Proceeds from long-term borrowings (net off  | R1205-R1207 | 3 | ZERO_STANDING 1 of 3 cells (R1205) |
| p18/L878 | Repayment of long-term borrowings | R1208-R1210 | 3 | - |
| p18/L879 | Proceeds from sublease | R1211-R1212 | 2 | ZERO_STANDING all 2 cells |
| p18/L880 | Repayment of lease liabilities | R1213-R1215 | 3 | - |
| p18/L881 | Dividend paid | R1216-R1218 | 3 | - |
| p18/L882 | Interest paid | R1219-R1221 | 3 | - |
| p18/L883 | Proceeds from exercise of share options | R1222-R1224 | 3 | ZERO_STANDING 2 of 3 cells (R1223-R1224) |
| p18/L884 | Net cash (used in) /from financing activitie | R1225-R1227 | 3 | - |
| p18/L885 | Net Increase /(Decrease) in cash and cash eq | R1228-R1230 | 3 | - |
| p18/L886 | Cash and cash equivalents as at the beginnin | R1231-R1233 | 3 | - |
| p18/L887 | Cash and cash equivalents as at the end of t | R1234-R1236 | 3 | - |
| p18/L904 | Earnings before exceptional items, Interest  | R1237-R1242 | 6 | NONNUMERIC_VALUE (label fragment or text cell) |
| p18/L909 | Profit/(Loss) for the period/ Income from Op | R1243-R1248 | 6 | NONNUMERIC_VALUE (label fragment or text cell) |
| p18/L915 | depreciation and amortization and tax | R1249-R1254 | 6 | - |
| **p19** | **STANDALONE Reg52(4) ratios + EXCEPTIONAL TABLE** | | | |
| p19/L928 | 1. Asset coverage ratio (no. of times) | R1256-R1257 | 2 | NONNUMERIC_VALUE (label fragment or text cell) |
| p19/L932 | 2. Debt Equity ratio | R1258-R1259 | 2 | - |
| p19/L935 | 3. Debt service coverage ratio (no. of times | R1260-R1261 | 2 | - |
| p19/L938 | 4. Current Ratio (no. of times) | R1262-R1263 | 2 | NONNUMERIC_VALUE (label fragment or text cell) |
| p19/L940 | 5. Bad debts to Accounts receivables ratio ( | R1264-R1265 | 2 | - |
| p19/L943 | 6. Current Liability ratio (no. of times) To | R1266-R1267 | 2 | - |
| p19/L946 | 7. Total Debt to Total Assets Total Debt/ To | R1268-R1269 | 2 | - |
| p19/L949 | 8. Debtors turnover (no. of times)$ Income f | R1270-R1271 | 2 | - |
| p19/L952 | 9. Long term debt to working capital (Long t | R1272-R1273 | 2 | - |
| p19/L954 | 10. Net worth (₹ in crores) | R1274-R1275 | 2 | - |
| p19/L972 | 1. Staff cost optimisation (refer note a) | R1276-R1281 | 6 | - |
| p19/L974 | 2. Gain on sale of assets “held for sale” 3. | R1282-R1287 | 6 | ZERO_STANDING 3 of 6 cells (R1282-R1283,R1285) |
| p19/L977 | 4. Statutory Impact of new Labour Codes (ref | R1288-R1293 | 6 | ZERO_STANDING 3 of 6 cells (R1288,R1290,R1292) |
| p19/L979 | 5. Accidental damages (refer note d) | R1294-R1299 | 6 | ZERO_STANDING 4 of 6 cells (R1294,R1296,R1298-R1299) |
| p19/L981 | 6. Provision for contractual obligation (ref | R1300-R1305 | 6 | ZERO_STANDING 4 of 6 cells (R1300,R1302,R1304-R1305) |
| p19/L983 | Total | R1306-R1311 | 6 | - |

## 4. ZERO_STANDING register
Total ZERO_STANDING cells: 87. Lines carrying at least one zero cell: 36.
| page/line | label | zero cells | of cells | pattern |
|---|---|---|---|---|
| p3/L162 | 12 Loss on sale of subsidiary (refer note | R126-R129 | 6 | zero in some periods |
| p3/L163 | 13 Loss after tax from discontinued operatio | R132-R135 | 6 | zero in some periods |
| p4/L210 | (i) Basic (`) | R215-R218 | 6 | zero in some periods |
| p4/L211 | (ii) Diluted earnings per share (`) | R221-R224 | 6 | zero in some periods |
| p9/L408 | Discontinued Operations | R499 | 3 | zero in some periods |
| p9/L413 | Gain on disposal of assets held for sale (re | R511 | 3 | zero in some periods |
| p9/L417 | Accidental damages (refer note 2d)** | R524-R525 | 3 | zero in some periods |
| p9/L418 | Reclassification of FCTR to P&L on sale of s | R526 | 3 | zero in some periods |
| p10/L461 | Proceeds from disposal of asset held for sal | R593 | 3 | zero in some periods |
| p10/L463 | Acquisition of Subsidiary (net off acquired  | R599-R600 | 3 | zero in some periods |
| p10/L465 | Proceeds from sale of non-current investment | R605 | 3 | zero in some periods |
| p10/L481 | Proceeds from exercise of share options | R649-R650 | 3 | zero in some periods |
| p11/L517 | 2. Gain on sale of asset “held for sale” (Re | R673-R674,R676 | 6 | zero in some periods |
| p11/L520 | 3. Statutory impact of new Labour Codes (Ref | R679,R681,R683 | 6 | zero in some periods |
| p11/L522 | 4. Accidental damages (Refer note d) | R685,R687,R689-R690 | 6 | zero in some periods |
| p11/L524 | 5. Provision for contractual obligation (Ref | R691,R693,R695-R696 | 6 | zero in some periods |
| p12/L589 | Revenue from Operations | R718-R720 | 5 | zero in some periods |
| p12/L591 | Profit/(Loss) after tax from discontinued op | R723-R727 | 5 | zero in ALL periods (template signal) |
| p12/L593 | Loss on sale of subsidiary | R728-R730 | 5 | zero in some periods |
| p12/L595 | Total Profit/(Loss) after tax from discontin | R733-R735 | 5 | zero in some periods |
| p17/L819 | Accidental damages (refer note | R1087-R1088 | 3 | zero in some periods |
| p17/L821 | Gain on disposal of assets held for sale (re | R1092 | 3 | zero in some periods |
| p17/L823 | Dividend income | R1098 | 3 | zero in some periods |
| p17/L830 | Advances written off | R1120 | 2 | zero in some periods |
| p17/L849 | Proceeds from disposal of assets held for sa | R1160 | 3 | zero in some periods |
| p17/L851 | Proceeds from sale of non-current investment | R1166-R1167 | 2 | zero in ALL periods (template signal) |
| p17/L857 | Dividend income from subsidiaries | R1183 | 3 | zero in some periods |
| p17/L859 | Fixed deposits placed (net) | R1190 | 3 | zero in some periods |
| p17/L860 | Earmarked funds liquidated | R1192-R1193 | 3 | zero in some periods |
| p18/L877 | Proceeds from long-term borrowings (net off  | R1205 | 3 | zero in some periods |
| p18/L879 | Proceeds from sublease | R1211-R1212 | 2 | zero in ALL periods (template signal) |
| p18/L883 | Proceeds from exercise of share options | R1223-R1224 | 3 | zero in some periods |
| p19/L974 | 2. Gain on sale of assets “held for sale” 3. | R1282-R1283,R1285 | 6 | zero in some periods |
| p19/L977 | 4. Statutory Impact of new Labour Codes (ref | R1288,R1290,R1292 | 6 | zero in some periods |
| p19/L979 | 5. Accidental damages (refer note d) | R1294,R1296,R1298-R1299 | 6 | zero in some periods |
| p19/L981 | 6. Provision for contractual obligation (ref | R1300,R1302,R1304-R1305 | 6 | zero in some periods |
Zero cells outside the line-item groups: R1410.

## 5. AUDITOR PARAGRAPHS (limited review reports, pp21-27)
Going Concern language: none (grep count 0 in structured and in fulltext). Opinion type: limited review, unmodified conclusion (R1653).
| ROW_ID | paragraph | A2 flags |
|---|---|---|
| R1653 | Board letter: Limited Review Report, unmodified opinion | - |
| R1745 | Consolidated para 3: moderate assurance, not an audit | - |
| R1746 | Consolidated para 3: no audit opinion expressed | - |
| R1747 | Consolidated para 6: emphasis, note 3 DOT demand notices, contingent liability Rs 7,513.71cr | EMPHASIS_OF_MATTER |
| R1748 | Consolidated para 7: emphasis, note 4 tax litigation uncertainty in one subsidiary | EMPHASIS_OF_MATTER |
| R1749 | Consolidated: conclusion not modified for paras 6 and 7 | - |
| R1750 | Consolidated para 8: one subsidiary reviewed by other auditor, sole reliance | OTHER_AUDITOR_RELIANCE |
| R1751 | Consolidated para 9: two subsidiaries and three associates not reviewed by their auditors, management-furnished | MGMT_FURNISHED_UNREVIEWED |
| R1752 | Consolidated: conclusion not modified for paras 8 and 9 | - |
| R1764 | Standalone para 3: moderate assurance, not an audit | - |
| R1765 | Standalone para 5: emphasis, note 3 DOT demand notices, conclusion not modified | EMPHASIS_OF_MATTER |
Auditor numbers (address, standard, emphasis refs, other-auditor and unreviewed-entity financials):
| ROW IDs | group | cells |
|---|---|---|
| R1326-R1331 | auditor address, LODR reg, SRE standard | 6 |
| R1332-R1334 | emphasis paragraph references (DoT years, contingent liability, subsidiary tax) | 3 |
| R1335-R1342 | one subsidiary reviewed by other auditor (financials) | 8 |
| R1343-R1351 | two subsidiaries not reviewed by their auditors (count and financials) | 9 |
| R1352-R1356 | three associates not reviewed (count and group share) | 5 |
| R1360-R1361 | standalone emphasis paragraph references | 2 |

## 6. ENTITIES
### 6a Consolidation list (auditor annexure, pp24-25): 72 subsidiaries + 3 associates = 75
| ROW_ID | seq | A2 flags | note |
|---|---|---|---|
| R1448 | subsidiary no. 1 | - | - |
| R1449 | subsidiary no. 2 | - | - |
| R1450 | subsidiary no. 3 | - | - |
| R1451 | subsidiary no. 4 | - | - |
| R1452 | subsidiary no. 5 | - | - |
| R1453 | subsidiary no. 6 | - | - |
| R1454 | subsidiary no. 7 | - | - |
| R1455 | subsidiary no. 8 | - | - |
| R1456 | subsidiary no. 9 | - | - |
| R1457 | subsidiary no. 10 | - | - |
| R1458 | subsidiary no. 11 | - | - |
| R1459 | subsidiary no. 12 | - | - |
| R1460 | subsidiary no. 13 | - | - |
| R1461 | subsidiary no. 14 | - | - |
| R1462 | subsidiary no. 15 | - | - |
| R1463 | subsidiary no. 16 | - | - |
| R1464 | subsidiary no. 17 | - | TCNL, transferee in Attachment D (R1426) |
| R1465 | subsidiary no. 18 | - | - |
| R1466 | subsidiary no. 19 | - | - |
| R1467 | subsidiary no. 20 | - | - |
| R1468 | subsidiary no. 21 | - | - |
| R1469 | subsidiary no. 22 | - | - |
| R1470 | subsidiary no. 23 | - | - |
| R1471 | subsidiary no. 24 | - | - |
| R1472 | subsidiary no. 25 | - | - |
| R1473 | subsidiary no. 26 | - | - |
| R1474 | subsidiary no. 27 | - | - |
| R1475 | subsidiary no. 28 | - | - |
| R1476 | subsidiary no. 29 | - | - |
| R1477 | subsidiary no. 30 | - | - |
| R1478 | subsidiary no. 31 | - | - |
| R1479 | subsidiary no. 32 | - | - |
| R1480 | subsidiary no. 33 | - | - |
| R1481 | subsidiary no. 34 | - | - |
| R1482 | subsidiary no. 35 | ENTITY_CHANGE | wef 18-Apr-2025 (R1630,R1753) |
| R1483 | subsidiary no. 36 | - | - |
| R1484 | subsidiary no. 37 | - | - |
| R1485 | subsidiary no. 38 | - | - |
| R1486 | subsidiary no. 39 | - | - |
| R1487 | subsidiary no. 40 | - | - |
| R1488 | subsidiary no. 41 | - | - |
| R1489 | subsidiary no. 42 | - | - |
| R1490 | subsidiary no. 43 | - | - |
| R1491 | subsidiary no. 44 | - | - |
| R1492 | subsidiary no. 45 | - | - |
| R1493 | subsidiary no. 46 | - | - |
| R1494 | subsidiary no. 47 | - | - |
| R1495 | subsidiary no. 48 | ENTITY_CHANGE | upto 15-Sep-2025 (R1631,R1754) |
| R1496 | subsidiary no. 49 | ENTITY_CHANGE | upto 22-Apr-2025 (R1632,R1755) |
| R1497 | subsidiary no. 50 | - | - |
| R1498 | subsidiary no. 51 | - | - |
| R1499 | subsidiary no. 52 | - | - |
| R1500 | subsidiary no. 53 | - | - |
| R1501 | subsidiary no. 54 | - | - |
| R1502 | subsidiary no. 55 | - | Kaleyra Inc: subject of Attachment D transfer to TCNL (R1425) |
| R1503 | subsidiary no. 56 | - | - |
| R1504 | subsidiary no. 57 | - | - |
| R1505 | subsidiary no. 58 | - | - |
| R1506 | subsidiary no. 59 | - | - |
| R1507 | subsidiary no. 60 | - | - |
| R1508 | subsidiary no. 61 | ENTITY_CHANGE | upto 14-Jan-2026 (R1633,R1756) |
| R1509 | subsidiary no. 62 | ENTITY_CHANGE | upto 04-Sep-2026, IN CURRENT PERIOD (R1634,R1757) |
| R1510 | subsidiary no. 63 | - | - |
| R1511 | subsidiary no. 64 | - | - |
| R1512 | subsidiary no. 65 | - | - |
| R1513 | subsidiary no. 66 | - | - |
| R1514 | subsidiary no. 67 | ENTITY_CHANGE | upto 01-Oct-2025 (R1635,R1758) |
| R1515 | subsidiary no. 68 | - | - |
| R1516 | subsidiary no. 69 | ENTITY_CHANGE | wef 01-Dec-2025 (R1636,R1759) |
| R1517 | subsidiary no. 70 | ENTITY_CHANGE | wef 01-Dec-2025 (R1637,R1760) |
| R1518 | subsidiary no. 71 | ENTITY_CHANGE | wef 12-Mar-2026 (R1638,R1761) |
| R1519 | subsidiary no. 72 | ENTITY_CHANGE | wef 21-May-2026, IN CURRENT PERIOD (R1639,R1762) |
| R1520 | associate no. 1 | - | - |
| R1521 | associate no. 2 | - | - |
| R1522 | associate no. 3 | - | - |
ENTITY_CHANGE: 10 rows (inclusions R1482,R1516,R1517,R1518,R1519; exclusions R1495,R1496,R1508,R1509,R1514). Two fall in the current half-year: R1509 (excluded) and R1519 (added). Prior list not available; no diff.
Entity qualifier rows (wef/upto brackets): R1753-R1762 - flag ENTITY_CHANGE, paired to entities above and dates R1630-R1639.
### 6b Other entities named (regulators, exchanges, counterparties, partners, signatories)
| ROW_ID | A2 flags | note |
|---|---|---|
| R1418 | - | - |
| R1419 | - | - |
| R1420 | - | - |
| R1421 | - | - |
| R1422 | - | - |
| R1423 | - | - |
| R1424 | - | statutory auditor |
| R1425 | - | Attachment D party |
| R1426 | - | Attachment D party |
| R1427 | - | - |
| R1428 | - | - |
| R1429 | - | named individual (signatory, appointee or partner) |
| R1430 | - | named individual (signatory, appointee or partner) |
| R1431 | - | - |
| R1432 | - | - |
| R1433 | NAME_NOT_DISCLOSED | - |
| R1434 | - | - |
| R1435 | - | - |
| R1436 | - | - |
| R1437 | - | - |
| R1438 | - | - |
| R1439 | NAME_NOT_DISCLOSED | - |
| R1440 | - | - |
| R1441 | - | - |
| R1442 | NAME_NOT_DISCLOSED | - |
| R1443 | - | - |
| R1444 | - | named individual (signatory, appointee or partner) |
| R1445 | - | - |
| R1446 | - | statutory auditor |
| R1447 | - | named individual (signatory, appointee or partner) |
| R1523 | - | - |
| R1524 | - | - |
| R1525 | - | - |
| R1526 | - | - |
| R1527 | - | - |
| R1528 | - | - |
| R1529 | - | - |
| R1530 | - | - |
| R1531 | - | - |
| R1532 | - | - |
| R1533 | - | - |
| R1534 | - | - |
| R1535 | - | - |
| R1536 | - | - |
| R1537 | - | - |
| R1538 | - | - |
| R1539 | - | - |
| R1540 | - | - |
| R1541 | - | - |
| R1542 | - | - |
| R1543 | - | - |
| R1544 | - | - |
| R1545 | - | - |
| R1546 | - | - |
| R1547 | - | - |
| R1548 | - | - |
| R1549 | - | - |

## 7. SIGNATURE BLOCKS, NOTE NUMBERS, ADMIN
### 7a Signatures (rule 7)
| signatory | ROW IDs | timestamp | A2 flags | note |
|---|---|---|---|---|
| Company Secretary Zubin Adil Patel (board outcome letter) | R015,R1430,R1586 | 15-Oct-2026 13:52:19 IST | - | signed after meeting concluded 13:45 (R007) |
| MD and CEO Ganapathi S. Lakshminarayanan (results, both sets) | R1323,R1324,R1444,R1622,R1623 | 15-Oct-2026 12:58:01 IST | SIGNATURE_BEFORE_MEETING_END | stamp is 47 min before the 13:45 conclusion; approval time inside the meeting is not stated |
| Auditor S.R. Batliboi & Associates, partner Sanjay Bachchani, consolidated report | R1628,R1629,R1446,R1447,R1357,R1358,R1359 | 15-Oct-2026 13:05:38 IST | SIGNATURE_BEFORE_MEETING_END | UDIN R1359; stamp 40 min before conclusion |
| Auditor, standalone report | R1641,R1642,R1362,R1363,R1364 | 15-Oct-2026 13:04:44 IST | SIGNATURE_BEFORE_MEETING_END | UDIN R1364; stamp 41 min before conclusion |
Signature-class number IDs: R015,R1323-R1324,R1357-R1359,R1362-R1364 (R1628,R1629,R1641,R1642,R1622,R1623,R1586 are DATE rows in section 9).
### 7b Numbers embedded in notes text
| ROW IDs | group |
|---|---|
| R703-R709 | page 11 note-text numbers (7) |
| R711-R717,R738-R740 | page 12 note-text numbers (10) |
| R1313-R1322 | page 20 note-text numbers (10) |
### 7c Admin (letter metadata, page footers)
| ROW IDs | group |
|---|---|
| R001-R005,R008-R013,R016-R018 | letter metadata (reference, addresses, pincodes, scrip code, regs, circular, CIN, phone) (14) |
| R156,R239,R336,R401,R452,R495,R583,R666,R710,R741,R868,R983,R1034,R1073,R1198,R1255,R1312,R1325 | page footer pagination (18) |
### 7d Board-letter numbers placed under agenda
| ROW IDs | group |
|---|---|
| R006-R007,R014 | meeting times and CS membership number (also in section 1) |

## 8. PRESS RELEASE (Attachment C) AND ATTACHMENTS D, E
| ROW IDs | group | cells | A2 flags |
|---|---|---|---|
| R1365-R1371 | press release headline claims (growth, margins, digital losses) | 7 | FOOTNOTE_UNRESOLVED (see 2c: R1766-R1768) |
| R1372-R1392 | press release Table 1 (7 lines x 3 cells) | 21 | RESTATED vs headline claims R1365-R1371; PAT after minority interest (R1771) |
| R1393 | press release DC-to-DC opportunity figure | 1 | - |
| R1394-R1401 | press release awards, contacts, company profile counts | 8 | - |
| R1402-R1410 | Attachment D Kaleyra transfer figures | 9 | - |
| R1411-R1417 | Attachment E CS appointment details | 7 | - |
Press release revenue and EBITDA are not defined against filed lines (R1766-R1768); reconcile in A3.

## 9. DATES
| ROW IDs | group | count | A2 flags |
|---|---|---|---|
| R1582-R1585,R1643-R1645,R1650-R1652 | A letter, press release and circular dates | 10 | - |
| R1587-R1593,R1612-R1614,R1624,R1640,R1646,R1648-R1649 | B reporting-period and column dates | 15 | - |
| R1586,R1622-R1623,R1628-R1629,R1641-R1642 | C signature, board approval and report dates | 7 | - |
| R1594,R1615 | C2 board approval dates (notes 1) | 2 | - |
| R1595-R1603,R1616-R1621,R1625-R1627 | D notes: exceptional items, Labour Codes, DoT/AGR timeline, subsidiary cash-flow periods | 18 | - |
| R1604-R1611 | E notes: VAT litigation timeline and discontinued ops dates | 8 | - |
| R1630-R1639 | F consolidation-list effective and cut-off dates (ENTITY_CHANGE) | 10 | ENTITY_CHANGE (cross-ref 6a) |
| R1647 | G award year labels | 1 | - |

## 10. FORWARD-LOOKING STATEMENTS
| ROW IDs | group | count |
|---|---|---|
| R1550-R1552,R1574-R1579 | Kaleyra transfer to TCNL (letter and Attachment D) | 9 |
| R1553-R1554,R1580-R1581 | CS appointment (letter and Attachment E) | 4 |
| R1555-R1561 | notes: reorganisation, DoT defence, VAT appeal outcome | 7 |
| R1562-R1566 | CEO quotes (H2 FY27 momentum, DC-to-DC, AI stack) | 5 |
| R1567-R1570 | press release news items and Mint interview | 4 |
| R1571-R1573 | data pack and disclaimer forward-looking language | 3 |
VAT appeal: National Court judgment was scheduled for 13-Oct-2026, two days before the board meeting; outcome not stated (R1558, R1608). Flag OUTCOME_NOT_DISCLOSED.

## 11. MISSING_FROM_STRUCTURED
None. Fulltext sweep of every decimal token on pp2, 11, 12, 18-20, 22-23, 27-28, 32 found each present in the structured file. Financial-table decimals on pp3-10, 13-17 match one-for-one.