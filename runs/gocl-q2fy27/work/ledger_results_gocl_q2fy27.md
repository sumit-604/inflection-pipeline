# A2 LEDGER: GOCL Q2 FY27 results (Board Outcome + results + merger update)

=== A2 COUNT TEST ===
ids_in_structured: 2233 | ids_referenced_in_ledger: 2233 | orphan_ids: [] | match: yes
category: notes (numbered C1-8 + S1-8)        grep_count: 16 (19 'QUALIFIER | Note N:' rows over 16 distinct numbers)   sweep_count: 16   match: yes
category: footnote/unnumbered qualifiers       grep_count: 32 (68 QUALIFIER - 26 note-block rows - 10 auditor rows)   sweep_count: 32   match: yes
category: image NUMBER cells                    grep_count: 796 (A1 header; rows R1438-R2233)   sweep_count: 796   match: yes
category: line_items (distinct table+line)     grep_count: 231 (distinct description minus period)   sweep_count: 231   match: yes
category: zero_standing image cells            grep_count: 31 (grep -c ZERO_STANDING in image section)   sweep_count: 31   match: yes
category: zero_standing line items             sweep_count: 21
category: zero_standing text-layer rows (non-superseded, A1-flagged)   sweep_count: 1
category: superseded old OCR rows              grep_count: 949 (grep -c SUPERSEDED_BY = 950 incl. header line 5; 253+171+53+81+226+82+83)   sweep_count: 949   match: yes
category: agenda_items                         grep_count: 4 (2 lettered + 2 Board paragraphs)   sweep_count: 4   match: yes
category: auditor_paras                        grep_count: 12 (7 consolidated + 5 standalone numbered)   sweep_count: 12   match: yes
category: entities                             grep_count: 26   sweep_count: 26   match: yes
category: forward                              grep_count: 20   sweep_count: 20   match: yes
gate_a2: pass
=== END COUNT TEST ===


Every row cites A1 structured ROW IDs (line anchor lives in that row). Verbatim values stay at the ID. Unit Rs. Lakhs (x0.01 for crore). No prior-quarter ledger supplied, so ENTITY_CHANGE and DROPPED checks were not run (stated, not flagged). No MISSING_FROM_STRUCTURED rows raised.


## 1. NOTES (numbered notes, consolidated C1-C8 then standalone S1-S8)

| ROW_ID(s) | category | A2 flags | cross-ref / materiality |
|---|---|---|---|
| R1398 | note C1 | - | - |
| R1399-R1401 | note C2 | - | put option as derivative; exceptional item; OCI loss |
| R1402-R1406 | note C3 | - | land MoU, JDA 32 acres; gains split continuing/discontinued; discontinued table R1404-R1406 |
| R1407 | note C4 | PRINTED_DIFF | EoM source; guarantees HNPCL 109,640 + HEIL 22,000 lakhs here vs HNPCL 109,610 in standalone R1430: PRINTED_DIFF |
| R1408-R1409 | note C5 | RESTATED | merger scheme; RESTATED R1431 |
| R1410 | note C6 | - | - |
| R1411-R1412 | note C7 | RESTATED | Ecopolis sale; RESTATED R1432 |
| R1413 | note C8 | RESTATED | dividend Rs.30/sh; RESTATED R1436 |
| R1427 | note S1 | - | - |
| R1428 | note S2 | - | segment info only in consolidated (Ind AS 108) |
| R1429 | note S3 | - | - |
| R1430 | note S4 | PRINTED_DIFF | printed 109,610 vs consolidated 109,640 R1407: PRINTED_DIFF |
| R1431 | note S5 | RESTATED | RESTATED R1408 |
| R1432 | note S6 | RESTATED | RESTATED R1411 |
| R1433-R1435 | note S7 | RESTATED | RESTATED R1402 |
| R1436 | note S8 | RESTATED | RESTATED R1413 |

## 1b. UNNUMBERED NOTES / FOOTNOTES / REFER-MARKERS

