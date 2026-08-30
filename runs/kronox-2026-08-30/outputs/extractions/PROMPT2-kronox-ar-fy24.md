# PROMPT 2 — Kronox Lab Sciences Ltd, Annual Report FY2023-24 (corpus-only extraction)

Source: `runs/kronox-2026-08-30/inputs/annual-report/8cda34fd-e700-4fbb-ae5d-c215cb7a976a.pdf`
Kronox Lab Sciences Limited, Annual Report 2023-24, year ended 31-Mar-2024.
All figures Rs. in Lakhs unless stated. Printed page = PDF page (offset zero).

Rule note: I answer only from this document. "NOT DISCLOSED" marks silence.
Quote first, then a short reading.

---

## CONTEXT TEST (screener data vs filed statements)

The brief gave screener figures: sales Rs 96 Cr (FY23) -> Rs 90 Cr (FY24),
expenses Rs 74 Cr -> Rs 62 Cr, OPM 23% -> 32%, and "FY24 was the year of the
June 2024 IPO." Test against the filed P&L (printed p.88):

- Revenue from operations: FY24 Rs 8,986.24 lakh (89.86 Cr); FY23 Rs 9,557.79
  lakh (95.58 Cr). Matches the 96 -> 90 Cr shape.
- Total expenses: FY24 Rs 6,283.22 lakh (62.83 Cr); FY23 Rs 7,545.70 lakh
  (75.46 Cr). Matches the 74 -> 62 Cr shape.
- IPO timing conflict. The filed statements place the IPO listing AFTER the
  balance sheet date. Note 27 sub-13 "Events subsequent to March 31, 2024"
  (printed p.124) states the listing was on 10th June, 2024. Note 1.A
  (printed p.91) repeats 10th June, 2024. So the IPO fell in FY2024-25, not
  in FY24. The context statement "FY24 was the year of the June 2024 IPO" is
  not supported by the filed statements; FY24 closed 31-Mar-2024, before the
  listing. Flag for the operator.

---

## 1. Statement of Profit and Loss, FY24 with FY23 comparative

> "Statement of Profit and Loss / for the year ended 31st March, 2024
> (Rs. In Lakhs)" — printed p.88.

| Particulars | Note | 31-Mar-2024 | 31-Mar-2023 |
|---|---|---:|---:|
| Revenue from operations | 19 | 8,986.24 | 9,557.79 |
| Other income | 20 | 157.79 | 192.02 |
| **Total Income** |  | **9,144.03** | **9,749.81** |
| *Expenses* |  |  |  |
| Cost of material consumed | 21 | 4,489.37 | 5,801.20 |
| Changes in Inventories of Finished Goods and Work in Progress | 22 | 96.38 | (312.99) |
| Employee benefits expense | 23 | 622.85 | 702.69 |
| Finance costs | 24 | - | 9.32 |
| Depreciation and amortisation expenses | 25 | 128.88 | 149.66 |
| Other expenses | 26 | 945.75 | 1,195.82 |
| **Total expenses** |  | **6,283.22** | **7,545.70** |
| **Profit/(Loss) before taxes** |  | **2,860.81** | **2,204.11** |
| *Tax Expenses* |  |  |  |
| Current Tax |  | 734.88 | 572.22 |
| Deferred Tax |  | (9.20) | (8.43) |
| **Profit/(Loss) for the year** |  | **2,135.13** | **1,640.32** |
| *Other Comprehensive Income* |  |  |  |
| (A) Items that will not be reclassified to P&L |  |  |  |
| (i) Defined benefit Plan liability / asset |  | 25.51 | 28.03 |
| (ii) Tax impact on above item |  | (5.23) | (7.05) |
| (B) Items that will be reclassified to P&L |  | - | - |
| **Total Other Comprehensive Income (After Tax)** |  | **20.29** | **20.98** |
| **Total Comprehensive Income** |  | **2,155.42** | **1,661.30** |
| Earning per Equity Share (Basic & Diluted, Rs.) | 27 | 5.81 | 4.29 |

Reading: revenue fell 5.98% but PBT rose 29.79% (2,204.11 -> 2,860.81) because
expenses fell faster than revenue. Note 21 "Cost of material consumed" is the
line the P&L labels; the P&L has no separate "purchases of stock-in-trade" line.

---

## 2. Expense-line rupee and % change FY23 -> FY24 (descending rupee reduction)

Base data from the P&L (printed p.88). % change = change / FY23.

| Rank | Expense line | FY24 | FY23 | Rupee change | % change |
|---|---|---:|---:|---:|---:|
| 1 | Cost of material consumed | 4,489.37 | 5,801.20 | (1,311.83) | -22.61% |
| 2 | Other expenses | 945.75 | 1,195.82 | (250.07) | -20.91% |
| 3 | Employee benefits expense | 622.85 | 702.69 | (79.84) | -11.36% |
| 4 | Depreciation and amortisation | 128.88 | 149.66 | (20.78) | -13.88% |
| 5 | Finance costs | - | 9.32 | (9.32) | -100.00% |
| — | Changes in Inventories (FG & WIP) | 96.38 | (312.99) | +409.37 | not meaningful* |

