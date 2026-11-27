# Stage 2 Notes, Pass 2 (what was missed): PREMEXPLN, FY2025-26
Run: premexpln-2026-11-15 | Model: claude-sonnet-5-5 | Source: Annual_Report_2026.txt (46th AR); comparatives cross-checked to Annual_Report_2025.txt

## Conventions
- Unit: INR lakhs ("L") as printed on the face (p.109-112 and every notes page). No conversion. Where B00 prints crore (the Rs 18.9 cr export order), the text says "cr" and I do not convert.
- Anchor form: (Note N, p.P, L). p. = the "[page N]" marker in the .txt (printed page = p. minus 3). Standalone anchors first; consolidated named when it differs.
- "Derived" = my arithmetic on anchored numbers. "[INFERENCE]" = reading, not a filed fact. Absent = "NOT FOUND IN DOCUMENT".
- B00 input_gaps (shareholding folder empty, screener sheets empty, no results PDFs, no rating PDF) are corpus gaps. None touches a filed, audited notes read.
- Pass 2 method: re-read Notes 1-46 standalone (p.113-153) and 3-46 consolidated (p.175-205) against the Pass 1 output, plus the face statements (p.109-112) for cross-references. Pass 1 items are not repeated.

## LOAD-BEARING FACTS: what Pass 2 adds
| B00 fact | What Pass 2 finds |
|---|---|
| 1 Guidance vs delivery | Not a notes topic. Notes carry no guidance, order book or segment split (Note 35 consolidated, p.199: single segment, geography only). NOT FOUND IN DOCUMENT. |
| 2 Cash conversion, other income | Adds findings N2, N3, N4, N6 (receivable roll-forward, supplier advances, customer advance mix, interest accrual). Operating cash flow (144.14) L stands (CFS, p.112). |
| 3 Control change, related parties | Adds N1: the AKS Family Trust holding equals the exact sum of the three promoter holdings, so the notes show an intra-promoter transfer. Date, consideration and the SPA remain NOT FOUND IN DOCUMENT (the 9 Jul 2026 SPA post-dates the 29 May 2026 approval, Note 1.3, p.113). |
| 4 Safety, licences, export cover | Note 45 (p.153) lists only the proposed dividend. The April 2026 licence refusal and the cancelled Rs 18.9 cr export order (B00) both fall inside the window 1 Apr to 29 May 2026. The notes disclose neither: NOT FOUND IN DOCUMENT. No Peddakandukur reference in any note. See N4 and N16. |

---
## PASS 2 NEW FINDINGS

### N1. AKS Family Trust holds exactly the sum of the three promoter holdings. 🟡
- Trust 2,22,21,735 shares = 1,31,00,915 (Dr. A.N. Gupta) + 58,37,335 (Dr. (Mrs.) Kailash Gupta) + 32,83,485 (A.N. Gupta HUF) (Note 14(iii),(iv), p.129; consolidated Note 12, p.181). Derived: 13,100,915 + 5,837,335 + 3,283,485 = 22,221,735, exact.
- FY26 dividend paid at Rs 0.50 per share equals each holder's full FY25 share count: 65.50 L, 29.19 L and 16.42 L (Note 38(f), p.150; derived 1,31,00,915 x 0.50 = 65.50). All three still held the full count on the dividend record date. The transfer to the trust therefore came after that record date and before 31 Mar 2026. The record date and transfer date: NOT FOUND IN DOCUMENT.
- Reading A: an inter-se family restructuring into one holding vehicle (the arithmetic supports this). Reading B: a step in a sale chain. The separating observation is the trust deed beneficiaries and the SPA seller name, neither in the notes. [INFERENCE] The B00 SPA stake (41.33%) equals this trust holding.
- Note 38(a)(d) (p.147) lists AKS Family Trust as a "significant interest entity" of KMP. No transaction with the trust is shown for FY26.

