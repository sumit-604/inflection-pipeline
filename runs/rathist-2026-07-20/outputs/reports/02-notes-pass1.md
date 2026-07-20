# STAGE 2 — NOTES TO FINANCIAL STATEMENTS, PASS 1 OF 3
Company: Rathi Steel & Power Ltd (RATHIST) | Run date: 2026-07-20
Model: Sonnet 5 | Source: Annual_Report_2023.pdf (as supplied)

## ⚠️ CRITICAL DOCUMENT-IDENTIFICATION FLAG (read first)

The supplied file is named `Annual_Report_2023.pdf`, and the task brief states
this is "the FY2023 annual report (the only AR on file; no FY24/FY25/FY26 AR
exists)." **This is factually incorrect based on the document's own content.**
The PDF's cover page, notice, board's report, auditor's report, balance sheet
and every page footer read "**Annual Report 2024-25**" and "**54th Annual
General Meeting**" to be held 30 September 2025. The financial statements
audited within are for the **year ended 31st March 2025** (FY2024-25), with
FY2023-24 comparatives, and the Other Equity note (Note 12) additionally
carries a FY2022-23 column. The auditor's report is dated 30/05/2025 and the
AGM notice is dated 03/09/2025 (p.1-16, p.67-76). There is no FY2023
(year-ended-March-2023) annual report content anywhere in this file.

**Implication:** this is in fact the most current AR available (FY25, not
FY23), one year newer than the run brief assumed. All figures, anchors and
findings below are extracted from FY2024-25 as reported, with FY2023-24 (and
where shown, FY2022-23) as comparatives. This discrepancy should be corrected
in the run metadata before downstream valuation stages proceed, since a stage
expecting "FY2023 data" would otherwise be working with mislabeled inputs.

All amounts below are ₹ Lakh unless stated as ₹ Cr for readability; page
references are the printed page numbers in the document footer (e.g. p.78).

---

## STRUCTURAL NOTE ON NUMBERING

The Notes to Financial Statements use two independent, overlapping numbering
sequences that both start at "1"/"2":
1. **Balance-sheet/P&L-linked notes** Note 1 (Company Information) through
   Note 27 (Extraordinary/Exceptional Items), referenced directly from the
   Balance Sheet and Statement of P&L "Note No." columns (p.75-84).
2. **"NOTES ON ACCOUNTS" 1-22**, a separate free-standing block of textual
   disclosures (Commitments, Contingent Liabilities, Segmental Reporting, FX,
   RPT, ageing schedules, solvency ratios, etc.) that follows immediately
   after the accounting-policy note and restarts numbering at "1" (p.89-94).

This dual numbering is itself a minor disclosure-quality observation (🟡):
a reader or automated extraction tool can easily conflate "Note 2" (PPE) with
"Note 2" (Significant Accounting Policies). Below, findings are anchored using
the sequence they belong to, explicitly labelled.

---

## NOTE-BY-NOTE EXTRACTION

### Note 1 — Company Information (p.86)
Rathi Steel and Power Limited, public limited company incorporated 1971,
engaged in steel and steel-related products. 🟢 Clean, routine.

### Note 2 — Significant Accounting Policies (a)-(p) (p.86-90)
- **(a) Basis of preparation:** Ind AS, Companies Act 2013, SEBI guidelines.
  No first-time standard adoption disclosed this year. 🟢
- **(b)-(c) Use of estimates / critical judgments:** Standard boilerplate.
  Areas of judgment named: useful life of PPE, taxability of certain income,
  claims recognition, trade receivable impairment, provisions/contingencies.
  No quantified sensitivity given for any of these. 🟢
- **(e) Revenue recognition:** point-in-time on shipment/delivery to
  customer; standard for a steel manufacturer, not aggressive. Job
  work/conversion charges recognized net of taxes under revenue. 🟢
- **(f)-(g) Impairment (non-financial assets, financial assets):**
  Qualitative policy only. No impairment loss recognized in either year (no
  impairment note triggered). ECL: "simplified approach," lifetime ECL from
  initial recognition — **no numeric ECL matrix/rate table disclosed
  anywhere in the AR** (NOT FOUND IN DOCUMENT). 🟡 Watch — required
  disclosure of the ECL basis (ageing-linked % rates) is qualitative only.
- **(h) Inventories:** lower of cost (weighted average) and NRV. No
  write-down or obsolescence disclosure found this year (NOT FOUND IN
  DOCUMENT — no inventory write-down / obsolete stock note despite the large
  finished-goods build, see Note 6 below). 🟡 Watch.
- **(j) PPE:** Schedule II useful lives, straight-line, single-shift basis.
  Leasehold land revalued once, as at 31 March 1992 (legacy revaluation,
  Revaluation Reserve ₹190.26 Lakh static across all three years shown —
  Note 12). No current-year revaluation, no change in useful lives
  disclosed. 🟢
- **(k) Investments:** long-term investments at cost, less-than-permanent
  diminution not provided. See Note 3 below for an apparent inconsistency
  with FVOCI classification. 🟡 Watch.
- **(m) Current Tax and Deferred Tax:** "In view of losses incurred in
  preceding previous years, company has not calculated deferred tax." **This
  directly conflicts with the Balance Sheet, which carries a static Deferred
  Tax Asset of ₹7,290.97 Lakh (₹72.91 Cr) unchanged between 31 March 2024 and
  31 March 2025** (p.75, p.86). No deferred tax note anywhere in the AR
  provides a component breakup, an effective-vs-statutory rate
  reconciliation, MAT credit position, or a realizability/recoverability
  reassessment for this asset (NOT FOUND IN DOCUMENT for all of these —
  see extraction item 10, "Deferred Tax," which is essentially unaddressed
  beyond this one static balance-sheet line). 🔴 Red Flag — see Pass 1
  Summary rank #1.
