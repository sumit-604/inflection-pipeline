# Stage 2, Pass 1: Notes to Financial Statements (full extraction)
Company: Narmada Gelatines Ltd (SHAWGELTIN, BSE 526739). Run date 2026-11-12. Model claude-sonnet-5-5.
Source: NGL Annual Report FY2025-26, standalone notes PDF pp.53-80 (printed 50-77), consolidated notes PDF pp.89-115. Unit: Rs LAKH on the face of the document (AR p.53 header "All amounts in Indian rupee lakhs"). Nothing is converted. Anchor form: (Note N, AR FY26 PDF p.X / printed p.Y). Printed page = PDF page minus 3 throughout.
Ratings: GREEN clean, YELLOW watch, RED red flag. "Computed" means my arithmetic on figures printed in the notes; the inputs are anchored.

OCR control. The PDF is scanned. Four OCR faults were found and corrected against page images (PDF pp.51, 62, 69, 73, 74, 87):
- Note 10 FY25 work-in-progress: OCR read 177.61. Image and Note 29 read 1,477.61 (PDF p.62 / printed 59; p.69 / printed 66).
- FY25 taxes paid in the cash flow: OCR read 853.99. Image reads (553.99) (PDF p.51 / printed 48). 2,258.24 less 553.99 equals the printed CFO 1,704.25.
- P&L and OCI line: OCR read (82.46). The equity statement, Note 34 and the image read (52.46).
- Cash flow associate dividend: OCR read (80.15). Image reads (50.15).

Check of the four load-bearing facts touching the notes (company memory is weighed, not cited):
1. Related-party flows with Pioneer Jellice and the IGCL stake: confirmed and extended, see section 2 and 6.
2. Capex Rs 33 Cr and term loan Rs 25 Cr plan: NOT FOUND IN NOTES. The notes show term loan outstanding 728.65 lakh, CWIP 528.97 lakh, commitments 1,205.00 lakh, no commissioning date (section 7, 12).
3. Inventory 156 days: reproduced on a cost basis (section 5). Note 48 prints 72 days, which does not tie.
4. Dividend: Rs 10 paid (604.96 lakh), Rs 11 recommended (665.45 lakh). FY23 payout NOT FOUND IN DOCUMENT (this AR carries FY26 and FY25 only).

---
## 1. Accounting policies and changes (Note 2, PDF pp.53-60)
- No change in policy. "Accounting policies adopted ... are consistent with those followed in the previous year" (Note 2(i), PDF p.53 / printed 50). GREEN.
- New standards effective 1 April 2025 (Ind AS 1, 7, 12, 21 amendments): "no impact" stated (Note 2, PDF p.53). GREEN. No quantified P&L impact of any policy change.
- Depreciation: straight line, Schedule II lives. Company ranges: buildings 5-60 yrs (Sch II 3-60), plant 5-25 yrs (Sch II 5-30), electrical 10, furniture 10 (Sch II 8-10), office equipment 3-5, vehicles 8 (Sch II 6-10) (Note 2(iv), PDF p.54). Lives at or below Schedule II maxima except furniture and vehicles at the upper end of the range. No change in lives disclosed. GREEN.
- Capitalisation threshold: assets up to Rs 75,000 each are fully depreciated in the year of purchase (Note 2(iv), PDF p.54). GREEN (small).
- Borrowing cost: policy capitalises costs on qualifying assets (Note 2(xix), PDF p.60). Amount capitalised in FY26: NOT FOUND IN DOCUMENT. Finance costs 101.87 lakh are shown in full in the P&L (Note 31). With CWIP of 528.97 lakh and a term loan outstanding, the nil disclosure is a gap. YELLOW.
- Revenue recognition: control passes at dispatch or delivery, or when risk of loss transfers; net of discounts and volume rebates; MEIS and duty drawback recognised on sale or receipt (Note 2(vi), PDF pp.54-55). Standard for the industry, not aggressive. GREEN. Note 26 includes "liabilities no longer required written back" (1.18 lakh; FY25 10.93) inside revenue from operations, which is a classification nuance. YELLOW (small).
- Impairment: generic policy. Impairment test assumptions (growth, discount rate) for the Rs 4,115.31 lakh associate investment: NOT FOUND IN DOCUMENT (Note 2(xi), PDF p.56; Note 39).
- ECL: simplified approach with provision matrix on historical default rates (Note 2(xii), PDF p.57). Matrix percentages: NOT FOUND IN DOCUMENT. Allowance 2.81 lakh, unchanged for two years (Note 43, PDF p.76). See section 4.
- Leases: Note 2(xv) states "the contracts entered into by the Company do not contain a lease ... or they are either short term or low value leases" (PDF p.59 / printed 56). Yet Note 37 shows lease rent 11.60 lakh paid to Pioneer Jellice (new this year). ROU asset, lease liability, discount rate: NOT FOUND IN DOCUMENT. YELLOW (small amount, policy and RPT do not match).
- Derivatives and hedge: policy exists (Note 2(xii)); no derivative balance, no forward contract outstanding disclosed. Note 43 says the company "is not exposed to foreign currency risk at the reporting dates" (PDF p.77 / printed 74). GREEN.
- Segment: single segment, Ind AS 108 aggregation; CODM is the Managing Director (Note 2(xvi), Note 45, PDF pp.59, 78). Customer concentration and geography: NOT FOUND IN DOCUMENT.
- Material judgement language is generic ("estimates ... prudent and reasonable", Note 2(ii), PDF p.54). No critical-judgement list.

