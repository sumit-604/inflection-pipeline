# STAGE 2, PASS 2 (WHAT WAS MISSED): Creative Newtech Ltd (CNL), run 2026-11-11

Source: runs/cnl-2026-11-11/inputs/annual-report/CNL_AR_FY2025-26.txt ("AR p.N" is the `[page N]` marker). Unit on the face of both sets of statements: **Rs. in Lakhs** (SA p.73, CON p.97). Nothing is converted; stage 10 converts once. "SA" is standalone, "CON" is consolidated. "Derived" means my arithmetic on disclosed numbers, with inputs shown.
Method: Standalone Notes 1-46 (AR p.75-91), Consolidated Notes 1-39 (AR p.99-112), both primary statements, and AOC-1 (AR p.63) were re-read from the start against Pass 1 plus errata. The errata govern. Pass 1 findings are not repeated. Items outside the notes are labelled OUTSIDE NOTES.
Rating key: 🟢 Clean | 🟡 Watch | 🔴 Red Flag.

---------------------------------------------------------------------
## A. CORRECTIONS AND REFINEMENTS TO PASS 1 (not counted as new findings)

- **C1. F43 "odd item" withdrawn.** Pass 1 called the cash-flow line "OCI amount (16.65)" odd. It is a correct reconciling entry. Provisions rose by (155.08 + 55.74) - (114.44 + 52.48) = 43.90 (SA Notes 16 and 21, AR p.83), which includes the 16.65 actuarial loss that went to OCI and not through PBT. The cash flow adds back 43.89 and removes 16.65 (SA cash flow, AR p.74). The 31.60 P&L charge + 16.65 - 4.35 benefits paid = 43.90 ties to it.
- **C2. F40 "2.7 times SCL PBT, difference not explained" is now bridged.** See P2-2 below.
- **C3. F28 associate loss.** AOC-1 (AR p.63) shows associate loss 11.08 at 100%, of which 5.40 is "considered in consolidation" and 5.68 "not considered". 5.40 is the CON charge (CON Note 5, AR p.104), so the loss ties. Only the 39.16 gap between net worth attributable (314.34) and carrying value (275.18) in Pass 1 stands.
- **C4. LB3 / F40 wording.** Pass 1 said segment result "is not gross margin" and the 40-42% brand margin was NOT FOUND. Arithmetic in P2-1 shows the reported segment result is gross profit. The conclusion on 40-42% changes (see P2-1).

---------------------------------------------------------------------
## B. NEW FINDINGS

### P2-1. Reported "segment result" is exactly gross profit; documented brand margin is 33.2%, not 40-42%  🟡
Anchors: SA Note 39 (AR p.89-90); CON Note 37 (AR p.111-112); SA P&L (AR p.73); CON P&L (AR p.97).
The segment tables say the result is "net revenue after deducting allocable cost". Rebuilding it from the P&L, in Rs. Lakhs:

| Basis | Revenue ex export entitlements | Purchases + change in stock (COGS) | Gross profit (derived) | Reported total segment result |
|---|---|---|---|---|
| SA FY26 | 255,116.00 | 248,723.17 + (4,789.26) = 243,933.91 | 11,182.09 | 11,182.07 |
| SA FY25 | 163,854.80 | 159,078.57 + (1,840.05) = 157,238.52 | 6,616.28 | 6,616.28 |
| CON FY26 | 269,977.25 | 255,227.91 + (6,608.57) = 248,619.34 | 21,357.91 | 21,357.91 |
| CON FY25 | 177,447.71 | 165,256.38 + (2,670.89) = 162,585.49 | 14,862.22 | 14,862.23 |