### N2. Receivables over one year old did not clear at all in FY26. 🔴
- Roll-forward on due-date buckets (Note 11(c),(d), p.127-128; checked against Annual_Report_2025.txt, same FY25 figures). FY25 1-2y 575.62 + 2-3y 123.87 + over 3y 187.87 = 887.36 L. FY26 2-3y 556.28 + over 3y 332.07 = 888.35 L (derived). The group aged more than one year grew by 0.99 L; nothing was collected net.
- The over-3-year bucket (332.07 L) exceeds the most it can hold from FY25 (123.87 + 187.87 = 311.74 L) by 20.33 L (derived). The 2-3 year bucket is 19.34 L below its feeder (575.62 L). The 20.33 L and 19.34 L nearly offset, so either 20 L was moved between buckets or the ageing basis is not stable. No note explains it.
- Bad debts written off in FY26: 30.13 L (Note 29, p.138). The FY25 ageing shows the write-off did not come out of the over-one-year balances on a net basis.
- ECL 905.47 L covers 76.3% of the over-one-year balance 1,186.73 L (derived) and 57.2% of the over-six-month balance (Pass 1). Every balance is classed "undisputed, considered good" and nothing is "credit impaired" (Note 11(b), p.127), while auditor confirmations went unanswered (Pass 1, KAM p.154).
- Feeds FLAG-CASH.

### N3. Advances to suppliers doubled, and the domestic part rose almost fivefold. 🟡
- Advances to suppliers 2,115.95 L vs 1,065.61 L (+98.6%) (Note 9(ii), p.126). Foreign-currency advances to suppliers are 921.69 L (FY25 819.15 L) (Note 32(B), p.142-143). Domestic remainder: 1,194.26 L vs 246.46 L (derived), 4.8 times.
- Total other current assets rose 859.50 L (3,495.14 vs 2,635.64); balances with government authorities fell 237.76 L (Note 9(ii)). Capital advances also rose 486.59 L (Pass 1 gave the levels).
- Provision for doubtful advances: charged 82.00 L in FY25, nil in FY26 (Note 29, p.138). The closing provision balance: NOT FOUND IN DOCUMENT. Supplier names and age of the advances: NOT FOUND IN DOCUMENT.
- Reading A: prepayment for FY27 raw material as the order book ramps. Reading B: cash parked with a supplier tied to the 3,417.80 L settlement (Pass 1 finding 1) or to a stuck supply. The separating observation is the FY27 raw material receipts against these advances; the notes do not show it.

### N4. Customer advances: domestic fell 35%, foreign rose 163%. The export cancellation is not in the notes. 🟡
- Advance from customers 6,622.26 L vs 7,242.69 L (Note 19, p.132). Foreign-currency part 2,546.28 L vs 967.39 L (Note 32(B), p.142-143). Derived domestic remainder 4,075.98 L vs 6,275.30 L (-35.0%); foreign +163.2%. The derivation assumes the foreign advances sit wholly in Note 19.
- Export revenue fell 34.1% to 5,168.78 L (Note 21, p.133) while foreign advances grew 2.6 times. B00 records a Rs 18.9 cr export order cancelled in April 2026 on licence refusal. Note 45 (p.153) has no such event and Note 34 (p.145) has no refund or claim item. Whether any of the 2,546.28 L relates to that order, and any refund obligation: NOT FOUND IN DOCUMENT.
- Revenue recognised from the opening contract liability, and the unwinding schedule: NOT FOUND IN DOCUMENT.

### N5. FX loss is realised, tied to a ~10.6% rupee fall, and the "natural hedge" is one-sided. 🟡
- Implied closing USD rate from the Note 32(B) tables: 2,804.73 L / 29,63,126 USD = about 94.65 (Mar-26); 9,791.93 L / 1,14,41,660 USD = about 85.58 (Mar-25) (p.142-143). Move +10.6% (derived). The filing prints a 2.5% sensitivity only.
- Cash flow statement removes only (21.51) L of "unrealised foreign exchange gain" (p.112). With the P&L net loss of 591.64 L (Note 29, p.138), the realised loss is about 613.15 L (derived). FY25: unrealised gain 157.44 L against a net P&L loss of 2.53 L, so realised loss about 159.97 L (derived). Pass 1 gave the loss and the net exposure; it did not say the loss was realised, in cash, on paying down USD payables.
- Foreign payables 2,804.73 L against foreign receivables 1,101.50 L = 2.5 times (FY25 9,791.93 vs 793.23 = 12.3 times, derived). The note says "natural hedging ... imports and exports being at similar levels" (p.142). The tables do not show similar levels in either year.
- Year-end net USD liability 17,99,419 USD at the observed 9.07 rupee move = about 163.2 L (derived), against the printed sensitivity of 42.65 L.
- Hedging policy, forward contracts, board limit: NOT FOUND IN DOCUMENT.