- **(n) Retirement benefits:** "Actual liability for gratuity is provided in
  respect of eligible employees." **No Ind AS 19 disclosure set is present**
  — no actuarial assumptions (discount rate, salary escalation, mortality),
  no funded status, no plan-asset reconciliation, no sensitivity analysis —
  despite a non-current Gratuity provision of ₹207.45 Lakh (Note 14, p.82).
  NOT FOUND IN DOCUMENT. 🟡 Watch — material disclosure gap for a listed
  Ind AS preparer.
- **(o) Foreign exchange:** monetary items translated at closing rate;
  exchange differences through P&L. No hedging policy/instruments described
  (see Notes on Accounts item 4 and Corporate Governance p.60, which states
  flatly "no commodity price risk or foreign exchange risk as there is no
  hedging activities" — an odd assertion given the company has FX-denominated
  raw material and capital-goods purchases; see below). 🟡 Watch.
- **(p) Provisions/contingent liabilities/assets:** Standard IND AS 37
  language. 🟢

### Note 2 (balance sheet) — Property, Plant and Equipment (p.77)
Gross block grew ₹201.79 Cr → ₹224.40 Cr (+11.2%), driven almost entirely by
Plant & Machinery additions of ₹20.96 Cr in the year (₹192.31 Cr → ₹213.27 Cr
gross). Net block ₹70.35 Cr → ₹83.38 Cr. Depreciation for the year ₹9.57 Cr
vs ₹8.74 Cr PY. No impairment, no disposals of any consequence (Sales/
Adjustment column is nil throughout). Vehicles net block rose sharply
(₹0.10 Cr → ₹1.49 Cr on additions of ₹1.46 Cr) — cross-references to Notes on
Accounts item 20 (p.94): "Company has purchased second hand vehicles during
the year, registration of three vehicles are yet to get transferred in name
of the Company however applicable depreciation has been charged on the
same." 🟡 Watch — asset title/registration not yet perfected on depreciated
assets; minor legal/governance point, immaterial in size (~₹1.46 Cr) but
worth tracking for closure.

### Note 3 — Non-Current Investments (p.78)
Small book: quoted equity instruments (Bank of Baroda, SBI, Focus Industrial
Resources, BOB Pioneer PSU Mid Cap fund) held "At FVOCI," total cost/carrying
₹10.49 Lakh both years; unquoted investments (Moradabad Syntex, First
Financial Services, Lynx Traders) ₹0.44 Lakh gross less ₹0.12 Lakh provision
for diminution. **Fair Market Value of quoted investments is separately
disclosed at ₹21.08 Lakh (FY25) / ₹21.52 Lakh (FY24) — roughly double the
₹10.49 Lakh "Value" column carried in the primary table.** Since the
instruments are stated to be designated at FVOCI under Ind AS 109, the
balance sheet carrying amount should equal fair value, not cost; the
presentation instead totals to the cost-basis figure with fair value shown
only as a memo line. 🟡 Watch — likely a presentation/measurement
inconsistency versus the stated FVOCI classification, though immaterial in
absolute size (₹10-21 Lakh against total assets of ₹265.42 Cr).

### Note 4 — Other Financial Assets, Non-current (p.78)
Security Deposit ₹395.10 Lakh vs ₹350.70 Lakh (+12.7%). 🟢 Routine.

### Note 5 — Other Non-Current Assets (p.78)
Trade receivable/advance recoverable, reclassified out of current assets:
Unsecured Considered Good ₹0.00 (FY25) vs ₹100.52 Lakh (FY24); Unsecured
Considered Doubtful ₹97.52 Lakh (FY25) vs ₹0.00 (FY24), less provision for
bad & doubtful ₹76.50 Lakh (FY25) vs ₹0.00 (FY24); plus a Miscellaneous
Expenses (not written off) balance of ₹76.50 Lakh appears again as a
separate memo line — the note's internal arithmetic is not fully
transparent line-by-line. Net total ₹174.02 Lakh vs ₹100.52 Lakh. This
ties to the trade receivable ageing schedule (Notes on Accounts item 13,
p.93) which shows a disputed >3-year doubtful bucket of ₹97,51,973 for FY25.
**Only ₹76.50 Lakh (78.4%) of the ₹97.52 Lakh doubtful receivable is
provided for — roughly ₹21 Lakh remains unprovided.** 🟡 Watch — modest ECL
provisioning gap on disputed long-ageing receivables; small in absolute
terms.

### Note 6 — Inventories (p.78)
| Category | FY25 (₹ Lakh) | FY24 (₹ Lakh) | YoY % |
|---|---|---|---|
| Raw Material | 1,138.63 | 959.94 | +18.6% |
| Work-in-progress | 0.00 | 0.00 | — |
| Finished Goods | 3,441.23 | 1,399.45 | **+145.9%** |
| Stores & Spares | 393.43 | 564.31 | -30.3% |
| Fuel & Oils | 35.59 | 35.47 | +0.3% |
| **Total** | **5,008.87** | **2,959.17** | **+69.3%** |

Revenue from operations grew only 2.0% in the same period (₹503.15 Cr vs
₹493.19 Cr, Note 20). **Finished goods inventory more than doubled while
revenue was essentially flat — a major disconnect.** No inventory
write-down, no obsolescence disclosure accompanies this build (NOT FOUND IN
DOCUMENT). This inventory increase drives the P&L "Changes in Inventories"
line to -₹20.42 Cr (a stock increase, which reduces reported cost of goods
sold and flatters gross margin/EBITDA) versus a +₹9.29 Cr stock decrease in
the prior year — a ~₹29.7 Cr swing in the P&L's favour purely from
inventory movement (Note 23, p.83). 🔴 Red Flag — see Pass 1 Summary #2.