So segment result = revenue (ex export entitlements) minus purchases and inventory change, to within 0.02 in all four cases. Consequences:
- Brand gross margin on the documented basis (derived): CON 12,629.19 / 38,085.50 = **33.16%** (FY25 9,356.16 / 27,067.93 = 34.57%). SA brand 2,453.37 / 23,224.22 = 10.56% (8.24%). MES: CON 3.76%, SA 3.76% (3.66%). Group gross margin 7.91% (FY25 8.38%); SA 4.38% (4.04%).
- The memory claim of 40-42% brand gross margin is **not supported** by this basis. The closest documented figure is 33.2% and it is falling. It could only reach 40-42% on a different perimeter or definition not in the notes.
- "Unallocable cost" is also reconstructable. SA FY26: employee 1,652.41 + depreciation 142.57 + other expenses 4,536.32 - other income 1,289.32 - export entitlements 484.47 = 4,557.51 (reported 4,557.49). SA FY25 gives 2,221.58 (reported 2,221.58). CON FY26: 2,129.98 + 152.10 + 10,601.59 - 1,289.32 - 484.47 + associate loss 5.40 = 11,115.28 (reported 11,115.28). It is all operating expense, net of other income and entitlements, and none of it is allocated to a segment. The notes therefore give no segment profit after operating cost.
- This also explains the Pass 1 oddity in F40: SA segment policy says "geographic segment" (SA Note 2(s), AR p.79) while the reported segments are Brand and MES. The reported measure is a product gross profit.

### P2-2. Bridge of the Hong Kong subsidiaries' contribution to CON, and what their cost base is  🟡
Anchors: CON Notes 27, 28, 29 (AR p.107-108); CON Note 37 (AR p.112); SA Notes 27-29 (AR p.84-85); AOC-1 (AR p.63).
Derived bridge (CON less SA), Rs. Lakhs: gross profit +10,175.84 (21,357.91 - 11,182.07) - unallocable cost +6,557.79 (11,115.28 - 4,557.49) - finance cost +23.51 (2,066.43 - 2,042.92) = **+3,594.54**, which equals CON PBT 8,176.20 less SA PBT 4,581.66 exactly. This explains the Pass 1 "2.7 times SCL PBT" point: the 10,175.82 is segment gross profit before the subsidiaries' own operating costs. It is not a profit comparable to the AOC-1 PBT.
Composition of the 6,557.79 (CON-only, derived): employee cost 477.57 (FY25 242.39, +97%), depreciation 9.53, other expenses 6,065.27 (FY25 5,176.47), associate loss 5.40. Within other expenses (CON Note 29 minus SA Note 29):
- Service charges reimbursement 2,537.02 (FY25 3,025.85, -16%) + reimbursement of expenses 602.65 (495.61) + royalty 595.73 (587.55) = 3,735.40, i.e. 57.0% of the 6,557.79 cost base. Payees are not identified, and none of these appear in the RPT table (SA Note 36 / CON Note 35) as related-party flows.
- Advertising and promotional 1,151.54 in CON versus nil in SA (FY25 384.48 vs 33.01), so the subsidiaries spent 1,151.54 (FY25 351.47, +228%).
- Clearing charges +329.75 (595.23 vs 265.48), storage charges 259.65 (139.15), certification 87.46, inspection 82.48.
Whether the 3,594.54 PBT contribution is "real" depends on those unnamed payees. Transfer-pricing basis between SA and SCL: NOT FOUND IN DOCUMENT (already in Pass 1 F6).

### P2-3. Hong Kong subsidiaries burn cash while reporting profit; the cash-flow "translation" line looks like a plug; SA operating outflow is flattered by SCL credit  🟡
Anchors: SA cash flow (AR p.74); CON cash flow (AR p.98); CON Note 9 / SA Note 9 (AR p.105 / p.81); SA Note 36 (AR p.89).
- CON less SA operating cash flow: (27,188.34) - (25,738.12) = **(1,450.22)** for the two subsidiaries, against a PBT contribution of +3,594.54. Operating profit before working capital for the subsidiaries is +3,604.07; working-capital items are (5,054.29): receivables +1,532.79, other assets (1,365.67), inventories (1,819.31), payables-side (3,402.10) (derived from CON less SA lines).
- Investing: (203.97) = the subsidiaries' intangible purchase (CON Note 4, see P2-13). Financing: +0.13.
- HK cash: opening FY26 4,387.66 - 3,376.29 = 1,011.37; closing 535.96 - 475.97 = 59.99. The CON cash flow shows "Exchange difference on translation of foreign currency" +702.68 (FY25 +202.21), which is 69.5% of the HK opening cash for FY26 and 8.0 times the HK opening cash for FY25 (719.73 - 694.55 = 25.18) (derived). A translation effect on cash cannot be that large relative to the cash it translates, so the line appears to balance the statement and to carry translation effects on non-cash balances. It tracks the equity translation credit (861.98 FY26, 237.74 FY25, CON SOCIE, AR p.98) at 81.5% and 85.1%. The notes do not say how the line is built.
- SA CFO benefit: the SCL balance swung from receivable 274.99 to payable (3,093.04), a 3,368.03 swing (SA Note 36, AR p.89). If the payable sits in trade payables and the receivable in trade receivables, SA's reported (25,738.12) outflow would be about (29,106.15) without that supplier credit from the 77.5% subsidiary (derived, assumption stated). This is 13.1% of the SA outflow. It nets out in CON, which is why the CON figure (27,188.34) is the cleaner group measure. SCL funded this out of its own working capital, and the two subsidiaries ended with 59.99 of cash between them.

