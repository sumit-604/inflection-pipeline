# STAGE 2, PASS 2 of 3: NOTES TO FINANCIAL STATEMENTS, WHAT PASS 1 MISSED
Company: MMP Industries Ltd (MMP) | Run date: 2026-10-04 | Source: inputs/annual-report/Annual_Report_2026.txt (FY2025-26), comparatives from the same AR and Annual_Report_2025.txt

## READING CONVENTIONS (same as Pass 1)
- UNIT: INR Lakhs (L) as printed on the face ("Amount in Rs in Lakhs"). Nothing converted. "(derived)" means my arithmetic on printed figures, inputs anchored.
- ANCHORS: "S" = standalone notes, "C" = consolidated notes, "p.N" = the "[page N]" marker in the .txt (printed page = N minus 5).
- RATINGS in words: GREEN, YELLOW, RED.
- Method: I re-read S Notes 1 to 56 and C Notes 1 to 59 from the top, and re-footed the P&L, cash flow, Note 2, Note 36, Note 18, Note 39B and Note 50 against each other. Items Pass 1 covered fully are skipped. Items Pass 1 covered in part carry only the remainder.
- Load-bearing facts (LBF1 to LBF4) were checked first; each finding below names the LBF it touches.
- Outside-notes reference used once: the auditors' Key Audit Matter on the fire (p.83) says they examined "surveyor reports" and "correspondence with insurance companies". The notes themselves state no surveyor outcome. This is context, not a notes finding.

---------------------------------------------------------------
## CORRECTIONS TO PASS 1 (three, all from the re-read)
1. Pass 1 Section 3 wrote that bank guarantees of 445.72 L are "backed by term deposits 445.72 L (Note 14)". Note 14 footnote says deposits are pledged against guarantees "amounting to 445.72 L". That is the guarantee amount, not the deposit amount. All term deposits on the S balance sheet are 242.24 L (113.16 non-current, S Note 7 p.120, plus 129.08 current, S Note 14 p.122). See P2-7.
2. Pass 1 Section 6 read the Schedule III table (C Note 50) as showing a "net deficit" for MEPL and Toyal and said the table "appears to deduct cost". For MEPL and Star that reading holds (carrying less cost). For Toyal it does not hold in FY26. See P2-4.
3. Pass 1 Section 12c quoted unhedged EUR 0.08 lakh payable and 2.47 lakh receivable as the unhedged position. That is Note 51. Note 39B prints a different EUR position and a sensitivity built on it. See P2-8.

---------------------------------------------------------------
## NEW FINDINGS

### P2-1 Fire accounting does not tie between Note 2, Note 36, Note 52 and the cash flow (LBF2, LBF4)
Rating: YELLOW
Facts:
- Non-cash PPE losses in the P&L: fire PPE loss 338.92 L (S Note 52 p.159) plus "Loss on Disposal of PPE" 32.53 L (S Note 36 p.135) = 371.45 L (derived).
- The cash flow adds back only "(Surplus)/Loss on Disposal of PPE (Including Loss due to Fire)" 23.45 L (S CF p.95). Gap to 371.45 L is 348.00 L (derived).
- Note 2 shows deductions of 595.77 L cost and 135.49 L accumulated depreciation, so net block derecognised 460.28 L (S Note 2 p.116; same in C p.195). 460.28 less the 23.45 L add-back equals 436.83 L (derived).
- The cash flow line "Investment in PPE (Net of Disposal)" is 2,899.94 L against gross additions of 3,336.76 L (S CF p.95; S Note 2 p.116). The difference is 436.82 L (derived), which matches the 436.83 L above. The cash flow therefore treats about 436.8 L of derecognised PPE as a cash offset in investing.
- No disposal proceeds are disclosed anywhere in the notes. The insurance claim of 793.05 L is still receivable (S Note 14 p.122). Fire losses are not cash receipts.
- FY25 check: the P&L shows loss on disposal 11.37 L (S Note 36 p.135) but the FY25 cash flow shows a surplus of (0.17) L (S CF p.95). The cash flow line does not tie to Note 36 in either year.
- Two other gaps of the same size sit in the fire accounting. Inventory: Note 52 gives 671.45 L loss, the P&L removals from cost are 583.03 L (Pass 1, LBF2), gap 88.42 L. PPE: net block removed 460.28 L less fire PPE 338.92 L less disposal loss 32.53 L leaves 88.83 L (derived). Note 52 says only that employee compensation is stated "net of disposal of debris". Debris proceeds: NOT FOUND IN DOCUMENT.
Two readings and the observation that separates them:
- Reading A: the add-back was understated by 348.00 L, so CFO is understated and investing is overstated by up to 436.83 L. CFO excluding borrowings (Pass 1: 4,649.19 L, 66.0% of EBITDA) would be up to 4,997.19 L (70.9%) (derived).
- Reading B: part of the 436.83 L was real sale or debris proceeds not disclosed. CFO stays as filed.
- Separating observation: disclosure of disposal and debris proceeds in FY26, or the Q4 FY26 filed cash flow. Neither is in the notes. Reading A and B do not change total cash. They change the CFO and investing split by 348 L to 437 L, which is 6% to 8% of CFO (derived).