*Changes in inventories rose (a swing of +409.37), so it is the only expense
line that increased, not reduced; listed last. Percentage is not meaningful
because the FY23 base is negative. All five other lines fell; finance costs
fell to zero (no borrowings during FY24, confirmed in the ratio note printed
p.119, "NA - Not Applicable as no borrowings during the year").

---

## 3. Other Expenses note-level itemisation (Note 26, printed p.114)

> "26 Other expenses" — printed p.114.

| Sub-line | FY24 | FY23 | Change |
|---|---:|---:|---:|
| Audit Fees | 4.50 | 4.50 | 0.00 |
| CSR Expense | 36.11 | 28.89 | +7.22 |
| Power and Fuel Expense | 59.07 | 53.58 | +5.49 |
| Factory Expenses | 11.18 | 12.31 | (1.13) |
| Freight & Transportation Expenses | 244.24 | 200.59 | +43.65 |
| Labour Charges | 301.20 | 252.19 | +49.01 |
| Bad Debt | 0.00 | 27.51 | (27.51) |
| Other expenses | 2.52 | 2.47 | +0.05 |
| Other administrative and general expenses | 35.16 | 28.64 | +6.52 |
| Pollution Control Expense | 7.01 | 5.64 | +1.37 |
| Telephone and Postage | 3.75 | 2.76 | +0.99 |
| Printing & Stationary | 5.35 | 4.65 | +0.70 |
| Professional Fees Expense | 35.59 | 43.59 | (8.00) |
| Impairment loss recognized on Financial Asset | (0.24) | 0.31 | (0.55) |
| Increase of Authorised Capital Expense | 0.00 | 29.25 | (29.25) |
| Rates & Taxes | 3.86 | 7.33 | (3.47) |
| Insurance | 2.72 | 5.13 | (2.41) |
| Repair & Maintenance Expense | 39.64 | 37.95 | +1.69 |
| Selling and Distribution Expense | 154.08 | 448.51 | (294.43) |
| **Total** | **945.75** | **1,195.82** | **(250.07)** |

Sub-lines that fell by more than Rs 25 lakh (three):
- Selling and Distribution Expense: (294.43) — the dominant cause of the Note
  26 fall, 448.51 -> 154.08.
- Increase of Authorised Capital Expense: (29.25) — a FY23 one-off, nil in FY24.
- Bad Debt: (27.51) — 27.51 in FY23 to nil in FY24.

Reading: the whole Rs 250.07 lakh drop in Other expenses is explained by these
three lines (sum of falls 351.19), offset by rises in Labour Charges (+49.01),
Freight (+43.65) and CSR (+7.22).

---

## 4. Materials consumed, purchases of stock-in-trade, changes in inventories

Cost of materials consumed (Note 21, printed p.113):
> "21 Cost of materials consumed ... Opening Stock 251.98 / 398.74; Add:
> Purchase during the year 4593.68 / 5654.44; [4845.66 / 6053.18]; Less:
> Closing Stock 356.29 / 251.98; Total 4489.37 / 5801.20."

| | FY24 | FY23 |
|---|---:|---:|
| Opening Stock | 251.98 | 398.74 |
| Add: Purchase during the year | 4,593.68 | 5,654.44 |
| (subtotal) | 4,845.66 | 6,053.18 |
| Less: Closing Stock | 356.29 | 251.98 |
| **Cost of materials consumed** | **4,489.37** | **5,801.20** |

Purchases of stock-in-trade: NOT DISCLOSED as a separate line. The P&L
(printed p.88) carries no "Purchases of Stock-in-Trade" line; the company is a
manufacturer. The only purchase figure is "Purchase during the year" inside
Note 21 (4,593.68 / 5,654.44), which is raw-material purchases, not traded goods.

Changes in Inventories of Finished Goods and WIP (Note 22, printed p.113):
> "22 Changes in Inventories of Finished Goods and Work in Progress ...
> (Increase)/decrease in inventories 96.38 / (312.99)."

| | FY24 | FY23 |
|---|---:|---:|
| Opening: WIP | 92.69 | 45.43 |
| Opening: Finished goods | 274.29 | 306.94 |
| Opening: Goods-in-transit | 298.37 | 0.00 |
| Opening total | 665.35 | 352.37 |
| Closing: WIP | 160.00 | 92.70 |
| Closing: Finished goods | 305.97 | 274.29 |
| Closing: Goods-in-transit | 103.00 | 298.37 |
| Closing total | 568.97 | 665.36 |
| **(Increase)/decrease in inventories** | **96.38** | **(312.99)** |

Materials consumed as % of Revenue from operations (Note 19: 8,986.24 /
9,557.79):
- FY24: 4,489.37 / 8,986.24 = **49.96%**
- FY23: 5,801.20 / 9,557.79 = **60.70%**

Reading: the ~10.7 point drop in material intensity is the single biggest
driver of the FY24 margin lift.

---

## 5. Employee benefit expense split (Note 23, printed p.113)

> "23 Employee benefits expense: Director Remuneration 372.50 / 510.00;
> Salary, wages and Bonus 184.22 / 141.47; Gratuity 26.73 / 28.08;
> Contribution to Provident fund and ESIC 21.31 / 14.76; Staff Welfare
> Expense 18.10 / 8.38; Total 622.85 / 702.69."

