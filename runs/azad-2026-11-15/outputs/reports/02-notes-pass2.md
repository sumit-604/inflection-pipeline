# Stage 2, Notes to Financial Statements, PASS 2 (what was missed)
Company: AZAD (Azad Engineering Ltd). Run date: 2026-11-15. Model: claude-sonnet-5-5.

Source: Annual_Report_2026.pdf (FY2025-26). Anchors are PDF page markers, "[page N]". Printed folio = PDF page minus 3. The text extraction puts the "[page N]" marker at the START of page N. Annual_Report_2025 is comparison only.
UNIT: INR million (Rs Mn) throughout, as printed ("All amounts are C in millions", e.g. [page 172]). No figure is converted. "[calc]" = my arithmetic on printed figures. "[INFERENCE]" = my reading, not filed text.
Method: Pass 1 report read in full with the ERRATA. Notes re-read from Note 1 on both sets. The standalone notes (pp.145-182) were read against the consolidated notes (pp.196-252). Only items Pass 1 did not close are listed. Items Pass 1 covered fully are skipped.
B00 input_gaps carried: QIP placement document not collected; five screener formula sheets absent; research/ empty. None blocks this pass.

## A. PASS 1 CARRY-FORWARD ITEMS, CLOSED OR CONFIRMED

| Carry-forward item | Result |
|---|---|
| ECL matrix rates | NOT FOUND IN DOCUMENT in the standalone (Credit risk note, [page 172]) or consolidated notes (Note 34, [page 242]). Both name a provision matrix "based on days past due ... by geographical region, product type, customer type and rating" and print no rate. See B1 for the coverage ratios that can be built. |
| Inventory write-down amount | NOT FOUND IN DOCUMENT. Standalone Note 9 ([page 148]) shows only the three-line category table, "lower of cost and net realisable value". No write-down line sits in standalone Note 29 ([page 160-161]) or consolidated Note 27 ([page 231-232]). Policy: provision for obsolescence "basis the management's estimate, based on demand and market" (Note 2E). CARO clause ii(a) says physical-verification discrepancies were under 10% of each class, no amount ([page 115]). |
| Composition of government balances 1,102.51 | NOT FOUND IN DOCUMENT. Standalone Note 12 ([page 151]) shows the same single line (1,082.25 vs 526.33). The only split in any note is the non-current "balance with statutory authorities - deposits" 56.57 vs 50.65 (Note 6, [page 220]). No GST, IGST, ITC or duty-credit wording appears in the notes. See B2 for what the balance does to the cash story. |
| Forward-contract disclosure | No forward contract, hedge or derivative asset is disclosed in the standalone or consolidated notes. The only derivative is the Azad Prime put/call (Pass 1). Policy statement sits outside the notes: "Foreign exchange exposure is covered by entering into forward contracts only if it is beneficial and/or favourable" (Corporate Governance report, [page 72]). See B3. |
| Factoring or bill-discounting wording | Re-checked in the standalone notes and policy (Note 2, financial instruments, derecognition) and in the consolidated Notes 13 and 14. No factoring, bill discounting, recourse or supply-chain-finance wording in either set. The WC lines are "working capital demand loan ... repayable on demand" (consortium UBI 491.82, IndusInd 385.66, ICICI 298.23, plus VTC 17.56; Note 14, [pages 226-227]). WC funding therefore shows as on-balance-sheet bank debt, up 144% (Pass 1). The notes give no sign that discounted receivables sit off balance sheet [INFERENCE from silence; silence is not evidence]. |
| Standalone top-5 customer definition | CLOSED. See B4. |

## B. NEW FINDINGS