### P2-2 Cost-line pattern behind the 133 bps margin fall (LBF1)
Rating: YELLOW
S P&L p.94; S Notes 31 to 36 p.133-135.
| Line (S, L) | FY26 | FY25 | Growth | % of revenue FY26 / FY25 |
|---|---|---|---|---|
| Materials consumed | 66,005.58 | 55,543.77 | +18.8% | 80.33% / 80.28% |
| Power and fuel | 2,837.22 | 2,810.35 | +1.0% | 3.45% / 4.06% |
| Employee cost | 4,680.15 | 4,395.32 | +6.5% | 5.70% / 6.35% |
| Other expenses excluding power and fuel (derived) | 2,302.62 | 2,101.96 | +9.5% | 2.80% / 3.04% |
| Change in FG, WIP, trading stock (credit) | (555.60) | (2,069.76) | n/a | 0.68% / 2.99% |
- Revenue grew 18.8% (S Note 29 p.132). Power and fuel grew 1.0%. Umred, the fire site, makes powder, the power-heavy product; the notes give no production volumes. Cause of the flat power line: NOT FOUND IN DOCUMENT.
- The stock-build credit shrank from 2,069.76 L to 555.60 L. The 555.60 L itself includes 526.00 L of fire-destroyed FG and WIP removed from the cost lines (S Note 32 p.134). Without that, the build is 29.59 L (derived: closing 9,670.90 less opening 9,641.31).
- Reading: materials consumed held at 80.3% of revenue, and the conversion cost lines grew slower than revenue. The ratio shift came from the stock-build credit, which carries conversion cost into inventory. FY25 EBITDA benefited from a 3.0% of revenue stock build. FY26 did not.
- Two readings: (a) a lower build reflects fire disruption and a one-time stock rebalancing; (b) FY25 margin of 9.4% was inflated by the build and FY26 is the cleaner base. Separating observation: FG and WIP days by quarter and Umred volumes after restart. Neither is in the notes.
- Other lines that moved: insurance 95.62 L vs 55.75 L (+71.5%); plant repairs 96.92 L vs 57.97 L (+67.2%); loss on disposal of PPE 32.53 L vs 11.37 L; legal and professional 230.20 L vs 186.66 L (+23.3%); selling and distribution 469.91 L vs 419.19 L (+12.1%) (S Note 36 p.135). Building and other repairs fell by 54.5 L together.

### P2-3 Start-up subsidiaries explain about 50 bps of the 133 bps fall (LBF1, LBF4)
Rating: YELLOW
- EBITDA, both books, excluding the Star dividend that C eliminates (derived):
  - S: FY26 7,045.18 less 9.98 = 7,035.20 L = 8.56% of S revenue; FY25 6,550.50 less 49.91 = 6,500.59 L = 9.40%. Fall 83 bps.
  - C: FY26 6,626.71 L = 8.04%; FY25 6,487.31 L = 9.38%. Fall 133 bps (Pass 1, LBF1).
  - Difference of the two falls: about 50 bps. In rupees, C EBITDA is 408.49 L below S EBITDA excluding dividend (derived), while C revenue is only 231.91 L higher (insulators, C Note 29 p.211).
- Where the 408.49 L comes from (C Note 36 p.214 vs S Note 36 p.135, derived): other expenses +344.17 L (5,484.01 vs 5,139.84), of which "Testing and Analysis Charges" 141.61 L (new line, nil PY), legal and professional +44.10 L, power and fuel +43.83 L, stores +26.63 L, selling +23.46 L, rent, rates and taxes +12.81 L, preliminary expenditure written off 11.24 L (PY 6.70 L). Employee cost +114.58 L (4,794.73 vs 4,680.15, C Note 33 p.213). Materials +216.17 L against revenue +231.91 L.
- Policy for preliminary expenditure: NOT FOUND IN DOCUMENT. Unamortised balance: NOT FOUND. C deferred tax asset of 4.74 L on it implies about 18.8 L unamortised at 25.168% (derived; C Note 20 p.207).
- Pre-tax subsidiary loss: C PBT after exceptional is 3,185.46 L (C Note 20B p.206) against S PBT 3,668.13 L. The gap of 482.67 L is 9.98 L Star dividend plus about 472.69 L of subsidiary results and eliminations (derived). The post-tax subsidiary loss in Note 50 is 352.81 L (C p.239). The gap of about 120 L is the deferred tax credit of 123.81 L on subsidiary losses (C Note 20C p.207). So 26% of the subsidiary pre-tax loss is booked as a tax asset (derived).
- Subsidiary gratuity: C Note 45 repeats the S obligation (611.39 L, 565 employees) line for line (C p.228-229). C salary cost is 111.78 L higher than S (4,414.58 vs 4,302.80 L, C Note 33 p.213). No subsidiary obligation is shown. Headcount in subsidiaries: NOT FOUND IN DOCUMENT.