| Component | FY24 | FY23 |
|---|---:|---:|
| Director Remuneration | 372.50 | 510.00 |
| Salary, wages and Bonus | 184.22 | 141.47 |
| Gratuity | 26.73 | 28.08 |
| Contribution to Provident fund and ESIC | 21.31 | 14.76 |
| Staff Welfare Expense | 18.10 | 8.38 |
| **Total** | **622.85** | **702.69** |

Reading: the fall (79.84) is entirely a directors' remuneration cut
(510.00 -> 372.50, -137.50); staff salaries actually rose (+42.75).
Director remuneration split is corroborated in Note 27 sub-3 (printed p.115):
Pritesh Ramani 137.00 / 192.00; Ketan Ramani 98.50 / 126.00; Jogindersingh
Jaswal 137.00 / 192.00; Total 372.50 / 510.00.

Employee headcount: NOT DISCLOSED in the financial statements or notes.

---

## 6. Power and fuel cost + per-tonne comparison (Note 26, printed p.114)

> "Power and Fuel Expense 59.07 / 53.58" — Note 26, printed p.114.

| | FY24 | FY23 |
|---|---:|---:|
| Power and Fuel Expense | 59.07 | 53.58 |

Production quantity for a per-tonne comparison: NOT DISCLOSED in the financial
statements or the notes. No production-volume figure (tonnes) appears in the
audited statements; a per-tonne power cost cannot be built from the filed
numbers.

---

## 7. One-off credit / provision reversal / write-back in FY24

Items in the audited statements that carry a credit, reversal or write-back
character in FY24:

> "Impairment loss recognized on Financial Asset (0.24)" — Note 26, printed
> p.114 (FY24 (0.24); FY23 0.31).

Reading: the (0.24) is a net reversal of expected-credit-loss allowance, a
credit to the P&L, not a charge. It is corroborated in the Cash Flow Statement
(printed p.89): "Allowance for credit losses Financial Asset (0.24)", and in
Note 8 (printed p.108) the ECL allowance fell from (0.31) at FY23 to (0.07) at
FY24.

> "Kasar & Discount 0.08 / 0.04" — Other income, Note 20, printed p.113.

Reading: a small rounding/discount credit of 0.08; immaterial.

No line labelled "liability no longer required written back", "excess provision
written back" or "provision reversal" appears in FY24. The other Other-income
credits (Duty Drawback 32.45, Subsidy 2.00, Interest Income 101.67) are
recurring operating items, not one-offs. Beyond the (0.24) ECL reversal:
NOT DISCLOSED.

---

## 8. Change in accounting policy, estimate, depreciation method, useful life,
inventory valuation FY23 -> FY24

No change is disclosed. The statements carry no "change in accounting policy",
"change in accounting estimate", or restatement note between FY23 and FY24.
The relevant policies read the same for both years:

> "Depreciation on Property, Plant and Equipment is provided on the reducing
> balance method over the estimated useful life of the assets as prescribed
> under Schedule II to the Companies Act, 2013." — Note 1.2, printed p.93.
> (The useful-life table lists Computer 3, Factory Buildings 30, Furniture &
> Fixtures 10, Lab Equipment 15, Office Equipment 15, Plant & Machineries 15,
> Vehicle 15, Factory Shed 30 years.)

> "For calculating inventories, the cost method for evaluation, it has been
> considered at FIFO Method." — Note 1.11 Inventories, printed p.103.

Reading: depreciation is reducing-balance (WDV) in both years; inventory
valuation is lower of cost (FIFO) and net realisable value in both years. A
change in method, estimate or useful life between FY23 and FY24:
NOT DISCLOSED (statements silent; no change stated).

---

## 9. Was any expense capitalised in FY24 that was expensed in FY23?

Policy allows pre-operative capitalisation:
> "Other Indirect Expenses incurred relating to project, net of income earned
> during the project development stage prior to its intended use, are
> considered as pre-operative expenses and disclosed under Capital
> Work-in-Progress." — Note 1.2 PPE, printed p.92.

FY24 CWIP movement (Note 3, printed p.106): opening as at 01-04-2023 nil;
"Addition/Adjustments 52.53; Capitalised during the Period 3.75; As at
31-03-2024 48.78" (Factory Building WIP). Balance Sheet (printed p.87) shows
Capital work-in-progress 48.78 at FY24 vs nil at FY23. Note 1.A (printed p.91)
notes the company "acquired an industrial plot on a leasehold basis at GIDC,
Dahej - II during the year."

Intangibles under development:
> "There is no any Intangible assets under development hence this clause is not
> applicable." — Note 27 sub-8 (iii), printed p.118.

Reading: FY24 opened a Rs 52.53 lakh CWIP (Dahej project) with pre-operative
expenses routed to CWIP under policy, versus nil CWIP in FY23. No note states
that a specific item expensed in FY23 was reclassified to capital in FY24, and
there are no intangibles under development. A deliberate FY23-to-FY24
capitalisation switch: NOT DISCLOSED.

---

## 10. IPO-related expenses treatment