### B1. Receivable provisioning coverage fell while the old bucket grew (Note 8 / Note 34; [pages 220-221, 242]) RATING YELLOW
Pass 1 gave the allowance (89.93) and its cover of the over-one-year balance (56.3%). It did not give the prior-year comparison or the policy link. All Rs Mn, consolidated, [calc]:
| Measure | FY26 | FY25 |
|---|---|---|
| Allowance / gross receivables | 89.93 / 3,206.54 = 2.80% | 72.15 / 2,306.95 = 3.13% |
| Allowance / balance over 1 year | 89.93 / 159.77 = 56.3% | 72.15 / 64.94 = 111.1% |
| Allowance / total past due | 89.93 / 987.24 = 9.1% | 72.15 / 1,162.56 = 6.2% |
| Credit loss added in the year | 17.78 | 35.76 (-50.3%) |
- The charge halved while the over-one-year bucket rose 2.46x (159.77 vs 64.94) [calc]. Cover of that bucket fell from 111% to 56%.
- The accounting policy says "it is presumed that credit risk has significantly increased if the payment is over due" (Note 2C(iii), [pages 202-203]). That points to lifetime ECL on every past-due balance. The allowance is 9.1% of past due. Without the matrix rates, adequacy cannot be tested.
- Standalone and consolidated allowances are identical (89.93 and 72.15, [page 172] and [page 242]), so the subsidiaries carry no allowance of their own.
- The note labels the whole 89.93 "credit impaired", while the ageing schedule shows credit impaired as "-" in every bucket (Pass 1). Both sets repeat this ([page 149], standalone). This is a labelling matter. The 89.93 reads as a general matrix provision, not as specific impairments [INFERENCE].

### B2. "Other assets" drain: composition of the 736.45 build (Note 10, [page 222]; standalone Note 12, [page 151]) RATING YELLOW (RED if the balance is not recoverable in cash)
Pass 1 said the government-balance line doubled and that "other assets" are 24.4% of the working-capital drain. It did not split the movement. Consolidated other current assets, Rs Mn:
| Line | FY26 | FY25 | Change | Share of change [calc] |
|---|---|---|---|---|
| Balance with government authorities | 1,102.51 | 554.83 | +547.68 | 74.4% |
| Advance to suppliers | 424.11 | 244.37 | +179.74 | 24.4% |
| Prepaid expenses | 32.58 | 12.07 | +20.51 | 2.8% |
| Advances to employees | 12.20 | 8.93 | +3.27 | 0.4% |
| Other deposits and advances | 5.33 | 5.38 | -0.05 | 0.0% |
| IPO receivables | nil | 14.70 | -14.70 | -2.0% |
| Total | 1,576.73 | 840.28 | +736.45 | 100% |
- The total change 736.45 sits within 3.31 of the cash-flow "other assets" line (739.76) [calc, Pass 1]. Government balances plus supplier advances are 98.8% of the build [calc].
- Government balances are 69.9% of the line (66.0% prior) and equal 18.3% of revenue, against 12.1% [calc]. In days of revenue: 66.7 against 44.3, +22.4 days [calc]. Pass 1's 336-day net cycle (rec + inv - pay) does not include this line. Whether the company's WC-day definition does is NOT FOUND IN DOCUMENT.
- Standalone gives 1,082.25 vs 526.33 (+105.6% [calc]); the subsidiaries hold 20.26 vs 28.50 [calc]. The balance is a parent item.
- Cause is NOT FOUND IN DOCUMENT. Export share of revenue is 91.1% (Pass 1). A refund-type receivable from zero-rated exports and credit on 5,000+ of capex are the two usual sources [INFERENCE, not filed text]. The notes give no refund-claim status, no ageing of the balance and no statement that it is realisable. Receivable from the tax authority earns no interest in the notes.
- Supplier advances rose 73.6% against COGS-related purchases (Pass 1: purchases 1,865.87); 10.80 is Atlas Fasteners (related party, Note 31). The ageing and vendor split are NOT FOUND IN DOCUMENT.
- New line: "Allowance for advances written off" 6.06 vs nil, in other expenses (Note 27, [page 232]; standalone Note 29, [page 161]). Which advance (supplier, capital or other) is NOT FOUND IN DOCUMENT. Small, but it is the first advance write-off in the two years shown. YELLOW.

