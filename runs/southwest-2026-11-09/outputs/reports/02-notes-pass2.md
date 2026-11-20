# STAGE 2 NOTES PASS 2 (WHAT WAS MISSED): SOUTHWEST, FY26 (year ended 31 Mar 2026)

Run date 2026-11-09. Source: inputs/annual-report/Annual_Report_2026.txt. Model: claude-sonnet-5-5.

## 0. Conventions

- Unit on the face of the document: INR Lakhs ("All amounts in INR Lakhs", S p.127, C p.169). Nothing is converted. The two announcement figures in P2-17 are printed in rupees and I say so.
- Anchors follow Pass 1: "S" = standalone note and page, "C" = consolidated note and page, page = the "[page N]" marker in the .txt.
- "(derived)" = my arithmetic on anchored figures. "[INFERENCE]" = reading beyond the printed number. "NOT FOUND IN DOCUMENT" = expected disclosure absent.
- Method: I re-read standalone Notes 1-66 (S pp.116-157), the consolidated auditor's report and primary statements (C pp.159-168), and consolidated Notes 1-65 (C pp.169-203) from the start, against Pass 1. Items Pass 1 covered fully are skipped. Pass 1 text that I corrected is listed in Section A.
- Rating key: GREEN / YELLOW / RED.

## A. Corrections to Pass 1 (anchor and reading fixes, not new findings)

1. Pass 1 Section 11 cites the FY25 stock-in-trade purchase 4,490.92 as "Note 35 S p.137". It is Note 34 S (p.137); Note 35 S is Operating Expenses. Figure unchanged.
2. Pass 1 Section 2e calls SWR (Pilot Pipelines) loss-making in tone ("accumulated losses of 314.88"). The accumulated loss is right, but SWR earned profit of 76.82 in FY26 (PY 28.44) and its net assets moved from (341.77) to (264.94) (Note 52 C p.202). See P2-1.
3. Pass 1 left three RPT cells as "col?" (Note 48 S p.148). The consolidated table (Note 49 C p.194) resolves them: sale of service of 241.97 in FY25 was to the jointly controlled entity, nil in FY26; purchase of geological and 2D seismic services of 45.41 (PY 445.03) is from the jointly controlled entity. The FY26 sale of service 282.92 and purchase of drilling 632.01 sit in the subsidiaries column in the standalone table. See P2-5.

## B. NEW FINDINGS

### P2-1. SWR is a profitable pass-through intermediary, not a pure loss-maker (YELLOW)