The only IPO disclosure is in Note 27 sub-13 "Events subsequent to March 31,
2024" (printed p.124):
> "Intail public Offer (IPO): The Company has completed its Initial Public
> Offer (IPO) being 100% offer for sale of 95,70,000 equity shares of face
> value of INR 10 each at and issue price of INR 136 per share.(including
> premium of Rs.126 per share). Pursuant to the IPO, the equity shares of the
> Company were listed on National Stock Exchange of India Limited (NSE) and
> BSE Limited (BSE) on 10th June, 2024."

Reading: the issue was a 100% OFFER FOR SALE. The selling shareholders sold
existing shares; the company received no fresh-issue proceeds. Consistent with
this, equity share capital is unchanged at Rs 3,710.40 lakh across both years
(Balance Sheet printed p.87; Note 12 printed p.111), and no securities premium
account or movement appears in the Statement of Changes in Equity (printed
p.90) or Note 13 Other Equity (printed p.109). The IPO listing is a subsequent
event (10-Jun-2024, i.e. FY25), not an FY24 transaction.

Whether IPO expenses were charged to P&L, to securities premium, or borne by
the selling shareholders: NOT DISCLOSED. The AR does not state the treatment or
split of IPO/OFS issue expenses. (In a 100% OFS no fresh capital or securities
premium arose in FY24, and no IPO expense line appears in the FY24 P&L, but the
document does not state who bore the costs.)

---

## 11. Auditor's Report — Opinion, Key Audit Matters, Emphasis of Matter (FY24)

Auditor: Mahesh Udhwani and Associates, Chartered Accountants (Firm Reg. No.
129738W), signed by Mahesh Udhwani (Partner, M.No. 047328), UDIN
24047328BJZYOT1524, Place Vadodara, Date 28/06/2024 (printed pp.72-78).

OPINION (verbatim, printed p.73):
> "Opinion
> We have audited the standalone financial statements of KRONOX LAB SCIENCES
> LIMITED ("the Company") which comprise the Balance Sheet as at 31st March
> 2024, the Statement of Profit and Loss, statement of changes in equity and
> Statement of Cash Flows for the year ended on that date, and notes to the
> financial statements, including a summary of significant accounting policies
> and other explanatory information.
> In our opinion and to the best of our information and according to the
> explanations given to us, the aforesaid standalone financial statements give
> the information required by the Companies A, 2013 ("the Act") in the manner
> so required and give a true and fair view in conformity with the Indian
> accounting Standards prescribed u/s 133 of the Act read with the Companies
> (Indian Accounting Standards) Rules, 2015 as amended, and other accounting
> principles generally accepted in India, of the state of affairs of the
> Company as 31st March 2024, and profit, total comprehensive income, changes
> in equity and its cash flows for the year ended on that date."

(Reading: an unmodified/clean opinion. "Companies A, 2013" is the document's
own typo for "Companies Act, 2013".)

KEY AUDIT MATTERS (verbatim, printed p.73):
> "Key Audit Matters
> Key audit matters are those matters that, in our professional judgment, were
> of most significance in our audit of the financial statements of the current
> period. These matters were addressed in the context of our audit of the
> financial statements as a whole, and in forming our opinion thereon, and we
> do not provide a separate opinion on these matters. Based on the
> circumstances and facts of the audit and entity, there aren't key audit
> matters to be communicated in our report."

(Reading: the auditor reports NO key audit matters.)

EMPHASIS OF MATTER: NOT DISCLOSED. The report contains no "Emphasis of Matter"
paragraph. The sequence runs Opinion -> Basis for Opinion -> Key Audit Matters
-> Information Other than the Financial Statements, with no Emphasis of Matter
and no Material Uncertainty Related to Going Concern section (printed pp.73-78).

---

## 12. Note 1 — Significant Accounting Policies (printed pp.91-105), in full

> "Note - 1:-
> A. Reporting Entity
> KRONOX LAB SCIENCES LIMITED was incorporated on November 18, 2008 as a
> private limited company under Companies Act, 1956. The company has its
> registered office at Block No.353, Village Ekalbara, Padra Vadodara GJ
> 391440. The Company has completed its Initial Public Offer (IPO) and
> accordingly the Company's equity shares are listed on National Stock Exchange
> (NSE) and Bombay Stock Exchange (BSE) on 10th June, 2024.
> The Company is engaged in the manufacturing of High Purity Fine, inorganic
> chemicals, phosphate and metallic chemicals. The company commenced its
> business activities in year 2008. The Company carried out its activities at
> three locations (Unit-1, 2 & 3) in Ekalbara village, Padra. Additionally, the
> company acquired an industrial plot on a leasehold basis at GIDC, Dahej - II
> during the year.
> B. NOTES FORMING PART OF ACCOUNTS: / SIGNIFICANT ACCOUNTING POLICIES: /
> Summary of Significant Accounting Policies" (printed p.91)

