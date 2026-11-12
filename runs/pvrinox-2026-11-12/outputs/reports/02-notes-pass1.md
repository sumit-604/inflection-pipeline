# STAGE 2 NOTES, PASS 1 (full extraction): PVRINOX, run 2026-11-12

Source: Annual_Report_2026.txt / .pdf (FY2025-26, 309 pp). All figures are in Rs MILLION (face of document: "Rupees in millions", p.248 onward). Nothing is converted. "Rs Cr" appears only where the company itself prints it.
Anchor form: (Note N, PDF p.X). PDF page = the "[page N]" marker; the printed page number is PDF page + 9 (e.g. PDF p.244 = printed 253).
Scope read: CONSOLIDATED notes 1 to 53 (PDF pp.244-305) in full, plus the consolidated primary statements (PDF pp.239-243) for tie-outs. STANDALONE notes (PDF pp.176-228) were NOT read line by line; only these standalone items were opened because they bear on the load-bearing facts: related parties (Note 44, pp.223-225), exceptional items, MSME disclosure, standalone P&L (p.172). Pass 2 and 3 should say so if they extend it.
Ratings: GREEN clean | YELLOW watch | RED red flag.

Input gaps carried: screener P&L, Balance Sheet, Cash Flow and Quarters CSVs absent; research/ empty; CINELINE has no concalls; sector_cap_row NOT FOUND. None of these limit a notes extraction. Receivable and payable days below use only this report's FY26 and FY25 columns. An FY24 (third-year) trend is NOT FOUND IN DOCUMENT.

---------------------------------------------------------------
## 0. LOAD-BEARING FACTS, CHECKED FIRST

### 0.1 Net cash / net debt (fact 1)
Separate lines, consolidated, Rs million:

| Line | 31-Mar-26 | 31-Mar-25 | Anchor |
|---|---|---|---|
| Non-current borrowings | 4,592 | 9,198 | Note 17, p.271; BS p.239 |
| Current borrowings (all current maturities of term loans) | 2,994 | 5,710 | Note 20, p.273 |
| of which commercial paper | nil | 1,487 | Note 20, p.273 |
| Total borrowings, carrying (net of transaction cost) | 7,586 | 14,908 | Note 40, pp.293-294 |
| Total borrowings, principal (excl. transaction cost) | 7,601 | 14,938 (13,446 LT + 1,492 ST) | Cash-flow reconciliation, p.242 |
| Cash and cash equivalents | 5,883 | 5,225 | Note 12A, p.267 |
| Other bank balances (current) | 33 | 64 | Note 12B, p.267 |
| Bank deposits >12 months (in Other financial assets) | 51 | 97 | Note 12B, p.267; Note 5, p.263 |
| Lease liabilities, non-current | 52,634 | 56,339 | Note 18, p.272 |
| Lease liabilities, current | 7,571 | 6,499 | Note 18, p.272 |
| Total lease liabilities (Ind AS 116) | 60,205 | 62,838 | Note 18(a), p.272 |
| Supplier finance (payables moved out of Trade payables into Other financial liabilities) | 1,251 | 1,635 | Note 22, p.274; Note 2A(ii), p.258 |
| Deferred consideration (refundable), current | 2,036 | 2,124 | Note 22, p.274 |

Derived (arithmetic on the lines above, not a company figure):
- Borrowings less cash and bank balances (5,883 + 33 + 51) = 7,586 - 5,967 = 1,619 at FY26. FY25: 14,908 - (5,225 + 64 + 97 = 5,386) = 9,522. These tie to the company's own MD&A net debt of 1,619 and 9,522 (MD&A, PDF p.35, lines 3376-3379). Excluding the 51 of long-dated deposits the figure is 1,670.
- Ind AS 116 lease liabilities of 60,205 sit OUTSIDE that net debt. They are 7.9 times borrowings.
- Supplier finance of 1,251 and deferred consideration of 2,036 are also outside borrowings. Adding supplier finance only gives 2,870. The deferred consideration is described only as "Deferred Consideration (Refundable)" discounted at 9.50% (Note 40, p.294). Its counterparty and what it was paid for are NOT FOUND IN DOCUMENT.
- Company gearing ratio is long-term debt 7,586 + PPE payables 382 = 7,968 over equity 73,787 = 11% (FY25 20%). (Note 43, p.298). Lease liabilities excluded by design.

What funded the debt fall (borrowings 14,908 to 7,586, down 7,322):
- Cash-flow reconciliation (p.242): long-term proceeds 1,500, repayment (7,320); short-term proceeds 1,898, repayment (3,398). Net borrowing cash flow = -7,320. Closing LT 7,601; ST nil (opening 13,446 and 1,492).
- Sources in the cash-flow statement (p.241), FY26: operating cash flow of continuing operations 21,597; less lease payments (principal and interest) 11,847; less interest on borrowings 1,456; less capex 2,587 (payments for PPE, intangibles, CWIP, deposits, advances). Residual 5,707 before the subsidiary sale. This matches the company's "organic free cash flow of approximately INR 5,700 million" (MD&A, PDF p.35).
- Sale of Zea Maize: proceeds 2,221 (p.241, Note 41 p.294). Cash rose 658.
- So roughly 5,707 of the 7,320 net repayment came from operations after lease cash, and 2,221 from the divestment, with cash balance up 658. RATING: GREEN on the debt fall; YELLOW on completeness of the "net debt" frame because leases (60,205), supplier finance (1,251) and deferred consideration (2,036) are not in it.
- Interest rate: term loans floating, effective 7.22% to 12.00% (FY25 8.48% to 12.00%) (Note 17(iii), p.271). ECLGS loans nil (FY25 1,235) (Note 17(i), p.271). Undrawn committed facilities 2,591 (FY25 2,457) (Note 20(ii), p.273). A 100 bp rate change moves profit before tax by 124 (FY25 153) (Note 42, p.296).

### 0.2 Two earnings bases (fact 2)
Consolidated statement of profit and loss (PDF p.240, Rs million):

| Line | FY26 | FY25 |
|---|---|---|
| Profit before share of JV, exceptional items and tax | 2,757 | (3,579) |
| Exceptional items, net loss (Note 31) | 483 | nil |
| Profit before tax, continuing | 2,269 | (3,582) |
| Total tax, continuing | 508 | (934) |
| PAT, continuing operations | 1,761 | (2,648) |
| Loss before tax, discontinued | (188) | (161) |
| Exceptional gain on disposal of discontinued operations (Note 41) | 1,952 | nil |
| Tax on discontinued | 197 | nil |
| PAT, discontinued | 1,567 | (161) |
| Profit for the year | 3,328 | (2,809) |
| Attributable to owners | 3,341 | (2,796) |
| Basic EPS, continuing / discontinued / total (Rs) | 17.93 / 16.08 / 34.01 | (26.97) / (1.51) / (28.48) |

