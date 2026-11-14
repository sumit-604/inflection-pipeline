# Stage 2, Pass 2: what Pass 1 missed (Notes to Financial Statements)
Company: Narmada Gelatines Ltd (SHAWGELTIN). Run date 2026-11-12. Model claude-sonnet-5-5.
Unit: Rs LAKH, as printed. Nothing converted. Anchor form: (Note N, PDF p.X). Printed page = PDF page minus 3. "Computed" means my arithmetic on anchored inputs. "Inference" is labelled.
Image checks this pass: PDF p.87 (consolidated cash flow), p.69 (Notes 29-33), p.79 (Note 48). OCR faults found: Note 31 FY25 other borrowing costs OCR 18.26, image 15.26 (Pass 1 value stands); consolidated FY25 taxes paid OCR (653.99), image (553.99).
Pass 1 items not repeated. Scope: Notes 1-50 standalone, consolidated notes, with cross-reads to the face statements, auditor Other Matter, AOC-1 and the Directors Report where a note depends on them.

## A. Queued items from Pass 1, resolved or narrowed

### A1. Consolidated FY25 cash flow does not foot (YELLOW)
Image-verified (consol cash flow, PDF p.87 / printed 84).
- Printed FY25: CFO 1,607.85; investing (2,890.46); financing 543.01. Sum (739.60). Printed net change (642.71), which equals closing 19.03 less opening 661.74.
- CFO does foot inside itself: cash generated 2,161.84 less taxes paid (553.99) = 1,607.85. The OCR value (653.99) was wrong.
- Standalone FY25 foots: 1,704.25 - 2,890.46 + 543.51 = (642.70) (standalone cash flow, PDF p.51).
- The 96.89 gap is 96.40 in CFO (1,704.25 less 1,607.85) plus 0.50 in financing (consolidated dividend paid (605.46) vs standalone and equity statement (604.96), PDF p.88).
- Line-level bridge, standalone to consolidated, FY25 (computed): PBT +82.01 (2,360.97 vs 2,278.96, the associate share); operating adjustments -15.81 (90.09 vs 105.90: consolidated drops the OCI deduction +66.19 and subtracts the associate share -82.00); working capital -162.59, of which receivables -163.22 (361.41 vs 198.19), other current assets +0.61, provisions and other liabilities +0.02. Net -96.39.
- The 163.22 receivables gap equals the FY25 rise in raw material, finished goods and WIP exactly (4,229.59 less 4,066.37 from Note 28 and 29 opening stock, PDF pp.68-69). The inventory line is 6.94 in both statements. Why consolidated receivables absorb this amount is NOT FOUND. A company with no subsidiary should have identical working-capital lines.
- FY26 consolidated foots to rounding: 2,455.66 - 1,272.06 - 1,191.33 = (7.73) vs printed (7.72).
- FY26 consolidated receivables (470.99) vs standalone (463.80): the 7.19 difference equals the associate OCI share (A3). The consolidated receivables line absorbs a non-cash equity credit (inference from the equal amount).
- Standalone FY25 inventory line: Note 28 and 29 opening stocks (RM 1,116.74, FG 1,433.16, WIP 1,516.47 = 4,066.37) and FY25 closing stock (RM+FG+WIP 4,229.59) show a rise of 163.22 before stores. The cash flow prints an inventory increase of 6.94. That needs stores to have fallen 156.28 (FY24 stores 584.06 implied, closing 427.78). FY24 stores NOT FOUND (this AR carries two years).

### A2. Note 48 inventory days 72 (YELLOW, unchanged)
I tried closing and average inventory over materials plus stores consumed (156 and 153 days), over revenue (83 and 81 days), and raw material only (34 days). None gives 72 (FY25 74). Debtor and payable days do reproduce. The printed figure stays unexplained (Note 48, PDF p.79, image-verified).

