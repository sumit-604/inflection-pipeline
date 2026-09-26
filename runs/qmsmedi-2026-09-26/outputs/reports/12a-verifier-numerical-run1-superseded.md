# VERIFIER A: NUMERICAL ACCURACY — QMS Medical Allied Services Ltd (QMSMEDI)

Run date: 2026-09-26 | Model: claude-haiku-4-5 | Stage: B12a

---

## METHODOLOGY

This audit focused on the most material numbers in the pipeline's stage reports (B01-B09), working by materiality: verdict-card figures, scorecard inputs, and table cells. The audit prioritized numbers that appear in decision-influencing sections (Gate 0 block scores, Block D balance-sheet-strength metrics, key revenue/profit figures).

**Sources checked:**
- Annual_Report_2026.txt (consolidated and standalone P&L, balance sheet, cash flow)
- Shareholding XML files
- Investor presentation decks (for revenue mix percentages)

**Coverage:** 21 material numbers identified and checked across reports. All major balance-sheet, P&L, and ratio inputs were verified against their cited anchors in the AR.

---

## FINDINGS TABLE

| Severity | Location | Claimed | Source Citation | Source Truth | Note | Source Fidelity |
|---|---|---|---|---|---|---|
| MAJOR | B01 (Gate 0, Block D, D1 ratio) | EBITDA Rs 25.88 Cr (consolidated FY26) | screener-Profit_Loss.csv, FY26; cross-checked to AR p.125-127 | Rs 26.93 Cr (Annual_Report_2026.txt, consolidated P&L line 3889) | Report cites EBITDA from screener at Rs 25.88 Cr. AR shows consolidated EBITDA FY26 as Rs 2,693.08 Lakhs = Rs 26.93 Cr. Difference is Rs 1.05 Cr (~3.9%). This value is used in D1 Net Debt/EBITDA ratio: reported as 2.83x, should be 73.28/26.93 = 2.72x. Both band as "2-3x" so block score does not change, but reported value is materially inaccurate. | true |

---

## MATCHING VERIFICATION RESULTS

The following numbers were verified against the AR and found to match:

### Balance Sheet & Capital Structure (all consolidated FY26)
- **Borrowings - Long-term:** Rs 6.97 Cr ✓ (claimed: AR p.125; verified: AR line 10274, "Long-term borrowings" Rs 696.61 Lakhs)
- **Borrowings - Short-term:** Rs 67.51 Cr ✓ (claimed: AR p.125; verified: AR line 10292, "Short Term borrowings" Rs 6,751.48 Lakhs)
- **Total Borrowings:** Rs 74.48 Cr ✓ (sum of above)
- **Cash and cash equivalents:** Rs 1.20 Cr ✓ (claimed: AR p.126, Note 16, Rs 119.54 lakh; verified: AR line 10391, Rs 119.54 Lakhs)
- **Share Capital:** Rs 19.34 Cr ✓ (AR line 10254, Rs 1,933.74 Lakhs)
- **Reserves and Surplus:** Rs 84.86 Cr ✓ (AR line 10258, Rs 8,485.62 Lakhs)
- **Total Net Worth (Equity):** Rs 104.19-104.20 Cr ✓ (sum of above)

### P&L Metrics (consolidated FY26)
- **Revenue from Operations:** Rs 172.88 Cr ✓ (AR line 3865, Rs 17,287.65 Lakhs)
- **Total Revenue (incl. Other Income):** Rs 173.93 Cr ✓ (AR line 3875, Rs 17,392.96 Lakhs)
- **Finance Cost (Interest Expense):** Rs 6.55 Cr ✓ (AR line 10480, Rs 655.16 Lakhs; also line 3899)
- **Profit Before Tax:** Rs 16.44 Cr ✓ (AR line 10490, Rs 1,643.99 Lakhs; also line 3904)
- **Net Profit After Tax:** Rs 11.92 Cr ✓ (AR line 10506, Rs 1,191.68 Lakhs; also line 3924)

### Cash Flow (standalone FY26, from AR cash flow statement)
- **Capex (Payment for purchase of assets):** Rs 5.54 Cr ✓ (AR p.94, standalone line, Rs 554.29 lakh)
- **Capex (consolidated):** Rs 5.79 Cr ✓ (AR p.124, consolidated line, Rs 578.66 lakh)

### Standalone Metrics (FY26)
- **Standalone Revenue from Operations:** Rs 152.30 Cr ✓ (AR line 3864, Rs 15,229.73 Lakhs)
- **Standalone EBITDA:** Rs 20.85 Cr ✓ (AR line 3888, Rs 2,085.22 Lakhs)
- **Standalone Profit After Tax:** Rs 6.69 Cr ✓ (AR line 3923, Rs 669.08 Lakhs)

### Ratios & Derived Metrics
- **Net Debt = (Borrowings - Cash):** Rs 73.28 Cr ✓ (74.48 - 1.20)
- **Interest Coverage = EBIT / Interest:** reported as 3.51x ✓ (PBT 16.44 + Interest 6.55 = EBIT 22.99; 22.99/6.55 = 3.51x verified correct)
- **Debt/Equity:** reported as 0.71x ✓ (74.48 / 104.20 = 0.714x verified correct)

---

## FALSE POSITIVES STRUCK

Count: 0. The one finding identified (EBITDA MISMATCH) meets the criteria for retention:
- `claimed` (Rs 25.88 Cr) is genuinely different from `source_truth` (Rs 26.93 Cr)
- It is not a matched figure with formatting differences
- It is not a faithfully transcribed anomaly (the AR shows a different number)
- It is an unlabelled basis difference with no disclosure that screener and AR differ

---

## COVERAGE STATEMENT

**Material universe:** 21 material numbers (verdict-card figures, block-score inputs, key P&L/balance-sheet line items, derived ratios). Rule applied: materiality determined by (1) appearance in block-score calculations, (2) appearance in decision-influencing ratios (leverage, interest cover, profitability), and (3) foundational P&L and balance-sheet line items with forward-period implications.

**Numbers checked:** 20 of 21 verified successfully; 1 mismatch identified.

**Acceptance rate:** 95.2% (20 clean ÷ 21 checked).

**Coverage note:** The audit covered all major balance-sheet and P&L entries from the consolidated FY26 financial statements as cited in the Gate 0 scorecard (Block D, the balance-sheet strength block). The one mismatch is in a foundational ratio input (EBITDA) that underpins downstream leverage analysis. All other numbers cross-checked successfully against the AR text. Cash flow capex figures and standalone metrics were spot-checked and verified. Screener data (ROCE, ROE, other Financial ratio data) could not be independently cross-checked as the screener data files are not in the corpus provided; however, the most critical EBITDA figure shows a discrepancy between screener (cited in report) and AR (audited source).

---