### Note 7 — Trade Receivables (p.78)
Considered Good ₹4.70 Lakh, Considered Doubtful ₹0.66 Lakh, less provision
for doubtful debts -₹4.49 Lakh, "Others" ₹2,476.56 Lakh, Total ₹2,477.43
Lakh vs ₹1,626.43 Lakh PY (**+52.3%**), against revenue growth of only 2.0%.
The "Others" category (₹24.77 Cr, essentially the entire receivable book) is
not a standard Ind AS ageing category and its composition is not explained —
NOT FOUND IN DOCUMENT for what "Others" comprises. Cross-referenced to the
company's own Solvency Ratio table (Notes on Accounts item 17, p.93): Trade
Receivables Turnover Ratio fell from 40.50x to 24.52x, described by the
company itself only as "Better collection from customers" — **this
explanation appears to be the opposite of what the ratio and the ageing
schedule (below) actually show.** 🔴 Red Flag — see Pass 1 Summary #5.

### Note 8 — Cash and Cash Equivalents (p.78)
Total cash and equivalents fell from ₹650.28 Lakh to ₹129.42 Lakh (-80.1%).
Balance with banks on current account fell from ₹547.55 Lakh to ₹19.22 Lakh.
🟡 Watch (context: see cash flow analysis under Pass 1 Summary #1 — this
decline is a symptom of negative operating cash flow, not a standalone
liquidity crisis given new bank facilities were drawn).

### Note 9 — Other Financial Assets, Current (p.78)
Advance recoverable in cash/kind ₹1,410.67 Lakh vs ₹996.31 Lakh (+41.6%);
Balance with Statutory/Government Authorities ₹481.00 Lakh vs ₹626.84 Lakh
(-23.3%); Trade advances ₹28.03 Lakh less provision for doubtful -₹3.38
Lakh. Total ₹1,980.16 Lakh vs ₹1,705.77 Lakh. 🟡 Watch — the growth in
"advance recoverable" is not explained; composition/counterparty not
disclosed (NOT FOUND IN DOCUMENT).

### Note 10 — Other Current Assets (p.79)
Prepaid Expenses ₹3.46 Lakh, Advance Income Tax/TDS ₹107.24 Lakh vs ₹216.07
Lakh PY. Total ₹110.70 Lakh vs ₹221.15 Lakh. 🟢 Routine.

### Note 11 — Equity Share Capital (p.79-80)
Extensive capital restructuring activity disclosed:
- Authorized capital reclassified during the year to ₹131.65 Cr (12,12,40,000
  equity shares of ₹10 + 1,04,08,147 preference shares of ₹10).
- Issued/paid-up equity rose from ₹85.06 Cr (8,50,63,003 shares) to ₹86.36 Cr
  (8,63,63,004 shares) — 13,00,001 shares issued in the year via conversion
  of Optionally Convertible Redeemable Preference Shares (OCRPS).
- Preference share capital fell from ₹10.40 Cr (1,03,99,265 shares) to ₹8.89
  Cr (88,94,000 shares) as 15,05,265 OCRPS were converted into equity.
- **Preference share terms:** 1% non-cumulative coupon, redeemable after 20
  years from issue date (or extension at a premium of ₹20/share over issue
  price) — an unusual, long-dated, low-coupon quasi-equity instrument. 🟡
  Watch — relevant to capital-structure and dilution analysis for
  valuation; the redemption obligation (20-year tenor) and conversion
  history should be modelled explicitly rather than treated as simple debt
  or simple equity.
- **Major shareholder movement:** PCR Holdings Private Ltd (formerly Archit
  Securities Private Ltd) increased its equity stake from 24.91% to 26.41%
  (2,11,86,867 → 2,28,06,868 shares) while its OCRPS holding fell from
  14.47% to nil (converted). Promoter Pradeep Kumar Rathi's direct stake
  slipped slightly from 9.43% to 9.11%. Preference shares are held
  predominantly by Char Investment and Trading Limited (72.57%) and Lenzing
  Poly Packs Limited (27.43%) — **neither of these two preference
  shareholders, nor PCR Holdings, is named in the Related Party Disclosure
  (Note 12 of Notes on Accounts, p.92), which lists only Smt Sushila Rathi
  as a related individual.** Whether Char Investment, Lenzing Poly Packs or
  PCR Holdings are promoter-linked entities is NOT FOUND IN DOCUMENT. 🟡
  Watch — worth an ownership-structure question for management given the
  concentration of preference-share and rising-equity-stake holders in
  entities not confirmed as arm's-length third parties.

### Note 12 (balance sheet) — Other Equity (p.81)
Three-year view (FY23/FY24/FY25) reveals a major balance-sheet turnaround:
- Closing "Other Equity": **-₹100.41 Cr (FY23) → +₹27.61 Cr (FY24) → +₹41.77
  Cr (FY25).**
- Retained Earnings (accumulated losses) remains deeply negative throughout:
  -₹444.43 Cr (FY23 opening) → -₹357.20 Cr (FY24 closing) → -₹319.72 Cr
  (FY25 closing). Even after two years of positive PAT (₹87.22 Cr add in
  FY23-comparative-column terms is actually shown as "Loss for the year" 
  ₹8,722.29 Lakh added back to reduce the deficit; then ₹2,353.40 Lakh in
  FY24; then ₹1,395.43 Lakh in FY25), the accumulated deficit remains
  roughly 8x the FY25 net worth's positive components combined.
- The swing to positive Other Equity is driven substantially by
  **non-operating capital actions**, not retained profit: ₹12.76 Cr credited
  to General Reserve in FY24 "on account of Waiver of Term Loan by
  Lenders," and ₹156.95 Cr received as Securities Premium in FY24 (against
  the ₹114.71 Cr preferential equity issue and OCRPS conversion referenced
  in Auditor's Annexure-A item 10(b), p.71).
- General Reserve itself: ₹78.14 Cr (FY23) → ₹146.75 Cr (FY24, +₹68.60 Cr
  reclassification/transfer) → ₹159.50 Cr (FY25, no further lender-waiver
  credit this year).

🟡 Watch / context-critical — the company's positive net worth trajectory
over the last two years is real but is largely a product of debt-waiver
accounting and large capital raises rather than organic profit
accumulation; core annual profitability (₹9-24 Cr range pre-exceptional,
see Note 27 below) is small relative to the ₹319.72 Cr accumulated deficit
still on the books. See Pass 1 Summary #9.