### P2-4 Schedule III table (C Note 50) does not tie to consolidated equity in FY26 (LBF3)
Rating: YELLOW
- FY25 table works: net assets column equals carrying value less cost for associates. Star 4,200.29 less 97.83 = 4,102.46. Toyal 567.52 less 702.26 = (134.74). Total 32,344.20 L equals C equity (C Note 50 p.240; C Note 39C p.221).
- FY26 table: Star 4,764.68 less 97.83 = 4,666.85 (works). Toyal should be 645.98 less 702.26 = (56.28). The table prints (702.25) (C Note 50 p.239). Total printed 34,004.81 L against C equity 34,650.78 L (C Note 39C p.221). Gap 645.97 L (derived), equal to Toyal's carrying value within 0.01 L.
- Effect: the percentage columns for FY26 (Toyal -2.07%, parent 89.41%) are built on the wrong base. Reported equity, profit (3,100.93 L) and OCI ((286.29) L) tie. This is a disclosure error, not a balance error.
- Pass 1 said MEPL shows "a net deficit". MEPL's (347.72) L is its cumulative loss (10.34 + 337.37), not its net worth. On cash equity of 500.00 L (S Note 45 p.153) about 70% is consumed (derived). MEPL's own balance sheet: NOT FOUND IN DOCUMENT. The 500.00 L preference shares sit on top and are redeemable at par on 9 March 2031 (S Note 5 p.118).

### P2-5 Associate profit: OCI, dividend leakage and unrealised profit (LBF3)
Rating: YELLOW
- Star's OCI share is (168.32) L this year against (32.30) L last year (C Note 46 p.234; Note 49 p.237). At 100% that is about (646) L (derived: 168.32 / 26.06%). Cause: NOT FOUND IN DOCUMENT. Pass 1 gave only the profit share of 742.70 L.
- Total comprehensive share from Star is 574.37 L, 22.7% below the profit share (C Note 49 p.237). The "Share of OCI in Associates" reserve fell from 218.84 L to 50.89 L (C Note 17 p.202-203). The P&L line of 820.78 L therefore overstates what the group kept in equity from Star's year by 168 L (derived).
- Carrying value of Star reconciles to the paisa: 4,200.29 + 742.70 - 168.32 - 9.98 dividend = 4,764.69 L (derived; C Note 5 p.197). Toyal: 567.52 + 78.09 + 0.37 = 645.98 L, no dividend.
- Star's own dividend: equity roll 16,116.21 + 2,849.67 - about 646 (OCI) leaves 18,319.98 against 18,281.73 reported. The implied total dividend paid by Star is about 38 L, 1.3% of Star's PAT (derived). MMP's 9.98 L share matches that.
- Policy gap: the unrealised profit elimination is written for subsidiaries only (C Note 1.2 p.177). Nothing is stated for downstream sales to Toyal (1,801.51 L, S Note 45 p.152) or job work for Star. Toyal's stock rose 464.02 L (Toyal "Changes in Inventories" (464.02), C Note 49 p.238). Elimination amount: NOT FOUND IN DOCUMENT.
- Star balance sheet shape (C Note 49 p.237): current assets 13,553.03 L = 70% of Star revenue (derived). Non-current liabilities 1,831.60 L.

