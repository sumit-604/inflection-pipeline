# STAGE 2, PASS 1: NOTES TO FINANCIAL STATEMENTS, FULL EXTRACTION
Company: TD Power Systems Ltd (TDPOWERSYS) | Run date: 2026-11-15 | Document: TDPOWERSYS_Annual_Report_FY2025-26.pdf (text route: TDPOWERSYS_Annual_Report_FY2025-26.txt)
Model: claude-sonnet-5-5 | Pass 1 of 3 | No B02 block is due from pass 1.

## 0. READ BASIS AND CONVENTIONS

- UNIT. Every statement and note in this annual report prints "Amounts in Indian Rupees in lakhs, except as otherwise stated" (standalone p.126 header; consolidated p.194 header). Every figure below is in Rs LAKH as printed, unless I write "cr". Where I write a Rs cr figure it is my own division by 100 and is marked "(cr, my conversion)". Stage 10 converts once. 1 cr = 100 lakh.
- PAGES. Anchors cite the PDF page number (the "[page N]" marker in the .txt, same as the PDF page index). The text file repeats each two-page spread twice (PDF p.132 and p.133 hold the same text, and so on), so I read one copy of each spread. The printed page footers are 12 numbers lower than the PDF page on the standalone side (for example PDF p.142 carries printed pages 154-155). I cite PDF pages only.
- SCOPE READ. Standalone: Notes 1 (corporate information, policies 1.1 to 1.26) to 57, PDF p.132 to p.182, plus the primary statements (balance sheet, P&L, equity, cash flow, PDF p.126 to p.131) for tie-outs. Consolidated: balance sheet, P&L, cash flow (p.194, p.198), policies 1.1 to 1.4 and 1.28 to 1.30 (p.200 to p.210), Notes 2 to 55 (p.210 to p.248), and the consolidated auditor's emphasis of matter (p.184). I did not read consolidated policies 1.5 to 1.27 line by line (p.202 to p.209); a text search shows the policy numbering matches the standalone set, and the differences I found sit in 1.1 (principles of consolidation), 1.28 to 1.30 (Turkey hyperinflation, subsidiary list). Treat consolidated policy text as unread beyond that.
- RATINGS. Green = clean. Yellow = watch. Red = red flag. I rate no finding Red in Pass 1. The highest Yellow items are listed in the Pass 1 Summary.
- NOT FOUND IN DOCUMENT is used wherever an expected disclosure is absent. I estimate nothing.
- Standalone is "S", consolidated is "C". "Note X (S)" and "Note X (C)" are different numbering: consolidated notes run one higher from Note 16 onward (for example S Note 15 equity = C Note 16; S Note 44 related parties = C Note 44; S Note 36 contingent = C Note 39).

## 1. FIRST VERIFICATION PRIORITY (load-bearing facts the notes can settle)

### 1.1 Guidance vs delivery
- The notes cannot settle the guidance path. H1 FY27 revenue of Rs 1,481.5 cr and the FY27 guidance bands are outside this annual report.
- FY26 base from the notes: consolidated revenue from operations 1,85,623.38 lakh (C P&L, p.194), standalone 1,71,666.38 lakh (S Note 26, p.158). FY25: 1,27,876.17 lakh (C) and 1,26,539.62 lakh (S).
- Arithmetic only, my conversion: C FY26 revenue is Rs 1,856.2 cr. A FY27 band of Rs 2,900 to 3,000 cr (the Q2 FY27 presentation figure from the stage context) implies +56.2% to +61.6% on that base. The context's "Rs 2,400 cr+" opening guidance implies about +29.3%.
- Order book / remaining performance obligations: NOT FOUND IN DOCUMENT. Note 26 (S) and Note 27 (C) give contract balances only (p.158, p.226). No unsatisfied performance obligation table is disclosed.
- Capacity-linked items in the notes: capital commitments 4,008.73 lakh (PY 7,855.88) (S Note 36, p.162); CWIP 1,732.46 lakh, all plant and machinery, all under one year (S Note 3, p.144); PPE additions 10,302.84 lakh (S Note 2, p.142). The Tumkur (Vasanthanarasapura) 15-acre KIADB land: possession 30 Jan 2024, lease-cum-sale agreement 11 Mar 2024 for 10 years, Rs 214.85 lakh differential allotment charges capitalised in FY26 (S Note 4, p.144). Nameplate capacity: NOT FOUND IN DOCUMENT in the notes.

### 1.2 Customer concentration (confirmed, with a reconstruction)
- C Note 42(ii) (p.238): Customer A 23.17% (PY 14.10%), Customer B 10.74% (PY 12.32%) of consolidated revenue. Confirms the stage context.
- S Note 42(ii) (p.170): Customer A 25.06% (PY 14.25%), Customer B 24.08% (PY 28.23%), Customer C 11.62% (PY 12.45%) of standalone revenue. Confirms "three customers above 10%".
- RECONSTRUCTION (my arithmetic on the printed figures). S Note 44 (p.174, p.176) sales to the three subsidiaries total 16,707.65 + 24,368.53 + 266.14 = 41,342.32 lakh. 41,342.32 / 1,71,666.38 = 24.08%. PY: 12,322.25 + 23,181.61 + 213.03 = 35,716.89 lakh, / 1,26,539.62 = 28.23%. Both match S Customer B to the second decimal. So S "Customer B" is the three subsidiaries taken together, not an external customer. This is an inference from an exact arithmetic match; the note does not say it.
- The external pair in the consolidated note then ties to standalone: S Customer A 25.06% x 1,71,666.38 = 43,020 lakh; C Customer A 23.17% x 1,85,623.38 = 43,009 lakh. S Customer C 11.62% x 1,71,666.38 = 19,947 lakh; C Customer B 10.74% x 1,85,623.38 = 19,936 lakh. So external Customer A is about 43,000 lakh and external Customer B about 19,940 lakh. Together 33.9% of consolidated revenue. Customer names: NOT FOUND IN DOCUMENT.
- Receivable concentration (S Note 40C, p.166; C Note 41C, p.234): two customers or groups hold 40,655.40 lakh in both sets (S 57.37% of 70,865.41; C 54.79% of 74,208.77). C Customer A 43.07%, Customer B 11.72%. S Customer A 45.10%, B 12.27%. PY S had three customers (A 27.10%, B 15.86%, D 24.02%).
- UNVERIFIED LINK: the receivable letters (A, B) and revenue letters (A, B, C) sit in different notes and the document does not say they name the same parties. If receivable Customer A is revenue Customer A, then receivable 31,961 lakh (43.07% x 74,208.77) against FY26 revenue of about 43,009 lakh is about 74% of a year of billing (about 271 days). Treat as a question for management, not a finding.

### 1.3 Cash conversion
- C cash flow (p.198): CFO 12,906.76 lakh vs PAT 23,877.49 lakh = 54.05% (my division). PY 3,952.27 / 17,457.51 = 22.64%. Matches the stage context (54% and 23%).
- S cash flow (p.130): CFO 11,479.64 / PAT 21,644.35 = 53.04%. PY 629.19 / 15,371.00 = 4.09%.
- Debtor days (my calculation, year-end receivables over annual revenue x 365). C: 74,208.77 / 1,85,623.38 = 145.9 days; PY 43,733.89 / 1,27,876.17 = 124.8. S: 150.7 days; PY 139.7. The context's 146 FY26 equals my consolidated figure.
- Receivables jumped 69.7% in C (43,733.89 to 74,208.77) against revenue +45.2%. S receivables +46.3% (48,427.58 to 70,865.41) against revenue +35.7%.
- Q4 loading: S Note 53 (p.180) books show receivables of 47,415.69 (Q1), 51,719.80 (Q2), 53,977.05 (Q3), 70,865.41 (Q4). Q4 alone added 16,888.36 lakh, 75.3% of the year's 22,437.83 lakh increase. Inventory books: 34,862.19, 36,617.65, 43,976.66, 49,681.21.
- "Other current liabilities Rs 190.3 cr": C Note 24 (p.226) other current liabilities 19,027.06 lakh = advance received from customers 18,717.26 + duties and taxes 309.80. So at 31 Mar 2026 the 190.3 cr is 98.4% customer advances. The H1 FY27 figure of Rs 430.3 cr is outside this document, so its nature at 30 Sep 2026 stays unconfirmed.
- Advances are mostly from subsidiaries on the standalone books: 11,729.80 lakh of S advances 17,205.21 (68.2%; PY 6,211.89 of 11,511.30, 54.0%) (S Note 23, p.158). By party (S Note 44, p.174, p.176): USA Inc 11,231.16 (PY 4,289.71), Europe GmbH 498.64 (PY 1,922.18), Turkey 113.65 (PY nil). The Turkey 113.65 lakh is not in the 11,729.80 total (11,231.16 + 498.64 = 11,729.80), which is a small disclosure mismatch.

### 1.4 Governance
- Promoter and promoter group holding at 31 Mar 2026 (S Note 15 VI, p.152; C Note 16 VI, p.220): 4,19,78,661 shares = 26.87% (13.22 + 8.30 + 5.08 + 0.19 + 0.08). At 31 Mar 2025: 5,18,78,661 = 33.22%. Shares sold in FY26: Saphire Finman 33,00,000, Nikhil Kumar 45,00,000, Hitoshi Matsuo 21,00,000 = 99,00,000 shares, 6.34% of 15,62,14,831 shares. The stage context's 26.51% and the SAST filing of 14 Nov 2026 are outside this document and not verified here.
- Nippon Life India Trustee: 7.98% (1,24,58,312) to 6.24% (97,53,276) (S Note 15 VII, p.152).
- Subsidiary transactions (S Note 44, p.174, p.176): Europe GmbH sales 24,368.53 + purchases and services from it 1,259.35 = 25,627.88 lakh (= Rs 256.3 cr, my conversion; matches the context). USA Inc sales 16,707.65 lakh (= Rs 167.1 cr; matches). Turkey 266.14.