## 2. Related party transactions (Note 37, PDF pp.72-73 / printed 69-70)
Related parties named: Pioneer Jellice India Pvt Ltd and Ashok Matches and Timber Industries Pvt Ltd (both "Associate Co"; together 75.00% of equity, Note 17a(iii)-(v), PDF p.64 / printed 61), KMP (Ashok Kapur MD, Arun Jaiswal CFO, Mahima Patkar CS, two ex-KMP), five non-executive directors. India Gelatine and Chemicals Ltd (IGCL) is NOT in the list.

Table (Rs lakh; PDF p.73 / printed 70, image-verified):
| Party | Relationship | Nature | FY26 | FY25 | YoY |
|---|---|---|---|---|---|
| Pioneer Jellice India Pvt Ltd | 40.06% shareholder | Purchase of raw material (incl GST) | 1,481.92 | 1,524.64 | -2.8% |
| Pioneer Jellice | same | Technical consultancy service | 24.00 | nil | new |
| Pioneer Jellice | same | Lease rent | 11.60 | nil | new |
| Pioneer Jellice | same | Sales commission | nil | 6.72 | ended |
| Ashok K Kapur | MD | Remuneration | 99.16 | 66.26 | +49.7% |
| Arun Jaiswal | CFO (joined 15.03.2025) | Remuneration | 20.45 | 0.91 | n.m. |
| Mahima Patkar | CS (joined 07.08.2024) | Remuneration | 5.74 | 2.93 | +95.9% |
| Mahesh Verma | ex-CFO | Remuneration | nil | 16.46 | ceased |
| Meenu Sharma | ex-CS | Remuneration | nil | 0.56 | ceased |
| Five NEDs | directors | Sitting fees | 9.70 | 8.36 (sum of listed 1.60+1.00+2.20+1.40+2.20 = 8.40; Note 33 prints 8.66) | +15% |
Balances at year end: Pioneer Jellice trade payable 83.53 (FY25 99.21); MD remuneration payable 26.00 (nil); CFO 0.45; CS 0.45.

Computed:
- Pioneer Jellice total (purchases, consultancy, rent) 1,517.52 lakh = 7.04% of revenue 21,541.15; FY25 1,531.36 = 8.11% of 18,892.07.
- Pioneer Jellice raw material 1,481.92 is 12.7% of total raw-material purchases 11,669.25 (Note 28); FY25 13.7%. The numerator includes GST; the Note 28 basis is not stated, so the ratio is an upper bound.
- KMP remuneration 125.35 lakh vs 87.12 lakh (+43.9%); 3.3% of PBT. MD alone +49.7% against PBT +67.6% and revenue +14.0%.
- Statement "all related party transactions ... are on arm's length basis" (Note 37(ii)). No benchmark, no audit committee approval reference, no pricing method in the note. "Relationships identified by management and relied upon by the auditors" (Note 37(iv)). YELLOW.
- Dividend income from IGCL 50.15 lakh (Note 27) is not in the related-party transaction table. Directors Report states the promoter group's aggregate holding makes IGCL an associate (PDF p.6, outside the notes). By the company's own associate treatment, IGCL is a related party; the omission is an RPT disclosure gap. YELLOW.
- No loans to promoter entities, no royalty, no guarantees, no write-offs ("no amounts in respect of related parties have been written off", Note 37(i)). GREEN on those heads.
- New related-party lines this year: consultancy (24.00) and lease rent (11.60), both with Pioneer Jellice. Consolidated Note 37 shows the same table, but its "outstanding balance" block repeats KMP remuneration figures (99.16, 20.45...) instead of the payables 26.00 and 0.45 shown standalone (consol Note 37, PDF p.109 / printed 106). Presentation error. YELLOW (small).