### N6. Loan from Premier Wire Products rose with no loan "accepted"; the cash flow shows all finance cost as paid. 🟡 low
- Balance 423.39 L vs 399.56 L (+23.83 L) (Note 38(f), p.149). Note 38(e) shows acceptance of unsecured loan nil and interest paid 26.48 L (p.148). Derived: 399.56 + 26.48 = 426.04 L, within 2.65 L of the closing balance.
- Cash flow statement finance costs paid (364.95) L equal the P&L charge to the lakh (p.112, p.110), with no accrual movement. Note 33(c) shows "interest accrued but unpaid" nil (p.144).
- [INFERENCE] The subsidiary's interest was added to the loan, not paid in cash. Amount small. The treatment contradicts the cash flow line. Interest treatment on this loan: NOT FOUND IN DOCUMENT.
- Consolidated frame: the subsidiary lends 423.39 L, which is 79.4% of its net assets of 532.94 L (derived; Note 41 consolidated, p.203), to the parent, while 20% minority holders sit in the lender.

### N7. Land at 2016 revalued deemed cost is 39% of PPE; the revaluation reserve is 19% of net worth. 🟡
- Freehold land 7,012.62 L carried at "deemed cost" fair value as at 1 Apr 2016 (Note 2.6, p.115; Note 3, p.123). That is 39.2% of net PPE 17,907.14 L (derived).
- Retained earnings include a land revaluation of 5,570.59 L at the Ind AS date, not available for dividend (Statement of Changes in Equity, nature of reserves (iv), p.111). That is 79.4% of land carrying value and 19.3% of net worth 28,903.17 L (derived).
- Investment property: carrying 8.02 L against a fair value 250.24 L from a valuation "as at April 1, 2016" by one valuer; management says "no significant change" with no fresh valuation (Note 5, p.124; consolidated Note 4(a), p.176). A ten-year-old Level 3 figure.
- Why it matters: the capital employed base for ROCE includes 5,570.59 L of 2016 revaluation. Land use (plant site vs surplus), any lease or sale plan: NOT FOUND IN DOCUMENT.

### N8. Ratio note: stated reason is false, and capital employed is defined two ways. 🟡
- Receivables turnover 8.49 vs 7.54: the note gives the reason "increase in Revenue" (Note 43, p.152). Revenue fell 6.97% (Note 21, p.132). The cause is the average balance: 5,536.57 L (FY25: average of 3,807.81 and 7,265.33) vs 4,576.19 L (FY26: average of 5,344.57 and 3,807.81) (derived). Closing net receivables rose 40.4% (derived). The same wrong reason repeats in the consolidated note (p.203).
- Current ratio 1.60 and net capital turnover 4.00 reproduce from the face only when the 683.59 L insurance receivable counts as a current asset (current assets 25,811.91 L, p.109; derived 25,811.91 / 16,093.65 = 1.60). Without it: 25,128.32 / 16,093.65 = 1.56 (derived). The balance sheet places the claim, pending since Q1 FY26, in current "other financial assets" (p.109) while Note 7(ii) sits under the non-current investments note (p.125). Fair value table (Note 31, p.141) and the pledged-asset table (Note 41, p.151) leave out the 683.59 L; they total 11,331.92 L for financial assets.
- ROCE: consolidated 8.35% (FY25 16.16%) reproduces only with deferred tax left out of capital employed: (6,569.16 + 338.47 - 4,214.24) / (29,042.78 + 3,233.32) = 8.34% (derived); FY25 (3,779.86 + 1,081.63 - 211.32) / (24,715.68 + 4,064.91) = 16.16% (derived) (Note 42, p.203). Standalone FY26 8.03% reproduces only with deferred tax included (Pass 1). The two notes use different definitions under one label, and both strip all other income from EBIT.