How the press numbers map (my reading, anchored):
- "Rs 176 Cr" = continuing PAT 1,761 million (Rs 176.1 Cr). It carries the 483 exceptional loss (Labour Codes 405 + CWIP provision 78). EPS Rs 17.93.
- "Rs 386 Cr" = INR 3,868 million, which the company states as "FY'26 Profit After Tax", including the Zea Maize gain, with "PAT from continuing operations INR 2,306 million" excluding the gain (MD&A, PDF p.35, lines 3372-3375). THESE TWO MD&A FIGURES DO NOT APPEAR IN THE AUDITED CONSOLIDATED STATEMENTS. The statements show 3,328 total and 1,761 continuing. Gaps are 540 and 545. The notes do not bridge them. RATING: RED for reconciliation (a disclosure inconsistency between management commentary and audited statements). Pass 3 should test whether 3,868 is a pre-exceptional or other non-GAAP basis.
- The standalone P&L shows profit 2,685 after a net exceptional GAIN of 800 (standalone p.172; MD&A note PDF p.95 line 8104: gain on Zea Maize disposal 1,270 less Labour Codes 392 less CWIP impairment 78). So the one-time gain is booked differently in the two sets: standalone puts it in exceptional items (+1,270); consolidated puts the gain (1,952) inside discontinued operations.
- Why the consolidated gain (1,952) exceeds the standalone gain (1,270): consolidated carrying net assets of the subsidiary at sale were 269 against proceeds of 2,221 (Note 41, p.294). Standalone carries the Zea Maize investment at cost 951 (150 + 801 per Note 44, pp.224-225), giving 1,270. The difference of 682 is group-level accumulated losses of Zea Maize. Derived.
- Recurring versus one-time within continuing profit: the 483 exceptional loss is excluded from "before exceptional items" profit of 2,752. Items INSIDE the 2,752 that the notes show as recurring but non-operating: liabilities written back 976 in other income (FY25 837) (Note 25, p.276); a further liabilities written back 871 netted in the lease cost table (FY25 790) (Note 18(d), p.272); mutual fund gains 236; interest 524. See finding F-2.
- Tax: effective rate on total profit before tax of 4,033 is 17.5% (tax 705 = 508 continuing + 197 discontinued) (Note 45, p.299). Deferred tax charge 716 in FY26 against a credit of 996 in FY25. Current tax is only 62 (Note 45). Cash tax paid is 1 (cash-flow, p.241). Profit growth is largely untaxed in cash terms because of brought-forward losses.
- EPS: dilution 411,669 shares (Note 33, p.278). FY25 diluted equals basic because dilution was anti-dilutive.

### 0.3 Screens added / closed, impairment on closures (fact 3)
- The screen counts are NOT in the notes. They are in management commentary only: 93 screens added, 18 exited, net 75, year-end 1,798 screens across 359 properties (PDF p.26, lines 2536-2540). NOT FOUND IN NOTES. Cross-reference only.
- What the notes show on closures:
  - Accelerated depreciation of 125 (FY25 217) "on account of change in estimate of useful lives ... resulting from Cinema closure earlier than planned or due to renovation" (Note 2.3(c), p.247). Falling 42%.
  - ROU assets: disposals/adjustments of 3,012 gross and 1,252 accumulated depreciation (Note 4B, pp.261-262). Footnote says these include ROU derecognised on closure before lease expiry or on renegotiation. Net derecognised ROU = 1,760.
  - Lease liability reversed on those events: 2,300 (FY25 2,714) (Note 18(a), p.272). Derived: 2,300 - 1,760 = 540 net credit from lease derecognition. Where that credit is booked is partly stated in the Note 28 footnote ("*Includes liability written back on termination of lease after adjusting ROU assets", p.276) and partly in "liabilities written back" 871 in Note 18(d). The split is NOT FOUND IN DOCUMENT.
  - PPE: disposals gross 589, accumulated depreciation 538, net 51 (Note 3, p.259). CWIP disposals/adjustments 2,697 reflects capitalisation, not write-off.
  - "The Group has neither revalued nor impaired its Property, plant and equipment during the year" (Note 3 point iv, p.259). So there is NO impairment charge on PPE or ROU of closed screens. The only impairment is CWIP of 78 on one property under landlord dispute, charged to exceptional items (Note 31(ii), p.278). Provision for suspended CWIP projects now 186 (FY25 108) (Note 3A, p.260). Suspended CWIP gross 186, all older than 3 years.
  - Goodwill and the ROU/PPE base are tested at a single CGU, "movie exhibition business as a single cash generating unit" (Note 2.3(g), p.249). Closed or underperforming screens therefore cannot be tested individually for impairment under the stated policy. RATING: YELLOW.
- Capex and openings: additions PPE 2,977 (FY25 3,919); CWIP additions 2,059; ROU additions 6,488 (FY25 5,354) (Notes 3 and 4B). Capital commitments 906 (FY25 906) (Note 36, p.291). Expenses capitalised to CWIP 300 (FY25 448), of which employee 160, rent for pre-operative period 33, architects 45 (Note 44, p.298).
- Capital-light mix (55% of additions) is NOT visible in the notes; ROU additions are 6,488 and leasehold improvements additions 1,130.

### 0.4 Related parties, contingents, goodwill, DTA (fact 4)
See sections 2, 3, 12 below. Headline numbers: related-party outflows about 1.0% of revenue; contingents 2,555 (my sum) = 3.5% of equity; goodwill 57,367 = 77.7% of equity and 36.7% of total assets; goodwill test discount rate 10.33% (down from 12.08%); DTA 5,184 including 3,252 on losses.

---------------------------------------------------------------
## 1. ACCOUNTING POLICIES AND CHANGES (Notes 2, 2A, 2B)

1.1 Basis. Ind AS, historical cost. Group = parent, PVR INOX Pictures Limited, PVR INOX Lanka Limited (100%), Zea Maize Private Limited (93.27% till 29-Jan-2026), and a 49% joint venture Devyani PVR INOX Private Limited (Note 1, p.244). Management states "no assumptions and estimation uncertainties that have a significant risk of resulting in a material adjustment within the next financial year" (Note 2.1(c), p.245). With goodwill at 77.7% of equity and a 10.33% discount rate, that statement is strong. RATING: YELLOW.

1.2 Depreciation lives vs Schedule II (Note 2.3(c), p.247):
- Concession equipment 8 years (Sch II 15); gaming equipment 13.33 (15); projectors and sound 10 and 13 (13); furniture 5 to 10.53 (8); windmill 23.5 (22); LCDs 4 (5); vehicles 5 (8). Shorter than Schedule II on most film-equipment classes: conservative. Residual value 5% of cost (10% on sound and projection); leasehold improvement residual 20% where the lease term used is shorter than the agreed term. The 20% residual on leasehold improvements is aggressive-leaning: it lowers depreciation on assets in leased halls. Not quantified in the document. RATING: YELLOW on that one item, GREEN on the shorter lives. No change in useful lives is disclosed for FY26 other than the closure-driven 125.
- Software 6 years; brands 20 years; beneficial lease rights over remaining lease; movie rights per a schedule (theatrical rights 30% on exploitation, non-theatrical 14% a year for 5 years) (Note 2.3(e)-(g), pp.248-249). Movie rights amortisation sits within D&A.