## 3. Contingent liabilities (Note 36, PDF p.72 / printed 69, image-verified)
| Nature | FY26 | FY25 | Stage | Company view |
|---|---|---|---|---|
| Excise duty | 240.88 | 240.88 | NOT FOUND IN DOCUMENT | "does not reasonably expect ... material impact" |
| Sales tax | 3.76 | 3.76 | NOT FOUND | same |
| Land revenue cess | nil | 14.14 | removed, reason NOT FOUND | n/a |
| Total | 244.64 | 258.78 | | |
- 244.64 / net worth 14,130.66 = 1.73%. Largest item (excise 240.88) = 1.70% of net worth. None above 10%. GREEN.
- Income tax demand AY2013-14 of Rs 7.85 lakh is "not considered as contingent liabilities" because management calls it a mistake apparent from record; rectification or appeal pending (Note 36(ii)). GREEN (tiny).
- Guarantees for subsidiaries: no subsidiary; no guarantee disclosed. Capital commitments 1,205.00 contracted, 1,194.06 net of advances 10.94 (FY25 1,311.46 and 1,254.74) (Note 35). See section 12.

## 4. Trade receivables (Note 11, 43, PDF pp.62, 63, 76)
- Gross 2,905.54 (good 2,902.73 plus credit impaired 2.81); allowance 2.81; net 2,902.73 (FY25 2,484.20). +16.9% against revenue +14.0%.
- Ageing from due date (Note 11, PDF p.63 / printed 60): FY26 not due 2,514.65; under 6 months 359.45; 6 months to 1 year 28.63; over 1 year nil (only the 2.81 impaired item is 3+ years). FY25: not due 1,910.17; under 6 months 572.00; 6-12 months 2.03.
- Overdue share (computed): FY26 388.08 / 2,902.73 = 13.4%; FY25 574.03 / 2,484.20 = 23.1%. Improved. Over 6 months: 28.63 = 1.0% of total (FY25 0.1%). The 6-12 month bucket grew from 2.03 to 28.63 lakh; no explanation. YELLOW (small).
- Ageing from invoice date (Note 43, PDF p.76 / printed 73): 0-6 months 2,874.10; 6-9 months 28.63. Reconciles to Note 11 (2,514.65 + 359.45 = 2,874.10).
- Days (computed, closing receivables / revenue x 365): FY26 49.2; FY25 48.0. Note 48 prints 46 and 45 on average receivables (PDF p.79 / printed 76). Three-year trend: FY24 NOT FOUND IN DOCUMENT.
- Average credit period 30-120 days (Note 43). Single customer above 10%: NOT FOUND IN DOCUMENT. Note 43 says concentration is "low". Receivables from related parties: none disclosed.
- ECL: 2.81 lakh = 0.10% of receivables; opening equals closing, no addition, no write-off for two years (Note 43(b)). The matrix is not published. Token provision. YELLOW. Sundry balances written off rose to 46.44 lakh from 3.99 (Note 33, PDF p.69); their nature is NOT FOUND. They bypass the ECL allowance.
- Note 46: "Certain financial assets and financial liabilities are subject to formal confirmation and reconciliations" (PDF p.78 / printed 75). Which balances: NOT FOUND. YELLOW.

## 5. Inventory (Note 10, 29, 48, PDF pp.62, 69, 79)
| Category | FY26 | FY25 | Change |
|---|---|---|---|
| Raw materials | 1,265.65 | 856.24 | +47.8% |
| Work-in-progress | 1,589.97 | 1,477.61 (image-verified) | +7.6% |
| Finished goods | 1,619.81 | 1,895.74 | -14.6% |
| Stores and spares | 404.05 | 427.78 | -5.5% |
| Total | 4,879.49 | 4,657.37 | +4.8% |
- FG growth (-14.6%) against revenue growth (+14.0%): FG days on revenue 27.4 vs 36.6. Sales ran ahead of production from stock. GREEN.
- Raw material rose 409.41 lakh: 41.0 days of consumption vs 27.4 (computed on Note 28 consumption 11,259.84 and 11,407.13). YELLOW (seasonal or pre-buy not disclosed).
- Inventory days (computed, closing inventory / (cost of materials consumed + change in inventory) x 365): FY26 4,879.49 / 11,423.41 = 155.9; FY25 4,657.37 / 10,983.41 = 154.8. Reproduces the 156 in the Step-1 brief. On revenue: 82.7 vs 90.0.
- Note 48 prints inventory turnover 72 days (FY25 74) using "material and stores consumed / average inventory" (PDF p.79 / printed 76). On those inputs (11,374.20 / 4,768.43) turnover is 2.39 times, about 153 days. The printed 72 does not tie. Debtor and payable days in the same table do tie. YELLOW.
- Write-downs with amounts, obsolescence provision, NRV test results: NOT FOUND IN DOCUMENT. Policy says "adequate allowance" (Note 2(v)). Inventory is hypothecated for cash credit (Note 21).
- WIP is 32.6% of inventory (computed), 50.8 days of cost; no WIP process-time disclosure.