### N9. Tax detail Pass 1 skipped. 🟡 low
- Non-recurring tax credits in FY26: prior-period current tax adjustment (44.09) L and deferred tax remeasurement (69.29) L, together 113.38 L = 2.5% of PAT (derived) (Note 30, p.140). Effective rate before them: (1,460.66 + 113.38) / 6,043.17 = 26.0% (derived), against the printed 24.2%.
- Note 18 movement table (p.132) shows deferred tax in P&L (115.42) L and OCI nil. Note 30 and the P&L face show deferred tax (120.25) L plus an OCI tax charge of 4.83 L (p.110, p.140). The closing balance is right; the 4.83 L is allocated to the wrong row in Note 18. The consolidated Note 16 shows it correctly in OCI (p.184).
- "Effect of interest on income tax" 38.05 L (FY25 32.38 L) sits in the rate reconciliation (Note 30(b), p.140). Note 20 shows the interest liability flat at 8.85 L (p.132). The P&L line that carries interest on income tax: NOT FOUND IN DOCUMENT (Note 26 and Note 29 name no such item).

### N10. Other expense lines that moved without comment. 🟡 low
Standalone Note 29 (p.138), derived percentages:
| Line | FY26 L | FY25 L | Change |
|---|---|---|---|
| Sales commission | 348.04 | 526.68 | -33.9% |
| Other selling expenses | 327.76 | 611.11 | -46.4% |
| Packing materials | 484.55 | 731.49 | -33.8% |
| Rent | 3.17 | 32.14 | -90.1% |
| Carriage outward | 405.32 | 305.01 | +32.9% |
| Legal and professional | 226.49 | 174.33 | +29.9% |
| General expenses | 295.46 | 213.16 | +38.6% |
| Donations | 15.40 | 4.90 | +214% |
- Excluding FX, other expenses were 5,033.30 L vs 5,817.63 L (-13.5%); excluding also the FY25 one-offs (500.00 and 82.00 L), 5,033.30 vs 5,235.63 L (-3.9%) (derived).
- Sales commission fell 33.9%, close to the export revenue fall of 34.1% (Note 21). [INFERENCE] The commission follows exports. Not stated in the notes.
- Reasons for the legal and professional rise (accident, SPA, other): NOT FOUND IN DOCUMENT. The rent fall: NOT FOUND IN DOCUMENT.

### N11. Cash earns 3.3% while debt costs 8.5% to 10.6%. 🟢 / 🟡 low
- Interest income 221.51 L (Note 22, p.133) over the average of term deposits plus margin money, ((4,610.86 + 914.00) + (6,935.99 + 795.90 + 9.11)) / 2 = 6,632.93 L, gives 3.3% (derived; Note 12-13, p.128). Borrowings of 3,656.71 L carry 7% to 10.6% (Note 15, p.130).
- Reading A: cash built only near year end (the FY25 year-end balance coincided with 11,654.90 L of payables). Reading B: low-yield deposits held for lenders' margin and flexibility. The separating observation is the quarterly cash balance, which the notes do not give.

### N12. Net block written off exceeds the items the notes name. 🟡 low
- Net carrying amount derecognised in Note 3 (p.123): 1,391.14 L gross less 585.68 L depreciation = 805.46 L. Named items: accident 709.80 L (Note 7(ii), p.125), assets discarded 37.50 L (Note 29, p.138), sale 11.64 L (proceeds 10.50 L + loss 1.14 L; CFS p.112, Note 29). Total 758.94 L. Gap 46.52 L (derived). Possible scrap or salvage; not stated.
- CWIP additions 2,486.93 L and capitalisations of 132.43 L from CWIP (Note 3, p.123). CWIP at year end 2,639.23 L, of which under 1 year 2,557.87 L. Project names and completion dates: NOT FOUND IN DOCUMENT. B00 says Katepally recommissioning targeted for Sept-Nov 2026; the notes tie no CWIP to it.
- The 73.79 L gap between the insurance receivable (683.59 L) and the booked claim (609.80 L) (Pass 1) does not appear in other income. Other non-operating income excluding the discount is 41.63 L (3,459.43 - 3,417.80, Note 22, p.133). Where the 73.79 L was credited: NOT FOUND IN DOCUMENT.