| ROW_ID(s) | category | A2 flags | cross-ref / materiality |
|---|---|---|---|
| R1378-R1384 | footnote consol P&L (units, columns, Refer-note markers, EPS) | - | page 4; markers refer to C2,C3,C4, all resolved |
| R1385-R1390 | footnote segment (# discontinued marker, units) | - | page 5; # resolves to Energetics Division and IDL Explosives R1233,R1234 |
| R1391-R1395 | footnote balance sheet (units, refer Notes 3,7,8) | - | page 6 |
| R1396 | footnote cash flow (unaudited) | - | page 7 |
| R1397 | notes heading consolidated | - | - |
| R1417-R1421 | footnote standalone P&L | - | page 12 |
| R1422-R1424 | footnote standalone balance sheet | - | page 13 |
| R1425 | footnote standalone cash flow | - | page 14 |
| R1426 | notes heading standalone | - | - |
| R1414, R1437 | statement: results on exchange and company websites | - | - |

## 2. FINANCIAL TABLE LINE ITEMS (grouped image-transcription IDs; ZERO_STANDING where any cell is nil/dash)

| line # | ROW_ID(s) | table / line item | cells | A2 flags | note |
|---|---|---|---|---|---|
| 1 | R1438-R1443 | Consolidated P&L, Revenue from operations | 6 (p4) | - | - |
| 2 | R1444-R1449 | Consolidated P&L, Other income | 6 (p4) | - | - |
| 3 | R1450-R1455 | Consolidated P&L, Total Income | 6 (p4) | - | - |
| 4 | R1456-R1461 | Consolidated P&L, Cost of materials consumed | 6 (p4) | - | - |
| 5 | R1462-R1467 | Consolidated P&L, Changes in inventories of FG, WIP and stock-in-trade | 6 (p4) | - | - |
| 6 | R1468-R1473 | Consolidated P&L, Employee benefits expense | 6 (p4) | - | - |
| 7 | R1474-R1479 | Consolidated P&L, Finance cost | 6 (p4) | - | - |
| 8 | R1480-R1485 | Consolidated P&L, Depreciation and amortisation expense | 6 (p4) | - | - |
| 9 | R1486-R1491 | Consolidated P&L, Other expense | 6 (p4) | - | - |
| 10 | R1492-R1497 | Consolidated P&L, Total expenses | 6 (p4) | - | - |
| 11 | R1498-R1503 | Consolidated P&L, Profit before exceptional items and tax (1-2) | 6 (p4) | - | - |
| 12 | R1504-R1509 | Consolidated P&L, Exceptional items (net) | 6 (p4) | - | - |
| 13 | R1510-R1515 | Consolidated P&L, Profit before tax (3+4) | 6 (p4) | - | - |
| 14 | R1516-R1521 | Consolidated P&L, Current tax | 6 (p4) | - | - |
| 15 | R1522-R1527 | Consolidated P&L, Deferred tax (Credit)/Expense | 6 (p4) | - | - |
| 16 | R1528-R1533 | Consolidated P&L, Total tax expense | 6 (p4) | - | - |
| 17 | R1534-R1539 | Consolidated P&L, Profit from continuing operations (5-6) | 6 (p4) | - | - |
| 18 | R1540-R1545 | Consolidated P&L, (Loss)/Profit before tax from discontinued operations | 6 (p4) | - | - |
| 19 | R1546-R1551 | Consolidated P&L, Tax expense of discontinued operations/(Credit) | 6 (p4) | - | - |
| 20 | R1552-R1557 | Consolidated P&L, (Loss)/Profit after tax from discontinued operations | 6 (p4) | - | - |
| 21 | R1558-R1563 | Consolidated P&L, Net profit after tax (7+9) | 6 (p4) | - | - |
| 22 | R1564-R1569 | Consolidated P&L, OCI: Remeasurement (loss) on defined benefit plans | 6 (p4) | - | - |
| 23 | R1570-R1575 | Consolidated P&L, OCI: Income tax on remeasurement | 6 (p4) | - | - |
| 24 | R1576-R1581 | Consolidated P&L, OCI: Net changes in FV of equity instruments through OCI (Re | 6 (p4) | ZERO_STANDING | nil/dash cells R1577-R1578, R1580-R1581 |
| 25 | R1582-R1587 | Consolidated P&L, OCI: Exchange differences on translation of foreign operatio | 6 (p4) | - | - |
| 26 | R1588-R1593 | Consolidated P&L, Other comprehensive income, net of tax | 6 (p4) | - | - |
| 27 | R1594-R1599 | Consolidated P&L, Total comprehensive income (10+11) | 6 (p4) | - | - |
| 28 | R1600-R1605 | Consolidated P&L, Paid up equity share capital (Face value Rs. 2 each) | 6 (p4) | - | - |
| 29 | R1606 | Consolidated P&L, Reserves i.e. other equity | 1 (p4) | - | - |
| 30 | R1607-R1612 | Consolidated P&L, EPS continuing operations, Basic and Diluted (Rs.) | 6 (p4) | - | - |
| 31 | R1613-R1618 | Consolidated P&L, EPS discontinued operations, Basic and Diluted (Rs.) | 6 (p4) | - | - |
| 32 | R1619-R1624 | Consolidated P&L, EPS continuing and discontinued, Basic and Diluted (Rs.) | 6 (p4) | - | - |
| 33 | R1625-R1630 | Segment, Segment income: Electronics Manufacturing Services | 6 (p5) | - | - |
| 34 | R1631-R1636 | Segment, Segment income: Realty | 6 (p5) | - | - |
| 35 | R1637-R1642 | Segment, Segment income: Unallocable income | 6 (p5) | - | - |
| 36 | R1643-R1648 | Segment, Segment income: Total | 6 (p5) | - | - |
| 37 | R1649-R1654 | Segment, Less: Inter segment revenue | 6 (p5) | ZERO_STANDING | nil/dash cells R1649-R1654 (all cells) |
| 38 | R1655-R1660 | Segment, Total Segment Revenue | 6 (p5) | - | - |
| 39 | R1661-R1666 | Segment, Discontinued Operations # (income) | 6 (p5) | - | - |
| 40 | R1667-R1672 | Segment, Total income | 6 (p5) | - | - |
| 41 | R1673-R1678 | Segment, Segment results: Electronics Manufacturing Services | 6 (p5) | - | - |
| 42 | R1679-R1684 | Segment, Segment results: Realty | 6 (p5) | - | - |
| 43 | R1685-R1690 | Segment, Segment results: Total | 6 (p5) | - | - |
| 44 | R1691-R1696 | Segment, Less: Finance costs | 6 (p5) | - | - |
| 45 | R1697-R1702 | Segment, Less: Other Unallocable expenditure net off (un-allocable in | 6 (p5) | - | - |
| 46 | R1703-R1708 | Segment, Profit before tax (continuing, subtotal) | 6 (p5) | - | - |
| 47 | R1709-R1714 | Segment, Discontinued Operations # (profit before tax) | 6 (p5) | - | - |
| 48 | R1715-R1720 | Segment, Total profit before tax | 6 (p5) | - | - |
| 49 | R1721-R1726 | Segment, Segment assets: Electronics Manufacturing Services | 6 (p5) | - | - |
| 50 | R1727-R1732 | Segment, Segment assets: Realty | 6 (p5) | - | - |
| 51 | R1733-R1738 | Segment, Segment assets: Unallocable assets | 6 (p5) | - | - |
| 52 | R1739-R1744 | Segment, Segment assets: Discontinued Operations # | 6 (p5) | - | - |
| 53 | R1745-R1750 | Segment, Total Assets | 6 (p5) | - | - |
| 54 | R1751-R1756 | Segment, Segment liabilities: Electronics Manufacturing Services | 6 (p5) | - | - |
| 55 | R1757-R1762 | Segment, Segment liabilities: Realty | 6 (p5) | - | - |
| 56 | R1763-R1768 | Segment, Segment liabilities: Unallocable liabilities | 6 (p5) | - | - |
| 57 | R1769-R1774 | Segment, Segment liabilities: Discontinued Operations # | 6 (p5) | - | - |
| 58 | R1775-R1780 | Segment, Total Liabilities | 6 (p5) | - | - |
| 59 | R1781-R1782 | Consolidated Balance Sheet, Property, plant and equipment | 2 (p6) | - | - |
| 60 | R1783-R1784 | Consolidated Balance Sheet, Capital work-in-progress | 2 (p6) | ZERO_STANDING | nil/dash cells R1783 |
| 61 | R1785-R1786 | Consolidated Balance Sheet, Investment property | 2 (p6) | - | - |
| 62 | R1787-R1788 | Consolidated Balance Sheet, Intangible assets | 2 (p6) | - | - |
| 63 | R1789-R1790 | Consolidated Balance Sheet, Non-current financial assets (a) Investments | 2 (p6) | - | - |
| 64 | R1791-R1792 | Consolidated Balance Sheet, Non-current financial assets (b) Other financial assets | 2 (p6) | - | - |
| 65 | R1793-R1794 | Consolidated Balance Sheet, Other non-current assets | 2 (p6) | - | - |
| 66 | R1795-R1796 | Consolidated Balance Sheet, Total Non-current assets | 2 (p6) | - | - |
| 67 | R1797-R1798 | Consolidated Balance Sheet, Inventories | 2 (p6) | - | - |
| 68 | R1799-R1800 | Consolidated Balance Sheet, Current financial assets (a) Investments | 2 (p6) | - | - |
| 69 | R1801-R1802 | Consolidated Balance Sheet, Current financial assets (b) Derivative asset | 2 (p6) | - | - |
| 70 | R1803-R1804 | Consolidated Balance Sheet, Current financial assets (c) Trade receivables | 2 (p6) | - | - |
| 71 | R1805-R1806 | Consolidated Balance Sheet, Current financial assets (d) Cash and cash equivalents | 2 (p6) | - | - |
| 72 | R1807-R1808 | Consolidated Balance Sheet, Current financial assets (e) Bank balances other than (d) | 2 (p6) | - | - |
| 73 | R1809-R1810 | Consolidated Balance Sheet, Current financial assets (f) Loans | 2 (p6) | - | - |
| 74 | R1811-R1812 | Consolidated Balance Sheet, Current financial assets (g) Other financial assets | 2 (p6) | - | - |
| 75 | R1813-R1814 | Consolidated Balance Sheet, Other current assets | 2 (p6) | - | - |
| 76 | R1815-R1816 | Consolidated Balance Sheet, Total current assets | 2 (p6) | - | - |
| 77 | R1817-R1818 | Consolidated Balance Sheet, Non current Assets held for sale (Refer Note 3 and 7) | 2 (p6) | - | - |
| 78 | R1819-R1820 | Consolidated Balance Sheet, TOTAL ASSETS | 2 (p6) | - | - |
| 79 | R1821-R1822 | Consolidated Balance Sheet, Equity share capital | 2 (p6) | - | - |
| 80 | R1823-R1824 | Consolidated Balance Sheet, Other equity | 2 (p6) | - | - |
| 81 | R1825-R1826 | Consolidated Balance Sheet, Total equity | 2 (p6) | - | - |
| 82 | R1827-R1828 | Consolidated Balance Sheet, Non-current liabilities: Provisions | 2 (p6) | - | - |
| 83 | R1829-R1830 | Consolidated Balance Sheet, Non-current liabilities: Deferred tax liabilities (net) | 2 (p6) | - | - |
| 84 | R1831-R1832 | Consolidated Balance Sheet, Total non-current liabilities | 2 (p6) | - | - |
| 85 | R1833-R1834 | Consolidated Balance Sheet, Current financial liabilities (a) Borrowings | 2 (p6) | ZERO_STANDING | nil/dash cells R1833 |
| 86 | R1835-R1836 | Consolidated Balance Sheet, Trade payables: micro enterprises and small enterprises | 2 (p6) | ZERO_STANDING | nil/dash cells R1835-R1836 (all cells) |
| 87 | R1837-R1838 | Consolidated Balance Sheet, Trade payables: creditors other than micro and small enterpr | 2 (p6) | - | - |
| 88 | R1839-R1840 | Consolidated Balance Sheet, Current financial liabilities (c) Other financial liabilitie | 2 (p6) | - | - |
| 89 | R1841-R1842 | Consolidated Balance Sheet, Other current liabilities | 2 (p6) | - | - |
| 90 | R1843-R1844 | Consolidated Balance Sheet, Current provisions | 2 (p6) | - | - |
| 91 | R1845-R1846 | Consolidated Balance Sheet, Income tax liabilities | 2 (p6) | - | - |
| 92 | R1847-R1848 | Consolidated Balance Sheet, Total current liabilities | 2 (p6) | - | - |
| 93 | R1849-R1850 | Consolidated Balance Sheet, Liabilities associated with Non current assets held for sale | 2 (p6) | - | - |
| 94 | R1851-R1852 | Consolidated Balance Sheet, TOTAL LIABILITIES | 2 (p6) | - | - |
| 95 | R1853-R1854 | Consolidated Balance Sheet, TOTAL EQUITY AND LIABILITIES | 2 (p6) | - | - |
| 96 | R1855-R1856 | Consolidated Cash Flow, Profit before Tax from continuing operations | 2 (p7) | - | - |
| 97 | R1857-R1858 | Consolidated Cash Flow, Profit before Tax from discontinued operations | 2 (p7) | - | - |
| 98 | R1859-R1860 | Consolidated Cash Flow, Profit before Tax | 2 (p7) | - | - |
| 99 | R1861-R1862 | Consolidated Cash Flow, Depreciation and amortisation expense | 2 (p7) | - | - |
| 100 | R1863-R1864 | Consolidated Cash Flow, Profit on sale of property, plant and equipment (net) | 2 (p7) | ZERO_STANDING | nil/dash cells R1863 |
| 101 | R1865-R1866 | Consolidated Cash Flow, Gain on fair valuation measurement of other investments | 2 (p7) | ZERO_STANDING | nil/dash cells R1866 |
| 102 | R1867-R1868 | Consolidated Cash Flow, Fair valuation gain on derivative asset | 2 (p7) | - | - |
| 103 | R1869-R1870 | Consolidated Cash Flow, Liabilities / provisions no longer required written back | 2 (p7) | - | - |
| 104 | R1871-R1872 | Consolidated Cash Flow, (Reversal) / Provision for doubtful debts, trade receivables | 2 (p7) | - | - |
| 105 | R1873-R1874 | Consolidated Cash Flow, Interest income | 2 (p7) | - | - |
| 106 | R1875-R1876 | Consolidated Cash Flow, Unrealised loss on foreign exchange fluctuation (net) | 2 (p7) | - | - |
| 107 | R1877-R1878 | Consolidated Cash Flow, Finance cost | 2 (p7) | - | - |
| 108 | R1879-R1880 | Consolidated Cash Flow, Operating profit/(Loss) before working capital changes | 2 (p7) | - | - |
| 109 | R1881-R1882 | Consolidated Cash Flow, (Increase)/decrease in trade receivables and financial/other | 2 (p7) | - | - |
| 110 | R1883-R1884 | Consolidated Cash Flow, Increase in inventories | 2 (p7) | - | - |
| 111 | R1885-R1886 | Consolidated Cash Flow, Increase/(decrease) in trade payables, financial/other liabi | 2 (p7) | - | - |
| 112 | R1887-R1888 | Consolidated Cash Flow, Net cash generated from operations | 2 (p7) | - | - |
| 113 | R1889-R1890 | Consolidated Cash Flow, Income taxes paid (net of refunds) | 2 (p7) | - | - |
| 114 | R1891-R1892 | Consolidated Cash Flow, NET CASH FROM/(USED IN) OPERATING ACTIVITIES (A) | 2 (p7) | - | - |
| 115 | R1893-R1894 | Consolidated Cash Flow, Acquisition of property, plant and equipment | 2 (p7) | - | - |
| 116 | R1895-R1896 | Consolidated Cash Flow, Proceeds from sale of property, plant and equipment | 2 (p7) | ZERO_STANDING | nil/dash cells R1895 |
| 117 | R1897-R1898 | Consolidated Cash Flow, Proceeds from sale of investment in subsidiary (net of expen | 2 (p7) | ZERO_STANDING | nil/dash cells R1897 |
| 118 | R1899-R1900 | Consolidated Cash Flow, Advance received against sale of land (net of expenses) | 2 (p7) | ZERO_STANDING | nil/dash cells R1900 |
| 119 | R1901-R1902 | Consolidated Cash Flow, Investments in bank deposits | 2 (p7) | - | - |
| 120 | R1903-R1904 | Consolidated Cash Flow, Redemption of bank deposits | 2 (p7) | - | - |
| 121 | R1905-R1906 | Consolidated Cash Flow, Loan to Companies: Given | 2 (p7) | - | - |
| 122 | R1907-R1908 | Consolidated Cash Flow, Loan to Companies: Realised | 2 (p7) | - | - |
| 123 | R1909-R1910 | Consolidated Cash Flow, Interest received | 2 (p7) | - | - |
| 124 | R1911-R1912 | Consolidated Cash Flow, NET CASH GENERATED FROM INVESTING ACTIVITIES (B) | 2 (p7) | FOOTING_GAP | FOOTING_GAP at R1912: printed 98,092.33 vs computed 98,090.33 |
| 125 | R1913-R1914 | Consolidated Cash Flow, Repayment of long-term borrowings | 2 (p7) | ZERO_STANDING | nil/dash cells R1913 |
| 126 | R1915-R1916 | Consolidated Cash Flow, Proceeds of short-term borrowings (net) | 2 (p7) | ZERO_STANDING | nil/dash cells R1915 |
| 127 | R1917-R1918 | Consolidated Cash Flow, Finance cost paid | 2 (p7) | - | - |
| 128 | R1919-R1920 | Consolidated Cash Flow, Dividends paid | 2 (p7) | ZERO_STANDING | nil/dash cells R1919 |
| 129 | R1921-R1922 | Consolidated Cash Flow, NET CASH USED IN FINANCING ACTIVITIES (C) | 2 (p7) | - | - |
| 130 | R1923-R1924 | Consolidated Cash Flow, NET INCREASE/(DECREASE) IN CASH AND CASH EQUIVALENTS (A+B+C) | 2 (p7) | FOOTING_GAP | FOOTING_GAP at R1924: printed (609.73) vs computed (599.73) |
| 131 | R1925-R1926 | Consolidated Cash Flow, Cash and cash equivalents as at beginning of the year | 2 (p7) | - | - |
| 132 | R1927-R1928 | Consolidated Cash Flow, Cash and cash equivalents as at the end of the year | 2 (p7) | - | - |
| 133 | R1929-R1934 | Standalone P&L, Revenue from operations | 6 (p12) | - | - |
| 134 | R1935-R1940 | Standalone P&L, Other income (Refer note 4 and 7) | 6 (p12) | - | - |
| 135 | R1941-R1946 | Standalone P&L, Total income | 6 (p12) | - | - |
| 136 | R1947-R1952 | Standalone P&L, Cost of materials consumed | 6 (p12) | - | - |
| 137 | R1953-R1958 | Standalone P&L, Changes in inventories of FG, WIP and stock-in-trade | 6 (p12) | - | - |
| 138 | R1959-R1964 | Standalone P&L, Employee benefits expense | 6 (p12) | - | - |
| 139 | R1965-R1970 | Standalone P&L, Finance cost | 6 (p12) | - | - |
| 140 | R1971-R1976 | Standalone P&L, Depreciation and amortisation expense | 6 (p12) | - | - |
| 141 | R1977-R1982 | Standalone P&L, Other expense | 6 (p12) | - | - |
| 142 | R1983-R1988 | Standalone P&L, Total expenses | 6 (p12) | - | - |
| 143 | R1989-R1994 | Standalone P&L, Profit before tax (1-2) | 6 (p12) | - | - |
| 144 | R1995-R2000 | Standalone P&L, Current tax | 6 (p12) | - | - |
| 145 | R2001-R2006 | Standalone P&L, Deferred tax Expense/(Credit) | 6 (p12) | - | - |
| 146 | R2007-R2012 | Standalone P&L, Total tax expense | 6 (p12) | - | - |
| 147 | R2013-R2018 | Standalone P&L, Profit from continuing operations (3-4) | 6 (p12) | - | - |
| 148 | R2019-R2024 | Standalone P&L, (Loss)/Profit before tax from discontinued operations | 6 (p12) | - | - |
| 149 | R2025-R2030 | Standalone P&L, Tax (credit)/expense of discontinued operations | 6 (p12) | - | - |
| 150 | R2031-R2036 | Standalone P&L, (Loss)/Profit after tax from discontinued operations | 6 (p12) | - | - |
| 151 | R2037-R2042 | Standalone P&L, Net profit after tax (5+7) | 6 (p12) | - | - |
| 152 | R2043-R2048 | Standalone P&L, OCI: Remeasurement (loss)/gain on defined benefit plans | 6 (p12) | - | - |
| 153 | R2049-R2054 | Standalone P&L, OCI: Income tax relating to remeasurement | 6 (p12) | - | - |
| 154 | R2055-R2060 | Standalone P&L, Other comprehensive income, net of tax | 6 (p12) | - | - |
| 155 | R2061-R2066 | Standalone P&L, Total comprehensive income (8+9) | 6 (p12) | - | - |
| 156 | R2067-R2072 | Standalone P&L, Paid up equity share capital (face value Rs. 2 each) | 6 (p12) | - | - |
| 157 | R2073 | Standalone P&L, Reserves i.e. other equity | 1 (p12) | - | - |
| 158 | R2074-R2079 | Standalone P&L, EPS continuing operations, Basic and Diluted (Rs.) | 6 (p12) | - | - |
| 159 | R2080-R2085 | Standalone P&L, EPS discontinued operations, Basic and Diluted (Rs.) | 6 (p12) | - | - |
| 160 | R2086-R2091 | Standalone P&L, EPS continuing and discontinued, Basic and Diluted (Rs.) | 6 (p12) | FOOTING_GAP | FOOTING_GAP at R2090: printed 248.87 vs computed 248.67 |
| 161 | R2092-R2093 | Standalone Balance Sheet, Property, plant and equipment | 2 (p13) | - | - |
| 162 | R2094-R2095 | Standalone Balance Sheet, Capital work-in-progress | 2 (p13) | ZERO_STANDING | nil/dash cells R2094 |
| 163 | R2096-R2097 | Standalone Balance Sheet, Investment property | 2 (p13) | - | - |
| 164 | R2098-R2099 | Standalone Balance Sheet, Intangible assets | 2 (p13) | - | - |
| 165 | R2100-R2101 | Standalone Balance Sheet, Financial assets (a) Investment in subsidiaries | 2 (p13) | - | - |
| 166 | R2102-R2103 | Standalone Balance Sheet, Financial assets (b) Other investments | 2 (p13) | - | - |
| 167 | R2104-R2105 | Standalone Balance Sheet, Financial assets (c) Other financial assets | 2 (p13) | - | - |
| 168 | R2106-R2107 | Standalone Balance Sheet, Other non-current assets | 2 (p13) | - | - |
| 169 | R2108-R2109 | Standalone Balance Sheet, Total Non-current assets | 2 (p13) | - | - |
| 170 | R2110-R2111 | Standalone Balance Sheet, Inventories | 2 (p13) | - | - |
| 171 | R2112-R2113 | Standalone Balance Sheet, Current financial assets (a) Trade receivables | 2 (p13) | - | - |
| 172 | R2114-R2115 | Standalone Balance Sheet, Current financial assets (b) Cash and cash equivalents | 2 (p13) | - | - |
| 173 | R2116-R2117 | Standalone Balance Sheet, Current financial assets (c) Other bank balances (other than | 2 (p13) | - | - |
| 174 | R2118-R2119 | Standalone Balance Sheet, Current financial assets (d) Loans | 2 (p13) | - | - |
| 175 | R2120-R2121 | Standalone Balance Sheet, Current financial assets (e) Other financial assets | 2 (p13) | - | - |
| 176 | R2122-R2123 | Standalone Balance Sheet, Other current assets | 2 (p13) | - | - |
| 177 | R2124-R2125 | Standalone Balance Sheet, Total current assets | 2 (p13) | - | - |
| 178 | R2126-R2127 | Standalone Balance Sheet, Non current assets held for sale (refer note 6 & 7) | 2 (p13) | - | - |
| 179 | R2128-R2129 | Standalone Balance Sheet, TOTAL ASSETS | 2 (p13) | - | - |
| 180 | R2130-R2131 | Standalone Balance Sheet, Equity share capital | 2 (p13) | - | - |
| 181 | R2132-R2133 | Standalone Balance Sheet, Other equity | 2 (p13) | - | - |
| 182 | R2134-R2135 | Standalone Balance Sheet, Total Equity | 2 (p13) | - | - |
| 183 | R2136-R2137 | Standalone Balance Sheet, Non-current liabilities: Provisions | 2 (p13) | - | - |
| 184 | R2138-R2139 | Standalone Balance Sheet, Non-current liabilities: Deferred tax liabilities (net) | 2 (p13) | - | - |
| 185 | R2140-R2141 | Standalone Balance Sheet, Total non-current liabilities | 2 (p13) | - | - |
| 186 | R2142-R2143 | Standalone Balance Sheet, Trade payables: micro enterprises and small enterprises | 2 (p13) | ZERO_STANDING | nil/dash cells R2142-R2143 (all cells) |
| 187 | R2144-R2145 | Standalone Balance Sheet, Trade payables: creditors other than micro and small enterpr | 2 (p13) | - | - |
| 188 | R2146-R2147 | Standalone Balance Sheet, Other financial liabilities (Refer note 8) | 2 (p13) | - | - |
| 189 | R2148-R2149 | Standalone Balance Sheet, Other current liabilities | 2 (p13) | - | - |
| 190 | R2150-R2151 | Standalone Balance Sheet, Provisions (current) | 2 (p13) | - | - |
| 191 | R2152-R2153 | Standalone Balance Sheet, Current tax liabilities (net) | 2 (p13) | - | - |
| 192 | R2154-R2155 | Standalone Balance Sheet, Total current liabilities | 2 (p13) | - | - |
| 193 | R2156-R2157 | Standalone Balance Sheet, Liabilities associated with non current assets held for sale | 2 (p13) | - | - |
| 194 | R2158-R2159 | Standalone Balance Sheet, TOTAL LIABILITIES | 2 (p13) | - | - |
| 195 | R2160-R2161 | Standalone Balance Sheet, TOTAL EQUITY AND LIABILITIES | 2 (p13) | - | - |
| 196 | R2162-R2163 | Standalone Cash Flow, Profit before Tax from continuing operations | 2 (p14) | - | - |
| 197 | R2164-R2165 | Standalone Cash Flow, Profit before tax from discontinued operations | 2 (p14) | - | - |
| 198 | R2166-R2167 | Standalone Cash Flow, Profit before Tax | 2 (p14) | - | - |
| 199 | R2168-R2169 | Standalone Cash Flow, Depreciation and amortisation expense | 2 (p14) | - | - |
| 200 | R2170-R2171 | Standalone Cash Flow, (Reversal)/Provision for doubtful debts/advances/contingenci | 2 (p14) | - | - |
| 201 | R2172-R2173 | Standalone Cash Flow, Profit on sale of property, plant and equipment (net) | 2 (p14) | ZERO_STANDING | nil/dash cells R2172 |
| 202 | R2174-R2175 | Standalone Cash Flow, Gain on fair valuation measurement of financial assets | 2 (p14) | - | - |
| 203 | R2176-R2177 | Standalone Cash Flow, Liabilities / provisions no longer required written back | 2 (p14) | - | - |
| 204 | R2178-R2179 | Standalone Cash Flow, Interest Income | 2 (p14) | - | - |
| 205 | R2180-R2181 | Standalone Cash Flow, Unrealised (gain)/loss on foreign exchange fluctuation (net) | 2 (p14) | - | - |
| 206 | R2182-R2183 | Standalone Cash Flow, Finance cost | 2 (p14) | - | - |
| 207 | R2184-R2185 | Standalone Cash Flow, Operating loss before working capital changes | 2 (p14) | - | - |
| 208 | R2186-R2187 | Standalone Cash Flow, (Increase)/Decrease in trade receivables and financial/other | 2 (p14) | - | - |
| 209 | R2188-R2189 | Standalone Cash Flow, (Increase)/Decrease in inventories | 2 (p14) | - | - |
| 210 | R2190-R2191 | Standalone Cash Flow, Decrease in trade payables, financial/other liabilities and  | 2 (p14) | - | - |
| 211 | R2192-R2193 | Standalone Cash Flow, Cash generated from/(used in) operations | 2 (p14) | - | - |
| 212 | R2194-R2195 | Standalone Cash Flow, Income Taxes paid (net of refunds) | 2 (p14) | - | - |
| 213 | R2196-R2197 | Standalone Cash Flow, Net cash generated from/(used in) operating activities (A) | 2 (p14) | - | - |
| 214 | R2198-R2199 | Standalone Cash Flow, Acquisition of property, plant and equipment | 2 (p14) | - | - |
| 215 | R2200-R2201 | Standalone Cash Flow, Proceeds from sale of property, plant and equipment | 2 (p14) | - | - |
| 216 | R2202-R2203 | Standalone Cash Flow, Advance received against sale of land (net of expenses incur | 2 (p14) | ZERO_STANDING | nil/dash cells R2203 |
| 217 | R2204-R2205 | Standalone Cash Flow, Proceeds from sale of investment in subsidiary (net of expen | 2 (p14) | ZERO_STANDING | nil/dash cells R2204 |
| 218 | R2206-R2207 | Standalone Cash Flow, Investment in bank deposits | 2 (p14) | - | - |
| 219 | R2208-R2209 | Standalone Cash Flow, Redemption of bank deposits | 2 (p14) | - | - |
| 220 | R2210-R2211 | Standalone Cash Flow, Loan to subsidiary (upto November 15, 2025): Given | 2 (p14) | ZERO_STANDING | nil/dash cells R2210 |
| 221 | R2212-R2213 | Standalone Cash Flow, Loan to subsidiary (upto November 15, 2025): Realised | 2 (p14) | ZERO_STANDING | nil/dash cells R2212 |
| 222 | R2214-R2215 | Standalone Cash Flow, Loan to Other Company: Given | 2 (p14) | - | - |
| 223 | R2216-R2217 | Standalone Cash Flow, Loan to Other Company: Realised | 2 (p14) | - | - |
| 224 | R2218-R2219 | Standalone Cash Flow, Interest received | 2 (p14) | - | - |
| 225 | R2220-R2221 | Standalone Cash Flow, Net cash generated from investing activities (B) | 2 (p14) | - | - |
| 226 | R2222-R2223 | Standalone Cash Flow, Interest paid | 2 (p14) | - | - |
| 227 | R2224-R2225 | Standalone Cash Flow, Dividend paid | 2 (p14) | ZERO_STANDING | nil/dash cells R2224 |
| 228 | R2226-R2227 | Standalone Cash Flow, Net cash used in financing activities (C) | 2 (p14) | - | - |
| 229 | R2228-R2229 | Standalone Cash Flow, (D) Net (decrease)/increase in cash and cash equivalents (A+ | 2 (p14) | - | - |
| 230 | R2230-R2231 | Standalone Cash Flow, (E) Cash and cash equivalents as at the beginning of the yea | 2 (p14) | - | - |
| 231 | R2232-R2233 | Standalone Cash Flow, (F) Cash and cash equivalents as at the end of the year (D+E | 2 (p14) | - | - |

## 3. SUPERSEDED OCR ROWS (accounted by group mapping, excluded from figures)

| ROW_ID(s) | category | A2 flags | cross-ref / materiality |
|---|---|---|---|
| R088-R335, R1284-R1288 | SUPERSEDED old OCR rows page 4 (253 IDs) | SUPERSEDED | superseded by image group R1438-R1624; use group rows only |
| R336-R500, R1289-R1294 | SUPERSEDED old OCR rows page 5 (171 IDs) | SUPERSEDED | superseded by image group R1625-R1780; use group rows only |
| R501-R553 | SUPERSEDED old OCR rows page 6 (53 IDs) | SUPERSEDED | superseded by image group R1781-R1854; use group rows only |
| R554-R634 | SUPERSEDED old OCR rows page 7 (81 IDs) | SUPERSEDED | superseded by image group R1855-R1928; use group rows only |
| R758-R978, R1335-R1339 | SUPERSEDED old OCR rows page 12 (226 IDs) | SUPERSEDED | superseded by image group R1929-R2091; use group rows only |
| R979-R1058, R1340-R1341 | SUPERSEDED old OCR rows page 13 (82 IDs) | SUPERSEDED | superseded by image group R2092-R2161; use group rows only |
| R1059-R1138, R1342-R1344 | SUPERSEDED old OCR rows page 14 (83 IDs) | SUPERSEDED | superseded by image group R2162-R2233; use group rows only |

## 3b. IMAGE_VERIFIED rows (kept)

| ROW_ID(s) | category | A2 flags | cross-ref / materiality |
|---|---|---|---|
| R1378-R1396, R1417-R1425 | IMAGE_VERIFIED QUALIFIER rows pages 4-7,12-14 (28 IDs) | IMAGE_VERIFIED | counted under 1b footnotes; cross-ref only |

## 4. AGENDA ITEMS (Board Outcome letter)

| ROW_ID(s) | category | A2 flags | cross-ref / materiality |
|---|---|---|---|
| R005-R007, R1269, R1370-R1371 | agenda 1: approve unaudited standalone and consolidated results, quarter and half year ended Sep 30 2026, with limited review reports | - | - |
| R1227-R1228, R1270 | agenda 2: noted NCLT Amaravati order Oct 08 2026 convening meetings for merger of HNPCL into GOCL | - | - |
| R008-R009, R1247 | agenda 3: Board reviewed Notice and Explanatory Statement for NCLT-directed meetings | - | - |
| R010-R011, R1248, R1271 | agenda 4: NCLT meeting of equity shareholders and unsecured creditors Tue Nov 24 2026 11:00 IST by VC | - | - |

Not in the letter (stated, no rows): AR approval, AGM notice, record date, dividend declaration, director appointment, auditor change, scrutinizer, ESOP, fund-raise resolutions.

## 4b. MEETING TIMES AND SIGNATURE BLOCK

| ROW_ID(s) | category | A2 flags | cross-ref / materiality |
|---|---|---|---|
| R012-R015 | board meeting start 05:30 p.m., end about 07:20 p.m. (about 1h50m) | - | R012-R015 |
| R016-R022, R1229 | digital signature: A Satyanarayana, Company Secretary, 2026.10.19 20:19:43 +05:30 | - | signed after meeting end (19:20); no early-signature flag |

## 4c. LETTER HEADER / ADDRESS / CODES (page 1 remainder)

| ROW_ID(s) | category | A2 flags | cross-ref / materiality |
|---|---|---|---|
| R001-R004, R023-R043 | cover letter header, addresses, scrip codes, CIN, phone | - | identifier tokens |

## 5. AUDITOR REPORT PARAGRAPHS (limited review, Haribhakti & Co LLP)

| para | ROW_ID(s) | content | A2 flags |
|---|---|---|---|
| C1 | R1370-R1371 | scope: review of unaudited consolidated statement | - |
| C2 | page group (text-layer tokens, section 7) | management responsibility | - |
| C3 | R1372 | SRE 2410 review, not an audit | - |
| C4 | R1231 | entity list reviewed: GOCL holding, HGHL Holdings Limited UK WOS | - |
| C5 | R1374 | conclusion unmodified | - |
| C6 | R1373 | Emphasis of Matter: Note 4 guarantees Rs.131,610 lakhs not processed as RPT | EOM |
| C7 | R1375-R1377 | Other Matter: one subsidiary reviewed by other auditor; local GAAP to Ind AS by management | OTHER_MATTER |
| S1 | page group (text-layer tokens, section 7) | standalone scope | - |
| S2 | page group (text-layer tokens, section 7) | management responsibility | - |
| S3 | page group (text-layer tokens, section 7) | review standard | - |
| S4 | R1416 | standalone conclusion unmodified | - |
| S5 | R1415 | Emphasis of Matter standalone Note 4 | EOM |

UDIN rows R086-R087 (consolidated, line 191) and R756-R757 (standalone, line 579). Audit partner Snehal Shah Mem 048539 (R1232). Report date Oct 19 2026 (R1283). All results unaudited; one subsidiary reviewed by another auditor (R1375). Going Concern language: none in rows. Opinion: limited review, unmodified, EoM on Note 4.

## 6. ENTITIES

| ROW_ID | entity | role | A2 flags | note |
|---|---|---|---|---|
| R1221 | GOCL Corporation Limited | reporting company | CONSOL_LIST | - |
| R1222 | BSE Limited | stock exchange | - | - |
| R1223 | National Stock Exchange of India Limited | stock exchange | - | - |
| R1224 | BSE Listing Center / NEAPS | filing portals | - | - |
| R1225 | GOCLCORP | NSE symbol; BSE 506480 | - | - |
| R1226 | Haribhakti & Co LLP | statutory auditors | - | - |
| R1227 | Hon'ble NCLT, Amaravati Bench | tribunal, regulator | - | - |
| R1228 | Hinduja National Power Corporation Limited (HNPCL) | merger transferor | - | - |
| R1229 | A Satyanarayana | Company Secretary | - | - |
| R1230 | Registered/Corporate offices | address block | - | - |
| R1231 | HGHL Holdings Limited, UK | wholly owned subsidiary | CONSOL_LIST | consolidation list = GOCL holding + HGHL Holdings UK WOS (standalone GOCL only); no prior list so no ENTITY_CHANGE |
| R1232 | Snehal Shah | audit partner, Mem 048539 | - | - |
| R1233 | Energetics Division | discontinued operations | - | - |
| R1234 | IDL Explosives Limited | discontinued, sold Nov 15 2025 | - | - |
| R1235 | ACHT Investment Limited | put option counterparty | - | - |
| R1236 | 57 Whitehall Investments SARL | put option investee | - | - |
| R1237 | Squarespace Builders Private Limited, Hyderabad | land buyer MoU | - | - |
| R1238 | Kukatpally, Hyderabad | 264.50 acres land | - | - |
| R1239 | Detonators and other blasting devices operations | ceased, Kukatpally | - | - |
| R1240 | IDL | discontinued business | - | - |
| R1241 | Hinduja Energy India Limited | guarantee beneficiary | - | - |
| R1242 | NCLAT | appellate tribunal | - | - |
| R1243 | SPVs of Tata Realty and Infrastructure Limited | Ecopolis buyer | - | - |
| R1244 | Hinduja Realty Ventures Limited | JDA counterparty Ecopolis | - | - |
| R1245 | Ecopolis, Yelahanka, Bengaluru | property held for sale | - | - |
| R1246 | DIN 09184688 | signing director | - | - |

## 7. FORWARD STATEMENTS, DATES, QUALIFIERS, TEXT-LAYER NUMBERS (remaining IDs, grouped)

| ROW_ID(s) | category | A2 flags | cross-ref / materiality |
|---|---|---|---|
| R1247-R1266 | FORWARD statements (20) | - | merger approvals pending; Ecopolis Rs.81,500 lakhs consideration pending formalities; land MoU Rs.3,41,800 lakhs 264.50 acres; guarantee regularisation; dividend Rs.30/sh paid post quarter; consolidated vs standalone restatements R1249/R1262, R1254/R1262 |
| R1267-R1268, R1272-R1282, R1295-R1334, R1345-R1369 | DATE rows (non-superseded) | - | - |
| R044-R071 | text-layer NUMBER tokens page 2: auditor report consolidated text tokens | - | values stay at ID |
| R072-R085 | text-layer NUMBER tokens page 3: auditor report consolidated EoM/OM text tokens | - | values stay at ID |
| R635-R711 | text-layer NUMBER tokens page 8: consolidated notes text tokens (acres, Rs.lakhs, dates) | - | values stay at ID |
| R712-R727 | text-layer NUMBER tokens page 9: consolidated notes 4-8 text tokens | - | values stay at ID |
| R728-R749 | text-layer NUMBER tokens page 10: auditor report standalone text tokens | - | values stay at ID |
| R750-R755 | text-layer NUMBER tokens page 11: auditor report standalone EoM text tokens | - | values stay at ID |
| R1139-R1156 | text-layer NUMBER tokens page 15: standalone notes text tokens | - | values stay at ID |
| R1157-R1220 | text-layer NUMBER tokens page 16: standalone notes text tokens | - | values stay at ID |

```yaml
stage: A2-enumerator
company: "GOCL"
quarter: "Q2 FY27"
doctype: "results"
model: claude-sonnet-5-5
status: complete
ledger_path: "runs/gocl-q2fy27/work/ledger_results_gocl_q2fy27.md"
counts:
  notes: 16
  line_items: 231
  zero_standing: 53
  agenda_items: 4
  auditor_paras: 12
  entities: 26
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, SUPERSEDED, IMAGE_VERIFIED, FOOTING_GAP, PRINTED_DIFF, RESTATED, EOM, OTHER_MATTER]
ids_in_structured: 2233
ids_referenced: 2233
orphan_ids: []
missing_from_structured: []
gate_a2: pass
mismatch_note: ""
analyst_note: "Superseded old OCR rows: 949 by row count (grep -c shows 950 because header line 5 repeats the token); all mapped to their page image group. Zero_standing: 31 nil/dash image cells across 21 line items, plus 1 A1-flagged non-superseded text row (R011). Three footing gaps sit on R1912 (investing B, H Sep25, +2.00), R1924 (net cash change, H Sep25, 10.00), R2090 (standalone EPS total, H Sep25, +0.20); printed values kept, not corrected. Guarantee to HNPCL prints as 109,640 lakhs in consolidated Note 4 (R1407) and 109,610 in standalone Note 4 (R1430), against 131,610 total in the EoM: PRINTED_DIFF. Both auditor reports carry an EoM on Note 4 guarantees not processed as RPT; conclusion unmodified. Meeting ran 05:30 to 07:20 p.m.; signature 20:19 follows. No prior ledger, so no ENTITY_CHANGE test."
```
