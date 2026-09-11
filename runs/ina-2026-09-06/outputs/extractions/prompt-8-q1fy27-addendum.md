# Prompt 8 addendum: Q1 FY2027 rows from the 12-August-2026 board outcome filing

Source document (single source for this extraction):
`runs/ina-2026-09-06/inputs/results/Q1FY27_Results_BoardOutcome_2026-08-12.pdf`
Extracted text: `runs/ina-2026-09-06/work/extracted/results__Q1FY27_Results_BoardOutcome_2026-08-12.txt`
Document's own date: 12-August-2026. Period covered: quarter ended 30-June-2026.
14 pages. Regulation 30 board-meeting outcome letter of Insolation Energy Limited
(BSE 543620, NSE INA).

Comparison documents used ONLY where marked, and always labelled:
`runs/ina-2026-09-06/work/extracted/annual-report__Annual_Report_2026.txt` (FY2026 Annual Report).
The screener data sheet was not needed and was not used.

All figures are Rs in LAKHS. The consolidated statement says "Rs in Lakhs" (page 3).
The standalone statement says "(In Lakhs)" (page 7).

---

## 0. OCR RELIABILITY

This PDF is a scan with an OCR text layer. Decimal points are dropped in most
numeric cells and digits are misread. tesseract is not available in this
container, so no re-OCR was possible. Every figure below was tested by
arithmetic before it was reported.

### 0.1 The decimal convention is proved, not assumed

The OCR drops the decimal point in most consolidated cells. That the true form
is two decimal places in Rs lakhs is proved three ways:

1. The standalone statement (page 7) retains decimals in many cells
   ("1,979.12", "2,445.79"), and those cells satisfy the statement's own
   arithmetic at two decimals.
2. The consolidated FY2026 column reconciles exactly at two decimals:
   2,14,602.13 + 1,750.25 = 2,16,352.38 (the printed Total Income).
3. FY2026 ANNUAL REPORT CROSS-CHECK. The FY2026 column of this filing matches
   the FY2026 Annual Report consolidated profit and loss line for line
   (AR extraction lines 15496 to 15560): revenue 2,14,602.13, other income
   1,750.25, total income 2,16,352.38, cost of materials 1,66,212.64,
   purchases 27,205.85, changes in inventories (21,874.20), employee 5,053.82,
   finance 2,354.09, depreciation 3,579.79, other 9,291.87, total expenses
   1,91,823.85, PBT 24,528.53, profit 20,063.15, OCI (16.01), total
   comprehensive 20,047.14. A whole audited column reproducing exactly is
   strong evidence that the decoding rule is right.

### 0.2 The three orchestrator-verified figures: I CONFIRM ALL THREE

- **Q1FY27 consolidated profit for the period Rs 3,802.46 lakh. AGREE.**
  Chain: revenue 74,069.83 + other income 470.59 = total income 74,540.42.
  74,540.42 - total expenses 69,790.45 = 4,749.97 (PBT).
  4,749.97 - total tax 947.51 = 3,802.46. The OCR string for profit is
  "380246", which matches. Three separately garbled cells all reconcile to
  this, so the chain is not a coincidence.
- **Owners Rs 3,703.64 lakh, non-controlling interests Rs 98.82 lakh. AGREE.**
  3,703.64 + 98.82 = 3,802.46 exactly. OCR strings "370364" and "9882" match.
- **Q1FY27 standalone loss Rs (291.05) lakh against Rs (180.60) lakh for the
  quarter ended 31-March-2026. AGREE.**
  Q1FY27: total income 1,294.22 - total expenses 1,548.70 = (254.48) PBT;
  (254.48) - tax 36.56 = (291.04), printed (291.05). A 0.01 rounding
  difference, see 0.5.
  Q4FY26: 2,179.76 - 2,445.79 = (266.03); (266.03) - (85.43) = (180.60) exact.

### 0.3 Digits the OCR garbled that arithmetic FIXES (corrected figures given)

| Item | Column | OCR string | Corrected | Arithmetic that fixes it |
|---|---|---|---|---|
| Profit before tax, lines 3 and 5 | Q1FY27 consol | "374997" and "174997" | 4,749.97 | 74,540.42 total income - 69,790.45 total expenses |
| Total Income | Q1FY27 consol | "754041" | 74,540.42 | 74,069.83 + 470.59; and 74,540.42 - 69,790.45 = 4,749.97 PBT |
| Current tax | Q1FY27 consol | "sa282" | 882.83 | total tax 947.51 - deferred 64.68 |
| Profit before tax line 5 | FY26 consol | "2452053" | 24,528.53 | matches line 3 "2452853" and the FY2026 AR |
| Total other comprehensive income | Q4FY26 consol | "1892" (line 8 shows "1882") | 18.82 | 7,003.29 - 6,984.47; also 18.97 + (0.15) |
| Total OCI attributable, sum row | Q4FY26 consol | "1862" | 18.82 | 18.97 + (0.15) |
| Profit attributable to NCI | Q4FY26 consol | "@29)" | (22.92) | 6,984.47 - 7,007.39; and (22.92) + (0.15) = (23.07) TCI NCI |
| Total comprehensive income, NCI | Q4FY26 consol | "@307)" | (23.07) | 7,003.29 - 7,026.36 |
| Profit attributable to owners | Q1FY26 consol | "429691" | 4,296.94 | 4,297.70 TCI owners - 0.76 OCI owners; and 4,296.94 + 15.04 = 4,311.98 profit |
| Profit attributable to NCI | Q1FY26 consol | "1508" | 15.04 | 15.17 TCI NCI - 0.13 OCI NCI; ties to 4,311.98 |
| OCI attributable to owners | FY26 consol | "(159)" | (15.96) | 20,005.70 - 20,021.66; and (15.96) + (0.05) = (16.01) |
| Total comprehensive income, NCI | FY26 consol | "a4" | 41.44 | 20,047.14 - 20,005.70; FY2026 AR prints 41.44 |
| Changes in inventories | FY26 standalone | "55530" (brackets lost) | (555.30) | expense lines sum to 9,624.99 against printed 9,625.01 only if negative; FY2026 AR line 27078 prints "(555.30)" |
| Other income | Q4FY26 consol | "5480)" | (154.84) DERIVED, see 0.4 | 79,238.32 total income - 79,393.16 revenue |
| Cost of materials consumed | Q1FY27 consol | "82739" | 59,267.48 DERIVED, see 0.4 | 69,790.45 total expenses minus the six other expense lines (10,522.97) |

### 0.4 Two figures DERIVED by residual, not read. Treat with care.

**Q1FY27 consolidated cost of materials consumed = Rs 59,267.48 lakh.**
The printed cell OCRs as "82739", five characters, clearly truncated, and bears
no digit resemblance to any plausible value. Derivation:
total expenses 69,790.45, minus purchases of stock-in-trade 81.57, minus
changes in inventories 2,711.26, minus employee benefits 1,817.84, minus
finance costs 1,204.45, minus depreciation 1,692.35, minus other expenses
3,015.50. Those six sum to 10,522.97. 69,790.45 - 10,522.97 = 59,267.48.
CAVEAT: this residual is only as good as those six OCR readings, none of which
can be tested individually in the Q1FY27 column because the usual
sub-lines-sum-to-total test is consumed by the derivation. In the other three
columns that same test passes to within 0.01, which supports the method but
does not prove the Q1FY27 six. Sanity: 59,267.48 / 74,069.83 = 80.0 percent of
revenue, against 88.1 percent in Q1FY26 and 77.5 percent in FY26.
Recommendation: re-read page 3 of the PDF visually before this number carries
any weight in a margin bridge.

**Q4FY26 consolidated other income = Rs (154.84) lakh.**
Only the SUM is proved. Total expenses 70,609.10 + PBT 8,629.22 = total income
79,238.32, which matches the printed "7923832". Revenue prints as "7939316"
(79,393.16). 79,238.32 - 79,393.16 = (154.84). The OCR cell is "5480)", and the
stray closing bracket is direct evidence that the printed figure is in
brackets, that is negative. A negative other income is possible at this
company: the standalone Q1FY26 other income prints as "(28.03)". The split
between revenue and other income in this column is UNDERDETERMINED: either
revenue is 79,393.16 with other income (154.84), or revenue is lower and other
income is small and positive. Only the 79,238.32 total is safe.