### P2-6 Funding of new-subsidiary capex: undrawn lines, commitments and the maturity table (LBF4)
Rating: YELLOW
- Undrawn sanctioned term loans (derived): MEPL 2,800.00 - 2,348.98 = 451.02 L; MCPL 3,188.00 - 512.70 = 2,675.30 L; total 3,126.32 L (C Note 18h, 18k p.205).
- Capital commitments not provided: C 5,642.27 L, S 3,278.31 L, so subsidiaries 2,363.96 L (derived; S Note 48 p.157; C Note 52 p.241). Subsidiary CWIP is 2,124.03 L (C 3,832.49 less S 1,708.46, C Note 4 p.197).
- Parent commitments of 3,278.31 L have no undrawn parent term loan disclosed. NOT FOUND IN DOCUMENT. Parent cash 56.38 L and liquidity 298.62 L (S Note 39B p.141).
- Two readings: (a) the 3,126.32 L undrawn lines plus parent cash flow fund the 5,642.27 L over the build period; (b) the parent also bears subsidiary shortfalls through further equity, preference shares and reimbursements, as in FY26 (1,425.00 L cash plus 1,139.54 L and 192.49 L reimbursements, S Note 45 p.152-153). Separating observation: undrawn amounts and disbursement schedule at MCPL (only 16% drawn).
- C maturity table (C Note 39B p.220): borrowings under 1 year 14,134.83 L, 1 to 5 years 4,371.62 L, over 5 years nil. Sum 18,506.45 L against carrying 18,452.46 L; the 54.00 L excess is a transposition of non-current 4,317.62 L (C Note 18 p.204). S table ties exactly (15,163.24 L).
- Over 5 years is nil, but MEPL's loan runs to March 2032 and MCPL's to March 2033 (C Note 18h, 18k p.205). From April 2031 the MEPL monthly instalments (31.34 L x 12 = 376.08 L, derived) and MCPL quarterly instalments (57.47 L x 8 = 459.76 L, derived) fall beyond five years.
- Instalment text does not close. MEPL: "monthly instalments commencing January 2026" and then "equated quarterly instalments of 31.34 L". Monthly closes (75 months x 31.34 = 2,350.50 L against 2,348.98 L drawn). Quarterly would repay 33%. MCPL: 57.47 L per quarter from March 2027 to March 2033 is 25 instalments = 1,436.75 L, 45% of the 3,188.00 L sanction (derived). Balloon or other terms: NOT FOUND IN DOCUMENT.
- Interest on subsidiary debt: C finance cost exceeds S by 30.17 L (1,333.31 vs 1,303.14, C Note 34 p.213). Capitalised interest: NOT FOUND IN DOCUMENT (also open from Pass 1).
- Fixed-rate borrowing rose from 3,755.30 L to 5,567.13 L in C while S fell from 3,337.29 L to 2,819.18 L (C Note 39B p.218; S p.139). The +2,747.95 L subsidiary fixed-rate position is not explained. The 70 bps sensitivity of 129.17 L is again 70 bps of total borrowings 18,452 L, not of the variable book 12,885 L (derived).

### P2-7 Collateral liens exceed all term deposits on the balance sheet (LBF4)
Rating: YELLOW
- Liens stated: 2,000.00 L cash collateral with Federal Bank (S Note 7 p.120); 100.00 L Federal Bank working capital lien (S Note 23d p.130); 445.72 L bank guarantees (S Note 14 p.122). Total 2,545.72 L (derived).
- Term deposits actually on the S balance sheet: 113.16 L + 129.08 L = 242.24 L (S Notes 7, 14). The stated liquidity of 298.62 L equals cash 56.38 L plus these 242.24 L exactly (derived; S Note 39B p.141). So no other deposits exist in the liquidity figure.
- The 2,000 L text is identical in the prior year (PY deposits 106.39 + 93.98 = 200.37 L). Either the text is a carry-over error or collateral sits outside the disclosed deposits. The notes do not say which. The note covering borrowings against 2,000 L: NOT FOUND IN DOCUMENT.
- This also means the "liquidity position" of 298.62 L is mostly pledged: 242.24 L of it is margin money (S Notes 7, 14).

### P2-8 Hedge accounting trail: MTM loss, labels and sensitivity (LBF1, LBF4)
Rating: YELLOW
- Forward MTM payable 57.02 L on notional 1,979.34 L = 2.9% (S Note 25 p.131; S Note 48 p.157). The only equity movement is the cash flow hedge reserve (10.12) L gross, (7.57) L net of tax 2.55 L (S P&L p.94; S Note 17 p.125). The counter-entry for the other 46.90 L (derived) is NOT FOUND IN DOCUMENT. Loss on future and option contracts in Note 36 is 0.34 L; FX gain fell only to 55.32 L from 63.09 L (S Note 30 p.133).
- Three labels for one item: Note 39A lists the forward payable as "FVTPL" Level 2 (S p.138); the equity reserve is "Cash Flow Hedge" (S p.125); the P&L face books the 10.12 L under "Net fair value gain/(loss) on investments in debt instruments through OCI" (S P&L p.94).
- Note 39B EUR table: liabilities 13.76 lakh, assets 7.33 lakh. The EUR sensitivity of 26.23 L PAT per 5% implies a net unhedged EUR 6.43 lakh exposure (derived: 26.23 / (1 - 25.168%) / 5% = about 701 L at about 109 per EUR). Note 51 shows unhedged EUR payable 0.08 lakh and receivable 2.47 lakh (net receivable 2.39 lakh) (S p.158-159). The two disclosures have opposite signs.
- Forward sales of EUR 13.68 lakh (1,457.19 L) equal 38.0% of FY26 export sales of 3,836.87 L (derived). Note 51 says the cover is for "underlying transactions and firm commitments". Forecast flows are not itemised.
- C Note 39B text reads "The Company has entered into any hedging arrangements" (C p.218); the S text reads "has not entered into" (S p.140). Both conflict with Note 51.