## 2. NOTE-BY-NOTE EXTRACTION

### 2.1 Note 1: Corporate information and accounting policies (S p.132 to p.140; C p.200 to p.210)

| # | Finding | Anchor | Rating |
|---|---|---|---|
| 1 | Going concern basis; financial statements authorised 14 May 2026. Operating cycle 12 months. | Note 1, 1.1, 1.3, p.132 | Green |
| 2 | Revenue policy: point-in-time on transfer of title and risks. Clause (b): "Where dispatch has not been done but tests have been completed as per the terms agreed with the customer, revenue is the transaction price the Company expects to be entitled to." This permits revenue before dispatch. The Ind AS 115 bill-and-hold criteria (substantive reason, separately identified, ready for transfer, cannot be redirected) are NOT FOUND IN DOCUMENT. The amount of revenue booked before dispatch: NOT FOUND IN DOCUMENT. Finished goods in transit rose from nil to 4,461.43 lakh (Note 9). | Note 1.5, p.134; Note 9, p.148 | Yellow |
| 3 | PPE depreciation: straight line, "as prescribed under Schedule II ... or useful life estimated by management, whichever is lower". Lives: factory building 30 years, non-factory building 60, plant and machinery (double shift) 10, office equipment 5, furniture 10, computers 3, servers 6, communication 5, vehicles 8. Items under Rs 5,000 fully depreciated. Depreciation for a complete quarter on addition or deletion. No change in lives disclosed this year. | Note 1.7, p.134 | Green |
| 4 | Intangibles (technical know-how, licences, software) amortised over 5 years straight line. Research cost expensed; development cost capitalised only after feasibility. | Notes 1.8, 1.9, p.134, p.136 | Green |
| 5 | Interest on constructed assets capitalised on specific or weighted borrowings; "no amount of expenditure recognised in the carrying amount of an item of PPE in the course of its construction" is stated for CWIP (Note 3). Interest capitalised: NIL stated. | Notes 1.7, 1.19, p.134, p.140; Note 3, p.144 | Green |
| 6 | Impairment of non-financial assets: recoverable amount (higher of fair value less cost to sell and value in use). Discount rate and growth rate assumptions: NOT FOUND IN DOCUMENT (Note 51 gives qualitative reasoning only). | Note 1.10, p.136 | Yellow |
| 7 | ECL: simplified approach. A "provision matrix" is cited but, "considering ... engineered-to-order products ... the determination of a provision based only on age analysis may not be realistic". The provision is "determined by the management for the specific trade receivables". The matrix by age band is NOT FOUND IN DOCUMENT; only the total (1.11%) is shown. | Note 1.4(e), p.134; Note 1.22; Note 40C, p.166 | Yellow |
| 8 | Inventory: lower of cost and NRV, FIFO for raw material and bought-out items; WIP and finished goods include "appropriate portion of overheads". | Note 1.11, p.136 | Green |
| 9 | Employee benefits: gratuity funded with LIC, projected unit credit; remeasurements to OCI. ESOP via an ESOP trust: trust buys shares from market and shares held are treasury shares in other equity (policy text; no treasury share amount appears in other equity in Note 16). | Notes 1.12, 1.13, p.136 | Green |
| 10 | Ind AS 116: short-term and low-value exemptions; discount at incremental borrowing rate. Lease liability presented "as Borrowing" per policy text, but the balance sheet shows lease liabilities on a separate line. ROU asset is depreciated per policy over the shorter of life and lease term, yet Note 4 shows no depreciation on the ROU asset (see 2.4). | Note 1.14, p.136, p.138 | Yellow |
| 11 | Tax: statutory rate 25.17%; deferred tax by balance-sheet approach; DTA recognised only to the extent probable. | Note 1.15, p.138 | Green |
| 12 | Foreign currency: monetary items restated at closing rate through P&L. Overseas (Japan) branch translated "as if the transactions are those of the Company itself", with the difference taken to OCI. Policy text conflicts with itself: if the INR is the functional currency of the branch, no translation difference should arise in OCI, yet OCI shows an exchange difference on translation of foreign operations of 68.49 (PY 17.39) on a standalone basis. | Note 1.16(e), p.138; P&L OCI, p.126 | Yellow |
| 13 | Derivatives: forward contracts only, fair valued through P&L. | Notes 1.17, 1.18, p.140 | Green |
| 14 | EPS: share split adjusted retrospectively for all periods. | Note 1.24, p.140 | Green |
| 15 | Consolidation: line-by-line; intercompany balances, transactions and unrealised profit eliminated; excess of equity share over cost recorded as Capital Reserve (718.29 in C Note 17.1). Four subsidiaries, all 100%: DF Power Systems (India), TD Power USA, TD Power Europe GmbH, TD Power Jenerator (Turkey). | C Notes 1.1, 1.29, p.200, p.210 | Green |
| 16 | Turkey subsidiary restated under Ind AS 29 (hyperinflation) per policies 1.28 and 1.30. These policies state "the price index used and the effect of restatement are disclosed in the notes". The price index and the net monetary gain or loss: NOT FOUND IN DOCUMENT. Note 2 (C) shows hyperinflation effect columns of 377.68 gross and 198.66 depreciation in FY25 and nil in FY26, yet Note 34 (C) still deducts 23.77 (PY 27.99) of "depreciation on account of hyper inflationary reinstatement" in FY26. | C Notes 1.28, 1.30, p.210; C Note 2, p.210, p.212; C Note 34, p.228 | Yellow |
| 17 | Policy cross-reference error (S Note 1.2): estimates list points to "Note 46 and Note 36" for provisions, which are warranty and contingent liabilities; correct. Not a finding. | p.132 | Green |

### 2.2 Note 2: Property, plant and equipment (S p.142; C p.210, p.212)

Standalone, FY26 (lakh):

| Class | Gross opening | Additions | Disposals | Gross closing | Accum. dep. closing | WDV |
|---|---|---|---|---|---|---|
| Freehold land | 1,627.30 | nil | nil | 1,627.30 | nil | 1,627.30 |
| Buildings | 11,783.90 | 4,684.95 | nil | 16,468.85 | 5,047.35 | 11,421.50 |
| Plant and machinery | 28,468.63 | 4,998.24 | 43.40 | 33,423.47 | 21,795.23 | 11,628.24 |
| Office equipment | 434.85 | 64.12 | nil | 498.97 | 358.41 | 140.56 |
| Furniture | 438.00 | 49.59 | nil | 487.59 | 394.10 | 93.49 |
| Computers | 1,384.18 | 379.81 | 35.82 | 1,728.17 | 1,162.91 | 565.26 |
| Communication | 17.05 | nil | nil | 17.05 | 16.34 | 0.71 |
| Vehicles | 741.40 | 126.13 | 46.19 | 821.34 | 374.13 | 447.21 |
| Total A | 44,895.31 | 10,302.84 | 125.41 | 55,072.74 | 29,148.47 | 25,924.27 |
| R&D plant and machinery (B) | 1,600.92 | nil | nil | 1,600.92 | 1,520.84 | 80.08 |
| Total C | 46,496.23 | 10,302.84 | 125.41 | 56,673.66 | 30,669.31 | 26,004.35 |

- Net block 26,004.35 vs 17,573.37 (+48.0%). Depreciation for the year 1,843.85 (PY 1,517.76 per Note 2; P&L Note 33 shows 1,517.77, a 0.01 rounding difference).
- Plant and machinery: charge 1,092.07 on closing gross 33,423.47 = 3.3% a year, against a stated 10 year life; accumulated depreciation is 65.2% of gross (PY 72.9%: 20,740.91 / 28,468.63). A large fully depreciated base is still in use, so the run-rate charge will rise as the new 4,998.24 additions carry a full year. Rating: Yellow (earnings trend, not accounting error).
- Security: first pari-passu charge to Bank of Baroda, Kotak Mahindra Bank and HDFC Bank over Unit 1 and Unit 2 factory land and buildings (plots and survey numbers listed) and the hypothecation of all present and future plant and machinery (Note 2 notes A, p.142). Green.
- No revaluation; no benami property (notes B, C). Green.
- Consolidated: net block 26,429.93 (PY 18,066.82); FY25 table carried a hyperinflation uplift of 377.68 gross (Turkey), FY26 shows none (p.210, p.212).

### 2.3 Note 3: Capital work in progress (S p.144; C p.212)

- Closing 1,732.46 (PY 1,658.94): all plant and machinery in FY26; FY25 was plant 358.15 + factory building 1,300.79. Ageing: all under one year in FY26; PY 18.88 in 1 to 2 years (S Note 3, p.144).
- The movement table is internally odd: "Additions during the year 1,732.46" equals the closing balance, and "Capitalisation during the year 1,658.94" equals the opening balance. PPE additions (Note 2) are 10,302.84, so most capex went straight to PPE and the CWIP roll is presented as a proxy. Yellow (presentation).
- Capital advances (Note 8): 347.51 (PY 1,410.94). Capex commitments (Note 36): 4,008.73 (PY 7,855.88). Capital creditors (Note 22): 1,995.05 (PY 398.42, 5x). Green/Yellow: 1,995.05 of FY26 capex is unpaid at year end; cash capex line (S cash flow, p.130) is 10,376.36 for PPE, 433.77 for intangibles, 214.85 for leasehold land.