1.3 Revenue (Note 2.3(j), p.250). Tickets when film is exhibited; F&B on delivery; gift-voucher breakage recognised in proportion to redemption; convenience fee when ticket is sold; movie distribution revenue recognised GROSS ("The revenue is recognised on gross basis", p.250). Gross presentation of distribution inflates revenue and cost together: movie production and distribution revenue is 2,224 against "movie production and distribution" cost of 3,160. RATING: GREEN on ticket and F&B, YELLOW on distribution gross-up.

1.4 Leases (Note 2.3(i) and Note 18(g), pp.249-250, 272): weighted average incremental borrowing rate 9.5% in both years. Rate is flat while the goodwill WACC fell 175 bp and borrowing rates fell (7.22% to 12.00% against 8.48% to 12.00%). Short-term and low-value leases expensed; rent expense (incl. variable) 817 (FY25 714). RATING: YELLOW (see F-8).

1.5 ECL: provision matrix on past experience; receivables "in default/doubtful if outstanding more than 270 days, and more than 365 days for government dues" (Note 42(c), p.297). A 270-day default trigger is looser than the common 180-day or one-year norms in Indian listed companies only on the government-dues leg (365). In practice the provision on receivables is 100% of credit-impaired balances: 351 impaired = 351 provision (Note 11, p.266). RATING: GREEN.

1.6 Policy changes and standards: Ind AS 1 amendments (no impact). Supplier finance disclosures under Ind AS 7 and 107 adopted: 1,251 (FY25 1,635) reclassified from Trade payables to Other financial liabilities; "no impact on total equity or profit" (Note 2A(ii), p.258). This is a first-time effect on presentation and moves operating cash flow lines. RATING: YELLOW (see F-4). Pillar Two not applicable (Note 2A(iii)). Ind AS 1 covenant classification amendment effective 1-Apr-2026 (Note 2B, p.258).

1.6a Discontinued operations policy (Note 2.3(x), p.257), comparatives re-presented. FY25 P&L and cash flow carry "(refer note 41)".

1.7 Capitalisation: pre-operative expenses capitalised to CWIP, 300 in FY26 (Note 44). Borrowing cost capitalised 19 (FY25 42) at 7.55% to 9.45% (Note 3 point ii, p.259). RATING: GREEN, small.

1.8 First-time standards: New Labour Codes notified 21-Nov-2025. Incremental impact 405 booked as exceptional (Note 31(i), p.278). Of which gratuity past service cost 113 (funded 111 plus unfunded 2) (Note 34, p.279). The balance of about 292 is not split by benefit type: NOT FOUND IN DOCUMENT. "The Group continues to monitor the finalisation of Central/State Rules ... would provide appropriate accounting effect as and when ... notified" (Note 31(i)). So further charges are possible. RATING: YELLOW. Standalone books 392 for the same item (MD&A p.95), the 13-million difference sits in subsidiaries.

1.9 Impairment test assumptions (Note 4A, p.261): value in use, post-tax DCF, 5-year projection, risk-adjusted WACC 10.33% (FY25 12.08%), terminal growth 4% to 5% (FY25 4% to 5%). "The Group believes that any reasonably possible change in the key assumptions ... would not cause the aggregate carrying amount to exceed the aggregate recoverable amount." No headroom figure, no sensitivity table. Revenue growth and margin assumptions NOT FOUND IN DOCUMENT. Note the auditor made this a Key Audit Matter and describes "recoverable value headroom ... sensitivity testing" as performed (audit report, PDF p.232). RATING: YELLOW to RED (see F-3).

---------------------------------------------------------------
## 2. RELATED PARTY TRANSACTIONS (Note 46, consolidated, PDF pp.300-301; standalone Note 44, pp.223-225)

Counterparties: KMP and relatives; the JV; and entities in which KMP/relatives have significant influence (PVR Nest, Bijli Realty Pvt Ltd, INOX India Ltd, GFL Ltd, Multiples Alternate Asset Management, Dhruva Advisors LLP, Shardul Amarchand Mangaldas & Co till 21-Oct-2024).

| Party | Relationship | Nature | FY26 | FY25 | YoY |
|---|---|---|---|---|---|
| Ajay Kumar Bijli | Managing Director | Remuneration | 255 | 235 | +8.5% |
| Sanjeev Kumar | Executive Director | Remuneration | 137 | 127 | +7.9% |
| Pavan Kumar Jain | Chairman, non-exec | Brand licence fees | 190 | 175 | +8.6% |
| Bijli Realty Pvt Ltd | KMP-influenced | Rent expense | 47 | 48 | -2.1% |
| PVR Nest | KMP-influenced | CSR spend | 14 | 10 | +40% |
| Aamer Krishan Bijli | Son of MD | Professional fees | 3 | 3 | 0% |
| Nayana Bijli | Daughter of MD | Professional fees | 3 | 3 | 0% |
| Niharika Bijli | Daughter of MD | Professional fees | 3 | 2 | +50% |
| Independent directors (Harris 2, Kanabar 2, Baijal 2, Chandiok 2) | KMP | Sitting fees and commission | 8 | about 7 | n/m |
| Shardul Amarchand Mangaldas | Ceased 21-Oct-2024 | Professional fees | nil | 7 | n/a |
| PVR Ltd Employees Group Gratuity Scheme | Post-employment trust | Contribution | 70 | 60 | +16.7% |
| Devyani PVR INOX Pvt Ltd | JV | Equity investment | 17 | 15 | |

Balances at year end: remuneration payable Ajay Kumar Bijli 132 (FY25 122), Sanjeev Kumar 71 (66): total 203 against remuneration of 392 (52%); trade payable to Pavan Kumar Jain 190 (175); security deposit given to Bijli Realty 17 (17); JV equity carrying 32 invested (15) (Note 46, p.301).

Standalone-only intragroup (Note 44, pp.224-225): PVR INOX Pictures film distributors share expense 1,415 (FY25 1,425); purchases from Zea Maize 148 (187) until sale; VPF income from Pictures 67 (66); inter-corporate loan to PVR INOX Lanka outstanding 78 (70), interest accrued 7; equity investment in Pictures 1,310, Lanka 420; Zea Maize investment 150 added in FY26 (447 in FY25) before the sale, carrying 951 in total. Corporate guarantee for Zea Maize bank facility nil (FY25 50).