### 0.5 Rounding noise of 0.01 to 0.02, present throughout

The statement rounds each line independently, so sub-lines do not always sum to
the printed total to the paisa. Every instance found:

| Check | Computed | Printed | Gap |
|---|---|---|---|
| Consol Q4FY26 expense lines sum | 70,609.11 | 70,609.10 | 0.01 |
| Consol Q4FY26 PBT less total tax | 6,984.48 | 6,984.47 | 0.01 |
| Consol FY26 expense lines sum | 1,91,823.86 | 1,91,823.85 | 0.01 |
| Consol FY26 tax lines sum | 4,465.37 | 4,465.38 | 0.01 |
| Consol Q1FY27 TCI owners (3,703.64 + 15.73) | 3,719.37 | 3,719.38 | 0.01 |
| Consol Q1FY27 TCI NCI (98.82 + 0.01) | 98.83 | 98.82 | 0.01 |
| Standalone Q1FY27 PBT less tax | (291.04) | (291.05) | 0.01 |
| Standalone Q4FY26 revenue + other income | 2,179.77 | 2,179.76 | 0.01 |
| Standalone Q4FY26 expense lines sum | 2,445.80 | 2,445.79 | 0.01 |
| Standalone Q4FY26 tax lines sum | (85.42) | (85.43) | 0.01 |
| Standalone Q4FY26 TCI | (184.90) | (184.91) | 0.01 |
| Standalone FY26 revenue + other income | 10,560.25 | 10,560.24 | 0.01 |
| Standalone FY26 expense lines sum | 9,624.99 | 9,625.01 | 0.02 |
| Standalone FY26 tax lines sum | 216.90 | 216.91 | 0.01 |
| Standalone FY26 PBT less tax | 718.32 | 718.33 | 0.01 |

None of these change any figure at the rupee-lakh level. The printed figures are
used throughout.

### 0.6 What I could NOT confirm

- The Q4FY26 consolidated revenue / other income SPLIT (see 0.4). The total
  79,238.32 is confirmed; the two components are not.
- The six Q1FY27 consolidated expense sub-lines other than cost of materials
  (purchases, changes in inventories, employee benefits, finance costs,
  depreciation, other expenses). Their AGGREGATE with cost of materials is
  pinned by total expenses 69,790.45. Individually they rest on OCR alone.
  This matters for finance costs (section C) and depreciation (section E).
- The two UDIN strings on the review reports (see section F). Both OCR to
  nonsense and no arithmetic exists. Marked OCR UNRESOLVED.

### 0.7 Figures marked OCR UNRESOLVED, do not use

| Item | Page | OCR string | Why unresolved |
|---|---|---|---|
| UDIN, consolidated limited review report | 6 | "264063Y44CD AROG 3BY)" | Alphanumeric, no arithmetic check exists |
| UDIN, standalone limited review report | 10 | "2640 534U VR HOKN QUL" | Alphanumeric, no arithmetic check exists |
| CIN, consolidated statement header | 3 | "L40104RJ20 15PLCO4B445" | Garbled. Page 7 standalone header gives "L40104Rj2015PLCO48445". FY2026 AR should be used for the correct CIN |
| Q4FY26 consolidated other income as PRINTED | 3 | "5480)" | Value (154.84) is derived, not read, see 0.4 |
| Q1FY27 consolidated cost of materials as PRINTED | 3 | "82739" | Value 59,267.48 is derived, not read, see 0.4 |

---

## A. FULL RESULTS REPRODUCTION

### A.1 Consolidated statement, page 3

Quote, page 3 heading:
> "STATEMENT OF CONSOLIDATED FINANCIAL RESULTS FOR THE QUARTER ENDED 30TH JUNE 2026"
> "Rsin Lakhs"

Quote, page 3 column labels:
> "Quarter Ended | Year ended"
> "0th [une 2026 | 315t March 2026 | _30th june 2025 | _31st Mar 2026"
> "(Unaudited) (Unaudited) (Unaudited) (Audited)"

Comment. The filing labels all three quarter columns Unaudited and the year
column Audited. That includes the quarter ended 31-March-2026, which the filing
calls Unaudited even though it is the Q4 balancing quarter of an audited year.
The column-header dates are OCR-garbled but unambiguous in sequence:
30-June-2026, 31-March-2026, 30-June-2025, 31-March-2026 (year).

All figures Rs in lakhs.

| # | Line | Q ended 30-Jun-2026 (Unaudited) | Q ended 31-Mar-2026 (Unaudited) | Q ended 30-Jun-2025 (Unaudited) | Year ended 31-Mar-2026 (Audited) |
|---|---|---|---|---|---|
| 1 | Revenue from operations | 74,069.83 | 79,393.16 (split unconfirmed) | 36,188.53 | 2,14,602.13 |
| 1 | Other income | 470.59 | (154.84) DERIVED | 106.25 | 1,750.25 |
| 1 | Total Income | **74,540.42** CORRECTED | 79,238.32 | 36,294.78 | 2,16,352.38 |
| 2 | Cost of materials consumed | **59,267.48** DERIVED | 61,798.75 | 31,871.67 | 1,66,212.64 |
| 2 | Purchases of Stock-in-Trade | 81.57 | 16,078.43 | 132.34 | 27,205.85 |
| 2 | Changes in inventories of finished goods, WIP and stock-in-trade | 2,711.26 | (15,153.51) | (3,709.72) | (21,874.20) |
| 2 | Employee benefits expense | 1,817.84 | 1,669.31 | 800.90 | 5,053.82 |
| 2 | Finance costs | 1,204.45 | 785.40 | 297.00 | 2,354.09 |
| 2 | Depreciation and amortisation expense | 1,692.35 | 1,495.78 | 278.56 | 3,579.79 |
| 2 | Other expenses | 3,015.50 | 3,934.95 | 1,418.85 | 9,291.87 |
| 2 | Total Expenses | 69,790.45 | 70,609.10 | 31,089.60 | 1,91,823.85 |
| 3 | Profit before share of profit from associates and tax | **4,749.97** CORRECTED | 8,629.22 | 5,205.18 | 24,528.53 |
| 4 | Share of (Loss)/Profit from associates, net of tax | blank (nil) | blank (nil) | blank (nil) | blank (nil) |
| 5 | Profit before tax | **4,749.97** CORRECTED | 8,629.22 | 5,205.18 | 24,528.53 CORRECTED |
| 6 | Current tax | **882.83** CORRECTED | 1,427.92 | 248.24 | 3,458.81 |
| 6 | Deferred tax | 64.68 | 207.81 | 644.96 | 997.55 |
| 6 | Earlier year tax {Short/(Excess)} | blank (nil) | 9.01 | blank (nil) | 9.01 |
| 6 | Total Tax expenses | 947.51 | 1,644.74 | 893.20 | 4,465.38 |
| 7 | **Profit for the period/year** | **3,802.46** | 6,984.47 | 4,311.98 | 20,063.15 |
| 8 | Other Comprehensive Income (net of tax), items not reclassified | 15.74 | 18.82 CORRECTED | 0.89 | (16.01) |
| 8 | Items that will be reclassified to profit or loss | blank (nil) | blank (nil) | blank (nil) | blank (nil) |
| 8 | Total other comprehensive (loss)/income, net of tax | 15.74 | 18.82 CORRECTED | 0.89 | (16.01) |
| 9 | Total comprehensive income | 3,818.20 | 7,003.29 | 4,312.87 | 20,047.14 |
| 10 | Profit attributable to owners of the Company | **3,703.64** | 7,007.39 | 4,296.94 CORRECTED | 20,021.66 |
| 10 | Profit attributable to non-controlling interests | **98.82** | (22.92) CORRECTED | 15.04 CORRECTED | 41.49 |
| 10 | Sum | 3,802.46 | 6,984.47 | 4,311.98 | 20,063.15 |
| 11 | OCI attributable to owners | 15.73 | 18.97 | 0.76 | (15.96) CORRECTED |
| 11 | OCI attributable to NCI | 0.01 | (0.15) | 0.13 | (0.05) |
| 11 | Sum | 15.74 | 18.82 CORRECTED | 0.89 | (16.01) |
| 12 | Total comprehensive income attributable to owners | 3,719.38 | 7,026.36 | 4,297.70 | 20,005.70 |
| 12 | Total comprehensive income attributable to NCI | 98.82 | (23.07) CORRECTED | 15.17 | 41.44 CORRECTED |
| 12 | Sum | 3,818.20 | 7,003.29 | 4,312.87 | 20,047.14 |
| 13 | Paid up share capital (face value Rs 1/- per share) | 2,204.49 | 2,203.95 | 2,203.43 | 2,203.95 |
| 14 | Other equity | not shown | not shown | not shown | 78,510.24 |
| 15 | EPS annualisation label | "Not annualised" | "Not annualised" | "Not annualised" | "Annualised" |
| 15 | Earnings per share, Basic (Rs) | **1.73** | 3.17 | 1.96 | 9.10 |
| 15 | Earnings per share, Diluted (Rs) | **1.73** | 3.17 | 1.96 | 9.10 |