### A3. Note 39B "total comprehensive income 50.83 / 75.17" decoded (YELLOW)
- The row sits under "Other comprehensive income: nil" and equals neither PAT nor PAT plus OCI (Note 39B, PDF p.74).
- IGCL equity roll, FY26 (computed): 17,150.10 + PAT 2,510.17 = 19,660.27. Printed closing equity 19,356.48. Movement of (303.79). An IGCL dividend of Rs 5.00 per share (our 50.15 on 1,003,000 shares) on about 7.09 million shares is about 354.6. The residual is about +50.9, which matches 50.83 within rounding of the 14.14% holding. So 50.83 is probably IGCL's OCI, not TCI. Inference, supported by two further facts.
- 14.14% x 50.83 = 7.19. Consolidated OCI (45.27) is standalone (52.46) plus 7.19 (consol P&L, PDF p.86; consol equity statement, PDF p.88: OCI reserve (116.59) vs standalone (123.78)).
- The auditor's Other Matter prints group share of "profit after tax and total comprehensive income" as 354.93 and 362.11 (auditor's report, PDF p.82). Difference 7.18. This is direct filed support.
- FY25: the row shows 75.17 but consolidated FY25 OCI is only the (66.19) and the FY25 carrying 4,197.31 = 4,115.31 + 82.00 with no OCI share (consol BS, PDF p.85). 14.14% of 75.17 would be 10.63. Whether it is pre-acquisition (stake bought 5 Dec 2024) is NOT FOUND.
- Consolidated OCI is labelled "Remeasurements of net defined benefit plans" though 7.19 of it is the associate's.
- Share of profit prints as 355.00 in Note 39B and 354.93 in the P&L (Note 39B, PDF p.74; consol P&L, PDF p.86).

### A4. Interest capitalisation (narrowed)
No capitalised amount is disclosed (NOT FOUND IN DOCUMENT). Evidence points to none: "Finance cost paid" equals the P&L finance cost in both years (101.87 and 122.05; standalone cash flow, PDF p.51), and interest expense on borrowings 80.00 is about 7.8% of average gross debt 1,030.64 (computed), in line with the 7.70-8.20% rates in Note 18 and 21. GREEN on this point; the disclosure gap stays.

### A5. Sundry balances written off 46.44 vs 3.99 (YELLOW)
Nature NOT FOUND. Cash-flow receivables outflow 463.80 less balance-sheet trade receivable change 418.53 (2,902.73 less 2,484.20) leaves 45.27 (computed). The write-off is 46.44, within 1.17. That fits write-offs of receivables or advances passing through the working-capital line. The same 45.27 equals consolidated OCI to the paisa, so the attribution is a coincidence risk. State it as a lead, not a finding of fact. The ECL allowance stayed at 2.81 (Note 43, PDF p.76).

## B. New findings by area

### B1. Related parties (Notes 33, 37, 2(xv); Directors Report; governance report)
1. Lease rent to Pioneer Jellice 11.60 is 97.6% of total rent expense 11.89 (Note 37, PDF p.73; Note 33, PDF p.69). FY25 rent 15.86 had no Pioneer lease, so the FY25 lessor is NOT FOUND. Note 2(xv) says contracts hold no lease or only short-term and low-value leases (PDF p.59). Security deposits fell 167.18 to 163.30 non-current but rose 4.48 to 12.02 current (Note 8, 15, PDF pp.62-63); no link to the lease is stated. YELLOW.
2. Directors Report says Form AOC-2 particulars "are set out in the Notes" (PDF p.8). Note 37 gives no tenure, no pricing method, no advance terms. The governance report says every related-party transaction has prior Audit Committee approval (PDF p.34); the note does not. YELLOW.
3. Commission to selling agents rose to 14.53 from 10.05 (Note 33, PDF p.69) while the Pioneer sales commission of 6.72 ended in FY26. Who the agents are is NOT FOUND. GREEN to watch.
4. Sitting fees FY25 sum to 8.40 in Note 37 (1.60+1.00+2.20+1.40+2.20) vs 8.66 in Note 33 (Pass 1 saw this). FY26 sums to 9.70 on both. Closed.