## 6. Investments (Note 6, 39, 42; consol Note 1, 6, 39; PDF pp.62, 74, 75, 89, 110)
- One investment: 1,003,000 equity shares of India Gelatine and Chemicals Ltd, face value Rs 10, carrying value 4,115.31 lakh both years (Note 39A, PDF p.74 / printed 71). Cost per share (computed) Rs 410.30. The column "fair value per unit 10.00" is the face value, so the heading misleads. Market value: NOT FOUND IN DOCUMENT.
- Ownership 14.14% (consol Note 1, PDF p.89; acquisition date 05-12-2024). Directors Report (PDF p.6): direct holding is below the Section 2(6) threshold; IGCL is an associate because the company and its promoters together hold above 20%. Standalone Note 39 does not state the percentage or this basis. The bought-alongside-promoter fact is therefore in the Directors Report, not in the notes.
- Standalone carries at cost, no remeasurement (Note 42: "not carried at fair value"). Consolidated carries 4,509.26 lakh (FY25 4,197.31) on the equity method: 4,115.31 + 82.00 + 354.93 - dividend 50.15 + share of OCI about 7.17 (computed; the OCI residual is my inference, not disclosed) (consol BS, PDF p.85).
- Share of IGCL profit: 354.93 lakh (14.14% x 2,510.17 = 354.93, exact). FY25 82.00 for the part year from 5 December 2024 (82.00 is 33% of 14.14% x 1,738.93).
- Dividend 50.15 lakh (Note 27) = Rs 5.00 per share (computed), 1.2% of cost; 14.1% of the profit share. Dividend recorded as income on standalone P&L, in other income, ahead of the cash.
- IGCL summarised financials (Note 39B, image-verified, PDF p.74): equity 19,356.48 (FY25 17,150.10); total income 17,819.38 (20,619.59, -13.6%); cost of materials 7,111.68 (9,128.21, -22.1%); PBT 3,261.39 (2,264.84, +44.0%); PAT 2,510.17 (1,738.93, +44.4%). IGCL PBT/total income 18.3% vs 11.0%. IGCL's margin step-up is of the same size and direction as NGL's (section 11), which is evidence that the margin move is not unique to the group's own books. The row "total comprehensive income 50.83 / 75.17" does not equal PAT 2,510.17 / 1,738.93 with nil OCI and is unexplained. YELLOW.
- Implied IGCL share count 7.09 million (1,003,000 / 14.14%), book value per share about Rs 273, trailing EPS about Rs 35.4, so cost is 1.50x book and 11.6x FY26 EPS. All three are computed from the 14.14% disclosure; share count is NOT FOUND in the notes.
- Impairment or fair-value test on 4,115.31 lakh (29.1% of standalone equity): NOT FOUND IN DOCUMENT. Note 48 shows "return on investment 0.00%, no investment made" (PDF p.79) while 4,115.31 lakh sits in investments. YELLOW.
- Standalone EPS 47.01 excludes IGCL profit; consolidated EPS 52.05 includes it (Note 38 standalone and consol).
- Loans and ICDs given: none beyond employee advances (Note 7: 20.58, Note 14: 46.36). Note 49(v) states no funds advanced to intermediaries. Loss-making subsidiaries: no subsidiary. Mutual fund gains: FY25 49.47 lakh, nil in FY26 (Note 27); FY25 purchase 4,115.31 and sale 960.48 of investments in cash flow.

