# Stage 3: Annual Report Deep Dive, backward read. DEEDEV, run 2026-11-15

Source: FY2025-26 annual report (Annual_Report_2026.txt, [page N] markers = PDF page; printed page = PDF page minus 20 in the financial section). Anchors read "p.N" = PDF page. Units: INR lacs as printed in the financial statements and notes; MD&A and Chairman's letter print Rs crore, and the unit is kept in each anchor. "Derived" = my arithmetic on anchored inputs. Nothing is converted silently. Auditor for both reports: S.R. Batliboi & Co. LLP, signed 21 May 2026. Directors' report dated 21 Aug 2026 (p.61).

## 0. LOAD-BEARING FACTS, checked first

| # | Fact (companies/DEEDEV.md) | What the AR page shows | Status |
|---|---|---|---|
| 1 | Guidance vs delivery | AR guides FY27 order inflow above Rs 2,000 cr, core revenue Rs 1,400-1,500 cr, core EBITDA margin 18-20%, Vision 2030 revenue above Rs 2,500 cr (MD&A Outlook p.101). The Rs 1,500 cr plus and above 19% wording is from the Q1 FY27 call, not the AR. Q2 FY27 results (p.4, INR lacs): H1 revenue 58,744.90 (Q1 29,446.22, Q2 29,298.68), PBT 4,991.76. Q2 is below Q1, confirmed. H1 FY26 was 49,375.82, so H1 growth is 19.0% (derived) against FY26 full-year growth of 38.0% (Cons. P&L p.263). | CONFIRMED. Full test in Phase 4C. |
| 2 | Cash conversion | FY26 consolidated operating cash flow +1,954.84 on PBT 9,624.89 (Cons. CF p.264). Standalone -4,450.03 (CF p.160). H1 FY27 consolidated operating cash flow -679.09 on PBT 4,991.76 (Q2 FY27 results p.7), standalone H1 -4,345.30 (p.9). Operating cycle is not stated in the AR. Derived on revenue basis, FY26 consolidated: inventory 184 days, debtors 122 days, creditors 31 days (52 with trade credits): cycle 254 to 275 days. The 261 days in the brief is a CARE figure, not an AR figure. | CONFIRMED, brief figures match the filings (-679.09 lacs = -Rs 6.79 cr). |
| 3 | Abohar and MPPL | Abohar: payable 1,384.96 at Rs 5.88/unit unprovided, High Court stay 23 Sep 2025, auditor EoM on both reports (Note 46 p.251; Auditor p.146, p.253). MPPL: assets 4,761.67 not impairment-tested, QUALIFIED consolidated opinion (Auditor p.253; Cons. Note 45(b) p.351). Subsidiary loans 4,181.51 = Thailand 3,630.51 + Fabricom 400.00 + MPPL 151.00 (Directors' report s.186 table p.47; CARO iii p.152). Guarantees outstanding 668.89 (MPPL 527.04, Fabricom 141.85, Thailand 0) (p.47; Note 32C p.230). | CONFIRMED. The brief's Rs 9.76 cr guarantee figure does not match the AR: AR says 668.89 lacs = Rs 6.69 cr (Note 32C p.230), and CARO says 4,885.22 (p.152). Both are shown in Phase 1D. |
| 4 | Concentration | Standalone customers over 10%: Numaligarh Refinery 17,268.79 (18.80%), Dow Chemical Canada ULC 11,048.38 (12.03%) (Note 33c p.234). Gail 4.79% (FY25 10.24%), John Zink 0.61% (FY25 10.10%). Eight customers hold just over 71% of receivables (FY25 33%) (Note 36 p.241). Top-10 about 80% of operating income is NOT FOUND in the AR. BHEL and L&T are named as customers (MD&A p.99) but no split is given. | PARTLY CONFIRMED. The two over-10% names and the 71% are in the AR. The top-10 80% figure is not. |

Regulatory check: no SEBI order or penalty is referenced. CG Report 10.2 (p.76) states no SEBI or stock exchange monetary penalty in FY26 and no capital-markets non-compliance in three years, but it lists three events: Haryana Pollution Control Board environmental compensation of Rs 4,40,000 on 29 Aug 2025 (paid, STP upgraded); a Structured Digital Database notice (responded, no penal action); an NSE notice on IPO proceeds utilisation (responded, matter closed without adverse action). Prospectus litigation summary (Summary of outstanding litigation, PDF p.~17) shows "Disciplinary actions by the SEBI or Stock Exchanges against our Promoters: Nil". Stage-0 grep result is confirmed, with the NSE and SDD notices added.

## PHASE 1: AUDITOR'S REPORT AND CARO

**1A Core opinion**

| Item | Standalone | Consolidated |
|---|---|---|
| Opinion | Unmodified, true and fair view (p.146) | QUALIFIED ("except for the possible effects") (p.253) |
| Basis | Standard (p.146) | Assets of Rs 4,761.67 lacs of Malwa Power Private Ltd, wholly owned. PPA expired 27 Apr 2025. "management is unable to make impairment assessment... we are unable to comment on the impairment and possible consequential effects" (p.253) |
| Emphasis of Matter | Note 46, PSPCL appeal at APTEL and writ petition in the Punjab and Haryana High Court on retrospective downward tariff revision effective 1 Jan 2024. "no adjustments have been made". Opinion not modified (p.146) | Same, to Note 45(a) (p.253) |
| Going concern | No material-uncertainty paragraph. Basis stated Note 2.1 (B02, p.164). Auditor's standard responsibility text only (p.148). CARO xix: nothing to suggest the company cannot meet liabilities falling due in one year, with the "not an assurance" disclaimer (p.155) | No material-uncertainty paragraph (p.253-261). MPPL viability: "adversely impacted the operational viability of MPPL and created uncertainty over its future cash flows" (Cons. Note 45(b) p.351) |
| Section 143(3)(e) | EoM "may have an adverse effect on the functioning of the Company" (p.149) | Qualification and EoM "may have an adverse effect on the functioning of the Company" (p.256) |
| Other information | Nothing to report (p.147) | Auditor cannot conclude whether Other Information is misstated on the MPPL matter (p.254) |

Going concern: no GC doubt language in either report (OR-19 overlay does not fire on the AR text). The 143(3)(e) adverse-effect wording is on both reports.

**1B Key audit matters**

| KAM | Why key | How addressed | Risk |
|---|---|---|---|
| Standalone: Impairment of investments in and loans to subsidiaries. Carrying 18,784.88 lacs (p.147) | Management judgement on discount rates, forecasts | Read valuation report, used own valuation experts, tested key assumptions (p.147) | 🔴 |
| Consolidated: none other than the qualification (p.253) | n/a | n/a | 🔴 |

Arithmetic: 18,784.88 = investments 11,708.61 + loans 4,181.51 + interest receivable 2,894.76 (BS p.158; Note 31C) (derived, ties to the lacs). Contradiction at the point it appears: the standalone auditor accepts a management valuation report for the same group (including the MPPL investment 959.01 and loan 151.00), while the consolidated auditor says management cannot assess MPPL. The two reports are signed the same day by the same partner (p.151, p.258). No KAM on revenue recognition, receivables or inventory despite receivables +68.9% and nil ECL.

**1C Other matters**: 5 subsidiaries audited by other auditors, total assets 27,561.20, revenues 23,478.78, net cash inflows 2,301.21 (Cons. Auditor Other Matter p.255). Thailand material subsidiary auditor appointed 9 May 2026 for FY26 (CG p.77), after year end. IFC opinion unmodified for both (p.157, p.261).

**1D CARO 2020**

| Clause | Finding | Anchor |
|---|---|---|
| i(c) | Title deeds not in company custody: pledged with banks, confirmed by banks | p.151 |
| ii(a) | Inventory verified, third-party stocks confirmed, no 10% discrepancy | p.151 |
| ii(b) QUALIFIED REMARK | Quarterly bank returns do not agree with books. Inventory gaps: Jun-25 13.26, Sep-25 (1.84), Dec-25 440.57, Mar-26 519.91. Receivables gaps: Jun-25 2.05, Sep-25 (517.87), Dec-25 298.06, Mar-26 1,303.20 (lacs). Listed as adverse for the holding company and for MPPL (p.259). Recurring: same remark in FY2022 and FY2023 CARO, explained then as returns prepared two to three days before quarter end (Prospectus risk factor 26, PDF p.59-60) | p.151; p.259 |
| iii | Loans to subsidiaries: granted in year 691.00, outstanding 4,181.51; guarantees granted 4,216.33, outstanding stated 4,885.22 (p.152). CONFLICT: Note 32C states guarantees 668.89 (p.230) and Directors' report s.186 table totals 668.89 (p.47). 668.89 + 4,216.33 = 4,885.22 exactly (derived), so CARO appears to add the year's grant to the balance. RPT table shows MPPL guarantee given 2,300.00 (Note 31B p.223). Three guarantee figures for one year cannot be reconciled from the filing. CARO iii(c): repayment and interest receipts "regular", yet Thailand interest receivable is 2,894.76 and cash interest is NOT FOUND | p.152 |
| vii(a) QUALIFIED REMARK | Undisputed statutory dues "slight delay in a few cases"; none over six months outstanding (p.152-153). Listed as adverse for holding company (p.259) | p.259 |
| vii(b) | Disputed dues: excise 32.86 (FY03, High Court); service tax 6.50; GST 408.89 (paid under protest 20.19), 40.70, 159.17; customs 1,120.09 (Commissioner of Customs, "amount paid under protest: Nil"); customs 72.40; income tax 252.46 (CIT Appeals). CONFLICT: Note 32(e) says 7.5% of 815.09 was paid under protest (61.13 derived) for the 1,120.09 demand (p.230) | p.153 |
| ix | No default on loans or interest, not a wilful defaulter, no short-term funds used long-term | p.153-154 |
| xi | No fraud noticed or reported; no whistle-blower complaints | p.154 |
| xvii | No cash losses in current or preceding year | p.154 |
| xx | CSR: no unspent amount | p.155 |
| xxi (consolidated) | Adverse remarks: holding company ii(b), vii(a); MPPL ii(b) | p.259 |

**1E Auditor continuity**: S.R. Batliboi & Co. LLP (ICAI 301003E/E300005). Appointed at the 34th AGM (23 Sep 2023, a re-appointment) for four years, to the 38th AGM (Directors' report p.54; AGM resolutions CG p.69). Audit reports on the consolidated accounts for FY2021 onward are in the Prospectus (PDF p.59), so tenure is at least five years; the start year is NOT FOUND IN DOCUMENT. Rotation: the 10-year limit year is NOT FOUND (appointment year before FY2021 not stated). Fees standalone: statutory audit 80.50, certification 2.00, expense reimbursement 18.18, total 100.68 (FY25 82.11) (Note 25(a) p.214). Non-audit ratio 2.00 / 80.50 = 2.5% (derived), not above audit. Consolidated fees paid to the auditor: Rs 100.68 lakhs (CG p.76), equal to the standalone total, so no group-wide non-audit fee is shown. Directors' report p.54 says the auditor's report "does not contain any qualification, reservation, adverse remark, or disclaimer". That sentence is true for the standalone report only. The consolidated report is qualified (p.253), and the CARO has adverse remarks. 🔴 as a disclosure inconsistency.

**1F Standalone vs consolidated**: the qualification exists only at group level, while the parent carries MPPL exposure unimpaired: investment 959.01, loan 151.00, receivable 310.05 (sum 1,420.06 derived), guarantee 527.04 (B02 pass 3; Note 5 p.184, Note 31C, p.47). Extra consolidated audit-trail remark: a subsidiary application has no database-level log (p.258). Other auditors: see 1C.

**Phase 1 verdict: 🔴 Red Flag.** Qualified group opinion, EoM on both reports, recurring CARO ii(b) bank-return gaps, a Board report that misstates the audit opinion.
**Kill Switch (informational):** Based on phases so far, a human reviewer would not stop on Phase 1 alone, because no going concern doubt, fraud, or default is reported. The reviewer would want the MPPL and Abohar outcomes sized before sizing a position.

## PHASE 2: NOTES TO FINANCIAL STATEMENTS

### Triple-pass verification (B02 Top 15, checked against the AR)

| Rank | B02 finding | Check at the page | Result |
|---|---|---|---|
| 1 | MPPL assets 4,761.67 qualified; tariff 8.59 to 5.22; MPPL loss 555.04; standalone 959.01 + 151.00 + 310.05; guarantee 527.04 | 4,761.67 (p.253, p.351); 8.59, 3.50 interim, 5.22 final, 5% escalation (p.351); MPPL net loss (555.04) in AOC-1 (p.78); 959.01 (Note 5, p.184); 527.04 (p.47) | ✓ verified |
| 2 | Abohar 1,384.96, Rs 5.26 then 5.88, stay 23 Sep 2025, 50% cap; consolidated Rs 5.42 and Rs 14 crore | Note 46 (p.251) and Cons. Note 45(a) (p.350-351) as stated. NEW: Directors' report says supply continues "at the prevailing tariff of Rs 7.47 per unit" (p.61), a third version | ✓ verified, extended |
| 3 | Receivables 34,304.28 vs 20,307.13 (+68.9%); sold 15,938.75 vs 4,186.33; over 6m 9.2%; nil ECL; 8 customers 71% | BS p.158; Note 6A p.186-187 (over 6m = 2,915.00 + 177.71 + 52.33 + 5.90 = 3,150.94, 9.18%); Note 36 p.241 | ✓ verified |
| 4 | CFO -4,450.03; current borrowings 50,984.72 (+75.9%); undrawn 1,304.77 from 4,964.13; cons CFO +1,954.84 | CF p.160; BS p.158; Note 6D (undrawn); Cons. CF p.264 | ✓ verified |
| 5 | Trade credits 6,577.63 outside gearing; TReDS additions 30,028.24; gearing 41.89%/42.87% | BS p.158; Note 6D table; gearing lines in Note 35 (standalone 41.89%, consolidated 42.87%) | ✓ verified. See Phase 3B for the MD&A ratio that includes them (0.77x) |
| 6 | Thailand 9,190.78 + 3,630.51 + 2,894.76 + 760.52 = 16,476.57 (18.6% of net worth) | Note 5 (9,190.78); Note 31C (3,630.51 at 7.5%, due 31 Dec 2028; 2,894.76; 760.52); net worth 88,706.85 (BS p.158) | ✓ verified (sum is derived) |
| 7 | Numaligarh 18.80% (FY25 4.38%), Dow 12.03% (0.12%) | Note 33(c) p.234 | ✓ verified |
| 8 | Export obligation 20,237.29, customs bond 1,759.76, customs 1,120.09 outside table | Note 32B p.229-230. Table total 350.62 + 622.54 + 1,759.76 + 20,237.29 = 22,970.21 = 25.9% of net worth (derived) | ✓ verified |
| 9 | Labour code 119.23 / 194.44; past service 116.10 / 190.03; employer contribution 25.83 | P&L p.159, p.263; Note 30; Cons. Note 28 | ✓ verified |
| 10 | Bank-return gaps 1,303.20 and 519.91; consolidated gaps 2,068.42 and 4,996.98 | Standalone gaps in CARO ii(b) p.151 verified. Consolidated Note 9B gaps not re-opened | ✓ standalone, consolidated part carried |
| 11 | Shikha Bansal payable 762.90; Molsieve-linked director loan 143.93; CSR 99.8% to promoter foundation | 762.90 (Cons. RPT p.~326); 143.93 (Sudhir Bhalla); CSR 54.29 of 54.42 = 99.76% (Note 25(b) p.214) | ✓ verified |
| 12 | Molsieve 658.82 for 70%, goodwill 602.56 (91.5%) | Note 43; 602.56 / 658.82 = 91.5% (derived); investment line 658.82 (Note 5) | ✓ verified |
| 13 | Audit trail gaps on all three applications | Auditor Rule 11(g) text p.150 and p.257-258 | ✓ verified |
| 14 | Supplier finance wording conflicts; liquidity table basis | 6,577.63 and 8,120.50 verified on BS p.158. Cross-note wording not re-read | ✓ numbers, wording carried |
| 15 | Tax credit 156.90; DTA 348.12; ECL charge 39.74 | P&L p.159; SOCIE p.162 (348.12); CF p.160 (39.74). NEW: consolidated equity shows the same item as 380.98 (p.266), 32.86 higher (derived), unexplained | ✓ verified, extended |

**Triple-pass result: 13 of 15 verified in full; ranks 10 (consolidated half) and 14 (wording) are carried, not re-opened. Zero value discrepancies. Reconciliation with B02 accounting score 5/10: I agree (Phase 2 verdict yellow, see below).**

### 2A Accounting policy aggressiveness

| Item | Policy | Reading | Anchor |
|---|---|---|---|
| Revenue | Sale of goods at point in time on delivery. Erection and job work as and when rendered. Power over time per unit (Note 2.2) | Standard. For build-to-print product shipped to EPCs, delivery-point recognition is conservative against percentage-of-completion | p.166-167 |
| Depreciation | Straight line. Buildings 15 to 60 years, plant 5 to 30 years. Certain items use lives "different from Schedule II" on technical assessment | 30-year plant life is long for robotic welding and trepanning equipment. Depreciation 3,808.69 on gross PPE; capex far above depreciation (Phase 3A) | p.168-169 |
| Capitalisation | Borrowing cost 623.19 and pre-operative 370.03 capitalised; CWIP 7,986.46 (from 14,813.54); intangible under development 454.08 | Moderate; CWIP still 7,986.46 while the Chairman says capex is "substantially complete" (p.7) | B02; BS p.158 |
| ECL | Provision matrix, simplified approach (Note 36). Allowance nil (Note 6A) while P&L charges 39.74 for doubtful debts and advances (CF p.160) | Aggressive: nil allowance with 9.2% over six months | p.186, p.241 |
| Useful-life / estimate changes | None quantified | NOT FOUND IN DOCUMENT | |
| Ind AS 116 | Incremental borrowing rate used (Note 3 estimates, p.~189) | Normal | |

### 2B Related-party map
Direct standalone RPT is 1.09% of revenue (B02). Flows that matter: promoter family pay (CMD 202.51 salary, Shruti Aggarwal 66.99, Shikha Bansal 42.81, Standalone p.67-68, total gross 312.30, 5.6% of standalone PAT 5,621.78, derived); CSR 54.29 to Atul Krishan Bansal Foundation; promoter personal guarantees and DDE Piping Components Pvt Ltd corporate guarantee on bank debt with no disclosed fee (Note 11A, p.~199-200; AR p.~13422); parent guarantees to subsidiaries with no commission (Note 31C p.225); consolidated payable to Shikha Bansal 762.90 vs 26.76 standalone, nature NOT FOUND. Value-extraction signal: low in direct terms; the promoter family is paid inside the subsidiaries (Cons. Note 29, B02) and subsidiaries are funded by the listed parent at 7.5% with interest unpaid in cash (Thailand).

### 2C Contingent liabilities

| Item | Amount (lacs) | % net worth (88,706.85) | % PAT (5,621.78) | Flag |
|---|---|---|---|---|
| Income tax demands | 350.62 | 0.4% | 6.2% | |
| Excise/GST | 622.54 | 0.7% | 11.1% | |
| Custom duty if export obligation unmet | 1,759.76 | 2.0% | 31.3% | |
| Export obligation | 20,237.29 | 22.8% | 360% | >25% of PAT flag; export obligation doubled (10,033.38 prior) |
| Customs demand 815.09 + 305.00 penalty | 1,120.09 | 1.3% | 19.9% | outside table |
| Abohar excess revenue | 1,384.96 | 1.6% | 24.6% (19.1% of PBT) | outside table |
| Guarantees to subsidiaries | 668.89 | 0.8% | 11.9% | CARO says 4,885.22 |
| FEMA ED notice (2023), antidumping duty 72.43 (38.15 provided), BRC request | Not quantified | | | Note 32B p.230 |

All percentages are derived. Table total plus Abohar and customs 1,120.09 gives 25,152.11 (28.4% of net worth, derived), above the 25% flag, driven by export obligation, which is a duty-free import commitment and not a claim.

### 2D Receivables (cross-check of B02)
Standalone ageing (p.187): not due 24,725.49 (72.1%); under 6m 6,427.85; 6m-1y 2,915.00; 1-2y 177.71; 2-3y 52.33; over 3y 5.90. Over-6-months 9.2% vs 5.3% (FY25). Receivable days 136.3 vs 116.0 (derived). Including 15,938.75 sold, receivables are 50,243.03 vs 24,493.46 (+105%, derived). Related-party receivables 1,073.13 (Note 6A p.186). Receivable terms "30 to 180 days". Concentration: eight customers hold 71%, yet the same note calls concentration "low" (Note 36 p.241).

### 2E Inventory
Standalone 51,344.53 vs 51,186.12 (+0.3%) against revenue +43.8%. Consolidated 57,601.52 vs 58,496.46 (BS p.262). Inventory days on revenue basis: standalone 204, consolidated 184 (derived). Half-year Sep-26: consolidated inventory 63,302.46, +5,700.94 in six months (Q2 FY27 p.5, p.7). Write-downs: NOT FOUND in this pass.

### 2F Borrowings
Standalone: non-current 12,678.87, current 50,984.72 (Note 11B), trade credits 6,577.63, leases 1,684.92. Interest cost +50.5%. Approximately 21% of long-term borrowings mature within a year (Note 36 p.241). Security: pledge of fixed assets, promoter personal guarantees, DDE Piping Components corporate guarantee (Note 11A). ICDs given: loans to subsidiaries 4,181.51. Covenant headroom NOT FOUND IN DOCUMENT. CARE rating A-/A2+ reaffirmed with limits enhanced (long-term 205.08 from 75.05 Rs cr; combined 673.00 from 452.00; short term 437.00 from 214.00) (CG p.75). Sanctioned facilities up from Rs 741.05 cr to Rs 1,315.08 cr (derived), +77%.

### 2G Deferred tax
Effective rate standalone 22.3% (24.5% without the 156.90 prior-year credit); consolidated total tax 1,908.18 on PBT 9,624.89 = 19.8% (21.4% without the 151.50 credit) (derived). DTA 348.12 on IPO expense credited to securities premium (SOCIE p.162).

### 2H Other
Exceptional item: Labour Codes 119.23 standalone, 194.44 consolidated, first year (P&L p.159, p.263); the segment note adds it back into employee cost (Cons. Note 31). ESOP: 2,09,264 shares allotted (0.30% of capital, derived) (Secretarial report p.83); ESOP cost 132.64 consolidated (Cons. CF p.264). Leases: RoU 1,590.87. Goodwill 873.74 = 0.98% of net worth (derived). Post balance sheet events: financial statements show none (accounts signed 21 May 2026); the Rs 300 cr preferential issue happened after: Board 3 Jun 2026, EGM 27 Jun 2026, 59,76,096 shares at Rs 502 (Announcement 8 Jul 2026; Chairman p.8). The Directors' report says "no material changes... other than those already disclosed to the Stock Exchanges" (p.46).

Cross-reference to Phase 1: the KAM on subsidiary investments is consistent with Note 31C exposure; the CARO ii(b) gap is consistent with B02 pattern 5; the unmodified standalone opinion on MPPL exposure is the contradiction flagged in 1B.

**Phase 2 verdict: 🟡 Watch.** Policies are standard and no covenant default is disclosed. The weak points are nil ECL, the unprovided Abohar item outside the contingent table, an unassessed MPPL carrying value, and tie-out gaps. B02 scores 5/10; I agree.
**Kill switch (informational):** a human reviewer would not stop on Phase 2 alone, because policies are standard and nothing is in default. They would want the ECL and covenant questions answered.

## PHASE 3: FINANCIAL STATEMENTS (cash flow first)

### 3A Cash flow

| Metric (INR lacs) | Standalone FY26 | Standalone FY25 | Consol. FY26 | Consol. FY25 |
|---|---|---|---|---|
| PAT | 5,621.78 | 2,335.14 | 7,716.71 | 4,363.31 |
| Operating profit before WC changes | 15,260.20 | 9,235.74 | 20,956.88 | 14,537.61 |
| Cash from operations before tax | (2,851.50) | (14,562.53) | 3,781.54 | (10,824.42) |
| Net CFO | (4,450.03) | (15,428.58) | 1,954.84 | (11,845.73) |
| CFO / PAT (derived) | -0.79 | -6.61 | 0.25 | -2.71 |
| EBITDA excluding other income, pre-exceptional (derived) | 15,055.08 | not computed | 19,121.29 | 12,376.32 |
| CFO / EBITDA (derived) | -0.30 | | 0.10 | -0.96 |
| Capex (PPE, CWIP, intangibles) | 16,957.53 | 15,217.18 | 18,953.82 | 16,396.31 |
| Free cash flow (CFO less capex, derived) | (21,407.56) | (30,645.76) | (16,998.98) | (28,242.04) |
| Capex / depreciation (derived) | 4.45x | 4.42x | 3.54x | 3.32x |
| Interest paid (financing) | 5,040.67 | 3,317.17 | 5,368.99 | 3,858.24 |
| CFO after interest paid (derived) | (9,490.70) | (18,745.75) | (3,414.15) | (15,703.97) |
| M&A (Molsieve 70%) | 658.82 | 4,168.47 (Thailand capitalisation) | 651.93 net of cash | not applicable |

Anchors: Standalone CF p.160-161; Cons. CF p.264-265. CFO/PAT is below 0.7 in both years in both views, the repeated flag.
CFO quality checks:
- Interest is classified in financing (5,040.67), so reported CFO is before interest. After interest the group cash drain is 3,414.15 (consolidated), the parent 9,490.70.
- Payables unwinding: standalone trade payables fell 6,896.73 in FY26 (CF p.160); trade payables plus trade credits fell from 22,338.89 to 14,440.83 (7,898.06 lower, derived).
- Receivable factoring flatters CFO: 15,938.75 sold versus 4,186.33 (+11,752.42, derived). Without it, receivables growth would have consumed 11,752.42 more.
- Customer advances and other liabilities added 4,274.65 standalone (CF p.160), 4,076.75 consolidated. These are timing inflows.
- Inventory: consolidated inventory fell 979.60 in FY26 (CF p.264), after 18,492.72 build in FY25. Not a stretch.
- NEW: in the consolidated cash flow, "Unrealized loss on foreign exchange (net)" is 528.03 in FY26 and 76.63 in FY25 (p.264). The foreign currency translation OCI is 528.03 and 76.63 in the same years (SOCIE p.266, P&L p.263). The add-back equals the translation reserve movement to the paisa in both years. A translation movement is not an operating item, so the operating profit line and working capital lines are unreliable by that amount. Net effect is small against 1,954.84, but it shows the statement is built by plug.
- Standalone: unrealised FX gain of 594.00 is deducted (p.160), i.e. profit includes a non-cash FX gain.
- One-time inflators: none identified.

Financing: FY26 consolidated funding came from long-term borrowing 10,906.90, short-term 20,234.99 (net), trade credit repayment 1,542.87 (outflow). Cash pile: consolidated cash 3,926.82 (from 589.04); bank balances 4,509.77 pledged in part (Cons. Note 4C, p.~21920).

**FLAG-CASH: raised.** CFO deteriorated relative to profit growth (PAT +76.9%, CFO consolidated +1,954.84 on EBITDA 19,121.29), with receivables, factoring and payables all moving against cash. FY27 H1 consolidated CFO is -679.09 (Q2 FY27 p.7).

### 3B Balance sheet (consolidated, p.262)

| Walk | Mar-26 | Mar-25 |
|---|---|---|
| PPE + CWIP + RoU + intangibles + goodwill | 72,818.73 + 454.08 ... see lines below | |
| PPE | 62,608.97 | 39,682.40 |
| CWIP | 7,986.46 | 14,813.55 |
| Goodwill | 873.74 | 271.18 |
| Inventories | 57,601.52 | 58,496.46 |
| Trade receivables | 38,334.05 | 24,815.67 |
| Cash + bank | 8,436.59 | 4,755.64 |
| Other current assets | 11,131.97 | 8,169.08 |
| Total assets | 192,372.72 | 159,349.91 |
| Equity | 89,043.69 | 80,057.24 |
| Borrowings (non-current + current) | 68,693.98 | 40,899.61 |
| Trade credits | 6,577.63 | 8,120.50 |
| Trade payables | 9,836.95 | 16,685.99 |
| Other current liabilities | 11,761.30 | 7,636.66 |

Key ratios (derived unless marked):
| Ratio | FY26 | Note |
|---|---|---|
| Net debt / equity per MD&A | 0.77 (FY25 0.58) | MD&A p.102. Reproduced only when trade credits 6,577.63 and leases 1,847.37 are added to borrowings and cash+bank deducted: 68,682.39 / 89,043.69 = 0.77 |
| Borrowings less cash and bank / equity | 0.68 | excludes trade credits and leases |
| Gearing per Note 35 | 42.87% (FY25 34.74%) | excludes trade credits; 45.18% with them (B02) |
| Net debt / EBITDA | 3.15x excluding trade credits and leases; 3.59x with | |
| Current ratio | 1.34 (MD&A 1.33) | p.102 |
| Quick ratio | 0.67 | (current assets less inventory) / current liabilities |
| Interest coverage (PBT before exceptional + finance cost) / finance cost | 2.75x | |
| DSCR per MD&A | 1.92 (FY25 1.81) | p.102 |
| ROCE per MD&A | 10.1% (FY25 8.4%) | p.102 |
| Implied cost of debt | 10.25% (5,617.13 / average borrowings 54,797) | ROCE 10.1% is about equal to the cost of debt. The capex programme earns no spread yet. Derived |
| ROE | 9.1% | MD&A p.102; reproduced: 7,716.71 / 84,550.47 average equity = 9.13% |
| Goodwill / net worth | 0.98% | |

DuPont (derived): net margin 6.76% x asset turnover 0.649 (revenue / average assets 175,861) x equity multiplier 2.08 = ROE 9.13%. ROE is margin and mild leverage driven, with asset turnover of 0.65 the weak leg. Not reproduced by simple formulas: MD&A inventory turnover 1.38 and payable turnover 6.05 (p.102); basis not stated.
Post year end: Rs 300 cr issue lifted equity to 122,617.56 and cut current borrowings to 40,240.72 at 30 Sep 2026 (Q2 FY27 p.5), though receivables 44,640.57, inventory 63,302.46 and other current assets 17,783.66 all rose and a new 5,864.59 of current investments appeared.

### 3C P&L (consolidated, p.263)

| Line | FY26 | FY25 | YoY |
|---|---|---|---|
| Revenue from operations | 114,199.92 | 82,736.22 | +38.0% |
| Other income | 1,664.53 | 2,089.70 | -20.3% |
| Raw material + traded + inventory change | 47,902.83 | 28,936.20 | +65.5% |
| Employee cost | 18,553.28 | 16,100.93 | +15.2% |
| Other expenses | 28,622.52 | 25,322.77 | +13.0% |
| EBITDA excluding other income (pre-exceptional) | 19,121.29 | 12,376.32 | +54.5% |
| Depreciation | 5,349.36 | 4,938.08 | +8.3% |
| Finance cost | 5,617.13 | 3,992.88 | +40.7% |
| PBT before exceptional | 9,819.33 | 5,535.06 | +77.4% |
| Exceptional (Labour Codes) | 194.44 | nil | |
| PAT | 7,716.71 | 4,363.31 | +76.9% |

Material cost rose 65.5% against revenue 38.0%, so gross margin fell to 58.0% from 65.0% (derived: (114,199.92 - 47,902.83) / 114,199.92 against (82,736.22 - 28,936.20) / 82,736.22). Employee and other expenses grew far slower than revenue, which is the operating leverage. Standalone selling commission and other selling expenses rose 129.7% (1,026.19 vs 446.78) against revenue +43.8% (Note 25 p.213; derived), consistent with new export customers; legal and professional +31.3%.
Other income as % of PBT: consolidated 17.3%, standalone 19.0% (derived), under the 20% flag. Tax rate: Phase 2G. Exceptional pattern: one year of data only. EPS: basic 11.16, diluted 11.14 (p.263), gap 0.02. EBITDA bridge to the AR headline: 19,121.29 / 114,199.92 = 16.74%, which ties to the 16.7% shown in the highlights. The highlights label the 16.7% as "operational metrics of core business" (p.6), but it is the whole-group margin, power losses included.
Segments (Cons. Note 31, p.333-335): Piping PBT 10,286.07 (FY25 4,714.68); Power (1,083.14) (FY25 +1,078.96), swing of 2,162.10 lacs; Heavy fabrication 1,771.77 (730.70); unallocated (1,349.81). Core revenue (total less power) = 108,653.28, +45.9%, ties to Rs 1,086.5 cr. Piping carries 100% of the group's PBT and more: total segment PBT before unallocated is 10,974.70 against group PBT 9,624.89.

**Phase 3 verdict: 🔴 Red Flag on cash quality; 🟢 on reported profit growth, which ties across P&L, segment note and the MD&A.**
**Kill switch (informational):** a human reviewer would not stop on Phase 3 alone, because profits reconcile and the Rs 300 cr raise has already repaid part of the debt. They would want the operating cycle proven to shorten before sizing, because two straight years of negative or near-zero CFO against a 3.5x to 4.5x capex-to-depreciation ratio is what the thesis rests on.

## PHASE 4: RISK FACTORS AND MD&A

### 4A Disclosed risks (MD&A p.100, p.103; Directors' report p.~56)
| Risk | Real or boilerplate | Evidence |
|---|---|---|
| Raw material price volatility | Boilerplate. Mitigation text says "back-to-back pricing"; material cost rose 65.5% against revenue 38.0% | p.100; Phase 3C |
| Regulatory and certification | Boilerplate | p.100 |
| Geopolitical and tariff | Boilerplate. Note 44 of the consolidated accounts says no material impact from reciprocal tariffs, states year ended March 31, 2025 (typo for 2026) (p.350) | |
| Competition | Boilerplate | p.100 |
| Macro: currency, interest rate | Generic | p.100 |
| Utilisation ramp-up at Anjar and seamless plant | Real, specific | p.103 |
| Working capital cycle "remains elevated" | Real, no number given | p.103 |
Directors' report risk management section (p.56) is one paragraph with no risk list. Insurance paragraph (p.56) is real, with a deductible caveat.

### 4B Missing risks

| Missing risk | Evidence | Likely reason for omission |
|---|---|---|
| Abohar tariff refund and High Court stay | EoM on both reports (p.146, p.253); Directors' report names it as a significant order "impacting the going concern status" (p.60-61); absent from MD&A risks and outlook (p.103) | Management treats it as won ("strong likelihood of succeeding", Note 46) |
| MPPL impairment and strategic alternatives | Qualified opinion (p.253); MD&A calls the Mar-26 order "a decisive step toward sustainability" (p.101) | Spin: the order lifted the tariff from the 3.50 interim, but is below the 8.59 PPA tariff (Cons. Note 45(b) p.351) |
| Customer concentration | 30.8% of standalone revenue in two customers (Note 33c p.234); 71% of receivables in eight (p.241); Note 36 calls concentration "low" | The risk note is template text |
| Receivable factoring and TReDS dependence | 15,938.75 sold; TReDS additions 30,028.24 (32.7% of revenue) (Note 6A; Note 6D) | Reported as financing mechanics |
| Thin liquidity headroom | Undrawn lines 1,304.77 from 4,964.13 (Note 6D) | Not a classified risk |
| Intra-group claims | Thailand 16,476.57 (Phase 2); Fabricom loan 400.00 | Considered internal |
| Controls | Audit trail gaps on three applications (p.150), recurring bank-return gaps since FY22 (Prospectus p.59-60), no daily backup | Presented as compliance footnotes |
| Key-person and succession | CMD aged 71 (Annexure C p.81); daughter appointed WTD April 2025 | Not a listed risk in India typically |
| Export obligation 20,237.29 doubling | Note 32B | Called "able to fulfil" |
| Financial reporting quality | Unfinished text in AR (Phase 6E) | Production issue |

### 4C MD&A deep dive

Industry claims are macro and unsourced (p.98-99: GE Vernova backlogs, Saudi Vision 2030, data centres); no market size in Rs or share. Growth explained by oil and gas execution plus Anjar ramp-up (p.100). Margin explanation: "operating leverage from newly commissioned Anjar and seamless-pipe capacity" (p.102). But the seamless plant started commercial production on 19 Mar 2026 (p.101), 12 days before year end, so it cannot explain FY26 margin. Credit-taking: all FY26 gains are credited to capacity; Q4 revenue ~Rs 361.6 cr and PAT ~Rs 27.7 cr "reflecting the initial contribution" (p.102). Blaming: working capital described as "capex-driven inventory build-out" (p.103), though inventory was flat in FY26 (BS p.262).

Forward guidance table:

| Claim | Number | Timeframe | Credibility check against delivery |
|---|---|---|---|
| Order inflow | above Rs 2,000 cr (about 60% power, 40% oil and gas; about 60% domestic) | FY27 | FY26 closing order book Rs 1,940 cr, +58% (p.102), but the MD&A footnote says FY25's 1,228 is "to be reconciled" (p.102). FY26 order inflow itself is NOT FOUND IN DOCUMENT |
| Core revenue | Rs 1,400-1,500 cr | FY27 | FY26 core Rs 1,086.5 cr, so +28.9% to +38.1% (derived). H1 FY27 total revenue 58,744.90 lacs, +19.0% (Q2 FY27 p.4). Consolidated FY26 H2 was 31.3% above H1 (64,824.10 vs 49,375.82, derived). The brief's Rs 1,500 cr needs H2 of about Rs 913 cr, +55% over H1. Medium-low |
| Core EBITDA margin | 18-20% | FY27 | FY26 core margin derived 17.8% after the labour-code charge, up to 18.0% if the 194.44 sits wholly in core (segment note p.333; derived). H1 FY27 group margin 18.5% (4,991.76 + 3,246.67 + 3,085.32 - 458.76 = 10,864.99 / 58,744.90; derived, Q2 FY27 p.4); Q2 alone 20.1%, Q1 16.9%. Medium-high |
| Vision 2030 revenue | above Rs 2,500 cr | FY30 | 21.6% CAGR from Rs 1,142 cr over four years (derived) |
| Net debt | net cash or minimal net debt | FY29 | Net debt 60,257.39 lacs at Mar-26 (excl. trade credits; derived). Preferential issue: 75-77% of net proceeds to debt repayment (p.102). By 30 Sep 2026 current borrowings fell 15,104.48 (Q2 FY27 p.5) but working capital absorbed cash. Unproven |
| Capex discipline | "limited to completion and maintenance spends" beyond FY27 | FY28 on | H1 FY27 CWIP up from 7,986.46 to 8,747.53 and RoU up (Q2 FY27 p.5). FY27 itself is not capex-free |
| Power segment | cash neutral | FY27 | FY26 power segment PBT (1,083.14); H1 FY27 power segment result before interest (270.98) vs (257.87) a year earlier (Q2 FY27 p.6). Q2 power revenue only 463.57 vs Q1 1,836.76. Not on track by H1 |
| Seamless plant | commissioning "by January 2026"; utilisation 60-70%; revenue from Q1 FY27 | p.11 | Commissioned 19 Mar 2026, about 2.5 months late; first order about Rs 58 cr for execution through Dec 2026 (p.11, p.101) |
| Anjar 30,000 MTPA | October 2025 | | Delivered Sep 2025 (p.11, p.101). Met |
| Debt: DSCR, ROCE inflection | "Expected to inflect upward" | FY27 | ROCE 10.1% about equals the 10.25% cost of debt |

Historical delivery on guidance: the FY25 AR and earlier guidance are NOT FOUND in the corpus, so only the two build milestones can be tested. One met (Anjar), one late (seamless).

Segment analysis: piping 100,197.90 of revenue (+44.1% derived), power 5,546.64 (-32.9%), heavy fabrication 8,042.75 (+62.7%) (Cons. Note 31 p.333-334). Power revenue fell with the MPPL interim tariff cut from 8.59 to 3.50 (Cons. Note 45(b)).

### 4D Tone and credibility (1 to 5)

| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 2 | Qualified opinion not mentioned in MD&A or Directors' report; Abohar absent from MD&A; Directors' report says audit report has no qualification (p.54) |
| Consistency | 2 | Three Abohar tariff figures (5.88, 5.42, 7.47); three guarantee figures; MD&A growth rates differ from Chairman's (77.3% vs 76.9%) |
| Specificity | 3 | Specific order book, capacity, dates; vague on working capital number |
| Accountability | 2 | Delays and the power loss explained as macro or "decisive step" |
| Capital allocation sense | 3 | Capex delivered, equity raise to repay debt; but ROCE equals cost of debt, dividend of Rs 7.52 cr (p.46) despite negative operating cash |

Contradictions against Phases 1-3: MD&A "balance-sheet strengthening initiatives" (p.100) vs gearing 42.87% and nil headroom; "FY26 preferential issue" (p.103, p.104) vs the issue date of June 2026.

**Phase 4 verdict: 🟡 Watch.** Real information on capacity and order book; the risk section omits every item that carries the audit flags.
**Kill switch (informational):** a human reviewer would not stop, because the guidance is checkable and partly on track (H1 margin 18.5%). They would want a clear management answer on Abohar and MPPL before forming a view.

## PHASE 5: GOVERNANCE AND BOARD

### 5A Board (31 Mar 2026) (CG p.62-64)

| Director | Role | Since | Board meetings attended of 8 | Other directorships |
|---|---|---|---|---|
| Krishan Lalit Bansal | CMD, executive, promoter | 21 Mar 1988 | 7 | 1 |
| Shruti Aggarwal | WTD, daughter | 14 Apr 2025 | 6 | 1 |
| Shikha Bansal | WTD, daughter-in-law | 1 Dec 2020 | 6 | 1 |
| Ashwani Kumar Prabhakar | Independent, Audit chair | 12 Jul 2023 | 5 (62.5%) | 1 |
| Bhisham Kumar Gupta | Independent | 12 Jul 2023 | 8 | 1 |
| Shilpi Barar | Independent, NRC and SRC chair | 12 Jul 2023 | 8 | 1 |

Flags: attendance under 75% (Prabhakar 5 of 8, the Audit Committee chair, who also missed AC-3 on 11 Aug 2025); all three executive directors are one family; Board "directors present" was 4 of 6 at two meetings (14 Apr 2025, 29 May 2025); independents just under three years in role; none over 10 years; seat count under 8. The identical "1" for other directorships across all six directors is unverifiable. Ashima Bansal (promoter, 6.35%) resigned as WTD on 14 Apr 2025 "due to health reasons" the day Shruti Aggarwal was appointed (p.48).

### 5B Committees
Audit: three independents plus the CMD as member (p.65); seven meetings, CMD absent AC-1. The CMD sits on the committee that approves promoter-family related party transactions. NRC: three independents, five meetings. SRC: one meeting. CSR: one meeting, the promoter family plus Shilpi Barar. No separate RPT or risk committee named in the report excerpt read. Independents' fees: 3.50, 4.30, 4.20 lakh.

### 5C Compensation
CMD salary 202.51 lakh, deduction 69.99, total 132.52 (p.67). Shruti Aggarwal 66.99 / 48.80; Shikha Bansal 42.81 / 32.92. Gross total 312.30 lakh = 5.6% of standalone PAT. CMD to median remuneration 26.45x, no increase in FY26; the median employee earns about Rs 5.0 lakh (derived 132.52 / 26.45) (Annexure C p.80). 671 permanent standalone employees. Promoter family payroll in subsidiaries is higher than standalone (B02, Cons. Note 29). ESOP dilution 0.30% issued this year.

### 5D Shareholding (p.72, Note 9F p.195, Q2 shareholding XBRL)

| Date | Promoter | Pledge | Mutual funds | FPI |
|---|---|---|---|---|
| 1 Apr 2024 | 100% (5,30,39,040 sh) pre-IPO | | | |
| 31 Mar 2025 | 70.29% (4,85,38,021) after OFS of 45,01,019 shares and fresh issue | | | |
| 31 Mar 2026 | 70.17% (4,86,06,381), -0.12 pt | None disclosed | 13.91% | 0.98% |
| 30 Sep 2026 | 65.13% (4,90,04,787) | false (XBRL) | | |

Between March and September 2026 promoter shares rose by 3,98,406 (derived) while the percentage fell on the 59.76 lakh preferential shares. Whether promoters took part in the preferential issue is NOT FOUND IN DOCUMENT. K.L. Bansal sold 45,07,179 shares in FY25 (the IPO selling stake). Against a growth story, the IPO sale is normal; no post-listing selling in FY26. Top-10 table (p.73) shows K.L. Bansal at 3,50,57,185 (50.61%) against 3,52,00,366 (50.82%) in Note 9F and in the Board table (p.64), a gap of 1,43,181 shares; Shikha Bansal 14,67,130 vs 14,71,930. One source is stale.

### 5E Red-flag checklist

| Item | Finding |
|---|---|
| Whistle-blower complaints | None (CARO xi(c) p.154; CG p.76) |
| SEBI actions | None found; NSE IPO-proceeds notice closed; SDD notice responded; HSPCB Rs 4.40 lakh fine paid (CG p.76) |
| RPT committee | Audit Committee approves; CMD is a member |
| Auditor fee ratio | 2.5% non-audit |
| CSR | Full spend 54.42; 99.8% to promoter foundation (Note 25(b)) |
| Section 143(12) fraud | None (p.54, p.154) |
| Material subsidiary auditor | Thailand auditor appointed 9 May 2026 for FY26 (p.77) |
| CFO turnover | CFO Sameer Agarwal resigned 5 Jan 2026 "personal reason"; Brham Prakash Yadav appointed 7 Jan 2026 (p.48). New CFO signed the accounts 21 May 2026 |
| Misstatement | Directors' report p.54 says audit report is unqualified (consolidated is qualified) |
| Secretarial audit | Unqualified (p.83-84) |
| Insider-confidence read | Promoter shares up 3,98,406 after year end (derived); no pledge |

**FLAG-PROMOTER-PRELIM:** not raised. No pledge, no post-listing selling.

**Phase 5 verdict: 🟡 Watch.** Clean on regulatory record, pledge, fees and fraud. Weak on family control of the executive bench, the Audit Committee chair's attendance, CFO turnover in the audit year, and a Board report that contradicts the auditor.
**Kill switch (informational):** a human reviewer would not stop, because no regulatory order or pledge exists. They would test the promoter's trust record in stage 8.

## PHASE 6: CHAIRMAN'S LETTER AND FRONT MATTER

### 6A Narrative vs reality

| Claim (p.) | Reality | Mark |
|---|---|---|
| Revenue up 38% to Rs 1,142 cr; operating EBITDA up 54.5% to Rs 191.2 cr; PAT up 76.9% (p.7) | Ties: 114,199.92; 19,121.29; 7,716.71 (p.263) | ✅ |
| Order book Rs 1,940 cr, up 58% (p.7) | Arithmetic ties (1,940 / 1,228). The MD&A footnote says the FY25 base is "to be reconciled" (p.102) | ✅ with caveat |
| "Capex is now substantially complete" (p.7) | CWIP 7,986.46 still open; capex 18,953.82; consolidated H1 FY27 CWIP 8,747.53 | ❌ partly |
| "A favourable PSERC tariff order (27 March 2026) revised Malwa Power's tariff upward" (p.7) | Final Rs 5.22 vs original PPA Rs 8.59, interim 3.50; auditor says management cannot assess impairment; viability "adversely impacted" (Cons. Note 45(b) p.351; Auditor p.253) | ❌ |
| Segment "targeting cash neutrality in FY27" (p.7) | Power segment loss 1,083.14 in FY26; H1 FY27 (270.98) (Q2 FY27 p.6) | ❌ so far |
| Anjar commissioned "ahead of schedule" (p.6) | Yes, Sep 2025 vs Oct 2025 target (p.11). Seamless plant came 2.5 months after the January 2026 target | ✅ / hedged |
| Preferential issue Rs 300 cr, about 75% to debt (p.8) | 59,76,096 shares at Rs 502 allotted (announcement 8 Jul 2026). Debt down 12,360.82 net at Sep-26 (derived) | ✅ |
| Audit report "does not contain any qualification" (Directors' report p.54) | Consolidated qualified (p.253) | ❌ |

### 6B Strategic priorities
FY27 priorities: utilisation ramp at Anjar and seamless, working capital normalisation, capex limited to completion and maintenance (p.8). Specific enough: yes on utilisation, no number given on working capital. Capital allocated: Rs 89.74 cr seamless plant (p.11), Rs 300 cr raise. Execution evidence: Anjar met; seamless late.

### 6C Showcased vs absent
Showcased: revenue, EBITDA, PAT, order book, capacity. Absent: operating cash flow, receivable days, the qualified opinion, Abohar, interest coverage, customer concentration, return on capital versus cost of debt, and the Rs 15,938.75 lacs of factored receivables.

### 6D Tone and drift
Tone is promotional ("strongest financial year yet", "synchronised demand cycle", "decisive step"). Priority drift versus the prospectus: not testable without the FY25 AR (NOT FOUND). Within the AR, the Chairman's letter now stresses working capital normalisation and balance sheet repair, which was not the headline of an IPO-era growth story.

### 6E Quiet Abandonment Check

| # | Opening claim | Where it should show | Class | Materiality |
|---|---|---|---|---|
| 1 | Malwa order "favourable... revised upward" (p.7); non-core "decisive step toward sustainability" (p.101) | Segment results and Note 45(b): tariff cut from 8.59 to 5.22, qualified opinion, "strategic alternatives" | (a) implicit retraction: operations say worse, no acknowledgement in the letter | Material for carrying value of 4,761.67 |
| 2 | Chairman's letter, MD&A outlook and risks silent on Abohar | EoM on both reports; Directors' report names it as a going-concern-impacting order (p.60-61); MD&A risks (p.103) | (b) silent drop | Material: 1,384.96 unprovided |
| 3 | "Capex substantially complete" (p.7) | CWIP and intangibles under development 454.08; cons. capex 18,953.82; the Heavy Fabrication segment capex 184.50 and Power 793.83 (Cons. Note 31 p.333) | (c) hedged retreat: capex continues in FY27 H1 | Moderate |
| 4 | "Disciplined capital allocation" with ROCE inflecting | ROCE 10.1% vs cost of debt 10.25% (derived) | (c) | Moderate |
| 5 | Heavy fabrication "important proof point" (p.101) | Segment: revenue 8,042.75, PBT 1,771.77; FY25 raw material cost nil, 100% gross margin (Cons. Note 31 p.334, B02) | (c): the FY25 comparison is not comparable | Low |

Draft-text artefacts left in the printed report (framework noise on substance, but a reporting-quality signal): "Section to be developed with input from HR" (p.18); "(deck cites 10,000 MT/yr design)" and "see Section 4" (p.14); "Diluted EPS for FY26 to be inserted once confirmed by Finance" and "[TBI] = to be inserted... by the Finance team" (p.102), even though diluted EPS 11.14 is printed in the same table; "FY25 closing order book... to be reconciled" (p.102); the MD&A is printed twice (PDF p.98-103, printed pages 118-123 and 43-48); Chairman's table headers mix "FY 2024-25 / FY 2023-24" with FY26 values (p.6). Directors' report date 21 Aug 2026 against signed accounts 21 May 2026.

**Phase 6 verdict: 🟡 Watch.** Headline numbers tie. Two characterisations contradict the filed notes (Malwa, audit opinion), and the report carries unfinished text.

## PHASE 7: MULTI-STRATEGY SIGNALS

| Strategy | Result | Top 3 reasons |
|---|---|---|
| GARP | WATCHLIST | (1) Growth is real: revenue +38.0%, PAT +76.9%, order book +58% (p.263, p.102). (2) Returns do not yet cover the cost of capital: ROCE 10.1% vs implied debt cost 10.25%. (3) Quality of growth is unproven because CFO/PAT is 0.25 consolidated and -0.79 standalone, and a qualified opinion sits over the power asset. Price/valuation is stage 11, not here |
| Turnaround | FAIL | (1) Not a recovery story: piping PBT 10,286.07 grew 118% (derived), from an already profitable base. (2) The power segment is the only distressed unit, and its recovery is unproven (H1 FY27 still loss-making). (3) Transition is capacity-led, not distress-led |
| Capex-Led Growth | WATCHLIST (best fit) | (1) Capex 18,953.82 consolidated, 3.54x depreciation, delivered ahead on Anjar. (2) Seamless commissioned 19 Mar 2026; benefit begins Q1 FY27 (p.11). (3) Cash cost: FCF -16,998.98 in FY26 and -28,242.04 in FY25, funded by IPO 30,195 and debt; the utilisation proof has not shown in cash |
| Value + Quality | FAIL | ROCE 10.1%, ROE 9.1%, CFO below PAT, qualified opinion |
| Cash Flow Compounder | FAIL | FCF negative for two years; CFO/EBITDA 0.10 |
| Contrarian | WATCHLIST | The market narrative is growth; the contrarian read is the audit flags. A contrarian long needs evidence of resolution (APTEL, ECL, cash). Not yet |
| Insider Confidence | WATCHLIST | Promoter shares +3,98,406 since March (derived), no pledge, 65.13% holding; against that, 45.01 lakh shares sold at IPO and promoter-family pay is large |
| Guidance Divergence | WATCHLIST | Management guide implies H2 revenue +55% over H1 vs +31.3% last year; margin guidance already tracking at 18.5% in H1 |

## PHASE 8: FINAL VERDICT DASHBOARD

**Snapshot:** DEE Development Engineers Ltd, process piping, listed 26 Jun 2024. FY26 consolidated revenue 114,199.92 lacs, EBITDA 19,121.29, PAT 7,716.71, borrowings 68,693.98, net worth 89,043.69 (pre-raise). Post-raise equity 122,617.56 at 30 Sep 2026.

| Phase | Verdict |
|---|---|
| 1 Auditor and CARO | 🔴 |
| 2 Notes | 🟡 |
| 3 Financials | 🔴 (cash) |
| 4 MD&A and risk | 🟡 |
| 5 Governance | 🟡 |
| 6 Front matter | 🟡 |
| 7 Strategy fit | Capex-Led Growth, watchlist |

**Quality score: 4.75 / 10.** Governance 5 (clean record, family bench, attendance and CFO churn, Board report contradiction); accounting 5 (ties to B02); balance sheet 5 (gearing 42.87% to 45.18%, current 1.34, quick 0.67, DSCR 1.92, repaired by the June 2026 raise); earnings quality 4 (profit ties but cash does not).

**Top 3 strengths**
1. Real operating growth that ties across statements: revenue +38.0%, EBITDA +54.5%, PAT +76.9%; piping PBT 10,286.07 (+118%) (Cons. Note 31 p.333).
2. Capacity delivered and funded: Anjar 30,000 MTPA a month early, seamless commissioned, Rs 300 cr equity raised at Rs 502, rating CARE A- with limits enhanced to Rs 1,315.08 cr (CG p.75).
3. No regulatory order, pledge or fraud; promoter holding 65.13% with shares rising post issue.

**Top 3 red flags**
1. Qualified consolidated opinion on MPPL assets 4,761.67, with standalone exposure of 1,420.06 plus guarantee unimpaired, and an Abohar liability of 1,384.96 unprovided under a High Court stay.
2. Cash: two years of negative or near-zero CFO (FCF -45,241.02 over two years, derived) funded by debt and equity; receivables +68.9% with 15,938.75 sold and nil ECL.
3. Disclosure quality: Board report says no audit qualification; three Abohar tariff numbers; three guarantee numbers; unfinished text in the printed report.

**Key monitorables**

| Metric | Threshold | Where | Why |
|---|---|---|---|
| Consolidated CFO / EBITDA | at or above 0.5 for H2 FY27 and FY27 (FY26: 0.10; H1 FY27: negative) | Q3/Q4 results cash flow, FY27 AR | Tests the working capital normalisation claim |
| Receivables (consolidated) vs revenue | debtor days at or below 122 (FY26); balance at or below 44,640.57 (Sep-26) | Quarterly balance sheet | Receivables +68.9% in FY26 |
| Over-6-month standalone receivables share and ECL | at or below 9.2%; first ECL allowance | FY27 AR Note 6A | Nil allowance today |
| Abohar (APTEL, High Court) and MPPL (APTEL) | any final order; any provision or write-down; FY27 audit opinion unqualified | Exchange filings; FY27 auditor report | 1,384.96 and 4,761.67 |
| H2 FY27 revenue | at least Rs 913 cr to reach Rs 1,500 cr | Q3 and Q4 results | +55% over H1 vs +31.3% last year |
| Gearing including trade credits | at or below 40% consolidated | Quarterly net debt | Reported 42.87%, 45.18% with credits |
| Top-two customer share | each below 15% by FY27 | AR Note 33(c) | 18.80% and 12.03% now |
| Promoter holding and pledge | at or above 65.13%, pledge nil | Quarterly shareholding XBRL | Insider signal |
| Controls | audit trail on all applications; CARO ii(b) gap nil | FY27 auditor report | Recurring since FY22 |

**One-line verdict:** A real capacity-led growth story with unproven cash conversion and a qualified group opinion; best fit is Capex-Led Growth on watchlist, not yet GARP-ready.

## Items for later stages (input to other stages, not conclusions)
- Stage 8: Shikha Bansal 762.90 payable, family pay inside subsidiaries, CSR to promoter foundation, promoter participation in the preferential issue, Ashima Bansal exit.
- Stage 10/11: show net debt both with and without trade credits (MD&A 0.77x vs Note 35 42.87%); MD&A net D/E reproduces only with trade credits and leases.
- Stages 4/5: Q2 FY27 call on 17 Nov 2026 must address Abohar billing since 1 Apr 2025, the tariff the Directors' report cites (Rs 7.47), and the guarantee quantum.

---
ORCHESTRATOR ERRATA (2026-11-15; reported by the stage itself, which could not edit its report after writing)
- Section 3B: the balance-sheet row reading "PPE + CWIP + RoU + intangibles + goodwill ... see lines below" is void. The PPE, CWIP and goodwill rows below it are correct.
- Section 4A and the Phase 4 risk paragraph cite Directors' report p.56 for risk management and insurance. The correct PDF page is p.51.
- Section 5D cites p.72 for the shareholding table. The correct page is p.73.
- Anchors in Phase 2 written "p.~" (RPT details, Note 11A, lease note) are approximate, not verified page anchors.
- The Q2 FY27 standalone operating cash flow cited as "p.9" sits in the standalone block of the results file; the page is unconfirmed.

---
ORCHESTRATOR ERRATUM, SOURCE FIDELITY (2026-11-15; Verifier A finding, B12a row 1; figure corrected at source)
- Phase 2C closing paragraph: the contingent-liabilities total "25,152.11 lacs (28.4% of net worth)" is wrong. The three components are each correct in the AR and sum to 22,970.21 (Note 32B p.229) + 1,384.96 (Note 46 p.251) + 1,120.09 (Note 32(e) p.230) = 25,475.26 INR lacs = 28.7% of net worth 88,706.85 INR lacs. Use 25,475.26 and 28.7%.

```yaml
stage: B03-ardeep
company: "DEEDEV"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
unit: "INR lacs as printed in the financial statements and notes; Rs crore where the MD&A and Chairman letter print crore. Nothing converted."
input_gaps:
  - "empty screener P&L/BS/CF/Quarters sheets (Data_Sheet populated)"
  - "Q2 FY27 concall transcript absent (call on 17 Nov 2026, after run date; CORPUS GAPPED-FRESHNESS)"
  - "Q2 FY27 investor presentation absent"
  - "research empty"
  - "shareholding is XBRL text"
  - "Results_Q4FY26 text is an OCR layer"
  - "FY25 annual report absent: prior-year guidance, prior-year targets and Phase 6D drift not testable"
  - "covenant headroom, Thailand DCF, 762.90 payable nature, Abohar billing since 1 Apr 2025: NOT FOUND IN DOCUMENT"
  - "top-10 customer 80% of operating income (brief fact 4) NOT FOUND in the AR"
flags:
  - {type: FLAG-CASH, reason: "consolidated CFO 1,954.84 vs PAT 7,716.71 (0.25) and EBITDA 19,121.29 (0.10); standalone CFO -4,450.03; FCF -16,998.98 consolidated; interest paid 5,368.99 sits in financing; receivables +68.9% with 15,938.75 sold; H1 FY27 CFO -679.09 (Cons. CF p.264; CF p.160; Note 6A; Q2 FY27 p.7)"}
  - {type: FLAG-QUALIFIED-OPINION, reason: "consolidated opinion qualified on MPPL assets 4,761.67 lacs, impairment not assessable (Auditor p.253; Cons. Note 45(b) p.351)"}
  - {type: FLAG-CONTINGENCY, reason: "Abohar 1,384.96 lacs unprovided under High Court stay, EoM on both reports, outside Note 32B table; Directors report cites a third tariff Rs 7.47 (Note 46 p.251; Auditor p.146; Directors report p.61)"}
  - {type: FLAG-BOARD-REPORT-MISSTATES-AUDIT, reason: "Directors report says the audit report has no qualification, reservation or adverse remark (p.54) while the consolidated report is qualified (p.253) and CARO lists adverse remarks ii(b), vii(a) (p.259)"}
  - {type: FLAG-DRAFT-ARTEFACTS, reason: "printed AR carries placeholders: [TBI], 'Diluted EPS to be inserted', 'Section to be developed with input from HR', 'to be reconciled' on FY25 order book (p.18, p.102)"}
  - {type: FLAG-GUARANTEE-QUANTUM, reason: "guarantees outstanding stated as 668.89 (Note 32C p.230; Directors report p.47) vs 4,885.22 (CARO iii p.152 = 668.89 + 4,216.33) vs 2,300.00 MPPL given in year (Note 31B p.223)"}
phase_verdicts: {p1: "RED", p2: "YELLOW", p3: "RED", p4: "YELLOW", p5: "YELLOW", p6: "YELLOW", p7_best_fit: "Capex-Led Growth (WATCHLIST)"}
overall_quality: 4.75
quality_components: {governance: 5, accounting: 5, balance_sheet: 5, earnings: 4}
kill_switch_notes:
  - "P1: reviewer would not stop alone; no going concern doubt, fraud or default; would size MPPL and Abohar before position size"
  - "P2: would not stop; policies standard, no covenant default; wants ECL and covenant answers"
  - "P3: would not stop; profits reconcile and Rs 300 cr raise repaid debt; wants operating cycle proven to shorten"
  - "P4: would not stop; guidance checkable (H1 margin 18.5%); wants a clear answer on Abohar and MPPL"
  - "P5: would not stop; no SEBI order or pledge; test promoter trust record in stage 8"
triple_pass_verification:
  verified: 13
  discrepancies: []
  carried_not_reopened: ["rank 10 consolidated bank-return gaps 2,068.42 and 4,996.98 (Cons. Note 9B)", "rank 14 cross-note supplier-finance wording (numbers 6,577.63 and 8,120.50 verified on BS p.158)"]
  extensions: ["rank 2: Directors report p.61 gives third tariff Rs 7.47", "rank 15: consolidated equity shows IPO deferred tax as 380.98 vs standalone 348.12 (p.266 vs p.162), gap 32.86 derived, unexplained", "CARO vii(b) customs 1,120.09 shows paid under protest Nil vs Note 32(e) 7.5% of 815.09 (p.153 vs p.230)"]
missing_risks:
  - {risk: "Abohar tariff refund and High Court stay", evidence: "EoM both reports p.146, p.253; Directors report p.60-61; absent from MD&A risks p.103"}
  - {risk: "MPPL impairment and strategic alternatives", evidence: "qualified opinion p.253; MD&A calls order decisive step p.101"}
  - {risk: "customer concentration 30.8% in two customers, 71% of receivables in eight", evidence: "Note 33(c) p.234; Note 36 p.241 calls concentration low"}
  - {risk: "receivable factoring and TReDS dependence", evidence: "15,938.75 sold; TReDS additions 30,028.24 (Note 6A p.186; Note 6D)"}
  - {risk: "thin liquidity headroom", evidence: "undrawn lines 1,304.77 from 4,964.13 (Note 6D)"}
  - {risk: "intra-group claims on Thailand and Fabricom", evidence: "Thailand 16,476.57 (Note 5, 31C); Fabricom loan 400.00 (p.47)"}
  - {risk: "control gaps: audit trail and recurring bank-return mismatch", evidence: "Auditor p.150, p.258; CARO ii(b) p.151; Prospectus risk factor 26 PDF p.59-60"}
  - {risk: "key person and succession", evidence: "CMD aged 71 (Annexure C p.81); daughter appointed WTD 14 Apr 2025 (p.48)"}
  - {risk: "export obligation doubled to 20,237.29", evidence: "Note 32B p.229-230"}
guidance_table:
  - {claim: "FY27 order inflow", number: "above Rs 2,000 cr", timeframe: "FY27", credibility: "unverified; FY26 order inflow NOT FOUND; FY25 base 1,228 flagged 'to be reconciled' in the MD&A (p.101-102)"}
  - {claim: "FY27 core revenue", number: "Rs 1,400-1,500 cr (brief: Rs 1,500 cr plus from Q1 call)", timeframe: "FY27", credibility: "medium-low; H1 growth +19.0% vs needed +29% to +38%; H2 needs +55% over H1 vs +31.3% in FY26 (Q2 FY27 p.4; derived)"}
  - {claim: "FY27 core EBITDA margin", number: "18-20%", timeframe: "FY27", credibility: "medium-high; FY26 core 17.8-18.0% derived; H1 FY27 group margin 18.5% derived"}
  - {claim: "Vision 2030 revenue", number: "above Rs 2,500 cr", timeframe: "FY30", credibility: "needs 21.6% CAGR from Rs 1,142 cr (derived)"}
  - {claim: "net cash or minimal net debt", number: "n/a", timeframe: "FY29", credibility: "unproven; net debt 60,257.39 lacs at Mar-26, 75-77% of Rs 300 cr raise earmarked for debt (p.102)"}
  - {claim: "power segment cash neutral", number: "n/a", timeframe: "FY27", credibility: "low so far; FY26 segment PBT (1,083.14); H1 FY27 (270.98) before interest (Q2 FY27 p.6)"}
  - {claim: "seamless plant commissioned by January 2026", number: "7,000 MTPA, 60-70% utilisation target", timeframe: "Jan 2026", credibility: "late by about 2.5 months (19 Mar 2026, p.11, p.101)"}
  - {claim: "Anjar 30,000 MTPA by Oct 2025", number: "30,000 MTPA", timeframe: "Oct 2025", credibility: "met: Sep 2025 (p.11, p.101)"}
  - {claim: "capex limited to completion and maintenance beyond FY27", number: "n/a", timeframe: "FY28 on", credibility: "unproven; H1 FY27 CWIP up 761.07 (Q2 FY27 p.5)"}
monitorables:
  - {metric: "consolidated CFO / EBITDA", threshold: "at or above 0.5 for H2 FY27 and FY27 (FY26 0.10)", where: "Q3/Q4 cash flow; FY27 AR", why: "tests working capital normalisation"}
  - {metric: "consolidated debtor days and receivables", threshold: "at or below 122 days; at or below 44,640.57 lacs", where: "quarterly balance sheet", why: "receivables +68.9% in FY26"}
  - {metric: "standalone over-6-month receivables share and first ECL", threshold: "at or below 9.2%", where: "FY27 AR Note 6A", why: "nil allowance today"}
  - {metric: "Abohar and MPPL court outcomes, FY27 audit opinion", threshold: "any final order; opinion unqualified", where: "exchange filings; FY27 auditor report", why: "1,384.96 and 4,761.67 lacs at stake"}
  - {metric: "H2 FY27 revenue", threshold: "at least Rs 913 cr to reach Rs 1,500 cr", where: "Q3/Q4 results", why: "+55% over H1"}
  - {metric: "gearing including trade credits", threshold: "at or below 40% consolidated", where: "quarterly net debt", why: "42.87% reported, 45.18% with credits"}
  - {metric: "top-two customer share", threshold: "each below 15% by FY27", where: "AR Note 33(c)", why: "18.80% and 12.03% now"}
  - {metric: "promoter holding and pledge", threshold: "at or above 65.13%, pledge nil", where: "quarterly shareholding XBRL", why: "insider signal"}
  - {metric: "audit trail coverage and CARO ii(b) gap", threshold: "all applications enabled; gap nil", where: "FY27 auditor report", why: "recurring since FY22"}
ar_new_downstream_entities:
  - name: "Numaligarh Refinery Limited"
    where_in_ar: "Note 33(c) p.234 (17,268.79 lacs, 18.80% of standalone revenue; FY25 4.38%); AR also lists a DEE Numaligarh facility, 6,000 MT/yr (p.14)"
    entity_type: "customer above 10% of revenue for the first time in this AR (FY25 AR not in corpus to confirm earlier disclosure)"
  - name: "Dow Chemical Canada ULC"
    where_in_ar: "Note 33(c) p.234 (11,048.38 lacs, 12.03%; FY25 0.12%)"
    entity_type: "customer above 10% of revenue, export"
  - name: "Molsieve Design Limited"
    where_in_ar: "Note 5 and Note 43 (658.82 lacs for 70%, goodwill 602.56); MD&A hydrogen platform p.101"
    entity_type: "acquired subsidiary (nitrogen, oxygen, ammonia cracking, hydrogen purification)"
strengths_top3:
  - "Real operating growth that ties across statements: revenue +38.0%, EBITDA +54.5%, PAT +76.9% (Cons. P&L p.263); piping PBT 10,286.07 (Cons. Note 31 p.333)"
  - "Capacity delivered and funded: Anjar 30,000 MTPA in Sep 2025, seamless plant 19 Mar 2026, Rs 300 cr equity at Rs 502, CARE A- limits enhanced (p.11, p.101, p.75)"
  - "No regulatory order, no pledge, no fraud; promoter holding 65.13% with promoter shares up 3,98,406 since March (CG p.76; XBRL 30 Sep 2026)"
red_flags_top3:
  - "Qualified consolidated opinion on MPPL assets 4,761.67 plus Abohar 1,384.96 unprovided under a stay (Auditor p.253; Note 46 p.251)"
  - "Cash: FCF -45,241.02 over two years (derived), receivables +68.9% with 15,938.75 sold and nil ECL (Cons. CF p.264; Note 6A)"
  - "Disclosure quality: Board report denies the qualification, three tariff and three guarantee figures, unfinished text in the printed AR (p.54, p.61, p.102)"
best_fit_strategy: "Capex-Led Growth (WATCHLIST); GARP WATCHLIST pending cash conversion"
one_line_verdict: "Real capacity-led growth with unproven cash conversion and a qualified group opinion; watchlist, not GARP-ready."
analyst_note: "Units INR lacs. The brief's Rs 9.76 cr guarantee figure is not in the AR: AR shows 668.89 lacs (Note 32C), 4,885.22 (CARO) and 2,300.00 given (Note 31B). MD&A net D/E 0.77 reproduces only with trade credits 6,577.63 and leases added; Note 35 gearing 42.87% excludes them. Consolidated cash flow adds back FX 'loss' 528.03 and 76.63 equal to the translation OCI in both years. Standalone auditor accepts a management valuation of subsidiary investments (KAM 18,784.88) while the consolidated auditor says MPPL cannot be assessed. Core EBITDA margin in the highlights (16.7%) is the whole-group margin. Unnamed counterparties (HRSG reservation EPC major, global OEM LOI, green hydrogen partner) are NOT DISCLOSED. Brief fact 4 (top-10 about 80%) not in the AR."
```