### B2. Associate (Notes 6, 39; AOC-1; consol BS)
1. Carrying vs share of IGCL net worth. AOC-1 prints net worth attributable 2,737.02 (= 14.14% x 19,356.48; AOC-1, PDF p.21). Standalone cost 4,115.31 exceeds it by 1,378.29. Consolidated carrying 4,509.26 exceeds it by 1,772.24, which is 43.1% of cost (computed). Under the equity method that premium sits inside the carrying amount with no separate test. Note 2(xi) and Note 39 give no test basis. Pass 1 had cost at 1.50x book; this adds the rupee premium and the consolidated figure. YELLOW.
2. Consolidated tax. Consolidated tax expense equals standalone (975.34) although PBT rises by 304.78 (354.93 less 50.15 eliminated dividend). Consolidated Note 20 shows "tax effect of share of profit of associate (76.70)" = 25.17% x 304.78, so the associate share is treated as tax-free. In FY25 the same effect (about 20.64) is hidden inside "Others (19.61)" (consol Note 20, PDF p.102). No deferred tax on undistributed associate profit is disclosed. YELLOW (small).
3. The associate is audited by another auditor; the group auditor relies "solely" on that report for 354.93 and 362.11 (PDF p.82). GREEN, but the whole associate evidence base is one step removed.
4. Note 42 lists the associate as a financial asset at amortised cost in the carrying-value table (PDF p.75). Ind AS 27 and 28 treat it as an investment in an associate. Classification slip, no number effect. GREEN.

### B3. Ratios (Note 48)
1. DSCR 7.71 reproduces only as consolidated PBT 4,123.93 + finance 101.87 + depreciation 287.11 = 4,512.91, over finance 101.87 + cash-flow repayments 195.00 + 288.13 = 585.00 (computed 7.71). Standalone PBT gives 7.19. The numerator includes 354.93 of non-cash associate profit, and the denominator uses the cash-flow "repayment" lines (the short-term line is a net movement, Pass 1 section 7). Debt-equity, ROE, net margin and debtor days reproduce on standalone figures. The FY25 DSCR 3.33 reproduces on standalone with 669.12 as principal (computed 3.32). Mixed bases across years and statements. YELLOW.
2. The variance column prints 100% for debt-equity (0.06 vs 0.11, actual -47%) and DSCR (7.71 vs 3.33, actual +132%) and no reason (PDF p.79). Current ratio 2.55 to 3.59 is explained as "Repayment of Debt"; current assets rose 956.83 (inventory +222.12, receivables +418.53, bank deposits +370.80) and current liabilities fell 588.98. YELLOW (small).
3. ROE 21.81% and ROCE 22.58% use PAT on average net worth that includes the 4,115.31 associate cost on standalone. Return on investment shows 0.00% with "No investment made", while the associate sits at 4,115.31 (Pass 1 saw this). Closed.

### B4. Cash flow mechanics (standalone, PDF p.51)
1. Bank deposits "placed" (370.80) equals the full change in Note 13 (397.16 less 26.36), which includes the 1.37 rise in the unpaid dividend account (22.30 to 23.67). The financing section also deducts "Unpaid dividend amount (1.37)". The statement still foots to cash, so another line absorbs 1.37. Small double count. YELLOW (small).
2. "Interest received 20.30" equals P&L interest income, but accrued interest on deposits rose 0.04 to 2.99 (Note 15, PDF p.63). Cash received would be about 17.35. Small.
3. Taxes paid (820.90) vs balance-sheet roll: net tax asset 23.21 (49.52 less 26.31) to net liability 42.25 (18.60 less 60.85); charge 870.79 + 6.26 = 877.05. Implied paid 811.59. Gap 9.31 (computed). The tax asset and liability lines carry no note number (balance sheet, PDF p.50). YELLOW (small).
4. FY25: Note 3 shows deductions of gross 68.23 and accumulated depreciation 54.84 (net 13.39); the cash flow deducts a 0.60 gain (PDF p.51). Implied sale proceeds 13.99 do not appear as a line in FY25 investing. May sit in the capex line. NOT FOUND.
5. Liabilities written back 8.23 in the cash flow = 1.18 (Note 26) + 7.06 (Note 27 "Miscellaneous income") = 8.24 (computed). So Note 27 miscellaneous income is wholly written-back liabilities (inference), shown in two different notes. GREEN (small).

### B5. Balance-sheet heads that appear or jump with no narrative
- Other payables 68.85 (nil), employees payable 12.11 (nil), payable for capital expenditure 53.07 (nil) (Notes 23, 24, PDF pp.67-68).
- Balances with government authorities 67.11 (1.62) (Note 16, PDF p.63); advances to suppliers 129.20 (223.22); other receivables 34.84 (62.92) (Note 15).
- Statutory dues payable 149.07 (271.20), down 122.13 (Note 24).
- Rates and taxes 21.86 (10.08) (Note 33).
- Total 282.62 across the three new liability lines (68.85 + 12.11 + 53.07 + 149.07 not netted; new heads alone 134.03). None has a stated nature. YELLOW.