Measures (derived):
- Total related-party operating payments on the lines above about 663 (FY25 about 617 incl. the departed law firm) = about 1.0% of consolidated revenue of 66,462.
- MD and ED remuneration 392 (FY25 362) = 14.2% of profit before exceptional items and tax of 2,752. Remuneration grew 8.3% against revenue up 16.6%. Payable of 203 at year end is 52% of the annual figure.
- Brand licence fee of 190 to the Chairman is also fully outstanding as a trade payable at year end (190), as in FY25 (175). The note does not say whether the year-end balance is the whole-year fee. Basis of fee (percent of revenue or fixed) NOT FOUND IN DOCUMENT in the notes.
- Managerial remuneration approved under Section 197 and Schedule V; shareholder approval 9-Jun-2023 (valid to 5-Feb-2026) and 14-Mar-2026 for 6-Feb-2026 to 5-Feb-2028 (Note 49, p.304).
- "All transactions with related parties are made on terms equivalent to those that prevail in arm's length transactions" (Note 46(d), p.301). A blanket statement.
- New related parties this year: none new; the JV was set up 26-Jul-2024 (Note 51, p.305). No loans to promoter entities. No promoter-family borrowings.
- Shareholding: GFL Limited 16.13% (15,835,940 shares), Ajay Bijli 5.55%; promoter group total 27.53% (27,034,066 shares), unchanged vs FY25 (Note 14, p.269).
RATING: GREEN on size and structure; YELLOW on the brand fee and the remuneration payable outstanding.

---------------------------------------------------------------
## 3. CONTINGENT LIABILITIES (Note 37, PDF p.292)

| Item | FY26 | FY25 | Deposited under protest FY26 | Stage per note |
|---|---|---|---|---|
| a Income tax appeals (CIT(A), ITAT, HC), FY2009-10 to 2017-18, 2021-22, 2023-24 | 103 | 167 | 37 | appeals |
| b Entertainment tax, Chennai (regional movies short deposit) | 16 | 16 | not stated | demand notice |
| c Entertainment tax, Indore (collection during exemption period) | 144 | 144 | not stated | demand notice |
| d Entertainment tax Maharashtra on convenience fees | nil | 26 | not stated | closed or reduced; note says a further 25 demand excluded, "exposure is low" |
| e Service tax: 3D glasses, TM charges, distribution, bowling | 60 | 60 | 4 | demand notices |
| f Service tax on food and beverages | 530 | 530 | 40 | demand |
| g SCN service tax on F&B | nil | 35 | nil | closed |
| h VAT various states | nil | 5 | not stated | closed under MVAT amnesty 2023 |
| i Service tax on box office "renting of immovable property" | 171 | 171 | 10 | demand |
| j Entertainment tax Punjab Rule 22 | nil | 16 | utilised | settled under OTS |
| k Employees Provident Fund Act | 11 | 11 | 4 | |
| l Kolhapur Municipal Corporation | 2 | 2 | 0 | |
| m GST demands from state authorities | 488 | 489 | 14.39 | |
| n Claims by developers/lessors | 964 | 720 | 188 | claims; "claims/counter claims assessed to be superfluous and remote" excluded |
| o Other statutory Acts | 66 | 66 | 39 | |
| p Other legal cases | not ascertainable | not ascertainable | | "not material in aggregate", management has "strong chances of success" |

Derived: item sum FY26 = 2,555 (FY25 = 2,458). The note prints no total. 2,555 = 3.46% of equity of 73,787. Largest single item 964 (claims by developers) = 1.3% of equity; no item is above 10% of net worth. Deposits under protest on the items above about 336 (derived from the note).
- Developer/lessor claims rose 244 (+34%) in the year while the company also impaired a CWIP project "on account of dispute arising with the landlord" (Note 31(ii)). Same theme. RATING: YELLOW.
- Tax-type disputes (a, b, c, e, f, i, m, o, k, l) total 1,591 (FY25 1,656). Entertainment-tax items remaining 160 (Chennai 16, Indore 144).
- Entertainment tax and GST exemption: the group has recognised government grant receivable of 63 (30 non-current plus 33 current) (Note 5, p.263), "accounted on the basis of eligibility criteria ... and applications filed with the authorities". It is under "obligation to operate respective Multiplexes for a certain number of years" (Note 36(b), p.291). The number of years and the exposure if screens are closed early are NOT FOUND IN DOCUMENT.
- Provision against litigation: other provisions 374 (FY25 332) "against probable liability under various litigations", movement +42 (Note 19, p.273). The cases behind it are NOT FOUND IN DOCUMENT.
- Guarantees for subsidiaries: standalone note shows corporate guarantee for Zea Maize nil (FY25 50) (Note 44(e), p.225). Consolidated note shows no guarantee.
RATING overall: GREEN on scale, YELLOW on the rising lessor claims and the wording on item p.

---------------------------------------------------------------
## 4. TRADE RECEIVABLES (Note 11, PDF pp.266-267; Note 42(c), p.297)

Gross 3,023 (FY25 2,846), credit-impaired 351 (416), net 2,672 (2,430). Net up 10.0% against revenue up 16.6%.

Ageing as printed (PDF p.266, checked against the PDF image): columns are Unbilled, Not due, 6 months to 1 year, 1 to 2, 2 to 3, more than 3 years, Total. There is NO "less than 6 months" column in the printed table, so the rows do not foot to the total.

| FY26 | Unbilled | Not due | 6m-1y | 1-2y | 2-3y | >3y | Printed total |
|---|---|---|---|---|---|---|---|
| Undisputed, good | 597 | 74 | 118 | nil | nil | nil | 2,672 |
| Undisputed, credit impaired | nil | nil | 8 | 62 | 19 | 33 | 122 |
| Disputed, credit impaired | nil | nil | blank | 20 | 14 | 195 | 229 |
| Total | 597 | 74 | 126 | 82 | 33 | 228 | 3,023 |

Printed buckets sum to 1,140 against 3,023. The missing 1,883 (3,023 - 1,140) is derived as the unlisted "within 6 months" bucket; the same is true for FY25 (printed 1,554 of 2,846; missing 1,292; FY25 columns: not due 1,016, 6m-1y 167, 1-2y 86, 2-3y 86, >3y 199). The omission of that column is a disclosure defect against the Schedule III ageing format. RATING: YELLOW (form, not substance).
- More than 6 months (printed buckets): FY26 469 = 15.5% of gross; FY25 538 = 18.9% of gross. The 469 is almost wholly credit-impaired (351 impaired of which 8+62+19+33+20+14+195 = 351 aged >6m), plus 118 good in the 6m to 1y bucket.
- Of the 351 impaired, 229 are disputed, 195 of those older than 3 years.
- Impairment allowance roll: 416 opening, +12 charged, (61) written off, (16) moved to discontinued, 351 closing (Note 42(c), p.297). The P&L line for "impairment allowance for trade receivables and other assets" is 108 (FY25 66) (Note 30, p.277), net of utilisation 125 leaves bad debt/advances written off 31.
- Provision cover: the impaired balance is provided 100% (351 of 351).
- Single customer above 10%: none ("does not have revenue more than 10% of total revenue from a single customer", Note 47, p.303). Receivables include card companies and online ticketing partners realisable in 1 to 3 working days (Note 42(c), p.297).
- Unbilled 597 is new in the ageing (nil in FY25). Contract asset line "Revenue earned but not billed" is nil non-current and nil current in FY26 versus 131 current in FY25 (Note 5, p.263). The two disclosures do not obviously tie: why FY26 shows 597 "unbilled" in receivables but nil contract asset is NOT FOUND IN DOCUMENT. RATING: YELLOW.
- Receivable days (net receivables x 365 / revenue from operations 66,462 and 56,999): about 14.7 days FY26, 15.6 days FY25. Trend: improving or stable. FY24: NOT FOUND IN DOCUMENT.
- Related-party receivables: PVR Nest 0 (Note 46, p.301). Immaterial.
- Cash-flow: increase in trade receivables (466) (FY25 (187)) (p.241). The working-capital line in the cash flow shows a larger rise than the balance-sheet movement of 242 because 188 of receivables left with Zea Maize (Note 41, p.295).
RATING: GREEN on level and cover.