### P2-4. Note 43 return ratios are built so as to flatter the year  🟡
Anchors: SA Note 43 (AR p.90); SA balance sheet (AR p.73).
- ROCE 22.01% (16.31%) is reproduced only with capital employed = total assets - current liabilities: EBIT 6,624.58 (4,581.66 + 2,042.92) / (86,311.16 - 56,206.41 = 30,104.75) = 22.0%; FY25 4,394.70 / (46,816.57 - 19,873.35 = 26,943.22) = 16.31% (derived). All 32,424.87 of borrowings sits in current liabilities, so it is excluded from capital employed. On equity plus debt (29,949.67 + 32,424.87 = 62,374.54; FY25 26,602.47 + 7,179.37 = 33,781.84) ROCE is **10.62% (13.01% in FY25)**: down, not up. The management explanation ("significant improvement in profitability at a higher rate than the increase in capital employed") is only true on the excluding-debt basis.
- Receivable turnover 6.71 (10.05) uses average receivables (255,600.47 / 38,004.62 = 6.73, derived); 365 / 6.71 = 54.4 days, against 78.7 on closing balances (Pass 1 F23). ROE 11.47% uses closing equity (3,434.75 / 29,949.67). Mixed averaging bases soften the year-end position.
- "Return on Investment" 5.95% (5.76%), numerator "income generated from invested funds", cannot be reproduced from Note 5: investments are 3,514.61 unchanged with no income line (SA Note 5, Note 24). The nearest reproduction is FD interest 83.26 / average other bank balances 1,408.88 = 5.91% (derived, not exact). The ratio is on a different base from the one named.
- DSCR 3.67 (5.59): numerator and denominator inputs not reproducible from disclosed lines; NOT FOUND IN DOCUMENT.

### P2-5. Revenue discount near zero against an audit emphasis on rebates; marketing-type costs expensed, not netted  🟡
Anchors: SA Note 23.3 (AR p.84); CON Note 23.3 (AR p.108); SA Note 29 (AR p.84-85); Auditor KAM 1 (OUTSIDE NOTES, AR p.91-92); SA Note 2(l) (AR p.78).
- The policy deducts "trade discounts, volume rebates" from revenue. Note 23.3 shows discount of 14.81 on a contract price of 255,130.81 (0.0058%), down from 129.50 on 163,984.30 (0.079%), a fall of 88.6% while revenue rose 55.2%. CON shows the same 14.81 / 129.50, so the subsidiaries report no discounts at all.
- The auditor's first key audit matter is variable consideration, rebates and discount schemes. The notes quantify none of it beyond 14.81.
- Meanwhile commission 1,110.71 (344.90) and sales promotion 1,098.35 (564.08) are expensed. Together 2,209.06 vs 908.98, +143.0%, or 0.86% of revenue vs 0.55% (derived). CON adds advertising: commission + sales promotion + advertising = 3,570.15 vs 1,307.61 (+173.0%), 1.32% of CON revenue vs 0.73%, and 43.7% of CON PBT. Payees, and whether any is consideration payable to customers (which Ind AS 115 treats as a revenue reduction unless for a distinct service), are NOT FOUND IN DOCUMENT. Commission is not in the RPT table.
- This is a disclosure gap, not a proven misclassification.