### B6. Employee benefits (Note 34, PDF pp.70-71)
- Remaining working life for non-management moved 9 to 13 years with attrition unchanged at 6%, yet "gain/loss from change in demographic assumptions" is nil in both years. The "adjusted average future services" row is blank. The change is not visible in the actuarial split. YELLOW (small).
- Discount rate rose 96 bp (6.71% to 7.67%) and produced a financial-assumption gain of (31.88), roughly the +1% sensitivity of (29.51) scaled to 0.96 (computed 28.3). Without it the FY26 OCI loss would be 84.34 vs 52.46 (computed). The gratuity cost is therefore cushioned by the rate rise.
- Gratuity BS provisions 56.89 + 85.97 = 142.86 vs Note 34 liability 142.80 (0.06 difference). Rounding.
- Employee-benefit headings in the P&L: Note 34 shows gratuity 38.20 + compensated absences 45.56 + pension 4.80 inside employee cost. The Labour Code amount is NOT FOUND (Note 47).

### B7. Other expenses and disclosures
- R&D expense line 20.18 (13.95) in Note 33 vs Note 41 total 15.29 (13.46), "other expenses" nil. Gap 4.89 (FY25 0.49) (Note 33, 41, PDF pp.69, 74). YELLOW (small).
- Audit fee: statutory audit incl. limited reviews 7.50 vs 4.00 (+87.5%), tax audit 1.50 vs 1.00 (Note 33 sub-table, PDF p.70). GREEN.
- Legal and professional 56.07 (73.57), effluent 35.39 (29.76), ground water charges 27.51 (25.92). Routine.
- Policy details not in Pass 1: duty drawback recognised on receipt, claims and refunds recognised on certainty of receipt (Note 2(vi), PDF p.55), voluntary retirement cost charged when paid (Note 2(ix)). Conservative to neutral. GREEN.
- Statement-level cosmetics: equity statement says "Notes 3-52", cash flow "3-50", signed notes end at 50 (standalone PDF pp.51, 52, 80); consolidated says "3-49" yet has 48 notes with no "previous year regrouped" note (consol PDF p.87, p.114). Consolidated Note 44 says "requirement of financial covenants" and Note 2 cites the Ind AS 1 covenant amendment, but no covenant is disclosed (PDF pp.113, 53). Ossein is named as a product in Notes 1 and 45 but no ossein revenue line exists in Note 26, and DCP (29.1% of revenue) is not named in the segment note. GREEN to YELLOW.

### B8. Cross-read to the Directors Report (outside the notes, Directors Report PDF p.12 / printed 9)
- The report gives gelatine volume +16.17% and average selling price -5.20%; DCP volume +11.35% and price +17.17%.
- Implied revenue (computed): gelatine 1.1617 x 0.9480 = +10.1% vs Note 26 +8.4%; DCP 1.1135 x 1.1717 = +30.5% vs +30.3%. The gelatine gap is 1.7 points, about 240 lakh on FY25 revenue 14,027.83. Rebates, mix or grade may explain it. NOT FOUND in the notes.
- The report says materials consumed "increased by 1.29%, due to lower cost of raw material". Note 28 shows consumption fell 1.29% (11,259.84 vs 11,407.13, PDF p.68). Direction error in the report.
- Power and fuel fell 4.98% on the report and in the P&L (2,333.26 vs 2,455.65), "due to decrease in coal prices and consumption". This is the only stated driver of the 217 bp fuel move. Gelatine price down 5.2% while revenue per unit of raw material rose is consistent with a cheaper input mix. Not tested. YELLOW.

## C. Checked, no new finding
Notes 3, 4, 5 (PPE and CWIP roll, depreciation ties to P&L), 7, 8, 9, 12, 14, 17a, 17b (equity ties to 14,130.66), 19, 25 (pension 19.98 + 10.18 = 30.16), 26 (sums to 21,541.15), 27 (sums to 77.51), 28, 29, 32, 33 (both years sum to the printed total), 35, 36, 38, 40, 42 (financial asset totals tie to Notes 7, 8, 14, 15), 49, 50. Current ratio 3.59 reproduces from the balance sheet. Going concern: no language in the notes or in the Directors Report beyond "no orders impacting going concern" (PDF p.10).