### P2-9 Credit loss charge is mostly the non-current "other receivable", not trade debtors (LBF4)
Rating: YELLOW (extends Pass 1 Section 4)
- FY26 provision in Note 36: 68.81 L (S p.135). Split (derived): trade 63.41 - 47.87 = 15.54 L; non-current other receivable 283.19 - 229.93 = 53.26 L. Other receivable is 77.4% of the charge (S Notes 7, 11 p.120-121).
- The gross other receivable is flat (703.86 L vs 700.86 L, +3.00 L) while the allowance rose 23.2%. Allowance now 40.2% of gross (Pass 1: 32.8% PY).
- Last year's charge was 54.15 L. At about 53 L a year, the net 420.66 L carrying value is the exposure; debtor identity and nature: NOT FOUND IN DOCUMENT (also open from Pass 1).
- Trade allowance of 63.41 L is 2.4x the "doubtful" bucket of 26.36 L (S Note 41 p.143).

### P2-10 Segment returns on segment assets (LBF1)
Rating: YELLOW
C Note 44 p.226-227, derived on closing segment assets:
| Segment | Result FY26 | Assets FY26 | Return FY26 | Result FY25 | Assets FY25 | Return FY25 |
|---|---|---|---|---|---|---|
| Powder and Paste | 5,988.44 | 32,473.91 | 18.4% | 5,422.66 | 29,303.75 | 18.5% |
| Foils | 430.53 | 13,511.96 | 3.2% | 303.18 | 12,487.44 | 2.4% |
| Conductors | 485.92 | 3,541.78 | 13.7% | 799.53 | 3,789.20 | 21.1% |
| Insulators | (329.13) | 3,489.42 | (9.4%) | (0.53) | 1,016.47 | n/m |
- Foils holds 25% of segment assets for 6.4% of segment result (derived). Revenue rose 39.4% on segment assets +8.2% (C p.226-227).
- Conductors return fell 7.4 points on revenue +3.4%.
- Segment results are before interest and unallocated costs (1,194.50 L, +11.0%), so these are not post-finance returns.

### P2-11 Balance sheet items Pass 1 did not cover
Rating: GREEN to YELLOW
- Income tax refund receivable, non-current: 101.76 L vs 3.28 L (S Note 8 p.120; same in C p.198). Source of the refund: NOT FOUND IN DOCUMENT. Current tax asset went from 78.66 L to nil, and a net current tax liability of 111.80 L appeared (S Notes 9, 28 p.120, 131).
- Subsidiary tax and GST position: "Balances with Revenue Authorities" C 377.37 L vs S 35.44 L, so 341.93 L sits in subsidiaries (derived; C Note 15 p.200; S Note 15 p.123). PY C 154.01 L vs S 80.40 L.
- Vendor advances S 250.36 L vs 134.33 L (+86.4%) (S Note 15 p.123). Capital advances 595.98 L vs 198.30 L (Pass 1).
- Capital creditors fell to 148.56 L from 456.59 L while capital commitments rose to 3,278.31 L (S Note 25 p.131; Note 48 p.157). The cash flow shows capital creditors as +4.24 L (S CF p.95).
- Interest income on amortised-cost assets 33.25 L vs 13.06 L (+155%) (S Note 30 p.133). Composition NOT FOUND IN DOCUMENT. Loans to subsidiaries are stated interest-free (S Note 45(c) p.152).
- Capital reserve 40.32 L is a sales tax incentive "subject to compliance" with forfeiture risk (S Note 17 p.126). Deferred grant liability 124.44 L (S Note 22 p.129). GREEN, small.

### P2-12 Related-party text and list differences (LBF3)
Rating: YELLOW, low
- Both S and C say related-party vendors supply "primarily to the Company" and give just-in-time and working capital benefits (S Note 45 p.151; C Note 46 p.232). Related-party purchases are 1.49 L (Star) and nil (Toyal) (S p.151). The text describes a vendor relationship the numbers do not show. The real flows are sales to Toyal and job work for Star. The arm's-length statement carries no method.
- C Note 46 adds Shri Aditya Kothari, "Director in Wholly Owned Subsidiary Company" (C p.232) as a related person. No transaction with him is listed. His role and pay: NOT FOUND IN DOCUMENT.
- Note 45(c) says all related-party balances are "interest free" and "repayable on demand". The S loans to MEPL (125.00 L) and MCPL (90.00 L) were repaid in-year with no interest income shown.