### 2.4 Note 4: Right of use assets and leases (S p.144; C p.212, p.214)

- Leasehold land ROU: opening 1,720.07, addition 214.85, closing 1,934.92 (PY 1,720.07 flat). No depreciation or amortisation on the ROU asset appears in either year, although policy 1.14 says the ROU asset is depreciated. The addition is "differential land allotment charges, including stamp duty and registration charges" for the KIADB Tumkur land under a 10 year lease-cum-sale, with the right to take ownership "subject to fulfilment of prescribed conditions". Rating Yellow: Rs 1,934.92 lakh of land carries no charge, and the capitalisation of land charges ties to a plant that is now partly commissioned (Buildings additions of 4,684.95 in FY26). Whether the Tumkur plant has started production is NOT FOUND IN DOCUMENT here.
- Lease liability 1.12 (PY 1.04): current 0.37, non-current 0.75. Maturity: up to one year 0.37, one to five years 0.37, over five years 0.38. Interest on lease liability below Rs 10,000, shown as nil. Rent on short-term leases (S) 49.73 (PY 32.43); (C) 281.65 (PY 182.12). Green.

### 2.5 Note 5: Other intangible assets (S p.146; C p.214)

- Net 1,005.39 (PY 941.35): software 89.40 (PY 121.46) and technical know-how 915.99 (PY 819.89). Additions: software 16.00; know-how 417.76 (PY 378.03). Amortisation 48.06 + 321.67 = 369.73 (matches P&L Note 33). Cash paid 433.77 = 417.76 + 16.00 (cash flow, p.130). So know-how is bought, not self-developed. Licensor names and amounts payable: NOT FOUND IN DOCUMENT. Green.
- R&D (Note 48, p.176): revenue R&D 732.90 employee + 139.60 other = 872.50 (PY 716.01 + 109.97 = 825.98, +5.6%); capital R&D nil. R&D expensed is about 0.51% of standalone revenue. Capitalised know-how of 417.76 is 32.4% of expensed R&D plus capitalised know-how together. Green.

### 2.6 Note 6: Investments (S p.146; C p.214)

| Entity | Number | Carrying FY26 | Carrying FY25 |
|---|---|---|---|
| D F Power Systems Pvt Ltd (India) | 59,99,998 shares of Rs 10 | 2,040.75 gross, less provision (2,040.75) = nil | 2,040.75 less (1,740.75) = 300.00 |
| TD Power Systems USA Inc | 80,100 shares of USD 10 | 481.78 | 481.78 |
| TD Power Systems Europe GmbH | 5,50,000 shares of EUR 1 | 414.12 | 414.12 |
| TD Power Systems Jenerator Sanayi A.S. (Turkey) | 12,782 shares of Lira 100 | 159.35 | 159.35 |
| Shamrao Vithal Co-op Bank (FVTPL) | 2,000 shares of Rs 25 | 0.50 | 0.50 |
| Total | | 1,055.75 | 1,355.75 |

- Subsidiary investments (A) total 1,055.25 (PY 1,355.25). Sum check: 481.78 + 414.12 + 159.35 = 1,055.25. DF Power is now fully provided: the Rs 300.00 lakh annual provision in FY25 and FY26 took the cumulative provision from 1,440.75 (FY24, my subtraction) to 2,040.75. The exceptional item should not recur after FY26 on this investment because the carrying value is nil. Rating: Yellow for the two-year recurrence, with the recurrence now structurally exhausted.
- No ICDs or loans to subsidiaries outstanding at either year end. FY25 had repayment of 352.33 and interest 9.51 (cash flow, p.130); the maximum loan outstanding in FY25 was 352.33 (Note 44, p.174). FY26: nil. Non-convertible debentures: matured for 1,000.00 in FY25; none in FY26. Green.
- Loss-making subsidiaries (C Note 46k, p.244): DF Power loss (8.75) (PY (6.23)), Turkey loss (61.12) (PY (25.35)). Profitable: USA Inc 1,232.93 (PY 1,519.84), Europe GmbH 609.74 (PY 299.11). Net assets: DF Power 821.61, USA 1,846.21, Europe 1,943.51, Turkey 738.28. Rating: Yellow for the losses in Turkey, which doubled in the year.

### 2.7 Notes 7 and 8: Other financial and non-current assets (S p.148; C p.216)

- Other financial assets (non-current) 225.23 (PY 156.72): electricity deposit 221.45, other deposits 3.78. Green.
- Other non-current assets: 1,470.91 (PY 2,603.70): capital advances 347.51 (PY 1,410.94), advance tax net 522.28 (585.15), balance with government 6.11 (361.14), prepaid 111.89 (0.15), gratuity excess of plan assets over DBO 483.12 (246.32). The drop in capital advances (1,063.43) tracks the capex commissioning. Green.
- C Note 8 differs from S only in "balance with government authorities" 47.90 vs 6.11 (p.216).

### 2.8 Note 9: Inventories (S p.148; C p.216)

| Category (S) | FY26 | FY25 |
|---|---|---|
| Raw materials | 23,617.47 | 17,571.08 |
| Work in progress | 16,067.23 | 11,233.14 |
| Work in progress - spares | 3,712.01 | 3,087.97 |
| Finished goods in transit | 4,461.43 | nil |
| Stock in trade | 274.93 | 724.38 |
| Goods in transit - raw materials | 1,548.14 | 528.95 |
| Total | 49,681.21 | 33,145.52 |

- Total +49.9% against standalone revenue +35.7%. Days on revenue (my calculation): 105.6 (PY 95.6).
- Finished goods in transit of 4,461.43 is new. At group level C Note 9 adds "finished goods with subsidiary companies" of 624.70 (PY 4,512.87): the group finished-goods stock moved from 4,512.87 at the subsidiaries to 4,461.43 in transit at the parent plus 624.70 at subsidiaries (C Note 31, p.228). Total C inventory 50,305.91 (PY 37,658.39).
- "There are no allowances towards slow and non-moving items during the year." Nil write-down; no obsolete stock disclosure. Rating: Yellow (an inventory base up half in a year with no allowance, in a made-to-order business where policy says "engineered-to-order").
- Note 28 raw materials: opening 17,571.08 + purchases 1,29,913.40 - closing 23,617.47 = consumption 1,23,867.01 (ties). Copper 28,548.77, steel and laminations 16,239.31, shaft forgings 8,090.49, stores 1,694.29, others 69,294.15.

### 2.9 Note 10: Trade receivables (S p.148; C p.216)

Face of note (S, lakh): considered good and secured by letter of credit 496.92 (PY 2,569.87); unsecured good 70,368.49 (PY 45,857.71); credit impaired 797.61 (PY 772.61); less ECL (797.61) (PY (772.61)). Net 70,865.41 (PY 48,427.58).

Standalone ageing at 31 Mar 2026 (lakh, undisputed, considered good):

| Bucket | Amount | % of 70,865.41 |
|---|---|---|
| Not due | 60,970.74 | 86.0% |
| Under 6 months | 9,082.67 | 12.8% |
| 6 months to 1 year | 412.21 | 0.6% |
| 1 to 2 years | 123.73 | 0.2% |
| 2 to 3 years | 204.19 | 0.3% |
| Over 3 years | 71.87 | 0.1% |
| Total | 70,865.41 | |

- Credit impaired 797.61, all over 3 years, with a matching ECL of 797.61 (bucket allowances: 5.23 under 6 months; 6.40; 2.48; 40.73; 742.77 over 3 years). The ageing table shows allowance amounts in the under-6-month buckets (5.23) against balances shown as "considered good", so the bucket allowance total is spread against good balances while the credit-impaired row is only over 3 years. Presentation is loose. Yellow (minor).
- Over 6 months, considered good (S): 412.21 + 123.73 + 204.19 + 71.87 = 812.00 = 1.15% of net receivables. PY: 967.60 + 247.53 + 70.73 + 33.96 = 1,319.82 on 48,427.58 = 2.73%.
- Consolidated ageing (C p.216): not due 62,381.68 (84.1% of 74,198.65 good); under 6 months 11,305.94; 6 to 12 months 205.61; 1 to 2 years 29.36; 2 to 3 years 204.19; over 3 years 71.87; credit impaired undisputed 624.09; disputed credit impaired 183.64 (allowance 173.52). The consolidated set shows a "disputed" row of 183.64. The standalone set shows none, and S Note 10(e) says there are no receivables under dispute "except as disclosed above". The credit-impaired total in the two sets also differs (S 797.61 gross; C 624.09 + 183.64 = 807.73 gross), while both carry an ECL of exactly 797.61. Yellow: the two sets classify the same impaired balances differently.
- ECL movement (S Note 40C, p.166): opening 772.61, made during the year 25.00, closing 797.61 (PY 636.27, 136.34, 772.61). The FY26 charge of 25.00 does not appear as a P&L line: Note 34 "Provision for doubtful debts" is "-" for FY26 (136.34 for FY25), and the cash flow add-back is also nil. Where the 25.00 was charged: NOT FOUND IN DOCUMENT. Separately, S Note 40C liquidity paragraph (p.168) gives net trade receivables as 70,890.41, which is 70,865.41 + 25.00. Yellow.
- Related party receivables included: 6,070.37 (8.6% of net; PY 11,621.00, 24.0%) (S Note 10(b), p.148). Ties to Note 44: Europe 2,034.68 + USA 3,770.06 + Turkey 265.63 = 6,070.37. PY: 10,334.20 + 1,065.12 + 221.68 = 11,621.00.
- Terms: "non interest bearing and generally on terms of 0 to 180 days" (S Note 10(d)).
- Trend (3 years): days on revenue S 150.7 (FY26), 139.7 (FY25). FY24: NOT FOUND IN DOCUMENT in this report. Direction: worsening on a revenue basis.
- Security: borrowings carry an exclusive first charge to Bank of Baroda on "current assets relating to orders from a particular customer" (Note 19, p.156). The customer is not named. Yellow.