## 7. Borrowings (Note 18, 21, 44, PDF pp.65, 66, 77-78; image-verified p.65)
| Instrument | FY26 | FY25 | Rate | Security / terms |
|---|---|---|---|---|
| Term loan (gross) | 728.65 | 798.08 | 7.95-8.20% (FY25 8.20%) | first ranking pari passu / exclusive charge on assets created from the loan; "60 equal monthly instalments" |
| of which current maturity | 320.56 | 195.00 | | |
| Non-current | 408.09 | 603.08 | | |
| Cash credit | 60.43 | 472.26 | 7.70-8.15% (FY25 8.15%) | exclusive charge on entire current assets; repayable on demand; 12 months |
| Bank overdraft | nil | 1.86 | | secured against a bank deposit |
| Gross debt | 789.08 | 1,272.20 | | Note 44(a) |
- Repayment schedule (Note 18): FY26 balance falls due 320.56 / 195.00 / 171.87 / 41.22 in years 1-4 (labelled "1-2 Years" onward, which is the next 12 months in effect). FY25: 195.00 x3, 171.86, 41.22. Five-year repayment visible; fixed or floating: NOT STATED in Note 18; Note 43 lists "long-term borrowings at variable rates" with "interest rate swaps" as the mitigant but no swap is disclosed.
- Implied FY26 drawdown (computed): gross term loan fell 69.43 against scheduled repayment 195.00, so about 125.57 lakh was drawn in the year. The cash flow shows only "repayment of long-term borrowings (195.00)" and "repayment of short-term borrowings (288.13)"; the drawdown is netted inside the short-term line (cash credit repaid 413.69 net). The financing section presents net movements, not gross proceeds. YELLOW.
- Opening FY25 borrowings were nil: FY25 financing shows 603.08 and 669.12 as inflows, equal to closing balances (PDF p.51). All debt of 1,272.20 lakh was first raised in FY25.
- Interest cost: interest expense on borrowings 80.00 (106.79), other borrowing costs 8.20 (15.26), interest on income tax 13.67 (nil) (Note 31, image-verified). The 13.67 lakh of interest on income tax signals late or short advance tax payment. YELLOW (small).
- Covenants, breaches, waivers, term changes: NOT FOUND IN DOCUMENT. Note 49(ix) and (xi): not a wilful defaulter; borrowings used for the purpose taken; Note 49(x) quarterly stock statements agree with books (PDF p.79-80).
- Related-party borrowings: none.
- Term loan sanction, planned Rs 25 Cr, drawdown schedule, link to the Rs 33 Cr project: NOT FOUND IN NOTES.
- Net debt 380.60 lakh, gearing 0.03 (FY25 0.09), Note 44(a) (PDF p.78 / printed 75). The consolidated capital table repeats standalone equity 14,130.66 instead of the consolidated 14,524.62 (consol Note 44, PDF p.114). YELLOW (small).
- Fixed deposits 373.49 lakh (FY25 4.06) are in "bank balances other than cash" (Note 13) and Note 44(b) lists "fixed deposits" with cash credit security. Whether they are lien-marked: NOT STATED.

## 8. Trade payables (Note 22, PDF p.67 / printed 64)
- Total 1,235.40 (FY25 1,718.71, -28.1%): MSME 477.18 (951.86, -49.9%), others 758.22 (766.85).
- Ageing: MSME all in "less than 1 year" 477.18, "not due" column blank; others 755.62 under 1 year, 0.64 in 1-2 years, 1.96 above 3 years. FY25: others 757.80 / 3.80 / 4.59 / 0.66.
- MSME disclosure: principal 477.18; "principal due and remaining unpaid" nil; interest due nil; payments beyond appointed day nil. Dues beyond 45 days: NOT FOUND (the ageing does not split by due date). The MSME classification is "based on information received ... relied upon by the auditors". GREEN with caveat.
- Payable days on purchases (computed): FY26 1,235.40 / 11,669.25 x 365 = 38.6; FY25 56.3. Note 48 prints 47 and 50 on average payables and cost of goods sold. The payables unwind of 483.31 lakh is the single largest working-capital outflow (cash flow, PDF p.51). YELLOW for cash, not for accounting.
- Pioneer Jellice payable 83.53 sits inside creditors other than MSME, 6.8% of that line (computed).
- Other financial liabilities (Note 23): advances from customers 247.55 (112.37, +120%), payable for capital expenditure 53.07 (nil), employees payable 12.11 (nil), unpaid dividend 23.67. No contract-liability note exists, so customer advances sit as a financial liability. YELLOW (small).