### P2-6. Other income of 549.71 has no disclosed nature; the 518.83 incentive receivable vanished  🟡
Anchors: SA Note 24 (AR p.84); SA Note 11 (AR p.81); SA Note 2(l) (AR p.78); CON Note 11 (AR p.105).
- "Other Income" 549.71 (625.93) is a single unexplained line: 42.6% of other income of 1,289.32 and 12.0% of SA PBT. With the exchange gain 652.71, the two unexplained or volatile lines are 1,202.42, 26.2% of SA PBT (derived). The policy says other income "is recognised based on agreements/arrangements with the customers, if any". Counterparty and arrangement: NOT FOUND IN DOCUMENT.
- Note 11 shows "Incentive & Commission Receivable" 518.83 at Mar-2025 and nil at Mar-2026. Cash settlement, write-off, or reclassification into supplier advances (8,595.74, +51.0%, Note 12) is not stated. FY25 other income of 625.93 against an incentive receivable of 518.83 suggests the receivable relates to this income, but the notes do not say so.

### P2-7. Credit-loss language is "incurred loss"; allowance static through FY25; the same 236.66 carries four labels  🟡
Anchors: SA Note 8 (AR p.81); SA Note 32 (AR p.86); CON Note 8 (AR p.104); SA Note 2(o) (AR p.78).
- Note 32 states the allowance "represents its estimate of incurred losses", an incurred-loss concept, while Note 2(o) claims lifetime ECL. It also says the 22.73 allowance was created "till the F.Y 2022-23", and the reconciliation shows 22.73 at both the opening and closing of FY25, unchanged while gross receivables stood at 20,893.93. The only increase, 54.04 in FY26, followed the disputed balance rising to 236.66, with gross receivables at 55,214.80.
- The same 236.66 is described as "Unsecured, Disputed" (nil line) and "Trade receivables which have significant increase in credit risk" (face of Note 8), "Disputed considered good" (ageing), "doubtful" (Note 32) and "credit impaired" (provision line). The credit stage is not clear. Coverage 76.77 / 236.66 = 32.4% (FY25 22.73 / 87.08 = 26.1%) (derived).
- SA and CON are identical (CON Note 32, AR p.109), so the subsidiaries add no provision.

### P2-8. The "critical estimates" list leaves out the areas the auditor flags as key audit matters  🟡
Anchors: SA Note 2(b) (AR p.75); CON Note 2(b) (AR p.99); Auditor KAMs (OUTSIDE NOTES, AR p.91-92).
- The estimates list covers useful lives, deferred tax asset recognition, defined benefit obligation, and provisions and contingent liabilities. It does not list expected credit loss on trade receivables (55,138.03 net), inventory net realisable value (13,188.06), variable consideration or rebates, or foreign currency items.
- The CON list does not list control of the 77.5%-owned SCL (policy defines a subsidiary as one where the group "exercise control or hold more than one-half of its total share capital", CON Note 2(a), AR p.99, rather than the Ind AS 110 control test), or the translation of foreign operations.
- The cross-reference shows the notes' judgement disclosure is narrower than the audit risk areas.

### P2-9. Borrowings: covenants are referred to but never disclosed; lenders other than banks; interest to "others"  🟡
Anchors: SA/CON Note 33 (AR p.86 / p.109); SA Note 17 (AR p.83); SA Note 28 (AR p.84); SA cash flow (AR p.74).
- Note 33 says the company adjusts its capital structure for "the requirements of the financial covenants". No covenant, ratio test, breach, or waiver is disclosed anywhere (Pass 1 F30 recorded covenants as NOT FOUND; this cross-reference shows covenants exist).
- SA Note 17 caption: "Secured Loans from Banks and NBFC" 32,417.28; the security text names only HDFC, Axis, DBS, and SBI. CON Note 17 caption reads "Loans repayable on demand from Others" 32,417.29 (AR p.106). Any NBFC lender: NOT FOUND IN DOCUMENT.
- Interest expense split (Note 28): banks 1,494.29 (635.21, +135.2%), others 252.62 (157.62, +60.3%). "Others" is 14.5% of interest (19.9% in FY25). Counterparty, rate, and security for the "others" interest: NOT FOUND IN DOCUMENT. The stated 9% to 11% range is given only for cash credit and ECLGS.
- ECLGS was fully repaid in FY26: repayment of long-term borrowings (226.31) (FY25 (470.04)), and the CON closing non-current term loan is 1.21 (SA cash flow, AR p.74; CON Note 15, AR p.106). Pass 1 F30 noted the nil balance; the cash flow confirms repayment, not reclassification. The Note 15 security description still lists ECLGS properties after repayment.