### 2.10 Notes 11 to 14: Cash, bank balances, other financial assets, other current assets (S p.150; C p.218)

- Cash and equivalents 1,617.82 (PY 2,447.00): current accounts 881.76, EEFC 728.44, deposits under 3 months nil (PY 900.00), cash 7.62. C: 7,834.03 (PY 7,496.30), including 2,487.68 deposit with original maturity under 3 months at a subsidiary (C Note 11).
- Other bank balances 11,950.11 (PY 12,313.24): deposits under 12 months 6,455.34; deposits under lien as margin money for bank guarantees 5,475.41 (PY 5,433.71); unclaimed dividend 4.41; ESOP trust balance 14.95. Deposits are concentrated: Bank A 10,298.13 of 11,930.75 total deposits (86.3%) (S Note 40C, p.166). A co-operative bank holds 400.00. Yellow (concentration, a scheduled bank).
- Other financial assets (current) 4,444.47 (PY 3,329.99): GST refund receivable 3,608.52 (PY 2,063.08, +74.9%); interest accrued 336.77; accrued export incentive 368.85 (PY 496.21); unbilled revenue 18.65 (44.27); forward MTM gain nil (PY 181.98). C Note 13: GST refund receivable 4,306.97 (PY 2,802.69) includes Rs 698.34 lakh (PY 739.61) of accumulated service tax and GST credit at the Indian subsidiary with "no operation ... the accumulated credit ... will be utilised ... on appropriate business opportunity" (p.218). See 2.30 for the GST demand against that credit. Yellow.
- Other current assets: advances to suppliers 2,484.49 (PY 2,088.38); input tax credit 2,384.66 (PY 2,992.15); prepaid 316.65. Green.

### 2.11 Notes 15 and 16 (S) / 16 and 17 (C): Share capital and other equity (S p.150 to p.154; C p.218 to p.222)