---------------------------------------------------------------
## 5. INVENTORY (Note 9, p.266; Note 26, p.276)

Food and beverages 481 (FY25 593, including stock in transit nil vs 8); stores and spares 251 (209); total 732 (802). Lower of cost and NRV, weighted average (Note 2.3(h), p.249). No write-downs disclosed: NOT FOUND IN DOCUMENT (no NRV write-down amount, no obsolescence disclosure).
- Comparability: FY25 F&B includes the Zea Maize stock; 166 of inventory left with the sale (Note 26, p.276).
- Consumption of F&B on continuing basis 4,695 (4,349) against F&B sales 20,884 (17,470): cost ratio 22.5% (24.9%) (derived). F&B revenue +19.5% against consumption +8.0%.
- Inventory days (732 over consumption 4,695 x 365): about 57 days (FY25 about 67 on the 4,349 base). Not comparable because FY25 opening includes Zea Maize. RATING: GREEN.

---------------------------------------------------------------
## 6. INVESTMENTS, SUBSIDIARIES, JV (Notes 1, 5A, 10, 41, 51)

- Subsidiaries: PVR INOX Pictures Limited (ownership % not printed in the consolidated note: the table row has no percentage, p.244; standalone carries investment 1,310); PVR INOX Lanka 100% (investment 420 standalone, loan 78 outstanding); Zea Maize 93.27% till 29-Jan-2026, sold to Marico (MD&A p.35 names Marico Limited, 29-Jan-2026) for net 2,221 (Note 41).
- JV Devyani PVR INOX: 49%, carrying 24 (FY25 12); equity paid 32 on 48,510,000 shares paid up Rs 6.50 each against Rs 10, uncalled liability 17 (FY25 34) (Notes 5A and 36). JV is early stage: revenue 63, loss (10), group share (5) (Note 5A, p.264). Net assets 48. No contingents or commitments in the JV.
- Vkaao Entertainment Pvt Ltd: shown "upto August 01, 2024", nil (Note 5A, p.263). The exit terms are NOT FOUND IN DOCUMENT.
- Loss-making subsidiary: Zea Maize loss 188 (FY25 161) before sale; PVR INOX Lanka profit 6 (FY25 loss 12); PVR INOX Pictures profit 148 (FY25 136) (Note 48, pp.303-304).
- Other investments: only National Savings Certificates 0 (Note 10). Mutual fund redemption gains 236 in other income (FY25 218) (Note 25); the mutual fund holdings are redeemed within the year, none at year end. No investment impairments.
- ICDs and loans given: standalone loan to PVR INOX Lanka 78; employee loans 10 (15) (Note 13). No loans to promoter entities.
- Goodwill on consolidation 31 (FY25 95) inside goodwill; goodwill of 64 left with Zea Maize (Note 41; Note 4A, p.261).
- Schedule III table (Note 48, p.303): parent 99.43% of net assets and contributes 1,569 of total comprehensive income 3,299; Pictures 2.75%; elimination (1,707).
RATING: GREEN.

---------------------------------------------------------------
## 7. BORROWINGS (Notes 17, 20, 42(d), 43, cash-flow note)

- Instruments: only secured bank term loans (no debentures, no NCDs, no related party borrowings). FY26 4,592 non-current plus 2,994 current maturities = 7,586. Commercial paper nil at year end (FY25 1,487; maximum during FY26 1,500, FY25 2,000) (Note 20, p.273).
- Security: first pari passu charge on all movable PPE, CWIP, intangibles, loans and advances, deposits, inventory, receivables and capital advances, excluding immovable property and assets under lien to regulators (Note 17(i), p.271). Second charge on current assets for ECLGS loans (nil now).
- Rate: floating, linked to bank benchmark; effective 7.22% to 12.00% (FY25 8.48% to 12.00%). The upper bound of 12.00% is unchanged, so some loans have not repriced. Short-term bank loans of 7 to 30 days at 7.75% to 9.4% (FY25 7.90% to 10.35%) (Note 20(iii)). RATING: GREEN.
- Repayment schedule, Note 17(ii) (p.271): within 1 year 3,003 (59 instalments); 1 to 3 years 3,787 (71); after 3 years 811 (14). Total 7,601. FY25: 4,233 / 7,365 / 1,848. A year-by-year five-year schedule is NOT FOUND IN DOCUMENT.
- Liquidity table Note 42(d), p.298 (borrowings / other financial liabilities columns, FY26): less than 3 months 966; 3 to 12 months 2,037; 1 to 5 years 4,598; total 7,601. More than 5 years nil. 
- Covenants: the capital management note mentions "requirements of the financial covenants" (Note 43, p.298) but no covenant terms, no breach and no waiver is disclosed anywhere. NOT FOUND IN DOCUMENT. The Ind AS 1 covenant amendment applies from 1-Apr-2026 (Note 2B).
- Term changes: none disclosed. Processing-fee amortisation (25) (cash-flow note, p.242).
- Interest on term loans and CP 1,099 (FY25 1,524); "Others" 168; other financial charges 240 (Note 28, p.276). Lease interest 5,821 is 79.4% of total finance costs of 7,328.
RATING: GREEN.

---------------------------------------------------------------
## 8. TRADE PAYABLES (Notes 21, 22, 2A(ii))