### B3. Foreign-exchange exposure is unhedged on the face of the sensitivity table (Note 34 consolidated, [pages 244-245]; standalone Note 36, [pages 174-175]) RATING YELLOW
- Standalone USD table, Rs Mn: receivables 2,292.95 (USD 24.18 Mn), payables 104.90, borrowings 107.16. Net = 2,292.95 - 104.90 - 107.16 = 2,080.89. Five percent of that is 104.04, which equals the printed USD sensitivity of 104.04 exactly [calc]. EUR: 618.85 - 6.29 - 900.28 = -287.72; 5% = 14.39, which equals the printed (14.39) [calc].
- No forward contract is netted in either currency. With no derivative asset or liability in any note, the exposure is unhedged at year end [INFERENCE from tie-out]. This matches the discretionary policy wording in the governance report ([page 72]).
- Implied closing rates [calc]: USD 2,292.95 / 24.18 = 94.83 vs 1,752.14 / 20.50 = 85.47 (+10.9%); EUR 618.85 / 5.68 = 108.95 vs 471.27 / 5.12 = 92.04 (+18.4%). The rupee fell about 11% against the dollar in the year, so the 214.01 FX gain in other income (Pass 1) is a rupee-weakness gain on an open long-USD position, not an operating item.
- The EUR borrowings (900.28) are a partial natural offset to EUR receivables. The USD book is net long 21.96 Mn [calc: 24.18 - 1.09 - 1.13].
- A 5% rupee recovery costs 104.04 pre-tax (5.6% of consolidated PBT 1,873.06, Pass 1).

### B4. Top-5 customer definition: standalone note closed, with one stale comparative (standalone credit risk note, [page 172]; Note 34 consolidated, [page 242]; Annual_Report_2025 credit-risk notes) RATING YELLOW
- Standalone FY26 label: "Revenue from top 5 customers (other than above customer)" 1,711.10. FY26 figures are the same on both sets: top customer 1,123.97 and the 1,711.10 line. Pass 1's inference stands: two customers are at least 10% of revenue (standalone and consolidated, "Two customers accounts for more than 10%", [page 172]). Ten percent of 5,903.75 is 590.4, and 1,711.10 less 1,123.97 is 587.13, which is lower than 590.4. So 1,711.10 cannot contain the top customer [calc].
- Literal reading: five customers other than the top one, so six names in all. If so, true top-5 (including top-1) lies between 2,835.07 less the sixth name and 2,835.07. The sixth name is at most the average of the five, 342.22 [calc: 1,711.10 / 5]. Range: 2,492.85 to 2,835.07 = 41.3% to 47.0% of consolidated revenue 6,029.75, and 42.2% to 48.0% of standalone 5,903.75 [calc]. Both are well under 65%. Pass 1 gave only the 47.0% upper end and spoke of "four or five" names. The label supports five others; the lower end is new.
- Stale comparative. In Annual_Report_2025 the standalone note printed top customer 631.30 and "top 5 customers" 2,314.75 (Annual_Report_2025.txt line 9131-9132). The consolidated note printed 648.81 and 2,352.65 (lines 12313-12314). In the FY26 AR the consolidated comparative was re-split: 2,352.65 - 648.81 = 1,703.84, which is the printed FY25 figure [page 242]. The standalone comparative was relabelled "other than above customer" but the number stayed at 2,314.75 [page 172]. It was not re-split.
- Two readings. (a) The standalone FY25 figure now excludes the top customer. Then FY25 top-5 including top-1 would be 2,314.75 + 631.30 = 2,946.05 = 65.0% of standalone revenue 4,529.28 [calc]. (b) The label was changed and the number was not, so 2,314.75 still includes the top customer. Reading (b) is the evidenced one. Reading (a) would put standalone top-5 at 2,946.05, above the consolidated top-5 of 2,352.65 printed in the FY25 AR, which cannot hold when the group revenue is the larger base. Under (b) FY25 standalone top-5 is 2,314.75 = 51.1% [calc]. The observation that separates them: the FY27 AR comparative for the standalone note. If it prints a number near 1,683.45 (2,314.75 - 631.30), reading (b) is confirmed.
- Pass 1 line for LB3 changes only in the lower bound and the stale-label note. Consolidated top-1 (18.6%) and top-5 (41.3% to 47.0%) stand against the 20% and 65% tripwires.
- Consolidated top customer in FY25 (648.81) was 17.51 above standalone (631.30). In FY26 both are 1,123.97. The subsidiaries sold to the top customer in FY25 and not in FY26 [calc, INFERENCE on cause].