> "1. Basis of preparation and presentation of financial statements:
> Compliance with Ind As: The financial statements of company has been prepared
> in accordance with Indian Accounting standards (Ind AS), under the historical
> cost conversion on the accrual basis unless specifically stated otherwise. The
> Ind AS are prescribed under section 133 of the Companies Act, 2013 read with
> companies (Indian accounting standards) Rules, 2015, as amended and other
> provisions of the Act.
> A. Basis of preparation: The financial statements of the company as at 31st
> March, 2024 are prepared in accordance with recognition and measurement
> principles of Indian Accounting Standards.
> B. Basis of measurement: The Financial Statements have been prepared on
> historical cost basis considering the applicable provisions of Companies Act
> 2013. The exceptions to the same are: -certain financial assets and
> liabilities (including derivative instruments) that are measured at fair
> value; and -net defined benefit (asset) / liability will be measured at year
> end on 31st March, 2024 after actuarial report has been obtained.
> C. Current and non-current classification of assets and liabilities: The
> Assets and Liabilities and the Statement of Profit & Loss, including related
> notes, are prepared and presented as per the requirements of Schedule III
> (Division II) to the Companies Act, 2013. All assets and liabilities have been
> classified and disclosed as current or non-current as per the Company's normal
> operating cycle and other criteria set out in Schedule III. Based on the
> nature of products and the time between the acquisition of assets for
> processing and their realization into cash and cash equivalents, the Company
> has ascertained its operating cycle as twelve months for the purpose of
> current and non-current classification of assets and liabilities.
> D. Functional and presentation currency: The functional and presentation
> currency in these Financial Statements is INR and all values are rounded to
> nearest lacs (INR 00,000), unless otherwise stated.
> E. Use of judgements, estimates and assumptions: The preparation of financial
> statements in conformity with Ind AS requires the Management to make
> estimates, judgments and assumptions that affect the reported amounts of
> revenue, expenses, current assets, non-current assets, current liabilities,
> noncurrent liabilities and the disclosure of the contingent liabilities on the
> date of the preparation of Financial Statements. Such estimates are on a
> reasonable and prudent basis considering all available information, however due
> to uncertainties about these judgements, estimates and assumptions, the actual
> results could differ from those estimates. Information about each of these
> estimates and judgements is included in relevant notes. Any revision to
> accounting estimates is recognized prospectively in current and future
> periods.
> Judgements: Information about judgements made in applying accounting policies
> that have the most significant effects on the amounts recognized in the
> Financial Statements is included in the following: Classification of financial
> assets: assessment of business model within which the assets are held and
> assessment of whether the contractual terms of the financial assets are solely
> payments of principal and interest on the principal amount outstanding."
> (printed pp.91-92)

> "2. Property, Plant and Equipment: Property, plant and equipment are stated at
> cost, less accumulated depreciation and impairment, if any. Costs directly
> attributable to acquisition are capitalized until the property, plant and
> equipment are ready for use, as intended by the Management. The Company
> depreciates property, plant and equipment over their estimated useful lives
> using the Written down value method. Other Indirect Expenses incurred relating
> to project, net of income earned during the project development stage prior to
> its intended use, are considered as pre-operative expenses and disclosed under
> Capital Work-in-Progress.
> An item of PPE is derecognised on disposal or when no future economic benefits
> are expected from use. Any profit or loss arising on the derecognition of an
> item of property, plant and equipment is determined as the difference between
> the net disposal proceeds and the carrying amount of the asset and is
> recognized in Statement of Profit and Loss.
> Subsequent Costs: The cost of replacing a part of an item of property, plant
> and equipment is recognised in the carrying amount of the item if it is
> probable that the future economic benefits embodied within the part will flow
> to the Company and its cost can be measured reliably. The carrying amount of
> the replaced part is derecognised. The cost of the day-to-day servicing the
> property, plant and equipment are recognised in the statement of profit and
> loss as incurred.
> Disposal: An item of property, plant and equipment is derecognised upon the
> disposal or when no future benefits are expected from its use or disposal.
> Gains and losses on disposal of an item of property, plant and equipment are
> determined by comparing the proceeds from disposal with the carrying amount of
> property, plant and equipment, and are recognised net within other income /
> expenses in the statement of profit and loss.
> Depreciation: The depreciable amount of an asset is determined after deducting
> its residual value. Where the residual value of an asset increases to an amount
> equal to or greater than the asset's carrying amount, no depreciation charge is
> recognised till the asset's residual value decreases below the asset's carrying
> amount. Depreciation of an asset begins when it is available for use, i.e., when
> it is in the location and condition necessary for it to be capable of operating
> in the intended manner. Depreciation of an asset ceases at the earlier of the
> date that the asset is classified as held for sale in accordance with Ind AS 105
> and the date that the asset is derecognised. Depreciation on Property, Plant and
> Equipment is provided on the reducing balance method over the estimated useful
> life of the assets as prescribed under Schedule II to the Companies Act, 2013.
> The management has estimated the useful life of the Tangible Assets as mentioned
> below: Computer 3; Factory Buildings 30; Furniture & Fixtures 10; Lab Equipment
> 15; Office Equipment 15; Plant & Machineries 15; Vehicle 15; Factory Shed 30.
> Impairment of all non-financial assets: The Company assesses at each balance
> sheet date whether there is any indication that an asset or cash generating unit
> (CGU) may be impaired. Indefinite life intangibles are subject to a review for
> impairment annually or more frequently if events or circumstances indicate that
> it is necessary. If any such indication exists, the Company estimates the
> recoverable amount of the asset. The recoverable amount is the higher of an
> asset's or CGU's fair value less costs of disposal or its value in use. Where
> the carrying amount of an asset or CGU exceeds its recoverable amount, the asset
> is considered impaired and is written down to its recoverable amount. In
> assessing the value in use, the estimated future cash flows are discounted to
> their present value using a pre-tax discount rate that reflects current market
> assessments of the time value of money and the risks specific to the asset. In
> determining the fair value less costs of disposal, recent market transactions
> are considered. An impairment loss is recognised if the carrying amount of an
> asset or CGU exceeds its recoverable amount, Impairment losses are recognised in
> the statement of profit and loss. If at the balance sheet date there is an
> indication that a previously assessed impairment loss no longer exists, an
> impairment loss is reversed only to the extent that the asset's carrying amount
> does not exceed the carrying amount that would have been determined, net of
> depreciation or amortisation, if no impairment loss had been recognised."
> (printed pp.92-94)