### P2-13 Further clerical and cross-reference slips (none changes a reported total)
Rating: GREEN
- S Note 13 footnote says 285.00 L "(Prev Year NIL)" due from the subsidiary; the table shows the 285.00 L in the prior year (S p.121-122).
- C Note 14 footnote cites "Note 55" for the fire; the fire note is C Note 56 (C p.200).
- C Note 17 labels the FY26 closing line "Balance as at March 31, 2024 (D)" (C p.203).
- C Note 52 headers read 31.03.2025 and 31.03.2024 (Pass 1). S Note 51 receivable table is headed "31.03.2025 31.03.2024" (S p.159).
- C Note 55 PY unhedged USD receivable 0.47 lakh (40.51 L) while S shows nil for the same date (C p.243; S p.159). C Note 39B prints USD liabilities 51.89 lakh and assets 5.76 lakh (C p.218) against C Note 55 payable USD 0.49 lakh.
- C Note 49 repeats "Star Circlips" in the Toyal paragraph (Pass 1).
- Audit fees: S 3.44 L; C 5.69 L (S p.135; C p.214). Statutory audit fee in C rose 65% (4.55 L vs 2.75 L).

---------------------------------------------------------------
## LOAD-BEARING FACTS: WHAT PASS 2 ADDS
- LBF1 (guidance vs delivery, margin): margin fall splits about 83 bps parent and 50 bps subsidiaries, ex-dividend (P2-3). The parent fall sits in the stock-build credit, not in materials or conversion ratios (P2-2). Segment returns: foils 3.2%, conductors 13.7% (P2-10).
- LBF2 (fire, claim): cash flow add-back does not match the PPE loss; about 88 L gaps in both the inventory and PPE tie-outs; debris proceeds NOT FOUND (P2-1). Pass 1 items (793.05 L receivable, nil collected) stand.
- LBF3 (associates, RPT): Star OCI loss (168.32) L cuts the group's comprehensive share to 574.37 L; Schedule III FY26 table misses by 645.97 L (P2-4, P2-5).
- LBF4 (cash, debt, funding): undrawn subsidiary lines 3,126.32 L against commitments 5,642.27 L; maturity table and instalment text do not close; liens 2,545.72 L vs deposits 242.24 L (P2-6, P2-7).

## PASS 2 NEW FINDINGS SUMMARY (new items only)
| # | Finding | Anchor | Rating |
|---|---|---|---|
| P2-1 | Fire PPE loss 338.92 L: cash flow add-back 23.45 L; investing nets 436.82 L; ~88 L gaps in inventory and PPE ties; CFO/investing split uncertain by 348 to 437 L | S CF p.95; S Notes 2, 36, 52 | YELLOW |
| P2-2 | Cost lines: power +1.0%, employee +6.5% on revenue +18.8%; stock-build credit 0.68% vs 2.99% of revenue is the margin swing | S Notes 31-36 p.133-135 | YELLOW |
| P2-3 | Subsidiaries cost ~50 bps of the 133 bps; C EBITDA 408.49 L below S; 26% of sub pre-tax loss booked as tax asset | C Notes 20, 33, 36, 50 | YELLOW |
| P2-4 | Schedule III FY26 table misses C equity by 645.97 L (Toyal row) | C Note 50 p.239; Note 39C p.221 | YELLOW |
| P2-5 | Star OCI (168.32) L; comprehensive share 22.7% below profit share; no associate unrealised profit policy | C Notes 17, 46, 49 | YELLOW |
| P2-6 | Undrawn sub lines 3,126.32 L vs commitments 5,642.27 L; C maturity table adds 54 L and shows nil over 5 years | C Notes 18, 39B, 52 | YELLOW |
| P2-7 | Liens 2,545.72 L vs term deposits 242.24 L; liquidity 298.62 L is mostly margin money | S Notes 7, 14, 23, 39B | YELLOW |
| P2-8 | Forward MTM 57.02 L vs OCI 10.12 L; three labels; 39B vs Note 51 opposite signs | S Notes 25, 39A, 39B, 51 | YELLOW |
| P2-9 | 77% of the credit-loss charge sits on the non-current other receivable | S Notes 7, 11, 36 | YELLOW |
| P2-10 | Segment returns: foils 3.2%, conductors 13.7% (21.1% PY), insulators (9.4%) | C Note 44 | YELLOW |
| P2-11 | Tax refund 101.76 L, subsidiary revenue-authority balances 341.93 L, vendor advances +86% | S Notes 8, 15; C Note 15 | GREEN/YELLOW |
| P2-12 | RPT vendor text not matched by data; new C related person | S Note 45; C Note 46 | YELLOW |
| P2-13 | Further clerical slips | various | GREEN |

## OPEN POINTS FOR PASS 3 (patterns, not findings)
- Contradiction scan: Note 7 lien text vs deposits; Note 39B vs Note 51 FX; Note 18 monthly vs quarterly; policy 1.4(r) vs 1.6(d) contingent assets.
- Tie-out scan: cash flow vs Note 2; Note 50 vs Note 39C; Note 52 vs Notes 31, 32.
- Events after the balance sheet date: still only the dividend recommendation. Re-check insurance receipt and subsidiary drawdowns against the Q1 FY27 filings outside the notes.