### Note 13 — Borrowings, Non-Current (p.82)
Term Loans ₹351.39 Lakh, Working Capital Term Loans ₹0.00, Finance/Lease
Obligations ₹5.37 Lakh, Total ₹356.76 Lakh — **versus ₹0.00 disclosed in the
prior year (both non-current and current, see Note 16).** Secured by first &
exclusive charge on all existing/future movable & immovable fixed and
current assets, hypothecation of plant & machinery at the Ghaziabad
facility, and personal guarantees of Shri Udit Rathi and Shri Pradeep
Rathi (promoter-family personal guarantees on company debt). 🟡 Watch —
promoter personal guarantees on secured bank facilities are a governance
item worth noting (not inherently negative, but a dependency).

### Note 14 — Provisions, Non-Current (p.82)
Gratuity provision ₹207.45 Lakh vs ₹200.04 Lakh. As noted under Note 2(n),
no actuarial assumption disclosure accompanies this. 🟡 Watch (cross-ref).

### Note 15 — Other Long-Term Liabilities (p.82)
Unsecured Loans ₹20.25 Lakh vs ₹161.04 Lakh (-87.4%); Sundry Creditors for
Capital Goods ₹120.39 Lakh vs ₹41.30 Lakh (+191.5%, consistent with the
capex ramp in PPE Note 2); Trade Deposits from Dealers ₹11.57 Lakh flat.
Total ₹152.22 Lakh vs ₹213.91 Lakh. 🟢 Routine, though the unsecured loan
counterparty is not identified — NOT FOUND IN DOCUMENT (could be
related-party in nature given the "Unsecured Loans" label and the RPT thin
disclosure noted above; not confirmable from this document).

### Note 16 — Borrowings, Current (p.82)
Secured working capital facilities from bank: ₹3,417.31 Lakh vs ₹0.00 PY.
Same security package language as Note 13 (near-identical boilerplate
repeated verbatim). **Combined with Note 13, total disclosed borrowings rose
from ₹0.00 to ₹3,774.07 Lakh (₹37.74 Cr) in one year** — funding both the
₹22.60 Cr fixed-asset capex (cash flow statement, p.85) and a working
capital build. Cross-references Director's Report (p.17): "The Company
availed credit facilities to the tune of Rs. 40.06 Crores from Kotak
Mahindra Bank Limited in the form of O.D / Term Loan during the Financial
Year 2024-25." 🟡 Watch — a fresh, meaningful re-leveraging event; combined
with the DSCR deterioration below this is a capital-structure item worth
tracking. See Pass 1 Summary #6.

### Note 17 — Trade Payables (p.82)
₹8,243.13 Lakh vs ₹6,422.42 Lakh (+28.4%), versus 2.0% revenue growth and
39,829.20 vs 36,577.88 Lakh cost of materials consumed (+8.9%). Payables
growing faster than the purchase base suggests some stretching of
supplier terms, consistent with the company's own Trade Payables Turnover
Ratio falling from 5.72x to 4.85x (Notes on Accounts item 17, p.93). See
Note 8 of Notes on Accounts below for the MSME disclosure gap that directly
touches this balance. 🟡 Watch.

### Note 18 — Other Current Liabilities (p.82)
Statutory Dues Payable ₹94.50 Lakh vs ₹929.49 Lakh (-89.8%); Advances From
Customers ₹102.44 Lakh vs ₹1,356.84 Lakh (-92.4%); Other Payable ₹75.21 Lakh
vs ₹490.54 Lakh; Current Maturities of Long-Term Debt ₹156.77 Lakh vs
₹0.00. Total ₹428.92 Lakh vs ₹2,776.87 Lakh (-84.6%). 🟡 Watch — the sharp
fall in Advances From Customers (down ₹12.5 Cr) alongside the finished-goods
inventory build (Note 6) is a pattern worth noting together: less
customer prepayment plus more unsold finished stock plus slower receivables
collection is a coherent, and not reassuring, demand-side narrative.

### Note 19 — Provisions, Current (p.82)
Bonus ₹13.38 Lakh, Leave Encashment ₹20.55 Lakh, Total ₹33.93 Lakh vs
₹30.03 Lakh. 🟢 Routine.

### Note 20 — Revenue from Operations (p.83)
Sale of Products/Services ₹50,117.05 Lakh vs ₹48,779.87 Lakh (+2.7%); Other
Operating Revenue ₹198.17 Lakh vs ₹538.69 Lakh (-63.2%). Total ₹50,315.22
Lakh vs ₹49,318.56 Lakh (+2.0%). **No disaggregation by product, geography,
or customer is disclosed** (single-segment claim under Note 3 of Notes on
Accounts exempts Ind AS 108 segment reporting — NOT FOUND IN DOCUMENT for
any product-mix or customer-concentration detail). Director's Report
(p.16-17) separately discloses rolled-product volume fell from 59,488.595 MT
to 47,440.040 MT (-20.3%) — **volume fell over 20% while rupee revenue rose
2.7%, implying realized price/mix improved materially, or a compositional
shift (e.g., higher share of job-work / less low-margin tonnage).** 🟡
Watch — worth a management question given the volume-value divergence is
large and unexplained in the notes.

### Note 21 — Other Income (p.83)
Interest Income ₹68.36 Lakh vs ₹25.13 Lakh; Net gain on sale of fixed
assets ₹0.00 vs ₹1.30 Lakh; Dividend income ₹1.87 Lakh vs ₹0.94 Lakh;
Provision no longer required, written back ₹0.89 Lakh vs ₹5.04 Lakh; Sundry
Balance Written Back (Net) ₹33.30 Lakh vs ₹233.24 Lakh; **Claims Received
₹123.75 Lakh vs ₹0.00 PY**; Profit on Sale of Investments ₹0.00 vs ₹44.11
Lakh. Total ₹228.17 Lakh vs ₹309.76 Lakh. 🟡 Watch — Other Income continues
to carry meaningful non-recurring components (claims received, balance
write-backs) in both years; nature of the ₹123.75 Lakh "Claims Received" is
not disclosed (NOT FOUND IN DOCUMENT — no note explains what claim this is).