## PASS 2 NEW FINDINGS SUMMARY (new items only)
| # | Finding | Anchor | Rating |
|---|---|---|---|
| 1 | Consolidated FY25 cash flow does not foot by 96.89 (96.40 CFO, 0.50 financing); gap is the consolidated receivables line (+163.22), equal to the FY25 rise in RM, FG, WIP | PDF p.87, 51, 88 | YELLOW |
| 2 | FY25 standalone inventory outflow 6.94 cannot be built from Notes 28-29 (RM+FG+WIP +163.22; stores would need to have fallen 156.28) | PDF pp.51, 68-69 | YELLOW |
| 3 | Note 39B "TCI 50.83" is IGCL OCI; consolidated OCI includes 7.19; auditor prints 362.11 vs 354.93; FY25 75.17 not reflected | PDF pp.74, 82, 86, 88 | YELLOW |
| 4 | Associate carrying exceeds share of net worth by 1,378.29 (cost) and 1,772.24 (consolidated, 43% of cost); no impairment test | AOC-1 PDF p.21; PDF pp.74, 85 | YELLOW |
| 5 | Consolidated tax equals standalone; associate share treated tax-free (76.70 in FY26, hidden in "Others" in FY25) | consol Note 20, PDF p.102 | YELLOW |
| 6 | Pioneer Jellice lease 11.60 = 97.6% of rent expense 11.89; FY25 lessor NOT FOUND; AOC-2 reference empty | PDF pp.69, 73, 59, 8, 34 | YELLOW |
| 7 | DSCR 7.71 only reproduces on consolidated PBT and cash-flow repayments (standalone 7.19); variance column 100% wrong | Note 48, PDF p.79 | YELLOW |
| 8 | Sundry balances written off 46.44 vs receivables outflow gap 45.27 (lead only; 45.27 also equals consol OCI) | PDF pp.69, 51, 62 | YELLOW |
| 9 | New unexplained heads: other payables 68.85, gov authority balances 67.11, capex payable 53.07, employees payable 12.11; statutory dues -122.13 | PDF pp.63, 67-68 | YELLOW |
| 10 | Gratuity: working life 9 to 13 years with nil demographic effect; 96 bp discount-rate gain 31.88 cushions OCI | Note 34, PDF pp.70-71 | YELLOW |
| 11 | R&D 20.18 in Note 33 vs 15.29 in Note 41 | PDF pp.69, 74 | YELLOW |
| 12 | Cash flow small items: unpaid dividend 1.37 counted in investing and financing; interest received overstated about 2.95; taxes paid vs balance-sheet roll 9.31 | PDF pp.51, 63 | YELLOW |
| 13 | Directors Report price and volume split: gelatine implied +10.1% vs +8.4% booked; direction of materials change misstated | Directors Report PDF p.12; PDF p.68 | YELLOW |
| 14 | Associate audited by other auditor; classified as financial asset in Note 42 | PDF pp.82, 75 | GREEN |
| 15 | Cosmetic: note-count labels 3-49, 3-50, 3-52; "financial covenants" mentioned with none disclosed; Ossein and DCP naming in segment note | PDF pp.51, 52, 77, 87, 113 | GREEN |

No RED items. Passes 3 should test: the consolidated FY25 restatement (A1), the Note 39B decode (A3) against the CARO and the associate's own filings (live-web, not in corpus), and the mix of bases in Note 48.

```yaml
stage: B02-notes-pass2
company: "SHAWGELTIN"
run_date: "2026-11-12"
status: complete
note: "Full YAML block is in outputs/blocks/B02-notes-pass2.yaml"
pass_2_empty: false
new_findings_count: 15
```

---
ERRATA (recorded by the orchestrator from the stage's own hand-back, 2026-11-12; the stage had no edit tool):
- Section B5, line 70: "Total 282.62" should read 134.03 for the three heads nil in FY25 (68.85 + 12.11 + 53.07).
- Section C: the going-concern cross-reference "PDF p.10" should read PDF p.9.
- Line 113: "Passes 3" should read "Pass 3".
None of these changes a finding.