```yaml
stage: B02-notes-pass2
company: "MMP"
run_date: "2026-10-04"
model: claude-sonnet-5-5
status: pass2_complete
input_gaps:
  - "B00 CORPUS GAPPED: screener P&L, Quarters, Balance Sheet, Cash Flow, Customization sheets are empty (no CSV); Data_Sheet.csv only"
  - "B00: scanned Q4 FY26 and Q3 FY26 results are image scans with no OCR; not used in this pass (AR FY26 text used instead)"
  - "B00: ARFIN transcripts absent; peer transcripts only APARINDS and MAANALU"
  - "B00: NSE results clarifications of 2026-03-05 and 2026-06-23 have no company reply in the corpus"
  - "B00: announcements and shareholding were repaired by hand; selection, not full list"
  - "Notes-level (pass 1): insurer acceptance and collection of the 793.05 L claim, FY26 guidance text, number of fire deaths, nature of 703.86 L other receivables, Toyal contingent liabilities, capitalised interest, 5-year repayment schedule are NOT FOUND IN DOCUMENT"
  - "Notes-level (pass 2): debris and disposal proceeds from the fire, Star OCI cause, counter-entry of 46.90 L forward MTM, MEPL own balance sheet, subsidiary headcount and gratuity, composition of interest income, preliminary expenditure policy, associate unrealised profit elimination, collateral behind the 2,000 L Federal Bank lien are NOT FOUND IN DOCUMENT"
flags:
  - {type: FLAG-CASH, reason: "CFO includes short-term borrowing increase (S 789.11 L, C 1,723.34 L); CFO ex-borrowings S 4,649.19 L vs 1,121.30 L; payables +70.2%; trade receivable ageing itself clean"}
  - {type: FLAG-INSURANCE-RECEIVABLE, reason: "793.05 L receivable booked on claim bill, 47% of 1,672.01 L loss, nil received in FY26, acceptance not shown (S Notes 14, 37, 52)"}
  - {type: FLAG-ASSOCIATE-PROFIT, reason: "Share of associate profit 820.78 L = 20.5% of C PBT; cash dividend 9.98 L (S Note 45 p.154); Star OCI share (168.32) L cuts comprehensive share to 574.37 L (C Note 49 p.237)"}
  - {type: FLAG-GUARANTEES, reason: "Corporate guarantees 6,688 L = 22.0% of S net worth; two items each above 10% (S Note 47 p.157)"}
  - {type: FLAG-CF-PRESENTATION, reason: "Cash flow add-back for PPE loss 23.45 L vs 371.45 L non-cash PPE losses; investing nets 436.82 L; CFO/investing split uncertain by 348 to 437 L; about 88 L gaps in inventory and PPE fire ties (S CF p.95; S Notes 2, 36, 52)"}
  - {type: FLAG-FUNDING, reason: "Undrawn sanctioned subsidiary term loans 3,126.32 L vs C capital commitments 5,642.27 L; C maturity table nil over 5 years though loans run to 2032 and 2033 (C Notes 18, 39B, 52)"}
  - {type: FLAG-COLLATERAL, reason: "Stated liens 2,545.72 L vs all term deposits 242.24 L; liquidity 298.62 L = cash 56.38 L + those deposits (S Notes 7, 14, 23, 39B)"}
accounting_quality: 6   # preliminary, unchanged after pass 2, /10; pass 3 sets final
pass_2_empty: false
pass_3_empty: null      # not yet run
top_findings:           # pass 2 new items only
  - {rank: 1, finding: "Fire PPE loss 338.92 L: cash flow add-back only 23.45 L and investing shown net of 436.82 L; about 88 L unexplained gaps in both inventory and PPE fire ties; debris proceeds not disclosed", note_ref: "S CF p.95; S Notes 2, 36, 52 (p.116, 135, 159)", rating: "YELLOW", why: "CFO and investing split uncertain by 348 to 437 L; bears on cash conversion (LBF2, LBF4)"}
  - {rank: 2, finding: "Start-up subsidiaries explain about 50 bps of the 133 bps EBITDA margin fall; C EBITDA 408.49 L below S ex-dividend; 26% of subsidiary pre-tax loss booked as DTA", note_ref: "C Notes 20, 33, 36, 50", rating: "YELLOW", why: "Splits the margin fall into parent 83 bps and subsidiaries 50 bps (LBF1)"}
  - {rank: 3, finding: "Parent margin fall sits in the stock-build credit (0.68% vs 2.99% of revenue) while power +1.0% and employee +6.5% on revenue +18.8%", note_ref: "S Notes 31-36 p.133-135", rating: "YELLOW", why: "FY25 margin carried a stock-build credit; FY26 cost lines flattered by fire period (LBF1)"}
  - {rank: 4, finding: "Undrawn sanctioned subsidiary term loans 3,126.32 L vs commitments 5,642.27 L; MCPL 16% drawn; C maturity table nil over 5 years and adds 54 L; instalment text contradictory", note_ref: "C Notes 18, 39B, 52", rating: "YELLOW", why: "Funding path of new-subsidiary capex leans on parent (LBF4)"}
  - {rank: 5, finding: "Stated liens 2,545.72 L exceed all term deposits 242.24 L; liquidity 298.62 L is mostly margin money", note_ref: "S Notes 7, 14, 23d, 39B", rating: "YELLOW", why: "Liquidity cushion overstated or collateral text wrong (LBF4)"}
  - {rank: 6, finding: "Star OCI share (168.32) L; comprehensive share 574.37 L vs profit share 742.70 L; no unrealised profit policy for associates", note_ref: "C Notes 1.2, 17, 46, 49", rating: "YELLOW", why: "Associate profit quality (LBF3)"}
  - {rank: 7, finding: "Schedule III FY26 table misses C equity by 645.97 L (Toyal row printed (702.25) vs (56.28))", note_ref: "C Note 50 p.239; Note 39C p.221", rating: "YELLOW", why: "Disclosure error; MEPL loss is 70% of its cash equity, no impairment test shown"}
  - {rank: 8, finding: "Forward MTM payable 57.02 L vs OCI hedge reserve 10.12 L gross; 46.90 L counter-entry not found; FVTPL vs cash flow hedge vs debt-instrument labels; 39B sensitivity opposite to Note 51", note_ref: "S Notes 25, 39A, 39B, 51", rating: "YELLOW", why: "Derivative accounting trail incomplete"}
  - {rank: 9, finding: "77% of FY26 credit-loss charge (53.26 of 68.81 L) is on the non-current other receivable, not trade debtors", note_ref: "S Notes 7, 11, 36", rating: "YELLOW", why: "Receivable risk sits outside the clean trade ageing"}
  - {rank: 10, finding: "Segment returns on segment assets: foils 3.2%, conductors 13.7% (PY 21.1%), insulators (9.4%), powder 18.4%", note_ref: "C Note 44 p.226-227", rating: "YELLOW", why: "Mix and capital intensity behind margin (LBF1)"}
red_flags: []
questions_for_mgmt:
  - "Has the insurer accepted the 793.05 L claim, and how much has been received since 31 March 2026?"
  - "What explains the 580.63 L of subsidiary reimbursement flows with no closing balance?"
  - "What is the nature and age of the 703.86 L non-current other receivables, and why is 77% of the credit-loss charge on them?"
  - "What caused the 67.9% rise in raw material stock?"
  - "What were the PPE disposal and debris proceeds from the fire, and why does the cash flow add back only 23.45 L of PPE losses?"
  - "What collateral stands behind the 2,000 L Federal Bank lien when term deposits total 242.24 L?"
  - "How will the 5,642.27 L of group capital commitments be funded against 3,126.32 L of undrawn subsidiary term loans?"
  - "Why did Star's OCI fall by 168.32 L (group share), and is unrealised profit on sales to Toyal eliminated?"
receivables_trend: "stable to improving: trade receivables net 8,822.61 L vs 8,951.34 L (-1.4%) on revenue +18.8%; days 39.2 vs 47.2 (FY24 36.0); not due 96.3% (PY 92.9%); over 6 months 104.89 L = 1.18% of gross (PY 32.04 L = 0.36%); other non-current receivables 703.86 L at 40% reserve is a separate watch item and carries 53.26 L of the 68.81 L FY26 credit-loss charge"
restatements_found:
  - "None material. FY25 comparatives differ from AR2025 by under 2 L in several lines; Note 56 says regrouped"
  - "Not a restatement: C Note 50 FY26 Schedule III table misstates Toyal net assets by 645.97 L; reported equity, profit and OCI tie"
going_concern_language: "NONE as doubt. Only objective text: 'Safeguard the Company's ability to continue as going a going concern' (S Note 39C, p.142)"
analyst_note: "Pass 2 adds ten YELLOW items, no RED. Three Pass 1 statements corrected: guarantees are not backed 1:1 by deposits (242.24 L deposits vs 445.72 L), Toyal Schedule III row misprinted, FX unhedged position differs between Note 39B and Note 51. Two readings are held open: P2-1 (cash flow add-back omitted vs undisclosed proceeds) and P2-2 (fire disruption vs FY25 stock-build inflation). Anchors use [page N] of the .txt; printed page = N minus 5. All figures INR Lakhs; derived items flagged. accounting_quality stays 6 pending Pass 3."
```