### P2-10. "Bank buyers credit expenses" of 4,493.48 cannot be a P&L expense  🟡
Anchors: SA Note 37 (AR p.89); SA Note 28 (AR p.84).
SA Note 37 lists "Bank Buyers Credit Expenses" in foreign currency 4,493.48 (296.26), a 15.2x rise. Total SA finance cost is 2,042.92, interest to banks 1,494.29, and buyer's credit / BG charges are 125.43 (Note 28). A 4,493.48 "expense" is 2.2 times total finance cost, so the label must be wrong or the figure is principal settled or drawn under buyers credit (derived inference; notes do not say). Either way, the foreign-currency borrowing under buyers credit, its outstanding balance and its currency are NOT FOUND IN DOCUMENT, and buyers credit is guaranteed by the "Director and Whole-time director" (Note 17(d)). Pass 1 F32 and F44 quoted the 4,493.48 without testing the label.

### P2-11. Contingent liabilities: details that weaken the table  🟡
Anchors: SA Note 35 (AR p.87-88); CON Note 34 (AR p.109-110), identical.
- **DGGI item 191.44** is 31.9% of the 600.01 ex-guarantee total and 37.2% of the GST items (derived). The note says the order is "under section 83" (provisional attachment), gives two dates for it (1 February 2024 and 9 January 2024), and quotes the rule that an attachment ceases after one year. It is unchanged at 191.44 in both years with the writ "not concluded". Whether a demand, show-cause notice, interest or penalty is separately pending: NOT FOUND IN DOCUMENT. The 191.44 may therefore understate.
- **Customs item (viii)**: the table's 4.53 equals tax 3.02787 + fine 1.50 only. The note states the order also seeks interest and a penalty equal to the differential duty (Section 114A), which the table excludes ("to the extent of disputed tax demand along with redemption fine"). Small in amount, but the scope of the measure is narrower than the demand.
- **VAT/CST FY25 comparative**: note (vii) says 5.81 CST + 17.35 VAT = 23.16 was due at Mar-2025, but the FY25 table shows 18.16. A 5.00 difference is not explained. FY26 ties: 5.81 + 6.67 = 12.48.
- **Delhi GST 2018-19**: 16.69 was already paid by DRC-03 against an original demand of 30.74; the 28.08 contingent amount is a further order (tax and interest 14.04 + penalty 14.04). Where the 16.69 was booked: NOT FOUND IN DOCUMENT.
- Tie-out passed: note (vi) total 295.26 = Hyderabad 7.79 + WB 42.59 + 16.81 + Maharashtra 202.61 + Delhi 25.46 (derived).

### P2-12. Employee benefits: no provision beyond gratuity; staff cost flat against a 55% revenue rise  🟡
Anchors: SA Notes 16, 21 (AR p.83); SA Note 34 (AR p.86-87); SA Notes 27, 28 (AR p.84); SA Note 2(n) (AR p.78).
- Provisions for employee benefits are 155.08 + 55.74 = 210.82, exactly the gratuity obligation (Note 34). No compensated-absence or leave-encashment obligation is provided or disclosed, and the policy refers to "pensions (in respect of certain employees)" and "other long-term benefits" that do not appear anywhere. A leave provision may exist unprovided; NOT FOUND IN DOCUMENT.
- The gratuity interest cost 11.57 is booked within finance costs ("Others", Note 28), and service cost 20.03 in Note 27; 31.60 in total ties to Note 34.
- Employee cost 1,652.41 (1,581.85) rose 4.5% while revenue rose 55.2%, so staff cost fell from 0.96% to 0.65% of revenue (derived). Salaries rose 3.6% (1,529.47 vs 1,476.84) and the provident fund and other funds contribution fell 25.0% (33.93 vs 45.25). Headcount: NOT FOUND IN DOCUMENT. CON staff cost rose 16.8% on the subsidiaries' +97%.