- Trade payables 5,948 (FY25 6,062): MSME 443 (249), others 5,505 (5,813) (Note 21, p.273). Ageing (Note 21, p.274): not due and unbilled 3,442 (3,694); less than 1 year 2,054 (1,227); 1 to 2 years 193 (883); 2 to 3 years 195 (143); more than 3 years 65 (115). No disputed dues.
- Items older than 1 year: 453 (FY25 1,141). Sharp reduction of 688 in the 1-2 year bucket (883 to 193). Linked in time to liabilities written back (976 in other income) and the lease reversals. The note does not say what the written-back liabilities consisted of. NOT FOUND IN DOCUMENT. RATING: YELLOW (see F-2).
- MSME: 443 payable, of which 22 is 1-2 years? Reading of the MSME row: not due 412, less than 1 year 22, 1-2 years 9 (Note 21, p.274). So dues beyond one year for MSME are 9. Statutory MSME interest disclosure (interest accrued and paid) is in the standalone notes: principal unpaid 569 (FY25 220) , interest due 1 (1), interest paid 8 (11), payments beyond appointed day 598 (623) (standalone MSME table, PDF p.190, lines 15855-15872). The consolidated notes in the extract have no such table. MSME dues more than 45 days: NOT FOUND IN DOCUMENT in the consolidated notes. Standalone MSME principal 569 does not tie to the consolidated MSME line 443; the difference is not explained. NOT RECONCILED.
- Supplier finance: 1,251 in other financial liabilities (FY25 1,635) after being moved out of trade payables. Carrying amount of payables in the arrangement 2,178 (2,312). Arrangement payment terms 15 to 90 days against 60 to 90 days for comparable non-arrangement payables; settled with finance providers within 90 days; no security (Note 22, p.274). Financing and interest cost settled upfront. Without this reclassification trade payables would have been 7,199 (FY26) against 7,697 (FY25) (derived). RATING: YELLOW, debt-like item outside borrowings.
- Payable days (payables / revenue x 365, derived, crude since cost base is not used): 5,948 gives about 32.7 days (FY26) and 6,062 about 38.8 days (FY25). Cash-flow shows trade and other payables +237 (FY25 +3,166).
- Other financial liabilities: PPE payables 382 (642); security deposits 1,237 non-current plus 243 current (FY25 1,329 + 5); interest accrued 25 (47); deferred consideration 2,036 (2,124); unpaid dividends 1 (Note 22).
- Other liabilities: contract liabilities 1,151 current plus 5 non-current (FY25 1,027 + 82); advances from developer 189 (nil) (new); employee benefit payables 801 (480); statutory dues 500 (364) (Note 23, p.275). Revenue of 1,027 recognised from opening contract liabilities (Note 24).
RATING: YELLOW on payables, tied to F-2 and F-4.

---------------------------------------------------------------
## 9. PROVISIONS (Note 19, p.273; Note 34, pp.279-281)

- Provisions: gratuity net 195 non-current plus 2 current (FY25 41 + 4); compensated absence 153 + 52 (112 + 45); other provisions (litigation) 374 current (332) (Note 19). Total 348 non-current, 428 current. Gratuity provision jumps from 45 to 197 on Labour Code past service cost.
- Gratuity (Note 34): funded DBO 848 (644), plan assets 670 (621), net funded shortfall 178 (23); unfunded DBO 19 (21) (Note 34, p.279). Past service cost 111 funded plus 2 unfunded (booked in exceptional). Actuarial loss in OCI 60 (8): of which 30 from plan assets earning less than the discount rate and 30 on obligations. Expected employer contribution FY27 178 (FY26 expected 23, actual 70). Plan assets 99.94% insurer-managed funds; four insurers. Duration 4 to 7 years (2 to 6). Sensitivity: 1% discount rate change moves the obligation by (29.43) / 31.84; 1% salary escalation by 29.19 / (27.50) (Note 34, p.281).
- Assumptions: expected return on plan assets 6.50 to 8.30% (FY25 6.40); salary increase 6.50% (6.40); attrition 8.00 to 10.00% (8.00 to 9.50); executive grade attrition 8 to 18 and 15 to 65 in the table (rows unlabelled on the printed page). THE DISCOUNT RATE ROW PRINTS "(%)" WITH NO VALUE in both years (Note 34, PDF p.280, image checked). Discount rate NOT FOUND IN DOCUMENT. RATING: YELLOW (disclosure gap on the key assumption).
- Defined contribution: 203 (194) (Note 34, p.281).
- Warranty: none applicable. Decommissioning: no provision disclosed; Note 2.3(i) says the ROU cost includes estimate of dismantling and restoration costs, but no restoration provision is shown. NOT FOUND IN DOCUMENT. Onerous contracts: NOT FOUND IN DOCUMENT.
- Litigation provision: see Note 19 above; the movement +42 against (82) in FY25. FY25 included a written-back "provision for other disputed liabilities" 85 booked to other income (Note 25).
RATING: YELLOW.

---------------------------------------------------------------
## 10. DEFERRED TAX (Notes 6, 45, pp.264-265, 299)

- Net DTA 5,184 (FY25 5,894); net DTL at subsidiary level nil (12). Components (Note 6A, p.264): DTA on lease liability 15,176 (15,760); DTA on business losses and unabsorbed depreciation 3,252 (4,372); impact on other financial assets 545; accruals 282; impairment 116. DTL on ROU assets 11,665 (12,496); DTL on depreciation difference 2,587 (2,697).
- Net lease-related DTA = 15,176 - 11,665 = 3,511 (derived). Loss-related DTA 3,252 at 25.17% implies about 12,920 of losses and unabsorbed depreciation (derived). Expiry profile of these losses NOT FOUND IN DOCUMENT. Loss DTA fell 1,120 in FY26 (Note 45(d), p.299): deferred tax charge came from using losses.
- Total deferred tax charge 716 = 519 continuing + 197 discontinued; note 45(a) calls total tax 705 including discontinued.
- Reconciliation (Note 45(c)): profit before tax incl. discontinued 4,033; computed at 25.17% = 1,015; adjustments: earlier-year deferred tax (122), earlier-year current tax (73), subsidiary losses without DTA and the profit on disposal (124), non-deductible 8; tax 705, effective rate 17.5% (FY25 25.0%). The (124) item covers the disposal gain sheltered by unrecognised-asset losses of the subsidiary. The tax rate benefit is therefore one-off.
- DTA realism: "management believes that it is probable that the Group will be able to realise the benefits" based on projected taxable income and tax planning (Note 6 text, p.265). Profit before tax before exceptional items of 2,752 is the first positive year after a loss of 3,582. The DTA of 5,184 equals 7.0% of equity and 2.8 times FY26 PBT before exceptional items (derived). The DTA on lease liability is a timing item tied to ROU. RATING: YELLOW (see F-6).
- Unrecognised DTA: subsidiary losses not recognised (45(c)); amount NOT FOUND IN DOCUMENT.
- MAT credit: none disclosed. Income tax assets (net) 885 (799), including 42 paid under protest (Note 7, p.265).
RATING: YELLOW.

---------------------------------------------------------------
## 11. REVENUE DETAILS (Notes 24 and 47, pp.275, 302-303)