> "3. Investments and Deposits: The total investments are carried at their actual
> amount of investment. Further, these investments are not held with a view earn
> contractual cash flow instead there are a type of membership deposit made.
> Hence, they do not classify as Financial Assets in accordance with IND AS.
> 4. Leases: At inception of a contract, the Company assesses whether a contract
> is, or contains, a lease. A contract is, or contains, a lease if the contract
> conveys the right to control the use of an identified asset for a period of time
> in exchange for consideration. To assess whether a contract conveys the right to
> control the use of an identified asset, the Company assesses whether: - the
> contract involves the use of an identified asset...; - the Company has the right
> to obtain substantially all of the economic benefits from use of the asset
> throughout the period of use; and - the Company has the right to direct the use
> of the asset... Company as a lessee: The Company recognises a right-of-use asset
> and a lease liability at the lease commencement date. The right-of-use asset is
> initially measured at cost... The right-of-use asset is subsequently depreciated
> using the straight-line method from the commencement date to the earlier of the
> end of the useful life of the right-of-use asset or the end of the lease term...
> The lease liability is initially measured at the present value of the lease
> payments that are not paid at the commencement date, discounted using the
> interest rate implicit in the lease or, if that rate cannot be readily
> determined, the Company's incremental borrowing rate. Generally, the Company
> uses its incremental borrowing rates as the discount rate... In case of early
> termination of lease agreement, company will derecognise ROU asset and lease
> liability to reflect the partial or full termination of the lease and recognise
> gain or loss in P&L Account on such termination... Short-term leases and leases
> of low-value assets: The Company has elected not to recognise right-of-use
> assets and lease liability for the short-term leases that have lease term of 12
> months of less and leases of low-value assets. The Company recognises the lease
> payments as an operating expense on a straight-line basis over lease term."
> (printed pp.94-97)

> "5. Financial Assets: A. Fair Value Assessment: Fair value is the price that
> would be received to sell an asset or paid to transfer a liability in an orderly
> transaction between market participants at the measurement date... B. Subsequent
> Measurement: For purposes of subsequent measurement financial assets are
> classified in three categories: Financial assets measured at amortized cost;
> Financial assets at fair value through OCI; Financial assets at fair value
> through profit or loss. C. Financial Assets measured at amortized cost:
> Financial assets are measured at amortized cost if the financials asset is held
> within a business model whose objective is to hold financial assets in order to
> collect contractual cash flows and the contractual terms of the financial asset
> give rise on specified dates to cash flows that are solely payments of principal
> and interest on the principal amount outstanding... amortized using the
> effective interest rate ('EIR') method, less impairment... D. Trade
> Receivables: Unconditional receivables are recognised as financial assets when
> the entity becomes a party to the contract... trade receivables that do not
> contain a significant financing component are measured at transaction price.
> E. Financial Assets at fair value through OCI ('FVTOCI'): ... F. Financial
> Assets at fair value through profit or loss ('FVTPL'): ... G. Derecognition:
> The Company derecognizes a financial asset only when the contractual rights to
> the cash flows from the asset expire, or when it transfers the financial asset
> and substantially all the risks and rewards of ownership of the asset to
> another entity... H. Impairment of Financial Assets: The Company recognizes
> loss allowances using the expected credit loss (ECL) model for the financial
> assets which are not fair valued through profit or loss. Loss allowance for
> trade receivables with no significant financing component is measured at an
> amount equal to lifetime ECL. For all other financial assets, ECLs are measured
> at an amount equal to the 12-month ECL, unless there has been a significant
> increase in credit risk from initial recognition in which case those are
> measured at lifetime ECL..." (printed pp.97-99)

> "6. Financial Liabilities: The company's financial liabilities include trade
> payable. A. Initial recognition and measurement: All financial liabilities at
> initial recognition are classified as financial liabilities at amortized cost or
> financial liabilities at fair value through profit or loss, as appropriate...
> B. Subsequent Measurement: ... i) Financial liabilities classified as Amortized
> cost: ... Interest expense that is not capitalized as part of costs of assets is
> included as Finance costs in the Statement of Profit and Loss. ii) Financial
> liabilities classified as fair value through profit and loss (FVTPL): ...
> Exports benefits are accounted for in the year of exports based on the
> eligibility and when there is certainty of receiving the same. C. Trade
> Payables: Unconditional payables are recognised as financial liabilities when
> the entity becomes a party to the contract... trade payables that do not contain
> a significant financing component are measured at transaction price. D.
> Derecognition: A financial liability is derecognized when the obligation under
> the liability is discharged / cancelled / expired... E. Offsetting of Financial
> Instruments: Financial assets and financial liabilities are offset and the net
> amount is reported in the balance sheet if there is a currently enforceable
> legal right to offset the recognized amounts and there is an intention to settle
> on a net basis, to realize the assets and settle the liabilities
> simultaneously." (printed pp.99-100)