## 9. Provisions (Note 19, 25, 34, 47, PDF pp.66, 68, 70-72, 78)
- Provisions: gratuity non-current 56.89 plus current 85.97 = 142.86 (FY25 116.67); compensated absences 36.97 (1.41); pension non-current 25.86 plus current 4.80 = 30.66 (30.16).
- Gratuity (Note 34, PDF pp.70-71): PV of obligation 463.47 (419.43); plan assets 320.67 (302.76), LIC group scheme; net liability 142.80 (116.67); funded ratio 69.2% (72.2%). Plan asset total is 320.67 in 34A and 320.62 in 34B; opening obligation 419.43 vs 419.40. Rounding noise, 0.05 lakh. GREEN.
- Movement FY26: interest cost 27.98, interest income 20.15, current service cost 30.37 (Note 34C; the row is missing from the OCR movement table but 419.40 + 27.98 + 30.37 - 31.88 + 86.13 - 68.53 = 463.47 ties), actuarial gain on financial assumptions (31.88), experience loss 86.13, employer contribution 64.48 (23.65), benefits paid 68.53 (79.27).
- Experience adjustment 86.13 lakh is 20.5% of opening obligation (computed); FY25 44.36 on 383.53 = 11.6%. Two successive large experience losses, 130.49 lakh combined, taken to OCI. YELLOW.
- Assumptions: discount rate 7.67% (6.71%); salary escalation 8.00% both categories; attrition 1% management, 6% non-management; TALM 2012-14; retirement age 60; remaining working lives non-management 13 years (FY25 9). Sensitivity +/-1%: discount rate (29.51)/+34.13; salary +34.00/(29.90). OCI remeasurement (52.46) FY26, (66.19) FY25.
- Compensated absences: expense 45.56 (3.44), liability 36.97 (1.41) (Note 34(ii), PDF p.72). A 13-fold step-up. Note 47 says the Labour Codes (effective 21 November 2025) impact on employee benefit obligations was "accounted" but the amount is NOT FOUND IN DOCUMENT. Gratuity service cost also rose 20.92 to 30.37. The step-ups point to a catch-up inside FY26 employee cost. YELLOW.
- Pension: fixed Rs 565 a month after 25 years, or lump sum Rs 34,000; balance 30.66; expense 4.80.
- Warranty, decommissioning, onerous contracts: NOT FOUND IN DOCUMENT (none disclosed). Litigation provisions: "adequate provisions wherever required" with no amounts (Note 36(i)).

## 10. Deferred tax and income tax (Note 20, PDF p.66 / printed 63)
- Deferred tax liability net 508.17 (409.89); components: accelerated depreciation (534.08) against (418.60), expenses allowable on payment 25.91 against 8.72. P&L deferred tax 98.29 (FY25 credit (21.99)); movement ties to 115.48 less 17.19.
- Statutory rate 25.17%. Reconciliation: computed 961.25; differences (6.82), 12.62 ("deduction under chapter VI A"), 2.03; total 969.08 (Note 20(i)). The 12.62 is added, though a deduction normally lowers tax; sign convention unexplained. Effective rate 969.08 / 3,819.16 = 25.4%.
- The Note 20 total 969.08 excludes "tax adjustment for earlier years" 6.26 lakh shown in the P&L (current 870.79 + deferred 98.29 + 6.26 = 975.34; PBT 3,819.16 less 975.34 = PAT 2,843.82). Effective rate with it 25.5%. YELLOW (small, 6.26 lakh).
- MAT credit: none. Unrecognised DTA: none disclosed. DTA realism not at issue (net liability). Current tax liability net 60.85 (26.31).
- Interest on income tax 13.67 in finance costs (section 7).
- Consolidated reconciliation adds "tax effect of share of profit of associate (76.70)" (consol Note 20, PDF p.102). Tax on the associate share is not provided on the consolidated statement beyond that; there is no deferred tax on the undistributed IGCL profit disclosed. YELLOW (small).

## 11. Revenue details (Note 26, 27, 28-33, PDF pp.68-69)
Revenue from operations 21,541.15 (18,892.07), +14.0%:
| Line | FY26 | FY25 | YoY | % of revenue FY26 |
|---|---|---|---|---|
| Gelatine | 15,212.47 | 14,027.83 | +8.4% | 70.6% |
| DCP animal feed grade | 6,264.24 | 4,809.26 | +30.3% | 29.1% |
| Bone meal products | 21.16 | 24.94 | -15.2% | 0.1% |
| Scrap and coal ash | 27.93 | 12.22 | +128% | |
| Export incentives, drawback | 5.66 | 0.16 | | |
| Liabilities written back | 1.18 | 10.93 | | |
| Miscellaneous | 8.51 | 6.73 | | |
Sum ties to 21,541.15. DCP share of revenue 29.1% against 25.5% in FY25. Geography, volume and price split, top-customer revenue, contract assets, unsatisfied performance obligations: NOT FOUND IN DOCUMENT. Export sales are mentioned in policy but not sized.