Revenue from operations 66,462 (FY25 56,999), +16.6%. Disaggregation (Note 24):
- Sale of services 45,154 (39,070): movie tickets 35,301 (29,549) +19.5%; advertisement 4,636 (4,475) +3.6%; movie production and distribution 2,224 (2,364) -5.9%; convenience fees 2,410 (2,111) +14.2%; virtual print fees 583 (571) +2.1%.
- Sale of food and beverages 20,884 (17,470) +19.5%.
- Other operating revenue 424 (459): rental 165 (148), management fees 93 (50), others 166 (261), including gift voucher breakage.
- Printed Note 24 headings are shifted against their figures (the header lines read "Sale of services / Sale of food and beverages / Other operating revenue" followed by 45,154 / 20,884 / 424 in a different order in the extract); the figures tie to the Note 47 footnote (p.303) and to the 66,462 total.
- Segment: movie exhibition revenue 64,238 (54,635) plus movie production and distribution 2,224 (2,364); exhibition segment operating result 2,536 (loss 3,767); production/distribution 216 (185) (Note 47, p.302). Others segment (Zea Maize) removed; food court income folded into exhibition. Total assets 156,123; allocated liabilities 82,336. Capital employed allocable 67,695 (63,840) (p.302).
- Contract liabilities 1,151 + 5 (1,027 + 82); unsatisfied obligations: 1,151 within 0 to 1 year, 5 beyond one year (Note 23, p.275). Convenience-fee time value adjustment (83) (cash-flow, p.241). Revenue recognised from opening contract liability 1,027 (967).
- Customers in India and Sri Lanka; Sri Lanka not material; no single customer above 10%.
- Sublease income 146 (136) in other operating revenue (Note 18(b)).
RATING: GREEN.

---------------------------------------------------------------
## 12. OTHER CRITICAL NOTES

12.1 Exceptional items (Note 31, p.278): Labour Codes 405 (consolidated; includes 113 gratuity past service cost); suspended CWIP provision 78 (landlord dispute). Total 483 (FY25 nil). Recurrence: FY25 had none. The Labour Code charge can recur if Rules change (Note 31(i)). Zea Maize gain 1,952 is in discontinued operations, not in exceptional items of continuing operations.

12.2 Goodwill (Notes 4A, 2.3(l), p.261, 251-252): goodwill 57,367 (57,431); 57,367 less 31 consolidation goodwill = 57,336 from the PVR-INOX merger (derived; the merger appears in Note 14(e): 36,701,729 shares allotted for the scheme of business combination in the year ended 31-Mar-2023, p.270). One CGU for the whole group. No impairment in FY26 or FY25. WACC 10.33% (12.08%); terminal growth 4% to 5% (4% to 5%); 5-year projection. Management states no reasonably possible change breaks the test; no headroom number, no breakeven WACC or growth. Goodwill = 77.7% of equity, 36.7% of total assets. Equity of 73,787 less goodwill 57,367 less other intangibles 1,160 gives tangible equity of 15,260 (derived).
- Also intangibles: other intangible assets 1,160 (1,256): software 195, brand 442 (20-year life), beneficial lease rights 414, movie rights 110 (Note 4A). Beneficial lease rights gross 942 on the face; Note 4B footnote refers to 1,354 beneficial lease rights recognised on the INOX Leisure acquisition, with 942 shown in intangibles (p.262). The balance 412 is not traced. NOT FOUND IN DOCUMENT.

12.3 Capital commitments (Note 36, p.291): 906 net of advances (FY25 906, identical); uncalled liability on JV shares 17 (34). Capital advances 113 (226) with 20 credit impaired.

12.4 FX (Note 38, p.293): unhedged: payable for PPE USD-linked 94 (180); balances with banks 5; receivable 1 (26). Group "does not hedge" and calls currency risk low. RATING: GREEN.

12.5 Segment: above.

12.6 EPS (Note 33, p.278): basic 34.01; diluted 33.87; gap 0.14 from 411,669 dilutive shares on 98,199,962 shares. Continuing basis 17.93 and 17.86. RATING: GREEN.

12.7 Events after balance sheet date: NOT FOUND IN DOCUMENT in the consolidated notes (no subsequent event note). Date of approval 11-May-2026 (Note 1, p.244).

12.8 CSR: P&L CSR expenditure 15 (13) (Note 30, p.277), of which 14 to PVR Nest (related party, Note 46). Required amount under Section 135 and any shortfall: NOT FOUND IN DOCUMENT in the notes. Flag: the main CSR vehicle is a related party. RATING: YELLOW (small).

12.9 ESOP and share-based pay (Note 35, pp.282-291): Equity-settled schemes PVR ESOS 2017, 2020, 2022. Outstanding options at 31-Mar-26: ESOS 2022 (Mar-2022 grant) 384,335 at exercise Rs 1,347, all exercisable; the extension of exercise period by one year was made on 27-Aug-2025; ESOS 2020 (Aug-2022 grant) 9,334 at Rs 1,738; ESOS 2017 (May-2024 grant) 12,000 at Rs 1,290; ESOS 2022 (Dec-2024) 6,000 at Rs 1,403. Total about 411,669 matches dilution count. Expense 14 in FY26 (FY25 1 in cash-flow, p.241); Note 27 shows 14 (nil). Employee stock options outstanding reserve 251 (268). Cash-settled stock incentive: 280,000 units granted 26-Aug-2025, vest if 4-week VWAP reaches target tranche prices by March 2027; liability nil at year end (Note 35, p.288). No exercises in FY26. Zea Maize ESOPs 54 expense (36) cancelled on sale; reserve of 90 transferred. RATING: GREEN on dilution (0.42% of shares); YELLOW because an extension of exercise period (modification) occurred.

12.10 Share capital (Note 14, pp.268-270): 98,199,962 shares of Rs 10, unchanged in FY26 (FY25 issued 65,516 on ESOP exercise). Authorised 2,744 equity; 0.001% non-cumulative convertible preference shares authorised 201; none issued. Non-promoter holders above 5%: Nippon India Small Cap 250 Index Fund 8.19%, HDFC Dividend Yield Fund 6.91%, ICICI Pru Technology Fund 5.86%. Promoter holding flat at 27.53%.

12.11 Direct movements through reserves bypassing P&L (Statement of changes in equity, p.243, and Note 15): "adjustment on account of change in ownership in subsidiary" (10) in general reserve and (33) in FY25; transfer on discontinued operations (90) from options reserve; retained earnings (13,735) -> (13,825) in the Note 15 figures, though the SOCIE table prints (13,735) in retained earnings for the total comprehensive income row; Note 15 carries "Retained earnings (13,825) / (17,125)" (p.270) while the SOCIE closing row prints (13,735) (p.243) and the balance sheet total of 72,805 ties. The 90 difference equals the 90 options reserve transferred. NOT RECONCILED in the notes: treat as presentation, ties to total equity.

12.12 Audit trail / controls (Note 50, p.304; audit report p.236): audit trail feature not enabled for direct data changes under privileged access in SAP Hana and Showbizz POS; for FY24 the audit trail preservation could not be assessed in absence of a Service Organisation Controls report; for subsidiary Zea Maize (Showbizz) the group "is not in possession of the requisite documents" to determine whether audit trail was enabled. Statutory auditor reports this under Rule 11(g) (audit report p.236). No qualification of the opinion. RATING: YELLOW (control gap, not a numbers issue).