### P2-13. Hong Kong intangibles of 203.97 bought in FY26 with no description; looser CON amortisation policy  🟡
Anchors: CON Note 4 (AR p.104); SA Note 4 (AR p.80); CON Note 2(d) (AR p.100); SA Note 2(e) (AR p.76); CON cash flow (AR p.98).
- CON intangible additions 441.41 vs SA 237.44; the difference is 203.97, and CON capex of 330.04 less SA 126.07 is also 203.97, so it was paid in cash in FY26 by the subsidiaries. CON net intangibles 406.57 vs SA 212.13 (+194.44); the extra amortisation is 9.53 (4.7% of the cost). Nature of the asset, seller, life, and related-party status: NOT FOUND IN DOCUMENT.
- The CON amortisation policy allows "3 years or useful life of the intangible asset as decided by the management", while the SA policy fixes 3 and 10 years. SA's own 10-year life for customised software (214.64 transferred from CWIP, SA Note 3) is a management choice; a 3-year life would roughly add 50.09 to FY26 amortisation (214.64 / 3 - 214.64 / 10, derived, illustrative).

### P2-14. Honeywell licence cost and commitments are not described  🟡
Anchors: CON Note 29 (AR p.108); SA Note 37 (AR p.89); CON Note 34 (AR p.109); AR p.15-16 (OUTSIDE NOTES narrative).
- CON royalty expense 595.73 (587.55) is 9.1% of the subsidiaries' derived cost base (6,557.79) and 5.6% of CON other expenses; relative to subsidiary net revenue of 14,861.25 it is 4.0% (derived). SA shows only IPR charges of 1.21 (SA Note 37). The AR narrative says the group is an exclusive trademark licensee (AR p.15) and describes SCL as building the "Honeywell trademark licensing business" (AR p.16).
- The notes contain no licence note: term, renewal, minimum guarantee, territory, and royalty rate are NOT FOUND IN DOCUMENT. "Contingencies and Commitments" (Note 35 / CON Note 34) has no commitment line. A licence that underpins the brand business is therefore unquantified in the notes.

### P2-15. Consolidation equity items that do not reconcile  🟡
Anchors: CON Note 14 (AR p.105-106); CON SOCIE (AR p.98); CON balance sheet (AR p.97); SA Note 14 (AR p.82); AOC-1 (AR p.63).
- CON securities premium is 13,166.19 vs SA 12,415.41, a difference of **750.78 in both years** (opening FY25 9,192.99 vs 8,442.21). A parent-only premium account should be the same in CON. The origin of the 750.78 is NOT FOUND IN DOCUMENT.
- NCI 2,366.40 vs 22.5% of SCL equity per AOC-1 (11,845.55 x 22.5% = 2,665.25): a gap of 298.85 (derived). NCI moved only by its profit share (842.15, Pass 1 LB1), so translation reserve is not allocated to it. If part of the 861.98 translation credit belonged to the 22.5% holder, NCI is understated; the notes do not say.
- Label errors: CON Note 14(e) calls the warrant money "Equity Instruments through OCI", and the FY25 CON SOCIE row "Purchase of Shares from Minority (1,015.88)" is in fact the warrant conversion (SA SOCIE, AR p.74). No purchase from minority is shown in CON Note 5.

### P2-16. Segment assets and liabilities do not reconcile to the balance sheet; possible transposed figure  🟡
Anchors: SA Note 39 (AR p.89-90); SA balance sheet (AR p.73); CON Note 37 (AR p.112).
- SA: segment assets 66,633.05 vs total assets 86,311.16, unallocated 19,678.11. Identifiable non-operating items are investments 3,514.61 + cash 475.97 + other bank balances 1,682.15 + other financial assets 15.22 + deferred tax asset 56.26 = 5,744.21. The other **13,933.90** is operating-type (inventory 13,188.06, receivables 55,138.03, other current assets 11,209.21, PPE 819.52, intangibles 212.13 total 80,566.95 vs 66,633.05) yet is not in segment assets. FY25 gap 9,142.40 (derived). Segment liabilities 11,542.84 vs operating liabilities 23,702.77: gap 12,159.93.
- Brand segment liabilities: SA 2,557.66 (364.09); CON FY25 shows (2,558.37), a negative liability. The FY26 SA value and the FY25 CON value are the same size (0.71 apart) with opposite sign and different years. A transposed or mis-keyed figure cannot be ruled out; the notes do not explain the negative.