### Note 22 — Cost of Materials Consumed (p.83)
₹39,829.20 Lakh vs ₹36,577.88 Lakh (+8.9%), against a 2.7% rise in product
sale revenue — raw material cost growing faster than revenue is consistent
with the margin compression shown in the solvency ratios (Net Profit Ratio
3% vs 5%). 🟡 Watch.

### Note 23 — Changes in Inventories of Finished Goods and WIP (p.83)
Covered above under Note 6 — the -₹2,041.78 Lakh (stock increase) versus
+₹929.11 Lakh (stock decrease) PY swing is the single largest driver of the
year's reported cost-of-sales relief. 🔴 Red Flag (cross-ref Note 6, Pass 1
Summary #2).

### Note 24 — Employee Benefit Expenses (p.83)
Salaries, Wages and Bonus ₹1,167.69 Lakh vs ₹902.66 Lakh (+29.4%);
Contribution to PF and other funds ₹33.72 Lakh vs ₹32.10 Lakh; Staff
Welfare ₹6.09 Lakh vs ₹16.53 Lakh. Total ₹1,207.50 Lakh vs ₹951.29 Lakh
(+26.9%) — a materially faster growth rate than revenue (2.0%), not
explained (no headcount disclosure found — NOT FOUND IN DOCUMENT). 🟡 Watch.

### Note 25 — Finance Costs (p.83)
| Line | FY25 | FY24 |
|---|---|---|
| Interest on Loans | 544.64 | **0.00** |
| Other Borrowing Costs | 0.00 | 0.00 |
| Bank Charges & Processing Fees/Finance Charges | 5.62 | **1,173.57** |
| **Total** | **550.26** | **1,173.57** |

**The composition flips almost entirely between the two years**: FY24 shows
essentially all ₹1,173.57 Lakh of finance cost labelled "Bank Charges &
Processing Fees," with zero "Interest on Loans," despite the balance sheet
showing zero period-end borrowings in FY24 (Notes 13 & 16). FY25 reverses
this — ₹544.64 Lakh of genuine "Interest on Loans" against new borrowings,
with bank charges collapsing to ₹5.62 Lakh. This large FY24 "bank
charges" figure very plausibly relates to interest/charges on the
short-term borrowings that were subsequently waived by lenders in the same
year (Note 27: "Waiver of Short Term Borrowings from Lenders" ₹1,983.65
Lakh) — but the note gives no explanation linking the two, and the
classification choice (interest recharacterized as "bank charges") is
unusual and not explained anywhere. 🟡 Watch — a legitimate management
question on why finance-cost composition changed so completely between
years with no note cross-reference.

### Note 26 — Other Expenses (p.84)
Total ₹9,117.37 Lakh vs ₹8,745.13 Lakh (+4.3%). Notable line-item moves:
Consumption of Stores & Spares ₹3,151.18 Lakh vs ₹2,409.77 Lakh (+30.8%);
Power & Fuel ₹4,510.33 Lakh vs ₹5,466.26 Lakh (-17.5%, consistent with the
20% volume decline in Note 20); **Legal & Professional Charges ₹316.23 Lakh
vs ₹138.18 Lakh (+128.9%)** — more than doubled, no explanation given (NOT
FOUND IN DOCUMENT); Travelling & Conveyance ₹195.04 Lakh vs ₹131.80 Lakh
(+48.0%); Freight Outward ₹467.75 Lakh vs ₹301.19 Lakh (+55.3%, faster than
revenue, consistent with a mix shift or geographic spread change);
Auditors' Remuneration flat at ₹4.00 Lakh both years. 🟡 Watch — the
Legal & Professional Charges jump is the most notable unexplained item and
warrants a management question (could reflect the capital-raise/debt-
restructuring activity, litigation defense on the contingent-liability
matters below, or something else — not disclosed).

### Note 27 — Extraordinary/Exceptional Items (p.84)
| Item | FY25 | FY24 |
|---|---|---|
| Waiver of Short Term Borrowings from Lenders | 0.00 | 1,983.65 |
| Exceptional Income (Electricity duty refund) | 471.48 | 0.00 |
| **Total** | **471.48** | **1,983.65** |

**Both of the last two reported years carry a large, different "exceptional"
gain that materially inflates reported PBT.** Profit before exceptional
items & tax was only ₹923.95 Lakh (FY25) and ₹377.06 Lakh (FY24) — i.e.
underlying, pre-exceptional operating profitability is thin, and the
headline PBT figures of ₹1,395.43 Lakh (FY25, +51% from the exceptional
item) and ₹2,360.71 Lakh (FY24, +526% from the exceptional item) are both
substantially propped up by non-recurring items of a different character
each year (a term-loan waiver, then an electricity-duty refund). 🔴 Red Flag
— see Pass 1 Summary #3.

---

## NOTES ON ACCOUNTS (separate numbering, p.89-94)

### Item 1 — Commitments (p.89)
Estimated capital commitments: NIL (PY NIL). 🟢