- Group Schedule III: Pilot Pipelines Pvt Ltd (SWR) profit 76.82 (PY 28.44); net assets (264.94) (PY (341.77)) (Note 52 C p.202). The deficit narrows by about the year's profit (76.83 derived).
- Auditor's paragraph: accumulated losses 314.88, current liabilities exceed current assets by 266.40, going-concern basis "as the Company has letter of financial support from Holding Company" (Auditor's report C p.159). The letter of financial support is not quantified in any note, in Note 42 contingent liabilities (C pp.185-186), or in the RPT note. Amount and terms: NOT FOUND IN DOCUMENT.
- Consolidated employee cost equals standalone exactly: 3,570.88 in both (Note 37 C p.183; Note 36 S p.138). Consolidated cost of materials equals standalone: 3,658.63 in both (Note 34 C p.183). So the subsidiaries carry no employees and no stores consumption. Consolidated sub-contract cost 8,043.00 against standalone 8,109.98 (Note 36 C p.183; Note 35 S p.137), a difference of 66.98. Total operating expenses differ by 66.53 (10,407.30 vs 10,340.77; derived).
- [INFERENCE] The group removes only 66.53 of operating cost on consolidation against 632.01 that the parent paid a subsidiary for drilling services (Note 48 S p.148). That fits a subsidiary that buys most of the work from outside and resells it to the parent at a markup of about 66.53, or 10.5% of 632.01 (derived). The confirming observation is SWR's own cost split, which is not in this AR.
- Consequence for the loan: the parent lends SWR 410.34 (Note 15 S p.131; 431.44 in the RPT table, Note 48 S p.148). The RPT table shows no interest on loans to subsidiaries in FY26 or FY25 (Note 48 S p.148, "Interest on Loans & Advances" subsidiary cell "-"). Interest rate on the SWR loan: nil as printed. Each 1% on 410.34 is 4.10 a year; 8.00% (the low end of the company's own stated borrowing range, Note 25 S p.135) is 32.83 (derived arithmetic, not a disclosed number). No Ind AS 109 fair-value discount on the interest-free loan is disclosed.
- Total standalone exposure to SWR: loan and other balances 431.44 + trade debtors 130.24 + investment at cost 42.38 = 604.06 (derived; Note 48 S p.148; Note 7 S p.129) against SWR net assets (264.94). Payables to subsidiaries are 450.17 (Note 48 S p.148); whether the group may set one against the other: NOT FOUND IN DOCUMENT.

### P2-2. Related-party "Other receivables" in Note 16 reconcile exactly to the RPT balance table (YELLOW)

- RPT "Loans & Advances (Asset)" balances: 431.44 + 293.48 + 0.19 = 725.11 (Note 48 S p.148). Notes 8 and 15 loans to related parties total 257.86 + 410.34 = 668.20 (S pp.130-131). The gap 725.11 − 668.20 = 56.91 equals Note 16 S "Other Receivables" of 56.91 (S p.132) exactly (derived).
- Consolidated cross-check: Note 16 C "Other Receivables" 35.62 (C p.178) equals RPT jointly controlled entity loans 293.48 less Note 8 non-current 257.86 = 35.62 (derived).
- So all of "Other receivables" 56.91 (PY 20.10, +183%; S p.132) are related-party balances. They were presented as ordinary other financial assets, not as loans to related parties, and carry no stated interest or tenor.
- Total related-party financial exposure on the standalone balance sheet: loans 668.20 + other receivables 56.91 + trade debtors 130.24 = 855.35, or 4.2% of standalone equity 20,251.42 (Note 49c S p.153; derived). Pass 1 stated 668.20 (3.3%).

### P2-3. Trade receivable allowance covers the old tail only (YELLOW)

- Allowance 187.95 (Note 12 S p.131). Balances aged over one year: 16.21 (2-3 years) + 173.13 (over 3 years) = 189.34. Allowance is 99.3% of that tail (derived). Residual allowance against the other 11,643.12 of gross receivables: negative 1.39 (derived), meaning the matrix leaves essentially no allowance on current and under-one-year balances.
- FY25: allowance 100.78 against over-one-year balances 131.90 + 173.14 = 305.04, or 33.0% (derived).
- 1-2 year bucket fell from 131.90 (FY25) to nil (FY26), and the 2-3 year bucket fell from 173.14 to 16.21 (S p.131). The two prior-year balances left the ageing: 115.69 gone from the 1-3 year buckets after roll-forward (131.90 − 16.21; derived). Whether they were collected or written off: NOT FOUND IN DOCUMENT. The ECL note shows no write-off (Pass 1 Section 4b).
- The over-3-year 173.13 is the same sum as the FY25 2-3 year 173.14, frozen for a year.
- Group FY25 ageing was larger than standalone (7,735.28 vs 7,534.67; C p.178 vs S p.131) and the group booked "Bad debt written off 119.32" in FY25 with nil in FY26 (Note 40 C p.184). This line is absent from the standalone Note 39 (S p.138), so it sat in a subsidiary. Debtor and customer: NOT FOUND IN DOCUMENT.

### P2-4. Jointly controlled entity classification: Samit JV and equity-method carrying (YELLOW)

- South West Samit JV: 80% held, accounted by equity method as a jointly controlled entity (Note 7 S p.129; Note 51 C p.201). An 80% holding is normally a control test. The judgement behind JV classification, and the other 20% holder: NOT FOUND IN DOCUMENT.
- Samit total income FY26 45.41 (PY 8.32) (Note 51 C p.201). The parent's purchase from the jointly controlled entity is 45.41 (Note 49 C p.194). The two figures match exactly (derived). [INFERENCE] Samit's revenue in FY26 is wholly the parent's spend.
- Samit net assets (13.51) (PY 39.99); loss (17.71); group share (14.17) (Note 51 C p.201). Group carrying 10.70 is positive (Note 7 C p.176; Note 52 C p.202 shows 10.62 net assets contribution). 80% of (13.51) is (10.81) (derived). Positive carrying against negative investee net assets: reconciling item NOT FOUND IN DOCUMENT. The equity-method policy says losses stop at the investment (Note 1(c)(2) C p.171), and the group still reports a loss share of 14.17.
- Alara Resources LLC carrying 500.97 against 35% of net assets 414.69 (Pass 1). FY25 gap was 339.90 less 219.59 (35% x 627.40) = 120.31 (derived; Note 50 C p.200). The gap fell 120.31 to 86.28 but a premium over share of net assets is not explained by any goodwill or fair-value disclosure (policy says goodwill sits inside carrying, C p.171).
- Alara LLC net assets rose 557.43 (1,184.83 vs 627.40) against profit 460.20, so 97.23 of net-asset growth is not profit (derived; OCI stated nil). Capital contribution or other movement: NOT FOUND IN DOCUMENT.
- Auditor: the 146.90 group share of JV net income "unaudited" and "furnished by management" (Auditor's report C p.161). This is 4.4% of group profit after tax 3,302.70 (derived; C p.167). The group share of Alara LLC (161.07) is non-cash to date (Pass 1).

### P2-5. Omani JV trading with the parent collapsed (YELLOW)

- Parent sales of services to the jointly controlled entity: nil in FY26, 241.97 in FY25. Purchases of geological and 2D seismic services from the entity: 45.41 (PY 445.03) (Note 49 C p.194). Combined trade moved from 687.00 (derived) to 45.41, down 93.4% (derived).
- Alara LLC third-party and own activity grew (total income 14,960.25 vs 6,444.12, Pass 1). Parent-linked trade fell as the JV scaled. Reason: NOT FOUND IN DOCUMENT.
- Payables to the jointly controlled entity at year end 85.89 (PY 151.75) (Note 48 S p.148) against FY26 purchases of 45.41. Balance exceeds the year's purchases by 40.48 (derived). It reflects the FY25 purchases of 445.03 not yet cleared.
- Interest on loans to the jointly controlled entity 11.42 on average loans of 198.58 = 5.75% (derived: average of RPT loan balances 293.48 and 103.67, Note 48 S p.148). The Omani loan sits in OMR (Note 8 S p.130; Note 49 S p.152). Rate and tenor: NOT FOUND IN DOCUMENT.

### P2-6. Depreciation did not yet absorb the rig additions (YELLOW)

- Plant and equipment additions 3,900.25 (Note 2 S p.127). Plant depreciation 930.74 (PY 780.24), an increase of 150.50 (derived) or 3.86% of additions (derived). Gross plant block +31.9% (11,194.64 to 14,767.83; derived); net plant block +47.3% (Pass 1).
- Dates of the additions and the "put to use" dates: NOT FOUND IN DOCUMENT. Useful life per class: NOT FOUND IN DOCUMENT (Pass 1). Depreciation method is written down value over Schedule II lives (Note 1(e)(iv) S p.118).
- Consequence for later stages: FY26 depreciation (Note 38 S p.138, 1,144.33) carries a part year of this block. Capital commitments of 1,720.64 and capital advances of 226.11 remain (Note 42B C p.185; Note 10 S p.130). I do not estimate FY27 depreciation.

### P2-7. Margin-money deposits fell sharply against non-fund limits (YELLOW)

- Non-fund utilisation = availed limits 6,510.62 less fund-based CC, WCDL, overdraft 4,237.05 = 2,273.57 (derived; Note 42C C p.186; Note 25 S p.135). FY25: 5,750.50 less 3,496.30 = 2,254.20 (derived). These tie to bank guarantees: 2,250.08 (PY 2,253.79) (Note 42A C p.185).
- Fixed deposits held as margin money: current 1,042.52 + non-current 348.05 = 1,390.57 (PY 2,157.36 + 71.96 = 2,229.32) (Note 14 S p.131; Note 9 S p.130).
- Margin cover of non-fund limits: 61.2% (FY26) against 98.9% (FY25) (derived).
- Reading: banks now hold about 38 points less cash margin per rupee of guarantee. The fixed deposits that were released fed the cash outflow (Investment in fixed deposits (net) +838.75 in the consolidated cash flow, C p.168). The bank margin terms and any rise in uncovered guarantee exposure: NOT FOUND IN DOCUMENT.
- Any further guarantee growth now needs less cash margin than before. If banks lift the margin ask, the release reverses. This ties to Pass 1 Finding 1 (cash conversion).

### P2-8. Quoted versus unquoted classification of "Investment others" 69.85 conflicts (YELLOW)

- Note 7 S lists "Investment others 69.85 (PY 162.53)" under "Investment in equity instruments (Unquoted)" and states aggregate unquoted investments 265.63 and aggregate quoted 274.76 (S p.129). 265.63 includes the 69.85 (42.38 + 0.74 + 1.00 + 111.66 + 0.08 + 39.92 + 69.85; derived).
- Note 49 S treats 344.61 (= 69.85 + 274.76) as "Investment at Level 1", meaning quoted prices (S p.149, p.150). Level 1 and "unquoted" cannot both be true for 69.85.
- The equity statement labels the OCI reserve "Gain on account of fair valuation of mutual fund" (S p.126). The nature of the 69.85 (mutual fund, equity, bond): NOT FOUND IN DOCUMENT.
- The cash flow shows "Proceeds from investments 92.68" in FY26 (C p.168). That equals the fall in "Investment others" 162.53 − 69.85 = 92.68 (derived). So the reduction was a sale or redemption. Realised gain or loss on that sale: NOT FOUND IN DOCUMENT.

### P2-9. Financing of the capex wave: working-capital lines up while borrowings are said to be "applied for the purposes" (YELLOW)

- Note 62 S: "borrowings obtained ... have been applied for the purposes for which such loans were taken" (S p.155).
- Cash flow FY26: proceeds from long-term borrowings 2,908.66, repayment 2,079.48, short-term borrowings net +740.76 (C p.168). Capital outflows: PPE 4,254.31, E&E 499.77, investment in JV 39.92, other companies 288.00, loans to JV 166.77 (C p.168).
- [INFERENCE] Cash collected from operations (consolidated CFO 1,244.88) did not cover the capex. The gap was met by FD release 838.75, cash drawdown 1,814.67 and a rise of 740.76 in short-term working-capital lines. Working-capital lines are secured on stock and book debts (Note 25 S p.135). Part of the rig funding therefore sits on short-term lines. The note does not split the term loan use against specific assets.
- Net debt definition conflict: "Net debt includes interest bearing loans and borrowings less cash and cash equivalents" (Note 49c S p.153) but the table also deducts "Bank balances other than above" 1,042.52 (margin money), giving 6,730.01. Following the stated definition gives 7,772.53 (derived; Pass 1 has this figure) and gearing 38.4% against the printed 33.23% (derived: 7,772.53 / 20,251.42). The same note says capital is managed to "the requirements of the financial covenants". Covenant terms stay NOT FOUND IN DOCUMENT, but the note confirms covenants exist.

### P2-10. Note 18 / 19 shareholding table internal conflict and warrant status (YELLOW; GREEN on outcome)

- Note 18(a) S shows Vikas Jain 42.36% and Piyush Jain 24.80% at 31 Mar 2025 (S p.132). Note 18(e) S shows 39.62% and 23.20% at the same date (S p.133). The consolidated Note 19 shows 39.62% and 23.20% for both dates (C p.179). The 42.36% and 24.80% match the pre-issue share count of 2,79,02,400 (1,18,18,922 / 2,79,02,400 = 42.36%; derived). The FY25 column in Note 18(a) S is stale.
- Warrants: 28,21,411 warrants, exercise window 18 months from 21 Feb 2025 (S p.134). Last date is 21 Aug 2026 (derived). The notes carry no subsequent-event note (Pass 1). Outside the notes: the company announced on 10 Jul 2026 the allotment of 2821411 equity shares on conversion of all 28,21,411 warrants against balance consideration of Rs 279742900 (rupees, equal to 2,797.43 Lakhs) and post-allotment capital of 3,26,51,422 shares (inputs/announcements/20260710-ccf0bac3-c591-45b9-9b2a-14d3416eb46b.txt, lines 37-43, 70). The identified equity inflow of 2,797.43 therefore arrived after the balance sheet date. Full-conversion dilution is 28,21,411 / 2,98,30,011 = 9.46% (derived), against the 2.3% EPS dilution gap in Note 40 S (Pass 1). Pending verification at the announcements stage.
- Also outside the notes: a SAST Regulation 29(2) filing says the promoter group had an acquisition on warrant conversion and "disposal of shares through open market on June 29, 2026 and June 30, 2026" (inputs/announcements/20260813-9C8BA238_258A_4D8E_AF3F_091E7305550B_101032.txt, lines 75-78). Quantities and sellers: not read here; flagged for the announcements and shareholding work. The notes say nothing on this: NOT FOUND IN DOCUMENT.

### P2-11. Cash is mostly physical currency in the group (YELLOW)

- Cash and cash equivalents standalone 88.81: cash on hand 51.30, current account balances 36.21, earmarked 1.30 (Note 13 S p.131). Cash on hand is 57.8% of the line (derived). FY25: cash on hand 37.64 of 1,824.50 (2.1%; the rest was a 1,745.25 short deposit).
- Group cash 129.40: cash on hand 79.78 (PY 41.12), current accounts 48.32 (PY 156.41) (Note 13 C p.178). Cash on hand is 61.7% of group cash (derived). Subsidiaries hold 28.48 of it (79.78 − 51.30; PY 3.48; derived) while their combined profit before tax is small (Note 52 C p.202).
- Business reason for holding cash on hand at this size: NOT FOUND IN DOCUMENT. Audit-trail and cash-count assurance: NOT FOUND IN DOCUMENT.

### P2-12. P&L lines that moved without explanation (YELLOW, minor each)

All S p.138 (Note 39 other expenses, Note 37 finance costs); FY26 vs FY25 in INR Lakhs.

| Line | FY26 | FY25 | Change (derived) |
|---|---|---|---|
| Cost of travel and local conveyance | 216.34 | 80.12 | +170% |
| Bank charges | 19.29 | 5.58 | +246% |
| Interest on taxes, demands and penalties | 16.87 | 8.27 | +104% (group FY25 12.07, C p.184) |
| Business development expenses | 46.76 | 19.18 | +144% |
| Insurance charges | 68.63 | 41.26 | +66% |
| Other borrowing costs (finance cost) | 64.89 | 45.06 | +44% |
| Fooding cost (Note 35 S p.137) | 498.00 | 329.44 | +51% |
| Total other expenses | 897.33 | 520.57 | +72% (revenue +35.6%) |

- Cost build ties: revenue 24,292.95 + other income 358.66 less the expense notes gives PBT 4,130.80 (derived: 24,651.61 − 20,520.81), which matches Note 44 S p.141. FY25 ties to 1,977.76.
- Interest on tax demands and penalties doubling fits the rise in disputed demands (GST 397.59 new, Pass 1 Section 3). Tax demand status and amounts already paid under protest: NOT FOUND IN DOCUMENT.
- Director sitting fees: Note 39 S shows 3.12 (PY 4.28) (S p.138). The KMP compensation note shows sitting fee 4.80 (PY 6.58) (S p.149). The gap is 1.68 (PY 2.30; derived). The compensation note covers "KMP and their relative" so a relative's fee or a GST element may explain it. Not stated.

### P2-13. Consolidated tax equals standalone tax although subsidiaries made profit (YELLOW, minor)

- Group tax expense 1,050.75 equals standalone 1,050.75 (Note 45 C p.187; Note 44 S p.141). Group profit before tax and JV share 4,206.55 exceeds standalone 4,130.80 by 75.75 (derived).
- The group reconciliation carries "Other Adjustments (18.42)" (C p.187). 75.75 x 25.17% = 19.07 (derived), so the adjustment is about the tax that the subsidiary profit would have attracted. The deferred tax line (40.49) is identical in both sets. [INFERENCE] SWR's profit is shielded by brought-forward losses and no deferred tax asset is recognised on them. Unrecognised deferred tax asset and expiry profile: NOT FOUND IN DOCUMENT (Pass 1).
- Group taxes paid 676.75 against standalone 655.17 (C p.168 vs S p.115, per Pass 1), 21.58 more; group current tax assets are 38.66 (PY 17.07) (Note 17 C p.178). So a subsidiary holds a net tax receivable.
- Standalone current tax payable 561.35 ties: opening 125.28 + current tax 1,091.24 − taxes paid 655.17 = 561.35 (derived). No unusual gap.

### P2-14. Deferred tax "Other" balances without description (YELLOW, minor)

- DTL "Other" 110.32 (PY 106.33) and DTL on "Other Comprehensive Income" 49.21 (PY 50.02) (Note 44 S p.141). Together 159.53, or 25.0% of gross DTL 638.09 (derived). The nature of the "Other" DTL: NOT FOUND IN DOCUMENT.
- OCI reserve is 105.45 (Note 19 S p.133). A DTL of 49.21 against a reserve of 105.45 implies a tax rate of 31.8% on the pre-tax gain (49.21 / (105.45 + 49.21); derived), above the applicable 25.17%. The OCI reserve holds the cumulative FVOCI gain, mostly on the older investments (Note 19 S p.133). The deferred tax rate applied to equity gains: NOT FOUND IN DOCUMENT.

### P2-15. Employee benefit fine print (YELLOW, minor)

- Retirement age assumption moved to "60 & 72 yrs" from "60 & 70 yrs" (Note 45 S p.145). No comment on the change or its P&L effect.
- Experience loss on the gratuity obligation 20.86 (PY 14.98) (Note 45 S p.142), 10.4% of opening obligation 200.05 (derived), while the demographic assumption of 2.68% attrition is held flat. Gain on financial assumptions (17.59) came from a discount-rate rise from 6.89% to 7.78% (S p.142). Net OCI loss is only 3.23 because the two offset. A reversal in the discount rate would show the real size.
- Leave data: "Total Salary (Encashment) 303.91" (PY 207.16) for 802 (PY 558) employees, average 0.38 (S p.145). The 0.38 average suggests a monthly basis (derived: 303.91 / 802). On that reading year-end payroll run-rate is 303.91 x 12 = 3,646.92 against FY26 salaries and wages 3,283.86 (Note 36 S p.138), 11.1% higher (derived). FY25 equivalent: 2,485.92 vs 2,503.67 (99%; derived). The monthly basis is my reading, not stated in the note.
- Average past service 2.90 years (PY 3.84) (S p.145): the workforce is young in tenure. Gratuity vests at five years (S p.142), so most employees have not yet vested.

### P2-16. Disclosure hygiene: stale labels and cross-note mismatches (YELLOW, minor; Pass 3 will weigh them together)

- Interest-rate sensitivity table columns read "year ended March 31, 2025 / March 31, 2024" for the 33.65 and 25.54 effects (Note 49 S p.153; Note 50 C p.199). They belong to FY26 and FY25. The consolidated market-risk text also says positions are as of "March 31, 2025 and March 31, 2024" (C p.198). 33.65 = 0.5% x 6,729.13 (derived), which confirms the FY26 base.
- Foreign-currency table: consolidated FY25 OMR asset 1.16 million against 91.09 INR (C p.198); standalone FY25 shows 0.41 million against the same 91.09 (S p.152). Only one can be right. Consolidated sensitivity table lists "AUD/INR" for a liability that the exposure table shows as EURO (C p.199).
- Lease maturity table: "Total undiscounted lease liabilities" 152.37 equals the discounted carrying amount 152.37 (Note 42 S p.140; Note 43 C p.186). An undiscounted total must exceed the carrying amount. Annual lease cash outflow is 37.95 (S p.140). The table is the carrying amount relabelled.
- Consolidated Note 20 total prints "17,079.98" for FY25 other equity while the sum and the balance sheet read 14,079.98 (C p.179; C p.166).
- Note 63 S refers to "notes 7, 26 and 48" for s.186(4) disclosures (S p.155). Note 26 S is Trade Payables. Guarantees given for others: NOT FOUND IN DOCUMENT (Pass 1 Section 3).
- Management commentary under Note 51 S: ROCE improved "without corresponding increase in capital employed" (S p.154). Group borrowings rose 24.9% (Pass 1), net PPE rose 46.9% (9,177.91 vs 6,250.13; derived) and equity rose 17.9% (20,251.42 vs 17,184.00; derived). The statement is not supported by the balance sheet movements. The payables commentary conflict is in Pass 1.

### P2-17. E&E spend profile by vintage (informational, YELLOW)

- The E&E ageing rolled between years gives the spend by year (Note 5 S p.129): at 31 Mar 2025 the 2-3 year bucket held 757.73 and the over-3-year bucket was nil. At 31 Mar 2026 the over-3-year bucket holds 757.73 (the same sum). Spend by year therefore reads: FY23 757.73; FY24 324.17; FY25 348.91; FY26 499.77; total 1,930.58 (derived from the two ageing tables; vintage labels are my reading of the buckets).
- Nothing was spent before FY23 although the block was "allocated in 2021-22" (Note 1 S p.116). FY26 spend rose 43.2% on FY25 (derived). The asset is 9.5% of standalone equity (1,930.58 / 20,251.42; derived).
- The cash outflow of 499.77 is investing activity (C p.168). The company reports "PL cum ML process is presently underway" (Note 1 S p.116). No disclosed milestone for the mining lease, and no reserve-quality status: NOT FOUND IN DOCUMENT. This strengthens the Pass 1 point that the E&E asset has no stated impairment trigger.

### P2-18. Auditor's report items that bear on the notes (YELLOW)

- CARO 2020 remarks: South West Oil Field Services Pvt Ltd and South West Geo Services Pvt Ltd are listed as subsidiaries with "Clause number of the CARO report which is qualified or adverse: xvii" (Auditor's report C p.162, table before the C p.163 marker). Clause xvii is the cash-loss reporting clause. SWOFS has made losses in both years (0.64 and 0.20; Note 52 C p.202) and SWGS lost 0.50. Both losses are tiny in amount; the point is that two of three subsidiaries are loss-making and one is in going-concern doubt.
- Key audit matter is revenue recognised "for the completed performance obligation which is part of incomplete contract ... based on the stage of completion" (Auditor's report C pp.159-160). The policy note describes recognition "with reference to the performance of each service in a particular month" (Note 1(c) S p.117) and unbilled revenue as services earned with "no enforceable claim" (S p.117). The KAM describes stage-of-completion judgement on unbilled work of 2,613.79 (Note 12 S p.131). The policy note does not mention the stage-of-completion method, input measure or allocation of transaction price. Estimation inputs: NOT FOUND IN DOCUMENT.
- Section 197 managerial remuneration: the auditor reports it is "in accordance with the provisions of Section 197 read with Schedule V" (Auditor's report C p.163). This answers the Pass 1 remuneration worry in part (GREEN). Remuneration up 75.2% remains a fact (Pass 1).

## C. Items re-checked and clean (not new findings; stated so the verifier knows they were read)

- Note 2 PPE roll-forward: gross 12,606.49 + additions 4,281.38 − disposals 447.86 = 16,440.01; accumulated 6,356.36 + 1,091.49 − 185.74 = 7,262.10; net 9,177.91 (S p.127). Depreciation 1,091.49 = Note 38 PPE 1,089.92 + leasehold land 1.57 (S p.138).
- Note 4 investment property, Note 6 ROU roll-forward, Note 13 and 14 balances, Note 20 repayment totals (2,024.84 = 1,937.06 + 87.79), Note 26 payables ageing totals (S p.136) all foot.
- Note 45 balance-sheet reconciliation: 199.40 + 47.10 + 3.23 − 40.00 = 209.73 (S p.144). Leave encashment liabilities tie to Notes 22 and 28: 19.30 + 4.43 = 23.73 (S pp.135-136).
- Non-current segment assets 11,752.46 = PPE 9,177.91 + CWIP 40.42 + E&E 1,930.58 + other non-current assets 230.82 + investment property 257.85 + ROU 114.88 (derived; Note 46 S p.146). Consolidated 11,763.67 differs by goodwill 11.21 (C p.192; derived).
- CSR carry-forward: PY opening 2.02 + 24.80 − 27.69 = closing 4.91 (S p.146; derived).
- Schedule III net assets add to 20,352.94 (Note 52 C p.202; derived).
- Rights and bonus issue history, warrants count and price: 19,27,611 x 132.20 = 2,548.30 and 28,21,411 x 132.20 = 3,729.91 (derived; S p.132, p.134).
- Notes 53 to 62 S (benami, wilful defaulter, struck-off companies, ROC charges, layers, crypto, undisclosed income): all "nil / none" statements. Note 54: the quarterly statements filed with banks agree with books (S p.155). This is a representation; the bank-statement reconciliation is NOT FOUND IN DOCUMENT.

## PASS 2 NEW FINDINGS SUMMARY (new items only)

| # | Finding | Anchor | Rating |
|---|---|---|---|
| P2-1 | SWR earns 76.82 (PY 28.44) yet has net assets (264.94); consolidation removes only 66.53 of cost against 632.01 bought from subsidiaries (implied markup about 10.5%, inference); loan to SWR carries no interest; financial-support letter from parent is unquantified; total standalone exposure 604.06 | Note 52 C p.202; Auditor C p.159; Note 48 S p.148; Notes 34-37 | YELLOW (RED for opacity of the support letter) |
| P2-2 | All of Note 16 "Other receivables" 56.91 (PY 20.10) are related-party balances; total related-party financial exposure 855.35 = 4.2% of equity | Note 16 S p.132; Note 48 S p.148 | YELLOW |
| P2-3 | ECL allowance 187.95 equals the over-one-year tail 189.34; nothing provided on 11,643.12 of other receivables; 115.69 of older balances left the ageing without explanation | Note 12 S p.131 | YELLOW |
| P2-4 | Samit JV: 80% holding treated as JV, revenue equals parent's spend 45.41, positive carrying against negative net assets (13.51); 146.90 JV profit share unaudited | Note 51 C p.201; Auditor C p.161 | YELLOW |
| P2-5 | Parent trade with Omani JV fell from 687.00 to 45.41 (-93.4%) | Note 49 C p.194 | YELLOW |
| P2-6 | Depreciation rose 150.50 on 3,900.25 plant additions; FY26 carries a part year only | Note 2 S p.127 | YELLOW |
| P2-7 | Margin-money cover of guarantees fell from 98.9% to 61.2%; FD release funded capex | Notes 9, 14, 25, 42 | YELLOW |
| P2-8 | "Investment others" 69.85 is both unquoted (Note 7) and Level 1 (Note 49); 92.68 sold in FY26 | Note 7 S p.129; Note 49 S p.149; CF C p.168 | YELLOW |
| P2-9 | Working-capital lines +740.76 helped fund capex; net debt definition in Note 49c conflicts with its own calculation (gearing 38.4% on the stated definition vs 33.23%) | Note 49c S p.153; CF C p.168 | YELLOW |
| P2-10 | Warrants all converted 10 Jul 2026 (2,797.43 inflow); full dilution 9.46%; promoter-group open-market disposals on 29-30 Jun 2026; no subsequent-event note | Note 19 S p.134; announcements | YELLOW (pending verification) |
| P2-11 | Cash on hand is 61.7% of group cash (79.78 of 129.40), subsidiaries hold 28.48 | Note 13 C p.178 | YELLOW |
| P2-12 | Travel +170%, bank charges +246%, tax-demand interest +104%, other expenses +72% | Note 39 S p.138 | YELLOW |
| P2-13 | Group tax equals standalone tax; subsidiary profit shielded, unrecognised DTA not disclosed | Note 45 C p.187 | YELLOW (minor) |
| P2-14 | DTL "Other" 110.32 and OCI DTL 49.21 undescribed (25% of gross DTL) | Note 44 S p.141 | YELLOW (minor) |
| P2-15 | Retirement age 70 to 72; experience loss 20.86; year-end payroll run-rate about 11% above FY26 expense (monthly-basis reading) | Note 45 S pp.142-145 | YELLOW (minor) |
| P2-16 | Stale labels and mismatches: sensitivity years, OMR FY25, lease "undiscounted" table, equity-total typo, Note 63 cross-reference, ROCE commentary | S p.140, p.152-155; C p.179, p.198-199 | YELLOW (minor) |
| P2-17 | E&E spend by vintage FY23 757.73 to FY26 499.77; nothing before FY23; no lease milestone | Note 5 S p.129 | YELLOW |
| P2-18 | CARO xvii remarks on two subsidiaries; KAM on stage-of-completion not matched by policy text; s.197 compliance confirmed | Auditor C pp.159-163 | YELLOW / GREEN |

No finding in this pass rises above the Pass 1 top three. P2-1 adds to Pass 1 Finding 3 (SWR); P2-7 and P2-9 add to Pass 1 Finding 1 (cash conversion under rig capex); P2-3 adds to Pass 1 Finding 1 on receivable quality.