### P2-17. Movements not commented on anywhere (low significance each)  🟡
Anchors: SA Notes 12, 19, 29 (AR p.82-85).
- Other financial liabilities 1,704.09 (663.15), +157.0%: creditors for expenses 869.47 (328.61) and "Other payables" 834.62 (334.54), the latter unspecified. 77.21 of it is due beyond 12 months despite the current caption (SA Note 32, AR p.86). CON identical (AR p.107).
- Prepaid expenses 195.61 (60.53), +223.2% (SA Note 12). Insurance 76.23 (47.51), +60.4%; CON 116.02 (80.97).
- "Sales Tax / GST Expenses / Income Tax" 46.10 (19.97), +130.8%, a line that includes an "income tax" head inside other expenses; composition NOT FOUND IN DOCUMENT.
- Payables to SCL of 3,093.04 are 15.5% of SA trade payables of 19,963.54 (derived). Other supplier concentration: NOT FOUND IN DOCUMENT.

### P2-18. Related-party disclosure completeness  🟡 (low)
Anchors: SA Note 36 (AR p.88-89); CON Note 35 (AR p.110-111); SA Note 29 (AR p.85).
- Independent-director sitting fees 4.00 (3.60) are an expense (Note 29) but not in the related-party table, though the four independents are listed as KMP.
- FY25 rows show advances given to the associate 70.94, advances received from the associate 96.19, and "advances repaid by World EMS" 67.50. These are loan-type flows with related parties, which sits oddly with the "no funds advanced" statement in SA Note 44(e) (AR p.90). They are FY25 only.
- Rinavaa Technologies payable (91.48) vs (91.50) is static with no FY26 transactions (stale balance).
- Ketan Patel loan roll-forward: 15.68 + 341.61 - 353.74 = 3.55, vs closing 7.59; difference 4.04 (derived), possibly accrued interest, not stated.
- Terms of outstanding balances (secured or not, settlement) and guarantees received from promoters (Notes 15(d), 17(d)) are not in the related-party note: NOT FOUND IN DOCUMENT.

---------------------------------------------------------------------
## C. TIE-OUTS PERFORMED THAT CAME OUT CLEAN (for Pass 3, not findings)
- SA other expenses foot to 4,536.32; SA total expenses 252,308.13 give PBT 4,581.66.
- Current tax liability roll-forward: 95.01 + 1,153.11 - 1,014.27 = 233.85 (SA Note 22 and cash flow); no prior-year true-up.
- Gratuity 31.60 = 20.03 + 11.57; OCI (12.46) = (16.65) + 4.19; deferred tax asset change ties to Note 6 and Note 30.
- SA investing (126.07) = PPE 103.28 + intangibles 237.44 - CWIP transfer 214.64. Dividend 75.08 = 15,016,675 x Re 0.50; Ketan Patel's 42.20 = 8,439,520 x Re 0.50.
- Current ratio 1.45, inventory turnover 22.60, debt-equity 1.08 reproduce (SA Note 43).
- SA current tax 1,153.11 is 25.17% x PBT within 0.1 in both years, with no permanent or timing items in the rate reconciliation (SA Note 30, AR p.85); it is a rate-times-PBT computation, not a reconciliation. Whether CSR 62.00 or the 54.04 allowance was adjusted is not shown.