### B5. Company's own Schedule III ratios and MD&A working-capital statement (standalone Note 45, [pages 181-182]; MD&A, [page 32]) RATING YELLOW
Pass 1 listed Note 45 only as labour codes. The standalone set has a ratio note that the consolidated set does not.
| Ratio (standalone) | FY26 | FY25 | Change | Reproducible? |
|---|---|---|---|---|
| Current ratio | 3.29 | 5.30 | -37.9% | Yes, cash fell on QIP use |
| Debt-equity | 0.29 | 0.17 | +73.1% | Yes: 4,515.80 / 15,519.78 = 0.29 [calc] |
| Debtors turnover | 2.22 | 2.31 | -3.7% | Yes: 5,903.75 / avg(3,092.38, 2,215.82) = 2.22 [calc] |
| Creditors turnover | 2.22 | 1.75 | +27.1% | Basis is purchases |
| Inventory turnover | 0.22 | 0.39 | -43.3% | No (see below) |
| Net capital turnover | 0.87 | 1.33 | -34.2% | Not tested, denominator not printed |
| ROCE | 11% | 9% | +23.6% | MD&A prints 10.7% vs 8.7% |
- Debtors turnover converts to 164 days (365 / 2.22) against 158 (365 / 2.31) [calc]. This is on average balances and credit sales. Pass 1's 188.7 days is on closing consolidated balances. Both show lengthening. The company's own days are closer to 164.
- Creditors turnover converts to 164 days against 209 (365 / 1.75) on a purchases basis [calc]. Against stated terms of 30 to 90 days, this agrees with the 63.0% overdue payables in Pass 1. The fall of about 44 days is the same direction as Pass 1's payable days (51.6 vs 63.9, revenue basis).
- Inventory turnover 0.22 would be 1,659 days. At standalone average inventory 2,575.58, a 0.22 turnover implies a numerator of about 567 [calc: 0.22 x 2,575.58], against standalone revenue 5,903.75 and consolidated purchases 1,865.87. The numerator is "cost of goods sold" but the figure cannot be reproduced from printed lines. The stated reason, "improved cost of goods sold margin and increase in inventories", does not explain a 43% fall. Do not use the inventory turnover figure in stage 10.
- MD&A ([page 32]): "Working capital intensity ... is structural to the business rather than a function of the year's activity" and "The Company expects a gradual normalisation of working capital days over the coming fiscal periods". Neither passage gives a day count, a target, or a financing arrangement. Not Notes text; recorded as context for the cash-conversion load-bearing fact. The 344-day tripwire definition is still NOT FOUND IN DOCUMENT.