### N13. Consolidation arithmetic in Note 41. 🟡 low
- NCI of 135.52 L is 25.4% of Premier Wire's net assets of 532.94 L, and NCI profit 0.21 L is 25% of its profit 0.84 L, while the holding is 80% (NCI 20% would be 106.59 L) (consolidated Note 41, p.203). Gap 28.93 L (derived).
- The net-asset column sums to 29,047.69 L (28,903.17 + 532.94 - 6.63 + 3.69 + 135.52 - 521.00; derived) against consolidated equity 29,042.78 L (Note 31, p.196). Difference 4.91 L, close to the 4.90 L JV cost.
- Joint venture Global Premier Limited: partner name, funding commitments and guarantees: NOT FOUND IN DOCUMENT (Note 37, p.147; Note 4(b), p.176).

### N14. Liquidity table and term loan terms. 🟡 low
- Note 32(C) puts all 1,316.00 L non-current debt in the 1-3 year bucket and none beyond 3 years (p.144). Note 15(b) lists an SBI loan of 16 quarterly instalments (p.130). If all 16 remain, four instalments (34.04 L, derived) fall after 3 years. Pass 1 already showed that current maturities (809.97 L) omit the SBI instalments. The note does not state instalments remaining.
- Note 32(C) text lists "loan from directors" as a liquidity source; director loans are nil (Note 38(f), p.149).

### N15. Restatement and comparative check (Note 46, p.153). 🟢
- Note 46 and CFS note 2 say FY25 figures were "regrouped /reclassified" with no amounts and no line named.
- I checked FY25 comparatives against Annual_Report_2025.txt on: revenue 41,745.23; other expenses 5,820.16; finance costs 1,109.55; PAT 2,855.26; tax 898.98; operating cash flow 11,861.66; operating profit before working capital 6,131.02; receivables 4,329.61 and ageing; payables 11,654.90 and ageing; borrowings 3,714.47; other financial liabilities 2,150.29; other current liabilities 7,313.24; other current assets 2,635.64; employee benefits payable 680.06; creditors for expenses 1,406.05; DTL on PPE 2,009.35; contingent liabilities 5,945.21; commitments 1,441.54. All agree. No restated amount found. Consolidated FY25 payables ageing shows 10,059.21 L in the under-1-year bucket against 10,056.11 L standalone (Note 34(c), p.198), which is the subsidiary's 3.10 L.

### N16. What the notes do not say after year end. 🟡
- Note 45 (p.153) and consolidated Note 44 (p.204) report only the proposed dividend of 268.81 L (Rs 0.50 per share). Board approval was 29 May 2026 (Note 1.3, p.113).
- Not disclosed: licence suspension or refusal in April 2026, the cancelled export order (B00, Rs 18.9 cr), Katepally recommissioning status, insurer settlement, any change in promoter holding after 31 Mar 2026. All NOT FOUND IN DOCUMENT in the notes.
- Going concern: Note 2.1(ii) states the going concern basis with no uncertainty on the parent (p.113). The only material uncertainty sits in the PELNEXT note (consolidated Note 43, p.204).