---------------------------------------------------------------------
## D. LOAD-BEARING FACTS: WHAT PASS 2 CHANGES
- LB1: HK profit at nil tax stays unexplained. Added: the subsidiaries' contribution bridge and cost base (P2-2) and the cash burn (P2-3).
- LB2: CFO (27,188.34 CON / 25,738.12 SA) re-verified; HK share (1,450.22) and the SCL supplier-credit benefit to SA (3,368.03) are new (P2-3).
- LB3: documented brand margin 33.16% CON, 34.57% FY25; SA brand 10.56%. 40-42% not supported (P2-1). It remains possible management quotes a different perimeter.
- LB4: BSNL / BharatNet still absent from the notes; nothing new.
- OUTSIDE NOTES lead (not a finding): AOC-1 shows SCL acquired 21 February 2017 and CPDL 01 June 2017 (AR p.63), so no HK acquisition occurred in FY26. The AR profile of the SCL chief executive is at AR p.16; the notes do not say whether he holds the 22.5%.

---------------------------------------------------------------------
## PASS 2 NEW FINDINGS SUMMARY (new items only)

| # | Finding | Anchor | Rating |
|---|---|---|---|
| P2-1 | Segment result equals gross profit; brand GM 33.16% CON (10.56% SA), not 40-42%; unallocable cost is all opex | SA Note 39 p.89-90; CON Note 37 p.112 | 🟡 |
| P2-2 | HK contribution bridge: GP 10,175.84 - cost 6,557.79 - finance 23.51 = 3,594.54; 57% of HK cost is unnamed-payee reimbursements and royalty | CON Notes 28-29 p.107-108 | 🟡 |
| P2-3 | HK operating cash flow (1,450.22) on profit; cash-flow FX line 702.68 vs HK cash 1,011.37 looks like a plug; SA CFO helped by 3,368.03 SCL credit | CON/SA cash flow p.98/p.74 | 🟡 |
| P2-4 | ROCE 22.01% excludes all borrowings; 10.62% on equity plus debt (13.01% FY25); ROI ratio not reproducible | SA Note 43 p.90 | 🟡 |
| P2-5 | Revenue discount 14.81 (-88.6%) vs audit focus on rebates; commission plus promotion 2,209.06 (+143%) | Note 23.3 p.84; Note 29 p.84-85 | 🟡 |
| P2-6 | Other income 549.71 undisclosed; incentive receivable 518.83 to nil unexplained | Notes 24, 11 p.84, p.81 | 🟡 |
| P2-7 | Incurred-loss wording; allowance static at 22.73 through FY25; 236.66 carries four labels | Note 8 p.81; Note 32 p.86 | 🟡 |
| P2-8 | Critical-estimates list omits ECL, NRV, rebates, SCL control | Note 2(b) p.75, p.99 | 🟡 |
| P2-9 | Covenants referred to in Note 33 but not disclosed; "NBFC/others" lenders; interest to others 252.62 | Notes 33, 17, 28 | 🟡 |
| P2-10 | "Buyers credit expenses" 4,493.48 exceeds total finance cost; label or content wrong | SA Note 37 p.89 | 🟡 |
| P2-11 | DGGI item rests on a Section 83 attachment, conflicting dates; customs measure excludes interest/penalty; VAT FY25 5.00 mismatch | Note 35 p.87-88 | 🟡 |
| P2-12 | Employee provisions equal gratuity only; staff cost +4.5% vs revenue +55.2% | Notes 16, 21, 27, 34 | 🟡 |
| P2-13 | HK intangibles 203.97 bought in FY26, undescribed; CON life policy open-ended | CON Note 4 p.104 | 🟡 |
| P2-14 | Honeywell licence: royalty 595.73, no licence or commitments note | CON Note 29 p.108 | 🟡 |
| P2-15 | CON share premium +750.78 over SA; NCI 298.85 below 22.5% of SCL equity; mislabelled reserve rows | CON Note 14 p.105-106 | 🟡 |
| P2-16 | Segment assets omit 13,933.90 of operating assets; brand liability sign/transposition question | SA Note 39 p.89-90; CON Note 37 p.112 | 🟡 |
| P2-17 | Uncommented movements: other financial liabilities +157%, prepaid +223%, SCL 15.5% of payables | Notes 12, 19, 29 | 🟡 |
| P2-18 | RPT completeness: sitting fees, FY25 related-party advances, stale balance, loan roll gap 4.04 | Note 36 p.88-89 | 🟡 |

New finding count: 18. Corrections to Pass 1: 4 (C1 to C4).