### Item 2 — Contingent Liabilities (p.89-91)
| Item | Amount (₹) | ₹ Cr | Status |
|---|---|---|---|
| Bank guarantees / counter-guarantees | NIL (PY ₹40,17,112) | 0 (PY 0.40) | — |
| Letters of Credit | NIL | — | — |
| VAT/Sales Tax disputed (company's appeals) | 5,16,45,541 | 5.16 | Stayed, company confident |
| VAT/Sales Tax (department's appeals, in company's favour) | 10,64,73,573 | 10.65 | Contra item, not a liability |
| Excise/Service Tax disputed | 7,67,29,699 | 7.67 | Company confident of relief |
| GST disputed | 3,40,33,408 | 3.40 | Appeals/writ filed |
| Civil/Recovery suits and Labour cases (not acknowledged as debt) | 12,78,48,416 | 12.78 | vs PY 12,48,10,916 |
| GAIL gas take-or-pay dispute | **Amount not quantified** | NOT FOUND IN DOCUMENT | Settlement Advisory Committee process ongoing |

Sum of quantified items excluding the contra department-appeal line and the
unquantified GAIL matter: ₹5.16 + 7.67 + 3.40 + 12.78 = **₹29.01 Cr**.
Against Total Equity (net worth) of ₹137.02 Cr (Balance Sheet, p.75), this
is **≈21.2% of net worth**. No single quantified item exceeds 10% of net
worth individually (largest is the civil/labour bucket at ₹12.78 Cr ≈ 9.3%
of net worth), but the aggregate is significant, and the GAIL matter is a
wholly unquantified open exposure. 🟡 Watch — see Pass 1 Summary #8.

Income Tax/Sales Tax assessment items (a)-(h): multiple AY additions under
appeal (AY2013-14, 2019-20, 2021-22, 2022-23), most stated to have been
adjusted against carried-forward losses; company "quite confident" of
favourable outcomes; ITAT appeal pending for AY2017-18 where CIT(A) had
already ruled in company's favour and revenue has appealed further. 🟢
Routine tax litigation for a company of this vintage, adequately narrated.

### Item 3 — Segmental Reporting (p.91)
Single segment (Steel); Ind AS 108 disclosure exemption claimed. 🟢

### Item 4 — Foreign Currency Transactions (p.91)
Expenditure in FX: Raw material (CIF) ₹27,99,00,589 (₹27.99 Cr) vs PY
₹58,54,21,625 (₹58.54 Cr) — down 52.2%; Capital Goods (CIF) ₹64,76,985
(₹0.65 Cr) vs NIL PY; Stores (CIF) ₹79,08,506 (₹0.79 Cr) vs ₹1,10,60,294
PY. Earnings in FX (exports): **NIL both years** — the company has zero
export revenue, entirely domestic sales. No hedging activity disclosed
(consistent with the Corporate Governance Report's blanket "no FX risk"
statement, p.60), despite genuine unhedged import exposure (~7% of raw
material imported this year per the consumption table, down from 16% PY).
🟡 Watch — unhedged FX exposure on ~₹28-30 Cr of annual imports is a real,
if modest, risk not actively managed per the company's own disclosure.

### Item 5 — Payment to Auditors (p.91)
Audit Fee ₹4,00,000 flat both years; Certification Fees ₹2,00,000 vs
₹92,000 PY (+117%). 🟢 Minor, routine.

### Item 6 — Debtors/Advances/Creditors Confirmation (p.91)
"Sundry debtors, advances, creditors & other liabilities include inter
parties transfers and are subject to confirmation and consequent
adjustments. In the opinion of the Board of Directors, the current assets
and loans & advances except doubtful in nature would realize at least the
amount at which these are stated in the Balance Sheet. For doubtful debts,
the Board of Directors is very much hopeful for their recovery. Therefore,
no provision during the year has been made." 🟡 Watch — this is a soft,
subjective management assertion standing in place of a hard ECL calculation
for a category the company itself flags as "doubtful," and it is used to
justify **not** providing for identified doubtful balances. Combined with
the sharp receivables growth (Note 7) and the partial non-provisioning
identified in Note 5, this pattern of management optimism substituting for
quantified provisioning is a recurring theme across the notes.

### Item 7 — Interest/Penalty on Delayed Statutory Dues (p.92)
Not provided; to be recognized when ascertained by the authority. 🟢
Standard.

### Item 8 — MSME Status of Creditors (p.92)
**"The MSME status of creditors is not in knowledge of the Company as per
available records even after adequate efforts."** 🔴 Red Flag — the company
is stating outright that it cannot determine which of its trade creditors
are registered MSME suppliers, meaning the mandatory Schedule III MSME
ageing/interest disclosure (shown as "N.A." across all buckets in the Trade
Payables Ageing Schedule, item 13 below) is not a genuine "no MSME dues"
position but an unresolved data/compliance gap. This creates unquantified
risk of undisclosed/unrecognized interest liability under the MSMED Act,
2006, and is itself a disclosure-quality and internal-controls concern for
a listed company. See Pass 1 Summary #7.

### Item 9 — Direct Charging Method Adopted (p.92)
"The Company during the period under report adopted direct charging method
to manufacture the products from billets in order to save on net energy
costs (power & fuel)/yield/other expenses etc." No quantified P&L savings
given (NOT FOUND IN DOCUMENT). Cross-references Director's Report (p.16):
"Implementing Direct Charging of Steel Billets into rolled products. The
said technology is one of its unique kind for Stainless Steel Rolled
Products in long segment." 🟢/🟡 — a genuine operational initiative,
plausibly linked to the Power & Fuel expense decline in Note 26, but
unquantified.

### Item 10 — Working Capital and Term Loan from Kotak Mahindra Bank (p.92)
Cross-referenced above under Notes 13/16 — new borrowing relationship
established this year; company "exploring various other financing options
with prospective Lenders." 🟡 Watch (cross-ref).

### Item 11 — Earnings Per Share (p.92)
Basic EPS ₹1.62 (FY25) vs ₹2.77 (FY24) — **down 41.5%**, tracking the PAT
decline (₹1,395.43 Lakh vs ₹2,353.40 Lakh, -40.7%) despite flat revenue.
Diluted EPS ₹1.62 (FY25, effectively no dilution gap this year — basic =
diluted) vs ₹2.73 (FY24, a small ~1.4% dilution gap from outstanding
OCRPS). "Cash EPS" also disclosed: ₹2.72 vs ₹3.79. 🟡 Watch — the sharp
YoY EPS decline, on flat revenue, directly reflects the margin
compression and finance-cost increase discussed above; also worth noting
given the significant equity issuance during the year (Note 11) that the
weighted-average share count grew (8,50,63,003 → 8,63,63,004), a modest
additional drag on per-share metrics independent of profitability.

### Item 12 — Related Party Disclosure (p.92)
- **Related Party (individual):** 1. Smt Sushila Rathi — relationship to
  the company/promoter group not stated in this note (NOT FOUND IN
  DOCUMENT; the surname strongly implies promoter-family linkage given
  Pradeep Kumar Rathi and Udit Rathi are named promoters/directors
  elsewhere, but the note itself gives no "relationship" column, unlike a
  standard Ind AS 24 table).
- **Key Managerial Personnel:** Shri P.N. Varshney, Smt Shobhita Singh, Shri
  Rakesh Kumar, Shri Rajeev Kumar, Rajesh Khurana, Abhishek Verma.
- **Transactions:** KMP Remuneration ₹14,06,797 (Individual-Related Party:
  NIL); Rent Paid to Individual-Related Party ₹9,60,000 (KMP: NIL).
- **No prior-year comparative figures are given in this transactions
  table** — Ind AS 24 requires comparatives; their absence here is a
  disclosure gap (NOT FOUND IN DOCUMENT for FY24 RPT amounts).
- No RPT balance-sheet disclosure (outstanding loans/advances/guarantees to
  or from related parties) beyond the blanket "NIL" at item 14 below.
🟡 Watch — RPT disclosure here is thin relative to Ind AS 24 norms (missing
relationship description, missing prior-year comparatives) even though the
absolute rupee amounts involved (₹14.07 Lakh remuneration, ₹9.6 Lakh rent)
are individually small. See Pass 1 Summary #10 (bundled with other
disclosure gaps).