---
## Items re-read and found already covered in Pass 1 (no repeat)
Policies 2.1-2.24, PPE/intangibles roll, investments, receivable levels and days, inventory table, borrowings table and covenants, payables ageing and its non-roll, gratuity table and assumptions, DTL and 115BAA, revenue split, variable consideration, other income, exceptional item, insurance gap 73.79 L, FX levels, CSR, auditor fees, EPS, ratio-column mixing. Verified clean in this pass: expense lines sum to 36,485.46 L (p.110); employee benefits tie (provident fund 197.09 + gratuity net cost 142.01 = 339.10 L, Note 25, p.134-135); sitting fees by name sum to 11.98 L (Note 38, p.150); CSR carry-forward arithmetic (1.19 + 1.06 = 2.25 L, Note 29(b), p.139); current ratio, debt-equity, ROE, inventory and payables turnover reproduce (Note 43, p.152); consolidated current ratio 1.65 and net capital turnover 3.82 reproduce (p.203).

# PASS 2 NEW FINDINGS SUMMARY (new items only)
| # | Finding | Anchor | Rating |
|---|---|---|---|
| N2 | Over-one-year receivables 887.36 to 888.35 L: nothing collected net; over-3-year bucket exceeds its feeder by 20.33 L | Note 11(c),(d), p.127-128 | 🔴 |
| N1 | Trust holding equals the exact sum of three promoter holdings; transfer fell after the dividend record date | Note 14(iii),(iv), p.129; Note 38(f), p.150 | 🟡 |
| N3 | Advances to suppliers +98.6% to 2,115.95 L; domestic part 4.8 times | Note 9(ii), p.126; Note 32(B), p.142 | 🟡 |
| N4 | Domestic customer advances -35.0%, foreign +163.2%; April 2026 export cancellation absent from the notes | Note 19, p.132; Note 32(B); Note 45, p.153 | 🟡 |
| N5 | FX loss is realised (about 613.15 L), rupee moved 10.6%, payables 2.5 times receivables | CFS p.112; Note 29, p.138; Note 32(B), p.142-143 | 🟡 |
| N7 | Land 39.2% of PPE at 2016 deemed cost; revaluation 5,570.59 L = 19.3% of net worth | Note 2.6, p.115; Note 3, p.123; SOCE p.111 | 🟡 |
| N8 | Stated reason for receivables turnover is false; capital employed defined two ways; insurance receivable lifts current ratio to 1.60 | Note 43, p.152; consolidated Note 42, p.203 | 🟡 |
| N16 | Notes silent on post-year-end licence refusal, export cancellation, recommissioning | Note 45, p.153 | 🟡 |
| N6 | Subsidiary loan grows by accrued interest while the cash flow shows interest paid in cash | Note 38, p.148-149; CFS p.112 | 🟡 low |
| N9 | 113.38 L non-recurring tax credits; Note 18 mislabels 4.83 L; interest on income tax unlocated | Note 30, p.140; Note 18, p.132 | 🟡 low |
| N10 | Seven expense lines moved 30% to 90% with no comment | Note 29, p.138 | 🟡 low |
| N12 | Net block derecognised exceeds named items by 46.52 L; 73.79 L insurance gap unlocated | Note 3, p.123; Note 22, p.133 | 🟡 low |
| N13 | NCI at 25.4% against 20% holding; net-asset column off by 4.91 L; JV partner unnamed | Consolidated Note 41, p.203 | 🟡 low |
| N14 | Liquidity table omits any bucket past 3 years | Note 32(C), p.144 | 🟡 low |
| N11 | Cash yield 3.3% against 7% to 10.6% debt | Notes 12-13, 15, 22 | 🟢 / 🟡 low |
| N15 | No restated FY25 amounts found on 18 checked lines | Note 46, p.153 | 🟢 |

Pass 2 emits no YAML block. The B02-notes block comes from Pass 3.

---
ORCHESTRATOR CORRECTION 2026-11-15 (FLAG-DISAGREEMENT, B02 vs B03, settled at source: AR FY26 Note 11 ageing row 'Considered good 3,724.82 | 942.85 | 395.64 | 298.38 | 556.28 | 332.07 | 6,250.04', txt line 8311): receivables over ONE year at 31 Mar 2026 are 298.38 + 556.28 + 332.07 = 1,186.73 L, up from 887.36 L at 31 Mar 2025 (+33.7%). The 888.35 L figure is the over-TWO-year sum only. The 'nothing collected net' wording applies to the over-two-year balance against last year's over-one-year balance. All INR lakhs.