Quote, page 3, the Q1FY27 profit rows as the OCR renders them:
> "7 |Profitfor the period/year (5-6)   380246   698447   431198   2006315"
> "10 {Profit for the period/year attributable to"
> "owners of the Company   370364   700739   429691   2002166"
> "Non-controlling interests   9882   @29)   1508   4149"

Comment. Line 9 is printed "(7+8)" and line 7 is printed "(5-6)". Both labels are
consistent with the arithmetic.

Signature block, page 3:
> "For Insolation Energy Limited ... DIN No 02917023 Chairman & whole Time Director"
> "Dode ' 19" Puguad Qo6" and "Place : Deupur"

Comment. The date and place on the signature block are OCR-garbled beyond
repair on page 3. The letter on page 1 dates the board meeting 12-August-2026
and the auditor reports (pages 6 and 10) give "Date: 12th August 2026, Place:
Jaipur". The DIN 02917023 is Mr Manish Gupta.

### A.2 Consolidated EPS: basis confirmed, and it is NOT the owners' share

This is a finding, not an interpretation. In all four columns the printed EPS
reproduces only when TOTAL profit for the period (owners plus non-controlling
interests) is divided by the OPENING paid up share capital in lakhs:

| Column | Total profit | Divisor (paid up capital, lakhs) | Computed | Printed |
|---|---|---|---|---|
| Q1FY27 | 3,802.46 | 2,203.95 | 1.7253 -> 1.73 | 1.73 |
| Q4FY26 | 6,984.47 | 2,203.95 | 3.1691 -> 3.17 | 3.17 |
| Q1FY26 | 4,311.98 | 2,203.43 | 1.9569 -> 1.96 | 1.96 |
| FY26 | 20,063.15 | 2,203.95 | 9.1042 -> 9.10 | 9.10 |

On the owners' share instead, Q1FY27 basic EPS would be 3,703.64 / 2,204.49 =
**1.68**, and FY26 would be 9.08. The printed figures are therefore internally
consistent across all four columns, and they are computed on a basis that
includes the non-controlling interests. Both numbers are stated here and left
to stand. The FY2026 Annual Report prints the same 9.10 for FY26 (AR extraction
line 15571), so the basis is not new to this filing.

Basic equals diluted in every column of both statements.

### A.3 Standalone statement, page 7

Quote, page 7 heading:
> "STATEMENT OF STANDALONE FINANCIAL RESULTS FOR THE QUARTER ENDED 30TH JUNE 2026"
> "(In Lakhs)"

Quote, page 7 column labels:
> "Quarter Ended | Year ended"
> "30th June 2026 | 31stMarch 2026 |  30th June 2025 | 315t Mar 2026"
> "(Unaudited) (Unaudited) (Unaudited)"

Comment. Only THREE audit labels are printed on the standalone statement, one
under each quarter column. The year ended 31-March-2026 column carries NO audit
label. The consolidated statement labels its year column "(Audited)". The
standalone year column does not. Stated as printed.

All figures Rs in lakhs.

| # | Line | Q ended 30-Jun-2026 (Unaudited) | Q ended 31-Mar-2026 (Unaudited) | Q ended 30-Jun-2025 (Unaudited) | Year ended 31-Mar-2026 (no label printed) |
|---|---|---|---|---|---|
| 1 | Revenue from operations | 1,219.03 | 1,979.12 | 3,039.21 | 9,802.52 |
| 1 | Other income | 75.19 | 200.65 | (28.03) | 757.73 |
| 1 | Total Income | 1,294.22 | 2,179.76 | 3,011.18 | 10,560.24 |
| 2 | Cost of materials consumed | 1,149.15 | 1,467.40 | 2,783.98 | 7,578.21 |
| 2 | Purchases of Stock-in-Trade | 0.85 | 336.73 | 48.14 | 1,087.24 |
| 2 | Changes in inventories of finished goods, WIP and stock-in-trade | 38.16 | 246.44 | (213.61) | (555.30) CORRECTED |
| 2 | Employee benefits expense | 99.85 | 43.99 | 104.87 | 429.33 |
| 2 | Finance costs | 64.62 | 69.46 | 49.13 | 258.19 |
| 2 | Depreciation and amortisation expense | 110.09 | 93.45 | 51.98 | 319.39 |
| 2 | Other expenses | 85.98 | 188.33 | 113.76 | 507.93 |
| 2 | Total Expenses | 1,548.70 | 2,445.79 | 2,938.25 | 9,625.01 |
| 3 | Profit before tax | **(254.48)** | (266.03) | 72.93 | 935.23 |
| 4 | Current tax | "-" (nil) | (150.40) | 17.58 | 26.59 |
| 4 | Deferred tax | 36.56 | 64.98 | 7.20 | 190.31 |
| 4 | Earlier year tax {Short/(Excess)} | blank (nil) | blank (nil) | blank (nil) | blank (nil) |
| 4 | Total Tax expenses | 36.56 | (85.43) | 24.78 | 216.91 |
| 5 | **Profit/(loss) for the period/year** | **(291.05)** | **(180.60)** | 48.15 | 718.33 |
| 6 | Other Comprehensive Income (net of tax), items not reclassified | 10.76 | (4.30) | (0.67) | (0.64) |
| 6 | Items that will be reclassified to profit or loss | blank (nil) | blank (nil) | blank (nil) | blank (nil) |
| 6 | Total other comprehensive (loss)/income, net of tax | 10.76 | (4.30) | (0.67) | (0.64) |
| 7 | Total comprehensive income | (280.29) | (184.91) | 47.48 | 717.69 |
| 8 | Paid up share capital (face value Rs 1/- per share) | 2,204.49 | 2,203.95 | 2,203.43 | 2,203.95 |
| 9 | Other equity | not shown | not shown | not shown | 41,982.03 |
| 10 | EPS annualisation label | "Not annualised" | "Not annualised" | "Not annualised" | "Annualised" |
| 10 | Earnings per share, Basic (Rs) | **(0.13)** | (0.08) | 0.02 | 0.33 |
| 10 | Earnings per share, Diluted (Rs) | **(0.13)** | (0.08) | 0.02 | 0.33 |

Quote, page 7:
> "5 |Profit for the period/year (3-4)   (291.05)   (180.60)   4815   718.33"
> "8 |Paid up share Capital (face value of Rs.1/- per share)   220449   2,203.95   2,203.43   2203.95"

Standalone EPS check, all four columns reproduce on profit for the period
divided by paid up capital: (291.05)/2,203.95 = (0.132) -> (0.13);
(180.60)/2,203.95 = (0.082) -> (0.08); 48.15/2,203.43 = 0.022 -> 0.02;
718.33/2,203.95 = 0.326 -> 0.33. All confirmed.

Comment on the standalone Q4FY26 current tax. It is printed in brackets,
(150.40), a current tax CREDIT. Confirmed by arithmetic: (150.40) + 64.98 =
(85.42) against the printed total tax (85.43), a 0.01 rounding gap.

Comment on line 7 label. It is printed "Total comprehensive income (5-6)" but
the arithmetic is 5 plus 6: (291.05) + 10.76 = (280.29). The printed value is
right, the label is wrong. The consolidated statement prints "(7+8)" correctly.