### Trade Payables Ageing Schedule (p.92-93)
FY25: Less than 1 year ₹8,10,32,398; 1-2 years ₹1,19,81,561; 2-3 years
₹12,99,725; More than 3 years ₹7,07,426. MSME: N.A. across all buckets both
current and prior year (see Item 8 red flag above — this "N.A." reflects an
unknown/unresolved status, not a confirmed absence of MSME dues). FY24
footnote: of ₹2,20,66,960 of disputed dues, ₹1,11,94,145 (50.7%) has since
been settled — a positive resolution data point.

### Item 13 — Trade Receivable Ageing Schedule (p.93)
FY25: Undisputed-Considered Good <6 months ₹24,76,55,571; 6mo-1yr ₹2,000;
1-2yr ₹4,68,337; Undisputed-Considered Doubtful 6mo-1yr ₹37,688, 1-2yr
₹28,425; Disputed-Considered Doubtful >3yr ₹97,51,973 (shown separately
under Note 5, Other Non-Current Assets, per the footnote). Total (current
book) ties to Note 7's ₹2,477.43 Lakh. FY24 comparative shows a materially
different ageing profile (₹1,46,511,947 <6mo, ₹1,27,29,043 in the 6mo-1yr
bucket) — the near-total collapse of the 6mo-1yr bucket in FY25 combined
with the receivables growth overall is consistent with, not contradictory
to, the Red Flag already raised at Note 7. 🔴 Red Flag (cross-ref Note 7).

### Item 14 — Loans/Advances to Directors/KMP/Related Parties (p.93)
NIL. 🟢

### Item 15 — Capital Work-in-Progress (p.93)
₹6,26,72,040 — ties to Balance Sheet CWIP of ₹626.72 Lakh (p.75, up from
₹0.00 PY, consistent with the ongoing capex programme). 🟢 Tie-out
confirmed, no CWIP ageing schedule provided (Schedule III technically
requires a CWIP ageing table for amounts outstanding — NOT FOUND IN
DOCUMENT as a formal ageing schedule, only the single aggregate figure).
🟡 Watch — minor Schedule III completeness gap.

### Item 16 — Intangible Assets Under Development (p.93)
NIL. 🟢

### Item 17 — Solvency Ratio Analysis (p.93)
| Ratio | FY25 | FY24 | Company's stated explanation |
|---|---|---|---|
| Current Ratio | 0.80 | 0.97 | "Increase in current liability" |
| Debt-Equity Ratio | 0.28 | ~0.00 | "Working capital availed from bank" |
| Debt Service Coverage Ratio | 0.23 | 0.46 | "Working capital availed from bank" |
| Return on Equity | 0.10 (10%) | 0.19 (19%) | "Increase in Shareholders Nos" |
| Inventory Turnover Ratio | 11.95 | 14.58 | "Better inventory management" |
| Trade Receivables Turnover Ratio | 24.52 | 40.50 | "Better collection from customers" |
| Trade Payables Turnover Ratio | 4.85 | 5.72 | "Better in payments to vendors" |
| Net Capital Turnover Ratio | -20.82 | -249.39 | "Increase in current liabilities" |
| Net Profit Ratio | 0.03 (3%) | 0.05 (5%) | "Lower price in steel market" |
| Return on Capital Employed | 0.13 | 0.28 | "Lower margin in revenue" |
| Return on Investment | 98 | 102 | "Increase in Market Value" |