### B6. Standalone-only intra-group items (standalone Notes 5, 6, 7, 31, [pages 147-148, 164-165]) RATING GREEN, one YELLOW
- Pass 1 flagged that the 54.13 advance to Leo Prime did not appear in consolidated Note 5. It reconciles. The standalone Note 7 line "Advance towards purchase of investments" is 74.91 (73.24) = 54.13 + 20.78 (54.13 + 19.11) [calc] ([page 148]). The consolidated figure 20.78 (19.11) is the Azad VTC advance only. The 54.13 is netted against the redemption liability 171.50 on consolidation (225.63 - 54.13, Pass 1). Mismatch closed.
- The VTC advance paid is 23.30 ([page 147]) while the carrying amount is 20.78 (2.52 below face). It rose 1.67 in the year [calc]. The note does not say why a refundable advance is carried below face. Discounting is the likely cause [INFERENCE]. Small.
- Loans to subsidiaries (10% simple interest, unsecured): 196.41 (188.88) = Azad VTC 27.10 + Azad Prime 169.31 (Note 6 and Note 31(c), [pages 147, 165]). New loan in FY26: 7.53 to Prime. Interest accrued and unpaid: 26.17 (8.81) = Prime 22.08 + VTC 4.09. Interest income from the two was 19.29 (16.58 + 2.71) [calc], and accrued interest rose 17.36 [calc], so about 90% of FY26 interest was not paid in cash. Eliminated on consolidation. No effect on group cash. It shows both subsidiaries fund themselves from the parent.
- Standalone job work paid to subsidiaries: 61.37 (VTC 60.33, Prime 1.04) vs 5.86, inside standalone job work charges of 370.91 (Note 29, [page 160]) [calc: 16.5% of that line]. Payable to VTC 23.43 vs 1.12. Eliminated on consolidation. VTC's FY26 revenue is therefore largely the parent's job work [INFERENCE: consolidated revenue exceeds standalone by 126.00 only].
- Corporate guarantee to VTC: 52.45 less 1.86 released = 50.59 [calc] ([page 164]). Ties to Pass 1.
- Sitting fees: standalone 4.36 vs consolidated 5.56 ([page 165]; Note 31, Pass 1). The 1.20 gap is paid by the subsidiaries [INFERENCE]. Immaterial.
- Standalone PAT 1,321.61 (EPS 20.46 vs 14.87) and consolidated PAT attributable to owners 1,328.77 (EPS 20.57 vs 14.66) (standalone Note 32 [page 167]; Note 30, Pass 1). Owners' profit exceeds standalone by 7.16 in FY26 and fell short by 12.07 in FY25 [calc: 873.18 vs 885.25]. This does not resolve Pass 1's 42.10 gap in Note 44 (parent column 1,363.71). Reconciling that gap needs the consolidation workings, NOT FOUND IN DOCUMENT. Pass 1 flag stands.

### B7. QIP: idle-funds figure and use of the general-purpose bucket (Note 40, [page 249]; CARO clause x(b), [page 117]) RATING GREEN on parking, YELLOW on one gap
- The auditor reports idle QIP funds of 1,600.06: 1,599.99 in fixed deposits and 0.07 in the monitoring account. Peak idle balance in the year was 6,430.00 ([page 117]). The auditor says funds were used for the stated purposes "except for idle funds". Note 40 shows unutilised 1,597.27 (Pass 1). The 2.79 difference [calc: 1,600.06 - 1,597.27] fits the 31.22 of expenses paid from the company account and not yet reimbursed, less interest earned, but the notes do not give the arithmetic. NOT FOUND IN DOCUMENT.
- General corporate purposes 1,562.10 is 100% used while 1,563.35 of the capex object remains. The note does not say what the 1,562.10 paid for. With OCF at (1,189.66) (Pass 1) and the debt build, a share of it may have funded working capital [INFERENCE only]. The monitoring-agency statement is the document that would show it (QIP placement document and agency statement not collected, B00 gap).
- CARO clause ix(d) reports that no short-term funds were used for long-term purposes ([page 117]), while demand-loan WC lines rose 144% and capex ran at 5,724.80 (Pass 1). The auditor's wording stands as filed. No contradiction shown by the notes.