> "7. Cash Flows and Cash and Cash Equivalents: Statement of cash flows is
> prepared in accordance with the indirect method prescribed in the relevant IND
> AS. For the purpose of presentation in the statement of cash flows, cash and
> cash equivalents includes cash on hand, cheques and drafts on hand, deposits
> held with Banks, other short-term, highly liquid investments with original
> maturities of three months or less that are readily convertible to known
> amounts of cash and which are subject to an insignificant risk of changes in
> value, and book overdrafts. However, Book overdrafts are to be shown within
> borrowings in current liabilities in the balance sheet for the purpose of
> presentation.
> 8. Provisions and Contingent Liabilities and Contingent Assets: The company
> recognizes a provision when there is a present obligation as a result of past
> event that requires an outflow of resources and a reliable estimate can be made
> of the amount of the obligation. Contingent liability is a possible obligation
> arising from past events and whose existence will be confirmed only by the
> occurrence or non-occurrence of one or more uncertain future events not wholly
> within the control of the entity or a present obligation that arises from past
> events but is not recognized because it is not probable that an outflow of
> resources embodying economic benefits will be required to settle the obligation
> or the amount of the obligation cannot be measured with sufficient reliability.
> Contingent liabilities are disclosed after careful evaluation by the management
> of facts and legal aspects of the matter involved. Contingent Asset are neither
> recognized nor disclosed in the financial statements.
> 9. Revenue Recognition and Other Income: Revenue is recognized to the extent
> that it is probable that the economic benefits will flow to the Company and the
> revenue can be reliably measured, regardless of when the payment is being made.
> Revenue is measured at the fair value of the consideration received or
> receivable, taking into account contractually defined terms of payment and
> excluding taxes or duties collected on behalf of the government. Revenue from
> sale of goods is recognised when control of the goods or services are
> transferred to the customer at an amount that reflects the consideration
> entitled in exchange for those goods or services. The Company is generally the
> principal as it typically controls the goods or services before transferring
> them to the customer. Generally, control is transferred upon shipment of goods
> to the customer or when the goods is made available to the customer, provided
> transfer of title to the customer occurs and the Company has not retained any
> significant risks of ownership or future obligations with respect to the goods
> shipped. Interest income or expense is recognised using the effective interest
> rate method. The 'effective interest rate' is the rate that exactly discounts
> estimated future cash receipts or payments through the expected life of the
> financial instrument to: -the gross carrying amount of the financial assets;
> -the amortized cost of the financial liability. However, in case of interest
> income on fixed deposit with banks is booked as per the interest rate fixed by
> bank on such deposits.
> 10. Income Taxes: Income tax expense represents the sum of tax currently payable
> and deferred tax. Tax is recognized in the Statement of Profit and Loss, except
> to the extent that it relates to items recognized directly in equity or in other
> comprehensive income. Current Tax: Current tax comprises the expected tax
> payable or receivable on the taxable income or loss for the year and any
> adjustment to the tax payable or receivable in respect of previous years...
> Deferred Tax: Deferred tax is provided using the balance sheet method on
> temporary differences between the tax base of assets and liabilities and their
> carrying amounts for financial reporting purposes at the reporting date...
> Deferred tax assets are recognised for all deductible temporary differences, the
> carry forward of unused tax credits and any unused tax losses. Deferred tax
> assets are recognised to the extent that it is probable that taxable profit will
> be available... The carrying amount of deferred tax assets is reviewed at each
> reporting date and reduced to the extent that it is no longer probable that
> sufficient taxable profit will be available... Deferred tax assets and
> liabilities are measured at the tax rates that are expected to apply in the year
> when the asset is realized or the liability is settled, based on tax rates (and
> tax laws) that have been enacted or substantively enacted at the reporting date.
> Deferred tax assets and deferred tax liabilities are offset if a legally
> enforceable right exists to set off current tax assets against current tax
> liabilities and the deferred taxes relate to the same taxable entity and the
> same taxation authority. Deferred tax relating to items recognized outside
> profit or loss is recognized outside profit or loss. Deferred tax is also
> recognized in correlation to the underlying transaction reflected in OCI.
> 11. Inventories: Raw materials, Work in Progress, Finished Goods and Packing
> Material are stated at lower of cost and net realizable value. For calculating
> inventories, the cost method for evaluation, it has been considered at FIFO
> Method. Cost comprises expenditure incurred in the normal course of business in
> bringing such inventories to its present location and condition and includes,
> where applicable, appropriate overheads based on normal level if activity.
> 12. Foreign Currency Transactions: Transactions in foreign currencies are
> translated into the respective functional currency of the Company at the
> exchange rates at the dates of the transactions. Monetary assets and liabilities
> denominated in foreign currencies are translated into the functional currency at
> the exchange rate at the reporting date. Non-monetary assets and liabilities that
> are measured at fair value in a foreign currency are translated into the
> functional currency at the exchange rate when the fair value was determined.
> Non-monetory items that are measured based on historical cost in a foreign
> currency are translated at the exchange rate at the date of the transaction.
> Foreign currency differences are generally recognised in the Statement of Profit
> and Loss.
> 13. Dividend: The final dividend on shares is recorded as a liability on the date
> of approval by the shareholders and interim dividends are recorded as a liability
> on the date of declaration by the Company's Board of Directors.
> 14. Employee Benefits: Long-term Benefits: Provident Fund - Defined Contribution
> Plan: As the provisions of The Employees' Provident Fund and Miscellaneous
> Provisions Act & Employees State Insurance Act are applicable to the company. The
> Company's contribution paid/payable under the scheme is recognized as an expense
> in the statement of profit and loss during the period in which the employee
> renders the related services. Gratuity - Defined Benefit Plans: The company
> operates an unfunded defined benefit plan for its employees in the form of
> gratuity. The cost of providing benefits under this plan is determined on the
> basis of actuarial valuation at each reporting date, using the projected unit
> credit method, actuarial gain or loss for defined benefit plan are recognized in
> full in the year in which they occur in the statement of Profit and Loss. Short
> term Benefits: All employee benefits payable wholly within twelve months of
> rendering the service are classified as short-term employee benefits. Undiscounted
> value of benefits such as salaries, leave encashment incentives, allowances and
> bonus are recognized in the period in which the employee renders the related
> service.
> 15. Borrowing Cost: Borrowing costs directly attributable to the acquisition,
> construction or production of an asset, that necessarily takes substantial period
> of time to get ready for its intended use or sale, are capitalized as part of the
> cost of the respective asset. All other borrowing costs are expensed in the
> period in which they are incurred. Borrowing costs consist of interest, exchange
> differences arising from foreign currency borrowings to the extent they are
> regarded as an adjustment to the interest cost another cost that an entity incurs
> in connection with the borrowings of the funds.
> 16. Segment Reporting: Company is exclusively engaged in the business of
> manufacturing of chemicals. As such, in accordance with Ind AS, our Company's
> business is considered to constitute one single primary segment.
> 17. Earnings Per Share: Basic EPS is calculated by dividing the profit for the
> year attributable to equity holders of the Company by the weighted average number
> of equity shares outstanding during the financial year, adjusted for bonus
> elements and stock split in equity shares issued during the year and excluding
> treasury shares. The weighted average number of equity shares outstanding during
> the period and for all periods presented is adjusted for events, such as bonus
> shares and stock split, other than the conversion of potential equity shares that
> changed the number of equity shares outstanding, without a corresponding change
> in resources. Diluted EPS adjust the figures used in the determination of basic
> EPS to consider. The after-income tax effect of interest and other financing costs
> associated with dilutive potential equity shares, and The weighted average number
> of additional equity shares that would have been outstanding assuming the
> conversion of all dilutive potential equity shares." (printed pp.100-105)