**Every efficiency and returns ratio deteriorated year-on-year (current
ratio below 1.0x in both years; DSCR below 0.5x in both years, meaning
operating cash generation does not even cover one year of debt service
once), while three of the company's own plain-English explanations for
Inventory Turnover, Receivables Turnover and Trade Payables Turnover are
worded as if performance improved ("Better inventory management," "Better
collection from customers," "Better in payments to vendors") — the exact
opposite of what each ratio's decline actually indicates.** 🔴 Red Flag —
this is either a templating/copy-paste error in the disclosure or a
genuine mischaracterization of deteriorating metrics as improvements; either
way it is a disclosure-integrity concern deserving a direct management
question. See Pass 1 Summary #4.

### Item 18 — Surety Given for Others (p.93)
"Surety given for others, amount not ascertained as company has not
maintained any such records." NOT FOUND IN DOCUMENT (amount). 🟡 Watch —
another instance (alongside the MSME status gap) of the company disclosing
that it does not maintain records sufficient to quantify a required
disclosure.

### Item 19 — Dividend on Preference Shares (p.93)
No dividend paid on non-cumulative preference shares during the year. 🟢
(Consistent with the 1% non-cumulative coupon terms in Note 11 — forgone
dividends on non-cumulative shares are not a future liability.)

### Item 20 — Second-Hand Vehicles (p.94)
Covered above under PPE Note 2 — three vehicles' registration not yet
transferred to the company's name despite depreciation being charged. 🟡
Watch.

### Item 21 — Stores Consumed (p.94)
Stores consumed includes value of stores issued for repair and maintenance.
🟢 Accounting-policy clarification, immaterial.

### Item 22 — Regrouping/Recast of Prior-Year Figures (p.94)
"Previous year figures have been regrouped or recast wherever necessary."
**No specifics given on what was regrouped or why** (NOT FOUND IN
DOCUMENT). 🟡 Watch — boilerplate regrouping language without detail
prevents verification of whether any prior-year reclassification affected
comparability of the ratios/trends analyzed above (e.g., the Finance Cost
composition flip in Note 25, or the Other Current Liabilities collapse in
Note 18, could in principle be partly regrouping-driven rather than
purely operational — this cannot be confirmed or ruled out from the
document as written).

---

## PASS 1 SUMMARY — TOP 10 MOST SIGNIFICANT FINDINGS

Ranked by investor importance.

1. **🔴 Operating cash flow negative (₹11.06 Cr outflow) despite positive
   reported PAT (₹13.95 Cr)** — working-capital driven (inventory +₹20.50
   Cr, receivables +₹8.51 Cr), a classic profit-versus-cash divergence.
   (Cash Flow Statement, p.85; cross-ref Notes 6, 7, 23.)

2. **🔴 Finished-goods inventory grew 145.9% (₹14.0 Cr → ₹34.4 Cr) against
   ~2% revenue growth**, mechanically producing a ₹29.7 Cr favourable swing
   in the P&L's "Changes in Inventory" line year-on-year, with no
   write-down/obsolescence disclosure. (Note 6, p.78; Note 23, p.83.)

3. **🔴 Reported profit in both FY24 and FY25 is substantially inflated by
   large, non-repeating exceptional items of different character each
   year** — a ₹19.84 Cr lender loan-waiver in FY24 and a ₹4.71 Cr
   electricity-duty refund in FY25; pre-exceptional profit was only ₹3.77
   Cr (FY24) and ₹9.24 Cr (FY25). (Note 27, p.84.)

4. **🔴 The company's own Solvency Ratio note describes deteriorating
   metrics (receivables turnover, inventory turnover, payables turnover)
   using improvement language ("better collection," "better inventory
   management," "better in payments to vendors") that contradicts the
   actual ratio movement**, alongside a current ratio and DSCR both below
   1.0x in both years. (Notes on Accounts item 17, p.93.)

5. **🔴 Trade receivables rose 52.3% (₹16.3 Cr → ₹24.8 Cr) against 2%
   revenue growth; receivables turnover fell from 40.50x to 24.52x.** (Note
   7, p.78; ageing schedule item 13, p.93.)

6. **🟡 Deferred Tax Asset of ₹72.91 Cr sits static, unchanged for two
   years, on a balance sheet where the accounting policy explicitly states
   deferred tax is not being calculated due to accumulated losses; no
   composition, reconciliation, or realizability reassessment is
   disclosed anywhere.** (Note 2(m), p.89; Balance Sheet, p.75.)

7. **🟡 Fresh re-leveraging: total disclosed borrowings jumped from ₹0.00 to
   ₹37.74 Cr in one year** (working capital facility + term loan from Kotak
   Mahindra Bank), funding a ₹22.6 Cr capex programme and working-capital
   build, with DSCR nearly halving to 0.23x. (Notes 13 & 16, p.82; Notes on
   Accounts item 10, p.92.)

8. **🔴 Company discloses it does not know the MSME status of its trade
   creditors "even after adequate efforts,"** making the mandatory MSME
   ageing disclosure (shown as "N.A." throughout) an unresolved compliance
   gap rather than a confirmed nil position, with unquantified risk of
   undisclosed MSMED Act interest liability. (Notes on Accounts item 8,
   p.92.)

9. **🟡 Contingent liabilities of approximately ₹29.0 Cr (≈21.2% of net
   worth) across VAT/sales tax, excise/service tax, GST and civil/labour
   disputes, plus a wholly unquantified GAIL gas take-or-pay dispute.**
   (Notes on Accounts item 2, p.89-91.)

10. **🟡 Net worth's recovery from -₹100.4 Cr (FY23) to +₹41.8 Cr (FY25) is
    driven substantially by lender debt-waivers (₹12.8 Cr) and large
    equity/OCRPS capital raises (~₹114.7 Cr preferential issue in FY24)
    rather than organic profit accumulation; the accumulated deficit
    (Retained Earnings) remains -₹319.7 Cr.** (Note 12, p.81; Auditor's
    Annexure-A item 10, p.71.)

**Additional cross-cutting disclosure-quality observations not in the top
10 but noted for Pass 2/3 attention:** no Ind AS 19 actuarial disclosure for
the ₹2.07 Cr gratuity provision; no Ind AS 107 financial-instruments/risk-
management note anywhere in the AR; Related Party Transactions table omits
prior-year comparatives and relationship descriptions; Finance Cost
composition flips almost entirely between "Interest on Loans" and "Bank
Charges" across the two years with no explanatory cross-reference; Legal &
Professional Charges more than doubled (+128.9%) unexplained; and the
document itself is mislabeled in the pipeline as a "FY2023" annual report
when it is in fact the FY2024-25 (54th) Annual Report — a metadata
correction needed upstream of this stage.