Cost lines (Rs lakh, computed as % of revenue):
| Line | FY26 | FY25 | % rev FY26 | % rev FY25 | bp |
|---|---|---|---|---|---|
| Cost of materials consumed (Note 28) | 11,259.84 | 11,407.13 | 52.3% | 60.4% | |
| Change in FG and WIP (Note 29) | 163.57 | (423.72) | | | |
| Materials plus inventory change | 11,423.41 | 10,983.41 | 53.0% | 58.1% | -511 |
| Power and fuel (no note) | 2,333.26 | 2,455.65 | 10.8% | 13.0% | -217 |
| Employee benefits (Note 30) | 2,007.70 | 1,618.21 | 9.3% | 8.6% | +75 |
| Other expenses (Note 33) | 1,646.15 | 1,376.81 | 7.6% | 7.3% | +35 |
- Operating margin before other income, computed (PBT + finance + depreciation - other income): FY26 4,130.63 = 19.2%; FY25 2,457.99 = 13.0%. The four lines above explain the whole +617 bp move (511 + 217 - 75 - 35). Raw material consumed fell 147.29 lakh on 2,649.08 lakh more revenue. Notes do not say whether price, volume, yield or mix drove this; NOT FOUND IN DOCUMENT. Pioneer Jellice supplied 12.7% of purchases (section 2).
- Employee benefits: salaries and wages 1,147.35 (1,360.72, -15.7%); provident and other funds 145.10 (204.06); staff welfare 715.25 (53.43) (Note 30, image-verified PDF p.69). The sum is right (2,007.70); the sub-head swing of +661.82 in welfare against -273.33 in the other two is unexplained, and Note 50 says prior-year figures were regrouped. YELLOW.
- Other expenses: plant repairs 760.37 (+25.0%), freight 190.81 (+60.8%), sundry balances written off 46.44 (3.99), CSR 40.81 (34.11), audit fees 10.55 (6.17) with statutory audit 7.50 (4.00), miscellaneous 230.48 (222.85).
- Other income 77.51 (165.25): interest 20.30 (115.18) after deposits were run down in FY25; dividend from IGCL 50.15; no MF gains.

## 12. Other critical notes
- Exceptional items: none either year (P&L, policy Note 2(xx)). GREEN.
- Goodwill: none. Intangibles: only "under development" 24.50 lakh (Note 5), ageing under 1 year. GREEN.
- PPE (Note 3, PDF p.61): gross block 5,321.70 (4,225.18); additions 1,096.52 (82.74 buildings, 1,007.61 plant, 2.22 furniture, 3.95 office equipment... listed total ties); no deductions in FY26; accumulated depreciation 1,214.62; net 4,107.03 (3,297.67). Depreciation 287.11 vs 222.23 (+29.2%). Note 2 says assets hypothecated for the term loan.
- CWIP (Note 4): 528.97 (678.29), all under 1 year, none suspended; "no cost overrun / time delay in the project". The project is not named. Capital commitments 1,205.00; capital advances 10.94 (56.72). CWIP plus net commitments plus intangible = 1,747.53 lakh (computed) against a Rs 33 Cr project in the Step-1 brief; the notes do not size the project. YELLOW (cannot test).
- Capex in cash flow 971.71 equals PPE additions 1,096.52 + CWIP change (-149.32) + intangible 24.50 (computed); it does not adjust for capex creditors 53.07 (Note 23) or capital advances. Difference is small. GREEN.
- Foreign currency: no exposure at the reporting dates (Note 43). Forward contracts and derivatives outstanding: none disclosed. GREEN.
- Basic and diluted EPS: 47.01 (28.45), no dilutive instruments, shares 6,049,587 unchanged (Note 38, 17a). GREEN.
- Share capital: no issue, bonus or buyback in five years (Note 17a). ESOP: none. Authorised capital includes 1,000.00 lakh of 9% cumulative redeemable preference shares, none issued. Promoter holding 75.00% (PJIPL 40.06%, Ashok Matches 34.94%), unchanged.
- Dividend: paid 604.96 (Rs 10) in both years; Rs 11 (665.45) recommended after the year end, 23.4% of FY26 PAT (computed); unpaid dividend 23.67 (Note 23, 44(c)). Equity statement shows no direct debit to reserves other than dividend and OCI remeasurement. GREEN.
- CSR: required 40.48, spent 40.81 (FY25 34.11 and 34.11), no shortfall (Note 40). Consolidated Note 40 shows FY25 34.46 and 34.50 for the same parent. YELLOW (small, inconsistent comparatives). R&D: salaries 15.29 (13.46) (Note 41).
- Events after the balance sheet date: no separate note; only the recommended dividend (Note 44(c)). Going concern: no language in the notes. Capital risk: gearing 0.03.
- Note 47 Labour Codes: see section 9. Note 46 confirmations: see section 4.
- Note 48 ratios (PDF p.79 / printed 76): current ratio 3.59 (2.55); debt service coverage 7.71 (3.33); ROE 21.81% (15.07%); ROCE 22.58% (16.08%); net margin 13.15% (9.03%); debtor 46 days (45); payable 47 (50); return on investment 0.00% (5.15%). Inventory days 72 does not tie (section 5).
- Note 49 statutory items: no benami, struck-off company, crypto, layering or wilful-default issues (PDF pp.79-80).
- Cash flow oddities (PDF p.51 / printed 48): the operating adjustments deduct the OCI remeasurement loss (52.46; 66.19 in FY25) from PBT although it never touched PBT; the cash flow also lists "dividend income from an associate (50.15)" as an operating deduction and again as an investing receipt (correct). Working-capital outflow 846.85 (FY25 126.62): receivables (463.80), inventories (222.12), payables (483.31), offsets +79.94 provisions, +148.44 other liabilities. CFO/PAT 86.4% (99.0%). Free cash flow (CFO less capex) 1,483.96 lakh; after dividends 879.00 (computed). YELLOW for the payables unwind and netted borrowing presentation.