(Reading: Note 1 runs items A-B plus policies 1-17. Manufacturer, single
segment, Ind AS historical cost, WDV depreciation per Schedule II, FIFO
inventory at lower of cost/NRV, unfunded gratuity by projected unit credit,
ECL model for financial assets. Nothing in Note 1 signals a policy change
versus FY23.)

---

## VERIFICATION LINE

- Filename: `8cda34fd-e700-4fbb-ae5d-c215cb7a976a.pdf` — this is the Kronox Lab
  Sciences Limited Annual Report FY2023-24 (15th AGM notice; year ended
  31-Mar-2024; audit report dated 28/06/2024). Note: the AGM cover letter
  (PDF p.1) reads "15th AGM"; the CLAUDE.md brief's "15th AGM" wording matches.
- Report date: audit report and financial statements signed 28th June, 2024,
  Vadodara (printed pp.78, 87, 88, 89, 124).
- Statement of Profit and Loss: printed page 88 (PDF p.88).
- Balance Sheet: printed p.87. Cash Flow: printed p.89. Statement of Changes in
  Equity: printed p.90.
- Notes quoted, with pages:
  - Note 1 Significant Accounting Policies: printed pp.91-105.
  - Note 2 PP&E / Note 3 CWIP: printed p.106.
  - Note 6/6A Deferred Tax & tax reconciliation, Note 7 Inventories:
    printed p.107.
  - Note 8 Trade receivables (ECL allowance): printed p.108.
  - Note 12 Share Capital: printed p.111.
  - Note 13 Other Equity: printed p.109.
  - Note 19 Revenue / Note 20 Other income / Note 21 Cost of materials consumed
    / Note 22 Changes in inventories / Note 23 Employee benefits: printed p.113.
  - Note 24 Finance costs / Note 25 Depreciation / Note 26 Other expenses /
    Note 27 sub-1 (payment to auditors): printed p.114.
  - Note 27 sub-2 EPS / sub-3 Director remuneration / sub-4 Gratuity:
    printed pp.115-116.
  - Note 27 sub-13 Events subsequent (IPO): printed pp.123-124.
- Auditor's Report (Opinion, KAM, Basis for Opinion, responsibilities):
  printed pp.72-78; Opinion and KAM on printed p.73.