### A.4 Consolidated notes, page 4 (six notes, quoted)

> "1) The above consolidated financial results of Insolation Energy Limited
> ("Company") including its wholly owned subsidiaries (collectively known as the
> "Group) and it associates has been prepared in accordance with the Indian
> Accounting Standards ("Ind AS") prescribed under Section 133 of the Companies
> Act, 2013 (the Act) read with the relevant rules issued thereunder..."

> "2) The above audited consolidated financial results has been prepared in
> accordance with principles and procedures as set out in the Ind AS 110 on
> "Consolidated financial statements" and Ind AS 28 on "Investments in Associates
> and Subsidiary" notified under Section 133 of the Act..."

Comment. Note 2 says "audited consolidated financial results". The column header
on page 3 says "(Unaudited)" for the quarter, the letter on page 1 says
"Un-Audited Financial Results", and the auditors on pages 5 and 6 issue a
limited review conclusion, not an audit opinion. The word "audited" in note 2 is
inconsistent with the rest of the filing. Stated, not interpreted.

> "3) The above consolidated financial results of the group as reviewed by the
> Audit Committee has been approved by the Board of Directors at its meeting held
> on 12th Aug, 2026, The results for the quarter ended on 30th June, 2026 has been
> reviewed by the statutory auditor. The statutory auditors of the Company have
> expressed an unmodified opinion on the financial results for the Quarter ended
> on 30th June, 2026 and have issued an unmodified conclusion in respect of the
> Limited review for the quarter ended 30th June, 2026."

Comment. Note 3 claims both an "unmodified opinion" and an "unmodified
conclusion". The report at pages 5 and 6 is a limited review and gives a
conclusion only. It contains no opinion paragraph. Stated, not interpreted.

> "4) The figures for the quarter ended 30th June, 2025 are the balancing figures
> taken from unaudited published figures of First Half ended on 30th Sept, 2025 and
> the unaudited published results of quarter ended on 30th Sept, 2025"

Comment. This is quoted exactly. As written it describes the June-2025 quarter
as H1 FY2026 minus the September-2025 quarter.

> "5) The Group is engaged in business of "manufacturing of solar panel and sale
> of electricity and related project activities" which constitutes a single segment
> as per Ind AS 108 - 'Operating Segments."

> "6) During the quarter ended on 30th June 2026, the Company on 25th May, 2026,
> allotted 54,750 equity shares of face value to Rs. 1/-each, at an exercise price
> of Rs. 3.8/-each, under Insolation Energy Employee Stock Option Plan 2024."

### A.5 Standalone notes, page 8 (five notes)

Notes 1, 2, 3 and 5 on page 8 mirror the consolidated notes 1, 3, 4 and 6 above,
with "standalone" substituted for "consolidated". Note 2 on page 8 repeats the
"unmodified opinion ... and ... unmodified conclusion" wording. Note 4 reads:

> "4) The Company is engaged in business of "manufacturing and selling of solar
> panel and sale of electricity and related project activities" which constitutes a
> single segment as per Ind AS 108 - 'Operating Segments."

Comment. The standalone note 2 says "The above standalone financial results of
the group", using "group" in a standalone statement. Stated as printed.

---

## B. RECEIVABLES (prompt 1, Q1 row)

**NOT DISCLOSED.** The filing carries no trade receivables figure, no ageing
schedule, and no expected credit loss provision. A full-text search of all 14
pages for "receivab", "credit loss", "ageing" and "balance sheet" returns
nothing.

What the filing DOES carry: a statement of profit and loss only, consolidated
(page 3) and standalone (page 7), plus notes (pages 4 and 8), two limited review
reports (pages 5 to 6, 9 to 10) and two director annexures (pages 11 to 14).

What it does NOT carry: no statement of assets and liabilities, no balance
sheet, no cash flow statement, no note on trade receivables, no ageing bucket,
no ECL provision, no movement in provision.

Where the fact would normally be found if it exists:
- SEBI LODR Regulation 33(3)(f) requires a listed entity to submit the statement
  of assets and liabilities and the cash flow statement as at the end of the
  HALF YEAR, along with the half-yearly results. A first-quarter filing is not
  required to carry either. The next occurrence for this company is the
  September-2026 quarter and half-year filing.
- FY2026 Annual Report: consolidated and standalone balance sheet, the note on
  Trade Receivables, and the trade receivables ageing schedule required by
  Schedule III Division II.

---

## C. DEBT AND FINANCE COST (prompt 3, Q1 row)

### C.1 Finance costs, all four columns, both statements

Quote, page 3, consolidated, finance costs row as the OCR renders it:
> "Finance costs   120445   78540   29700   235409"

| Finance costs (Rs lakh) | Q ended 30-Jun-2026 | Q ended 31-Mar-2026 | Q ended 30-Jun-2025 | Year ended 31-Mar-2026 |
|---|---|---|---|---|
| Consolidated | 1,204.45 | 785.40 | 297.00 | 2,354.09 |
| Standalone | 64.62 | 69.46 | 49.13 | 258.19 |

Arithmetic support. The Q4FY26, Q1FY26 and FY26 consolidated columns each have
all seven expense lines summing to the printed total expenses to within 0.01
(70,609.11 vs 70,609.10; 31,089.60 exact; 1,91,823.86 vs 1,91,823.85). Finance
costs 785.40, 297.00 and 2,354.09 are therefore confirmed as part of a sum that
closes. The FY26 figure 2,354.09 also matches the FY2026 ANNUAL REPORT
consolidated profit and loss exactly (AR extraction line 15530 block). The
Q1FY27 figure 1,204.45 CANNOT be confirmed individually, because the closing
test in that column is consumed by deriving cost of materials (see 0.4). It is
reported as read.

Standalone finance costs pass the same test: the Q1FY26 column sums exactly to
2,938.25, and the Q4FY26 and FY26 columns to within 0.01 and 0.02.

Comment. Consolidated finance cost at 1,204.45 is 53.4 percent above the
785.40 of the immediately preceding quarter and 4.05 times the 297.00 of
Q1FY26. Standalone finance cost of 64.62 is 5.4 percent of the consolidated
figure, so the borrowing sits almost entirely in subsidiaries. Both statements
are quoted; no interpretation is offered.

### C.2 Everything else asked for: NOT DISCLOSED

- Borrowings, gross or net: **NOT DISCLOSED**. No balance sheet is attached.
- Guarantees given: **NOT DISCLOSED**. A full-text search for "guarantee"
  returns nothing across all 14 pages.
- Covenant disclosure, breach or waiver: **NOT DISCLOSED**. A full-text search
  for "covenant" returns nothing.
- Balance sheet or statement of assets and liabilities: **NOT ATTACHED**.
- Cash flow statement: **NOT ATTACHED**.
- Contingent liabilities: **NOT DISCLOSED**.
- Related party transactions: **NOT DISCLOSED**.

Where these would normally be found if they exist: the half-yearly Regulation
33(3)(f) statement of assets and liabilities and cash flow statement, filed with
the September-2026 quarter; the separate Regulation 23(9) related party
disclosure filed within the same window; and in the FY2026 Annual Report, the
notes on Borrowings, on Contingent Liabilities and Commitments, and on Related
Party Transactions.

---

## D. CELL PLANT AND SEGMENT (prompts 4 and 6, Q1 rows)

### D.1 The Narmadapuram cell line: the only mention is a postal address

The filing mentions Narmadapuram exactly twice in readable form, both times in
the factory-address block of the company letterhead footer, on pages 12 and 14.
A third, heavily garbled occurrence sits in the same footer position on page 2.

Quote, page 12 footer (identical text on page 14):
> "INA 4 & 5: Factory - Mohasa-Babai, Narmadapuram, Bhopal, (MP) - 411661"

Quote, page 2 footer, garbled:
> "INA 4 & 5: Factory Babai, Narm p )"

Comment. This is a printed letterhead address line, not a disclosure. It
confirms only that the company lists INA 4 and INA 5 at Mohasa-Babai,
Narmadapuram.

The full factory list on the same footer, page 12 and page 14:
> "INA 1: Factory - Near Daulatpura Toll Tax, Jaipur-Delhi Bypass, Jaipur (Raj.) - 303805"
> "INA 2: Factory - Jatawali Industrial Area, Tehsil Chomu, Jaipur (Raj.)- 303806"
> "INA 3: Factory - NH - 48, Sawarda, Delhi -Ajmer Expressway, Jaipur (Raj.)- 303348"
> "INA 4 & 5: Factory - Mohasa-Babai, Narmadapuram, Bhopal, (MP) - 411661"

### D.2 Everything operational: NOT DISCLOSED

Every one of the following returns nothing on a full-text search of all 14 pages:

- Solar cell line commissioning date or status: **NOT DISCLOSED**
- Aluminium frame plant, commissioning or status: **NOT DISCLOSED**. The word
  "aluminium"/"aluminum"/"frame" does not appear anywhere in the filing.
- Capex incurred or committed in the quarter: **NOT DISCLOSED**
- Volumes in MW, module or cell: **NOT DISCLOSED**. The token "MW" does not
  appear in the filing.
- Realisation per watt or per unit: **NOT DISCLOSED**
- Order book or order inflow: **NOT DISCLOSED**
- Customer concentration: **NOT DISCLOSED**
- Installed or nameplate capacity: **NOT DISCLOSED**

Comment. The absence is the expected shape of a Regulation 30 board-outcome
letter carrying Regulation 33 results. This document type has no management
discussion, no operating metrics and no investor presentation attached. No
earnings presentation and no press release are enclosed. The enclosure line on
page 2 reads only:
> "Encl: as above"

Where these facts would normally be found if they exist: a quarterly investor
presentation or press release filed separately under Regulation 30, the earnings
call transcript, the FY2026 Annual Report (Management Discussion and Analysis,
Directors' Report, and the note on Capital Work in Progress), and Regulation 30
Schedule III Part A Para A intimations on commissioning of new capacity.

### D.3 Segment disclosure under Ind AS 108

Disclosed, and it is a single-segment declaration in both statements.

Quote, page 4, consolidated note 5:
> "The Group is engaged in business of "manufacturing of solar panel and sale of
> electricity and related project activities" which constitutes a single segment
> as per Ind AS 108 - 'Operating Segments."

Quote, page 8, standalone note 4:
> "The Company is engaged in business of "manufacturing and selling of solar
> panel and sale of electricity and related project activities" which constitutes
> a single segment as per Ind AS 108 - 'Operating Segments."

Comment. No segment revenue, segment result, segment asset or segment liability
table is given, because a single segment is declared. The consolidated wording
says "manufacturing of solar panel"; the standalone wording says "manufacturing
and selling of solar panel". No cell, frame or EPC segment is separated. No
split between module sales, electricity sales and project activities is given.

---

## E. SHARE COUNT, TAX, DEPRECIATION (prompt 7, Q1 row)

### E.1 Paid up share capital and implied share count at 30-June-2026

Quote, page 3, consolidated line 13:
> "13 {Paid up share Capital (face value of Rs1/-per share)   220449   220395   220343   220395"

Quote, page 7, standalone line 8:
> "8 |Paid up share Capital (face value of Rs.1/- per share)   220449   2,203.95   2,203.43   2203.95"

**Paid up share capital at 30-June-2026: Rs 2,204.49 lakh (Rs 22.0449 crore).**
Identical in both statements. Face value Re 1 per share.

**Implied share count at 30-June-2026: 22,04,49,375 shares (220,449,375).**

The arithmetic that fixes this exactly:
- FY2026 ANNUAL REPORT, statement of changes in equity (AR extraction line
  16006): "Balance as at the end of the year  22,03,94,625  2,203.95
  22,03,43,000  2,203.43". So 22,03,94,625 shares at 31-March-2026, and
  22,03,43,000 at 31-March-2025.
- This filing, page 4 note 6 and page 8 note 5: 54,750 equity shares of Re 1
  allotted on 25-May-2026 under the Insolation Energy Employee Stock Option
  Plan 2024, at an exercise price of Rs 3.8 each.
- 22,03,94,625 + 54,750 = 22,04,49,375 shares = Rs 2,204.49375 lakh, printed as
  2,204.49. The printed capital confirms the share count to the rupee.
- ESOP cash raised: 54,750 x Rs 3.8 = Rs 2,08,050, that is Rs 2.08 lakh. Of that
  Rs 0.5475 lakh is capital and Rs 1.53 lakh is securities premium. Not
  separately disclosed in the filing; stated here as arithmetic on the note.

Dilution from the allotment: 54,750 / 22,03,94,625 = 0.025 percent.

### E.2 Earnings per share, basic and diluted

| EPS (Rs) | Q ended 30-Jun-2026 | Q ended 31-Mar-2026 | Q ended 30-Jun-2025 | Year ended 31-Mar-2026 |
|---|---|---|---|---|
| Consolidated basic | 1.73 | 3.17 | 1.96 | 9.10 |
| Consolidated diluted | 1.73 | 3.17 | 1.96 | 9.10 |
| Standalone basic | (0.13) | (0.08) | 0.02 | 0.33 |
| Standalone diluted | (0.13) | (0.08) | 0.02 | 0.33 |

**Basic equals diluted in every column of both statements.** This repeats the
FY2026 Annual Report, where consolidated basic and diluted are both 9.10 (AR
extraction line 15571) and the two are equal.

Comment. An Employee Stock Option Plan 2024 is live, and page 4 note 6 records
an allotment under it during the quarter. The FY2026 Annual Report records the
plan as "exercisable into not more than 20,00,000 Shares of face value of Re. 1/-
each fully paid up" (AR extraction lines 22363 and 32929). Outstanding options
would normally produce a diluted share count above basic. The filing reports no
difference. The filing gives no weighted average share count, basic or diluted,
and no reconciliation between them. Stated, not interpreted.

Quarter-ended figures carry the label "Not annualised"; the year column carries
"Annualised".

For the EPS BASIS finding, which materially affects how consolidated EPS should
be read, see section A.2. On the owners' share alone, Q1FY27 consolidated basic
EPS would be Rs 1.68, not Rs 1.73.

### E.3 Tax

| Tax (Rs lakh) | Q ended 30-Jun-2026 | Q ended 31-Mar-2026 | Q ended 30-Jun-2025 | Year ended 31-Mar-2026 |
|---|---|---|---|---|
| **Consolidated** | | | | |
| Current tax | **882.83** CORRECTED (OCR "sa282") | 1,427.92 | 248.24 | 3,458.81 |
| Deferred tax | 64.68 | 207.81 | 644.96 | 997.55 |
| Earlier year tax {Short/(Excess)} | blank (nil) | 9.01 | blank (nil) | 9.01 |
| Total tax expense | 947.51 | 1,644.74 | 893.20 | 4,465.38 |
| **Standalone** | | | | |
| Current tax | "-" (nil) | (150.40) credit | 17.58 | 26.59 |
| Deferred tax | 36.56 | 64.98 | 7.20 | 190.31 |
| Earlier year tax {Short/(Excess)} | blank | blank | blank | blank |
| Total tax expense | 36.56 | (85.43) credit | 24.78 | 216.91 |

Arithmetic that fixes consolidated Q1FY27 current tax: total tax 947.51 minus
deferred tax 64.68 = 882.83. The OCR string "sa282" is consistent with a printed
"882.83" whose leading characters were misread. No earlier-year tax line is
filled in the Q1FY27 column.

Effective tax rate, consolidated Q1FY27: 947.51 / 4,749.97 = 19.95 percent.
Comparatives on the same arithmetic: Q4FY26 1,644.74 / 8,629.22 = 19.06 percent;
Q1FY26 893.20 / 5,205.18 = 17.16 percent; FY26 4,465.38 / 24,528.53 = 18.21
percent.

There is no earlier-year tax charge in Q1FY27. The Rs 9.01 lakh earlier-year tax
sits in the Q4FY26 quarter and in the FY26 year, the same amount in both, which
is internally consistent.

### E.4 Depreciation and amortisation

| Depreciation and amortisation (Rs lakh) | Q ended 30-Jun-2026 | Q ended 31-Mar-2026 | Q ended 30-Jun-2025 | Year ended 31-Mar-2026 |
|---|---|---|---|---|
| Consolidated | 1,692.35 | 1,495.78 | 278.56 | 3,579.79 |
| Standalone | 110.09 | 93.45 | 51.98 | 319.39 |

Quote, page 3, consolidated:
> "Depreciation and amortzation expense.   169235   149578   27856   357979"

Arithmetic support. The Q4FY26, Q1FY26 and FY26 consolidated depreciation
figures are confirmed inside columns whose expense lines sum to the printed
total. The FY26 figure 3,579.79 also matches the FY2026 ANNUAL REPORT
consolidated profit and loss. The Q1FY27 figure 1,692.35 is reported as read and
cannot be confirmed individually, for the reason in section 0.4.

Consistency check on the FY26 column: Q1FY26 278.56 + Q4FY26 1,495.78 =
1,774.34, leaving 1,805.45 for the two middle quarters of FY2026. That is a
plausible residual and contains no contradiction.

Comment. Consolidated depreciation at 1,692.35 in Q1FY27 is 6.07 times the
278.56 of Q1FY26 and 13.2 percent above the 1,495.78 of the preceding quarter.
No fixed asset note, no capitalisation date and no asset-class split is given.

---

## F. THE LIMITED REVIEW REPORTS

### F.1 The auditor

Quote, page 5 and page 9 letterhead:
> "ARS & CO."
> "Chartered Accountants"
> "F-101, 102, Sumer Complex, Gautam Marg, C-Scheme, Jaipur"
> "Phone: 9829791979 Email: arsandcompanyca@gmail.com"

Quote, page 6 and page 10 signature block:
> "For ARS & Company"
> "Chartered Accountants"
> "FRN: 009406C"
> "Avinash Khandelwal"
> "Partner"
> "M. No. 405344"
> "Date: 12th August 2026"
> "Place: Jaipur"

Comment. The letterhead says "ARS & CO." and the signature says "For ARS &
Company". Firm registration number 009406C. Signing partner Avinash Khandelwal,
membership number 405344. The partner name is spelled "Avinash Khandelwat" by
the OCR on page 6 and "Avinash Khandelwal" on page 10; the page 10 spelling is
taken as correct.

Both reports are dated 12-August-2026 at Jaipur, the same date as the board
meeting.

UDINs: **OCR UNRESOLVED, do not use.** Page 6 reads "UDIN: 264063Y44CD AROG
3BY)"; page 10 reads "UDIN: 2640 534U VR HOKN QUL". Both are alphanumeric and no
arithmetic test exists. A visual re-read of pages 6 and 10 is needed if the UDINs
must be verified on the ICAI portal.

### F.2 Consolidated limited review report, conclusion paragraph in full (page 6)

Title, page 5:
> "Independent Auditor's Review Report on the Quarterly Unaudited Consolidated
> Financial Results of Insolation Energy Limited Pursuant to Regulation 33 of the
> SEBI (Listing Obligations and Disclosure Requirements) Regulations, 2015, as
> amended."

Conclusion, page 6, quoted in full:
> "Conclusion
> Based on our review conducted and procedures performed as stated above, nothing
> has come to our attention that causes us to believe that the accompanying
> Statement of unaudited consolidated financial results has not been prepared in
> accordance with the recognition and measurement principles laid down in the
> aforesaid Ind AS and other accounting principles generally accepted in India and
> has not disclosed the information required to be disclosed in terms of Regulation
> 33 of the Listing Regulations, 2015 including the manner in which it is to be
> disclosed, or that it contains any material misstatement."

### F.3 Standalone limited review report, conclusion paragraph in full (page 10)

Title, page 9:
> "Independent Auditor's Review Report on the Quarterly Unaudited Standalone
> Financial Results of Insolation Energy Limited Pursuant to Regulation 33 of the
> SEBI (Listing Obligations and Disclosure Requirements) Regulations, 2015, as
> amended."

Conclusion, page 10, quoted in full:
> "Conclusion
> Based on our review conducted and procedures performed as stated above, nothing
> has come to our attention that causes us to believe that the accompanying
> Statement of unaudited standalone financial results has not been prepared in
> accordance with the recognition and measurement principles laid down in the
> aforesaid Ind AS and other accounting principles generally accepted in India and
> has not disclosed the information required to be disclosed in terms of Regulation
> 33 of the Listing Regulations, 2015 including the manner in which it is to be
> disclosed, or that it contains any material misstatement."

Comment. The two conclusions are word for word identical except for
"consolidated" against "standalone". Both are clean, unmodified conclusions.

### F.4 Qualification, emphasis of matter, other matter

**NONE IN EITHER REPORT.**

- Qualification paragraph: **NOT PRESENT** in either report.
- Emphasis of Matter paragraph: **NOT PRESENT** in either report.
- Other Matter paragraph: **NOT PRESENT** in either report.

Both reports run: Introduction, Scope of Review, (consolidated only: the list of
entities), Conclusion, signature. Nothing follows the Conclusion except the
signature block.

The scope paragraph, identical in both reports (pages 5 and 9), reads:
> "We conducted our review of the Statement in accordance with the Standard on
> Review Engagements ('SRE') 2410 "Review of Interim Financial Information
> Performed by the Independent Auditor of the Entity", issued by the Institute of
> Chartered Accountants of India ('ICAI'). This Standard requires that we plan and
> perform the review to obtain moderate assurance as to whether the Statement is
> free of material misstatement. A review of interim financial information consists
> of making inquiries, primarily of persons responsible for financial and
> accounting matters, and applying analytical and other review procedures. A review
> is substantially less in scope than an audit conducted in accordance with
> Standards on Auditing and consequently does not enable us to obtain assurance
> that we would become aware of all significant matters that might be identified in
> an audit. Accordingly, we do not express an audit opinion."

The consolidated report adds, page 6:
> "We also performed the procedures in accordance with the circulars issued by
> SEBI under Regulation 33(8) of the Listing Regulations, to the extent applicable."

### F.5 How many subsidiaries the review covered

Quote, page 6, in full as the table is printed:
> "The Statement includes the results of the following entities:
> Sr No | Name of the Entity | Relationship
> 1 | Insolation Energy Limited | Parent
> 2 | Insolation Green Energy Private Limited (Consolidated) and its subsidiaries | Wholly Owned Subsidiary
> 3 | Insolation Green Infra Private Limited (Consolidated) | Subsidiary and its associates
> 4 | MGVI Green Infra One Private Limited | Subsidiary
> 5 | MGVI Green Infra Two Private Limited | Subsidiary
> 6 | MGVI Green Infra Three Private Limited | Subsidiary
> 7 | MGVI Green Infra Four Private Limited | Subsidiary
> 8 | MGVI Green Infra Five Private Limited | Subsidiary"

Comment on the count. The table names **eight entities: the parent plus seven
subsidiaries.** Two of those seven are shown as consolidated sub-groups:
- Entry 2, Insolation Green Energy Private Limited, marked "(Consolidated) and
  its subsidiaries", a wholly owned subsidiary. The number and names of ITS
  subsidiaries are **NOT DISCLOSED** in this report.
- Entry 3, Insolation Green Infra Private Limited, marked "(Consolidated)",
  relationship "Subsidiary and its associates". The number and names of those
  associates are **NOT DISCLOSED** in this report.

So the ultimate entity count in the consolidation cannot be read off this
filing. Where it would be found if it exists: the FY2026 Annual Report note on
subsidiaries, associates and joint ventures, and Form AOC-1.

Note that the consolidated statement of profit and loss carries a line
"Share of (Loss)/Profit from associates, net of tax" (page 3, line 4) which is
BLANK in all four columns, while the review report names associates at entry 3.

### F.6 Component auditors: NOT STATED

**The reports do NOT say the work of other, component auditors was relied upon.**
Neither report contains an Other Matters paragraph. Neither report gives any of
the numbers that such a paragraph normally carries: the number of subsidiaries
reviewed by other auditors, their total assets, total revenue, net profit or net
cash flows, and the number of unreviewed components.

So the answer to "with the numbers the reports give" is: **NO SUCH NUMBERS ARE
GIVEN.** The reports are silent on which entities were reviewed by ARS & Co.
itself and which, if any, by anybody else.

Comment on a related fact, and it is stated only, not interpreted: the FY2026
ANNUAL REPORT consolidated audit report is signed by a DIFFERENT firm, BADAYA &
CO, Chartered Accountants, FRN 006395C (AR extraction lines 15584 to 15586 and
UDIN 26462343LKLRJG3681 at AR line 15482, dated 25.05.2026). The Q1FY27 limited
review is signed by ARS & Company, FRN 009406C. The filing carries no note
explaining a change of auditor and no Regulation 30 intimation of an auditor
change is enclosed. See section H item H7.

---

## G. THE ANNEXURES

There are TWO annexures, not one. The covering letter on pages 1 and 2 refers to
"Annexure - 1" and "Annexure - II". The OCR of the annexure headings reads
"Annexure -1" on page 11 and "Annexure - 1" on page 13; the page 13 heading is
the Annexure II referred to in the letter.

Both follow the SEBI Master Circular disclosure format, cited on both pages as:
> "SEBI Master Circular HO/49/14/14(7)2025-CFD-POD2/1/3762/2026 dated January 30, 2026"

### G.1 Annexure I, pages 11 to 12: Mr Manish Gupta

| Field | Detail as printed |
|---|---|
| Who | Mr Manish Gupta, DIN 02917023 |
| What role | Whole-Time Director, designated as Chairman of the Company |
| Reason for change | **Re-appointment**, not a new appointment |
| Effective date | 15-December-2026 |
| Term | Five years, 15-December-2026 to 14-December-2031 |
| Stated basis | Recommendation of the Nomination and Remuneration Committee, subject to approval of the members at the ensuing Annual General Meeting |
| Relationship with other directors | Spouse of Mrs Payal Gupta, DIN 09353350, Non-Executive Director of the Company |
| Debarment | Not debarred by any SEBI or other order |

Quote, page 11:
> "Re-appointment of Mr. Manish Gupta (DIN: 02917023) as Whole-Time Director,
> designated as Chairman of the Company, subject to approval of the members at the
> ensuing Annual General Meeting."

> "Date of re-appointment: 15" December, 2026. Term of re-appointment: Based on
> the recommendation of the Nomination and Remuneration Committee, re-appointment
> of Mr. Manish Gupta (DIN: 02917023) as Whole-Time Director, designated as
> chairman of the company for a period of five years w.e.f. 15" December, 2026 to
> 14" December, 2031, subject to the approval of the members of the Company in the
> ensuing Annual General Meeting."

Brief profile, pages 11 to 12, quoted:
> "A visionary first-generation entrepreneur, Mr. Manish Gupta brings over 25
> years of dynamic, multi-industry experience. As the driving force behind
> Insolation Energy Limited, he has established INA Solar as one of the top leading
> solar panel manufacturer, and a recognized leader in India's renewable energy
> sector. Under his leadership, INA Solar has set benchmarks in innovation,
> manufacturing, operations, and business outreach. His strategic foresight and
> relentless pursuit of excellence have garnered INA numerous prestigious awards and
> accolades on national and international platforms. Business Acumen Mr. Gupta
> excels in creating robust supply chain networks, building trusted customer
> relationships, and driving profitable business ventures. His "out-of-the-box"
> thinking and persuasive leadership have made INA a prominent player in the solar
> PV module manufacturing industry."

Quote, page 12:
> "Spouse of Director Mrs. Payal Gupta (DIN: 09353350), Non-Executive Director of
> the Company."
> "Mr. Manish Gupta is not debarred from holding office of a Director by virtue of
> any Securities and Exchange Board of India Order or any other such authority."

### G.2 Annexure II, pages 13 to 14: Mr Vikas Jain

| Field | Detail as printed |
|---|---|
| Who | Mr Vikas Jain, DIN 00812760, aged 49 |
| What role | Managing Director of the Company |
| Reason for change | **Re-appointment**, not a new appointment |
| Effective date | 15-December-2026 |
| Term | Five years, 15-December-2026 to 14-December-2031 |
| Stated basis | Recommendation of the Nomination and Remuneration Committee, subject to approval of the members at the ensuing Annual General Meeting |
| Relationship with other directors | Spouse of Mrs Ekta Jain, DIN 09409513, Non-Executive Director of the Company |
| Debarment | Not debarred by any SEBI or other order |

Quote, page 13:
> "Re-appointment of Mr. Vikas Jain (DIN: 00812760) as Managing Director of the
> Company, subject to approval of the members at the ensuing Annual General
> Meeting."

> "Date of re-appointment: 15" December, 2026. Term of re-appointment: Based on
> the recommendation of the Nomination and Remuneration Committee, re-appointment
> of Mr. Vikas Jain (DIN: 00812760) as Managing Director of the company for a
> period of five years w.e.f. 15" December, 2026 to 14" December, 2031, subject to
> the approval of the members of the Company in the ensuing Annual General Meeting."

Brief profile, pages 13 to 14, quoted:
> "Vikas Jain, aged 49 is a visionary technocrat and the Promoter & Managing
> Director of Insolation Energy Ltd. An engineering graduate from North Maharashtra
> University, Jalgaon, Mr. Jain brings over two decades of hands-on leadership
> across the energy and industrial sectors. From his early college days, he
> demonstrated a deep curiosity for technology, an instinct that later shaped his
> journey as a serial entrepreneur and angel investor. He has founded and scaled
> notable ventures such as Fluidcon Engineers and Pink City Pipe Fitting Pvt. Ltd.,
> establishing a track record of building resilient, tech-driven enterprises. As the
> driving force behind INA, he transformed it into Rajasthan's largest solar module
> manufacturer. His leadership is defined by a bold approach to restructuring, a
> strong belief in quality first systems, and relentless pursuit of innovation from
> integrating new-age solar tech to expanding manufacturing capacities."

Quote, page 14:
> "Spouse of Director Mrs. Ekta Jain (DIN: 09409513), Non-Executive Director of
> the Company."
> "Mr. Vikas Jain (DIN: 00812760) is not debarred from holding office of a
> Director by virtue of any Securities and Exchange Board of India Order or any
> other such authority."

### G.3 What the annexures do NOT disclose

- Proposed remuneration, fixed or variable, for either re-appointment:
  **NOT DISCLOSED**. The SEBI Master Circular format normally carries this.
- Shareholding of either director: **NOT DISCLOSED**
- Number of other directorships or committee memberships: **NOT DISCLOSED**
- Date of first appointment for either director: **NOT DISCLOSED**

Where these would be found if they exist: the AGM notice and the explanatory
statement under Section 102 of the Companies Act 2013 for the ensuing Annual
General Meeting; and the FY2026 Annual Report Corporate Governance Report and
the Directors' Report annexure on managerial remuneration.

### G.4 Other facts from the covering letter, pages 1 and 2

Quote, page 2:
> "The meeting of the Board of Directors of the Company commenced at 03:53 P. M.
> and concluded at 04:11 P.M."

Comment. An 18-minute board meeting.

Quote, page 2:
> "Nitesh Sharma"
> "Company Secretary & Compliance Officer"
> "ACS: 66702"

Digital signature timestamp, page 2 (readable only in the layout rendering):
> "NITESH SHARMA Date: 2026.08.12 16:37:33 +05'30'"

Comment. The filing was signed at 16:37 IST on 12-August-2026, 26 minutes after
the board meeting closed at 16:11.

---

## H. AGAINST THE FY2026 ANNUAL REPORT

Every item below gives both anchors. No interpretation is offered.

### H1. CONFIRMS. The entire FY2026 consolidated column reproduces exactly.

This filing, page 3, year ended 31-March-2026 column (Audited), against the
FY2026 ANNUAL REPORT consolidated statement of profit and loss (AR extraction
lines 15496 to 15566). Rs lakh.

| Line | Q1FY27 filing, page 3 | FY2026 Annual Report |
|---|---|---|
| Revenue from operations | 2,14,602.13 | 2,14,602.13 |
| Other income | 1,750.25 | 1,750.25 |
| Total Income | 2,16,352.38 | 2,16,352.38 |
| Cost of materials consumed | 1,66,212.64 | 1,66,212.64 |
| Purchases of Stock-in-Trade | 27,205.85 | 27,205.85 |
| Changes in inventories | (21,874.20) | (21,874.20) |
| Employee benefits expense | 5,053.82 | 5,053.82 |
| Finance costs | 2,354.09 | 2,354.09 |
| Depreciation and amortisation | 3,579.79 | 3,579.79 |
| Other expenses | 9,291.87 | 9,291.87 |
| Total Expenses | 1,91,823.85 | 1,91,823.85 |
| Profit before tax | 24,528.53 | 24,528.53 |
| Current tax | 3,458.81 | 3,458.81 |
| Deferred tax | 997.55 | 997.55 |
| Earlier year tax | 9.01 | 9.01 |
| Profit for the year | 20,063.15 | 20,063.15 |
| Total other comprehensive income | (16.01) | (16.01) |
| Total comprehensive income | 20,047.14 | 20,047.14 |
| TCI attributable to owners | 20,005.70 | 20,005.70 |
| TCI attributable to NCI | 41.44 | 41.44 |
| EPS basic and diluted | 9.10 / 9.10 | 9.10 / 9.10 |
| Other equity | 78,510.24 | 78,510.24 |
| Paid up share capital | 2,203.95 | 2,203.95 |

No restatement. No reclassification. The FY2026 audited consolidated numbers
stand unchanged in the Q1FY27 filing.

### H2. CONFIRMS. FY2026 standalone profit and loss also reproduces.

| Line | Q1FY27 filing, page 7 | FY2026 Annual Report |
|---|---|---|
| Revenue from operations | 9,802.52 | 9,802.52 (AR lines 3333, 27045) |
| Total Income | 10,560.24 | 10,560.24 (AR line 27052) |
| Changes in inventories | (555.30) CORRECTED by arithmetic | (555.30) (AR line 27078) |
| Total Expenses | 9,625.01 | 9,625.01 (AR line 27083) |
| Profit before tax | 935.23 | 935.23 (AR lines 3341, 27084, 27086) |
| Profit for the year | 718.33 | 718.33 (AR lines 3345, 27096, 27524) |

Comment. The Annual Report independently CONFIRMS my arithmetic correction of
the OCR-lost brackets on the FY26 standalone changes-in-inventories line.

### H3. A 0.01 DIFFERENCE. Standalone other equity at 31-March-2026.

- Q1FY27 filing, page 7, standalone line 9, year ended 31-March-2026 column:
  "41982.03", that is **Rs 41,982.03 lakh**.
- FY2026 Annual Report, standalone balance sheet and statement of changes in
  equity (AR extraction lines 26960 and 29379): **Rs 41,982.04 lakh**
  ("Total 41,364.97  41,982.04  3,030.48").

Difference: Rs 0.01 lakh, that is Rs 1,000. Both figures are stated side by
side. The filing figure is a single OCR cell with no arithmetic check available,
so the 0.01 may be an OCR artefact rather than a real difference. It is flagged,
not resolved.

Note by contrast that consolidated other equity agrees exactly: 78,510.24 in
both documents.

### H4. CONFIRMS AND UPDATES. Share capital and share count.

- FY2026 Annual Report, statement of changes in equity (AR line 16006):
  22,03,94,625 shares, Rs 2,203.95 lakh at 31-March-2026; 22,03,43,000 shares,
  Rs 2,203.43 lakh at 31-March-2025.
- Q1FY27 filing, pages 3 and 7: Rs 2,203.95 lakh at 31-March-2026 and Rs
  2,203.43 lakh at 30-June-2025. Both CONFIRM the Annual Report.
- Q1FY27 filing UPDATES both to Rs 2,204.49 lakh at 30-June-2026, that is
  22,04,49,375 shares, on the 54,750-share ESOP allotment of 25-May-2026
  (page 4 note 6, page 8 note 5).

### H5. CONTRADICTS ON FACE VALUE LABEL. Rs 10 against Re 1.

- FY2026 Annual Report, consolidated statement of profit and loss, EPS heading
  (AR extraction line 15568): "Equity shares of par value Rs 10/- each",
  above basic 9.10 and diluted 9.10.
- Q1FY27 filing, page 3 line 15 and page 7 line 10: "Earning per equity share
  (Face value of Rs. 1/- per share)", above basic 9.10 and diluted 9.10 for the
  SAME FY2026 year.

Both documents print the same EPS of 9.10 for FY2026 under two different stated
face values. The FY2026 Annual Report elsewhere records the sub-division
(AR extraction lines 22391 to 22392): "1 (one) equity share having face value of
Rs. 10.00 (Rupees Ten only) each, fully paid-up, was sub-divided into 10 (ten)
equity shares having face value of Rs. 1.00 (Rupee One only) each, fully
paid-up." Paid up capital of Rs 2,203.95 lakh on 22,03,94,625 shares is
arithmetically Re 1 per share. The two labels are stated side by side.

### H6. UPDATES. Segment declaration unchanged, still a single segment.

- Q1FY27 filing, page 4 note 5 and page 8 note 4: single segment under Ind AS
  108, covering "manufacturing of solar panel and sale of electricity and
  related project activities".
- FY2026 Annual Report describes a 4.5 GW solar cell manufacturing facility and
  an 18,000 MTPA aluminium frame project at Narmadapuram (AR extraction lines
  233 to 235, 632 to 633, 677, 737, 10021 to 10023), and lists INA-4 as the
  "Cell Factory" at Narmadapuram (AR lines 449 to 450, 1091 to 1092).
- The Q1FY27 filing carries NO segment split and no mention of the cell or
  frame projects beyond the factory address. The two are stated side by side.
  The filing neither confirms nor contradicts any commissioning status.

### H7. AUDITOR FIRM DIFFERS BETWEEN THE TWO DOCUMENTS.

- FY2026 Annual Report, consolidated audit report signature (AR extraction lines
  15584 to 15586): "For BADAYA & CO, Chartered Accountants, FRN: 006395C",
  dated 25.05.2026 at Jaipur, UDIN 26462343LKLRJG3681 (AR line 15482).
- Q1FY27 filing, pages 6 and 10: "For ARS & Company, Chartered Accountants,
  FRN: 009406C", partner Avinash Khandelwal, M. No. 405344, dated 12th August
  2026 at Jaipur.

Two different firms and two different firm registration numbers. The Q1FY27
filing contains no note about a change of auditor. Both anchors are stated; the
fact is not interpreted here.

### H8. INTERNAL INCONSISTENCIES INSIDE THE Q1FY27 FILING ITSELF.

Listed for completeness, both anchors within the one document:
- Page 3 column header says "(Unaudited)" for the quarter; page 4 note 2 says
  "The above audited consolidated financial results".
- Page 4 note 3 and page 8 note 2 both claim an "unmodified opinion" AND an
  "unmodified conclusion"; the reports at pages 5 to 6 and 9 to 10 give a
  conclusion only and expressly state "we do not express an audit opinion".
- Page 8 note 2 says "The above standalone financial results of the group".
- Page 7 line 7 is labelled "Total comprehensive income (5-6)" but is computed
  as 5 plus 6.
- Page 7 year-ended column carries no audit label, while page 3 year-ended
  column is labelled "(Audited)".
- Page 3 line 4, "Share of (Loss)/Profit from associates, net of tax", is blank
  in all four columns, while the review report on page 6 names entry 3 as
  "Subsidiary and its associates".

---

## VERIFICATION QUESTION

I quoted most heavily from
`runs/ina-2026-09-06/inputs/results/Q1FY27_Results_BoardOutcome_2026-08-12.pdf`,
the Regulation 30 board-outcome letter of Insolation Energy Limited dated
**12-August-2026**, covering the quarter ended 30-June-2026, and specifically
from its page 3 (consolidated statement) and page 7 (standalone statement).

**My question: on page 3 of that 12-August-2026 PDF, please read two cells
visually and confirm them, because the OCR text layer destroyed both and my
figures for them are derived by subtraction, not read.**
1. Line 2, "Cost of materials consumed", column "30th June 2026". I report
   **Rs 59,267.48 lakh**. The OCR string is "82739".
2. Line 1, "Other income", column "31st March 2026". I report
   **Rs (154.84) lakh**, a negative. The OCR string is "5480)".

If either differs, the Q1FY27 gross-margin bridge and the Q4FY26 revenue split
both change, and this extraction must be reissued.