---
## PASS 1 SUMMARY: top 10 findings by investor importance
| # | Finding | Note anchor | Rating |
|---|---|---|---|
| 1 | IGCL: 14.14% stake at cost 4,115.31 lakh (29.1% of standalone equity), associate only via promoter aggregation, no impairment test, no market value, absent from RPT table; consolidated share of profit 354.93 lakh; dividend 50.15 lakh | Note 6, 27, 37, 39; consol Note 1 (PDF pp.62, 68, 73, 74, 89) | YELLOW |
| 2 | Pioneer Jellice flows: raw material 1,481.92 incl GST (12.7% of purchases), new consultancy 24.00 and lease 11.60; total 7.0% of revenue; arm's length asserted not evidenced; policy denies leases | Note 37, 2(xv) (PDF pp.73, 59) | YELLOW |
| 3 | Margin reset in note lines: materials plus inventory -511 bp, power and fuel -217 bp, employee +75 bp, other +35 bp; reason (price, yield, mix) not disclosed; IGCL margin moved the same way | Note 26-33, 39B (PDF pp.68, 69, 74) | YELLOW |
| 4 | Staff welfare 715.25 vs 53.43 while salaries fell 213.37; employee cost +24.1%; Labour Code impact unquantified; compensated absence 1.41 to 36.97 | Note 30, 34, 47 (PDF pp.69, 72, 78) | YELLOW |
| 5 | Inventory 4,879.49, 156 days on cost; raw material +47.8%, FG -14.6%; no write-down amounts; Note 48 prints 72 days | Note 10, 29, 48 (PDF pp.62, 69, 79) | YELLOW |
| 6 | Cash conversion CFO 2,455.67 vs PAT 2,843.82 (86% vs 99%); payables down 483.31 (MSME 951.86 to 477.18); FCF 1,483.96 | Cash flow, Note 22 (PDF pp.51, 67) | YELLOW |
| 7 | Borrowings 789.08 gross, net debt 380.60, gearing 0.03; implied term-loan draw about 125.57 hidden in net presentation; sanction, covenants and capex link NOT FOUND | Note 18, 21, 44 (PDF pp.65, 66, 78) | GREEN |
| 8 | Capex: CWIP 528.97, commitments 1,205.00, additions 1,096.52, no delay stated; project size NOT FOUND IN NOTES | Note 3, 4, 5, 35 (PDF pp.61, 62, 72) | GREEN |
| 9 | Gratuity net liability 142.80, funded 69%, experience losses 86.13 and 44.36 in two years | Note 34 (PDF pp.70-71) | YELLOW |
| 10 | Receivables 2,902.73 (+16.9%), overdue 13.4% (23.1%), ECL 2.81 static, Note 46 confirmations caveat; contingent liabilities 244.64 (1.7% of net worth) | Note 11, 36, 43, 46 (PDF pp.62-63, 72, 76, 78) | GREEN |

Items already queued for Pass 2 and Pass 3 (not findings yet): consolidated FY25 cash flow does not foot (CFO 1,607.85, investing (2,890.46), financing 543.01 sum to (739.60) against printed (642.71); standalone FY25 CFO 1,704.25 differs by 96.40); consolidated FY25 working-capital lines differ from standalone; Note 39B TCI row 50.83; Note 18 versus cash flow term-loan presentation; consolidated notes say "rounded to the nearest crore" while amounts are in lakh (consol Note 2, PDF p.89).

```yaml
stage: B02-notes-pass1
company: "SHAWGELTIN"
run_date: "2026-11-12"
status: complete
note: "Full YAML block is in outputs/blocks/B02-notes-pass1.yaml"
```