### B8. Minor items not in Pass 1
- Statutory dues: CARO clause vii(a) reports 1.00 of provident fund unpaid for over six months "due to non-updation of mandatory employee details in the portal", and a "slight delay in a few cases" in depositing statutory dues ([page 116]). GREEN, small.
- Note 41(c) says the Group "has not revalued its property, plant and equipment during the financial year 2024-25" ([page 249]). The year printed is the prior year. Clerical. GREEN.
- CARO clause xix ([page 118]) gives no material uncertainty on meeting liabilities for one year. This is not going-concern language; the finding stays NONE.

## C. NOTES CHECKED AND FOUND FULLY COVERED BY PASS 1 (no new item)
Notes 2 (policies, other than B1 policy link), 3, 4, 11, 12, 13, 15 to 17, 19 to 26, 28, 31 to 33, 35 to 39, 41 to 45 consolidated. Standalone Notes 1 to 4, 8, 9, 10, 13 to 28, 30 to 35 agree with the consolidated notes after subsidiary additions (for example standalone inventory 3,266.32 vs consolidated 3,291.13, a 24.81 difference [calc]; receivables gross 3,182.31 vs 3,206.54, a 24.23 difference [calc]; variable-rate borrowings 3,450.60 vs 3,501.19). Fixed-rate borrowings are 1,065.20 on both sets.

## PASS 2 NEW FINDINGS SUMMARY (new items only)
1. B1: receivable allowance cover of the over-one-year bucket fell from 111% to 56% as the charge halved (17.78 vs 35.76) and that bucket rose 2.46x; allowance is 9.1% of past due. ECL rates NOT FOUND IN DOCUMENT. YELLOW. (Note 8, pp.220-221; Note 34, p.242.)
2. B2: the 736.45 other-current-asset build is 74.4% government balances (+547.68, now 66.7 days of revenue vs 44.3) and 24.4% supplier advances (+179.74). Composition and realisability NOT FOUND IN DOCUMENT. New 6.06 advance write-off. YELLOW. (Note 10, p.222; Note 27, p.232.)
3. B3: FX sensitivity ties to gross balances with no forward netted (USD 104.04, EUR 14.39). Open long-USD book, rupee down 10.9%. The 214.01 FX gain is not operating profit. YELLOW. (Note 34, pp.244-245; standalone p.174-175; governance p.72.)
4. B4: standalone top-5 label closed. 1,711.10 excludes the top customer. Top-5 range 41.3% to 47.0% consolidated. Standalone FY25 comparative 2,314.75 is stale (still includes top-1), not re-split; reading (b) evidenced, FY27 AR separates them. YELLOW. (p.172; p.242; AR2025.)
5. B5 to B8: company's own ratios (debtors 164 days vs 158; creditors 164 vs 209 on purchases; inventory turnover 0.22 not reproducible and not to be used); MD&A calls WC "structural", gives no day target; the 54.13 and 20.78 advance mismatch closes; QIP idle funds 1,600.06 per auditor; no factoring wording anywhere. YELLOW and GREEN. (Note 45 pp.181-182; MD&A p.32; Notes 5-7, 31 standalone; CARO p.117.)


---
ERRATA (appended by the orchestrator 2026-11-15 from the stage's own hand-back; the stage has no edit tool):
- B2: the non-current statutory deposit line (Note 6) is anchored to [page 220]; it should read [page 219], per Pass 1.
- B2: "5,000+ of capex" is loose; the capex cash flow is 5,724.80 (Rs Mn).
- B2: the statement that the government receivable "earns no interest in the notes" is an absence (the notes are silent on interest), not a finding.
- B7: the reading that the 2.79 gap "fits the 31.22 less interest" is speculation; the notes give no such arithmetic.
- Section C: the standalone-to-consolidated agreement was spot-checked on inventory, receivables, borrowings and the allowance, not on every note.
- B3: standalone "Note 36" for the FX table was inferred from the receivables note cross-reference; the note number is unconfirmed.