12.13 Other statutory (Note 52, p.305): no struck-off company transactions, not wilful defaulter, no unrecorded income. Transfer pricing documentation "in the process of updating" (Note 39, p.293). RATING: GREEN, small.

12.14 Fair value (Notes 40, 5, 4C): investment property 142 net carrying, fair value 216 (200) level 3; financial instruments at amortised cost; carrying value of borrowings 7,586; lease liabilities 60,205. No Level 1 or 2 instruments. Deferred consideration valued at 9.50%.

12.15 Cash-flow tie-outs (p.241): cash flow adjustment "Liabilities written back (including related rent concessions)" (976) (FY25 (837)); "Interest income (including time value of money adjustment)" (524). Operating cash flow of continuing operations 21,597 is after (976) of non-cash credit. Interest paid on borrowings 1,456; lease repayment including interest 11,847.

---------------------------------------------------------------
## 13. DETAILED FINDINGS TABLE (anchors; ratings)

F-1 Net debt falls to 1,619 but 60,205 lease liability and 1,251 supplier finance sit outside it. (Notes 17, 18, 20, 22; pp.271-274). YELLOW.
F-2 Liabilities written back of 976 (53% of other income 1,835; 43% of continuing profit before tax 2,269; FY25 837) plus 871 in lease costs; recurring every year; nature of the liabilities NOT FOUND. (Note 25 p.276; Note 18(d) p.272; cash flow p.241). RED.
F-3 Goodwill 57,367 = 77.7% of equity; WACC cut to 10.33% from 12.08%; no headroom; one CGU. (Note 4A p.261). RED.
F-4 Supplier finance reclassification 1,251 / 1,635 out of trade payables; first-year Ind AS 7 disclosure. (Notes 2A(ii), 22). YELLOW.
F-5 Two earnings bases: statements show PAT 3,328 and continuing 1,761; MD&A states 3,868 and 2,306, a gap of 540 and 545 not bridged in the notes. (p.240 vs MD&A p.35). RED for reconciliation.
F-6 DTA 5,184 including 3,252 on losses; effective tax rate 17.5% helped by disposal sheltered with unrecognised losses; first profitable year. (Notes 6, 45). YELLOW.
F-7 Labour Codes charge 405 as exceptional; gratuity funded shortfall 178; discount rate value absent from note; more charges possible. (Notes 31, 34). YELLOW.
F-8 Lease discount rate unchanged at 9.5% while WACC and loan rates fell; lease liability 60,205 against ROU 46,329. (Notes 18, 4B). YELLOW.
F-9 Closures: no impairment on PPE or ROU of closed screens; single CGU; ROU derecognition 1,760 net against 2,300 liability reversed (net credit about 540). (Notes 3, 4B, 18). YELLOW.
F-10 Developer/lessor claims 964 (+34%); CWIP impairment 78 for landlord dispute. (Notes 37, 31). YELLOW.
F-11 Remuneration to two executives 392 (14.2% of pre-exceptional PBT), 203 payable at year end; chairman brand fee 190, fully payable at year end. (Note 46). YELLOW.
F-12 Receivable ageing table omits the "less than 6 months" column, rows do not foot; unbilled 597 new versus contract asset nil. (Note 11; Note 5). YELLOW.
F-13 Deferred consideration (refundable) 2,036 unexplained. (Notes 22, 40). YELLOW.
F-14 Zea Maize divestment net 2,221, gain 1,952 in discontinued; standalone 1,270. (Note 41). GREEN on mechanics; the 1,952 is non-recurring.
F-15 Audit trail not fully enabled; subsidiary records unavailable. (Notes 50). YELLOW.
F-16 Debt: bank term loans only, floating 7.22% to 12.00%, no covenant terms disclosed, 2,591 undrawn. (Notes 17, 20, 43). GREEN.
F-17 Contingents 2,555 (my sum) = 3.5% of equity; no item above 1.3%. (Note 37). GREEN.
F-18 Receivables net 2,672, 14.7 days; impaired 351 provided 100%. (Note 11). GREEN.

---------------------------------------------------------------
## PASS 1 SUMMARY: TOP 10 FINDINGS BY INVESTOR IMPORTANCE

| # | Finding | Anchor | Rating |
|---|---|---|---|
| 1 | Two earnings bases: audited PAT 3,328 (continuing 1,761) includes a 1,952 disposal gain in discontinued operations; management commentary quotes 3,868 and 2,306, unbridged by 540 and 545. Press 176 Cr = 1,761; press 386 Cr = 3,868 | Statement p.240; Note 41 p.294; MD&A p.35 | RED |
| 2 | Goodwill 57,367 is 77.7% of equity and 36.7% of assets; test uses single CGU, WACC 10.33% (12.08%), terminal growth 4% to 5%, no headroom shown | Note 4A, p.261 | RED |
| 3 | Liabilities written back 976 (53% of other income, 43% of PBT) plus 871 in lease cost; repeats every year; origin undisclosed | Notes 25, 18(d), pp.276, 272 | RED |
| 4 | Borrowings cut from 14,908 to 7,586; net debt 1,619 (9,522 a year ago). Funded by 5,707 of free cash after lease payments, plus 2,221 from the Zea Maize sale. Leases 60,205 and supplier finance 1,251 sit outside this | Notes 17, 18, 22, 41; cash flow pp.241-242 | YELLOW |
| 5 | Lease structure: lease liability 60,205 vs ROU 46,329; lease cash 11,847 a year; discount rate flat at 9.5%; closure derecognition credit about 540 | Notes 18, 4B | YELLOW |
| 6 | Deferred tax asset 5,184 (loss DTA 3,252); tax rate 17.5% helped by loss shelter on disposal; first profitable year | Notes 6, 45 | YELLOW |
| 7 | Labour Codes 405 booked as exceptional with more rules pending; funded gratuity shortfall 178 vs 23; discount rate value missing | Notes 31, 34 | YELLOW |
| 8 | Supplier finance 1,251 moved out of trade payables; deferred consideration 2,036 unexplained | Notes 2A, 22, 40 | YELLOW |
| 9 | Closed or exited screens (18) cause no impairment (PPE and ROU not impaired); one CGU; entertainment-tax/GST scheme obligation to keep screens running, exposure unquantified | Notes 3, 2.3(g), 36(b) | YELLOW |
| 10 | Related parties are small (about 1.0% of revenue) but executive remuneration 392 is 14.2% of pre-exceptional PBT; lessor claims 964 up 34% | Notes 46, 37 | YELLOW |

Scope note for Pass 2 and 3: the standalone notes were not read in full; consolidated numbers carry the analysis. Items needing a closer re-read: Note 24 label alignment (p.275), Note 15 vs SOCIE retained earnings (pp.243, 270), MD&A 3,868 and 2,306 vs statements (p.35 vs p.240), MSME standalone 569 vs consolidated 443, the "less than 6 months" receivables bucket (p.266, PDF image).