- Authorised 17,50,00,000 shares of Rs 2 (3,500.00). Issued and paid 15,62,14,831 shares (3,124.30), up 31,219 shares from ESAR exercises (PY 13,511). Par value is "Rs 10/- each (sub-divided into Rs 2/- each)". The sub-division date: NOT FOUND IN DOCUMENT in the notes. All share counts and per-share figures in this report, including PY, are on the Rs 2 basis (EPS PY 9.84 on 15,61,80,650 weighted shares, p.164). Share-count basis statement for downstream stages: Rs 2 face value throughout, PY restated.
- No bonus shares, buyback or non-cash issue in the five preceding years (Note 15 III). No QIP or preferential allotment appears in the share capital note as at 31 Mar 2026 (only ESAR allotments of 31,219 shares). Any such corporate action is after the balance sheet date or outside this document. Events after the balance sheet date other than the proposed dividend: NOT FOUND IN DOCUMENT (no subsequent events note exists).
- Promoter holdings: see 1.4. FY25 percentages in the standalone PY table for 31 Mar 2024 (Saphire 15.41%, Nikhil 12.34%, Hitoshi 6.46%) differ from the consolidated table for the same date (15.34%, 12.29%, 6.43%) on the same share counts (2,39,58,225; 1,91,93,320; 1,00,40,486). 2,39,58,225 / 15,61,70,101 = 15.34%. So the standalone 31 Mar 2024 percentages are mis-stated. Green/Yellow (typographic).
- Other equity S 99,757.77 (PY 80,464.89): securities premium 19,383.57; capital redemption reserve 230.42; general reserve 2,955.06; retained earnings 77,012.34 (PY 57,888.91); stock options outstanding 148.38 (PY 92.48); exchange translation reserve 28.00 (PY (23.25)). Retained earnings roll: 57,888.91 - 1,015.20 - 1,561.92 + 21,644.35 + 56.20 = 77,012.34 (ties). C other equity 1,04,052.13; exchange reserve (648.22) (PY (318.81)); capital reserve 718.29.
- Dividends: FY26 interim Rs 1.00 per share (1,561.92); FY25 final Rs 0.65 paid in FY26 (1,015.20); proposed FY26 final Rs 1.10 (Note 47, p.176; not accrued). Interim 1.00 + proposed 1.10 = 2.10 per share against 0.60 + 0.65 = 1.25 (PY). On my arithmetic, 1,561.92 + (1.10 x 15,62,14,831 = 1,718.36) = 3,280.28 on PAT 21,644.35 = 15.2% (PY (937.10 + 1,015.20) / 15,371.00 = 12.7%). Green.
- Exchange difference reserve movement in S (51.25 credit) mirrors an OCI gain on the standalone Japan branch translation, which clashes with policy 1.16(e) (see 2.1 #12). C: reserve fell by (329.41). Yellow.

### 2.12 Note 17 (S): Provisions (non-current) and Note 24 (S): Provisions (current)

- Non-current compensated absences provision 980.10 (PY 886.17). Current: warranty 840.15 (PY 615.17), compensated absences 44.52 (PY 29.80); total 884.67 (PY 644.97) (p.154, p.158).
- Warranty roll (Note 46, p.176): opening 615.17, provision for the year 224.98, closing 840.15. FY25: 467.89 + 147.28 = 615.17. The roll shows no utilisation, write-back or reversal in either year (closing = opening + provision). Either claims are charged to expense directly or none is paid. Warranty provision as a share of revenue: 0.489% (FY26), 0.486% (FY25). Consolidated roll (C Note 47, p.244): 620.88 + 233.45 = 854.33; FY25 shows "withdrawn and credited to P&L" of 1.35. Yellow: a warranty provision that only accumulates.
- Litigation provisions: none recognised (see 2.15).
- Onerous contracts: policy only (1.26); no provision. Decommissioning: NOT FOUND IN DOCUMENT (none expected).

### 2.13 Note 18 (S) / 19 (C): Deferred tax (S p.154; C p.222)

- Net DTL 180.08 (PY 330.72 S; 276.79 C). DTL on depreciation 1,050.90 (PY 882.38); DTA on expenditure timing differences 612.94 (PY 321.13); DTA on employee benefits 257.88 (PY 230.53). Deferred tax credit in P&L (150.64) (PY charge 294.52). C: DTL on depreciation 1,104.83; credit (96.71).
- The DTA on "timing differences in recognition of expenditure" nearly doubled (+291.81). Nature of the expenditure: NOT FOUND IN DOCUMENT. Likely linked to MSME payables disallowed under section 43B(h) (Note 21 says MSME dues increased "pursuant to amendment to Sec.43B(h)"). That link is my inference, not stated. Green/Yellow.
- No unrecognised DTA; no MAT credit. Green.

### 2.14 Note 39 (S) / 40 (C): Income tax reconciliation (S p.164; C p.232)

- S: PBT 29,407.57 x 25.17% = 7,401.30; add non-deductible expenses 232.71 (PY 209.60) and other adjustments 129.21 (PY 71.43); total tax 7,763.22. Effective rate 26.40% (PY 26.51%).
- C: PBT 32,611.71 x 25.17% = 8,207.72; non-deductible 157.21; different tax rates of subsidiaries +240.08 (PY (287.80)); other incl. eliminations 129.22; total 8,734.22. Effective 26.78% (PY 24.64%). The swing in the foreign-rate line from (287.80) to +240.08 is 527.88 and moves the consolidated effective rate 2.1 points. Yellow (explains why consolidated tax grew 53.0% while consolidated PBT grew 40.8%).
- Current tax liability (net) 2,349.12 (PY 973.75; C 2,783.00 / 1,171.13), which "includes provisions held for earlier years pending completion of assessments/appellate proceedings" (Note 25 S, p.158). Current tax charged 7,913.86; tax paid 6,135.95 (S cash flow). Yellow (liability up 141%).

### 2.15 Note 36 (S) / 39 (C): Contingent liabilities and commitments (S p.162; C p.230, p.232)

| Item (lakh) | FY26 | FY25 | Stage / assessment |
|---|---|---|---|
| Performance guarantees | 12,246.21 | 11,159.24 | Not probable |
| Performance guarantees for subsidiaries | 1,400.45 | 1,567.43 | Not probable |
| Advance guarantees for subsidiaries | nil | 69.05 | |
| Indirect tax demand disputed | 120.85 | 6.89 | |
| Income tax demand disputed | 1,986.03 | 1,986.03 | AY 2017-18 transfer pricing, High Court stay |
| Other sums | 13.12 | 10.42 | |
| Total (my sum) | 15,766.66 | 14,799.06 | |

- Total is 15.3% of standalone net worth 1,02,882.07 (PY: 14,799.06 / 83,588.56 = 17.7%). Performance guarantees alone are 11.9% of net worth: a single item above 10% of net worth. Performance guarantees grew 9.7% against revenue +35.7%. Bank guarantees for subsidiaries outstanding: Europe 971.42 + Turkey 429.02 = 1,400.44 (S Note 44), matching the 1,400.45 line. Rating Yellow (normal for the sector, large against net worth).
- Income tax: demand of 1,942.67 in May 2021 for AY 2017-18, with the TPO applying transfer pricing "on the overall turnover ... instead of restricting to transactions with Associate Enterprises" (associate sales 1,964.90 against total sales 36,944.03 in that year). DRP objection filed 26 May 2021; High Court of Karnataka stay on 30 Jun 2021 and again on 21 Mar 2022 after the DRP-directed assessment order. Table shows 1,986.03 against text 1,942.67 (difference 43.36, not explained). Interest-bearing demand outstanding for 4+ years while the group's sales to subsidiaries are now 41,342.32 lakh (24.1% of revenue): related-party pricing is a standing tax exposure. Yellow.
- C extra: the Indian subsidiary received a KGST/CGST order for 2017-18 to 2023-24 raising a demand of 824.87 lakh (including GST 412.43) for ineligible input credit availed with no outward supplies; an appeal is filed (C Note 39, p.232). The consolidated contingent table (120.85 indirect tax) is identical to the standalone figure, so the 824.87 demand is not in the table totals and appears only in text. Consolidated contingent total including it: 16,591.53 lakh (my sum), 15.5% of consolidated net worth 1,07,176.43. Yellow.
- Capital commitments: 4,008.73 (PY 7,855.88).
- Guarantees given for subsidiaries: 1,400.45 performance guarantees; no loan guarantees.

### 2.16 Note 19 (S) / 20 (C): Borrowings (S p.156; C p.224)

- Only working capital cash credit, repayable on demand: 1,809.62 (PY 1,220.75), split Bank of Baroda 1,792.35, HDFC Bank 17.27 (the text labels the 17.27 under the Kotak paragraph heading and the HDFC text, so the allocation of 17.27 between Kotak and HDFC is unclear; the table gives Bank of Baroda 1,792.35 and one other figure of 17.27). Rates: Bank of Baroda 8.15% (PY 9.55%), Kotak Mahindra 8.70% (10.35%), HDFC 7.90% (8.90%); "reviewed annually". Floating in practice (reset annually) while Note 40C calls the borrowings "fixed rate". Yellow (minor).
- Security: first pari-passu charge on all current assets, excluding current assets of orders from "a particular customer" which carry an exclusive first charge for Bank of Baroda; collateral of factory land, buildings and plant (as in Note 2). No default. Covenants: NOT FOUND IN DOCUMENT. Repayment schedule: not applicable (on demand). Borrowings from related parties: nil. Term debt: nil.
- Finance cost 190.32 (PY 305.84), of which interest paid on bank borrowings 68.29 (PY 21.32) and interest accrued on delayed MSME payments 122.03 (PY 284.52). 68.29 + 122.03 = 190.32 and 21.32 + 284.52 = 305.84 (my sums tie to the rupee lakh). So 64.1% of FY26 finance cost, and 93.0% of FY25, is statutory interest on late payments to micro and small suppliers. Yellow.

### 2.17 Note 21 (S) / 22 (C): Trade payables (S p.156, p.158; C p.224, p.226)

- Total 38,646.15 (PY 22,982.36, +68.2%); MSME principal 4,871.60 (PY 2,380.30, +104.7%); others 33,774.55 (PY 20,602.06). C total 41,172.68 (PY 23,085.86).
- Ageing: every payable is in "less than 1 year - includes amounts which are Not Due" (MSME 4,871.60; others 33,754.55) plus disputed 20.00 over 3 years (both years). No finer bucket is given, so overdue amounts and the 45-day MSME overdue split are NOT FOUND IN DOCUMENT.
- MSME: principal due 4,871.60; interest due and unpaid 122.03 (PY 284.52); further interest that would be due in coming years 648.33 (PY 526.30). The amount in line 6 is not provided for. The MSME balance "increased pursuant to amendment to Sec.43B(h) of Income tax Act" (the note says so). Interest paid in the year beyond the appointed day: nil. Yellow.
- Payable days on revenue (my calculation): 82.2 (PY 66.3). Note 54 payables turnover 4.27 vs 5.13 (-16.76%) (p.180). Payables funded 15,423.79 of working capital (S cash flow) against 20,754.43 absorbed by receivables and 16,535.69 by inventory.
- Dues to related parties 206.60 (PY 10.81): Europe GmbH.
- Supplier finance arrangements: Note 55 (S) says the Ind AS 7/107 amendment "had no effect"; none disclosed. Green.

### 2.18 Notes 22 and 23 (S) / 23 and 24 (C): Other financial liabilities and other current liabilities (S p.158; C p.226)

- Other financial liabilities S 11,970.89 (PY 8,881.50): accrued expenses 8,566.50 (PY 7,616.03); capital creditors 1,995.05 (398.42); employee benefits payable 723.09 (857.64); MTM loss on forwards 674.82 (PY nil); due to director 4.87 (4.28); unclaimed dividend 4.41. Accrued expenses are not broken down (8,566.50 is 71.6% of the line, 5.0% of revenue). C accrued expenses 10,224.97 (PY 8,891.96). Yellow (undisclosed nature).
- Other current liabilities S 17,478.50: advance from customers 17,205.21 (PY 11,511.30, +49.5%); duties and taxes 273.29. Related party advances 11,729.80 of that (see 1.3). C 19,027.06: advances 18,717.26 (PY 12,672.68, +47.7%). Revenue recognised from opening contract liabilities: 10,211.88 (PY 5,120.50), 88.7% of the 11,511.30 opening S advances (p.158). Green on roll; Yellow on the dependence of working capital on advances via the USA subsidiary (11,231.16, up 161.8%).
- "Due to Director" 4.87 equals the MD's year-end outstanding (Note 44). Green.

### 2.19 Note 26 (S) / 27 (C): Revenue from operations (S p.158; C p.226)

| Standalone line (lakh) | FY26 | FY25 | Change |
|---|---|---|---|
| AC generators | 1,44,917.49 | 99,944.30 | +45.0% |
| AC generator spares/components | 19,722.25 | 20,134.18 | -2.0% |
| Spares and aftermarket - domestic | 679.02 | 682.18 | -0.5% |
| Spares and aftermarket - overseas branch | 2,702.86 | 2,126.88 | +27.1% |
| Sale of goods | 1,68,021.62 | 1,22,887.54 | +36.7% |
| Services | 2,607.04 | 2,933.10 | -11.1% |
| Scrap | 2,371.68 | 2,230.52 | +6.3% |
| Gross | 1,73,000.34 | 1,28,051.16 | |
| Less sales to Japan branch | (1,333.96) | (1,511.54) | |
| Revenue from operations | 1,71,666.38 | 1,26,539.62 | +35.7% |

- Consolidated adds "From Subsidiary offices" 56,558.67 (PY 37,579.40, +50.5%), then removes sales to Japan branch (1,333.96) and sales to subsidiaries (42,601.67; PY 36,242.85) to reach 1,85,623.38. Reconciliation: 42,601.67 = S sales to subsidiaries 41,342.32 + purchases and services from the Europe subsidiary 1,259.35 (my sum). Ties.
- Point in time 1,70,393.30 (S) and over time 2,607.04. Contract balances: trade receivables 70,865.41, customer advances 17,205.21, unbilled revenue 18.65. No remaining performance obligation disclosure: NOT FOUND IN DOCUMENT.
- Scrap sales 2,371.68 are taken into revenue. 1.4% of standalone revenue. Green.
- Export and domestic split (S Note 42, p.170): domestic including deemed exports 73,438.95 (PY 84,769.65, -13.4%); exports 96,858.53 (PY 41,154.63, +135.4%). Of export sales, 41,342.32 (42.7%) go to the group's own subsidiaries. Standalone domestic revenue shrank while exports more than doubled. Yellow (mix shift; the domestic number falls 11,330.70 lakh).

### 2.20 Notes 27 to 35 (S): Income and expense line items (S p.160, p.162)

- Other income 2,000.91 (PY 2,309.44): interest on bank deposits 744.47 (1,074.45); FX fluctuation and MTM gain net 1,203.42 (1,146.79); interest on NCDs nil (35.57); interest on loans to subsidiaries nil (9.51); misc 53.02. FX gain is 4.1% of PBT before exceptional items and 60.1% of other income. Yellow (recurring but volatile; the MTM forward loss of 674.82 sits in liabilities, so the 1,203.42 is net of it).
- Employee benefits 14,715.63 (PY 11,137.98, +32.1%): salaries 10,453.38; PF 801.26; whole-time directors 521.62; sitting fees 31.70; share-based 118.20 (PY 55.20); staff welfare 2,789.47 (PY 2,078.28). Green.
- Other expenses 10,828.07 (PY 8,777.50, +23.4%): travelling and conveyance 2,361.46 (1,675.22, +41.0%); carriage, freight and selling 2,373.56; power and fuel 1,370.69; legal and professional 824.91 (715.32); software 670.99; bank charges 514.97; CSR 337.89; royalty 64.89 (71.61); manufacturing expenses 338.77 (146.21, 2.3x); auditors: audit fee 15.75, limited review 10.05, other services 3.12. Royalty payee is NOT FOUND IN DOCUMENT and no royalty appears in the related party list. Green/Yellow.
- Bank charges are shown net of a reimbursement of 37.53 received from a subsidiary (PY 0.97). Green.
- EBITDA excluding other income (Note 40D, p.168): 17.54% (PY 16.66%) standalone. My recompute: (29,707.57 + 2,213.58 + 190.32 - 2,000.91) / 1,71,666.38 = 17.54% (ties). Consolidated: 17.77% (PY 18.05%) (C Note 41D, p.236). My recompute: (32,611.71 + 2,299.35 + 190.32 - 2,129.82) / 1,85,623.38 = 17.76% (ties). So standalone margin rose 0.88 points while consolidated margin fell 0.28 points.
- Exceptional item (Note 35): (300.00) in both years, DF Power investment provision.

### 2.21 Note 40 (S) / 41 (C): Financial instruments and risk (S p.164 to p.168; C p.232 to p.236)

- Classification table: S financial assets at amortised cost: cash 1,617.82; bank 11,950.11; receivables 70,865.41; other 4,669.70. Liabilities at amortised cost: borrowings 1,809.62; payables 38,646.15; other 11,296.07. Level 2 forward MTM loss 674.82 (PY gain 181.98). Level 3 investment 0.50.
- Credit risk: see 1.2, 2.9, 2.10. Statement that credit risk is "well contained" sits beside a receivable base where one customer group is 45.10%. Yellow.
- Liquidity: contractual maturities within one year S 52,427.03 (PY 33,084.83) against cash and bank 13,567.93 (S). Statement says "no liquidity risk is perceived." Cash figures inside the paragraph conflict: PY cash and bank is 14,459.24 in the credit risk paragraph (p.166) and 14,760.24 in the liquidity paragraph (p.168). The balance sheet gives 2,447.00 + 12,313.24 = 14,760.24, so 14,459.24 is a typo. Green/Yellow.
- Foreign currency (S p.168 to p.170):
  - Forwards: EUR 120.00 lakh (12 contracts) at Rs 12,728.97 lakh (implied rate Rs 106.07 per EUR); PY EUR 333.00 lakh at Rs 31,596.06 lakh. No USD or JPY forwards disclosed.
  - Recognised exposure at 31 Mar 2026 (foreign currency lakh): USD assets 68.42, liabilities including advances 171.59; EUR assets 342.26, liabilities 43.85; JPY assets 1,121.19, liabilities 1,052.93. Rupee equivalents: EUR receivables 37,035.97 vs payables 4,780.35; USD receivables 6,452.98 vs liabilities 15,633.86.
  - Net EUR position 298.41 lakh against forwards of 120.00 lakh: 40.2% hedged (my division) against PY net EUR 236.44 lakh with forwards 333.00 lakh (140.8%). Cover on the recognised Euro book fell from above 100% to 40%. The forwards may also hedge forecast sales, which the note does not say. Yellow.
  - 5% sensitivity on P&L before tax: EUR 1,612.78 (PY 1,080.88), USD 459.04 (PY 110.61), JPY 31.64. The EUR sensitivity is 5.4% of PBT before exceptional items.
  - The EUR receivable of 37,035.97 lakh is 52.3% of standalone net receivables, and mostly relates to the German subsidiary and euro customers; the split is NOT FOUND IN DOCUMENT (Europe subsidiary receivable is only 2,034.68).
- Interest rate: "Fixed rate interest bearing deposits" and bank borrowings that "bear fixed rate" yet "reviewed periodically". Commodity: "The Company hedges major raw materials based on dips" (copper 28,548.77 lakh consumed). The hedge instruments are not disclosed (only EUR forwards are listed as derivatives). Yellow.
- Capital management: monitors EBITDA and dividends only. No debt covenant data.

### 2.22 Note 38 (S) / 38 (C): EPS (S p.164; C p.230)

- S basic 13.86 (PY 9.84); diluted 13.85 (9.84). Weighted shares 15,61,98,750 basic and 15,62,24,585 diluted: dilution of 25,835 shares (0.017%). C basic 15.29 (PY 11.18), diluted 15.28 (11.17). All on a Rs 2 face value basis with PY restated.
- Dilution sources: ESARs. At year end outstanding ESARs: not vested 32,970; vested not exercised 54,607 (Rs 2 FV) and 2,757 (Rs 10 FV). Total 90,334 units. Green.

### 2.23 Note 43: Employee benefits (S p.170 to p.174; C p.238 to p.240)

- Gratuity (funded, LIC conventional insurance 100% of plan assets): DBO opening 1,970.81, service cost 213.64, interest 125.94, actuarial gain (75.10), benefits paid 125.28, closing 2,110.01. Plan assets opening 2,217.13, interest income 153.67, contributions 347.61 (PY 220.24), benefits paid 125.28, closing 2,593.13. Net asset 483.12 (PY 246.32), shown under other non-current assets. The employer paid 347.61 into a plan already in surplus. Green.
- Assumptions: discount rate 7.10% (PY 6.60%); salary escalation 7.00% (7.00%); withdrawal 3.00%; retirement 58 years; mortality IALM 2006-08 Ultimate. Sensitivity (1% discount rate): (200.96) / +236.01. Expected payments: under 1 year 87.60; 1 to 2 years 170.53; 5 to 10 years 736.91. Green. Discount rate rose 50 basis points and drove the FY26 actuarial gain of 75.10. Green.
- Leave liability (unfunded): opening 915.97, service 240.35, interest 53.31, actuarial loss 31.39, paid 216.40, closing 1,024.62. Split: non-current 980.10 and current 44.52 (sum 1,024.62, ties). Green.
- Defined contribution: PF 570.58 (PY 429.30), ESI 61.91 (41.98). Green.
- Labour Codes (Note 56 S, Note 53 C): notified 21 Nov 2025; "no material impact has been identified on the gratuity liability, leave liability". No quantification given. Yellow (the claim of nil impact is stated without a number).

### 2.24 Note 42: Segment reporting (S p.170; C p.238)

- Single segment (AC generators and electric motors). Geography (S, lakh): domestic 73,438.95 (84,769.65); export 96,858.53 (41,154.63); overseas branch 2,702.86 (2,126.88); less Japan branch (1,333.96) (1,511.54).
- C geographies add "sales of overseas branch and subsidiary" 59,261.53 (PY 39,706.28) and eliminate subsidiary sales (42,601.67). Non-current assets outside India (C): 435.53 (PY 500.36). The export country split is NOT FOUND IN DOCUMENT.
- Major customers: see 1.2. Green on disclosure, Yellow on concentration.

### 2.25 Note 44: Related party disclosure (S p.174, p.176; C p.242)

Related parties (S): subsidiaries DF Power, TD Power USA, Europe GmbH, Turkey; companies in which KMP or relatives are interested: Trident Automobiles Pvt Ltd, Trident Automobiles (Bangalore) Pvt Ltd, Trilegal; KMP: Nikhil Kumar (MD), Mohib N Khericha (Chairman), S Prabhamani, Prathibha Sastry, Rahul Matthan, Karl Olof Alexander Olsson, Bharat Rajwani (CS), Deepak Kumar Sinha (CEO from 2 Apr 2026), M N Varalakshmi (CFO). No new related party appears in the list against the PY, except Trilegal's first transaction (8.58, nil PY).

Transaction table (S, lakh):

| Party | Relationship | Nature | FY26 | FY25 | YoY |
|---|---|---|---|---|---|
| TD Power USA Inc | Subsidiary | Sale of generators, spares, supervision | 16,707.65 | 12,322.25 | +35.6% |
| TD Power USA Inc | Subsidiary | Trade advance received (balance) | 11,231.16 | 4,289.71 | +161.8% |
| TD Power USA Inc | Subsidiary | Receivable (balance) | 3,770.06 | 1,065.12 | +254.0% |
| TD Power USA Inc | Subsidiary | ICD repaid / interest | nil | 279.00 / 9.51 | |
| TD Power Europe GmbH | Subsidiary | Sale of generators, spares, services | 24,368.53 | 23,181.61 | +5.1% |
| TD Power Europe GmbH | Subsidiary | Purchases and services availed | 1,259.35 | 525.96 | +139.4% |
| TD Power Europe GmbH | Subsidiary | Receivable (balance) | 2,034.68 | 10,334.20 | -80.3% |
| TD Power Europe GmbH | Subsidiary | Trade advance received (balance) | 498.64 | 1,922.18 | -74.1% |
| TD Power Europe GmbH | Subsidiary | Bank guarantee outstanding | 971.42 | 2,240.81 | -56.6% |
| TD Power Europe GmbH | Subsidiary | Payable by TDPS (balance) | 206.60 | 10.81 | |
| TD Power Turkey | Subsidiary | Sale of spares | 266.14 | 213.03 | +24.9% |
| TD Power Turkey | Subsidiary | Receivable / advance / BG | 265.63 / 113.65 / 429.02 | 221.68 / nil / 47.24 | |
| TD Power Turkey | Subsidiary | BG charges reimbursed | 37.09 | nil | |
| DF Power | Subsidiary | Provision for diminution of investment | 300.00 | 300.00 | |
| Nikhil Kumar | MD | Short-term benefits incl. commission 410.00 (PY 333.00) | 509.66 | 432.66 | +17.8% |
| Nikhil Kumar | MD | Other long-term benefit | 11.96 | 11.96 | |
| Nikhil Kumar | MD | Dividend received | 213.93 | 209.92 | |
| M N Varalakshmi | CFO | Short-term benefits | 96.12 | 71.32 | +34.8% |
| Bharat Rajwani | CS | Short-term benefits | 28.35 | 24.97 | +13.5% |
| S Prabhamani | Non-exec director | Consultancy charges | 31.92 | 10.76 | +196.7% |
| Sitting fees | Five directors | Total 31.70 (PY 28.40) | | | |
| Trident Automobiles Pvt Ltd | KMP-interested | Vehicle purchase 80.93; servicing 2.16 | 83.09 | nil | new |
| Trident Automobiles (Bangalore) | KMP-interested | Servicing | 0.28 | 0.20 | |
| Trilegal | KMP-interested | Professional services | 8.58 | nil | new |

- Subsidiary sales as share of standalone revenue: 41,342.32 / 1,71,666.38 = 24.1% (PY 28.2%). Subsidiary sales rose 15.8% against standalone revenue +35.7%. Related-party receivables fell from 24.0% to 8.6% of net receivables. Standalone receivables from the Europe subsidiary fell by 8,299.52 lakh. So the standalone receivable build is overwhelmingly external.
- Arm's-length basis for subsidiary pricing: NOT FOUND IN DOCUMENT (and the open AY 2017-18 transfer pricing dispute is on exactly this subject). Pricing of the Europe purchases (1,259.35, up 139%): NOT FOUND IN DOCUMENT.
- No loans to promoter entities; no promoter rent or royalty disclosed. Vehicle purchase from Trident Automobiles (80.93) is a KMP-interested party transaction. Trident and Trilegal relationships are not defined in the note. Yellow.
- CONSOLIDATED KMP PAY (C p.242), not shown in the standalone table: Nikhil Kumar short-term benefits 1,299.09 (PY 992.78, +30.9%), of which commission 995.02 (PY 713.41, +39.5%); standalone shows 509.66 and commission 410.00. So subsidiaries paid him 789.43 lakh in total and 585.02 lakh of commission (my subtraction), none of which is in the standalone related party note. C Note 32 whole-time director remuneration 1,311.05 (PY 1,004.74) = 1,299.09 + 11.96 (ties). Total MD remuneration is 4.0% of consolidated PBT (1,311.05 / 32,611.71) and 5.5% of consolidated PAT. Subsidiary commission basis and approvals: NOT FOUND IN DOCUMENT. Yellow.
- Sitting fees in C are higher than in S for the same directors (Mohib 8.15 vs 7.35; S Prabhamani 5.60 vs 4.80; Nikhil Kumar 0.80), i.e. subsidiaries pay fees too.
- Performance guarantees on behalf of subsidiaries 1,400.45 are not in the transaction table (they are in Note 36). Green/Yellow.

### 2.26 Note 45: Operating lease (S p.176; C p.242)

- Short-term, cancellable leases only (offices, guesthouse, employee residences). Rent S 49.73; C 281.65 (PY 182.12). Green.

### 2.27 Note 46 (S) / 47 (C): Warranty provision; Note 41 (S): Other disclosures

- See 2.12 for warranty. S Note 41 (p.170): no pending litigation affecting financial position beyond Note 36; no IEPF transfers; no intermediary funding. Green.

### 2.28 Note 47 to 49 (S): Dividend, R&D, CSR (S p.176)

- Dividends: see 2.11. R&D: see 2.5.
- CSR: required 337.55 (PY 242.45); spent 337.89 (242.45); no shortfall; no related-party channel. Activities: education, school infrastructure, health care, sports training. Green.

### 2.29 Note 50: Employee stock benefit plans (S p.178; C p.246)

- Plan instituted August 2019 (up to 10,00,000 shares: 5,65,000 by trust secondary acquisition, 4,35,000 fresh). Grants: 5,63,884 ESOPs and 3,99,216 ESARs. Exercise price Rs 2. Black-Scholes inputs: reissued ESAR market price Rs 254.70, volatility 49.91 to 51.22%, risk-free 6.99 to 7.03%, dividend yield 0.39%, fair value Rs 159.35 per vest; earlier ESAR market price Rs 134.45, fair value Rs 78.92.
- FY26: 31,219 shares allotted to the trust on 38,333 ESARs exercised (PY 13,511 shares on 14,075). ESARs issued in the year 27,000 (reissue). Outstanding at 31 Mar 2026: 32,970 not vested, 54,607 vested not exercised (Rs 2 FV), 2,757 vested not exercised (Rs 10 FV, pre-split units).
- Expense 118.20 (PY 55.20, +114%). Stock options outstanding reserve 148.38 (PY 92.48). Dilution is below 0.1% of shares. Total number of options and ESARs granted by employee class, and the ESOP counts vs the 5,63,884 grant: NOT FOUND IN DOCUMENT for ESOPs (the table shows ESARs only; the status of the 5,63,884 ESOPs is not shown). Green/Yellow.
- The 2,757 ESARs carried "face value Rs 10" after the split should translate into 13,785 Rs 2 units; the note leaves them unconverted. Yellow (minor, share-basis hygiene).

### 2.30 Note 51 (S) / 52 (C): Impairment of subsidiary; going concern of Indian subsidiary (S p.178; C p.246)

- S Note 51: exposure 2,040.75 lakh in DF Power equity. DF Power's net worth "continues to remain positive ... owing to substantial reduction in accumulated losses arising from write-backs recognised in earlier years" relating to claims and counterclaims with creditors over project equipment and cancelled projects. Going concern depends on "expected improvement in market conditions and continued operational and financial support from the Parent Company". Impairment test "in accordance with Ind AS 36 considering the subsidiary's past operating performance, current level of business operations, expected realisation of claims and counterclaims". Additional provision 300.00 in FY26; cumulative 2,040.75. Discount rate, growth rate and projections: NOT FOUND IN DOCUMENT.
- C Note 52: same text and "awaiting improvement in market conditions which is gradually recovering due to the receding pandemic". The pandemic reference is stale text. The consolidated auditor's EMPHASIS OF MATTER (p.184, "Our opinion is not modified"): "the Independent auditor of the subsidiary mentioned in note no. 52 ... has expressed material uncertainty that may cast significant doubt about the subsidiary's ability to continue as a going concern", with the group auditor judging the subsidiary "not material to the group".
- Going concern language therefore exists for DF Power (material uncertainty by its own auditor; group auditor emphasis; management's going concern basis). Its financial anchors: net assets 821.61 (PY 830.36), loss (8.75), GST credit asset 698.34 held in the group's "GST refund receivable" and an open demand of 824.87 lakh against it. Rating Yellow (subsidiary-level, not material to the group, but the parent's "operational and financial support" is a stated dependency).

### 2.31 Note 52 (S) additional disclosures (S p.178)

- No struck-off company balances, no unregistered charges, no crypto, not a wilful defaulter, no undisclosed income, layers compliance. Note 52(f): "no material uncertainty exists ... that the Company is capable of meeting its liabilities ... within a period of one year" (standalone parent). Going concern language for the parent: positive assurance. Green.

### 2.32 Note 53 (S) / 51 (C): Quarterly statements filed with banks (S p.180; C p.246)

| Quarter | Item | Per bank | Per books | Difference |
|---|---|---|---|---|
| Q1 | Inventory | 31,327.16 | 34,862.19 | (3,535.03) |
| Q1 | Receivables | 47,416.22 | 47,415.69 | 0.53 |
| Q2 | Inventory | 32,416.38 | 36,617.65 | (4,201.27) |
| Q2 | Receivables | 52,464.06 | 51,719.80 | 744.26 |
| Q3 | Inventory | 38,431.50 | 43,976.66 | (5,545.16) |
| Q3 | Receivables | 55,038.24 | 53,977.05 | 1,061.19 |
| Q4 | Inventory | 45,721.24 | 49,681.21 | (3,959.97) |
| Q4 | Receivables | 71,138.56 | 70,865.41 | 273.15 |

- Reasons given: inventory differs because of "conversion/carrying cost of inventory, inventory in Japan branch and material at port"; receivables differ for "Japan branch related trade receivables adjustment as per sanctioned terms". Q1 to Q3 books are unaudited. Receivables submitted to banks exceeded books in each quarter, up to 1,061.19 lakh (Q3), while inventory submitted was below books. With cash credit of only 1,809.62 and cash of 13,567.93, drawing power is not a binding constraint. Yellow (minor): the pattern is a consistent receivables overstatement of up to 2.0% of books in bank statements, though the amounts are small.
- Q4 jump in books (see 1.3). The Q1 to Q3 figures also give an intra-year read: receivables rose 16,888.36 in the last quarter alone.

### 2.33 Note 54: Ratios (S p.180)

| Ratio | FY26 | FY25 | Variance |
|---|---|---|---|
| Current ratio | 1.97 | 2.27 | (13.27%) |
| Debt equity | "Not Applicable. As closing balance of borrowing is NIL" | | |
| Debt service coverage | 24,048.25 / 68.29 = 352.15 | 17,561.91 / 21.32 = 823.73 | (57.25%) |
| ROE | 0.23 | 0.20 | 16.07% |
| Inventory turnover | 4.15 | 4.45 | (6.77%) |
| Receivables turnover | 2.88 | 3.18 | (9.63%) |
| Payables turnover | 4.27 | 5.13 | (16.76%) |
| Net capital turnover | 2.43 | 2.15 | 12.96% |
| Net profit ratio | 0.13 | 0.12 | 3.80% |
| ROCE | 0.23 | 0.21 | 11.17% |

- CONTRADICTION: the debt-equity ratio is reported as not applicable because "closing balance of borrowing is NIL", but Note 19 shows borrowings of 1,809.62 at year end (and the same note's DSCR and ROCE use total debt). Yellow.
- The DSCR variance of 57.25% exceeds the 25% threshold the note itself sets ("less than 25%, hence no reasons are mentioned"). The reason given is "increased utilisation of borrowings", yet the explanation field for the other ratios is blank for variances below 25%, consistent. Debt service uses 68.29 of interest only, so the ratio is not a debt-repayment cover ratio. ROCE numerator uses PAT + D&A + finance cost (not EBIT), which flatters ROCE relative to pre-tax. Green/Yellow.
- Receivables turnover 2.88 (about 127 days on average receivables); payables turnover 4.27 (about 85 days). Averages use 59,646.50 and 30,814.26. Green.

### 2.34 Notes 55 to 57 (S) / 54 and 55 (C): Pronouncements, labour code, comparatives (S p.182; C p.248)

- Amendments to Ind AS 1 (current/non-current with covenants), Ind AS 12 (Pillar Two), Ind AS 7/107 (supplier finance), Ind AS 21 (lack of exchangeability): all stated to have no effect. Ind AS 1 amendments effective 1 Apr 2026: no expected effect (no term debt). Green.
- Prior period: "regrouped where necessary ... impact ... not material" (Note 57 S, Note 55 C). No restatement with an amount is disclosed. Restated items: NOT FOUND IN DOCUMENT. Green.
- The consolidated Labour Code note (C Note 53) says "no adjustment has been considered necessary in the Standalone Financial Statements" inside the consolidated set, a copy-paste slip. Green/Yellow.

### 2.35 Cash flow statement cross-checks (S p.130; C p.198)

- S CFO 11,479.64 (PY 629.19); capex (10,376.36 + 433.77 + 214.85) = 11,024.98; free cash flow before dividends 454.66 (my subtraction); dividends paid (2,577.12); closing cash and equivalents 1,617.82. Working capital absorbed (14,194.82) in S (PY (16,091.88)). C CFO 12,906.76 (PY 3,952.27); working capital (15,113.09); capex 10,418.02 + 433.76 + 214.85 = 11,066.63; FCF before dividends 1,840.13 (my subtraction).
- "Unrealised foreign exchange loss/(gain)" add-back (256.76) (PY (1,257.00)) and "Net foreign exchange difference on translation of foreign operations (51.25)" shown inside the financing section. Green/Yellow.
- Interest received in investing 797.89 (S) is shown against interest income of 744.47 in the P&L. Green.

## 3. TIE-OUTS RUN (no break unless listed)

Ties: PPE roll to balance sheet 26,004.35; intangibles 1,005.39; investments 1,055.75; inventories 49,681.21; Note 28 consumption 1,23,867.01; Note 30 change in inventories; retained earnings roll; deferred tax; warranty roll; leave liability 1,024.62 = 980.10 + 44.52; related receivables 6,070.37 and 11,621.00; sale-to-subsidiary elimination 42,601.67; finance cost 190.32 = 68.29 + 122.03; EBITDA margin 17.54% and 17.76%; consolidated PAT = parent 21,644.35 + DF (8.75) + USA 1,232.93 + Europe 609.74 + Turkey (61.12) + consolidation adjustment 460.34 = 23,877.49.
Breaks and mismatches (all small): CWIP movement lines; related advances 11,729.80 vs 11,843.45 (Turkey 113.65); ECL charge 25.00 not in P&L; liquidity paragraph receivables 70,890.41; PY cash and bank 14,459.24 vs 14,760.24; contingent income tax 1,942.67 text vs 1,986.03 table; debt-equity "borrowing NIL"; 31 Mar 2024 promoter percentages; consolidated contingent table excludes the 824.87 demand; hyperinflation columns vs Note 34.
The consolidation adjustment to profit of +460.34 (PY +299.14) is 1.9% of consolidated PAT and is not explained in the notes (the group inventory at subsidiaries fell by 3,888.17, which would release eliminated unrealised profit; that mechanism is my inference).

## 4. NOT FOUND IN DOCUMENT (expected disclosures that are absent)

1. Remaining performance obligations / order book (Ind AS 115).
2. Bill-and-hold criteria and amount of revenue booked before dispatch (policy 1.5(b)).
3. Impairment test assumptions (growth and discount rates) for the DF Power investment.
4. ECL matrix by ageing band; where the FY26 ECL charge of 25.00 sits in the P&L.
5. Ind AS 29 price index and net monetary gain or loss for Turkey.
6. Events after the balance sheet date (no note); QIP or preferential allotment (not in this document).
7. Share sub-division date (the note states only "sub-divided into Rs 2/-").
8. Customer names (A, B, C), and the "particular customer" with the exclusive Bank of Baroda charge.
9. Payables ageing beyond "less than 1 year includes not due"; MSME overdue beyond 45 days.
10. Royalty and know-how licensor names; arm's-length basis for subsidiary pricing; basis of subsidiary-paid commission to the MD.
11. Borrowing covenants.
12. ESOP (as distinct from ESAR) status counts.
13. Export country split; capacity data.

## 5. PASS 1 SUMMARY: TOP 10 FINDINGS, RANKED BY INVESTOR IMPORTANCE

| Rank | Finding | Anchor | Rating |
|---|---|---|---|
| 1 | Receivables up 69.7% (C) and 46.3% (S) against revenue +45.2% and +35.7%. Debtor days 145.9 (C), up from 124.8. Q4 alone added 16,888.36 lakh (75.3% of the S year increase). CFO/PAT 54.05% (C), up from 22.64%, but still half of profit. Ageing is clean (86.0% not due; over 6 months 1.15% of net) and ECL is 1.11%. | Note 10 p.148 / p.216; Note 53 p.180; cash flow p.198 | Yellow (high) |
| 2 | Two customer groups hold 40,655.40 lakh of receivables (S 57.37%; C 54.79%); Customer A alone 43.07% (C) / 45.10% (S). Two external customers are 33.9% of C revenue (23.17% and 10.74%). S "Customer B" 24.08% equals subsidiary sales exactly. The letter link between receivable A and revenue A is unverified; if it holds, A's receivable is about 74% of its yearly billing. | Note 40C p.166; Note 41C p.234; Note 42(ii) p.170 / p.238; Note 44 p.174 / p.176 | Yellow (high) |
| 3 | Standalone domestic revenue fell 13.4% (84,769.65 to 73,438.95) while export rose 135.4% (41,154.63 to 96,858.53); 42.7% of exports are sales to group subsidiaries (41,342.32). Subsidiary pass-through advances of 11,729.80 lakh fund 68.2% of S customer advances. Arm's-length basis and the AY 2017-18 transfer pricing demand (1,986.03) sit on this same relationship. | Note 42 p.170; Note 44 p.174 / p.176; Note 23 p.158; Note 36 p.162 | Yellow (high) |
| 4 | Promoter group sold 99,00,000 shares (6.34% of equity) in FY26; holding 33.22% to 26.87%. Separately, the MD's consolidated pay is 1,299.09 lakh (commission 995.02) against 509.66 (commission 410.00) in the standalone related party note: 789.43 lakh paid by subsidiaries is outside the standalone table. Total 4.0% of consolidated PBT. | Note 15 VI p.152; C Note 44 p.242; S Note 44 p.174 | Yellow |
| 5 | Euro cover cut: forwards EUR 120.00 lakh against net EUR position 298.41 lakh (40.2%), from EUR 333.00 lakh against 236.44 lakh (140.8%) a year earlier. MTM swing from gain 181.98 to loss 674.82. FX gain 1,203.42 is 60.1% of other income. 5% EUR move = 1,612.78 lakh before tax. | Note 40C p.168 / p.170; Notes 13, 22; Note 27 p.160 | Yellow |
| 6 | Revenue policy allows recognition before dispatch when tests are complete; finished goods in transit rose from nil to 4,461.43 lakh; no bill-and-hold criteria, no amount, and no remaining-performance-obligation disclosure. Inventory +49.9% with no slow-moving allowance. | Note 1.5 p.134; Note 9 p.148 | Yellow |
| 7 | Finance cost is 64.1% interest on late payments to MSME suppliers (122.03 of 190.32; PY 93.0%). MSME principal doubled to 4,871.60; unprovided further interest 648.33; payable days 82.2 (66.3). Payables ageing has no overdue split. | Notes 21, 32 p.156 / p.158 / p.160 | Yellow |
| 8 | Contingencies: total 15,766.66 lakh (15.3% of S net worth); performance guarantees 12,246.21 (11.9% of net worth, one item above 10%); income tax demand 1,986.03 under High Court stay; Indian subsidiary GST demand 824.87 lakh appears only in text, outside the table, against a 698.34 lakh GST asset kept on the balance sheet. | Note 36 p.162; C Note 39 p.230 / p.232; C Note 13 p.218 | Yellow |
| 9 | Going concern language: DF Power's own auditor flagged material uncertainty; the group auditor carries an emphasis of matter (opinion unmodified); the investment is now provided to nil after 300.00 in each of FY25 and FY26; no impairment inputs disclosed. The parent's "continued operational and financial support" is stated as a dependency. Immaterial to the group today. | Note 51 p.178; C Note 52 p.246; auditor's report p.184 | Yellow |
| 10 | Disclosure inconsistencies that point to loose closing controls but change no total: ECL charge of 25.00 not in P&L; debt-equity ratio "not applicable, borrowing is NIL" against 1,809.62 of borrowings; ROU land of 1,934.92 with no depreciation; warranty provision with no utilisation; bank-submitted receivables above books by up to 1,061.19 lakh. | Notes 10, 40C, 54, 4, 46, 53 | Yellow (minor) |

Rating count: Red 0, Yellow 10 headline items (plus the minor Yellows in the note-by-note tables), Green on the core mechanics (PPE roll, intangibles, tax, gratuity, equity roll, ESOP, CSR, borrowings default status, tie-outs to the primary statements).
No 🔴 in this pass. The pass-1 read supports a working view that the notes are internally consistent in the totals and loose in labelling, and that the cash and concentration items (ranks 1 to 3) are what an investor should carry forward. Pass 2 should re-read the notes against this list and report only new items.
